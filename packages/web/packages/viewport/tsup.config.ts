import { defineConfig } from 'tsup'
import { preserveDirectivesPlugin } from 'esbuild-plugin-preserve-directives'

export default defineConfig({
  entry: {
    index: 'src/index.ts',
    ViewportShell: 'src/ViewportShell.tsx',
    ViewportSpacer: 'src/ViewportSpacer.tsx',
    ViewportComposer: 'src/ViewportComposer.tsx',
  },
  outDir: 'dist',
  format: ['esm'],
  target: 'es2022',
  platform: 'browser',
  sourcemap: true,
  clean: true,
  dts: false,
  bundle: true,
  splitting: true,
  outExtension: () => ({ js: '.js' }),
  external: ['react', 'react-dom', 'react/jsx-runtime'],
  esbuildPlugins: [
    preserveDirectivesPlugin({
      directives: ['use client', 'use server'],
      include: /\.(js|ts|jsx|tsx)$/,
      exclude: /node_modules/,
    }),
  ],
})
