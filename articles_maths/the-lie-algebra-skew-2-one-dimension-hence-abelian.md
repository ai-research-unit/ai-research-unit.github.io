# __The Lie Algebra $\operatorname{Skew}_2$: One Dimension, Hence Abelian__

## Introduction

**The antisymmetric matrices of order two form a one-dimensional Lie algebra, so the bracket vanishes identically, the Killing form is zero, and the trace form is the single number $-2$.**

The article proves the identification $\Lambda^{2}\mathbb{R}^{2}=\mathbb{R}J$ with $J^{2}=-I$, proves that the bracket is identically zero, computes the Killing form and the trace form, identifies the universal enveloping algebra with the complex numbers, computes the centraliser of $J$ as the span of $I$ and $J$, shows that the antisymmetric line is not a Lie ideal of $\mathfrak{gl}_2$, and reads the bracket of two symmetric matrices as a scalar with the value $-2$ on an orthonormal pair. It assumes *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$*, *The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$ at $n=2$* and *The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_2(\mathbb{C})$*.

It defers the exponential of the line to *The Exponential of $\operatorname{Skew}_2$: the Single Rotation Plane*, the absence of a second angle to *Simple Rotations at $n=2$: Why There Is Only One Angle*, and the antisymmetric direction of the triangular algebra to *The Antisymmetric Part inside $UT_2$: the Radical as the Commutator*.

## The Space and the Bracket

**Definition.** $\operatorname{Skew}_2(\mathbb{R})=\Lambda^{2}\mathbb{R}^{2}=\{K:K^{\mathsf T}=-K\}=\mathbb{R}J$ with $J=\begin{pmatrix}0&1\\ -1&0\end{pmatrix}$.

**Proposition.** The space is one-dimensional, and the bracket of any two elements vanishes.

**Proof.** An antisymmetric two-by-two matrix has the form $\begin{pmatrix}0&c\\ -c&0\end{pmatrix}=cJ$, so the space is the line spanned by $J$; the bracket of two multiples of $J$ is a multiple of $[J,J]=0$.

**Corollary.** $\operatorname{Skew}_2(\mathbb{R})$ is an abelian Lie algebra of dimension one, and it is the Lie algebra $\mathfrak{so}(2)$ of the rotation group.

**Proof.** Every one-dimensional Lie algebra is abelian, and the antisymmetric matrices are the derivatives at the identity of the orthogonal matrices with determinant one.

**The dimension is degenerate at order two.** At order $n$ the space $\Lambda^{2}\mathbb{R}^{n}$ has dimension $n(n-1)/2$, which is $3$ at $n=3$ and $6$ at $n=4$; at $n=2$ it collapses to a line, so the bracket has no room for structure.

**Proof.** The dimension formula is $n(n-1)/2$, and the value at $n=2$ is $1$.

## The Two Forms

**Proposition.** The Killing form of $\operatorname{Skew}_2(\mathbb{R})$ vanishes.

**Proof.** The adjoint representation of an abelian algebra is zero, so $\operatorname{ad}J=0$ and the trace of any product of adjoint operators is zero.

**Proposition.** The trace form is $\operatorname{tr}(J^{2})=-2$, so it is negative definite on the line.

**Proof.** $J^{2}=-I$ and $\operatorname{tr}I=2$.

**Corollary.** The antisymmetric line is the negative definite direction of the trace form on $M_2(\mathbb{R})$, of signature $(3,1)$.

**Proof.** The form is $-2c^{2}$ at $cJ$, and the symmetric half is positive definite by *The Two Halves as Orthogonal Complements at $n=2$*.

**The two forms say opposite things.** The Killing form cannot see the line because the bracket vanishes there, and the trace form sees it as the unique timelike direction of the algebra.

## The Enveloping Algebra

**Theorem.** The universal enveloping algebra of $\operatorname{Skew}_2(\mathbb{R})$ is $\mathbb{R}[J]/(J^{2}+1)$, which is the field $\mathbb{C}$.

**Proof.** A one-dimensional abelian Lie algebra has the polynomial algebra in one generator as its enveloping algebra, and the relation $J^{2}=-1$ comes from the matrix, so the quotient is the field of complex numbers realised as $\mathbb{R}\oplus\mathbb{R}J$.

**Corollary.** The line acts on the real plane by a complex structure, and the two-dimensional real space becomes a one-dimensional complex space.

**Proof.** Multiplication by $J$ is a real-linear map with square $-1$, which is exactly the datum of a complex structure.

**The complex structure is the one of the plane.** In the standard coordinates $J(x,y)=(-y,x)$, which is the rotation by $\pi/2$; the identification of $\mathbb{R}^{2}$ with $\mathbb{C}$ sends $(x,y)$ to $x+iy$.

**Proof.** The matrix $J$ sends the first basis vector to $-e_{2}$ and the second to $e_{1}$.

## The Centraliser of $J$

**Proposition.** The centraliser of $J$ in $M_2(\mathbb{R})$ is the span of $I$ and $J$, of dimension $2$.

**Proof.** A matrix commuting with $J$ commutes with the complex structure, hence is complex linear as a real map, hence of the form $\begin{pmatrix}a&-b\\ b&a\end{pmatrix}=aI+bJ$; the two parameters are the dimension.

**Corollary.** The centraliser is a copy of $\mathbb{C}$, and it is the largest subalgebra of $M_2(\mathbb{R})$ in which the antisymmetric line is central.

