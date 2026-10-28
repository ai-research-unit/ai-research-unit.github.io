# __The Exponential and the Lie Group__

## Introduction

**The exponential map $\exp:\mathfrak{gl}_4(\mathbb{C})\to GL_4(\mathbb{C})$ is the bridge between the Lie algebra and the Lie group.** It is defined by the convergent power series, it is a local diffeomorphism at the origin, it is surjective over $\mathbb{C}$, and it is not injective. The Lie algebra $\mathfrak{gl}_4$ is the tangent space at the identity with the commutator bracket; the group $GL_4$ is a connected complex Lie group of real dimension $32$, with maximal compact subgroup $U(4)$.

The article defines the exponential, proves its elementary properties and the determinant formula, describes the differential and the Baker–Campbell–Hausdorff formula, identifies the Lie algebras of the classical subgroups, and describes the global structure of $GL_4$.

The polar decomposition is *The Polar Decomposition*; the exponential polar decomposition is *The Exponential Polar Decomposition*; the topology is *The Topology of $M_4(\mathbb{C})$*; the one-parameter subgroups of the compact group are in *The Exponential and the Lie Group* of the biquaternion corpus.

## The Exponential Map

**Definition.** For $X\in M_4(\mathbb{C})$, the **exponential** is

$$
e^X=\exp(X)=\sum_{n=0}^{\infty}\frac{X^n}{n!}=I+X+\frac{X^2}{2!}+\frac{X^3}{3!}+\cdots.
$$

The series converges absolutely and uniformly on compact subsets of $M_4$, because $\lVert X^n/n!\rVert\le\lVert X\rVert^n/n!$.

**Proposition.** The exponential satisfies

$$
e^0=I,\qquad
e^{-X}=(e^X)^{-1},\qquad
e^{SXS^{-1}}=Se^XS^{-1},
$$

and, if $[X,Y]=0$,

$$
e^{X+Y}=e^Xe^Y.
$$

In general $e^{X+Y}\ne e^Xe^Y$; the correction is the Baker–Campbell–Hausdorff series.

**Proof.** The identities follow from the series and the absolute convergence. For commuting $X,Y$, the binomial theorem gives $(X+Y)^n=\sum_k\binom{n}{k}X^kY^{n-k}$, and the series factors. The inverse is $e^{-X}$ because $X$ and $-X$ commute. The conjugation formula is termwise.

**The determinant.** For every $X$,

$$
\det e^X=e^{\operatorname{tr}X}.
$$

**Proof.** The determinant is the product of the eigenvalues; if $\lambda_1,\dots,\lambda_4$ are the eigenvalues of $X$, then $e^{\lambda_1},\dots,e^{\lambda_4}$ are the eigenvalues of $e^X$, and

$$
\det e^X=\prod_{k=1}^{4}e^{\lambda_k}=e^{\sum\lambda_k}=e^{\operatorname{tr}X}.
$$

The identity also follows from the Jacobi formula $\frac{d}{dt}\det e^{tX}=\operatorname{tr}(X)\det e^{tX}$ and the value $1$ at $t=0$.

**The eigenvalues.** If $X=SJS^{-1}$ is the Jordan form, then

$$
e^X=Se^JS^{-1}.
$$

For a Jordan block $J_n(\lambda)=\lambda I+N$,

$$
e^{J_n(\lambda)}=e^\lambda e^N
=e^\lambda\Bigl(I+N+\frac{N^2}{2!}+\cdots+\frac{N^{n-1}}{(n-1)!}\Bigr),
$$

because $N^n=0$. The exponential of a nilpotent is unipotent; the exponential of a semisimple is semisimple with exponentiated eigenvalues.

**Example.** For the root

$$
H=\operatorname{diag}(1,i,-1,-i),
$$

the exponential is

$$
e^{tH}=\operatorname{diag}(e^t,e^{it},e^{-t},e^{-it}),
$$

