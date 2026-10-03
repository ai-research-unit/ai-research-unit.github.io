
# __Real Norm and Invertibility__

## Introduction

This article studies the norm of the real algebra and the invertibility of its elements. It follows the basic algebra article *Real Algebra*, which defined $\mathbb{R}$ as the complete ordered field and as the one-dimensional real algebra carrying its single trivial involution. The goal here is to define the norm and the Hermitian form, to establish the criterion for invertibility, to describe the group of units and its split into a positive scale and a two-element sign group, and to record the sign trichotomy $a > 0$, $a = 0$, $a < 0$. The real algebra is the one-dimensional member of the tensor family and the base case of the norm series; it collects the facts that the other members generalise, almost all of them by losing the definiteness that holds here.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked, and concrete instances appear only where a statement would otherwise be misread. Throughout, the basis is $e_0 = 1$, a general element is $a = a e_0$ with $a \in \mathbb{R}$, the sole involution is the identity $\operatorname{id}$, and the norm is

$$
N(a) = a\,a = a^2 .
$$

The norm of a biquaternion is written $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural}$, a complex-valued form, in *Biquaternion Norm and Invertibility*; here the same symbol is used for the real norm $N(a) = a^2$, and the differences between the two are stated wherever they matter.

## The Norm

### Definition

The **norm** of a real number $a$ is

$$
N(a) = a\,a = a^2 \in \mathbb{R}.
$$

**Basic properties.**

- $N(a)$ is a real number, and $N(a) \geq 0$ with equality if and only if $a = 0$. The norm is **positive definite**.
- $N(a)$ is invariant under the involution: the involution is the identity, so $N(\operatorname{id} a) = N(a)$ holds trivially. There is no analogue here of the sign reversal $N(i\tilde{Q}) = -N(\tilde{Q})$ of the biquaternion algebra, because there is no central scalar imaginary separate from the algebra.
- $N$ is an even function, $N(-a) = (-a)^2 = a^2 = N(a)$.
- $N(a) = 0$ if and only if $a = 0$. There are no nonzero real numbers of vanishing norm; equivalently, the algebra has no zero divisors.

The last point is the sharp difference from the biquaternion algebra, where the norm is complex-valued and vanishes on a cone of nonzero elements. The difference from the complex algebra is only in the number of squares: $N(A) = u^2+v^2$ is a sum of two squares, and $N(a) = a^2$ is the single-square base case of that sum.

### Multiplicativity

**Theorem.** The norm is multiplicative:

$$
N(ab) = N(a)\,N(b).
$$

**Proof.** By definition $N(ab) = (ab)^2$, and commutativity and associativity of the real product give $(ab)^2 = abab = a^2b^2 = N(a)N(b)$.

**Corollary.** If $N(a) \neq 0$ and $N(b) \neq 0$ then $N(ab) \neq 0$. Equivalently, the product of two units is a unit.

The multiplicativity is the formal identity $a^2b^2 = (ab)^2$ of any commutative ring, and it is used below to prove the invertibility criterion in one line, exactly as in the complex and biquaternion cases. It is also the source of the scale-and-sign decomposition: the norm is the squared scale.

### The Modulus

The name "norm" is not a misnomer here, in contrast with the biquaternion case. Define the **modulus**, or absolute value,

$$
|a| = \sqrt{N(a)} = \sqrt{a^2} \ \geq 0 .
$$

Then $|\cdot|$ satisfies the axioms of a norm on the one-dimensional real vector space $\mathbb{R}$:

- **Positive definiteness:** $|a| \geq 0$, and $|a| = 0$ if and only if $a = 0$.
- **Homogeneity:** $|\lambda a| = |\lambda|\,|a|$ for every $\lambda \in \mathbb{R}$.
- **Triangle inequality:** $|a + b| \leq |a| + |b|$.
- **Multiplicativity:** $|ab| = |a|\,|b|$, from the multiplicativity of the norm.

The square root is a strictly non-negative real number with no sign choice and no branch choice, because $N(a) \geq 0$. The modulus is the **Euclidean norm** of the underlying one-dimensional real space, and the audit of the biquaternion semi-norm has no content here: the value is real, the vanishing locus is the origin alone, and the scaling axiom holds with a real scalar.

