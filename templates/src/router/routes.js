import constantRoutes from "./constant";
import * as mainRoutes from "components/RouteModel/Router";
import { i18n } from "boot/i18n";
const { t } = i18n.global;

const routes = [
	{
		path: "/",
		name: "首页",
		component: () => import("layouts/MainLayout.vue"),
		meta: { isHidden: true },
		children: [
			{
				path: "",
				name: "index",
				component: () => import("pages/IndexPage.vue"),
				meta: { isHidden: false },
			},
			{
				path: "test",
				name: "测试",
				component: () => import("pages/NewTest.vue"),
				meta: { isHidden: true },
			},
			{
				path: "user",
				name: "user",
				component: () => import("pages/user/UserProfile.vue"),
				meta: { isHidden: true },
			},
		],
	},
	{
		path: "/:catchAll(.*)*",
		name: ":catchAll(.*)*",
		meta: { isHidden: false },
		component: () => import("pages/ErrorNotFound.vue"),
	},

	...mainRoutes.default,
];

constantRoutes.forEach((item) => {
	routes.push(item);
});
export default routes;
