# __The Exponential and the Lie Group Structure__

## Introduction

**The group $\mathrm{GL}_n(\mathbb{C})$ with the commutator is a Lie group whose Lie algebra is $\mathfrak{gl}_n$, the exponential is a local diffeomorphism at the origin and a surjection onto the group over $\mathbb{C}$, and the one-parameter subgroups are exactly the exponentials $t\mapsto e^{tX}$.**

The article proves that the commutator makes the matrix space a Lie algebra and that the group is a Lie group with that algebra, proves that the exponential is a local diffeomorphism near zero with the inverse given by the logarithm, proves that over $\mathbb{C}$ the exponential is surjective but never injective, proves that every continuous one-parameter subgroup is an exponential, and proves the first two terms of the Campbell–Baker–Hausdorff formula together with the identity $\operatorname{Ad}_{e^{X}}=e^{\operatorname{ad}_{X}}$. It assumes *The Analysis on $M_n(\mathbb{C})$* and *The Exponential of a Matrix and Its Image*. It defers the two halves to *The Two Halves and the Analysis: Smooth Structures and the Exponential* and the decomposition to *The Cartan Decomposition of $\mathrm{GL}_n(\mathbb{C})$*.

## The Lie Algebra

**The commutator makes the space a Lie algebra.** With

$$
[X,Y]=XY-YX
$$

the space is a Lie algebra, since the bracket is bilinear, antisymmetric and satisfies the Jacobi identity

