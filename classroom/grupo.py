from classroom.asignatura import Asignatura


class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        if estudiantes is not None:
            self.listadoAlumnos = estudiantes
        else:
            self.listadoAlumnos = []

        self.grupo = grupo

        if asignaturas is not None:
            self._asignaturas = asignaturas
        else:
            self._asignaturas = []

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is not None:
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos = self.listadoAlumnos + [alumno]

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        return "Grupo de estudiantes: " + self.grupo