parser grammar RestAPIParser;

options {
    tokenVocab=RestAPILexer;
}

// Parser Rules

api_specification
    : api_declaration model_declaration* endpoint_declaration* EOF
    ;

api_declaration
    : API STRING VERSION STRING AT STRING USING database_type
    ;

database_type
    : SQLITE
    | POSTGRES
    ;

model_declaration
    : MODEL IDENTIFIER TABLE STRING LBRACE field_declaration* RBRACE
    ;

field_declaration
    : IDENTIFIER COLON type_spec field_modifier* (DEFAULT value)?
    ;

type_spec
    : STR
    | INT
    | FLOAT
    | BOOL
    | DATETIME
    | IDENTIFIER LBRACKET RBRACKET  // Array type like Pet[]
    | IDENTIFIER                     // Reference type
    ;

field_modifier
    : REQUIRED
    | UNIQUE
    | INDEXED
    ;

value
    : STRING
    | NUMBER
    | BOOLEAN
    | NULL
    ;

endpoint_declaration
    : ENDPOINT http_method STRING ARROW type_spec (DESCRIPTION STRING)?
    ;

http_method
    : GET
    | POST
    | PUT
    | PATCH
    | DELETE
    ;
