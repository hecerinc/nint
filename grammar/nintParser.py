# Generated from nint.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


import sys
sys.path.append("C:/dev/compiler")
from icg.Node import Node
from icg.Expr import Expr
from icg.Op import Op
from icg.Arith import Arith
from icg.Stmt import Stmt
from icg.Seq import Seq


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\u0110\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\7\2-\n\2\f\2\16\2\60\13\2")
        buf.write("\3\2\7\2\63\n\2\f\2\16\2\66\13\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3A\n\3\3\4\3\4\7\4E\n\4\f\4\16\4H\13")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5T\n\5\3")
        buf.write("\5\3\5\3\5\5\5Y\n\5\3\5\3\5\5\5]\n\5\3\5\3\5\5\5a\n\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5m\n\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5v\n\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6\u0082\n\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\5\6\u00a5\n\6\3\6\7\6\u00a8\n\6\f\6\16\6\u00ab\13")
        buf.write("\6\3\7\3\7\3\7\7\7\u00b0\n\7\f\7\16\7\u00b3\13\7\3\b\3")
        buf.write("\b\3\t\3\t\5\t\u00b9\n\t\3\n\6\n\u00bc\n\n\r\n\16\n\u00bd")
        buf.write("\3\n\3\n\5\n\u00c2\n\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\5\f\u00cb\n\f\3\r\3\r\5\r\u00cf\n\r\3\16\3\16\3\16\3")
        buf.write("\16\7\16\u00d5\n\16\f\16\16\16\u00d8\13\16\5\16\u00da")
        buf.write("\n\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\5\20\u00ea\n\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\7\21\u00f2\n\21\f\21\16\21\u00f5\13\21\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\5\23\u00fd\n\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\7\24\u0104\n\24\f\24\16\24\u0107\13\24")
        buf.write("\3\25\3\25\3\25\6\25\u010c\n\25\r\25\16\25\u010d\3\25")
        buf.write("\2\4\n \26\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&(\2\t\4\2$$88\4\2))\60\60\4\2%%\64\64\3\2,/\4\2**\61")
        buf.write("\61\5\2\16\16\24\26\30\32\6\2\4\5\7\b\r\r\21\22\2\u0129")
        buf.write("\2\64\3\2\2\2\4@\3\2\2\2\6B\3\2\2\2\bu\3\2\2\2\n\u0081")
        buf.write("\3\2\2\2\f\u00ac\3\2\2\2\16\u00b4\3\2\2\2\20\u00b8\3\2")
        buf.write("\2\2\22\u00bb\3\2\2\2\24\u00c3\3\2\2\2\26\u00c7\3\2\2")
        buf.write("\2\30\u00ce\3\2\2\2\32\u00d0\3\2\2\2\34\u00dd\3\2\2\2")
        buf.write("\36\u00e6\3\2\2\2 \u00eb\3\2\2\2\"\u00f6\3\2\2\2$\u00f9")
        buf.write("\3\2\2\2&\u0100\3\2\2\2(\u0108\3\2\2\2*.\5\b\5\2+-\t\2")
        buf.write("\2\2,+\3\2\2\2-\60\3\2\2\2.,\3\2\2\2./\3\2\2\2/\63\3\2")
        buf.write("\2\2\60.\3\2\2\2\61\63\78\2\2\62*\3\2\2\2\62\61\3\2\2")
        buf.write("\2\63\66\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\67\3\2")
        buf.write("\2\2\66\64\3\2\2\2\678\b\2\1\289\7\2\2\39\3\3\2\2\2:;")
        buf.write("\7\37\2\2;<\5\n\6\2<=\7#\2\2=A\3\2\2\2>A\5\16\b\2?A\7")
        buf.write("\26\2\2@:\3\2\2\2@>\3\2\2\2@?\3\2\2\2A\5\3\2\2\2BF\7\35")
        buf.write("\2\2CE\5\b\5\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2")
        buf.write("GI\3\2\2\2HF\3\2\2\2IJ\7 \2\2J\7\3\2\2\2Kv\5\6\4\2LM\7")
        buf.write("\13\2\2MN\7\37\2\2NO\5\n\6\2OP\7#\2\2PS\5\6\4\2QR\7\6")
        buf.write("\2\2RT\5\6\4\2SQ\3\2\2\2ST\3\2\2\2Tv\3\2\2\2UV\7\t\2\2")
        buf.write("VX\7\37\2\2WY\5\20\t\2XW\3\2\2\2XY\3\2\2\2YZ\3\2\2\2Z")
        buf.write("\\\7$\2\2[]\5\n\6\2\\[\3\2\2\2\\]\3\2\2\2]^\3\2\2\2^`")
        buf.write("\7$\2\2_a\5\f\7\2`_\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\7#\2")
        buf.write("\2cv\5\6\4\2de\7\23\2\2ef\7\37\2\2fg\5\n\6\2gh\7#\2\2")
        buf.write("hi\5\6\4\2iv\3\2\2\2jl\7\20\2\2km\5\n\6\2lk\3\2\2\2lm")
        buf.write("\3\2\2\2mn\3\2\2\2nv\7$\2\2op\5\n\6\2pq\7$\2\2qr\b\5\1")
        buf.write("\2rv\3\2\2\2sv\5\34\17\2tv\5\24\13\2uK\3\2\2\2uL\3\2\2")
        buf.write("\2uU\3\2\2\2ud\3\2\2\2uj\3\2\2\2uo\3\2\2\2us\3\2\2\2u")
        buf.write("t\3\2\2\2v\t\3\2\2\2wx\b\6\1\2xy\5\4\3\2yz\b\6\1\2z\u0082")
        buf.write("\3\2\2\2{\u0082\5$\23\2|\u0082\5(\25\2}~\7\64\2\2~\u0082")
        buf.write("\5\n\6\f\177\u0080\7(\2\2\u0080\u0082\5\n\6\13\u0081w")
        buf.write("\3\2\2\2\u0081{\3\2\2\2\u0081|\3\2\2\2\u0081}\3\2\2\2")
        buf.write("\u0081\177\3\2\2\2\u0082\u00a9\3\2\2\2\u0083\u0084\f\n")
        buf.write("\2\2\u0084\u0085\t\3\2\2\u0085\u0086\5\n\6\13\u0086\u0087")
        buf.write("\b\6\1\2\u0087\u00a8\3\2\2\2\u0088\u0089\f\t\2\2\u0089")
        buf.write("\u008a\t\4\2\2\u008a\u008b\5\n\6\n\u008b\u008c\b\6\1\2")
        buf.write("\u008c\u00a8\3\2\2\2\u008d\u008e\f\b\2\2\u008e\u008f\t")
        buf.write("\5\2\2\u008f\u00a8\5\n\6\t\u0090\u0091\f\7\2\2\u0091\u0092")
        buf.write("\t\6\2\2\u0092\u00a8\5\n\6\b\u0093\u0094\f\6\2\2\u0094")
        buf.write("\u0095\7+\2\2\u0095\u00a8\5\n\6\6\u0096\u0097\f\5\2\2")
        buf.write("\u0097\u0098\7&\2\2\u0098\u00a8\5\n\6\6\u0099\u009a\f")
        buf.write("\4\2\2\u009a\u009b\7\62\2\2\u009b\u00a8\5\n\6\5\u009c")
        buf.write("\u009d\f\3\2\2\u009d\u009e\7\'\2\2\u009e\u00a8\5\n\6\3")
        buf.write("\u009f\u00a0\f\17\2\2\u00a0\u00a4\7\36\2\2\u00a1\u00a5")
        buf.write("\5\n\6\2\u00a2\u00a5\5\22\n\2\u00a3\u00a5\7\3\2\2\u00a4")
        buf.write("\u00a1\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2")
        buf.write("\u00a5\u00a6\3\2\2\2\u00a6\u00a8\7!\2\2\u00a7\u0083\3")
        buf.write("\2\2\2\u00a7\u0088\3\2\2\2\u00a7\u008d\3\2\2\2\u00a7\u0090")
        buf.write("\3\2\2\2\u00a7\u0093\3\2\2\2\u00a7\u0096\3\2\2\2\u00a7")
        buf.write("\u0099\3\2\2\2\u00a7\u009c\3\2\2\2\u00a7\u009f\3\2\2\2")
        buf.write("\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3")
        buf.write("\2\2\2\u00aa\13\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00b1")
        buf.write("\5\n\6\2\u00ad\u00ae\7\33\2\2\u00ae\u00b0\5\n\6\2\u00af")
        buf.write("\u00ad\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b1\u00b2\3\2\2\2\u00b2\r\3\2\2\2\u00b3\u00b1\3\2\2")
        buf.write("\2\u00b4\u00b5\t\7\2\2\u00b5\17\3\2\2\2\u00b6\u00b9\5")
        buf.write("\24\13\2\u00b7\u00b9\5\f\7\2\u00b8\u00b6\3\2\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9\21\3\2\2\2\u00ba\u00bc\7\27\2\2\u00bb")
        buf.write("\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00bb\3\2\2\2")
        buf.write("\u00bd\u00be\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00c0\7")
        buf.write("\33\2\2\u00c0\u00c2\5\22\n\2\u00c1\u00bf\3\2\2\2\u00c1")
        buf.write("\u00c2\3\2\2\2\u00c2\23\3\2\2\2\u00c3\u00c4\5\36\20\2")
        buf.write("\u00c4\u00c5\5\26\f\2\u00c5\u00c6\7$\2\2\u00c6\25\3\2")
        buf.write("\2\2\u00c7\u00ca\7\26\2\2\u00c8\u00c9\7\'\2\2\u00c9\u00cb")
        buf.write("\5\30\r\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb")
        buf.write("\27\3\2\2\2\u00cc\u00cf\5\32\16\2\u00cd\u00cf\5\n\6\2")
        buf.write("\u00ce\u00cc\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf\31\3\2")
        buf.write("\2\2\u00d0\u00d9\7\36\2\2\u00d1\u00d6\5\30\r\2\u00d2\u00d3")
        buf.write("\7\33\2\2\u00d3\u00d5\5\30\r\2\u00d4\u00d2\3\2\2\2\u00d5")
        buf.write("\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2")
        buf.write("\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00d1\3")
        buf.write("\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dc")
        buf.write("\7!\2\2\u00dc\33\3\2\2\2\u00dd\u00de\7\n\2\2\u00de\u00df")
        buf.write("\7\26\2\2\u00df\u00e0\7\37\2\2\u00e0\u00e1\5 \21\2\u00e1")
        buf.write("\u00e2\7#\2\2\u00e2\u00e3\7\"\2\2\u00e3\u00e4\5\36\20")
        buf.write("\2\u00e4\u00e5\5\6\4\2\u00e5\35\3\2\2\2\u00e6\u00e9\t")
        buf.write("\b\2\2\u00e7\u00e8\7\36\2\2\u00e8\u00ea\7!\2\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\37\3\2\2\2\u00eb\u00ec")
        buf.write("\b\21\1\2\u00ec\u00ed\5\"\22\2\u00ed\u00f3\3\2\2\2\u00ee")
        buf.write("\u00ef\f\3\2\2\u00ef\u00f0\7\33\2\2\u00f0\u00f2\5\"\22")
        buf.write("\2\u00f1\u00ee\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1")
        buf.write("\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4!\3\2\2\2\u00f5\u00f3")
        buf.write("\3\2\2\2\u00f6\u00f7\5\36\20\2\u00f7\u00f8\7\26\2\2\u00f8")
        buf.write("#\3\2\2\2\u00f9\u00fa\7\26\2\2\u00fa\u00fc\7\37\2\2\u00fb")
        buf.write("\u00fd\5&\24\2\u00fc\u00fb\3\2\2\2\u00fc\u00fd\3\2\2\2")
        buf.write("\u00fd\u00fe\3\2\2\2\u00fe\u00ff\7#\2\2\u00ff%\3\2\2\2")
        buf.write("\u0100\u0105\5\n\6\2\u0101\u0102\7\33\2\2\u0102\u0104")
        buf.write("\5\n\6\2\u0103\u0101\3\2\2\2\u0104\u0107\3\2\2\2\u0105")
        buf.write("\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106\'\3\2\2\2\u0107")
        buf.write("\u0105\3\2\2\2\u0108\u010b\5$\23\2\u0109\u010a\7\63\2")
        buf.write("\2\u010a\u010c\5$\23\2\u010b\u0109\3\2\2\2\u010c\u010d")
        buf.write("\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e")
        buf.write(")\3\2\2\2\36.\62\64@FSX\\`lu\u0081\u00a4\u00a7\u00a9\u00b1")
        buf.write("\u00b8\u00bd\u00c1\u00ca\u00ce\u00d6\u00d9\u00e9\u00f3")
        buf.write("\u00fc\u0105\u010d")
        return buf.getvalue()


