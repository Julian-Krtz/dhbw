#include <iostream>

void ausgabe(const char* text, ...) {
    const char** field = &text;
    std::cout << "LOL" << std::endl;
}

int main() {
    ausgabe("Hallo", "Welt", "Hallo", "Universum");
}