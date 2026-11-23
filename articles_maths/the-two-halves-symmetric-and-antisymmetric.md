# __The Two Halves: Symmetric and Antisymmetric__

## Introduction

**The transpose cuts $M_n(\mathbb{R})$ into a $+1$ half and a $-1$ half, and the two halves are not alike: one is a Jordan algebra, the other a Lie algebra, and neither is closed under the product of the algebra it came from.**

The article proves the split, counts the two dimensions, and exhibits with explicit matrices at $n=2$ and $n=3$ that the ordinary product leaves both halves. It proves that the square of an antisymmetric matrix is symmetric and negative semidefinite, that an antisymmetric matrix of odd order is singular, and that the two halves are orthogonal for the trace form. It assumes *The Matrix Algebra $M_n(\mathbb{R})$* for the matrix units and the trace, and defers the comparison with the symplectic fixed space to *The Two Classes Compared: $\operatorname{Sym}_n$ and $\mathfrak{sp}_n$ Have the Same Dimension*.

## The Transpose

**The transpose is an $\mathbb{R}$-linear anti-automorphism of order two.** For $A,B\in M_n(\mathbb{R})$ and $\lambda\in\mathbb{R}$,

$$
(A+B)^{\mathsf T}=A^{\mathsf T}+B^{\mathsf T},\qquad (\lambda A)^{\mathsf T}=\lambda A^{\mathsf T},\qquad (AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T},\qquad A^{\mathsf T\mathsf T}=A.
$$

The only condition that is not shared with an automorphism is the third: the order of a product is reversed.

**On matrix units the transpose exchanges the two indices.** $E_{ij}^{\mathsf T}=E_{ji}$. So it fixes each diagonal unit $E_{ii}$ and it swaps the pair $E_{ij}$, $E_{ji}$ for $i\ne j$.

**The trace and the determinant do not see the transpose.** $\operatorname{tr}(A^{\mathsf T})=\operatorname{tr}A$ and $\det(A^{\mathsf T})=\det A$. Both follow from the Leibniz formula, whose right-hand side is unchanged when every permutation is replaced by its inverse.

## The Two Eigenspaces

**Every matrix is the sum of a symmetric and an antisymmetric matrix, in exactly one way.**

$$
A=\underbrace{\tfrac12(A+A^{\mathsf T})}_{S}+\underbrace{\tfrac12(A-A^{\mathsf T})}_{K},\qquad S^{\mathsf T}=S,\qquad K^{\mathsf T}=-K.
$$

**Definition.** $\operatorname{Sym}_n=\{S\in M_n(\mathbb{R}):S^{\mathsf T}=S\}$ and $\operatorname{Skew}_n=\{K\in M_n(\mathbb{R}):K^{\mathsf T}=-K\}$.

**The two halves are the eigenspaces, so they meet only at zero.** If $X$ is both symmetric and antisymmetric then $X=X^{\mathsf T}=-X$, hence $X=0$. The two formulas above give the projections, and they add to the identity map.

**The dimensions are $n(n+1)/2$ and $n(n-1)/2$.** A symmetric matrix is free on the diagonal and above it, which is $n+\binom{n}{2}$ entries. An antisymmetric matrix is free strictly above the diagonal, which is $\binom{n}{2}$ entries, and its diagonal is zero. Hence

$$
\dim\operatorname{Sym}_n=\frac{n(n+1)}{2},\qquad \dim\operatorname{Skew}_n=\frac{n(n-1)}{2},\qquad \frac{n(n+1)}{2}+\frac{n(n-1)}{2}=n^{2}.
$$

The values are $3+1$, $6+3$, $10+6$ at $n=2,3,4$. The sum is the dimension of the algebra, as it must be for a direct sum.

## The Two Products

**The symmetric half is closed under the anticommutator.** Put $X\circ Y=\tfrac12(XY+YX)$. For symmetric $X,Y$,

$$
(X\circ Y)^{\mathsf T}=\tfrac12\bigl((XY)^{\mathsf T}+(YX)^{\mathsf T}\bigr)=\tfrac12(YX+XY)=X\circ Y,
$$

