# __The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form__

## Introduction

The WKB approximation is the semiclassical expansion of the wave function in powers of $\hbar$. Its leading order is the classical Hamilton–Jacobi equation for the action, and its next order is a transport equation for the amplitude. It is the bridge between the quantum problem and the classical trajectories, and it is the method by which barrier penetration, quantisation conditions, and the correspondence principle are usually obtained. This article develops both the WKB approximation and the Hamilton–Jacobi equation in the biquaternion framework, for a spin-0 particle in an external scalar potential.

The biquaternion content of the semiclassical limit is unusually clean, because the approximation is organised by the **phase**. In the biquaternion algebra the phase $e^{iS/\hbar}$ is a central element — its exponent is a real scalar times the central imaginary — so the WKB ansatz $\psi = A\,e^{iS/\hbar}$ places the amplitude in the center and the action in the center, and the leading-order momentum is the real quaternion $\nabla S$, the algebra's spatial vector. The Hamilton–Jacobi equation then turns out to be nothing but the **norm form of the momentum** equated to twice the kinetic energy,

$$
\frac{1}{2m}N(\nabla S) = E - V ,
$$

which is the same norm form whose vanishing defines the zero divisor cone and whose value on $\mathbb{M}_+$ measures the purity of a state. The semiclassical limit is thus the regime in which the dynamics is carried by a real vector of the algebra, the phase gradient, and in which the norm form of that vector is the energy. This article derives that statement, its first correction, and its consequences.

The article is organised as follows. The next section sets up the amplitude–phase decomposition and derives the two real equations into which the Schrödinger equation separates. The third section treats the Hamilton–Jacobi equation, its norm-form reading, and the trajectories and rays it defines. The fourth treats the transport equation, the WKB amplitude, and the van Vleck determinant. The fifth obtains the quantisation condition, the Maslov phase, and the tunnelling law. The sixth gives the exact rewriting with the quantum potential. The seventh states what the biquaternion form adds and what remains open, and the closing sections are the summary, the notation table, and the external literature.

The conventions are those of the companion articles. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with $e_0=1,e_1,e_2,e_3$, $e_j^2=-e_0$, central scalar imaginary $i$; $\mathbb{C}_{\mathbb{B}}$ is the center; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace; $\mathbb{M}_+$ and $\mathbb{M}_-$ are the Hermitian and anti-Hermitian sectors; the state module is $\mathbb{B}\tilde P\cong\mathbb{C}^2$; and $\mathrm{Tr}(\tilde H)=2\,\mathrm{Sc}(\tilde H)$. The Hamiltonian for a scalar potential is $\tilde H = [-\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf x)]e_0$, central. The d'Alembertian is not used here; the only sign conventions engaged are those of the norm form and the Laplacian, both of which follow from $e_j^2=-e_0$.

## The WKB Ansatz in Biquaternionic Form

### The amplitude–phase decomposition

Write the stationary state as

$$
\psi(\mathbf x) = A(\mathbf x)\;e^{\,iS(\mathbf x)/\hbar}\;\chi,
\qquad
A(\mathbf x) > 0, \quad S(\mathbf x) \in \mathbb{R}, \quad \chi \in \mathbb{B}\tilde P ,
$$

with a real positive amplitude $A$ and a real phase $S$. The exponential is central, so it commutes with the module element $\chi$ and with everything else; the amplitude is real and therefore also central. Under the isomorphism $\Phi$, the state is $A e^{iS/\hbar}\chi$ with a scalar phase multiplying both components equally. This is the WKB form that the framework's conventions make natural: the phase is central, and the module factor is a constant spectator, exactly as in the free and scattering problems.

The momentum acts on the phase in a fixed way. Since $\partial_k e^{iS/\hbar} = (i/\hbar)(\partial_k S)e^{iS/\hbar}$,

