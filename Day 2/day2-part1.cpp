#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int horizontal = 0, depth = 0;
    ifstream iFile("input.txt");

    while (!iFile.eof()) {
        string instruction;
        int num;
        // read line
        iFile >> instruction >> num;

        // based on instruction do the correct move
        if (!instruction.compare("forward")) horizontal += num;
        else if (!instruction.compare("down")) depth += num;
        else depth -= num;        
    }

    cout << "Result is " << horizontal * depth << endl;
}