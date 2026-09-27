
# __Real Norm and Invertibility__

## Introduction

This article studies the norm form of the real algebra and the invertibility of its elements. It follows the basic algebra article *Real Algebra*, which defined $\mathbb{R}$ as the complete ordered field and as the one-dimensional real algebra carrying its single trivial involution. The goal here is to define the norm form and the Hermitian form, to establish the criterion for invertibility, to describe the group of units and its split into a positive scale and a two-element sign group, and to record the sign trichotomy $x > 0$, $x = 0$, $x < 0$. The real algebra is the one-dimensional member of the tensor family and the base case of the norm series; it collects the facts that the other members generalise, almost all of them by losing the definiteness that holds here.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked, and concrete instances appear only where a statement would otherwise be misread. Throughout, the basis is $e_0 = 1$, a general element is $x = x e_0$ with $x \in \mathbb{R}$, the sole involution is the identity $\operatorname{id}$, and the norm form is

$$
N(x) = x\,x = x^2 .
$$

The norm form of a biquaternion is written $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$, a complex-valued form, in *Biquaternion Norm and Invertibility*; here the same symbol is used for the real norm form $N(x) = x^2$, and the differences between the two are stated wherever they matter.

## The Norm Form

### Definition

The **norm form** of a real number $x$ is

$$
N(x) = x\,x = x^2 \in \mathbb{R}.
$$

**Basic properties.**

- $N(x)$ is a real number, and $N(x) \geq 0$ with equality if and only if $x = 0$. The norm form is **positive definite**.
- $N(x)$ is invariant under the involution: the involution is the identity, so $N(\operatorname{id} x) = N(x)$ holds trivially. There is no analogue here of the sign reversal $N(i\tilde{Q}) = -N(\tilde{Q})$ of the biquaternion algebra, because there is no central scalar imaginary separate from the algebra.
- $N$ is an even function, $N(-x) = (-x)^2 = x^2 = N(x)$.
- $N(x) = 0$ if and only if $x = 0$. There are no nonzero real numbers of vanishing norm form; equivalently, the algebra has no zero divisors.

The last point is the sharp difference from the biquaternion algebra, where the norm form is complex-valued and vanishes on a cone of nonzero elements. The difference from the complex algebra is only in the number of squares: $N(z) = a^2+b^2$ is a sum of two squares, and $N(x) = x^2$ is the single-square base case of that sum.

### Multiplicativity

**Theorem.** The norm form is multiplicative:

$$
N(xy) = N(x)\,N(y).
$$

**Proof.** By definition $N(xy) = (xy)^2$, and commutativity and associativity of the real product give $(xy)^2 = xyxy = x^2y^2 = N(x)N(y)$. $\square$

**Corollary.** If $N(x) \neq 0$ and $N(y) \neq 0$ then $N(xy) \neq 0$. Equivalently, the product of two units is a unit.

The multiplicativity is the formal identity $x^2y^2 = (xy)^2$ of any commutative ring, and it is used below to prove the invertibility criterion in one line, exactly as in the complex and biquaternion cases. It is also the source of the scale-and-sign decomposition: the norm form is the squared scale.

### The Modulus

The name "norm form" is not a misnomer here, in contrast with the biquaternion case. Define the **modulus**, or absolute value,

$$
|x| = \sqrt{N(x)} = \sqrt{x^2} \ \geq 0 .
$$

Then $|\cdot|$ satisfies the axioms of a norm on the one-dimensional real vector space $\mathbb{R}$:

- **Positive definiteness:** $|x| \geq 0$, and $|x| = 0$ if and only if $x = 0$.
- **Homogeneity:** $|\lambda x| = |\lambda|\,|x|$ for every $\lambda \in \mathbb{R}$.
- **Triangle inequality:** $|x + y| \leq |x| + |y|$.
- **Multiplicativity:** $|xy| = |x|\,|y|$, from the multiplicativity of the norm form.

The square root is a strictly non-negative real number with no sign choice and no branch choice, because $N(x) \geq 0$. The modulus is the **Euclidean norm** of the underlying one-dimensional real space, and the audit of the biquaternion semi-norm has no content here: the value is real, the vanishing locus is the origin alone, and the scaling axiom holds with a real scalar.

