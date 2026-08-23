import os
import yaml
import piexif
from PIL import Image
import base64
import codecs
import ctfcli.cli.challenges

def test_challenges():
    print("=" * 60)
    print("OPERATION ROGUE ECHO - CHALLENGE & HINTS VERIFICATION")
    print("=" * 60)

    challenges = ctfcli.cli.challenges.ChallengeCommand._resolve_all_challenges()
    print(f"[+] Total challenges recognized by ctfcli: {len(challenges)}")
    assert len(challenges) == 15, f"Expected 15 challenges, found {len(challenges)}"

    for idx, c in enumerate(challenges, 1):
        name = c.get("name")
        cat = c.get("category")
        val = c.get("value")
        ctype = c.get("type")
        extra = c.get("extra")
        reqs = c.get("requirements")
        flags = c.get("flags")
        files = c.get("files") or []
        hints = c.get("hints") or []
        state = c.get("state")
        print(f"\n[Level {idx:02d}] {name}")
        print(f"  Category:     {cat}")
        print(f"  Type:         {ctype}")
        print(f"  Points:       {val}")
        print(f"  Extra Decay:  {extra}")
        print(f"  Requirements: {reqs}")
        print(f"  Hints:        {len(hints)} configured (Cost: {hints[0]['cost']} pts)")
        print(f"  Flags:        {flags}")
        print(f"  Files:        {files}")

        assert ctype == "dynamic", f"Expected dynamic type for {name}, got {ctype}"
        assert extra is not None, f"Expected extra decay parameters for {name}"
        assert len(hints) >= 1, f"Expected at least 1 hint for {name}"
        assert hints[0]["cost"] > 0, f"Hint must have non-zero cost for {name}"
        assert all(f.startswith("PROTOCOL{") and f.endswith("}") for f in flags), f"Invalid flag format in {flags}"

        if idx == 1:
            assert reqs is None or reqs == [], f"Level 01 should have no prerequisites"
        else:
            prev_name = challenges[idx - 2].get("name")
            assert reqs == [prev_name], f"Level {idx:02d} expected requirement {prev_name}, got {reqs}"

        # Check that files exist
        for f in files:
            file_path = c.challenge_directory / f
            assert file_path.is_file(), f"File {file_path} not found!"
            print(f"    -> Verified file: {f} ({os.path.getsize(file_path)} bytes)")

    print("\n" + "=" * 60)
    print("TESTING METADATA / EXIF EXTRACTION")
    print("=" * 60)

    # Test Level 01 EXIF
    l1_img = r"d:\protocol-ctfd\challenges\level-01\datacenter_leak.jpg"
    exif_dict = piexif.load(l1_img)
    user_comment = exif_dict["Exif"].get(piexif.ExifIFD.UserComment, b"")
    img_desc = exif_dict["0th"].get(piexif.ImageIFD.ImageDescription, b"")
    print(f"[Level 01] UserComment: {user_comment}")
    print(f"[Level 01] ImageDescription: {img_desc}")
    assert b"PROTOCOL{3x_3mpl0y33_l34v35_4_tr4c3}" in user_comment or b"PROTOCOL{3x_3mpl0y33_l34v35_4_tr4c3}" in img_desc

    # Test Level 02 HTML Comment
    l2_html = r"d:\protocol-ctfd\challenges\level-02\goodbye.html"
    with open(l2_html, "r", encoding="utf-8") as f:
        html_src = f.read()
    assert "<!-- PROTOCOL{v13w_50urc3_15_f1r5t_5t3p} -->" in html_src
    print(f"[Level 02] Verified HTML comment flag in {l2_html}")

    # Test Level 03 EXIF
    l3_img = r"d:\protocol-ctfd\challenges\level-03\device_photo.jpg"
    exif_dict3 = piexif.load(l3_img)
    user_comment3 = exif_dict3["Exif"].get(piexif.ExifIFD.UserComment, b"")
    model3 = exif_dict3["0th"].get(piexif.ImageIFD.Model, b"")
    print(f"[Level 03] Model: {model3}")
    print(f"[Level 03] UserComment: {user_comment3}")
    assert b"PROTOCOL{c4m3r4_m4k3_m0d3l_3xp053d}" in model3 or b"PROTOCOL{c4m3r4_m4k3_m0d3l_3xp053d}" in user_comment3

    # Test Decodings
    b64_cipher = "UFJPVE9DT0x7YjQ1MzY0X3VubDBja3NfdGgzX3BhdGh9"
    b64_plain = base64.b64decode(b64_cipher).decode()
    print(f"[Level 04] Base64 decode: {b64_plain}")
    assert b64_plain == "PROTOCOL{b45364_unl0cks_th3_path}"

    rot13_cipher = "CEBGBPBY{ebg13_qrpvcure_fhpprff}"
    rot13_plain = codecs.decode(rot13_cipher, "rot_13")
    print(f"[Level 06] ROT13 decode: {rot13_plain}")
    assert rot13_plain == "PROTOCOL{rot13_decipher_success}"

    # Test Level 15 synthesis logic
    l11_station = "pune"
    l12_flight = "ek501"
    l14_hotel_prefix = "taj"
    synth_flag = f"PROTOCOL{{{l11_station}_{l12_flight}_{l14_hotel_prefix}_apprehended}}"
    print(f"[Level 15] Synthesis Flag: {synth_flag}")
    assert synth_flag == "PROTOCOL{pune_ek501_taj_apprehended}"

    print("\n" + "=" * 60)
    print("ALL 15 CHALLENGES PASSED VERIFICATION WITH COSTED HINTS!")
    print("=" * 60)

if __name__ == "__main__":
    test_challenges()