a one-parameter subgroup of $GL_4$ whose compact part is a circle and whose noncompact part is a line. For the nilpotent $N=E_{12}$,

$$
e^{tN}=I+tN,
$$

a unipotent one-parameter subgroup.

## The Differential and the Local Structure

**The derivative at the origin.** The differential of the exponential at $0$ is the identity:

$$
d(\exp)_0(Y)=\frac{d}{dt}\Big|_{t=0}e^{tY}=Y.
$$

Hence the exponential is a local diffeomorphism near $0$: there are neighbourhoods $U$ of $0$ in $\mathfrak{gl}_4$ and $V$ of $I$ in $GL_4$ such that $\exp:U\to V$ is a diffeomorphism.

**The differential at $X$.** For general $X$,

$$
d(\exp)_X(Y)=e^X\sum_{n=0}^{\infty}\frac{(-1)^n}{(n+1)!}\operatorname{ad}_X^n(Y)
=e^X\frac{1-e^{-\operatorname{ad}_X}}{\operatorname{ad}_X}(Y).
$$

The operator $\operatorname{ad}_X$ is $Y\mapsto[X,Y]$.

**The critical points.** The differential $d(\exp)_X$ is singular exactly when $\operatorname{ad}_X$ has an eigenvalue in $2\pi i\mathbb{Z}\setminus\{0\}$, equivalently when two eigenvalues of $X$ differ by a nonzero multiple of $2\pi i$. At such a point the exponential is not a local diffeomorphism; the image can have a singularity.

**The Baker–Campbell–Hausdorff formula.** Near $0$,

$$
\log(e^Xe^Y)=X+Y+\frac12[X,Y]+\frac1{12}[X,[X,Y]]-\frac1{12}[Y,[X,Y]]+\cdots.
$$

The series involves only iterated commutators. It shows that the Lie algebra structure determines the group structure locally: the product near the identity is reconstructed from the bracket.

**The inverse.** The inverse of the exponential near $0$ is the **logarithm**, defined by the series

$$
\log(I+Z)=\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}Z^n
$$

for $\lVert Z\rVert<1$, and extended by the Jordan form and a branch of the logarithm to every invertible matrix.

## The Lie Algebra and the Lie Group

**The Lie algebra.** The Lie algebra of $GL_4(\mathbb{C})$ is

$$
\mathfrak{gl}_4(\mathbb{C})=M_4(\mathbb{C}),
$$

with the commutator bracket

$$
[X,Y]=XY-YX.
$$

The Lie algebra is the tangent space at the identity, and the exponential is the flow of the left-invariant vector fields. Its complex dimension is $16$ and its real dimension is $32$.

**The Lie group.** The group $GL_4(\mathbb{C})$ is a complex Lie group: it is an open subset of $M_4(\mathbb{C})\cong\mathbb{C}^{16}$, and the multiplication and inversion are holomorphic. Its real dimension is $32$; it is connected but not compact.

**The Lie correspondence.** The exponential is the map from the Lie algebra to the Lie group. The one-parameter subgroups are exactly the maps

$$
\gamma_X:\mathbb{R}\longrightarrow GL_4,\qquad
\gamma_X(t)=e^{tX},
$$

for $X\in\mathfrak{gl}_4$. Every continuous group homomorphism $\mathbb{R}\to GL_4$ is of this form. The Lie algebra is the set of these generators.

**The closed subgroup theorem.** A closed subgroup of $GL_4$ is a Lie subgroup, and its Lie algebra is the set of $X$ with $e^{tX}$ in the subgroup for all $t$. The classical subgroups are:

