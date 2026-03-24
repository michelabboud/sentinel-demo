<template>
  <div class="max-w-2xl">
    <h1 class="text-2xl font-bold mb-4">{{ task?.title }}</h1>
    <div class="bg-white p-6 rounded-lg shadow" v-if="task">
      <p class="text-gray-600 mb-4">{{ task.description || 'No description' }}</p>
      <div class="grid grid-cols-2 gap-4">
        <div><span class="font-medium">Status:</span> {{ task.status }}</div>
        <div><span class="font-medium">Priority:</span> {{ task.priority }}</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const task = ref<any>(null)

onMounted(async () => {
  const token = localStorage.getItem('token')
  const { data } = await axios.get(`/api/v1/tasks/${route.params.id}`, { headers: { Authorization: `Bearer ${token}` } })
  task.value = data
})
</script>
