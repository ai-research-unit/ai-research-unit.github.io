# __The Minimal Polynomial and the Jordan Form__

## Introduction

**The characteristic polynomial gives the spectrum with multiplicities, the minimal polynomial gives the spectrum with the size of the largest block, and the Jordan form gives everything: the two polynomials are two summaries of one combinatorial datum, the partition of $n$ attached to each eigenvalue.**

The article defines the minimal polynomial as the monic generator of the annihilator of $A$, proves that it divides the characteristic polynomial and has the same roots, constructs the Jordan form from the generalised eigenspaces, and states the classification: two matrices are conjugate exactly when their Jordan types agree. It then counts: the number of types for a nilpotent of size $n$ is the number of partitions of $n$, and the dimension of the centraliser is the sum of the squares of the conjugate partition. It assumes *The Element: Rank, Trace, Determinant, Characteristic Polynomial* for the invariants and *The Elementary Symmetric Functions and $\det(\mathrm{I}+tA)$* for the coefficients. It defers the idempotents that the blocks produce to *The Peirce Decomposition and the Two Halves* and the real classification to *The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$*.

## The Annihilator

**The polynomials that kill $A$ form a nonzero ideal, and its monic generator is the minimal polynomial.** Put $\mathcal{I}(A)=\{f\in\mathbb{C}[t]: f(A)=0\}$. It is an ideal of $\mathbb{C}[t]$, and it is nonzero because the $n^{2}+1$ powers $\mathrm{I},A,\dots,A^{n^{2}}$ lie in the $n^{2}$-dimensional space $M_n(\mathbb{C})$ and are therefore dependent. The ring $\mathbb{C}[t]$ is principal, so $\mathcal{I}(A)=(m_A)$ with $m_A$ monic, and $m_A$ is the **minimal polynomial** of $A$.

**The minimal polynomial is a conjugacy invariant of degree at most $n$.** For $S$ invertible, $f(SAS^{-1})=Sf(A)S^{-1}$, so $\mathcal{I}(SAS^{-1})=\mathcal{I}(A)$. The degree bound is Cayley–Hamilton: $\chi_A(A)=0$, so $\chi_A\in\mathcal{I}(A)$ and

$$
m_A\mid\chi_A,\qquad \deg m_A\le n .
$$

The degree of $m_A$ is the dimension of the algebra $\mathbb{C}[A]$, since the powers of $A$ are independent exactly up to that degree.

**The minimal polynomial and the characteristic polynomial have the same roots.** If $Av=\lambda v$ with $v\ne0$, then $0=m_A(A)v=m_A(\lambda)v$, so $m_A(\lambda)=0$. Conversely, if $m_A(\lambda)=0$, write $m_A=(t-\lambda)g$; by minimality $g(A)\ne0$, so there is $v$ with $w=g(A)v\ne0$, and $(A-\lambda)w=m_A(A)v=0$. So $\lambda$ is an eigenvalue. Therefore

$$
m_A(t)=\prod_{i=1}^{r}(t-\lambda_i)^{a_i},\qquad \{m_A=0\}=\{\chi_A=0\},
$$

with the $\lambda_i$ distinct, and the exponent $a_i$ is the size of the largest Jordan block attached to $\lambda_i$.

**The matrix is nonderogatory exactly when the two polynomials agree.** The equality $m_A=\chi_A$ means one block per eigenvalue, and then $\mathbb{C}[A]$ has dimension $n$ and is a maximal commutative subalgebra. The generic matrix is nonderogatory, since the condition that two eigenvalues coalesce or that a block splits is the vanishing of polynomial conditions.

## The Jordan Form

**Every matrix is conjugate to a direct sum of Jordan blocks, uniquely up to the order of the summands.** A **Jordan block** is

$$
J_d(\lambda)=\lambda\mathrm{I}+N_d,\qquad N_d=\sum_{k=1}^{d-1}E_{k,k+1},
$$

with $N_d$ nilpotent of index $d$. The theorem states that for every $A$ there is an invertible $S$ and a list of pairs $(d_i,\lambda_i)$ with

$$
A=S\Big(\bigoplus_{i}J_{d_i}(\lambda_i)\Big)S^{-1},
$$

and that the list is unique once the blocks are grouped by eigenvalue and sorted by size.

**The construction is the one of the generalised eigenspaces.** Let $V_\lambda=\ker(A-\lambda\mathrm{I})^{n}$, the generalised eigenspace. The space $V$ is the direct sum of the $V_\lambda$, and on each summand $A-\lambda\mathrm{I}$ is nilpotent. A nilpotent is a sum of a chain of nested subspaces, and choosing a basis adapted to the chain exhibits the block. The sizes of the blocks are the numerical invariants of the nilpotent, read from the ranks

$$
\dim\ker N^{k}-\dim\ker N^{k-1}=\#\{i: d_i\ge k\},
$$

