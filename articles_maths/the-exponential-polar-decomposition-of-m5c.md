# __The Exponential-Polar Decomposition__

## Introduction

The polar decomposition $A=UP$ of *The Polar Decomposition* has an exponential form:

$$
A=e^{iH}e^{S},\qquad H=H^*,\quad S=S^*,
$$

where $e^{iH}$ is unitary and $e^S$ is positive definite. Indeed, the unitary part is $U=e^{iH}$ by the spectral theorem for unitary matrices, and the positive part is $P=e^S$ by the spectral theorem for positive definite matrices. The **exponential-polar decomposition** is the decomposition

$$
GL_5(\mathbb{C})=U(5)\cdot\exp(i\mathfrak{u}(5)),
\qquad U(5)=\exp(\mathfrak{u}(5)),
$$

written in exponential coordinates.

The decomposition is **not unique in $H$**: the unitary logarithm is defined modulo $2\pi$, because $e^{2\pi iI}=I$. The positive part $S$ is unique; the unitary part $e^{iH}$ is unique, but its logarithm $H$ is not. The exponential-polar coordinates are therefore coordinates on $GL_5$ modulo the lattice of the unitary periods.

The article develops the exponential form of the polar decomposition, the Cartan decomposition $G=K\exp(\mathfrak{p})$, the $KAK$ decomposition (the SVD in group form), and the Iwasawa decomposition $G=KAN$. It proves the decompositions, states the uniqueness and the Weyl-group ambiguity, and describes the geodesic polar coordinates on the symmetric space $GL_5/U(5)$. It assumes the polar decomposition, the exponential and the Lie group of the preceding articles.

## The Exponential Form of the Polar Decomposition

### The Right and Left Forms

**Theorem.** Every invertible $A\in GL_5(\mathbb{C})$ can be written as

$$
A=e^{iH}e^{S},
$$

with $H,S$ Hermitian. The positive part $e^S=|A|$ is unique, and the unitary part $e^{iH}=A|A|^{-1}$ is unique.

**Proof.** The polar decomposition gives $A=UP$ with $U$ unitary and $P$ positive definite. By the spectral theorem for unitary matrices, $U=V\operatorname{diag}(e^{i\theta_1},\dots,e^{i\theta_5})V^*=e^{iH}$ with $H=V\operatorname{diag}(\theta_1,\dots,\theta_5)V^*$ Hermitian. By the spectral theorem for positive definite matrices, $P=W\operatorname{diag}(e^{s_1},\dots,e^{s_5})W^*=e^S$ with $S=W\operatorname{diag}(s_1,\dots,s_5)W^*$ Hermitian, $s_k=\log\lambda_k$. Hence $A=e^{iH}e^S$. The uniqueness of $P$ and $U$ gives the uniqueness of $S$ and $e^{iH}$.

**Corollary.** The left form is

$$
A=e^{S'}e^{iH'},\qquad e^{S'}=|A^*|=(AA^*)^{1/2},\quad e^{iH'}=|A^*|^{-1}A .
$$

The left and right positive parts are related by $S'=U S U^*$.

**Proof.** Apply the theorem to $A^*$ and take adjoints; or use the left polar decomposition $A=P'U$ with $P'=(AA^*)^{1/2}$; the relation follows from $AA^*=UP^2U^*$.

**Corollary.** The exponential-polar decomposition is the polar decomposition in exponential coordinates; the positive part is the exponential of a Hermitian matrix, the unitary part the exponential of $i$ times a Hermitian matrix.

**Proof.** The spectral theorem for $P$ and $U$; the exponentials are the spectral functions.

### The Uniqueness

**Theorem.** The Hermitian part $S$ is unique. The Hermitian part $H$ is unique modulo the lattice

$$
H\sim H+2\pi D,\qquad D=\operatorname{diag}(n_1,\dots,n_5),\quad n_k\in\mathbb{Z},
$$

in a basis diagonalizing $H$; equivalently, $e^{iH}$ is unique.

**Proof.** $e^{2S}=A^*A$ determines $S$ uniquely because the positive definite square root is unique and the logarithm of a positive definite matrix is unique. The unitary part $e^{iH}=A|A|^{-1}$ is unique; the logarithm $H$ is determined up to the addition of $2\pi$ times an integer diagonal matrix in the eigenbasis of $H$, because $e^{i(H+2\pi D)}=e^{iH}e^{2\pi iD}=e^{iH}$.

**Corollary.** The map

$$
i\mathfrak{u}(5)\times i\mathfrak{u}(5)\longrightarrow GL_5,\qquad (H,S)\longmapsto e^{iH}e^S
$$