$$
\tilde p\,\psi = \sum_k e_k \hat p_k \psi
= \sum_k e_k\left(\partial_k S - i\hbar\,\partial_k \ln A\right)\psi ,
$$

so, separating the real phase gradient from the $\hbar$-suppressed amplitude term,

$$
\tilde p\,\psi = \Big[\,\nabla S - i\hbar\,\nabla\ln A\,\Big]\psi,
\qquad
\nabla S = \sum_k (\partial_k S)\,e_k .
$$

The leading term $\nabla S$ is a **real quaternion**, an element of the algebra's spatial-vector subspace $\mathbb{H}_{\mathbb{B}}$; the correction is imaginary-scalar times a real vector, and is the first term of the expansion in $\hbar$. At leading order the state is an approximate eigenstate of the momentum with the real eigenvalue $\nabla S$, which is the classical momentum of the trajectory through the point.

### The two real equations

Apply the Hamiltonian to the ansatz and separate powers of $\hbar$. From $\tilde H\psi = E\psi$ with $\tilde H = (-\frac{\hbar^2}{2m}\nabla^2+V)e_0$,

$$
-\frac{\hbar^2}{2m}\nabla^2\!\left(A e^{iS/\hbar}\right) + \left(V - E\right)A e^{iS/\hbar} = 0 ,
$$

and carrying out the derivatives,

$$
\left[\frac{|\nabla S|^2}{2m} + V - E\right]A
-\frac{i\hbar}{2m}\left(2\nabla A\cdot\nabla S + A\nabla^2 S\right)
-\frac{\hbar^2}{2m}\nabla^2 A = 0 .
$$

The bracket is real; the middle term is purely imaginary; the last term is real. Separating the imaginary part gives the **transport equation**,

$$
\nabla\cdot\left(A^2\,\nabla S\right) = 0 ,
$$

and separating the real part gives the **quantum Hamilton–Jacobi equation**,

$$
\frac{|\nabla S|^2}{2m} + V + Q = E ,
\qquad
Q = -\frac{\hbar^2}{2m}\,\frac{\nabla^2 A}{A} ,
$$

where $Q$ is the quantum potential. The two equations are exact: together they are equivalent to the Schrödinger equation for a state of the WKB form. The semiclassical expansion is the expansion of this pair in powers of $\hbar$; at leading order $Q$ is dropped, and the equation that remains is the classical Hamilton–Jacobi equation.

## The Hamilton–Jacobi Equation

### The equation as a norm form

Dropping the quantum potential, the leading-order equation is

$$
\frac{|\nabla S|^2}{2m} + V(\mathbf x) = E ,
$$

the **Hamilton–Jacobi equation** for the action $S$ of a particle of energy $E$ in the potential $V$. In the biquaternion algebra the phase gradient is the real quaternion $\nabla S=\sum_k(\partial_kS)e_k$, and its quaternion square is

$$
(\nabla S)^2 = \sum_{j,k} e_je_k\,\partial_jS\,\partial_kS
= -\sum_k (\partial_k S)^2\,e_0
= -|\nabla S|^2 e_0 ,
$$

while its norm form is

$$
N(\nabla S) = |\nabla S|^2 ,
$$

the central element $\nabla S\,\overline{\nabla S}=|\nabla S|^2\,e_0$. The Hamilton–Jacobi equation is therefore the statement

$$
\frac{1}{2m}N(\nabla S) = E - V ,
$$

an equation in the center of the algebra: **the kinetic energy is the norm form of the phase gradient**. This is the same identity that the free-particle article records for the momentum operator, $\tilde T=\tilde p\bar{\tilde p}/2m$, now applied to the leading-order momentum $\nabla S$. Two consequences follow immediately. First, the right-hand side is positive in the classically allowed region, $E>V$, and the norm form of a real vector is positive, so the equation can be solved there; in the forbidden region the right-hand side is negative, no real $\nabla S$ solves the equation, and the momentum becomes imaginary, turning the oscillatory phase into an exponential. Second, the vanishing of the norm form would be the condition $\nabla S=0$, i.e. the turning point; the null (zero divisor) cone is not reached by the phase gradient, whose norm form is fixed by the energy defect and vanishes only where the classical particle stops.

