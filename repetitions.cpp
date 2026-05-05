//Jasmine Carrion
//jasmine.carrion73@myhunter.cuny.edu
//Mini project: Repetitions
#include <iostream>
#include <string>
using namespace std;

int main() {
    int repetitions;
    string message;

    cout << "How many repetitions? ";
    cin >> repetitions;

    cout << "What message? ";
    cin.ignore();
    getline(cin, message);

    for (int i = 0; i < repetitions; i++) {
        cout << message << endl;
    }
}