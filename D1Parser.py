# Generated from D1.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,83,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,3,0,20,8,0,1,0,1,0,3,0,24,8,0,1,0,3,0,27,8,
        0,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,3,4,49,8,4,1,4,1,4,1,4,1,4,5,4,55,8,4,10,4,12,
        4,58,9,4,1,5,1,5,1,5,1,5,5,5,64,8,5,10,5,12,5,67,9,5,1,5,1,5,1,5,
        1,5,3,5,73,8,5,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,0,1,8,9,0,2,4,
        6,8,10,12,14,16,0,3,1,0,1,5,1,0,12,13,1,0,14,18,85,0,26,1,0,0,0,
        2,30,1,0,0,0,4,32,1,0,0,0,6,36,1,0,0,0,8,48,1,0,0,0,10,72,1,0,0,
        0,12,74,1,0,0,0,14,76,1,0,0,0,16,80,1,0,0,0,18,20,3,2,1,0,19,18,
        1,0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,21,27,5,19,0,0,22,24,3,2,1,0,
        23,22,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,27,5,0,0,1,26,19,1,
        0,0,0,26,23,1,0,0,0,27,1,1,0,0,0,28,31,3,4,2,0,29,31,3,8,4,0,30,
        28,1,0,0,0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,5,20,0,0,33,34,3,6,3,
        0,34,35,3,8,4,0,35,5,1,0,0,0,36,37,7,0,0,0,37,7,1,0,0,0,38,39,6,
        4,-1,0,39,49,5,21,0,0,40,49,5,22,0,0,41,49,3,10,5,0,42,49,5,20,0,
        0,43,49,3,12,6,0,44,45,5,6,0,0,45,46,3,8,4,0,46,47,5,7,0,0,47,49,
        1,0,0,0,48,38,1,0,0,0,48,40,1,0,0,0,48,41,1,0,0,0,48,42,1,0,0,0,
        48,43,1,0,0,0,48,44,1,0,0,0,49,56,1,0,0,0,50,51,10,2,0,0,51,52,3,
        16,8,0,52,53,3,8,4,3,53,55,1,0,0,0,54,50,1,0,0,0,55,58,1,0,0,0,56,
        54,1,0,0,0,56,57,1,0,0,0,57,9,1,0,0,0,58,56,1,0,0,0,59,65,5,8,0,
        0,60,61,3,8,4,0,61,62,5,9,0,0,62,64,1,0,0,0,63,60,1,0,0,0,64,67,
        1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,
        68,69,3,8,4,0,69,70,5,10,0,0,70,73,1,0,0,0,71,73,5,11,0,0,72,59,
        1,0,0,0,72,71,1,0,0,0,73,11,1,0,0,0,74,75,7,1,0,0,75,13,1,0,0,0,
        76,77,3,8,4,0,77,78,3,16,8,0,78,79,3,8,4,0,79,15,1,0,0,0,80,81,7,
        2,0,0,81,17,1,0,0,0,8,19,23,26,30,48,56,65,72
    ]

