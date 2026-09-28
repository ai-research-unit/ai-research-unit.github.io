
# __Split-Biquaternion Split-Complex Subspace__

## Introduction

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ carries four linear involutions, and each of them splits $\mathbb{H}_{\mathbb{D}}$ into a fixed space and an anti-fixed space. Four of the resulting spaces — the split complex subspace, the quaternion subspace, the Hermitian subspace and the anti-Hermitian subspace — are the distinguished real subspaces of the algebra and are the subject of the four single-subspace articles. This article treats the smallest of them, the **split complex subspace** $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, on its own: its definition, its basis, its algebra structure, the restriction of the split-biquaternion norm to it, its idempotents and zero divisors, the action of the four involutions upon it, and its intersections with the other subspaces. The companions are *Split-Biquaternion Quaternion Subspace*, *Split-Biquaternion Hermitian Subspace* and *Split-Biquaternion Anti-Hermitian Subspace*; their relations with one another are collected in *Split-Biquaternion Relations Between Subspaces*, and the involutions themselves in *Split-Biquaternion Involution Lattice*.

The treatment is purely mathematical. No physics is invoked. The split biquaternion algebra is assumed from the basic algebra article, the split complex algebra $\mathbb{D}$ from the article on split complex algebra, and the quaternion algebra $\mathbb{H}$ from the article on quaternion algebra. The two idempotents $\tilde\Pi_+ = \tfrac{1}{2}(1 + j)$ and $\tilde\Pi_- = \tfrac{1}{2}(1 - j)$ and the isomorphism $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$ are assumed known.

Throughout, elements are written $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ with $Q_\mu = q_\mu + j q'_\mu \in \mathbb{D}$, and the conjugations are $\bar{\cdot}$ (quaternion), ${}^{*}$ (split complex), ${}^{\dagger} = {}^{*}\circ\bar{\cdot}$ (Hermitian) and ${}^{\flat} = -{}^{\dagger}$ (anti-Hermitian). The split-biquaternion norm is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$.

## Definition and Basis

**Definition.** The **split complex subspace** is the fixed space of quaternion conjugation,

$$
\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} = \left\{ \tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \bar{\tilde{Q}} = \tilde{Q} \right\},
$$

where quaternion conjugation is $\bar{\tilde{Q}} = Q_0 e_0 - Q_1 e_1 - Q_2 e_2 - Q_3 e_3$.

Since $\bar{\cdot}$ is an involution, it has eigenvalues $\pm 1$ and $\mathbb{H}_{\mathbb{D}}$ is the direct sum of its fixed space and its anti-fixed space. The anti-fixed space is the **vector subspace** $\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$, the set of elements with vanishing split scalar part, of real dimension $6$; it has no dedicated article in this series, and is mentioned only where a relation requires it.

### The Condition in Coordinates

Comparing the two sides of $\bar{\tilde{Q}} = \tilde{Q}$ coefficient by coefficient: the coefficient of $e_0$ gives $Q_0 = Q_0$, no condition; the coefficient of $e_k$ gives $-Q_k = Q_k$, that is $Q_k = 0$, for $k = 1, 2, 3$. The subspace is therefore the set of elements with **vanishing vector part**,

$$
\tilde{Q} = Q_0 e_0, \qquad Q_0 \in \mathbb{D}.
$$

### Basis and Dimension

**Proposition.** The split complex subspace is a real vector space of dimension $2$, with basis $e_0, j$. In real coordinates it is the coordinate plane $q_1 = q_2 = q_3 = q'_1 = q'_2 = q'_3 = 0$, with the two free parameters $q_0$ and $q'_0$.

**Proof.** The four split complex coefficients reduce to $Q_0$ alone, and a split complex number is a real pair $Q_0 = q_0 + j q'_0$; the elements $e_0$ and $j$ are linearly independent over $\mathbb{R}$ and span the set.

Of the four distinguished subspaces, $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is the only one of dimension $2$; the other three have dimension $4$.

## Algebra Structure

### It Is the Centre of the Algebra

