# __The Elementary Symmetric Functions and $\det(\mathrm{I}+tA)$__

## Introduction

**One polynomial carries the whole spectrum of $A$: the generating polynomial $\det(\mathrm{I}+tA)$ has the elementary symmetric functions of $A$ as its coefficients, and those coefficients are the complete set of conjugation-invariant polynomial functions on the algebra.**

The article defines $e_k(A)$ as the sum of the principal $k\times k$ minors, proves that $\det(\mathrm{I}+tA)=\sum_k e_k(A)t^{k}$, derives Newton's identities that recover the $e_k$ from the power sums $\operatorname{tr}(A^{m})$, and shows that the $e_k$ generate the ring of invariant polynomials with no relation among them. The last two sections read the derivative at the origin, which is the trace and which forces $\det e^{A}=e^{\operatorname{tr}A}$, and the case $n=2$. It assumes *The Element: Rank, Trace, Determinant, Characteristic Polynomial* for the four invariants and for the characteristic polynomial. It defers the structure of the invariant ring as a symmetric algebra to *The Trace Form and Its Inertia on the Two Halves*, and the exponential itself to *The Exponential of a Matrix and Its Image*.

## The Elementary Symmetric Functions

**The $k$-th elementary symmetric function of a matrix is the sum of its principal $k\times k$ minors.** For $A\in M_n(\mathbb{C})$ and $0\le k\le n$, write $K$ for a subset of $\{1,\dots,n\}$ of size $k$ and $A_K$ for the submatrix on the rows and columns of $K$. Then

$$
e_k(A)=\sum_{|K|=k}\det A_K,\qquad e_0=1,\qquad e_1=\operatorname{tr}A,\qquad e_n=\det A .
$$

There are $\binom{n}{k}$ summands, so $e_k$ is a homogeneous polynomial of degree $k$ in the entries. The definition uses principal submatrices only; the non-principal minors enter the rank but not the spectrum.

**The $e_k$ are the elementary symmetric functions of the eigenvalues.** If $A$ is triangular with diagonal $\lambda_1,\dots,\lambda_n$, then $A_K$ is triangular with diagonal the corresponding $\lambda$'s, so $\det A_K$ is the product of those $\lambda$'s and $e_k$ is the sum of all products of $k$ distinct eigenvalues. Both sides are polynomial in the entries and the triangular matrices are dense, so the identity holds for all $A$.

**At $n=2$ and $n=3$ the list is short.**

$$
e_1=\operatorname{tr}A,\qquad e_2=\tfrac12\big((\operatorname{tr}A)^{2}-\operatorname{tr}(A^{2})\big),\qquad e_3=\det A
$$

at $n=3$, with $e_2$ also equal to the sum of the three principal $2\times2$ minors. The identity $e_2=\tfrac12((\operatorname{tr}A)^{2}-\operatorname{tr}A^{2})$ is the case $k=2$ of Newton's identities and holds at every $n$.

## The Generating Polynomial

**The polynomial $\det(\mathrm{I}+tA)$ has the $e_k$ as coefficients.** For every $A$ and every scalar $t$,

$$
\det(\mathrm{I}+tA)=\sum_{k=0}^{n}e_k(A)\,t^{k}.
$$

*Proof.* Expand the determinant by the Leibniz rule over the $n$ columns. The column $j$ of $\mathrm{I}+tA$ is $e_j+tA_{\cdot j}$, and a term of the expansion chooses, for each $j$, either the unit column $e_j$ or the column $tA_{\cdot j}$. The columns where $tA$ is chosen form a set $K$; the remaining columns are unit vectors, so the term is nonzero only if those unit vectors occupy the rows of the complement of $K$, and the value is then $t^{|K|}\det A_K$. Summing over $K$ gives the formula.

**The same polynomial read at $t=-1/t'$ gives the characteristic polynomial.** Since $\chi_A(t)=t^{n}\det(\mathrm{I}-A/t)$,

$$
\chi_A(t)=\sum_{k=0}^{n}(-1)^{k}e_k(A)\,t^{n-k},
$$

which is the coefficient statement of *The Element: Rank, Trace, Determinant, Characteristic Polynomial*, now with the $e_k$ named and computable from the minors.

**The polynomial is multiplicative across a product in either order.** For square $A,B$ of the same size,

$$
\det(\mathrm{I}+tAB)=\det(\mathrm{I}+tBA).
$$

*Proof.* For invertible $A$, $\mathrm{I}+tAB=A(\mathrm{I}+tBA)A^{-1}$. Both sides are polynomial in the entries of $A$, and the invertible matrices are dense, so the identity extends to all $A$. The consequence is that $AB$ and $BA$ have the same characteristic polynomial and hence the same $e_k$ for every $k$, although they need not be conjugate.

**A table of the first cases.**

