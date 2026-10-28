# __The Element, the Coordinates and the Trace of $M_5(\mathbb{C})$__

## Introduction

An element of $M_5(\mathbb{C})$ is a matrix $A=(A_{ij})$, and the twenty-five entries are its coordinates in the basis of matrix units:

$$
A=\sum_{i,j=1}^{5}A_{ij}E_{ij}.
$$

The coordinates are complex numbers; separating real and imaginary parts gives fifty real coordinates. The **trace** is the linear form

$$
\operatorname{tr}A=\sum_{i=1}^{5}A_{ii},
$$

the sum of the diagonal coordinates. It is the unique (up to scale) linear form invariant under conjugation, and it defines the trace pairing $\langle A,B\rangle=\operatorname{tr}(AB)$, a symmetric nondegenerate complex bilinear form.

This article develops the element from the coordinate side: the matrix units and the coordinates, the real and complex readings, the trace as an invariant linear form, the trace pairing and its dual, the hyperplane $\mathfrak{sl}_5$ of traceless matrices, and the Jordan decomposition $A=S+N$ with its trace. The trace pairing is **not** the positive definite form of the Hilbert space; that form is $\operatorname{tr}(A^*B)$, defined with the conjugate transpose in *The Involution and the Hermitian Structure of $M_5(\mathbb{C})$*. The present article uses the complex bilinear pairing of the algebra, the one that pairs $E_{ij}$ with $E_{ji}$.

The article assumes the matrix algebra of *The Matrix Algebra $M_5(\mathbb{C})$* and the root of *Roots of Unity and the Lagrange Idempotents of $M_5(\mathbb{C})$*. The Jordan decomposition is stated and proved in the finite-dimensional case; the spectral theorem for the Hermitian form, the polar decomposition and the exponential are later articles.

## The Coordinates

### The Matrix Units

**Definition.** The **coordinates** of $A$ are the numbers $A_{ij}$ in the expansion

$$
A=\sum_{i,j=1}^{5}A_{ij}E_{ij}.
$$

The coordinate functional $x_{ij}:M_5\to\mathbb{C}$ is $x_{ij}(A)=A_{ij}$; it is the dual basis element to $E_{ij}$.

**Proposition.** The map $A\mapsto(A_{ij})$ is a linear isomorphism $M_5(\mathbb{C})\cong\mathbb{C}^{25}$. The coordinate functionals satisfy $x_{ij}(E_{kl})=\delta_{ik}\delta_{jl}$, and the product is

$$
(AB)_{ij}=\sum_{k=1}^{5}A_{ik}B_{kj}.
$$

**Proof.** The matrix units are a basis, so the expansion is unique; the coordinate of $E_{kl}$ is the Kronecker delta; the product formula is the definition of the matrix product.

**Corollary.** The algebra is a complex vector space of dimension $25$ and a real vector space of dimension $50$. A real basis is $E_{ij}$ and $iE_{ij}$ for $1\le i,j\le5$.

**Proof.** The $25$ complex coordinates give $25$ complex dimensions; separating real and imaginary parts gives $50$ real coordinates. The real basis is the $25$ units and their $i$-multiples.

### The Real and Complex Readings

**Definition.** Write $A_{ij}=x_{ij}+iy_{ij}$ with $x_{ij},y_{ij}\in\mathbb{R}$. The **real coordinates** of $A$ are the fifty numbers $(x_{ij},y_{ij})$.

**Proposition.** The multiplication is polynomial in the real coordinates, and the conjugation $A\mapsto\bar A$ is the real-linear map $(x_{ij},y_{ij})\mapsto(x_{ij},-y_{ij})$. The algebra is a real algebra of dimension $50$ whose complexification is itself.

**Proof.** The product formula is polynomial with real coefficients in the real and imaginary parts; the conjugation negates the imaginary part. The complex structure is the multiplication by $i$, a real-linear map $J$ with $J^2=-1$; the real algebra with $J$ is the complex algebra.