### The Norm from the Real Coordinate

Writing an element as $a = a e_0$ with coordinate $a \in \mathbb{R}$, the norm is the single square

$$
N(a) = a^2 ,
$$

a positive-definite quadratic form on the coordinate space $\mathbb{R}^1$ of signature $(1,0)$. The one coordinate contributes with a positive sign. In the complex algebra the corresponding expression is the sum of two squares $u^2+v^2$, also of signature $(2,0)$, and in the biquaternion algebra it is the complex quadratic form $\sum_\mu Q_\mu^2$, whose restrictions to the two sectors carry opposite signatures. The real algebra has no second coordinate and no sector on which the sign reverses; the norm is real and definite throughout.

## The Hermitian Form

### Definition

Because the sole involution of $\mathbb{R}$ is the identity, the **Hermitian form** of a real number $a$ is the same expression as the norm,

$$
a\,a = a^2 .
$$

It is a real number, non-negative, and vanishes if and only if $a = 0$. The Hermitian form coincides with the norm for the same reason it does in the complex algebra — the algebra is commutative and its involution is trivial — and the coincidence is even more complete here, since there is no second coefficient field over which the two could differ. In the biquaternion algebra the two objects separate: the Hermitian form $\tilde{Q}\tilde{Q}^{*}$ is a biquaternion whose vector part need not vanish, and it carries information the norm does not.

### The Euclidean Norm

The **Euclidean norm** of a real number is the square root of the Hermitian form,

$$
\|a\|_E = \sqrt{a\,a} = \sqrt{a^2} = |a| .
$$

It is a genuine norm on the real vector space $\mathbb{R} \cong \mathbb{R}^1$: positive-definite, subadditive, and homogeneous of degree one. It **is** multiplicative with respect to the real product, because $|ab| = |a||b|$. Here there is no distinction to draw between the Euclidean norm and the modulus, and the underlying real space $\mathbb{R}^1$ is the algebra itself.

### Relation Between the Norm and the Hermitian Form

The two forms are related as follows.

- The **norm** $N(a) = a^2$ is real, positive-definite and multiplicative, and it vanishes only at the origin. It controls the multiplicative structure: invertibility, the group of units, and the scale (the modulus).
- The **Hermitian form** $a^2$ is the same expression. It controls the topological structure: the Euclidean norm, the metric topology of $\mathbb{R}$, and completeness.

The **inner product** on $\mathbb{R}$ as a real vector space is

$$
\langle a, b \rangle = a\,b = ab,
$$

symmetric and bilinear, with $\langle a, a \rangle = a^2 = N(a)$. It is real-valued, and its "imaginary part" is identically zero; the complex inner product $\langle c, w \rangle = \bar{c}w$ is complex-valued in general, and the biquaternion Hermitian form is not even scalar-valued. The real algebra is the case in which the inner product, the Hermitian form and the norm are one and the same real-valued object, and this collapse is the degeneracy of the one-dimensional case.

## Invertibility

### Definition

A real number $a$ is **invertible** if there exists a real number $b$ such that

$$
a b = b a = e_0 = 1 .
$$

The element $b$, if it exists, is the **inverse** of $a$ and is denoted $a^{-1}$.

### Left and Right Inverses

In a general algebra the notions of left inverse, right inverse and two-sided inverse are distinct. In $\mathbb{R}$ they coincide, for two reasons: $\mathbb{R}$ is commutative, so a left inverse is automatically a right inverse, and $\mathbb{R}$ is finite-dimensional over $\mathbb{R}$, so a one-sided inverse in a finite-dimensional algebra over a field is two-sided. We may therefore speak of "the" inverse without ambiguity. The biquaternion algebra is finite-dimensional as well, so the three notions coincide there too; the distinction acquires content only outside the finite-dimensional setting, as in an endomorphism algebra of an infinite-dimensional space.

### Criterion for Invertibility

**Theorem.** A real number $a$ is invertible if and only if $a \neq 0$, equivalently if and only if $N(a) \neq 0$.

**Proof.** If $a \neq 0$ then $N(a) = a^2 > 0$, and the element

$$
b = \frac{a}{N(a)} = \frac{1}{a}
$$

