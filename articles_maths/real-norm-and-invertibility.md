
# __Real Norm and Invertibility__

## Introduction

This article studies the norm of the real algebra and the invertibility of its elements. It follows the basic algebra article *Real Algebra*, which defined $\mathbb{R}$ as the complete ordered field and as the one-dimensional real algebra carrying its single trivial involution. The goal here is to define the norm and the Hermitian form, to establish the criterion for invertibility, to describe the group of units and its split into a positive scale and a two-element sign group, and to record the sign trichotomy $q > 0$, $q = 0$, $q < 0$. The real algebra is the one-dimensional member of the tensor family and the base case of the norm series; it collects the facts that the other members generalise, almost all of them by losing the definiteness that holds here.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked, and concrete instances appear only where a statement would otherwise be misread. Throughout, the basis is $e_t = 1$, a general element is $q = q e_t$ with $q \in \mathbb{R}$, the sole involution is the identity $\operatorname{id}$, and the norm is

$$
\langle q\rangle = q\,q = q^2 .
$$

The same symbol $\langle\cdot\rangle$ is used for the real norm $\langle q\rangle = q^2$ throughout.

## The Norm

### Definition

The **norm** of a real number $q$ is

$$
\langle q\rangle = q\,q = q^2 \in \mathbb{R}.
$$

**Basic properties.**

- $\langle q\rangle$ is a real number, and $\langle q\rangle \geq 0$ with equality if and only if $q = 0$. The norm is **positive definite**.
- $\langle q\rangle$ is invariant under the involution: the involution is the identity, so $\langle \operatorname{id} q\rangle = \langle q\rangle$ holds trivially. There is no central scalar imaginary separate from the algebra.
- $\langle\cdot\rangle$ is an even function, $\langle -q\rangle = (-q)^2 = q^2 = \langle q\rangle$.
- $\langle q\rangle = 0$ if and only if $q = 0$. There are no nonzero real numbers of vanishing norm; equivalently, the algebra has no zero divisors.

The difference from the complex algebra is only in the number of squares: $\langle A\rangle = u^2+v^2$ is a sum of two squares, and $\langle q\rangle = q^2$ is the single-square base case of that sum.

### Multiplicativity

**Theorem.** The norm is multiplicative:

$$
\langle q_1 q_2\rangle = \langle q_1\rangle\,\langle q_2\rangle.
$$

**Proof.** By definition $\langle q_1 q_2\rangle = (q_1 q_2)^2$, and commutativity and associativity of the real product give $(q_1 q_2)^2 = q_1 q_2 q_1 q_2 = q_1^2 q_2^2 = \langle q_1\rangle\langle q_2\rangle$.

**Corollary.** If $\langle q_1\rangle \neq 0$ and $\langle q_2\rangle \neq 0$ then $\langle q_1 q_2\rangle \neq 0$. Equivalently, the product of two units is a unit.

The multiplicativity is the formal identity $q_1^2 q_2^2 = (q_1 q_2)^2$ of any commutative ring, and it is used below to prove the invertibility criterion in one line, exactly as in the complex case. It is also the source of the scale-and-sign decomposition: the norm is the squared scale.

### The Modulus

The name "norm" is not a misnomer here. Define the **modulus**, or absolute value,

$$
|q| = \sqrt{\langle q\rangle} = \sqrt{q^2} \ \geq 0 .
$$

Then $|\cdot|$ satisfies the axioms of a norm on the one-dimensional real vector space $\mathbb{R}$:

- **Positive definiteness:** $|q| \geq 0$, and $|q| = 0$ if and only if $q = 0$.
- **Homogeneity:** $|\lambda q| = |\lambda|\,|q|$ for every $\lambda \in \mathbb{R}$.
- **Triangle inequality:** $|q_1 + q_2| \leq |q_1| + |q_2|$.
- **Multiplicativity:** $|q_1 q_2| = |q_1|\,|q_2|$, from the multiplicativity of the norm.