**Remark.** **The real dimension $50$ is the dimension of the algebra as a real vector space, not the dimension of a real form.** The real form $\mathfrak{u}(5)$ has dimension $25$ and is not the whole algebra; it is the skew-Hermitian half of *The Matrix Algebra*. The fifty real coordinates are the coordinates of the complex algebra read over $\mathbb{R}$; the twenty-five complex coordinates are the coordinates over $\mathbb{C}$.

### The Element as a Vector

**Definition.** The **element** $A$ is the vector of its coordinates; the **scalar part** is $\frac15\operatorname{tr}(A)I$, and the **traceless part** is $A-\frac15\operatorname{tr}(A)I$.

**Proposition.** The map

$$
A\longmapsto\Bigl(\frac15\operatorname{tr}(A)I,\ A-\frac15\operatorname{tr}(A)I\Bigr)
$$

is a direct-sum decomposition

$$
M_5(\mathbb{C})=\mathbb{C}I\oplus\mathfrak{sl}_5(\mathbb{C}),
\qquad \mathfrak{sl}_5=\{A:\operatorname{tr}A=0\},
$$

of complex dimensions $1$ and $24$.

**Proof.** The map is linear; the scalar part is a multiple of $I$ and the traceless part has trace $\operatorname{tr}A-\frac15\operatorname{tr}(A)\operatorname{tr}I=0$. The intersection is zero: a scalar matrix $\lambda I$ with trace $5\lambda=0$ has $\lambda=0$. The dimensions are $1$ and $25-1=24$.

**Corollary.** The trace is the coordinate of the scalar part: $\operatorname{tr}A=5\lambda$ for the scalar part $\lambda I$. The hyperplane $\mathfrak{sl}_5$ is the kernel of the trace.

**Proof.** The trace of $\lambda I$ is $5\lambda$; the traceless part is in the kernel by definition.

## The Trace

### The Invariant Linear Form

**Theorem.** The linear forms $\ell:M_5(\mathbb{C})\to\mathbb{C}$ invariant under conjugation,

$$
\ell(gAg^{-1})=\ell(A)\qquad\text{for all }g\in GL_5(\mathbb{C}),
$$

form the one-dimensional space $\mathbb{C}\operatorname{tr}$.

**Proof.** Let $\ell$ be invariant. Differentiating the identity $\ell(gAg^{-1})=\ell(A)$ at $g=I$ in the direction $X$ gives

$$
\ell([X,A])=0\qquad\text{for all }X,A .
$$

The commutators span the traceless subspace: for $i\ne j$, $E_{ij}=[E_{ii},E_{ij}]$, and $E_{ii}-E_{jj}=[E_{ij},E_{ji}]$; these elements span $\mathfrak{sl}_5$. Hence $\ell$ vanishes on $\mathfrak{sl}_5$, and $\ell(A)=\ell(\frac15\operatorname{tr}(A)I)=\frac15\operatorname{tr}(A)\ell(I)$. So $\ell$ is a multiple of the trace. Conversely the trace is invariant, $\operatorname{tr}(gAg^{-1})=\operatorname{tr}(A)$.

**Corollary.** The trace is the unique invariant linear form with $\operatorname{tr}I=5$. It is the **character** of the defining representation of $GL_5$.

**Proof.** The normalization fixes the multiple; the trace of the identity is $5$.

### The Trace Pairing

**Definition.** The **trace pairing** is

$$
\langle A,B\rangle=\operatorname{tr}(AB).
$$

**Proposition.** The trace pairing is complex bilinear, symmetric and nondegenerate. In the matrix-unit basis,

$$
\langle E_{ij},E_{kl}\rangle=\delta_{il}\delta_{jk},
$$

so the dual basis of $E_{ij}$ is $E_{ji}$.

**Proof.** Bilinearity is the linearity of the trace and of the product; symmetry is $\operatorname{tr}(AB)=\operatorname{tr}(BA)$; the matrix-unit value is $\operatorname{tr}(E_{ij}E_{kl})=\delta_{jk}\operatorname{tr}(E_{il})=\delta_{jk}\delta_{il}$. If $\langle A,B\rangle=0$ for all $B$, testing $B=E_{ji}$ gives $A_{ij}=0$; hence $A=0$.

