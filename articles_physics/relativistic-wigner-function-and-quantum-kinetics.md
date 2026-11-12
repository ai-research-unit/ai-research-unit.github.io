# __Relativistic Wigner Function and Quantum Kinetics__

## Introduction

**The kinetic equation of this article is the $\hbar$-expansion of the Wigner element of the preceding one, and its content is two terms: a classical drift and a correction at order $\hbar^{2}$.** Nothing else is derived. The drift moves the phase-space density along the flow's worldlines; the correction, a third derivative in momentum weighted by the third derivative of the potential, is the first place the expansion differs from the classical transport equation.

**This article is [The Wigner Function in Biquaternionic Form](the-wigner-function-in-biquaternionic-form.html) differentiated in time and expanded in $\hbar$.** The definition of $\tilde W_\Xi$, its marginals, its classical limit and its negativity are that article's and are not restated. What is new here is the equation the element satisfies, the order at which the equation departs from the classical one, and the moments at which that departure shows.

**The kinetic equation and its collision structure are the corpus's already, and are cited, not repeated.** [The Schwinger–Keldysh Formalism in Biquaternionic Form](the-schwinger-keldysh-formalism-in-biquaternionic-form.html) owns the closed-time-path contour, the branch doubling, the Keldysh rotation, the matrix of Green's functions, the Kadanoff–Baym equations and their collision term. This article treats the *collisionless* equation — the one whose only content is the free drift plus the $\hbar^{2}$ term — and says so at every point where a reader might expect a collision integral. The two articles fit together as follows: the Schwinger–Keldysh article gives the equation *with* self-energies, and this one gives the free part of it at the order where the quantum correction first appears.

**The order of business.** The expansion is set up first, from the Moyal bracket, with the operator that generates it and the counting that organises it. Then the zeroth order, which is the classical drift, in the letters of the corpus and on the mass shell. Then the order-$\hbar^{2}$ term, its moments, and the two exact statements that can be made about it: it vanishes for a quadratic potential, and its first nonzero moment is the third. Then the relativistic bookkeeping, in which the temporal coordinate is a length. Then a short section on what the Kadanoff–Baym structure supplies and what this article deliberately leaves to it. The article closes with the status section, the summary, and the notation.

## Where the Expansion Comes From

### The Moyal bracket, in one display

**The Wigner element's time derivative is the Moyal bracket of the Hamiltonian element with the Wigner element.** Write the Hamiltonian of the scalar field's non-relativistic reduction as the element built from the operator

$$
\hat H=\frac{\lvert\hat{\vec p}\rvert^{2}}{2m}+V(\hat r),
$$

and let $H(r,\vec p)=\lvert\vec p\rvert^{2}/(2m)+V(r)$ be its symbol. Then the exact equation for the Wigner function is

$$
\frac{\partial W}{\partial t}=\frac{2}{\hbar}\sin\!\left(\frac{\hbar}{2}\Lambda\right)\bigl(H\,W\bigr),
\qquad
\Lambda=\overleftarrow{\frac{\partial}{\partial r_\eta}}\overrightarrow{\frac{\partial}{\partial p_\eta}}
-\overleftarrow{\frac{\partial}{\partial p_\eta}}\overrightarrow{\frac{\partial}{\partial r_\eta}},
$$

with the summation over the spatial index $\eta$ understood and every index low, as the corpus's metric $\delta_{\mu\nu}$ requires. The operator $\Lambda$ is antisymmetric and it acts on the product $HW$, differentiating the first factor to the left and the second to the right.

**The structure of the display is worth reading before the expansion.** The sine is what makes the equation exact: it is the whole of the difference between quantum and classical transport, written as a power series in $\hbar\Lambda/2$. Expanding the sine gives the series whose first term is the Poisson bracket and whose next term is the order-$\hbar^{2}$ correction. Nothing is dropped in the display; what is dropped later is dropped explicitly and with a stated reason.

### The counting

**Each application of $\Lambda$ to $HW$ brings one power of $\hbar$ in the expansion, and the reason is that one of its two derivatives must fall on $W$.** The symbol $W$ varies on the scale of the state's phase-space structure, so a momentum derivative of it is of order $1/\delta p$ and a position derivative of order $1/\delta r$; the product $\delta r\,\delta p$ is of order $\hbar$ for a state near the uncertainty limit. So $\hbar\Lambda$ acting on $HW$ is of order one, and the series is a series in the *smallness of the state relative to the scale on which the potential varies* — the gradient expansion — rather than a series in a numeric small parameter.

