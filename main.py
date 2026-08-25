import os
import random
import time
import json
import string
import datetime
import argparse
import sys
from playwright.sync_api import sync_playwright
from i18n import t, set_language, LANGUAGE

LINKWEB = "https://www.capcut.com/signup"

def clear_screen():
    """Bersihkan layar console biar output ga numpuk."""
    os.system('cls' if os.name == 'nt' else 'clear')

def log_step(msg):
    """Log detail tiap langkah (click/wait) biar progress keliatan jelas."""
    print(f"   ➜ {msg}")
    return msg

# --- HELPER FUNCTIONS (Sama seperti sebelumnya) ---
def get_first_and_remove(filename):
    if not os.path.exists(filename):
        print(t("file_not_found", filename=filename))
        return None
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines:
        print(t("file_empty", filename=filename))
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
    print(t("data_saved", filename=filename))

# --- CORE LOGIC ---
def create_single_account(headless_mode=False):
    """Fungsi inti untuk membuat 1 akun."""

    # Ambil email dari gmail-list.txt, kalau habis langsung return False biar loop berhenti
    gmail = get_first_and_remove("gmail-list.txt")
    if not gmail:
        print(t("emails_exhausted"))
        return False

    password = generate_password()
    birthday = birthDay_generator()
    day, month, year = birthday.split('/')
    day = str(int(day))
    month_name = get_month_name(month)

    print(t("processing", email=gmail))

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
            log_step(t("step_goto"))
            page.goto(LINKWEB)
            page.wait_for_load_state("domcontentloaded")
            page.wait_for_timeout(2000)
            log_step(t("step_goto_done"))

            # --- LOGIKA FILL FORM (flow UI terbaru) ---
            # 1. Pilih daftar dengan alamat email
            log_step(t("step_click_email_btn"))
            page.get_by_text("Lanjutkan dengan alamat email").click()
            page.wait_for_timeout(1000)

            # 2. Input email, lalu klik Lanjutkan
            log_step(t("step_fill_email"))
            page.get_by_role("textbox", name="Masukkan alamat email").fill(gmail)
            log_step(t("step_click_continue"))
            page.get_by_role("button", name="Lanjutkan", exact=True).click()
            page.wait_for_timeout(1500)

            # 3. Input password, lalu klik Daftar
            log_step(t("step_fill_password"))
            page.get_by_role("textbox", name="Masukkan kata sandi").fill(password)
            log_step(t("step_click_daftar"))
            page.locator("div.lv_sign_in_panel_wide-form").get_by_text("Daftar", exact=True).click()
            page.wait_for_timeout(1500)

            # 4. Input tanggal lahir
            log_step(t("step_fill_birthday"))
            page.get_by_role("textbox", name="Tahun").fill(year)
            page.wait_for_timeout(500)
            page.get_by_text("Bulan", exact=True).click()
            page.get_by_role("option", name=month_name).click()
            page.wait_for_timeout(500)
            page.get_by_text("Hari", exact=True).click()
            page.get_by_role("option", name=day, exact=True).click()

            # 5. Lanjut ke halaman verifikasi kode (OTP)
            # Klik button "Lanjutkan" DI DALAM wrapper, bukan wrapper-nya
            log_step(t("step_next_otp"))
            page.locator("div.lv_sign_in_panel_wide-enter-code-wrapper").get_by_text("Lanjutkan", exact=True).click()

            # --- OTP SECTION ---
            print(t("otp_sent", email=gmail))

            # Input OTP via CLI (mode manual)
            kode_otp = input(t("otp_prompt"))

            # 6. Input kode OTP (klik box kode lalu ketik)
            log_step(t("step_input_otp"))
            page.locator("div.verification_code_input-number").first.click()
            page.keyboard.type(kode_otp, delay=100)

            # Setelah OTP benar, otomatis lanjut ke page berikutnya
            log_step(t("step_wait_buka"))
            page.get_by_text("Buka CapCut").wait_for(state="visible", timeout=30000)

            # --- VERIFIKASI AKUN via API user_info ---
            user_info = {"data": None}

            def _on_response(response):
                if "commerce/v1/subscription/user_info" in response.url and response.request.method == "POST":
                    try:
                        user_info["data"] = response.json()
                    except Exception:
                        pass

            context.on("response", _on_response)

            # 7. Klik "Buka CapCut"
            log_step(t("step_click_buka"))
            page.get_by_text("Buka CapCut").click()

            # Tunggu response user_info (maks 30 detik)
            log_step(t("step_wait_verify"))
            deadline = time.time() + 30
            while time.time() < deadline and user_info["data"] is None:
                page.wait_for_timeout(500)

            data = user_info["data"]
            if not data:
                raise Exception(t("verif_no_response"))
            if str(data.get("ret")) != "0" or data.get("errmsg") != "success":
                raise Exception(t("verif_failed", ret=data.get("ret"), errmsg=data.get("errmsg")))

            uid = (data.get("data") or {}).get("uid")
            print(t("verify_success", uid=uid))

            # Save Data
            account_data = {
                "email": gmail,
                "password": password,
                "birthday": birthday,
                "uid": uid,
                "verified": True,
                "status": "success",
                "created_at": datetime.datetime.now().isoformat()
            }
            save_to_json(account_data)
            print(t("account_success", email=gmail))
            return True

        except Exception as e:
            print(t("account_failed", email=gmail, err=e))
            # Simpan juga sebagai proof gagal/invalid
            failed_data = {
                "email": gmail,
                "password": password,
                "birthday": birthday,
                "uid": None,
                "verified": False,
                "status": "error",
                "error": str(e),
                "created_at": datetime.datetime.now().isoformat()
            }
            save_to_json(failed_data)
            return None  # Akun ini gagal -> lanjut ke akun berikutnya

        finally:
            context.close()
            browser.close()

