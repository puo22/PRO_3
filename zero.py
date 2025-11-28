import re
import sys
from antlr4 import CommonTokenStream, InputStream
from ZeroLexer import ZeroLexer
from ZeroParser import ZeroParser
from ZeroVisitor import ZeroVisitor

from librerias.algebra import *  # noqa: F403
from librerias.archivos import cargar, col
from librerias.modelos import regresion, predecir, perceptron, kmeans
from librerias.graficos import puntos, linea, graficar


ZERO_KEYWORDS = {
    "ver": "eco",
    "cargar": "leer",
    "col": "columna",
    "regresion": "ajustar",
    "predecir": "pronosticar",
    "perceptron": "red_simple",
    "kmeans": "segmentar",
    "mat_suma": "suma_mat",
    "mat_resta": "resta_mat",
    "mat_mult": "multiplica_mat",
    "mat_trans": "transpuesta",
    "mat_inv": "inversa",
    "puntos": "nube",
    "linea": "trazo",
    "graficar": "render",
}
_KEYWORD_PATTERN = re.compile(r"\b(" + "|".join(map(re.escape, ZERO_KEYWORDS)) + r")\b")


def _rewrite_zero_syntax(source: str) -> str:
    """Normaliza palabras clave. No toca => porque ya es un token válido."""
    parts = re.split(r'("(?:\\\\.|[^"\\\\])*")', source)
    for i in range(0, len(parts), 2):
        parts[i] = _KEYWORD_PATTERN.sub(lambda m: ZERO_KEYWORDS[m.group(0)], parts[i])
    return "".join(parts)


