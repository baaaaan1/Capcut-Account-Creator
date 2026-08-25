# CapCut Account Maker 🎬

Automation tool untuk membuat akun CapCut secara otomatis menggunakan Playwright. Cocok buat yang males bikin akun satu-satu.

An automation tool that creates CapCut accounts automatically using Playwright. Perfect for anyone who doesn't want to create accounts one by one.

---

## 🌐 Bahasa — Language

- 🇮🇩 [Bahasa Indonesia](#bahasa-indonesia)
- 🇬🇧 [English](#english)

---

<a name="english"></a>
## 🇬🇧 English

### ⚠️ Disclaimer

This tool is built for educational and automation-testing purposes only. Use it responsibly and respect CapCut's Terms of Service. I am not responsible for any misuse of this tool.

### 🚀 Features

- ✅ Auto register CapCut accounts
- ✅ Batch creation (create many accounts at once)
- ✅ Headless mode (runs in the background, browser window is hidden)
- ✅ Secure random password generator
- ✅ Auto-save credentials to JSON
- ✅ Stealth mode (bypass anti-bot detection)
- ✅ **Detailed step logging** — logs every click and wait during account creation
- ✅ **Auto verification** — verifies the account via the CapCut API and stores the `uid`
- ✅ **Error / invalid proof** — failed attempts are also saved to `proof.json`

### ⚠️ Note about Web Selectors (IMPORTANT)

The web selectors used to target elements on the CapCut page may **differ between countries/regions and may change over time** (CapCut frequently updates their UI). If the tool fails to fill the form, register an account, or read the OTP, the selectors in `main.py` probably need to be adjusted. Check the release notes / issues for selector updates.

### 📋 Requirements

- Python 3.8+
- Google Chrome (used by Playwright)
- A stable internet connection

### 🔧 Installation

1. Clone this repository
```bash
git clone https://github.com/baaaaan1/Capcut-Account-Creator.git
cd Capcut-Account-Creator
```

2. Create a virtual environment
```bash
python -m venv .venv
```

3. Activate the virtual environment
```bash
# Windows
.venv\Scripts\Activate.ps1

# Linux/Mac
source .venv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 📧 Preparing the Email List

Create a `gmail-list.txt` file in the project root, filled with a list of emails (one email per line):

```
email1@example.com
email2@example.com
email3@example.com
```

**Recommended Temp Mail Services:**

1. **[Boomlify](https://boomlify.com/)**
2. **[Temp Mail IO](https://temp-mail.io/)**
3. **[NoSpam Today](https://nospam.today/)**
4. **[Email Generator](https://generator.email/)**

> **💡 Note — use a strong email for a higher success rate:**
> For the **best success rate and more security**, prefer a **strong, real email** (e.g. **Gmail** / **Outlook**). Temp-mail domains are frequently blacklisted by CapCut, so real emails get far better OTP deliverability, a much higher account activation/verification rate, and are safer to recover if your password is lost.
>
> If you still prefer temp mail, use the services above — but expect a **lower success rate**.

#### 🪄 Gmail Trick Generator (recommended)

Sick of filling `gmail-list.txt` with many real emails? Use the built-in **Gmail trick generator** (`gmail_gen.py`). It turns **one** real Gmail/Outlook address into many unique-looking addresses, then **auto-writes them to `gmail-list.txt`**:

```bash
python gmail_gen.py -b my.name@gmail.com -n 20
```

- `-b, --base` — your one real email (all generated variants deliver to this inbox)
- `-n, --count` — number of unique emails to generate
- `-m, --mode` — `dot` (Gmail), `plus` (Gmail/Outlook), or `both` (default)
- `--append` — add to the existing list instead of overwriting
- `--lang en|id` — output language

**How the trick works:**
- **Dot trick** (Gmail): Gmail ignores dots, so `my.name@gmail.com` can also be `my.na.me@gmail.com`, `m.y.n.a.me@gmail.com`, etc. — all deliver to the same inbox.
- **Plus trick** (Gmail/Outlook): `base+1@gmail.com`, `base+2@gmail.com` … all deliver to the same inbox.

So with **one real Gmail** you can fill `gmail-list.txt` and register many CapCut accounts — every OTP lands in the same inbox. Run it **with no arguments** to be prompted interactively.

### 🎮 Usage

The output language defaults to **English**. Use the `--lang id` flag (or the interactive menu) to switch to Bahasa Indonesia.

#### Interactive Config Menu

Run `python main.py` with **no arguments** to open an interactive menu and configure the run:

```text
==================================================
🤖 CAPCUT BOT - CONFIG MENU
==================================================
[1] Language / Bahasa: English
[2] Number of accounts / Jumlah akun: 1
[3] Headless mode: OFF
[4] Start / Mulai
[0] Exit / Keluar
==================================================
Choose / Pilih: 
```

- `1` — toggle the output language (English / Bahasa Indonesia)
- `2` — set the number of accounts to create
- `3` — toggle headless mode
- `4` — start running
- `0` — exit

> 💡 Passing **any** argument (e.g. `python main.py -n 5`) skips the menu and runs directly, so the tool stays scriptable. Invalid menu input re-prompts instead of crashing.

#### Create 1 Account

```bash
python main.py -n 1
```

#### Create Multiple Accounts

```bash
python main.py -n 5
```

#### Headless Mode (Background)

```bash
python main.py -n 3 --headless
```

#### Choose the Output Language

```bash
python main.py -n 5 --lang id
```

#### Advanced Options

```bash
python main.py --help
```

Output:
```
usage: main.py [-h] [-n NUMBER] [--headless] [--lang {en,id}]

CapCut Auto Register CLI Tool

options:
  -h, --help            show this help message and exit
  -n, --number NUMBER   Number of accounts to create (Default: 1)
  --headless            Run the browser in the background (not visible)
  --lang {en,id}        Output language: en or id
```

### 📸 CLI Screenshot

Result of a batch of 3 accounts:
![CapCut bot success](image.png)

### 📁 File Structure

```
Capcut-Acc-Maker/
│
├── main.py              # Main script
├── gmail_gen.py         # Gmail trick generator (auto-fill gmail-list.txt)
├── i18n.py              # Bilingual string table (EN / ID)
├── gmail-list.txt       # Email list (created manually)
├── proof.json           # Output credentials (auto-generated)
├── .venv/               # Virtual environment
└── README.md            # This file
```

### 📊 Output Format

Account data is saved to `proof.json`:

```json
[
    {
        "email": "your.email@example.com",
        "password": "YourStrongPassword123!",
        "birthday": "01/01/2000",
        "uid": "YOUR_UID_HERE",
        "verified": true,
        "status": "success",
        "created_at": "2026-08-25T00:00:00.000000"
    }
]
```

> The `uid` and `verified` fields were added after enabling the account verification feature via the `commerce/v1/subscription/user_info` API.

> Failed/invalid attempts are also saved to `proof.json` with `"status": "error"`, `"verified": false` and an `"error"` message, so you can review which emails failed.

> **🔒 Privacy note:** `proof.json` and `gmail-list.txt` contain real credentials and are **git-ignored** — they are never committed. Replace the values above with your own data; they are only placeholders.

### 🐛 Troubleshooting

#### Error: gmail-list.txt file not found

Create a `gmail-list.txt` file first in the project folder.

#### Error: Import "playwright" could not be resolved

Reinstall playwright:
```bash
pip install playwright
playwright install chromium
```

#### Browser doesn't open

Check that Chrome is installed. If not:
```bash
playwright install chromium
```

#### OTP doesn't arrive

- Check the spam folder in the temp mail service
- Wait 30-60 seconds
- If it still doesn't arrive, try another email

### 💡 Tips & Tricks

> **⚠️ Note — use a proxy/VPN to stay safe:**
> Creating many accounts from a single IP is very easy for CapCut to detect and ban. Use a **proxy or VPN** (ideally a different IP per account, or rotate IPs) so each registration looks like it comes from a different user. This dramatically lowers the risk of your main IP and accounts being flagged/blacklisted. Combine it with the email-trick generator above for the best result.

1. **Use a proxy/VPN** when creating many accounts at once to avoid rate limits and IP bans
2. **Don't spam** — wait at least 1-2 minutes between accounts
3. **Back up `proof.json`** regularly
4. **Use different temp mails** so you don't get detected as a bot
5. **Headless mode** is faster but harder to debug when an error occurs

### 📝 Known Issues

- Selectors can change (CapCut updates their UI), just adjust them in `main.py`
- OTP sometimes arrives late, be patient
- Some temp mail domains may be blacklisted by CapCut, try another domain

### 🤝 Contributing

Pull requests are welcome! If you find a bug or have an idea for a new feature, feel free to open an issue.

### 📜 License

MIT License — free to use, modify, and distribute. Use it responsibly.

### ☕ Support

If this tool was useful, consider:
- ⭐ Starring this repo
- 🐛 Reporting a bug you found
- 💡 Suggesting a new feature

---

<a name="bahasa-indonesia"></a>
## 🇮🇩 Bahasa Indonesia

### ⚠️ Disclaimer

Tool ini dibuat untuk keperluan edukasi dan testing automation. Gunakan dengan bijak dan patuhi Terms of Service CapCut. Saya tidak bertanggung jawab atas penyalahgunaan tool ini.

### 🚀 Features

- ✅ Auto register akun CapCut
- ✅ Support batch creation (bisa bikin banyak akun sekaligus)
- ✅ Headless mode (background, ga keliatan browser-nya)
- ✅ Random password generator yang aman
- ✅ Auto-save credentials ke JSON
- ✅ Stealth mode (bypass anti-bot detection)
- ✅ **Detail step logging** — nge-log tiap klik dan tunggu pas bikin akun
- ✅ **Auto verifikasi** — akun diverifikasi via API CapCut dan `uid` disimpan
- ✅ **Proof error/invalid** — percobaan yang gagal juga tersimpan di `proof.json`

### ⚠️ Catatan tentang Web Selector (PENTING)

Selector web yang dipakai buat narget elemen di halaman CapCut bisa **beda di tiap negara dan bisa berubah sewaktu-waktu** (CapCut sering update UI-nya). Kalau tool gagal ngisi form, daftar akun, atau baca OTP, kemungkinan besar selector di `main.py` perlu di-adjust. Cek release notes / issues buat update selector.

### 📋 Requirements

- Python 3.8+
- Google Chrome (dipakai Playwright)
- Koneksi internet yang stabil

### 🔧 Installation

1. Clone repo ini
```bash
git clone https://github.com/baaaaan1/Capcut-Account-Creator.git
cd Capcut-Account-Creator
```

2. Buat virtual environment
```bash
python -m venv .venv
```

3. Aktifkan venv
```bash
# Windows
.venv\Scripts\Activate.ps1

# Linux/Mac
source .venv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 📧 Nyiapin Email List

Buat file `gmail-list.txt` di root folder, isi dengan list email (satu email per baris):

```
email1@example.com
email2@example.com
email3@example.com
```

**Rekomendasi Temp Mail Services:**

1. **[Boomlify](https://boomlify.com/)**
2. **[Temp Mail IO](https://temp-mail.io/)**
3. **[NoSpam Today](https://nospam.today/)**
4. **[Email Generator](https://generator.email/)**

> **💡 Catatan — pake email yang kuat biar success rate lebih gede:**
> Buat **success rate terbaik dan lebih aman**, pake **email kuat / asli** (misal **Gmail** / **Outlook**). Domain temp mail sering di-blacklist CapCut, jadi email asli dapet OTP jauh lebih lancar, tingkat aktivasi/verifikasi akun jauh lebih tinggi, dan lebih aman buat recovery kalo password hilang.
>
> Kalo masih mau pake temp mail, pake layanan di atas — tapi expect **success rate lebih rendah**.

#### 🪄 Generator Gmail Trick (recommended)

Bokep ngisi `gmail-list.txt` dengan banyak email asli? Pake **generator Gmail trick** bawaan (`gmail_gen.py`). Satu email Gmail/Outlook asli jadi banyak alamat yang keliatan unik, lalu **otomatis ditulis ke `gmail-list.txt`**:

```bash
python gmail_gen.py -b my.name@gmail.com -n 20
```

- `-b, --base` — email asli lu (semua varian masuk ke inbox ini)
- `-n, --count` — jumlah email unik yang mau dibuat
- `-m, --mode` — `dot` (Gmail), `plus` (Gmail/Outlook), atau `both` (default)
- `--append` — tambah ke list existing, bukan nimpain
- `--lang en|id` — bahasa output

**Cara kerja trick-nya:**
- **Dot trick** (Gmail): Gmail ng-ignore titik, jadi `my.name@gmail.com` bisa jadi `my.na.me@gmail.com`, `m.y.n.a.me@gmail.com`, dst — semua masuk ke inbox yang sama.
- **Plus trick** (Gmail/Outlook): `base+1@gmail.com`, `base+2@gmail.com` … semua masuk ke inbox yang sama.

Jadi dengan **satu Gmail asli** lu bisa isi `gmail-list.txt` dan daftarin banyak akun CapCut — semua OTP masuk ke inbox yang sama. Jalanin **tanpa argumen** bakal di-prompt interaktif.

### 🎮 Usage

Bahasa output **default-nya English**. Pake flag `--lang id` (atau menu interaktif) buat ganti ke Bahasa Indonesia.

#### Menu Konfigurasi Interaktif

Jalanin `python main.py` **tanpa argumen** buat buka menu interaktif dan atur run-nya:

```text
==================================================
🤖 CAPCUT BOT - CONFIG MENU
==================================================
[1] Language / Bahasa: English
[2] Number of accounts / Jumlah akun: 1
[3] Headless mode: OFF
[4] Start / Mulai
[0] Exit / Keluar
==================================================
Choose / Pilih: 
```

- `1` — ganti bahasa output (English / Bahasa Indonesia)
- `2` — atur jumlah akun yang mau dibuat
- `3` — toggle headless mode
- `4` — mulai jalanin
- `0` — keluar

> 💡 Kalo lu kasih **argumen apapun** (contoh `python main.py -n 5`), menunya di-skip dan langsung jalan — jadi tool tetep bisa dipake di script. Input menu yang invalid bakal di-prompt ulang, bukan error.

#### Bikin 1 Akun

```bash
python main.py -n 1
```

#### Bikin Multiple Akun

```bash
python main.py -n 5
```

#### Headless Mode (Background)

```bash
python main.py -n 3 --headless
```

#### Pilih Bahasa Output

```bash
python main.py -n 5 --lang id
```

#### Advanced Options

```bash
python main.py --help
```

Output:
```
usage: main.py [-h] [-n NUMBER] [--headless] [--lang {en,id}]

CapCut Auto Register CLI Tool

options:
  -h, --help            show this help message and exit
  -n, --number NUMBER   Jumlah akun yang ingin dibuat (Default: 1)
  --headless            Jalankan browser di background (tidak terlihat)
  --lang {en,id}        Output language: en or id
```

### 📸 Screenshot CLI

Hasil batch 3 akun:
![CapCut bot sukses](image.png)

### 📁 File Structure

```
Capcut-Acc-Maker/
│
├── main.py              # Script utama
├── gmail_gen.py         # Generator Gmail trick (auto-fill gmail-list.txt)
├── i18n.py              # String table bilingual (EN / ID)
├── gmail-list.txt       # List email (dibuat manual)
├── proof.json           # Output credentials (auto-generated)
├── .venv/               # Virtual environment
└── README.md            # File ini
```

### 📊 Output Format

Data akun tersimpan di `proof.json`:

```json
[
    {
        "email": "your.email@example.com",
        "password": "YourStrongPassword123!",
        "birthday": "01/01/2000",
        "uid": "YOUR_UID_HERE",
        "verified": true,
        "status": "success",
        "created_at": "2026-08-25T00:00:00.000000"
    }
]
```

> Field `uid` dan `verified` baru ada setelah diaktifkan fitur verifikasi akun via API `commerce/v1/subscription/user_info`.

> Percobaan yang gagal/invalid juga ikut disimpan di `proof.json` dengan `"status": "error"`, `"verified": false` dan pesan `"error"`, jadi bisa dilihat email mana yang gagal.

> **🔒 Catatan privasi:** `proof.json` dan `gmail-list.txt` isinya kredensial asli dan **di-git-ignore** — ga pernah di-commit. Ganti nilai di atas sama data lu sendiri; itu cuma placeholder.

### 🐛 Troubleshooting

#### Error: File gmail-list.txt tidak ditemukan

Buat file `gmail-list.txt` dulu di folder project.

#### Error: Import "playwright" could not be resolved

Install ulang playwright:
```bash
pip install playwright
playwright install chromium
```

#### Browser ga kebuka

Cek Chrome udah terinstall atau belum. Kalo belum:
```bash
playwright install chromium
```

#### OTP ga masuk

- Cek folder spam di temp mail
- Tunggu 30-60 detik
- Kalo masih ga masuk, coba email lain

### 💡 Tips & Tricks

> **⚠️ Catatan — pake proxy/VPN biar aman:**
> Bikin banyak akun dari satu IP gampang banget kedetect sama CapCut dan bisa kena ban. Pake **proxy atau VPN** (ideal tiap akun beda IP, atau rotate IP) biar tiap registrasi keliatan datang dari user beda. Ini jauh nurunin risiko IP utama dan akun lu di-flag/blacklist. Gabungin sama trick email generator di atas buat hasil terbaik.

1. **Pake proxy/VPN** kalo bikin banyak akun sekaligus biar ga kena rate limit dan IP ban
2. **Jangan spam** - kasih jeda minimal 1-2 menit per akun
3. **Backup `proof.json`** secara berkala
4. **Pake temp mail yang beda-beda** biar ga kedetect sebagai bot
5. **Headless mode** lebih cepat tapi susah debug kalo error

### 📝 Known Issues

- Kadang selector CapCut berubah (mereka update UI), tinggal adjust aja di `main.py`
- OTP kadang telat masuk, sabar aja
- Beberapa domain temp mail mungkin diblacklist sama CapCut, coba domain lain

### 🤝 Contributing

Pull request welcome! Kalo nemu bug atau ada ide fitur baru, feel free buat bikin issue.

### 📜 License

MIT License - bebas pake, modif, distribute. Tapi pake dengan bijak.

### ☕ Support

Kalo tool ini berguna, consider buat:
- ⭐ Star repo ini
- 🐛 Report bug yang lu temuin
- 💡 Suggest fitur baru

---

**Dibuat dengan ☕**
