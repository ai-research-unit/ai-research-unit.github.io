
# __Split-Quaternion Norm and Invertibility__

## Introduction

This article studies the norm form of the split-quaternion algebra, its isotropy, and the invertibility theory it determines. It proves the criterion that an element is invertible exactly when its norm does not vanish, identifies the group of units with the general linear group $GL_2(\mathbb{R})$, classifies the elements, and describes how the invertible elements are distributed among the distinguished subspaces.

The split-quaternion algebra, its basis, its conjugation $\bar{\cdot}$, its norm form $N$, its matrix model $\Phi$, its idempotents $u_\pm$ and its subspaces $S$, $V$, $\mathbb{D}_2$, $\mathbb{D}_3$ are assumed from *Split-Quaternion Algebra* and are not redefined. The determinant and the invertibility criterion for matrices are assumed from *Matrix Algebras*. The zero divisor set is treated separately in *Split-Quaternion Zero Divisors*, and the roots of $-1$ in *Split-Quaternion Roots of Minus One*. Nothing physical is invoked.

## The Norm Form and the Determinant Form

### The Norm Form

**Definition.** The **norm form** of a split-quaternion $x = a + be_1 + ce_2 + de_3$ is

$$
N(x) = x\bar{x} = \bar{x}x = a^2 + b^2 - c^2 - d^2,
$$

where $\bar{x} = a - be_1 - ce_2 - de_3$ is the conjugation of (*Split-Quaternion Algebra*, §*The Conjugation*).

By (*Split-Quaternion Algebra*, §*The Norm Form*) the form $N$ is a quadratic form of signature $(2,2)$, it is multiplicative,

$$
N(xy) = N(x)N(y) \qquad (x, y \in \mathbb{H}_{\mathrm{s}}),
$$

and its polarisation is the bilinear form

$$
B(x, y) = \tfrac{1}{2}\big(N(x+y) - N(x) - N(y)\big) = aa' + bb' - cc' - dd'
$$

for $x = a + be_1 + ce_2 + de_3$ and $y = a' + b'e_1 + c'e_2 + d'e_3$. The matrix of $B$ in the basis $1, e_1, e_2, e_3$ is $\operatorname{diag}(+1, +1, -1, -1)$.

### The Determinant Form

The matrix model $\Phi : \mathbb{H}_{\mathrm{s}} \to M_2(\mathbb{R})$ carries a quadratic form of its own, the determinant. The two forms agree.

**Theorem (The Norm Form Is the Determinant Form).** For every $x \in \mathbb{H}_{\mathrm{s}}$,

$$
N(x) = \det \Phi(x),
$$

and $N$ is the restriction to $\Phi(\mathbb{H}_{\mathrm{s}}) = M_2(\mathbb{R})$ of the determinant form of $M_2(\mathbb{R})$, a quadratic form of signature $(2,2)$.

**Proof.** The computation of (*Split-Quaternion Algebra*, §*The Matrix Model*) gives

$$
\det \Phi(x) = (a-d)(a+d) - (c-b)(b+c) = a^2 - d^2 - (c^2 - b^2) = a^2 + b^2 - c^2 - d^2 = N(x).
$$

The determinant form on $M_2(\mathbb{R})$ has signature $(2,2)$, since the matrix

$$
\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}
$$

has square $0$ and the two diagonal unit matrices have squares $1$ and $-1$ under the polarised determinant; equivalently, the two real forms $\mathrm{Cl}_{1,1} \cong \mathrm{Cl}_{2,0} \cong M_2(\mathbb{R})$ of *The Number Systems as Clifford Algebras* correspond exactly to the two signatures of the same algebra. $\square$

The determinant is therefore not a second invariant: the norm form of the algebra and the determinant of the matrix model are one object in two notations. The trace gives the complementary invariant, $\operatorname{tr}\Phi(x) = 2\operatorname{Sc}(x)$.

### Multiplicativity and the Sign

The multiplicativity of $N$ has an immediate consequence for the sign.

**Proposition.** The set $\{N > 0\}$ and the set $\{N < 0\}$ are each closed under multiplication, and the product of an element of $\{N>0\}$ with an element of $\{N<0\}$ has $N < 0$. The scalar line and the $e_1$-direction have positive norm, while the $e_2$- and $e_3$-directions have negative norm.

