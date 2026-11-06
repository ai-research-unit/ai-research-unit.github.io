# __The Mass Length Scale of a Massive Particle__

## Introduction

Every length in this series comes from one rule: divide $\hbar$ by a momentum. A particle of mass $m$ supplies three momenta, and each gives a length.

$$
\lambda_m = \dfrac{\hbar}{mc},
\qquad
\lambda_p = \dfrac{\hbar}{p},
\qquad
\lambda_E = \dfrac{\hbar c}{E}.
$$

The first belongs to the particle alone: it holds at rest, in every state, and in every frame, because $m$, $\hbar$ and $c$ are fixed. The other two belong to the state, and they move when the particle moves.

The three are not independent. The mass shell relates the three momenta, and one division turns that relation into a relation among the three lengths:

$$
\dfrac{1}{\lambda_E^{2}} = \dfrac{1}{\lambda_p^{2}} + \dfrac{1}{\lambda_m^{2}} .
$$

That relation is the content of this article. The three lengths close into a triangle, the triangle is the velocity triangle, and each of the three answers a different question about the same particle.

**The three questions.** The mass length answers *how close can the particle be brought to a point*. It is the distance at which the rest energy is the energy of the probe, so it is where a one-particle description stops being possible and where the force the particle carries runs out. The momentum length answers *how fast does the state wind*. It is the distance over which the phase of the state turns by one radian, so it is the spacing of interference fringes, the width of the narrowest state of that momentum, and the circumference of a bound orbit divided by $2\pi$. The energy length answers *how fast does the clock run*. It is the distance light covers while the phase turns by one radian, so it is the length a lapse of time becomes when it is read as a length, and it is the reach of any process that borrows a given energy.

**What is new here and what is not.** The definitions, the triangle and the values are bookkeeping. The physical readings are the subject: the rest of the article takes each of the three in turn, and states what it measures, where it enters as a threshold, and which equation of the series carries it.

The article is named for the mass length scale because that is the only one of the three the particle carries at rest. The other two are needed with it and not without it: the Dirac article of the series writes the coefficient of a mass term and the temporal entry of a parameter as two inverse lengths side by side, and a reader who has one of the three without the others cannot tell which of the two is which.

## The Three Definitions

**One rule, three times.** Each length is $\hbar$ divided by a momentum. The mass supplies the momentum $mc$, the state supplies $p$, and the energy supplies $E/c$. The last is the one that is easy to miss: an energy over $c$ is a momentum, so $\hbar c/E$ is a length by the same rule as the other two and not by a second one.

**The dimensions.** All three are lengths, and the check is one line:

$$
[\lambda_m]=[\lambda_p]=[\lambda_E]
=\frac{\mathsf{M}\mathsf{L}^2\mathsf{T}^{-1}}{\mathsf{M}\mathsf{L}\mathsf{T}^{-1}}=\mathsf{L},
$$

since $E/c$ carries $\mathsf{M}\mathsf{L}\mathsf{T}^{-1}$, the unit of a momentum, exactly as $mc$ and $p$ do.

**Why $\hbar$ and not $h$.** The series uses the reduced wavelength throughout. The ordinary de Broglie wavelength is $h/p=2\pi\lambda_p$ and the ordinary Compton wavelength is $h/(mc)=2\pi\lambda_m$; the factor $2\pi$ is the whole difference. The reduced forms are the ones that enter the exponents, the derivatives and the operator coefficients, which is why they are the ones with names here. A text that quotes $h/p$ must be divided by $2\pi$ before it is compared with a $\lambda$ of this series.

**The reduced form is the length per radian.** That is what the missing $2\pi$ means, and it is why the readings below are phrased per radian rather than per turn: a phase advances by one radian over one $\lambda$, and by a full turn over $2\pi\lambda$. Every comparison with a measured fringe spacing, a spectrometer reading or a quoted wavelength carries the $2\pi$ back.

**Which is which.** Three subscripts, three inputs, and no fourth symbol. The subscript names the quantity the length is computed from: $m$ for the mass, $p$ for the momentum, $E$ for the total energy. It never names the particle, so a length is never written $\lambda_{e}$ or $\lambda_{N}$ for an electron or a nucleon; the subscript is an input and not a label of the object.

**One length is invariant and two are not.** $\lambda_m$ is built from three constants, so no boost and no change of state touches it. $\lambda_p$ and $\lambda_E$ are built from the momentum and the energy of the state, so both move when the particle is accelerated. A statement about $\lambda_m$ is a statement about the species; a statement about $\lambda_p$ or $\lambda_E$ is a statement about one preparation of one particle.

## The Relation Between the Three

**The mass shell.** For a free particle,

$$
E^2 = p^2c^2 + m^2c^4,
$$

with $E$ the total energy, the rest energy included, and $p$ the magnitude of the three-momentum.

**Divide by $(\hbar c)^2$.** Every term is an energy squared, so every term becomes a squared momentum, and each bracket below is an inverse length:

$$
\frac{E^2}{(\hbar c)^2} = \frac{p^2c^2}{(\hbar c)^2} + \lambda_m^{-2},
\qquad\text{that is}\qquad
\left(\frac{E}{\hbar c}\right)^2 = \left(\frac{p}{\hbar}\right)^2 + \left(\frac{mc}{\hbar}\right)^2 .
$$

**Read each bracket as the inverse of a length.** Each is a reciprocal length, so the line becomes

$$
\boxed{\;\dfrac{1}{\lambda_E^{2}} = \dfrac{1}{\lambda_p^{2}} + \dfrac{1}{\lambda_m^{2}}\;}
$$

That box is the whole geometry of the three lengths, and it is the mass shell itself in other units.

**The triangle.** In inverse lengths the three sides form a right triangle whose hypotenuse is $1/\lambda_E$. The energy length is therefore the shortest of the three, and it is fixed by the other two through the combination in inverse squares:

$$
\lambda_E = \frac{\lambda_p\,\lambda_m}{\sqrt{\lambda_p^{2}+\lambda_m^{2}}} .
$$

**The ratios are the kinematic parameters.** With the Lorentz factor $\gamma=E/(mc^2)$ and the speed $\beta=pc/E$,

$$
\frac{\lambda_m}{\lambda_E}=\gamma,
\qquad
\frac{\lambda_E}{\lambda_p}=\beta,
\qquad
\frac{\lambda_m}{\lambda_p}=\gamma\beta .
$$

The triangle of inverse lengths is the energy–momentum triangle, whose side ratios are the kinematic parameters: the angle opposite the mass side has $\cos\theta=\beta$ and $\sin\theta=1/\gamma$.

**The two limits.** At rest, $p=0$ and $\lambda_p$ diverges, so the hypotenuse coincides with the mass side: $\lambda_E=\lambda_m$ and the momentum length is infinite. Ultra-relativistic, the mass side becomes negligible beside the other two, so $\lambda_E\to\lambda_p$, and the mass length stays where it was. The approach is $\lambda_p=\lambda_m/(\gamma\beta)\approx\lambda_m/\gamma$ for $\beta\to1$. The mass length is the fixed side of the triangle and the other two turn about it.

**Which of the two moving lengths is longer depends on the speed.** Their ratio is $\lambda_p/\lambda_m=1/(\gamma\beta)=\sqrt{1-\beta^{2}}/\beta$. They are equal at $\beta=1/\sqrt{2}$, the momentum length is the longer below that speed, and the shorter above it. At the speeds of ordinary matter the momentum length is enormously the longer, and at the energies of a collider it is the shorter.

