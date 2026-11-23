# __One-Sided Operators on the N-Degenerate Sector in $M_2(\mathbb{C})$__

## Introduction

**The question.** On the null cone $\det A=0$, $A\neq0$, the matrix is singular, so $L_A(Y)=AY$ and $R_A(Y)=YA$ drop rank. What are their ranks, kernels, spectra, Jordan types and one-parameter groups, on the two strata $\Sigma_{01}$ and $\Sigma_{00}$?

**Why it is the same statement.** This is the in-depth matrix reading of [One-Sided Operators on the N-Degenerate Sector](one-sided-operators-on-the-n-degenerate-sector.html). The source's polar pair, its rank-one singular value decomposition and its two strata become, under $A=\mathsf M_2(\tilde Q)$, the rank-one matrix $A=2auv^{\dagger}$; the two slots become the two unit vectors $u$ and $v$; the overlap $v^{\dagger}u$ becomes the trace. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The two strata as matrix sets. The rank-one decomposition $A=2auv^{\dagger}$ with $a=\lVert A\rVert_F/2$, and the two slots. The overlap $v^{\dagger}u=\operatorname{tr}A/(2a)$ and its criterion for the strata. The polar pair $P=uu^{\dagger}$, $A_H=2auu^{\dagger}$, $A_0=uv^{\dagger}$. The closed form on $\Sigma_{01}$ with $\kappa$ and $A_0^2=\frac{Q_t}{a}A_0$. The canonical Hermitian pair on $\Sigma_{00}$. The one-sided operators: rank $2$, two-dimensional kernel, minimal right ideal as image, spectra $c,c,0,0$ and $0,0,0,0$. Their exponentials.

**What the article does not do.** It does not treat the two-sided operator, which is [Two-Sided Operators on the N-Degenerate Sector in $M_2(\mathbb{C})$](two-sided-operators-on-the-n-degenerate-sector-in-m2c.html). It does not re-derive the polar decomposition of a singular matrix, which is [The Polar Decomposition from the Two Halves at $n=2$](the-polar-decomposition-from-the-two-halves-at-n-2.html).

**A note on the source.** The source's text stops after the canonical Hermitian pair, although its plan lists further operator sections. The operator statements below are therefore computed from the display and verified numerically; they agree with every statement the source does make, and the place where the source is silent is marked in the body.

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, so $\operatorname{tr}A=2Q_t$ and $\det A=N=Q_t^2+B^2$. The null cone is $\det A=0$ with $A\neq0$. Its strata are
$$
\Sigma_{01}=\{\det A=0,\ B^2\neq0\},\qquad \Sigma_{00}=\{\det A=0,\ B^2=0\}.
$$
The Hermitian adjoint is $A^{\dagger}=\overline{A^{\mathsf T}}$. The Frobenius norm is $\lVert A\rVert_F$, and the scalar $a=\lVert A\rVert_F/2$ is the non-zero singular value.

