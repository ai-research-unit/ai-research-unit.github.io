# __The Spectrum of a Matrix__

## Introduction

**The spectrum of $A\in M_n(\mathbb{C})$ is the set of the $n$ roots of the characteristic polynomial $\chi_A(t)=\det(t\mathrm{I}-A)$, counted with multiplicity, and it is the object that survives similarity, transposition, conjugation and the passage to polynomials, while it is destroyed by nothing else.**

The article defines the spectrum through the characteristic polynomial, proves that it has $n$ complex roots counted with multiplicity, computes the two spectral invariants $\operatorname{tr}A$ and $\det A$, proves the invariance under similarity and the two symmetries under transposition and conjugation, proves that the spectrum of a triangular matrix is its diagonal, and bounds the spectrum by the operator norm. It assumes *The Element: Rank, Trace, Determinant, Characteristic Polynomial* for the characteristic polynomial and *The Elementary Symmetric Functions and $\det(\mathrm{I}+tA)$* for its coefficients. It defers the reality of the spectrum of the Hermitian matrices to the spectral theorems and the common structure to *Normal Matrices and the Common Spectral Theorem*.

## The Characteristic Polynomial and Its Roots

**The spectrum is the zero set of the characteristic polynomial.** Put

$$
\chi_A(t)=\det(t\mathrm{I}-A).
$$

Then $\lambda\in\operatorname{Spec}(A)$ exactly when $t\mathrm{I}-A$ is singular at $t=\lambda$, exactly when $\chi_A(\lambda)=0$. The polynomial has degree $n$ and leading coefficient $1$, so it is

$$
\chi_A(t)=t^{n}-(\operatorname{tr}A)t^{n-1}+e_2(A)t^{n-2}-\cdots+(-1)^{n}\det A,
$$

where $e_k$ is the $k$-th elementary symmetric function of the eigenvalues, and the two end coefficients are the trace and the determinant by *The Elementary Symmetric Functions and $\det(\mathrm{I}+tA)$*.

**The spectrum has $n$ complex roots counted with multiplicity.** By the fundamental theorem of algebra $\chi_A$ factors as

$$
\chi_A(t)=\prod_{i=1}^{n}(t-\lambda_i),
$$

so the spectrum is a multiset of $n$ complex numbers, and two matrices are counted as having the same spectrum exactly when their characteristic polynomials agree. The multiset structure matters: two matrices with the same set of roots but different multiplicities have different spectra.

**The two coefficients at the ends give the trace and the determinant.** Comparing the two forms of $\chi_A$ at $t=0$ gives $\chi_A(0)=(-1)^{n}\det A$ and at $t^{n-1}$ gives the trace, hence

$$
\operatorname{tr}A=\sum_{i=1}^{n}\lambda_i,\qquad \det A=\prod_{i=1}^{n}\lambda_i ,
$$

which was verified at $n=3,4$ on random complex matrices. So the trace is the additive spectral invariant and the determinant the multiplicative one, and both are computed from the spectrum without knowing the eigenvectors.

**A matrix is invertible exactly when zero is not in its spectrum.** Since $\det A=(-1)^{n}\chi_A(0)$, invertibility is the statement $\chi_A(0)\neq0$, and the inverse is a rational function of $A$ whose poles are the spectrum. So the spectrum is the exact obstruction to invertibility, and the set of matrices with a given spectrum is the set on which a fixed polynomial vanishes.

## Multiplicity

**Each root has an algebraic multiplicity, and the multiplicities sum to $n$.** Writing $\chi_A(t)=\prod_i(t-\lambda_i)^{m_i}$ with distinct $\lambda_i$, the integer $m_i$ is the algebraic multiplicity and

$$
\sum_{i}m_i=n .
$$

A root that occurs once is simple, and a matrix whose characteristic polynomial has $n$ distinct roots is called generic in this respect; the set of matrices with a repeated root is the zero set of the discriminant, a hypersurface.

**The geometric multiplicity is at most the algebraic one.** The eigenspace $E_\lambda=\ker(\lambda\mathrm{I}-A)$ has dimension $\gamma_\lambda$ equal to the number of Jordan blocks of $\lambda$, and

$$
1\le\gamma_\lambda\le m_\lambda .
$$

The equality $\gamma_\lambda=m_\lambda$ for every $\lambda$ is exactly diagonalisability, so the spectrum alone does not decide diagonalisability; the Jordan form of *The Minimal Polynomial and the Jordan Form* does.

**The failure of equality is measured by the nilpotent part.** If $\gamma_\lambda<m_\lambda$ then $A-\lambda\mathrm{I}$ has a nilpotent Jordan block at $\lambda$, of size at least two, and the matrix is not diagonalisable. So the spectrum is the first invariant and the multiplicities are the second, and the two together do not yet determine the similarity class.

**The roots are continuous.** The coefficients of $\chi_A$ depend continuously on $A$, and the roots of a polynomial depend continuously on its coefficients, so the spectrum is a continuous multivalued function of the matrix. A double root can split under a small perturbation, which is why the multiplicities are the fragile part and the set of roots the stable part.

