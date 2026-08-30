# AJI MULTITOOL SERVIS

Tool servis MediaTek untuk Windows. Baseline kompatibilitas menggunakan **SP Flash Tool v5 yang telah diuji pengguna**, sementara GUI, scatter parser, dry-run planner, dan integrasi launcher dikembangkan di repository ini.

## Status sekarang

**Fase 2 — aplikasi uji sudah siap.**

Fitur:
- GUI AJI MULTITOOL SERVIS berbasis Python/Tkinter.
- Pemilihan dan parsing scatter MediaTek.
- Daftar partisi, alamat, ukuran, region, dan operation.
- Dry-run untuk memeriksa file firmware tanpa menulis perangkat.
- Tombol menjalankan `flash_tool.exe` dari paket SP Flash Tool v5 lokal.
- Test parser otomatis.

Riset menunjukkan pendekatan open-source seperti MTKClient mendukung BROM, DA, GPT, pembacaan/penulisan flash, sedangkan implementasi kompatibilitas scatter dapat dibangun terpisah dari binary SP Flash Tool. citeturn0search7turn0search2

## Uji coba Windows

1. Clone/download repository ini.
2. Ekstrak paket SP Flash Tool v5 Anda ke folder lokal, misalnya:
   `C:\AJI-MULTITOOL-SERVIS\SP_Flash_Tool_v5\`
3. Pastikan terdapat `flash_tool.exe` di folder tersebut.
4. Jalankan `run.bat`.
5. Pilih folder SP Flash Tool v5.
6. Pilih scatter firmware.
7. Tekan **Baca Scatter**.
8. Tekan **Dry-Run Flash Plan** untuk pemeriksaan tanpa hardware write.
9. Jika ingin membuka tool flashing yang sudah terbukti bekerja, tekan **Jalankan SP Flash Tool**.

**Penting:** repository belum mengaktifkan write langsung dari engine AJI. Tahap ini sengaja dibuat aman untuk memvalidasi GUI, parser, firmware mapping, dan integrasi dengan SP Flash Tool yang sudah Anda uji.

## Struktur

```text
app/main.py              GUI utama
tools/scatter_parser.py  parser scatter
tests/                   pengujian
mtk/                     backend MTK yang sedang dikembangkan
docs/                    dokumentasi integrasi
run.bat                  launcher Windows
```

## Referensi SP Flash Tool

Paket yang Anda upload berisi `flash_tool.exe`, beberapa `DA_*.bin`, `MTK_AllInOne_DA.bin`, `FlashToolLib*.dll`, dan komponen Qt. Binary tersebut **tidak disalin ke repository publik**. Gunakan paket SP Flash Tool yang Anda miliki secara lokal.

## Catatan keselamatan

Jangan melakukan flash dengan firmware yang salah. Khususnya jangan menghapus/menulis NVRAM, NVDATA, atau partisi identitas tanpa backup dan verifikasi perangkat. Tahap berikutnya adalah menghubungkan backend MTK open-source secara bertahap setelah pengujian GUI ini berhasil.
