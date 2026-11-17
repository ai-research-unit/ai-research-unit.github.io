# __$UT_n$ as the Complement of the Antisymmetric Part__

## Introduction

**The upper triangular matrices have dimension $n(n+1)/2$, the same as the symmetric matrices, and they meet the antisymmetric matrices only at zero, so $M_n(\mathbb{R})=UT_n\oplus\operatorname{Skew}_n$ is a direct sum of the same dimensions as the symmetric split and of a different kind.**

The article proves the dimension count, proves that the intersection is zero, derives the direct sum, and shows that this complement is not the orthogonal complement for the trace form: the trace form is degenerate on $UT_n$, with kernel $n_+$ of dimension $n(n-1)/2$. It identifies the true orthogonal complement of $\operatorname{Skew}_n$, which is $\operatorname{Sym}_n$, computes the projection onto $UT_n$ along $\operatorname{Skew}_n$, shows that this projection is not the symmetrisation, and uses it to model $\operatorname{Sym}_n$ linearly by upper triangular matrices. It assumes *The Two Halves as Orthogonal Complements for the Trace Form* and *The Triangular Decomposition $h\oplus n_+\oplus n_-$*.

## The Two Dimensions

**Definition.** $UT_n=\{A:A_{ij}=0\ \text{for}\ i>j\}$.

**The two spaces have the same dimension.** A symmetric matrix is free on the diagonal and above it, and an upper triangular matrix is free on the diagonal and above it. The two free regions are the same set of entries, so

$$
\dim UT_n=n+\binom{n}{2}=\frac{n(n+1)}{2}=\dim\operatorname{Sym}_n.
$$

Measured as the rank of the basis of upper triangular units, the dimension is $3$ at $n=2$, $6$ at $n=3$ and $10$ at $n=4$.

**The antisymmetric part has the complementary dimension.** $\dim\operatorname{Skew}_n=\binom{n}{2}=n(n-1)/2$, so the two numbers add to $n^{2}$:

$$
\frac{n(n+1)}{2}+\frac{n(n-1)}{2}=n^{2}.
$$

**Equal dimension is not equality.** $UT_n$ contains the whole diagonal and the identity $\mathrm{I}$, and $\mathrm{I}$ is not antisymmetric. The two spaces are different subspaces of the same dimension, and the article compares them as complements rather than as subspaces.

## The Intersection Is Zero

**Proposition.** $UT_n\cap\operatorname{Skew}_n=\{0\}$.

*Proof.* Let $A$ be upper triangular and anti-Hermitian. Antisymmetry forces $A_{ii}=0$ and $A_{ij}=-A_{ji}$. Upper triangularity forces $A_{ij}=0$ for $i>j$. So every entry is zero: the diagonal by antisymmetry, the lower part by triangularity, and the upper part by antisymmetry together with the lower part.

**The measurement confirms the zero intersection.** On the union of the two bases the rank is the sum of the dimensions: $3+1=4$ at $n=2$, $6+3=9$ at $n=3$ and $10+6=16$ at $n=4$. A nonzero intersection would make the rank smaller.

**The intersection is zero for a structural reason.** An antisymmetric matrix with zero lower part is zero, because antisymmetry turns the upper part into the lower part with a sign. An upper triangular matrix has no lower part to supply, so the two conditions cancel each other.

## The Direct Sum

**Theorem.** $M_n(\mathbb{R})=UT_n\oplus\operatorname{Skew}_n$.

*Proof.* The two subspaces span a space whose dimension is the sum of their dimensions, namely $n^{2}$, and $n^{2}$ is the dimension of the algebra. So they span the algebra, and their intersection is zero.

**Every matrix has a unique decomposition.** For $X\in M_n(\mathbb{R})$ there are unique $T\in UT_n$ and $K\in\operatorname{Skew}_n$ with $X=T+K$. The two parts are computed by the formula of a later section.

**The complement carries the same dimension as the symmetric half, and it is not the symmetric half.** This is the contrast of the article: two different complements of the same space $\operatorname{Skew}_n$, one of them orthogonal for the trace form and one of them not.

