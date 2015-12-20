#!/bin/bash

d1="2 2 2 2 1 1"
d2="2 2 2 2 1 1"
t1="1 1"
t2="1 1"
tosses="100"

echo $d1 > data
echo $d2 >> data
echo $t1 >> data
echo $t2 >> data

echo "$d1 $d2 $t1 $t2 $tosses" | ./Bio 1> >(tee | tail -n+5 >> data) 2> >(tee > dice)
