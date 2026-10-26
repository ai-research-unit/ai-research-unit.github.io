# __The Centraliser__

## Introduction

The centraliser of an element is the set of elements that commute with it. In the biquaternion algebra it is small and completely determined: for every non-central element it is the plane spanned by $e_t$ and the element itself, of complex dimension two, and only its algebra type changes with the discriminant. The central element is the single exception, and there the centraliser is the whole algebra.

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

**The central element.** If $\tilde Q=Q_te_t$ then $\tilde Q$ commutes with everything, so

$$
C(\tilde Q)=\mathbb{B},\qquad C(C(\tilde Q))=\mathbb{C}e_t .
$$

The double centraliser is the centre, not the element: the central element carries no information.

**The element off the cone, $B^2\neq0$.** Then the minimal polynomial of $\tilde Q$ is

$$
p_{\tilde Q}(X)=(X-Q_t)^2+B^2,
$$

of degree two with distinct roots $\lambda_\pm=Q_t\pm iB$. In the matrix model $\tilde Q$ is a $2\times2$ matrix whose minimal polynomial has degree two, equal to the size of the matrix: it is **nonderogatory**. The commutant of a nonderogatory matrix is the algebra of polynomials in it, so

$$
C(\tilde Q)=\mathbb{C}[\tilde Q]\cong\mathbb{C}[X]/(p_{\tilde Q})\cong\mathbb{C}\times\mathbb{C},
$$

of complex dimension two. The isomorphism is the pair of evaluations at the two eigenvalues, $\tilde X\mapsto(\tilde X(\lambda_+),\tilde X(\lambda_-))$.

**The element on the cone, $B^2=0$ and $\tilde Q$ non-central.** Write $\tilde Q=Q_te_t+\tilde N$ with $\tilde N=\vec Q\neq0$ and $\tilde N^2=0$. The minimal polynomial is $(X-Q_t)^2$, of degree two, so the matrix is again nonderogatory, and

$$
C(\tilde Q)=\mathbb{C}[\tilde Q]\cong\mathbb{C}[X]/((X-Q_t)^2)\cong\mathbb{C}[\varepsilon]/(\varepsilon^2),
$$

the **dual numbers**, of complex dimension two. The isomorphism sends $\varepsilon$ to $\tilde N=\tilde Q-Q_te_t$.

The three cases are exhaustive: an element is central, or $B^2\neq0$, or $B^2=0$ and non-central. In every non-central case the centraliser is two-dimensional, and the type is decided by the discriminant:

| element | $C(\tilde Q)$ | type | dimension |
|---|---|---|---|
| $\tilde Q=Q_te_t$ | $\mathbb{B}$ | the algebra | $4$ |
| $B^2\neq0$ | $\mathbb{C}[\tilde Q]$ | $\mathbb{C}\times\mathbb{C}$ | $2$ |
| $B^2=0$, $\tilde Q$ non-central | $\mathbb{C}[\tilde Q]$ | dual numbers | $2$ |

**The equality $C(\tilde Q)=\mathbb{C}[\tilde Q]$ is the statement that the element is nonderogatory**, and it fails only at the centre, where the minimal polynomial has degree one while the algebra has dimension four.

## The Double Centraliser

For a non-central element, $C(\tilde Q)=\mathbb{C}[\tilde Q]$ is commutative and equals its own centraliser:

$$
C(C(\tilde Q))=C(\mathbb{C}[\tilde Q])=\mathbb{C}[\tilde Q]=C(\tilde Q).
$$

For the central element, $C(\tilde Q)=\mathbb{B}$ and $C(\mathbb{B})=\mathbb{C}e_t$. The two cases are the two extremes of the double-centraliser theorem: the bicommutant of a subalgebra of a matrix algebra is the subalgebra itself when the subalgebra is its own bicommutant, and the centre is the fixed point of the operation.

The double centraliser is the algebra-side statement of the module classification: the endomorphism ring of the simple module is $\mathbb{C}$, and the double centraliser of $\mathbb{C}$ is $\mathbb{B}$. The module form is *The Category of Modules*.

## The Uniqueness of the Split

The centraliser is what makes the semisimple–nilpotent split unique.

Let $\tilde Q=\tilde S+\tilde N$ with $\tilde S$ semisimple, $\tilde N$ nilpotent and $\tilde S\tilde N=\tilde N\tilde S$. Both $\tilde S$ and $\tilde N$ are polynomials in $\tilde Q$ by the Chinese-remainder construction on the two eigenvalues, and $\tilde N$ has zero constant term; hence both lie in $\mathbb{C}[\tilde Q]=C(\tilde Q)$. The centraliser is commutative, so any two such decompositions commute, and their semisimple and nilpotent parts agree by the uniqueness of the Jordan decomposition in a commutative algebra.

The two explicit cases are these.

- $B^2\neq0$: $\tilde Q$ is semisimple already, so $\tilde S=\tilde Q$ and $\tilde N=0$.
- $B^2=0$: $\tilde Q=Q_te_t+\vec Q$ with $\vec Q^2=0$, so $\tilde S=Q_te_t$ and $\tilde N=\vec Q$.

The four types of the split — scalar, semisimple, Jordan, nilpotent — are the four positions of $(\tilde S,\tilde N)$ in these two cases. They are stated, with the corner pattern, in *The Semisimple–Nilpotent Split*.

## Summary

- $C(\tilde Q)=\{\tilde X:\tilde X\tilde Q=\tilde Q\tilde X\}$ is a unital subalgebra containing $\tilde Q$.
- For a non-central element $C(\tilde Q)=\mathbb{C}[\tilde Q]$, of complex dimension two.
- Off the cone, $C(\tilde Q)\cong\mathbb{C}\times\mathbb{C}$; on the cone, $C(\tilde Q)\cong\mathbb{C}[\varepsilon]/(\varepsilon^2)$, the dual numbers.
- For the central element, $C(\tilde Q)=\mathbb{B}$ and $C(C(\tilde Q))=\mathbb{C}e_t$.
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
