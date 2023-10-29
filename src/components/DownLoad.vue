<script setup lang="ts">
  const props = defineProps<{
    url: string
    isURL: boolean
  }>()

  const startDownload = () => {
    console.log(props.url)
  }
</script>

<template>
  <div>
    <button class="btn" @click="startDownload">Start download!</button>
  </div>
</template>