**Theorem.** $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is the centre of $\mathbb{H}_{\mathbb{D}}$,

$$
\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} = \left\{ \tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \tilde{Q}\tilde{R} = \tilde{R}\tilde{Q} \ \text{for every} \ \tilde{R} \in \mathbb{H}_{\mathbb{D}} \right\}.
$$

**Proof.** An element commutes with every other element if and only if it commutes with the basis elements $e_1, e_2, e_3$, and $Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ commutes with all three precisely when $Q_1 = Q_2 = Q_3 = 0$, because $Q_k e_k$ anticommutes with the other quaternion units. The central elements are then the $\mathbb{D}$-multiples of $e_0$, which is the fixed space of $\bar{\cdot}$.

The subspace therefore has two descriptions: it is the fixed space of quaternion conjugation, and it is the centre of the algebra. Its elements are the **central elements**, written $z e_0$ with $z \in \mathbb{D}$.

### Subalgebra, Commutativity, and the Absence of a Field Structure

**Proposition.** $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is a subalgebra of $\mathbb{H}_{\mathbb{D}}$, it is commutative, and as a real algebra it is isomorphic to $\mathbb{D}$ via $Q_0 e_0 \mapsto Q_0$.

**Proof.** For two central elements, $(Q_0 e_0)(R_0 e_0) = (Q_0 R_0) e_0$, which lies in the subspace; commutativity is the commutativity of $\mathbb{D}$; and the displayed map is a bijective ring homomorphism because $e_0$ is the unit.

The subspace is a **subalgebra**, and it is one of the two subalgebras among the four distinguished subspaces, the other being the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$. It is the only **commutative** one. Unlike the biquaternion centre, however, it is **not a field**: the split complex algebra is not a division algebra, having the zero divisors $\tilde\Pi_+$ and $\tilde\Pi_-$. As a real algebra it is $\mathbb{R} \oplus \mathbb{R}$ through the idempotent basis, and its group of units is the four open quadrants of the plane, not the punctured plane.

### Ideals

Being the centre, $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ acts on $\mathbb{H}_{\mathbb{D}}$ by scalar extension: $\mathbb{H}_{\mathbb{D}}$ has $\mathbb{D}$-basis $e_0, e_1, e_2, e_3$. The subspace is not a proper two-sided ideal of $\mathbb{H}_{\mathbb{D}}$; the two coordinate lines $\mathbb{R} \tilde\Pi_+$ and $\mathbb{R} \tilde\Pi_-$ inside it are two-sided ideals of the subalgebra $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, and they are the intersections with the centre of the minimal ideals $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$ of the algebra. The ideal theory of the algebra is developed in *Split-Biquaternion Ideals and Peirce Decomposition*, and that of the centre is the ideal theory of $\mathbb{R} \oplus \mathbb{R}$.

### Multiplication Tables

The products within the subspace and with the vector units are

| product | value | product | value |
|---|---|---|---|
| $e_0 \cdot e_0$ | $e_0$ | $e_0 \cdot e_k$ | $e_k$ |
| $j \cdot e_0$ | $j$ | $j \cdot e_k$ | $j e_k$ |
| $e_0 \cdot j$ | $j$ | $e_k \cdot e_0$ | $e_k$ |

for $k = 1, 2, 3$. The table states that $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ multiplies into every subspace and is multiplied into by every subspace with no sign change: multiplication by a central element is a scalar extension, and the vector subspace is closed under multiplication by $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ in the same way.

## The Split-Biquaternion Norm

**Proposition.** On the split complex subspace the split-biquaternion norm is the square of the coefficient,

$$
N(\tilde{Q}) = Q_0^2, \qquad \tilde{Q} = Q_0 e_0.
$$

**Proof.** $\bar{\tilde{Q}} = \tilde{Q}$ on the subspace, so $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \tilde{Q}^2 = Q_0^2 e_0$, read as the split complex scalar $Q_0^2$.