The square root is a strictly non-negative real number with no sign choice and no branch choice, because $\langle q\rangle \geq 0$. The modulus is the **Euclidean norm** of the underlying one-dimensional real space, and the audit of the semi-norm has no content here: the value is real, the vanishing locus is the origin alone, and the scaling axiom holds with a real scalar.

### The Norm from the Real Coordinate

Writing an element as $q = q e_t$ with coordinate $q \in \mathbb{R}$, the norm is the single square

$$
\langle q\rangle = q^2 ,
$$

a positive-definite quadratic form on the coordinate space $\mathbb{R}^1$ of signature $(1,0)$. The one coordinate contributes with a positive sign. In the complex algebra the corresponding expression is the sum of two squares $u^2+v^2$, also of signature $(2,0)$. The real algebra has no second coordinate and no sector on which the sign reverses; the norm is real and definite throughout.

## The Hermitian Form

### Definition

Because the sole involution of $\mathbb{R}$ is the identity, the **Hermitian form** of a real number $q$ is the same expression as the norm,

$$
q\,q = q^2 .
$$

It is a real number, non-negative, and vanishes if and only if $q = 0$. The Hermitian form coincides with the norm for the same reason it does in the complex algebra — the algebra is commutative and its involution is trivial — and the coincidence is even more complete here, since there is no second coefficient field over which the two could differ.

### The Euclidean Norm

The **Euclidean norm** of a real number is the square root of the Hermitian form,

$$
\|q\|_E = \sqrt{q\,q} = \sqrt{q^2} = |q| .
$$

It is a genuine norm on the real vector space $\mathbb{R} \cong \mathbb{R}^1$: positive-definite, subadditive, and homogeneous of degree one. It **is** multiplicative with respect to the real product, because $|q_1 q_2| = |q_1||q_2|$. Here there is no distinction to draw between the Euclidean norm and the modulus, and the underlying real space $\mathbb{R}^1$ is the algebra itself.

### Relation Between the Norm and the Hermitian Form

The two forms are related as follows.

- The **norm** $\langle q\rangle = q^2$ is real, positive-definite and multiplicative, and it vanishes only at the origin. It controls the multiplicative structure: invertibility, the group of units, and the scale (the modulus).
- The **Hermitian form** $q^2$ is the same expression. It controls the topological structure: the Euclidean norm, the metric topology of $\mathbb{R}$, and completeness.

The **inner product** on $\mathbb{R}$ as a real vector space is

$$
\langle q_1, q_2 \rangle = q_1\,q_2 = q_1 q_2,
$$

symmetric and bilinear, with $\langle q_1, q_1 \rangle = q_1^2 = \langle q_1\rangle$. It is real-valued, and its "imaginary part" is identically zero; the complex inner product $\langle c, w \rangle = \bar{c}w$ is complex-valued in general. The real algebra is the case in which the inner product, the Hermitian form and the norm are one and the same real-valued object, and this collapse is the degeneracy of the one-dimensional case.

## Invertibility

### Definition

A real number $q$ is **invertible** if there exists a real number $q_1$ such that

$$
q q_1 = q_1 q = e_t = 1 .
$$

The element $q_1$, if it exists, is the **inverse** of $q$ and is denoted $q^{-1}$.

### Left and Right Inverses

In a general algebra the notions of left inverse, right inverse and two-sided inverse are distinct. In $\mathbb{R}$ they coincide, for two reasons: $\mathbb{R}$ is commutative, so a left inverse is automatically a right inverse, and $\mathbb{R}$ is finite-dimensional over $\mathbb{R}$, so a one-sided inverse in a finite-dimensional algebra over a field is two-sided. We may therefore speak of "the" inverse without ambiguity. The distinction acquires content only outside the finite-dimensional setting, as in an endomorphism algebra of an infinite-dimensional space.

### Criterion for Invertibility

**Theorem.** A real number $q$ is invertible if and only if $q \neq 0$, equivalently if and only if $\langle q\rangle \neq 0$.

**Proof.** If $q \neq 0$ then $\langle q\rangle = q^2 > 0$, and the element

$$
q_1 = \frac{q}{\langle q\rangle} = \frac{1}{q}
$$

