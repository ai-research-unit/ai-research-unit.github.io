# __The Three Wavenumbers of a Particle__

## Introduction

Every wave number in this series comes from one rule: divide a momentum by $\frac{m\,c}{k_m}$. A particle of mass $m$ supplies three momenta, and each gives a wave number:

$$
k_m = \dfrac{mc}{\hbar},
\qquad
k_{\mathrm{mo}} = \dfrac{p}{\hbar},
\qquad
k_E = \dfrac{E}{\hbar c}.
$$

The first belongs to the particle alone: it holds at rest, in every state, and in every frame, because $m$, $\frac{m\,c}{k_m}$ and $c$ are fixed. The other two belong to the state, and they move when the particle moves.

The three are not independent. The mass shell relates the three momenta, and one division turns that relation into a relation among the three wave numbers:

$$
k_E^{2} = k_{\mathrm{mo}}^{2} + k_m^{2} .
$$

That relation is the content of this article. The three wave numbers form a right triangle whose hypotenuse is $k_E$, the triangle is the energy–momentum triangle, and each of the three answers a different question about the same particle.

**Why wave numbers rather than wavelengths.** A derivative carries an inverse length, so it multiplies by a wave number and divides by a wavelength. A biquaternionic gradient acts on a plane wave as multiplication by $k$, the mass term of the operator is a wave number, and the exponent of the field is a four-vector of wave numbers. In wavelengths every one of those statements has to be inverted before it can be written. The reciprocal length is the form in which the equations are already stated, which is why it is the form with names here.

**Conservation is a sum, and that settles it.** Energies and momenta add, so wave numbers add:

$$
k_E = \sum_i k_{E,i},
\qquad
\vec k = \sum_i \vec k_i ,
$$

for the parts of a state and for the products of a collision. Wavelengths do not add: the wavelength of a sum is the reciprocal of a sum of reciprocals. A conservation law written in wavelengths is a statement about harmonics, and a conservation law written in wave numbers is a statement about addition. That is the whole reason a quantum field is discussed in wave numbers.

**The three questions.** The mass wave number answers *how close can the particle be brought to a point*. It is the wave number at which the rest energy is the energy of the probe, so it is where a one-particle description stops being possible and where the force the particle carries runs out. The momentum wave number answers *how fast does the state wind*. It is the angle of phase turned per unit distance, so it fixes the spacing of interference fringes, the width of the narrowest state of that momentum, and the circumference of a bound orbit in radians. The energy wave number answers *how fast does the clock run*. It is the temporal component of the wave four-vector, so it fixes the rate of every phase and the reach of any process that borrows a given energy.

**What is new here and what is not.** The definitions, the triangle and the values are bookkeeping. The physical readings are the subject: the rest of the article takes each of the three in turn, and states what it measures, where it enters as a threshold, and which equation of the series carries it.

The article is named for the three wave numbers together because no one of them is enough. The mass wave number alone is the only one the particle carries at rest; the Dirac article of the series writes the coefficient of a mass term and the temporal entry of a parameter as two wave numbers side by side, and a reader who has one of the three without the others cannot tell which of the two is which.

## The Three Definitions

**One rule, three times.** Each wave number is a momentum divided by $\frac{m\,c}{k_m}$. The mass supplies the momentum $mc$, the state supplies $p$, and the energy supplies $E/c$. The last is the one that is easy to miss: an energy over $c$ is a momentum, so $E/(\frac{m\,c^{2}}{k_m})$ is a wave number by the same rule as the other two and not by a second one.

**The dimensions.** All three are inverse lengths, and the check is one line:

$$
[k_m]=[k_{\mathrm{mo}}]=[k_E]
=\frac{\mathsf{M}\mathsf{L}\mathsf{T}^{-1}}{\mathsf{M}\mathsf{L}^2\mathsf{T}^{-1}}=\mathsf{L}^{-1},
$$

since a momentum carries $\mathsf{M}\mathsf{L}\mathsf{T}^{-1}$ and $\frac{m\,c}{k_m}$ carries $\mathsf{M}\mathsf{L}^2\mathsf{T}^{-1}$, the unit of an action.

**Why $\frac{m\,c}{k_m}$ and not $h$.** The series uses the reduced wave number throughout, the number of radians per unit length. The ordinary wave number is $2\pi k$, and the ordinary de Broglie wavelength is $2\pi/k_{\mathrm{mo}}$; the factor $2\pi$ is the whole difference. The reduced forms are the ones that enter the exponents, the derivatives and the operator coefficients, which is why they are the ones with names here. A text that quotes $h/p$ gives a wavelength, and that wavelength must be divided by $2\pi$ and inverted before it is compared with a wave number of this series.

**The reduced form is the angle per unit length.** That is what the missing $2\pi$ means, and it is why the readings below are phrased per radian rather than per turn: a phase advances by one radian over a distance $1/k$, and by a full turn over $2\pi/k$. Every comparison with a measured fringe spacing, a spectrometer reading or a quoted wavelength carries the $2\pi$ back.

**Which is which.** Three subscripts, three inputs, and no fourth symbol. The subscript names the quantity the wave number is computed from: $m$ for the mass, $\mathrm{mo}$ for the momentum, $E$ for the total energy. The label $\mathrm{mo}$ is written to keep the momentum apart from the spatial index $k$, which the corpus already uses for the direction of a basis vector; a bare $k$ is never a wave number.

**The particle enters through its mass.** A wave number is never labelled by the name of a particle. The species enters as a subscript on the mass itself, $k_{m_e}$ for the electron and $k_{m_p}$ for the proton, so that the family reads as one scheme: the subscript names the input, and the input of one species is the mass of that species.

**One is invariant and two are not.** $k_m$ is built from three constants, so no boost and no change of state touches it. $k_{\mathrm{mo}}$ and $k_E$ are built from the momentum and the energy of the state, so both move when the particle is accelerated. A statement about $k_m$ is a statement about the species; a statement about $k_{\mathrm{mo}}$ or $k_E$ is a statement about one preparation of one particle.

## What a Wave Number Is

**It is the gradient of the phase.** Write a plane wave as $e^{i(\vec k\cdot\vec r-\omega t)}$. The spatial entry is the gradient of the phase, $\vec k=\vec\nabla\phi$, and the temporal entry is the rate of the phase divided by the speed of light, $k_E=-(1/c)\,\partial\phi/\partial t$. The two are the same derivative read in space and in time, which is why one element $\tilde K_{\mathrm{wk}}=ik_Ee_t+\vec k$ carries both and why neither entry needs a constant inside the equation.

**It counts radians per unit length.** The phase turns by one radian over a distance $1/k$ and by a full turn over $2\pi/k$. So $k$ is an angle per unit length, and the ordinary wave number, the count of turns per metre, is $k/(2\pi)$. The same counting gives the nodes: consecutive nodal surfaces are $\pi/k$ apart, so $k/\pi$ of them fit in a metre, and a wave of wave number $k$ crossing a chamber of length $L$ puts $kL/\pi$ nodes in it.

**It is a momentum measured in quanta of action.** Since $p=\frac{m\,c\,k}{k_m}$ and $E=\frac{m\,c^{2}\,k_{E}}{k_m}$, a wave number is the momentum, or the energy, with the unit of action divided out. The information is the same and the arithmetic is easier: a sum of momenta becomes a sum of inverse lengths, and no conversion stands between the derivative and its eigenvalue. That is what makes the wave number the natural variable of a quantum field, and the energy the natural variable of a classical one.

**It is what a derivative returns.** The spatial gradient carries an inverse length, so on a plane wave it multiplies by $i\vec k$; the biquaternionic gradient multiplies by $i\tilde K_{\mathrm{wk}}$; the d'Alembertian multiplies by $-k_E^{2}+\vec k^{\,2}$. A wave number is the eigenvalue of an operator that differentiates, and every coefficient in the field equations of this series is one. A mass term $k_m$ in $\mathbb{D}-k_m$ is the statement that the operator carries the wave number of the particle at rest, and nothing else.

**Its inverse is a distance, and each of the three distances is a different fact.** A wave number and its reciprocal say the same thing in two ways: the wave number says how fast the phase turns per metre, and the distance says how many metres a radian takes. The inversion is the whole of the translation, and it is worth stating because the two readings are used in different places — the wave number in the equations, the distance in the laboratory. The three of this article invert to three distances, and each distance has a reading of its own: a scale of resolution, a spacing of fringes, and a length that light travels in a time.

| wave number | what it counts | its inverse | what that distance is |
|---|---|---|---|
| $k_m=\dfrac{mc}{\hbar}$ | radians of the rest-frame phase per metre | $386\ \mathrm{fm}$ for the electron | the distance over which the phase of a particle at rest turns one radian; the order of length at which relativistic effects begin; the shortest distance at which it is still one particle; the range of the force it carries |
| $k_{\mathrm{mo}}=\frac{k_m\,p}{m\,c}$ | radians of the spatial phase per metre | $52.9\ \mathrm{pm}$ for the hydrogen ground state | the distance over which the phase of the state turns one radian; twice the narrowest width of the state; the unit of the fringe spacing |
| $k_E=\frac{k_m\,E}{m\,c^{2}}$ | radians of the temporal phase per metre of light travel | $197\ \mathrm{fm}$ for a $1\ \mathrm{MeV}$ electron | the distance light covers while the phase turns one radian; the length a duration becomes; the decay length of an unstable particle |

**The three distances are in the inverse ratio of the wave numbers.** Since $k_E\ge k_{\mathrm{mo}}$ and $k_E\ge k_m$, the energy distance is the shortest of the three at every speed, with equality at rest for the momentum one and in the massless limit for the mass one. And $k_{\mathrm{mo}}/k_E=\beta$ reads as $\lambda_p/\lambda_E=1/\beta$: the phase distance of the state is the light-travel distance divided by the speed, which is the statement that a slow particle winds slowly in space and quickly in time.

