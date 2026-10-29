# __Relations between the Split Norm and Spectral Regularity and Degeneracy__

## Introduction

An element $q=t+bj$ carries two quadratic conditions. The **split norm** $q\bar q=t^2-b^2$ is the determinant of left multiplication and the product of the eigenvalues; it vanishes exactly on the non-units. The **spectral condition** $b^2$ is a quarter of the discriminant and the square of half the eigenvalue difference; it vanishes exactly when the eigenvalues coincide. This article compares them, proves that neither implies the other, and reads the four combinations as four sectors. The mixed sectors are the point: a zero divisor with distinct eigenvalues, and a unit with a repeated one.

**Notation.** An element is $q=t+bj$, its conjugate is $\bar q=t-bj$, and the idempotents are $e_\pm=\tfrac12(1\pm j)$. The idempotent coordinates are $u=t+b$ and $v=t-b$, so that $q=ue_+ +ve_-$, the eigenvalues are $\lambda_+=u$ and $\lambda_-=v$, the split norm is $q\bar q=uv$, and $b=(u-v)/2$. The split norm is indefinite and is not a length. The corpus writes the same element $Q=q+jq'$, with its $q,q'$ equal to $t,b$ here and its $\Pi_\pm$ equal to the $e_\pm$.

## The Two Conditions in One Quadratic

**Definition (the two conditions).** The **split norm** of $q$ is $q\bar q=t^2-b^2$; the element is **norm-regular** when the norm is non-zero and **norm-degenerate** when it is zero. The **spectral condition** is $b^2$; the element is **spectrally regular** when $b\neq0$ and **spectrally degenerate** when $b=0$.

**Theorem (one polynomial carries both).** For every $q$,

$$
p_q(X)=X^2-2tX+q\bar q=(X-\lambda_+)(X-\lambda_-),
\qquad \lambda_\pm=t\pm b.
$$

The split norm is the constant term and the product of the eigenvalues; the spectral condition is a quarter of the discriminant and the square of half their difference:

$$
q\bar q=\lambda_+\lambda_-,\qquad
b^2=\frac{(\lambda_+-\lambda_-)^2}{4},\qquad
\operatorname{disc}p_q=4b^2.
$$

*Proof.* The characteristic polynomial of $L_q$ is $X^2-2tX+t^2-b^2$, and its roots are $t\pm b$. The product and the difference of the roots give the displayed identities.

**Corollary.** The split norm vanishes exactly when one eigenvalue is zero; the spectral condition vanishes exactly when the eigenvalues coincide.

*Proof.* The product is $q\bar q$, and the difference is $\lambda_+-\lambda_-=2b$.

**Proposition (multiplicativity).** For $q_1,q_2\in\mathbb{D}$, $(q_1q_2)\overline{(q_1q_2)}=(q_1\bar q_1)(q_2\bar q_2)$.

*Proof.* The conjugation is an automorphism and the algebra is commutative: $(q_1q_2)\overline{(q_1q_2)}=q_1q_2\bar q_2\bar q_1=q_1\bar q_1q_2\bar q_2$.

**Proposition (the spectral condition is not multiplicative).** The elements $q_1=2+j$ and $q_2=-2+j$ have $b^2=1$, and $q_1q_2=-3$ has $b^2=0$.

*Proof.* Direct computation: $(2+j)(-2+j)=-4+2j-2j+1=-3$.

**Corollary (the unit criterion).** For $q\neq0$, $q$ is a unit exactly when $q\bar q\neq0$; then $q^{-1}=\bar q/(q\bar q)$. If the norm vanishes, $q$ is a zero divisor.

*Proof.* The product $q\bar q$ is real and equals $\bar q q$, so the formula gives an inverse when the denominator is non-zero. When it vanishes and $q\neq0$, the element is a non-unit in a finite-dimensional algebra, hence a zero divisor.

## Independence of the Two Conditions

**Theorem (independence).** The two conditions are **independent**: neither implication $q\bar q=0\Rightarrow b=0$ and $b=0\Rightarrow q\bar q=0$ holds, and all four combinations occur.