class D1Parser ( Parser ):

    grammarFileName = "D1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'('", "')'", "'['", "','", "']'", "'[]'", "'True'", 
                     "'False'", "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NEWLINES", 
                      "VARNAME", "NUMBER", "STRING", "WS" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_eqStatement = 3
    RULE_value = 4
    RULE_array = 5
    RULE_boolean = 6
    RULE_arithmetic = 7
    RULE_arithSymbol = 8

    ruleNames =  [ "start", "statement", "assignment", "eqStatement", "value", 
                   "array", "boolean", "arithmetic", "arithSymbol" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    NEWLINES=19
    VARNAME=20
    NUMBER=21
    STRING=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINES(self):
            return self.getToken(D1Parser.NEWLINES, 0)

        def statement(self):
            return self.getTypedRuleContext(D1Parser.StatementContext,0)


        def EOF(self):
            return self.getToken(D1Parser.EOF, 0)

        def getRuleIndex(self):
            return D1Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = D1Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7354688) != 0):
                    self.state = 18
                    self.statement()


                self.state = 21
                self.match(D1Parser.NEWLINES)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7354688) != 0):
                    self.state = 22
                    self.statement()


                self.state = 25
                self.match(D1Parser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(D1Parser.AssignmentContext,0)


        def value(self):
            return self.getTypedRuleContext(D1Parser.ValueContext,0)


        def getRuleIndex(self):
            return D1Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = D1Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.value(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(D1Parser.VARNAME, 0)

        def eqStatement(self):
            return self.getTypedRuleContext(D1Parser.EqStatementContext,0)


        def value(self):
            return self.getTypedRuleContext(D1Parser.ValueContext,0)


        def getRuleIndex(self):
            return D1Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = D1Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(D1Parser.VARNAME)
            self.state = 33
            self.eqStatement()
            self.state = 34
            self.value(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D1Parser.RULE_eqStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqStatement" ):
                listener.enterEqStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqStatement" ):
                listener.exitEqStatement(self)




    def eqStatement(self):

        localctx = D1Parser.EqStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_eqStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(D1Parser.NUMBER, 0)

        def STRING(self):
            return self.getToken(D1Parser.STRING, 0)

        def array(self):
            return self.getTypedRuleContext(D1Parser.ArrayContext,0)


        def VARNAME(self):
            return self.getToken(D1Parser.VARNAME, 0)

        def boolean(self):
            return self.getTypedRuleContext(D1Parser.BooleanContext,0)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D1Parser.ValueContext)
            else:
                return self.getTypedRuleContext(D1Parser.ValueContext,i)


        def arithSymbol(self):
            return self.getTypedRuleContext(D1Parser.ArithSymbolContext,0)


        def getRuleIndex(self):
            return D1Parser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)



    def value(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D1Parser.ValueContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_value, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 39
                self.match(D1Parser.NUMBER)
                pass
            elif token in [22]:
                self.state = 40
                self.match(D1Parser.STRING)
                pass
            elif token in [8, 11]:
                self.state = 41
                self.array()
                pass
            elif token in [20]:
                self.state = 42
                self.match(D1Parser.VARNAME)
                pass
            elif token in [12, 13]:
                self.state = 43
                self.boolean()
                pass
            elif token in [6]:
                self.state = 44
                self.match(D1Parser.T__5)
                self.state = 45
                self.value(0)
                self.state = 46
                self.match(D1Parser.T__6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D1Parser.ValueContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_value)
                    self.state = 50
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 51
                    self.arithSymbol()
                    self.state = 52
                    self.value(3) 
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D1Parser.ValueContext)
            else:
                return self.getTypedRuleContext(D1Parser.ValueContext,i)


        def getRuleIndex(self):
            return D1Parser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = D1Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(D1Parser.T__7)
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 60
                        self.value(0)
                        self.state = 61
                        self.match(D1Parser.T__8) 
                    self.state = 67
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                self.state = 68
                self.value(0)
                self.state = 69
                self.match(D1Parser.T__9)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(D1Parser.T__10)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D1Parser.RULE_boolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)




    def boolean(self):

        localctx = D1Parser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D1Parser.ValueContext)
            else:
                return self.getTypedRuleContext(D1Parser.ValueContext,i)


        def arithSymbol(self):
            return self.getTypedRuleContext(D1Parser.ArithSymbolContext,0)


        def getRuleIndex(self):
            return D1Parser.RULE_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)




    def arithmetic(self):

        localctx = D1Parser.ArithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arithmetic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.value(0)
            self.state = 77
            self.arithSymbol()
            self.state = 78
            self.value(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithSymbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D1Parser.RULE_arithSymbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithSymbol" ):
                listener.enterArithSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithSymbol" ):
                listener.exitArithSymbol(self)




    def arithSymbol(self):

        localctx = D1Parser.ArithSymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arithSymbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 507904) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.value_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def value_sempred(self, localctx:ValueContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




