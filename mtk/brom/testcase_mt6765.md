# BROM test case — MT6765

Sumber: log pengujian yang tersimpan pada proyek.

- Port: MediaTek USB Port_V1632 (COM3)
- USB VID/PID: `0E8D/0003`
- Chipset: `MT6765`
- SoC: Helio P35/G35 `[0766]`
- Sub Code: `8A00`
- HW: `CA00`
- SW: `0000`
- Security state pada awal log: `[SBA DAA SW_JTAG]`
- Preloader yang tercatat: `preloader_oppo6762_18540.bin`

Keberhasilan baseline: BROM terdeteksi dan DA Stage 1 mencapai SYNC; pada log lain perangkat yang sama melanjutkan ke DA Stage 2, DA Extended, informasi RAM/storage, GPT, dan operasi flash.
