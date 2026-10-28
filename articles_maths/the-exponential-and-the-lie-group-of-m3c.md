# __The Exponential and the Lie Group of $M_3(\mathbb{C})$__

## Introduction

**The exponential map $\exp:\mathfrak{gl}_3(\mathbb{C})\to GL_3(\mathbb{C})$ is entire, surjective, and not injective.** It is defined by the norm-convergent series

$$
\exp X=\sum_{n=0}^{\infty}\frac{X^{n}}{n!}=I+X+\frac{X^{2}}{2}+\frac{X^{3}}{6}+\cdots,
$$

and it carries the Lie algebra structure of $M_3$ under the commutator to the group structure of $GL_3$:

$$
\exp(X)\exp(Y)=\exp\big(X+Y+\tfrac12[X,Y]+\tfrac1{12}[X,[X,Y]]-\tfrac1{12}[Y,[X,Y]]+\cdots\big).
$$

The differential at the identity is the identity, so $\exp$ is a local diffeomorphism near $0$; it is surjective onto $GL_3(\mathbb{C})$ but not injective, because it is periodic. The eigenvalues of $\exp X$ are $e^{\lambda}$ for the eigenvalues $\lambda$ of $X$, and

$$
\det\exp X=e^{\operatorname{tr}X}.
$$

The real Lie algebra $\mathfrak{gl}_3$ has dimension $18$; the group $GL_3(\mathbb{C})$ has real dimension $18$; the $*$-unitary subgroup $U(3)$ has dimension $9$ and its Lie algebra $\mathfrak{u}(3)$ consists of the skew-Hermitian matrices; the special linear group $SL_3$ and its Lie algebra $\mathfrak{sl}_3$ have complex dimension $8$, and $\mathfrak{su}(3)$ has real dimension $8$.

The article defines the exponential, computes it on the Jordan forms, proves the determinant and eigenvalue formulas, proves surjectivity and the failure of injectivity, describes the one-parameter subgroups and the Lie algebra, computes the root and the gauge in exponential coordinates, and works explicit matrices. The polar decomposition is *The Polar Decomposition of $M_3(\mathbb{C})$*; the combined exponential polar form is *The Exponential Polar Decomposition of $M_3(\mathbb{C})$*; the analysis of the map is *Analysis on $M_3(\mathbb{C})$*.

## Definition and Convergence

**Definition.** For $X\in M_3(\mathbb{C})$ the exponential is the sum of the series above.

**Proposition.** The series converges absolutely for every $X$, uniformly on compact sets, and defines a holomorphic map $\mathfrak{gl}_3\to M_3$.

**Proof.** For $\|X\|\le R$ the norm of the $n$-th term is at most $R^{n}/n!$, and the scalar series converges. Each matrix entry is an entire function of the entries of $X$, because it is a uniform limit of polynomials. The map is therefore holomorphic, and the derivative is obtained by differentiating term by term.

**Proposition.** If $[X,Y]=0$ then $\exp(X+Y)=\exp X\exp Y$. In particular $\exp X$ is invertible, with inverse $\exp(-X)$, and $\exp((s+t)X)=\exp(sX)\exp(tX)$.

**Proof.** When $X$ and $Y$ commute, the binomial theorem applies to $(X+Y)^{n}$, and the Cauchy product of the two exponential series gives the exponential of the sum. The inverse is $\exp(-X)$ because $X$ commutes with $-X$.

**The derivative.** The right-trivialized differential of $\exp$ at $X$ is

$$
d\exp_X(Y)\,e^{-X}
=\sum_{n=0}^{\infty}\frac{1}{(n+1)!}\operatorname{ad}_X^{n}(Y)
=\frac{e^{\operatorname{ad}_X}-1}{\operatorname{ad}_X}(Y),
$$

where $\operatorname{ad}_X(Y)=[X,Y]$; the derivative itself is this expression multiplied on the right by $e^{X}$. At $X=0$ it is $Y$, so $\exp$ is a local diffeomorphism near $0$.

**Proof.** This is the standard derivative formula for the exponential map; see Hall, *Lie Groups, Lie Algebras, and Representations*, Theorem 3.35. The right multiplication by $e^{-X}$ is invertible, so the invertibility of $d\exp_X$ is the invertibility of the displayed operator.

**The BCH formula.** Near $0$, the product $\exp X\exp Y$ is the exponential of

$$
X+Y+\frac12[X,Y]+\frac1{12}[X,[X,Y]]-\frac1{12}[Y,[X,Y]]+\cdots .
$$

