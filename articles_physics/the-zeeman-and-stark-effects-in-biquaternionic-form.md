# __The Zeeman and Stark Effects in Biquaternionic Form__

## Introduction

If an atom is placed in a static magnetic field, its energy levels split; the splitting is the **Zeeman effect**. If it is placed in a static electric field, its levels shift and split; this is the **Stark effect**. The two effects are the elementary static responses of a quantum system to the two classical fields, and together they fix the form of the field couplings that the rest of non-relativistic spin-1/2 physics uses. Magnetic resonance, the Stern–Gerlach deflection and the spin precession all use the Zeeman coupling; the atomic polarizability and Rydberg spectroscopy use the Stark coupling.

This article treats both effects in the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ of the read-list articles. The effects themselves are standard and are reproduced exactly. What the article establishes is the algebraic structure of the two couplings and the reason their leading behaviours differ:

1. **Both couplings are Hermitian elements of $\mathbb{M}_+$.** The Zeeman coupling is $\tilde{H}_Z = -\gamma B\,\tilde{S}_3 = -\tfrac{\hbar\omega_L}{2}i\vec e_z$; the Stark coupling in a two-level truncation is $\tilde{H}_S = -dE\,i\vec e_x$. Both are of the form $h_te_t + i\vec h$ with a real vector part, and both are traceless when the permanent diagonal moment vanishes.
2. **The Zeeman splitting is linear and isotropic.** A spin-1/2 in a field $\vec B = B\vec u$ has energies $\pm\tfrac{\hbar\omega_L}{2}$ for every direction $\vec u$; the splitting $\hbar\omega_L$ depends on $|\vec B|$ only, and the field direction selects the eigenbasis, not the eigenvalues.
3. **The Stark effect is linear for degenerate levels and quadratic otherwise.** The linear Stark effect is the spectrum of $-dE\,i\vec e_x$ at an exact degeneracy, $\pm dE$; the quadratic Stark effect is the second-order shift of a non-degenerate pair, $\Delta E = -(dE)^2/\hbar\omega_0 = -\tfrac12\alpha E^2$, with $\alpha = 2d^2/\hbar\omega_0$.
4. **The difference is diagonal versus off-diagonal coupling.** The magnetic coupling is diagonal in the energy basis because a spin-1/2 carries a permanent magnetic dipole; the electric coupling is off-diagonal because a state of definite parity has no permanent electric dipole. The first gives a first-order (linear) shift; the second gives a second-order (quadratic) shift or, at a degeneracy, a first-order splitting between the two mixed states.

The notation is the series notation: $\tilde{S}_k = \tfrac{\hbar}{2}i\vec e_k$, $\tilde\Pi_{1,2}(\vec u) = \tfrac12(e_t\pm i\vec u)$, $\tilde{Ϛ} = \tfrac12(e_t+i\vec r)$, $\tilde{H} = h_te_t + i\vec h$ with eigenvalues $h_t\pm|\vec h|$, and $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$.

The companion articles supply the pieces:
- Companion article *Angular Momentum and Spin in Biquaternionic Form*, for the spin observable and its coupling to a field.
- Companion article *Quantum Physics in Biquaternionic Form*, for the two-level algebra and the trace pairing.
- Companion article *The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case*, for the atomic levels and the electric-dipole matrix element.
- Companion article *Exercise: Measuring Spin Along an Arbitrary Direction*, for the spin observable along an arbitrary axis.

## The Zeeman Effect

### The Magnetic Coupling

A magnetic dipole $\vec\mu$ in a field $\vec B$ has energy $V_{\mathrm{pot}} = -\vec\mu\cdot\vec B$. For a spin-1/2 with $\vec\mu = \gamma\vec S$, the coupling is the Hermitian element

$$
\tilde{H}_Z = -\gamma\,\vec B\cdot\tilde S = -\gamma B\,\tilde{S}(\vec u)
= -\frac{\hbar\omega_L}{2}\,i\vec u,
\qquad
\tilde{S}(\vec u) = \vec u_k\tilde{S}_k = \frac{\hbar}{2}\,i\vec u,
$$

where $\vec u = \vec B/B$ and

$$
\omega_L = \gamma B
$$

