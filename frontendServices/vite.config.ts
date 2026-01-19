import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
server: {
  host: true, // allow external connections
  port: 5173, // optional, but keeps ngrok consistent
  allowedHosts: [
    'localhost',
    '127.0.0.1',
    'overdiligent-liberatory-agatha.ngrok-free.dev', // your current tunnel
  ],
},

})
