# __The N-Degenerate, Spectrally Degenerate Sector: The Vacuum and the Nilpotent Ladder__

## Introduction

The cell $\Sigma_{00}$ is the set of elements for which both invariants vanish: $N=0$ and $B^2=0$. The characteristic polynomial is $X^2$, the element is square-zero,

$$
\tilde Q^2=0,
$$

and the two eigenvalues are both zero. The cell is the intersection of the null cone and the spectral cone, the degenerate stratum of the arrangement.

It has two faces. The **origin** is the only semisimple element: the zero element, with no scale, no mode and no direction. The **nilpotent cone** is the set of non-zero pure isotropic vectors: elements that square to zero but are not zero. On the material slice only the origin survives. In the full algebra the nilpotents are the fermionic ladder: a pair of them anticommutes to the identity, and their products are the two orthogonal rungs of a two-level system.

The physical content is therefore the **vacuum and its nilpotent excitations**. The article reads the cell, the origin, the nilpotent, the ladder and the products. It proves nothing; the nilpotent cone and the ladder are those of *The Square-Zero Element: Nilpotency as Mode, Differential and Supercharge*, and the sector theorems are those of *The N-Degenerate, Spectrally Degenerate Sector*.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The definition, the five descriptions and the geometry of the cell | [The N-Degenerate, Spectrally Degenerate Sector](../articles_maths/the-n-degenerate-spectrally-degenerate-sector.html) |
| The nilpotent cone, the ladder and the ladder action | [The Square-Zero Element: Nilpotency as Mode, Differential and Supercharge](the-square-zero-element-nilpotency-as-mode-differential-and-supercharge.html) |
| The zero-divisor cone and its strata | [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html) |
| The primitive idempotents and the minimal left ideals | [The Minimal Left Ideals](../articles_maths/the-minimal-left-ideals.html) |
| The independence of the two conditions | [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html) |
| The four-vector dictionary and the origin | [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) |
| The indefinite form and the cone | [The Krein Form and the Indefinite Structure](the-krein-form-and-the-indefinite-structure.html) |

## The Cell

The cell is

$$
\Sigma_{00}=\{N=0,\ B^2=0\}
=\{Q_t^2+B^2=0,\ B^2=0\}
=\{Q_t=0,\ (\vec Q,\vec Q)=0\}.
$$

The two conditions force the scalar part to vanish, so the cell is the set of pure isotropic vectors:

$$
\Sigma_{00}=\{\vec\Upsilon\ :\ \vec\Upsilon^2=0\}.
$$

It is the **nilpotent cone** — the non-zero pure isotropic vectors — with the origin adjoined. It has complex dimension two and real dimension four. The cone is not a manifold at the origin; the origin is its vertex. Off the origin the element is a non-zero nilpotent.

The characteristic polynomial is

$$
p_{\tilde Q}(X)=X^2,
\qquad
\lambda_+=0,
\qquad
\lambda_-=0,
$$

and the minimal polynomial is

$$
m_{\tilde Q}(X)=X
\quad\text{at the origin},
\qquad
m_{\tilde Q}(X)=X^2
\quad\text{off the origin}.
$$

The origin is semisimple; every non-zero nilpotent is defective, with a single Jordan block of size two. The cell is the only one in which the two eigenvalues are equal **and** zero; it is the common limit of the rest frame and the light ray.

## The Vacuum

The origin is the zero element:

$$
\tilde Q=0,
\qquad
N=0,
\qquad
B^2=0,
\qquad
Q_t=0.
$$

It is the unique element with no scale, no mode and no direction. On the material slice it is the only point of the cell:

$$
Q_t=0,\quad\vec p=0
\quad\Longleftrightarrow\quad
N=0,\quad B=0.
$$

The reading is the **vacuum**: the zero four-momentum, the element that carries neither mass nor motion. It is the additive zero, not the multiplicative identity. The identity $e_t$ is a unit, with $N=1$ and $B^2=0$; it lies on the scalar line of $\Sigma_{10}$, not in $\Sigma_{00}$, and the vacuum is not a state with a norm.

The origin is the apex of the arrangement. Every cell has the origin in its closure:

$$
0\in\overline{\Sigma_{11}}\cap\overline{\Sigma_{10}}\cap\overline{\Sigma_{01}}\cap\overline{\Sigma_{00}}.
$$

The reading is the common limit: a massive particle at rest, a light ray, and a nilpotent all degenerate to the zero element when their scale is sent to zero. The limit is not a physical process; it is the geometry of the cones.

## The Nilpotent

### The Element

Off the origin the element is a pure isotropic vector:

$$
\vec\Upsilon=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,
\qquad
Q_x^2+Q_y^2+Q_z^2=0,
\qquad
\vec\Upsilon^2=0.
$$

It is defective, with minimal polynomial $X^2$ and a single Jordan block. The centraliser is the dual-number algebra