is the Larmor frequency. In the series convention $\tilde{S}_k = \tfrac{\hbar}{2}i\vec e_k$ and the isomorphism $\mathsf{M}_2$ sends $i\vec e_k\mapsto\sigma_k$, so $\tilde{H}_Z\mapsto -\tfrac{\hbar\omega_L}{2}(\vec u\cdot\boldsymbol{\sigma})$. The coupling is a Hermitian element of $\mathbb{M}_+$ with $h_t = 0$ and $\vec h = -\tfrac{\hbar\omega_L}{2}\vec u$.

### The Spin-1/2 Splitting

The observable $\tilde{H}_Z$ has the spectral decomposition

$$
\tilde{H}_Z = -\frac{\hbar\omega_L}{2}\,\tilde\Pi_1(\vec u) + \frac{\hbar\omega_L}{2}\,\tilde\Pi_2(\vec u),
$$

because $\vec u_k\tilde{S}_k\tilde\Pi_{1,2}(\vec u) = \pm\tfrac{\hbar}{2}\tilde\Pi_{1,2}(\vec u)$ and $\tilde{H}_Z\propto\vec u_k\tilde{S}_k$. The two eigenvalues are

$$
E_\pm = \pm\frac{\hbar\omega_L}{2},
$$

so the **Zeeman splitting** is

$$
\Delta E_{\mathrm{Zeeman}} = \hbar|\omega_L| = \hbar|\gamma|B,
$$

linear in the field and independent of its direction. The direction $\vec u$ enters only through the two eigenstates $\tilde\Pi_{1,2}(\vec u)$: rotating the field rotates the eigenbasis on the Bloch sphere but leaves the two energy levels fixed. This is a clean algebraic statement: a traceless Hermitian element of $\mathbb{M}_+$ has eigenvalues $\pm|\vec h|$, and $|\vec h|$ depends on the magnitude of the vector part alone.

For an electron, $\gamma = -g_e\mu_B/\hbar$ with $g_e\approx2.0023$; the two levels are separated by $\hbar|\omega_L| = g_e\mu_B B$. The magnitude of the splitting, and with it the numerical value of the gyromagnetic ratio, is external data: the algebra supplies the two-dimensional spectral structure and the isotropy, not the value of $\gamma$. The spin g-factor close to 2 is a relativistic (Dirac) result and belongs to the relativistic companion series; the orbital g-factor and the Landé factor for coupled $L$–$S$ systems belong to the companion article *Angular Momentum and Spin in Biquaternionic Form*.

### The g-Tensor and Anisotropy

For a spin in a crystal or on a molecule, the magnetic coupling need not be isotropic: the response of the moment to the field is a tensor rather than a number. The most general linear coupling of a spin-1/2 to a magnetic field is

$$
\tilde{H}_Z = \frac{\mu_B}{\hbar}\,B_i\, g_{ij}\tilde{S}_j,
$$

where $g_{ij}$ is the **g-tensor**, a real $3\times3$ matrix whose isotropic value is the g-factor $g_e$ of the preceding paragraph. This is still a Hermitian element of $\mathbb{M}_+$, of the form $i\vec h\cdot\mathbf{e}$ with

$$
h_j = \frac{\mu_B}{2}\,g_{ij}B_i,
$$

so the spectrum is $\pm\tfrac12\mu_B|g\vec B|$ and the Zeeman splitting is $\mu_B|g\vec B|$: the splitting depends on the angle between the field and the principal axes of the g-tensor. In the algebra the anisotropy is the statement that the vector part $\vec h$ of the observable is a linear image of the field, and the eigenvalues are still $\pm|\vec h|$. The isotropic case $g_{ij} = g_e\delta_{ij}$ reduces to the preceding subsection, where $\tilde{H}_Z = \mu_B g_e B\,\tilde{S}_3/\hbar = -\gamma B\tilde{S}_3$ for $\gamma = -g_e\mu_B/\hbar$. The g-tensor is measured by electron paramagnetic resonance; the framework supplies the two-dimensional spectral structure and the vector-part formula, and takes the tensor itself as external data.

### Level Crossings and the Field Axis

