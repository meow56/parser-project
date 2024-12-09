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


    # Enter a parse tree produced by D1Parser#lines.
    def enterLines(self, ctx:D1Parser.LinesContext):
        pass

    # Exit a parse tree produced by D1Parser#lines.
    def exitLines(self, ctx:D1Parser.LinesContext):
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


    # Enter a parse tree produced by D1Parser#conditional.
    def enterConditional(self, ctx:D1Parser.ConditionalContext):
        pass

    # Exit a parse tree produced by D1Parser#conditional.
    def exitConditional(self, ctx:D1Parser.ConditionalContext):
        pass


    # Enter a parse tree produced by D1Parser#block.
    def enterBlock(self, ctx:D1Parser.BlockContext):
        pass

    # Exit a parse tree produced by D1Parser#block.
    def exitBlock(self, ctx:D1Parser.BlockContext):
        pass


    # Enter a parse tree produced by D1Parser#conditional2.
    def enterConditional2(self, ctx:D1Parser.Conditional2Context):
        pass

    # Exit a parse tree produced by D1Parser#conditional2.
    def exitConditional2(self, ctx:D1Parser.Conditional2Context):
        pass


    # Enter a parse tree produced by D1Parser#block2.
    def enterBlock2(self, ctx:D1Parser.Block2Context):
        pass

    # Exit a parse tree produced by D1Parser#block2.
    def exitBlock2(self, ctx:D1Parser.Block2Context):
        pass


    # Enter a parse tree produced by D1Parser#conditional3.
    def enterConditional3(self, ctx:D1Parser.Conditional3Context):
        pass

    # Exit a parse tree produced by D1Parser#conditional3.
    def exitConditional3(self, ctx:D1Parser.Conditional3Context):
        pass


    # Enter a parse tree produced by D1Parser#block3.
    def enterBlock3(self, ctx:D1Parser.Block3Context):
        pass

    # Exit a parse tree produced by D1Parser#block3.
    def exitBlock3(self, ctx:D1Parser.Block3Context):
        pass


    # Enter a parse tree produced by D1Parser#boolExpr.
    def enterBoolExpr(self, ctx:D1Parser.BoolExprContext):
        pass

    # Exit a parse tree produced by D1Parser#boolExpr.
    def exitBoolExpr(self, ctx:D1Parser.BoolExprContext):
        pass


    # Enter a parse tree produced by D1Parser#comparisons.
    def enterComparisons(self, ctx:D1Parser.ComparisonsContext):
        pass

    # Exit a parse tree produced by D1Parser#comparisons.
    def exitComparisons(self, ctx:D1Parser.ComparisonsContext):
        pass


    # Enter a parse tree produced by D1Parser#while.
    def enterWhile(self, ctx:D1Parser.WhileContext):
        pass

    # Exit a parse tree produced by D1Parser#while.
    def exitWhile(self, ctx:D1Parser.WhileContext):
        pass


    # Enter a parse tree produced by D1Parser#while2.
    def enterWhile2(self, ctx:D1Parser.While2Context):
        pass

    # Exit a parse tree produced by D1Parser#while2.
    def exitWhile2(self, ctx:D1Parser.While2Context):
        pass


    # Enter a parse tree produced by D1Parser#while3.
    def enterWhile3(self, ctx:D1Parser.While3Context):
        pass

    # Exit a parse tree produced by D1Parser#while3.
    def exitWhile3(self, ctx:D1Parser.While3Context):
        pass


    # Enter a parse tree produced by D1Parser#for.
    def enterFor(self, ctx:D1Parser.ForContext):
        pass

    # Exit a parse tree produced by D1Parser#for.
    def exitFor(self, ctx:D1Parser.ForContext):
        pass


    # Enter a parse tree produced by D1Parser#for2.
    def enterFor2(self, ctx:D1Parser.For2Context):
        pass

    # Exit a parse tree produced by D1Parser#for2.
    def exitFor2(self, ctx:D1Parser.For2Context):
        pass


    # Enter a parse tree produced by D1Parser#for3.
    def enterFor3(self, ctx:D1Parser.For3Context):
        pass

    # Exit a parse tree produced by D1Parser#for3.
    def exitFor3(self, ctx:D1Parser.For3Context):
        pass



del D1Parser