/*** Definition Section has variables ***/
%{
int wordCount = 0;
int spaceCount = 0;
int capitalCount = 0;
int vowelCount = 0;
%}

/*** Rule Section ***/
%%
[A-Z] {
    printf("%s is a capital letter\n", yytext);
    capitalCount++;
}

[a-zA-Z]+ {
    printf("%s is a word\n", yytext);
    wordCount++;
    for (int i = 0; yytext[i]; i++) {
        char c = yytext[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            vowelCount++;
        }
    }
}

" " {
    spaceCount++;
}

\n {
    return 0;
}

. {
    // Ignore other characters
}

%%

/*** Code Section ***/
int main() {
    yylex();
    printf("\nNumber of Words: %d\n", wordCount);
    printf("Number of Spaces: %d\n", spaceCount);
    printf("Number of Capital Letters: %d\n", capitalCount);
    printf("Number of Vowels: %d\n", vowelCount);
    return 0;
}

int yylex(void); // Declare the yylex function.

int yywrap() {
    return 1; // Indicate that there are no more tokens to process.
}
