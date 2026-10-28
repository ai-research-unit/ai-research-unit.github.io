# __The Four Sectors of the Split-Complex Algebra__

## Introduction

The split-complex algebra $\mathbb{D}=\mathbb{R}[j]/(j^2-1)$ carries two quadratic conditions on $q=t+bj$: the split norm $q\bar q=t^2-b^2$, which decides invertibility, and the spectral condition $b^2$, which decides whether the eigenvalues $t\pm b$ coincide. Their vanishing loci are the two null lines $t=\pm b$ and the real axis $b=0$. The truth values of the pair cut the plane into four sectors. This article defines them, proves all four non-empty, describes their geometry, and computes their closures, dimensions and components. It proves that none is a defective stratum. The sector $\Sigma_{11}$ is the largest: because $b=0$ is removed, it has six components, not two.

**Notation.** An element is $q=t+bj$, its conjugate is $\bar q=t-bj$, and the idempotents are $e_\pm=\tfrac12(1\pm j)$. The idempotent coordinates are $u=t+b$ and $v=t-b$, so that $q=ue_+ +ve_-$ and the eigenvalues are $u$ and $v$. The split norm is $q\bar q=uv=t^2-b^2$; it is indefinite and is not a length. The two conditions were compared in *[Relations between the Split Norm and Spectral Regularity and Degeneracy](relations-between-the-split-norm-and-spectral-regularity-and-degeneracy.html)*.

## The Four Sectors

**Definition (the sectors).** For $i,j\in\{0,1\}$, $\Sigma_{ij}$ is the set on which the split norm is zero exactly when $i=0$, and the spectral condition is zero exactly when $j=0$:

$$
\Sigma_{11}=\{t^2\neq b^2,\ b\neq0\},\qquad
\Sigma_{01}=\{t^2=b^2,\ b\neq0\},
$$
$$
\Sigma_{10}=\{t^2\neq b^2,\ b=0\},\qquad
\Sigma_{00}=\{t^2=b^2,\ b=0\}.
$$

The first index is $1$ when the norm is non-zero and $0$ when it is zero; the second is $1$ when $b$ is non-zero and $0$ when it is zero.

**Proposition (the sectors cover the plane).** The sets $\Sigma_{11},\Sigma_{01},\Sigma_{10},\Sigma_{00}$ are pairwise disjoint and their union is $\mathbb{D}$.

*Proof.* Each element has exactly one truth value for each of the two conditions, so it lies in exactly one of the four combinations.

**Proposition (all four sectors are non-empty).** The following witnesses lie in the four sectors:

| sector | witness | norm | $b$ |
|---|---|---|---|
| $\Sigma_{11}$ | $2+j$ | $3$ | $1$ |
| $\Sigma_{01}$ | $1+j$ | $0$ | $1$ |
| $\Sigma_{10}$ | $2$ | $4$ | $0$ |
| $\Sigma_{00}$ | $0$ | $0$ | $0$ |

*Proof.* Direct evaluation of $t^2-b^2$ and $b$ at each witness.

## The Sector $\Sigma_{11}$

**Theorem (the shape of $\Sigma_{11}$).** The sector $\Sigma_{11}$ is the complement in $\mathbb{R}^2$ of the union of the three lines

$$
b=0,\qquad t=b,\qquad t=-b.
$$

It is open and dense, and it has exactly six connected components, the six open angular sectors cut out by the three lines.

*Proof.* The conditions defining $\Sigma_{11}$ exclude exactly the points with $b=0$ or $t^2=b^2$, that is the three lines. Their complement is open. Three distinct lines through the origin divide the plane into six open angular sectors; each is convex and therefore connected, and two different sectors are separated by a removed line. Hence there are six components.

The open quadrants of positive norm are $Q_+=\{t>|b|\}$ and $Q_-=\{t<-|b|\}$. Each is convex, but the removed real axis cuts $Q_+$ into the components $b>0$ and $b<0$, and cuts $Q_-$ similarly. The negative-norm region $|t|<|b|$ contributes the components $b>|t|$ and $b<-|t|$. Hence four components have positive norm and two have negative norm.

