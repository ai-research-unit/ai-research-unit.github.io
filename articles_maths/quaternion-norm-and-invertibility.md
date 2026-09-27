
# __Quaternion Norm and Invertibility__

## Introduction

The quaternion algebra $\mathbb{H}$ is the four-dimensional algebra with basis $e_0 = 1, e_1, e_2, e_3$ and the multiplication rules $e_1^2 = e_2^2 = e_3^2 = e_1e_2e_3 = -e_0$, so that $e_1e_2 = e_3$ and the basis elements anticommute in pairs. This article studies the multiplicative quadratic form that the algebra carries, the **norm form** $N(\tilde q) = \tilde q\bar{\tilde q}$, and the property that the form forces: every non-zero quaternion is invertible, so that $\mathbb{H}$ is a division algebra. It is the entry of the quaternion family that owns the norm form, its multiplicativity, the inverse formula and the group of units.

The companion article *Quaternion Algebra* fixes the basis, the conjugation, the multiplication table and the scalar–vector decomposition, and they are used here without restatement. The companion article *Quaternion Ideals and Simplicity* treats the absence of proper one- and two-sided ideals and the central-simplicity statement; this article owns the norm form, the multiplicativity, the invertibility criterion and the unit group, and it refers to that article for the ideal-theoretic consequences. A reader who wants the full structure of the algebra should read the three together: the algebra supplies the multiplication, this article supplies the norm and the division property, and the ideals article supplies the consequences of division for the ideal structure.

The corpus's default base is a commutative ring with identity, and the algebra $\mathbb{H}$ is defined over such a base by the same presentation. The results of this article that need more than that base are obtained over a field $F$ of characteristic not $2$; the positivity statements are obtained over $F = \mathbb{R}$, and they are flagged where they occur. In particular, the multiplicativity of the norm form, the inverse formula and the group-of-units statements hold over any field of characteristic not $2$, whereas the statement that the norm form is positive definite, the polar split of the unit group, and the topological description of the unit sphere are statements over $\mathbb{R}$.

Throughout, a quaternion is written

$$
\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3 = \sum_{\mu=0}^{3} q_\mu e_\mu, \qquad q_0, q_1, q_2, q_3 \in F,
$$

with **scalar part** $\operatorname{Sc}(\tilde q) = q_0$ and **vector part** $\mathbf{q} = q_1e_1 + q_2e_2 + q_3e_3$; the **conjugate** is $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$. The pure imaginary subspace is $\operatorname{Im}\mathbb{H} = \{\tilde q : \bar{\tilde q} = -\tilde q\}$.

## The Norm Form

### Definition

**Definition.** The **norm form** of a quaternion $\tilde q$ is

$$
N(\tilde q) = \tilde q\bar{\tilde q} = \bar{\tilde q} \tilde q = q_0^2 + q_1^2 + q_2^2 + q_3^2 .
$$

The equality of the two products is checked from the multiplication table: the vector part of $\tilde q\bar{\tilde q}$ is $q_0\mathbf{q} - \mathbf{q}q_0 + \mathbf{q}\times(-\mathbf{q}) = 0$, and the scalar calculation is the sum of squares.

**Proposition.** $N(\tilde q)$ is a central element of $\mathbb{H}$, it lies in the image of $F$, and the map $N : \mathbb{H}\to F$ is a quadratic form on the underlying vector space, with polar form $b(p,\tilde q) = \operatorname{Sc}(p\bar{\tilde q})$.

*Proof.* The scalar part of $\tilde q\bar{\tilde q}$ is $\sum_\mu q_\mu^2$, a scalar, and a scalar commutes with every quaternion; this is the centrality. The coordinate expression is homogeneous of degree two and its polarisation is $\operatorname{Sc}(p\bar{\tilde q})$, as the polar form of a sum of squares. $\square$

### Multiplicativity

**Theorem.** The norm form is multiplicative:

$$
N(pq) = N(p)\,N(\tilde q), \qquad p, \tilde q \in \mathbb{H}.
$$

