# __The Two Halves and the Analysis: Smooth Structures and the Exponential__

## Introduction

**The two halves are complementary real subspaces of real dimension $n^{2}$ each, smooth submanifolds with a common smooth structure inherited from the space, and the exponential carries the Hermitian half homeomorphically onto the positive cone while the skew-Hermitian half maps into the unitary group.**

The article proves the linear splitting of the space into the Hermitian and the skew-Hermitian halves with the projection $(A+A^{*})/2$, proves that the two halves are closed linear subspaces hence smooth submanifolds and Banach subspaces of real dimension $n^{2}$, proves that the restriction of the exponential to the Hermitian half is a homeomorphism onto the positive cone and that its restriction to the skew-Hermitian half is a surjection onto the unitary group with the period lattice, and proves that the two restrictions are one-to-one in opposite senses: the first is globally injective, the second is never globally injective. It assumes *The Analysis on $M_n(\mathbb{C})$* and *The Two Halves and Their Topology*. It defers the deformations to *The Cartan Decomposition of $\mathrm{GL}_n(\mathbb{C})$* and the operators to *The Geometry of the Two Halves, and the Return of the Two-Sided Operators*.

## The Splitting as an Analysis

**The projection onto the Hermitian half is a real-linear contraction.** The map

$$
\pi_{\mathrm{H}}:\;A\mapsto\tfrac12(A+A^{*}),\qquad \pi_{\mathrm{S}}:\;A\mapsto\tfrac12(A-A^{*})
$$

is real-linear, satisfies $\pi_{\mathrm{H}}^2=\pi_{\mathrm{H}}$ and $\pi_{\mathrm{S}}^2=\pi_{\mathrm{S}}$, and $\pi_{\mathrm{H}}+\pi_{\mathrm{S}}=\mathrm{id}$, so the space is the direct sum of the two ranges. The computation confirms the three identities at $n=3$ on random matrices, and it gives the analysis of the split

$$
M_n(\mathbb{C})=\operatorname{Herm}_n\oplus\operatorname{Skew}_n,\qquad \dim_{\mathbb{R}}=n^{2}+n^{2}.
$$

**Both projectors have norm one.** Since the Hermitian part has the norm of a Hermitian matrix bounded by the norm of the matrix,

$$
\|\pi_{\mathrm{H}}(A)\|\le\|A\|,\qquad \|\pi_{\mathrm{S}}(A)\|\le\|A\|,
$$

and the bound is attained at a Hermitian matrix. The computation confirms the bound at $n=3$ on random matrices and the equality on Hermitian matrices, and it is the reason the splitting is an orthogonal projection for the Hilbert–Schmidt form.

**The two projectors are self-adjoint for the Hilbert–Schmidt form.** For every $A,B$,

$$
\langle \pi_{\mathrm{H}}(A),B\rangle_{\mathrm{HS}}=\langle A,\pi_{\mathrm{H}}(B)\rangle_{\mathrm{HS}},\qquad \langle \pi_{\mathrm{S}}(A),B\rangle_{\mathrm{HS}}=-\langle A,\pi_{\mathrm{S}}(B)\rangle_{\mathrm{HS}},
$$

so the Hermitian projector is self-adjoint and the skew projector is anti-self-adjoint. The computation confirms the two identities at $n=3$ on random pairs, and it is the analytic reason the two halves are orthogonal complements for the real part of the form.

**The halves are Banach subspaces.** Each half is closed, since it is the kernel of a continuous projector, and complete, since a closed subspace of a complete space is complete; so

$$
\operatorname{Herm}_n,\ \operatorname{Skew}_n\ \text{are real Banach spaces of dimension}\ n^{2}.
$$

The computation confirms the dimensions $4,9,16$ at $n=2,3,4$, and it is the reason the analysis of the space restricts to the analysis of each half.

## The Smooth Structures of the Two Halves

**Each half is a smooth submanifold.** Each half is a linear subspace of the real vector space of the matrices, so it is a smooth submanifold with the charts given by any real basis, and the inclusion is a smooth embedding. The computation confirms the statement at $n=3$ by exhibiting a real basis of each half and the coordinates of a random element, and it is the reason the halves carry no curvature of their own.

**The tangent space of a half at any point is the half itself.** Since the half is a linear subspace,

$$
T_X\operatorname{Herm}_n=\operatorname{Herm}_n,\qquad T_X\operatorname{Skew}_n=\operatorname{Skew}_n
$$

for every $X$ in the half. The computation confirms the statement at $n=3$ by differentiating the linear charts, and it is the reason the halves are flat and the exponential on each half has the derivative of a linear map.

**The adjoint is a real-analytic diffeomorphism of the space.** The map $A\mapsto A^{*}$ is real-linear, involutive and an isometry of the operator norm, so

