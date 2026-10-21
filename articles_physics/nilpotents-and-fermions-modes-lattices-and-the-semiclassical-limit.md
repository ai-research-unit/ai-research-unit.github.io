# __Nilpotents and Fermions: Modes, Lattices and the Semiclassical Limit__

## Introduction

A nilpotent is a nonzero element of the biquaternion algebra whose square is zero,

$$
\vec\Upsilon^2=0,\qquad \vec\Upsilon\neq0 .
$$

It is the extreme case of a zero divisor: it does not merely fail to be invertible, it annihilates itself. The algebra places this object in a small and rigid locus, the pure elements whose complex vector part is isotropic. The question of this article is what physics that locus carries.

The answer has three layers. A nilpotent is a **mode**: the one-site fermionic ladder is a pair of nilpotents, and Pauli exclusion is their square-zero product. It is a **lattice point**: the gapless point of a band symbol is a null momentum, and on a periodic lattice the null points are paired by topology. It is a **limit**: the semiclassical phase gradient stays off the cone except at a turning point, where it vanishes, and a contraction of the algebra reaches the cone only at the degenerate end of a family.

The article owns no theorem. It states the algebraic classification, with its source, and interprets nine consequences. Each interpretation is labelled and each carries its boundary.

One caution governs the whole article. The nilpotent is **not** the physical null four-momentum. A physical null vector lies in the material sector $\mathbb{M}_-$, has a nonzero imaginary time component, and is a zero divisor but not a nilpotent: its square is not zero. The nilpotent is pure, lies in the complexified vector subspace, and is the algebraic form of a lightlike **displacement**, not of a lightlike momentum. The two objects sit in the same cone and play different roles. Confusing them turns every later statement into a false one.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The square-zero equation, the nilpotent cone, index two and the position among the remarkable subspaces | [Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](../articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html) |
| The roots of $+1$, the idempotents and the halving map | [Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html) |
| The zero divisors, the two families and the cone | [Zero Divisors of the Biquaternion Algebra](../articles_maths/zero-divisors-of-the-biquaternion-algebra.html) |
| The norm, its multiplicativity and the inverse | [Norm and Invertibility in the Biquaternion Algebra](../articles_maths/norm-and-invertibility-in-the-biquaternion-algebra.html) |
| The Peirce decomposition and the orthogonal idempotents | [Ideals and Peirce Decomposition of the Biquaternion Algebra](../articles_maths/ideals-and-peirce-decomposition-of-the-biquaternion-algebra.html) |
| The $2\times2$ matrix model and the trace-free singular matrices | [Introduction to the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions](../articles_maths/introduction-to-the-2x2-matrix-element-representation-of-biquaternions.html) |
| The root sets across the twelve products | [Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](../articles_maths/square-roots-of-a-general-element-in-the-algebraic-structures-over-the-biquaternion-c-space.html) |

## The Algebraic Object

### The Nilpotent Cone

Write a general element as $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ and complex coefficients. The square is

$$
\tilde Q^2=\bigl(Q_t^2-(\vec Q,\vec Q)\bigr)e_t+2Q_t\vec Q,
\qquad
(\vec Q,\vec Q)=Q_x^2+Q_y^2+Q_z^2 .
$$

The equation $\tilde Q^2=0$ therefore splits into $2Q_t\vec Q=0$ and $Q_t^2=(\vec Q,\vec Q)$. The scalar branch returns $\tilde Q=0$. The nonzero branch has $Q_t=0$ and $(\vec Q,\vec Q)=0$: the nilpotent is a pure element with an isotropic complex vector part. The set is the **nilpotent cone**, of complex dimension two and real dimension four, inside the six-real-dimensional zero-divisor cone. In this algebra every nilpotent has index two, so $\vec\Upsilon^3=0$ exactly when $\vec\Upsilon^2=0$. No nilpotent is an idempotent; the two classes meet only at the origin. In the $2\times2$ matrix model the nilpotents are the nonzero trace-free singular matrices.

The pure condition is what separates the nilpotent from the rest of the cone. An element of the cone with a nonzero scalar part is a complex multiple of a non-trivial idempotent; it is a zero divisor but not a nilpotent. The nilpotent is the part of the cone that is also pure.

### The Ladder

The fermionic interpretation needs a pair, not a single nilpotent. A canonical pair is

