#!/bin/bash

# Buat folder sistem
mkdir -p ~/sawit_lang

# Download core engine dari GitHub lu (Ganti 'username' sama username GitHub lu)
curl -o ~/sawit_lang/nyawit_core.py https://raw.githubusercontent.com/username/sawit-lang/main/nyawit_core.py

# Bikin command 'nyawit' biar bisa dipanggil di mana aja
echo 'python ~/sawit_lang/nyawit_core.py "$@"' > $PREFIX/bin/nyawit
chmod +x $PREFIX/bin/nyawit

echo "Selesai ngab! Sekarang ketik 'nyawit' buat mulai beraksi."

