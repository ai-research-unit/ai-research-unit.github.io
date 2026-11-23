# __The Three Wavenumbers of a Particle__

## Introduction

This article has one object and one operation. The object is the four-momentum of a particle of mass $m$,

$$
\tilde P_{\Phi}=i\,p_{t}^{\prime}\,e_{t}+\vec p_{\Phi}=i\,\frac{E}{c}\,e_{t}+\gamma m\,\vec v,
$$

and the operation is its division by $h$. Define

$$
\tilde\Upsilon_{\Phi}:=\frac{\tilde P_{\Phi}}{h}.
$$

Nothing else is assumed. The three wave numbers of the title are the coordinates of $\tilde\Upsilon_{\Phi}$, and they are deduced from that division rather than postulated beside it.


The deduction. $h$ is a real central scalar, so it divides every coefficient of the element and touches no basis unit. Distributing it over the four units gives

$$
\tilde\Upsilon_{\Phi}=\frac{1}{h}\left(i\,p_{t}^{\prime}\,e_{t}+\vec p_{\Phi}\right)
=i\,\frac{p_{t}^{\prime}}{h}\,e_{t}+\frac{\vec p_{\Phi}}{h},
$$

and writing the same element as $\tilde\Upsilon_{\Phi}=i\,\nu_t^{\prime}e_{t}+\vec\nu_{\Phi}$ makes the coefficients of the two displays equal term by term:

$$
h\,\nu_t^{\prime}=p_{t}^{\prime},
\qquad
 h\,\vec\nu_{\Phi}=\vec p_{\Phi},
\qquad\text{that is}\qquad
\nu_t^{\prime}=\frac{p_{t}^{\prime}}{h}=\frac{E}{h\,c},
\qquad
\vec\nu_{\Phi}=\frac{\vec p_{\Phi}}{h}=\frac{\gamma m}{h}\,\vec v .
$$

That matching is the whole deduction: the coordinates of the quotient are the coordinates of the momentum, divided by $h$, in the same slot. The vector part has a modulus, $\nu_{\Phi}:=\lvert\vec\nu_{\Phi}\rvert$. The element has a biquaternion norm, and that norm fixes the mass wave number:

$$
-\langle\tilde\Upsilon_{\Phi}\rangle_{\natural}=\nu_m^{2},
\qquad
\nu_m=\frac{m\,c}{h},
$$

the inverse Compton wavelength, the third of the three. The third number is therefore read off the quotient too, as the value its two coordinates must satisfy.

The division changes the unit and nothing else. $h$ commutes with every coefficient, is fixed by all four involutions, and moves no element from one sector into another. The momentum is anti-Hermitian, so the quotient is anti-Hermitian, and $\tilde\Upsilon_{\Phi}$ stays in $\mathbb{B}_{\Phi}$ where $\tilde P_{\Phi}$ was. What changes is the dimension, from $\mathsf{M}\,\mathsf{L}\,\mathsf{T}^{-1}$ to $\mathsf{L}^{-1}$.

The two coordinates belong to the state and move when the particle moves. The norm does not: it is built from $m$, $h$ and $c$ alone, so it holds at rest, in every state and in every frame.

The three are not independent. The momentum is on shell, $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}=-m^{2}c^{2}$, and dividing that line by $h^{2}$ turns it into the norm of $\tilde\Upsilon_{\Phi}$, which read in coefficients is a relation among the three wave numbers:

$$
\tilde\Upsilon_{\Phi}\tilde\Upsilon_{\Phi}^{\natural}=-\nu_t^{\prime\,2}+\nu_{\Phi}^{2}=-\nu_m^{2},
\qquad\text{that is}\qquad
\nu_t^{\prime\,2}=\nu_{\Phi}^{2}+\nu_m^{2}.
$$

That relation is the content of this article. The three wave numbers form a right triangle whose hypotenuse is $\nu_t^{\prime}$, the triangle is the energy–momentum triangle, and each of the three answers a different question about the same particle.

Why wave numbers rather than wavelengths. A derivative carries an inverse length, so it multiplies by a wave number and divides by a wavelength. A biquaternionic gradient acts on a plane wave as left multiplication by $2\pi i\tilde\Upsilon_{\Phi}$, the mass term of the operator is a wave number, and the exponent of the field is the scalar part $2\pi\,\mathrm{Sc}(\tilde\Upsilon_{\Phi}\tilde R_{\Phi}^{\natural})$. In wavelengths every one of those statements has to be inverted before it can be written. The reciprocal length is the form in which the equations are already stated, which is why it is the form with names here.

Conservation is a sum, and that settles it. Energies and momenta add, so the coefficients add, and the element adds:

$$
\tilde\Upsilon_{\Phi}=\sum_i\tilde\Upsilon_{\Phi,i},
\qquad
\nu_t^{\prime}=\sum_i \nu_{t,i}^{\prime},
\qquad
\vec\nu_{\Phi}=\sum_i\vec\nu_{\Phi,i},
$$

for the parts of a state and for the products of a collision. One sum replaces three, because the three coefficients travel in one element. Wavelengths do not add: the wavelength of a sum is the reciprocal of a sum of reciprocals. A conservation law written in wavelengths is a statement about harmonics, and a conservation law written in wave numbers is a statement about addition. That is the whole reason a quantum field is discussed in wave numbers.

The three questions. The mass wave number answers *how close can the particle be brought to a point*. It is the wave number at which the rest energy is the energy of the probe, so it is where a one-particle description stops being possible and where the force the particle carries runs out. The momentum wave number answers *how fast does the state wind*. It is the modulus of the vector part of $\tilde\Upsilon_{\Phi}$, the number of waves per unit distance, so it fixes the spacing of interference fringes, the width of the narrowest state of that momentum, and the circumference of a bound orbit in radians. The energy wave number answers *how fast does the clock run*. It is the temporal coefficient of the same element, so it fixes the rate of every phase and the reach of any process that borrows a given energy.

What is new here and what is not. The definitions, the triangle and the values are bookkeeping. The physical readings are the subject: the rest of the article takes each of the three in turn, and states what it measures, where it enters as a threshold, and which equation of the series carries it. The article closes with the non-relativistic limit, which is not a fourth reading but the one operation the triangle admits: split off the mass side exactly, expand in the ratio of the other two, and keep the leading term.

The article is named for the three wave numbers together because no one of them is enough. The mass wave number alone is the only one the particle carries at rest; the Dirac article of the series writes the coefficient of a mass term and the temporal entry of a parameter as two wave numbers side by side, and a reader who has one of the three without the others cannot tell which of the two is which.

## Naming the Coordinates

**Nothing is defined twice.** The deduction gave each number one source and no other. The temporal coefficient of $\tilde\Upsilon_{\Phi}$ is the temporal coefficient of $\tilde P_{\Phi}$ divided by $h$; the vector part of $\tilde\Upsilon_{\Phi}$ is the vector part of $\tilde P_{\Phi}$ divided by $h$; the mass wave number is the norm of $\tilde\Upsilon_{\Phi}$. There is no second rule for the energy, and none is needed: $E/c$ is already a coordinate of the momentum, so $\frac{E}{h\,c}$ is the corresponding coordinate of the quotient, obtained by the same division. An energy over $c$ is a momentum, and that is the whole of the step that is easy to miss.

The dimensions. All three are inverse lengths, and the check is one line:

$$
[\nu_m]=[\nu_{\Phi}]=[\nu_t^{\prime}]
=\frac{\mathsf{M}\mathsf{L}\mathsf{T}^{-1}}{\mathsf{M}\mathsf{L}^2\mathsf{T}^{-1}}=\mathsf{L}^{-1},
$$

since a momentum carries $\mathsf{M}\mathsf{L}\mathsf{T}^{-1}$ and $h$ carries $\mathsf{M}\mathsf{L}^2\mathsf{T}^{-1}$, the unit of an action.

Why $h$ and not $\frac{h}{2\pi}$. The series uses the spectroscopic wave number throughout, the number of wavelengths per unit length. The angular wave number is $2\pi\nu_{\Phi}$, and the ordinary de Broglie wavelength is $1/\nu_{\Phi}$; the factor $2\pi$ is the whole difference. It is the angular form that enters the exponents, the derivatives and the operator coefficients, so it is written out only where those appear. A text that quotes $h/p$ gives a wavelength, and its inverse is a wave number of this series without further ado. A spectrometer quotes the same form, $1/\lambda=\nu_{\Phi}$, in $\mathrm{cm^{-1}}$.

The division by $h$ is what leaves the count of waves. That is what the missing $2\pi$ means, and it is why the readings below are phrased per turn rather than per radian: a phase advances by a full turn over a distance $1/\nu_{\Phi}$, and by one radian over $1/(2\pi\nu_{\Phi})$. Every comparison with a measured fringe spacing, a spectrometer reading or a quoted wavelength carries the $2\pi$ back.

Which is which. Three labels, and no bare symbol. Two of the labels name the slot the coefficient fills in $\tilde\Upsilon_{\Phi}$: the sector letter $\Phi$ on the vector part, $\vec\nu_{\Phi}$, and the primed $t$ on the temporal one, $\nu_t^{\prime}$. The third names the norm, $\nu_m$ from the mass. The sector letter is written rather than the letter of the quantity because the momentum already writes its components $p_{\imath}$, and $\nu_p$ beside $p_{\imath}$ would be one transposition apart in running text. The prime on the temporal coefficient is the mark the corpus puts on a temporal slot, as on $p_{t}^{\prime}$ and $r'_t$, and it is kept because the division by $h\,c$ converts a quantity and not a coordinate.

The particle enters through its mass. A wave number is never labelled by the name of a particle. The species enters as a subscript on the mass itself, $\nu_{m_e}$ for the electron and $\nu_{m_p}$ for the proton, so that the family reads as one scheme: the subscript names the input, and the input of one species is the mass of that species.

One is invariant and two are not. $\nu_m$ is built from three constants, so no boost and no change of state touches it. $\nu_{\Phi}$ and $\nu_t^{\prime}$ are built from the momentum and the energy of the state, so both move when the particle is accelerated. A statement about $\nu_m$ is a statement about the species; a statement about $\nu_{\Phi}$ or $\nu_t^{\prime}$ is a statement about one preparation of one particle.

## The Wave-Number Biquaternion

**The momentum, written as one element.** The four-momentum of a particle of mass $m$ is the mass times the four-velocity, $\tilde P_{\Phi}=m\tilde V_{\Phi}$, and in coefficients

$$
\tilde P_{\Phi}=i\,p_{t}^{\prime}\,e_{t}+\vec p_{\Phi}=i\,\frac{E}{c}\,e_{t}+\gamma m\,\vec v,
\qquad
p_{t}^{\prime}=\frac{E}{c},
\qquad
\vec p_{\Phi}=\gamma m\,\vec v .
$$

Its norm is the mass shell, $\langle\tilde P_{\Phi}\rangle_{\natural}=\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}=-m^{2}c^{2}$, and it is the object the Dirac, Klein–Gordon and Maxwell articles of the series carry.

The quotient, in the coefficient the series carries. The same division written with the coefficient of this corpus, since $\frac{1}{h}$ is one over an action:

$$
\tilde\Upsilon_{\Phi}=\frac{\tilde P_{\Phi}}{h}
=\frac{1}{h}\tilde P_{\Phi}
=i\,\nu_t^{\prime}\,e_{t}+\vec\nu_{\Phi}.
$$

The division is legitimate term by term, and the reason is one line: $h$ is real and central, so it passes unchanged through the coefficient bar, the quaternion involution and the star, and it therefore moves no element out of its subspace. The momentum is anti-Hermitian, $\tilde P_{\Phi}^{*}=-\tilde P_{\Phi}$; multiplying by the real central $\frac{1}{h}$ preserves that, so $\tilde\Upsilon_{\Phi}^{*}=-\tilde\Upsilon_{\Phi}$ and $\tilde\Upsilon_{\Phi}\in\mathbb{B}_{\Phi}$.

The check of the equality. Two routes must agree, and they do. Divide the norm of the momentum:

$$
\frac{\langle\tilde P_{\Phi}\rangle_{\natural}}{h^{2}}
=\frac{-m^{2}c^{2}}{h^{2}}
=-\left(\nu_m\right)^{2}
=-\nu_m^{2},
$$

and expand the norm of the wave-number element in its own coefficients, using $e_{t}^{2}=e_{t}$ and $\vec\nu_{\Phi}\vec\nu_{\Phi}^{\natural}=\nu_{\Phi}^{2}$:

$$
\tilde\Upsilon_{\Phi}\tilde\Upsilon_{\Phi}^{\natural}
=\left(i\nu_t^{\prime}\right)^{2}e_{t}+\vec\nu_{\Phi}\vec\nu_{\Phi}^{\natural}
=-\nu_t^{\prime\,2}+\nu_{\Phi}^{2}.
$$

The two routes are the same number because $\tilde\Upsilon_{\Phi}=\frac{\tilde P_{\Phi}}{h}$ and $h$ is fixed by the bar, so

$$
-\nu_t^{\prime\,2}+\nu_{\Phi}^{2}=-\nu_m^{2},
\qquad\text{that is}\qquad
\nu_t^{\prime\,2}=\nu_{\Phi}^{2}+\nu_m^{2}.
$$

The first line is the norm of one element and the second is the mass shell divided by $h^{2}c^{2}$; the two are one statement, and the equality is what the rest of the article reads.

The arithmetic, once. For the electron at $1.6022\times10^{-13}\ \mathrm{J}$ the three numbers of §*The Values* are $\nu_t^{\prime}=8.0655\times10^{11}$, $\nu_{\Phi}=6.9330\times10^{11}$ and $\nu_m=4.1215\times10^{11}\ \mathrm{m^{-1}}$, and in $\mathrm{m^{-2}}$

$$
-\nu_t^{\prime\,2}+\nu_{\Phi}^{2}=-6.505\times10^{23}+4.807\times10^{23}=-1.699\times10^{23}=-\nu_m^{2},
$$

which is the box, and it is the only numerical check the identity needs.

What the element is good for. Three lines, each a place where the three wave numbers enter at once.

