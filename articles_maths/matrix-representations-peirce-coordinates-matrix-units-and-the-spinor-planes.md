# __Matrix Representations : Peirce Coordinates, Matrix Units and the Spinor Planes__

## Introduction

A Peirce decomposition with two primitive idempotents writes every biquaternion in four corners. In the $2\times2$ model the four corner coordinates are the four entries of the matrix, and the four corner elements are the four matrix units. In the $4\times4$ regular model the same four elements become rank-two matrices, and the corner matrix is duplicated: the regular matrix is $\operatorname{diag}(B,B)$ in the Peirce frame. The duplication is the two spinor planes, and the $2\times2$ model is the compression of the regular matrix to one of them.

This article develops the Peirce table, the corner coordinates, the regular matrix as the duplicated corner matrix, the system of matrix units, the two spinor planes, the left and right actions, the column spaces of the idempotents and the nilpotents. It uses no form and no module; the only invariant it reads is the determinant of the corner matrix.

**Conventions.** The algebra and the models are those of *Matrix Representations : The Models and the Change of Frame*. The standard pair and the standard nilpotents are
$$
\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z),
\qquad
\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y),
$$
with $\vec\Upsilon_+=\vec\Upsilon_{+-}$ and $\vec\Upsilon_-=\vec\Upsilon_{-+}$ in the generic labelling. The Peirce basis is ordered
$$
\mathcal P=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)
=(E_{11},E_{21},E_{12},E_{22}),
$$
the order that makes the two spinor planes contiguous. In this frame
$$
\mathsf M_4^L(\tilde Q)=\operatorname{diag}\bigl(\mathsf M_2(\tilde Q),\mathsf M_2(\tilde Q)\bigr)
=I_2\otimes\mathsf M_2(\tilde Q).
$$
The coefficient basis is the conjugate display, related by the Peirce change $C_{\Pi}$.

**Boundaries.** The abstract Peirce decomposition is *The Peirce Decomposition of the Biquaternion Algebra*; the planes and the exchange are *Spinors as Peirce Coordinates in the Biquaternion Algebra*; the right regular matrix is *Matrix Representations : The Centraliser and the Double Centraliser*; the diagonalising matrix is *Matrix Representations : The Eigenbasis and the Diagonalising Matrix*.

## The Peirce Table

**The four Peirce elements multiply as the four matrix units.**

| Product | Value | Product | Value |
|---|---|---|---|
| $\tilde\Pi_+^2$ | $\tilde\Pi_+$ | $\tilde\Pi_-^2$ | $\tilde\Pi_-$ |
| $\tilde\Pi_+\tilde\Pi_-$ | $0$ | $\vec\Upsilon_+^2$, $\vec\Upsilon_-^2$ | $0$ |
| $\vec\Upsilon_-\vec\Upsilon_+$ | $\tilde\Pi_+$ | $\vec\Upsilon_+\vec\Upsilon_-$ | $\tilde\Pi_-$ |
| $\tilde\Pi_+\vec\Upsilon_-=\vec\Upsilon_-\tilde\Pi_-$ | $\vec\Upsilon_-$ | $\tilde\Pi_-\vec\Upsilon_+=\vec\Upsilon_+\tilde\Pi_+$ | $\vec\Upsilon_+$ |

The correspondence is
$$
\tilde\Pi_+\longmapsto E_{11},\qquad
\vec\Upsilon_+\longmapsto E_{21},\qquad
\vec\Upsilon_-\longmapsto E_{12},\qquad
\tilde\Pi_-\longmapsto E_{22},
$$
and the table is the matrix-unit table $E_{ij}E_{kl}=\delta_{jk}E_{il}$.

**The order.** The two idempotents are the two diagonal units, and the two nilpotents are the two off-diagonal units. The order $(\Pi_+,\Upsilon_+,\Upsilon_-,\Pi_-)$ puts the first column of the corner matrix in the first two coordinates and the second column in the last two: it is the order in which the two spinor planes are contiguous.

## The Corner Coordinates

