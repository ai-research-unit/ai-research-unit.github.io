# __The Peirce Decomposition of $\operatorname{Sym}_n$ as a Jordan Algebra__

## Introduction

**An idempotent of the Jordan algebra $\operatorname{Sym}_n$ cuts it into three Peirce spaces of dimensions $r(r+1)/2$, $r(n-r)$ and $(n-r)(n-r+1)/2$, and the multiplication rules among them are the graded rules of a Jordan algebra, with $J_1\circ J_0=0$ and $J_{1/2}\circ J_{1/2}\subseteq J_1\oplus J_0$.**

The article proves the three eigenvalues and the dimensions from the block form, proves the six multiplication rules, computes the rank-one case as the decomposition $\mathbb{R}E\oplus\mathbb{R}^{n-1}\oplus\operatorname{Sym}_{n-1}$, and shows that a maximal family of idempotents gives the $n$ diagonal lines and the $\binom n2$ off-diagonal lines of the Peirce basis. It assumes *The Jordan Algebra $\operatorname{Sym}_n$* for the product and *The Peirce Decomposition in $n$ Dimensions* for the associative version that it refines. It defers the identification of the Peirce lines with the corners of the algebra to *The Peirce Basis in $n$ Dimensions*.

## The Three Peirce Spaces

**The multiplication operator by an idempotent has the three eigenvalues $1$, $\tfrac12$, $0$.** For $E$ idempotent and $X\in\operatorname{Sym}_n$,

$$
L(E)X=E\circ X=\tfrac12(EX+XE),
$$

and the eigenvalues of $L(E)$ are determined by the block form. With $E=\operatorname{diag}(\mathrm{I}_r,0)$ and $X$ in blocks,

$$
X=\begin{pmatrix}A&B\\B^{\mathsf T}&C\end{pmatrix},\qquad E\circ X=\tfrac12\begin{pmatrix}2A&B\\B^{\mathsf T}&0\end{pmatrix},
$$

so $L(E)$ acts by $2A$ on the $A$-block, by $B$ on the $B$-block and by $0$ on the $C$-block. The three Peirce spaces are therefore

$$
J_1=\{X:L(E)X=X\},\qquad J_{1/2}=\{X:L(E)X=\tfrac12 X\},\qquad J_0=\{X:L(E)X=0\},
$$

and every symmetric $X$ lies in exactly one of them according to its block type.

**The three spaces sum directly to the whole algebra.** Since $L(E)$ is a self-adjoint operator for the trace form with eigenvalues $1$, $\tfrac12$, $0$, the eigenspaces span and their sum is direct:

$$
\operatorname{Sym}_n=J_1\oplus J_{1/2}\oplus J_0 .
$$

The identity was verified by building the three bases at $n=5$ for $r=1,2,3,4$ and checking that the union is a basis of $\operatorname{Sym}_5$.

**Only three eigenvalues occur, which is the difference from the associative Peirce decomposition.** The multiplication operator by an idempotent in the associative algebra has four eigenspaces, with the two off-diagonal corners separated; the Jordan operator merges them into the single space $J_{1/2}$. So the Jordan decomposition has three parts where the associative one has four, and the middle part is the sum of the two associative corners.

**The eigenspaces are the fixed points of the two projections $X\mapsto EXE$ and $X\mapsto(\mathrm{I}-E)X(\mathrm{I}-E)$.** In block form,

$$
J_1=\Big\{\begin{pmatrix}A&0\\0&0\end{pmatrix}\Big\},\qquad J_0=\Big\{\begin{pmatrix}0&0\\0&C\end{pmatrix}\Big\},\qquad J_{1/2}=\Big\{\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix}\Big\},
$$

so the three spaces are read off the three block positions, exactly as in the associative case, with the difference that the two off-diagonal positions are identified by the symmetry of $X$.

## The Dimensions and the Blocks

**The dimensions are the three triangular numbers.** The $A$-block is a symmetric $r\times r$ matrix, the $C$-block a symmetric $(n-r)\times(n-r)$ matrix, and the $B$-block an arbitrary $r\times(n-r)$ matrix. Hence

