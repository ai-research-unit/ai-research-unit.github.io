
# __Vector Space Transformations__

## Introduction

This article introduces transformations of vector spaces and modules. The treatment is introductory and purely mathematical. The goal is to explain what a transformation is, how transformations compose, and how a group of transformations is defined.

We assume familiarity with vector spaces and modules, as developed in the preceding article. No prior knowledge of groups, quadratic forms, Lie algebras, or Clifford algebras is required.

Throughout this article, we work over a **commutative ring** $R$, not necessarily a field. When $R$ is a field, the theory reduces to the classical theory of vector space transformations. When $R$ is a commutative ring with zero divisors (such as $\mathbb{D}$), some definitions require care, and we indicate where this happens.

---

## Part I: Transformations

### The Definition

Let $M$ be a module over a commutative ring $R$. A **transformation** of $M$ is a function

$$
T : M \to M
$$

that is **$R$-linear**:

$$
T(u + v) = T(u) + T(v) \qquad \text{for all } u, v \in M,
$$

$$
T(r v) = r T(v) \qquad \text{for all } r \in R \text{ and } v \in M.
$$

In words: a transformation is a function from $M$ to itself that respects addition and scalar multiplication.

When $R$ is a field, a transformation is exactly a linear map from a vector space to itself.

### Examples

**The identity.** The function $I : M \to M$ defined by $I(v) = v$ is a transformation. It sends every vector to itself.

**The zero transformation.** The function $0 : M \to M$ defined by $0(v) = 0$ is a transformation. It sends every vector to the zero vector.

**Scalar multiplication.** For a fixed scalar $r \in R$, the function $v \mapsto r v$ is a transformation.

**Rotation of the plane.** On $M = \mathbb{R}^2$, the function

$$
(x, y) \mapsto (x \cos\theta - y \sin\theta, \quad x \sin\theta + y \cos\theta)
$$

is a transformation. It rotates the plane by angle $\theta$.

**Reflection of the plane.** On $M = \mathbb{R}^2$, the function

$$
(x, y) \mapsto (x, -y)
$$

is a transformation. It reflects the plane across the $x$-axis.

**Matrix multiplication.** On $M = R^n$, any $n \times n$ matrix $M$ with entries in $R$ defines a transformation by

$$
v \mapsto Mv.
$$

In fact, every transformation of $R^n$ arises in this way from a unique matrix. This holds over any commutative ring $R$, not just over a field.

### Composition

If $S$ and $T$ are transformations of $M$, their **composition** $S \circ T$ is defined by

$$
(S \circ T)(v) = S(T(v)).
$$

The composition of two transformations is again a transformation: it is $R$-linear, because $S$ and $T$ are $R$-linear.

Composition is **associative**:

$$
(R \circ S) \circ T = R \circ (S \circ T).
$$

Composition is **not commutative** in general: $S \circ T$ and $T \circ S$ may be different.

The identity transformation $I$ satisfies

$$
I \circ T = T \circ I = T
$$

for every transformation $T$. So $I$ is the unit for composition.

### Invertible Transformations

A transformation $T$ is **invertible** if there exists a transformation $T^{-1}$ such that

$$
T \circ T^{-1} = T^{-1} \circ T = I.
$$

If $T$ is invertible, then $T^{-1}$ is unique, and it is called the **inverse** of $T$.

Not every transformation is invertible. The zero transformation is not invertible. Scalar multiplication by $0$ is not invertible. A rotation of the plane is invertible, and its inverse is the rotation by $-\theta$. A reflection is invertible, and it is its own inverse.

Over a commutative ring $R$, a transformation may fail to be invertible even if its "determinant" is nonzero, because the determinant must be a **unit** of $R$, not merely nonzero. We discuss this in the next section.

### The Determinant

Let $M = R^n$ be a free module of rank $n$ over a commutative ring $R$. Choose a basis $e_1, \ldots, e_n$ of $M$. A transformation $T$ is determined by its matrix $A$ with respect to this basis. The **determinant** of $T$ is the determinant of the matrix $A$:

$$
\det T = \det A.
$$