satisfies $ab = a\cdot\frac{1}{a} = 1$, so $a$ has an inverse. Conversely, if $a$ is invertible then applying the norm to $ab = 1$ and using multiplicativity gives $N(a)N(b) = N(1) = 1$, so $N(a) \neq 0$ and hence $a \neq 0$.

The criterion $N(a) \neq 0$ is the general form of the invertibility test of the family; in $\mathbb{R}$ it is equivalent to the elementary statement $a \neq 0$ because the norm is definite. In the biquaternion algebra the two conditions differ, and $N(\tilde{Q}) = 0$ with $\tilde{Q} \neq 0$ is exactly the definition of a zero divisor.

### The Inverse Formula

For $a \neq 0$ the inverse is

$$
a^{-1} = \frac{1}{N(a)}\,a = \frac{1}{a}.
$$

**Proof.** The verification is the computation in the first part of the proof of the criterion.

**Corollary.** If $a$ is invertible then so is $-a$, and $(-a)^{-1} = -a^{-1}$. If $a$ is invertible then so is $a^{-1}$, and $(a^{-1})^{-1} = a$. Inversion reverses the order of a product, which in a commutative algebra is invisible: $(ab)^{-1} = b^{-1}a^{-1} = a^{-1}b^{-1}$.

### Worked Examples

On the elements $a = -\tfrac{3}{4}$ and $b = \tfrac{7}{2}$, both nonzero and therefore units,

$$
a^{-1} = \frac{a}{a^2} = \frac{-\tfrac{3}{4}}{\tfrac{9}{16}} = -\tfrac{4}{3}, \qquad
b^{-1} = \frac{b}{b^2} = \frac{\tfrac{7}{2}}{\tfrac{49}{4}} = \tfrac{2}{7},
$$

with the exact verifications $a\,a^{-1} = 1$ and $b\,b^{-1} = 1$; the element $0$ has $N(0) = 0$ and is the only non-unit.

| element | $N$ | unit? | inverse |
|---|---|---|---|
| $a = -\tfrac{3}{4}$ | $\tfrac{9}{16}$ | yes | $-\tfrac{4}{3}$ |
| $b = \tfrac{7}{2}$ | $\tfrac{49}{4}$ | yes | $\tfrac{2}{7}$ |
| $0$ | $0$ | no | — |

## The Group of Units

### Definition

The **group of units** of $\mathbb{R}$ is the set of invertible elements:

$$
\mathbb{R}^\times = \{ a \in \mathbb{R} : N(a) \neq 0 \} = \mathbb{R} \setminus \{0\}.
$$

It is a group under multiplication with identity $e_0 = 1$.

### Basic Properties

- **Abelian.** Every two elements commute, because the algebra is commutative. The centre of $\mathbb{R}^\times$ is the whole group, as it is for $\mathbb{C}^\times$ and in contrast with $\mathbb{B}^\times \cong GL_2(\mathbb{C})$.
- **Open and dense.** $\mathbb{R}^\times$ is the complement of the single point $0$, hence open and dense in $\mathbb{R}$; its complement is the point $\{0\}$.
- **Disconnected, two components.** $\mathbb{R}^\times = \mathbb{R}_{>0} \cup \mathbb{R}_{<0}$ is the disjoint union of the positive and negative rays, so it has **two** connected components. This is the first structural difference from the complex case, where $\mathbb{C}^\times$ is connected; the two components of $\mathbb{R}^\times$ are the two elements of the sign group, dilated by the positive scale.
- **Non-compact.** $\mathbb{R}^\times$ is unbounded, hence not compact.
- **Infinite.** $\mathbb{R}^\times$ is uncountable and contains the infinite cyclic group of powers of any element other than $\pm1$.
- **Dimension.** As a topological group the units are one-dimensional, the positive ray contributing the one dimension and the sign group the zero-dimensional factor; the Lie structure of the group is the analytic content of *Real Exponential and Lie Group Structure*.

The unit group is the base case of the family: below it lies only the non-unit $0$, and every nonzero element is a unit because the algebra is a field.

### The Split into Positive Scale and the Sign Group

**Theorem.** The map

