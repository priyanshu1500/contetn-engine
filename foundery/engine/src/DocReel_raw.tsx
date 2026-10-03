import React, { useEffect, useState } from 'react';
import {
  AbsoluteFill, Sequence, OffthreadVideo, Img, staticFile, useCurrentFrame,
  interpolate, delayRender, continueRender, useVideoConfig,
} from 'remotion';
import edl from './edl_v10.json';
import { theme, f } from './theme';

const clamp = { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' } as const;
const shots: any[] = edl.shots as any[];

/* ---------- fonts ---------- */
const useFonts = () => {
  const [handle] = useState(() => delayRender('fonts'));
  useEffect(() => {
    const defs: [string, string, string, string][] = [
      ['Newsreader', 'newsreader-400.woff2', '400', 'normal'],
      ['Newsreader', 'newsreader-600.woff2', '600', 'normal'],
      ['Newsreader', 'newsreader-400-italic.woff2', '400', 'italic'],
      ['Newsreader', 'newsreader-600-italic.woff2', '600', 'italic'],
      ['Inter', 'inter-500.woff2', '500', 'normal'],
      ['Inter', 'inter-600.woff2', '600', 'normal'],
      ['Inter', 'inter-700.woff2', '700', 'normal'],
    ];
    Promise.all(defs.map(([fam, file, w, st]) => {
      const ff = new FontFace(fam, `url(${staticFile(file)})`, { weight: w, style: st });
      return ff.load().then((l) => { (document as any).fonts.add(l); });
    })).then(() => continueRender(handle)).catch(() => continueRender(handle));
  }, [handle]);
};

const seedOf = (id: string) => ([...id].reduce((a, c) => (a * 31 + c.charCodeAt(0)) | 0, 7) % 100) / 10;
const rnd = (i: number) => { const x = Math.sin(i * 12.9898) * 43758.5453; return x - Math.floor(x); };

/* previous shot's drift direction (for whip continuity) */
const prevDir = (id: string): 'L' | 'R' => {
  const i = shots.findIndex((s) => s.id === id);
  for (let k = i - 1; k >= 0; k--) if (shots[k].dir) return shots[k].dir;
  return 'R';
};

/* ---------- FullBleedClip: handheld drift, lens breathing, whip-in, rack focus ---------- */
const Media: React.FC<{ shot: any; dur: number }> = ({ shot, dur }) => {
  const frame = useCurrentFrame();
  const sd = seedOf(shot.id);
  const p = interpolate(frame, [0, dur], [0, 1], clamp);
  const e = theme.easeOut(p);
  const sign = shot.dir === 'L' ? -1 : 1;
  const dx = sign * p * 14 + 5 * Math.sin(frame / 13 + sd) + 3 * Math.sin(frame / 5.1 + sd * 2);
  const dy = 4 * Math.sin(frame / 11 + sd * 3) + 2 * Math.sin(frame / 4.3 + sd);
  const rot = 0.12 * Math.sin(frame / 19 + sd);
  const breath = 1 + 0.004 * Math.sin(frame / 9 + sd);
  const scale = (1.035 + (shot.push ?? 0.05) * e) * (shot.zoom ?? 1) * breath;

  let whipX = 0; let blur = 0; let rackScale = 1;
  if (shot.whip) {
    const w = theme.easeOut(interpolate(frame, [0, 5], [0, 1], clamp));
    const from = prevDir(shot.id) === 'R' ? -300 : 300;
    whipX = from * (1 - w);
    blur = 18 * (1 - w);
    rackScale = 1 + 0.14 * (1 - w);
  }
  if (shot.rack) {
    const r = theme.easeOut(interpolate(frame, [0, 10], [0, 1], clamp));
    blur = Math.max(blur, 14 * (1 - r));
    rackScale = Math.max(rackScale, 1.03 - 0.03 * r);
  }
  const duo = shot.duotone ? 'grayscale(1) contrast(1.28) brightness(0.92)' : '';
  const filter = `${duo} ${blur > 0.3 ? `blur(${blur}px)` : ''}`.trim() || undefined;
  const style: React.CSSProperties = {
    width: '100%', height: '100%', objectFit: 'cover', filter,
    transform: `translate(${dx + whipX}px,${dy}px) rotate(${rot}deg) scale(${scale * rackScale})`,
  };
  if (shot.kind === 'video') {
    return <><OffthreadVideo src={staticFile(shot.src)} startFrom={f(shot.from ?? 0)} muted style={style} /><FootageFinish /></>;
  }
  if (shot.kind === 'still') {
    const ox = `${(shot.fx ?? 0.5) * 100}% ${(shot.fy ?? 0.5) * 100}%`;
    return <><Img src={staticFile(shot.src)} style={{ ...style, objectPosition: ox, transformOrigin: ox }} /><FootageFinish /></>;
  }
  return null;
};

/* light finish on footage only: soft vignette + fine grain (cards stay crisp) */
const FootageFinish: React.FC = () => {
  const frame = useCurrentFrame();
  const gx = (frame * 53) % 240, gy = (frame * 97) % 240;
  return (
    <>
      <AbsoluteFill style={{ background: 'radial-gradient(ellipse at 50% 50%, rgba(0,0,0,0) 62%, rgba(0,0,0,0.20) 100%)' }} />
      <AbsoluteFill style={{ backgroundImage: `url("data:image/svg+xml,${grainSvg}")`, backgroundPosition: `${gx}px ${gy}px`, opacity: 0.07, mixBlendMode: 'overlay' }} />
    </>
  );
};

/* ---------- small controlled imperfections ---------- */
let SPECKS_ON = true;
const Specks: React.FC<{ n?: number; dark?: boolean }> = ({ n = 26, dark = true }) => {
  const frame = useCurrentFrame();
  if (!SPECKS_ON) return null;
  return (
    <AbsoluteFill>
      {Array.from({ length: n }).map((_, i) => {
        const x = rnd(i + 1) * 100, y = rnd(i + 50) * 100, s = 2 + rnd(i + 90) * 4;
        const flick = 0.35 + 0.25 * Math.sin(frame / (6 + (i % 5)) + i);
        return <div key={i} style={{ position: 'absolute', left: `${x}%`, top: `${y + Math.sin(frame / 40 + i) * 0.2}%`, width: s, height: s, borderRadius: '50%', background: dark ? `rgba(40,28,16,${flick})` : `rgba(255,255,255,${flick * 0.7})` }} />;
      })}
    </AbsoluteFill>
  );
};

const Paper: React.FC = () => (
  <AbsoluteFill style={{ background: theme.paper }}>
    <AbsoluteFill style={{ backgroundImage: `url(${staticFile('img/paper.png')})`, backgroundSize: '316px 288px', opacity: 0.85, mixBlendMode: 'multiply' }} />
    <AbsoluteFill style={{ background: 'radial-gradient(ellipse at 50% 45%, rgba(255,255,255,0.35) 0%, rgba(120,90,50,0.28) 100%)' }} />
    <Specks />
  </AbsoluteFill>
);

const numeralStyle = (size: number, color: string): React.CSSProperties => ({
  fontFamily: theme.serif, fontWeight: 600, fontStyle: 'italic', fontSize: size, color, lineHeight: 1, letterSpacing: '-0.02em',
});

const pop = (frame: number, start: number, dur = 8) => {
  const p = interpolate(frame, [start, start + dur], [0, 1], { ...clamp, easing: theme.easeBack });
  return { p, opacity: interpolate(frame, [start, start + 4], [0, 1], clamp), y: (1 - p) * 34, s: 0.86 + 0.14 * p };
};

/* Card: 1-2-3 counter (numeral sits right of centre; caption owns the lower-left) */
const CountCard: React.FC<{ t0: number }> = ({ t0 }) => {
  const frame = useCurrentFrame() + f(t0);
  const ticks = [5.5, 5.8, 6.1];
  const idx = ticks.filter((t) => frame >= f(t)).length - 1;
  const a = pop(frame, idx >= 0 ? f(ticks[idx]) : 0, 7);
  const exit = interpolate(frame, [f(7.02), f(7.2)], [1, 0], clamp);
  const breathe = 1 + 0.008 * Math.sin(frame / 5);
  return (
    <AbsoluteFill>
      <Paper />
      {idx >= 0 && (
        <AbsoluteFill style={{ alignItems: 'flex-end', justifyContent: 'center', paddingRight: 210, paddingBottom: 60, opacity: exit }}>
          <div style={{ ...numeralStyle(idx === 2 ? 720 : 620, idx === 2 ? theme.oxblood : theme.ink), opacity: a.opacity, transform: `translateY(${a.y}px) scale(${a.s * breathe})` }}>{idx + 1}</div>
        </AbsoluteFill>
      )}
    </AbsoluteFill>
  );
};

/* Card: 2015 (offset upper-left, small label under it) */
const YearCard: React.FC<{ t0: number; rack?: boolean }> = ({ t0, rack }) => {
  const local = useCurrentFrame();
  const frame = local + f(t0);
  const a = pop(frame, f(12.8), 9);
  const drift = interpolate(frame, [f(12.58), f(13.3)], [0, 1], clamp);
  const blur = rack ? 14 * (1 - theme.easeOut(interpolate(local, [0, 10], [0, 1], clamp))) : 0;
  return (
    <AbsoluteFill style={{ filter: blur > 0.3 ? `blur(${blur}px)` : undefined }}>
      <Paper />
      <AbsoluteFill style={{ justifyContent: 'center', paddingLeft: 200 }}>
        <div style={{ ...numeralStyle(460, theme.ink), fontVariantNumeric: 'tabular-nums', opacity: a.opacity, transform: `translateY(${a.y - drift * 10}px) scale(${a.s * (1 + 0.03 * drift)})`, transformOrigin: '0 50%' }}>{Math.round(interpolate(frame, [f(12.8), f(13.3)], [1995, 2015], { ...clamp, easing: theme.easeOut }))}</div>
        <div style={{ marginLeft: 12, marginTop: 8, fontFamily: theme.sans, fontWeight: 600, fontSize: 30, letterSpacing: '0.22em', color: theme.oxblood, opacity: interpolate(frame, [f(13.0), f(13.15)], [0, 1], clamp) }}>OPENAI IS FOUNDED</div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* Black title card: label above, hero below, left-offset */
const TitleBlack: React.FC<{ t0: number; id: string }> = ({ t0, id }) => {
  const frame = useCurrentFrame() + f(t0);
  if (id !== 's11') return (
    <AbsoluteFill style={{ background: '#040405' }} />
  );
  const a = pop(frame, f(9.32), 9);
  const b = pop(frame, f(9.76), 9);
  return (
    <AbsoluteFill style={{ background: '#040405', justifyContent: 'center', paddingLeft: 240 }}>
      <div style={{ fontFamily: theme.sans, fontWeight: 600, fontSize: 44, letterSpacing: '0.32em', textTransform: 'uppercase', color: theme.cream, opacity: a.opacity, transform: `translateY(${a.y}px)` }}>Play</div>
      <div style={{ ...numeralStyle(440, theme.gold), opacity: b.opacity, transform: `translateY(${b.y}px) scale(${b.s})`, transformOrigin: '0 50%', marginTop: -30 }}>01</div>
    </AbsoluteFill>
  );
};

/* Title on paper: label above, oxblood numeral below */
const TitlePaper: React.FC<{ t0: number }> = ({ t0 }) => {
  const frame = useCurrentFrame() + f(t0);
  const a = pop(frame, f(9.32), 9);
  const b = pop(frame, f(9.76), 9);
  return (
    <AbsoluteFill>
      <Paper />
      <AbsoluteFill style={{ justifyContent: 'center', paddingLeft: 240 }}>
        <div style={{ fontFamily: theme.sans, fontWeight: 600, fontSize: 44, letterSpacing: '0.32em', textTransform: 'uppercase', color: theme.ink, opacity: a.opacity, transform: `translateY(${a.y}px)` }}>Play</div>
        <div style={{ ...numeralStyle(440, theme.oxblood), opacity: b.opacity, transform: `translateY(${b.y}px) scale(${b.s})`, transformOrigin: '0 50%', marginTop: -30 }}>01</div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* Word-by-word caption: centred lower third, 1-2 words at a time, one typeface (serif), italic gold for emphasis */
const WordCap: React.FC<{ c: any }> = ({ c }) => {
  const frame = useCurrentFrame();
  const g = frame + f(c.t0);
  const ink = !!c.ink;
  const words = (c.words as any[]).filter((w) => g >= f(w.t) - 1);
  return (
    <AbsoluteFill style={{ justifyContent: 'flex-end', alignItems: 'center', paddingBottom: c.pad ?? 250 }}>
      <div style={{ display: 'flex', gap: 22, alignItems: 'baseline' }}>
        {words.map((w, i) => {
          const a = pop(g, f(w.t) - 1, 6);
          const em = !!w.em;
          return (
            <span key={i} style={{
              fontFamily: theme.serif, fontStyle: em ? 'italic' : 'normal', fontWeight: 600, fontSize: em ? 104 : 88, lineHeight: 1.05,
              color: em ? (ink ? theme.oxblood : theme.gold) : ink ? theme.ink : theme.cream,
              textShadow: ink ? 'none' : '0 3px 26px rgba(0,0,0,0.85), 0 1px 3px rgba(0,0,0,0.6)',
              opacity: a.opacity, transform: `translateY(${a.y * 0.6}px) scale(${a.s})`, display: 'inline-block',
            }}>{w.w}</span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- generic cards for the full build ---------- */
const DarkBg: React.FC = () => (
  <AbsoluteFill style={{ background: '#0B0A09' }}>
    <AbsoluteFill style={{ background: 'radial-gradient(ellipse at 50% 45%, rgba(70,55,35,0.35) 0%, rgba(5,5,5,0.9) 85%)' }} />
  </AbsoluteFill>
);

/* rolling-money / number counter: shot.stat = {prefix,to,from,suffix,roll:[a,b],style:'paper'|'dark'} */
const StatCard: React.FC<{ t0: number; shot: any }> = ({ t0, shot }) => {
  const g = useCurrentFrame() + f(t0);
  const st = shot.stat;
  const dark = st.style === 'dark';
  const val = Math.round(interpolate(g, [f(st.roll[0]), f(st.roll[1])], [st.from ?? 0, st.to], { ...clamp, easing: theme.easeOut }));
  const a = pop(g, f(st.roll[0]) - 1, 9);
  const dt = g - f(st.roll[1]);
  const settle = dt >= 0 ? 1 + 0.03 * Math.sin(dt / 3) * Math.exp(-dt / 6) : 1;
  const col = dark ? theme.gold : theme.oxblood;
  return (
    <AbsoluteFill>
      {dark ? <DarkBg /> : <Paper />}
      <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', opacity: a.opacity, transform: `translateY(${a.y}px) scale(${a.s * settle})` }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 26 }}>
          <div style={{ ...numeralStyle(400, col), fontVariantNumeric: 'tabular-nums' }}>{st.prefix ?? ''}{val.toLocaleString('en-US')}</div>
          {st.suffix && <div style={{ fontFamily: theme.serif, fontWeight: 600, fontSize: 150, color: dark ? theme.cream : theme.ink }}>{st.suffix}</div>}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* year counter: shot.year = {from,to,roll:[a,b],label} */
const YearGen: React.FC<{ t0: number; shot: any }> = ({ t0, shot }) => {
  const g = useCurrentFrame() + f(t0);
  const y = shot.year;
  const a = pop(g, f(y.roll[0]) - 1, 9);
  const v = Math.round(interpolate(g, [f(y.roll[0]), f(y.roll[1])], [y.from, y.to], { ...clamp, easing: theme.easeOut }));
  return (
    <AbsoluteFill>
      <Paper />
      <AbsoluteFill style={{ justifyContent: 'center', paddingLeft: 200 }}>
        <div style={{ ...numeralStyle(460, theme.ink), fontVariantNumeric: 'tabular-nums', opacity: a.opacity, transform: `translateY(${a.y}px) scale(${a.s})`, transformOrigin: '0 50%' }}>{v}</div>
        {y.label && <div style={{ marginLeft: 12, marginTop: 8, fontFamily: theme.sans, fontWeight: 600, fontSize: 30, letterSpacing: '0.22em', color: theme.oxblood, opacity: interpolate(g, [f(y.roll[1]), f(y.roll[1]) + 4], [0, 1], clamp) }}>{y.label}</div>}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* chapter title: shot.title = {label:'PLAY', num:'02', pop:[a,b]} */
const TitleGen: React.FC<{ t0: number; shot: any }> = ({ t0, shot }) => {
  const g = useCurrentFrame() + f(t0);
  const t = shot.title;
  const a = pop(g, f(t.pop[0]), 9);
  const b = pop(g, f(t.pop[1]), 9);
  return (
    <AbsoluteFill>
      <Paper />
      <AbsoluteFill style={{ justifyContent: 'center', paddingLeft: 240 }}>
        <div style={{ fontFamily: theme.sans, fontWeight: 600, fontSize: 44, letterSpacing: '0.32em', textTransform: 'uppercase', color: theme.ink, opacity: a.opacity, transform: `translateY(${a.y}px)` }}>{t.label}</div>
        <div style={{ ...numeralStyle(440, theme.oxblood), opacity: b.opacity, transform: `translateY(${b.y}px) scale(${b.s})`, transformOrigin: '0 50%', marginTop: -30 }}>{t.num}</div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* single big word card: shot.wordcard = {text, sub?, pop, style} */
const WordCard: React.FC<{ t0: number; shot: any }> = ({ t0, shot }) => {
  const g = useCurrentFrame() + f(t0);
  const w = shot.wordcard;
  const dark = w.style === 'dark';
  const a = pop(g, f(w.pop), 10);
  return (
    <AbsoluteFill>
      {dark ? <DarkBg /> : <Paper />}
      <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', opacity: a.opacity, transform: `translateY(${a.y}px) scale(${a.s})` }}>
        <div style={{ ...numeralStyle(w.size ?? 420, dark ? theme.gold : theme.oxblood) }}>{w.text}</div>
        {w.sub && <div style={{ fontFamily: theme.serif, fontStyle: 'italic', fontWeight: 600, fontSize: 96, color: dark ? theme.cream : theme.ink, marginTop: 10 }}>{w.sub}</div>}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* call-to-action end card: shot.cta = {kicker,hero,line,pop:[a,b,c]} */
const EndCard: React.FC<{ t0: number; shot: any }> = ({ t0, shot }) => {
  const g = useCurrentFrame() + f(t0);
  const c = shot.cta;
  const a = pop(g, f(c.pop[0]), 9), b = pop(g, f(c.pop[1]), 11), l = pop(g, f(c.pop[2]), 9);
  return (
    <AbsoluteFill>
      <Paper />
      <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
        <div style={{ fontFamily: theme.sans, fontWeight: 600, fontSize: 48, letterSpacing: '0.34em', textTransform: 'uppercase', color: theme.ink, opacity: a.opacity, transform: `translateY(${a.y}px)` }}>{c.kicker}</div>
        <div style={{ ...numeralStyle(330, theme.oxblood), opacity: b.opacity, transform: `translateY(${b.y}px) scale(${b.s})`, margin: '6px 0 14px' }}>{c.hero}</div>
        <div style={{ fontFamily: theme.serif, fontWeight: 600, fontSize: 64, color: theme.ink, textAlign: 'center', maxWidth: 1500, opacity: l.opacity, transform: `translateY(${l.y}px)` }}>{c.line}</div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const FadeBlack: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  return <AbsoluteFill style={{ background: '#000', opacity: interpolate(frame, [0, durationInFrames - 1], [0, 1], clamp) }} />;
};

/* ---------- EvidenceCard: torn-edge sheet on a desk, highlighter sweep, marker circle ---------- */
const CARD_W = 760, CARD_H = 430;
const tornClip = (() => {
  const pts: string[] = ['0% 0%', '100% 0%'];
  const n = 46;
  for (let i = 0; i <= n; i++) {
    const x = 100 - (i / n) * 100;
    const y = 96.2 + rnd(i + 7) * 3.4 - (i % 3 === 0 ? 1.2 : 0);
    pts.push(`${x.toFixed(2)}% ${y.toFixed(2)}%`);
  }
  return `polygon(${pts.join(',')})`;
})();

const EvidenceCard: React.FC<{ t0: number; dur: number; shot: any }> = ({ t0, dur, shot }) => {
  const local = useCurrentFrame();
  const g = local + f(t0);
  const p = interpolate(local, [0, dur], [0, 1], clamp);
  const enter = theme.easeOut(interpolate(local, [0, 9], [0, 1], clamp));
  const S = (shot.scale ?? 1.72) + 0.06 * p;
  const rot = -1.2 - 1.6 * (1 - enter);
  const ty = (shot.pos?.[1] ?? 64) + 70 * (1 - enter);
  const blur = shot.rack ? 12 * (1 - enter) : 0;
  const SW = shot.sweep ?? [10.46, 10.78]; const CI = shot.circle ?? [10.94, 11.22]; const LB = shot.label ?? [10.42, 10.56];
  const sweep = interpolate(g, [f(SW[0]), f(SW[1])], [0, 1], { ...clamp, easing: theme.easeInOut });
  const circle = interpolate(g, [f(CI[0]), f(CI[1])], [1, 0], { ...clamp, easing: theme.easeInOut });
  const label = interpolate(g, [f(LB[0]), f(LB[1])], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ background: '#1b1613' }}>
      <AbsoluteFill style={{ background: 'radial-gradient(ellipse at 40% 35%, rgba(90,66,44,0.55) 0%, rgba(20,14,10,0.95) 85%)' }} />
      <AbsoluteFill style={{ backgroundImage: `url(${staticFile('img/paper.png')})`, backgroundSize: '316px 288px', opacity: 0.10, mixBlendMode: 'screen' }} />
      <Specks n={18} dark={false} />
      <div style={{ position: 'absolute', left: shot.pos?.[0] ?? 70, top: ty, width: CARD_W, height: CARD_H, transformOrigin: '0 0', transform: `rotate(${rot}deg) scale(${S})`, filter: `drop-shadow(0 26px 34px rgba(0,0,0,0.6)) ${blur > 0.3 ? `blur(${blur}px)` : ''}`, opacity: interpolate(local, [0, 4], [0, 1], clamp) }}>
        <div style={{ position: 'absolute', inset: 0, clipPath: tornClip, background: '#fff', overflow: 'hidden' }}>
          <Img src={staticFile(shot.src)} style={{ position: 'absolute', left: -570, top: -150, width: 1920, height: 1080 }} />
          {(shot.hl ?? [{ x: 128, y: 184, w: 84, h: 24, t: SW }]).map((h: any, i: number) => (<div key={i} style={{ position: 'absolute', left: h.x, top: h.y, width: h.w * interpolate(g, [f(h.t[0]), f(h.t[1])], [0, 1], { ...clamp, easing: theme.easeInOut }), height: h.h, background: 'rgba(255,214,64,0.92)', mixBlendMode: 'multiply' }} />))}
          <AbsoluteFill style={{ backgroundImage: `url(${staticFile('img/paper.png')})`, backgroundSize: '158px 144px', opacity: 0.22, mixBlendMode: 'multiply' }} />
          <div style={{ position: 'absolute', left: 0, right: 0, top: '54%', height: 3, background: 'linear-gradient(90deg, rgba(0,0,0,0.10), rgba(255,255,255,0.35) 50%, rgba(0,0,0,0.08))' }} />
          <div style={{ position: 'absolute', left: 0, right: 0, top: 0, height: 60, background: 'linear-gradient(rgba(0,0,0,0.10), rgba(0,0,0,0))' }} />
          {!shot.nocircle && <svg width={CARD_W} height={CARD_H} style={{ position: 'absolute', left: 0, top: 0 }}>
            <path d="M 112 205 C 105 180, 150 170, 185 172 C 225 174, 240 195, 225 210 C 205 226, 140 226, 118 208 C 108 199, 118 184, 150 178" pathLength={1} fill="none" stroke="#C1272D" strokeWidth={4.2} strokeLinecap="round" strokeDasharray={1} strokeDashoffset={circle} />
          </svg>}
        </div>
        {/* tape strip */}
        <div style={{ position: 'absolute', left: -12, top: -6, width: 96, height: 24, transform: 'rotate(-38deg)', background: 'linear-gradient(90deg, rgba(232,214,160,0.85), rgba(240,226,180,0.7))', boxShadow: '0 2px 4px rgba(0,0,0,0.3)' }} />
      </div>
      <div style={{ position: 'absolute', left: 84, bottom: 44, fontFamily: theme.sans, fontWeight: 500, fontSize: 26, letterSpacing: '0.16em', color: 'rgba(246,240,226,0.9)', opacity: label }}>
        {shot.source ?? 'SOURCE · OPENAI BLOG, 11 DEC 2015 · VIA WAYBACK MACHINE'}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Overlay with in/peak/out envelope ---------- */
const Overlay: React.FC<{ o: any }> = ({ o }) => {
  const frame = useCurrentFrame();
  const g = frame + f(o.t_in);
  const op = interpolate(g, [f(o.t_in), f(o.t_peak), f(o.t_out)], [0, o.peak, 0], { ...clamp, easing: theme.easeInOut });
  return (
    <AbsoluteFill style={{ mixBlendMode: o.blend, opacity: op }}>
      <OffthreadVideo src={staticFile(o.src)} startFrom={f(o.from ?? 0)} muted style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
    </AbsoluteFill>
  );
};

/* ---------- Typography: small supporting words + one hero word, off-centre ---------- */
const SMALL = 50, BIG = 150, EM = 170;
const Caption: React.FC<{ c: any }> = ({ c }) => {
  const frame = useCurrentFrame();
  const g = frame + f(c.t0);
  const dur = f(c.t1) - f(c.t0);
  const exit = interpolate(frame, [dur - 5, dur], [1, 0], clamp);
  const ink = !!c.ink;
  const shadow = ink ? 'none' : '0 3px 22px rgba(0,0,0,0.8), 0 1px 2px rgba(0,0,0,0.6)';
  const right = c.pos === 'r';
  const centre0 = c.pos === 'c';
  const words = (c.words as any[]).filter((w) => g >= f(w.t) - 1);
  const renderWord = (w: any, i: number) => {
    const a = pop(g, f(w.t) - 1, 8);
    const hero = w.em || w.big;
    const size = w.size ?? (w.em ? EM : w.big ? BIG : SMALL);
    return (
      <span key={i} style={{
        fontFamily: hero ? theme.serif : theme.sans, fontStyle: w.em ? 'italic' : 'normal',
        fontWeight: hero ? 600 : 600, fontSize: size, lineHeight: hero ? 1 : 1.2,
        color: w.em ? (ink ? theme.oxblood : theme.gold) : ink ? theme.ink : theme.cream,
        textShadow: shadow, opacity: a.opacity, transform: `translateY(${a.y}px) scale(${a.s})`, transformOrigin: centre0 ? '50% 100%' : right ? '100% 100%' : '0 100%',
        display: 'inline-block', letterSpacing: hero ? '-0.01em' : '0.01em',
      }}>{w.w}</span>
    );
  };
  const small = words.filter((w) => !(w.em || w.big));
  const heroes = words.filter((w) => w.em || w.big);
  const box: React.CSSProperties = {
    position: 'absolute', bottom: c.bottom ?? 120,
    ...(centre0 ? { left: 0, right: 0, justifyContent: 'center' } : { [right ? 'right' : 'left']: 140 }),
    display: 'flex', flexDirection: 'column', alignItems: centre0 ? 'center' : right ? 'flex-end' : 'flex-start', gap: 6, opacity: exit,
  };
  if (c.stack) {
    return (
      <AbsoluteFill>
        <div style={box}>
          {small.length > 0 && <div style={{ display: 'flex', gap: 20 }}>{small.map((w) => renderWord(w, (c.words as any[]).indexOf(w)))}</div>}
          {heroes.length > 0 && <div style={{ display: 'flex', gap: c.gap ?? 24 }}>{heroes.map((w) => renderWord(w, (c.words as any[]).indexOf(w)))}</div>}
        </div>
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill>
      <div style={{ ...box, flexDirection: 'row', alignItems: 'baseline', gap: 26 }}>{words.map((w) => renderWord(w, (c.words as any[]).indexOf(w)))}</div>
    </AbsoluteFill>
  );
};

/* Annotation: tiny source label with a rule (top-left) */
const Annotation: React.FC<{ a: any }> = ({ a }) => {
  const frame = useCurrentFrame();
  const dur = f(a.t1) - f(a.t0);
  const fd = Math.max(1, Math.min(6, Math.floor(dur / 3)));
  const op = interpolate(frame, [0, fd, dur - fd, dur], [0, 1, 1, 0], clamp);
  const rule = interpolate(frame, [0, 10], [0, 1], { ...clamp, easing: theme.easeOut });
  return (
    <AbsoluteFill style={{ opacity: op }}>
      <div style={{ position: 'absolute', [a.pos === 'br' ? 'right' : 'left']: 90, [a.pos === 'br' ? 'bottom' : 'top']: a.pos === 'br' ? 60 : 72, textAlign: a.pos === 'br' ? 'right' : 'left' }}>
        <div style={{ height: 2, width: 64 * rule, background: theme.gold, marginBottom: 12, marginLeft: a.pos === 'br' ? 'auto' : 0 }} />
        <div style={{ fontFamily: theme.sans, fontWeight: 600, fontSize: 26, letterSpacing: '0.2em', color: theme.cream, textShadow: '0 2px 12px rgba(0,0,0,0.85)' }}>{a.text}</div>
      </div>
    </AbsoluteFill>
  );
};

const GodHero: React.FC = () => {
  const frame = useCurrentFrame();
  const g = frame + f(19.18);
  const a = pop(g, f(19.18), 12);
  const glow = 0.6 + 0.4 * Math.sin(frame / 4);
  return (
    <AbsoluteFill style={{ justifyContent: 'flex-end', paddingBottom: 60, paddingLeft: 140, opacity: a.opacity }}>
      <div style={{ ...numeralStyle(340, theme.cream), textShadow: `0 0 ${60 * glow}px rgba(233,196,106,0.55), 0 6px 40px rgba(0,0,0,0.8)`, transform: `translateY(${a.y}px) scale(${a.s * (1 + 0.05 * (frame / f(1.3)))})`, transformOrigin: '0 100%' }}>God.</div>
    </AbsoluteFill>
  );
};

const Flash: React.FC = () => {
  const frame = useCurrentFrame();
  return <AbsoluteFill style={{ background: '#fff', opacity: interpolate(frame, [0, 1, 4], [0.7, 0.55, 0], clamp), mixBlendMode: 'screen' }} />;
};

var grainSvg = encodeURIComponent("<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0.5  0 0 0 0 0.5  0 0 0 0 0.5  0 0 0 1.1 -0.1'/></filter><rect width='100%' height='100%' filter='url(#n)'/></svg>");

const Finish: React.FC = () => {
  const frame = useCurrentFrame();
  const gx = (frame * 53) % 240, gy = (frame * 97) % 240;
  return (
    <>
      <AbsoluteFill style={{ background: 'rgba(30,22,10,0.10)', mixBlendMode: 'soft-light' }} />
      <AbsoluteFill style={{ background: 'radial-gradient(ellipse at 50% 50%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.42) 100%)' }} />
      <AbsoluteFill style={{ backgroundImage: `url("data:image/svg+xml,${grainSvg}")`, backgroundPosition: `${gx}px ${gy}px`, opacity: 0.16, mixBlendMode: 'overlay' }} />
    </>
  );
};

export const ReelV10: React.FC<{ data?: any }> = ({ data }) => {
  useFonts();
  const E: any = data ?? edl;
  SPECKS_ON = E.specks !== false;
  return (
    <AbsoluteFill style={{ background: '#000' }}>
      <AbsoluteFill style={{ filter: 'contrast(1.06) saturate(0.92)' }}>
        {(E.shots as any[]).map((s) => {
          const dur = f(s.t1) - f(s.t0);
          return (
            <Sequence key={s.id} from={f(s.t0)} durationInFrames={dur} name={`${s.id} ${s.job}`}>
              {s.kind === 'card' && <CountCard t0={s.t0} />}
              {s.kind === 'card2' && <YearCard t0={s.t0} rack={s.rack} />}
              {s.kind === 'black' && <TitleBlack t0={s.t0} id={s.id} />}
              {s.kind === 'titlepaper' && <TitlePaper t0={s.t0} />}
              {s.kind === 'evidence' && <EvidenceCard t0={s.t0} dur={dur} shot={s} />}
              {s.kind === 'stat' && <StatCard t0={s.t0} shot={s} />}
              {s.kind === 'year' && <YearGen t0={s.t0} shot={s} />}
              {s.kind === 'title' && <TitleGen t0={s.t0} shot={s} />}
              {s.kind === 'wordcard' && <WordCard t0={s.t0} shot={s} />}
              {s.kind === 'cta' && <EndCard t0={s.t0} shot={s} />}
              {(s.kind === 'video' || s.kind === 'still') && <Media shot={s} dur={dur} />}
            </Sequence>
          );
        })}
        {((E.overlays ?? []) as any[]).map((o) => (
          <Sequence key={o.id} from={f(o.t_in)} durationInFrames={f(o.t_out) - f(o.t_in)} name={o.id}><Overlay o={o} /></Sequence>
        ))}
      </AbsoluteFill>
      {(E.text as any[]).map((c, i) => (
        <Sequence key={i} from={f(c.t0)} durationInFrames={f(c.t1) - f(c.t0)} name={`txt ${c.words.map((w: any) => w.w).join(' ')}`}>{c.mode === 'word' ? <WordCap c={c} /> : <Caption c={c} />}</Sequence>
      ))}
      {((E.annotations ?? []) as any[]).map((a, i) => (
        <Sequence key={`a${i}`} from={f(a.t0)} durationInFrames={f(a.t1) - f(a.t0)} name={`note ${a.text}`}><Annotation a={a} /></Sequence>
      ))}
      {E.godHero !== false && <Sequence from={f(19.18)} durationInFrames={f(20.5) - f(19.18)} name="God"><GodHero /></Sequence>}
      {E.fadeOut && (<Sequence from={f(E.fadeOut[0])} durationInFrames={f(E.fadeOut[1]) - f(E.fadeOut[0])} name="fadeOut"><FadeBlack /></Sequence>)}
      {(E.flashes as number[]).map((t, i) => (
        <Sequence key={i} from={f(t)} durationInFrames={5} name={`flash ${t}`}><Flash /></Sequence>
      ))}
    </AbsoluteFill>
  );
};
