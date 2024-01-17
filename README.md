# SSDestroyer

This project alows you to use a Raspberry Pi Zero 2W as a bad USB with usb mass storage support.

Features:
- USB HID with baisic keystroke injection
- USB mass storage with USb boot
- WI-FI & Bluetooth

## Setup:

- Clone this repo on your pi.
```
git clone https://github.com/thatduckoverthere/SSDestroyer
```
- Folow this instructabels tutorial and after step 3 stop.[https://www.instructables.com/Raspberry-Pi-Zero-W-As-WiFi-USB-Media-Device/](https://www.instructables.com/Raspberry-Pi-Zero-W-As-WiFi-USB-Media-Device/)

- Create and foramt the binaty files that we will use as the "flash drives". This will take some time.
```
sudo dd bs=1M if=/dev/zero of=/piusb0.bin count=16384
```
```
sudo mkdosfs /piusb0.bin -F 32 -I
```

```
sudo dd bs=1M if=/dev/zero of=/piusb1.bin count=8192 
```
```
sudo mkdosfs /piusb1.bin -F 32 -I
```

```
sudo dd bs=1M if=/dev/zero of=/piusb2.bin count=4096
```
```
sudo mkdosfs /piusb2.bin -F 32 -I
```

```
sudo dd bs=1M if=/dev/zero of=/piusb3.bin count=4096
```
```
sudo mkdosfs /piusb3.bin -F 32 -I
```
- Continue the instructabels tutorial from step 5, excludeing step 7.

- Make the python code run on startup.


Open the rc.local file
```
sudo nano /etc/rc.local
```
Enter the following line of code before the "exit 0" line.
```
python3 /home/pi/SSDestroyer/main.py &
```
- Reboot
```
sudo reboot now
```
now you can access the web ui at [raspberrypi.local:8080](raspberrypi.local:8080)