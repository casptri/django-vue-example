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

  const store = useAccountStore();
  let title = ref('playground')
</script>

<style>
</style>
