<template>
    <Disclosure as="nav" class="bg-green-900  " v-slot="{ open }">
      <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
        <div class="relative flex h-16 items-center justify-between">
          <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
            <!-- Mobile menu button-->
            <DisclosureButton class="relative inline-flex items-center justify-center rounded-md p-2 text-green-400 hover:bg-green-100 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white">
              <span class="absolute -inset-0.5" />
              <span class="sr-only">Open main menu</span>
              <!-- <Bars3Icon v-if="!open" class="block size-6" aria-hidden="true" /> -->
              <!-- <XMarkIcon v-else class="block size-6" aria-hidden="true" /> -->
            </DisclosureButton>
          </div>
          <div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
            <div class="flex shrink-0 items-center">
              <RouterLink to="/">
                                <img class="h-14 w-auto" src="./icons/icons8-tachiyomi-50.png" alt="Your Company" />
                </RouterLink>
            </div>
            <div class="hidden sm:ml-6 sm:block">
              <div class="flex space-x-4">
                <a class="[item.current ? 'bg-green-900 text-white' : 'text-green-300 hover:bg-green-700 hover:text-white', 'rounded-md px-3 py-2 text-sm font-medium'] hover:rounded-xl" :aria-current="current ? 'page' : undefined"><RouterLink to="/">Home</RouterLink></a>
                <a class="[item.current ? 'bg-green-900 text-white' : 'text-green-300 hover:bg-green-700 hover:text-white', 'rounded-md px-3 py-2 text-sm font-medium'] hover:rounded-xl" :aria-current="current ? 'page' : undefined"><RouterLink to="/livres">Livres</RouterLink></a>
                <a class="[item.current ? 'bg-green-900 text-white' : 'text-green-300 hover:bg-green-700 hover:text-white', 'rounded-md px-3 py-2 text-sm font-medium'] hover:rounded-xl" :aria-current="current ? 'page' : undefined"><RouterLink to="/about">About</RouterLink></a>
              </div>
            </div>
          </div>
          <div class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
            <button type="button" class="relative rounded-full bg-green-800 p-1 text-green-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-green-900">
              <span class="absolute -inset-1.5" />
              <span class="sr-only">View notifications</span>
              <!-- <BellIcon class="size-6" aria-hidden="true" /> -->
            </button>
  
            <!-- Profile dropdown -->
            <Menu as="div" class="relative ml-3">
              <div>
                <MenuButton class="relative flex rounded-full bg-green-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-green-800">
                  <span class="absolute -inset-1.5" />
                  <span class="sr-only">Open user menu</span>
                  <img class="size-8 rounded-full " src="/public/icons8-manga-50.png" alt="" />
                </MenuButton>
              </div>
              <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
                <MenuItems class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-green/5 focus:outline-none">
                  <MenuItem v-slot="{ active }">
                    <a href="#" :class="[active ? 'bg-green-100 outline-none' : '', 'block px-4 py-2 text-sm text-green-700']">Your Profile</a>
                  </MenuItem>
                  <MenuItem v-slot="{ active }">
                    <a href="#" :class="[active ? 'bg-green-100 outline-none' : '', 'block px-4 py-2 text-sm text-green-700']">Settings</a>
                  </MenuItem>
                  <MenuItem v-slot="{ active }">
                    <a href="#" :class="[active ? 'bg-green-100 outline-none' : '', 'block px-4 py-2 text-sm text-green-700']">Sign out</a>
                  </MenuItem>
                </MenuItems>
              </transition>
            </Menu>
          </div>
        </div>
      </div>
  
      
    </Disclosure>
  </template>
  
  <script setup>
  import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import { ref } from 'vue';
const current = ref(true)
const onChangeCurrent=()=>{

}
  </script>