**The transpose relates the two complements.** $\operatorname{Sym}_n$ is the fixed space of the transpose and $UT_n$ is the stabiliser of the standard flag. Both have dimension $n(n+1)/2$, both meet $\operatorname{Skew}_n$ at zero, and both complete it to the algebra.

## The Trace Form Is Degenerate on $UT_n$

**Proposition.** For $X,Y\in UT_n$,

$$
\operatorname{tr}(XY)=\sum_{i=1}^{n}X_{ii}Y_{ii}.
$$

*Proof.* $\operatorname{tr}(XY)=\sum_{i,j}X_{ij}Y_{ji}$, and the term $(i,j)$ needs $i\le j$ for $X$ and $j\le i$ for $Y$, hence $i=j$.

**So the form is degenerate on $UT_n$, and its rank is $n$.** The Gram matrix in the basis of upper triangular units is diagonal with $n$ entries equal to $1$ and the rest zero. Measured, the rank is $2$ at $n=2$, $3$ at $n=3$ and $4$ at $n=4$, equal to $n$ in each case, while the dimension of $UT_n$ is $3$, $6$ and $10$.

**Definition.** The kernel of the restriction is $\{X\in UT_n:X_{ii}=0\ \text{for all}\ i\}$.

**The kernel is $n_+$, of dimension $n(n-1)/2$.** Measured, the kernel has dimension $1$ at $n=2$, $3$ at $n=3$ and $6$ at $n=4$, which is $\binom{n}{2}$ in each case.

**The direction $E_{11}-E_{22}$ is not in the kernel.** It is diagonal, hence upper triangular, and it pairs with $\operatorname{diag}(1,2)$ to give

$$
\operatorname{tr}\bigl((E_{11}-E_{22})\operatorname{diag}(1,2)\bigr)=1-2=-1.
$$

So the kernel is not the trace-zero diagonal: it is the strictly upper triangular part, and the diagonal of $UT_n$ pairs with itself as the ordinary dot product.

## The Kernel and the Nilpotent Part

**The kernel of the trace form on $UT_n$ is exactly $n_+$.** The strictly upper triangular part is the nilpotent ideal of $UT_n$ described in *The Triangular Decomposition $h\oplus n_+\oplus n_-$*, and it is also the kernel of the trace form restricted to $UT_n$. The two roles are different and the subspace is the same.

**This is why the trace form does not project onto $UT_n$.** A degenerate form defines an orthogonal complement that is too large: the space of matrices orthogonal to $UT_n$ has dimension $n^{2}-n$, while a complement of $UT_n$ inside the algebra has dimension $n(n-1)/2$.

**The orthogonal complement of $UT_n$ is $n_-$.** The condition $\operatorname{tr}(ZT)=0$ for all $T\in UT_n$ reads $Z_{ji}=0$ for $i\le j$, hence $Z$ is strictly lower triangular. Measured, the dimension is $1$ at $n=2$, $3$ at $n=3$ and $6$ at $n=4$, which is $\binom{n}{2}$ and also the codimension of $UT_n$.

## The Orthogonal Complement of the Antisymmetric Part

**The trace-orthogonal complement of $\operatorname{Skew}_n$ is $\operatorname{Sym}_n$, not $UT_n$.**

$$
\operatorname{Skew}_n^{\perp}=\operatorname{Sym}_n,\qquad \operatorname{Sym}_n^{\perp}=\operatorname{Skew}_n.
$$

This is the content of *The Two Halves as Orthogonal Complements for the Trace Form*, and the proof is the identity $\operatorname{tr}(SK)=0$ for symmetric $S$ and antisymmetric $K$, together with the dimension count.

**$UT_n$ is not orthogonal to $\operatorname{Skew}_n$: if it were, it would equal $\operatorname{Sym}_n$.** The orthogonal complement $\operatorname{Skew}_n^{\perp}$ has dimension $n(n+1)/2$, and $UT_n\subseteq\operatorname{Skew}_n^{\perp}$ would force the equality $UT_n=\operatorname{Sym}_n$ because the dimensions agree. But $E_{12}$ is upper triangular and is not symmetric, so the inclusion fails.