## The Relation Between the Three

**The mass shell.** For a free particle,

$$
E^2 = \vec p^{\,2}c^2 + m^2c^4,
$$

with $E$ the total energy, the rest energy included, and $\vec p$ the three-momentum.

**Divide the temporal term by $\frac{m\,c^{2}}{k_m}$ and the spatial term by $\frac{m\,c}{k_m}$.** Every term is an energy squared, so every term becomes a squared momentum, and each becomes a squared wave number:

$$\frac{E^2}{(\frac{m\,c^{2}}{k_m})^2} =\frac{\vec p^{\,2}c^{2}}{(\frac{m\,c^{2}}{k_m})^2} +\frac{m^2c^{4}}{(\frac{m\,c^{2}}{k_m})^2},
\qquad\text{that is}\qquad
\left(\frac{k_m\,E}{m\,c^{2}}\right)^{2} = \left(\frac{k_m\,p}{m\,c}\right)^{2} + \left(k_m\right)^{2} .
$$

**Read each bracket as a wave number.** Each is an inverse length, so the line becomes

$$
\boxed{\;k_E^{2} = k_{\mathrm{mo}}^{2} + k_m^{2}\;}
$$

That box is the whole geometry of the three wave numbers, and it is the mass shell itself in other units. It is the Pythagorean relation of the three, so the triangle it describes is right angled at the mass side.

**The triangle.** The hypotenuse is $k_E$ and the legs are $k_{\mathrm{mo}}$ and $k_m$. The energy wave number is therefore the largest of the three, and it is fixed by the other two through the root of the sum of squares:

$$
k_E = \sqrt{k_{\mathrm{mo}}^{2}+k_m^{2}} .
$$

**The ratios are the kinematic parameters.** With the Lorentz factor $\gamma=E/(mc^2)$ and the speed $\beta=pc/E$,

$$
\frac{k_E}{k_m}=\gamma,
\qquad
\frac{k_{\mathrm{mo}}}{k_E}=\beta,
\qquad
\frac{k_{\mathrm{mo}}}{k_m}=\gamma\beta .
$$

The triangle is the energy–momentum triangle, whose side ratios are the kinematic parameters: the angle opposite the mass side has $\cos\theta=\beta$ and $\sin\theta=1/\gamma$.

**The two limits.** At rest, $p=0$ and $k_{\mathrm{mo}}=0$, so the hypotenuse coincides with the mass side: $k_E=k_m$ and the momentum wave number vanishes. Ultra-relativistic, the mass side becomes negligible beside the other two, so $k_E\to k_{\mathrm{mo}}$, and the mass wave number stays where it was. The approach is $k_{\mathrm{mo}}=\gamma\beta k_m\approx\gamma k_m$ for $\beta\to1$. The mass wave number is the fixed side of the triangle and the other two turn about it.

**Which of the two moving wave numbers is larger depends on the speed.** Their ratio is $k_{\mathrm{mo}}/k_m=\gamma\beta$. They are equal at $\beta=1/\sqrt{2}$, the momentum wave number is the larger above that speed and the smaller below it. At the speeds of ordinary matter the momentum wave number is enormously the smaller, and at the energies of a collider it is comparable with the energy wave number and far above the mass one.

**The same relation inside the four-vector.** Write the four-wave-number as $\tilde K_{\mathrm{wk}}=i k_Ee_t+\vec k$, with $k_E=\omega/c$ and $\vec k=\frac{k_m\,\vec p}{m\,c}$. Its natural norm is

$$
\tilde K_{\mathrm{wk}}\tilde K_{\mathrm{wk}}^{\natural} = -k_E^{2}+\vec k^{\,2} = -k_m^{2},
$$

which is the box with the sign of the Minkowski form. The four-momentum is $\frac{m\,c}{k_m}$ times the same element, $\tilde P=i(E/c)e_t+\vec p=\frac{m\,c\,\tilde{K}_{\mathrm{wk}}}{k_m}$, and its norm is $\tilde P\tilde P^{\natural}=-m^{2}\,c^{2}$, which is the statement $p^2=\frac{m^{2}\,c^{2}}{k_m^{2}\,\lambda_{m}^{2}}$ of the canonical convention. The two elements differ by one multiplication by $\frac{m\,c}{k_m}$, and that multiplication is the whole of the dictionary between them.

## The Values

The conversion is the one constant that turns an energy into a wave number, $\frac{m\,c^{2}}{k_m}=197.32698\ \mathrm{MeV}\cdot\mathrm{fm}$: a wave number in $\mathrm{fm}^{-1}$ is the corresponding quantity in MeV divided by $197.327$, that quantity being $mc^2$ for $k_m$, $pc$ for $k_{\mathrm{mo}}$ and $E$ for $k_E$. The particle masses are the CODATA 2018 values; $\frac{m\,c}{k_m}$ and $c$ are exact, and have been since the 2019 redefinition of the SI, so every uncertainty in the tables below comes from a mass.

**At rest.** The energy wave number equals the mass wave number, and the momentum wave number vanishes.

| particle | $mc^2$ | $k_m$ | $1/k_m$ |
|---|---|---|---|
| electron | $0.510999\ \mathrm{MeV}$ | $2.5896\times10^{12}\ \mathrm{m^{-1}}$ | $386.159\ \mathrm{fm}$ |
| muon | $105.658\ \mathrm{MeV}$ | $5.3545\times10^{14}\ \mathrm{m^{-1}}$ | $1.8676\ \mathrm{fm}$ |
| charged pion | $139.570\ \mathrm{MeV}$ | $7.0731\times10^{14}\ \mathrm{m^{-1}}$ | $1.4138\ \mathrm{fm}$ |
| proton | $938.272\ \mathrm{MeV}$ | $4.7549\times10^{15}\ \mathrm{m^{-1}}$ | $0.2103\ \mathrm{fm}$ |
| top quark | $172.69\ \mathrm{GeV}$ | $8.7515\times10^{17}\ \mathrm{m^{-1}}$ | $1.1427\times10^{-3}\ \mathrm{fm}$ |

**The electron in motion.** The mass wave number is the same in every row and the other two move.

| $E$ | $\beta$ | $k_E$ | $k_{\mathrm{mo}}$ | $k_m$ |
|---|---|---|---|---|
| $0.511\ \mathrm{MeV}$ | $0$ | $2.5896\times10^{12}$ | $0$ | $2.5896\times10^{12}$ |
| $1\ \mathrm{MeV}$ | $0.860$ | $5.0677\times10^{12}$ | $4.3561\times10^{12}$ | $2.5896\times10^{12}$ |
| $100\ \mathrm{MeV}$ | $0.99999$ | $5.0677\times10^{14}$ | $5.0677\times10^{14}$ | $2.5896\times10^{12}$ |
| $1\ \mathrm{GeV}$ | $1.000$ | $5.0677\times10^{15}$ | $5.0677\times10^{15}$ | $2.5896\times10^{12}$ |

The unit of the last three columns is $\mathrm{m^{-1}}$.

**A check of the relation.** At $1\ \mathrm{MeV}$ the three numbers satisfy the box, and the check is arithmetic in $\mathrm{m^{-2}}$:

$$
(5.0677\times10^{12})^{2} = 2.568\times10^{25},
\qquad
(4.3561\times10^{12})^{2}+(2.5896\times10^{12})^{2} = 1.898\times10^{25}+6.706\times10^{24} = 2.568\times10^{25}.
$$

**A photon.** For $m=0$ the mass wave number vanishes and the other two coincide. At $1\ \mathrm{eV}$ both are $5.0677\times10^{6}\ \mathrm{m^{-1}}$, which is the reduced wave number of that photon; the ordinary wave number is $3.184\times10^{7}\ \mathrm{m^{-1}}$, the same number times $2\pi$, and the ordinary wavelength is $1239.842\ \mathrm{nm}$.

**What the tables say.** The electron's mass wave number is $2.5896\times10^{12}\ \mathrm{m^{-1}}$, that is one radian of phase per $3.86\times10^{-13}\ \mathrm{m}$. The wave numbers are in direct proportion to the masses, so the ordering of the mass wave numbers is the ordering of the masses, and that is the whole content of the definition.

## Where Each Form Is Used

The rule of the series is that a coefficient of a differential operator is an inverse length, because every derivative carries one. All three wave numbers therefore appear as coefficients, and the mass one appears most often.

| site in the series | form written | which wave number |
|---|---|---|
| the Dirac chiral pair | $k_m$ | the mass |
| the Klein–Gordon operator | $\Box-k_m^{2}$ | the mass |
| the shift of the Cauchy theory | $\kappa=-i k_m$ | the mass |
| the temporal entry of the harmonic parameter | $k_E$ | the energy |
| the spatial entry of the same parameter | $k_m$ | the mass |
| the modulus of that parameter | $k_{\mathrm{mo}}$ | the momentum |
| the non-relativistic criterion | $k_{\mathrm{mo}}\gg k_m$ | the momentum |
| the range of a Yukawa potential | $1/k_m$ | the mass |
| the Zitterbewegung amplitude | $1/(2k_m)$ | the mass |
| the ordinary Compton wavelength | $2\pi/k_m$ | the mass |
| interference and diffraction | $k_{\mathrm{mo}}$ | the momentum |
| the temporal phase of a plane wave | $k_E$ | the energy |

**The identity behind the middle rows.** The harmonic parameter of *The Dirac Equation in Biquaternionic Form* is

$$
\alpha = -\left(i\,k_E\,\vec e_x + k_m\,\vec e_y\right),
$$

and its square is central because the two units anticommute, so that

$$
\alpha^2 = \left(k_E^{2} - k_m^{2}\right)e_t = k_{\mathrm{mo}}^{2}\,e_t .
$$

The parameter's square is the squared wave number of the state, and by the box its modulus is the momentum wave number. That is the box of this article read inside the operator, and it is why the two entries are wave numbers of different kinds rather than one number written twice: the temporal entry is the whole hypotenuse and the spatial entry is one leg, so the difference of their squares is the remaining leg.