**In natural units.** At $\hbar=c=1$ the three definitions lose their constants and read $\lambda_m=1/m$, $\lambda_p=1/p$ and $\lambda_E=1/E$, while the relation keeps its form. An article that sets the constants to one says so where it does it, and this line is the conversion that allows the return to units.

## The Values

The conversion is the product $\hbar c = 197.32698\ \mathrm{MeV}\cdot\mathrm{fm}$, which turns an energy into a length in one step: a length in femtometres is $197.327$ divided by the corresponding quantity in MeV, that quantity being $mc^2$ for $\lambda_m$, $pc$ for $\lambda_p$ and $E$ for $\lambda_E$. The particle masses are the CODATA 2018 values; $\hbar$ and $c$ are exact, and have been since the 2019 redefinition of the SI, so every uncertainty in the tables below comes from a mass.

**At rest.** The energy length equals the mass length, and the momentum length is infinite.

| particle | $mc^2$ | $\lambda_m=\lambda_E$ | $\lambda_p$ |
|---|---|---|---|
| electron | $0.510999\ \mathrm{MeV}$ | $386.159\ \mathrm{fm}$ | $\infty$ |
| proton | $938.272\ \mathrm{MeV}$ | $0.2103\ \mathrm{fm}$ | $\infty$ |
| muon | $105.658\ \mathrm{MeV}$ | $1.8676\ \mathrm{fm}$ | $\infty$ |
| charged pion | $139.570\ \mathrm{MeV}$ | $1.4138\ \mathrm{fm}$ | $\infty$ |

**The electron in motion.** The mass length is the same in every row and the other two move.

| $E$ | $\beta$ | $\lambda_E$ | $\lambda_p$ | $\lambda_m$ |
|---|---|---|---|---|
| $0.511\ \mathrm{MeV}$ | $0$ | $386.159\ \mathrm{fm}$ | $\infty$ | $386.159\ \mathrm{fm}$ |
| $1\ \mathrm{MeV}$ | $0.860$ | $197.327\ \mathrm{fm}$ | $229.562\ \mathrm{fm}$ | $386.159\ \mathrm{fm}$ |
| $100\ \mathrm{MeV}$ | $0.99999$ | $1.9733\ \mathrm{fm}$ | $1.9733\ \mathrm{fm}$ | $386.159\ \mathrm{fm}$ |
| $1\ \mathrm{GeV}$ | $1.000$ | $0.19733\ \mathrm{fm}$ | $0.19733\ \mathrm{fm}$ | $386.159\ \mathrm{fm}$ |

**A check of the relation.** At $1\ \mathrm{MeV}$ the three numbers satisfy the box, and the check is arithmetic in $\mathrm{fm}^{-2}$:

$$
\frac{1}{197.327^{2}} = 2.568\times10^{-5},
\qquad
\frac{1}{229.562^{2}}+\frac{1}{386.159^{2}} = 1.898\times10^{-5}+6.706\times10^{-6} = 2.568\times10^{-5}.
$$

**A photon.** For $m=0$ the mass length diverges and the other two coincide. At $1\ \mathrm{eV}$ both are $197.327\ \mathrm{nm}$, which is the reduced wavelength of that photon; the ordinary wavelength is $1239.842\ \mathrm{nm}$, the same number times $2\pi$.

**What the tables say.** The electron's mass length is $3.86\times10^{-13}\ \mathrm{m}$, which lies between the size of a nucleus and the size of an atom and closer to the nucleus. The lengths are in inverse proportion to the masses, so the ordering of the mass lengths is the reverse of the ordering of the masses, and that is the whole content of the definition.

## Where Each Form Is Used

The rule of the series is that a coefficient of a differential operator is an inverse length, because every derivative carries one. Two of the three lengths therefore appear as coefficients, and the third appears as the entry that the energy supplies.

| site in the series | form written | which length |
|---|---|---|
| the Dirac chiral pair | $\dfrac{1}{\lambda_m}$ | the mass |
| the Klein–Gordon operator | $\Box-\dfrac{1}{\lambda_m^{2}}$ | the mass |
| the shift of the Cauchy theory | $\kappa=-\dfrac{i}{\lambda_m}$ | the mass |
| the temporal entry of the harmonic parameter | $E/(\hbar c)$ | the energy |
| the spatial entry of the same parameter | $\dfrac{1}{\lambda_m}$ | the mass |
| the modulus of that parameter | $\dfrac{1}{\lambda_p}$ | the momentum |
| the non-relativistic criterion | $L\gg\lambda_m$ | the mass |
| the range of a Yukawa potential | $\lambda_m$ | the mass |
| the Zitterbewegung amplitude | $\tfrac12\lambda_m$ | the mass |
| the Compton shift | $\lambda_C=2\pi\lambda_m$ | the mass |
| interference and diffraction | $\lambda_p$ | the momentum |
| the phase of a plane wave, temporal part | $\lambda_E$ | the energy |

**The identity behind the middle rows.** The harmonic parameter of *The Dirac Equation in Biquaternionic Form* is

$$
\alpha = -\left(i\,\frac{E}{\hbar c}\,\vec e_x + \dfrac{1}{\lambda_m}\,\vec e_y\right),
$$

and its square is central because the two units anticommute, so that

$$
\alpha^2 = \dfrac{1}{\lambda_E^{2}} - \dfrac{1}{\lambda_m^{2}} = \dfrac{1}{\lambda_p^{2}} .
$$

The parameter's square is the squared wave number of the state, and by the box its modulus is the inverse momentum length. That is the box of this article read inside the operator, and it is why the two entries are inverse lengths of different kinds rather than one length written twice: the temporal entry is the whole hypotenuse and the spatial entry is one leg, so the difference of their squares is the remaining leg.

## The Mass Length

### What the Length Measures

**It is the length of the rest frame.** Set $p=0$. Then $\lambda_p$ diverges, $\lambda_E=\lambda_m$, and the triangle collapses onto the mass side. Every interpretation of $\lambda_m$ is therefore an interpretation in the rest frame, and the length travels with the particle unchanged, which is why it can be quoted as a property of the species.

**It is a wavelength and not a radius.** It is the wavelength of the field in its own rest frame, not the extent of the field in space. A particle whose mass length is $386\ \mathrm{fm}$ may have no measured size at all, and the two statements are compatible because a wavelength is a period of a phase and a radius is a distribution of charge. §*It Is Not the Size of the Particle* collects the numbers that make the difference unmistakable.

**It is the shortest distance at which the particle is still one particle.** The next subsection derives that statement, and it is the reading that carries the rest.

### The Cost of Localization

**Confine the particle and the momentum rises.** A region of size $L$ admits a momentum spread of order $\hbar/L$, by the uncertainty relation, and a momentum $p$ costs an energy $pc$ at least. The two together give an energy spread of order $\hbar c/L$, so the energy grows as the region shrinks.

**At $L=\lambda_m$ the spread is the rest energy.** Put $L=\lambda_m=\hbar/(mc)$:

$$
\Delta p \sim \dfrac{\hbar}{\lambda_m} = mc,
\qquad
\Delta E \sim \dfrac{\hbar c}{\lambda_m} = mc^2 .
$$

The energy available in the region has reached the energy needed to make a second particle of the same mass. Beyond that point the description with a fixed number of particles fails, not because the calculation is difficult, but because the state that would be described has the energy to become a different state.

