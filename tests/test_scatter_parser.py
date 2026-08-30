import tempfile
from pathlib import Path
from tools.scatter_parser import parse_scatter

def test_parse_scatter():
    text='''############################################################################################################\n- partition_index: SYS0\n  partition_name: preloader\n  file_name: preloader.bin\n  is_download: true\n  type: SV5_BL_BIN\n  linear_start_addr: 0x0\n  physical_start_addr: 0x0\n  partition_size: 0x40000\n  region: EMMC_BOOT_1\n  operation_type: BIN\n- partition_index: SYS1\n  partition_name: boot\n  file_name: boot.img\n  linear_start_addr: 0x80000\n  physical_start_addr: 0x80000\n  partition_size: 0x2000000\n  region: EMMC_USER\n'''
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/'MT6765_Android_scatter.txt'; p.write_text(text)
        parts=parse_scatter(p)
        assert len(parts)==2
        assert parts[0].name=='preloader'
        assert parts[1].size==0x2000000
