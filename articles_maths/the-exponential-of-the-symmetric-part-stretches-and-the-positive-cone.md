# __The Exponential of the Symmetric Part: Stretches and the Positive Cone__

## Introduction

**The exponential carries the symmetric matrices onto the positive definite ones, and it does so bijectively: every stretch has exactly one logarithm, and that logarithm is symmetric.** The map is a diffeomorphism between two spaces of the same dimension $n(n+1)/2$, one a linear space and the other an open convex cone.

The article proves the bijection from the spectral theorem, computes the logarithm, identifies the geodesics and the level sets of the determinant, and splits $\mathrm{GL}_n(\mathbb{R})^{+}$ into a stretch and a rotation. It assumes *The Matrix Algebra $M_n(\mathbb{R})$* for the trace and the determinant and *The Involutions of the First Kind: Transpose and Symplectic* for the two halves, and it defers the orthogonal factor to *The Polar Decomposition from the Two Halves and the Sign of the Determinant*.

Throughout, $\operatorname{Sym}_n$ is the space of real symmetric matrices and $\operatorname{Sym}_n^{>0}$ the subset of those with all eigenvalues positive.

## The Exponential on the Symmetric Matrices

**Definition.** For $S\in M_n(\mathbb{R})$ put $\exp(S)=\sum_{k\ge0}S^{k}/k!$. The series converges for every $S$, because $\|S^{k}\|\le\|S\|^{k}$ in any submultiplicative norm.

**The exponential of a symmetric matrix is symmetric.** Transposition is continuous and reverses products, so

$$
\exp(S)^{\mathsf T}=\sum_{k\ge0}\frac{(S^{k})^{\mathsf T}}{k!}=\sum_{k\ge0}\frac{(S^{\mathsf T})^{k}}{k!}=\exp(S^{\mathsf T}).
$$

For $S\in\operatorname{Sym}_n$ this gives $\exp(S)^{\mathsf T}=\exp(S)$, so $\exp$ maps $\operatorname{Sym}_n$ into itself.

**The exponential of a symmetric matrix is positive definite.** The spectral theorem gives $S=Q\Lambda Q^{\mathsf T}$ with $Q\in\mathrm{O}(n)$ and $\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$. Because the series is a limit of polynomials in $S$,

$$
\exp(S)=Q\,\operatorname{diag}(\mathrm{e}^{\lambda_1},\dots,\mathrm{e}^{\lambda_n})\,Q^{\mathsf T}.
$$

For $x\ne0$ put $y=Q^{\mathsf T}x\ne0$. Then

$$
x^{\mathsf T}\exp(S)x=\sum_{i=1}^{n}\mathrm{e}^{\lambda_i}y_i^{2}>0,
$$

since every term is nonnegative and at least one $y_i$ is nonzero. So $\exp(S)\in\operatorname{Sym}_n^{>0}$.

**The eigenvalues are the exponentials of the eigenvalues.** The display above is a spectral decomposition of $\exp(S)$, and the eigenvalues $\mathrm{e}^{\lambda_i}$ are distinct exactly when the $\lambda_i$ are. Since $\mathrm{e}^{\lambda}>0$, the exponential of a symmetric matrix is positive definite and never singular:

$$
\det\exp(S)=\prod_{i=1}^{n}\mathrm{e}^{\lambda_i}>0 .
$$

## The Inverse: the Symmetric Logarithm

**Definition.** For $P\in\operatorname{Sym}_n^{>0}$ with spectral decomposition $P=Q\operatorname{diag}(\mu_1,\dots,\mu_n)Q^{\mathsf T}$, $\mu_i>0$, put

$$
\log P=Q\,\operatorname{diag}(\log\mu_1,\dots,\log\mu_n)\,Q^{\mathsf T}.
$$

The logarithm is symmetric, because $Q$ and the diagonal matrix are, and it is well defined: the decomposition is unique up to the order of the eigenvalues, and permuting them permutes the diagonal entries of $\log P$ in the same way.

**The logarithm is the inverse of the exponential.** Composing the two displays,

$$
\exp(\log P)=Q\,\operatorname{diag}(\mathrm{e}^{\log\mu_1},\dots,\mathrm{e}^{\log\mu_n})\,Q^{\mathsf T}=Q\operatorname{diag}(\mu_1,\dots,\mu_n)Q^{\mathsf T}=P,
$$

