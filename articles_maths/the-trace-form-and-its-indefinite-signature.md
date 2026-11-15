# __The Trace Form and Its Indefinite Signature__

## Introduction

**The form $\langle X,Y\rangle=\operatorname{tr}(XY)$ on $M_n(\mathbb{R})$ is symmetric, nondegenerate, and indefinite for every $n\ge2$, with signature $\bigl(n(n+1)/2,\,n(n-1)/2\bigr)$.**

The article computes the Gram matrix of the form in the matrix-unit basis and identifies it with the permutation matrix of the transposition. It counts the signs, describes the isotropic cone and gives an explicit null vector, proves the associativity of the form and its invariance under the derivations, and reads the transpose as the fundamental symmetry of a Krein space. It assumes *The Matrix Algebra $M_n(\mathbb{R})$* for the algebra and its two halves, and it defers the definite competitor to *The Hilbert–Schmidt Form: Definite but Not Invariant*.

## The Form

**Define $\langle X,Y\rangle=\operatorname{tr}(XY)$ for $X,Y\in M_n(\mathbb{R})$.** The expression is bilinear, because the trace is linear and the matrix product is bilinear.

**The form is symmetric.** The identity $\operatorname{tr}(XY)=\operatorname{tr}(YX)$ holds for all pairs, by the cyclicity of the trace on a product of two factors.

**The form is nondegenerate.** Suppose $\operatorname{tr}(XY)=0$ for every $Y$. Testing on the matrix unit $Y=E_{ji}$ gives $X_{ij}=0$. Since $i$ and $j$ are arbitrary, $X=0$, and the radical is zero.

**In entries the form pairs $X$ with its transpose.** Each matrix unit has one nonzero entry, so

$$
\operatorname{tr}(XY)=\sum_{i,j=1}^{n}X_{ij}Y_{ji}.
$$

**The form is indefinite for $n\ge2$.** For $i\ne j$ the matrix unit $E_{ij}$ is nonzero and

$$
\operatorname{tr}(E_{ij}^{2})=\operatorname{tr}(\delta_{ji}E_{ij})=0.
$$

So a nonzero vector is isotropic. A positive definite form has no isotropic vector, and the form is not definite.

## The Gram Matrix

**In the matrix-unit basis the Gram matrix is the permutation matrix of the transposition.** On matrix units,

$$
\operatorname{tr}(E_{ij}E_{kl})=\delta_{jk}\delta_{il}.
$$

So the Gram entry of the units $(i,j)$ and $(k,l)$ equals $1$ exactly when $(k,l)=(j,i)$, and the Gram matrix is the permutation matrix $\Pi$ of the map $\tau(i,j)=(j,i)$.

**The identification was checked in low dimensions.** At $n=2$ and $n=3$ the computed Gram matrix equals $\Pi$ entry for entry. The matrix $\Pi$ has one $1$ in each row and in each column, and $\Pi^{2}=\mathrm{I}$.

**The permutation has $n$ fixed points and $n(n-1)/2$ transposed pairs.** The fixed points are the diagonal units $E_{ii}$. The remaining $n(n-1)$ units fall into the pairs $\{(i,j),(j,i)\}$ with $i<j$.

**The eigenvalues are the signs of the cycles.** A fixed point contributes the eigenvalue $+1$. A transposed pair contributes the block

$$
\begin{pmatrix}0&1\\ 1&0\end{pmatrix},
$$

of eigenvalues $+1$ and $-1$. So the positive directions are the $n$ fixed points together with one direction of each pair, and the negative directions are the other direction of each pair. Hence

$$
p=\frac{n(n-1)}{2}+n=\frac{n(n+1)}{2},\qquad q=\frac{n(n-1)}{2},\qquad p+q=n^{2}.
$$

**The count is confirmed at the first four dimensions.** The signatures read from the Gram matrix are these.

