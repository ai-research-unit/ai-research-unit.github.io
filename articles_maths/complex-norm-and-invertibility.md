
# __Complex Norm and Invertibility__

## Introduction

This article studies the norm of the complex algebra and the invertibility of its elements. It follows the basic algebra article, which defined the algebra, its unique nontrivial involution and its two distinguished subspaces. The goal here is to define the norm and the Hermitian form, to establish the criterion for invertibility, and to describe the group of units and its polar split. The complex algebra is the definite two-dimensional member of the family of algebras and the base case of the polar series, and the article collects the facts that the other members of the family generalise.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked, and concrete instances appear only where a statement would otherwise be misread. Throughout, the basis is $1$, $i$ with $i^2 = -1$, a general element is $A = a + i a'$ with $a, a' \in \mathbb{R}$, and the involution is complex conjugation $\bar{A} = a - i a'$. The norm is $\langle A\rangle_{*} = A\bar{A}$.

## The Norm

### Definition

The **norm** of a complex number $A$ is

$$
\langle A\rangle_{*} = A\bar{A} = (a+i a')(a-i a') = a^2 + a'^2 \in \mathbb{R}.
$$

**Basic properties.**

- $\langle A\rangle_{*}$ is a **real** number, and $\langle A\rangle_{*} \geq 0$ with equality if and only if $A = 0$. The norm is positive definite.
- $\langle A\rangle_{*}$ is invariant under conjugation: $\langle \bar{A}\rangle_{*} = A\bar{A} = \langle A\rangle_{*}$.
- $\langle A\rangle_{*}$ is invariant under multiplication by the imaginary unit: $\langle iZ\rangle_{*} = (iZ)(\overline{iZ}) = (iZ)(-i\bar{A}) = A\bar{A} = \langle A\rangle_{*}$. There is no sign reversal, because the imaginary unit of $\mathbb{C}$ is not a coefficient scalar separate from the algebra.
- $\langle A\rangle_{*} = 0$ if and only if $A = 0$. There are no nonzero complex numbers of vanishing norm; equivalently, the algebra has no zero divisors.

The complex norm is a genuine positive-definite quadratic form.

### Multiplicativity

**Theorem.** The norm is multiplicative:

$$
\langle A B\rangle_{*} = \langle A\rangle_{*} \, \langle B\rangle_{*}.
$$

**Proof.** Compute

$$
\langle AB\rangle_{*} = (AB)\overline{(AB)} = A B \bar{B} \bar{A} = A\, \langle B\rangle_{*}\, \bar{A}.
$$

Since $\langle B\rangle_{*}$ is a real number and the algebra is commutative, it commutes with $A$ and with $\bar{A}$, so $A \langle B\rangle_{*} \bar{A} = \langle B\rangle_{*} A\bar{A} = \langle B\rangle_{*} \langle A\rangle_{*}$.

**Corollary.** If $\langle A\rangle_{*} \neq 0$ and $\langle B\rangle_{*} \neq 0$, then $\langle AB\rangle_{*} \neq 0$. Equivalently, the product of two units is a unit.

The multiplicativity is used below to prove the invertibility criterion in one line, and it is the source of the polar decomposition: the norm is the squared scale.

### The Norm Is a Genuine Norm

The name "norm" is not a misnomer here. Define the **modulus**

