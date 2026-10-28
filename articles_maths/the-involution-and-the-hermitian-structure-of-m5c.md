# __The Involution and the Hermitian Structure__

## Introduction

The conjugate transpose

$$
A^*=\bar A^{\mathsf T},\qquad (A^*)_{ij}=\overline{A_{ji}},
$$

is an involutive, conjugate-linear anti-automorphism of $M_5(\mathbb{C})$:

$$
(A^*)^*=A,\qquad (AB)^*=B^*A^*,\qquad (\lambda A)^*=\bar\lambda A^* .
$$

It is an involution of the **real** algebra, not of the complex algebra. Its fixed points are the Hermitian matrices, its anti-fixed points the skew-Hermitian matrices, and the two real subspaces

$$
\mathfrak{u}(5)=\{X:X^*=-X\},\qquad i\mathfrak{u}(5)=\{H:H^*=H\}
$$

give the real decomposition $M_5=\mathfrak{u}(5)\oplus i\mathfrak{u}(5)$, of real dimensions $25+25=50$. The skew-Hermitian part is the compact real form $\mathfrak{u}(5)$, of real dimension $25$, and its traceless part $\mathfrak{su}(5)$ has dimension $24$.

The involution defines the **positive definite** Hermitian form on the algebra,

$$
\langle A,B\rangle_F=\operatorname{tr}(A^*B),
$$

the Frobenius form, with norm

$$
\|A\|_F^2=\operatorname{tr}(A^*A)=\sum_{i,j}|A_{ij}|^2 .
$$

This is the Hilbert space structure on $M_5(\mathbb{C})\cong\mathbb{C}^{25}\cong\mathbb{R}^{50}$; it is positive definite, and it has **no null cone**. The complex bilinear trace pairing $\operatorname{tr}(AB)$ of *The Element, the Coordinates and the Trace* is a different object; it is indefinite, and its isotropic cone is not the metric.

The **singular set** of the algebra is the zero locus of the determinant,

$$
\Sigma=\{A:\det A=0\},
$$

a complex hypersurface of **real codimension $2$** in $M_5(\mathbb{C})\cong\mathbb{R}^{50}$: the determinant is a complex polynomial, and its vanishing imposes one complex equation, equivalently two real equations. The complement $GL_5(\mathbb{C})$ is connected and dense. The singular set is not a null cone of the positive definite form, and there are no nonzero null vectors.

The article assumes the matrix algebra and the trace. The spectral theorem for Hermitian matrices, the polar decomposition and the exponential are later articles; the present one fixes the involution, the form and the real form on which they rest.

## The Conjugate Transpose

### The Involution

**Definition.** The **conjugate transpose** of $A$ is $A^*=\bar A^{\mathsf T}$.

**Proposition.** The map $A\mapsto A^*$ is conjugate-linear and involutive, and it reverses products:

$$
(A+B)^*=A^*+B^*,\qquad (\lambda A)^*=\bar\lambda A^*,\qquad (A^*)^*=A,\qquad (AB)^*=B^*A^* .
$$

**Proof.** The entries of $(AB)^*$ are $\overline{(AB)_{ji}}=\sum_k\overline{A_{jk}B_{ki}}=\sum_k\bar B_{ki}\bar A_{jk}=(B^*A^*)_{ji}$. The other identities are entrywise.

**Corollary.** The conjugate transpose is an involution of the real algebra $M_5(\mathbb{C})$, and the transpose $A^{\mathsf T}$ is a complex-linear anti-automorphism but not the Hermitian involution. The two coincide on real matrices.

**Proof.** The star is conjugate-linear by $(\lambda A)^*=\bar\lambda A^*$; the transpose is complex-linear and satisfies $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$. On real matrices the conjugation is trivial.

**Remark.** **An involution of a complex algebra is by definition conjugate-linear; a complex-linear anti-automorphism is a different notion.** The star is the involution that makes $M_5(\mathbb{C})$ a complex algebra with involution in the sense of *The Book of Involutions*; the transpose is the transpose. The distinction matters: the Hermitian matrices are the fixed points of the star, not of the transpose.

### Hermitian and Skew-Hermitian

**Definition.** $A$ is **Hermitian** if $A^*=A$ and **skew-Hermitian** if $A^*=-A$.