**An explicit pair is not orthogonal.** Take $T=E_{12}$ and $K=E_{21}-E_{12}$, which is antisymmetric. Then

$$
TK=E_{12}E_{21}-E_{12}E_{12}=E_{11},
$$

so $\operatorname{tr}(TK)=1$. The pairing of an upper triangular matrix with an antisymmetric matrix is therefore not always zero, and the complement is not orthogonal.

## The Projection along the Antisymmetric Part

**Definition.** Let $\pi:M_n(\mathbb{R})\to UT_n$ be the projection with kernel $\operatorname{Skew}_n$.

**The projection has an explicit formula.**

$$
\pi(X)_{ii}=X_{ii},\qquad \pi(X)_{ij}=X_{ij}+X_{ji}\ (i<j),\qquad \pi(X)_{ij}=0\ (i>j).
$$

*Proof.* Put $T=\pi(X)$ and $K=X-T$. For $i>j$ the entry $T_{ij}$ is zero by the formula and $K_{ij}=X_{ij}$. For $i<j$ the condition $K_{ij}=-K_{ji}$ reads $X_{ij}-T_{ij}=-X_{ji}$, hence $T_{ij}=X_{ij}+X_{ji}$. The diagonal is untouched because an antisymmetric matrix has zero diagonal.

**Measured, the remainder is always anti-Hermitian.** On $100$ random matrices at each of $n=2,3,4$ the part $X-\pi(X)$ was anti-Hermitian in $100$ cases out of $100$, and $\pi(X)$ was upper triangular in every case.

**The projection is not the symmetrisation.** On the diagonal the two maps agree, because both copy $X_{ii}$. Above the diagonal they differ by a factor two, since

$$
\pi(X)_{ij}=X_{ij}+X_{ji}=2\cdot\tfrac12(X_{ij}+X_{ji}).
$$

So the projection doubles what the symmetrisation computes, exactly where the matrix is not diagonal.

**The projection is not self-adjoint for the trace form.** Take $n=2$, $X=E_{21}$ and $Y=E_{12}$. Then $\pi(X)=0$ because $X$ is strictly lower, while $\pi(Y)=E_{12}+E_{21}$, and

$$
\langle\pi(X),Y\rangle=0,\qquad \langle X,\pi(Y)\rangle=\operatorname{tr}(E_{21}(E_{12}+E_{21}))=\operatorname{tr}(E_{22})=1.
$$

The two values differ, so $\pi$ is not self-adjoint.

**Self-adjointness would force the image to be the orthogonal complement.** A projection with kernel $\operatorname{Skew}_n$ is self-adjoint for the trace form exactly when its image is $\operatorname{Skew}_n^{\perp}=\operatorname{Sym}_n$. The image is $UT_n$, so the projection fails, and the symmetrisation is the self-adjoint projection onto the correct image.

## The Linear Model of the Symmetric Half

**The direct sum gives a linear isomorphism $\operatorname{Sym}_n\to UT_n$.** It is the restriction of $\pi$ to the symmetric matrices:

$$
S\longmapsto T=\pi(S),\qquad T_{ii}=S_{ii},\qquad T_{ij}=2S_{ij}\ (i<j),
$$

and its inverse is $T\mapsto\tfrac12(T+T^{\mathsf T})$.

**The two formulas are inverse.** For symmetric $S$ and $T=\pi(S)$ the equation $T+T^{\mathsf T}=2S$ holds entry by entry: on the diagonal both sides are $2S_{ii}$, and above the diagonal $T_{ij}+T_{ji}=2S_{ij}+0$. Measured on random symmetric matrices at $n=2,3,4$, the identity held in every case.

**The model is linear and not multiplicative.** The map preserves sums and scalar multiples because $\pi$ is linear. It does not preserve products: the product of two upper triangular matrices is upper triangular, while the product of two symmetric matrices need not be symmetric. So the model transports the vector space structure of $\operatorname{Sym}_n$ to $UT_n$ and leaves the Jordan product behind.

## What the Complement Buys

