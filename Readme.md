# PROTOCOL OSINT CTF: Operation Rogue Echo

Welcome to **Operation Rogue Echo**, a progressive 15-level OSINT and digital reconnaissance CTF workshop designed for beginners and intermediate investigators.

---

## 🎯 Campaign Overview

* **Scenario:** Rogue ex-employee Viktor Vance has exfiltrated sensitive assets from XYZ Ltd. and vanished. Trace his physical movements, burner identities, metadata trails, and digital breadcrumbs to apprehend him.
* **Format:** CTFd Standard Challenge Format (`ctfcli` compatible)
* **Total Levels:** 15 Challenges
* **Total Points:** 2,050 Points

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

## 🗺️ Campaign Matrix

| Phase | Level | Challenge Name | Category | Points | Core Tool | Flag |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| **Phase 1: The Breach** | **01** | Level 01: The Break-In | Metadata / EXIF | 50 | Jimpl / ExifTool | `FLAG{3x_3mpl0y33_l34v35_4_tr4c3}` |
| | **02** | Level 02: The Hidden Signature | Web Recon | 50 | View Page Source (`Ctrl+U`) | `FLAG{v13w_50urc3_15_f1r5t_5t3p}` |
| | **03** | Level 03: The Camera Fingerprint | Metadata / EXIF | 75 | Jimpl / ExifTool | `FLAG{c4m3r4_m4k3_m0d3l_3xp053d}` |
| **Phase 2: The Digital Footprint** | **04** | Level 04: The Scrambled Transmission | Decoding / CyberChef | 75 | CyberChef (From Base64) | `FLAG{b45364_unl0cks_th3_path}` |
| | **05** | Level 05: The Burner Alias | SOCMINT / Username Recon | 100 | WhatsMyName / Profile Search | `FLAG{un4m3_3num3r4t10n_succ355}` |
| | **06** | Level 06: Caesar's Escape | Decoding / CyberChef | 100 | CyberChef (ROT13) | `FLAG{rot13_decipher_success}` |
| **Phase 3: The Archive & The Web** | **07** | Level 07: Google Dorking 101 | Search Recon | 125 | Google Search Dorks | `FLAG{g00gl3_d0rk1ng_3xp053d}` |
| | **08** | Level 08: The Deleted Webpage | Web Archive | 125 | Wayback Machine | `FLAG{w4yb4ck_m4ch1n3_r3m3mb3r5}` |
| | **09** | Level 09: The Hidden Paste | Search Recon | 150 | Search Dorks / Paste Recon | `FLAG{p45t3_d0rk1ng_unc0v3r3d}` |
| **Phase 4: The Physical Trail** | **10** | Level 10: The Departure Landmark | GEOINT / Image Search | 150 | Google Lens / Reverse Search | `FLAG{gateway_of_india}` |
| | **11** | Level 11: The Train Station | GEOINT / Image Search | 175 | Google Lens / Platform Recon | `FLAG{pune_junction}` |
| | **12** | Level 12: The Airport Boarding Gate | GEOINT / Search | 175 | Flight Lookup (EK501 -> DXB) | `FLAG{d35t1n4t10n_dxb}` |
| **Phase 5: The Final Pursuit** | **13** | Level 13: The Street Corner Cafe | GEOINT / Google Maps | 200 | Google Maps / Street View | `FLAG{cafe_mondegar}` |
| | **14** | Level 14: The Safehouse Coordinates | GEOINT / Google Maps | 225 | Google Maps / Satellite View | `FLAG{t4j_m4h4l_p4l4c3}` |
| | **15** | Level 15: The Final Takedown | Master Challenge / Synthesis | 250 | Multi-source Synthesis | `FLAG{pune_ek501_taj_apprehended}` |

---

## 📁 Repository Structure

```
protocol-ctfd/
├── .ctf/
│   └── config                  # ctfcli configuration pointing to CTFd instance
├── challenges/
│   ├── level-01/
│   │   ├── challenge.yml       # CTFd challenge descriptor
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
├── Dockerfile                  # CTFd container deployment
├── setup_challenges.py         # Automation script to generate challenges & EXIF tags
└── verify_challenges.py        # Automated test verification suite
```

---

## 🚀 Managing Challenges with ctfcli

### 1. Validate All Challenges
```bash
python verify_challenges.py
```

### 2. Install / Sync Challenges to CTFd
```bash
# Sync all configured challenges
python -m ctfcli challenge sync

# Or install a specific level
python -m ctfcli challenge install challenges/level-01
```

---
*Created for PROTOCOL @ AISSMS COE OSINT Workshop*