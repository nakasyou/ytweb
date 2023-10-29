<script setup lang="ts">
  import { ref } from "vue"
  import DownLoad from "./DownLoad.vue"

  const isURL = ref(false)
  const urlInput = (e: Event) => {
    const text = (e.target as HTMLInputElement).value
    try {
      const url: URL = new URL(text)
      if(!["http:", "https:"].includes(url.protocol) || !url.host.includes("."))
        isURL.value = false
      else
        isURL.value = true
    }catch (error) {
      if (error instanceof TypeError) {
        isURL.value = false
      }else {
        throw error
      }
    }
  }

  const url = ref("")
</script>
<template>
  <div>
    <div class="text-3xl text-center font-bold">Ytdl-Web</div>
    <div class="mx-auto text-center">
      <p>Ytdl-Web は、オープンソースのYouTube動画ダウンローラーです。</p>
    </div>
    <div class="mx-auto text-center">
      <div>
        <label>URLを入力:</label>
        <input
          class="input w-full max-w-xs border "
          v-on:input="urlInput"
          :class="{
            'input-success': isURL,
            'input-error': !isURL,
          }"
          v-model="url"
        />
        <div>{{ isURL ? "" : "URLが不正ですね~" }}</div>
      </div>
      <div class="my-10">
        <DownLoad :url="url" :isURL="isURL" />
      </div>
    </div>
  </div>
</template>