**Two consequences of the counting, both standard.** First, the series terminates at a finite order when $V$ is a polynomial, because a derivative of $V$ eventually vanishes. Second, the first correction is not universal: it is the first term of a gradient expansion, and its size is set by how fast the potential varies across the state. A state spread over a region where the potential is quadratic has no correction at any order, which is the statement of the next section's exactness result.

### The coefficient, and how it was checked

**The order-$\hbar^{2}$ term of the sine expansion carries the coefficient $1/24$ and the third derivative of the potential.** From $\sin z=z-z^{3}/6+\cdots$ with $z=\hbar\Lambda/2$,

$$
\frac{2}{\hbar}\sin\!\left(\frac{\hbar}{2}\Lambda\right)
=\Lambda-\frac{\hbar^{2}}{24}\Lambda^{3}+\mathcal{O}(\hbar^{4}),
$$

so the equation reads

$$
\boxed{\;
\frac{\partial W}{\partial t}=\Lambda(HW)-\frac{\hbar^{2}}{24}\Lambda^{3}(HW)+\mathcal{O}(\hbar^{4})
\;}
$$

and the whole of the $\hbar^{2}$ correction is the second term.

**The coefficient and the structure were checked symbolically, not remembered.** Applying the bidifferential operator three times to the pair $(H,W)$ with $H=\lvert\vec p\rvert^{2}/(2m)+V(r)$ and a general symbol $W(r,\vec p)$, only one of the eight ordered terms survives, because every term in which the position and momentum derivatives fall on the same side mixes them, and a mixed third derivative of a separable Hamiltonian vanishes. The surviving term is

$$
\Lambda^{3}(H,W)=\frac{\partial^{3}V}{\partial r_\eta^{3}}\,
\frac{\partial^{3}W}{\partial p_\eta^{3}},
$$

with the sum over $\eta$, **and the identity is exact rather than leading**: a computer-algebra evaluation of the four surviving monomials returns $\Lambda^{3}(H,W)-V'''\partial_{p}^{3}W=0$ as an identity in $W$. The expansion of the sine is therefore not a gradient approximation at this order — for a Hamiltonian at most quadratic in momentum, the third-order term is precisely the third derivative of the potential times the third momentum derivative of the Wigner element.

**This is worth one paragraph of explanation, because it is not an accident.** Each application of $\Lambda$ contributes one position derivative and one momentum derivative, and the split of them between the two factors is what decides whether a term survives. **The Hamiltonian is separable — a function of $\vec p$ alone plus a function of $\vec r$ alone — and that is what kills every mixed term.** A third derivative of $H$ that carries both a position and a momentum derivative is zero, because the position derivatives must fall on $V$ and the momentum derivatives on $\lvert\vec p\rvert^{2}/(2m)$, and the two pieces of the sum carry different variables; a derivative does not act across a sum into a product. So of the eight ordered terms only the one with all three position derivatives on $H$ and all three momentum derivatives on $W$ survives, and inside it only the purely positional part of $H$'s third derivative, which is $V'''$.

**The same argument repeats at every order, so the expansion can be written down whole.** The term of order $\hbar^{2k}$ is $\Lambda^{2k+1}$ with the same selection, and the only surviving piece is again purely positional on $H$:

$$
\frac{2}{\hbar}\sin\left(\frac{\hbar\Lambda}{2}\right)(H,W)
=\Lambda(H,W)-\frac{\hbar^{2}}{24}V'''\frac{\partial^{3}W}{\partial p_\eta^{3}}
+\frac{\hbar^{4}}{1920}V^{(5)}\frac{\partial^{5}W}{\partial p_\eta^{5}}+\mathcal{O}(\hbar^{6}),
$$

with $V^{(5)}$ the fifth derivative of the potential and the coefficients the sine's, $\tfrac{1}{3!\,2^{2}}$ and $\tfrac{1}{5!\,2^{4}}$. **The expansion therefore terminates for a potential whose fifth and higher odd derivatives vanish**, which is to say a polynomial of degree at most four: a harmonic potential has $V'''=0$ and the classical equation is exact, a quartic has $V'''$ constant and $V^{(5)}=0$ and the one correction is exact, and a general potential has every order. The identity at fifth order was checked the same way as the third, symbolically, and returned $\Lambda^{5}(H,W)=V^{(5)}\partial_p^{5}W$ with no other term.

## The Zeroth Order: the Classical Drift

### The drift equation

**At order $\hbar^{0}$ the equation says that the phase-space density is constant along the classical flow.** With $\Lambda(HW)=\{H,W\}$ the Poisson bracket,

$$
\frac{\partial W}{\partial t}+\frac{p_\eta}{m}\frac{\partial W}{\partial r_\eta}
-\frac{\partial V}{\partial r_\eta}\frac{\partial W}{\partial p_\eta}=0 .
$$

**The three terms are one statement written three ways.** The first is the rate of change at a fixed phase-space point; the second is the transport of the density by the flow's velocity $\vec p/m$; the third is the change produced by the force. Their sum being zero says that the density at a point moving with the flow does not change — the statement that the flow of a collisionless fluid in phase space is incompressible.

**Why incompressible, in one line.** The phase-space velocity is $(\vec p/m,-\vec\nabla_\Phi V)$, and its divergence is $\partial_\eta(p_\eta/m)+\partial(-\partial_\eta V)/\partial p_\eta=0$ because the first term has no $r_\eta$ and the second no $p_\eta$. So Liouville's theorem is not an extra assumption; it is the observation that the drift vector field is divergenceless, which the corpus's $\delta_{\mu\nu}$ with all coefficients $+1$ makes manifest: the phase-space metric is flat and the flow is a rotation of it.

### The characteristics, and the corpus's flow

**The characteristics of the drift equation are the flow's worldlines, and this is where the hydrodynamic and the kinetic descriptions meet.** The characteristic equations are

$$
\frac{d r_\eta}{d t}=\frac{p_\eta}{m},
\qquad
\frac{d p_\eta}{d t}=-\frac{\partial V}{\partial r_\eta},
$$

which are Newton's equations for a particle of mass $m$. Written with the corpus's velocity element, the first is $v_{\Phi,\eta}=p_{\Phi,\eta}/m$ with the index low, and the second is the statement that the force changes the momentum and hence the rapidity.

**The identification is the content of [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html)'s remark that the flow is not a gradient.** A Wigner element supported on a single characteristic is the phase-space image of a fluid element, and the fluid's velocity field is the projection of the characteristic's velocity. When the element is supported on a *family* of characteristics, the projection is a flow with vorticity unless the family is a gradient family — which is exactly the distinction the spin-fluid article draws between the scalar case (a gradient, closed) and the spinor case (not a gradient, vortical). The kinetic picture makes the distinction visible: two Wigner elements with the same density and the same mean velocity but different velocity spreads have different vorticity in their projected flows.

### The corpus's letters for the drift

**The drift term's letters are the polar form's, with the factor $c$ where the length coordinate requires it.** Since $r'_t$ is a length and the temporal derivative acts through the material sector's imaginary direction, the time derivative is $c\,\partial/\partial r'_t$ in the units of the corpus, and the drift equation becomes

$$
c\,\frac{\partial W}{\partial r'_t}
+\frac{p_\eta}{m}\frac{\partial W}{\partial r_\eta}
-\frac{\partial V}{\partial r_\eta}\frac{\partial W}{\partial p_\eta}=0 .
$$

**The factor of $c$ is the corpus's rule for a rate against a length**, the same rule that gives $E=-c\,\partial S_{\tilde\Xi}/\partial r'_t$ in the polar-form article. A reader who writes $\partial/\partial r'_t$ without the $c$ has produced a dimensionally inconsistent equation and will find the drift speed off by that factor against the polar form's velocity. This is the single place where the corpus's units bite in this article, and it is worth stating plainly.

### On the mass shell, and off it

**The Wigner element is defined off the mass shell, and the physical states populate a shell whose width is the quantum potential.** The transform of article 4 integrates over all $\vec p$, so $\tilde W_\Xi$ has support wherever the overlap of the two field values has support — in general a neighbourhood of the shell and not the shell itself. The shell is not the classical one: the polar-form article's modification is

$$
\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2m\,Q_{\mathrm{qnt}},
\qquad
Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box_\Phi\lVert\tilde\Xi\rVert}{\lVert\tilde\Xi\rVert},
$$

so the width of the shell is set by $Q_{\mathrm{qnt}}$, which is itself of order $\hbar^{2}$.

**The two $\hbar^{2}$'s are the same $\hbar^{2}$, and this is the article's central observation.** The kinetic equation's correction is of order $\hbar^{2}$ and the shell's broadening is of order $\hbar^{2}$, and they are two readings of one fact: the state is not a point in phase space. The on-shell reading says that the energy of a fluid element at momentum $\vec p$ differs from the classical value by $Q_{\mathrm{qnt}}$; the off-shell reading says that the phase-space density is not supported on the classical shell. [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html) uses the first reading for the pressure and this article uses the second for the transport; the two must agree, and the agreement is checked in the equilibrium section below.

## The Correction at Order $\hbar^{2}$

### The equation

**Substituting the exact third-order term gives the kinetic equation with its first quantum correction.** From the two displays above,

$$
\frac{\partial W}{\partial t}
+\frac{p_\eta}{m}\frac{\partial W}{\partial r_\eta}
-\frac{\partial V}{\partial r_\eta}\frac{\partial W}{\partial p_\eta}
=-\frac{\hbar^{2}}{24}\,\frac{\partial^{3}V}{\partial r_\eta^{3}}\,
\frac{\partial^{3}W}{\partial p_\eta^{3}}
+\mathcal{O}(\hbar^{4}),
$$

with the sum over the spatial index $\eta$, every index low, and the sign as it falls out of the convention fixed above: $\Lambda(H,W)=V'W_p-(p_\eta/m)W_{r_\eta}$ reproduces the classical drift with the sign of the drift display, and the same convention fixes the sign of the correction. **A reader who reverses the orientation of $\Lambda$ reverses both signs together and gets an equivalent equation**; what cannot be done is to reverse one and not the other.

**Three readings of the right-hand side, in increasing order of interpretation.**

- It is a third derivative in momentum, so it is a *spreading* term: it redistributes the density among momenta without creating or destroying any.
- It is weighted by the third derivative of the potential, so it vanishes wherever the potential is locally quadratic. This is the exactness statement of the next subsection.
- It is the phase-space form of the quantum force: the Bohm force $-\vec\nabla_\Phi Q_{\mathrm{qnt}}$ and this term are the same $\hbar^{2}$, seen on the shell and off it. The identification is stated as an interpretation and the on-shell statement is the corpus's polar form; the mapping between them is a computation this article does not carry out.

### The moments the correction does not touch

**The correction is a total derivative in momentum, and three of its moments vanish identically.** Integrating by parts on a distribution that falls off at large momentum,

$$
\int d^{3}p\;\frac{\partial^{3}W}{\partial p_\eta^{3}}=0,
\qquad
\int d^{3}p\;p_\eta\,\frac{\partial^{3}W}{\partial p_\eta^{3}}=0,
\qquad
\int d^{3}p\;p_\eta p_\lambda\,\frac{\partial^{3}W}{\partial p_\eta^{3}}=0,
$$

so the zeroth, first and second moments of the equation are exactly the classical ones, at this order and at every higher order too. **The continuity equation is therefore exact**, not approximate:

$$
c\,\frac{\partial\rho_{\mathrm{num}}}{\partial r'_t}+\frac{\partial j_\eta}{\partial r_\eta}=0,
\qquad
\rho_{\mathrm{num}}=\int d^{3}p\;W,
\qquad
j_\eta=\int d^{3}p\;\frac{p_\eta}{m}W,
$$

with the $c$ of the length coordinate. The same is true of the momentum balance and of the pressure: the quantum correction does not touch them at this order, because a total momentum derivative cannot.

**The first moment that does not vanish is the third, and its value is one line.** With two more integrations by parts,

$$
\int d^{3}p\;p_\eta^{3}\,\frac{\partial^{3}W}{\partial p_\eta^{3}}=-6\int d^{3}p\;W=-6\rho_{\mathrm{num}},
$$

so the third moment of the equation acquires the correction $+\tfrac{\hbar^{2}}{4}V'''\rho_{\mathrm{num}}$. **This is where the quantum correction enters the hydrodynamic hierarchy**: not in the density, not in the velocity, not in the pressure, but in the heat-flow-type moment — the third moment, the first one the ideal fluid does not carry. A fluid description truncated at the pressure is therefore blind to the $\hbar^{2}$ correction of this order, and a description that keeps the heat flow is not.

