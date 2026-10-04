# __Harmonic Elementary Particles and the Periodic System of Atoms__

## Introduction

The companion article *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis* records an external programme: the reading of the biquaternionic A-field as an electro-gravimagnetic (EGM) field under the hypothesis that magnetic-charge density is gravitational mass density. That article follows the programme to its law structure — the mutual complex gradients, the field analogues of Newton's laws, the interaction energy, the shocks of the charge–current field.

This article follows the same programme one step further, into a claim of a different kind. In the formulation of 2019 the programme asks what a **monochromatic** solution of its free charge–current equation looks like, finds that the solutions are classified by the spherical harmonics, and proposes that they are **elementary particles**: standing spherical waves whose mass-charge density at the centre is fixed by their oscillation frequency. The spherically symmetric scalar-potential solutions are named **bosons**; the vector-potential solutions, whose density vanishes at the centre, are named **leptons**. The hydrogen atom is then the fundamental spherical pulsar, and the periodic system of atoms becomes a **musical scale**, in which each octave is a period of the table and the repetition of tones between octaves explains the repetition of chemical properties down a column.

The claim is a large one, made from a small algebraic base, and the corpus's task is the same as before: record what is derived, mark what is chosen, and state the cost. The division is unusually clean here, and it is made in the two halves of this article. The **monochromatic sector** of the charge–current field is elementary algebra, and it is fully solvable: the free equation factors, every solution is generated from a Helmholtz potential by one operator, the pulsar and the spinor have closed forms, their energy densities are the same function of the Bessel functions, and their Poynting biquaternion vanishes identically. All of that is verified below and belongs to the algebra. The **particle reading and the musical periodic system** are not: they rest on the identification of a solution with a particle, on the identification of frequency with mass, and on the placement of atoms on a musical scale — three choices, none of them forced, and the last of them supplying exactly the discreteness that the algebra does not.

One structural point should be stated at the outset, because it governs the whole assessment. The monochromatic amplitude obeys the **Helmholtz equation**, which is an eigenvalue equation only when a boundary condition is supplied. The programme supplies none: the frequency $\omega$ is a free parameter of the solution, continuous and arbitrary. A real cavity has discrete resonant frequencies because its walls impose a condition at a radius. Here the discreteness of the "periodic system" is imposed from outside, by the musical scale, and the dynamics is indifferent to it. That is the sharpest way to state both what the construction achieves and what it does not.

Throughout, the conventions are the corpus's, and they are not the 2019 paper's. The charge–current biquaternion is

$$
\tilde{\Theta} = i\rho + \mathbf J,
$$

as in the companion EGM article and in *Shock Electromagnetic Waves*. The 2019 paper writes the same object with a partly different sign convention, $\rho = -\rho_E/\sqrt{\epsilon} + i\rho_H/\sqrt{\mu}$ and $\mathbf J = -\sqrt{\mu}\,\mathbf{j}_E + i\sqrt{\epsilon}\,\mathbf{j}_H$, which is the negative of the corpus's; every equation below is stated in the paper's own 2019 convention where it is quoted from the paper, and the conventions are not mixed. The source's symbol $\nabla$ means the **pure-vector** gradient, $\nabla = e_1\partial_x + e_2\partial_y + e_3\partial_z$ acting by quaternion multiplication on the left, so that $\nabla\circ\nabla = -\Delta$; this is not the corpus's $\tilde{\nabla}$, which carries the time derivative, and the relation between the two is given in its own section.

## The Free Charge–Current Field and Its Monochromatic Sector

The programme's free-field law is the one recorded in the companion articles: a charge–current that is subject to no external field satisfies the inertia equation

$$
D_-\tilde{\Theta} = 0,
\qquad
D_- = \partial_\tau - i\nabla,
\qquad
\tau = ct,
$$

with the paper's pure-vector $\nabla$. Its scalar part is the conservation law $\partial_\tau\rho + \mathrm{div}\,\mathbf{J} = 0$ and its vector part the first-order inertia equation for the current; both are in the companion article, and nothing here changes them.

A **monochromatic** field is one whose time dependence is a single exponential,

$$
\tilde{\Theta}(\tau,\mathbf{x}) = \tilde{\Theta}(\mathbf{x},\omega)\,e^{-i\omega\tau},
\qquad
\omega > 0 .
$$

Substituting, $\partial_\tau \to -i\omega$, so the inertia equation becomes

$$
-i\left(\omega + \nabla\right)\tilde{\Theta}(\mathbf{x},\omega) = 0,
\qquad\text{that is}\qquad
\left(\omega + \nabla\right)\tilde{\Theta}(\mathbf{x},\omega) = 0 .
$$

The **biamplitude** $\tilde{\Theta}(\mathbf{x},\omega)$ therefore obeys a first-order equation in which the frequency appears as a mass-like term. The first thing to note is the factorisation. Because $\nabla\circ\nabla = -\Delta$,

$$
\left(\omega + \nabla\right)\circ\left(\omega - \nabla\right)
= \omega^2 + \Delta ,
$$

which is the Helmholtz operator. Hence every solution of the second-order equation

$$
\Delta\tilde{\Psi} + \omega^2\tilde{\Psi} = 0
$$

generates a solution of the first-order equation through

$$
\tilde{\Theta}(\mathbf{x},\omega) = \left(\omega - \nabla\right)\circ\,\tilde{\Psi}(\mathbf{x},\omega),
$$