This is well-defined: it does not depend on the choice of basis. It is a function

$$
\det : \operatorname{End}_R(M) \to R,
$$

where $\operatorname{End}_R(M)$ is the ring of $R$-linear transformations of $M$. The determinant is multiplicative:

$$
\det(ST) = (\det S)(\det T).
$$

**Key difference from the field case.** Over a field, a transformation is invertible if and only if its determinant is nonzero. Over a commutative ring, a transformation is invertible if and only if its determinant is a **unit** of $R$. This is because a matrix over a ring is invertible if and only if its determinant is a unit.

For example, over $R = \mathbb{Z}$, the matrix $\begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ has determinant $2$, which is nonzero but not a unit. So it is not invertible as a $\mathbb{Z}$-linear transformation of $\mathbb{Z}^2$.

For example, over $R = \mathbb{D}$, the matrix $\begin{pmatrix} 1 + e & 0 \\ 0 & 1 \end{pmatrix}$ has determinant $1 + e$, which is nonzero but not a unit. So it is not invertible as a $\mathbb{D}$-linear transformation of $\mathbb{D}^2$.

---

## Part II: Groups of Transformations

### The Group of Invertible Transformations

The set of all invertible transformations of a free module $M$ of rank $n$ over a commutative ring $R$ forms a group under composition. This group is called the **general linear group** of $M$, written

$$
GL(M).
$$

The group operation is composition. The identity is the identity transformation. The inverse of a transformation is its inverse.

If $M = R^n$, then $GL(M)$ is written $GL(n, R)$, and it is the group of $n \times n$ invertible matrices with entries in $R$.

Over a field $F$, the group $GL(n, F)$ consists of the matrices with nonzero determinant. Over a general commutative ring $R$, the group $GL(n, R)$ consists of the matrices whose determinant is a **unit** of $R$. This is a crucial difference.

### Subgroups

A **subgroup** of $GL(M)$ is a subset $G \subseteq GL(M)$ such that:

1. The identity $I$ is in $G$.
2. If $S, T \in G$, then $S \circ T \in G$.
3. If $T \in G$, then $T^{-1} \in G$.

In words: a subgroup is a subset that is closed under composition and inverses, and contains the identity.

### Examples of Subgroups

**The special linear group.** The set of invertible transformations with determinant $1$ is a subgroup of $GL(M)$. It is written $SL(M)$, or $SL(n, R)$ if $M = R^n$. It is a subgroup because the determinant is multiplicative:

$$
\det(ST) = (\det S)(\det T),
$$

so if $\det S = \det T = 1$, then $\det(ST) = 1$; and if $\det T = 1$, then $\det T^{-1} = 1$.

Note that the definition of $SL(n, R)$ makes sense over any commutative ring $R$, not just over a field. The condition is $\det T = 1$, which is meaningful in any ring.

**The group of scalar multiplications.** The set of transformations of the form $v \mapsto r v$ for $r \in R^\times$ (a unit of $R$) is a subgroup of $GL(M)$. It is isomorphic to the group of units $R^\times$ under multiplication.

Over a field $F$, the units are $F^\times = F \setminus \{0\}$. Over a general commutative ring $R$, the units $R^\times$ may be a proper subset of $R \setminus \{0\}$. For example, over $\mathbb{Z}$, the units are $\{\pm 1\}$. Over $\mathbb{D}$, the units are the elements $a + be$ with $a^2 - b^2 \neq 0$.

**The group generated by a single transformation.** If $T$ is an invertible transformation, the set of all powers of $T$,

$$
\{ \ldots, T^{-2}, T^{-1}, I, T, T^2, \ldots \},
$$

is a subgroup of $GL(M)$. It is called the **cyclic subgroup generated by $T$**.

---

## Part III: Actions of Groups on Sets

### The Definition

Let $G$ be a group and $X$ a set. An **action** of $G$ on $X$ is a function

$$
G \times X \to X, \qquad (g, x) \mapsto g \cdot x
$$

such that:

1. **Identity:** $e \cdot x = x$ for all $x \in X$, where $e$ is the identity of $G$.
2. **Compatibility:** $(gh) \cdot x = g \cdot (h \cdot x)$ for all $g, h \in G$ and $x \in X$.