$$
\mathbb{R}^\times \longrightarrow \mathbb{R}_{>0} \times \{\pm1\}, \qquad a \longmapsto \bigl( |a|, \operatorname{sgn} a \bigr),
$$

where $\operatorname{sgn} a = a/|a| \in \{\pm1\}$ for $a \neq 0$, is an isomorphism of groups and a homeomorphism of topological spaces onto the product of the positive ray and the two-element group.

**Proof.** The map is well defined because $|a| > 0$ for $a \neq 0$, and its image lies in $\mathbb{R}_{>0} \times \{\pm1\}$. It is a group homomorphism: $|ab| = |a||b|$ and $\operatorname{sgn}(ab) = \operatorname{sgn}a\,\operatorname{sgn}b$, since each is positive exactly when the two factors have the same sign. Its inverse is $(r, \sigma) \mapsto r\sigma$, continuous in the product topology, so the map is a homeomorphism.

The two factors are the **scale** $r = |a| \in \mathbb{R}_{>0}$, a positive real, and the **sign** $\sigma = \operatorname{sgn}a \in \{\pm1\}$. The group $\{\pm1\}$ is the two-element cyclic group, denoted $O(1)$ below when it is regarded as the orthogonal group of the line. The product form of this isomorphism is $a = |a|\operatorname{sgn}a$, the splitting of the unit group that the norm supplies. In the complex case the second factor is the circle $U(1)$, a one-dimensional compact group, and it is connected; here it is a two-point discrete group, and the unit group is disconnected.

### The Inverse Map

The inversion map $\iota : \mathbb{R}^\times \to \mathbb{R}^\times$, $\iota(a) = a^{-1}$, is a group automorphism of order two, and writing $a = r\sigma$ with $r = |a| > 0$ and $\sigma = \operatorname{sgn}a$ it reads

$$
\iota(r\sigma) = r^{-1}\sigma^{-1} = r^{-1}\sigma ,
$$

because $\sigma^{-1} = \sigma$ for $\sigma = \pm1$. Inversion therefore inverts the scale and fixes the sign. The smoothness of the operation and its differential at the identity are Lie-group data, and they are analytic: they belong to *Real Exponential and Lie Group Structure*, the analytic article of this category, and are named here only. In the complex case inversion inverts the scale and conjugates the phase; here the sign is discrete and inversion fixes it.

## The Three-Way Classification

An element of a finite-dimensional real algebra of the tensor family is of one of three kinds: a unit, a zero divisor, or zero. The classes are read off from the norm.

**Definition.** Let $a \in \mathbb{R}$. Then exactly one of the following holds:

- $N(a) > 0$: $a$ is a **unit**, i.e. an invertible element;
- $N(a) = 0$ and $a \neq 0$: $a$ is a **zero divisor**;
- $a = 0$: $a$ is **zero**.

**Theorem (the classification of $\mathbb{R}$).** The zero-divisor class is empty, so every nonzero real number is a unit and the classification has only two non-empty classes.

**Proof.** $N(a) = a^2 = 0$ forces $a = 0$ because the square of a real number is non-negative, so the only element of vanishing norm is $0$.

### The Sign Trichotomy

The three-way classification refines, in the ordered case, to the **sign trichotomy**: every real number is positive, zero or negative, and the two nonzero cases are distinguished by the sign. This is the real analogue of the sign of the norm in the higher members, but it is finer, because the order of $\mathbb{R}$ is total and gives a third class.

| class | sign | norm | unit? | sign factor |
|---|---|---|---|---|
| $a > 0$ | $\operatorname{sgn}a = +1$ | $N(a) = a^2 > 0$ | yes | $+1$ |
| $a = 0$ | none | $N(a) = 0$ | no | undefined |
| $a < 0$ | $\operatorname{sgn}a = -1$ | $N(a) = a^2 > 0$ | yes | $-1$ |

The trichotomy is the statement that $\mathbb{R}$ is a **linearly ordered field**: the positive cone $\mathbb{R}_{>0}$ is closed under addition and multiplication, and $\mathbb{R}$ is its disjoint union with $\{0\}$ and $-\mathbb{R}_{>0}$. The sign group $\{\pm1\}$ is the multiplicative quotient $\mathbb{R}^\times/\mathbb{R}_{>0}$, the group of the two components.

