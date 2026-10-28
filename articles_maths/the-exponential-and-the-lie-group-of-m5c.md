# __The Exponential and the Lie Group of $M_5(\mathbb{C})$__

## Introduction

The **matrix exponential** is

$$
e^A=\sum_{m=0}^{\infty}\frac{A^m}{m!},\qquad A\in M_5(\mathbb{C}).
$$

The series converges absolutely and uniformly on compact sets, and it defines a smooth map

$$
\exp:\mathfrak{gl}_5=M_5(\mathbb{C})\longrightarrow GL_5(\mathbb{C}).
$$

The group $GL_5(\mathbb{C})$ is a complex Lie group of complex dimension $25$, with Lie algebra $\mathfrak{gl}_5$ and Lie bracket $[X,Y]=XY-YX$. The exponential is the bridge between the two: it sends the Lie algebra to the group, its derivative at $0$ is the identity, and it is a local diffeomorphism. For $GL_5(\mathbb{C})$ the exponential is **surjective** but not injective: every invertible matrix is an exponential, and $e^{2\pi iI}=I$ shows the ambiguity.

The standard subgroups are the images of the standard subalgebras:

$$
SL_5=\exp(\mathfrak{sl}_5),\qquad
U(5)=\exp(\mathfrak{u}(5)),\qquad
SU(5)=\exp(\mathfrak{su}(5)),
$$

and the Borel $B=T\ltimes U$ is the product of the torus and the unipotent group $U=\exp(\mathfrak{n})$, where $\mathfrak{n}$ is the nilpotent upper triangular algebra. The exponential of the root is

$$
e^{tH}=\sum_k e^{t\zeta_k}P_k,
$$

and the exponential of a simple nilpotent is polynomial,

$$
e^{tE_{k,k+1}}=I+tE_{k,k+1},
$$

because $E_{k,k+1}^2=0$. The gauge torus acts by conjugation and rescales the nilpotents.

The article develops the exponential, its convergence, the group law for commuting matrices, the Lie algebra and the Lie bracket, the local diffeomorphism and the surjectivity, the standard subgroups and the exponential of the root and the nilpotents. It assumes the trace, the determinant, the Hermitian structure and the spectral theorem. The polar decomposition and the exponential-polar decomposition are the next articles.

## The Exponential Map

### The Series

**Definition.** The **exponential** of $A$ is the sum of the series

$$
e^A=\sum_{m=0}^{\infty}\frac{A^m}{m!}.
$$

**Theorem.** The series converges absolutely for every $A$; the convergence is uniform on every bounded subset of $M_5$. The exponential is a smooth map $M_5\to M_5$.

**Proof.** Choose a submultiplicative norm $\|\cdot\|$ (for example the operator norm or the Frobenius norm). Then $\|A^m/m!\|\le\|A\|^m/m!$, and the scalar series $\sum\|A\|^m/m!=e^{\|A\|}$ converges. On the ball $\|A\|\le R$ the convergence is uniform by the Weierstrass test; each term is polynomial, so the sum is smooth.

**Corollary.** The exponential is entire (complex analytic) in the entries of $A$, and it commutes with conjugation:

$$
e^{gAg^{-1}}=ge^Ag^{-1}.
$$

**Proof.** The series is a uniform limit of polynomials, hence analytic; the conjugation identity follows term by term.

### Convergence

**Proposition.** The exponential satisfies

$$
e^0=I,\qquad (e^A)^*=e^{A^*},\qquad e^Ae^{-A}=I .
$$

In particular $e^A$ is invertible, with inverse $e^{-A}$.

**Proof.** The first identity is the constant term; the adjoint is termwise because $(A^m)^*=(A^*)^m$; the product $e^Ae^{-A}=e^{A-A}=I$ uses the group law for the commuting matrices $A$ and $-A$.

**Corollary.** The image of the exponential is contained in $GL_5$; the exponential is a map $\mathfrak{gl}_5\to GL_5$.

