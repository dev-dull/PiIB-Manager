# PiIB Manager
Project to use a Raspberry Pi Zero as an aftermarket in-band management tool, adding enterprise functionality to consumer hardware. Ideal for resuing old desktop hardware for a homelab environment.

## Parts
1. Raspberry Pi Zero WH ('H' has the headers. Get the W if you prefer soldered connections)
    1. Power supply (for getting started)
    1. Keyboard + Mouse (for getting started)
    1. Micro SD card (for OS)
1. Auvidea B102 HDMI to CSI-2 Bridge
1. Breadboard jumper cables (other wiring could work, but the tips will come in helpful here.
1. HDMI cables
1. Micro USB to USB A cable
1. HDMI splitter (optional)

## Wiring
![ alt text](https://github.com/dev-dull/PiIB-Manager/blob/master/images/diagrams/piib.png?raw=true "Wiring diagram")

## TODO:
- Code to send signals to the reset motherboard header
    - See Power Button code
- Code to read HDD and PC speaker headers
    - See Power LED code
    - Partially implemented but needs to take into account the following:
        - The postive pin is always 5v (on most mobotherboards).
        - The voltage on the negitive pin goes low to activate the HDD LED.
- Code that uses the Zero USB port to tell host system it is a device.
    - keyboard and mouse
    - USB storage device
    - [see gist on how to configure the Pi to be multiple devices](https://gist.github.com/gbaman/50b6cca61dd1c3f88f41)
- Code that captures HDMI (camera) input and shows it in some kind of UI
    - [capture camera to network stream](https://picamera.readthedocs.io/en/release-1.13/recipes1.html#capturing-to-a-network-stream) (a network stream might allow some other interesting uses later).
    - [capture images and show in a tkinter GUI app](https://stackoverflow.com/questions/16366857/show-webcam-sequence-tkinter)
    - [same as above, but in-depth](https://www.pyimagesearch.com/2016/05/30/displaying-a-video-feed-with-opencv-and-tkinter/) (this is from 2016)
    - [capture images and show in a PySimpleGUI app](https://www.youtube.com/watch?v=-Dp2_X9q7GU) (no link to code D: )
    - [open source app that does on-the-fly camera adjustmets including resolution and digital zoom](https://github.com/amchagas/Flypi)
    - [PiCameraApp has _appears_ to have on-the-fly camera adjustments](https://github.com/Billwilliams1952/PiCameraApp) (This looks like the best bet for seeing exammples on how to get started.)
    - Tkinter appears to be the most popular platform for GUI development on the Pi.
- Pi config that enables a remote desktop
- Config Management code (puppet, probably) to set up the device.
- Additional research needed for...
    - Thermocouples to monitor temperatures
    - [Monitor PSU voltages](https://www.raspberrypi.org/forums/viewtopic.php?t=57480)

# Potential 5v power sources for the Pi
- Some motherboards have a jumper that can enable keeping the (5v) USB power on even when the machine is powered off
    - inadequate for a Pi 3 (the warning lightning bolt appears intermittently)
    - Pi Zero W runs normally
- If no 5v USB jumper is available, pin 9 (color coded purple) on a 20 or 24 pin motherboard power connector.
    - an always-on 5v line.
    - Untested, but should be the same power source as the mentioned USB jumper.
- The brave or vaguely foolish could wire a standard wall AC to 5v DC adapter to the power connector inside the ATX power supply.

## Testing results:
NOTE: Always test jumper wires for continuity before using.

- Powering up the machine:
    - Directly applying 3.3v and 5v to either pin on the power switch headers on the motherboard failed to boot the machine.
    - Using a transister (PN2222A) across the power switch pinouts on the motherboard worked with a GPIO pin 16 -- see diagram

- Monitoring the Power LED
    - Attaching the the base pin of a transister to the posittive pin of the motherboard PLED connector, then wiring the emmittter and collector to a +3.3v pin and GPIO pin 18 let us read the PLED status.

- Monitoring the HDD LED:
    - Figured out (the hard way) that the negitive pin on the HDD LED pinout _reduces_ voltage to the negitive pin to activate teh HDD activity LED.
    - [@mckern](https://github.com/mckern) helpfully linked [this forum post that confirmed my testing (see post from BMorse)](https://forum.allaboutcircuits.com/threads/pc-hard-drive-activity-led.69991/)
    - So far so good using the NPN 2N3904 transistor that came in a kit from Sparkfun (NOTE: invert value that is read from code when using an NPN trasistor).
    - So far so good using the PNP 2N3906 transistor that came in a kit from Sparkfun.

- Auvidea HDMI bridges
    - The B101 (for the Pi 3) Only supports 1080p at 25fps -- a resolution and refresh rate not likely to be supported during boot up.
    - The B102 (for the Pi Zero WH) has been working much more consistantly (it supports a wider range of resolutions starting at 720p).
    - The B102 was able to show a motherboard boot splash (shown by the BIOS/UEFI) but it was cropped and rapsivid didn't like the resolution change that promptly followed.
