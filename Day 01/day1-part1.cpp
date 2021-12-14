#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int prevNum, i = 0, increased = 0;
    ifstream iFile("input.txt");

    while (!iFile.eof()) {
        int currentNum;
        iFile >> currentNum;

        // first number read, nothing to compare
        if (i == 0) prevNum = currentNum;
        // compare currentNum with prevNum. If current > prev then increased++
        // if not do nothing. Every time after check make prevNum eq to currentNum
        else {
            if (currentNum > prevNum) increased++;
            prevNum = currentNum;
        }
        i++;
    }

    cout << "Increased " << increased << " times!" << endl;
}