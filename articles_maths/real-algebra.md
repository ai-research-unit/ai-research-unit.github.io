
# __Real Algebra__

## Introduction

This article introduces the real algebra as an algebraic structure. The goal is to define the algebra precisely, establish its basic properties, and describe the distinguished substructures that arise from its order and completeness.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No topology beyond the order is invoked. The real numbers are treated as an algebraic object, and the consequences of their algebraic properties are developed systematically.

## The Real Numbers

### Definition

The **real number field** $\mathbb{R}$ is a set equipped with two binary operations $+$ and $\cdot$, two distinguished elements $0$ and $1$, and a total order $<$, satisfying the following axioms.

**Field axioms.** The structure $(\mathbb{R}, +, \cdot)$ is a field:

$$
q_1 + q_2 = q_2 + q_1, \qquad q_1 \cdot q_2 = q_2 \cdot q_1,
$$

$$
(q_1 + q_2) + q_3 = q_1 + (q_2 + q_3), \qquad (q_1 \cdot q_2) \cdot q_3 = q_1 \cdot (q_2 \cdot q_3),
$$

$$
q_1 \cdot (q_2 + q_3) = q_1 \cdot q_2 + q_1 \cdot q_3,
$$

$$
q + 0 = q, \qquad q \cdot 1 = q,
$$

and for every $q \in \mathbb{R}$ there exists $-q$ with $q + (-q) = 0$, and for every $q \neq 0$ there exists $q^{-1}$ with $q \cdot q^{-1} = 1$.

**Order axioms.** The order $<$ is total and compatible with the field operations:

$$
\text{for any } q_1, q_2 \in \mathbb{R}, \text{ exactly one of } q_1 < q_2, \; q_1 = q_2, \; q_1 > q_2 \text{ holds},
$$

$$
q_1 < q_2 \implies q_1 + q_3 < q_2 + q_3,
$$

$$
q_1 < q_2 \text{ and } q_3 > 0 \implies q_1 \cdot q_3 < q_2 \cdot q_3.
$$

**Completeness axiom.** Every non-empty subset of $\mathbb{R}$ that is bounded above has a least upper bound in $\mathbb{R}$:

$$
S \subseteq \mathbb{R}, \; S \neq \emptyset, \; S \text{ bounded above} \implies \sup S \in \mathbb{R}.
$$

A general real number is written in developed form as

$$
q = q \cdot 1, \qquad q \in \mathbb{R},
$$

or, more compactly, as

$$
q \in \mathbb{R}.
$$

We write

$$
q = q \cdot 1,
$$

where $q$ is the **scalar part** and there is no vector part. The absence of a tilde signals that $q$ is an element of the algebra $\mathbb{R}$, not a vector in some larger space.

There is no complexification and no distinguished imaginary unit. The only imaginary unit in the algebra is the one we do not introduce. The real numbers are real.

### Basic Properties

**Commutative.** Real addition and multiplication are commutative: $q_1 + q_2 = q_2 + q_1$ and $q_1 \cdot q_2 = q_2 \cdot q_1$.

**Associative.** Real addition and multiplication are associative: $(q_1 + q_2) + q_3 = q_1 + (q_2 + q_3)$ and $(q_1 \cdot q_2) \cdot q_3 = q_1 \cdot (q_2 \cdot q_3)$.

**Distributive.** $q_1 \cdot (q_2 + q_3) = q_1 \cdot q_2 + q_1 \cdot q_3$.

**Ordered field.** The real numbers form a totally ordered field. The order is Archimedean: for any $q, b \in \mathbb{R}$ with $q > 0$, there exists a natural number $n$ with $n q > b$. This excludes ordered fields containing infinitesimals.

**Complete ordered field.** The real numbers are the unique complete ordered field up to isomorphism. Every other complete ordered field is order-isomorphic to $\mathbb{R}$.

**Frobenius theorem.** The real numbers are one of only three finite-dimensional associative real division algebras. In fact, $\mathbb{R}$ is the only one that is commutative and ordered.

### The Absolute Value and the Positive Cone

The **absolute value** of a real number $q$ is

