<template>
	<div class="q-pa-md">
		<q-table
			ref="tableRef"
			:class="{
				'my-sticky-header-table': action === false,
				'my-sticky-header-column-table': action === true,
			}"
			:rows="rows"
			:columns="columns"
			row-key="id"
			:rows-per-page-options="rowsPerPageOptions"
			v-model:pagination="pagination"
			rows-per-page-label="每页多少行"
			:loading="loading"
			:filter="filter"
			binary-state-sort
			@request="onRequest"
			:style="{ height: $q.screen.height - 85 + '' + 'px' }"
			bordered
		>
			<template v-slot:header="props">
				<q-tr :props="props">
					<q-th />
					<q-th
						v-for="col in props.cols"
						:key="col.name"
						:props="props"
					>
						{{ col.label }}
					</q-th>
				</q-tr>
			</template>
			<template v-slot:body="props">
				<q-tr :props="props" :key="`m_${props.row.index}`">
					<q-td>
						{{ props.rowIndex + 1 }}
					</q-td>
					<q-td
						v-for="col in props.cols"
						:key="col.name"
						:props="props"
					>
						<div v-if="col.value === true">
							<q-icon
								color="secondary"
								size="30px"
								name="check_circle_outline"
							></q-icon>
						</div>
						<div v-else-if="col.value === false">
							<q-icon
								color="brown-5"
								size="30px"
								name="clear"
							></q-icon>
						</div>
						<div v-else>
							<div v-if="col.name === 'action'">
								<q-btn
									round
									flat
									push
									color="purple"
									icon="edit"
									@click="editData(props.row)"
								>
									<q-tooltip
										content-class="bg-amber text-black shadow-4"
										:offset="[10, 10]"
										content-style="font-size: 12px"
									>
										{{ $t("edit") }}
									</q-tooltip>
								</q-btn>
								<q-btn
									round
									flat
									push
									color="dark"
									icon="delete"
									@click="deleteData(props.row)"
								>
									<q-tooltip
										content-class="bg-amber text-black shadow-4"
										:offset="[10, 10]"
										content-style="font-size: 12px"
									>
										{{ $t("delete") }}
									</q-tooltip>
								</q-btn>
								<!-- 分割线------------------- -->
								<q-btn
									no-caps
									push
									flat
									color="white"
									text-color="primary"
									label="权限"
									@click="show(true)"
								/>
							</div>
							<div v-else>
								{{ col.value }}
							</div>
						</div>
					</q-td>
				</q-tr>
			</template>
			<template v-slot:top-left>
				<q-btn-group push>
					<q-btn
						push
						color="primary"
						label="新增"
						icon="person_add_alt"
						@click="addOpenDrawer"
					/>
					<q-btn
						push
						color="primary"
						icon-right="archive"
						label="Export to csv"
						no-caps
					/>
				</q-btn-group>
				<OperationNote />
			</template>
			<template v-slot:top-right="props">
				<q-input
					borderless
					dense
					debounce="300"
					v-model="filter"
					:placeholder="$t('search')"
					@click="testSearch()"
				>
					<template v-slot:append>
						<q-icon name="search" />
					</template>
				</q-input>
				<q-btn
					flat
					round
					dense
					:icon="
						props.inFullscreen ? 'fullscreen_exit' : 'fullscreen'
					"
					@click="props.toggleFullscreen"
					class="q-ml-md"
				/>
			</template>
			<template v-slot:pagination="scope">
				总共：{{ pagination.rowsNumber }}行数据
				<q-btn
					v-if="scope.pagesNumber > 2"
					icon="first_page"
					color="grey-8"
					round
					dense
					flat
					:disable="scope.isFirstPage"
					@click="scope.firstPage"
				/>
				<q-btn
					icon="chevron_left"
					color="grey-8"
					round
					dense
					flat
					:disable="scope.isFirstPage"
					@click="scope.prevPage"
				/>
				<q-pagination
					v-model="scope.pagination.page"
					:max="scope.pagesNumber"
					:max-pages="10"
					boundary-numbers
					@click="onRequest(scope)"
				/>
				<q-btn
					icon="chevron_right"
					color="grey-8"
					round
					dense
					flat
					:disable="scope.isLastPage"
					@click="scope.nextPage"
				/>
				<q-btn
					v-if="scope.pagesNumber > 2"
					icon="last_page"
					color="grey-8"
					round
					dense
					flat
					:disable="scope.isLastPage"
					@click="scope.lastPage"
				/>
			</template>
			<template v-slot:no-data="{ icon, message, filter }">
				<div class="full-width row flex-center text-accent q-gutter-sm">
					<q-icon size="2em" name="sentiment_dissatisfied" />
					<span> Well this is sad... {{ message }} </span>
					<q-icon
						size="2em"
						:name="filter ? 'filter_b_and_w' : icon"
					/>
				</div>
			</template>
		</q-table>
	</div>
	<addData :columnData="columnData" :dataUrl="dataUrl"></addData>
	<searchData :columnData="columnData" :dataUrl="dataUrl"></searchData>
	<EditData :columnData="columnData" :dataUrl="dataUrl"></EditData>
	<delData :dataUrl="dataUrl" />
