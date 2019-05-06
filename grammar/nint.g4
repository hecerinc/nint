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
from symbols.Types import DType
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
    : literal
    | '(' {self.nint.paren_open()} expression ')' {self.nint.paren_close()}
    ;

block
    : '{' statement* '}'
    ;


statement returns [stmt]
@init {
stmt = None
}
    : block
    | IF '(' expression ')' {self.nint.ifelse_start_jump()} block (ELSE {self.nint.ifelse_start_else()} statement)? {self.nint.ifelse_end_jump()}
    | FOR '(' forInit? ';' expression? ';' expressionList? ')' block
    | WHILE {self.nint.while_condition_start()} '(' expression ')' {self.nint.while_block_start()} block {self.nint.while_end()}
    | RETURN expression? {self.nint.procedure_return($expression.ctx is not None)} ';'
    | expression ';'
    | functionDeclaration
    | declaration ';'
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
    | <assoc=right> '!' expression // negation TODO: assoc=right?
    // | a=expression bop=('*'|'/') b=expression
    // | a=expression bop=('+'|'-') b=expression
    | <assoc=right> expression '=' {self.nint.add_operator('=')} expression {self.nint.assignment_quad()} // assignment
    | expression bop=('<=' | '>=' | '>' | '<') {self.nint.add_operator($bop.text)} expression {self.nint.check_relop()}
    | expression bop=('==' | '!=') {self.nint.add_operator($bop.text)} expression {self.nint.check_eqop()}
    | exp
    | <assoc=right> expression bop='**' expression // exponentiation
    | expression bop='&&' {self.nint.add_operator($bop.text)} expression {self.nint.check_and()}
    | expression bop='||' {self.nint.add_operator($bop.text)} expression {self.nint.check_or()}
    ;

exp
    : term {self.nint.check_addsub()} (bop=('+'|'-') {self.nint.add_operator($bop.text)} term {self.nint.check_addsub()})*
    ;
term
    : factor {self.nint.check_multdiv()} (bop=('*'|'/') {self.nint.add_operator($bop.text)} factor {self.nint.check_multdiv()})*
    ;

factor
    : primary
    | functionCall
    ;

expressionList
    : expression (',' expression)*
    ;


literal
    : INT_LITERAL {self.nint.add_constant($INT_LITERAL.text, DType.INT)}
    | FLOAT_LITERAL {self.nint.add_constant($FLOAT_LITERAL.text, DType.FLOAT)}
    | STRING_LITERAL {self.nint.add_constant($STRING_LITERAL.text, DType.STRING)}
    | BOOL_LITERAL {self.nint.add_constant($BOOL_LITERAL.text, DType.BOOL)}
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
    : INT_LITERAL (',' indexList)?
    ;


/* Declaration */
declaration
    : typeSpecifier ID {self.nint.add_var_declaration($typeSpecifier.text, $ID.text)} ('=' {self.nint.add_var($ID.text)} {self.nint.add_operator('=')} init=initializer {self.nint.assignment_quad()})?
    ;
initializer
    : vectorInitializer
    | expression
    ;
vectorInitializer
    : '[' (initializer (',' initializer)* )? ']'
    ;

/* Functions */

functionDeclaration
    : 'function' ID {self.nint.procedure_start($ID.text)} '(' (plist=parameterList {self.nint.procedure_add_params($plist.ctx.plist)})? ')' '::' typeSpecifier {self.nint.procedure_set_type($typeSpecifier.text); self.nint.procedure_mark_start()} block {self.nint.procedure_end()}
    ;


parameterList returns [plist]
@init {
plist = None
}
    : pd=parameterDeclaration {$ctx.plist = [$pd.ctx.pd]}
    | paramlist=parameterList ',' pd=parameterDeclaration {$ctx.plist = $paramlist.ctx.plist + [$pd.ctx.pd]}
    ;


parameterDeclaration returns [pd]
@init {
pd = dict()
}
    : ts=typeSpecifier ID {$ctx.pd = {'type': $ts.text, 'id': $ID.text}}
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


/* Function calls */

functionCall
    : 'print' {self.nint.print_start()} '(' expression {self.nint.print_expression()} (',' expression {self.nint.print_expression()})* ')' {self.nint.print_end()}
    | {self.nint.paren_open()} ID {self.nint.method_call_start($ID.text)} '(' {self.nint.method_call_param_start()} callArgs? ')' {self.nint.method_call_param_end()} {self.nint.method_call_end()} {self.nint.paren_close()}
    ;

callArgs
    : expression {self.nint.method_call_param()} (',' {self.nint._param_k += 1} expression {self.nint.method_call_param()})* // TODO: Is this better than separating like parameterList?
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
FLOAT_LITERAL: [0-9]*'.'[0-9]+;
ID: [a-zA-Z][a-zA-Z0-9_]*;
fragment DIGIT: [0-9];
INT_LITERAL: DIGIT+;
RANGE: DIGIT+'..'DIGIT+;
STRING_LITERAL:  '"' (~["\\\r\n])* '"' |  '\'' (~['\\\r\n])* '\'';

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
