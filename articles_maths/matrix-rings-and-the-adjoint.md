
# __Matrix Rings and the Adjoint__

## Introduction

When the endomorphism ring of *Involutions of the Endomorphism Ring* is a matrix ring, the adjoint becomes a concrete formula: with respect to a sesquilinear form with Gram matrix $\Phi$ and coefficient involution $\sigma$, the adjoint of a matrix $X$ is $\Phi^{-1}\sigma(X)^{\mathrm t}\Phi$, and with respect to the $\sigma$-twisted trace pairing of the category it is read off from the left and the right multiplications. Three objects come together in the matrix case and are easy to confuse: the **adjoint involution** $X \mapsto \Phi^{-1}\sigma(X)^{\mathrm t}\Phi$ defined by a form, the **self-adjoint** and **skew-adjoint** matrices it picks out, and the **unitary group** of the matrices with $X^{*}X = XX^{*} = I$, which are exactly the matrices preserving the form. This article computes the adjoint in the matrix ring, identifies the self-adjoint matrices and the unitary group, and relates them to the trace pairing of the ring.

It assumes *Matrix Rings with an Involution*, *Involutions of the Endomorphism Ring* for the adjoint, and *The Transpose as an Adjoint* for the trace duality; the sesquilinear forms themselves and their classification are Part II, and the Gram matrix is used only as a matrix. Throughout, $R$ is a commutative ring with $1 \neq 0$ and an involution $\sigma$, $\Phi \in M_n(R)$ is a matrix with $\Phi$ invertible when it is used as a Gram matrix, $\tau$ is the matrix trace, and $X^{*} = \Phi^{-1}\sigma(X)^{\mathrm t}\Phi$.

## The Adjoint Defined by a Form

**Theorem.** Let $\Phi$ be invertible and let the sesquilinear form be $\langle x,y\rangle = \sigma(x)^{\mathrm t}\Phi y$ on $R^n$. Then

$$
\langle Xx,y\rangle = \langle x, X^{*}y\rangle , \qquad X^{*} = \Phi^{-1}\sigma(X)^{\mathrm t}\Phi ,
$$

so $X\mapsto X^{*}$ is the adjoint involution of $M_n(R)$ determined by $\Phi$ and $\sigma$; for $\Phi = I$ it is $X\mapsto \sigma(X)^{\mathrm t}$, and for $\sigma = \mathrm{id}$ and $\Phi = I$ it is the transpose.

**Proof.** $\langle Xx,y\rangle = \sigma(Xx)^{\mathrm t}\Phi y = \sigma(x)^{\mathrm t}\sigma(X)^{\mathrm t}\Phi y = \sigma(x)^{\mathrm t}\Phi(\Phi^{-1}\sigma(X)^{\mathrm t}\Phi)y = \langle x, X^{*}y\rangle$. The four laws are those of *Involutions of the Endomorphism Ring*.

**Example (degree two).** For $n = 2$, $\sigma$ the complex conjugation and $\Phi = \operatorname{diag}(1,-1)$, the adjoint of

$$
X=\begin{pmatrix}i&1\\0&2\end{pmatrix}
$$

is

$$
X^{*}=\Phi^{-1}\sigma(X)^{\mathrm t}\Phi
=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}-i&0\\1&2\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}
=\begin{pmatrix}-i&0\\-1&2\end{pmatrix},
$$

the middle factor being $\sigma(X)^{\mathrm t}$; and with $\Phi = I$ the same involution is the conjugate transpose, $X^{*} = \begin{pmatrix}-i&0\\1&2\end{pmatrix}$.

**Proposition (self-adjoint and skew-adjoint).** The **self-adjoint** matrices are those with $\sigma(X)^{\mathrm t}\Phi = \Phi X$, equivalently $X^{*} = X$; the **skew-adjoint** ones are those with $X^{*} = -X$. For $\Phi = \operatorname{diag}(1,-1)$ the self-adjoint matrices are $\begin{pmatrix}a&b\\-\bar b&d\end{pmatrix}$ with $a,d$ real, the matrix $\Phi$ itself among them. With $2$ invertible the ring is the sum of the two, and for $\Phi = I$ they are the matrices with $\sigma(X)^{\mathrm t} = \pm X$, the Hermitian and skew-Hermitian matrices of the coefficient involution.

**Proof.** $X^{*} = X$ is $\Phi^{-1}\sigma(X)^{\mathrm t}\Phi = X$, i.e. $\sigma(X)^{\mathrm t}\Phi = \Phi X$; the rest is *Involutive Rings* applied to the adjoint involution.

**Proposition (the unitary group).** The matrices with

$$
X^{*}X = XX^{*} = I, \qquad \text{equivalently } \sigma(X)^{\mathrm t}\Phi X = \Phi ,
$$

form a subgroup $U_n(R,\Phi,\sigma)$ of $\mathrm{GL}_n(R)$ and are exactly the matrices preserving the form, $\langle Xx,Xy\rangle = \langle x,y\rangle$ for all $x,y$. For $\sigma = \mathrm{id}$ and $\Phi$ symmetric this is the orthogonal group, for $\Phi^{\mathrm t} = -\Phi$ the symplectic group, and for $R = \mathbb{C}$, $\sigma$ the conjugation and $\Phi = I$ the unitary group.

**Proof.** $\sigma(X)^{\mathrm t}\Phi X = \Phi$ is $X^{*}X = I$; multiplying by $X$ on the left gives $X X^{*} = I$ by the standard group argument, and the preservation is the unitary-element proposition of *Involutions of the Endomorphism Ring*.

## The Trace Pairing

**Proposition.** With the trace pairing $\beta(X,Y) = \tau(XY)$ of the ring, the adjoint of the left multiplication is the right multiplication, $L_X^{*} = R_X$, and the trace of the adjoint is the $\sigma$-image of the trace,

$$
\tau(X^{*}) = \sigma(\tau(X)) .
$$

Hence the trace pairing is $\sigma$-semilinear in the appropriate sense and its restriction to the self-adjoint matrices is a symmetric bilinear form.

**Proof.** $\beta(L_XY,Z) = \tau(XYZ) = \tau(YZX) = \beta(Y,R_XZ)$ is *The Transpose as an Adjoint*; $\tau(X^{*}) = \tau(\Phi^{-1}\sigma(X)^{\mathrm t}\Phi) = \tau(\sigma(X)^{\mathrm t}) = \sigma(\tau(X))$, since the trace is invariant under conjugation by $\Phi$ and additive over the diagonal.

**Corollary (the two involutions).** The adjoint involution $X\mapsto\sigma(X)^{\mathrm t}$ of $\Phi = I$ and the transpose involution $X\mapsto X^{\mathrm t}$ of *Matrix Rings with an Involution* agree exactly when $\sigma = \mathrm{id}$; for a nontrivial $\sigma$ the adjoint involution is of the second kind and its self-adjoint matrices are the Hermitian ones.

**Proof.** Comparison of the two formulas; the kind is read off from the action on the centre $R\cdot I$, where $\sigma(X)^{\mathrm t}$ acts by $\sigma$ on the scalars.

## Examples

**(a) The real orthogonal case.** $R = \mathbb{R}$, $\sigma = \mathrm{id}$, $\Phi = I$: $X^{*} = X^{\mathrm t}$, the self-adjoint matrices are the symmetric ones, $\begin{pmatrix}1&2\\2&3\end{pmatrix}$ among them against the skew-adjoint $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, and $U_n$ is the orthogonal group.

**(b) The complex unitary case.** $R = \mathbb{C}$, $\sigma$ the conjugation, $\Phi = I$: $X^{*} = \overline{X}^{\mathrm t}$, the self-adjoint matrices are the Hermitian ones, and $U_n$ is the unitary group. For $n = 2$ the Pauli matrix

$$
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}
$$

is Hermitian, and $\tfrac{1}{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}$ is unitary. The adjoint involution is of the second kind.

**(c) The symplectic case.** $\Phi = J$ with $J^{\mathrm t} = -J$, $J^2 = -1$, in the degree-two model $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$: $X^{*} = -JX^{\mathrm t}J$, the self-adjoint matrices are the scalar matrices, $-JX^{\mathrm t}J=X$ being equivalent to $X=\lambda I$, so that the matrix $J$ and its multiples are skew-adjoint, and $U_n$ is the symplectic group of *Matrix Rings with an Involution*.

**(d) The indefinite case.** $\Phi = \operatorname{diag}(1,\dots,1,-1,\dots,-1)$, in the degree-two model $\Phi=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$: the self-adjoint matrices are the Hermitian matrices of a signature, and the unitary group is the corresponding indefinite unitary group; the signature is a Part II invariant and is only named here.

## Summary

In the matrix ring with a coefficient involution $\sigma$ and an invertible Gram matrix $\Phi$, the adjoint is $X^{*} = \Phi^{-1}\sigma(X)^{\mathrm t}\Phi$, defined by the sesquilinear form $\langle x,y\rangle = \sigma(x)^{\mathrm t}\Phi y$; for $\Phi = I$ it is $\sigma(X)^{\mathrm t}$. The self-adjoint matrices satisfy $\sigma(X)^{\mathrm t}\Phi = \Phi X$, the skew-adjoint ones the same with the opposite sign, and the unitary group $U_n(R,\Phi,\sigma) = \{X : X^{*}X = XX^{*} = I\}$ is the group of matrices preserving the form; the transpose, the orthogonal, the symplectic and the unitary groups are the cases $\Phi = I$ with $\sigma = \mathrm{id}$, a symmetric $\Phi$, an antisymmetric $\Phi$, and $R = \mathbb{C}$ with the conjugation. Under the trace pairing $\beta(X,Y) = \tau(XY)$ the adjoint of the left multiplication is the right multiplication and $\tau(X^{*}) = \sigma(\tau(X))$, so the trace pairing restricts to a symmetric form on the self-adjoint part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$, $\Phi$ | Coefficient involution and invertible Gram matrix |
| $\langle x,y\rangle = \sigma(x)^{\mathrm t}\Phi y$ | Sesquilinear form |
| $X^{*} = \Phi^{-1}\sigma(X)^{\mathrm t}\Phi$ | Adjoint of $X$ |
| $\sigma(X)^{\mathrm t}\Phi = \Phi X$ | Self-adjoint matrices |
| $X^{*}X = XX^{*} = I$ | Unitary group $U_n(R,\Phi,\sigma)$ |
| $\sigma(X)^{\mathrm t}\Phi X = \Phi$ | Preservation of the form |
| $\beta(X,Y) = \tau(XY)$ | Trace pairing; $L_X^{*} = R_X$ |
| $\tau(X^{*}) = \sigma(\tau(X))$ | Trace of the adjoint |
| $\Phi = I$ / $J$ / indefinite | Orthogonal / symplectic / indefinite unitary cases |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the adjoint involution, the Gram matrix and the classical groups.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the adjoint involution and the unitary elements of a matrix ring.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the Hermitian and skew-Hermitian matrices and the trace.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for sesquilinear forms, their Gram matrices and the groups that preserve them.
