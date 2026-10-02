
# __Split-Biquaternion Anti-Hermitian Subspace__

## Introduction

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ carries four linear involutions, and four of the resulting fixed spaces are its distinguished real subspaces. This article treats the **anti-Hermitian subspace** $\mathbb{M}_-$, the fixed space of anti-Hermitian conjugation: its definition, its basis, the failure of closure under multiplication, the symmetrized product that carries it into $\mathbb{M}_+$, the Lie structure it acquires under the commutator, the forms on it, its roots of $-1$, the action of the four involutions and its intersections with the other subspaces. Its complementary partner $\mathbb{M}_+$ is treated in *Split-Biquaternion Hermitian Subspace*; the comparative tables are in *Split-Biquaternion Relations Between Subspaces* and *Split-Biquaternion Involution Lattice*.

The treatment is purely mathematical. No physics is invoked. The split biquaternion algebra is assumed from the basic algebra article and the quaternion algebra $\mathbb{H}$ from the article on quaternion algebra. Throughout, elements are written $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ with $Q_\mu = q_\mu + j q'_\mu \in \mathbb{D}$, and the conjugations are ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (split complex), ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ (Hermitian) and ${}^{\flat} = -{}^{*}$ (anti-Hermitian). The split-biquaternion norm is $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$, and the Hermitian form has scalar part $\sum_\mu (q_\mu^2 - q'^2_\mu)$.

## Definition and Basis

**Definition.** The **anti-Hermitian subspace** is the fixed space of anti-Hermitian conjugation,

$$
\mathbb{M}_- = \left\{ \tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \tilde{Q}^{\flat} = \tilde{Q} \right\}, \qquad \tilde{Q}^\flat = -\tilde{Q}^{*} = -\overline{\tilde{Q}^{\natural}}.
$$

### The Condition in Coordinates

Comparing $-\overline{\tilde{Q}^{\natural}} = \tilde{Q}$ coefficient by coefficient:

- the coefficient of $e_0$ gives $-\bar{Q_0} = Q_0$, that is $\bar{Q_0} = -Q_0$, so $Q_0 = j r_0$ is **purely split-imaginary**;
- the coefficient of $e_k$ gives $\bar{Q_k} = Q_k$, so $Q_k = q_k$ is **real**.

The subspace is therefore the set of elements with purely split-imaginary scalar part and real vector part,

$$
\tilde{Q} = j r_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad r_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

### Basis and Dimension

**Proposition.** The anti-Hermitian subspace is a real vector space of dimension $4$, with basis $je_0, e_1, e_2, e_3$.

**Proof.** The condition removes the four real scalar parameters and the four split-imaginary vector parameters, leaving the four real parameters $r_0, q_1, q_2, q_3$; the four basis elements are linearly independent and span the set.

## Algebra Structure

### It Is Not a Subalgebra

**Proposition.** $\mathbb{M}_-$ is **not** closed under multiplication, and is therefore not a subalgebra of $\mathbb{H}_{\mathbb{D}}$.

**Proof.** The element $je_0$ lies in the subspace, but its square is

$$
(je_0)^2 = j^2 = e_0,
$$

which has real scalar part $1$ and so is not in $\mathbb{M}_-$.

The obstruction is that a product of two anti-Hermitian elements has a real scalar part, which belongs to $\mathbb{M}_+$; the product leaves $\mathbb{M}_-$ in the Hermitian direction.

### The Symmetrized Product Lands in the Hermitian Subspace

**Proposition.** For $\tilde{Q} = j r_0 e_0 + \mathbf{u}$ and $\tilde{R} = j s_0 e_0 + \mathbf{v}$ in $\mathbb{M}_-$, with $\mathbf{u}, \mathbf{v}$ real pure quaternions,

$$
\tilde{Q} \circ \tilde{R} = \tfrac{1}{2}(\tilde{Q}\tilde{R} + \tilde{R}\tilde{Q}) = \left(r_0 s_0 - \mathbf{u}\cdot\mathbf{v}\right) e_0 + j\left(r_0 \mathbf{v} + s_0 \mathbf{u}\right) \in \mathbb{M}_+.
$$