**Proof.** If $N(x)$ and $N(y)$ are both positive, then $N(xy) = N(x)N(y) > 0$, and similarly in the other cases. The signs of the basis elements are $N(1) = N(e_1) = +1$ and $N(e_2) = N(e_3) = -1$. $\square$

## Isotropy

**Definition.** The form $N$ is **isotropic**: there exist nonzero $x$ with $N(x) = 0$. A nonzero element with $N(x) = 0$ is an **isotropic vector**, and a one-dimensional subspace $\mathbb{R}x$ spanned by an isotropic vector is an **isotropic line**.

**Theorem (The Isotropic Vectors).** The isotropic vectors of $\mathbb{H}_{\mathrm{s}}$ are the nonzero quadrivectors \((a, b, c, d)\) with

$$
a^2 + b^2 = c^2 + d^2 .
$$

Writing $z = a + ib$ and $w = c + id$ with $i^2 = -1$, the condition is $|z| = |w|$. The isotropic vectors are therefore parametrised by a pair $(z, w)$ of complex numbers of equal modulus.

**Proof.** The equation $N(x) = 0$ is $a^2 + b^2 = c^2 + d^2$, which in the notation of the statement is $|z|^2 = |w|^2$. $\square$

**Proposition (Explicit Isotropic Lines).** Write $x = a + be_1 + ce_2 + de_3$. If $x$ is isotropic then $(a,b) \neq (0,0)$ and $(c,d) \neq (0,0)$, and $x$ is a positive multiple of

$$
(\cos\alpha, \sin\alpha, \cos\beta, \sin\beta)
$$

for a unique pair of angles $\alpha, \beta$ modulo the simultaneous replacement $(\alpha,\beta) \mapsto (\alpha+\pi, \beta+\pi)$. The isotropic lines are therefore parametrised by $S^1 \times S^1$ modulo the identification $(\alpha,\beta)\sim(\alpha+\pi,\beta+\pi)$ of pairs of angles, and the isotropic lines lying in the vector subspace $V$ are exactly

$$
\mathbb{R}\big(e_1 + \cos\theta\, e_2 + \sin\theta\, e_3\big), \qquad \theta \in [0, 2\pi),
$$

a circle's worth of lines; in particular $\mathbb{R}(e_1 + e_2)$, $\mathbb{R}(e_1 - e_2)$, $\mathbb{R}(e_1 + e_3)$ and $\mathbb{R}(e_1 - e_3)$ are isotropic.

**Proof.** The equation $N(x) = 0$ is $a^2 + b^2 = c^2 + d^2$. If $(a,b) = (0,0)$ then $c = d = 0$ and $x = 0$, contrary to the definition of an isotropic vector; the same argument applies to $(c,d)$. Hence both pairs are nonzero, and there are $r > 0$ and angles $\alpha, \beta$ with $(a,b) = r(\cos\alpha, \sin\alpha)$ and $(c,d) = r(\cos\beta, \sin\beta)$; the common radius is forced by the equation. Multiplying $x$ by a positive scalar does not change either angle, and multiplying by $-1$ adds $\pi$ to both, so the line determines $(\alpha,\beta)$ modulo the simultaneous replacement. For the vector subspace, $a = 0$ and the equation is $b^2 = c^2 + d^2$ with $b \neq 0$; normalising $b = 1$ and writing $(c,d) = (\cos\theta,\sin\theta)$ gives the displayed family. $\square$

**Theorem (The Isotropic Lines Are Doubly Ruled).** The isotropic lines of $\mathbb{H}_{\mathrm{s}}$ are the images under $\Phi$ of the lines of rank-one matrices of $M_2(\mathbb{R})$. The set of isotropic lines carries two families of lines of the projective null quadric; the two families are defined and computed in *Split-Quaternion Zero Divisors*, §*The Two Families*, where they are identified with the sets

$$
\{ \mathbb{R}x : \operatorname{im} \Phi(x) \subseteq \ell \}, \qquad
\{ \mathbb{R}x : \ker \Phi(x) \supseteq \ell \},
$$

indexed by the lines $\ell \subset \mathbb{R}^2$.

