const skeletonConfig = {
              name: 'Skeleton',
              route: {name: 'Skeleton'},
              caption: 'App Skeleton',
              icon: '',
          }

const skeletonRoute = {
        path: 'skeleton',
        component:() => import('pages/apps/skeleton/SkeletonLayout.vue'),
        name: 'Skeleton',
    }

export { skeletonConfig, skeletonRoute }
