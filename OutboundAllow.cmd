@echo off
setlocal

set "COMFY_RULE=ComfyUI_Block_Outgoing"

REM --- self-elevate ---
net session >nul 2>&1
if not "%errorlevel%"=="0" (
  powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
  exit /b
)

echo [INFO] Switching to NORMAL MODE (Private outbound = ALLOW) ...

REM 1) Private の既定 Outbound を Allow
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "Set-NetFirewallProfile -Profile Domain,Private,Public -DefaultOutboundAction Allow;Set-NetFirewallProfile -Profile Domain,Private,Public -AllowLocalFirewallRules True"

REM 2) （任意）MouseWithoutBorders 許可ルールを無効化（残してもOK）
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$name='ALLOW_MWB_OUT_PRIVATE'; if (Get-NetFirewallRule -DisplayName $name -ErrorAction SilentlyContinue) { Set-NetFirewallRule -DisplayName $name -Enabled False | Out-Null }"

REM 3) （任意）ComfyUIの個別ブロック規則を無効化
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$r='%COMFY_RULE%'; if (Get-NetFirewallRule -DisplayName $r -ErrorAction SilentlyContinue) { Set-NetFirewallRule -DisplayName $r -Enabled False | Out-Null }"

echo [OK] NORMAL MODE enabled.
pause
endlocal