### The Norm Form from the Real Coordinate

Writing an element as $x = x e_0$ with coordinate $x \in \mathbb{R}$, the norm form is the single square

$$
N(x) = x^2 ,
$$

a positive-definite quadratic form on the coordinate space $\mathbb{R}^1$ of signature $(1,0)$. The one coordinate contributes with a positive sign. In the complex algebra the corresponding expression is the sum of two squares $a^2+b^2$, also of signature $(2,0)$, and in the biquaternion algebra it is the complex quadratic form $\sum_\mu Q_\mu^2$, whose restrictions to the two sectors carry opposite signatures. The real algebra has no second coordinate and no sector on which the sign reverses; the norm form is real and definite throughout.

## The Hermitian Form

### Definition

Because the sole involution of $\mathbb{R}$ is the identity, the **Hermitian form** of a real number $x$ is the same expression as the norm form,

$$
x\,x = x^2 .
$$

It is a real number, non-negative, and vanishes if and only if $x = 0$. The Hermitian form coincides with the norm form for the same reason it does in the complex algebra — the algebra is commutative and its involution is trivial — and the coincidence is even more complete here, since there is no second coefficient field over which the two could differ. In the biquaternion algebra the two objects separate: the Hermitian form $\tilde{Q}\tilde{Q}^\dagger$ is a biquaternion whose vector part need not vanish, and it carries information the norm form does not.

### The Euclidean Norm

The **Euclidean norm** of a real number is the square root of the Hermitian form,

$$
\|x\|_E = \sqrt{x\,x} = \sqrt{x^2} = |x| .
$$

It is a genuine norm on the real vector space $\mathbb{R} \cong \mathbb{R}^1$: positive-definite, subadditive, and homogeneous of degree one. It **is** multiplicative with respect to the real product, because $|xy| = |x||y|$. Here there is no distinction to draw between the Euclidean norm and the modulus, and the underlying real space $\mathbb{R}^1$ is the algebra itself.

### Relation Between the Norm Form and the Hermitian Form

The two forms are related as follows.

- The **norm form** $N(x) = x^2$ is real, positive-definite and multiplicative, and it vanishes only at the origin. It controls the multiplicative structure: invertibility, the group of units, and the scale (the modulus).
- The **Hermitian form** $x^2$ is the same expression. It controls the topological structure: the Euclidean norm, the metric topology of $\mathbb{R}$, and completeness.

The **inner product** on $\mathbb{R}$ as a real vector space is

$$
\langle x, y \rangle = x\,y = xy,
$$

symmetric and bilinear, with $\langle x, x \rangle = x^2 = N(x)$. It is real-valued, and its "imaginary part" is identically zero; the complex inner product $\langle z, w \rangle = \bar{z}w$ is complex-valued in general, and the biquaternion Hermitian form is not even scalar-valued. The real algebra is the case in which the inner product, the Hermitian form and the norm form are one and the same real-valued object, and this collapse is the degeneracy of the one-dimensional case.

## Invertibility

### Definition

A real number $x$ is **invertible** if there exists a real number $y$ such that

$$
x y = y x = e_0 = 1 .
$$

The element $y$, if it exists, is the **inverse** of $x$ and is denoted $x^{-1}$.

### Left and Right Inverses

In a general algebra the notions of left inverse, right inverse and two-sided inverse are distinct. In $\mathbb{R}$ they coincide, for two reasons: $\mathbb{R}$ is commutative, so a left inverse is automatically a right inverse, and $\mathbb{R}$ is finite-dimensional over $\mathbb{R}$, so a one-sided inverse in a finite-dimensional algebra over a field is two-sided. We may therefore speak of "the" inverse without ambiguity. The biquaternion algebra is finite-dimensional as well, so the three notions coincide there too; the distinction acquires content only outside the finite-dimensional setting, as in an endomorphism algebra of an infinite-dimensional space.

### Criterion for Invertibility

**Theorem.** A real number $x$ is invertible if and only if $x \neq 0$, equivalently if and only if $N(x) \neq 0$.

**Proof.** If $x \neq 0$ then $N(x) = x^2 > 0$, and the element

$$
y = \frac{x}{N(x)} = \frac{1}{x}
$$

