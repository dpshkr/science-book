Geometrical Capacitance
========================

In classical electromagnetics, we know that the capacitance of a conductor (or a semiconductor) [#]_ is defined as 

.. math::
  C_0 = \frac{\delta q}{\delta \phi_e}

where :math:`\delta q` is the charge put on the conductor and :math:`\delta \phi_e` is the change in the resulting electrostatic potential.
For example, consider a spherical conductor of radius :math:`R`.  
If we charge `\delta q` on the conductor, its electrostatic potential changes by :math:`\delta \phi = \frac{\delta q}{4\pi\epsilon_0}`.
This implies that its capacitance is :math:`C_0 = 4\pi\epsilon_0R`.

In quantum / nano-scale physics literature, this capacitance is usually called the *geometric capacitance* or *electrostatic capacitance*.
This is so because the capacitance only depends on the geometry of the charge distribution and not on any other conductor properties.
Of course, the distribution may, in turn, depend on the underlying material. 
For example, a conductor and semiconductor with the same geometry (shape and size) might have
different charge distributions, leading to different capacitances.
A good example of this is the MOS capacitor, which, despite being a normal parallel plate capacitor in geometry, 
has very different capacitance characteristics.
The bottom line, however, is the *charge distribution*.  

The physical origin of this capacitance lies in the electrostatic potential due to Coulomb forces. 
As we deposit more charges on a conductor, it requires more energy to charge the conductor further,
as the existing charges repel the new charges that need to be deposited.

.. [#] In this chapter, we will interchange the words conductor and semiconductor.
