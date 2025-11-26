lexer grammar RestAPILexer;

// Keywords
API         : 'api';
MODEL       : 'model';
ENDPOINT    : 'endpoint';
TABLE       : 'table';
USING       : 'using';
VERSION     : 'version';
AT          : 'at';
DEFAULT     : 'default';
DESCRIPTION : 'description';

// HTTP Methods
GET         : 'GET';
POST        : 'POST';
PUT         : 'PUT';
PATCH       : 'PATCH';
DELETE      : 'DELETE';

// Database Types
SQLITE      : 'sqlite';
POSTGRES    : 'postgres';

// Field Types
STR         : 'str';
INT         : 'int';
FLOAT       : 'float';
BOOL        : 'bool';
DATETIME    : 'datetime';

// Field Modifiers
REQUIRED    : 'required';
UNIQUE      : 'unique';
INDEXED     : 'indexed';

// Literals
BOOLEAN     : 'true' | 'false';
NULL        : 'null';
NUMBER      : '-'? [0-9]+ ('.' [0-9]+)?;
STRING      : '"' (~["\r\n])* '"';

// Identifiers
IDENTIFIER  : [A-Za-z_][A-Za-z0-9_]*;

// Symbols
LBRACE      : '{';
RBRACE      : '}';
LBRACKET    : '[';
RBRACKET    : ']';
COLON       : ':';
ARROW       : '->';
COMMA       : ',';

// Whitespace and Comments
WS          : [ \t\r\n]+ -> skip;
COMMENT     : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;