### The Algebra Is a Division Algebra

The emptiness of the zero-divisor class is the statement that $\mathbb{R}$ is a **division algebra**: every nonzero element is invertible, and there are no $a, b \neq 0$ with $ab = 0$. By the Frobenius theorem, $\mathbb{R}$ is one of exactly three finite-dimensional associative real division algebras, the others being $\mathbb{C}$ and the quaternions $\mathbb{H}$, and it is the only one that is ordered. The three-way classification of the family is thus present here with its middle class empty; the biquaternion algebra has all three classes non-empty, its zero divisors being the nonzero points of the null cone $N(\tilde{Q}) = 0$.

## Distribution of the Invertible Elements

The invertible elements are distributed over the distinguished subspaces of $\mathbb{R}$ as follows. Since the only subspace is the whole algebra, the computation is immediate, and its content is the inversion-stability of the algebra.

### The Real Subspace

The real subspace $\mathbb{R}_{\mathbb{R}}$ of *Real Algebra* is the whole field, so every nonzero element $a$ is invertible and $a^{-1} = 1/a \in \mathbb{R}_{\mathbb{R}}$. Thus $\mathbb{R}_{\mathbb{R}} \setminus \{0\} = \mathbb{R}^\times$, and the algebra is inversion-stable.

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

with no anti-fixed summand. On the single piece the norm is definite, $N(a) = a^2 \geq 0$, and multiplying by an element preserves it:

$$
N(ab) = N(a)N(b).
$$

This is the degeneracy of the involution decomposition of the real field. In the complex algebra the involution splits $\mathbb{C} = \mathbb{R}_{\mathbb{C}} \oplus i\mathbb{R}_{\mathbb{C}}$ into two definite pieces of the same signature, and in the biquaternion algebra the Hermitian conjugation splits $\mathbb{B}$ into an eight-dimensional sum of a Hermitian and an anti-Hermitian subspace whose sectors carry opposite signatures, $(1,3)$ and $(3,1)$, with a sign reversal $N(i\tilde{Q}) = -N(\tilde{Q})$ for the central scalar imaginary. Here there is no second subspace, no central scalar imaginary and no sign reversal; the fixed-point decomposition collapses to its single summand, and the norm and the Hermitian form collapse with it.

## The Base Case of the Norm Series

The norm series of the corpus records, for each algebra of the family, whether its norm is real or complex, definite or indefinite, and what its vanishing locus is. In $\mathbb{R}$ the norm is the single square $N(a) = a^2$, a real positive-definite quadratic form, and its vanishing locus is the single point $\{0\}$:

| algebra | norm | value field | definite? | vanishing locus |
|---|---|---|---|---|
| $\mathbb{R}$ | $a^2$ | $\mathbb{R}$ | yes | $\{0\}$ |
| $\mathbb{C}$ | $u^2+v^2$ | $\mathbb{R}$ | yes | $\{0\}$ |
| $\mathbb{H}$ | $q_0^2+q_1^2+q_2^2+q_3^2$ | $\mathbb{R}$ | yes | $\{0\}$ |
| $\mathbb{B}$ | $\sum_\mu Q_\mu^2$ | $\mathbb{C}$ | no | the null cone |

The real case is the bottom of the definite column, the complex case adds the second square, the quaternion case adds the third and fourth, and the biquaternion case replaces the definite real form by an indefinite complex one. In every member the norm is multiplicative; the real case is the least instance of that multiplicativity, $a^2b^2 = (ab)^2$.

## Comparison with the Complex and Quaternion Cases

The definite cases of the family, and the real case for contrast, are:

| algebra | norm | definite? | zero divisors | group of units |
|---|---|---|---|---|
| $\mathbb{R}$ | $a^2$, real | yes | none | $\mathbb{R}^\times \cong \mathbb{R}_{>0} \times \{\pm1\}$ |
| $\mathbb{C}$ | $u^2+v^2$, real | yes | none | $\mathbb{C}^\times \cong \mathbb{R}_{>0} \times U(1)$ |
| $\mathbb{H}$ | $\sum_{k=0}^{3}q_k^2$, real | yes | none | $\mathbb{H}^\times \cong \mathbb{R}_{>0} \times S^3$ |
| $\mathbb{B}$ | $\sum_\mu Q_\mu^2$, complex | no | the null cone | $\mathbb{B}^\times \cong GL_2(\mathbb{C})$ |