**Proof.** An element $x \neq 0$ is isotropic exactly when $\det \Phi(x) = N(x) = 0$, i.e. when $\Phi(x)$ is a nonzero singular matrix, i.e. a rank-one matrix, since the matrices are $2 \times 2$. The ruling is proved in *Split-Quaternion Zero Divisors*, §*The Two Families*. $\square$

The isotropic lines are also visible in the vector subspace: the isotropic lines lying in $V$ are the lines of the three-dimensional light cone $b^2 = c^2 + d^2$. Isotropic lines not lying in $V$ have a nonzero scalar part; an example is $\mathbb{R}(1 + e_2)$, since $N(1+e_2) = 1 - 1 = 0$, and another is $\mathbb{R}(1 + e_3)$.

## The Invertibility Criterion

**Theorem (The Invertibility Criterion).** Let $x \in \mathbb{H}_{\mathrm{s}}$ be nonzero. The following are equivalent.

1. $x$ is **invertible**: there exists $y$ with $xy = yx = 1$.
2. $N(x) \neq 0$.
3. $\det \Phi(x) \neq 0$.

When these hold, the inverse is

$$
x^{-1} = \frac{\bar{x}}{N(x)} .
$$

**Proof.** Suppose first that $N(x) \neq 0$. Then $\bar{x}/N(x)$ is a real multiple of $\bar{x}$, and

$$
x \cdot \frac{\bar{x}}{N(x)} = \frac{x\bar{x}}{N(x)} = \frac{N(x)}{N(x)} = 1, \qquad
\frac{\bar{x}}{N(x)} \cdot x = \frac{\bar{x}x}{N(x)} = 1,
$$

so $x$ is invertible with the displayed inverse. Conversely, suppose $x$ is invertible, say $xy = 1$. Applying $N$ and using multiplicativity, $N(x)N(y) = N(1) = 1$, so $N(x) \neq 0$. This proves the equivalence of (1) and (2); the equivalence of (2) and (3) is the theorem that $N(x) = \det \Phi(x)$. $\square$

**Corollary (Zero Divisors).** A nonzero element is a zero divisor if and only if $N(x) = 0$. Indeed, $\Phi(x)$ is then a singular nonzero matrix, which has a nonzero kernel and a nonzero cokernel, so there exist nonzero $y$ and nonzero $z$ with $\Phi(x)\Phi(y) = 0$ and $\Phi(z)\Phi(x) = 0$; pulling back through $\Phi$ gives $xy = 0$ and $zx = 0$.

The criterion has the form the menu names: **invertibility is $N \neq 0$**, and the boundary is the null cone of the determinant form. Since the determinant is the norm, the multiplicative structure of the algebra and the invertibility theory are governed by one quadratic form.

## The Group of Units

**Definition.** The **group of units** of the split-quaternion algebra is

$$
\mathbb{H}_{\mathrm{s}}^{\times} = \{x \in \mathbb{H}_{\mathrm{s}} : N(x) \neq 0\},
$$

with multiplication inherited from the algebra.

**Theorem.** The map $\Phi$ restricts to a group isomorphism

$$
\Phi : \mathbb{H}_{\mathrm{s}}^{\times} \longrightarrow GL_2(\mathbb{R}),
$$

and the norm form is a surjective group homomorphism

$$
N : \mathbb{H}_{\mathrm{s}}^{\times} \longrightarrow \mathbb{R}^{\times}.
$$

**Proof.** The model $\Phi$ is an algebra isomorphism, so it restricts to an isomorphism from the set of invertible elements of $\mathbb{H}_{\mathrm{s}}$ to the set of invertible elements of $M_2(\mathbb{R})$, which is $GL_2(\mathbb{R})$. Multiplicativity of $N$ makes it a group homomorphism, and it is surjective because $N(\lambda) = \lambda^2$ for real $\lambda \neq 0$. $\square$

**Corollary (The Norm-One Groups).** The kernel of $N$ is the group of **unit split-quaternions**

$$
U = \{x \in \mathbb{H}_{\mathrm{s}} : N(x) = 1\} \cong \mathrm{SL}_2(\mathbb{R}),
$$

and the union of the two norm levels $\pm 1$ is

$$
\{x : N(x) = \pm 1\} = \mathrm{SL}_2^{\pm}(\mathbb{R}) = \{M \in M_2(\mathbb{R}) : \det M = \pm 1\},
$$

