# __The Element: Rank, Trace, Determinant, Characteristic Polynomial__

## Introduction

**Four invariants measure an element of $M_n(\mathbb{C})$, and they are ordered by how much of it they remember: the rank remembers the image, the trace and the determinant remember two symmetric functions of the spectrum, and the characteristic polynomial remembers all the symmetric functions but not the element.**

The article defines the four invariants, proves their elementary properties, and states exactly what each one loses. The rank is computed from the minors and from the kernel, the trace is characterised as the only invariant linear functional, the determinant is characterised as the multiplicative polynomial of degree $n$, and the characteristic polynomial collects the coefficients. The article ends with the failure: two matrices with the same characteristic polynomial and different ranks. It assumes *The Matrix Algebra $M_n(\mathbb{C})$* for the algebra and *The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$* for the behaviour of the invariants under conjugation. It defers the classification of the elements to *The Minimal Polynomial and the Jordan Form* and the finer symmetric functions to *The Elementary Symmetric Functions and $\det(\mathrm{I}+tA)$*.

## The Rank

**The rank is the dimension of the image, and it is also the dimension of the image of the transpose.** For $A\in M_n(\mathbb{C})$,

$$
\operatorname{rank}A=\dim\operatorname{im}A=n-\dim\ker A=\dim\operatorname{im}A^{\mathsf T}.
$$

The last equality is the statement that the row rank equals the column rank: the row space of $A$ is the column space of $A^{\mathsf T}$, and both have dimension equal to the size of the largest nonvanishing minor. The rank is an integer between $0$ and $n$, it is invariant under conjugation by an invertible element, and $\operatorname{rank}A=n$ is exactly invertibility.

**The rank is the number of nonzero singular values.** For every $A$ there are unitaries $U,V$ with $A=U\Sigma V^{*}$ and $\Sigma$ diagonal with entries $\sigma_1\ge\cdots\ge\sigma_n\ge0$. Then $\operatorname{rank}A$ is the number of nonzero $\sigma_k$, and

$$
\operatorname{tr}(A^{*}A)=\sum_{k}\sigma_k^{2}.
$$

This is the reading of the rank through the positive definite trace form of *The Matrix Algebra $M_n(\mathbb{C})$*, and it is the reason the rank of $A$ equals the rank of $A^{*}A$ and of $AA^{*}$.

**The rank is subadditive and multiplicative in the weak sense.** For all $A,B$,

$$
\operatorname{rank}(A+B)\le\operatorname{rank}A+\operatorname{rank}B,\qquad
\operatorname{rank}(AB)\le\min(\operatorname{rank}A,\operatorname{rank}B),\qquad
\operatorname{rank}(AB)\ge\operatorname{rank}A+\operatorname{rank}B-n .
$$

The middle inequality is the inclusion $\operatorname{im}AB\subseteq\operatorname{im}A$ together with $\ker AB\supseteq\ker B$. The last is Sylvester's inequality, and it is sharp: the deficiency of $AB$ is at most the sum of the deficiencies of the factors.

**The strata by rank are the orbits of the group on the singular set.** Let $\Sigma_r=\{A:\operatorname{rank}A=r\}$. Then $\Sigma_r$ is a single orbit under $A\mapsto UAV$ with $U,V$ invertible, and its complex dimension is

$$
\dim_{\mathbb{C}}\Sigma_r=r(2n-r),\qquad r=0,\dots,n .
$$

At $n=3$ the values are $0,5,8$ for $r=0,1,2$, and at $n=4$ they are $0,7,12,15$. The formula is the count of an $r$-dimensional subspace of the domain and an $r$-dimensional subspace of the codomain together with an invertible map between them: $r(n-r)+r(n-r)+r^{2}=r(2n-r)$.

## The Trace

**The trace is linear, vanishes on commutators, and is the only such functional up to scale.** Linearity is clear, and

$$
\operatorname{tr}(AB)=\sum_{i,j}A_{ij}B_{ji}=\operatorname{tr}(BA)
$$

is the cyclic rule. Conversely, let $f$ be a linear functional with $f(AB)=f(BA)$ for all $A,B$. Taking $A=E_{ij}$ and $B=E_{ji}$ for $i\ne j$ gives $f(E_{ii})=f(E_{jj})$, and taking $A=E_{ij}$, $B=E_{kl}$ with $j\ne k$ gives $f(E_{il})=0$ for $i\ne l$. So

$$
f(A)=f(I)\cdot\frac{\operatorname{tr}A}{n},
$$

and the space of invariant linear functionals is one-dimensional. A direct count at $n=3$ confirms it: the annihilator of the commutator span has dimension $1$ inside the $9$ dimensions of $M_3(\mathbb{C})$.

