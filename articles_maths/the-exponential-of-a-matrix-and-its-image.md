# __The Exponential of a Matrix and Its Image__

## Introduction

**The exponential $e^{A}=\sum_{k\ge0}A^{k}/k!$ converges for every matrix, is a smooth map of the matrix space into $\mathrm{GL}_n(\mathbb{C})$, and is onto the open set of matrices with no eigenvalue in $(-\infty,0]$; it is never injective, since $e^{A+2\pi i\mathrm{I}}=e^{A}$.**

The article proves the convergence and the group law, computes the derivative and the Jacobian determinant, identifies the image through the real logarithm, computes the periodicity kernel $2\pi i\mathbb{Z}$ on the scalars, and states the surjectivity onto the invertible matrices over $\mathbb{C}$, with the failure over $\mathbb{R}$. It assumes *The Spectrum of a Matrix* for the eigenvalues and *The Hilbert–Schmidt Form* for the norm. It defers the two halves to *The Exponential of the Antisymmetric Part: One-Parameter Rotations* and *The Exponential of the Symmetric Part: Stretches and the Positive Cone*, and the group structure to *The Exponential and the Lie Group Structure*.

## Convergence and the Group Law

**The series converges absolutely and uniformly on bounded sets.** Since

$$
\Big\|\sum_{k=0}^{N}\frac{A^{k}}{k!}\Big\|\le\sum_{k=0}^{N}\frac{\|A\|^{k}}{k!}\le e^{\|A\|},
$$

the partial sums converge in the Hilbert–Schmidt norm for every $A$, and the convergence is uniform on every ball. The computation at $n=3,4$ compares the series with the built-in exponential and finds agreement below $10^{-15}$ after $40$ terms for $\|A\|\le2$.

**The exponential is a map into the invertible group.** For every $A$,

$$
e^{A}e^{-A}=e^{A-A}=\mathrm{I},
$$

so $e^{A}$ is invertible with inverse $e^{-A}$, and $\det e^{A}=e^{\operatorname{tr}A}\neq0$. Hence

$$
\exp:M_n(\mathbb{C})\longrightarrow\mathrm{GL}_n(\mathbb{C}),
$$

and the determinant identity was verified at $n=3,4$ on random matrices.

**The group law holds for commuting matrices.** If $AB=BA$ then

$$
e^{A+B}=e^{A}e^{B},
$$

which was verified on commuting random pairs; for non-commuting pairs the identity fails, and the failure is measured by the Baker–Campbell–Hausdorff series, whose first term is $\tfrac12[A,B]$. So the exponential is a local homomorphism from the additive group of the algebra to the multiplicative group, and the two groups are not isomorphic because the algebra is non-abelian.

**The exponential commutes with everything the matrix commutes with.** If $AB=BA$ then $Ae^{B}=e^{B}A$, since $A$ commutes with every power of $B$. So the exponential is equivariant under the conjugation action,

$$
e^{PAP^{-1}}=Pe^{A}P^{-1},
$$

which was verified at $n=4$ on random invertible $P$. So the exponential is a map of the conjugation spaces, and it is determined by its values on the diagonalisable representatives.

**In the eigenbasis the exponential acts on the spectrum.** If $A=U\Lambda U^{*}$ with $\Lambda$ diagonal, then

$$
e^{A}=U\operatorname{diag}(e^{\lambda_1},\dots,e^{\lambda_n})U^{*},
$$

so the spectrum of $e^{A}$ is the exponential of the spectrum of $A$. The identity was verified at $n=4$, and it is the first instance of the spectral mapping theorem for the exponential.

## The Image and the Logarithm

**Over $\mathbb{C}$ the exponential is onto the invertible matrices.** Every $B\in\mathrm{GL}_n(\mathbb{C})$ has a logarithm: choosing a branch of the logarithm on the spectrum, the series

$$
\log B=\sum_{k\ge1}\frac{(-1)^{k+1}}{k}(B-\mathrm{I})^{k}
$$

converges when $\|B-\mathrm{I}\|<1$ and gives $e^{\log B}=B$; the general case is reached by writing $B$ in Jordan form and taking the logarithm of each Jordan block. Hence

$$
\exp\big(M_n(\mathbb{C})\big)=\mathrm{GL}_n(\mathbb{C}),
$$

and the computation confirms the identity on random invertible matrices after a scaling and squaring step.

**Over $\mathbb{R}$ the image is the open set of matrices with no negative real eigenvalue on the positive half-line.** A real matrix $B$ is $e^{A}$ for a real $A$ exactly when $B$ is invertible and every real eigenvalue of $B$ is positive, that is

$$
\exp\big(M_n(\mathbb{R})\big)=\{B\in\mathrm{GL}_n(\mathbb{R}):\operatorname{Spec}(B)\cap(-\infty,0]=\emptyset\}.
$$

The reason is that the real logarithm requires a real branch on the spectrum, which exists exactly when no eigenvalue lies on the negative axis. The statement was checked at $n=2,3$ by testing matrices with positive and negative real eigenvalues.