**Proposition.** The Hermitian and skew-Hermitian matrices form real subspaces of dimension $25$ each, and

$$
M_5(\mathbb{C})=\mathfrak{u}(5)\oplus i\mathfrak{u}(5),
\qquad
A=\underbrace{\tfrac12(A-A^*)}_{\text{skew-Hermitian}}+\underbrace{\tfrac12(A+A^*)}_{\text{Hermitian}} .
$$

**Proof.** The two projections are real-linear, idempotent and sum to the identity; the first is skew-Hermitian and the second Hermitian; their intersection is zero because a matrix both Hermitian and skew-Hermitian satisfies $A=-A$. A skew-Hermitian matrix has purely imaginary diagonal entries (five real parameters) and arbitrary complex entries above the diagonal (ten complex $=20$ real), total $25$; the Hermitian matrices have real diagonal entries and arbitrary complex entries above the diagonal, also $25$.

**Corollary.** The real dimension of $\mathfrak{u}(5)$ is $25$, and the real dimension of the traceless subspace $\mathfrak{su}(5)$ is $24$.

**Proof.** The trace of a skew-Hermitian matrix is purely imaginary; the condition $\operatorname{tr}X=0$ is one real linear equation on the $25$-dimensional space.

### The Real Form

**Theorem.** The complexification of the real Lie algebra $\mathfrak{u}(5)$ is $\mathfrak{gl}_5(\mathbb{C})$:

$$
\mathbb{C}\otimes_{\mathbb{R}}\mathfrak{u}(5)\cong\mathfrak{gl}_5(\mathbb{C}),\qquad X\otimes(a+ib)\longmapsto aX+b\,iX .
$$

The complexification of $\mathfrak{su}(5)$ is $\mathfrak{sl}_5(\mathbb{C})$.

**Proof.** Every $A$ is $X+iY$ with $X=\frac12(A-A^*)\in\mathfrak{u}(5)$ and $Y=\frac12(A+A^*)\in i\mathfrak{u}(5)$; writing $Y=iH$ with $H=-iY\in\mathfrak{u}(5)$ gives $A=X+iH$. The complex dimensions are $25$ and $25$, so the surjection is an isomorphism. The traceless case is the same with the trace condition.

**Corollary.** $\mathfrak{u}(5)$ is the **compact real form** of $\mathfrak{gl}_5(\mathbb{C})$, and $\mathfrak{su}(5)$ is the compact real form of $\mathfrak{sl}_5(\mathbb{C})$. The Hermitian matrices $i\mathfrak{u}(5)$ are the other real half of the complexification.

**Proof.** The real form $\mathfrak{u}(5)$ is the fixed-point set of the Cartan involution $\theta(A)=-A^*$; the fixed points of $\theta$ are the skew-Hermitian matrices, and the $-1$ eigenspace is the Hermitian matrices. The form is compact because the Killing form is negative definite on $\mathfrak{u}(5)$.

## The Hermitian Form on the Carrier

### The Standard Form

**Definition.** The **standard Hermitian form** on $V=\mathbb{C}^5$ is

$$
\langle x,y\rangle=\sum_{i=1}^{5}\bar x_iy_i,\qquad x,y\in\mathbb{C}^5 .
$$

**Proposition.** The form is Hermitian, positive definite and nondegenerate:

$$
\langle x,y\rangle=\overline{\langle y,x\rangle},\qquad
\langle x,x\rangle=\sum_i|x_i|^2>0\quad(x\ne0).
$$

**Proof.** The conjugate symmetry is the conjugation of the sum; the positivity is the sum of the squares of the absolute values, which is positive for a nonzero vector.

**Corollary.** The standard basis $e_1,\dots,e_5$ is orthonormal, $\langle e_i,e_j\rangle=\delta_{ij}$. The form identifies $V$ with its conjugate dual.

**Proof.** The inner product of two standard basis vectors is the Kronecker delta; the identification is $y\mapsto\langle\cdot,y\rangle$.

### The $*$-Unitary Group

**Definition.** The **$*$-unitary group** is

$$
U(5)=\{U\in GL_5(\mathbb{C}):U^*U=I\},
$$

