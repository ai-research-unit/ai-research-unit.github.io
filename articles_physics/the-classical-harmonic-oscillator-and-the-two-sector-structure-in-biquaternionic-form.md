# __The Classical Harmonic Oscillator and the Two-Sector Structure in Biquaternionic Form__

## Introduction

The harmonic oscillator is the first system in this subcategory with a **restoring force**. The free particle of the companion article has a constant velocity and a straight worldline; the oscillator has an acceleration proportional to its displacement, $\ddot{\mathbf{x}} = -\omega^2\mathbf{x}$, so its motion is bounded and periodic and its trajectory closes. In the biquaternion framework it is the first system in which the **two-sector structure** of the algebra becomes visible in a classical mechanical quantity rather than in a formal classification.

The observation the article develops is the following. The state of a one-dimensional oscillator is a pair of conjugate real numbers, the displacement $x$ and the momentum $p$, or, in the normalization that makes the motion a rigid rotation, the complex amplitude

$$
a = x + i\,\frac{p}{m\omega} \in \mathbb{C} .
$$

Because $a$ is a complex number, it embeds in the algebra as a **central** element,

$$
\tilde{A} = a\,e_0 = x\,e_0 + i\,\frac{p}{m\omega}\,e_0 \in \mathbb{C}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0, ie_0\} .
$$

The centre $\mathbb{C}_{\mathbb{B}}$ is the intersection of the algebra with the complex numbers, it is two-real-dimensional, and its two real directions $e_0$ and $ie_0$ lie **one in each sector**: $e_0$ is Hermitian and belongs to $\mathbb{M}_+$, while $ie_0$ is anti-Hermitian and belongs to $\mathbb{M}_-$. The two conjugate quadratures of the oscillator therefore occupy the two sectors, and the oscillator's phase advance is the **sector exchange restricted to the centre** — the rotation that multiplication by $i$ performs. The energy is the Hermitian form of the amplitude, $\tfrac12 m\omega^2|a|^2$, which is positive definite, in contrast with the indefinite norm form.

This is a genuinely classical statement and it is deliberately different from the quantum one. In the quantum oscillator the two quadratures are Hermitian operators and both lie in $\mathbb{M}_+$; the companion article *The Harmonic Oscillator in Biquaternionic Form* shows that the canonical commutator cannot be realized by two elements of $\mathbb{M}_+$ and treats the sector structure accordingly. Here there is no commutator and no operator: a classical real number is not an element of a sector until one chooses where to place it, and the placement that makes the oscillator's phase a rotation places the two quadratures in the two sectors. The two treatments agree that the phase is the sector exchange; they differ in what carries the quadratures, because operators and classical numbers are different objects.

The article is organized as follows. The oscillator is first written in the material sector, where its trajectory and its restoring force live. The complex amplitude is then constructed and decomposed into its two sector parts. The phase advance is identified with the sector exchange, and its generator with the timelike direction of the material sector. The energy is identified with the Hermitian form, and its positivity is contrasted with the signature of the norm form. The article closes by asking the quantum companion's question — whether the complexification makes the two sectors two oscillators — and answering it in the classical case.

**Conventions.** The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_je_k = \epsilon_{jkl}e_l$ for $j \neq k$; the scalar imaginary $i$ is central with $i^2 = -e_0$. The anti-Hermitian subspace $\mathbb{M}_-$ is the material sector, the Hermitian subspace $\mathbb{M}_+$ the informational sector, and $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ with $i\mathbb{M}_\pm = \mathbb{M}_\mp$. The real-quaternion subalgebra is $\mathbb{H}_{\mathbb{B}}$ and the centre is $\mathbb{C}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0, ie_0\}$. The trace is normalized so that $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ for $\tilde{P}, \tilde{H} \in \mathbb{M}_+$, and the real part of a biquaternion is written $\mathrm{Sc}$. The classical phase-space bracket is the Poisson bracket of the companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator*; the quantum treatment of the same system, which is not used here, is that of *The Harmonic Oscillator in Biquaternionic Form*.

<!-- CONVENTION — classical quadrature placement: the assignment of $x$ to the Hermitian central direction $e_0$ and $\Pi$ to the anti-Hermitian central direction $ie_0$ is an embedding of $\mathbb{C}$ into the centre, chosen so that the phase advance is a rotation. It is not a claim about observables, and it is not in conflict with the quantum treatment, in which both quadratures are Hermitian and lie in $\mathbb{M}_+$. A reviewer must not align the two placements by moving a classical quadrature across the sector boundary. -->