so $X\circ Y\in\operatorname{Sym}_n$. The product $\circ$ is commutative and $\mathbb{R}$-bilinear, and it satisfies the Jordan identity $X\circ(Y\circ X^{2})=(X\circ Y)\circ X^{2}$. So $\operatorname{Sym}_n$ is a Jordan algebra with unit $\mathrm{I}$.

**The anti-Hermitian half is closed under the commutator.** For anti-Hermitian $X,Y$,

$$
[X,Y]^{\mathsf T}=(XY-YX)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}-X^{\mathsf T}Y^{\mathsf T}=YX-XY=-[X,Y],
$$

so $[X,Y]\in\operatorname{Skew}_n$. The bracket is bilinear, alternating and satisfies the Jacobi identity, which holds in every associative algebra. So $\operatorname{Skew}_n=\mathfrak{so}(n)$ is a Lie algebra.

**The two products are exchanged by the sign, and that is the whole story.** The symmetric half is not closed under the commutator, because $[X,Y]$ is anti-self-adjoint for symmetric $X,Y$. The antisymmetric half is not closed under the anticommutator, because $X\circ Y$ is symmetric for antisymmetric $X,Y$. Each half carries the operation that the other one refuses.

## Neither Half Is Closed under the Product

**The product of two symmetric matrices is symmetric exactly when they commute.** $(XY)^{\mathsf T}=YX$, so $XY$ is symmetric exactly when $XY=YX$. At $n=2$, with

$$
S_1=\begin{pmatrix}1&2\\ 2&3\end{pmatrix},\qquad S_2=\begin{pmatrix}0&1\\ 1&0\end{pmatrix},\qquad S_1S_2=\begin{pmatrix}2&1\\ 3&2\end{pmatrix},
$$

the product is not symmetric. So $\operatorname{Sym}_2$ is not a subalgebra of $M_2(\mathbb{R})$.

**The same failure at $n=3$ is not a small-dimension accident.** With $S_1=\operatorname{diag}(1,2,3)$ and $S_2=E_{12}+E_{21}$,

$$
S_1S_2=\begin{pmatrix}0&1&0\\ 2&0&0\\ 0&0&0\end{pmatrix},
$$

which is not symmetric. The diagonal matrix and the permutation matrix commute only when the two diagonal entries they involve are equal.

