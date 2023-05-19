import {
	app,
	BrowserWindow,
	nativeTheme,
	ipcMain,
	dialog,
	net,
} from "electron";
import { autoUpdater } from "electron-updater";
import isDev from "electron-is-dev";
import path from "path";
import os from "os";
import fs from "fs";

// needed in case process is undefined under Linux
const platform = process.platform || os.platform();
const baseUrlFolder = path.resolve(
	__dirname,
	process.env.QUASAR_PUBLIC_FOLDER,
	"statics/baseurl.txt"
);

try {
	if (platform === "win32" && nativeTheme.shouldUseDarkColors === true) {
		require("fs").unlinkSync(
			path.join(app.getPath("userData"), "DevTools Extensions")
		);
	}
} catch (_) {}

process.env["ELECTRON_DISABLE_SECURITY_WARNINGS"] = "true";

let mainWindow;

function createWindow() {
	/**
	 * Initial window options
	 */
	mainWindow = new BrowserWindow({
		icon: path.resolve(__dirname, "icons/icon.png"), // tray icon
		width: 1000,
		height: 600,
		useContentSize: true,
		webPreferences: {
			nodeIntegration: true,
			contextIsolation: false,
			// More info: https://v2.quasar.dev/quasar-cli-vite/developing-electron-apps/electron-preload-script
			preload: path.resolve(
				__dirname,
				process.env.QUASAR_ELECTRON_PRELOAD
			),
		},
	});
	// mainWindow.maximize()
	mainWindow.loadURL(process.env.APP_URL);
	// if (isDev) {
	mainWindow.webContents.openDevTools();
	// }
	mainWindow.setMenuBarVisibility(false);
	mainWindow.on("closed", () => {
		mainWindow = null;
	});

	if (!isDev || isDev) {
		autoUpdater.autoDownload = false;
		autoUpdater.allowDowngrade = true;
		autoUpdater.on("error", (error) => {
			sendUpdateMessage({
				cmd: "error",
				message: error,
			});
		});
		autoUpdater.on("checking-for-update", (info) => {
			sendUpdateMessage({
				cmd: "checking-for-update",
				message: info,
			});
		});
		autoUpdater.on("update-available", (info) => {
			sendUpdateMessage({
				cmd: "update-available",
				message: info,
			});
		});
		autoUpdater.on("update-not-available", (info) => {
			sendUpdateMessage({
				cmd: "update-not-available",
				message: info,
			});
		});
		autoUpdater.on("download-progress", function (progressObj) {
			sendUpdateMessage({
				cmd: "download-progress",
				message: progressObj,
			});
		});
		autoUpdater.on(
			"update-downloaded",
			function (
				event,
				releaseNotes,
				releaseName,
				releaseDate,
				updateUrl
			) {
				sendUpdateMessage({
					cmd: "update-downloaded",
					message: {
						releaseNotes: releaseNotes,
						releaseName: releaseName,
						releaseDate: releaseDate,
						updateUrl: updateUrl,
					},
				});
			}
		);
		ipcMain.on("checkForUpdate", (e, arg) => {
			autoUpdater.setFeedURL(arg);
			autoUpdater.checkForUpdates();
		});
		ipcMain.on("downloadUpdate", (e, arg) => {
			autoUpdater.downloadUpdate();
		});
		ipcMain.on("updateNow", (e, arg) => {
			autoUpdater.quitAndInstall();
		});
		ipcMain.on("printData", (e, arg) => {
			const data = JSON.parse(arg);
			PosPrinter.print(JSON.parse(arg.data), {
				copies: 1,
				timeOutPerLine: 400,
				silent: true,
				preview: true,
				printerName: data.printer,
			}).catch((err) => {
				console.log(err);
			});
		});
		ipcMain.on("getBaseUrl", (event, arg) => {
			fs.readFile(baseUrlFolder, { encoding: "utf-8" }, (err, result) => {
				if (err) {
					console.log(err);
				} else {
					event.returnValue = result;
				}
			});
		});
		ipcMain.on("upLoadSoft", (event, arg) => {
			upLoadSoft();
		});
		ipcMain.on("getLicense", (event, arg) => {
			getLicense();
		});
		ipcMain.on("isDev", (event, arg) => {
			sendUpdateMessage({
				cmd: "isDev",
				message: {
					isDev: isDev,
				},
			});
		});
	}
}

app.whenReady().then(() => {
	createWindow();
	readLicense();
});

function sendUpdateMessage(text) {
	mainWindow.webContents.send("message", text);
}

function BomiotUrl() {
	return "https://po.56yhz.com/";
}

function getLicense() {
	const request = net.request(BomiotUrl() + "license/");
	request.on("response", (response) => {
		response.on("data", (chunk) => {
			writeLicense(`${chunk}`);
		});
	});
	request.end();
}

function writeLicense(text) {
	fs.writeFile(
		path.resolve(
			__dirname,
			process.env.QUASAR_PUBLIC_FOLDER,
			"statics/license.txt"
		),
		JSON.parse(JSON.stringify(text)),
		{ encoding: "utf-8" },
		(err, result) => {
			if (err) {
				console.log(err);
			} else {
				return JSON.parse(text).license;
			}
		}
	);
}

function readLicense(text) {
	fs.readFile(
		path.resolve(
			__dirname,
			process.env.QUASAR_PUBLIC_FOLDER,
			"statics/license.txt"
		),
		{ encoding: "utf-8" },
		(err, result) => {
			if (err) {
				getLicense();
			} else {
				return JSON.parse(result);
			}
		}
	);
}

function upLoadSoft() {
	dialog
		.showOpenDialog({
			properties: ["openFile", "multiSelections"],
			filters: [{ name: "update", extensions: ["exe", "yml"] }],
		})
		.then((res) => {
			sendUpdateMessage({
				cmd: "upLoadSoft",
				message: {
					filePaths: res.filePaths,
				},
			});
		})
		.catch((err) => {
			console.log(err);
		});
}

app.on("window-all-closed", () => {
	if (process.platform !== "darwin") {
		app.quit();
	}
});

app.on("activate", () => {
	if (mainWindow === null) {
		createWindow();
	}
});