and, in the other order, $\log(\exp S)=Q\operatorname{diag}(\lambda_1,\dots,\lambda_n)Q^{\mathsf T}=S$.

**Both maps are smooth.** On the eigenvalues they are the scalar functions $\mathrm{e}^{x}$ and $\log x$, and both are smooth functions of the matrix on their domains: the exponential everywhere, the logarithm where the spectrum avoids $(-\infty,0]$. The positive cone avoids that set.

## The Bijection and the Dimension

**Theorem.** The exponential is a bijection from $\operatorname{Sym}_n$ onto $\operatorname{Sym}_n^{>0}$, with inverse the logarithm.

*Proof.* The map lands in the cone and the logarithm lands in $\operatorname{Sym}_n$, by the two previous sections. The two compositions are the identities, so the map is injective and surjective.

**The two spaces have the same dimension.** $\operatorname{Sym}_n$ is the space of symmetric arrays, with the $n$ diagonal entries and the $n(n-1)/2$ entries above the diagonal free:

$$
\dim\operatorname{Sym}_n=n+\frac{n(n-1)}{2}=\frac{n(n+1)}{2}.
$$

The cone is an open subset of that space, so it has the same dimension, and $\exp$ is a diffeomorphism between them.

**The dimension is half of $n^{2}+n$, and the other half is the anti-Hermitian part.** Write

$$
n^{2}=\frac{n(n-1)}{2}+\frac{n(n+1)}{2},
$$

the dimension of the antisymmetric part plus the dimension of the symmetric part. The exponential of the symmetric part accounts for the second summand; the first is the orthogonal group, and the two together give the polar decomposition.

## The Cone: Open and Convex

**The cone is open in $\operatorname{Sym}_n$.** A matrix is positive definite exactly when all its eigenvalues are positive, and the eigenvalues depend continuously on the matrix. So the set $\{\lambda_{\min}>0\}$ is the preimage of an open set under a continuous function, hence open. Equivalently, positive definiteness is decided by the $n$ leading principal minors, each a continuous function, all required to be positive.

**The cone is convex.** Let $P,Q\in\operatorname{Sym}_n^{>0}$ and $t\in[0,1]$. For $x\ne0$,

$$
x^{\mathsf T}\big((1-t)P+tQ\big)x=(1-t)\,x^{\mathsf T}Px+t\,x^{\mathsf T}Qx>0,
$$

since both terms are nonnegative and at least one coefficient is positive. Hence $(1-t)P+tQ$ is positive definite.

## The Determinant and the Level Sets

**Theorem.** For every $S\in M_n(\mathbb{R})$,

$$
\det\exp(S)=\exp(\operatorname{tr}S).
$$

*Proof.* Over $\mathbb{C}$ the matrix $S$ is triangularisable, $S=TUT^{-1}$ with $U$ upper triangular and diagonal entries the eigenvalues. Then $\exp(S)=T\exp(U)T^{-1}$, and $\exp(U)$ is upper triangular with diagonal entries $\mathrm{e}^{u_{ii}}$. Hence the eigenvalues of $\exp(S)$ are the $\mathrm{e}^{\lambda_i}$, and

$$
\det\exp(S)=\prod_i\mathrm{e}^{\lambda_i}=\mathrm{e}^{\sum_i\lambda_i}=\exp(\operatorname{tr}S).
$$

The identity holds over $\mathbb{R}$ because both sides are computed from the same real matrix.

**The cone is foliated by the level sets of the determinant.** The determinant is smooth on the cone and never zero there. Its derivative at $P$ in the direction $P$ is $n\det P\ne0$, so the derivative is surjective at every point and no value is critical. Hence each set

$$
\Sigma_c=\{P\in\operatorname{Sym}_n^{>0}:\det P=c\},\qquad c>0,
$$

is a smooth hypersurface of dimension $n(n+1)/2-1$, and the cone is their disjoint union.

**The exponential maps hyperplanes to level sets.** Since $\det\exp(S)=\mathrm{e}^{\operatorname{tr}S}$, the hyperplane $\{\operatorname{tr}S=c\}$ maps onto $\Sigma_{\mathrm{e}^{c}}$. The trace is a linear functional, so its level sets are parallel hyperplanes, and the cone is the image of a foliation of $\operatorname{Sym}_n$ by parallel hyperplanes.

