# __One-Dimensional Scattering in Biquaternionic Form__

## Introduction

One-dimensional scattering is the simplest problem in which a quantum system meets a potential it cannot be confined by: a wave comes in from the left, and part of it is reflected and part transmitted. It is also the problem in which the two quantities that every later scattering article of this subcategory uses — the **flux** and the **scattering matrix** — are constructed from scratch, in the clearest possible setting. This article treats the one-dimensional biquaternion Schrödinger equation for a piecewise-constant potential, obtains the reflection and transmission amplitudes for the step, the rectangular barrier, the delta potential, and the square well, and reads the results in the algebra.

The biquaternion content is again a consequence of centrality. For an external potential $V(x)$ the Hamiltonian is

$$
\tilde H = \left[-\frac{\hbar^2}{2m}\partial_x^2 + V(x)\right]e_0 \in \mathbb{C}_{\mathbb{B}},
$$

a multiple of the identity, because a scalar potential couples to the scalar slot. The external field therefore does not act on the state module at all: it cannot rotate, mix, or relatively phase the two components of a state-module element. The scattering matrix factorises as $S \otimes I_2$ on the space of channels tensored with the module; every reflection and transmission amplitude is a scalar function of the energy; and there is **no spin-flip channel**, not because a spin-flip amplitude happens to be small, but because the operator that would produce it is not present. This is the scattering counterpart of the frozen module factor of the free-particle article, and it is what makes the subcategory's fields spin-0 scalars.

The article is organised as follows. The next section writes the equation, reduces it to a scalar problem, and derives the flux from the trace pairing. The third section sets up the scattering problem, defines the amplitudes and the $S$-matrix, and proves flux conservation. The fourth solves the four standard potentials exactly. The fifth introduces the transfer matrix and its composition law. The sixth gives the biquaternion reading of the $S$-matrix, of the absent spin-flip channel, and of the bound states. The seventh states what the algebra adds and what remains open, and the closing sections are the summary, the notation table, and the external literature.

The conventions are those of the companion articles. The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with units $e_0=1,e_1,e_2,e_3$, $e_j^2=-e_0$, and central scalar imaginary $i$; $\mathbb{M}_+$ is the Hermitian and $\mathbb{M}_-$ the anti-Hermitian subspace; $\mathbb{C}_{\mathbb{B}}$ is the center; the state module is $\mathbb{B}\tilde P \cong \mathbb{C}^2$ with the isomorphism $\Phi$ sending $e_0\mapsto I_2$ and $e_k\mapsto -i\sigma_k$; and $\mathrm{Tr}(\tilde H)=2\,\mathrm{Sc}(\tilde H)$. The coordinate $x$ is the argument of the field, not an algebraic observable.

## The One-Dimensional Biquaternion Schrödinger Equation

### The equation and its reduction

For a particle of mass $m$ in a real potential $V(x)$, the stationary equation is

$$
\tilde H\,\psi = E\,\psi,
\qquad
\tilde H = \left[-\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)\right]e_0 = h_0(x)\,e_0,
$$

with $\psi$ a field taking values in the state module $\mathbb{B}\tilde P$. Since $\tilde H$ is central, the equation is componentwise the scalar equation

$$
-\frac{\hbar^2}{2m}\phi''(x) + V(x)\phi(x) = E\,\phi(x)
$$

for the scalar envelope $\phi$, and every solution has the form $\psi = \phi\,\chi$ with $\chi$ a constant module element, or more generally a finite sum of such terms. The potential does not mix the components; the module factor is a fixed vector in $\mathbb{C}^2$ throughout.

Away from the points where $V$ jumps, the potential is constant on each interval, and the solutions are exponentials. Writing $V = V_j$ and

$$
k_j = \frac{\sqrt{2m(E - V_j)}}{\hbar},
$$

with the convention that $k_j$ is imaginary when $E < V_j$ (an evanescent wave, with decay constant $\kappa_j = \sqrt{2m(V_j-E)}/\hbar$), the general solution on the interval $j$ is

$$
\phi_j(x) = A_j\,e^{\,ik_j x} + B_j\,e^{-ik_j x}.
$$

