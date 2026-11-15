# __The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric__

## Introduction

**Over the real field the transpose cuts the algebra into the symmetric matrices and the antisymmetric ones, and the two halves carry the two products that the category needs: the symmetric half is a Jordan algebra under the anticommutator and the antisymmetric half is the Lie algebra $\mathfrak{so}(n)$ under the commutator.**

The article proves the direct sum, the orthogonality of the two halves for the trace form, the closure rules $[\operatorname{Sym},\operatorname{Sym}]\subseteq\operatorname{Skew}$, $[\operatorname{Skew},\operatorname{Skew}]\subseteq\operatorname{Sym}$ and $[\operatorname{Sym},\operatorname{Skew}]\subseteq\operatorname{Sym}$, and the properties that make each half what it is: even rank and purely imaginary spectrum for the antisymmetric half, real spectrum and orthogonal diagonalisation for the symmetric one. It computes the Killing form of $\mathfrak{so}(n)$, which is $(n-2)\operatorname{tr}(XY)$ and vanishes at $n=2$, and it shows that the exponential of each half lands in the corresponding group. It assumes *The Involutions over $\mathbb{R}$ and over $\mathbb{C}$* for the split and *The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$* for the real trace form. It defers the multiplication tables to *The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$* and the complex case to *The Two Halves over $\mathbb{C}$: Hermitian and Skew-Hermitian*.

## The Split

**Every real matrix is a symmetric matrix plus an antisymmetric one, uniquely.** With $A^{\mathsf T}$ the transpose,

$$
A=\underbrace{\tfrac12(A+A^{\mathsf T})}_{S}+\underbrace{\tfrac12(A-A^{\mathsf T})}_{K},\qquad S^{\mathsf T}=S,\quad K^{\mathsf T}=-K .
$$

The two summands are the projections onto the eigenspaces of the transpose, and they are orthogonal for the trace form:

$$
\operatorname{tr}(S^{\mathsf T}K)=\operatorname{tr}(SK)=-\operatorname{tr}(KS)=-\operatorname{tr}(SK)=0 .
$$

The last equality uses the cyclicity of the trace, so the vanishing holds for every pair, not only for a pair in general position.

**The dimensions are $n(n+1)/2$ and $n(n-1)/2$, and they sum to $n^{2}$.** A symmetric matrix is free on and above the diagonal, an antisymmetric one is free strictly above it, and

$$
\frac{n(n+1)}{2}+\frac{n(n-1)}{2}=n^{2}.
$$

At $n=2$ the split is $4=3+1$, at $n=3$ it is $9=6+3$, and at $n=4$ it is $16=10+6$. The antisymmetric half has dimension $n(n-1)/2$ and the dimension of the Lie algebra $\mathfrak{so}(n)$. The triangular algebra $UT_n$ is the other complement of the antisymmetric half in the vector space, with the same dimension as $\operatorname{Sym}_n$ and a different product; the comparison is in *$UT_n$ as the Complement of the Antisymmetric Part (Transpose Case)*.

**The halves are not subalgebras for the ordinary product.** The product of two symmetric matrices is symmetric exactly when they commute, and the product of two antisymmetric matrices is antisymmetric exactly when they commute. So neither half is closed under the matrix product, and the two closure rules of §*The Closure Rules* are the correct substitute. The vector space splits; the algebra does not.

## The Symmetric Half

**The symmetric half is a Jordan algebra under the anticommutator.** Put

$$
S\circ T=\tfrac12(ST+TS).
$$

The product is commutative and it satisfies the Jordan identity $(S\circ S)\circ(T\circ S)=((S\circ S)\circ T)\circ S$, so $\operatorname{Sym}_n$ with $\circ$ is a **Jordan algebra**, of dimension $n(n+1)/2$. The unit is the identity matrix, and the product of two symmetric matrices is again symmetric because $(ST+TS)^{\mathsf T}=T^{\mathsf T}S^{\mathsf T}+S^{\mathsf T}T^{\mathsf T}=TS+ST$.

