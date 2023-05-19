<!-- <template>
	<div>aaaa</div>
</template> -->

<template>
	<v-md-preview :text="text"></v-md-preview>
</template>
<script>
export default {
	name: "_md",
};
</script>
<script setup>
import { ref, reactive, onMounted } from "vue";
import VMdPreview from "@kangc/v-md-editor/lib/preview";
import vuepressTheme from "@kangc/v-md-editor/lib/theme/vuepress.js";
import "@kangc/v-md-editor/lib/style/base-editor.css";
import "@kangc/v-md-editor/lib/theme/style/vuepress.css";
import ReadMe from "boot/ReadMe.md?import&raw";
VMdPreview.use(vuepressTheme);
const text = ref(ReadMe);
</script>