**Proof.** Expanding and using $\mathbf{u}\mathbf{v} = -\mathbf{u}\cdot\mathbf{v} + \mathbf{u}\times\mathbf{v}$, the products $\tilde{Q}\tilde{R}$ and $\tilde{R}\tilde{Q}$ differ only in the sign of the cross term $\mathbf{u}\times\mathbf{v}$, which therefore cancels under symmetrization; the remaining scalar part is real and the remaining vector part is purely split-imaginary.

So the symmetrized product of two anti-Hermitian elements is Hermitian, the mirror image of the fact that the commutator of two Hermitian elements is anti-Hermitian.

### It Is a Lie Subalgebra

**Proposition.** Under the commutator, $\mathbb{M}_-$ is a **Lie subalgebra** of $\mathbb{H}_{\mathbb{D}}$:

$$
[\tilde{Q}, \tilde{R}] = \tilde{Q}\tilde{R} - \tilde{R}\tilde{Q} = 2\,\mathbf{u} \times \mathbf{v} \in \mathbb{M}_-.
$$

**Proof.** With the same expansion, the commutator retains only the cross term $2\mathbf{u}\times\mathbf{v}$, which is a pure real quaternion; this lies in $\mathbb{M}_-$ because its scalar part is $0$ and its vector part is real. The Jacobi identity is inherited from the associativity of the product.

The bracket image $[\mathbb{M}_-, \mathbb{M}_-]$ is the three-dimensional space of pure real quaternions, the same three-dimensional Lie algebra $\mathrm{SO}(3)$ that is the commutator subalgebra of the quaternion subspace; the bracket of anti-Hermitian elements generates $\mathrm{SO}(3)$, developed in *Split-Biquaternion Exponential and Lie Group Structure*.

### The Correspondence with the Hermitian Subspace

**Proposition.** Multiplication by $j$ is a linear isomorphism $\mathbb{M}_- \to \mathbb{M}_+$ with inverse multiplication by $j$:

$$
j\left(j r_0 e_0 + \mathbf{u}\right) = r_0 e_0 + j \mathbf{u} \in \mathbb{M}_+, \qquad j\, \mathbb{M}_- = \mathbb{M}_+, \qquad j\, \mathbb{M}_+ = \mathbb{M}_-.
$$

**Proof.** Since $j$ is central with $j^2 = 1$, multiplying an element with purely split-imaginary scalar part and real vector part by $j$ exchanges the two parts, producing a real scalar part and a purely split-imaginary vector part, which is $\mathbb{M}_+$; applying $j$ twice is the identity.

The map swaps the roles of the forms: the split-biquaternion norm on $\mathbb{M}_-$ is the split-biquaternion norm on $\mathbb{M}_+$ pulled back, and the Hermitian form changes sign. In the biquaternion algebra the corresponding map is multiplication by the central unit $i$.

### The Square

For $\tilde{Q} = j r_0 e_0 + \mathbf{u}$ the square is

$$
\tilde{Q}^2 = \left(r_0^2 - (\mathbf{u}, \mathbf{u})\right) e_0 + 2 j r_0 \mathbf{u} \in \mathbb{M}_+,
$$

the square of an anti-Hermitian element being Hermitian. In particular, for a real vector $\mathbf{u}$,

$$
\mathbf{u}^2 = -(\mathbf{u},\mathbf{u})\, e_0,
$$

a negative real scalar. The square of $je_0$ is $e_0$, so $je_0$ itself is an involution of the algebra that is not the identity.

## The Split-Biquaternion Norm and the Hermitian Form

### The Split-Biquaternion Norm and Its Signature

**Theorem.** On the anti-Hermitian subspace the split-biquaternion norm is the **positive definite** real quadratic form

$$
N(\tilde{Q}) = r_0^2 + q_1^2 + q_2^2 + q_3^2, \qquad \tilde{Q} = j r_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3,
$$

of signature $(4,0)$.

**Proof.** Substituting $Q_0 = j r_0$ and $Q_k = q_k$ in $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ gives $r_0^2 + \sum_k q_k^2$, because $(j r_0)^2 = j^2 r_0^2 = +r_0^2$.

Here the split-biquaternion norm is definite exactly as on $\mathbb{M}_+$; the difference from the Hermitian subspace appears in the Hermitian form, not the split-biquaternion norm.

### The Hermitian Form and Its Isotropic Cone