$$
\dim J_1=\frac{r(r+1)}{2},\qquad \dim J_{1/2}=r(n-r),\qquad \dim J_0=\frac{(n-r)(n-r+1)}{2},
$$

and the three add to $n(n+1)/2$. At $n=5$ the triples are $(1,4,10)$, $(3,6,6)$, $(6,6,3)$, $(10,4,1)$ for $r=1,2,3,4$, which the computation reproduces, and the sums are $15=\dim\operatorname{Sym}_5$ in each case.

**The middle space is the largest for $r$ near $n/2$, and the two outer cases are exchanged by $E\mapsto\mathrm{I}-E$.** The function $r(n-r)$ is maximal at $r=n/2$, where it is $n^{2}/4$, while the two outer spaces grow as $r^{2}/2$ and $(n-r)^{2}/2$; at $r=1$ and $r=n-1$ the dimensions are $(1,n-1,n(n-1)/2)$ and its reverse.

**The dimensions are those of the associative decomposition, collected and halved by symmetry.** The associative decomposition has dimensions $r^{2}$, $r(n-r)$, $(n-r)r$ and $(n-r)^{2}$, and the Jordan one keeps the same blocks with the off-diagonal mirrored. Hence

$$
\frac{r(r+1)}{2}=\frac{r^{2}+r}{2},\qquad r(n-r)=\frac{2r(n-r)}{2},\qquad \frac{(n-r)(n-r+1)}{2}=\frac{(n-r)^{2}+(n-r)}{2},
$$

which is the diagonal of the associative decomposition plus half of the off-diagonal, and the arithmetic is the arithmetic of the symmetric square.

## The Multiplication Rules

**The Peirce spaces multiply by the rule of the eigenvalues.** For $X_i\in J_i$ and $X_j\in J_j$,

$$
J_1\circ J_1\subseteq J_1,\qquad J_1\circ J_{1/2}\subseteq J_{1/2},\qquad J_1\circ J_0=0,
$$

$$
J_{1/2}\circ J_{1/2}\subseteq J_1\oplus J_0,\qquad J_{1/2}\circ J_0\subseteq J_{1/2},\qquad J_0\circ J_0\subseteq J_0 .
$$

All six were verified at $n=5$ for $r=1,2,3,4$ by multiplying basis elements and decomposing the products in the Peirce basis. The rules are the statement that $L(E)$ acts on a product by the sum of the eigenvalues, with the sum truncated at $1$ and at $0$ when it would leave the interval.

*Proof of the first and the third.* For $A,A'\in J_1$ the blocks are $\begin{pmatrix}A&0\\0&0\end{pmatrix}$, so $A\circ A'=\begin{pmatrix}A\circ A'&0\\0&0\end{pmatrix}\in J_1$. For $A\in J_1$ and $C\in J_0$ the blocks are complementary, so $AC=0$ and $CA=0$, hence $A\circ C=0$.

**The middle space squares into the two outer spaces.** For $B,B'$ the block computation gives

$$
\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix}\circ\begin{pmatrix}0&B'\\B'{}^{\mathsf T}&0\end{pmatrix}
=\frac12\begin{pmatrix}BB'{}^{\mathsf T}+B'B^{\mathsf T}&0\\0&B^{\mathsf T}B'+B'{}^{\mathsf T}B\end{pmatrix},
$$

so the $J_1$ component is the symmetrised $BB'{}^{\mathsf T}$ and the $J_0$ component is the symmetrised $B^{\mathsf T}B'$. The two components are the two Gram matrices of the pair, and the identity was verified numerically at $n=5$.

**The rules are the Jordan analogue of a grading, with the middle eigenvalue halved.** Since $L(E)$ is a derivation of the Jordan algebra with respect to itself, the eigenvalue of a product is the sum of the eigenvalues whenever the sum lies in the spectrum. The spectrum is $\{0,\tfrac12,1\}$, so $\tfrac12+\tfrac12=1$ lands in $J_1$, $\tfrac12+0=\tfrac12$ stays, and $1+1=2$ is truncated to $1$ by the identity $E\circ E=E$.

