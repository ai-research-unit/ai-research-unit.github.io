
# __Involutions of a Central Simple Algebra__

## Introduction

A **central simple algebra** over a field $F$ is an $F$-algebra whose centre is $F$ and which has no nonzero proper two-sided ideal; the matrix algebras $M_n(F)$ are the split examples, and the quaternion algebra over $\mathbb{R}$ is the standard non-split one. On such an algebra the involutions are rigidly constrained. An involution is of the **first kind** when it fixes $F$ elementwise and of the **second kind** when it acts on $F$ through a nontrivial automorphism of order two; the **first-kind** involutions split into two **types**, the **orthogonal** and the **symplectic**, distinguished by the dimension of the symmetric part, and on a matrix algebra the two types are the transpose and the symplectic involution of *Matrix Rings with an Involution*. Because every automorphism of a central simple algebra is inner, two involutions differ by an inner automorphism, and this reduces the classification to the study of a single unit: the unit that conjugates one involution into the other, and the associated symmetry or skew-symmetry.

This article treats the kind, the two types of the first kind, the reduction of the comparison of two involutions to an inner automorphism, and the examples; the dimension theory of a central simple algebra, the Brauer group, the discriminant and the Clifford invariant belong to *Central Simple Algebras and the Brauer Group* and to *Hilbert Algebras* in Part II, and are named only to mark the boundary, not defined or used. It assumes *Involutive Rings* for the involution and *Fields* and *Division Rings* for the objects, and it forward-references the algebra category where the central simple algebras are treated. Throughout, $A$ is a central simple $F$-algebra with $1 \neq 0$, $\sigma$ is an involution, and $2$ is invertible in $F$ when the eigenspaces are used.

## First and Second Kind

**Definition.** An involution $\sigma$ of $A$ is of the **first kind** when $\sigma(z) = z$ for every $z \in Z(A) = F$, and of the **second kind** when its restriction to $F$ is a nontrivial automorphism of order two.

**Proposition.** If $\sigma$ is of the second kind then $F$ is a quadratic extension of its fixed field $F^\sigma$; the involution is $\varsigma$-semilinear with $\varsigma = \sigma|_F$, and the pair $(A,\sigma)$ is a form of the pair over $F^\sigma$ obtained by the descent along the quadratic extension. If $\sigma$ is of the first kind then it is $F$-linear, and $A$ is the sum of the symmetric and the skew parts, $A = \mathrm{Sym}(A,\sigma)\oplus\mathrm{Skew}(A,\sigma)$.

**Proof.** An order-two automorphism of a field has fixed field of index two when it is nontrivial, by the quadratic-extension theorem of *Involutive Rings*; the semilinearity of $\sigma$ over the fixed field is *Rings with a Semilinear Involution*; and the eigenspace decomposition is the same theorem applied to the $F$-linear order-two map $\sigma$.

**Theorem (the two types of the first kind).** A first-kind involution $\sigma$ of $A$ is of **orthogonal type** or of **symplectic type**; the type is determined by

$$
\dim_F \mathrm{Sym}(A,\sigma) = \tfrac12 n(n+1) \quad \text{(orthogonal)}, \qquad \dim_F \mathrm{Sym}(A,\sigma) = \tfrac12 n(n-1) \quad \text{(symplectic)},
$$

where $n$ is the degree of $A$ over $F$ in the sense of *Central Simple Algebras and the Brauer Group*; an orthogonal involution has a symmetric unit and a family of orthogonal symmetric idempotents summing to $1$, a symplectic one has neither, and a symplectic involution exists only when $n$ is even.

**Proof.** This is the matrix classification of *Matrix Rings with an Involution* transported to the general $A$: splitting $A$ by a finite extension of $F$ in which the algebra becomes a matrix algebra, the involution becomes a matrix involution of the same type there, and the dimension of the symmetric part is invariant under the extension because the type is; the idempotent criterion is the one of that article, and the parity obstruction to the symplectic type is the evenness of the rank of a symplectic idempotent.

**Remark.** The general classification of the first-kind involutions by orthogonal and symplectic type is due to Albert and is the algebraic core of the theory of the classical groups; the arithmetic refinement, by the discriminant and the Clifford invariant, requires the quadratic forms of Part II and is deferred to *Hilbert Algebras*.

## Comparing Two Involutions

**Theorem (inner reduction).** Let $\sigma$ and $\tau$ be two involutions of $A$, and suppose that $\sigma$ and $\tau$ have the same restriction to $F$, so that $\sigma\tau^{-1}$ is an $F$-linear automorphism of $A$. Then $\sigma\tau^{-1}$ is inner: there is a unit $u \in A^\times$ with

$$
\sigma(a) = u\,\tau(a)\,u^{-1} \quad \text{for all } a \in A .
$$

**Proof.** The composite $\sigma\tau^{-1}$ is an $F$-linear automorphism of $A$, and every automorphism of a central simple algebra is inner by the Skolem–Noether theorem, which is proved in *Central Simple Algebras and the Brauer Group*; write it as conjugation by $u$.

**Proposition (when the conjugate is an involution).** For a unit $u$ the map $\sigma = \operatorname{inn}_u\circ\tau$ is an involution if and only if $\tau(u)u$ is central,

$$
\sigma^2 = \mathrm{id} \iff \tau(u)\,u \in F .
$$

