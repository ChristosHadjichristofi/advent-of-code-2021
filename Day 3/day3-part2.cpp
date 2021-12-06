#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

#define BIN_LEN 12

string filter(int position, vector<string> v, bool mostCommon = true) {
    while (v.size() != 1 && position <= BIN_LEN) {
        vector<string> ones, zeros;
        for (string binNum : v) {
            if (binNum[position] == '1') ones.push_back(binNum);
            else zeros.push_back(binNum);
        }
        if (mostCommon) {
            if (ones.size() >= zeros.size()) v = ones;
            else if (zeros.size() > ones.size()) v = zeros;
        }
        else {
            if (ones.size() < zeros.size()) v = ones;
            else if (zeros.size() <= ones.size()) v = zeros;
        }
        position++;
    }
    return v.front();
}

int main() {
    vector<string> binNums;
    ifstream iFile("input.txt");

    while (!iFile.eof()) {
        string binNum;
        iFile >> binNum;
        binNums.push_back(binNum);
    }

    string oxygen = filter(0, binNums);
    string co2 = filter(0, binNums, false);

    cout << "Oxygen is " << stoi(oxygen, 0, 2) << endl;
    cout << "CO2 is " << stoi(co2, 0, 2) << endl;
    cout << "Answer is " << stoi(oxygen, 0, 2) * stoi(co2, 0, 2) << endl;
}