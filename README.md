# Airgap Tray

![Version](https://img.shields.io/badge/version-1.0.1-blue)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![Python](https://img.shields.io/badge/python-3.9+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Offline](https://img.shields.io/badge/network-offline-important)

**Airgap Tray** は、ローカルAI生成環境のための  
**Windows用ファイアウォール切替トレイツール**です。

**Airgap Tray** is a  
**Windows tray tool for switching firewall outbound modes**  
for local AI generation environments.

---

生成AIを使用する際に

- 普段は **ネット接続OK**
- 生成時は **ネット遮断**

という切り替えを **ダブルクリック1回で行える**ようにします。

When using generative AI, this tool lets you switch between:

- **Internet allowed during normal use**
- **Internet blocked during generation**

with a **single double-click**.

---

# 日本語

## ✨ Features

- 🟢 トレイアイコンで現在のネットワーク状態を表示
- 🖱 **ダブルクリックでモード切替**
- 🔒 Windows Firewall の outbound 設定を切替
- ⚡ 非常に軽量（常駐CPUほぼ0%）
- 🌐 日本語 / English 対応
- 🧠 ローカルAI生成環境向け設計

---

## 🖥 動作環境

- Windows 10 / 11
- Python 3.9 以上

---

## 📦 インストール

インストーラは不要です。  
任意のフォルダに配置して使用できます。

例：

```text
D:\Tools\AirgapTray\
```

以下のファイルを配置してください。

```text
airgap_tray.pyw
OutboundAllow.cmd
OutboundBlock.cmd
locales/
```

必要なPythonパッケージをインストールします。

```bash
pip install -r requirements.txt
```

---

## 🚀 起動

```bash
python airgap_tray.pyw
```

起動するとタスクトレイにアイコンが表示されます。

---

## 🖱 操作方法

| 操作 | 内容 |
| ----- | ----- |
| ダブルクリック | ネットワークモード切替 |
| 右クリック | メニュー表示 |
| Refresh | 状態再取得 |
| About | バージョン表示 |

---

## 🔄 モード

### NORMAL MODE

🟢 ネット接続OK

```text
Firewall outbound: Allow
```

インターネット接続可能

---

### BLOCKING MODE

🔴 ネット接続NG

```text
Firewall outbound: Block
```

外部通信を遮断  
ローカルAI生成時に使用

---

## ⚠ 管理者権限

Windows Firewall を変更するため、  
モード切替時に **管理者権限の確認ダイアログ** が表示されます。

これは正常な動作です。

---

## 🔁 自動起動（おすすめ）

Windows起動時に自動起動する場合

1. `airgap_tray.pyw` を右クリック
2. **ショートカットを作成**
3. 以下を開く

```text
Win + R
shell:startup
```

4. 作成したショートカットを配置

これで Windows 起動時に自動起動します。

---

## 🌐 言語設定

通常は OS 言語を自動検出します。

固定したい場合は `config.json` を作成します。

例：

```json
{
  "language": "ja"
}
```

または

```json
{
  "language": "en"
}
```

---

## 🧩 フォルダ構成

```text
AirgapTray/
 ├ airgap_tray.pyw
 ├ OutboundAllow.cmd
 ├ OutboundBlock.cmd
 ├ requirements.txt
 ├ README.md
 ├ LICENSE
 └ locales/
      ├ ja.json
      └ en.json
```

---

## 💡 用途

このツールは主に以下の用途を想定しています。

ローカル画像生成AIを  
**完全にローカル環境で実行するための補助ツール**です。

生成時のみ外部通信を遮断することで

- モデルの外部通信防止
- 意図しないAPIアクセス防止
- セキュリティ確保

を簡単に実現できます。

---

## ⚠ 注意

このツールは Windows Firewall の既定の通信設定そのものを変更します。

**Blocking Mode** を有効にすると、以下を含むPCからの外向き通信が  
すべてブロックされます。

- Webブラウザ
- Windows Update
- クラウド同期
- メッセージアプリ

ですから、用が済んだら確実に **Normal Mode** に戻してください。

---

## 🛠 初回起動時の既知の挙動

一部のクリーンな Windows 環境では、初回起動時にトレイが  
**UNKNOWN MODE** で始まることがあります。

この場合は、以下の手順で初期化してください。

1. トレイアイコンを一度ダブルクリックする  
   → **OutboundBlock.cmd** が実行され、**BLOCKING MODE** に切り替わります
2. もう一度ダブルクリックする  
   → **OutboundAllow.cmd** が実行され、**NORMAL MODE** に戻ります

この初期化後は、通常どおり動作すると思います。

---

# English

## ✨ Features

- 🟢 Shows the current network state with a tray icon
- 🖱 **Switches modes with a double-click**
- 🔒 Toggles the Windows Firewall outbound policy
- ⚡ Very lightweight (almost no idle CPU usage)
- 🌐 Supports Japanese / English
- 🧠 Designed for local AI generation environments

---

## 🖥 Requirements

- Windows 10 / 11
- Python 3.9 or later

---

## 📦 Installation

No installer is required.  
You can place the files in any folder.

Example:

```text
D:\Tools\AirgapTray\
```

Place the following files there:

```text
airgap_tray.pyw
OutboundAllow.cmd
OutboundBlock.cmd
locales/
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## 🚀 Launch

```bash
python airgap_tray.pyw
```

After launch, an icon will appear in the task tray.

---

## 🖱 Controls

| Action | Description |
| ----- | ----- |
| Double-click | Switch network mode |
| Right-click | Open menu |
| Refresh | Reload current state |
| About | Show version information |

---

## 🔄 Modes

### NORMAL MODE

🟢 Internet access allowed

```text
Firewall outbound: Allow
```

Internet connection is available.

---

### BLOCKING MODE

🔴 Internet access blocked

```text
Firewall outbound: Block
```

Outbound communication is blocked.  
Use this mode during local AI generation.

---

## ⚠ Administrator Privileges

Because this tool changes Windows Firewall settings,  
Windows may display a **UAC / administrator confirmation dialog** when switching modes.

This is normal behavior.

---

## 🔁 Auto Start (Recommended)

To launch the tool automatically when Windows starts:

1. Right-click `airgap_tray.pyw`
2. Create a shortcut
3. Open the following:

```text
Win + R
shell:startup
```

4. Place the shortcut in that folder

The tool will then start automatically with Windows.

---

## 🌐 Language Settings

By default, the application automatically detects the OS language.

If you want to fix the language manually, create a `config.json` file.

Example:

```json
{
  "language": "ja"
}
```

or

```json
{
  "language": "en"
}
```

---

## 🧩 Folder Structure

```text
AirgapTray/
 ├ airgap_tray.pyw
 ├ OutboundAllow.cmd
 ├ OutboundBlock.cmd
 ├ requirements.txt
 ├ README.md
 ├ LICENSE
 └ locales/
      ├ ja.json
      └ en.json
```

---

## 💡 Intended Use

This tool is mainly intended for the following use case:

A helper utility for running local image-generation AI  
in a **fully local environment**.

By blocking outbound communication only during generation, it makes it easier to:

- prevent unwanted external communication by models or tools
- prevent unintended API access
- improve operational security

---

## ⚠ Important Notice

This tool modifies the default outbound communication policy of Windows Firewall itself.

When **Blocking Mode** is enabled, all outbound network connections from the PC  
may be blocked, including:

- Web browsers
- Windows Update
- Cloud synchronization
- Messaging applications

So after you are done, make sure to switch back to **Normal Mode**.

---

## 🛠 Known Behavior on First Launch

On some clean Windows environments, the tray may start in  
**UNKNOWN MODE** on the first launch.

If this happens, initialize it with the following steps:

1. Double-click the tray icon once  
   → `OutboundBlock.cmd` runs and the tray switches to **BLOCKING MODE**
2. Double-click the tray icon again  
   → `OutboundAllow.cmd` runs and the tray returns to **NORMAL MODE**

After this initialization sequence, the tray may behave normally.

---

# 📜 License

MIT License

```text
Copyright (c) 2026 Jun Wakaya
```