**No rule sends the outer spaces into the middle one.** Since $J_1\circ J_0=0$ and $J_1\circ J_1\subseteq J_1$, the sum $J_1\oplus J_0$ is a subalgebra, of dimension $r(r+1)/2+(n-r)(n-r+1)/2$. So the Peirce decomposition exhibits $\operatorname{Sym}_n$ as a subalgebra plus a bimodule over it, and the bimodule is the middle space.

## The Rank-One Case

**At $r=1$ the decomposition is $\mathbb{R}E\oplus\mathbb{R}^{n-1}\oplus\operatorname{Sym}_{n-1}$.** With $E=uu^{\mathsf T}$ a unit vector,

$$
J_1=\mathbb{R}E,\qquad J_{1/2}=\{ub^{\mathsf T}+bu^{\mathsf T}:b\in u^{\perp}\},\qquad J_0=\{X\in\operatorname{Sym}_n:Xu=0\},
$$

of dimensions $1$, $n-1$ and $n(n-1)/2$. The middle space is the space of vectors in the hyperplane, doubled by symmetry, and the outer space is the symmetric algebra of the hyperplane.

**The middle space carries the structure of the hyperplane.** For $B=ub^{\mathsf T}+bu^{\mathsf T}$ and $B'=ub'{}^{\mathsf T}+b'u^{\mathsf T}$,

$$
B\circ B'=\tfrac12\big(bb'{}^{\mathsf T}+b'b^{\mathsf T}\big)+\langle b,b'\rangle\,uu^{\mathsf T},
$$

so the product has a $J_0$ part which is the symmetric product of the two vectors and a $J_1$ part which is their inner product times the idempotent. The identity was verified for random vectors at $n=5$, and it is the matrix form of the spin-factor product of the Jordan theory.

**The rank-one decomposition is the cone decomposition.** The idempotent $E$ spans an extreme ray of the cone of squares, the space $J_1\oplus J_{1/2}$ is the tangent space to the cone at $E$ intersected with the algebra, and $J_0$ is the space of directions orthogonal to the ray. So the Peirce decomposition at a rank-one idempotent is the decomposition of the algebra along an extreme ray, which is the subject of *The Positive Cone and Its Boundary*.

**The decomposition is the model of the biquaternion case.** At $n=2$ and $r=1$ the dimensions are $1,1,1$, and the three spaces are the corner $\mathbb{B}_{++}$, the two mixed corners collected into one line, and the corner $\mathbb{B}_{--}$.

## The Maximal Family and the Coordinate Lines

**A maximal family of idempotents gives $n$ lines and $\binom n2$ lines.** Take $E_1,\dots,E_n$ orthogonal idempotents with sum $\mathrm{I}$, for instance the coordinate projections. The refined Peirce decomposition has the spaces

$$
J_{ii}=\mathbb{R}E_i\quad(1\le i\le n),\qquad J_{ij}=\{X:X=E_iXE_j+E_jXE_i\}\quad(i<j),
$$

each of dimension one, so the total is $n+\binom n2=n(n+1)/2$. The dimensions were checked by counting the coordinate lines and the pairs.

**The refined spaces are the common eigenspaces of the family.** Each $J_{ij}$ is the intersection of the $\tfrac12$-eigenspace of $L(E_i)$ with the $\tfrac12$-eigenspace of $L(E_j)$ and the $0$-eigenspace of every other $L(E_k)$, so the refined decomposition is the simultaneous diagonalisation of the commuting operators $L(E_1),\dots,L(E_n)$. So the Peirce decomposition is a spectral decomposition of a commuting family, and the $n$ coordinate lines are its fixed part.

**The coordinate lines are the idempotents and the off-diagonal lines are the nilpotent-like directions.** An element of $J_{ij}$ for $i<j$ has square in $J_{ii}\oplus J_{jj}$, since $L(E_i)$ gives $\tfrac12+\tfrac12=1$; so the off-diagonal line is not an idempotent line but a line whose square lands on the two diagonal lines. That is the Jordan shadow of the nilpotent structure of the Peirce basis, which the Peirce basis article develops in full.

**The maximal family is unique up to the orthogonal group.** Two maximal families summing to the identity are carried into one another by an element of $\mathrm{O}(n)$, so the $n+\binom n2$ count is an invariant of the algebra rather than of the frame.

