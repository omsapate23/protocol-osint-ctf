import os
import shutil
import piexif
from PIL import Image

BASE_DIR = r"d:\protocol-ctfd"
BRAIN_DIR = r"C:\Users\Lenovo\.gemini\antigravity-ide\brain\f368b578-08b1-4743-a5bd-e8f7f6bcbc35"

CHALLENGES = [
    {
        "dir": "level-01",
        "name": "Level 01: The Break-In",
        "category": "Metadata / EXIF",
        "value": 50,
        "description": "At 02:40 AM, rogue ex-employee Viktor Vance accessed the server room of XYZ Ltd. and left a snapshot behind. \n\nInspect the image file metadata using Jimpl.com to uncover the initial recovery flag.\n\n**Flag Format:** `FLAG{...}`",
        "flags": ["FLAG{3x_3mpl0y33_l34v35_4_tr4c3}"],
        "files": ["datacenter_leak.jpg"],
        "state": "visible",
    },
    {
        "dir": "level-02",
        "name": "Level 02: The Hidden Signature",
        "category": "Web Recon",
        "value": 50,
        "description": "Viktor left a static page on XYZ Ltd.'s internal server. Inspect the page source to find his hidden signature.\n\n**Flag Format:** `FLAG{...}`",
        "flags": ["FLAG{v13w_50urc3_15_f1r5t_5t3p}"],
        "files": ["goodbye.html"],
        "state": "visible",
    },
    {
        "dir": "level-03",
        "name": "Level 03: The Camera Fingerprint",
        "category": "Metadata / EXIF",
        "value": 75,
        "description": "Forensics intercepted a second photo dropped by Viktor. Extract the device specifications and metadata tags to recover the flag.\n\n**Flag Format:** `FLAG{...}`",
        "flags": ["FLAG{c4m3r4_m4k3_m0d3l_3xp053d}"],
        "files": ["device_photo.jpg"],
        "state": "visible",
    },
    {
        "dir": "level-04",
        "name": "Level 04: The Scrambled Transmission",
        "category": "Decoding / CyberChef",
        "value": 75,
        "description": "We intercepted a scrambled string from Viktor's terminal buffer:\n`RkxBR3tiNDUzNjRfdW5sMGNrc190aDNfcGF0aH0=`\n\nUse CyberChef to decode the message.\n\n**Flag Format:** `FLAG{...}`",
        "flags": ["FLAG{b45364_unl0cks_th3_path}"],
        "files": [],
        "state": "visible",
    },
    {
        "dir": "level-05",
        "name": "Level 05: The Burner Alias",
        "category": "SOCMINT / Username Recon",
        "value": 100,
        "description": "Threat intelligence discovered Viktor goes by the handle `viktor_echo_99`. Find where this profile is registered to view his bio.\n\n**Flag Format:** `FLAG{...}`",
        "flags": ["FLAG{un4m3_3num3r4t10n_succ355}"],
        "files": [],
        "state": "visible",
    },
    {
        "dir": "level-06",
        "name": "Level 06: Caesar's Escape",
        "category": "Decoding / CyberChef",
        "value": 100,
        "description": "Viktor shifted his final note using a classic Caesar cipher (ROT13):\n`SYNT{ebg13_qrpvcure_fhpprff}`\n\nUse CyberChef to reveal the plaintext.\n\n**Flag Format:** `FLAG{...}`",
        "flags": ["FLAG{rot13_decipher_success}"],
        "files": [],
        "state": "visible",
    },
    {
        "dir": "level-07",
        "name": "Level 07: Google Dorking 101",
        "category": "Search Recon",
        "value": 125,
        "description": "Viktor leaked an unindexed PDF document containing company notes. Use Google search filters (dorks) to find the leaked file.\n\n**Flag Format:** `FLAG{...}`",
        "flags": ["FLAG{g00gl3_d0rk1ng_3xp053d}"],
        "files": [],
        "state": "visible",
    },
    {
        "dir": "level-08",
        "name": "Level 08: The Deleted Webpage",
        "category": "Web Archive",
        "value": 125,
        "description": "Viktor wiped his personal webpage (`http://vance-tech.xyz/note`) before fleeing. Use the Wayback Machine to view the archived snapshot.\n\n**Flag Format:** `FLAG{...}`",
        "flags": ["FLAG{w4yb4ck_m4ch1n3_r3m3mb3r5}"],
        "files": [],
        "state": "visible",
    },
    {
        "dir": "level-09",
        "name": "Level 09: The Hidden Paste",
        "category": "Search Recon",
        "value": 150,
        "description": "Viktor dropped a note on a paste hosting site referencing `Operation Rogue Echo`. Locate the paste to retrieve the flag.\n\n**Flag Format:** `FLAG{...}`",
        "flags": ["FLAG{p45t3_d0rk1ng_unc0v3r3d}"],
        "files": [],
        "state": "visible",
    },
    {
        "dir": "level-10",
        "name": "Level 10: The Departure Landmark",
        "category": "GEOINT / Image Search",
        "value": 150,
        "description": "Viktor shared a photo taken while fleeing. Identify the landmark in the photo.\n\n**Flag Format:** `FLAG{landmark_name}` (lowercase, words separated by underscores, e.g., `FLAG{eiffel_tower}`).",
        "flags": ["FLAG{gateway_of_india}"],
        "files": ["departure_view.jpg"],
        "state": "visible",
    },
    {
        "dir": "level-11",
        "name": "Level 11: The Train Station",
        "category": "GEOINT / Image Search",
        "value": 175,
        "description": "An image recovered from Viktor's social account shows an Indian Railways station platform with unique architectural details. Identify the station.\n\n**Flag Format:** `FLAG{station_name}` (lowercase, underscores, e.g., `FLAG{mumbai_central}`).",
        "flags": ["FLAG{pune_junction}"],
        "files": ["station_platform.jpg"],
        "state": "visible",
    },
    {
        "dir": "level-12",
        "name": "Level 12: The Airport Boarding Gate",
        "category": "GEOINT / Search",
        "value": 175,
        "description": "Viktor posted a photo showing flight `EK501`. Find the 3-letter destination airport IATA code.\n\n**Flag Format:** `FLAG{d35t1n4t10n_XXX}` (e.g., `FLAG{d35t1n4t10n_del}`).",
        "flags": ["FLAG{d35t1n4t10n_dxb}"],
        "files": ["flight_board.jpg"],
        "state": "visible",
    },
    {
        "dir": "level-13",
        "name": "Level 13: The Street Corner Cafe",
        "category": "GEOINT / Google Maps",
        "value": 200,
        "description": "Viktor checked into a vintage cafe near the harbor. Use the visual clues and Google Maps to identify the cafe's exact name.\n\n**Flag Format:** `FLAG{cafe_name}` (lowercase, underscores, e.g., `FLAG{blue_tokai}`).",
        "flags": ["FLAG{cafe_mondegar}"],
        "files": ["cafe_front.jpg"],
        "state": "visible",
    },
    {
        "dir": "level-14",
        "name": "Level 14: The Safehouse Coordinates",
        "category": "GEOINT / Google Maps",
        "value": 225,
        "description": "Viktor's final uploaded photo reveals a distinct hotel facade across the water. Identify the building name.\n\n**Flag Format:** `FLAG{building_name}` (lowercase, underscores, e.g., `FLAG{hotel_trident}`).",
        "flags": ["FLAG{t4j_m4h4l_p4l4c3}"],
        "files": ["balcony_view.jpg"],
        "state": "visible",
    },
    {
        "dir": "level-15",
        "name": "Level 15: The Final Takedown",
        "category": "Master Challenge / Synthesis",
        "value": 250,
        "description": "Assemble the master apprehension code using the clues collected from your investigation:\n`[Station Name from L11]_[Flight Code from L12]_[Safehouse Name Prefix from L14]_apprehended`\n\nExample format: `FLAG{mumbai_ai101_trident_apprehended}`",
        "flags": ["FLAG{pune_ek501_taj_apprehended}"],
        "files": [],
        "state": "visible",
    },
]

