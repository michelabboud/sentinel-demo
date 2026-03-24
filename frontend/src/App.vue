<template>
  <div class="min-h-screen bg-gray-100">
    <nav class="bg-white shadow" v-if="isAuthenticated">
      <div class="max-w-7xl mx-auto px-4 flex justify-between h-16 items-center">
        <div class="flex gap-4">
          <router-link to="/dashboard" class="font-bold text-lg">TaskManager</router-link>
          <router-link to="/tasks" class="text-gray-600 hover:text-gray-900">{{ $t('nav.tasks') }}</router-link>
          <router-link to="/groups" class="text-gray-600 hover:text-gray-900">{{ $t('nav.groups') }}</router-link>
          <router-link to="/admin/users" v-if="isAdmin" class="text-gray-600 hover:text-gray-900">{{ $t('nav.users') }}</router-link>
          <router-link to="/admin/settings" v-if="isAdmin" class="text-gray-600 hover:text-gray-900">{{ $t('nav.settings') }}</router-link>
        </div>
        <div class="flex items-center gap-4">
          <span class="text-sm text-gray-500">{{ userEmail }}</span>
          <!-- BUG: Button with only icon, no aria-label — Sentinel a11y should catch this -->
          <button @click="logout" class="p-2 rounded hover:bg-gray-100">
            <img src="/logout-icon.svg" width="20" height="20" />
          </button>
        </div>
      </div>
    </nav>
    <main class="max-w-7xl mx-auto px-4 py-6">
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const isAuthenticated = computed(() => !!localStorage.getItem('token'))
const userEmail = computed(() => localStorage.getItem('userEmail') || '')
const isAdmin = computed(() => localStorage.getItem('userRole') === 'admin')

function logout() {
  localStorage.removeItem('token')
  localStorage.removeItem('userEmail')
  localStorage.removeItem('userRole')
  router.push('/login')
}
</script>
