import { i18n } from "boot/i18n";
const { t } = i18n.global;
export default [
	/* {
		path: "/menu_Three",
		name: `${t("index.app_title")}`,

		component: () => import("layouts/MainLayout.vue"),
		children: [
			{
				path: "/menu_Three",
				name: "二级菜单",
				component: () => import("pages/menu_Three/index.vue"),
				children: [
					{
						path: "/menu_Three",
						name: "三级菜单",
						component: () => import("pages/menu_Three/index.vue"),
					},
				],
			},
		],
	},
	{
		path: "/menu_Two",
		name: "一级",
		component: () => import("layouts/MainLayout.vue"),
		children: [
			{
				path: "/menu_Two",
				name: "二级",
				component: () => import("pages/menu_Two/index.vue"),
			},
		],
	}, */
	{
		path: "/md",
		name: "应用文档",
		component: () => import("layouts/MainLayout.vue"),
		children: [
			{
				path: "/md",
				name: "应用使用文档",
				component: () => import("pages/md/index.vue"),
			},
		],
	},
];
