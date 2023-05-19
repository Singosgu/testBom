import { defineStore } from "pinia";

export const useTableDataStore = defineStore("tabledata", {
	state: () => ({
		tableData: {
			column: [],
			originalRow: [],
			rowPerPage: [30, 100, 500, 1000],
			addOpen: false,
			searchOpen: false,
			editOpen: false,
			edit: {},
			delOpen: false,
			del: {},
		},
	}),

	getters: {
		getColumn: (state) => state.tableData.column,
		getoriginalRow: (state) => state.tableData.originalRow,
		getrowPerPage: (state) => state.tableData.rowPerPage,
		getaddOpen: (state) => state.tableData.addOpen,
		getsearchOpen: (state) => state.tableData.searchOpen,
		geteditOpen: (state) => state.tableData.editOpen,
		getedit: (state) => state.tableData.edit,
		getdelOpen: (state) => state.tableData.delOpen,
		getdel: (state) => state.tableData.del,
	},

	actions: {
		columnChange(e) {
			this.tableData.column = e;
		},
		originalRowChange(e) {
			this.tableData.originalRow = e;
		},
		addOpenChange(e) {
			this.tableData.addOpen = e;
		},
		searchOpenChange(e) {
			this.tableData.searchOpen = e;
		},
		editOpenChange(e) {
			this.tableData.editOpen = e;
		},
		editDataChange(e) {
			this.tableData.edit = e;
		},
		delOpenChange(e) {
			this.tableData.delOpen = e;
		},
		delDataChange(e) {
			this.tableData.del = e;
		},
	},
	persist: {
		enabled: true,
	},
});
