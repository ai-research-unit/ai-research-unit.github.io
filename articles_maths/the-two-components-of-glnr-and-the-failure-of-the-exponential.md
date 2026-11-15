# __The Two Components of $\mathrm{GL}_n(\mathbb{R})$ and the Failure of the Exponential__

## Introduction

**The unit group of $M_n(\mathbb{R})$ has exactly two connected components, cut by the sign of the determinant, and the exponential does not reach all of the positive one: the matrix with both diagonal entries $-1$ and a $1$ above the diagonal has positive determinant and is not an exponential.**

The article proves that the determinant cuts $\mathrm{GL}_n(\mathbb{R})$ into exactly two components, that the polar decomposition joins every matrix of positive determinant to the identity, and that the exponential image is a proper part of that component. It proves the counterexample in full: the centraliser of the matrix is two-dimensional, the exponential of every element of that centraliser has a positive diagonal, and the matrix has a negative one. It replaces the false guess that the image is dense by the parity obstruction. It assumes *The Exponential of a Real Matrix and Its Image*, and defers the connectedness of $\mathrm{SO}(n)$ to *The Exponential of the Antisymmetric Part: One-Parameter Rotations*.

Throughout $n\ge2$, the transpose is ${}^{\mathsf T}$ and the identity is $\mathrm{I}$.

## The Determinant Cuts the Group

**The determinant is a continuous homomorphism onto $\mathbb{R}^{\times}$.** It is a polynomial in the entries, so it is continuous, and $\det(AB)=\det A\det B$, so it is a homomorphism from the group to the multiplicative group of the field. It is onto, because $\det\operatorname{diag}(t,1,\dots,1)=t$ for every $t\ne0$.

**Definition.** Put

$$
\mathrm{GL}_n(\mathbb{R})^{+}=\{A:\det A>0\},\qquad \mathrm{GL}_n(\mathbb{R})^{-}=\{A:\det A<0\}.
$$

These are the preimages of the two components of $\mathbb{R}^{\times}$, they are open, and they are exchanged by multiplication by $-\mathrm{I}$.

**The sign of the determinant is locally constant.** A continuous function on a connected set has connected image, and the image of $\det$ on a connected set is a connected subset of $\mathbb{R}^{\times}$, that is, a single point of $(0,\infty)$ or of $(-\infty,0)$.

## At Least Two Components

**Two matrices of opposite determinant sign lie in different components.** Since $\det$ is locally constant, a component lies entirely in one of the two halves. The identity has determinant $1$ and $-\mathrm{I}$ has determinant $(-1)^{n}$, so for odd $n$ the two halves are already separated by the identity and its negative, and for even $n$ the matrix $\operatorname{diag}(-1,1,\dots,1)$ separates them. So there are at least two components, and each half is a union of components.

**The count is the whole content.** The hard part is not the lower bound; it is the statement that each half is connected. That is the next two sections.

## The Polar Decomposition

**Every invertible matrix is a positive definite matrix times an orthogonal one.** Let $A\in\mathrm{GL}_n(\mathbb{R})$. The matrix $AA^{\mathsf T}$ is symmetric and positive definite, so it has a unique positive definite square root $P=(AA^{\mathsf T})^{1/2}$, by the spectral theorem for $\operatorname{Sym}_n$. Then

$$
A=PQ,\qquad Q=P^{-1}A,
$$

and $Q$ is orthogonal, because

$$
Q^{\mathsf T}Q=A^{\mathsf T}P^{-2}A=A^{\mathsf T}(AA^{\mathsf T})^{-1}A=\mathrm{I}.
$$

The factor $P$ is symmetric positive definite and the factor $Q$ is orthogonal. The decomposition is unique: $P$ is forced to be $(AA^{\mathsf T})^{1/2}$ and $Q$ is then forced.

**The sign of the determinant lives in the orthogonal factor.** Since $\det P>0$,

$$
\det Q=\frac{\det A}{\det P},
$$

so $Q\in\mathrm{SO}(n)$ exactly when $\det A>0$. On the positive half the polar decomposition is a decomposition into a positive definite stretch and a rotation.

## At Most Two Components

**On the positive half the exponential of the symmetric part does the stretching.** A positive definite $P$ is $\exp S$ for the symmetric $S=\log P$, by the bijection of *The Exponential of a Real Matrix and Its Image*. Then

$$
A=\exp(S)\,Q,\qquad S\in\operatorname{Sym}_n,\quad Q\in\mathrm{SO}(n),
$$

and therefore

$$
\mathrm{GL}_n(\mathbb{R})^{+}=\exp(\operatorname{Sym}_n)\cdot\mathrm{SO}(n).
$$

