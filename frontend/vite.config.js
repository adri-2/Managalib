// import { defineConfig } from 'vite'
// import vue from '@vitejs/plugin-vue'

// export default defineConfig({
//     plugins: [vue()],
//     server: {
//         proxy: {
//             '/api': {
//                 target: 'http://127.0.0.1:8000', // Adresse de Django
//                 changeOrigin: true,
//                 rewrite: (path) => path.replace(/^\/api/, '/api'),
//             },
//         },
//     },
// })
import { defineConfig } from "vite";
import path from "path";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  // Plugin pour activer Vue.js
  plugins: [vue()],

  // Configuration de la base pour les URLs des fichiers statiques
  base: "/static/",

  resolve: {
    // Définition d'un alias pour accéder facilement au dossier src
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
});

// import { fileURLToPath, URL } from 'node:url'

// import { defineConfig } from 'vite'
// import vue from '@vitejs/plugin-vue'
// import vueDevTools from 'vite-plugin-vue-devtools'

// // https://vite.dev/config/
// export default defineConfig({
//   plugins: [
//     vue(),
//     vueDevTools(),
//   ],
//   resolve: {
//     alias: {
//       '@': fileURLToPath(new URL('./src', import.meta.url))
//     },
//   },
// })