and conversely every biamplitude is of that form for some $\tilde{\Psi}$. Both statements are pure algebra and both were verified numerically, the first by composing the operator with finite differences on a polynomial biquaternion field, the second on the closed forms below.

This is the cleanest part of the programme and it is worth naming. The corpus has plane-wave solutions and it has the retarded-potential and Green-function machinery, but it has no account of the **monochromatic standing** sector of the charge–current field, and that sector is what the rest of the paper is built on. Two consequences follow immediately and are used throughout.

- **A monochromatic charge–current field is equivalent to a Helmholtz potential.** The single operator $\omega - \nabla$ converts one into the other, so the classification of monochromatic solutions is the classification of Helmholtz potentials.
- **The frequency is the Helmholtz eigenvalue in the usual sense, but there is no eigenproblem.** The equation $\Delta\tilde{\Psi} + \omega^2\tilde{\Psi} = 0$ on its own admits every $\omega$. A discrete spectrum requires a boundary condition, and the programme does not impose one. Everything discrete that appears later comes from elsewhere.

The Helmholtz potentials themselves have a general integral form, which the paper gives as its equation (4): every function integrable on the sphere of radius $\omega$ generates a solution through

$$
\psi(\mathbf{x},\omega) = \int_{|\boldsymbol{\xi}| = \omega} \varphi(\boldsymbol{\xi},\omega)\, e^{-i(\boldsymbol{\xi},\mathbf{x})}\, dS(\boldsymbol{\xi}),
$$

which is the superposition of plane waves whose wave vector has fixed length $\omega$. It is the precise sense in which the frequency is the length of the wave vector here, exactly as for a plane wave of speed $c$; the rest of the article uses the spherical solutions below, and this representation is recorded only to fix the meaning of $\omega$ and to show that the general monochromatic solution carries no further parameter.

The regular solutions of the Helmholtz equation in spherical coordinates are products of a spherical Bessel function, a Legendre function and an azimuthal exponential,

$$
\psi_{nm}(\mathbf{x},\omega) = j_n(\omega r)\,P_n^m(\cos\theta)\,e^{im\lambda},
\qquad
n = 0,1,2,\dots
$$

and it is these the programme takes as its building blocks. Their two properties that matter are the symmetry statement — among the Helmholtz solutions only $\psi_{00}$ is spherically symmetric — and the behaviour at the origin,

$$
j_n(z) \sim \frac{z^n}{(2n+1)!!},
\qquad\text{as } z\to 0 ,
$$

which is the whole basis of the later particle classification. Both were verified numerically; the asymptotic form was checked against the ascending series of $j_n$ for $n = 0,1,2,3$.

## Pulsars and Spinors

The programme divides its generating potentials into two classes. Taking the potential to be a **scalar**, $\tilde{\Psi} = \psi_{nm}$, gives what the paper calls a **pulsar**,

$$
\tilde{\Theta}_{nm}^{\,0}(\mathbf{x},\omega)
= \left(\omega - \nabla\right)\circ\,\psi_{nm}
= \omega\,\psi_{nm}(\mathbf{x},\omega) - \mathrm{grad}\,\psi_{nm}(\mathbf{x},\omega),
$$

because for a scalar potential the pure-vector gradient acts as the ordinary gradient. Taking the potential to be a **vector** directed along a coordinate axis, $\tilde{\Psi} = \psi_{nm}e_j$, gives a **spinor**,

$$
\tilde{\Theta}_{nm}^{\,j}(\mathbf{x},\omega)
= \left(\omega - \nabla\right)\circ\left(\psi_{nm}e_j\right)
= \mathrm{div}\!\left(\psi_{nm}e_j\right) + \omega\,\psi_{nm}e_j - \mathrm{rot}\!\left(\psi_{nm}e_j\right),
$$

where the three terms on the right are the scalar part, the vector part and the vector part coming from the curl, as the expansion of the biquaternion product gives them. One reading caution applies to the source here. Its intermediate line for the spinor prints $\omega j_0'(\omega r)e_j$ where the expansion gives $\omega j_0(\omega r)e_j$; the results the paper then states use $j_0$, so the prime is a slip of the transcription and is not carried below.

The two classes are not on the same footing, and the difference is exactly the behaviour at the origin that the Bessel asymptotics fixes. For a pulsar the gradient term is finite or vanishing at $r = 0$ while the $\omega\psi_{nm}$ term survives whenever $n = 0$; for $n \geq 1$ the potential itself vanishes there, so the pulsar's density vanishes too. For a spinor the scalar part is built from the divergence, which carries the factor $j_1$ and vanishes at the origin, while the vector part carries $j_0$ and does not. So:

- among the **pulsars**, only the spherically symmetric one, $n = 0$, has a non-zero charge density at the centre;
- among the **spinors**, none has a non-zero charge density at the centre, whatever $n$.

That single dichotomy is what the programme turns into bosons and leptons, and the next two sections give the closed forms and the verification.

## The Spherical Harmonic Pulsar

For the spherically symmetric scalar potential $\psi_{00}(\mathbf{x},\omega) = j_0(\omega r)$ the pulsar amplitude closes in elementary functions. Using $j_0'(z) = -j_1(z)$,

$$
\tilde{\Theta}_{00}^{\,0}(\mathbf{x},\omega)
= \omega\left(j_0(\omega r) + j_1(\omega r)\,e_x\right),
\qquad
e_x = \frac{\mathbf{x}}{r},
$$

