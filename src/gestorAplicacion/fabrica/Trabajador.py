class Trabajador:
    def __init__(self, id_trabajador, nombre, horario):
        self.ID_TRABAJADOR = id_trabajador
        self.nombre = nombre
        self.horario = horario
        self.estado = "Disponible"

    def get_id_trabajador(self):
        return self.ID_TRABAJADOR

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_horario(self):
        return self.horario

    def set_horario(self, horario):
        self.horario = horario

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado
