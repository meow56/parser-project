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
        4,1,37,156,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,3,0,
        28,8,0,1,0,4,0,31,8,0,11,0,12,0,32,1,0,3,0,36,8,0,1,0,1,0,3,0,40,
        8,0,1,1,1,1,3,1,44,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,3,4,62,8,4,1,4,1,4,1,4,1,4,5,4,68,8,4,10,4,
        12,4,71,9,4,1,5,1,5,1,5,1,5,5,5,77,8,5,10,5,12,5,80,9,5,1,5,1,5,
        1,5,1,5,3,5,86,8,5,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,107,8,9,1,9,1,9,1,9,3,9,112,8,
        9,1,10,1,10,1,10,1,10,4,10,118,8,10,11,10,12,10,119,1,10,1,10,1,
        10,1,10,3,10,126,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,3,11,141,8,11,1,11,1,11,1,11,1,11,1,11,1,
        11,5,11,149,8,11,10,11,12,11,152,9,11,1,12,1,12,1,12,0,2,8,22,13,
        0,2,4,6,8,10,12,14,16,18,20,22,24,0,4,1,0,1,5,1,0,12,13,1,0,14,18,
        1,0,27,32,166,0,39,1,0,0,0,2,43,1,0,0,0,4,45,1,0,0,0,6,49,1,0,0,
        0,8,61,1,0,0,0,10,85,1,0,0,0,12,87,1,0,0,0,14,89,1,0,0,0,16,93,1,
        0,0,0,18,95,1,0,0,0,20,125,1,0,0,0,22,140,1,0,0,0,24,153,1,0,0,0,
        26,28,3,2,1,0,27,26,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,31,5,
        33,0,0,30,27,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,
        40,1,0,0,0,34,36,3,2,1,0,35,34,1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,
        0,37,40,5,0,0,1,38,40,3,18,9,0,39,30,1,0,0,0,39,35,1,0,0,0,39,38,
        1,0,0,0,40,1,1,0,0,0,41,44,3,4,2,0,42,44,3,8,4,0,43,41,1,0,0,0,43,
        42,1,0,0,0,44,3,1,0,0,0,45,46,5,34,0,0,46,47,3,6,3,0,47,48,3,8,4,
        0,48,5,1,0,0,0,49,50,7,0,0,0,50,7,1,0,0,0,51,52,6,4,-1,0,52,62,5,
        35,0,0,53,62,5,36,0,0,54,62,3,10,5,0,55,62,5,34,0,0,56,62,3,12,6,
        0,57,58,5,6,0,0,58,59,3,8,4,0,59,60,5,7,0,0,60,62,1,0,0,0,61,51,
        1,0,0,0,61,53,1,0,0,0,61,54,1,0,0,0,61,55,1,0,0,0,61,56,1,0,0,0,
        61,57,1,0,0,0,62,69,1,0,0,0,63,64,10,2,0,0,64,65,3,16,8,0,65,66,
        3,8,4,3,66,68,1,0,0,0,67,63,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,
        69,70,1,0,0,0,70,9,1,0,0,0,71,69,1,0,0,0,72,78,5,8,0,0,73,74,3,8,
        4,0,74,75,5,9,0,0,75,77,1,0,0,0,76,73,1,0,0,0,77,80,1,0,0,0,78,76,
        1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,78,1,0,0,0,81,82,3,8,4,0,
        82,83,5,10,0,0,83,86,1,0,0,0,84,86,5,11,0,0,85,72,1,0,0,0,85,84,
        1,0,0,0,86,11,1,0,0,0,87,88,7,1,0,0,88,13,1,0,0,0,89,90,3,8,4,0,
        90,91,3,16,8,0,91,92,3,8,4,0,92,15,1,0,0,0,93,94,7,2,0,0,94,17,1,
        0,0,0,95,96,5,19,0,0,96,97,3,22,11,0,97,98,5,20,0,0,98,99,5,33,0,
        0,99,106,3,20,10,0,100,101,5,21,0,0,101,102,3,22,11,0,102,103,5,
        20,0,0,103,104,5,33,0,0,104,105,3,20,10,0,105,107,1,0,0,0,106,100,
        1,0,0,0,106,107,1,0,0,0,107,111,1,0,0,0,108,109,5,22,0,0,109,110,
        5,33,0,0,110,112,3,20,10,0,111,108,1,0,0,0,111,112,1,0,0,0,112,19,
        1,0,0,0,113,114,5,23,0,0,114,115,3,2,1,0,115,116,5,33,0,0,116,118,
        1,0,0,0,117,113,1,0,0,0,118,119,1,0,0,0,119,117,1,0,0,0,119,120,
        1,0,0,0,120,126,1,0,0,0,121,122,5,23,0,0,122,123,3,2,1,0,123,124,
        5,0,0,1,124,126,1,0,0,0,125,117,1,0,0,0,125,121,1,0,0,0,126,21,1,
        0,0,0,127,128,6,11,-1,0,128,141,3,12,6,0,129,130,5,26,0,0,130,141,
        3,22,11,4,131,132,5,6,0,0,132,133,3,22,11,0,133,134,5,7,0,0,134,
        141,1,0,0,0,135,136,3,8,4,0,136,137,3,24,12,0,137,138,3,8,4,0,138,
        141,1,0,0,0,139,141,5,34,0,0,140,127,1,0,0,0,140,129,1,0,0,0,140,
        131,1,0,0,0,140,135,1,0,0,0,140,139,1,0,0,0,141,150,1,0,0,0,142,
        143,10,6,0,0,143,144,5,24,0,0,144,149,3,22,11,7,145,146,10,5,0,0,
        146,147,5,25,0,0,147,149,3,22,11,6,148,142,1,0,0,0,148,145,1,0,0,
        0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,23,1,0,0,0,
        152,150,1,0,0,0,153,154,7,3,0,0,154,25,1,0,0,0,16,27,32,35,39,43,
        61,69,78,85,106,111,119,125,140,148,150
    ]

