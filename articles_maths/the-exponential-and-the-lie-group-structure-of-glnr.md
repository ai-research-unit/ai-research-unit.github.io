# __The Exponential and the Lie Group Structure of $\mathrm{GL}_n(\mathbb{R})$__

## Introduction

**The general linear group is an open subset of the matrix algebra, so it is a Lie group with the algebra itself as its Lie algebra, and the bracket is the commutator; this is the whole content of the Lie theory in this setting, and everything else is the exponential.**

The article proves that $\mathrm{GL}_n(\mathbb{R})$ is a smooth manifold and a topological group with smooth operations, identifies its tangent space at the identity with $M_n(\mathbb{R})$, derives the bracket as the second-order term of the group law, proves that the one-parameter subgroups are exactly $t\mapsto e^{tX}$, states the Baker–Campbell–Hausdorff expansion to low order, and computes the Lie algebras and dimensions of the classical subgroups. It assumes *The Analysis on $M_n(\mathbb{R})$* and *The Exponential of a Real Matrix and Its Image*. It defers the global decomposition to *The Cartan Decomposition of $\mathrm{GL}_n(\mathbb{R})$*.

## The Manifold Structure

**Theorem.** $\mathrm{GL}_n(\mathbb{R})=\{X:\det X\ne0\}$ is an open subset of $M_n(\mathbb{R})\cong\mathbb{R}^{n^{2}}$, hence a smooth manifold of dimension $n^{2}$ with a single chart, the identity map.

*Proof.* The determinant is continuous and $\mathbb{R}^{\times}$ is open, so the preimage is open. An open subset of $\mathbb{R}^{n^{2}}$ is a smooth manifold with the inclusion as its only chart.

**The group operations are smooth.** The product $M_n\times M_n\to M_n$ is bilinear, hence polynomial in the entries, hence smooth. The inverse $X\mapsto X^{-1}$ is smooth on the open set by Cramer's rule, whose entries are polynomials divided by $\det X$.

**So $\mathrm{GL}_n(\mathbb{R})$ is a Lie group of dimension $n^{2}$.** It is not compact, not connected, and not simply connected, and these three failures are the subject of the topology articles.

**The tangent space at the identity is the whole algebra.** For an open subset of a vector space the tangent space at every point is the vector space itself, so

$$
T_{\mathrm{I}}\mathrm{GL}_n(\mathbb{R})=M_n(\mathbb{R})=\mathfrak{gl}_n(\mathbb{R}).
$$

**The tangent space at a general point is obtained by left translation.** $d(L_A)_{\mathrm{I}}(X)=AX$, so the tangent space at $A$ is $\{AX\}=M_n(\mathbb{R})$, and the left-invariant vector fields are the maps $A\mapsto AX$ for a fixed $X$.

## The Bracket from the Group Law

**The Lie bracket is the second-order defect of commutativity.** For $X,Y$ in the algebra,

$$
e^{tX}e^{sY}e^{-tX}e^{-sY}=\mathrm{I}+ts\,[X,Y]+O(3),
$$

where $O(3)$ denotes terms of total degree at least three in $t,s$. So the commutator of the group elements, at second order, is the bracket of the tangent vectors.

*Proof.* Expand each factor to second order: $e^{tX}=\mathrm{I}+tX+\tfrac{t^{2}}{2}X^{2}$, and similarly for the others. The product of the four expansions is $\mathrm{I}+ts(XY-YX)$ plus terms of degree three, since all terms of degree one and of pure degree two cancel in pairs.

**The bracket satisfies the Jacobi identity, and the identity is inherited from the associativity of the product.** Expanding $\operatorname{ad}_X\operatorname{ad}_Y-\operatorname{ad}_Y\operatorname{ad}_X=\operatorname{ad}_{[X,Y]}$ gives the Jacobi identity directly, and this is the abstract reason the commutator of an associative algebra is a Lie algebra.

**The Lie algebra is $\mathfrak{gl}_n(\mathbb{R})$, of dimension $n^{2}$, with centre $\mathbb{R}\mathrm{I}$.** The centre of the Lie algebra is the centre of the associative algebra, since $[X,Y]=0$ for all $Y$ is exactly the commuting condition.

**The derived algebra is $\mathfrak{sl}_n(\mathbb{R})$, of dimension $n^{2}-1$.** Every commutator has trace zero, and conversely every traceless matrix is a commutator: for $X$ traceless with a nonzero off-diagonal entry the formula $X=[A,X]$ type construction works, and the general case follows by a change of basis. So $[\mathfrak{gl}_n,\mathfrak{gl}_n]=\mathfrak{sl}_n$.

## One-Parameter Subgroups