so the amplitude has the scalar part $\omega j_0(\omega r)$ and the vector part directed **radially**, $\omega j_1(\omega r)e_x$. This closed form was verified numerically by evaluating the operator $(\omega - \nabla)$ on $j_0(\omega r)$ by central differences and comparing with the right-hand side at random points, with the residual at the finite-difference floor; the identity $j_0' = -j_1$ is exact between the two closed forms.

The energy–momentum biquaternion of the programme is

$$
\tilde{\Xi} = \tfrac12\,\tilde{\Theta}\circ\tilde{\Theta}^{*},
\qquad
\tilde{\Theta}^{*} = \bar{s} - \bar{\mathbf{V}} \ \ \text{for}\ \ \tilde{\Theta} = s + \mathbf{V};
$$

the conjugation negates the vector part and complex-conjugates the coefficients, exactly the corpus's ${}^{*}$. Its scalar part is the energy density and its vector part the Poynting analogue. For the spherical pulsar,

$$
W_{00}^{\,0} = \tfrac12\,\omega^2\left(j_0^2(\omega r) + j_1^2(\omega r)\right),
\qquad
\mathbf P_{00}^{\,0} \equiv 0 .
$$

Both were verified numerically, the density against the closed form and the vanishing of $\mathbf P$ against the computed product. The vanishing is not an accident of this solution. Because ${}^{*}$ negates the vector part, the vector part of $\tilde{\Theta}\tilde{\Theta}^{*}$ is $-s\bar{\mathbf{V}} + \bar{s}\mathbf{V} - [\mathbf{V},\bar{\mathbf{V}}]_{\mathrm{vec}}$, which vanishes identically whenever the amplitude's four components are **real**, as they are for every standing monochromatic solution of this kind. A standing wave has no net energy flux, and the model's expression for it says so algebraically. The programme's reading is that a harmonic particle does not radiate, and on this point the algebra agrees: $\mathbf P \equiv 0$ is a theorem about the conjugation, not a hypothesis.

The asymptotics follow from the same two closed forms and are the quantitative content of the model at short and long range. As $r\to 0$, with $j_0(0) = 1$ and $j_1(z)\sim z/3$,

$$
\rho_{00}^{\,0} \to \omega ,
\qquad
\left\|\mathbf J_{00}^{\,0}\right\| \to \frac{\omega^2 r}{3},
\qquad
W_{00}^{\,0} \to \tfrac12\omega^2 ,
\qquad
\mathbf P_{00}^{\,0} \equiv 0 ,
$$

so the charge density at the centre is **equal to the oscillation frequency**, the current density vanishes linearly, and the energy density is half the frequency squared. As $r\to\infty$, $j_0(\omega r) = \sin(\omega r)/(\omega r)$ gives

$$
\rho_{00}^{\,0} = \frac{\sin(\omega r)}{r},
\qquad
W_{00}^{\,0} \to \frac{1}{2r^2},
$$

so the density falls as $r^{-1}$ and the energy as $r^{-2}$. Both limits were verified numerically. One numerical detail differs: the source states the current asymptote as $\tfrac{2}{3}\omega^2r$ where the derivation gives $\tfrac13\omega^2r$, and the closed form gives the smaller value.

Two structural facts about the radial profile are worth extracting, since they are what the "atom" section uses.

- **The charge density has nodal spheres, the energy density has none.** Setting $j_0(\omega r) = 0$ gives the spherical nodes of the density at $r_k = \pi k/\omega$, $k = 1,2,3,\dots$, verified for $k = 1,\dots,4$. The energy density, however, is $\tfrac12\omega^2(j_0^2+j_1^2)$, which is strictly positive: clearing denominators writes the node condition as $x^2 + \sin^2x - x\sin 2x = 0$ with $x = \omega r$, and that function is positive for every $x > 0$. The energy density of a spherical harmonic pulsar therefore has no nodes at all.
- **The source's own node equation is mis-signed but reaches the same conclusion.** The paper prints the condition as $x^2 + x\sin 2x - \sin^2x = 0$, which is the negative of the two terms beyond $x^2$; the derived equation is $x^2 + \sin^2x - x\sin 2x = 0$. Both were scanned numerically on a fine grid, and neither has a positive real root, so the conclusion the paper draws — no nodal spheres in the energy — survives the slip.

## The Spherical Spinor

For the vector potential directed along the first axis, $\tilde{\Psi} = j_0(\omega r)e_1$, the spinor amplitude also closes. Expanding the product gives

$$
\tilde{\Theta}_{00}^{\,1}(\mathbf{x},\omega)
= -\,\omega\,j_1(\omega r)\,r_{,1}
+ \omega\left(j_0(\omega r)\,e_1 + j_1(\omega r)\left(r_{,3}e_2 - r_{,2}e_3\right)\right),
\qquad
r_{,k} = \frac{x_k}{r},
$$

so the scalar part carries the factor $j_1$ and vanishes at the origin while the vector part carries $j_0$ and does not. This was verified numerically to the finite-difference floor. For a general orientation $\mathbf e$ the derived form is

$$
\tilde{\Theta}_{00}^{\,\mathbf e}(\mathbf{x},\omega)
= -\,\omega\,j_1(\omega r)\left(\mathbf e, e_x\right)
+ \omega\left(j_0(\omega r)\,\mathbf e - j_1(\omega r)\left[\mathbf e, e_x\right]\right),
$$

