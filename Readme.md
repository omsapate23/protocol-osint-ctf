# PROTOCOL OSINT CTF: Operation Rogue Echo

Welcome to **Operation Rogue Echo**, a progressive 15-level OSINT and digital reconnaissance CTF workshop designed for beginners and intermediate investigators.

---

## 🎯 Campaign Overview

* **Scenario:** Rogue ex-employee Viktor Vance has exfiltrated sensitive assets from XYZ Ltd. and vanished. Trace his physical movements, burner identities, metadata trails, and digital breadcrumbs to apprehend him.
* **Flag Format:** `PROTOCOL{...}`
* **Scoring Format:** Dynamic Scoring (`type: dynamic`) with First Blood decay and Sequential Prerequisite Progression.
* **Hints System:** Balanced contextual clues available for each level at a calibrated point penalty.
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

## 🗺️ Campaign Matrix (Dynamic Decay, Prerequisites & Hint Costs)

| Phase | Level | Challenge Name | Category | Initial | Decay | Min Floor | Hint Cost | Prerequisite | Flag |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Phase 1: The Breach** | **01** | Level 01: The Break-In | Metadata / EXIF | **150** | 15 | **50** | **15 pts** | 🔓 *Initially Unlocked* | `PROTOCOL{3x_3mpl0y33_l34v35_4_tr4c3}` |
| | **02** | Level 02: The Hidden Signature | Web Recon | **150** | 15 | **50** | **15 pts** | 🔒 Level 01 | `PROTOCOL{v13w_50urc3_15_f1r5t_5t3p}` |
| | **03** | Level 03: The Camera Fingerprint | Metadata / EXIF | **150** | 15 | **50** | **15 pts** | 🔒 Level 02 | `PROTOCOL{c4m3r4_m4k3_m0d3l_3xp053d}` |
| **Phase 2: The Digital Footprint** | **04** | Level 04: The Scrambled Transmission | Decoding / CyberChef | **250** | 20 | **100** | **25 pts** | 🔒 Level 03 | `PROTOCOL{b45364_unl0cks_th3_path}` |
| | **05** | Level 05: The Burner Alias | SOCMINT / Username Recon | **250** | 20 | **100** | **25 pts** | 🔒 Level 04 | `PROTOCOL{un4m3_3num3r4t10n_succ355}` |
| | **06** | Level 06: Caesar's Escape | Decoding / CyberChef | **250** | 20 | **100** | **25 pts** | 🔒 Level 05 | `PROTOCOL{rot13_decipher_success}` |
| **Phase 3: The Archive & The Web** | **07** | Level 07: Google Dorking 101 | Search Recon | **350** | 25 | **150** | **35 pts** | 🔒 Level 06 | `PROTOCOL{g00gl3_d0rk1ng_3xp053d}` |
| | **08** | Level 08: The Deleted Webpage | Web Archive | **350** | 25 | **150** | **35 pts** | 🔒 Level 07 | `PROTOCOL{w4yb4ck_m4ch1n3_r3m3mb3r5}` |
| | **09** | Level 09: The Hidden Paste | Search Recon | **350** | 25 | **150** | **35 pts** | 🔒 Level 08 | `PROTOCOL{p45t3_d0rk1ng_unc0v3r3d}` |
| **Phase 4: The Physical Trail** | **10** | Level 10: The Departure Landmark | GEOINT / Image Search | **450** | 30 | **200** | **45 pts** | 🔒 Level 09 | `PROTOCOL{gateway_of_india}` |
| | **11** | Level 11: The Train Station | GEOINT / Image Search | **450** | 30 | **200** | **45 pts** | 🔒 Level 10 | `PROTOCOL{pune_junction}` |
| | **12** | Level 12: The Airport Boarding Gate | GEOINT / Search | **450** | 30 | **200** | **45 pts** | 🔒 Level 11 | `PROTOCOL{d35t1n4t10n_dxb}` |
| **Phase 5: The Final Pursuit** | **13** | Level 13: The Street Corner Cafe | GEOINT / Google Maps | **600** | 35 | **300** | **60 pts** | 🔒 Level 12 | `PROTOCOL{cafe_mondegar}` |
| | **14** | Level 14: The Safehouse Coordinates | GEOINT / Google Maps | **600** | 35 | **300** | **60 pts** | 🔒 Level 13 | `PROTOCOL{t4j_m4h4l_p4l4c3}` |
| | **15** | Level 15: The Final Takedown | Master Challenge / Synthesis | **600** | 35 | **300** | **60 pts** | 🔒 Level 14 | `PROTOCOL{pune_ek501_taj_apprehended}` |

---

## 📁 Repository Structure

```
protocol-ctfd/
├── .ctf/
│   └── config                  # ctfcli configuration pointing to CTFd instance
├── challenges/
│   ├── level-01/               # Level 01: The Break-In (Dynamic: 150 -> 50, Hint: 15 pts)
│   ├── level-02/               # Level 02: The Hidden Signature (Dynamic: 150 -> 50, Hint: 15 pts)
│   ├── level-03/               # Level 03: The Camera Fingerprint (Dynamic: 150 -> 50, Hint: 15 pts)
│   ├── level-04/               # Level 04: The Scrambled Transmission (Dynamic: 250 -> 100, Hint: 25 pts)
│   ├── level-05/               # Level 05: The Burner Alias (Dynamic: 250 -> 100, Hint: 25 pts)
│   ├── level-06/               # Level 06: Caesar's Escape (Dynamic: 250 -> 100, Hint: 25 pts)
│   ├── level-07/               # Level 07: Google Dorking 101 (Dynamic: 350 -> 150, Hint: 35 pts)
│   ├── level-08/               # Level 08: The Deleted Webpage (Dynamic: 350 -> 150, Hint: 35 pts)
│   ├── level-09/               # Level 09: The Hidden Paste (Dynamic: 350 -> 150, Hint: 35 pts)
│   ├── level-10/               # Level 10: The Departure Landmark (Dynamic: 450 -> 200, Hint: 45 pts)
│   ├── level-11/               # Level 11: The Train Station (Dynamic: 450 -> 200, Hint: 45 pts)
│   ├── level-12/               # Level 12: The Airport Boarding Gate (Dynamic: 450 -> 200, Hint: 45 pts)
│   ├── level-13/               # Level 13: The Street Corner Cafe (Dynamic: 600 -> 300, Hint: 60 pts)
│   ├── level-14/               # Level 14: The Safehouse Coordinates (Dynamic: 600 -> 300, Hint: 60 pts)
│   └── level-15/               # Level 15: The Final Takedown (Dynamic: 600 -> 300, Hint: 60 pts)
├── pages/
│   └── index.html              # Custom CTFd homepage theme
├── Dockerfile                  # CTFd container deployment with PostgreSQL support
├── Readme.md                   # Updated documentation with dynamic matrix & rules
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