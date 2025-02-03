from machine import Pin               #knihovna pro PICO
from neopixel import NeoPixel         #knihovna pro Neopixel LED
from utime import sleep               #knihovna časování
#původní zdroj programu
#https://www.coderdojotc.org/micropython/basics/05-neopixel/

NEOPIXEL_PIN = 0                      # Pin 1 je 0 protože GP0 :-(
NUMBER_PIXELS = 10                    # počet LED
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)    #inicializace Neopixel pásku

# přepočitání barev dle velikosti parametru
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

# funkce ovládaní LED
def rainbow_cycle(wait):                                  #wait - prodleva mezi zm2nou barev
    global NUMBER_PIXELS, strip                            
    for j in range(255):                                  #změna barvy od 0 do 255
        for i in range(NUMBER_PIXELS):                    #procházení všech LED 
            rc_index = (i * 256 // NUMBER_PIXELS) + j     #dopočet barev  
            strip[i] = wheel(rc_index & 255)              #volání funkce zm2ny barev a zápis do pole na pozici LED 
        strip.write()                                     #zápis do pásku
    sleep(wait)                                           #prodleva v s

counter = 0      # proměnné počítadel
offset = 0

while True:                           #hlavní smyčka
    print('Running cycle', counter)   #výpis počítadla smzčky na konzolu 
    rainbow_cycle(.05)                #jdi na funkci ovládání LED 
    counter += 1                      # počítadlo cyklú 
