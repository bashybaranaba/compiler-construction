%{
#include "calc.tab.h"
%}

%%

[0-9]+      { yylval = atoi(yytext); return NUM; }
[-+*/\(\)]  { return yytext[0]; }
[ \t\n]     ; // Ignore whitespace and newline

.           { fprintf(stderr, "Unexpected character: %s\n", yytext); }

%%
