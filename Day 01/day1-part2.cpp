#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    int prevSum, i = 0, increased = 0;
    vector<int> v;

    ifstream iFile("input.txt");

    while (!iFile.eof()) {
        int currentNum;
        iFile >> currentNum;
        v.push_back(currentNum);
    }

    for (int i = 0; i < v.size() - 2; i++) {
        int currSum = v.at(i) + v.at(i + 1) + v.at(i + 2);

        if (i == 0) {
            prevSum = currSum;
            continue;
        }
        
        if (currSum > prevSum) increased++;
        prevSum = currSum;
        
    }

    cout << "Increased " << increased << " times!" << endl;
}