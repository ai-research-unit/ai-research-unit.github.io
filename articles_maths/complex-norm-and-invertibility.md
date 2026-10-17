
# __Complex Norm and Invertibility__

## Introduction

This article studies the norm of the complex algebra and the invertibility of its elements. It follows the basic algebra article, which defined the algebra, its unique nontrivial involution and its two distinguished subspaces. The goal here is to define the norm and the Hermitian form, to establish the criterion for invertibility, and to describe the group of units and its polar split. The complex algebra is the definite two-dimensional member of the family of algebras and the base case of the polar series, and the article collects the facts that the other members of the family generalise.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked, and concrete instances appear only where a statement would otherwise be misread. Throughout, the basis is $1$, $i$ with $i^2 = -1$, a general element is $Q = q + i q'$ with $q, q' \in \mathbb{R}$, and the involution is complex conjugation $\bar{Q} = q - i q'$. The norm is $\langle Q\rangle_{*} = Q\bar{Q}$.

## The Norm

### Definition

The **norm** of a complex number $Q$ is

$$
\langle Q\rangle_{*} = Q\bar{Q} = (q+i q')(q-i q') = q^2 + q'^2 \in \mathbb{R}.
$$

**Basic properties.**

- $\langle Q\rangle_{*}$ is a **real** number, and $\langle Q\rangle_{*} \geq 0$ with equality if and only if $Q = 0$. The norm is positive definite.
- $\langle Q\rangle_{*}$ is invariant under conjugation: $\langle \bar{Q}\rangle_{*} = Q\bar{Q} = \langle Q\rangle_{*}$.
- $\langle Q\rangle_{*}$ is invariant under multiplication by the imaginary unit: $\langle iQ\rangle_{*} = (iQ)(\overline{iQ}) = (iQ)(-i\bar{Q}) = Q\bar{Q} = \langle Q\rangle_{*}$. There is no sign reversal, because the imaginary unit of $\mathbb{C}$ is not a coefficient scalar separate from the algebra.
- $\langle Q\rangle_{*} = 0$ if and only if $Q = 0$. There are no nonzero complex numbers of vanishing norm; equivalently, the algebra has no zero divisors.

The complex norm is a genuine positive-definite quadratic form.

### Multiplicativity

**Theorem.** The norm is multiplicative:

$$
\langle Q_1 Q_2\rangle_{*} = \langle Q_1\rangle_{*} \, \langle Q_2\rangle_{*}.
$$

**Proof.** Compute

$$
\langle Q_1Q_2\rangle_{*} = (Q_1Q_2)\overline{(Q_1Q_2)} = Q_1 Q_2 \bar{Q}_2 \bar{Q}_1 = Q_1\, \langle Q_2\rangle_{*}\, \bar{Q}_1.
$$

Since $\langle Q_2\rangle_{*}$ is a real number and the algebra is commutative, it commutes with $Q_1$ and with $\bar{Q}_1$, so $Q_1 \langle Q_2\rangle_{*} \bar{Q}_1 = \langle Q_2\rangle_{*} Q_1\bar{Q}_1 = \langle Q_2\rangle_{*} \langle Q_1\rangle_{*}$.

**Corollary.** If $\langle Q_1\rangle_{*} \neq 0$ and $\langle Q_2\rangle_{*} \neq 0$, then $\langle Q_1Q_2\rangle_{*} \neq 0$. Equivalently, the product of two units is a unit.

The multiplicativity is used below to prove the invertibility criterion in one line, and it is the source of the polar decomposition: the norm is the squared scale.

### The Norm Is a Genuine Norm

The name "norm" is not a misnomer here. Define the **modulus**