The series is the Baker–Campbell–Hausdorff series; on a nilpotent Lie algebra it terminates, and on $\mathfrak{gl}_3$ it does not.

## Eigenvalues and Determinant

**Theorem.** Let $X$ have eigenvalues $\lambda_1,\lambda_2,\lambda_3$, counted with algebraic multiplicity. Then $\exp X$ has eigenvalues $e^{\lambda_1},e^{\lambda_2},e^{\lambda_3}$, and

$$
\det\exp X=e^{\lambda_1+\lambda_2+\lambda_3}=e^{\operatorname{tr}X}.
$$

**Proof.** Put $X$ in Jordan form $X=S(J_1\oplus J_2\oplus J_3)S^{-1}$ with $J_k=\lambda_kI+N_k$. Then $\exp X=S(\exp J_1\oplus\exp J_2\oplus\exp J_3)S^{-1}$, and on a block of size $m$,

$$
\exp(\lambda I+N)=e^{\lambda}\Big(I+N+\frac{N^{2}}{2!}+\cdots+\frac{N^{m-1}}{(m-1)!}\Big),
$$

because $N^{m}=0$. The eigenvalues of the block are $e^{\lambda}$, with multiplicity $m$. The determinant is the product of the eigenvalues, $e^{\lambda_1+\lambda_2+\lambda_3}=e^{\operatorname{tr}X}$.

**The Jordan form of the exponential.** The exponential of a Jordan block of size $m$ is $e^{\lambda}$ times the unipotent block $I+N+\cdots+N^{m-1}/(m-1)!$. It is diagonalisable exactly when $N=0$, that is, when the block was scalar. For $N\neq0$ the unipotent factor is a single Jordan block, so the exponential preserves the Jordan type of each block: it shifts the eigenvalue $\lambda$ to $e^{\lambda}$ and keeps the block size. Different Jordan types are not identified; the non-injectivity comes only from the ambiguity of the logarithm, not from a collapse of the Jordan structure.

**The Hermitian and skew-Hermitian cases.** If $X$ is Hermitian, then $\exp X$ is positive definite Hermitian. If $X$ is skew-Hermitian, then $\exp X$ is $*$-unitary. If $X$ is traceless and skew-Hermitian, then $\exp X\in SU(3)$.

**Proof.** For Hermitian $X$, diagonalise $X=UDU^{*}$ with real $D$; then $\exp X=Ue^{D}U^{*}$ with $e^{D}$ real positive diagonal, which is positive definite Hermitian. For skew-Hermitian $X$, $(\exp X)^{*}=\exp(X^{*})=\exp(-X)=(\exp X)^{-1}$. The determinant is $e^{\operatorname{tr}X}=1$ when $\operatorname{tr}X=0$.

**Worked example.** For

$$
X=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}
$$

one has $X^{2}=E_{13}$, $X^{3}=0$, and

$$
\exp X=I+X+\frac{X^{2}}{2}
=\begin{pmatrix}1&1&\tfrac12\\0&1&1\\0&0&1\end{pmatrix}.
$$

The eigenvalues are all $1$, the determinant is $1$, and the matrix is unipotent. For

$$
X=\begin{pmatrix}0&1&0\\0&0&0\\0&0&0\end{pmatrix}
$$

one has $X^{2}=0$ and $\exp X=I+X=\begin{pmatrix}1&1&0\\0&1&0\\0&0&1\end{pmatrix}$.

## Surjectivity and Injectivity

**Theorem (surjectivity).** Every invertible $A\in GL_3(\mathbb{C})$ is $\exp X$ for some $X\in\mathfrak{gl}_3(\mathbb{C})$. The exponential is surjective onto $GL_3(\mathbb{C})$.

**Proof.** Put $A$ in Jordan form $A=S(J_1\oplus J_2\oplus J_3)S^{-1}$. On a block $J=\lambda I+N$ with $\lambda\neq0$ and $N^{m}=0$, define

$$
\log J=(\log\lambda)I+\frac{N}{\lambda}-\frac{N^{2}}{2\lambda^{2}}+\cdots+\frac{(-1)^{m-1}N^{m-1}}{(m-1)\lambda^{m-1}} .
$$

For $m\le3$ this is $(\log\lambda)I+N/\lambda-N^{2}/(2\lambda^{2})$. The series is finite because $N$ is nilpotent, and $\exp(\log J)=J$ by the functional identity $\exp(\log(1+z))=1+z$ applied to the nilpotent $z=N/\lambda$. Then $X=S(\log J_1\oplus\log J_2\oplus\log J_3)S^{-1}$ satisfies $\exp X=A$.

