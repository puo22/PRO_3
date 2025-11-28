grammar Zero;

program         : statement+ EOF ;

statement
    : ID '=>' expression                    #assignStmt
    | 'eco' printItem (',' printItem)*      #printStmt
    | 'si' '(' expression ')' bloque ('sino' bloque)? #ifStmt
    | 'mientras' '(' expression ')' bloque  #whileStmt
    | 'leer' '(' STRING ')'                 #loadStmt
    | 'columna' '(' expression ',' expression ')' #colStmt
    | 'ajustar' '(' expression ',' expression ')' #regresionStmt
    | 'pronosticar' '(' expression ',' expression ')'  #predecirStmt
    | 'red_simple' '(' expression ',' expression (',' expression)? ')' #perceptronStmt
    | 'segmentar' '(' expression ',' expression (',' expression)? ')' #kmeansStmt
    | 'suma_mat' '(' expression ',' expression ')' #matSumaStmt
    | 'resta_mat' '(' expression ',' expression ')' #matRestaStmt
    | 'multiplica_mat' '(' expression ',' expression ')' #matMultStmt
    | 'transpuesta' '(' expression ')'            #matTransStmt
    | 'inversa' '(' expression ')'                #matInvStmt
    | 'nube' '(' expression ',' expression (',' STRING)? ')' #puntosStmt
    | 'trazo' '(' expression ')'            #lineaStmt
    | 'render' '(' ')'                      #graficarStmt
    | expression                            #exprStmt
    ;

bloque          : '{' statement* '}' ;

printItem
    : STRING                                #stringItem
    | expression                            #exprItem
    ;

expression
    : atom                                  #atomExpr
    | 'raiz' '(' expression ')'             #sqrtExpr
    | 'seno' '(' expression ')'             #sinExpr
    | 'leer' '(' STRING ')'                 #loadExpr
    | 'columna' '(' expression ',' expression ')' #colExpr
    | 'ajustar' '(' expression ',' expression ')' #regresionExpr
    | 'pronosticar' '(' expression ',' expression ')'  #predecirExpr
    | 'red_simple' '(' expression ',' expression (',' expression)? ')' #perceptronExpr
    | 'segmentar' '(' expression ',' expression (',' expression)? ')' #kmeansExpr
    | 'suma_mat' '(' expression ',' expression ')' #matSumaExpr
    | 'resta_mat' '(' expression ',' expression ')' #matRestaExpr
    | 'multiplica_mat' '(' expression ',' expression ')' #matMultExpr
    | 'transpuesta' '(' expression ')'            #matTransExpr
    | 'inversa' '(' expression ')'                #matInvExpr
    | expression '^' expression             #powerExpr
    | expression op=('*'|'/'|'%') expression #mulDivExpr
    | expression op=('+'|'-') expression    #addSubExpr
    | expression op=('<'|'>'|'>='|'<='|'=='|'!=') expression #cmpExpr
    | expression op=('&&'|'||') expression    #boolExpr
    ;

atom
    : NUMBER                                #numberAtom
    | 'verdadero'                           #trueAtom
    | 'falso'                               #falseAtom
    | ID '[' expression ']'                 #indexAtom
    | ID                                    #varAtom
    | '[' exprList ']'                      #vectorAtom
    | '(' expression ')'                    #parenAtom
    ;

exprList        : expression (',' expression)* ;

ID              : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER          : [0-9]+ ('.' [0-9]+)? ;
STRING          : '"' (~["\\] | '\\' .)* '"' ;
WS              : [ \t\r\n]+ -> skip ;
COMMENT         : '#' ~[\r\n]* -> skip ;
