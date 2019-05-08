#!/usr/bin/env python
#-*- coding: utf-8 -*-

class RunType:
    lambdaValue = 0
    interference = 0
    minMass = 0
    maxMass = 0

    def __init__(self, minM, maxM, l, i) :
        minMass = minM
        maxMass = maxM
        lambdaValue = l
        inteference = i
        
