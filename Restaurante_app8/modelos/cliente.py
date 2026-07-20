class Cliente:
    def __init__(self, id_cliente: int, nombre: str, correo: str):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo

    @property
    def id_cliente(self) -> int:
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, nuevo_id: int):
        if nuevo_id <= 0:
            raise ValueError("El ID del cliente debe ser un número entero positivo.")
        self.__id_cliente = nuevo_id

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre del cliente no puede estar vacío.")
        self.__nombre = nuevo_nombre.strip()

    @property
    def correo(self) -> str:
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo: str):
        if not nuevo_correo.strip():
            raise ValueError("El correo electrónico no puede estar vacío.")
        self.__correo = nuevo_correo.strip()

    def mostrar_informacion(self):
        print(f"ID Cliente: {self.id_cliente} | Nombre: {self.nombre} | Correo: {self.correo}")