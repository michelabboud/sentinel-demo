<template>
  <div class="flex items-center justify-center min-h-[80vh]">
    <div class="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
      <h1 class="text-2xl font-bold mb-6">{{ $t('login.title') }}</h1>
      <form @submit.prevent="handleLogin">
        <!-- BUG: Missing label element — Sentinel a11y should catch this -->
        <div class="mb-4">
          <input v-model="email" type="email" placeholder="Email" class="w-full border rounded px-3 py-2" />
        </div>
        <!-- BUG: Missing label element — Sentinel a11y should catch this -->
        <div class="mb-6">
          <input v-model="password" type="password" placeholder="Password" class="w-full border rounded px-3 py-2" />
        </div>
        <p v-if="error" class="text-red-500 text-sm mb-4">{{ $t('login.error') }}</p>
        <button type="submit" class="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700">
          {{ $t('login.submit') }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const email = ref('')
const password = ref('')
const error = ref(false)
const router = useRouter()

async function handleLogin() {
  try {
    const { data } = await axios.post('/api/v1/auth/login', {
      email: email.value,
      password: password.value,
    })
    localStorage.setItem('token', data.access_token)
    localStorage.setItem('userEmail', email.value)
    // Extract role from JWT payload
    const payload = JSON.parse(atob(data.access_token.split('.')[1]))
    localStorage.setItem('userRole', payload.role)
    router.push('/dashboard')
  } catch {
    error.value = true
  }
}
</script>
