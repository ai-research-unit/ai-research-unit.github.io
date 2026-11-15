# __The Two Halves over $\mathbb{C}$: Hermitian and Skew-Hermitian at $n=2$__

## Introduction

**Over $\mathbb{C}$ the two halves are the Hermitian matrices of real dimension $4$ and the skew-Hermitian ones of real dimension $4$, and the determinant of a Hermitian matrix of order two is a Minkowski form of signature $(1,3)$.**

The article proves the split $M_2(\mathbb{C})=\operatorname{Herm}_2\oplus\mathfrak{u}(2)$ as the eigenspaces of the conjugate transpose, identifies $\operatorname{Herm}_2$ with Minkowski space through the determinant and with the Pauli coordinates, identifies the skew-Hermitian half with the Lie algebra $\mathfrak{u}(2)=\mathbb{R}iI\oplus\mathfrak{su}(2)$, computes the product rules $\{H,K\}$ Hermitian and $[H,K]$ skew-Hermitian, and reads the light cone and the rank-one elements. It assumes *The Involutions of $M_2(\mathbb{C})$ over $\mathbb{R}$ and over $\mathbb{C}$* for the conjugate transpose, and *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$* for the real slice.

It defers the orthogonal complement to *The Two Halves as Orthogonal Complements at $n=2$*, the spectral statement to *The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents*, and the complex structure on the algebra to *The Element: The Coordinates and the Conjugations*.

## The Split over $\mathbb{C}$

**Theorem.** Every complex matrix is the sum of a Hermitian and a skew-Hermitian one in exactly one way:

$$
M_2(\mathbb{C})=\operatorname{Herm}_2\oplus\mathfrak{u}(2),\qquad \dim_{\mathbb{R}}=4+4=8 .
$$

**Proof.** $A=H+K$ with $H=\tfrac12(A+A^{*})$ and $K=\tfrac12(A-A^{*})$; the two pieces satisfy $H^{*}=H$ and $K^{*}=-K$. If $H+K=0$, applying the conjugate transpose gives $H-K=0$, so both vanish.

**The two halves are the eigenspaces of the conjugate transpose.** The map $\theta(A)=A^{*}$ has $+1$ on $\operatorname{Herm}_2$ and $-1$ on the skew-Hermitian half, so the split is the eigenspace decomposition of an involution, exactly as over $\mathbb{R}$ with the transpose.

**The halves have the same real dimension.** Each is four-dimensional over $\mathbb{R}$: the Hermitian condition fixes two real equations on the four complex entries, and the skew-Hermitian condition fixes the other two.

**The real slice.** The real matrices inside $\operatorname{Herm}_2$ are the real symmetric matrices, and the real matrices inside the skew-Hermitian half are the real antisymmetric ones. So the two halves of this article restrict on $M_2(\mathbb{R})$ to the two halves of *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$*.

## The Hermitian Half as Minkowski Space

**Proposition.** Every Hermitian matrix of order two is

$$
X=x_{0}I+x_{1}\sigma_{1}+x_{2}\sigma_{3}+x_{3}\sigma_{2}
=\begin{pmatrix}x_{0}+x_{1}&x_{2}-ix_{3}\\ x_{2}+ix_{3}&x_{0}-x_{1}\end{pmatrix}
$$

with real $x_{0},x_{1},x_{2},x_{3}$, and the four matrices $I,\sigma_{1},\sigma_{3},\sigma_{2}$ form a real basis.

**Proof.** A Hermitian matrix has real diagonal entries and conjugate off-diagonal entries, so it has four real parameters; the four displayed matrices are Hermitian and independent, and the display inverts the coordinates.

**Theorem.** In these coordinates

$$
\det X=x_{0}^{2}-x_{1}^{2}-x_{2}^{2}-x_{3}^{2},
$$

so the determinant is a quadratic form of signature $(1,3)$ on $\operatorname{Herm}_2$.

**Proof.** $\det$ of the displayed matrix is $(x_{0}+x_{1})(x_{0}-x_{1})-(x_{2}-ix_{3})(x_{2}+ix_{3})=x_{0}^{2}-x_{1}^{2}-x_{2}^{2}-x_{3}^{2}$. The Gram matrix of the form in the basis is $\operatorname{diag}(1,-1,-1,-1)$.

**Corollary (the light cone).** The Hermitian matrices of determinant zero form the cone of the three space directions plus the time axis; the cone is the set of rank-one positive semidefinite Hermitian matrices.

