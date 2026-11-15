# __$UT_2$ as a Linear Model of $\operatorname{Sym}_2$: Same Space, Wrong Product__

## Introduction

**The map $U\mapsto\tfrac12(U+U^{\mathsf T})$ is a linear isomorphism from the upper triangular matrices onto the symmetric matrices, both of dimension $3$, and it carries neither the product, nor the norm, nor the nilpotents, nor the trace form.**

The article proves the linear isomorphism, exhibits two matrices for which the transported product fails, locates the diagonal algebra as the place where the two products agree, contrasts the nilpotent lines, the trace forms, the idempotents and the automorphism groups of the two models, and identifies what does transport. It assumes *The Antisymmetric Part inside $UT_2$: the Radical as the Commutator*, *The Jordan Algebra $\operatorname{Sym}_2$* and *The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_2(\mathbb{C})$*.

It defers the geometric reading of the two halves to *The Geometry of the Two Halves at $n=2$, and the Return of the Two-Sided Operators* and the analysis of the smooth structures to *The Two Halves and the Analysis: Smooth Structures at $n=2$*.

## The Linear Isomorphism

**Theorem.** The map $\sigma(U)=\tfrac12(U+U^{\mathsf T})$ is a linear isomorphism from $UT_2$ onto $\operatorname{Sym}_2(\mathbb{R})$, with inverse $S\mapsto S$ the inclusion.

**Proof.** The map is linear and its values are symmetric. Its kernel is $UT_2\cap\Lambda^{2}=0$, since an antisymmetric matrix has a nonzero lower left entry unless it vanishes. Both spaces have dimension $3$, so the map is an isomorphism. The symmetric matrices are fixed, so the inclusion is an inverse.

**Corollary.** Every symmetric matrix is the symmetric part of exactly one upper triangular matrix, and conversely.

**Proof.** The two maps are inverse to each other on the two spaces.

**The isomorphism is the projection along the antisymmetric line.** The kernel of the projection onto $UT_2$ is the line, and the composition of the projection with $\sigma$ is the identity on the symmetric half.

**Proof.** For $X\in M_2(\mathbb{R})$ the upper projection is $p_+(X)$, and $\sigma(p_+(X))$ keeps the diagonal entries and half the two off-diagonal entries, which is the symmetric part of $X$ read along the diagonal.

## The Product Does Not Transport

**Theorem.** There are upper triangular $P,Q$ with $\sigma(PQ)\neq\sigma(P)\circ\sigma(Q)$.

**Proof.** Take $P=\begin{pmatrix}1&1\\ 0&0\end{pmatrix}$ and $Q=\begin{pmatrix}0&1\\ 0&0\end{pmatrix}$. Then $PQ=\begin{pmatrix}0&1\\ 0&0\end{pmatrix}$ and $\sigma(PQ)=\begin{pmatrix}0&\tfrac12\\ \tfrac12&0\end{pmatrix}$, while $\sigma(P)=\begin{pmatrix}1&\tfrac12\\ \tfrac12&0\end{pmatrix}$ and $\sigma(Q)=\begin{pmatrix}0&\tfrac12\\ \tfrac12&0\end{pmatrix}$ give $\sigma(P)\circ\sigma(Q)=\begin{pmatrix}\tfrac14&\tfrac14\\ \tfrac14&\tfrac14\end{pmatrix}$.

**Corollary.** The linear isomorphism is not an isomorphism of algebras, and $UT_2$ with the plain product and $\operatorname{Sym}_2$ with the Jordan product are different structures on the same three-dimensional space.

**Proof.** An isomorphism of algebras would carry products to products, and the two displays differ.

**Corollary.** The plain product on the symmetric half is not the Jordan product, because it is not even defined there; only the symmetrised product closes the half.

**Proof.** The product of two symmetric matrices need not be symmetric, as the entry $\sigma_{3}\sigma_{1}=J$ shows.

## The Defect and the Diagonal Algebra