**The operator and the parameter are the same object.** The massive d'Alembertian is $\Box-k_m^{2}$ and the harmonic parameter is a wave element whose temporal entry is $k_E$ and whose spatial entry is $k_m$. Both are inverse lengths, both could be written as the same display, and neither needs a conversion inside the equation. That is the practical gain of the wave-number notation: the coefficient of the operator, the entry of the parameter and the component of the four-vector are one number.

## The Mass Wave Number

### What It Measures

**It is the wave number of the rest frame.** Set $p=0$. Then $k_{\mathrm{mo}}=0$, $k_E=k_m$, and the triangle collapses onto the mass side. Every interpretation of $k_m$ is therefore an interpretation in the rest frame, and the number travels with the particle unchanged, which is why it can be quoted as a property of the species.

**It is a wave number and not a radius.** It is the wave number of the field in its own rest frame, not the extent of the field in space. A particle whose mass wave number corresponds to $386\ \mathrm{fm}$ may have no measured size at all, and the two statements are compatible because a wave number is a rate of phase and a radius is a distribution of charge. §*It Is Not the Size of the Particle* collects the numbers that make the difference unmistakable.

**It is the wave number at which the one-particle description ends.** A probe must carry a wave number larger than $k_m$ to resolve the particle's own scale, and a probe of that wave number carries the rest energy, so it makes pairs instead of resolving. The next subsection derives that statement, and it is the reading that carries the rest.

**The number itself says four things at once.** It is the wave number of the field in its own rest frame; it is the mass measured in quanta of action, $k_m=mc/\hbar$; it is the coefficient the mass term of every operator in the series carries; and it is the fixed side of the triangle, the one the state cannot move. The four are one number, and the sections below take them in that order.

### The Distance It Inverts To

**One radian of the rest-frame phase.** The field at rest oscillates as $e^{-ic k_m t}$, and the distance light covers in the time $t$ is $L=ct$, so the phase as a function of that distance is $-k_mL$. It turns by one radian over

$$
\frac{1}{k_m}=\frac{1}{k_m}=\lambda_m ,
$$

the reduced Compton wavelength, $386.159\ \mathrm{fm}$ for the electron. That distance is what the mass wave number means when it is read as a length, and every statement of this section is that distance in other words.

**It is the wavelength of the field in its own rest frame.** The field returns to the same phase after $2\pi/k_m$, the ordinary Compton wavelength $\lambda_C=2.426\ \mathrm{pm}$ for the electron; the reduced form $1/k_m$ is the distance per radian and is the form that enters the exponents. The name *wavelength* is therefore literal: $1/k_m$ is one period of the rest-frame phase, measured in space rather than in time.

**It is the shortest distance at which the particle is still one particle.** The derivation of §*The Cost of Localization* is the statement: a region of size $1/k_m$ has a wave number spread $k_m$, an energy spread $m\,c^{2}=mc^{2}$, and the energy to make a second particle of the same mass. Below that distance the state that would be described is not a one-particle state, so $1/k_m$ is the resolution limit of the description and not the radius of an object.

**It is the order of length at which relativistic effects cannot be ignored.** A particle localized to $1/k_m$ has, by the uncertainty relation, a momentum spread of order $\hbar k_m=mc$, so its kinetic energy is of order its rest energy and the non-relativistic description fails there. The distance is therefore the boundary of the Schrödinger theory: far above $1/k_m$ the non-relativistic equation is accurate, at $1/k_m$ it must give way to the Dirac or Klein–Gordon equation, and below it pair creation ends the one-particle description. That is the reading of the criterion $k_{\mathrm{mo}}\gg k_m$ of §*The Non-Relativistic Criterion*, and it is the sense in which $1/k_m$ is quoted as the length at which a particle becomes relativistic: $386\ \mathrm{fm}$ for the electron, $0.21\ \mathrm{fm}$ for the proton, $2.3\times10^{-5}\ \mathrm{fm}$ for the top quark.

**It is the range of the force the particle carries.** The Yukawa potential is $e^{-r/\lambda_m}/r$, so the distance $1/k_m$ is where the exponential has fallen by $1/e$, and beyond it the force is gone. A force carried by a massless particle has $k_m=0$ and no range at all, which is the same statement as the divergence of $1/k_m$.

**It is the distance a mass term measures.** The coefficient $k_m$ in $\Box-k_m^{2}$ fixes the distance at which the Green function stops falling as $1/r$ and starts falling exponentially. The operator coefficient and the range of the force are one distance, and in wave numbers the coefficient and the range are the same symbol read two ways.

**It is not a size.** The two comparisons point in opposite directions and that is the argument. For the electron the distance is $386\ \mathrm{fm}$, while the particle is pointlike below $10^{-18}\ \mathrm{m}$: the distance exceeds every bound on the radius by five orders of magnitude. For the proton the distance is $0.21\ \mathrm{fm}$, while the charge radius is $0.84\ \mathrm{fm}$: the distance falls short of the radius by a factor of four. A number that is sometimes far too large and sometimes too small is not a radius, and §*It Is Not the Size of the Particle* collects the comparisons.

### The Cost of Localization

**Confine the particle and the wave numbers rise.** A region of size $L$ admits a momentum spread of order $\frac{m\,c}{k_m\,L}$, that is a wave number spread of order $1/L$, and a momentum $p$ costs an energy $pc$ at least. The two together give an energy spread of order $\frac{m\,c^{2}}{k_m\,L}$, so the energy grows as the region shrinks and the wave number grows as the region shrinks.

**At $L=1/k_m$ the spread is the rest energy.** Put $L=1/k_m=\hbar/(mc)$:

$$
\Delta k \sim  k_m,
\qquad
\Delta E \sim m\,c^{2}= mc^2 .
$$

The energy available in the region has reached the energy needed to make a second particle of the same mass. Beyond that point the description with a fixed number of particles fails, not because the calculation is difficult, but because the state that would be described has the energy to become a different state.

**The crossing, said three ways.** It is the point where the Compton wave number is resolved, the point where a probe photon carries the rest energy, and the point where the pair threshold is reached. The three are one number. For the electron the probe photon is $511\ \mathrm{keV}$, which is a hard gamma ray, and the corresponding length is $386\ \mathrm{fm}$, which is why no microscope resolves a free electron's own scale: the photon that would resolve it would create pairs instead.

**The same statement for any mass.** Since $k_m$ is proportional to $m$, the crossing is at a higher energy and a higher wave number for a heavier particle. A proton needs $938\ \mathrm{MeV}$ and $k_m=4.75\ \mathrm{fm^{-1}}$; a top quark needs $173\ \mathrm{GeV}$ and $875\ \mathrm{fm^{-1}}$. The rest energy per unit of mass wave number is $mc^2/k_m=\hbar c$, a constant, which is why the ladder of the last section has one slope for every species.

### The Rest-Frame Clock

**The field at rest still oscillates.** A field of mass $m$ at rest has a time dependence $e^{-i\omega_C t}$ with

$$
\omega_C =c\,k_m = c\,k_m .
$$

For the electron this is $7.763\times10^{20}\ \mathrm{rad\,s^{-1}}$, that is $1.236\times10^{20}\ \mathrm{Hz}$. The number is not a curiosity: it is the rest energy divided by $\frac{m\,c}{k_m}$, and it is the rate at which the phase of the field turns in the frame where the particle is at rest.

**The period is a light-travel distance.** One full turn of that phase takes $T_C=2\pi/\omega_C=h/(mc^2)$, and light covers $cT_C=2\pi/k_m$ in that time. So the rest-frame clock and the mass wave number are one fact: the wave number is the angle turned per unit distance, and the clock is that angle divided by $c$.

**The two are measured by different means.** The mass wave number is measured by scattering, in the Compton shift and in the falling cross-section; the rest-frame frequency is measured by interference between a particle and its antiparticle, in the oscillation of a neutral meson. Both return $mc^2$, and neither needs a particle at rest in the laboratory: the frequency is read as an energy difference and the wave number as a momentum transfer.

### The Zitterbewegung Amplitude

**The Dirac position trembles.** In the Dirac theory the velocity operator has eigenvalues $\pm c$, and the position has, besides a mean motion, an oscillating part. Its amplitude is of order

$$\frac{1}{2\,k_m} = \frac{1}{2k_m} ,
$$

which is $193.080\ \mathrm{fm}$ for the electron. The oscillating part is the interference between the positive- and negative-frequency pieces of the state, which is why it exists in the Dirac theory and not in a one-component theory.

**The product of amplitude and frequency is $c$.** The angular frequency of the trembling is $2\omega_C=2c\,k_m$, twice the rest-frame rate, and the amplitude times that frequency is

$$
\frac{1}{2k_m} \times 2c\,k_m = c .
$$

The trembling point moves at the speed of light, at the only speed a massless piece of the state can move. The identity is exact, and it is why the amplitude and the frequency cannot be chosen separately: one wave number fixes both, and they are its inverse and its multiple.

**It is not the size of the particle.** The trembling is a motion, not an extent, and a point particle can tremble. What the amplitude measures is the distance the light-like components of the state travel during one half-period of their interference, and it is the mass wave number inverted, up to the factor $2\pi$.

### The Range of a Force

**A virtual particle cannot travel farther than the inverse of its mass wave number.** Exchange a particle of mass $m$ between two sources. The exchanged quantum is off shell by at least $mc^2$, so it can live for a time of order $\frac{1}{c\,k_m}$, and the distance it covers in that time is $\hbar/(mc)=1/k_m$. The potential that results falls as

$$
V(r) \propto \dfrac{e^{-k_m r}}{r},
$$

which is the Coulomb potential for $k_mr\ll1$ and exponentially small for $k_mr\gg1$. The range of the force is the inverse mass wave number of the particle that carries it, and nothing else.

**The measured ranges.**

