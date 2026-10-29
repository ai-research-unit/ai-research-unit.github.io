# __$M_4(\mathbb{C})_L$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes__

## Introduction

The left regular matrix reads a biquaternion as an operator on its own four-dimensional complex space. It is an injective algebra map whose image is a four-dimensional subalgebra of $M_4(\mathbb{C})$. In the Peirce basis the image is block diagonal with two identical $2\times2$ blocks, and the two blocks are the two spinor planes.

This article develops the Peirce table, the coordinate isomorphism, the systems of matrix units, the two planes and the left and right actions in the $4\times4$ model. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*. It uses no form, no norm and no module.

**Conventions.** The algebra, the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and the left regular matrix $\mathsf M_4$ are those of *$M_4(\mathbb{C})_L$ Representation : The Matrix Product and the Algebra Structure*: the $\mu$-th column of $\mathsf M_4(\tilde Q)$ is the coordinate column of $\tilde Q e_\mu$. The standard pair and the standard nilpotents are

$$
\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z),\qquad
\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y),\qquad
\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y),
$$

with $\vec\Upsilon_x=\vec\Upsilon_-$ and $\vec\Upsilon_y=\vec\Upsilon_+$ in the generic labelling of *Spinors as Peirce Coordinates in the Biquaternion Algebra*. The $2\times2$ model is

$$
\mathsf M_2(\tilde Q)=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}.
$$

The Peirce basis is ordered

$$
\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_y,\vec\Upsilon_x,\tilde\Pi_-)
=(E_{11},E_{21},E_{12},E_{22}),
$$

which is the order that makes the two spinor planes contiguous. The change of basis $\mathsf S$ with these four coordinate columns satisfies

$$
\mathsf S^{-1}\mathsf M_4(\tilde Q)\mathsf S
=\begin{pmatrix}\mathsf M_2(\tilde Q)&0\\0&\mathsf M_2(\tilde Q)\end{pmatrix}.
$$

**Boundaries.** The abstract Peirce decomposition is *The Peirce Decomposition of the Biquaternion Algebra*; the two planes and the exchange are *Spinors as Peirce Coordinates in the Biquaternion Algebra*; the $2\times2$ picture is *$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*; the right regular matrix is *$M_4(\mathbb{C})_L$ Representation : The Centraliser and the Double Centraliser*. The module reading is *The Minimal Left Ideals* and is not used here.

## The Peirce Table

**The four Peirce elements multiply as the four matrix units, and the table is the same table as in the $2\times2$ model.**

| Product | Value | Product | Value |
|---|---|---|---|
| $\tilde\Pi_+^2$ | $\tilde\Pi_+$ | $\tilde\Pi_-^2$ | $\tilde\Pi_-$ |
| $\tilde\Pi_+\tilde\Pi_-$ | $0$ | $\vec\Upsilon_+^2$, $\vec\Upsilon_-^2$ | $0$ |
| $\vec\Upsilon_-\vec\Upsilon_+$ | $\tilde\Pi_+$ | $\vec\Upsilon_+\vec\Upsilon_-$ | $\tilde\Pi_-$ |
| $\tilde\Pi_+\vec\Upsilon_-=\vec\Upsilon_-\tilde\Pi_-$ | $\vec\Upsilon_-$ | $\tilde\Pi_-\vec\Upsilon_+=\vec\Upsilon_+\tilde\Pi_+$ | $\vec\Upsilon_+$ |

The correspondence is

$$
\tilde\Pi_+\longmapsto E_{11},\qquad
\vec\Upsilon_-\longmapsto E_{12},\qquad
\vec\Upsilon_+\longmapsto E_{21},\qquad
\tilde\Pi_-\longmapsto E_{22},
$$

and the table is the matrix-unit table $E_{ij}E_{kl}=\delta_{jk}E_{il}$.

## The Coordinate Isomorphism

**The four Peirce elements go to four rank-two matrices, each duplicated in the two blocks.**