**Proposition (the elements of $\Sigma_{11}$).** Every element of $\Sigma_{11}$ is a unit with two distinct real eigenvalues $t+b$ and $t-b$, and spectral decomposition $q=(t+b)e_+ +(t-b)e_-$.

*Proof.* The element is not scalar because $b\neq0$, so the eigenvalues are distinct. The norm is non-zero, so the element is a unit, with inverse $\bar q/(q\bar q)$. The idempotent expansion is the spectral decomposition.

The two open quadrants $Q_+\cup Q_-$ are not the whole sector: after $b=0$ is removed each splits in two, and with the two negative-norm sectors the total is six.

## The Sector $\Sigma_{01}$

**The sector $\Sigma_{01}$ is the union of the two null lines with the origin removed: the zero divisors with distinct eigenvalues.**

**Theorem (the punctured null lines).** The sector $\Sigma_{01}$ is

$$
\{t=b,\ t\neq0\}\cup\{t=-b,\ t\neq0\}.
$$

Every element has the form $q=2t e_+$ or $q=2t e_-$ with $t\neq0$. It is a zero divisor, its spectrum is $\{2t,0\}$, and its spectral decomposition is $q=2t\,e_\pm+0\cdot e_\mp$.

*Proof.* The condition $t^2=b^2$ gives $b=\pm t$; the condition $b\neq0$ excludes the origin. If $b=t$, then $q=t(1+j)=2t e_+$; if $b=-t$, then $q=t(1-j)=2t e_-$. The annihilator of $2t e_\pm$ contains $e_\mp$, so the element is a zero divisor.

**Corollary (the components).** The sector $\Sigma_{01}$ has real dimension one and four connected components, the four rays

$$
t>0,\ b=t;\qquad t<0,\ b=t;\qquad t>0,\ b=-t;\qquad t<0,\ b=-t.
$$

*Proof.* Each punctured line has the two rays $t>0$ and $t<0$, and the two lines meet only at the origin, which is removed. Each ray is homeomorphic to an open interval.

The two lines annihilate each other: $\operatorname{ann}(2t e_+)=\mathbb{R}e_-$ and $\operatorname{ann}(2t e_-)=\mathbb{R}e_+$ for $t\neq0$. The sector is the zero-divisor set of the algebra, studied in *[Zero Divisors of the Split-Complex Algebra](zero-divisors-of-the-split-complex-algebra.html)*.

## The Sector $\Sigma_{10}$

**The sector $\Sigma_{10}$ is the real axis minus the origin: the scalar units, with a repeated eigenvalue.**

**Theorem (the real half-lines).** The sector $\Sigma_{10}$ is $\mathbb{R}^{\times}=\{t\neq0,\ b=0\}$. Every element is the scalar $q=t$, a unit with $q^{-1}=1/t$, norm $t^2>0$, spectrum $\{t\}$ and minimal polynomial $X-t$. Its spectral decomposition is the one-term writing $q=t\cdot1$.

*Proof.* The conditions are $b=0$ and $t^2-b^2=t^2\neq0$, hence $t\neq0$. The inverse is $1/t$, the characteristic polynomial is $(X-t)^2$, and the minimal polynomial is $X-t$ because $q-t=0$.

**Corollary (the components).** The sector $\Sigma_{10}$ has real dimension one and two connected components, the positive and the negative half-lines.

*Proof.* The set $\mathbb{R}^{\times}$ is the disjoint union of $\{t>0\}$ and $\{t<0\}$, each homeomorphic to an open interval.

This is the opposite divergence from $\Sigma_{01}$: units with a singleton spectrum. Invertibility and spectral separation are independent; see *[Spectral Regularity and Degeneracy in the Split-Complex Algebra](spectral-regularity-and-degeneracy-in-the-split-complex-algebra.html)*.

## The Sector $\Sigma_{00}$