so the ranks of the powers determine the partition and nothing else does.

**The rank of a nilpotent counts the blocks.** For a nilpotent with block sizes $d_1,\dots,d_r$ and $d_1+\cdots+d_r=n$,

$$
\operatorname{rank}N=n-r .
$$

So the identity $N=0$ has rank $0$ and $n$ blocks, and a single block of size $n$ has rank $n-1$. This is the sharpest illustration of the failure recorded in *The Element: Rank, Trace, Determinant, Characteristic Polynomial*: the characteristic polynomial of every nilpotent is $t^{n}$, and the rank separates the types.

## The Classification

**Two matrices are conjugate exactly when their Jordan types agree.** Conjugation preserves the list of blocks, because it preserves the generalised eigenspaces and the ranks of the powers of $A-\lambda\mathrm{I}$. Conversely, two matrices with the same list are conjugate, since each is conjugate to the same direct sum. Hence

$$
A\sim B\iff (d_i,\lambda_i)_A=(d_i,\lambda_i)_B\ \text{up to order}.
$$

**The classification is the orbit decomposition of the conjugation action.** Each Jordan type is one orbit of $GL_n(\mathbb{C})$ on $M_n(\mathbb{C})$, and the orbit of a nonderogatory matrix is open and dense: its dimension is $n^{2}-n+1$, the dimension of $GL_n$ minus the dimension $n-1$ of the centraliser of the companion matrix. The union of the other orbits is the discriminant, the zero set of the polynomial that says two eigenvalues coincide or a block splits.

**The Jordan form is a refinement of the characteristic polynomial and a coarsening of the element.** For a fixed characteristic polynomial $\prod(t-\lambda_i)^{m_i}$ the types are the tuples of partitions of the multiplicities $m_i$. The number of types with a given spectrum is therefore the product of the partition numbers of the multiplicities, and the spectrum is recovered from the type.

## The Centraliser and the Commutant

**The centraliser of a matrix is the space of matrices commuting with it, and its dimension is read from the blocks.** For $A$ with blocks of sizes $d_{i,1}\ge d_{i,2}\ge\cdots$ attached to the eigenvalue $\lambda_i$, let $\lambda^{(i)}$ be the conjugate partition of the sizes. Then

$$
\dim C(A)=\sum_{i}\sum_{j}\big(\lambda^{(i)}_{j}\big)^{2}.
$$

The count is verified on the nilpotents of size at most four: the blocks $J_4,J_3\oplus J_1,J_2\oplus J_2,J_2\oplus J_1\oplus J_1,0$ give $4,6,8,10,16$, and the zero matrix gives $16=n^{2}$ as it must.

**The algebra generated by $A$ sits inside the centraliser, and the inclusion is strict except in the nonderogatory case.** Since $\mathbb{C}[A]$ is commutative and contains $A$, $\mathbb{C}[A]\subseteq C(A)$, and the dimensions are $\deg m_A$ and the number above. For the zero matrix the left side is $1$ and the right side is $n^{2}$. The equality $\mathbb{C}[A]=C(A)$ holds exactly when $m_A=\chi_A$.

**The centraliser of a single element is a product of matrix algebras, one for each eigenvalue.** On the block of $\lambda_i$ the centraliser is the algebra of matrices that are upper triangular in the flag of the chain and constant on each diagonal of the chain; it is a quotient of a product of matrix algebras, and its dimension is the sum of the squares above. The case of a single block of size $n$ is the extreme: $C(J_n(\lambda))=\mathbb{C}[J_n]$, of dimension $n$, the polynomials in one nilpotent.

## The Number of Types at Small $n$

**The nilpotent types of size $n$ are the partitions of $n$.** The counts are

| $n$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|
| partitions of $n$ | $2$ | $3$ | $5$ | $7$ | $11$ |

and the lists are

$$
(2),\ (1,1);\qquad (3),\ (2,1),\ (1,1,1);\qquad (4),\ (3,1),\ (2,2),\ (2,1,1),\ (1,1,1,1).
$$

Each partition is one conjugacy class of nilpotents, and the classes are ordered by the rank $n-r$ and by the index of nilpotency, the largest part.

**The total number of types at size $n$ is infinite for $n\ge1$, since the eigenvalues are free, but the combinatorial part is finite.** For a fixed spectrum the number of types is the product of the partition numbers of the multiplicities; for a single eigenvalue of multiplicity $n$ it is the partition number of $n$. So at $n=6$ a matrix with one eigenvalue has $11$ possible types, and the generic matrix, with six distinct eigenvalues, has exactly one.

**The Peirce decomposition sees the blocks, not the types.** A complete family of $n$ idempotents requires $n$ distinct spectral lines, hence $n$ distinct eigenvalues and blocks of size one. A single block of size $n$ carries one eigenvalue and one idempotent, and the construction of *The Peirce Decomposition in $n$ Dimensions* degenerates to the trivial one. The passage from the Jordan form to the Peirce frame is the passage from one eigenvalue to a full spectrum.