Under this condition $\sigma$ is of the same kind as $\tau$; it is of the **same type** as $\tau$ when $\tau(u)u$ is a square in $F$ and of the **opposite type** when it is not, in the first-kind case.

**Proof.** $\operatorname{inn}_u\tau$ is additive and $F$-linear, and its square is $\operatorname{inn}_u\tau\operatorname{inn}_u\tau = \operatorname{inn}_{u\tau(u)}\tau^2 = \operatorname{inn}_{u\tau(u)}$, which is the identity exactly when $u\tau(u)$ is central, i.e. $\tau(u)u \in F$ by the centrality of scalars. For the type, conjugation by $u$ leaves the dimension of the symmetric part unchanged, and the change is read off from the symmetry of $u$ relative to $\tau$: a unit fixed up to the scalar $\tau(u)u$ contributes a symmetric or a skew symmetry according as that scalar is a square, which exchanges the two dimensions of the matrix case.

**Corollary (the classification reduces to units).** Two first-kind involutions of $A$ differ by an inner automorphism, and the comparison is governed by the class of $\tau(u)u$ in $F^\times/F^{\times2}$, where $u$ is the unit with $\sigma = \operatorname{inn}_u\circ\tau$; this class is the elementary invariant of the pair, and it decides whether the two involutions have the same type or opposite type. The finer invariants, the discriminant and the Clifford invariant, are the forms of Part II.

## Examples

**(a) The matrix algebra.** For $A = M_n(F)$ the first-kind involutions are the transpose and the symplectic involution, with $\dim\mathrm{Sym} = \tfrac12 n(n+1)$ and $\tfrac12 n(n-1)$, and the second-kind ones exist when $F$ has an involution $\varsigma$ and are the conjugate transposes of *Matrix Rings with an Involution*.

**(b) The quaternion algebra.** For the quaternion algebra $A = \mathbb{H}(F)$ over a field $F$ of characteristic not two and the conjugation $\sigma$, the involution is of the first kind; the symmetric part is $F$ and the skew part is the trace-zero subspace of dimension three, so for $n = 2$ the conjugation is of orthogonal type, in agreement with $\tfrac12\cdot 2\cdot 3 = 3$; the quaternion algebras are the central simple algebras of degree two that are not split.

**(c) The complex matrix algebra.** For $A = M_n(\mathbb{C})$ over $\mathbb{C}$ with the conjugate transpose, the involution is of the second kind, its fixed field is $\mathbb{R}$, and the pair is the descent of $M_n(\mathbb{C})$ to the real form $M_n(\mathbb{R})$ or to the quaternionic form according to the symmetry of the Hermitian form involved; the classification of the second-kind involutions is the classification of the Hermitian forms over $\mathbb{C}$ with the conjugation.

**(d) The degree-two case.** For a degree-two central simple algebra every first-kind involution is either the conjugation of a quaternion algebra, of orthogonal type, or the composite of it with the symplectic matrix involution after splitting, of symplectic type; the two occur on the same algebra and the passage between them is conjugation by a unit with $\tau(u)u$ a non-square.

## Summary

An involution of a central simple $F$-algebra is of the **first kind** when it fixes the centre and of the **second kind** when it acts on the centre by a nontrivial automorphism of order two; the second-kind involutions are $\varsigma$-semilinear over the fixed field, and the first-kind ones are $F$-linear and split the algebra into symmetric and skew parts. A first-kind involution is of **orthogonal** or of **symplectic** type, determined by the dimension of the symmetric part, $\tfrac12 n(n+1)$ or $\tfrac12 n(n-1)$, with the orthogonal type characterised by a symmetric unit and by orthogonal symmetric idempotents summing to $1$ and the symplectic type occurring only in even degree. Two involutions with the same restriction to the centre differ by an inner automorphism, $\sigma = \operatorname{inn}_u\circ\tau$, by Skolem–Noether; the composite is an involution exactly when $\tau(u)u$ is central, and the type is unchanged or exchanged according as that scalar is or is not a square, so the classification reduces to the orbits of the norm-one torus and to the class of $\tau(u)u$ in $F^\times/F^{\times2}$. The arithmetic invariants, the discriminant, the Clifford invariant and the Brauer classes, are the forms of Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $F$ | Central simple $F$-algebra with centre $F$ |
| $n$ | Degree of $A$ over $F$ |
| $\sigma$ | Involution of $A$ |
| first kind, second kind | Fixes $F$, or acts on $F$ by a nontrivial order-two automorphism |
| $\mathrm{Sym},\mathrm{Skew}$ | Eigenspaces of a first-kind involution, $2$ invertible |
| $\tfrac12 n(n+1)$, $\tfrac12 n(n-1)$ | Dimensions of the symmetric part, orthogonal and symplectic types |
| $\sigma = \operatorname{inn}_u\circ\tau$ | Any two involutions with the same centre restriction |
| $\tau(u)u \in F$ | Condition for the conjugate to be an involution |
| $F^\times/F^{\times2}$ | The type invariant for a first-kind involution |
| $\mathbb{H}(F)$, $M_n(F)$ | Quaternion and matrix examples |

## Further Reading

- Albert Adrian Albert, *Structure of Algebras*, American Mathematical Society Colloquium Publications 24 (1939), for the classification of the involutions of a central simple algebra and the two types of the first kind.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the first and second kind, the inner reduction and the symmetric and skew parts.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the discriminant, the Clifford invariant and the full classification of involutions of a central simple algebra.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for Skolem–Noether and the inner structure of a simple ring.
