<template>
  <q-toolbar>
    <q-btn icon="apps" flat dense :to="startPage" />
    <q-space />
    <q-btn-dropdown
      :label="entEntry"
      flat
      dense
    >
      <q-list v-for="item in entity" :key="item.name">
        <q-item
          clickable
          v-close-popup
          @click="item_click(item)"
        >
          <q-item-section>
            <q-item-label>{{item.name}}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
    <q-btn-dropdown  dropdown-icon="person" no-icon-animation flat dense >
      <q-list>
        <q-item >
          <q-item-section>
            <q-item-label>Dark Mode</q-item-label>
          </q-item-section>
          <q-item-section side>
        <q-toggle
          size="s"
          v-model="darkMode"
          color="blue"
          @update:model-value="switch_dark"
        />
          </q-item-section>
        </q-item>
        <hr>
        <q-item clickable >
          <q-item-section>
            <q-item-label>My Profile</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable >
          <q-item-section>
            <q-item-label>Settings</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable @click="logout">
          <q-item-section>
            <q-item-label>Log Out</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
  </q-toolbar>
</template>

<style>
</style>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useQuasar} from 'quasar'
import { useAccountStore } from 'stores/AccountStore';
import { useRouter } from 'vue-router'

const account = useAccountStore()
const router = useRouter()

const props = defineProps({
    startPage: { type: Object },
    entity: { type: Object },
  })
const $q = useQuasar()
account.refresh()
const entEntry = computed(() => account.getName)
const darkMode = ref(true)
$q.dark.set(darkMode.value)
const item_click = (item) => {
  entEntry.value = item.name
}
const switch_dark = (value) => {
  $q.dark.set(value)
}
const logout = () => {
  account.logout()
  router.push({name: "login"})
}
</script>