**Proof.** The centraliser is closed under products, contains $J$, and is isomorphic to $\mathbb{C}$ through $aI+bJ\mapsto a+ib$.

**The other centralisers are larger.** The centraliser of the identity is the whole algebra, and the centraliser of a matrix with two distinct eigenvalues is the two-dimensional algebra of the diagonal matrices in its eigenbasis.

**Proof.** A matrix commuting with the identity is arbitrary, and a matrix commuting with a diagonal matrix with distinct entries is diagonal.

## The Line Is Not an Ideal

**Proposition.** The antisymmetric line is not an ideal of $\mathfrak{gl}_2(\mathbb{R})$.

**Proof.** For symmetric $A$ the commutator $[A,J]=AJ-JA$ is symmetric and traceless, hence not a multiple of $J$ unless it vanishes; with $A=\sigma_{3}$ it is $2\sigma_{1}\neq0$.

**Corollary.** The line is a subalgebra and a subspace invariant under no large group, and the derived algebra of $\mathfrak{gl}_2(\mathbb{R})$ is $\mathfrak{sl}_2(\mathbb{R})$.

**Proof.** The derived algebra is spanned by the commutators, which generate the traceless matrices; the line lies inside it but is not stable under it.

**The diagonal algebra does not preserve the line either.** For $D=\operatorname{diag}(a,d)$ one has $[D,J]=(a-d)\sigma_{1}$, which leaves the line as soon as $a\neq d$.

**Proof.** The computation is the same as the previous one with a diagonal $A$.

**Corollary.** The antisymmetric direction is the one that the whole algebra moves, which is why it appears in the off-diagonal corner of the Peirce decomposition and not on the diagonal.

## The Bracket of Two Symmetric Matrices

**Theorem.** For traceless symmetric $u,v$ the bracket is a multiple of $J$, and the scalar is the cross product of the two vectors of coefficients.

**Proof.** The commutator of two symmetric matrices is antisymmetric, hence a multiple of $J$; in the Pauli coordinates $u=\vec a\cdot\vec\sigma$ and $v=\vec b\cdot\vec\sigma$, and $[\sigma_{i},\sigma_{j}]=2i\epsilon_{ijk}\sigma_{k}$ gives the cross product.

**Corollary.** The bracket on the traceless plane is a skew form $\Lambda^{2}V\to\mathbb{R}$, hence a multiple of the area form, and the algebra $\operatorname{Skew}_2(\mathbb{R})$ is the one-dimensional target of that form.

**Proof.** A skew bilinear form on a two-dimensional space is a multiple of the determinant, and the target is one-dimensional.

**The scale on the orthonormal pair.** With $u=\sigma_{3}/\sqrt2$ and $v=\sigma_{1}/\sqrt2$ the bracket is $J$, so the pairing $\langle[u,v],J\rangle=\operatorname{tr}(J^{2})=-2$; the constant $-2$ is the normalisation of the identification of the line with the reals.

**Proof.** $[\sigma_{3},\sigma_{1}]=2J$ gives $[u,v]=J$ after the division by $2$, and the trace form at $J$ is $-2$.

**Corollary.** The bracket of the symmetric half into the antisymmetric line is onto, so the two halves generate the traceless algebra.

**Proof.** The bracket of the two traceless basis elements is $2J\neq0$, and $J$ together with the traceless symmetric elements spans $\mathfrak{sl}_2(\mathbb{R})$.

## Summary

$\operatorname{Skew}_2(\mathbb{R})$ is the line $\mathbb{R}J$ with $J^{2}=-I$, an abelian Lie algebra of dimension one, which is $\mathfrak{so}(2)$. Its Killing form vanishes because the bracket does, and its trace form is the single negative number $-2$, which makes it the timelike direction of the trace form of signature $(3,1)$.

The universal enveloping algebra is $\mathbb{R}[J]/(J^{2}+1)=\mathbb{C}$, the centraliser of $J$ is the copy of $\mathbb{C}$ spanned by $I$ and $J$, and the line is not an ideal of $\mathfrak{gl}_2$ since $[\sigma_{3},J]=2\sigma_{1}$ is symmetric. The bracket of two traceless symmetric matrices is a multiple of $J$ given by a cross product, with the value $J$ on the orthonormal Pauli pair and the trace pairing $-2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J$ | $\begin{pmatrix}0&1\\ -1&0\end{pmatrix}$, the antisymmetric unit |
| $\mathfrak{so}(2)$ | the line $\mathbb{R}J$, the Lie algebra of the rotations |
| $\operatorname{tr}(J^{2})$ | $-2$, the trace form on the line |
| $\operatorname{ad}J$ | the zero operator, since the bracket vanishes |
| $U(\operatorname{Skew}_2)$ | $\mathbb{R}[J]/(J^{2}+1)\cong\mathbb{C}$ |
| $C(J)$ | the centraliser, $\mathbb{R}I\oplus\mathbb{R}J$ |

## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for abelian Lie algebras, their Killing forms and their enveloping algebras.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for $\mathfrak{so}(2)$ and the rotation group.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-2.html), for the two halves and their dimensions.
- [The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$ at $n=2$](the-four-multiplication-tables-ss-sk-ks-kk-at-n-2.html), for the products involving $J$.
- [The Two Halves as Orthogonal Complements at $n=2$](the-two-halves-as-orthogonal-complements-at-n-2.html), for the trace form and its signature.
