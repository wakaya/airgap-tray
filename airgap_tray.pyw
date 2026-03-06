import locale
import json
from pathlib import Path
import subprocess
import threading
import time
import ctypes

from PIL import Image, ImageDraw
import pystray
import win32event
import win32api
import winerror

APP_NAME = "AirgapTray 1.0.0"
COPYRIGHT = "© 2026 Jun"

BASE_DIR = Path(__file__).resolve().parent
LOCALES_DIR = BASE_DIR / "locales"
CONFIG_FILE = BASE_DIR / "config.json"

ALLOW_CMD = BASE_DIR / "OutboundAllow.cmd"
BLOCK_CMD = BASE_DIR / "OutboundBlock.cmd"


def normalize_lang(lang):
    if not lang:
        return None
    return lang.split("_")[0].split("-")[0]


def run_hidden(command):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    return subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        startupinfo=startupinfo,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )

def load_messages():
    cfg_lang = None
    if CONFIG_FILE.exists():
        try:
            cfg = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
            cfg_lang = cfg.get("language")
        except Exception:
            pass

    sys_lang = None
    try:
        sys_lang = locale.getdefaultlocale()[0]
    except Exception:
        pass

    order = []
    for l in (cfg_lang, sys_lang, "ja", "en"):
        l = normalize_lang(l)
        if l and l not in order:
            order.append(l)

    for code in order:
        p = LOCALES_DIR / f"{code}.json"
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))

    return {}


MSG = load_messages()


def t(key, default=""):
    return MSG.get(key, default)


def get_private_outbound_action():
    try:
        result = run_hidden(
            [
                "powershell",
                "-NoProfile",
                "-WindowStyle", "Hidden",
                "-Command",
                "(Get-NetFirewallProfile -Name Private).DefaultOutboundAction",
            ]
        )
        return result.stdout.strip()
    except Exception:
        return "Unknown"

def make_icon(color):
    img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if color == "green":
        fill = (40, 180, 80, 255)
    elif color == "red":
        fill = (220, 60, 60, 255)
    else:
        fill = (150, 150, 150, 255)
    d.ellipse((8, 8, 56, 56), fill=fill)
    d.ellipse((16, 16, 48, 48), outline=(255, 255, 255, 220), width=3)
    return img


class AirgapTray:
    def __init__(self):
        self.icon = pystray.Icon(APP_NAME)
        self.current_mode = "Unknown"
        self.last_activate_time = 0.0
        self.double_click_threshold = 0.5  # seconds

        self.rebuild_menu()

    def rebuild_menu(self):
        self.icon.menu = pystray.Menu(
            pystray.MenuItem(
                lambda item: self.status_label(),
                lambda item: False,
                enabled=False,
            ),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(
                "toggle_hidden_default",
                self.on_activate,
                default=True,
                visible=False,
            ),
            pystray.MenuItem(t("menu_allow", "NORMAL MODE"), self.switch_allow),
            pystray.MenuItem(t("menu_block", "BLOCKING MODE"), self.switch_block),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(t("menu_refresh", "Refresh"), self.refresh),
            pystray.MenuItem("About", self.show_about),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(t("menu_exit", "Exit"), self.exit_app),
        )

    def status_label(self):
        if self.current_mode == "Allow":
            return t("status_label_normal", "現在: NORMAL MODE")
        if self.current_mode == "Block":
            return t("status_label_generate", "現在: BLOCKING MODE")
        return t("status_label_unknown", "現在: 状態不明")

    def update_status(self):
        mode = get_private_outbound_action()
        self.current_mode = mode
        if mode == "Allow":
            self.icon.icon = make_icon("green")
            self.icon.title = t("status_normal", "NORMAL MODE")
        elif mode == "Block":
            self.icon.icon = make_icon("red")
            self.icon.title = t("status_generate", "BLOCKING MODE")
        else:
            self.icon.icon = make_icon("gray")
            self.icon.title = t("status_unknown", "UNKNOWN MODE")
        self.icon.update_menu()

    def run_cmd(self, cmd):
        if not cmd.exists():
            return
        subprocess.Popen([str(cmd)], shell=True)

    def wait_and_refresh(self, expected):
        for _ in range(10):
            time.sleep(0.3)
            if get_private_outbound_action() == expected:
                break
        self.update_status()

    def run_cmd_and_follow(self, cmd, expected):
        self.run_cmd(cmd)
        threading.Thread(target=self.wait_and_refresh, args=(expected,), daemon=True).start()

    def switch_allow(self, icon=None, item=None):
        self.run_cmd_and_follow(ALLOW_CMD, "Allow")

    def switch_block(self, icon=None, item=None):
        self.run_cmd_and_follow(BLOCK_CMD, "Block")

    def toggle_mode(self):
        if self.current_mode == "Allow":
            self.switch_block()
        elif self.current_mode == "Block":
            self.switch_allow()
        else:
            self.refresh()

    def on_activate(self, icon=None, item=None):
        now = time.monotonic()
        if now - self.last_activate_time <= self.double_click_threshold:
            self.last_activate_time = 0.0
            self.toggle_mode()
        else:
            self.last_activate_time = now

    def refresh(self, icon=None, item=None):
        self.update_status()

    def _about_dialog(self):
        text = f"{APP_NAME}\n\n{t('about_text', 'Firewall mode toggle tray tool')}\n\n{COPYRIGHT}"
        ctypes.windll.user32.MessageBoxW(None, text, "About", 0x40)

    def show_about(self, icon=None, item=None):
        threading.Thread(target=self._about_dialog, daemon=True).start()

    def exit_app(self, icon=None, item=None):
        self.icon.stop()

    def run(self):
        self.update_status()
        self.icon.run()


if __name__ == "__main__":
    mutex = win32event.CreateMutex(None, False, "AirgapTraySingleton")
    if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
        raise SystemExit(0)
    AirgapTray().run()
