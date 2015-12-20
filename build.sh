#!/bin/bash

mkdir -p temp
cd temp
cmake ../croupier
make
cp Bio ../
