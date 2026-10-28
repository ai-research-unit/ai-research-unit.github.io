# __The Polar Decomposition__

## Introduction

Every $A\in M_6(\mathbb{C})$ factors as

$$
A=UP,
\qquad
U\in U(6),\quad
P=(A^*A)^{1/2}\ge0,
$$

with $P$ positive semidefinite and Hermitian. The factor $P$ is unique; the unitary factor $U$ is unique when $A$ is invertible, and is free on the kernel when $A$ is singular. The decomposition separates the **rotation** $U$ from the **scale** $P$, and it is the matrix form of the singular value decomposition

$$
A=U\Sigma V^*,
\qquad
P=V\Sigma V^*,
\qquad
U_{\mathrm{polar}}=UV^* .
$$

The quotient $GL_6/U(6)$ is the manifold of positive definite Hermitian matrices, of real dimension $36$; the polar decomposition is the diffeomorphism

$$
GL_6\cong U(6)\times\operatorname{Herm}_6^{>0}.
$$

The exponential form is $A=Ue^H$ with $H$ Hermitian; the logarithm of the positive factor is the Hermitian exponent.

The article assumes the unitary group and the Hermitian form of *The Involution and the Hermitian Structure* and the singular values of *The Forms, the Norms and the Singular Set*. It uses the exponential of Hermitian matrices, whose general theory is *The Exponential and the Lie Group*. The mass block's polar decomposition is *The Mass Block and the Chiral Polar Decomposition*; the biquaternion case is *The Polar Decomposition of the Biquaternion Algebra*.

## The Polar Decomposition

### Existence

**Theorem (the right polar decomposition).** Every $A\in M_6(\mathbb{C})$ has a factorization

$$
A=UP,
\qquad
U\in U(6),\quad
P=P^*\ge0,
$$

with $P=(A^*A)^{1/2}$.

**Proof.** $A^*A$ is positive semidefinite, so it has a unique positive semidefinite square root $P$. On the image of $P$, define $U(Px)=Ax$. It is well defined: if $Px=Py$, then $P(x-y)=0$ and

$$
\lVert A(x-y)\rVert^2=\langle x-y,A^*A(x-y)\rangle=\langle x-y,P^2(x-y)\rangle=0,
$$

so $Ax=Ay$. It is isometric:

$$
\lVert Ax\rVert^2=\langle x,A^*Ax\rangle=\langle x,P^2x\rangle=\lVert Px\rVert^2 .
$$

Extend $U$ from the image of $P$ to its orthogonal complement, the kernel of $P$, by any unitary isomorphism onto $(\operatorname{im}A)^\perp$; both complements have dimension $6-\operatorname{rank}A$. Then $U$ is unitary and $UPx=Ax$ for all $x$, so $A=UP$.

**Corollary (the left polar decomposition).** Every $A$ has a factorization

$$
A=P'U,
\qquad
P'=(AA^*)^{1/2}\ge0,\quad
U\in U(6),
$$

and $P'=UPU^*$.

**Proof.** Apply the right polar decomposition to $A^*$: $A^*=VQ$, so $A=QV^*$ with $Q=(AA^*)^{1/2}$ and $V^*\in U(6)$.

### Uniqueness

**Theorem.** The positive factor $P=(A^*A)^{1/2}$ is unique. If $A$ is invertible, the unitary factor is unique as well.

**Proof.** $P$ is determined by $A^*A$. If $A=U_1P_1=U_2P_2$ with $P_i>0$, then $U_2^*U_1=P_2P_1^{-1}$; the left side is unitary, the right side is positive definite, and a unitary positive definite matrix is the identity (its eigenvalues are positive and of modulus one, hence $1$). So $U_1=U_2$ and $P_1=P_2$.

**Corollary (the singular case).** If $A$ has rank $k<6$, the positive factor is unique, and the unitary factor is determined on the image of $P$ and arbitrary on the kernel:

$$
U\big|_{\ker P}\in U(\ker P)\cong U(6-k).
$$

**Proof.** $P$ is unique; on the image of $P$ the map $U$ is determined by $A$; on the kernel of $P$ any unitary extension is allowed. The freedom is the unitary group of the $(6-k)$-dimensional kernel.

### The Singular Value Decomposition

**Theorem (the SVD).** Every $A$ has a factorization

$$
A=U\Sigma V^*,
\qquad
U,V\in U(6),\quad
\Sigma=\operatorname{diag}(\sigma_1,\dots,\sigma_6)\ge0 .
$$

The $\sigma_i$ are the singular values, and

$$
P=V\Sigma V^*,
\qquad
U_{\mathrm{polar}}=UV^* .
$$

**Proof.** Diagonalize $A^*A=V\Sigma^2V^*$. The polar decomposition gives $A=U_{\mathrm{polar}}P$ with $P=V\Sigma V^*$; set $U=U_{\mathrm{polar}}V$. Then

$$
A=U_{\mathrm{polar}}V\Sigma V^*=U\Sigma V^*,
$$

and the polar factor is $U_{\mathrm{polar}}=UV^*$ because

$$
A=(UV^*)(V\Sigma V^*).
$$

**Corollary (the polar decomposition is the SVD with phases separated).** The SVD separates the two unitaries $U,V$; the polar decomposition combines them into $U_{\mathrm{polar}}=UV^*$ and keeps the positive factor $V\Sigma V^*$.

**Proof.** Multiply the two factors.

**Corollary (the singular values are the eigenvalues of $P$).** The eigenvalues of $P$ are $\sigma_1,\dots,\sigma_6$; the eigenvalues of $U_{\mathrm{polar}}$ are the phases of the SVD.

**Proof.** $P=V\Sigma V^*$; the unitary factor $UV^*$ has eigenvalues on the unit circle.

## The Manifold $GL_6/U(6)$

### The Positive Cone

**Definition.** The **positive cone** is

$$
\operatorname{Herm}_6^{>0}=\{P\in M_6(\mathbb{C}):P=P^*,\ P>0\}.
$$

**Theorem.** $\operatorname{Herm}_6^{>0}$ is an open convex cone in the real vector space $\operatorname{Herm}_6$ of real dimension $36$.

**Proof.** The Hermitian matrices form a real vector space of dimension $36$; the positive definite ones are defined by the positivity of the six principal minors, which are open conditions; convexity follows from $\langle x,((1-t)P+tQ)x\rangle=(1-t)\langle x,Px\rangle+t\langle x,Qx\rangle>0$.

### The Symmetric Space

**Theorem (the polar diffeomorphism).** The map

$$
U(6)\times\operatorname{Herm}_6^{>0}\longrightarrow GL_6,
\qquad
(U,P)\longmapsto UP
$$

is a diffeomorphism. Hence

$$
GL_6/U(6)\cong\operatorname{Herm}_6^{>0},
\qquad
\dim_{\mathbb{R}}GL_6/U(6)=36 .
$$

**Proof.** The polar decomposition gives the map and its inverse $A\mapsto(U,P)$; it is smooth because $P=(A^*A)^{1/2}$ and $U=AP^{-1}$ are smooth on the invertible locus. The dimensions add: $36+36=72$.

**Corollary (the principal bundle).** $GL_6$ is a principal $U(6)$-bundle over the positive cone, with fibre $U(6)$.

**Proof.** The action of $U(6)$ on $GL_6$ by left multiplication is free, and the quotient is the positive cone by the polar decomposition.

**Remark (the symmetric space).** The quotient is the symmetric space of the Cartan involution $\theta(A)=-A^*$; the geodesics are the curves $P^{1/2}e^{tH}P^{1/2}$? The exponential of Hermitian matrices gives the geodesics through the identity. The metric is the Hilbert–Schmidt metric.

## The Singular Element

### The Freedom on the Kernel