**The crossing, said three ways.** It is the point where the Compton wavelength is resolved, the point where a probe photon carries the rest energy, and the point where the pair threshold is reached. The three are one number. For the electron the probe photon is $511\ \mathrm{keV}$, which is a hard gamma ray, and the length is $386\ \mathrm{fm}$, which is why no microscope resolves a free electron's own scale: the photon that would resolve it would create pairs instead.

**The same statement for any mass.** Since $\lambda_m$ is inversely proportional to $m$, the crossing is at a higher energy and a shorter distance for a heavier particle. A proton needs $938\ \mathrm{MeV}$ and $0.21\ \mathrm{fm}$; a top quark needs $173\ \mathrm{GeV}$ and $1.14\times10^{-3}\ \mathrm{fm}$. The rest energy per unit of mass length is $mc^2/\lambda_m=m^2c^3/\hbar$, and it grows as the square of the mass, which is why heavy particles probe short distances at high cost.

### The Rest-Frame Clock

**The field at rest still oscillates.** A field of mass $m$ at rest has a time dependence $e^{-i\omega_C t}$ with

$$
\omega_C = \dfrac{mc^2}{\hbar} = \dfrac{c}{\lambda_m} .
$$

For the electron this is $7.763\times10^{20}\ \mathrm{rad\,s^{-1}}$, that is $1.236\times10^{20}\ \mathrm{Hz}$. The number is not a curiosity: it is the rest energy divided by $\hbar$, and it is the rate at which the phase of the field turns in the frame where the particle is at rest.

**The period is a light-travel distance.** One full turn of that phase takes $T_C=2\pi/\omega_C=h/(mc^2)$, and light covers $cT_C=2\pi\lambda_m$ in that time. So the rest-frame clock and the mass length are one fact: the length is the distance light covers while the phase turns by one radian.

**The two are measured by different means.** The mass length is measured by scattering, in the Compton shift and in the falling cross-section; the rest-frame frequency is measured by interference between a particle and its antiparticle, in the oscillation of a neutral meson. Both return $mc^2$, and neither needs a particle at rest in the laboratory: the frequency is read as an energy difference and the length as a momentum transfer.

### The Zitterbewegung Amplitude

**The Dirac position trembles.** In the Dirac theory the velocity operator has eigenvalues $\pm c$, and the position has, besides a mean motion, an oscillating part. Its amplitude is of order

$$
\frac{\hbar}{2mc} = \tfrac12\lambda_m ,
$$

which is $193.080\ \mathrm{fm}$ for the electron. The oscillating part is the interference between the positive- and negative-frequency pieces of the state, which is why it exists in the Dirac theory and not in a one-component theory.

**The product of amplitude and frequency is $c$.** The angular frequency of the trembling is $2\omega_C=2c/\lambda_m$, twice the rest-frame rate, and the amplitude times that frequency is

$$
\tfrac12\lambda_m \times \dfrac{2c}{\lambda_m} = c .
$$

The trembling point moves at the speed of light, at the only speed a massless piece of the state can move. The identity is exact, and it is why the amplitude and the frequency cannot be chosen separately: the mass length fixes both.

**It is not the size of the particle.** The trembling is a motion, not an extent, and a point particle can tremble. What the amplitude measures is the distance the light-like components of the state travel during one half-period of their interference, and it is the Compton wavelength of the field up to the factor $2\pi$.

### The Range of a Force

**A virtual particle cannot travel farther than its mass length.** Exchange a particle of mass $m$ between two sources. The exchanged quantum is off shell by at least $mc^2$, so it can live for a time of order $\hbar/(mc^2)$, and the distance it covers in that time is $\hbar/(mc)=\lambda_m$. The potential that results falls as

$$
V(r) \propto \dfrac{e^{-r/\lambda_m}}{r},
$$

which is the Coulomb potential for $r\ll\lambda_m$ and exponentially small for $r\gg\lambda_m$. The range of the force is the mass length of the particle that carries it, and nothing else.

**The measured ranges.**

| carrier | $mc^2$ | $\lambda_m$ | force |
|---|---|---|---|
| photon | $<10^{-27}\ \mathrm{eV}$ | $>2\times10^{20}\ \mathrm{m}$ | electromagnetism |
| pion | $139.57\ \mathrm{MeV}$ | $1.4138\ \mathrm{fm}$ | the nuclear force |
| $Z$ | $91.188\ \mathrm{GeV}$ | $2.164\times10^{-18}\ \mathrm{m}$ | the weak neutral current |
| $W$ | $80.377\ \mathrm{GeV}$ | $2.455\times10^{-18}\ \mathrm{m}$ | the weak charged current |

**The ordering of the force ranges is the reverse of the ordering of the masses.** The electromagnetic force is long ranged because its carrier is massless; the weak force is the shortest because its carriers are the heaviest known gauge bosons; the nuclear force sits between them because the pion is light on the scale of the weak bosons. In every case the number that decides is $\lambda_m$, and no other number enters.

**The same statement in the operator.** The massive d'Alembertian of the series carries the coefficient $1/\lambda_m^{2}$, and its Green function is the Yukawa kernel. *The Biquaternion D'Alembertian and Its Green's Functions* derives it there, and the coefficient is the only place the mass enters. The range of the force and the coefficient of the operator are one length written twice.

**The Coulomb limit.** As $m\to0$ the exponential becomes a constant and the potential becomes $1/r$. The photon-mass bound in the table is the experimental statement that $\lambda_m$ for the photon is at least a galactic scale, so the Coulomb potential is the massless limit to within a bound far below any measurement of it.

### The Field That Pays for a Pair

**A strong enough field creates pairs.** A constant electric field does work $eEL$ on a charge over a distance $L$. If that work reaches the rest energy over one mass length, the field can separate a pair from the vacuum:

$$
eE_c\,\lambda_m = mc^2,
\qquad\text{that is}\qquad
E_c = \dfrac{mc^2}{e\,\lambda_m} = \dfrac{m^2c^3}{e\hbar} .
$$

For the electron the number is $1.323\times10^{18}\ \mathrm{V\,m^{-1}}$, the Schwinger field. The reading is direct: the rest energy, divided by the charge and by the mass length, is the field that supplies it over that length.

**The same number as a voltage.** Divide by $e$ and the statement becomes a potential difference: the rest energy per unit charge is $511\ \mathrm{kV}$, delivered over $386\ \mathrm{fm}$. Both numbers are the same pair again, energy and length, and the mass length is what fixes the second.

**Why the length is the invariant statement.** The critical field depends on the charge as well as on the mass, so it is not a property of the particle alone; the mass length is. The Schwinger field is the mass length read through the coupling, and it is quoted in volts per metre only because a laboratory field is measured that way.

### The Compton Shift

**The shift is the mass length measured with a spectrometer.** A photon of wavelength $\lambda$ scattered by a particle of mass $m$ emerges with

$$
\Delta\lambda = \lambda_C\,(1-\cos\theta),
\qquad
\lambda_C = \dfrac{h}{mc} = 2\pi\lambda_m .
$$

For the electron $\lambda_C=2.426\ \mathrm{pm}$, and the maximum shift, at backward scattering, is $2\lambda_C=4.85\ \mathrm{pm}$.

