# __Norm and Invertibility in the Quaternion Algebra__

## Introduction

The quaternion algebra $\mathbb{H}$ is the four-dimensional algebra with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ and the multiplication rules $\vec e_x^2 = \vec e_y^2 = \vec e_z^2 = \vec e_x\vec e_y\vec e_z = -e_t$, so that $\vec e_x\vec e_y = \vec e_z$ and the basis elements anticommute in pairs. This article studies the multiplicative quadratic form that the algebra carries, the **quaternion norm** $\langle\tilde q\rangle_{\natural} = \tilde q\tilde{q}^{\natural}$, and the property that the form forces: every non-zero quaternion is invertible, so that $\mathbb{H}$ is a division algebra. It is the entry of the quaternion family that owns the quaternion norm, its multiplicativity, the inverse formula and the group of units.

The companion article *Quaternion Algebra* fixes the basis, the conjugation, the multiplication table and the scalar–vector decomposition, and they are used here without restatement. The companion article *Ideals and Simplicity of the Quaternion Algebra*, below this article in this category treats the absence of proper one- and two-sided ideals and the central-simplicity statement; this article owns the quaternion norm, the multiplicativity, the invertibility criterion and the unit group, and it refers to that article for the ideal-theoretic consequences. A reader who wants the full structure of the algebra should read the three together: the algebra supplies the multiplication, this article supplies the quaternion norm and the division property, and the ideals article supplies the consequences of division for the ideal structure.

The corpus's default base is a commutative ring with identity, and the algebra $\mathbb{H}$ is defined over such a base by the same presentation. The results of this article that need more than that base are obtained over a field $F$ of characteristic not $2$; the positivity statements are obtained over $F = \mathbb{R}$, and they are flagged where they occur. In particular, the multiplicativity of the quaternion norm, the inverse formula and the group-of-units statements hold over any field of characteristic not $2$, whereas the statement that the quaternion norm is positive definite, the polar split of the unit group, and the identification of the unit sphere are statements over $\mathbb{R}$.

Throughout, a quaternion is written

$$
\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z = \sum_{\mu\in\{t,x,y,z\}} q_\mu e_\mu, \qquad q_t, q_x, q_y, q_z \in F,
$$

with **scalar part** $\mathrm{Sc}(\tilde q) = q_t$ and **vector part** $\vec q = q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$; the **conjugate** is $\tilde{q}^{\natural} = q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z$. The pure imaginary subspace is $\operatorname{Im}\mathbb{H} = \{\tilde q : \tilde{q}^{\natural} = -\tilde q\}$.

## The Quaternion Norm

### Definition

**Definition.** The **quaternion norm** of $\tilde q$ is

$$
\langle\tilde q\rangle_{\natural} = \tilde q\tilde{q}^{\natural} = \tilde{q}^{\natural} \tilde q = q_t^2 + q_x^2 + q_y^2 + q_z^2.
$$

The equality of the two products is checked from the multiplication table: the vector part of $\tilde q\tilde{q}^{\natural}$ is $q_t\vec q - \vec q q_t + \vec q\times(-\vec q) = 0$, and the scalar calculation is the sum of squares.

**Proposition.** $\langle\tilde q\rangle_{\natural}$ is a central element of $\mathbb{H}$, it lies in the image of $F$, and the map $N : \mathbb{H}\to F$ is a quadratic form on the underlying vector space, with polar form $\mathfrak{b}(\tilde q_1,\tilde q_2) = \mathrm{Sc}(\tilde q_1\tilde q_2^{\natural})$.

*Proof.* The scalar part of $\tilde q\tilde{q}^{\natural}$ is $\sum_\mu q_\mu^2$, a scalar, and a scalar commutes with every quaternion; this is the centrality. The coordinate expression is homogeneous of degree two and its polarisation is $\mathrm{Sc}(\tilde q_1\tilde q_2^{\natural})$, as the polar form of a sum of squares.

### Multiplicativity

**Theorem.** The quaternion norm is multiplicative:

$$
\langle\tilde q_1\tilde q_2\rangle_{\natural} = \langle\tilde q_1\rangle_{\natural}\,\langle\tilde q_2\rangle_{\natural}, \qquad \tilde q_1, \tilde q_2 \in \mathbb{H}.
$$

*Proof.* Using $(\tilde q_1\tilde q_2)^{\natural} = \tilde q_2^{\natural}\tilde q_1^{\natural}$ and the fact that $\langle\tilde q\rangle_{\natural} = \tilde q\tilde{q}^{\natural}$ is central,

