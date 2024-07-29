<template>
  <q-page>
    <div class="q-pa-md">
      <q-layout view="hHh Lpr lff" >
        {{ title }}
        <div>{{ store.name }} </div>
        <CustomUploader />
      </q-layout>
    </div>
  </q-page>
</template>

<script setup lang="ts">
  import { ref } from 'vue'
  import CustomUploader from 'pages/apps/playground/CustomUploader.vue'
  import { useAccountStore } from 'stores/AccountStore';

  const mode = process.env.MODE
  console.log(`mode is:${mode}`)

  var some_val = 455
  if (import.meta.env.VITE_SOME_KEY) {
    some_val = import.meta.env.VITE_SOME_KEY
    console.log("got here")
  }
  const more = some_val
  console.log(more)
  console.log(import.meta.env.VITE_SOME_KEY)
  if (process.env.DEV) {
    console.log(`I'm on a development build`)
  }

  const store = useAccountStore();
  let title = ref('playground')
</script>

<style>
</style>
