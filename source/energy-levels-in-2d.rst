Energy Levels in 2D Semiconductors
===================================

2D materials are atomically thin sheets.
As a result, the electrons in a 2D material are confined in one direction while free in the other two directions.
Without loss of generality, we can assume that the electron is confined in the :math:`z` direction and free in the :math:`x-y` plane.
We will also assume that the sheet is :math:`L`. :math:`L` typically has atomic length scales.

The Schrodinger equation for electrons in such a system is

.. math:: -\frac{\hbar^2}{2m} \nabla^2 \Psi + V(z)\Psi = E\Psi

The electron  potential depends only on :math:`z` due to its confinement.
The :math:`V(z)` is an infinite potential well, shown in the figure below.


The above problem can be easily solved by separating the variables.
We can write the wavefunction :math:`\Psi` of the electron as :math:`\Psi = \Psi_{xy} \Psi_z`,
where :math:`\Psi_{xy}` depends only on :math:`x` and :math:`y`, while :math:`\Psi_z` depends only on :math:`z`.
Similarly, the total energy of the electron can be represented as :math:`E = E_{xy} + E_z`.
We will not do the (fairly simple) mathematics to derive the results.
Rather, we will give the results and justify them physically.

The electron is free in the :math:`x-y` plane.
It should, therefore, have a free electron wavefunction.
:math:`\Psi_{xy} \propto e^{i(k_xx + k_yy)}`. Here :math:`k_x` and :math:`k_y` can take any real values.
The energy component of the electron along the :math:`x-y` plane can then be written as

.. math:: E_{xy} = \frac{\hbar^2}{2m} (k_x^2 + k_y^2)

Since :math:`k_x` and :math:`k_y` can take any real value, the energy component :math:`E_{xy}` can take continuous values :math:`E_{xy} \ge 0`.

Along the :math:`z` direction, the electron is trapped in an infinite potential well.
From elementary quantum mechanics, we know that the wavefunction of such an electron is :math:`\Psi_z \propto \sin\big(\frac{n\pi z}{L}\big)`.
Here :math:`n` is only allowed to be a positive integer (:math:`n = 1,2,3 \dots`).
The energy component in this direction also has an exact form of electron's energy in an infinite potential well.

.. math:: E_z = \frac{n^2\pi^2\hbar^2}{2mL^2},\ n=1,2,3\dots

Combining both expressions, we now get the expression for the total energy of the electron in a confined 2D sheet.

.. math:: E = \frac{\hbar^2}{2m} (k_x^2 + k_y^2) +  \frac{n^2\pi^2\hbar^2}{2mL^2},\ n=1,2,3\dots

1. The energy of an electron in a 2D system is *continuous*. :math:`E` can take any value greater than :math:`\frac{\pi^2\hbar^2}{2mL^2}`.  In a potential well, the total energy is *quantized*. However, here, only a part of the energy is quantized.
2. Every electronic state in the system can be uniquely described by four numbers - :math:`n`, :math:`k_x`, :math:`k_y` and spin :math:`s`. :math:`n` can take only positive integer values, while :math:`k_x` and :math:`k_y` can take continuous real values. Spin :math:`s` can be take two values :math:`+\frac{1}{2}` and :math:`-\frac{1}{2}`.
3. We know from Pauli's exclusion principle that two electrons (being Fermions) cannot have identical quantum states. Therefore, no two electrons in the system can have an identical set of the four quantum numbers.
4. Often, it is convenient to define :math:`n` as the *principal* quantum number. All the energy states that have a given principal quantum number are said to belong to :math:`n^{th}` subband. For example, all the electrons having :math:`n=2` are said to be in the second subband.

The above diagram schematically represents the energy levels of the system.
The discrete energy levels of :math:`E_z` are marked :math:`E_z^1`, :math:`E_z^2` and :math:`E_z^3`
which correspond to :math:`n=1`, :math:`n=2` and :math:`n=3` respectively.
Some arbitrary energy leves :math:`E_1`, :math:`E_2` and :math:`E_3` are also shown.

1. No electron state can have energy level :math:`E_1` as it is below the first quantum level of :math:`E_z`. Such a case would lead to a negative :math:`E_{xy}` which is physically not possible.
2. The energy level :math:`E_2` is allowed for a quantum state. Such a state can have only one possible principal quantum number :math:`n=1`. However, this state can have infinitely many possible :math:`k_x` and :math:`k_y`. All the real :math:`k_x` and :math:`k_y` which satisfy the equation :math:`\frac{\hbar^2}{2m} (k_x^2 + k_y^2) = E_1 - E_z^1` are allowed.
3. A state with energy level :math:`E_3` can have two principal quantum numbers, :math:`n=1` and :math:`n=2` as shown in the figure. Again, for each state, infinitely many :math:`k_x` and :math:`k_y` are allowed.

If we extrapolate this trend it is easy to see that energy levels between :math:`E_z^3` and :math:`E_z^4`
can have three possible principle quantum numbers :math:`n=1`, :math:`n=2` and :math:`n=3`.
This subtle point, though trivial, is not usually mentioned explicitly in most works on 2D materials.