### Exactness for a quadratic potential

**For a harmonic potential the right-hand side vanishes identically, so the classical drift equation is the exact quantum equation.** With $V=\tfrac12 m\omega^{2}r_\eta^{2}$ the third derivative is zero and every higher term of the sine expansion vanishes too, because the series terminates: a quadratic symbol has only the two monomials of the star product. This is the standard statement that the Wigner equation is exact for quadratic Hamiltonians, and it is the reason the harmonic oscillator is the test case of every Wigner computation.

**The exactness is visible in the stationary state without any expansion at all.** For the ground state the Wigner element is the Gaussian

$$
W_0(r,\vec p)=\frac{1}{\pi\hbar}
\exp\!\left(-\frac{m\omega\,r_\eta^{2}}{\hbar}-\frac{p_\eta^{2}}{m\omega\hbar}\right),
$$

whose position and momentum variances are $\sigma^{2}=\hbar/(2m\omega)$ and $\sigma_{p}^{2}=m\omega\hbar/2$. Its time derivative is zero because it is stationary, and the drift terms cancel identically:

$$
\frac{p_\eta}{m}\frac{\partial W_0}{\partial r_\eta}
-\frac{\partial V}{\partial r_\eta}\frac{\partial W_0}{\partial p_\eta}
=W_0\left(-\frac{p_\eta}{m}\frac{m\omega}{\hbar}r_\eta\cdot 2
+m\omega^{2}r_\eta\frac{2}{m\omega\hbar}p_\eta\right)=0,
$$

