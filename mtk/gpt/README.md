# GPT / Partition baseline

Lapisan ini mengikuti pemetaan source GSM Laboratory:

- `Library/gpt.py`
- `Library/partition.py`
- `Library/mtk.py`
- modul GUI read/write/erase partition

## Fungsi baseline

1. Membaca informasi storage setelah DA tersedia.
2. Membaca dan mem-parsing GPT.
3. Memetakan nama, alamat awal, ukuran, region, dan atribut partition.
4. Menangani kondisi GPT yang tidak valid sesuai alur aplikasi referensi.
5. Menyediakan data partition untuk operasi flash berbasis scatter.

Test case MT6765 pada log referensi menunjukkan storage `HBG4a2`, USERDATA sekitar 29,12 GB dan kondisi `INVALID GPT!` yang kemudian tercatat `Repair Gpt.. OK`.

Implementasi tahap ini difokuskan pada parsing/validasi data; operasi tulis perangkat dilakukan pada tahap flash setelah transport, BROM, dan DA teruji.