satisfies $q q_1 = q\cdot\frac{1}{q} = 1$, so $q$ has an inverse. Conversely, if $q$ is invertible then applying the norm to $q q_1 = 1$ and using multiplicativity gives $\langle q\rangle\langle q_1\rangle = \langle 1\rangle = 1$, so $\langle q\rangle \neq 0$ and hence $q \neq 0$.

The criterion $\langle q\rangle \neq 0$ is the general form of the invertibility test of the family; in $\mathbb{R}$ it is equivalent to the elementary statement $q \neq 0$ because the norm is definite.

### The Inverse Formula

For $q \neq 0$ the inverse is

$$
q^{-1} = \frac{1}{\langle q\rangle}\,q = \frac{1}{q}.
$$

**Proof.** The verification is the computation in the first part of the proof of the criterion.

**Corollary.** If $q$ is invertible then so is $-q$, and $(-q)^{-1} = -q^{-1}$. If $q$ is invertible then so is $q^{-1}$, and $(q^{-1})^{-1} = q$. Inversion reverses the order of a product, which in a commutative algebra is invisible: $(q_1 q_2)^{-1} = q_2^{-1}q_1^{-1} = q_1^{-1}q_2^{-1}$.

### Worked Examples

On the elements $q_1 = -\tfrac{3}{4}$ and $q_2 = \tfrac{7}{2}$, both nonzero and therefore units,

$$
q_1^{-1} = \frac{q_1}{q_1^2} = \frac{-\tfrac{3}{4}}{\tfrac{9}{16}} = -\tfrac{4}{3}, \qquad
q_2^{-1} = \frac{q_2}{q_2^2} = \frac{\tfrac{7}{2}}{\tfrac{49}{4}} = \tfrac{2}{7},
$$

with the exact verifications $q_1\,q_1^{-1} = 1$ and $q_2\,q_2^{-1} = 1$; the element $0$ has $\langle 0\rangle = 0$ and is the only non-unit.

| element | $\langle\cdot\rangle$ | unit? | inverse |
|---|---|---|---|
| $q_1 = -\tfrac{3}{4}$ | $\tfrac{9}{16}$ | yes | $-\tfrac{4}{3}$ |
| $q_2 = \tfrac{7}{2}$ | $\tfrac{49}{4}$ | yes | $\tfrac{2}{7}$ |
| $0$ | $0$ | no | — |

## The Group of Units

### Definition

The **group of units** of $\mathbb{R}$ is the set of invertible elements:

$$
\mathbb{R}^\times = \{ q \in \mathbb{R} : \langle q\rangle \neq 0 \} = \mathbb{R} \setminus \{0\}.
$$

It is a group under multiplication with identity $e_t = 1$.

### Basic Properties

- **Abelian.** Every two elements commute, because the algebra is commutative. The centre of $\mathbb{R}^\times$ is the whole group, as it is for $\mathbb{C}^\times$.
- **Open and dense.** $\mathbb{R}^\times$ is the complement of the single point $0$, hence open and dense in $\mathbb{R}$; its complement is the point $\{0\}$.
- **Disconnected, two components.** $\mathbb{R}^\times = \mathbb{R}_{>0} \cup \mathbb{R}_{<0}$ is the disjoint union of the positive and negative rays, so it has **two** connected components. This is the first structural difference from the complex case, where $\mathbb{C}^\times$ is connected; the two components of $\mathbb{R}^\times$ are the two elements of the sign group, dilated by the positive scale.
- **Non-compact.** $\mathbb{R}^\times$ is unbounded, hence not compact.
- **Infinite.** $\mathbb{R}^\times$ is uncountable and contains the infinite cyclic group of powers of any element other than $\pm1$.
- **Dimension.** As a topological group the units are one-dimensional, the positive ray contributing the one dimension and the sign group the zero-dimensional factor; the Lie structure of the group is the analytic content of *Real Exponential and Lie Group Structure*.

The unit group is the base case of the family: below it lies only the non-unit $0$, and every nonzero element is a unit because the algebra is a field.

### The Split into Positive Scale and the Sign Group

**Theorem.** The map