The Hermitian form has scalar part $\sum_\mu (q_\mu^2 - q'^2_\mu)$, which on $\mathbb{M}_-$ is

$$
\sum_{\mu=0}^{3} (q_\mu^2 - q'^2_\mu) = -r_0^2 + q_1^2 + q_2^2 + q_3^2,
$$

of signature $(3,1)$. Its isotropic cone is the three-dimensional cone

$$
r_0^2 = q_1^2 + q_2^2 + q_3^2.
$$

The signatures of the Hermitian form on the two sectors are complementary, $(1,3)$ on $\mathbb{M}_+$ and $(3,1)$ on $\mathbb{M}_-$; the map $j$ of the correspondence above exchanges the two.

### Units, Zero Divisors and Nilpotents

**Theorem.** For $\tilde{Q} \in \mathbb{M}_-$ the following are equivalent: $\tilde{Q}$ is a unit; $N(\tilde{Q}) \neq 0$; $\tilde{Q} \neq 0$. Hence $\mathbb{M}_-$ contains no zero divisor and no nilpotent.

**Proof.** The split-biquaternion norm is positive definite, vanishing only at the origin, so every nonzero element is a unit, with inverse $\tilde{Q}^{-1} = \tilde{Q}^{\natural}/N(\tilde{Q})$. A nilpotent $\tilde{Q} \neq 0$ would require $\tilde{Q}^2 = 0$, that is $r_0^2 = |\mathbf{u}|^2$ and $r_0\mathbf{u} = 0$, forcing $\tilde{Q} = 0$.

As on $\mathbb{M}_+$, the isotropic cone of the Hermitian form consists of units, not zero divisors: the two sectors together contain no zero divisor at all, and the zero divisors of $\mathbb{H}_{\mathbb{D}}$ are confined to the two four-dimensional subspaces $Z_+$ and $Z_-$ of *Split-Biquaternion Zero Divisors*.

### The Roots of Minus One

**Theorem.** The roots of $-1$ in $\mathbb{M}_-$ are the unit pure real quaternions,

$$
\xi = q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_1^2 + q_2^2 + q_3^2 = 1,
$$

which form a two-sphere $S^2$.

**Proof.** For $\tilde{Q} = j r_0 e_0 + \mathbf{u}$ the equation $\tilde{Q}^2 = -1$ reads, by the square formula, $r_0^2 - |\mathbf{u}|^2 = -1$ and $2 r_0 \mathbf{u} = 0$. The second equation gives $r_0 = 0$ or $\mathbf{u} = 0$; $\mathbf{u} = 0$ would give $r_0^2 = -1$, impossible, so $r_0 = 0$ and $|\mathbf{u}|^2 = 1$.

The three imaginary units $e_1, e_2, e_3$ lie in $\mathbb{M}_-$, so the subspace contains the quaternion imaginary sphere; the roots of $-1$ in $\mathbb{M}_-$ are exactly the roots of $-1$ in the quaternion subspace. The roots of $-1$ in $\mathbb{M}_+$ are instead the elements $j\mathbf{u}$ with $\mathbf{u}$ a unit pure real quaternion, the sphere $jS^2$; the two spheres are exchanged by multiplication by $j$.

## The Image in the Two Halves

Under the idempotent-decomposition isomorphism $\varphi : \mathbb{H}_{\mathbb{D}} \to \mathbb{H} \oplus \mathbb{H}$, an anti-Hermitian element $\tilde{Q} = j r_0 e_0 + \mathbf{u}$ has components

$$
\tilde{Q}_+ = r_0 + \mathbf{u}, \qquad \tilde{Q}_- = -r_0 + \mathbf{u} = -(\tilde{Q}_+)^{\natural}.
$$

The image of $\mathbb{M}_-$ is therefore the set of **anti-conjugate pairs**

$$
\varphi(\mathbb{M}_-) = \left\{ (h, -h^{\natural}) : h \in \mathbb{H} \right\} \cong \mathbb{H},
$$

a real four-dimensional subspace of $\mathbb{H} \oplus \mathbb{H}$. Together with the image $(h, h^{\natural})$ of $\mathbb{M}_+$ it exhibits the Hermitian decomposition $\mathbb{H}_{\mathbb{D}} = \mathbb{M}_+ \oplus \mathbb{M}_-$ as the decomposition of a pair $(h_1, h_2)$ into its conjugate-symmetric and conjugate-antisymmetric parts.

## The Four Involutions on It

In the basis $je_0, e_1, e_2, e_3$ the four involutions act diagonally:

| involution | matrix | effect |
|---|---|---|
| ${}^{\natural}$ | $\operatorname{diag}(1, -1, -1, -1)$ | negates the vector part |
| $\bar{\cdot}$ | $\operatorname{diag}(-1, 1, 1, 1)$ | negates the scalar part |
| ${}^{*}$ | $-\mathrm{id}$ | minus the identity |
| ${}^{\flat}$ | $+\mathrm{id}$ | the identity, by definition |

The subspace is invariant under all four. Quaternion conjugation negates the vector part and fixes the split-imaginary scalar $je_0$; split complex conjugation does the opposite; their composite Hermitian conjugation negates the whole subspace. Inside $\mathbb{M}_-$ the fixed space of quaternion conjugation is the line $j\mathbb{R}$ of purely split-imaginary scalars, and the fixed space of split complex conjugation is the three-dimensional space $\mathrm{span}\{e_1,e_2,e_3\}$ of real vectors.

## Relations to the Other Subspaces

The intersections of $\mathbb{M}_-$ with the other distinguished subspaces are, with dimensions:

| pair | intersection | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{M}_- \cap \mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $j\mathbb{R}$ | $1$ |
| $\mathbb{M}_- \cap \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathrm{span}\{e_1, e_2, e_3\}$ | $3$ |
| $\mathbb{M}_- \cap \mathbb{M}_+$ | $\{0\}$ | $0$ |
| $\mathbb{M}_- \cap \mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ | $\mathrm{span}\{e_1, e_2, e_3\}$ | $3$ |

The subspace is complementary to $\mathbb{M}_+$, giving the Hermitian decomposition $\mathbb{H}_{\mathbb{D}} = \mathbb{M}_+ \oplus \mathbb{M}_-$. Its coordinate-block decomposition is $\mathbb{M}_- = j\mathbb{R} \oplus \mathrm{span}\{e_1, e_2, e_3\}$: the line $j\mathbb{R}$ is shared with the split complex subspace, and the real triple with the quaternion subspace and with the vector subspace. Its sums with the centre and with $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$-complements have dimension $5$; only the pair with $\mathbb{M}_+$ spans the algebra. The full tables are in *Split-Biquaternion Relations Between Subspaces*.

## The Analysis on the Anti-Hermitian Subspace

The anti-Hermitian subspace is not a subalgebra, so, like the Hermitian subspace, it carries no intrinsic multiplicative function theory; the analysis on it is the restriction of the ambient analysis of *Split-Biquaternion Analysis* to a four-dimensional subspace. The symmetrized product of two elements of $\mathbb{M}_-$ lies in $\mathbb{M}_+$, so the functions on $\mathbb{M}_-$ acquire a bracket, the commutator, rather than a pointwise product, and the intrinsic differential structure is the Lie-theoretic one of *Split-Biquaternion Anti-Hermitian Subspace*. The second-order operator obtained from the restriction of the ambient operators is the wave operator of the restricted Lorentzian form $-q'^2_0 + \sum_k q_k^2$ of signature $(3,1)$.

## The Geometry of the Anti-Hermitian Subspace

The anti-Hermitian subspace is the negative eigenspace of the involution ${}^{*}$ of the algebra, and geometrically the invariant four-plane of the corresponding linear involution of $\mathbb{R}^8$. It is a Lorentzian subspace of the Hermitian scalar form: $g$ restricts to $-q'^2_0 + \sum_k q_k^2$ of signature $(3,1)$, while the split-biquaternion norm restricts to the positive definite form $q'^2_0 + \sum_k q_k^2$ of signature $(4,0)$ recorded in the notation table above. The null cone of $g$ is again cut out by $q'^2_0 = \sum_k q_k^2$; the restricted form being indefinite of signature $(3,1)$, it has isotropic lines, and their projectivisation in $\mathbb{P}(\mathbb{M}_-)$ is a two-sphere. The motions it carries are the same Lorentz group $SO(1,3)$, realised on $\mathbb{M}_-$ rather than on $\mathbb{M}_+$; the two subspaces are interchanged by multiplication by $j$, since $(j\tilde Q)^{\dagger} = -j\tilde{Q}^{*}$.

## Summary

The anti-Hermitian subspace $\mathbb{M}_-$ is the fixed space of anti-Hermitian conjugation, the set of elements $\tilde{Q} = j r_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with purely split-imaginary scalar part and real vector part; it is a real vector space of dimension $4$ with basis $je_0, e_1, e_2, e_3$. It is **not** a subalgebra — $(je_0)^2 = e_0$ leaves it — but the symmetrized product of two of its elements is Hermitian, the commutator is $2\,\mathbf{u}\times\mathbf{v}$, a pure real quaternion, and under that bracket $\mathbb{M}_-$ is a **Lie subalgebra** with bracket image the three-dimensional $\mathrm{SO}(3)$. Multiplication by $j$ is a linear isomorphism $\mathbb{M}_- \to \mathbb{M}_+$, and the square of an anti-Hermitian element is Hermitian. The split-biquaternion norm restricts to the positive definite form $N = r_0^2 + q_1^2 + q_2^2 + q_3^2$ of signature $(4,0)$, so $\mathbb{M}_-$ contains no zero divisor and no nilpotent; the indefinite form is the Hermitian form, of signature $(3,1)$ and isotropic cone $r_0^2 = q_1^2 + q_2^2 + q_3^2$, whose nonzero points are all units. The roots of $-1$ in the subspace are the unit pure real quaternions, a two-sphere $S^2$, the same roots as in the quaternion subspace. The image under $\varphi$ is the set of anti-conjugate pairs $(h, -h^{\natural})$ in $\mathbb{H} \oplus \mathbb{H}$. Of the four involutions, anti-Hermitian conjugation fixes the subspace pointwise, quaternion and split complex conjugations negate the vector and scalar parts respectively, and Hermitian conjugation is minus the identity; the subspace is complementary to $\mathbb{M}_+$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ | Split biquaternion algebra, real dimension $8$ |
| $\tilde{Q} = j r_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | Element of the anti-Hermitian subspace, coefficients real |
| $\mathbb{M}_-$ | Anti-Hermitian subspace, fixed space of ${}^{\flat}$ |
| $\mathbb{M}_+$ | Hermitian subspace, fixed space of ${}^{*}$ |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ | The four conjugations |
| $N(\tilde{Q}) = r_0^2 + |\mathbf{u}|^2$ | Norm on $\mathbb{M}_-$, signature $(4,0)$ |
| $\sum_\mu (q_\mu^2 - q'^2_\mu)$ | Scalar part of the Hermitian form, signature $(3,1)$ on $\mathbb{M}_-$ |
| $\tilde{Q} \circ \tilde{R} = \tfrac{1}{2}(\tilde{Q}\tilde{R} + \tilde{R}\tilde{Q})$ | Symmetrized product, landing in $\mathbb{M}_+$ |
| $[\tilde{Q}, \tilde{R}] = 2\,\mathbf{u} \times \mathbf{v}$ | Commutator, a pure real quaternion |
| $j : \mathbb{M}_- \to \mathbb{M}_+$ | Isomorphism by multiplication by $j$ |
| $S^2$ | The roots of $-1$ in $\mathbb{M}_-$, unit pure real quaternions |
| $r_0^2 = q_1^2 + q_2^2 + q_3^2$ | Isotropic cone of the Hermitian form |
| $SO(1,3)$ | Lorentz group acting on the anti-Hermitian subspace |
| $(j\tilde{Q})^{\dagger} = -j\tilde{Q}^{*}$ | Multiplication by $j$ swaps $\mathbb{M}_\pm$ |

## Further Reading

- I. L. Kantor and A. S. Solodovnikov, *Hypercomplex Numbers: An Elementary Introduction to Algebras* (Springer, 1989), for anti-Hermitian elements and the Lie structure of algebras with a conjugation.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997), for the Hermitian and anti-Hermitian sectors of the split biquaternion algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Lie algebra $\mathrm{SO}(3)$ generated by the pure imaginary units and the roots of $-1$.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the general theory of Lie subalgebras and the bracket relations of the classical algebras.
