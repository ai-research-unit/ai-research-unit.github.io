# __The Forms, the Norms and the Singular Set__

## Introduction

The algebra $M_6(\mathbb{C})$ carries three kinds of quantitative structure. The **trace form** $\operatorname{tr}(A^*B)$ is a positive definite Hermitian form; the **determinant** is a homogeneous polynomial of degree six; and the **norms** are the Schatten norms of the singular values,

$$
\lVert A\rVert_p=\left(\sum_{i=1}^{6}\sigma_i(A)^p\right)^{1/p},
\qquad
p=1,2,\infty,
$$

the nuclear, Frobenius and operator norms. The determinant vanishes on the **singular set**

$$
\Sigma=\{A:\det A=0\},
$$

a complex hypersurface of complex dimension $35$ and real codimension two. The set is stratified by the rank; the rank-$k$ stratum has complex dimension $k(12-k)$.

The Hermitian form is definite, so there is no null cone: the only isotropic vector is $0$. The singular set is a cone, but it is not the isotropic cone of the form. This is the contrast with the biquaternion algebra, whose trace form is indefinite, whose null cone is the zero-divisor cone, and whose link is a five-dimensional manifold.

The article assumes the Hermitian form of *The Involution and the Hermitian Structure* and the rank strata of *The Rank-Two and Rank-Three Splits*. It uses no topology beyond the finite-dimensional metric. The singular values of a matrix are also used in *The Polar Decomposition*; the biquaternion comparison is *The Biquaternion Algebra and Its Vector Spaces*.

## The Forms

### The Hermitian Trace Form

**Definition.** The **trace form** is

$$
\langle A,B\rangle=\operatorname{tr}(A^*B).
$$

**Theorem.** The form is Hermitian and positive definite:

$$
\langle A,B\rangle=\overline{\langle B,A\rangle},
\qquad
\langle A,A\rangle=\sum_{i,j}\lvert a_{ij}\rvert^2\ge0,
$$

with equality if and only if $A=0$.

**Proof.** This is *The Involution and the Hermitian Structure*.

**Corollary (the real and imaginary parts).** The real part is the Euclidean inner product of the $72$ real coordinates; the imaginary part is a symplectic form. The form is definite, so its isotropic set is $\{0\}$.

**Proof.** Expand in the real and imaginary coordinates; the sum of squares is positive definite, and the imaginary part is alternating.

### The Complex Bilinear Trace Pairing

**Definition.** The **trace pairing** is

$$
(A,B)\longmapsto\operatorname{tr}(AB).
$$

**Theorem.** The trace pairing is symmetric, nondegenerate and invariant, but it is indefinite: it has nonzero isotropic vectors.

**Proof.** It is *The Element, the Coordinates and the Trace*. The matrix unit $E_{12}$ is isotropic: $\operatorname{tr}(E_{12}^2)=0$.

**Remark (two forms, two roles).** The complex bilinear pairing is the algebra form; it identifies the algebra with its dual and gives the Killing form on $\mathfrak{sl}_6$. The Hermitian form is the metric; it gives the Frobenius norm and the Hilbert-space structure. **The complex bilinear trace pairing has a null cone; the Hermitian form does not.**

### The Determinant

**Definition.** The **determinant** is the polynomial

$$
\det:M_6(\mathbb{C})\longrightarrow\mathbb{C}
$$

of degree six, multiplicative and invariant under conjugation.

**Theorem (the derivative).** For invertible $A$,

$$
d(\det)_A(B)=\det(A)\operatorname{tr}(A^{-1}B).
$$

For singular $A$ of rank five, the derivative is the cofactor pairing, and it is nonzero.

**Proof.** $\det(A+tB)=\det(A)\det(I+tA^{-1}B)=\det(A)(1+t\operatorname{tr}(A^{-1}B)+O(t^2))$. At rank five, the adjugate is nonzero and $d(\det)_A(B)=\operatorname{tr}(\operatorname{adj}(A)B)$.

**Corollary (the singular set is smooth at rank five).** The gradient of $\det$ is nonzero at every matrix of rank five or six.

**Proof.** The adjugate of a rank-five matrix is nonzero (it is the product of the nonzero cofactors), and it vanishes at rank at most four.

## The Norms

### The Singular Values

**Definition.** The **singular values** of $A$ are the nonnegative square roots of the eigenvalues of $A^*A$:

$$
\sigma_i(A)=\sqrt{\lambda_i(A^*A)},\qquad
\sigma_1\ge\sigma_2\ge\cdots\ge\sigma_6\ge0 .
$$

**Theorem.** The singular values are the eigenvalues of $\lvert A\rvert=(A^*A)^{1/2}$, and

$$
\operatorname{tr}(A^*A)=\sum_i\sigma_i^2,
\qquad
\lvert\det A\rvert=\prod_i\sigma_i .
$$