$$
\vec\Upsilon_x=\tfrac12\bigl(i\vec e_x-\vec e_y\bigr),
\qquad
\vec\Upsilon_y=\tfrac12\bigl(i\vec e_x+\vec e_y\bigr),
\qquad
\bigl\{\vec\Upsilon_x,\vec\Upsilon_y\bigr\}=e_t .
$$

Both are pure nilpotents, $\vec\Upsilon_x^2=\vec\Upsilon_y^2=0$. Their products are orthogonal idempotents,

$$
\tilde\Pi_+=\vec\Upsilon_x\vec\Upsilon_y=\tfrac12\bigl(e_t+i\vec e_z\bigr),
\qquad
\tilde\Pi_-=\vec\Upsilon_y\vec\Upsilon_x=\tfrac12\bigl(e_t-i\vec e_z\bigr),
$$

with $\tilde\Pi_++\tilde\Pi_-=e_t$ and $\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0$. Both are Hermitian and lie in the informational sector $\mathbb{M}_+$. The pair is adjoint, $\vec\Upsilon_x^{*}=\vec\Upsilon_y$. The action is the ladder:

$$
\vec\Upsilon_x\tilde\Pi_-=\vec\Upsilon_x,\qquad
\vec\Upsilon_y\tilde\Pi_+=\vec\Upsilon_y,\qquad
\vec\Upsilon_x\tilde\Pi_+=\vec\Upsilon_y\tilde\Pi_-=0 .
$$

The element $\vec\Upsilon_x$ carries the $\tilde\Pi_-$-rung to the $\tilde\Pi_+$-rung, and $\vec\Upsilon_y$ carries $\tilde\Pi_+$ back to $\tilde\Pi_-$. The identity has split into two orthogonal rungs, and the ladder has two levels. There is no third orthogonal idempotent in $\mathbb{B}$, because $\mathbb{B}\cong M_2(\mathbb{C})$ acts on a two-dimensional complex module.

The pair is the algebraic skeleton of a fermionic mode. What the algebra does not supply is the field: a mode is not yet a field, and a ladder is not yet a dynamics.

### What the Nilpotent Is Not

The nesting of the three sets is the first physical statement, and it is worth a table. The table defines the objects before it compares them.

| object | equation | where it lives | physical interpretation |
| --- | --- | --- | --- |
| nilpotent | $\vec\Upsilon^2=0$, $\vec\Upsilon\neq0$ | pure vector subspace, complex isotropic | one fermionic mode; null symbol; contraction limit |
| physical null four-momentum | $\langle\tilde P\rangle_{\natural}=0$, $\tilde P^2\neq0$ | material sector $\mathbb{M}_-$ | photon or other massless carrier |
| idempotent | $\tilde\Pi^2=\tilde\Pi$ | Hermitian family in $\mathbb{M}_+$ | state, rung, vacuum |
| Grassmann label | $\theta^2=0$ | outside $\mathbb{B}$ | odd label of a coherent state |

A physical null momentum has $\tilde P=i(E/c)e_t+\vec p$ with $E^2=c^2\vec p^{\,2}$. Its norm vanishes, but its square is

$$
\tilde P^2=2P_t\tilde P,
$$

which is nonzero whenever the energy is nonzero. The photon is a zero divisor of the cone, not a nilpotent. The nilpotent is the pure lightlike displacement, the element whose composition with itself is nothing.

## The Nine Interpretations

### Dirac's Hole Is Not a Nilpotent

Hole theory fills the negative-energy sea and reads a missing occupation as a hole. The hole is a **difference** from the sea: it carries the quantum numbers that make it an antiparticle of the missing state, and it disappears when the state is refilled. The nilpotent is not that difference. It is the mode operator itself, the object whose square is zero and whose repeated application is impossible.

The modern reading makes the distinction sharper. The vacuum is empty, the negative-frequency modes create antiparticles, and no sea is needed. The nilpotent remains the mode; the antiparticle is a state created by the mode, not a square-zero element. The algebra supplies the anticommutation of the modes, $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$ with $\vec\Upsilon_x^2=\vec\Upsilon_y^2=0$, and the exclusion principle is its square-zero consequence. The hole, if one keeps the language, is a relational object: a missing rung, not a nilpotent.

**Boundary.** The article does not adjudicate between hole theory and the modern reading. It says which algebraic object carries which role. The hole has no square-zero representative in $\mathbb{B}$; the nilpotent has no charge label by itself. A reader who identifies the two will look for a nilpotent with the quantum numbers of a positron and will not find one.

