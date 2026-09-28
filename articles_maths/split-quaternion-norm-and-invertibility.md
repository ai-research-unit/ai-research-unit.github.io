
# __Split-Quaternion Norm and Invertibility__

## Introduction

This article studies the split-quaternion norm, its isotropy, and the invertibility theory it determines. It proves the criterion that an element is invertible exactly when its split-quaternion norm does not vanish, describes the group of units, classifies the elements, and describes how the invertible elements are distributed among the distinguished subspaces.

The split-quaternion algebra, its basis, its conjugation $\bar{\cdot}$, its split-quaternion norm $N$, its idempotents $\tilde\pi_\pm$ and its subspaces $S$, $V$, $\mathbb{D}_2$, $\mathbb{D}_3$ are assumed from *Split-Quaternion Algebra* and are not redefined. The zero divisor set is treated separately in *Split-Quaternion Zero Divisors*, and the roots of $-1$ in *Split-Quaternion Roots of Minus One*. Nothing physical is invoked.

## The Split-Quaternion Norm

### The Split-Quaternion Norm

**Definition.** The **split-quaternion norm** of $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ is

$$
N(\tilde q) = \tilde q\bar{\tilde q} = \bar{\tilde q}\tilde q = q_0^2 + q_1^2 - q_2^2 - q_3^2,
$$

where $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ is the conjugation of (*Split-Quaternion Algebra*, §*The Conjugation*).

The form is a real quadratic form of **signature $(2,2)$**, read directly from the diagonal expression as two positive and two negative squares. It is **multiplicative**:

$$
N(\tilde q y) = N(\tilde q)N(y) \qquad (\tilde q, y \in \mathbb{H}_{\mathrm{s}}).
$$

**Proof.** The product $\tilde q\bar{\tilde q}$ is fixed by the conjugation, hence central; therefore, for all $\tilde q, y$,

$$
N(\tilde q y) = (\tilde q y)\overline{(\tilde q y)} = \tilde q\, y\bar y\, \bar{\tilde q} = \tilde q \bar{\tilde q}\, y\bar y = N(\tilde q)N(y),
$$

using $\overline{\tilde q y} = \bar y \bar{\tilde q}$ and the centrality of $y\bar y$.

Its polarisation is the bilinear form

$$
B(\tilde q, y) = \tfrac{1}{2}\big(N(\tilde q+y) - N(\tilde q) - N(y)\big) = q_0 q_0' + q_1 q_1' - q_2 q_2' - q_3 q_3'
$$

for $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ and $y = q_0' e_0 + q_1' e_1 + q_2' e_2 + q_3' e_3$. The matrix of $B$ in the basis $1, e_1, e_2, e_3$ is $\operatorname{diag}(+1, +1, -1, -1)$.

### Multiplicativity and the Sign

The multiplicativity of $N$ has an immediate consequence for the sign.

**Proposition.** The set $\{N > 0\}$ and the set $\{N < 0\}$ are each closed under multiplication, and the product of an element of $\{N>0\}$ with an element of $\{N<0\}$ has $N < 0$. The scalar line and the $e_1$-direction have positive norm, while the $e_2$- and $e_3$-directions have negative norm.

**Proof.** If $N(\tilde q)$ and $N(y)$ are both positive, then $N(\tilde q y) = N(\tilde q)N(y) > 0$, and similarly in the other cases. The signs of the basis elements are $N(1) = N(e_1) = +1$ and $N(e_2) = N(e_3) = -1$.

## Isotropy

**Definition.** The form $N$ is **isotropic**: there exist nonzero $\tilde q$ with $N(\tilde q) = 0$. A nonzero element with $N(\tilde q) = 0$ is an **isotropic vector**, and a one-dimensional subspace $\mathbb{R}\tilde q$ spanned by an isotropic vector is an **isotropic line**.

**Theorem (The Isotropic Vectors).** The isotropic vectors of $\mathbb{H}_{\mathrm{s}}$ are the nonzero quadrivectors \((q_0, q_1, q_2, q_3)\) with

$$
q_0^2 + q_1^2 = q_2^2 + q_3^2 .
$$