$$
\mathbb{R}^\times \longrightarrow \mathbb{R}_{>0} \times \{\pm1\}, \qquad q \longmapsto \bigl( |q|, \operatorname{sgn} q \bigr),
$$

where $\operatorname{sgn} q = q/|q| \in \{\pm1\}$ for $q \neq 0$, is an isomorphism of groups and a homeomorphism of topological spaces onto the product of the positive ray and the two-element group.

**Proof.** The map is well defined because $|q| > 0$ for $q \neq 0$, and its image lies in $\mathbb{R}_{>0} \times \{\pm1\}$. It is a group homomorphism: $|q_1 q_2| = |q_1||q_2|$ and $\operatorname{sgn}(q_1 q_2) = \operatorname{sgn}q_1\,\operatorname{sgn}q_2$, since each is positive exactly when the two factors have the same sign. Its inverse is $(r, \sigma) \mapsto r\sigma$, continuous in the product topology, so the map is a homeomorphism.

The two factors are the **scale** $r = |q| \in \mathbb{R}_{>0}$, a positive real, and the **sign** $\sigma = \operatorname{sgn}q \in \{\pm1\}$. The group $\{\pm1\}$ is the two-element cyclic group, denoted $O(1)$ below when it is regarded as the orthogonal group of the line. The product form of this isomorphism is $q = |q|\operatorname{sgn}q$, the splitting of the unit group that the norm supplies. In the complex case the second factor is the circle $\mathrm{U}(1)$, a one-dimensional compact group, and it is connected; here it is a two-point discrete group, and the unit group is disconnected.

### The Inverse Map

The inversion map $\iota : \mathbb{R}^\times \to \mathbb{R}^\times$, $\iota(q) = q^{-1}$, is a group automorphism of order two, and writing $q = r\sigma$ with $r = |q| > 0$ and $\sigma = \operatorname{sgn}q$ it reads

$$
\iota(r\sigma) = r^{-1}\sigma^{-1} = r^{-1}\sigma ,
$$

because $\sigma^{-1} = \sigma$ for $\sigma = \pm1$. Inversion therefore inverts the scale and fixes the sign. The smoothness of the operation and its differential at the identity are Lie-group data, and they are analytic: they belong to *Real Exponential and Lie Group Structure*, the analytic article of this category, and are named here only. In the complex case inversion inverts the scale and conjugates the phase; here the sign is discrete and inversion fixes it.

## The Three-Way Classification

An element of a finite-dimensional real algebra of the tensor family is of one of three kinds: a unit, a zero divisor, or zero. The classes are read off from the norm.

**Definition.** Let $q \in \mathbb{R}$. Then exactly one of the following holds:

- $\langle q\rangle > 0$: $q$ is a **unit**, i.e. an invertible element;
- $\langle q\rangle = 0$ and $q \neq 0$: $q$ is a **zero divisor**;
- $q = 0$: $q$ is **zero**.

**Theorem (the classification of $\mathbb{R}$).** The zero-divisor class is empty, so every nonzero real number is a unit and the classification has only two non-empty classes.

**Proof.** $\langle q\rangle = q^2 = 0$ forces $q = 0$ because the square of a real number is non-negative, so the only element of vanishing norm is $0$.

### The Sign Trichotomy

The three-way classification refines, in the ordered case, to the **sign trichotomy**: every real number is positive, zero or negative, and the two nonzero cases are distinguished by the sign. This is the real analogue of the sign of the norm in the higher members, but it is finer, because the order of $\mathbb{R}$ is total and gives a third class.

| class | sign | norm | unit? | sign factor |
|---|---|---|---|---|
| $q > 0$ | $\operatorname{sgn}q = +1$ | $\langle q\rangle = q^2 > 0$ | yes | $+1$ |
| $q = 0$ | none | $\langle q\rangle = 0$ | no | undefined |
| $q < 0$ | $\operatorname{sgn}q = -1$ | $\langle q\rangle = q^2 > 0$ | yes | $-1$ |