$$
\langle\tilde q_1\tilde q_2\rangle_{\natural} = (\tilde q_1\tilde q_2)(\tilde q_1\tilde q_2)^{\natural} = \tilde q_1\tilde q_2\,\tilde q_2^{\natural}\,\tilde q_1^{\natural} = \tilde q_1\,\langle\tilde q_2\rangle_{\natural}\,\tilde q_1^{\natural} = \langle\tilde q_2\rangle_{\natural}\,\tilde q_1 \tilde q_1^{\natural} = \langle\tilde q_1\rangle_{\natural}\langle\tilde q_2\rangle_{\natural}.
$$

Multiplicativity is the single feature that makes the quaternion norm the algebraic centre of gravity of the subject. It holds over any commutative base in which the computation makes sense, and in particular over any field.

**Corollary.** If $\langle\tilde q_1\rangle_{\natural} = 0$ then $\langle\tilde q_1\tilde q_2\rangle_{\natural} = \langle\tilde q_2\tilde q_1\rangle_{\natural} = 0$ for every $\tilde q_2$, so a vanishing norm propagates and neither $\tilde q_1$ nor any multiple of it is a unit; over a field over which the quaternion norm is anisotropic, that is $\langle\tilde q_3\rangle_{\natural} = 0$ only for $\tilde q_3 = 0$, this middle case is empty and every non-zero element is a unit.

### Positive Definiteness and the Real Case

**Theorem.** Over $F = \mathbb{R}$ the quaternion norm is positive definite: $\langle\tilde q\rangle_{\natural} \geq 0$ for every $\tilde q$, and $\langle\tilde q\rangle_{\natural} = 0$ if and only if $\tilde q = 0$.

*Proof.* $\langle\tilde q\rangle_{\natural} = \sum_\mu q_\mu^2$ is a sum of squares of real numbers, hence non-negative, and it vanishes only when every $q_\mu$ vanishes.

**Definition.** Over $\mathbb{R}$ the **modulus** of $\tilde q$ is $|\tilde q| = \sqrt{\langle\tilde q\rangle_{\natural}}$, a non-negative real number, zero only at $\tilde q = 0$, and the modulus is multiplicative,

$$
|\tilde q_1\tilde q_2| = |\tilde q_1|\,|\tilde q_2|,
$$

because $\langle\cdot\rangle_{\natural}$ is multiplicative by the theorem above and $\langle\cdot\rangle_{\natural}$ is non-negative on $\mathbb{R}$. The modulus is the value of the quaternion norm under the real square root; its metric properties on $\mathbb{H}\cong\mathbb{R}^4$ are owned by *Quaternion Topology*, below this article in this category, and the algebra uses it only through the multiplicativity just displayed and the polar split of the units below.

### The Quaternion Norm and the Conjugate

**Proposition.** The quaternion norm is invariant under conjugation, $\langle\tilde{q}^{\natural}\rangle_{\natural} = \langle\tilde q\rangle_{\natural}$, and it is the **reduced norm** of $\mathbb{H}$ viewed as a central simple algebra of degree two over the base field.

*Proof.* $\langle\tilde{q}^{\natural}\rangle_{\natural} = \tilde{q}^{\natural} \tilde q = \langle\tilde q\rangle_{\natural}$. For a central simple algebra over a field the corresponding form is the reduced norm; for a quaternion algebra the reduced norm is the quaternion norm above, and the identification is the classical one, quoted here as standard.

## The Inner Product

### Definition

**Definition.** The **inner product** of two quaternions is

$$
\langle\tilde q_1, \tilde q_2\rangle = \mathrm{Sc}(\tilde q_1\tilde q_2^{\natural}) = \sum_{\mu\in\{t,x,y,z\}} q_{1\mu} q_{2\mu},
$$

a symmetric bilinear form on the real vector space $\mathbb{H}$. The one-variable expression $\tilde q\tilde{q}^{\natural}$ is the **Hermitian form**; in the quaternion case, the coefficients being real, it coincides with the quaternion norm, as in *Quaternion Algebra*.

**Proposition.** The form $\langle\cdot,\cdot\rangle$ is bilinear, symmetric and positive definite over $\mathbb{R}$; it satisfies $\langle\tilde q_1, \tilde q_2\rangle = \mathrm{Sc}(\tilde q_1^{\natural} \tilde q_2)$, and it is invariant under left and under right multiplication by a unit quaternion.

