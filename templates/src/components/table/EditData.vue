<template>
	<q-drawer v-model="editOpen" side="right" overlay elevated>
		<div class="q-pa-md">
			<q-input
				v-for="i in inputData"
				:key="i"
				outlined
				style="margin-bottom: 10px"
				v-model="i.data.data"
				:label="i.field"
			/>
			<q-toggle
				v-for="item in toggleData"
				:key="item.field"
				v-model="item.toggle"
				>{{ item.field }}</q-toggle
			>

			<q-select
				v-for="(i, index) in selectData"
				:key="index"
				filled
				v-model="i.data.data"
				use-input
				hide-selected
				fill-input
				input-debounce="0"
				:options="options"
				@filter="filterFn"
				:label="i.label"
				@input-value="clickFn(i)"
				hint="Minimum 2 characters to trigger filtering"
				style="width: 250px; padding-bottom: 32px"
			>
				<template v-slot:no-option>
					<q-item>
						<q-item-section class="text-grey">
							No results
						</q-item-section>
					</q-item>
				</template>
			</q-select>

			<q-separator spaced />
			<q-btn icon="close" label="取消" @click="editOpen = false"></q-btn>
			<q-btn
				color="primary"
				icon="check"
				label="提交"
				@click="clickHandel()"
			></q-btn>
		</div>
	</q-drawer>
</template>
<script setup>
import { ref, watch, onMounted, computed } from "vue";
import { api } from "boot/axios";
import { useTableDataStore } from "stores/tableData";
//接收父组件

const props = defineProps({
	columnData: {
		default: [],
	},
	dataUrl: {
		default: "",
	},
});
// console.log(props.columnData);
//定义pinia
const store = useTableDataStore();
const editOpen = ref(store.geteditOpen);
// const rowsgetedit = computed(() => store.getedit);
const is_testSelect = computed(() => store.getoriginalRow);
const rowsgetedit = ref({});
//存放pinia里存储的本条数据
const keysArr = ref([]);
const newKeysArr = ref([]);
// keysArr.value = Object.keys(store.getedit);
//存储父组件表头
const itemData = ref(props.columnData);
const inputData = ref([]);
const toggleData = ref([]);
const selectData = ref([]);

watch(
	() => store.geteditOpen,
	(newValue) => (editOpen.value = newValue)
);
watch(
	() => editOpen.value,
	(newValue) => store.editOpenChange(newValue)
);
watch(
	() => store.getedit,
	(newValue) => {
		rowsgetedit.value = newValue;
		keysArr.value = Object.keys(rowsgetedit.value);
		//数据重构树形
		newKeysArr.value = Object.keys(rowsgetedit.value).map((key) => ({
			field: key,
			data: rowsgetedit.value[key],
		}));

		//重构所有元素
		itemData.value.map((el) => {
			return (el.data = newKeysArr.value.find(
				(item) => item.field == el.field
			));
		});

		//input框数据
		inputData.value = itemData.value.filter((i) => i.input);
		//toggle数据
		toggleData.value = itemData.value.filter(
			(i) => i.toggle === true || i.toggle === false
		);
		//选择框数据
		selectData.value = itemData.value.filter((i) => i.select);
	}
);

// console.log(itemData.value);
// console.log(newKeysArr.value);
// console.log(itemData.value);

//下拉框
const stringOptions = ["Google", "Facebook", "Twitter", "Apple", "Oracle"];
const options = ref(stringOptions);
const testindex = ref("");
const clickFn = (e) => {
	testindex.value = e.url;
	// console.log(selectData.value[testindex.value].url);
};
const filterFn = (val, update, abort) => {
	if (val.length < 2) {
		abort();
		return;
	}
	//此处调接口取数据
	update(() => {
		//needle为输入框数据
		api.get(props.dataUrl + "?" + testindex.value + "=" + val);
		const needle = val.toLowerCase();
		//过滤出可显示输入框数据
		options.value = stringOptions.filter(
			(v) => v.toLowerCase().indexOf(needle) > -1
		);
	});
};
//确定事件
const clickHandel = () => {
	/* selectData.value.forEach((item) => {
		// console.log(item.field);
		is_testSelect.value.filter((el) => {
			console.log(el);
		});
	}); */
	// console.log(selectData.value);
	// console.log(is_testSelect.value);
	// console.log(props.dataUrl);
	// console.log(all.value);
	// api.get(rowsgetedit.value.id + "/" + props.dataUrl);
	// api.get(rowsgetedit.value.id + "?page=" + "");
	// console.log(rowsgetedit.value);
	// console.log(newKeysArr.value, "----");
	// console.log(all.value, "修改后的数据");
};
</script>