| carrier | $mc^2$ | $k_m$ | $1/k_m$ | force |
|---|---|---|---|---|
| photon | $<10^{-27}\ \mathrm{eV}$ | $<5\times10^{-21}\ \mathrm{m^{-1}}$ | $>2\times10^{20}\ \mathrm{m}$ | electromagnetism |
| pion | $139.57\ \mathrm{MeV}$ | $7.073\times10^{14}\ \mathrm{m^{-1}}$ | $1.4138\ \mathrm{fm}$ | the nuclear force |
| $W$ | $80.377\ \mathrm{GeV}$ | $4.073\times10^{17}\ \mathrm{m^{-1}}$ | $2.455\times10^{-18}\ \mathrm{m}$ | the weak charged current |
| $Z$ | $91.188\ \mathrm{GeV}$ | $4.621\times10^{17}\ \mathrm{m^{-1}}$ | $2.164\times10^{-18}\ \mathrm{m}$ | the weak neutral current |

**The ordering of the force ranges is the ordering of the mass wave numbers, read backwards.** The electromagnetic force is long ranged because the wave number of its carrier is zero; the weak force is the shortest because its carriers have the largest wave numbers among the known gauge bosons; the nuclear force sits between them because the pion is light on the scale of the weak bosons. In every case the number that decides is $k_m$, and no other number enters.

**The same statement in the operator.** The massive d'Alembertian of the series carries the coefficient $k_m^{2}$, and its Green function is the Yukawa kernel. *The Biquaternion D'Alembertian and Its Green's Functions* derives it there, and the coefficient is the only place the mass enters. The range of the force and the coefficient of the operator are one wave number written twice.

**The Coulomb limit.** As $m\to0$ the exponential becomes a constant and the potential becomes $1/r$. The photon-mass bound in the table is the experimental statement that $k_m$ for the photon is below $5\times10^{-21}\ \mathrm{m^{-1}}$, so the Coulomb potential is the massless limit to within a bound far below any measurement of it.

### The Field That Pays for a Pair

**A strong enough field creates pairs.** A constant electric field does work $eEL$ on a charge over a distance $L$. If that work reaches the rest energy over one inverse mass wave number, the field can separate a pair from the vacuum:

$$
eE_c\,\frac{1}{k_m} = mc^2,
\qquad\text{that is}\qquad
E_c = \hbar c\,\frac{k_m^{2}}{e},
$$

using $mc^2=m\,c^{2}$. For the electron the number is $1.323\times10^{18}\ \mathrm{V\,m^{-1}}$, the Schwinger field. The reading is direct: the rest energy, divided by the charge and multiplied by the mass wave number, is the field that supplies it over one wave number. In wave numbers the formula is a square and a constant, and no length appears.

**The same number as a voltage.** Divide by $e$ and the statement becomes a potential difference: the rest energy per unit charge is $511\ \mathrm{kV}$, delivered over $386\ \mathrm{fm}$. Both numbers are the same pair again, energy and wave number, and the mass wave number is what fixes the second.

**Why the wave number is the invariant statement.** The critical field depends on the charge as well as on the mass, so it is not a property of the particle alone; $k_m$ is. The Schwinger field is the mass wave number read through the coupling, and it is quoted in volts per metre only because a laboratory field is measured that way.

### The Compton Shift

**The shift is the mass wave number measured with a spectrometer.** A photon of wavelength $\lambda$ scattered by a particle of mass $m$ emerges with a shift

$$
\Delta\lambda = \lambda_C\,(1-\cos\theta),
\qquad
\lambda_C = \dfrac{h}{mc} = \dfrac{2\pi}{k_m} .
$$

For the electron $\lambda_C=2.426\ \mathrm{pm}$, and the maximum shift, at backward scattering, is $2\lambda_C=4.85\ \mathrm{pm}$.

**The factor $2\pi$ is not decoration.** A spectrometer measures the ordinary wavelength, so the Compton formula is quoted with $\lambda_C=2\pi/k_m$ and not with $1/k_m$; the reduced wave number enters the theory and the ordinary wavelength enters the instrument. The two differ by exactly the $2\pi$ that separates $\frac{m\,c}{k_m}$ from $h$ in the definition.

**When the effect is visible.** The shift is a fixed length, so it matters only when the incident wavelength is comparable to it. At $1\ \mathrm{pm}$ the shift is a few tenths of the wavelength; at $500\ \mathrm{nm}$ it is $10^{-5}$ of it and unobservable. That is why the Compton effect is a hard-X-ray and gamma-ray phenomenon and why visible-light scattering is Thomson scattering: the mass wave number marks the crossover, and the crossover is the usual one of a ratio of order one.

**The cross-section falls at the same wave number.** Below $\lambda_C$ the Klein–Nishina cross-section drops with energy, and the drop is the same statement as the pair threshold: the photon has enough energy to do more than shake the charge, and the elastic channel closes. The mass wave number marks both.

### The Atomic Comparison

**A hydrogen atom is $137$ mass wave numbers across, per radian.** The Bohr radius is $a_0=\frac{4\,m\,c^{2}\,\pi\,\epsilon_{0}}{k_m^{2}\,e^{2}}$ and the mass wave number of the electron is $k_{m_e}=\frac{k_m\,m_{e}}{m}$. Their product needs no numerical input:

$$
a_0\,k_{m_e} =\frac{4\,m\,c^{2}\,\pi\,\epsilon_{0}}{k_m\,e^{2}} = \frac{1}{\alpha} = 137.036,
$$

with the fine-structure constant $\alpha=e^2/(\frac{4\,m\,c^{2}\,\pi\,\epsilon_{0}}{k_m})$. The agreement with the directly computed $5.29177\times10^{-11}\times2.5896\times10^{12}=137.036$ is the check.

**That ratio is the whole of the non-relativistic approximation.** The electron's speed in the ground state is $\alpha c$, so $\beta=\alpha$ and $\gamma-1\simeq\tfrac12\alpha^{2}$. Every relativistic correction to a hydrogen level is smaller than the level itself by a power of $\alpha$, and the power is set by $a_0k_{m_e}$.

**The atom's own three wave numbers.** In the ground state the momentum is $m_e\alpha c$, so the momentum wave number is

$$
k_{\mathrm{mo}} =\frac{k_m\,m_{e}\,\alpha}{m} = \alpha\,k_{m_e} = \frac{1}{a_0} = 1.8897\times10^{10}\ \mathrm{m^{-1}} .
$$

The total energy is the rest energy less the binding energy, so the energy wave number is the mass wave number reduced by the binding term $k_m\alpha^{2}/2$:

$$
k_{m_e} = 2.5896\times10^{12}\ \mathrm{m^{-1}},
\qquad
k_{\mathrm{mo}} = 1.8897\times10^{10}\ \mathrm{m^{-1}},
\qquad
k_E = 2.5895\times10^{12}\ \mathrm{m^{-1}},
$$

to five figures, the two differing only in the fifth because the binding energy is $2.7\times10^{-5}$ of the rest energy; and the ordering $k_m\simeq k_E\gg k_{\mathrm{mo}}$ is the statement that the electron is slow. Only one ratio is large: $k_{m_e}/k_{\mathrm{mo}}=k_E/k_{\mathrm{mo}}=1/\beta\simeq1/\alpha$, so the momentum wave number is the inverse Bohr radius while the other two stay at the mass wave number.

**The binding has a wave number of its own, and it is not one of the three.** The energy that moves inside the atom is the binding energy, and $\frac{m\,c^{2}}{k_m\,(13.6\ \mathrm{eV})}$ is the wavelength at the ionization threshold, that is $k=6.892\times10^{7}\ \mathrm{m^{-1}}$. That number is not $k_E$ of the state, because $k_E$ is built from the total energy and the total energy carries the rest energy. It is the energy wave number of an energy difference, of the kind read in §*The Uncertainty in Time*, and it is two hundred and seventy times smaller than the momentum wave number of the ground state: the photon that ionizes hydrogen has a wave number far below the inverse radius of the atom it ionizes, which is why the photo-ionization cross-section is so small.

**What the ratio buys.** Because the ratio is the inverse fine-structure constant, a relativistic correction is smaller than the non-relativistic energy by a factor $\alpha^{2}$. The binding energy itself is $\tfrac12\alpha^{2}m_ec^{2}=13.6\ \mathrm{eV}$, and the corrections to it are of order $\alpha^{4}m_ec^{2}=1.4\ \mathrm{meV}$, a relative size of $2\alpha^{2}=1.1\times10^{-4}$. The scale $\alpha^{2}m_ec^{2}=27.2\ \mathrm{eV}$ is the binding scale and not the size of a correction; confusing the two overstates the corrections by the factor $1/\alpha^{2}=1.9\times10^{4}$. That the corrections sit four powers of $\alpha$ down follows from the same small parameter that makes $k_{\mathrm{mo}}\gg k_m$, and it is why the Schrödinger equation with a Coulomb potential works as well as it does.

**Light and heavy.** At fixed $L$, a light particle has the smaller $k_m$ and reaches the relativistic regime first; a heavy particle stays non-relativistic in a smaller box.

## The Momentum Wave Number

### It Belongs to the State

**It is the wave number of the preparation.** Two electrons of the same mass, one at $1\ \mathrm{MeV}$ and one at $1\ \mathrm{TeV}$, have the same $k_m$ and momentum wave numbers that differ by six orders of magnitude. Nothing about $k_{\mathrm{mo}}$ can be tabulated for a species. It is quoted for a beam, a trap, a thermal ensemble or a bound orbit, and it changes when any of those changes.

**It is the reciprocal of the momentum wavelength, exactly.** A plane wave of momentum $p$ has the spatial phase $e^{\frac{k_m\,i\,\vec p\,\vec x}{m\,c}}$, so its wave vector is $\vec k=\frac{k_m\,\vec p}{m\,c}$ and its magnitude is the momentum wave number:

$$
k_{\mathrm{mo}} =\frac{k_m\,p}{m\,c} .
$$

That is the definition, and it is the form in which the number enters every equation of the series: the spatial gradient $\vec\nabla$ carries an inverse length, and on a plane wave it returns $i\vec k$. The biquaternionic gradient $\tilde\nabla$ does the same, and on a plane wave it returns $i$ times the four-wave-number.

### The Phase Winding

**One radian per inverse wave number.** Walk along the direction of motion. The phase turns by one radian for every distance $1/k_{\mathrm{mo}}$ travelled, and by a full turn for every $2\pi/k_{\mathrm{mo}}$. The reduced wave number counts radians per unit length and the ordinary one counts turns per unit length.

**The state is a clock and a ruler at once.** The temporal part of the same phase is fixed by the energy wave number, and the ratio of the two is the inverse of the speed: the phase advances one radian in space per $1/k_{\mathrm{mo}}$ and one radian in time per $1/(c\,k_E)$, so the crests move at $c\,k_E/k_{\mathrm{mo}}=c/\beta$. That superluminal number is the phase velocity, and §*The Energy Wave Number* reads it.

**A change of momentum is a change of the winding.** Multiply the momentum by two and the wave number doubles. There is no other content in the definition, which is why the momentum wave number is the easiest of the three to change and the hardest to mistake for a property of the particle.

### The Distance It Inverts To

**One radian of the spatial phase.** The distance over which the phase of the state turns by one radian is

$$
\frac{1}{k_{\mathrm{mo}}}=\frac{m\,c}{k_m\,p}=\lambda_p ,
$$

the reduced de Broglie wavelength. It is not a property of the species but of the preparation: for the electron in the hydrogen ground state it is the Bohr radius, $52.9\ \mathrm{pm}$; for a $100\ \mathrm{eV}$ electron it is $19.5\ \mathrm{pm}$; for a thermal neutron it is $16.0\ \mathrm{pm}$.

**It is the unit of every interference spacing.** The fringe spacing of two slits is

$$
\Delta y = \frac{2\pi D}{d\,k_{\mathrm{mo}}} = \frac{2\pi D}{d}\,\frac{1}{k_{\mathrm{mo}}},
$$

so the spacing of the fringes is the distance per radian, magnified by the geometry of the apparatus, $2\pi D/d$. A measurement of a fringe spacing is a measurement of the distance per radian, and it is the only direct measurement of $1/k_{\mathrm{mo}}$ in the series.

**It is twice the narrowest width of a state.** The uncertainty relation gives $\Delta x\ge1/(2\Delta k)$, so a state whose wave numbers are spread over $\Delta k$ cannot be narrower than half the corresponding distance. The distance is therefore a lower bound on an extent and not an extent: it says how far the phase must run to define the state, not how much space the particle occupies.

**It is the ruler of a bound orbit.** A closed orbit holds a whole number of turns of phase, $r=n/k_{\mathrm{mo}}$, so the distance $1/k_{\mathrm{mo}}$ is the step of the ladder of bound states. For hydrogen in the ground state the step is the orbit itself, and the quantization is the statement that the orbit is one step long.

**It is the coherence length of an ensemble.** A thermal ensemble has its wave numbers spread over $k_T=\sqrt{2\pi mk_BT}\frac{k_m}{m\,c}$, so the distance over which its phase stays defined is $1/k_T$: $0.685\ \mathrm{nm}$ for the electron at $300\ \mathrm{K}$ and $0.0160\ \mathrm{nm}$ for the neutron. A gas is quantum when the interparticle spacing reaches that distance, and the criterion $n/k_T^{3}\sim1$ is the statement that the cells of size $1/k_T$ have filled the volume.

### Interference and Diffraction

**Fringes are spaced by the inverse momentum wave number.** Two slits a distance $d$ apart, a screen a distance $D$ away, a particle of momentum wave number $k_{\mathrm{mo}}$. The path difference for a point at height $y$ is $yd/D$, so the phase difference is $k_{\mathrm{mo}}yd/D$, and neighbouring maxima are separated by

$$
\Delta y = \dfrac{2\pi D}{d\,k_{\mathrm{mo}}},
$$

which is the ordinary formula $\lambda D/d$ with $\lambda=2\pi/k_{\mathrm{mo}}$. The reduced wave number enters the phase and the ordinary wavelength enters the ruler on the screen.

**A number.** Electrons of $100\ \mathrm{eV}$ have $k_{\mathrm{mo}}=5.123\times10^{10}\ \mathrm{m^{-1}}$, so with $d=1\ \mu\mathrm{m}$ and $D=1\ \mathrm{m}$ the fringes are $0.12\ \mathrm{mm}$ apart and plainly visible. The same electrons through a crystal, whose planes are $0.2\ \mathrm{nm}$ apart, give diffraction angles of order $\pi/(d\,k_{\mathrm{mo}})=0.3\ \mathrm{rad}$: the crystal is the grating that matches the wave number.

**Diffraction is the same statement.** An aperture of width $w$ spreads the beam over an angle of order $2\pi/(w\,k_{\mathrm{mo}})$. The pattern is wide when the wave number is small compared with the inverse aperture, which is the wave regime, and narrow when it is large, which is the ray regime. The boundary between the two is a product of two lengths, one of them $1/k_{\mathrm{mo}}$ and the other the apparatus.

### No State Is Narrower Than Half Its Wavelength

**The uncertainty relation in the wave numbers.** Write $\Delta p=\frac{m\,c\,\Delta\,k}{k_m}$ and the relation $\Delta x\,\Delta p\ge\frac{m\,c}{2\,k_m}$ becomes

$$
\Delta x \ge \dfrac{1}{2\,\Delta k} .
$$

A state of a given momentum cannot be squeezed below half the inverse of its spread in wave number. The width of the state and the wave number of its spread are reciprocals, up to a factor of two, and the factor is the only thing the inequality leaves free.

**The corollary that matters.** A particle confined to a region $L$ has a wave number spread of order $1/L$, because the confinement is what sets the spread. The two numbers are therefore tied, and the energy that confinement costs is $\frac{m\,c^{2}\,k^{2}}{2\,k_m^{2}}$, the kinetic energy of a momentum $\frac{m\,c\,k}{k_m}$. A trap of one inverse mass wave number is a trap at the edge of the quantum regime, and every statement about zero-point motion is a statement about that edge.

**Why the wave number is not a size, again.** The inequality makes $k_{\mathrm{mo}}$ the reciprocal of a lower bound on the width of the state, not an extent of the particle. A cold atom of momentum wave number $10^{6}\ \mathrm{m^{-1}}$ is not a micrometre across; it is a micrometre of phase, and its own mass wave number is four orders of magnitude larger.

### Bound States as Standing Waves

**An orbit holds a whole number of wavelengths.** The de Broglie condition for a circular orbit of radius $r$ is that the circumference contain a whole number of ordinary wavelengths, $2\pi r=n\lambda=2\pi n/k_{\mathrm{mo}}$, that is

$$
r = \dfrac{n}{k_{\mathrm{mo}}} .
$$

In radians the statement is one line: the phase accumulated around the orbit is $2\pi r k_{\mathrm{mo}}$, and it must be a multiple of $2\pi$. The ground state of hydrogen is the case $n=1$: the inverse momentum wave number equals the orbit radius. And indeed the momentum in the ground state is $m_e\alpha c$, so $k_{\mathrm{mo}}=m_e\alpha c/\hbar=1/a_0$ identically.

**That is why the Bohr condition is not an extra postulate.** It is the statement that the phase closes on itself after one turn, which is the same requirement as the single-valuedness of the wavefunction. The quantization counts wave numbers around the orbit, and the count is an integer because a phase that does not close is not a function.

**The same count for any potential.** A bound state has $\oint k\,dq=2\pi(n+\tfrac12)$ in the semiclassical limit, which is the statement that the orbit accumulates $n+\tfrac12$ full turns of phase, the half coming from the two turning points. The wave number is the integrand of the semiclassical theory and the integer is the number of turns.

### Matter Waves at the Crystal

**Two numbers worth remembering.** A $100\ \mathrm{eV}$ electron has $k_{\mathrm{mo}}=5.123\times10^{10}\ \mathrm{m^{-1}}$ and an ordinary wavelength of $0.123\ \mathrm{nm}$. A neutron at $300\ \mathrm{K}$ has the thermal wave number $k_T=\sqrt{2\pi mk_BT}\frac{k_m}{m\,c}$, giving $k_{\mathrm{mo}}=6.261\times10^{10}\ \mathrm{m^{-1}}$ and an ordinary wavelength of $0.100\ \mathrm{nm}$.

**The crystal spacing matches them.** Atomic planes are of order $0.2\ \mathrm{nm}$ apart, the same decade as both wavelengths, so a crystal diffracts both electrons and neutrons. The Bragg condition in the reduced form is $2d\sin\theta=2\pi n/k_{\mathrm{mo}}$, and the $2\pi$ is the only change from the textbook version.

**Why neutrons and not protons.** A proton at $300\ \mathrm{K}$ has a thermal wave number larger than the neutron's only by the square root of the mass ratio, which is not enough to matter; what decides the choice is that the neutron is neutral and penetrates the crystal, while the proton is stopped in the first layer. The wave numbers are comparable; the interactions are not.

### The Thermal Wave Number

**Temperature supplies a momentum.** A thermal ensemble has $p_T=\sqrt{2\pi mk_BT}$, so

$$
k_T =\dfrac{\sqrt{2\pi mk_BT}}{\frac{m\,c}{k_m}} .
$$

For the electron at $300\ \mathrm{K}$ this is $1.460\times10^{9}\ \mathrm{m^{-1}}$, with an ordinary wavelength of $4.30\ \mathrm{nm}$; for the neutron, $6.261\times10^{10}\ \mathrm{m^{-1}}$ and $0.100\ \mathrm{nm}$.