*Proof.* Bilinearity and symmetry are immediate from the coordinate expression. Positive definiteness is $\langle \tilde q,\tilde q\rangle = \sum_\mu q_\mu^2 = \langle\tilde q\rangle_{\natural}$. For a unit $u$, $\langle u\tilde q_1, u\tilde q_2\rangle = \mathrm{Sc}(u\tilde q_1(u\tilde q_2)^{\natural}) = \mathrm{Sc}(u\,\tilde q_1\tilde q_2^{\natural}\,u^{\natural}) = \mathrm{Sc}(\tilde q_1\tilde q_2^{\natural})$ because conjugation by a unit preserves the scalar part, as in *Quaternion Rotations and Reflections*, below this article in this category; the right case is the same computation.

### The Group of Linear Maps Preserving the Form

In the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the Gram matrix of the inner product is the identity, $\langle\cdot,\cdot\rangle=\sum_\mu q_{1\mu} q_{2\mu}$, so a linear map $T$ preserves the form exactly when its matrix satisfies the algebraic condition $T^{\mathsf T}T=\mathrm I_4$; the group of linear maps preserving the form is therefore the group defined by that matrix condition, $T^{\mathsf T}T=\mathrm I_4$, named here algebraically. The inner automorphisms $\tilde q\mapsto u\tilde q u^{-1}$ of the units are elements of that group, since conjugation by a unit preserves the scalar part; their further reading is in *Quaternion Rotations and Reflections*, below this article in this category and *Quaternion Automorphisms and Derivations*, below this article in this category.

### Relation Between the Quaternion Norm and the Inner Product

**Proposition.** The quaternion norm is the diagonal of the inner product, $\langle\tilde q\rangle_{\natural} = \langle \tilde q, \tilde q\rangle$, and the inner product is recovered from the quaternion norm by polarisation,

$$
\langle\tilde q_1, \tilde q_2\rangle = \tfrac{1}{2}\bigl(\langle\tilde q_1+\tilde q_2\rangle_{\natural} - \langle\tilde q_1\rangle_{\natural} - \langle\tilde q_2\rangle_{\natural}\bigr).
$$

The two forms are therefore the same datum: a positive definite quadratic form on a four-dimensional real space, whose associated bilinear form is the inner product. The multiplicativity of $\langle\cdot,\cdot\rangle_{\natural}$ is an extra property, not shared by a general positive definite form.

## Invertibility

### Definition

**Definition.** An element $\tilde q_1\in\mathbb{H}$ is **invertible** if there is $\tilde q_2\in\mathbb{H}$ with $\tilde q_2\tilde q_1 = \tilde q_1\tilde q_2 = 1$; the element $\tilde q_2$ is then the **inverse** and is written $\tilde q_1^{-1}$.

**Proposition.** The inverse, when it exists, is unique, and the invertible elements of $\mathbb{H}$ form a group under multiplication.

*Proof.* If $\tilde q_1$ and $\tilde q_2$ are inverses then $\tilde q_1 = \tilde q_1 1 = \tilde q_1(\tilde q_3 \tilde q_2) = (\tilde q_1\tilde q_3)\tilde q_2 = \tilde q_2$. Closure, associativity, the identity and the existence of inverses are then immediate, so the invertible elements form a group.

### Left and Right Inverses

**Theorem.** For $\tilde q\in\mathbb{H}$ the following are equivalent: $\tilde q$ has a left inverse; $\tilde q$ has a right inverse; $\tilde q$ has a two-sided inverse; $\langle\tilde q\rangle_{\natural}\neq 0$.

*Proof.* If $\tilde q_1\tilde q_2 = 1$ for some $\tilde q_1$, then $\langle\tilde q_1\rangle_{\natural}\langle\tilde q_2\rangle_{\natural} = \langle\tilde q_1\tilde q_2\rangle_{\natural} = 1$, so $\langle\tilde q_2\rangle_{\natural}\neq 0$ in the base field; conversely if $\langle\tilde q_2\rangle_{\natural}\neq 0$ then $\tilde q_2\cdot(\tilde q_2^{-1}) $ with $\tilde q_2^{-1} = \tilde q_2^{\natural}/\langle\tilde q_2\rangle_{\natural}$ is a two-sided inverse by the inverse formula below. The right case is symmetric.

