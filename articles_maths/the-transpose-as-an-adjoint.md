
# __The Transpose as an Adjoint__

## Introduction

The transpose of a matrix is the adjoint of the matrix read against the standard pairing of its module, and the identification is the simplest appearance in algebra of the general adjoint of *Involutions of the Endomorphism Ring*. Two pairings are involved and they must not be confused. The **standard pairing** on the free module $R^n$ is $\langle x,y\rangle = \sum_i x_iy_i$; it is symmetric and perfect, and the defining identity of the adjoint, $\langle Xx,y\rangle = \langle x,X^{\mathrm t}y\rangle$, says exactly that the transpose is the adjoint of $X$. The **trace pairing** on the matrix ring, $(X,Y)\mapsto \tau(XY) = \operatorname{tr}(XY)$, is likewise symmetric and perfect, and it realises the matrix ring as its own dual: this is the **trace duality**, and under it the transpose involution is the adjoint involution of the algebra.

This article treats the transpose as the adjoint with respect to the standard pairing, the identification of the dual map with the transpose, and the trace duality that identifies the matrix ring with its dual. It assumes *Rings*, *Matrix Rings with an Involution* for the transpose, *Involutions of the Endomorphism Ring* for the adjoint and *Modules* only by forward reference. Throughout, $R$ is a commutative ring with $1 \neq 0$, $X, Y$ are $n\times n$ matrices over $R$, $x, y$ are columns, $X^{\mathrm t}$ is the transpose, and $\tau$ is the matrix trace.

## The Transpose as the Adjoint of the Standard Pairing

**Definition.** The **standard pairing** of $R^n$ is

$$
\langle x,y\rangle = \sum_i x_i y_i = x^{\mathrm t}y .
$$

It is biadditive, symmetric, and perfect: the map $x \mapsto \langle x,-\rangle$ is an isomorphism $R^n \to \operatorname{Hom}_R(R^n,R)$.

**Theorem.** For every matrix $X$ and all columns $x, y$,

$$
\langle Xx, y\rangle = \langle x, X^{\mathrm t}y\rangle ,
$$

so $X^{\mathrm t}$ is the adjoint of $X$ with respect to the standard pairing. Consequently $X \mapsto X^{\mathrm t}$ is the adjoint involution of the matrix ring, it is additive, anti-multiplicative and of order two, and the orthogonal matrices, those with $X^{\mathrm t}X = XX^{\mathrm t} = I$, are exactly the matrices preserving the standard pairing.

**Proof.** $\langle Xx,y\rangle = (Xx)^{\mathrm t}y = x^{\mathrm t}X^{\mathrm t}y = \langle x,X^{\mathrm t}y\rangle$; the identification with *Involutions of the Endomorphism Ring* is the definition of the adjoint there, the four laws are those of that article, and the preservation statement is its unitary-element proposition.

**Corollary (the dual map).** Let $X$ correspond to the endomorphism $T$ of $R^n$ by the standard basis. Then $X^{\mathrm t}$ corresponds to the **dual map** $T^{\mathrm t} : \operatorname{Hom}_R(R^n,R) \to \operatorname{Hom}_R(R^n,R)$, $f \mapsto f\circ T$, transported back along the isomorphism $R^n \to \operatorname{Hom}_R(R^n,R)$ given by the pairing; the transpose matrix and the dual map are the same object under this identification.

**Proof.** The dual map is defined on the dual basis by the matrix transpose by *Linear Maps and Matrices*, and the identification with $\operatorname{Hom}_R(R^n,R)$ by the standard pairing converts it into the transpose of the matrix of $T$. The two transposes are one.

## Trace Duality

**Theorem (trace duality).** The **trace pairing** $\beta(X,Y) = \tau(XY)$ on $M_n(R)$ is biadditive, symmetric and perfect; the induced map $M_n(R) \to \operatorname{Hom}_R(M_n(R),R)$, $X\mapsto \beta(X,-)$, is an isomorphism. Under it the matrix ring is identified with its own dual.

**Proof.** Symmetry and biadditivity are immediate; for perfectness, $\beta(X,E_{ij}) = (X E_{ij})$'s trace $= X_{ji}$, so $X\mapsto \beta(X,-)$ has matrix $X^{\mathrm t}$ in the basis $E_{ij}$ of the dual, and the map sending $X$ to $X^{\mathrm t}$ is an isomorphism with inverse the transpose. Hence the trace pairing is perfect.

