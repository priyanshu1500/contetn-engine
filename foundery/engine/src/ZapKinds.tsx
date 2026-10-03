/**
 * Extra shot kinds added for ep-C1-zappos (additive — the original kinds in DocReel.tsx are untouched):
 *   'mech'      animated SVG mechanism diagram. shot.mech = { scene:'deal'|'shelf'|'loop', t:[...absolute secs] }
 *   'bigtext'   stacked hero lines, each popping on its own beat. shot.bigtext = { lines:[{text,t,color?,size?,strike?}], label? }
 *   'statchips' rolling counter (supports decimals) + chips. shot.statchips = { prefix?,suffix?,from?,to,decimals?,roll:[a,b],sub?,chips?:[{text,t}],style?:'warn' }
 * Same theme, same motion rules as the rest of the engine: eased, staggered, nothing linear, nothing simultaneous.
 */
import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';
import { theme, f } from './theme';

const clamp = { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' } as const;
const rnd = (i: number) => { const x = Math.sin(i * 12.9898) * 43758.5453; return x - Math.floor(x); };

const heroStyle = (size: number, color: string): React.CSSProperties => ({
  fontFamily: theme.hero, fontWeight: 400, fontSize: size, color, lineHeight: 0.86, letterSpacing: '0.01em', textTransform: 'uppercase',
});
const labelStyle = (color: string = theme.muted, size = 24): React.CSSProperties => ({
  fontFamily: theme.mono, fontWeight: 600, fontSize: size, letterSpacing: '0.28em', textTransform: 'uppercase', color,
});
const pop = (frame: number, start: number, dur = 8) => {
  const p = interpolate(frame, [start, start + dur], [0, 1], { ...clamp, easing: theme.easeBack });
  return { p, opacity: interpolate(frame, [start, start + 4], [0, 1], clamp), y: (1 - p) * 34, s: 0.86 + 0.14 * p };
};
const seg = (g: number, a: number, b: number) => theme.easeOut(interpolate(g, [f(a), f(b)], [0, 1], clamp));

/* dark panel with a faint blueprint grid — the "mechanism" surface */
const Bg: React.FC<{ grid?: boolean; tint?: string }> = ({ grid = true, tint }) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{ background: theme.bg }}>
      <AbsoluteFill style={{ background: `radial-gradient(ellipse at 50% 42%, ${tint ?? 'rgba(78,113,255,0.10)'} 0%, rgba(0,0,0,0) 70%)` }} />
      {grid && <AbsoluteFill style={{ backgroundImage: 'linear-gradient(rgba(247,245,239,0.035) 1px, transparent 1px), linear-gradient(90deg, rgba(247,245,239,0.035) 1px, transparent 1px)', backgroundSize: '80px 80px', backgroundPosition: `${(frame * 0.25) % 80}px 0px` }} />}
      {Array.from({ length: 16 }).map((_, i) => (
        <div key={i} style={{ position: 'absolute', left: `${rnd(i + 1) * 100}%`, top: `${rnd(i + 40) * 100}%`, width: 3, height: 3, borderRadius: '50%', background: `rgba(247,245,239,${0.2 + 0.15 * Math.sin(frame / (7 + (i % 5)) + i)})` }} />
      ))}
    </AbsoluteFill>
  );
};

/* ---------- icons (SVG, theme colours only) ---------- */
const stroke = { stroke: theme.ink, strokeWidth: 5, strokeLinejoin: 'round', strokeLinecap: 'round' } as const;

const ShoeBox: React.FC<{ x: number; y: number; s?: number; op?: number; rot?: number }> = ({ x, y, s = 1, op = 1, rot = 0 }) => (
  <g transform={`translate(${x},${y}) rotate(${rot}) scale(${s})`} opacity={op}>
    <rect x={-70} y={-8} width={140} height={78} rx={6} fill="#1b1b1e" {...stroke} />
    <rect x={-78} y={-34} width={156} height={30} rx={6} fill={theme.evidence} stroke={theme.ink} strokeWidth={5} />
    <rect x={-26} y={20} width={52} height={16} rx={3} fill="none" stroke={theme.muted} strokeWidth={3} />
    <path d="M -50 56 L 50 56" stroke={theme.muted} strokeWidth={3} strokeLinecap="round" />
  </g>
);

