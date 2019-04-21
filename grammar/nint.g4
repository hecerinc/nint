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
from nintCompiler import nintCompiler
}



/* 2. Rules
---------------------------------------------------------- */




prog returns [s]
@init {
self.nint = nintCompiler()
}
@after {
$ctx.s = self.nint
}
    :   (   stats+=statement (';'|NL)*
    |   NL
        )*
    EOF
    ;


primary
    : '(' expression ')'
    | literal
    ;


block
    : '{' statement* '}'
    ;


statement returns [stmt]
@init {
stmt = None
}
    : block
    | IF '(' expression ')' {self.nint.ifelse_start_jump()} block (ELSE {self.nint.ifelse_start_else()} block)? {self.nint.ifelse_end_jump()}
    | FOR '(' forInit? ';' expression? ';' expressionList? ')' block
    | WHILE {self.nint.while_condition_start()} '(' expression ')' {self.nint.while_block_start()} block {self.nint.while_end()}
    | RETURN expression? ';'
    | expression ';'
    | functionDeclaration
    | declaration
    ;


expression returns [result]
@init{
result = None
}
    : primary
    | expression '[' (expression | indexList | ':') ']' // `:` = all the dimension
    | functionCall
    | pipeStmt
    | '-' expression // negative numbers
    | '!' expression // negation TODO: assoc=right?
    // | a=expression bop=('*'|'/') b=expression
    // | a=expression bop=('+'|'-') b=expression
    | <assoc=right> expression '=' {self.nint.add_operator('=')} expression {self.nint.assignment_quad()} // assignment
    | expression bop=('<=' | '>=' | '>' | '<') {self.nint.add_operator($bop.text)} expression {self.nint.check_relop()}
    | expression bop=('==' | '!=') expression
    | exp
    | <assoc=right> expression bop='**' expression // exponentiation
    | expression bop='&&' expression
    | expression bop='||' expression
    ;

exp
    : term {self.nint.check_addsub()} (bop=('+'|'-') {self.nint.add_operator($bop.text)} term {self.nint.check_addsub()})*
    ;
term
    : p1=primary {self.nint.check_multdiv()} (bop=('*'|'/') {self.nint.add_operator($bop.text)} p2=primary {self.nint.check_multdiv()})*
    ;


expressionList
    : expression (',' expression)*
    ;


literal
    : INT_LITERAL {self.nint.add_constant($INT_LITERAL.text, 'int')}
    | FLOAT_LITERAL {self.nint.add_constant($FLOAT_LITERAL.text, 'float')}
    | STRING_LITERAL {self.nint.add_constant($STRING_LITERAL.text, 'string')}
    | BOOL_LITERAL {self.nint.add_constant($BOOL_LITERAL.text, 'bool')}
    | RANGE
    | NULL
    | ID {self.nint.add_var($ID.text)}
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