### Rays, trajectories, and the eikonal

The Hamilton–Jacobi equation is solved by the method of characteristics, and the characteristics are the classical trajectories. Writing $\mathbf p = \nabla S$ for the classical momentum, the equation reads $|\mathbf p|^2/2m+V=E$, and its characteristic system is

$$
\dot{\mathbf x} = \frac{\mathbf p}{m},
\qquad
\dot{\mathbf p} = -\nabla V .
$$

The phase gradient therefore defines a congruence of trajectories along which $S$ is constant along the wave fronts and increases at the rate $\dot S = \mathbf p\cdot\dot{\mathbf x} = |\mathbf p|^2/m$, which recovers the classical action. This is the optical–mechanical analogy in its algebraic form: the wave fronts $S=\text{const}$ are the surfaces of constant phase, the rays are the trajectories, and the phase gradient is the ray direction. In the biquaternion reading the ray direction per point is an element of the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the algebra's copy of three-dimensional space, and the phase accumulated along a ray is a central element of $\mathbb{C}_{\mathbb{B}}$.

### The free and separable cases

For the free particle the Hamilton–Jacobi equation has the complete integral

$$
S(\mathbf x,t) = \mathbf p\cdot\mathbf x - E t,
\qquad
E = \frac{|\mathbf p|^2}{2m},
$$

whose phase gradient is the constant vector $\mathbf p$, and whose wave function $Ae^{i(\mathbf p\cdot\mathbf x-Et)/\hbar}$ is the plane wave of the free-particle article. For a separable potential $V=V_1(x_1)+V_2(x_2)+V_3(x_3)$ the equation separates, $S=\sum_k S_k(x_k)$, and each $S_k$ obeys

$$
\frac{1}{2m}\left(\frac{dS_k}{dx_k}\right)^2 + V_k(x_k) = E_k,
\qquad
\sum_k E_k = E ,
$$

so that