since the two coefficients are $-2p_\eta\omega r_\eta/\hbar$ and $+2p_\eta\omega r_\eta/\hbar$. **With $\hbar=m=\omega=1$ the numbers are $\sigma^{2}=\sigma_{p}^{2}=1/2$, $1/(m\sigma^{2})=2$ and $m\omega^{2}/\sigma_{p}^{2}=2$**, and the cancellation is the equality of those two numbers. This is the check that the drift display's coefficients are right: a factor of two error anywhere in it would leave $2$ against $1$ or $2$ against $4$, and the residual would be a non-zero multiple of $W_0$.

### What the correction is, and what it is not

**It is not a collision term.** A collision term is an integral operator built from the self-energy; it changes the number of particles in a phase-space cell and it drives the distribution to equilibrium. The $\hbar^{2}$ term does neither: it is a differential operator of third order in momentum, it conserves particle number, momentum and energy exactly, and it is present in the *free* equation, with no interaction and no bath. **The distinction matters for the second law**: a collision term is the only place where entropy production can enter a kinetic equation, and since the free equation has none, the entropy of a collisionless quantum fluid is conserved at this order — not increased.

**It is not the whole of the quantum correction to transport.** The term shown is the leading one in the gradient expansion of the free equation. The corrections from a finite collision width, from the off-shell behaviour of the self-energy, and from the $\hbar$ corrections to the collision integral are the Kadanoff–Baym structure's, and they are in [The Schwinger–Keldysh Formalism in Biquaternionic Form](the-schwinger-keldysh-formalism-in-biquaternionic-form.html). This article's term is the one that survives when the collision integral is switched off, which is the sense in which it is the "quantum Vlasov" correction.

**It is not a thermal pressure either.** The correction redistributes momentum at fixed particle number; a thermal pressure does work at fixed entropy and changes the density. The two objects have the same dimensions and different symmetries, and the mistake of identifying them is the one [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html) warns against in the stress language.

## The Relativistic Form

### The flow, in the corpus's letters

**Relativistically the drift is the contraction of the flow element with the gradient, and the mass shell is a constraint rather than an equation.** With the velocity element of the polar form, $\tilde V_{\Phi,\nu}=p_{\Phi,\nu}/m$ and $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$, the drift term becomes