$$
\mathbb{C}[\vec\Upsilon]=\{a e_t+b\vec\Upsilon\}
\cong\mathbb{C}[\varepsilon]/(\varepsilon^2),
$$

whose only idempotents are $0$ and $e_t$. No non-trivial idempotent commutes with $\vec\Upsilon$, so no non-trivial Peirce decomposition is attached to it and there is no spectral decomposition. A Peirce decomposition still exists relative to an idempotent adapted to the nilpotent; in it $\vec\Upsilon$ lies in the mixed corner. The closest structure is the flag

$$
0\subset\mathbb{C}\vec\Upsilon\subset\ker L_{\vec\Upsilon},
$$

and the flag is the whole of the invariant data.

The powers and the exponential are

$$
\vec\Upsilon^n=0\quad(n\ge2),
\qquad
e^{\theta\vec\Upsilon}=e_t+\theta\vec\Upsilon.
$$

The exponential is a shear, not a rotation. There is no inverse and no logarithm: $\vec\Upsilon$ is a zero divisor, and the exponential is invertible.

### The Reading

The physical reading of the nilpotent is the **fermionic mode**, and it needs a pair. A single nilpotent is a square-zero direction; the ladder is a pair.

The canonical pair is

$$
\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y),
\qquad
\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y),
\qquad
\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t.
$$

Both are nilpotent, and their products are orthogonal idempotents:

$$
\tilde\Pi_+=\vec\Upsilon_x\vec\Upsilon_y=\tfrac12(e_t+i\vec e_z),
\qquad
\tilde\Pi_-=\vec\Upsilon_y\vec\Upsilon_x=\tfrac12(e_t-i\vec e_z),
$$

with

$$
\tilde\Pi_++\tilde\Pi_-=e_t,
\qquad
\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0.
$$

Both idempotents are Hermitian and lie in the informational sector. The action is the ladder:

$$
\vec\Upsilon_x\tilde\Pi_-=\vec\Upsilon_x,
\qquad
\vec\Upsilon_y\tilde\Pi_+=\vec\Upsilon_y,
\qquad
\vec\Upsilon_x\tilde\Pi_+=\vec\Upsilon_y\tilde\Pi_-=0.
$$

The reading is a two-level system: two rungs, two raising and lowering operators, and a vacuum. The algebra is the full $2\times2$ matrix algebra, so the ladder has exactly two rungs; there is no third orthogonal idempotent.

### What the Nilpotent Is Not

The nilpotent is not a physical null four-momentum. A massless momentum has $N=0$ but $B^2\neq0$, and its square is

$$
\tilde P^2=2P_t\tilde P\neq0.
$$

The photon is a zero divisor of the light-ray cell $\Sigma_{01}$, not a nilpotent. The nilpotent is the pure lightlike displacement, the element whose composition with itself is nothing. The distinction is the distinction between the two degenerate cells.

The nilpotent is not an idempotent. The two classes meet only at the origin. An idempotent is a rung; a nilpotent is a ladder operator between rungs. The product of two nilpotents can be a non-zero element of the light-ray cell; the product of an idempotent with itself is itself.

The nilpotent is not a Grassmann label. A Grassmann number $\theta$ with $\theta^2=0$ lives outside the algebra; the nilpotent is an element of the algebra. The algebraic square-zero and the exterior square-zero are different structures, and the ladder is the bridge between them.

## Products and the Boundary

The cell is not closed under products. The product of two elements of the cell is null,

$$
\Sigma_{00}\cdot\Sigma_{00}\subseteq\{0\}\cup\Sigma_{01},
$$

and both outcomes occur. The product of two orthogonal nilpotents is zero; the product of the ladder pair is an idempotent in $\Sigma_{01}$, because a non-zero idempotent has $N=0$ and $B^2\neq0$. The product never leaves the null cone.

The cell is the boundary of both degenerate cells:

$$
\Sigma_{00}=\overline{\Sigma_{10}}\cap\overline{\Sigma_{01}}
=\overline{\Sigma_{10}}\cap\overline{\Sigma_{01}}\cap\overline{\Sigma_{11}}.
$$

A path in the rest-frame cell that sends $Q_t\to0$ lands in $\Sigma_{00}$: at the origin if the nilpotent part also vanishes, and at a non-zero nilpotent otherwise. A path in the light-ray cell that sends the scale to zero lands at the origin. A path in the two-mode cell that sends both invariants to zero lands somewhere in $\Sigma_{00}$, not necessarily at the origin. The origin is in the closure of every cell; the nilpotent cone is the tangent cone at the origin.

## Physical Interpretations