const Store: React.FC<{ x: number; y: number; s?: number; op?: number }> = ({ x, y, s = 1, op = 1 }) => (
  <g transform={`translate(${x},${y}) scale(${s})`} opacity={op}>
    <rect x={-160} y={-40} width={320} height={190} fill="#141416" {...stroke} />
    {/* awning */}
    {Array.from({ length: 8 }).map((_, i) => (
      <rect key={i} x={-176 + i * 44} y={-96} width={44} height={56} fill={i % 2 ? theme.ink : theme.warn} stroke={theme.bg} strokeWidth={2} />
    ))}
    <rect x={-176} y={-40} width={352} height={10} fill={theme.bg} opacity={0.35} />
    <rect x={-40} y={40} width={80} height={110} fill="none" {...stroke} />
    <rect x={-138} y={-4} width={78} height={80} fill="none" stroke={theme.accentBlue} strokeWidth={4} />
    <rect x={62} y={-4} width={78} height={80} fill="none" stroke={theme.accentBlue} strokeWidth={4} />
    <circle cx={26} cy={98} r={5} fill={theme.ink} />
  </g>
);

const Browser: React.FC<{ x: number; y: number; s?: number; op?: number; badge?: number }> = ({ x, y, s = 1, op = 1, badge = 0 }) => (
  <g transform={`translate(${x},${y}) scale(${s})`} opacity={op}>
    <rect x={-170} y={-100} width={340} height={210} rx={14} fill="#141416" stroke={theme.accentBlue} strokeWidth={5} />
    <path d="M -170 -60 L 170 -60" stroke={theme.accentBlue} strokeWidth={4} />
    {[0, 1, 2].map((i) => <circle key={i} cx={-144 + i * 26} cy={-80} r={7} fill={i === 0 ? theme.warn : i === 1 ? theme.evidence : theme.muted} />)}
    <rect x={-40} y={-84} width={190} height={14} rx={7} fill="none" stroke={theme.muted} strokeWidth={3} />
    <ShoeBox x={-4} y={2} s={0.62} />
    {badge > 0 && (
      <g transform={`translate(148,-104) scale(${badge})`}>
        <circle r={30} fill={theme.warn} stroke={theme.bg} strokeWidth={5} />
        <text x={0} y={12} textAnchor="middle" fontFamily={theme.mono} fontWeight={700} fontSize={34} fill="#fff">1</text>
      </g>
    )}
  </g>
);

const Car: React.FC<{ x: number; y: number; s?: number; op?: number; wheel?: number }> = ({ x, y, s = 1, op = 1, wheel = 0 }) => (
  <g transform={`translate(${x},${y}) scale(${s})`} opacity={op}>
    <path d="M -100 28 L -84 -4 Q -70 -34 -34 -34 L 34 -34 Q 60 -34 76 -10 L 100 6 Q 112 12 112 28 L 112 42 L -108 42 Q -112 34 -100 28 Z" fill="#1b1b1e" {...stroke} />
    <path d="M -50 -26 L 46 -26 L 66 -6 L -68 -6 Z" fill="none" stroke={theme.accentBlue} strokeWidth={4} strokeLinejoin="round" />
    {[-56, 66].map((cx, i) => (
      <g key={i} transform={`translate(${cx},46) rotate(${wheel})`}>
        <circle r={24} fill={theme.bg} {...stroke} />
        <path d="M -16 0 L 16 0 M 0 -16 L 0 16" stroke={theme.ink} strokeWidth={4} strokeLinecap="round" />
      </g>
    ))}
  </g>
);

const House: React.FC<{ x: number; y: number; s?: number; op?: number }> = ({ x, y, s = 1, op = 1 }) => (
  <g transform={`translate(${x},${y}) scale(${s})`} opacity={op}>
    <path d="M -110 30 L 0 -70 L 110 30 L 84 30 L 84 120 L -84 120 L -84 30 Z" fill="#141416" {...stroke} />
    <rect x={-22} y={62} width={44} height={58} fill="none" {...stroke} />
    <rect x={38} y={52} width={30} height={30} fill="none" stroke={theme.accentBlue} strokeWidth={4} />
  </g>
);

