# Airgap Tray

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![Python](https://img.shields.io/badge/python-3.9+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Offline](https://img.shields.io/badge/network-offline-important)

**Airgap Tray** は、ローカルAI生成環境のための  
**Windows用ファイアウォール切替トレイツール**です。

A Windows tray tool that toggles firewall outbound mode
for local AI generation environments.

---

生成AIを使用する際に

- 普段は **ネット接続OK**
- 生成時は **ネット遮断**

という切り替えを **ダブルクリック1回で行える**ようにします。

---

# ✨ Features

- 🟢 トレイアイコンで現在のネットワーク状態を表示
- 🖱 **ダブルクリックでモード切替**
- 🔒 Windows Firewall の outbound 設定を切替
- ⚡ 非常に軽量（常駐CPUほぼ0%）
- 🌐 日本語 / English 対応
- 🧠 ローカルAI生成環境向け設計

---

# 🖥 動作環境

- Windows 10 / 11
- Python 3.9 以上

---

# 📦 インストール

インストーラは不要です。  
任意のフォルダに配置して使用できます。

例：

```
D:\Tools\NetModeTray\
```

以下のファイルを配置してください。

```
airgap_tray.pyw
OutboundAllow.cmd
OutboundBlock.cmd
locales/
```

必要なPythonパッケージをインストールします。

```
pip install -r requirements.txt
```

---

# 🚀 起動

```
python airgap_tray.pyw
```

起動するとタスクトレイにアイコンが表示されます。

---

# 🖱 操作方法

| 操作           |         内容           |
|      -----     |        -----           |
| ダブルクリック | ネットワークモード切替 |
| 右クリック     |     メニュー表示       |
| Refresh        |      状態再取得        |
| About          |    バージョン表示      |

---

# 🔄 モード

## NORMAL MODE
🟢 ネット接続OK

```
Firewall outbound: Allow
```

インターネット接続可能

---

## BLOCKING MODE
🔴 ネット接続NG

```
Firewall outbound: Block
```

外部通信を遮断  
ローカルAI生成時に使用

---

# ⚠ 管理者権限

Windows Firewall を変更するため  
モード切替時に **管理者権限の確認ダイアログ** が表示されます。

これは正常な動作です。

---

# 🔁 自動起動（おすすめ）

Windows起動時に自動起動する場合

1. `net_mode_tray.pyw` を右クリック
2. **ショートカットを作成**
3. 以下を開く

```
Win + R
shell:startup
```

4. 作成したショートカットを配置

これで Windows 起動時に自動起動します。

---

# 🌐 言語設定

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

# 🧩 フォルダ構成

```
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

# 💡 用途

このツールは主に以下の用途を想定しています。

ローカル画像生成AIを  
**完全にローカル環境で実行するための補助ツール**です。

生成時のみ外部通信を遮断することで

- モデルの外部通信防止
- 意図しないAPIアクセス防止
- セキュリティ確保

を簡単に実現できます。

---

## 注意

このツールは Windows Firewall の既定の通信設定そのものを変更します。

**Blocking Mode** を有効にすると、以下を含むPCからの外向き通信が
すべてブロックされます。

- Webブラウザ
- Windows Update
- クラウド同期
- メッセージアプリ

ですから、用が済んだら確実に**Normal Mode** に戻してください。

---

# 🌍 English

Airgap Tray is a lightweight Windows tray tool  
that toggles Windows Firewall outbound rules.

It allows you to quickly switch between:

- **Normal Mode (Internet allowed)**
- **Blocking Mode (Internet blocked)**

This is particularly useful for **local AI generation environments**  
such as ComfyUI or Stable Diffusion where external network access  
should be disabled during generation.

---

## Important Notice

This tool modifies the Windows Firewall default outbound policy.

When **Blocking Mode** is enabled, all outbound network connections
from the PC may be blocked.

This includes:

- Web browsers
- Windows Update
- Cloud synchronization
- Messaging applications

If your internet connection appears to stop working,
switch back to **Normal Mode**.

---

# 📜 License

MIT License

```
Copyright (c) 2026 Jun Wakaya
```

---

# 👤 Author

Jun Wakaya

---

# ⭐ If this tool helps you

Feel free to ⭐ the repository!
