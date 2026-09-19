
# __Orthogonal Transformations__

## Introduction

This article introduces orthogonal transformations. The treatment is introductory and purely mathematical.

An orthogonal transformation is a linear transformation that preserves a quadratic form. The goal of this article is to explain what this means, why it is natural, and how the orthogonal transformations of a given quadratic form organize themselves into a group.

We assume familiarity with modules, bilinear forms, and quadratic forms, as developed in the preceding articles. No prior knowledge of Lie algebras or Clifford algebras is required.

This article treats the general theory, over a **commutative ring** in which 2 is invertible. The examples over specific rings, including the signature over $\mathbb{R}$, the Cartan–Dieudonné theorem, and the hyperbolic transformations, are the subject of the following article.

A word on the base structure. The classical theory of orthogonal transformations assumes that the scalars form a field. But the definition and many of the basic properties carry over to the more general setting where the scalars form a **commutative ring**. This is the setting we adopt here. The main differences from the field case are:

- Modules over a commutative ring need not be free, so the orthogonal group need not be a matrix group. We assume the module is free of finite rank.
- Invertibility of a linear transformation requires the determinant to be a **unit** of the ring, not merely nonzero.
- The determinant takes values in the ring, and its square is 1 only up to units. So the determinant map is not as clean as over a field.
- The theory of Lie algebras over a general commutative ring is more subtle than over a field.

We indicate where these differences matter.

---

## Part I: The Definition

### Preserving a Quadratic Form

Let $M$ be a free module of finite rank over a commutative ring $R$ in which 2 is invertible, equipped with a quadratic form $Q$. A linear transformation $T : M \to M$ is **orthogonal** with respect to $Q$ if it preserves $Q$:

$$
Q(Tv) = Q(v) \quad \text{for all } v \in M.
$$

Equivalently, using the bilinear form $B$ associated with $Q$:

$$
B(Tu, Tv) = B(u, v) \quad \text{for all } u, v \in M.
$$

The two conditions are equivalent because $Q(v) = B(v, v)$ and $B$ is recovered from $Q$ by polarization. The polarization identity requires that 2 is invertible in $R$.

### The Orthogonal Group

The set of all orthogonal transformations of $Q$ forms a group under composition. It is called the **orthogonal group** of $Q$ and is written

$$
O(M, Q).
$$

It is a subgroup of the general linear group $GL(M)$. To verify that it is a subgroup:

- The identity is orthogonal.
- If $S$ and $T$ are orthogonal, then $Q(STv) = Q(Tv) = Q(v)$, so $ST$ is orthogonal.
- If $T$ is orthogonal, then $Q(T^{-1}v) = Q(T(T^{-1}v)) = Q(v)$, so $T^{-1}$ is orthogonal.

So $O(M, Q)$ is a group.

**Key difference from the field case.** Over a field, $GL(M)$ consists of the invertible linear transformations, and "invertible" is equivalent to "nonzero determinant." Over a general commutative ring, $GL(M)$ consists of the linear transformations whose determinant is a **unit** of $R$. So the orthogonal group $O(M, Q)$ is a subgroup of $GL(M)$ in the ring-theoretic sense, which is more restrictive than over a field.

### The Rotation Group

Let $M$ be free of finite rank with $Q$ **non-degenerate**, so that the Gram matrix of $B$ is invertible. For any orthogonal transformation $T$, the determinant satisfies

$$
\det(T)^2 = 1.
$$

(Write the condition $B(Tu, Tv) = B(u, v)$ as $T^T G T = G$ for the Gram matrix $G$; since $\det G$ is a unit, taking determinants gives $\det(T)^2 = 1$.) Over a field of characteristic not equal to 2, this means $\det T = +1$ or $\det T = -1$.

Non-degeneracy is needed here: with $Q = 0$ every linear transformation preserves $Q$, and $\det(T)^2 = 1$ fails for $T = 2\,\mathrm{id}$. The set of orthogonal transformations with determinant $+1$ is a subgroup, called the **special orthogonal group** or **rotation group**:

$$
SO(M, Q) = \{T \in O(M, Q) : \det T = +1\}.
$$

The rotation group is the kernel of the determinant map restricted to $O(M, Q)$:

$$
\det : O(M, Q) \to \{+1, -1\}.
$$

So $SO(M, Q)$ is a normal subgroup of $O(M, Q)$, and the quotient $O(M, Q)/SO(M, Q)$ is the image of the determinant map. Over a field that image has order $1$ or $2$, but over a general commutative ring it can be larger: for $R = \mathbb{R} \times \mathbb{R}$ with $M = R$ and $Q(x) = x^2$, the orthogonal transformations are multiplication by $a$ with $a^2 = 1$, so $O(M, Q) \cong \mathbb{Z}/2 \times \mathbb{Z}/2$ while $SO(M, Q)$ is trivial, and the quotient has four elements.

