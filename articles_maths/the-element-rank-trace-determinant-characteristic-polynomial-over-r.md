# __The Element: Rank, Trace, Determinant, Characteristic Polynomial over $\mathbb{R}$__

## Introduction

**A single real matrix carries four invariants, and over $\mathbb{R}$ the fourth one fails to determine anything: the characteristic polynomial does not see the field.** The rank, the trace, the determinant and the characteristic polynomial are computed from the entries by polynomial formulas with real coefficients, so they are real numbers and a real polynomial. What changes from the complex case is the reading of the polynomial: its roots need not be real, so it describes the spectrum only through real points and conjugate pairs.

The article defines the four invariants, proves that the rank stratifies the algebra by real manifolds of dimension $r(2n-r)$, identifies the trace and the determinant inside the characteristic polynomial, proves Cayley–Hamilton over $\mathbb{R}$, and exhibits two nilpotents with the same characteristic polynomial and different rank. It assumes *The Matrix Algebra $M_n(\mathbb{R})$* and *The Split Real Form: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$*. It defers the elementary symmetric functions to *The Elementary Symmetric Functions and the Real Characteristic Polynomial* and the canonical form to *The Minimal Polynomial over $\mathbb{R}$ and the Real Jordan Form*.

## The Rank and Its Strata

**The rank is the dimension of the image, and it is the same over $\mathbb{R}$ and over $\mathbb{C}$.** For $A\in M_n(\mathbb{R})$,

$$
\operatorname{rk}A=\dim\operatorname{im}A=n-\dim\ker A,
$$

and the rank is also the largest order of a nonvanishing minor. Since the minors are real polynomials, a real matrix has rank at least $r$ over $\mathbb{R}$ exactly when it has rank at least $r$ over $\mathbb{C}$.

**The set of matrices of rank at most $r$ is a real algebraic variety of dimension $r(2n-r)$.** Write $\Sigma_{\le r}=\{A:\operatorname{rk}A\le r\}$. It is the zero set of all minors of order $r+1$, hence algebraic. To compute its dimension, factor $A=UV^{\mathsf T}$ with $U,V$ of size $n\times r$: the pair has $2nr$ parameters and the factorisation is unique up to $GL_r(\mathbb{R})$, of dimension $r^{2}$, so

$$
\dim\Sigma_{\le r}=2nr-r^{2}=r(2n-r).
$$

The codimension is $(n-r)^{2}$, and the open stratum $\Sigma_r=\{\operatorname{rk}=r\}$ is a smooth manifold of that dimension.

**The strata are checked at small $n$.** For $n=3$ the dimensions are $5$ at $r=1$ and $8$ at $r=2$, against $9$ for the whole algebra; the codimensions are $4$ and $1$. For $n=2$ they are $3$ at $r=1$ and $0$ at $r=2$: the rank-one matrices form a quadric cone of dimension $3$ in $\mathbb{R}^{4}$, the set $\{\det=0\}$.

**The rank is not determined by the other three invariants.** This is the point of the last section. The rank is, however, the invariant that controls the topology of the strata and the singular set, and it is the one that survives every base field unchanged.

## The Trace

**The trace is the sum of the diagonal entries and the only invariant linear functional.** It satisfies

$$
\operatorname{tr}(A+B)=\operatorname{tr}A+\operatorname{tr}B,\qquad \operatorname{tr}(AB)=\operatorname{tr}(BA),\qquad \operatorname{tr}(SAS^{-1})=\operatorname{tr}A,
$$

and every linear $f$ with $f(AB)=f(BA)$ is $c\operatorname{tr}$.

**The trace is the sum of the eigenvalues with multiplicities, counted in $\mathbb{C}$.** The eigenvalues are the roots of the characteristic polynomial, which has real coefficients; the sum of the roots is real even when individual roots are not, because the nonreal ones occur in conjugate pairs and their imaginary parts cancel:

$$
\operatorname{tr}A=\sum_{\lambda\in\operatorname{spec}(A)}\lambda=\sum_{\lambda\in\mathbb{R}}\lambda+2\sum_{\{\mu,\bar\mu\}}\operatorname{Re}\mu .
$$

**The trace is not the sum of the diagonal entries in every basis, but it is in every basis the same number.** This is the invariance above: the diagonal entries change with the basis, their sum does not. Equivalently, $\operatorname{tr}$ is the trace of the linear map, independent of the matrix used to write it.

## The Determinant and Its Sign

**The determinant is the product of the eigenvalues, and its sign is a topological invariant.** With

$$
\det A=\prod_{\lambda\in\operatorname{spec}(A)}\lambda=\prod_{\lambda\in\mathbb{R}}\lambda\prod_{\{\mu,\bar\mu\}}|\mu|^{2},
$$

