import { defineStore } from 'pinia';

export const useAccountStore = defineStore('account', {
  state: () => ({
    counter: 0,
    name: "user",
    token: "",
  }),

  getters: {
    doubleCount (state) {
      return state.counter * 2;
    }
  },

  actions: {
    login() {
      this.user = "caspar"
      this.token = "1234"
    },
    increment () {
      this.counter++;
    }
  }
});
