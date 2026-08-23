# PROTOCOL OSINT CTF: Operation Rogue Echo

Welcome to **Operation Rogue Echo**, a progressive 15-level OSINT and digital reconnaissance CTF workshop designed for beginners and intermediate investigators.

---

## 🎯 Campaign Overview

* **Scenario:** Rogue ex-employee Viktor Vance has exfiltrated sensitive assets from XYZ Ltd. and vanished. Trace his physical movements, burner identities, metadata trails, and digital breadcrumbs to apprehend him.
* **Format:** CTFd Dynamic Scoring Format (`ctfcli` compatible) with Sequential Prerequisite Progression.
* **Total Levels:** 15 Challenges
* **Progression:** Linear sequential unlocking (Level $N$ unlocks upon solving Level $N-1$).

---

## 🛠️ Core Toolset

This campaign relies exclusively on core beginner-friendly tools:
1. **Metadata & EXIF:** [Jimpl.com](https://jimpl.com) / ExifTool / Jeffrey's Image Metadata Viewer
2. **Web Recon & Source Code:** Browser "View Page Source" (`Ctrl + U`) & DevTools
3. **Encoding & Deciphering:** [CyberChef](https://gchq.github.io/CyberChef/) (Base64, ROT13)
4. **Username Recon (SOCMINT):** [WhatsMyName.app](https://whatsmyname.app/) / Profile Search
5. **Search Operators & Dorking:** Google Dorks (`filetype:`, `site:`, intext search)
6. **Web Archiving:** [Wayback Machine](https://web.archive.org/)
7. **Visual GEOINT:** Google Lens / Google Maps / Google Street View

---

## 🗺️ Campaign Matrix (Dynamic Decay & Prerequisites)

| Phase | Level | Challenge Name | Category | Initial | Decay | Min Floor | Prerequisite (Unlocked by) |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **Phase 1: The Breach** | **01** | Level 01: The Break-In | Metadata / EXIF | **150** | 15 | **50** | 🔓 *Initially Unlocked* |
| | **02** | Level 02: The Hidden Signature | Web Recon | **150** | 15 | **50** | 🔒 Level 01: The Break-In |
| | **03** | Level 03: The Camera Fingerprint | Metadata / EXIF | **150** | 15 | **50** | 🔒 Level 02: The Hidden Signature |
| **Phase 2: The Digital Footprint** | **04** | Level 04: The Scrambled Transmission | Decoding / CyberChef | **250** | 20 | **100** | 🔒 Level 03: The Camera Fingerprint |
| | **05** | Level 05: The Burner Alias | SOCMINT / Username Recon | **250** | 20 | **100** | 🔒 Level 04: The Scrambled Transmission |
| | **06** | Level 06: Caesar's Escape | Decoding / CyberChef | **250** | 20 | **100** | 🔒 Level 05: The Burner Alias |
| **Phase 3: The Archive & The Web** | **07** | Level 07: Google Dorking 101 | Search Recon | **350** | 25 | **150** | 🔒 Level 06: Caesar's Escape |
| | **08** | Level 08: The Deleted Webpage | Web Archive | **350** | 25 | **150** | 🔒 Level 07: Google Dorking 101 |
| | **09** | Level 09: The Hidden Paste | Search Recon | **350** | 25 | **150** | 🔒 Level 08: The Deleted Webpage |
| **Phase 4: The Physical Trail** | **10** | Level 10: The Departure Landmark | GEOINT / Image Search | **450** | 30 | **200** | 🔒 Level 09: The Hidden Paste |
| | **11** | Level 11: The Train Station | GEOINT / Image Search | **450** | 30 | **200** | 🔒 Level 10: The Departure Landmark |
| | **12** | Level 12: The Airport Boarding Gate | GEOINT / Search | **450** | 30 | **200** | 🔒 Level 11: The Train Station |
| **Phase 5: The Final Pursuit** | **13** | Level 13: The Street Corner Cafe | GEOINT / Google Maps | **600** | 35 | **300** | 🔒 Level 12: The Airport Boarding Gate |
| | **14** | Level 14: The Safehouse Coordinates | GEOINT / Google Maps | **600** | 35 | **300** | 🔒 Level 13: The Street Corner Cafe |
| | **15** | Level 15: The Final Takedown | Master Challenge / Synthesis | **600** | 35 | **300** | 🔒 Level 14: The Safehouse Coordinates |

---

## 📁 Repository Structure

```
protocol-ctfd/
├── .ctf/
│   └── config                  # ctfcli configuration pointing to CTFd instance
├── challenges/
│   ├── level-01/
│   │   ├── challenge.yml       # Dynamic challenge descriptor
│   │   └── datacenter_leak.jpg # Image with EXIF UserComment & Description
│   ├── level-02/
│   │   ├── challenge.yml
│   │   └── goodbye.html        # HTML error page with commented flag signature
│   ├── level-03/
│   │   ├── challenge.yml
│   │   └── device_photo.jpg    # Image with EXIF Model & UserComment
│   ├── level-04/
│   │   └── challenge.yml       # Base64 encoded buffer challenge
│   ├── level-05/
│   │   └── challenge.yml       # Handle viktor_echo_99 recon challenge
│   ├── level-06/
│   │   └── challenge.yml       # ROT13 encoded note challenge
│   ├── level-07/
│   │   └── challenge.yml       # Leaked PDF Google Dork challenge
│   ├── level-08/
│   │   └── challenge.yml       # Wayback Machine note snapshot challenge
│   ├── level-09/
│   │   └── challenge.yml       # Operation Rogue Echo paste challenge
│   ├── level-10/
│   │   ├── challenge.yml
│   │   └── departure_view.jpg  # Gateway of India photo asset
│   ├── level-11/
│   │   ├── challenge.yml
│   │   └── station_platform.jpg# Pune Junction railway station platform asset
│   ├── level-12/
│   │   ├── challenge.yml
│   │   └── flight_board.jpg    # Airport flight departures display asset
│   ├── level-13/
│   │   ├── challenge.yml
│   │   └── cafe_front.jpg      # Cafe Mondegar Colaba street view asset
│   ├── level-14/
│   │   ├── challenge.yml
│   │   └── balcony_view.jpg    # Taj Mahal Palace hotel harbor view asset
│   └── level-15/
│       └── challenge.yml       # Master synthesis challenge descriptor
├── pages/
│   └── index.html              # Custom CTFd homepage theme
├── Dockerfile                  # CTFd container deployment with PostgreSQL support
└── verify_challenges.py        # Automated test verification suite
```

---

## 🚀 Managing Challenges with ctfcli

### 1. Validate All Challenges
```bash
python verify_challenges.py
```

### 2. Synchronize Challenges to CTFd
```bash
ctf challenge sync
```

---
*Created for PROTOCOL @ AISSMS COE OSINT Workshop*