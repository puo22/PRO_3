import math
import random

# Fijar semilla para reproducibilidad
random.seed(42)

# ---------------- REGRESIÓN LINEAL ----------------

def regresion(X, y):
    n = len(X)
    sx = sy = sxy = sx2 = 0
    for i in range(n):
        sx += X[i]
        sy += y[i]
        sxy += X[i] * y[i]
        sx2 += X[i] * X[i]
    m = (n * sxy - sx * sy) / (n * sx2 - sx * sx)
    b = (sy - m * sx) / n
    return (m, b)


# ---------------- FUNCIONES DE ACTIVACIÓN ----------------

def _sigmoide(x):
    if x < -500:
        return 0.0
    if x > 500:
        return 1.0
    return 1 / (1 + math.exp(-x))

def _sigmoide_deriv(x):
    s = _sigmoide(x)
    return s * (1 - s)


# ---------------- PERCEPTRÓN MULTICAPA (SIN LOGS, XOR CORRECTO) ----------------

def perceptron(X, y, config=None):
    import math, random
    random.seed(42)  # Asegura resultados reproducibles

    hidden_size = 2
    epochs = 5000
    lr = 1.0

    if config is not None:
        if isinstance(config, list) and len(config) >= 1:
            hidden_size = config[0]
        elif isinstance(config, int):
            epochs = config

    # Inicialización de pesos
    w1 = [[(random.random() - 0.5) for _ in range(hidden_size)] for _ in range(2)]
    b1 = [(random.random() - 0.5) for _ in range(hidden_size)]
    w2 = [(random.random() - 0.5) for _ in range(hidden_size)]
    b2 = (random.random() - 0.5)

    def sigmoid(x):
        if x < -500: return 0.0
        if x > 500: return 1.0
        return 1 / (1 + math.exp(-x))

    def sigmoid_deriv(x):
        s = sigmoid(x)
        return s * (1 - s)

    # Entrenamiento (SILENCIOSO)
    for _ in range(epochs):
        for xi, yi in zip(X, y):
            # Forward
            hidden = []
            for j in range(hidden_size):
                z = w1[0][j] * xi[0] + w1[1][j] * xi[1] + b1[j]
                hidden.append(sigmoid(z))
            z_out = sum(w2[j] * hidden[j] for j in range(hidden_size)) + b2
            output = sigmoid(z_out)

            # Backpropagation
            d_output = (output - yi) * sigmoid_deriv(z_out)
            d_hidden = []
            for j in range(hidden_size):
                z_hidden = w1[0][j] * xi[0] + w1[1][j] * xi[1] + b1[j]
                grad = d_output * w2[j] * sigmoid_deriv(z_hidden)
                d_hidden.append(grad)

            # Actualización de pesos
            for j in range(hidden_size):
                w2[j] -= lr * d_output * hidden[j]
            b2 -= lr * d_output

            for i in range(2):
                for j in range(hidden_size):
                    w1[i][j] -= lr * d_hidden[j] * xi[i]
            for j in range(hidden_size):
                b1[j] -= lr * d_hidden[j]

    # Construir modelo en formato compatible
    pesos_oculta = []
    for j in range(hidden_size):
        pesos_oculta.append([w1[0][j], w1[1][j], b1[j]])
    pesos_salida = [w2[j] for j in range(hidden_size)] + [b2]

    return {
        "tipo": "perceptron",
        "capas": [2, hidden_size, 1],
        "pesos": [pesos_oculta, [pesos_salida]]
    }


def _forward_perceptron(modelo, x):
    pesos = modelo["pesos"]
    entrada = x
    for capa in pesos:
        salida = []
        for neuron in capa:
            s = sum(w * v for w, v in zip(neuron[:-1], entrada)) + neuron[-1]
            salida.append(_sigmoide(s))
        entrada = salida
    return entrada


# ---------------- K-MEANS ----------------

def kmeans(X, k, iteraciones=20):
    if not X:
        return {"tipo": "kmeans", "centroides": [], "etiquetas": []}

    dim = len(X[0])
    centroides = random.sample(X, min(k, len(X)))
    etiquetas = [0] * len(X)

    for _ in range(iteraciones):
        for i, x in enumerate(X):
            dist_min = None
            c_min = 0
            for idx, c in enumerate(centroides):
                d = sum((xi - ci) ** 2 for xi, ci in zip(x, c))
                if dist_min is None or d < dist_min:
                    dist_min = d
                    c_min = idx
            etiquetas[i] = c_min

        nuevos = [[0.0] * dim for _ in centroides]
        cont = [0] * len(centroides)
        for etiqueta, x in zip(etiquetas, X):
            cont[etiqueta] += 1
            for j, v in enumerate(x):
                nuevos[etiqueta][j] += v

        for i in range(len(centroides)):
            if cont[i]:
                centroides[i] = [v / cont[i] for v in nuevos[i]]

    return {"tipo": "kmeans", "centroides": centroides, "etiquetas": etiquetas}


# ---------------- PREDICCIÓN ----------------

def predecir(modelo, x):
    if isinstance(modelo, tuple) and len(modelo) == 2:
        m, b = modelo
        return m * x + b

    if isinstance(modelo, dict):
        tipo = modelo.get("tipo")

        if tipo == "perceptron":
            salida = _forward_perceptron(modelo, x)[0]
            return 1 if salida >= 0.5 else 0

        if tipo == "kmeans":
            centroides = modelo.get("centroides", [])
            if not centroides:
                return -1
            dist_min = None
            c_min = 0
            for idx, c in enumerate(centroides):
                d = sum((xi - ci) ** 2 for xi, ci in zip(x, c))
                if dist_min is None or d < dist_min:
                    dist_min = d
                    c_min = idx
            return c_min

    raise ValueError("Modelo no soportado")