- On the plane wave $\tilde{Ξ}=\tilde{Ξ}_{0}\exp\bigl(-i\theta_{\mathrm{pwp}})$ the exponent is $2\pi\,\mathrm{Sc}(\tilde\Upsilon_{\Phi}\tilde R_{\Phi}^{\natural})=2\pi\left(\vec\nu_{\Phi}\cdot\vec r_{\Phi}-\nu_t^{\prime}\,r'_t\right)$, the phase in inverse lengths and in no other unit.
- The gradient acts by left multiplication by $2\pi i\tilde\Upsilon_{\Phi}$, $\tilde\nabla_\Phi\tilde{Ξ}=2\pi i\tilde\Upsilon_{\Phi}\tilde{Ξ}$, and the d'Alembertian by $-4\pi^{2}\tilde\Upsilon_{\Phi}\tilde\Upsilon_{\Phi}^{\natural}$, $\Box_\Phi\tilde{Ξ}=-4\pi^{2}\tilde\Upsilon_{\Phi}\tilde\Upsilon_{\Phi}^{\natural}\tilde{Ξ}=4\pi^{2}\nu_m^{2}\tilde{Ξ}$, which is why the massive operator of the series is written $\Box_\Phi-4\pi^{2}\nu_m^{2}$.
- On the null cone, where $\nu_m=0$ and $\nu_t^{\prime}=\nu_{\Phi}$, the element is null and therefore a zero divisor, and the equation $\tilde\Upsilon_{\Phi}\tilde{Ξ}_{0}=0$ has a two-dimensional kernel there. That is the massless case of §*The Massless Case*, and it exists because the norm has vanished, not because a limit was taken.

The angle is $\theta_{\mathrm{pwp}}=\frac{2\pi p\cdot x}{h}=2\pi\left(\vec\nu_{\Phi}\cdot\vec r_{\Phi}-\nu_t^{\prime}r'_t\right)$: a real four-momentum paired with a real position over $h$, so the angle is real.

The two objects differ by a division. $\tilde P_{\Phi}$ is the momentum, in the dimension of a momentum; $\tilde\Upsilon_{\Phi}$ is the same element in inverse lengths. Every statement in one is a statement in the other after multiplication by $h$, and both are kept because the dynamics is written in the first and the derivative returns the second.

## What a Wave Number Is

The wave number is $\nu=k/2\pi=1/\lambda$, the number of wavelengths per unit length, the spectroscopic wave number; the angular form $k=2\pi\nu$ enters phases and derivatives, and is written only where those appear.

It is the gradient of the phase. Write a plane wave as $e^{-i\theta_{\mathrm{pwp}}}$. The spatial entry is the gradient of the phase, $\vec\nu_{\Phi}=(1/2\pi)\vec\nabla_\Phi\phi$, and the temporal entry is the rate of the phase divided by the speed of light, $\nu_t^{\prime}=-(1/2\pi c)\,\partial\phi/\partial t$. The two are the same derivative read in space and in time, which is why the single element $\tilde\Upsilon_{\Phi}=i\nu_t^{\prime}e_t+\vec\nu_{\Phi}$ carries both and why neither entry needs a constant inside the equation.

It counts wavelengths per unit length. The phase turns by a full turn over a distance $1/\nu_{\Phi}$ and by one radian over $1/(2\pi\nu_{\Phi})$. So a wave number is a count of waves per unit length, and the angular wave number, the count of radians per metre, is $2\pi\nu_{\Phi}$. The same counting gives the nodes: consecutive nodal surfaces are $1/(2\nu_{\Phi})$ apart, so $2\nu_{\Phi}$ of them fit in a metre, and a wave of wave number $\nu_{\Phi}$ crossing a chamber of length $L$ puts $2\nu_{\Phi}L$ nodes in it.

It is a momentum measured in quanta of action. Since $\vec p_{\Phi}=h\,\vec\nu_{\Phi}$ and $E=h\,c\,\nu_t^{\prime}$, a wave number is the momentum, or the energy, with the unit of action divided out. The information is the same and the arithmetic is easier: a sum of momenta becomes a sum of inverse lengths, and no conversion stands between the derivative and its eigenvalue. That is what makes the wave number the natural variable of a quantum field, and the energy the natural variable of a classical one.

It is what a derivative returns. The spatial gradient carries an inverse length, so on a plane wave it multiplies by $2\pi i\vec\nu_{\Phi}$; the biquaternionic gradient multiplies by $2\pi i\tilde\Upsilon_{\Phi}$; the d'Alembertian multiplies by $-4\pi^{2}\tilde\Upsilon_{\Phi}\tilde\Upsilon_{\Phi}^{\natural}=4\pi^{2}\left(\nu_t^{\prime\,2}-\vec\nu_{\Phi}^{\,2}\right)$, which is $\nu_m^{2}$ on shell. A wave number is the eigenvalue of an operator that differentiates, and every coefficient in the field equations of this series is one. A mass term $2\pi\nu_m$ in the two first-order equations, $\tilde\nabla_\Phi\tilde{Ξ}_{R}=2\pi\nu_m\tilde{Ξ}_{L}$ and $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=2\pi\nu_m\tilde{Ξ}_{R}$, is the statement that the operator carries the wave number of the particle at rest, and nothing else.

Its inverse, up to the factor $2\pi$, is a distance, and each of the three distances is a different fact. A wave number and the distance per radian say the same thing in two ways: the wave number says how many waves fit in a metre, and the distance says how many metres a radian takes. The inversion is the whole of the translation, and it is worth stating because the two readings are used in different places — the wave number in the equations, the distance in the laboratory. The three of this article invert to three distances, and each distance has a reading of its own: a scale of resolution, a spacing of fringes, and a length that light travels in a time.

| wave number | what it counts | the distance per radian | what that distance is |
|---|---|---|---|
| $\nu_m=\frac{m\,c}{h}$ | waves of the rest-frame phase per metre | $3.86\times10^{-13}\ \mathrm{m}$ for the electron | the distance over which the phase of a particle at rest turns one radian; the order of length at which relativistic effects begin; the shortest distance at which it is still one particle; the range of the force it carries |
| $\nu_{\Phi}=\frac{p}{h}$ | waves of the spatial phase per metre | $5.29\times10^{-11}\ \mathrm{m}$ for the hydrogen ground state | the distance over which the phase of the state turns one radian; the unit of the fringe spacing; the coherence scale of the state |
| $\nu_t^{\prime}=\frac{E}{h\,c}$ | waves of the temporal phase per metre of light travel | $1.97\times10^{-13}\ \mathrm{m}$ for a $1.6022\times10^{-13}\ \mathrm{J}$ electron | the distance light covers while the phase turns one radian; the length a duration becomes; the decay length of an unstable particle |

**The three distances are in the inverse ratio of the wave numbers.** Since $\nu_t^{\prime}\ge \nu_{\Phi}$ and $\nu_t^{\prime}\ge \nu_m$, the energy distance is the shortest of the three at every speed, with equality at rest for the momentum one and in the massless limit for the mass one. And $\nu_{\Phi}/\nu_t^{\prime}=\beta$ reads as $\lambda_{\Phi}/\lambda_{t}=1/\beta$: the phase distance of the state is the light-travel distance divided by the speed, which is the statement that a slow particle winds slowly in space and quickly in time.

**The mass sets the scale and the speed sets the ratio.** Divide any one length by the mass length, and the mass leaves the quotient:

$$
\frac{\lambda_{\Phi}}{\lambda_m}=\frac{1}{\gamma\beta},
\qquad
\frac{\lambda_t}{\lambda_m}=\frac{1}{\gamma},
\qquad
\frac{\lambda_{\Phi}}{\lambda_t}=\frac{1}{\beta}.
$$

The last is the ratio above, read on lengths. The first two say that at a fixed speed every length of the particle scales as $1/m$: double the mass and all three lengths halve. So the reading "the heavier the particle, the shorter its wavelength" is one fact about $1/m$ stated three times, and it holds of the mass length and the energy length as much as of the de Broglie one. The objection is that a heavier particle is also harder to accelerate, so that the comparison of two species at one speed is a comparison of two different preparations. It is, and that is why the ratios are taken at fixed $\beta$: they carry no mass at all, so they cannot be disturbed by one.

The three lengths therefore have two different owners. The mass fixes the row of numbers — the scale $1/\nu_m$ of the species, and the scale $1/m$ of every other length of that species at a given speed. The state fixes the column — the position in the row, which is the ratio $\gamma\beta$. A statement about the first is a statement about the species and is true at every speed; a statement about the second is a statement about one preparation.

## The Relation Between the Three

The mass shell. For a free particle,

$$
E^2 = \vec p_{\Phi}^{\,2}c^2 + m^2c^4,
$$

with $E$ the total energy, the rest energy included, and $\vec p_{\Phi}$ the three-momentum.

Divide by $h^{2}c^{2}$. Every term is an energy squared, so every term becomes a squared momentum and then a squared wave number:

$$
\frac{E^2}{h^{2}c^{2}}=\frac{\vec p_{\Phi}^{\,2}c^{2}}{h^{2}c^{2}}+\frac{m^{2}c^{4}}{h^{2}c^{2}},
\qquad\text{that is}\qquad
\nu_t^{\prime\,2}=\nu_{\Phi}^{2}+\nu_m^{2}.
$$

**The same line is the norm of $\tilde\Upsilon_{\Phi}$.** The division is the one of §*The Wave-Number Biquaternion*, read coefficient by coefficient: the temporal term gives $-\nu_t^{\prime\,2}$, the spatial term $+\vec\nu_{\Phi}^{\,2}$, the mass term $-\nu_m^{2}$, and their sum is the norm. So

$$
\boxed{\;\tilde\Upsilon_{\Phi}\tilde\Upsilon_{\Phi}^{\natural}=-\nu_t^{\prime\,2}+\vec\nu_{\Phi}^{\,2}=-\nu_m^{2}\;}
$$

That box is the whole geometry of the three wave numbers, and it is the mass shell itself in other units. It is the Pythagorean relation of the three, so the triangle it describes is right angled at the mass side.

The triangle. The hypotenuse is $\nu_t^{\prime}$ and the legs are $\nu_{\Phi}$ and $\nu_m$. The energy wave number is therefore the largest of the three, and it is fixed by the other two through the root of the sum of squares:

$$
\nu_t^{\prime} = \sqrt{\nu_{\Phi}^{2}+\nu_m^{2}} .
$$

The ratios are the kinematic parameters. With the Lorentz factor $\gamma=E/(mc^2)$ and the speed $\beta=pc/E$,

$$
\frac{\nu_t^{\prime}}{\nu_m}=\gamma,
\qquad
\frac{\nu_{\Phi}}{\nu_t^{\prime}}=\beta,
\qquad
\frac{\nu_{\Phi}}{\nu_m}=\gamma\beta .
$$

The triangle is the energy–momentum triangle, whose side ratios are the kinematic parameters: the angle opposite the mass side has $\cos\theta=\beta$ and $\sin\theta=1/\gamma$.

The two limits. At rest, $p=0$ and $\nu_{\Phi}=0$, so the hypotenuse coincides with the mass side: $\nu_t^{\prime}=\nu_m$ and the momentum wave number vanishes. Ultra-relativistic, the mass side becomes negligible beside the other two, so $\nu_t^{\prime}\to \nu_{\Phi}$, and the mass wave number stays where it was. The approach is $\nu_{\Phi}=\gamma\beta \nu_m\approx\gamma \nu_m$ for $\beta\to1$. The mass wave number is the fixed side of the triangle and the other two turn about it.

Which of the two moving wave numbers is larger depends on the speed. Their ratio is $\nu_{\Phi}/\nu_m=\gamma\beta$. They are equal at $\beta=1/\sqrt{2}$, the momentum wave number is the larger above that speed and the smaller below it. At the speeds of ordinary matter the momentum wave number is enormously the smaller, and at the energies of a collider it is comparable with the energy wave number and far above the mass one.

The same relation, read on the four-momentum. The element carries the whole statement once, and the two norms are one line apart. The norm of the momentum is $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}=-m^{2}c^{2}$; since $\tilde P_{\Phi}=h\,\tilde\Upsilon_{\Phi}$ and $h$ is fixed by the bar, its norm is $h^{2}\tilde\Upsilon_{\Phi}\tilde\Upsilon_{\Phi}^{\natural}$, so the two lines are the same statement divided by $h^{2}$:

$$
\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}=-m^{2}c^{2}
\qquad\Longleftrightarrow\qquad
\tilde\Upsilon_{\Phi}\tilde\Upsilon_{\Phi}^{\natural}=-\nu_t^{\prime\,2}+\vec\nu_{\Phi}^{\,2}=-\nu_m^{2}.
$$

The second is the box with the sign of the Minkowski form, and the division by $h$ is the whole of the dictionary between the two objects: it is the same division that turns the momentum $p$ into the wave number $\nu_{\Phi}$ and the energy $E$ into $\nu_t^{\prime}$.

## The Values

The conversion is the one constant that turns an energy into a wave number, $h\\,c=1.986\\,446\\times10^{-25}\\ \\mathrm{J\\,m}$: a wave number in $\\mathrm{m^{-1}}$ is the corresponding quantity in $\\mathrm{J}$ divided by $1.986\\,446\\times10^{-25}$, that quantity being $mc^2$ for $\\nu_m$, $pc$ for $\\nu_{\\Phi}$ and $E$ for $\\nu_t^{\\prime}$. The particle masses are the CODATA 2018 values; $\\frac{h}{2\\pi}$ and $c$ are exact, and have been since the 2019 redefinition of the SI, so every uncertainty in the tables below comes from a mass.

At rest. The energy wave number equals the mass wave number, and the momentum wave number vanishes.

| particle | $mc^2$ | $\nu_m$ | $1/(2\pi\nu_m)$ |
|---|---|---|---|
| electron | $8.1871\times10^{-14}\ \mathrm{J}$ | $4.1215\times10^{11}\ \mathrm{m^{-1}}$ | $3.86159\times10^{-13}\ \mathrm{m}$ |
| muon | $1.6928\times10^{-11}\ \mathrm{J}$ | $8.5218\times10^{13}\ \mathrm{m^{-1}}$ | $1.8676\times10^{-15}\ \mathrm{m}$ |
| charged pion | $2.2362\times10^{-11}\ \mathrm{J}$ | $1.1258\times10^{14}\ \mathrm{m^{-1}}$ | $1.4138\times10^{-15}\ \mathrm{m}$ |
| proton | $1.5033\times10^{-10}\ \mathrm{J}$ | $7.5675\times10^{14}\ \mathrm{m^{-1}}$ | $2.103\times10^{-16}\ \mathrm{m}$ |
| top quark | $2.7668\times10^{-8}\ \mathrm{J}$ | $1.3928\times10^{17}\ \mathrm{m^{-1}}$ | $1.1427\times10^{-18}\ \mathrm{m}$ |

The electron in motion. The mass wave number is the same in every row and the other two move.

