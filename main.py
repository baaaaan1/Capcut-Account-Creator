import os
import random
import time
import json
import string
import datetime
import argparse
import sys
from playwright.sync_api import sync_playwright

LINKWEB = "https://www.capcut.com/signup"

# --- HELPER FUNCTIONS (Sama seperti sebelumnya) ---
def get_first_and_remove(filename):
    if not os.path.exists(filename):
        print(f"❌ ERROR: File {filename} tidak ditemukan!")
        return None
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines:
        print(f"⚠️  INFO: File {filename} sudah kosong!")
        return None
    target_data = lines[0]
    remaining_data = lines[1:]
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(remaining_data))
        if remaining_data:
            f.write('\n')
    return target_data

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#"
    return ''.join(random.choice(chars) for _ in range(length))

def birthDay_generator():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(1980, 2004)
    return f"{day:02d}/{month:02d}/{year}"

def get_month_name(month_num):
    months = {
        "01": "Januari", "02": "Februari", "03": "Maret", "04": "April",
        "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus",
        "09": "September", "10": "Oktober", "11": "November", "12": "Desember"
    }
    return months.get(month_num, month_num)

def save_to_json(data, filename="proof.json"):
    existing_data = []
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        except json.JSONDecodeError:
            existing_data = []
    existing_data.append(data)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, indent=4, ensure_ascii=False)
    print(f"💾 Data disimpan ke {filename}")

# --- CORE LOGIC ---
def create_single_account(headless_mode=False):
    """Fungsi inti untuk membuat 1 akun."""

    # Ambil email dulu, kalau habis langsung return False biar loop berhenti
    gmail = get_first_and_remove("gmail-list.txt")
    if not gmail:
        print("❌ Stok email habis.")
        return False 

    password = generate_password()
    birthday = birthDay_generator()
    day, month, year = birthday.split('/')
    day = str(int(day))
    month_name = get_month_name(month)

    print(f"\n🔹 Memproses: {gmail}")

    with sync_playwright() as p:
        args = [
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-infobars",
            "--start-maximized",
        ]

        # Gunakan parameter headless dari CLI
        browser = p.chromium.launch(headless=headless_mode, args=args, channel="chrome")

        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            locale="id-ID",
            timezone_id="Asia/Jakarta",
        )
        context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
        page = context.new_page()

        try:
            page.goto(LINKWEB)

            # --- LOGIKA FILL FORM ---
            # [Versi Singkat dari kode Anda sebelumnya]
            page.get_by_placeholder("Masukkan alamat email").fill(gmail)
            page.click('button[type="button"]:has-text("Lanjutkan")')
            page.wait_for_timeout(1500)

            page.fill('input[type="password"]', password)
            page.click('button[type="button"]:has-text("Daftar")')
            page.wait_for_timeout(1500)

            page.get_by_placeholder("Tahun").fill(year)
            page.wait_for_timeout(500)
            page.get_by_role("combobox").filter(has_text="Bulan").click()
            page.get_by_role("option", name=month_name).click()
            page.wait_for_timeout(500)

            page.get_by_role("combobox").filter(has_text="Hari").click()
            page.get_by_role("option", name=day, exact=True).click()

            page.click('button:has-text("Berikutnya")')

            # --- OTP SECTION ---
            print(f"\n📬 OTP dikirim ke {gmail}")
            print("👉 Masukkan OTP di bawah ini:")

            # Input OTP via CLI
            kode_otp = input("🔑 OTP > ") 

            otp_input = page.locator("input[maxlength='6']")
            otp_input.press_sequentially(kode_otp, delay=100)

            # Tunggu redirect atau sukses
            page.wait_for_timeout(5000)

            # Save Data
            account_data = {
                "email": gmail,
                "password": password,
                "birthday": birthday,
                "created_at": datetime.datetime.now().isoformat()
            }
            save_to_json(account_data)
            print(f"✅ SUKSES: {gmail}\n")
            return True

        except Exception as e:
            print(f"❌ GAGAL {gmail}: {e}")
            return False # Tetap lanjut ke email berikutnya (return True) atau stop (return False) tergantung selera

        finally:
            context.close()
            browser.close()

# --- ENTRY POINT UTAMA (CLI HANDLER) ---
def main():
    # 1. Definisi Argumen CLI
    parser = argparse.ArgumentParser(description="CapCut Auto Register CLI Tool")

    # Argumen Jumlah Akun (-n atau --number)
    parser.add_argument(
        '-n', '--number',
        type=int,
        default=1,
        help='Jumlah akun yang ingin dibuat (Default: 1)'
    )

    # Argumen Headless (--headless)
    parser.add_argument(
        '--headless',
        action='store_true',
        help='Jalankan browser di background (tidak terlihat)'
    )

    # Parsing argumen
    args = parser.parse_args()

    print("="*50)
    print(f"🤖 CAPCUT BOT STARTED")
    print(f"🎯 Target: {args.number} Akun")
    print(f"👻 Mode Headless: {'ON' if args.headless else 'OFF'}")
    print("="*50)

    # 2. Loop sesuai jumlah permintaan
    sukses = 0
    for i in range(args.number):
        print(f"\n🔄 Proses Akun ke-{i+1} dari {args.number}")

        try:
            result = create_single_account(headless_mode=args.headless)
            if result:
                sukses += 1
            else:
                # Jika return False (misal email habis), break loop
                print("⚠️ Proses dihentikan.")
                break
        except KeyboardInterrupt:
            print("\n\n🛑 Script dihentikan oleh User (Ctrl+C)")
            sys.exit(0)

    print("\n" + "="*50)
    print(f"🏁 SELESAI. Total Berhasil: {sukses}/{args.number}")
    print("="*50)

if __name__ == "__main__":
    main()