**The trace is the sum of the eigenvalues, counted with multiplicity.** In a triangular basis every matrix is upper triangular, and the diagonal carries the eigenvalues. So

$$
\operatorname{tr}A=\sum_{k=1}^{n}\lambda_k,\qquad \operatorname{tr}(A^{m})=\sum_{k=1}^{n}\lambda_k^{m},
$$

the second identity following from the first applied to $A^{m}$. The trace is therefore the first symmetric function of the spectrum, and it is blind to everything else.

**The trace of a commutator is zero, and the converse fails.** Every commutator $[A,B]=AB-BA$ has trace zero, and the traceless matrices are exactly $\mathfrak{sl}_n$, of complex dimension $n^{2}-1$. Over $\mathbb{C}$ the trace is the only obstruction: for $n\ge2$ every traceless matrix is a commutator $[A,B]$.

## The Determinant

**The determinant is the multiplicative polynomial of degree $n$ normalised at the identity.** It is defined by

$$
\det A=\sum_{\pi\in S_n}\operatorname{sgn}(\pi)\prod_{i=1}^{n}A_{i\pi(i)},
$$

it satisfies $\det(AB)=\det A\det B$, $\det I=1$, and $\det(\lambda A)=\lambda^{n}\det A$. It vanishes exactly on the non-invertible matrices, and then the cofactor formula gives the inverse,

$$
A\cdot\operatorname{adj}A=(\det A)I .
$$

**The determinant is the product of the eigenvalues, and it is the last coefficient of the characteristic polynomial.** With $\lambda_1,\dots,\lambda_n$ the eigenvalues counted with multiplicity,

$$
\det A=\prod_{k=1}^{n}\lambda_k,\qquad \det A=(-1)^{n}\chi_A(0).
$$

A multiplicative polynomial normalised at $I$ and homogeneous of degree $n$ equals $\det$, and every multiplicative polynomial normalised at $I$ is a power of $\det$. The uniqueness is what makes the determinant canonical rather than a choice.

**The determinant of a sum is not the sum of the determinants, and the defect is measured by the mixed discriminant.** For $n=2$,

$$
\det(A+B)=\det A+\det B+\operatorname{tr}A\operatorname{tr}B-\operatorname{tr}(AB),
$$

which shows that $\det$ is a quadratic form on $M_2(\mathbb{C})$ but not an additive function. The general expansion, with $\binom{n}{k}^{2}$ terms, is the subject of *The Elementary Symmetric Functions and $\det(\mathrm{I}+tA)$*.

## The Characteristic Polynomial

**The characteristic polynomial is monic of degree $n$, and its coefficients are the elementary symmetric functions of the spectrum.** Define

$$
\chi_A(t)=\det(tI-A)=t^{n}-e_1t^{n-1}+e_2t^{n-2}-\cdots+(-1)^{n}e_n,
$$

with $e_1=\operatorname{tr}A$, $e_n=\det A$, and $e_k$ the sum of the principal $k\times k$ minors. The $e_k$ are the elementary symmetric functions of $\lambda_1,\dots,\lambda_n$, and the identity is a polynomial identity in the entries.

**Cayley and Hamilton: the polynomial annihilates the matrix.** For every $A$,

$$
\chi_A(A)=0 .
$$

*Proof.* Over a dense open set $A$ is diagonalisable, and the statement is then the eigenvalue equation applied in an eigenbasis: $\prod_k(A-\lambda_k I)=0$ because the factors commute and each kills one eigendirection. Both sides of $\chi_A(A)=0$ are polynomial in the entries, and a polynomial that vanishes on a dense open set vanishes everywhere.

**The characteristic polynomial is conjugacy invariant and its degree is the size of the matrix.** For $S$ invertible, $\chi_{SAS^{-1}}=\chi_A$, since $\det(tI-SAS^{-1})=\det(S(tI-A)S^{-1})$. So $\chi$ is a function of the conjugacy class. It is a complete invariant at $n=2$ and at no larger $n$: the two nilpotents of §*What the Four Do Not Determine* share it and are not conjugate. The classification is in *The Minimal Polynomial and the Jordan Form*.

## What the Four Do Not Determine

**The characteristic polynomial does not determine the rank.** The two nilpotents

$$
N_1=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix},\qquad N_2=\begin{pmatrix}0&1&0\\0&0&0\\0&0&0\end{pmatrix}
$$

both have $\chi(t)=t^{3}$, and $\operatorname{rank}N_1=2$ against $\operatorname{rank}N_2=1$. The two are not conjugate, since the rank is a conjugacy invariant. So the four invariants together do not determine the element, and two matrices with equal trace, equal determinant and equal characteristic polynomial may still be far apart.