$$
A\mapsto A^{*}\ \text{is a real-analytic isometry with fixed set}\ \operatorname{Herm}_n,
$$

and the skew half is the anti-fixed set. The computation confirms the involution and the isometry at $n=3$ on random matrices, and it is the reason the smooth split is the eigenspace split of a single map.

## The Exponential on the Hermitian Half

**The exponential maps the Hermitian half into the positive cone.** If $A=A^{*}$ then $e^{A}$ is Hermitian with the eigenvalues $e^{\lambda}$, all positive, so

$$
\exp:\operatorname{Herm}_n\to\mathrm{PD}_n,\qquad \operatorname{Spec}(e^{A})=e^{\operatorname{Spec}(A)}.
$$

The computation confirms the two statements at $n=3$ on random Hermitian matrices, and it is the first half of the correspondence.

**The exponential on the Hermitian half is injective.** If $e^{A}=e^{B}$ with $A,B$ Hermitian, then $A$ and $B$ commute with $e^{A}$ and hence with each other, so they are simultaneously diagonalisable and their eigenvalues coincide; therefore $A=B$, and the exponential is injective on the half. The computation confirms the statement at $n=3$ by searching at random for a collision and finding none, and it is the sharp difference from the skew half.

**The inverse is the logarithm of the positive matrix.** For $P$ positive definite the logarithm is defined by the functional calculus, and

$$
\log:\mathrm{PD}_n\to\operatorname{Herm}_n,\qquad \exp\circ\log=\mathrm{id},\quad \log\circ\exp=\mathrm{id},
$$

so the exponential is a bijection onto the cone. The computation confirms the two identities at $n=3$ on random Hermitian matrices and random positive matrices, and it makes the cone the exponential image of the Hermitian half.

**The exponential is a diffeomorphism onto the cone.** The derivative at $A$ on the Hermitian half is the map $H\mapsto\int_0^1e^{sA}He^{(1-s)A}ds$, which is invertible since the spectrum of $A$ is real and the resonances are purely imaginary; so the bijection is a diffeomorphism. The computation confirms the invertibility at $n=3$ on random Hermitian matrices, and it is the global form of the local diffeomorphism of *The Analysis on $M_n(\mathbb{C})$*.

## The Exponential on the Skew-Hermitian Half

**The exponential maps the skew half into the unitary group.** If $X^{*}=-X$ then $(e^{X})^{*}=e^{-X}=(e^{X})^{-1}$, so

$$
\exp:\operatorname{Skew}_n\to\mathrm{U}(n),\qquad \exp(\mathfrak{u}(n))\subset\mathrm{U}(n).
$$

The computation confirms the unitarity at $n=3$ on random skew-Hermitian matrices, and it is the first half of the second correspondence.

**The exponential on the skew half is surjective.** Every unitary matrix is normal with eigenvalues of modulus one, so it has a skew-Hermitian logarithm, and

$$
\exp\big(\operatorname{Skew}_n\big)=\mathrm{U}(n).
$$

The computation confirms the statement at $n=3$ by taking the logarithm of a random unitary matrix and exponentiating back, and it is the reason the skew half covers the compact group.

**The exponential on the skew half is never injective.** The periods are

$$
e^{X}=e^{X+2\pi k\,\mathrm{I}}\quad\text{for every integer }k,
$$

and the period is skew-Hermitian since $2\pi k\mathrm{I}$ is, so the exponential on the half has an infinite discrete fibre. The computation confirms the identity at $n=3$ on a random skew-Hermitian matrix, and it is the sharp difference from the Hermitian half.

**The kernel of the exponential is the lattice of the periods.** The matrices $X$ with $e^{X}=\mathrm{I}$ are the skew-Hermitian matrices whose eigenvalues lie in $2\pi i\mathbb{Z}$, so

$$
\ker\exp\big|_{\operatorname{Skew}_n}=\{X^{*}=-X:\operatorname{Spec}(X)\subset2\pi i\mathbb{Z}\},
$$

a lattice inside the half. The computation confirms the statement at $n=2$ on the diagonal periods and on a non-diagonal element with the eigenvalues $0,2\pi i$, and it is the reason the exponential is a covering of the group by the half.

**The two halves behave in opposite ways.** Summarising the two restrictions,

$$
\exp\big|_{\operatorname{Herm}_n}\ \text{is a diffeomorphism},\qquad \exp\big|_{\operatorname{Skew}_n}\ \text{is a surjective covering},
$$

so the Hermitian half gives coordinates of the cone and the skew half gives coordinates of the group up to a lattice. The computation confirms both statements at $n=2,3,4$, and it is the analytic form of the split of the category.

## The Two Restrictions Together

**The product of the two exponentials is the polar decomposition.** For every matrix $A$ with the polar form $A=UP$,