| $E$ | $\beta$ | $\nu_t^{\prime}$ | $\nu_{\Phi}$ | $\nu_m$ |
|---|---|---|---|---|
| $8.187\times10^{-14}\ \mathrm{J}$ | $0$ | $4.1215\times10^{11}$ | $0$ | $4.1215\times10^{11}$ |
| $1.6022\times10^{-13}\ \mathrm{J}$ | $0.860$ | $8.0655\times10^{11}$ | $6.9330\times10^{11}$ | $4.1215\times10^{11}$ |
| $1.6022\times10^{-11}\ \mathrm{J}$ | $0.99999$ | $8.0655\times10^{13}$ | $8.0655\times10^{13}$ | $4.1215\times10^{11}$ |
| $1.6022\times10^{-10}\ \mathrm{J}$ | $1.000$ | $8.0655\times10^{14}$ | $8.0655\times10^{14}$ | $4.1215\times10^{11}$ |

The unit of the last three columns is $\mathrm{m^{-1}}$.

A check of the relation. At $1.6022\times10^{-13}\ \mathrm{J}$ the three numbers satisfy the box, and the check is arithmetic in $\mathrm{m^{-2}}$:

$$
(8.0655\times10^{11})^{2} = 6.505\times10^{23},
\qquad
(6.9330\times10^{11})^{2}+(4.1215\times10^{11})^{2} = 4.807\times10^{23}+1.699\times10^{23} = 6.505\times10^{23}.
$$

A photon. For $m=0$ the mass wave number vanishes and the other two coincide. At $1.6022\times10^{-19}\ \mathrm{J}$ both are $8.0655\times10^{5}\ \mathrm{m^{-1}}$, the wave number of that photon; the angular wave number is $5.0677\times10^{6}\ \mathrm{m^{-1}}$, the same number multiplied by $2\pi$, that is $8.0655\times10^{5}\ \mathrm{m^{-1}}$, and the wavelength is $1.239842\times10^{-6}\ \mathrm{m}$.

What the tables say. The electron's mass wave number is $4.1215\times10^{11}\ \mathrm{m^{-1}}$, one wavelength per $2.426\times10^{-12}\ \mathrm{m}$, that is one radian of phase per $3.86\times10^{-13}\ \mathrm{m}$. The wave numbers are in direct proportion to the masses, so the ordering of the mass wave numbers is the ordering of the masses, and that is the whole content of the definition.

## Where Each Form Is Used

The rule of the series is that a coefficient of a differential operator is an inverse length, because every derivative carries one. All three wave numbers therefore appear as coefficients, and the mass one appears most often.

| site in the series | form written | which wave number |
|---|---|---|
| the Dirac chiral pair | $\nu_m$ | the mass |
| the Klein–Gordon operator | $\Box_\Phi-4\pi^{2}\nu_m^{2}$ | the mass |
| the shift of the Cauchy theory | $\kappa=-2\pi i\nu_m$ | the mass |
| the temporal entry of the harmonic parameter | $\nu_t^{\prime}$ | the energy |
| the spatial entry of the same parameter | $\nu_m$ | the mass |
| the modulus of that parameter | $\nu_{\Phi}$ | the momentum |
| the non-relativistic criterion | $\nu_{\Phi}\ll \nu_m$ | the momentum |
| the range of a Yukawa potential | $1/(2\pi\nu_m)$ | the mass |
| the Zitterbewegung amplitude | $1/(4\pi\nu_m)$ | the mass |
| the ordinary Compton wavelength | $1/\nu_m$ | the mass |
| interference and diffraction | $\nu_{\Phi}$ | the momentum |
| the temporal phase of a plane wave | $\nu_t^{\prime}$ | the energy |
| the plane-wave exponent | $2\pi\,\mathrm{Sc}(\tilde\Upsilon_{\Phi}\tilde R_{\Phi}^{\natural})$ | the three together |

The identity behind the middle rows. The harmonic parameter of *The Dirac Equation in Biquaternionic Form* is

$$
\alpha = -\left(i\,\nu_t^{\prime}\,\vec e_x + \nu_m\,\vec e_y\right),
$$

and its square is central because the two units anticommute, so that

$$
\alpha^2 = \left(\nu_t^{\prime\,2} - \nu_m^{2}\right)e_t = \nu_{\Phi}^{2}\,e_t .
$$

The parameter's square is the squared wave number of the state, and by the box its modulus is the momentum wave number. That is the box of this article read inside the operator, and it is why the two entries are wave numbers of different kinds rather than one number written twice: the temporal entry is the whole hypotenuse and the spatial entry is one leg, so the difference of their squares is the remaining leg.

**The operator and the parameter are the same object.** The massive d'Alembertian is $\Box_\Phi-4\pi^{2}\nu_m^{2}$ and the harmonic parameter is a wave element whose temporal entry is $\nu_t^{\prime}$ and whose spatial entry is $\nu_m$. Both are inverse lengths, both could be written as the same display, and neither needs a conversion inside the equation. That is the practical gain of the wave-number notation: the coefficient of the operator, the entry of the parameter and the component of the four-vector are one number.

## The Mass Wave Number

### What It Measures

**It is the wave number of the rest frame.** Set $p=0$. Then $\nu_{\Phi}=0$, $\nu_t^{\prime}=\nu_m$, and the triangle collapses onto the mass side. Every interpretation of $\nu_m$ is therefore an interpretation in the rest frame, and the number travels with the particle unchanged, which is why it can be quoted as a property of the species.

It is a wave number and not a radius. It is the wave number of the field in its own rest frame, not the extent of the field in space. A particle whose $1/(2\pi\nu_m)$ is $3.86\times10^{-13}\ \mathrm{m}$ may have no measured size at all, and the two statements are compatible because a wave number is a rate of phase and a radius is a distribution of charge. §*It Is Not the Size of the Particle* collects the numbers that make the difference unmistakable.

It is the wave number at which the one-particle description ends. A probe must carry a wave number larger than $\nu_m$ to resolve the particle's own scale, and a probe of that wave number carries the rest energy, so it makes pairs instead of resolving. The next subsection derives that statement, and it is the reading that carries the rest.

The number itself says four things at once. It is the wave number of the field in its own rest frame; it is the mass measured in quanta of action, $\nu_m=\frac{m\,c}{h}$; it is the coefficient the mass term of every operator in the series carries; and it is the fixed side of the triangle, the one the state cannot move. The four are one number, and the sections below take them in that order.

### The Distance It Inverts To

One radian of the rest-frame phase. The field at rest oscillates as $e^{-2\pi i c\nu_m t}$, and the distance light covers in the time $t$ is $L=ct$, so the phase as a function of that distance is $-2\pi\nu_mL$. It turns by one radian over

$$
\frac{1}{2\pi\nu_m},
$$

which is $3.86159\times10^{-13}\ \mathrm{m}$ for the electron. The full turn is $2\pi$ times as long, $\lambda_m=1/\nu_m=h/(mc)=2.426\times10^{-12}\ \mathrm{m}$, and only the full turn is called the Compton wavelength. Every statement of this section is the first of those numbers read another way.

**One radian is the form the exponents use.** The phase of a plane wave is written as an angle, and an angle counts radians, so the length that enters every exponent is the turn divided by $2\pi$. No shorter length is given a letter of its own: the rule is in *Physics Units and Common Elements Conventions*, §*No reduced length, no reduced constant*.

It is the shortest distance at which the particle is still one particle. The derivation of §*The Cost of Localization* is the statement: a region of size $1/(2\pi\nu_m)$ has a wave number spread $\nu_m$, an energy spread $m\,c^{2}=mc^{2}$, and the energy to make a second particle of the same mass. Below that distance the state that would be described is not a one-particle state, so $1/(2\pi\nu_m)$ is the resolution limit of the description and not the radius of an object.

It is the order of length at which relativistic effects cannot be ignored. A particle localized to $1/(2\pi\nu_m)$ has, by the uncertainty relation, a momentum spread of order $h\,\nu_m=mc$, so its kinetic energy is of order its rest energy and the non-relativistic description fails there. The distance is therefore the boundary of the Schrödinger theory: far above $1/(2\pi\nu_m)$ the non-relativistic equation is accurate, at $1/(2\pi\nu_m)$ it must give way to the Dirac or Klein–Gordon equation, and below it pair creation ends the one-particle description. That is the reading of the criterion $\nu_{\Phi}\ll \nu_m$ of §*The Non-Relativistic Criterion*, and it is the sense in which $1/(2\pi\nu_m)$ is quoted as the length at which a particle becomes relativistic: $3.86\times10^{-13}\ \mathrm{m}$ for the electron, $2.1\times10^{-16}\ \mathrm{m}$ for the proton, $1.1\times10^{-18}\ \mathrm{m}$ for the top quark.

It is the range of the force the particle carries. The Yukawa potential is $e^{-2\pi\nu_m r}/r$, so the distance $1/(2\pi\nu_m)$ is where the exponential has fallen by $1/e$, and beyond it the force is gone. A force carried by a massless particle has $\nu_m=0$ and no range at all, which is the same statement as the divergence of $1/(2\pi\nu_m)$.

It is the distance a mass term measures. The coefficient $\nu_m$ in $\Box_\Phi-4\pi^{2}\nu_m^{2}$ fixes the distance at which the Green function stops falling as $1/r$ and starts falling exponentially. The operator coefficient and the range of the force are one distance, and in wave numbers the coefficient and the range are the same symbol read two ways.

**It is not a size.** The two comparisons point in opposite directions and that is the argument. For the electron the distance is $3.86\times10^{-13}\ \mathrm{m}$, while the particle is pointlike below $10^{-18}\ \mathrm{m}$: the distance exceeds every bound on the radius by five orders of magnitude. For the proton the distance is $2.1\times10^{-16}\ \mathrm{m}$, while the charge radius is $8.4\times10^{-16}\ \mathrm{m}$: the distance falls short of the radius by a factor of four. A number that is sometimes far too large and sometimes too small is not a radius, and §*It Is Not the Size of the Particle* collects the comparisons.

### The Cost of Localization

Confine the particle and the wave numbers rise. A region of size $L$ admits a momentum spread of order $\frac{h}{2\pi L}$, that is a wave number spread of order $\frac{1}{2\pi L}$, and a momentum $p$ costs an energy $pc$ at least. The two together give an energy spread of order $\frac{h\,c}{2\pi L}$, so the energy grows as the region shrinks and the wave number grows as the region shrinks.

At $L=\frac{1}{2\pi\nu_m}$ the spread is the rest energy:

$$
\delta \nu_{\Phi} \sim  \nu_m,
\qquad
\delta E \sim m\,c^{2}= mc^2 .
$$

The energy available in the region has reached the energy needed to make a second particle of the same mass. Beyond that point the description with a fixed number of particles fails, not because the calculation is difficult, but because the state that would be described has the energy to become a different state.

The crossing, said three ways. It is the point where the Compton wave number is resolved, the point where a probe photon carries the rest energy, and the point where the pair threshold is reached. The three are one number. For the electron the probe photon is $8.187\times10^{-14}\ \mathrm{J}$, which is a hard gamma ray, and the corresponding length is $3.86\times10^{-13}\ \mathrm{m}$, which is why no microscope resolves a free electron's own scale: the photon that would resolve it would create pairs instead.

The same statement for any mass. Since $\nu_m$ is proportional to $m$, the crossing is at a higher energy and a higher wave number for a heavier particle. A proton needs $1.503\times10^{-10}\ \mathrm{J}$ and $\nu_m=7.57\times10^{14}\ \mathrm{m^{-1}}$; a top quark needs $2.772\times10^{-8}\ \mathrm{J}$ and $1.395\times10^{17}\ \mathrm{m^{-1}}$. The rest energy per unit of mass wave number is $mc^2/\nu_m=h\,c$, a constant, which is why the ladder of the last section has one slope for every species.

### The Rest-Frame Clock

The field at rest still oscillates. A field of mass $m$ at rest has a time dependence $e^{-i\theta_{\mathrm{pwt}}}$ with

$$
\omega_C=2\pi c\,\nu_m .

$$

The angle is $\theta_{\mathrm{pwt}}$, a real frequency times a real interval, $\omega r'_t/c$ for a length and $\omega r'_t$ for a time, so the angle is real.

For the electron this is $7.763\times10^{20}\ \mathrm{rad\,s^{-1}}$, that is $1.236\times10^{20}\ \mathrm{Hz}$. The number is not a curiosity: it is the rest energy divided by $h$, and it is the rate at which the phase of the field turns in the frame where the particle is at rest.

The period is a light-travel distance. One full turn of that phase takes $T_C=2\pi/\omega_C=h/(mc^2)$, and light covers $cT_C=1/\nu_m$ in that time. So the rest-frame clock and the mass wave number are one fact: the wave number is the angle turned per unit distance, and the clock is that angle divided by $c$.

The two are measured by different means. The mass wave number is measured by scattering, in the Compton shift and in the falling cross-section; the rest-frame frequency is measured by interference between a particle and its antiparticle, in the oscillation of a neutral meson. Both return $mc^2$, and neither needs a particle at rest in the laboratory: the frequency is read as an energy difference and the wave number as a momentum transfer.

### The Zitterbewegung Amplitude

The Dirac position trembles. In the Dirac theory the velocity operator has eigenvalues $\pm c$, and the position has, besides a mean motion, an oscillating part. Its amplitude is of order

$$
\frac{1}{4\pi\nu_m} ,
$$

which is $1.93080\times10^{-13}\ \mathrm{m}$ for the electron. The oscillating part is the interference between the positive- and negative-frequency pieces of the state, which is why it exists in the Dirac theory and not in a one-component theory.

The product of amplitude and frequency is $c$. The angular frequency of the trembling is $2\omega_C=4\pi c\,\nu_m$, twice the rest-frame rate, and the amplitude times that frequency is

$$
\frac{1}{4\pi\nu_m} \times 4\pi c\,\nu_m = c .
$$

The trembling point moves at the speed of light, at the only speed a massless piece of the state can move. The identity is exact, and it is why the amplitude and the frequency cannot be chosen separately: one wave number fixes both, and they are its inverse and its multiple.

**It is not the size of the particle.** The trembling is a motion, not an extent, and a point particle can tremble. What the amplitude measures is the distance the light-like components of the state travel during one half-period of their interference, and it is the mass wave number inverted, up to the factor $4\pi$.

### The Range of a Force

**A virtual particle cannot travel farther than the inverse of its mass wave number.** Exchange a particle of mass $m$ between two sources. The exchanged quantum is off shell by at least $mc^2$, so it can live for a time of order $\frac{h}{2\pi m\,c^{2}}$, and the distance it covers in that time is $\frac{1}{2\pi\nu_m}=1/(2\pi\nu_m)$. The potential that results falls as

$$
V(r) \propto \dfrac{e^{-2\pi\nu_m r}}{r},
$$

which is the Coulomb potential for $2\pi\nu_mr\ll1$ and exponentially small for $2\pi\nu_mr\gg1$. The range of the force is the inverse mass wave number of the particle that carries it, and nothing else.

The measured ranges.

