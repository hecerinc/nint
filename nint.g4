/*
 *  nint Grammar
 *
 *  @date 04/02/2019
 *  @version 1.0
 *  @author Hector Rincon
 */

grammar nint;

/* 1. Tokens
---------------------------------------------------------- */

// Keywords
BOOL:               'bool';
DF:                 'data.frame';
ELSE:               'else';
FACTOR:             'factor';
FLOAT:              'float';
FOR:                'for';
FUN:                'function';
IF:                 'if';
INPUT:              'input';
INT:                'int';
NULL:               'null';
PRINT:              'print';
RETURN:             'return';
STRING:             'string';
VOID:               'void';
WHILE:              'while';

// Literals
BOOL_LITERAL: 'true' | 'false';
FLOAT_LITERAL: -?([0-9]*'.')?[0-9]+;
ID: [a-zA-Z][a-zA-Z0-9_]*;
INT_LITERAL: -?[0-9]+;
RANGE: [0-9]+'..'[0-9]+
STRING_LITERAL: '"'.*'"' | '\''.*'\'';

// Separators
COMMA:              ',';
DOT:                '.';
LBRACE:             '{';
LBRACK:             '[';
LPAREN:             '(';
RBRACE:             '}';
RBRACK:             ']';
RETURNSTYPE:        '::';
RPAREN:             ')';
SEMICOLON:          ';';

// Operators
ADD:                '+';
AND:                '&&';
ASSIGN:             '=';
BANG:               '!';
DIV:                '/';
EQUAL:              '==';
EXP:                '**';
GT:                 '>';
GTE:                '>=';
LE:                 '<=';
LTE:                '<';
MUL:                '*';
NOTEQUAL:           '!=';
OR:                 '||';
PIPE:               '>>';
SUB:                '-';

// Whitespace and comments
COMMENT:            '/*'.*'*/'       -> skip;
LINE_COMMENT:       '//' ~[\r\n]*    -> skip;
WS:                 [ \t\r\n\u000C]+ -> skip;

/* 2. Rules
---------------------------------------------------------- */

