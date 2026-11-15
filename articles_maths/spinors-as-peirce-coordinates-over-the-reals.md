# __Spinors as Peirce Coordinates over the Reals__

## Introduction

**The off-diagonal Peirce coordinates of a real matrix are maps between the lines of a frame, and at $n=2$ those coordinates are a pair of real numbers that the transpose exchanges the way a spinor is exchanged with its conjugate.**

The article defines the Peirce coordinates of an element, reads the off-diagonal part as a family of real maps, treats the case $n=2$ in full, shows that the transpose exchanges the two chiralities and that the trace form pairs them, counts the dimensions at $n=2,3,4$, compares the real case with the complex one, and identifies the pure spinors with the rank-one matrices. It assumes *The Peirce Basis and the Corners over $\mathbb{R}$* for the frame and its corners, and it defers the symmetric reading of the coordinates to *The Peirce Decomposition and the Two Halves over $\mathbb{R}$*.

## The Peirce Coordinates of an Element

**Every real matrix is the sum of its corner components, and the components are its Peirce coordinates.** For a frame $P_{1},\dots,P_{n}$ with subspaces $V_{k}=\operatorname{im}P_{k}$ of ranks $r_{k}$,

$$
X=\sum_{k,l=1}^{n}X_{kl},\qquad X_{kl}=P_{k}XP_{l}\in A_{kl}=\operatorname{Hom}(V_{l},V_{k}).
$$

The coordinates are unique, because the corners are independent. The sum of the diagonal coordinates $X_{kk}$ is the part of $X$ that preserves each $V_{k}$, and the sum of the off-diagonal ones is the part that moves between them.

**The diagonal coordinates are square matrices and the off-diagonal ones are rectangular.** In a basis adapted to the frame, $X_{kk}$ is an $r_{k}\times r_{k}$ array and $X_{kl}$ is an $r_{k}\times r_{l}$ array. The off-diagonal coordinates are the maps $V_{l}\to V_{k}$, and that is what a spinor coordinate is here: a map between two lines of the frame, not a column of an ambient array.

**The coordinates multiply by the corner rule.**

$$
(XY)_{kl}=\sum_{m=1}^{n}X_{km}Y_{ml},
$$

so the algebra reads as an $n\times n$ array of blocks with the matrix product, as in *The Peirce Basis in $n$ Dimensions* for the complex case.

## The Off-Diagonal Coordinates as Maps

**The off-diagonal part of an element is a collection of real maps, one for each ordered pair of distinct lines.**

$$
X_{\text{off}}=\sum_{k\ne l}X_{kl},\qquad X_{kl}:V_{l}\longrightarrow V_{k}.
$$

For a complete frame each $V_{k}$ is a line, each $X_{kl}$ is a scalar multiple of a chosen unit, and the off-diagonal part is an $n\times n$ array with zero diagonal. That array is the spinor data of the element.

**The diagonal part is not spinor data.** It carries the endomorphisms of the lines, of dimension $\sum_{k}r_{k}^{2}$, and the spinorial content of the frame is the off-diagonal part, of real dimension

$$
\sum_{k\ne l}r_{k}r_{l}=n^{2}-\sum_{k}r_{k}^{2}.
$$

At a complete frame this is $n^{2}-n=n(n-1)$: two real dimensions for each unordered pair of lines.

**The diagonal corners form a subalgebra and the off-diagonal ones a bimodule over it.** A spinor is an element of that bimodule, and the frame is what makes the bimodule visible.

## The Case $n=2$

**At $n=2$ the off-diagonal corner is one-dimensional and the off-diagonal part is a pair of real numbers.**

$$
E=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
X=aE_{12}+bE_{21}=\begin{pmatrix}0&a\\ b&0\end{pmatrix},\qquad (a,b)\in\mathbb{R}^{2}.
$$

The pair $(a,b)$ is the **spinor** of $X$ in the frame: one real number for the map $V_{2}\to V_{1}$ and one for the map $V_{1}\to V_{2}$.

