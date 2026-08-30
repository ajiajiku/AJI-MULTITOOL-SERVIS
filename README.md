# AJI MULTITOOL SERVIS

Proyek pengembangan tool servis Android/MediaTek dengan baseline analisis paket MTK GSM LABORATORY yang sudah diberikan dalam proyek ini.

## Prinsip proyek

- Nama proyek: **AJI MULTITOOL SERVIS**.
- Fungsi inti yang menjadi target: deteksi MediaTek BROM, identifikasi perangkat, komunikasi DA, pembacaan storage/GPT, parsing scatter, serta operasi flash/servis yang dapat dijalankan melalui antarmuka yang sah.
- GUI dikembangkan bertahap dengan mempertahankan alur kerja referensi.
- Lapisan transport USB/UART dipisahkan agar dapat diuji dan dikembangkan tanpa mengubah logika perangkat.
- Binary/vendor dari paket referensi tidak disalin ke repository publik tanpa dasar distribusi yang sesuai.

## Baseline yang dipetakan

Paket referensi yang tersedia berisi executable utama, runtime Python, PySide6, pyserial/pyusb, dan modul MTKClient. Struktur yang teridentifikasi mencakup:

- `bin/Doc/mtkclient/gui/main_gui.py`
- `bin/Doc/mtkclient/gui/main_gui.ui`
- modul read/write flash
- library BROM/DA
- konfigurasi chipset
- loader dan preloader
- library GPT/partition

## Target arsitektur

```text
AJI MULTITOOL SERVIS
├── app/                 # aplikasi utama dan GUI
├── mtk/                 # lapisan komunikasi MediaTek
│   ├── brom/            # deteksi/handshake/identifikasi
│   ├── da/              # komunikasi Download Agent
│   ├── gpt/             # pembacaan dan parsing GPT
│   └── flash/           # operasi flash berbasis scatter
├── transport/           # abstraksi USB/UART
├── firmware/            # parser dan metadata firmware
├── ui/                  # resource dan desain antarmuka
├── tests/               # pengujian tanpa perangkat terlebih dahulu
└── docs/                # dokumentasi dan catatan teknis
```

## Referensi MT6765

Log pengujian yang tersimpan pada proyek menunjukkan `MT6765`, Helio P35/G35 `[0766]`, Sub Code `8A00`, BROM HW `CA00`, dan storage `HBG4a2`. Log tersebut menunjukkan urutan deteksi BROM, pembacaan security state, tahapan DA, pembacaan storage, perbaikan GPT, kemudian penulisan partisi firmware.

## Status

**Fase 0 — baseline dan pemetaan arsitektur.**

Perubahan berikutnya akan dibuat dalam commit kecil agar setiap tahap dapat diuji secara terpisah.
