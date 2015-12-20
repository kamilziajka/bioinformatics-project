#!/bin/bash

d1="2 2 2 2 1 1"
d2="2 2 1 1 2 2"
t1="3 2"
t2="2 3"
tosses="100"

echo $d1 > data
echo $d2 >> data
echo $t1 >> data
echo $t2 >> data

echo "$d1 $d2 $t1 $t2 $tosses" | ./Bio 1> >(tee | tail -n+5 >> data) 2> >(tee > dice)

python viterbi.py
cat dice
echo
python fwbw.py