**Proposition.** On the diagonal algebra the two products agree: for $D=\operatorname{diag}(a,d)$ and $D'=\operatorname{diag}(a',d')$ one has $\sigma(DD')=\sigma(D)\circ\sigma(D')$.

**Proof.** Diagonal matrices are symmetric, so $\sigma$ is the identity on them and both products are the plain product.

**Corollary.** The defect vanishes when one of the two factors is a scalar matrix, and it can be nonzero as soon as the two diagonal entries differ.

**Proof.** For a scalar $aI$ one has $\sigma(aIX)=a\sigma(X)$ and $\sigma(aI)\circ\sigma(X)=a\sigma(X)$. For $D=\operatorname{diag}(2,5)$ and $P=\begin{pmatrix}3&5\\ 0&7\end{pmatrix}$ the transported product has off-diagonal entry $5$, while the Jordan product of the images has $\tfrac{35}{4}$.

**The defect sits on the off-diagonal entries when the two sides share their diagonal.** The two sides are bilinear, they agree on the diagonal algebra, and the failure comes from the product of the off-diagonal entry with the difference of the diagonal entries of the other factor.

**Proof.** Expand $\sigma(DP)$ and $\sigma(D)\circ\sigma(P)$ for $D=\operatorname{diag}(a,d)$: both have diagonal entries $ap$ and $dr$, while the off-diagonal entries are $\tfrac{aq}{2}$ and $\tfrac{(a+d)q}{4}$.
## Nilpotents: One Line against None

**Proposition.** The nilpotent elements of $UT_2$ are exactly the multiples of $E_{12}$, while $\operatorname{Sym}_2(\mathbb{R})$ has no nonzero nilpotent element.

**Proof.** An upper triangular matrix has the eigenvalues $a$ and $d$ on the diagonal, so it is nilpotent only if $a=d=0$, which leaves $bE_{12}$; in the symmetric half a nilpotent is positive semidefinite with zero square, hence zero.

**Corollary.** The isomorphism $\sigma$ carries the nilpotent line of $UT_2$ to the line of matrices $\tfrac b2\begin{pmatrix}0&1\\ 1&0\end{pmatrix}$, all of which have square $\tfrac{b^{2}}{4}I\neq0$ unless $b=0$.

**Proof.** $\sigma(bE_{12})=\tfrac b2\sigma_{1}$ and $\sigma_{1}^{2}=I$.

**Corollary.** No linear isomorphism can repair the difference, because the two models differ in a property that is defined by the product alone.

**Proof.** Having a nonzero element with vanishing square is a property of the multiplicative structure, and the two models differ on it.

## The Trace Form

**Proposition.** The trace form pulled back along $\sigma$ differs from the trace form of the symmetric half: on $UT_2$ it has Gram matrix $\operatorname{diag}(1,0,1)$, and on $\operatorname{Sym}_2(\mathbb{R})$ its eigenvalues are $1,1,2$.

**Proof.** The two computations are those of *The Antisymmetric Part inside $UT_2$: the Radical as the Commutator* and *The Two Halves as Orthogonal Complements at $n=2$*.

**Corollary.** The trace itself does transport, since $\operatorname{tr}(\sigma(U))=\operatorname{tr}(U)$, but the positive definite form does not.

**Proof.** The symmetric part keeps the diagonal, so the trace is unchanged; the form is $\operatorname{tr}(XY)$ and not $\operatorname{tr}(\sigma(X)\sigma(Y))$, and the two differ at the off-diagonal entry.

**The form is only semidefinite on the triangular model.** A sum of squares in $UT_2$ can vanish without every term vanishing, since $E_{12}$ is orthogonal to the whole algebra; in the symmetric half that cannot happen.

**Proof.** The radical is the line $n_+$, and a nonzero element of the radical has zero square in the form.

## The Idempotents of Both Models

**Proposition.** The idempotents of $UT_2$ are $0$, $I$, and the two affine lines $\begin{pmatrix}1&b\\ 0&0\end{pmatrix}$ and $\begin{pmatrix}0&b\\ 0&1\end{pmatrix}$ with $b$ arbitrary.

**Proof.** From $\begin{pmatrix}a&b\\ 0&d\end{pmatrix}^{2}=\begin{pmatrix}a^{2}&b(a+d)\\ 0&d^{2}\end{pmatrix}$ one needs $a^{2}=a$ and $d^{2}=d$ and $b(a+d)=b$; the last condition is automatic exactly when $a+d=1$.

**Corollary.** Both models have infinitely many idempotents, but the model of the triangle has two affine lines of them and the symmetric model has a circle, so the two sets are not homeomorphic.

**Proof.** The set of idempotents of $UT_2$ is degenerate at the two extreme idempotents and opens into lines, while the rank-one idempotents of the symmetric half form the circle.

**Corollary.** $E_{11}$ is a primitive idempotent in both models, and its complement is $E_{22}$ in both, since $E_{11}+E_{22}=I$.

**Proof.** The rank of $E_{11}$ is one and its complement is the projection onto the other axis, which is the same matrix $E_{22}$ in both models.

## The Two Jordan Algebras behind the Symmetrised Products

**Proposition.** The symmetrised product of $UT_2$ makes it a Jordan algebra, and that algebra is not isomorphic to $\operatorname{Sym}_2(\mathbb{R})$.

**Proof.** The symmetrised product of any associative algebra is a Jordan algebra. In $UT_2$ the element $E_{12}$ satisfies $E_{12}\circ E_{12}=E_{12}^{2}=0$, while the symmetric half has no nonzero element of square zero, so the two Jordan algebras are not isomorphic.

**Corollary.** The symmetrisation repairs the closure but not the structure: the two Jordan algebras have the same dimension and different nilpotent cones.

**Proof.** The nilpotent cone of the Jordan algebra of $UT_2$ contains the line $\mathbb{R}E_{12}$, and the cone of the symmetric half is a point.

**The symmetric model is formally real.** The model of the symmetric half is the only one of the two in which a sum of squares can vanish only trivially, which is the property that makes the Peirce decomposition of the algebra meaningful.

**Proof.** Formal reality was proved for the symmetric half and fails at $E_{12}$ for the triangular model.

## The Automorphism Groups

**Proposition.** $\operatorname{Aut}(\operatorname{Sym}_2)\cong\mathrm{O}(2)$ has dimension $1$, while the inner automorphisms of $UT_2$ form a group of dimension $2$.

**Proof.** The automorphisms of the symmetric half are $X\mapsto gXg^{\mathsf T}$ with $g$ orthogonal, and $\pm g$ give the same map. The inner automorphisms of $UT_2$ are $U\mapsto T^{-1}UT$ with $T$ upper triangular and invertible, which depend on the ratio of the diagonal entries and on the off-diagonal entry.

**Corollary.** The two models are distinguished by the size of their symmetry groups, and the triangular model has the larger one.

**Proof.** The dimensions $1$ and $2$ differ.

**Corollary.** The conjugation by an upper triangular matrix fixes the diagonal and rescales the off-diagonal entry by the ratio of the diagonal entries.

**Proof.** For $T=\begin{pmatrix}p&q\\ 0&s\end{pmatrix}$ one computes $T^{-1}E_{12}T=\tfrac{p}{s}E_{12}$ and $T^{-1}E_{11}T=E_{11}+\tfrac{q}{p}E_{12}$.

## What Does Transport

**Proposition.** The dimension, the unit, the trace and the diagonal subalgebra transport along $\sigma$, and the product, the determinant, the trace form, the nilpotent cone and the automorphism group do not.

**Proof.** The first three are linear or diagonal data, and $\sigma$ keeps the diagonal. The determinant of $\sigma(U)$ is $ad-\tfrac{b^{2}}{4}$, which depends on $b$, while the determinant of $U$ is $ad$; and the failing items are the ones computed above.

**Corollary.** The linear model is a model of the space and not of the algebra, and it is useful exactly for the questions that see only the space.

**Proof.** The transports listed first are all linear invariants, and the ones listed second are all invariants of the product or of the form.

## Summary

The map $\sigma(U)=\tfrac12(U+U^{\mathsf T})$ is a linear isomorphism from $UT_2$ onto $\operatorname{Sym}_2(\mathbb{R})$, both of dimension $3$, and it does not carry the product: for $P=\begin{pmatrix}1&1\\ 0&0\end{pmatrix}$ and $Q=E_{12}$ the two sides differ.

The two models agree on the diagonal algebra and differ on the off-diagonal entry: $UT_2$ has a nilpotent line where the symmetric half has none, its trace form is semidefinite with radical $n_+$ where the symmetric form is definite, its idempotents form two affine lines rather than a circle, its symmetrised product gives a Jordan algebra with a nonzero nilpotent cone, and its inner automorphism group has dimension $2$ against the dimension $1$ of $\mathrm{O}(2)$. The dimension, the unit, the trace and the diagonal subalgebra do transport, so the model is faithful exactly for the questions that see only the space.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$ | the linear isomorphism $U\mapsto\tfrac12(U+U^{\mathsf T})$ |
| $UT_2$ | the upper triangular matrices |
| $\operatorname{Sym}_2(\mathbb{R})$ | the symmetric matrices, a Jordan algebra |
| $n_+$ | the nilpotent line $\mathbb{R}E_{12}$ |
| $\circ$ | the symmetrised product |
| $E_{12}$ | the nilpotent matrix unit |

## Further Reading

- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for special Jordan algebras and the symmetrised product of an associative algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for automorphisms and derivations of triangular algebras.
- [The Jordan Algebra $\operatorname{Sym}_2$](the-jordan-algebra-sym-2.html), for the algebra whose structure the model fails to carry.
- [The Antisymmetric Part inside $UT_2$: the Radical as the Commutator](the-antisymmetric-part-inside-ut2-the-radical-as-the-commutator.html), for the triangular model and its radical.
- [The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_2(\mathbb{C})$](the-triangular-decomposition-h-n-plus-n-minus-of-m2c.html), for the three subspaces involved.
