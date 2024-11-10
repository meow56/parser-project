grammar D1;

start: statement? NEWLINES
	| statement? EOF;

NEWLINES: [\n]+;

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
STRING: '"' .+? '"'
	| '\'' .+? '\'';
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

WS:	[ \t\r]+ -> skip;