Because the two Zeeman levels are non-degenerate for $B>0$ and their splitting is proportional to $B$, a spin-1/2 in a field has a single crossing at $B = 0$, where the two idempotents become degenerate and any axis is an eigenbasis. The Zeeman spectrum contains no accidental degeneracy and no level repulsion; the field cannot mix the two states because the coupling is diagonal in the basis it defines. This is in sharp contrast to the Stark case below, where the coupling is off-diagonal and produces an avoided crossing. The reason is algebraic: the Zeeman coupling is proportional to the same element $i\vec u$ whose idempotents it diagonalises, so it is a function of the observable being measured.

### The Selection Rule as a Commutator

A drive transverse to the static field is a Hermitian element built from $i\vec e_x$ and $i\vec e_y$. The commutator of a transverse coupling with the longitudinal Zeeman term is, using the identity $[\tilde{Q}_1,\tilde{Q}_2] = -2(\vec Q_1\times\vec Q_2)$ of the companion article *Quantum Physics in Biquaternionic Form*,

$$
\left[\tilde{H}_Z,\,dE\,i\vec e_x\right] = -2\left(-\frac{\hbar\omega_L}{2}\vec u\right)\times(dE\,\vec u_x)
= \hbar\omega_L\,dE\,(\vec u\times\vec u_x),
$$

which is non-zero precisely when the transverse coupling is not parallel to the field. The selection rule $\Delta m = \pm1$ for a transverse drive and $\Delta m = 0$ for a longitudinal one is thus a statement about the vanishing of this cross product: the observable component along $\vec u$ commutes with $\tilde{H}_Z$ and the orthogonal components do not. In the spin-1/2 case the two non-commuting components are exactly the off-diagonal elements that connect the two eigenstates.

## The Stark Effect

### The Electric Coupling

An electric dipole $\vec d$ in a field $\vec E$ has energy $V_{\mathrm{pot}} = -\vec d\cdot\vec E$, giving the Hermitian coupling

$$
\tilde{H}_S = -\vec d\cdot\vec E = -E\,d\,i\vec e_x
$$

when the dipole operator is taken along the field direction and truncated to its off-diagonal matrix element $d$ between two levels. The choice $i\vec e_x$ is a choice of basis in the two-level space; a general dipole coupling is $-E(d_1\,i\vec e_x + d_2\,i\vec e_y)$, and the two components correspond to the two independent dipole matrix elements. In the two-level truncation the coupling is a traceless Hermitian element of $\mathbb{M}_+$ with $\vec h = (-d_1E, -d_2E, 0)$.

A physical dipole operator has a definite parity: $\vec d$ is odd under spatial inversion, so its diagonal matrix elements between states of definite parity vanish. For a pair of levels of opposite parity the only non-zero matrix element is the off-diagonal one, and the coupling therefore has no diagonal part. A spin-1/2 with no orbital structure — a bare magnetic moment — has no electric dipole coupling at this order at all; the electric field couples to the orbital motion, and the two-level truncation above represents a pair of opposite-parity orbital states dressed by the spin. The electron electric dipole moment, which would give a diagonal coupling, is a beyond-Standard-Model quantity and is not part of this framework.

### Linear Stark in a Degenerate Pair

Consider a pair of states of opposite parity and equal unperturbed energy, $\hbar\omega_0 = 0$. The Hamiltonian in the two-level space is

$$
\tilde{H} = -E\,d\,i\vec e_x .
$$

This is a traceless Hermitian element with $\vec h = (-dE,0,0)$, so its eigenvalues are

$$
E_\pm = \pm\,dE,
$$

a **linear** Stark splitting. The eigenstates are $\tilde\Pi_{1,2}(\vec u_x)$, the equal superpositions of the two parity eigenstates, which carry opposite permanent dipole moments $\pm d$ along $\vec u_x$ and are therefore shifted linearly by the field. This is the situation of the hydrogen $n=2$ manifold, where the $2s$ and $2p$ states are degenerate and the Stark effect is linear; the degeneracy is what permits a permanent dipole moment to exist in the field direction.

In the algebra the linear Stark effect is nothing but the spectral decomposition of a traceless Hermitian element with a vector part along the field axis: $\tilde{H}_S = -dE\,i\vec e_x = -dE\,(\tilde\Pi_1(\vec u_x)-\tilde\Pi_2(\vec u_x))$, so the two eigenvalues are $\mp dE$ and the two eigenstates are the two idempotents of the field axis. The essential input is the degeneracy; without it the two idempotents are not degenerate and the linear splitting is modified, as the next subsection shows.