The norm is real and definite in $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, and all three are division algebras; the norm is complex and indefinite in $\mathbb{B}$, which has zero divisors. The unit group is compact modulo the non-compact scale in $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, and genuinely non-compact in the biquaternion case. The real algebra sits at the bottom of the definite column: the complex case replaces the sign group $O(1)$ by the circle $U(1)$ and thereby connects the two components of the unit group into one, the quaternion case replaces the circle by the three-sphere $S^3$, and the biquaternion case replaces the definite norm by a complex one and the group of units by $GL_2(\mathbb{C})$.

## Summary

The norm of a real number is $N(a) = a^2$, real, positive-definite and multiplicative, $N(ab) = N(a)N(b)$; it vanishes only at the origin. The Hermitian form is the same expression, so the norm and the Hermitian form coincide, and the Euclidean norm $|a| = \sqrt{N(a)}$ is a genuine norm that is multiplicative. This is the degeneracy of the one-dimensional case.

A real number is invertible if and only if it is nonzero, equivalently if and only if its norm is nonzero, and the inverse is $a^{-1} = a/N(a) = 1/a$. The zero-divisor class is empty, so $\mathbb{R}$ is a division algebra by the Frobenius theorem, and the single distinguished subspace, the whole field, consists entirely of units together with zero.

The group of units is $\mathbb{R}^\times = \mathbb{R}\setminus\{0\}$, abelian, open, dense, disconnected and non-compact, and it splits as $\mathbb{R}^\times \cong \mathbb{R}_{>0} \times \{\pm1\}$ into a positive scale and a sign, $a = |a|\operatorname{sgn}a$. The norm is definite on the whole algebra, and the sign trichotomy $a > 0$, $a = 0$, $a < 0$ refines the three-way classification; the only element of vanishing norm is the origin, which is why the real algebra is the definite base case of the family.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}$ | the real algebra, the complete ordered field, basis $e_0 = 1$ |
| $a = a e_0$ | a real number, $a$ its coordinate |
| $\operatorname{id}$ | the identity involution, the sole involution of $\mathbb{R}$ |
| $N(a) = a\,a = a^2$ | the norm, real, positive definite, multiplicative |
| $\lvert a\rvert = \sqrt{N(a)} = \sqrt{a^2}$ | the modulus, the Euclidean norm |
| $\langle a, b \rangle = ab$ | the real inner product, $\langle a, a \rangle = N(a)$ |
| $\operatorname{sgn} a = a/\lvert a\rvert$ | the sign of a nonzero $a$, an element of $\{\pm1\}$ |
| $\mathbb{R}^\times = \mathbb{R}\setminus\{0\}$ | the group of units |
| $\mathbb{R}_{>0}, \mathbb{R}_{<0}$ | the positive and negative rays, the two components of $\mathbb{R}^\times$ |
| $\{\pm1\} \cong O(1)$ | the sign group, the two-element cyclic group |
| $a = \lvert a\rvert\operatorname{sgn}a$ | the sign decomposition, $r = \lvert a\rvert \in \mathbb{R}_{>0}$, $\sigma = \operatorname{sgn}a$ |
| $a^{-1} = a/N(a) = 1/a$ | the inverse of a nonzero element |
| $\mathbb{R}_{\mathbb{R}}$ | the fixed subspace of the identity involution, all of $\mathbb{R}$ |

## Further Reading

- Edmund Landau, *Grundlagen der Analysis* (Akademische Verlagsgesellschaft, 1930), for the ordered-field axioms and the uniqueness of $\mathbb{R}$.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for inverses, the group of units and the Frobenius theorem.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for norms and invertibility in finite-dimensional algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of the real division algebras and the place of $\mathbb{R}$ among them.
- Walter Rudin, *Principles of Mathematical Analysis*, 3rd edition (McGraw-Hill, 1976), for the absolute value, the modulus and the metric structure of the line.
- Serge Lang, *Algebra*, 3rd edition (Addison–Wesley, 1993), for ordered fields, the sign of an element and the positive cone.
