import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Crear la tabla producto
cursor.execute('''
    CREATE TABLE IF NOT EXISTS producto (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        category TEXT NOT NULL
    )
''')

# Crear la tabla comentario
cursor.execute('''
    CREATE TABLE IF NOT EXISTS comentario (
        id INTEGER PRIMARY KEY,
        comentario TEXT NOT NULL,
        id_producto INTEGER,
        FOREIGN KEY (id_producto) REFERENCES producto (id)
    )
''')

# Datos de ejemplo para la tabla producto
productos = [
    # Camisas
    (1, "Camisa Cuadros Blanca", 19.99, "Camisa"),
    (2, "Camisa de Lino Azul", 25.99, "Camisa"),
    (3, "Camisa Manga Larga Negra", 22.99, "Camisa"),

    # Pantalones
    (4, "Pantalón Mezclilla", 29.99, "Pantalon"),
    (5, "Pantalón de Vestir Negro", 35.99, "Pantalon"),
    (6, "Pantalón Cargo Verde", 31.99, "Pantalon"),

    # Chamarras
    (7, "Chamarra Verde Niño", 49.99, "Chamarra"),
    (8, "Chamarra de Cuero", 89.99, "Chamarra"),
    (9, "Chamarra Impermeable", 59.99, "Chamarra"),

    # Faldas
    (10, "Falda de Algodón Roja", 24.99, "Falda"),
    (11, "Falda Larga Floral", 29.99, "Falda"),
    (12, "Minifalda de Jean", 27.99, "Falda"),

    # Sudaderas
    (13, "Sudadera con Capucha Gris", 34.99, "Sudadera"),
    (14, "Sudadera Azul Marino", 32.99, "Sudadera"),
    (15, "Sudadera con Cremallera", 37.99, "Sudadera"),

    # Camisetas
    (16, "Camiseta Estampada", 15.99, "Camiseta"),
    (17, "Camiseta Básica Blanca", 9.99, "Camiseta"),
    (18, "Camiseta de Rayas", 12.99, "Camiseta"),

    # Blusas
    (19, "Blusa Seda Azul", 39.99, "Blusa"),
    (20, "Blusa Cuello V", 34.99, "Blusa"),
    (21, "Blusa Estampado Floral", 29.99, "Blusa"),

    # Accesorios
    (25, "Gorro de Lana", 12.99, "Accesorio"),
    (26, "Bufanda de Cashmere", 19.99, "Accesorio"),
    (27, "Cinturón de Cuero", 17.99, "Accesorio"),

    # Calzado
    (28, "Zapatillas Deportivas", 89.99, "Calzado"),
    (29, "Botas de Cuero", 95.99, "Calzado"),
    (30, "Sandalias Planas", 49.99, "Calzado")
]


# Insertar datos en la tabla producto
cursor.executemany('INSERT INTO producto VALUES (?, ?, ?, ?)', productos)

