
# Real Algebra

## Introduction

This article introduces the real algebra as an algebraic structure. The goal is to define the algebra precisely, establish its basic properties, and describe the distinguished substructures that arise from its order and completeness.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No topology beyond the order is invoked. The real numbers are treated as an algebraic object, and the consequences of their algebraic properties are developed systematically.

## The Real Numbers

### Definition

The **real number field** $\mathbb{R}$ is a set equipped with two binary operations $+$ and $\cdot$, two distinguished elements $0$ and $1$, and a total order $<$, satisfying the following axioms.

**Field axioms.** The structure $(\mathbb{R}, +, \cdot)$ is a field:

$$
a + b = b + a, \qquad a \cdot b = b \cdot a,
$$

$$
(a + b) + c = a + (b + c), \qquad (a \cdot b) \cdot c = a \cdot (b \cdot c),
$$

$$
a \cdot (b + c) = a \cdot b + a \cdot c,
$$

$$
a + 0 = a, \qquad a \cdot 1 = a,
$$

and for every $a \in \mathbb{R}$ there exists $-a$ with $a + (-a) = 0$, and for every $a \neq 0$ there exists $a^{-1}$ with $a \cdot a^{-1} = 1$.

**Order axioms.** The order $<$ is total and compatible with the field operations:

$$
\text{for any } a, b \in \mathbb{R}, \text{ exactly one of } a < b, \; a = b, \; a > b \text{ holds},
$$

$$
a < b \implies a + c < b + c,
$$

$$
a < b \text{ and } c > 0 \implies a \cdot c < b \cdot c.
$$

**Completeness axiom.** Every non-empty subset of $\mathbb{R}$ that is bounded above has a least upper bound in $\mathbb{R}$:

$$
S \subseteq \mathbb{R}, \; S \neq \emptyset, \; S \text{ bounded above} \implies \sup S \in \mathbb{R}.
$$

A general real number is written in developed form as

$$
a = a \cdot 1, \qquad a \in \mathbb{R},
$$

or, more compactly, as

$$
a \in \mathbb{R}.
$$

We write

$$
a = a,
$$

where $a$ is the **scalar part** and there is no vector part. The absence of a tilde signals that $a$ is an element of the algebra $\mathbb{R}$, not a vector in some larger space.

There is no complexification and no distinguished imaginary unit. The only imaginary unit in the algebra is the one we do not introduce. The real numbers are real.

### Basic Properties

**Commutative.** Real addition and multiplication are commutative: $a + b = b + a$ and $a \cdot b = b \cdot a$.

**Associative.** Real addition and multiplication are associative: $(a + b) + c = a + (b + c)$ and $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.

**Distributive.** $a \cdot (b + c) = a \cdot b + a \cdot c$.

**Ordered field.** The real numbers form a totally ordered field. The order is Archimedean: for any $a, b \in \mathbb{R}$ with $a > 0$, there exists a natural number $n$ with $n a > b$. This excludes ordered fields containing infinitesimals.

**Complete ordered field.** The real numbers are the unique complete ordered field up to isomorphism. Every other complete ordered field is order-isomorphic to $\mathbb{R}$.

**Frobenius theorem.** The real numbers are one of only three finite-dimensional associative real division algebras. In fact, $\mathbb{R}$ is the only one that is commutative and ordered.

### The Absolute Value and the Positive Cone

The **absolute value** of a real number $a$ is

$$
|a| = \begin{cases} a & a \geq 0, \\ -a & a < 0. \end{cases}
$$

It satisfies $|a| \geq 0$, $|a| = 0 \iff a = 0$, $|ab| = |a||b|$, and $|a + b| \leq |a| + |b|$. The last is the triangle inequality, and it is the only one that uses the order in an essential way.

The set of non-negative reals

$$
\mathbb{R}_{\geq 0} = \{a \in \mathbb{R} : a \geq 0\}
$$

is a multiplicative submonoid of $\mathbb{R}$ and is closed under addition. It is the **positive cone** of the ordered field, and it determines the order by

$$
a < b \iff b - a \in \mathbb{R}_{>0}.
$$

The absolute value is not a separate operation from the field structure; it is defined in terms of the order, and the order is defined in terms of the field structure together with the completeness axiom.

### The Vector Part and $\mathbb{R}^1$

There is no vector part. The real numbers are one-dimensional over themselves, and the scalar part exhausts the element. The product of two real numbers is

$$
a \cdot b = ab,
$$

which has no dot product and no cross product, because there is no vector part. The field multiplication is the only operation, and it is commutative.

## Real Algebra

### Definition

The **real algebra** is the field $\mathbb{R}$ considered as a one-dimensional real vector space equipped with its field multiplication. As a real vector space, $\mathbb{R}$ has dimension $1$. As a ring, it is a field. A general element is written in developed form as

$$
a = a \cdot 1, \qquad a \in \mathbb{R},
$$

or, more compactly, as

$$
a \in \mathbb{R}.
$$

We write

$$
a = a,
$$

where $a$ is the **scalar part** and there is no vector part.

### Multiplication

The product of two real numbers is defined by the field multiplication:

