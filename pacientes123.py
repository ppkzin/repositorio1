pacientes = {
    "H001": ["Laura Pérez", "Pediatria", "11-03-2024"],
    "H002": ["Carlos Díaz", "Traumatologia", "22-01-2024"],
    "H003": ["Daniela Soto", "Neurologia", "05-07-2023"],
    "H004": ["Matías Rojas", "Pediatria", "14-03-2024"],
    "H005": ["Fernanda Silva", "Cardiologia", "03-10-2023"],
    "H006": ["José Vargas", "Traumatologia", "28-03-2024"],
    "H007": ["Ana Beltrán", "Neurologia", "19-09-2023"],
    "H008": ["María Contreras", "Cardiologia", "12-01-2024"],
}
while True:
    print("MENÚ HOSPITAL")
    print("1-Pacientes por especialidad")
    print("2- Porcentaje de ingresos por mes")
    print("3-Eliminar paciente")
    print("4-Salir")
    
    OPCIONES = input("Selecciona una opción: ")
    
    if OPCIONES == "1":
        especialidad = input("Ingrese la especialidad para listar los pacientes: ")
        
        for paciente in pacientes.values():
            if(especialidad.lower() == paciente[1].lower()):
                print(f"{paciente[0]}")
                
    elif(OPCIONES =="2"):
        while True:
            try:
                mes = int(input("Porcentaje de pacientes por mes: "))
            except ValueError:
                print("El mes debe ingresarse como numero")
            else:
                if(mes>=1 and mes<=12):
                    break
        contador = 0
        for paciente in pacientes:
            
            mes_actual = int(paciente)
            if(int(paciente[2].split("-")[1])==mes):
                contador = contador + 1
        porcentaje = contador/len(pacientes)*100
        print(f"El porcentaje de pacientes del mes fueron: {porcentaje}")
        