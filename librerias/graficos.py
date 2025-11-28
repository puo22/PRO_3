puntos_datos = []
lineas = []


def puntos(X, y, color="rojo"):
    """Acumula puntos a graficar."""
    global puntos_datos
    colores = {"rojo": (255, 0, 0), "azul": (0, 0, 255), "verde": (0, 255, 0)}
    c = colores.get(color.lower(), (255, 0, 0))
    for x, yy in zip(X, y):
        puntos_datos.append((float(x), float(yy), c))


def linea(modelo):
    """Añade una línea (m, b) a graficar."""
    global lineas
    # asegurar que vienen dos valores
    if len(modelo) != 2:
        raise ValueError("El modelo debe ser [m, b]")
    m, b = float(modelo[0]), float(modelo[1])
    lineas.append((m, b))


def _ajustar_rango(valores, extra=0.1):
    """Devuelve (min, max) con padding configurable."""
    vmin = min(valores)
    vmax = max(valores)

    if vmin == vmax:
        delta = abs(vmin) if vmin != 0 else 1.0
        vmin -= delta * extra
        vmax += delta * extra
    else:
        margen = (vmax - vmin) * extra
        vmin -= margen
        vmax += margen

    return vmin, vmax


def _a_pixel(x, y, x1, x2, y1, y2, w, h):
    """Convierte coordenadas reales a pixel."""
    px = int((x - x1) / (x2 - x1) * (w - 1))
    py = int((y2 - y) / (y2 - y1) * (h - 1))
    return px, py


def _guardar_ppm(nombre, ancho, alto, pixels):
    with open(nombre, "wb") as f:
        f.write(f"P6\n{ancho} {alto}\n255\n".encode())
        f.write(pixels)


def graficar(nombre="resultado.png", ancho=800, alto=600, limpiar=True):
    if not puntos_datos and not lineas:
        print("No hay datos para graficar")
        return

    # -----------------------------------------------------
    # Determinar rangos globales considerando puntos y líneas
    # -----------------------------------------------------
    xs = [p[0] for p in puntos_datos] if puntos_datos else [0]
    ys = [p[1] for p in puntos_datos] if puntos_datos else [0]

    # si hay líneas, añadir algunos puntos representativos
    for m, b in lineas:
        xs += [-5, 5]
        ys += [m * -5 + b, m * 5 + b]

    x1, x2 = _ajustar_rango(xs)
    y1, y2 = _ajustar_rango(ys)

    fondo = 255
    pixels = bytearray([fondo] * (ancho * alto * 3))

    def dibujar(px, py, color):
        if 0 <= px < ancho and 0 <= py < alto:
            idx = (py * ancho + px) * 3
            pixels[idx:idx + 3] = bytes(color)

    # --------------------
    # Dibujar Eje Y si está dentro
    # --------------------
    gris = (200, 200, 200)
    if x1 <= 0 <= x2:
        px0, _ = _a_pixel(0, y1, x1, x2, y1, y2, ancho, alto)
        for py in range(alto):
            dibujar(px0, py, gris)

    # --------------------
    # Dibujar Eje X si está dentro
    # --------------------
    if y1 <= 0 <= y2:
        _, py0 = _a_pixel(x1, 0, x1, x2, y1, y2, ancho, alto)
        for px in range(ancho):
            dibujar(px, py0, gris)

    # --------------------
    # Dibujar líneas de regresión (azul por defecto)
    # --------------------
    for m, b in lineas:
        for px in range(ancho):
            x = x1 + (px / (ancho - 1)) * (x2 - x1)
            y = m * x + b
            py = int((y2 - y) / (y2 - y1) * (alto - 1))
            dibujar(px, py, (0, 0, 255))

    # --------------------
    # Dibujar puntos (3x3)
    # --------------------
    for x, y, color in puntos_datos:
        cx, cy = _a_pixel(x, y, x1, x2, y1, y2, ancho, alto)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                dibujar(cx + dx, cy + dy, color)

    # --------------------
    # Guardado
    # --------------------
    ext = nombre.lower().rsplit(".", 1)[-1] if "." in nombre else ""

    if ext == "ppm" or not ext:
        _guardar_ppm(nombre, ancho, alto, pixels)
    else:
        try:
            from PIL import Image
            img = Image.frombytes("RGB", (ancho, alto), bytes(pixels))
            img.save(nombre)
        except Exception as exc:
            fallback = "resultado.ppm"
            _guardar_ppm(fallback, ancho, alto, pixels)
            print(f"No se pudo guardar {nombre} ({exc}); se guardó PPM como {fallback}")
            nombre = fallback

    if limpiar:
        puntos_datos.clear()
        lineas.clear()

    print(f"Gráfica generada: {nombre}")