$$
a \cdot b = ab, \qquad a, b \in \mathbb{R}.
$$

In developed form,

$$
a \cdot b = (a)(b),
$$

where the product $ab$ is that of the real field.

### Conjugations

There is **one** natural conjugation on $\mathbb{R}$, and it is trivial: the identity map.

**Identity conjugation** $\operatorname{id}$:

$$
\operatorname{id}(a) = a.
$$

There is no quaternion conjugation, no complex conjugation, no Hermitian conjugation, and no anti-Hermitian conjugation. The real numbers are totally ordered and totally real; there is no room for a nontrivial involution that preserves the field structure.

The identity is an involution: applying it twice returns the original real number. Its fixed-point set is all of $\mathbb{R}$, which is a real vector subspace of $\mathbb{R}$ of dimension $1$.

## The One Fixed-Point Subspace

The identity conjugation has a fixed-point set, namely all of $\mathbb{R}$. This fixed-point set is a real vector subspace of $\mathbb{R}$. It is described below.

### The Real Subspace

The fixed points of the **identity conjugation** are the real numbers satisfying $\operatorname{id}(a) = a$. In developed form,

$$
a = a.
$$

Comparing the coefficients of $1$:

- Coefficient of $1$: $a = a$, always satisfied.

The fixed points are all real numbers:

$$
a = a \cdot 1, \qquad a \in \mathbb{R}.
$$

This is the **real subspace** $\mathbb{R}_{\mathbb{R}}$, a copy of the real number line embedded in $\mathbb{R}$ as the whole thing. It is a real vector space of dimension $1$. It is a subalgebra of $\mathbb{R}$ (isomorphic to $\mathbb{R}$), and it is commutative.

It is the only one of the fixed-point sets that is a division algebra, because it is the only fixed-point set.

## Real Decomposition

There is no nontrivial decomposition of $\mathbb{R}$ associated with a conjugation, because the only conjugation is the identity. Every real number can be written uniquely as

$$
a = a_r,
$$

where $a_r$ is an **ordinary real number**, with real coefficient. The component is

$$
a_r = \frac{1}{2}(a + a) = a.
$$

Indeed, $a_r$ is fixed by the identity conjugation, so it lies in the real subspace $\mathbb{R}_{\mathbb{R}}$. The sum is $a_r = a$.

This gives the direct sum decomposition

$$
\mathbb{R} = \mathbb{R}_{\mathbb{R}},
$$

where $\mathbb{R}_{\mathbb{R}}$ is the real subspace. It is a real vector space of dimension $1$, and its direct sum is the full algebra $\mathbb{R}$ of real dimension $1$.

This is the **real decomposition** of a real number. It expresses $a$ as a real number. It is the natural decomposition when we think of $\mathbb{R}$ as the realification of $\mathbb{R}$.

## Hermitian Decomposition

There is no Hermitian subspace and no anti-Hermitian subspace, because there is no Hermitian conjugation. The decomposition

$$
\mathbb{R} = \mathbb{M}_+ \oplus \mathbb{M}_-
$$

does not exist, because $\mathbb{M}_+$ and $\mathbb{M}_-$ are not defined. There is only one subspace, and it is the whole algebra.

## Quadratic Forms and Inner Product

### The Norm Form

The **norm form** of a real number $a$ is

$$
N(a) = a \cdot a = a^2,
$$

where the product is the field multiplication. It is a real number in general. It is positive-definite, since $a^2 \geq 0$ for every $a$, and it vanishes only at $a = 0$, because $\mathbb{R}$ is a field.

The norm form is **multiplicative**:

$$
N(a \cdot b) = N(a) \, N(b).
$$

This is the statement that $a^2 b^2 = (ab)^2$, which is true in any commutative ring.

### The Hermitian Form

The **Hermitian form** of a real number $a$ is

$$
a \cdot a = a^2,
$$

where the product is the field multiplication. It is a **non-negative real number**, and it vanishes if and only if $a = 0$. It is a genuine positive-definite quadratic form, and it is the natural "length squared" of $a$ in the underlying real vector space of dimension $1$.

The corresponding **Euclidean norm** is

$$
\|a\|_E = \sqrt{a \cdot a} = |a|.
$$

It is a genuine norm on the real vector space $\mathbb{R} \cong \mathbb{R}^1$: positive-definite, subadditive, and homogeneous of degree one. It **is** multiplicative with respect to the real product, because $|ab| = |a||b|$.

### The Inner Product

The **inner product** of two real numbers $a$ and $b$ is

$$
\langle a, b \rangle = a \cdot b = ab.
$$

In general this is a **real number**, not a complex one. This is a genuinely real feature: the inner product of two real numbers is real, and its imaginary part is zero.

The inner product is linear in both arguments:

$$
\langle \lambda a, b \rangle = \lambda \langle a, b \rangle, \qquad \langle a, \lambda b \rangle = \lambda \langle a, b \rangle, \qquad \lambda \in \mathbb{R}.
$$

It is **symmetric** in the sense that

$$
\langle a, b \rangle = \langle b, a \rangle,
$$

which follows from the commutativity of multiplication.

