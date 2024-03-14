import pyautogui, webbrowser
import time
from email.message import EmailMessage
import smtplib
import ssl
import os 
import re
import json
import sys

    
def programa():
    
    def validar_nombre():
        nombre =str(input("Ingrese su Nombre\n"))
        regextName = re.compile(r"^[A-ZÑa-zñáéíóúÁÉÍÓÚ'° ]+$")
        dataN1 =  regextName.search(nombre)
        os.system('cls')
        if dataN1 == None:
            print(f"Nombre Invalido: {nombre}")
            nombre2 = input("Vuelva a introducir un nombre correcto\n")
            dataN2 = regextName.search(nombre2)
            if dataN2 == None:
                print("Numero de intentos exedidos")
                sys.exit()   
            else:
                print("Nombre registrado exitosamente")
                return nombre2       
        else:
            print("Nombre registrado exitosamente")
            return nombre
         
    def validar_apellido():
        apellido = str(input ("Ingrese su Apellido\n"))
        regextLastName= re.compile(r"^[A-ZÑa-zñáéíóúÁÉÍÓÚ'° ]+$")
        dataA1 =  regextLastName.search(apellido)
        os.system('cls')    
        if dataA1 == None:
            print(f"Apellido Invalido: {apellido}")
            apellido2 = input("Vuelva a introducir un apellido correcto\n")
            dataA2 = regextLastName.search(apellido2)
            if dataA2 == None:
                print("Numero de intentos exedidos")
                sys.exit()   
            else:
                print("Apellido registrado exitosamente")
                return apellido2
        else:
            print("Apellido registrado exitosamente")
            return apellido
    
    def validar_fecha():
        date = input ("Ingrese su fecha de Nacimiento (dd/mm/yyyy)\n")
        regextDate =re.compile( r"^(?:(?:(?:0?[1-9]|1\d|2[0-8])[/](?:0?[1-9]|1[0-2])|(?:29|30)[/](?:0?[13-9]|1[0-2])|31[/](?:0?[13578]|1[02]))[/](?:0{2,3}[1-9]|0{1,2}[1-9]\d|0?[1-9]\d{2}|[1-9]\d{3})|29[/]0?2[/](?:\d{1,2}(?:0[48]|[2468][048]|[13579][26])|(?:0?[48]|[13579][26]|[2468][048])00))$")
        dataF1 =  regextDate.search(date)
        os.system('cls')
        if dataF1 == None:
            print(f"Fecha Invalida: {date}")
            fecha2 = input("Vuelva a introducir la fecha correcta\n")
            dataF2 = regextDate.search(fecha2)
            if dataF2 == None:
                print("Numero de intentos exedidos")
                sys.exit()   
            else:
                print("Fecha registrada exitosamente")
                return fecha2
        else:
            print("Fecha registrada exitosamente")
            return date
        
    def validar_pais():
        country = input ("Ingrese su Pais\n")
        regextCountry = re.compile(r"^[a-zA-ZñÑáéíóúÁÉÍÓÚ]+$")
        dataP1 =  regextCountry.search(country)
        os.system('cls') 
        if dataP1 == None:
            print(f"Pais Invalido: {country}")
            pais2 = input("Vuelva a introducir el pais correcto\n")
            dataP2 = regextCountry.search(pais2)
            if dataP2 == None:
                print("Numero de intentos exedidos")
                sys.exit()   
            else:
                print("Pais registrado exitosamente")
                return pais2
        else:
            print("Pais registrado exitosamente")
            return country
        
      
    def validar_correo():     
        email = input ("Ingrese su Correo\n")
        regextEmail = re.compile(r"^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$")
        dataC1 =  regextEmail.search(email)
        os.system('cls')
        if dataC1 == None:
            print(f"Correo Invalido: {email}")
            correo2 = input("Vuelva a introducir un correo valido\n")
            dataC2 = regextEmail.search(correo2)
            if dataC2 == None:
                print("Numero de intentos exedidos")
                sys.exit()   
            else:
                print("Correo registrado exitosamente")
                return correo2
        else:
            print("Correo registrado exitosamente")
            return email

    def validar_telefono():
        telefono = input ("Ingrese su Numero Telefonico incluya el +58 como el ejemplo (+58424, +58412,+58416)\n")
        regextNumber = re.compile(r"^(\(?(\+58|0058)\)?)?(\d{10})")
        dataT1 =  regextNumber.search(telefono)
        os.system('cls')
        if dataT1 == None:
            print(f"Telefono Invalido: {telefono}")
            telefono2 = input("Vuelva a introducir un Telefono correcto recuerde que incluya el +58 como el ejemplo (+58424, +58412,+58416) \n")
            dataT2 = regextNumber.search(telefono2)
            if dataT2 == None:
                print("Numero de intentos exedidos")
                sys.exit()   
            else:
                print("Telefono registrado exitosamente")
                return telefono2
        else:
            print("Telefono registrado exitosamente")
            return telefono
    menu = input(' Pulse 1 para registrarse\n pulse 2 para ver los usuarios registrados\n pulse 3 para modificar los datos de un usuario\n pulsa 4 para Borrar Base de Datos\n pulsa 5 para finalizar programa\n')
    if len(menu) == 0:
        print("Ingrese una opcion valida")
    opciones = int(menu)
    if opciones == 1:
        name = validar_nombre()
        apellido = validar_apellido()
        fechaN = validar_fecha()
        pais = validar_pais()
        correo = validar_correo()
        telefono = validar_telefono()
        if os.path.isfile('usuarios.txt'):
            f = open('usuarios.txt','a')
            data= {'Nombre': name, 'Apellido': apellido, 'Nacimiento': fechaN, 'Pais':pais, 'Correo':correo, 'Numero':telefono}
            f.write(f"\n{str(data)}")
            
        else:
            f = open('usuarios.txt','a')
            data = {'Nombre': name, 'Apellido': apellido, 'Nacimiento': fechaN, 'Pais':pais, 'Correo':correo, 'Numero':telefono}
            f.write(f"{str(data)}")
            
        f.close()
        
        input("Usuario registrado con exito")
        def envio_email(email_recibir,nombre, apellido):
            email_sender = 'rjalvarezprueba@gmail.com' 
            email_password = 'stllyyynwbuafxlv' 
            email_receiver = email_recibir 

            subject = "Esto es una prueba de Python"
            body = ("Hola " + nombre + ' ' +  apellido + ' Gracias por registrarte, Bienvenido') 

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context() 

            with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
                 smtp.login(email_sender, email_password)
                 smtp.sendmail(email_sender, email_receiver, em.as_string()) 

        envio_email(correo, name, apellido) 
        
        def enviar(telefono , nombre, apellido):
                webbrowser.open(f'https://web.whatsapp.com/send?phone={telefono}')
                time.sleep(5)
                pyautogui.typewrite(str((f'Bienvenido {nombre} {apellido}'))) 
                pyautogui.press('enter')
                os.system('cls')
                
        enviar(telefono, name, apellido)   
        programa()
    elif opciones == 2:
        print("usuarios registrados")
        f = open('usuarios.txt', 'r')
        print(f.read())
        f.close()
        programa()
    elif opciones == 3:
        print('Usuarios a Modificar')
        f = open('usuarios.txt', 'r')
        print(f.read())
        entrada = int(input('Ingrese que usuario quiere modificar en numero\n'))
        with open("usuarios.txt", "r") as f:
         entradas = f.readlines()
        data = json.loads(entradas[entrada - 1].replace("'", '"'))
        print(data)
        valor = int(input('1 Nombre,\n 2 Apellido,\n 3 Fecha de nacimiento,\n 4 Pais,\n 5 Correo,\n 6 Numero\n'))
        if valor == 1:
            name = validar_nombre()
            data['Nombre'] = name
        elif valor == 2:
            apellido = validar_apellido()
            data['Apellido'] = apellido
        elif valor == 3:
            fechaN = validar_fecha()
            data['Nacimiento'] = fechaN
        elif valor == 4:
            pais = validar_pais()
            data['Pais'] = pais
        elif valor == 5:
            correo = validar_correo()
            data['Correo'] = correo
        elif valor == 6:
            telefono = validar_telefono()
            data['Numero'] = telefono
        dataNueva = str(data)
        with open('usuarios.txt', 'r+') as f:
                entradas = f.readlines()
                entradas[entrada - 1] = f'{dataNueva}\n'
                f.seek(0)
                f.writelines(entradas)
                f.truncate()
        f.close()
        print('Cambios de Usuario Exitoso')
        programa()
    elif opciones == 4:
        if os.path.exists('usuarios.txt'):
           os.remove('usuarios.txt')
           print('Se elimino correctamente')
        else:
           print('El archivo no existe')
    elif opciones == 5:
        sys.exit()    



programa()