### Jordan–Wigner Is a Choice of Square Root

The one-site spin ladder is already fermionic. The raising and lowering operators of a spin one half are nilpotent, and their anticommutator is the identity. The Jordan–Wigner transformation is the choice of that square root and its extension along a chain. At one site the spin algebra and the fermion algebra are the same algebra, and the map is a relabelling of its generators; the nonlocal string appears only when a second site is added, and it is the branch cut that keeps the square root consistent across the chain.

The algebraic content is therefore one sentence: nilpotency is a one-site fact, and the string is the price of a consistent global choice of square root.

**Boundary.** Jordan–Wigner is an equivalence of algebras on a chain, not a derivation of fermions from spins. The string is a nonlocal rewriting; it changes the locality of the operators, not the spectrum. The algebra supplies the one-site nilpotent, not the chain.

### Grassmann Coherent States Are the Minimal Odd Extension

A fermionic coherent state is written with a Grassmann label $\theta$,

$$
|\theta\rangle_{*}=|0\rangle+\theta|1\rangle,
\qquad
\theta^2=0 .
$$

The label is odd, and the algebra $\mathbb{B}$ is even. The Grassmann algebra generated by one odd variable per mode is a minimal extension in which the fermionic grading can be written. The states of the original algebra are even; the odd label is a coordinate on the coherent-state manifold, not a state.

**Boundary.** The odd generator is not an element of $\mathbb{B}$. The extension $\mathbb{B}\otimes\Lambda$ is not unique, and the Berezin integral is an extra structure on it. The algebra supplies the even carrier; the odd label is the minimal addition that makes the grading writable.

### The WKB Phase Gradient Avoids the Cone

In the semiclassical approximation the leading-order momentum is the phase gradient, the real quaternion

$$
\nabla S=\sum_\mu\frac{\partial S}{\partial Q_\mu}\vec e_\mu .
$$

The Hamilton–Jacobi equation fixes its norm to the energy defect,

$$
\langle\nabla S\rangle_{\natural}=2m(E-V).
$$

In the classically allowed region this is positive, and the gradient is never a nonzero nilpotent. The cone $\langle\nabla S\rangle_{\natural}=0$ is reached only where $\nabla S=0$, at a turning point: the gradient vanishes, and the origin is not a nilpotent either. A material four-momentum is a different object, since it carries the energy as its imaginary scalar part; its mass shell is not the level set of the phase gradient.

**Boundary.** The statement is about the leading order. Caustics, tunneling and backreaction are outside it. The gradient is not the wavefunction, and the WKB approximation is not exact. The algebra says where the leading-order momentum can live; it does not say that the exact solution stays there.

### The Dirac Point of Graphene Is a Null Momentum

The effective Hamiltonian of graphene near a Dirac point is linear in the momentum, $H=v_F(k_x\sigma_x+k_y\sigma_y)$, and its square is quadratic, $H^2=v_F^2|\vec k|^2I$. The linear branch is the square root of the quadratic symbol. The Dirac point is the apex of the cone, and the gapless excitations around it lie on the null cone $\langle\tilde P\rangle_{\natural}=0$.

In the biquaternion interpretation the physical branch is the **zero-divisor cone**: a null four-momentum is a zero divisor, and the node is its apex. The nilpotent appears in the **chiral block** of the symbol, where the raising and lowering combinations of the Pauli matrices are square-zero; it is the algebraic corner of the branch, not the four-momentum of a particle on it. The Dirac point itself is where the momentum vanishes, and the origin is not a nilpotent.

**Boundary.** The lattice model, the two valleys and the topological protection are input. The algebra supplies the form of the linear branch and the null cone; it does not derive the band structure of graphene. The physical branch is the zero-divisor cone, not the nilpotent cone; the phrase "nilpotent corner" names the algebraic form of the chiral block, not a particle with a nonzero momentum.

### Nielsen–Ninomiya Is a Pairing of Lattice Null Points

On a periodic lattice the zeros of the Bloch symbol are counted by topology. The signed count is the degree of the symbol on the boundary of the Brillouin zone; on a torus the boundary is empty, so the count vanishes and the zeros come in pairs of opposite chirality. A single null point cannot be removed by a local deformation. The nilpotent is the local square-zero corner, and the pairing is the global statement that the corners cannot be unpaired.

