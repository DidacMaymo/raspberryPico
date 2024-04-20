from machine import Pin  #esta clase se utiliza para interactuar con los pines GPIO de la Raspberry Pi Pico.
import utime #proporciona funciones para trabajar con el tiempo

#Se configura como una entrada (Pin.IN) y se activa una resistencia de pull-down (Pin.PULL_DOWN),
#que es una configuración típica para leer un sensor PIR
pir = Pin(28,Pin.IN,Pin.PULL_DOWN)

#Este pin está conectado a un LED rojo que se encenderá cuando se detecte movimiento.
rojo = Pin(16,Pin.OUT)

#Este pin está conectado a un zumbador que sonará cuando se detecte movimiento.
buzzer = Pin(17,Pin.OUT)

#Esta función manejará la interrupción generada por el sensor PIR cuando se detecte movimiento.
def interrupcin_pir(pin):
    #Espera 100 milisegundos. Para evitar falsos positivos en la detección del sensor PIR.
    utime.sleep_ms(100)
    #Verifica si el valor del pin es alto, lo que indica que se detectó movimiento.
    if pin.value(): #esto mira si es igual a 1, es decir a TRUE
        print("Alarma! Movimiento detectado!")
        #Inicia un bucle que se repetirá 50 veces
        for i in range(50):
            #Alterna el estado del pin rojo, es decir, enciende o apaga el LED conectado a él en cada iteración del bucle
            rojo.toggle()
            # Alterna el estado del zumbador, lo que activará o desactivará el sonido en cada iteración del bucle.
            buzzer.toggle()
            #Espera 100 milisegundos antes de la próxima iteración del bucle.
            utime.sleep_ms(100)
#Configura una interrupción (irq) en el pin pir que se activa cuando su nivel cambia de bajo a alto (trigger=Pin.
#Cuando se detecta esta interrupción, se llamará a la función interrupción_pir.
pir.irq(trigger=Pin.IRQ_RISING, handler=interrupcin_pir) 


