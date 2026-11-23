# __The Peirce Decomposition of $\operatorname{Sym}_n(\mathbb{R})$ as a Jordan Algebra__

## Introduction

**A real orthogonal projection $E$ cuts the symmetric matrices into three Peirce spaces of dimensions $r(r+1)/2$, $r(n-r)$ and $(n-r)(n-r+1)/2$, and these three numbers add to $n(n+1)/2$.** The cut is the one of a formally real Jordan algebra, written in coordinates.

The article defines the Jordan product $X\circ Y=\tfrac12(XY+YX)$, shows that an idempotent of the Jordan algebra is an orthogonal projection, computes the three Peirce spaces with their dimensions, states the five multiplication rules, and reads the Jordan axioms and the trace form in the block coordinates of a projection of rank $r$. The case $n=3$ with a rank-one idempotent gives dimensions $1$, $2$ and $3$. It assumes *The Peirce Basis and the Corners over $\mathbb{R}$* for the corners of the associative algebra, and it defers the interaction with the transpose to *The Peirce Decomposition and the Two Halves over $\mathbb{R}$*.

## The Jordan Product on $\operatorname{Sym}_n$

**The symmetric matrices form a Jordan algebra under the anticommutator.**

$$
X\circ Y=\tfrac12\big(XY+YX\big).
$$

The product is bilinear and symmetric, and it lands in $\operatorname{Sym}_n$ because $(XY+YX)^{\mathsf T}=YX+XY$. The unit is $\mathrm{I}$, since $\mathrm{I}\circ X=X$.

**The algebra is formally real.** For $X\in\operatorname{Sym}_n$,

$$
X\circ X=X^{2},\qquad \operatorname{tr}(X^{2})=\sum_{i,j}X_{ij}^{2}\ \ge 0,
$$

with equality only at $X=0$. A sum of squares that vanishes only at zero is the formal reality of the algebra. It is what fails on $\operatorname{Skew}_n$ for the same product, where $K\circ K=-K^{\mathsf T}K$ has nonpositive trace.

**The product obeys the Jordan identity.**

$$
(X\circ Y)\circ(X\circ X)=X\circ\big(Y\circ(X\circ X)\big).
$$

Both sides are polynomials of degree four in the entries, and the identity holds because the associative product does. With commutativity, an invertible element and this identity, $\operatorname{Sym}_n$ is a Jordan algebra over $\mathbb{R}$.

## The Idempotents

**An idempotent of the Jordan algebra is a real orthogonal projection.** An element $E\in\operatorname{Sym}_n$ satisfies $E\circ E=E$ exactly when

$$
E^{2}=E,\qquad E^{\mathsf T}=E .
$$

The first equation is the idempotent condition and the second is membership in $\operatorname{Sym}_n$; together they say that $E$ is the orthogonal projection onto its image. The rank $r=\operatorname{rk}E=\operatorname{tr}E$ is an integer between $0$ and $n$.

**The decomposition depends on $E$ through its two eigenspaces.** Put $U=\operatorname{im}E$ and $W=\ker E=U^{\perp}$, of dimensions $r$ and $n-r$, and $\mathrm{I}=E+(\mathrm{I}-E)$. In an orthonormal basis adapted to $U$ and $W$ every symmetric matrix reads

$$
X=\begin{pmatrix} A & B\\ B^{\mathsf T} & C\end{pmatrix},
$$

with $A$ of order $r$, $C$ of order $n-r$ and $B$ of size $r\times(n-r)$.

## The Three Peirce Spaces

**The Peirce spaces are the three ways a symmetric matrix can sit inside the two eigenspaces of $E$.**

$$
\operatorname{Sym}(1)=E\operatorname{Sym}_nE,\qquad
\operatorname{Sym}(\tfrac12)=\{X\in\operatorname{Sym}_n:EX+XE=X\},\qquad
\operatorname{Sym}(0)=(\mathrm{I}-E)\operatorname{Sym}_n(\mathrm{I}-E).
$$

**Proposition.** The three spaces are the eigenspaces of the operator $X\mapsto E\circ X$ with eigenvalues $1$, $\tfrac12$ and $0$, and

