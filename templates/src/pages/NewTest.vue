<template>
	<div><MainTable :_columns="column" :_data="data"></MainTable></div>
</template>

<script setup>
import MainTable from "components/table/MainTable.vue";
import { useI18n } from "vue-i18n";
const { t } = useI18n();
import { defineComponent, ref } from "vue";
//必传项 data为url,column为标头
const data = ref("user/list/");
/* const data = ref({
	get: "1111",
	del: "2222+1",
}); */
const column = ref([
	{
		name: "username",
		required: true,
		label: `${t("action")}`,
		align: "left",
		field: "username",
		sortable: true,
		isShow: true, //是否展示新增
		input: true, //修改input框
		search: true, //是否显示搜索
		txt: "",
	},
	{
		name: "email",
		label: "email",
		field: "email",
		select: true /* 开启下拉框url必传 */,
		url: "email__icontains" /* 开启下拉框url必传 */,
		sortable: true,
		isShow: true,
		input: false,
		search: true, //是否显示搜索
		txt: "",
	},
	{
		name: "phone",
		label: "phone",
		field: "phone",
		select: true /* 开启下拉框url必传 */,
		url: "phone__icontains" /* 开启下拉框url必传 */,
		sortable: true,
		search: true, //是否显示搜索
		// toggle: false,
		// input: true,
	},
	{
		name: "is_active",
		label: "is_active",
		field: "is_active",
		sortable: true,
		search: true, //是否显示搜索
		toggle: true,
		search: true,
	},
	{
		name: "date_joined",
		label: "date_joined",
		field: "date_joined",
		search: true, //是否显示搜索
		sortable: true,
	},
	{
		name: "last_login",
		label: "last_login",
		field: "last_login",
		search: true, //是否显示搜索
		sortable: true,
	},
	{ name: "action", label: `${t("action")}`, align: "right" },
]);
</script>

<style scoped></style>
