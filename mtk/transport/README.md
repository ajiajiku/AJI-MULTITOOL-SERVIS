# Transport

Lapisan transport mengikuti komponen `usblib.py` pada source referensi GSM Laboratory.

Target tahap ini adalah memisahkan transport dari logika BROM/DA sehingga perangkat dapat diuji tanpa mengubah lapisan protokol.

Komunikasi yang dicatat pada baseline menggunakan MediaTek USB Port dengan VID/PID `0E8D/0003` pada perangkat MT6765.