$$
\operatorname{Sym}_n=\operatorname{Sym}(1)\oplus\operatorname{Sym}(\tfrac12)\oplus\operatorname{Sym}(0).
$$

*Proof.* In the block form above, $E\circ X=\tfrac12\begin{pmatrix}2A&B\\ B^{\mathsf T}&0\end{pmatrix}$. The eigenvalue $1$ forces $B=0$ and $C=0$, which is $E\operatorname{Sym}_nE$; the eigenvalue $\tfrac12$ forces $A=0$ and $C=0$; the eigenvalue $0$ forces $A=0$ and $B=0$. The three conditions are complementary, so every $X$ splits uniquely.

**The middle space is the annihilator of the corner.** The condition $EX+XE=X$ reads $EXE=0$: multiply on both sides by $E$ and use $E^{2}=E$. So

$$
\operatorname{Sym}(\tfrac12)=\{X\in\operatorname{Sym}_n:EXE=0\},
$$

the symmetric part of the two off-diagonal corners taken together.

## The Dimensions

**The three dimensions are $r(r+1)/2$, $r(n-r)$ and $(n-r)(n-r+1)/2$.** A basis of $\operatorname{Sym}(1)$ is $E_{ii}$ for $i\in U$ together with $E_{ij}+E_{ji}$ for $i<j$ in $U$, which gives $r+r(r-1)/2=r(r+1)/2$. A basis of $\operatorname{Sym}(\tfrac12)$ is $E_{ij}+E_{ji}$ with $i\in U$ and $j\in W$, which gives $r(n-r)$. A basis of $\operatorname{Sym}(0)$ is the same construction inside $W$, which gives $(n-r)(n-r+1)/2$.

**The three numbers add to the dimension of the algebra.** Writing $s=n-r$,

$$
\frac{r(r+1)}{2}+rs+\frac{s(s+1)}{2}=\frac{r^{2}+r+2rs+s^{2}+s}{2}=\frac{(r+s)^{2}+(r+s)}{2}=\frac{n(n+1)}{2}.
$$

So the Peirce decomposition is a decomposition of the whole of $\operatorname{Sym}_n$ and loses nothing.

**The dimensions are not $r^{2}$, $2r(n-r)$ and $(n-r)^{2}$.** Those are the dimensions of the corners of the associative algebra $M_{n}(\mathbb{R})$, and they add to $n^{2}$. The Jordan algebra is the smaller space of dimension $n(n+1)/2$: the diagonal corner contributes only its symmetric part $A_{kk}\cap\operatorname{Sym}_n$, of dimension $r(r+1)/2$, and the middle space takes one copy of the off-diagonal corner pair, not two.

## The Coordinates at the Standard Idempotent

**With $E=\operatorname{diag}(1,\dots,1,0,\dots,0)$ the three spaces are the three block positions.**

$$
X_{1}=\begin{pmatrix}A&0\\ 0&0\end{pmatrix},\qquad
X_{1/2}=\begin{pmatrix}0&B\\ B^{\mathsf T}&0\end{pmatrix},\qquad
X_{0}=\begin{pmatrix}0&0\\ 0&C\end{pmatrix},
$$

with $A$ symmetric of order $r$, $B$ arbitrary of size $r\times(n-r)$ and $C$ symmetric of order $n-r$. The dimensions follow at once: $r(r+1)/2$, $r(n-r)$ and $(n-r)(n-r+1)/2$.

**A general element is the sum of its three components.**

$$
X_{1}=EXE,\qquad X_{0}=(\mathrm{I}-E)X(\mathrm{I}-E),\qquad X_{1/2}=X-X_{1}-X_{0},
$$

and the three pieces satisfy $EX_{1}E=X_{1}$, $EX_{1/2}E=0$, $(\mathrm{I}-E)X_{0}(\mathrm{I}-E)=X_{0}$. The reconstruction is exact and the components are unique.

## The Multiplication Rules

**The five Peirce rules are the multiplication table of the three spaces.**

$$
\operatorname{Sym}(1)\circ\operatorname{Sym}(1)\subseteq\operatorname{Sym}(1),\qquad
\operatorname{Sym}(1)\circ\operatorname{Sym}(\tfrac12)\subseteq\operatorname{Sym}(\tfrac12),
$$