**A symmetric matrix has a real spectrum and is diagonalisable by an orthogonal matrix.** The spectral theorem gives $S=Q\Lambda Q^{\mathsf T}$ with $Q\in\mathrm{O}(n)$ and $\Lambda$ real diagonal, so the eigenvalues of $S$ are real and the eigenvectors can be chosen orthonormal. The trace and the determinant are the sum and the product of those eigenvalues, and both are real.

**The quadratic form of the half is the trace of the square.** For symmetric $S$,

$$
\operatorname{tr}(S^{2})=\sum_{i,j}S_{ij}^{2}\ge0,
$$

with equality only for $S=0$. So the trace form restricted to the symmetric half is positive definite, of signature $\big(\tfrac{n(n+1)}{2},0\big)$, and the same computation on the antisymmetric half gives $\operatorname{tr}(K^{2})=-\sum_{i<j}K_{ij}^{2}<0$.

## The Antisymmetric Half

**The antisymmetric half is the Lie algebra $\mathfrak{so}(n)$ under the commutator.** For antisymmetric $K,L$ the commutator is antisymmetric, since

$$
[K,L]^{\mathsf T}=(KL-LK)^{\mathsf T}=L^{\mathsf T}K^{\mathsf T}-K^{\mathsf T}L^{\mathsf T}=LK-KL=-[K,L],
$$

and the Jacobi identity holds because the commutator of matrices always satisfies it. The dimension is $n(n-1)/2$, and the rank of the algebra, the dimension of a maximal torus, is $\lfloor n/2\rfloor$.

**An antisymmetric matrix has even rank and a purely imaginary spectrum.** If $Kv=\lambda v$ then $K\bar v=\bar\lambda\bar v$ and $\bar v^{\mathsf T}Kv=\lambda\bar v^{\mathsf T}v$, while transposing gives $\bar v^{\mathsf T}Kv=-(\bar v^{\mathsf T}Kv)$, so $\lambda$ is purely imaginary or zero. The eigenvalues are therefore $0$ and pairs $\pm i\theta$ with $\theta\in\mathbb{R}\setminus\{0\}$, and the rank, which is twice the number of nonzero pairs, is even:

$$
\operatorname{rank}K\in\{0,2,4,\dots\},\qquad \operatorname{rank}K\le 2\Big\lfloor\frac{n}{2}\Big\rfloor .
$$

The computation at $n=3,4,5,6$ gives ranks $2,4,4,6$ for a generic antisymmetric matrix, and the eigenvalues have vanishing real part to machine precision.

**The determinant of an antisymmetric matrix vanishes at odd $n$ and is a square at even $n$.** For odd $n$ the matrix is singular, since a nonzero determinant would make the rank odd. For even $n=2m$ there is a polynomial $\operatorname{Pf}$ of degree $m$, the **Pfaffian**, with

$$
\det K=\operatorname{Pf}(K)^{2},\qquad \operatorname{Pf}(K)=\sum_{\text{pairings}}\operatorname{sgn}\prod K_{i j}.
$$

At $n=4$ the formula reads $\operatorname{Pf}=K_{12}K_{34}-K_{13}K_{24}+K_{14}K_{23}$, and the identity $\det K=\operatorname{Pf}^{2}$ was verified on a random antisymmetric matrix.

## The Closure Rules

**The four products land in the two halves according to a sign rule.** For symmetric $S,T$ and antisymmetric $K,L$,

$$
[S,T]=ST-TS\in\operatorname{Skew}_n,\qquad \{K,L\}=KL+LK\in\operatorname{Sym}_n,\qquad [S,K]=SK-KS\in\operatorname{Sym}_n .
$$

The first two say that the commutator exchanges the halves and that the anticommutator also exchanges them; the third says that the commutator of a symmetric with an antisymmetric matrix stays in the symmetric half. All three were verified on random elements at $n=2,\dots,6$.

