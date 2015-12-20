//
// Created by mateusz on 20.12.15.
//

#include "Croupier.h"

int Croupier::Next() {
    int nextNumber;
    int oldDice = currentDice;

    if(currentDice == 0) {
        nextNumber = dice1_->Next();
        currentDice = transistionDice1.Next() - 1;
    } else {
        nextNumber = dice2_->Next();
        currentDice = transistionDice2.Next() - 1;
    }
    hasJustChangedDice_ = (currentDice != oldDice);

    return nextNumber;
}

bool Croupier::HasJustChangedDice() const {
    return hasJustChangedDice_;
}

int Croupier::CurrentDice() const {
    return currentDice + 1;
}