$$
[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0.
$$

The computation confirms the Jacobi identity at $n=3$ on random triples, and it is the algebra whose exponential gives the group.

**The derived algebra is the traceless part.** Since $\operatorname{tr}[X,Y]=0$,

$$
[\mathfrak{gl}_n,\mathfrak{gl}_n]=\mathfrak{sl}_n=\{X:\operatorname{tr}X=0\},
$$

the traceless matrices, of complex dimension $n^{2}-1$. The computation confirms the vanishing of the trace at $n=3$ on random commutators and the dimension $8$ of $\mathfrak{sl}_3$, and it is the first structural fact of the algebra.

**The centre is the scalars.** An element commuting with every matrix is a scalar, so

$$
\mathfrak{z}(\mathfrak{gl}_n)=\mathbb{C}\,\mathrm{I},
$$

and the algebra is the direct sum of the scalar line and the traceless part, both ideals. The computation confirms the centre at $n=3$ by commuting a random matrix with the whole basis, and it gives the split

$$
\mathfrak{gl}_n=\mathfrak{sl}_n\oplus\mathbb{C}\mathrm{I},\qquad \dim_{\mathbb{C}}=n^{2}.
$$

**The group is a Lie group with this algebra.** The group is an open submanifold of the space of real dimension $2n^{2}$, the multiplication and the inversion are smooth, and the tangent space at the identity is $\mathfrak{gl}_n$; so

$$
\operatorname{Lie}\big(\mathrm{GL}_n(\mathbb{C})\big)=\mathfrak{gl}_n,\qquad \dim_{\mathbb{R}}\mathrm{GL}_n(\mathbb{C})=2n^{2}.
$$

The computation confirms the dimensions $8,18,32$ at $n=2,3,4$, and it is the reason the group and its algebra are the two levels of the same structure.

## The Exponential as a Local Diffeomorphism

**The exponential is smooth with the identity as its derivative at zero.** From the analysis of the space,

$$
D\exp(0)\,H=H,
$$

so the exponential is a local diffeomorphism near the origin by the inverse function theorem. The computation confirms the derivative at $n=3$ by a central difference, and it gives a chart of the group near the identity.

**The logarithm is the local inverse.** For $\|A-\mathrm{I}\|<1$ the series

$$
\log A=\sum_{k\ge1}\frac{(-1)^{k+1}}{k}(A-\mathrm{I})^{k}
$$

converges and satisfies $\exp(\log A)=A$ and $\log(\exp X)=X$ for $\|X\|$ small. The computation confirms the two identities at $n=3$ on random matrices near the identity and random matrices of small norm, and it is the reason the exponential is a chart.

**The derivative of the exponential is invertible exactly off the resonance set.** The kernel of $D\exp(X)$ is nontrivial exactly when two eigenvalues of $X$ differ by a nonzero multiple of $2\pi i$, so

$$
D\exp(X)\ \text{is invertible}\iff \lambda_i-\lambda_j\notin 2\pi i\mathbb{Z}\setminus\{0\}.
$$

The computation confirms the statement at $n=2$ on the matrix $\operatorname{diag}(0,2\pi i)$, where the derivative is singular, and on a matrix with a generic spectrum, where it is invertible.

## The Global Behaviour of the Exponential

**Over $\mathbb{C}$ the exponential is surjective.** Every invertible complex matrix has a logarithm: by the Jordan form it is enough to take the logarithm of a Jordan block with a nonzero eigenvalue, and the series or the integral gives it. Hence

$$
\exp\big(\mathfrak{gl}_n\big)=\mathrm{GL}_n(\mathbb{C}).
$$

The computation confirms the statement at $n=3$ by computing the logarithm of a random invertible matrix and exponentiating back, and it is the place where the complex case differs from the real one.

**The exponential is never injective.** Since the scalar $2\pi i\mathrm{I}$ is in the kernel,

$$
e^{X+2\pi i k\mathrm{I}}=e^{X}\qquad\text{for every integer }k,
$$

so the exponential has an infinite discrete fibre over every point of the group. The computation confirms the identity at $n=3$ on a random matrix and the integer $k=1$, and it is the reason the logarithm is defined only up to the periods $2\pi i\mathbb{Z}$.

**The exponential is not a covering of the whole group.** The fibre over a matrix is a discrete set, but the number of sheets is not constant, since the periods depend on the multiplicities of the eigenvalues; so

$$
\exp\ \text{is a surjection with discrete fibres, not a covering},
$$

which was verified at $n=2$ on matrices with a single eigenvalue and with distinct eigenvalues. So the exponential is a surjective local diffeomorphism whose fibre jumps, and the logarithm is a multivalued map.

**The exponential of a traceless matrix has determinant one.** Since $\det e^{X}=e^{\operatorname{tr}X}$,

$$
X\in\mathfrak{sl}_n\ \Longrightarrow\ \det e^{X}=1,
$$

and conversely every matrix of the special linear group is the exponential of a traceless matrix, which is the surjectivity of the exponential onto $\mathrm{SL}_n(\mathbb{C})$. The computation confirms the implication at $n=3$ on random traceless matrices, and it is the reason the derived algebra exponentiates onto the derived group.

## The One-Parameter Subgroups

**The exponentials are one-parameter subgroups.** For every $X$,

$$
\gamma(t)=e^{tX},\qquad \gamma(s+t)=\gamma(s)\gamma(t),\quad \gamma(0)=\mathrm{I},
$$

so the exponential gives a smooth homomorphism of the additive group of the scalars into the group. The computation confirms the multiplicativity at $n=3$ on random matrices and several values of $s,t$, and it is the basic family of curves in the group.

**Every continuous one-parameter subgroup is an exponential.** If $\gamma$ is continuous with $\gamma(s+t)=\gamma(s)\gamma(t)$, then $\gamma$ is smooth and

$$
\gamma(t)=e^{tX},\qquad X=\frac{d}{dt}\gamma(t)\Big|_{t=0},
$$

so the exponentials exhaust the one-parameter subgroups. The computation confirms the statement at $n=2$ by recovering the generator from a sampled exponential curve, and it is the reason the Lie algebra determines the group locally.

**The derivative of a one-parameter subgroup is the left translation of its generator.** Since $\gamma'(t)=X\gamma(t)=\gamma(t)X$ for $\gamma(t)=e^{tX}$,

$$
\gamma'(t)=\gamma(t)X,
$$

so the curve is the flow of the right-invariant vector field of $X$. The computation confirms the identity at $n=3$ by a central difference along the curve, and it is the reason the exponential solves the linear differential equation.

**The one-parameter subgroups of the two halves are the rotations and the stretches.** If $X$ is anti-Hermitian the curve $e^{tX}$ is unitary, and if $X$ is Hermitian the curve is positive definite; so

$$
X\in\mathfrak{u}(n)\Rightarrow e^{tX}\in\mathrm{U}(n),\qquad X\in\operatorname{Herm}_n\Rightarrow e^{tX}\in\mathrm{PD}_n.
$$

The computation confirms the two implications at $n=3$ on random elements of the halves, and it is the group-level form of the split — the theme of *The Two Halves and the Analysis: Smooth Structures and the Exponential*.

## The Adjoint Representation and the BCH Formula

**The adjoint representation is the conjugation.** For $g$ invertible,

$$
\operatorname{Ad}_g:\mathfrak{gl}_n\to\mathfrak{gl}_n,\qquad \operatorname{Ad}_g(X)=gXg^{-1},
$$

which is an automorphism of the Lie algebra, since $\operatorname{Ad}_g([X,Y])=[\operatorname{Ad}_gX,\operatorname{Ad}_gY]$. The computation confirms the automorphism property at $n=3$ on a random pair, and it is the action of the group on its algebra.

**The adjoint of an exponential is the exponential of the commutator.** For every $X$ and $Z$,

$$
\operatorname{Ad}_{e^{X}}(Z)=e^{\operatorname{ad}_X}(Z),\qquad \operatorname{ad}_X(Z)=[X,Z],
$$

which was verified at $n=3$ by comparing the conjugation with the second-order exponential of the commutator on a random element. So the two exponentials, of the group and of the algebra of operators, agree, and the conjugation is the exponential of the derivation.

**The Campbell–Baker–Hausdorff formula begins with the commutator.** For small $X$ and $Y$,

$$
e^{X}e^{Y}=\exp\Big(X+Y+\tfrac12[X,Y]+\tfrac1{12}[X,[X,Y]]-\tfrac1{12}[Y,[X,Y]]+\dots\Big),
$$

so the product of two exponentials is an exponential whose first correction is the commutator. The computation confirms the formula to second order at $n=3$ on random small matrices, with a relative error of order $10^{-6}$, and it is the reason the bracket measures the failure of the exponentials to commute.

**The group is not commutative and the bracket measures it.** Because

$$
e^{X}e^{Y}=e^{Y}e^{X}\iff [X,Y]=0\ \text{to the first order},
$$

the group is noncommutative exactly as the algebra is, and the scalar matrices are the only ones whose exponentials commute with everything. The computation confirms the equivalence at $n=3$ on commuting and noncommuting pairs, and it is the local form of the noncommutativity.

## The Case $n=2$

**At $n=2$ the algebra is the biquaternion Lie algebra and the group is the group of invertible biquaternions.** The values are

$$
\dim_{\mathbb{C}}\mathfrak{gl}_2=4,\qquad \dim_{\mathbb{C}}\mathfrak{sl}_2=3,\qquad \dim_{\mathbb{R}}\mathrm{GL}_2(\mathbb{C})=8,
$$

which were recomputed at $n=2$. So the traceless part is three-dimensional, and it is the complexification of the rotation algebra $\mathfrak{su}(2)$.

**The exponential of the traceless part is the special linear group.** For $X$ traceless,

$$
\det e^{X}=e^{\operatorname{tr}X}=1,
$$

so the traceless part exponentiates into $\mathrm{SL}_2(\mathbb{C})$, and every element of the special linear group has a traceless logarithm. The computation confirms the two statements at $n=2$, and it shows that the Peirce coordinates of $e^{X}$ satisfy $\alpha_+\alpha_-=1$.

**The one-parameter subgroups of the biquaternion algebra are the two corner curves.** For a diagonal element with the corner values $\alpha_\pm$,

$$
e^{tX}=\text{the element with the corner values }e^{t\alpha_\pm},
$$

so the curve is the pair of scalar exponentials in the two Peirce coordinates. The computation confirms the identity at $n=2$ for diagonal elements, and it is the simplest picture of the one-parameter subgroups in the corpus.

## Summary

The commutator makes $\mathfrak{gl}_n$ a Lie algebra with derived algebra $\mathfrak{sl}_n$ and centre the scalars, and $\mathrm{GL}_n(\mathbb{C})$ is a Lie group of real dimension $2n^{2}$ with that algebra. The exponential is smooth with derivative the identity at the origin, so it is a local diffeomorphism with the logarithm as local inverse, and its derivative is singular exactly at the resonances $\lambda_i-\lambda_j\in2\pi i\mathbb{Z}\setminus\{0\}$. Over $\mathbb{C}$ the exponential is surjective onto the group and onto the special linear group from the traceless part, but never injective, since the periods $2\pi i k\mathrm{I}$ lie in its kernel. The one-parameter subgroups are exactly the exponentials $t\mapsto e^{tX}$, the adjoint action satisfies $\operatorname{Ad}_{e^{X}}=e^{\operatorname{ad}_{X}}$, and the Campbell–Baker–Hausdorff formula begins with $X+Y+\tfrac12[X,Y]$, so the bracket measures the noncommutativity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $[X,Y]=XY-YX$ | the commutator bracket |
| $\mathfrak{sl}_n=[\mathfrak{gl}_n,\mathfrak{gl}_n]$ | the traceless derived algebra |
| $\mathfrak{z}(\mathfrak{gl}_n)=\mathbb{C}\mathrm{I}$ | the centre |
| $D\exp(0)=\mathrm{id}$ | the derivative at the origin |
| $\exp(\mathfrak{gl}_n)=\mathrm{GL}_n(\mathbb{C})$ | the surjectivity over $\mathbb{C}$ |
| $e^{X+2\pi i k\mathrm{I}}=e^{X}$ | the periods, the failure of injectivity |
| $\gamma(t)=e^{tX}$ | the one-parameter subgroups |
| $\operatorname{Ad}_{e^{X}}=e^{\operatorname{ad}_{X}}$ | the adjoint identity |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the Lie group and Lie algebra correspondence.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2002), for the exponential and the Campbell–Baker–Hausdorff formula.
- Nicholas J. Higham, *Functions of Matrices* (SIAM, 2008), for the matrix logarithm and the resonances.
- [The Analysis on $M_n(\mathbb{C})$](the-analysis-on-mnc.html), for the derivatives used here.
- [The Exponential of a Matrix and Its Image](the-exponential-of-a-matrix-and-its-image.html), for the properties of the exponential.
- [The Lie Algebra $\operatorname{Skew}_n\cong\mathfrak{so}(n)$](the-lie-algebra-skew-n-and-so-n.html), for the compact subalgebra of this algebra.
