# __Matrix Representations : The Polar Decomposition of a Matrix__

## Introduction

Every invertible matrix is the product of a positive definite matrix and a unitary one. The decomposition is unique, it is a diffeomorphism, and it splits the determinant into modulus and phase. In the biquaternion algebra the two factors have names: the positive factor is the boost, the unitary factor is the rotor, and the determinant carries the scale and the central phase.

This article develops the matrix theorem, the closed form of the positive factor, the biquaternion word, the two halves, the singular case and the singular value decomposition. It is the article that turns the exponential of *Matrix Representations : The Functional Calculus* and the unitarities of *Matrix Representations : The Hermitian Sandwich* into a factorisation of every element.

**Conventions.** The algebra and the displays are those of *Matrix Representations : The Models and the Change of Frame*. The element is $\tilde Q=Q_te_t+\vec Q$, with $B=\mathsf M_2(\tilde Q)$ and $N=\langle\tilde Q\rangle_{\natural}=\det B$. The regular matrix is $L=L(\tilde Q)=I_2\otimes B$, with $\det L=N^2$. The dagger is the Hermitian adjoint of *Matrix Representations : The Hermitian Sandwich*, and $*$-unitary means $V^{\dagger}V=\mathrm I$.

**Boundaries.** The matrix theorem is *Matrix Representations : The Polar Decomposition of a Matrix* and *Matrix Representations : The Polar Decomposition of a Matrix*; the algebra word is *The Polar Decomposition of a Biquaternion*; the exponential is *Matrix Representations : The Functional Calculus*; the singular value decomposition is *The Singular Value Decomposition of a Biquaternion*; the boost and the rotor are *The Two Halves*.

## Common Aspects



### The Theorem

**The statement.** Every matrix $M$ has a factorisation
$$
M=PV,
$$
with $P$ positive semidefinite and $V$ a partial isometry. When $M$ is invertible, $P$ is positive definite, $V$ is $*$-unitary, and the pair is unique:
$$
P=(MM^{\dagger})^{1/2},\qquad V=P^{-1}M .
$$

*Proof.* The matrix $MM^{\dagger}$ is Hermitian positive semidefinite and has a unique positive semidefinite square root $P$. For invertible $M$ the factor $P$ is invertible, and
$$
V^{\dagger}V=M^{\dagger}P^{-2}M=M^{\dagger}(MM^{\dagger})^{-1}M=\mathrm I,
$$
so $V$ is $*$-unitary. If $M=PV=P'V'$ with positive definite $P,P'$, then $MM^{\dagger}=P^2=P'^2$, and the uniqueness of the positive square root gives $P=P'$ and $V=V'$.

**The diffeomorphism.**
$$
Herm^{>0}\times U\longrightarrow GL,
\qquad
(P,V)\longmapsto PV,
$$
with inverse $M\mapsto((MM^{\dagger})^{1/2},(MM^{\dagger})^{-1/2}M)$. The positive factor has real dimension four and the unitary factor has real dimension four, in both displays; the product accounts for the eight real dimensions of the group of units.

**The determinant split.**
$$
\det M=\det P\,\det V,\qquad
\det P=\lvert\det M\rvert,\qquad
\lvert\det V\rvert=1 .
$$
For the regular matrix, $\det M=N^2$, $\det P=\lvert N\rvert^2$ and $\det V=N^2/\lvert N\rvert^2$.

**The factors stay in the regular image.** If $M=L(\tilde Q)$, then $MM^{\dagger}=L(\tilde Q\tilde Q^{*})$ is the image of a Hermitian positive element. Its positive square root is a function of that element, hence lies in the image, and the unitary factor is a product of two images:
$$
P=L(\tilde Q_H),\qquad V=L(\tilde Q_0),
\qquad
\tilde Q_H=\tilde Q_H^{*}\ge0,\quad \tilde Q_0^{*}\tilde Q_0=e_t .
$$

### The Closed Form of the Positive Factor

