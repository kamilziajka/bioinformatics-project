//
// Created by mateusz on 20.12.15.
//

#pragma once

#include <cstdlib>
#include <time.h>


class Dice {
public:
    Dice(int prob1, int prob2, int prob3, int prob4, int prob5, int prob6) : PROBS{prob1, prob2, prob3, prob4, prob5,
                                                                                   prob6},
                                                                             MAX(prob1 + prob2 + prob3 + prob4 + prob5 +
                                                                                 prob6) {
        srand(time(NULL));
    }

    int Next();

private:
    const int PROBS[6];
    const int MAX;
};


