#include <iostream>
#include "Dice.h"
#include <memory>
#include <Croupier.h>

using namespace std;

int main() {

    int diceProbs[6];
    int transProbs[4];
    int tosses;

    cout << "Enter 1st dice probabilities(6 integers):" << endl;
    for (int i = 0; i < 6; i++) {
        cin >> diceProbs[i];
    }
    auto dice1 = make_unique<Dice>(diceProbs[0], diceProbs[1], diceProbs[2], diceProbs[3], diceProbs[4], diceProbs[5]);

    cout << "Enter 2nd dice probabilities(6 integers):" << endl;
    for (int i = 0; i < 6; i++) {
        cin >> diceProbs[i];
    }
    auto dice2 = make_unique<Dice>(diceProbs[0], diceProbs[1], diceProbs[2], diceProbs[3], diceProbs[4], diceProbs[5]);

    cout << "Enter transistion probabilities(d1t1, d1t2, d2t1, d2t2):" << endl;
    for (int i = 0; i < 4; i++) {
        cin >> transProbs[i];
    }
    Croupier croupier(move(dice1), move(dice2), transProbs[0], transProbs[1], transProbs[2], transProbs[3]);

    cout << "Enter number of tosses:" << endl;
    cin >> tosses;
    
    for (int i = 0; i < tosses; i++) {
        cerr << croupier.CurrentDice() - 1 << " ";
        cout << croupier.Next() << " ";
        /*if (croupier.HasJustChangedDice()) {
            cout << "d" << croupier.CurrentDice() << " ";
        }*/
    }

    return 0;
}