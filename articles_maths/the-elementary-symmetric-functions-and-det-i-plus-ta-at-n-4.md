# __The Elementary Symmetric Functions and $\det(\mathrm{I}+tA)$ at $n=4$__

## Introduction

**The four coefficients of $\det(\mathrm I+tA)$ are the elementary symmetric functions of the eigenvalues, and they are polynomials in the traces of the powers of $A$: $e_1=\operatorname{tr}A$ up to the trace itself, $e_4=\det A$, and the two middle ones carry the information the ends lose.**

The article defines the four coefficients, proves Newton's identities that express them through the power sums, identifies $e_k$ with the trace of $A$ on the $k$-th exterior power so that the ladder of dimensions $1,4,6,4,1$ appears, shows that each $e_k$ is invariant under conjugation and that each level set $\{e_k=0\}$ is a hypersurface, and reads the four coefficients in the axis-free basis, where $e_1=4c_{tt}$ and $e_4$ is the square of the quaternionic norm.

It assumes *The Element, the Coordinates and the Trace of $M_4(\mathbb{C})$* for the coordinates, and *The Matrix Algebra $M_4(\mathbb{C})$* for the product and the determinant. The general order is *The Elementary Symmetric Functions, the Trace and the Determinant*; the case $n=2$ is *The Elementary Symmetric Functions: $\operatorname{tr}$ and $\det$ in Dimension Two*. The spectral reading of the same numbers is *The Spectral Theorem: the Hermitian Case at $n=4$*.

## The Four Coefficients

**Definition.** For $A\in M_4(\mathbb{C})$ the **elementary symmetric functions** are the coefficients of the polynomial in $t$,

$$
\det(\mathrm I+tA)=\sum_{k=0}^{4}e_k(A)\,t^{k},\qquad e_0=1,\quad e_4=\det A .
$$

**Proposition.** The coefficient $e_k$ is the $k$-th elementary symmetric function of the eigenvalues, counted with multiplicity:

$$
e_k=\sum_{i_1<\cdots<i_k}\lambda_{i_1}\cdots\lambda_{i_k}.
$$

**Proof.** Over $\mathbb{C}$ the matrix is triangularisable, $A=PTP^{-1}$ with $T$ upper triangular; then $\mathrm I+tA=P(\mathrm I+tT)P^{-1}$ and $\det(\mathrm I+tT)=\prod_i(1+t\lambda_i)$. Expanding the product collects $t^{k}$ with the sum of the $k$-fold products of distinct eigenvalues.

**Corollary.** The four coefficients are $e_1=\sum\lambda_i$, $e_2=\sum_{i<j}\lambda_i\lambda_j$, $e_3=\sum_{i<j<k}\lambda_i\lambda_j\lambda_k$ and $e_4=\lambda_1\lambda_2\lambda_3\lambda_4$.

**Proof.** Expand the product $\prod_i(1+t\lambda_i)$ and read the coefficient of $t^{k}$.

**The polynomial at $t=-1$ and at large $t$.** At $t=-1$ the identity gives $\det(\mathrm I-A)=\sum_k(-1)^{k}e_k$, the value at the eigenvalue $1$; at $t\to\infty$ it gives $e_4=\det A$. The four coefficients thus interpolate between the trace and the determinant.

## Newton's Identities

**Definition.** The **power sums** are $p_k=\operatorname{tr}(A^{k})=\sum_i\lambda_i^{k}$, for $k=1,2,3,4$.

**Theorem (Newton).** For $1\le k\le4$,

$$
k\,e_k=\sum_{i=1}^{k}(-1)^{i-1}e_{k-i}\,p_i .
$$

**Proof.** Differentiate the identity $\log\det(\mathrm I+tA)=\sum_i\log(1+t\lambda_i)$ at $t$ and multiply by $t$: the left side is $t\operatorname{tr}\bigl(A(\mathrm I+tA)^{-1}\bigr)$ and the right side is $\sum_{k\ge1}(-1)^{k-1}p_kt^{k}$. Comparing coefficients in the expansion of $E(t)=\det(\mathrm I+tA)$ gives the recursion $k e_k=\sum_{i=1}^{k}(-1)^{i-1}e_{k-i}p_i$.

**Corollary (the four identities written out).**

$$
p_1=e_1,\qquad p_2=e_1p_1-2e_2,\qquad p_3=e_1p_2-e_2p_1+3e_3,\qquad p_4=e_1p_3-e_2p_2+e_3p_1-4e_4 .
$$

**Proof.** Substitute $k=1,2,3,4$ in the theorem and collect.

**Corollary (the coefficients through the traces).**