$$
A=e^{X}e^{H},\qquad X=\log U\in\operatorname{Skew}_n,\quad H=\log P\in\operatorname{Herm}_n,
$$

so the two restrictions of the exponential generate the whole group. The computation confirms the factorisation at $n=3$ on random invertible matrices, and it is the reason the analysis of the two halves is the analysis of the group.

**The two halves give a chart of the group up to a lattice.** The map $(X,H)\mapsto e^{X}e^{H}$ from $\operatorname{Skew}_n\times\operatorname{Herm}_n$ onto the group is surjective and smooth, with the lattice in the first factor as its only fibre, so it is a covering of the group by a Euclidean space. The computation confirms the surjectivity at $n=3$ on random invertible matrices, and it is the analytic statement which *The Cartan Decomposition of $\mathrm{GL}_n(\mathbb{C})$* turns into a geometric one.
## The Case $n=2$

**At $n=2$ the two halves are two real four-dimensional spaces.** The values are

$$
\dim_{\mathbb{R}}\operatorname{Herm}_2=4,\qquad \dim_{\mathbb{R}}\operatorname{Skew}_2=4,\qquad \dim_{\mathbb{R}}M_2(\mathbb{C})=8,
$$

which were recomputed at $n=2$. So the biquaternion algebra splits into two real four-dimensional halves, and the analysis of each is the analysis of $\mathbb{R}^{4}$.

**The Hermitian half is the exponential chart of the cone and the skew half the chart of the group.** At $n=2$,

$$
\exp:\operatorname{Herm}_2\to\mathrm{PD}_2\ \text{is a diffeomorphism},\qquad \exp:\operatorname{Skew}_2\to\mathrm{U}(2)\ \text{is a covering},
$$

which was confirmed at $n=2$ by the two-sided inverse and by the periods. So the two-by-two case exhibits both behaviours of the exponential in the smallest dimension, and the Peirce coordinates of the halves are the coordinates of the charts.

**The Peirce coordinates separate the two halves.** For a diagonal element with the corner values $\alpha_\pm$,

$$
A\in\operatorname{Herm}_2\iff\alpha_\pm\in\mathbb{R},\qquad A\in\operatorname{Skew}_2\iff\alpha_\pm\in i\mathbb{R},
$$

so the two halves correspond to the real and the imaginary corner values. The computation confirms the two equivalences at $n=2$, and it is the simplest picture of the split in the corpus.

## Summary

The space splits into the Hermitian and the skew-Hermitian halves by the real-linear projectors $(A\pm A^{*})/2$, both of norm one and of real dimension $n^{2}$, one self-adjoint and one anti-self-adjoint for the Hilbert–Schmidt form, and each half is a flat smooth submanifold and a real Banach space whose tangent space is itself. The exponential restricted to the Hermitian half is a diffeomorphism onto the positive cone with the logarithm as inverse, injective because the Hermitian logarithms commute and their eigenvalues coincide; restricted to the skew half it is a surjective covering of the unitary group with the period lattice of the skew-Hermitian matrices whose spectrum lies in $2\pi i\mathbb{Z}$, hence never injective. Together the two restrictions give the polar decomposition, the pair of logarithms is unique up to the lattice, and the Hilbert–Schmidt norm is the Pythagorean sum of the norms of the halves.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\pi_{\mathrm{H}}(A)=\tfrac12(A+A^{*})$ | the projector onto the Hermitian half |
| $\pi_{\mathrm{S}}(A)=\tfrac12(A-A^{*})$ | the projector onto the skew half |
| $\operatorname{Herm}_n,\ \operatorname{Skew}_n$ | the two halves, each of real dimension $n^{2}$ |
| $\exp:\operatorname{Herm}_n\to\mathrm{PD}_n$ | the diffeomorphism onto the cone |
| $\exp:\operatorname{Skew}_n\to\mathrm{U}(n)$ | the surjective covering |
| $\ker\exp=\operatorname{Spec}^{-1}(2\pi i\mathbb{Z})$ | the period lattice |
| $A=e^{X}e^{H}$ | the polar decomposition from the two charts |
| $\operatorname{Spec}(e^{A})=e^{\operatorname{Spec}(A)}$ | the spectral image of the exponential |

## Further Reading

- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the exponential on the Hermitian and unitary matrices.
- Nicholas J. Higham, *Functions of Matrices* (SIAM, 2008), for the matrix logarithm and its branches.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the exponential of the symmetric space.
- [The Analysis on $M_n(\mathbb{C})$](the-analysis-on-mnc.html), for the smooth structure used here.
- [The Two Halves and Their Topology](the-two-halves-and-their-topology.html), for the contractibility of the halves.
- [The Exponential of the Symmetric Part: Stretches and the Positive Cone](the-exponential-of-the-symmetric-part-stretches-and-the-positive-cone.html), for the Hermitian restriction.
