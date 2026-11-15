# __The Elementary Symmetric Functions and the Real Characteristic Polynomial__

## Introduction

**The coefficients of $\chi_A$ are the elementary symmetric functions of the eigenvalues, and each of them is also a sum of principal minors of $A$, hence computable without leaving $\mathbb{R}$.** This double description is what makes the real characteristic polynomial an object of real algebra rather than a complex accident.

The article proves the identification of the coefficient $e_k$ with the sum of the principal $k\times k$ minors, proves the expansion $\det(\mathrm{I}+tA)=\sum_k e_k t^{k}$, derives Newton's identities and the power sums, records what reality does to the coefficients, identifies the invariant ring, and proves $\det e^{A}=e^{\operatorname{tr}A}$ by Jacobi's formula. It assumes *The Element: Rank, Trace, Determinant, Characteristic Polynomial over $\mathbb{R}$*. It defers the discriminant to *The Discriminant and the Spectral Strata of a Real Matrix*.

## The Principal Minors

**A principal minor is the determinant of the submatrix on a set of rows and the same set of columns.** For $S\subseteq\{1,\dots,n\}$ let $A_{S}$ be the submatrix with rows and columns in $S$. Then

$$
e_k(A)=\sum_{|S|=k}\det A_S,\qquad k=0,1,\dots,n,
$$

with $e_0=1$ and $e_n=\det A$. There are $\binom{n}{k}$ summands, each a real polynomial of degree $k$ in the entries, so $e_k$ is a real polynomial of degree $k$.

**Each $e_k$ is the $k$-th elementary symmetric function of the eigenvalues.** Two proofs are available, and both are instructive. The first is the expansion of $\det(t\mathrm{I}-A)$ along the permutation formula: a nonzero term selects a fixed set $S$ of $k$ indices on which the permutation is not the identity, and the remaining $n-k$ diagonal factors contribute $t^{n-k}$. The second is the diagonalisable case, where $A=S\operatorname{diag}(\lambda)S^{-1}$ gives

$$
\det(t\mathrm{I}-A)=\prod_{j=1}^{n}(t-\lambda_j)=\sum_{k=0}^{n}(-1)^{k}e_k(\lambda)\,t^{n-k},
$$

and the principal minors are invariant under conjugation, so the identity extends by density.

**The two readings agree and each has its use.** The spectral reading explains why $e_k$ is conjugation invariant and why its degree in the eigenvalues is $k$. The minor reading shows that $e_k(A)$ is defined over any field and computed by determinants of size $k$, with no eigenvector and no complex number.

**At $n=3$ the three functions read off the matrix.** With $A=(a_{ij})$,

$$
e_1=a_{11}+a_{22}+a_{33},\qquad
e_2=\det A_{\{1,2\}}+\det A_{\{1,3\}}+\det A_{\{2,3\}},\qquad
e_3=\det A,
$$

so $\chi_A(t)=t^{3}-e_1t^{2}+e_2t-e_3$. Every coefficient is real, and $e_2$ involves the three $2\times2$ minors, not the single number $\operatorname{tr}(A)^{2}$.

## The Expansion of $\det(\mathrm{I}+tA)$

**The generating function of the $e_k$ is one determinant.** For every $A$ and every scalar $t$,

$$
\det(\mathrm{I}+tA)=\sum_{k=0}^{n}e_k(A)\,t^{k}.
$$

*Proof.* The Leibniz formula gives a sum over permutations $\sigma$. A permutation decomposes into cycles, and a cycle of length $\ell\ge2$ contributes the product of $\ell$ off-diagonal entries of $tA$ times a sign; the fixed points contribute the diagonal entries $1+ta_{ii}$. Collecting the terms by the set $S$ of indices that are not fixed points gives exactly $\sum_{|S|=k}\det(A_S)t^{k}$, which is the claim. A direct expansion at $n=2$ confirms it: $\det(\mathrm{I}+tA)=1+t\operatorname{tr}A+t^{2}\det A$.

**The characteristic polynomial is this expansion at $t=-1/\tau$, rescaled.** Substituting $t=-1/\tau$ and multiplying by $\tau^{n}$,

$$
\det(\tau\mathrm{I}-A)=\tau^{n}\det\!\Bigl(\mathrm{I}-\frac{A}{\tau}\Bigr)=\sum_{k=0}^{n}(-1)^{k}e_k(A)\tau^{n-k},
$$

which is the formula of §*The Principal Minors*. So the expansion of $\det(\mathrm{I}+tA)$ and the characteristic polynomial are the same statement.