*Proof.* Two witnesses.

- $q_1=1+j$ has $q_1\bar q_1=0$ and $b=1$; its spectrum is $\{2,0\}$.
- $q_2=2$ has $q_2\bar q_2=4$ and $b=0$; its spectrum is $\{2\}$.

The first is norm-degenerate and spectrally regular; the second is norm-regular and spectrally degenerate. The other combinations occur at $2+j$, with norm $3$ and $b=1$, and at $0$.

**Corollary (the zero loci meet only at the origin).** If $q\bar q=0$ and $b=0$, then $t=0$ and $q=0$.

*Proof.* The second condition gives $b=0$; the first then gives $t^2=0$.

**Corollary (four non-empty sectors).** The four sets

$$
\Sigma_{11}=\{q\bar q\neq0,\ b\neq0\},\quad
\Sigma_{01}=\{q\bar q=0,\ b\neq0\},\quad
\Sigma_{10}=\{q\bar q\neq0,\ b=0\},\quad
\Sigma_{00}=\{q\bar q=0,\ b=0\}
$$

are all non-empty, and $\mathbb{D}$ is their disjoint union.

*Proof.* The witnesses lie in the first three, and $0$ lies in the fourth. Each element has one truth value for each condition, so it lies in one combination. The first index is the split norm, $1$ for non-vanishing and $0$ for vanishing; the second is the spectral condition, with the same convention.

## The Null Lines

**The null lines are $t=\pm b$; away from the origin their elements are zero divisors with distinct eigenvalues.**

**Theorem (the null lines).** For $q\neq0$, the following are equivalent:

1. $q\bar q=0$;
2. $b=\pm t$;
3. $q=2t e_+$ or $q=2t e_-$ with $t\neq0$;
4. $\sigma(q)=\{2t,0\}$;
5. $q$ is a zero divisor;
6. $q$ is spectrally regular.

Each admits the two-term spectral decomposition $q=2t\,e_\pm +0\cdot e_\mp$.

*Proof.* (1)$\iff$(2): $t^2-b^2=(t-b)(t+b)$, and $q\neq0$ excludes $t=b=0$. (2)$\iff$(3): if $b=t$, then $q=t(1+j)=2t e_+$; if $b=-t$, then $q=t(1-j)=2t e_-$. (3)$\iff$(4): $e_\pm$ are eigenvectors with eigenvalues $2t$ and $0$, distinct because $t\neq0$. (4)$\iff$(6): the spectrum has two elements exactly when $b\neq0$. (3)$\iff$(5): if $q=2t e_+$ then $qe_-=0$ with $e_-\neq0$, and symmetrically; conversely a zero divisor is a non-unit, so $q\bar q=0$ by the unit criterion.

**Corollary (the annihilators).** On the null cone,

$$
\operatorname{ann}(2t e_+)=\mathbb{R}e_-,\qquad
\operatorname{ann}(2t e_-)=\mathbb{R}e_+,\qquad t\neq0.
$$

*Proof.* For $q=2t e_+$ and $w=w_+e_++w_-e_-$, the product is $2t w_+e_+$, which vanishes exactly when $w_+=0$.

**Corollary (the zero-divisor set).** The zero-divisor set is exactly $\Sigma_{01}$, the two null lines with the origin removed. It has real dimension one and four connected components, the rays determined by the sign of $t$; its closure is $\mathcal{N}=\{q\bar q=0\}$.

*Proof.* The theorem identifies the zero divisors with the non-zero null elements. Each punctured line has the rays $t>0$ and $t<0$.

## The Real Axis Minus the Origin

**The real axis minus the origin is the sector of units with a repeated eigenvalue: the norm is positive and the spectrum is a singleton.**

**Theorem (the real axis).** For $q=t$ with $t\neq0$, one has $q\bar q=t^2>0$, $q^{-1}=1/t$, $\sigma(q)=\{t\}$, and minimal polynomial $X-t$. The element is norm-regular and spectrally degenerate, with the one-term spectral decomposition $q=t\cdot1$.

