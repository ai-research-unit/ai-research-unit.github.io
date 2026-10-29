# __$M_2(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix__

## Introduction

Every invertible complex matrix is the product of a positive Hermitian matrix and a $*$-unitary one, and the product is unique. For a biquaternion matrix the two factors carry the two pieces of the polar decomposition of the element: the positive factor is the boost, the $*$-unitary factor is the phase times the rotor.

This article develops the matrix polar decomposition, its refinement by the determinant, its behaviour on the singular matrices, and the singular value decomposition. It is the matrix form of *The Polar Decomposition of a N-Regular Biquaternion*, §*The Matrix Picture*, and of *The Polar Decomposition of a N-Degenerate Biquaternion*, §*The Matrix Picture*.

**Conventions.** The algebra and the model are those of *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. The norm is $N=\det M$. A matrix is **positive** when it is Hermitian with non-negative eigenvalues, and **positive definite** when the eigenvalues are positive. The $*$-unitary group is $U(2)$ and the special $*$-unitary group is $SU(2)$.

**Boundaries.** The polar decomposition of the element is *The Polar Decomposition of a Biquaternion*, of the regular element *The Polar Decomposition of a N-Regular Biquaternion*, and of the degenerate element *The Polar Decomposition of a N-Degenerate Biquaternion*; the sandwich action of the factors is *The Sandwich in the $M_2(\mathbb{C})$ Model*; the groups are *$M_2(\mathbb{C})$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant*.

## The Matrix Polar Decomposition

**Theorem.** Every $M\in M_2(\mathbb{C})$ has a factorisation

$$
M=PV,
$$

with $P$ positive semidefinite and $V$ a partial isometry. When $M$ is invertible, $P$ is positive definite, $V$ is $*$-unitary, and the factorisation is unique:

$$
P=(MM^{\dagger})^{1/2},\qquad V=P^{-1}M.
$$

*Proof.* The matrix $MM^{\dagger}$ is Hermitian positive semidefinite, so it has a unique positive semidefinite square root $P$. If $M$ is invertible, $P$ is invertible and $V=P^{-1}M$ satisfies

$$
V^{\dagger}V=M^{\dagger}P^{-2}M=M^{\dagger}(MM^{\dagger})^{-1}M=\mathrm I_2,
$$

so $V$ is $*$-unitary. For uniqueness, suppose $M=PV=P'V'$ with $P,P'$ positive definite and $V,V'$ $*$-unitary. Then $MM^{\dagger}=P^2=P'^2$, and the uniqueness of the positive square root gives $P=P'$, hence $V=V'$.

**The diffeomorphism.** The map

$$
Herm^{>0}\times U(2)\longrightarrow GL_2(\mathbb{C}),\qquad
(P,V)\longmapsto PV,
$$

is a diffeomorphism. The inverse is $M\mapsto((MM^{\dagger})^{1/2},(MM^{\dagger})^{-1/2}M)$. The two factors have real dimensions four and four, and the product accounts for the eight real dimensions of $GL_2$.

**The determinant split.** Taking determinants,

$$
\det M=\det P\det V.
$$

The first factor is positive real and the second has modulus one, so the decomposition splits the nonzero complex determinant into its modulus and its phase:

$$
\det P=|\det M|,\qquad |\det V|=1.
$$

The polar decomposition is therefore the matrix form of the polar form of a nonzero complex number, applied to the determinant.

## The Closed Form of the Positive Factor

**The square root by Cayley–Hamilton.** For a Hermitian $2\times2$ matrix $Y$ with non-negative eigenvalues, not both zero, the positive square root is the degree-one polynomial

$$
Y^{1/2}=\frac{Y+\sqrt{\det Y}\,\mathrm I_2}
{\sqrt{\operatorname{Tr}Y+2\sqrt{\det Y}}},
$$

because $Y$ satisfies $Y^2-(\operatorname{Tr}Y)Y+(\det Y)\mathrm I_2=0$ and the scalar function is applied to the two eigenvalues. For $Y=MM^{\dagger}$ this gives the positive factor in closed form:

$$
P=(MM^{\dagger})^{1/2}
=\frac{MM^{\dagger}+\lvert\det M\rvert\,\mathrm I_2}
{\sqrt{\operatorname{Tr}(MM^{\dagger})+2\lvert\det M\rvert}},
$$