**The rule is a grading and not a decomposition into ideals.** In the language of the split, $\operatorname{Sym}$ is the $+1$ part and $\operatorname{Skew}$ the $-1$ part, and the commutator carries $(+1,+1)$ and $(-1,-1)$ to $-1$ while it carries $(+1,-1)$ to $+1$. The symmetric half is therefore a Lie subalgebra only under the commutator of its own elements composed with a sign, and the correct object is the pair $(\mathfrak{so}(n),\operatorname{Sym}_n)$ with $\operatorname{Sym}_n$ a module.

**The product of two symmetric matrices has both parts, and each part is forced.** For symmetric $S,T$,

$$
ST=\tfrac12\{S,T\}+\tfrac12[S,T],
$$

with the first term symmetric and the second antisymmetric. The decomposition of $ST$ is therefore the decomposition of the product into its symmetric and antisymmetric parts, which is the content of *The Symmetric and Antisymmetric Parts of a Product*. Neither part vanishes identically, and the two are exchanged by the transpose.

## The Two Forms

**The trace form is definite on each half, with opposite signs.** For symmetric $S$ and antisymmetric $K$,

$$
\operatorname{tr}(S^{2})=\sum_{i,j}S_{ij}^{2}>0,\qquad \operatorname{tr}(K^{2})=-\sum_{i<j}2K_{ij}^{2}<0 ,
$$

so the restriction to $\operatorname{Sym}_n$ has signature $\big(\tfrac{n(n+1)}{2},0\big)$ and the restriction to $\operatorname{Skew}_n$ has signature $\big(0,\tfrac{n(n-1)}{2}\big)$. The form on the whole algebra is the sum of the two, of signature $(n(n+1)/2,\,n(n-1)/2)$ in the ordered pair, which is the split form of $\operatorname{tr}(A^{2})$ on $M_n(\mathbb{R})$.

**The Killing form of $\mathfrak{so}(n)$ is $(n-2)\operatorname{tr}(XY)$.** A direct computation from the structure constants gives

$$
B(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)=(n-2)\operatorname{tr}(XY),
$$

and the identity was verified at $n=2,\dots,6$ by building the matrices of the adjoint action in the basis $E_{ij}-E_{ji}$ and comparing. The factor $n-2$ is the whole story: the form is negative definite for $n\ge3$ and vanishes identically at $n=2$, where $\mathfrak{so}(2)$ is one-dimensional and abelian. The consequences for the radical and for the triangular case are in *The Killing Form, Its Radical and the Triangular Case*.

**The two forms are different objects.** The trace form is a form on the algebra, defined without a Lie structure; the Killing form is built from the adjoint action. On $\mathfrak{so}(n)$ they differ by the scalar $n-2$, and at $n=2$ the Killing form degenerates while the trace form does not. A statement about one is not a statement about the other, and the article *The Trace Form and Its Signature on the Two Halves* keeps them apart.

## The Exponential of Each Half

**The exponential of an antisymmetric matrix is a rotation.** If $K^{\mathsf T}=-K$ then

$$
(e^{K})^{\mathsf T}e^{K}=e^{K^{\mathsf T}}e^{K}=e^{-K}e^{K}=\mathrm{I},\qquad \det e^{K}=e^{\operatorname{tr}K}=1 ,
$$

so $e^{K}\in\mathrm{SO}(n)$. Both identities were verified at $n=2,\dots,5$ by summing the series. The map $K\mapsto e^{K}$ is a local diffeomorphism near $0$ and its image is the identity component of $\mathrm{SO}(n)$, which is the whole group.

**The exponential of a symmetric matrix is a positive definite symmetric matrix.** If $S^{\mathsf T}=S$ then $(e^{S})^{\mathsf T}=e^{S}$, and the eigenvalues of $e^{S}$ are $e^{\lambda_i}>0$. Conversely every positive definite symmetric matrix is $e^{S}$ for a unique symmetric $S$, namely $S=\log P$ computed in the eigenbasis. So