In words: an action is a rule that assigns to each group element a transformation of $X$, in a way that respects the group structure.

### Examples

**The trivial action.** Every group acts trivially on any set by $g \cdot x = x$ for all $g$ and $x$.

**The action of $GL(M)$ on $M$.** The general linear group $GL(M)$ acts on $M$ by $T \cdot v = T(v)$. This is the standard action.

**The action of a group on itself.** Every group $G$ acts on itself by left multiplication: $g \cdot h = gh$.

### Why Actions Matter

An action of a group $G$ on a set $X$ is a way of representing the group as a group of transformations of $X$. In many cases, the group $G$ is abstract, and the action is what makes it concrete: it tells you what the group does.

---

## Part IV: Linear Actions

### Representations

If $G$ is a group and $M$ is a module over a commutative ring $R$, a **representation** of $G$ on $M$ is an action of $G$ on $M$ such that each $g \in G$ acts by an $R$-linear transformation of $M$. In other words, it is a group homomorphism

$$
\rho : G \to GL(M).
$$

The module $M$ is called the **representation space**. The elements of $M$ are the **vectors of the representation**.

Over a field, this is the classical theory of group representations. Over a general commutative ring, the theory is more subtle, because $GL(M)$ may be a smaller group (since invertibility requires the determinant to be a unit).

### Examples

**The standard representation of $GL(M)$.** The identity map $GL(M) \to GL(M)$ is a representation of $GL(M)$ on $M$.

**The trivial representation.** The map $g \mapsto I$ for all $g \in G$ is a representation of $G$ on any module $M$. It is the trivial representation.

**The action of a cyclic group.** If $G$ is the cyclic group generated by an invertible transformation $T$, then $G$ acts on $M$ by powers of $T$. This is a representation of $G$ on $M$.

### Why Representations Matter

A representation is a way of making a group act linearly on a module. This is useful because modules and transformations are well understood. If you can represent a group as a group of matrices, you can use the tools of linear algebra to study the group.

Over a commutative ring, the theory of representations is more subtle than over a field, but many of the basic ideas carry over.

---

## Part V: Summary

Let me summarize the main points.

**A transformation** of a module $M$ over a commutative ring $R$ is an $R$-linear function $T : M \to M$. Transformations compose, and composition is associative but not commutative.

**An invertible transformation** is one that has an inverse. Over a commutative ring, a transformation is invertible if and only if its determinant is a **unit** of $R$. The invertible transformations form a group under composition, called the general linear group $GL(M)$.

**The determinant** is a function $\det : \operatorname{End}_R(M) \to R$, defined for free modules of finite rank. It is multiplicative: $\det(ST) = (\det S)(\det T)$. Over a field, invertibility is equivalent to nonzero determinant; over a general commutative ring, it is equivalent to the determinant being a unit.

**A subgroup** of $GL(M)$ is a subset closed under composition and inverses, containing the identity. Examples include $SL(M)$, the group of scalar multiplications by units, and the cyclic subgroups.

**An action** of a group $G$ on a set $X$ is a rule that assigns to each $g \in G$ a transformation of $X$, respecting the group structure.

**A representation** of a group $G$ on a module $M$ is an action of $G$ on $M$ such that each $g$ acts by an $R$-linear transformation of $M$. Equivalently, it is a homomorphism $G \to GL(M)$.

**Key difference from the field case.** Over a field, every nonzero scalar is a unit, so invertibility is equivalent to nonzero determinant. Over a general commutative ring, the units may be a proper subset of the nonzero elements, so invertibility requires the determinant to be a unit. This is the main modification needed to extend the theory from fields to commutative rings.

---

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991), for an introduction to groups, transformations, and representations.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for a more advanced treatment.
- I. N. Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for a classic introduction to group theory and transformations.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for a modern introduction to groups and their actions.
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for a thorough treatment of transformations and groups.
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for a comprehensive treatment of groups, rings, and modules.
- Thomas W. Hungerford, *Algebra* (Springer, 1974), for a graduate-level treatment of algebra.