using $\sqrt{\det(MM^{\dagger})}=\lvert\det M\rvert$. The formula is valid for every nonzero $M$; for a singular $M$ it gives the rank-one positive factor.

**The $*$-unitary factor.** When $M$ is invertible, $P$ is positive definite and

$$
V=P^{-1}M
=\frac{\sqrt{\operatorname{Tr}(MM^{\dagger})+2\lvert\det M\rvert}}
{MM^{\dagger}+\lvert\det M\rvert\,\mathrm I_2}\,M,
$$

which is $*$-unitary. When $M$ is singular, $P$ is only positive semidefinite and the factor $V$ is the partial isometry obtained from the Moore–Penrose inverse $P^{+}$, not from $P^{-1}$.

## The Biquaternion Word

**The two factors in the algebra.** For a regular element, the matrix polar decomposition reads

$$
M=r\,\zeta\,M_bM_r,
\qquad
r>0,\quad|\zeta|=1,\quad
M_b\text{ positive Hermitian of determinant }1,\quad
M_r\in SU(2).
$$

The factor $P$ is $rM_b$ and the factor $V$ is $\zeta M_r$. The four factors are the scale, the phase, the boost and the rotor.

| Factor | Matrix | Determinant | Algebra-side name |
|---|---|---|---|
| $r$ | $r\mathrm I_2$ | $r^2$ | the modulus |
| $\zeta$ | $\zeta\mathrm I_2$ | $\zeta^2$ | the central phase |
| $M_b$ | positive Hermitian, $\det1$ | $1$ | the boost |
| $M_r$ | $SU(2)$ | $1$ | the rotor |

**Why the factors are these.** The positive Hermitian matrices are the images of the Hermitian elements; the positive definite ones of determinant one are the images of the Hermitian unit-norm elements, which are the boosts. The $*$-unitary matrices are the images of the elements with $\tilde Q^{*}\tilde Q=e_t$; those of determinant one are the images of the rotors. The scale is the modulus and the phase is the central $U(1)$. The matrix polar decomposition is therefore the algebra polar decomposition read factor by factor.

**The determinant check.** From the word,

$$
\det M=r^2\zeta^2,
$$

because both $M_b$ and $M_r$ have determinant one. The modulus is $r=|\det M|^{1/2}$ and the phase is a square root of $\det M/|\det M|$. The phase is defined up to sign, and the sign is the double cover: $\zeta$ and $-\zeta$ give the same matrix only when $M_r$ is also negated, and $M_r$ and $-M_r$ are the two preimages of the same rotation.

**The special linear case.** If $M\in SL_2$, then $r=1$ and $\zeta^2=1$, so $\zeta=\pm1$. The decomposition reduces to

$$
SL_2(\mathbb{C})=Herm^{>0}_1\cdot SU(2),
$$

the positive Hermitian matrices of determinant one times the special $*$-unitary group. Both factors are of real dimension three, and the product is a diffeomorphism. The factor $Herm^{>0}_1$ is the boost and $SU(2)$ is the rotor.

**The cost of the division.** The decomposition has a computational face. Sangwine and Hitzer observe that the matrix image is not the cheaper route to the numbers: the biquaternion itself carries four complex numbers, the general matrix carries four complex entries, but only the matrices of the model occur, and a general numerical polar decomposition of an arbitrary matrix need not preserve that form over a long computation. Their algorithm obtains the hyperbolic factor by dividing out the trigonometric factor, $	ilde U_{\mathrm b}=\tilde Q\tilde u_{\mathrm r}^{-1}$, which costs a division; the square root $\sqrt{\tilde Q\tilde Q^{*}}$ used above exhibits the existence and the Hermiticity of the factor, and is not the cheapest way to compute it.

## The Two Halves

**The boost.** A positive Hermitian matrix of determinant one is the exponential of a traceless Hermitian matrix:

$$
M_b=\exp(H),\qquad H=H^{\dagger},\quad\operatorname{Tr}H=0.
$$

Writing $H=\tfrac{\eta}{2}\hat u\cdot\sigma$ with $\hat u$ a unit vector and $\eta\in\mathbb{R}$, the matrix is

$$
M_b=\cosh\tfrac{\eta}{2}\,\mathrm I_2+\sinh\tfrac{\eta}{2}\,\hat u\cdot\sigma,
$$