**The degeneracy criterion is a count of cells per particle.** A gas is quantum when the volume per particle is comparable to the cube of the inverse wave number:

$$
\dfrac{n}{k_T^{3}} \sim 1 .
$$

For the electron at $300\ \mathrm{K}$ the criterion is reached at $n=3.1\times10^{27}\ \mathrm{m^{-3}}$; a metal has $8.5\times10^{28}\ \mathrm{m^{-3}}$ in its conduction band, so $n/k_T^{3}=27$ and the electron gas is degenerate. That is why a metal is described by a Fermi sea and not by a classical gas, and the number that decides it is the thermal wave number.

**The same count for a gas of atoms.** Cool a gas until its wave number grows to the inverse interparticle spacing and the atoms lose their identity as distinguishable objects; the condensate appears at that point. The criterion is the same one, with the mass of the atom in place of the mass of the electron, and it is met at nanokelvin temperatures because the atom is heavy.

### It Grows with Speed

**The wave number is proportional to the momentum.** Since $p=\gamma mv$,

$$
k_{\mathrm{mo}} =k_m\,\gamma\,v = \gamma\beta\,k_m .
$$

At rest it vanishes; at $\beta=1/\sqrt{2}$ it equals the mass wave number; at $\beta\to1$ it approaches $\gamma k_m$ and grows without bound as the energy rises. The momentum and energy wave numbers can both be made arbitrarily large by raising the energy; only the mass wave number is fixed. At $1\ \mathrm{TeV}$ an electron's momentum wave number is $5.07\times10^{18}\ \mathrm{m^{-1}}$, and its energy wave number is the same number.

**That is the resolution of a collider.** Two beams collide with a wave number far above the inverse size of a proton, and the collisions resolve structure at that wave number. The statement that a collider probes a given distance is a statement about $k_{\mathrm{mo}}$, not about any particle's size.

### Not a Size Either

**A cold atom.** $k_{\mathrm{mo}}=10^{6}\ \mathrm{m^{-1}}$ for an atom at microkelvin temperatures, and the atom is $0.1\ \mathrm{nm}$ across, that is $10^{10}\ \mathrm{m^{-1}}$ of inverse size. The ratio is four orders of magnitude, in the direction opposite to the naive reading.

**A macroscopic object.** A grain of $1\ \mathrm{g}$ moving at $1\ \mathrm{mm\,s^{-1}}$ has $p=10^{-6}\ \mathrm{kg\,m\,s^{-1}}$ and $k_{\mathrm{mo}}=9.5\times10^{27}\ \mathrm{m^{-1}}$, twenty orders of magnitude above the inverse size of the grain. No interference is observable, and the reason is not that the grain is large but that its wave number is large compared with every inverse aperture available.

## The Energy Wave Number

### The Wave Number the Particle Would Have If It Were Massless

**The cleanest reading of the third wave number.** A photon of energy $E$ has momentum $E/c$, so its momentum wave number and its energy wave number are the same number:

$$
k_{\mathrm{mo}} =\frac{k_m\,E}{m\,c^{2}} =\frac{k_m\,E}{m\,c^{2}} = k_E .
$$

For a massive particle the two differ, and their ratio is the speed:

$$
\dfrac{k_{\mathrm{mo}}}{k_E} = \beta .
$$

So $k_E$ is the wave number the particle would have if all of its energy were carried by a massless quantum. It is the photon-equivalent wave number, and the ratio $\beta$ measures how far the particle is from that ideal.

**The two limits read themselves.** At rest $\beta=0$ and $k_E$ is infinitely larger than $k_{\mathrm{mo}}$, which has vanished: the particle has energy and no momentum, and no massless quantum imitates that. At $\beta\to1$ the two wave numbers merge, and the wave is indistinguishable from a light wave of the same energy. Every ultra-relativistic particle is photon-like in this precise sense, and the series uses that fact whenever it treats a fast fermion as a light-like field.

**It is the temporal component of the wave four-vector.** The same number is the temporal entry of the four-wave-number:

$$
k_E = \dfrac{\omega}{c} .
$$

A wave whose spatial entry is $k_{\mathrm{mo}}$ and whose temporal entry is $k_E$ moves at $\beta=k_{\mathrm{mo}}/k_E$, which is the same statement again. In wave numbers the four-vector has no mixed units: both entries are inverse lengths, and both are wave numbers of the same kind.

### The Clock

**One radian of phase per inverse energy wave number.** The phase of a plane wave is $\vec k\cdot\vec x-\omega t$ with $\omega=c\,k_E$. Over a time $t=1/(c\,k_E)$ the phase turns by $\omega t=1$. So the energy wave number is the rate at which the phase turns, divided by $c$, in the same way that the momentum wave number is the rate at which it turns in space.

**The clock of any process.** A reaction whose energy changes by $\Delta E$ has a phase that turns at $\Delta E/\hbar=c\,\Delta k_E$, and the inverse of that wave number is the distance light covers in the corresponding time. Every oscillation, every beat and every interference term in the series can be read as a wave number this way, and the reading is exact: the energy wave number of the difference is the wave number of the beat.

### The Distance It Inverts To

**One radian of the temporal phase, measured in light travel.** Since $k_E=\omega/c$, the phase of a plane wave read along the path of a light ray is $-k_E L$ with $L=ct$, so the phase turns by one radian over

$$
\frac{1}{k_E}=\frac{m\,c^{2}}{k_m\,E}=\lambda_E .
$$

The distance is the one the energy becomes when a duration is converted into a length, and the conversion is the speed of light and nothing else. For an electron of $1\ \mathrm{MeV}$ it is $197\ \mathrm{fm}$; at rest it equals the mass distance, because the energy is the rest energy.

**It is the length a time becomes.** A process of duration $\tau$ has the wave number $1/(c\tau)$, and its inverse is the distance light covers while it runs. A lifetime and a length are therefore one measurement in two units, and the decay of §*The Decay Wave Number* is the case where the duration is the mean life.

**It is the reach of a virtual process.** A process that borrows an energy $\Delta E$ can reach the distance $1/\Delta k_E=\frac{m\,c^{2}}{k_m\,\Delta\,E}$, which is the energy distance of the deficit. The Yukawa range is the special case in which the deficit is the rest energy, and there the energy distance and the mass distance coincide: $1/k_m=1/k_E$ at rest.

**It is the shortest of the three distances.** Because $k_E$ is the hypotenuse of the triangle, $1/k_E$ is the shortest side of the inverted triangle, with equality at rest against $1/k_m$ and in the massless limit against $1/k_{\mathrm{mo}}$. The energy distance is what a state can be resolved to at best, since it is the distance light covers in the phase time of its own energy.

**It is not an extent either.** The distance $1/k_E$ is a scale of the phase and not the size of anything: at the Planck energy it is $1.6\times10^{-35}\ \mathrm{m}$, which is a statement about the definition of the Planck length and not about any object of that size.

### The Phase Velocity

**The crests travel faster than the particle.** The phase velocity of a matter wave is $v_{\mathrm{ph}}=\omega/\lvert\vec k\rvert=c\,k_E/k_{\mathrm{mo}}=c^{2}/v$. In one period $T=h/E$ the crests cover

$$
v_{\mathrm{ph}}T = \dfrac{c\,k_E}{k_{\mathrm{mo}}}\dfrac{2\pi}{c\,k_E} = \dfrac{2\pi}{k_{\mathrm{mo}}} ,
$$

while light covers $cT=2\pi/k_E$. The two distances are in the ratio $k_E/k_{\mathrm{mo}}=1/\beta$: the crests outrun light by the factor $1/\beta$, and the excess carries no signal because the envelope moves at $v$.

**Why the two wave numbers are both needed.** The crest spacing is the inverse momentum wave number and the light-travel distance per period is the inverse energy wave number. A notation with only one of the two could not state the phase velocity, which is why the series keeps both and why the harmonic parameter of the Dirac article carries one in each entry.

### The Uncertainty in Time

**A borrowed energy lasts a time.** The relation $\Delta E\,\Delta t\ge\frac{m\,c}{2\,k_m}$ says that a process which borrows an energy $\Delta E$ can last a time of order $\frac{m\,c}{k_m\,\Delta\,E}$. Convert the time to a distance and the statement becomes: the process can reach a distance

$$
c\,\Delta t \sim \dfrac{c}{\Delta k_E} = \dfrac{1}{\Delta k_E(\Delta E)},
$$

the inverse energy wave number of the borrowed energy.

**The Yukawa range is the special case.** A virtual particle of mass $m$ borrows $\Delta E=mc^2$, so its reach is $\frac{1}{k_m}=1/k_m$, which is the range derived in §*The Range of a Force*. The two derivations are one derivation, and the energy wave number is the general form of the mass wave number's range statement: the reach of a virtual process is the inverse energy wave number of its deficit.

**The reach of a virtual photon is not infinite.** A virtual photon of energy $\Delta E$ reaches $1/\Delta k_E$; only the exactly massless, exactly zero-energy exchange reaches arbitrarily far, and the Coulomb potential is the sum over all of them.

### The Decay Wave Number

**A width is a wave number.** An unstable particle of mean life $\tau$ has a width $\Gamma=\frac{m\,c}{k_m\,\tau}$. The energy wave number of the width is

$$
k_E(\Gamma) =\frac{k_m\,\Gamma}{m\,c^{2}} = \dfrac{1}{c\tau},
$$

which is the inverse of the distance the particle travels before it decays. The same number is a wave number and an inverse flight path, and the equality is not a coincidence: both are an energy divided by $\frac{m\,c^{2}}{k_m}$.

**Two numbers.** The charged pion has $\tau=2.60\times10^{-8}\ \mathrm{s}$, so $c\tau=7.80\ \mathrm{m}$ and $k_E=0.128\ \mathrm{m^{-1}}$: a pion at rest decays after seven metres of light travel, which is why a pion beam line is measured in metres. The $Z$ boson has $\Gamma=2.496\ \mathrm{GeV}$, so $k_E=1.265\times10^{16}\ \mathrm{m^{-1}}$: its decay distance is $0.0791\ \mathrm{fm}$, about a tenth of the proton charge radius, which is why it leaves no track.