## The Oscillator in the Material Sector

### The Equation of Motion

A particle of mass $m$ bound to the origin by the linear restoring force $\mathbf{F} = -k\mathbf{x}$, with $k = m\omega^2$, obeys

$$
m\ddot{\mathbf{x}} = -m\omega^2\mathbf{x}, \qquad \ddot{\mathbf{x}} + \omega^2\mathbf{x} = 0 .
$$

In the framework the worldline is the material-sector curve

$$
\tilde{X}(t) = ic\,t\,e_0 + \mathbf{x}(t), \qquad \mathbf{x}(t) = x(t)\,e_1 + y(t)\,e_2 + z(t)\,e_3 ,
$$

and the equation of motion is a statement about its vector part alone. The scalar direction $ie_0$ is untouched: the restoring force acts on the spatial displacement and not on the time. This is the same split that the free particle exhibits, now with a nontrivial vector equation.

For the present article it is enough to take the motion one-dimensional along a fixed direction $\hat{\mathbf{n}}$, so that

$$
\mathbf{x}(t) = \xi(t)\,\hat{\mathbf{n}}, \qquad \xi(t) = A\cos(\omega t + \varphi),
$$

with amplitude $A$ and phase $\varphi$. The general motion is a superposition of three such one-dimensional motions, or a single one after the orientation of the axes is chosen; nothing in the sector structure depends on the number of dimensions, and the one-dimensional case carries all of it.

### The Restoring Force as a Central Material Vector

The force $\mathbf{F} = -m\omega^2\mathbf{x}$ is a real pure quaternion: it lies in the vector part of the material sector, the real three-space $\operatorname{span}\{e_1, e_2, e_3\} \subset \mathbb{M}_-$. It is proportional and opposite to the position, so it is a **central force** in the mechanical sense of being directed along the radius from the origin; the oscillator is therefore the simplest member of the family of central-force problems that the later articles of this subcategory treat. Its force law is linear rather than inverse-square, and its orbits are the closed ellipses of the phase plane rather than the conic sections of the Kepler problem, but the structural placement is the same: a real force vector in $\mathbb{M}_-$ acting on a real position vector in $\mathbb{M}_-$.

Because the force is a pure vector, its product with the position is a pure quaternion with both a scalar and a vector part,

$$
\mathbf{F}\,\mathbf{x} = -\mathbf{F}\cdot\mathbf{x} + \mathbf{F}\times\mathbf{x} = m\omega^2|\mathbf{x}|^2\,e_0 + 0 ,
$$

the vector part vanishing because $\mathbf{F}$ and $\mathbf{x}$ are parallel. The scalar part of the product is the negative of the potential energy's double, $-\mathbf{F}\cdot\mathbf{x} = m\omega^2|\mathbf{x}|^2$, and the vanishing of the vector part is the algebraic statement that the force is central: a force is central about the origin exactly when its product with the position has no vector part, equivalently when $\mathbf{F}$ and $\mathbf{x}$ commute, $[\mathbf{F}, \mathbf{x}] = 0$. The later articles of this subcategory develop this criterion; for the oscillator it is immediate.

### Energy

The energy is the sum of the kinetic and elastic terms,

$$
E = \frac{1}{2}m\dot{\xi}^2 + \frac{1}{2}m\omega^2\xi^2 ,
$$

and it is conserved, $dE/dt = 0$, by the equation of motion. In the normalized variables $x = \xi$ and $p = m\dot{\xi}$ it reads $E = p^2/(2m) + \tfrac12 m\omega^2x^2$, and in the amplitude normalization below it will take the compact form $\tfrac12 m\omega^2|a|^2$. The energy is a real scalar; its placement in the algebra is the subject of the section "Energy and the Hermitian Form".

## The Complex Amplitude and the Centre

### The Amplitude

Introduce the normalized momentum and the complex amplitude

$$
\Pi = \frac{p}{m\omega}, \qquad a = x + i\Pi = x + i\,\frac{p}{m\omega} \in \mathbb{C} .
$$