*Proof.* Using $\overline{pq} = \bar{\tilde q}\bar p$ and the fact that $N(\tilde q) = \tilde q\bar{\tilde q}$ is central,

$$
N(pq) = (pq)\overline{(pq)} = pq\,\bar{\tilde q}\,\bar p = p\,N(\tilde q)\,\bar p = N(\tilde q)\,p\bar p = N(p)N(\tilde q) . \square
$$

Multiplicativity is the single feature that makes the norm form the algebraic centre of gravity of the subject. It holds over any commutative base in which the computation makes sense, and in particular over any field.

**Corollary.** If $N(p) = 0$ then $N(pq) = N(qp) = 0$ for every $\tilde q$, so a vanishing norm propagates and neither $p$ nor any multiple of it is a unit; over a field over which the norm form is anisotropic, that is $N(u) = 0$ only for $u = 0$, this middle case is empty and every non-zero element is a unit.

### Positive Definiteness and the Real Norm

**Theorem.** Over $F = \mathbb{R}$ the norm form is positive definite: $N(\tilde q) \geq 0$ for every $\tilde q$, and $N(\tilde q) = 0$ if and only if $\tilde q = 0$.

*Proof.* $N(\tilde q) = \sum_\mu q_\mu^2$ is a sum of squares of real numbers, hence non-negative, and it vanishes only when every $q_\mu$ vanishes. $\square$

**Definition.** Over $\mathbb{R}$ the **modulus** of $\tilde q$ is $|\tilde q| = \sqrt{N(\tilde q)}$.

**Theorem.** The modulus is a norm on the real vector space $\mathbb{H}\cong\mathbb{R}^4$: it is positive definite, absolutely homogeneous, and satisfies the triangle inequality. It is also multiplicative,

$$
|pq| = |p|\,|\tilde q|,
$$

and therefore submultiplicative as well.

*Proof.* Positive definiteness is the preceding theorem; homogeneity and the triangle inequality are those of the Euclidean norm on $\mathbb{R}^4$ under the identification $\tilde q\leftrightarrow(q_0,q_1,q_2,q_3)$. Multiplicativity is the square root of the multiplicativity of $N$, both factors being non-negative. $\square$

The modulus is the unique real norm on $\mathbb{H}$ compatible with the algebra in the sense of being multiplicative; this is the content of the next statement.

### The Norm Form and the Conjugate

**Proposition.** The norm form is invariant under conjugation, $N(\bar{\tilde q}) = N(\tilde q)$, and it is the **reduced norm** of $\mathbb{H}$ viewed as a central simple algebra of degree two over the base field.

*Proof.* $N(\bar{\tilde q}) = \bar{\tilde q} \tilde q = N(\tilde q)$. For a central simple algebra over a field the corresponding form is the reduced norm; for a quaternion algebra the reduced norm is the norm form above, and the identification is the classical one, quoted here as standard. $\square$

## The Inner Product

### Definition

**Definition.** The **inner product** of two quaternions is

$$
\langle p, \tilde q\rangle = \operatorname{Sc}(p\bar{\tilde q}) = \sum_{\mu=0}^{3} p_\mu q_\mu ,
$$

a symmetric bilinear form on the real vector space $\mathbb{H}$. The one-variable expression $\tilde q\bar{\tilde q}$ is the **Hermitian form**; in the quaternion case, the coefficients being real, it coincides with the norm form, as in *Quaternion Algebra*.

**Proposition.** The form $\langle\cdot,\cdot\rangle$ is bilinear, symmetric and positive definite over $\mathbb{R}$; it satisfies $\langle p, \tilde q\rangle = \operatorname{Sc}(\bar p \tilde q)$, and it is invariant under left and under right multiplication by a unit quaternion.