**Theorem.** Let $A$ have rank $k$ and polar decomposition $A=U_0P$. Then the polar factors of $A$ are exactly

$$
U=U_0V,
\qquad
V\in U(\ker P)\cong U(6-k),
$$

with $V$ acting as the identity on the image of $P$. The set is a coset of $U(6-k)$, of real dimension $(6-k)^2$.

**Proof.** Any other unitary factor differs from $U_0$ by a unitary that commutes with $P$ on the image and is arbitrary on the kernel; the kernel is $\ker P=\ker A$, of dimension $6-k$.

**Corollary (the image and the kernel).** The polar factor maps

$$
\operatorname{im}P\longrightarrow\operatorname{im}A,
\qquad
\ker P\longrightarrow(\operatorname{im}A)^\perp,
$$

and is arbitrary on the second factor.

**Proof.** $A=UP$; $U$ is unitary, so $U((\operatorname{im}P)^\perp)=(\operatorname{im}A)^\perp$; the kernel of $P$ is the orthogonal complement of the image of $P$.

### The Limit at a Singular Element

**Theorem.** The positive factor $P(A)=(A^*A)^{1/2}$ is continuous everywhere. The unitary factor $U(A)$ is continuous on the invertible locus; at a singular element it may fail to have a limit, and when it has one, the limit depends on the direction of approach.

**Proof.** The square root is continuous; $U=AP^{-1}$ is continuous where $P$ is invertible. On the singular locus, the freedom on the kernel is a coset, and different approaches select different points of the coset.

**Example.** For $A(\varepsilon)=\operatorname{diag}(1,\varepsilon e^{\mathrm i\theta})$ with $\varepsilon>0$, the polar factor is $\operatorname{diag}(1,e^{\mathrm i\theta})$, which tends to $\operatorname{diag}(1,e^{\mathrm i\theta})$ as $\varepsilon\to0$; the limit depends on $\theta$. The positive factor tends to $\operatorname{diag}(1,0)$ independently of $\theta$.

**Corollary (the polar map is not continuous at the singular set).** The map $A\mapsto U(A)$ does not extend continuously to the singular matrices.

**Proof.** The example gives two approaches with different limits.

## The Exponential Form

### The Exponential of Hermitian Matrices

**Theorem.** The exponential map

$$
\exp:\operatorname{Herm}_6\longrightarrow\operatorname{Herm}_6^{>0},
\qquad
H\longmapsto e^H
$$

is a diffeomorphism.

**Proof.** For Hermitian $H$, $e^H$ is Hermitian positive definite (diagonalize $H$ unitarily: $H=U\operatorname{diag}(h_i)U^*$, $e^H=U\operatorname{diag}(e^{h_i})U^*$). The inverse is the logarithm $P\mapsto\log P$, defined by the spectral theorem; both maps are smooth.

### The Exponential Polar Decomposition

**Theorem.** Every invertible $A$ has a unique factorization

$$
A=Ue^H,
\qquad
U\in U(6),\quad
H\in\operatorname{Herm}_6 .
$$

**Proof.** The polar decomposition $A=UP$ with $P>0$; write $P=e^H$ with $H=\log P$ Hermitian. Uniqueness follows from the uniqueness of the polar decomposition and of the logarithm.

**Corollary (the Cartan decomposition).** The map

$$
U(6)\times\operatorname{Herm}_6\longrightarrow GL_6,
\qquad
(U,H)\longmapsto Ue^H
$$

is a diffeomorphism, and

$$
\mathfrak{gl}_6=\mathfrak{u}(6)\oplus\mathrm i\mathfrak{u}(6),
\qquad
\dim_{\mathbb{R}}GL_6=36+36=72 .
$$

**Proof.** The polar diffeomorphism and the exponential diffeomorphism compose; the Lie algebra decomposition is the derivative at the identity.

### The Exponential Form of the SVD

**Theorem.** With $A=U\Sigma V^*$ and $\Sigma>0$,

