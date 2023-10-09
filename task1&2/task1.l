/*** The following script takes a .py file and outputs the comments
/*** Definition Section ***/
%{
int count = 0;
%}
 
/*** Rule Section ***/
%%
#.* {printf("%s \n", yytext);
       count++;}
" "*#.* {printf("%s \n", yytext);
       count++;}
.     {return 0;}
%%
 
/*** Code Section ***/
int yywrap(){
      return 1;
}

int main(){
      // Takes file input
      FILE *fp;
      char filename[50];
      printf("Enter the filename: \n");
      scanf("%s",filename);
      fp = fopen(filename,"r");
      if (fp == NULL){
            printf("Error: The file cannot be opened.\n");
            return 1;
      }
      yyin = fp;
      
      // Outputs comments
      printf("The following lines are comments: \n");
      yylex();
      printf("\nNumber of comments - %d\n", count);
      
      fclose(fp);

      return 0;
}