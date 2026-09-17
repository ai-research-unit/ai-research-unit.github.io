
# __Lie Algebras categorization__

## Introduction

This article gives a classification of Lie algebras, organized by the **commutative ring of scalars**. For each commutative ring, we state the classification of the simplest and most important Lie algebras over that ring.

The general theory of Lie algebras is in the preceding article, *Lie Algebras: A General Introduction*. We assume familiarity with the definitions given there.

We consider four commutative rings, in order of increasing complexity:

- The rational numbers $\mathbb{Q}$, a field.
- The real numbers $\mathbb{R}$, a field.
- The complex numbers $\mathbb{C}$, a field.
- The split complex numbers $\mathbb{D}$, a commutative ring with zero divisors.

For each commutative ring, we state the rank of the Lie algebra over that ring, and describe its structure.

A note on terminology. The first three rings are fields, so the classical theory of Lie algebras over a field applies verbatim. The fourth ring $\mathbb{D}$ is not a field: it is a commutative ring with zero divisors. The theory of Lie algebras over $\mathbb{D}$ is similar to the theory over a field, with the caveat that not every nonzero element is a unit, and that the classical structure theory (solvable, nilpotent, simple Lie algebras) is cleanest over fields of characteristic zero. We indicate where this difference matters.

Throughout this article, we use **rank** rather than **dimension** when speaking of Lie algebras over a general commutative ring, reserving **dimension** for the field case. When the ring is a field, the two notions coincide.

---

# Part I: Lie Algebras over $\mathbb{Q}$

## 1. The Abelian Lie Algebra over $\mathbb{Q}$

Let $\mathfrak{g}$ be any $\mathbb{Q}$-module, and define

$$
[u, v] = 0
$$

for all $u, v \in \mathfrak{g}$. This is a Lie algebra over $\mathbb{Q}$, called the **abelian Lie algebra**. The Jacobi identity is trivially satisfied.

For example, $\mathbb{Q}$ itself with the zero bracket is a one-dimensional abelian Lie algebra over $\mathbb{Q}$.

## 2. The General Linear Lie Algebra $\mathfrak{gl}(n, \mathbb{Q})$

The set $M_n(\mathbb{Q})$ of $n \times n$ matrices with rational entries is an $n^2$-dimensional Lie algebra over $\mathbb{Q}$, with the commutator bracket

$$
[A, B] = AB - BA.
$$

It is called the **general linear Lie algebra over $\mathbb{Q}$** and is written $\mathfrak{gl}(n, \mathbb{Q})$.

The center of $\mathfrak{gl}(n, \mathbb{Q})$ is the set of scalar matrices $\{\lambda I : \lambda \in \mathbb{Q}\}$.

## 3. The Special Linear Lie Algebra $\mathfrak{sl}(n, \mathbb{Q})$

The subspace of $\mathfrak{gl}(n, \mathbb{Q})$ consisting of matrices with trace zero is a Lie subalgebra over $\mathbb{Q}$, written $\mathfrak{sl}(n, \mathbb{Q})$. It is $(n^2 - 1)$-dimensional over $\mathbb{Q}$.

## 4. The Orthogonal Lie Algebra $\mathfrak{so}(n, \mathbb{Q})$

The subspace of $\mathfrak{gl}(n, \mathbb{Q})$ consisting of antisymmetric matrices $A^T = -A$ is a Lie subalgebra over $\mathbb{Q}$, written $\mathfrak{so}(n, \mathbb{Q})$. It is $\binom{n}{2}$-dimensional over $\mathbb{Q}$.

---

# Part II: Lie Algebras over $\mathbb{R}$

## 5. The Abelian Lie Algebra over $\mathbb{R}$

Any real vector space with the zero bracket is an abelian Lie algebra over $\mathbb{R}$. For example, $\mathbb{R}$ itself is a one-dimensional abelian Lie algebra, and $\mathbb{R}^n$ is an $n$-dimensional abelian Lie algebra.

## 6. The General Linear Lie Algebra $\mathfrak{gl}(n, \mathbb{R})$

The set $M_n(\mathbb{R})$ of $n \times n$ real matrices is an $n^2$-dimensional Lie algebra over $\mathbb{R}$, with the commutator bracket

$$
[A, B] = AB - BA.
$$

It is called the **general linear Lie algebra** and is written $\mathfrak{gl}(n, \mathbb{R})$.

## 7. The Special Linear Lie Algebra $\mathfrak{sl}(n, \mathbb{R})$

The subspace of $\mathfrak{gl}(n, \mathbb{R})$ consisting of matrices with trace zero is a Lie subalgebra over $\mathbb{R}$, written $\mathfrak{sl}(n, \mathbb{R})$. It is $(n^2 - 1)$-dimensional.

For $n = 2$, the Lie algebra $\mathfrak{sl}(2, \mathbb{R})$ is three-dimensional. It is the Lie algebra of the group $SL(2, \mathbb{R})$ of area-preserving linear transformations of the plane.

## 8. The Orthogonal Lie Algebra $\mathfrak{so}(n, \mathbb{R})$