## The Case $n=2$

**At $n=2$ the decomposition has two possible ranks.** For $r=1$ the dimensions are $1,1,1$ and for $r=2$ the idempotent is the identity and the decomposition is trivial, with $J_1=\operatorname{Sym}_2$ and the other two spaces zero. So the only nontrivial decomposition is the rank-one one, and it is the finest decomposition of the three-dimensional algebra.

**The rank-one decomposition at $n=2$ is the split into the three coordinate lines.** With $E=\tfrac12(\mathrm{I}+\sigma_3)$,

$$
J_1=\mathbb{R}E,\qquad J_{1/2}=\mathbb{R}\sigma_1,\qquad J_0=\mathbb{R}(\mathrm{I}-E),
$$

and the multiplication rules read $\sigma_1\circ\sigma_1=\mathrm{I}=E+(\mathrm{I}-E)\in J_1\oplus J_0$, $E\circ\sigma_1=\tfrac12\sigma_1\in J_{1/2}$ and $E\circ(\mathrm{I}-E)=0$. The three identities were verified on the Pauli matrices, and they are the smallest instance of the six rules.

**The biquaternion reading identifies the three lines with the corners.** The idempotent $E=\tilde\Pi_{\mathrm{id},+}$ spans the corner $\mathbb{B}_{++}$, its complement $\mathrm{I}-E=\tilde\Pi_{\mathrm{id},-}$ spans $\mathbb{B}_{--}$, and the middle line $\sigma_1$ is the sum of the two mixed corners $\mathbb{B}_{+-}$ and $\mathbb{B}_{-+}$ under the symmetry. So the Jordan Peirce decomposition is the Peirce decomposition of the algebra with the two mixed corners identified, which is the exact sense in which the Jordan structure is the quotient of the associative one by the symmetry.

## Summary

An idempotent $E$ of rank $r$ in $\operatorname{Sym}_n$ gives the Peirce decomposition $\operatorname{Sym}_n=J_1\oplus J_{1/2}\oplus J_0$, with $J_1$ the symmetric $r\times r$ block, $J_0$ the symmetric $(n-r)\times(n-r)$ block and $J_{1/2}$ the rectangular block, of dimensions $r(r+1)/2$, $(n-r)(n-r+1)/2$ and $r(n-r)$. The six multiplication rules hold, with $J_1\circ J_0=0$, $J_1\circ J_{1/2}\subseteq J_{1/2}$, $J_0\circ J_{1/2}\subseteq J_{1/2}$ and $J_{1/2}\circ J_{1/2}\subseteq J_1\oplus J_0$, the last with the two Gram matrix components. A maximal family of idempotents refines the decomposition into $n$ lines and $\binom n2$ lines, and at $n=2$ with $r=1$ the three spaces are one-dimensional and correspond to the two diagonal corners and the pair of mixed corners of the biquaternion frame.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E$ | an idempotent of $\operatorname{Sym}_n$, an orthogonal projection of rank $r$ |
| $L(E)X=E\circ X$ | the multiplication operator, with eigenvalues $1,\tfrac12,0$ |
| $J_1,J_{1/2},J_0$ | the three Peirce spaces |
| $r(r+1)/2$, $r(n-r)$, $(n-r)(n-r+1)/2$ | the three dimensions |
| $J_1\circ J_0=0$ | the vanishing of the outer product |
| $J_{1/2}\circ J_{1/2}\subseteq J_1\oplus J_0$ | the squaring rule of the middle space |
| $J_{ij}=\mathbb{R}E_iXE_j$ | the refined lines for a maximal family |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (AMS, 1968), for the Peirce decomposition of a Jordan algebra and its multiplication rules.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Peirce spaces and the rank-one spin factor.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the associative Peirce decomposition that the Jordan one refines.
- [The Jordan Algebra $\operatorname{Sym}_n$](the-jordan-algebra-sym-n.html), for the product, the idempotents and the degrees.
- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the associative decomposition with its four parts.
- [The Peirce Basis in $n$ Dimensions](the-peirce-basis-in-n-dimensions.html), for the coordinate lines and the refined decomposition.
