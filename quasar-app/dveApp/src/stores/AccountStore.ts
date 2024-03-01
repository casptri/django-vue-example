import { defineStore } from 'pinia';
import UserHandler from 'components/auth/UserHandler.vue'

export const useAccountStore = defineStore('account', {
  state: () => ({
    name: null,
    token: null,
  }),

  getters: {
    getToken (state) {
      return this.token
    },
    getName (state) {
      return this.name
    }
  },

  actions: {
    async login(username, password) {
      const data = await UserHandler.getToken(username, password)
      this.name = data.username
      this.token = data.access
      localStorage.setItem('userAuthToken', data.refresh)
      return true
    },
    async checkLogged() {
      if (this.token) {
        return true
      }
      if (localStorage.getItem('userAuthToken')) {
        return this.refresh()
      }
      return false
    },
    async refresh() {
      if (!this.token) {
        const refreshToken = localStorage.getItem('userAuthToken')
        if (refreshToken) {
          this.token = await UserHandler.refresh(refreshToken)
          const me = await UserHandler.getMe()
          this.name = me.username
        }
      }
      return true
    },
    logout() {
      localStorage.removeItem('userAuthToken')
      this.user = null
      this.token = null
    },
  }
});