Thus, over a field of characteristic not $2$, the three notions coincide, and an element is a unit exactly when its quaternion norm does not vanish.

### Criterion for Invertibility

**Theorem.** A quaternion $\tilde q$ is invertible if and only if $\tilde q\neq 0$ over $F = \mathbb{R}$; more generally, $\tilde q$ is invertible if and only if $\langle\tilde q\rangle_{\natural}\neq 0$, and over a field of characteristic not $2$ the vanishing of $\langle\cdot\rangle_{\natural}$ away from $0$ is exactly what it means for the algebra to fail to be a division algebra.

*Proof.* Over $\mathbb{R}$ the quaternion norm is positive definite, so $\langle\tilde q\rangle_{\natural} = 0$ holds only for $\tilde q = 0$; by the criterion of the preceding paragraph every non-zero $\tilde q$ is a unit.

### The Inverse Formula

**Theorem.** If $\langle\tilde q\rangle_{\natural}\neq 0$ then

$$
\tilde q^{-1} = \frac{\tilde{q}^{\natural}}{\langle\tilde q\rangle_{\natural}} = \frac{\tilde{q}^{\natural}}{\tilde q\tilde{q}^{\natural}}.
$$

*Proof.* $(\tilde q)(\tilde{q}^{\natural}/\langle\tilde q\rangle_{\natural}) = (\tilde q\tilde{q}^{\natural})/\langle\tilde q\rangle_{\natural}/\langle\tilde q\rangle_{\natural} = 1$, and $(\tilde{q}^{\natural}/\langle\tilde q\rangle_{\natural})(\tilde q) = (\tilde{q}^{\natural} \tilde q)/\langle\tilde q\rangle_{\natural} = 1$ because $\tilde{q}^{\natural} \tilde q = \langle\tilde q\rangle_{\natural}$ is central.

For a unit quaternion $\langle\tilde q\rangle_{\natural} = 1$ the formula reduces to $\tilde q^{-1} = \tilde{q}^{\natural}$: on the unit sphere, inversion is conjugation. For a pure imaginary $\vec q$ one has $\vec q^{\natural} = -\vec q$ and $\vec q^{-1} = -\vec q/\langle \vec q\rangle_{\natural}$, so the imaginary line is closed under inversion up to the real scale.

## The Group of Units

### Definition

**Definition.** The **group of units** of $\mathbb{H}$ is

$$
\mathbb{H}^{\times} = \{\tilde q\in\mathbb{H} : \langle\tilde q\rangle_{\natural}\neq 0\}.
$$

**Proposition.** $\mathbb{H}^{\times}$ is a group under multiplication, it is the complement of the set $\{\tilde q : \langle\tilde q\rangle_{\natural} = 0\}$, and over $\mathbb{R}$ it is $\mathbb{H}\setminus\{0\}$.

*Proof.* Closure and inverses are the multiplicativity of $\langle\cdot\rangle_{\natural}$ and the inverse formula; the complement description is the criterion for invertibility. Over $\mathbb{R}$ the vanishing set of $\langle\cdot\rangle_{\natural}$ is $\{0\}$ by positive definiteness.

### Basic Properties

**Theorem.** The centre of $\mathbb{H}^{\times}$ is $F^{\times} = F\setminus\{0\}$, realised as the non-zero scalars; over $\mathbb{R}$ every central quaternion is real, and the centre is $\mathbb{R}^{\times}$.

*Proof.* An element commuting with every quaternion is central in $\mathbb{H}$; the centre of the quaternion algebra over a field of characteristic not $2$ is the scalar field, as in *Quaternion Algebra*. Conversely a non-zero scalar commutes with everything and is invertible.

### The Inverse Map

**Proposition.** The inverse map $\tilde q\mapsto \tilde q^{-1}$ is an anti-automorphism of the group: $(\tilde q_1\tilde q_2)^{-1} = \tilde q_2^{-1}\tilde q_1^{-1}$. It is the composite of the conjugation anti-automorphism $\tilde q\mapsto\tilde{q}^{\natural}$ with the central scalar division $\tilde q\mapsto \tilde q/\langle\tilde q\rangle_{\natural}$, and it coincides with conjugation on the unit sphere $\langle\tilde q\rangle_{\natural} = 1$.