**Theorem (kernel).** $\exp X=I$ if and only if $X$ is diagonalisable and its eigenvalues lie in $2\pi i\mathbb{Z}$.

**Proof.** If $X$ is diagonalisable with eigenvalues $2\pi i k_j$, then $\exp X=I$ because $e^{2\pi i k}=1$. Conversely, if $\exp X=I$, then the minimal polynomial of $X$ divides $e^{t}-1$, which has distinct roots $2\pi i k$; hence $X$ is diagonalisable and its eigenvalues are of that form.

**Examples of non-injectivity.** The scalar $X=2\pi i I$ satisfies $\exp X=I$. The matrix $X=\operatorname{diag}(2\pi i,0,0)$ also satisfies $\exp X=I$, so the fibre of the exponential over $I$ is infinite: it contains every diagonal matrix with entries in $2\pi i\mathbb{Z}$. The exponential is a covering map from a neighbourhood of $0$ onto a neighbourhood of $I$, but not globally.

**The real case.** Over $\mathbb{R}$ the exponential $\mathfrak{gl}_3(\mathbb{R})\to GL_3(\mathbb{R})$ is not surjective: $\det\exp X=e^{\operatorname{tr}X}>0$, so a matrix with negative determinant is not in the image. Even on $GL_3(\mathbb{R})^{+}$ the exponential is not surjective: the matrix $J_2(-1)\oplus(1)$ has determinant $1$, but a real logarithm $X$ would have the eigenvalue $(2k+1)\pi i$ with a Jordan block of size $2$, and hence also its complex conjugate with a Jordan block of size $2$; that needs at least four dimensions, and the matrix has three. Over $\mathbb{C}$ these obstructions disappear, because every nonzero complex number has a logarithm.

**The critical set.** The differential $d\exp_X$ is singular exactly when two eigenvalues of $\operatorname{ad}_X$ differ by $2\pi i k$ with $k\in\mathbb{Z}\setminus\{0\}$, that is, when

$$
\lambda_i-\lambda_j\in 2\pi i\mathbb{Z}\setminus\{0\}
$$

for some pair of eigenvalues of $X$. At those points the exponential is not a local diffeomorphism.

**Proof.** The eigenvalues of $\operatorname{ad}_X$ are the differences $\lambda_i-\lambda_j$. The factor $(e^{z}-1)/z$ vanishes exactly at the nonzero multiples of $2\pi i$, so $d\exp_X$ is singular exactly when some difference is such a multiple.

## One-Parameter Subgroups

**Definition.** A **one-parameter subgroup** of $GL_3(\mathbb{C})$ is a continuous homomorphism $\gamma:\mathbb{R}\to GL_3(\mathbb{C})$.

**Theorem.** Every one-parameter subgroup is of the form

$$
\gamma(t)=\exp(tX),\qquad X=\gamma'(0)\in\mathfrak{gl}_3 .
$$

**Proof.** This is the standard theorem of Lie group theory: a continuous one-parameter subgroup is smooth, and its derivative at $0$ determines it by the differential equation $\gamma'(t)=X\gamma(t)$ with $\gamma(0)=I$. The solution is the exponential. The proof for matrix groups is elementary: $\gamma$ is differentiable because it is continuous and measurable, and the uniqueness of the solution of the linear ODE gives the formula.

**The flow.** For fixed $X$, the map $t\mapsto\exp(tX)$ is the flow of the left-invariant vector field $Y\mapsto XY$ on $GL_3$. In coordinates,

$$
\exp(tX)=I+tX+\frac{t^{2}X^{2}}{2}+\cdots,
$$

and the derivative at $t=0$ is $X$.

**Examples.** For $X=\operatorname{diag}(1,2,4)$,

$$
\exp(tX)=\operatorname{diag}(e^{t},e^{2t},e^{4t}).
$$

For $X=E_{12}$,

$$
\exp(tX)=I+tE_{12}=\begin{pmatrix}1&t&0\\0&1&0\\0&0&1\end{pmatrix},
$$

a shear. For $X=i\operatorname{diag}(0,2\pi/3,4\pi/3)$,

$$
\exp(tX)=\operatorname{diag}(1,e^{2\pi it/3},e^{4\pi it/3}),
$$

a circle inside the diagonal torus, which at $t=1$ gives the diagonal root.

## The Lie Algebra