satisfies $xy = x\cdot\frac{1}{x} = 1$, so $x$ has an inverse. Conversely, if $x$ is invertible then applying the norm form to $xy = 1$ and using multiplicativity gives $N(x)N(y) = N(1) = 1$, so $N(x) \neq 0$ and hence $x \neq 0$. $\square$

The criterion $N(x) \neq 0$ is the general form of the invertibility test of the family; in $\mathbb{R}$ it is equivalent to the elementary statement $x \neq 0$ because the norm form is definite. In the biquaternion algebra the two conditions differ, and $N(\tilde{Q}) = 0$ with $\tilde{Q} \neq 0$ is exactly the definition of a zero divisor.

### The Inverse Formula

For $x \neq 0$ the inverse is

$$
x^{-1} = \frac{1}{N(x)}\,x = \frac{1}{x}.
$$

**Proof.** The verification is the computation in the first part of the proof of the criterion. $\square$

**Corollary.** If $x$ is invertible then so is $-x$, and $(-x)^{-1} = -x^{-1}$. If $x$ is invertible then so is $x^{-1}$, and $(x^{-1})^{-1} = x$. Inversion reverses the order of a product, which in a commutative algebra is invisible: $(xy)^{-1} = y^{-1}x^{-1} = x^{-1}y^{-1}$.

## The Group of Units

### Definition

The **group of units** of $\mathbb{R}$ is the set of invertible elements:

$$
\mathbb{R}^\times = \{ x \in \mathbb{R} : N(x) \neq 0 \} = \mathbb{R} \setminus \{0\}.
$$

It is a group under multiplication with identity $e_0 = 1$.

### Basic Properties

- **Abelian.** Every two elements commute, because the algebra is commutative. The centre of $\mathbb{R}^\times$ is the whole group, as it is for $\mathbb{C}^\times$ and in contrast with $\mathbb{B}^\times \cong GL_2(\mathbb{C})$.
- **Open and dense.** $\mathbb{R}^\times$ is the complement of the single point $0$, hence open and dense in $\mathbb{R}$; its complement is the point $\{0\}$.
- **Disconnected, two components.** $\mathbb{R}^\times = \mathbb{R}_{>0} \cup \mathbb{R}_{<0}$ is the disjoint union of the positive and negative rays, so it has **two** connected components. This is the first structural difference from the complex case, where $\mathbb{C}^\times$ is connected; the two components of $\mathbb{R}^\times$ are the two elements of the sign group, dilated by the positive scale.
- **Non-compact.** $\mathbb{R}^\times$ is unbounded, hence not compact.
- **Infinite.** $\mathbb{R}^\times$ is uncountable and contains the infinite cyclic group of powers of any element other than $\pm1$.
- **Dimension.** As a real Lie group, $\mathbb{R}^\times$ has dimension $1$, its Lie algebra being $\mathbb{R}$ itself with the zero bracket; the sign group contributes dimension $0$.

The unit group is the base case of the family: below it lies only the non-unit $0$, and every nonzero element is a unit because the algebra is a field.

### The Split into Positive Scale and the Sign Group

**Theorem.** The map

$$
\mathbb{R}^\times \longrightarrow \mathbb{R}_{>0} \times \{\pm1\}, \qquad x \longmapsto \bigl( |x|, \operatorname{sgn} x \bigr),
$$

where $\operatorname{sgn} x = x/|x| \in \{\pm1\}$ for $x \neq 0$, is an isomorphism of groups and a homeomorphism of topological spaces onto the product of the positive ray and the two-element group.

**Proof.** The map is well defined because $|x| > 0$ for $x \neq 0$, and its image lies in $\mathbb{R}_{>0} \times \{\pm1\}$. It is a group homomorphism: $|xy| = |x||y|$ and $\operatorname{sgn}(xy) = \operatorname{sgn}x\,\operatorname{sgn}y$, since each is positive exactly when the two factors have the same sign. Its inverse is $(r, \sigma) \mapsto r\sigma$, continuous in the product topology, so the map is a homeomorphism. $\square$

