Quantum Capacitance of 2D Material - I 
=======================================

Now, we will derive an expression for the quantum capacitance of a 2D material.
Consider a neutral isolated sheet of degenerately doped 2D semiconductor of area :math:`A`.
Let the geometric capacitance of the sheet per unit area be :math:`C_0`.
The equilibrium condition of the sheet is shown on the left side of the figure below.
The density of states :math:`D(E)` is plotted as a function of energy :math:`E`.
The area under the blue curve in the figure represents the total number of free electrons per unit area, :math:`N_0`.

As we have seen in the chapter on carrier statistics, for degenerately doped 2D semiconductors,
the number of free electrons can be written as

.. math::
  N_0 = D_0(E_F - E_0)

where :math:`D_0` is the density of states, :math:`E_F` is the Fermi energy and :math:`E_0` is the first subband energy.
Now, suppose we add :math:`\delta N` electrons per unit area to the sheet. 
This means we add an additional charge of :math:`\delta \sigma = e \delta N` to the sheet.
This will lead to a change in electrostatic potential :math:`\delta \phi_e  = eC_0\delta N`.
A change in electrostatic potential is depicted as an upward shift in the bands by :math:`e\delta \phi_e`
on the right side of the figure above.
Therefore the first subband :math:`E_0` is at :math:`E_0 + e\delta \phi_e` now.

What about the change in the Fermi level ? Let the Fermi level shift by :math:`\delta E_F`.
The new Fermi level is at :math:`E_{F1} = E_F + \delta E_F`. 
The new carrier concentration :math:`N_1 = N_0 + \delta N` is shown as the blue shaded area in the figure above.
We can write it as 

.. math::
  N_1 = N_0 + \delta N = D_0(E_F + \delta E_F - (E_0 + e\phi_e))

From this equation, it is very easy to conclude that -

.. math::
  \delta E_F = e\phi_e + \frac{\delta N}{D_0}

This equation shows that the shift in Fermi energy (:math:`\delta E_F`) is not equal 
to the shift electrostatic potential energy (:math:`e\phi_e`).
There is an additional shift of :math:`\delta N / D_0`. 
However, in the limit that the density of states is very high, :math:`D_0 \to \infty`, 
the shift in Fermi level is  nearly equal to the shift in electrostatic potential energy.

.. math::
  \delta E_F \approx e\phi_e \ (D_0 \to \infty)

We have already seen the physics behind this previously.
A high density of states at a given energy implies that we can pump more electrons to  a given energy. 
In contrast, a low density of states implies we need to go to higher energy levels to add more electrons.

Classical physics assumes a very high density of states. 
In such a situation, we can see that the system's capacitance is nearly the same as that of its geometrical/electrostatic capacitance.

.. math::
  C = e\frac{\delta q}{\delta E_F} \ approx \frac{\delta q}{\phi_e} = C_0


