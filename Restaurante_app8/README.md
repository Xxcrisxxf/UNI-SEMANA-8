Nombre : CRISTIAN JAIR BRAVO CHIMBORAZO
Este sistema es una aplicación de consola modular desarrollada en Python para la gestión interna de un restaurante. Permite administrar de forma eficiente colecciones de productos tradicionales, bebidas específicas y clientes mediante una interfaz interactiva de menús. El diseño pone especial énfasis en el control de duplicados , anotaciones de tipos consistentes y la protección de datos mediante encapsulamiento estricto.
capa de Modelos 
Producto:Define los atributos básicos de cualquier artículo comercial del restaurante (código, nombre, categoría y precio). Aplica validaciones mediante propiedades para impedir campos vacíos o precios negativos.

Bebida: Extiende a la clase Producto, especializándose en los líquidos del menú al incorporar el atributo único de tamaño o presentación.

Cliente: Entidad independiente encargada de modelar la información de los usuarios (ID entero positivo, nombre y correo), aislando sus datos de las lógicas comerciales de los artículos.
Capa de Servicios 

Restaurante: Centraliza la lógica operativa y de almacenamiento del negocio. Gestiona de manera unificada los arreglos de productos y clientes, encargándose de validar que no existan códigos ni identificaciones duplicadas antes de proceder a su inserción.
Relación entre Producto y Bebida
La relación entre ambas clases se fundamenta en el concepto de Herencia.La clase Bebida hereda directamente de Producto, lo que significa que una bebida es un producto dentro del dominio del restaurante. Esto permite reutilizar el constructor del padre con super().__init__() y los métodos existentes.
Principios SOLID Aplicados
Principio de Responsabilidad Única: Cada componente tiene una única razón para cambiar. Los modelos solo validan y representan datos, el servicio Restaurante manipula exclusivamente las colecciones del negocio, y main.py se limita a la captura de datos con input() y la visualización de la interfaz.

Principio de Abierto/Cerrado (OCP): El sistema está abierto a la extensión pero cerrado a la modificación. Si en el futuro se requiere añadir un nuevo tipo de artículo (por ejemplo, PlatoFuerte), se puede crear una nueva subclase que herede de Producto sin alterar las colecciones ni el comportamiento lógico del servicio Restaurante.

Principio de Sustitución de Liskov (LSP): La subclase Bebida puede sustituir por completo a su clase base Producto en cualquier sección del programa sin alterar la integridad del sistema. Esto se evidencia al almacenar tanto productos como bebidas dentro del mismo arreglo unificado (self.productos) y procesarlos sin errores.

El archivo main.py actúa como el punto de entrada del programa al implementar una interfaz interactiva en consola basada en un bucle continuo , coordinando las operaciones del restaurante mediante funciones específicas conectadas al servicio Restaurante. El sistema despliega un menú estructurado con seis opciones numéricas obligatorias: las opciones de la 1 a la 3 permiten recolectar los datos controlados para el alta de productos generales, bebidas y clientes respectivamente; las opciones 4 y 5 ejecutan el listado dinámico delegando de forma polimórfica la impresión visual mediante el método común mostrar_informacion()

El diseño de software estructurado y mantenible es un pilar fundamental en la ingeniería de sistemas. Desarrollar soluciones basadas en la cohesión, el bajo acoplamiento y las buenas prácticas de la Programación Orientada a Objetos previene que el código se convierta en una estructura frágil ante el crecimiento del negocio.

Al aislar las responsabilidades y proteger los datos a través del encapsulamiento, garantizamos que la detección de fallos sea inmediata y que los cambios en un módulo no desaten efectos secundarios inesperados en el resto del software.
