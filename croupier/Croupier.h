//
// Created by mateusz on 20.12.15.
//

#pragma once

#include <memory>
#include <Dice.h>
#include <cstdlib>
#include <time.h>


class Croupier {
public:
    Croupier(std::unique_ptr<Dice> dice1, std::unique_ptr<Dice> dice2, int d1t1, int d1t2, int d2t1, int d2t2) :
            dice1_(std::move(dice1)), dice2_(std::move(dice2)),
            transistionDice1(d1t1, d1t2, 0, 0, 0, 0), transistionDice2(d2t1, d2t2, 0, 0, 0, 0), hasJustChangedDice_(false) {
        srand(time(NULL));
        currentDice = rand() % 2;
    }

    int Next();

    bool HasJustChangedDice() const;

    int CurrentDice() const;

private:
    const std::unique_ptr<Dice> dice1_, dice2_;
    Dice transistionDice1, transistionDice2;

    int currentDice;
    bool hasJustChangedDice_;
};