$$
S_k(x_k) = \pm\int^{x_k}\sqrt{2m\left(E_k - V_k(x_k')\right)}\;dx_k' .
$$

The signs are the two directions of motion, and the norm-form reading applies to each term: the square of the phase derivative is the norm form of the one-dimensional momentum. The turning points $E_k = V_k$ are where the radicand vanishes and the two branches meet.

## The Amplitude and the Transport Equation

### The transport equation and the WKB amplitude

The transport equation

$$
\nabla\cdot\left(A^2\,\nabla S\right) = 0
$$

is the statement that the vector field $A^2\nabla S$ is divergence-free. Since $\nabla S = m\mathbf v$ is the classical momentum, this is the continuity equation of a conserved density $A^2$ carried by the classical flow, and it is exactly the probability continuity equation $\nabla\cdot\mathbf J=0$ for a stationary state, with $\mathbf J = A^2\nabla S/m$. In one dimension it integrates at once:

$$
A^2\,\frac{dS}{dx} = \text{const}
\qquad\Longrightarrow\qquad
A(x) = \frac{C}{\sqrt{|p(x)|}},
\qquad
p(x) = \sqrt{2m(E-V(x))},
$$

which is the WKB amplitude: the wave function is large where the particle moves slowly and small where it moves fast, in inverse proportion to the square root of the classical momentum.

In three dimensions the transport equation is solved by the **van Vleck determinant**,

$$
A(\mathbf x)\ \propto\ \left|\det\frac{\partial^2 S_{\mathrm{cl}}}{\partial \mathbf x_i\,\partial \mathbf x_f}\right|^{1/2},
$$

which measures the focusing of the ray congruence: $A^2$ is the density of trajectories, and the determinant is the Jacobian of the map from initial to final positions. This is the same object that the path-integral article extracts from the Gaussian fluctuation determinant of the semiclassical kernel; the transport equation and the stationary-phase evaluation of the path integral give the same amplitude, as they must, since both are the leading order of the same expansion.

### The phase and the amplitude in the algebra

The transport equation involves only the real amplitude and the real phase gradient, so it lives in the real-quaternion and central parts of the algebra. There is no non-central element anywhere in the leading semiclassical state:

$$
\psi_{\mathrm{WKB}} = A\,e^{iS/\hbar}\,\chi,
\qquad
A\in\mathbb{C}_{\mathbb{B}}|_{\mathbb{R}}=\mathbb{R}e_0,
\quad
e^{iS/\hbar}\in\mathbb{C}_{\mathbb{B}},
\quad
\nabla S\in\mathbb{H}_{\mathbb{B}},
\qquad
\chi \ \text{constant}.
$$

The module element $\chi$ is untouched, as for every central Hamiltonian. The first correction to this picture is the quantum potential, which is central as well, and which is the subject of the sixth section.

## Semiclassical Quantisation

### Connection formulas and the Maslov index

The WKB solutions fail at the turning points, where $p(x)\to0$ and the amplitude diverges. The repair is the standard one: near a simple turning point the equation is approximated by Airy's equation, and the Airy functions provide the connection between the oscillatory solution on the allowed side and the exponential solution on the forbidden side. In the biquaternion reading nothing changes in the analysis, because the equation being approximated is the scalar equation for the envelope; what the framework contributes is the location of the phase in the center and the identity of the imaginary unit under the square roots that the connection formulas contain.

Across a soft turning point the oscillatory solution acquires a phase $-\pi/2$ relative to the naive WKB phase; across a hard wall (a Dirichlet boundary) it acquires $-\pi$, twice as much, which is the statement that the wall carries Maslov index two where a soft turning point carries one. These are the **Maslov phases**. In the framework they are operations on the central $i$: the connection formulas contain $\sqrt{2\pi i\hbar}$ and the factor $i^{-1/2}$, and the square root is taken inside the center $\mathbb{C}_{\mathbb{B}}$, which is a copy of $\mathbb{C}$. This is the same observation that the path-integral article records for the semiclassical kernel, and it is the reason the Maslov phases are unambiguous here: the central $i$ is supplied by the algebra and does not require a chosen complex structure.

### Bohr–Sommerfeld quantisation

For a bound state in a smooth one-dimensional well with two soft turning points, the phase must return to itself after a round trip. The single-valuedness of $e^{iS/\hbar}$ around the closed orbit, together with the two Maslov phases, gives the **Bohr–Sommerfeld condition**

$$
\oint p\,dx = 2\pi\hbar\left(n + \tfrac12\right),
\qquad n = 0,1,2,\dots
$$

and for a well bounded by a hard wall on one side and a soft turning point on the other the Maslov count changes and the condition becomes

$$
\int_{x_1}^{x_2} p\,dx = \pi\hbar\left(n + \tfrac34\right),
\qquad n = 0,1,2,\dots
$$

where the offset $3/4$ replaces the $1/2$ of the two-soft-turning-point case because one of the two turning points is a wall. Both conditions are statements about the central phase $e^{iS/\hbar}$: the action accumulated around the orbit, divided by $\hbar$, must equal a multiple of $2\pi$ up to the Maslov offset.

The condition was verified numerically in two ways. For the harmonic oscillator, $V=\tfrac12m\omega^2x^2$, the integral $\oint p\,dx$ evaluates to $2\pi E/\omega$, so the condition returns $E_n=\hbar\omega(n+\tfrac12)$ exactly; a direct quadrature of $\oint p\,dx$ at those energies reproduced $2\pi\hbar(n+\tfrac12)$ to a relative error below $5\times10^{-9}$ for $n=0,\dots,4$. For the Morse potential, $V=D(1-e^{-ax})^2$, the same condition with two soft turning points reproduced the exact spectrum $E_n=\hbar\omega(n+\tfrac12)-[\hbar\omega(n+\tfrac12)]^2/4D$ to a relative error below $2\times10^{-9}$ for the four lowest levels, at $D=5$, $a=0.7$, $m=\hbar=1$. The harmonic oscillator and the Morse potential are the standard cases in which WKB quantisation is exact.

That WKB is nonetheless an approximation is visible in a genuinely anharmonic well. For $V=\tfrac12x^2+\lambda x^4$ with $\lambda=0.1$, the same quantisation condition gives $E_0^{\mathrm{WKB}}=0.5333$ against the exact $0.5591$ (a relative error of $-4.6\%$), $E_1^{\mathrm{WKB}}=1.7540$ against $1.7695$ ($-0.88\%$), $E_2^{\mathrm{WKB}}=3.1269$ against $3.1386$ ($-0.37\%$), and $E_3^{\mathrm{WKB}}=4.6193$ against $4.6289$ ($-0.21\%$); the exact values were obtained by a finite-difference diagonalisation of the Hamiltonian on a grid, via the Sturm sequence. The error decreases with $n$, as the correspondence principle requires.

### Tunnelling

In the classically forbidden region the momentum is imaginary, $p=i\kappa$ with $\kappa=\sqrt{2m(V-E)}$, and the phase becomes a real exponential. Matching the exponential across the barrier gives the WKB transmission

$$
T\ \approx\ \exp\!\left(-\frac{2}{\hbar}\int_{x_1}^{x_2}\sqrt{2m(V(x)-E)}\;dx\right),
$$

whose exponent is the imaginary part of the action across the barrier. The brackets of the piecewise-constant barrier of the scattering article are the special case in which $\kappa$ is constant and the exponent is $2\kappa a$. For a parabolic barrier $V=V_0-\tfrac12m\omega^2x^2$ the exponent evaluates to $\pi(V_0-E)/\hbar\omega$; a direct quadrature at $V_0=1$, $\omega=1.3$, $E=0.4$, $m=\hbar=1$ gave $\int\sqrt{2m(V-E)}\,dx = 1.4499658$ against the closed value $\pi(V_0-E)/\omega = 1.4499658$, agreeing to $10^{-9}$. The exact transmission of the parabolic barrier is Kemble's formula $T=(1+e^{-2\pi(E-V_0)/\hbar\omega})^{-1}$, whose exponent is the same; the WKB result is the leading exponential, and the ratio of the two, $T_{\mathrm{WKB}}/T_{\mathrm{exact}} = 1+e^{-2\pi(V_0-E)/\hbar\omega}$, tends to one for a deep barrier.

## The Quantum Potential

### The exact rewriting

Restoring the quantum potential, the real part of the decomposition is

$$
\frac{|\nabla S|^2}{2m} + V + Q = E ,
\qquad
Q = -\frac{\hbar^2}{2m}\frac{\nabla^2 A}{A},
$$

which is exact for any state written in the form $Ae^{iS/\hbar}$. The equation has the same shape as Hamilton–Jacobi with the potential shifted by $Q$; consequently the trajectories defined by $\mathbf p=\nabla S$ are those of a particle moving in $V+Q$, not in $V$. The quantum potential is the entire difference between the classical and the quantum descriptions in this rewriting, and it is of order $\hbar^2$: the semiclassical expansion is the expansion of $Q$ in powers of $\hbar$, and the WKB approximation is the truncation at $Q=0$.

The quantum potential is central: $A$ is real and central, $\nabla^2A$ is real and central, so $Q\in\mathbb{C}_{\mathbb{B}}|_{\mathbb{R}}=\mathbb{R}e_0$. The phase is central and the amplitude is central, and the exact rewriting of the Schrödinger equation into a Hamilton–Jacobi equation plus a transport equation therefore involves only the center of the algebra at every order. This is the sharpest statement of what the semiclassical expansion is in this framework: **the entire expansion lives in the center**, the phase as a central unitary element and the amplitude as a central real one. The non-central structure of the algebra does not enter the semiclassical limit of a spin-0 particle at any order.

### Why the amplitude is real

The reality of $A$ is not an assumption but a choice of gauge. Any state can be written $Ae^{iS/\hbar}$ with a complex $A$; imposing that $A$ be real and positive is the choice that makes the transport equation take its divergence form. In the biquaternion setting, a complex $A$ would place the amplitude in $\mathbb{C}_{\mathbb{B}}$ rather than in $\mathbb{R}e_0$, and the separation into real and imaginary parts would have to be redone. The standard convention, and the one used here, is the real positive amplitude; it is also the one that makes $A^2$ a probability density and the transport equation a continuity equation.

## What the Biquaternion Form Adds

**Standard quantum mechanics, transcribed.** The amplitude–phase decomposition, the two real equations, the Hamilton–Jacobi equation, the method of characteristics, the optical–mechanical analogy, the transport equation, the WKB amplitude, the van Vleck determinant, the connection formulas, the Maslov index, the Bohr–Sommerfeld condition, the tunnelling exponent, and the quantum potential are all standard. None of them is new here.

**What the biquaternion notation provides.**

- **The Hamilton–Jacobi equation as a norm form.** The leading-order equation is $\frac{1}{2m}N(\nabla S)=E-V$: the kinetic energy is the norm form of the phase gradient, the same algebraic object whose vanishing defines the zero divisor cone and which on $\mathbb{M}_+$ measures purity. The forbidden region is where the norm form of the real phase gradient would have to be negative, which no real vector allows; that is the algebraic statement of the imaginary momentum.
- **The phase gradient as a real quaternion.** The leading-order momentum is an element of the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the algebra's copy of space, while the momentum operator is Hermitian in $\mathbb{M}_+$. The correspondence is the semiclassical statement that the operator's expectation is the classical vector.
- **A central phase and a central amplitude.** The WKB state is $Ae^{iS/\hbar}\chi$ with $A$ real and central and the phase central; the quantum potential is central; the whole semiclassical expansion lives in the center, and the module factor is a constant. The Maslov phases are operations on the central $i$, and the square roots under the connection formulas are taken inside the center.
- **The same amplitude as the path integral.** The van Vleck determinant appears here from the transport equation and in the companion path-integral article from the stationary phase of the path integral; the framework exhibits them as one object.

**What remains open.**

- **Uniformity of the approximation.** The WKB expansion breaks down at turning points and caustics and is repaired by connection formulas and Airy functions; the algebra does not supply a uniform approximation, and the standard methods are used unchanged.
- **The complex action.** For tunnelling and for the classically forbidden region, $S$ becomes complex. The biquaternion reading of the phase then involves a complex scalar exponent, and whether there is an algebraic reason to prefer one branch of the complex action is not addressed here.
- **The extension to fields.** The WKB method for field theory, where the phase is a functional and the transport equation becomes a functional equation, is outside the finite-dimensional algebra for the same reason that the path-integral measure is.
- **Empirical content.** As elsewhere, whether the semiclassical reformulation yields any prediction distinguishing it from scalar WKB is open.

## Open Questions

**1. Is there a native algebraic characterisation of the turning set?** The turning points are where $N(\nabla S)=0$ in the sense that the kinetic energy vanishes; this is not the zero divisor cone, and whether the algebra distinguishes the two loci is not explored here.

**2. Can the Maslov index be read from the algebra?** The $\pm\tfrac{\pi}{2}$ and $\pm\tfrac{\pi}{4}$ phases are the phases of the central square roots that appear in the Airy connection formulas. Whether their counting is an algebraic invariant of the ray congruence, or only an analytic one, is open.

**3. What is the biquaternion status of the quantum potential?** It is a central real scalar and is the first correction to the Hamilton–Jacobi equation. Whether the framework gives it a sector reading, or a relation to the norm form at the next order, is not known.

**4. Empirical content.** Nothing in the semiclassical reformulation distinguishes it from scalar WKB.

## Summary

The WKB ansatz in the biquaternion framework is $\psi=A\,e^{iS/\hbar}\,\chi$ with a central phase, a real central amplitude, and a constant module element $\chi$. The momentum acts on it as $\tilde p\psi=[\nabla S - i\hbar\nabla\ln A]\psi$, with the leading term the real quaternion $\nabla S$ in the spatial-vector subspace $\mathbb{H}_{\mathbb{B}}$. Separating the Schrödinger equation into real and imaginary parts gives the exact pair

$$
\nabla\cdot(A^2\nabla S) = 0,
\qquad
\frac{|\nabla S|^2}{2m} + V + Q = E,
\qquad
Q = -\frac{\hbar^2}{2m}\frac{\nabla^2 A}{A}.
$$

Dropping the quantum potential gives the **Hamilton–Jacobi equation**, which in the algebra is the norm-form statement

$$
\frac{1}{2m}N(\nabla S) = E - V :
$$

the kinetic energy is the norm form of the phase gradient. Its characteristics are the classical trajectories, with $\dot{\mathbf x}=\mathbf p/m$ and $\dot{\mathbf p}=-\nabla V$, and the wave fronts are the surfaces of constant phase. The transport equation gives the WKB amplitude $A=C/\sqrt{|p|}$ and, in three dimensions, the van Vleck determinant $\big|\det\partial^2S_{\mathrm{cl}}/\partial x_i\partial x_f\big|^{1/2}$ — the same object that the companion path-integral article obtains from the Gaussian fluctuation determinant.

The Bohr–Sommerfeld condition $\oint p\,dx = 2\pi\hbar(n+\tfrac12)$, with the Maslov offsets from the Airy connection formulas, was verified to be exact for the harmonic oscillator and the Morse potential (relative errors below $5\times10^{-9}$ and $2\times10^{-9}$ respectively) and to be approximate for the anharmonic well $\tfrac12x^2+0.1x^4$, where it underestimates the exact levels by $4.6\%$, $0.88\%$, $0.37\%$, and $0.21\%$ for $n=0,\dots,3$ (exact values from finite-difference diagonalisation). The WKB tunnelling exponent $-\frac{2}{\hbar}\int\sqrt{2m(V-E)}\,dx$ matches the closed parabolic-barrier value $\pi(V_0-E)/\hbar\omega$ to $10^{-9}$ and reproduces the leading exponential of Kemble's exact formula.

The whole semiclassical expansion lives in the **center** of the algebra: the phase is a central unitary element, the amplitude and the quantum potential are central real scalars, the Maslov phases are operations on the central $i$, and the module factor is a constant. The framework supplies the norm-form reading of the Hamilton–Jacobi equation, the sector location of the phase and the amplitude, and the identity of the transport amplitude with the path-integral fluctuation determinant; it does not supply a uniform approximation at caustics, the branch of the complex action, or any prediction distinguishing the reformulation from scalar WKB.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_j^2=-e_0$ |
| $i$ | Central scalar imaginary |
| $\mathbb{C}_{\mathbb{B}}$ | Center; home of the phase and the amplitude |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace; home of the phase gradient |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian and anti-Hermitian sectors |
| $\mathbb{B}\tilde P\cong\mathbb{C}^2$ | State module |
| $\psi=Ae^{iS/\hbar}\chi$ | WKB state; central phase, real central amplitude, constant $\chi$ |
| $\tilde p=-i\hbar\nabla$ | Momentum operator, Hermitian |
| $\tilde p\psi=[\nabla S-i\hbar\nabla\ln A]\psi$ | Action of the momentum on the WKB state |
| $\nabla S=\sum_k(\partial_kS)e_k$ | Phase gradient; real quaternion, $\in\mathbb{H}_{\mathbb{B}}$ |
| $N(\nabla S)=\lvert\nabla S\rvert^2$ | Norm form of the phase gradient; $\nabla S\,\overline{\nabla S}=\lvert\nabla S\rvert^2e_0$ |
| $\frac{1}{2m}N(\nabla S)=E-V$ | Hamilton–Jacobi equation as a norm form |
| $\mathbf p=\nabla S$, $\dot{\mathbf x}=\mathbf p/m$, $\dot{\mathbf p}=-\nabla V$ | Characteristics; classical trajectories |
| $\nabla\cdot(A^2\nabla S)=0$ | Transport equation |
| $A=C/\sqrt{\lvert p\rvert}$ | WKB amplitude in one dimension |
| $\lvert\det\partial^2S_{\mathrm{cl}}/\partial x_i\partial x_f\rvert^{1/2}$ | Van Vleck determinant |
| $Q=-\frac{\hbar^2}{2m}\nabla^2A/A$ | Quantum potential; central real scalar |
| $\oint p\,dx=2\pi\hbar(n+\tfrac12)$ | Bohr–Sommerfeld quantisation; two soft turning points |
| $\int_{x_1}^{x_2}p\,dx=\pi\hbar(n+\tfrac34)$ | Quantisation with a hard wall and a soft turning point |
| $\exp(-\frac{2}{\hbar}\int\sqrt{2m(V-E)}\,dx)$ | WKB tunnelling factor |
| $\mathrm{Tr}(\tilde H)=2\,\mathrm{Sc}(\tilde H)$ | Trace convention |

## Further Reading

- H. Goldstein, C. P. Poole, and J. L. Safko, *Classical Mechanics* (Addison-Wesley, 2002), for the Hamilton–Jacobi equation, the characteristic equations, and the optical–mechanical analogy.
- L. D. Landau and E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory* (Pergamon, 1977), for the WKB method, the connection formulas, and the quantisation conditions.
- A. Messiah, *Quantum Mechanics* (North-Holland, 1961), for the semiclassical expansion, the transport equation, and the quantum potential.
- L. Schiff, *Quantum Mechanics* (McGraw-Hill, 1968), for the WKB approximation and barrier penetration.
- J. Heading, *An Introduction to Phase-Integral Methods* (Methuen, 1962), for the uniform approximation at turning points.
- M. V. Berry and K. E. Mount, "Semiclassical approximations in wave mechanics," *Reports on Progress in Physics* **35** (1972) 315–397, for the Maslov phases and caustics.
- N. Fröman and P. O. Fröman, *JWKB Approximation: Contributions to the Theory* (North-Holland, 1965), for the rigorous phase-integral method and the exactness of JWKB for shape-invariant potentials.
- J. B. Keller, "Corrected Bohr–Sommerfeld quantum conditions for nonseparable systems," *Annals of Physics* **4** (1958) 180–188, for the multidimensional quantisation conditions.
- M. Born, "Zur Quantenmechanik der Stoßvorgänge," *Zeitschrift für Physik* **37** (1926) 863–867, and *Zeitschrift für Physik* **38** (1926) 803–827, for the statistical interpretation of the amplitude and the quantum potential's precursor.
- D. Bohm, "A Suggested Interpretation of the Quantum Theory in Terms of 'Hidden' Variables," *Physical Review* **85** (1952) 166–193, for the quantum potential and the trajectory formulation.
- E. C. Kemble, "A Contribution to the Theory of the B. W. K. Method," *Physical Review* **48** (1935) 549–561, for the exact parabolic-barrier transmission and the uniform connection.
- M. Abramowitz and A. Stegun (eds.), *Handbook of Mathematical Functions* (National Bureau of Standards, 1964), for Airy functions and the zeros used in the quantisation checks.