## Invariance under Similarity and the Two Symmetries

**The spectrum is invariant under similarity.** For invertible $P$,

$$
\chi_{PAP^{-1}}(t)=\det(P(t\mathrm{I}-A)P^{-1})=\det(t\mathrm{I}-A)=\chi_A(t),
$$

so similar matrices have equal spectra. The computation at $n=4$ confirms it on a random pair, and the invariance is the reason the spectrum is a property of the linear map rather than of the matrix.

**The transpose has the same spectrum.** Since $\det(t\mathrm{I}-A^{\mathsf T})=\det(t\mathrm{I}-A)$,

$$
\operatorname{Spec}(A^{\mathsf T})=\operatorname{Spec}(A),
$$

which is the spectral form of the statement that a matrix and its transpose have the same eigenvalues. So the two halves of the algebra have the same spectrum after transposition, and the involution does not move the spectrum as a set.

**Conjugation reflects the spectrum in the real axis.** Since $\chi_{A^{*}}(t)=\overline{\chi_A(\bar t)}$,

$$
\operatorname{Spec}(A^{*})=\overline{\operatorname{Spec}(A)}=\{\bar\lambda:\lambda\in\operatorname{Spec}(A)\},
$$

which was verified at $n=3,4$. So a Hermitian matrix has a conjugation-invariant spectrum, which forces it onto the real axis, and that is the first step of the Hermitian spectral theorem.

**Products have the same spectrum in either order.** For square matrices $A,B$,

$$
\operatorname{Spec}(AB)=\operatorname{Spec}(BA),
$$

which was verified at $n=3,4$ on random pairs. The reason is that $AB$ and $BA$ are similar when $A$ is invertible, $BA=A^{-1}(AB)A$, and the identity extends to the singular case by continuity. So the spectrum of a product is insensitive to the order, which is the spectral shadow of the cyclicity of the trace.

## The Spectrum of a Triangular Matrix

**The determinant of a triangular matrix is the product of its diagonal, so the spectrum is the diagonal.** For upper triangular $U$,

$$
\chi_U(t)=\prod_{i=1}^{n}(t-U_{ii}),
$$

since $t\mathrm{I}-U$ is upper triangular and its determinant is the product of its diagonal. Hence

$$
\operatorname{Spec}(U)=\{U_{11},\dots,U_{nn}\},
$$

with the multiplicity of each value equal to the number of times it occurs on the diagonal, which the computation confirms at $n=4,5$.

**So the triangular algebra carries its spectrum on its diagonal, and the strictly upper part does not move it.** The algebra $n_+$ consists of the matrices with zero spectrum, and the map $U\mapsto\operatorname{Spec}(U)$ factors through the quotient $UT_n/n_+$, which is the diagonal. So the spectrum of the triangular algebra is the projection onto the abelianisation, and the nilpotent radical is exactly the set of elements of zero spectrum.

**The companion matrix shows that every polynomial is a characteristic polynomial.** For any monic $p$ of degree $n$ there is a matrix $C_p$ with $\chi_{C_p}=p$, namely the companion matrix of the polynomial. So the map from matrices to monic polynomials of degree $n$ is surjective, and every spectrum occurs: the space of spectra is the space of unordered $n$-tuples of complex numbers.

**The eigenvalue condition is one equation per eigenvalue.** For a fixed $\lambda$ the condition $\lambda\in\operatorname{Spec}(A)$ is the single scalar equation $\det(\lambda\mathrm{I}-A)=0$, so the set of matrices having $\lambda$ as an eigenvalue is a hypersurface. The spectrum as a whole is therefore the common zero set of $n$ such equations, which is why the generic matrix has $n$ distinct eigenvalues and the exceptional ones lie on a discriminant hypersurface.

## The Spectral Radius and Its Bounds

**The spectral radius is bounded by every operator norm.** Put $\rho(A)=\max_i|\lambda_i|$. If $A v=\lambda v$ with $\|v\|=1$, then

$$
|\lambda|=\|Av\|\le\|A\|\,\|v\|=\|A\|,
$$

so $\rho(A)\le\|A\|$ for the operator norm, and by the equivalence of the norms also $\rho(A)\le\|A\|_{HS}$, which was verified at $n=3,4$. The bound is not an equality in general: a nilpotent has $\rho=0$ and positive norm.

**The spectral radius governs the powers.** For every $\varepsilon>0$ there is a norm with $\|A\|\le\rho(A)+\varepsilon$, so

$$
\rho(A)=\lim_{k\to\infty}\|A^{k}\|^{1/k},
$$

and $A^{k}\to0$ exactly when $\rho(A)<1$. So the spectrum decides the asymptotic behaviour of the powers, and the norm decides only the size at each step.

**The spectrum of a polynomial is the polynomial of the spectrum.** For every polynomial $p$,

$$
\operatorname{Spec}(p(A))=p\big(\operatorname{Spec}(A)\big)=\{p(\lambda):\lambda\in\operatorname{Spec}(A)\},
$$

