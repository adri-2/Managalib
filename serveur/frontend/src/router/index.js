import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue';
import About from '../views/About.vue';
import LivreView from '../views/LivreView.vue';
import ProfilLivre from '../views/ProfilLivre.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'Home', component: Home },
    { path: '/about', name: 'About', component: About },
    { path: '/livres', name: 'Livres', component: LivreView },
    { path: '/livre/:id', name: 'livres', component: ProfilLivre },

  ],
})

export default router