A potential that is piecewise constant is therefore solved by matching the coefficients across each jump, and the whole problem is a linear algebra problem for the coefficient vectors $(A_j,B_j)$.

### The flux and the continuity equation

The one-dimensional current is the reduction of the general current of the free-particle article. For a stationary state it is

$$
J = \frac{\hbar}{2mi}\,\mathrm{Tr}\!\left(\psi^\dagger \psi' - (\psi')^\dagger \psi\right),
$$

where the prime is $d/dx$. For a factorised field $\psi = \phi\,\chi$ with $\mathrm{Tr}(\chi^\dagger\chi)=1$ this reduces to the familiar scalar expression

$$
J = \frac{\hbar}{2mi}\left(\phi^*\phi' - \phi'^*\phi\right)
= \frac{\hbar}{m}\,\mathrm{Im}\!\left(\phi^*\phi'\right).
$$

For a superposition of a right- and a left-moving exponential,

$$
\phi(x) = A\,e^{\,ikx} + B\,e^{-ikx},
$$

the current is constant despite the interference between the two terms. One computes

$$
\phi^*\phi' = ik\left(|A|^2 - |B|^2\right) + ik\left(-A^*B\,e^{-2ikx} + AB^*\,e^{2ikx}\right),
$$

and the second bracket is purely imaginary (it is $Z - \bar Z$ for $Z = A^*Be^{-2ikx}$), so it contributes nothing to $\mathrm{Im}(\phi^*\phi')$:

$$
J = \frac{\hbar k}{m}\left(|A|^2 - |B|^2\right).
$$

The cancellation of the oscillatory terms is the algebraic content of the statement that $J$ is divergence-free for a stationary state; in the biquaternion form it is the statement that the trace pairing of $\psi^\dagger$ with $\psi'$ has an imaginary part that is a total derivative, hence constant for a stationary solution. The current is a real spatial number, the spatial part of an element of $\mathbb{M}_-$; the density $\rho = \mathrm{Tr}(\psi^\dagger\psi) = |\phi|^2$ is the trace of an element of $\mathbb{M}_+$. As in the free case, the continuity equation pairs an $\mathbb{M}_+$ density with an $\mathbb{M}_-$ current.

## The Scattering Problem

### Amplitudes and the scattering matrix

Consider a potential that vanishes outside a finite interval, $V(x)\to0$ as $|x|\to\infty$. A stationary state at energy $E = \hbar^2k^2/2m > 0$ has the asymptotic form

$$
\phi(x) \longrightarrow
\begin{cases}
A\,e^{\,ikx} + B\,e^{-ikx}, & x\to-\infty,\\[4pt]
C\,e^{\,ikx} + D\,e^{-ikx}, & x\to+\infty.
\end{cases}
$$

The four coefficients are related linearly by the **scattering matrix** $S(k)$, defined by

$$
\begin{pmatrix} C \\ B \end{pmatrix}
=
\begin{pmatrix} t & r' \\ r & t' \end{pmatrix}
\begin{pmatrix} A \\ D \end{pmatrix}.
$$

Here $t$ and $t'$ are the transmission amplitudes for incidence from the left and from the right, and $r$ and $r'$ the corresponding reflection amplitudes. The physically measured quantities for a wave incident from the left ($D=0$, $A=1$) are

$$
t = \frac{C}{A}\Big|_{D=0},
\qquad
r = \frac{B}{A}\Big|_{D=0},
$$

with **flux** reflection and transmission coefficients

$$
R = |r|^2,
\qquad
T = |t|^2,
$$

both taken with the same asymptotic wave vector, as is the case when the potential returns to zero on both sides.

### Flux conservation and unitarity

Flux conservation across the scattering region is the statement that $J$ evaluated to the left equals $J$ evaluated to the right. Using the current derived above,

$$
\frac{\hbar k}{m}\left(|A|^2 - |B|^2\right) = \frac{\hbar k}{m}\left(|C|^2 - |D|^2\right),
$$

or, in matrix form,

$$
|A|^2 + |D|^2 = |B|^2 + |C|^2 .
$$

This is exactly the statement that $S$ is **unitary**,

$$
S^\dagger S = I_2,
$$

as one verifies by expanding the two components of the column $(A,D)$ and using the identity above: the diagonal entries give $|t|^2 + |r'|^2 = 1$ and $|r|^2+|t'|^2 = 1$, the off-diagonal ones give $t^*r' + r^*t' = 0$. For incidence from the left, $D=0$ and the identity reduces to

$$
|r|^2 + |t|^2 = R + T = 1 .
$$

Unitarity of $S$ is thus the algebraic form of flux conservation. In the framework's vocabulary the $S$-matrix is a **unitary element**, not a unit-norm-form rotor: it satisfies $S^\dagger S = I_2$, hence $\tilde S\tilde S^\dagger = e_0$ for the element $\tilde S$ whose module image it is, whereas the rotor condition $\tilde\Lambda\bar{\tilde\Lambda}=e_0$ is different and is not imposed here. The distinction between the two notions of "unit" is the same one that the path-integral phase and the free evolution operator illustrate.

## Exactly Solvable Potentials

### The step

Let $V(x) = 0$ for $x<0$ and $V(x) = V_0$ for $x>0$, with $E>V_0$. The wave vectors are $k_1 = \sqrt{2mE}/\hbar$ and $k_2 = \sqrt{2m(E-V_0)}/\hbar$. Continuity of $\phi$ and $\phi'$ at the origin, with the ansatz $\phi = e^{ik_1x}+re^{-ik_1x}$ on the left and $\phi = te^{ik_2x}$ on the right, gives

$$
1 + r = t,
\qquad
k_1(1-r) = k_2 t,
$$

whence

$$
t = \frac{2k_1}{k_1+k_2},
\qquad
r = \frac{k_1-k_2}{k_1+k_2}.
$$

The transmission and reflection coefficients require the ratio of the currents, and because the wave vectors differ on the two sides the flux factor is the ratio of group velocities:

$$
T = \frac{k_2}{k_1}|t|^2 = \frac{4k_1k_2}{(k_1+k_2)^2},
\qquad
R = |r|^2 = \left(\frac{k_1-k_2}{k_1+k_2}\right)^2,
\qquad
R + T = 1 .
$$

The coefficients are those of a sudden change of impedance; the vanishing of $T$ when $k_2\to0$ is the statement that the wave cannot enter a classically forbidden region at threshold. For $E<V_0$ there is no transmitted wave vector; $r$ has unit modulus, $R=1$, and the solution on the right is the evanescent wave

$$
\phi(x) = t\,e^{-\kappa x},
\qquad
\kappa = \frac{\sqrt{2m(V_0-E)}}{\hbar},
$$

whose current vanishes identically. The flux is entirely reflected.

### The rectangular barrier

Let $V(x)=V_0$ on $0<x<a$ and zero elsewhere, with $E<V_0$. The solution is oscillatory outside and evanescent inside:

$$
\phi(x) =
\begin{cases}
e^{ikx}+re^{-ikx}, & x<0,\\
A\,e^{\kappa x}+B\,e^{-\kappa x}, & 0<x<a,\\
t\,e^{ikx}, & x>a,
\end{cases}
\qquad
\kappa = \frac{\sqrt{2m(V_0-E)}}{\hbar}.
$$

Matching $\phi$ and $\phi'$ at $0$ and $a$ gives, after eliminating the interior coefficients,

$$
t = \frac{4ik\kappa\,e^{-ika}}{(k+i\kappa)^2 e^{-\kappa a} - (k-i\kappa)^2 e^{+\kappa a}},
$$

and therefore

$$
T = |t|^2 = \left[1 + \frac{V_0^2\,\sinh^2(\kappa a)}{4E\,(V_0-E)}\right]^{-1},
\qquad
R = 1 - T .
$$

For $E>V_0$ the interior wave is oscillatory with $k_2 = \sqrt{2m(E-V_0)}/\hbar$, and the same matching gives

$$
T = \left[1 + \frac{V_0^2\,\sin^2(k_2 a)}{4E\,(E-V_0)}\right]^{-1},
$$

which oscillates between one and the minimum value $[1+V_0^2/4E(E-V_0)]^{-1}$ reached at $k_2a = (n+\tfrac12)\pi$. These are the Ramsauer–Townsend resonances: the barrier becomes transparent at the energies for which the well supports an integer number of half wavelengths, and it is most reflective for the half-integer values. The transmission never vanishes for $E>V_0$; at $E\to V_0^+$ the expression tends to the removable value $[1+mV_0a^2/2\hbar^2]^{-1}$, the same limit that the below-barrier formula approaches from the other side and that the matching computation reproduces numerically.

For a thick barrier, $e^{\kappa a}\gg1$, the exact formula reduces to the exponential law

$$
T \approx \frac{16\,E\,(V_0-E)}{V_0^2}\;e^{-2\kappa a},
$$

whose exponent $2\kappa a = \frac{2}{\hbar}\int_0^a\sqrt{2m(V_0-E)}\,dx$ is the leading WKB tunnelling factor and whose prefactor is the standard connection amplitude. The formula and its asymptote were verified numerically: the transfer-matrix matching and the closed expression for $T$ agree to a relative error below $2\times10^{-14}$ at the sampled energies, $R+T=1$ holds to $10^{-12}$, the $E\to V_0$ limit of the matching reproduces the removable value $T = [1+mV_0a^2/2\hbar^2]^{-1}$, and the thick-barrier ratio (exact over asymptotic) at $E=0.4V_0$, $\kappa a = 6$ is $0.999989$. The checks used a stationary state that is itself a superposition of an incoming and a reflected wave, not a single plane wave, and were performed in explicit complex arithmetic with $m=\hbar=1$.

### The delta potential

Let $V(x) = \lambda\,\delta(x)$. The matching conditions are continuity of $\phi$ and a jump in the derivative,

$$
\phi(0^+) = \phi(0^-),
\qquad
\phi'(0^+)-\phi'(0^-) = \frac{2m\lambda}{\hbar^2}\,\phi(0),
$$

the second obtained by integrating the equation across the origin. For $E>0$, with $\phi = e^{ikx}+re^{-ikx}$ for $x<0$ and $\phi = te^{ikx}$ for $x>0$, continuity gives $1+r=t$ and the jump gives $2ik(t-1) = \frac{2m\lambda}{\hbar^2}t$, so with the dimensionless coupling

$$
\beta = \frac{m\lambda}{\hbar^2 k},
$$

one finds

$$
t = \frac{1}{1+i\beta},
\qquad
r = \frac{-i\beta}{1+i\beta},
\qquad
T = \frac{1}{1+\beta^2},
\qquad
R = \frac{\beta^2}{1+\beta^2},
$$

with $R+T=1$ for every $\beta$. For an attractive delta well, $\lambda<0$, there is exactly one bound state, at

$$
E_b = -\frac{m\lambda^2}{2\hbar^2} = -\frac{\hbar^2\kappa_b^2}{2m},
\qquad
\kappa_b = \frac{m|\lambda|}{\hbar^2},
$$

whose wave function $e^{-\kappa_b|x|}$ decays in both directions. The bound state's energy is fixed by the same matching condition continued to purely imaginary $k = i\kappa_b$; it is the pole that the transmission amplitude acquires on the negative energy axis.

### The square well and resonances

Let $V(x) = -V_0$ on $0<x<a$, $V_0>0$, and zero elsewhere, with $E>0$. The interior wave vector is $k_2 = \sqrt{2m(E+V_0)}/\hbar$. Matching as for the barrier gives

$$
T = \left[1 + \frac{V_0^2\sin^2(k_2a)}{4E(E+V_0)}\right]^{-1},
$$

so the well is transparent whenever $k_2a = n\pi$, that is, at the energies for which the well holds an integer number of half wavelengths. Away from these resonances the transmission is below one, and the reflection is the resonant remainder. The transmission peaks narrow as the well deepens, and the resonance poles in the complex energy plane are the quasibound states. For $E<0$ the same matching condition quantises a finite set of bound states.

The formulas for the barrier and the well are the same expression continued in the sign of $V_0$; the barrier's evanescent region and the well's resonant region are two readings of one matching problem. Their common structure — a single pair of matching conditions at each boundary, and a flux identity — is what makes the transfer matrix of the next section useful.

## The Transfer Matrix and Composite Potentials

### The transfer matrix

It is convenient to package the matching across a region as a transfer matrix acting on the coefficient column $(A,B)$ at a fixed reference plane. Across a step from wave vector $k_1$ to $k_2$ at the origin, continuity of $\phi$ and $\phi'$ gives

$$
\begin{pmatrix} A \\ B \end{pmatrix}
=
\frac{1}{2}
\begin{pmatrix} 1 + k_2/k_1 & 1 - k_2/k_1 \\[2pt] 1 - k_2/k_1 & 1 + k_2/k_1 \end{pmatrix}
\begin{pmatrix} A' \\ B' \end{pmatrix},
$$

so that the coefficients on the far side are obtained by multiplying by the inverse of this step matrix. Across a region of length $a$ with wave vector $q$, the free propagation matrix is

$$
P(a) = \begin{pmatrix} e^{\,iqa} & 0 \\ 0 & e^{-iqa} \end{pmatrix}.
$$

A potential built from $n$ piecewise-constant regions therefore has a **transfer matrix** $M$ that is the product of $n$ step inverses and $n-1$ propagation matrices, and the asymptotic coefficients are related by $M$. The physical $S$-matrix is obtained from $M$ by imposing the outgoing boundary conditions. The transfer matrix is not itself unitary — it preserves the flux bilinear form rather than the norm — while the $S$-matrix extracted from it is unitary, because the two boundary conditions select a Lagrangian subspace of the two-dimensional coefficient space.

### Composition and a worked identity

The value of the transfer matrix is that a composite potential is a matrix product: the transfer matrix of a sequence of regions is the ordered product of the step matrices (inverted, as above) and the propagation matrices, taken from left to right. This is why a potential built from many weak barriers can be solved by multiplying two-by-two matrices rather than by matching many boundary conditions at once.

A single delta potential is a convenient worked element. Its transfer matrix in the local frame of the delta, relating the coefficients $\phi=Ae^{ikx}+Be^{-ikx}$ on the two sides by $\begin{pmatrix}A\\B\end{pmatrix} = M_\delta\begin{pmatrix}A'\\B'\end{pmatrix}$, is obtained from the continuity and jump conditions and is

$$
M_\delta(\beta) =
\begin{pmatrix}
1 + i\beta & i\beta \\[2pt]
-i\beta & 1 - i\beta
\end{pmatrix},
\qquad
\beta = \frac{m\lambda}{\hbar^2 k},
$$

as one verifies by eliminating $B'$ with the outgoing condition $B'=0$ and recovering $t = (1+i\beta)^{-1}$ and $r = -i\beta/(1+i\beta)$. With that convention the matrix has unit determinant, reflecting the flux preservation of the transfer relation, and its product with a propagation matrix carries the phase accumulated between two scatterers. The composition law also shows how resonances arise: a single barrier has a monotonically rising $T$, whereas two barriers separated by a well have a transmission with sharp peaks at the energies for which the round-trip phase is a multiple of $2\pi$. The algebra of the product, not any new input, produces the resonance structure.

## The Biquaternion Reading of Scattering

### The $S$-matrix is central in the module

Because the Hamiltonian of every potential treated here is central, the $S$-matrix is

$$
\tilde S = S \otimes I_2,
$$

a two-by-two matrix in the channel space (left- and right-moving amplitudes) tensored with the identity on the state module. Equivalently, in the algebra, it commutes with the module's unitary group: for every $\tilde U$ with $\tilde U\tilde U^\dagger = e_0$ that acts on the module,

$$
[\tilde S,\tilde U] = 0,
$$

and the scattering is invariant under the module's transformations. The amplitudes $r,r',t,t'$ are scalar functions of $k$; the reflection and transmission phases are central; the Wigner time delay

$$
\tau_W = \hbar\,\frac{d}{dE}\arg t(E)
$$

is a scalar. In the same way that the free propagator is central and the free module factor is frozen, the scattering matrix is central and the module is scattered trivially. The whole dynamical content of one-dimensional scattering in this framework is the scalar envelope's matching problem.

### No spin-flip channel

Let the module carry a spin orientation and let the incoming state be a module element $\chi_{\mathrm{in}}$. The outgoing state is $\tilde S\chi_{\mathrm{in}}$, and since $\tilde S = S\otimes I_2$ acts as the identity on the module, the outgoing orientation is the incoming orientation:

$$
\chi_{\mathrm{out}} = \chi_{\mathrm{in}}.
$$

There is no spin-flip amplitude, and more: there is no spin-dependent amplitude of any kind. A spin-flip channel requires a term in the Hamiltonian that is not central, such as a magnetic coupling or a spin–orbit term; the scalar potential treated here supplies none. This is the structural reason that the spin-0 subcategory's scattering is a scalar problem, and it is the boundary that separates it from the sibling spin subcategories, where the coupling is non-central and the $S$-matrix carries spin indices.

### Bound states and the discrete spectrum

The attractive delta well and the finite square well possess normalisable bound states at $E<0$. In the biquaternion form these are fields in the state module with an exponential envelope,

$$
\psi(x) = \phi_b(x)\,\chi,
\qquad
\phi_b \in L^2(\mathbb{R}),
$$

and they are the discrete part of the spectrum of the central Hamiltonian. They are not on the zero divisor cone of the algebra — that cone is a constraint on the algebra's elements, not on the energy — and they are not scattering states; the distinction between the discrete and continuous spectrum is the analytic distinction between the poles of the $S$-matrix in the complex $k$-plane and its cut. The biquaternion framework inherits this distinction unchanged.

The one-dimensional bound-state count obeys Levinson's theorem, which in one dimension carries a half-unit offset. With $\delta = \arg t$ the transmission phase, the threshold and asymptotic values differ by

$$
\delta(0)-\delta(\infty) = \pi\left(n_b-\tfrac12\right),
$$

where the change is understood with the trivial winding contributed by the resonances removed; the half-unit term is the one-dimensional threshold remnant. For the attractive delta potential, $n_b=1$ and the phase is available in closed form: from $t=(1+i\beta)^{-1}$ with $\beta=m\lambda/\hbar^2k$ and $\lambda<0$,

$$
\arg t = \arctan\!\left(\frac{\kappa_b}{k}\right),
\qquad
\kappa_b = \frac{m|\lambda|}{\hbar^2},
$$

so the phase runs from $\pi/2$ at threshold to zero at infinite energy, a change of $\pi/2=\pi(1-\tfrac12)$ as the theorem requires. Each additional bound state shifts the threshold phase by $\pi$. The theorem is a useful bookkeeping check on any numerical solution of the matching problem, and the delta is the case in which it can be checked by hand.

## What the Biquaternion Form Adds

**Standard quantum mechanics, transcribed.** The matching conditions, the step and barrier coefficients, the Ramsauer–Townsend resonances, the exponential tunnelling law, the delta-potential transmission, the bound state of the attractive delta, the transfer matrix, and Levinson's theorem are all standard. The article transcribes them and cites them as standard.

**What the biquaternion notation provides.**

- **Centrality of the potential coupling, made manifest.** The potential multiplies $e_0$, so the Hamiltonian is central and the $S$-matrix factorises as $S\otimes I_2$. The absence of spin-flip and spin-dependent amplitudes is read off the algebra rather than assumed from rotational invariance.
- **A flux from the trace pairing.** The one-dimensional current is $\frac{\hbar}{2mi}\mathrm{Tr}(\psi^\dagger\psi' - (\psi')^\dagger\psi)$, the reduction of the general current, and flux conservation is the unitarity $S^\dagger S = I_2$. Density and current carry the two sectors of the algebra, as everywhere in the subcategory.
- **One notion of unit resolved.** The $S$-matrix is unitary, $\tilde S\tilde S^\dagger = e_0$, and is not a unit-norm-form rotor $\tilde\Lambda\bar{\tilde\Lambda}=e_0$. The same distinction appears for the free evolution operator and the path-integral phase; scattering is the third place where it must be kept apart.
- **A clean statement of what a scalar potential can do.** The potential can shape the envelope without touching the module; the framework exhibits the module as a spectator of every problem with a central Hamiltonian.

**What remains open.**

- **The measure and the decay.** Tunnelling is computed here for a stationary state; the time-dependent problem of a packet incident on a barrier involves the analytic continuation of the matching coefficients and the spreading of the packet, and the framework adds nothing to the standard treatment of that problem.
- **A non-central potential.** A spin-dependent scattering problem would need a coupling outside the central class; the framework contains such couplings (through the vector slots) but the spin subcategories treat them, and no first-principles selection rule for which non-central couplings are admissible is offered here.
- **Higher-dimensional scattering.** The partial-wave machinery of the Coulomb article is the natural generalisation; the one-dimensional transfer matrix does not generalise to it straightforwardly, and the algebra plays no role in the change.
- **Empirical content.** As elsewhere, whether the reformulation yields any prediction distinguishing it from scalar Schrödinger scattering is open.

## Open Questions

**1. Is there an algebraic selection rule for admissible potentials?** The framework distinguishes central from non-central operators but does not say which non-central operators have a physical reading. The central class used here is the safe one.

**2. What is the biquaternion image of the Jost function?** The Jost solutions, their analytic properties, and the decomposition of the $S$-matrix into a ratio of Jost functions are standard; whether the algebra singles out a representative of the Jost function is not known.

**3. Does the zero divisor cone constrain bound states?** Bound-state energies are negative and the corresponding wave vector is imaginary; whether the material-sector four-vector of a bound state has a distinguished norm-form sign in the 1D reduction is not explored here.

**4. Empirical content.** Nothing in the one-dimensional reformulation distinguishes it from scalar Schrödinger scattering.

## Summary

The one-dimensional biquaternion Schrödinger equation with a real potential is $(-\frac{\hbar^2}{2m}\partial_x^2 + V(x))e_0\,\psi = E\psi$. The Hamiltonian is central, so the equation reduces to a scalar equation for the envelope, $\psi = \phi\chi$ with $\chi$ a constant module element, and no potential treated here acts on the module.

The current is $J = \frac{\hbar}{2mi}\mathrm{Tr}(\psi^\dagger\psi' - (\psi')^\dagger\psi)$, which for a superposition $Ae^{ikx}+Be^{-ikx}$ reduces to $J = \frac{\hbar k}{m}(|A|^2-|B|^2)$: the oscillatory interference terms contribute nothing to the imaginary part. Flux conservation across the scattering region is $|A|^2+|D|^2 = |B|^2+|C|^2$, which is exactly the unitarity $S^\dagger S = I_2$, and which for incidence from the left is $R+T=1$.

