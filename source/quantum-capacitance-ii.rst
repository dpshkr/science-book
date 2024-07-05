Equivalent Circuit Model 
=========================

In the previous section, we have derived the following formula for change in electrochemical potential 
for a 2D conductor/semiconductor on the addition of additional electron charge density -

.. math ::
  \delta E_F = e\delta \phi_e + \frac{\delta N_e}{D_0}

The first term is due to Coulomb forces, while the second is due to the Pauli exclusion principle.
The Pauli exclusion principle prohibits us from depositing the new electrons into filled electron states and hence provide 
additional energy to deposit them in the higher energy unfilled states.

We know that the first term depends only on the geometry of the conductor and hence can be represented by the classical equation - 

.. math ::
  \delta \phi_e = \frac{\delta \sigma_e}{C_0}

where :math:`C_0` is the electrostatic capacitance per unit area and :math: `\delta \sigma_e` 
is the change in charge concentration per unit area (:math:`\delta \sigma_e = e\delta N_e`).
Similarly, the second term can be refactored as 

.. math ::
  \frac{\delta N_e}{D_0} = \frac{e\delta \sigma_e}{C_Q}

where :math:`C_Q \equiv e^2D_0` is defined as the **quantum capacitance** (per unit area).
Combining all the equations above, we finally have 

.. math ::
  \frac{\delta E_F}{e} = {\delta \sigma_e}\bigg(\frac{1}{C_Q} + \frac{1}{C_0}\bigg)

As previously defined, total capacitance per unit unit area :math:`C` is given by :math:`e\frac{\delta \sigma_e}{\delta E_F}`.

.. math ::
  \frac{1}{C} = \frac{1}{C_0} + \frac{1}{C_Q}

The total capacitance of the conductor is hence a series combination of the electrostatic geometrical capacitance (:math:`C_0`)
and the quantum capacitance (:math:`e^2D_0`). This is schematically shown in the figure below. 
