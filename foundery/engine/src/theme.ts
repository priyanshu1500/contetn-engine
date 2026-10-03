import { Easing } from 'remotion';
export const FPS = 24;
export const W = 1920;
export const H = 1080;

/**
 * v2 palette — Big Short / Dirty Money / Drive to Survive register: cold, restrained, high-contrast.
 * Yellow is reserved for evidence/highlight only — never used as a general brand color.
 * accentBlue intentionally matches the agency's own brand blue (brand.md #4E71FF): a quiet visual
 * thread back to the brand with no verbal pitch.
 */
export const theme = {
  bg: '#0B0B0C',
  ink: '#F7F5EF',       // primary text, off-white (was oxblood/paper-era "ink")
  paper: '#141416',     // card surfaces are now dark panels, not literal paper
  cream: '#F7F5EF',
  evidence: '#F5C542',  // "documentary yellow" — evidence highlight color only
  warn: '#C83A2A',
  accentBlue: '#4E71FF',
  muted: '#8B8B8B',
  gold: '#F5C542',       // legacy alias so older components (hero em color) pick up the new evidence yellow
  oxblood: '#C83A2A',    // legacy alias -> warning red
  black: '#0B0B0C',
  sans: '"Inter", "Helvetica Neue", Arial, sans-serif',      // body — Söhne substitute (free)
  serif: '"Inter", "Helvetica Neue", Arial, sans-serif',     // legacy alias, no longer serif in v2
  hero: '"Bebas Neue", "Arial Narrow", sans-serif',          // Druk Condensed substitute (free) — gigantic, compressed
  mono: '"IBM Plex Mono", "Courier New", monospace',         // classified/evidence labels
  easeOut: Easing.out(Easing.cubic),
  easeInOut: Easing.inOut(Easing.cubic),
  easeBack: Easing.out(Easing.back(1.6)),
};
export const f = (s: number) => Math.round(s * FPS);
