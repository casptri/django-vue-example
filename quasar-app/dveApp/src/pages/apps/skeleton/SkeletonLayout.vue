<template>
  <q-page>
    <div class="q-pa-md">
      <q-layout view="hHh Lpr lff" >
        {{title}}
      </q-layout>
    </div>
  </q-page>
</template>

<script>
//import { ref } from 'vue'
//import { api } from 'boot/axios'
//import { _ } from 'vue-underscore'
export default {
  name: 'SkeletonLayout',
  data() {
    return {
      title: 'skeleton',
    }
  },
}
</script>
<style>
</style>