### Quadratic Stark and the Polarizability

Now take a non-degenerate pair, with unperturbed splitting $\hbar\omega_0$ and the same off-diagonal coupling,

$$
\tilde{H}(\lambda) = -\frac{\hbar\omega_0}{2}\,i\vec e_z - E\,d\,i\vec e_x .
$$

The two eigenvalues are the spectral endpoints of a traceless Hermitian element with $\vec h = (-Ed,0,-\tfrac{\hbar\omega_0}{2})$:

$$
E_\pm(E) = \pm\sqrt{\left(\frac{\hbar\omega_0}{2}\right)^2 + (Ed)^2}.
$$

For small fields, $|Ed|\ll\hbar\omega_0$, expanding the square root gives

$$
E_-(E) = -\frac{\hbar\omega_0}{2} - \frac{(Ed)^2}{\hbar\omega_0} + O(E^4),
\qquad
E_+(E) = +\frac{\hbar\omega_0}{2} + \frac{(Ed)^2}{\hbar\omega_0} + O(E^4).
$$

The ground state therefore shifts downward by

$$
\Delta E_0 = -\frac{(Ed)^2}{\hbar\omega_0} = -\frac{1}{2}\,\alpha E^2,
\qquad
\boxed{\;\alpha = \frac{2d^2}{\hbar\omega_0}\;}
$$

This is the **quadratic Stark effect**, and $\alpha$ is the static polarizability of the two-level system. The shift is second order in the field because the first-order shift $-\langle \pm|\vec d\cdot\vec E|\pm\rangle$ vanishes: the two states have definite parity and no permanent dipole moment. Equivalently, in the algebra the diagonal part of the coupling in the unperturbed basis vanishes, so the coupling contributes only at second order. The exact expression above is the resummation of that perturbation series; its leading term is the polarizability formula.

The same result can be read directly in the algebra as a level repulsion: the two eigenvalues move apart as $E$ grows, and their separation

$$
E_+(E)-E_-(E) = \sqrt{(\hbar\omega_0)^2 + (2Ed)^2}
$$

increases from $\hbar\omega_0$ toward $2|Ed|$. At $|Ed| = \hbar\omega_0/2$ the nonlinearity is already appreciable: the exact lower-level shift is $-0.20711\,\hbar\omega_0$ against the quadratic prediction $-0.25\,\hbar\omega_0$. Deep in the perturbative regime, at $Ed = \hbar\omega_0/100$, the two agree to five places, $-0.00009999\,\hbar\omega_0$ against $-0.0001\,\hbar\omega_0$. The quadratic formula is the leading term of a convergent expansion in $(Ed/\hbar\omega_0)^2$.

### The Resolvent and the Full Polarizability

The polarizability formula of the two-level model is the truncation of the standard second-order expression. For a state $|0\rangle$ coupled by $V = -\vec d\cdot\vec E$ to a complete set of states $\{|m\rangle\}$, the second-order shift is

$$
E_0^{(2)} = \sum_{m\neq 0}\frac{|\langle m|V|0\rangle|^2}{E_0-E_m}
= -E_i E_j \sum_{m\neq 0}\frac{\langle 0|d_i|m\rangle\langle m|d_j|0\rangle}{E_m-E_0},
$$

which defines the polarizability tensor $\alpha_{ij} = 2\sum_{m\neq 0}\frac{\langle 0|d_i|m\rangle\langle m|d_j|0\rangle}{E_m-E_0}$ through $\Delta E_0 = -\tfrac12\alpha_{ij}E_iE_j$. The two-level formula $\alpha = 2d^2/\hbar\omega_0$ is the single-term version with one intermediate state. In the algebra the sum is over the spectral resolutions of the intermediate states, and the structure of the expression is the standard one: the coupling enters twice, once in the matrix element and once in the energy denominator, and the overall sign is negative because the ground state is pushed down by the admixture of the excited states.

