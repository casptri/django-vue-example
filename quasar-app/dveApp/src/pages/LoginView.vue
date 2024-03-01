<template>
<q-layout view="lHh LpR lFf">
  <q-page-container>
  <q-page class="window-height window-width row justify-center items-center">
  <div class="q-pa-md">
    <div class="q-gutter-y-md column" style="max-width: 300px">
    <q-input outlined v-model="username" label="Username"/>
    <q-input outlined v-model="password" label="Password" type="password"/>
    <q-btn
      color="white"
      text-color="black"
      label="Login"
      @click="doLogin"
    />
    </div>
  </div>
  </q-page>
  </q-page-container>
</q-layout>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useAccountStore } from 'stores/AccountStore';
import { useRouter } from 'vue-router'

const account = useAccountStore()
const router = useRouter()

let username = ref("")
let password = ref("")
let doLogin = async () => {
  await account.login(username.value, password.value)
  router.push({name: "AppsHome"})
}

</script>
<style>
h1 {
 font-size: 40px; 
}
</style>