class D1Parser ( Parser ):

    grammarFileName = "D1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'('", "')'", "'['", "','", "']'", "'[]'", "'True'", 
                     "'False'", "'+'", "'-'", "'*'", "'/'", "'%'", "'if'", 
                     "':'", "'elif'", "'else:'", "'\\t'", "'and'", "'or'", 
                     "'not'", "'=='", "'!='", "'>='", "'<='", "'>'", "'<'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NEWLINES", "VARNAME", "NUMBER", "STRING", 
                      "WS" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_eqStatement = 3
    RULE_value = 4
    RULE_array = 5
    RULE_boolean = 6
    RULE_arithmetic = 7
    RULE_arithSymbol = 8
    RULE_conditional = 9
    RULE_block = 10
    RULE_boolExpr = 11
    RULE_comparisons = 12

    ruleNames =  [ "start", "statement", "assignment", "eqStatement", "value", 
                   "array", "boolean", "arithmetic", "arithSymbol", "conditional", 
                   "block", "boolExpr", "comparisons" ]

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
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    NEWLINES=33
    VARNAME=34
    NUMBER=35
    STRING=36
    WS=37

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

        def NEWLINES(self, i:int=None):
            if i is None:
                return self.getTokens(D1Parser.NEWLINES)
            else:
                return self.getToken(D1Parser.NEWLINES, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(D1Parser.StatementContext,i)


        def EOF(self):
            return self.getToken(D1Parser.EOF, 0)

        def conditional(self):
            return self.getTypedRuleContext(D1Parser.ConditionalContext,0)


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
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 120259098944) != 0):
                        self.state = 26
                        self.statement()


                    self.state = 29
                    self.match(D1Parser.NEWLINES)
                    self.state = 32 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 128849033536) != 0)):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 120259098944) != 0):
                    self.state = 34
                    self.statement()


                self.state = 37
                self.match(D1Parser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.conditional()
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
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
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
            self.state = 45
            self.match(D1Parser.VARNAME)
            self.state = 46
            self.eqStatement()
            self.state = 47
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
            self.state = 49
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
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.state = 52
                self.match(D1Parser.NUMBER)
                pass
            elif token in [36]:
                self.state = 53
                self.match(D1Parser.STRING)
                pass
            elif token in [8, 11]:
                self.state = 54
                self.array()
                pass
            elif token in [34]:
                self.state = 55
                self.match(D1Parser.VARNAME)
                pass
            elif token in [12, 13]:
                self.state = 56
                self.boolean()
                pass
            elif token in [6]:
                self.state = 57
                self.match(D1Parser.T__5)
                self.state = 58
                self.value(0)
                self.state = 59
                self.match(D1Parser.T__6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D1Parser.ValueContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_value)
                    self.state = 63
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 64
                    self.arithSymbol()
                    self.state = 65
                    self.value(3) 
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(D1Parser.T__7)
                self.state = 78
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 73
                        self.value(0)
                        self.state = 74
                        self.match(D1Parser.T__8) 
                    self.state = 80
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                self.state = 81
                self.value(0)
                self.state = 82
                self.match(D1Parser.T__9)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
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
            self.state = 87
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
            self.state = 89
            self.value(0)
            self.state = 90
            self.arithSymbol()
            self.state = 91
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
            self.state = 93
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


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D1Parser.BoolExprContext)
            else:
                return self.getTypedRuleContext(D1Parser.BoolExprContext,i)


        def NEWLINES(self, i:int=None):
            if i is None:
                return self.getTokens(D1Parser.NEWLINES)
            else:
                return self.getToken(D1Parser.NEWLINES, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D1Parser.BlockContext)
            else:
                return self.getTypedRuleContext(D1Parser.BlockContext,i)


        def getRuleIndex(self):
            return D1Parser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)




    def conditional(self):

        localctx = D1Parser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(D1Parser.T__18)
            self.state = 96
            self.boolExpr(0)
            self.state = 97
            self.match(D1Parser.T__19)
            self.state = 98
            self.match(D1Parser.NEWLINES)
            self.state = 99
            self.block()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 100
                self.match(D1Parser.T__20)
                self.state = 101
                self.boolExpr(0)
                self.state = 102
                self.match(D1Parser.T__19)
                self.state = 103
                self.match(D1Parser.NEWLINES)
                self.state = 104
                self.block()


            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 108
                self.match(D1Parser.T__21)
                self.state = 109
                self.match(D1Parser.NEWLINES)
                self.state = 110
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(D1Parser.StatementContext,i)


        def NEWLINES(self, i:int=None):
            if i is None:
                return self.getTokens(D1Parser.NEWLINES)
            else:
                return self.getToken(D1Parser.NEWLINES, i)

        def EOF(self):
            return self.getToken(D1Parser.EOF, 0)

        def getRuleIndex(self):
            return D1Parser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = D1Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 113
                    self.match(D1Parser.T__22)
                    self.state = 114
                    self.statement()
                    self.state = 115
                    self.match(D1Parser.NEWLINES)
                    self.state = 119 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==23):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.match(D1Parser.T__22)
                self.state = 122
                self.statement()
                self.state = 123
                self.match(D1Parser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean(self):
            return self.getTypedRuleContext(D1Parser.BooleanContext,0)


        def boolExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D1Parser.BoolExprContext)
            else:
                return self.getTypedRuleContext(D1Parser.BoolExprContext,i)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D1Parser.ValueContext)
            else:
                return self.getTypedRuleContext(D1Parser.ValueContext,i)


        def comparisons(self):
            return self.getTypedRuleContext(D1Parser.ComparisonsContext,0)


        def VARNAME(self):
            return self.getToken(D1Parser.VARNAME, 0)

        def getRuleIndex(self):
            return D1Parser.RULE_boolExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpr" ):
                listener.enterBoolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpr" ):
                listener.exitBoolExpr(self)



    def boolExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D1Parser.BoolExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_boolExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 128
                self.boolean()
                pass

            elif la_ == 2:
                self.state = 129
                self.match(D1Parser.T__25)
                self.state = 130
                self.boolExpr(4)
                pass

            elif la_ == 3:
                self.state = 131
                self.match(D1Parser.T__5)
                self.state = 132
                self.boolExpr(0)
                self.state = 133
                self.match(D1Parser.T__6)
                pass

            elif la_ == 4:
                self.state = 135
                self.value(0)
                self.state = 136
                self.comparisons()
                self.state = 137
                self.value(0)
                pass

            elif la_ == 5:
                self.state = 139
                self.match(D1Parser.VARNAME)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 148
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = D1Parser.BoolExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                        self.state = 142
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 143
                        self.match(D1Parser.T__23)
                        self.state = 144
                        self.boolExpr(7)
                        pass

                    elif la_ == 2:
                        localctx = D1Parser.BoolExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                        self.state = 145
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 146
                        self.match(D1Parser.T__24)
                        self.state = 147
                        self.boolExpr(6)
                        pass

             
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparisonsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D1Parser.RULE_comparisons

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisons" ):
                listener.enterComparisons(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisons" ):
                listener.exitComparisons(self)




    def comparisons(self):

        localctx = D1Parser.ComparisonsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comparisons)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8455716864) != 0)):
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
        self._predicates[11] = self.boolExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def value_sempred(self, localctx:ValueContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def boolExpr_sempred(self, localctx:BoolExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