$$
\operatorname{Sym}(\tfrac12)\circ\operatorname{Sym}(\tfrac12)\subseteq\operatorname{Sym}(1)\oplus\operatorname{Sym}(0),\qquad
\operatorname{Sym}(\tfrac12)\circ\operatorname{Sym}(0)\subseteq\operatorname{Sym}(\tfrac12),
$$

$$
\operatorname{Sym}(0)\circ\operatorname{Sym}(0)\subseteq\operatorname{Sym}(0).
$$

*Proof.* A block-diagonal matrix times a matrix with only the $B$ block has only the $B$ block, which gives the second and fourth rules. Two matrices with only the $B$ block multiply to a block-diagonal matrix, which gives the third rule. Two block-diagonal matrices multiply blockwise, which gives the first and fifth rules.

**The middle square is one dimension smaller than the direct sum.** From the second display,

$$
\operatorname{tr}(BB'^{\mathsf T})=\operatorname{tr}(B^{\mathsf T}B'),
$$

so the two diagonal blocks of $X_{1/2}\circ Y_{1/2}$ have equal trace. The image is therefore the block-diagonal matrices with matched traces, of dimension

$$
\frac{r(r+1)}{2}+\frac{(n-r)(n-r+1)}{2}-1,
$$

one less than $\operatorname{Sym}(1)\oplus\operatorname{Sym}(0)$.

**The Peirce grading is compatible with the product.** Since $X^{2}=X_{1}^{2}+2X_{1}\circ X_{1/2}+X_{1/2}^{2}+2X_{1/2}\circ X_{0}+X_{0}^{2}$ and the five summands lie in the spaces named by their subscripts, the algebra generated by $X$ is graded by the Peirce spaces.

## The Example $n=3$ with a Rank-One Idempotent

**At $n=3$ with $\operatorname{rk}E=1$ the dimensions are $1$, $2$ and $3$, and they add to $6$.**

$$
\frac{1\cdot2}{2}=1,\qquad 1\cdot2=2,\qquad \frac{2\cdot3}{2}=3,\qquad 1+2+3=6=\frac{3\cdot4}{2}.
$$

A rank-one projection in $\operatorname{Sym}_3$ fixes a line, its orthogonal plane, and the two-dimensional space of symmetric maps between them.

**In a basis adapted to $E$ the element reads as one entry, two entries and a symmetric $2\times2$ block.**

$$
E=\operatorname{diag}(1,0,0),\qquad
X_{1}=aE_{11},\qquad
X_{1/2}=b(E_{12}+E_{21})+c(E_{13}+E_{31}),\qquad
X_{0}=dE_{22}+e(E_{23}+E_{32})+fE_{33},
$$

with $a,b,c,d,e,f$ real: $1+2+3=6$ parameters, which is $\dim\operatorname{Sym}_3$.

**The middle square has dimension $3$ at $n=3$ and $r=1$.** The matched-trace condition cuts the direct sum of dimensions $1+3=4$ down to $3$, in agreement with the formula $1+3-1=3$.

## The Axioms in Coordinates

**The Peirce rules are the Jordan axioms written block by block.** Commutativity is the symmetry of each block product, the unit is $\mathrm{I}=E+(\mathrm{I}-E)$, and the Jordan identity is the identity of the two block products displayed above. The Peirce rules add the information that the three spaces are eigenspaces of a single operator, and that is what makes the coordinate description complete: the blocks multiply by the rules, and the associative product of the ambient algebra supplies the numbers.

**The trace form is the coordinate form of formal reality.** With

$$
\langle X,Y\rangle=\operatorname{tr}(XY),
$$

the three Peirce spaces are mutually orthogonal. For $X_{1}=EXE$ and $Y_{1/2}$ with $EY_{1/2}E=0$,

$$
\langle X_{1},Y_{1/2}\rangle=\operatorname{tr}(EXEY_{1/2})=\operatorname{tr}(XEY_{1/2}E)=0,
$$

and the same computation with $\mathrm{I}-E$ gives $\langle Y_{1/2},Z_{0}\rangle=0$, while $\langle X_{1},Z_{0}\rangle=0$ because $EZ_{0}=0$.