is surjective and is a local diffeomorphism; it is not injective, and its fibres are the lattice translates of $H$.

**Proof.** Surjectivity is the theorem; the derivative at $(0,0)$ is $(H,S)\mapsto H+S$, which is surjective but not injective on the product (the diagonal directions overlap); the local diffeomorphism is the inverse function theorem on the quotient by the lattice; the non-injectivity is $e^{2\pi iI}=I$.

**Remark.** **The exponential-polar decomposition is unique in the group, not in the Lie algebra.** The group elements $e^{iH}$ and $e^S$ are unique; the Lie algebra element $H$ is not, because the exponential is not injective on the unitary directions. The positive part $S$ is unique because the exponential is injective on the Hermitian matrices. The lattice ambiguity is the price of the exponential coordinates.

### The Lattice Ambiguity

**Proposition.** The fibre of the exponential-polar map over $A=e^{iH}e^S$ is

$$
\{(H+2\pi D,\ S):D\text{ diagonal with integer entries in a basis diagonalizing }H\}.
$$

**Proof.** $e^{i(H+2\pi D)}=e^{iH}$ for integer diagonal $D$; conversely, if $e^{iH'}=e^{iH}$, then $H'$ and $H$ commute and differ by $2\pi$ times an integer diagonal in the common eigenbasis.

**Corollary.** The exponential-polar coordinates are coordinates on $GL_5$ modulo the lattice $\mathbb{Z}^5$ of the unitary periods; the quotient is the group itself.

**Proof.** The group is the quotient of the Lie algebra product by the lattice; the positive part has no lattice.

## The Cartan Decomposition

### The Lie Algebra Decomposition

**Theorem.** The Lie algebra has the Cartan decomposition

$$
\mathfrak{gl}_5=\mathfrak{u}(5)\oplus\mathfrak{p},\qquad \mathfrak{p}=i\mathfrak{u}(5),
$$

where $\mathfrak{p}$ is the space of Hermitian matrices. The decomposition is the $+1$ and $-1$ eigenspaces of the Cartan involution $\theta(X)=-X^*$.

**Proof.** Every $X$ is $X=\frac12(X-X^*)+\frac12(X+X^*)$, skew-Hermitian plus Hermitian; the intersection is zero. The involution $\theta(X)=-X^*$ has $+1$ eigenspace $\mathfrak{u}(5)$ and $-1$ eigenspace $i\mathfrak{u}(5)$; the two are orthogonal for the trace form.

**Corollary.** $[\mathfrak{u},\mathfrak{u}]\subseteq\mathfrak{u}$, $[\mathfrak{u},\mathfrak{p}]\subseteq\mathfrak{p}$, $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{u}$; the decomposition is a symmetric Lie algebra.

**Proof.** The bracket of skew-Hermitian matrices is skew-Hermitian; the bracket of a skew-Hermitian and a Hermitian is Hermitian; the bracket of two Hermitian is skew-Hermitian.

### The Global Decomposition

**Theorem (Cartan decomposition).** Every $g\in GL_5(\mathbb{C})$ is uniquely

$$
g=Ue^S,\qquad U\in U(5),\quad S\in i\mathfrak{u}(5),
$$

with $U$ unitary and $S$ Hermitian. This is the polar decomposition.

**Proof.** The polar decomposition $g=UP$ with $P$ positive definite; $P=e^S$ with $S$ Hermitian; the uniqueness is the polar uniqueness.

**Corollary.** The map $U(5)\times i\mathfrak{u}(5)\to GL_5$, $(U,S)\mapsto Ue^S$, is a diffeomorphism.

**Proof.** It is the polar diffeomorphism composed with the exponential diffeomorphism $i\mathfrak{u}(5)\to\mathcal{P}$.

### The Symmetric Space

**Theorem.** The quotient $GL_5(\mathbb{C})/U(5)$ is diffeomorphic to $i\mathfrak{u}(5)\cong\mathbb{R}^{25}$; it is a symmetric space of noncompact type.

**Proof.** The quotient is the positive cone $\mathcal{P}$; the exponential of Hermitian matrices is a diffeomorphism onto $\mathcal{P}$; the symmetric space structure is the Cartan decomposition.

**Corollary.** The exponential-polar decomposition is the global form of the Cartan decomposition; the unitary group is the compact part and the Hermitian exponential the noncompact part.

**Proof.** The global Cartan decomposition is the polar decomposition; the exponential coordinates are the Hermitian part.

## The $KAK$ Decomposition

### The SVD in Group Form

**Theorem ($KAK$).** Every $g\in GL_5(\mathbb{C})$ can be written as

$$
g=K_1AK_2,\qquad K_1,K_2\in U(5),\quad A=\operatorname{diag}(a_1,\dots,a_5),\quad a_k>0 .
$$

The diagonal entries $a_k$ are the singular values of $g$, and they are unique up to permutation; if ordered $a_1\ge\cdots\ge a_5$, they are unique.

**Proof.** The singular value decomposition $g=V\Sigma W^*$ with $V,W$ unitary and $\Sigma$ positive diagonal gives $g=K_1AK_2$ with $K_1=V$, $A=\Sigma$, $K_2=W^*$. The singular values are unique; the ordering fixes the diagonal.

**Corollary.** The $KAK$ decomposition is the SVD in group form; the $A$ part is the exponential of the real diagonal Lie algebra, $A=e^D$ with $D=\operatorname{diag}(\log a_k)$.

**Proof.** The positive diagonal matrix is the exponential of the real diagonal matrix of the logarithms.

### The Weyl Group

**Proposition.** The diagonal part $A$ is unique up to the action of the Weyl group $S_5$, which permutes the diagonal entries; the $K$-parts are unique up to the corresponding permutation.

**Proof.** The SVD determines the singular values as a multiset; a permutation of the diagonal entries is compensated by permuting the columns of $V$ and $W$; the Weyl group of $U(5)$ is $S_5$.

**Corollary.** The $KAK$ decomposition is unique if the diagonal entries are ordered; the quotient of $A$ by the Weyl group is the set of unordered singular values.

**Proof.** The ordering fixes the representative; the Weyl group acts by permutation.

### The Geodesic Polar Coordinates

**Theorem.** On the symmetric space $GL_5/U(5)\cong\mathcal{P}$, the $KAK$ decomposition gives the geodesic polar coordinates: every $P\in\mathcal{P}$ is $P=K e^D K^*$ with $K$ unitary and $D$ real diagonal; the geodesic from $I$ to $P$ is $K e^{tD}K^*$, and the distance is $\|D\|_F$.

**Proof.** The spectral theorem for $P$ gives $P=K e^D K^*$ with $D$ the diagonal of the logarithms; the geodesic $t\mapsto K e^{tD}K^*$ starts at $I$ and ends at $P$; its length is $\|D\|_F$ for the trace metric.

**Corollary.** The singular values of $g$ are the exponentials of the diagonal entries of $D$; the distance from $I$ to $P$ is the Euclidean norm of the logarithms of the singular values.

**Proof.** $a_k=e^{d_k}$; the distance is $\sqrt{\sum d_k^2}$.

**Remark.** **The $KAK$ decomposition is the polar decomposition of the group, read as geodesic polar coordinates.** The $K$ parts are the angular coordinates, the $A$ part the radial coordinate; the Weyl group is the ambiguity of the angles. The exponential-polar decomposition is the same picture with the unitary part written as $e^{iH}$.

## The Iwasawa Decomposition

### The $KAN$ Decomposition

**Theorem (Iwasawa).** Every $g\in GL_5(\mathbb{C})$ is uniquely

$$
g=KAN,
$$

where $K=U(5)$, $A$ is the group of positive diagonal matrices, and $N$ is the unipotent group of upper triangular matrices with diagonal entries $1$.

**Proof.** Gram–Schmidt on the columns of $g$: $g=QR$ with $Q$ unitary and $R$ upper triangular with positive diagonal. Write $R=AN$ with $A$ the positive diagonal of $R$ and $N=A^{-1}R$ unipotent upper triangular. Then $g=QAN$; the uniqueness is the uniqueness of the Gram–Schmidt decomposition.

**Corollary.** The Iwasawa decomposition is a diffeomorphism $U(5)\times A\times N\to GL_5$; the real dimensions are $25+5+20=50$, which is the real dimension of $GL_5$.

**Proof.** The Gram–Schmidt map is a diffeomorphism. The dimensions are $25$ for $U(5)$, $5$ for the positive diagonal $A$, and $20$ for the unipotent $N$ (complex dimension $10$); the sum is $50$.

**Corollary.** The Iwasawa decomposition is not the polar decomposition: the polar positive part $P$ is positive definite, not diagonal, and the unitary part is $U$, while the Iwasawa $A$ is diagonal and $N$ is unipotent. The two decompositions are related by the Gram–Schmidt process.

**Proof.** The polar decomposition uses the positive square root of $g^*g$; the Iwasawa uses the QR decomposition. The $A$ part is diagonal, the $N$ part unipotent; the polar $P$ is general positive definite.

### The Gram–Schmidt Proof

**Proposition.** The Gram–Schmidt decomposition of the columns $g_1,\dots,g_5$ gives

$$
g_k=\sum_{l\le k}r_{lk}q_l,\qquad r_{kk}>0,
$$

with $q_1,\dots,q_5$ orthonormal; the matrix $Q=(q_1,\dots,q_5)$ is unitary and $R=(r_{lk})$ is upper triangular with positive diagonal.

**Proof.** The Gram–Schmidt process orthogonalizes the columns; the coefficients $r_{lk}$ are the projections; the diagonal entries are the norms of the orthogonalized columns, positive.

**Corollary.** The Iwasawa decomposition is the matrix form of the Gram–Schmidt process; the $A$ part is the diagonal of the norms, the $N$ part the unipotent upper triangular factor.

**Proof.** $R=AN$; $A$ is the diagonal of $R$; $N$ is unipotent upper triangular.

### The Relation to the Polar Decomposition

**Proposition.** The polar decomposition and the Iwasawa decomposition are related by

$$
g=UP=QAN,
$$

where $U,Q$ are unitary, $P$ is positive definite, $A$ is positive diagonal and $N$ is unipotent upper triangular. The two decompositions are distinct: $P=AN$ would require $AN$ to be positive definite, but $AN$ is Hermitian only when $N=I$. In general $U\ne Q$ and $P\ne AN$.

**Proof.** $AN$ is upper triangular with positive diagonal; it is Hermitian iff it is diagonal, i.e., $N=I$. The polar decomposition uses the positive square root of $g^*g$; the Iwasawa decomposition uses the Gram–Schmidt factorization. They are different coordinate systems.

**Corollary.** The Iwasawa decomposition is not the polar decomposition; the positive part of the polar decomposition is not the $A$ part of the Iwasawa decomposition. The $A$ part is diagonal, the $P$ part is positive definite.

**Proof.** The diagonal $A$ is a special positive definite matrix; the general $P$ is not diagonal.

**Remark.** **The three decompositions are different coordinate systems on $GL_5$.** The polar decomposition $G=K\exp(\mathfrak{p})$ uses the positive definite cone; the $KAK$ decomposition uses the maximal torus of the cone and the Weyl group; the Iwasawa decomposition $G=KAN$ uses the Borel subgroup. The exponential-polar decomposition is the polar one written with exponentials; the $KAK$ and $KAN$ are the geodesic and the Gram–Schmidt coordinates.

## The Exponential-Polar Coordinates

### The Map

**Theorem.** The map

$$
\Phi:i\mathfrak{u}(5)\times i\mathfrak{u}(5)\longrightarrow GL_5,\qquad (H,S)\longmapsto e^{iH}e^S
$$

is surjective, smooth, and a local diffeomorphism at every point where the eigenvalues of $H$ have no differences in $2\pi\mathbb{Z}$; the fibre is the lattice of the unitary periods.

**Proof.** Surjectivity is the exponential-polar decomposition; smoothness is the exponential. The derivative at $(H,S)$ is the composition of the derivatives of the exponential and the product. The exponential $S\mapsto e^S$ is a diffeomorphism on the Hermitian matrices; the exponential $H\mapsto e^{iH}$ is a local diffeomorphism exactly when the eigenvalues of $\operatorname{ad}_{iH}$ avoid $2\pi i\mathbb{Z}\setminus\{0\}$, i.e., when no two eigenvalues of $H$ differ by a multiple of $2\pi$. The inverse function theorem then gives the local diffeomorphism; the global ambiguity is the lattice.

**Corollary.** The exponential-polar coordinates are the polar coordinates of the group: the unitary directions are angular, the Hermitian directions radial.

**Proof.** The positive part $e^S$ is the radial coordinate; the unitary part $e^{iH}$ is the angular coordinate; the lattice is the periodicity of the angles.

### The Jacobian

**Proposition.** The derivative of $\Phi$ at $(H,S)$ in the directions $(\dot H,\dot S)$ is

$$
\left(D\exp_{iH}(i\dot H)\right)e^S+e^{iH}\left(D\exp_S(\dot S)\right),
$$

with the exponential derivatives of *Analysis on $M_5$*. At $(0,0)$ the derivative is $(\dot H,\dot S)\mapsto i\dot H+\dot S$, which is an isomorphism from the Hermitian product to $\mathfrak{gl}_5$.

**Proof.** The product rule and the chain rule; the derivative of $e^{iH}$ in the direction $\dot H$ is $D\exp_{iH}(i\dot H)$; the derivative of $e^S$ is $D\exp_S(\dot S)$; at $(0,0)$, $D\exp_0=I$.

**Corollary.** The Jacobian is singular exactly when the unitary exponential fails to be a local diffeomorphism, i.e., when two eigenvalues of $H$ differ by a multiple of $2\pi$. The Hermitian exponential is always a local diffeomorphism.

**Proof.** The derivative is the sum of the invertible Hermitian exponential derivative and the unitary exponential derivative; the latter is singular exactly at the period differences; the former is invertible everywhere.

### The Geometry

**Theorem.** The exponential-polar decomposition gives the geodesic polar coordinates on the symmetric space $GL_5/U(5)$: the geodesic from $I$ to $e^S$ is $e^{tS}$, and the unitary part is the angular coordinate. The distance is $\|S\|_F$.

**Proof.** The positive cone is the symmetric space; the geodesic from $I$ to $e^S$ is $e^{tS}$; the distance is the Frobenius norm of $S$.

**Corollary.** The $KAK$ decomposition refines the exponential-polar coordinates by diagonalizing $S$: $S=KDK^*$; the radial coordinate is the diagonal $D$, and the angular coordinates are the two unitary factors.

**Proof.** The spectral theorem for $S$; the $KAK$ decomposition of $e^S$.

**Remark.** **The exponential-polar decomposition is the group-level analogue of the polar form of a complex number.** A complex number is $re^{i\theta}$; a matrix is $e^Se^{iH}$, with $S$ the logarithm of the modulus and $H$ the phase. The noncommutativity makes the order matter: the right and left forms differ, and the unitary logarithm is periodic. The $KAK$ and Iwasawa decompositions are the finer coordinate systems adapted to the torus and the Borel.

## Summary

Every invertible matrix has the exponential-polar decomposition

$$
A=e^{iH}e^S,\qquad H,S\text{ Hermitian},
$$

with $e^S=|A|$ unique and $e^{iH}=A|A|^{-1}$ unique; $H$ is unique modulo the lattice of unitary periods. The group decompositions are

$$
GL_5=U(5)\exp(i\mathfrak{u}(5))=KAK=KAN,
$$

the Cartan (polar), the $KAK$ (SVD) and the Iwasawa (Gram–Schmidt) decompositions.

$$
\boxed{\ A=e^{iH}e^S;\quad GL_5=U(5)\exp(i\mathfrak{u}(5));\quad g=K_1AK_2;\quad g=KAN.\ }
$$

The exponential-polar coordinates are the polar coordinates of the group: the positive part is radial, the unitary part angular, the lattice is the periodicity. The $KAK$ decomposition gives the geodesic polar coordinates on the symmetric space $GL_5/U(5)$; the $KAN$ decomposition gives the Gram–Schmidt coordinates. The three decompositions are different coordinate systems, related by the polar decomposition, the SVD and the QR decomposition.

| Decomposition | Form | Factors |
|---|---|---|
| Polar | $A=UP$ | $U\in U(5)$, $P>0$ |
| Exponential-polar | $A=e^{iH}e^S$ | $H,S$ Hermitian |
| Cartan | $G=K\exp(\mathfrak{p})$ | $K=U(5)$, $\mathfrak{p}=i\mathfrak{u}(5)$ |
| $KAK$ | $g=K_1AK_2$ | $A$ positive diagonal |
| Iwasawa | $g=KAN$ | $A$ positive diagonal, $N$ unipotent |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e^{iH}$ | The unitary part |
| $e^S$ | The positive part |
| $\mathfrak{p}=i\mathfrak{u}(5)$ | The Hermitian tangent directions |
| $K=U(5)$ | The unitary group |
| $A$ | The positive diagonal group |
| $N$ | The unipotent upper triangular group |
| $KAK$ | The SVD in group form |
| $KAN$ | The Iwasawa decomposition |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the Cartan, $KAK$ and Iwasawa decompositions and the symmetric spaces.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, second edition, 2015), for the Cartan decomposition and the exponential map.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the polar decomposition, the SVD and the QR decomposition.
- [The Polar Decomposition](the-polar-decomposition-of-m5c.html), for the polar decomposition and the positive cone.
- [The Exponential and the Lie Group](the-exponential-and-the-lie-group-of-m5c.html), for the exponential, the logarithm and the Lie group.
- [The Adjoint Action, the Orbits and the Flag Variety](the-adjoint-action-the-orbits-and-the-flag-variety-of-m5c.html), for the symmetric space and the group action.
- [The Geometry of the Idempotents](the-geometry-of-the-idempotents-of-m5c.html), for the geometry of the idempotent varieties.
