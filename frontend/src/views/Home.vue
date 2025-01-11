

<template>
  <div class="carousel"> 
    <div class="carousel-inner">
      <div class="carousel-item" v-for="(item, index) in slides " key="item.id" :class="{'active':currentIndex === index}">
        <img :src="item.chr" alt="" class="max-w-full h-auto object-cover">
      </div>
    </div>
     <!-- Boutons de navigation -->
     <button @click="prev" class="carousel-control-prev">&#10094;</button>
    <button @click="next" class="carousel-control-next">&#10095;</button>

  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';


const slides=ref([
  
    {id:'1',chr:'/public/photo_2024-12-15_15-20-14.jpg'},
    {id:'2',chr:'/public/photo_2024-12-15_15-20-03.jpg'},
    {id:'3',chr:'/public/photo_2024-12-15_15-19-44.jpg'},
    {id:'4',chr:'/public/photo_2024-12-15_15-19-55.jpg'},
    {id:'5',chr:'/public/photo_2024-12-15_15-20-03.jpg'},
    {id:'1',chr:'/public/photo_2024-12-15_15-20-14.jpg'},
    {id:'2',chr:'/public/photo_2024-12-15_15-20-03.jpg'},
    {id:'3',chr:'/public/photo_2024-12-15_15-19-44.jpg'},
    {id:'4',chr:'/public/photo_2024-12-15_15-19-55.jpg'},
    {id:'5',chr:'/public/photo_2024-12-15_15-20-03.jpg'},
  
]);
const currentIndex = ref(0)

const next=()=>{
  currentIndex.value = (currentIndex.value+1) % slides.value.length;

};
const prev = ()=>{
  currentIndex.value =(currentIndex.value-1)%slides.value;
};
onMounted(()=>{
  setInterval(()=>{
    next();
  },3000);
})

</script>

<style scoped>
.carousel {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.carousel-inner {
  position: relative;
  width: 900px;
  height: 400px;
  overflow: hidden;
}

.carousel-item {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  opacity: 0;
  transition: opacity 0.5s ease;
}

.carousel-item.active {
  opacity: 1;
}

.carousel-control-prev,
.carousel-control-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  padding: 10px;
  font-size: 24px;
  cursor: pointer;
}

.carousel-control-prev {
  left: 10px;
}

.carousel-control-next {
  right: 10px;
}

.carousel-control-prev:hover,
.carousel-control-next:hover {
  background-color: rgba(0, 0, 0, 0.7);
}
</style>