**The sector $\Sigma_{00}$ is the origin: the zero element, degenerate for both conditions and not a zero divisor.**

**Theorem (the origin).** The sector $\Sigma_{00}$ is the singleton $\{0\}$. Its element has norm zero, spectrum $\{0\}$, minimal polynomial $X$, and is the only element with both eigenvalues zero. It is not a zero divisor.

*Proof.* The conditions $t^2=b^2$ and $b=0$ give $t=0$. The spectrum of $0$ is $\{0\}$ and its minimal polynomial is $X$; the definition of a zero divisor excludes $0$. Both eigenvalues vanish only if $t+b=0$ and $t-b=0$, hence $t=b=0$.

The origin lies in the closure of every sector, as the next section shows.

## Closure, Dimension and Connected Components

| sector | closure | dimension | components |
|---|---|---|---|
| $\Sigma_{11}$ | $\mathbb{D}$ | $2$ | $6$ |
| $\Sigma_{01}$ | $\mathcal{N}=\{t^2=b^2\}$ | $1$ | $4$ |
| $\Sigma_{10}$ | $\mathcal{S}=\{b=0\}$ | $1$ | $2$ |
| $\Sigma_{00}$ | $\{0\}$ | $0$ | $1$ |

**Theorem (closures).** The closures are as in the table. The sector $\Sigma_{11}$ is open and dense, $\Sigma_{00}$ is closed, and $\Sigma_{01}$ and $\Sigma_{10}$ are neither open nor closed. The origin lies in the closure of all four sectors.

*Proof.* The complement of $\Sigma_{11}$ is the union of the three lines, which has empty interior, so the closure is $\mathbb{D}$. The null cone $\mathcal{N}$ is closed and contains $\Sigma_{01}$, and the origin is a limit along either line, so the closure is $\mathcal{N}$. The real axis $\mathcal{S}$ is closed and contains $\Sigma_{10}$, and the origin is a limit of $t\neq0$, so the closure is $\mathcal{S}$. The singleton $\{0\}$ is closed.

$\Sigma_{11}$ is the complement of a closed union of lines, hence open. A ball around a point of $\Sigma_{01}$ or $\Sigma_{10}$ contains points outside the sector, so neither is open; both miss the origin, which lies in their closures, so neither is closed.

**Theorem (dimensions and components).** The dimensions and component counts are as in the table. In particular $\Sigma_{11}$ has six components, $\Sigma_{01}$ four, $\Sigma_{10}$ two and $\Sigma_{00}$ one.

*Proof.* $\Sigma_{11}$ is open in $\mathbb{R}^2$, hence of dimension two; its six components are the open angular sectors of the three-line complement. $\Sigma_{01}$ and $\Sigma_{10}$ are unions of open rays, of dimension one, with four and two components. The origin has dimension zero and one component.

The closures overlap: $\overline{\Sigma_{11}}=\mathbb{D}$ meets every sector, while $\overline{\Sigma_{01}}\cap\overline{\Sigma_{10}}=\{0\}$. The origin is the only point common to all four closures.

## The Absence of a Defective Stratum

**Definition (defective).** An element is **semisimple** if its minimal polynomial is squarefree; it is **defective** otherwise.

**Theorem (no defective element).** Every element of $\mathbb{D}$ is semisimple. Consequently no sector is a defective stratum.

*Proof.* If $b\neq0$, the minimal polynomial is $(X-t-b)(X-t+b)$, whose roots are distinct. If $b=0$, the minimal polynomial is $X-t$, which is squarefree. In both cases the minimal polynomial is squarefree.

**Corollary (sector by sector).** Elements of $\Sigma_{11}$ and $\Sigma_{01}$ have distinct eigenvalues; elements of $\Sigma_{10}$ and $\Sigma_{00}$ are scalar; all are semisimple. In particular $\Sigma_{00}$ is not a defective nilpotent stratum.

*Proof.* The first two sectors have $b\neq0$ and the last two $b=0$; apply the theorem.

