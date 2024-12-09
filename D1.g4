grammar D1;

start: lines+ EOF;

lines: MULTILINE
	| (statement? COMMENT? NEWLINES)+
	| conditional
	| while
	| for;

COMMENT: '#' [a-zA-Z0-9 #]+;

MULTILINE: '\'\'\'' ([a-zA-Z0-9 .\t',]+ NEWLINES)+ '\'\'\''
	| '\'\'\'' [a-zA-Z0-9 .\t',]+ '\'\'\'';

NEWLINES: [\r\n]+;

statement: assignment
	| value;

assignment: VARNAME eqStatement value;

eqStatement: '='
	| '+='
	| '-='
	| '*='
	| '/=';

VARNAME: [a-zA-Z_][a-zA-Z0-9_]*;

value: NUMBER
	| STRING
	| array
	| VARNAME
	| boolean
	| value arithSymbol value
	| '(' value ')';

NUMBER: '-'?[0-9]+('.'[0-9]+)?;
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

block: ('\t' statement NEWLINES)
	| ('\t' statement NEWLINES) block
	| ('\t' statement EOF)
	| conditional2
	| while2
	| for2;

conditional2: '\tif' boolExpr ':' NEWLINES block2 ('\telif' boolExpr ':' NEWLINES block2)? ('\telse:' NEWLINES block2)?;

block2: ('\t\t' statement NEWLINES)
	| ('\t\t' statement NEWLINES) block2
	| ('\t\t' statement EOF)
	| conditional3
	| while3
	| for3;

conditional3: '\t\tif' boolExpr ':' NEWLINES block3 ('\t\telif' boolExpr ':' NEWLINES block2)? ('\t\telse:' NEWLINES block2)?;

block3: ('\t\t\t' statement NEWLINES)+
	| ('\t\t\t' statement EOF);

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

while: 'while' boolExpr ':' NEWLINES block;
while2: '\twhile' boolExpr ':' NEWLINES block2;
while3: '\t\twhile' boolExpr ':' NEWLINES block3;

for: 'for' VARNAME 'in' VARNAME ':' NEWLINES block
	| 'for' VARNAME 'in range(' NUMBER ',' NUMBER ')' ':' NEWLINES block;
for2: '\tfor' VARNAME 'in' VARNAME ':' NEWLINES block
	| '\tfor' VARNAME 'in range(' NUMBER ',' NUMBER ')' ':' NEWLINES block;
for3: '\t\tfor' VARNAME 'in' VARNAME ':' NEWLINES block
	| '\t\tfor' VARNAME 'in range(' NUMBER ',' NUMBER ')' ':' NEWLINES block;

WS:	[ \t\r]+ -> skip;