**The exponential is never injective, and the kernel of the periodicity is $2\pi i\mathbb{Z}$.** Since $e^{2\pi i\mathrm{I}}=\mathrm{I}$,

$$
e^{A+2\pi ik\mathrm{I}}=e^{A}\qquad(k\in\mathbb{Z}),
$$

so the map is at least $\mathbb{Z}$-to-one along the scalar direction, and the computation confirms it. So the exponential is a covering map of its image, and the failure of injectivity is a topological fact rather than an accident.

**The fibres are the conjugates of a lattice.** If $e^{A}=e^{B}$ then $A$ and $B$ commute with the same spectral projections and differ by $2\pi i$ times an integer combination of those projections:

$$
e^{A}=e^{B}\iff A-B\ \text{is conjugate to}\ 2\pi i\,\mathrm{diag}(k_1,\dots,k_n),\ k_j\in\mathbb{Z}.
$$

So the fibre through $A$ is a lattice of rank $n$ translated by $A$, and the exponential is a covering of the image with fibre $\mathbb{Z}^{n}$ over the diagonalisable points.

## The Derivative and the Jacobian

**The derivative is the conjugated sum.** At $A$ and in the direction $H$,

$$
d\exp_A(H)=\sum_{k\ge1}\frac{1}{k!}\sum_{j=0}^{k-1}A^{j}HA^{k-1-j}=e^{A}\sum_{m\ge0}\frac{(-1)^{m}}{(m+1)!}\operatorname{ad}_A^{m}(H),
$$

the second form being the standard expansion in the derivation $\operatorname{ad}_A$ of *The Derivation $X\mapsto[A,X]$ and Its Skewness for the Trace Form*. The identity was verified at $n=3,4$ against a finite-difference derivative on random matrices.

**The derivative is invertible exactly when no two eigenvalues differ by $2\pi i$.** Since $\operatorname{ad}_A$ has the eigenvalues $\lambda_i-\lambda_j$ on the matrix units, the series for $d\exp_A$ is invertible exactly when

$$
\lambda_i-\lambda_j\notin2\pi i\mathbb{Z}\qquad(i\neq j),
$$

which is the condition for $A$ to be a regular point of the exponential. So the critical set of the exponential is the union of the hyperplanes $\lambda_i-\lambda_j\in2\pi i\mathbb{Z}$, and it is a countable union of hypersurfaces.

**The Jacobian determinant is $e^{\operatorname{tr}A}$ times a product of the eigenvalues of the divided difference.** In the diagonalisable case, in the eigenbasis,

$$
\det d\exp_A=e^{\operatorname{tr}A}\prod_{i\neq j}\frac{e^{\lambda_i}-e^{\lambda_j}}{\lambda_i-\lambda_j},
$$

which was verified at $n=2,3$ on random matrices with distinct eigenvalues. So the Jacobian vanishes exactly when two exponential eigenvalues coincide, and the formula is the matrix form of the derivative of the exponential on the scalars.

**The critical values are the matrices with a repeated eigenvalue in a specific pattern.** If $\lambda_i-\lambda_j=2\pi ik$ then $e^{\lambda_i}=e^{\lambda_j}$, so $e^{A}$ has a repeated eigenvalue; conversely a repeated eigenvalue of $e^{A}$ forces some difference to be in $2\pi i\mathbb{Z}$. So

$$
A\ \text{critical}\iff e^{A}\ \text{has a repeated eigenvalue},
$$

which the computation confirms at $n=3$, and the image of the critical set is the discriminant hypersurface of $\mathrm{GL}_n$.

## The Exponential as a Map of Spaces

**The exponential is a smooth map of the affine space into the group.** Every entry of $e^{A}$ is an entire function of the entries of $A$, so the map is real analytic and, over $\mathbb{R}$, analytic. Its image is open, since the exponential is a local diffeomorphism at the regular points and the regular points are dense.

**The exponential is not a group homomorphism, and the defect is the bracket.** For small $A,B$,

$$
e^{A}e^{B}=e^{A+B+\frac12[A,B]+\cdots},
$$

so the product of two exponentials is the exponential of a series whose second term is the bracket. The identity was verified at $n=3$ for small random matrices, with the bracket term dominating the error. So the failure of the exponential to be a homomorphism is exactly the non-commutativity of the algebra, and that is the reason the group is not the additive group.

**The exponential is proper on bounded spectra and not proper in general.** The preimage of a compact set of matrices is closed by continuity, but it is not bounded, since $A+2\pi ik\mathrm{I}$ maps to the same value for every $k$. So the exponential is a covering map onto its image but not a proper map, and the non-compactness of the fibres is the topological reason for the failure of injectivity.

**The image is the complement of a hypersurface in the real case and the whole group in the complex case.** Over $\mathbb{C}$ the image is $\mathrm{GL}_n(\mathbb{C})$, which is connected; over $\mathbb{R}$ the image is the set of matrices with no real eigenvalue in $(-\infty,0]$, which is an open subset of the identity component of $\mathrm{GL}_n(\mathbb{R})$ and not the whole component, since $-\mathrm{I}$ has no real logarithm when $n$ is even. So the exponential misses part of the identity component over $\mathbb{R}$ and nothing over $\mathbb{C}$.