**Boundary.** The theorem assumes a local, periodic, finite-range Hamiltonian with a Hermitian symbol. It is a no-go statement, not a construction. The algebra sees the local null symbol; the signed count is a property of the band bundle over the Brillouin zone, not of the algebra alone. A lattice with defects or a boundary can evade the pairing, and the theorem says nothing about that case.

### The Fermionic Wick Theorem Is Exact

For a single nilpotent mode, a product that contains a repeated mode vanishes, because the repeated pair squares to zero. The only nonzero contractions are the two-point ones, and the graph expansion terminates. This is why the fermionic Wick theorem is an exact operator identity for the mode and not an approximation: there is no infinite series of higher contractions to resum.

**Boundary.** The statement is per mode. For a fermionic field the standard Grassmann Wick theorem is exact, but its exactness is a property of the Grassmann algebra, not of $\mathbb{B}$ alone; the single mode is the smallest instance. The algebra's nilpotency supplies the mode, not the Gaussian state or the measure. The theorem is not a substitute for the path integral, and it does not by itself define the vacuum.

### The Ladder Is Capped at Two Rungs

A nilpotent raising operator climbs one step and stops. The identity splits into at most two orthogonal idempotents, as the pair $\tilde\Pi_\pm$ shows, and no three-level module exists in $\mathbb{B}$. The qutrit is outside the algebra. The cap is the $2\times2$ matrix model: a complex module has dimension two, and three mutually orthogonal rank-one idempotents cannot fit.

**Boundary.** The cap is on the native module, not on composite systems. Two qubits give four levels, and a qutrit can be embedded in $M_3(\mathbb{C})$, but not in $\mathbb{B}$. The algebra says that its own ladder has two rungs; it does not say that nature has only two levels.

### Squeezing Is a Contraction to the Cone

A contraction of the algebra rescales the structure constants and the norm together. In the corpus's example the bracket and the norm degenerate as

$$
[E_2,E_3]=2\epsilon^2E_1,
\qquad
\langle E_2\rangle_{\natural}=\epsilon^2e_t,
$$

so that at $\epsilon=0$ the elements $E_2$ and $E_3$ are nilpotent and mutually annihilating, the bracket $[E_2,E_3]$ vanishes while $[E_1,E_2]$ and $[E_1,E_3]$ survive, and the basis elements that were invertible are zero divisors. The cone is the limiting locus of the degeneration.

**Boundary.** A contraction is a limit of algebras, not a physical squeezing process. The family lives outside $\mathbb{B}$ at nonzero $\epsilon$, and the cone is a boundary of the family, not a dynamics. No state is squeezed by the algebra; the interpretation explains why the cone is the endpoint, not how a physical system reaches it.

## The Nilpotent in One Table

The nine interpretations share one algebraic object and divide its roles. The table states the division.

| interpretation | the object it uses | what the algebra supplies | what it does not supply |
| --- | --- | --- | --- |
| Dirac's hole | nilpotent mode against the vacuum | exclusion as square-zero composition | the sea, the hole's quantum numbers |
| Jordan–Wigner | one-site nilpotent | the local square root | the chain and the string |
| Grassmann coherent states | odd label $\theta$ | the even carrier to be extended | the odd generator, the Berezin integral |
| WKB | phase gradient | the energy defect as a norm | the approximation, the caustics |
| graphene | null momentum | the linear branch as a square root | the lattice and the valleys |
| Nielsen–Ninomiya | null points of the symbol | the local square-zero corner | the global index and its pairing |
| Wick theorem | one nilpotent mode | termination of the expansion | the Gaussian state |
| qutrit | two-rung ladder | the cap at two idempotents | composite level counting |
| squeezing | contraction parameter | the cone as a limit | the physical process |

## Limits

The algebra supplies the mode, not the field content. It gives the nilpotent, the ladder and the pairing, but no mass, no coupling and no dynamics. The lattice interpretations are topological and model-dependent; the algebra is not a lattice. The WKB interpretation is leading order; the exact solution, the caustics and the tunneling are outside it. The fermionic ladder is one mode; a field is a collection of modes, and the qutrit is outside $\mathbb{B}$. The contraction is a limit, not a process.

The sharpest limit is the one stated at the outset. The nilpotent is not the physical null four-momentum. The physical null vector is a zero divisor with a nonzero square; the nilpotent is a pure displacement with a zero square. The two are distinct elements of the same cone, and the distinction is the boundary of every interpretation in this article.