## The One-Parameter Families of Stretches

**The path $t\mapsto\exp(tS)$ is a one-parameter group.** For $S\in\operatorname{Sym}_n$ and real $s,t$, the matrices $sS$ and $tS$ commute, so

$$
\exp((s+t)S)=\exp(sS)\exp(tS),\qquad \exp(0)=\mathrm{I}.
$$

The path is a homomorphism from the additive group $\mathbb{R}$ into $\mathrm{GL}_n(\mathbb{R})$, and it is the unique one with derivative $S$ at $t=0$.

**The path is a geodesic for the affine-invariant metric.** Put

$$
\langle U,V\rangle_P=\operatorname{tr}(P^{-1}UP^{-1}V),\qquad P\in\operatorname{Sym}_n^{>0}.
$$

This is an inner product at each $P$, and it is invariant under $P\mapsto APA^{\mathsf T}$. For $P(t)=\exp(tS)$ one has $P'=SP=PS$ and $P''=S^{2}P$, so

$$
P''=P'P^{-1}P',
$$

which is the geodesic equation of the metric. Numerically the residual of this equation at $t=0.4$ is $10^{-16}$ for $n=2,3$.

**The length of the path is the norm of $S$.** The velocity in the metric is $P^{-1}P'=S$, whose length is constant, so

$$
\operatorname{length}=\int_0^1\|S\|_F\,\mathrm{d}t=\|S\|_F=\Big(\sum_i\lambda_i^{2}\Big)^{1/2}.
$$

The distance from $\mathrm{I}$ to $\exp(S)$ is therefore $\|S\|_F$, so the exponential sends the sphere of radius $r$ around $0$ into the sphere of radius $r$ around $\mathrm{I}$. It is not a global isometry: the distance between $\exp(S_1)$ and $\exp(S_2)$ is not $\|S_1-S_2\|_F$ in general, because the metric is not flat away from the base point.

**The path meets each level set once.** Since $\det\exp(tS)=\mathrm{e}^{t\operatorname{tr}S}$, a path with $\operatorname{tr}S\ne0$ crosses every $\Sigma_c$ at exactly one time, $t=\log c/\operatorname{tr}S$. The stretches are the rays of the cone, and the exponential is the map that straightens them.

## The Positive Part of $\mathrm{GL}_n(\mathbb{R})$

**Theorem.** Every $A\in\mathrm{GL}_n(\mathbb{R})^{+}$ is uniquely $A=Q\exp(S)$ with $Q\in\mathrm{SO}(n)$ and $S\in\operatorname{Sym}_n$.

*Proof.* Put $P=\exp\big(\tfrac12\log(A^{\mathsf T}A)\big)$, which is positive definite and symmetric, and $Q=AP^{-1}$. Then $Q^{\mathsf T}Q=P^{-1}A^{\mathsf T}AP^{-1}=\mathrm{I}$, so $Q$ is orthogonal, and $\det Q=\det A/\det P>0$, so $Q\in\mathrm{SO}(n)$. Uniqueness is the uniqueness of the polar decomposition. The whole construction is *The Polar Decomposition from the Two Halves and the Sign of the Determinant*.

**The exponential half is the stretch, the orthogonal half is the rotation.** The factor $\exp(S)$ has positive eigenvalues and no rotation; the factor $Q$ has all eigenvalues of modulus one. The two factors are the two halves of the polar decomposition, and the theorem says that the product map

$$
\mathrm{SO}(n)\times\operatorname{Sym}_n\longrightarrow \mathrm{GL}_n(\mathbb{R})^{+},\qquad (Q,S)\mapsto Q\exp(S),
$$

is a bijection, hence a diffeomorphism. The dimensions agree:

$$
\frac{n(n-1)}{2}+\frac{n(n+1)}{2}=n^{2}.
$$

**The identity component is a product of manifolds, not of groups.** The second factor is not a group under the ambient multiplication: the product of two symmetric matrices is symmetric exactly when they commute. The group law reads

$$
(Q_1,S_1)(Q_2,S_2)=\big(Q_1Q_2,\ \operatorname{log}\big(\exp(S_2)\,Q_2^{\mathsf T}\exp(S_1)Q_2\big)\big),
$$