# --- BOT EXECUTION ---
def run_bot(number, headless):
    """Run the account-creation loop with the given settings."""
    clear_screen()
    print("="*50)
    print(t("banner_started"))
    print(t("banner_target", n=number))
    print(t("banner_headless", state="ON" if headless else "OFF"))
    print("="*50)

    sukses = 0
    for i in range(number):
        clear_screen()
        print(t("processing_i_of_n", i=i + 1, n=number))

        try:
            result = create_single_account(headless_mode=headless)
            if result is None:
                # Akun ini gagal, lanjut ke akun berikutnya
                continue
            if result:
                sukses += 1
            else:
                # Fatal: stok email habis
                print(t("process_stopped"))
                break
        except KeyboardInterrupt:
            print(t("interrupted"))
            sys.exit(0)

    print("\n" + "="*50)
    print(t("finished", ok=sukses, total=number))
    print("="*50)


# --- INTERACTIVE CONFIG MENU ---
def _prompt_number():
    """Prompt for the number of accounts; validate a positive integer."""
    while True:
        try:
            raw = input(t("menu_num_prompt")).strip()
        except KeyboardInterrupt:
            print()
            print(t("interrupted"))
            sys.exit(0)
        if not raw:
            print(t("menu_num_invalid"))
            continue
        try:
            num = int(raw)
        except ValueError:
            print(t("menu_num_invalid"))
            continue
        if num <= 0:
            print(t("menu_num_invalid"))
            continue
        return num


def run_menu():
    """Interactive config screen: toggle settings, then Start."""
    lang = LANGUAGE
    number = 1
    headless = False

    while True:
        clear_screen()
        print("\n" + "="*50)
        print(t("menu_title"))
        print("="*50)
        lang_label = "English" if lang == "en" else "Bahasa Indonesia"
        print(f"{t('menu_lang')}: {lang_label}")
        print(f"{t('menu_number')}: {number}")
        print(f"{t('menu_headless')}: {'ON' if headless else 'OFF'}")
        print(t("menu_start"))
        print(t("menu_exit"))
        print("="*50)

        try:
            choice = input(t("menu_prompt")).strip()
        except KeyboardInterrupt:
            print()
            print(t("interrupted"))
            sys.exit(0)

        if choice == "1":
            lang = "id" if lang == "en" else "en"
            set_language(lang)
        elif choice == "2":
            number = _prompt_number()
        elif choice == "3":
            headless = not headless
        elif choice == "4":
            break
        elif choice == "0":
            sys.exit(0)
        else:
            print(t("menu_invalid"))

    run_bot(number, headless)


# --- HELPERS ---
def _pre_parse_language():
    """Scan argv for --lang before argparse builds (so --help localizes)."""
    argv = sys.argv[1:]
    for i, arg in enumerate(argv):
        if arg.startswith("--lang="):
            set_language(arg.split("=", 1)[1])
            return
        if arg == "--lang" and i + 1 < len(argv):
            set_language(argv[i + 1])
            return


# --- ENTRY POINT UTAMA (CLI HANDLER) ---
def main():
    _pre_parse_language()

    # Jika dijalankan tanpa argumen -> buka menu interaktif
    if len(sys.argv) == 1:
        run_menu()
        return

    # 1. Definisi Argumen CLI
    parser = argparse.ArgumentParser(description="CapCut Auto Register CLI Tool")

    # Argumen Jumlah Akun (-n atau --number)
    parser.add_argument(
        '-n', '--number',
        type=int,
        default=1,
        help=t('number_help')
    )

    # Argumen Headless (--headless)
    parser.add_argument(
        '--headless',
        action='store_true',
        help=t('headless_help')
    )

    # Argumen Bahasa (--lang)
    parser.add_argument(
        '--lang',
        choices=['en', 'id'],
        default=None,
        help=t('lang_help')
    )

    # Parsing argumen
    args = parser.parse_args()
    run_bot(args.number, args.headless)


if __name__ == "__main__":
    main()