**Key difference from the field case.** Over a field, the equation $\det(T)^2 = 1$ has exactly two solutions, $+1$ and $-1$, provided the field has characteristic not equal to 2. Over a general commutative ring, the equation $\det(T)^2 = 1$ may have many more solutions, and the determinant map may not be surjective onto $\{+1, -1\}$. So the definition of $SO(M, Q)$ as the kernel of the determinant map is still valid, but the structure of the quotient $O(M, Q) / SO(M, Q)$ may be more complicated than $\{+1, -1\}$.

---

## Part II: The Orthogonal Lie Algebra

### The Definition

The orthogonal group $O(M, Q)$ is a continuous group for a non-degenerate quadratic form over the real or complex numbers. Its infinitesimal version is the **orthogonal Lie algebra** $\mathfrak{so}(M, Q)$, defined as the set of linear transformations $A : M \to M$ that are **antisymmetric** with respect to $B$:

$$
B(Au, v) + B(u, Av) = 0 \quad \text{for all } u, v \in M.
$$

### The Lie Bracket

The set $\mathfrak{so}(M, Q)$ is a module over $R$. It is closed under the **commutator bracket**

$$
[A, C] = AC - CA.
$$

Indeed, if $A$ and $C$ are antisymmetric, then $[A, C]$ is antisymmetric:

$$
B([A, C]u, v) + B(u, [A, C]v) = 0.
$$

So $\mathfrak{so}(M, Q)$ is a Lie algebra under the commutator bracket.

### The Rank

For a free module of rank $n$ with $Q$ **non-degenerate**, the orthogonal Lie algebra has rank

$$
\operatorname{rank} \mathfrak{so}(M, Q) = \binom{n}{2} = \frac{n(n-1)}{2}.
$$

Multiplication by the invertible Gram matrix of $B$ identifies $\mathfrak{so}(M, Q)$ with the antisymmetric matrices, whose rank is $\binom{n}{2}$; this is the number of independent antisymmetric transformations. The rank does not depend on the ring or on the signature; only the structure of the Lie algebra depends on them.

Without non-degeneracy the count fails, because the condition $B(Au, v) + B(u, Av) = 0$ can become vacuous: for $Q = 0$ it holds for every $A$, so $\mathfrak{so}(M, 0)$ is all of $\operatorname{End}(M)$, of rank $n^2$.

**Key difference from the field case.** Over a field, the rank of $\mathfrak{so}(M, Q)$ is the dimension, and it is well-defined. Over a general commutative ring, the rank is well-defined only if the module is free. We assume this throughout.

### The Exponential Map

For a non-degenerate quadratic form over $\mathbb{R}$ or $\mathbb{C}$, the **exponential map** sends $\mathfrak{so}(M, Q)$ to $SO(M, Q)$: if $A \in \mathfrak{so}(M, Q)$, then $\exp(A) \in SO(M, Q)$.

The exponential map is not surjective in general, but its image contains the connected component of the identity in $SO(M, Q)$.

**Key difference from the field case.** The exponential map is defined over $\mathbb{R}$ or $\mathbb{C}$, where the notion of convergence makes sense. Over a general commutative ring, the exponential map is not defined in the same way, because there is no topology. So the relationship between the Lie algebra and the group is more subtle over a general commutative ring.

---

## Part III: Summary

Let me summarize the main points.

**An orthogonal transformation** of a quadratic form $Q$ is a linear transformation $T$ that preserves $Q$: $Q(Tv) = Q(v)$ for all $v$. Equivalently, $B(Tu, Tv) = B(u, v)$ for all $u, v$.

**The orthogonal group** $O(M, Q)$ is the group of all orthogonal transformations of $Q$. It is a subgroup of $GL(M)$.

**The rotation group** $SO(M, Q)$ is the subgroup of orthogonal transformations with determinant $+1$. It is the kernel of the determinant map on $O(M, Q)$.

**The orthogonal Lie algebra** $\mathfrak{so}(M, Q)$ is the set of antisymmetric linear transformations with respect to the bilinear form $B$. For non-degenerate $Q$ on a free module of rank $n$ its rank is $\binom{n}{2}$. The exponential map sends $\mathfrak{so}(M, Q)$ to $SO(M, Q)$ over $\mathbb{R}$ or $\mathbb{C}$.

**Key differences from the field case.**

- Over a field, every module is free, so the orthogonal group is a matrix group. Over a general commutative ring, the module need not be free.
- Over a field, invertibility is equivalent to nonzero determinant. Over a general commutative ring, invertibility requires the determinant to be a unit.
- Over a field of characteristic not equal to 2, the equation $\det(T)^2 = 1$ has exactly two solutions. Over a general commutative ring, it may have more.
- The exponential map is defined over $\mathbb{R}$ or $\mathbb{C}$, where there is a topology. Over a general commutative ring, it is not defined in the same way.

The examples over specific rings, including the signature over $\mathbb{R}$, the Cartan–Dieudonné theorem, and the hyperbolic transformations, are the subject of the following article.

---

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991), for an introduction to bilinear forms and orthogonal groups.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for a more advanced treatment.
- I. N. Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for a classic introduction.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for a modern introduction.
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for a thorough treatment.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1971), for the Cartan–Dieudonné theorem and the structure of classical groups.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for the theory over commutative rings.


