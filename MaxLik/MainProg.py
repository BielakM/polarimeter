import MaxLik as ML
import numpy as np

#Ideal projectors for WP
# H, D, R, V, A, L
H = np.array([1,0])
V = np.array([0,1])
D = (H + V)/np.sqrt(2)
A = (H - V)/np.sqrt(2)
R = (H + 1j * V)/np.sqrt(2)
L = (H - 1j * V)/np.sqrt(2)
states = [H, V, D, A, R, L]

#projectors Pi_i
projectors = []
for state in states:
	projectors.append(np.outer(state,state.conj()))

#Measured output from DET (ADC [V])
in_data = [6.67265857458,0.00272742509842,3.30350962877,3.36134728193,3.60658968687,3.31671561003]
[rho,stokes] = ML.Maxlik(in_data, projectors)

print ('Stokes:' + str(stokes))
print (rho)

print ('P = ' + str(ML.Purity(rho)))
print ('F(H) = ' + str(ML.Fidelity(rho,projectors[0])))