| $n$ | $p$ | $q$ | $p+q=n^{2}$ |
|---|---|---|---|
| 2 | 3 | 1 | 4 |
| 3 | 6 | 3 | 9 |
| 4 | 10 | 6 | 16 |
| 5 | 15 | 10 | 25 |

**The form is indefinite for every $n\ge2$, with exactly $n(n-1)/2$ negative directions.** The number $q=n(n-1)/2$ is positive as soon as $n\ge2$, and $p$ is positive too. So both signs occur, and the negative directions are counted by $q$.

## The Two Halves

**On $\operatorname{Sym}_n$ the form is positive definite.** For symmetric $X$ the entry formula gives $X_{ji}=X_{ij}$, so

$$
\operatorname{tr}(X^{2})=\sum_{i}X_{ii}^{2}+2\sum_{i<j}X_{ij}^{2}.
$$

The right-hand side is a sum of squares with positive coefficients, and it vanishes only for $X=0$. The restriction is the Euclidean structure of $\mathbb{R}^{n(n+1)/2}$ in the entries, up to the factor two.

**On $\operatorname{Skew}_n$ the form is negative definite.** For skew $X$ the entry formula gives $X_{ji}=-X_{ij}$, so

$$
\operatorname{tr}(X^{2})=-2\sum_{i<j}X_{ij}^{2}.
$$

The right-hand side is negative for every nonzero $X$.

**The two halves are orthogonal.** Let $S$ be symmetric and $K$ skew. Then

$$
\operatorname{tr}(SK)=\operatorname{tr}\bigl((SK)^{\mathsf T}\bigr)=\operatorname{tr}(K^{\mathsf T}S^{\mathsf T})=-\operatorname{tr}(KS)=-\operatorname{tr}(SK),
$$

so $\operatorname{tr}(SK)=0$. The first step uses the invariance of the trace under transposition, and the last uses $\operatorname{tr}(KS)=\operatorname{tr}(SK)$.

**The halves are the signature decomposition.** They are orthogonal, their dimensions add to $n^{2}$, and the form is positive on one and negative on the other. So $p=\dim\operatorname{Sym}_n$ and $q=\dim\operatorname{Skew}_n$ with no diagonalisation.

**At $n=2$ the count reads $4=3+1$.** The symmetric part is spanned by $E_{11}$, $E_{22}$ and $E_{12}+E_{21}$, and it is positive definite. The skew part is spanned by $J=E_{12}-E_{21}$, and $\operatorname{tr}(J^{2})=-2$. This is the signature $(3,1)$ of the form on the split-quaternion algebra, as in *Split-Quaternion Algebra*.

## The Isotropic Cone

**The null vectors are the solutions of $\operatorname{tr}(X^{2})=0$.** They form a quadric cone of dimension $n^{2}-1$. The cone is not a linear subspace for $n\ge2$: it contains $E_{12}$ and $E_{21}$ but not their sum, because $\operatorname{tr}\bigl((E_{12}+E_{21})^{2}\bigr)=2$.

**A null vector is built from one positive direction and one negative direction of equal norm.** Take

$$
H=E_{11}-E_{22},\qquad K=E_{12}-E_{21}.
$$

The first is symmetric and the second is skew, so the two are orthogonal. Their norms are

$$
\operatorname{tr}(H^{2})=2,\qquad \operatorname{tr}(K^{2})=-2.
$$

The norms are opposite, so the sum is null:

$$
X=H+K=E_{11}-E_{22}+E_{12}-E_{21},\qquad \operatorname{tr}(X^{2})=2-2=0.
$$

This was checked with numpy: the trace of $X^{2}$ is zero and $X$ is not zero.

**The pair $E_{12}+E_{21}$ and $E_{11}-E_{22}$ is orthogonal but not isotropic.** Both are symmetric, both have norm $2$, and their product has trace zero. Two positive directions span a positive definite plane, so that plane carries no null vector. The check with numpy gives $\operatorname{tr}(S^{2})=2$, $\operatorname{tr}(H^{2})=2$ and $\operatorname{tr}(SH)=0$ for $S=E_{12}+E_{21}$. A null vector needs one direction of each sign.

