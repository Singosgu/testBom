import { watch } from "vue";
import { boot } from "quasar/wrappers";
import { createI18n } from "vue-i18n";
import messages from "src/i18n";
import { useLanguageStore } from "stores/language";
// const store = useLanguageStore();
// console.log(useLanguageStore());
export let i18n = createI18n({
	locale: localStorage.getItem("lang"),
	// locale: "zh-hans",
	globalInjection: true,
	messages,
});

export default boot(({ app }) => {
	// Set i18n instance on app
	app.use(i18n);
});