# Datos de ejemplo para la tabla comentario
comentarios = [
    # Comentarios para "Camisa Cuadros Blanca"
    (1, "Amo el patrón, muy a la moda.", 1),
    (2, "El material se siente genial, pero es un poco ajustada.", 1),
    (3, "Excelente para uso diario, se lava bien.", 1),
    (4, "Llegó con un pequeño desgarro en la manga.", 1),
    (5, "El color es perfecto y justo como se muestra en la imagen.", 1),

    # Comentarios para "Camisa de Lino Azul"
    (6, "Ideal para el verano, muy fresca.", 2),
    (7, "La camisa se arruga fácilmente.", 2),
    (8, "Mejor de lo que esperaba, volveré a comprar en otros colores.", 2),
    (9, "El corte no es muy favorecedor.", 2),
    (10, "El lino es de buena calidad, pero requiere cuidado al lavar.", 2),

    # Comentarios para "Camisa Manga Larga Negra"
    (11, "Perfecta para mi trabajo de oficina.", 3),
    (12, "Se encoge un poco después del primer lavado.", 3),
    (13, "Elegante y cómoda, la manga tiene un largo ideal.", 3),
    (14, "Los botones son un poco endebles.", 3),
    (15, "Una prenda básica para cualquier armario.", 3),

    # Comentarios para "Pantalón Mezclilla"
    (16, "Gran ajuste, el color es resistente.", 4),
    (17, "Un poco rígidos al principio, pero se suavizan con el uso.", 4),
    (18, "No son tan elásticos como esperaba.", 4),
    (19, "Perfectos para el uso diario, robustos y cómodos.", 4),
    (20, "La talla es más grande de lo esperado.", 4),

    # Comentarios para "Pantalón de Vestir Negro"
    (21, "Elegantes y con un buen corte.", 5),
    (22, "La tela se arruga fácilmente, requiere planchado constante.", 5),
    (23, "Muy cómodos, pero la tela es un poco delgada.", 5),
    (24, "Perfectos para eventos formales o trabajo.", 5),
    (25, "La calidad no justifica el precio.", 5),

    # Comentarios para "Pantalón Cargo Verde"
    (26, "Muchos bolsillos útiles, ideal para actividades al aire libre.", 6),
    (27, "El color se desvaneció después de algunos lavados.", 6),
    (28, "Cómodos y prácticos.", 6),
    (29, "La tela es más gruesa de lo que esperaba.", 6),
    (30, "Buen ajuste, pero la cintura es un poco estrecha.", 6),

    # Comentarios para "Chamarra Verde Niño"
    (31, "A mi hijo le encanta, es cálida y resistente.", 7),
    (32, "Buena chamarra, pero no es tan impermeable como esperaba.", 7),
    (33, "El color es vibrante y no se desvanece con el lavado.", 7),
    (34, "El tamaño es un poco más grande de lo normal.", 7),
    (35, "Excelente para el clima frío.", 7),

    # Comentarios para "Chamarra de Cuero"
    (36, "Elegante y de alta calidad.", 8),
    (37, "El cuero es rígido y necesita tiempo para suavizarse.", 8),
    (38, "Perfecta para salidas nocturnas.", 8),
    (39, "Más pesada de lo que esperaba.", 8),
    (40, "El precio es alto, pero vale la pena por la calidad.", 8),

    # Comentarios para "Chamarra Impermeable"
    (41, "Mantiene seco en la lluvia ligera, pero no en tormentas fuertes.", 9),
    (42, "Ligera y fácil de empacar.", 9),
    (43, "Las costuras internas podrían mejorar.", 9),
    (44, "Buena relación calidad-precio.", 9),
    (45, "La capucha podría ser más grande.", 9),

    # Comentarios para "Falda de Algodón Roja"
    (46, "Color brillante y hermoso, justo como en la foto.", 10),
    (47, "La tela es un poco transparente.", 10),
    (48, "Cómoda y perfecta para el verano.", 10),
    (49, "La cintura elástica es muy ajustada.", 10),
    (50, "Fácil de combinar con diferentes tops.", 10),

    # Comentarios para "Falda Larga Floral"
    (51, "El estampado floral es encantador.", 11),
    (52, "Más larga de lo que esperaba.", 11),
    (53, "Ideal para salidas casuales o la playa.", 11),
    (54, "La calidad del material podría ser mejor.", 11),
    (55, "Muy cómoda y fluida.", 11),

    # Comentarios para "Minifalda de Jean"
    (56, "Estilosa y versátil, buena para diferentes ocasiones.", 12),
    (57, "La talla es más pequeña de lo esperado.", 12),
    (58, "La tela es durable y de buena calidad.", 12),
    (59, "Un poco corta para mi gusto.", 12),
    (60, "Perfecta combinación con camisetas o blusas.", 12),

    # Comentarios para "Sudadera con Capucha Gris"
    (61, "Muy suave por dentro, calienta bien.", 13),
    (62, "La capucha es un poco pequeña.", 13),
    (63, "Ideal para entrenar o relajarse en casa.", 13),
    (64, "Se encogió un poco después del lavado.", 13),
    (65, "Buena calidad por el precio.", 13),

    # Comentarios para "Sudadera Azul Marino"
    (66, "Color sólido incluso después de varios lavados.", 14),
    (67, "La costura del hombro se deshizo un poco.", 14),
    (68, "Cómoda y cálida para el clima frío.", 14),
    (69, "Un poco grande en la zona de los brazos.", 14),
    (70, "Buena compra para el uso diario.", 14),

    # Comentarios para "Sudadera con Cremallera"
    (71, "La cremallera es suave y de buena calidad.", 15),
    (72, "No es tan gruesa como esperaba, pero aún así calienta.", 15),
    (73, "Perfecta para capas en el invierno.", 15),
    (74, "La talla es precisa según la guía.", 15),
    (75, "Un básico necesario para el armario.", 15),

    # Comentarios para "Camiseta Estampada"
    (76, "El diseño es único y llamativo.", 16),
    (77, "El material es un poco delgado.", 16),
    (78, "Gran ajuste y confortable.", 16),
    (79, "El estampado no se desvanece con el lavado.", 16),
    (80, "Ideal para el verano.", 16),

    # Comentarios para "Camiseta Básica Blanca"
    (81, "Una prenda esencial, se ajusta bien.", 17),
    (82, "Se vuelve un poco transparente después de algunos lavados.", 17),
    (83, "Buena relación calidad-precio.", 17),
    (84, "La tela se siente suave contra la piel.", 17),
    (85, "Podría ser un poco más gruesa.", 17),

    # Comentarios para "Camiseta de Rayas"
    (86, "Estilosa y cómoda para uso diario.", 18),
    (87, "La tela no es tan suave como esperaba.", 18),
    (88, "Se ajusta bien y el diseño es atractivo.", 18),
    (89, "Ideal para combinar con jeans o pantalones cortos.", 18),
    (90, "Se mantiene bien después de varios lavados.", 18),

    # Comentarios para "Blusa Seda Azul"
    (91, "Elegante y perfecta para salidas nocturnas.", 19),
    (92, "Requiere cuidado al lavar debido al material delicado.", 19),
    (93, "La seda es de buena calidad y se siente lujosa.", 19),
    (94, "Un poco más brillante de lo que esperaba.", 19),
    (95, "Cómoda y ligera, ideal para el verano.", 19),

    # Comentarios para "Blusa Cuello V"
    (96, "El cuello en V es un buen detalle, muy favorecedor.", 20),
    (97, "La tela se arruga fácilmente.", 20),
    (98, "Perfecta para el trabajo o una cena casual.", 20),
    (99, "Se adapta bien a diferentes tipos de cuerpo.", 20),
    (100, "Podría tener una mejor calidad de tela.", 20),

    # Comentarios para "Blusa Estampado Floral"
    (101, "El estampado es hermoso y femenino.", 21),
    (102, "Un poco grande en la zona de los hombros.", 21),
    (103, "Fresca y vibrante, ideal para la primavera.", 21),
    (104, "El material es un poco transparente.", 21),
    (105, "Gran adición a mi armario para el día a día.", 21),

    # Comentarios para "Gorro de Lana"
    (106, "Calienta bien y es suave.", 25),
    (107, "El tamaño es un poco pequeño.", 25),
    (108, "Buena calidad de lana, no pica.", 25),
    (109, "El color es un poco diferente al de la imagen.", 25),
    (110, "Duradero y bien hecho.", 25),

    # Comentarios para "Bufanda de Cashmere"
    (111, "Increíblemente suave y calienta bien.", 26),
    (112, "Un poco cara, pero vale la pena por la calidad.", 26),
    (113, "Elegante y versátil, combina con muchas prendas.", 26),
    (114, "La bufanda es más larga de lo que pensaba.", 26),
    (115, "No se deshilacha fácilmente, buena construcción.", 26),

    # Comentarios para "Cinturón de Cuero"
    (116, "El cuero es de alta calidad y duradero.", 27),
    (117, "La hebilla podría ser mejor.", 27),
    (118, "Un básico para cualquier armario.", 27),
    (119, "Ajusta bien y es cómodo.", 27),
    (120, "El color es un poco más oscuro en persona.", 27),

    # Comentarios para "Zapatillas Deportivas"
    (121, "Perfectas para correr, muy cómodas.", 28),
    (122, "El soporte para el arco podría ser mejor",28),
    (123, "Increíblemente cómodas para correr y hacer ejercicio.", 28),
    (124, "Me gustó el diseño moderno, pero esperaba mejor amortiguación.", 28),
    (125, "Resistentes y de buena calidad, valen su precio.", 28),
    (126, "El color es un poco diferente al de la foto, pero aún así me gustan.", 28),
    (127, "Perfectas para entrenamientos diarios, muy ligeras.", 28),
    (128, "No son tan transpirables como esperaba.", 28),

    # Comentarios para "Botas de Cuero"
    (129, "Elegantes y duraderas, excelentes para el invierno.", 29),
    (130, "Un poco rígidas al principio, pero se adaptan bien con el tiempo.", 29),
    (131, "La calidad del cuero es excepcional, muy satisfecho con la compra.", 29),
    (132, "No son tan cómodas para largas caminatas, pero lucen geniales.", 29),
    (133, "Mejores de lo que esperaba, se ven y se sienten premium.", 29),
    (134, "Necesitan cuidado regular para mantener el cuero en buenas condiciones.", 29),

    # Comentarios para "Sandalias Planas"
    (135, "Muy cómodas y versátiles para el verano.", 30),
    (136, "Ligeras y con un diseño bonito, pero la suela se desgasta rápido.", 30),
    (137, "Excelente relación calidad-precio, las uso casi todos los días.", 30),
    (138, "La correa rozó un poco al principio, pero luego se suavizó.", 30),
    (139, "Ideales para la playa o para salir casualmente.", 30),
    (140, "No son tan resistentes, pero son bastante cómodas para el precio.", 30)


]


# Insertar datos en la tabla comentario
cursor.executemany('INSERT INTO comentario VALUES (?, ?, ?)', comentarios)

# Guardar (commit) los cambios
conn.commit()

# Cerrar la conexión
conn.close()