$$
|Q| = \sqrt{\langle Q\rangle_{*}} = \sqrt{q^2 + q'^2} \geq 0.
$$

Then $|\cdot|$ satisfies the axioms of a norm on the real vector space $\mathbb{C} \cong \mathbb{R}^2$:

- **Positive definiteness:** $|Q| \geq 0$, and $|Q| = 0$ if and only if $Q = 0$.
- **Homogeneity:** $|\lambda Q| = |\lambda|\,|Q|$ for every $\lambda \in \mathbb{R}$; more generally $|\lambda Q| = |\lambda|\,|Q|$ for every $\lambda \in \mathbb{C}$, by multiplicativity.
- **Triangle inequality:** $|Q_1 + Q_2| \leq |Q_1| + |Q_2|$, which is the Cauchy–Schwarz inequality for the Euclidean inner product $(Q_1,Q_2) \mapsto \operatorname{Re}(\bar{Q}_1Q_2)$.
- **Multiplicativity:** $|Q_1Q_2| = |Q_1|\,|Q_2|$, from the multiplicativity of the norm.

The value is real, the vanishing locus is the origin alone, and the scaling axiom holds with a complex scalar. The complex norm is the definite base case of the norm series.

### The Norm from the Real Coordinates

Writing $Q = q + i q'$ with $q, q' \in \mathbb{R}$, the norm is the sum of two squares,

$$
\langle Q\rangle_{*} = q^2 + q'^2,
$$

a positive-definite quadratic form on the coordinate space $\mathbb{R}^2$ of signature $(2,0)$. The two coordinates contribute with the same sign, and the norm is real throughout.

## The Hermitian Form

### Definition

The **Hermitian form** of a complex number $Q$ is

$$
Q \bar{Q} = q^2 + q'^2 .
$$

It is a real number, non-negative, and vanishes if and only if $Q = 0$. Because $\mathbb{C}$ is commutative and the bar is its only nontrivial involution, the Hermitian form coincides with the norm. There are not two distinct objects here.

### The Euclidean Norm

The **Euclidean norm** of a complex number is the square root of the Hermitian form,

$$
\|Q\|_E = \sqrt{Q\bar{Q}} = \sqrt{q^2 + q'^2} = |Q| .
$$

It is a genuine norm on the real vector space $\mathbb{C} \cong \mathbb{R}^2$: positive-definite, subadditive, and homogeneous of degree one. It **is** multiplicative with respect to the complex product, because $|Q_1Q_2| = |Q_1||Q_2|$.

### Relation Between the Norm and the Hermitian Form

The two forms are related as follows.

- The **norm** $\langle Q\rangle_{*} = Q\bar{Q} = q^2+q'^2$ is real, positive-definite and multiplicative, and it vanishes only at the origin. It controls the multiplicative structure: invertibility, the group of units, and the polar scale.
- The **Hermitian form** $Q\bar{Q} = q^2+q'^2$ is the same expression. It controls the topological structure: the Euclidean norm, the topology of $\mathbb{C}$ as $\mathbb{R}^2$, and completeness.

That the two coincide is a degeneracy of the commutative two-dimensional case. The information collapses into one real positive-definite form. This is the same degeneracy that makes $\mathbb{C}$ the trivial example in the theory of composition algebras.

The **inner product** on $\mathbb{C}$ as a complex vector space is

$$
\langle Q_1, Q_2 \rangle = \bar{Q}_1 Q_2 = (q_1 q_2+q'_1 q'_2) + (q_1 q'_2-q'_1 q_2)i, \qquad Q_1 = q_1+i q'_1, \; Q_2 = q_2+i q'_2,
$$

linear in the second argument and anti-linear in the first, with $\langle Q_1, Q_1 \rangle = q_1^2+q'^2_1 = \langle Q_1\rangle_{*}$. It is complex-valued in general, and its imaginary part $q_1 q'_2 - q'_1 q_2$ is the oriented area of the parallelogram on $Q_1$ and $Q_2$. It is Hermitian, $\langle Q_1, Q_2\rangle^{*} = \langle Q_2, Q_1\rangle$, and its diagonal is the norm, $\langle Q_1,Q_1\rangle = \langle Q_1\rangle_{*}$: the inner product is the two-variable object of which the norm and the Hermitian form are the diagonal, and it is developed here.

## Invertibility

### Definition

A complex number $Q_1$ is **invertible** if there exists a complex number $Q_2$ such that

$$
Q_1 Q_2 = Q_2 Q_1 = 1 .
$$

The element $Q_2$, if it exists, is the **inverse** of $Q_1$ and is denoted $Q_1^{-1}$.

### Left and Right Inverses

In a general algebra the notions of left inverse, right inverse and two-sided inverse are distinct. In $\mathbb{C}$ they coincide, for two reasons: $\mathbb{C}$ is commutative, so a left inverse is automatically a right inverse, and $\mathbb{C}$ is finite-dimensional over $\mathbb{R}$, so a one-sided inverse in a finite-dimensional algebra over a field is two-sided. We may therefore speak of "the" inverse without ambiguity.

### Criterion for Invertibility

**Theorem.** A complex number $Q$ is invertible if and only if $Q \neq 0$, equivalently if and only if $\langle Q\rangle_{*} \neq 0$.

**Proof.** If $Q_1 \neq 0$ then $\langle Q_1\rangle_{*} = q_1^2+q'^2_1 > 0$, and the element

$$
Q_2 = \frac{\bar{Q}_1}{\langle Q_1\rangle_{*}}
$$

satisfies

$$
Q_1 Q_2 = \frac{Q_1\bar{Q}_1}{\langle Q_1\rangle_{*}} = \frac{\langle Q_1\rangle_{*}}{\langle Q_1\rangle_{*}} = 1,
$$

so $Q_1$ has an inverse. Conversely, if $Q_1$ is invertible then applying the norm to $Q_1Q_2 = 1$ and using multiplicativity gives $\langle Q_1\rangle_{*}\langle Q_2\rangle_{*} = \langle 1\rangle_{*} = 1$, so $\langle Q_1\rangle_{*} \neq 0$ and hence $Q_1 \neq 0$.

The criterion $\langle Q\rangle_{*} \neq 0$ is equivalent to the elementary statement $Q \neq 0$ because the norm is definite.

### The Inverse Formula

For $Q \neq 0$ the inverse is

$$
Q^{-1} = \frac{\bar{Q}}{\langle Q\rangle_{*}} = \frac{q - i q'}{q^2+q'^2} = \frac{q}{q^2+q'^2} - \frac{q'}{q^2+q'^2} i .
$$

**Proof.** The verification is the computation in the first part of the proof of the criterion.

**Corollary.** If $Q$ is invertible then so is $\bar{Q}$, and $(\bar{Q})^{-1} = \overline{Q^{-1}}$. If $Q$ is invertible then so is $Q^{-1}$, and $(Q^{-1})^{-1} = Q$.

### Worked Example

For the worked pair of the category, $Q_1 = 3+4i$ and $Q_2 = 1-2i$, the criterion and the inverse formula are exact. Here $\langle Q_1\rangle_{*} = 3^2+4^2 = 25 \neq 0$ and $\langle Q_2\rangle_{*} = 1^2+(-2)^2 = 5 \neq 0$, so both are units, with

$$
Q_1^{-1} = \frac{\bar{Q}_1}{\langle Q_1\rangle_{*}} = \frac{3-4i}{25} = 0.12 - 0.16 i, \qquad Q_2^{-1} = \frac{\bar{Q}_2}{\langle Q_2\rangle_{*}} = \frac{1+2i}{5} = 0.2 + 0.4 i,
$$

and $Q_1 Q_1^{-1} = 25/25 = 1$, $Q_2 Q_2^{-1} = 5/5 = 1$. The product $Q_1Q_2 = 11-2i$ has $\langle Q_1Q_2\rangle_{*} = 121+4 = 125 = 25 \cdot 5$, so it is a unit, and its inverse is computed in the two ways with the same result:

$$
(Q_1Q_2)^{-1} = Q_2^{-1}Q_1^{-1} = (0.2+0.4i)(0.12-0.16i) = 0.088 + 0.016 i, \qquad (Q_1Q_2)^{-1} = \frac{\overline{Q_1Q_2}}{\langle Q_1Q_2\rangle_{*}} = \frac{11+2i}{125} = 0.088 + 0.016 i .
$$

The only element of vanishing norm is $0$, since $q^2+q'^2 = 0$ forces $q = q' = 0$, so there is no nonzero non-unit and no zero divisor.

## The Group of Units

### Definition

The **group of units** of $\mathbb{C}$ is the set of invertible elements:

$$
\mathbb{C}^\times = \{ Q \in \mathbb{C} : \langle Q\rangle_{*} \neq 0 \} = \mathbb{C} \setminus \{0\}.
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
\mathbb{C}^\times \longrightarrow \mathbb{R}_{>0} \times \mathrm{U}(1), \qquad Q \longmapsto \bigl( |Q|, \; Q/|Q| \bigr),
$$

where $\mathrm{U}(1) = \{ u \in \mathbb{C} : |u| = 1 \}$ is the unit circle, is an isomorphism of topological groups.

**Proof.** The map is well defined because $|Q_1| > 0$ for $Q_1 \neq 0$, and its image lies in $\mathbb{R}_{>0} \times \mathrm{U}(1)$ because $|Q_1/|Q_1|| = 1$. It is a group homomorphism: $|Q_1Q_2| = |Q_1||Q_2|$ and $Q_1Q_2/|Q_1Q_2| = (Q_1/|Q_1|)(Q_2/|Q_2|)$. Its inverse is $(r,u) \mapsto ru$, which is continuous, so it is a homeomorphism.

The two factors are the **scale** $r = |Q| \in \mathbb{R}_{>0}$, a positive real, and the **phase** $u = Q/|Q| \in \mathrm{U}(1)$. The product form is $Q = ru$; here it is recorded as the splitting of the unit group, which is what the norm supplies.

### The Inverse Map

The inversion map $\iota : \mathbb{C}^\times \to \mathbb{C}^\times$, $\iota(Q) = Q^{-1}$, is a continuous group automorphism of order two, and in the polar coordinates it reads

$$
\iota(ru) = r^{-1} u^{-1} = r^{-1} \bar{u},
$$

because for a unit $u$ one has $u^{-1} = \bar{u}$. Inversion therefore inverts the scale and conjugates the phase.

## The Three-Way Classification

An element of a finite-dimensional real algebra is of one of three kinds: a unit, a zero divisor, or zero. The classes are read off from the norm.

**Definition.** Let $Q \in \mathbb{C}$. Then exactly one of the following holds:

- $\langle Q\rangle_{*} > 0$: $Q$ is a **unit**, i.e. an invertible element;
- $\langle Q\rangle_{*} = 0$ and $Q \neq 0$: $Q$ is a **zero divisor**;
- $Q = 0$: $Q$ is **zero**.

**Theorem (the classification of $\mathbb{C}$).** The zero-divisor class is empty, so every nonzero complex number is a unit and the classification has only two non-empty classes.

**Proof.** $\langle Q\rangle_{*} = q^2+q'^2 = 0$ forces $q = q' = 0$ because squares of reals are non-negative, so the only element of vanishing norm is $0$.

### The Algebra Is a Division Algebra

The emptiness of the zero-divisor class is the statement that $\mathbb{C}$ is a **division algebra**: every nonzero element is invertible, and there are no $Q_1, Q_2 \neq 0$ with $Q_1Q_2 = 0$. By the Frobenius theorem, $\mathbb{C}$ is one of exactly three finite-dimensional associative real division algebras, and it is the only one that is commutative but not ordered. The zero-divisor class is here empty.

## Distribution of the Invertible Elements

The invertible elements are distributed over the two distinguished subspaces as follows. Since every nonzero element is a unit, both computations are immediate, and their content is the inversion-stability of the two subspaces.

### The Real Subspace

The real subspace $\mathbb{R}_{\mathbb{C}} = \{q : q \in \mathbb{R}\}$ is a field, so every nonzero element $q$ is invertible and $q^{-1} = 1/q \in \mathbb{R}_{\mathbb{C}}$. Thus $\mathbb{R}_{\mathbb{C}} \setminus \{0\} \subset \mathbb{C}^\times$, and the real subspace is inversion-stable.

### The Imaginary Subspace

For a nonzero element $i q'$, $q' \neq 0$, of the imaginary subspace $i\mathbb{R}_{\mathbb{C}}$,

$$
(i q')^{-1} = \frac{-i q'}{q'^2} = -\frac{1}{q'} i = -\frac{1}{q'} i \in i\mathbb{R}_{\mathbb{C}},
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
\langle q\rangle_{*} = q^2 \geq 0 \;\; (q \in \mathbb{R}_{\mathbb{C}}), \qquad \langle i q'\rangle_{*} = q'^2 \geq 0 \;\; (q' \in \mathbb{R}_{\mathbb{C}}),
$$

each vanishing only at the origin. The two pieces therefore carry the **same** sign of the norm, $(+,+)$ on the two-dimensional real coordinate space, and multiplying by the imaginary unit preserves it:

$$
\langle i Q\rangle_{*} = \langle Q\rangle_{*}.
$$

This is the degeneracy of the Hermitian decomposition of the definite field. No sign reversal and no indefinite form occur. The distinction between the norm and the Hermitian form collapses: both are the single expression $Q\bar{Q}$.

## The Base Case of the Norm Series

The norm series of the corpus records, for each algebra of the family, whether its norm is real, complex or split-complex valued, whether it is definite or indefinite, and what its vanishing locus is. In $\mathbb{C}$ the norm is the real positive-definite quadratic form $\langle Q\rangle_{*} = q^2+q'^2$, the sum of two squares, and its vanishing locus is the single point $\{0\}$:

| algebra | norm | value field | definite? | vanishing locus |
|---|---|---|---|---|
| $\mathbb{R}$ | $a^2$ | $\mathbb{R}$ | yes | $\{0\}$ |
| $\mathbb{C}$ | $q^2+q'^2$ | $\mathbb{R}$ | yes | $\{0\}$ |
| $\mathbb{H}$ | $q_t^2+q_x^2+q_y^2+q_z^2$ | $\mathbb{R}$ | yes | $\{0\}$ |
| $\mathbb{H}_{\mathbb{D}}$ | $\sum_\mu Q_\mu^2$ | $\mathbb{D}$ | no | the elements whose norm is a zero divisor of $\mathbb{D}$ |

The complex case is the second rung of the definite column: it adds the second square to the square of $\mathbb{R}$. The norm is multiplicative, $\langle Q_1Q_2\rangle_{*} = \langle Q_1\rangle_{*}\langle Q_2\rangle_{*}$, and because the form is definite the vanishing locus stays a single point.

## Summary

The norm of a complex number is $\langle Q\rangle_{*} = Q\bar{Q} = q^2+q'^2$, real, positive-definite and multiplicative, $\langle Q_1Q_2\rangle_{*} = \langle Q_1\rangle_{*}\langle Q_2\rangle_{*}$; it vanishes only at the origin. The Hermitian form is the same expression, so the norm and the Hermitian form coincide, and the Euclidean norm $\|Q\|_E = \sqrt{\langle Q\rangle_{*}}$ is a genuine norm that is multiplicative. This is the degeneracy of the commutative two-dimensional case.

A complex number is invertible if and only if it is nonzero, equivalently if and only if its norm is nonzero, and the inverse is $Q^{-1} = \bar{Q}/\langle Q\rangle_{*}$. On the worked pair $Q_1 = 3+4i$, $Q_2 = 1-2i$ the criterion gives $\langle Q_1\rangle_{*} = 25$, $\langle Q_2\rangle_{*} = 5$ and $\langle Q_1Q_2\rangle_{*} = 125$, with inverses $Q_1^{-1} = (3-4i)/25$ and $Q_2^{-1} = (1+2i)/5$. The zero-divisor class is empty, so $\mathbb{C}$ is a division algebra by the Frobenius theorem, and every nonzero element of each of the two distinguished subspaces is invertible.

The group of units is $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$, abelian, open, dense, connected and non-compact, and it splits as $\mathbb{C}^\times \cong \mathbb{R}_{>0} \times \mathrm{U}(1)$ into a positive scale and a phase, the product form of that splitting being $Q = ru$. The norm is definite on both the real and the imaginary subspace with the same sign, and the only element of vanishing norm is the origin, which is why the complex norm is the definite base case of the norm series and the complex algebra the definite base case of the family.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex algebra, basis $1$, $i$, $i^2 = -1$ |
| $Q = q + i q'$ | a complex number, $q$ its real part, $q'$ its imaginary part |
| $\bar{Q} = q - i q'$ | complex conjugation, the nontrivial involution |
| $\langle Q\rangle_{*} = Q\bar{Q} = q^2+q'^2$ | the norm, real, positive definite, multiplicative |
| $\|Q\|_E = \sqrt{\langle Q\rangle_{*}} = |Q|$ | the Euclidean norm and the modulus |
| $\langle Q_1, Q_2 \rangle = \bar{Q}_1Q_2$ | the complex inner product, $\langle Q_1,Q_1\rangle = \langle Q_1\rangle_{*}$ |
| $Q_1 = 3+4i$, $Q_2 = 1-2i$ | the worked pair of the category |
| $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$ | the group of units |
| $\mathrm{U}(1) = \{u : |u| = 1\}$ | the unit circle, the phase factor group |
| $Q = ru$ | the polar split, $r = |Q| \in \mathbb{R}_{>0}$, $u = Q/|Q| \in \mathrm{U}(1)$ |
| $Q^{-1} = \bar{Q}/\langle Q\rangle_{*}$ | the inverse of a nonzero element |
| $\mathbb{R}_{\mathbb{C}}, i\mathbb{R}_{\mathbb{C}}$ | the real and imaginary subspaces of $\mathbb{C}$ |

## Further Reading

- Carl Friedrich Gauss, *Theoria residuorum biquadraticorum, Commentatio secunda* (Göttingen, 1831), for the norm and the modulus of a complex number.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for division algebras, inverses and the Frobenius theorem.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for norms, invertibility in finite-dimensional algebras and the group of units.
- Walter Rudin, *Real and Complex Analysis*, 3rd edition (McGraw-Hill, 1987), for the modulus, the Euclidean norm and the polar decomposition of a complex number.