The two factors are the **scale** $r = |x| \in \mathbb{R}_{>0}$, a positive real, and the **sign** $\sigma = \operatorname{sgn}x \in \{\pm1\}$. The group $\{\pm1\}$ is the two-element cyclic group, denoted $O(1)$ below when it is regarded as the orthogonal group of the line. The product form of this isomorphism is $x = |x|\operatorname{sgn}x$, the splitting of the unit group that the norm form supplies. In the complex case the second factor is the circle $U(1)$, a one-dimensional compact group, and it is connected; here it is a two-point discrete group, and the unit group is disconnected.

### The Inverse Map

The inversion map $\iota : \mathbb{R}^\times \to \mathbb{R}^\times$, $\iota(x) = x^{-1}$, is a smooth group automorphism of order two, and writing $x = r\sigma$ with $r = |x| > 0$ and $\sigma = \operatorname{sgn}x$ it reads

$$
\iota(r\sigma) = r^{-1}\sigma^{-1} = r^{-1}\sigma ,
$$

because $\sigma^{-1} = \sigma$ for $\sigma = \pm1$. Inversion therefore inverts the scale and fixes the sign, and its differential at the identity is $-\operatorname{id}$, the infinitesimal reason the Lie bracket of a commutative Lie algebra is antisymmetric. In the complex case inversion inverts the scale and conjugates the phase; here the sign is discrete and inversion fixes it.

## The Three-Way Classification

An element of a finite-dimensional real algebra of the tensor family is of one of three kinds: a unit, a zero divisor, or zero. The classes are read off from the norm form.

**Definition.** Let $x \in \mathbb{R}$. Then exactly one of the following holds:

- $N(x) > 0$: $x$ is a **unit**, i.e. an invertible element;
- $N(x) = 0$ and $x \neq 0$: $x$ is a **zero divisor**;
- $x = 0$: $x$ is **zero**.

**Theorem (the classification of $\mathbb{R}$).** The zero-divisor class is empty, so every nonzero real number is a unit and the classification has only two non-empty classes.

**Proof.** $N(x) = x^2 = 0$ forces $x = 0$ because the square of a real number is non-negative, so the only element of vanishing norm form is $0$. $\square$

### The Sign Trichotomy

The three-way classification refines, in the ordered case, to the **sign trichotomy**: every real number is positive, zero or negative, and the two nonzero cases are distinguished by the sign. This is the real analogue of the sign of the norm form in the higher members, but it is finer, because the order of $\mathbb{R}$ is total and gives a third class.

| class | sign | norm form | unit? | sign factor |
|---|---|---|---|---|
| $x > 0$ | $\operatorname{sgn}x = +1$ | $N(x) = x^2 > 0$ | yes | $+1$ |
| $x = 0$ | none | $N(x) = 0$ | no | undefined |
| $x < 0$ | $\operatorname{sgn}x = -1$ | $N(x) = x^2 > 0$ | yes | $-1$ |

The trichotomy is the statement that $\mathbb{R}$ is a **linearly ordered field**: the positive cone $\mathbb{R}_{>0}$ is closed under addition and multiplication, and $\mathbb{R}$ is its disjoint union with $\{0\}$ and $-\mathbb{R}_{>0}$. The sign group $\{\pm1\}$ is the multiplicative quotient $\mathbb{R}^\times/\mathbb{R}_{>0}$, the group of the two components.

### The Algebra Is a Division Algebra

The emptiness of the zero-divisor class is the statement that $\mathbb{R}$ is a **division algebra**: every nonzero element is invertible, and there are no $x, y \neq 0$ with $xy = 0$. By the Frobenius theorem, $\mathbb{R}$ is one of exactly three finite-dimensional associative real division algebras, the others being $\mathbb{C}$ and the quaternions $\mathbb{H}$, and it is the only one that is ordered. The three-way classification of the family is thus present here with its middle class empty; the biquaternion algebra has all three classes non-empty, its zero divisors being the nonzero points of the null cone $N(\tilde{Q}) = 0$.

## Distribution of the Invertible Elements

The invertible elements are distributed over the distinguished subspaces of $\mathbb{R}$ as follows. Since the only subspace is the whole algebra, the computation is immediate, and its content is the inversion-stability of the algebra.

### The Real Subspace

