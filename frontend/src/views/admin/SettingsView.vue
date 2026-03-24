<template>
  <div>
    <h1 class="text-3xl font-bold mb-6">{{ $t('nav.settings') }}</h1>
    <div class="bg-white p-6 rounded-lg shadow max-w-lg">
      <p class="text-gray-500">Application settings will go here.</p>
      <!-- BUG: This section uses a key that only exists in English -->
      <p class="mt-4 text-sm text-gray-400">{{ $t('errors.serverError') }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