the nonreal pairs contribute positive factors, so the sign of the determinant is the product of the signs of the real eigenvalues, counted with multiplicity. In particular $\det A<0$ forces an odd number of negative real eigenvalues, and $\det A>0$ does not force the spectrum to be real.

**The sign is what cuts the group of invertibles in two.** $\det:\mathrm{GL}_n(\mathbb{R})\to\mathbb{R}^{\times}$ is continuous and surjective, so its two signs are the two components. A matrix with $\det>0$ may still have no real eigenvalue of either sign: the rotation $J$ at $n=2$ has $\det J=1$ and no real eigenvalue. So the sign of the determinant is not readable from the real spectrum unless the spectrum is real.

**The determinant is multiplicative and vanishes exactly on the singular set.** $\det(AB)=\det A\det B$, and $\det A=0$ exactly when $A$ is not invertible, which is exactly when $\operatorname{rk}A<n$. So the zero set of the determinant is the closed stratum $\Sigma_{\le n-1}$, of codimension one.

## The Characteristic Polynomial

**The characteristic polynomial has real coefficients and degree $n$.** Define

$$
\chi_A(t)=\det(t\mathrm{I}-A)=t^{n}-(\operatorname{tr}A)t^{n-1}+\cdots+(-1)^{n}\det A .
$$

The coefficients are polynomials in the entries with integer coefficients, hence real. The two ends are the trace and the determinant:

$$
[t^{n-1}]\chi_A=-\operatorname{tr}A,\qquad \chi_A(0)=(-1)^{n}\det A .
$$

**The intermediate coefficients are the elementary symmetric functions of the eigenvalues, with signs.** Writing $\chi_A(t)=\prod_{k}(t-\lambda_k)$ and expanding,

$$
\chi_A(t)=\sum_{k=0}^{n}(-1)^{k}e_k(\lambda)t^{n-k},
$$

where $e_k$ is the $k$-th elementary symmetric function. This is *The Elementary Symmetric Functions and the Real Characteristic Polynomial*.

**The polynomial is invariant under conjugation and unchanged by transposition.** $\chi_{SAS^{-1}}=\chi_A$ because the determinant is conjugation invariant, and $\chi_{A^{\mathsf T}}=\chi_A$ because $\det(t\mathrm{I}-A^{\mathsf T})=\det((t\mathrm{I}-A)^{\mathsf T})=\det(t\mathrm{I}-A)$. This is compatible with the real Jordan form, where a block and its transpose are similar over $\mathbb{R}$.

## Real Roots and Conjugate Pairs

**The spectrum of a real matrix is stable under conjugation.** If $\chi_A(\mu)=0$ then $\chi_A(\bar\mu)=0$, because the coefficients are real. So the spectrum is the union of a set of real points and a set of pairs $\{\mu,\bar\mu\}$ with $\mu\notin\mathbb{R}$.

**A real root gives a real eigenvector and a real invariant line.** If $\lambda\in\mathbb{R}$ is a root, then $A-\lambda\mathrm{I}$ is a real singular matrix, so it has a nonzero real kernel; a nonzero vector there is an eigenvector. The line it spans is a real invariant line, and the restriction of $A$ to it is $\lambda$.

**A conjugate pair gives a real invariant plane and a rotation block.** Let $\mu=a+bi$ with $b\ne0$ and let $z=u+iv$ be a complex eigenvector, with $u,v\in\mathbb{R}^{n}$. Then $Au=au-bv$ and $Av=bu+av$, so the real plane spanned by $u$ and $v$ is invariant, and the matrix of $A$ on the basis $(u,v)$ is

$$
\begin{pmatrix}a&-b\\ b&a\end{pmatrix}.
$$

This block is a rotation by the angle $\theta$ with $\cos\theta=a/\sqrt{a^{2}+b^{2}}$ composed with the dilation $\sqrt{a^{2}+b^{2}}$. It has no real eigenvector, and its determinant $a^{2}+b^{2}=|\mu|^{2}$ is positive.

**The two kinds of block account for the whole real dimension.** A real matrix of size $n$ splits its spectrum into $r$ real eigenvalues and $s$ conjugate pairs with $r+2s=n$, and the real Jordan form is built from $1\times1$ blocks for the real roots and $2\times2$ blocks for the pairs, with nilpotent extensions. *The Real Jordan Form and the Rotation Blocks* proves the canonical form.

## Cayley–Hamilton over $\mathbb{R}$

**Every matrix satisfies its own characteristic polynomial.** With $\chi_A(t)=t^{n}+c_{n-1}t^{n-1}+\cdots+c_0$ one has

$$
\chi_A(A)=A^{n}+c_{n-1}A^{n-1}+\cdots+c_0\mathrm{I}=0 .
$$