const PriceTag: React.FC<{ x: number; y: number; text: string; p: number; color?: string }> = ({ x, y, text, p, color = theme.evidence }) => (
  <g transform={`translate(${x},${y}) scale(${0.7 + 0.3 * p}) rotate(${-4 + (1 - p) * -14})`} opacity={p}>
    <path d="M -130 -34 L 96 -34 L 138 0 L 96 34 L -130 34 Z" fill={color} stroke={theme.bg} strokeWidth={4} />
    <circle cx={104} cy={0} r={8} fill={theme.bg} />
    <text x={-8} y={12} textAnchor="middle" fontFamily={theme.hero} fontSize={50} fill={theme.bg} letterSpacing={2}>{text}</text>
  </g>
);

const Tag: React.FC<{ x: number; y: number; text: string; p: number; color?: string }> = ({ x, y, text, p, color = theme.muted }) => (
  <text x={x} y={y + (1 - p) * 14} textAnchor="middle" opacity={p} fontFamily={theme.mono} fontWeight={600} fontSize={26} letterSpacing={7} fill={color}>{text}</text>
);

/* a drawn line with a travelling dot */
const Flow: React.FC<{ x1: number; y1: number; x2: number; y2: number; p: number; color?: string; dot?: boolean }> = ({ x1, y1, x2, y2, p, color = theme.evidence, dot = true }) => {
  const len = Math.hypot(x2 - x1, y2 - y1);
  return (
    <g>
      <line x1={x1} y1={y1} x2={x2} y2={y2} stroke={color} strokeWidth={6} strokeLinecap="round" strokeDasharray={`${len * p} ${len}`} opacity={0.9} />
      {dot && p > 0.02 && p < 0.999 && <circle cx={x1 + (x2 - x1) * p} cy={y1 + (y2 - y1) * p} r={13} fill={color} />}
      {p > 0.98 && <path d={`M ${x2 - 26} ${y2 - 18} L ${x2} ${y2} L ${x2 - 26} ${y2 + 18}`} fill="none" stroke={color} strokeWidth={6} strokeLinecap="round" strokeLinejoin="round" />}
    </g>
  );
};

