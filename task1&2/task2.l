/*** This script takes a given identifier as input and determines whether it is valid in Python***/
/*** Definition Section ***/
%{
%}
 
/*** Rule Section ***/
%%
"and"|"as"|"assert"|"break"|"class"|"continue"|"def"|"del"|"elif"|"else"|"except"|"False"|"finally"|"for"|"from"|"global"|"if"|"import"|"in"|"is"|"lambda"|"None"|"nonlocal"|"not"|"or"|"pass"|"raise"|"return"|"True"|"try"|"while"|"with"|"yield" {printf("%s is an invalid identifier.\n", yytext);}
[a-zA-Z_][0-9a-zA-Z_]* {printf("%s is a valid identifier.\n", yytext);}
.*     {printf("%s is an invalid identifier.\n", yytext);}
%%
 
/*** Code Section ***/
int yywrap(){}
int main(){
 
yylex();
 
return 0;
}