<template>
	<q-layout view="hHh lpr lfr">
		<q-header reveal elevated class="bg-primary text-white">
			<q-toolbar>
				<q-btn
					flat
					dense
					round
					icon="menu"
					aria-label="Menu"
					@click="toggleLeftDrawer"
				/>

				<q-toolbar-title> GreaterWMS </q-toolbar-title>
				<q-btn
					v-show="uploadShow"
					flat
					style="color: white"
					label="上传"
					@click="HandelUpload()"
				/>
				<LanguageChoice />
				<DarkMode />
				<FullScreen />
			</q-toolbar>
		</q-header>

		<q-drawer v-model="leftDrawerOpen" side="left" elevated>
			<q-list>
				<q-item-label header> 主菜单 </q-item-label>
				<EssentialLink :asyncRoutes="asyncRoutes" />
			</q-list>
		</q-drawer>

		<q-page-container>
			<router-view />
		</q-page-container>
	</q-layout>
</template>

<script setup>
import { defineComponent, onBeforeMount, onMounted, ref } from "vue";
import EssentialLink from "components/EssentialLink.vue";
import DarkMode from "components/headers/DarkMode.vue";
import FullScreen from "components/headers/FullScreen.vue";
import LanguageChoice from "components/headers/LanguageChoice.vue";
import { Platform, useQuasar } from "quasar";
import { usetokenStore } from "stores/token";
import asyncRoutes from "../router/routes";
import _Json from "../components/RouteModel/Router.js";

const essentialLinks = ref([]);
const leftDrawerOpen = ref(true);
const tokenStore = usetokenStore();

function checkUpdate() {
	if (Platform.is.electron) {
		require("electron").ipcRenderer.send(
			"checkForUpdate",
			"http://127.0.0.1:8000/media"
		);
	}
}
const uploadShow = ref(false);
onBeforeMount(() => {
	// require("electron").ipcRenderer.send("upLoadSoft");
	require("electron").ipcRenderer.send("isDev");
	require("electron").ipcRenderer.on("message", (event, arg) => {
		// console.log(arg);
		if (arg.cmd === "isDev") {
			uploadShow.value = arg.message.isDev;
		}
	});
	checkUpdate();
	essentialLinks.value = _Json;
	tokenStore.tokencheck();
});

onMounted(() => {
	// require('electron').ipcRenderer.send('isDev')
});
const HandelUpload = () => {
	require("electron").ipcRenderer.send("upLoadSoft");
};
const toggleLeftDrawer = () => (leftDrawerOpen.value = !leftDrawerOpen.value);
</script>