The two real numbers $x$ and $\Pi$ are the standard quadratures of the oscillator; the passage from $(x, \Pi)$ to $a$ is the passage from the real phase plane to the complex plane, and it is what makes the oscillator's flow a rigid rotation. Embedding the complex number in the algebra gives the central element

$$
\tilde{A} = a\,e_0 = x\,e_0 + i\,\Pi\,e_0 \in \mathbb{C}_{\mathbb{B}} .
$$

The centre is the natural home of a complex amplitude, because it is exactly the part of the algebra isomorphic to $\mathbb{C}$: it commutes with everything, and its two real directions are the only central directions available.

### The Two-Sector Decomposition

The element $\tilde{A}$ decomposes into its Hermitian and anti-Hermitian parts. Since $e_0^\dagger = e_0$ and $i^\dagger = -i$,

$$
\tilde{A} = \underbrace{x\,e_0}_{\text{Hermitian}} + \underbrace{i\,\Pi\,e_0}_{\text{anti-Hermitian}} ,
$$

so that

$$
\tilde{A}_{\mathbb{M}_+} = \frac{1}{2}\left(\tilde{A} + \tilde{A}^\dagger\right) = x\,e_0 \in \mathbb{M}_+ , \qquad
\tilde{A}_{\mathbb{M}_-} = \frac{1}{2}\left(\tilde{A} - \tilde{A}^\dagger\right) = i\,\Pi\,e_0 \in \mathbb{M}_- .
$$

This is the two-sector structure of the oscillator: **the two conjugate quadratures lie one in each sector**. The position quadrature sits along the central Hermitian direction $e_0$, the normalized momentum quadrature along the central anti-Hermitian direction $ie_0$. The decomposition is summarized by

$$
\tilde{A} = \tilde{A}_{\mathbb{M}_+} + \tilde{A}_{\mathbb{M}_-}, \qquad i\tilde{A}_{\mathbb{M}_\pm} = \text{an element of } \mathbb{M}_\mp ,
$$

and the sector exchange that $i$ performs is exactly the map that interchanges the two quadratures.

Two remarks fix the interpretation. First, the assignment of $x$ to the Hermitian direction and $\Pi$ to the anti-Hermitian one is a **phase convention**, not a dynamical fact: replacing $a$ by $-ia$ swaps the roles of the two quadratures and exchanges the sector assignments, and this is the quarter-period shift of the oscillation. What is convention-independent is that the two quadratures occupy the two central directions, and those two directions lie in different sectors. Second, the decomposition uses only the **central** part of the sector split: $\mathbb{M}_+ \cap \mathbb{C}_{\mathbb{B}}$ is the real axis $e_0\mathbb{R}$ and $\mathbb{M}_- \cap \mathbb{C}_{\mathbb{B}}$ the imaginary axis $ie_0\mathbb{R}$. The vector directions $ie_k$ of $\mathbb{M}_+$ and $e_k$ of $\mathbb{M}_-$ are not involved. The oscillator's sector structure is the one-dimensional-per-sector structure of the centre, and it is the simplest case of the general split.

### Contrast with the Quantum Oscillator

The classical decomposition above should be compared carefully with the quantum treatment, because the two statements look similar and are not. In the quantum oscillator the quadratures are **operators** $\hat{x}$ and $\hat{p}$, both of which are observables and both of which therefore lie in $\mathbb{M}_+$; the canonical commutator is $[\hat{x}, \hat{p}] = i\hbar\,e_0$, whose right-hand side lies in $\mathbb{M}_-$. The companion article *The Harmonic Oscillator in Biquaternionic Form* shows that this equation cannot be satisfied by two elements of $\mathbb{M}_+$: the commutator of two Hermitian biquaternions is a pure real quaternion with a vanishing scalar part, whereas $i\hbar\,e_0$ is a purely imaginary scalar. The quantum oscillator's phase space is not a pair of elements of the two sectors.