*Proof.* $(\tilde q_1\tilde q_2)(\tilde q_2^{-1}\tilde q_1^{-1}) = \tilde q_1(\tilde q_2\tilde q_2^{-1})\tilde q_1^{-1} = \tilde q_1\tilde q_1^{-1} = 1$ by associativity. The formula $\tilde q^{-1} = \tilde{q}^{\natural}/\langle\tilde q\rangle_{\natural}$ then exhibits the composite.

### The Polar Split of the Units

**Theorem.** Over $\mathbb{R}$ the group of units factors as a direct product

$$
\mathbb{H}^{\times} \cong \mathbb{R}_{>0}\times \mathbb{H}^1, \qquad \tilde q = |\tilde q|\,\frac{\tilde q}{|\tilde q|},
$$

where $\mathbb{H}^1 = \{\tilde q : \langle\tilde q\rangle_{\natural} = 1\}$ is the unit sphere, the shell of the norm-one elements, and the two factors commute. The map is an isomorphism of groups; the topological structure of $\mathbb{H}^1$ is owned by *The Quaternion Unit Group as a Topological Group*, below this article in this category.

*Proof.* The map $\tilde q\mapsto(|\tilde q|, \tilde q/|\tilde q|)$ is a bijection with inverse $(r,u)\mapsto ru$, and it is a homomorphism because the modulus is multiplicative and positive. Every positive real is central, so the two factors commute and the product is direct. The identification $\mathbb{H}^1 = \{\tilde q : \langle\tilde q\rangle_{\natural} = 1\}$ is the definition.

Thus every unit is the product of a positive scale and a unit quaternion, and the two factors are unique. This is the polar decomposition of the quaternion algebra, and it divides the group theory of the units into the multiplicative group $\mathbb{R}_{>0}$ and the norm-one shell $\mathbb{H}^1$.

## The Absence of Zero Divisors

**Definition.** An element $\tilde q_1\neq 0$ is a **zero divisor** if there is $\tilde q_2\neq 0$ with $\tilde q_2\tilde q_1 = 0$ or $\tilde q_1\tilde q_2 = 0$.

**Theorem.** Over $F = \mathbb{R}$ the algebra $\mathbb{H}$ has no zero divisors: $\tilde q_1\tilde q_2 = 0$ implies $\tilde q_1 = 0$ or $\tilde q_2 = 0$.

*Proof.* Take norms: $\langle\tilde q_1\tilde q_2\rangle_{\natural} = \langle\tilde q_1\rangle_{\natural}\langle\tilde q_2\rangle_{\natural}$ and $\langle\tilde q_1\tilde q_2\rangle_{\natural} = 0$, so $\langle\tilde q_1\rangle_{\natural}\langle\tilde q_2\rangle_{\natural} = 0$ in the field $\mathbb{R}$, hence $\langle\tilde q_1\rangle_{\natural} = 0$ or $\langle\tilde q_2\rangle_{\natural} = 0$, and by positive definiteness $\tilde q_1 = 0$ or $\tilde q_2 = 0$.

The same argument shows that over any field in which the quaternion norm is anisotropic — that is, vanishes only at the origin — there are no zero divisors. The failure of anisotropy is exactly the failure of the algebra to be a division algebra: if $\langle\tilde q\rangle_{\natural} = 0$ for some $\tilde q\neq 0$, then $\tilde{q}^{\natural}$ is a non-zero element annihilating $\tilde q$.

## The Three-Way Classification

The three are mutually exclusive and, over the complex field, exhaust the algebra. Here the classification has the same three slots but one of them is empty.

**Theorem (classification).** Over $\mathbb{R}$ every quaternion is exactly one of the following:

| Class | Condition | Status in $\mathbb{H}$ |
|---|---|---|
| invertible | $\langle\tilde q\rangle_{\natural}\neq 0$ | non-empty; every $\tilde q\neq 0$ |
| zero divisor, non-zero | $\tilde q\neq 0$ and $\langle\tilde q\rangle_{\natural} = 0$ | empty |
| zero | $\tilde q = 0$ | a single element |

*Proof.* The classes are defined by the mutually exclusive conditions $N\neq 0$, $N = 0$ with $\tilde q\neq 0$, and $\tilde q = 0$. The middle class is empty by positive definiteness, and the first class is the whole punctured algebra.