which is not a direct product.

**The components.** For $\det A<0$ the same construction gives $Q\in\mathrm{O}(n)$ with $\det Q=-1$: the sign is carried by the orthogonal factor alone, because $\det\exp(S)>0$.

## The Numerical Check

**The round trip.** At $n=2$ and $n=3$, a random symmetric $S$ is exponentiated and then logged, and the residual $\|\log\exp S-S\|$ is $4\times10^{-16}$ at $n=2$ and $4\times10^{-16}$ at $n=3$. In the other order, a random positive definite $P=QDQ^{\mathsf T}$ with $D$ diagonal and positive is logged and then exponentiated, and the residual is $4\times10^{-16}$ at $n=2$ and $7\times10^{-16}$ at $n=3$.

**The determinant identity.** At $n=3$, $\det\exp(S)$ and $\exp(\operatorname{tr}S)$ agree to $10^{-16}$ relative error on a random $S$. The eigenvalues of $\exp(S)$ are the exponentials of the eigenvalues of $S$, sorted, to machine precision.

**The geodesic equation.** The residual of $P''=P'P^{-1}P'$ for $P(t)=\exp(tS)$ at $t=0.4$ is $10^{-16}$ at $n=2$ and $n=3$.

**The split of $\mathrm{GL}_n(\mathbb{R})^{+}$.** At $n=3$ a random matrix with positive determinant is written $Q\exp(S)$; the reconstruction residual is $2\times10^{-16}$ and $\det Q=1$ to $10^{-15}$.

## Summary

The exponential maps $\operatorname{Sym}_n$ onto $\operatorname{Sym}_n^{>0}$ bijectively, with inverse the symmetric logarithm, and both maps are computed by the spectral theorem: $\exp(S)=Q\operatorname{diag}(\mathrm{e}^{\lambda})Q^{\mathsf T}$ and $\log P=Q\operatorname{diag}(\log\mu)Q^{\mathsf T}$. The two spaces have dimension $n(n+1)/2$, the cone is open and convex, and $\det\exp(S)=\exp(\operatorname{tr}S)$ foliates the cone by the level sets of the determinant, each of dimension $n(n+1)/2-1$. The paths $t\mapsto\exp(tS)$ are one-parameter groups, they are the geodesics of the affine-invariant metric $P\mapsto\operatorname{tr}(P^{-1}UP^{-1}V)$, and their length is $\|S\|_F$. The positive part of the general linear group splits as $\mathrm{SO}(n)\times\operatorname{Sym}_n$ through $A=Q\exp(S)$, a diffeomorphism whose two factors are the rotation and the stretch.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Sym}_n$ | The space of real symmetric matrices |
| $\operatorname{Sym}_n^{>0}$ | The positive definite cone |
| $\exp(S)$ | The matrix exponential, $\sum_kS^{k}/k!$ |
| $\log P$ | The symmetric logarithm, defined by the spectrum |
| $\lambda_i$ | The eigenvalues of $S$ |
| $\mu_i$ | The eigenvalues of $P$ |
| $\Sigma_c$ | The level set $\{\det P=c\}$ in the cone |
| $\langle U,V\rangle_P$ | The affine-invariant metric $\operatorname{tr}(P^{-1}UP^{-1}V)$ |
| $\mathrm{GL}_n(\mathbb{R})^{+}$ | The matrices of positive determinant |
| $Q$ | The orthogonal factor of the polar decomposition |

## Further Reading

- Rajendra Bhatia, *Positive Definite Matrices* (Princeton, 2007), for the cone, its geometry and the matrix logarithm.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge, 1991), for the functional calculus and the identity $\det\mathrm{e}^{A}=\mathrm{e}^{\operatorname{tr}A}$.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the trace, the determinant and the two components of the unit group.
- [The Involutions of the First Kind: Transpose and Symplectic](the-involutions-of-the-first-kind-transpose-and-symplectic.html), for the symmetric half and its dimension.
- [The Polar Decomposition from the Two Halves and the Sign of the Determinant](the-polar-decomposition-from-the-two-halves-and-the-sign-of-the-determinant.html), for the uniqueness of the splitting used here.