The subspace of $\mathfrak{gl}(n, \mathbb{R})$ consisting of antisymmetric matrices $A^T = -A$ is a Lie subalgebra over $\mathbb{R}$, written $\mathfrak{so}(n, \mathbb{R})$. It is $\binom{n}{2}$-dimensional.

For $n = 3$, the Lie algebra $\mathfrak{so}(3, \mathbb{R})$ is three-dimensional. It is the Lie algebra of the rotation group $SO(3)$.

## 9. The Cross Product on $\mathbb{R}^3$

The cross product on $\mathbb{R}^3$ is a Lie bracket. It is bilinear over $\mathbb{R}$, antisymmetric, and satisfies the Jacobi identity. The resulting Lie algebra is isomorphic to $\mathfrak{so}(3, \mathbb{R})$.

## 10. The Heisenberg Lie Algebra over $\mathbb{R}$

The **Heisenberg Lie algebra** is the three-dimensional Lie algebra over $\mathbb{R}$ with basis $X, Y, Z$ and brackets

$$
[X, Y] = Z, \qquad [X, Z] = 0, \qquad [Y, Z] = 0.
$$

The Jacobi identity is satisfied because all nested brackets vanish. The center is spanned by $Z$. The Heisenberg Lie algebra does not arise from any associative algebra over $\mathbb{R}$.

## 11. The Clifford Algebra as a Lie Algebra over $\mathbb{R}$

Every Clifford algebra $Cl(V, Q)$ over $\mathbb{R}$ is an associative algebra, hence a Lie algebra with the commutator bracket. In particular, the subspace of bivectors is a Lie subalgebra isomorphic to $\mathfrak{so}(V, Q)$.

## 12. The Quaternions as a Lie Algebra over $\mathbb{R}$

The quaternions $\mathbb{H}$, viewed as an algebra over $\mathbb{R}$, become a Lie algebra with the commutator bracket. The subspace of pure quaternions (those with zero scalar part) is a Lie subalgebra isomorphic to $\mathfrak{so}(3, \mathbb{R})$.

## 13. The Split Complex Numbers as a Lie Algebra over $\mathbb{R}$

The split complex numbers $\mathbb{D}$, viewed as an algebra over $\mathbb{R}$, become a Lie algebra with the commutator bracket. But since $\mathbb{D}$ is commutative, the commutator bracket is identically zero. So $\mathbb{D}$ with the commutator bracket is the abelian Lie algebra over $\mathbb{R}$.

---

# Part III: Lie Algebras over $\mathbb{C}$

## 14. The Abelian Lie Algebra over $\mathbb{C}$

Any complex vector space with the zero bracket is an abelian Lie algebra over $\mathbb{C}$. For example, $\mathbb{C}$ itself is a one-dimensional abelian Lie algebra over $\mathbb{C}$, and $\mathbb{C}^n$ is an $n$-dimensional abelian Lie algebra.

## 15. The General Linear Lie Algebra $\mathfrak{gl}(n, \mathbb{C})$

The set $M_n(\mathbb{C})$ of $n \times n$ complex matrices is an $n^2$-dimensional Lie algebra over $\mathbb{C}$, with the commutator bracket. It is written $\mathfrak{gl}(n, \mathbb{C})$.

## 16. The Special Linear Lie Algebra $\mathfrak{sl}(n, \mathbb{C})$

The subspace of $\mathfrak{gl}(n, \mathbb{C})$ consisting of matrices with trace zero is a Lie subalgebra over $\mathbb{C}$, written $\mathfrak{sl}(n, \mathbb{C})$. It is $(n^2 - 1)$-dimensional.

For $n = 2$, the Lie algebra $\mathfrak{sl}(2, \mathbb{C})$ is three-dimensional. It is the smallest simple Lie algebra over $\mathbb{C}$, and it is the model for the classification of simple Lie algebras.

## 17. The Orthogonal Lie Algebra $\mathfrak{so}(n, \mathbb{C})$

The subspace of $\mathfrak{gl}(n, \mathbb{C})$ consisting of antisymmetric matrices is a Lie subalgebra over $\mathbb{C}$, written $\mathfrak{so}(n, \mathbb{C})$. It is $\binom{n}{2}$-dimensional.

## 18. The Complex Cross Product on $\mathbb{C}^3$

The complex cross product on $\mathbb{C}^3$ is a Lie bracket over $\mathbb{C}$. It is bilinear over $\mathbb{C}$, antisymmetric, and satisfies the Jacobi identity. The resulting Lie algebra is isomorphic to $\mathfrak{so}(3, \mathbb{C})$.

## 19. The Biquaternions as a Lie Algebra over $\mathbb{C}$

The biquaternions $\mathbb{H} \otimes \mathbb{C}$, viewed as an algebra over $\mathbb{C}$, become a Lie algebra with the commutator bracket. They are isomorphic to $M_2(\mathbb{C})$, so the resulting Lie algebra is $\mathfrak{gl}(2, \mathbb{C})$.

---

# Part IV: Lie Algebras over $\mathbb{D}$

The split complex numbers $\mathbb{D}$ are not a field in the strict sense: they form a commutative ring with zero divisors. The theory of Lie algebras over $\mathbb{D}$ is similar to the theory over a field, with the caveat that not every nonzero element has an inverse.

