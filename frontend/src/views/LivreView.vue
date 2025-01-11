<template>
  <div>
    <Popup>
      <LivreForm @addLivreTolist="fetchLivres" />
    </Popup>
    <!-- <div v-show="etat === true"> -->

    <!-- </div> -->
    <div class="bg-white" v-if="livres.length !== 0">
      <div
        class="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-5xl lg:px-8"
      >
        <h2 class="text-2xl font-bold tracking-tight text-gray-900">
          Bibliotheque Mangalib
        </h2>
        <div
          class="mt-1 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8"
        >
          <div v-for="livre in livres" :key="livre.id" class="group relative">
            <img
              src="/public/photo.jpg"
              :alt="livre.imageAlt"
              class="aspect-square w-full rounded-md bg-gray-200 object-cover group-hover:opacity-75 lg:aspect-auto lg:h-80"
            />
            <div class="mt-1 flex justify-between">
              <div>
                <h3 class="text-sm text-gray-700">
                  <RouterLink :to="`/livre/${livre.id}`">
                    <span aria-hidden="true" class="absolute inset-0" />
                    {{ livre.titre }}
                  </RouterLink>
                </h3>
                <p class="mt-1 text-sm text-gray-500">{{ livre.titre }}</p>
              </div>
              <p class="text-sm font-medium text-gray-900">
                {{ livre.quantity }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="bg-white" v-else>
      <div
        class="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-5xl lg:px-8"
      >
        <h2 class="text-2xl font-bold tracking-tight text-gray-900">
          Aucun livre trouvé
        </h2>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import LivreForm from "./LivreForm.vue";
import Popup from "../components/Popup.vue";
const apiUrl = import.meta.env.VITE_API_URL;
// Déclarer une variable réactive pour stocker les livres
const livres = ref([]);
const etat = ref(false);

// Fonction pour récupérer les livres
const fetchLivres = () => {
  // console.log("fetchLivres appelé");
  axios
    .get(`${apiUrl}/livre/`)
    .then((response) => {
      livres.value = response.data;
      // console.log("Données récupérées :", response.data);
    })
    .catch((error) => {
      console.error("Erreur lors de la récupération des livres:", error);
    });
};

onMounted(fetchLivres);
</script>