**The expansion.** Every element has a unique expansion
$$
\tilde Q=a_{11}\tilde\Pi_++a_{12}\vec\Upsilon_-+a_{21}\vec\Upsilon_++a_{22}\tilde\Pi_-,
$$
and the map
$$
\tilde Q\longmapsto B=\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}
$$
is an isomorphism of $\mathbb{C}$-algebras $\mathbb{B}\to M_2(\mathbb{C})$. It is the fixed model $\mathsf M_2$.

**The recovery.** The four coordinates are the trace pairings with the four matrix units:
$$
a_{11}=\operatorname{Tr}(E_{11}B),\qquad
a_{12}=\operatorname{Tr}(E_{12}B),\qquad
a_{21}=\operatorname{Tr}(E_{21}B),\qquad
a_{22}=\operatorname{Tr}(E_{22}B).
$$
In the regular model each block carries one copy, so every coefficient is half the corresponding $4\times4$ trace:
$$
a_{ij}=\tfrac12\operatorname{Tr}_4\bigl((I_2\otimes E_{ij})\,M\bigr).
$$

**The coefficient form.** With $B=\mathsf M_2(\tilde Q)$, the four entries are
$$
a_{11}=Q_t-iQ_z,\qquad
a_{12}=-iQ_x-Q_y,\qquad
a_{21}=-iQ_x+Q_y,\qquad
a_{22}=Q_t+iQ_z.
$$
The two invariants are
$$
\operatorname{Tr}_2B=2Q_t,
\qquad
\det B=Q_t^2+B^2=\langle\tilde Q\rangle_{\natural},
$$
and in the regular model
$$
\operatorname{Tr}_4M=2\operatorname{Tr}_2B=4Q_t,
\qquad
\det M=(\det B)^2=\langle\tilde Q\rangle_{\natural}^2.
$$
The trace is the trace of the corner matrix multiplied by the dimension of the multiplicity space, and the determinant is its determinant squared.

## The Regular Matrix as the Duplicated Corner Matrix

**The block form.** In the Peirce frame
$$
M=\mathsf M_4^L(\tilde Q)=
\begin{pmatrix}
a_{11}&a_{12}&0&0\\
a_{21}&a_{22}&0&0\\
0&0&a_{11}&a_{12}\\
0&0&a_{21}&a_{22}
\end{pmatrix}
=\operatorname{diag}(B,B).
$$
The two blocks are identical. The duplication is the regular representation: every element acts on the algebra by left multiplication, and the algebra is the direct sum of two copies of the same module.

**The coefficient frame.** In the coefficient basis the same matrix is
$$
M_{\mathrm{coef}}=C_{\Pi}\,(I_2\otimes B)\,C_{\Pi}^{-1}.
$$
The duplication is hidden there: the coefficient matrix is full, and the two blocks are visible only after the change $C_{\Pi}$.

**The isomorphism.** The map $\tilde Q\mapsto B$ is the algebra isomorphism; the map $\tilde Q\mapsto I_2\otimes B$ is the regular representation. The first is one copy of the corner matrix, the second is two copies. The two agree on the corner table because the table is the table of matrix units.

## One System of Matrix Units

**The four Peirce elements are one system of $2\times2$ matrix units.** A system of $2\times2$ matrix units is a family $\{E_{ij}\}$ with $E_{ij}E_{kl}=\delta_{jk}E_{il}$ and $E_{11}+E_{22}=e_t$. The four Peirce elements satisfy these relations exactly.

**They are not a system of $4\times4$ units.** In the regular model each Peirce element goes to the rank-two matrix
$$
\mathsf M_4^L(\tilde\Pi_+)=I_2\otimes E_{11},
\quad
\mathsf M_4^L(\vec\Upsilon_+)=I_2\otimes E_{21},
\quad
\mathsf M_4^L(\vec\Upsilon_-)=I_2\otimes E_{12},
\quad
\mathsf M_4^L(\tilde\Pi_-)=I_2\otimes E_{22}.
$$
Each has rank two, each is an idempotent or a square-zero element, and the four together span only four complex dimensions. A system of $4\times4$ matrix units would have sixteen elements, and the image of $\mathbb{B}$ has dimension four. The regular model carries one system of $2\times2$ units, duplicated; it does not carry the sixteen units of $M_4(\mathbb{C})$.

