from pystyle import Colors, Colorate
titulo = fr"""
██ ███    ███  ██████ 
██ ████  ████ ██      
██ ██ ████ ██ ██      
██ ██  ██  ██ ██      
██ ██      ██  ██████ 
                      
"""
print(Colorate.Vertical(Colors.red_to_purple,titulo))

print(Colorate.Vertical(Colors.purple_to_blue, """
┌══════════════════════════════════════════════════┐
█ Sistema preferido [ 1 ] Imperial [ 2 ] Métrico   █
└══════════════════════════════════════════════════┘""",3))

sistemaelegido = int(input(Colorate.Vertical(Colors.purple_to_blue, "└═>>> ")))

sistema = 0
valordefaultpeso = 0
valordefaultestatura = 0

match sistemaelegido:
    case 1:
        sistema = "imperial"
        # PESO
        print(Colorate.Vertical(Colors.purple_to_blue, f"""
┌═══════════════════════════════════════┐
█ Ingrese su peso en sistema: Imperial  █
└═══════════════════════════════════════┘""",3))
        pesolb = 0
        try:
            medidas_pesoLB = float(input(Colorate.Vertical(Colors.purple_to_blue, "└═>>> ")))
            pesolb = medidas_pesoLB * 0.453592
            pesocalculadoaKG = pesolb
        except ValueError:
            print("Simbolo no permitido")
            exit()
        # ESTATURA
        
        print(Colorate.Vertical(Colors.purple_to_blue, f"""
┌═══════════════════════════════════════════┐
█ Ingrese su estatura en sistema: Imperial  █
└═══════════════════════════════════════════┘""",3))
        estaturaFT = 0
        try:
            medidas_estaturaFT = float(input(Colorate.Vertical(Colors.purple_to_blue, "└═>>> ")))
            estaturaFT = medidas_estaturaFT * 0.3048
            estatura_calculada=estaturaFT
        except ValueError:
            print('Simbolo no permitido')
            exit()

        calcular_imc = pesocalculadoaKG / (estatura_calculada**2)
        print(Colorate.Vertical(Colors.purple_to_blue, f"""
┌══════════════════════════════════┐
█ Tu IMC es: {calcular_imc}    █ 
└══════════════════════════════════┘""",3))

    
    # SISTEMA METRICO
    
    
    
    case 2:
        sistema = "metrico"
        print(Colorate.Vertical(Colors.purple_to_blue, f"""
┌═════════════════════════════════════┐
█ Ingrese su peso en sistema: Metrico █
└═════════════════════════════════════┘""",3))
        pesokg = 0
        try:
            medidas_pesoKG = float(input(Colorate.Vertical(Colors.purple_to_blue, "└═>>> ")))
            pesokg = medidas_pesoKG
        except ValueError:
            print("Simbolo no permitido")
            exit()
        # ESTATURA
        
        print(Colorate.Vertical(Colors.purple_to_blue, f"""
┌═══════════════════════════════════════════┐
█ Ingrese su estatura en sistema: Metrico   █
└═══════════════════════════════════════════┘""",3))
        estaturaMetro = 0
        try:
            medidas_estaturaM = float(input(Colorate.Vertical(Colors.purple_to_blue, "└═>>> ")))
            estaturaMetro = medidas_estaturaM
        except ValueError:
              print('Simbolo no permitido')
              exit()

        calcular_imc = pesokg / (estaturaMetro**2)
        print(Colorate.Vertical(Colors.purple_to_blue, f"""
┌══════════════════════════════════┐
█ Tu IMC es: {calcular_imc}     █ 
└══════════════════════════════════┘""",3))
    case _:
        print(fr"Lo sentimos, no se ha encontrado esa opcion")