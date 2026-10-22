
# __Split-Biquaternion Split-Complex Subspace__

## Introduction

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ carries four linear involutions, and each of them splits $\mathbb{H}_{\mathbb{D}}$ into a fixed space and an anti-fixed space. Four of the resulting spaces — the split complex subspace, the quaternion subspace, the Hermitian subspace and the anti-Hermitian subspace — are the distinguished real subspaces of the algebra and are the subject of the four single-subspace articles. This article treats the smallest of them, the **split complex subspace** $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, on its own: its definition, its basis, its algebra structure, the restriction of the split-biquaternion norm to it, its idempotents and zero divisors, the action of the four involutions upon it, and its intersections with the other subspaces. The companions are *Split-Biquaternion Quaternion Subspace*, *Split-Biquaternion Hermitian Subspace* and *Split-Biquaternion Anti-Hermitian Subspace*; their relations with one another are collected in *Split-Biquaternion Relations Between Subspaces*, and the involutions themselves in *Split-Biquaternion Involution Lattice*.

The treatment is purely mathematical. No physics is invoked. The split biquaternion algebra is assumed from the basic algebra article, the split complex algebra $\mathbb{D}$ from the article on split complex algebra, and the quaternion algebra $\mathbb{H}$ from the article on quaternion algebra. The two idempotents $\tilde\Pi_1 = \tfrac{1}{2}(1 + j)$ and $\tilde\Pi_2 = \tfrac{1}{2}(1 - j)$ and the isomorphism $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$ are assumed known.

Throughout, elements are written $\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$ with $Q_\mu = q_\mu + j q'_\mu \in \mathbb{D}$, and the conjugations are ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (split complex), ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ (Hermitian) and ${}^{\flat} = -{}^{*}$ (anti-Hermitian). The split-biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$.

## Definition and Basis

**Definition.** The **split complex subspace** is the fixed space of quaternion conjugation,

$$
\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} = \left\{ \tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \tilde{Q}^{\natural} = \tilde{Q} \right\},
$$

where quaternion conjugation is $\tilde{Q}^{\natural} = Q_t e_t - Q_x \vec e_x - Q_y \vec e_y - Q_z \vec e_z$.

Since ${}^{\natural}$ is an involution, it has eigenvalues $\pm 1$ and $\mathbb{H}_{\mathbb{D}}$ is the direct sum of its fixed space and its anti-fixed space. The anti-fixed space is the **vector subspace** $\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$, the set of elements with vanishing split scalar part, of real dimension $6$; it has no dedicated article in this series, and is mentioned only where a relation requires it.

### The Condition in Coordinates

Comparing the two sides of $\tilde{Q}^{\natural} = \tilde{Q}$ coefficient by coefficient: the coefficient of $e_t$ gives $Q_t = Q_t$, no condition; the coefficient of $\vec e_\mu$ gives $-Q_\mu = Q_\mu$, that is $Q_\mu = 0$, for $\mu\in\{x,y,z\}$. The subspace is therefore the set of elements with **vanishing vector part**,

$$
\tilde{Q} = Q_t e_t, \qquad Q_t \in \mathbb{D}.
$$

### Basis and Dimension

**Proposition.** The split complex subspace is a real vector space of dimension $2$, with basis $e_t, j$. In real coordinates it is the coordinate plane $q_x = q_y = q_z = q'_x = q'_y = q'_z = 0$, with the two free parameters $q_t$ and $q'_t$.

**Proof.** The four split complex coefficients reduce to $Q_t$ alone, and a split complex number is a real pair $Q_t = q_t + j q'_t$; the elements $e_t$ and $j$ are linearly independent over $\mathbb{R}$ and span the set.

Of the four distinguished subspaces, $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is the only one of dimension $2$; the other three have dimension $4$.

## Algebra Structure

### It Is the Centre of the Algebra

**Theorem.** $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is the centre of $\mathbb{H}_{\mathbb{D}}$,

$$
\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} = \left\{ \tilde{Q}_1 \in \mathbb{H}_{\mathbb{D}} : \tilde{Q}_1\tilde{Q}_2 = \tilde{Q}_2\tilde{Q}_1 \ \text{for every} \ \tilde{Q}_2 \in \mathbb{H}_{\mathbb{D}} \right\}.
$$

