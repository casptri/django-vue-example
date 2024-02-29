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

<script>
import UserHandler from 'components/auth/UserHandler.vue'

export default {
  data() {
    return {
      username: "",
      password: "",
    }
  },
  methods: {
    async doLogin () {
    console.log("do_login")
      UserHandler.login(this.username, this.password).then(response => {
          console.log(response)
          this.$router.push({name: "AppsHome"})
        }).catch(error => {
          console.log(error)
        })
    },
  },
  created() {
    let token = localStorage.getItem('userAuthToken')
    if(token) {
      console.log(token)
      this.$router.push({ name: 'AppsHome'})
    }
  }
}
</script>
<style>
h1 {
 font-size: 40px; 
}
</style>
