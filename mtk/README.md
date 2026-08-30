# MTK core

Struktur modul ini mengikuti pemetaan source MTK GSM LABORATORY yang tersedia pada baseline proyek.

## Urutan baseline

1. Transport USB
2. BROM detection/handshake
3. Identifikasi chipset
4. DA Stage 1
5. DA Stage 2
6. DA Extended
7. RAM/storage information
8. GPT/partition handling
9. Flash operation

Implementasi Aji MultiTool akan mengambil struktur dan perilaku yang dapat digunakan dari source baseline, sambil menjaga pemisahan modul agar setiap tahap dapat diuji sendiri.

## Referensi modul

- `Library/mtk.py`
- `Library/mtk_main.py`
- `Library/mtk_daloader.py`
- `Library/mtk_da_cmd.py`
- `Library/mtk_daxflash.py`
- `Library/mtk_preloader.py`
- `Library/usblib.py`
- `Library/gpt.py`
- `Library/partition.py`
