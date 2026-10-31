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

## Common Aspects

A Peirce decomposition with two primitive idempotents writes every biquaternion in four corners. In the entry model the four corner coordinates are the four entries of the matrix, and the four corner elements are the four matrix units. In the regular model the same four elements become rank-two matrices, and the corner matrix is duplicated. The duplication is the two spinor planes, and the entry model is the compression of the regular matrix to one of them.

**The Peirce table.** The four Peirce elements multiply as the four matrix units:

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
and the table is the matrix-unit table $E_{ij}E_{kl}=\delta_{jk}E_{il}$. The order $(\Pi_+,\Upsilon_+,\Upsilon_-,\Pi_-)$ puts the first column of the corner matrix in the first two coordinates and the second column in the last two: it is the order in which the two spinor planes are contiguous.

**The corner coordinates.** Every element has a unique expansion
$$
\tilde Q=a_{11}\tilde\Pi_++a_{12}\vec\Upsilon_-+a_{21}\vec\Upsilon_++a_{22}\tilde\Pi_-,
\qquad
\tilde Q\longmapsto B=\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix},
$$
an isomorphism of $\mathbb{C}$-algebras $\mathbb{B}\to M_2(\mathbb{C})$. The four coordinates are the trace pairings with the matrix units,
$$
a_{11}=\operatorname{Tr}(E_{11}B),\qquad
a_{12}=\operatorname{Tr}(E_{12}B),\qquad
a_{21}=\operatorname{Tr}(E_{21}B),\qquad
a_{22}=\operatorname{Tr}(E_{22}B),
$$
and in the regular model every coefficient is half the corresponding $4\times4$ trace:
$$
a_{ij}=\tfrac12\operatorname{Tr}_4\bigl((I_2\otimes E_{ij})\,M\bigr).
$$
With $B=\mathsf M_2(\tilde Q)$ the four entries are
$$
a_{11}=Q_t-iQ_z,\qquad
a_{12}=-iQ_x-Q_y,\qquad
a_{21}=-iQ_x+Q_y,\qquad
a_{22}=Q_t+iQ_z.
$$
The invariant is $\operatorname{Tr}_2B=2Q_t$, $\det B=\langle\tilde Q\rangle_{\natural}$, and in the regular model $\operatorname{Tr}_4M=4Q_t$, $\det M=\langle\tilde Q\rangle_{\natural}^2$: the trace is multiplied by the dimension of the multiplicity space and the determinant is squared.

**One system of matrix units.** A system of $2\times2$ matrix units is a family with $E_{ij}E_{kl}=\delta_{jk}E_{il}$ and $E_{11}+E_{22}=e_t$. The four Peirce elements satisfy these relations exactly. They are not a system of $4\times4$ units: in the regular model each goes to $I_2\otimes E_{ij}$, of rank two, and the four together span only four complex dimensions, while a system of $4\times4$ units has sixteen elements. The regular model carries one system of $2\times2$ units, duplicated.

**The reciprocal scaling.** The two mixed elements are normalised by $E_{12}E_{21}=E_{11}$. Replacing $E_{12}$ by $\mu E_{12}$ and $E_{21}$ by $\mu^{-1}E_{21}$ leaves every product unchanged. In the regular model the scaling acts on both blocks simultaneously, so the reciprocal $\mathbb{C}^{\times}$ is one scalar, not one scalar per block.

**The two planes.** The Peirce planes are
$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-,
$$
and in the Peirce basis they are the first two and the last two coordinates: $S_+\mapsto\{(x,y,0,0)\}$, $S_-\mapsto\{(0,0,z,w)\}$, $\mathbb{C}^4=S_+\oplus S_-$. The two diagonal blocks of the regular matrix are exactly these planes.

**The left and right actions.** Left multiplication by $\tilde P$ preserves each plane and acts on both by the same matrix:
$$
L_{\tilde P}|_{S_+}=L_{\tilde P}|_{S_-}=\mathsf M_2(\tilde P).
$$
Left multiplication never mixes the two planes; the two copies are the multiplicity of the regular representation, not two chiralities. Right multiplication by the mixed units swaps the planes,
$$
R_{\vec\Upsilon_-}=\begin{pmatrix}0&0\\ \mathrm I_2&0\end{pmatrix},
\qquad
R_{\vec\Upsilon_+}=\begin{pmatrix}0&\mathrm I_2\\0&0\end{pmatrix},
$$
and both blocks move together. The Peirce index is therefore: left multiplication preserves each block, right multiplication swaps them.

**The column-space caution.** The column space of $\mathsf M_4^L(\tilde\Pi_+)$ is not $S_+$. It is the image of left multiplication by $\tilde\Pi_+$,
$$
\tilde\Pi_+\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_-,
$$
the right Peirce row, and in the Peirce basis it is the first and third coordinates. A rank-two idempotent matrix projects onto the row generated by its idempotent, not onto the plane that the idempotent generates from the left. The two planes of this article are the two blocks, not the column spaces of the two idempotents.

