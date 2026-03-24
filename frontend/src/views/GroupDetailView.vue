<template>
  <div class="max-w-2xl">
    <h1 class="text-2xl font-bold mb-4">{{ group?.name }}</h1>
    <div class="bg-white p-6 rounded-lg shadow" v-if="group">
      <p class="text-gray-600 mb-4">{{ group.description }}</p>
      <h3 class="font-semibold mb-2">{{ $t('groups.members') }}</h3>
      <p v-if="!members.length" class="text-gray-400">{{ $t('groups.noMembers') }}</p>
      <ul v-else>
        <li v-for="m in members" :key="m.id" class="py-1">{{ m.name }} ({{ m.task_count }} tasks)</li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const group = ref<any>(null)
const members = ref<any[]>([])

onMounted(async () => {
  const token = localStorage.getItem('token')
  const headers = { Authorization: `Bearer ${token}` }
  const [groupRes, membersRes] = await Promise.all([
    axios.get(`/api/v1/groups/${route.params.id}`, { headers }),
    axios.get(`/api/v1/groups/${route.params.id}/members`, { headers }),
  ])
  group.value = groupRes.data
  members.value = membersRes.data
})
</script>
