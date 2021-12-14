#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include "board.hpp"

using namespace std;

int main() {

    vector<int> numbers;
    vector<Board> boards;
    string line;
    int n, score = 0;
    
    ifstream iFile("input.txt");
    getline(iFile, line);
    istringstream iss(line);

    // read first line and place all numbers in a vector
	while (iss >> n) {
        numbers.push_back(n);
        if (iss.peek() == ',') iss.ignore();
    }

    // read all boards, create board obj each time and place the numbers in the bingo board
    while (!iFile.eof()) {
        Board board;
        
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                iFile >> n;
                board.bingo[i][j] = n;
            }
        }

        boards.push_back(board);
    }

    for (int num : numbers) {
        for (Board &b : boards) {
            if (b.won) continue;

            bool exists = b.markIfExists(num);
            if (exists) {
                if (b.checkBingoRows() || b.checkBingoCols()) {
                    score = b.calcScore(num);
                    b.won = true;
                }
            }
        }
    }
    std::cout << "Last board won with score: " << score << endl;
}