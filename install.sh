#!/bin/bash

echo "🚀 Memulai instalasi Sawit-Lang (Pria 19 JT IQ Edition)..."

# Buat folder sistem jika belum ada
mkdir -p ~/sawit_lang

# Download core engine terbaru dari GitHub kamu
curl -o ~/sawit_lang/nyawit_core.py https://raw.githubusercontent.com/Reyofficial77/sawit-lang/main/nyawit_core.py

# Membuat perintah 'nyawit' agar bisa dipanggil dari mana saja
echo 'python ~/sawit_lang/nyawit_core.py "$@"' > $PREFIX/bin/nyawit
chmod +x $PREFIX/bin/nyawit

echo "✅ Selesai ngab! Sekarang ketik 'nyawit' buat beraksi."
echo "💡 Contoh: nyawit now file.sawit"