**Proof.** An element commutes with every other element if and only if it commutes with the basis elements $\vec e_x, \vec e_y, \vec e_z$, and $Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$ commutes with all three precisely when $Q_x = Q_y = Q_z = 0$, because $Q_\mu \vec e_\mu$ anticommutes with the other quaternion units. The central elements are then the $\mathbb{D}$-multiples of $e_t$, which is the fixed space of ${}^{\natural}$.

The subspace therefore has two descriptions: it is the fixed space of quaternion conjugation, and it is the centre of the algebra. Its elements are the **central elements**, written $Q_t e_t$ with $Q_t \in \mathbb{D}$.

### Subalgebra, Commutativity, and the Absence of a Field Structure

**Proposition.** $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is a subalgebra of $\mathbb{H}_{\mathbb{D}}$, it is commutative, and as a real algebra it is isomorphic to $\mathbb{D}$ via $Q_t e_t \mapsto Q_t$.

**Proof.** For two central elements, $(Q_{1t} e_t)(Q_{2t} e_t) = (Q_{1t} Q_{2t}) e_t$, which lies in the subspace; commutativity is the commutativity of $\mathbb{D}$; and the displayed map is a bijective ring homomorphism because $e_t$ is the unit.

The subspace is a **subalgebra**, and it is one of the two subalgebras among the four distinguished subspaces, the other being the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$. It is the only **commutative** one. Unlike the biquaternion centre, however, it is **not a field**: the split complex algebra is not a division algebra, having the zero divisors $\tilde\Pi_1$ and $\tilde\Pi_2$. As a real algebra it is $\mathbb{R} \oplus \mathbb{R}$ through the idempotent basis, and its group of units is the four open quadrants of the plane, not the punctured plane.

### Ideals

Being the centre, $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ acts on $\mathbb{H}_{\mathbb{D}}$ by scalar extension: $\mathbb{H}_{\mathbb{D}}$ has $\mathbb{D}$-basis $e_t, \vec e_x, \vec e_y, \vec e_z$. The subspace is not a proper two-sided ideal of $\mathbb{H}_{\mathbb{D}}$; the two coordinate lines $\mathbb{R} \tilde\Pi_1$ and $\mathbb{R} \tilde\Pi_2$ inside it are two-sided ideals of the subalgebra $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, and they are the intersections with the centre of the minimal ideals $\mathbb{H} \tilde\Pi_1$ and $\mathbb{H} \tilde\Pi_2$ of the algebra. The ideal theory of the algebra is developed in *Split-Biquaternion Ideals and Peirce Decomposition*, and that of the centre is the ideal theory of $\mathbb{R} \oplus \mathbb{R}$.

### Multiplication Tables

The products within the subspace and with the vector units are

| product | value | product | value |
|---|---|---|---|
| $e_t \cdot e_t$ | $e_t$ | $e_t \cdot \vec e_\mu$ | $\vec e_\mu$ |
| $j \cdot e_t$ | $j$ | $j \cdot \vec e_\mu$ | $j \vec e_\mu$ |
| $e_t \cdot j$ | $j$ | $\vec e_\mu \cdot e_t$ | $\vec e_\mu$ |

for $\mu\in\{x,y,z\}$. The table states that $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ multiplies into every subspace and is multiplied into by every subspace with no sign change: multiplication by a central element is a scalar extension, and the vector subspace is closed under multiplication by $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ in the same way.

## The Split-Biquaternion Norm

**Proposition.** On the split complex subspace the split-biquaternion norm is the square of the coefficient,

$$
\langle\tilde{Q}\rangle_{\natural} = Q_t^2, \qquad \tilde{Q} = Q_t e_t.
$$

**Proof.** $\tilde{Q}^{\natural} = \tilde{Q}$ on the subspace, so $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \tilde{Q}^2 = Q_t^2 e_t$, read as the split complex scalar $Q_t^2$.

Two features are worth isolating. First, $\langle\cdot\rangle_{\natural}$ takes **split complex** values on the subspace: writing $Q_t = q_t + j q'_t$, one has $Q_t^2 = (q_t^2 + q'^2_0) + 2 j q_t q'_t$, real on the lines $q'_t = 0$ and $q_t = 0$ separately but not in general. Second, the real restriction in the basis $e_t, j$ has the matrix $\operatorname{diag}(1, 1)$ on the real part and $2 q_t q'_t$ on the split-imaginary part, so the associated quadratic form is **not** definite: this is the form $\langle\cdot\rangle_{\natural}$ restricted to the two-dimensional centre, and its isotropic lines are the light lines $Q_t = a \tilde\Pi_{1,2}$.