and the paper's stated general form, its equation (4.4), carries the opposite sign on the commutator term. The source contradicts itself here: its equation (4.1) for the axis-directed case writes the term out explicitly as $\omega j_1(\omega r)(r_{,3}e_2 - r_{,2}e_3)$, which is $-\omega j_1[\mathbf e, e_x]$, while its general form would give $+\omega j_1[\mathbf e, e_x]$. The sign printed here is the derived one, and it is the one the source's own components use.

The energy density is the same function of the Bessel functions as the pulsar's. Because the scalar and vector parts contribute with the weights $r_{,1}^2$ and $r_{,2}^2 + r_{,3}^2$, and because

$$
\sum_{k=1}^{3} r_{,k}^2 = 1
$$

identically, the two contributions complete to

$$
W_{00}^{\,1} = \tfrac12\,\omega^2\left(j_0^2(\omega r) + j_1^2(\omega r)\right),
\qquad
\mathbf P_{00}^{\,1} \equiv 0 ,
$$

which is exactly the pulsar's energy density, and which the paper states without displaying the identity that makes it work. Both were verified numerically, the identity to machine precision and the density against the closed form. The same asymptotics follow: the charge density vanishes at the centre as $r$, the current density tends to the finite value $\omega$, and the energy density tends to $\tfrac12\omega^2$.

So the pulsar and the spinor differ in exactly one respect, and it is a single term: at the centre the pulsar's scalar part is $\omega$ while the spinor's is zero. Their energies, their vanishing Poynting vectors and their far-field falloffs are identical.

## Monochromatic Structures and Crystals

The paper's last construction widens the class of monochromatic solutions without solving anything new, and it is the one item of this paper that the corpus does not already have elsewhere. Take any biquaternion function $K(\mathbf{x})$ — the paper calls it a **structural biquaternion** — and convolve a solution with it. The operator is a differential operator with constant coefficients, and differentiation passes through a convolution, so the convolution of a solution with any $K$ is again a solution. The same device reappears in the programme's 2020 paper on the field side, where it weights the free-photon cloud; *The Ether and Photons in the Electro-Gravimagnetic Programme* records it there and cross-refers to this section. In components, for $\tilde{\Theta} = i\rho + \mathbf{J}$ and $K = k + \mathbf{K}$,

$$
\tilde{\Theta} * K = i\,\rho * k - \sum_{j=1}^{3} \mathbf{J}_j * \mathbf{K}_j
+ \Big\{ i\,\rho * \mathbf{K} + \mathbf{J} * k
+ \sum_{j,l,m=1}^{3} \varepsilon_{jlm}\,(\mathbf{J}_j * \mathbf{K}_l)\,e_m \Big\},
$$

which is just the biquaternion product carried out with convolution in place of multiplication; it was checked against that product to machine precision. The mechanism is elementary: a shift commutes with a derivative, $D(S_{\mathbf{s}}f) = S_{\mathbf{s}}(Df)$ for $S_{\mathbf{s}}f(\mathbf{x}) = f(\mathbf{x}-\mathbf{s})$, which was verified exactly on a grid, so every shifted copy of a solution is a solution, and so is any weighted sum of copies.

Choosing the structural biquaternion to be a lattice of shifted $\delta$-functions is what the paper builds from this. For an inhomogeneous rectangular lattice with steps $(h_l,h_m,h_n)$ and weights $a_{lmn}$,

$$
K(\mathbf{x}) = \sum_{l,m,n} a_{lmn}\,\delta(x_1 - l h_l)\,\delta(x_2 - m h_m)\,\delta(x_3 - n h_n),
$$

and convolution with it is the weighted sum of shifted copies of the base particle,

$$
\tilde{\Theta}(\mathbf{x},\omega) = \sum_{l,m,n} a_{lmn}\,
\tilde{\theta}_0\big(\mathbf{x} - (l h_l,\, m h_m,\, n h_n),\, \omega\big),
$$

so a lattice of harmonic pulsars is again a monochromatic solution of the free charge–current equation. Several frequencies may be superposed in the same way, and the paper notes that such a superposition is in general **incommensurable** — it has no common period — which is the same fact that later excludes the equal-tempered scale from its periodic system.

The construction is genuine algebra, and it is the one part of this paper that supplies the corpus with something it lacked: a way to build a periodic biquaternion structure, by convolution, out of a single solution, with nothing further solved and nothing assumed. The corpus had no periodic or crystalline biquaternion object before it. What the naming adds is interpretation. The paper calls the products **crystals**, **bodies**, **tissues** and **filaments**, according as the structure is periodic, extended, spread out or linear, and reads the lattice construction as matter assembled from particles. The construction and the naming are recorded separately, for the same reason as everywhere else in this article: the convolution theorem is a property of the linear equation, while the identification of a lattice of solutions with a crystal is one more choice, of the same kind as the particle reading itself, and it inherits that reading's gap — nothing in the algebra fixes the lattice steps, the weights, or the frequency.

## The Classification into Bosons and Leptons

The programme's classification is the following. A harmonic solution whose mass-charge density is non-zero at its centre is a **heavy** particle; one whose density vanishes at the centre is a **light** particle. By the asymptotics above, the first class consists of the spherical pulsars — and, among the pulsars, of the single spherically symmetric one — while the second consists of all spinors and of all pulsars with $n \geq 1$. The paper identifies the first class with **bosons** and the second with **leptons**, and reads the spinors as a lepton family.