**The square root of a Hermitian matrix.** For a Hermitian $Y$ with non-negative eigenvalues $a,b$, not both zero, the positive square root is a degree-one polynomial:
$$
Y^{1/2}=\frac{Y+\sqrt{ab}\,\mathrm I}{\sqrt{a+b+2\sqrt{ab}}} .
$$
In the $2\times2$ display $a,b$ are the eigenvalues of $Y=BB^{\dagger}$ and $a+b=\operatorname{Tr}Y$. In the regular display the eigenvalues are $a,a,b,b$, the trace is $2(a+b)$, and the same polynomial reads
$$
Y^{1/2}=\frac{Y+\sqrt{ab}\,\mathrm I_4}{\sqrt{\tfrac12\operatorname{Tr}Y+2\sqrt{ab}}} .
$$
The half-trace is the only difference between the two displays.

**The positive factor.**
$$
P=(MM^{\dagger})^{1/2}=
\begin{cases}
\dfrac{MM^{\dagger}+\lvert\det M\rvert\,\mathrm I_2}
{\sqrt{\operatorname{Tr}(MM^{\dagger})+2\lvert\det M\rvert}}, & 2\times2,\\[10pt]
\dfrac{MM^{\dagger}+\lvert N\rvert\,\mathrm I_4}
{\sqrt{\tfrac12\operatorname{Tr}(MM^{\dagger})+2\lvert N\rvert}}, & 4\times4,
\end{cases}
$$
using $\sqrt{\det(MM^{\dagger})}=\lvert\det M\rvert$ in the first line and $\sqrt{\det(LL^{\dagger})}=\lvert N\rvert$ in the second. Both formulas are valid for every nonzero $M$; for a singular $M$ they give the positive semidefinite factor.

**The unitary factor.** For invertible $M$,
$$
V=P^{-1}M=\frac{\sqrt{\operatorname{Tr}(MM^{\dagger})+2\lvert\det M\rvert}}
{MM^{\dagger}+\lvert\det M\rvert\,\mathrm I_2}\,M
$$
in the $2\times2$ display, and the same expression with the half-trace in the regular display. For singular $M$ the inverse is replaced by the Moore–Penrose inverse $P^{+}$ and $V$ is a partial isometry.

### The Two Halves

**The boost.** A positive Hermitian matrix of determinant one is the exponential of a traceless Hermitian matrix:
$$
M_b=\exp(H),\qquad H=H^{\dagger},\quad\operatorname{Tr}H=0 .
$$
Writing $H=\tfrac{\eta}{2}\hat u\cdot\Sigma$ with $\hat u$ a unit spatial direction and $\eta\in\mathbb{R}$,
$$
L(H_b)=\operatorname{diag}(M_b,M_b),
$$
with eigenvalues $e^{\pm\eta/2}$, each twice. The parameter $\eta$ is the rapidity and $\hat u$ the direction. In the algebra it is the Hermitian unit-norm element $\exp(\tfrac{\eta}{2}i\hat u\cdot\vec e)$.

**The rotor.** A special unitary matrix is the exponential of a traceless anti-Hermitian matrix:
$$
M_r=\exp(K),\qquad K=-K^{\dagger},\quad\operatorname{Tr}K=0 .
$$
Writing $K=-\tfrac{i\theta}{2}\hat u\cdot\Sigma$,
$$
L(M_r)=\operatorname{diag}(M_r,M_r),
$$
with eigenvalues $e^{\pm i\theta/2}$, each twice. The parameter $\theta$ is the angle and $\hat u$ the axis. In the algebra it is the rotor $\exp(\tfrac{\theta}{2}\hat u\cdot\vec e)$.

**The order.** The decomposition is $M=PV$, positive factor first. The algebra word has the same order, $\tilde Q=\tilde Q_H\tilde Q_0$. The reverse order gives different factors, related by conjugating the unitary factor by the positive one.

### The Singular Case

**The partial isometry.** For a nonzero singular $M$, the positive factor $P=(MM^{\dagger})^{1/2}$ has rank equal to the rank of $M$, and $V$ is a partial isometry with initial space the kernel of $M$ and final space the image of $M$. The decomposition $M=PV$ remains unique if $P$ is required positive semidefinite and $V$ to vanish on the kernel.

