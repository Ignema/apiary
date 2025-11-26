# Generated from apiary/parser/grammar/RestAPIParser.g4 by ANTLR 4.13.1
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
        4,1,39,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,1,
        0,5,0,29,8,0,10,0,12,0,32,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,53,8,3,10,3,12,3,56,
        9,3,1,3,1,3,1,4,1,4,1,4,1,4,5,4,64,8,4,10,4,12,4,67,9,4,1,4,1,4,
        3,4,71,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,82,8,5,1,6,1,
        6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,95,8,8,1,9,1,9,1,9,0,0,
        10,0,2,4,6,8,10,12,14,16,18,0,4,1,0,15,16,1,0,22,24,1,0,25,28,1,
        0,10,14,100,0,20,1,0,0,0,2,35,1,0,0,0,4,44,1,0,0,0,6,46,1,0,0,0,
        8,59,1,0,0,0,10,81,1,0,0,0,12,83,1,0,0,0,14,85,1,0,0,0,16,87,1,0,
        0,0,18,96,1,0,0,0,20,24,3,2,1,0,21,23,3,6,3,0,22,21,1,0,0,0,23,26,
        1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,30,1,0,0,0,26,24,1,0,0,0,
        27,29,3,16,8,0,28,27,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,
        0,0,0,31,33,1,0,0,0,32,30,1,0,0,0,33,34,5,0,0,1,34,1,1,0,0,0,35,
        36,5,1,0,0,36,37,5,28,0,0,37,38,5,6,0,0,38,39,5,28,0,0,39,40,5,7,
        0,0,40,41,5,28,0,0,41,42,5,5,0,0,42,43,3,4,2,0,43,3,1,0,0,0,44,45,
        7,0,0,0,45,5,1,0,0,0,46,47,5,2,0,0,47,48,5,29,0,0,48,49,5,4,0,0,
        49,50,5,28,0,0,50,54,5,30,0,0,51,53,3,8,4,0,52,51,1,0,0,0,53,56,
        1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,57,1,0,0,0,56,54,1,0,0,0,
        57,58,5,31,0,0,58,7,1,0,0,0,59,60,5,29,0,0,60,61,5,34,0,0,61,65,
        3,10,5,0,62,64,3,12,6,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,
        0,65,66,1,0,0,0,66,70,1,0,0,0,67,65,1,0,0,0,68,69,5,8,0,0,69,71,
        3,14,7,0,70,68,1,0,0,0,70,71,1,0,0,0,71,9,1,0,0,0,72,82,5,17,0,0,
        73,82,5,18,0,0,74,82,5,19,0,0,75,82,5,20,0,0,76,82,5,21,0,0,77,78,
        5,29,0,0,78,79,5,32,0,0,79,82,5,33,0,0,80,82,5,29,0,0,81,72,1,0,
        0,0,81,73,1,0,0,0,81,74,1,0,0,0,81,75,1,0,0,0,81,76,1,0,0,0,81,77,
        1,0,0,0,81,80,1,0,0,0,82,11,1,0,0,0,83,84,7,1,0,0,84,13,1,0,0,0,
        85,86,7,2,0,0,86,15,1,0,0,0,87,88,5,3,0,0,88,89,3,18,9,0,89,90,5,
        28,0,0,90,91,5,35,0,0,91,94,3,10,5,0,92,93,5,9,0,0,93,95,5,28,0,
        0,94,92,1,0,0,0,94,95,1,0,0,0,95,17,1,0,0,0,96,97,7,3,0,0,97,19,
        1,0,0,0,7,24,30,54,65,70,81,94
    ]

