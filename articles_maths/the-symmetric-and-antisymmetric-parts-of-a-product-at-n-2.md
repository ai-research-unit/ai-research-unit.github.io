# __The Symmetric and Antisymmetric Parts of a Product at $n=2$__

## Introduction

**Every product of two matrices splits into a symmetric and an antisymmetric part, the two parts have dimensions $3$ and $1$, and the product of a symmetric with an antisymmetric matrix exchanges the roles of the anticommutator and the commutator.**

The article proves the split $XY=\operatorname{sym}(XY)+\operatorname{skew}(XY)$, shows that the trace reads only the symmetric part, treats the three kinds of product by the halves of the two factors, proves that $\operatorname{sym}(SK)=\tfrac12[S,K]$ and $\operatorname{skew}(SK)=\tfrac12\{S,K\}$, and records the Clifford identity $\{u,v\}=2\operatorname{tr}(uv)I$ for traceless symmetric matrices. It assumes *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$* and *The Two Halves as Orthogonal Complements at $n=2$*.

It defers the collection of the four tables to *The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$ at $n=2$*, the algebra axioms of the symmetric half to *The Jordan Algebra $\operatorname{Sym}_2$*, and the bracket of the antisymmetric half to *The Lie Algebra $\operatorname{Skew}_2$: One Dimension, Hence Abelian*.

## The Two Parts of a Product

**Definition.** For a square matrix $P$ the **symmetric part** is $\operatorname{sym}P=\tfrac12(P+P^{\mathsf T})$ and the **antisymmetric part** is $\operatorname{skew}P=\tfrac12(P-P^{\mathsf T})$.

**Theorem.** Every matrix splits in one way as a symmetric plus an antisymmetric matrix, so every product splits too:

$$
XY=\operatorname{sym}(XY)+\operatorname{skew}(XY),\qquad
\operatorname{sym}(XY)=\tfrac12\bigl(XY+(XY)^{\mathsf T}\bigr),\qquad
\operatorname{skew}(XY)=\tfrac12\bigl(XY-(XY)^{\mathsf T}\bigr).
$$

**Proof.** $P=\tfrac12(P+P^{\mathsf T})+\tfrac12(P-P^{\mathsf T})$ and the two terms are symmetric and antisymmetric. The sum is direct because a matrix that is both symmetric and antisymmetric satisfies $P=-P$.

**Corollary.** The product $XY$ is symmetric exactly when $XY=Y^{\mathsf T}X^{\mathsf T}$, and antisymmetric exactly when $XY=-Y^{\mathsf T}X^{\mathsf T}$.

**Proof.** The condition $P=P^{\mathsf T}$ reads $XY=Y^{\mathsf T}X^{\mathsf T}$ after applying the transpose to each factor.

**The transpose of a product turns the order around.** $(XY)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}$, so the two parts of a product are written with the transposes of the factors and not with the factors themselves.

## The Trace Reads Only the Symmetric Part

**Proposition.** $\operatorname{tr}(P)=\operatorname{tr}(\operatorname{sym}P)$ and $\operatorname{tr}(\operatorname{skew}P)=0$.

**Proof.** The trace of a matrix equals the trace of its transpose, so $\operatorname{tr}(P^{\mathsf T})=\operatorname{tr}(P)$ and the antisymmetric part has trace $\tfrac12(\operatorname{tr}P-\operatorname{tr}P)=0$.

**Corollary.** $\operatorname{tr}(XY)=\tfrac12\operatorname{tr}\bigl(XY+Y^{\mathsf T}X^{\mathsf T}\bigr)$, and $\operatorname{tr}([X,Y])=0$ while $\operatorname{tr}(\{X,Y\})=2\operatorname{tr}(XY)$.

**Proof.** The first identity is the proposition applied to $XY$; the second follows from the cyclicity of the trace, $\operatorname{tr}(YX)=\operatorname{tr}(XY)$.