**The expansion is multiplicative in a strong sense.** For commuting $A$ and $B$,

$$
\det(\mathrm{I}+tAB)=\det(\mathrm{I}+tBA),
$$

because $AB$ and $BA$ have the same characteristic polynomial, which is the identity $\det(\mathrm{I}-tAB)=\det(\mathrm{I}-tBA)$ proved by a block determinant. Hence $e_k(AB)=e_k(BA)$ for all $k$, and each $e_k$ is a trace-like invariant: a polynomial function constant on similarity classes and blind to the order of a product.

**The first two coefficients are the trace and the elementary function of order two.** $e_1=\operatorname{tr}A$ and

$$
e_2=\tfrac12\bigl((\operatorname{tr}A)^{2}-\operatorname{tr}(A^{2})\bigr),
$$

which is Newton's identity at $k=2$ and shows that $e_2$ is determined by the two power sums $p_1$ and $p_2$.

## Newton's Identities and the Power Sums

**The power sums determine the elementary functions and conversely.** Put $p_k=\operatorname{tr}(A^{k})=\sum_j\lambda_j^{k}$. Then for $1\le k\le n$,

$$
k\,e_k=\sum_{j=1}^{k}(-1)^{j-1}e_{k-j}\,p_j,
$$

and for $k>n$ the same relation holds with $e_k=0$. The identities are proved by differentiating the generating function $\sum_k e_kt^{k}=\prod_j(1+t\lambda_j)$ and comparing coefficients of $t^{k-1}$.

**The first three identities.** Explicitly,

$$
e_1=p_1,\qquad 2e_2=e_1p_1-p_2,\qquad 3e_3=e_2p_1-e_1p_2+p_3,
$$

so the three lowest elementary functions are polynomials in the three lowest power sums, with integer coefficients. The pattern is triangular: $e_k$ depends on $p_1,\dots,p_k$ and not on the higher ones.

**The power sums are real and are the moments of the spectrum.** $p_k=\operatorname{tr}(A^{k})$ is real for real $A$, since $A^{k}$ is real. For a conjugate pair $\mu,\bar\mu$ the contribution is $2\operatorname{Re}(\mu^{k})$, so every $p_k$ is real even though no individual $\mu$ need be. So the coefficients $e_k$ are real twice over: as sums of real principal minors, and as integer polynomials in the real numbers $p_k$.

**The identities are what make the coefficients computable by matrix powers.** Computing $p_1,\dots,p_n$ costs $n$ matrix multiplications and $n$ traces; then $n$ triangular steps give the $e_k$. No eigenvalue and no factorisation is used, so the computation is valid over $\mathbb{R}$ and stable under the field.

## Reality and the Sign

**Reality of the coefficients is a constraint on the multiset of roots.** A monic real polynomial of degree $n$ has a root multiset stable under conjugation; conversely every conjugation-stable multiset of $n$ complex numbers with the right multiplicities is the spectrum of a real matrix, because the companion matrix of the polynomial is real. So the spectral data of $M_n(\mathbb{R})$ is exactly the set of conjugation-stable multisets of size $n$.

**The signs of the coefficients give the signs of the real roots only in special cases.** For $n=2$, $\chi_A(t)=t^{2}-(\operatorname{tr}A)t+\det A$, and the discriminant $\Delta=(\operatorname{tr}A)^{2}-4\det A$ decides: two real roots for $\Delta>0$, a double real root for $\Delta=0$, a conjugate pair for $\Delta<0$. At $n=3$ the discriminant is a polynomial of degree four in the coefficients, and its sign separates the three real roots from one real and one pair.

**A positive determinant is compatible with a nonreal spectrum, and a negative one is not.** If $\det A<0$ then $e_n<0$, and the product of the eigenvalues is negative; a conjugation-stable multiset with negative product must contain a real negative eigenvalue, because each conjugate pair contributes $|\mu|^{2}>0$. Hence $\det A<0$ forces a real negative eigenvalue, while $\det A>0$ forces nothing of the kind.

**The sum of the principal minors can be negative while the matrix is symmetric positive definite.** $e_2$ is not a norm and has no sign in general; for $A=\operatorname{diag}(2,-1)$ one has $e_1=1$ and $e_2=-2$. The positivity statements of the theory concern the trace form and the Hilbert–Schmidt form, not the coefficients.

## The Invariant Ring