**The regular singular stratum.** In the regular image the nonzero singular matrices have rank two, so $P$ and $V$ have rank two and the product has rank two. The decomposition preserves the rank stratification.

**The zero matrix.** At $M=0$ the positive factor is $0$ and the partial isometry is arbitrary; the decomposition is not unique.

## The $S_3$ Frame



### The Biquaternion Word

**The factorisation.** For a regular element,
$$
M=r\,\zeta\,M_bM_r,
\qquad
r>0,\quad\lvert\zeta\rvert=1,\quad
M_b\text{ positive Hermitian of determinant }1,\quad
M_r\in SU(2).
$$
The positive factor is $P=rM_b$ and the unitary factor is $V=\zeta M_r$. The four factors are the scale, the phase, the boost and the rotor.

| Factor | Matrix | Determinant | Algebra side |
|---|---|---|---|
| $r$ | $r\mathrm I$ | $r^2$ | the modulus |
| $\zeta$ | $\zeta\mathrm I$ | $\zeta^2$ | the central phase |
| $M_b$ | positive Hermitian, $\det1$ | $1$ | the boost |
| $M_r$ | $SU(2)$ | $1$ | the rotor |

**The determinant check.**
$$
\det M=r^2\zeta^2,
$$
because $M_b$ and $M_r$ have determinant one. Hence $r=\lvert\det M\rvert^{1/2}$ and $\zeta$ is a square root of $\det M/\lvert\det M\rvert$. The phase is defined up to sign; the sign is the double cover, and $\zeta$ and $-\zeta$ describe the same matrix when the rotor is also negated.

**The special linear case.** If $M\in SL_2(\mathbb{C})$, then $r=1$ and $\zeta=\pm1$, and
$$
SL_2(\mathbb{C})=Herm^{>0}_1\cdot SU(2),
$$
a diffeomorphism of two three-dimensional factors. The first is the boost and the second is the rotor.

**The regular display.** In the regular model,
$$
L(\tilde Q)=r\zeta\,L(\tilde Q_H)\,L(\tilde Q_0),
$$
with $L(\tilde Q_H)=\operatorname{diag}(M_b,M_b)$ and $L(\tilde Q_0)=\operatorname{diag}(M_r,M_r)$. The two factors act identically on the two minimal left ideals.

**The two real forms.** The positive factor is Hermitian and non-compact; the unitary factor is compact. The decomposition is the matrix form of the Cartan decomposition of the group of units, and the two factors are the two real forms of the algebra.

## The $2\times2$ $z$ Frame



**The entry formula.** In the entry model the decomposition is $B=PV$, with
$$
P=(BB^{\dagger})^{1/2}=\frac{BB^{\dagger}+\lvert\det B\rvert\,\mathrm I_2}
{\sqrt{\operatorname{Tr}(BB^{\dagger})+2\lvert\det B\rvert}},
\qquad
V=P^{-1}B
$$
for invertible $B$. The formula is the Cayley–Hamilton square root: the positive factor is a degree-one polynomial in $BB^{\dagger}$, and the trace in the denominator is the $2\times2$ trace. For singular $B$ the inverse is replaced by the Moore–Penrose inverse and $V$ is a partial isometry.

**The word in the entry model.** With $B=r\zeta M_bM_r$ and $r>0$, $\lvert\zeta\rvert=1$, $M_b$ positive Hermitian of determinant one and $M_r\in SU(2)$, the determinant is $\det B=r^2\zeta^2$ and the modulus is $r^2$. The positive factor is $rM_b$ and the unitary factor is $\zeta M_r$.

**The singular values.** The eigenvalues of $rM_b$ are $re^{\pm\eta/2}$, so
$$
s_1=re^{\eta/2},\qquad s_2=re^{-\eta/2},\qquad s_1s_2=r^2=\lvert\det B\rvert.
$$
The rank is two when $r\neq0$, one on the nonzero singular stratum and zero at $B=0$. The singular values coincide exactly when the boost is trivial, and their multiset equals the multiset of eigenvalue moduli exactly when $B$ is normal.