## The Form Is Associative

**The form satisfies $\langle XY,Z\rangle=\langle X,YZ\rangle$.** Both sides equal

$$
\sum_{i,j,k}X_{ij}Y_{jk}Z_{ki}.
$$

The identity is the associativity of the matrix product written through the trace, and it is what makes the form natural on an algebra rather than on a vector space.

**Every inner derivation is skew for the form.** For all $A,X,Y$,

$$
\langle [A,X],Y\rangle+\langle X,[A,Y]\rangle=\operatorname{tr}(AXY)-\operatorname{tr}(XAY)+\operatorname{tr}(XAY)-\operatorname{tr}(XYA)=0,
$$

because $\operatorname{tr}(AXY)=\operatorname{tr}(XYA)$ by cyclicity. The two middle terms cancel and the two outer terms agree.

**The form is invariant under the whole derivation algebra.** Every derivation of $M_n(\mathbb{R})$ is inner, of the form $\operatorname{ad}_A$, because the algebra is central simple. So the identity above is invariance under all derivations, not only under the inner ones.

**The form is invariant under conjugation by any invertible matrix.** For $S\in\mathrm{GL}_n(\mathbb{R})$,

$$
\langle SXS^{-1},SYS^{-1}\rangle=\operatorname{tr}(SXYS^{-1})=\operatorname{tr}(XY).
$$

So the isometry group contains the image of $\mathrm{GL}_n(\mathbb{R})$ under conjugation, of dimension $n^{2}-1$, and it contains the transpose as well. The invariance is far larger than the orthogonal group.

## The Krein Structure

**The transpose is an isometry of the form.** Indeed

$$
\operatorname{tr}(X^{\mathsf T}Y^{\mathsf T})=\operatorname{tr}\bigl((YX)^{\mathsf T}\bigr)=\operatorname{tr}(YX)=\operatorname{tr}(XY),
$$

and the transpose is an involution. So $J(X)=X^{\mathsf T}$ is an isometric involution.

**The transpose is the fundamental symmetry of the pair of forms.** Write $\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{\mathsf T}Y)$ for the Hilbert–Schmidt form. Then

$$
\langle X,Y\rangle=\operatorname{tr}(XY)=\langle X^{\mathsf T},Y\rangle_{\mathrm{HS}}.
$$

The operator $J$ is self-adjoint for the Hilbert–Schmidt form, its square is the identity, and its eigenspaces are $\operatorname{Sym}_n$ and $\operatorname{Skew}_n$ with eigenvalues $+1$ and $-1$. Those are the defining properties of a fundamental symmetry, and the definite form $\langle JX,Y\rangle_{\mathrm{HS}}$ has the signature of the trace form.

**So $M_n(\mathbb{R})$ with this form is a Krein space of type $(p,q)$.** The form is indefinite and nondegenerate, the fundamental symmetry exists, and the type is $\bigl(n(n+1)/2,n(n-1)/2\bigr)$. The imbalance is $p-q=n$, so the space is not neutral; it is split in the sense that both halves are nonzero for $n\ge2$.

**The maximal definite subspaces are the two halves.** The space $\operatorname{Sym}_n$ is positive definite of dimension $p$, the space $\operatorname{Skew}_n$ is negative definite of dimension $q$, and each is the orthogonal complement of the other. No positive definite subspace has dimension larger than $p$, and no negative definite subspace has dimension larger than $q$.

## No Definite Invariant Form

**A positive definite form cannot be invariant under the inner derivations.** Let $B$ be symmetric and positive definite, and suppose $B([A,X],Y)+B(X,[A,Y])=0$ for all $A,X,Y$. Take $A=E_{11}$ and $X=Y=E_{12}$. Then $[A,X]=E_{12}$, and the identity reads