which was verified at $n=4$ for $p(t)=t^{2}+3t-1$. The reason is the factorisation $p(t)-p(\lambda)=(t-\lambda)q(t)$, which shows that $p(A)-p(\lambda)\mathrm{I}$ is singular exactly when $A-\lambda\mathrm{I}$ is. So the spectral calculus is multiplicative, and it is the first instance of the functional calculus of *The Analysis on $M_n(\mathbb{C})$*.

**The spectrum of a block triangular matrix is the union of the spectra of the diagonal blocks.** If $M=\begin{pmatrix}A&B\\0&D\end{pmatrix}$ then $\chi_M=\chi_A\chi_D$, so

$$
\operatorname{Spec}(M)=\operatorname{Spec}(A)\cup\operatorname{Spec}(D),
$$

which the computation confirms at $n=4$. So the spectra add under the triangular decomposition, and the strictly block-upper part $B$ does not affect the spectrum at all.

## The Case $n=2$

**At $n=2$ the spectrum is given by the quadratic formula.** For $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$,

$$
\chi_A(t)=t^{2}-(a+d)t+(ad-bc),
$$

so the spectrum is

$$
\operatorname{Spec}(A)=\Big\{\frac{\operatorname{tr}A\pm\sqrt{(\operatorname{tr}A)^{2}-4\det A}}{2}\Big\},
$$

and the discriminant $(\operatorname{tr}A)^{2}-4\det A$ decides whether the spectrum is real, double or conjugate. The formula was verified on random complex matrices.

**The two halves have the two extreme spectral behaviours.** For $S$ symmetric the discriminant is a sum of squares and the spectrum is real; for $K$ antisymmetric, $\operatorname{tr}K=0$ and $\det K\ge0$, so the spectrum is $\{\pm i\sqrt{\det K}\}$, purely imaginary. So

$$
\operatorname{Spec}(S)\subset\mathbb{R},\qquad \operatorname{Spec}(K)\subset i\mathbb{R},
$$

which was verified on random elements of the two halves and is the $n=2$ case of the two spectral theorems.

**The biquaternion reading gives the spectrum two coordinates.** The four coordinates $e_t,\tilde{Ζ}$ and the two mixed directions give the trace and the determinant, so $\operatorname{Spec}$ of a biquaternion is the pair of roots of $t^{2}-(\text{scalar part})t+(\text{norm})$, and the norm $N$ is the determinant. So the indefinite norm of signature $(2,2)$ is the product of the two spectral values, and the spectrum of an idempotent is $\{1,0\}$ while that of a companion nilpotent is $\{0,0\}$.

## Summary

The spectrum of $A$ is the multiset of the $n$ roots of $\chi_A(t)=\det(t\mathrm{I}-A)$, with multiplicities summing to $n$; its sum is the trace and its product the determinant. It is invariant under similarity, under transposition, and under conjugation up to complex conjugation, and it satisfies $\operatorname{Spec}(AB)=\operatorname{Spec}(BA)$ and $\operatorname{Spec}(p(A))=p(\operatorname{Spec}A)$. The spectrum of a triangular matrix is its diagonal, so the triangular algebra carries its spectrum on the diagonal and the nilpotent radical is the zero-spectrum set. The spectral radius is bounded by every operator norm, governs the powers and the functional calculus, and at $n=2$ is given by the quadratic formula, real on the symmetric half and purely imaginary on the antisymmetric half.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\chi_A(t)=\det(t\mathrm{I}-A)$ | the characteristic polynomial |
| $\operatorname{Spec}(A)$ | the multiset of its roots |
| $m_\lambda$, $\gamma_\lambda$ | the algebraic and the geometric multiplicity |
| $\operatorname{tr}A=\sum\lambda_i$, $\det A=\prod\lambda_i$ | the two spectral invariants |
| $\operatorname{Spec}(A^{*})=\overline{\operatorname{Spec}(A)}$ | the reflection under conjugation |
| $\rho(A)=\max|\lambda_i|$ | the spectral radius |
| $\operatorname{Spec}(p(A))=p(\operatorname{Spec}A)$ | the spectral mapping for polynomials |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the characteristic polynomial, the multiplicities and the spectral radius.
- Peter D. Lax, *Linear Algebra and Its Applications* (Wiley, 2007), for the spectral mapping theorem and the continuity of the roots.
- F. R. Gantmacher, *The Theory of Matrices* (AMS Chelsea, 1959), for the companion matrix and the elementary symmetric functions of the spectrum.
- [The Element: Rank, Trace, Determinant, Characteristic Polynomial](the-element-rank-trace-determinant-characteristic-polynomial.html), for the characteristic polynomial and its coefficients.
- [The Elementary Symmetric Functions and $\det(\mathrm{I}+tA)$](the-elementary-symmetric-functions-and-det-i-plus-ta.html), for the coefficients as symmetric functions of the eigenvalues.
- [The Minimal Polynomial and the Jordan Form](the-minimal-polynomial-and-the-jordan-form.html), for the multiplicities and the diagonalisability criterion.