/* ---------- MECH scenes ---------- */
export const MechCard: React.FC<{ t0: number; shot: any }> = ({ t0, shot }) => {
  const local = useCurrentFrame();
  const g = local + f(t0);
  const m = shot.mech;
  const T: number[] = m.t;
  const breathe = 1 + 0.006 * Math.sin(local / 9);
  const drift = interpolate(local, [0, 240], [0, 1]) ;
  let body: React.ReactNode = null;

  if (m.scene === 'deal') {
    // T: [order appears, arrow to store, full-price tag]
    const a = pop(g, f(T[0]), 9);
    const b = seg(g, T[1], T[1] + 0.9);
    const c = pop(g, f(T[2]), 9);
    const st = pop(g, f(T[1]) + 4, 9);
    body = (
      <g transform={`translate(960,${478 - drift * 8}) scale(1.22) translate(-960,-430)`}>
        <Browser x={470} y={420} s={a.s * 1.05} op={a.opacity} badge={Math.min(1, Math.max(0, (g - f(T[0]) - 6) / 6))} />
        <Tag x={470} y={610} text="ONLINE ORDER" p={a.opacity} />
        <Flow x1={690} y1={420} x2={1170} y2={420} p={b} />
        <Store x={1450} y={400} s={st.s * 1.05} op={st.opacity} />
        <Tag x={1450} y={610} text="SHOE STORE" p={st.opacity} />
        <PriceTag x={930} y={330} text="FULL PRICE" p={c.opacity} />
      </g>
    );
  } else if (m.scene === 'shelf') {
    // T: [shelves start, ...boxes..., "owned" tag, stamp]
    const shelfP = seg(g, T[0], T[0] + 0.5);
    const owned = pop(g, f(T[1]), 9);
    const stamp = pop(g, f(T[2]), 8);
    const rows = [0, 1, 2];
    body = (
      <g>
        <g opacity={shelfP} transform={`translate(0,${(1 - shelfP) * 30})`}>
          <rect x={330} y={110} width={1260} height={450} rx={10} fill="#111113" stroke={theme.muted} strokeWidth={4} />
          {rows.map((r) => (
            <g key={r}>
              <line x1={350} y1={205 + r * 130} x2={1570} y2={205 + r * 130} stroke={theme.muted} strokeWidth={5} />
              {Array.from({ length: 8 }).map((_, i) => {
                const bp = pop(g, f(T[0]) + 3 + (r * 8 + i) * 2, 8);
                return <ShoeBox key={i} x={450 + i * 150} y={150 + r * 130} s={0.5 * bp.s} op={bp.opacity} />;
              })}
            </g>
          ))}
        </g>
        <g transform={`translate(960,668)`} opacity={owned.opacity}>
          <text x={0} y={0} textAnchor="middle" fontFamily={theme.hero} fontSize={104} fill={theme.ink} letterSpacing={3} transform={`scale(${owned.s})`}>SHOES OWNED: <tspan fill={theme.warn}>0</tspan></text>
        </g>
        <g transform={`translate(1240,175) rotate(-9) scale(${0.6 + 0.4 * stamp.p})`} opacity={stamp.opacity}>
          <rect x={-270} y={-56} width={540} height={112} rx={8} fill="#0B0B0C" stroke={theme.warn} strokeWidth={9} />
          <text x={0} y={24} textAnchor="middle" fontFamily={theme.hero} fontSize={82} fill={theme.warn} letterSpacing={4}>SOMEONE ELSE'S</text>
        </g>
      </g>
    );
  } else {
    // 'loop' T: [order, drive to store, paid retail, ship to customer]
    const a = pop(g, f(T[0]), 9);
    const toStore = seg(g, T[1], T[1] + 1.1);
    const tag = pop(g, f(T[2]), 9);
    const toHome = seg(g, T[3], T[3] + 1.2);
    const stp = pop(g, f(T[1]), 9);
    const hp = pop(g, f(T[3]) - 8, 9);
    const X = { order: 340, store: 960, home: 1580 }, Y = 400, ROAD = Y + 175;
    const carX = X.order + (X.store - X.order) * toStore + (X.home - X.store) * toHome;
    const moving = (toStore > 0 && toStore < 1) || (toHome > 0 && toHome < 1);
    const bump = moving ? 2.5 * Math.sin(g * 0.9) : 0;
    const haveBox = toStore >= 1 && g >= f(T[2]) + 8;
    const carOp = interpolate(g, [f(T[1]) - 3, f(T[1]) + 4], [0, 1], clamp);
    body = (
      <g transform="translate(960,470) scale(1.1) translate(-960,-420)">
        <line x1={X.order - 60} y1={ROAD} x2={X.home + 60} y2={ROAD} stroke={theme.muted} strokeWidth={4} strokeDasharray="18 16" opacity={0.55} />
        <line x1={X.order} y1={ROAD} x2={carX} y2={ROAD} stroke={theme.evidence} strokeWidth={6} strokeLinecap="round" opacity={carOp} />
        <Browser x={X.order} y={Y - 10} s={a.s * 0.85} op={a.opacity} badge={Math.min(1, Math.max(0, (g - f(T[0]) - 6) / 6))} />
        <Store x={X.store} y={Y - 20} s={stp.s * 0.95} op={stp.opacity} />
        <House x={X.home} y={Y - 30} s={hp.s * 0.95} op={hp.opacity} />
        <PriceTag x={X.store} y={Y - 200} text="PAID RETAIL" p={tag.opacity} color={theme.warn} />
        <g transform={`translate(${carX},${ROAD - 63 + bump})`}>
          <Car x={0} y={0} s={0.9} op={carOp} wheel={g * 14} />
          {haveBox && <ShoeBox x={0} y={-58} s={0.4} op={1} />}
        </g>
        <Tag x={carX} y={ROAD + 62} text="NICK" p={carOp} color={theme.evidence} />
      </g>
    );
  }

  return (
    <AbsoluteFill>
      <Bg />
      <AbsoluteFill>
        <svg width={1920} height={1080} viewBox="0 0 1920 1080" style={{ transform: `scale(${breathe})`, transformOrigin: '50% 45%' }}>{body}</svg>
      </AbsoluteFill>
      {m.label && <div style={{ position: 'absolute', left: 90, top: 72, ...labelStyle(theme.evidence, 24) }}>{m.label}</div>}
    </AbsoluteFill>
  );
};