**The pair $(\operatorname{tr},\det)$ determines the characteristic polynomial only up to $n=2$.** For $n=2$ the polynomial is $t^{2}-(\operatorname{tr}A)t+\det A$, so the two numbers are the whole of it. For $n\ge3$ the intermediate coefficients $e_2,\dots,e_{n-1}$ are independent data, and $(\operatorname{tr},\det)$ loses them.

**The rank and the characteristic polynomial together do not determine the class either.** A matrix and its transpose have the same rank, the same trace, the same determinant and the same characteristic polynomial, and they are not always conjugate: a Jordan block of size $n\ge3$ is not conjugate to its transpose. What the invariants do give is a stratification, and the classification inside a stratum is the Jordan form.

| Invariant | What it remembers | What it loses |
|---|---|---|
| $\operatorname{rank}$ | the dimension of the image | everything about the eigenvalues |
| $\operatorname{tr}$ | the sum of the eigenvalues | the individual eigenvalues |
| $\det$ | the product of the eigenvalues | the individual eigenvalues, and invertibility is the only dichotomy it sees |
| $\chi_A$ | all the symmetric functions | the Jordan type inside a fixed spectrum |

## The Case $n=2$

**At $n=2$ the invariants collapse to two numbers and one identity.** For $A\in M_2(\mathbb{C})$,

$$
\chi_A(t)=t^{2}-(\operatorname{tr}A)t+\det A,\qquad A^{2}-(\operatorname{tr}A)A+(\det A)I=0 ,
$$

so the algebra generated by $A$ has dimension at most two unless $A$ is scalar. This is the identity used in the biquaternion articles: a biquaternion $q$ satisfies its own quadratic, and the two coefficients are the trace and the determinant of the matrix representing it.

**The rank at $n=2$ has three values and the middle one is split by the trace.** The rank is $0$ for $A=0$, it is $2$ exactly when $\det A\ne0$, and it is $1$ when $\det A=0$ and $A\ne0$. A rank-one matrix satisfies $A^{2}=(\operatorname{tr}A)A$, so it is a nonzero scalar multiple of an idempotent exactly when $\operatorname{tr}A\ne0$; when $\operatorname{tr}A=0$ it is nilpotent of index two. The two cases are the two kinds of Peirce line of *The Peirce Decomposition in $n$ Dimensions* at $n=2$.

## Summary

The four invariants of $A\in M_n(\mathbb{C})$ are the rank, the trace, the determinant and the characteristic polynomial. The rank is the dimension of the image, equal to the number of nonzero singular values, subadditive, and the strata $\Sigma_r$ have complex dimension $r(2n-r)$. The trace is the only invariant linear functional up to scale, and it is the sum of the eigenvalues. The determinant is the multiplicative polynomial of degree $n$, equal to the product of the eigenvalues and to $(-1)^{n}\chi_A(0)$. The characteristic polynomial is monic of degree $n$ with the elementary symmetric functions as coefficients, and Cayley–Hamilton says $\chi_A(A)=0$. The four do not determine the element: two nilpotents can share $\chi(t)=t^{3}$ and differ in rank, and the pair $(\operatorname{tr},\det)$ determines $\chi$ only for $n=2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{rank}A$ | the dimension of $\operatorname{im}A$, an integer in $[0,n]$ |
| $\Sigma_r$ | the set of matrices of rank $r$, of complex dimension $r(2n-r)$ |
| $\operatorname{tr}A$ | the sum of the diagonal entries, and the sum of the eigenvalues |
| $\det A$ | the product of the eigenvalues, the multiplicative polynomial of degree $n$ |
| $\operatorname{adj}A$ | the adjugate, with $A\operatorname{adj}A=(\det A)I$ |
| $\chi_A(t)=\det(tI-A)$ | the characteristic polynomial |
| $e_k$ | the $k$-th elementary symmetric function, the sum of the principal $k\times k$ minors |
| $[A,B]=AB-BA$ | the commutator, of trace zero |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the rank, its inequalities, the determinant and the characteristic polynomial.
- Peter Lancaster and Miron Tismenetsky, *The Theory of Matrices* (Academic Press, 1985), for the uniqueness of the trace functional and the cofactor formula.
- Sheldon Axler, *Linear Algebra Done Right* (Springer, 2015), for the determinant as the unique alternating multilinear form.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the trace, the determinant and the singular set.
- [The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$](the-two-base-fields-mnr-inside-mnc.html), for the reality of the invariants and the conjugation-stable spectrum.
- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the two kinds of line at $n=2$.