**The factor $2\pi$ is not decoration.** A spectrometer measures the ordinary wavelength, so the Compton formula is quoted with $\lambda_C$ and not with $\lambda_m$; the reduced length enters the theory and the ordinary one enters the instrument. The two differ by exactly the $2\pi$ that separates $\hbar$ from $h$ in the definition.

**When the effect is visible.** The shift is a fixed length, so it matters only when the incident wavelength is comparable to it. At $1\ \mathrm{pm}$ the shift is a few tenths of the wavelength; at $500\ \mathrm{nm}$ it is $10^{-5}$ of it and unobservable. That is why the Compton effect is a hard-X-ray and gamma-ray phenomenon and why visible-light scattering is Thomson scattering: the mass length marks the crossover, and the crossover is the usual one of a ratio of order one.

**The cross-section falls at the same length.** Below $\lambda_C$ the Klein–Nishina cross-section drops with energy, and the drop is the same statement as the pair threshold: the photon has enough energy to do more than shake the charge, and the elastic channel closes. The mass length marks both.

### The Atomic Comparison

**A hydrogen atom is $137$ mass lengths across.** The Bohr radius is $a_0=4\pi\epsilon_0\hbar c\lambda_m/e^2$ and the mass length of the electron is $\hbar/(m_ec)$. Their ratio needs no numerical input:

$$
\frac{a_0}{\lambda_m} = \frac{4\pi\epsilon_0\hbar c\lambda_m/e^2}{\lambda_m} = \frac{4\pi\epsilon_0\hbar c}{e^2} = \frac{1}{\alpha} = 137.036,
$$

with the fine-structure constant $\alpha=e^2/(4\pi\epsilon_0\hbar c)$. The agreement with the directly computed $5.29177\times10^{-11}/3.86159\times10^{-13}=137.036$ is the check.

**That ratio is the whole of the non-relativistic approximation.** The electron's speed in the ground state is $\alpha c$, so $\beta=\alpha$ and $\gamma-1\simeq\tfrac12\alpha^2$. Every relativistic correction to a hydrogen level is smaller than the level itself by a power of $\alpha$, and the power is set by $a_0/\lambda_m$.

**The atom's own three lengths.** In the ground state the momentum is $m_e\alpha c=\hbar/a_0$, so the momentum length is the Bohr radius itself: $\lambda_p=a_0$. The total energy is the rest energy less the binding energy, $E=m_ec^2-13.6\ \mathrm{eV}$, so the energy length is the mass length enlarged by the binding fraction $13.6/511000=2.7\times10^{-5}$:

$$
\lambda_m = 386.159\ \mathrm{fm},
\qquad
\lambda_p = a_0 = 52.9\ \mathrm{pm},
\qquad
\lambda_E = 386.169\ \mathrm{fm},
$$

and the ordering $\lambda_E\simeq\lambda_m\ll\lambda_p$ is the statement that the electron is slow. Only one ratio is large: $\lambda_p/\lambda_m=\lambda_p/\lambda_E=1/(\gamma\beta)\simeq1/\beta\simeq1/\alpha$, so the momentum length is the Bohr radius while the other two stay at the mass length.

**The binding has a length of its own, and it is not one of the three.** The energy that moves inside the atom is the binding energy, and $\hbar c/(13.6\ \mathrm{eV})=14.5\ \mathrm{nm}$ is the reduced wavelength of the photon at the ionization threshold. That number is not $\lambda_E$ of the state, because $\lambda_E$ is built from the total energy and the total energy carries the rest energy. It is the energy length of an energy difference, of the kind read in §*The Uncertainty in Time*, and it is two hundred and seventy times the Bohr radius: the photon that ionizes hydrogen is much larger than the atom it ionizes, which is why the photo-ionization cross-section is so small.

**What the ratio buys.** Because the ratio is the inverse fine-structure constant, a relativistic correction is smaller than the non-relativistic energy by a factor $\alpha^2$. The binding energy itself is $\tfrac12\alpha^2m_ec^2=13.6\ \mathrm{eV}$, and the corrections to it are of order $\alpha^4m_ec^2=1.4\ \mathrm{meV}$, a relative size of $2\alpha^2=1.1\times10^{-4}$. The scale $\alpha^2m_ec^2=27.2\ \mathrm{eV}$ is the binding scale and not the size of a correction; confusing the two overstates the corrections by the factor $1/\alpha^2=1.9\times10^{4}$. That the corrections sit four powers of $\alpha$ down follows from the same small parameter that makes $a_0\gg\lambda_m$, and it is why the Schrödinger equation with a Coulomb potential works as well as it does.

**Light and heavy.** At fixed $L$, a light particle has the larger $\lambda_m$ and reaches the relativistic regime first; a heavy particle stays non-relativistic in a smaller box.

## The Momentum Length

### It Belongs to the State

**It is the length of the preparation.** Two electrons of the same mass, one at rest and one at $1\ \mathrm{GeV}$, have the same $\lambda_m$ and momentum lengths that differ by nine orders of magnitude. Nothing about the momentum length can be tabulated for a species. It is quoted for a beam, a trap, a thermal ensemble or a bound orbit, and it changes when any of those changes.

**It is the inverse wave number, exactly.** A plane wave of momentum $p$ has the spatial phase $e^{i\vec p\cdot\vec x/\hbar}$, so the wave number is $\vec k=\vec p/\hbar$ and its magnitude is the reciprocal of the momentum length:

$$
k = \dfrac{p}{\hbar} = \dfrac{1}{\lambda_p} .
$$

That is the definition read the other way, and it is the form in which the length enters every equation of the series: the biquaternionic gradient $\tilde\nabla$ carries an inverse length, and on a plane wave it returns $1/\lambda_p$.

### The Phase Winding

**One radian per momentum length.** Walk along the direction of motion. The phase turns by one radian for every $\lambda_p$ travelled, and by a full turn for every $2\pi\lambda_p$. The reduced length is the distance per radian and the ordinary de Broglie wavelength is the distance per turn.

**The state is a clock and a ruler at once.** The temporal part of the same phase is fixed by the energy length, and the ratio of the two is the speed: the phase advances one radian in space per $\lambda_p$ and one radian in time per $\lambda_E/c$, so the crests move at $\lambda_p/(\lambda_E/c)=c\lambda_p/\lambda_E=c/\beta$. That superluminal number is the phase velocity, and §*The Energy Length* reads it.

**A change of momentum is a change of the winding.** Multiply the momentum by two and the length halves. There is no other content in the definition, which is why the momentum length is the easiest of the three to change and the hardest to mistake for a property of the particle.

### Interference and Diffraction

**Fringes are spaced by the momentum length.** Two slits a distance $d$ apart, a screen a distance $D$ away, a particle of momentum length $\lambda_p$. The path difference for a point at height $y$ is $yd/D$, so the phase difference is $yd/(D\lambda_p)$, and neighbouring maxima are separated by

$$
\Delta y = \dfrac{2\pi\lambda_p D}{d},
$$

which is the ordinary formula $\lambda D/d$ with $\lambda=2\pi\lambda_p$. The reduced length enters the phase and the ordinary one enters the ruler on the screen.

**A number.** Electrons of $100\ \mathrm{eV}$ have $\lambda_p=0.0195\ \mathrm{nm}$, so with $d=1\ \mu\mathrm{m}$ and $D=1\ \mathrm{m}$ the fringes are $0.12\ \mathrm{mm}$ apart and plainly visible. The same electrons through a crystal, whose planes are $0.2\ \mathrm{nm}$ apart, give diffraction angles of order $\pi\lambda_p/d=0.3\ \mathrm{rad}$: the crystal is the grating that matches the length.