$$
e_1=\operatorname{tr}A,\qquad
e_2=\tfrac12\bigl[(\operatorname{tr}A)^{2}-\operatorname{tr}(A^{2})\bigr],
$$

$$
e_3=\tfrac16\bigl[(\operatorname{tr}A)^{3}-3\operatorname{tr}A\operatorname{tr}(A^{2})+2\operatorname{tr}(A^{3})\bigr],\qquad
e_4=\det A .
$$

**Proof.** Solve the four identities for $e_1,e_2,e_3$ in turn: $e_2=\tfrac12(p_1^{2}-p_2)$, then $e_3=\tfrac13(p_3-e_1p_2+e_2p_1)$, which reduces to the display.

**The first three are determined by traces, the fourth is not.** The traces of $A,A^{2},A^{3}$ determine $e_1,e_2,e_3$; the determinant needs one more number. Equivalently, $\mathrm{tr}(A^{k})$ for $k=1,2,3$ fixes the characteristic polynomial up to the constant term, and the constant term is $\det A$.

## The Exterior Powers and the Ladder $1,4,6,4,1$

**Theorem.** $e_k(A)=\operatorname{tr}\bigl(\Lambda^{k}A\bigr)$, the trace of the induced map on the $k$-th exterior power of $\mathbb{C}^{4}$.

**Proof.** The eigenvalues of $\Lambda^{k}A$ are the products $\lambda_{i_1}\cdots\lambda_{i_k}$ over the $k$-element subsets, each once; their sum is $e_k$ by the first proposition.

**Corollary.** The four coefficients live on spaces of dimensions $1,4,6,4,1$:

$$
\dim\Lambda^{0}=\dim\Lambda^{4}=1,\qquad \dim\Lambda^{1}=\dim\Lambda^{3}=4,\qquad \dim\Lambda^{2}=6 .
$$

**Proof.** The binomial coefficients $\binom{4}{k}$ for $k=0,1,2,3,4$, and $\Lambda^{2}\mathbb{C}^{4}$ also has dimension the dimension of the antisymmetric half, $6$.

**The two readings of the middle coefficient.** $e_2$ is the trace on $\Lambda^{2}\mathbb{C}^{4}$, and it is also the sum of the six principal $2\times2$ minors of $A$. The identity $\operatorname{tr}(\Lambda^{2}A)=\sum_{i<j}\det A_{[i,j]}$ is the Cauchy–Binet theorem applied to the six coordinate projections.

**The four coefficients and the four forms.** $e_1$ and $e_4$ are the trace and the determinant of the algebra; $e_2$ and $e_3$ are the coefficients that distinguish the two middle exterior powers. At $n=4$ all four are needed: the characteristic polynomial has degree four and no two of its coefficients are functions of the others.

## Invariance and the Strata

**Proposition.** Each $e_k$ is invariant under conjugation: $e_k(PAP^{-1})=e_k(A)$ for invertible $P$.

**Proof.** The eigenvalues are unchanged by conjugation, and each $e_k$ is a symmetric function of them. Equivalently, $\det(\mathrm I+tPAP^{-1})=\det P\det(\mathrm I+tA)\det P^{-1}$.

**Corollary.** Each $e_k$ is a polynomial in the entries invariant under $\mathrm{GL}_4$, and the four together generate the invariant ring of the conjugation action on the sixteen coordinates.

**Proof.** The invariant ring of $n\times n$ matrices under conjugation is generated by the coefficients of the characteristic polynomial, and at $n=4$ those are $e_1,e_2,e_3,e_4$.

**The strata.** Each set $\{e_k=0\}$ is a hypersurface, of complex dimension $15$ in the space of dimension $16$, except that $\{e_2=0\}$ and $\{e_3=0\}$ are singular at the origin.

| Stratum | Equation | Reading |
|---|---|---|
| traceless hyperplane | $e_1=0$ | $\mathfrak{sl}_4$, dimension $15$ |
| the quadric | $e_2=0$ | rank at most two, or trace data of a degenerate pair |
| the cubic | $e_3=0$ | one eigenvalue zero, or three summing to zero |
| the singular set | $e_4=0$ | $\det A=0$, rank at most three |

**Proposition.** The singular set $\{e_4=0\}$ is exactly the set of non-invertible matrices, and it is a hypersurface whose smooth part has complex dimension $15$.

**Proof.** $\det A=0$ is the condition of non-invertibility, and the derivative of the determinant at $A$ is $X\mapsto\operatorname{tr}(\operatorname{adj}(A)X)$, which is nonzero whenever $\operatorname{adj}(A)\neq0$, that is whenever $\operatorname{rank}A\ge3$.

## The Axis-Free Reading

