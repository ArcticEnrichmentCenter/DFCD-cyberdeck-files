from micropython import const
import machine
import struct
import time
import usb.device

from usb.device.hid import HIDInterface

_INTERFACE_PROTOCOL_MOUSE = const(0x02)


class MouseInterface(HIDInterface):
    def __init__(self, interface_str="MicroPython Mouse"):
        super().__init__(
            _MOUSE_REPORT_DESC,
            protocol=_INTERFACE_PROTOCOL_MOUSE,
            interface_str=interface_str,
        )
        self._l = False  # Left button
        self._m = False  # Middle button
        self._r = False  # Right button
        self._buf = bytearray(5)

    def send_report(self, dx=0, dy=0, w=0, p=0, z=0):
        b = 0
        if self._l:
            b |= 1 << 0
        if self._r:
            b |= 1 << 1
        if self._m:
            b |= 1 << 2
        if z == -1:
            b |= 1 << 3
        if z == +1:
            b |= 1 << 4

        while self.busy():
            machine.idle()

        struct.pack_into("Bbbbb", self._buf, 0, b, dx, dy, w, p)

        return super().send_report(self._buf)

    def click_left(self, down=True):
        self._l = down
        return self.send_report()

    def click_middle(self, down=True):
        self._m = down
        return self.send_report()

    def click_right(self, down=True):
        self._r = down
        return self.send_report()

    def move_by(self, dx, dy):
        if not -127 <= dx <= 127:
            raise ValueError("dx")
        if not -127 <= dy <= 127:
            raise ValueError("dy")
        return self.send_report(dx, dy)

    def scroll(self, w):
        return self.send_report(0, 0, w, 0, 0)

    def pan(self, p):
        return self.send_report(0, 0, 0, p, 0)

    def zoom(self, z):
        return self.send_report(0, 0, 0, 0, z)


# Basic 3-button mouse HID Report Descriptor.
# This is based on Appendix E.10 of the HID v1.11 document.
# fmt: off
_MOUSE_REPORT_DESC = (
    b'\x05\x01'  # Usage Page (Generic Desktop)
        b'\x09\x02'  # Usage (Mouse)
    b'\xA1\x01'  # Collection (Application)
        b'\x09\x01'  # Usage (Pointer)
        b'\xA1\x00'  # Collection (Physical)
            b'\x05\x09'  # Usage Page (Buttons)
                b'\x19\x01'  # Usage Minimum (01),
                b'\x29\x05'  # Usage Maximum (05),
                b'\x15\x00'  # Logical Minimum (0),
                b'\x25\x01'  # Logical Maximum (1),
                b'\x95\x05'  # Report Count (5),
                b'\x75\x01'  # Report Size (1),
                b'\x81\x02'  # Input (Data, Var, Abs)
                b'\x95\x01'  # Report Count (1),
                b'\x75\x03'  # Report Size (3),
                b'\x81\x01'  # Input (Constant), ;5 bit padding
            b'\x05\x01'  # Usage Page (Generic Desktop),
                b'\x09\x30'  # Usage (X),
                b'\x09\x31'  # Usage (Y),
                b'\x09\x38'  # Usage (Wheel),
                b'\x15\x81'  # Logical Minimum (-127),
                b'\x25\x7F'  # Logical Maximum (127),
                b'\x75\x08'  # Report Size (8),
                b'\x95\x03'  # Report Count (3),
                b'\x81\x06'  # Input (Data, Var, Rel)
            b'\x05\x0c'  # Usage Page (Consumer Devices),
                b'\x0a\x38\x02'  # Usage (AC Pan),
                b'\x15\x81'  # Logical Minimum (-127),
                b'\x25\x7F'  # Logical Maximum (127),
                b'\x75\x08'  # Report Size (8),
                b'\x95\x01'  # Report Count (1),
                b'\x81\x06'  # Input (Data, Var, Rel)
        b'\xC0'  # End Collection
    b'\xC0'  # End Collection
)
# fmt: on


def main():
    A = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
    B = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)
    Z = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
    E = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
    I = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
    H = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
    L = machine.Pin(25, machine.Pin.OUT)

    m = MouseInterface()
    usb.device.get().init(m, builtin_driver=True)
    while not m.is_open():
        time.sleep_ms(100)

    pa, pb, pz, pe, pi, ph = True, True, True, True, True, True
    while True:
        a, b, z, e, i, h = A(), B(), Z(), E(), I(), H()
        L(not z)
        if pe != e:
            m.click_middle(not e)
        if pi != i:
            m.click_right(not i)
        if pa and not a:
            if not z:
                if b:
                    m.zoom(+1)
                    m.zoom(0)
                else:
                    m.zoom(-1)
                    m.zoom(0)
            else:
                if h:
                    if b:
                        m.pan(+1)
                    else:
                        m.pan(-1)
                else:
                    if b:
                        m.scroll(+1)
                    else:
                        m.scroll(-1)
        pa, pb, pz, pe, pi, ph = a, b, z, e, i, h
        time.sleep_us(100)


main()
