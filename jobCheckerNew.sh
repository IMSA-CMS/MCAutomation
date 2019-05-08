#!/bin/bash
#The first input is project directory
#Returns both text and exit code  0 if complete, 1 if something failed, and 2 if still running. 3 Means inappropriate argument quantity
jobCheck(){
echo "project name: "$1
if [ $# -lt 1 ] ; then
    echo Enter the directory of the crab job being checked as the sole argument
    result="3"
    printf "result=%s" "${result}"
fi
if crab status $1 | grep "Publication status:" | grep "100.0%"
then
    echo "0"
    result="0"
    printf "result=%s" "${result}"
elif crab status -d $1 | grep -e "running.*)"
then
    echo "2"
    result="2"
    printf "result=%s" "${result}"
elif crab status -d $1 | grep -e "idle"
then
   echo "2"
   result="2"
    printf "result=%s" "${result}"
else
    echo "1"
    result="1"
    printf "result=%s" "${result}"
fi
}

echo $1
echo $#
jobCheck $1
