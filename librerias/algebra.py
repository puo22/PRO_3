def _es_matriz(m):
    return isinstance(m, list) and m and all(isinstance(f, list) for f in m)


def _shape(m):
    if _es_matriz(m):
        return len(m), len(m[0]) if m else 0
    return None


def _es_num(x):
    return isinstance(x, (int, float))


def sumar(a, b):
    if isinstance(a, list) and isinstance(b, list) and not _es_matriz(a) and not _es_matriz(b):
        return [x + y for x, y in zip(a, b)]
    if _es_matriz(a) and _es_matriz(b):
        return mat_suma(a, b)
    return a + b


def restar(a, b):
    if isinstance(a, list) and isinstance(b, list) and not _es_matriz(a) and not _es_matriz(b):
        return [x - y for x, y in zip(a, b)]
    if _es_matriz(a) and _es_matriz(b):
        return mat_resta(a, b)
    return a - b


def multiplicar(a, b):
    if _es_matriz(a) or _es_matriz(b):
        return mat_mult(a, b)
    if isinstance(a, list) and _es_num(b):
        return [x * b for x in a]
    if isinstance(b, list) and _es_num(a):
        return [a * x for x in b]
    return a * b


def dividir(a, b):
    if isinstance(a, list) and _es_num(b):
        return [x / b for x in a]
    return a / b


def potencia(b, e):
    r = 1
    for _ in range(int(e)):
        r *= b
    return r


def raiz(x):
    if x < 0:
        return 0
    g = x / 2
    for _ in range(20):
        g = (g + x / g) / 2
    return g


def seno(x):
    x = x % 6.283185307
    r = x
    t = x
    for i in range(1, 15):
        t = -t * x * x / ((2 * i) * (2 * i + 1))
        r += t
    return r


# Operaciones de matrices básicas
def mat_suma(A, B):
    if not (_es_matriz(A) and _es_matriz(B)):
        raise ValueError("mat_suma requiere dos matrices")
    if _shape(A) != _shape(B):
        raise ValueError("Dimensiones incompatibles en mat_suma")
    return [[x + y for x, y in zip(fa, fb)] for fa, fb in zip(A, B)]


def mat_resta(A, B):
    if not (_es_matriz(A) and _es_matriz(B)):
        raise ValueError("mat_resta requiere dos matrices")
    if _shape(A) != _shape(B):
        raise ValueError("Dimensiones incompatibles en mat_resta")
    return [[x - y for x, y in zip(fa, fb)] for fa, fb in zip(A, B)]


def mat_mult(A, B):
    # Matriz x matriz o matriz x vector o escalar
    if _es_matriz(A) and _es_matriz(B):
        ra, ca = _shape(A)
        rb, cb = _shape(B)
        if ca != rb:
            raise ValueError("Dimensiones incompatibles en mat_mult")
        return [
            [sum(A[i][k] * B[k][j] for k in range(ca)) for j in range(cb)]
            for i in range(ra)
        ]
    if _es_matriz(A) and _es_num(B):
        return [[x * B for x in fila] for fila in A]
    if _es_matriz(B) and _es_num(A):
        return [[A * x for x in fila] for fila in B]
    if _es_matriz(A) and isinstance(B, list) and not _es_matriz(B):
        ra, ca = _shape(A)
        if ca != len(B):
            raise ValueError("Dimensiones incompatibles en mat_mult con vector")
        return [sum(A[i][k] * B[k] for k in range(ca)) for i in range(ra)]
    if isinstance(A, list) and not _es_matriz(A) and _es_matriz(B):
        rb, cb = _shape(B)
        if len(A) != rb:
            raise ValueError("Dimensiones incompatibles en mat_mult con vector")
        return [sum(A[k] * B[k][j] for k in range(rb)) for j in range(cb)]
    return A * B


def mat_trans(A):
    if not _es_matriz(A):
        raise ValueError("mat_trans requiere matriz")
    return [list(fila) for fila in zip(*A)]


def mat_inv(A):
    if not _es_matriz(A):
        raise ValueError("mat_inv requiere matriz cuadrada")
    n, m = _shape(A)
    if n != m:
        raise ValueError("mat_inv requiere matriz cuadrada")
    # Copia extendida con identidad
    M = [list(fila) + [1 if i == j else 0 for j in range(n)] for i, fila in enumerate(A)]
    # Gauss-Jordan
    for i in range(n):
        pivote = M[i][i]
        if pivote == 0:
            # buscar fila para intercambiar
            for j in range(i + 1, n):
                if M[j][i] != 0:
                    M[i], M[j] = M[j], M[i]
                    pivote = M[i][i]
                    break
        if pivote == 0:
            raise ValueError("mat_inv matriz singular")
        # normalizar fila
        for k in range(2 * n):
            M[i][k] /= pivote
        # eliminar otras filas
        for j in range(n):
            if j == i:
                continue
            factor = M[j][i]
            for k in range(2 * n):
                M[j][k] -= factor * M[i][k]
    return [fila[n:] for fila in M]