| carrier | $mc^2$ | $\nu_m$ | $1/(2\pi\nu_m)$ | force |
|---|---|---|---|---|
| photon | $<1.602\times10^{-46}\ \mathrm{J}$ | $<5\times10^{-21}\ \mathrm{m^{-1}}$ | $>2\times10^{20}\ \mathrm{m}$ | electromagnetism |
| pion | $2.2361\times10^{-11}\ \mathrm{J}$ | $1.1258\times10^{14}\ \mathrm{m^{-1}}$ | $1.4138\times10^{-15}\ \mathrm{m}$ | the nuclear force |
| $W$ | $1.2878\times10^{-8}\ \mathrm{J}$ | $6.483\times10^{16}\ \mathrm{m^{-1}}$ | $2.455\times10^{-18}\ \mathrm{m}$ | the weak charged current |
| $Z$ | $1.4610\times10^{-8}\ \mathrm{J}$ | $7.355\times10^{16}\ \mathrm{m^{-1}}$ | $2.164\times10^{-18}\ \mathrm{m}$ | the weak neutral current |

The ordering of the force ranges is the ordering of the mass wave numbers, read backwards. The electromagnetic force is long ranged because the wave number of its carrier is zero; the weak force is the shortest because its carriers have the largest wave numbers among the known gauge bosons; the nuclear force sits between them because the pion is light on the scale of the weak bosons. In every case the number that decides is $\nu_m$, and no other number enters.

The same statement in the operator. The massive d'Alembertian of the series carries the coefficient $\nu_m^{2}$, and its Green function is the Yukawa kernel. *The Biquaternion D'Alembertian and Its Green's Functions* derives it there, and the coefficient is the only place the mass enters. The range of the force and the coefficient of the operator are one wave number written twice.

The Coulomb limit. As $m\to0$ the exponential becomes a constant and the potential becomes $1/r$. The photon-mass bound in the table is the experimental statement that $\nu_m$ for the photon is below $5\times10^{-21}\ \mathrm{m^{-1}}$, so the Coulomb potential is the massless limit to within a bound far below any measurement of it.

### The Field That Pays for a Pair

A strong enough field creates pairs. A constant electric field does work $eEL$ on a charge over a distance $L$. If that work reaches the rest energy over one inverse mass wave number, the field can separate a pair from the vacuum:

$$
eE_c\,\frac{1}{2\pi\nu_m} = mc^2,
\qquad\text{that is}\qquad
E_c = \frac{2\pi h\,c\,\nu_m^{2}}{e},
$$

using $mc^2=m\,c^{2}$. For the electron the number is $1.323\times10^{18}\ \mathrm{V\,m^{-1}}$, the Schwinger field. The reading is direct: the rest energy, divided by the charge and multiplied by the mass wave number, is the field that supplies it over one wave number. In wave numbers the formula is a square and a constant, and no length appears.

The same number as a voltage. Divide by $e$ and the statement becomes a potential difference: the rest energy per unit charge is $511\ \mathrm{kV}$, delivered over $3.86\times10^{-13}\ \mathrm{m}$. Both numbers are the same pair again, energy and wave number, and the mass wave number is what fixes the second.

Why the wave number is the invariant statement. The critical field depends on the charge as well as on the mass, so it is not a property of the particle alone; $\nu_m$ is. The Schwinger field is the mass wave number read through the coupling, and it is quoted in volts per metre only because a laboratory field is measured that way.

### The Compton Shift

**The shift is the mass wave number measured with a spectrometer.** A photon of wavelength $\lambda$ scattered by a particle of mass $m$ emerges with a shift

$$
\delta\lambda = \lambda_C\,(1-\cos\theta),
\qquad
\lambda_C = \dfrac{h}{mc} = \dfrac{1}{\nu_m} .
$$

For the electron $\lambda_C=2.426\times10^{-12}\ \mathrm{m}$, and the maximum shift, at backward scattering, is $2\lambda_C=4.85\times10^{-12}\ \mathrm{m}$.

The factor $2\pi$ is not decoration. A spectrometer measures the ordinary wavelength, so the Compton formula is quoted with $\lambda_C=1/\nu_m$ and not with $1/(2\pi\nu_m)$; the angular wave number enters the theory and the ordinary wavelength enters the instrument. The two differ by exactly the $2\pi$ that separates $\frac{h}{2\pi}$ from $h$ in the definition.

When the effect is visible. The shift is a fixed length, so it matters only when the incident wavelength is comparable to it. At $1\times10^{-12}\ \mathrm{m}$ the shift is a few tenths of the wavelength; at $5.00\times10^{-7}\ \mathrm{m}$ it is $10^{-5}$ of it and unobservable. That is why the Compton effect is a hard-X-ray and gamma-ray phenomenon and why visible-light scattering is Thomson scattering: the mass wave number marks the crossover, and the crossover is the usual one of a ratio of order one.

The cross-section falls at the same wave number. Below $\lambda_C$ the Klein–Nishina cross-section drops with energy, and the drop is the same statement as the pair threshold: the photon has enough energy to do more than shake the charge, and the elastic channel closes. The mass wave number marks both.

### The Atomic Comparison

A hydrogen atom is $21.8$ mass wavelengths across. The Bohr radius is $a_0=\frac{\epsilon_{0}\,h\,c}{\pi\,e^{2}\,\nu_{m_e}}$ and the mass wave number of the electron is $\nu_{m_e}=\frac{m_e\,c}{h}$. Their product needs no numerical input:

$$
a_0\,\nu_{m_e} =\frac{h\,c\,\epsilon_{0}}{\pi e^{2}} = \frac{1}{2\pi\alpha} = 21.81,
$$

with the fine-structure constant $\alpha=e^2/(2\,h\,c\,\epsilon_{0})$. The agreement with the directly computed $5.29177\times10^{-11}\times4.1215\times10^{11}=21.81$ is the check.

**That ratio is the whole of the non-relativistic approximation.** The electron's speed in the ground state is $\alpha c$, so $\beta=\alpha$ and $\gamma-1\simeq\tfrac12\alpha^{2}$. Every relativistic correction to a hydrogen level is smaller than the level itself by a power of $\alpha$, and the power is set by $a_0\nu_{m_e}$.

The atom's own three wave numbers. In the ground state the momentum is $m_e\alpha c$, so the momentum wave number is

$$
\nu_{\Phi} =\frac{m_e\,c\,\alpha}{h} = \alpha\,\nu_{m_e} = \frac{1}{2\pi a_0} = 3.007\times10^{9}\ \mathrm{m^{-1}} .
$$

The total energy is the rest energy less the binding energy, so the energy wave number is the mass wave number reduced by the binding term $\nu_m\alpha^{2}/2$:

$$
\nu_{m_e} = 4.1215\times10^{11}\ \mathrm{m^{-1}},
\qquad
\nu_{\Phi} = 3.007\times10^{9}\ \mathrm{m^{-1}},
\qquad
\nu_t^{\prime} = 4.1214\times10^{11}\ \mathrm{m^{-1}},
$$

to five figures, the two differing only in the fifth because the binding energy is $2.7\times10^{-5}$ of the rest energy; and the ordering $\nu_m\simeq \nu_t^{\prime}\gg \nu_{\Phi}$ is the statement that the electron is slow. Only one ratio is large: $\nu_{m_e}/\nu_{\Phi}=\nu_t^{\prime}/\nu_{\Phi}=1/\beta\simeq1/\alpha$, so the momentum wave number is $1/(2\pi a_0)$ while the other two stay at the mass wave number.

The binding has a wave number of its own, and it is not one of the three. The energy that moves inside the atom is the binding energy, and $\frac{h\,c}{2.179\times10^{-18}\ \mathrm{J}}$ is the wavelength at the ionization threshold, that is $\nu_{\gamma}=1.097\times10^{7}\ \mathrm{m^{-1}}$. That number is not $\nu_t^{\prime}$ of the state, because $\nu_t^{\prime}$ is built from the total energy and the total energy carries the rest energy. It is the energy wave number of an energy difference, of the kind read in §*The Uncertainty in Time*, and it is two hundred and seventy times smaller than the momentum wave number of the ground state: the photon that ionizes hydrogen has a wave number far below the inverse radius of the atom it ionizes, which is why the photo-ionization cross-section is so small.

What the ratio buys. Because the ratio is the inverse fine-structure constant divided by $2\pi$, a relativistic correction is smaller than the non-relativistic energy by a factor $\alpha^{2}$. The binding energy itself is $\tfrac12\alpha^{2}m_ec^{2}=2.179\times10^{-18}\ \mathrm{J}$, and the corrections to it are of order $\alpha^{4}m_ec^{2}=2.24\times10^{-22}\ \mathrm{J}$, a relative size of $2\alpha^{2}=1.1\times10^{-4}$. The scale $\alpha^{2}m_ec^{2}=4.358\times10^{-18}\ \mathrm{J}$ is the binding scale and not the size of a correction; confusing the two overstates the corrections by the factor $1/\alpha^{2}=1.9\times10^{4}$. That the corrections sit four powers of $\alpha$ down follows from the same small parameter that makes $\nu_{\Phi}\ll \nu_m$, and it is why the Schrödinger equation with a Coulomb potential works as well as it does.

## The Momentum Wave Number

### It Belongs to the State

**It is the wave number of the preparation.** Two electrons of the same mass, one at $1.6022\times10^{-13}\ \mathrm{J}$ and one at $1.6022\times10^{-7}\ \mathrm{J}$, have the same $\nu_m$ and momentum wave numbers that differ by six orders of magnitude. Nothing about $\nu_{\Phi}$ can be tabulated for a species. It is quoted for a beam, a trap, a thermal ensemble or a bound orbit, and it changes when any of those changes.

It is the reciprocal of the momentum wavelength, exactly. A plane wave of momentum $\vec p_{\Phi}$ has the spatial phase $e^{i\theta_{\mathrm{spa}}}$, so its wave vector is the vector part of the element, $\vec\nu_{\Phi}=\frac{\vec p_{\Phi}}{h}$, and its magnitude is the momentum wave number:

$$
\nu_{\Phi} =\frac{p_{\Phi}}{h} .

$$

The angle is $\theta_{\mathrm{spa}}=2\pi\,\vec\nu_{\Phi}\cdot\vec r_{\Phi}$, the spatial part of the plane-wave phase: a real wave vector dotted with a real position, so the angle is real.

That is the definition, and it is the form in which the number enters every equation of the series: the spatial gradient $\vec\nabla_\Phi$ carries an inverse length, and on a plane wave it returns $2\pi i\vec\nu_{\Phi}$. The biquaternionic gradient $\tilde\nabla_\Phi$ does the same, and on a plane wave it returns $2\pi i$ times the four-wave-number.

### The Phase Winding

One radian per inverse wave number. Walk along the direction of motion. The phase turns by one radian for every distance $1/(2\pi\nu_{\Phi})$ travelled, and by a full turn for every $1/\nu_{\Phi}$. The angular wave number counts radians per unit length and the spectroscopic one counts wavelengths per unit length.

The state is a clock and a ruler at once. The temporal part of the same phase is fixed by the energy wave number, and the ratio of the two is the inverse of the speed: the phase advances one radian in space per $1/(2\pi\nu_{\Phi})$ and one radian in time per $1/(2\pi c\,\nu_t^{\prime})$, so the crests move at $c\,\nu_t^{\prime}/\nu_{\Phi}=c/\beta$. That superluminal number is the phase velocity, and §*The Energy Wave Number* reads it.

A change of momentum is a change of the winding. Multiply the momentum by two and the wave number doubles. There is no other content in the definition, which is why the momentum wave number is the easiest of the three to change and the hardest to mistake for a property of the particle.

### The Distance It Inverts To

One radian of the spatial phase. The distance over which the phase of the state turns by one radian is

$$
\frac{1}{2\pi\nu_{\Phi}}=\frac{h}{2\pi p_{\Phi}} ,
$$

the full turn being $2\pi$ times as long, $\lambda_{\Phi}=1/\nu_{\Phi}=h/p_{\Phi}$, the de Broglie wavelength. The quotient is one radian of the spatial phase, and it is the distance this section is about. It is not a property of the species but of the preparation: for the electron in the hydrogen ground state it is the Bohr radius, $5.29\times10^{-11}\ \mathrm{m}$; for a $1.6022\times10^{-17}\ \mathrm{J}$ electron it is $1.95\times10^{-11}\ \mathrm{m}$; for a thermal neutron it is $1.60\times10^{-11}\ \mathrm{m}$.

It is the unit of every interference spacing. The fringe spacing of two slits is

$$
\delta y = \frac{D}{d\,\nu_{\Phi}} ,
$$

so the spacing of the fringes is the distance per radian, magnified by the geometry of the apparatus, $2\pi D/d$. A measurement of a fringe spacing is a measurement of the distance per radian, and it is the only direct measurement of $1/(2\pi\nu_{\Phi})$ in the series.

**It is twice the narrowest width of a state.** The uncertainty relation gives $\delta x\ge1/(4\pi\delta \nu_{\Phi})$, so a state whose wave numbers are spread over $\delta \nu_{\Phi}$ cannot be narrower than half the corresponding distance. The distance is therefore a lower bound on an extent and not an extent: it says how far the phase must run to define the state, not how much space the particle occupies.

It is the ruler of a bound orbit. A closed orbit holds a whole number of turns of phase, $r=n/(2\pi\nu_{\Phi})$, so the distance $1/(2\pi\nu_{\Phi})$ is the step of the ladder of bound states. For hydrogen in the ground state the step is the orbit itself, and the quantization is the statement that the orbit is one step long.

It is the coherence length of an ensemble. A thermal ensemble has its wave numbers spread over $\nu_T=\frac{\sqrt{2\pi m k_BT}}{h}$, so the distance over which its phase stays defined is $1/(2\pi\nu_T)$: $6.85\times10^{-10}\ \mathrm{m}$ for the electron at $300\ \mathrm{K}$ and $1.60\times10^{-11}\ \mathrm{m}$ for the neutron. A gas is quantum when the interparticle spacing reaches that distance, and the criterion $n/\nu_T^{3}\sim1$ is the statement that the basis operators of size $1/(2\pi\nu_T)$ have filled the volume.

### Interference and Diffraction

Fringes are spaced by the inverse momentum wave number. Two slits a distance $d$ apart, a screen a distance $D$ away, a particle of momentum wave number $\nu_{\Phi}$. The path difference for a point at height $y$ is $yd/D$, so the phase difference is $2\pi\nu_{\Phi}yd/D$, and neighbouring maxima are separated by

$$
\delta y = \dfrac{D}{d\,\nu_{\Phi}},
$$

which is the ordinary formula $\lambda D/d$ with $\lambda=1/\nu_{\Phi}$. The wave number enters the phase with its $2\pi$ in front, and the wavelength enters the ruler on the screen.