$$
|A| = \sqrt{\langle A\rangle_{*}} = \sqrt{a^2 + a'^2} \geq 0.
$$

Then $|\cdot|$ satisfies the axioms of a norm on the real vector space $\mathbb{C} \cong \mathbb{R}^2$:

- **Positive definiteness:** $|A| \geq 0$, and $|A| = 0$ if and only if $A = 0$.
- **Homogeneity:** $|\lambda A| = |\lambda|\,|A|$ for every $\lambda \in \mathbb{R}$; more generally $|\lambda A| = |\lambda|\,|A|$ for every $\lambda \in \mathbb{C}$, by multiplicativity.
- **Triangle inequality:** $|A + B| \leq |A| + |B|$, which is the Cauchy–Schwarz inequality for the Euclidean inner product $(A,B) \mapsto \operatorname{Re}(\bar{A}B)$.
- **Multiplicativity:** $|AB| = |A|\,|B|$, from the multiplicativity of the norm.

The value is real, the vanishing locus is the origin alone, and the scaling axiom holds with a complex scalar. The complex norm is the definite base case of the norm series.

### The Norm from the Real Coordinates

Writing $A = a + i a'$ with $a, a' \in \mathbb{R}$, the norm is the sum of two squares,

$$
\langle A\rangle_{*} = a^2 + a'^2,
$$

a positive-definite quadratic form on the coordinate space $\mathbb{R}^2$ of signature $(2,0)$. The two coordinates contribute with the same sign, and the norm is real throughout.

## The Hermitian Form

### Definition

The **Hermitian form** of a complex number $A$ is

$$
A \bar{A} = a^2 + a'^2 .
$$

It is a real number, non-negative, and vanishes if and only if $A = 0$. Because $\mathbb{C}$ is commutative and the bar is its only nontrivial involution, the Hermitian form coincides with the norm. There are not two distinct objects here.

### The Euclidean Norm

The **Euclidean norm** of a complex number is the square root of the Hermitian form,

$$
\|A\|_E = \sqrt{A\bar{A}} = \sqrt{a^2 + a'^2} = |A| .
$$

It is a genuine norm on the real vector space $\mathbb{C} \cong \mathbb{R}^2$: positive-definite, subadditive, and homogeneous of degree one. It **is** multiplicative with respect to the complex product, because $|AB| = |A||B|$.

### Relation Between the Norm and the Hermitian Form

The two forms are related as follows.

- The **norm** $\langle A\rangle_{*} = A\bar{A} = a^2+a'^2$ is real, positive-definite and multiplicative, and it vanishes only at the origin. It controls the multiplicative structure: invertibility, the group of units, and the polar scale.
- The **Hermitian form** $A\bar{A} = a^2+a'^2$ is the same expression. It controls the topological structure: the Euclidean norm, the topology of $\mathbb{C}$ as $\mathbb{R}^2$, and completeness.

That the two coincide is a degeneracy of the commutative two-dimensional case. The information collapses into one real positive-definite form. This is the same degeneracy that makes $\mathbb{C}$ the trivial example in the theory of composition algebras.

The **inner product** on $\mathbb{C}$ as a complex vector space is

$$
\langle A, B \rangle = \bar{A} B = (a b+a' b') + (a b'-a' b)i, \qquad A = a+i a', \; B = b+i b',
$$

linear in the second argument and anti-linear in the first, with $\langle A, A \rangle = a^2+a'^2 = \langle A\rangle_{*}$. It is complex-valued in general, and its imaginary part $a b' - a' b$ is the oriented area of the parallelogram on $A$ and $B$. It is Hermitian, $\langle A, B\rangle^{*} = \langle B, A\rangle$, and its diagonal is the norm, $\langle A,A\rangle = \langle A\rangle_{*}$: the inner product is the two-variable object of which the norm and the Hermitian form are the diagonal, and it is developed here.

## Invertibility

### Definition

A complex number $A$ is **invertible** if there exists a complex number $B$ such that

$$
A B = B A = 1 .
$$

The element $B$, if it exists, is the **inverse** of $A$ and is denoted $A^{-1}$.

### Left and Right Inverses

In a general algebra the notions of left inverse, right inverse and two-sided inverse are distinct. In $\mathbb{C}$ they coincide, for two reasons: $\mathbb{C}$ is commutative, so a left inverse is automatically a right inverse, and $\mathbb{C}$ is finite-dimensional over $\mathbb{R}$, so a one-sided inverse in a finite-dimensional algebra over a field is two-sided. We may therefore speak of "the" inverse without ambiguity.

### Criterion for Invertibility

**Theorem.** A complex number $A$ is invertible if and only if $A \neq 0$, equivalently if and only if $\langle A\rangle_{*} \neq 0$.

**Proof.** If $A \neq 0$ then $\langle A\rangle_{*} = a^2+a'^2 > 0$, and the element

$$
B = \frac{\bar{A}}{\langle A\rangle_{*}}
$$

satisfies

$$
A B = \frac{A\bar{A}}{\langle A\rangle_{*}} = \frac{\langle A\rangle_{*}}{\langle A\rangle_{*}} = 1,
$$

so $A$ has an inverse. Conversely, if $A$ is invertible then applying the norm to $AB = 1$ and using multiplicativity gives $\langle A\rangle_{*}\langle B\rangle_{*} = \langle 1\rangle_{*} = 1$, so $\langle A\rangle_{*} \neq 0$ and hence $A \neq 0$.

The criterion $\langle A\rangle_{*} \neq 0$ is equivalent to the elementary statement $A \neq 0$ because the norm is definite.

### The Inverse Formula

For $A \neq 0$ the inverse is

$$
A^{-1} = \frac{\bar{A}}{\langle A\rangle_{*}} = \frac{a - i a'}{a^2+a'^2} = \frac{a}{a^2+a'^2} - \frac{a'}{a^2+a'^2} i .
$$

**Proof.** The verification is the computation in the first part of the proof of the criterion.

**Corollary.** If $A$ is invertible then so is $\bar{A}$, and $(\bar{A})^{-1} = \overline{A^{-1}}$. If $A$ is invertible then so is $A^{-1}$, and $(A^{-1})^{-1} = A$.

### Worked Example

For the worked pair of the category, $A = 3+4i$ and $B = 1-2i$, the criterion and the inverse formula are exact. Here $\langle A\rangle_{*} = 3^2+4^2 = 25 \neq 0$ and $\langle B\rangle_{*} = 1^2+(-2)^2 = 5 \neq 0$, so both are units, with

$$
A^{-1} = \frac{\bar{A}}{\langle A\rangle_{*}} = \frac{3-4i}{25} = 0.12 - 0.16 i, \qquad B^{-1} = \frac{\bar{B}}{\langle B\rangle_{*}} = \frac{1+2i}{5} = 0.2 + 0.4 i,
$$

and $A A^{-1} = 25/25 = 1$, $B B^{-1} = 5/5 = 1$. The product $AB = 11-2i$ has $\langle AB\rangle_{*} = 121+4 = 125 = 25 \cdot 5$, so it is a unit, and its inverse is computed in the two ways with the same result:

$$
(AB)^{-1} = B^{-1}A^{-1} = (0.2+0.4i)(0.12-0.16i) = 0.088 + 0.016 i, \qquad (AB)^{-1} = \frac{\overline{AB}}{\langle AB\rangle_{*}} = \frac{11+2i}{125} = 0.088 + 0.016 i .
$$

The only element of vanishing norm is $0$, since $a^2+a'^2 = 0$ forces $a = a' = 0$, so there is no nonzero non-unit and no zero divisor.

## The Group of Units

### Definition

The **group of units** of $\mathbb{C}$ is the set of invertible elements:

$$
\mathbb{C}^\times = \{ A \in \mathbb{C} : \langle A\rangle_{*} \neq 0 \} = \mathbb{C} \setminus \{0\}.
$$

It is a group under multiplication with identity $1$.

### Basic Properties

- **Open and dense.** $\mathbb{C}^\times$ is the complement of the single point $0$, hence open and dense in $\mathbb{C}$; its complement is the point $\{0\}$, of real dimension $0$.
- **Connected and non-compact.** $\mathbb{C}^\times$ is path-connected, and it is not compact since it is unbounded; it has one component, where $\mathbb{D}^\times$ has four.
- **Infinite.** $\mathbb{C}^\times$ is uncountable and contains the infinite cyclic group of powers of any non-root-of-unity element.
- **Dimension.** $\mathbb{C}^\times$ is a topological group whose underlying space is a manifold of real dimension $2$; its Lie group and Lie algebra structure are the subject of the companion article *Complex Exponential and Lie Group Structure*.

The unit group is the base case of the family: below it lies only the non-unit $0$, and every nonzero element is a unit because the algebra is a field.

### The Polar Split of the Group of Units

**Theorem.** The map

$$
\mathbb{C}^\times \longrightarrow \mathbb{R}_{>0} \times U(1), \qquad A \longmapsto \bigl( |A|, \; A/|A| \bigr),
$$

where $U(1) = \{ u \in \mathbb{C} : |u| = 1 \}$ is the unit circle, is an isomorphism of topological groups.

**Proof.** The map is well defined because $|A| > 0$ for $A \neq 0$, and its image lies in $\mathbb{R}_{>0} \times U(1)$ because $|A/|A|| = 1$. It is a group homomorphism: $|AB| = |A||B|$ and $AB/|AB| = (A/|A|)(B/|B|)$. Its inverse is $(r,u) \mapsto ru$, which is continuous, so it is a homeomorphism.

The two factors are the **scale** $r = |A| \in \mathbb{R}_{>0}$, a positive real, and the **phase** $u = A/|A| \in U(1)$. The product form is $A = ru$; here it is recorded as the splitting of the unit group, which is what the norm supplies.

### The Inverse Map

The inversion map $\iota : \mathbb{C}^\times \to \mathbb{C}^\times$, $\iota(A) = A^{-1}$, is a continuous group automorphism of order two, and in the polar coordinates it reads

$$
\iota(ru) = r^{-1} u^{-1} = r^{-1} \bar{u},
$$

because for a unit $u$ one has $u^{-1} = \bar{u}$. Inversion therefore inverts the scale and conjugates the phase.

## The Three-Way Classification

An element of a finite-dimensional real algebra is of one of three kinds: a unit, a zero divisor, or zero. The classes are read off from the norm.

**Definition.** Let $A \in \mathbb{C}$. Then exactly one of the following holds:

- $\langle A\rangle_{*} > 0$: $A$ is a **unit**, i.e. an invertible element;
- $\langle A\rangle_{*} = 0$ and $A \neq 0$: $A$ is a **zero divisor**;
- $A = 0$: $A$ is **zero**.

**Theorem (the classification of $\mathbb{C}$).** The zero-divisor class is empty, so every nonzero complex number is a unit and the classification has only two non-empty classes.

**Proof.** $\langle A\rangle_{*} = a^2+a'^2 = 0$ forces $a = a' = 0$ because squares of reals are non-negative, so the only element of vanishing norm is $0$.

### The Algebra Is a Division Algebra

The emptiness of the zero-divisor class is the statement that $\mathbb{C}$ is a **division algebra**: every nonzero element is invertible, and there are no $A, B \neq 0$ with $AB = 0$. By the Frobenius theorem, $\mathbb{C}$ is one of exactly three finite-dimensional associative real division algebras, and it is the only one that is commutative but not ordered. The zero-divisor class is here empty.

## Distribution of the Invertible Elements

The invertible elements are distributed over the two distinguished subspaces as follows. Since every nonzero element is a unit, both computations are immediate, and their content is the inversion-stability of the two subspaces.

### The Real Subspace

The real subspace $\mathbb{R}_{\mathbb{C}} = \{a : a \in \mathbb{R}\}$ is a field, so every nonzero element $a$ is invertible and $a^{-1} = 1/a \in \mathbb{R}_{\mathbb{C}}$. Thus $\mathbb{R}_{\mathbb{C}} \setminus \{0\} \subset \mathbb{C}^\times$, and the real subspace is inversion-stable.

### The Imaginary Subspace

For a nonzero element $i a'$, $a' \neq 0$, of the imaginary subspace $i\mathbb{R}_{\mathbb{C}}$,

$$
(i a')^{-1} = \frac{-i a'}{a'^2} = -\frac{1}{a'} i = -\frac{1}{a'} i \in i\mathbb{R}_{\mathbb{C}},
$$

so the inverse is again a real multiple of $i$. Hence $i\mathbb{R}_{\mathbb{C}} \setminus \{0\} \subset \mathbb{C}^\times$, and the imaginary subspace is also inversion-stable.

### Summary of the Distribution

| subspace | nonzero elements | invertible | invertible elements not units |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | all of $\mathbb{R}_{\mathbb{C}} \setminus \{0\}$ | all | none |
| $i\mathbb{R}_{\mathbb{C}}$ | all of $i\mathbb{R}_{\mathbb{C}} \setminus \{0\}$ | all | none |

Equivalently, $\mathbb{C}^\times = (\mathbb{R}_{\mathbb{C}} \setminus \{0\}) \cup (i\mathbb{R}_{\mathbb{C}} \setminus \{0\}) \cup (\text{the mixed elements})$, and the union is all nonzero complex numbers. There is no sector of the algebra carrying a zero divisor, and the distribution is uniform.

## The Relation to the Hermitian Decomposition

The algebra splits as $\mathbb{C} = \mathbb{R}_{\mathbb{C}} \oplus i\mathbb{R}_{\mathbb{C}}$ into the fixed and anti-fixed subspaces of conjugation, and on each piece the norm is definite:

$$
\langle a\rangle_{*} = a^2 \geq 0 \;\; (a \in \mathbb{R}_{\mathbb{C}}), \qquad \langle i a'\rangle_{*} = a'^2 \geq 0 \;\; (a' \in \mathbb{R}_{\mathbb{C}}),
$$

each vanishing only at the origin. The two pieces therefore carry the **same** sign of the norm, $(+,+)$ on the two-dimensional real coordinate space, and multiplying by the imaginary unit preserves it:

$$
\langle i A\rangle_{*} = \langle A\rangle_{*}.
$$

This is the degeneracy of the Hermitian decomposition of the definite field. No sign reversal and no indefinite form occur. The distinction between the norm and the Hermitian form collapses: both are the single expression $A\bar{A}$.

## The Base Case of the Norm Series

The norm series of the corpus records, for each algebra of the family, whether its norm is real, complex or split-complex valued, whether it is definite or indefinite, and what its vanishing locus is. In $\mathbb{C}$ the norm is the real positive-definite quadratic form $\langle A\rangle_{*} = a^2+a'^2$, the sum of two squares, and its vanishing locus is the single point $\{0\}$:

| algebra | norm | value field | definite? | vanishing locus |
|---|---|---|---|---|
| $\mathbb{R}$ | $a^2$ | $\mathbb{R}$ | yes | $\{0\}$ |
| $\mathbb{C}$ | $a^2+a'^2$ | $\mathbb{R}$ | yes | $\{0\}$ |
| $\mathbb{H}$ | $q_0^2+q_1^2+q_2^2+q_3^2$ | $\mathbb{R}$ | yes | $\{0\}$ |
| $\mathbb{H}_{\mathbb{D}}$ | $\sum_\mu Q_\mu^2$ | $\mathbb{D}$ | no | the elements whose norm is a zero divisor of $\mathbb{D}$ |

The complex case is the second rung of the definite column: it adds the second square to the square of $\mathbb{R}$. The norm is multiplicative, $\langle AB\rangle_{*} = \langle A\rangle_{*}\langle B\rangle_{*}$, and because the form is definite the vanishing locus stays a single point.

## Summary

The norm of a complex number is $\langle A\rangle_{*} = A\bar{A} = a^2+a'^2$, real, positive-definite and multiplicative, $\langle AB\rangle_{*} = \langle A\rangle_{*}\langle B\rangle_{*}$; it vanishes only at the origin. The Hermitian form is the same expression, so the norm and the Hermitian form coincide, and the Euclidean norm $\|A\|_E = \sqrt{\langle A\rangle_{*}}$ is a genuine norm that is multiplicative. This is the degeneracy of the commutative two-dimensional case.

A complex number is invertible if and only if it is nonzero, equivalently if and only if its norm is nonzero, and the inverse is $A^{-1} = \bar{A}/\langle A\rangle_{*}$. On the worked pair $A = 3+4i$, $B = 1-2i$ the criterion gives $\langle A\rangle_{*} = 25$, $\langle B\rangle_{*} = 5$ and $\langle AB\rangle_{*} = 125$, with inverses $A^{-1} = (3-4i)/25$ and $B^{-1} = (1+2i)/5$. The zero-divisor class is empty, so $\mathbb{C}$ is a division algebra by the Frobenius theorem, and every nonzero element of each of the two distinguished subspaces is invertible.

The group of units is $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$, abelian, open, dense, connected and non-compact, and it splits as $\mathbb{C}^\times \cong \mathbb{R}_{>0} \times U(1)$ into a positive scale and a phase, the product form of that splitting being $A = ru$. The norm is definite on both the real and the imaginary subspace with the same sign, and the only element of vanishing norm is the origin, which is why the complex norm is the definite base case of the norm series and the complex algebra the definite base case of the family.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex algebra, basis $1$, $i$, $i^2 = -1$ |
| $A = a + i a'$ | a complex number, $a$ its real part, $a'$ its imaginary part |
| $\bar{A} = a - i a'$ | complex conjugation, the nontrivial involution |
| $\langle A\rangle_{*} = A\bar{A} = a^2+a'^2$ | the norm, real, positive definite, multiplicative |
| $\|A\|_E = \sqrt{\langle A\rangle_{*}} = |A|$ | the Euclidean norm and the modulus |
| $\langle A, B \rangle = \bar{A}B$ | the complex inner product, $\langle A,A\rangle = \langle A\rangle_{*}$ |
| $A = 3+4i$, $B = 1-2i$ | the worked pair of the category |
| $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$ | the group of units |
| $U(1) = \{u : |u| = 1\}$ | the unit circle, the phase factor group |
| $A = ru$ | the polar split, $r = |A| \in \mathbb{R}_{>0}$, $u = A/|A| \in U(1)$ |
| $A^{-1} = \bar{A}/\langle A\rangle_{*}$ | the inverse of a nonzero element |
| $\mathbb{R}_{\mathbb{C}}, i\mathbb{R}_{\mathbb{C}}$ | the real and imaginary subspaces of $\mathbb{C}$ |

## Further Reading

- Carl Friedrich Gauss, *Theoria residuorum biquadraticorum, Commentatio secunda* (Göttingen, 1831), for the norm and the modulus of a complex number.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for division algebras, inverses and the Frobenius theorem.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for norms, invertibility in finite-dimensional algebras and the group of units.
- Walter Rudin, *Real and Complex Analysis*, 3rd edition (McGraw-Hill, 1987), for the modulus, the Euclidean norm and the polar decomposition of a complex number.