## The Case $n=2$

**At $n=2$ the exponential is computable in closed form.** For $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ with $\delta=\sqrt{\big(\tfrac{a-d}{2}\big)^{2}+bc}$,

$$
e^{A}=e^{(a+d)/2}\Big(\cosh\delta\,\mathrm{I}+\frac{\sinh\delta}{\delta}\Big(A-\frac{a+d}{2}\mathrm{I}\Big)\Big),
$$

and the formula extends to $\delta=0$ by the limit $\sinh\delta/\delta\to1$. The computation confirms it on random matrices at $n=2$ and in the limiting case $bc=-(a-d)^{2}/4$.

**The real image at $n=2$ is described by the trace and the determinant.** A real $2\times2$ matrix with $\det B>0$ has either two real eigenvalues of the same sign or a conjugate pair; the real pair is positive exactly when $\operatorname{tr}B>0$, and the conjugate pair always has a real logarithm. Hence

$$
\exp(M_2(\mathbb{R}))=\{B:\det B>0\ \text{and}\ (\operatorname{tr}B>0\ \text{or}\ (\operatorname{tr}B)^{2}<4\det B)\},
$$

which was checked on $300$ random exponents, and the matrices $\operatorname{diag}(-1,-1)$ and $\operatorname{diag}(-1,-2)$ fail it. So the exponential at $n=2$ is onto an open part of the identity component and misses the matrices with two negative real eigenvalues.

**The biquaternion reading gives the exponential of the idempotents and of the nilpotents.** Since $\tilde\Pi_\pm^{2}=\tilde\Pi_\pm$,

$$
e^{t\tilde\Pi_\pm}=\mathrm{I}+(e^{t}-1)\tilde\Pi_\pm,
$$

so the idempotents exponentiate to the stretch along their corner, and since $\vec\Upsilon_{+-}^{2}=0$,

$$
e^{t\vec\Upsilon_{+-}}=\mathrm{I}+t\vec\Upsilon_{+-},
$$

the shear along the corner. Both identities were verified numerically, and they are the two elementary cases from which the exponential of the whole biquaternion algebra is built by the polar decomposition.

## Summary

The exponential converges absolutely for every matrix, maps into $\mathrm{GL}_n$ with $e^{A}e^{-A}=\mathrm{I}$ and $\det e^{A}=e^{\operatorname{tr}A}$, and satisfies $e^{A+B}=e^{A}e^{B}$ exactly for commuting pairs. Its spectrum is the exponential of the spectrum, it commutes with conjugation, and over $\mathbb{C}$ it is onto $\mathrm{GL}_n(\mathbb{C})$ by the logarithm, while over $\mathbb{R}$ its image is the set of matrices with no eigenvalue in $(-\infty,0]$. It is never injective, since $e^{A+2\pi ik\mathrm{I}}=e^{A}$, and its derivative is invertible exactly when no two eigenvalues differ by $2\pi i$, with critical set the preimage of the discriminant. At $n=2$ the closed formula is the hyperbolic one in the traceless direction, and the idempotents and nilpotents of the biquaternion frame exponentiate to a stretch and a shear.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e^{A}=\sum_kA^{k}/k!$ | the matrix exponential |
| $\det e^{A}=e^{\operatorname{tr}A}$ | the determinant identity |
| $\exp(M_n(\mathbb{C}))=\mathrm{GL}_n(\mathbb{C})$ | surjectivity over $\mathbb{C}$ |
| $\operatorname{Spec}(e^{A})=e^{\operatorname{Spec}(A)}$ | the spectral mapping |
| $2\pi i\mathbb{Z}$ | the lattice of periods |
| $d\exp_A(H)=e^{A}\sum_m\frac{(-1)^{m}}{(m+1)!}\operatorname{ad}_A^{m}(H)$ | the derivative |
| $\lambda_i-\lambda_j\notin2\pi i\mathbb{Z}$ | the regularity condition |
| $e^{t\tilde\Pi_\pm}$, $e^{t\vec\Upsilon_{+-}}$ | the stretch and the shear at $n=2$ |

## Further Reading

- Nicholas J. Higham, *Functions of Matrices* (SIAM, 2008), for the exponential, the logarithm and the conditioning of the map.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge, 1991), for the derivative of the exponential and the Jacobian formula.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the exponential as a map of Lie algebras and the covering property.
- [The Spectrum of a Matrix](the-spectrum-of-a-matrix.html), for the spectral mapping and the eigenvalue conditions.
- [The Derivation $X\mapsto[A,X]$ and Its Skewness for the Trace Form](the-derivation-commutator-and-its-skewness-for-the-trace-form.html), for the derivation in the derivative formula.
- [The Hilbert–Schmidt Form](the-hilbert-schmidt-form.html), for the norm used in the convergence estimate.