*Proof.* Bilinearity and symmetry are immediate from the coordinate expression. Positive definiteness is $\langle \tilde q,\tilde q\rangle = \sum_\mu q_\mu^2 = N(\tilde q)$. For a unit $u$, $\langle up, uq\rangle = \operatorname{Sc}(up\overline{uq}) = \operatorname{Sc}(u\,p\bar{\tilde q}\,\bar u) = \operatorname{Sc}(p\bar{\tilde q})$ because conjugation by a unit preserves the scalar part, as in *Quaternion Rotations and Reflections*; the right case is the same computation. $\square$

### The Euclidean Norm

The form $\langle\cdot,\cdot\rangle$ is the Euclidean inner product of $\mathbb{R}^4$ under the identification $\tilde q\leftrightarrow(q_0,q_1,q_2,q_3)$, and the modulus is its norm: $N(\tilde q) = \langle \tilde q, \tilde q\rangle$ and $|\tilde q| = \sqrt{\langle \tilde q,\tilde q\rangle}$. The orthogonal group of the form is $O(4)$, and the isometries of $\mathbb{H}$ that are also algebra automorphisms are the inner automorphisms of *Quaternion Rotations and Reflections*.

### Relation Between the Norm Form and the Inner Product

**Proposition.** The norm form is the diagonal of the inner product, $N(\tilde q) = \langle \tilde q, \tilde q\rangle$, and the inner product is recovered from the norm form by polarisation,

$$
\langle p, \tilde q\rangle = \tfrac{1}{2}\bigl(N(p+\tilde q) - N(p) - N(\tilde q)\bigr).
$$

The two forms are therefore the same datum: a positive definite quadratic form on a four-dimensional real space, whose associated bilinear form is the Euclidean inner product. The multiplicativity of $N$ is an extra property, not shared by a general Euclidean form.

## Invertibility

### Definition

**Definition.** An element $\tilde q\in\mathbb{H}$ is **invertible** if there is $p\in\mathbb{H}$ with $pq = qp = 1$; the element $p$ is then the **inverse** and is written $\tilde q^{-1}$.

**Proposition.** The inverse, when it exists, is unique, and the invertible elements of $\mathbb{H}$ form a group under multiplication.

*Proof.* If $p$ and $p'$ are inverses then $p = p1 = p(qp') = (pq)p' = p'$. Closure, associativity, the identity and the existence of inverses are then immediate, so the invertible elements form a group. $\square$

### Left and Right Inverses

**Theorem.** For $\tilde q\in\mathbb{H}$ the following are equivalent: $\tilde q$ has a left inverse; $\tilde q$ has a right inverse; $\tilde q$ has a two-sided inverse; $N(\tilde q)\neq 0$.

*Proof.* If $pq = 1$ for some $p$, then $N(p)N(\tilde q) = N(pq) = 1$, so $N(\tilde q)\neq 0$ in the base field; conversely if $N(\tilde q)\neq 0$ then $\tilde q\cdot(\tilde q^{-1}) $ with $\tilde q^{-1} = \bar{\tilde q}/N(\tilde q)$ is a two-sided inverse by the inverse formula below. The right case is symmetric. $\square$

Thus, over a field of characteristic not $2$, the three notions coincide, and an element is a unit exactly when its norm form does not vanish.

### Criterion for Invertibility

**Theorem.** A quaternion $\tilde q$ is invertible if and only if $\tilde q\neq 0$ over $F = \mathbb{R}$; more generally, $\tilde q$ is invertible if and only if $N(\tilde q)\neq 0$, and over a field of characteristic not $2$ the vanishing of $N$ away from $0$ is exactly what it means for the algebra to fail to be a division algebra.

*Proof.* Over $\mathbb{R}$ the norm form is positive definite, so $N(\tilde q) = 0$ holds only for $\tilde q = 0$; by the criterion of the preceding paragraph every non-zero $\tilde q$ is a unit. $\square$

### The Inverse Formula

**Theorem.** If $N(\tilde q)\neq 0$ then

$$
\tilde q^{-1} = \frac{\bar{\tilde q}}{N(\tilde q)} = \frac{\bar{\tilde q}}{\tilde q\bar{\tilde q}}.
$$