The trichotomy is the statement that $\mathbb{R}$ is a **linearly ordered field**: the positive cone $\mathbb{R}_{>0}$ is closed under addition and multiplication, and $\mathbb{R}$ is its disjoint union with $\{0\}$ and $-\mathbb{R}_{>0}$. The sign group $\{\pm1\}$ is the multiplicative quotient $\mathbb{R}^\times/\mathbb{R}_{>0}$, the group of the two components.

### The Algebra Is a Division Algebra

The emptiness of the zero-divisor class is the statement that $\mathbb{R}$ is a **division algebra**: every nonzero element is invertible, and there are no $q_1, q_2 \neq 0$ with $q_1 q_2 = 0$. By the Frobenius theorem, $\mathbb{R}$ is the only finite-dimensional associative real division algebra that is ordered.

## Distribution of the Invertible Elements

The invertible elements are distributed over the distinguished subspaces of $\mathbb{R}$ as follows. Since the only subspace is the whole algebra, the computation is immediate, and its content is the inversion-stability of the algebra.

### The Real Subspace

The real subspace $\mathbb{R}_{\mathbb{R}}$ of *Real Algebra* is the whole field, so every nonzero element $q$ is invertible and $q^{-1} = 1/q \in \mathbb{R}_{\mathbb{R}}$. Thus $\mathbb{R}_{\mathbb{R}} \setminus \{0\} = \mathbb{R}^\times$, and the algebra is inversion-stable.

### Summary of the Distribution

| subspace | nonzero elements | invertible | invertible elements not units |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{R}} = \mathbb{R}$ | all of $\mathbb{R} \setminus \{0\}$ | all | none |

There is no sector of the algebra carrying a zero divisor, and the distribution is uniform; $\mathbb{R}^\times = \mathbb{R}_{>0} \cup \mathbb{R}_{<0}$ is the union of the two signs. In the complex algebra the distribution is over the real and imaginary subspaces; here the single subspace is the whole algebra, and the statement is the field property.

## The Relation to the Fixed-Point Decomposition

The sole involution of $\mathbb{R}$ is the identity, whose fixed subspace is the whole algebra. Writing $\mathbb{R}_{\mathbb{R}}$ for that fixed subspace, the decomposition is

$$
\mathbb{R} = \mathbb{R}_{\mathbb{R}} ,
$$

with no anti-fixed summand. On the single piece the norm is definite, $\langle q\rangle = q^2 \geq 0$, and multiplying by an element preserves it:

$$
\langle q_1 q_2\rangle = \langle q_1\rangle\langle q_2\rangle.
$$

This is the degeneracy of the involution decomposition of the real field. In the complex algebra the involution splits $\mathbb{C} = \mathbb{R}_{\mathbb{C}} \oplus i\mathbb{R}_{\mathbb{C}}$ into two definite pieces of the same signature. Here there is no second subspace, no central scalar imaginary and no sign reversal; the fixed-point decomposition collapses to its single summand, and the norm and the Hermitian form collapse with it.

## The Base Case of the Norm Series

The norm series of the corpus records, for each algebra of the family, whether its norm is real or complex, definite or indefinite, and what its vanishing locus is. In $\mathbb{R}$ the norm is the single square $\langle q\rangle = q^2$, a real positive-definite quadratic form, and its vanishing locus is the single point $\{0\}$:

| algebra | norm | value field | definite? | vanishing locus |
|---|---|---|---|---|
| $\mathbb{R}$ | $q^2$ | $\mathbb{R}$ | yes | $\{0\}$ |
| $\mathbb{C}$ | $u^2+v^2$ | $\mathbb{R}$ | yes | $\{0\}$ |

The real case is the bottom of the definite column, and the complex case adds the second square. In every member the norm is multiplicative; the real case is the least instance of that multiplicativity, $q_1^2 q_2^2 = (q_1 q_2)^2$.

## Comparison with the Complex Case

The definite cases of the family, and the real case for contrast, are:

| algebra | norm | definite? | zero divisors | group of units |
|---|---|---|---|---|
| $\mathbb{R}$ | $q^2$, real | yes | none | $\mathbb{R}^\times \cong \mathbb{R}_{>0} \times \{\pm1\}$ |
| $\mathbb{C}$ | $u^2+v^2$, real | yes | none | $\mathbb{C}^\times \cong \mathbb{R}_{>0} \times \mathrm{U}(1)$ |