and the **special $*$-unitary group** is $SU(5)=U(5)\cap SL_5(\mathbb{C})$.

**Proposition.** $U(5)$ is the group of linear isometries of the standard Hermitian form; it is a compact real Lie group of real dimension $25$. Its Lie algebra is $\mathfrak{u}(5)$, and the Lie algebra of $SU(5)$ is $\mathfrak{su}(5)$, of real dimension $24$.

**Proof.** A linear map preserves the form iff $U^*U=I$. The group is the zero set of the polynomial equations $U^*U=I$, hence closed and bounded in $M_5\cong\mathbb{R}^{50}$ (the columns are orthonormal), hence compact. The tangent space at $I$ is $\{X:X^*=-X\}=\mathfrak{u}(5)$; the traceless condition gives $\mathfrak{su}(5)$.

**Corollary.** For $X\in\mathfrak{u}(5)$ and $t\in\mathbb{R}$, the exponential $e^{tX}$ is $*$-unitary; the map $t\mapsto e^{tX}$ is a one-parameter subgroup of $U(5)$.

**Proof.** $(e^{tX})^*=e^{tX^*}=e^{-tX}=(e^{tX})^{-1}$.

### The Orthonormal Basis

**Proposition.** The basis

$$
iE_{ii},\quad \frac{i(E_{ij}+E_{ji})}{\sqrt2},\quad \frac{E_{ij}-E_{ji}}{\sqrt2}
\qquad(i<j)
$$

is an orthonormal basis of $\mathfrak{u}(5)$ for the positive definite form $\operatorname{tr}(X^*Y)=-\operatorname{tr}(XY)$; its cardinality is $5+10+10=25$.

**Proof.** The matrices $iE_{ii}$ are skew-Hermitian, the matrices $i(E_{ij}+E_{ji})$ are skew-Hermitian, and the matrices $E_{ij}-E_{ji}$ are real skew-symmetric, hence skew-Hermitian. The trace pairings give $\operatorname{tr}(X^*X)=1$ for each normalized basis element and $0$ for distinct ones: for the diagonal, $\operatorname{tr}((iE_{ii})^*(iE_{ii}))=\operatorname{tr}(E_{ii})=1$; for the off-diagonal, the two entries of the symmetric or antisymmetric combination give trace $2$, divided by $2$. The count is $5$ diagonal $+10$ symmetric $+10$ antisymmetric $=25$.

**Corollary.** The form $-\operatorname{tr}(XY)$ is positive definite on $\mathfrak{u}(5)$; it is the restriction of the Frobenius form to the skew-Hermitian half.

**Proof.** For $X\in\mathfrak{u}(5)$, $-\operatorname{tr}(X^2)=\operatorname{tr}(X^*X)=\|X\|_F^2>0$ for $X\ne0$.

## The Trace Form on the Algebra

### The Positive Definite Form

**Definition.** The **Frobenius form** on $M_5(\mathbb{C})$ is

$$
\langle A,B\rangle_F=\operatorname{tr}(A^*B).
$$

**Theorem.** The Frobenius form is a positive definite Hermitian inner product:

$$
\langle A,B\rangle_F=\overline{\langle B,A\rangle}_F,\qquad
\langle A,A\rangle_F=\|A\|_F^2=\sum_{i,j}|A_{ij}|^2>0\quad(A\ne0).
$$

**Proof.** The conjugate symmetry: $\overline{\operatorname{tr}(A^*B)}=\operatorname{tr}(B^*A)$. The positivity: $(A^*A)_{ii}=\sum_k\bar A_{ki}A_{ki}=\sum_k|A_{ki}|^2$, so the trace is the sum of the absolute squares of all entries, positive for $A\ne0$.

**Corollary.** The form is nondegenerate, and the map $A\mapsto\langle A,\cdot\rangle_F$ identifies $M_5$ with its conjugate dual. The Hilbert space dimension is $25$ complex, $50$ real.

**Proof.** Positive definiteness implies nondegeneracy; the real dimension is twice the complex dimension.