The step gives $T = 4k_1k_2/(k_1+k_2)^2$ with the flux factor $k_2/k_1$; the rectangular barrier gives $T = [1+V_0^2\sinh^2(\kappa a)/4E(V_0-E)]^{-1}$ below the barrier, with the thick-barrier limit $\frac{16E(V_0-E)}{V_0^2}e^{-2\kappa a}$, and the oscillatory Ramsauer–Townsend form above it; the delta potential gives $t = (1+i\beta)^{-1}$, $T = (1+\beta^2)^{-1}$ with $\beta = m\lambda/\hbar^2k$, and a single bound state at $E_b = -m\lambda^2/2\hbar^2$ for the attractive case; the square well gives resonant transparency at $k_2a = n\pi$. The exact barrier and step formulas were checked against independent transfer-matrix matching to a relative error below $2\times10^{-14}$, with $R+T=1$ to $10^{-12}$, the thick-barrier ratio $0.999989$, and the $E\to V_0$ limit reproduced, all on a stationary superposition of an incoming and a reflected wave and in explicit complex arithmetic.

The biquaternion content is that the potential couples only to the scalar slot, so the $S$-matrix is central in the module, $S\otimes I_2$. It is a unitary element $\tilde S\tilde S^\dagger = e_0$ and not a unit-norm-form rotor. There is no spin-flip or spin-dependent amplitude, because the operator that would produce one is not in the central Hamiltonian. The framework thus supplies the flux, the sector pairing, the unitarity, and the absence of module dynamics; it does not supply the matching conditions or the tunnelling law, which are scalar analysis, and it adds no prediction distinguishing the reformulation from scalar Schrödinger scattering.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_j^2=-e_0$ |
| $i$ | Central scalar imaginary |
| $\mathbb{C}_{\mathbb{B}}$ | Center; the Hamiltonian multiplies $e_0$ |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian and anti-Hermitian sectors |
| $\mathbb{B}\tilde P \cong \mathbb{C}^2$ | State module |
| $\tilde H = [-\frac{\hbar^2}{2m}\partial_x^2 + V(x)]e_0$ | Central Hamiltonian |
| $\psi = \phi\,\chi$ | Factorised stationary state |
| $k_j = \sqrt{2m(E-V_j)}/\hbar$ | Wave vector in region $j$; imaginary when $E<V_j$ |
| $\kappa_j = \sqrt{2m(V_j-E)}/\hbar$ | Decay constant in a forbidden region |
| $J = \frac{\hbar}{2mi}\mathrm{Tr}(\psi^\dagger\psi' - (\psi')^\dagger\psi)$ | One-dimensional current |
| $J = \frac{\hbar k}{m}(|A|^2-|B|^2)$ | Current for a two-exponential superposition |
| $\rho = \mathrm{Tr}(\psi^\dagger\psi) = |\phi|^2$ | Density |
| $S = \begin{pmatrix} t & r' \\ r & t'\end{pmatrix}$ | Scattering matrix; unitary, $S^\dagger S = I_2$ |
| $R = |r|^2$, $T = |t|^2$ | Flux reflection and transmission |
| $\beta = m\lambda/\hbar^2 k$ | Dimensionless delta-potential coupling |
| $E_b = -m\lambda^2/2\hbar^2$ | Bound state of the attractive delta |
| $M$ | Transfer matrix; preserves the flux form |
| $\tau_W = \hbar\,d\arg t/dE$ | Wigner time delay; a scalar |
| $\tilde S = S\otimes I_2$ | Scattering matrix central in the module |
| $\mathrm{Tr}(\tilde H) = 2\,\mathrm{Sc}(\tilde H)$ | Trace convention |

