import React from 'react';
import { Composition } from 'remotion';
import { DocReel } from './DocReel';
import { FPS, W, H } from './theme';

/** Episode duration comes from the EDL's own `duration` field (seconds), passed via inputProps.
 * If Remotion calls this before inputProps are known it falls back to a generous default;
 * calculateMetadata below is what actually sizes the real render. */
const FALLBACK_S = 60;

export const Root: React.FC = () => (
  <Composition
    id="Episode"
    component={DocReel}
    fps={FPS}
    width={W}
    height={H}
    durationInFrames={Math.round(FALLBACK_S * FPS)}
    defaultProps={{ data: { shots: [], text: [], duration: FALLBACK_S } }}
    calculateMetadata={async ({ props }) => ({
      durationInFrames: Math.round(((props as any).data?.duration ?? FALLBACK_S) * FPS),
    })}
  />
);