The algebra here is sound and the naming is not. Three things should be said.

- **The classification criterion is one number at one point.** Everything that is asserted about a particle follows from whether the scalar part survives at $r = 0$, which by the Bessel asymptotics is a question about $n$ and about whether the potential was scalar or vector. It distinguishes the family $n = 0$, scalar potential, from everything else. That is a genuinely derived dichotomy, and it is thin: it is a statement about the first term of a Taylor expansion.
- **The words "boson" and "lepton" are borrowed, not derived.** The programme has no spin, no statistics, no exclusion principle and no spin–statistics relation, so there is nothing in it for the words to attach to. The paper says as much — it states that it uses "the names for heavy and light particles, adopted from" quantum field theory — and the reader should take that literally: the classification is into heavy and light, and the quantum names are labels.
- **The heavy/light reading is supported by the centre density, not by a mass.** The density at the centre is $\omega$, and the frequency is identified with mass. That identification is the programme's, is dimensionally unsupported without a constant, and is what the next two sections test.

The remaining structural point is that the third class the paper mentions — spinors and asymmetric pulsars together — has no internal distinction in the algebra. Any potential with $n \geq 1$, or any vector potential, gives a vanishing central density and hence a "lepton". The model therefore predicts one heavy particle and an unlimited family of light ones, and the observed one-to-many structure of the particle spectrum is not reproduced by it.

## The Elementary Hydrogen Atom

The programme's hydrogen atom is the spherically symmetric pulsar of §III at a frequency $\omega_0$ that it takes to be the minimum frequency of the hydrogen spectrum:

$$
\tilde H_0(\tau,\mathbf{x})
= \omega_0\left(j_0(\omega_0 r) + j_1(\omega_0 r)e_x\right)e^{-i\omega_0\tau}.
$$

Everything in the preceding sections applies to it without change: the charge density at the centre is $\omega_0$, the density falls as $r^{-1}$, the energy density as $r^{-2}$, the energy density has no nodal spheres, the charge density has them at $r_k = \pi k/\omega_0$, and the energy flux vanishes identically — which the paper reads as the statement that the atom does not radiate.

Two comparisons must be made, and both are about what the object is not. It is **not** the hydrogen atom of the corpus. *The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case* and its relativistic companion solve the Coulomb two-body problem: a potential is inserted, the bound-state eigenvalue problem is set up, separated in spherical coordinates, and solved for the Rydberg spectrum. Here no potential is inserted, no two-body problem is posed, and no eigenvalue problem is solved: the object is a single monochromatic standing wave of the charge–current field, and its frequency is a free parameter. The two constructions share the spherical harmonics and the letter $\omega$ and nothing else. The programme's atom has no proton, no electron, no Coulomb field and no Rydberg series.

It is also **not** a spectrum. The paper writes the frequency $\omega_0$ as "the minimum frequency of the hydrogen spectrum", which is an input read off the atom it is supposed to explain. Because the Helmholtz equation carries no boundary condition, no sequence of frequencies is selected; a discrete set would require either a boundary at some radius or a quantisation condition, and the programme supplies neither. What the model has is a one-parameter family of standing waves, and the discreteness of the periodic system in the next section is imposed on that family from outside.

The paper's further claim — that the electric and gravimagnetic charge densities and currents of this atom are given by its equations (5.1) and (5.2), which are products of $\cos(\omega_0\tau)$ or $\sin(\omega_0\tau)$ with $\sin(\omega_0 r)/r$ and with the corresponding combination for the current — is a rewriting of the pulsar amplitude into the electric and gravimagnetic variables. It is not independently verified here: the placement of $\sqrt{\epsilon}$ and $\sqrt{\mu}$ between the complex and the physical densities is convention-dependent, the source's text mixes the arguments $\omega_0r$ and $\omega_0r/c$ in the two ways of writing the same solution, and its numerical value of $c$ carries an extra digit ($2997924581$ rather than $299792458$). The $r$-dependence that the paper uses from these formulas — the nodal spheres at $\pi k/\omega_0$ — is the one verified above from the pulsar amplitude directly.

## The Periodic System as a Musical Scale

The programme's last step is to order atoms by frequency, identify frequency with mass, and place the atoms on the **pure (just-intonation) major scale**. In the *simple gamma* the tones of an octave have frequencies in the rational ratios

$$
1,\ \tfrac98,\ \tfrac54,\ \tfrac43,\ \tfrac32,\ \tfrac53,\ \tfrac{15}{8},\ 2,
$$

and each successive octave doubles the previous one, so that the frequency of the $k$-th tone in the $n$-th octave is

$$
\omega_{nk} = 2^n\gamma_k\,\omega,
\qquad
\gamma_k \in \left\{1, \tfrac98, \tfrac54, \tfrac43, \tfrac32, \tfrac53, \tfrac{15}{8}, 2\right\},
$$

where $\omega$ is the fundamental. The hydrogen atom is the tone *do* of the first octave. All the ratios were verified as stated: they are the classical just scale, they are rational, and consecutive octaves differ by the factor $2$.