The real subspace $\mathbb{R}_{\mathbb{R}}$ of *Real Algebra* is the whole field, so every nonzero element $x$ is invertible and $x^{-1} = 1/x \in \mathbb{R}_{\mathbb{R}}$. Thus $\mathbb{R}_{\mathbb{R}} \setminus \{0\} = \mathbb{R}^\times$, and the algebra is inversion-stable.

### Summary of the Distribution

| subspace | nonzero elements | invertible | invertible elements not units |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{R}} = \mathbb{R}$ | all of $\mathbb{R} \setminus \{0\}$ | all | none |

There is no sector of the algebra carrying a zero divisor, and the distribution is uniform; $\mathbb{R}^\times = \mathbb{R}_{>0} \cup \mathbb{R}_{<0}$ is the union of the two signs. In the complex algebra the distribution is over the real and imaginary subspaces, in the quaternion algebra over the real line and the pure quaternion space, and in the biquaternion algebra over sectors that carry zero divisors as well as units; here the single subspace is the whole algebra, and the statement is the field property.

## The Relation to the Fixed-Point Decomposition

The sole involution of $\mathbb{R}$ is the identity, whose fixed subspace is the whole algebra. Writing $\mathbb{R}_{\mathbb{R}}$ for that fixed subspace, the decomposition is

$$
\mathbb{R} = \mathbb{R}_{\mathbb{R}} ,
$$

with no anti-fixed summand. On the single piece the norm form is definite, $N(x) = x^2 \geq 0$, and multiplying by an element preserves it:

$$
N(xy) = N(x)N(y).
$$

This is the degeneracy of the involution decomposition of the real field. In the complex algebra the involution splits $\mathbb{C} = \mathbb{R}_{\mathbb{C}} \oplus i\mathbb{R}_{\mathbb{C}}$ into two definite pieces of the same signature, and in the biquaternion algebra the Hermitian conjugation splits $\mathbb{B}$ into an eight-dimensional sum of a Hermitian and an anti-Hermitian subspace whose sectors carry opposite signatures, $(1,3)$ and $(3,1)$, with a sign reversal $N(i\tilde{Q}) = -N(\tilde{Q})$ for the central scalar imaginary. Here there is no second subspace, no central scalar imaginary and no sign reversal; the fixed-point decomposition collapses to its single summand, and the norm form and the Hermitian form collapse with it.

## The Base Case of the Norm Series

The norm series of the corpus records, for each algebra of the family, whether its norm form is real or complex, definite or indefinite, and what its vanishing locus is. In $\mathbb{R}$ the norm form is the single square $N(x) = x^2$, a real positive-definite quadratic form, and its vanishing locus is the single point $\{0\}$:

| algebra | norm form | value field | definite? | vanishing locus |
|---|---|---|---|---|
| $\mathbb{R}$ | $x^2$ | $\mathbb{R}$ | yes | $\{0\}$ |
| $\mathbb{C}$ | $a^2+b^2$ | $\mathbb{R}$ | yes | $\{0\}$ |
| $\mathbb{H}$ | $q_0^2+q_1^2+q_2^2+q_3^2$ | $\mathbb{R}$ | yes | $\{0\}$ |
| $\mathbb{B}$ | $\sum_\mu Q_\mu^2$ | $\mathbb{C}$ | no | the null cone |

The real case is the bottom of the definite column, the complex case adds the second square, the quaternion case adds the third and fourth, and the biquaternion case replaces the definite real form by an indefinite complex one. In every member the norm form is multiplicative; the real case is the least instance of that multiplicativity, $x^2y^2 = (xy)^2$.

## Comparison with the Complex and Quaternion Cases

The definite cases of the family, and the real case for contrast, are:

| algebra | norm form | definite? | zero divisors | group of units |
|---|---|---|---|---|
| $\mathbb{R}$ | $x^2$, real | yes | none | $\mathbb{R}^\times \cong \mathbb{R}_{>0} \times \{\pm1\}$ |
| $\mathbb{C}$ | $a^2+b^2$, real | yes | none | $\mathbb{C}^\times \cong \mathbb{R}_{>0} \times U(1)$ |
| $\mathbb{H}$ | $\sum_{k=0}^{3}q_k^2$, real | yes | none | $\mathbb{H}^\times \cong \mathbb{R}_{>0} \times S^3$ |
| $\mathbb{B}$ | $\sum_\mu Q_\mu^2$, complex | no | the null cone | $\mathbb{B}^\times \cong GL_2(\mathbb{C})$ |

