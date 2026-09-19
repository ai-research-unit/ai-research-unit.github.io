
# __Vector Spaces categorization__

## Introduction

This article gives a classification of vector spaces and their generalizations, organized by the **field or ring of scalars**. For each scalar structure, we state the classification of the simplest and most important modules, and we describe the position of the class in the hierarchy of module-theoretic structures.

The general theory is in the preceding article, *Vector Spaces over a Commutative Ring: A General Introduction*. We assume familiarity with the definitions given there.

We consider four scalar structures, in order of increasing complexity:

- The rational numbers $\mathbb{Q}$, a field.
- The real numbers $\mathbb{R}$, a field.
- The complex numbers $\mathbb{C}$, a field.
- The split complex numbers $\mathbb{D}$, a commutative ring with zero divisors.

For each scalar structure, we state the dimension of the module, the classification of finitely generated modules, and the structure of the general linear group.

Throughout this article, we use $R$ for a general commutative ring, $F$ for a field, and $M$ for an $R$-module.

---

# Part I: Vector Spaces over $\mathbb{Q}$

## 1. The Field $\mathbb{Q}$

The rational numbers $\mathbb{Q}$ form a field. Every nonzero rational number has a multiplicative inverse, and there are no zero divisors.

## 2. Vector Spaces over $\mathbb{Q}$

A **vector space over $\mathbb{Q}$** is a $\mathbb{Q}$-module. Since $\mathbb{Q}$ is a field, every $\mathbb{Q}$-module is free, so every vector space over $\mathbb{Q}$ has a basis.

The **dimension** of a $\mathbb{Q}$-vector space $V$ is the cardinality of any basis. It is well-defined: every basis has the same cardinality.

## 3. Classification of Finitely Generated Vector Spaces over $\mathbb{Q}$

Every finitely generated $\mathbb{Q}$-vector space is isomorphic to $\mathbb{Q}^n$ for some $n \geq 0$. The integer $n$ is the dimension, and it is a complete invariant: two finitely generated $\mathbb{Q}$-vector spaces are isomorphic if and only if they have the same dimension.

## 4. The General Linear Group over $\mathbb{Q}$

The **general linear group** $GL(n, \mathbb{Q})$ is the group of invertible $\mathbb{Q}$-linear maps $\mathbb{Q}^n \to \mathbb{Q}^n$. It is isomorphic to the group of invertible $n \times n$ matrices with entries in $\mathbb{Q}$.

A matrix $A \in M_n(\mathbb{Q})$ is invertible if and only if its determinant is nonzero.

## 5. Summary over $\mathbb{Q}$

| Notion | Description |
|---|---|
| Scalar structure | Field |
| Modules | Vector spaces |
| Free? | Always |
| Basis? | Always exists |
| Dimension | Well-defined |
| Finitely generated modules | $\mathbb{Q}^n$ |
| General linear group | $GL(n, \mathbb{Q})$ |

---

# Part II: Vector Spaces over $\mathbb{R}$

## 6. The Field $\mathbb{R}$

The real numbers $\mathbb{R}$ form a field. Every nonzero real number has a multiplicative inverse, and there are no zero divisors. Unlike $\mathbb{Q}$, the field $\mathbb{R}$ is complete with respect to the usual order.

## 7. Vector Spaces over $\mathbb{R}$

A **vector space over $\mathbb{R}$** is an $\mathbb{R}$-module. Since $\mathbb{R}$ is a field, every $\mathbb{R}$-module is free, so every vector space over $\mathbb{R}$ has a basis.

The **dimension** of an $\mathbb{R}$-vector space $V$ is the cardinality of any basis. It is well-defined.

## 8. Classification of Finitely Generated Vector Spaces over $\mathbb{R}$

Every finitely generated $\mathbb{R}$-vector space is isomorphic to $\mathbb{R}^n$ for some $n \geq 0$. The integer $n$ is the dimension, and it is a complete invariant: two finitely generated $\mathbb{R}$-vector spaces are isomorphic if and only if they have the same dimension.

## 9. The General Linear Group over $\mathbb{R}$

The **general linear group** $GL(n, \mathbb{R})$ is the group of invertible $\mathbb{R}$-linear maps $\mathbb{R}^n \to \mathbb{R}^n$. It is isomorphic to the group of invertible $n \times n$ matrices with entries in $\mathbb{R}$.

A matrix $A \in M_n(\mathbb{R})$ is invertible if and only if its determinant is nonzero.

## 10. Additional Structure over $\mathbb{R}$

The field $\mathbb{R}$ carries a natural topology and a notion of positivity, and unlike $\mathbb{Q}$ it is complete with respect to this topology. This allows the definition of:

- **Inner products.** A positive definite symmetric bilinear form on a real vector space.
- **Normed spaces.** A vector space equipped with a norm.
- **Hilbert spaces.** A complete inner product space.
- **Orthogonal groups.** The groups of isometries of a real vector space with an inner product.

