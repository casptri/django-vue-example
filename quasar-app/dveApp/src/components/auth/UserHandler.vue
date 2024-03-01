<script>
import { api } from 'boot/axios'
export default {
  name: 'UserHandler',
  async testF() {
    return "Hello world"
  },
  async getToken(username, password) {
    return new Promise((resolve, reject) => {
      const bodyData = {
        username: username,
        password: password,
      }
      const dataUrl = 'auth/token/pair'
      api.post(dataUrl, bodyData).then(response =>
      {
        resolve(response.data)
      }).catch(error =>
      {
        reject(error)
      })
    })
  },
  async refresh(token) {
    return new Promise((resolve, reject) => {
      const bodyData = {
        refresh: token,
      }
      const dataUrl = 'auth/token/refresh'
      api.post(dataUrl, bodyData).then(response =>
      {
        resolve(response.data.access)
      }).catch(error =>
      {
        reject(error)
      })
    })
  },
  async login(username, password) {
    return new Promise((resolve, reject) => {
      const bodyData = {
        username: username,
        password: password,
      }
      const dataUrl = 'auth/token/pair'
      api.post(dataUrl, bodyData).then(response =>
      {
        let token = response.data.access
        localStorage.setItem('userAuthToken',token)
        resolve(token)
      }).catch(error =>
      {
        reject(error)
      })
    })
  },
  async logout() {
    return new Promise((resolve) => {
        localStorage.removeItem('userAuthToken')
        resolve("logged out")
      })
    //return new Promise((resolve,reject) => {
    //  let token = localStorage.getItem('userAuthToken')
    //  if(token) {
    //    const dataUrl = 'auth/token/logout/'
    //    api.post(dataUrl, token).then(response =>
    //    {
    //      localStorage.removeItem('userAuthToken')
    //      resolve(response.data)
    //    }).catch(error =>
    //    {
    //      reject(error)
    //    })
    //  }  else {
    //    reject("already logged out")
    //  }
    //})
  },
  async getMe() {
    return new Promise((resolve,reject) => {
      const dataUrl = 'auth/me'
      api.get(dataUrl).then(response =>
      {
        resolve(response.data)
      }).catch(error =>
      {
        reject(error)
      })
    })
  },
};
</script>