| $n$ | $\det(\mathrm{I}+tA)$ |
|---|---|
| $2$ | $1+t\operatorname{tr}A+t^{2}\det A$ |
| $3$ | $1+t\operatorname{tr}A+t^{2}e_2+t^{3}\det A$ |
| $4$ | $1+t\operatorname{tr}A+t^{2}e_2+t^{3}e_3+t^{4}\det A$ |

The middle coefficients at $n\ge4$ are new data, and they are the reason that the trace and the determinant do not determine the spectrum beyond $n=2$.

## Newton's Identities and the Power Sums

**The power sums determine the $e_k$, and Newton's identities give the recursion.** Put $p_i=\operatorname{tr}(A^{i})=\sum_k\lambda_k^{i}$. Then for $1\le k\le n$,

$$
k\,e_k=\sum_{i=1}^{k}(-1)^{i-1}e_{k-i}\,p_i .
$$

For $k=1$ this reads $e_1=p_1$, for $k=2$ it reads $2e_2=e_1p_1-p_2$, and for $k=3$ it reads $3e_3=e_2p_1-e_1p_2+p_3$. The identity is the statement that the generating functions are related by

$$
\sum_{k\ge0}e_kt^{k}=\exp\Big(\sum_{i\ge1}(-1)^{i-1}\frac{p_i}{i}t^{i}\Big),
$$

which is the expansion of $\prod_k(1+t\lambda_k)$ in terms of $\log(1+t\lambda_k)$.

**The recursion shows that the $n$ power sums $p_1,\dots,p_n$ carry the same information as the $n$ coefficients.** Each $e_k$ is a polynomial in $p_1,\dots,p_k$ with rational coefficients, and conversely $p_k$ is a polynomial in $e_1,\dots,e_k$. The two lists are two bases of the same ring, and neither is smaller.

**The trace is the derivative of the determinant along the identity, and the other $e_k$ are the higher derivatives.** Expanding at $t=0$,

$$
\det(\mathrm{I}+tA)=1+t\operatorname{tr}A+\tfrac12t^{2}\big((\operatorname{tr}A)^{2}-\operatorname{tr}A^{2}\big)+\cdots,
$$

so the first derivative is $\operatorname{tr}$ and the second is $2e_2$. This reading is the one used for the exponential in §*The Derivative at the Origin*.

## The Invariant Ring

**A polynomial function on the algebra is conjugation invariant exactly when it is a polynomial in the $e_k$.** Let $\mathbb{C}[M_n]$ be the polynomial ring in the $n^{2}$ entries. Then

$$
\mathbb{C}[M_n]^{GL_n}=\mathbb{C}[e_1,\dots,e_n],
$$

the subring of invariants is a polynomial ring in $n$ generators, of degrees $1,2,\dots,n$.

**The $n$ generators are algebraically independent, and their degrees sum to $n(n+1)/2$.** Independence holds because the Jacobian of $(e_1,\dots,e_n)$ with respect to the diagonal entries is the Vandermonde determinant of $\lambda_1,\dots,\lambda_n$, which is nonzero on the diagonal matrices with distinct eigenvalues; a relation among the $e_k$ would therefore vanish on an open set of diagonal matrices and be zero. The degree sum is

$$
1+2+\cdots+n=\frac{n(n+1)}{2}=3,6,10,15,21\quad\text{for }n=2,3,4,5,6 .
$$

This number is also the dimension of the space of symmetric matrices, the carrier of the Jordan algebra of *The Jordan Algebra $\operatorname{Sym}_n$*, and the coincidence is not accidental: on a symmetric matrix the $e_k$ are read from symmetric data.

**The rank is not an invariant of this ring.** The rank is not a polynomial function: it is the largest $r$ with a nonzero minor, and the vanishing of all $(r+1)\times(r+1)$ minors is a closed condition, not an equation. So the polynomial invariants see the spectrum and not the size of the image, which is the algebraic form of the failure recorded in *The Element: Rank, Trace, Determinant, Characteristic Polynomial*.

## The Derivative at the Origin

**The logarithmic derivative of the determinant is the trace.** For a differentiable family $A(t)$ with $A(0)=\mathrm{I}$,

$$
\frac{d}{dt}\Big|_{t=0}\det A(t)=\operatorname{tr}\dot A(0),
$$

which is Jacobi's formula $\frac{d}{dt}\det A=\det A\cdot\operatorname{tr}(A^{-1}\dot A)$ evaluated at the identity. Applied to $A(t)=\mathrm{I}+tA$ it recovers the coefficient $e_1=\operatorname{tr}A$.

**The formula forces $\det e^{A}=e^{\operatorname{tr}A}$.** Let $f(t)=\det e^{tA}$. Jacobi's formula with $A(t)=e^{tA}$ and $\dot A=A(t)A$ gives

$$
f'(t)=f(t)\operatorname{tr}A,\qquad f(0)=1,
$$

so $f(t)=e^{t\operatorname{tr}A}$ and $t=1$ is the statement. This is the only place where the determinant and the trace are tied by a formula rather than by a coefficient, and it is used in *The Exponential of a Matrix and Its Image* to place the exponential inside $SL_n(\mathbb{C})$.