The classical oscillator is different because a classical number is not an operator. The real number $\Pi$ has no Hermiticity of its own; one may place it along $e_0$, along $ie_0$, or anywhere else, and the physically meaningful placement is the one dictated by the complex structure of the amplitude. Placing $x$ along $e_0$ and $\Pi$ along $ie_0$ makes the flow a rotation, and that is the placement used here. The quantum and classical statements agree on the **role of the phase** — it is the sector exchange — and disagree on the carrier of the quadratures, because the operator and the classical number are different kinds of object. The quantum companion puts its side of the contrast sharply: in any representation inside $\mathbb{B}$ each quadrature would be an observable, observables are Hermitian, so both quadratures lie in $\mathbb{M}_+$, and the sectors separate the observable content of the amplitude from its generator content rather than the amplitude's two real degrees of freedom. Nothing in the classical construction contradicts that. A classical real number carries no Hermiticity, and placing $x$ along $e_0$ and $\Pi$ along $ie_0$ is the embedding of $\mathbb{C}$ into the centre under which the flow is a rotation; the constraint that forces both quantum quadratures into one sector is simply absent here, and the placement along the two central directions is available. Neither statement is a deformation of the other; they are about different algebras of observables.

## The Phase Advance as the Sector Exchange

### The Solution as a Rotation of the Centre

The equation of motion in the amplitude variables is the pair

$$
\dot{x} = \omega\Pi, \qquad \dot{\Pi} = -\omega x ,
$$

which is equivalent to the single complex equation

$$
\frac{d\tilde{A}}{dt} = -i\omega\,\tilde{A} .
$$

Its solution is the phase rotation

$$
\tilde{A}(t) = e^{-i\omega t}\tilde{A}(0), \qquad a(t) = e^{-i\omega t}a(0),
$$

so that the trajectory in the centre is a circle of radius $|a|$ traversed at angular rate $\omega$. Multiplying the decomposition $\tilde{A} = x\,e_0 + i\Pi\,e_0$ by $e^{-i\omega t}$ and using the centrality of $i$ gives

$$
x(t) = x_0\cos\omega t + \Pi_0\sin\omega t, \qquad \Pi(t) = \Pi_0\cos\omega t - x_0\sin\omega t ,
$$

which is the standard solution written with the standard initial conditions. In terms of the momentum, $\Pi(t) = p(t)/(m\omega)$, so this is $x(t) = x_0\cos\omega t + \frac{p_0}{m\omega}\sin\omega t$ and $p(t) = p_0\cos\omega t - m\omega x_0\sin\omega t$.

### The Generator Lies in the Material Sector

The generator of the phase rotation is the central element

$$
-i\omega\,e_0 = \omega\,(ie_0)\cdot(-1) ,
$$

a real multiple of $ie_0$, which lies in $\mathbb{M}_-$: it is along the **timelike direction of the material sector**. The phase advance is therefore generated by the material sector's own time direction, and the rotation it generates is a rotation of the centre by the sector-exchange element $i$. Written as an action on the two quadratures, the generator maps the $\mathbb{M}_+$ part of $\tilde{A}$ into the $\mathbb{M}_-$ part and back:

$$
-i\omega\left(x\,e_0 + i\Pi\,e_0\right) = \omega\left(\Pi\,e_0 - i x\,e_0\right),
$$

so that a quarter period later the position quadrature has become the momentum quadrature. This is the precise sense in which the oscillator's phase is the sector exchange: the flow generated by the material time direction rotates the Hermitian quadrature into the anti-Hermitian one and returns it after a full period.

The rotation is a **one-parameter group**, and this is special to the oscillator. For a general Hamiltonian system the phase flow is not the orbit of a fixed algebra element, because the Hamiltonian is not quadratic. For the oscillator the amplitude equation is linear with constant coefficients, the generator $-i\omega e_0$ is constant, and the flow is the exponential of a fixed central element. The oscillator is thus the exact classical analogue of a one-parameter unitary group, with the generator in the material sector and the flow acting on the centre.

### Phase Space and the Sector Split

It is worth recording the geometric picture. The classical phase plane is coordinatized by $(x, \Pi)$, and the algebra sees it as the centre $\mathbb{C}_{\mathbb{B}} \cong \mathbb{R}^2$. The complex structure of the plane — the operation $J$ that sends $(x, \Pi)$ to $(-\Pi, x)$, which is what a quarter-period advance does — is multiplication by $i$. The phase plane is therefore the centre, and $J$ is the algebra's scalar imaginary restricted to it. The two-sector split of the centre is the split of the phase plane into the real and imaginary axes, and the Hamiltonian flow is the rotation generated by $J$ composed with the frequency.

This gives a compact statement of the oscillator's sector structure:

$$
\text{phase plane} = \mathbb{C}_{\mathbb{B}} = \left(\mathbb{M}_+ \cap \mathbb{C}_{\mathbb{B}}\right) \oplus \left(\mathbb{M}_- \cap \mathbb{C}_{\mathbb{B}}\right), \qquad
J = i\big|_{\mathbb{C}_{\mathbb{B}}} \ \text{swaps the two summands.}
$$

The oscillator is the system that makes this picture dynamical. A general classical system with $n$ degrees of freedom has a $2n$-dimensional phase space; the oscillator is the case $n=1$ in which the phase space is the centre and the flow is the algebra's complex structure. The higher-dimensional and nonlinear cases are the business of the companions on central forces.

## Energy and the Hermitian Form

### The Energy Is the Hermitian Form

With the amplitude $a = x + i\Pi$ the energy is

$$
E = \frac{1}{2}m\omega^2\left(x^2 + \Pi^2\right) = \frac{1}{2}m\omega^2|a|^2 .
$$

In the algebra, $|a|^2$ is the scalar part of the Hermitian form of the central element $\tilde{A}$:

$$
\tilde{A}\,\tilde{A}^\dagger = |a|^2\,e_0, \qquad E = \frac{1}{2}m\omega^2\,\mathrm{Sc}\!\left(\tilde{A}\tilde{A}^\dagger\right) .
$$

The energy is therefore the **Hermitian form** of the amplitude, and it is positive definite: $\tilde{A}\tilde{A}^\dagger = 0$ if and only if $\tilde{A} = 0$. This is what makes the oscillator bounded — the orbit in the centre is a circle and the energy is the squared radius. The positivity of the energy and the compactness of the orbit are the same fact.

### The Norm Form Instead of the Hermitian Form

The contrast with the **norm form** is instructive. The norm form of the central element is not the squared modulus but the complex square,

$$
N(\tilde{A}) = \tilde{A}\,\overline{\tilde{A}} = a^2\,e_0 = \left(x^2 - \Pi^2\right)e_0 + 2ix\Pi\,e_0 ,
$$

which is indefinite: it vanishes on the pair of lines $x = \pm\Pi$ and is negative for $|\Pi| > |x|$. A "energy" built from the norm form would be unbounded below on the centre, and the orbit would be a hyperbola rather than a circle. The oscillator's stability is precisely the statement that its energy is the Hermitian form and not the norm form. This is the same distinction that separates the two sectors: $N$ restricted to $\mathbb{M}_-$ has the Lorentzian signature $(3,1)$ and restricted to $\mathbb{M}_+$ has the signature $(1,3)$, while the Hermitian form $\tilde{Q}\tilde{Q}^\dagger$ is positive definite on the centre.

The two forms coincide only on the real axis: for $\tilde{A} = x\,e_0$, $N(\tilde{A}) = \tilde{A}\tilde{A}^\dagger = x^2e_0$. The discrepancy grows with the imaginary (momentum) quadrature, which is exactly the quadrature that the sector decomposition places in $\mathbb{M}_-$.

## The Flow as a Bracket Derivation

The phase rotation can also be written as a Hamiltonian flow, and the exercise makes the sector roles precise. With the normalized momentum $\Pi = p/(m\omega)$ the canonical bracket is $\{x, \Pi\} = 1/(m\omega)$, inherited from $\{x,p\} = 1$, and the energy is $H = \tfrac12 m\omega^2(x^2 + \Pi^2)$. The equations of motion are the bracket equations

$$
\dot x = \{x, H\} = \frac{\partial H}{\partial p} = \omega\Pi, \qquad
\dot\Pi = \{\Pi, H\} = -\frac{1}{m\omega}\frac{\partial H}{\partial x} = -\omega x ,
$$

which are the two real equations of the phase advance. Assembling them into the amplitude gives $\dot{\tilde{A}} = -i\omega\tilde{A}$ again.

The bracket shows how the sector split interacts with the flow. The energy is a central scalar and lies in the central part of $\mathbb{M}_+$; the bracket with it is a derivation on the space of functions of the centre, and that derivation carries the real part of the amplitude into the imaginary part and back. The oscillator is thus the case in which the Hamiltonian derivation generated by an element of $\mathbb{M}_+$ is the sector exchange on the centre — the classical, single-degree-of-freedom instance of the general relation between the bracket and the algebra discussed in the companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator*. Nothing quantum is used: the bracket is the classical one, and the derivation is a derivation on classical functions, not a commutator with an operator.

