def cargar(ruta):
    datos = []
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea and not linea.startswith("#"):
                fila = []
                for v in linea.split(","):
                    v = v.strip()
                    if v.replace(".", "").replace("-", "").isdigit() or (
                        v and v[0] in "+-" and v[1:].replace(".", "").isdigit()
                    ):
                        fila.append(float(v))
                    else:
                        fila.append(v)
                datos.append(fila)
    return datos


def col(matriz, i):
    return [fila[i] for fila in matriz if len(fila) > i]
