# BROM baseline

Modul ini disiapkan berdasarkan source BROM/MTK pada paket GSM Laboratory yang diberikan sebagai referensi.

## Modul referensi

- `Library/mtk.py`
- `Library/mtk_main.py`
- `Library/usblib.py`
- `config/brom_config.py`
- `config/mtk_config.py`
- `config/usb_ids.py`

## Test case perangkat

Baseline log menggunakan MediaTek USB Port `VID=0E8D`, `PID=0003` dan mengidentifikasi `MT6765`, Helio P35/G35 `[0766]`, Sub Code `8A00`, HW `CA00`, SW `0000`.

Tahap ini hanya mencatat dan memisahkan deteksi/identifikasi BROM. Implementasi autentikasi atau mekanisme bypass security tidak direplikasi di modul ini.