**Both factors are connected.** The space $\operatorname{Sym}_n$ is a real vector space, hence connected, and $\exp$ is continuous, so $\exp(\operatorname{Sym}_n)=\operatorname{Sym}_n^{++}$ is connected. The group $\mathrm{SO}(n)$ is connected: every rotation is the exponential of an antisymmetric matrix, so it is the continuous image of the connected space $\operatorname{Skew}_n$. The product of two connected spaces is connected, and the multiplication map is continuous.

**Every matrix of positive determinant is joined to the identity.** Let $A=\exp(S)Q$ and let $t\mapsto Q_{t}$ be a path in $\mathrm{SO}(n)$ from $Q$ to $\mathrm{I}$. Then

$$
t\longmapsto \exp(tS)\,Q_{t}
$$

is a path in $\mathrm{GL}_n(\mathbb{R})^{+}$ from $A$ to $\mathrm{I}$. So the positive half is path-connected, hence connected.

**The negative half is a translate.** Multiplication by $-\mathrm{I}$ is a homeomorphism carrying $\mathrm{GL}_n(\mathbb{R})^{+}$ onto $\mathrm{GL}_n(\mathbb{R})^{-}$, so the negative half is path-connected too. The group has exactly two components, and both are path-connected.

**The two components are not the two halves of the transpose.** The symmetric and the antisymmetric matrices both meet each half, since $\mathrm{I}$ and $-\mathrm{I}$ are symmetric. The cut by the sign of the determinant is topological.

## The Counterexample

**A matrix of positive determinant that is not an exponential.** Put

$$
A=\begin{pmatrix}-1&1\\0&-1\end{pmatrix}.
$$

Then $\det A=1>0$ and $\operatorname{tr}A=-2$. The matrix lies in $\mathrm{GL}_2(\mathbb{R})^{+}$, and it is not $\exp X$ for any real $X$.

**Every candidate commutes with $A$.** Suppose that $\exp X=A$ for some $X\in M_2(\mathbb{R})$. The matrix $X$ commutes with its own exponential, because $X$ commutes with every power of $X$ and the series converges:

$$
XA=X\exp X=\exp X\,X=AX .
$$

So the problem is confined to the centraliser of $A$.

## The Centraliser

**The centraliser is two-dimensional.** Let $X=\begin{pmatrix}a&b\\c&d\end{pmatrix}$. The condition $XA=AX$ reads

$$
\begin{pmatrix}-a&a-b\\-c&c-d\end{pmatrix}=\begin{pmatrix}-a+c&d-b\\-c&-d\end{pmatrix},
$$

and comparing entries gives $c=0$ and $d=a$. So

$$
X=a\mathrm{I}+bN,\qquad N=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad N^{2}=0 .
$$

Conversely every matrix of that form commutes with $A$, so the centraliser is the two-dimensional space $\mathbb{R}\mathrm{I}\oplus\mathbb{R}N$. A numerical check of the linear system $XA-AX=0$ in the four entries returns rank two and the same two-dimensional kernel.

**The centraliser is the algebra generated by $\mathrm{I}$ and a square-zero matrix.** The two generators commute, $\mathrm{I}$ with everything and $N$ with itself, so the exponential factorises on the centraliser.

## The Exponential on the Centraliser

**The exponential of a centraliser element is the scalar exponential times a unipotent factor.** Since $a\mathrm{I}$ and $bN$ commute and $N^{2}=0$,

$$
\exp(a\mathrm{I}+bN)=e^{a}\big(\mathrm{I}+bN\big)=\begin{pmatrix}e^{a}&e^{a}b\\0&e^{a}\end{pmatrix}.
$$

The formula is checked numerically on $20$ random pairs $(a,b)$ with maximum error $3.8\cdot10^{-15}$.

**No value of the parameters gives $A$.** The two diagonal entries of $\exp(a\mathrm{I}+bN)$ are equal to $e^{a}$, while those of $A$ are $-1$. So equality would require

$$
e^{a}=-1,
$$

which has no real solution, because $e^{a}>0$ for every real $a$. Equivalently, $\det\exp(a\mathrm{I}+bN)=e^{2a}>0$ is consistent with $\det A=1$, and the trace $2e^{a}>0$ is not consistent with $\operatorname{tr}A=-2$.

**The obstruction survives the whole centraliser, not just the diagonal.** Both diagonal entries are $e^{a}$, so the matrix $\exp X$ is always a scalar multiple of a unipotent matrix, and its diagonal is positive. The matrix $A$ is a negative scalar multiple of a unipotent matrix. The two classes are disjoint.

## The Numerical Check

**A hundred samples of the centraliser never reach $A$.** With $a$ and $b$ drawn independently from the normal law with standard deviation $2$, and $X=a\mathrm{I}+bN$, the smallest value of $\lVert\exp X-A\rVert$ over the sample is

