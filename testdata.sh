#!/bin/bash

echo "Generating testdata"
echo "------------------------"

if [[ -d "testdata" ]]; then
  rm -rf testdata
fi

mkdir testdata

cnt=1
  for i in ./subtasks/subtask*.py; do
    for ((j = 0 ; j < 5 ; j ++)); do
      python3 $i > ./testdata/$cnt.in
      python3 csie_night.py < ./testdata/$cnt.in  > ./testdata/$cnt.out
      ((cnt+= 1))
    done
  done

echo "done."
