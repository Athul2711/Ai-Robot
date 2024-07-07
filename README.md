## AI-Robot Installation Guide

### Video Demo

[![Watch the video](https://img.youtube.com/vi/Ayy0UCJ_gd4/0.jpg)](https://www.youtube.com/watch?v=Ayy0UCJ_gd4)

### Installation Steps

1. **Upload Code to ESP8266:**
   - Upload `espCode.ino` to your ESP8266 module using the Arduino IDE or an equivalent tool.

2. **Edit IP Addresses:**
   - Update the IP address of the ESP8266 in both `main.py` and `senddatatoespv2.py` to match the IP address of your ESP8266 module.

3. **Run Python Scripts on PC:**
   - Open PyCharm (or your preferred Python IDE) on your PC.
   - Run the following scripts:
     - `Senddata.py`
     - `main.py`
     - `senddatatoespv2.py`
   - Note the IP address displayed by `Senddata.py`.

4. **Edit and Run Script on Raspberry Pi:**
   - On your Raspberry Pi (version 3 or 4) with a 3.5-inch screen installed, edit `emo.py` to replace the placeholder IP address with the IP address noted from `Senddata.py`.
   - Run `emo.py` on the Raspberry Pi.

Follow these steps to set up and run your AI-Robot using Google Gemini. Enjoy your project!

