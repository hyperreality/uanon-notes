#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    int i=0;
    int lines=0;
    char* words[50];
    char line[50];

    FILE *file;
    file = fopen("google-10000-english-no-swears.txt", "r");

    while(fgets(line, sizeof line, file)!=NULL) {
        printf("%s", line);
        /* words[i]=malloc(sizeof(line)); */
        /* strcpy(words[i], line); */
        words[i] = strdup(line);
        i++;
        lines++;
    }

    for (int j=0 ; j<lines+1; j++) {
        printf("\n%s", words[j]);
    }

    fclose(file);
    return 0;
}