### Units and Zero Divisors

**Theorem.** For $\tilde{Q} = Q_t e_t$, the following are equivalent:

1. $\tilde{Q}$ is a unit of $\mathbb{H}_{\mathbb{D}}$;
2. $\langle\tilde{Q}\rangle_{\natural} = Q_t^2$ is a unit of $\mathbb{D}$;
3. $Q_t$ is a unit of $\mathbb{D}$, that is $Q_t = q_t + j q'_t$ with $q_t^2 \neq q'^2_0$.

The inverse is $\tilde{Q}^{-1} = Q_t^{-1} e_t = \dfrac{\bar{Q_t}}{Q_t \bar{Q_t}} e_t = \dfrac{q_t - j q'_t}{q_t^2 - q'^2_0} e_t$.

**Proof.** $\langle Q_t e_t\rangle_{\natural} = Q_t^2$ is a unit of $\mathbb{D}$ exactly when $Q_t$ is, since $\mathbb{D}$ is commutative; a split complex number is a unit precisely when its real form norm $q_t^2 - q'^2_0$ is nonzero. The inverse formula is the standard inverse in $\mathbb{D}$.

**Corollary.** The zero divisors of the split complex subspace are exactly the nonzero elements of the two **light lines**

$$
\mathbb{R} \tilde\Pi_1 \cup \mathbb{R} \tilde\Pi_2, \qquad \tilde\Pi_1 = \tfrac{1}{2}(1 + j), \quad \tilde\Pi_2 = \tfrac{1}{2}(1 - j),
$$

and the annihilator of each light line is the other.

**Proof.** A split complex number $Q_t = q_t + j q'_t$ is a zero divisor exactly when $q_t^2 = q'^2_0$, that is $q_t = \pm q'_t$, which is the union of the lines $\mathbb{R}(1 + j) = \mathbb{R} \tilde\Pi_1$ and $\mathbb{R}(1 - j) = \mathbb{R} \tilde\Pi_2$. Since $\tilde\Pi_1 \tilde\Pi_2 = 0$, each line annihilates the other.

This is the first sharp difference from the biquaternion centre: there the split-biquaternion norm vanished only at the origin and the subspace was a field, whereas here the split-biquaternion norm degenerates on two lines and the subspace is only a product of fields.

## The Idempotents of the Centre

**Proposition.** The idempotents of $\mathbb{H}_{\mathbb{D}}$ all lie in the split complex subspace, and they are exactly

$$
0, \qquad \tilde\Pi_1, \qquad \tilde\Pi_2, \qquad 1.
$$

**Proof.** Solve $Q_t^2 = Q_t$ in $\mathbb{D}$. In the idempotent basis $Q_t = \lambda_+ \tilde\Pi_1 + \lambda_- \tilde\Pi_2$, so $Q_t^2 = \lambda_+^2 \tilde\Pi_1 + \lambda_-^2 \tilde\Pi_2$; the equation holds exactly when $\lambda_+, \lambda_- \in \{0, 1\}$. The four combinations are $0, \tilde\Pi_1, \tilde\Pi_2, 1$. Every idempotent of $\mathbb{H}_{\mathbb{D}}$ is one of these, as proved in *Split-Biquaternion Idempotents and Projections*.

The idempotents $\tilde\Pi_1$ and $\tilde\Pi_2$ are the two nontrivial ones, they are orthogonal and primitive, and they lie in the centre — unlike the biquaternion case, where the nontrivial idempotents are noncentral and lie outside the centre. Since they are central, the decomposition $\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_1 \oplus \mathbb{H} \tilde\Pi_2$ generated by them is a decomposition into two-sided ideals. The idempotents are the only nonzero elements of the light lines that are idempotent; the remaining points of each light line are nilpotent-free zero divisors, and there are no nilpotents in the centre.

## The Four Involutions on It

Each of the four involutions preserves the condition $Q_x = Q_y = Q_z = 0$, so the subspace is invariant under all four. Their action in the basis $e_t, j$ is diagonal:

| involution | $\tilde{Q} = Q_t e_t$ | matrix on $e_t, j$ |
|---|---|---|
| ${}^{\natural}$ | $Q_t e_t$ | $\operatorname{diag}(1, 1)$ |
| $\bar{\cdot}$ | $\bar{Q_t} e_t$ | $\operatorname{diag}(1, -1)$ |
| ${}^{*}$ | $\bar{Q_t} e_t$ | $\operatorname{diag}(1, -1)$ |
| ${}^{\flat}$ | $-\bar{Q_t} e_t$ | $\operatorname{diag}(-1, 1)$ |

Quaternion conjugation fixes the subspace pointwise — it is the defining involution — and Hermitian conjugation agrees with split complex conjugation there, because ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ and ${}^{\natural}$ acts as the identity. Split complex conjugation acts as the exchange $j \mapsto -j$, the non-trivial involution of $\mathbb{D}$, and anti-Hermitian conjugation is its negative. So of the four involutions only ${}^{\natural}$ acts trivially on the centre, and $\bar{\cdot}$ is the one that swaps the two light lines $\mathbb{R} \tilde\Pi_1$ and $\mathbb{R} \tilde\Pi_2$.

## Relations to the Other Subspaces

The intersections of $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ with the other distinguished subspaces are, with dimensions:

| pair | intersection | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap \mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ | $\{0\}$ | $0$ |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{R}$ | $1$ |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_+$ | $\mathbb{R}$ | $1$ |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_-$ | $j\mathbb{R}$ | $1$ |

The two lines $\mathbb{R}$ and $j\mathbb{R}$ are the **coordinate blocks** of the centre, and it is their direct sum:

$$
\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} = \mathbb{R} \oplus j\mathbb{R}, \qquad \mathbb{R} = \mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} = \mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_+, \qquad j\mathbb{R} = \mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_-.
$$

The intersection with the vector subspace is the origin, so $\mathbb{H}_{\mathbb{D}} = \mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \oplus \mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ is the split scalar–vector decomposition of the algebra; with each of the other two subspaces the intersection is one-dimensional, so no pair among them spans $\mathbb{H}_{\mathbb{D}}$. The same pattern is recorded for all four subspaces in *Split-Biquaternion Relations Between Subspaces*.

## The Image in the Two Halves

Under the idempotent-decomposition isomorphism $\varphi : \mathbb{H}_{\mathbb{D}} \to \mathbb{H} \oplus \mathbb{H}$, a central element has image the pair of **real scalars**

$$
\varphi(Q_t e_t) = (Q_t^+, Q_t^-), \qquad Q_t^\pm = q_t \pm q'_t \in \mathbb{R}.
$$

The image of $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is therefore the set $\mathbb{R} \oplus \mathbb{R}$ of pairs of real scalars, the centre of $\mathbb{H} \oplus \mathbb{H}$. The split-biquaternion norm has the matching description

$$
\langle Q_t e_t\rangle_{\natural} = (Q_t^+)^2 \tilde\Pi_1 + (Q_t^-)^2 \tilde\Pi_2,
$$

the pair of squares of the two real scalars. The two light lines are the loci $Q_t^- = 0$ and $Q_t^+ = 0$, so the split-biquaternion norm degenerates on the coordinate axes of the pair, exactly as the two-dimensional split complex plane requires.

## The Analysis on the Split Complex Subspace

The centre is a copy of the split complex algebra $\mathbb{D}$, so the function theory it carries is the one-variable split complex analysis of *Split-Complex Analysis*. A differentiable function of the centre variable $Q_t = q_t + jq'_t$, written $f = u + jv$, satisfies the Cauchy–Riemann pair

$$
\partial/\partial q_t\,u = \partial/\partial q'_t\,v, \qquad \partial/\partial q'_t\,u = \partial/\partial q_t\,v,
$$