**Proof.** A Hermitian matrix of order two with determinant zero has rank one or zero. It is positive semidefinite exactly when $x_{0}\ge0$ and $x_{0}^{2}\ge x_{1}^{2}+x_{2}^{2}+x_{3}^{2}$, that is on the forward cone.

**The group action.** For $g\in\mathrm{SL}_2(\mathbb{C})$ the map $X\mapsto gXg^{*}$ preserves $\operatorname{Herm}_2$ and multiplies the determinant by $|\det g|^{2}=1$, so it acts by Lorentz transformations of the Minkowski space of the Hermitian half.

**The traces are positive definite.** $\operatorname{tr}(X^{2})=2(x_{0}^{2}+x_{1}^{2}+x_{2}^{2}+x_{3}^{2})$, so the trace form is positive definite on $\operatorname{Herm}_2$, unlike the determinant.

## The Skew-Hermitian Half as $\mathfrak{u}(2)$

**Proposition.** The skew-Hermitian matrices are exactly the products $iX$ with $X$ Hermitian, and they form the Lie algebra $\mathfrak{u}(2)$ of the unitary group.

**Proof.** $K^{*}=-K$ is equivalent to $(iK)^{*}=-iK^{*}=iK$, so $iK$ is Hermitian. The unitary group consists of the matrices with $g^{*}g=I$, and differentiating at the identity gives $K^{*}+K=0$.

**Corollary.** $\mathfrak{u}(2)=\mathbb{R}iI\oplus\mathfrak{su}(2)$, with $\mathfrak{su}(2)$ the traceless skew-Hermitian matrices, of real dimension $3$.

**Proof.** A skew-Hermitian matrix has a purely imaginary trace; subtracting the scalar part leaves the traceless skew-Hermitian matrices, which are three real dimensions.

**Proposition (the structure constants).** With $S_{a}=i\sigma_{a}$,

$$
[S_{a},S_{b}]=-2i\,\epsilon_{abc}S_{c},
$$

so $\mathfrak{su}(2)$ is isomorphic to $\mathfrak{so}(3)$.

**Proof.** The Pauli matrices satisfy $[\sigma_{a},\sigma_{b}]=2i\epsilon_{abc}\sigma_{c}$; multiplying both factors by $i$ multiplies the bracket by $i^{2}=-1$.

**Example.** $[S_{1},S_{2}]=-2S_{3}$, and the three brackets are the multiplication table of the rotations of three-dimensional space.

## The Products of the Two Halves

**Proposition.** For Hermitian $H,K$,

$$
(HK)^{*}=KH,
$$

so $HK+KH$ is Hermitian and $HK-KH$ is skew-Hermitian.

**Proof.** $(HK)^{*}=K^{*}H^{*}=KH$. Then $(HK+KH)^{*}=KH+HK$ and $(HK-KH)^{*}=KH-HK=-(HK-KH)$.

**Corollary.** The Hermitian half is a Jordan algebra under the product $\tfrac12(HK+KH)$ and the skew-Hermitian half is a Lie algebra under the commutator, and both are closed.

**Proof.** The two statements are the two halves of the proposition; the axioms of a Jordan algebra are checked by polarising the associativity of the ambient product.

**Proposition.** For skew-Hermitian $S$ and Hermitian $H$ the commutator $[S,H]$ is traceless Hermitian.

**Proof.** $[S,H]^{*}=[H^{*},S^{*}]=[H,-S]=[S,H]$, so it is Hermitian; its trace is zero because the trace is a linear functional vanishing on commutators.

**The product rules are the ones of the four tables.** At order two the tables $HH$, $HK$, $KH$, $KK$ are written out in *The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$ at $n=2$*, where the letters denote the two halves.

## The Traces and the Real Part

**Proposition.** The trace is real on $\operatorname{Herm}_2$ and purely imaginary on $\mathfrak{u}(2)$.

**Proof.** A Hermitian matrix has real diagonal, so its trace is real; a skew-Hermitian one has purely imaginary diagonal.

**Proposition.** For Hermitian $H,K$ the number $\operatorname{tr}(HK)$ is real and nonnegative when $H=K$; for $H$ Hermitian and $K$ skew-Hermitian the number $\operatorname{tr}(HK)$ is purely imaginary.

**Proof.** $\overline{\operatorname{tr}(HK)}=\operatorname{tr}((HK)^{*})=\operatorname{tr}(KH)=\operatorname{tr}(HK)$ by cyclicity, so it is real. If $K=iS$ with $S$ Hermitian then $\operatorname{tr}(HK)=i\operatorname{tr}(HS)$ is purely imaginary. Positivity follows because $H$ is diagonalisable by a unitary matrix with real eigenvalues.