**The form is positive definite on each space.** On $\operatorname{Sym}(1)$ it is the trace form of $\operatorname{Sym}_r$, on $\operatorname{Sym}(1/2)$ it is $2\sum B_{ij}^{2}$, on $\operatorname{Sym}(0)$ it is the trace form of $\operatorname{Sym}_{n-r}$; each is positive definite, and the three inertias reproduce the three dimensions $r(r+1)/2$, $r(n-r)$ and $(n-r)(n-r+1)/2$.

**The automorphisms are the orthogonal conjugations.** A map $X\mapsto QXQ^{\mathsf T}$ with $Q\in\mathrm{O}(n)$ preserves the product, and every automorphism is of this form, because it preserves the unit and the cone of squares. So $\operatorname{Aut}(\operatorname{Sym}_n)=\mathrm{O}(n)$ and the derivations form $\mathfrak{so}(n)$, of dimension $n(n-1)/2$. A conjugation carries the Peirce spaces of $E$ to those of $QEQ^{\mathsf T}$, which is why the dimension formula depends on $E$ through $r$ alone.

## Summary

The symmetric matrices form a formally real Jordan algebra under $X\circ Y=\tfrac12(XY+YX)$, with unit $\mathrm{I}$ and automorphism group $\mathrm{O}(n)$. An idempotent of this algebra is an orthogonal projection $E$ of rank $r$, and it cuts the algebra into the three Peirce spaces $\operatorname{Sym}(1)=E\operatorname{Sym}_nE$, $\operatorname{Sym}(1/2)=\{X:EX+XE=X\}=\{X:EXE=0\}$ and $\operatorname{Sym}(0)=(\mathrm{I}-E)\operatorname{Sym}_n(\mathrm{I}-E)$, of dimensions $r(r+1)/2$, $r(n-r)$ and $(n-r)(n-r+1)/2$, which sum to $n(n+1)/2$. The five multiplication rules say that the first and third spaces are subalgebras, that the middle space is a bimodule over both, and that the square of the middle space lies in their direct sum, with image the block-diagonal matrices whose two blocks have equal trace. At $n=3$ with $r=1$ the dimensions are $1$, $2$ and $3$, summing to $6=3\cdot4/2$. The three spaces are mutually orthogonal for the positive definite trace form $\langle X,Y\rangle=\operatorname{tr}(XY)$, so the Peirce decomposition is an orthogonal decomposition of a space of dimension $n(n+1)/2$; this is the Jordan algebra of a formally real form, and its Peirce rules are its axioms in coordinates.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X\circ Y=\tfrac12(XY+YX)$ | The Jordan product on $\operatorname{Sym}_n$ |
| $E$ | An idempotent of the Jordan algebra, $E=E^{2}=E^{\mathsf T}$ |
| $r=\operatorname{rk}E$ | The rank of $E$, equal to $\operatorname{tr}E$ |
| $\operatorname{Sym}(1)=E\operatorname{Sym}_nE$ | The Peirce space of eigenvalue $1$ |
| $\operatorname{Sym}(\tfrac12)=\{X:EXE=0\}$ | The Peirce space of eigenvalue $\tfrac12$ |
| $\operatorname{Sym}(0)=(\mathrm{I}-E)\operatorname{Sym}_n(\mathrm{I}-E)$ | The Peirce space of eigenvalue $0$ |
| $A,B,C$ | The two diagonal blocks and the off-diagonal block |
| $\langle X,Y\rangle=\operatorname{tr}(XY)$ | The trace form on $\operatorname{Sym}_n$ |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for Peirce decompositions of Jordan algebras and their axioms.
- Pascual Jordan, John von Neumann and Eugene Wigner, *On an Algebraic Generalization of the Quantum Mechanical Formalism* (Annals of Mathematics 35, 1935), for the origin of the formally real Jordan algebras.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce corners of the associative algebra that the Jordan spaces refine.
- [The Peirce Basis and the Corners over $\mathbb{R}$](the-peirce-basis-and-the-corners-over-r.html), for the corners of $M_n(\mathbb{R})$ whose symmetric parts appear here.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the trace form and the split into symmetric and antisymmetric matrices.
- [The Peirce Decomposition and the Two Halves over $\mathbb{R}$](the-peirce-decomposition-and-the-two-halves-over-r.html), for the grading of the two halves by a frame.
