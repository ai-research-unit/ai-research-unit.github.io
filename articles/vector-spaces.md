

# __Vector Spaces : A General Introduction__

## Introduction

This article introduces the theory of vector spaces over a commutative ring. The classical theory of vector spaces assumes that the scalars form a field. But many of the constructions and theorems carry over to the more general setting where the scalars form a commutative ring. The resulting objects are called **modules**, and they are the natural generalization of vector spaces.

The treatment is introductory and purely mathematical. We assume familiarity with rings, fields, and the basic theory of vector spaces over a field.

We begin with the definition of a module over a commutative ring, then introduce the notions of submodules, homomorphisms, free modules, bases, and dimension. We compare the theory over a ring with the classical theory over a field, and we indicate where the two diverge.

---

# Part I: Modules over a Commutative Ring

## 1. Definition of a Module

Let $R$ be a commutative ring with identity. An **$R$-module** is an abelian group $(M, +)$ equipped with a scalar multiplication

$$
R \times M \to M, \qquad (r, m) \mapsto r m,
$$

satisfying the following axioms for all $r, s \in R$ and $m, n \in M$:

**(M1)** $r(m + n) = r m + r n$.

**(M2)** $(r + s)m = r m + s m$.

**(M3)** $(r s)m = r(s m)$.

**(M4)** $1 m = m$.

If $R$ is a field, an $R$-module is exactly a **vector space** over $R$. So modules generalize vector spaces to arbitrary commutative rings.

## 2. Elementary Properties

Let $M$ be an $R$-module. The following properties follow from the axioms.

**(a) Multiplication by zero.** For all $m \in M$,

$$
0 m = 0.
$$

**(b) Multiplication by zero scalar.** For all $r \in R$,

$$
r 0 = 0.
$$

**(c) Sign rules.** For all $r \in R$ and $m \in M$,

$$
(-r) m = r(-m) = -(r m), \qquad (-r)(-m) = r m.
$$

**(d) Distributivity over subtraction.** For all $r, s \in R$ and $m, n \in M$,

$$
r(m - n) = r m - r n, \qquad (r - s)m = r m - s m.
$$

## 3. Examples of Modules

**(a) The ring itself.** Every commutative ring $R$ is an $R$-module, with scalar multiplication given by the ring multiplication.

**(b) The free module $R^n$.** The set of $n$-tuples of elements of $R$,

$$
R^n = \{(r_1, \ldots, r_n) : r_i \in R\},
$$

is an $R$-module with componentwise addition and scalar multiplication.

**(c) Ideals.** Every ideal $I \subseteq R$ is an $R$-module.

**(d) Quotient rings.** If $I \subseteq R$ is an ideal, then $R/I$ is an $R$-module.

**(e) The polynomial ring.** The polynomial ring $R[x]$ is an $R$-module.

**(f) The matrix ring.** The set $M_n(R)$ of $n \times n$ matrices over $R$ is an $R$-module.

**(g) Abelian groups as $\mathbb{Z}$-modules.** Every abelian group is a $\mathbb{Z}$-module, with scalar multiplication given by repeated addition.

---

# Part II: Submodules and Homomorphisms

## 4. Submodules

A subset $N \subseteq M$ of an $R$-module $M$ is a **submodule** if:

**(S1)** $N$ is a subgroup of $(M, +)$: for all $m, n \in N$, $m - n \in N$.

**(S2)** $N$ is closed under scalar multiplication: for all $r \in R$ and $m \in N$, $r m \in N$.

A submodule of a module over a field is exactly a vector subspace.

## 5. Module Homomorphisms

Let $M$ and $N$ be $R$-modules. An **$R$-module homomorphism** is a function

$$
\varphi : M \to N
$$

such that for all $r \in R$ and $m, n \in M$:

**(H1)** $\varphi(m + n) = \varphi(m) + \varphi(n)$.

**(H2)** $\varphi(r m) = r \varphi(m)$.

An $R$-module homomorphism that is bijective is an **$R$-module isomorphism**. If there is an $R$-module isomorphism $M \to N$, we write $M \cong N$ and say that $M$ and $N$ are **isomorphic**.

The **kernel** of an $R$-module homomorphism $\varphi : M \to N$ is

$$
\ker \varphi = \{m \in M : \varphi(m) = 0\}.
$$

The **image** of $\varphi$ is

$$
\operatorname{im} \varphi = \{\varphi(m) : m \in M\}.
$$

The kernel is a submodule of $M$, and the image is a submodule of $N$.

## 6. Quotient Modules

Let $M$ be an $R$-module and $N \subseteq M$ a submodule. The **quotient module** $M/N$ is the set of cosets

$$
M/N = \{m + N : m \in M\}
$$

with addition and scalar multiplication defined by

$$
(m + N) + (n + N) = (m + n) + N, \qquad r(m + N) = r m + N.
$$

These operations are well-defined, and $M/N$ is an $R$-module.

The **first isomorphism theorem** states that if $\varphi : M \to N$ is an $R$-module homomorphism, then

$$
M / \ker \varphi \cong \operatorname{im} \varphi.
$$

---

# Part III: Free Modules and Bases

## 7. Linear Independence

Let $M$ be an $R$-module. A subset $S \subseteq M$ is **linearly independent** if for every finite subset $\{m_1, \ldots, m_k\} \subseteq S$, the equation

$$
r_1 m_1 + \cdots + r_k m_k = 0
$$

with $r_i \in R$ implies $r_1 = \cdots = r_k = 0$.

A subset $S \subseteq M$ **spans** $M$ if every element of $M$ can be written as a finite linear combination of elements of $S$.

A **basis** of $M$ is a linearly independent spanning set.

## 8. Free Modules

An $R$-module $M$ is **free** if it has a basis. If $M$ has a basis of cardinality $n$, then $M \cong R^n$.