**Diffraction is the same statement.** An aperture of width $w$ spreads the beam over an angle of order $2\pi\lambda_p/w$. The pattern is wide when the momentum length is long compared with the aperture, which is the wave regime, and narrow when it is short, which is the ray regime. The boundary between the two is a ratio of two lengths, one of them $\lambda_p$ and the other the apparatus.

### No State Is Narrower Than Half Its Momentum Length

**The uncertainty relation in the lengths.** Write $\Delta p=\hbar/\lambda_p$ and the relation $\Delta x\,\Delta p\ge\hbar/2$ becomes

$$
\Delta x \ge \tfrac12\lambda_p .
$$

A state of a given momentum cannot be squeezed below half its own momentum length. The width of the state and the length of its momentum are the same size, up to a factor of two, and the factor is the only thing the inequality leaves free.

**The corollary that matters.** A particle confined to a region $L$ has a momentum length of order $L$, because the confinement is what sets the spread. The two lengths of a confined state are therefore tied, and the energy that confinement costs is $\hbar^2/(2mL^2)$, the kinetic energy of a momentum $\hbar/L$. A trap of one momentum length is a trap at the edge of the quantum regime, and every statement about zero-point motion is a statement about that edge.

**Why the length is not a size, again.** The inequality makes the momentum length a lower bound on the width of the state, not an extent of the particle. A cold atom of momentum length $1\ \mu\mathrm{m}$ is not a micrometre across; it is a micrometre of phase, and its own mass length is four orders of magnitude smaller.

### Bound States as Standing Waves

**An orbit holds a whole number of momentum lengths.** The de Broglie condition for a circular orbit of radius $r$ is that the circumference contain a whole number of ordinary wavelengths, $2\pi r=n\lambda=2\pi n\lambda_p$, that is

$$
r = n\,\lambda_p .
$$

The ground state of hydrogen is the case $n=1$: the momentum length equals the orbit radius. And indeed the momentum in the ground state is $m_e\alpha c=\hbar/a_0$, so $\lambda_p=\hbar/p=a_0$ identically.

**That is why the Bohr condition is not an extra postulate.** It is the statement that the phase closes on itself after one turn, which is the same requirement as the single-valuedness of the wavefunction. The quantization counts momentum lengths around the orbit, and the count is an integer because a phase that does not close is not a function.

**The same count for any potential.** A bound state has $\oint p\,dq=2\pi\hbar(n+\tfrac12)$ in the semiclassical limit, which is the statement that the orbit contains $n+\tfrac12$ momentum lengths, the half coming from the two turning points. The momentum length is the ruler of the semiclassical theory and the integer is the number of times it fits.

### Matter Waves at the Crystal

**Two numbers worth remembering.** A $100\ \mathrm{eV}$ electron has $\lambda_p=0.0195\ \mathrm{nm}$ and an ordinary wavelength of $0.123\ \mathrm{nm}$. A neutron at $300\ \mathrm{K}$ has the thermal momentum $p_T=\sqrt{2\pi mk_BT}$, giving $\lambda_p=0.0160\ \mathrm{nm}$ and an ordinary wavelength of $0.100\ \mathrm{nm}$.

**The crystal spacing matches them.** Atomic planes are of order $0.2\ \mathrm{nm}$ apart, the same decade as both numbers, so a crystal diffracts both electrons and neutrons. The Bragg condition in the reduced form is $2d\sin\theta=2\pi n\lambda_p$, and the $2\pi$ is the only change from the textbook version.

**Why neutrons and not protons.** A proton at $300\ \mathrm{K}$ has a thermal momentum length smaller than the neutron's only by the square root of the mass ratio, which is not enough to matter; what decides the choice is that the neutron is neutral and penetrates the crystal, while the proton is stopped in the first layer. The lengths are comparable; the interactions are not.

### The Thermal Momentum Length

**Temperature supplies a momentum.** A thermal ensemble has $p_T=\sqrt{2\pi mk_BT}$, so

$$
\lambda_p = \dfrac{\hbar}{\sqrt{2\pi mk_BT}} .
$$

For the electron at $300\ \mathrm{K}$ this is $0.685\ \mathrm{nm}$, with an ordinary wavelength of $4.30\ \mathrm{nm}$; for the neutron, $0.0160\ \mathrm{nm}$ and $0.100\ \mathrm{nm}$.

**The degeneracy criterion is a count of lengths per particle.** A gas is quantum when the volume per particle is comparable to the cube of the momentum length:

$$
n\,\lambda_p^{3} \sim 1 .
$$

For the electron at $300\ \mathrm{K}$ the criterion is reached at $n=3.1\times10^{27}\ \mathrm{m^{-3}}$; a metal has $8.5\times10^{28}\ \mathrm{m^{-3}}$ in its conduction band, so $n\lambda_p^{3}=27$ and the electron gas is degenerate. That is why a metal is described by a Fermi sea and not by a classical gas, and the number that decides it is the momentum length.

**The same count for a gas of atoms.** Cool a gas until $\lambda_p$ grows to the interparticle spacing and the atoms lose their identity as distinguishable objects; the condensate appears at that point. The criterion is the same one, with the mass of the atom in place of the mass of the electron, and it is met at nanokelvin temperatures because the atom is heavy.

### It Shortens with Speed

**The length is inversely proportional to the momentum.** Since $p=\gamma mv$,

$$
\lambda_p = \dfrac{\hbar}{\gamma mv} = \dfrac{\lambda_m}{\gamma\beta} .
$$

At rest it diverges; at $\beta=1/\sqrt{2}$ it equals the mass length; at $\beta\to1$ it goes to $\lambda_m/\gamma$ and falls without bound as the energy rises. The momentum length and the energy length can both be made arbitrarily small by raising the energy; only the mass length is fixed. At $1\ \mathrm{TeV}$ an electron's momentum length is $1.97\times10^{-19}\ \mathrm{m}$, and its energy length is the same number.

**That is the resolution of a collider.** Two beams collide with a momentum length far below the size of a proton, and the collisions resolve structure at that length. The statement that a collider probes a given distance is a statement about $\lambda_p$, not about any particle's size.

### Not a Size Either

**A cold atom.** $\lambda_p=1\ \mu\mathrm{m}$ for an atom at microkelvin temperatures, and the atom is $0.1\ \mathrm{nm}$ across. The ratio is four orders of magnitude, in the direction opposite to the naive reading.

**A macroscopic object.** A grain of $1\ \mathrm{g}$ moving at $1\ \mathrm{mm\,s^{-1}}$ has $p=10^{-6}\ \mathrm{kg\,m\,s^{-1}}$ and $\lambda_p=1.05\times10^{-28}\ \mathrm{m}$, twenty orders of magnitude below the grain. No interference is observable, and the reason is not that the grain is large but that its momentum length is small compared with every aperture available.

## The Energy Length

### The Wavelength the Particle Would Have If It Were Massless

**The cleanest reading of the third length.** A photon of energy $E$ has momentum $E/c$, so its momentum length and its energy length are the same number:

$$
\lambda_p = \dfrac{\hbar}{E/c} = \dfrac{\hbar c}{E} = \lambda_E .
$$

For a massive particle the two differ, and their ratio is the speed:

$$
\dfrac{\lambda_E}{\lambda_p} = \beta .
$$

