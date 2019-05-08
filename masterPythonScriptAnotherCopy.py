#!/usr/bin/env python
import os
import getpass
import csv
import sys
import subprocess
from datetime import date
import datetime as dt
from datetime import datetime
sys.path.insert(0,'/uscms/home/avanderp/nobackup/CMSS@_9_3_6/src/GenStudy/Dimuon/test/')
from inputsNew import makeArray
from masterListManager import createTextFile, getLine
from testOutputData import getOutputDatasetInput
masterlist = [[]];
today=date.today().strftime("%B%d")
date=dt.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
dateFile=''
directory=subprocess.check_output("echo $PWD", shell=True)
directory=directory.rstrip()
#calls the inputsNew function to create initatiations for job requests, and begins the process to submit genSim by calling assignArray()
def startCrabJobs():

    #function call to inputsNew to get user request
    #createS an array of arrays (masterlist) with all request instantiations
    masterList=makeArray();
    print masterList
    #creates and writes to the log text file that keeps track of the current step
    createTextFile(masterList, today, date)
    dateFile=date
    #starts assigning values to each array to pass into makeGenSimFile() by using assignArray()
    for i in masterList:
        assignArray(i)




#takes arguments from a run-type style array and assigns them to variables to pass into makeGenSimFile()
def assignArray(run):

    #assigning variables to each array object/variable
    minMass=run[0]
    maxMass=run[1]
    lambdaValue=run[2]
    makeGenSimFile(minMass, maxMass, lambdaValue)
    #passing the assigned variables into makeGenSimFile() to fill in the template



#takes run type inputs to make a genSim config file through calling template substitution function createFile() and submits the config file
def makeGenSimFile(minMass, maxMass, lambdaValue):
    #fills a subsitution list with the run type inputs to be used in template substitution
    substitution = makeSubstitutionList(minMass, maxMass, lambdaValue)
    #opens up the genSim crab config template to be filled
    inputFilename = '/uscms/home/avanderp/nobackup/CMSSW_9_3_6/src/GenStudy/Dimuon/test/crabConfig_GENSIM_LED_template.py'
    newFile=open("/uscms/home/avanderp/nobackup/CMSSW_9_3_6/src/GenStudy/Dimuon/test/crabConfig_GENSIM_LED_template.py", 'r')
    inputFilenameInf='/uscms/home/avanderp/nobackup/CMSSW_9_3_6/src/GenStudy/Dimuon/test/crabConfig_GENSIM_LED_2000toinf_template.py'
    #creates the name for the output genSimConfig file
    outputFilename = directory + '/genSimCrabConfig/crabConfig_GENSIM_M' + \
        str(minMass) + 'to' + str(maxMass) + '_LED_L' + str(lambdaValue) + '.py'

    
    command = str("touch " + outputFilename)

    os.system('command')
    
    #fills in the genSim config template under the name of the new genSimConfig file
    if (maxMass=='inf'):
        createFile(substitution, inputFilenameInf, outputFilename)
    else:
        createFile(substitution, inputFilename, outputFilename)
    

    command2=str("/uscms/home/avanderp/nobackup/CMSSW_9_3_6/src/GenStudy/Dimuon/test/runGenSim.sh " + outputFilename)

    
    print(directory, "genSim", outputFilename)
    os.system(command2)




#creates a substitution list of run type inputs to put in a config file template
def makeSubstitutionList(minMass, maxMass, lambdaValue):

    #assigning variables for various other run type inputs as extracted from the given run type variables
    leptonTypes = {'EE':11, 'MuMu':13}
    helicityTypes = ['LL', 'LR', 'RR']
#    interferenceTypes = {'Con':'-', 'Des':''}
    #compiles the substitution list and returns it
    substitution = {'DATE':today,'LAMBDA':str(lambdaValue), 'MINMASS':minMass, 'MAXMASS':maxMass}
    return substitution




#This creates a new file and writes to the file (config file)
def createFile(substitution, inputFilename, outputFilename):

    #opens the crabConfig template to read
    with open(inputFilename, 'r') as input:

        #opens the new crabConfig file to input the filled template in
        with open(outputFilename, 'w') as output:

            #substitutes the run type inputs for each line in the template using substituteLine()
            for line in input:
                output.write(substituteLine(line, substitution))




#uses run type inputs to make a substitution in a line of the config file
def substituteLine(line, substitution):
    
    #loops through each run type input in the instatiation's array
    for key, value in substitution.items():

        #associates each input variable with its substitution key in the template
        replacementKey = '{$' + key.upper() + '}'

        #makes the substitution for the line and returns the filled line
        line = line.replace(str(replacementKey), str(value))
    return line


def makeSubstitutionListOther(minMass, maxMass, lambdaValue, date):

    #assigning variables for various other run type inputs as extracted from the given run type variables
    today = date
    leptonTypes = {'EE':11, 'MuMu':13}
    helicityTypes = ['LL', 'LR', 'RR']
#l    interferenceTypes = {'Con':'-1', 'Des':'1'}

    #makes the maxMassInput blank if there is no maximum mass cut
    if maxMass=="inf" :
        maxMassInput= ' '
    else:
        maxMassInput=maxMass

    #compiles the substitution list and returns it
    substitution = {'DATE':today, 'LAMBDA':str(lambdaValue), 'MINMASS':minMass, 'MAXMASS':maxMass}
    return substitution





#calls a script that will find the output data set for a given projectDirectory
def getCrabLog(projectDirectory, dataFormat):
    #print(projectDirectory)
    projectDirectory.rstrip()
    filename=str(getPrevStep(dataFormat) + '/crab_projects/' + projectDirectory)
    print("filename in the getCrabLog" + filename)
    return getOutputDatasetInput(filename)
 