The argument for a *pure* scale rather than the familiar twelve-tone equal temperament is the one interesting piece of reasoning in this section, and it is correct as far as it goes. Equal temperament has a semitone step $2^{1/12}$, which is **irrational**; the paper's point is that tones whose frequency ratios are irrational have no common period, so their superposition never repeats exactly. In the just scale the ratios are rational, so every tone of an octave shares a common period and whole octaves can be superposed without beats. The irrationality was checked — no rational approximation $p/q$ with $q < 1000$ reproduces $(p/q)^{12} = 2$ — and it is elementary. The paper uses this to explain the *repeatability* of chemical properties down a column of the periodic table: all the tones of a previous octave are present in the next, as the octave doubles.

Two limits on the argument must be stated with it. First, the reasoning is about **commensurability**, which is a statement about superposition, not about atoms; nothing in the model couples an atom to another atom's tone, so the harmony that the argument establishes has nothing to act on. Second, the mapping from tones to elements is never fixed. The paper says only that the frequency, and hence the mass, increases with the tone, that the number of tones in an octave can grow with the octave, and that the previous octave's tones must be present. That leaves the assignment of an element to a tone free, and it does not touch the actual row lengths of the periodic table — $2, 8, 8, 18, 18, 32, 32$ — which the just scale's eight tones per octave do not produce.

Since the one quantitative prediction the programme makes is that atomic masses stand in the ratios $2^n\gamma_k$, it is worth testing. It fails as stated, and it fails in the two ways such tests usually fail.

- **Read in mass order, it is wrong immediately.** With the lightest atoms assigned to the tones of the first octave in order, the mass of helium should be $\tfrac98$ of hydrogen's, whereas the measured ratio is about $3.97$.
- **Read with a free octave for each element, it is vacuous.** If each element may sit on any tone of any octave, then all but lithium and nitrogen among the eight lightest atomic weights lie within about one per cent of some $2^n\gamma_k$ — but so they must, because the scale's ratios are ratios of small integers and atomic weights are close to integers, the mass number dominating the atomic weight. The test is not whether a weight is near a simple rational, which is nearly always true, but whether the simple rational is *predicted*; and the counterexample is lithium, whose weight ratio $6.885$ is not near any $2^n\gamma_k$ while being within $1.6$ per cent of the plain integer $7$, which is not in the scale at all.

The programme's own admission is worth recording in its own words: it says that its model is "completely different, deterministic, based on the definition of real physical characteristics of elementary particles and atoms, not probabilistic". That is a statement of what the author intends the model to be. It is not an argument against the quantum theory, because it does not engage with the reasons that theory is probabilistic — the violation of the Bell inequalities, which the corpus treats in its own articles — and a deterministic model that reproduces no quantum number cannot displace a stochastic one that reproduces millions of them.

## What the Programme Establishes and What It Does Not

The division is unusually clean, and it is worth stating as a list, because the two halves of this article have different standing.

Established, and verified above by recomputation.

1. The free charge–current equation factors monochromatically into $(\omega - \nabla)$ and $(\omega + \nabla)$, and $(\omega+\nabla)(\omega-\nabla) = \omega^2 + \Delta$; every monochromatic solution is $(\omega-\nabla)\tilde{\Psi}$ for a Helmholtz potential $\tilde{\Psi}$.
2. The spherical pulsar has the closed form $\omega(j_0 + j_1e_x)$, energy density $\tfrac12\omega^2(j_0^2+j_1^2)$, and vanishing Poynting biquaternion.
3. The spherical spinor has the closed form $- \omega j_1 r_{,1} + \omega(j_0e_1 + j_1(r_{,3}e_2-r_{,2}e_3))$, the **same** energy density as the pulsar, and vanishing Poynting biquaternion.
4. The vanishing Poynting biquaternion is a general property of standing monochromatic solutions with real amplitude components, not a special feature of these two.
5. The central charge density is $\omega$ for the spherically symmetric pulsar and zero for every spinor and every pulsar with $n\geq1$, by the Bessel asymptotics.
6. The charge density of the spherical pulsar has nodal spheres at $r_k = \pi k/\omega$; its energy density has no nodes.
7. The just scale's ratios are rational and octave-doubled as stated.
8. **Convolution with any structural biquaternion $K$ preserves solutions**, because differentiation passes through a convolution; the shift identity $D(S_{\mathbf s}f) = S_{\mathbf s}(Df)$ holds exactly; and taking $K$ to be a lattice of shifted $\delta$-functions therefore gives a lattice of shifted harmonic particles that is again a monochromatic solution — the paper's crystal construction.

Not established, and not derivable from the algebra.

1. **No boundary condition, hence no spectrum.** The Helmholtz equation admits every $\omega$. There is no eigenvalue problem, so the model selects no frequencies; the discreteness of the "periodic system" is imported from the musical scale. This is the single largest gap, and every discrete claim rests on it.
2. **No coupling constant, hence no masses.** The identification of frequency with mass fixes no units, exactly as the companion article's identification of magnetic charge with mass fixed no value of $G$. The model cannot predict a mass and cannot be falsified by one.
3. **No spin, no statistics, no exclusion principle.** The words boson and lepton are borrowed; the algebra has nothing for them to name beyond a value at the origin.
4. **No atoms.** The "elementary hydrogen atom" is a single standing wave with a free frequency: no proton, no electron, no Coulomb field, no Rydberg series, no comparison with the measured hydrogen spectrum.
5. **No periodic system.** The tone-to-element map is never fixed; the row lengths of the periodic table are not reproduced; and the mass-ratio prediction fails in mass order and is vacuous when the octave is left free.

