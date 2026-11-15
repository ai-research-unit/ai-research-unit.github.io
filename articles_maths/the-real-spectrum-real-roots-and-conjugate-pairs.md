# __The Real Spectrum: Real Roots and Conjugate Pairs__

## Introduction

**The spectrum of a real matrix is stable under conjugation, and that one symmetry fixes the count of the eigenvalues, the trace, the determinant and the shape of the generalised eigenspaces.** The spectrum is a multiset in $\mathbb{C}$, but it is not an arbitrary multiset of $n$ points: it is the union of $r$ real points and $s$ conjugate pairs, with $r+2s=n$.

The article proves the stability of the spectrum under conjugation, the count $r+2s=n$, the reality of the generalised eigenspaces, the trace and the determinant in terms of $r$ and $s$, the emptiness of the real spectrum for the rotation $J$, the cases of symmetric and antisymmetric matrices, the reality of the elementary symmetric functions, and the attainment of the spectral radius. It assumes *The Element: Rank, Trace, Determinant, Characteristic Polynomial over $\mathbb{R}$*, and it defers the blocks to *The Real Jordan Form and the Rotation Blocks* and the orthonormal eigenbases to *The Spectral Theorem: the Symmetric Case*.

## The Spectrum and the Action of Conjugation

**The spectrum is the multiset of roots of $\chi_A$ in $\mathbb{C}$, with algebraic multiplicity.** By the factorisation of the characteristic polynomial,

$$
\chi_A(t)=\det(t\mathrm{I}-A)=t^{n}-e_1t^{n-1}+e_2t^{n-2}-\cdots+(-1)^{n}e_n,
$$

where $e_k$ is the sum of the principal $k\times k$ minors of $A$. Each $e_k$ is a real polynomial in the entries, so $\chi_A$ lies in $\mathbb{R}[t]$.

**Conjugation fixes $\chi_A$ coefficient by coefficient.** The coefficients are real numbers, so

$$
\chi_A(\bar\mu)=\overline{\chi_A(\mu)}
$$

for every $\mu\in\mathbb{C}$.

**Proposition.** If $\mu$ is an eigenvalue of $A$ then $\bar\mu$ is an eigenvalue with the same multiplicity.

*Proof.* The first claim is the identity above: $\chi_A(\mu)=0$ gives $\chi_A(\bar\mu)=0$. The multiplicity is the order of vanishing of $\chi_A$ at the root, and the order of vanishing of $\chi_A$ at $\bar\mu$ equals the order of vanishing of $\overline{\chi_A}$ at $\mu$, because the Taylor coefficients are conjugated. Since $\overline{\chi_A}=\chi_A$, the two orders agree.

**The conjugation acts on the spectrum as an involution with two kinds of orbits.** A fixed point is a real eigenvalue. A two-point orbit is a pair $\{\mu,\bar\mu\}$ with $\mu\notin\mathbb{R}$, and the two members have equal multiplicity. The spectrum is therefore the disjoint union of its real points and its pairs.

## The Count $r+2s=n$

**Definition.** Let $r$ be the number of real eigenvalues of $A$, counted with multiplicity, and let $2s$ be the number of nonreal eigenvalues, counted with multiplicity.

**Proposition.** $r+2s=n$, and $s$ is an integer with $0\le s\le\lfloor n/2\rfloor$.

*Proof.* The spectrum has $n$ members counted with multiplicity, because $\deg\chi_A=n$. The nonreal members fall into two-point orbits of equal size, so their number is even and equals $2s$ for the integer $s$ that counts the orbits. Adding the $r$ real members gives $n$. The bound $2s\le n$ gives $s\le\lfloor n/2\rfloor$.

**The parity of $n$ decides whether a real eigenvalue must exist.** If $n$ is odd then $r$ is odd, hence $r\ge1$, so every real matrix of odd size has at least one real eigenvalue. If $n$ is even then $r$ may be zero, and $r=0$ exactly when no eigenvalue is real.

**Example at $n=5$.** Take the real eigenvalue $2$ and the pairs $1\pm2i$ and $-1\pm i$, so that $r=1$ and $s=2$. Then