## 20. The Abelian Lie Algebra over $\mathbb{D}$

Any $\mathbb{D}$-module with the zero bracket is an abelian Lie algebra over $\mathbb{D}$. For example, $\mathbb{D}$ itself is a one-dimensional abelian Lie algebra over $\mathbb{D}$.

## 21. The General Linear Lie Algebra $\mathfrak{gl}(n, \mathbb{D})$

The set $M_n(\mathbb{D})$ of $n \times n$ matrices with entries in $\mathbb{D}$ is an $n^2$-dimensional Lie algebra over $\mathbb{D}$, with the commutator bracket. It is written $\mathfrak{gl}(n, \mathbb{D})$.

## 22. The Split Quaternions as a Lie Algebra over $\mathbb{D}$

The split quaternions $\mathbb{H} \otimes \mathbb{D}$, viewed as an algebra over $\mathbb{D}$, become a Lie algebra with the commutator bracket. The subspace of pure split quaternions is a Lie subalgebra, analogous to the pure quaternions over $\mathbb{R}$.

---

# Summary

Let me summarize the classification in a table.

| Lie algebra | Ring | Rank | Abelian | Simple |
|---|---|---|---|---|
| $\mathbb{Q}$ with zero bracket | $\mathbb{Q}$ | 1 | yes | no |
| $\mathfrak{gl}(n, \mathbb{Q})$ | $\mathbb{Q}$ | $n^2$ | no | no |
| $\mathfrak{sl}(n, \mathbb{Q})$ | $\mathbb{Q}$ | $n^2 - 1$ | no | yes |
| $\mathfrak{so}(n, \mathbb{Q})$ | $\mathbb{Q}$ | $\binom{n}{2}$ | no | yes |
| $\mathbb{R}$ with zero bracket | $\mathbb{R}$ | 1 | yes | no |
| $\mathfrak{gl}(n, \mathbb{R})$ | $\mathbb{R}$ | $n^2$ | no | no |
| $\mathfrak{sl}(n, \mathbb{R})$ | $\mathbb{R}$ | $n^2 - 1$ | no | yes |
| $\mathfrak{so}(n, \mathbb{R})$ | $\mathbb{R}$ | $\binom{n}{2}$ | no | yes |
| cross product on $\mathbb{R}^3$ | $\mathbb{R}$ | 3 | no | yes |
| Heisenberg | $\mathbb{R}$ | 3 | no | no |
| pure quaternions | $\mathbb{R}$ | 3 | no | yes |
| $\mathbb{C}$ with zero bracket | $\mathbb{C}$ | 1 | yes | no |
| $\mathfrak{gl}(n, \mathbb{C})$ | $\mathbb{C}$ | $n^2$ | no | no |
| $\mathfrak{sl}(n, \mathbb{C})$ | $\mathbb{C}$ | $n^2 - 1$ | no | yes |
| $\mathfrak{so}(n, \mathbb{C})$ | $\mathbb{C}$ | $\binom{n}{2}$ | no | yes |
| complex cross product on $\mathbb{C}^3$ | $\mathbb{C}$ | 3 | no | yes |
| $\mathbb{D}$ with zero bracket | $\mathbb{D}$ | 1 | yes | no |
| $\mathfrak{gl}(n, \mathbb{D})$ | $\mathbb{D}$ | $n^2$ | no | no |
| pure split quaternions | $\mathbb{D}$ | 3 | no | no |

The pattern is clear: the ring of scalars determines the structure of the Lie algebra. Over $\mathbb{Q}$, the algebras are arithmetic versions of the classical algebras. Over $\mathbb{R}$, the algebras are the Lie algebras of the classical groups. Over $\mathbb{C}$, the algebras are the complexifications, and the classification of simple Lie algebras is cleanest. Over $\mathbb{D}$, the algebras are analogous to those over $\mathbb{R}$, but with the caveat that $\mathbb{D}$ has zero divisors.

**Key differences from the field case.**

- Over a field, every Lie algebra is a vector space, so it has a well-defined dimension. Over a general commutative ring, a Lie algebra is a module, which need not be free. When the module is free, we speak of its **rank**.
- The classical structure theory (solvable, nilpotent, simple Lie algebras) is cleanest over fields of characteristic zero. Over a general commutative ring, the theory is more subtle.
- The classification of simple Lie algebras by Dynkin diagrams requires the base ring to be a field of characteristic zero. Over $\mathbb{D}$, which has characteristic zero but has zero divisors, the classification does not apply directly.
- The notion of a "division algebra" is not relevant for Lie algebras, because Lie algebras are never division algebras (they are non-associative and have zero divisors: $[u, u] = 0$ for all $u$).

---

## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972).
- Nathan Jacobson, *Lie Algebras* (Dover, 1979).
- Karin Erdmann and Mark J. Wildon, *Introduction to Lie Algebras* (Springer, 2006).
- Brian Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2nd ed. 2015).
- Jean-Pierre Serre, *Complex Semisimple Lie Algebras* (Springer, 1987).
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984).
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004).