**The determinant is not blind to the antisymmetric part.** For $X=I$ and $Y=J$ the sum $I+J$ has determinant $2$ and the symmetric part alone has determinant $1$, so the antisymmetric part does change the determinant.

**Proof.** $\det(I+J)=\det\begin{pmatrix}1&1\\ -1&1\end{pmatrix}=2$, and $\operatorname{sym}(I+J)=I$.

## Products of Two Symmetric Matrices

**Theorem.** For symmetric $S,T$,

$$
\operatorname{sym}(ST)=\tfrac12\{S,T\},\qquad \operatorname{skew}(ST)=\tfrac12[S,T].
$$

**Proof.** $(ST)^{\mathsf T}=T^{\mathsf T}S^{\mathsf T}=TS$, so $\operatorname{sym}(ST)=\tfrac12(ST+TS)$ and $\operatorname{skew}(ST)=\tfrac12(ST-TS)$.

**Corollary.** The symmetric part of a product of two symmetric matrices is symmetric and the antisymmetric part is antisymmetric, and both are nonzero in general.

**Proof.** The two formulas express the parts by the anticommutator and the commutator, which are symmetric and antisymmetric respectively.

**Example.** With $S=\sigma_{3}$ and $T=\sigma_{1}$ one has $\{S,T\}=0$ and $[S,T]=2J$, so the product $\sigma_{3}\sigma_{1}=J$ is purely antisymmetric.

**Proof.** $\sigma_{3}\sigma_{1}=J$ and $\sigma_{1}\sigma_{3}=-J$, so the sum vanishes and the difference is $2J$.

**The product is symmetric exactly when the two matrices commute.** For symmetric $S,T$ the product $ST$ is symmetric iff $[S,T]=0$.

**Proof.** $ST$ is symmetric iff $ST=TS$, which is the vanishing of the commutator.

## Products of a Symmetric and an Antisymmetric Matrix

**Theorem.** For symmetric $S$ and antisymmetric $K$,

$$
\operatorname{sym}(SK)=\tfrac12(SK-KS)=\tfrac12[S,K],\qquad
\operatorname{skew}(SK)=\tfrac12(SK+KS)=\tfrac12\{S,K\}.
$$

**Proof.** $(SK)^{\mathsf T}=K^{\mathsf T}S^{\mathsf T}=(-K)S=-KS$, so the symmetric part is $\tfrac12(SK-KS)$ and the antisymmetric part is $\tfrac12(SK+KS)$.

**Corollary (the roles are exchanged).** For a mixed product the symmetric part is the commutator term and the antisymmetric part is the anticommutator term, which is the reverse of the rule for two symmetric factors.

**Proof.** Compare the two theorems: for $S,T$ symmetric the symmetric part carries the anticommutator, and for the mixed product it carries the commutator.

**Example.** With $S=\sigma_{3}$ and $K=J$ one has $SK=\sigma_{1}$ and $KS=-\sigma_{1}$, so the product is symmetric, the commutator term is $\sigma_{1}$ and the anticommutator term vanishes.

**Proof.** $\sigma_{3}J=\sigma_{1}$ and $J\sigma_{3}=-\sigma_{1}$, hence $SK-KS=2\sigma_{1}$ and $SK+KS=0$.

**Corollary.** A product $SK$ with $S$ symmetric and $K$ antisymmetric is symmetric iff the two matrices anticommute.

**Proof.** By the theorem, the antisymmetric part vanishes exactly when $\{S,K\}=0$.

**The reversed product.** For $KS$ the same computation gives $\operatorname{sym}(KS)=-\tfrac12[S,K]$ and $\operatorname{skew}(KS)=\tfrac12\{S,K\}$, so the two mixed products have opposite symmetric parts and equal antisymmetric parts.

**Proof.** Apply the transpose to the theorem, or recompute with $(KS)^{\mathsf T}=S(-K)=-SK$.

## Products of Two Antisymmetric Matrices

**Proposition.** The antisymmetric matrices of order two form the line $\mathbb{R}J$ with $J^{2}=-I$, so every product of two of them is a scalar multiple of the identity.