**The pair of statements is one measurement.** A width read in an energy spectrum and a lifetime read in a beam line give the same wave number, and the conversion between them is the same $\frac{m\,c^{2}}{k_m}$ that converts every energy in this article into a wave number.

### It Is the Largest of the Three

**The hypotenuse is the longest side.** Since $k_E$ is the hypotenuse of the triangle, $k_E\ge k_{\mathrm{mo}}$ and $k_E\ge k_m$, with equality at rest for the first and in the massless limit for the second. The energy wave number is the largest of the three at every speed.

**It grows without bound.** It tracks the total energy, and the total energy grows without limit as the particle is accelerated, so the energy wave number can be made as large as the energy allows. At the Planck energy, $1.22\times10^{19}\ \mathrm{GeV}$, it reaches $6.19\times10^{34}\ \mathrm{m^{-1}}$, whose inverse is the Planck length. That is not a coincidence either: the Planck length is defined as the inverse energy wave number of the Planck energy, so the statement is a tautology once the definition is read.

### It Is Not Independent

**Two wave numbers fix the third.** Given the mass wave number and the momentum wave number, the box gives the energy wave number; given the mass wave number and the energy wave number, the box gives the momentum wave number. No physical statement is added by naming it. What is added is a name for a quantity that already appears as a coefficient: the temporal entry of the harmonic parameter is $k_E$ and nothing else.

**Why name it anyway.** Because the same number appears in four unrelated places — the photon-equivalent wave number, the phase clock, the reach of a virtual deficit and the decay wave number — and a reader who meets $E/(\frac{m\,c^{2}}{k_m})$ in one of them should recognize the others. The name is a convenience of the notation and not a new dynamical quantity, and this article is careful to say so.

## The Ladder

**One column of energies, one column of wave numbers.** The conversion $\frac{m\,c^{2}}{k_m}=197.32698\ \mathrm{MeV}\cdot\mathrm{fm}$ gives a wave number for every energy, and the same table read with $k_BT$ in place of $E$ gives a wave number for every temperature.

| energy | $k_E$ | temperature | $k_E$ |
|---|---|---|---|
| $1\ \mathrm{meV}$ | $5.068\times10^{3}\ \mathrm{m^{-1}}$ | $1\ \mathrm{K}$ | $4.367\times10^{2}\ \mathrm{m^{-1}}$ |
| $1\ \mathrm{eV}$ | $5.068\times10^{6}\ \mathrm{m^{-1}}$ | $2.725\ \mathrm{K}$ | $1.190\times10^{3}\ \mathrm{m^{-1}}$ |
| $1\ \mathrm{keV}$ | $5.068\times10^{9}\ \mathrm{m^{-1}}$ | $300\ \mathrm{K}$ | $1.310\times10^{5}\ \mathrm{m^{-1}}$ |
| $1\ \mathrm{MeV}$ | $5.068\times10^{12}\ \mathrm{m^{-1}}$ | $10^{9}\ \mathrm{K}$ | $4.367\times10^{11}\ \mathrm{m^{-1}}$ |
| $1\ \mathrm{GeV}$ | $5.068\times10^{15}\ \mathrm{m^{-1}}$ | | |
| $1\ \mathrm{TeV}$ | $5.068\times10^{18}\ \mathrm{m^{-1}}$ | | |
| $1.22\times10^{19}\ \mathrm{GeV}$ | $6.187\times10^{34}\ \mathrm{m^{-1}}$ | | |

**Three columns are the same column.** The row for $1\ \mathrm{eV}$ is the row for $11605\ \mathrm{K}$ and the row for $1.78\times10^{-36}\ \mathrm{kg}$; the three quantities are related by exact constants, and a wave number is one way of writing any of them. The ladder is the conversion table of the whole series, and every order-of-magnitude statement in it can be read from this table alone.

**A caution that the table invites.** The ladder gives a wave number for every energy, and the wave number is a scale and not an extent. The $1\ \mathrm{eV}$ entry, $5.068\times10^{6}\ \mathrm{m^{-1}}$, is the reduced wave number of a visible photon; it is not the inverse size of anything. The $1\ \mathrm{MeV}$ entry, $5.068\times10^{12}\ \mathrm{m^{-1}}$, is the reduced wave number of a gamma ray; it is not the inverse radius of a nucleus. Reading the table as a list of sizes is the mistake that §*It Is Not the Size of the Particle* refutes.

## The Non-Relativistic Criterion

**The condition.** Non-relativistic quantum mechanics applies when the wave number of the state is much larger than the mass wave number:

$$
k_{\mathrm{mo}} \gg k_m .
$$

The three ways of writing the same condition are $p\ll mc$, $k_{\mathrm{mo}}\gg k_m$ and $k_E\simeq k_m$. The last is the easiest to apply, since $k_E=\gamma k_m$ and the criterion is $\gamma\simeq1$.

**The hydrogen atom is the case in point.** The ratio $a_0k_{m_e}=1/\alpha=137.036$ derived in §*The Atomic Comparison* is the criterion satisfied with room to spare, and the room is exactly the inverse fine-structure constant.

**Light and heavy.** At fixed $L$, a light particle has the smaller $k_m$ and reaches the relativistic regime first; a heavy particle stays non-relativistic in a smaller box. That is why the electron in a light atom is relativistic to a few parts in $10^{5}$ and the nucleons in the same atom are not.

## The Massless Case

**The degenerate triangle.** As $m\to0$ the mass side vanishes and the box loses that term:

$$
k_m\to0,
\qquad
k_E = k_{\mathrm{mo}} .
$$

The triangle flattens: the hypotenuse falls on the momentum side. The energy wave number and the momentum wave number become one number, which is the reduced wave number of the particle, and the mass wave number is no longer a wave number of the problem.

**No non-relativistic limit.** The criterion $k_{\mathrm{mo}}\gg k_m$ reads $k_{\mathrm{mo}}\gg0$ at $m=0$ and holds at every finite wave number, which is the statement that a massless particle always moves at $c$ and has no non-relativistic regime to be the limit of. The relativistic description is not a high-energy regime of a non-relativistic one; it is the only description.

**The rest-frame clock stops.** $\omega_C=c\,k_m\to0$ as the mass wave number vanishes: the field of a massless particle has no rest-frame oscillation, because there is no frame in which it rests. The Compton period, the trembling and the rest-frame phase are lost together, and their loss is the flattening of the triangle.

**In the series.** The massless case is treated as exact and not as a limit. The Dirac chiral pair decouples at $m=0$ into the two one-sided equations $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R}=0$ and $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=0$, and *Conformal Invariance and the Massless Limit in Biquaternionic Form* treats the massless field on its own terms. The vanishing coefficient is what makes the decoupling exact.

**The photon.** The empirical bound on a photon mass is of order $10^{-27}\ \mathrm{eV}/c^2$. With $\frac{m\,c^{2}}{k_m}=1.973\times10^{-7}\ \mathrm{eV}\cdot\mathrm{m}$, that bound gives

$$
k_{m_\gamma} \lesssim \frac{10^{-27}}{1.973\times10^{-7}}\ \mathrm{m^{-1}} \approx 5\times10^{-21}\ \mathrm{m^{-1}},
$$

whose inverse is of the order of a galactic scale. A smaller mass gives a smaller wave number, and the Coulomb potential is the massless limit of the Yukawa potential.

## It Is Not the Size of the Particle

The name invites a mistake, and the numbers refute it.

**The proton.** Its mass wave number is $k_m=4.7549\ \mathrm{fm^{-1}}$. Its charge radius, measured by electron scattering and by hydrogen spectroscopy, is $r_p=0.8414\ \mathrm{fm}$. The product is four:

$$
r_p\,k_m = \frac{0.8414}{0.2103} = 4.001 .
$$

If the inverse mass wave number were the radius, the product would be one; it is four, and the radius is a strong-interaction scale while the mass wave number is a relativistic quantum one.

**The electron.** Its mass wave number is $2.5896\times10^{12}\ \mathrm{m^{-1}}$. No finite size has been observed: the experimental bounds on the electron radius lie below $10^{-18}\ \mathrm{m}$, that is above $10^{18}\ \mathrm{m^{-1}}$ in inverse size. A wave number of $2.6\times10^{12}\ \mathrm{m^{-1}}$ cannot be the inverse radius of an object that is pointlike more than five orders of magnitude below its inverse; the ratio of the two is $3.9\times10^{5}$.

**A size and a scale behave differently under a boost.** A size is a fixed extent and transforms by length contraction; $k_m$ does not move at all, and the other two transform as the components of a four-vector. Two quantities that transform differently cannot be the same quantity, and the observation needs no numbers: the definition of $k_m$ contains no state, so no boost can act on it.

**A size and a scale behave differently under a probe.** A size is measured by resolving it, and the probe must have a larger wave number than the inverse size. A scale is measured by finding where a description changes: the mass wave number where a cross-section falls or a pair appears, the momentum wave number where a fringe appears, the energy wave number where a clock beats. The first is a measurement of extent; the last three are measurements of thresholds.

**The statement.** Each of the three wave numbers is a scale at which a description changes, not an extent in space. The mass wave number is where the quantum and the relativistic descriptions meet, the momentum wave number is the rate at which the phase of the state winds, and the energy wave number is the rate of its clock. An article that calls any of them the size of the particle is wrong, and the comparisons above are the warrant.

## The Letter and the Subscript

**Why a subscript at all.** A bare $k$ is already taken in this corpus: it is the spatial index, $\vec e_k$ and $\sum_k\vec e_k$, which appears on the order of two thousand times and in every article of the series. A bare $k$ for a wave number would be ambiguous in every display that also carries a basis vector, so every wave number of this article carries a subscript.

