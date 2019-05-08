#!/usr/bin/env python
#-*- coding: utf-8 -*-

from RunType import RunType
import subprocess
#from MasterPythonScript import startCrabJobs

#CURRENTLY THIS DOES NOT WORK!!!!!!!!
#def email():
  #  emailAddress = subprocess.check_output('whoami', shell=True) + '@fnal.gov'
  #  message = 'Your jobs have finished running! :)'
  #  subject = 'Jobs Finished'
  #  emailCommandString = 'mail -s ' + subject + ' ' + emailAddress + ' <<< ' + message
  #  emailOutput = subprocess.check_output('emailCommandString', shell=True)

#All the variables
#particleType = ['EE', 'MuMu']
minMass = ['300','800','1300','2000']
#lambdas = ['16','24','32','40','100000']
lambdas = ['5', '6', '7', '8', '9', '10', '11', '12']
#helicitys = ['LL', 'LR', 'RR']
#interferences = ['Con', 'Des']

masterList = [] #List that stores all the different combinations

#email() # Checks to see if the email function works

#Asks for Lepton Type and sets parameters for getting all combinations
def makeArray():
#    leptonType = raw_input('Particle Type (EE, MuMu, ALL): ')
#    if leptonType == 'EE':
#        pStart = 0
#        pEnd = 1
#    elif leptonType == 'MuMu':
#        pStart = 1
#        pEnd = 2
#    elif leptonType == 'ALL':
#        pStart = 0
#        pEnd = 2
#    else:
#        raise ValueError('You entered an incorrect lepton type!') #Throws a Value Error if wrong value is inputed

	#Asks for Min Mass and sets parameters for getting all combinations
    massCut = raw_input('Minimum Mass (300,800,1300,2000, ALL): ')
    if massCut == '300':
        mStart = 0
        mEnd = 1
    elif massCut == '800':
        mStart = 1
        mEnd = 2
    elif massCut == '1300':
        mStart = 2
        mEnd = 3
    elif massCut == '2000':
        mStart = 3
        mEnd = 4
    elif massCut == 'ALL':
        mStart = 0
        mEnd = 4
    else:
        raise ValueError('You entered an incorrect minimum mass cut!')
	
	#Asks for Lambdas and sets parameters for getting all combinations
    lambdaValue = raw_input('Lambda (5,6,7,8,9,10,11,12, ALL): ')    
    if lambdaValue == '5':
        lStart = 0
        lEnd = 1
    elif lambdaValue == '6':
        lStart = 1
        lEnd = 2
    elif lambdaValue == '7':
        lStart = 2
        lEnd = 3
    elif lambdaValue == '8':
        lStart = 3
        lEnd = 4
    elif lambdaValue == '9':
        lStart = 4
        lEnd = 5
    elif lambdaValue == '10':
        lStart = 5
        lEnd = 6
    elif lambdaValue == '11':
        lStart = 6
        lEnd = 7
    elif lambdaValue == '12':
        lStart = 7
        lEnd = 8
    elif lambdaValue == 'ALL':
        lStart = 0
        lEnd = 8
    else:
        raise ValueError('You entered an incorrect lambda value!')
    
	#Asks for helicities and sets parameters for getting all combinations
#    helicity = raw_input('Helicity (LL, RR, LR, ALL): ')
#    if helicity == 'LL':
#        hStart = 0
#        hEnd = 1
#    elif helicity == 'LR':
#        hStart = 1
#        hEnd = 2
#    elif helicity == 'RR':
#        hStart = 2
#        hEnd = 3
#    elif helicity == 'ALL':
#        hStart = 0
#        hEnd = 3
#    else:
#        raise ValueError('You entered an incorrect helicity type!')
    
	#Asks for interferences and sets parameters for getting all combinations 
#    interference = raw_input('Interference (Con, Des, ALL): ')
#    if interference == 'Con':
#        iStart = 0
#        iEnd = 1
#    elif interference == 'Des':
#        iStart = 1
#        iEnd = 2
#    elif interference == 'ALL':
#        iStart = 0
#        iEnd = 2
#    else:
#        raise ValueError('You entered an incorrect interference type!')
    
    
	#Takes all the parameters when asking for variables to create a loop
	#that gets every combination and sets the max mass based off the
	#min mass.
#    for i in range(pStart, pEnd):
    for j in range(mStart, mEnd):
        if minMass[j] == '300':
            maxMass = '800'
        elif minMass[j] == '800':
            maxMass = '1300'
        elif minMass[j] == '1300':
            maxMass = '2000'
        elif minMass[j] == '2000':
            maxMass = 'inf'
        else:
            raise ValueError('Maximum Mass was not found')
        for k in range(lStart, lEnd):
#               for l in range(hStart, hEnd):
#            for m in range(iStart, iEnd):
            values = [str(minMass[j]), str(maxMass), str(lambdas[k])]
            masterList.append(values)
    return masterList
	# startCrabJobs(masterList) #Will run the next python script that starts the Gen Sim process
                        