def make_challenge_yml(c):
    lines = []
    lines.append(f'name: "{c["name"]}"')
    lines.append('author: "PROTOCOL"')
    lines.append(f'category: "{c["category"]}"')
    lines.append(f'value: {c["value"]}')
    lines.append('description: |')
    for desc_line in c["description"].split("\n"):
        lines.append(f'  {desc_line}')
    lines.append('flags:')
    for flag in c["flags"]:
        lines.append(f'  - "{flag}"')
    if c["files"]:
        lines.append('files:')
        for f in c["files"]:
            lines.append(f'  - {f}')
    lines.append(f'state: {c["state"]}')
    return "\n".join(lines) + "\n"

def process_level_01_image(src, dst):
    im = Image.open(src)
    flag = "FLAG{3x_3mpl0y33_l34v35_4_tr4c3}"
    user_comment_bytes = b"ASCII\x00\x00\x00" + flag.encode("utf-8")
    
    zeroth_ifd = {
        piexif.ImageIFD.Make: b"XYZ Terminal Forensics",
        piexif.ImageIFD.Model: b"ServerRack-Cam v4",
        piexif.ImageIFD.ImageDescription: f"Workstation snapshot - {flag}".encode("utf-8"),
        piexif.ImageIFD.Software: b"VanceLeak v1.0",
        piexif.ImageIFD.Artist: b"Viktor Vance",
        piexif.ImageIFD.XPComment: flag.encode("utf-16le"),
    }
    exif_ifd = {
        piexif.ExifIFD.UserComment: user_comment_bytes,
        piexif.ExifIFD.DateTimeOriginal: b"2026:08:23 02:40:15",
    }
    exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd, "GPS": {}, "1st": {}, "interop": {}}
    exif_bytes = piexif.dump(exif_dict)
    im.save(dst, "jpeg", exif=exif_bytes, quality=95)
    print(f"[+] Created Level 01 EXIF image: {dst}")

