<template>
  <q-layout view="lHh Lpr lff">
    <q-header
      reveal
    >
      <AppsToolbar :startPage="startPage" :entity="entityList" />
    </q-header>
    <q-page-container>
      <q-page class="row no-wrap">
        <div class="col">
          <div class="full-height">
            <q-scroll-area class="col q-pr-sm full-height" visible>
              <router-view />
            </q-scroll-area>
          </div>
        </div>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
  import { ref } from 'vue'
  import AppsToolbar from 'pages/apps/layout/AppsToolbar.vue'

  const startPage = ref({name: 'AppsHome'})
  //let entityList = ref([{name: 'Caspar'},{name: 'Ghost Inc'}])
  const entityList = ref([])


</script>

<style>
h1 {
  font-size: 40px;
}
h2 {
  font-size: 32px;
}
</style>
