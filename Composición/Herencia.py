# Clase Persona

class Persona:
    
    # método constructor
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__Edad = 0

    def getNombre(self):
        return self.__Nombre
    
    def setNombre(self, nombre):
        self.__Nombre = nombre

    def getApellidos(self):
        return self.__Apellidos
    
    def setApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def getEdad(self):
        return self.__Edad
    
    def setEdad(self, edad):
        self.__Edad = edad

    # método para mostrar los datos de una persona
    def MostrarPersona(self):
        print("Nombre: " + self.__Nombre)
        print("Apellidos: " + self.__Apellidos)
        print("Edad: " + str(self.__Edad))

class Alumno(Persona):
    def __init__(self):
        self.__Curso = ""
        self.__Asignaturas = ""
    
    def getCurso(self):
        return self.__Curso
    
    def setCurso(self, curso):
        self.__Curso = curso

    def getAsignaturas(self):
        return self.__Asignaturas
    
    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def mostrarAlumno(self):
        print("Alumno")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tCurso: ", self.__Curso)
        print("\tMatrículas: ", self.__Asignaturas)


class Profesor(Persona):
    def __init__(self):
        self.__Departamento = ""
        self.__Asignaturas = ""

    def getDepartamento(self):
        return self.__Departamento
    
    def setDepartamento(self, departamento):
        self.__Departamento = departamento

    def getAsignaturas(self):
        return self.__Asignaturas
    
    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def mostrarProfesor(self):
        print("Profesor")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tDepartamento: ", self.__Departamento)
        print("\tMatrículas: ", self.__Asignaturas)
# metodo principal
def main():
    # ALUMNO
    alumno = Alumno()
    alumno.setNombre("Andres")
    alumno.setApellidos("Pinilla Arciniegas")
    alumno.setEdad(15)
    alumno.setCurso("Bachillerato")
    alumno.setAsignaturas(["física", "sociales", "castellano"])
    alumno.mostrarAlumno()
    # PROFESOR
    profesor = Profesor()
    profesor.setNombre("Nestor")
    profesor.setApellidos("Paez")
    profesor.setEdad(33)
    profesor.setDepartamento("Santander")
    profesor.setAsignaturas(["Especialidad en sistemas", "Etica", "Valores"])
    profesor.mostrarProfesor()

if __name__ == "__main__":
    main()