**Definition.** The Lie algebra of $GL_3(\mathbb{C})$ is $\mathfrak{gl}_3=M_3(\mathbb{C})$ with the bracket $[X,Y]=XY-YX$.

**The dimensions.** Over $\mathbb{R}$,

$$
\dim\mathfrak{gl}_3=18,\qquad
\dim\mathfrak{u}(3)=9,\qquad
\dim\mathfrak{su}(3)=8,\qquad
\dim\mathfrak{so}(3)=3,
$$

and over $\mathbb{C}$,

$$
\dim_\mathbb{C}\mathfrak{gl}_3=9,\qquad
\dim_\mathbb{C}\mathfrak{sl}_3=8.
$$

**The subalgebras.** The bracket preserves the following subspaces:

- $\mathfrak{sl}_3=\{X:\operatorname{tr}X=0\}$, of complex dimension $8$, the Lie algebra of $SL_3$;
- $\mathfrak{u}(3)=\{X:X^{*}=-X\}$, of real dimension $9$, the Lie algebra of $U(3)$;
- $\mathfrak{su}(3)=\mathfrak{u}(3)\cap\mathfrak{sl}_3$, of real dimension $8$, the Lie algebra of $SU(3)$;
- $\mathfrak{so}(3)=\{X:X^{\mathsf T}=-X,\ \bar X=X\}$, of real dimension $3$, the Lie algebra of $SO(3)$.

**Proof.** The trace of a bracket is zero, the conjugate transpose of a bracket of skew-Hermitian matrices is the negative of the bracket, and the real skew-symmetric matrices are closed under the commutator. The dimensions are the counts of the independent entries: $9$ complex for $\mathfrak{gl}_3$; $8$ complex for the traceless subspace; $9$ real for the skew-Hermitian matrices (three imaginary diagonal entries and three independent complex off-diagonal entries); $8$ real for $\mathfrak{su}(3)$ after removing the trace; $3$ real for $\mathfrak{so}(3)$.

**The adjoint representation.** The map

$$
\operatorname{ad}:\mathfrak{gl}_3\to\operatorname{End}(\mathfrak{gl}_3),\qquad
X\mapsto\operatorname{ad}_X,
$$

is a Lie algebra homomorphism with kernel the centre $\mathbb{C}I$. Its image is the Lie algebra of derivations, isomorphic to $\mathfrak{sl}_3$, of dimension $8$. The exponential of the adjoint action is the conjugation:

$$
\exp(\operatorname{ad}_X)(Y)=e^{X}Ye^{-X}.
$$

**Proof.** The identity is the derivative at $t=0$ of $e^{tX}Ye^{-tX}$, and both sides satisfy the same differential equation with the same initial value.

**The root and the gauge.** For the standard root $H_0=\operatorname{diag}(1,\omega,\omega^{2})$ and the cyclic permutation root, which are $*$-unitary,

$$
H=\exp K,\qquad
K=\frac{2\pi i}{3}\big(P_2+2P_3\big),
$$

with $P_k$ the projector for $\zeta_k$ and eigenvalues $0,2\pi i/3,4\pi i/3$. The matrix $K$ is skew-Hermitian. For a general root $H=SH_0S^{-1}$ the spectral logarithm $K=SK_0S^{-1}$ satisfies $H=\exp K$ but is skew-Hermitian only when $S$ can be chosen $*$-unitary, that is, when $H$ is normal; a non-normal root is not $*$-unitary. A gauge transformation $E\mapsto e^{t}Ee^{-t}$ with $t=\operatorname{diag}(t_1,t_2,t_3)$ traceless rescales the nilpotents:

$$
e^{t}E_{ij}e^{-t}=e^{t_i-t_j}E_{ij},
$$

so with $\lambda_1=e^{t_1-t_2}$ and $\lambda_2=e^{t_2-t_3}$,

$$
E_{12}\mapsto\lambda_1E_{12},\qquad
E_{23}\mapsto\lambda_2E_{23},\qquad
E_{13}\mapsto\lambda_1\lambda_2E_{13}.
$$

The product is forced by the additive parameters: $t_1-t_3=(t_1-t_2)+(t_2-t_3)$. The idempotents $P_k$ are eigenvectors of the gauge with eigenvalue $1$, so they do not depend on $\lambda$.

## Worked Examples

**A nilpotent exponential.** For

$$
N=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix},
\qquad N^{2}=E_{13},\quad N^{3}=0,
$$

one has

