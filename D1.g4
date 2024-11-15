grammar D1;

start: (statement? NEWLINES)+
	| statement? EOF
	| conditional;

NEWLINES: [\r\n]+;

statement: assignment
	| value;

assignment: VARNAME eqStatement value;

eqStatement: '='
	| '+='
	| '-='
	| '*='
	| '/=';

VARNAME: [a-zA-Z_][a-zA-Z0-9_]+;

value: NUMBER
	| STRING
	| array
	| VARNAME
	| boolean
	| value arithSymbol value
	| '(' value ')';

NUMBER: '-'?[0-9]+(.[0-9]+)?;
STRING: '"' .*? '"'
	| '\'' .*? '\'';
array: '[' (value ',')* (value) ']'
	| '[]';
boolean: 'True'
	| 'False';

arithmetic: value arithSymbol value;

arithSymbol: '+'
	| '-'
	| '*'
	| '/'
	| '%';

conditional: 'if' boolExpr ':' NEWLINES block ('elif' boolExpr ':' NEWLINES block)? ('else:' NEWLINES block)?;

block: ('\t' statement NEWLINES)+
	| ('\t' statement EOF);

boolExpr: boolean
	| boolExpr 'and' boolExpr
	| boolExpr 'or' boolExpr
	| 'not' boolExpr
	| '(' boolExpr ')'
	| value comparisons value
	| VARNAME;

comparisons: '=='
	| '!='
	| '>='
	| '<='
	| '>'
	| '<';

WS:	[ \t\r]+ -> skip;