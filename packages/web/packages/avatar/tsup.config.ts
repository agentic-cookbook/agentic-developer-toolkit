import { defineConfig } from 'tsup'
import { preserveDirectivesPlugin } from 'esbuild-plugin-preserve-directives'

export default defineConfig({
  entry: { index: 'src/index.ts' },
  outDir: 'dist',
  format: ['esm'],
  target: 'es2022',
  platform: 'browser',
  sourcemap: true,
  clean: true,
  dts: false,
  bundle: true,
  splitting: false,
  outExtension: () => ({ js: '.js' }),
  // react is a peer; gsap is EXTERNAL too (not bundled). gsap is a stateful
  // singleton — the engine registers MorphSVGPlugin on it, and a consumer (e.g.
  // @olylo/avatar's yawn timeline) drives morphSVG on the same instance. Bundling
  // a private copy here would split that into two instances and the plugin
  // registration wouldn't be seen by the consumer's tweens.
  external: ['react', 'react-dom', 'react/jsx-runtime', 'gsap', 'gsap/*'],
  esbuildPlugins: [
    preserveDirectivesPlugin({
      directives: ['use client', 'use server'],
      include: /\.(js|ts|jsx|tsx)$/,
      exclude: /node_modules/,
    }),
  ],
})