$$
e^{N}=I+N+\frac{N^{2}}{2}
=\begin{pmatrix}1&1&\tfrac12\\0&1&1\\0&0&1\end{pmatrix}.
$$

**A Jordan logarithm.** For

$$
A=\begin{pmatrix}2&1&0\\0&2&0\\0&0&3\end{pmatrix},
$$

the block at $2$ has $N=E_{12}$, $N^{2}=0$, so

$$
\log A=\begin{pmatrix}\log2&\tfrac12&0\\0&\log2&0\\0&0&\log3\end{pmatrix}.
$$

Then

$$
\exp(\log A)=\begin{pmatrix}2&1&0\\0&2&0\\0&0&3\end{pmatrix}=A,
$$

because $e^{\log2 I+\frac12E_{12}}=2(I+\frac12E_{12})=2I+E_{12}$ on the block.

**The root.** For the diagonal root $H=\operatorname{diag}(1,\omega,\omega^{2})$,

$$
K=\operatorname{diag}\Big(0,\frac{2\pi i}{3},\frac{4\pi i}{3}\Big),
\qquad
\exp K=H .
$$

For the cyclic permutation root, the same $K$ is expressed in the spectral projectors as $K=\frac{2\pi i}{3}(P_2+2P_3)$, and the identity $\exp K=P_1+\omega P_2+\omega^{2}P_3=H$ is the spectral decomposition of *Spectral Theory and the Spectral Projectors of $M_3(\mathbb{C})$*.

**The exponential by Lagrange interpolation.** If $A$ has simple spectrum $\lambda_1,\lambda_2,\lambda_3$ and spectral projectors $P_k$, then

$$
e^{A}=\sum_{k=1}^{3}e^{\lambda_k}P_k .
$$

For $A=\operatorname{diag}(1,2,4)$ this gives $e^{A}=\operatorname{diag}(e,e^{2},e^{4})$. For the cyclic permutation root multiplied by a scalar, it gives the exponential directly from the projectors.

**Proof.** The identity holds for every polynomial $f$ of degree at most $2$ by the interpolation identity, and $e^{A}$ is the limit of the partial sums of the exponential series, which are polynomials in $A$; the limit of the interpolants is the interpolant of the exponential, because $P_k$ are fixed and the convergence is entrywise.

**A $*$-unitary exponential.** For $X=i\pi\operatorname{diag}(1,0,-1)$,

$$
\exp X=\operatorname{diag}(e^{i\pi},1,e^{-i\pi})=\operatorname{diag}(-1,1,-1),
$$

which is $*$-unitary with determinant $1$, hence in $SU(3)$.

## The Group Structure

**The group.** $GL_3(\mathbb{C})=\{A:\det A\neq0\}$ is a complex Lie group of complex dimension $9$ and real dimension $18$. Its Lie algebra is $\mathfrak{gl}_3$. The exponential is a local diffeomorphism at $0$ and a surjection, and the BCH formula computes the group law in a normal neighbourhood of the identity.

**The subgroups.** The closed subgroups that appear in this series are:

| Group | Lie algebra | Real dimension |
|---|---|---|
| $GL_3(\mathbb{C})$ | $\mathfrak{gl}_3$ | $18$ |
| $SL_3(\mathbb{C})$ | $\mathfrak{sl}_3$ | $16$ |
| $U(3)$ | $\mathfrak{u}(3)$ | $9$ |
| $SU(3)$ | $\mathfrak{su}(3)$ | $8$ |
| $SO(3)$ | $\mathfrak{so}(3)$ | $3$ |
| diagonal torus $T\cong(\mathbb{C}^{\times})^{3}$ | diagonal | $6$ |
| gauge torus $T/\mathbb{C}^{\times}$ | traceless diagonal | $4$ |

The diagonal torus $T\cong(\mathbb{C}^{\times})^{3}$ has complex dimension $3$ and real dimension $6$; the gauge torus of the frame is $T/\mathbb{C}^{\times}$, of real dimension $4$ and complex dimension $2$.

**The centre.** The centre of $GL_3$ is $\mathbb{C}^{\times}I$, of real dimension $2$; the centre of $U(3)$ is $U(1)$, of real dimension $1$; the centre of $SU(3)$ is $\mu_3$, finite.

**The adjoint group.** $PGL_3=GL_3/\mathbb{C}^{\times}I$ has real dimension $16$ and complex dimension $8$, and its Lie algebra is $\mathfrak{sl}_3$. The exponential of $\mathfrak{sl}_3$ lands in $SL_3$, and the exponential of $\mathfrak{u}(3)$ lands in $U(3)$; the exponential of the traceless skew-Hermitian matrices lands in $SU(3)$.