**Corollary (the adjoint of the left and right multiplications).** With the trace pairing of the ring, the adjoint of the left multiplication $L_X$ is the right multiplication $R_X$, and conversely; the transpose of the matrix appears through the standard pairing above, while the trace pairing realises the switching of the sides of the regular representation. This is the specialisation to the matrix ring of *The Adjoint of the Left Multiplication on a Ring*.

**Proof.** $\beta(L_XY,Z) = \tau(XYZ) = \tau(YZX) = \beta(Y,R_XZ)$, and the same computation with the sides exchanged.

**Remark (the two transposes).** The transpose of the standard pairing and the switching of the sides under the trace pairing are different involutions of the matrix ring, and the article separates them. The first is the orthogonal involution and is the adjoint of the matrix as an endomorphism; the second is the transpose of the trace form of the algebra and is not, by itself, the transpose involution. The two agree as maps $X \mapsto X^{\mathrm t}$ but play different roles, the first in the adjoint of the operators and the second in the duality of the algebra with its own dual.

## Examples

**(a) The identity matrix pairing.** $R = \mathbb{R}$, $n = 3$: $\langle x,y\rangle = x^{\mathrm t}y$ is the dot product, the adjoint is the transpose, and the orthogonal group is the group of matrices with $X^{\mathrm t}X = I$.

**(b) The symplectic pairing.** With the pairing of *Involutions of the Endomorphism Ring*, $B(x,y) = \sum_i(x_iy_{i+n}-x_{i+n}y_i)$, the adjoint of $X$ is the symplectic adjoint $-JX^{\mathrm t}J$; the transpose alone is the adjoint only for the standard pairing.

**(c) The trace duality.** For $R = \mathbb{C}$, the trace pairing $\tau(XY)$ identifies $M_n(\mathbb{C})$ with its dual, and the symmetric matrices $X^{\mathrm t}=X$ pair symmetrically with themselves, $\tau(X^2)\neq 0$ for $X\neq0$ symmetric over $\mathbb{R}$; the pairing is the algebraic ancestor of the trace form of *Hilbert Algebras* in Part II.

**(d) The transpose involution.** As an involution of the matrix ring the transpose is the first-kind orthogonal involution of *Matrix Rings with an Involution*; its self-adjoint elements are the symmetric matrices and its skew elements the antisymmetric ones, and the trace vanishes on the latter, the sign structure of *The Skew Field of a Ring with Involution*.

## Summary

The **standard pairing** $\langle x,y\rangle = x^{\mathrm t}y$ on $R^n$ is symmetric and perfect, and the transpose is the adjoint of a matrix with respect to it, $\langle Xx,y\rangle = \langle x,X^{\mathrm t}y\rangle$; the assignment $X\mapsto X^{\mathrm t}$ is therefore the orthogonal adjoint involution of the matrix ring and its unitary group is the orthogonal group. Under the standard identification of the module with its dual, the transpose matrix is the **dual map** of the endomorphism, so the two transposes coincide. The **trace pairing** $\tau(XY)$ on the matrix ring is likewise symmetric and perfect and identifies the ring with its own dual, the adjoint of the left multiplication being the right multiplication; this is the trace duality, and it is the ring-level form of the general adjoint of *Involutions of the Endomorphism Ring*. The two pairings and the two roles of the transpose are the whole content of the article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $R^n$ | Commutative ring and free module of columns |
| $\langle x,y\rangle = x^{\mathrm t}y$ | Standard pairing; symmetric, perfect |
| $\langle Xx,y\rangle=\langle x,X^{\mathrm t}y\rangle$ | The transpose is the adjoint |
| $X\mapsto X^{\mathrm t}$ | Orthogonal adjoint involution of $M_n(R)$ |
| $X^{\mathrm t}X=XX^{\mathrm t}=I$ | Orthogonal matrices preserving the standard pairing |
| $T^{\mathrm t}$, dual map | $f\mapsto f\circ T$; identified with the transpose matrix |
| $\beta(X,Y)=\tau(XY)$ | Trace pairing; symmetric, perfect |
| $\beta(L_XY,Z)=\beta(Y,R_XZ)$ | Adjoint of left multiplication: $L_X^{*}=R_X$ |
| $\tau$, $E_{ij}$ | Matrix trace and matrix units; duality of the algebra with its dual |

## Further Reading

- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the adjoint involution and the trace duality of a matrix algebra.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for bilinear forms, the dual map and the transposition of a linear map.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the transpose involution, the symmetric and the skew matrices and the trace.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the orthogonal involution, the standard pairing and the trace form.
