# Generated from Zero.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ZeroParser import ZeroParser
else:
    from ZeroParser import ZeroParser

# This class defines a complete generic visitor for a parse tree produced by ZeroParser.

class ZeroVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZeroParser#program.
    def visitProgram(self, ctx:ZeroParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#assignStmt.
    def visitAssignStmt(self, ctx:ZeroParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#printStmt.
    def visitPrintStmt(self, ctx:ZeroParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#ifStmt.
    def visitIfStmt(self, ctx:ZeroParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#whileStmt.
    def visitWhileStmt(self, ctx:ZeroParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#loadStmt.
    def visitLoadStmt(self, ctx:ZeroParser.LoadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#colStmt.
    def visitColStmt(self, ctx:ZeroParser.ColStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#regresionStmt.
    def visitRegresionStmt(self, ctx:ZeroParser.RegresionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#predecirStmt.
    def visitPredecirStmt(self, ctx:ZeroParser.PredecirStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#perceptronStmt.
    def visitPerceptronStmt(self, ctx:ZeroParser.PerceptronStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#kmeansStmt.
    def visitKmeansStmt(self, ctx:ZeroParser.KmeansStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#matSumaStmt.
    def visitMatSumaStmt(self, ctx:ZeroParser.MatSumaStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#matRestaStmt.
    def visitMatRestaStmt(self, ctx:ZeroParser.MatRestaStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#matMultStmt.
    def visitMatMultStmt(self, ctx:ZeroParser.MatMultStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#matTransStmt.
    def visitMatTransStmt(self, ctx:ZeroParser.MatTransStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#matInvStmt.
    def visitMatInvStmt(self, ctx:ZeroParser.MatInvStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#puntosStmt.
    def visitPuntosStmt(self, ctx:ZeroParser.PuntosStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#lineaStmt.
    def visitLineaStmt(self, ctx:ZeroParser.LineaStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#graficarStmt.
    def visitGraficarStmt(self, ctx:ZeroParser.GraficarStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#exprStmt.
    def visitExprStmt(self, ctx:ZeroParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#bloque.
    def visitBloque(self, ctx:ZeroParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#stringItem.
    def visitStringItem(self, ctx:ZeroParser.StringItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#exprItem.
    def visitExprItem(self, ctx:ZeroParser.ExprItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#loadExpr.
    def visitLoadExpr(self, ctx:ZeroParser.LoadExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#matSumaExpr.
    def visitMatSumaExpr(self, ctx:ZeroParser.MatSumaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#powerExpr.
    def visitPowerExpr(self, ctx:ZeroParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#addSubExpr.
    def visitAddSubExpr(self, ctx:ZeroParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#regresionExpr.
    def visitRegresionExpr(self, ctx:ZeroParser.RegresionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#predecirExpr.
    def visitPredecirExpr(self, ctx:ZeroParser.PredecirExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#sinExpr.
    def visitSinExpr(self, ctx:ZeroParser.SinExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#sqrtExpr.
    def visitSqrtExpr(self, ctx:ZeroParser.SqrtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#atomExpr.
    def visitAtomExpr(self, ctx:ZeroParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#matRestaExpr.
    def visitMatRestaExpr(self, ctx:ZeroParser.MatRestaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#matTransExpr.
    def visitMatTransExpr(self, ctx:ZeroParser.MatTransExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#kmeansExpr.
    def visitKmeansExpr(self, ctx:ZeroParser.KmeansExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#cmpExpr.
    def visitCmpExpr(self, ctx:ZeroParser.CmpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#colExpr.
    def visitColExpr(self, ctx:ZeroParser.ColExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#matInvExpr.
    def visitMatInvExpr(self, ctx:ZeroParser.MatInvExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#perceptronExpr.
    def visitPerceptronExpr(self, ctx:ZeroParser.PerceptronExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#matMultExpr.
    def visitMatMultExpr(self, ctx:ZeroParser.MatMultExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#boolExpr.
    def visitBoolExpr(self, ctx:ZeroParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:ZeroParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#numberAtom.
    def visitNumberAtom(self, ctx:ZeroParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#trueAtom.
    def visitTrueAtom(self, ctx:ZeroParser.TrueAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#falseAtom.
    def visitFalseAtom(self, ctx:ZeroParser.FalseAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#indexAtom.
    def visitIndexAtom(self, ctx:ZeroParser.IndexAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#varAtom.
    def visitVarAtom(self, ctx:ZeroParser.VarAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#vectorAtom.
    def visitVectorAtom(self, ctx:ZeroParser.VectorAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#parenAtom.
    def visitParenAtom(self, ctx:ZeroParser.ParenAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZeroParser#exprList.
    def visitExprList(self, ctx:ZeroParser.ExprListContext):
        return self.visitChildren(ctx)



del ZeroParser