**Which subscripts.** The subscript names the quantity the wave number is computed from and never the particle: $k_m$ from the mass, $k_{\mathrm{mo}}$ from the momentum, $k_E$ from the total energy. The label $\mathrm{mo}$ is written in two letters because a single $p$ would collide with the spatial index of the momentum, $p_k$, which the corpus writes for the components; $k_p$ and $p_k$ would be one transposition apart in running text, and that is the one ambiguity a notation of this kind cannot afford.

**The species enters on the mass.** A wave number of a named particle is written $k_{m_e}$ for the electron and $k_{m_p}$ for the proton, which is the rule of the series that the label names the input: the input of one species is the mass of that species. No wave number is ever labelled by the name of a particle alone.

**The wavelength is the inverse and never a second symbol.** The series keeps $\lambda$ wherever a length is what the sentence needs: the Compton shift, the range of a potential, the size of an atom. In this article it appears only inside an inversion, $1/k_m=\lambda_m$, $1/k_{\mathrm{mo}}=\lambda_p$ and $1/k_E=\lambda_E$, and never as an independent definition, so the three letters are three distances and not three further quantities. A display that wrote both a wave number and a wavelength for the same object, without the inversion between them, would be the duplication this notation exists to remove: the wave number is the form the equations take, and the wavelength is that number read as a distance.

**Why not $\mu$.** The letter $\mu$ names the permeability, the direction label and the index of a component, and it is not used for an inverse Compton length anywhere in the series.

**One caution on the neighbourhood.** The corpus writes $k_{\mathrm{eu}}$ for a Euclidean momentum after a Wick rotation, a number that is also an inverse length but belongs to a different construction. The two are told apart by the label: $\mathrm{eu}$ marks the continuation of a component to imaginary time, and its square is positive, $k_{\mathrm{eu}}^{2}\ge0$, whereas $k_E$ is a Lorentzian component and the box of this article carries a minus sign in the Minkowski form. No display mixes them.

## Summary

Three wave numbers come from one rule, a momentum divided by $\frac{m\,c}{k_m}$: $k_m=mc/\hbar$ from the mass, $k_{\mathrm{mo}}=\frac{k_m\,p}{m\,c}$ from the momentum, $k_E=E/(\frac{m\,c^{2}}{k_m})$ from the total energy. The first belongs to the particle and the other two to the state.

The mass shell, divided by $\frac{m^{2}\,c^{2}}{k_m^{2}}$ term by term, gives the box $k_E^{2}=k_{\mathrm{mo}}^{2}+k_m^{2}$. The three are the sides of a right triangle with the energy wave number the largest and the mass wave number the fixed side. The ratios of the sides are the kinematic parameters: $k_E/k_m=\gamma$, $k_{\mathrm{mo}}/k_E=\beta$ and $k_{\mathrm{mo}}/k_m=\gamma\beta$.

The mass wave number is where localization costs the rest energy: at $1/k_m$ the wave number spread is $k_m$ and the energy spread is $mc^{2}$, so a second particle can be made and the one-particle description ends. It is the rest-frame clock, $c\,k_m=c\,k_m$, which is $7.76\times10^{20}\ \mathrm{rad\,s^{-1}}$ for the electron. It is twice the trembling amplitude, and the amplitude times the trembling frequency is exactly $c$. It is the range of the force the particle carries, from $7.07\times10^{14}\ \mathrm{m^{-1}}$ for the pion to $4.6\times10^{17}\ \mathrm{m^{-1}}$ for the $Z$. It is the field that pays for a pair, $\frac{m\,c^{2}\,k_m}{e}=1.32\times10^{18}\ \mathrm{V\,m^{-1}}$ for the electron. It is $2\pi$ divided by the Compton wavelength, and the wave number at which elastic scattering gives way. It is the scale the hydrogen atom is $137$ of, and that ratio is the fine-structure constant.

The momentum wave number is the rate at which the phase winds. It fixes the fringe spacing $2\pi D/(d\,k_{\mathrm{mo}})$, and no state is narrower than half the inverse of its spread. It is the ruler of a bound state: the ground state of hydrogen is the one whose momentum wave number is the inverse Bohr radius, and the Bohr condition is the statement that the orbit accumulates a whole number of turns of phase. It is what a crystal diffracts, $5.12\times10^{10}\ \mathrm{m^{-1}}$ for a $100\ \mathrm{eV}$ electron and $6.26\times10^{10}\ \mathrm{m^{-1}}$ for a thermal neutron. It sets quantum degeneracy through $n/k_T^{3}\sim1$, met by a metal and not by a gas at room temperature. It grows with speed as $\gamma\beta k_m$, and it is the resolution of a collider.

The energy wave number is the wave number the particle would have if it were massless, and $k_{\mathrm{mo}}/k_E=\beta$ is the measure of how far it is from that. It is the temporal component of the wave four-vector, one radian per $1/(c\,k_E)$ of light travel. It is the inverse reach of a virtual deficit of energy, and the Yukawa range is the case of a deficit $mc^{2}$. It is the inverse decay length, $\Gamma/(\frac{m\,c^{2}}{k_m})=1/(c\tau)$: $0.128\ \mathrm{m^{-1}}$ for the pion and $1.265\times10^{16}\ \mathrm{m^{-1}}$ for the $Z$. It is the largest of the three, and at the Planck energy it is the inverse Planck length.

For the electron $k_m=2.5896\times10^{12}\ \mathrm{m^{-1}}$, and it is the same at every energy; at $1\ \mathrm{MeV}$ the other two are $k_E=5.0677\times10^{12}\ \mathrm{m^{-1}}$ and $k_{\mathrm{mo}}=4.3561\times10^{12}\ \mathrm{m^{-1}}$, at $100\ \mathrm{MeV}$ both are $5.0677\times10^{14}\ \mathrm{m^{-1}}$, and at rest the energy wave number equals the mass wave number while the momentum wave number vanishes.

None of the three is the size of the particle: the proton's charge radius times its mass wave number is four, and the electron is pointlike far below its own inverse. At $m=0$ the triangle degenerates, $k_E=k_{\mathrm{mo}}$ and the mass wave number is no longer a wave number of the problem. The massless equations of the series are exact for that reason, not approximate.

## Summary of Notation

| symbol | meaning |
|---|---|
| $k_m = \frac{mc}{\hbar}$ | The mass wave number, the inverse reduced Compton wavelength; $\mathsf{L}^{-1}$; the only one of the three that belongs to the particle alone |
| $k_{\mathrm{mo}} =\frac{k_m\,p}{m\,c}$ | The momentum wave number, the reduced wave number of the state; $\mathsf{L}^{-1}$; a property of the state |
| $k_E =\frac{k_m\,E}{m\,c^{2}}$ | The energy wave number, the temporal component of the wave four-vector; $\mathsf{L}^{-1}$; the largest of the three |
| $1/k_m=\lambda_m$, $1/k_{\mathrm{mo}}=\lambda_p$, $1/k_E=\lambda_E$ | The three distances, the inverses of the three wave numbers; each is the distance per radian of the corresponding phase |
| $k_E^{2}=k_{\mathrm{mo}}^{2}+k_m^{2}$ | The mass shell in wave numbers; the right triangle of the three |
| $\frac{k_E}{k_m}=\gamma$, $\frac{k_{\mathrm{mo}}}{k_E}=\beta$ | The side ratios, which are the kinematic parameters of the state |
| $\tilde K_{\mathrm{wk}}=i k_Ee_t+\vec k$ | The wave four-vector, whose natural norm is $-k_m^{2}$ |
| $\omega_C = c\,k_m =c\,k_m$ | The rest-frame angular frequency; one radian of phase per $1/k_m$ of light travel |
| $2\omega_C = 2c\,k_m$ | The trembling angular frequency; its amplitude $1/(2k_m)$ times it is $c$ |
| $\lambda_C = \frac{2\pi}{k_m}$ | The ordinary Compton wavelength, the shift in Compton scattering |
| $E_c =\frac{m\,c^{2}\,k_m}{e}$ | The pair-creation field, $1.32\times10^{18}\ \mathrm{V\,m^{-1}}$ for the electron |
| $a_0\,k_{m_e} = \frac{1}{\alpha}=137.036$ | The Bohr radius in wave numbers, and the fine-structure constant |
| $k_T =\frac{\sqrt{2\pi mk_BT}}{\frac{m\,c}{k_m}}$ | The thermal wave number, whose cube sets the degeneracy criterion $n/k_T^{3}\sim1$ |
| $\frac{m\,c^{2}}{k_m}= 197.32698\ \mathrm{MeV}\cdot\mathrm{fm}$ | The conversion between an energy and a wave number |
| $\gamma = \frac{E}{mc^{2}}$, $\beta = \frac{pc}{E}$ | The Lorentz factor and the speed, the two parameters the ratios give |
| $\mathsf{L}$, $\mathsf{M}$, $\mathsf{T}$ | The dimensions of length, mass and time of the notation conventions |

## Further Reading

- [Physics Units and Common Elements Conventions](physics-units-and-common-elements-conventions.html), for the five dimensions, the derived units, and the cautions on $k$ and on $\lambda$.
- [Operator and Calculus Conventions](operator-and-calculus-conventions.html), for the gradient as a pure element and the unit of each derivative.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the chiral pair in which the mass wave number appears as a coefficient and for the harmonic parameter whose entries are the energy wave number and the mass wave number.
- [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html), for the operator $\Box-k_m^{2}$ and the non-relativistic limit.
- [The Biquaternion D'Alembertian and Its Green's Functions](the-biquaternion-dalembertian-and-its-greens-functions.html), for the Yukawa kernel whose range is $1/k_m$.
- [Conformal Invariance and the Massless Limit in Biquaternionic Form](conformal-invariance-and-the-massless-limit-in-biquaternionic-form.html), for the degenerate case $k_m\to0$.