**Corollary.** The trace pairing identifies $M_5$ with its dual by $A\mapsto\langle A,\cdot\rangle$; the inverse identification sends a linear form $\ell$ to the matrix $\sum_{i,j}\ell(E_{ij})E_{ji}$.

**Proof.** The pairing is nondegenerate, so the map to the dual is an isomorphism; the inverse is read on the basis.

### The Orthogonality and the Adjoint

**Definition.** The **orthogonal complement** of a subspace $W$ is

$$
W^{\perp}=\{A:\langle A,B\rangle=0\text{ for all }B\in W\}.
$$

**Proposition.** $\dim W+\dim W^{\perp}=25$, and $(W^{\perp})^{\perp}=W$.

**Proof.** The pairing is nondegenerate; the orthogonal complement is the annihilator of $W$ under the isomorphism with the dual, of dimension $25-\dim W$; the double complement is $W$.

**Proposition.** The trace pairing is invariant under conjugation and under the adjoint action:

$$
\langle gAg^{-1},gBg^{-1}\rangle=\langle A,B\rangle,\qquad
\langle [A,B],C\rangle+\langle B,[A,C]\rangle=0 .
$$

**Proof.** The first identity is the cyclic invariance of the trace: $\operatorname{tr}(gAg^{-1}gBg^{-1})=\operatorname{tr}(gABg^{-1})=\operatorname{tr}(AB)$. For the second, $\langle [A,B],C\rangle=\operatorname{tr}(ABC-BAC)$ and $\langle B,[A,C]\rangle=\operatorname{tr}(BAC-BCA)$; the sum is $\operatorname{tr}(ABC-BCA)=0$ by cyclicity.

**Corollary.** The adjoint operator $\operatorname{ad}_A$ is skew for the trace pairing: $\langle\operatorname{ad}_A B,C\rangle=-\langle B,\operatorname{ad}_A C\rangle$. The trace form is the invariant bilinear form of the Lie algebra $\mathfrak{gl}_5$.

**Proof.** The second identity is exactly the skew-adjointness.

**Remark.** **The trace pairing is indefinite.** It is a complex bilinear form, not a Hermitian form; $\langle A,A\rangle=\operatorname{tr}(A^2)$ can be zero for a nonzero nilpotent $A$. The positive definite form is $\operatorname{tr}(A^*B)$, which uses the conjugate transpose and is treated in *The Involution and the Hermitian Structure of $M_5(\mathbb{C})$*. The trace pairing is the algebraic pairing of the Frobenius algebra; the definite form is the metric of the Hilbert space.

## The Jordan Decomposition

### The Semisimple and Nilpotent Parts

**Definition.** An element $S$ is **semisimple** if it is diagonalizable; an element $N$ is **nilpotent** if $N^k=0$ for some $k$.

**Theorem (Jordan decomposition).** Every $A\in M_5(\mathbb{C})$ has a unique decomposition

$$
A=S+N,\qquad S\text{ semisimple},\quad N\text{ nilpotent},\quad SN=NS .
$$

Moreover $S=p(A)$ for a polynomial $p$, and $N=A-S$.

**Proof.** Let $\chi_A(t)=\prod_{k=1}^{r}(t-\lambda_k)^{m_k}$ be the characteristic polynomial with distinct roots $\lambda_k$. By the Chinese remainder theorem, choose a polynomial $p$ with

$$
p(t)\equiv\lambda_k\pmod{(t-\lambda_k)^{m_k}},\qquad k=1,\dots,r .
$$

Then $S=p(A)$ commutes with $A$, and $S$ acts on the generalized eigenspace of $\lambda_k$ as $\lambda_k$; hence $S$ is semisimple with the same eigenvalues. The difference $N=A-S$ is nilpotent on each generalized eigenspace, because $A-\lambda_kI$ is nilpotent there and $S-\lambda_kI$ vanishes there; hence $N$ is nilpotent. The parts commute because $S$ is a polynomial in $A$. For uniqueness, if $A=S'+N'$ with $S'$ semisimple, $N'$ nilpotent and $S'N'=N'S'$, then $S'$ commutes with $A$ and preserves each generalized eigenspace; on the generalized eigenspace of $\lambda_k$, $S'$ has the single eigenvalue $\lambda_k$ (because $N'$ is nilpotent and commutes with $S'$), so $S'=S$ and $N'=N$.