which has two connected components, namely $\mathrm{SL}_2(\mathbb{R})$ and the determinant $-1$ component. The group of units has two connected components as well, the sets $\{N > 0\} = GL_2^{+}(\mathbb{R})$ and $\{N < 0\} = GL_2^{-}(\mathbb{R})$; the norm-one subgroup $U$ is connected.

**Proof.** The kernel of $N$ is $\{N = 1\}$, which maps to $\{M : \det M = 1\} = \mathrm{SL}_2(\mathbb{R})$. The determinant is negative exactly on the second component of $GL_2(\mathbb{R})$, and $\mathrm{SL}_2(\mathbb{R})$ is connected, as recalled in *Matrix Groups and Classical Groups*. $\square$

This is the exact point at which the indefinite norm changes the group theory. The quaternion unit sphere is the compact group $Sp(1) \cong SU(2)$, the kernel of a positive-definite norm on a division algebra. The split-quaternion norm-one set is the non-compact $\mathrm{SL}_2(\mathbb{R})$, and the passage from $Sp(1)$ to $\mathrm{SL}_2(\mathbb{R})$ is the passage from the double cover of the rotation group of three-space to the double cover of the Lorentz group of signature $(2,1)$. The rotations themselves are treated in *Split-Quaternion Rotations and the Lorentz Group*.

## The Three-Way Classification

The menu's three-way classification of the elements is the following.

**Theorem (Classification).** Every element of $\mathbb{H}_{\mathrm{s}}$ falls into exactly one of the three classes:

| Class | Criterion | Size |
|---|---|---|
| the zero element | $x = 0$ | one element |
| the invertible elements | $x \neq 0$ and $N(x) \neq 0$ | the complement of the null cone |
| the zero divisors | $x \neq 0$ and $N(x) = 0$ | the null cone minus the origin |

There is no fourth class, and in particular the third class is **not** empty: the isotropic vectors of *Isotropy* are zero divisors by the corollary of *The Invertibility Criterion*. The two classes partition $\mathbb{H}_{\mathrm{s}} \setminus \{0\}$; the invertible class is open, and the zero divisor class is closed there.

**Proof.** Let $x$ be nonzero. The real number $N(x)$ is either zero or a unit of $\mathbb{R}$; there is no third possibility, because $\mathbb{R}$ is a field. If $N(x) = 0$ then $x$ is a zero divisor by the corollary of the criterion; if $N(x) \neq 0$ then $x$ is invertible. The two cases are exclusive and exhaust the nonzero elements. $\square$

**Remark.** In the split-biquaternion case the corresponding classification genuinely has three nonzero classes, because there the norm takes values in a ring with zero divisors rather than in a field, so that $N(x)$ can be a nonzero non-unit. The three-way classification of the present article is therefore a **dichotomy plus the zero element**, and its third row is the single element $0$. The contrast is developed in *Comparison with the Quaternion and Split-Biquaternion Cases*.

**Corollary (The Refinement by Sign).** The invertible class splits into the two open sets

$$
P = \{x : N(x) > 0\}, \qquad Q = \{x : N(x) < 0\},
$$

each of which is closed under multiplication, while $P \cdot Q \subseteq Q$ and $Q \cdot Q \subseteq P$. The identity lies in $P$, and $P$ is the component $GL_2^{+}(\mathbb{R})$ of the group of units.

## Distribution of the Invertible Elements

The invertible elements are distributed over the distinguished subspaces as follows. The subspaces are those of (*Split-Quaternion Algebra*, §*Conjugations and Fixed-Point Subspaces* and §*The Idempotents and the Split-Complex Subspaces*).

### The Scalar Subspace

On $S = \mathbb{R} \cdot 1$, an element is $x = a$ with $N(x) = a^2$. Every nonzero scalar is a unit, and every such unit lies in $P$. The only non-unit of $S$ is $0$.

### The Vector Subspace

On $V$, an element is $u = be_1 + ce_2 + de_3$ with

$$
N(u) = b^2 - c^2 - d^2 .
$$