**Proof.** The antisymmetric matrices are the multiples of $J$ and $J^{2}=-I$.

**Corollary.** Every product $KK'$ of two antisymmetric matrices is symmetric, and its antisymmetric part vanishes.

**Proof.** $KK'=cc'J^{2}=-cc'I$, which is symmetric, and a scalar matrix has zero antisymmetric part.

**The trace of the product is negative.** For $K=cJ$ and $K'=c'J$ one has $\operatorname{tr}(KK')=-2cc'$, so the trace form is negative definite on the antisymmetric line.

**Proof.** $\operatorname{tr}(J^{2})=\operatorname{tr}(-I)=-2$.

**The mixed and the pure cases are the whole list.** Every product of two matrices falls in one of the three cases according to the halves of its factors, since every factor is symmetric or antisymmetric.

## The Traceless Symmetric Matrices

**Theorem.** For traceless symmetric $u,v$ of order two,

$$
\{u,v\}=2\operatorname{tr}(uv)\,I .
$$

**Proof.** In the Pauli basis $u=\vec a\cdot\vec\sigma$ and $v=\vec b\cdot\vec\sigma$ with real vectors $\vec a,\vec b$, the anticommutator of two Pauli matrices is $\{\sigma_{i},\sigma_{j}\}=2\delta_{ij}I$, hence $\{u,v\}=2(\vec a\cdot\vec b)I$ and $\vec a\cdot\vec b=\tfrac12\operatorname{tr}(uv)$.

**Corollary.** The anticommutator of two traceless symmetric matrices is a scalar, and its determinant vanishes unless the scalar is zero.

**Proof.** The result is a multiple of the identity, whose determinant is the square of the scalar.

**Corollary.** The commutator $[u,v]$ is antisymmetric and its size is governed by the cross product: $[u,v]=2i\,(\vec a\times\vec b)\cdot\vec\sigma$, a multiple of the antisymmetric unit, since a commutator of two symmetric matrices is antisymmetric and the line is one-dimensional.

**Proof.** $[\sigma_{i},\sigma_{j}]=2i\epsilon_{ijk}\sigma_{k}$, so the commutator is $2i$ times the Pauli combination of the cross product.

**The traceless part is closed under the anticommutator up to the scalar term.** The product $\{u,v\}$ leaves the traceless space and lands in the scalars, which is why the symmetric half with its trace is the right object and not the traceless part alone.

## Summary

Every product splits into a symmetric and an antisymmetric part, of dimensions $3$ and $1$, and the trace reads only the symmetric part, so commutators are traceless and $\operatorname{tr}\{X,Y\}=2\operatorname{tr}(XY)$.

For two symmetric factors the symmetric part of the product is the anticommutator and the antisymmetric part is the commutator; for a mixed product the roles are exchanged, with $\operatorname{sym}(SK)=\tfrac12[S,K]$ and $\operatorname{skew}(SK)=\tfrac12\{S,K\}$; for two antisymmetric factors the product is a scalar matrix because $J^{2}=-I$. For traceless symmetric matrices the anticommutator is the scalar $2\operatorname{tr}(uv)I$, and the commutator is a cross product in the antisymmetric direction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{sym}P$ | $\tfrac12(P+P^{\mathsf T})$ |
| $\operatorname{skew}P$ | $\tfrac12(P-P^{\mathsf T})$ |
| $\{X,Y\}$ | the anticommutator $XY+YX$ |
| $[X,Y]$ | the commutator $XY-YX$ |
| $\sigma_{1},\sigma_{3}$ | the two real Pauli matrices, symmetric |
| $J$ | $i\sigma_{2}$, the antisymmetric unit |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the symmetric and antisymmetric parts of a matrix and their traces.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the anticommutator identities of the Pauli matrices.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-2.html), for the two halves and their bracket.
- [The Two Halves as Orthogonal Complements at $n=2$](the-two-halves-as-orthogonal-complements-at-n-2.html), for the trace form that separates the two parts.
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the same product splitting in the biquaternion language.
