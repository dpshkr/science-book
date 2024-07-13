Quantum Capacitance
====================

Consider a very small quantum dot of radius :math:`R`.
The quantum dot's energy levels (band diagram) are shown in the figure below.
Because of its small size, it has quantized energy levels denoted by :math:`E_1`, :math:`E_2` and so on.
Suppose we put an electron in it. 
The electron occupies the first energy level :math:`E_1`. 
The quantum dot is now charged. 
As a result, the quantum dot now possesses electrostatic potential energy given by
:math:`\delta \phi_e = -\frac{e}{4\pi\epsilon_0R} = -\frac{e}{C_0}`, where :math:`e` is the absolute value of fundamental electron charge.
This is shown on the right side of the band diagram where all the bands are shifted by :math:`-e\delta \phi_e`.

Now, we want to put a second electron. 
Already, the electron needs to possess an additional energy of :math:`-e\phi_e` 
, compared to the first electron, to be deposited now, as the band diagram has shifted upwards.
This shift in all the energy levels due to electrostatic potential is what is 
captured by the geometrical/electrostatic capacitance.
However, we must remember that the second electron cannot be put at the level :math:`E_1`.
This follows from the famous Pauli exclusion principle [#]_.
Rather, it has to go to the energy level :math:`E_2`. 
Therefore, to put a second electron, we must provide an additional energy given by :math:`E_2 - E_1` to the second electron
(in addition to the electrostatic potential energy).
This is the origin of quantum capacitance.
The additional energy required (compared to only electrostatic energy) is captured by quantum capacitance.

The physical origin of quantum capacitance is due to two quantum phenomena -

1. Discretization of energy levels.
2. Pauli's exclusion principle.

Had it not been for Pauli, we could have continued to put electrons in the energy level :math:`E_1` 
only hindered by the additional electrostatic potential energy.
Similarly, if the energy levels are extremely close, 
as in the case of 3D bulk material, we would not be able to observe any significant change as :math:`E_2 - E_1 \ll -e\phi_e`.

.. [#] If you consider spin degeneracy, there is room for one more electron. After that, there is no more allowance.