A number. Electrons of $1.6022\times10^{-17}\ \mathrm{J}$ have $\nu_{\Phi}=8.154\times10^{9}\ \mathrm{m^{-1}}$, so with $d=1\times10^{-6}\ \mathrm{m}$ and $D=1\ \mathrm{m}$ the fringes are $1.2\times10^{-4}\ \mathrm{m}$ apart and plainly visible. The same electrons through a crystal, whose planes are $2\times10^{-10}\ \mathrm{m}$ apart, give diffraction angles of order $1/(2d\,\nu_{\Phi})=0.3\ \mathrm{rad}$: the crystal is the grating that matches the wave number.

Diffraction is the same statement. An aperture of width $w$ spreads the beam over an angle of order $1/(w\,\nu_{\Phi})$. The pattern is wide when the wave number is small compared with the inverse aperture, which is the wave regime, and narrow when it is large, which is the ray regime. The boundary between the two is a product of two lengths, one of them $1/(2\pi\nu_{\Phi})$ and the other the apparatus.

### The Diffraction Limit and the Electron Microscope

An aperture resolves nothing smaller than its own wavelength. A wave collected over an aperture of width $w$ is spread over an angle of order $1/(w\nu_{\Phi})$, so two points closer than about half a wavelength are not separated in the image:

$$
\Delta x\sim\frac{1}{2\nu_{\Phi}}=\frac{\lambda_{\Phi}}{2}.
$$

The factor of two is a convention — Abbe's — and the constant of order one beside it is Rayleigh's; the statement that matters is that the resolution is a wave number and not a size.

Visible light stops at about $2\times10^{-7}\ \mathrm{m}$ and a proton is $10^{-15}\ \mathrm{m}$ across, so the gap is eight orders of magnitude. The way past the barrier is a larger $\nu_{\Phi}$, and since $\nu_{\Phi}=p/h$ a fast light particle supplies one. The electron is the choice: its mass is small, so a modest accelerating voltage buys a large momentum without a large rest-energy budget.

The arithmetic, relativistically. An electron through a potential difference $V$ has $e\,V$ of kinetic energy, so $pc=\sqrt{(e\,V)^{2}+2\,e\,V\,m_ec^{2}}$, and one division by $h$ gives the wave number. At $100\ \mathrm{kV}$, $\lambda_{\Phi}=3.70\times10^{-12}\ \mathrm{m}$; at $200\ \mathrm{kV}$, $2.51\times10^{-12}\ \mathrm{m}$; at $300\ \mathrm{kV}$, $1.97\times10^{-12}\ \mathrm{m}$. Each is some hundred thousand times shorter than a visible photon, and the diffraction limit each sets is far below the spacing of atoms in a crystal.

**The limit met in practice is not the diffraction one.** A transmission electron microscope resolves $50$ to $1.00\times10^{-10}\ \mathrm{m}$, whereas $\lambda_{\Phi}/2$ at $300\ \mathrm{kV}$ is $1\times10^{-12}\ \mathrm{m}$: the instrument sits a factor of fifty to a hundred above its own diffraction limit. The gap is the aberration of the magnetic lenses, chiefly spherical and chromatic, together with the small aperture those aberrations force. So the electron microscope is the case where the wavelength stops being the obstacle: at these wave numbers the instrument is the limit and the wave is not. That is the opposite of the optical microscope, where the wavelength is the limit and the glass is nearly perfect.

The mass wave number plays no part in the argument and must not be put in its place. To resolve $1/(2\pi\nu_{m_e})=3.86\times10^{-13}\ \mathrm{m}$ a probe would need a wave number $\nu_{m_e}$, and a photon of that wave number carries $8.187\times10^{-14}\ \mathrm{J}$. That is the pair threshold: the photon that reaches the electron's own scale makes an electron-positron pair instead of resolving the electron. The resolution of an instrument is written in $\nu_{\Phi}$, and the boundary beyond which the one-particle description ends is written in $\nu_m$. They are different numbers and they answer different questions.

### No State Is Narrower Than Half Its Wavelength

The uncertainty relation in the wave numbers. Write $\delta p=h\,\delta \nu_{\Phi}$ and the relation $\delta x\,\delta p\ge\frac{h}{4\pi}$ becomes

$$
\delta x \ge \dfrac{1}{4\pi\,\delta\nu_{\Phi}} .
$$

A state of a given momentum cannot be squeezed below half the inverse of its spread in wave number. The width of the state and the wave number of its spread are reciprocals, up to a factor of two, and the factor is the only thing the inequality leaves free.

The corollary that matters. A particle confined to a region $L$ has a wave number spread of order $1/(2\pi L)$, because the confinement is what sets the spread. The two numbers are therefore tied, and the energy that confinement costs is $\frac{h^{2}\,\nu_{\Phi}^{2}}{2m}$, the kinetic energy of a momentum $h\,\nu_{\Phi}$. A trap of one inverse mass wave number is a trap at the edge of the quantum regime, and every statement about zero-point motion is a statement about that edge.

Why the wave number is not a size, again. The inequality makes $\nu_{\Phi}$ the reciprocal of a lower bound on the width of the state, not an extent of the particle. A cold atom of momentum wave number $10^{6}\ \mathrm{m^{-1}}$ is not a micrometre across; it is a micrometre of phase, and its own mass wave number is four orders of magnitude larger.

### Bound States as Standing Waves

An orbit holds a whole number of wavelengths. The de Broglie condition for a circular orbit of radius $r$ is that the circumference contain a whole number of ordinary wavelengths, $2\pi r=n\lambda=n/\nu_{\Phi}$, that is

$$
r = \dfrac{n}{2\pi\nu_{\Phi}} .
$$

In radians the statement is one line: the phase accumulated around the orbit is $4\pi^{2} r\,\nu_{\Phi}$, and it must be a multiple of $2\pi$. The ground state of hydrogen is the case $n=1$: the radius is the inverse of $2\pi\nu_{\Phi}$. And indeed the momentum in the ground state is $m_e\alpha c$, so $\nu_{\Phi}=\frac{m_e\alpha c}{h}=\frac{1}{2\pi a_0}$ identically.

That is why the Bohr condition is not an extra postulate. It is the statement that the phase closes on itself after one turn, which is the same requirement as the single-valuedness of the wavefunction. The quantization counts wave numbers around the orbit, and the count is an integer because a phase that does not close is not a function.

The same count for any potential. A bound state has $\oint\nu_{\Phi}\,dq=n+\tfrac12$ in the semiclassical limit, which is the statement that the orbit accumulates $n+\tfrac12$ full turns of phase, the half coming from the two turning points. The wave number is the integrand of the semiclassical theory and the integer is the number of turns.

### Matter Waves at the Crystal

Two numbers worth remembering. A $1.6022\times10^{-17}\ \mathrm{J}$ electron has $\nu_{\Phi}=8.154\times10^{9}\ \mathrm{m^{-1}}$ and an ordinary wavelength of $1.23\times10^{-10}\ \mathrm{m}$. A neutron at $300\ \mathrm{K}$ has the thermal wave number $\nu_T=\frac{\sqrt{2\pi m k_BT}}{h}$, giving $\nu_{\Phi}=9.963\times10^{9}\ \mathrm{m^{-1}}$ and an ordinary wavelength of $1.00\times10^{-10}\ \mathrm{m}$.

The crystal spacing matches them. Atomic planes are of order $2\times10^{-10}\ \mathrm{m}$ apart, the same decade as both wavelengths, so a crystal diffracts both electrons and neutrons. The Bragg condition in this notation is $2d\sin\theta=n\lambda=n/\nu_{\Phi}$, which is the textbook form read with $\lambda=1/\nu_{\Phi}$.

Why neutrons and not protons. A proton at $300\ \mathrm{K}$ has a thermal wave number larger than the neutron's only by the square root of the mass ratio, which is not enough to matter; what decides the choice is that the neutron is neutral and penetrates the crystal, while the proton is stopped in the first layer. The wave numbers are comparable; the interactions are not.

### The Thermal Wave Number

Temperature supplies a momentum. A thermal ensemble has $p_T=\sqrt{2\pi mk_BT}$, so

$$
\nu_T =\frac{\sqrt{2\pi m k_BT}}{h} .
$$

For the electron at $300\ \mathrm{K}$ this is $2.324\times10^{8}\ \mathrm{m^{-1}}$, with an ordinary wavelength of $4.30\times10^{-9}\ \mathrm{m}$; for the neutron, $9.963\times10^{9}\ \mathrm{m^{-1}}$ and $1.00\times10^{-10}\ \mathrm{m}$.

**The degeneracy criterion is a count of basis operators per particle.** A gas is quantum when the volume per particle is comparable to the cube of the inverse wave number:

$$
\dfrac{n}{\nu_T^{3}} \sim 1 .
$$

For the electron at $300\ \mathrm{K}$ the criterion is reached at $n=1.3\times10^{25}\ \mathrm{m^{-3}}$; a metal has $8.5\times10^{28}\ \mathrm{m^{-3}}$ in its conduction band, so $n/\nu_T^{3}=6.8\times10^{3}$ and the electron gas is degenerate. That is why a metal is described by a Fermi sea and not by a classical gas, and the number that decides it is the thermal wave number.

The same count for a gas of atoms. Cool a gas until its wave number grows to the inverse interparticle spacing and the atoms lose their identity as distinguishable objects; the condensate appears at that point. The criterion is the same one, with the mass of the atom in place of the mass of the electron, and it is met at nanokelvin temperatures because the atom is heavy.

### It Grows with Speed

The wave number is proportional to the momentum. Since $p=\gamma mv$,

$$
\nu_{\Phi} =\gamma\,\frac{v}{c}\,\nu_m = \gamma\beta\,\nu_m .
$$

At rest it vanishes; at $\beta=1/\sqrt{2}$ it equals the mass wave number; at $\beta\to1$ it approaches $\gamma \nu_m$ and grows without bound as the energy rises. The momentum and energy wave numbers can both be made arbitrarily large by raising the energy; only the mass wave number is fixed. At $1.6022\times10^{-7}\ \mathrm{J}$ an electron's momentum wave number is $8.07\times10^{17}\ \mathrm{m^{-1}}$, and its energy wave number is the same number.

That is the resolution of a collider. Two beams collide with a wave number far above the inverse size of a proton, and the collisions resolve structure at that wave number. The statement that a collider probes a given distance is a statement about $\nu_{\Phi}$, not about any particle's size.

In the length it is one line. Invert the relation and divide by the mass length:

$$
\frac{\lambda_{\Phi}}{\lambda_m}=\frac{1}{\gamma\beta},
$$

so the de Broglie length is the mass length divided by $\gamma\beta$. The electron gives the ladder: $2.414\times10^{-11}\ \mathrm{m}$ at $\beta=0.1$, $4.202\times10^{-12}\ \mathrm{m}$ at $\beta=0.5$, and $2.426\times10^{-12}\ \mathrm{m}$ at $\beta=1/\sqrt{2}$, where the two lengths are equal. Above that speed the de Broglie length is the shorter of the two, and below it the longer. A proton at $\beta=0.5$ carries $2.289\times10^{-15}\ \mathrm{m}$, shorter than the electron's by the mass ratio $1836$.

The limit at rest is the one worth stating. As $\beta\to0$ the de Broglie length diverges while the mass length does not move: $2.426\times10^{-12}\ \mathrm{m}$ for the electron at every speed. A particle at rest has no de Broglie wavelength at all and a finite Compton wavelength, and the two statements are about two different lengths. The reading that a massive particle has a short wavelength comes from confusing them.

### Not a Size Either

A cold atom. $\nu_{\Phi}=1.6\times10^{5}\ \mathrm{m^{-1}}$ for an atom at microkelvin temperatures, and the atom is $1\times10^{-10}\ \mathrm{m}$ across, that is $10^{10}\ \mathrm{m^{-1}}$ of inverse size. The ratio is four orders of magnitude, in the direction opposite to the naive reading.

A macroscopic object. A grain of $1\times10^{-3}\ \mathrm{kg}$ moving at $1\times10^{-3}\ \mathrm{m\,s^{-1}}$ has $p=10^{-6}\ \mathrm{kg\,m\,s^{-1}}$ and $\nu_{\Phi}=1.51\times10^{27}\ \mathrm{m^{-1}}$, twenty orders of magnitude above the inverse size of the grain. No interference is observable, and the reason is not that the grain is large but that its wave number is large compared with every inverse aperture available.

**The grain shows the other length too.** Its mass wave number is $\nu_m=4.52\times10^{38}\ \mathrm{m^{-1}}$, so $\lambda_m=2.210\times10^{-39}\ \mathrm{m}$. That is $3.34\times10^{-12}$ of its own de Broglie length, and $1.37\times10^{-4}$ of the Planck length. For a macroscopic body the mass length is the shortest length in the description by eleven orders of magnitude, and it is the de Broglie length that matters for every observable: the two are separate numbers and only the second is set by the motion.

## The Energy Wave Number

### The Wave Number the Particle Would Have If It Were Massless

The cleanest reading of the third wave number. A photon of energy $E$ has momentum $E/c$, so its momentum wave number and its energy wave number are the same number:

$$
\nu_{\Phi} =\frac{E}{h\,c} = \nu_t^{\prime} .
$$

For a massive particle the two differ, and their ratio is the speed:

$$
\dfrac{\nu_{\Phi}}{\nu_t^{\prime}} = \beta .
$$

So $\nu_t^{\prime}$ is the wave number the particle would have if all of its energy were carried by a massless quantum. It is the photon-equivalent wave number, and the ratio $\beta$ measures how far the particle is from that ideal.

The two limits read themselves. At rest $\beta=0$ and $\nu_t^{\prime}$ is infinitely larger than $\nu_{\Phi}$, which has vanished: the particle has energy and no momentum, and no massless quantum imitates that. At $\beta\to1$ the two wave numbers merge, and the wave is indistinguishable from a light wave of the same energy. Every ultra-relativistic particle is photon-like in this precise sense, and the series uses that fact whenever it treats a fast fermion as a light-like field.

**It is the temporal coefficient of $\tilde\Upsilon_{\Phi}$.** The same number is the temporal entry of the wave-number biquaternion, and it is the ordinary frequency over $c$, the angular frequency with its $2\pi$ divided out:

$$
\nu_t^{\prime} = \dfrac{\omega}{2\pi c} = \dfrac{f}{c} .
$$

A wave whose spatial entry is $\vec\nu_{\Phi}$ and whose temporal entry is $\nu_t^{\prime}$ moves at $\beta=\nu_{\Phi}/\nu_t^{\prime}$, which is the same statement again. In the element there are no mixed units: both entries are inverse lengths, and both are coefficients of the same kind. The same number is $\tilde P_{\Phi}$ read in inverse lengths, and $\tilde\Upsilon_{\Phi}$ is that momentum divided by $h$, which is why the temporal entry can be written as an energy per unit of action or as a frequency over $c$ without a conversion inside the equation.