## The $4\times4$ $z$ Frame



### The Singular Value Decomposition

**The theorem.** Every $M$ factors as
$$
M=U\Sigma V^{\dagger},
\qquad
\Sigma=\operatorname{diag}(s_1,\dots),
$$
with $U,V$ $*$-unitary and $s_j\ge0$. In the $2\times2$ display $\Sigma=\operatorname{diag}(s_1,s_2)$; in the regular display $\Sigma=\operatorname{diag}(s_1,s_1,s_2,s_2)$, so every singular value is doubled.

**The construction.** Write $M=PW$ with $W$ unitary, diagonalise the positive factor,
$$
P=U\Sigma U^{\dagger},
$$
and set $V=W^{\dagger}U$. Then $M=U\Sigma V^{\dagger}$. Conversely, $P=U\Sigma U^{\dagger}$ and $W=UV^{\dagger}$ recover the polar factors. The SVD is the polar decomposition with the positive factor diagonalised.

**The singular values in the word.** With $M=r\zeta M_bM_r$, the positive factor is $rM_b$, whose eigenvalues are $e^{\pm\eta/2}$. Hence
$$
s_1=re^{\eta/2},\qquad
s_2=re^{-\eta/2},\qquad
s_1^2s_2^2=r^4=\lvert\det M\rvert,
$$
each repeated twice in the regular display. The singular values coincide exactly when the boost is trivial.

**The rank.** The rank is the number of nonzero singular values counted with multiplicity: four generically, two on the nonzero part of the determinantal variety, zero at the zero matrix. This is twice the rank of the $2\times2$ model, as the rank stratification requires.

**The normal case.** The multiset of singular values equals the multiset of eigenvalue moduli exactly when $M$ is normal. In the regular display the eigenvalues are doubled, and the condition is the normality of the underlying element.

## Summary

Every invertible matrix is uniquely $M=PV$, with $P$ positive definite and $V$ unitary; $P=(MM^{\dagger})^{1/2}$ and $V=P^{-1}M$. In the biquaternion word $M=r\zeta M_bM_r$, with $r>0$, $\lvert\zeta\rvert=1$, $M_b$ a positive Hermitian matrix of determinant one and $M_r\in SU(2)$; the determinant is $r^2\zeta^2$ and the modulus is $\lvert\det M\rvert^{1/2}$. The closed form of the positive factor is the Cayley–Hamilton square root, with the trace in the $2\times2$ display and the half-trace in the regular display. On singular matrices the positive factor is semidefinite and the unitary factor is only a partial isometry. The singular value decomposition diagonalises the positive factor; the singular values are $re^{\pm\eta/2}$, each doubled in the regular display.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M=PV$ | the polar decomposition |
| $P=(MM^{\dagger})^{1/2}$ | the positive factor |
| $V=P^{-1}M$ | the unitary factor |
| $r=\lvert\det M\rvert^{1/2}$ | the modulus |
| $\zeta$ | the central phase |
| $M_b$ | the boost, positive Hermitian of determinant one |
| $M_r$ | the rotor, in $SU(2)$ |
| $\eta,\theta$ | rapidity and angle |
| $s_1,s_2$ | the singular values |

## Further Reading

- [Matrix Representations : The Functional Calculus](matrix-representations-the-functional-calculus.html), for the square root
- [Matrix Representations : The Hermitian Sandwich](matrix-representations-the-hermitian-sandwich.html), for the unitary slice
- [Matrix Representations : GL2, SL2 and the Determinant](matrix-representations-gl2-sl2-and-the-determinant.html), for the determinant split
- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the displays
- [Matrix Representations : The Polar Decomposition of a Matrix](matrix-representations-the-polar-decomposition-of-a-matrix.html), for the full $2\times2$ treatment
- [Matrix Representations : The Polar Decomposition of a Matrix](matrix-representations-the-polar-decomposition-of-a-matrix.html), for the full $4\times4$ treatment
- [The Polar Decomposition of a Biquaternion](the-polar-decomposition-of-a-biquaternion.html), for the algebra word