**The same computation at the level of the $e_k$ gives the derivative of each coefficient.** Differentiating $\det(\mathrm{I}+tA)=\sum_ke_kt^{k}$ in $t$ and setting $t=0$ gives $e_1$, and differentiating $k$ times gives $k!e_k$. So the whole polynomial is the Taylor expansion of the determinant along the line $\mathrm{I}+tA$, and the $e_k$ are its Taylor coefficients divided by $k!$.

## The Case $n=2$

**At $n=2$ the polynomial has three terms and the pair $(e_1,e_2)$ is the whole spectrum.** For $A\in M_2(\mathbb{C})$,

$$
\det(\mathrm{I}+tA)=1+t\operatorname{tr}A+t^{2}\det A,\qquad e_2=\det A=\tfrac12\big((\operatorname{tr}A)^{2}-\operatorname{tr}(A^{2})\big).
$$

Newton's identity at $k=2$ is the second formula, and it is the reason that a $2\times2$ matrix satisfies its own characteristic polynomial with no intermediate coefficient.

**The invariant ring at $n=2$ has two generators of degrees $1$ and $2$, summing to $3$.** The conjugation orbits in $M_2(\mathbb{C})$ are therefore described by two numbers, $\operatorname{tr}$ and $\det$, with the discriminant

$$
\Delta=(\operatorname{tr}A)^{2}-4\det A
$$

separating the two distinct eigenvalues from the double one. The orbits are the strata of *The Minimal Polynomial and the Jordan Form*: two distinct eigenvalues, one eigenvalue with a diagonalisable matrix, and one eigenvalue with a nontrivial Jordan block, the last being the single orbit of $A\ne\lambda\mathrm{I}$ with $\Delta=0$.

**The biquaternion norm is not the determinant.** At $n=2$ the algebra is the biquaternion algebra $\mathbb{B}$, and the article *Introduction to the Algebra of Biquaternions* attaches to each element a real norm $N$. That norm is real-valued and indefinite, while $\det$ is complex-valued and multiplicative; the two agree in neither inertia nor domain. The determinant of the matrix of $q$ is the complex number $\det q$, and the statement $N(q)=\det q$ is false for a biquaternion. What survives is the trace: $\operatorname{tr}$ is complex-linear on $\mathbb{B}$, and its real part is the real part of the biquaternion trace.

## Summary

The elementary symmetric functions $e_k(A)$, the sum of the principal $k\times k$ minors, are the coefficients of $\det(\mathrm{I}+tA)=\sum_ke_k(A)t^{k}$, and they are the elementary symmetric functions of the eigenvalues. Newton's identities recover them from the power sums $\operatorname{tr}(A^{m})$ by a recursion with rational coefficients, so the two lists carry the same information. The $e_k$ are algebraically independent and generate the ring of conjugation-invariant polynomials, with degrees $1,\dots,n$ summing to $n(n+1)/2$. The derivative of $\det(\mathrm{I}+tA)$ at the origin is $\operatorname{tr}A$, and Jacobi's formula turns that into $\det e^{A}=e^{\operatorname{tr}A}$. At $n=2$ the polynomial is $1+t\operatorname{tr}A+t^{2}\det A$, and the biquaternion norm $N$ is not the determinant.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e_k(A)$ | the sum of the principal $k\times k$ minors of $A$ |
| $A_K$ | the principal submatrix on the index set $K$ |
| $\det(\mathrm{I}+tA)$ | the generating polynomial of the $e_k$ |
| $p_i=\operatorname{tr}(A^{i})$ | the $i$-th power sum of the eigenvalues |
| $\mathbb{C}[M_n]^{GL_n}$ | the ring of conjugation-invariant polynomials |
| $\Delta=(\operatorname{tr}A)^{2}-4\det A$ | the discriminant at $n=2$ |
| $N$ | the indefinite biquaternion norm, not the determinant |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the expansion of $\det(\mathrm{I}+tA)$ and Newton's identities.
- Israel M. Gelfand, *Lectures on Linear Algebra* (Dover, 1989), for the elementary symmetric functions of the spectrum and their generating polynomial.
- David Cox, John Little and Donal O'Shea, *Ideals, Varieties, and Algorithms* (Springer, 2015), for the invariant ring of the conjugation action and the algebraic independence of the generators.
- [The Element: Rank, Trace, Determinant, Characteristic Polynomial](the-element-rank-trace-determinant-characteristic-polynomial.html), for the four invariants and the coefficient form of $\chi_A$.
- [The Frame, the Simple Nilpotents and the Frame Group of $M_n(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-frame-group-of-mnc.html), for the degree count $n(n+1)/2$ against the frame count.
- [The Biquaternion Algebra](introduction-to-the-algebra-of-biquaternions.html), for the indefinite norm $N$ that is not the determinant.
