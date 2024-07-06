Quantum Capacitance 
====================

Consider an uncharged 2D conductor (or semiconductor) of area :math:`A`. 
The band diagram of the conductor is shown below.

.. figure::
	/_static/images/quantum-capacitance.png

The conductor has a Fermi level at :math:`E_F` and first sub-band energy at :math:`E_0`.
We will assume the conductor to be at 0 K (only for mathematical convenience). As you will see, the analysis is easily generalized to higher temperatures.
Recall that at 0 K, all the states below the Fermi level are filled,
while all states above the Fermi level are empty.
The free electron concentration in such circumstances is then given by the area of the shaded curve, as shown in figure -

.. math::
	n_0 = AD_0(E_F - E_0)

This free electron concentration is compensated by some fixed ion concentration to make the conductor neutral.

Now we would like to add a small number of electrons, :math:`\delta n` to the conductor. When we do so, the conductor will now become charged, with a charge given by :math:`\delta q = -e\delta n`.
A charged body acquires an  electrostatic potential :math:`\delta \phi_e`.
This electrostatic potential is due to Coulomb forces.
As such, this electrostatic potential depends only on the charge added (:math:`\delta q`) and the geometry of the conductor - shape and dimensions. Although we do not have any simple analytical formula for a 2D sheet of conductor, had our conductor been a sphere of radius :math:`R`, the change in electrostatic potential would be 

.. math::
	\delta \phi_e = \frac{\delta q}{4\pi\epsilon_0R}
	
As we mentioned, :math:`\delta \phi_e` depends only on the charge added and the geometry of the 
conductor - shape and dimensions ( sphere and radius :math:`R` respectively). 
In classical electromagnetics, the capacitance of the conductor is defined by 

.. math::
	C_0 = \frac{\delta q}{\delta \phi_e}

However, let us take a closer look at the band diagram.
As you can see due to an additional electrostatic potential energy :math:`\delta \phi_e`, the band diagram shifts upwards by :math:`e\delta \phi_e`.
The first subband energy is at :math:`E_0 + e\delta \phi_e` now.

However, what happens to the Fermi level?
Let us assume that Fermi level also changes by :math:`\delta E_F` so that the new Fermi level is :math:`E_{F1} = E_F + \delta E_F`.
The number of electrons is now given by the blue-shaded area -

.. math ::
	n_1 = AD_0(E_{F1} - (E_0 + e\delta \phi_e))

The change in number of electrons :math:`\delta n = n_1 - n_0` is then given by -

.. math ::
	\delta n = AD_0(\delta E_F - e\delta \phi_e)

In the above equation, we know all three quantities, except :math:`\delta E_F`, which can be solved as 

.. math ::
	\delta E_F = e\delta \phi_e + \frac{\delta n}{AD_0}

In the above equation, we will club :math:`\delta n / A` into  :math:`\delta N_e` - the change in electron concentration rather than electron number.

.. math ::
	\delta E_F = e\delta \phi_e + \frac{\delta N_e}{D_0}
	
As you can see, the change in Fermi level also depends on material properties, through its dependence on :math:`D_0`.
In the case of extremely high density of states (:math:`D_0 \to \infty`), :math:`\delta E_F` can be approximated as :math:`e\delta \phi_e`.

.. math ::
	\delta E_F \approx e\delta \phi_e \ (D_0 \to \infty)

We know from elementary statistical and semiconductor physics that we can only measure the Fermi energy, also known as electrochemical potential.
It is impossible to measure or use the electrostatic potential alone [#]_. 
A more accurate definition of capacitance is given by 

.. math::
	C = e\frac{\delta q}{\delta E_F}

If the density of states is very large, as with a typical metal, the above definition reduces to the one given in classical physics.
However, there can be a significant deviation from classical physics for low-DOS materials, as with typical low-dimensional materials.

.. [#] A classic example of this is the p-n junction diode. Although the junction has built-in electrostatic potential due to charge separation, we cannot measure it with a voltmeter. 