**A complement is a choice of splitting, and the two complements answer different questions.** $\operatorname{Sym}_n$ is the orthogonal complement for the trace form and the natural home of the Jordan product. $UT_n$ is the complement along $\operatorname{Skew}_n$ and the natural home of the flag.

**The two splittings are the two linear models of the same quotient.** The quotient $M_n(\mathbb{R})/\operatorname{Skew}_n$ has dimension $n(n+1)/2$; both $\operatorname{Sym}_n$ and $UT_n$ map isomorphically onto it. The first map is the symmetrisation, the second is $\pi$, and the two isomorphisms differ by the linear automorphism $S\mapsto\pi(S)$ of $\operatorname{Sym}_n$.

**The difference is visible in one number.** The trace form restricts to a nondegenerate form on $\operatorname{Sym}_n$ and to a form of rank $n$ on $UT_n$. So the first complement carries an inertia and the second carries a radical, and the radical is the nilpotent part $n_+$ of the triangular algebra.

## Summary

$UT_n$ and $\operatorname{Skew}_n$ have dimensions $n(n+1)/2$ and $n(n-1)/2$, they meet only at zero, and their sum is the whole algebra: $M_n(\mathbb{R})=UT_n\oplus\operatorname{Skew}_n$, measured as $3+1=4$, $6+3=9$ and $10+6=16$ at $n=2,3,4$. This complement is not orthogonal. The trace form restricted to $UT_n$ is $\sum_i X_{ii}Y_{ii}$, of rank $n$, with kernel the strictly upper triangular part $n_+$ of dimension $n(n-1)/2$; the diagonal direction $E_{11}-E_{22}$ is not in the kernel, since it pairs with $\operatorname{diag}(1,2)$ to $-1$. The trace-orthogonal complement of $\operatorname{Skew}_n$ is $\operatorname{Sym}_n$, and $UT_n$ is not orthogonal to it: $E_{12}$ pairs with $E_{21}-E_{12}$ to $1$. The projection onto $UT_n$ along $\operatorname{Skew}_n$ keeps the diagonal and sends the entry $(i,j)$ above it to $X_{ij}+X_{ji}$; it is not the symmetrisation and it is not self-adjoint. Restricted to $\operatorname{Sym}_n$ it is a linear isomorphism onto $UT_n$, with inverse $T\mapsto\tfrac12(T+T^{\mathsf T})$, and this is the linear model of the symmetric half on triangular matrices.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $UT_n$ | the upper triangular algebra, of dimension $n(n+1)/2$ |
| $\operatorname{Skew}_n$ | the antisymmetric matrices, of dimension $n(n-1)/2$ |
| $n_+$ | the strictly upper triangular part, the kernel of the trace form on $UT_n$ |
| $\pi$ | the projection onto $UT_n$ with kernel $\operatorname{Skew}_n$ |
| $\pi(X)_{ij}=X_{ij}+X_{ji}$ | the formula of $\pi$ above the diagonal |
| $\operatorname{tr}(XY)=\sum_i X_{ii}Y_{ii}$ | the trace form on $UT_n$, of rank $n$ |
| $T\mapsto\tfrac12(T+T^{\mathsf T})$ | the inverse of the linear model $\operatorname{Sym}_n\to UT_n$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for triangular matrices, projections and the trace.
- James E. Humphreys, *Linear Algebraic Groups* (Springer, 1975), for the flag, its stabiliser and the triangular splitting.
- [The Triangular Decomposition $h\oplus n_+\oplus n_-$](the-triangular-decomposition-h-n-plus-n-minus-of-mnr.html), for the three pieces and the nilpotent ideal.
- [The Two Halves as Orthogonal Complements for the Trace Form](the-two-halves-as-orthogonal-complements-for-the-trace-form.html), for the inertia and the true orthogonal complement.
- [$UT_n$ as a Linear Model of $\operatorname{Sym}_n$](utn-as-a-linear-model-of-sym-n-same-space-wrong-product.html), for the model in full.
- [Symmetric Pairs and Cartan Pairs: the Reductivity Criterion over $\mathbb{R}$](symmetric-pairs-and-cartan-pairs-the-reductivity-criterion-over-r.html), for the orthogonal split inside a Lie algebra.