**Remark.** **The Frobenius form and the trace pairing are different.** The trace pairing $\operatorname{tr}(AB)$ is complex bilinear and indefinite; the Frobenius form $\operatorname{tr}(A^*B)$ is Hermitian and positive definite. The first pairs $E_{ij}$ with $E_{ji}$; the second pairs $E_{ij}$ with $E_{ij}$:
$$
\langle E_{ij},E_{kl}\rangle_F=\delta_{ik}\delta_{jl}.
$$
The Frobenius form is the Hilbert space metric; the trace pairing is the algebraic form of the Frobenius algebra.

### The Frobenius Norm

**Definition.** The **Frobenius norm** is $\|A\|_F=\sqrt{\operatorname{tr}(A^*A)}$.

**Proposition.** The Frobenius norm is a norm, and it is unitarily invariant:

$$
\|UAV\|_F=\|A\|_F\qquad(U,V\in U(5)).
$$

**Proof.** The norm is the Euclidean norm of the $25$ complex coordinates; the triangle inequality and homogeneity are those of the Euclidean norm. For $*$-unitary $U,V$, $(UAV)^*(UAV)=V^*A^*U^*UAV=V^*A^*AV$, which has the same trace as $A^*A$ by cyclicity.

**Corollary.** The $*$-unitary group acts on $M_5$ by isometries of the Frobenius form, on the left and on the right.

**Proof.** $\langle U A,V B\rangle_F=\operatorname{tr}(A^*U^*VB)$; for $U=V$ $*$-unitary this is $\operatorname{tr}(A^*B)$; the left action is $*$-unitary. The right action is the same with $A\mapsto AU$.

### The Hilbert Space

**Theorem.** $M_5(\mathbb{C})$ with the Frobenius form is a complex Hilbert space of dimension $25$ (real dimension $50$). The left and right regular representations of $U(5)$ are $*$-unitary, and the adjoint representation of $U(5)$ is $*$-unitary.

**Proof.** A finite-dimensional inner product space is complete, hence a Hilbert space. The left and right actions preserve the form by the proposition; the adjoint action $A\mapsto UAU^{-1}$ is the composition of the left and right actions with $U^{-1}=U^*$, hence $*$-unitary.

**Corollary.** The Hilbert space structure is the one used in *The Polar Decomposition* and *Analysis on $M_5(\mathbb{C})$*: the norm, the inner product and the orthogonal projection onto a subspace are those of the Frobenius form.

**Proof.** The form is positive definite; the orthogonal projection is defined by the inner product.

## The $*$-Unitary Action

### The Left and Right Actions

**Definition.** The **left** and **right regular actions** of $U(5)$ on $M_5$ are

$$
L_U(A)=UA,\qquad R_U(A)=AU .
$$

**Proposition.** Both actions are $*$-unitary for the Frobenius form, and they commute. The map $(U,V)\mapsto L_UR_V$ is an action of $U(5)\times U(5)$.

**Proof.** $\langle UA,UB\rangle_F=\operatorname{tr}(A^*U^*UB)=\operatorname{tr}(A^*B)$; $\langle AU,BU\rangle_F=\operatorname{tr}(U^*A^*BU)=\operatorname{tr}(A^*B)$; the actions commute because $UAV$ is associative.

**Corollary.** The algebra $M_5$ decomposes under $U(5)\times U(5)$ as $V\otimes V^*$, the tensor product of the defining representation and its dual; the decomposition is the Peter–Weyl decomposition of the regular representation.

**Proof.** The left action is on the first factor and the right action on the second; the identification $M_5\cong V\otimes V^*$ sends $v\otimes\ell$ to $v\ell$. The decomposition is the standard tensor product.

### The Adjoint Action

**Definition.** The **adjoint action** of $U(5)$ is

$$
\operatorname{Ad}_U(A)=UAU^{-1}=UAU^*.
$$

**Proposition.** The adjoint action is $*$-unitary, and it preserves the Hermitian and skew-Hermitian subspaces; it preserves the trace and the determinant.

**Proof.** It is the composition of the left and right $*$-unitary actions; $(UAU^*)^*=UA^*U^*$, so Hermitian and skew-Hermitian elements are preserved; the trace and determinant are conjugation-invariant.

**Corollary.** The adjoint orbit of $A$ is contained in the set of matrices with the same characteristic polynomial; the orbit is a submanifold of the Frobenius sphere of radius $\|A\|_F$.

