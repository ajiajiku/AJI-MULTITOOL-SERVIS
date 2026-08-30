# GSM LABORATORY MTK — Source Inventory

Basis kerja lokal yang tersedia pada proyek ini telah diperiksa dari paket `MTK GSM LABORATORY` yang diekstrak.

## Struktur yang ditemukan

```text
bin/Doc/mtkclient/
├── gui/
│   ├── main_gui.py
│   ├── main_gui.ui
│   ├── toolkit.py
│   ├── toolsMenu.py
│   ├── readFlashPartitions.py
│   ├── writeFlashPartitions.py
│   └── eraseFlashPartitions.py
├── Library/
│   ├── mtk.py
│   ├── mtk_main.py
│   ├── mtk_preloader.py
│   ├── mtk_daloader.py
│   ├── mtk_daxflash.py
│   ├── mtk_da_cmd.py
│   ├── mtk_dalegacy.py
│   ├── daconfig.py
│   ├── usblib.py
│   ├── Port.py
│   ├── gpt.py
│   ├── partition.py
│   ├── pltools.py
│   ├── utils.py
│   ├── error.py
│   ├── meta.py
│   ├── settings.py
│   ├── seccfg.py
│   ├── xflash_ext.py
│   └── modul pendukung hardware/crypto lainnya
└── config/
    ├── brom_config.py
    ├── mtk_config.py
    ├── payloads.py
    └── usb_ids.py
```

Sebanyak **42 file Python** teridentifikasi pada bagian source `mtkclient`, dengan ukuran gabungan sekitar 669 KB. Paket juga memiliki loader, payload, DLL USB, dan binary vendor yang terpisah.

## Baseline perilaku

Log pengujian yang sudah tersimpan menunjukkan urutan berikut pada MT6765:

1. BROM terdeteksi.
2. Chipset MT6765 / Helio P35-G35 `[0766]` diidentifikasi.
3. Status security terbaca.
4. Tahap komunikasi DA berjalan.
5. RAM dan storage terbaca.
6. GPT dapat diperiksa/diperbaiki.
7. Partisi firmware dapat diproses berdasarkan scatter.

## Catatan publikasi

Repository publik ini menggunakan source referensi sebagai dasar rekayasa. Binary vendor/DA/payload dan komponen yang berfungsi khusus untuk melewati mekanisme keamanan tidak dimasukkan ke snapshot publik. Komponen tersebut tetap menjadi objek analisis lokal dan akan dipisahkan dari lapisan GUI serta transport.

## Langkah berikutnya

Tahap berikutnya adalah memetakan dependency `main_gui.py` ke lapisan `mtk/`, kemudian menghubungkan GUI Aji Multitool Servis ke engine komunikasi dan parser milik baseline secara bertahap. Tidak ada perubahan perilaku firmware yang dilakukan pada tahap inventaris ini.