**The $e_k$ generate the ring of polynomial invariants of the conjugation action.** A polynomial $f$ on $M_n(\mathbb{R})$ with $f(SAS^{-1})=f(A)$ for all $S\in\mathrm{GL}_n(\mathbb{R})$ is a polynomial in the coefficients of $\chi_A$. The reason is that the coefficients separate the semisimple orbits: two semisimple matrices with the same characteristic polynomial are similar over $\mathbb{R}$ when their real Jordan forms agree, and the polynomial invariants cannot see the nilpotent part, which is why the ring is the polynomial ring on $n$ generators.

**The degrees of the generators are $1,2,\dots,n$, and their sum is $n(n+1)/2$.** So the invariant ring is a polynomial ring on $n$ generators of those degrees, and the algebraic quotient $M_n(\mathbb{R})/\!/\mathrm{GL}_n(\mathbb{R})$ has dimension $n$. The number $n(n+1)/2$ coincides with the dimension of $\operatorname{Sym}_n$, which is not an accident: the quotient can be read as the space of symmetric matrices modulo the orthogonal group, which is *The Cartan Decomposition of $\mathrm{GL}_n(\mathbb{R})$*.

**The ring is the same over $\mathbb{C}$, and the real structure enters through the fibres.** The generators are the same polynomials. What differs is the fibre: over $\mathbb{C}$ the fibre over a polynomial with distinct roots is a single orbit, while over $\mathbb{R}$ it is a finite union of orbits, one for each way of grouping the roots into real points and conjugate pairs.

## The Derivative and $\det e^{A}$

**Jacobi's formula: the derivative of the determinant is the cofactor matrix.** For $A$ invertible,

$$
\frac{d}{dt}\Big|_{t=0}\det(A+tB)=\det(A)\operatorname{tr}(A^{-1}B).
$$

*Proof.* $\det(A+tB)=\det A\det(\mathrm{I}+tA^{-1}B)$, and the expansion of §*The Expansion of $\det(\mathrm{I}+tA)$* gives $\det(\mathrm{I}+tA^{-1}B)=1+t\operatorname{tr}(A^{-1}B)+O(t^{2})$.

**Consequence: the logarithmic derivative of $\det$ along a path is the trace.** If $A(t)$ is differentiable and invertible then

$$
\frac{d}{dt}\log\det A(t)=\operatorname{tr}\bigl(A(t)^{-1}A'(t)\bigr).
$$

**Consequence: $\det e^{A}=e^{\operatorname{tr}A}$.** Apply the formula to $A(t)=e^{tA}$, whose derivative is $Ae^{tA}$. Then $A(t)^{-1}A'(t)=A$ and the logarithmic derivative is the constant $\operatorname{tr}A$; integrating from $0$ to $1$ and using $\det e^{0}=1$ gives the identity. Both sides are real, and the identity holds for every real matrix, with no eigenvalue and no diagonalisation.

## Summary

The coefficient $e_k$ of the real characteristic polynomial is the sum of the $\binom{n}{k}$ principal $k\times k$ minors and the $k$-th elementary symmetric function of the eigenvalues. The generating function is $\det(\mathrm{I}+tA)=\sum_ke_kt^{k}$, and Newton's identities express the $e_k$ as integer polynomials in the power sums $p_k=\operatorname{tr}(A^{k})$. All coefficients are real, the sign of the determinant forces a negative real eigenvalue, and the $e_k$ generate the ring of polynomial invariants, with degrees $1,\dots,n$ summing to $n(n+1)/2$. Jacobi's formula gives the logarithmic derivative of the determinant and the identity $\det e^{A}=e^{\operatorname{tr}A}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e_k(A)$ | the sum of the principal $k\times k$ minors |
| $p_k=\operatorname{tr}(A^{k})$ | the $k$-th power sum |
| $A_S$ | the principal submatrix on the index set $S$ |
| $\chi_A(t)$ | the characteristic polynomial, $\sum_k(-1)^{k}e_kt^{n-k}$ |
| $\Delta$ | the discriminant, of degree $2n-2$ in the coefficients |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the principal minors and the coefficients of the characteristic polynomial.
- Ian G. Macdonald, *Symmetric Functions and Hall Polynomials* (Oxford, 1995), for the elementary symmetric functions and Newton's identities.
- [The Element: Rank, Trace, Determinant, Characteristic Polynomial over $\mathbb{R}$](the-element-rank-trace-determinant-characteristic-polynomial-over-r.html), for the four invariants.
- [The Elementary Symmetric Functions and $\det(\mathrm{I}+tA)$](the-elementary-symmetric-functions-and-det-i-plus-ta.html), for the complex case.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the trace and the determinant.
