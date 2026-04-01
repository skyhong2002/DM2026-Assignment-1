import numpy as np

def MSE_grad(y,y_pred):
	'''
	Derivative of MSE loss w.r.t y_pred (not w)
	'''
	return (2/len(y))*(y_pred-y)

def MAE_grad(y,y_pred):
	'''
	Derivative of MAE loss w.r.t y_pred (subgradient at 0 is set to 0)
	'''
	return np.sign(y_pred-y)/len(y)

def logloss_sigmoid_grad(y,y_pred):
	'''
	Derivative of sigmoid + log loss combination is equivalent to derivative of MSE 
	'''
	return MSE_grad(y,y_pred)/2
