registros = ["000000000", "000101010", "001010100", "010001000", "010100010"]
w = "11100"
print("Cadena de entrada:", w)
estado = "00"    # estado inicial 
finales = ["10"] # estados finales

# Codificación de símbolos 
simbolos = {"0": "00", "1": "01"} 
blanco = "10"

# Cinta
cinta = []
for i in w:
    cinta.append(simbolos[i])
cinta.append(blanco) #['00', '00', '01', '01', '00', '00, '10']

cabezal = 0  # posicion del cabezal
pasos = 0

while True:
    simb_leido = cinta[cabezal]

    cadena = "".join(cinta[:cabezal]) + "*" + "".join(cinta[cabezal + 1:]) # reemplaza el símbolo bajo el cabezal con un *
    print(cadena + "$" + estado + simb_leido + "#" + "#".join(registros), end=" ")

    # Buscar el registro que empieza con estado + simbolo leido
    registro = None
    for r in registros:
        if r.startswith(estado + simb_leido): #startswith() devuelve True si la cadena comienza con el prefijo especificado
            registro = r

    if registro is None:
        print("-> no hay registro para continuar")
        break
    print("-> uso", registro)

    estado_nuevo = registro[4:6] #ej: 0001 01 010 -> estado_nuevo = 01
    escribe = registro[6:8] #ej: 000101 01 0 -> escribe = 01
    mov = registro[8] #ej: 00010101 0 -> muevo hacia = 0

    cinta[cabezal] = escribe # simbolo a escribir
    if mov == "0":  # 0 = R
        cabezal = cabezal + 1
        if cabezal == len(cinta):
            cinta.append(blanco) #agrego blanco al final de la cinta
    else: # 1 = L
        if cabezal == 0:
            cinta.insert(0, blanco) #agrego blanco al inicio de la cinta
        else:
            cabezal = cabezal - 1 #retrocedo el cabezal a la izquierda
    estado = estado_nuevo  # actualizo el estado
    pasos += 1

if estado in finales: # si llego a un estado final, acepto la cadena, sino rechazo
    print("ACEPTA")
    print("Número de pasos:", pasos)
else:
    print("RECHAZA")
    print("Número de pasos:", pasos)