**Theorem.** The smooth homomorphisms $\gamma:\mathbb{R}\to\mathrm{GL}_n(\mathbb{R})$ are exactly the maps $\gamma(t)=e^{tX}$ for $X\in M_n(\mathbb{R})$.

*Proof.* Let $X=\gamma'(0)$. Differentiating $\gamma(t+s)=\gamma(t)\gamma(s)$ in $s$ at $s=0$ gives $\gamma'(t)=\gamma(t)X$, a linear differential equation with constant coefficients and the initial condition $\gamma(0)=\mathrm{I}$. The unique solution is $\gamma(t)=e^{tX}$, by the same computation that defines the exponential. Conversely $e^{tX}$ is a homomorphism whenever the exponents commute, and $tX$ commutes with $sX$.

**So the exponential is the Lie functor on this group: it is the map from the algebra to the group that integrates a tangent vector into a subgroup.** The correspondence is injective at the level of $X$, since $\gamma'(0)=X$ recovers the vector.

**The correspondence is not injective at the level of subgroups.** Two different $X$ can give the same one-parameter subgroup only if $X=X'$; but two different subgroups can have images that intersect, and the exponential itself is not injective, since $e^{2\pi J}=\mathrm{I}$.

**Every one-parameter subgroup lies in the identity component.** Its image is connected and contains the identity, so it is contained in $\mathrm{GL}_n(\mathbb{R})^{+}$. This is the first sign that the exponential cannot reach the other component.

## The Baker–Campbell–Hausdorff Expansion

**The product of two exponentials is an exponential of a series in the two matrices.**

$$
\log\bigl(e^{X}e^{Y}\bigr)=X+Y+\tfrac12[X,Y]+\tfrac1{12}\bigl([X,[X,Y]]-[Y,[X,Y]]\bigr)-\tfrac1{24}[Y,[X,[X,Y]]]+\cdots
$$

The series converges for $\|X\|,\|Y\|$ small, and every term is a Lie polynomial, that is a combination of iterated brackets.

**Consequence: the group law near the identity is determined by the bracket.** The product in a neighbourhood of the identity, read in the coordinates given by the logarithm, is the BCH series. So the local structure of the group is entirely encoded in the Lie algebra, which is the content of the third Lie theorem in this setting.

**Consequence: the exponential is a group homomorphism exactly on commuting sets.** If $[X,Y]=0$ then all the bracket terms vanish and $e^{X+Y}=e^{X}e^{Y}$. If $[X,Y]\ne0$ then the product differs from $e^{X+Y}$ at second order, and at $n=2$ the difference is already visible: with $X=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ and $Y=\begin{pmatrix}0&0\\1&0\end{pmatrix}$ the matrix $e^{X}e^{Y}$ has diagonal entry $2$, where $e^{X+Y}$ has diagonal entry $\cosh 1\approx1.5431$, as the computation in the next paragraph shows.

**The computation at $n=2$.** $X^{2}=0$ and $Y^{2}=0$, so $e^{X}=\mathrm{I}+X$ and $e^{Y}=\mathrm{I}+Y$, and

$$
e^{X}e^{Y}=\mathrm{I}+X+Y+XY=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
$$

Meanwhile $X+Y=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ has $(X+Y)^{2}=\mathrm{I}$, so $e^{X+Y}=\cosh(1)\,\mathrm{I}+\sinh(1)(X+Y)$, whose $(1,1)$ entry is $\cosh 1\approx1.5431$, not $2$. So the two matrices differ.

## The Classical Subgroups

**Each classical subgroup is the zero set of polynomial equations and is a Lie subgroup whose Lie algebra is the corresponding subspace.**

| Group | Lie algebra | Dimension |
|---|---|---|
| $\mathrm{GL}_n(\mathbb{R})$ | $\mathfrak{gl}_n(\mathbb{R})=M_n(\mathbb{R})$ | $n^{2}$ |
| $\mathrm{SL}_n(\mathbb{R})$ | $\mathfrak{sl}_n(\mathbb{R})=\{X:\operatorname{tr}X=0\}$ | $n^{2}-1$ |
| $\mathrm{O}(n)$ | $\mathfrak{so}(n)=\operatorname{Skew}_n$ | $n(n-1)/2$ |
| $\mathrm{SO}(n)$ | $\mathfrak{so}(n)$ | $n(n-1)/2$ |
| $UT_n$ | the upper triangular algebra | $n(n+1)/2$ |

**The Lie algebra of $\mathrm{SL}_n(\mathbb{R})$ is the traceless part.** $\det e^{tX}=e^{t\operatorname{tr}X}=1$ for all $t$ exactly when $\operatorname{tr}X=0$, so the tangent space at the identity is the traceless subspace.

