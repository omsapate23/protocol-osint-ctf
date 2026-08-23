import os
import yaml
import piexif
from PIL import Image
import ctfcli.cli.challenges

def test_challenges():
    print("=" * 60)
    print("OPERATION ROGUE ECHO - DYNAMIC CHALLENGE VERIFICATION")
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
        state = c.get("state")
        print(f"\n[Level {idx:02d}] {name}")
        print(f"  Category:     {cat}")
        print(f"  Type:         {ctype}")
        print(f"  Points:       {val}")
        print(f"  Extra Decay:  {extra}")
        print(f"  Requirements: {reqs}")
        print(f"  State:        {state}")
        print(f"  Flags:        {flags}")
        print(f"  Files:        {files}")

        assert ctype == "dynamic", f"Expected dynamic type for {name}, got {ctype}"
        assert extra is not None, f"Expected extra decay parameters for {name}"

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
    assert b"FLAG{3x_3mpl0y33_l34v35_4_tr4c3}" in user_comment or b"FLAG{3x_3mpl0y33_l34v35_4_tr4c3}" in img_desc

    # Test Level 02 HTML Comment
    l2_html = r"d:\protocol-ctfd\challenges\level-02\goodbye.html"
    with open(l2_html, "r", encoding="utf-8") as f:
        html_src = f.read()
    assert "<!-- FLAG{v13w_50urc3_15_f1r5t_5t3p} -->" in html_src
    print(f"[Level 02] Verified HTML comment flag in {l2_html}")

    # Test Level 03 EXIF
    l3_img = r"d:\protocol-ctfd\challenges\level-03\device_photo.jpg"
    exif_dict3 = piexif.load(l3_img)
    user_comment3 = exif_dict3["Exif"].get(piexif.ExifIFD.UserComment, b"")
    model3 = exif_dict3["0th"].get(piexif.ImageIFD.Model, b"")
    print(f"[Level 03] Model: {model3}")
    print(f"[Level 03] UserComment: {user_comment3}")
    assert b"FLAG{c4m3r4_m4k3_m0d3l_3xp053d}" in model3 or b"FLAG{c4m3r4_m4k3_m0d3l_3xp053d}" in user_comment3

    print("\n" + "=" * 60)
    print("ALL 15 CHALLENGES PASSED DYNAMIC CONFIGURATION VERIFICATION!")
    print("=" * 60)

if __name__ == "__main__":
    test_challenges()