**Proof.** The spectral theorem for the positive semidefinite $A^*A$; the trace is the sum of the eigenvalues, the determinant is the product.

**Corollary (the $*$-unitary invariance).** The singular values are invariant under $A\mapsto UAV$ for $U,V\in U(6)$.

**Proof.** $(UAV)^*(UAV)=V^*A^*AV$, unitarily conjugate to $A^*A$.

### The Schatten Norms

**Definition.** For $1\le p<\infty$,

$$
\lVert A\rVert_p=\left(\sum_{i=1}^{6}\sigma_i(A)^p\right)^{1/p},
\qquad
\lVert A\rVert_\infty=\sigma_1(A).
$$

The cases are the **nuclear norm** $p=1$, the **Frobenius norm** $p=2$, and the **operator norm** $p=\infty$.

**Theorem.** Each $\lVert\cdot\rVert_p$ is a norm, unitarily invariant, and

$$
\lVert A\rVert_\infty\le\lVert A\rVert_p\le\lVert A\rVert_1
\qquad
(1\le p\le\infty),
$$

with

$$
\lVert A\rVert_\infty\le\lVert A\rVert_2\le\sqrt6\,\lVert A\rVert_\infty,
\qquad
\lVert A\rVert_2\le\lVert A\rVert_1\le\sqrt6\,\lVert A\rVert_2,
\qquad
\lVert A\rVert_\infty\le\lVert A\rVert_1\le6\lVert A\rVert_\infty .
$$

**Proof.** The Schatten norms are the $\ell^p$ norms of the singular value vector; the inequalities are the standard $\ell^p$ inequalities in dimension six, with the factor $\sqrt6$ from the Cauchy–Schwarz inequality and $6$ from the comparison of $\ell^1$ and $\ell^\infty$.

**Theorem (the operator norm).** The operator norm is

$$
\lVert A\rVert_\infty=\sup_{\lVert x\rVert=1}\lVert Ax\rVert=\sigma_1(A),
$$

and it is a $C^*$-norm:

$$
\lVert A^*A\rVert_\infty=\lVert A\rVert_\infty^2 .
$$

**Proof.** The supremum of $\lVert Ax\rVert$ over the unit sphere is the square root of the largest eigenvalue of $A^*A$, that is $\sigma_1$. The $C^*$-identity follows from $\lVert A^*A\rVert=\sigma_1^2=\lVert A\rVert^2$.

**Theorem (the nuclear norm).** The nuclear norm is

$$
\lVert A\rVert_1=\operatorname{tr}\lvert A\rvert=\sum_i\sigma_i(A),
$$

and it is the dual of the operator norm:

$$
\lVert A\rVert_1=\sup_{\lVert B\rVert_\infty\le1}\lvert\operatorname{tr}(A^*B)\rvert,
\qquad
\lVert A\rVert_\infty=\sup_{\lVert B\rVert_1\le1}\lvert\operatorname{tr}(A^*B)\rvert .
$$

**Proof.** The von Neumann trace inequality $\lvert\operatorname{tr}(A^*B)\rvert\le\sum_i\sigma_i(A)\sigma_i(B)$, with equality for suitable unitaries; the two suprema follow.

### The Determinant Bounds

**Theorem.** For every $A$,

$$
\lvert\det A\rvert\le\left(\frac{\lVert A\rVert_2}{\sqrt6}\right)^6
\le\lVert A\rVert_\infty^6,
\qquad
\lvert\det A\rvert\le\left(\frac{\lVert A\rVert_1}{6}\right)^6 .
$$

**Proof.** The determinant modulus is $\prod_i\sigma_i$. The arithmetic–geometric mean inequality gives

$$
\left(\prod_i\sigma_i\right)^{1/6}
\le\left(\frac{1}{6}\sum_i\sigma_i^2\right)^{1/2}
=\frac{\lVert A\rVert_2}{\sqrt6},
$$

and the same with $\sum_i\sigma_i/6$. The bound $\prod_i\sigma_i\le\sigma_1^6$ is immediate.

**Corollary (the trace bound).** For every $A$,

$$
\lvert\operatorname{tr}A\rvert\le\lVert A\rVert_1,
\qquad
\lvert\operatorname{tr}A\rvert\le\sqrt6\,\lVert A\rVert_2 .
$$

**Proof.** The first is the von Neumann inequality with $B=I_6$; the second is the Cauchy–Schwarz inequality for the Frobenius form.

**Remark (the operator norm is the algebra norm).** The operator norm is submultiplicative,

$$
\lVert AB\rVert_\infty\le\lVert A\rVert_\infty\lVert B\rVert_\infty,
$$