**The exponential is not a group homomorphism.** In general $\exp(X+Y)\neq\exp X\exp Y$; the defect is the BCH series. The map is equivariant under conjugation,

$$
\exp(SXS^{-1})=S\exp(X)S^{-1},
$$

which is the statement that the exponential is natural for the adjoint action.

**Proof.** The series is invariant under conjugation term by term: $(SXS^{-1})^{n}=SX^{n}S^{-1}$.

## Summary

The exponential $\exp X=\sum X^{n}/n!$ is an entire surjection $\mathfrak{gl}_3(\mathbb{C})\to GL_3(\mathbb{C})$, with eigenvalues $e^{\lambda}$ and determinant $e^{\operatorname{tr}X}$. It is a local diffeomorphism at $X$ exactly when no two eigenvalues of $X$ differ by a nonzero multiple of $2\pi i$. It is not injective: $\exp X=I$ exactly when $X$ is diagonalisable with eigenvalues in $2\pi i\mathbb{Z}$. Every invertible matrix has a logarithm, computed on the Jordan blocks by the finite series $(\log\lambda)I+N/\lambda-N^{2}/(2\lambda^{2})$. One-parameter subgroups are exactly the maps $t\mapsto e^{tX}$. The Lie algebra $\mathfrak{gl}_3$ has real dimension $18$; the subalgebras $\mathfrak{sl}_3$, $\mathfrak{u}(3)$, $\mathfrak{su}(3)$, $\mathfrak{so}(3)$ have dimensions $16$, $9$, $8$, $3$ over $\mathbb{R}$. For a $*$-unitary root $H$ one has $H=e^{K}$ with $K=\frac{2\pi i}{3}(P_2+2P_3)$ skew-Hermitian; a non-normal root is not $*$-unitary. The gauge rescales $E_{12},E_{23}$ by $e^{t_1-t_2},e^{t_2-t_3}$, forcing the composite $E_{13}$ to scale by the product.

$$
\boxed{\ \exp:\mathfrak{gl}_3\to GL_3\ \text{surjective, not injective};\quad \det e^{X}=e^{\operatorname{tr}X};\quad \dim_\mathbb{R}\mathfrak{gl}_3=18,\ \dim_\mathbb{R}\mathfrak{u}(3)=9,\ \dim_\mathbb{C}\mathfrak{sl}_3=8.\ }
$$

| Map | Formula |
|---|---|
| exponential | $e^{X}=\sum_{n\ge0}X^{n}/n!$ |
| determinant | $\det e^{X}=e^{\operatorname{tr}X}$ |
| derivative | $de^{X}=(e^{\operatorname{ad}_X}-1)/\operatorname{ad}_X$ |
| conjugation | $e^{SXS^{-1}}=Se^{X}S^{-1}$ |
| unitary root | $H=e^{K}$, $K=\frac{2\pi i}{3}(P_2+2P_3)$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{gl}_3$ | $M_3(\mathbb{C})$ as a Lie algebra |
| $\mathfrak{sl}_3$ | traceless matrices |
| $\mathfrak{u}(3)$ | skew-Hermitian matrices |
| $\mathfrak{su}(3)$ | traceless skew-Hermitian matrices |
| $\operatorname{ad}_X$ | $Y\mapsto[X,Y]$ |
| $H$ | the root with $H^{3}=I$ |
| $K$ | the skew-Hermitian logarithm of a $*$-unitary root $H$ |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the exponential map, the BCH formula and the matrix Lie groups.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the Jordan form and the matrix logarithm.
- Walter Rossmann, *Lie Groups: An Introduction through Linear Groups* (Oxford, 2002), for one-parameter subgroups and the exponential of matrices.
- [The Polar Decomposition of $M_3(\mathbb{C})$](the-polar-decomposition-of-m3c.html), for $U=e^{iK}$ and $P=e^{H}$.
- [The Exponential Polar Decomposition of $M_3(\mathbb{C})$](the-exponential-polar-decomposition-of-m3c.html), for the combined form.
- [Spectral Theory and the Spectral Projectors of $M_3(\mathbb{C})$](spectral-theory-and-the-spectral-projectors-of-m3c.html), for the exponential by Lagrange interpolation.
- [Analysis on $M_3(\mathbb{C})$](analysis-on-m3c.html), for the analytic properties of the exponential.
