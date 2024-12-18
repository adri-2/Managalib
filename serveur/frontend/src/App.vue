<script setup>
import { RouterLink, RouterView } from 'vue-router'

import Navbar from './components/Navbar.vue';
</script>

<template>
  <header>
    
    <div>
     
    <Navbar/>
    </div>
  </header>

   
    <RouterView/>
</template>

<!-- <style>
/* Ajoutez votre style ici */
nav ul {
  list-style: none;
  display: flex;
  gap: 1rem;
}
nav ul li {
  display: inline;
}
nav ul li a {
  text-decoration: none;
  color: #42b983;
}
nav ul li a.router-link-active {
  font-weight: bold;
}
</style> -->