"""
i18n — bilingual (English / Indonesian) string table for the CLI.

This module is leaf-level: it does NOT import anything from main.py
(avoids circular imports). The default language is English (en); it can be
changed via the code constant LANGUAGE, the interactive menu, or the --lang flag.

Usage:
    from i18n import t, set_language, LANGUAGE
    print(t("processing", email=gmail))
"""

LANGUAGE = "en"

STRINGS = {
    "en": {
        # main.py helpers
        "file_not_found": "❌ ERROR: File {filename} not found!",
        "file_empty": "⚠️ INFO: File {filename} is empty!",
        "data_saved": "💾 Data saved to {filename}",

        # main.py account creation
        "emails_exhausted": "❌ No more emails left.",
        "processing": "\n🔹 Processing: {email}",
        "otp_sent": "\n📬 OTP sent to {email}",
        "otp_prompt": "🔑 OTP > ",
        "verify_success": "🪪 Verification successful. UID: {uid}",
        "account_success": "✅ SUCCESS: {email}\n",
        "account_failed": "❌ FAILED {email}: {err}",
        "verif_no_response": "Verification failed: user_info response not received",
        "verif_failed": "Verification failed: ret={ret} errmsg={errmsg}",

        # step logs (detail progress)
        "step_goto": "Opening signup page...",
        "step_goto_done": "Signup page loaded.",
        "step_click_email_btn": "Clicking 'Continue with email'...",
        "step_fill_email": "Filling email field...",
        "step_click_continue": "Clicking 'Continue'...",
        "step_fill_password": "Filling password field...",
        "step_click_daftar": "Clicking 'Sign up'...",
        "step_fill_birthday": "Filling birth date (year/month/day)...",
        "step_next_otp": "Proceeding to OTP page...",
        "step_input_otp": "Entering OTP code...",
        "step_wait_buka": "Waiting for 'Open CapCut' button...",
        "step_click_buka": "Clicking 'Open CapCut'...",
        "step_wait_verify": "Waiting for verification response...",

        # main.py banner / loop
        "banner_started": "🤖 CAPCUT BOT STARTED",
        "banner_target": "🎯 Target: {n} Account(s)",
        "banner_headless": "👻 Headless Mode: {state}",
        "processing_i_of_n": "\n🔄 Processing account {i} of {n}",
        "process_stopped": "⚠️ Process stopped.",
        "interrupted": "\n\n🛑 Script stopped by user (Ctrl+C)",
        "finished": "🏁 DONE. Total Success: {ok}/{total}",

        # argparse help text
        "number_help": "Number of accounts to create (Default: 1)",
        "headless_help": "Run the browser in the background (not visible)",
        "lang_help": "Output language: en or id",

        # interactive menu
        "menu_title": "🤖 CAPCUT BOT - CONFIG MENU",
        "menu_lang": "[1] Language / Bahasa",
        "menu_number": "[2] Number of accounts / Jumlah akun",
        "menu_headless": "[3] Headless mode",
        "menu_start": "[4] Start / Mulai",
        "menu_exit": "[0] Exit / Keluar",
        "menu_prompt": "Choose / Pilih: ",
        "menu_invalid": "❌ Invalid choice, try again.",
        "menu_num_prompt": "Enter number of accounts: ",
        "menu_num_invalid": "❌ Number must be a positive integer.",
        "lang_label_en": "English",
        "lang_label_id": "Bahasa Indonesia",

        # gmail_gen.py
        "gen_base_help": "Base real email (e.g. my.name@gmail.com)",
        "gen_count_help": "Number of unique emails to generate",
        "gen_mode_help": "Trick method: dot / plus / both",
        "gen_file_help": "Output file (default: gmail-list.txt)",
        "gen_append_help": "Append to the list instead of overwriting",
        "gen_base_prompt": "Base email (e.g. my.name@gmail.com): ",
        "gen_count_prompt": "How many unique emails to generate: ",
        "gen_base_invalid": "❌ Base email is not valid (need '@' and a domain).",
        "gen_count_invalid": "❌ Count must be a positive integer.",
        "gen_info_dot": "ℹ️ Dot-trick: dots are ignored by Gmail, all variants land in the same inbox.",
        "gen_info_plus": "ℹ️ Plus-trick (+tag) works on Gmail & Outlook; all land in the same inbox.",
        "gen_dot_gmail_only": "ℹ️ Dot-trick only works on Gmail. For Outlook use --mode plus.",
        "gen_short": "⚠️ Only generated {got}/{want} unique emails (mode/domain limit). Use --mode both or plus for more.",
        "gen_done": "✅ Generated {n} unique email(s) -> {file}",
    },
    "id": {
        # main.py helpers
        "file_not_found": "❌ ERROR: File {filename} tidak ditemukan!",
        "file_empty": "⚠️ INFO: File {filename} sudah kosong!",
        "data_saved": "💾 Data disimpan ke {filename}",

        # main.py account creation
        "emails_exhausted": "❌ Stok email habis.",
        "processing": "\n🔹 Memproses: {email}",
        "otp_sent": "\n📬 OTP dikirim ke {email}",
        "otp_prompt": "🔑 OTP > ",
        "verify_success": "🪪 Verifikasi sukses. UID: {uid}",
        "account_success": "✅ SUKSES: {email}\n",
        "account_failed": "❌ GAGAL {email}: {err}",
        "verif_no_response": "Verifikasi gagal: response user_info tidak diterima",
        "verif_failed": "Verifikasi gagal: ret={ret} errmsg={errmsg}",

        # step logs (detail progress)
        "step_goto": "Membuka halaman signup...",
        "step_goto_done": "Halaman signup sudah terbuka.",
        "step_click_email_btn": "Klik 'Lanjutkan dengan alamat email'...",
        "step_fill_email": "Mengisi kolom email...",
        "step_click_continue": "Klik 'Lanjutkan'...",
        "step_fill_password": "Mengisi kolom password...",
        "step_click_daftar": "Klik 'Daftar'...",
        "step_fill_birthday": "Mengisi tanggal lahir (tahun/bulan/hari)...",
        "step_next_otp": "Melanjutkan ke halaman OTP...",
        "step_input_otp": "Memasukkan kode OTP...",
        "step_wait_buka": "Menunggu tombol 'Buka CapCut'...",
        "step_click_buka": "Klik 'Buka CapCut'...",
        "step_wait_verify": "Menunggu response verifikasi...",

        # main.py banner / loop
        "banner_started": "🤖 CAPCUT BOT STARTED",
        "banner_target": "🎯 Target: {n} Akun",
        "banner_headless": "👻 Mode Headless: {state}",
        "processing_i_of_n": "\n🔄 Proses Akun ke-{i} dari {n}",
        "process_stopped": "⚠️ Proses dihentikan.",
        "interrupted": "\n\n🛑 Script dihentikan oleh User (Ctrl+C)",
        "finished": "🏁 SELESAI. Total Berhasil: {ok}/{total}",

        # argparse help text
        "number_help": "Jumlah akun yang ingin dibuat (Default: 1)",
        "headless_help": "Jalankan browser di background (tidak terlihat)",
        "lang_help": "Output language: en or id",

        # interactive menu
        "menu_title": "🤖 CAPCUT BOT - CONFIG MENU",
        "menu_lang": "[1] Language / Bahasa",
        "menu_number": "[2] Number of accounts / Jumlah akun",
        "menu_headless": "[3] Headless mode",
        "menu_start": "[4] Start / Mulai",
        "menu_exit": "[0] Exit / Keluar",
        "menu_prompt": "Choose / Pilih: ",
        "menu_invalid": "❌ Pilihan tidak valid, coba lagi.",
        "menu_num_prompt": "Masukkan jumlah akun: ",
        "menu_num_invalid": "❌ Jumlah harus angka positif.",
        "lang_label_en": "English",
        "lang_label_id": "Bahasa Indonesia",

        # gmail_gen.py
        "gen_base_help": "Email asli (base), misal my.name@gmail.com",
        "gen_count_help": "Jumlah email unik yang mau dibuat",
        "gen_mode_help": "Metode trick: dot / plus / both",
        "gen_file_help": "File output (default: gmail-list.txt)",
        "gen_append_help": "Tambah ke list (append) bukan timpa",
        "gen_base_prompt": "Email base (misal my.name@gmail.com): ",
        "gen_count_prompt": "Mau bikin berapa email unik: ",
        "gen_base_invalid": "❌ Email base ga valid (harus '@' + domain).",
        "gen_count_invalid": "❌ Jumlah harus angka positif.",
        "gen_info_dot": "ℹ️ Dot-trick: titik di-ignore Gmail, semua varian masuk ke inbox yang sama.",
        "gen_info_plus": "ℹ️ Plus-trick (+tag) jalan di Gmail & Outlook; semua masuk ke inbox yang sama.",
        "gen_dot_gmail_only": "ℹ️ Dot-trick cuma jalan di Gmail. Buat Outlook pake --mode plus.",
        "gen_short": "⚠️ Cuma kebentuk {got}/{want} email unik (limit metode/domain). Pake --mode both atau plus buat lebih.",
        "gen_done": "✅ {n} email unik dibuat -> {file}",
    },
}


def set_language(lang):
    """Switch the active language. Ignores unknown languages."""
    global LANGUAGE
    if lang in STRINGS:
        LANGUAGE = lang


def t(key, **fmt):
    """Translate a key in the active language, falling back to the key itself."""
    return STRINGS[LANGUAGE].get(key, key).format(**fmt)