So $\lambda_E$ is the wavelength the particle would have if all of its energy were carried by a massless quantum. It is the photon-equivalent wavelength, and the ratio $\beta$ measures how far the particle is from that ideal.

**The two limits read themselves.** At rest $\beta=0$ and $\lambda_E$ is infinitely shorter than $\lambda_p$, which has diverged: the particle has energy and no momentum, and no massless quantum imitates that. At $\beta\to1$ the two lengths merge, and the wave is indistinguishable from a light wave of the same energy. Every ultra-relativistic particle is photon-like in this precise sense, and the series uses that fact whenever it treats a fast fermion as a light-like field.

**It is also the temporal wavelength.** The same number is the reciprocal of the temporal component of the wave four-vector:

$$
k_0 = \dfrac{\omega}{c} = \dfrac{E}{\hbar c} = \dfrac{1}{\lambda_E} .
$$

A wave whose spatial wavelength is $\lambda_p$ and whose temporal wavelength is $\lambda_E$ moves at $\beta=\lambda_E/\lambda_p$, which is the same statement again.

### The Clock

**One radian of phase per energy length.** The phase of a plane wave is $kx-\omega t$ with $\omega=E/\hbar$. Over a time $t=\lambda_E/c$ the phase turns by $\omega t=E\lambda_E/(\hbar c)=1$. So the energy length is the distance light covers while the phase turns by one radian, in the same way that the momentum length is the distance the particle covers while the phase turns by one radian.

**The clock of any process.** A reaction whose energy changes by $\Delta E$ has a phase that turns at $\Delta E/\hbar$, and the length associated with that turn is $\hbar c/\Delta E$. Every oscillation, every beat and every interference term in the series can be read as a length this way, and the reading is exact: the energy length of the difference is the length of the beat.

### The Phase Velocity

**The crests travel faster than the particle.** The phase velocity of a matter wave is $v_{\mathrm{ph}}=\omega/k=E/p=c^2/v$. In one period $T=h/E$ the crests cover

$$
v_{\mathrm{ph}}T = \dfrac{E}{p}\dfrac{h}{E} = \dfrac{h}{p} = 2\pi\lambda_p ,
$$

while light covers $cT=hc/E=2\pi\lambda_E$. The two distances are in the ratio $\lambda_p/\lambda_E=1/\beta$: the crests outrun light by the factor $1/\beta$, and the excess carries no signal because the envelope moves at $v$.

**Why the two lengths are both needed.** The crest spacing is the momentum length and the light-travel distance per period is the energy length. A notation with only one of the two could not state the phase velocity, which is why the series keeps both and why the harmonic parameter of the Dirac article carries one in each entry.

### The Uncertainty in Time

**A borrowed energy lasts a time.** The relation $\Delta E\,\Delta t\ge\hbar/2$ says that a process which borrows an energy $\Delta E$ can last a time of order $\hbar/\Delta E$. Convert the time to a length and the statement becomes: the process can reach a distance

$$
c\,\Delta t \sim \dfrac{\hbar c}{\Delta E} = \lambda_E(\Delta E),
$$

the energy length of the borrowed energy.

**The Yukawa range is the special case.** A virtual particle of mass $m$ borrows $\Delta E=mc^2$, so its reach is $\hbar c/(mc^2)=\lambda_m$, which is the range derived in §*The Range of a Force*. The two derivations are one derivation, and the energy length is the general form of the mass length's range statement: the reach of a virtual process is the energy length of its deficit.

**The reach of a virtual photon is not infinite.** A virtual photon of energy $\Delta E$ reaches $\hbar c/\Delta E$; only the exactly massless, exactly zero-energy exchange reaches arbitrarily far, and the Coulomb potential is the sum over all of them.

### The Decay Length

**A width is a length.** An unstable particle of mean life $\tau$ has a width $\Gamma=\hbar/\tau$. The energy length of the width is

$$
\lambda_E(\Gamma) = \dfrac{\hbar c}{\Gamma} = c\tau ,
$$

which is the distance the particle travels before it decays. The same number is a wavelength and a flight path, and the equality is not a coincidence: both are $\hbar c$ divided by an energy.

**Two numbers.** The charged pion has $\tau=2.60\times10^{-8}\ \mathrm{s}$, so $c\tau=7.80\ \mathrm{m}$: a pion at rest decays after seven metres of light travel, which is why a pion beam line is measured in metres. The $Z$ boson has $\Gamma=2.496\ \mathrm{GeV}$, so $\lambda_E=0.0791\ \mathrm{fm}$: its decay length is smaller than a proton, which is why it leaves no track.

**The pair of statements is one measurement.** A width read in an energy spectrum and a lifetime read in a beam line give the same length, and the conversion between them is the same $\hbar c$ that converts every energy in this article into a length.

### It Is the Shortest of the Three

**The hypotenuse is the shortest side in inverse lengths.** Since $1/\lambda_E$ is the hypotenuse of the triangle, $\lambda_E\le\lambda_p$ and $\lambda_E\le\lambda_m$, with equality at rest for the first and in the massless limit for the second. The energy length is the shortest of the three at every speed.

**It falls without bound.** It tracks the total energy, and the total energy grows without limit as the particle is accelerated, so the energy length can be made as small as the energy allows. At the Planck energy, $1.22\times10^{19}\ \mathrm{GeV}$, it reaches $1.616\times10^{-35}\ \mathrm{m}$, which is the Planck length. That is not a coincidence either: the Planck length is defined as the energy length of the Planck energy, so the statement is a tautology once the definition is read.

### It Is Not Independent

**Two lengths fix the third.** Given the mass length and the momentum length, the box gives the energy length; given the mass length and the energy length, the box gives the momentum length. No physical statement is added by naming it. What is added is a name for a quantity that already appears as a coefficient: the temporal entry of the harmonic parameter is $E/(\hbar c)$ and nothing else.

**Why name it anyway.** Because the same number appears in four unrelated places — the photon-equivalent wavelength, the phase clock, the reach of a virtual deficit and the decay length — and a reader who meets $\hbar c/E$ in one of them should recognize it in the others. The name is a convenience of the notation and not a new dynamical quantity, and this article is careful to say so.

## The Ladder

**One column of energies, one column of lengths.** The conversion $\hbar c=197.32698\ \mathrm{MeV}\cdot\mathrm{fm}$ gives a length for every energy, and the same table read with $k_BT$ in place of $E$ gives a length for every temperature.

| energy | $\lambda_E$ | temperature | $\lambda_E$ |
|---|---|---|---|
| $1\ \mathrm{meV}$ | $0.197\ \mathrm{mm}$ | $1\ \mathrm{K}$ | $2.290\ \mathrm{mm}$ |
| $1\ \mathrm{eV}$ | $197.327\ \mathrm{nm}$ | $2.725\ \mathrm{K}$ | $0.840\ \mathrm{mm}$ |
| $1\ \mathrm{keV}$ | $0.197\ \mathrm{nm}$ | $300\ \mathrm{K}$ | $7.63\ \mu\mathrm{m}$ |
| $1\ \mathrm{MeV}$ | $197.3\ \mathrm{fm}$ | $10^{9}\ \mathrm{K}$ | $2.29\ \mathrm{pm}$ |
| $1\ \mathrm{GeV}$ | $0.197\ \mathrm{fm}$ | | |
| $1\ \mathrm{TeV}$ | $1.97\times10^{-19}\ \mathrm{m}$ | | |
| $1.22\times10^{19}\ \mathrm{GeV}$ | $1.616\times10^{-35}\ \mathrm{m}$ | | |