*Proof.* $(\tilde q)(\bar{\tilde q}/N(\tilde q)) = (\tilde q\bar{\tilde q})/N(\tilde q) = N(\tilde q)/N(\tilde q) = 1$, and $(\bar{\tilde q}/N(\tilde q))(\tilde q) = (\bar{\tilde q} \tilde q)/N(\tilde q) = 1$ because $\bar{\tilde q} \tilde q = N(\tilde q)$ is central. $\square$

For a unit quaternion $N(\tilde q) = 1$ the formula reduces to $\tilde q^{-1} = \bar{\tilde q}$: on the unit sphere, inversion is conjugation. For a pure imaginary $x$ one has $\bar x = -x$ and $x^{-1} = -x/N(x)$, so the imaginary line is closed under inversion up to the real scale.

## The Group of Units

### Definition

**Definition.** The **group of units** of $\mathbb{H}$ is

$$
\mathbb{H}^{\times} = \{\tilde q\in\mathbb{H} : N(\tilde q)\neq 0\}.
$$

**Proposition.** $\mathbb{H}^{\times}$ is a group under multiplication, it is the complement of the set $\{\tilde q : N(\tilde q) = 0\}$, and over $\mathbb{R}$ it is $\mathbb{H}\setminus\{0\}$.

*Proof.* Closure and inverses are the multiplicativity of $N$ and the inverse formula; the complement description is the criterion for invertibility. Over $\mathbb{R}$ the vanishing set of $N$ is $\{0\}$ by positive definiteness. $\square$

### Basic Properties

**Theorem.** The centre of $\mathbb{H}^{\times}$ is $F^{\times} = F\setminus\{0\}$, realised as the non-zero scalars; over $\mathbb{R}$ every central quaternion is real, and the centre is $\mathbb{R}^{\times}$.

*Proof.* An element commuting with every quaternion is central in $\mathbb{H}$; the centre of the quaternion algebra over a field of characteristic not $2$ is the scalar field, as in *Quaternion Algebra*. Conversely a non-zero scalar commutes with everything and is invertible. $\square$

### The Inverse Map

**Proposition.** The inverse map $\tilde q\mapsto \tilde q^{-1}$ is an anti-automorphism of the group: $(pq)^{-1} = \tilde q^{-1}p^{-1}$. It is the composite of the conjugation anti-automorphism $\tilde q\mapsto\bar{\tilde q}$ with the central scalar division $\tilde q\mapsto \tilde q/N(\tilde q)$, and it coincides with conjugation on the unit sphere $N(\tilde q) = 1$.

*Proof.* $(pq)(\tilde q^{-1}p^{-1}) = p(qq^{-1})p^{-1} = pp^{-1} = 1$ by associativity. The formula $\tilde q^{-1} = \bar{\tilde q}/N(\tilde q)$ then exhibits the composite. $\square$

### The Polar Split of the Units

**Theorem.** Over $\mathbb{R}$ the group of units factors as a direct product

$$
\mathbb{H}^{\times} \cong \mathbb{R}_{>0}\times Sp(1), \qquad \tilde q = |\tilde q|\,\frac{\tilde q}{|\tilde q|},
$$

where $Sp(1) = \{\tilde q : N(\tilde q) = 1\}$ is the unit sphere $S^3$ and the two factors commute. The map is a homeomorphism and a group isomorphism, and $Sp(1)$ is a compact connected Lie group.

*Proof.* The map $\tilde q\mapsto(|\tilde q|, \tilde q/|\tilde q|)$ is a bijection with inverse $(r,u)\mapsto ru$, it is a homomorphism because the modulus is multiplicative and positive, and it is continuous with continuous inverse. Every positive real is central, so the two factors commute and the product is direct. The identification $Sp(1) = S^3$ is the definition, and the Lie-group statements are those of *Quaternion Rotations and Reflections*. $\square$

