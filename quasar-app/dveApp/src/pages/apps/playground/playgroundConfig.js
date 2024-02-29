const playgroundConfig = {
        name: 'Playground',
        route: {name: 'playground'},
        caption: 'App playground',
        icon: '',
    }

const playgroundRoute = {
        path: 'playground',
        component:() => import('pages/apps/playground/PlaygroundView.vue'),
        name: 'playground',
    }

export { playgroundConfig, playgroundRoute }