*Proof.* The norm is $t^2$, and $1/t$ is the inverse. The characteristic polynomial is $(X-t)^2$, whose only root is $t$; the minimal polynomial is $X-t$ because $q-t=0$.

**Corollary.** The sector $\Sigma_{10}$ is exactly $\mathbb{R}^{\times}$, with the two components $\mathbb{R}_{>0}$ and $\mathbb{R}_{<0}$.

*Proof.* The conditions are $b=0$ and $t^2-b^2=t^2\neq0$, that is $t\neq0$.

The sign of the norm does not isolate this sector: $\Sigma_{11}$ also contains elements with positive norm. What isolates it is $b=0$.

## The Origin

**The origin is the unique element degenerate for both conditions, and the two degenerations coincide there.**

**Theorem (the doubly degenerate element).** The element $q=0$ is the only one with $q\bar q=0$ and $b=0$. Its spectrum is $\{0\}$, its minimal polynomial is $X$, and it is not a zero divisor.

*Proof.* The conditions give $t^2=b^2$ and $b=0$, hence $t=0$. The spectrum of $0$ is $\{0\}$ and its minimal polynomial is $X$. The definition of a zero divisor excludes $0$.

The origin is $\mathcal{N}\cap\mathcal{S}$, the intersection of the null cone and the spectral-degenerate line. It is doubly degenerate but not a zero divisor.

## The Chain of Invariants

**The norm is the constant term of the characteristic polynomial, and the chain stops at the characteristic polynomial.**

| invariant | data | degeneration types |
|---|---|---|
| split norm | $q\bar q=t^2-b^2$ | $2$: zero and non-zero |
| spectral condition | $b^2$ | $2$: zero and non-zero |
| characteristic polynomial | $(2t,q\bar q)$ | $4$: the root patterns |
| minimal polynomial | $m_q$ | $4$: no new stratum |

**Theorem (the chain).** The split norm is the constant term of $p_q$. The characteristic polynomial determines $t$ and $b^2=t^2-q\bar q$, hence the sector and the unordered pair of eigenvalues. The minimal polynomial determines the characteristic polynomial by

$$
p_q=
\begin{cases}
m_q, & \deg m_q=2,\\
m_q^2, & \deg m_q=1.
\end{cases}
$$

Consequently the minimal polynomial separates exactly the four sectors and adds no stratum.

*Proof.* The coefficients $2t$ and $q\bar q$ give $t$ and $b^2=t^2-q\bar q$; the eigenvalues $t\pm b$ follow up to order. If $b\neq0$, the minimal polynomial is $p_q$; if $b=0$, it is $X-t$ and its square is $p_q$. The four root patterns are two distinct non-zero roots, two distinct roots with one zero, a double non-zero root, and a double root at zero; they are the four sectors.

In the biquaternion algebra, as *[The Spectrum](the-spectrum.html)* proves, the minimal polynomial refines the degenerate cone into a scalar, a nilpotent and a unipotent stratum, and the last two are defective. In $\mathbb{D}$ no refinement exists, because the algebra is reduced and every element is semisimple.

## The Place of the Case Among the Algebras of the Corpus

**The plane is the only algebra of the table in which the conditions are independent and neither creates a defect.**

| algebra | norm | spectral-degenerate locus | defective elements | $\Sigma_{01}$ non-empty |
|---|---|---|---|---|
| $\mathbb{C}$ | $t^2+b^2$, positive definite | real axis | none | no |
| $\mathbb{D}$ | $t^2-b^2$, indefinite | real axis | none | yes |
| $\mathbb{H}$ | $t^2+\lVert\vec v\rVert^2$, positive definite | real axis | none | no |
| $\mathbb{H}_{\mathrm{s}}$ | indefinite | the cone $\langle\vec v\rangle_{\natural}=0$ | non-zero null vector part | yes |
| $\mathbb{B}$ | $Q_t^2+B^2$, complex-valued | the cone $B^2=0$ | nilpotent and unipotent strata | yes |