$$
A=U_{\mathrm{polar}}e^H,
\qquad
U_{\mathrm{polar}}=UV^*,
\qquad
H=V(\log\Sigma)V^* .
$$

**Proof.** $V\Sigma V^*=e^{V(\log\Sigma)V^*}$; multiply by $UV^*$.

**Corollary (the singular values are the exponents).** The eigenvalues of $H$ are $\log\sigma_1,\dots,\log\sigma_6$; the singular values are the exponentials of the Hermitian spectrum.

**Proof.** $H$ is unitarily equivalent to $\operatorname{diag}(\log\sigma_i)$.

## Summary

Every $A\in M_6(\mathbb{C})$ has the polar decomposition

$$
A=UP,
\qquad
U\in U(6),\quad
P=(A^*A)^{1/2}\ge0 .
$$

The positive factor is unique; the unitary factor is unique for invertible $A$ and free on the kernel for singular $A$, with freedom $U(6-k)$ of real dimension $(6-k)^2$. The SVD is

$$
A=U\Sigma V^*,
\qquad
P=V\Sigma V^*,
\qquad
U_{\mathrm{polar}}=UV^* .
$$

$$
\boxed{\ A=UP,\qquad GL_6/U(6)\cong\operatorname{Herm}_6^{>0},\qquad \dim_{\mathbb{R}}=36,\qquad A=Ue^H .\ }
$$

The polar decomposition is the diffeomorphism $GL_6\cong U(6)\times\operatorname{Herm}_6^{>0}$; the quotient is the positive cone, the symmetric space of the Cartan involution. The exponential form is $A=Ue^H$ with $H$ Hermitian; the Cartan decomposition is $\mathfrak{gl}_6=\mathfrak{u}(6)\oplus\mathrm i\mathfrak{u}(6)$.

| Object | Data |
|---|---|
| Polar decomposition | $A=UP$, $U\in U(6)$, $P\ge0$ |
| Positive factor | $P=(A^*A)^{1/2}$, unique |
| Unitary factor | unique if $A$ invertible |
| Singular freedom | $U(6-k)$, dimension $(6-k)^2$ |
| SVD | $A=U\Sigma V^*$ |
| Quotient | $GL_6/U(6)\cong\operatorname{Herm}_6^{>0}$ |
| Dimension | $36$ |
| Exponential form | $A=Ue^H$, $H$ Hermitian |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P=(A^*A)^{1/2}$ | the positive factor |
| $U$ | the unitary polar factor |
| $\sigma_1,\dots,\sigma_6$ | the singular values |
| $\operatorname{Herm}_6^{>0}$ | the positive definite Hermitian cone |
| $GL_6/U(6)$ | the symmetric space of the polar decomposition |
| $H=\log P$ | the Hermitian exponent |

## Further Reading

- [The Involution and the Hermitian Structure](the-involution-and-the-hermitian-structure-of-m6c.html), for the unitary group and the positive definite form.
- [The Forms, the Norms and the Singular Set](the-forms-the-norms-and-the-singular-set-of-m6c.html), for the singular values.
- [The Mass Block and the Chiral Polar Decomposition](the-mass-block-and-the-chiral-polar-decomposition-of-m6c.html), for the polar decomposition of the mass block.
- [The Exponential and the Lie Group](the-exponential-and-the-lie-group-of-m6c.html), for the exponential of Hermitian matrices.
- [Spectral Theory and the Spectral Projectors](spectral-theory-and-the-spectral-projectors-of-m6c.html), for the spectral theorem behind the square root.
- [The Polar Decomposition of the Biquaternion Algebra](the-polar-decomposition-of-the-biquaternion-algebra.html), for the rank-one case.
- [The Polar Decomposition](the-polar-decomposition.html), for the general theory in a Hilbert space.
- [Symmetric Spaces](symmetric-spaces.html), for the Cartan decomposition and the positive cone.
