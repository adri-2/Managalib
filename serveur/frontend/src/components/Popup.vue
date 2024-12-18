<template>
    <div>
      <!-- Bouton pour ouvrir la popup -->
      <button
        @click="showPopup = true"
        class="bg-blue-500 text-white px-4 py-2 rounded"
      >
        Ouvrir Popup
      </button>
  
      <!-- Popup -->
      <div
        v-if="showPopup"
        class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
      >
        <div class="bg-white p-8 rounded shadow-md max-w-md w-full">
                <slot>
                    
                </slot>
          <button
            @click="showPopup = false"
            class="mt-4 bg-red-500 text-white px-4 py-2 rounded"
          >
            Fermer
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  
  const showPopup = ref(false);
  </script>
  