Writing $z = q_0 + ib$ and $w = q_2 + id$ with $i^2 = -1$, the condition is $|z| = |w|$. The isotropic vectors are therefore parametrised by a pair $(z, w)$ of complex numbers of equal modulus.

**Proof.** The equation $N(\tilde q) = 0$ is $q_0^2 + q_1^2 = q_2^2 + q_3^2$, which in the notation of the statement is $|z|^2 = |w|^2$.

**Proposition (Explicit Isotropic Lines).** Write $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$. If $\tilde q$ is isotropic then $(q_0,q_1) \neq (0,0)$ and $(q_2,q_3) \neq (0,0)$, and $\tilde q$ is a positive multiple of

$$
(\cos\alpha, \sin\alpha, \cos\beta, \sin\beta)
$$

for a unique pair of angles $\alpha, \beta$ modulo the simultaneous replacement $(\alpha,\beta) \mapsto (\alpha+\pi, \beta+\pi)$. The isotropic lines are therefore parametrised by $S^1 \times S^1$ modulo the identification $(\alpha,\beta)\sim(\alpha+\pi,\beta+\pi)$ of pairs of angles, and the isotropic lines lying in the vector subspace $V$ are exactly

$$
\mathbb{R}\big(e_1 + \cos\theta\, e_2 + \sin\theta\, e_3\big), \qquad \theta \in [0, 2\pi),
$$

a circle's worth of lines; in particular $\mathbb{R}(e_1 + e_2)$, $\mathbb{R}(e_1 - e_2)$, $\mathbb{R}(e_1 + e_3)$ and $\mathbb{R}(e_1 - e_3)$ are isotropic.

**Proof.** The equation $N(\tilde q) = 0$ is $q_0^2 + q_1^2 = q_2^2 + q_3^2$. If $(q_0,q_1) = (0,0)$ then $q_2 = q_3 = 0$ and $\tilde q = 0$, contrary to the definition of an isotropic vector; the same argument applies to $(q_2,q_3)$. Hence both pairs are nonzero, and there are $r > 0$ and angles $\alpha, \beta$ with $(q_0,q_1) = r(\cos\alpha, \sin\alpha)$ and $(q_2,q_3) = r(\cos\beta, \sin\beta)$; the common radius is forced by the equation. Multiplying $\tilde q$ by a positive scalar does not change either angle, and multiplying by $-1$ adds $\pi$ to both, so the line determines $(\alpha,\beta)$ modulo the simultaneous replacement. For the vector subspace, $q_0 = 0$ and the equation is $q_1^2 = q_2^2 + q_3^2$ with $q_1 \neq 0$; normalising $q_1 = 1$ and writing $(q_2,q_3) = (\cos\theta,\sin\theta)$ gives the displayed family.

**Theorem (The Isotropic Lines Are Doubly Ruled).** The isotropic lines of $\mathbb{H}_{\mathrm{s}}$ are the points of the projective null quadric $\{N = 0\} \subset \mathbb{P}(\mathbb{H}_{\mathrm{s}})$, and that quadric is doubly ruled: its lines fall into two families, such that two lines of one family are skew while a line of one family meets a line of the other in exactly one point unless the two are parallel. The two families are defined and computed in *Split-Quaternion Zero Divisors*, §*The Two Families*.

**Proof.** A nonzero element $\tilde q$ is isotropic exactly when $N(\tilde q) = 0$, so the isotropic lines are the points of the projective null quadric of the non-degenerate form $N$ of signature $(2,2)$. A non-degenerate quadric of signature $(2,2)$ in $\mathbb{P}^3$ is doubly ruled. The explicit ruling is proved in *Split-Quaternion Zero Divisors*, §*The Two Families*.

The isotropic lines are also visible in the vector subspace: the isotropic lines lying in $V$ are the lines of the three-dimensional light cone $q_1^2 = q_2^2 + q_3^2$. Isotropic lines not lying in $V$ have a nonzero scalar part; an example is $\mathbb{R}(1 + e_2)$, since $N(1+e_2) = 1 - 1 = 0$, and another is $\mathbb{R}(1 + e_3)$.