| Group | Lie algebra | Real dimension | Condition |
|---|---|---|---|
| $GL_4(\mathbb{C})$ | $\mathfrak{gl}_4(\mathbb{C})$ | $32$ | invertible |
| $SL_4(\mathbb{C})$ | $\mathfrak{sl}_4(\mathbb{C})$ | $30$ | $\det=1$, $\operatorname{tr}X=0$ |
| $U(4)$ | $\mathfrak{u}(4)$ | $16$ | $U^*U=I$, $X^*=-X$ |
| $SU(4)$ | $\mathfrak{su}(4)$ | $15$ | $\det=1$, $X^*=-X$, $\operatorname{tr}X=0$ |
| $T=(\mathbb{C}^\times)^4$ | diagonal matrices | $8$ real | diagonal |
| $B$ upper triangular | upper triangular | $20$ real | triangular |

**The exponential and the subgroups.** The exponential maps

$$
\mathfrak{sl}_4\longrightarrow SL_4,\qquad
\mathfrak{u}(4)\longrightarrow U(4),\qquad
\mathfrak{su}(4)\longrightarrow SU(4),
$$

because $\det e^X=e^{\operatorname{tr}X}$ and $(e^X)^*=e^{X^*}$. The exponential of a traceless matrix has determinant one; the exponential of a skew-Hermitian matrix is unitary; the exponential of a Hermitian matrix is positive definite.

**The polar decomposition.** Every invertible $A$ is

$$
A=UP=e^{iK}e^H,
$$

with $K,H$ Hermitian. The unitary factor is the exponential of a skew-Hermitian matrix $iK$, and the positive factor is the exponential of the Hermitian matrix $H$. The polar decomposition is the global Cartan decomposition of the group.

## Surjectivity and Non-Injectivity

**Theorem (surjectivity over $\mathbb{C}$).** Every invertible complex matrix has a logarithm:

$$
\exp:\mathfrak{gl}_4(\mathbb{C})\longrightarrow GL_4(\mathbb{C})
$$

is surjective.

**Proof.** By the Jordan form, it suffices to define the logarithm on a Jordan block $J_n(\lambda)$ with $\lambda\ne0$. Write $J_n(\lambda)=\lambda(I+N/\lambda)$ with $N$ nilpotent. Choose a logarithm $\mu$ of $\lambda$ and set

$$
\log J_n(\lambda)=\mu I+\log(I+N/\lambda)
=\mu I+\sum_{k=1}^{n-1}\frac{(-1)^{k+1}}{k}\Bigl(\frac{N}{\lambda}\Bigr)^k.
$$

The series is finite because $N^n=0$, and its exponential is $J_n(\lambda)$. Summing over the Jordan blocks and conjugating gives a logarithm of $A$.

**Non-injectivity.** The exponential is not injective. For example,

$$
e^{2\pi i I}=I,
$$

and more generally every matrix $X$ that is diagonalisable with eigenvalues in $2\pi i\mathbb{Z}$ satisfies $e^X=I$. The fibre over $I$ is the union of the conjugacy classes of

$$
\operatorname{diag}(2\pi i k_1,\dots,2\pi i k_4),\qquad k_j\in\mathbb{Z}.
$$

The fibre is not a subgroup of the additive group, because the exponential is not a homomorphism on non-commuting matrices.

**The principal logarithm.** On the domain of matrices with no eigenvalues on the closed negative real axis, the **principal logarithm** is holomorphic and satisfies $e^{\log A}=A$. It is the inverse of the exponential on a neighbourhood of $I$, extended by the spectral calculus.

**The image of the exponential.** The image is all of $GL_4(\mathbb{C})$; the exponential is a surjective local diffeomorphism. It is not a covering map, because the fibre over $I$ is not discrete (it contains the continuous family of diagonalisable matrices with eigenvalues $2\pi i k$? The set of eigenvalues is discrete, but the conjugating matrix varies continuously; the fibre is a union of conjugacy classes of dimension up to $12$, not discrete). The exponential is not a covering.

## The Global Structure of $GL_4$

**Connectedness.** The Lie algebra $\mathfrak{gl}_4$ is connected, and the exponential is continuous and surjective, so $GL_4(\mathbb{C})$ is connected.

