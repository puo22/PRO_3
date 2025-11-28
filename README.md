# Lenguaje Zero

Para probar operaciones numéricas, matrices y modelos sencillos (regresión, perceptrón, k-means) con una sintaxis en español.

## Estructura del proyecto
- `zero.py`: intérprete. Carga código `.zero`, reescribe las palabras clave de Zero y ejecuta el árbol ANTLR.
- `Zero.g4`: gramática ANTLR (Python3). Si regeneras el parser/lexer usa este archivo.
- `librerias/`: utilidades que usa el lenguaje.
  - `algebra.py`: aritmética, trigonometría y operaciones de matrices.
  - `archivos.py`: carga CSV sencilla (`leer`) y selección de columnas (`columna`).
  - `modelos.py`: regresión lineal (`ajustar`), perceptrón (`red_simple`), k-means (`segmentar`) y predicción (`pronosticar`).
  - `graficos.py`: puntos, línea de regresión y `render`.
- `info/`: datos de ejemplo (CSV).
- `ejercicios/`: programas de muestra `.zero` (básico, regresión, control de flujo, perceptrón OR, k-means, seno).

## Ejecutar un programa
```bash
python3 zero.py ejercicios/01_intro_basico.zero
```
El intérprete imprime un mensaje de éxito al terminar.

## Sintaxis básica de Zero
- **Asignación**: `nombre => expresion`
- **Imprimir**: `eco item [, item]*` (cada `item` puede ser string o expresión)
- **Condicional**: `si (cond) { ... } [sino { ... }]`
- **Bucle**: `mientras (cond) { ... }`
- **Vectores**: `[1, 2, 3]`; matrices: `[[1,2],[3,4]]`
- **Indexar**: `v[0]`
- **Operadores**: `+ - * / % ^` y comparaciones `< > <= >= == !=`; booleanos `&& ||`
- **Funciones numéricas**: `raiz(x)`, `seno(x)`

### Operaciones con datos y modelos
- Cargar CSV: `datos => leer("archivo.csv")` (busca en `info/`)
- Tomar columna: `x => columna(datos, 0)`
- Regresión lineal: `modelo => ajustar(x, y)`
- Perceptrón: `red => red_simple(X, y, [capas...])`
- K-means: `clusters => segmentar(X, k, iteracionesOpcional)`
- Predicción: `p => pronosticar(modelo, entrada)`

### Operaciones con matrices
- `suma_mat(A, B)`, `resta_mat(A, B)`, `multiplica_mat(A, B)`
- `transpuesta(A)`, `inversa(A)`

### Gráficos
- `nube(X, y, "colorOpcional")`
- `trazo(modelo)` para línea de regresión
- `render()` para mostrar la figura

## Ejemplo corto
```zero
datos => leer("altura_peso.csv")
X => columna(datos, 0)
y => columna(datos, 1)
modelo => ajustar(X, y)
eco "Predicción 1.78m:", pronosticar(modelo, 1.78)
nube(X, y, "rojo")
trazo(modelo)
render()
```