- **The origin is the vacuum.** The zero four-momentum, the unique element with no scale and no mode. It is the additive zero, not the identity and not a state with a norm.
- **The nilpotent is a fermionic mode.** A square-zero direction; a pair of them anticommutes to the identity; their products are the two rungs of a two-level system.
- **The ladder is capped at two rungs.** The algebra is $M_2(\mathbb{C})$, the module is two-dimensional, and there is no third orthogonal idempotent. The reading is a single fermionic mode, not a field.
- **The square-zero is exclusion.** Applying the same nilpotent twice gives zero; the mode cannot be occupied twice. The algebraic statement is the skeleton of the Pauli exclusion principle, not its derivation.
- **The vacuum is not the identity.** $e_t$ is a unit on the scalar line; the vacuum is $0$. Zero is not the multiplicative identity, and the two must not be confused.
- **The origin is the apex of the arrangement; the cell is the common boundary.** Every cell has the origin in its closure; the nilpotent cone is the tangent cone at the origin. The vacuum is the limit of every regime.
- **The nilpotent is not a photon.** A massless momentum is a zero divisor with $B^2\neq0$ and a non-zero square; a nilpotent has $B^2=0$ and a zero square. The two degenerate cells are different physical regimes.
- **The ladder is the bridge to the state space.** The nilpotents are not Hermitian, but their products are; the rungs lie in the informational sector. The reading connects the vacuum cell to the two-state space.

## Limits

The vacuum reading needs the material slice. On the full algebra the origin is the zero element, and calling it a vacuum is an identification with the zero four-momentum.

The fermionic reading is algebraic. The ladder is a pair of nilpotents with the anticommutator $e_t$; the identification with a physical fermionic mode, with statistics and with a field is an extra step, not a theorem of the cell.

The nilpotent cone is not on the real material slice. A real four-momentum with $N=0$ and $B=0$ is the origin. The non-zero nilpotents need a complex isotropic spatial vector.

The square-zero is not a derivation of the exclusion principle. It is the algebraic form of a two-rung ladder; the spin-statistics theorem is not proved here.

No dynamics is supplied. The cell says what the vacuum and the nilpotents are at an instant; it does not supply a Hamiltonian, a field or a scattering amplitude.

## Summary

- $\Sigma_{00}=\{N=0,\ B^2=0\}=\{\vec\Upsilon:\vec\Upsilon^2=0\}$ is the nilpotent cone, of real dimension four, with the origin as vertex.
- The origin is the vacuum: the zero four-momentum, the unique element with no scale and no mode; it is the additive zero, not the identity.
- Off the origin the element is a non-zero nilpotent: defective, minimal polynomial $X^2$, dual-number centraliser, no idempotent, no canonical Peirce decomposition; a chosen adapted idempotent gives $J_2(0)$, and there is no inverse and no logarithm.
- A pair of nilpotents with anticommutator $e_t$ is the fermionic ladder; their products are two orthogonal Hermitian idempotents, the two rungs.
- The ladder has exactly two rungs; the algebra is $M_2(\mathbb{C})$ and the module is two-dimensional.
- The product of two nilpotents is zero or a scaled idempotent in $\Sigma_{01}$; the cell is not product-closed.
- The cell is the common boundary of the arrangement: every cell has the origin in its closure, and the nilpotent cone is the tangent cone at the origin.
- The nilpotent is not a photon: a massless momentum has $B^2\neq0$ and a non-zero square; a nilpotent has $B^2=0$ and a zero square.
- The cell supplies no dynamics, no field, no statistics and no derivation of exclusion.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\Sigma_{00}$ | the cell $N=0$, $B^2=0$ |
| $\vec\Upsilon$ | a pure nilpotent, $\vec\Upsilon^2=0$ |
| $\vec\Upsilon_x,\vec\Upsilon_y$ | the ladder pair, $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$ |
| $\tilde\Pi_\pm$ | the two rungs, $\tilde\Pi_+=\vec\Upsilon_x\vec\Upsilon_y$, $\tilde\Pi_-=\vec\Upsilon_y\vec\Upsilon_x$ |
| $L_{\vec\Upsilon}$ | left multiplication by the nilpotent |
| $e^{\theta\vec\Upsilon}=e_t+\theta\vec\Upsilon$ | the shear exponential |

## Further Reading

- [The Four Regimes of an Element: Mass and Motion](the-four-regimes-of-an-element-mass-and-motion.html), for the partition and the other three cells.
- [The Square-Zero Element: Nilpotency as Mode, Differential and Supercharge](the-square-zero-element-nilpotency-as-mode-differential-and-supercharge.html), for the nine interpretations of the nilpotent.
- [The N-Degenerate, Spectrally Regular Sector: The Massless Regime](the-n-degenerate-spectrally-regular-sector-the-massless-regime.html), for the other degenerate cell.
- [The N-Regular, Spectrally Degenerate Sector: The Rest Frame and the Exceptional Point](the-n-regular-spectrally-degenerate-sector-the-rest-frame-and-the-exceptional-point.html), for the defective unit.
- [Spin and the Three Elementary Carriers](spin-and-the-three-elementary-carriers.html), for the rungs and the state space.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the nesting of the cones.