class nintParser ( Parser ):

    grammarFileName = "nint.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'bool'", "'data.frame'", "'else'",
                     "'factor'", "'float'", "'for'", "'function'", "'if'",
                     "'input'", "'int'", "'null'", "'print'", "'return'",
                     "'string'", "'void'", "'while'", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "','", "'.'", "'{'", "'['", "'('", "'}'",
                     "']'", "'::'", "')'", "';'", "'+'", "'&&'", "'='",
                     "'!'", "'/'", "'=='", "'**'", "'>'", "'>='", "'<='",
                     "'<'", "'*'", "'!='", "'||'", "'>>'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BOOL", "DF", "ELSE", "FACTOR",
                      "FLOAT", "FOR", "FUN", "IF", "INPUT", "INT", "NULL",
                      "PRINT", "RETURN", "STRING", "VOID", "WHILE", "BOOL_LITERAL",
                      "FLOAT_LITERAL", "ID", "DIGIT", "INT_LITERAL", "RANGE",
                      "STRING_LITERAL", "COMMA", "DOT", "LBRACE", "LBRACK",
                      "LPAREN", "RBRACE", "RBRACK", "RETURNSTYPE", "RPAREN",
                      "SEMICOLON", "ADD", "AND", "ASSIGN", "BANG", "DIV",
                      "EQUAL", "EXP", "GT", "GTE", "LE", "LTE", "MUL", "NOTEQUAL",
                      "OR", "PIPE", "SUB", "COMMENT", "LINE_COMMENT", "WS",
                      "NL" ]

    RULE_prog = 0
    RULE_primary = 1
    RULE_block = 2
    RULE_statement = 3
    RULE_expression = 4
    RULE_expressionList = 5
    RULE_literal = 6
    RULE_forInit = 7
    RULE_indexList = 8
    RULE_declaration = 9
    RULE_declarator = 10
    RULE_initalizer = 11
    RULE_vectorInitializer = 12
    RULE_functionDeclaration = 13
    RULE_typeSpecifier = 14
    RULE_parameterList = 15
    RULE_parameterDeclaration = 16
    RULE_functionCall = 17
    RULE_callArgs = 18
    RULE_pipeStmt = 19

    ruleNames =  [ "prog", "primary", "block", "statement", "expression",
                   "expressionList", "literal", "forInit", "indexList",
                   "declaration", "declarator", "initalizer", "vectorInitializer",
                   "functionDeclaration", "typeSpecifier", "parameterList",
                   "parameterDeclaration", "functionCall", "callArgs", "pipeStmt" ]

    EOF = Token.EOF
    T__0=1
    BOOL=2
    DF=3
    ELSE=4
    FACTOR=5
    FLOAT=6
    FOR=7
    FUN=8
    IF=9
    INPUT=10
    INT=11
    NULL=12
    PRINT=13
    RETURN=14
    STRING=15
    VOID=16
    WHILE=17
    BOOL_LITERAL=18
    FLOAT_LITERAL=19
    ID=20
    DIGIT=21
    INT_LITERAL=22
    RANGE=23
    STRING_LITERAL=24
    COMMA=25
    DOT=26
    LBRACE=27
    LBRACK=28
    LPAREN=29
    RBRACE=30
    RBRACK=31
    RETURNSTYPE=32
    RPAREN=33
    SEMICOLON=34
    ADD=35
    AND=36
    ASSIGN=37
    BANG=38
    DIV=39
    EQUAL=40
    EXP=41
    GT=42
    GTE=43
    LE=44
    LTE=45
    MUL=46
    NOTEQUAL=47
    OR=48
    PIPE=49
    SUB=50
    COMMENT=51
    LINE_COMMENT=52
    WS=53
    NL=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self._statement = None # StatementContext
            self.stats = list() # of StatementContexts

        def EOF(self):
            return self.getToken(nintParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(nintParser.NL)
            else:
                return self.getToken(nintParser.NL, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nintParser.StatementContext)
            else:
                return self.getTypedRuleContext(nintParser.StatementContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(nintParser.SEMICOLON)
            else:
                return self.getToken(nintParser.SEMICOLON, i)

        def getRuleIndex(self):
            return nintParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = nintParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)

        s = None

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << nintParser.BOOL) | (1 << nintParser.DF) | (1 << nintParser.FACTOR) | (1 << nintParser.FLOAT) | (1 << nintParser.FOR) | (1 << nintParser.FUN) | (1 << nintParser.IF) | (1 << nintParser.INT) | (1 << nintParser.NULL) | (1 << nintParser.RETURN) | (1 << nintParser.STRING) | (1 << nintParser.VOID) | (1 << nintParser.WHILE) | (1 << nintParser.BOOL_LITERAL) | (1 << nintParser.FLOAT_LITERAL) | (1 << nintParser.ID) | (1 << nintParser.INT_LITERAL) | (1 << nintParser.RANGE) | (1 << nintParser.STRING_LITERAL) | (1 << nintParser.LBRACE) | (1 << nintParser.LPAREN) | (1 << nintParser.BANG) | (1 << nintParser.SUB) | (1 << nintParser.NL))) != 0):
                self.state = 48
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [nintParser.BOOL, nintParser.DF, nintParser.FACTOR, nintParser.FLOAT, nintParser.FOR, nintParser.FUN, nintParser.IF, nintParser.INT, nintParser.NULL, nintParser.RETURN, nintParser.STRING, nintParser.VOID, nintParser.WHILE, nintParser.BOOL_LITERAL, nintParser.FLOAT_LITERAL, nintParser.ID, nintParser.INT_LITERAL, nintParser.RANGE, nintParser.STRING_LITERAL, nintParser.LBRACE, nintParser.LPAREN, nintParser.BANG, nintParser.SUB]:
                    self.state = 40
                    localctx._statement = self.statement()
                    localctx.stats.append(localctx._statement)
                    self.state = 44
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 41
                            _la = self._input.LA(1)
                            if not(_la==nintParser.SEMICOLON or _la==nintParser.NL):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()
                        self.state = 46
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                    pass
                elif token in [nintParser.NL]:
                    self.state = 47
                    self.match(nintParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            localctx.s = Seq(list(map(lambda x: x.stmt, localctx.stats)))
            self.state = 54
            self.match(nintParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(nintParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(nintParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(nintParser.RPAREN, 0)

        def literal(self):
            return self.getTypedRuleContext(nintParser.LiteralContext,0)


        def ID(self):
            return self.getToken(nintParser.ID, 0)

        def getRuleIndex(self):
            return nintParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = nintParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_primary)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(nintParser.LPAREN)
                self.state = 57
                self.expression(0)
                self.state = 58
                self.match(nintParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(nintParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(nintParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(nintParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nintParser.StatementContext)
            else:
                return self.getTypedRuleContext(nintParser.StatementContext,i)


        def getRuleIndex(self):
            return nintParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = nintParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(nintParser.LBRACE)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << nintParser.BOOL) | (1 << nintParser.DF) | (1 << nintParser.FACTOR) | (1 << nintParser.FLOAT) | (1 << nintParser.FOR) | (1 << nintParser.FUN) | (1 << nintParser.IF) | (1 << nintParser.INT) | (1 << nintParser.NULL) | (1 << nintParser.RETURN) | (1 << nintParser.STRING) | (1 << nintParser.VOID) | (1 << nintParser.WHILE) | (1 << nintParser.BOOL_LITERAL) | (1 << nintParser.FLOAT_LITERAL) | (1 << nintParser.ID) | (1 << nintParser.INT_LITERAL) | (1 << nintParser.RANGE) | (1 << nintParser.STRING_LITERAL) | (1 << nintParser.LBRACE) | (1 << nintParser.LPAREN) | (1 << nintParser.BANG) | (1 << nintParser.SUB))) != 0):
                self.state = 65
                self.statement()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(nintParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.stmt = None
            self.exp = None # ExpressionContext

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nintParser.BlockContext)
            else:
                return self.getTypedRuleContext(nintParser.BlockContext,i)


        def IF(self):
            return self.getToken(nintParser.IF, 0)

        def LPAREN(self):
            return self.getToken(nintParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(nintParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(nintParser.RPAREN, 0)

        def ELSE(self):
            return self.getToken(nintParser.ELSE, 0)

        def FOR(self):
            return self.getToken(nintParser.FOR, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(nintParser.SEMICOLON)
            else:
                return self.getToken(nintParser.SEMICOLON, i)

        def forInit(self):
            return self.getTypedRuleContext(nintParser.ForInitContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(nintParser.ExpressionListContext,0)


        def WHILE(self):
            return self.getToken(nintParser.WHILE, 0)

        def RETURN(self):
            return self.getToken(nintParser.RETURN, 0)

        def functionDeclaration(self):
            return self.getTypedRuleContext(nintParser.FunctionDeclarationContext,0)


        def declaration(self):
            return self.getTypedRuleContext(nintParser.DeclarationContext,0)


        def getRuleIndex(self):
            return nintParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = nintParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)

        stmt = None

        self._la = 0 # Token type
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [nintParser.LBRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.block()
                pass
            elif token in [nintParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(nintParser.IF)
                self.state = 75
                self.match(nintParser.LPAREN)
                self.state = 76
                self.expression(0)
                self.state = 77
                self.match(nintParser.RPAREN)
                self.state = 78
                self.block()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==nintParser.ELSE:
                    self.state = 79
                    self.match(nintParser.ELSE)
                    self.state = 80
                    self.block()


                pass
            elif token in [nintParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.match(nintParser.FOR)
                self.state = 84
                self.match(nintParser.LPAREN)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << nintParser.BOOL) | (1 << nintParser.DF) | (1 << nintParser.FACTOR) | (1 << nintParser.FLOAT) | (1 << nintParser.INT) | (1 << nintParser.NULL) | (1 << nintParser.STRING) | (1 << nintParser.VOID) | (1 << nintParser.BOOL_LITERAL) | (1 << nintParser.FLOAT_LITERAL) | (1 << nintParser.ID) | (1 << nintParser.INT_LITERAL) | (1 << nintParser.RANGE) | (1 << nintParser.STRING_LITERAL) | (1 << nintParser.LPAREN) | (1 << nintParser.BANG) | (1 << nintParser.SUB))) != 0):
                    self.state = 85
                    self.forInit()


                self.state = 88
                self.match(nintParser.SEMICOLON)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << nintParser.NULL) | (1 << nintParser.BOOL_LITERAL) | (1 << nintParser.FLOAT_LITERAL) | (1 << nintParser.ID) | (1 << nintParser.INT_LITERAL) | (1 << nintParser.RANGE) | (1 << nintParser.STRING_LITERAL) | (1 << nintParser.LPAREN) | (1 << nintParser.BANG) | (1 << nintParser.SUB))) != 0):
                    self.state = 89
                    self.expression(0)


                self.state = 92
                self.match(nintParser.SEMICOLON)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << nintParser.NULL) | (1 << nintParser.BOOL_LITERAL) | (1 << nintParser.FLOAT_LITERAL) | (1 << nintParser.ID) | (1 << nintParser.INT_LITERAL) | (1 << nintParser.RANGE) | (1 << nintParser.STRING_LITERAL) | (1 << nintParser.LPAREN) | (1 << nintParser.BANG) | (1 << nintParser.SUB))) != 0):
                    self.state = 93
                    self.expressionList()


                self.state = 96
                self.match(nintParser.RPAREN)
                self.state = 97
                self.block()
                pass
            elif token in [nintParser.WHILE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.match(nintParser.WHILE)
                self.state = 99
                self.match(nintParser.LPAREN)
                self.state = 100
                self.expression(0)
                self.state = 101
                self.match(nintParser.RPAREN)
                self.state = 102
                self.block()
                pass
            elif token in [nintParser.RETURN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 104
                self.match(nintParser.RETURN)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << nintParser.NULL) | (1 << nintParser.BOOL_LITERAL) | (1 << nintParser.FLOAT_LITERAL) | (1 << nintParser.ID) | (1 << nintParser.INT_LITERAL) | (1 << nintParser.RANGE) | (1 << nintParser.STRING_LITERAL) | (1 << nintParser.LPAREN) | (1 << nintParser.BANG) | (1 << nintParser.SUB))) != 0):
                    self.state = 105
                    self.expression(0)


                self.state = 108
                self.match(nintParser.SEMICOLON)
                pass
            elif token in [nintParser.NULL, nintParser.BOOL_LITERAL, nintParser.FLOAT_LITERAL, nintParser.ID, nintParser.INT_LITERAL, nintParser.RANGE, nintParser.STRING_LITERAL, nintParser.LPAREN, nintParser.BANG, nintParser.SUB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 109
                localctx.exp = self.expression(0)
                self.state = 110
                self.match(nintParser.SEMICOLON)
                localctx.stmt = localctx.exp.result
                pass
            elif token in [nintParser.FUN]:
                self.enterOuterAlt(localctx, 7)
                self.state = 113
                self.functionDeclaration()
                pass
            elif token in [nintParser.BOOL, nintParser.DF, nintParser.FACTOR, nintParser.FLOAT, nintParser.INT, nintParser.STRING, nintParser.VOID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 114
                self.declaration()
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


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.a = None # ExpressionContext
            self._primary = None # PrimaryContext
            self.bop = None # Token
            self.b = None # ExpressionContext

        def primary(self):
            return self.getTypedRuleContext(nintParser.PrimaryContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(nintParser.FunctionCallContext,0)


        def pipeStmt(self):
            return self.getTypedRuleContext(nintParser.PipeStmtContext,0)


        def SUB(self):
            return self.getToken(nintParser.SUB, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nintParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(nintParser.ExpressionContext,i)


        def BANG(self):
            return self.getToken(nintParser.BANG, 0)

        def MUL(self):
            return self.getToken(nintParser.MUL, 0)

        def DIV(self):
            return self.getToken(nintParser.DIV, 0)

        def ADD(self):
            return self.getToken(nintParser.ADD, 0)

        def LE(self):
            return self.getToken(nintParser.LE, 0)

        def GTE(self):
            return self.getToken(nintParser.GTE, 0)

        def GT(self):
            return self.getToken(nintParser.GT, 0)

        def LTE(self):
            return self.getToken(nintParser.LTE, 0)

        def EQUAL(self):
            return self.getToken(nintParser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(nintParser.NOTEQUAL, 0)

        def EXP(self):
            return self.getToken(nintParser.EXP, 0)

        def AND(self):
            return self.getToken(nintParser.AND, 0)

        def OR(self):
            return self.getToken(nintParser.OR, 0)

        def ASSIGN(self):
            return self.getToken(nintParser.ASSIGN, 0)

        def LBRACK(self):
            return self.getToken(nintParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(nintParser.RBRACK, 0)

        def indexList(self):
            return self.getTypedRuleContext(nintParser.IndexListContext,0)


        def getRuleIndex(self):
            return nintParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = nintParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expression, _p)

        result = None

        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 118
                localctx._primary = self.primary()
                localctx.result = Expr((None if localctx._primary is None else self._input.getText((localctx._primary.start,localctx._primary.stop))), 'string')
                pass

            elif la_ == 2:
                self.state = 121
                self.functionCall()
                pass

            elif la_ == 3:
                self.state = 122
                self.pipeStmt()
                pass

            elif la_ == 4:
                self.state = 123
                self.match(nintParser.SUB)
                self.state = 124
                self.expression(10)
                pass

            elif la_ == 5:
                self.state = 125
                self.match(nintParser.BANG)
                self.state = 126
                self.expression(9)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 165
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = nintParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 129
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 130
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==nintParser.DIV or _la==nintParser.MUL):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 131
                        localctx.b = self.expression(9)
                        localctx.result = Arith((None if localctx.bop is None else localctx.bop.text), localctx.a.result, localctx.b.result)
                        pass

                    elif la_ == 2:
                        localctx = nintParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 134
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 135
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==nintParser.ADD or _la==nintParser.SUB):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 136
                        localctx.b = self.expression(8)
                        localctx.result = Arith((None if localctx.bop is None else localctx.bop.text), localctx.a.result, localctx.b.result);
                        pass

                    elif la_ == 3:
                        localctx = nintParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 139
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 140
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << nintParser.GT) | (1 << nintParser.GTE) | (1 << nintParser.LE) | (1 << nintParser.LTE))) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 141
                        self.expression(7)
                        pass

                    elif la_ == 4:
                        localctx = nintParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 142
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 143
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==nintParser.EQUAL or _la==nintParser.NOTEQUAL):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 144
                        self.expression(6)
                        pass

                    elif la_ == 5:
                        localctx = nintParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 145
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 146
                        localctx.bop = self.match(nintParser.EXP)
                        self.state = 147
                        self.expression(4)
                        pass

                    elif la_ == 6:
                        localctx = nintParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 148
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 149
                        localctx.bop = self.match(nintParser.AND)
                        self.state = 150
                        self.expression(4)
                        pass

                    elif la_ == 7:
                        localctx = nintParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 151
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 152
                        localctx.bop = self.match(nintParser.OR)
                        self.state = 153
                        self.expression(3)
                        pass

                    elif la_ == 8:
                        localctx = nintParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 154
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 155
                        self.match(nintParser.ASSIGN)
                        self.state = 156
                        self.expression(1)
                        pass

                    elif la_ == 9:
                        localctx = nintParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 157
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 158
                        self.match(nintParser.LBRACK)
                        self.state = 162
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [nintParser.NULL, nintParser.BOOL_LITERAL, nintParser.FLOAT_LITERAL, nintParser.ID, nintParser.INT_LITERAL, nintParser.RANGE, nintParser.STRING_LITERAL, nintParser.LPAREN, nintParser.BANG, nintParser.SUB]:
                            self.state = 159
                            self.expression(0)
                            pass
                        elif token in [nintParser.DIGIT]:
                            self.state = 160
                            self.indexList()
                            pass
                        elif token in [nintParser.T__0]:
                            self.state = 161
                            self.match(nintParser.T__0)
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 164
                        self.match(nintParser.RBRACK)
                        pass


                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nintParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(nintParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(nintParser.COMMA)
            else:
                return self.getToken(nintParser.COMMA, i)

        def getRuleIndex(self):
            return nintParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = nintParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.expression(0)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==nintParser.COMMA:
                self.state = 171
                self.match(nintParser.COMMA)
                self.state = 172
                self.expression(0)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(nintParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(nintParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(nintParser.STRING_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(nintParser.BOOL_LITERAL, 0)

        def RANGE(self):
            return self.getToken(nintParser.RANGE, 0)

        def NULL(self):
            return self.getToken(nintParser.NULL, 0)

        def ID(self):
            return self.getToken(nintParser.ID, 0)

        def getRuleIndex(self):
            return nintParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = nintParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << nintParser.NULL) | (1 << nintParser.BOOL_LITERAL) | (1 << nintParser.FLOAT_LITERAL) | (1 << nintParser.ID) | (1 << nintParser.INT_LITERAL) | (1 << nintParser.RANGE) | (1 << nintParser.STRING_LITERAL))) != 0)):
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


    class ForInitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(nintParser.DeclarationContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(nintParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return nintParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)




    def forInit(self):

        localctx = nintParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forInit)
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [nintParser.BOOL, nintParser.DF, nintParser.FACTOR, nintParser.FLOAT, nintParser.INT, nintParser.STRING, nintParser.VOID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.declaration()
                pass
            elif token in [nintParser.NULL, nintParser.BOOL_LITERAL, nintParser.FLOAT_LITERAL, nintParser.ID, nintParser.INT_LITERAL, nintParser.RANGE, nintParser.STRING_LITERAL, nintParser.LPAREN, nintParser.BANG, nintParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.expressionList()
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


    class IndexListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(nintParser.DIGIT)
            else:
                return self.getToken(nintParser.DIGIT, i)

        def COMMA(self):
            return self.getToken(nintParser.COMMA, 0)

        def indexList(self):
            return self.getTypedRuleContext(nintParser.IndexListContext,0)


        def getRuleIndex(self):
            return nintParser.RULE_indexList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexList" ):
                listener.enterIndexList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexList" ):
                listener.exitIndexList(self)




    def indexList(self):

        localctx = nintParser.IndexListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_indexList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 184
                self.match(nintParser.DIGIT)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==nintParser.DIGIT):
                    break

            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==nintParser.COMMA:
                self.state = 189
                self.match(nintParser.COMMA)
                self.state = 190
                self.indexList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(nintParser.TypeSpecifierContext,0)


        def declarator(self):
            return self.getTypedRuleContext(nintParser.DeclaratorContext,0)


        def SEMICOLON(self):
            return self.getToken(nintParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return nintParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = nintParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.typeSpecifier()
            self.state = 194
            self.declarator()
            self.state = 195
            self.match(nintParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nintParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(nintParser.ASSIGN, 0)

        def initalizer(self):
            return self.getTypedRuleContext(nintParser.InitalizerContext,0)


        def getRuleIndex(self):
            return nintParser.RULE_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarator" ):
                listener.enterDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarator" ):
                listener.exitDeclarator(self)




    def declarator(self):

        localctx = nintParser.DeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(nintParser.ID)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==nintParser.ASSIGN:
                self.state = 198
                self.match(nintParser.ASSIGN)
                self.state = 199
                self.initalizer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitalizerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vectorInitializer(self):
            return self.getTypedRuleContext(nintParser.VectorInitializerContext,0)


        def expression(self):
            return self.getTypedRuleContext(nintParser.ExpressionContext,0)


        def getRuleIndex(self):
            return nintParser.RULE_initalizer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitalizer" ):
                listener.enterInitalizer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitalizer" ):
                listener.exitInitalizer(self)




    def initalizer(self):

        localctx = nintParser.InitalizerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_initalizer)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [nintParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.vectorInitializer()
                pass
            elif token in [nintParser.NULL, nintParser.BOOL_LITERAL, nintParser.FLOAT_LITERAL, nintParser.ID, nintParser.INT_LITERAL, nintParser.RANGE, nintParser.STRING_LITERAL, nintParser.LPAREN, nintParser.BANG, nintParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.expression(0)
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


    class VectorInitializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(nintParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(nintParser.RBRACK, 0)

        def initalizer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nintParser.InitalizerContext)
            else:
                return self.getTypedRuleContext(nintParser.InitalizerContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(nintParser.COMMA)
            else:
                return self.getToken(nintParser.COMMA, i)

        def getRuleIndex(self):
            return nintParser.RULE_vectorInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVectorInitializer" ):
                listener.enterVectorInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVectorInitializer" ):
                listener.exitVectorInitializer(self)




    def vectorInitializer(self):

        localctx = nintParser.VectorInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_vectorInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(nintParser.LBRACK)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << nintParser.NULL) | (1 << nintParser.BOOL_LITERAL) | (1 << nintParser.FLOAT_LITERAL) | (1 << nintParser.ID) | (1 << nintParser.INT_LITERAL) | (1 << nintParser.RANGE) | (1 << nintParser.STRING_LITERAL) | (1 << nintParser.LBRACK) | (1 << nintParser.LPAREN) | (1 << nintParser.BANG) | (1 << nintParser.SUB))) != 0):
                self.state = 207
                self.initalizer()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==nintParser.COMMA:
                    self.state = 208
                    self.match(nintParser.COMMA)
                    self.state = 209
                    self.initalizer()
                    self.state = 214
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 217
            self.match(nintParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUN(self):
            return self.getToken(nintParser.FUN, 0)

        def ID(self):
            return self.getToken(nintParser.ID, 0)

        def LPAREN(self):
            return self.getToken(nintParser.LPAREN, 0)

        def parameterList(self):
            return self.getTypedRuleContext(nintParser.ParameterListContext,0)


        def RPAREN(self):
            return self.getToken(nintParser.RPAREN, 0)

        def RETURNSTYPE(self):
            return self.getToken(nintParser.RETURNSTYPE, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(nintParser.TypeSpecifierContext,0)


        def block(self):
            return self.getTypedRuleContext(nintParser.BlockContext,0)


        def getRuleIndex(self):
            return nintParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)




    def functionDeclaration(self):

        localctx = nintParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_functionDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(nintParser.FUN)
            self.state = 220
            self.match(nintParser.ID)
            self.state = 221
            self.match(nintParser.LPAREN)
            self.state = 222
            self.parameterList(0)
            self.state = 223
            self.match(nintParser.RPAREN)
            self.state = 224
            self.match(nintParser.RETURNSTYPE)
            self.state = 225
            self.typeSpecifier()
            self.state = 226
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(nintParser.STRING, 0)

        def VOID(self):
            return self.getToken(nintParser.VOID, 0)

        def INT(self):
            return self.getToken(nintParser.INT, 0)

        def FLOAT(self):
            return self.getToken(nintParser.FLOAT, 0)

        def DF(self):
            return self.getToken(nintParser.DF, 0)

        def FACTOR(self):
            return self.getToken(nintParser.FACTOR, 0)

        def BOOL(self):
            return self.getToken(nintParser.BOOL, 0)

        def LBRACK(self):
            return self.getToken(nintParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(nintParser.RBRACK, 0)

        def getRuleIndex(self):
            return nintParser.RULE_typeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpecifier" ):
                listener.enterTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpecifier" ):
                listener.exitTypeSpecifier(self)




    def typeSpecifier(self):

        localctx = nintParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << nintParser.BOOL) | (1 << nintParser.DF) | (1 << nintParser.FACTOR) | (1 << nintParser.FLOAT) | (1 << nintParser.INT) | (1 << nintParser.STRING) | (1 << nintParser.VOID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==nintParser.LBRACK:
                self.state = 229
                self.match(nintParser.LBRACK)
                self.state = 230
                self.match(nintParser.RBRACK)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterDeclaration(self):
            return self.getTypedRuleContext(nintParser.ParameterDeclarationContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(nintParser.ParameterListContext,0)


        def COMMA(self):
            return self.getToken(nintParser.COMMA, 0)

        def getRuleIndex(self):
            return nintParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)



    def parameterList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = nintParser.ParameterListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_parameterList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.parameterDeclaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = nintParser.ParameterListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterList)
                    self.state = 236
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 237
                    self.match(nintParser.COMMA)
                    self.state = 238
                    self.parameterDeclaration()
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ParameterDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(nintParser.TypeSpecifierContext,0)


        def ID(self):
            return self.getToken(nintParser.ID, 0)

        def getRuleIndex(self):
            return nintParser.RULE_parameterDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterDeclaration" ):
                listener.enterParameterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterDeclaration" ):
                listener.exitParameterDeclaration(self)




    def parameterDeclaration(self):

        localctx = nintParser.ParameterDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_parameterDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.typeSpecifier()
            self.state = 245
            self.match(nintParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nintParser.ID, 0)

        def LPAREN(self):
            return self.getToken(nintParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(nintParser.RPAREN, 0)

        def callArgs(self):
            return self.getTypedRuleContext(nintParser.CallArgsContext,0)


        def getRuleIndex(self):
            return nintParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = nintParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(nintParser.ID)
            self.state = 248
            self.match(nintParser.LPAREN)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << nintParser.NULL) | (1 << nintParser.BOOL_LITERAL) | (1 << nintParser.FLOAT_LITERAL) | (1 << nintParser.ID) | (1 << nintParser.INT_LITERAL) | (1 << nintParser.RANGE) | (1 << nintParser.STRING_LITERAL) | (1 << nintParser.LPAREN) | (1 << nintParser.BANG) | (1 << nintParser.SUB))) != 0):
                self.state = 249
                self.callArgs()


            self.state = 252
            self.match(nintParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nintParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(nintParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(nintParser.COMMA)
            else:
                return self.getToken(nintParser.COMMA, i)

        def getRuleIndex(self):
            return nintParser.RULE_callArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallArgs" ):
                listener.enterCallArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallArgs" ):
                listener.exitCallArgs(self)




    def callArgs(self):

        localctx = nintParser.CallArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_callArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.expression(0)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==nintParser.COMMA:
                self.state = 255
                self.match(nintParser.COMMA)
                self.state = 256
                self.expression(0)
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PipeStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nintParser.FunctionCallContext)
            else:
                return self.getTypedRuleContext(nintParser.FunctionCallContext,i)


        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(nintParser.PIPE)
            else:
                return self.getToken(nintParser.PIPE, i)

        def getRuleIndex(self):
            return nintParser.RULE_pipeStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipeStmt" ):
                listener.enterPipeStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipeStmt" ):
                listener.exitPipeStmt(self)




    def pipeStmt(self):

        localctx = nintParser.PipeStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_pipeStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.functionCall()
            self.state = 265
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 263
                    self.match(nintParser.PIPE)
                    self.state = 264
                    self.functionCall()

                else:
                    raise NoViableAltException(self)
                self.state = 267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        self._predicates[4] = self.expression_sempred
        self._predicates[15] = self.parameterList_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)


            if predIndex == 1:
                return self.precpred(self._ctx, 7)


            if predIndex == 2:
                return self.precpred(self._ctx, 6)


            if predIndex == 3:
                return self.precpred(self._ctx, 5)


            if predIndex == 4:
                return self.precpred(self._ctx, 4)


            if predIndex == 5:
                return self.precpred(self._ctx, 3)


            if predIndex == 6:
                return self.precpred(self._ctx, 2)


            if predIndex == 7:
                return self.precpred(self._ctx, 1)


            if predIndex == 8:
                return self.precpred(self._ctx, 13)


    def parameterList_sempred(self, localctx:ParameterListContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 1)