**Proof.** The characteristic polynomial is conjugation-invariant; the Frobenius norm is invariant, so the orbit lies in the sphere of that radius.

### The Compact Real Form

**Theorem.** The Lie algebra $\mathfrak{u}(5)$ is the compact real form of $\mathfrak{gl}_5(\mathbb{C})$, and the exponential map $\mathfrak{u}(5)\to U(5)$ is surjective.

**Proof.** The compactness is the closed boundedness of $U(5)$; the real form is the skew-Hermitian subspace. The surjectivity of the exponential is the standard theorem for compact connected Lie groups: every $*$-unitary matrix is diagonalizable by a $*$-unitary matrix, $U=VDV^*$ with $D=\operatorname{diag}(e^{i\theta_1},\dots,e^{i\theta_5})$, and $U=e^{iH}$ with $H=V\operatorname{diag}(\theta_1,\dots,\theta_5)V^*\in\mathfrak{u}(5)$.

**Corollary.** Every $*$-unitary matrix is the exponential of a skew-Hermitian matrix, and every special $*$-unitary matrix is the exponential of a traceless skew-Hermitian matrix.

**Proof.** The diagonal angles can be chosen with sum zero for determinant one; the traceless condition is the sum of the angles.

## The Singular Set

### The Determinant

**Definition.** The **singular set** is $\Sigma=\{A:\det A=0\}$; its complement is $GL_5(\mathbb{C})$.

**Proposition.** $\Sigma$ is a complex algebraic hypersurface, of complex dimension $24$ and real dimension $48$.

**Proof.** The determinant is a nonconstant polynomial on $M_5\cong\mathbb{C}^{25}$; its zero locus is a hypersurface, of complex dimension $24$. The real dimension is twice the complex dimension, $48$.

**Corollary.** $\Sigma$ is the set of matrices of rank at most $4$; it is the union of the determinantal varieties of rank $k$, $k=0,\dots,4$, with the rank-$4$ locus dense in $\Sigma$.

**Proof.** A matrix is singular iff its rank is at most $4$; the rank-$4$ matrices are the smooth points of $\Sigma$, and the lower-rank loci are the singular strata.

### Real Codimension 2

**Theorem.** The singular set $\Sigma$ has **real codimension $2$** in $M_5(\mathbb{C})\cong\mathbb{R}^{50}$: at a smooth point, the determinant is a complex-valued function with nonzero complex derivative, so its zero set is locally the zero set of one complex equation, equivalently two independent real equations.

**Proof.** At a point $A$ of rank $4$, the derivative of $\det$ is the linear form $H\mapsto\operatorname{tr}(\operatorname{adj}(A)H)$, which is nonzero. A nonzero complex-linear functional from $\mathbb{C}^{25}$ to $\mathbb{C}$ has real and imaginary parts that are independent real linear functionals; its kernel has real codimension $2$. The zero set is a complex hypersurface, of real codimension $2$.

**Corollary.** The complement $GL_5(\mathbb{C})$ is connected and dense. A path between two invertible matrices can be chosen to avoid $\Sigma$, because the obstacle has real codimension $2$, not $1$.

**Proof.** The complement of a complex hypersurface in $\mathbb{C}^{25}$ is path-connected; the real codimension $2$ allows a small generic perturbation of a path to avoid the zeros. The density is the density of a nonempty Zariski open set.

### No Null Cone

**Theorem.** The Frobenius form is positive definite, so it has **no null cone**: the only vector $A$ with $\langle A,A\rangle_F=0$ is $A=0$. The singular set $\Sigma$ is not the null cone of the form.

**Proof.** $\langle A,A\rangle_F=\sum_{i,j}|A_{ij}|^2=0$ iff every entry is zero. The set $\Sigma$ is the zero locus of the determinant, a complex hypersurface; it contains nonzero matrices, so it is not the null set of the positive definite form.

**Corollary.** The complex bilinear trace pairing $\operatorname{tr}(AB)$ has an isotropic cone $\{A:\operatorname{tr}(A^2)=0\}$, but that cone is not the metric and is not the singular set. The positive definite form and the indefinite pairing must not be confused.

**Proof.** The nilpotent matrices satisfy $\operatorname{tr}(A^2)=0$; the trace pairing is indefinite. The Frobenius form is positive definite, so it has no isotropic vectors.