class RestAPIParser ( Parser ):

    grammarFileName = "RestAPIParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'api'", "'model'", "'endpoint'", "'table'", 
                     "'using'", "'version'", "'at'", "'default'", "'description'", 
                     "'GET'", "'POST'", "'PUT'", "'PATCH'", "'DELETE'", 
                     "'sqlite'", "'postgres'", "'str'", "'int'", "'float'", 
                     "'bool'", "'datetime'", "'required'", "'unique'", "'indexed'", 
                     "<INVALID>", "'null'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'{'", "'}'", "'['", "']'", "':'", "'->'", "','" ]

    symbolicNames = [ "<INVALID>", "API", "MODEL", "ENDPOINT", "TABLE", 
                      "USING", "VERSION", "AT", "DEFAULT", "DESCRIPTION", 
                      "GET", "POST", "PUT", "PATCH", "DELETE", "SQLITE", 
                      "POSTGRES", "STR", "INT", "FLOAT", "BOOL", "DATETIME", 
                      "REQUIRED", "UNIQUE", "INDEXED", "BOOLEAN", "NULL", 
                      "NUMBER", "STRING", "IDENTIFIER", "LBRACE", "RBRACE", 
                      "LBRACKET", "RBRACKET", "COLON", "ARROW", "COMMA", 
                      "WS", "COMMENT", "BLOCK_COMMENT" ]

    RULE_api_specification = 0
    RULE_api_declaration = 1
    RULE_database_type = 2
    RULE_model_declaration = 3
    RULE_field_declaration = 4
    RULE_type_spec = 5
    RULE_field_modifier = 6
    RULE_value = 7
    RULE_endpoint_declaration = 8
    RULE_http_method = 9

    ruleNames =  [ "api_specification", "api_declaration", "database_type", 
                   "model_declaration", "field_declaration", "type_spec", 
                   "field_modifier", "value", "endpoint_declaration", "http_method" ]

    EOF = Token.EOF
    API=1
    MODEL=2
    ENDPOINT=3
    TABLE=4
    USING=5
    VERSION=6
    AT=7
    DEFAULT=8
    DESCRIPTION=9
    GET=10
    POST=11
    PUT=12
    PATCH=13
    DELETE=14
    SQLITE=15
    POSTGRES=16
    STR=17
    INT=18
    FLOAT=19
    BOOL=20
    DATETIME=21
    REQUIRED=22
    UNIQUE=23
    INDEXED=24
    BOOLEAN=25
    NULL=26
    NUMBER=27
    STRING=28
    IDENTIFIER=29
    LBRACE=30
    RBRACE=31
    LBRACKET=32
    RBRACKET=33
    COLON=34
    ARROW=35
    COMMA=36
    WS=37
    COMMENT=38
    BLOCK_COMMENT=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Api_specificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def api_declaration(self):
            return self.getTypedRuleContext(RestAPIParser.Api_declarationContext,0)


        def EOF(self):
            return self.getToken(RestAPIParser.EOF, 0)

        def model_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RestAPIParser.Model_declarationContext)
            else:
                return self.getTypedRuleContext(RestAPIParser.Model_declarationContext,i)


        def endpoint_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RestAPIParser.Endpoint_declarationContext)
            else:
                return self.getTypedRuleContext(RestAPIParser.Endpoint_declarationContext,i)


        def getRuleIndex(self):
            return RestAPIParser.RULE_api_specification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApi_specification" ):
                listener.enterApi_specification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApi_specification" ):
                listener.exitApi_specification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApi_specification" ):
                return visitor.visitApi_specification(self)
            else:
                return visitor.visitChildren(self)




    def api_specification(self):

        localctx = RestAPIParser.Api_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_api_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.api_declaration()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 21
                self.model_declaration()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 27
                self.endpoint_declaration()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self.match(RestAPIParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Api_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def API(self):
            return self.getToken(RestAPIParser.API, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(RestAPIParser.STRING)
            else:
                return self.getToken(RestAPIParser.STRING, i)

        def VERSION(self):
            return self.getToken(RestAPIParser.VERSION, 0)

        def AT(self):
            return self.getToken(RestAPIParser.AT, 0)

        def USING(self):
            return self.getToken(RestAPIParser.USING, 0)

        def database_type(self):
            return self.getTypedRuleContext(RestAPIParser.Database_typeContext,0)


        def getRuleIndex(self):
            return RestAPIParser.RULE_api_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApi_declaration" ):
                listener.enterApi_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApi_declaration" ):
                listener.exitApi_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApi_declaration" ):
                return visitor.visitApi_declaration(self)
            else:
                return visitor.visitChildren(self)




    def api_declaration(self):

        localctx = RestAPIParser.Api_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_api_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(RestAPIParser.API)
            self.state = 36
            self.match(RestAPIParser.STRING)
            self.state = 37
            self.match(RestAPIParser.VERSION)
            self.state = 38
            self.match(RestAPIParser.STRING)
            self.state = 39
            self.match(RestAPIParser.AT)
            self.state = 40
            self.match(RestAPIParser.STRING)
            self.state = 41
            self.match(RestAPIParser.USING)
            self.state = 42
            self.database_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Database_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQLITE(self):
            return self.getToken(RestAPIParser.SQLITE, 0)

        def POSTGRES(self):
            return self.getToken(RestAPIParser.POSTGRES, 0)

        def getRuleIndex(self):
            return RestAPIParser.RULE_database_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDatabase_type" ):
                listener.enterDatabase_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDatabase_type" ):
                listener.exitDatabase_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDatabase_type" ):
                return visitor.visitDatabase_type(self)
            else:
                return visitor.visitChildren(self)




    def database_type(self):

        localctx = RestAPIParser.Database_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_database_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
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


    class Model_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODEL(self):
            return self.getToken(RestAPIParser.MODEL, 0)

        def IDENTIFIER(self):
            return self.getToken(RestAPIParser.IDENTIFIER, 0)

        def TABLE(self):
            return self.getToken(RestAPIParser.TABLE, 0)

        def STRING(self):
            return self.getToken(RestAPIParser.STRING, 0)

        def LBRACE(self):
            return self.getToken(RestAPIParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(RestAPIParser.RBRACE, 0)

        def field_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RestAPIParser.Field_declarationContext)
            else:
                return self.getTypedRuleContext(RestAPIParser.Field_declarationContext,i)


        def getRuleIndex(self):
            return RestAPIParser.RULE_model_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel_declaration" ):
                listener.enterModel_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel_declaration" ):
                listener.exitModel_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModel_declaration" ):
                return visitor.visitModel_declaration(self)
            else:
                return visitor.visitChildren(self)




    def model_declaration(self):

        localctx = RestAPIParser.Model_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_model_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(RestAPIParser.MODEL)
            self.state = 47
            self.match(RestAPIParser.IDENTIFIER)
            self.state = 48
            self.match(RestAPIParser.TABLE)
            self.state = 49
            self.match(RestAPIParser.STRING)
            self.state = 50
            self.match(RestAPIParser.LBRACE)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 51
                self.field_declaration()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.match(RestAPIParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(RestAPIParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(RestAPIParser.COLON, 0)

        def type_spec(self):
            return self.getTypedRuleContext(RestAPIParser.Type_specContext,0)


        def field_modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RestAPIParser.Field_modifierContext)
            else:
                return self.getTypedRuleContext(RestAPIParser.Field_modifierContext,i)


        def DEFAULT(self):
            return self.getToken(RestAPIParser.DEFAULT, 0)

        def value(self):
            return self.getTypedRuleContext(RestAPIParser.ValueContext,0)


        def getRuleIndex(self):
            return RestAPIParser.RULE_field_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_declaration" ):
                listener.enterField_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_declaration" ):
                listener.exitField_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_declaration" ):
                return visitor.visitField_declaration(self)
            else:
                return visitor.visitChildren(self)




    def field_declaration(self):

        localctx = RestAPIParser.Field_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_field_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(RestAPIParser.IDENTIFIER)
            self.state = 60
            self.match(RestAPIParser.COLON)
            self.state = 61
            self.type_spec()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0):
                self.state = 62
                self.field_modifier()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 68
                self.match(RestAPIParser.DEFAULT)
                self.state = 69
                self.value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(RestAPIParser.STR, 0)

        def INT(self):
            return self.getToken(RestAPIParser.INT, 0)

        def FLOAT(self):
            return self.getToken(RestAPIParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(RestAPIParser.BOOL, 0)

        def DATETIME(self):
            return self.getToken(RestAPIParser.DATETIME, 0)

        def IDENTIFIER(self):
            return self.getToken(RestAPIParser.IDENTIFIER, 0)

        def LBRACKET(self):
            return self.getToken(RestAPIParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(RestAPIParser.RBRACKET, 0)

        def getRuleIndex(self):
            return RestAPIParser.RULE_type_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_spec" ):
                listener.enterType_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_spec" ):
                listener.exitType_spec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_spec" ):
                return visitor.visitType_spec(self)
            else:
                return visitor.visitChildren(self)




    def type_spec(self):

        localctx = RestAPIParser.Type_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type_spec)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(RestAPIParser.STR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(RestAPIParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.match(RestAPIParser.FLOAT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.match(RestAPIParser.BOOL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
                self.match(RestAPIParser.DATETIME)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 77
                self.match(RestAPIParser.IDENTIFIER)
                self.state = 78
                self.match(RestAPIParser.LBRACKET)
                self.state = 79
                self.match(RestAPIParser.RBRACKET)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 80
                self.match(RestAPIParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_modifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REQUIRED(self):
            return self.getToken(RestAPIParser.REQUIRED, 0)

        def UNIQUE(self):
            return self.getToken(RestAPIParser.UNIQUE, 0)

        def INDEXED(self):
            return self.getToken(RestAPIParser.INDEXED, 0)

        def getRuleIndex(self):
            return RestAPIParser.RULE_field_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_modifier" ):
                listener.enterField_modifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_modifier" ):
                listener.exitField_modifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_modifier" ):
                return visitor.visitField_modifier(self)
            else:
                return visitor.visitChildren(self)




    def field_modifier(self):

        localctx = RestAPIParser.Field_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_field_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
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

        def STRING(self):
            return self.getToken(RestAPIParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(RestAPIParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(RestAPIParser.BOOLEAN, 0)

        def NULL(self):
            return self.getToken(RestAPIParser.NULL, 0)

        def getRuleIndex(self):
            return RestAPIParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = RestAPIParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0)):
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


    class Endpoint_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENDPOINT(self):
            return self.getToken(RestAPIParser.ENDPOINT, 0)

        def http_method(self):
            return self.getTypedRuleContext(RestAPIParser.Http_methodContext,0)


        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(RestAPIParser.STRING)
            else:
                return self.getToken(RestAPIParser.STRING, i)

        def ARROW(self):
            return self.getToken(RestAPIParser.ARROW, 0)

        def type_spec(self):
            return self.getTypedRuleContext(RestAPIParser.Type_specContext,0)


        def DESCRIPTION(self):
            return self.getToken(RestAPIParser.DESCRIPTION, 0)

        def getRuleIndex(self):
            return RestAPIParser.RULE_endpoint_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndpoint_declaration" ):
                listener.enterEndpoint_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndpoint_declaration" ):
                listener.exitEndpoint_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndpoint_declaration" ):
                return visitor.visitEndpoint_declaration(self)
            else:
                return visitor.visitChildren(self)




    def endpoint_declaration(self):

        localctx = RestAPIParser.Endpoint_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_endpoint_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(RestAPIParser.ENDPOINT)
            self.state = 88
            self.http_method()
            self.state = 89
            self.match(RestAPIParser.STRING)
            self.state = 90
            self.match(RestAPIParser.ARROW)
            self.state = 91
            self.type_spec()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 92
                self.match(RestAPIParser.DESCRIPTION)
                self.state = 93
                self.match(RestAPIParser.STRING)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Http_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GET(self):
            return self.getToken(RestAPIParser.GET, 0)

        def POST(self):
            return self.getToken(RestAPIParser.POST, 0)

        def PUT(self):
            return self.getToken(RestAPIParser.PUT, 0)

        def PATCH(self):
            return self.getToken(RestAPIParser.PATCH, 0)

        def DELETE(self):
            return self.getToken(RestAPIParser.DELETE, 0)

        def getRuleIndex(self):
            return RestAPIParser.RULE_http_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHttp_method" ):
                listener.enterHttp_method(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHttp_method" ):
                listener.exitHttp_method(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHttp_method" ):
                return visitor.visitHttp_method(self)
            else:
                return visitor.visitChildren(self)




    def http_method(self):

        localctx = RestAPIParser.Http_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_http_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0)):
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





