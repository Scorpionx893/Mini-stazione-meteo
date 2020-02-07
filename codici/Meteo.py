import RPi.GPIO as GPIO ##importiamo la libreria GPIO(General Purpose Input/OutPut)
import dht11 ##importiamo la libreria dht11(sensore di temp e umidità)
import I2C_LCD_driver ## importiamo la libreria I2C LCD

from time import *

lcd = I2C_LCD_driver.lcd() ##assegniamo a lcd la classe lcd presente in I2C_LCD_driver

GPIO.setwarnings(False) ## serve a disabilitare gli avvisi
GPIO.setmode(GPIO.BCM) ##L'opzione GPIO.BCM specifica che si fa riferisce ai pin in base al numero del pin del Raspberry
GPIO.cleanup() ## Ripristina tutte le porte di input, utilizzate in questo programma

lcd.lcd_display_string("mini stazione", 1)

while True:

  instanza = dht11.DHT11(pin = 27) ##(pin = pin GPIO) in questo caso il pin del segnale del DHT-11 è collegato al GPIO27
  risultato = instanza.read() ## Se è presente un segnale dal dht11

# Fahrenheit:
# risultato.temperature = (risultato.temperature * 1.8) + 32

  if risultato.is_valid(): ## se il segnale è valido stampa sul lcd temp e umidità
    lcd.lcd_display_string("Temperatura:%d%sC" % (risultato.temperature, chr(223)), 1)
    lcd.lcd_display_string("Umidita:    %d %%" % risultato.humidity, 2)