**Three columns are the same column.** The row for $1\ \mathrm{eV}$ is the row for $11605\ \mathrm{K}$ and the row for $1.78\times10^{-36}\ \mathrm{kg}$; the three quantities are related by exact constants, and the length is one way of writing any of them. The ladder is the conversion table of the whole series, and every order-of-magnitude statement in it can be read from this table alone.

**A caution that the table invites.** The ladder gives a length for every energy, and the length is a scale and not an extent. The $1\ \mathrm{eV}$ entry, $197\ \mathrm{nm}$, is the reduced wavelength of a visible photon; it is not the size of anything. The $1\ \mathrm{MeV}$ entry, $197\ \mathrm{fm}$, is the reduced wavelength of a gamma ray; it is not the radius of a nucleus. Reading the table as a list of sizes is the mistake that §*It Is Not the Size of the Particle* refutes.

## The Non-Relativistic Criterion

**The condition.** Non-relativistic quantum mechanics applies when the length over which the particle is localized or probed is much larger than its mass scale:

$$
L \gg \lambda_m .
$$

The three ways of writing the same condition are $p\ll mc$, $\lambda_p\gg\lambda_m$ and $\lambda_E\simeq\lambda_m$. The last is the easiest to apply, since $\lambda_E=\lambda_m/\gamma$ and the criterion is $\gamma\simeq1$.

**The hydrogen atom is the case in point.** The ratio $a_0/\lambda_m=1/\alpha=137.036$ derived in §*The Atomic Comparison* is the criterion satisfied with room to spare, and the room is exactly the inverse fine-structure constant.

**Light and heavy.** At fixed $L$, a light particle has the larger $\lambda_m$ and reaches the relativistic regime first; a heavy particle stays non-relativistic in a smaller box. That is why the electron in a light atom is relativistic to a few parts in $10^{5}$ and the nucleons in the same atom are not.

## The Massless Case

**The degenerate triangle.** As $m\to0$ the mass side diverges and the box loses that term:

$$
\lambda_m\to\infty,
\qquad
\dfrac{1}{\lambda_m}\to 0,
\qquad
\lambda_E=\lambda_p .
$$

The triangle flattens: the hypotenuse falls on the momentum side. The energy length and the momentum length become one length, which is the reduced wavelength of the particle, and the mass length is no longer a length of the problem.

**No non-relativistic limit.** The criterion $\lambda_p\gg\lambda_m$ reads $\lambda_p\gg\infty$ at $m=0$ and can never hold at a finite momentum. A massless particle has no rest frame, always moves at $c$, and the relativistic description is not a high-energy regime of a non-relativistic one; it is the only description.

**The rest-frame clock stops.** $\omega_C=c/\lambda_m\to0$ as the mass length diverges: the field of a massless particle has no rest-frame oscillation, because there is no frame in which it rests. The Compton period, the trembling and the rest-frame phase are lost together, and their loss is the flattening of the triangle.

**In the series.** The massless case is treated as exact and not as a limit. The Dirac chiral pair decouples at $m=0$ into the two one-sided equations $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R}=0$ and $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=0$, and *Conformal Invariance and the Massless Limit in Biquaternionic Form* treats the massless field on its own terms. The vanishing coefficient is what makes the decoupling exact.

**The photon.** The empirical bound on a photon mass is of order $10^{-27}\ \mathrm{eV}/c^2$. With $\hbar c=1.973\times10^{-7}\ \mathrm{eV}\cdot\mathrm{m}$, that bound gives

$$
\lambda_m = \lambda_{m_\gamma} \gtrsim \frac{1.973\times10^{-7}}{10^{-27}}\ \mathrm{m} \approx 2\times10^{20}\ \mathrm{m},
$$

which is of the order of a galactic scale. A smaller mass gives a longer length, and the Coulomb potential is the massless limit of the Yukawa potential.

## It Is Not the Size of the Particle

The name invites a mistake, and the numbers refute it.

**The proton.** Its mass length is $\lambda_m=0.2103\ \mathrm{fm}$. Its charge radius, measured by electron scattering and by hydrogen spectroscopy, is $r_p=0.8414\ \mathrm{fm}$. The radius is four times the mass length:

$$
\frac{r_p}{\lambda_m} = \frac{0.8414}{0.2103} = 4.001 .
$$

If $\lambda_m$ were the radius, the ordering would be inverted and the comparison meaningless. The radius is a strong-interaction scale; the mass length is a relativistic quantum one.

**The electron.** Its mass length is $386.159\ \mathrm{fm}$. No finite size has been observed: the experimental bounds on the electron radius lie below $10^{-18}\ \mathrm{m}$. A length of $3.9\times10^{-13}\ \mathrm{m}$ cannot be the radius of an object that is pointlike more than five orders of magnitude below it; the ratio of the two bounds is $3.9\times10^{5}$.

**A size and a scale behave differently under a boost.** A size is a fixed extent and transforms by length contraction; the mass length does not move at all, and the other two transform as the reciprocals of the components of a four-vector. Two quantities that transform differently cannot be the same quantity, and the observation needs no numbers: the definition of $\lambda_m$ contains no state, so no boost can act on it.

**A size and a scale behave differently under a probe.** A size is measured by resolving it, and the probe must have a shorter wavelength than the size. A scale is measured by finding where a description changes: the mass length where a cross-section falls or a pair appears, the momentum length where a fringe appears, the energy length where a clock beats. The first is a measurement of extent; the last three are measurements of thresholds.

**The statement.** Each of the three lengths is a scale at which a description changes, not an extent in space. The mass length is where the quantum and the relativistic descriptions meet, the momentum length is where the phase of the state winds, and the energy length is where its clock ticks. An article that calls any of them the size of the particle is wrong, and the comparisons above are the warrant.

## The Letter and the Subscript

**Why a subscript at all.** The letter $\lambda$ already carries three meanings in the corpus: a central value, its own set of eigenvalues, and the helicity weight $\lambda=\vec u_p\cdot\vec S$ of *Helicity in Biquaternionic Form*; it also appears as a free exponent in $e^{\lambda}$. A bare $\lambda$ for a fourth meaning would be ambiguous in every article that uses two of them.

**Which subscript.** The subscript names the quantity the length is computed from and never the particle. The mass gives $\lambda_m$, the momentum gives $\lambda_p$, the total energy gives $\lambda_E$. The three subscripts are the three inputs, so the family reads as one scheme and not as three unrelated names; a length that depends on both mass and momentum is written by the box above and takes no fourth subscript.

**Why not the standard glyph.** The literature writes the reduced Compton wavelength with a bar through the lambda. The site renders mathematics with KaTeX, which has no macro for that glyph, and $\bar\lambda$ already means the complex conjugate of a scalar, as in $(\lambda T)^{*}=\bar\lambda\,T^{*}$ of the Banach articles. The subscripted form is the rendering that survives.

**No letter for the reciprocals.** The inverse lengths $mc/\hbar$, $p/\hbar$ and $E/(\hbar c)$ carry no symbol of their own. They are written $\dfrac{1}{\lambda_m}$, $\dfrac{1}{\lambda_p}$ and $\dfrac{1}{\lambda_E}$ in a display, and as the quotient itself when a field or an operator multiplies them, as in $\dfrac{\tilde{Ξ}_{\mathrm{sp},L}}{\lambda_m}$. The series writes them as divisions and never as negative powers. The letter $\mu$ is not used for any of them: it names the permeability and the direction label, and the inverse Compton length is no longer written with it anywhere in the series.