## The Invertibility Criterion

**Theorem (The Invertibility Criterion).** Let $\tilde q \in \mathbb{H}_{\mathrm{s}}$ be nonzero. The following are equivalent.

1. $\tilde q$ is **invertible**: there exists $y$ with $\tilde q y = y\tilde q = 1$.
2. $N(\tilde q) \neq 0$.

When these hold, the inverse is

$$
\tilde q^{-1} = \frac{\bar{\tilde q}}{N(\tilde q)} .
$$

**Proof.** Suppose first that $N(\tilde q) \neq 0$. Then $\bar{\tilde q}/N(\tilde q)$ is a real multiple of $\bar{\tilde q}$, and

$$
\tilde q \cdot \frac{\bar{\tilde q}}{N(\tilde q)} = \frac{\tilde q\bar{\tilde q}}{N(\tilde q)} = \frac{N(\tilde q)}{N(\tilde q)} = 1, \qquad
\frac{\bar{\tilde q}}{N(\tilde q)} \cdot \tilde q = \frac{\bar{\tilde q}\tilde q}{N(\tilde q)} = 1,
$$

so $\tilde q$ is invertible with the displayed inverse. Conversely, suppose $\tilde q$ is invertible, say $\tilde q y = 1$. Applying $N$ and using multiplicativity, $N(\tilde q)N(y) = N(1) = 1$, so $N(\tilde q) \neq 0$. This proves the equivalence of (1) and (2).

**Corollary (Zero Divisors).** A nonzero element is a zero divisor if and only if $N(\tilde q) = 0$. If $N(\tilde q) = 0$ and $\tilde q \neq 0$, then $\tilde q\bar{\tilde q} = 0$ with $\bar{\tilde q} \neq 0$, so $\tilde q$ is a zero divisor; conversely a zero divisor is not a unit, so $N(\tilde q) = 0$ by the criterion.

The criterion has the form the menu names: **invertibility is $N \neq 0$**, and the boundary is the null cone of the split-quaternion norm. Since the split-quaternion norm is multiplicative, the multiplicative structure of the algebra and the invertibility theory are governed by one quadratic form.

## The Group of Units

**Definition.** The **group of units** of the split-quaternion algebra is

$$
\mathbb{H}_{\mathrm{s}}^{\times} = \{\tilde q \in \mathbb{H}_{\mathrm{s}} : N(\tilde q) \neq 0\},
$$

with multiplication inherited from the algebra.

**Theorem.** The split-quaternion norm restricts to a surjective group homomorphism

$$
N : \mathbb{H}_{\mathrm{s}}^{\times} \longrightarrow \mathbb{R}^{\times}.
$$

**Proof.** Multiplicativity of $N$ makes it a group homomorphism from the units to $\mathbb{R}^{\times}$, and it is surjective because $N(\lambda) = \lambda^2$ and $N(\lambda e_2) = -\lambda^2$ for real $\lambda \neq 0$.

**Corollary (The Norm-One Groups).** The kernel of $N$ is the group of **unit split-quaternions**

$$
U = \{\tilde q \in \mathbb{H}_{\mathrm{s}} : N(\tilde q) = 1\} \cong \mathrm{SL}_2(\mathbb{R}),
$$

and the union of the two split-quaternion norm levels $\pm 1$ is the disjoint union $\{\tilde q : N(\tilde q) = \pm 1\} = U \sqcup (-U)$ of two connected components, namely $U$ and its negative. The group of units has two connected components as well, the open sets $\{N > 0\}$ and $\{N < 0\}$; the norm-one subgroup $U$ is connected.

**Proof.** The kernel of $N$ is $\{N = 1\}$, which is the group of unit split-quaternions and is connected, as recalled in *Matrix Groups and Classical Groups*; the second norm level is its negative coset $-U$. The group of units is the disjoint union of the two open sign sets $\{N > 0\}$ and $\{N < 0\}$.

