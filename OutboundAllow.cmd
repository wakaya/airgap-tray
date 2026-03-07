@echo off
setlocal

set "COMFY_RULE=ComfyUI_Block_Outgoing"

net session >nul 2>&1
if not "%errorlevel%"=="0" (
  powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
  exit /b
)

echo [INFO] Switching to NORMAL MODE (Private outbound = ALLOW) ...

powershell -NoProfile -ExecutionPolicy Bypass -Command "Set-NetFirewallProfile -Profile Domain,Private,Public -DefaultOutboundAction Allow; Set-NetFirewallProfile -Profile Domain,Private,Public -AllowLocalFirewallRules True"

powershell -NoProfile -ExecutionPolicy Bypass -Command "$name='ALLOW_MWB_OUT_PRIVATE'; if (Get-NetFirewallRule -DisplayName $name -ErrorAction SilentlyContinue) { Set-NetFirewallRule -DisplayName $name -Enabled False | Out-Null }"

powershell -NoProfile -ExecutionPolicy Bypass -Command "$r='%COMFY_RULE%'; if (Get-NetFirewallRule -DisplayName $r -ErrorAction SilentlyContinue) { Set-NetFirewallRule -DisplayName $r -Enabled False | Out-Null }"

echo [OK] NORMAL MODE enabled.
pause
endlocal
