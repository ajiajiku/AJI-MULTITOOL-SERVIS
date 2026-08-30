from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import re

@dataclass
class Partition:
    name: str
    file_name: str
    linear_start: int | None = None
    physical_start: int | None = None
    size: int | None = None
    region: str = ""
    operation: str = ""

_HEX = re.compile(r"0x[0-9a-fA-F]+")


def _value(text: str, key: str) -> str | None:
    m = re.search(rf"^\s*{re.escape(key)}\s*:\s*(.*?)\s*$", text, re.M)
    return m.group(1).strip().strip('"') if m else None


def _num(value: str | None) -> int | None:
    if not value or value.lower() in {"-", "none", "null"}:
        return None
    try:
        return int(value, 0)
    except ValueError:
        m = _HEX.search(value)
        return int(m.group(0), 16) if m else None


def parse_scatter(path: str | Path) -> list[Partition]:
    """Parse standard MediaTek scatter files and common dashless variants."""
    path = Path(path)
    text = path.read_text(encoding="utf-8-sig", errors="replace")

    # Standard MTK scatter syntax uses YAML-like blocks:
    #   - partition_index: SYS0
    # Older/custom files may omit the leading dash.
    blocks = re.split(
        r"^\s*-?\s*partition_index\s*:\s*[^\r\n]*\r?$",
        text,
        flags=re.I | re.M,
    )

    out: list[Partition] = []
    for block in blocks[1:]:
        name = _value(block, "partition_name") or "unknown"
        file_name = _value(block, "file_name") or ""
        out.append(Partition(
            name=name,
            file_name=file_name,
            linear_start=_num(_value(block, "linear_start_addr")),
            physical_start=_num(_value(block, "physical_start_addr")),
            size=_num(_value(block, "partition_size")),
            region=_value(block, "region") or "",
            operation=_value(block, "operation_type") or "",
        ))
    return out


def firmware_path(scatter: str | Path, file_name: str) -> Path:
    return Path(scatter).resolve().parent / file_name