The norm form is real and definite in $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, and all three are division algebras; the norm form is complex and indefinite in $\mathbb{B}$, which has zero divisors. The unit group is compact modulo the non-compact scale in $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, and genuinely non-compact in the biquaternion case. The real algebra sits at the bottom of the definite column: the complex case replaces the sign group $O(1)$ by the circle $U(1)$ and thereby connects the two components of the unit group into one, the quaternion case replaces the circle by the three-sphere $S^3$, and the biquaternion case replaces the definite norm form by a complex one and the group of units by $GL_2(\mathbb{C})$.

## Summary

The norm form of a real number is $N(x) = x^2$, real, positive-definite and multiplicative, $N(xy) = N(x)N(y)$; it vanishes only at the origin. The Hermitian form is the same expression, so the norm form and the Hermitian form coincide, and the Euclidean norm $|x| = \sqrt{N(x)}$ is a genuine norm that is multiplicative. This is the degeneracy of the one-dimensional case.

A real number is invertible if and only if it is nonzero, equivalently if and only if its norm form is nonzero, and the inverse is $x^{-1} = x/N(x) = 1/x$. The zero-divisor class is empty, so $\mathbb{R}$ is a division algebra by the Frobenius theorem, and the single distinguished subspace, the whole field, consists entirely of units together with zero.

The group of units is $\mathbb{R}^\times = \mathbb{R}\setminus\{0\}$, abelian, open, dense, disconnected and non-compact, and it splits as $\mathbb{R}^\times \cong \mathbb{R}_{>0} \times \{\pm1\}$ into a positive scale and a sign, $x = |x|\operatorname{sgn}x$. The norm form is definite on the whole algebra, and the sign trichotomy $x > 0$, $x = 0$, $x < 0$ refines the three-way classification; the only element of vanishing norm form is the origin, which is why the real algebra is the definite base case of the family.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}$ | the real algebra, the complete ordered field, basis $e_0 = 1$ |
| $x = x e_0$ | a real number, $x$ its coordinate |
| $\operatorname{id}$ | the identity involution, the sole involution of $\mathbb{R}$ |
| $N(x) = x\,x = x^2$ | the norm form, real, positive definite, multiplicative |
| $\lvert x\rvert = \sqrt{N(x)} = \sqrt{x^2}$ | the modulus, the Euclidean norm |
| $\langle x, y \rangle = xy$ | the real inner product, $\langle x, x \rangle = N(x)$ |
| $\operatorname{sgn} x = x/\lvert x\rvert$ | the sign of a nonzero $x$, an element of $\{\pm1\}$ |
| $\mathbb{R}^\times = \mathbb{R}\setminus\{0\}$ | the group of units |
| $\mathbb{R}_{>0}, \mathbb{R}_{<0}$ | the positive and negative rays, the two components of $\mathbb{R}^\times$ |
| $\{\pm1\} \cong O(1)$ | the sign group, the two-element cyclic group |
| $x = \lvert x\rvert\operatorname{sgn}x$ | the sign decomposition, $r = \lvert x\rvert \in \mathbb{R}_{>0}$, $\sigma = \operatorname{sgn}x$ |
| $x^{-1} = x/N(x) = 1/x$ | the inverse of a nonzero element |
| $\mathbb{R}_{\mathbb{R}}$ | the fixed subspace of the identity involution, all of $\mathbb{R}$ |

## Further Reading

- Edmund Landau, *Grundlagen der Analysis* (Akademische Verlagsgesellschaft, 1930), for the ordered-field axioms and the uniqueness of $\mathbb{R}$.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for inverses, the group of units and the Frobenius theorem.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for norm forms and invertibility in finite-dimensional algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of the real division algebras and the place of $\mathbb{R}$ among them.
- Walter Rudin, *Principles of Mathematical Analysis*, 3rd edition (McGraw-Hill, 1976), for the absolute value, the modulus and the metric structure of the line.
- Serge Lang, *Algebra*, 3rd edition (Addison–Wesley, 1993), for ordered fields, the sign of an element and the positive cone.
