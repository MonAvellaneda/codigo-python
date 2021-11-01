menu1 = """

BIENVENIDO AL BANCO DE OPORTUNIDADES 💰💰💰

1 - Cosas 
2 - Dinero 
3 - Habilidades
4 - Tiempo

Elige una opción de lo que tienes para ofrecer: """

opcion1 = int(input(menu1))

menu2 = """

BIENVENIDO AL BANCO DE OPORTUNIDADES 💰💰💰

1 - Cosas 
2 - Dinero 
3 - Habilidades
4 - Tiempo

Elige una opción de lo que necesitas: """

opcion2 = int(input(menu2))

if opcion1 & opcion2 == 1:
    print("Mándame una fotografía a mon@gmail.com de lo que tienes y explícanos lo que necesitas")
    
elif opcion1 == 1 & opcion2 == 2: 
    print("Perfecto, mándanos una fotografía y te hacemos un Buzum")

elif opcion1 == 3 & opcion2 == 2: 
    print("Explicanos tus habilidades por telegram")

elif opcion1 == 4 & opcion2 ==2: 
    service_time = float(input("¿De cuántas horas dispones?: "))
    value_time = 10
    value_time = round(value_time, 2)
    value_service = str(service_time * value_time)
    print(str(("El valor del servicio es de " + value_service + " euros")))

else:
    print("Ingresa una opción correcta, por favor")

