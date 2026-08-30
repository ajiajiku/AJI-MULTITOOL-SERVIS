# Firmware / Scatter baseline

Lapisan firmware mengikuti struktur yang teridentifikasi dari GSM Laboratory, terutama parser partition/scatter dan modul GUI flash.

## Data referensi

Scatter MT6765 yang tersedia di proyek memuat partition seperti `lk`, `boot`, `logo`, `dtbo`, `tee1`, `tee2`, `odm`, `vendor`, `system`, `cache`, dan `userdata`, beserta alamat serta ukuran.

## Alur

```text
Scatter
  ↓
Partition map
  ↓
Validasi file/region
  ↓
Mapping ke GPT
  ↓
Flash operation
```

Tahap ini hanya menyiapkan metadata dan validasi. Jangan memasukkan firmware pribadi atau image perangkat ke repository publik.