$$
2B(E_{12},E_{12})=0.
$$

That contradicts $B(E_{12},E_{12})>0$, because $E_{12}$ is nonzero.

**So definiteness and invariance exclude each other on $M_n(\mathbb{R})$.** The trace form is invariant and indefinite. The Hilbert–Schmidt form is definite and not invariant, and the next article measures its defect.

**Every symmetric associative form is a multiple of the trace form.** Solving the associativity conditions $B(XY,Z)=B(X,YZ)$ for a symmetric $B$ leaves a one-dimensional space, spanned by $\operatorname{tr}(XY)$. The computation was done numerically at $n=2$ with ten unknowns and at $n=3$ with forty-five, and in both cases the solution space has dimension one and its Gram matrix is the transposition permutation of the units. Every member of that line is indefinite, because $\operatorname{tr}(E_{12}^{2})=0$.

## Summary

The form $\langle X,Y\rangle=\operatorname{tr}(XY)$ on $M_n(\mathbb{R})$ is symmetric and nondegenerate. Its Gram matrix in the matrix-unit basis is the permutation matrix of the transposition $(i,j)\mapsto(j,i)$, so its signature is $\bigl(n(n+1)/2,n(n-1)/2\bigr)$, measured as $(3,1)$, $(6,3)$, $(10,6)$ and $(15,10)$ at $n=2,3,4,5$. The form is therefore indefinite for every $n\ge2$, with exactly $n(n-1)/2$ negative directions, and the negative directions are the skew ones. The form is positive definite on $\operatorname{Sym}_n$ and negative definite on $\operatorname{Skew}_n$, and the two halves are orthogonal, which is the signature decomposition. The isotropic cone has dimension $n^{2}-1$, and an explicit null vector is $E_{11}-E_{22}+E_{12}-E_{21}$, the sum of a positive direction and a negative direction of equal norm. The form is associative, every inner derivation is skew for it, and it is invariant under conjugation by any invertible matrix. The transpose is an isometric involution and the fundamental symmetry, so the space is a Krein space of type $\bigl(n(n+1)/2,n(n-1)/2\bigr)$. No positive definite form is invariant under the inner derivations, and every symmetric associative form is a scalar multiple of this one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle X,Y\rangle=\operatorname{tr}(XY)$ | the trace form on $M_n(\mathbb{R})$ |
| $E_{ij}$ | the matrix unit, $1$ in the entry $(i,j)$ |
| $\mathrm{I}$ | the identity matrix |
| ${}^{\mathsf T}$ | the transpose |
| $\Pi$ | the Gram matrix of the form in the matrix-unit basis, a permutation matrix |
| $\tau(i,j)=(j,i)$ | the transposition whose permutation matrix is $\Pi$ |
| $(p,q)$ | the signature, $p=n(n+1)/2$ and $q=n(n-1)/2$ |
| $\operatorname{Sym}_n$, $\operatorname{Skew}_n$ | the positive and negative halves, of dimensions $p$ and $q$ |
| $\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{\mathsf T}Y)$ | the Hilbert–Schmidt form |
| $J(X)=X^{\mathsf T}$ | the fundamental symmetry |
| $\operatorname{ad}_A(X)=[A,X]$ | the inner derivation |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the trace form of a central simple algebra and its uniqueness among invariant forms.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the trace, the transpose and the symmetric and skew halves.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for Krein spaces, fundamental symmetries and maximal definite subspaces.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the algebra and the two halves of the transpose.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric.html), for the dimensions and the algebra of the two eigenspaces.
- [The Hilbert–Schmidt Form: Definite but Not Invariant](the-hilbert-schmidt-form-definite-but-not-invariant.html), for the definite form and the defect of invariance.
- [The Killing Form, Its Radical and the Centre of $\mathfrak{gl}_n(\mathbb{R})$](the-killing-form-its-radical-and-the-centre-of-gl-n-r.html), for the invariant form built from the adjoint representation.