**The reciprocal scaling.** The two mixed elements are normalised by $E_{12}E_{21}=E_{11}$. Replacing $E_{12}$ by $\mu E_{12}$ and $E_{21}$ by $\mu^{-1}E_{21}$ leaves every product of the system unchanged. In the regular model the scaling is diagonal in each block and acts on the two blocks simultaneously:
$$
I_2\otimes E_{12}\longmapsto \mu\,I_2\otimes E_{12},
\qquad
I_2\otimes E_{21}\longmapsto \mu^{-1}\,I_2\otimes E_{21}.
$$
The reciprocal $\mathbb{C}^{\times}$ of the system is therefore one scalar, not one scalar per block.

## The Two Spinor Planes

**The planes.** The two Peirce planes are
$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-,
$$
and in the Peirce basis they are the first two and the last two coordinates:
$$
S_+\longmapsto\{(x,y,0,0)\},
\qquad
S_-\longmapsto\{(0,0,z,w)\},
\qquad
\mathbb{C}^4=S_+\oplus S_-.
$$
The two diagonal blocks of the regular matrix are exactly these planes.

**The left action.** Left multiplication by $\tilde P$ preserves each plane and acts on both by the same matrix:
$$
L_{\tilde P}|_{S_+}=L_{\tilde P}|_{S_-}=\mathsf M_2(\tilde P).
$$
Left multiplication never mixes the two planes. The two copies are the multiplicity of the regular representation, not two chiralities.

**The compression.** The $2\times2$ model is the regular matrix compressed to one plane. On $S_+$ with the basis $(\tilde\Pi_+,\vec\Upsilon_+)$, the matrix of left multiplication by $\tilde Q$ is $B$; the two columns of $B$ are the coordinates of $\tilde Q\tilde\Pi_+$ and $\tilde Q\vec\Upsilon_+$ in that basis. The $2\times2$ display therefore carries the action on one spinor plane, and the regular display carries the action on both. This is the compression statement of *Matrix Representations : The Models and the Change of Frame*, read in the Peirce frame.

**The invariance.** Each plane is a left ideal, so it is invariant under left multiplication by every element. The two planes are not the two eigenspaces of a general element; they are the two Peirce components, and the spectral eigenspaces are different planes unless the element points along the standard axis.

**The star.** The star carries a spinor plane to a right Peirce row, not to the other plane. The standard idempotents are Hermitian, so
$$
S_+^{*}=\tilde\Pi_+\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_-,
$$
which is the right Peirce row of $\tilde\Pi_+$, not $S_-$. The two planes are exchanged by right multiplication, not by the star.

## Left and Right Multiplication

**Right multiplication by the mixed units.** In the Peirce frame,
$$
R_{\vec\Upsilon_-}=\begin{pmatrix}0&0\\ \mathrm I_2&0\end{pmatrix},
\qquad
R_{\vec\Upsilon_+}=\begin{pmatrix}0&\mathrm I_2\\0&0\end{pmatrix}.
$$
Hence $\xi\vec\Upsilon_-$ lies in $S_-$ for every $\xi\in S_+$, and $S_-\vec\Upsilon_-=0$; right multiplication by $\vec\Upsilon_+$ does the reverse. The two maps are inverse on the planes, and both blocks move together: the exchange is a single right multiplication, not a pair of independent maps on the two copies.

**The Peirce index.** Left multiplication preserves each block; right multiplication swaps them. The two blocks are the two Peirce copies, and the only operation of the algebra that relates them is multiplication on the right by a mixed unit. This is the matrix form of the fact that the algebra is a bimodule over itself, with the left action diagonal and the right action exchanging the two copies.

## The Column Space of the Idempotent

**A caution.** The column space of $\mathsf M_4^L(\tilde\Pi_+)$ is not $S_+$. It is the image of left multiplication by $\tilde\Pi_+$, which is
$$
\tilde\Pi_+\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_-,
$$
the right Peirce row, and in the Peirce basis it is the first and third coordinates. A rank-two idempotent matrix projects onto the row generated by its idempotent, not onto the plane that the idempotent generates from the left. The two planes of this article are the two blocks, not the column spaces of the two idempotents.