with eigenvalues $e^{\pm\eta/2}$. The parameter $\eta$ is the rapidity and $\hat u$ the boost direction. In the algebra it is the Hermitian unit-norm element $\exp(\tfrac{\eta}{2}i\hat u\cdot\vec e)$.

**The rotor.** A special $*$-unitary matrix is the exponential of a traceless anti-Hermitian matrix:

$$
M_r=\exp(K),\qquad K=-K^{\dagger},\quad\operatorname{Tr}K=0,
$$

and writing $K=-\tfrac{i\theta}{2}\hat u\cdot\sigma$ gives

$$
M_r=\cos\tfrac{\theta}{2}\,\mathrm I_2-i\sin\tfrac{\theta}{2}\,\hat u\cdot\sigma,
$$

with eigenvalues $e^{\pm i\theta/2}$. The parameter $\theta$ is the rotation angle and $\hat u$ the axis. In the algebra it is the rotor $\exp(\tfrac{\theta}{2}\hat u\cdot\vec e)$.

**The order of the factors.** The decomposition is $M=PV$, positive factor first, $*$-unitary second. The algebra decomposition is $\tilde Q=\tilde Q_H\tilde Q_0$ with the same order. The reverse order would give a different pair of factors, and the two orders are related by conjugating the $*$-unitary factor by the positive one. The convention is fixed by the matrix theorem, and the algebra articles use the same order.

**The two real forms.** The boost is Hermitian and the rotor is $*$-unitary. The Hermitian matrices are the informational subspace $\mathbb{M}_+$; the $*$-unitary group is the compact real form of the unit group. The polar decomposition is therefore a decomposition of the complex group into a non-compact Hermitian factor and a compact $*$-unitary factor, and it is the matrix form of the split of the algebra into its two real forms.

## The Singular Case

**The partial isometry.** When $M$ is singular, $P=(MM^{\dagger})^{1/2}$ is positive semidefinite of rank equal to the rank of $M$, and $V$ is a partial isometry: it is an isometry on the orthogonal complement of $\ker M$ and zero on $\ker M$. The factorisation $M=PV$ still holds and is still unique with $P$ positive semidefinite and $\ker V=\ker M$.

**The rank-one case.** For $M=uv^{\mathsf T}$,

$$
MM^{\dagger}=\|v\|^2\,uu^{\dagger},
\qquad
P=\|v\|\,\frac{uu^{\dagger}}{\|u\|},
$$

a rank-one positive matrix, and $V$ maps $(\ker M)^{\perp}$ isometrically onto the image line of $M$ and kills $\ker M$. The $*$-unitary factor is not $*$-unitary: it has a one-dimensional kernel. The matrix is a partial isometry times a rank-one positive factor, and the missing direction is the kernel of the rank-one element.

**The degenerate element.** On the null cone the algebra-side polar decomposition has a vanishing modulus; the matrix factor $P$ is rank one and the factor $V$ is a partial isometry. The two chiralities of the rank-one element correspond to the image and the kernel of $V$. The details are *The Polar Decomposition of a N-Degenerate Biquaternion*, §*The Degenerate Factorisation*.

**The cone.** The map $M\mapsto P$ is continuous on the whole matrix algebra and sends the cone to the positive semidefinite matrices of rank at most one. The map $M\mapsto V$ is not continuous at the origin: the direction of $V$ depends on the direction of approach. The polar decomposition is a diffeomorphism on the open set of invertible matrices and only a bijection on the singular locus, where $V$ fails to be continuous at the origin.

## The Singular Value Decomposition

**The theorem.** Every $M\in M_2(\mathbb{C})$ factors as

$$
M=U\Sigma V^{\dagger},\qquad
\Sigma=\operatorname{diag}(s_1,s_2),\quad s_1\ge s_2\ge0,
$$

with $U$ and $V$ $*$-unitary. The numbers $s_1,s_2$ are the **singular values**; they are the eigenvalues of the positive factor $P=(MM^{\dagger})^{1/2}$ and are determined by $M$. The factorisation is unique up to $U\mapsto U\Lambda$, $V\mapsto V\Lambda$ for a diagonal $*$-unitary $\Lambda$ when $s_1>s_2$.

**From the polar decomposition.** Write the polar decomposition as $M=PW$, with $W$ $*$-unitary when $M$ is invertible, and diagonalise the positive factor,