*Proof.* Over $\mathbb{C}$ the matrix is triangularisable, and on a triangular matrix the product $\prod_k(A-\lambda_k\mathrm{I})$ annihilates the flag step by step. The identity is a polynomial identity in the entries with integer coefficients, and it holds on the dense open set of matrices with distinct eigenvalues over $\mathbb{C}$; hence it holds identically, in particular on real matrices.

**The proof does not need the real Jordan form, and the statement does not need $\mathbb{C}$.** The coefficients of $\chi_A$ and of the identity are real, and the identity can be verified by expansion. What the complex proof supplies is the idea; the algebraic identity is what makes it true over any field.

**A consequence: the powers of $A$ from $A^{n}$ on are linear combinations of the first $n$ powers.** The span of $\{\mathrm{I},A,\dots,A^{n-1}\}$ is a subalgebra of dimension at most $n$ containing $A$, and $\chi_A$ gives the first relation. The least-degree relation is the minimal polynomial, which is *The Minimal Polynomial over $\mathbb{R}$ and the Real Jordan Form*.

## What the Invariants Do Not Determine

**The characteristic polynomial does not determine the similarity class, and over $\mathbb{R}$ the failure is already visible at $n=3$.** Take the two nilpotents

$$
N_{(2,1)}=\begin{pmatrix}0&1&0\\ 0&0&0\\ 0&0&0\end{pmatrix},\qquad
N_{(3)}=\begin{pmatrix}0&1&0\\ 0&0&1\\ 0&0&0\end{pmatrix}.
$$

Both have $\chi(t)=t^{3}$, both have trace $0$ and determinant $0$, and they are not similar: their ranks are $1$ and $2$. So the four invariants of the title agree and the elements differ.

**The rank is what separates them, and even the rank does not separate everything.** At $n=4$ the nilpotents of type $(2,2)$ and $(3,1)$ both have rank $2$ and characteristic polynomial $t^{4}$, and they are not similar. The complete invariant is the Jordan type, that is the partition of $n$ given by the block sizes; over $\mathbb{R}$ the same statement holds with the rotation blocks added, and the partition is then a partition of the real dimension into the sizes of the real and the rotation blocks.

**What the invariants do give is a finite partition of the algebra.** The characteristic polynomial is a continuous map to the space of monic polynomials of degree $n$, and the fibres are unions of similarity classes. The Jordan type is constant on each similarity class and the classes of a fixed type form a manifold; the algebraic quotient of the conjugation action is the space of polynomials, of dimension $n$, and the extra invariants needed over $\mathbb{R}$ are the signs and the rotation data of *The Real Jordan Form and the Rotation Blocks*.

## Summary

The rank, the trace, the determinant and the characteristic polynomial of a real matrix are real data computed by polynomial formulas. The rank stratifies $M_n(\mathbb{R})$ into the varieties $\Sigma_{\le r}$ of dimension $r(2n-r)$ and codimension $(n-r)^{2}$. The trace is the only invariant linear functional and the sum of the eigenvalues; the determinant is the product, and its sign cuts the group of invertibles in two. The characteristic polynomial has real coefficients, its roots are real or come in conjugate pairs, a real root gives a real invariant line and a conjugate pair a real invariant plane with a $2\times2$ rotation block. Cayley–Hamilton holds over $\mathbb{R}$. The four invariants do not determine the element: at $n=3$ the nilpotents of type $(2,1)$ and $(3)$ share $t^{3}$ and differ in rank.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{rk}A$ | the rank, the dimension of the image |
| $\Sigma_{\le r}$, $\Sigma_r$ | the matrices of rank at most $r$, and of rank exactly $r$ |
| $\operatorname{tr}A$ | the trace, the sum of the diagonal entries |
| $\det A$ | the determinant, the product of the eigenvalues |
| $\chi_A(t)=\det(t\mathrm{I}-A)$ | the characteristic polynomial, of degree $n$ |
| $\operatorname{spec}(A)$ | the spectrum, a conjugation-stable multiset in $\mathbb{C}$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the rank, the determinant, the characteristic polynomial and Cayley–Hamilton.
- Peter Lancaster and Miron Tismenetsky, *The Theory of Matrices* (Academic Press, 1985), for the rank stratification and the determinantal varieties.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the algebra and its invariants.
- [The Element: Rank, Trace, Determinant, Characteristic Polynomial](the-element-rank-trace-determinant-characteristic-polynomial.html), for the complex case.
- [The Matrix Algebra $M_3(\mathbb{C})$](the-matrix-algebra-m3c.html), for the invariants at $n=3$.
- [The Forms, the Norms and the Singular Set of $M_3(\mathbb{C})$](the-forms-the-norms-and-the-singular-set-of-m3c.html), for the singular set and its strata.