### The Clock

**One radian of phase per inverse energy wave number.** The phase of a plane wave is $2\pi\vec\nu_{\Phi}\cdot\vec x-\omega t$ with $\omega=2\pi c\,\nu_t^{\prime}$. Over a time $t=1/(2\pi c\,\nu_t^{\prime})$ the phase turns by $\omega t=1$. So the energy wave number is the rate at which the phase turns, divided by $c$, in the same way that the momentum wave number is the rate at which it turns in space.

The clock of any process. A reaction whose energy changes by $\delta E$ has a phase that turns at $\frac{2\pi\delta E}{h}=2\pi c\,\delta\nu_t^{\prime}$, and the inverse of that wave number is the distance light covers in the corresponding time. Every oscillation, every beat and every interference term in the series can be read as a wave number this way, and the reading is exact: the energy wave number of the difference is the wave number of the beat.

### The Distance It Inverts To

One radian of the temporal phase, measured in light travel. Since $\nu_t^{\prime}=\omega/(2\pi c)$, the phase of a plane wave read along the path of a light ray is $-2\pi\nu_t^{\prime} L$ with $L=ct$, so the phase turns by one radian over

$$
\frac{1}{2\pi\nu_t^{\prime}}=\frac{h\,c}{2\pi E} ,
$$

the full turn being $2\pi$ times as long, $\lambda_{t}=1/\nu_t^{\prime}=h\,c/E$, the wavelength of the temporal phase.

The distance is the one the energy becomes when a duration is converted into a length, and the conversion is the speed of light and nothing else. For an electron of $1.6022\times10^{-13}\ \mathrm{J}$ it is $1.97\times10^{-13}\ \mathrm{m}$; at rest it equals the mass distance, because the energy is the rest energy.

It is the length a time becomes. A process of duration $\tau$ has the wave number $1/(2\pi c\tau)$, and the distance light covers while it runs is $c\tau$, the reciprocal of $2\pi$ times that wave number. A lifetime and a length are therefore one measurement in two units, and the decay of §*The Decay Wave Number* is the case where the duration is the mean life.

It is the reach of a virtual process. A process that borrows an energy $\delta E$ can reach the distance $1/(2\pi\delta\nu_t^{\prime})=\frac{h\,c}{2\pi \delta E}$, which is the energy distance of the deficit. The Yukawa range is the special case in which the deficit is the rest energy, and there the energy distance and the mass distance coincide: $1/(2\pi\nu_m)=1/(2\pi\nu_t^{\prime})$ at rest.

It is the shortest of the three distances. Because $\nu_t^{\prime}$ is the hypotenuse of the triangle, $1/(2\pi\nu_t^{\prime})$ is the shortest side of the inverted triangle, with equality at rest against $1/(2\pi\nu_m)$ and in the massless limit against $1/(2\pi\nu_{\Phi})$. The energy distance is what a state can be resolved to at best, since it is the distance light covers in the phase time of its own energy.

**It is not an extent either.** The distance $1/(2\pi\nu_t^{\prime})$ is a scale of the phase and not the size of anything: at the Planck energy it is $1.6\times10^{-35}\ \mathrm{m}$, which is a statement about the definition of the Planck length and not about any object of that size.

### The Phase Velocity

The crests travel faster than the particle. The phase velocity of a matter wave is $v_{\mathrm{ph}}=\omega/(2\pi\lvert\vec\nu_{\Phi}\rvert)=c\,\nu_t^{\prime}/\nu_{\Phi}=c^{2}/v$. In one period $T=h/E$ the crests cover

$$
v_{\mathrm{ph}}T = \dfrac{c\,\nu_t^{\prime}}{\nu_{\Phi}}\dfrac{1}{c\,\nu_t^{\prime}} = \dfrac{1}{\nu_{\Phi}} ,
$$

while light covers $cT=1/\nu_t^{\prime}$. The two distances are in the ratio $\nu_t^{\prime}/\nu_{\Phi}=1/\beta$: the crests outrun light by the factor $1/\beta$, and the excess carries no signal because the envelope moves at $v$.

Why the two wave numbers are both needed. The crest spacing is the inverse momentum wave number and the light-travel distance per period is the inverse energy wave number. A notation with only one of the two could not state the phase velocity, which is why the series keeps both and why the harmonic parameter of the Dirac article carries one in each entry.

### The Uncertainty in Time

A borrowed energy lasts a time. The relation $\delta E\,\delta t\ge\frac{h}{4\pi}$ says that a process which borrows an energy $\delta E$ can last a time of order $\frac{h}{2\pi \delta E}$. Convert the time to a distance and the statement becomes: the process can reach a distance

$$
c\,\delta t \sim \dfrac{1}{2\pi\delta \nu_t^{\prime}} = \dfrac{h\,c}{2\pi\delta E},
$$

the inverse energy wave number of the borrowed energy.

The Yukawa range is the special case. A virtual particle of mass $m$ borrows $\delta E=mc^2$, so its reach is $\frac{1}{2\pi\nu_m}=1/(2\pi\nu_m)$, which is the range derived in §*The Range of a Force*. The two derivations are one derivation, and the energy wave number is the general form of the mass wave number's range statement: the reach of a virtual process is the inverse energy wave number of its deficit.

The reach of a virtual photon is not infinite. A virtual photon of energy $\delta E$ reaches $1/(2\pi\delta\nu_t^{\prime})$; only the exactly massless, exactly zero-energy exchange reaches arbitrarily far, and the Coulomb potential is the sum over all of them.

### The Decay Wave Number

A width is a wave number. An unstable particle of mean life $\tau$ has a width $\Gamma=\frac{h}{2\pi \tau}$. The energy wave number of the width is

$$
\nu_t^{\prime}(\Gamma) =\frac{\Gamma}{h\,c} = \dfrac{1}{2\pi c\tau},
$$

which is the inverse of the distance the particle travels before it decays. The same number is a wave number and an inverse flight path, and the equality is not a coincidence: both are an energy divided by $h\,c$.

Two numbers. The charged pion has $\tau=2.60\times10^{-8}\ \mathrm{s}$, so $c\tau=7.80\ \mathrm{m}$ and $\nu_t^{\prime}=0.0204\ \mathrm{m^{-1}}$: a pion at rest decays after seven metres of light travel, which is why a pion beam line is measured in metres. The $Z$ boson has $\Gamma=4.000\times10^{-10}\ \mathrm{J}$, so $\nu_t^{\prime}=1.265\times10^{16}\ \mathrm{m^{-1}}$: its decay distance is $7.91\times10^{-17}\ \mathrm{m}$, about a tenth of the proton charge radius, which is why it leaves no track.

The pair of statements is one measurement. A width read in an energy spectrum and a lifetime read in a beam line give the same wave number, and the conversion between them is the same $h\,c$ that converts every energy in this article into a wave number.

### It Is the Largest of the Three

**The hypotenuse is the longest side.** Since $\nu_t^{\prime}$ is the hypotenuse of the triangle, $\nu_t^{\prime}\ge \nu_{\Phi}$ and $\nu_t^{\prime}\ge \nu_m$, with equality at rest for the first and in the massless limit for the second. The energy wave number is the largest of the three at every speed.

It grows without bound. It tracks the total energy, and the total energy grows without limit as the particle is accelerated, so the energy wave number can be made as large as the energy allows. At the Planck energy, $1.955\times10^{9}\ \mathrm{J}$, it reaches $9.85\times10^{33}\ \mathrm{m^{-1}}$, whose inverse is the Planck length. That is not a coincidence either: the Planck length is defined as the inverse energy wave number of the Planck energy, so the statement is a tautology once the definition is read.

### It Is Not Independent

**Two wave numbers fix the third.** Given the mass wave number and the momentum wave number, the box gives the energy wave number; given the mass wave number and the energy wave number, the box gives the momentum wave number. No physical statement is added by naming it. What is added is a name for a quantity that already appears as a coefficient: the temporal entry of the harmonic parameter is $\nu_t^{\prime}$ and nothing else.

Why name it anyway. Because the same number appears in four unrelated places — the photon-equivalent wave number, the phase clock, the reach of a virtual deficit and the decay wave number — and a reader who meets $\frac{E}{h\,c}$ in one of them should recognize the others. The name is a convenience of the notation and not a new dynamical quantity, and this article is careful to say so.

## The Ladder

One column of energies, one column of wave numbers. The conversion $h\\,c=1.986\\,446\\times10^{-25}\\ \\mathrm{J\\,m}$ gives a wave number for every energy, and the same table read with $k_BT$ in place of $E$ gives a wave number for every temperature.

| energy | $\nu_t^{\prime}$ | temperature | $\nu_t^{\prime}$ |
|---|---|---|---|
| $1.6022\times10^{-22}\ \mathrm{J}$ | $8.066\times10^{2}\ \mathrm{m^{-1}}$ | $1\ \mathrm{K}$ | $69.49\ \mathrm{m^{-1}}$ |
| $1.6022\times10^{-19}\ \mathrm{J}$ | $8.066\times10^{5}\ \mathrm{m^{-1}}$ | $2.725\ \mathrm{K}$ | $189.4\ \mathrm{m^{-1}}$ |
| $1.6022\times10^{-16}\ \mathrm{J}$ | $8.066\times10^{8}\ \mathrm{m^{-1}}$ | $300\ \mathrm{K}$ | $2.085\times10^{4}\ \mathrm{m^{-1}}$ |
| $1.6022\times10^{-13}\ \mathrm{J}$ | $8.066\times10^{11}\ \mathrm{m^{-1}}$ | $10^{9}\ \mathrm{K}$ | $6.949\times10^{10}\ \mathrm{m^{-1}}$ |
| $1.6022\times10^{-10}\ \mathrm{J}$ | $8.066\times10^{14}\ \mathrm{m^{-1}}$ | | |
| $1.6022\times10^{-7}\ \mathrm{J}$ | $8.066\times10^{17}\ \mathrm{m^{-1}}$ | | |
| $1.955\times10^{9}\ \mathrm{J}$ | $9.847\times10^{33}\ \mathrm{m^{-1}}$ | | |

**Three columns are the same column.** The row for $1.6022\times10^{-19}\ \mathrm{J}$ is the row for $11605\ \mathrm{K}$ and the row for $1.78\times10^{-36}\ \mathrm{kg}$; the three quantities are related by exact constants, and a wave number is one way of writing any of them. The ladder is the conversion table of the whole series, and every order-of-magnitude statement in it can be read from this table alone.

A caution that the table invites. The ladder gives a wave number for every energy, and the wave number is a scale and not an extent. The $1.6022\times10^{-19}\ \mathrm{J}$ entry, $8.066\times10^{5}\ \mathrm{m^{-1}}$, is the wave number of a visible photon; it is not the inverse size of anything. The $1.6022\times10^{-13}\ \mathrm{J}$ entry, $8.066\times10^{11}\ \mathrm{m^{-1}}$, is the wave number of a gamma ray; it is not the inverse radius of a nucleus. Reading the table as a list of sizes is the mistake that §*It Is Not the Size of the Particle* refutes.

## The Non-Relativistic Criterion

The condition. Non-relativistic quantum mechanics applies when the wave number of the state is much smaller than the mass wave number:

$$
\nu_{\Phi} \ll \nu_m .
$$

The three ways of writing the same condition are $p\ll mc$, $\nu_{\Phi}\ll \nu_m$ and $\nu_t^{\prime}\simeq \nu_m$. The last is the easiest to apply, since $\nu_t^{\prime}=\gamma \nu_m$ and the criterion is $\gamma\simeq1$.

The hydrogen atom is the case in point. The ratio $a_0\nu_{m_e}=1/(2\pi\alpha)=21.81$ derived in §*The Atomic Comparison* is the criterion satisfied with room to spare, and the room is the inverse fine-structure constant divided by $2\pi$.

Light and heavy. At fixed $L$, a light particle has the smaller $\nu_m$ and reaches the relativistic regime first; a heavy particle stays non-relativistic in a smaller box. That is why the electron in a light atom is relativistic to a few parts in $10^{5}$ and the nucleons in the same atom are not.

## The Non-Relativistic Limit

The condition, read on the three numbers. Non-relativistic means that the excess of the energy wave number over the mass wave number is small, $\Omega:=\nu_t^{\prime}-\nu_m\ll \nu_m$, which is the same as $\nu_{\Phi}\ll \nu_m$. In that regime the mass wave number is a fixed constant, the momentum wave number is the dynamical variable, and the energy wave number is forced by the box of §*The Relation Between the Three*.

The element, truncated. The rule is one line: keep $\gamma$ to order $\beta^{2}$ in the temporal slot and replace it by $1$ in the vector slot,

$$
\tilde\Upsilon_{\Phi,1}=i\,\nu_m\left(1+\frac{\beta^{2}}{2}\right)e_{t}+\nu_m\vec\beta
=i\left(\nu_m+\Omega\right)e_{t}+\vec\nu_{\Phi},
\qquad
\Omega=\frac{\nu_m\beta^{2}}{2},
\qquad
\nu_{\Phi}=\nu_m\beta .
$$

The temporal slot keeps its first correction because that correction *is* the kinetic energy; the vector slot keeps its leading term because its first correction, $\frac{1}{2}\beta^{2}\nu_m\vec\beta$, is of order $\beta^{3}$: one order below the term the temporal slot keeps, and therefore below the order of the element.

The same rule on the box. Write $\nu_t^{\prime}=\nu_m+\Omega$ in $\nu_t^{\prime\,2}=\nu_{\Phi}^{2}+\nu_m^{2}$ and cancel the $\nu_m^{2}$:

$$
\nu_{\Phi}^{2}=2\nu_m\Omega+\Omega^{2}
\qquad\longrightarrow\qquad
\Omega=\frac{\nu_{\Phi}^{2}}{2\nu_m},
$$

the arrow being the statement $\Omega\ll \nu_m$: the quadratic term is a fraction $\Omega/2\nu_m=\frac{1}{4}\beta^{2}$ of the linear one and is dropped.

The relation then closes exactly. On the truncated element the two entries are $\Omega=\nu_m\beta^{2}/2$ and $\nu_{\Phi}=\nu_m\beta$, so

$$
\frac{\nu_{\Phi}^{2}}{2\nu_m}=\frac{\nu_m^{2}\beta^{2}}{2\nu_m}=\frac{\nu_m\beta^{2}}{2}=\Omega ,
\qquad\text{that is}\qquad
 h\,c\,\Omega=\frac{\left(h \nu_{\Phi}\right)^{2}}{2m}=\frac{1}{2}m\lvert\vec v\rvert^{2}.
$$