## Summary

A nilpotent is a nonzero square-zero element of $\mathbb{B}$, necessarily pure with an isotropic complex vector part. The algebra places it in a four-real-dimensional cone inside the six-real-dimensional zero-divisor cone. A pair of nilpotents with anticommutator $e_t$ is a fermionic mode, and their products are two orthogonal idempotents, the two rungs of the algebra's ladder. The nine interpretations use that object as a mode, a lattice null point and a limit. The Dirac hole is not the nilpotent; the physical null four-momentum is a zero divisor, not a nilpotent; the odd Grassmann label is outside the algebra; the ladder stops at two rungs; and the contraction reaches the cone only at the degenerate end of a family. The algebra supplies the mode, the local square-zero corner and the boundary of the limit, and it supplies no dynamics.

## Summary of Notation

| notation | meaning |
| --- | --- |
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $\vec\Upsilon$ | a pure nilpotent, $\vec\Upsilon^2=0$, $\vec\Upsilon\neq0$ |
| $\tilde\Pi$ | an idempotent, $\tilde\Pi^2=\tilde\Pi$ |
| $\vec\Upsilon_x,\vec\Upsilon_y$ | the canonical nilpotent pair, $\vec\Upsilon_x^2=\vec\Upsilon_y^2=0$, $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$ |
| $\tilde\Pi_\pm$ | the two orthogonal idempotents $\vec\Upsilon_x\vec\Upsilon_y$ and $\vec\Upsilon_y\vec\Upsilon_x$ |
| $\langle\tilde Q\rangle_{\natural}$ | the natural norm $\sum_\mu Q_\mu^2$ |
| $\mathbb{M}_-$ | the material sector, the anti-Hermitian subspace |
| $\mathbb{M}_+$ | the informational sector, the Hermitian subspace |
| $\theta$ | a Grassmann odd label, $\theta^2=0$, outside $\mathbb{B}$ |
| $\tilde P$ (four-momentum) | a material four-momentum, $\tilde P=i(E/c)e_t+\vec p$ |

## Further Reading

- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the distinction between the nilpotent cone and the physical light cone.
- [The Physical Interpretation of the 12 Products](the-physical-interpretation-of-the-12-products.html), for the root sets of $0$ in the twelve products.
- [Roots, Idempotents and Observables](roots-idempotents-and-observables.html), for the idempotents as states and the roots of $+1$.
- [Roots, Idempotents and Quantum Information](roots-idempotents-and-quantum-information.html), for the idempotent basis of the qubit and the stabilizer codes.
- [The Spinor Module and Its Two Structures](the-spinor-module-and-its-two-structures.html), for the module on which the ladder acts.
- [The Complementary Ideal and the Second State Space](the-complementary-ideal-and-the-second-state-space.html), for the mass coupling as a nilpotent matrix unit.
- [The Dirac Sea, Hole Theory and Antimatter in Biquaternionic Form](the-dirac-sea-hole-theory-and-antimatter-in-biquaternionic-form.html), for the hole-theory reading.
- [The Jordan–Wigner Transformation in Biquaternionic Form](the-jordan-wigner-transformation-in-biquaternionic-form.html), for the one-site square root and the string.
- [Grassmann Coherent States in Biquaternionic Form](grassmann-coherent-states-in-biquaternionic-form.html), for the odd extension.
- [The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form](the-wkb-approximation-and-the-hamilton-jacobi-equation-in-biquaternionic-form.html), for the phase gradient.
- [Dirac Matter: Graphene, Dirac Cones and Topological Insulators in Biquaternionic Form](dirac-matter-graphene-dirac-cones-and-topological-insulators-in-biquaternionic-form.html), for the Dirac point.
- [Fermion Doubling and the Nielsen–Ninomiya Theorem in Biquaternionic Form](fermion-doubling-and-the-nielsen-ninomiya-theorem-in-biquaternionic-form.html), for the lattice pairing.
- [The Wick Theorem in Biquaternionic Form](the-wick-theorem-in-biquaternionic-form.html), for the exact fermionic expansion.
- [The Qutrit Problem: Three-Level Systems Outside the Biquaternion Algebra](the-qutrit-problem-three-level-systems-outside-the-biquaternion-algebra.html), for the two-rung cap.
- [Squeezing Beyond the Biquaternion Algebra](squeezing-beyond-the-biquaternion-algebra.html), for the contraction.