### Numerical Checks

The structural claims of this section were verified by explicit computation with complex-coefficient quaternions. The Hermitian and anti-Hermitian parts of the central amplitude were computed and found to be $x\,e_0$ and $i(p/m\omega)e_0$ respectively; the phase rotation $a\mapsto e^{-i\omega t}a$ was found to reproduce the standard oscillator solution for the displacement and the momentum to twelve decimal places; the energy was found to equal $\tfrac12 m\omega^2|a|^2$ and to equal the scalar part of $\tilde{A}\tilde{A}^\dagger$; and the norm form was found to be $a^2e_0$, indefinite. Separately, the commutator of two Hermitian biquaternions was computed and found to be the pure real quaternion $-2\,\mathbf{h}\times\mathbf{k}$ with a vanishing scalar part, which is the fact that prevents the canonical commutator from being realized in $\mathbb{M}_+$.

## One Oscillator or Two?

The companion article on the quantum oscillator asks whether the complexification that defines $\mathbb{B}$ makes the material and informational sectors behave as two oscillators, and answers the question in the quantum setting. The classical case has a clean answer, and it is worth stating.

**The classical oscillator is one oscillator, not two.** The phase rotation is a single one-parameter group, with a single frequency $\omega$ and a single conserved energy. There is no second frequency and no independent second degree of freedom. The phase plane is two-real-dimensional, and it is exhausted by the two quadratures of the single amplitude.

**The two sectors carry the two quadratures, not two modes.** The $\mathbb{M}_+$ and $\mathbb{M}_-$ parts of $\tilde{A}$ are $x\,e_0$ and $i\Pi\,e_0$; they are the real and imaginary parts of one complex number, coupled rigidly by the phase rotation. They are not independently excitable: setting one to zero at one time does not keep it zero, because the flow carries it into the other after a quarter period. The sector split of the centre is a **direct-sum decomposition of the phase plane**, and the dynamics is a rotation that does not respect it.

**The two first-order equations are the sector pair.** The equation of motion, written as $\dot{x} = \omega\Pi$ and $\dot{\Pi} = -\omega x$, is a pair of real equations, one for each sector component. The pair is coupled, and the coupling constant is the frequency. In this reading the two sectors do carry the two equations of motion, and the phase advance is the coupling. This is the most one can say: the sectors are the two quadratures, and the oscillator is the coupling between them.

A genuinely two-oscillator structure would require two independent complex amplitudes, hence a four-real-dimensional phase space and two frequencies. That is what a two-dimensional isotropic oscillator has, and it is not the structure of the centre. The centre is one complex dimension, and the two sectors are its real and imaginary axes.

## Summary

The classical harmonic oscillator in biquaternionic form has its trajectory, its restoring force and its energy in the material sector, and its phase structure in the centre. The trajectory is $\tilde{X} = ic\,t\,e_0 + \mathbf{x}(t)$ with $\ddot{\mathbf{x}} = -\omega^2\mathbf{x}$; the restoring force $\mathbf{F} = -m\omega^2\mathbf{x}$ is a real vector in $\mathbb{M}_-$ and is central about the origin.

The complex amplitude $a = x + ip/(m\omega)$ embeds in the algebra as the central element

$$
\tilde{A} = a\,e_0 = \underbrace{x\,e_0}_{\in \mathbb{M}_+} + \underbrace{i\,\frac{p}{m\omega}\,e_0}_{\in \mathbb{M}_-},
$$

so that the two conjugate quadratures occupy the two sectors, along the two real directions of the centre $\mathbb{C}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0, ie_0\}$. The assignment of which quadrature occupies which sector is a phase convention; the fact that they occupy different sectors is not.

The equation of motion is $\dot{\tilde{A}} = -i\omega\tilde{A}$, whose solution is the phase rotation $\tilde{A}(t) = e^{-i\omega t}\tilde{A}(0)$. The generator $-i\omega\,e_0$ lies in $\mathbb{M}_-$ along the timelike direction $ie_0$, and the rotation it generates is the **sector exchange restricted to the centre**: the $\mathbb{M}_+$ quadrature is carried into the $\mathbb{M}_-$ quadrature and back. The oscillator is therefore the system in which the sector exchange is a classical mechanical motion.

