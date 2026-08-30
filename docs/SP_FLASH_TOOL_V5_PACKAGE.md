# SP Flash Tool v5 — Paket Referensi Lokal

Paket `SP_Flash_Tool_v5.zip` yang diberikan pengguna telah diinventarisasi sebagai baseline pengembangan.

## Komponen utama terdeteksi

- `flash_tool.exe` — executable utama
- `FlashToolLib.dll`, `FlashToolLib.v1.dll`, `FlashtoollibEx.dll` — library utama
- `MTK_AllInOne_DA.bin` — Download Agent
- `DA_PL.bin`, `DA_PL_CRYPTO20.bin` — DA variant
- `DA_SWSEC.bin`, `DA_SWSEC_CRYPTO20.bin` — DA/security variant
- `SLA_Challenge.dll` — komponen SLA
- `BromAdapterTool.ini` — konfigurasi BROM adapter
- `usb_setting.xml` — konfigurasi USB
- `storage_setting.xml` — konfigurasi storage
- `dl_without_scatter.xml` — konfigurasi download tanpa scatter
- `rb_without_scatter.xml` — konfigurasi readback tanpa scatter
- `platform.xml` — metadata platform
- Qt 4 runtime dan codec DLL

## Kesimpulan

Paket ini adalah **binary distribution**, bukan source tree C/C++ lengkap. Karena itu AJI MULTITOOL tidak akan mengklaim `flash_tool.exe` atau DLL sebagai source code. Komponen tersebut diperlakukan sebagai **referensi/baseline lokal**.

Pengembangan AJI MULTITOOL akan mengambil kompatibilitas workflow dan mengimplementasikan engine yang dapat didistribusikan berdasarkan source yang lisensinya jelas/open-source, sambil tetap mendukung artefak DA/firmware milik pengguna secara terpisah.

## Status

Baseline SP Flash Tool v5 diterima dan ditetapkan sebagai referensi pengujian. Prioritas implementasi berikutnya: **Scatter Parser → BROM transport → DA loader → GPT → Flash Engine**.