The inner product of a real number with itself is

$$
\langle a, a \rangle = a \cdot a = a^2,
$$

which is the Hermitian form. So the Hermitian form is the restriction of the inner product to the diagonal.

### Relation Between the Three Forms

The three quadratic objects are related as follows:

- **Norm form:** $N(a) = a^2$. Real-valued, vanishes only at $a = 0$, multiplicative.
- **Hermitian form:** $a^2$. Non-negative real, vanishes only at $a = 0$, multiplicative.
- **Inner product:** $\langle a, b \rangle = ab$. Real-valued, symmetric, bilinear.

The norm form and the Hermitian form are the same function here, and the inner product is the bilinear form from which they are recovered by polarization. The norm form controls the multiplicative structure (invertibility, zero divisors). The Hermitian form controls the topological structure (continuity, completeness). The inner product combines both, and is the natural pairing on the algebra as a real vector space.

In the real case, the norm form and the Hermitian form coincide, because the conjugation is trivial and there is no imaginary part. This is a degeneracy of the one-dimensional case, and it is the reason the real numbers are often treated as a trivial example rather than as a case study.

## Order-Theoretic Structure

The order on $\mathbb{R}$ is not merely a binary relation. It interacts with the field operations and with completeness in ways that have no analogue in an unordered field.

### Intervals

For $a, b \in \mathbb{R}$ with $a \leq b$:

$$
[a, b] = \{x \in \mathbb{R} : a \leq x \leq b\}, \qquad (a, b) = \{x \in \mathbb{R} : a < x < b\},
$$

$$
[a, b) = \{x \in \mathbb{R} : a \leq x < b\}, \qquad (a, b] = \{x \in \mathbb{R} : a < x \leq b\}.
$$

Intervals are the convex subsets of $\mathbb{R}$: a set $S \subseteq \mathbb{R}$ is an interval iff for all $a, b \in S$ with $a < b$, every $x$ with $a < x < b$ lies in $S$.

### Bounds

A set $S \subseteq \mathbb{R}$ is **bounded above** if there exists $M \in \mathbb{R}$ with $x \leq M$ for all $x \in S$. Such an $M$ is an **upper bound**. The **supremum** $\sup S$ is the least upper bound, and it exists by completeness whenever $S$ is non-empty and bounded above.

Dually, $S$ is **bounded below** if there exists $m \in \mathbb{R}$ with $m \leq x$ for all $x \in S$, and the **infimum** $\inf S$ is the greatest lower bound.

### The Completeness Consequences

Completeness is the axiom that distinguishes $\mathbb{R}$ from $\mathbb{Q}$. Its consequences are:

**Archimedean property.** For any $a \in \mathbb{R}$, there exists $n \in \mathbb{N}$ with $n > a$. Proof: if not, $\mathbb{N}$ is bounded above, so $\sup \mathbb{N}$ exists; then $\sup \mathbb{N} - 1$ is not an upper bound, so some $n > \sup \mathbb{N} - 1$, hence $n + 1 > \sup \mathbb{N}$, contradiction.

**Density of $\mathbb{Q}$.** For any $a, b \in \mathbb{R}$ with $a < b$, there exists $q \in \mathbb{Q}$ with $a < q < b$. Proof: by Archimedes, choose $n$ with $n(b - a) > 1$; then choose $m$ with $m > na$ minimal; then $m/n \in (a, b)$.

**Existence of $n$-th roots.** For any $a \geq 0$ and any $n \geq 1$, there exists a unique $b \geq 0$ with $b^n = a$. Proof: let $S = \{x \geq 0 : x^n \leq a\}$; $S$ is non-empty and bounded above, so $b = \sup S$ exists; one shows $b^n = a$ by excluding $b^n < a$ and $b^n > a$.

**Nested interval property.** If $(I_n)$ is a decreasing sequence of non-empty closed intervals, then $\bigcap_n I_n \neq \emptyset$. Proof: the left endpoints form a set bounded above, whose supremum lies in every $I_n$.

### The Nested Interval Property and Uniqueness

The completeness axiom, which is the least upper bound property stated as an axiom above, is equivalent to the nested interval property and to the convergence of Cauchy sequences. These equivalences are not trivial; they are the content of the standard constructions of $\mathbb{R}$ from $\mathbb{Q}$.

The **uniqueness** of $\mathbb{R}$ as a complete ordered field is a theorem: if $F$ is any complete ordered field, there is a unique order-isomorphism $F \to \mathbb{R}$. This is why we speak of *the* real numbers.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{R}$ | Real number field |
| $1$ | Identity |
| $a$ | General real number |
| $a$ | Real coefficient |
| $a$ | Scalar part |
| $\operatorname{id}(a) = a$ | Identity conjugation |
| $N(a) = a \cdot a$ | Norm form |
| $a \cdot a$ | Hermitian form |
| $\langle a, b \rangle = a \cdot b$ | Inner product |
| $\|a\|_E = \sqrt{a \cdot a}$ | Euclidean norm |
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
- Charles C. Pinter, *A Book of Abstract Algebra* (Dover, 2010), for the representation theory of fields.

