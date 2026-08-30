# AJI MULTITOOL SERVIS

Proyek pengembangan tool servis Android/MediaTek dengan baseline analisis paket MTK GSM LABORATORY yang sudah diberikan dalam proyek ini.

## Prinsip proyek

- Nama proyek: **AJI MULTITOOL SERVIS**.
- Fungsi inti yang menjadi target: deteksi MediaTek BROM, identifikasi perangkat, komunikasi DA, pembacaan storage/GPT, parsing scatter, serta operasi flash/servis.
- GUI dikembangkan bertahap dengan mempertahankan alur kerja referensi.
- Lapisan transport USB/UART dipisahkan agar dapat diuji dan dikembangkan tanpa mengubah logika perangkat.
- Binary/vendor dari paket referensi tidak disalin ke repository publik tanpa dasar distribusi yang sesuai.

## Baseline yang dipetakan

Paket referensi yang tersedia berisi executable utama, runtime Python, PySide6, pyserial/pyusb, dan modul MTKClient. Struktur yang teridentifikasi mencakup GUI, library BROM/DA, konfigurasi chipset, loader/preloader, serta library GPT/partition.

Inventaris source lengkap yang berhasil dipetakan dari paket lokal dicatat di `docs/GSM_SOURCE_INVENTORY.md`.

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

Log pengujian tersimpan menunjukkan `MT6765`, Helio P35/G35 `[0766]`, Sub Code `8A00`, BROM HW `CA00`, dan storage `HBG4a2`. Urutan yang berhasil pada baseline meliputi deteksi BROM, pembacaan security state, DA Stage 1/2/Extended, pembacaan RAM/storage, pemeriksaan/perbaikan GPT, dan penulisan partisi firmware. fileciteturn221file0L15-L39

## Status

**Fase 1 — source inventory selesai.**

Langkah aktif berikutnya: mengambil modul komunikasi dan parser yang diperlukan dari baseline lokal, kemudian mengintegrasikannya ke struktur Aji Multitool Servis secara bertahap dan dapat diuji.
