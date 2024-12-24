from machine import Pin 
from machine import ADC #Analog to Digital Converter
import time
import dht

LedRed= Pin(0, Pin.OUT)
LedYellow= Pin(1, Pin.OUT)
LedGreen= Pin(2, Pin.OUT)
RelayPump= Pin(3, Pin.OUT) #This relay controls the pump to irrigate or not to irrigate the plant.
RelayLight= Pin(5 , Pin.OUT) #This relay provides the quantity of luminosity that needs the plant.
RelayAir = Pin(6, Pin.OUT) #This relay allows the ventilating of the plant.
HumidityTemperatureSensor = dht.DHT22(Pin(4))
ObscuritySensor = ADC(28)
TemperatureAirSensor = ADC(27)

while True:
    HumidityTemperatureSensor.measure()
    SoilTemperature = HumidityTemperatureSensor.temperature() #Temperature of the plant's soil.
    SoilHumidity = HumidityTemperatureSensor.humidity()
    obscurity= ObscuritySensor.read_u16() *(100/65536) #unsigned : 0 - 65536
                                                       #The luminosity value is converted to a luminosity percentage
    ExternalTemperature = TemperatureAirSensor.read_u16()
    
#Irrigation based on humidity:    
    if (0<= SoilHumidity <= 30):   #Alert: excessive dryness!
        LedRed.on()
        LedYellow.off()
        LedGreen.off()
        RelayPump.off()

    elif (30< SoilHumidity <= 70): #Alert: moderate dryness!
        LedRed.off()
        LedYellow.on()
        LedGreen.off()
        RelayPump.on() #This relay is 'on' in the case of moderate dryness in order to not reach the excessive dryness case. 
    
    else:                          #Normal case
        LedRed.off()
        LedYellow.off()
        LedGreen.on()
        RelayPump.off()

#Providing luminosity based on natural obscurity    
    if (obscurity>70):
        RelayLight.on() 

    else:
        RelayLight.off()

#Plant ventilation in case of exceeding 25°C:
    if(ExternalTemperature < 32535): #32535 is the numeric ADC value of 25°C given by the sensor of external temperature.
        RelayAir.on()

    else:
        RelayAir.off()