<template>
	<q-btn
		round
		dense
		flat
		color="white"
		icon="translate"
		style="margin: 0 10px 0 10px"
	>
		<q-menu>
			<q-list style="min-width: 100px">
				<q-item
					clickable
					v-close-popup
					v-for="(language, index) in langOptions"
					:key="index"
					@click="store.LanguageChange(language.value)"
				>
					<q-item-section>{{ language.label }}</q-item-section>
				</q-item>
			</q-list>
		</q-menu>
	</q-btn>
</template>

<script setup>
import { computed, watch } from "vue";
import { useLanguageStore } from "stores/language";
import { useI18n } from "vue-i18n";
const langstest = useI18n();
const store = useLanguageStore();
const lang = computed(() => store.lang);
const langOptions = [
	{ value: "en-US", label: "English" },
	{ value: "zh-hans", label: "中文简体" },
	{ value: "zh-hant", label: "中文繁體" },
	{ value: "fr", label: "Français" },
	{ value: "pt", label: "Português" },
	{ value: "sp", label: "Español" },
	{ value: "de", label: "Deutsch" },
	{ value: "ru", label: "русский язык" },
	{ value: "ar", label: "Arabic" },
	{ value: "it", label: "Italiano" },
	{ value: "ja", label: "日本語" },
];

watch(
	() => lang.value,
	(newValue) => {
		langstest.locale.value = newValue;
		localStorage.setItem("lang", newValue);
		location.reload();
	}
);
</script>
