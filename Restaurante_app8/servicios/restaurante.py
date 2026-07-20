from modelos.producto import Producto
from modelos.cliente import Cliente
from typing import List

class Restaurante:
    def __init__(self):
        self.productos: List[Producto] = []
        self.clientes: List[Cliente] = []

    def agregar_producto(self, producto: Producto) -> bool:
        for p in self.productos:
            if p.codigo == producto.codigo:
                return False
        self.productos.append(producto)
        return True

    def listar_productos(self) -> List[Producto]:
        return self.productos

    def agregar_cliente(self, cliente: Cliente) -> bool:
        for c in self.clientes:
            if c.id_cliente == cliente.id_cliente:
                return False
        self.clientes.append(cliente)
        return True

    def listar_clientes(self) -> List[Cliente]:
        return self.clientes