class ZeroInterpreter(ZeroVisitor):
    def __init__(self):
        self.mem = {}

    def _log_exec(self, ctx, message):
        line = ctx.start.line
        col = ctx.start.column + 1
        print(f"line {line}:{col} → {message}")

    def visitAssignStmt(self, ctx):
        name = ctx.ID().getText()
        val = self.visit(ctx.expression())
        self.mem[name] = val
        if isinstance(val, list) and len(val) > 4:
            val_repr = f"[{len(val)} elementos]"
        else:
            val_repr = str(val)
        self._log_exec(ctx, f"assign {name} = {val_repr}")
        return val

    def visitBloque(self, ctx):
        for st in ctx.statement():
            self.visit(st)

    def visitPrintStmt(self, ctx):
        outputs = []
        for item in ctx.printItem():
            if isinstance(item, ZeroParser.StringItemContext):
                val = item.STRING().getText()[1:-1]
            else:
                val = self.visit(item.expression())
            outputs.append(str(val))
        result = " ".join(outputs)
        self._log_exec(ctx, f"eco → {result}")
        print(result)
        return result

    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.expression())
        if cond:
            self.visit(ctx.bloque(0))
        elif ctx.bloque(1):
            self.visit(ctx.bloque(1))

    def visitWhileStmt(self, ctx):
        while self.visit(ctx.expression()):
            self.visit(ctx.bloque())

    def _load_data(self, string_ctx):
        ruta = string_ctx.getText()[1:-1]
        return cargar("info/" + ruta)

    def visitLoadStmt(self, ctx):
        return self._load_data(ctx.STRING())

    def visitLoadExpr(self, ctx):
        return self._load_data(ctx.STRING())

    def visitColStmt(self, ctx):
        mat_expr = ctx.expression(0)
        if hasattr(mat_expr, 'ID'):
            var_name = mat_expr.ID().getText()
        else:
            var_name = "mat"
        idx = int(self.visit(ctx.expression(1)))
        result = self._col(ctx)
        self._log_exec(ctx, f"columna({var_name}, {idx}) → {len(result)} elementos")
        return result

    def visitColExpr(self, ctx):
        return self._col(ctx)

    def _col(self, ctx):
        mat = self.visit(ctx.expression(0))
        idx = int(self.visit(ctx.expression(1)))
        return col(mat, idx)

    def visitRegresionStmt(self, ctx):
        result = self._regresion(ctx)
        self._log_exec(ctx, "trained modelo (regresión lineal)")
        return result

    def visitRegresionExpr(self, ctx):
        return self._regresion(ctx)

    def _regresion(self, ctx):
        X = self.visit(ctx.expression(0))
        y = self.visit(ctx.expression(1))
        return regresion(X, y)

    def visitPredecirStmt(self, ctx):
        mod = self.visit(ctx.expression(0))
        x = self.visit(ctx.expression(1))
        result = predecir(mod, x)
        # No log aquí para evitar ruido; ya se ve en eco
        return result

    def visitPredecirExpr(self, ctx):
        return self._predecir(ctx)

    def _predecir(self, ctx):
        mod = self.visit(ctx.expression(0))
        x = self.visit(ctx.expression(1))
        return predecir(mod, x)

    def visitPerceptronStmt(self, ctx):
        self._log_exec(ctx, "train red_simple(...) → iniciando")
        result = self._perceptron(ctx)
        self._log_exec(ctx, "trained modelo (perceptrón)")
        return result

    def visitPerceptronExpr(self, ctx):
        return self._perceptron(ctx)

    def _perceptron(self, ctx):
        X = self.visit(ctx.expression(0))
        y = self.visit(ctx.expression(1))
        capas = self.visit(ctx.expression(2)) if ctx.expression(2) else None
        return perceptron(X, y, capas)

    def visitKmeansStmt(self, ctx):
        self._log_exec(ctx, "train segmentar(...) → iniciando")
        result = self._kmeans(ctx)
        self._log_exec(ctx, "trained modelo (k-means)")
        return result

    def visitKmeansExpr(self, ctx):
        return self._kmeans(ctx)

    def _kmeans(self, ctx):
        X = self.visit(ctx.expression(0))
        k = int(self.visit(ctx.expression(1)))
        it = int(self.visit(ctx.expression(2))) if ctx.expression(2) else 20
        return kmeans(X, k, it)

    def visitPuntosStmt(self, ctx):
        X = self.visit(ctx.expression(0))
        y = self.visit(ctx.expression(1))
        color = "rojo"
        if ctx.STRING():
            color = ctx.STRING().getText()[1:-1]
        puntos(X, y, color)
        self._log_exec(ctx, f"nube({len(X)} puntos, color='{color}')")
        return None

    def visitLineaStmt(self, ctx):
        mod = self.visit(ctx.expression())
        linea(mod)
        self._log_exec(ctx, "trazo modelo de regresión")
        return None

    def visitGraficarStmt(self, ctx):
        self._log_exec(ctx, "render → generando gráfica")
        graficar()
        return None

    # === EXPRESIONES ===
    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())

    def visitSqrtExpr(self, ctx):
        return raiz(self.visit(ctx.expression()))

    def visitSinExpr(self, ctx):
        return seno(self.visit(ctx.expression()))

    def visitPowerExpr(self, ctx):
        return potencia(self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

    def visitMulDivExpr(self, ctx):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        op = ctx.op.text
        if op == "*":
            return multiplicar(a, b)
        if op == "/":
            return dividir(a, b)
        return a % b

    def visitAddSubExpr(self, ctx):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        return sumar(a, b) if ctx.op.text == "+" else restar(a, b)

    def visitCmpExpr(self, ctx):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        op = ctx.op.text
        if op == "==":
            return a == b
        if op == "!=":
            return a != b
        if op == ">":
            return a > b
        if op == "<":
            return a < b
        if op == ">=":
            return a >= b
        return a <= b

    def visitBoolExpr(self, ctx):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        if ctx.op.text == "&&":
            return bool(a) and bool(b)
        return bool(a) or bool(b)

    # === ÁTOMOS ===
    def visitNumberAtom(self, ctx):
        t = ctx.getText()
        return int(t) if "." not in t else float(t)

    def visitTrueAtom(self, ctx):
        return True

    def visitFalseAtom(self, ctx):
        return False

    def visitVarAtom(self, ctx):
        n = ctx.ID().getText()
        return self.mem.get(n, 0)

    def visitIndexAtom(self, ctx):
        nombre = ctx.ID().getText()
        seq = self.mem.get(nombre, [])
        idx = int(self.visit(ctx.expression()))
        return seq[idx]

    def visitVectorAtom(self, ctx):
        return [self.visit(e) for e in ctx.exprList().expression()]

    def visitParenAtom(self, ctx):
        return self.visit(ctx.expression())


def ejecutar(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        fuente = f.read()
    input_stream = InputStream(_rewrite_zero_syntax(fuente))
    lexer = ZeroLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ZeroParser(stream)
    tree = parser.program()
    ZeroInterpreter().visit(tree)
    print(f"\nZERO → '{archivo}' ejecutado con éxito")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        ejecutar(sys.argv[1])
    else:
        print("Uso: python3 zero.py archivo.zero")