Two features are worth isolating. First, $N$ takes **split complex** values on the subspace: writing $Q_0 = q_0 + j q'_0$, one has $Q_0^2 = (q_0^2 + q'^2_0) + 2 j q_0 q'_0$, real on the lines $q'_0 = 0$ and $q_0 = 0$ separately but not in general. Second, the real restriction in the basis $e_0, j$ has the matrix $\operatorname{diag}(1, 1)$ on the real part and $2 q_0 q'_0$ on the split-imaginary part, so the associated quadratic form is **not** definite: this is the form $N$ restricted to the two-dimensional centre, and its isotropic lines are the light lines $Q_0 = a \tilde\Pi_\pm$.

### Units and Zero Divisors

**Theorem.** For $\tilde{Q} = Q_0 e_0$, the following are equivalent:

1. $\tilde{Q}$ is a unit of $\mathbb{H}_{\mathbb{D}}$;
2. $N(\tilde{Q}) = Q_0^2$ is a unit of $\mathbb{D}$;
3. $Q_0$ is a unit of $\mathbb{D}$, that is $Q_0 = q_0 + j q'_0$ with $q_0^2 \neq q'^2_0$.

The inverse is $\tilde{Q}^{-1} = Q_0^{-1} e_0 = \dfrac{Q_0^*}{Q_0 Q_0^*} e_0 = \dfrac{q_0 - j q'_0}{q_0^2 - q'^2_0} e_0$.

**Proof.** $N(Q_0 e_0) = Q_0^2$ is a unit of $\mathbb{D}$ exactly when $Q_0$ is, since $\mathbb{D}$ is commutative; a split complex number is a unit precisely when its real form norm $q_0^2 - q'^2_0$ is nonzero. The inverse formula is the standard inverse in $\mathbb{D}$.

**Corollary.** The zero divisors of the split complex subspace are exactly the nonzero elements of the two **light lines**

$$
\mathbb{R} \tilde\Pi_+ \cup \mathbb{R} \tilde\Pi_-, \qquad \tilde\Pi_+ = \tfrac{1}{2}(1 + j), \quad \tilde\Pi_- = \tfrac{1}{2}(1 - j),
$$

and the annihilator of each light line is the other.

**Proof.** A split complex number $Q_0 = q_0 + j q'_0$ is a zero divisor exactly when $q_0^2 = q'^2_0$, that is $q_0 = \pm q'_0$, which is the union of the lines $\mathbb{R}(1 + j) = \mathbb{R} \tilde\Pi_+$ and $\mathbb{R}(1 - j) = \mathbb{R} \tilde\Pi_-$. Since $\tilde\Pi_+ \tilde\Pi_- = 0$, each line annihilates the other.

This is the first sharp difference from the biquaternion centre: there the split-biquaternion norm vanished only at the origin and the subspace was a field, whereas here the split-biquaternion norm degenerates on two lines and the subspace is only a product of fields.

## The Idempotents of the Centre

**Proposition.** The idempotents of $\mathbb{H}_{\mathbb{D}}$ all lie in the split complex subspace, and they are exactly

$$
0, \qquad \tilde\Pi_+, \qquad \tilde\Pi_-, \qquad 1.
$$

**Proof.** Solve $Q_0^2 = Q_0$ in $\mathbb{D}$. In the idempotent basis $Q_0 = \lambda_+ \tilde\Pi_+ + \lambda_- \tilde\Pi_-$, so $Q_0^2 = \lambda_+^2 \tilde\Pi_+ + \lambda_-^2 \tilde\Pi_-$; the equation holds exactly when $\lambda_+, \lambda_- \in \{0, 1\}$. The four combinations are $0, \tilde\Pi_+, \tilde\Pi_-, 1$. Every idempotent of $\mathbb{H}_{\mathbb{D}}$ is one of these, as proved in *Split-Biquaternion Idempotents and Projections*.

