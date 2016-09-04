# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:39:55 2016

@author: bbalasub
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 20:27:07 2016

@author: bbalasub
"""
import sys
sys.path.append('../test')
sys.path.append('../lib')

import scipy
import ctypes 
import glmnet 
import importlib

importlib.reload(glmnet)

# parameters
baseDataDir= '/home/bbalasub/Desktop/Summer2016/glmnet/github/glmnet_python/data/'
testType = 'binomial'

# call test functions
if testType == 'gaussian':
    ##  elnet caller 
    y = scipy.loadtxt(baseDataDir + 'QuickStartExampleY.dat', dtype = scipy.float64)
    x = scipy.loadtxt(baseDataDir + 'QuickStartExampleX.dat', dtype = scipy.float64)
    fit = glmnet.glmnet(x = x, y = y, family = 'gaussian')
    print('fit:\n', fit)

if testType == 'binomial':
    # lognet caller
    x = scipy.loadtxt(baseDataDir + 'BinomialExampleX.dat', dtype = scipy.float64, delimiter = ',')
    y = scipy.loadtxt(baseDataDir + 'BinomialExampleY.dat', dtype = scipy.float64)
    fit = glmnet.glmnet(x = x, y = y, family = 'binomial')
    print('fit:\n', fit)