## Summary

Three lengths come from one rule, $\hbar$ divided by a momentum: $\lambda_m=\hbar/(mc)$ from the mass, $\lambda_p=\hbar/p$ from the momentum, $\lambda_E=\hbar c/E$ from the total energy. The first belongs to the particle and the other two to the state.

The mass shell, divided by $(\hbar c)^2$, gives the box $\dfrac{1}{\lambda_E^{2}}=\dfrac{1}{\lambda_p^{2}}+\dfrac{1}{\lambda_m^{2}}$. The three sides form a right triangle in inverse lengths, with the energy length the shortest and the mass length the fixed side. The ratios of the sides are the kinematic parameters: $\lambda_m/\lambda_E=\gamma$, $\lambda_E/\lambda_p=\beta$ and $\lambda_m/\lambda_p=\gamma\beta$.

The mass length is where localization costs the rest energy: at $L=\lambda_m$ the momentum spread is $mc$ and the energy spread is $mc^2$, so a second particle can be made and the one-particle description ends. It is the rest-frame clock, $c/\lambda_m=mc^2/\hbar$, which is $7.76\times10^{20}\ \mathrm{rad\,s^{-1}}$ for the electron. It is twice the trembling amplitude, and the amplitude times the trembling frequency is exactly $c$. It is the range of the force the particle carries, from $1.4138\ \mathrm{fm}$ for the pion to $2.455\times10^{-18}\ \mathrm{m}$ for the $W$. It is the field that pays for a pair, $mc^2/(e\lambda_m)=1.32\times10^{18}\ \mathrm{V\,m^{-1}}$ for the electron. It is the Compton shift divided by $2\pi$, and the wavelength at which elastic scattering gives way. It is the scale the hydrogen atom is $137$ of, and that ratio is the fine-structure constant.

The momentum length is the distance per radian of the phase. It fixes the fringe spacing $2\pi\lambda_p D/d$, and no state is narrower than half of it. It is the ruler of a bound state: the ground state of hydrogen is the one whose momentum length equals the Bohr radius, and the Bohr condition is the statement that the orbit holds a whole number of them. It is what a crystal diffracts, $0.0195\ \mathrm{nm}$ for a $100\ \mathrm{eV}$ electron and $0.0160\ \mathrm{nm}$ for a thermal neutron. It sets quantum degeneracy through $n\lambda_p^{3}\sim1$, met by a metal and not by a gas at room temperature. It shortens with speed as $\lambda_m/(\gamma\beta)$, and it is the resolution of a collider.

The energy length is the wavelength the particle would have if it were massless, and $\lambda_E/\lambda_p=\beta$ is the measure of how far it is from that. It is the phase clock, one radian per $\lambda_E$ of light travel. It is the reach of a virtual deficit of energy, and the Yukawa range is the case of a deficit $mc^2$. It is the decay length, $\hbar c/\Gamma=c\tau$: seven metres for the pion and $0.0791\ \mathrm{fm}$ for the $Z$. It is the shortest of the three, and at the Planck energy it is the Planck length.

For the electron $\lambda_m=386.159\ \mathrm{fm}$, and it is the same at every energy; at $1\ \mathrm{MeV}$ the other two are $\lambda_E=197.327\ \mathrm{fm}$ and $\lambda_p=229.562\ \mathrm{fm}$, at $100\ \mathrm{MeV}$ both are $1.9733\ \mathrm{fm}$, and at rest the energy length equals the mass length while the momentum length diverges.

None of the three is the size of the particle: the proton's charge radius exceeds its mass length fourfold, and the electron is pointlike far below its own. At $m=0$ the triangle degenerates, $\lambda_E=\lambda_p$ and the mass length is no longer a length of the problem. The massless equations of the series are exact for that reason, not approximate.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\lambda_m = \frac{\hbar}{mc}$ | The mass length scale, the reduced Compton wavelength; $\mathsf{L}$; the only one of the three that belongs to the particle alone |
| $\lambda_p = \frac{\hbar}{p}$ | The momentum length, the reduced de Broglie wavelength; $\mathsf{L}$; a property of the state |
| $\lambda_E = \frac{\hbar c}{E}$ | The energy length, the inverse temporal wave number; $\mathsf{L}$; the shortest of the three |
| $\dfrac{1}{\lambda_E^{2}}=\dfrac{1}{\lambda_p^{2}}+\dfrac{1}{\lambda_m^{2}}$ | The mass shell in inverse lengths; the right triangle of the three |
| $\frac{\lambda_m}{\lambda_E}=\gamma$, $\frac{\lambda_E}{\lambda_p}=\beta$ | The side ratios, which are the kinematic parameters of the state |
| $\omega_C = \frac{mc^2}{\hbar} = \frac{c}{\lambda_m}$ | The rest-frame angular frequency; one radian of phase per $\lambda_m$ of light travel |
| $2\omega_C = \frac{2c}{\lambda_m}$ | The trembling angular frequency; its amplitude $\tfrac12\lambda_m$ times it is $c$ |
| $\lambda_C = \frac{h}{mc} = 2\pi\lambda_m$ | The ordinary Compton wavelength, the shift in Compton scattering |
| $E_c = \frac{mc^2}{e\lambda_m}$ | The pair-creation field, $1.32\times10^{18}\ \mathrm{V\,m^{-1}}$ for the electron |
| $a_0 = \frac{4\pi\epsilon_0\hbar c\lambda_m}{e^2}$ | The Bohr radius, with $a_0/\lambda_m = 1/\alpha$ and $a_0=\lambda_p$ in the ground state |
| $\alpha = \frac{e^2}{4\pi\epsilon_0\hbar c}$ | The fine-structure constant, $1/137.036$ |
| $p_T = \sqrt{2\pi mk_BT}$ | The thermal momentum, whose length sets the degeneracy criterion $n\lambda_p^{3}\sim1$ |
| $\hbar c = 197.32698\ \mathrm{MeV}\cdot\mathrm{fm}$ | The conversion between an energy and a length |
| $\gamma = E/(mc^2)$, $\beta = pc/E$ | The Lorentz factor and the speed, the two parameters the ratios give |
| $\mathsf{L}$, $\mathsf{M}$, $\mathsf{T}$ | The dimensions of length, mass and time of the notation conventions |

## Further Reading

- [Unit, Index and Notation Conventions](unit-index-and-notation-conventions.html), for the five dimensions, the three lengths in the table of derived units, and the cautions on $\mu$ and on $\lambda$.
- [Operator and Calculus Conventions](operator-and-calculus-conventions.html), for the gradient as a pure element and the unit of each derivative.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the chiral pair in which the mass length appears in the denominator and for the harmonic parameter whose entries are the energy length and the mass length.
- [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html), for the operator $\Box-1/\lambda_m^{2}$ and the non-relativistic limit.
- [The Biquaternion D'Alembertian and Its Green's Functions](the-biquaternion-dalembertian-and-its-greens-functions.html), for the Yukawa kernel whose range is $\lambda_m$.
- [Conformal Invariance and the Massless Limit in Biquaternionic Form](conformal-invariance-and-the-massless-limit-in-biquaternionic-form.html), for the degenerate case $\lambda_m\to\infty$.