$$
\exp:\operatorname{Sym}_n\longrightarrow\{P\ \text{symmetric, positive definite}\}
$$

is a bijection, and it is the model of the polar decomposition of *The Polar Decomposition from the Two Halves*.

## The Case $n=2$

**At $n=2$ the split is $4=3+1$ and the antisymmetric half is one line.** The antisymmetric matrices are $\theta J$ with $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, so $\mathfrak{so}(2)=\mathbb{R}J$ is abelian of dimension $1$ and rank $1$. The symmetric half is spanned by $\mathrm{I}$, $\sigma_3=\operatorname{diag}(1,-1)$ and $\sigma_1$, of dimension $3$.

**The exponential of the line is the circle.** Since $J^{2}=-\mathrm{I}$,

$$
e^{\theta J}=(\cos\theta)\mathrm{I}+(\sin\theta)J=\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix},
$$

so $\exp:\mathfrak{so}(2)\to\mathrm{SO}(2)$ is surjective with kernel $2\pi\mathbb{Z}$, and $\mathrm{SO}(2)$ is a circle. The period is the first instance of the double cover of *The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover*.

## Summary

The transpose splits $M_n(\mathbb{R})$ into the symmetric half, of dimension $n(n+1)/2$, and the antisymmetric half, of dimension $n(n-1)/2$, orthogonal for the trace form. The symmetric half is a Jordan algebra under $S\circ T=\tfrac12(ST+TS)$, with real spectrum and orthogonal diagonalisation, and the trace form is positive definite on it. The antisymmetric half is the Lie algebra $\mathfrak{so}(n)$ under the commutator, of rank $\lfloor n/2\rfloor$, with even rank, purely imaginary spectrum, vanishing determinant at odd $n$ and $\det K=\operatorname{Pf}(K)^{2}$ at even $n$. The closure rules send $[\operatorname{Sym},\operatorname{Sym}]$ and $\{K,L\}$ across the halves and keep $[S,K]$ in $\operatorname{Sym}$. The Killing form of $\mathfrak{so}(n)$ is $(n-2)\operatorname{tr}(XY)$, degenerate exactly at $n=2$. The exponentials are the rotations and the positive stretches.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Sym}_n$ | the symmetric half, of dimension $n(n+1)/2$ |
| $\operatorname{Skew}_n$ | the antisymmetric half, of dimension $n(n-1)/2$ |
| $S\circ T=\tfrac12(ST+TS)$ | the anticommutator, the Jordan product |
| $[S,T]=ST-TS$ | the commutator, the Lie product |
| $\mathfrak{so}(n)$ | the antisymmetric half as a Lie algebra, of rank $\lfloor n/2\rfloor$ |
| $\operatorname{Pf}(K)$ | the Pfaffian, with $\det K=\operatorname{Pf}(K)^{2}$ at even $n$ |
| $B(X,Y)=(n-2)\operatorname{tr}(XY)$ | the Killing form of $\mathfrak{so}(n)$ |
| $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ | the generator of $\mathfrak{so}(2)$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for symmetric and skew-symmetric matrices, their spectra and the Pfaffian.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (AMS, 1968), for the Jordan product on symmetric matrices.
- Karin Erdmann and Mark Wildon, *Introduction to Lie Algebras* (Springer, 2006), for $\mathfrak{so}(n)$, its rank and its Killing form.
- [The Involutions over $\mathbb{R}$ and over $\mathbb{C}$](the-involutions-over-r-and-over-c.html), for the transpose involution and the classification of its kind.
- [The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$](the-two-base-fields-mnr-inside-mnc.html), for the real trace form and its definiteness.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the trace, the determinant and the skew-Hermitian algebra $\mathfrak{u}(n)$.