$$
\operatorname{tr}A=2+2\cdot1+2\cdot(-1)=2,\qquad \det A=2\cdot(1+4)\cdot(1+1)=20 .
$$

A random real change of basis preserves both numbers, and the computed trace and determinant of the conjugated matrix are $2$ and $20$.

## The Real Generalised Eigenspaces

**Definition.** For $\mu\in\sigma(A)$ the generalised eigenspace is $V_\mu=\ker(A-\mu\mathrm{I})^{m}$, where $m$ is the multiplicity of $\mu$.

**Proposition.** If $\lambda$ is a real eigenvalue then $V_\lambda$ has a basis of vectors of $\mathbb{R}^{n}$, and $\dim_{\mathbb{R}}V_\lambda$ is the multiplicity of $\lambda$.

*Proof.* The matrix $A-\lambda\mathrm{I}$ is real, so its powers are real, and the kernel of a real matrix is defined by real linear equations; a real matrix in row echelon form has a basis of real vectors. The dimension is $n-\operatorname{rk}(A-\lambda\mathrm{I})^{m}$, which is the multiplicity by the rank formula for the generalised eigenspace.

**Proposition.** Let $\mu=a+bi$ with $b\ne0$, and put $W=V_\mu\oplus V_{\bar\mu}$. Then $W$ is stable under conjugation, $W=W_0\otimes_{\mathbb{R}}\mathbb{C}$ for the real space $W_0=W\cap\mathbb{R}^{n}$, and $\dim_{\mathbb{R}}W_0=2\dim_{\mathbb{C}}V_\mu$.

*Proof.* The conjugate of $V_\mu$ is $V_{\bar\mu}$, so $W$ is stable under conjugation. A conjugation-stable subspace of $\mathbb{C}^{n}$ is the complexification of its real part: if $w=u+iv\in W$ then $\bar w=u-iv\in W$, hence $u,v\in W_0$ and $\mathbb{C}W_0=W$. The real dimension is twice the complex dimension because a conjugation-stable space has a basis of real vectors together with their imaginary parts, and $\dim_{\mathbb{R}}W=2\dim_{\mathbb{C}}W$.

**The restriction of $A$ to $W_0$ is a rotation block.** In a suitable real basis of $W_0$ the matrix of $A|_{W_0}$ is

$$
R_d(a,b)=\begin{pmatrix}C&\mathrm{I}_2&&\\&\ddots&\ddots&\\&&\ddots&\mathrm{I}_2\\&&&C\end{pmatrix},\qquad C=\begin{pmatrix}a&-b\\ b&a\end{pmatrix},
$$

with $d=\dim_{\mathbb{C}}V_\mu$. The construction of this basis is the content of *The Real Jordan Form and the Rotation Blocks*.

**The space $\mathbb{R}^{n}$ is the direct sum of the real generalised eigenspaces.** Summing over the real eigenvalues and over the pairs,

$$
\mathbb{R}^{n}=\bigoplus_{\lambda\in\sigma(A)\cap\mathbb{R}}V_\lambda\ \oplus\ \bigoplus_{\{\mu,\bar\mu\}}W_0,
$$

and each summand is preserved by $A$. The dimension count reads $n=\sum m_\lambda+\sum 2d_\mu$, which is $r+2s=n$ written additively.

**The characteristic polynomial is the product of the two kinds of factors.** With $\mu=a+bi$,

$$
(t-\mu)(t-\bar\mu)=(t-a)^2+b^2,
$$

so

$$
\chi_A(t)=\prod_{\lambda\in\sigma(A)\cap\mathbb{R}}(t-\lambda)^{m_\lambda}\prod_{\{\mu,\bar\mu\}}\bigl((t-a)^2+b^2\bigr)^{d_\mu}.
$$

## The Trace and the Determinant in Terms of $r$ and $s$

**Proposition.** With $r$ real eigenvalues $\lambda_1,\dots,\lambda_r$ and $s$ pairs $\mu_j=a_j+b_ji$,

$$
\operatorname{tr}A=\sum_{k=1}^{r}\lambda_k+2\sum_{j=1}^{s}\operatorname{Re}\mu_j,\qquad
\det A=\prod_{k=1}^{r}\lambda_k\ \prod_{j=1}^{s}|\mu_j|^{2}.
$$

