@echo off
setlocal

set "MWB_EXE=C:\Program Files (x86)\Microsoft Garage\Mouse without Borders\MouseWithoutBorders.exe"
set "COMFY_RULE=ComfyUI_Block_Outgoing"

net session >nul 2>&1
if not "%errorlevel%"=="0" (
  powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
  exit /b
)

echo [INFO] Switching to GENERATE MODE (Private outbound = BLOCK) ...
echo [INFO] Allow MouseWithoutBorders: "%MWB_EXE%"

powershell -NoProfile -ExecutionPolicy Bypass -Command "$p='%MWB_EXE%'; if (Test-Path $p) { $name='ALLOW_MWB_OUT_PRIVATE'; if (-not (Get-NetFirewallRule -DisplayName $name -ErrorAction SilentlyContinue)) { New-NetFirewallRule -DisplayName $name -Direction Outbound -Action Allow -Program $p -Profile Private | Out-Null } else { Set-NetFirewallRule -DisplayName $name -Enabled True | Out-Null } } else { Write-Host '[WARN] MouseWithoutBorders.exe not found. Edit MWB_EXE in the cmd.' }"

powershell -NoProfile -ExecutionPolicy Bypass -Command "Set-NetFirewallProfile -Profile Domain,Private,Public -DefaultOutboundAction Block; Set-NetFirewallProfile -Profile Domain,Private,Public -AllowLocalFirewallRules False"

powershell -NoProfile -ExecutionPolicy Bypass -Command "$r='%COMFY_RULE%'; if (Get-NetFirewallRule -DisplayName $r -ErrorAction SilentlyContinue) { Set-NetFirewallRule -DisplayName $r -Enabled True | Out-Null }"

echo [OK] GENERATE MODE enabled.
pause
endlocal