**The maximal compact subgroup.** The unitary group $U(4)$ is a maximal compact subgroup of $GL_4(\mathbb{C})$. The polar decomposition gives the diffeomorphism

$$
GL_4(\mathbb{C})\cong U(4)\times P_+,
$$

and $P_+$ is contractible. Hence $GL_4$ deformation retracts onto $U(4)$.

**The fundamental group.** Because $GL_4$ deformation retracts onto $U(4)$,

$$
\pi_1(GL_4(\mathbb{C}))\cong\pi_1(U(4))\cong\mathbb{Z}.
$$

The generator is the loop $t\mapsto\operatorname{diag}(e^{2\pi i t},1,1,1)$; the scalar loop $e^{2\pi i t}I$ is four times the generator, and its determinant has winding four. The universal cover is a complex Lie group; the details are in *The Topology of $M_4(\mathbb{C})$*.

**The centre.** The centre of $GL_4$ is $\mathbb{C}^\times I$, and the centre of $U(4)$ is $U(1)I$. The projective group is

$$
PGL_4=GL_4/\mathbb{C}^\times I,
$$

of dimension $15$; the projective unitary group is $PU(4)=U(4)/U(1)I$, of dimension $15$.

**The Lie algebra centre.** The centre of $\mathfrak{gl}_4$ is $\mathbb{C}I$, of dimension $1$; the traceless algebra $\mathfrak{sl}_4$ has dimension $15$ and is the Lie algebra of $SL_4$ and of $PGL_4$.

## The Exponential of the Root and the Torus

**The root generates a torus.** The root

$$
H=\operatorname{diag}(1,i,-1,-i)
$$

has exponential

$$
e^{tH}=\operatorname{diag}(e^t,e^{it},e^{-t},e^{-it}).
$$

The compact part $e^{it}$ and $e^{-it}$ lies in $U(1)$, and the real part $e^t,e^{-t}$ lies in $\mathbb{R}_{>0}$. The one-parameter subgroup is not contained in a compact group, because of the real eigenvalues $\pm1$; the compact part is the circle generated by $i$ and $-i$.

**The compact torus.** The diagonal matrices

$$
\operatorname{diag}(e^{i\theta_1},e^{i\theta_2},e^{i\theta_3},e^{i\theta_4})
$$

form the maximal torus $T^4$ of $U(4)$, of real dimension $4$. The quotient by the diagonal $U(1)$ is the maximal torus of $PU(4)$, of dimension $3$, the gauge torus of *The Frame, the Simple Nilpotents and the Gauge*.

**The nilpotent exponential.** For the simple nilpotents,

$$
e^{tE_{12}}=I+tE_{12},\qquad
e^{tE_{23}}=I+tE_{23},\qquad
e^{tE_{34}}=I+tE_{34},
$$

unipotent one-parameter subgroups. The products $e^{t_1E_{12}}e^{t_2E_{23}}e^{t_3E_{34}}$ form the maximal unipotent subgroup of the upper triangular Borel.

## The Biquaternion Case

**At $n=2$ the same theorem.** For $M_2(\mathbb{C})$,

$$
\exp:\mathfrak{gl}_2(\mathbb{C})\longrightarrow GL_2(\mathbb{C})
$$

is surjective and not injective; the Lie group $GL_2$ has real dimension $8$, the maximal compact $U(2)$ has dimension $4$, and

$$
\pi_1(GL_2)=\mathbb{Z}.
$$

The biquaternion algebra's exponential is the same exponential on $2\times2$ matrices; the regular model embeds it in $M_4$.

**The comparison.** The exponential of the full algebra is the $4\times4$ exponential; the biquaternion exponential is the $2\times2$ exponential. The Lie algebra dimensions are $32$ and $8$; the Lie groups are $GL_4$ and $GL_2$. The exponential is surjective in both cases over $\mathbb{C}$.

