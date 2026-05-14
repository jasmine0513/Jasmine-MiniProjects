//Jasmine Carrion
//jasmine.carrion73@myhunter.cuny.edu
#include <iostream>
#include <limits>

int main() {
    int value;
    int maximum = std::numeric_limits<int>::min();
    bool has_value = false;

    while (std::cin >> value) {
        has_value = true;
        if (value > maximum) {
            maximum = value;
        }
    }

    if (has_value) {
        std::cout << maximum;
    }
    return 0;
}