and the twice differentiable functions that are harmonic in the split complex sense solve the wave equation $\partial^2/\partial q_t^2 f - \partial^2/\partial {q'_t}^2 f = 0$ rather than the Laplace equation. Embedded in $\mathbb{H}_{\mathbb{D}}$, the centre inherits the restriction of the ambient Cauchy–Riemann operator of *Split-Biquaternion Analysis*, and on the centre that operator is the split complex Cauchy–Riemann operator above. The absence of an elliptic harmonic theory on the centre is the analytic expression of the indefiniteness of its split-biquaternion norm: the restricted form is $q_t^2 - q'^2_0$, of signature $(1,1)$, and its isotropic directions are the two null lines of the zero divisors.

## The Geometry of the Split Complex Subspace

As the fixed space of quaternion conjugation, the centre is the axis of that involution of the algebra, and geometrically it is the invariant plane of the corresponding linear involution of $\mathbb{R}^8$. Its own geometry is that of the split complex plane: the two null lines $\mathbb{R}(1+j)$ and $\mathbb{R}(1-j)$ are the zero divisors, the level set of unit norm is the pair of hyperbolas $q_t^2 - q'^2_0 = 1$, and the motions it carries are the hyperbolic rotations $Q_t\mapsto \exp(\theta j)Q_t$ of $\mathbb{D}$, the identity component of the group of units of $\mathbb{D}$ up to sign. The Euclidean form restricts to the ordinary Euclidean metric of the plane, while the Hermitian scalar form restricts to the split form $q_t^2 - q'^2_0$ of signature $(1,1)$, so the centre is an indefinite slice of the ambient algebra carrying the same null lines as the split complex plane.

## Summary

The split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is the fixed space of quaternion conjugation, the set of elements $\tilde{Q} = Q_t e_t$ with vanishing vector part; it is a real vector space of dimension $2$ with basis $e_t, j$. It coincides with the centre of the algebra, is a commutative subalgebra isomorphic to the split complex algebra $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$, and is one of the two subalgebras among the four distinguished subspaces. It is **not** a field: the split-biquaternion norm restricts to $N = Q_t^2$, which is split-complex-valued and degenerates on the two light lines $\mathbb{R} \tilde\Pi_{1,2}$, and these are exactly the zero divisors of the subspace, each annihilating the other. The units are the elements with $Q_t$ a unit of $\mathbb{D}$, that is $Q_t = q_t + j q'_t$ with $q_t^2 \neq q'^2_0$, and the inverse is $Q_t^{-1} e_t = (q_t - j q'_t)/(q_t^2 - q'^2_0)\, e_t$. All four idempotents $0, \tilde\Pi_1, \tilde\Pi_2, 1$ of the algebra lie in the subspace, unlike the biquaternion case, where the nontrivial idempotents are noncentral. Of the four involutions, quaternion conjugation fixes the subspace pointwise, split complex and Hermitian conjugations act by $j \mapsto -j$ and swap the two light lines, and anti-Hermitian conjugation is the negative of that. The subspace meets the vector subspace only at the origin and meets both the quaternion and Hermitian subspaces in $\mathbb{R}$, the anti-Hermitian subspace in $j\mathbb{R}$, so it is the direct sum of the two coordinate blocks $\mathbb{R}$ and $j\mathbb{R}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ | Split biquaternion algebra, real dimension $8$ |
| $\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$ | General element, $Q_\mu \in \mathbb{D}$ |
| $Q_\mu = q_\mu + j q'_\mu$ | Real and split-imaginary parts of a coefficient |
| $j$ | Split complex unit, central, $j^2 = +1$ |
| $\tilde\Pi_{1,2} = \tfrac{1}{2}(1 \pm j)$ | Idempotents, giving the light lines $\mathbb{R} \tilde\Pi_{1,2}$ |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | Split complex subspace, the centre, fixed space of ${}^{\natural}$ |
| $\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ | Vector subspace, the anti-fixed space of ${}^{\natural}$, $\dim 6$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}, \mathbb{M}_+, \mathbb{M}_-$ | Quaternion, Hermitian, anti-Hermitian subspaces |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ | The four conjugations |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Split-Biquaternion norm, restricting to $Q_t^2$ |
| $\varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-)$ | Idempotent-decomposition isomorphism |
| $\mathbb{R}, j\mathbb{R}$ | The two coordinate blocks of the centre |
| $\partial/\partial q_t, \partial/\partial q'_t$ | Split complex Cauchy–Riemann operator on the centre |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the original treatment of the biquaternion algebra and its centre.
- I. L. Kantor and A. S. Solodovnikov, *Hypercomplex Numbers: An Elementary Introduction to Algebras* (Springer, 1989), for the split complex numbers and the idempotent decomposition of algebras of split signature.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997), for the centre and the idempotent decomposition of the split biquaternion algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for fixed spaces of involutions in Clifford algebras of split signature.