This is the exact point at which the indefinite norm changes the group theory. The quaternion unit sphere is the compact group $Sp(1) \cong SU(2)$, the kernel of a positive-definite norm on a division algebra. The split-quaternion norm-one set is the non-compact $\mathrm{SL}_2(\mathbb{R})$, and the passage from $Sp(1)$ to $\mathrm{SL}_2(\mathbb{R})$ is the passage from the double cover of the rotation group of three-space to the double cover of the Lorentz group of signature $(2,1)$. The rotations themselves are treated in *Split-Quaternion Rotations and the Lorentz Group*.

## The Three-Way Classification

The menu's three-way classification of the elements is the following.

**Theorem (Classification).** Every element of $\mathbb{H}_{\mathrm{s}}$ falls into exactly one of the three classes:

| Class | Criterion | Size |
|---|---|---|
| the zero element | $\tilde q = 0$ | one element |
| the invertible elements | $\tilde q \neq 0$ and $N(\tilde q) \neq 0$ | the complement of the null cone |
| the zero divisors | $\tilde q \neq 0$ and $N(\tilde q) = 0$ | the null cone minus the origin |

There is no fourth class, and in particular the third class is **not** empty: the isotropic vectors of *Isotropy* are zero divisors by the corollary of *The Invertibility Criterion*. The two classes partition $\mathbb{H}_{\mathrm{s}} \setminus \{0\}$; the invertible class is open, and the zero divisor class is closed there.

**Proof.** Let $\tilde q$ be nonzero. The real number $N(\tilde q)$ is either zero or a unit of $\mathbb{R}$; there is no third possibility, because $\mathbb{R}$ is a field. If $N(\tilde q) = 0$ then $\tilde q$ is a zero divisor by the corollary of the criterion; if $N(\tilde q) \neq 0$ then $\tilde q$ is invertible. The two cases are exclusive and exhaust the nonzero elements.

**Remark.** In the split-biquaternion case the corresponding classification genuinely has three nonzero classes, because there the norm takes values in a ring with zero divisors rather than in a field, so that $N(\tilde q)$ can be a nonzero non-unit. The three-way classification of the present article is therefore a **dichotomy plus the zero element**, and its third row is the single element $0$. The contrast is developed in *Comparison with the Quaternion and Split-Biquaternion Cases*.

**Corollary (The Refinement by Sign).** The invertible class splits into the two open sets

$$
P = \{\tilde q : N(\tilde q) > 0\}, \qquad Q = \{\tilde q : N(\tilde q) < 0\},
$$

each of which is closed under multiplication, while $P \cdot Q \subseteq Q$ and $Q \cdot Q \subseteq P$. The identity lies in $P$, and $P$ is the identity component of the group of units.

## Distribution of the Invertible Elements

The invertible elements are distributed over the distinguished subspaces as follows. The subspaces are those of (*Split-Quaternion Algebra*, §*Conjugations and Fixed-Point Subspaces* and §*The Idempotents and the Split-Complex Subspaces*).

### The Scalar Subspace

On $S = \mathbb{R} \cdot 1$, an element is $\tilde q = q_0$ with $N(\tilde q) = q_0^2$. Every nonzero scalar is a unit, and every such unit lies in $P$. The only non-unit of $S$ is $0$.

### The Vector Subspace

On $V$, an element is $u = q_1 e_1 + q_2 e_2 + q_3 e_3$ with

$$
N(u) = q_1^2 - q_2^2 - q_3^2 .
$$

The invertible elements of $V$ are the vectors with $q_1^2 \neq q_2^2 + q_3^2$: the **spacelike** vectors with $q_1^2 < q_2^2 + q_3^2$, on which $N < 0$, and the **timelike** vectors with $q_1^2 > q_2^2 + q_3^2$, on which $N > 0$. The non-invertible nonzero elements of $V$ are the **lightlike** vectors, the cone $q_1^2 = q_2^2 + q_3^2$. This is the trichotomy of the Lorentzian geometry of the vector subspace, and it is the reason the geometry of the system is the hyperbolic plane; see *Split-Quaternion Rotations and the Lorentz Group*.

### The Split-Complex Subspaces

On $\mathbb{D}_2 = \operatorname{span}\{1, e_2\}$, an element is $\tilde q = q_0 + q_2 e_2$ with

$$
N(\tilde q) = q_0^2 - q_2^2 .
$$