The invertible elements of $V$ are the vectors with $b^2 \neq c^2 + d^2$: the **spacelike** vectors with $b^2 < c^2 + d^2$, on which $N < 0$, and the **timelike** vectors with $b^2 > c^2 + d^2$, on which $N > 0$. The non-invertible nonzero elements of $V$ are the **lightlike** vectors, the cone $b^2 = c^2 + d^2$. This is the trichotomy of the Lorentzian geometry of the vector subspace, and it is the reason the geometry of the system is the hyperbolic plane; see *Split-Quaternion Rotations and the Lorentz Group*.

### The Split-Complex Subspaces

On $\mathbb{D}_2 = \operatorname{span}\{1, e_2\}$, an element is $x = a + ce_2$ with

$$
N(x) = a^2 - c^2 .
$$

The invertible elements are those with $a^2 \neq c^2$; the non-invertible nonzero elements are the real multiples of $1 + e_2$ and of $1 - e_2$, which are the zero divisors of the split-complex algebra $\mathbb{D}$ studied in *Split-Complex Algebra*. On $\mathbb{D}_3 = \operatorname{span}\{1, e_3\}$ the identical statement holds with $e_3$ in place of $e_2$.

### The Minimal Left and Right Ideals

On the two minimal left ideals $\mathbb{H}_{\mathrm{s}} u_\pm$, every element is a zero divisor or zero.

**Proposition.** For every $x \in \mathbb{H}_{\mathrm{s}}$, $N(xu_\pm) = N(x)N(u_\pm) = 0$. Hence $\mathbb{H}_{\mathrm{s}} u_+$ and $\mathbb{H}_{\mathrm{s}} u_-$ are **totally isotropic**: they contain no invertible element other than the origin. The same statement holds for the two minimal right ideals $u_+ \mathbb{H}_{\mathrm{s}}$ and $u_- \mathbb{H}_{\mathrm{s}}$.

**Proof.** $N(u_\pm) = \tfrac14 N(1 \pm e_2) = \tfrac14(1 - 1) = 0$, and multiplicativity gives $N(xu_\pm) = N(x) \cdot 0 = 0$. $\square$

So each of the four two-dimensional subspaces $\mathbb{H}_{\mathrm{s}} u_\pm$, $u_\pm \mathbb{H}_{\mathrm{s}}$ consists entirely of zero divisors together with the origin.

### Summary of the Distribution

| Subspace | Dimension | Norm | Zero divisors |
|---|---|---|---|
| $S = \mathbb{R}\cdot 1$ | $1$ | $a^2 \geq 0$ | none except $0$ |
| $V$ | $3$ | $b^2 - c^2 - d^2$, signature $(2,1)$ | the light cone $b^2 = c^2 + d^2$ |
| $\mathbb{D}_2$ | $2$ | $a^2 - c^2$, signature $(1,1)$ | $\mathbb{R}(1 \pm e_2) \setminus \{0\}$ |
| $\mathbb{D}_3$ | $2$ | $a^2 - d^2$, signature $(1,1)$ | $\mathbb{R}(1 \pm e_3) \setminus \{0\}$ |
| $\mathbb{H}_{\mathrm{s}} u_\pm$, $u_\pm \mathbb{H}_{\mathrm{s}}$ | $2$ | identically $0$ | the whole subspace minus the origin |

The invertible elements are the complement of the null cone $\{N = 0\}$, an open dense set of full measure. They form two connected components, $\{N > 0\}$ and $\{N < 0\}$.

## Comparison with the Quaternion and Split-Biquaternion Cases

### The Quaternion Case

For $\mathbb{H}$ the norm form is $N(q) = q_0^2 + q_1^2 + q_2^2 + q_3^2$, positive definite by (*Quaternion Algebra*, §*The Norm Form*). It vanishes only at the origin, so every nonzero quaternion is invertible, the algebra is a division algebra, the invertible class is the whole of $\mathbb{H} \setminus \{0\}$, and the classification has the single nonzero class. The norm-one group is the compact $Sp(1) \cong SU(2)$, and the group of units is $\mathbb{R}_{>0} \times Sp(1)$, which is connected. The change from $\mathbb{H}$ to $\mathbb{H}_{\mathrm{s}}$ is the change of the norm from signature $(4,0)$ to signature $(2,2)$; it empties no class away, but it inserts the null cone and the two-component structure.

### The Split-Biquaternion Case

