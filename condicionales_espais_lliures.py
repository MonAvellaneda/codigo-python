places_available_outside = int(input("¿Cuántas mesas disponibles tienes en la terraza? "))

if places_available_outside >= 50: 
    print("genial,podeis irnos todos juntos de tapeo")
else:
    places_available_inside = int(input("¿Cuántas mesas disponibles tienes en el interior? "))

    if places_available_inside >= 50: 
        print("No nos gusta tanto estar dentro pero guárdanos sitio que vamos")

    else: 
        print("Tenemos que buscar otro sitio, hoy está demasiado lleno para los que somos")
