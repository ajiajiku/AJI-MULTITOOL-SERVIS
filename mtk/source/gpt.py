#!/usr/bin/python3
# -*- coding: utf-8 -*-
# (c) B.Kerler 2018-2021
# Ported from the GSM Laboratory MTK source baseline supplied for this project.
import struct
import zlib
from dataclasses import dataclass

@dataclass
class GPTPartition:
    index: int
    name: str
    first_lba: int
    last_lba: int
    attributes: int
    type_guid: bytes
    unique_guid: bytes

class GPTParser:
    """GPT reader derived from the supplied GSM Laboratory baseline.

    This module parses GPT metadata only. It does not write or repair a device.
    """
    HEADER_SIZE = 92
    ENTRY_SIZE = 128

    @staticmethod
    def parse_header(data: bytes):
        if len(data) < GPTParser.HEADER_SIZE or data[:8] != b"EFI PART":
            raise ValueError("Invalid GPT header")
        revision, header_size, header_crc, reserved = struct.unpack_from("<IIII", data, 8)
        current_lba, backup_lba, first_usable, last_usable = struct.unpack_from("<QQQQ", data, 24)
        disk_guid = data[56:72]
        entry_lba, entry_count, entry_size = struct.unpack_from("<QII", data, 72)
        return {
            "revision": revision,
            "header_size": header_size,
            "header_crc": header_crc,
            "current_lba": current_lba,
            "backup_lba": backup_lba,
            "first_usable_lba": first_usable,
            "last_usable_lba": last_usable,
            "disk_guid": disk_guid.hex(),
            "part_entry_start_lba": entry_lba,
            "num_part_entries": entry_count,
            "part_entry_size": entry_size,
        }

    @staticmethod
    def parse_entries(data: bytes, count: int, entry_size: int):
        if entry_size < 128:
            raise ValueError("Unsupported GPT entry size")
        result = []
        for index in range(count):
            off = index * entry_size
            entry = data[off:off + entry_size]
            if len(entry) < 128:
                break
            type_guid = entry[0:16]
            unique_guid = entry[16:32]
            first_lba, last_lba, attributes = struct.unpack_from("<QQQ", entry, 32)
            raw_name = entry[56:128]
            name = raw_name.decode("utf-16-le", errors="ignore").split("\x00", 1)[0]
            if name or type_guid != bytes(16):
                result.append(GPTPartition(index, name, first_lba, last_lba, attributes, type_guid, unique_guid))
        return result