The eight-dimensional algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ of the notation table is a real algebra of dimension eight, and it is treated later in Part V, under Split-Biquaternions; nothing of it is used here. The structural difference that decides the comparison is visible from the conventions alone: its coefficients lie in the split-complex ring $\mathbb{D}$, so its norm form takes values in $\mathbb{D}$, and $\mathbb{D}$ has zero divisors of its own. An invertibility criterion in that system is a criterion in a ring with zero divisors, and its classification therefore has a third nonzero class — the elements whose norm is a nonzero zero divisor — which does not exist in the present article. The present classification, by contrast, is the dichotomy of *The Three-Way Classification*, and the reason is exactly that the coefficient field here is $\mathbb{R}$.

## Summary

The norm form of the split-quaternion algebra is $N(x) = a^2 + b^2 - c^2 - d^2$, of signature $(2,2)$, multiplicative, and equal under the matrix model to the determinant: $N(x) = \det \Phi(x)$. The form is isotropic; its isotropic vectors satisfy $a^2 + b^2 = c^2 + d^2$, its isotropic lines are the lines of rank-one matrices, and on the vector subspace the isotropic lines are the lines of the light cone $b^2 = c^2 + d^2$.

A nonzero element is invertible exactly when $N(x) \neq 0$, and then $x^{-1} = \bar{x}/N(x)$; it is a zero divisor exactly when $N(x) = 0$. The group of units is $\{N \neq 0\} \cong GL_2(\mathbb{R})$, the norm-one subgroup is $U = \{N = 1\} \cong \mathrm{SL}_2(\mathbb{R})$, and $\{N = \pm 1\} = \mathrm{SL}_2^{\pm}(\mathbb{R})$ has two components. The units form the two connected components $\{N > 0\}$ and $\{N < 0\}$.

The classification of the elements is a dichotomy plus the zero element: invertible, or zero divisor, or zero; there is no further class, because the norm takes values in the field $\mathbb{R}$. The invertible elements are distributed as follows: all nonzero scalars are units; in $V$ the units are the spacelike and timelike vectors and the zero divisors are the light cone; in each split-complex subalgebra the units avoid the two isotropic lines; and the four minimal ideals $\mathbb{H}_{\mathrm{s}} u_\pm$, $u_\pm \mathbb{H}_{\mathrm{s}}$ are totally isotropic. In the eight-dimensional $\mathbb{H}_{\mathbb{D}}$ the norm takes values in a ring with zero divisors, and the corresponding classification has a genuinely third nonzero class; that system is treated later under Split-Biquaternions.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $N(x) = x\bar{x}$ | the norm form, signature $(2,2)$ | this article |
| $B(x,y)$ | the polarised bilinear form | this article |
| $\det \Phi(x) = N(x)$ | the determinant form of the matrix model | this article |
| isotropic vector, isotropic line | nonzero $x$ with $N(x)=0$, and its span | this article |
| $\mathbb{H}_{\mathrm{s}}^{\times}$ | the group of units $\{N \neq 0\}$ | this article |
| $U = \{N = 1\}$ | the unit split-quaternions, $\cong \mathrm{SL}_2(\mathbb{R})$ | this article |
| $\mathrm{SL}_2^{\pm}(\mathbb{R})$ | $\{M : \det M = \pm 1\} = \{N = \pm 1\}$ | this article |
| $P = \{N > 0\}$, $Q = \{N < 0\}$ | the two components of the units | this article |
| $S$, $V$, $\mathbb{D}_2$, $\mathbb{D}_3$ | the scalar, vector and split-complex subspaces | *Split-Quaternion Algebra* |
| $u_\pm = \tfrac12(1 \pm e_2)$ | the non-central idempotents | *Split-Quaternion Algebra* |
| spacelike, timelike, lightlike | the sign of $N$ on $V$ | this article |
| $\mathbb{H}$ | the real quaternions | *Quaternion Algebra* |
| $\mathbb{H}_{\mathbb{D}}$ | the split-biquaternions, a later Part V system | *The Number Systems as Clifford Algebras* |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the norm and determinant forms of the low-dimensional Clifford algebras.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for $SL_2(\mathbb{R})$ and the indefinite orthogonal groups in their matrix models.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for isotropic forms, their null cones and their maximal totally isotropic subspaces.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the split forms and the comparison with the division algebra case.