and it is the $C^*$-norm. The Frobenius norm is also submultiplicative, $\lVert AB\rVert_2\le\lVert A\rVert_2\lVert B\rVert_2$ (Cauchy–Schwarz), but it is not the $C^*$-norm. The nuclear norm satisfies $\lVert AB\rVert_1\le\lVert A\rVert_2\lVert B\rVert_2\le\lVert A\rVert_1\lVert B\rVert_1$.

## The Singular Set

### Definition and Codimension

**Definition.** The **singular set** is

$$
\Sigma=\{A\in M_6(\mathbb{C}):\det A=0\}.
$$

**Theorem.** $\Sigma$ is a complex algebraic hypersurface of complex dimension $35$, real dimension $70$, and real codimension $2$. Its complement is $GL_6(\mathbb{C})$, an open dense subset of real dimension $72$.

**Proof.** The determinant is a nonzero polynomial of degree six; its zero set is a hypersurface. The differential is nonzero at the matrices of rank five, so the hypersurface is smooth there; the dimension is $36-1=35$ complex, $70$ real.

**Corollary (the singular set is a cone).** $\Sigma$ is homogeneous: if $A\in\Sigma$ and $\lambda\in\mathbb{C}$, then $\lambda A\in\Sigma$.

**Proof.** $\det(\lambda A)=\lambda^6\det A$.

**Remark (a cone, but not a null cone).** The singular set is a cone over the projective determinantal variety, but it is not the isotropic cone of the Hermitian form: the form is definite, and its only isotropic vector is $0$. **The word "cone" in "null cone" refers to the isotropic cone of an indefinite form; the determinant cone is a different object.**

### The Rank Stratification

**Definition.** For $k=0,\dots,6$, the **rank-$k$ stratum** is

$$
M_k=\{A:\operatorname{rank}A=k\}.
$$

**Theorem.** $M_k$ is a smooth locally closed submanifold of complex dimension

$$
\dim_{\mathbb{C}}M_k=k(12-k),
$$

and real dimension $2k(12-k)$. The closure of $M_k$ is

$$
\overline{M_k}=\{A:\operatorname{rank}A\le k\},
$$

of complex codimension $(6-k)^2$.

**Proof.** A rank-$k$ matrix factors as $A=UV$ with $U\in\mathbb{C}^{6\times k}$ and $V\in\mathbb{C}^{k\times6}$ of rank $k$. The pair $(U,V)$ has $12k$ complex parameters; the stabilizer of the factorization is $GL_k$, of dimension $k^2$, acting by $U\mapsto UG$, $V\mapsto G^{-1}V$. The quotient has dimension $12k-k^2=k(12-k)$. The closure is the determinantal variety of rank at most $k$, of codimension $(6-k)^2$ in $M_6$.

**Corollary (the table).**

| $k$ | $\dim_{\mathbb{C}}M_k$ | $\dim_{\mathbb{R}}M_k$ | Status |
|---|---|---|---|
| $6$ | $36$ | $72$ | open dense, $GL_6$ |
| $5$ | $35$ | $70$ | smooth part of $\Sigma$ |
| $4$ | $32$ | $64$ | singular locus of $\Sigma$ |
| $3$ | $27$ | $54$ | |
| $2$ | $20$ | $40$ | |
| $1$ | $11$ | $22$ | |
| $0$ | $0$ | $0$ | the zero matrix |

**Proof.** Substitute $k$ in $k(12-k)$ and double for the real dimension.

**Corollary (the singular locus).** The singular locus of $\Sigma$ is

$$
\Sigma_{\mathrm{sing}}=\{A:\operatorname{rank}A\le4\},
$$

of complex dimension $32$ and complex codimension $3$ in $\Sigma$. The smooth locus is $M_5$, of complex dimension $35$.

**Proof.** The gradient of the determinant vanishes exactly at rank at most four; the rank-five stratum is the smooth part of the hypersurface.

**Corollary (the link).** The link of the determinantal cone,

$$
\mathrm{Lk}(\Sigma)=\Sigma\cap S^{71},
$$

has real dimension $69$.

**Proof.** $\Sigma$ has real dimension $70$ and is a cone; intersecting with the unit sphere removes the radial direction, leaving dimension $69$.

**Remark (the rank stratification is the canonical one).** The strata $M_k$ are the orbits of the action of $GL_6\times GL_6$ by $A\mapsto UAV^{-1}$; they are smooth, and the closure order is the order of the ranks. The determinant's singular set is the union of the strata of rank at most five.

## The Absence of a Null Cone

### The Definite Form

**Theorem.** The Hermitian trace form has no nonzero isotropic vector:

$$
\langle A,A\rangle=0\quad\Longleftrightarrow\quad A=0 .
$$

**Corollary.** There is no null cone, no isotropic cone of positive dimension, and no link of a null cone. The only "isotropic" element is the zero matrix.

**Proof.** The form is a sum of squares.

### The Comparison with the Biquaternion Cone

