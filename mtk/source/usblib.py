#!/usr/bin/python3
# -*- coding: utf-8 -*-
# (c) B.Kerler 2018-2021 GPLv3 License
# Ported from the GSM Laboratory MTK source baseline supplied for this project.
# Security-bypass routines are intentionally excluded from the Aji MultiTool integration.
import io
import logging
import time
import inspect
import traceback
from struct import calcsize
from enum import Enum
from binascii import hexlify
from ctypes import c_void_p, c_int

import usb.core
import usb.util
import usb.backend.libusb0
import usb.backend.libusb1

USB_DIR_OUT = 0
USB_DIR_IN = 0x80
USB_TYPE_MASK = (0x03 << 5)
USB_TYPE_STANDARD = (0x00 << 5)
USB_TYPE_CLASS = (0x01 << 5)
USB_TYPE_VENDOR = (0x02 << 5)
USB_TYPE_RESERVED = (0x03 << 5)
USB_RECIP_MASK = 0x1f
USB_RECIP_DEVICE = 0x00
USB_RECIP_INTERFACE = 0x01
USB_RECIP_ENDPOINT = 0x02
USB_RECIP_OTHER = 0x03
USB_RECIP_PORT = 0x04
USB_RECIP_RPIPE = 0x05

tag = 0

CDC_CMDS = {
    "SEND_ENCAPSULATED_COMMAND": 0x00,
    "GET_ENCAPSULATED_RESPONSE": 0x01,
    "SET_COMM_FEATURE": 0x02,
}

class USBTransportBaseline:
    """Minimal transport-facing compatibility layer from the supplied source.

    Device discovery only; protocol/security operations remain in the original
    MTK layers and are intentionally not implemented here.
    """
    VID = 0x0E8D
    PID = 0x0003

    @classmethod
    def find_devices(cls, vid=VID, pid=PID):
        return list(usb.core.find(find_all=True, idVendor=vid, idProduct=pid) or [])

    @classmethod
    def identify_usb(cls, device):
        return {
            "vid": getattr(device, "idVendor", None),
            "pid": getattr(device, "idProduct", None),
            "manufacturer": getattr(device, "manufacturer", None),
            "product": getattr(device, "product", None),
            "serial_number": getattr(device, "serial_number", None),
        }
