# 🚗 Dtire - Government Tire Purchase Automation System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange)
![Windows](https://img.shields.io/badge/Windows-CLI-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

**Advanced automated system for purchasing government-subsidized tires**  
*(Deprecated due to policy changes - Preserved as top project for technical excellence)*

## 🌟 Key Features
- **Dual Implementation**:
  - CLI Script version (Lightweight)
  - Windows Command-line Application (Enhanced)
- **Core Functionality**:
  - Real-time inventory monitoring
  - Multi-threaded operation
  - Proxy rotation system

```python
# Sample of Windows CLI implementation
class TirePurchaser:
    def __init__(self):
        self.mode = "windows_cli"  # or "script"
```
📦 Version Comparison
Feature	Script Version	Windows CLI App
Real-time Monitoring	✓	✓
GUI Interface	✗	✗
Proxy Support	Basic	Advanced
Installation	PIP	EXE Installer
⚙️ Technical Architecture

graph TD
    A[Input Parameters] --> B{Version}
    B -->|Script| C[Quick Execution]
    B -->|Windows CLI| D[Persistent Service]
    C & D --> E[Purchase Flow]
    