**The spinor determines the element and the element determines the spinor.** The diagonal part of $X$ is separate data, so the off-diagonal corner $A_{12}\oplus A_{21}$ is isomorphic to $\mathbb{R}^{2}$ as a real vector space, and the two numbers $a$ and $b$ are its coordinates.

**The square of the element is the product of the two components.**

$$
X^{2}=ab\,\mathrm{I},
$$

so the element is nilpotent exactly when $ab=0$, that is, when one of the two spinor components vanishes. For $a,b$ both nonzero the element has eigenvalues $\pm\sqrt{ab}$, which are real exactly when $ab>0$ and a conjugate pair when $ab<0$. The sign of the product is a real invariant of the spinor.

**The transpose swaps the two components.**

$$
X^{\mathsf T}=bE_{12}+aE_{21},
$$

so the transpose acts on the spinor by $(a,b)\mapsto(b,a)$. The symmetric elements are those with $a=b$ and the antisymmetric ones are those with $a=-b$; the symmetric part of $X$ is $\tfrac12(a+b)(E_{12}+E_{21})$ and the antisymmetric part is $\tfrac12(a-b)(E_{12}-E_{21})$. The two halves of the spinor space are the diagonal and the antidiagonal of the pair.

**The pairing between the two chiralities is the trace form.** With $X=aE_{12}+bE_{21}$ and $Y=a'E_{12}+b'E_{21}$,

$$
\langle X,Y\rangle=\operatorname{tr}(XY)=ab'+ba',
$$

because $\operatorname{tr}(E_{12}E_{21})=1$ and $\operatorname{tr}(E_{12}E_{12})=\operatorname{tr}(E_{21}E_{21})=0$. The form is symmetric, nondegenerate, and its matrix in the basis $E_{12},E_{21}$ is $\begin{pmatrix}0&1\\ 1&0\end{pmatrix}$, of signature $(1,1)$. It is the perfect pairing between the two one-dimensional spaces $A_{12}$ and $A_{21}$.

**The pairing is invariant and indefinite.** The space $A_{12}\oplus A_{21}$ has the invariant form $\operatorname{tr}(XY)$, of signature $(1,1)$, and the positive definite form $\operatorname{tr}(X^{\mathsf T}Y)$ is not invariant. So a real spinor pair comes with a symmetric indefinite pairing.

## The Two Chiralities

**The two off-diagonal corners are the two chiralities of the frame.** Write

$$
S^{+}=\bigoplus_{k<l}A_{kl},\qquad S^{-}=\bigoplus_{k<l}A_{lk}.
$$

An element of $S^{+}$ raises the index, an element of $S^{-}$ lowers it, and the off-diagonal part of every element splits as $X_{\text{off}}=X^{+}+X^{-}$ with $X^{+}\in S^{+}$ and $X^{-}\in S^{-}$.

**The transpose exchanges the two chiralities.** For a symmetric frame, $A_{kl}^{\mathsf T}=A_{lk}$, so

$$
(S^{+})^{\mathsf T}=S^{-},\qquad (S^{-})^{\mathsf T}=S^{+}.
$$

The transpose is $\mathbb{R}$-linear, so the exchange is an isomorphism of real vector spaces. The fixed points of the exchange are the symmetric off-diagonal elements and the anti-fixed points are the antisymmetric ones.

**The trace form pairs $S^{+}$ with $S^{-}$ and vanishes on each chirality separately.** For $X\in A_{kl}$ and $Y\in A_{pq}$ with $k\ne l$ and $p\ne q$, the trace $\operatorname{tr}(XY)$ is nonzero only when $l=p$ and $q=k$, that is, only when $Y$ lies in the corner $A_{lk}$ opposite to $X$. Hence

$$
\langle S^{+},S^{+}\rangle=0,\qquad \langle S^{-},S^{-}\rangle=0,\qquad \langle S^{+},S^{-}\rangle\ \text{nondegenerate}.
$$

This is the real form of the statement that the two spinor spaces are dual to each other.