$$
|q| = \begin{cases} q & q \geq 0, \\ -q & q < 0. \end{cases}
$$

It satisfies $|q| \geq 0$, $|q| = 0 \iff q = 0$, $|q_1 q_2| = |q_1||q_2|$, and $|q_1 + q_2| \leq |q_1| + |q_2|$. The last is the triangle inequality, and it is the only one that uses the order in an essential way.

The set of non-negative reals

$$
\mathbb{R}_{\geq 0} = \{a \in \mathbb{R} : a \geq 0\}
$$

is a multiplicative submonoid of $\mathbb{R}$ and is closed under addition. It is the **positive cone** of the ordered field, and it determines the order by

$$
q_1 < q_2 \iff q_2 - q_1 \in \mathbb{R}_{>0}.
$$

The absolute value is not a separate operation from the field structure; it is defined in terms of the order, and the order is defined in terms of the field structure together with the completeness axiom.

### The Vector Part and $\mathbb{R}^1$

There is no vector part. The real numbers are one-dimensional over themselves, and the scalar part exhausts the element. The product of two real numbers is

$$
q_1 \cdot q_2 = q_1 q_2,
$$

which has no dot product and no cross product, because there is no vector part. The field multiplication is the only operation, and it is commutative.

## Real Algebra

### Definition

The **real algebra** is the field $\mathbb{R}$ considered as a one-dimensional real vector space equipped with its field multiplication. As a real vector space, $\mathbb{R}$ has dimension $1$. As a ring, it is a field. A general element is written in developed form as

$$
q = q \cdot 1, \qquad q \in \mathbb{R},
$$

or, more compactly, as

$$
q \in \mathbb{R}.
$$

We write

$$
q = q \cdot 1,
$$

where $q$ is the **scalar part** and there is no vector part.

### Multiplication

The product of two real numbers is defined by the field multiplication:

$$
q_1 \cdot q_2 = q_1 q_2, \qquad q_1, q_2 \in \mathbb{R}.
$$

In developed form,

$$
q_1 \cdot q_2 = (q_1)(q_2),
$$

where the product $q_1 q_2$ is that of the real field.

### Conjugations

There is **one** natural conjugation on $\mathbb{R}$, and it is trivial: the identity map.

**Identity conjugation** $\operatorname{id}$:

$$
\operatorname{id}(q) = q.
$$

There is no complex conjugation, no Hermitian conjugation, and no anti-Hermitian conjugation. The real numbers are totally ordered and totally real; there is no room for a nontrivial involution that preserves the field structure.

The identity is an involution: applying it twice returns the original real number. Its fixed-point set is all of $\mathbb{R}$, which is a real vector subspace of $\mathbb{R}$ of dimension $1$.

## The One Fixed-Point Subspace

The identity conjugation has a fixed-point set, namely all of $\mathbb{R}$. This fixed-point set is a real vector subspace of $\mathbb{R}$. It is described below.

### The Real Subspace

The fixed points of the **identity conjugation** are the real numbers satisfying $\operatorname{id}(q) = q$. In developed form,

$$
q = q.
$$

Comparing the coefficients of $1$:

- Coefficient of $1$: $q = q$, always satisfied.

The fixed points are all real numbers:

$$
q = q \cdot 1, \qquad q \in \mathbb{R}.
$$

This is the **real subspace** $\mathbb{R}_{\mathbb{R}}$, a copy of the real number line embedded in $\mathbb{R}$ as the whole thing. It is a real vector space of dimension $1$. It is a subalgebra of $\mathbb{R}$ (isomorphic to $\mathbb{R}$), and it is commutative.

It is the only one of the fixed-point sets that is a division algebra, because it is the only fixed-point set.

## Real Decomposition

There is no nontrivial decomposition of $\mathbb{R}$ associated with a conjugation, because the only conjugation is the identity. Every real number can be written uniquely as

$$
q = q_r,
$$

where $q_r$ is an **ordinary real number**, with real coefficient. The component is

$$
q_r = \frac{1}{2}(q + q) = q.
$$

Indeed, $q_r$ is fixed by the identity conjugation, so it lies in the real subspace $\mathbb{R}_{\mathbb{R}}$. The sum is $q_r = q$.

