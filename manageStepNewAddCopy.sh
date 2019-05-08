#!/bin/bash
#Go through all the lines in the file, write the step name and date


stepShort() {
    echo "entered"$1
    if [ "$1" == "genSimCrabConfig" ]
    then
	echo "entered2"
	stepName="GENSIM"
    elif [ "$1" == "recoCrabConfig" ]
    then
	stepName="RECO"
    elif [ "$1" == "aodCrabConfig" ]
    then
	stepName="AOD"
    elif [ "$1" == "miniAODSIM_crabConfig" ]
    then
	stepName="MINIAOD"
    fi
}

jobCheck(){
#crab status $1
if [ $# -lt 1 ] ; then
    echo Enter the directory of the crab job being checked as the sole argument
    jobChecker="3"
fi
if crab status $1 | grep "Publication status:" | grep "100.0%"
then
    echo "0"
    jobChecker="0"
elif crab status -d $1 | grep -e "running.*)"
then
    echo "2"
    jobChecker="2"
elif crab status -d $1 | grep -e "idle"
then
   echo "2"
   jobChecker="2"
else
    echo "1"
    jobChecker="1"
fi
}

#particle=''
minMass=''
maxMass=''
lambda=''
#helicity=''
date=''
stepName=''
jobChecker=''
textFileDir="$PWD/textFiles/"
for file in $PWD/textFiles/*.txt
do
    echo "fileName "$file
    lineNum=-1
    cat $file | while read line
    #echo "Text read from file: $line"
    do
	lineNum=$(($lineNum+1))
	i=0
	for object in $line
	do
	    obj[$i]=$object
	    echo ${obj[$i]}
	    i=$((i+1))
	done 
	if [ "${obj[0]}" == " " ]
	then
	    break 2
	fi
	if [ "${obj[0]}" == "300" ] || [ "${obj[0]}" == "800" ] || [ "${obj[0]}" == "1300" ] || [ "${obj[0]}" == "2000" ]
	then
#	    particle="${obj[0]}"
	    minMass="${obj[0]}"
	    maxMass="${obj[1]}"
	    lambda="${obj[2]}"
#	    helicity="${obj[4]}"
	    date="${obj[3]}"
	    continue
	fi
	stepNameOld=${obj[0]}
	stepShort "$stepNameOld"
	echo "stepNameOld: "$stepNameOld
	echo "stepName: "$stepName
	crabProjectName=$PWD'/'$stepNameOld'/crab_projects/crab_'$stepName'_M'$minMass'to'$maxMass'_LED_L'$lambda'_13TeV_'$date
	shortCrabProjectName='crab_'$stepName'_M'$minMass'to'$maxMass'_LED_L'$lambda'_13TeV_'$date
	echo "our crab project name is " $crabProjectName
	fullTextFile="$file"
	#echo 'crabProjectName '$crabProjectName
 	#Check if we need to move on, unless it is the miniAODSIM, in which case it does not need to proceed
	jobCheck "$crabProjectName"
	if [ "$jobChecker" == "0" ]
	then
	    if [ "$stepName" != 'miniAODSIM_CrabConfig' ]
	    then
		echo "in here"
		newLine=$(($lineNum+1))
		obj[0]=" "
		/uscms/home/avanderp/nobackup/CMSSW_9_3_6/src/GenStudy/Dimuon/test/moveOnCopy.sh $newLine "$stepNameOld" "$fullTextFile" "$minMass" "$maxMass" "$lambda" "$date"
	    fi
	#If the job is completed on miniAOD, then this adds to the completeCounter
	elif [ "$jobChecker" == "0" ]
	then
	    echo jobChecker was 0
	    if [ "$stepName" == 'miniAODSIM_CrabConfig' ]
	    then
		obj[0]=" "
		echo $crabProjectName 'is completed!'
	    fi
	#Check to resubmit jobs
	elif [ "$jobChecker" == "1" ]
	then
	    cur=$PWD
	    echo jobChecker was 1
	    echo $crabProjectName
	    /uscms/home/avanderp/nobackup/CMSSW_9_3_6/src/GenStudy/Dimuon/test/resubmitJobsNew.sh $stepNameOld $shortCrabProjectName
	    cd $crabProject
	    echo $crabProjectName ' is being resubmitted to step ' $stepName
	    cd $cur
	    obj[0]=" "
	#If the job is still running, then this adds to the runningCounter
	elif [ "$jobChecker" == "2" ]
	then
	    echo jobChecker was 2  
	    echo $crabProjectName ' is still runnning on step ' $stepName
	    obj[0]=" "
	else
	    echo "Nothing Matched! :("
	    obj[0]=" "
	fi
	if [ "${obj[0]}" == "genSimCrabConfig" ] || [ "${obj[0]}" == "recoCrabConfig" ] || [ "${obj[0]}" == "aodCrabConfig" ] || [ "${obj[0]}" == "miniAODSIM_crabConfig" ]
	then
	    obj[0]=" "
	fi
    done
done