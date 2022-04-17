#!/bin/bash

echo "------ JudgeGuest ------"
mkdir tmp 

filename=$1

echo "Test on: ${filename}"
echo "------------------------"



if [[ $? == "1" ]]; then
	echo "Compile Error"

else	
	case_id=0

	while $(cp ./testcase/${case_id}.{in,out} ./tmp/ &>/dev/null) ; do

		python3 $1 < ./tmp/${case_id}.in > ./tmp/${case_id}.myout 
                if [[ $? != "0" ]]  ; then
		       echo "${case_id}        CE / RE"	
		else	
        		diff -wB ./tmp/${case_id}.out ./tmp/${case_id}.myout 1> /dev/null

			if [[ $? == "1" ]];  then
				echo "${case_id}        Wrong Answer"
			else
				echo "${case_id}        Accepted"
			fi
                fi
		((case_id+=1))
	done

fi

rm -r tmp
