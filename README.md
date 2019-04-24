# PiPMI
Project to use a Raspberry Pi Zero as an aftermarket IPMI (BMC, Drac, iDrac, et. al.) adding enterprise functionality to consumer hardware. Ideal for resuing old desktop hardware for a homelab environment.

## Parts
1. Raspberry Pi Zero WH ('H' has the headers. Get the W if you prefer soldered connections)
    1. Power supply (for getting started)
    1. Keyboard + Mouse (for getting started)
    1. Micro SD card (for OS)
1. Auvidea B102 HDMI to CSI-2 Bridge (get the 101 if you're _not_ using a Pi Zero. Do _*NOT*_ combine the Pi Zero, the B101, and the official Pi camera adaptor ribbon cable)
1. Breadboard jumper cables (other wiring could work, but the tips will come in helpful here.
1. HDMI cables
1. Micro USB to USB A cable
1. HDMI splitter (optional)

## TODO:
- Code to send signals to the power and reset motherboard headers (may require transister or relay switch)
- Code to read HDD and PLED motherboard headers (may require a resister or transister to lower the voltage from the motherboard)
- Code that uses the Zero USB port to send keyboard and mouse signals to the host system.
- Pi config that enables a remote desktop
