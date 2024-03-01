//import layoutConfig from 'pages/apps/layout/layoutConfig.js'
import { skeletonConfig, skeletonRoute } from 'pages/apps/skeleton/skeletonConfig.js'
//import { knowledgeConfig, knowledgeRoute } from 'pages/apps/knowledge/knowledgeConfig.js'
//import { todoConfig, todoRoute } from 'pages/apps/todo/todoConfig.js'
//import { vaultConfig, vaultRoute } from 'pages/apps/vault/vaultConfig.js'
//import { contactConfig, contactRoute } from 'pages/apps/contact/contactConfig.js'
//import { calendarConfig, calendarRoute } from 'pages/apps/calendar/calendarConfig.js'
import { playgroundConfig, playgroundRoute } from 'pages/apps/playground/playgroundConfig.js'

//import { useAccountStore } from 'stores/AccountStore';
//const account = useAccountStore()

const installedApps = [
    //knowledgeConfig,
    //vaultConfig,
    //contactConfig,
    //calendarConfig,
    //layoutConfig,
    skeletonConfig,
    playgroundConfig,
    //todoConfig,
]
const guard = function(to, from, next) {
  if(localStorage.getItem('userAuthToken')) {
    next()
  } else {
    window.location.href = "/login"
  }
}

const appsRoute = {
    path: '/apps',
    name: 'Apps',
    component: () => import('pages/apps/layout/AppsLayout.vue'),
    beforeEnter: (to, from, next) => {
      guard(to, from, next)
    },
    children: [
      {
        path: '',
        component:() => import('pages/apps/layout/AppsHomeView.vue'),
        name: 'AppsHome',
      },
      skeletonRoute,
      //knowledgeRoute,
      //vaultRoute,
      //contactRoute,
      //calendarRoute,
      playgroundRoute,
      //todoRoute,
    ]
  }


export { installedApps, appsRoute }