Thus every unit is the product of a positive scale and a unit quaternion, and the two factors are unique. This is the polar decomposition of the quaternion algebra, and it divides the group theory of the units into the multiplicative group $\mathbb{R}_{>0}$ and the compact group $Sp(1)$.

## The Absence of Zero Divisors

**Definition.** An element $\tilde q\neq 0$ is a **zero divisor** if there is $p\neq 0$ with $pq = 0$ or $qp = 0$.

**Theorem.** Over $F = \mathbb{R}$ the algebra $\mathbb{H}$ has no zero divisors: $pq = 0$ implies $p = 0$ or $\tilde q = 0$.

*Proof.* Take norms: $N(pq) = N(p)N(\tilde q)$ and $N(pq) = 0$, so $N(p)N(\tilde q) = 0$ in the field $\mathbb{R}$, hence $N(p) = 0$ or $N(\tilde q) = 0$, and by positive definiteness $p = 0$ or $\tilde q = 0$. $\square$

The same argument shows that over any field in which the norm form is anisotropic — that is, vanishes only at the origin — there are no zero divisors. The failure of anisotropy is exactly the failure of the algebra to be a division algebra: if $N(\tilde q) = 0$ for some $\tilde q\neq 0$, then $\bar{\tilde q}$ is a non-zero element annihilating $\tilde q$.

## The Three-Way Classification

The elements of the biquaternion algebra fall into three classes: the invertible elements, the non-zero zero divisors, and zero. The three are mutually exclusive and, over the complex field, exhaust the algebra. Here the classification has the same three slots but one of them is empty.

**Theorem (classification).** Over $\mathbb{R}$ every quaternion is exactly one of the following:

| Class | Condition | Status in $\mathbb{H}$ |
|---|---|---|
| invertible | $N(\tilde q)\neq 0$ | non-empty; every $\tilde q\neq 0$ |
| zero divisor, non-zero | $\tilde q\neq 0$ and $N(\tilde q) = 0$ | empty |
| zero | $\tilde q = 0$ | a single element |

*Proof.* The classes are defined by the mutually exclusive conditions $N\neq 0$, $N = 0$ with $\tilde q\neq 0$, and $\tilde q = 0$. The middle class is empty by positive definiteness, and the first class is the whole punctured algebra. $\square$

**Corollary.** Over $\mathbb{R}$ the algebra $\mathbb{H}$ is a division algebra: for $a\neq 0$ the equations $ax = b$ and $xa = b$ have the unique solutions $x = a^{-1}b$ and $x = ba^{-1}$ respectively.

*Proof.* The classification makes every non-zero element invertible; multiplying the equation $ax = b$ on the left by $a^{-1}$ gives $x = a^{-1}b$, and uniqueness is the same computation, the right case being symmetric. $\square$

The division property is the reason the quaternion algebra stands at the head of its family: it is a four-dimensional real division algebra, and it is the largest-dimensional associative one.

## Comparison with the Biquaternion Case

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries the same multiplication table with the coefficients extended from $\mathbb{R}$ to $\mathbb{C}$, and its norm form

$$
N(\tilde Q) = \tilde Q\,\bar{\tilde Q}
$$

takes values in $\mathbb{C}$ rather than in $\mathbb{R}$. The comparison isolates what the real coefficient field buys.

| Feature | $\mathbb{H}$ over $\mathbb{R}$ | $\mathbb{B}$ over $\mathbb{C}$ |
|---|---|---|
| Values of $N$ | non-negative reals | complex numbers |
| Positive definite | yes | no |
| Zero divisors | none | the null cone $N = 0$ |
| Invertibility criterion | $\tilde q\neq 0$ | $N(\tilde Q)\neq 0$ |
| Classes of elements | two (zero, invertible) | three (invertible, zero divisor, zero) |
| Group of units | $\mathbb{R}_{>0}\times Sp(1)$ | $GL_2(\mathbb{C})$, connected |