This gives the direct sum decomposition

$$
\mathbb{R} = \mathbb{R}_{\mathbb{R}},
$$

where $\mathbb{R}_{\mathbb{R}}$ is the real subspace. It is a real vector space of dimension $1$, and its direct sum is the full algebra $\mathbb{R}$ of real dimension $1$.

This is the **real decomposition** of a real number. It expresses $q$ as a real number. It is the natural decomposition when we think of $\mathbb{R}$ as the realification of $\mathbb{R}$.

## Hermitian Decomposition

There is no Hermitian subspace and no anti-Hermitian subspace, because there is no Hermitian conjugation. The decomposition

$$
\mathbb{R} = \mathbb{M}_+ \oplus \mathbb{M}_-
$$

does not exist, because $\mathbb{M}_+$ and $\mathbb{M}_-$ are not defined. There is only one subspace, and it is the whole algebra.

## Order-Theoretic Structure

The order on $\mathbb{R}$ is not merely a binary relation. It interacts with the field operations and with completeness in ways that have no analogue in an unordered field.

### Intervals

For $a, b \in \mathbb{R}$ with $a \leq b$:

$$
[a, b] = \{c \in \mathbb{R} : a \leq c \leq b\}, \qquad (a, b) = \{c \in \mathbb{R} : a < c < b\},
$$

$$
[a, b) = \{c \in \mathbb{R} : a \leq c < b\}, \qquad (a, b] = \{c \in \mathbb{R} : a < c \leq b\}.
$$

Intervals are the convex subsets of $\mathbb{R}$: a set $S \subseteq \mathbb{R}$ is an interval iff for all $a, b \in S$ with $a < b$, every $c$ with $a < c < b$ lies in $S$.

### Bounds

A set $S \subseteq \mathbb{R}$ is **bounded above** if there exists $M \in \mathbb{R}$ with $q \leq M$ for all $q \in S$. Such an $M$ is an **upper bound**. The **supremum** $\sup S$ is the least upper bound, and it exists by completeness whenever $S$ is non-empty and bounded above.

Dually, $S$ is **bounded below** if there exists $m \in \mathbb{R}$ with $m \leq q$ for all $q \in S$, and the **infimum** $\inf S$ is the greatest lower bound.

### The Completeness Consequences

Completeness is the axiom that distinguishes $\mathbb{R}$ from $\mathbb{Q}$. Its consequences are:

**Archimedean property.** For any $a \in \mathbb{R}$, there exists $n \in \mathbb{N}$ with $n > a$. Proof: if not, $\mathbb{N}$ is bounded above, so $\sup \mathbb{N}$ exists; then $\sup \mathbb{N} - 1$ is not an upper bound, so some $n > \sup \mathbb{N} - 1$, hence $n + 1 > \sup \mathbb{N}$, contradiction.

**Density of $\mathbb{Q}$.** For any $q_1, q_2 \in \mathbb{R}$ with $q_1 < q_2$, there exists $q \in \mathbb{Q}$ with $q_1 < q < q_2$. Proof: by Archimedes, choose $n$ with $n(q_2 - q_1) > 1$; then choose $m$ with $m > n q_1$ minimal; then $m/n \in (q_1, q_2)$.

**Existence of $n$-th roots.** For any $q_1 \geq 0$ and any $n \geq 1$, there exists a unique $q_2 \geq 0$ with $q_2^n = q_1$. Proof: let $S = \{c \geq 0 : c^n \leq q_1\}$; $S$ is non-empty and bounded above, so $q_2 = \sup S$ exists; one shows $q_2^n = q_1$ by excluding $q_2^n < q_1$ and $q_2^n > q_1$.

**Nested interval property.** If $(I_n)$ is a decreasing sequence of non-empty closed intervals, then $\bigcap_n I_n \neq \emptyset$. Proof: the left endpoints form a set bounded above, whose supremum lies in every $I_n$.

### The Nested Interval Property and Uniqueness