The last equality is the kinetic energy written in the three wave numbers, and it holds without remainder: the truncated element satisfies $E_{\mathrm{kin}}=p^{2}/2m$ and not merely $p^{2}/2m$ to leading order. That is what makes the truncation of the two slots at different orders the consistent one — any other split leaves a remainder in this equality.

The error, and its only parameter. The exact solution of the quadratic is $\Omega=-\nu_m+\sqrt{\nu_{\Phi}^{2}+\nu_m^{2}}$, which expands as

$$
\Omega=\frac{\nu_{\Phi}^{2}}{2\nu_m}\left(1-\frac{1}{4}\frac{\nu_{\Phi}^{2}}{\nu_m^{2}}+\cdots\right),
$$

so the truncated $\Omega$ is high by the fraction $\frac{1}{4}\nu_{\Phi}^{2}/\nu_m^{2}=\frac{1}{4}\beta^{2}$. At $\nu_{\Phi}/\nu_m=0.1$ the error is $0.25$ per cent and the limit is usable; at $\nu_{\Phi}/\nu_m=1$ the exact figure is $21$ per cent and the limit has ended. The single parameter of the whole section is $\nu_{\Phi}/\nu_m$.

The equation. The exponent of the rung separates exactly, because $\Omega$ is a definition and not a series:

$$
e^{-i\theta_{\mathrm{pwp}}}
=\underbrace{e^{-i\theta_{\mathrm{rst}}}}_{f}\,
\underbrace{e^{-i\theta_{\mathrm{pwp}}}}_{\chi},
$$

