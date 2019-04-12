/*
 *  nint Grammar
 *
 *  @date 04/02/2019
 *  @version 1.0
 *  @author Hector Rincon
 */

grammar nint;

@parser::header {
import sys
sys.path.append("C:/dev/compiler")
from icg.Node import Node
from icg.Expr import Expr
from icg.Op import Op
from icg.Arith import Arith
from icg.Stmt import Stmt
from icg.Seq import Seq
}



/* 2. Rules
---------------------------------------------------------- */




prog returns [s]
@init {
s = None
}
    :   (   stats+=statement (';'|NL)*
    |   NL
        )* {$ctx.s = Seq(list(map(lambda x: x.stmt, $stats)))}
    EOF
    ;


primary
    : '(' expression ')'
    | literal
    | ID
    ;


block
    : '{' statement* '}'
    ;


statement returns [stmt]
@init {
stmt = None
}
    : block
    | IF '(' expression ')' block (ELSE block)?
    | FOR '(' forInit? ';' expression? ';' expressionList? ')' block
    | WHILE '(' expression ')' block
    | RETURN expression? ';'
    | exp=expression ';' {$ctx.stmt = $exp.ctx.result}
    | functionDeclaration
    | declaration
    ;


expression returns [result]
@init{
result = None
}
    : primary {$ctx.result = Expr($primary.text, 'string')}
    | expression '[' (expression | indexList | ':') ']' // `:` = all the dimension
    | functionCall
    | pipeStmt
    | '-' expression // negative numbers
    | '!' expression // negation TODO: assoc=right?
    | a=expression bop=('*'|'/') b=expression {$ctx.result = Arith($bop.text, $a.ctx.result, $b.ctx.result)}
    | a=expression bop=('+'|'-') b=expression {$ctx.result = Arith($bop.text, $a.ctx.result, $b.ctx.result);}
    | expression bop=('<=' | '>=' | '>' | '<') expression
    | expression bop=('==' | '!=') expression
    | <assoc=right> expression bop='**' expression // exponentiation
    | expression bop='&&' expression
    | expression bop='||' expression
    | <assoc=right> expression '=' expression // assignment
    ;

expressionList
    : expression (',' expression)*
    ;


literal
    : INT_LITERAL
    | FLOAT_LITERAL
    | STRING_LITERAL
    | BOOL_LITERAL
    | RANGE
    | NULL
    | ID
    ;


/* For loops */

forInit
    : declaration
    | expressionList
    ;

indexList
    : DIGIT+ (',' indexList)?
    ;


/* Declaration */
declaration
    : typeSpecifier declarator ';'
    ;
declarator
    : ID ('=' initalizer)?
    ;
initalizer
    : vectorInitializer
    | expression
    ;
vectorInitializer
    : '[' (initalizer (',' initalizer)* )? ']'
    ;

/* Functions */

functionDeclaration
    : 'function' ID '(' parameterList ')' '::' typeSpecifier block
    ;

/* TODO: how to handle null? */
typeSpecifier
    :   ('string'
    |   'void'
    |   'int'
    |   'float'
    |   'data.frame'
    |   'factor'
    |   'bool') ('[' ']')? /* TODO: vectors of data frames? */
    ;


parameterList
    : parameterDeclaration
    | parameterList ',' parameterDeclaration
    ;


parameterDeclaration
    : typeSpecifier ID
    ;


/* Function calls */

functionCall
    : ID '(' callArgs? ')'
    ;

callArgs
    : expression (',' expression)* // TODO: Is this better than separating like parameterList?
    ;

/* Pipe declarations */
pipeStmt
    : functionCall ('>>' functionCall)+
    ;



// TODO: fix typeorVoid
// TODO: define factor handling
/* IO operations */
/* Factors */
/* Data frame */
/* Special functions */


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
FLOAT_LITERAL: ([0-9]*'.')?[0-9]+;
ID: [a-zA-Z][a-zA-Z0-9_]*;
DIGIT: [0-9];
INT_LITERAL: DIGIT+;
RANGE: DIGIT+'..'DIGIT+;
STRING_LITERAL:  '"' (~["\\\r\n])* '"' |  '\'' (~["\\\r\n])* '\'';

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
COMMENT:            '/*'.*?'*/'       -> skip;
LINE_COMMENT:       '//' ~[\r\n]*    -> skip;
WS:                 [ \t\r\n\u000C]+ -> skip;

// Match both UNIX and Windows newlines
NL:                 '\r'? '\n' ;
