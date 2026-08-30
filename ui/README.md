# GUI baseline — AJI MULTITOOL SERVIS

GUI ini mengikuti pemetaan GUI pada paket MTK GSM LABORATORY yang diberikan sebagai baseline.

## Source referensi

- `bin/Doc/mtkclient/gui/main_gui.py`
- `bin/Doc/mtkclient/gui/main_gui.ui`
- `bin/Doc/mtkclient/gui/toolkit.py`
- modul GUI read/write/erase flash

## Prinsip tahap ini

Tampilan dan alur kerja referensi dipertahankan sebagai acuan. Branding target proyek adalah **AJI MULTITOOL SERVIS**.

Fungsi GUI akan dihubungkan ke engine MTK melalui lapisan `mtk/`, bukan dengan membuat komunikasi perangkat kedua yang terpisah.

## Alur GUI baseline

```text
GUI
 ├── koneksi / device
 ├── informasi perangkat
 ├── partition / GPT
 ├── read
 ├── write / flash
 └── erase
```

Tahap ini tidak memasukkan mekanisme bypass autentikasi/security.