$$
\mathsf M_4(\tilde\Pi_+)=
\begin{pmatrix}
\tfrac12&0&0&-\tfrac i2\\
0&\tfrac12&-\tfrac i2&0\\
0&\tfrac i2&\tfrac12&0\\
\tfrac i2&0&0&\tfrac12
\end{pmatrix},
\qquad
\mathsf M_4(\vec\Upsilon_+)=
\begin{pmatrix}
0&-\tfrac i2&-\tfrac12&0\\
\tfrac i2&0&0&\tfrac12\\
\tfrac12&0&0&-\tfrac i2\\
0&-\tfrac12&\tfrac i2&0
\end{pmatrix},
$$

$$
\mathsf M_4(\vec\Upsilon_-)=
\begin{pmatrix}
0&-\tfrac i2&\tfrac12&0\\
\tfrac i2&0&0&-\tfrac12\\
-\tfrac12&0&0&-\tfrac i2\\
0&\tfrac12&\tfrac i2&0
\end{pmatrix},
\qquad
\mathsf M_4(\tilde\Pi_-)=
\begin{pmatrix}
\tfrac12&0&0&\tfrac i2\\
0&\tfrac12&\tfrac i2&0\\
0&-\tfrac i2&\tfrac12&0\\
-\tfrac i2&0&0&\tfrac12
\end{pmatrix}.
$$

Each has rank two, each is an idempotent or a square-zero element, and each satisfies

$$
\mathsf S^{-1}\mathsf M_4(\tilde\Pi_+)\mathsf S=\operatorname{diag}(E_{11},E_{11}),
\qquad
\mathsf S^{-1}\mathsf M_4(\tilde\Pi_-)\mathsf S=\operatorname{diag}(E_{22},E_{22}),
$$

$$
\mathsf S^{-1}\mathsf M_4(\vec\Upsilon_-)\mathsf S=\operatorname{diag}(E_{12},E_{12}),
\qquad
\mathsf S^{-1}\mathsf M_4(\vec\Upsilon_+)\mathsf S=\operatorname{diag}(E_{21},E_{21}).
$$

**Proposition.** Every element has a unique expansion

$$
\tilde Q=a_{11}\tilde\Pi_++a_{12}\vec\Upsilon_-+a_{21}\vec\Upsilon_++a_{22}\tilde\Pi_-,
$$

and the map $\tilde Q\mapsto\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}$ is an isomorphism $\mathbb{B}\to M_2(\mathbb{C})$. The left regular matrix is its inflation,

$$
\mathsf M_4(\tilde Q)=\mathsf S\bigl(\operatorname{diag}(\mathsf M_2(\tilde Q),\mathsf M_2(\tilde Q))\bigr)\mathsf S^{-1}.
$$

*Proof.* The Peirce basis is a basis, so the expansion is unique and the map is a linear bijection. It is multiplicative because the images of the four basis elements are the four matrix units. The second statement follows by applying the first to each basis element and extending by linearity; it is the explicit form of the block theorem of §*The Two Spinor Planes in the Regular Model*.

**The corner coordinates.** The four coefficients are recovered by the trace pairing of the $2\times2$ model,

$$
a_{11}=\operatorname{Tr}\bigl(\mathsf M_2(\tilde\Pi_+)\mathsf M_2(\tilde Q)\bigr),\qquad
a_{12}=\operatorname{Tr}\bigl(\mathsf M_2(\vec\Upsilon_+)\mathsf M_2(\tilde Q)\bigr),
$$

$$
a_{21}=\operatorname{Tr}\bigl(\mathsf M_2(\vec\Upsilon_-)\mathsf M_2(\tilde Q)\bigr),\qquad
a_{22}=\operatorname{Tr}\bigl(\mathsf M_2(\tilde\Pi_-)\mathsf M_2(\tilde Q)\bigr),
$$

with the two nilpotents exchanged because $\operatorname{Tr}(\mathsf M_2(\vec\Upsilon_-)\mathsf M_2(\vec\Upsilon_+))=\operatorname{Tr}(\mathsf M_2(\vec\Upsilon_+)\mathsf M_2(\vec\Upsilon_-))=1$. The pairing is the trace pairing of the $2\times2$ model, not a form and not a norm. In the regular model each block carries one copy, so every coefficient is half the corresponding $4\times4$ trace.

## The Coordinates in the Coefficients

The corner coordinates of the standard pair are the entries of the fixed $2\times2$ model,