In the biquaternion case the norm form is a complex-valued quadratic form, its zero set is the null cone, and an element with $N = 0$ but $\tilde Q\neq 0$ is a genuine zero divisor; the three-way classification is then a genuine trichotomy. Here the norm form is real and positive definite, the null cone degenerates to the origin, the middle class of the classification is empty, and the unit group is the product of a line and a compact group. The biquaternion case is treated in *Biquaternion Norm and Invertibility*.

## Summary

The quaternion algebra carries the multiplicative quadratic form $N(\tilde q) = \tilde q\bar{\tilde q} = \bar{\tilde q} \tilde q = \sum_\mu q_\mu^2$, central valued and multiplicative, $N(pq) = N(p)N(\tilde q)$; over $\mathbb{R}$ it is positive definite, and its square root is the modulus, the unique real norm compatible with the algebra. The associated inner product is $\langle p,\tilde q\rangle = \operatorname{Sc}(p\bar{\tilde q})$, a real symmetric bilinear form whose diagonal is $N(\tilde q)$ and whose polarisation recovers it; the Hermitian form $\tilde q\bar{\tilde q}$ coincides with $N(\tilde q)$.

Invertibility is decided by the norm: $\tilde q$ is a unit exactly when $N(\tilde q)\neq 0$, the inverse being $\tilde q^{-1} = \bar{\tilde q}/N(\tilde q)$, which reduces to $\tilde q^{-1} = \bar{\tilde q}$ on the unit sphere. Over $\mathbb{R}$ every non-zero quaternion is invertible, the algebra has no zero divisors, and it is a division algebra, so the three-way classification of the biquaternion case collapses to the dichotomy zero or invertible. The group of units is $\mathbb{H}^{\times} = \mathbb{H}\setminus\{0\}$, with centre the non-zero scalars, and it splits as the direct product $\mathbb{R}_{>0}\times Sp(1)$ of a positive scale and the unit sphere.

The contrast with the biquaternion case is the contrast between a real and a complex norm form: the complex norm has a null cone, the null cone supplies non-zero zero divisors, and the trichotomy invertible–zero-divisor–zero is genuine there, whereas here it degenerates.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $F$ | Base field of characteristic not $2$; $\mathbb{R}$ for the definite statements |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3 = \sum_{\mu=0}^{3} q_\mu e_\mu$ | General quaternion, scalar part $q_0$, vector part $\mathbf{q}$ |
| $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ | Quaternion conjugate |
| $N(\tilde q) = \tilde q\bar{\tilde q} = \bar{\tilde q} \tilde q$ | Norm form |
| $\lvert \tilde q\rvert = \sqrt{N(\tilde q)}$ | Modulus over $\mathbb{R}$ |
| $\langle p,\tilde q\rangle = \operatorname{Sc}(p\bar{\tilde q})$ | Inner product, $N(\tilde q) = \langle \tilde q,\tilde q\rangle$ |
| $\tilde q\bar{\tilde q}$ | Hermitian form, coinciding with $N(\tilde q)$ |
| $\tilde q^{-1} = \bar{\tilde q}/N(\tilde q)$ | Inverse formula |
| $\mathbb{H}^{\times} = \{\tilde q : N(\tilde q)\neq 0\}$ | Group of units |
| $Sp(1) = \{\tilde q : N(\tilde q) = 1\} = S^3$ | Unit quaternions, the compact factor |
| $\mathbb{H}^{\times}\cong\mathbb{R}_{>0}\times Sp(1)$ | Polar split of the units |
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, for contrast |
| $N(\tilde Q) = \tilde Q\bar{\tilde Q}$ | Complex-valued norm form of $\mathbb{B}$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the norm form and its multiplicativity.
- Leonard Dickson, *Algebras and Their Arithmetics* (University of Chicago Press, 1923), for the norm form and the division property of the quaternion algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the reduced norm and the group of units of a central simple algebra.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for multiplicative quadratic forms and the anisotropic case.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the norm form, the unit sphere and the division algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the identification of the norm form with a Clifford norm.
