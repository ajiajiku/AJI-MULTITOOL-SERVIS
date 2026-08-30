# Integrasi SP Flash Tool ke AJI MULTITOOL SERVIS

## Status

AJI MULTITOOL SERVIS akan menggunakan pendekatan **clean-room / open-source compatible**. Source SP Flash Tool v5.1720 yang dipublikasikan di `acontini/SP-Flash-Tool-src` tercatat sebagai GPL-3.0, tetapi beberapa repositori terkait menyebut adanya binary/vendor blob pada varian source tertentu. Karena itu komponen dengan lisensi atau asal-usul yang belum terverifikasi tidak dimasukkan langsung ke repository ini.

Referensi:
- https://github.com/acontini/SP-Flash-Tool-src
- https://github.com/galaxy4public/SP_Flash_Tool
- https://github.com/bkerler/mtkclient

## Arsitektur target

```text
GUI AJI MULTITOOL
      |
      +-- Scatter parser
      +-- Flash job planner
      +-- Device identification
      |
      v
MTK transport abstraction
      |
      +-- USB
      +-- UART (bila diperlukan)
      |
      v
MediaTek protocol layer
      |
      +-- BROM handshake
      +-- DA transport
      +-- storage/GPT
      +-- partition read/write
```

## Aturan integrasi

1. Jangan memasukkan executable SP Flash Tool proprietary ke source tree.
2. Jangan memasukkan loader/preloader milik perangkat tanpa lisensi/asal yang jelas.
3. Modul yang bersumber dari GPL wajib mempertahankan copyright/license dan memenuhi kewajiban GPL saat didistribusikan.
4. Parser scatter, GPT, job planner, GUI, dan abstraction layer dikembangkan sebagai kode AJI MULTITOOL SERVIS.
5. Implementasi flash harus memiliki mode simulasi/dry-run sebelum hardware write diaktifkan.
6. Operasi yang berpotensi menghapus NVRAM/NVDATA/identitas perangkat harus memerlukan konfirmasi eksplisit.

## Tahap implementasi

- [x] Repository AJI MULTITOOL SERVIS tersedia.
- [x] Struktur MTK baseline tersedia.
- [x] Catatan integrasi SP Flash Tool dibuat.
- [ ] Parser scatter yang kompatibel dengan format umum MediaTek.
- [ ] Flash job planner.
- [ ] Transport USB MTK.
- [ ] BROM identification.
- [ ] DA session layer.
- [ ] GPT reader.
- [ ] Flash engine.
- [ ] GUI flash workflow.
- [ ] Automated tests.

## Catatan

Targetnya bukan membuat salinan binary SP Flash Tool, melainkan membuat AJI MULTITOOL SERVIS dengan workflow flashing MediaTek yang dapat diaudit dan dikembangkan dari komponen yang lisensinya jelas.