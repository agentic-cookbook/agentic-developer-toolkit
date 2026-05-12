import { defineConfig } from 'vitest/config'

export default defineConfig({
  server: {
    fs: {
      allow: ['..'],
    },
  },
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: ['./vitest.setup.ts'],
    dir: '../packages',
  },
})