$$
a_{11}=Q_t-iQ_z,\qquad
a_{12}=-iQ_x-Q_y,\qquad
a_{21}=-iQ_x+Q_y,\qquad
a_{22}=Q_t+iQ_z,
$$

so that

$$
\mathsf M_4(\tilde Q)=\mathsf S
\begin{pmatrix}
a_{11}&a_{12}&0&0\\
a_{21}&a_{22}&0&0\\
0&0&a_{11}&a_{12}\\
0&0&a_{21}&a_{22}
\end{pmatrix}\mathsf S^{-1}.
$$

The two invariants are

$$
\operatorname{Tr}\mathsf M_4(\tilde Q)=2(a_{11}+a_{22})=4Q_t,
\qquad
\det\mathsf M_4(\tilde Q)=(a_{11}a_{22}-a_{12}a_{21})^2=\langle\tilde Q\rangle_{\natural}^2 .
$$

The trace is the trace of the $2\times2$ model multiplied by the dimension of the multiplicity space, and the determinant is its determinant squared. The four differences are

$$
a_{11}-a_{22}=-2iQ_z,\qquad
a_{12}+a_{21}=-2iQ_x,\qquad
a_{12}-a_{21}=-2Q_y,
$$

so the four corner coordinates and the four coefficients carry the same information.

## Systems of Matrix Units

**The four Peirce elements are a system of $2\times2$ matrix units inside a four-dimensional algebra; they are not a system of $4\times4$ matrix units, and the regular model shows why.**

A system of $2\times2$ matrix units is a family $\{E_{ij}\}$ with $E_{ij}E_{kl}=\delta_{jk}E_{il}$ and $E_{11}+E_{22}=e_t$. The four Peirce elements satisfy the relations of §*Systems of Matrix Units* of *$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*. In the regular model each of them goes to a rank-two matrix, because the regular representation doubles every element: the image of $E_{ij}$ is $E_{ij}\otimes\mathrm I_2$, the block matrix with $E_{ij}$ in each diagonal block.

This is not a system of $4\times4$ matrix units. Such a system would have sixteen elements, and the image of $\mathbb{B}$ has dimension four. The regular model carries one system of $2\times2$ units, duplicated; it does not carry the sixteen units of $M_4(\mathbb{C})$.

**The reciprocal scaling.** The two mixed elements are normalised by $E_{12}E_{21}=E_{11}$. Replacing $E_{12}$ by $\mu E_{12}$ and $E_{21}$ by $\mu^{-1}E_{21}$ leaves every product of the system unchanged, so the regular system carries the same reciprocal $\mathbb{C}^{\times}$ as the $2\times2$ system. In the regular model the scaling is diagonal in each block and acts on the two blocks simultaneously.

## The Two Spinor Planes in the Regular Model

**The Peirce basis splits the space into two coordinate planes, and the left regular matrix is block diagonal on them.**

The two planes are

$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+
=\{x\tilde\Pi_++y\vec\Upsilon_+\},
\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-
=\{z\vec\Upsilon_-+w\tilde\Pi_-\},
$$

and in the Peirce basis they are the first two and the last two coordinates,

$$
S_+\longmapsto\{(x,y,0,0)\},\qquad
S_-\longmapsto\{(0,0,z,w)\},
$$

with $\mathbb{C}^4=S_+\oplus S_-$. The two blocks of the block form are exactly these planes.

**Left multiplication.** By the block form, $\mathsf M_4(\tilde P)$ preserves each plane and acts on both by the same matrix:

$$
L_{\tilde P}|_{S_+}=L_{\tilde P}|_{S_-}=\mathsf M_2(\tilde P).
$$

This is the matrix form of the proposition of *$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*, §*The Left Action on a Couple*. The two copies are the two chiralities, and left multiplication never mixes them.

**A caution about the projector.** The column space of $\mathsf M_4(\tilde\Pi_+)$ is not $S_+$. It is the image of left multiplication by $\tilde\Pi_+$, which is $\tilde\Pi_+\mathbb{B}$, the right Peirce row $\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_-$; in the Peirce basis it is the first and third coordinates. A rank-two idempotent matrix projects onto the row generated by its idempotent, not onto the plane that the idempotent generates from the left. The two planes of this section are the two blocks, not the column spaces of the two idempotents.