</template>

<script setup>
import { ref, onMounted, defineComponent, computed, nextTick } from "vue";
import { useTableDataStore } from "stores/tableData";
import OperationNote from "components/operation/OperationNote.vue";
import EditData from "./EditData.vue";
import addData from "./AddData.vue";
import searchData from "./SearchData.vue";
import delData from "components/operation/OperationDel.vue";
import { api } from "boot/axios";
import { useI18n } from "vue-i18n";
import { useQuasar } from "quasar";
const $q = useQuasar();
const show = (grid) => {
	$q.bottomSheet({
		message: "Bottom Sheet message",
		grid,
		actions: [
			{
				label: "Drive",
				img: "https://cdn.quasar.dev/img/logo_drive_128px.png",
				id: "drive",
			},
			{
				label: "Keep",
				img: "https://cdn.quasar.dev/img/logo_keep_128px.png",
				id: "keep",
			},
			{
				label: "Google Hangouts",
				img: "https://cdn.quasar.dev/img/logo_hangouts_128px.png",
				id: "calendar",
			},
			{
				label: "Calendar",
				img: "https://cdn.quasar.dev/img/logo_calendar_128px.png",
				id: "calendar",
			},
			{},
			{
				label: "Share",
				icon: "share",
				id: "share",
			},
			{
				label: "Upload",
				icon: "cloud_upload",
				color: "primary",
				id: "upload",
			},
			{},
			{
				label: "John",
				avatar: "https://cdn.quasar.dev/img/boy-avatar.png",
				id: "john",
			},
		],
	})
		.onOk((action) => {
			console.log("选择的:", action.id);
		})
		.onCancel(() => {
			console.log("取消");
		})
		.onDismiss(() => {
			console.log("在“确定”和“取消”时都被触发");
		});
};

const props = defineProps({
	data: {
		default: "",
	},
	_columns: {
		default: [],
	},
});
const columnData = ref(props._columns);
const dataUrl = ref(props.data);
const store = useTableDataStore();
const { t } = useI18n();
const tableRef = ref();
const columns = computed(() => store.getColumn);
const originalRows = computed(() => store.getoriginalRow);
const rowsPerPageOptions = computed(() => store.getrowPerPage);
const rows = ref([]);
const filter = ref("");
const loading = ref(false);
const action = ref(false);
const pagination = ref({
	sortBy: "id",
	descending: false,
	page: 1,
	rowsPerPage: 30,
	rowsNumber: 30,
});
const addOpen = ref(false);
const searchOpen = ref(false);

async function fetchFromServer(startRow, count, filter, sortBy, descending) {
	if (descending === false) {
		sortBy = "-" + sortBy;
	}
	//_column.data作为url传值
	await api
		.get(
			dataUrl.value +
				"?page=" +
				"" +
				pagination.value.page +
				"&max_page=" +
				"" +
				count +
				"&ordering=" +
				sortBy
		)
		.then((res) => {
			store.originalRowChange(res.data.results);
			pagination.value.rowsNumber = res.data.count;
		});
	return originalRows.value?.slice();
}

function onRequest(props) {
	const { page, rowsPerPage, sortBy, descending } = props.pagination;
	const filter = props.filter;
	loading.value = true;
	setTimeout(async () => {
		const fetchCount =
			rowsPerPage === 0 ? pagination.value.rowsNumber : rowsPerPage;
		const startRow = (page - 1) * rowsPerPage;
		const returnedData = await fetchFromServer(
			startRow,
			fetchCount,
			filter,
			sortBy,
			descending
		);

		rows.value?.splice(0, rows.value.length, ...returnedData);
		pagination.value.page = page;
		pagination.value.rowsPerPage = rowsPerPage;
		pagination.value.sortBy = sortBy;
		pagination.value.descending = descending;
		loading.value = false;
	}, 1000);
}

onMounted(() => {
	columns.value.forEach((item) => {
		if (item.name === "action") {
			action.value = true;
		}
	});
	tableRef.value.requestServerInteraction();
});
const addOpenDrawer = () => {
	addOpen.value = store.getaddOpen;
	addOpen.value = !addOpen.value;
	store.addOpenChange(addOpen.value);
};

const editData = (e) => {
	const editOpen = ref(false);
	store.editDataChange(e);
	editOpen.value = store.geteditOpen;
	editOpen.value = !editOpen.value;
	store.editOpenChange(editOpen.value);
};
//删除
const deleteData = (e) => {
	const delOpen = ref(false);
	store.delDataChange(e);
	delOpen.value = store.getdelOpen;
	delOpen.value = !delOpen.value;
	store.delOpenChange(delOpen.value);
};
const testSearch = () => {
	searchOpen.value = store.getsearchOpen;
	searchOpen.value = !searchOpen.value;
	store.searchOpenChange(searchOpen.value);
};
</script>