The invertible elements are those with $q_0^2 \neq q_2^2$; the non-invertible nonzero elements are the real multiples of $1 + e_2$ and of $1 - e_2$, which are the zero divisors of the split-complex algebra $\mathbb{D}$ studied in *Split-Complex Algebra*. On $\mathbb{D}_3 = \operatorname{span}\{1, e_3\}$ the identical statement holds with $e_3$ in place of $e_2$.

### The Minimal Left and Right Ideals

On the two minimal left ideals $\mathbb{H}_{\mathrm{s}} \tilde\pi_\pm$, every element is a zero divisor or zero.

**Proposition.** For every $\tilde q \in \mathbb{H}_{\mathrm{s}}$, $N(\tilde q\tilde\pi_\pm) = N(\tilde q)N(\tilde\pi_\pm) = 0$. Hence $\mathbb{H}_{\mathrm{s}} \tilde\pi_+$ and $\mathbb{H}_{\mathrm{s}} \tilde\pi_-$ are **totally isotropic**: they contain no invertible element other than the origin. The same statement holds for the two minimal right ideals $\tilde\pi_+ \mathbb{H}_{\mathrm{s}}$ and $\tilde\pi_- \mathbb{H}_{\mathrm{s}}$.

**Proof.** $N(\tilde\pi_\pm) = \tfrac14 N(1 \pm e_2) = \tfrac14(1 - 1) = 0$, and multiplicativity gives $N(\tilde q\tilde\pi_\pm) = N(\tilde q) \cdot 0 = 0$.

So each of the four two-dimensional subspaces $\mathbb{H}_{\mathrm{s}} \tilde\pi_\pm$, $\tilde\pi_\pm \mathbb{H}_{\mathrm{s}}$ consists entirely of zero divisors together with the origin.

### Summary of the Distribution

| Subspace | Dimension | Split-Quaternion norm | Zero divisors |
|---|---|---|---|
| $S = \mathbb{R}\cdot 1$ | $1$ | $q_0^2 \geq 0$ | none except $0$ |
| $V$ | $3$ | $q_1^2 - q_2^2 - q_3^2$, signature $(2,1)$ | the light cone $q_1^2 = q_2^2 + q_3^2$ |
| $\mathbb{D}_2$ | $2$ | $q_0^2 - q_2^2$, signature $(1,1)$ | $\mathbb{R}(1 \pm e_2) \setminus \{0\}$ |
| $\mathbb{D}_3$ | $2$ | $q_0^2 - q_3^2$, signature $(1,1)$ | $\mathbb{R}(1 \pm e_3) \setminus \{0\}$ |
| $\mathbb{H}_{\mathrm{s}} \tilde\pi_\pm$, $\tilde\pi_\pm \mathbb{H}_{\mathrm{s}}$ | $2$ | identically $0$ | the whole subspace minus the origin |

The invertible elements are the complement of the null cone $\{N = 0\}$, an open dense set of full measure. They form two connected components, $\{N > 0\}$ and $\{N < 0\}$.

## Comparison with the Quaternion and Split-Biquaternion Cases

### The Quaternion Case

For $\mathbb{H}$ the quaternion norm is $N(q) = q_0^2 + q_1^2 + q_2^2 + q_3^2$, positive definite by (*Quaternion Algebra*, §*Basic Properties*). It vanishes only at the origin, so every nonzero quaternion is invertible, the algebra is a division algebra, the invertible class is the whole of $\mathbb{H} \setminus \{0\}$, and the classification has the single nonzero class. The norm-one group is the compact $Sp(1) \cong SU(2)$, and the group of units is $\mathbb{R}_{>0} \times Sp(1)$, which is connected. The change from $\mathbb{H}$ to $\mathbb{H}_{\mathrm{s}}$ is the change of the norm from signature $(4,0)$ to signature $(2,2)$; it empties no class away, but it inserts the null cone and the two-component structure.

### The Split-Biquaternion Case

