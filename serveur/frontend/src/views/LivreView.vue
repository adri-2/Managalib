<template>
    <div  class="ma-table">
      <h1 > Bienvenu sur mangalib  </h1>
      <router-link to="">[+] Ajouter livre</router-link>  
      
      <table>
              <tr>
                  <th>NOM</th>
                  <th>AUTEUR</th>
                  <th>QTE</th>
                  <th colspan="2">ACTIONS</th>
              </tr>
          
              <tr  v-for="livre in livres" :key="livre.id">
                <td><router-link :to="`/livres/${livre.id}`">{{ livre.titre }}</router-link></td>

                  <!-- router-link :to="`/articles/${article.id}`">{{ livre.titre }} </router-link> -->
                  <td> {{ livre.auteur}} </td>
                  <td> {{ livre.quantity }} </td>
                  <td><router-link to="">[e]</router-link></td>
                  <td><router-link to="">[-]</router-link></td>
              </tr>
      </table>
     
    </div>
  </template>
  

  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  
  // Declare a reactive variable for storing livre
  const livres = ref([]);
  
  // Fetch livre when the component is mounted
  onMounted(() => {
    axios.get('http://127.0.0.1:8000/api/livre/')
      .then(response => {
        livres.value = response.data;
      })
      .catch(error => {
        console.error('Error fetching livre:', error);
      });
  });
  </script>
  
  
  
  
  
  <!-- <script >
  import axios from 'axios';
  
  export default {
    data() {
      return {
        livre: [],
      };
    },
    mounted() {
      axios.get('http://127.0.0.1:8000/api/livre/libre/')
        .then(response => {
          this.livre = response.data;
        });
    },
  };
  </script> -->
  