**Remark.** **The singular set is $\det=0$, of real codimension $2$, and it is not a null cone.** The phrase "null cone" belongs to an indefinite bilinear form; the Frobenius form is positive definite and has none. The complex hypersurface $\det=0$ is a codimension-two real obstacle, and the complement $GL_5$ is connected. This is the metric picture of *The Forms, the Norms and the Singular Set*, where the determinant and the norm are treated algebraically.

## Summary

The conjugate transpose $A^*=\bar A^{\mathsf T}$ is the involution of the real algebra $M_5(\mathbb{C})$; its fixed points are the Hermitian matrices and its anti-fixed points the skew-Hermitian matrices. The real decomposition is

$$
M_5(\mathbb{C})=\mathfrak{u}(5)\oplus i\mathfrak{u}(5),
\qquad 25+25=50,
$$

with $\mathfrak{u}(5)$ the compact real form of real dimension $25$ and $\mathfrak{su}(5)$ its traceless part of real dimension $24$.

$$
\boxed{\ \langle A,B\rangle_F=\operatorname{tr}(A^*B)\text{ is positive definite};\quad \Sigma=\{\det=0\}\text{ has real codimension }2;\quad \text{no null cone.}\ }
$$

The Frobenius form is the Hilbert space structure on $M_5\cong\mathbb{C}^{25}\cong\mathbb{R}^{50}$; the $*$-unitary group $U(5)$ acts by isometries on the left, on the right and by conjugation. The singular set is the complex hypersurface of singular matrices, of real codimension $2$; its complement $GL_5$ is connected and dense. There is no null cone: the only null vector of the positive definite form is zero.

| Object | Value |
|---|---|
| Involution | $A^*=\bar A^{\mathsf T}$, conjugate-linear |
| Hermitian matrices | $A^*=A$, real dimension $25$ |
| Skew-Hermitian matrices | $A^*=-A$, real dimension $25$ |
| Compact real form | $\mathfrak{u}(5)$, real dimension $25$ |
| Special $*$-unitary | $\mathfrak{su}(5)$, real dimension $24$ |
| Frobenius form | $\operatorname{tr}(A^*B)$, positive definite |
| Frobenius norm | $\sum_{ij}|A_{ij}|^2$ |
| Singular set | $\det=0$, real codimension $2$ |
| Null cone | none |
| $GL_5(\mathbb{C})$ | connected and dense |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A^*=\bar A^{\mathsf T}$ | The conjugate transpose |
| $\mathfrak{u}(5)$ | The skew-Hermitian matrices, the compact real form |
| $\mathfrak{su}(5)$ | The traceless skew-Hermitian matrices |
| $\langle x,y\rangle=\sum\bar x_iy_i$ | The standard Hermitian form on $\mathbb{C}^5$ |
| $U(5)$, $SU(5)$ | The $*$-unitary and special $*$-unitary groups |
| $\langle A,B\rangle_F=\operatorname{tr}(A^*B)$ | The Frobenius form |
| $\|A\|_F$ | The Frobenius norm |
| $\Sigma=\{\det=0\}$ | The singular set, real codimension $2$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the conjugate transpose, the Hermitian matrices and the $*$-unitary group.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions of a central simple algebra and the $*$-unitary groups.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, second edition, 2015), for the compact real form $\mathfrak{u}(5)$, the exponential of a skew-Hermitian matrix and the $*$-unitary group.
- [The Matrix Algebra $M_5(\mathbb{C})$](the-matrix-algebra-m5c.html), for the algebra, the conjugate transpose and the real form.
- [The Element, the Coordinates and the Trace](the-element-the-coordinates-and-the-trace-of-m5c.html), for the trace, the trace pairing and the Jordan decomposition.
- [The Forms, the Norms and the Singular Set](the-forms-the-norms-and-the-singular-set-of-m5c.html), for the determinant and the singular set.
- [Spectral Theory and the Spectral Projectors](spectral-theory-and-the-spectral-projectors-of-m5c.html), for the spectral theorem for Hermitian matrices.
- [The Polar Decomposition](the-polar-decomposition-of-m5c.html), for the polar decomposition with respect to the Frobenius form.