**Right multiplication and the exchange.** In the Peirce basis, right multiplication by the two mixed units is the pair of block swaps

$$
R_{\vec\Upsilon_-}=\begin{pmatrix}0&0\\ \mathrm I_2&0\end{pmatrix},
\qquad
R_{\vec\Upsilon_+}=\begin{pmatrix}0&\mathrm I_2\\0&0\end{pmatrix}.
$$

Hence $\xi\vec\Upsilon_-$ lies in $S_-$ for every $\xi\in S_+$, and $S_-\vec\Upsilon_-=0$; right multiplication by $\vec\Upsilon_+$ does the reverse. The two maps are inverse on the planes, and both blocks move together: the exchange is a single right multiplication, not a pair of independent maps on the two copies.

**Peirce index.** Left multiplication preserves each block; right multiplication swaps them. The two blocks are the two Peirce copies, not two chiralities, and the only operation of the algebra that relates them is multiplication on the right by a mixed unit.

## The Nilpotents as Off-Diagonal Units

**Every nilpotent is a scalar multiple of the image of an off-diagonal matrix unit, and every nonzero nilpotent is a square-zero rank-two matrix.**

A nilpotent of $\mathbb{B}$ is a nonzero element of a mixed Peirce corner, so its image under $\mathsf M_4$ is a nonzero element of the image of $\mathbb{C}E_{12}$ or $\mathbb{C}E_{21}$ in the block form. Such an element is $\mu E_{12}\otimes\mathrm I_2$ or $\mu E_{21}\otimes\mathrm I_2$ with $\mu\in\mathbb{C}^{\times}$. Its square is zero, its trace is zero and its rank is two.

The two standard nilpotents give the two off-diagonal doubled units. Every other nilpotent is a nonzero scalar multiple of one of them, conjugated by an inner automorphism of the algebra; the scalar is the coordinate of the nilpotent in its corner, and the conjugacy is the change of the Peirce frame.

## Summary

The Peirce coordinates of the standard pair are the entries of the $2\times2$ model, and the left regular matrix is that model duplicated: $\mathsf S^{-1}\mathsf M_4(\tilde Q)\mathsf S=\operatorname{diag}(\mathsf M_2(\tilde Q),\mathsf M_2(\tilde Q))$ in the basis $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$. The two diagonal blocks are the two spinor planes, left multiplication acts on each by the same matrix and never mixes them, right multiplication by the mixed units swaps them, and the two planes are not the column spaces of the idempotents. The trace is four times the scalar part and the determinant is the square of the central scalar. The four Peirce elements are one system of $2\times2$ matrix units, duplicated, not a system of $4\times4$ units.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf M_4(\tilde Q)$ | the left regular matrix, $\mu$-th column $=$ coordinates of $\tilde Q e_\mu$ |
| $\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ | the Peirce basis, ordered by contiguous planes |
| $\mathsf S$ | the change of basis with the four Peirce coordinate columns |
| $\mathsf M_2(\tilde Q)$ | the $2\times2$ model, $\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}$ |
| $a_{ij}$ | the four Peirce coordinates |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the two spinor planes, the two blocks |
| $R_{\vec\Upsilon_\pm}$ | right multiplication by the mixed units, the block swaps |
| $\langle\tilde Q\rangle_{\natural}$ | the central scalar $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ |

## Further Reading

- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-in-the-biquaternion-algebra.html), for the corners and the Peirce table
- [Spinors as Peirce Coordinates in the Biquaternion Algebra](spinors-as-peirce-coordinates-in-the-biquaternion-algebra.html), for the two planes, their weight bases and the exchange
- [$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m2c-representation-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the $2\times2$ version
- [$M_4(\mathbb{C})_L$ Model : The Product, the Trace and the Determinant](m4c-representation-the-matrix-product-and-the-algebra-structure.html), for the regular matrix
- [$M_4(\mathbb{C})_L$ Model : The Centraliser and the Double Centraliser](m4c-representation-the-centraliser-and-the-double-centraliser.html), for the right regular matrix
- [Nilpotents](square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html), for the nilpotent cone