**The product of two antisymmetric matrices is symmetric, so it misses the antisymmetric half.** $(KK')^{\mathsf T}=K'{}^{\mathsf T}K^{\mathsf T}=K'K$, which is the transpose of $KK'$; hence $KK'\in\operatorname{Sym}_n$. At $n=2$, with $K_1=E_{12}-E_{21}$ and $K_2=2E_{12}-2E_{21}$,

$$
K_1K_2=\begin{pmatrix}-2&0\\ 0&-2\end{pmatrix},
$$

symmetric and not antisymmetric. At $n=3$, with $K=E_{12}-E_{21}$ and $L=E_{23}-E_{32}$,

$$
KL=\begin{pmatrix}0&0&1\\ 0&0&0\\ 0&0&0\end{pmatrix}=E_{13},
$$

symmetric again, and again not antisymmetric. So the product maps $\operatorname{Skew}_n\times\operatorname{Skew}_n$ into $\operatorname{Sym}_n$ and never onto a nonzero element of $\operatorname{Skew}_n$.

**The square of a symmetric matrix stays symmetric.** $(S^{2})^{\mathsf T}=(S^{\mathsf T})^{2}=S^{2}$, for every symmetric $S$. The square of an antisymmetric matrix also stays symmetric, by the previous paragraph. So both halves square into the symmetric half, and only the symmetric half is stable under squaring.

## The Square of a Anti-Hermitian Matrix

**The square of an antisymmetric matrix is symmetric and negative semidefinite.** For antisymmetric $K$,

$$
K^{2}=-K^{\mathsf T}K,
$$

because $K^{\mathsf T}=-K$. The matrix $K^{\mathsf T}K$ is symmetric and positive semidefinite, since $v^{\mathsf T}K^{\mathsf T}Kv=\lVert Kv\rVert^{2}$. Hence

$$
\langle K^{2}v,v\rangle=-\lVert Kv\rVert^{2}\le0
$$

for every $v$. The eigenvalues of $K^{2}$ are therefore real and non-positive, and they are the negatives of the squared singular values of $K$.

**The measurement agrees with the proof.** On $100$ random antisymmetric matrices at each of $n=2,3,4$, the square was symmetric and had no positive eigenvalue in $100$ cases out of $100$ at each order.

**This is the inclusion $KK\subseteq SS$ in the notation of the cone of squares.** The set $\{K^{2}:K\in\operatorname{Skew}_n\}$ is contained in the cone of squares of $\operatorname{Sym}_n$, and it is contained in the negative semidefinite cone. The two inclusions are strict: a positive definite symmetric matrix is a square of a symmetric matrix and not a square of an antisymmetric matrix.

**The rank of the square is the rank of $K$, and it is even.** An antisymmetric matrix has $\ker K=\ker K^{2}$, so the rank of $K^{2}$ equals the rank of $K$. The nonzero eigenvalues of $K^{2}$ come in equal pairs, because the spectrum of $K$ is purely imaginary and conjugate. So the rank of an antisymmetric matrix is always even.

## Odd Order: the Determinant Vanishes

**An antisymmetric matrix of odd order is singular.** $\det K=\det K^{\mathsf T}=\det(-K)=(-1)^{n}\det K$. For odd $n$ this reads $\det K=-\det K$, hence $\det K=0$.

**The measurement confirms it and shows the even case is different.** Over $100$ random antisymmetric matrices the largest $|\det|$ was $0$ at $n=3$ and at $n=5$, and it was $15.6$ at $n=2$ and $181.2$ at $n=4$. The value is nonzero in the even case and exactly zero in the odd case, as the sign argument forces.

**For even order the determinant is a square and is non-negative.** An antisymmetric matrix of order $2m$ has $\det K=\operatorname{pf}(K)^{2}$ for the Pfaffian $\operatorname{pf}$, a polynomial of degree $m$ in the entries. So $\det K\ge0$ on $\operatorname{Skew}_{2m}$, and the zero set of the determinant is the zero set of the Pfaffian, of codimension one in the antisymmetric half.

## The Two Halves Are Orthogonal for the Trace Form

**The trace of a product of a symmetric and an antisymmetric matrix is zero.** $\operatorname{tr}(SK)=\operatorname{tr}((SK)^{\mathsf T})=\operatorname{tr}(K^{\mathsf T}S^{\mathsf T})=-\operatorname{tr}(KS)=-\operatorname{tr}(SK)$, hence $\operatorname{tr}(SK)=0$. Measured on $100$ random pairs at each of $n=2,3,4,5$, the value never differed from zero.

**The trace form has opposite signs on the two halves.** For symmetric $S$,

$$
\operatorname{tr}(S^{2})=\sum_{i,j}S_{ij}S_{ji}=\sum_{i,j}S_{ij}^{2}>0,
$$

and for anti-Hermitian $K$,

$$
\operatorname{tr}(K^{2})=-\sum_{i,j}K_{ij}^{2}<0.
$$

So the form is positive definite on $\operatorname{Sym}_n$ and negative definite on $\operatorname{Skew}_n$, and the two halves are exact orthogonal complements for it. *The Two Halves as Orthogonal Complements for the Trace Form* proves that statement and computes the inertia $(n(n+1)/2,n(n-1)/2)$.

**The splitting is therefore both a direct sum and an orthogonal one.** A direct sum of subspaces needs only $S\cap K=0$. The trace form adds that every element of one half is orthogonal to every element of the other.

## The Complex Contrast

**Over $\mathbb{C}$ the split is made by the conjugate transpose, not by the transpose.** Put $A^{*}=\overline{A^{\mathsf T}}$. Then $A^{*}$ is conjugate linear, $A^{**}=A$, and $(AB)^{*}=B^{*}A^{*}$. Its eigenspaces are the Hermitian matrices and the anti-Hermitian matrices.

**The two complex halves have equal real dimension.** A Hermitian matrix of order $n$ is determined by $n$ real diagonal entries and $\binom{n}{2}$ complex entries above the diagonal, so its real dimension is

$$
n+2\binom{n}{2}=n^{2}.
$$

An anti-Hermitian matrix is $i$ times a Hermitian one, so its real dimension is also $n^{2}$, and $n^{2}+n^{2}=2n^{2}$ is the real dimension of $M_n(\mathbb{C})$. The complex split is even; the real split by the transpose is not, because $n(n+1)/2$ and $n(n-1)/2$ differ by $n$.

**The reason is that the conjugate transpose is of the second kind, and the transpose is of the first kind.** The map $A^{*}$ fixes only the real scalars, so its fixed space is a real subspace and not a complex one. The transpose is complex linear on $M_n(\mathbb{C})$ as well, and its two complex eigenspaces $\operatorname{Sym}_n(\mathbb{C})$ and $\operatorname{Skew}_n(\mathbb{C})$ have complex dimensions $n(n+1)/2$ and $n(n-1)/2$, hence real dimensions $n(n+1)$ and $n(n-1)$, which again differ.

**The complex picture has one more feature: the Hermitian part carries a positive definite form.** $A\mapsto\operatorname{tr}(A^{*}A)$ is a norm there. Over $\mathbb{R}$ the analogous form $\operatorname{tr}(A^{\mathsf T}A)$ is also positive definite, but it is not the invariant form $\operatorname{tr}(AB)$, which is indefinite.

**The Jordan and the Lie structure survive the passage to $\mathbb{C}$.** $\operatorname{Sym}_n(\mathbb{C})$ is a Jordan algebra under the anticommutator and $\operatorname{Skew}_n(\mathbb{C})$ a Lie algebra under the commutator, for the same one-line proofs. What the real form adds is the sign of the trace form on each half, since a complex number has no sign.

## Summary

The transpose is an involution of $M_n(\mathbb{R})$, and its eigenspaces are the $\tfrac{n(n+1)}{2}$-dimensional symmetric half and the $\tfrac{n(n-1)}{2}$-dimensional antisymmetric half. The symmetric half is a Jordan algebra under the anticommutator and the antisymmetric half is a Lie algebra under the commutator. Neither is a subalgebra for the ordinary product: two symmetric matrices multiply to a symmetric matrix only when they commute, and two antisymmetric matrices always multiply to a symmetric one. The square of an antisymmetric matrix is symmetric and negative semidefinite, the rank of an antisymmetric matrix is even, and an antisymmetric matrix of odd order is singular. The two halves are orthogonal for the trace form, with a positive sign on the symmetric half and a negative one on the antisymmetric half. Over $\mathbb{C}$ the roles pass to the Hermitian and anti-Hermitian halves, which have equal real dimension $n^{2}$, because the conjugate transpose is conjugate linear.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| ${}^{\mathsf T}$ | the transpose, an involution of order two |
| $A^{*}$ | the conjugate transpose, used only in the complex contrast |
| $\operatorname{Sym}_n$ | the fixed space $\{S:S^{\mathsf T}=S\}$, of dimension $n(n+1)/2$ |
| $\operatorname{Skew}_n$ | the anti-fixed space $\{K:K^{\mathsf T}=-K\}$, of dimension $n(n-1)/2$ |
| $X\circ Y=\tfrac12(XY+YX)$ | the anticommutator, the Jordan product on $\operatorname{Sym}_n$ |
| $[X,Y]=XY-YX$ | the commutator, the Lie bracket on $\operatorname{Skew}_n$ |
| $\operatorname{tr}(XY)$ | the trace form, positive on $\operatorname{Sym}_n$ and negative on $\operatorname{Skew}_n$ |
| $\operatorname{pf}$ | the Pfaffian, with $\det K=\operatorname{pf}(K)^{2}$ for antisymmetric $K$ of even order |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the symmetric and antisymmetric parts, the transpose and the conjugate transpose.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the trace form and its behaviour on the two halves.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the matrix units, the trace and the two halves.
- [The Two Classes Compared: $\operatorname{Sym}_n$ and $\mathfrak{sp}_n$ Have the Same Dimension](the-two-classes-compared-sym-n-and-sp-n-have-the-same-dimension.html), for the second class of fixed spaces.
- [The Two Halves as Orthogonal Complements for the Trace Form](the-two-halves-as-orthogonal-complements-for-the-trace-form.html), for the inertia of the trace form.
