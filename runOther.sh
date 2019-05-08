#!/bin/bash
#Script that submits a crab job, specifically the genSimCrabConfig
#First argument is fileName, second is the pathway
currentDir=$PWD
cd $2
crab submit -c $1
echo $PWD $1
cd $currentDir