**Corollary.** The trace of $A$ is the sum of its eigenvalues with multiplicity, and the trace of $N$ is zero. The determinant is the product of the eigenvalues with multiplicity.

**Proof.** The trace is the sum of the diagonal entries in a triangular form; the eigenvalues are the diagonal entries with multiplicity; $N$ is strictly triangular in a suitable basis, so its trace is zero. The determinant is the product of the diagonal entries.

### The Jordan Form

**Theorem.** Every $A$ is similar to a Jordan matrix: a direct sum of Jordan blocks $J_m(\lambda)$, of size $m$ and eigenvalue $\lambda$, with $1$ on the superdiagonal and $\lambda$ on the diagonal. The semisimple part $S$ is the diagonal part and the nilpotent part $N$ the superdiagonal part of the Jordan form.

**Proof.** The standard Jordan form theorem; the generalized eigenspaces decompose into cyclic subspaces for $A-\lambda I$, each giving a Jordan block. The diagonal part is semisimple, the superdiagonal part nilpotent, and they commute.

**Corollary.** The trace depends only on the eigenvalues and their multiplicities; the nilpotent part does not contribute. Two matrices with the same characteristic polynomial have the same trace and determinant, but not necessarily the same Jordan form.

**Proof.** The trace is the sum of the diagonal entries, which are the eigenvalues; the Jordan form exhibits the diagonal part. The characteristic polynomial records the eigenvalues with multiplicity, not the block sizes.

### The Trace and the Decomposition

**Proposition.** For the Jordan decomposition $A=S+N$,

$$
\operatorname{tr}A=\operatorname{tr}S,\qquad \operatorname{tr}N=0,\qquad \det A=\det S .
$$

**Proof.** $N$ is nilpotent, hence all its eigenvalues are zero, hence its trace is zero and its determinant is zero; the determinant of $A$ is the product of the eigenvalues, which are those of $S$ with multiplicity. The trace of $A$ is the trace of $S$ plus the trace of $N$.

**Remark.** **The trace is blind to the nilpotent part.** The nilpotent part is visible in the Jordan form and in the minimal polynomial, not in the trace or the determinant. The characteristic polynomial records the eigenvalues with multiplicity; the trace and the determinant are the first and last coefficients. The intermediate coefficients are the elementary symmetric functions, which also see only the eigenvalues.

## The Trace and the Determinant

### The Differential

**Proposition.** The differential of the determinant at the identity is the trace:

$$
\det(I+tA)=1+t\operatorname{tr}A+O(t^2),\qquad
d\det_I(A)=\operatorname{tr}A .
$$

**Proof.** Expand the determinant of $I+tA$ by the Leibniz formula; the identity permutation contributes $1$; the transpositions contribute terms of order $t^2$ or higher; the only order-$t$ term is the product of the diagonal entries $1+tA_{ii}$, whose sum is $1+t\operatorname{tr}A$. The higher-order terms are $O(t^2)$.

**Corollary.** The determinant is a local coordinate near the identity, and its level set $\det=1$ is a hypersurface of dimension $24$ through $I$; the tangent space is $\mathfrak{sl}_5$.

**Proof.** The derivative is the nonzero linear form $\operatorname{tr}$; its kernel is $\mathfrak{sl}_5$, of dimension $24$; the level set is a smooth hypersurface by the implicit function theorem.

### The Exponential Identity

**Theorem.** For every $A\in M_5(\mathbb{C})$,

$$
\det(e^A)=e^{\operatorname{tr}A}.
$$

**Proof.** Put $A$ in Jordan form, $A=gJg^{-1}$. Then $e^A=ge^Jg^{-1}$, and both sides are invariant under conjugation: $\det(e^A)=\det(e^J)$ and $\operatorname{tr}A=\operatorname{tr}J$. For a Jordan block $J_m(\lambda)=\lambda I+N$ with $N$ nilpotent, $e^{J_m(\lambda)}=e^\lambda e^N$, and $e^N$ is unipotent with determinant $1$; hence $\det(e^{J_m(\lambda)})=e^{m\lambda}$. The product over the blocks gives $e^{\operatorname{tr}J}=e^{\operatorname{tr}A}$.