**The Lie algebra of $\mathrm{O}(n)$ is the antisymmetric part.** Differentiate $Q(t)^{\mathsf T}Q(t)=\mathrm{I}$ at $t=0$ along $Q(t)=e^{tX}$: $X^{\mathsf T}+X=0$. Conversely $e^{tX}$ is orthogonal for all $t$ when $X$ is antisymmetric, because $(e^{tX})^{\mathsf T}=e^{tX^{\mathsf T}}=e^{-tX}=(e^{tX})^{-1}$.

**The Lie algebra of the upper triangular group is the upper triangular algebra.** The exponential of an upper triangular matrix is upper triangular, and the logarithm of an upper triangular matrix with positive diagonal is upper triangular; the group is connected and simply connected, so the exponential is a diffeomorphism onto it.

**The dimension count is consistent with the decompositions.** $n^{2}=n(n-1)/2+n(n+1)/2$ is the split of the algebra into the antisymmetric and symmetric parts, and that is the Cartan decomposition at the level of the algebras.

## The Exponential Is Not Global

**The exponential is a local diffeomorphism and not a global one, and the two failures are independent.** It is not injective: $e^{2\pi J}=\mathrm{I}$. It is not surjective onto $\mathrm{GL}_n(\mathbb{R})^{+}$: the matrix $\begin{pmatrix}-1&1\\0&-1\end{pmatrix}$ has determinant $1$ and no real logarithm.

**The second failure is the interesting one for the Lie theory.** It says that the group is not the image of its Lie algebra under the exponential, so the correspondence between Lie algebras and Lie groups is not a bijection at the level of the exponential map. The correct statement is that the group is generated by the image, and that every element is a finite product of exponentials.

**Theorem.** Every element of $\mathrm{GL}_n(\mathbb{R})^{+}$ is a product of at most two exponentials.

*Proof.* By the polar decomposition $A=QP$ with $Q\in\mathrm{SO}(n)$ and $P$ positive definite. Every rotation is a rotation in a family of orthogonal planes, so $Q=e^{K}$ with $K$ antisymmetric, using the block form of *The Exponential of the Antisymmetric Part: One-Parameter Rotations*. And $P=e^{S}$ with $S=\log P$ symmetric, by the spectral theorem. So $A=e^{K}e^{S}$, a product of two exponentials.

**So the exponential covers the group after one multiplication, and the failure is confined to a single factor.** This is the sharp form of the statement that the image of the exponential is not the whole group.

## Summary

$\mathrm{GL}_n(\mathbb{R})$ is an open subset of $M_n(\mathbb{R})$, hence a Lie group of dimension $n^{2}$ with Lie algebra $\mathfrak{gl}_n(\mathbb{R})$ and bracket the commutator, which arises as the second-order defect of commutativity. The smooth one-parameter subgroups are exactly $t\mapsto e^{tX}$, the BCH series expresses the group law near the identity in terms of brackets, and $e^{X}e^{Y}\ne e^{X+Y}$ as soon as $[X,Y]\ne0$, already at $n=2$. The classical subgroups have Lie algebras $\mathfrak{sl}_n$, $\mathfrak{so}(n)$ and the upper triangular algebra, of dimensions $n^{2}-1$, $n(n-1)/2$ and $n(n+1)/2$. The exponential is neither injective nor surjective, but every element of the identity component is a product of at most two exponentials.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{gl}_n(\mathbb{R})$ | the Lie algebra $M_n(\mathbb{R})$ with the commutator |
| $\mathfrak{sl}_n(\mathbb{R})$ | the traceless matrices, of dimension $n^{2}-1$ |
| $\mathfrak{so}(n)$ | the antisymmetric matrices, of dimension $n(n-1)/2$ |
| $\gamma(t)=e^{tX}$ | the one-parameter subgroup of the tangent vector $X$ |
| $\operatorname{BCH}$ | the Baker–Campbell–Hausdorff series for $\log(e^{X}e^{Y})$ |
| $UT_n$ | the upper triangular group, of dimension $n(n+1)/2$ |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (American Mathematical Society, 2001), for the Lie group structure and the exponential.
- John Lee, *Introduction to Smooth Manifolds* (Springer, 2012), for the manifold structure of open subsets and the classical groups.
- [The Analysis on $M_n(\mathbb{R})$](the-analysis-on-mnr.html), for the norms, the derivatives and the exponential series.
- [The Exponential and the Lie Group Structure of $M_3(\mathbb{C})$](the-exponential-and-the-lie-group-of-m3c.html), for the complex case at $n=3$.
- [The Cartan Decomposition of $\mathrm{GL}_n(\mathbb{R})$](the-cartan-decomposition-of-glnr.html), for the global product decomposition.