$$
P=U\Sigma U^{\dagger}.
$$

Then

$$
M=U\Sigma\,(W^{\dagger}U)^{\dagger},
$$

so the left $*$-unitary is the eigenbasis of $P$ and the right $*$-unitary is $W^{\dagger}U$. The SVD is the polar decomposition with the positive factor diagonalised; conversely $P=U\Sigma U^{\dagger}$ and $W=UV^{\dagger}$ recover the polar factors.

**The singular values in the biquaternion word.** With $M=r\zeta M_bM_r$, the positive factor is $P=rM_b$. The eigenvalues of $M_b$ are $e^{\pm\eta/2}$, so

$$
s_1=r e^{\eta/2},\qquad s_2=r e^{-\eta/2},\qquad s_1s_2=r^2=\lvert\det M\rvert.
$$

The singular values coincide exactly when $M_b=\mathrm I_2$, that is when $M$ is a scalar times a $*$-unitary. The rapidity $\eta$ is the parameter that separates them.

**The normal case.** The multiset of singular values equals the multiset of eigenvalue moduli exactly when $M$ is normal: $\sum_i s_i^2=\operatorname{tr}(MM^{\dagger})$ equals $\sum_i\lvert\lambda_i\rvert^2$ exactly in that case, by Schur's inequality. In the biquaternion word normality makes $M_b$ commute with $M_r$, and the eigenvalues then have moduli $r e^{\pm\eta/2}$.

**The rank and the strata.** The rank is the number of nonzero singular values. On the determinantal variety $s_2=0$: the rank-one matrices have $s_1>0$, $s_2=0$, and the zero matrix has $s_1=s_2=0$. The modulus of the determinant is the product $s_1s_2$, so it vanishes exactly when a singular value does.

**The algebra reading.** The left $*$-unitary is the eigenbasis of the boost, the diagonal factor is the boost read in that basis, and the right $*$-unitary is the rotor composed with the same basis. The SVD separates the two rotations from the rapidity; the polar decomposition keeps the boost and the rotor together.

## Summary

Every invertible matrix is uniquely $M=PV$ with $P$ positive definite and $V$ $*$-unitary; explicitly $P=(MM^{\dagger})^{1/2}$ and $V=P^{-1}M$. For a biquaternion matrix the word is $M=r\zeta M_bM_r$ with $r>0$, $|\zeta|=1$, $M_b$ positive Hermitian of determinant one and $M_r\in SU(2)$. The determinant is $r^2\zeta^2$, the modulus is $|\det M|^{1/2}$, and on $SL_2$ the decomposition is $Herm^{>0}_1\cdot SU(2)$. On singular matrices the positive factor is semidefinite and the $*$-unitary factor is only a partial isometry. The singular value decomposition diagonalises the positive factor, $P=U\Sigma U^{\dagger}$, and the singular values are $r e^{\pm\eta/2}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M=PV$ | the polar decomposition |
| $P=(MM^{\dagger})^{1/2}$ | the positive factor |
| $V=P^{-1}M$ | the $*$-unitary factor |
| $r=|\det M|^{1/2}$ | the modulus |
| $\zeta$ | the central phase, $|\zeta|=1$ |
| $M_b$ | the boost, positive Hermitian of determinant one |
| $M_r$ | the rotor, in $SU(2)$ |
| $M=U\Sigma V^{\dagger}$ | the singular value decomposition |
| $s_1,s_2$ | the singular values, the eigenvalues of $P$ |
| $W$ | the polar $*$-unitary in the SVD derivation |
| $Herm^{>0}_1$ | positive Hermitian matrices of determinant one |

## Further Reading

- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the regular element
- [The Polar Decomposition of a N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the singular element
- [The Polar Decomposition of a Biquaternion](the-polar-decomposition-of-a-biquaternion.html), for the general statement
- [$M_2(\mathbb{C})$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant](m2c-representation-gl2-sl2-and-the-determinant.html), for the group decomposition
- [The Sandwich in the $M_2(\mathbb{C})$ Model](the-sandwich-in-the-m2c-model.html), for the action of the factors
- [The Unitary Group of the Biquaternion Algebra](the-unitary-group-of-the-biquaternion-algebra.html), for $U(2)$
- [Eigenvalues and Diagonalisation](eigenvalues-and-diagonalisation.html), for the matrix polar decomposition