The idempotents $\tilde\Pi_+$ and $\tilde\Pi_-$ are the two nontrivial ones, they are orthogonal and primitive, and they lie in the centre — unlike the biquaternion case, where the nontrivial idempotents are noncentral and lie outside the centre. Since they are central, the decomposition $\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_+ \oplus \mathbb{H} \tilde\Pi_-$ generated by them is a decomposition into two-sided ideals. The idempotents are the only nonzero elements of the light lines that are idempotent; the remaining points of each light line are nilpotent-free zero divisors, and there are no nilpotents in the centre.

## The Four Involutions on It

Each of the four involutions preserves the condition $Q_1 = Q_2 = Q_3 = 0$, so the subspace is invariant under all four. Their action in the basis $e_0, j$ is diagonal:

| involution | $\tilde{Q} = Q_0 e_0$ | matrix on $e_0, j$ |
|---|---|---|
| $\bar{\cdot}$ | $Q_0 e_0$ | $\operatorname{diag}(1, 1)$ |
| ${}^{*}$ | $Q_0^{*} e_0$ | $\operatorname{diag}(1, -1)$ |
| ${}^{\dagger}$ | $Q_0^{*} e_0$ | $\operatorname{diag}(1, -1)$ |
| ${}^{\flat}$ | $-Q_0^{*} e_0$ | $\operatorname{diag}(-1, 1)$ |

Quaternion conjugation fixes the subspace pointwise — it is the defining involution — and Hermitian conjugation agrees with split complex conjugation there, because $\dagger = {}^{*}\circ\bar{\cdot}$ and $\bar{\cdot}$ acts as the identity. Split complex conjugation acts as the exchange $j \mapsto -j$, the non-trivial involution of $\mathbb{D}$, and anti-Hermitian conjugation is its negative. So of the four involutions only $\bar{\cdot}$ acts trivially on the centre, and ${}^{*}$ is the one that swaps the two light lines $\mathbb{R} \tilde\Pi_+$ and $\mathbb{R} \tilde\Pi_-$.

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
\varphi(Q_0 e_0) = (Q_0^+, Q_0^-), \qquad Q_0^\pm = q_0 \pm q'_0 \in \mathbb{R}.
$$

The image of $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is therefore the set $\mathbb{R} \oplus \mathbb{R}$ of pairs of real scalars, the centre of $\mathbb{H} \oplus \mathbb{H}$. The split-biquaternion norm has the matching description

$$
N(Q_0 e_0) = (Q_0^+)^2 \tilde\Pi_+ + (Q_0^-)^2 \tilde\Pi_-,
$$

the pair of squares of the two real scalars. The two light lines are the loci $Q_0^- = 0$ and $Q_0^+ = 0$, so the split-biquaternion norm degenerates on the coordinate axes of the pair, exactly as the two-dimensional split complex plane requires.

## The Analysis on the Split Complex Subspace

The centre is a copy of the split complex algebra $\mathbb{D}$, so the function theory it carries is the one-variable split complex analysis of *Split Complex Analysis*. A differentiable function of the centre variable $z = q_0 + jq'_0$, written $f = u + jv$, satisfies the Cauchy–Riemann pair

$$
\partial_{q_0}u = \partial_{q'_0}v, \qquad \partial_{q'_0}u = \partial_{q_0}v,
$$

