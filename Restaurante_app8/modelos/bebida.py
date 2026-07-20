from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str):
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano = tamano

    @property
    def tamano(self) -> str:
        return self.__tamano

    @tamano.setter
    def tamano(self, nuevo_tamano: str):
        if not nuevo_tamano.strip():
            raise ValueError("El tamaño de la bebida no puede estar vacío.")
        self.__tamano = nuevo_tamano.strip()

    def mostrar_informacion(self):
        print(f"[Bebida] Código: {self.codigo} | Nombre: {self.nombre} | Categoría: {self.categoria} | Tamaño: {self.tamano} | Precio: ${self.precio:.2f}")