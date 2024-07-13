Redefining Capacitance
=======================

Before deriving exact expressions for quantum capacitance, 
we will have to give a more general definition.
Capacitance is defined as 

.. math::
  C = \frac{1}{e} \frac{\delta q}{\delta E_F}

where :math:`\delta q` is the (additional) charge put on the conductor and 
:math:`E_F` is the resulting change in the *Fermi energy*.
This definition is almost similar to geometrical capacitance where electrostatic 
potential :math:`\delta \phi_e` has been replaced by the Fermi energy :math:`eE_F`.
This change is necessary as Fermi energy, also called electrochemical energy, 
encompasses both electrostatic and chemical energy - the energy due to the internal quantum structure of the system.

To look at how this change in definition helps, let us go to our previous example of the quantum dot.
Let us assume the conductor to be at temperature :math:`T=0\ K` (only for mathematical convenience).
We know that at :math:`T=0`, all the states below Fermi energy are occupied, while all states above it are empty.
Therefore, when there is no electron in the quantum dot, the Fermi energy has to be  between :math:`0` and :math:`E_1`.
When we put an electron in the quantum dot, its electrostatic potential increases 
and all the bands shift upwards by :math:`-e\phi_e`. 
However, the Fermi level has to shift by an additional amount.
This is shown in the figure below. The new Fermi level has to be between :math:`E_1` and :math:`E_2`, 
since the level :math:`E_1` is now filled. 
Had the Fermi level been shifted by the same amount as the electrostatic potential energy (shown in dashed lines), 
it would still lie below :math:`E_1`, implying no electron in the quantum dot.
When a second electron is added to the conductor, the Fermi energy lies between :math:`E_2` and :math:`E_3`.

As we can see, Fermi energy captures the additional quantum energy required to charge a conductance more.
We must also, at this point, remember that, for the external terminals, 
what really matters is only Fermi energy and not the electrostatic potential alone.
A classic example is the p-n junction diode, which shows zero reading when measured using a voltmeter in equilibrium
despite having a built-in electrostatic potential.
Therefore, even from a practical point of view, this change in definition is very much justified.
