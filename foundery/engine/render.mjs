/**
 * DocReel engine renderer — episode-agnostic.
 * Usage:
 *   node render.mjs video   <edl.json> <publicDir> <out.mp4> [frameRange]
 *   node render.mjs stills  <edl.json> <publicDir> <outDir> frame1,frame2,...
 * The EDL's own `duration` field (seconds) drives the composition length via calculateMetadata.
 */
import path from 'node:path';
import fs from 'node:fs';
import { pathToFileURL, fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const { bundle } = await import(pathToFileURL(path.join(here, 'node_modules/@remotion/bundler/dist/index.js')).href);
const { selectComposition, renderMedia, renderStill } = await import(pathToFileURL(path.join(here, 'node_modules/@remotion/renderer/dist/index.js')).href);

const mode = process.argv[2];
const edlPath = path.resolve(process.argv[3]);
const publicDir = path.resolve(process.argv[4]);
const outArg = process.argv[5];
const browserExecutable = 'D:/agency content/.remotion/chrome-headless-shell/win64/chrome-headless-shell-win64/chrome-headless-shell.exe';

const edlData = JSON.parse(fs.readFileSync(edlPath, 'utf8'));
console.log(`[DocReel] EDL: ${edlPath} (duration ${edlData.duration}s, ${edlData.shots.length} shots)`);
console.log(`[DocReel] publicDir: ${publicDir}`);

const serveUrl = await bundle({ entryPoint: path.join(here, 'src/index.ts'), publicDir });
const comp = await selectComposition({ serveUrl, id: 'Episode', inputProps: { data: edlData }, browserExecutable });
console.log(`[DocReel] Composition: ${comp.width}x${comp.height} @ ${comp.fps}fps, ${comp.durationInFrames} frames`);

if (mode === 'stills') {
  fs.mkdirSync(outArg, { recursive: true });
  const frames = (process.argv[6] || '').split(',').map(Number).filter((n) => !Number.isNaN(n));
  for (const fr of frames) {
    await renderStill({ composition: comp, serveUrl, frame: fr, inputProps: { data: edlData }, output: path.join(outArg, `f_${String(fr).padStart(4, '0')}.png`), browserExecutable, overwrite: true });
  }
} else {
  fs.mkdirSync(path.dirname(outArg), { recursive: true });
  const frameRange = process.argv[6] ? process.argv[6].split('-').map(Number) : undefined;
  await renderMedia({
    composition: comp, serveUrl, codec: 'h264', outputLocation: outArg, inputProps: { data: edlData },
    crf: 16, pixelFormat: 'yuv420p', concurrency: 1,
    browserExecutable, imageFormat: 'jpeg', jpegQuality: 88,
    timeoutInMilliseconds: 90000,
    chromiumOptions: {
      enableMultiProcessOnWindows: true,
      args: ['--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu', '--js-flags=--max-old-space-size=4096'],
    },
    frameRange,
    onProgress: ({ renderedFrames }) => { if (renderedFrames % 60 === 0) console.log('rendered', renderedFrames, '/', comp.durationInFrames); },
  });
}
console.log('done', outArg);
