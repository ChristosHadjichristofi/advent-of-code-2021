#include <iostream>
#include "board.hpp"

/* mark position only if the number n exists in the bingo board (-1 means marked) */
bool Board::markIfExists(int n) {
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (bingo[i][j] == n) {
                bingo[i][j] = -1;
                return true;
            }
        }
    }
    return false;
}

/* check rows for bingo */
bool Board::checkBingoRows(){
    for (int i = 0; i < 5; i++) {
        int sum = 0;
        for (int k = 0; k < 5; k++) sum += bingo[i][k];
        if (sum == -5) return true;
    }
    return false;
}

/* check columns for bingo */
bool Board::checkBingoCols(){
    for (int i = 0; i < 5; i++) {
        int sum = 0;
        for (int k = 0; k < 5; k++) sum += bingo[k][i];
        if ( sum == -5 ) return true;
    }
    return false;
}

/* calculate total score */
int Board::calcScore(int n) {
    int score = 0;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (bingo[i][j] != -1) score += bingo[i][j];
        }
    }
    return score * n;
}