Unlike *[The Spectrum](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html)*, whose degenerate cone carries nilpotent and unipotent defective strata, $\mathbb{D}$ is reduced: its degenerate locus is the real axis, with no defective stratum. "Degenerate" records the vanishing of a condition, not a defect of the operator.

## The Sectors at a Glance

| sector | condition | description | dimension |
|---|---|---|---|
| $\Sigma_{11}$ | $t^2\neq b^2,\ b\neq0$ | six open regions: the positive-norm quadrants $t>|b|$ and $t<-|b|$, each cut by the real axis into two, and the negative-norm sectors $b>|t|$ and $b<-|t|$ | $2$ |
| $\Sigma_{01}$ | $t^2=b^2,\ b\neq0$ | the two punctured null lines $t=\pm b$, four rays; zero divisors with eigenvalues $2t$ and $0$ | $1$ |
| $\Sigma_{10}$ | $t^2\neq b^2,\ b=0$ | the two open real half-lines $t>0$ and $t<0$; units with the repeated eigenvalue $t$ | $1$ |
| $\Sigma_{00}$ | $t^2=b^2,\ b=0$ | the origin; the zero element | $0$ |

## Summary

The four sectors are the truth-value cells of the split norm and the spectral condition. $\Sigma_{11}$ is the complement of the three lines $b=0$, $t=b$ and $t=-b$; it is open and dense, of dimension two, with six components: the positive-norm quadrants $t>|b|$ and $t<-|b|$, each split by the removed real axis, and the negative-norm sectors $b>|t|$ and $b<-|t|$. Its elements are units with distinct eigenvalues.

$\Sigma_{01}$ is the two null lines with the origin removed, of dimension one and four rays; its elements are zero divisors $2t e_\pm$ with eigenvalues $2t$ and $0$. $\Sigma_{10}$ is the real axis minus the origin, of dimension one and two half-lines; its elements are scalar units with repeated eigenvalue $t$. $\Sigma_{00}$ is the origin, of dimension zero, the only element degenerate for both and not a zero divisor.

The closures are $\mathbb{D}$, the null cone, the real axis and the origin. Every element is semisimple, so no sector is defective; the origin is not a defective nilpotent stratum. The sectors are the geometry of the independence proved in *Relations between the Split Norm and Spectral Regularity and Degeneracy*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{D}=\mathbb{R}[j]/(j^2-1)$ | the split-complex algebra |
| $q=t+bj$ | a general element, $t,b\in\mathbb{R}$ |
| $q\bar q=t^2-b^2$ | the split norm |
| $b^2$ | the spectral condition |
| $e_\pm=\tfrac12(1\pm j)$ | the two non-trivial idempotents |
| $\Sigma_{ij}$ | the sector with norm $i$ and spectrum $j$ |
| $\mathcal{N}=\{t^2=b^2\}$ | the null cone, the two null lines |
| $\mathcal{S}=\{b=0\}$ | the real axis |

## Further Reading

- [Relations between the Split Norm and Spectral Regularity and Degeneracy](relations-between-the-split-norm-and-spectral-regularity-and-degeneracy.html), for the two conditions and their independence.
- [Spectral Regularity and Degeneracy in the Split-Complex Algebra](spectral-regularity-and-degeneracy-in-the-split-complex-algebra.html), for the eigenvalue criterion.
- [Zero Divisors of the Split-Complex Algebra](zero-divisors-of-the-split-complex-algebra.html), for the null lines and the annihilators.
- [Split-Complex Algebra](split-complex-algebra.html), for the product and the idempotent decomposition.
- [Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number](eigenvalue-decomposition-and-eigenbasis-of-a-split-complex-number.html), for the spectral decomposition.
- [Eigenbasis of a Split-Complex Number in Matrix Elements Representations](eigenbasis-of-a-split-complex-number-in-matrix-elements-representations.html), for the matrix models.
- [Worked Examples of Eigenbasis of a Split-Complex Number](worked-examples-of-eigenbasis-of-a-split-complex-number.html), for explicit computations.
