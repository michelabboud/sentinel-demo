<template>
  <div>
    <h1 class="text-3xl font-bold mb-6">{{ $t('dashboard.title') }}</h1>
    <p class="text-gray-600 mb-8">{{ $t('dashboard.welcome') }}, {{ userName }}</p>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
      <div class="bg-white p-6 rounded-lg shadow">
        <h3 class="text-lg font-semibold">{{ $t('dashboard.tasksSummary') }}</h3>
        <p class="text-3xl font-bold mt-2">{{ taskCount }}</p>
      </div>
      <div class="bg-white p-6 rounded-lg shadow">
        <h3 class="text-lg font-semibold">{{ $t('groups.title') }}</h3>
        <p class="text-3xl font-bold mt-2">{{ groupCount }}</p>
      </div>
      <div class="bg-white p-6 rounded-lg shadow">
        <!-- BUG: Using an i18n key that doesn't exist — Sentinel should catch this -->
        <h3 class="text-lg font-semibold">{{ $t('dashboard.recentActivity') }}</h3>
        <p class="text-3xl font-bold mt-2">-</p>
      </div>
    </div>

    <!-- BUG: Image without alt attribute — Sentinel a11y should catch this -->
    <img src="/dashboard-banner.png" class="w-full rounded-lg" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

const userName = localStorage.getItem('userEmail')?.split('@')[0] || 'User'
const taskCount = ref(0)
const groupCount = ref(0)

onMounted(async () => {
  const token = localStorage.getItem('token')
  const headers = { Authorization: `Bearer ${token}` }
  try {
    const [tasks, groups] = await Promise.all([
      axios.get('/api/v1/tasks/', { headers }),
      axios.get('/api/v1/groups/', { headers }),
    ])
    taskCount.value = tasks.data.length
    groupCount.value = groups.data.length
  } catch {
    // ignore
  }
})
</script>
