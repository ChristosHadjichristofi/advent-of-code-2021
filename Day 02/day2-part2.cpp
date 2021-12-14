#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int horizontal = 0, depth = 0, aim = 0;
    ifstream iFile("input.txt");

    while (!iFile.eof()) {
        string instruction;
        int num;
        // read line
        iFile >> instruction >> num;

        // based on instruction do the correct move
        if (!instruction.compare("down")) aim += num;
        else if (!instruction.compare("up")) aim -= num;
        else {
            horizontal += num;
            depth += aim * num;
        }       
    }

    cout << "Result is " << horizontal * depth << endl;
}