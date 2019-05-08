#!/bin/bash
dirname=$PWD/textFiles
genSimName=$PWD'/genSimCrabConfig'
genCrab=$genSimName'/crab_projects'
recoName=$PWD'/recoCrabConfig'
recoCrab=$genSimName'/crab_projects'
aodName=$PWD'/aodCrabConfig'
aodCrab=$genSimName'/crab_projects'
miniAodName=$PWD'/miniAODSIM_crabConfig'
miniAodCrab=$genSimName'/crab_projects'
if [ -d $dirname ]
then
    :
else
    mkdir $dirname
fi
if [ -d $genSimName ]
then
    :
else
    mkdir $genSimName
fi
if [ -d $recoName ]
then
    :
else
    mkdir $recoName
fi
if [ -d $aodName ]
then
    :
else
    mkdir $aodName
fi
if [ -d $miniAodName ]
then
    :
else
    mkdir $miniAodName
fi
if [ -d $genCrab ]
then
    :
else
    mkdir $genCrab
fi
if [ -d $recoCrab ]
then
    :
else
    mkdir $recoCrab
fi
if [ -d $aodCrab ]
then
    :
else
    mkdir $aodCrab
fi
if [ -d $miniAodCrab ]
then
    :
else
    mkdir $miniAodCrab
fi
python /uscms/home/avanderp/nobackup/CMSSW_9_3_6/src/GenStudy/Dimuon/test/callStart.py
#write out current crontab
#crontab -l > mycron
#echo new cron into cron file to submit every 2 hours
#echo "*/5 * * * * /uscms/home/pdong/work/IMSACMS/scripts/manageStepNewAddCopy.sh" >> mycron
#install new cron file
#crontab mycron
#rm mycron