## Summary

The exponential $e^X=\sum X^n/n!$ maps the Lie algebra $\mathfrak{gl}_4$ to the Lie group $GL_4$. It satisfies $e^{X+Y}=e^Xe^Y$ for commuting $X,Y$, $e^{-X}=(e^X)^{-1}$, $\det e^X=e^{\operatorname{tr}X}$, and $e^{SXS^{-1}}=Se^XS^{-1}$. Its differential at $0$ is the identity, so it is a local diffeomorphism near $0$; at $X$ the differential is $e^X(1-e^{-\operatorname{ad}_X})/\operatorname{ad}_X$, singular exactly when two eigenvalues of $X$ differ by a nonzero multiple of $2\pi i$. The Baker–Campbell–Hausdorff series reconstructs the local group from the bracket. Over $\mathbb{C}$ the exponential is surjective onto $GL_4$ and not injective; the fibre over $I$ contains the conjugates of the diagonal matrices with eigenvalues in $2\pi i\mathbb{Z}$. The group $GL_4$ is connected, of real dimension $32$, with maximal compact $U(4)$, polar decomposition $GL_4\cong U(4)\times P_+$, and fundamental group $\mathbb{Z}$; it deformation retracts onto $U(4)$. The Lie algebras of $SL_4,U(4),SU(4)$ are $\mathfrak{sl}_4,\mathfrak{u}(4),\mathfrak{su}(4)$, of real dimensions $30,16,15$. The root generates the one-parameter subgroup $\operatorname{diag}(e^t,e^{it},e^{-t},e^{-it})$, the nilpotents generate unipotent subgroups, and the compact diagonal torus is the gauge torus of the frame.

$$
\boxed{\ \exp:\mathfrak{gl}_4\to GL_4\ \text{surjective},\quad \det e^X=e^{\operatorname{tr}X},\quad d(\exp)_0=I,\quad GL_4\simeq U(4),\quad \pi_1(GL_4)=\mathbb{Z}. }
$$

| Group | Lie algebra | Real dimension |
|---|---|---|
| $GL_4(\mathbb{C})$ | $\mathfrak{gl}_4$ | $32$ |
| $SL_4(\mathbb{C})$ | $\mathfrak{sl}_4$ | $30$ |
| $U(4)$ | $\mathfrak{u}(4)$ | $16$ |
| $SU(4)$ | $\mathfrak{su}(4)$ | $15$ |
| $PGL_4$ | $\mathfrak{sl}_4$ | $30$ |
| $PU(4)$ | $\mathfrak{su}(4)$ | $15$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e^X=\exp(X)$ | the matrix exponential |
| $\mathfrak{gl}_4$ | the Lie algebra of $GL_4$ |
| $\operatorname{ad}_X(Y)=[X,Y]$ | the adjoint operator |
| $d(\exp)_X$ | the differential of the exponential |
| $\operatorname{BCH}$ | the Baker–Campbell–Hausdorff series |
| $P_+$ | the positive definite cone |
| $T^4$ | the maximal torus of $U(4)$ |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the exponential map, the BCH formula, the closed subgroup theorem and the classical groups.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the Cartan decomposition and the global structure of $GL_4$.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the matrix exponential, the logarithm and the Jordan form.
- [The Polar Decomposition](the-polar-decomposition-of-m4c.html), for the diffeomorphism $GL_4\cong U(4)\times P_+$.
- [The Exponential Polar Decomposition](the-exponential-polar-decomposition-of-m4c.html), for the ordering $e^He^{iK}$.
- [The Topology of $M_4(\mathbb{C})$](the-topology-of-m4c.html), for the fundamental group and the homotopy type.
- [The Frame, the Simple Nilpotents and the Gauge](the-frame-the-simple-nilpotents-and-the-gauge-of-m4c.html), for the gauge torus and the nilpotents.
