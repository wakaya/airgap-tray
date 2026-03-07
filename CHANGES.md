# Changelog

All notable changes to this project will be documented in this file.

## [1.0.1] - 2026-03-07

### Fixed

- Fixed `.cmd` execution stability on Windows by removing fragile multi-line `^` continuations in PowerShell calls.
- Fixed quoting issues in `OutboundBlock.cmd` that could break execution on some systems.
- Improved startup behavior documentation around tray state detection and firewall initialization.

### Changed

- Updated release documentation for the 1.0.1 patch release.
- Clarified that mode switching may trigger a UAC prompt because firewall profile changes require administrator privileges.
- Clarified that this tool changes the Windows Firewall default outbound policy for the selected profiles.

## [1.0.0] - 2026-03-06

### Added

- Initial release
- Windows tray icon for firewall mode
- Double-click toggle
- Outbound firewall block / allow switch
- Local AI environment support
- Japanese / English localization