These notions do not carry over to $\mathbb{Q}$ or $\mathbb{C}$ in the same way.

## 11. Summary over $\mathbb{R}$

| Notion | Description |
|---|---|
| Scalar structure | Field |
| Modules | Vector spaces |
| Free? | Always |
| Basis? | Always exists |
| Dimension | Well-defined |
| Finitely generated modules | $\mathbb{R}^n$ |
| General linear group | $GL(n, \mathbb{R})$ |
| Additional structure | Inner products, norms, topology |

---

# Part III: Vector Spaces over $\mathbb{C}$

## 12. The Field $\mathbb{C}$

The complex numbers $\mathbb{C}$ form a field. Every nonzero complex number has a multiplicative inverse, and there are no zero divisors. Unlike $\mathbb{R}$, the field $\mathbb{C}$ is algebraically closed: every non-constant polynomial with complex coefficients has a root in $\mathbb{C}$.

## 13. Vector Spaces over $\mathbb{C}$

A **vector space over $\mathbb{C}$** is a $\mathbb{C}$-module. Since $\mathbb{C}$ is a field, every $\mathbb{C}$-module is free, so every vector space over $\mathbb{C}$ has a basis.

The **dimension** of a $\mathbb{C}$-vector space $V$ is the cardinality of any basis. It is well-defined.

## 14. Classification of Finitely Generated Vector Spaces over $\mathbb{C}$

Every finitely generated $\mathbb{C}$-vector space is isomorphic to $\mathbb{C}^n$ for some $n \geq 0$. The integer $n$ is the dimension, and it is a complete invariant: two finitely generated $\mathbb{C}$-vector spaces are isomorphic if and only if they have the same dimension.

## 15. The General Linear Group over $\mathbb{C}$

The **general linear group** $GL(n, \mathbb{C})$ is the group of invertible $\mathbb{C}$-linear maps $\mathbb{C}^n \to \mathbb{C}^n$. It is isomorphic to the group of invertible $n \times n$ matrices with entries in $\mathbb{C}$.

A matrix $A \in M_n(\mathbb{C})$ is invertible if and only if its determinant is nonzero.

## 16. Additional Structure over $\mathbb{C}$

Unlike $\mathbb{R}$, the field $\mathbb{C}$ does not carry a natural total order. But it carries a natural conjugation and a notion of complex modulus. This allows the definition of:

- **Hermitian forms.** A sesquilinear form that is conjugate-symmetric.
- **Inner products.** A positive definite Hermitian form on a complex vector space.
- **Hilbert spaces.** A complete inner product space.
- **Unitary groups.** The groups of isometries of a complex vector space with an inner product.

These notions do not carry over to $\mathbb{Q}$ or $\mathbb{R}$ in the same way.

## 17. Summary over $\mathbb{C}$

| Notion | Description |
|---|---|
| Scalar structure | Field |
| Modules | Vector spaces |
| Free? | Always |
| Basis? | Always exists |
| Dimension | Well-defined |
| Finitely generated modules | $\mathbb{C}^n$ |
| General linear group | $GL(n, \mathbb{C})$ |
| Additional structure | Hermitian forms, topology |

---

# Part IV: Modules over $\mathbb{D}$

## 18. The Ring $\mathbb{D}$

The split complex numbers $\mathbb{D}$ form a commutative ring with identity, but they are **not a field**. They have zero divisors: $(1 + e)(1 - e) = 0$. The element $1 + e$ has no inverse.

The ring $\mathbb{D}$ is isomorphic, as an $\mathbb{R}$-algebra, to the product ring $\mathbb{R} \times \mathbb{R}$:

$$
\mathbb{D} \xrightarrow{\;\sim\;} \mathbb{R} \times \mathbb{R}, \qquad a + be \mapsto (a + b, \; a - b).
$$

This isomorphism is the key to understanding modules over $\mathbb{D}$.

## 19. Modules over $\mathbb{D}$

A **$\mathbb{D}$-module** is a module over the ring $\mathbb{D}$. Since $\mathbb{D}$ is not a field, not every $\mathbb{D}$-module is free, and torsion can occur.

Under the isomorphism $\mathbb{D} \cong \mathbb{R} \times \mathbb{R}$, every $\mathbb{D}$-module $M$ decomposes as a pair of $\mathbb{R}$-vector spaces:

$$
M \cong M_1 \times M_2
$$

where $M_1$ and $M_2$ are real vector spaces. The scalar multiplication by $\mathbb{D}$ acts componentwise:

$$
(a + be) \cdot (m_1, m_2) = ((a + b)m_1, (a - b)m_2).
$$

This reduces the theory of $\mathbb{D}$-modules to the theory of real vector spaces.

## 20. Classification of Finitely Generated Modules over $\mathbb{D}$