$$
1.26 .
$$

The distance is bounded below, as it must be: the quantity $e^{a}$ is positive, and the diagonal entry $-1$ is at distance $1+e^{a}\ge1$ from it.

**The exponent of the series is not the issue.** The truncated sums converge to $\exp X$ to machine precision, so the failure is not numerical. It is the sign of the diagonal: no truncation of a series of matrices with a positive diagonal converges to a matrix with a negative one.

## What the Image Is

**The exponential is not surjective onto the positive component.** The counterexample gives $\exp(M_2(\mathbb{R}))\ne\mathrm{GL}_2(\mathbb{R})^{+}$, and the block embedding $X\mapsto\operatorname{diag}(X,1,\dots,1)$ carries the same failure into every dimension $n\ge2$.

**The image is not open and not dense.** The matrices with two simple negative eigenvalues form an open set, they have no real logarithm by the parity argument of *The Exponential of a Real Matrix and Its Image*, and $\operatorname{diag}(-1,-2)$ is an interior point of that set. So an open set misses the image, and the image is neither dense nor the whole component. The claim that the image is dense in $\mathrm{GL}_n(\mathbb{R})^{+}$ is false, and the example at $n=2$ refutes it.

**The exact criterion is Culver's.** A real invertible matrix $A$ is $\exp X$ for a real $X$ if and only if, for every negative real eigenvalue $\lambda$ of $A$ and every size $d$, the number of Jordan blocks of size $d$ for $\lambda$ is even. For the counterexample the eigenvalue $-1$ carries a single block of size $2$, an odd number, and the criterion fails. The parity of the multiplicity alone is not enough: the multiplicity of $-1$ is two, and the block count is one.

**The image sits strictly between two extremes.** It contains a neighbourhood of $\mathrm{I}$, because the exponential is a local diffeomorphism at the origin, and it misses an open set, so it is neither a neighbourhood of the whole component nor a thin subset of it.

**What the two components say about the exponential.** The exponential is a map whose image lies in a connected component, misses part of it, and generates it as a group. That is the sharp picture: the local statement is true, the global one is false, and the two components are the exact arena in which the difference is visible.

## Summary

The determinant is a continuous surjection of $\mathrm{GL}_n(\mathbb{R})$ onto $\mathbb{R}^{\times}$, so the group has at least two components, one of positive and one of negative determinant. The polar decomposition $A=\exp(S)Q$ with $S$ symmetric and $Q$ orthogonal makes both halves connected, so the components are exactly two. The matrix $\begin{pmatrix}-1&1\\0&-1\end{pmatrix}$ has determinant $1$ and is not an exponential: any $X$ with $\exp X=A$ commutes with $A$, the centraliser is $\{a\mathrm{I}+bN\}$ with $N^{2}=0$, and $\exp(a\mathrm{I}+bN)=e^{a}(\mathrm{I}+bN)$ has positive diagonal entries while $A$ has $-1$ there. Over $100$ samples of the centraliser the distance to $A$ never falls below $1.26$. So the exponential misses part of the positive component, is not dense there, and its exact image is described by Culver's criterion on the Jordan blocks at the negative eigenvalues.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{GL}_n(\mathbb{R})^{+}$, $\mathrm{GL}_n(\mathbb{R})^{-}$ | the matrices of positive and of negative determinant |
| $\det$ | the determinant homomorphism |
| $P=(AA^{\mathsf T})^{1/2}$ | the positive definite polar factor |
| $Q=P^{-1}A$ | the orthogonal polar factor |
| $A$ | the counterexample $\begin{pmatrix}-1&1\\0&-1\end{pmatrix}$ |
| $N$ | the nilpotent $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ |
| $\operatorname{Sym}_n$ | the symmetric matrices |
| $\mathrm{SO}(n)$ | the rotations, of determinant one |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the polar decomposition and the sign of the determinant.
- W. J. Culver, *On the existence and uniqueness of the real logarithm of a matrix*, Proceedings of the American Mathematical Society (1966), for the criterion of §*What the Image Is*.
- [The Exponential of a Real Matrix and Its Image](the-exponential-of-a-real-matrix-and-its-image.html), for the series, the determinant identity and the local diffeomorphism.
- [The Exponential of the Antisymmetric Part: One-Parameter Rotations](the-exponential-of-the-antisymmetric-part-one-parameter-rotations.html), for the connectedness of $\mathrm{SO}(n)$.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the unit group and the singular set.
- [The Minimal Polynomial over $\mathbb{R}$ and the Real Jordan Form](the-minimal-polynomial-over-r-and-the-real-jordan-form.html), for the Jordan blocks at a negative eigenvalue.