## Summary

The 2019 formulation of the electro-gravimagnetic programme takes the **monochromatic** sector of its free charge–current field and proposes to read the solutions as elementary particles. The monochromatic sector is a clean piece of algebra: the free equation is $(\omega+\nabla)\tilde{\Theta}(\mathbf{x},\omega) = 0$, the operator factors so that $(\omega+\nabla)(\omega-\nabla) = \omega^2+\Delta$, and every solution is generated from a Helmholtz potential by the single operator $\omega - \nabla$. The regular Helmholtz solutions are the spherical harmonics, and they split into **pulsars**, from a scalar potential, and **spinors**, from a vector one.

The spherically symmetric pulsar is $\omega(j_0(\omega r) + j_1(\omega r)e_x)$ with the scalar part $\omega j_0$; the spinor polarised along a fixed axis is $-\omega j_1r_{,1} + \omega(j_0e_1 + j_1(r_{,3}e_2-r_{,2}e_3))$ with scalar part $-\omega j_1r_{,1}$. Both have energy density $\tfrac12\omega^2(j_0^2+j_1^2)$ and both have a vanishing Poynting biquaternion — which is a general property of standing waves under the conjugation $\tilde{\Theta}^{*} = \bar s - \bar{\mathbf{V}}$, and which the programme reads as the statement that a harmonic particle does not radiate. The pulsar's central density is $\omega$; every spinor's is zero; and that one dichotomy, decided by the Bessel asymptotics $j_n(z)\sim z^n/(2n+1)!!$, is the programme's classification of heavy particles from light ones, which it names bosons and leptons. All of these statements were verified numerically, as were the $r^{-1}$ and $r^{-2}$ far-field falloffs, the nodal spheres of the density at $\pi k/\omega$, and the absence of nodes in the energy density.

The one construction in the paper that the corpus did not already have is the **convolution**: since a constant-coefficient differential operator commutes with convolution, convolving any monochromatic solution with an arbitrary structural biquaternion $K(\mathbf x)$ yields another solution, and choosing $K$ to be an inhomogeneous lattice of shifted $\delta$-functions produces a lattice of shifted harmonic pulsars — the paper's crystal, body, tissue and filament construction. This part is algebra and it was verified; the naming of the products as crystals is interpretation, and the lattice steps, weights and frequencies are free parameters, as everything else discrete in the programme is.

What the algebra does not supply is everything the particle reading needs. The Helmholtz equation carries no boundary condition, so no frequency is selected and there is no spectrum; the identification of frequency with mass carries no constant, so no mass is predicted; the algebra has no spin or statistics, so the quantum names are labels on a heavy/light split; and the "hydrogen atom" shares nothing with the corpus's hydrogen articles but the spherical harmonics. The periodic system is placed on the just-intonation scale by hand, and its one testable consequence — that atomic masses stand in the ratios $2^n\gamma_k$ — fails in mass order (helium would be $\tfrac98$ of hydrogen, and is $3.97$ times it) and is vacuous when the octave is free, since the scale's ratios are simple rationals and atomic weights are near integers. The argument that the pure scale is required for commensurability is correct in itself and has nothing in the model to act on.

The corpus's relation to this part of the programme is therefore the same as to the rest of it, and the same verdict applies with less to be said in praise of the additions: the monochromatic algebra — the factorisation, the Helmholtz correspondence, the pulsar and spinor closed forms, and the convolution that builds periodic structures from a single solution — is a genuine and reusable piece of the biquaternion formalism, and the particle, atom, crystal and periodic-system readings built on it are choices, none of which is forced by that algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{\Theta} = i\rho + \mathbf J$ | Charge–current biquaternion (corpus symbol) |
| $\rho, \mathbf J$ | Complex charge and current densities of the charge–current field |
| $\rho_E, \rho_H$ | Electric and gravimagnetic charge densities |
| $\mathbf{j}_E, \mathbf{j}_H$ | Electric and gravimagnetic current densities |
| $\rho = -\rho_E/\sqrt{\epsilon} + i\rho_H/\sqrt{\mu}$ | 2019 source's charge convention (negative of the corpus's) |
| $\mathbf J = -\sqrt{\mu}\,\mathbf{j}_E + i\sqrt{\epsilon}\,\mathbf{j}_H$ | 2019 source's current convention |
| $\tau = ct$ | Scaled time; $\omega$ is a frequency in units of $1/\mathrm{length}$ |
| $\nabla = e_1\partial_x+e_2\partial_y+e_3\partial_z$ | Pure-vector gradient, acting by left quaternion multiplication |
| $\nabla\circ\nabla = -\Delta$ | The square of $\nabla$; hence the factorisation below |
| $(\omega+\nabla)(\omega-\nabla) = \omega^2+\Delta$ | Helmholtz factorisation of the monochromatic operator |
| $D_\pm = \partial_\tau \pm i\nabla$ | Mutual complex gradients; monochromatically $D_\pm \to -i(\omega \mp \nabla)$ |
| $K = k + \mathbf K$ | Structural biquaternion; any biquaternion function used as a convolution kernel |
| $\tilde{\Theta} * K$ | Biquaternion convolution, with component convolutions; preserves solutions of the free equation |
| $\delta(x_j - n h_j)$ | Lattice of shifted $\delta$-functions; the crystal structural biquaternion |
| $\tilde{\Theta}(\mathbf{x},\omega)$ | Biamplitude, $\tilde{\Theta}(\tau,\mathbf{x}) = \tilde{\Theta}(\mathbf{x},\omega)e^{-i\omega\tau}$ |
| $\tilde{\Psi}$ | Helmholtz potential, $\Delta\tilde{\Psi} + \omega^2\tilde{\Psi} = 0$ |
| $\psi_{nm} = j_n(\omega r)P_n^m(\cos\theta)e^{im\lambda}$ | Regular spherical Helmholtz solutions |
| $j_n$ | Spherical Bessel function of order $n$ |
| $\tilde{\Theta}_{nm}^{\,0} = (\omega-\nabla)\circ\,\psi_{nm}$ | Pulsar (scalar potential) |
| $\tilde{\Theta}_{nm}^{\,j} = (\omega-\nabla)\circ(\psi_{nm}e_j)$ | Spinor (vector potential) |
| $e_x = \mathbf{x}/r$ | Radial unit vector |
| $r_{,k} = x_k/r$ | Direction cosines; $\sum_k r_{,k}^2 = 1$ |
| $\tilde{\Xi} = \tfrac12\tilde{\Theta}\circ\tilde{\Theta}^{*}$ | Energy–momentum biquaternion |
| $\tilde{\Theta}^{*} = \bar s - \bar{\mathbf V}$ | Vector-negating, coefficient-conjugating conjugation |
| $W = \tfrac12(|s|^2 + \|\mathbf V\|^2)$ | Energy density (scalar part of $\tilde{\Xi}$) |
| $\mathbf P$ | Poynting analogue (vector part of $\tilde{\Xi}$) |
| $\omega_0$ | Frequency of the "elementary hydrogen atom" |
| $\gamma_k$ | Just-scale ratios $\{1,\tfrac98,\tfrac54,\tfrac43,\tfrac32,\tfrac53,\tfrac{15}{8},2\}$ |
| $\omega_{nk} = 2^n\gamma_k\omega$ | Frequency of tone $k$ in octave $n$ |

