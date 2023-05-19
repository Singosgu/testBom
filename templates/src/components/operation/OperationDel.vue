<template>
	<!-- <q-btn round flat icon="spatial_audio" @click="showOperation">
		<q-tooltip class="bg-indigo" :offset="[10, 10]"> 操作教程 </q-tooltip>
	</q-btn> -->
	<div></div>
</template>

<script setup>
import { defineComponent, ref, onMounted, watch } from "vue";
import { useQuasar } from "quasar";
import { api } from "boot/axios";
import { useTableDataStore } from "stores/tableData";
const $q = useQuasar();
const store = useTableDataStore();
const props = defineProps({
	dataUrl: {
		default: "",
	},
});
watch(
	() => store.getdelOpen,
	(newValue) => {
		if (newValue) {
			$q.dialog({
				title: "警告",
				message: "是否进行删除?",
				ok: {
					label: "确定",
				},
				cancel: {
					label: "取消",
					color: "negative",
				},
				persistent: true,
			})
				.onOk(() => {
					const e = store.getdel;
					api.get(props.dataUrl + e.id + "/");

					// api.get();
					// console.log(e.id);
					console.log("确认删除----");
					store.delOpenChange(false);
				})
				.onCancel(() => {
					console.log("取消");
					store.delOpenChange(false);
				});
		}
	}
);

const showOperation = () => {
	$q.dialog({
		title: "警告",
		message: "是否进行删除?",
		ok: {
			label: "确定",
		},
		cancel: {
			label: "取消",
			color: "negative",
		},
		persistent: true,
	})
		.onOk(() => {
			api.get(e.id + "/" + dataUrl.value);
			console.log(e.id);
			console.log("确认删除----");
		})
		.onCancel(() => {
			console.log("取消");
		});
};
</script>
