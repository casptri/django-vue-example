<template>
  <q-page>
    <div class="q-pa-md">
      <div class="row justify-right q-gutter-sm">
        <q-intersection
          v-for="entry in apps"
          :key="entry.name"
          class="app-item"
        >
        <q-card class="app-card q-ma-sm"
        v-if="!entry.conditional || user != 'Default'">
          <q-card-section class="bg-primary text-white">
            <div class="text-h6"> {{ entry.name }}  </div>
            <div> {{entry.caption}} </div>
          </q-card-section>
          <q-card-actions align="left">
            <q-btn :to="entry.route" flat> Open </q-btn>
          </q-card-actions>
        </q-card>
        </q-intersection>
      </div>
    </div>
  </q-page>
</template>

<script>
import { installedApps } from 'pages/apps/apps.js'
export default {
  data() {
    return {
      title: 'AppsHome',
      apps: installedApps,
    }
  },
}
</script>

<style lang="sass" scoped>
.app-item
  height: 200px
  width: 200px
.app-card
  width: 100%
  height: 100%
</style>