**There is one real spinor space, not two.** The two chiralities are subspaces of the one real algebra $M_{n}(\mathbb{R})$, and the transpose moves one to the other. Nothing is added by naming them separately: a real spinor is an element of the off-diagonal part, and its two chiral components are read off from the corners.

## The Dimension Counts

**The off-diagonal part has dimension $n(n-1)$ at a complete frame.**

| $n$ | $S^{+}$ | $S^{-}$ | off-diagonal total | $\dim M_{n}(\mathbb{R})$ |
|---|---|---|---|---|
| $2$ | $1$ | $1$ | $2$ | $4$ |
| $3$ | $3$ | $3$ | $6$ | $9$ |
| $4$ | $6$ | $6$ | $12$ | $16$ |

At $n=2$ each chirality is a line, at $n=3$ each is a plane, and at $n=4$ each has six dimensions. The two chiralities always have equal dimension, $\tfrac12 n(n-1)$, and the two together with the $n$ diagonal coordinates rebuild the algebra:

$$
n+\frac{n(n-1)}{2}+\frac{n(n-1)}{2}=n^{2}.
$$

**At a coarse frame the counts change with the ranks.** The chirality $S^{+}$ has dimension $\sum_{k<l}r_{k}r_{l}$ and $S^{-}$ the same, while the diagonal part has dimension $\sum_{k}r_{k}^{2}$. For the rank vector $(2,1,1)$ at $n=4$ the three numbers are $5$, $5$ and $6$, which add to $16$.

**Each entry is the dimension of a real space.** Over $\mathbb{C}$ the corner $A_{kl}$ has complex dimension $r_{k}r_{l}$, the same number, so the passage to $\mathbb{C}$ doubles the real dimension of every corner and leaves the table unchanged.

## The Complex Case

**Over $\mathbb{C}$ the two chiralities are exchanged by the conjugate transpose.** For a Hermitian frame, with $P_{k}^{*}=P_{k}$, the conjugate transpose sends $A_{kl}$ to $A_{lk}$, and it is conjugate linear. The two spinor spaces are then complex conjugate spaces, and the pairing between them is Hermitian, not symmetric.

**Over $\mathbb{R}$ the exchanging map is linear and the pairing is symmetric.** The transpose sends $A_{kl}$ to $A_{lk}$ and satisfies $\operatorname{tr}(XY)=\operatorname{tr}(YX)$ with no conjugation. The bilinear form on $A_{12}\oplus A_{21}$ at $n=2$ is $\operatorname{tr}(XY)=ab'+ba'$, with signature $(1,1)$, and its matrix is symmetric with integer entries.

**The difference is the difference between a real and a Hermitian form.** A Hermitian form is conjugate linear in one argument and positive definite for the standard frame; the real form $\operatorname{tr}(XY)$ is bilinear and indefinite. So the real spinor of this article is a pair of real components with an indefinite pairing, and the complex spinor of *Spinors as Peirce Coordinates in $n$ Dimensions* is a pair of conjugate components with a Hermitian pairing.

## The Pure Spinors Are the Rank-One Elements

**A rank-one matrix has a spinor whose two chiral components factor through one vector on each side.** Let $X=uv^{\mathsf T}$ with $u,v\in\mathbb{R}^{n}$ nonzero. Then

$$
X_{kl}=P_{k}uv^{\mathsf T}P_{l}=(P_{k}u)(P_{l}^{\mathsf T}v)^{\mathsf T},
$$

so each corner component of $X$ is the rank-one map $(P_{l}^{\mathsf T}v)\mapsto P_{k}u$ followed by a scalar, and the whole off-diagonal part is determined by the two vectors $P_{k}u$ and $P_{l}^{\mathsf T}v$ together with the frame.

**Conversely, a spinor whose components factor through one vector on each side is rank one.** If $X^{+}$ is built from a single vector $u$ and $X^{-}$ from a single vector $v$ in the sense of the display, then $X=uv^{\mathsf T}$ has rank one. So the **pure spinors** are the rank-one matrices, read in the frame.

