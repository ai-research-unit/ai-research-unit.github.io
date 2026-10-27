# __The Centraliser__

## Introduction

The centraliser of an element is the set of elements that commute with it. In the biquaternion algebra it is small and completely determined: for every non-central element it is the plane spanned by $e_t$ and the element itself, of complex dimension two, and its algebra type changes with the discriminant, $\mathbb{C}\times\mathbb{C}$ off the spectral-degenerate cone and the dual numbers on it. The central element is the single exception, and it lies on that same cone: there the centraliser is the whole algebra.

The article is the intrinsic half of the element's theory. It gives the centraliser, its type, the double centraliser and the dimension count, and it supplies the uniqueness proof of *The Semisimple–Nilpotent Split*: the two parts of the split are polynomials in the element, hence lie in a commutative centraliser, hence commute.

The article is form-free. It uses the product, the coefficients and the square of *The Square of an Element*.

## The Definition

For $\tilde Q\in\mathbb{B}$ the **centraliser** is

$$
C(\tilde Q)=\{\tilde X\in\mathbb{B}:\ \tilde X\tilde Q=\tilde Q\tilde X\},
$$

a unital complex subalgebra of $\mathbb{B}$ containing $\tilde Q$ and the centre $\mathbb{C}e_t$. The **double centraliser** is $C(C(\tilde Q))$.

Two elementary facts are used below.

- $C(\tilde Q)$ is a subalgebra: the sum and the product of two elements that commute with $\tilde Q$ commute with $\tilde Q$.
- $\mathbb{C}[\tilde Q]=\operatorname{span}\{e_t,\tilde Q\}\subseteq C(\tilde Q)$, with equality exactly when the two spaces have the same dimension.

## The Three Cases

**The order is by the discriminant, and centrality refines the degenerate side.** The first case is $B^2\neq0$, the spectrally regular case. The second and the third are the two halves of $B^2=0$: the central case $\vec Q=0$, and the non-central case $\vec Q\neq0$. The central element is therefore a particular case of the spectral-degenerate cone, the scalar line, not a fourth case beside it. In every case the centraliser contains $\mathbb{C}[\tilde Q]=\operatorname{span}\{e_t,\tilde Q\}$; its dimension is two off the centre and four at the centre, and its type off the centre is decided by the discriminant.

**First case: spectrally regular, $B^2\neq0$.** Then the minimal polynomial of $\tilde Q$ is

$$
p_{\tilde Q}(X)=(X-Q_t)^2+B^2,
$$

of degree two with distinct roots $\lambda_\pm=Q_t\pm iB$. In the matrix model $\tilde Q$ is a $2\times2$ matrix whose minimal polynomial has degree two, equal to the size of the matrix: it is **nonderogatory**. The commutant of a nonderogatory matrix is the algebra of polynomials in it, so

$$
C(\tilde Q)=\mathbb{C}[\tilde Q]\cong\mathbb{C}[X]/(p_{\tilde Q})\cong\mathbb{C}\times\mathbb{C},
$$

of complex dimension two. The isomorphism is the pair of evaluations at the two eigenvalues, $\tilde X\mapsto(\tilde X(\lambda_+),\tilde X(\lambda_-))$.

**Second case: spectrally degenerate and central, $B^2=0$ and $\vec Q=0$.** The condition $\vec Q=0$ is exactly $\tilde Q=Q_te_t$, with $Q_t$ arbitrary: this is the whole scalar line, the vertex of the spectral-degenerate cone, and it contains the origin. The element is central, so it commutes with everything:

$$
C(\tilde Q)=\mathbb{B},\qquad C(C(\tilde Q))=\mathbb{C}e_t .
$$

Its minimal polynomial is $X-Q_t$, of degree one, so the matrix is derogatory and $C(\tilde Q)\neq\mathbb{C}[\tilde Q]$: the polynomial algebra is the scalar line itself, of complex dimension one, while the centraliser has dimension four. The double centraliser is the centre, not the element: the central element carries no information.

**Third case: spectrally degenerate and non-central, $B^2=0$ and $\vec Q\neq0$.** Write $\tilde Q=Q_te_t+\vec\Upsilon$ with $\vec\Upsilon=\vec Q\neq0$ and $\vec\Upsilon^2=0$. The minimal polynomial is $(X-Q_t)^2$, of degree two, so the matrix is again nonderogatory, and

$$
C(\tilde Q)=\mathbb{C}[\tilde Q]\cong\mathbb{C}[X]/((X-Q_t)^2)\cong\mathbb{C}[\varepsilon]/(\varepsilon^2),
$$

the **dual numbers**, of complex dimension two. The isomorphism sends $\varepsilon$ to $\vec\Upsilon=\tilde Q-Q_te_t$.

The three cases are exhaustive: either $B^2\neq0$, or $B^2=0$ and $\vec Q$ is zero or non-zero. In both non-central cases the centraliser is two-dimensional, and the type is decided by the discriminant: $\mathbb{C}\times\mathbb{C}$ off the cone, the dual numbers on it. The central case is the whole algebra.

