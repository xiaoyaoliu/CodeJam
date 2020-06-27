#include <stdio.h>
#include <string.h>

int greeting(char *temp1, char *temp2){
    char name[400];
    strcpy(name, temp2);
    printf("Hello %s %s\n", temp1, name);
}

int main(int args, char *argv[]){
    greeting(argv[1], argv[2]);
    printf("Bye %s %s\n", argv[1], argv[2]);
}
