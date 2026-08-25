"""
Gmail Trick Generator
=====================
Menghasilkan banyak alamat email unik dari SATU email asli (base) lalu
otomatis menulisnya ke gmail-list.txt (file yang dipakai mode manual main.py).

Teknik:
  - "Dot trick"  : sisipkan titik di local-part (khusus Gmail). Semua varian
                   tetap masuk ke inbox yang sama, mis. `my.name@gmail.com`
                   -> `my.na.me@gmail.com`, `m.y.name@gmail.com`, dst.
  - "Plus trick" : tambahkan +tag di local-part. Berjalan di Gmail & Outlook,
                   mis. `base+1@gmail.com`. Semua tetap masuk ke base.

Kenapa penting? Tanpa trick ini, satu email Gmail asli cuma bisa dipake buat
1 akun karena CapCut menganggap tiap varian sebagai alamat berbeda. Dengan
trick ini, lu bikin N akun dari 1 Gmail, dan semua OTP masuk ke inbox yang sama.

Cara pakai:
    python gmail_gen.py                      # tanya base + jumlah secara interaktif
    python gmail_gen.py -b my.name@gmail.com -n 20
    python gmail_gen.py -n 30 --mode plus --append
    python gmail_gen.py --lang id
"""

import argparse
import os
import random
import sys

from i18n import t, set_language


def pre_parse_language():
    """Scan argv untuk --lang sebelum argparse (biar --help terlokalisasi)."""
    argv = sys.argv[1:]
    for i, arg in enumerate(argv):
        if arg.startswith("--lang="):
            set_language(arg.split("=", 1)[1])
            return
        if arg == "--lang" and i + 1 < len(argv):
            set_language(argv[i + 1])
            return


def canonical_local(local):
    """Hapus semua titik untuk dapat bentuk kanonik (dasar dot trick)."""
    return local.replace(".", "")


def dot_variants(canonical):
    """Semua kombinasi penyisipan titik pada local-part kanonik."""
    n = len(canonical)
    if n == 0:
        return []
    variants = []
    for mask in range(1 << (n - 1)):
        s = canonical[0]
        for i in range(n - 1):
            if mask & (1 << i):
                s += "."
            s += canonical[i + 1]
        variants.append(s)
    return variants


def generate(base_email, count, mode="both"):
    """Kembalikan list unik alamat email sejumlah `count` (atau sebanyak mungkin)."""
    local, domain = base_email.rsplit("@", 1)
    canonical = canonical_local(local)
    seen = set()
    result = []

    # 1) Dot trick (prioritas). Catatan: hanya benar-benar berfungsi di Gmail.
    if mode in ("dot", "both"):
        for v in dot_variants(canonical):
            if v not in seen:
                seen.add(v)
                result.append(f"{v}@{domain}")
                if len(result) >= count:
                    return result

    # 2) Plus trick (tidak terbatas). Jalan di Gmail & Outlook.
    if mode in ("plus", "both"):
        tag = 1
        while len(result) < count:
            v = f"{canonical}+{tag}"
            tag += 1
            if v not in seen:
                seen.add(v)
                result.append(f"{v}@{domain}")

    return result


def write_list(emails, path="gmail-list.txt", append=False):
    """Tulis ke `path`, bila append=True gabungkan dengan isi yang sudah ada."""
    existing = []
    if append and os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            existing = [line.strip() for line in f if line.strip()]
    seen = set(existing)
    combined = list(existing)
    for e in emails:
        if e not in seen:
            seen.add(e)
            combined.append(e)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(combined))
        if combined:
            f.write("\n")
    return combined


def main():
    pre_parse_language()

    parser = argparse.ArgumentParser(description="Gmail Trick Generator - auto fill gmail-list.txt")
    parser.add_argument("-b", "--base", default=None, help=t("gen_base_help"))
    parser.add_argument("-n", "--count", type=int, default=None, help=t("gen_count_help"))
    parser.add_argument("-m", "--mode", choices=["dot", "plus", "both"], default="both", help=t("gen_mode_help"))
    parser.add_argument("--file", default="gmail-list.txt", help=t("gen_file_help"))
    parser.add_argument("--append", action="store_true", help=t("gen_append_help"))
    parser.add_argument("--lang", choices=["en", "id"], default=None, help=t("lang_help"))
    args = parser.parse_args()

    # --- Base email ---
    base_email = args.base
    if not base_email:
        base_email = input(t("gen_base_prompt")).strip()
    if "@" not in base_email or "." not in base_email.split("@", 1)[0] + base_email.split("@", 1)[1]:
        print(t("gen_base_invalid"))
        sys.exit(1)

    domain = base_email.rsplit("@", 1)[1].lower()

    # --- Info trick ---
    if args.mode in ("dot", "both") and domain == "gmail.com":
        print(t("gen_info_dot"))
    if args.mode in ("plus", "both"):
        print(t("gen_info_plus"))
    if args.mode in ("dot", "both") and domain != "gmail.com":
        print(t("gen_dot_gmail_only"))

    # --- Jumlah ---
    count = args.count
    if count is None:
        while True:
            try:
                raw = input(t("gen_count_prompt")).strip()
                count = int(raw)
                break
            except (ValueError, TypeError):
                print(t("gen_count_invalid"))
    if count <= 0:
        print(t("gen_count_invalid"))
        sys.exit(1)

    emails = generate(base_email, count, args.mode)

    if len(emails) < count:
        print(t("gen_short", got=len(emails), want=count))

    write_list(emails, args.file, args.append)
    print(t("gen_done", n=len(emails), file=args.file))


if __name__ == "__main__":
    main()