**The four coordinates.** Write $A=\sum_{\mu,\nu}c_{\mu\nu}T_{\mu\nu}$ in the axis-free basis $T_{\mu\nu}=L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$; the matrix units are the basis in which the product is defined, and the axis-free sixteen are the basis in which the coefficients are read by traces. The trace is one coordinate, $e_1=\operatorname{tr}A=4c_{tt}$, and the determinant is the fourth coefficient.

**The left matrix.** For $A=L_{\mathrm{axf}}(\tilde Q)$ the eigenvalues are $Q_t\pm iB$, each twice, with $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$. Hence

$$
\det(\mathrm I+tL_{\mathrm{axf}}(\tilde Q))=\bigl(1+2Q_tt+(Q_t^{2}+B^{2})t^{2}\bigr)^{2},
$$

and the four coefficients are

$$
e_1=4Q_t,\qquad e_2=6Q_t^{2}+2B^{2},\qquad e_3=4Q_t(Q_t^{2}+B^{2}),\qquad e_4=(Q_t^{2}+B^{2})^{2}.
$$

**Proof.** The eigenvalues come in two conjugate pairs, so the characteristic polynomial is the square of a quadratic; expanding the square gives the display, and $e_1=4Q_t$ agrees with the trace, while $e_4=\det L_{\mathrm{axf}}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^{2}$.

**The check at the identity and at the vector part.** At $Q_t=1$ and $B=0$ the display gives $e_2=6$, $e_3=4$, $e_4=1$, which is $\det(\mathrm I+t\mathrm I_4)=(1+t)^{4}$. At $Q_t=0$ the display gives $e_1=e_3=0$ and $e_2=2B^{2}$, $e_4=B^{4}$: the traceless left matrices have the spectrum $\pm iB$ twice.

**What the axis-free reading adds.** The determinant is the square of a quadratic form, and the quadratic form is the quaternionic norm $\langle\tilde Q\rangle_{\natural}$, which is the sum of four squares over $\mathbb{C}$ and a Euclidean norm on the real slice. The other three coefficients are the same norm together with the scalar coordinate. In the matrix-unit basis the four coefficients are the same numbers, written as sums over $4^{k}$ minors; the axis-free basis writes them as sums over four coordinates.

## Summary

The four coefficients of $\det(\mathrm I+tA)$ are the elementary symmetric functions of the eigenvalues, and Newton's identities express the first three through $\operatorname{tr}A$, $\operatorname{tr}(A^{2})$ and $\operatorname{tr}(A^{3})$, with $e_4=\det A$ independent of them. The coefficient $e_k$ is the trace of $A$ on the $k$-th exterior power, so the four live on spaces of dimensions $1,4,6,4,1$, and the middle one is also the sum of the six principal minors.

Each $e_k$ is invariant under conjugation, the four generate the invariant ring, and each level set is a hypersurface with the singular set $\{\det=0\}$ for the fourth. In the axis-free basis $e_1=4c_{tt}$ and $e_4=\langle\tilde Q\rangle_{\natural}^{2}$, and for a one-sided matrix the four coefficients are $4Q_t$, $6Q_t^{2}+2B^{2}$, $4Q_t(Q_t^{2}+B^{2})$ and $(Q_t^{2}+B^{2})^{2}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e_k$ | the $k$-th coefficient of $\det(\mathrm I+tA)$ |
| $p_k$ | $\operatorname{tr}(A^{k})$, the $k$-th power sum |
| $\lambda_i$ | the four eigenvalues, with multiplicity |
| $\Lambda^{k}A$ | the induced map on the $k$-th exterior power |
| $c_{\mu\nu}$ | the axis-free coordinates, $c_{tt}=e_1/4$ |
| $Q_t$, $B^{2}$ | the scalar coordinate and $Q_x^{2}+Q_y^{2}+Q_z^{2}$ |
| $\langle\tilde Q\rangle_{\natural}$ | $Q_t^{2}+B^{2}$, whose square is $e_4$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the characteristic polynomial, Newton's identities and the exterior powers.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the trace, the determinant and the rank.
- [The Element, the Coordinates and the Trace of $M_4(\mathbb{C})$](the-element-the-coordinates-and-the-trace-of-m4c.html), for the axis-free coordinates and the trace pairing.
- [The Quartic, the Discriminant and the Spectral Strata of $M_4(\mathbb{C})$](the-quartic-the-discriminant-and-the-spectral-strata-of-m4c.html), for the discriminant of the characteristic polynomial and the strata it cuts.
- [The Elementary Symmetric Functions: $\operatorname{tr}$ and $\det$ in Dimension Two](the-elementary-symmetric-functions-trace-and-determinant-in-dimension-two.html), for the same four identities at order two.