$$
p_{\Phi,\nu}\,\frac{\partial W}{\partial R_\nu}
=\frac{E}{c}\,\frac{\partial W}{\partial r'_t}+p_{\Phi,\eta}\,\frac{\partial W}{\partial r_\eta},
$$

with the index low throughout. **No component is raised.** The two factors of the temporal term are separately imaginary and their product is real: $p_{\Phi,t}=iE/c$ on the polar form's display, and the temporal slot of the algebra's derivative is $\partial/\partial R_t=-i\,\partial/\partial r'_t$, so

$$
p_{\Phi,t}\,\frac{\partial}{\partial R_t}=\frac{iE}{c}\left(-i\frac{\partial}{\partial r'_t}\right)=\frac{E}{c}\,\frac{\partial}{\partial r'_t},
$$

whose rest-frame value is $mc\,\partial/\partial r'_t=m\,\partial/\partial t$, since $r'_t$ is a length and $r'_t=c\,t$. **The two $i$'s cancel, and that is why a drift built from two imaginary objects is a real equation.** A reader who writes $p_{\Phi,t}\,c\,\partial/\partial r'_t$ keeps one $i$ and makes the drift imaginary while also putting the $c$ in the wrong place; the cancellation is in the temporal slot of the derivative, not in the coefficient.

**The mass shell is the corpus's modified relation, and it enters as a constraint on the support.** The states populate the shell

$$
p_{\Phi,\nu}p_{\Phi,\nu}+m^{2}c^{2}+2m\,Q_{\mathrm{qnt}}=0,
$$

in the corpus's $\delta_{\mu\nu}$ form with the index low, and $Q_{\mathrm{qnt}}$ is the quantum potential with its minus sign. The constraint is not an equation of motion: it restricts where $\tilde W_\Xi$ has support, and the kinetic equation moves that support. **The two equations together are the relativistic pair**: a constraint that fixes the shell and a transport equation that moves the distribution along it.

### Off-shell, and why the corpus keeps it so

**A relativistic Wigner element cannot be supported on the shell alone if it is to carry a finite spread, and the corpus's off-shell emphasis is the honest bookkeeping of that fact.** In the non-relativistic case the drift equation alone determines the evolution and the energy is whatever the Hamiltonian says. In the relativistic case the four components of $p_{\Phi,\nu}$ are not independent: the shell ties the energy to the momentum, and a distribution with a momentum spread has an energy spread tied to it by the shell relation. **The tie is the $2mQ_{\mathrm{qnt}}$ term.** A state with zero quantum potential sits exactly on the classical shell and has a delta-supported energy; a state with a finite width has $Q_{\mathrm{qnt}}\neq0$ and a shell broadened by it.

**The consequence for the kinetic equation is that the drift term's temporal component is not independent of its spatial components.** Writing $p_{\Phi,t}$ from the shell,

$$
p_{\Phi,t}^{2}=-\left(\lvert\vec p\rvert^{2}+m^{2}c^{2}+2m\,Q_{\mathrm{qnt}}\right),
$$

and taking the branch with the positive energy, $p_{\Phi,t}=imc\sqrt{1+\lvert\vec p\rvert^{2}/(m^{2}c^{2})+2Q_{\mathrm{qnt}}/(mc^{2})}$. For small momentum and small quantum potential this is $imc\left(1+\lvert\vec p\rvert^{2}/(2m^{2}c^{2})+Q_{\mathrm{qnt}}/(mc^{2})\right)$, whose first correction reproduces the non-relativistic drift and whose second is the quantum potential's contribution to the temporal slot. **The expansion is the same $\hbar^{2}$ expansion**, read on the shell instead of off it, and this is the precise sense in which the two sections of this article are one computation.

### Temperature, and where it enters

**Nothing in the free kinetic equation knows about temperature; temperature enters through the state.** The drift and the $\hbar^{2}$ correction are properties of the equation, not of its solutions, and they are the same at every temperature. A thermal state is a particular solution — the one selected by the KMS condition of [The KMS Condition and the Biquaternion Framework](the-kms-condition-and-the-biquaternion-framework.html) — and the temperature appears in the boundary condition that selects it, not in the operator.

**The distinguishing feature of the thermal solution is that it is stationary in the appropriate sense, and the correction then cancels in the moments.** For a state in equilibrium in a static potential, the distribution depends on the momentum only through the combination $E$ that the shell fixes, and the third moment of the correction integrates to zero over a symmetric distribution. So the equilibrium heat flow is zero, as it must be, and the $\hbar^{2}$ correction does not produce a spurious equilibrium current. **This is the agreement the earlier section promised to check**: the on-shell broadening $Q_{\mathrm{qnt}}$ and the off-shell correction term are consistent precisely because the stationary solution annihilates the correction's odd moments.

## What the Kadanoff–Baym Structure Supplies

**The division of labour is worth stating as a list, because the two articles are easy to confuse.** [The Schwinger–Keldysh Formalism in Biquaternionic Form](the-schwinger-keldysh-formalism-in-biquaternionic-form.html) supplies the following, and this article supplies none of it:

| Supplied by the Schwinger–Keldysh article | Supplied here |
|---|---|
| The closed-time-path contour and the branch doubling | The free equation in one symbol |
| The Keldysh rotation and the $2\times2$ matrix of Green's functions | The Wigner element and its moments |
| The self-energy and with it the collision integral | The drift term and its characteristics |
| The Kadanoff–Baym equations and their kinetic component | The order-$\hbar^{2}$ correction and its moments |
| The fluctuation–dissipation relation and the thermal solution | The on-shell reading of the same $\hbar^{2}$ |
| The contour generating functional and the $2$-particle-irreducible action | The exactness statement for a quadratic potential |

**The free equation is the collisionless limit of the Kadanoff–Baym kinetic equation, and the limit is not a truncation of the formalism but a choice inside it.** Setting the self-energy to zero in the Keldysh equation leaves the free part, and that free part is what this article expands. So the relation between the two is not "approximate versus exact" but "one term of a sum versus the whole sum": a reader who needs the collision term goes to the Schwinger–Keldysh article, and a reader who wants to know what the collisionless part does at order $\hbar^{2}$ stays here.

**One thing this article should not be read as claiming.** It does not claim that the $\hbar^{2}$ term is the quantum correction to the *full* kinetic equation. It is the quantum correction to the free one. In a system with a finite collision rate the ordering of the terms can change — the gradient expansion and the collision-width expansion compete — and the conditions under which the gradient expansion is the correct one are stated in the standard references and not re-derived here.

## What Is Established and What Is Interpretation

**Established.** The Moyal-bracket equation for the Wigner element, and the exact identity $\Lambda^{3}(H,W)=V'''\partial_{p}^{3}W$ for a Hamiltonian at most quadratic in momentum, verified in a computer algebra system. The expansion $\tfrac{2}{\hbar}\sin(\hbar\Lambda/2)=\Lambda-\tfrac{\hbar^{2}}{24}\Lambda^{3}+\cdots$ and the resulting kinetic equation with its order-$\hbar^{2}$ term. The vanishing of the zeroth, first and second moments of that term, hence the exactness of the continuity equation, and the value $-6\rho_{\mathrm{num}}$ of its third moment. The exactness of the classical drift equation for a quadratic potential, checked analytically on the oscillator ground state with the numbers $\sigma^{2}=\sigma_{p}^{2}=1/2$, $1/(m\sigma^{2})=2$, $m\omega^{2}/\sigma_{p}^{2}=2$. The relativistic drift as a contraction with the flow element, and the shell relation $p_{\Phi,\nu}p_{\Phi,\nu}+m^{2}c^{2}+2mQ_{\mathrm{qnt}}=0$ with every index low.

**Interpretation.** That the $\hbar^{2}$ term is the phase-space form of the quantum force. The term is a fact of the expansion; its identification with $-\vec\nabla_\Phi Q_{\mathrm{qnt}}$ is a reading of it in the hydrodynamic variables, and the two are related by the moments — precisely, by the third moment and beyond, since the lower ones vanish. The article states the reading and marks it as one.

**Not claimed.** That the correction term is enough for a quantum kinetic theory of an interacting system. That the gradient expansion is the correct expansion at all densities and all coupling strengths. That the entropy production of a collisionless quantum fluid is nonzero — it is zero at this order, because there is no collision integral, and the entropy production of the interacting theory lives in the Schwinger–Keldysh article's collision term. That the Bohm force has been derived here from the kinetic equation.

## Summary

The Wigner element of the scalar field satisfies an exact equation whose generator is the Moyal bracket, $\partial_t W=\tfrac{2}{\hbar}\sin(\hbar\Lambda/2)(H,W)$ with $\Lambda=\overleftarrow{\partial_{r_\eta}}\overrightarrow{\partial_{p_\eta}}-\overleftarrow{\partial_{p_\eta}}\overrightarrow{\partial_{r_\eta}}$, every index low. Expanding the sine gives the classical drift at order $\hbar^{0}$ and one term at order $\hbar^{2}$; for a Hamiltonian at most quadratic in momentum the third-order term is exactly $\Lambda^{3}(H,W)=V'''\partial_{p}^{3}W$, so the expansion is not approximate at that order.

The drift equation, $\partial_t W+(p_\eta/m)\partial_{r_\eta}W-V'\partial_{p_\eta}W=0$, has the worldlines as its characteristics and is the statement that the phase-space flow is incompressible; its velocity field is divergenceless identically, which is Liouville's theorem rather than an assumption. With $r'_t$ a length, the temporal derivative carries a factor $c$, the same factor that gives $E=-c\,\partial S_{\tilde\Xi}/\partial r'_t$.

The correction is $-\tfrac{\hbar^{2}}{24}V'''\partial_{p}^{3}W$. It is a total momentum derivative, so its zeroth, first and second moments vanish identically and the continuity equation is exact; its third moment is $-6\rho_{\mathrm{num}}$, which is why the correction's hydrodynamic signature is in the heat flow and not in the pressure. It vanishes for a quadratic potential, where the classical drift equation is therefore exact — checked on the oscillator ground state, where the drift terms cancel because $1/(m\sigma^{2})$ and $m\omega^{2}/\sigma_{p}^{2}$ are both $2$ in units with $\hbar=m=\omega=1$.

Relativistically the drift is a contraction with the flow element and the shell is a constraint in the corpus's divided form, $E^{2}/c^{2}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2mQ_{\mathrm{qnt}}$. The two $\hbar^{2}$'s of the article — the shell's broadening and the kinetic correction — are one $\hbar^{2}$, read on the shell and off it. Temperature enters only through the state, and the equilibrium solution annihilates the correction's odd moments, so there is no spurious equilibrium heat flow. The collision integral, its self-energy and the entropy production it carries are [The Schwinger–Keldysh Formalism in Biquaternionic Form](the-schwinger-keldysh-formalism-in-biquaternionic-form.html)'s, and are cited rather than repeated.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde W_\Xi(r,\vec p)$ | Biquaternionic Wigner element |
| $W$ | Its scalar representative in the fixed-unit case |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $\tilde\Xi$ | Scalar field, an element of $\mathbb{B}$ |
| $\lVert\tilde\Xi\rVert^{2}=\rho_{\mathrm{num}}$ | Amplitude squared, and the proper density |
| $S_{\tilde\Xi}$ | Action of the polar form |
| $m$, $c$ | Mass and speed of light in the medium |
| $\hbar$ | Action quantum |
| $k_m$ | Mass wave number |
| $r_\eta$, $p_\eta$ | Spatial components of position and momentum; indices low |
| $r'_t$ | Temporal coordinate of the material sector, a length |
| $R_\mu$, $\partial/\partial R_\mu$ | Derivative coordinate, with $\partial/\partial R_t=-i\,\partial/\partial r'_t$ and $\partial/\partial R_\eta=\partial/\partial r_\eta$ |
| $E=-c\,\partial S_{\tilde\Xi}/\partial r'_t$ | Energy |
| $p_{\Phi,\nu}$ | Components of the flow momentum element |
| $\tilde V_{\Phi,\nu}=p_{\Phi,\nu}/m$ | Components of the velocity element |
| $\Lambda$ | The bidifferential operator of the Moyal bracket |
| $H$ | Hamiltonian symbol, $\lvert\vec p\rvert^{2}/(2m)+V$ |
| $V$ | Potential; $V'''$ its third derivative |
| $Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\Box_\Phi\lVert\tilde\Xi\rVert/\lVert\tilde\Xi\rVert$ | Quantum potential, with the minus sign |
| $\omega$ | Oscillator frequency |
| $\sigma^{2}$, $\sigma_{p}^{2}$ | Position and momentum variances of a Gaussian |
| $W_0$ | Wigner element of the oscillator ground state |
| $\rho_{\mathrm{num}}=\int d^{3}p\,W$ | Proper density as a marginal |
| $j_\eta=\int d^{3}p\,(p_\eta/m)W$ | Current density as a first moment |
| $\delta_{\mu\nu}$ | The metric; no raised indices |
| $\mathcal{O}(\hbar^{4})$ | The remainder of the sine expansion; for a separable Hamiltonian the next explicit term is the $\hbar^{4}$ one, $\frac{\hbar^{4}}{1920}V^{(5)}\partial_{p_\eta}^{5}W$ |

## Further Reading

- J. E. Moyal, "Quantum mechanics as a statistical theory," *Proceedings of the Cambridge Philosophical Society* **45** (1949) 99–124, for the bracket and the expansion.
- H.-T. Elze, M. Gyulassy and D. Vasak, "Transport equations for the Wigner function," *Nuclear Physics B* **276** (1986) 706–728, for the gradient expansion and the quantum Vlasov equation.
- D. Vasak, M. Gyulassy and H.-T. Elze, "Quantum transport equations for the quark-gluon plasma," *Annals of Physics* **173** (1987) 462–492, for the matrix-valued case and the $\hbar$ counting.
- W. Botermans and R. Malfliet, "Quantum transport theory of nuclear matter," *Physics Reports* **198** (1990) 115–210, for the off-shell and gradient bookkeeping together.
- L. P. Kadanoff and G. Baym, *Quantum Statistical Mechanics* (Benjamin, 1962), for the equations whose collisionless part this article expands.
- C. Zachos, D. Fairlie and T. Curtright, *Quantum Mechanics in Phase Space* (World Scientific, 2005), for the star product's systematic treatment and its semiclassical expansion.
- P. Carruthers and F. Zachariasen, "Quantum collision theory with phase-space distributions," *Reviews of Modern Physics* **55** (1983) 245–285, for the phase-space reading of the quantum force.
- The companion articles: [The Wigner Function in Biquaternionic Form](the-wigner-function-in-biquaternionic-form.html), [The Schwinger–Keldysh Formalism in Biquaternionic Form](the-schwinger-keldysh-formalism-in-biquaternionic-form.html), [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html), and [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html).