*Proof.* Expand the factorisation of $\chi_A$. The coefficient of $t^{n-1}$ is minus the sum of the roots, and each quadratic factor contributes $2a_j$ to that sum, because $(t-a)^2+b^2=t^2-2at+(a^2+b^2)$. The constant term is $(-1)^{n}$ times the product of the roots, and each quadratic contributes $a^2+b^2=|\mu_j|^{2}$ to that product.

**Each pair contributes a positive factor to the determinant.** Since $b_j\ne0$, one has $|\mu_j|^{2}=a_j^{2}+b_j^{2}>0$. Hence

$$
\operatorname{sgn}\det A=\operatorname{sgn}\prod_{k=1}^{r}\lambda_k ,
$$

and a matrix with no real eigenvalue has $\det A>0$. The pairs never change the sign of the determinant, and only the real eigenvalues do.

**Corollary.** A matrix with $r=0$ is invertible, and its determinant is the product of the squared moduli of one member of each pair. At $n=2$ this reads $\det A=a^{2}+b^{2}$ for $A=R_1(a,b)$.

## The Elementary Symmetric Functions

**Every $e_k$ is real although the roots are not.** In the reading by minors, $e_k$ is a sum of principal minors and hence a real polynomial in the entries. In the spectral reading, $e_k$ is the sum of all products of $k$ distinct roots, and conjugation permutes the terms of that sum; a sum invariant under conjugation is real.

**Example at $n=2$ with a pair.** For the eigenvalues $a\pm bi$,

$$
e_1=2a,\qquad e_2=a^{2}+b^{2},
$$

so $\chi_A(t)=t^{2}-2at+(a^{2}+b^{2})=(t-a)^{2}+b^{2}$.

**Example at $n=3$ with one real eigenvalue and one pair.** For the eigenvalues $\lambda$ and $a\pm bi$,

$$
e_1=\lambda+2a,\qquad e_2=2a\lambda+(a^{2}+b^{2}),\qquad e_3=\lambda(a^{2}+b^{2}),
$$

so the pair enters through $a$ and $a^{2}+b^{2}$ only.

**The computation confirms it.** For a random real $6\times6$ matrix the coefficients of $\chi_A$, computed from the eigenvalues, have zero imaginary part. *The Elementary Symmetric Functions and the Real Characteristic Polynomial* develops the minors and Newton's identities.

## Two Extremes: Symmetric and Antisymmetric

**A symmetric matrix has $r=n$ and $s=0$.** Its spectrum is real, so every eigenvalue is a fixed point of the conjugation. The proof is the spectral theorem; *The Spectral Theorem: the Symmetric Case* gives two proofs and the orthonormal eigenbasis.

**An antisymmetric matrix has $r=0$, apart from the zero eigenvalues.** Its spectrum is purely imaginary, so the nonzero eigenvalues form pairs $\pm bi$ and the real eigenvalues are all zero. If $n$ is odd then $0$ is an eigenvalue, with multiplicity at least one, and the multiplicity is the corank. *The Spectral Theorem: the Antisymmetric Case and the Purely Imaginary Spectrum* proves the statement and computes the Pfaffian.

**The measurement on random matrices.** On $100$ random symmetric matrices of size $4$ the largest modulus of an imaginary part of an eigenvalue is $0$; on $100$ random antisymmetric matrices of size $4$ the largest modulus of a real part is $4.4\times10^{-16}$, which is zero up to rounding.

**The rotation $J$ at $n=2$ has an empty real spectrum.** For

$$
J=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix},\qquad \chi_J(t)=t^{2}+1,\qquad \sigma(J)=\{i,-i\},
$$

one has $r=0$ and $s=1$. Every $2\times2$ real matrix with no real eigenvalue is $a\mathrm{I}+bJ$ for some $b\ne0$, up to conjugation, that is, it is $R_1(a,b)$. So the rotation is the model of the elliptic case at $n=2$.

## The Spectral Radius

**Definition.** The spectral radius of $A$ is

$$
\rho(A)=\max_{\mu\in\sigma(A)}|\mu| .
$$

