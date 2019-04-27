# PiIB Manager
Project to use a Raspberry Pi Zero as an aftermarket in-band management tool, adding enterprise functionality to consumer hardware. Ideal for resuing old desktop hardware for a homelab environment.

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
- Code to send signals to the power and reset motherboard headers (may require transistor or relay switch)
- Code to read HDD and PLED motherboard headers (may require a resister or transistor to lower the voltage from the motherboard)
- Code that uses the Zero USB port to send keyboard and mouse signals to the host system.
- Pi config that enables a remote desktop

# Potential 5v power sources for the Pi
- Some motherboards have a jumper that can enable keeping the (5v) USB power on even when the machine is powered off
    - inadequate for a Pi 3 (the warning lightning bolt appears intermittently)
    - Pi Zero W runs normally
- If no 5v USB jumper is available, pin 9 (color coded purple) 
    - an always-on 5v line.
    - Untested, but should be the same power source as the mentioned USB jumper.

## Testing results:
NOTE: The headers on the raspberry pi were too short to make electrical contact with the female connector of the breadboard jumpers I was testing with.

- Powering up the machine:
    - Directly applying 3.3v and 5v to either pin on the power switch headers on the motherboard failed to boot the machine.
    - Using a transister (PN2222A) across the power switch pinouts on the motherboard worked when 3.3v was applied to the base pin (5v also worked, but the gpio pins of the Pi can only ouput 3.3v)