**Examples.**

- $R^n$ is a free $R$-module of rank $n$.
- Every vector space over a field is free.
- Over $\mathbb{Z}$, the free modules are the groups $\mathbb{Z}^n$.
- Over $\mathbb{D}$, the free modules are the modules $\mathbb{D}^n$.

**Non-examples.**

- $\mathbb{Z}/n\mathbb{Z}$ is a $\mathbb{Z}$-module that is not free for $n \geq 2$.
- Any ideal $I \subseteq R$ that is not principal is not free as an $R$-module in general.

## 9. Rank

If $M$ is a free $R$-module with a basis of cardinality $n$, we say that $M$ has **rank** $n$. Over a field, the rank is the dimension, and it is well-defined: every basis has the same cardinality.

Over a general commutative ring, the rank of a free module is well-defined if $R$ has the **invariant basis number** property. Many rings of interest (including fields, $\mathbb{Z}$, and $\mathbb{D}$) have this property. But not every ring does: there are rings over which $R^m \cong R^n$ for $m \neq n$.

## 10. Torsion

An element $m \in M$ is a **torsion element** if there exists a nonzero $r \in R$ such that

$$
r m = 0.
$$

The set of torsion elements of $M$ is a submodule, called the **torsion submodule** of $M$. A module is **torsion-free** if its torsion submodule is zero.

Over a field, every module is torsion-free. Over a general commutative ring, torsion is a new phenomenon.

**Example.** In $\mathbb{Z}/n\mathbb{Z}$ as a $\mathbb{Z}$-module, every element is torsion.

---

# Part IV: Comparison with Vector Spaces

## 11. What Carries Over

Many of the basic notions of linear algebra carry over to modules over a commutative ring without change:

- Submodules, quotient modules, and homomorphisms.
- The first isomorphism theorem.
- Direct sums and direct products.
- Free modules and bases.
- Linear independence and spanning sets.

## 12. What Does Not Carry Over

Several key properties of vector spaces fail for modules over a general commutative ring:

**(a) Not every module is free.** Over a field, every module is free. Over a general ring, this is false. For example, $\mathbb{Z}/n\mathbb{Z}$ is not a free $\mathbb{Z}$-module.

**(b) Not every submodule is a direct summand.** Over a field, every subspace of a vector space has a complement. Over a general ring, this is false.

**(c) Rank may not be well-defined.** Over a field, every basis has the same cardinality. Over a general ring, this may fail if the ring does not have the invariant basis number property.

**(d) Torsion may exist.** Over a field, every module is torsion-free. Over a general ring, torsion is a new phenomenon.

**(e) Linear maps may not have a determinant.** Over a field, every linear map has a determinant, and invertibility is equivalent to nonzero determinant. Over a general ring, the determinant is still defined, but invertibility is equivalent to the determinant being a **unit** of the ring.

## 13. The Case of a Field

When $R = F$ is a field, the theory of $F$-modules is exactly the theory of vector spaces over $F$. Every module is free, every submodule is a direct summand, every basis has the same cardinality, and there is no torsion. The classification of finitely generated $F$-modules is trivial: every finitely generated $F$-module is isomorphic to $F^n$ for some $n$.

## 14. The Case of $\mathbb{Z}$

When $R = \mathbb{Z}$, the theory of $\mathbb{Z}$-modules is exactly the theory of abelian groups. Not every abelian group is free: for example, $\mathbb{Z}/n\mathbb{Z}$ is not free. The classification of finitely generated $\mathbb{Z}$-modules is the **structure theorem for finitely generated abelian groups**: every finitely generated abelian group is isomorphic to

$$
\mathbb{Z}^r \oplus \mathbb{Z}/n_1\mathbb{Z} \oplus \cdots \oplus \mathbb{Z}/n_k\mathbb{Z}
$$

for some $r \geq 0$ and $n_1, \ldots, n_k \geq 2$.

## 15. The Case of $\mathbb{D}$

When $R = \mathbb{D}$, the split complex numbers, the theory of $\mathbb{D}$-modules is more subtle because $\mathbb{D}$ has zero divisors. A $\mathbb{D}$-module need not be free, and torsion can occur. But since $\mathbb{D} \cong \mathbb{R} \times \mathbb{R}$ as a ring, every $\mathbb{D}$-module decomposes as a pair of $\mathbb{R}$-vector spaces:

$$
M \cong M_1 \times M_2
$$

where $M_1$ and $M_2$ are real vector spaces. This reduces the theory of $\mathbb{D}$-modules to the theory of real vector spaces.

---

# Part V: Summary

## 16. Summary of the Theory

| Notion | Over a field $F$ | Over a commutative ring $R$ |
|---|---|---|
| Module | Vector space | Module |
| Submodule | Subspace | Submodule |
| Homomorphism | Linear map | $R$-linear map |
| Free module | Always free | Not always free |
| Basis | Always exists | May not exist |
| Rank | Well-defined | Well-defined if IBN holds |
| Torsion | None | Possible |
| Determinant | Defined | Defined, invertibility iff unit |
| Classification | Trivial for f.g. modules | Structure theorem for PIDs |

## 17. The Role of Commutative Rings

Commutative rings are the natural setting for:

1. **Algebraic geometry.** The ring of functions on an algebraic variety is a commutative ring, and the modules over it are the sheaves on the variety.
2. **Number theory.** The ring of integers of a number field is a commutative ring, and the modules over it are the ideals and fractional ideals of the field.
3. **The theory of quadratic forms over rings.** Clifford algebras can be defined over any commutative ring, and their representation theory is the theory of modules over the Clifford algebra.
4. **The theory of modules.** Modules over commutative rings generalize vector spaces, and their classification is a central problem in commutative algebra.

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

