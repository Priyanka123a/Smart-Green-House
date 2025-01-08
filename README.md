
## Submitted by SURIYA AKSHAYA.N JUSTINA.A EIJAS MOHAMED.P TAMIL.S VELAN.V College Name: UNIVERSITY COLLEGE OF ENGINEERING, BIT CAMPUS, TRICHY##

This project demonstrates how to measure temperature and humidity using a DHT22 sensor and display the readings on a 16x2 I2C LCD screen. It also logs the data to the serial monitor, making it suitable for IoT applications, prototyping, and educational purposes.

Features:
Sensor Integration: Reads temperature and humidity using the DHT22 sensor.
Real-Time Display: Displays the measured data on a 16x2 I2C LCD screen.
Line 1: Temperature in Celsius.
Line 2: Humidity in percentage.
Serial Output: Logs the temperature and humidity readings to the serial monitor for debugging or additional processing.
Simulation Ready: Designed for use with the Wokwi Online IoT Simulator, but also works with real hardware.
Libraries Used:
DHTesp: For reading data from the DHT22 sensor.
LiquidCrystal_I2C: For controlling the 16x2 I2C LCD module.
Setup Instructions:
Connect the DHT22 sensor to the specified pin (DHT_PIN = 15) on your microcontroller.
Connect the 16x2 I2C LCD to the I2C bus (I2C_ADDR = 0x27).
Upload the code to your microcontroller using the Arduino IDE.
Open the serial monitor to view the temperature and humidity readings.
Observe the real-time data displayed on the LCD.