In $\mathbb{C}$ and $\mathbb{H}$ the norm is positive definite and vanishes only at the origin; $\Sigma_{01}$ is empty and the picture has three non-empty cells, with $\Sigma_{00}=\{0\}$. In $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$ the mixed sectors are non-empty, but the degenerate locus is a cone carrying defective elements. In $\mathbb{D}$ the norm is indefinite, the conditions are independent, the degenerate locus is a line, and every element is semisimple. The plane is therefore the unique algebra with four non-empty sectors and no defective stratum; the geometry of the sectors is *The Four Sectors of the Split-Complex Algebra*.

The sign of $j^2$ separates the definite norm and complex spectrum of $\mathbb{C}$ from the indefinite norm and real spectrum of $\mathbb{D}$.

## Summary

The split norm $q\bar q=t^2-b^2$ is the determinant of $L_q$ and the product of the eigenvalues; it decides invertibility. The spectral condition $b^2$ is a quarter of the discriminant; it decides whether the spectrum is separated. Both sit in $p_q(X)=X^2-2tX+q\bar q$: the norm as constant term, $4b^2$ as discriminant.

The conditions are independent: $1+j$ has zero norm and eigenvalues $2,0$; $2$ has non-zero norm and repeated eigenvalue $2$. The null lines $t=\pm b$ are the zero divisors; the real axis minus the origin is the group of units with repeated eigenvalue $t$; the origin is the unique element degenerate for both and is not a zero divisor.

The four combinations are $\Sigma_{11}$, $\Sigma_{01}$, $\Sigma_{10}$ and $\Sigma_{00}$. The norm separates units from non-units, the spectral condition regular from degenerate spectra, and the characteristic polynomial the four sectors. The minimal polynomial adds nothing: it reproduces the same four types, unlike the biquaternion case, where it refines the degenerate cone into three strata. The plane is the unique algebra of the table with four non-empty sectors and no defective element.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{D}=\mathbb{R}[j]/(j^2-1)$ | the split-complex algebra |
| $q=t+bj$ | a general element, $t,b\in\mathbb{R}$ |
| $\bar q=t-bj$ | the conjugation |
| $q\bar q=t^2-b^2$ | the split norm |
| $u=t+b,\ v=t-b$ | the idempotent coordinates and the eigenvalues |
| $e_\pm=\tfrac12(1\pm j)$ | the two non-trivial idempotents |
| $p_q(X)=X^2-2tX+q\bar q$ | the characteristic polynomial |
| $b^2=\operatorname{disc}p_q/4$ | the spectral condition |
| $\mathcal{N}=\{q\bar q=0\}$ | the null cone, the two null lines |
| $\mathcal{S}=\{b=0\}$ | the spectral-degenerate line, the real axis |
| $\Sigma_{ij}$ | the sector with norm $i$ and spectrum $j$ |
| $m_q$ | the minimal polynomial |

## Further Reading

- [Spectral Regularity and Degeneracy in the Split-Complex Algebra](spectral-regularity-and-degeneracy-in-the-split-complex-algebra.html), for the eigenvalue problem and the criterion.
- [The Four Sectors of the Split-Complex Algebra](the-four-sectors-of-the-split-complex-algebra.html), for the geometry of the four cells.
- [Zero Divisors of the Split-Complex Algebra](zero-divisors-of-the-split-complex-algebra.html), for the null lines and the annihilators.
- [Norm and Invertibility in the General Split-Complex Algebra](norm-and-invertibility-in-the-general-split-complex-algebra.html), for the split norm.
- [Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number](eigenvalue-decomposition-and-eigenbasis-of-a-split-complex-number.html), for the spectral decomposition.
- [Eigenbasis of a Split-Complex Number in Matrix Elements Representations](eigenbasis-of-a-split-complex-number-in-matrix-elements-representations.html), for the matrix models.
- [Worked Examples of Eigenbasis of a Split-Complex Number](worked-examples-of-eigenbasis-of-a-split-complex-number.html), for computations.