def process_level_02_html(dst):
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XYZ Ltd. - 403 Access Terminated</title>
    <!-- Viktor was here. You will never catch me. -->
    <!-- FLAG{v13w_50urc3_15_f1r5t_5t3p} -->
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body {
            background-color: #0d1117;
            color: #58a6ff;
            font-family: 'Consolas', 'Courier New', monospace;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            padding: 20px;
        }
        .terminal-card {
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 8px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.6);
            width: 100%;
            max-width: 650px;
            overflow: hidden;
        }
        .terminal-header {
            background: #21262d;
            padding: 12px 16px;
            display: flex;
            align-items: center;
            gap: 8px;
            border-bottom: 1px solid #30363d;
        }
        .dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }
        .dot.red { background: #ff5f56; }
        .dot.yellow { background: #ffbd2e; }
        .dot.green { background: #27c93f; }
        .title {
            color: #8b949e;
            font-size: 0.85rem;
            margin-left: auto;
        }
        .terminal-body {
            padding: 24px;
            line-height: 1.6;
            color: #c9d1d9;
        }
        .error-code {
            color: #ff7b72;
            font-size: 1.4rem;
            font-weight: bold;
            margin-bottom: 12px;
        }
        .prompt {
            color: #79c0ff;
        }
        .warning-box {
            background: rgba(255, 123, 114, 0.1);
            border-left: 3px solid #ff7b72;
            padding: 12px;
            margin-top: 16px;
            font-size: 0.9rem;
            color: #ffa198;
        }
    </style>
</head>
<body>
    <div class="terminal-card">
        <div class="terminal-header">
            <div class="dot red"></div>
            <div class="dot yellow"></div>
            <div class="dot green"></div>
            <div class="title">XYZ-INTRANET-GATEWAY v3.12</div>
        </div>
        <div class="terminal-body">
            <div class="error-code">HTTP 403: ACCESS REVOKED</div>
            <p><span class="prompt">root@xyz-node01:~$</span> session_status --uid v.vance</p>
            <p style="color: #8b949e; margin-top: 8px;">[WARN] User credentials purged by system administrator.</p>
            <p style="color: #8b949e;">[INFO] Departure timestamp logged: 02:40:15 UTC.</p>
            <div class="warning-box">
                <strong>ALERT:</strong> Unauthorized terminal session detected. All keystrokes and inspection routines are monitored.
            </div>
            <p style="margin-top: 16px; font-size: 0.85rem; color: #8b949e;">XYZ Ltd. Cyber Defense System // Project Rogue Echo</p>
        </div>
    </div>
</body>
</html>
"""
    with open(dst, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[+] Created Level 02 HTML file: {dst}")

def process_level_03_image(src, dst):
    im = Image.open(src)
    flag = "FLAG{c4m3r4_m4k3_m0d3l_3xp053d}"
    user_comment_bytes = b"ASCII\x00\x00\x00" + flag.encode("utf-8")
    
    zeroth_ifd = {
        piexif.ImageIFD.Make: b"BurnerTech Mobile",
        piexif.ImageIFD.Model: f"EOS-Burner / {flag}".encode("utf-8"),
        piexif.ImageIFD.ImageDescription: flag.encode("utf-8"),
        piexif.ImageIFD.Software: b"VanceBurnerCam v2.1",
        piexif.ImageIFD.Artist: b"viktor_echo_99",
        piexif.ImageIFD.XPComment: flag.encode("utf-16le"),
    }
    exif_ifd = {
        piexif.ExifIFD.UserComment: user_comment_bytes,
        piexif.ExifIFD.LensModel: f"BurnerLens 24mm {flag}".encode("utf-8"),
        piexif.ExifIFD.DateTimeOriginal: b"2026:08:23 03:15:22",
    }
    gps_ifd = {
        piexif.GPSIFD.GPSLatitudeRef: "N",
        piexif.GPSIFD.GPSLatitude: ((18, 1), (55, 1), (12, 1)),
        piexif.GPSIFD.GPSLongitudeRef: "E",
        piexif.GPSIFD.GPSLongitude: ((72, 1), (50, 1), (30, 1)),
    }
    exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd, "GPS": gps_ifd, "1st": {}, "interop": {}}
    exif_bytes = piexif.dump(exif_dict)
    im.save(dst, "jpeg", exif=exif_bytes, quality=95)
    print(f"[+] Created Level 03 EXIF image: {dst}")

def main():
    challenges_root = os.path.join(BASE_DIR, "challenges")
    os.makedirs(challenges_root, exist_ok=True)

    # Generated image artifacts from brain directory
    img_map = {
        "level-01": os.path.join(BRAIN_DIR, "datacenter_leak_1787496049417.jpg"),
        "level-03": os.path.join(BRAIN_DIR, "device_photo_1787496066916.jpg"),
        "level-10": os.path.join(BRAIN_DIR, "departure_view_1787496085710.jpg"),
        "level-11": os.path.join(BRAIN_DIR, "station_platform_1787496108040.jpg"),
        "level-12": os.path.join(BRAIN_DIR, "flight_board_1787496129431.jpg"),
        "level-13": os.path.join(BRAIN_DIR, "cafe_front_1787496150301.jpg"),
        "level-14": os.path.join(BRAIN_DIR, "balcony_view_1787496173585.jpg"),
    }

    for c in CHALLENGES:
        lvl_dir = os.path.join(challenges_root, c["dir"])
        os.makedirs(lvl_dir, exist_ok=True)
        
        # Write challenge.yml
        yml_path = os.path.join(lvl_dir, "challenge.yml")
        with open(yml_path, "w", encoding="utf-8") as f:
            f.write(make_challenge_yml(c))
        print(f"[+] Wrote {yml_path}")

        # Handle specific assets
        if c["dir"] == "level-01":
            process_level_01_image(img_map["level-01"], os.path.join(lvl_dir, "datacenter_leak.jpg"))
        elif c["dir"] == "level-02":
            process_level_02_html(os.path.join(lvl_dir, "goodbye.html"))
        elif c["dir"] == "level-03":
            process_level_03_image(img_map["level-03"], os.path.join(lvl_dir, "device_photo.jpg"))
        elif c["dir"] == "level-10":
            shutil.copy2(img_map["level-10"], os.path.join(lvl_dir, "departure_view.jpg"))
        elif c["dir"] == "level-11":
            shutil.copy2(img_map["level-11"], os.path.join(lvl_dir, "station_platform.jpg"))
        elif c["dir"] == "level-12":
            shutil.copy2(img_map["level-12"], os.path.join(lvl_dir, "flight_board.jpg"))
        elif c["dir"] == "level-13":
            shutil.copy2(img_map["level-13"], os.path.join(lvl_dir, "cafe_front.jpg"))
        elif c["dir"] == "level-14":
            shutil.copy2(img_map["level-14"], os.path.join(lvl_dir, "balcony_view.jpg"))

    print("\n[SUCCESS] All 15 challenges created successfully.")

if __name__ == "__main__":
    main()