## The Case $n=2$

**At $n=2$ there are three kinds and the discriminant separates them.** For $A\in M_2(\mathbb{C})$ with $\chi_A(t)=t^{2}-\tau t+\delta$, where $\tau=\operatorname{tr}A$ and $\delta=\det A$:

| condition | type | minimal polynomial |
|---|---|---|
| $\Delta=\tau^{2}-4\delta\ne0$ | two distinct eigenvalues, diagonalisable | $(t-\lambda_1)(t-\lambda_2)$ |
| $\Delta=0$, $A\ne\tfrac{\tau}{2}\mathrm{I}$ | one eigenvalue, one block of size two | $(t-\tfrac{\tau}{2})^{2}$ |
| $A=\tfrac{\tau}{2}\mathrm{I}$ | scalar | $t-\tfrac{\tau}{2}$ |

The middle row is the interesting one: the minimal polynomial has degree two and equals the characteristic polynomial, and $A-\tfrac{\tau}{2}\mathrm{I}$ is a nonzero nilpotent with rank $1$.

**The middle row is the companion nilpotent of the biquaternion frame.** At $n=2$ a nonzero nilpotent $\vec\Pi_{\mathrm{nil},+-}$ of *The Companion Nilpotents of the Biquaternion Algebra* satisfies $\vec\Pi_{\mathrm{nil},+-}^{2}=0$ and has rank $1$, so its minimal polynomial is $t^{2}$ and its Jordan type is $(2)$. The two companion nilpotents $\vec\Pi_{\mathrm{nil},+-}$ and $\vec\Pi_{\mathrm{nil},-+}$ are conjugate, since there is one type, and they are distinguished only by the frame, which is the frame freedom of *The Frame, the Simple Nilpotents and the Frame Group of $M_n(\mathbb{C})$*.

**The classification at $n=2$ is the classification of the real forms at $n=2$ read differently.** A real $2\times2$ matrix with $\Delta<0$ is not diagonalisable over $\mathbb{R}$ and is a rotation block, which is the real normal form of *The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$*; the complex type is two distinct eigenvalues and the real type is one $2\times2$ block. The two classifications differ in the field and not in the algebra.

## Summary

The minimal polynomial $m_A$ is the monic generator of the ideal of polynomials killing $A$; it divides $\chi_A$, it has degree at most $n$, and it has the same roots as $\chi_A$, with exponents equal to the sizes of the largest blocks. The Jordan form writes $A$ as a direct sum of blocks $J_d(\lambda)$, uniquely up to order, and two matrices are conjugate exactly when their lists agree. For a nilpotent the types are the partitions of $n$, counted $2,3,5,7,11$ for $n=2,\dots,6$, the rank is $n$ minus the number of blocks, and the centraliser has dimension the sum of the squares of the conjugate partition. At $n=2$ the three kinds are separated by the discriminant, and the non-scalar double-eigenvalue case is the companion nilpotent of the biquaternion frame.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{I}(A)$ | the ideal of polynomials $f$ with $f(A)=0$ |
| $m_A$ | the minimal polynomial, the monic generator of $\mathcal{I}(A)$ |
| $\chi_A$ | the characteristic polynomial |
| $J_d(\lambda)$ | the Jordan block of size $d$ with eigenvalue $\lambda$ |
| $N_d$ | the nilpotent $\sum_{k<d}E_{k,k+1}$, of index $d$ |
| $V_\lambda=\ker(A-\lambda\mathrm{I})^{n}$ | the generalised eigenspace |
| $C(A)$ | the centraliser, $\{X: AX=XA\}$ |
| $\lambda^{(i)}$ | the conjugate partition of the block sizes at $\lambda_i$ |
| $\Delta=(\operatorname{tr}A)^{2}-4\det A$ | the discriminant at $n=2$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the Jordan form, the minimal polynomial and the centraliser.
- James E. Humphreys, *Linear Algebraic Groups* (Springer, 1975), for the orbit decomposition of the conjugation action and the nonderogatory open orbit.
- Peter Lancaster and Miron Tismenetsky, *The Theory of Matrices* (Academic Press, 1985), for the structure of the commutant of a single matrix.
- [The Element: Rank, Trace, Determinant, Characteristic Polynomial](the-element-rank-trace-determinant-characteristic-polynomial.html), for the invariants that the type refines.
- [The Elementary Symmetric Functions and $\det(\mathrm{I}+tA)$](the-elementary-symmetric-functions-and-det-i-plus-ta.html), for the coefficients of $\chi_A$ and Newton's identities.
- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the full spectrum that the frame requires.
- [The Companion Nilpotents of the Biquaternion Algebra](the-companion-nilpotents-of-the-biquaternion-algebra.html), for the two nilpotents at $n=2$.