## Further Reading

- L. A. Alexeyeva, "Biquaternionic representation of harmonic elementary particles. Periodic system of atoms", *SSRG International Journal of Applied Physics* **6**(3) (2019) 73–80, doi:10.14445/23500301/IJAP-V6I3P112, the paper recorded here.
- L. A. Alexeyeva, "Periodic System of Atoms in Biquaternionic Representation", *Journal of Modern Physics* **9** (2018) 1633–1644, doi:10.4236/jmp.2018.98102, the journal-published earlier form of the same programme: the inertia law for monochromatic fields, the structural-biquaternion convolution and the lattice (crystal) construction recorded here, which are this paper's and not the 2019 paper's.
- L. A. Alexeyeva, "Ether and photons in biquaternionic presentation", *SSRG International Journal of Applied Physics* **7**(1) (2020) 96–101, doi:10.14445/23500301/IJAP-V7I1P114, the same programme's later turn: the same Helmholtz factorisation applied to the **field** rather than the source, with the ether naming, the elementary photon, the free plane modes and the no-pure-gravitational-wave claim. It is recorded in *The Ether and Photons in the Electro-Gravimagnetic Programme*.
- L. A. Alexeyeva, "Lorentz Transformations for One Biquaternionic Model of the Electro-Gravimagnetic Field. Conservation Laws" (2009), arXiv:0904.3446v1, the Russian-language preprint of the same 2009 work recorded in *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis*, for the free charge–current equation, the mutual complex gradients and the inertia law on which the monochromatic sector is built.
- L. A. Alexeyeva, "One Biquaternion Model of the Electro-Gravimagnetic Field. Field Analogues of Newton's Laws", arXiv:math-ph/0703034v1 (2007), for the charge–current biquaternion, the energy–momentum biquaternion and the current-field density and flux used here.
- G. E. Shilov, *Simple Gamma* (Moscow State University, 1970), cited by the paper as the source of the just-intonation scale's ratios.
- M. Abramowitz and I. A. Stegun (eds.), *Handbook of Mathematical Functions*, Applied Mathematics Series 55, National Bureau of Standards (1964), cited by the paper for the spherical Bessel functions, the associated Legendre functions and their asymptotics.
- V. S. Vladimirov, *Generalized Functions in Mathematical Physics* (Moscow, Nauka, 1978), cited by the paper for the surface-integral representation of the Helmholtz solutions and the biquaternionic convolution.
- *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis*, for the programme's field equations, its Newton-law analogues and its empirical claims, of which those recorded here are the continuation.
- *Maxwell's Equations in the Biquaternionic Formulation*, for the corpus's A-field, its energy density and Poynting vector, and the corpus's sign conventions, which this article restates before quoting the 2019 paper.
- *The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case* and *— The Relativistic Case*, for the Coulomb bound-state problem to which the programme's "elementary hydrogen atom" is not related beyond the spherical harmonics.
- *Shock Electromagnetic Waves*, for the charge–current field's first-order system and its non-transverse fronts, recorded there from the same programme.
- John Stewart Bell, "On the Einstein Podolsky Rosen paradox", *Physics* **1** (1964) 195–200, and its companion articles in this corpus, for the reason a deterministic alternative to quantum physics must also be non-local, which the programme's closing claim does not address.
