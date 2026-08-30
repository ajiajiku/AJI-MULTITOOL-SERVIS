# Baseline MTK GSM LABORATORY

Dokumen ini mencatat apa yang benar-benar teridentifikasi dari paket referensi yang tersedia pada proyek.

## Komponen utama yang teridentifikasi

| Komponen | Lokasi referensi |
|---|---|
| Executable utama | `MTK GSM LABORATORY.exe` |
| GUI utama | `bin/Doc/mtkclient/gui/main_gui.py` |
| GUI Qt Designer | `bin/Doc/mtkclient/gui/main_gui.ui` |
| Toolkit GUI | `bin/Doc/mtkclient/gui/toolkit.py` |
| Tools menu | `bin/Doc/mtkclient/gui/toolsMenu.py` |
| Read flash | `bin/Doc/mtkclient/gui/readFlashPartitions.py` |
| Write flash | `bin/Doc/mtkclient/gui/writeFlashPartitions.py` |
| BROM/MTK core | `bin/Doc/mtkclient/Library/mtk.py`, `mtk_main.py` |
| DA loader | `bin/Doc/mtkclient/Library/mtk_daloader.py` |
| DA command | `bin/Doc/mtkclient/Library/mtk_da_cmd.py` |
| DA/XFlash | `bin/Doc/mtkclient/Library/mtk_daxflash.py` |
| Preloader | `bin/Doc/mtkclient/Library/mtk_preloader.py` |
| GPT | `bin/Doc/mtkclient/Library/gpt.py` |
| Partition | `bin/Doc/mtkclient/Library/partition.py` |
| USB | `bin/Doc/mtkclient/Library/usblib.py` |
| BROM config | `bin/Doc/mtkclient/config/brom_config.py` |
| MTK config | `bin/Doc/mtkclient/config/mtk_config.py` |
| USB IDs | `bin/Doc/mtkclient/config/usb_ids.py` |
| DA loaders | `bin/Doc/mtkclient/Loader/` |
| Preloader collection | `bin/Doc/mtkclient/Loader/Preloader/` |

## Referensi perangkat yang diuji

Log proyek mencatat perangkat MediaTek `MT6765` / Helio P35/G35 `[0766]`, Sub Code `8A00`, HW `CA00`, SW `0000`, dan USB MediaTek Port dengan VID/PID `0E8D/0003`.

## Urutan operasi yang tercatat pada log

1. BROM terdeteksi.
2. Identitas chipset dibaca.
3. Security state terdeteksi.
4. Tahap keamanan pada log referensi selesai.
5. DA Stage 1 melakukan SYNC.
6. DA Stage 2 berjalan.
7. DA Extended berjalan.
8. RAM dan storage dibaca.
9. GPT diperiksa/diperbaiki ketika diperlukan.
10. Partisi firmware ditulis sesuai scatter.

## Catatan pengembangan

Repository ini tidak menyalin keseluruhan paket binary referensi ke repository publik. Struktur dan perilaku yang terdokumentasi di sini digunakan sebagai baseline untuk implementasi komponen proyek sendiri dan pengujian bertahap.