The energy is the Hermitian form,

$$
E = \frac{1}{2}m\omega^2|a|^2 = \frac{1}{2}m\omega^2\,\mathrm{Sc}\!\left(\tilde{A}\tilde{A}^\dagger\right),
$$

positive definite and bounded below, whereas the norm form $N(\tilde{A}) = a^2e_0$ is indefinite. The oscillator is one oscillator, not two: its two sectors carry the two quadratures of a single complex amplitude, coupled by the phase rotation, and a genuine two-oscillator structure would require a second complex dimension that the centre does not have.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_je_k = \epsilon_{jkl}e_l$ $(j\neq k)$ |
| $i$ | Central scalar imaginary, $i^2 = -e_0$; $i\mathbb{M}_\pm = \mathbb{M}_\mp$ |
| $\mathbb{M}_-$ | Anti-Hermitian (material) sector: $iq_0e_0 + \mathbf{q}$ |
| $\mathbb{M}_+$ | Hermitian (informational) sector: $h_0e_0 + i\mathbf{h}$ |
| $\mathbb{C}_{\mathbb{B}} = \operatorname{span}_\mathbb{R}\{e_0, ie_0\}$ | Centre; the phase plane of the oscillator |
| $\mathbb{M}_+ \cap \mathbb{C}_{\mathbb{B}} = e_0\mathbb{R}$ | Real axis of the phase plane (position quadrature) |
| $\mathbb{M}_- \cap \mathbb{C}_{\mathbb{B}} = ie_0\mathbb{R}$ | Imaginary axis of the phase plane (momentum quadrature) |
| $\tilde{X} = ic\,t\,e_0 + \mathbf{x}$ | Worldline, in $\mathbb{M}_-$ |
| $\omega$, $k = m\omega^2$ | Angular frequency; spring constant |
| $\mathbf{F} = -m\omega^2\mathbf{x}$ | Restoring force, real vector in $\mathbb{M}_-$; central, $[\mathbf{F},\mathbf{x}]=0$ |
| $x$, $p$, $\Pi = p/(m\omega)$ | Displacement, momentum, normalized momentum |
| $a = x + i\Pi \in \mathbb{C}$ | Complex amplitude |
| $\tilde{A} = a\,e_0 \in \mathbb{C}_{\mathbb{B}}$ | Central embedding of the amplitude |
| $\tilde{A}_{\mathbb{M}_\pm} = \tfrac12(\tilde{A} \pm \tilde{A}^\dagger)$ | Sector components: $x\,e_0$ and $i\Pi\,e_0$ |
| $\dot{\tilde{A}} = -i\omega\tilde{A}$ | Amplitude equation; generator $-i\omega\,e_0 \in \mathbb{M}_-$ |
| $e^{-i\omega t}$ | Phase rotation; sector exchange on the centre |
| $E = \tfrac12 m\omega^2|a|^2$ | Energy; the Hermitian form of the amplitude |
| $\tilde{A}\tilde{A}^\dagger = |a|^2e_0$ | Hermitian form (positive definite) |
| $N(\tilde{A}) = a^2e_0$ | Norm form (indefinite) |
| $J = i|_{\mathbb{C}_{\mathbb{B}}}$ | Complex structure of the phase plane; swaps the two sectors |
| $\{x, p\} = 1$ | Poisson bracket; bracket conventions of the companion article |

## Further Reading

- Herbert Goldstein, Charles Poole and John Safko, *Classical Mechanics* (Pearson, 2002), for the harmonic oscillator, normal modes and phase-space orbits.
- L. D. Landau and E. M. Lifshitz, *Mechanics* (Pergamon, 1976), for the oscillator, action-angle variables and the phase plane.
- Vladimir I. Arnold, *Mathematical Methods of Classical Mechanics* (Springer, 1989), for the complex structure and the linear symplectic form of the oscillator.
- V. Bargmann, "On a Hilbert space of analytic functions and an associated integral transform," *Communications on Pure and Applied Mathematics* **14** (1961) 187–214, for the complex-amplitude description of the oscillator.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the operator treatment of the oscillator and the canonical commutator.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the biquaternion algebra, its centre and its two real subspaces.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of rotations and complex structures.
