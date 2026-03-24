<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold">{{ $t('tasks.title') }}</h1>
      <button @click="showCreate = true" class="bg-blue-600 text-white px-4 py-2 rounded">
        {{ $t('tasks.create') }}
      </button>
    </div>
    <div class="bg-white rounded-lg shadow overflow-hidden">
      <table class="w-full">
        <thead class="bg-gray-50">
          <tr>
            <th class="px-4 py-3 text-left text-sm font-medium text-gray-500">Title</th>
            <th class="px-4 py-3 text-left text-sm font-medium text-gray-500">Status</th>
            <th class="px-4 py-3 text-left text-sm font-medium text-gray-500">Priority</th>
            <th class="px-4 py-3 text-left text-sm font-medium text-gray-500">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="task in tasks" :key="task.id" class="border-t">
            <td class="px-4 py-3">
              <router-link :to="`/tasks/${task.id}`" class="text-blue-600 hover:underline">{{ task.title }}</router-link>
            </td>
            <td class="px-4 py-3">
              <span :class="statusClass(task.status)" class="px-2 py-1 rounded text-xs font-medium">
                {{ $t(`tasks.status.${task.status}`) }}
              </span>
            </td>
            <td class="px-4 py-3">{{ $t(`tasks.priority.${task.priority}`) }}</td>
            <td class="px-4 py-3">
              <!-- BUG: Click handler on div without keyboard support — Sentinel a11y should catch -->
              <div @click="deleteTask(task.id)" class="text-red-500 cursor-pointer">
                {{ $t('tasks.delete') }}
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

const tasks = ref<any[]>([])
const showCreate = ref(false)

function statusClass(status: string) {
  return {
    'bg-gray-100 text-gray-700': status === 'todo',
    'bg-blue-100 text-blue-700': status === 'in_progress',
    'bg-green-100 text-green-700': status === 'done',
  }
}

async function deleteTask(id: string) {
  if (!confirm('Delete this task?')) return
  const token = localStorage.getItem('token')
  await axios.delete(`/api/v1/tasks/${id}`, { headers: { Authorization: `Bearer ${token}` } })
  tasks.value = tasks.value.filter(t => t.id !== id)
}

onMounted(async () => {
  const token = localStorage.getItem('token')
  const { data } = await axios.get('/api/v1/tasks/', { headers: { Authorization: `Bearer ${token}` } })
  tasks.value = data
})
</script>