/* ---------- BIGTEXT ---------- */
export const BigText: React.FC<{ t0: number; shot: any }> = ({ t0, shot }) => {
  const g = useCurrentFrame() + f(t0);
  const b = shot.bigtext;
  const col = (c?: string) => (c === 'warn' ? theme.warn : c === 'ink' ? theme.ink : theme.evidence);
  return (
    <AbsoluteFill>
      <Bg grid={false} tint={b.tint} />
      <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', paddingBottom: b.lift ?? 90 }}>
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6 }}>
          {b.lines.map((ln: any, i: number) => {
            const a = pop(g, f(ln.t), 10);
            const sk = ln.strike ? seg(g, ln.strike, ln.strike + 0.25) : 0;
            const size = ln.size ?? 230;
            return (
              <div key={i} style={{ position: 'relative', opacity: a.opacity, transform: `translateY(${a.y}px) scale(${a.s})` }}>
                <div style={{ ...heroStyle(size, col(ln.color)), textAlign: 'center' }}>{ln.text}</div>
                {ln.strike && <div style={{ position: 'absolute', left: -20, top: '50%', height: 14, width: `${sk * 106}%`, background: theme.warn, transform: 'rotate(-3deg)', borderRadius: 4 }} />}
              </div>
            );
          })}
        </div>
      </AbsoluteFill>
      {b.label && <div style={{ position: 'absolute', left: 0, right: 0, top: 84, textAlign: 'center', ...labelStyle(theme.muted, 24), opacity: pop(g, f(b.labelT ?? 0) , 9).opacity }}>{b.label}</div>}
    </AbsoluteFill>
  );
};

/* ---------- STATCHIPS ---------- */
export const StatChips: React.FC<{ t0: number; shot: any }> = ({ t0, shot }) => {
  const g = useCurrentFrame() + f(t0);
  const s = shot.statchips;
  const warn = s.style === 'warn';
  const col = warn ? theme.warn : theme.evidence;
  const v = interpolate(g, [f(s.roll[0]), f(s.roll[1])], [s.from ?? 0, s.to], { ...clamp, easing: theme.easeOut });
  const dec = s.decimals ?? 0;
  const txt = dec ? v.toFixed(dec) : Math.round(v).toLocaleString('en-US');
  const a = pop(g, f(s.early ? t0 : s.roll[0]) - 1, 9);
  const dt = g - f(s.roll[1]);
  const settle = dt >= 0 ? 1 + 0.03 * Math.sin(dt / 3) * Math.exp(-dt / 6) : 1;
  const chips: any[] = s.chips ?? [];
  return (
    <AbsoluteFill>
      <Bg grid={false} tint={warn ? 'rgba(200,58,42,0.10)' : undefined} />
      <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', paddingBottom: chips.length ? 210 : 90 }}>
        <div style={{ opacity: a.opacity, transform: `translateY(${a.y}px) scale(${a.s * settle})`, display: 'flex', alignItems: 'baseline', gap: 18 }}>
          <div style={{ ...heroStyle(s.size ?? 330, col), fontVariantNumeric: 'tabular-nums' }}>{s.prefix ?? ''}{txt}</div>
          {s.suffix && <div style={heroStyle((s.size ?? 330) * 0.42, theme.ink)}>{s.suffix}</div>}
        </div>
        {s.sub && <div style={{ ...labelStyle(theme.muted, 26), marginTop: 26, opacity: interpolate(g, [f(s.roll[1]) - 6, f(s.roll[1])], [0, 1], clamp) }}>{s.sub}</div>}
      </AbsoluteFill>
      {chips.length > 0 && (
        <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', paddingTop: 230 }}>
          <div style={{ display: 'flex', gap: 26 }}>
            {chips.map((c, i) => {
              const p = pop(g, f(c.t), 9);
              return (
                <div key={i} style={{ opacity: p.opacity, transform: `translateY(${p.y}px) scale(${p.s})`, padding: '14px 34px', border: `3px solid ${theme.ink}`, borderRadius: 60, background: 'rgba(247,245,239,0.06)', ...labelStyle(theme.ink, 30), letterSpacing: '0.2em' }}>{c.text}</div>
              );
            })}
          </div>
        </AbsoluteFill>
      )}
    </AbsoluteFill>
  );
};