and the twice differentiable functions that are harmonic in the split complex sense solve the wave equation $\partial_{q_0}^2 f - \partial_{q'_0}^2 f = 0$ rather than the Laplace equation. Embedded in $\mathbb{H}_{\mathbb{D}}$, the centre inherits the restriction of the ambient Cauchy–Riemann operator of *Split-Biquaternion Analysis*, and on the centre that operator is the split complex Cauchy–Riemann operator above. The absence of an elliptic harmonic theory on the centre is the analytic expression of the indefiniteness of its split-biquaternion norm: the restricted form is $q_0^2 - q'^2_0$, of signature $(1,1)$, and its isotropic directions are the two null lines of the zero divisors.

## The Geometry of the Split Complex Subspace

As the fixed space of quaternion conjugation, the centre is the axis of that involution of the algebra, and geometrically it is the invariant plane of the corresponding linear involution of $\mathbb{R}^8$. Its own geometry is that of the split complex plane: the two null lines $\mathbb{R}(1+j)$ and $\mathbb{R}(1-j)$ are the zero divisors, the level set of unit norm is the pair of hyperbolas $q_0^2 - q'^2_0 = 1$, and the motions it carries are the hyperbolic rotations $z\mapsto e^{\theta j}z$ of $\mathbb{D}$, the identity component of the group of units of $\mathbb{D}$ up to sign. The Euclidean form restricts to the ordinary Euclidean metric of the plane, while the Hermitian scalar form restricts to the positive definite form $q_0^2 + q'^2_0$ of signature $(2,0)$, so the centre is a definite slice of an indefinite ambient algebra.

## Summary

The split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is the fixed space of quaternion conjugation, the set of elements $\tilde{Q} = Q_0 e_0$ with vanishing vector part; it is a real vector space of dimension $2$ with basis $e_0, j$. It coincides with the centre of the algebra, is a commutative subalgebra isomorphic to the split complex algebra $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$, and is one of the two subalgebras among the four distinguished subspaces. It is **not** a field: the split-biquaternion norm restricts to $N = Q_0^2$, which is split-complex-valued and degenerates on the two light lines $\mathbb{R} \tilde\Pi_\pm$, and these are exactly the zero divisors of the subspace, each annihilating the other. The units are the elements with $Q_0$ a unit of $\mathbb{D}$, that is $Q_0 = q_0 + j q'_0$ with $q_0^2 \neq q'^2_0$, and the inverse is $Q_0^{-1} e_0 = (q_0 - j q'_0)/(q_0^2 - q'^2_0)\, e_0$. All four idempotents $0, \tilde\Pi_+, \tilde\Pi_-, 1$ of the algebra lie in the subspace, unlike the biquaternion case, where the nontrivial idempotents are noncentral. Of the four involutions, quaternion conjugation fixes the subspace pointwise, split complex and Hermitian conjugations act by $j \mapsto -j$ and swap the two light lines, and anti-Hermitian conjugation is the negative of that. The subspace meets the vector subspace only at the origin and meets both the quaternion and Hermitian subspaces in $\mathbb{R}$, the anti-Hermitian subspace in $j\mathbb{R}$, so it is the direct sum of the two coordinate blocks $\mathbb{R}$ and $j\mathbb{R}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ | Split biquaternion algebra, real dimension $8$ |
| $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ | General element, $Q_\mu \in \mathbb{D}$ |
| $Q_\mu = q_\mu + j q'_\mu$ | Real and split-imaginary parts of a coefficient |
| $j$ | Split complex unit, central, $j^2 = +1$ |
| $\tilde\Pi_\pm = \tfrac{1}{2}(1 \pm j)$ | Idempotents, giving the light lines $\mathbb{R} \tilde\Pi_\pm$ |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | Split complex subspace, the centre, fixed space of $\bar{\cdot}$ |
| $\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ | Vector subspace, the anti-fixed space of $\bar{\cdot}$, $\dim 6$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}, \mathbb{M}_+, \mathbb{M}_-$ | Quaternion, Hermitian, anti-Hermitian subspaces |
| $\bar{\cdot}, {}^{*}, {}^{\dagger}, {}^{\flat}$ | The four conjugations |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Split-Biquaternion norm, restricting to $Q_0^2$ |
| $\varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-)$ | Idempotent-decomposition isomorphism |
| $\mathbb{R}, j\mathbb{R}$ | The two coordinate blocks of the centre |
| $\partial_{q_0}, \partial_{q'_0}$ | Split complex Cauchy–Riemann operator on the centre |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the original treatment of the biquaternion algebra and its centre.
- I. L. Kantor and A. S. Solodovnikov, *Hypercomplex Numbers: An Elementary Introduction to Algebras* (Springer, 1989), for the split complex numbers and the idempotent decomposition of algebras of split signature.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997), for the centre and the idempotent decomposition of the split biquaternion algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for fixed spaces of involutions in Clifford algebras of split signature.