#for word in optl:
#   print(word)
#  wordcounter+=1




#with a given step dataFormat, finds the associated pset to put in the config file
def getPSET(dataFormat):
    if dataFormat=='recoCrabConfig':
        pset='/uscms/home/avanderp/nobackup/CMSSW_9_3_6/src/GenStudy/Dimuon/test/mc17digiRECOcfg.py'
    elif dataFormat=='aodCrabConfig':
        pset='/uscms/home/avanderp/nobackup/CMSSW_9_3_6/src/GenStudy/Dimuon/test/mc17AODcfg.py'
    elif dataFormat=='miniAODSIM_crabConfig':
        pset='/uscms/home/avanderp/nobackup/CMSSW_9_3_6/src/GenStudy/Dimuon/test/mc17miniAODcfg.py'
    return pset

def getPrevStep(dataFormat):
    if dataFormat=='recoCrabConfig':
        prevStep='genSimCrabConfig'
    elif dataFormat=='aodCrabConfig':
        prevStep='recoCrabConfig'
    elif dataFormat=='miniAODSIM_crabConfig':
        prevStep='aodCrabConfig'
    return prevStep

def stepDirToStep(dataFormat):
    if dataFormat=='recoCrabConfig':
        step='RECO'
    elif dataFormat=='aodCrabConfig':
        step='AOD'
    elif dataFormat=='miniAODSIM_crabConfig':
        step='MINIAOD'
    elif dataFormat=='genSimCrabConfig':
        step='GENSIM'
    return step


 
#returns the userName   
def getUserName():
    return getpass.getuser()

#takes the run type inputs to make a subsitution list (including the outputDataSet) 
#fills a template and submit the next step's jobs
#updates the step log text file
def makeOtherFile(lineNum, dataFormat, fileName):
    line=getLine(int(lineNum)-2, fileName)
    words=line.split(" ")
    print "our line is "
    print words
    minMass=words[0]
    maxMass=words[1]
    lambdaValue=words[2]
    dateOfFile=words[3]
    
#assigns string variables to dataFormat and date
    dataFormat=str(dataFormat)


    #creates and writes to the log text file that keeps track of the current step
    #changeStep(leptonType, minMass, maxMass, lambdaValue, helicity, interference, date)

    #creates a substitution list from the run type inputs
    substitution = makeSubstitutionListOther(minMass, maxMass, lambdaValue, dateOfFile)

    #associates each dataFormat directory with the step to put in the template
    stepType = {'genSimCrabConfig':'GENSIM', 'recoCrabConfig':'DIGIRECO', 'aodCrabConfig':'AOD', 'miniAODSIM_crabConfig':'MINIAOD'}
    
    #finds the name of the crab project from the run type inputs
    #this isfrom the directory of the step just completed, this is in the format of requestName
    crabProjectName = str('crab_' + str(stepDirToStep(getPrevStep((dataFormat)))) + '_M' + minMass \
                              + 'to' + maxMass + '_LED_L' + lambdaValue \
                              + '_13TeV_' + dateOfFile)
    crabProjectNameNew=crabProjectName.rstrip()
    #some exception handling to check that there is an output dataset from the previous step
    #print("crab project name in masterPythonScriptAnotherCopy", str(crabProjectName))
    outputDataSet=getCrabLog(crabProjectNameNew, dataFormat)
    #try
                          #except RuntimeError as r:
        #print r
        #return

    #appends the output dataset to the substitution list
    #substitution.append('OUTPUTDATASET':outputDataSet)
    substitution['OUTPUTDATASET'] = outputDataSet
    
    #appends the step to the substitution list
    #substitution.append('STEP':str(stepDirToStep(dataFormat)))
    substitution['STEP'] = str(stepDirToStep(dataFormat))

    #appends the pset to the substitution list
    #substitution.append('PSET':)
    substitution['PSET'] = str(getPSET(dataFormat))


    #importing the config file template
    inputFilename = '/uscms/home/avanderp/nobackup/CMSSW_9_3_6/src/GenStudy/Dimuon/test/crabConfig_DIGItoMINIAOD_LED_template.py'

    #creating a file name for the filled config file template
    outputFilename = directory + '/' + dataFormat + '/crabConfig_' + stepDirToStep(dataFormat) + \
    str(minMass) + 'to' + str(maxMass) + '_LED' + str(lambdaValue) + '.py'
    print(outputFilename)
    #making the filled config file from the template 
    createFile(substitution, inputFilename, outputFilename)
    directoryNew=directory+'/' + dataFormat
    command4=str("/uscms/home/avanderp/nobackup/CMSSW_9_3_6/src/GenStudy/Dimuon/test/changeDate.sh " + lineNum + ' ' + today + ' ' + dateOfFile + ' ' + fileName)
    os.system(command4)
    #submitting crab jobs for the new config file
    command3=str("/uscms/home/avanderp/nobackup/CMSSW_9_3_6/src/GenStudy/Dimuon/test/runOther.sh " + outputFilename + ' ' + directoryNew)

    os.system(command3)
    #os.system('crab submit -c' + outputFilename)
    

#begins the process of moving on crab jobs to the next steps, dataFormat needs to be the next step in the process
def startCrabJobsOther(lineNum, dataFormat, fileName):
    #calls the file to make (from a template) and submit the config file
    makeOtherFile(lineNum, dataFormat, fileName)
    
    #startCrabJobsOther(sys.argv[1], sys.argv[2], sys.argv[3])