| case | element | $C(\tilde Q)$ | type | complex dimension |
|---|---|---|---|---|
| spectrally regular, $B^2\neq0$ | general, non-central | $\mathbb{C}[\tilde Q]$ | $\mathbb{C}\times\mathbb{C}$ | $2$ |
| spectrally degenerate, central, $B^2=0$ and $\vec Q=0$ | $Q_te_t$ | $\mathbb{B}$ | the algebra | $4$ |
| spectrally degenerate, non-central, $B^2=0$ and $\vec Q\neq0$ | $Q_te_t+\vec N$, $\vec N\neq0$, $\vec N^2=0$ | $\mathbb{C}[\tilde Q]$ | dual numbers | $2$ |

**The equality $C(\tilde Q)=\mathbb{C}[\tilde Q]$ is the statement that the element is nonderogatory**, and it fails only at the centre, $B^2=0$ with $\vec Q=0$, where the minimal polynomial has degree one while the algebra has dimension four.

## The Double Centraliser

For a non-central element, $C(\tilde Q)=\mathbb{C}[\tilde Q]$ is commutative and equals its own centraliser:

$$
C(C(\tilde Q))=C(\mathbb{C}[\tilde Q])=\mathbb{C}[\tilde Q]=C(\tilde Q).
$$

For the central element, $C(\tilde Q)=\mathbb{B}$ and $C(\mathbb{B})=\mathbb{C}e_t$. The two cases are the two extremes of the double-centraliser theorem: the bicommutant of a subalgebra of a matrix algebra is the subalgebra itself when the subalgebra is its own bicommutant, and the centre is the fixed point of the operation.

The double centraliser is the algebra-side statement of the module classification: the endomorphism ring of the simple module is $\mathbb{C}$, and the double centraliser of $\mathbb{C}$ is $\mathbb{B}$. The module form is *The Category of Modules*.

## The Uniqueness of the Split

The centraliser is what makes the semisimple–nilpotent split unique.

Let $\tilde Q=\tilde Q_s+\vec\Upsilon$ with $\tilde Q_s$ semisimple, $\vec\Upsilon$ nilpotent and $\tilde Q_s\vec\Upsilon=\vec\Upsilon\tilde Q_s$. Both $\tilde Q_s$ and $\vec\Upsilon$ are polynomials in $\tilde Q$ by the Chinese-remainder construction on the two eigenvalues, and $\vec\Upsilon$ has zero constant term; hence both lie in $\mathbb{C}[\tilde Q]=C(\tilde Q)$. The centraliser is commutative, so any two such decompositions commute, and their semisimple and nilpotent parts agree by the uniqueness of the Jordan decomposition in a commutative algebra.

The two explicit cases are these.

- $B^2\neq0$: $\tilde Q$ is semisimple already, so $\tilde Q_s=\tilde Q$ and $\vec\Upsilon=0$.
- $B^2=0$: $\tilde Q=Q_te_t+\vec Q$ with $\vec Q^2=0$, so $\tilde Q_s=Q_te_t$ and $\vec\Upsilon=\vec Q$. This covers both halves of the cone; at the centre $\vec Q=0$ and the nilpotent part vanishes.

The four types of the split — scalar, semisimple, Jordan, nilpotent — are the four positions of $(\tilde Q_s,\vec\Upsilon)$ in these two cases. They are stated, with the corner pattern, in *The Semisimple–Nilpotent Split*.

## Summary

- $C(\tilde Q)=\{\tilde X:\tilde X\tilde Q=\tilde Q\tilde X\}$ is a unital subalgebra containing $\tilde Q$.
- If $B^2\neq0$, then $C(\tilde Q)=\mathbb{C}[\tilde Q]\cong\mathbb{C}\times\mathbb{C}$, of complex dimension two.
- If $B^2=0$ and $\tilde Q=Q_te_t$ is central, then $C(\tilde Q)=\mathbb{B}$ and $C(C(\tilde Q))=\mathbb{C}e_t$.
- If $B^2=0$ and $\tilde Q$ is non-central, then $C(\tilde Q)=\mathbb{C}[\tilde Q]\cong\mathbb{C}[\varepsilon]/(\varepsilon^2)$, the dual numbers, of complex dimension two.
- The double centraliser of a non-central element is its centraliser.
- The parts of the semisimple–nilpotent split are polynomials in the element, hence lie in the commutative centraliser; this is the uniqueness proof.

## Summary of Notation

| symbol | meaning |
|---|---|
| $C(\tilde Q)$ | the centraliser of $\tilde Q$ |
| $\mathbb{C}[\tilde Q]=\operatorname{span}\{e_t,\tilde Q\}$ | the polynomial algebra of $\tilde Q$ |
| $\mathbb{C}[\varepsilon]/(\varepsilon^2)$ | the dual numbers |

## Further Reading

- [The Spectrum](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the discriminant and the two eigenvalues.
- [The Semisimple–Nilpotent Split](the-jordan-chevalley-decomposition-of-a-biquaternion.html), for the decomposition.
- [$M_2(\mathbb{C})$ Model : The Centraliser and the Double Centraliser](m2c-representation-the-centraliser-and-the-double-centraliser.html), for the matrix form.