**The nilpotents and the idempotents.** A nilpotent is a nonzero element of a mixed Peirce corner, so its image is $\mu\,I_2\otimes E_{12}$ or $\mu\,I_2\otimes E_{21}$ with $\mu\in\mathbb{C}^{\times}$: square-zero, traceless and of rank two. Every nilpotent is a nonzero scalar multiple of one of the two standard nilpotents, conjugated by an inner automorphism. Every nontrivial idempotent is a product of two nilpotents from opposite corners, rescaled so that $uw=\tilde\Pi$; the trivial idempotent $e_t$ is the exception, because a product equal to a unit has unit factors and a nilpotent is not a unit.

## The Coefficient Frame

**The coefficient display.** In the coefficient basis the regular matrix is
$$
M_{\mathrm{coef}}=C_{\Pi}\,(I_2\otimes B)\,C_{\Pi}^{-1}.
$$
The duplication is hidden there: the coefficient matrix is full, and the two blocks are visible only after the change $C_{\Pi}$. The coefficient frame is therefore the frame in which the corner structure is encoded in the entries rather than displayed in blocks.

**The coordinates in coefficient form.** The corner coordinates are the entries of $B$, but the coefficient matrix has entries that are sums of the four coefficients. The four corner elements in coefficient coordinates are the columns of $C_{\Pi}$; the first and last are the idempotents, the two middle are the nilpotents. The four coordinates $a_{ij}$ are recovered by the trace pairings $a_{ij}=\tfrac12\operatorname{Tr}_4((I_2\otimes E_{ij})M_{\mathrm{coef}})$, where $I_2\otimes E_{ij}=C_{\Pi}^{-1}(I_2\otimes E_{ij})C_{\Pi}$ is the coefficient matrix of the corner element.

**The exchange.** Right multiplication by the mixed units in the coefficient frame is the conjugate of the block swap, $C_{\Pi}R_{\vec\Upsilon_\pm}C_{\Pi}^{-1}$. It is not a simple permutation of the coefficient coordinates: the coefficient basis does not split the two planes. The block language is native to the Peirce frame, and the coefficient frame carries the same structure in dressed form.

## The Entry Model

**The corner matrix.** The entry model is the corner matrix itself,
$$
B=\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}
=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}.
$$
Its four entries are the four Peirce coordinates, and the four standard matrix units are the four Peirce elements. The trace is $2Q_t$ and the determinant is $\langle\tilde Q\rangle_{\natural}$.

**The matrix units and the planes.** The two columns of $B$ are the coordinates of $\tilde Q\tilde\Pi_+$ and $\tilde Q\vec\Upsilon_+$ in the basis $(\tilde\Pi_+,\vec\Upsilon_+)$; the two rows are the coordinates in the dual row basis. The left plane $S_+$ is the first two coordinates of the regular display, and the entry matrix is the action on that plane. The entry model is therefore the compression of the regular matrix to one spinor plane.

**The nilpotents.** The standard nilpotents are $E_{12}$ and $E_{21}$, of rank one and square-zero. Every nilpotent is a nonzero scalar multiple of one of them, conjugated by an inner automorphism of $M_2(\mathbb{C})$. Every nontrivial idempotent is a product of two of them, rescaled to $uw=E_{11}$.

## The Peirce Frame

**The duplicated corner matrix.** In the Peirce frame
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

**The rank-two units.** Each Peirce element goes to
$$
\mathsf M_4^L(\tilde\Pi_+)=I_2\otimes E_{11},
\quad
\mathsf M_4^L(\vec\Upsilon_+)=I_2\otimes E_{21},
\quad
\mathsf M_4^L(\vec\Upsilon_-)=I_2\otimes E_{12},
\quad
\mathsf M_4^L(\tilde\Pi_-)=I_2\otimes E_{22},
$$
of rank two, idempotent or square-zero, spanning four complex dimensions. The regular model carries one system of $2\times2$ units, duplicated; it does not carry the sixteen units of $M_4(\mathbb{C})$.

**The two planes and the actions.** The two blocks are $S_+$ and $S_-$. Left multiplication acts on each by the same $B$ and never mixes them; right multiplication by $\vec\Upsilon_-$ sends $S_+$ to $S_-$ and kills $S_-$, and right multiplication by $\vec\Upsilon_+$ does the reverse. The two maps are inverse on the planes. The column space of $I_2\otimes E_{11}$ is the right Peirce row, spanned by the first and third Peirce coordinates, not the left plane $S_+$; the two groupings of the four entries by columns and by rows are different, and the first column and the first row meet in $E_{11}$ and together span a three-dimensional space that is neither a left plane nor a right plane.

**The nilpotents.** The nilpotents are $\mu\,I_2\otimes E_{12}$ and $\mu\,I_2\otimes E_{21}$, of rank two, square-zero, traceless, and conjugate to the direct sum of two Jordan blocks, one in each spinor plane. The two standard nilpotents are conjugate to each other; the labels record the mixed corner, not a conjugacy class.

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