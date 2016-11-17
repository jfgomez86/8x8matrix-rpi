# README
This is a very simple implementation of software multiplexing an 8x8 LED Matrix (like this one: [Adafruit](http://adafru.it/1817)).

# Setup
You should first identify the Column and Row pins of your 8x8 LED Matrix. You can do that by reading the datasheet of the LED Matrix. [This](http://www.circuitstoday.com/interfacing-8x8-led-matrix-with-arduino) helped me do so. I used 330 Ohm resistors for all the column pins (anodes?).

# Usage

Open a Python console and try this to familiarize yourself with the code:

```
import base
base.draw("J")
```

*Press `<Control>-C` to stop multiplexing*

