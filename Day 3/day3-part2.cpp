#include <iostream>
#include <fstream>
using namespace std;

#define BIN_LEN 12

int main() {
    int counter[BIN_LEN] = {0};
    string gammaStr, epsilonStr;
    long gamma, epsilon;
    ifstream iFile("input.txt");

    // read all binary numbers and at the same time
    // each loop to every digit of each binary number
    // if the digit at position i is 1 then increment the counter[i]
    // else decrement the counter[i]
    while (!iFile.eof()) {
        string binNum;
        iFile >> binNum;
        for (int i = 0; i < binNum.length(); i++) {
            if (binNum[i] == '1') counter[i]++;
            else counter[i]--;
        }
    }

    // loop in counter array
    // if the number is positive then add 1 to the gammaStr/epsilonStr
    // if the number is negative then add 0 to the gammStr/epsilonStr
    for (int i = 0; i < BIN_LEN; i++) {
        if (counter[i] > 0) {
            gammaStr.append("1");
            epsilonStr.append("0");
        }
        else {
            gammaStr.append("0");
            epsilonStr.append("1");
        }
    }

    // convert string to integer
    gamma = stoi(gammaStr, 0, 2);
    epsilon = stoi(epsilonStr, 0, 2);

    cout << "Result is " << gamma * epsilon << endl;
}