# Generated from D1.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .D1Parser import D1Parser
else:
    from D1Parser import D1Parser

# This class defines a complete listener for a parse tree produced by D1Parser.
class D1Listener(ParseTreeListener):

    # Enter a parse tree produced by D1Parser#start.
    def enterStart(self, ctx:D1Parser.StartContext):
        pass

    # Exit a parse tree produced by D1Parser#start.
    def exitStart(self, ctx:D1Parser.StartContext):
        pass


    # Enter a parse tree produced by D1Parser#statement.
    def enterStatement(self, ctx:D1Parser.StatementContext):
        pass

    # Exit a parse tree produced by D1Parser#statement.
    def exitStatement(self, ctx:D1Parser.StatementContext):
        pass


    # Enter a parse tree produced by D1Parser#assignment.
    def enterAssignment(self, ctx:D1Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by D1Parser#assignment.
    def exitAssignment(self, ctx:D1Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by D1Parser#eqStatement.
    def enterEqStatement(self, ctx:D1Parser.EqStatementContext):
        pass

    # Exit a parse tree produced by D1Parser#eqStatement.
    def exitEqStatement(self, ctx:D1Parser.EqStatementContext):
        pass


    # Enter a parse tree produced by D1Parser#value.
    def enterValue(self, ctx:D1Parser.ValueContext):
        pass

    # Exit a parse tree produced by D1Parser#value.
    def exitValue(self, ctx:D1Parser.ValueContext):
        pass


    # Enter a parse tree produced by D1Parser#array.
    def enterArray(self, ctx:D1Parser.ArrayContext):
        pass

    # Exit a parse tree produced by D1Parser#array.
    def exitArray(self, ctx:D1Parser.ArrayContext):
        pass


    # Enter a parse tree produced by D1Parser#boolean.
    def enterBoolean(self, ctx:D1Parser.BooleanContext):
        pass

    # Exit a parse tree produced by D1Parser#boolean.
    def exitBoolean(self, ctx:D1Parser.BooleanContext):
        pass


    # Enter a parse tree produced by D1Parser#arithmetic.
    def enterArithmetic(self, ctx:D1Parser.ArithmeticContext):
        pass

    # Exit a parse tree produced by D1Parser#arithmetic.
    def exitArithmetic(self, ctx:D1Parser.ArithmeticContext):
        pass


    # Enter a parse tree produced by D1Parser#arithSymbol.
    def enterArithSymbol(self, ctx:D1Parser.ArithSymbolContext):
        pass

    # Exit a parse tree produced by D1Parser#arithSymbol.
    def exitArithSymbol(self, ctx:D1Parser.ArithSymbolContext):
        pass



del D1Parser