**Corollary.** Over $\mathbb{R}$ the algebra $\mathbb{H}$ is a division algebra: for $\tilde q_1\neq 0$ the equations $\tilde q_1\tilde q_2 = \tilde q_3$ and $\tilde q_2\tilde q_1 = \tilde q_3$ have the unique solutions $\tilde q_2 = \tilde q_1^{-1}\tilde q_3$ and $\tilde q_2 = \tilde q_3\tilde q_1^{-1}$ respectively.

*Proof.* The classification makes every non-zero element invertible; multiplying the equation $\tilde q_1\tilde q_2 = \tilde q_3$ on the left by $\tilde q_1^{-1}$ gives $\tilde q_2 = \tilde q_1^{-1}\tilde q_3$, and uniqueness is the same computation, the right case being symmetric.

The division property is the reason the quaternion algebra stands at the head of its family: it is a four-dimensional real division algebra, and it is the largest-dimensional associative one.

## Summary

The quaternion algebra carries the multiplicative quadratic form $\langle\tilde q\rangle_{\natural} = \tilde q\tilde{q}^{\natural} = \tilde{q}^{\natural} \tilde q = \sum_\mu q_\mu^2$, central valued and multiplicative, $\langle\tilde q_1\tilde q_2\rangle_{\natural} = \langle\tilde q_1\rangle_{\natural}\langle\tilde q_2\rangle_{\natural}$; over $\mathbb{R}$ it is positive definite, and its square root is the modulus, the unique real norm compatible with the algebra. The associated inner product is $\langle\tilde q_1,\tilde q_2\rangle = \mathrm{Sc}(\tilde q_1\tilde q_2^{\natural})$, a real symmetric bilinear form whose diagonal is $\langle\tilde q\rangle_{\natural}$ and whose polarisation recovers it; the Hermitian form $\tilde q\tilde{q}^{\natural}$ coincides with $\langle\tilde q\rangle_{\natural}$.

Invertibility is decided by the quaternion norm: $\tilde q$ is a unit exactly when $\langle\tilde q\rangle_{\natural}\neq 0$, the inverse being $\tilde q^{-1} = \tilde{q}^{\natural}/\langle\tilde q\rangle_{\natural}$, which reduces to $\tilde q^{-1} = \tilde{q}^{\natural}$ on the unit sphere. The group of units is $\mathbb{H}^{\times} = \mathbb{H}\setminus\{0\}$, with centre the non-zero scalars, and it splits as the direct product $\mathbb{R}_{>0}\times \mathbb{H}^1$ of a positive scale and the unit sphere.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $F$ | Base field of characteristic not $2$; $\mathbb{R}$ for the definite statements |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z = \sum_{\mu\in\{t,x,y,z\}} q_\mu e_\mu$ | General quaternion, scalar part $q_t$, vector part $\vec q$ |
| $\tilde{q}^{\natural} = q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z$ | Quaternion conjugate |
| $\langle\tilde q\rangle_{\natural} = \tilde q\tilde{q}^{\natural} = \tilde{q}^{\natural} \tilde q$ | Quaternion norm |
| $\lvert \tilde q\rvert = \sqrt{\langle\tilde q\rangle_{\natural}}$ | Modulus over $\mathbb{R}$ |
| $\langle\tilde q_1,\tilde q_2\rangle = \mathrm{Sc}(\tilde q_1\tilde q_2^{\natural})$ | Inner product, $\langle\tilde q\rangle_{\natural} = \langle \tilde q,\tilde q\rangle$ |
| $\tilde q\tilde{q}^{\natural}$ | Hermitian form, coinciding with $\langle\tilde q\rangle_{\natural}$ |
| $\tilde q^{-1} = \tilde{q}^{\natural}/\langle\tilde q\rangle_{\natural}$ | Inverse formula |
| $\mathbb{H}^{\times} = \{\tilde q : \langle\tilde q\rangle_{\natural}\neq 0\}$ | Group of units |
| $\mathbb{H}^1 = \{\tilde q : \langle\tilde q\rangle_{\natural} = 1\}$ | Unit quaternions, the norm-one shell |
| $\mathbb{H}^{\times}\cong\mathbb{R}_{>0}\times \mathbb{H}^1$ | Polar split of the units |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the quaternion norm and its multiplicativity.
- Leonard Dickson, *Algebras and Their Arithmetics* (University of Chicago Press, 1923), for the quaternion norm and the division property of the quaternion algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the reduced norm and the group of units of a central simple algebra.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for multiplicative quadratic forms and the anisotropic case.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion norm, the unit sphere and the division algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the identification of the quaternion norm with a Clifford norm.