**Theorem (the biquaternion cone).** In the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$, the conjugation is $\mathbb{C}$-linear and the trace form is indefinite. Its null cone is the zero-divisor cone

$$
\mathcal N=\{A\in\mathbb{B}:A\neq0,\ \det A=0\},
$$

of real dimension $6$. The link

$$
\mathrm{Lk}(\mathcal N)=\{A\in\mathcal N:\lVert A\rVert_F=1\}
$$

has real dimension $5$; it is a circle bundle over $\mathbb{P}^1\times\mathbb{P}^1=S^2\times S^2$.

**Proof.** The biquaternion norm is $N(A)=\det A$, and $\operatorname{tr}(A^*A)=2N(A)$; the isotropic vectors are the singular matrices. The rank-one matrices of unit Frobenius norm are $u\otimes v$ with $\lVert u\rVert=\lVert v\rVert=1$, modulo the common phase; the pair of lines gives $S^2\times S^2$, and the relative phase is the circle. The dimension is $2+2+1=5$.

**Corollary (the contrast).**

| Algebra | Form | Isotropic cone | Link |
|---|---|---|---|
| $M_6(\mathbb{C})$ | definite | $\{0\}$ | none |
| $\mathbb{B}$ | indefinite | zero divisors, real dimension $6$ | real dimension $5$ |

**Proof.** The definite form has the single isotropic vector; the indefinite biquaternion form has the zero-divisor cone.

**Remark (the singular set is not the null cone).** The singular set $\Sigma$ of $M_6$ has real codimension two and a link of real dimension $69$; it is a determinantal cone, not an isotropic cone. The biquaternion null cone has real dimension six and a link of real dimension five. **The determinant can vanish on a large cone without the form being indefinite; the two notions of "cone" must not be conflated.**

## Summary

The trace form $\langle A,B\rangle=\operatorname{tr}(A^*B)$ is positive definite; the complex bilinear pairing $\operatorname{tr}(AB)$ is indefinite. The determinant is a degree-six polynomial; its zero set is the singular set

$$
\Sigma=\{\det A=0\},
$$

of complex dimension $35$, real dimension $70$, and real codimension $2$. The rank-$k$ stratum has complex dimension $k(12-k)$:

| $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|---|---|
| $\dim_{\mathbb{C}}M_k$ | $0$ | $11$ | $20$ | $27$ | $32$ | $35$ | $36$ |

The norms are the Schatten norms of the six singular values:

$$
\lVert A\rVert_1=\sum_i\sigma_i,
\qquad
\lVert A\rVert_2=\left(\sum_i\sigma_i^2\right)^{1/2},
\qquad
\lVert A\rVert_\infty=\sigma_1,
$$

the nuclear, Frobenius and operator norms; the operator norm is the $C^*$-norm, and the nuclear norm is its dual.

$$
\boxed{\ \Sigma=\{\det=0\},\quad \operatorname{codim}_{\mathbb{R}}\Sigma=2,\quad \dim_{\mathbb{C}}M_k=k(12-k),\quad \text{no null cone} .\ }
$$

The Hermitian form has the single isotropic vector $0$. The biquaternion algebra has the zero-divisor null cone of real dimension $6$ and link of real dimension $5$. The determinant cone of $M_6$ is not the isotropic cone of a form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle A,B\rangle$ | the Hermitian trace form $\operatorname{tr}(A^*B)$ |
| $\operatorname{tr}(AB)$ | the complex bilinear trace pairing |
| $\sigma_1,\dots,\sigma_6$ | the singular values |
| $\lVert A\rVert_p$ | the Schatten $p$-norm |
| $\lVert A\rVert_1$ | the nuclear norm |
| $\lVert A\rVert_2$ | the Frobenius norm |
| $\lVert A\rVert_\infty$ | the operator norm |
| $\Sigma$ | the singular set $\{\det=0\}$ |
| $M_k$ | the rank-$k$ stratum |
| $\mathcal N$ | the biquaternion null cone |

## Further Reading

- [The Involution and the Hermitian Structure](the-involution-and-the-hermitian-structure-of-m6c.html), for the positive definite form.
- [The Element, the Coordinates and the Trace](the-element-the-coordinates-and-the-trace-of-m6c.html), for the complex bilinear trace pairing.
- [The Rank-Two and Rank-Three Splits](the-rank-two-and-rank-three-splits-of-m6c.html), for the rank strata of the mass block.
- [The Polar Decomposition](the-polar-decomposition-of-m6c.html), for the singular values and the positive factor.
- [The Topology of $M_6(\mathbb{C})$](the-topology-of-m6c.html), for the complement of the singular set and the link.
- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the biquaternion null cone.
- [The Matrix Algebra $M_6(\mathbb{C})$](the-matrix-algebra-m6c.html), for the matrix units and the rank.
