# CapCut Account Maker 🎬

Automation tool untuk membuat akun CapCut secara otomatis menggunakan Playwright. Cocok buat yang males bikin akun satu-satu.

## ⚠️ Disclaimer

Tool ini dibuat untuk keperluan edukasi dan testing automation. Gunakan dengan bijak dan patuhi Terms of Service CapCut. Saya tidak bertanggung jawab atas penyalahgunaan tool ini.

## 🚀 Features

- ✅ Auto register akun CapCut
- ✅ Support batch creation (bisa bikin banyak akun sekaligis)
- ✅ Headless mode (background, ga keliatan browser-nya)
- ✅ Random password generator yang aman
- ✅ Auto-save credentials ke JSON
- ✅ Stealth mode (bypass anti-bot detection)
- ✅ Support temp mail

## 📋 Requirements

- Python 3.8+
- Google Chrome (akan dipakai Playwright)
- Koneksi internet yang stabil

## 🔧 Installation

1. Clone repo ini
```bash
git clone https://github.com/username/Capcut-Acc-Maker.git
cd Capcut-Acc-Maker
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
pip install playwright
playwright install chromium
```

## 📧 Nyiapin Email List

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

> **Tips:** Jangan pake gmail asli lu kalo ga mau kena ban. Pake temp mail aja biar aman.

## 🎮 Usage

### Bikin 1 Akun (Default)

```bash
python main.py
```

### Bikin Multiple Akun

```bash
python main.py -n 5
```

### Headless Mode (Background)

```bash
python main.py -n 3 --headless
```

### Advanced Options

```bash
python main.py --help
```

Output:
```
usage: main.py [-h] [-n NUMBER] [--headless]

CapCut Auto Register CLI Tool

options:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        Jumlah akun yang ingin dibuat (Default: 1)
  --headless            Jalankan browser di background (tidak terlihat)
```

## 📁 File Structure

```
Capcut-Acc-Maker/
│
├── main.py              # Script utama
├── gmail-list.txt       # List email (dibuat manual)
├── proof.json          # Output credentials (auto-generated)
├── .venv/              # Virtual environment
└── README.md           # File ini
```

## 📊 Output Format

Data akun tersimpan di `proof.json`:

```json
[
    {
        "email": "example@temp.com",
        "password": "RMePPubILrp!",
        "birthday": "25/05/2003",
        "created_at": "2025-11-20T10:35:01.775443"
    }
]
```

## 🐛 Troubleshooting

### Error: File gmail-list.txt tidak ditemukan

Buat file `gmail-list.txt` dulu di folder project.

### Error: Import "playwright" could not be resolved

Install ulang playwright:
```bash
pip install playwright
playwright install chromium
```

### Browser ga kebuka

Cek Chrome udah terinstall atau belum. Kalo belum:
```bash
playwright install chromium
```

### OTP ga masuk

- Cek folder spam di temp mail
- Tunggu 30-60 detik
- Kalo masih ga masuk, coba email lain

## 💡 Tips & Tricks

1. **Pake VPN** kalo bikin banyak akun sekaligis biar ga kena rate limit
2. **Jangan spam** - kasih jeda minimal 1-2 menit per akun
3. **Backup `proof.json`** secara berkala
4. **Pake temp mail yang beda-beda** biar ga kedetect sebagai bot
5. **Headless mode** lebih cepat tapi susah debug kalo error

## 📝 Known Issues

- Kadang selector CapCut berubah (mereka update UI), tinggal adjust aja di `main.py`
- OTP kadang telat masuk, sabar aja
- Beberapa domain temp mail mungkin diblacklist sama CapCut, coba domain lain

## 🤝 Contributing

Pull request welcome! Kalo nemu bug atau ada ide fitur baru, feel free buat bikin issue.

## 📜 License

MIT License - bebas pake, modif, distribute. Tapi pake dengan bijak.

## ☕ Support

Kalo tool ini berguna, consider buat:
- ⭐ Star repo ini
- 🐛 Report bug yang lu temuin
- 💡 Suggest fitur baru

---

**Dibuat dengan ☕**