from gtts import gTTS
from playsound import playsound
# requisitos 
# pip install gtts y playsound


# EJERCICIO CON TIEMPO

import time
import msvcrt
from os import system




# Variables iniciales
saldo_tarjeta = 0  # Saldo inicial de la tarjeta en pesos
valor_pasaje = 2900   # Valor de un pasaje en Transmilenio en pesos

# se agrefga el texto
text = "¡Bienvenido al sistema de simulación de tarjeta Transmilenio!"
# Mensaje de bienvenida
print("\n--------------------------------------------------------------")
print(text)
print("--------------------------------------------------------------")
# se cre un objeto gtts 
tts = gTTS(text=text, lang='es', )
# se guarda el archivo de audio 
tts.save("Bienvenida.mp3")
# se reproduce con la opcion de playsound 
playsound("bienvenida.mp3")


# --------------------------------voz 2---
INTRO = "Por favor selecciona una opción"
tts=gTTS(text=INTRO, lang= 'es')
tts.save("INTRO.mp3")
# ---------------------------------------
# ---------------------------voz 3-------
interaccion= "Presiona cualquier tecla para continuar..."
tts = gTTS(text= interaccion, lang= 'es')
tts.save("interaccion.mp3")
# ---------------------------------voz 4

erro ="Por favor ingresa un valor válido para recargar."
tts =gTTS(text= erro, lang='es')
tts.save("erro.mp3")
# -----------------------------------voz 5-
aviso = "RECARGUE SU TARJETA PARA EL PRÓXIMO TRANSPORTE "
tts =gTTS(text=aviso, lang='es')
tts.save("aviso.mp3")
# ------------------------------voz 6
fin = "Gracias por usar el sistema de Transporte de Transmilenio. ¡Hasta pronto!"
tts = gTTS(text=fin, lang='es')
tts.save("fin.mp3")
# ------------------------------------voz 7
money = "       T R A S A C C I O N        R E A L I Z A D A           "
tts =gTTS(text=money, lang='es')
tts.save("money.mp3")
# ------------------------------------voz 8-
anuncio ="Opción no válida. Por favor elige una opción entre 1 y 5."
tts = gTTS(text=anuncio, lang='es')
tts.save("anuncio.mp3")
# -----------------------------------------
tiempo= "Tiempo de gracia para el transbordo 30 segundos..."
tts= gTTS(text=tiempo, lang='es')
tts.save("tiempo.mp3")
# ----------------------------------------
carga = "Por favor ingresa un valor válido para recargar."
tts =gTTS(text=carga,lang='es')
tts.save("carga.mp3")
# ---------------------------------
monto ="Recargue la tarjeta"
tts= gTTS(text=monto, lang='es')
tts.save("monto.mp3")
# -------------------------------
agradecimiento = "                  GRACIAS             "
tts= gTTS(text=agradecimiento, lang='es')
tts.save("agradecimiento.mp3")
# --------------------------
# Bucle principal
while True:
    # texto de seleccion
    print("\n---------------------------------")
    print(INTRO)
    print("---------------------------------")
    playsound("INTRO.mp3")
   

    print("1. Consultar saldo de la tarjeta")
    print("2. Recargar tarjeta")
    print("3. Ingreso al bus")
    print("4. Transbordo")
    print("5. Salir del sistema")
    print("-----------------------------------")
    
    # Entrada del usuario
    opcion = input("Elige una opción (1, 2, 3, 4, 5): ")
    system("cls") #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    
    # Consultar saldo
    match opcion:
        case"1":
            print(f"Tu saldo actual es de: ${saldo_tarjeta} COP")
            
            print(interaccion)
            playsound("interaccion.mp3")
            msvcrt.getch()
            system("cls")
            
        
    # Recargar tarjeta
        case "2":
           
            recarga = int(input("¿Cuánto deseas recargar? (en pesos colombianos) "))
            system("cls")
            
            if recarga > 0:
                saldo_tarjeta += recarga
                print("\n--------------------------------------------------------------------")
                print(f"Has recargado ${recarga} COP. Tu nuevo saldo es: ${saldo_tarjeta} COP")
                print("--------------------------------------------------------------------")
                print(interaccion)
                playsound("interaccion.mp3")
                msvcrt.getch()
                system("cls")
            
        
            else:
                print("\n----------------------------------------------")
                print(carga)
                playsound("carga.mp3")
                print("\n----------------------------------------------")
                system("cls")
        
    
    # Simular ingreso al bus
        case"3":
            if saldo_tarjeta >= valor_pasaje:
                saldo_tarjeta -= valor_pasaje
            
                print("\n---------------")
                print(agradecimiento)
                playsound("agradecimiento.mp3")
                print("-----------------")
                
            
                print("\n----------------------------------------------------------")
                print(f"Has ingresado al bus. Se ha descontado ${valor_pasaje} COP.")
                print(f"Tu saldo actual es: ${saldo_tarjeta} COP")
                print("----------------------------------------------------------")
            
                print(interaccion)
                playsound("interaccion.mp3")
                msvcrt.getch()
                system("cls")
            

            elif saldo_tarjeta >= -2000:
                saldo_tarjeta -= valor_pasaje
                print(f"Recargue la tarjeta ${saldo_tarjeta} COP")
                print("\n------------------------------------------------------------")
                print(agradecimiento)
                print("------------------------------------------------------------")
                playsound("agradecimiento.mp3")
            

                print(f"Has ingresado al bus. Se ha descontado ${valor_pasaje} COP.")
                print(f"Tu saldo actual es: ${saldo_tarjeta} COP")
                print(aviso)
                print("--------------------------------------------------------")
                playsound("aviso.mp3")
                
                            
                print(interaccion)
                playsound("interaccion.mp3")
                
                msvcrt.getch()
                system("cls")
            else:
                print("\n----------------------------------------------------------")
                print(erro)
                print("------------------------------------------------------------")
                playsound("error.mp3")
            
                print(interaccion)
                playsound("interaccion.mp3")
                msvcrt.getch()
                system("cls")
    
        case"4":
            inicio = time.time()
            print(tiempo)
            playsound("tiempo.mp3")
            msvcrt.getch()
            system("cls")
         
            transbordos = (time.time() - inicio)
            print(f"\nHan transcurrido {int(transbordos)} segundos.")
            print("------------------------------------------------")

         

            if transbordos <= 30 and saldo_tarjeta < -4000:
                print("\n------------------------------------------------------------")
                print(money)
                print("\n--------------------------------------------------------------")
                playsound("money.mp3")
             
                print("Has ingresado nuevamente al bus. Transacción realizada $ 0 COP")
                print(f"Tu saldo actual es: ${saldo_tarjeta} COP")
                print("--------------------------------------------------------------")
                
                if saldo_tarjeta < 0:
                    print(aviso)
                    print("------------------------------------------------------------")
                    playsound("aviso.mp3")
                  
                    print(interaccion)
                    playsound("interaccion.mp3")
                    msvcrt.getch()
                    system("cls")


                elif transbordos > 30 and saldo_tarjeta <= 0:
                    print("\n-------------------------------------------")
                    print("Recargue la tarjeta")
                    print(f"Tu saldo actual es de: ${saldo_tarjeta} COP")
                    print("\n-------------------------------------------")

                
                    print(interaccion)
                    playsound("interacion.mp3")
                    msvcrt.getch()
                    system("cls")
            
                elif transbordos < 30 and saldo_tarjeta == 0:
                    print("\n-------------------------------------------")
                    print(monto)
                    playsound("monto.mp3")
                    print(f"Tu saldo actual es de: ${saldo_tarjeta} COP")
                    print("\n-------------------------------------------")

                
                    print(interaccion)
                    playsound("interaccion.mp3")
                    msvcrt.getch()
                    system("cls")   
            
            
                elif transbordos > 30 and saldo_tarjeta > 0:
                    saldo_tarjeta -= valor_pasaje
                
                    print("\n------------------------------------------------------------")
                    print(agradecimiento)
                    print("------------------------------------------------------------")
                    playsound("agradecimiento.mp3")
            

                    print(f"Has ingresado al bus. Se ha descontado ${valor_pasaje} COP.")
                    print(f"Tu saldo actual es: ${saldo_tarjeta} COP")
                            
                    print(interaccion)
                    playsound("interaccion.mp3")
                    msvcrt.getch()
                    system("cls")
        
    
    # Salir del sistema
        case"5":
            print("\n------------------------------------------------------------------------")
            print(fin)
            print("--------------------------------------------------------------------------")
            playsound("fin.mp3")
            break
    
    # Opción no válida
        case _:
            print("\n----------------------------------------------------------")
            print(anuncio)
            print("----------------------------------------------------------")
            playsound("anuncio.mp3")
        
            print(interaccion)
            playsound("interaccion.mp3")
            msvcrt.getch()
            system("cls")
        

            
        
        
    