The eight-dimensional algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ of the notation table is a real algebra of dimension eight, and it is treated later in Part V, under Split-Biquaternions; nothing of it is used here. The structural difference that decides the comparison is visible from the conventions alone: its coefficients lie in the split-complex ring $\mathbb{D}$, so its norm takes values in $\mathbb{D}$, and $\mathbb{D}$ has zero divisors of its own. An invertibility criterion in that system is a criterion in a ring with zero divisors, and its classification therefore has a third nonzero class — the elements whose norm is a nonzero zero divisor — which does not exist in the present article. The present classification, by contrast, is the dichotomy of *The Three-Way Classification*, and the reason is exactly that the coefficient field here is $\mathbb{R}$.

## Summary

The split-quaternion norm is $N(\tilde q) = q_0^2 + q_1^2 - q_2^2 - q_3^2$, of signature $(2,2)$ and multiplicative. The form is isotropic; its isotropic vectors satisfy $q_0^2 + q_1^2 = q_2^2 + q_3^2$, its isotropic lines are the points of a doubly ruled projective null quadric, and on the vector subspace the isotropic lines are the lines of the light cone $q_1^2 = q_2^2 + q_3^2$.

A nonzero element is invertible exactly when $N(\tilde q) \neq 0$, and then $\tilde q^{-1} = \bar{\tilde q}/N(\tilde q)$; it is a zero divisor exactly when $N(\tilde q) = 0$. The group of units is $\{N \neq 0\}$, the norm-one subgroup is $U = \{N = 1\} \cong \mathrm{SL}_2(\mathbb{R})$, and $\{N = \pm 1\} = U \sqcup (-U)$ has two components. The units form the two connected components $\{N > 0\}$ and $\{N < 0\}$.

The classification of the elements is a dichotomy plus the zero element: invertible, or zero divisor, or zero; there is no further class, because the split-quaternion norm takes values in the field $\mathbb{R}$. The invertible elements are distributed as follows: all nonzero scalars are units; in $V$ the units are the spacelike and timelike vectors and the zero divisors are the light cone; in each split-complex subalgebra the units avoid the two isotropic lines; and the four minimal ideals $\mathbb{H}_{\mathrm{s}} \tilde\pi_\pm$, $\tilde\pi_\pm \mathbb{H}_{\mathrm{s}}$ are totally isotropic. In the eight-dimensional $\mathbb{H}_{\mathbb{D}}$ the norm takes values in a ring with zero divisors, and the corresponding classification has a genuinely third nonzero class; that system is treated later under Split-Biquaternions.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $N(\tilde q) = \tilde q\bar{\tilde q}$ | the split-quaternion norm, signature $(2,2)$ | this article |
| $B(\tilde q,y)$ | the polarised bilinear form | this article |
| isotropic vector, isotropic line | nonzero $\tilde q$ with $N(\tilde q)=0$, and its span | this article |
| $\mathbb{H}_{\mathrm{s}}^{\times}$ | the group of units $\{N \neq 0\}$ | this article |
| $U = \{N = 1\}$ | the unit split-quaternions, $\cong \mathrm{SL}_2(\mathbb{R})$ | this article |
| $\{N = \pm 1\}$ | the two split-quaternion norm levels, $U$ and $-U$ | this article |
| $P = \{N > 0\}$, $Q = \{N < 0\}$ | the two components of the units | this article |
| $S$, $V$, $\mathbb{D}_2$, $\mathbb{D}_3$ | the scalar, vector and split-complex subspaces | *Split-Quaternion Algebra* |
| $\tilde\pi_\pm = \tfrac12(1 \pm e_2)$ | the non-central idempotents | *Split-Quaternion Algebra* |
| spacelike, timelike, lightlike | the sign of $N$ on $V$ | this article |
| $\mathbb{H}$ | the real quaternions | *Quaternion Algebra* |
| $\mathbb{H}_{\mathbb{D}}$ | the split-biquaternions, a later Part V system | *The Number Systems as Clifford Algebras* |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the split-quaternion norm and determinant forms of the low-dimensional Clifford algebras.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for $SL_2(\mathbb{R})$ and the indefinite orthogonal groups in their matrix models.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for isotropic forms, their null cones and their maximal totally isotropic subspaces.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the split forms and the comparison with the division algebra case.
