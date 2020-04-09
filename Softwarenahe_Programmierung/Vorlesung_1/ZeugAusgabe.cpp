#include <iostream>
#include<stdio.h>

void ausgabe(const char* text, ...) {
    const char** field = &text;
    int i = 0;
    while(field[i]) {
        std::cout << field[i++] << std::endl;
    }
    
}

int main() {
    ausgabe("Hallo", "Welt", "Hallo", "Universum", NULL);
}