//
// Created by mateusz on 20.12.15.
//

#include "Dice.h"

int Dice::Next() {
    int random = rand() % MAX;

    int next = 0;
    while(random >= PROBS[next]) {
        random -= PROBS[next];
        ++next;
    }

    return next + 1;
}