Every finitely generated $\mathbb{D}$-module is isomorphic to a pair of finitely generated $\mathbb{R}$-vector spaces:

$$
M \cong \mathbb{R}^m \times \mathbb{R}^n
$$

for some $m, n \geq 0$. The pair $(m, n)$ is a complete invariant: two finitely generated $\mathbb{D}$-modules are isomorphic if and only if they have the same pair of dimensions.

Equivalently, every finitely generated $\mathbb{D}$-module is isomorphic to $\mathbb{D}^k \oplus T$ where $T$ is a torsion module. But since $\mathbb{D} \cong \mathbb{R} \times \mathbb{R}$ is a product of two fields, every $\mathbb{D}$-module is a direct sum of a free part and a torsion part, and the torsion part is a direct sum of copies of $\mathbb{R}$ (viewed as a $\mathbb{D}$-module via one of the two projections).

## 21. The General Linear Group over $\mathbb{D}$

The **general linear group** $GL(n, \mathbb{D})$ is the group of invertible $\mathbb{D}$-linear maps $\mathbb{D}^n \to \mathbb{D}^n$. It is isomorphic to the group of invertible $n \times n$ matrices with entries in $\mathbb{D}$.

A matrix $A \in M_n(\mathbb{D})$ is invertible if and only if its determinant is a **unit** of $\mathbb{D}$. The units of $\mathbb{D}$ are the elements $a + be$ with $a^2 - b^2 \neq 0$.

Under the isomorphism $\mathbb{D} \cong \mathbb{R} \times \mathbb{R}$, the group $GL(n, \mathbb{D})$ decomposes as

$$
GL(n, \mathbb{D}) \cong GL(n, \mathbb{R}) \times GL(n, \mathbb{R}).
$$

This is a product of two copies of the real general linear group.

## 22. Summary over $\mathbb{D}$

| Notion | Description |
|---|---|
| Scalar structure | Commutative ring with zero divisors |
| Modules | $\mathbb{D}$-modules |
| Free? | Not always |
| Basis? | May not exist |
| Rank | Well-defined for free modules |
| Finitely generated modules | $\mathbb{R}^m \times \mathbb{R}^n$ |
| General linear group | $GL(n, \mathbb{R}) \times GL(n, \mathbb{R})$ |
| Additional structure | Decomposition $\mathbb{D} \cong \mathbb{R} \times \mathbb{R}$ |

---

# Part V: Summary

## 23. The Hierarchy of Scalar Structures

The four scalar structures form a hierarchy of increasing complexity:

$$
\mathbb{Q} \subset \mathbb{R} \subset \mathbb{C} \quad \text{(fields)},
$$

$$
\mathbb{D} \quad \text{(commutative ring with zero divisors)}.
$$

The first three are fields, so the theory of modules over them is the classical theory of vector spaces. The fourth is a commutative ring with zero divisors, so the theory of modules over it is more subtle.

## 24. Summary Table

| Scalar structure | Type | Modules free? | Dimension well-defined? | Finitely generated modules | General linear group |
|---|---|---|---|---|---|
| $\mathbb{Q}$ | Field | Always | Yes | $\mathbb{Q}^n$ | $GL(n, \mathbb{Q})$ |
| $\mathbb{R}$ | Field | Always | Yes | $\mathbb{R}^n$ | $GL(n, \mathbb{R})$ |
| $\mathbb{C}$ | Field | Always | Yes | $\mathbb{C}^n$ | $GL(n, \mathbb{C})$ |
| $\mathbb{D}$ | Commutative ring | Not always | For free modules | $\mathbb{R}^m \times \mathbb{R}^n$ | $GL(n, \mathbb{R}) \times GL(n, \mathbb{R})$ |

## 25. The Pattern

The pattern is clear: the scalar structure determines the structure of the module theory.

- Over $\mathbb{Q}$, $\mathbb{R}$, and $\mathbb{C}$, the theory is the classical theory of vector spaces. Every module is free, every basis has the same cardinality, and there is no torsion.
- Over $\mathbb{D}$, the theory is more subtle. Not every module is free, torsion can occur, and the theory decomposes into a pair of real vector spaces via the isomorphism $\mathbb{D} \cong \mathbb{R} \times \mathbb{R}$.

The passage from fields to commutative rings with zero divisors introduces new phenomena: torsion, non-free modules, and a more complicated classification. But the theory over $\mathbb{D}$ is still tractable, because $\mathbb{D}$ decomposes as a product of two fields.

---

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991).
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002).
- I. N. Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975).
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003).
- Nathan Jacobson, *Basic Algebra I* and *II* (Dover, 2nd ed. 2009).
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004).
- Thomas W. Hungerford, *Algebra* (Springer, 1974).
- Oscar Zariski and Pierre Samuel, *Commutative Algebra* (Springer, 1975).
- Hideyuki Matsumura, *Commutative Ring Theory* (Cambridge University Press, 1989).

