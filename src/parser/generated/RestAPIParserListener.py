# Generated from apiary/parser/grammar/RestAPIParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RestAPIParser import RestAPIParser
else:
    from RestAPIParser import RestAPIParser

# This class defines a complete listener for a parse tree produced by RestAPIParser.
class RestAPIParserListener(ParseTreeListener):

    # Enter a parse tree produced by RestAPIParser#api_specification.
    def enterApi_specification(self, ctx:RestAPIParser.Api_specificationContext):
        pass

    # Exit a parse tree produced by RestAPIParser#api_specification.
    def exitApi_specification(self, ctx:RestAPIParser.Api_specificationContext):
        pass


    # Enter a parse tree produced by RestAPIParser#api_declaration.
    def enterApi_declaration(self, ctx:RestAPIParser.Api_declarationContext):
        pass

    # Exit a parse tree produced by RestAPIParser#api_declaration.
    def exitApi_declaration(self, ctx:RestAPIParser.Api_declarationContext):
        pass


    # Enter a parse tree produced by RestAPIParser#database_type.
    def enterDatabase_type(self, ctx:RestAPIParser.Database_typeContext):
        pass

    # Exit a parse tree produced by RestAPIParser#database_type.
    def exitDatabase_type(self, ctx:RestAPIParser.Database_typeContext):
        pass


    # Enter a parse tree produced by RestAPIParser#model_declaration.
    def enterModel_declaration(self, ctx:RestAPIParser.Model_declarationContext):
        pass

    # Exit a parse tree produced by RestAPIParser#model_declaration.
    def exitModel_declaration(self, ctx:RestAPIParser.Model_declarationContext):
        pass


    # Enter a parse tree produced by RestAPIParser#field_declaration.
    def enterField_declaration(self, ctx:RestAPIParser.Field_declarationContext):
        pass

    # Exit a parse tree produced by RestAPIParser#field_declaration.
    def exitField_declaration(self, ctx:RestAPIParser.Field_declarationContext):
        pass


    # Enter a parse tree produced by RestAPIParser#type_spec.
    def enterType_spec(self, ctx:RestAPIParser.Type_specContext):
        pass

    # Exit a parse tree produced by RestAPIParser#type_spec.
    def exitType_spec(self, ctx:RestAPIParser.Type_specContext):
        pass


    # Enter a parse tree produced by RestAPIParser#field_modifier.
    def enterField_modifier(self, ctx:RestAPIParser.Field_modifierContext):
        pass

    # Exit a parse tree produced by RestAPIParser#field_modifier.
    def exitField_modifier(self, ctx:RestAPIParser.Field_modifierContext):
        pass


    # Enter a parse tree produced by RestAPIParser#value.
    def enterValue(self, ctx:RestAPIParser.ValueContext):
        pass

    # Exit a parse tree produced by RestAPIParser#value.
    def exitValue(self, ctx:RestAPIParser.ValueContext):
        pass


    # Enter a parse tree produced by RestAPIParser#endpoint_declaration.
    def enterEndpoint_declaration(self, ctx:RestAPIParser.Endpoint_declarationContext):
        pass

    # Exit a parse tree produced by RestAPIParser#endpoint_declaration.
    def exitEndpoint_declaration(self, ctx:RestAPIParser.Endpoint_declarationContext):
        pass


    # Enter a parse tree produced by RestAPIParser#http_method.
    def enterHttp_method(self, ctx:RestAPIParser.Http_methodContext):
        pass

    # Exit a parse tree produced by RestAPIParser#http_method.
    def exitHttp_method(self, ctx:RestAPIParser.Http_methodContext):
        pass



del RestAPIParser