with $f$ the rest-frame clock of §*The Rest-Frame Clock*. On the envelope $\chi$ the exponent gives $\partial_{r'_t}\chi=-2\pi i\Omega\chi$, and $\Omega$ is quadratic in $\vec\nu_{\Phi}$, so the number $\nu_{\Phi}^{2}$ is the symbol of the operator $-\Delta_\Phi$:

$$
i\,\frac{\partial\chi}{\partial r'_t}=-\frac{1}{4\pi\nu_m}\,\Delta_\Phi\,\chi
\qquad\longrightarrow\qquad
i \frac{h}{2\pi}\,\frac{\partial\chi}{\partial t}=-\frac{hc}{8\pi^{2}\nu_m}\,\Delta_\Phi\,\chi ,
$$

the last step multiplying by $\frac{h}{2\pi} c$ with $r'_t=c\,t$ and $\frac{h\,c}{8\pi^{2}\nu_m}$ the coefficient of $\Delta_\Phi$. This is the free Schrödinger equation, and it is the limit of the three wave numbers: $\nu_m$ is the constant, $\nu_{\Phi}$ the variable, and the box has been turned into an operator by dropping one term.

The angle is $\theta_{\mathrm{rst}}=2\pi\nu_m r'_t$: the mass wave number and the real interval give a real angle.

**The mass length survives the limit.** It is not eliminated; it changes its dress. The coefficient of $\Delta_\Phi$ in the boxed equation is $1/(4\pi\nu_m)$, which is half of one radian of the mass length, and it is a length because $\Delta_\Phi$ carries an inverse length squared and the time derivative an inverse length. Pass to clock time, $r'_t=c\,t$, and the same coefficient becomes

$$
\frac{c}{4\pi\nu_m}=5.788\times10^{-5}\ \mathrm{m^{2}\,s^{-1}}
$$

for the electron: the coefficient of a diffusion equation, and the inertia the mass imposes on the Schrödinger equation. So the non-relativistic limit keeps one visible wavelength, $\lambda_{\Phi}$, and folds the other two into one constant. A reader who takes the limit for a deletion of the mass can test the point here, because the mass is still in the equation, in the only place a non-relativistic equation has for it.

## The Classical Limit in Wavelengths

Classicality is a statement about the state and not about the mass. A body behaves classically when the phase it winds across the apparatus is large, and the measure of that is the number of wavelengths that fit across it:

$$
N=L\,\nu_{\Phi}=\frac{L}{\lambda_{\Phi}} .
$$

The limit $N\gg1$ is classical and $N\lesssim1$ is wave. The criterion never mentions $\nu_m$, and the reason is that a heavy body and a light one at the same speed differ in scale alone.

The heavy body is classical because its length is short. A grain of $1\times10^{-3}\ \mathrm{kg}$ at $1\times10^{-3}\ \mathrm{m\,s^{-1}}$ has $\lambda_{\Phi}=6.626\times10^{-28}\ \mathrm{m}$, so a chamber of $1\ \mathrm{m}$ holds $1.51\times10^{27}$ wavelengths of it. No instrument holds fewer, and interference is impossible for that reason and not for any other. The mass length of the same grain, $2.210\times10^{-39}\ \mathrm{m}$, is shorter still and plays no part in the argument: the classical criterion is built on the length the state supplies.

**What $h\to0$ does depends on what is held fixed.** Hold the speed and let $h\to0$: the three lengths all go to zero in proportion, because each is $h$ over a momentum or an energy over $c$, and every ratio of §*What a Wave Number Is* is untouched. The triangle keeps its shape and loses its scale, and no length becomes large. Hold the wave number and let $h\to0$: the momentum $\vec p_{\Phi}=h\vec\nu_{\Phi}$ goes to zero, so the speed goes to zero and the particle comes to rest. The two readings are opposite, and *The Non-Quantum Limit of the Biquaternion Model* states both with the caution that the second is the one a fixed-wavelength statement of the limit actually makes.

The reason the triangle cannot supply a second parameter. It has one shape, fixed by $\beta$ through $\nu_{\Phi}/\nu_m=\gamma\beta$, and a right triangle has no second degree of freedom. So $h$ cannot appear in any internal ratio of the three lengths, and the classical limit cannot be a statement about those ratios. It can only be a statement about $h$ against a length the apparatus supplies, which is the ratio $N$ of the first display.

The objection, and the answer. A reader may say that the grain is classical because it is heavy, and that the criterion $N\gg1$ merely restates the fact in other units. It does not. Two grains of the same mass, one at rest and one at $1\times10^{-3}\ \mathrm{m\,s^{-1}}$, have the same $\nu_m$ and de Broglie lengths that differ by an infinity; only the moving one has a finite $N$ at all. If mass made a body classical, a cold atom of large mass would be as classical as a cannonball, and a Bose–Einstein condensate of $10^{5}$ heavy atoms shows interference over its whole extent. The mass fixes the scale; the state fixes the classicality.

## The Massless Case

The degenerate triangle. As $m\to0$ the mass side vanishes and the box loses that term:

$$
\nu_m\to0,
\qquad
\nu_t^{\prime} = \nu_{\Phi} .
$$

The triangle flattens: the hypotenuse falls on the momentum side. The energy wave number and the momentum wave number become one number, which is the wave number of the particle, and the mass wave number is no longer a wave number of the problem.

**No non-relativistic limit.** The criterion $\nu_{\Phi}\ll \nu_m$ reads $\nu_{\Phi}\ll0$ at $m=0$, which no finite wave number satisfies, so there is no non-relativistic regime for the massless particle to be the limit of. The relativistic description is not a high-energy regime of a non-relativistic one; it is the only description.

The rest-frame clock stops. $\omega_C=2\pi c\,\nu_m\to0$ as the mass wave number vanishes: the field of a massless particle has no rest-frame oscillation, because there is no frame in which it rests. The Compton period, the trembling and the rest-frame phase are lost together, and their loss is the flattening of the triangle.

In the series. The massless case is treated as exact and not as a limit. The Dirac chiral pair decouples at $m=0$ into the two one-sided equations $\tilde\nabla_\Phi\tilde{Ξ}_{R}=0$ and $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=0$, and *Conformal Invariance and the Massless Limit in Biquaternionic Form* treats the massless field on its own terms. The vanishing coefficient is what makes the decoupling exact.

The photon. The empirical bound on a photon mass is of order $2\times10^{-63}\ \mathrm{kg}$, which is the mass a photon would need for its Coulomb potential to acquire a range shorter than the observed one. With $\nu_m=m\,c/h$, that bound gives

$$
\nu_{m_\gamma} \lesssim \frac{1.8\times10^{-63}\times2.998\times10^{8}}{6.626\times10^{-34}}\ \mathrm{m^{-1}} \approx 8\times10^{-22}\ \mathrm{m^{-1}},
$$

whose inverse is of the order of a galactic scale. A smaller mass gives a smaller wave number, and the Coulomb potential is the massless limit of the Yukawa potential.

## It Is Not the Size of the Particle

The name invites a mistake, and the numbers refute it.

The proton. Its mass wave number is $\nu_m=7.568\times10^{14}\ \mathrm{m^{-1}}$. Its charge radius, measured by electron scattering and by hydrogen spectroscopy, is $r_p=8.414\times10^{-16}\ \mathrm{m}$. The product with $2\pi$ is four:

$$
2\pi\,r_p\,\nu_m = \frac{0.8414}{0.2103} = 4.001 .
$$

If the inverse mass wave number were the radius, the product would be one; it is four, and the radius is a strong-interaction scale while the mass wave number is a relativistic quantum one.

The electron. Its mass wave number is $4.1215\times10^{11}\ \mathrm{m^{-1}}$. No finite size has been observed: the experimental bounds on the electron radius lie below $10^{-18}\ \mathrm{m}$, that is above $10^{18}\ \mathrm{m^{-1}}$ in inverse size. A wave number of $4.1\times10^{11}\ \mathrm{m^{-1}}$ cannot be the inverse radius of an object that is pointlike more than six orders of magnitude below its inverse; the ratio of the two is $2.4\times10^{6}$.

**A size and a scale behave differently under a boost.** A size is a fixed extent and transforms by length contraction; $\nu_m$ does not move at all, and the other two transform as the components of a four-vector. Two quantities that transform differently cannot be the same quantity, and the observation needs no numbers: the definition of $\nu_m$ contains no state, so no boost can act on it.

A size and a scale behave differently under a probe. A size is measured by resolving it, and the probe must have a larger wave number than the inverse size. A scale is measured by finding where a description changes: the mass wave number where a cross-section falls or a pair appears, the momentum wave number where a fringe appears, the energy wave number where a clock beats. The first is a measurement of extent; the last three are measurements of thresholds.

The statement. Each of the three wave numbers is a scale at which a description changes, not an extent in space. The mass wave number is where the quantum and the relativistic descriptions meet, the momentum wave number is the rate at which the phase of the state winds, and the energy wave number is the rate of its clock. An article that calls any of them the size of the particle is wrong, and the comparisons above are the warrant.

## The Letter and the Subscript

Why a subscript at all. Four wave numbers share one letter: the mass one, the momentum one, the temporal one and the Euclidean one. A bare letter therefore names none of them, and every wave number of this article carries a subscript. The space index is $k$, in $\vec e_{\imath}$ and $\sum_{\imath\in\{x,y,z\}}$; it is not a wave number, and the migration that keeps the two apart is recorded in *Wavenumber Migration*.

Which subscripts. The labels come in two kinds, and neither names a particle. Two of them name a slot of $\tilde\Upsilon_{\Phi}$: the sector letter $\Phi$ on the vector part, $\vec\nu_{\Phi}$ and its modulus $\nu_{\Phi}$, and the primed $t$ on the temporal coefficient, $\nu_t^{\prime}$, which is the corpus's mark for a temporal slot and matches $p_{t}^{\prime}$ of the four-momentum and $r'_t$ of the four-position; the prime stays because the division by $h\,c$ converts a quantity and not a coordinate. The third names the norm of the element, $\nu_m$, and with it the species, $\nu_{m_e}$ and $\nu_{m_p}$. The letter of the momentum is not used: the momentum already writes its components $p_{\imath}$, and $\nu_p$ beside $p_{\imath}$ would be one transposition apart in running text. The sector letter is not open to that confusion, and it carries a fact the letter of the quantity would not — it says to which subspace the element belongs.

The species enters on the mass. A wave number of a named particle is written $\nu_{m_e}$ for the electron and $\nu_{m_p}$ for the proton, which is the rule of the series that the label names the input: the input of one species is the mass of that species. No wave number is ever labelled by the name of a particle alone.

**The wavelength is the inverse and never a second symbol.** The series keeps $\lambda$ wherever a length is what the sentence needs: the Compton shift, the range of a potential, the size of an atom. The wavelength of a wave number is its inverse and nothing else: $\lambda_m=1/\nu_m=h/(mc)$, $\lambda_{\Phi}=1/\nu_{\Phi}=h/p_{\Phi}$ and $\lambda_t=1/\nu_t^{\prime}=h\,c/E$. **There is no reduced wavelength.** The series defines no shorter length of that name, writes no barred letter for one, and carries no constant written with a bar: one radian of the phase is the wavelength over $2\pi$, written $\lambda_m/(2\pi)=1/(2\pi\nu_m)$ and its two companions, a quotient and not a symbol of its own. The rule is recorded in *Physics Units and Common Elements Conventions*, §*No reduced length, no reduced constant*. A display that wrote both a wave number and a wavelength for the same object, without the inversion between them, would be the duplication this notation exists to remove: the wave number is the form the equations take, and the wavelength is that number read as a distance.

Why not $\mu$. The letter $\mu$ names the permeability, the direction label and the index of a component, and it is not used for an inverse Compton length anywhere in the series.

One caution on the neighbourhood. The corpus writes $\nu_{\mathrm{eu}}$ for a Euclidean momentum after a Wick rotation, a number that is also an inverse length but belongs to a different construction. The two are told apart by the label: $\mathrm{eu}$ marks the continuation of a component to imaginary time, and its square is positive, $\nu_{\mathrm{eu}}^{2}\ge0$, whereas $\nu_t^{\prime}$ is a Lorentzian component and the box of this article carries a minus sign in the Minkowski form. No display mixes them.

## The Two Relations and the Three Numbers

Two of the three numbers were postulated and the third was measured, and the order of their arrival is worth stating because the presentation above delivers them together.

**The mass length came first, in 1923.** Compton found that an X-ray scattered through an angle $\theta$ emerges with its wavelength shifted by

$$
\Delta\lambda=\lambda_m\left(1-\cos\theta\right),
\qquad
\lambda_m=\frac{1}{\nu_m},
$$

so the electron's mass length, $2.426\times10^{-12}\ \mathrm{m}$, entered physics as a measured shift of a spectrum line, one year before any matter wave was proposed. The number in the formula is read off the same element this article divides by $h$: it is the norm of $\tilde\Upsilon_{\Phi}$.

**The two relations came in 1924.** De Broglie's thesis proposed that every particle carries a wave, and it did so through two equations. The first, $p=\frac{h}{\lambda}$, is $\lambda_{\Phi}=1/\nu_{\Phi}$ with the momentum of the state. The second, $hf_{\mathrm{frq}}=m\,c^{2}$, sets the rest energy of a particle as a frequency; divided by $c$ it is the rest-frame value of $\nu_t^{\prime}$, that is $\nu_m$. So the two relations give the momentum number and the mass number, and the third number is what the mass shell makes of them.

**The triangle is the two relations plus the mass shell, divided by $h$.** That is the whole of the deduction, and it follows that this article can claim no novelty in the arithmetic: the two relations are de Broglie's, the geometry is Minkowski's, and the division by $h$ is the change of unit. What the article adds is that the three are read off one element, $\tilde\Upsilon_{\Phi}$, and that the same division produces the coefficient of every operator of the series.

**The error the two relations separate.** Mass is energy, and energy is a frequency; from the two it does not follow that a massive particle has a short wavelength in space. The frequency the second relation fixes is the rest-frame phase, $c\,\nu_m$, whose wavelength is $\lambda_m$. The spatial wavelength of the state is $\lambda_{\Phi}$, and it is infinite at rest. A particle at rest has a finite Compton wavelength and no de Broglie wavelength at all. Both statements are true, they are about two different lengths, and the cost of running them together is the error this article exists to remove.

**What the history does not show.** It does not show that the three numbers were always kept apart. The $\frac{1}{2\pi}$ convention, the distinction between a wave number and its inverse, and the habit of writing the mass term of an operator as a coefficient all arrived later, through Schrödinger's equation and through the relativistic wave equations of 1926 to 1928, and the notation of this series is a later tidying rather than a reconstruction of the original. The reader who wants the framework's own history has *A Brief History of Biquaternions in Physics*; the paragraphs above are the history of the three numbers alone.

## Summary

Three wave numbers come from one division, $\tilde\Upsilon_{\Phi}=\frac{\tilde P_{\Phi}}{h}$: the quotient's temporal coefficient is $\nu_t^{\prime}=\frac{E}{h\,c}$, its vector part is $\vec\nu_{\Phi}=\frac{\vec p_{\Phi}}{h}$ with modulus $\nu_{\Phi}$, and its norm is $\nu_m=\frac{m\,c}{h}$. The first two belong to the state and the third to the particle, and all three are read off the one element $\tilde\Upsilon_{\Phi}=i\nu_t^{\prime}e_t+\vec\nu_{\Phi}$.

The mass shell, divided by $h^{2}$ term by term, gives the box $\nu_t^{\prime\,2}=\nu_{\Phi}^{2}+\nu_m^{2}$. The three are the sides of a right triangle with the energy wave number the largest and the mass wave number the fixed side. The ratios of the sides are the kinematic parameters: $\nu_t^{\prime}/\nu_m=\gamma$, $\nu_{\Phi}/\nu_t^{\prime}=\beta$ and $\nu_{\Phi}/\nu_m=\gamma\beta$.

The mass wave number is where localization costs the rest energy: at $1/(2\pi\nu_m)$ the wave number spread is $\nu_m$ and the energy spread is $mc^{2}$, so a second particle can be made and the one-particle description ends. It is the rest-frame clock, $\omega_C=2\pi c\,\nu_m$, which is $7.76\times10^{20}\ \mathrm{rad\,s^{-1}}$ for the electron. It is twice the trembling amplitude, and the amplitude times the trembling frequency is exactly $c$. It is the range of the force the particle carries, from $1.126\times10^{14}\ \mathrm{m^{-1}}$ for the pion to $7.36\times10^{16}\ \mathrm{m^{-1}}$ for the $Z$. It is the field that pays for a pair, $\frac{2\pi c^{3}\,m^{2}}{h\,e}=1.32\times10^{18}\ \mathrm{V\,m^{-1}}$ for the electron. It is the inverse of the Compton wavelength, and the wave number at which elastic scattering gives way. It is the scale the hydrogen atom is $21.8$ of, and that ratio is the inverse fine-structure constant over $2\pi$.

The momentum wave number is the rate at which the phase winds. It fixes the fringe spacing $D/(d\,\nu_{\Phi})$, and no state is narrower than half the inverse of its spread. It is the ruler of a bound state: the ground state of hydrogen is the one whose momentum wave number is the inverse Bohr radius, and the Bohr condition is the statement that the orbit accumulates a whole number of turns of phase. It is what a crystal diffracts, $8.15\times10^{9}\ \mathrm{m^{-1}}$ for a $1.6022\times10^{-17}\ \mathrm{J}$ electron and $9.96\times10^{9}\ \mathrm{m^{-1}}$ for a thermal neutron. It sets quantum degeneracy through $n/\nu_T^{3}\sim1$, met by a metal and not by a gas at room temperature. It grows with speed as $\gamma\beta \nu_m$, and it is the resolution of a collider.

The energy wave number is the temporal coefficient of $\tilde\Upsilon_{\Phi}$, and it is the wave number the particle would have if it were massless, with $\nu_{\Phi}/\nu_t^{\prime}=\beta$ the measure of how far it is from that. It is one radian per $1/(2\pi\nu_t^{\prime})$ of light travel. It is the inverse reach of a virtual deficit of energy, and the Yukawa range is the case of a deficit $mc^{2}$. It is the inverse decay length, $\frac{\Gamma}{h\,c}=1/(2\pi c\tau)$: $0.0204\ \mathrm{m^{-1}}$ for the pion and $1.265\times10^{16}\ \mathrm{m^{-1}}$ for the $Z$. It is the largest of the three, and at the Planck energy it is the inverse Planck length.

For the electron $\nu_m=4.1215\times10^{11}\ \mathrm{m^{-1}}$, and it is the same at every energy; at $1.6022\times10^{-13}\ \mathrm{J}$ the other two are $\nu_t^{\prime}=8.0655\times10^{11}\ \mathrm{m^{-1}}$ and $\nu_{\Phi}=6.9330\times10^{11}\ \mathrm{m^{-1}}$, at $1.6022\times10^{-11}\ \mathrm{J}$ both are $8.0655\times10^{13}\ \mathrm{m^{-1}}$, and at rest the energy wave number equals the mass wave number while the momentum wave number vanishes.

None of the three is the size of the particle: the proton's charge radius times $2\pi\nu_m$ is four, and the electron is pointlike far below its own inverse. At $m=0$ the triangle degenerates, $\nu_t^{\prime}=\nu_{\Phi}$ and the mass wave number is no longer a wave number of the problem. The massless equations of the series are exact for that reason, not approximate.

The non-relativistic limit is one operation on the triangle. Split off the mass side exactly, $\nu_t^{\prime}=\nu_m+\Omega$, note that the triangle then reads $\nu_{\Phi}^{2}=2\nu_m\Omega+\Omega^{2}$, expand once, and keep the term linear in the excess. The quotient of the two terms, $\digamma_{\mathrm{nr}}=\Omega/(2\nu_m)$, is the small parameter, and the error of the truncation is $-\digamma_{\mathrm{nr}}/(1+\digamma_{\mathrm{nr}})$ in closed form. The leading term is $h\,c\,\Omega=p^{2}/2m$, and the first-order relation it carries, with $\nu_{\Phi}^{2}\to-\Delta_\Phi$, is the free Schrödinger equation. The mass length is not deleted by the limit: the coefficient of $\Delta_\Phi$ is $1/(4\pi\nu_m)$, and in clock time it is $c/(4\pi\nu_m)=5.788\times10^{-5}\ \mathrm{m^{2}\,s^{-1}}$ for the electron.

**The scale is the mass and the ratio is the speed.** At a fixed $\beta$ every length of the particle scales as $1/m$, so "the heavier the particle, the shorter its wavelength" is one fact about the mass and is true of all three lengths. The ratios carry no mass: $\lambda_{\Phi}/\lambda_m=1/(\gamma\beta)$ and $\lambda_t/\lambda_m=1/\gamma$. The de Broglie length is infinite at rest while the mass length is not, and the two are different lengths that answer different questions.

The classical limit is a statement about the state and not about the mass. The criterion is $L\gg\lambda_{\Phi}$, the number of wavelengths across the apparatus, and it never mentions $\nu_m$. Lowering $h$ at fixed speed shrinks every length in proportion and leaves every ratio; lowering it at fixed wave number brings the particle to rest.

The history is two relations and one measurement. Compton's shift, $\Delta\lambda=\lambda_m(1-\cos\theta)$, put the mass length into physics in 1923; de Broglie's two relations of 1924 supplied $\lambda_{\Phi}=1/\nu_{\Phi}$ and the rest frequency $c\,\nu_m$; the mass shell divided by $h$ gives the triangle. The arithmetic is not new, and the article claims none.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\nu_m = \frac{m\,c}{h}$ | The mass wave number, the inverse Compton wavelength; $\mathsf{L}^{-1}$; the norm of $\tilde\Upsilon_{\Phi}$, and the only one of the three that belongs to the particle alone |
| $\vec\nu_{\Phi}=\frac{\vec p_{\Phi}}{h}$, $\nu_{\Phi} =\lvert\vec\nu_{\Phi}\rvert$ | The vector part of $\tilde\Upsilon_{\Phi}$ and its modulus, the momentum wave number, the wave number of the state; $\mathsf{L}^{-1}$; a property of the state |
| $\nu_t^{\prime} =\frac{E}{h\,c}$ | The temporal coefficient of $\tilde\Upsilon_{\Phi}$, the energy wave number; $\mathsf{L}^{-1}$; the largest of the three |
| $\lambda_m=1/\nu_m$, $\lambda_{\Phi}=1/\nu_{\Phi}$, $\lambda_t=1/\nu_t^{\prime}$ | The three wavelengths, the inverses of the three wave numbers; one radian of each is $\lambda/(2\pi)$, a quotient and not a symbol |
| $\frac{\lambda_{\Phi}}{\lambda_m}=\frac{1}{\gamma\beta}$, $\frac{\lambda_t}{\lambda_m}=\frac{1}{\gamma}$, $\frac{\lambda_{\Phi}}{\lambda_t}=\frac{1}{\beta}$ | The three lengths at a fixed speed; the mass sets the scale and the state sets the ratio, so no ratio carries a mass |
| $\nu_t^{\prime\,2}=\nu_{\Phi}^{2}+\nu_m^{2}$ | The mass shell in wave numbers; the right triangle of the three |
| $\frac{\nu_t^{\prime}}{\nu_m}=\gamma$, $\frac{\nu_{\Phi}}{\nu_t^{\prime}}=\beta$ | The side ratios, which are the kinematic parameters of the state |
| $\tilde\Upsilon_{\Phi}=\frac{\tilde P_{\Phi}}{h}=i\nu_t^{\prime}e_t+\vec\nu_{\Phi}$ | The wave-number biquaternion, the four-momentum in inverse lengths, an element of $\mathbb{B}_{\Phi}$; its norm is $\tilde\Upsilon_{\Phi}\tilde\Upsilon_{\Phi}^{\natural}=-\nu_t^{\prime\,2}+\vec\nu_{\Phi}^{\,2}=-\nu_m^{2}$; the gradient multiplies by $2\pi i\tilde\Upsilon_{\Phi}$ and the d'Alembertian by $-4\pi^{2}\tilde\Upsilon_{\Phi}\tilde\Upsilon_{\Phi}^{\natural}$ |
| $\omega_C=2\pi c\,\nu_m$ | The rest-frame angular frequency; one radian of phase per $1/(2\pi\nu_m)$ of light travel |
| $2\omega_C=4\pi c\,\nu_m$ | The trembling angular frequency; its amplitude $1/(4\pi\nu_m)$ times it is $c$ |
| $\lambda_C = \frac{1}{\nu_m}$ | The ordinary Compton wavelength, the shift in Compton scattering |
| $E_c =\frac{2\pi c^{3}\,m^{2}}{h\,e}$ | The pair-creation field, $1.32\times10^{18}\ \mathrm{V\,m^{-1}}$ for the electron |
| $a_0\,\nu_{m_e} = \frac{1}{2\pi\alpha}=21.81$ | The Bohr radius in wave numbers, and the inverse fine-structure constant over $2\pi$ |
| $\nu_T =\frac{\sqrt{2\pi m k_BT}}{h}$ | The thermal wave number, whose cube sets the degeneracy criterion $n/\nu_T^{3}\sim1$ |
| $\frac{h}{2\pi}\,c= 3.161\,527\times10^{-26}\ \mathrm{J\,m}$ | The conversion between an energy and a wave number |
| $\Omega = \nu_t^{\prime}-\nu_m$ | The excess wave number; the part of the energy wave number above the mass side, $\Omega=\sqrt{\nu_{\Phi}^{2}+\nu_m^{2}}-\nu_m=\nu_{\Phi}^{2}/2\nu_m-\cdots$ |
| $\nu_{\Phi}^{2}=2\nu_m\Omega+\Omega^{2}$ | The triangle with its origin moved to the mass side; exact, one term linear in the excess and one quadratic |
| $\digamma_{\mathrm{nr}} = \frac{\Omega}{2\nu_m}=\frac{\gamma-1}{2}$ | The ratio of the quadratic term to the linear one; the small parameter of the limit, with $-\digamma_{\mathrm{nr}}/(1+\digamma_{\mathrm{nr}})$ the error of the truncation |
| $\gamma = \frac{E}{mc^{2}}$, $\beta = \frac{pc}{E}$ | The Lorentz factor and the speed, the two parameters the ratios give |
| $\mathsf{L}$, $\mathsf{M}$, $\mathsf{T}$ | The dimensions of length, mass and time of the notation conventions |

## Further Reading

- [Physics Units and Common Elements Conventions](physics-units-and-common-elements-conventions.html), for the five dimensions, the derived units, and the cautions on the wave number and on $\lambda$.
- [Operator and Calculus Conventions](operator-and-calculus-conventions.html), for the gradient as a pure element and the unit of each derivative.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the chiral pair in which the mass wave number appears as a coefficient and for the harmonic parameter whose entries are the energy wave number and the mass wave number.
- [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html), for the operator $\Box_\Phi-4\pi^{2}\nu_m^{2}$ and the non-relativistic limit.
- [The Biquaternion D'Alembertian and Its Green's Functions](the-biquaternion-dalembertian-and-its-greens-functions.html), for the Yukawa kernel whose range is $1/(2\pi\nu_m)$.
- [Conformal Invariance and the Massless Limit in Biquaternionic Form](conformal-invariance-and-the-massless-limit-in-biquaternionic-form.html), for the degenerate case $\nu_m\to0$.
- [The Non-Quantum Limit of the Biquaternion Model](the-non-quantum-limit-of-the-biquaternion-model.html), for what $h\to0$ does at fixed speed and at fixed wave number, and for why no internal ratio of the three lengths can carry it.
- [The Quantum–Classical Divide in the Biquaternion Framework](the-quantum-classical-divide-in-the-biquaternion-framework.html), for the operational criterion that replaces a wavelength boundary.
