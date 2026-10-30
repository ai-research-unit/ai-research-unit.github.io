# __$M_4(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix__

## Introduction

Every invertible regular matrix is the product of a positive Hermitian matrix and a $*$-unitary one, and the product is unique. The two factors are the images of the two factors of the biquaternion polar decomposition: the positive factor is the boost, the $*$-unitary factor is the phase times the rotor. The regular model doubles the eigenvalues and squares the determinants.

This article develops the matrix polar decomposition, its refinement by the determinant, its closed form, its behaviour on the singular matrices, and the singular value decomposition. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix*.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. The norm is $N=\langle\tilde Q\rangle_{\natural}$, and $\det\mathsf{M}_4^{L}(\tilde Q)=N^2$. A matrix is **positive** when it is Hermitian with non-negative eigenvalues, and **positive definite** when the eigenvalues are positive. The $*$-unitary group of the image is $\mathrm U(\mathbb{B})\cong U(2)$.

**Boundaries.** The polar decomposition of the element is *The Polar Decomposition of a Biquaternion*; the groups are *$M_4(\mathbb{C})$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant*; the sandwich action is *$M_4(\mathbb{C})$ Model : The Sandwich*; the $2\times2$ version is *$M_2(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix*.

**Frame.** Unless a basis is named, matrices are written in the canonical frame of *Conventions in Mathematics*, §*The Matrix Models*, where $\mathsf{M}_4^{L}(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q)$. The coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ is the conjugate display: $\mathsf M_{4,\mathrm{coef}}^{L}=S\,(I_2\otimes\mathsf M_2)\,S^{-1}$, with $S$ the change of *The Product, the Trace and the Determinant*.

## The Matrix Polar Decomposition

**Theorem.** Every $M\in\mathsf{M}_4^{L}(\mathbb{B})$ has a factorisation
$$
M=PV,
$$
with $P$ positive semidefinite and $V$ a partial isometry. When $M$ is invertible, $P$ is positive definite, $V$ is $*$-unitary, and the factorisation is unique:
$$
P=(MM^{\dagger})^{1/2},\qquad V=P^{-1}M.
$$

*Proof.* The matrix $MM^{\dagger}$ is Hermitian positive semidefinite, so it has a unique positive semidefinite square root $P$. If $M$ is invertible, $P$ is invertible and $V=P^{-1}M$ satisfies
$$
V^{\dagger}V=M^{\dagger}P^{-2}M=M^{\dagger}(MM^{\dagger})^{-1}M=\mathrm I_4,
$$
so $V$ is $*$-unitary. For uniqueness, $MM^{\dagger}=P^2=P'^2$ and the uniqueness of the positive square root give $P=P'$, hence $V=V'$.

**The factors stay in the image.** Since $M=\mathsf{M}_4^{L}(\tilde Q)$, the product $MM^{\dagger}=\mathsf{M}_4^{L}(\tilde Q\tilde Q^{*})$ is the image of a Hermitian positive element. Its positive square root is a function of $\tilde Q\tilde Q^{*}$, hence lies in the image; the $*$-unitary factor is the product of two images. Therefore
$$
P=\mathsf{M}_4^{L}(\tilde Q_H),\qquad V=\mathsf{M}_4^{L}(\tilde Q_0),
$$
with $\tilde Q_H=\tilde Q_H^{*}\ge0$ and $\tilde Q_0^{*}\tilde Q_0=e_t$.

**The diffeomorphism.** The map
$$
Herm^{>0}\times \mathrm U(\mathbb{B})\longrightarrow\mathsf{M}_4^{L}(\mathbb{B}^{\times}),
\qquad
(P,V)\longmapsto PV,
$$
is a diffeomorphism. The inverse is $M\mapsto((MM^{\dagger})^{1/2},(MM^{\dagger})^{-1/2}M)$. The two factors have real dimensions four and four, and the product accounts for the eight real dimensions of the regular group.

## The Closed Form of the Positive Factor

**The square root by the minimal polynomial.** The Hermitian matrix $Y=MM^{\dagger}$ has eigenvalues $a,a,b,b$ with $a=\lvert\lambda_+\rvert^2$ and $b=\lvert\lambda_-\rvert^2$, so its minimal polynomial has degree at most two. Its positive square root is therefore a degree-one polynomial in $Y$:
$$
Y^{1/2}=\alpha Y+\beta\mathrm I_4,
\qquad
\alpha=\frac{1}{\sqrt a+\sqrt b},
\qquad
\beta=\frac{\sqrt{ab}}{\sqrt a+\sqrt b}.
$$
The coefficients are fixed by the two eigenvalues: on the $a$-eigenspace, $\alpha a+\beta=\sqrt a$, and on the $b$-eigenspace, $\alpha b+\beta=\sqrt b$.

**The closed form.** Since
$$
\sqrt a+\sqrt b=\sqrt{a+b+2\sqrt{ab}}
=\sqrt{\tfrac12\operatorname{Tr}Y+2\sqrt{ab}},
\qquad
\sqrt{ab}=\lvert\lambda_+\lambda_-\rvert=\lvert N\rvert,
$$
the positive factor is
$$
\boxed{\;
P=(MM^{\dagger})^{1/2}
=\frac{MM^{\dagger}+\lvert N\rvert\,\mathrm I_4}
{\sqrt{\tfrac12\operatorname{Tr}(MM^{\dagger})+2\lvert N\rvert}}
\;}
$$
with $N=\langle\tilde Q\rangle_{\natural}$ and $\lvert N\rvert=\lvert\det M\rvert^{1/2}$.

*Check.* On the $a$-eigenspace the numerator is $a+\lvert N\rvert=a+\sqrt{ab}=\sqrt a(\sqrt a+\sqrt b)$, and the denominator is $\sqrt a+\sqrt b$; the quotient is $\sqrt a$. On the $b$-eigenspace it is $\sqrt b$.

**The $*$-unitary factor.** When $M$ is invertible,
$$
V=P^{-1}M
=\frac{\sqrt{\tfrac12\operatorname{Tr}(MM^{\dagger})+2\lvert N\rvert}}
{MM^{\dagger}+\lvert N\rvert\,\mathrm I_4}\,M,
$$
which is $*$-unitary. When $M$ is singular, $P$ is only positive semidefinite and $V$ is the partial isometry obtained from the Moore–Penrose inverse $P^{+}$.

**The $2\times2$ comparison.** In the $2\times2$ model the eigenvalues of $Y$ are $a,b$, $\operatorname{Tr}Y=a+b$, and $\sqrt{ab}=\lvert\det M\rvert=\lvert N\rvert$. The denominator is $\sqrt{\operatorname{Tr}Y+2\lvert N\rvert}=\sqrt a+\sqrt b$, and the formula is the $2\times2$ one. In the regular model the eigenvalues are doubled, $\operatorname{Tr}Y=2(a+b)$, and the half-trace appears. The numerator is unchanged.

## The Biquaternion Word

**The two factors in the algebra.** For a regular element, the matrix polar decomposition reads
$$
M=r\,\zeta\,\mathsf{M}_4^{L}(\tilde H_b)\,\mathsf{M}_4^{L}(\tilde U_r),
\qquad
r>0,\quad\lvert\zeta\rvert=1,
$$
with $\tilde H_b$ positive Hermitian of norm one and $\tilde U_r$ a rotor, $\tilde U_r^{*}\tilde U_r=e_t$ and $N(\tilde U_r)=1$. The factor $P$ is $r\mathsf{M}_4^{L}(\tilde H_b)$ and the factor $V$ is $\zeta\mathsf{M}_4^{L}(\tilde U_r)$.

| Factor | Matrix | Determinant | Algebra-side name |
|---|---|---|---|
| $r$ | $r\mathrm I_4$ | $r^4$ | the modulus |
| $\zeta$ | $\zeta\mathrm I_4$ | $\zeta^4$ | the central phase |
| $\tilde H_b$ | positive Hermitian, $N=1$ | $1$ | the boost |
| $\tilde U_r$ | rotor, $N=1$, $*$-unitary | $1$ | the rotor |

**Why the determinants are fourth powers.** The regular determinant is the square of the norm, and the norm of a scalar is the square of the scalar. Hence the scale $r$ contributes $r^4$ and the phase $\zeta$ contributes $\zeta^4$:
$$
\det M=r^4\zeta^4.
$$
The modulus is $r=\lvert\det M\rvert^{1/4}$ and the phase is a fourth root of $\det M/\lvert\det M\rvert$. The fourth root is the composition of the square in the norm and the square in the determinant.

**The special linear case.** If $M$ lies in the norm-one group, then $r=1$ and $\zeta^4=1$, so $\zeta$ is a fourth root of unity. The decomposition reduces to
$$
M=\mathsf{M}_4^{L}(\tilde H_b)\mathsf{M}_4^{L}(\tilde U_r),
$$
the positive factor of norm one and the rotor.

**The Lie algebra.** The polar decomposition at the identity is the Cartan decomposition
$$
\mathfrak{gl}_2(\mathbb{C})=\mathfrak{u}(2)\oplus Herm,
$$
the skew-Hermitian part and the Hermitian part. In the regular image the same decomposition is
$$
\mathsf{M}_4^{L}(\mathbb{B})=\mathsf{M}_4^{L}(\mathfrak{u}(\mathbb{B}))\oplus\mathsf{M}_4^{L}(Herm),
$$
with the two summands of real dimensions four and four.

**The group.** The multiplication map
$$
\mathrm U(\mathbb{B})\times Herm^{>0}\longrightarrow\mathbb{B}^{\times}
$$
is a diffeomorphism, and its image is the polar decomposition of the regular group. The two factors are the maximal compact subgroup and the positive Hermitian cone.

## The Two Halves

**The boost.** A positive Hermitian matrix of determinant one is the exponential of a traceless Hermitian matrix:
$$
M_b=\exp(H),\qquad H=H^{\dagger},\quad\operatorname{Tr}H=0.
$$
Writing $H=\tfrac{\eta}{2}\hat u\cdot\Sigma$ with $\hat u$ a unit vector and $\eta\in\mathbb{R}$, the regular matrix is the block matrix
$$
\mathsf{M}_4^{L}(H_b)=\operatorname{diag}(M_b,M_b),
$$
with eigenvalues $e^{\pm\eta/2}$, each twice. The parameter $\eta$ is the rapidity and $\hat u$ the boost direction. In the algebra it is the Hermitian unit-norm element $\exp(\tfrac{\eta}{2}i\hat u\cdot\vec e)$.

**The rotor.** A special $*$-unitary matrix is the exponential of a traceless anti-Hermitian matrix:
$$
M_r=\exp(K),\qquad K=-K^{\dagger},\quad\operatorname{Tr}K=0,
$$
and writing $K=-\tfrac{i\theta}{2}\hat u\cdot\Sigma$ gives the block matrix
$$
\mathsf{M}_4^{L}(U_r)=\operatorname{diag}(M_r,M_r),
$$
with eigenvalues $e^{\pm i\theta/2}$, each twice. The parameter $\theta$ is the rotation angle and $\hat u$ the axis. In the algebra it is the rotor $\exp(\tfrac{\theta}{2}\hat u\cdot\vec e)$.

**The order of the factors.** The decomposition is $M=PV$, positive factor first, $*$-unitary second. The algebra decomposition is $\tilde Q=\tilde Q_H\tilde Q_0$ with the same order. The reverse order would give a different pair of factors, and the two orders are related by conjugating the $*$-unitary factor by the positive one. The convention is fixed by the matrix theorem, and the algebra articles use the same order.

**The two real forms.** The boost is Hermitian and the rotor is $*$-unitary. The Hermitian matrices are the informational subspace $\mathbb{M}_+$; the $*$-unitary group is the compact real form of the unit group. The polar decomposition is therefore a decomposition of the complex group into a non-compact Hermitian factor and a compact $*$-unitary factor, and it is the matrix form of the split of the algebra into its two real forms. In the regular model each factor is doubled, and the two copies are the two minimal left ideals.

**Theorem.** For an invertible $M$,
$$
\det M=\det P\,\det V,
\qquad
\det P=\lvert\det M\rvert,
\qquad
\lvert\det V\rvert=1.
$$
In the regular model,
$$
\det M=N^2,\qquad
\det P=\lvert N\rvert^2,\qquad
\det V=\frac{N^2}{\lvert N\rvert^2}.
$$

*Proof.* The positive factor has positive real determinant, and the $*$-unitary factor has determinant of modulus one. The product is the determinant of $M$. For the regular matrix, $\det M=N^2$ and $\det P=(\lvert N\rvert)^2$.

**The phase.** The determinant of the $*$-unitary factor is a complex number of modulus one. It is the square of the phase of the norm, because the determinant is the square of the norm; equivalently it is the fourth power of the central phase $\zeta$.

## The Singular Case

**The partial isometry.** For a nonzero singular $M$, the positive factor $P=(MM^{\dagger})^{1/2}$ has rank two, and $V$ is a partial isometry with initial space the kernel of $M$ and final space the image of $M$. The decomposition $M=PV$ is still unique if $P$ is required to be positive semidefinite and $V$ to vanish on the kernel.

**The rank.** The regular model has rank two on the singular stratum, so $P$ has rank two, $V$ has rank two, and the product has rank two. The polar decomposition preserves the rank stratification of *$M_4(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety*.

**The zero matrix.** At $M=0$ the positive factor is $0$ and the partial isometry is arbitrary; the decomposition is not unique.

## The Singular Value Decomposition

**The theorem.** Every $M\in M_4(\mathbb{C})$ factors as

$$
M=U\Sigma V^{\dagger},\qquad
\Sigma=\operatorname{diag}(s_1,s_1,s_2,s_2),\quad s_1\ge s_2\ge0,
$$

with $U$ and $V$ $*$-unitary. The two numbers $s_1,s_2$ are the singular values of the regular matrix, each repeated twice.

**The doubling.** The assignment $\mathsf{M}_4^{L}$ is a $*$-isomorphism onto its image, so

$$
MM^{\dagger}=\mathsf{M}_4^{L}(\tilde Q\tilde Q^{*})
$$

has the eigenvalues of $AA^{\dagger}$ each twice, with $A=\mathsf{M}_2(\tilde Q)$. Hence the singular values of $\mathsf{M}_4^{L}(\tilde Q)$ are those of $A$, each twice, and the ambient $4\times4$ matrix has no further singular values.

**From the polar decomposition.** Write $M=PW$, with $W$ $*$-unitary when $M$ is invertible, and diagonalise the positive factor,

$$
P=U\Sigma U^{\dagger},\qquad
\Sigma=\operatorname{diag}(s_1,s_1,s_2,s_2).
$$

Then

$$
M=U\Sigma\,(W^{\dagger}U)^{\dagger},
$$

so the left $*$-unitary is the eigenbasis of $P$ and the right $*$-unitary is $W^{\dagger}U$. The SVD is the polar decomposition with the positive factor diagonalised; conversely $P=U\Sigma U^{\dagger}$ and $W=UV^{\dagger}$ recover the polar factors.

**The singular values in the biquaternion word.** With $M=r\zeta\mathsf{M}_4^{L}(\tilde H_b)\mathsf{M}_4^{L}(\tilde U_r)$, the positive factor is $P=r\mathsf{M}_4^{L}(\tilde H_b)$. The eigenvalues of $\tilde H_b$ are $e^{\pm\eta/2}$, so

$$
s_1=r e^{\eta/2},\qquad s_2=r e^{-\eta/2},\qquad s_1^2s_2^2=r^4=\lvert\det M\rvert,
$$

each singular value repeated twice. The singular values coincide exactly when $\tilde H_b=e_t$.

**The normal case.** The multiset of singular values equals the multiset of eigenvalue moduli exactly when $M$ is normal, by the equality case of Schur's inequality. In the regular model the eigenvalues are doubled, and the condition is the normality of the underlying element.

**The rank and the strata.** The rank is the number of nonzero singular values counted with multiplicity: it is $4$ generically, $2$ on the nonzero part of the determinantal variety, and $0$ at the zero matrix. This is twice the rank of the $2\times2$ model, as the rank stratification requires.

**The algebra reading.** In the basis in which the regular matrix is the two copies of $A$, the SVD is the direct sum of two copies of the $2\times2$ SVD. The two unitaries then act identically on the two copies; the diagonal factor is the boost read in the eigenbasis, and it need not lie in the image.

## Summary

Every invertible regular matrix is uniquely $M=PV$ with $P$ positive definite Hermitian and $V$ $*$-unitary, both in the image. The positive factor is $(MM^{\dagger})^{1/2}$, with the closed form $(MM^{\dagger}+\lvert\det M\rvert\mathrm I_4)/\sqrt{\tfrac12\operatorname{Tr}(MM^{\dagger})+2\lvert\det M\rvert}$, and the $*$-unitary factor is $P^{-1}M$. The determinant splits as $\det P=\lvert\det M\rvert$ and $\lvert\det V\rvert=1$. In the algebra word $M=r\zeta\mathsf{M}_4^{L}(\tilde H_b)\mathsf{M}_4^{L}(\tilde U_r)$, the determinant is $r^4\zeta^4$: the regular model squares the $2\times2$ determinants. The singular case gives a rank-two positive factor and a partial isometry. The singular value decomposition diagonalises the positive factor, $P=U\Sigma U^{\dagger}$, and the singular values are $r e^{\pm\eta/2}$, each repeated twice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M=PV$ | the polar decomposition |
| $P=(MM^{\dagger})^{1/2}$ | the positive factor |
| $V=P^{-1}M$ | the $*$-unitary factor |
| $r=\lvert\det M\rvert^{1/4}$ | the modulus in the regular model |
| $\zeta$ | the phase, a fourth root of the determinant phase |
| $M=U\Sigma V^{\dagger}$ | the singular value decomposition |
| $s_1,s_2$ | the singular values, each repeated twice |
| $W$ | the polar $*$-unitary in the SVD derivation |
| $\tilde H_b,\tilde U_r$ | the boost and the rotor |

## Further Reading

- [$M_4(\mathbb{C})$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant](m4c-representation-gl2-sl2-and-the-determinant.html), for the groups
- [$M_4(\mathbb{C})$ Model : The Sandwich](the-sandwich-in-the-m4c-l-model.html), for the action of the factors
- [$M_2(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix](m2c-representation-the-polar-decomposition-of-a-matrix.html), for the $2\times2$ version
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the algebra
- [The Polar Decomposition of a N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the singular case