**The rank of a random rank-one matrix is one.** Ten random real $3\times 3$ matrices of the form $uv^{\mathsf T}$, with $u$ and $v$ with independent Gaussian entries, all have rank exactly $1$, as computed with numpy. A rank-one matrix is nilpotent exactly when $v^{\mathsf T}u=0$, which is the spinor condition at $n=2$ written in general.

**At $n=2$ the pure spinors are the pairs with exactly one nonzero component.** With $X=aE_{12}+bE_{21}$ the rank is $2$ when $ab\ne0$ and $1$ when $ab=0$; the trace is zero in both cases. So the pure spinors of the frame are the two coordinate axes of $\mathbb{R}^{2}$, and the general spinor is a sum of two pure ones. This is the real form of the statement that a spinor is a sum of decomposable pieces.

## Summary

For a real frame with subspaces $V_{k}$ of ranks $r_{k}$, every matrix splits into Peirce coordinates $X=\sum_{k,l}X_{kl}$ with $X_{kl}:V_{l}\to V_{k}$ of dimension $r_{k}r_{l}$. The off-diagonal coordinates are the spinor data: at a complete frame they form two blocks of dimension $n(n-1)/2$ each, one raising the index and one lowering it, and at $n=2$ they are a single pair $(a,b)\in\mathbb{R}^{2}$ with $X=aE_{12}+bE_{21}$ and $X^{2}=ab\,\mathrm{I}$. The transpose exchanges the two blocks, so the symmetric and antisymmetric parts of the pair are its diagonal and antidiagonal; the trace form pairs the blocks perfectly, with $\operatorname{tr}(E_{12}E_{21})=1$ and matrix $\begin{pmatrix}0&1\\ 1&0\end{pmatrix}$ of signature $(1,1)$ on the pair at $n=2$. The off-diagonal dimension is $2$ at $n=2$, $6$ at $n=3$ and $12$ at $n=4$, and the diagonal part of dimension $n$ completes the algebra. Over $\mathbb{C}$ with a Hermitian frame the two blocks are exchanged by a conjugate-linear map, while over $\mathbb{R}$ they are exchanged by the linear transpose and paired by a symmetric indefinite form. The pure spinors are the rank-one matrices, and a random rank-one real matrix has rank one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_{k}$, $V_{k}=\operatorname{im}P_{k}$ | The frame and the line of its $k$-th idempotent |
| $r_{k}=\operatorname{rk}P_{k}$ | The rank, with $\sum_{k}r_{k}=n$ |
| $X_{kl}=P_{k}XP_{l}$ | The Peirce coordinate in the corner $A_{kl}$ |
| $S^{+}=\bigoplus_{k<l}A_{kl}$ | The raising chirality |
| $S^{-}=\bigoplus_{k<l}A_{lk}$ | The lowering chirality |
| $(a,b)$ | The spinor of $aE_{12}+bE_{21}$ at $n=2$ |
| $\langle X,Y\rangle=\operatorname{tr}(XY)$ | The pairing between the chiralities |
| $uv^{\mathsf T}$ | A pure spinor, a rank-one matrix |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for Peirce coordinates and the corner decomposition of an algebra as an array of maps.
- Elie Cartan, *The Theory of Spinors* (Hermann, 1966), for the classical construction of spinors as coordinates relative to a maximal isotropic family.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for rank-one matrices, the trace form and its signature.
- [The Peirce Basis and the Corners over $\mathbb{R}$](the-peirce-basis-and-the-corners-over-r.html), for the corners and the frame that the coordinates use.
- [Spinors as Peirce Coordinates in $n$ Dimensions](spinors-as-peirce-coordinates-in-n-dimensions.html), for the complex version of the same reading.
- [The Peirce Decomposition and the Two Halves over $\mathbb{R}$](the-peirce-decomposition-and-the-two-halves-over-r.html), for the transpose, the two halves and the corner pair.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the trace form and the indefinite pairing.