**Boundaries.** The general rank trichotomy is [Introduction to the Operators on the Four Sectors in $M_2(\mathbb{C})$](introduction-to-the-operators-on-the-four-sectors-in-m2c.html). The invertible case is [One-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$](one-sided-operators-on-the-n-regular-sector-in-m2c.html). The rank-one projections are [The Spin-Half Bispinors and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinors-and-n-norm-regularity-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $A$ is the parameter matrix, $u,v$ the two slots, $a$ the singular value, $P,P'$ the rank-one projections, $\Pi$ an idempotent, $\nu$ a nilpotent, $\kappa$ the obliqueness.

## The Two Strata as Matrix Sets

**The regular stratum.** $\Sigma_{01}$ consists of the non-zero complex multiples of non-trivial idempotents:
$$
A=c\Pi,\qquad \Pi^2=\Pi,\qquad \Pi\neq0,\mathrm I_2,\qquad c=2Q_t\neq0,\qquad \operatorname{tr}\Pi=1 .
$$
A rank-one idempotent always has trace one, so $c=\operatorname{tr}A$ and $Q_t=\operatorname{tr}A/2$.

**The degenerate stratum.** $\Sigma_{00}$ consists of the non-zero nilpotents:
$$
A=\nu,\qquad \nu^2=0,\qquad \nu\neq0 .
$$
Every non-zero nilpotent matrix is similar to $\begin{pmatrix}0&1\\0&0\end{pmatrix}$, and its norm vanishes: $\det\nu=0$ and $\operatorname{tr}\nu=0$, so $Q_t=0$ and $B^2=0$.

**The example.** $A=\begin{pmatrix}0&1+2i\\0&0\end{pmatrix}$ has $\det A=0$, $\operatorname{tr}A=0$, and $A^2=0$; it is on $\Sigma_{00}$. The matrix $A=c\Pi$ with $\Pi=\frac{1}{v^{\dagger}u}uv^{\dagger}$ is on $\Sigma_{01}$ for every $c\neq0$.

## The Rank-One Decomposition

**The theorem.** A non-zero $A$ has $\det A=0$ exactly when
$$
A=2a\,uv^{\dagger},\qquad \lVert u\rVert=\lVert v\rVert=1,\qquad a>0,
$$
and then $a=\lVert A\rVert_F/2$ and $A_0=uv^{\dagger}$ is a partial isometry,
$$
A_0A_0^{\dagger}A_0=A_0,\qquad \operatorname{rank}A_0=1.
$$

**The proof.** A non-zero matrix of determinant zero has rank one, so $A=\sigma uv^{\dagger}$ with $\sigma$ the non-zero singular value; setting $2a=\sigma$ gives the form. Conversely a rank-one matrix has determinant zero. The Frobenius norm is $\lVert A\rVert_F=2a$, and $(uv^{\dagger})(vu^{\dagger})(uv^{\dagger})=uv^{\dagger}$.

**The two slots.** The vectors $u$ and $v$ are the left and the right slot of the rank-one matrix: $u$ spans the image and $v^{\dagger}$ spans the row space. They are defined up to a common phase, and the relative phase is the phase of $A$.

**The overlap.** By the cyclic property of the trace,
$$
v^{\dagger}u=\frac{\operatorname{tr}A}{2a}=\frac{2Q_t}{2a}=\frac{Q_t}{a},\qquad \lvert v^{\dagger}u\rvert\le1 .
$$
Its modulus is the cosine of the angle between the two slots. The stratum criterion is the vanishing of the overlap:
$$
\Sigma_{01}\iff v^{\dagger}u\neq0,\qquad \Sigma_{00}\iff v^{\dagger}u=0 .
$$

**The check.** On $A=\begin{pmatrix}0&1+2i\\0&0\end{pmatrix}$ the decomposition is $u=(1,0)$, $v=(0,1)$, and $v^{\dagger}u=0$, as $\Sigma_{00}$ requires. On the idempotent $A=c\Pi$ with $\Pi=uv^{\dagger}/(v^{\dagger}u)$ the overlap is $v^{\dagger}u$, and $\operatorname{tr}\Pi=1$.

## The Polar Pair

**The factorisation.** For non-zero $A$ on the null cone put
$$
a=\frac{\lVert A\rVert_F}{2},\qquad P=\frac{AA^{\dagger}}{4a^2},\qquad A_H=2aP,\qquad A_0=\frac{A}{2a}.
$$
Then $P$ is a rank-one Hermitian projection, $A_H$ is positive semidefinite of rank one with spectrum $\{0,2a\}$, $A_0$ is a partial isometry with $A_0A_0^{\dagger}=P$ and $A_0^{\dagger}A_0=P'$, and
$$
A=A_HA_0=2aA_0 .
$$
In the slots, $P=uu^{\dagger}$, $P'=vv^{\dagger}$, $A_H=2auu^{\dagger}$ and $A_0=uv^{\dagger}$; verified to $10^{-16}$.

**What it is not.** This is not the modulus–unit decomposition: $\det A=0$, so the complex modulus of the source vanishes, while $A_H$ is a non-zero rank-one matrix. The number $2a$ is the singular value, not an eigenvalue, except on the Hermitian part of $\Sigma_{01}$.

**The comparison with the invertible case.** On the N-regular sector the modulus is a scalar and the operator is a bijection; here the positive factor has rank one, and the collapse
$$
L_A=2a\,L_{A_0}
$$
is the whole content: the one-sided operator is a positive scalar times the operator of a partial isometry.

## The Closed Form on $\Sigma_{01}$

**The parameters.** Let $A=c\Pi$ with $\Pi^2=\Pi$, $\operatorname{tr}\Pi=1$ and $c\neq0$. Put
$$
\kappa=\frac{a^2}{\lvert Q_t\rvert^2}=\frac{1}{\lvert v^{\dagger}u\rvert^2}\ge1 .
$$
Then
$$
a=\lvert Q_t\rvert\sqrt{\kappa},\qquad P=\frac{\Pi\Pi^{\dagger}}{\kappa},\qquad A_H=\lvert Q_t\rvert\sqrt{\kappa}\,P,\qquad A_0=\frac{c}{\lvert c\rvert}\frac{\Pi}{\sqrt{\kappa}} .
$$
Verified on a non-Hermitian idempotent: $a=1.80156$, $\kappa=2.07721$, $\lvert v^{\dagger}u\rvert=1/\sqrt{\kappa}=0.693841$.

**The angle between the slots.** $\cos\theta=\lvert v^{\dagger}u\rvert=1/\sqrt{\kappa}$. The idempotent is Hermitian exactly when the slots coincide, $\kappa=1$ and $\cos\theta=1$; the more oblique the idempotent, the larger $\kappa$.

**The square of the normalized element.** On $\Sigma_{01}$,
$$
A_0^2=\frac{Q_t}{a}A_0,
$$
verified to $3\cdot10^{-17}$. So $A_0/(Q_t/a)=\Pi$ is an idempotent: the normalized element is a scalar times an idempotent, not a nilpotent.

**The failure at the wall.** The scalar $Q_t/a$ vanishes exactly when the overlap does, that is on $\Sigma_{00}$; there the normalized element is nilpotent and no scalar multiple of it is an idempotent.

## The Canonical Hermitian Pair on $\Sigma_{00}$

**The nilpotent form.** Write $\nu=\vec A+i\vec B$ with $\vec A,\vec B$ real, orthogonal and of equal norm $a>0$. Its matrix is
$$
A=\vec B\cdot\sigma-i\,\vec A\cdot\sigma,
$$
that is $B\cdot\sigma-iA\cdot\sigma$, and $A^2=(|B|^2-|A|^2)\mathrm I_2-2i(A\cdot B)\mathrm I_2=0$.

**The pair.** With $\vec c=\vec A\times\vec B/a^2$, a real unit vector,
$$
\Pi_+=\frac{\mathrm I_2+\vec c\cdot\sigma}{2},\qquad \Pi_-=\frac{\mathrm I_2-\vec c\cdot\sigma}{2},
$$
both Hermitian rank-one projections with $\Pi_++\Pi_-=\mathrm I_2$, $\Pi_+\Pi_-=0$. They satisfy
$$
\Pi_+A=A,\qquad A\Pi_+=0,\qquad \Pi_-A=0,\qquad A\Pi_-=A,
$$
and
$$
AA^{\dagger}=4a^2\Pi_+,\qquad A^{\dagger}A=4a^2\Pi_-,\qquad \operatorname{tr}(AA^{\dagger})=4a^2 .
$$
All the identities are immediate from $(a\cdot\sigma)(b\cdot\sigma)=a\cdot b\,\mathrm I_2+i(a\times b)\cdot\sigma$.

**The check.** For $A=\begin{pmatrix}0&1+2i\\0&0\end{pmatrix}$ the singular value is $2a=\sqrt5$, $u=(1,0)$ and $v=(0,1)$, so $\Pi_+=uu^{\dagger}=E_{11}$ and $\Pi_-=vv^{\dagger}=E_{22}$; and indeed $E_{11}A=A$ and $AE_{22}=A$.

## The One-Sided Operators

**The rank.** For $A$ of rank one, $L_A(Y)=A(Y)=2a\,u(v^{\dagger}Y)$ is zero exactly when $v^{\dagger}Y=0$. That is two independent linear conditions on $Y$, the columns of $Y$ lying in the hyperplane orthogonal to $v$. Hence
$$
\ker L_A=\{Y:v^{\dagger}Y=0\},\qquad \dim\ker L_A=2,\qquad \operatorname{rank}L_A=2 .
$$
Symmetrically $YA=2a(Yu)v^{\dagger}$ vanishes exactly when $Yu=0$, so $\ker R_A=\{Y:Yu=0\}$, also of dimension two. Verified on both strata.

**The images.** The image of $L_A$ is
$$
A M_2(\mathbb{C})=\left\{u\,w^{\dagger}:w\in\mathbb{C}^2\right\},
$$
the minimal right ideal of matrices all of whose columns are proportional to $u$, of complex dimension two; it is $A_0M_2$, a spinor space. The image of $R_A$ is $M_2A=\{z\,v^{\dagger}\}$, the minimal left ideal of matrices whose columns are proportional to $u$. On $\Sigma_{01}$ the two ideals are distinct and meet in $\mathbb{C}A$.

**The spectra.** $L_A=\mathrm I_2\otimes A$ has the eigenvalues of $A$, each twice:
$$
\Sigma_{01}:\ \operatorname{spec}L_A=\{c,c,0,0\},\qquad \Sigma_{00}:\ \operatorname{spec}L_A=\{0,0,0,0\}.
$$
Verified on both strata with agreement to $10^{-15}$.

**The Jordan types.**
$$
\Sigma_{01}:\ L_A\ \text{is diagonalizable, of type}\ \operatorname{diag}(c,c,0,0);\qquad
\Sigma_{00}:\ L_A\ \text{is nilpotent, of type}\ J_2(0)\oplus J_2(0).
$$
On $\Sigma_{01}$ the rank of $L_A-c\mathrm I_4$ is $2$, so the geometric multiplicity of $c$ is two. On $\Sigma_{00}$ the ranks of $L_A^k$ are $4,2,0$, so $L_A^2=0$ and the type is $2+2$.

**The operator of a projection.** For an idempotent $\Pi$, $L_\Pi$ is itself idempotent, $L_\Pi^2=L_{\Pi^2}=L_\Pi$, but not Hermitian unless $\Pi$ is. So $L_A$ is $2a$ times a projection of rank two, and the two-sided operator of the same $A$ is a projection of rank one: the one-sided reading keeps the rank of the slot, the two-sided one keeps the rank of the product.

## The Exponential

**The element identity survives.** Since $L_A^n=L_{A^n}$ at every point,
$$
\exp\left(tL_A\right)=L_{\exp(tA)} .
$$

**On $\Sigma_{01}$.** With $A=c\Pi$ and $\Pi^2=\Pi$,
$$
\exp(tA)=\mathrm I_2+\left(e^{tc}-1\right)\Pi,\qquad
\exp\left(tL_A\right)=\mathrm I_4+\left(e^{tc}-1\right)L_\Pi,
$$
verified to $4\cdot10^{-16}$. The group is the identity plus a multiple of a rank-two projection: a one-parameter family of affine maps along one direction of the operator space.

**On $\Sigma_{00}$.** With $A^2=0$,
$$
\exp(tA)=\mathrm I_2+tA,\qquad \exp\left(tL_A\right)=\mathrm I_4+tL_A,
$$
verified exactly. The group is a transvection, and the operator $L_A$ is its infinitesimal generator.

**The contrast.** On $\Sigma_{01}$ the group has the eigenvalue $e^{tc}$ twice and $1$ twice; on $\Sigma_{00}$ it is unipotent with a single eigenvalue $1$ and two blocks of size two.

## Worked Examples

**A Hermitian idempotent.** $A=\operatorname{diag}(2,0)$: $\Pi=\operatorname{diag}(1,0)$, $c=2$, $a=1$, $\kappa=1$, $v^{\dagger}u=1$. Then $L_A=\operatorname{diag}(2,2,0,0)$ in the appropriate basis, of rank two, and $\exp(tL_A)=\operatorname{diag}(e^{2t},e^{2t},1,1)$.

**A non-Hermitian idempotent.** The idempotent of the closed-form section has $\kappa=2.07721>1$, so the two slots are at an angle $\arccos(1/\sqrt\kappa)\approx46.6^{\circ}$.

**The standard nilpotent.** $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$: $L_A$ has rank two and $L_A^2=0$, so its type is $J_2(0)\oplus J_2(0)$, and $\exp(tL_A)=\mathrm I_4+tL_A$.

**A complex scalar multiple.** $A=c\Pi$ with $\Pi$ Hermitian: $\kappa=1$, $a=|Q_t|$, and the exponential is $\mathrm I_4+(e^{tc}-1)L_\Pi$.

## Where $n=2$ Differs

**The rank.** At $n=2$ a singular non-zero matrix has rank one, so the singular value decomposition has one term and the partial isometry is $uv^{\dagger}$. At order $n$ the rank can be anything from $1$ to $n-1$ and the decomposition has that many terms; the one-sided operator then has rank $2r$ and kernel of dimension $n^2-2r$.

**The strata.** At $n=2$ the null cone splits into exactly two strata, $\Sigma_{01}$ and $\Sigma_{00}$; there is no third. At order $n$ the discriminant is a form on a larger space and the Jordan types are partitions of $n^2$.

**The canonical pair.** At $n=2$ the nilpotent determines exactly two canonical rank-one projections $\Pi_\pm$, and they are the whole Peirce decomposition. At order $n$ a nilpotent of rank $r$ has a Peirce decomposition with more corners.

**What does not differ.** The scalar collapse $L_A=2a\,L_{A_0}$, the rank $2r$, the minimal ideals as images and the element identity for the exponential hold at every order.

## Summary

On the null cone $\det A=0$, $A\neq0$, the matrix is rank one, $A=2auv^{\dagger}$ with $a=\lVert A\rVert_F/2$, and the overlap $v^{\dagger}u=\operatorname{tr}A/(2a)$ distinguishes the strata: $\Sigma_{01}$ has $v^{\dagger}u\neq0$ and $\Sigma_{00}$ has $v^{\dagger}u=0$. The polar pair is $P=uu^{\dagger}$, $A_H=2auu^{\dagger}$, $A_0=uv^{\dagger}$, and $A=A_HA_0=2aA_0$.

On $\Sigma_{01}$ the matrix is $c\Pi$ with $\Pi$ idempotent, $a=|Q_t|\sqrt\kappa$, $\cos\theta=1/\sqrt\kappa$, and $A_0^2=(Q_t/a)A_0$. On $\Sigma_{00}$ the canonical pair $\Pi_\pm=(\mathrm I_2\pm c\cdot\sigma)/2$ satisfies $\Pi_+A=A$ and $A\Pi_-=A$, with $AA^{\dagger}=4a^2\Pi_+$.

The one-sided operators have rank $2$, kernel of dimension two, and images the minimal right and left ideals $AM_2$ and $M_2A$. Their spectra are $c,c,0,0$ and $0,0,0,0$; their Jordan types are $\operatorname{diag}(c,c,0,0)$ and $J_2(0)\oplus J_2(0)$. The exponential is $\mathrm I_4+(e^{tc}-1)L_\Pi$ on $\Sigma_{01}$ and $\mathrm I_4+tL_A$ on $\Sigma_{00}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | the parameter matrix on the null cone |
| $u,v$ | the left and right slots |
| $a=\lVert A\rVert_F/2$ | the non-zero singular value |
| $P,P'$ | $uu^{\dagger}$ and $vv^{\dagger}$ |
| $\Pi$ | the idempotent with $A=c\Pi$ on $\Sigma_{01}$ |
| $\nu$ | the nilpotent on $\Sigma_{00}$ |
| $\kappa=a^2/|Q_t|^2$ | the obliqueness |
| $\Pi_\pm$ | the canonical Hermitian pair |

## Further Reading

- [One-Sided Operators on the N-Degenerate Sector](one-sided-operators-on-the-n-degenerate-sector.html), for the source's rank-one decomposition and its two strata.
- [Two-Sided Operators on the N-Degenerate Sector in $M_2(\mathbb{C})$](two-sided-operators-on-the-n-degenerate-sector-in-m2c.html), for the rank-one two-sided operator and its single Jordan chain.
- [One-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$](one-sided-operators-on-the-n-regular-sector-in-m2c.html), for the invertible case that this article deforms.
- [The Polar Decomposition from the Two Halves at $n=2$](the-polar-decomposition-from-the-two-halves-at-n-2.html), for the polar decomposition of a singular matrix.
- [Introduction to the Operators on the Four Sectors in $M_2(\mathbb{C})$](introduction-to-the-operators-on-the-four-sectors-in-m2c.html), for the four sector table in one page.