For the hydrogen ground state the sum gives the standard result $\alpha\mathfrak{a}_{\mathrm{H}} = \tfrac92 a_0^3$ in atomic units, i.e. $\alpha\mathfrak{a}_{\mathrm{H}} = 4\pi\epsilon_0\cdot\tfrac92 a_0^3$ in SI; the $2p$ states dominate the sum, which is why the two-level truncation with the $1s$–$2p$ matrix element and the $1s$–$2p$ splitting already gives the correct order of magnitude. The framework does not evaluate the sum: the dipole matrix elements and the level spacings are data of the atomic problem, treated in the companion article *The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case*.

### The Avoided Crossing

The two-level Stark Hamiltonian is the standard avoided-crossing problem. As the field is swept, the levels repel rather than cross; in the absence of the coupling they would cross at zero detuning, and the coupling $Ed$ opens a gap $2|Ed|$ at that point. In the algebra the repulsion is the statement that the two eigenvalues of a traceless Hermitian element are $\pm|\vec h|$, and $|\vec h| = \sqrt{(Ed)^2 + (\hbar\omega_0/2)^2}$ never vanishes when both components are present. The situation is exactly the effective Hamiltonian of the Rabi problem with the roles of detuning and drive exchanged: there the longitudinal component was $(\omega_0-\omega)$ and the transverse was $\omega_1$; here the longitudinal component is the detuning divided by two and the transverse component is the dipole coupling. The two problems are the same algebraic object, read in different physical variables.

## The Two Couplings Compared

### Both Are Hermitian Elements of $\mathbb{M}_+$

The Zeeman and Stark couplings are

$$
\tilde{H}_Z = -\frac{\hbar\omega_L}{2}\,i\vec e_z,
\qquad
\tilde{H}_S = -E\left(d_1\,i\vec e_x + d_2\,i\vec e_y\right),
$$

after choosing $\vec u_z$ along the magnetic field and noting that an electric field can have components along both transverse directions relative to it. Both are of the form $i\vec h$ with real $\vec h$; both are traceless if the permanent moments vanish; and both are elements of the informational sector, so both couple to the state through the trace pairing and the spectral decomposition of $\mathbb{M}_+$. Neither coupling requires an element of the material sector: the fields are external data that multiply Hermitian observables.

### Diagonal Versus Off-Diagonal

The difference between the two effects is the placement of the coupling in the energy eigenbasis.

| Feature | Zeeman | Stark |
|---|---|---|
| Coupling | $\tilde{H}_Z = -\tfrac{\hbar\omega_L}{2}i\vec e_z$ | $\tilde{H}_S = -E(d_1i\vec e_x+d_2i\vec e_y)$ |
| Position in the $\vec u_z$ eigenbasis | diagonal | off-diagonal |
| Permanent moment? | yes (magnetic) | no (parity) |
| First-order shift | linear, $\pm\tfrac{\hbar\omega_L}{2}$ | zero unless degenerate |
| Degenerate case | level crossing at $B=0$ | linear Stark, $\pm Ed$ |
| Non-degenerate case | — | quadratic Stark, $-\tfrac12\alpha E^2$ |
| Mixes the eigenstates? | no | yes |

The reason the magnetic coupling is diagonal is that the two spin states carry definite, opposite magnetic moments; the reason the electric coupling is off-diagonal is that they carry no definite electric dipole moment. In the algebra the first is the statement that $\tilde{H}_Z$ is a function of the same element $i\vec e_z$ that defines the eigenbasis, and the second is the statement that $\tilde{H}_S$ is built from $i\vec e_x$, which anticommutes with $i\vec e_z$: $i\vec e_x\,i\vec e_z = -i\vec e_z\,i\vec e_x = \vec e_y$. The commutator $[\tilde{H}_Z,\tilde{H}_S] = -2(\vec h_Z\times\vec h_S)$ is non-zero, so the two couplings are incompatible observables when the fields are not parallel; this is the algebraic statement of the fact that a magnetic field and a transverse electric field cannot be simultaneously diagonalised.

### Conventions of Sign

The signs in the two couplings follow from $V_{\mathrm{pot}} = -\vec\mu\cdot\vec B$ and $V_{\mathrm{pot}} = -\vec d\cdot\vec E$. In the convention of the companion exercise *Exercise: Spin Precession in a Magnetic Field*, the spin magnetic moment is taken along the spin, $\vec\mu = \gamma\vec S$, so that $\tilde{H}_Z = -\gamma B\tilde{S}_3 = -\tfrac{\hbar\omega_L}{2}i\vec e_z$ with $\omega_L = \gamma B$. A negative gyromagnetic ratio (the electron) reverses the ordering of the two levels but not the structure; the algebra treats the sign of $\gamma$ as external data.