**The two groupings.** The four entries are grouped by columns and by rows. The columns give the two left planes $S_\pm=\mathbb{B}\tilde\Pi_\pm$; the rows give the two right Peirce rows $\tilde\Pi_\pm\mathbb{B}$. The same four entries carry both groupings, and the groupings differ: the first column and the first row meet in $E_{11}$, and together they span a three-dimensional space that is neither one of the two left planes nor one of the two right planes.

## The Nilpotents

**The off-diagonal units.** A nilpotent of $\mathbb{B}$ is a nonzero element of a mixed Peirce corner, so its image under $\mathsf M_4^L$ is a nonzero element of the image of $\mathbb{C}E_{12}$ or $\mathbb{C}E_{21}$ in the block form. Such an element is $\mu\,I_2\otimes E_{12}$ or $\mu\,I_2\otimes E_{21}$ with $\mu\in\mathbb{C}^{\times}$. Its square is zero, its trace is zero and its rank is two.

**The conjugacy.** Every nilpotent is a nonzero scalar multiple of one of the two standard nilpotents, conjugated by an inner automorphism of the algebra. The scalar is the coordinate of the nilpotent in its corner, and the conjugacy is the change of the Peirce frame. In the regular model the conjugacy is the block-diagonal conjugation by the two copies of the same unit.

**The Jordan form.** A nonzero nilpotent of the regular image is conjugate to the direct sum of two Jordan blocks $\begin{pmatrix}0&1\\0&0\end{pmatrix}$, one in each spinor plane. The two standard nilpotents are conjugate to each other; the labels record the mixed corner, not a conjugacy class.

**The idempotents.** Every nontrivial idempotent of $\mathbb{B}$ is a product of two nilpotents. The two mixed corners of an idempotent and its complement are square-zero, and a nonzero pair $u,w$ from opposite corners can be rescaled to $uw=\tilde\Pi$. The trivial idempotent $e_t$ is the exception, because a product equal to a unit has unit factors and a nilpotent is not a unit.

## Summary

The four Peirce elements are one system of $2\times2$ matrix units; in the regular model they become the rank-two matrices $I_2\otimes E_{ij}$, and the corner matrix is duplicated: $\mathsf M_4^L(\tilde Q)=\operatorname{diag}(B,B)$ in the frame $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$. The two blocks are the two spinor planes, left multiplication acts on each by the same matrix and never mixes them, right multiplication by the mixed units swaps them, and the two planes are not the column spaces of the idempotents. The $2\times2$ model is the compression of the regular matrix to one plane. The four Peirce elements are not a system of $4\times4$ units.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal P=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ | the Peirce basis, ordered by contiguous planes |
| $C_{\Pi}$ | the Peirce change, columns the four Peirce elements |
| $a_{ij}$ | the four corner coordinates |
| $B=\mathsf M_2(\tilde Q)$ | the corner matrix |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the two spinor planes, the two blocks |
| $R_{\vec\Upsilon_\pm}$ | right multiplication by the mixed units, the block swaps |
| $I_2\otimes E_{ij}$ | the regular image of the Peirce element |
| $\langle\tilde Q\rangle_{\natural}$ | the central scalar $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ |

## Further Reading

- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the models, the Peirce change and the compression
- [Matrix Representations : The Product, the Trace and the Determinant](matrix-representations-the-product-the-trace-and-the-determinant.html), for the regular matrix and the Peirce frame
- *Matrix Representations : The Centraliser and the Double Centraliser*, for the right regular matrix
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the corners and the table
- [Spinors as Peirce Coordinates in the Biquaternion Algebra](spinors-as-peirce-coordinates-in-the-biquaternion-algebra.html), for the planes and the exchange
- [Nilpotents](nilpotents.html), for the nilpotent cone
- [Matrix Representations : Peirce Coordinates, Matrix Units and the Spinor Planes](matrix-representations-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the $2\times2$ source
- [Matrix Representations : Peirce Coordinates, Matrix Units and the Spinor Planes](matrix-representations-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the $4\times4$ source
