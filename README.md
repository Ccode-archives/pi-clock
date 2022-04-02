# pi-clock
A clock for your programming desk.

# Setup
## Supplies
* Breadboard
* Raspberry pi pico with micropython installed
* 4xFemale to male jumper wires
* 2xMale to male jumper wires
* An i2c lcd screen (https://www.amazon.com/HiLetgo-HD44780-I2C1602-Interface-Backlight/dp/B07W5KC65S?tag=georiot-us-default-20&ascsubtag=tomshardware-us-1175317091022762200-20&geniuslink=true)
## Assemble
1. Put the pico on thee breadboard
2. Route the 3v3 out pin to the posistive rail of the breadboard.
3. Route the GND pin to the negaive rail of the breadboard.
4. Route the VCC pin of the lcd to the positive rail of the breadboard.
5. Route the GND pin of the lcd to the negative rail of the breadboard.
6. Route the SDA pin of the lcd to the pico's GPIO 1 pin.
7. Route the SCL pin of the lcd to the pico's GPIO 2 pin.
8. Turn the dial on the back of the lcd all thee way left.
## Upload software
1. upload these scripts to your pico using Thonny (https://raw.githubusercontent.com/dhylands/python_lcd/master/lcd/lcd_api.py) (https://raw.githubusercontent.com/T-622/RPI-PICO-I2C-LCD/main/pico_i2c_lcd.py)
2. Upload clock.py from this repository.
## Run
Open Thonny and connect to the pico.  Load clock.py and run it.  It should start showing the current time on the lcd.
