/**
 * DocReel v3 — Master Editorial Documentary & MetroMedia Engine.
 * High-Status Investigative Documentary Standard:
 * - Multi-font kinetic typography (Sans, Serif Italic, Condensed Display, Monospace, Handwritten).
 * - High-key stark contrast reset slides (pure white / deep black).
 * - Polaroid pinboard frames with authentic handwritten script.
 * - Real document crops with animated highlight sweeps.
 */
import React, { useEffect, useState } from 'react';
import {
  AbsoluteFill, Sequence, Video, Img, staticFile, useCurrentFrame,
  interpolate, delayRender, continueRender, useVideoConfig,
} from 'remotion';
import { theme, f } from './theme';
import { MechCard, BigText, StatChips } from './ZapKinds';

const clamp = { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' } as const;

/* ---------- Fonts Loader ---------- */
const useFonts = () => {
  const [handle] = useState(() => delayRender('fonts'));
  useEffect(() => {
    if (typeof document !== 'undefined') {
      const linkId = 'docreel-google-fonts';
      if (!document.getElementById(linkId)) {
        const link = document.createElement('link');
        link.id = linkId;
        link.rel = 'stylesheet';
        link.href = 'https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Caveat:wght@600;700&family=IBM+Plex+Mono:ital,wght@0,400;0,600;1,400&family=Inter:wght@400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,500;1,6..72,600;1,6..72,700&family=Playfair+Display:ital,wght@0,600;0,700;1,600;1,700&display=swap';
        document.head.appendChild(link);
      }
    }

    const defs: [string, string, string, string][] = [
      ['Inter', 'inter-500.woff2', '500', 'normal'],
      ['Inter', 'inter-600.woff2', '600', 'normal'],
      ['Inter', 'inter-700.woff2', '700', 'normal'],
      ['Bebas Neue', 'bebas-neue-400.ttf', '400', 'normal'],
      ['IBM Plex Mono', 'ibm-plex-mono-400.ttf', '400', 'normal'],
      ['IBM Plex Mono', 'ibm-plex-mono-500.ttf', '500', 'normal'],
      ['IBM Plex Mono', 'ibm-plex-mono-600.ttf', '600', 'normal'],
    ];

    Promise.all(defs.map(([fam, file, w, st]) => {
      try {
        const ff = new FontFace(fam, `url(${staticFile(file)})`, { weight: w, style: st });
        return ff.load().then((l) => { (document as any).fonts.add(l); }).catch(() => {});
      } catch (e) {
        return Promise.resolve();
      }
    })).then(() => {
      setTimeout(() => continueRender(handle), 200);
    }).catch(() => continueRender(handle));
  }, [handle]);
};

const seedOf = (id: string) => ([...id].reduce((a, c) => (a * 31 + c.charCodeAt(0)) | 0, 7) % 100) / 10;
const rnd = (i: number) => { const x = Math.sin(i * 12.9898) * 43758.5453; return x - Math.floor(x); };

const prevDir = (shots: any[], id: string): 'L' | 'R' => {
  const i = shots.findIndex((s) => s.id === id);
  for (let k = i - 1; k >= 0; k--) if (shots[k].dir) return shots[k].dir;
  return 'R';
};

/* ---------- Broadcast Flicker & Atmosphere ---------- */
const Flicker: React.FC = () => {
  const frame = useCurrentFrame();
  const j = 0.94 + 0.06 * Math.sin(frame * 7.3) * (rnd(frame) > 0.85 ? 1.6 : 0.4);
  return (
    <>
      <AbsoluteFill style={{ background: `rgba(0,0,0,${1 - j})`, mixBlendMode: 'multiply' }} />
      <AbsoluteFill style={{ backgroundImage: 'repeating-linear-gradient(0deg, rgba(0,0,0,0.10) 0px, rgba(0,0,0,0) 1px, rgba(0,0,0,0) 2px)', opacity: 0.35, mixBlendMode: 'overlay' }} />
    </>
  );
};

const Specks: React.FC<{ n?: number; on: boolean }> = ({ n = 22, on }) => {
  const frame = useCurrentFrame();
  if (!on) return null;
  return (
    <AbsoluteFill>
      {Array.from({ length: n }).map((_, i) => {
        const x = rnd(i + 1) * 100, y = rnd(i + 50) * 100, s = 1.5 + rnd(i + 90) * 3;
        const flick = 0.25 + 0.2 * Math.sin(frame / (6 + (i % 5)) + i);
        return <div key={i} style={{ position: 'absolute', left: `${x}%`, top: `${y + Math.sin(frame / 40 + i) * 0.2}%`, width: s, height: s, borderRadius: '50%', background: `rgba(247,245,239,${flick})` }} />;
      })}
    </AbsoluteFill>
  );
};

const Panel: React.FC<{ specksOn: boolean; tint?: string }> = ({ specksOn, tint }) => (
  <AbsoluteFill style={{ background: theme.bg }}>
    <AbsoluteFill style={{ background: `radial-gradient(ellipse at 50% 40%, ${tint ?? 'rgba(78,113,255,0.06)'} 0%, rgba(0,0,0,0) 70%)` }} />
    <Specks on={specksOn} />
  </AbsoluteFill>
);

const heroStyle = (size: number, color: string): React.CSSProperties => ({
  fontFamily: theme.hero, fontWeight: 400, fontSize: size, color, lineHeight: 0.86, letterSpacing: '0.01em', textTransform: 'uppercase',
});
const labelStyle = (color: string = theme.muted): React.CSSProperties => ({
  fontFamily: theme.mono, fontWeight: 600, fontSize: 24, letterSpacing: '0.28em', textTransform: 'uppercase', color,
});

const pop = (frame: number, start: number, dur = 8) => {
  const p = interpolate(frame, [start, start + dur], [0, 1], { ...clamp, easing: theme.easeBack });
  return { p, opacity: interpolate(frame, [start, start + 4], [0, 1], clamp), y: (1 - p) * 34, s: 0.86 + 0.14 * p };
};

/* ---------- Typewriter Reveal ---------- */
const Typewriter: React.FC<{ t0: number; text: string; size?: number; color?: string; cps?: number }> = ({ t0, text, size = 30, color, cps = 22 }) => {
  const g = useCurrentFrame() + f(t0);
  const secs = g / 24;
  const n = Math.max(0, Math.min(text.length, Math.floor(secs * cps)));
  const shown = text.slice(0, n);
  const caretOn = Math.floor(secs * 3) % 2 === 0 && n < text.length;
  return (
    <div style={{ ...labelStyle(color), fontSize: size }}>
      {shown}{caretOn && <span style={{ opacity: 0.9 }}>_</span>}
    </div>
  );
};

/* ---------- Multi-Font Word Caption Renderer ---------- */
const WordCap: React.FC<{ c: any }> = ({ c }) => {
  const frame = useCurrentFrame();
  const g = frame + f(c.t0);
  const words = (c.words as any[]).filter((w) => g >= f(w.t) - 1);

  return (
    <AbsoluteFill style={{ justifyContent: 'flex-end', alignItems: 'center', paddingBottom: c.pad ?? 230, pointerEvents: 'none' }}>
      <div style={{ display: 'flex', gap: 24, alignItems: 'baseline', flexWrap: 'wrap', justifyContent: 'center', maxWidth: 1600, padding: '0 40px' }}>
        {words.map((w, i) => {
          const a = pop(g, f(w.t) - 1, 6);
          const em = !!w.em;
          const fontKind = w.fontKind || (em ? 'serif-italic' : 'sans');

          let fontFamily = theme.sans;
          let fontStyle: 'normal' | 'italic' = 'normal';
          let fontWeight: number | string = em ? 700 : 600;
          let fontSize = em ? 94 : 78;
          let color = em ? theme.evidence : theme.ink;
          let textTransform: 'none' | 'uppercase' = 'none';
          let letterSpacing = 'normal';
          let boxBg: string | undefined = undefined;

          if (fontKind === 'serif' || fontKind === 'serif-italic' || w.style === 'serif-italic') {
            fontFamily = theme.serifItalic;
            fontStyle = 'italic';
            fontWeight = 700;
            fontSize = 98;
            color = w.color || theme.evidence;
          } else if (fontKind === 'hero' || fontKind === 'condensed' || w.style === 'condensed') {
            fontFamily = theme.displayCondensed;
            fontWeight = 400;
            fontSize = 110;
            textTransform = 'uppercase';
            color = w.color || theme.ink;
          } else if (fontKind === 'mono' || w.style === 'mono') {
            fontFamily = theme.mono;
            fontWeight = 600;
            fontSize = 68;
            letterSpacing = '0.08em';
            color = w.color || theme.evidence;
          } else if (fontKind === 'handwritten' || w.style === 'handwritten') {
            fontFamily = theme.handwritten;
            fontWeight = 700;
            fontSize = 100;
            color = w.color || '#FFFFFF';
          }

          if (w.box === 'yellow' || w.highlight === 'yellow') {
            boxBg = 'rgba(245, 197, 66, 0.95)';
            color = '#0A0A0A';
          } else if (w.box === 'white' || w.highlight === 'white') {
            boxBg = 'rgba(255, 255, 255, 0.95)';
            color = '#0A0A0A';
          }

          const rot = w.rotate ? `rotate(${w.rotate}deg)` : '';

          return (
            <span key={i} style={{
              fontFamily, fontStyle, fontWeight, fontSize, color, textTransform, letterSpacing,
              background: boxBg, padding: boxBg ? '4px 18px' : undefined, borderRadius: boxBg ? 6 : undefined,
              textShadow: boxBg ? 'none' : '0 3px 26px rgba(0,0,0,0.85), 0 1px 3px rgba(0,0,0,0.6)',
              opacity: a.opacity, transform: `translateY(${a.y * 0.6}px) scale(${a.s}) ${rot}`.trim(), display: 'inline-block',
            }}>{w.w}</span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Stark Slide (Optical Contrast Reset) ---------- */
const StarkSlide: React.FC<{ shot: any }> = ({ shot }) => {
  const local = useCurrentFrame();
  const st = shot.stark;
  const isWhite = st.bg === 'white' || st.bg === '#FFFFFF';
  const bg = isWhite ? '#FFFFFF' : '#0B0B0C';
  const textColor = isWhite ? '#0A0A0A' : '#F7F5EF';
  const a = pop(local, 0, 8);
  return (
    <AbsoluteFill style={{ background: bg, justifyContent: 'center', alignItems: 'center', zIndex: 10 }}>
      <div style={{ opacity: a.opacity, transform: `translateY(${a.y}px) scale(${a.s})`, textAlign: 'center', padding: '0 120px' }}>
        {st.tag && <div style={{ ...labelStyle(isWhite ? '#666666' : theme.evidence), marginBottom: 24, fontSize: 26 }}>{st.tag}</div>}
        <div style={{ fontFamily: theme.sans, fontWeight: 800, fontSize: st.size ?? 120, color: textColor, lineHeight: 1.05, letterSpacing: '-0.02em' }}>
          {st.text}
        </div>
        {st.sub && <div style={{ fontFamily: theme.sans, fontWeight: 500, fontSize: 42, color: isWhite ? '#444444' : '#999999', marginTop: 28 }}>{st.sub}</div>}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- Polaroid Pinboard Frame ---------- */
const PolaroidCard: React.FC<{ dur: number; shot: any }> = ({ dur, shot }) => {
  const local = useCurrentFrame();
  const pol = shot.polaroid;
  const enter = theme.easeOut(interpolate(local, [0, 8], [0, 1], clamp));
  const scale = (pol.scale ?? 1.0) + 0.03 * (local / dur);
  const rot = (pol.rot ?? -2.5) + (1 - enter) * 4;
  return (
    <AbsoluteFill style={{ background: theme.bg, justifyContent: 'center', alignItems: 'center' }}>
      <div style={{
        position: 'relative', width: 620, background: '#FFFFFF', padding: '24px 24px 72px 24px',
        boxShadow: '0 30px 60px rgba(0,0,0,0.85), 0 4px 12px rgba(0,0,0,0.5)',
        transform: `translateY(-40px) rotate(${rot}deg) scale(${scale * enter})`, opacity: enter,
      }}>
        {/* Masking tape piece at top */}
        <div style={{
          position: 'absolute', top: -16, left: '50%', transform: 'translateX(-50%) rotate(1deg)',
          width: 140, height: 34, background: theme.tape, boxShadow: '0 2px 6px rgba(0,0,0,0.25)',
        }} />
        <div style={{ width: '100%', height: 490, overflow: 'hidden', background: '#111' }}>
          <Img src={staticFile(pol.src)} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
        </div>
        {pol.label && (
          <div style={{
            position: 'absolute', bottom: 16, left: 24, right: 24, textAlign: 'center',
            fontFamily: theme.handwritten, fontSize: 44, color: '#1B1B1B', fontWeight: 700,
          }}>
            {pol.label}
          </div>
        )}
      </div>
    </AbsoluteFill>
  );
};

/* ---------- FullBleed Media with Camera Dynamics ---------- */
const Media: React.FC<{ shot: any; dur: number; shots: any[] }> = ({ shot, dur, shots }) => {
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

  let whipX = 0; let blur = 0; let rackScale = 1; let slideX = 0; let slideY = 0;
  if (shot.whip) {
    const w = theme.easeOut(interpolate(frame, [0, 5], [0, 1], clamp));
    const from = prevDir(shots, shot.id) === 'R' ? -300 : 300;
    whipX = from * (1 - w);
    blur = 18 * (1 - w);
    rackScale = 1 + 0.14 * (1 - w);
  }
  if (shot.rack) {
    const r = theme.easeOut(interpolate(frame, [0, 10], [0, 1], clamp));
    blur = Math.max(blur, 14 * (1 - r));
    rackScale = Math.max(rackScale, 1.03 - 0.03 * r);
  }
  if (shot.enter === 'slide') {
    const dir = shot.slideFrom ?? (shot.dir === 'L' ? 'right' : 'left');
    const s = theme.easeOut(interpolate(frame, [0, 14], [0, 1], clamp));
    const dist = (1 - s) * 420;
    slideX = dir === 'left' ? -dist : dir === 'right' ? dist : 0;
    slideY = dir === 'top' ? -dist : dir === 'bottom' ? dist : 0;
  }
  const duo = shot.duotone ? 'contrast(1.12) brightness(0.92) saturate(1.08)' : (shot.grade ?? 'contrast(1.05) brightness(0.98) saturate(1.02)');
  const filter = `${duo} ${blur > 0.3 ? `blur(${blur}px)` : ''}`.trim() || undefined;
  const style: React.CSSProperties = {
    width: '100%', height: '100%', objectFit: 'cover', filter,
    transform: `translate(${dx + whipX + slideX}px,${dy + slideY}px) rotate(${rot}deg) scale(${scale * rackScale})`,
  };
  return (
    <>
      {shot.kind === 'video' && <Video src={staticFile(shot.src)} startFrom={f(shot.from ?? 0)} muted style={style} />}
      {shot.kind === 'still' && <Img src={staticFile(shot.src)} style={{ ...style, objectPosition: `${(shot.fx ?? 0.5) * 100}% ${(shot.fy ?? 0.5) * 100}%`, transformOrigin: `${(shot.fx ?? 0.5) * 100}% ${(shot.fy ?? 0.5) * 100}%` }} />}
      {shot.scrim && <AbsoluteFill style={{ background: 'linear-gradient(to top, rgba(0,0,0,0.72) 0%, rgba(0,0,0,0.38) 30%, rgba(0,0,0,0) 52%), linear-gradient(to bottom, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0) 22%)' }} />}
      {shot.flicker && <Flicker />}
    </>
  );
};

/* ---------- StatCard, YearGen, TitleGen, WordCard, EndCard, LabelCard ---------- */
const StatCard: React.FC<{ t0: number; shot: any; specksOn: boolean }> = ({ t0, shot, specksOn }) => {
  const g = useCurrentFrame() + f(t0);
  const st = shot.stat;
  const val = Math.round(interpolate(g, [f(st.roll[0]), f(st.roll[1])], [st.from ?? 0, st.to], { ...clamp, easing: theme.easeOut }));
  const a = pop(g, st.early ? f(t0) + 1 : f(st.roll[0]) - 1, 9);
  const dt = g - f(st.roll[1]);
  const settle = dt >= 0 ? 1 + 0.03 * Math.sin(dt / 3) * Math.exp(-dt / 6) : 1;
  const warn = st.style === 'warn';
  const col = warn ? theme.warn : theme.evidence;
  return (
    <AbsoluteFill>
      <Panel specksOn={specksOn} tint={warn ? 'rgba(200,58,42,0.08)' : undefined} />
      <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', opacity: a.opacity, transform: `translateY(${a.y}px) scale(${a.s * settle})` }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 20 }}>
          <div style={{ ...heroStyle(280, col), fontVariantNumeric: 'tabular-nums' }}>{st.prefix ?? ''}{val.toLocaleString('en-US')}</div>
          {st.suffix && <div style={{ ...heroStyle(110, theme.ink) }}>{st.suffix}</div>}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const YearGen: React.FC<{ t0: number; shot: any; specksOn: boolean }> = ({ t0, shot, specksOn }) => {
  const g = useCurrentFrame() + f(t0);
  const y = shot.year;
  const a = pop(g, f(y.roll[0]) - 1, 9);
  const v = Math.round(interpolate(g, [f(y.roll[0]), f(y.roll[1])], [y.from, y.to], { ...clamp, easing: theme.easeOut }));
  return (
    <AbsoluteFill>
      <Panel specksOn={specksOn} />
      <AbsoluteFill style={{ justifyContent: 'center', paddingLeft: 180 }}>
        <div style={{ ...heroStyle(300, theme.ink), fontVariantNumeric: 'tabular-nums', opacity: a.opacity, transform: `translateY(${a.y}px) scale(${a.s})`, transformOrigin: '0 50%' }}>{v}</div>
        {y.label && <div style={{ marginLeft: 4, marginTop: 12, opacity: interpolate(g, [f(y.roll[1]), f(y.roll[1]) + 4], [0, 1], clamp) }}><div style={labelStyle(theme.evidence)}>{y.label}</div></div>}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const TitleGen: React.FC<{ t0: number; shot: any; specksOn: boolean }> = ({ t0, shot, specksOn }) => {
  const g = useCurrentFrame() + f(t0);
  const t = shot.title;
  const a = pop(g, f(t.pop[0]), 9);
  const b = pop(g, f(t.pop[1]), 9);
  return (
    <AbsoluteFill>
      <Panel specksOn={specksOn} />
      <AbsoluteFill style={{ justifyContent: 'center', paddingLeft: 200 }}>
        <div style={{ ...labelStyle(theme.evidence), opacity: a.opacity, transform: `translateY(${a.y}px)` }}>{t.label}</div>
        <div style={{ ...heroStyle(280, theme.ink), opacity: b.opacity, transform: `translateY(${b.y}px) scale(${b.s})`, transformOrigin: '0 50%', marginTop: 6 }}>{t.num}</div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const WordCard: React.FC<{ t0: number; shot: any; specksOn: boolean }> = ({ t0, shot, specksOn }) => {
  const g = useCurrentFrame() + f(t0);
  const w = shot.wordcard;
  const warn = w.style === 'warn';
  const customBg = w.bg as string | undefined;
  const a = pop(g, f(w.pop), 10);
  return (
    <AbsoluteFill>
      {customBg
        ? <AbsoluteFill style={{ background: customBg }} />
        : <Panel specksOn={specksOn} tint={warn ? 'rgba(200,58,42,0.08)' : undefined} />}
      <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', opacity: a.opacity, transform: `translateY(${a.y}px) scale(${a.s})` }}>
        <div style={{ ...heroStyle(w.size ?? (w.text.length > 24 ? 190 : 260), customBg ? '#FFFFFF' : warn ? theme.warn : theme.evidence), textAlign: 'center', padding: '0 120px' }}>{w.text}</div>
        {w.sub && <div style={{ fontFamily: theme.sans, fontWeight: 600, fontSize: 40, color: customBg ? 'rgba(255,255,255,0.8)' : theme.ink, marginTop: 14 }}>{w.sub}</div>}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const EndCard: React.FC<{ t0: number; shot: any; specksOn: boolean }> = ({ t0, shot, specksOn }) => {
  const g = useCurrentFrame() + f(t0);
  const c = shot.cta;
  const a = pop(g, f(c.pop[0]), 9), b = pop(g, f(c.pop[1]), 11), l = pop(g, f(c.pop[2]), 9);
  return (
    <AbsoluteFill>
      <Panel specksOn={specksOn} />
      <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
        <div style={{ ...labelStyle(theme.evidence), opacity: a.opacity, transform: `translateY(${a.y}px)` }}>{c.kicker}</div>
        <div style={{ ...heroStyle(200, theme.ink), opacity: b.opacity, transform: `translateY(${b.y}px) scale(${b.s})`, margin: '10px 0' }}>{c.hero}</div>
        <div style={{ fontFamily: theme.sans, fontWeight: 500, fontSize: 42, color: theme.muted, textAlign: 'center', maxWidth: 1500, opacity: l.opacity, transform: `translateY(${l.y}px)` }}>{c.line}</div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const LabelCard: React.FC<{ t0: number; shot: any; specksOn: boolean }> = ({ t0, shot, specksOn }) => (
  <AbsoluteFill>
    <Panel specksOn={specksOn} />
    <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
      <Typewriter t0={t0 + (shot.label.at ?? 0) - t0} text={shot.label.text} size={shot.label.size ?? 56} color={theme.evidence} cps={shot.label.cps ?? 18} />
      {shot.label.sub && <div style={{ ...labelStyle(theme.muted), fontSize: 20, marginTop: 14 }}>{shot.label.sub}</div>}
    </AbsoluteFill>
  </AbsoluteFill>
);

const FadeBlack: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  return <AbsoluteFill style={{ background: '#000', opacity: interpolate(frame, [0, Math.max(1, durationInFrames - 1)], [0, 1], clamp) }} />;
};

/* ---------- EvidenceCard: Torn-edge document crop with highlight sweep ---------- */
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

const EvidenceCard: React.FC<{ t0: number; dur: number; shot: any; specksOn: boolean }> = ({ t0, dur, shot, specksOn }) => {
  const local = useCurrentFrame();
  const g = local + f(t0);
  const p = interpolate(local, [0, dur], [0, 1], clamp);
  const enter = theme.easeOut(interpolate(local, [0, 9], [0, 1], clamp));
  const S = (shot.scale ?? 1.72) + 0.06 * p;
  const rot = -1.0 - 1.3 * (1 - enter);
  const ty = (shot.pos?.[1] ?? 64) + 70 * (1 - enter);
  const blur = shot.rack ? 12 * (1 - enter) : 0;
  const LB = shot.label ?? [1.0, 1.14];
  const label = interpolate(g, [f(LB[0]), f(LB[1])], [0, 1], clamp);
  const imgSize = shot.imgSize ?? [1920, 1080];
  const imgOff = shot.imgOff ?? [-570, -150];
  return (
    <AbsoluteFill style={{ background: theme.bg }}>
      <AbsoluteFill style={{ background: 'radial-gradient(ellipse at 40% 35%, rgba(78,113,255,0.05) 0%, rgba(0,0,0,0) 75%)' }} />
      <Specks on={specksOn} />
      <div style={{ position: 'absolute', left: shot.pos?.[0] ?? 70, top: ty, width: CARD_W, height: CARD_H, transformOrigin: '0 0', transform: `rotate(${rot}deg) scale(${S})`, filter: `drop-shadow(0 26px 40px rgba(0,0,0,0.7)) ${blur > 0.3 ? `blur(${blur}px)` : ''}`, opacity: interpolate(local, [0, 4], [0, 1], clamp) }}>
        <div style={{ position: 'absolute', inset: 0, clipPath: tornClip, background: '#fff', overflow: 'hidden' }}>
          <Img src={staticFile(shot.src)} style={{ position: 'absolute', left: imgOff[0], top: imgOff[1], width: imgSize[0], height: imgSize[1] }} />
          {(shot.hl ?? []).map((h: any, i: number) => {
            const w = h.w * interpolate(g, [f(h.t[0]), f(h.t[1])], [0, 1], { ...clamp, easing: theme.easeInOut });
            if (h.shape === 'underline') {
              return <div key={i} style={{ position: 'absolute', left: h.x, top: h.y + (h.h ?? 24) - 3, width: w, height: 4, background: theme.evidence }} />;
            }
            return <div key={i} style={{ position: 'absolute', left: h.x, top: h.y, width: w, height: h.h, background: theme.highlightYellow, mixBlendMode: 'multiply' }} />;
          })}
          <div style={{ position: 'absolute', left: 0, right: 0, top: 0, height: 60, background: 'linear-gradient(rgba(0,0,0,0.10), rgba(0,0,0,0))' }} />
        </div>
      </div>
      {shot.source && <div style={{ position: 'absolute', left: 84, bottom: 44, opacity: label }}><div style={labelStyle(theme.muted)}>{shot.source}</div></div>}
    </AbsoluteFill>
  );
};

const Annotation: React.FC<{ a: any }> = ({ a }) => {
  const frame = useCurrentFrame();
  const dur = f(a.t1) - f(a.t0);
  const fd = Math.max(1, Math.min(6, Math.floor(dur / 3)));
  const op = interpolate(frame, [0, fd, dur - fd, dur], [0, 1, 1, 0], clamp);
  const rule = interpolate(frame, [0, 10], [0, 1], { ...clamp, easing: theme.easeOut });
  return (
    <AbsoluteFill style={{ opacity: op }}>
      <div style={{ position: 'absolute', [a.pos === 'br' ? 'right' : 'left']: 90, [a.pos === 'br' ? 'bottom' : 'top']: a.pos === 'br' ? 60 : 72, textAlign: a.pos === 'br' ? 'right' : 'left' }}>
        <div style={{ height: 2, width: 64 * rule, background: theme.evidence, marginBottom: 12, marginLeft: a.pos === 'br' ? 'auto' : 0 }} />
        <div style={labelStyle(theme.ink)}>{a.text}</div>
      </div>
    </AbsoluteFill>
  );
};

const Flash: React.FC = () => {
  const frame = useCurrentFrame();
  return <AbsoluteFill style={{ background: '#fff', opacity: interpolate(frame, [0, 1, 4], [0.6, 0.45, 0], clamp), mixBlendMode: 'screen' }} />;
};

/* ---------- MASTER DOCREEL COMPOSITION ---------- */
export const DocReel: React.FC<{ data: any }> = ({ data }) => {
  useFonts();
  const E = data;
  const specksOn = E.specks !== false;
  const shots: any[] = E.shots as any[];

  return (
    <AbsoluteFill style={{ background: theme.bg }}>
      <AbsoluteFill style={{ filter: 'contrast(1.05) saturate(0.95)' }}>
        {shots.map((s) => {
          const dur = f(s.t1) - f(s.t0);
          return (
            <Sequence key={s.id} from={f(s.t0)} durationInFrames={dur} name={`${s.id} ${s.job ?? ''}`}>
              {s.kind === 'stark' && <StarkSlide shot={s} />}
              {s.kind === 'polaroid' && <PolaroidCard dur={dur} shot={s} />}
              {s.kind === 'evidence' && <EvidenceCard t0={s.t0} dur={dur} shot={s} specksOn={specksOn} />}
              {s.kind === 'stat' && <StatCard t0={s.t0} shot={s} specksOn={specksOn} />}
              {s.kind === 'year' && <YearGen t0={s.t0} shot={s} specksOn={specksOn} />}
              {s.kind === 'title' && <TitleGen t0={s.t0} shot={s} specksOn={specksOn} />}
              {s.kind === 'wordcard' && <WordCard t0={s.t0} shot={s} specksOn={specksOn} />}
              {s.kind === 'cta' && <EndCard t0={s.t0} shot={s} specksOn={specksOn} />}
              {s.kind === 'label' && <LabelCard t0={s.t0} shot={s} specksOn={specksOn} />}
              {s.kind === 'mech' && <MechCard t0={s.t0} shot={s} />}
              {s.kind === 'bigtext' && <BigText t0={s.t0} shot={s} />}
              {s.kind === 'statchips' && <StatChips t0={s.t0} shot={s} />}
              {(s.kind === 'video' || s.kind === 'still') && <Media shot={s} dur={dur} shots={shots} />}
            </Sequence>
          );
        })}
      </AbsoluteFill>
      {(E.text as any[]).map((c, i) => (
        <Sequence key={i} from={f(c.t0)} durationInFrames={f(c.t1) - f(c.t0)} name={`txt ${c.words.map((w: any) => w.w).join(' ')}`}><WordCap c={c} /></Sequence>
      ))}
      {((E.annotations ?? []) as any[]).map((a, i) => (
        <Sequence key={`a${i}`} from={f(a.t0)} durationInFrames={f(a.t1) - f(a.t0)} name={`note ${a.text}`}><Annotation a={a} /></Sequence>
      ))}
      {E.fadeOut && (<Sequence from={f(E.fadeOut[0])} durationInFrames={f(E.fadeOut[1]) - f(E.fadeOut[0])} name="fadeOut"><FadeBlack /></Sequence>)}
      {((E.flashes ?? []) as number[]).map((t, i) => (
        <Sequence key={i} from={f(t)} durationInFrames={5} name={`flash ${t}`}><Flash /></Sequence>
      ))}
    </AbsoluteFill>
  );
};

