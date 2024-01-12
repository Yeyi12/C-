#include <stdio.h>
#include <stdlib.h>

#define KNRM  "\x1B[0m"
#define KRED  "\x1B[1;31m"
#define KGRN  "\x1B[1;32m"
#define KYEL  "\x1B[1;33m"

void copyFile(const char *sourceFile, const char *destinationFile) {
    FILE *source, *destination;
    char ch;

    source = fopen(sourceFile, "r");
    if (source == NULL) {
        printf("%sError:%s Unable to open source file\n", KRED, KNRM);
        exit(EXIT_FAILURE);
    }

    destination = fopen(destinationFile, "w");
    if (destination == NULL) {
        printf("%sError:%s Unable to open destination file\n", KRED, KNRM);
        fclose(source);
        exit(EXIT_FAILURE);
    }

    while ((ch = fgetc(source)) != EOF) {
        fputc(ch, destination);
    }

    printf("%sFile copied successfully from %s to %s%s\n", KGRN, sourceFile, destinationFile, KNRM);

    fclose(source);
    fclose(destination);
}

int main(int argc, char **argv) {
    if (argc != 3) {
        printf("%sUsage: %s source_file destination_file%s\n", KYEL, argv[0], KNRM);
        return EXIT_FAILURE;
    }

    copyFile(argv[1], argv[2]);

    return EXIT_SUCCESS;
}
