#!/bin/bash
# This script submits the next step for submission. It takes the old step name, text file name, particle, min mass, maxmass, lambda, helicity, interference, date
#What it actually took was 1 $newLine 2 "$stepNameOld" 3 "$fullTextFile" 4 "$particle" 5 "$minMass" 6 "$maxMass" 7 "$lambda" 8 "$helicity" 9 "$interference" 10 "$date"
#What it takes now is 1 newline 2 stepNameOld 3 fullTextFile 4 minMass 5 maxMass 6 lambda 7 date


#This function changes the step name in the text file
changeStep()
{
#echo $3
sed -i "$1s/$2/$stepdir/" $4 #this is the particle ?
}
if [ $2 == 'genSimCrabConfig' ] ; then
    stepdir='recoCrabConfig'
    shortName='RECO'
elif [ $2 == 'recoCrabConfig' ] ; then
    stepdir='aodCrabConfig'
    shortName='AOD'
elif [ $2 == 'AODCrabConfig' ] ; then
    stepdir='miniAODSIM_CrabConfig'
    shortName='MINIAODSIM'
fi
projectDir=$PWD'crab_projects/crab_'$shortName'_M'$4'to'$5'_LED_L'$6'_13TeV_'$7
crabdir=$PWD'/'$stepdir'/crab_projects/'
#echo "project dir in moveOnCopy" $projectDir
if [ -d $projectDir ]
then
    echo "This step is already done"
else
    python /uscms/home/avanderp/nobackup/CMSSW_9_3_6/src/GenStudy/Dimuon/test/callRunOther.py $1 $stepdir $3
    changeStep $1 $2 $stepdir $3 
fi

#'import masterListManager; masterListManager.changeStep("$3", "$stepdir", "$4")' 