The completeness axiom, which is the least upper bound property stated as an axiom above, is equivalent to the nested interval property and, in the metric reading, to the convergence of Cauchy sequences. These equivalences are not trivial; they are the content of the standard constructions of $\mathbb{R}$ from $\mathbb{Q}$. Only the order-theoretic form of them is used here: the metric reading is the topological development of *Real Topology*.

The **uniqueness** of $\mathbb{R}$ as a complete ordered field is a theorem: if $F$ is any complete ordered field, there is a unique order-isomorphism $F \to \mathbb{R}$. This is why we speak of *the* real numbers.

### Real Closedness

**Definition.** An ordered field $F$ is **real closed** if every positive element of $F$ is a square in $F$ and every polynomial of odd degree over $F$ has a root in $F$.

**Theorem.** $\mathbb{R}$ is real closed. It is the unique ordered field that is complete, and its order is the only order compatible with its field structure.

An ordered field that is real closed has a unique ordering, since the positive elements are exactly the nonzero squares; and it has no proper ordered algebraic extension, so it coincides with its own real closure. Every ordered subfield $F \subsetneq \mathbb{R}$ is Archimedean, because $\mathbb{R}$ is, and has a **real closure** inside $\mathbb{R}$, namely the field of its elements algebraic over $F$ in the sense of field theory; this is the smallest real-closed subfield of $\mathbb{R}$ containing $F$. In particular $\overline{\mathbb{Q}} \cap \mathbb{R}$, the field of real algebraic numbers, is the real closure of $\mathbb{Q}$ inside $\mathbb{R}$.

**Remark.** Real closedness is a field-theoretic property, and its proof from completeness is carried out in *Real-Closed and Complete Ordered Fields*. It is recorded here because the ordered-field structure of the real algebra is not complete without it: the order and the field structure of $\mathbb{R}$ determine one another.

## Summary

The real algebra is the field $\mathbb{R}$ of real numbers considered as a one-dimensional real vector space equipped with its field multiplication. It is the base case of the ladder: commutative, associative and unital, and a field, so that every nonzero element is invertible. It is the only system of the family that also carries a total order compatible with its operations.

The only conjugation is the identity. Its fixed-point set is all of $\mathbb{R}$, so the single fixed-point subspace is $\mathbb{R}$ itself. There is no nontrivial conjugate decomposition, because the eigenspace for the eigenvalue $-1$ is zero, and there is no Hermitian or anti-Hermitian subspace, because there is no Hermitian conjugation: the decomposition of the general case collapses to a single summand.

The order is total, Archimedean and complete, and it interacts with the field operations in ways that have no analogue in an unordered field: the positive cone determines the order, and completeness supplies the least upper bound, the Archimedean property, the density of $\mathbb{Q}$, the existence of $n$-th roots and the nested interval property. The field is real closed — every positive element is a square, every odd-degree polynomial has a root, and the order is the only one compatible with the field structure. The norm, the Hermitian form and the inner product are a form and a distance rather than algebraic data, and they are carried by *Real Norm and Invertibility*, the topology entry of this category.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}$ | Real number field |
| $1$ | Identity |
| $q$ | General real number |
| $q$ | Real coefficient |
| $q$ | Scalar part |
| $\operatorname{id}(q) = q$ | Identity conjugation |
| $\mathbb{R}_{\mathbb{R}}$ | Real subspace, fixed-point set of $\operatorname{id}$ |
| $\mathbb{R}_{\geq 0}$ | Positive cone (the non-negative reals) |
| $[a, b], (a, b)$ | Closed and open intervals |
| $\sup S, \inf S$ | Supremum and infimum |

## Further Reading

- Richard Dedekind, *Stetigkeit und irrationale Zahlen* (1872), for the construction of $\mathbb{R}$ by cuts.
- Georg Cantor, "Über die Ausdehnung eines Satzes aus der Theorie der trigonometrischen Reihen" (1872), for the construction by Cauchy sequences.
- Edmund Landau, *Grundlagen der Analysis* (1930), for the axiomatic treatment.
- Walter Rudin, *Principles of Mathematical Analysis* (McGraw-Hill, 1976), for the standard modern treatment.
- John H. Conway, *On Numbers and Games* (Academic Press, 1976), for the construction by surreal numbers.