The norm is real and definite in $\mathbb{R}$ and $\mathbb{C}$, and both are division algebras. The unit group is compact modulo the non-compact scale in $\mathbb{R}$ and $\mathbb{C}$. The real algebra sits at the bottom of the definite column: the complex case replaces the sign group $O(1)$ by the circle $\mathrm{U}(1)$ and thereby connects the two components of the unit group into one.

## Summary

The norm of a real number is $\langle q\rangle = q^2$, real, positive-definite and multiplicative, $\langle q_1 q_2\rangle = \langle q_1\rangle\langle q_2\rangle$; it vanishes only at the origin. The Hermitian form is the same expression, so the norm and the Hermitian form coincide, and the Euclidean norm $|q| = \sqrt{\langle q\rangle}$ is a genuine norm that is multiplicative. This is the degeneracy of the one-dimensional case.

A real number is invertible if and only if it is nonzero, equivalently if and only if its norm is nonzero, and the inverse is $q^{-1} = q/\langle q\rangle = 1/q$. The zero-divisor class is empty, so $\mathbb{R}$ is a division algebra by the Frobenius theorem, and the single distinguished subspace, the whole field, consists entirely of units together with zero.

The group of units is $\mathbb{R}^\times = \mathbb{R}\setminus\{0\}$, abelian, open, dense, disconnected and non-compact, and it splits as $\mathbb{R}^\times \cong \mathbb{R}_{>0} \times \{\pm1\}$ into a positive scale and a sign, $q = |q|\operatorname{sgn}q$. The norm is definite on the whole algebra, and the sign trichotomy $q > 0$, $q = 0$, $q < 0$ refines the three-way classification; the only element of vanishing norm is the origin, which is why the real algebra is the definite base case of the family.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}$ | the real algebra, the complete ordered field, basis $e_t = 1$ |
| $q = q e_t$ | a real number, $q$ its coordinate |
| $\operatorname{id}$ | the identity involution, the sole involution of $\mathbb{R}$ |
| $\langle q\rangle = q\,q = q^2$ | the norm, real, positive definite, multiplicative |
| $\lvert q\rvert = \sqrt{\langle q\rangle} = \sqrt{q^2}$ | the modulus, the Euclidean norm |
| $\langle q_1, q_2 \rangle = q_1 q_2$ | the real inner product, $\langle q_1, q_1 \rangle = \langle q_1\rangle$ |
| $\operatorname{sgn} q = q/\lvert q\rvert$ | the sign of a nonzero $q$, an element of $\{\pm1\}$ |
| $\mathbb{R}^\times = \mathbb{R}\setminus\{0\}$ | the group of units |
| $\mathbb{R}_{>0}, \mathbb{R}_{<0}$ | the positive and negative rays, the two components of $\mathbb{R}^\times$ |
| $\{\pm1\} \cong O(1)$ | the sign group, the two-element cyclic group |
| $q = \lvert q\rvert\operatorname{sgn}q$ | the sign decomposition, $r = \lvert q\rvert \in \mathbb{R}_{>0}$, $\sigma = \operatorname{sgn}q$ |
| $q^{-1} = q/\langle q\rangle = 1/q$ | the inverse of a nonzero element |
| $\mathbb{R}_{\mathbb{R}}$ | the fixed subspace of the identity involution, all of $\mathbb{R}$ |

## Further Reading

- Edmund Landau, *Grundlagen der Analysis* (Akademische Verlagsgesellschaft, 1930), for the ordered-field axioms and the uniqueness of $\mathbb{R}$.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for inverses, the group of units and the Frobenius theorem.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for norms and invertibility in finite-dimensional algebras.
- Walter Rudin, *Principles of Mathematical Analysis*, 3rd edition (McGraw-Hill, 1976), for the absolute value, the modulus and the metric structure of the line.
- Serge Lang, *Algebra*, 3rd edition (Addison–Wesley, 1993), for ordered fields, the sign of an element and the positive cone.
