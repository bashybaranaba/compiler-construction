%{
#include <stdio.h>
%}

%token NUM
%left '+' '-'
%left '*' '/'

%%
calc:   expr { printf("Result: %d\n", $1); }
    ;

expr:   NUM
    |   expr '+' expr { $$ = $1 + $3; }
    |   expr '-' expr { $$ = $1 - $3; }
    |   expr '*' expr { $$ = $1 * $3; }
    |   expr '/' expr { $$ = $1 / $3; }
    |   '(' expr ')' { $$ = $2; }
    ;

%%

int main() {
    yyparse();
    return 0;
}