**Proof.** $e^A$ has the inverse $e^{-A}$.

### The Group Law

**Theorem.** If $[A,B]=0$, then

$$
e^{A+B}=e^Ae^B .
$$

**Proof.** When $A$ and $B$ commute, the binomial theorem applies to $(A+B)^m$:

$$
(A+B)^m=\sum_{k=0}^{m}\binom{m}{k}A^kB^{m-k},
$$

and the exponential series factors into the product of the two exponential series.

**Corollary.** The one-parameter subgroups $t\mapsto e^{tA}$ are group homomorphisms $\mathbb{R}\to GL_5$; they satisfy $e^{sA}e^{tA}=e^{(s+t)A}$.

**Proof.** The matrices $sA$ and $tA$ commute; apply the group law.

**Remark.** **The group law fails for noncommuting matrices.** The correct formula is the Baker–Campbell–Hausdorff formula,

$$
e^Xe^Y=e^{X+Y+\frac12[X,Y]+\frac1{12}[X,[X,Y]]-\frac1{12}[Y,[X,Y]]+\cdots},
$$

whose first correction is the commutator. The exponential is not a group homomorphism from the additive group of the Lie algebra to $GL_5$; it is a local diffeomorphism whose derivative is the identity.

## The Lie Algebra

### Left-Invariant Vector Fields

**Definition.** The **Lie algebra** of $GL_5$ is the tangent space at the identity, $\mathfrak{gl}_5=M_5(\mathbb{C})$, with the bracket $[X,Y]=XY-YX$.

**Proposition.** The tangent space at $I$ is $M_5$; a left-invariant vector field is determined by its value $X$ at $I$, and its value at $g$ is $gX$. The bracket of two left-invariant fields is left-invariant, with value $[X,Y]$ at $I$.

**Proof.** $GL_5$ is open in $M_5$, so the tangent space at $I$ is $M_5$. The left translation $L_g(h)=gh$ has derivative $X\mapsto gX$; the left-invariant field is $g\mapsto gX$. The bracket of the fields $gX$ and $gY$ is $g(XY-YX)$, which is left-invariant with value $[X,Y]$.

**Corollary.** The Lie bracket is bilinear, antisymmetric and satisfies the Jacobi identity:

$$
[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0 .
$$

**Proof.** The associativity of the matrix product gives the Jacobi identity by expansion.

### The Bracket

**Proposition.** The bracket is the derivative of the conjugation:

$$
[X,Y]=\left.\frac{d}{dt}\right|_{t=0}e^{tX}Ye^{-tX}.
$$

**Proof.** Differentiate $e^{tX}Ye^{-tX}=Y+t(XY-YX)+O(t^2)$.

**Corollary.** The adjoint representation $\operatorname{ad}_X(Y)=[X,Y]$ is the derivative at the identity of the adjoint action $\operatorname{Ad}_{e^{tX}}(Y)=e^{tX}Ye^{-tX}$.

**Proof.** The derivative is the bracket by the proposition.

### The One-Parameter Subgroups

**Theorem.** Every one-parameter subgroup $\gamma:\mathbb{R}\to GL_5$ is of the form $\gamma(t)=e^{tX}$ for a unique $X\in\mathfrak{gl}_5$.

**Proof.** The one-parameter subgroups of a Lie group are the integral curves of the left-invariant vector fields through the identity; the integral curve of the field $gX$ is $g e^{tX}$. The uniqueness is the uniqueness of the solution of the ordinary differential equation $\gamma'(t)=\gamma(t)X$ with $\gamma(0)=I$.

**Corollary.** The exponential is the map from the Lie algebra to the one-parameter subgroups; it is injective on a neighborhood of $0$ and a local diffeomorphism there.

**Proof.** The derivative at $0$ is the identity; the inverse function theorem gives a local inverse, the logarithm.

## The Lie Group

### $GL_5$ as a Lie Group

**Theorem.** $GL_5(\mathbb{C})$ is a complex Lie group of complex dimension $25$; its Lie algebra is $\mathfrak{gl}_5$; the multiplication, the inverse and the exponential are smooth.

**Proof.** $GL_5$ is the open subset $\det\ne0$ of $M_5\cong\mathbb{C}^{25}$; the multiplication is polynomial, the inverse is rational with denominator $\det$, and the exponential is entire. The Lie algebra is the tangent space at $I$, with the bracket of left-invariant fields.

**Corollary.** The Lie algebra of $SL_5$ is $\mathfrak{sl}_5$, of dimension $24$; the Lie algebra of $U(5)$ is $\mathfrak{u}(5)$, of real dimension $25$; the Lie algebra of $SU(5)$ is $\mathfrak{su}(5)$, of real dimension $24$.

**Proof.** The subgroups are the zero sets of the determinant, of $U^*U=I$, and of both; their tangent spaces are the traceless, skew-Hermitian, and traceless skew-Hermitian matrices.

### The Exponential Is a Local Diffeomorphism

**Theorem.** The derivative of the exponential at $0$ is the identity:

$$
d\exp_0(X)=X .
$$

Hence the exponential is a local diffeomorphism at $0$: there is a neighborhood $U$ of $0$ in $\mathfrak{gl}_5$ and a neighborhood $V$ of $I$ in $GL_5$ such that $\exp:U\to V$ is a diffeomorphism.

**Proof.** $e^{tX}=I+tX+O(t^2)$, so the derivative at $0$ in the direction $X$ is $X$. The derivative is invertible; the inverse function theorem gives the local diffeomorphism.

**Corollary.** The inverse of the exponential near $I$ is the **logarithm**

$$
\log(I+N)=\sum_{m=1}^{\infty}\frac{(-1)^{m+1}}{m}N^m,
$$

which converges for $\|N\|<1$ and satisfies $e^{\log(I+N)}=I+N$.

**Proof.** The scalar series for $\log(1+z)$ converges for $|z|<1$; the matrix series converges for $\|N\|<1$; the identity $e^{\log(1+z)}=1+z$ is formal and holds for the matrix series.

### Surjectivity

**Theorem.** Every invertible matrix $A\in GL_5(\mathbb{C})$ is an exponential: there exists $X\in\mathfrak{gl}_5$ with $e^X=A$.

**Proof.** Put $A$ in Jordan form $A=gJg^{-1}$, with $J$ a direct sum of Jordan blocks $J_m(\lambda)=\lambda I+N$, $\lambda\ne0$, $N$ nilpotent. Choose $\mu\in\mathbb{C}$ with $e^\mu=\lambda$. Then

$$
J_m(\lambda)=\lambda\left(I+\lambda^{-1}N\right)
=e^\mu e^{\log(I+\lambda^{-1}N)}
=e^{\mu I+\log(I+\lambda^{-1}N)},
$$

because the two matrices commute. The logarithm series terminates because $\lambda^{-1}N$ is nilpotent. Summing over the blocks gives $J=e^X$; then $A=e^{gXg^{-1}}$.

**Corollary.** The exponential is surjective onto $GL_5(\mathbb{C})$, and onto $SL_5(\mathbb{C})$ when restricted to $\mathfrak{sl}_5$.

**Proof.** The first is the theorem. For $A\in SL_5$, put $A=gJg^{-1}$; the eigenvalues $\lambda_k$ of $J$ have product $1$. Choose logarithms $\mu_k$ with $\sum_km_k\mu_k=0$: since $\sum_km_k\log\lambda_k=2\pi i\,m$ for an integer $m$, shift one branch by $-2\pi i\,m$; this does not change its exponential and makes the weighted sum zero. The logarithm of the Jordan form built from these branches has trace $\sum_km_k\mu_k=0$, and $A=e^{gXg^{-1}}$ with $X$ traceless.

**Remark.** **The exponential is surjective but not injective.** $e^{2\pi iI}=I$, and more generally $e^{2\pi iD}=I$ for any diagonal matrix $D$ with integer entries. The fibres of the exponential are discrete unions of affine subspaces; the logarithm is multivalued. The local diffeomorphism is the correct statement; the global inverse does not exist.

## The Standard Subgroups

### $SL_5$

**Theorem.** $SL_5(\mathbb{C})=\{A:\det A=1\}$ is a closed complex Lie subgroup of $GL_5$, of dimension $24$, with Lie algebra $\mathfrak{sl}_5=\{X:\operatorname{tr}X=0\}$. The exponential maps $\mathfrak{sl}_5$ onto $SL_5$.

**Proof.** The determinant is a holomorphic homomorphism $GL_5\to\mathbb{C}^\times$; its kernel is closed; the dimension is $25-1=24$. The Lie algebra is the kernel of the derivative $\operatorname{tr}$ at $I$. The surjectivity is the corollary above.

**Corollary.** $\det(e^X)=e^{\operatorname{tr}X}$; the exponential of a traceless matrix has determinant $1$.

**Proof.** The identity $\det(e^X)=e^{\operatorname{tr}X}$ is the determinant-exponential identity; a traceless $X$ gives determinant $1$.

### $U(5)$ and $SU(5)$

**Theorem.** $U(5)$ is a compact real Lie group of dimension $25$, with Lie algebra $\mathfrak{u}(5)$; the exponential maps $\mathfrak{u}(5)$ onto $U(5)$. $SU(5)$ is compact of dimension $24$, with Lie algebra $\mathfrak{su}(5)$, and the exponential maps $\mathfrak{su}(5)$ onto $SU(5)$.

**Proof.** The $*$-unitary group is the zero set of $U^*U=I$, closed and bounded, hence compact; the tangent space at $I$ is $\mathfrak{u}(5)$; the exponential of a skew-Hermitian matrix is $*$-unitary. The surjectivity is the $*$-unitary diagonalization: $U=VDV^*$ with $D=\operatorname{diag}(e^{i\theta_k})$, and $U=e^{iH}$ with $H=VD_0V^*$, $D_0=\operatorname{diag}(\theta_k)$, skew-Hermitian. For $SU(5)$, choose the angles with sum zero modulo $2\pi$.

**Corollary.** The exponential of a Hermitian matrix is positive definite; the exponential of a skew-Hermitian matrix is $*$-unitary; the exponential of a nilpotent matrix is unipotent.

**Proof.** If $H$ is Hermitian, $e^H$ is Hermitian with positive eigenvalues $e^{\lambda_k}$; if $X$ is skew-Hermitian, $(e^X)^*=e^{X^*}=e^{-X}=(e^X)^{-1}$; if $N$ is nilpotent, $e^N=I+N+\cdots+N^{k-1}/(k-1)!$ is unipotent.

### The Borel and the Unipotent Group

**Definition.** The **Borel subgroup** $B$ is the group of upper triangular matrices; the **unipotent group** $U$ is the group of upper triangular matrices with diagonal entries $1$; the **torus** $T$ is the group of diagonal matrices.

**Theorem.** $B=T\ltimes U$, $\dim B=15$, $\dim U=10$, $\dim T=5$. The Lie algebra of $U$ is the nilpotent strictly upper triangular algebra $\mathfrak{n}$, and the exponential maps $\mathfrak{n}$ bijectively onto $U$.

**Proof.** Every upper triangular matrix is the product of its diagonal and a unipotent matrix; the multiplication is the semidirect product. The dimensions are the number of diagonal entries, off-diagonal upper entries, and diagonal entries. The exponential of a strictly upper triangular matrix is unipotent, and the logarithm is its inverse; both series terminate.

**Corollary.** The exponential of the nilpotent algebra $\mathfrak{n}$ is polynomial of degree at most $4$; the group $U$ is unipotent, and its elements are $I+N$ with $N$ nilpotent.

**Proof.** A strictly upper triangular $5\times5$ matrix satisfies $N^5=0$; the exponential series terminates at $N^4/4!$; the logarithm terminates at $N^4/4$.

## The Exponential of the Root and the Nilpotents

### The Root

**Proposition.** For the root $H=\sum_k\zeta_kE_{kk}$,

$$
e^{tH}=\sum_k e^{t\zeta_k}E_{kk}=\sum_k e^{t\zeta_k}P_k .
$$

The one-parameter subgroup $t\mapsto e^{tH}$ is periodic if the $\zeta_k$ are integer multiples of a common frequency; in particular $H$ itself is $e^L$ with $L=\operatorname{diag}(2\pi ik/5)$ (up to the choice of the logarithm branches).

**Proof.** The exponential of a diagonal matrix is the diagonal of the exponentials; the spectral projectors are $E_{kk}$. The root has eigenvalues $\zeta_k=e^{2\pi ik/5}$, so $H=e^L$ with $L=\operatorname{diag}(2\pi ik/5)$.

**Corollary.** The root is in $SL_5$, because $\det H=\prod_k\zeta_k=1$; the logarithm $L$ can be chosen traceless.

**Proof.** The product of all fifth roots of unity is $(-1)^{5-1}=1$; the determinant is $1$. The naive logarithm $L_0=\operatorname{diag}(2\pi ik/5)$ has trace $2\pi i(0+1+2+3+4)/5=4\pi i$; replacing the $k=0$ entry $0$ by $-4\pi i$ does not change $e^{L_0}$ and makes the trace zero. Hence $H=e^L$ with $L\in\mathfrak{sl}_5$.

### The Simple Nilpotents

**Proposition.** For a simple nilpotent $E_{k,k+1}$, $E_{k,k+1}^2=0$, and

$$
e^{tE_{k,k+1}}=I+tE_{k,k+1}.
$$

The exponential of the sum $N=\sum_k c_kE_{k,k+1}$ is the finite polynomial

$$
e^N=I+N+\frac{N^2}{2}+\frac{N^3}{6}+\frac{N^4}{24},
$$

a unipotent matrix.

**Proof.** The square of a simple nilpotent is zero; the exponential series terminates at the linear term. The sum $N$ is strictly upper triangular, hence $N^5=0$; the exponential is the displayed polynomial.

**Corollary.** The unipotent group $U$ is the image of the nilpotent algebra $\mathfrak{n}$ under the exponential; the simple nilpotents exponentiate to the elementary unipotents $I+tE_{k,k+1}$.

**Proof.** The exponential of $\mathfrak{n}$ is contained in $U$; the logarithm is its inverse; the simple nilpotents give the elementary generators.

### The Gauge

**Proposition.** The gauge torus $T$ acts on the group by conjugation, $g\mapsto tgt^{-1}$; on the simple nilpotents,

$$
tE_{k,k+1}t^{-1}=\frac{t_k}{t_{k+1}}E_{k,k+1},
$$

and on the exponential,

$$
e^{tE_{k,k+1}}\longmapsto I+\frac{t_k}{t_{k+1}}E_{k,k+1}.
$$

The four parameters $\lambda_k=t_k/t_{k+1}$ rescale the four simple nilpotents; the composites rescale by the products; there is no fifth independent scalar.

**Proof.** The conjugation of a matrix unit by a diagonal matrix multiplies it by the ratio of the diagonal entries; the exponential is equivariant. The four ratios are the gauge parameters; the product around a cycle is $1$.

**Corollary.** The gauge is an inner automorphism of $GL_5$; it preserves the group and the exponential, and it rescales the nilpotent directions. The exponential of the gauge-fixed root is the same root, because the root is fixed by the torus.

**Proof.** Conjugation by $t\in T$ is inner; the root is diagonal and commutes with $T$; the nilpotents are the weight vectors.

**Remark.** **The exponential is the group-level expression of the Lie algebra data.** The root $H$ gives the one-parameter subgroup $e^{tH}$; the simple nilpotents give the elementary unipotents $I+tE_{k,k+1}$; the gauge rescales the nilpotent directions. The composites are the products of the elementary unipotents, and the cocycle fixes them. The exponential of the upper triangular algebra is the Borel group, and the exponential of the nilpotent algebra is the unipotent radical.

## Summary

The exponential $e^A=\sum_mA^m/m!$ converges everywhere and defines a smooth surjective map $\mathfrak{gl}_5\to GL_5$. Its derivative at $0$ is the identity, so it is a local diffeomorphism; it is not injective, because $e^{2\pi iI}=I$. The group law $e^{A+B}=e^Ae^B$ holds for commuting matrices; the Baker–Campbell–Hausdorff formula gives the general correction.

$$
\boxed{\ \exp:\mathfrak{gl}_5\to GL_5\text{ is surjective, locally invertible};\quad \det(e^A)=e^{\operatorname{tr}A};\quad e^{tE_{k,k+1}}=I+tE_{k,k+1}.\ }
$$

The Lie algebra $\mathfrak{gl}_5$ has the commutator bracket; the one-parameter subgroups are $e^{tX}$; the standard subalgebras $\mathfrak{sl}_5,\mathfrak{u}(5),\mathfrak{su}(5),\mathfrak{n},\mathfrak{t}$ exponentiate to $SL_5,U(5),SU(5),U,T$. The root gives $e^{tH}=\sum_ke^{t\zeta_k}P_k$; the simple nilpotents give the elementary unipotents; the gauge rescales the four nilpotent directions.

| Object | Lie algebra | Group |
|---|---|---|
| $GL_5$ | $\mathfrak{gl}_5$, dimension $25$ | $GL_5$, dimension $25$ |
| $SL_5$ | $\mathfrak{sl}_5$, dimension $24$ | $SL_5$, dimension $24$ |
| $U(5)$ | $\mathfrak{u}(5)$, real dimension $25$ | $U(5)$, compact |
| $SU(5)$ | $\mathfrak{su}(5)$, real dimension $24$ | $SU(5)$, compact |
| Borel $B$ | $\mathfrak{b}$, dimension $15$ | $B=T\ltimes U$ |
| Unipotent $U$ | $\mathfrak{n}$, dimension $10$ | $U$, unipotent |
| Torus $T$ | $\mathfrak{t}$, dimension $5$ | $T$, diagonal |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e^A$ | The matrix exponential |
| $\mathfrak{gl}_5$ | The Lie algebra $M_5$ with the commutator |
| $\mathfrak{sl}_5$ | The traceless matrices |
| $\mathfrak{u}(5)$ | The skew-Hermitian matrices |
| $\mathfrak{su}(5)$ | The traceless skew-Hermitian matrices |
| $\mathfrak{n}$ | The strictly upper triangular matrices |
| $\mathfrak{t}$ | The diagonal matrices |
| $B=T\ltimes U$ | The Borel group |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, second edition, 2015), for the matrix exponential, the Lie algebra, the one-parameter subgroups and the Lie group structure.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the exponential, the logarithm and the Jordan form.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the exponential map, the Lie groups and the symmetric spaces.
- [The Element, the Coordinates and the Trace of $M_5(\mathbb{C})$](the-element-the-coordinates-and-the-trace-of-m5c.html), for the determinant identity and the Jordan decomposition.
- [The Involution and the Hermitian Structure of $M_5(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m5c.html), for the $*$-unitary group and the compact real form.
- [Spectral Theory and the Spectral Projectors of $M_5(\mathbb{C})$](spectral-theory-and-the-spectral-projectors-of-m5c.html), for the functional calculus and the exponential of a Hermitian matrix.
- [The Polar Decomposition of $M_5(\mathbb{C})$](the-polar-decomposition-of-m5c.html), for the polar decomposition and the positive cone.
- [The Exponential-Polar Decomposition of $M_5(\mathbb{C})$](the-exponential-polar-decomposition-of-m5c.html), for the combination of the exponential and the polar decomposition.