**The maximum is attained.** The spectrum is finite and $|\cdot|$ is a function on it, so the maximum is attained. This is where the real spectrum differs from the spectrum of an operator on an infinite-dimensional space, where the supremum need not be attained.

**Proposition.** $\rho(A)\le\|A\|$ for every operator norm on $\mathbb{R}^{n}$.

*Proof.* Let $\mu$ be an eigenvalue with eigenvector $z$ over $\mathbb{C}$. The norm extends to the complexification with the same bound, so $\|Az\|=|\mu|\,\|z\|$ gives $|\mu|\le\|A\|$. Take the maximum over the spectrum.

**The bound is attained for a normal matrix and it is strict in general.** For normal $A$ one has $\rho(A)=\|A\|_2$, because the eigenvectors are orthonormal. On $100$ random matrices of size $3$ the inequality $\rho(A)\le\|A\|_2$ holds every time. For the non-normal matrix with entries $1,1,0,2$ the values are $\rho=2$ and $\|A\|_2=2.288$, so the inequality is strict. *Normal Matrices over $\mathbb{R}$ and the Orthogonal Spectral Theorem* proves the equality.

**Proposition (Gelfand).** $\rho(A)=\lim_{k\to\infty}\|A^{k}\|^{1/k}$, and $\rho(A)<1$ exactly when $A^{k}\to0$.

*Proof.* On a Jordan block of size $d$ for the eigenvalue $\mu$ the power $A^{k}$ has entries $\binom{k}{j}\mu^{k-j}$ with $j<d$, so $\|A^{k}\|^{1/k}\to|\mu|$; the maximum over the blocks gives $\rho$. A sequence with $\|A^{k}\|\to0$ has $\rho<1$, and conversely.

## Summary

The spectrum of a real matrix is stable under conjugation, so it consists of $r$ real eigenvalues and $s$ conjugate pairs with $r+2s=n$. A real eigenvalue has a real generalised eigenspace, and a pair $\mu=a\pm bi$ has a conjugation-stable sum whose real part has dimension $2d$ and carries a rotation block. The trace is the sum of the real eigenvalues plus twice the sum of the real parts of the pairs; the determinant is the product of the real eigenvalues times the product of the squared moduli of the pairs, so each pair contributes positively and $\det A>0$ when $r=0$. Every elementary symmetric function is real. The rotation $J$ has empty real spectrum, symmetric matrices have real spectrum and antisymmetric ones purely imaginary spectrum. The spectral radius is attained, it is bounded by every operator norm, and it equals the Euclidean norm for normal matrices.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma(A)$ | the spectrum, the multiset of roots of $\chi_A$ in $\mathbb{C}$ |
| $\chi_A$ | the characteristic polynomial $\det(t\mathrm{I}-A)$ |
| $r$ | the number of real eigenvalues, counted with multiplicity |
| $s$ | the number of conjugate pairs |
| $V_\mu$ | the generalised eigenspace of $\mu$ |
| $W_0$ | the real part of $V_\mu\oplus V_{\bar\mu}$, of dimension $2d$ |
| $R_d(a,b)$ | the rotation block built from $C$ and $\mathrm{I}_2$ |
| $e_k$ | the $k$-th elementary symmetric function, a sum of principal minors |
| $\rho(A)$ | the spectral radius, $\max|\mu|$ over the spectrum |
| $J$ | the rotation $\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the spectrum of a real matrix and its conjugate symmetry.
- F. R. Gantmacher, *The Theory of Matrices* (Chelsea, 1959), for the real Jordan form and the reality of the generalised eigenspaces.
- [The Element: Rank, Trace, Determinant, Characteristic Polynomial over $\mathbb{R}$](the-element-rank-trace-determinant-characteristic-polynomial-over-r.html), for the characteristic polynomial and its coefficients.
- [The Elementary Symmetric Functions and the Real Characteristic Polynomial](the-elementary-symmetric-functions-and-the-real-characteristic-polynomial.html), for the reality of the coefficients.
- [The Real Jordan Form and the Rotation Blocks](the-real-jordan-form-and-the-rotation-blocks.html), for the block attached to a pair.
- [The Spectral Theorem: the Symmetric Case](the-spectral-theorem-the-symmetric-case.html), for the case $s=0$.
