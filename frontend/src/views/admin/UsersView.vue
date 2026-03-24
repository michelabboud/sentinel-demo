<template>
  <div>
    <h1 class="text-3xl font-bold mb-6">{{ $t('nav.users') }}</h1>
    <div class="bg-white rounded-lg shadow overflow-hidden">
      <table class="w-full">
        <thead class="bg-gray-50">
          <tr>
            <th class="px-4 py-3 text-left">Name</th>
            <th class="px-4 py-3 text-left">Email</th>
            <th class="px-4 py-3 text-left">Role</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id" class="border-t">
            <td class="px-4 py-3">{{ user.name }}</td>
            <td class="px-4 py-3">{{ user.email }}</td>
            <td class="px-4 py-3">
              <span class="px-2 py-1 rounded text-xs font-medium"
                :class="{'bg-red-100 text-red-700': user.role === 'admin', 'bg-yellow-100 text-yellow-700': user.role === 'manager', 'bg-gray-100 text-gray-700': user.role === 'user'}">
                {{ user.role }}
              </span>
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

const users = ref<any[]>([])

onMounted(async () => {
  const token = localStorage.getItem('token')
  const { data } = await axios.get('/api/v1/users/', { headers: { Authorization: `Bearer ${token}` } })
  users.value = data
})
</script>
