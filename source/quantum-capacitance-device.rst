Quantum Capacitance Devices
============================

In the previous sections, we analyzed a quantum capacitance device in isolation.
A more probable configuration that you are likely to encounter is shown below.
A thin 2D sheet is sandwiched between two metallic plates.
The sheet is connected to a contact (huge reservoir of electrons) at a Fermi level :math:`E_F=0`.
As a result, the Fermi level of the sheet is constant, unlike in the previous cases, where the Fermi level could change.

Initially, the top and the bottom plates are maintained at an electrostatic potential of zero.
Under this condition, the band diagram of the 2D sheet is shown below.
If the area of the sheet is :math:`A`, the number of free carriers in the sheet are 

.. math::
  N = D_0(E_F - E_0)

These free carriers are compensated by fixed ions to keep the sheet neutral.

Suppose a bias of math:`\phi_0` is applied to the top plate while maintaining the bottom plate at 0.
The thin sheet may acquire some electrostatic potential and charge in this case.
However, the Fermi level remains constant as the sheet is connected to a contact.
We will assume that the sheet is now at an electrostatic potential :math:`phi`.
The result is that all the bands come down by an amount :math:`e\phi`. 
The additional charge induced in the sheet is given by (shown in the figure using a shaded region)

.. math::
  \sigma = -e \times (e\phi) \times D_0 = e^2D_0\phi = C_Q\phi

The electric fields in the top and bottom insulators are shown in the figure as :math:`E_1` and :math:`E_2`, respectively.
:math:`E_1 = \frac{\phi-\phi_0}{t}` and :math:`E_2 = \frac{\phi}{t}`. 
We can use the standard electrostatic boundary condition, :math:`\epsilon E_1 + \epsilon E_2 = -\sigma` 
(and some elementary math) to get

.. math::
  \phi = \frac{C_0}{2C_0 + C_Q} \phi_0

where :math:`C_0` is the geometrical capacitance (per unit area) of each section of the device given by :math:`\frac{\epsilon}{t}`.

Now let us examine two extreme cases of :math:`\phi`.

1. :math:`C_Q \gg C_0`. In this case :math:`\phi \approx 0`. This is the case of a standard metal with a very high density of states. The electric field in the 2D sheet is zero, which implies that the sheet has completely screened the electric field.
2. :math:`C_Q \ll C_0`. In this case, :math:`\phi \approx \phi_0/2`! The sheet is completely transparent. It is as if the sheet is not there at all. The electric field at the other bottom of the sheet is the same as the top.

The low-density state 2D material can, therefore, allow an electric field to penetrate them (without screening) despite being conductive. 