**Corollary.** The exponential maps the traceless hyperplane $\mathfrak{sl}_5$ into the special linear group $SL_5$, and $\det(e^A)=1$ if and only if $\operatorname{tr}A\in2\pi i\mathbb{Z}$.

**Proof.** $\det(e^A)=e^{\operatorname{tr}A}=1$ iff $\operatorname{tr}A\in2\pi i\mathbb{Z}$; in particular a traceless $A$ gives determinant $1$.

## Summary

An element $A$ has $25$ complex coordinates $A_{ij}$ in the matrix-unit basis, or $50$ real coordinates. The trace is the sum of the diagonal coordinates; it is the unique conjugation-invariant linear form up to scale, and it defines the symmetric nondegenerate complex bilinear pairing $\langle A,B\rangle=\operatorname{tr}(AB)$, with dual basis $E_{ji}$ to $E_{ij}$.

$$
\boxed{\ \dim_{\mathbb{C}}M_5=25,\quad \dim_{\mathbb{R}}M_5=50,\quad \operatorname{tr}\text{ is the unique invariant linear form},\quad \langle E_{ij},E_{kl}\rangle=\delta_{il}\delta_{jk}.\ }
$$

The algebra splits as $\mathbb{C}I\oplus\mathfrak{sl}_5$, of dimensions $1+24$. Every element has the Jordan decomposition $A=S+N$ with $S$ semisimple, $N$ nilpotent and $SN=NS$; the trace is $\operatorname{tr}S$, the nilpotent part has trace zero, and $\det A=\det S$. The differential of the determinant at $I$ is the trace, and $\det(e^A)=e^{\operatorname{tr}A}$.

| Object | Value |
|---|---|
| Complex coordinates | $25$ |
| Real coordinates | $50$ |
| Trace | $\sum_iA_{ii}$ |
| Invariant linear forms | $\mathbb{C}\operatorname{tr}$ |
| Trace pairing | $\operatorname{tr}(AB)$, symmetric, nondegenerate, indefinite |
| Dual of $E_{ij}$ | $E_{ji}$ |
| Traceless hyperplane $\mathfrak{sl}_5$ | $24$ |
| Jordan decomposition | $A=S+N$, $SN=NS$ |
| Trace of $N$ | $0$ |
| Differential of $\det$ at $I$ | $\operatorname{tr}$ |
| Exponential identity | $\det(e^A)=e^{\operatorname{tr}A}$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A_{ij}$ | The coordinates of $A$ in the matrix-unit basis |
| $x_{ij}$ | The coordinate functional $A\mapsto A_{ij}$ |
| $\operatorname{tr}A$ | The trace, $\sum_iA_{ii}$ |
| $\langle A,B\rangle=\operatorname{tr}(AB)$ | The trace pairing |
| $\mathfrak{sl}_5$ | The traceless matrices, dimension $24$ |
| $S,N$ | The semisimple and nilpotent parts of $A$ |
| $J_m(\lambda)$ | The Jordan block of size $m$ and eigenvalue $\lambda$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the trace, the determinant, the Jordan form and the Jordan decomposition.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the trace form, the invariant linear forms and the Frobenius algebra structure.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the Killing form, the trace form of $\mathfrak{gl}_5$ and the adjoint action.
- [The Matrix Algebra $M_5(\mathbb{C})$](the-matrix-algebra-m5c.html), for the algebra, the matrix units and the trace.
- [The Involution and the Hermitian Structure of $M_5(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m5c.html), for the conjugate transpose and the positive definite form $\operatorname{tr}(A^*B)$.
- [The Forms, the Norms and the Singular Set of $M_5(\mathbb{C})$](the-forms-the-norms-and-the-singular-set-of-m5c.html), for the determinant, the norm and the singular set.
- [The Exponential and the Lie Group of $M_5(\mathbb{C})$](the-exponential-and-the-lie-group-of-m5c.html), for the exponential map and the identity $\det(e^A)=e^{\operatorname{tr}A}$.
