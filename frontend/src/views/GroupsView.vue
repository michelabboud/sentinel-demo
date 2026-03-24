<template>
  <div>
    <h1 class="text-3xl font-bold mb-6">{{ $t('groups.title') }}</h1>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <router-link v-for="group in groups" :key="group.id" :to="`/groups/${group.id}`"
        class="bg-white p-6 rounded-lg shadow hover:shadow-md transition">
        <h3 class="text-xl font-semibold">{{ group.name }}</h3>
        <p class="text-gray-500 mt-1">{{ group.description }}</p>
      </router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

const groups = ref<any[]>([])

onMounted(async () => {
  const token = localStorage.getItem('token')
  const { data } = await axios.get('/api/v1/groups/', { headers: { Authorization: `Bearer ${token}` } })
  groups.value = data
})
</script>
