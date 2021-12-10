#ifndef BOARD_H__
#define BOARD_H__

#include <iostream>

class Board {
public:
    int bingo[5][5];
    int markedCells;
    bool won;

    bool markIfExists(int n);
    bool checkBingoRows();
    bool checkBingoCols();
    int calcScore(int n);
    void print();
};

#endif