**Corollary (the subtlety of the complex form).** The two halves are not orthogonal for the complex bilinear form $\operatorname{tr}(XY)$: with $H=I$ and $K=iI$ one has $\operatorname{tr}(HK)=2i$. They are orthogonal for the real form $\operatorname{Re}\operatorname{tr}(X^{*}Y)$, since then the pairing is $\operatorname{Re}\operatorname{tr}(H^{*}K)=0$.

**The Hermitian form is the right one over $\mathbb{C}$.** The form $\langle X,Y\rangle=\operatorname{tr}(X^{*}Y)$ is positive definite Hermitian on $M_2(\mathbb{C})$, and the two halves are orthogonal for its real part; that form is *The Hilbert–Schmidt Form at $n=2$*.

## The Idempotents and the Two Halves

**Proposition.** A Hermitian idempotent of order two is exactly a matrix $\tfrac12(I+\vec n\cdot\vec\sigma)$ with $\vec n$ a unit vector in $\mathbb{R}^{3}$, and every such matrix has rank one.

**Proof.** $P$ Hermitian and $P^{2}=P$ has eigenvalues $0$ and $1$, so $\operatorname{tr}P$ is $0,1,2$; the values $0$ and $2$ give $P=0$ and $P=I$, and the value $1$ gives $P=\tfrac12(I+\vec n\cdot\vec\sigma)$ with $\vec n$ of norm $1$ because $\operatorname{tr}(P^{2})=\operatorname{tr}(P)$ forces $|\vec n|^{2}=1$.

**Corollary.** The rank-one Hermitian idempotents form a sphere $S^{2}$, and the projections onto the lines of $\mathbb{C}^{2}$ are exactly them.

**Proof.** Each is the projection onto the eigenspace of the eigenvalue $1$, which is a line, and every line has a projection of this form.

**The two halves meet the idempotents differently.** A symmetric idempotent is a Hermitian idempotent with real $\vec n$, so the symmetric ones form the equator $S^{1}$ of the sphere; a skew-Hermitian matrix is never an idempotent except $0$, because its eigenvalues are purely imaginary.

## Summary

The complex matrices split into the Hermitian half and the skew-Hermitian half, each of real dimension $4$, as the eigenspaces of the conjugate transpose. In the Pauli coordinates $X=x_{0}I+x_{1}\sigma_{1}+x_{2}\sigma_{3}+x_{3}\sigma_{2}$ the determinant of a Hermitian matrix is $x_{0}^{2}-x_{1}^{2}-x_{2}^{2}-x_{3}^{2}$, of signature $(1,3)$, and the light cone is the set of rank-one positive semidefinite matrices.

The skew-Hermitian half is $\mathfrak{u}(2)=\mathbb{R}iI\oplus\mathfrak{su}(2)$, with $[S_{a},S_{b}]=-2i\epsilon_{abc}S_{c}$. For Hermitian $H,K$ the sum $HK+KH$ is Hermitian and the difference is skew-Hermitian, the trace is real on the Hermitian half and purely imaginary on the other, and $\operatorname{tr}(HK)$ is real while $\operatorname{tr}(HK)$ with $K$ skew is purely imaginary. The Hermitian idempotents form the sphere $S^{2}$, and the symmetric ones form its equator $S^{1}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Herm}_2$ | the fixed space of $A\mapsto A^{*}$, real dimension $4$ |
| $\mathfrak{u}(2)$ | the skew-Hermitian matrices, the Lie algebra of $\mathrm{U}(2)$ |
| $\mathfrak{su}(2)$ | the traceless skew-Hermitian matrices, dimension $3$ |
| $S_{a}$ | $i\sigma_{a}$, the traceless skew-Hermitian basis |
| $x_{0},x_{1},x_{2},x_{3}$ | the Pauli coordinates of a Hermitian matrix |
| $\det$ | on $\operatorname{Herm}_2$, the form of signature $(1,3)$ |
| $P$ | a Hermitian idempotent, $\tfrac12(I+\vec n\cdot\vec\sigma)$ |
| $\vec n$ | a unit vector of $\mathbb{R}^{3}$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the Hermitian and skew-Hermitian decomposition and its traces.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for $\mathfrak{su}(2)\cong\mathfrak{so}(3)$ and the structure constants of the Pauli matrices.
- [The Involutions of $M_2(\mathbb{C})$ over $\mathbb{R}$ and over $\mathbb{C}$](the-involutions-of-m2c-over-r-and-over-c.html), for the conjugate transpose whose eigenspaces these halves are.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-2.html), for the real slice of this split.
- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the idempotents and the corner recursion at general order.