## What the Algebra Adds and What It Does Not

**Standard physics, transcribed.** The Zeeman Hamiltonian, the linear Zeeman splitting, the g-factor, the linear and quadratic Stark effects, the polarizability formula $\alpha = 2d^2/\hbar\omega_0$, and the avoided crossing are all standard. The article adds no predictions.

**What the algebra organises.**

- **A common home.** Both field couplings are Hermitian elements of $\mathbb{M}_+$, and both effects are read off by the two mechanisms of that subspace: the spectral decomposition for the eigenvalues and the trace pairing for the expectation values.
- **Isotropy of the Zeeman splitting as a spectral statement.** The eigenvalues $\pm|\vec h|$ of a traceless Hermitian element depend on the magnitude of the vector part only, which is why the Zeeman splitting is independent of the field direction.
- **The diagonal/off-diagonal dichotomy.** The distinction between the linear Zeeman effect and the quadratic Stark effect is the distinction between a diagonal and an off-diagonal coupling, and in the algebra this is the distinction between a coupling proportional to $i\vec e_z$ and one proportional to $i\vec e_x$.
- **A unified avoided crossing.** The Stark two-level problem and the Rabi effective Hamiltonian are the same traceless Hermitian element read in different variables; the framework makes the identity of the two problems explicit.

**What the algebra does not supply.** The gyromagnetic ratio $\gamma$, the electric dipole matrix element $d$, and the level spacing $\hbar\omega_0$ are external data of the specific system. The algebra supplies the two-dimensional structure and the way the parameters enter it; it does not supply their values. The relativistic corrections that give the electron $g\approx2$ are outside the scope of this subcategory.

## Open Questions

1. **The electric dipole moment of the electron.** A non-zero electron EDM would add a diagonal electric coupling and produce a linear Stark effect for a spin-1/2 in an electric field. Whether the framework has anything to say about the size of such a coupling, or about the discrete symmetries that forbid it, is open; the question is a standard one in particle physics and is not addressed here.

2. **Non-linear response beyond second order.** The exact two-level Stark shift is a square root, not a polynomial. Is there a systematic algebraic expansion of the eigenvalues of a two-level Hermitian element in powers of the transverse coupling, and does it have the structure of the standard perturbative series?

3. **The polarizability as a trace.** The polarizability $\alpha = 2d^2/\hbar\omega_0$ is written here in terms of the two-level parameters. Can it be written as a trace pairing in the algebra, $\alpha\propto\mathrm{Tr}(\ldots)$? The second-order formula suggests a resolvent kernel, which the algebra may or may not be able to represent.

4. **Combined fields and the crossed-field problem.** With both a magnetic and a transverse electric field present, the effective Hamiltonian is $\tilde{H} = -\tfrac{\hbar\omega_L}{2}i\vec e_z - E(d_1i\vec e_x+d_2i\vec e_y)$, the same form as the Rabi effective Hamiltonian. Is there a distinguished "crossed-field" geometry in which the two couplings are arranged symmetrically, and does the algebra name it?

5. **Empirical contact.** As everywhere in the series, the reformulation reproduces the standard predictions; whether its additional structure implies a measurable deviation is open.

## Summary

The two elementary static field couplings of a spin-1/2 are Hermitian elements of the informational sector. The **Zeeman coupling** in a field $\vec B = B\vec u$ is

$$
\tilde{H}_Z = -\gamma B\,\tilde{S}(\vec u) = -\frac{\hbar\omega_L}{2}\,i\vec u,
\qquad \omega_L = \gamma B,
$$

with the spectral decomposition $\tilde{H}_Z = -\tfrac{\hbar\omega_L}{2}\tilde\Pi_1(\vec u) + \tfrac{\hbar\omega_L}{2}\tilde\Pi_2(\vec u)$ and linear, isotropic splitting $\Delta E = \hbar|\omega_L| = \hbar|\gamma|B$. The field direction selects the eigenbasis $\tilde\Pi_{1,2}(\vec u)$ and not the eigenvalues.

