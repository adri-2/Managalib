<template>
  
  <div class="bg-green-300 p-8  shadow-md w-full h-[350px] rounded-2xl mt-2 mb-[3]">
  <form @submit.prevent="submitForm">
    <h2 class="text-2xl font-bold text-gray-800 mb-4 text-center">Ajouter un Livre</h2>
    
    <div class="mb-4">
      <label for="titre" class="block text-sm font-medium text-gray-700">
        Titre :
      </label>
      <input
        type="text"
        id="titre"
        v-model="livre.titre"
        required
        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
        placeholder="Entrez le titre du livre"
      />
    </div>
    
    <div class="mb-4">
      <label for="auteur" class="block text-sm font-medium text-gray-700">
        Auteur :
      </label>
      <input
        type="text"
        id="auteur"
        v-model="livre.auteur"
        required
        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
        placeholder="Entrez l'auteur du livre"
      />
    </div>
    
    <div class="mb-4">
      <label for="quantity" class="block text-sm font-medium text-gray-700">
        Quantité :
      </label>
      <input
        type="number"
        id="quantity"
        v-model="livre.quantity"
        min="1"
        required
        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
        placeholder="Entrez la quantité"
      />
    </div>
    
    <button
      @click="$emit('addLivreTolist')"
      type="submit"
      :disabled="isLoading"
      class="py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed"
    >
      {{ isLoading ? "Chargement..." : "Ajouter un livre" }}
    </button>

    <div v-if="message" class="mt-4">
      <p
        :class="{
          'text-green-600': isSuccess,
          'text-red-600': !isSuccess,
        }"
        class="text-sm font-medium"
      >
        {{ message }}
      </p>
    </div>
  </form>
</div>

  </template>
  
  <script setup>
  import { reactive, ref } from 'vue';
  import axios from 'axios';
  
  const livre = reactive({
    titre: '',
    auteur: '',
    quantity: '',
  });
  
  const isSuccess = ref(false);
  const message = ref('');
  const isLoading = ref(false);
  
  const submitForm = async () => {
    if (isNaN(Number(livre.quantity)) || Number(livre.quantity) <= 0) {
      message.value = 'La quantité doit être un nombre positif.';
      isSuccess.value = false;
      return;
    }
  
    isLoading.value = true;
    try {
        
      const response = await axios.post('http://127.0.0.1:8000/api/addBooks/', [livre]);
      message.value = 'Le livre a été ajouté avec succès !';
      isSuccess.value = true;
  
      // Émettre le nouveau livre pour mise à jour locale
      // emit('addLivreTolist', response.data[0]);
  
      // Réinitialisation du formulaire
      livre.titre = '';
      livre.auteur = '';
      livre.quantity = '';
    } catch (error) {
      message.value = error.response?.data?.message || 'Une erreur s\'est produite.';
      isSuccess.value = false;
    } finally {
      isLoading.value = false;
    }
  };
  
  defineEmits(['addLivreTolist']);
  </script>
  