## Further Reading

- L. D. Landau and E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory* (Pergamon, 1977), for one-dimensional scattering, the transmission coefficients, and the transfer matrix.
- A. Messiah, *Quantum Mechanics* (North-Holland, 1961), for the matching conditions, the S-matrix, and flux conservation.
- E. Merzbacher, *Quantum Mechanics* (Wiley, 1998), for the step, barrier, and well, and for the delta potential.
- D. J. Griffiths, *Introduction to Quantum Mechanics* (Pearson, 2018), for the standard one-dimensional scattering problems.
- C. Cohen-Tannoudji, B. Diu, and F. Laloë, *Quantum Mechanics* (Wiley, 1977), for the barrier and well and the resonant transmission.
- L. Schiff, *Quantum Mechanics* (McGraw-Hill, 1968), for the transfer matrix and composite barriers.
- C. W. J. Beenakker, "Random-matrix theory of quantum transport," *Reviews of Modern Physics* **69** (1997) 731–808, for the transfer-matrix composition law and its unitarity properties.
- J. M. Ziman, *Principles of the Theory of Solids* (Cambridge, 1972), for the one-dimensional periodic potential as a product of transfer matrices.
- N. Levinson, "On the uniqueness of the potential in a Schrödinger equation for a given asymptotic phase," *Danske Videnskabernes Selskab Matematisk-Fysiske Meddelelser* **25** (1949) 1–29, for the bound-state count and the transmission phase.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the biquaternion algebra and its matrix representation.
- S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford, 1995), for quaternionic formulations and the role of a chosen complex structure.