The **Stark coupling** is off-diagonal in the energy basis, $\tilde{H}_S = -E\,d\,i\vec e_x$ in a two-level truncation, and its effect depends on the degeneracy. For a degenerate pair it gives the linear Stark splitting $E_\pm = \pm Ed$, the exact spectrum of a traceless Hermitian element with the vector part along the field. For a non-degenerate pair with splitting $\hbar\omega_0$ it gives $E_\pm = \pm\sqrt{(\hbar\omega_0/2)^2+(Ed)^2}$, whose expansion is the quadratic Stark shift

$$
\Delta E_0 = -\frac{(Ed)^2}{\hbar\omega_0} = -\frac{1}{2}\alpha E^2,
\qquad
\alpha = \frac{2d^2}{\hbar\omega_0},
$$

and whose level repulsion is the avoided crossing with gap $2|Ed|$.

The two effects differ because a spin-1/2 carries a permanent magnetic dipole and no permanent electric dipole: the magnetic coupling is diagonal and gives a first-order shift, and the electric coupling is off-diagonal and gives a second-order shift unless a degeneracy supplies a permanent moment in the field direction. The algebra expresses this as the difference between a coupling proportional to the same $i\vec e_z$ that defines the energy basis and a coupling proportional to a transverse $i\vec e_x$. Both couplings are incompatible observables when the fields are not parallel, with commutator $[\tilde{H}_Z,\tilde{H}_S] = -2(\vec h_Z\times\vec h_S)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Central scalar imaginary |
| $\mathbb{M}_+$ | Hermitian (informational) subspace; home of both couplings |
| $\tilde{S}(\vec u) = \tfrac{\hbar}{2}i\vec u$ | Spin observable along $\vec u$ |
| $\tilde{H}_Z = -\gamma B\tilde{S}(\vec u) = -\tfrac{\hbar\omega_L}{2}i\vec u$ | Zeeman coupling |
| $\omega_L = \gamma B$ | Larmor frequency |
| $\Delta E_{\mathrm{Zeeman}} = \hbar|\omega_L| = \hbar|\gamma|B$ | Zeeman splitting |
| $\tilde{H}_S = -E(d_1i\vec e_x+d_2i\vec e_y)$ | Stark coupling (two-level truncation) |
| $d$ | Electric dipole matrix element between the two levels |
| $E_\pm = \pm Ed$ | Linear Stark splitting (degenerate pair) |
| $E_\pm = \pm\sqrt{(\hbar\omega_0/2)^2+(Ed)^2}$ | Exact two-level Stark levels |
| $\alpha = 2d^2/\hbar\omega_0$ | Static polarizability of the two-level system |
| $\Delta E_0 = -\tfrac12\alpha E^2$ | Quadratic Stark shift |
| $[\tilde{Q}_1,\tilde{Q}_2] = -2(\vec Q_1\times\vec Q_2)$ | Commutator of two Hermitian elements |

## Further Reading

- P. Zeeman, "On the Influence of Magnetism on the Nature of the Light Emitted by a Substance," *Philosophical Magazine* **43** (1897) 226–239, for the discovery of the magnetic splitting.
- A. E. Ruark, "The Zeeman Effect and Stark Effect of Hydrogen in Wave Mechanics," *Physical Review* **31** (1928) 533–538, for the early wave-mechanical treatment of both effects.
- J. Stark, "Beobachtungen über den Effekt des elektrischen Feldes auf Spektrallinien," *Annalen der Physik* **43** (1914) 965–982, for the discovery of the electric splitting.
- P. S. Epstein, "The Stark Effect from the Point of View of Schrödinger's Quantum Theory," *Physical Review* **28** (1926) 695–710, for the linear Stark effect of the degenerate hydrogenic levels.
- L. D. Landau and E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory* (Pergamon, 1977), for the systematic perturbation theory of the Stark and Zeeman effects.
- H. A. Bethe and E. E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms* (Springer, 1957), for the atomic polarizability and the higher-order Stark corrections.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the spin-1/2 Zeeman Hamiltonian and the g-factor.
- Claude Cohen-Tannoudji, Bernard Diu, and Franck Laloë, *Quantum Mechanics* (Wiley, 1977), for the two-level Stark treatment and the avoided crossing.
