# __$M_4(\mathbb{C})_L$ Representation : The Peirce Coordinates and the Matrix Units__

## Introduction

The Peirce decomposition writes a biquaternion as four coordinates in a system of matrix units. In the $2\times2$ model the units are the ordinary matrix units of $M_2(\mathbb{C})$. In the $4\times4$ regular model they become four rank-two matrices, each a doubled copy of a $2\times2$ unit, and the four coordinates are unchanged.

This article displays the four matrices, proves that they multiply as the matrix units of $M_2(\mathbb{C})$, and reads the Peirce coordinates in the coefficients. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Representation : The Peirce Coordinates and the Matrix Units*.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})_L$ Representation : The Matrix Product and the Algebra Structure*. The fixed Peirce elements are
$$
\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z),\qquad
\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y),
$$
and the change $S$ has columns $\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-$, with
$$
S^{-1}\mathsf{M}_4(\tilde Q)S=\mathrm I_2\otimes\mathsf{M}_2(\tilde Q).
$$

**Boundaries.** The spectral projectors of a general element are *$M_4(\mathbb{C})_L$ Representation : The Spectral Projectors and the Nilpotents*; the minimal left ideals are *$M_4(\mathbb{C})_L$ Representation : The Columns, the Rows and the Spinor Module*; the abstract Peirce decomposition is *Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra*; the $2\times2$ units are *$M_2(\mathbb{C})$ Representation : The Peirce Coordinates and the Matrix Units*.

## The Peirce Table

The four elements satisfy

$$
\tilde\Pi_+^2=\tilde\Pi_+,\quad
\tilde\Pi_-^2=\tilde\Pi_-,\quad
\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0,
$$

$$
\vec\Upsilon_\pm^2=0,\qquad
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,
$$

and the mixed products are

$$
\tilde\Pi_+\vec\Upsilon_+=0,\quad
\vec\Upsilon_+\tilde\Pi_+=\vec\Upsilon_+,\quad
\tilde\Pi_-\vec\Upsilon_+=\vec\Upsilon_+,\quad
\vec\Upsilon_+\tilde\Pi_-=\vec\Upsilon_+,
$$

$$
\tilde\Pi_+\vec\Upsilon_-=\vec\Upsilon_-,\quad
\vec\Upsilon_-\tilde\Pi_+=0,\quad
\tilde\Pi_-\vec\Upsilon_-=0,\quad
\vec\Upsilon_-\tilde\Pi_-=\vec\Upsilon_-.
$$

The table is the multiplication table of the four units
$$
E_{11}=\tilde\Pi_+,\qquad E_{21}=\vec\Upsilon_+,\qquad E_{12}=\vec\Upsilon_-,\qquad E_{22}=\tilde\Pi_-,
$$
in the order $(E_{11},E_{21},E_{12},E_{22})$.

**The coordinate isomorphism.** Every element has a unique expansion

$$
\tilde Q=a\tilde\Pi_++b\vec\Upsilon_-+c\vec\Upsilon_++d\tilde\Pi_-,
$$

and the four coefficients, in the order of the matrix entries, are

$$
a=Q_t-iQ_z,\qquad b=-iQ_x-Q_y,\qquad c=-iQ_x+Q_y,\qquad d=Q_t+iQ_z.
$$

The map $\tilde Q\mapsto(a,b,c,d)$ is a $\mathbb{C}$-linear isomorphism $\mathbb{B}\to\mathbb{C}^4$, and the multiplication becomes the ordinary $2\times2$ multiplication,
$$
\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}a'&b'\\c'&d'\end{pmatrix}
=\begin{pmatrix}aa'+bc'&ab'+bd'\\ca'+dc'&cb'+dd'\end{pmatrix}.
$$

## The Coordinate Isomorphism

The images of the four units are

$$
\mathsf{M}_4(\tilde\Pi_+)=\begin{pmatrix}
\tfrac12&0&0&-\tfrac{i}{2}\\
0&\tfrac12&-\tfrac{i}{2}&0\\
0&\tfrac{i}{2}&\tfrac12&0\\
\tfrac{i}{2}&0&0&\tfrac12
\end{pmatrix},
\qquad
\mathsf{M}_4(\tilde\Pi_-)=\begin{pmatrix}
\tfrac12&0&0&\tfrac{i}{2}\\
0&\tfrac12&\tfrac{i}{2}&0\\
0&-\tfrac{i}{2}&\tfrac12&0\\
-\tfrac{i}{2}&0&0&\tfrac12
\end{pmatrix},
$$

$$
\mathsf{M}_4(\vec\Upsilon_+)=\begin{pmatrix}
0&-\tfrac{i}{2}&-\tfrac12&0\\
\tfrac{i}{2}&0&0&\tfrac12\\
\tfrac12&0&0&-\tfrac{i}{2}\\
0&-\tfrac12&\tfrac{i}{2}&0
\end{pmatrix},
\qquad
\mathsf{M}_4(\vec\Upsilon_-)=\begin{pmatrix}
0&-\tfrac{i}{2}&\tfrac12&0\\
\tfrac{i}{2}&0&0&-\tfrac12\\
-\tfrac12&0&0&-\tfrac{i}{2}\\
0&\tfrac12&\tfrac{i}{2}&0
\end{pmatrix}.
$$

Each is a rank-two matrix, and the four together span the four-dimensional image $M_4(\mathbb{C})_L$.

**The unique expansion.** Every element has a unique expansion
$$
\tilde X=a_{11}\tilde\Pi_++a_{12}\vec\Upsilon_++a_{21}\vec\Upsilon_-+a_{22}\tilde\Pi_-,
\qquad a_{ij}\in\mathbb{C},
$$
and the map that sends $\tilde X$ to $\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}$ is an isomorphism of $\mathbb{C}$-algebras $\mathbb{B}\to M_2(\mathbb{C})$. The four regular matrices above are the images of the four basis elements, and the theorem below is the statement that the isomorphism is multiplicative.

**Theorem (the regular units multiply as $2\times2$ units).** With the order above,

$$
\mathsf{M}_4(E_{ij})\mathsf{M}_4(E_{kl})=\delta_{jk}\mathsf{M}_4(E_{il}),
\qquad
\sum_{i=1}^{2}\mathsf{M}_4(E_{ii})=\mathrm I_4.
$$

*Proof.* Apply $\mathsf{M}_4$ to the Peirce table. The last identity is $\mathsf{M}_4(\tilde\Pi_++\tilde\Pi_-)=\mathsf{M}_4(e_t)=\mathrm I_4$. $\square$

**The block form.** In the Peirce basis,

$$
S^{-1}\mathsf{M}_4(E_{11})S=\operatorname{diag}(E_{11},E_{11}),\quad
S^{-1}\mathsf{M}_4(E_{21})S=\operatorname{diag}(E_{21},E_{21}),
$$
$$
S^{-1}\mathsf{M}_4(E_{12})S=\operatorname{diag}(E_{12},E_{12}),\quad
S^{-1}\mathsf{M}_4(E_{22})S=\operatorname{diag}(E_{22},E_{22}).
$$

Each unit is duplicated in the two blocks. This is the precise sense in which the regular model carries the $2\times2$ matrix units twice.

## The Coordinates in the Coefficients

The four coordinates are the entries of the $2\times2$ matrix:

$$
\mathsf{M}_2(\tilde Q)=\begin{pmatrix}a&b\\c&d\end{pmatrix}
=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}.
$$

The scalar coordinate $a+d=2Q_t$ is the trace; the determinant $ad-bc=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ is the norm. The vector part is split between the off-diagonal coordinates and the diagonal difference:
$$
b-c=-2Q_y,\qquad b+c=-2iQ_x,\qquad a-d=-2iQ_z.
$$

The formulas are the same as in the $2\times2$ model. The regular matrix repeats them in its two blocks, so every coordinate appears twice in the $4\times4$ matrix.

## Systems of Matrix Units

**The algebra system.** The four elements $E_{ij}$ form a complete system of matrix units: they are linearly independent, multiply by the $E_{ij}$ rule, and sum to the identity. The algebra is therefore isomorphic to $M_2(\mathbb{C})$, with the isomorphism sending $E_{ij}$ to the ordinary unit.

**The regular system.** The four matrices $\mathsf{M}_4(E_{ij})$ are not the ordinary matrix units of $M_4(\mathbb{C})$. They are rank-two matrices, and the ordinary units $e_{ij}$ of $M_4(\mathbb{C})$ are rank one. The two systems are related by the block decomposition: $\mathsf{M}_4(E_{ij})$ is the direct sum of two copies of the $2\times2$ unit $E_{ij}$, placed in the two diagonal blocks. The ordinary $4\times4$ units that mix the blocks do not lie in the image.

**The off-diagonal units.** The two nilpotents $\vec\Upsilon_\pm$ are the off-diagonal units $E_{21}$ and $E_{12}$. They satisfy
$$
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,
$$
so each nilpotent is a partial isomorphism between the two minimal left ideals. In the regular model this becomes a pair of maps between the two copies, one in each block.

## The Nilpotents as Off-Diagonal Units

**Proposition.** Every nontrivial idempotent of $\mathbb{B}$ is a product of two nilpotents.

*Proof.* Let $\tilde\Pi$ be a nontrivial idempotent and $\tilde\Pi'=e_t-\tilde\Pi$ its complement. The two mixed corners are square-zero, so every nonzero $u\in\tilde\Pi\mathbb{B}\tilde\Pi'$ and every nonzero $w\in\tilde\Pi'\mathbb{B}\tilde\Pi$ is nilpotent. The construction of the Peirce basis gives $uw=\lambda\tilde\Pi$ for some $\lambda\in\mathbb{C}^{\times}$; replacing $w$ by $\lambda^{-1}w$ keeps it in the corner, nonzero and square-zero, and gives $uw=\tilde\Pi$. The trivial idempotent $e_t$ is the exception: if $uv=e_t$ then $u$ is a unit, and a nilpotent is not a unit. $\square$

**The regular image.** In the regular model the two off-diagonal units are
$$
\mathsf{M}_4(\vec\Upsilon_+)=\mathsf{M}_4(E_{12}),\qquad
\mathsf{M}_4(\vec\Upsilon_-)=\mathsf{M}_4(E_{21}),
$$
each duplicated in the two blocks. Their squares vanish, their products are the rank-two spectral projectors, and every nilpotent of the image is a conjugate of one of them. The nilpotent cone of the algebra is a single conjugacy class up to scale; in the regular model each nonzero nilpotent has rank two, because it is the direct sum of two identical $2\times2$ nilpotents.

**The Jordan block.** In the $2\times2$ model a nonzero nilpotent is conjugate to the single Jordan block $\begin{pmatrix}0&1\\0&0\end{pmatrix}$. In the $4\times4$ regular model the corresponding matrix is the direct sum of two copies of that block, of rank two and with a single eigenvalue zero. The Jordan form has two blocks of size two, not one block of size four, because the two copies are independent.

**The two chiralities.** The two off-diagonal units are not conjugate by a diagonal element of the standard torus; they are exchanged by the Weyl element, which is the image of a unit of $\mathbb{B}$ exchanging the two idempotents. The exchange is an inner automorphism, so the two nilpotents are conjugate in the image; the labels $x$ and $y$ are a choice of which is which.

## Summary

The four Peirce elements $\tilde\Pi_\pm,\vec\Upsilon_\pm$ map to four rank-two matrices that multiply as the $2\times2$ matrix units. Their span is the four-dimensional image of the regular representation. In the Peirce basis each unit becomes the direct sum of two copies of the corresponding $2\times2$ unit, so each Peirce corner is doubled. The coordinates themselves are unchanged: they are the four entries of $\mathsf{M}_2(\tilde Q)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Pi_\pm,\vec\Upsilon_\pm$ | the Peirce idempotents and nilpotents |
| $E_{11},E_{21},E_{12},E_{22}$ | the abstract matrix units |
| $a,b,c,d$ | the four Peirce coordinates |
| $\mathsf{M}_4(E_{ij})$ | the regular unit, a rank-two matrix |
| $S$ | the Peirce change |

## Further Reading

- [$M_4(\mathbb{C})_L$ Representation : The Columns, the Rows and the Spinor Module](m4c-representation-the-columns-the-rows-and-the-spinor-module.html), for the ideals
- [$M_4(\mathbb{C})_L$ Representation : The Spectral Projectors and the Nilpotents](m4c-representation-the-spectral-projectors-and-the-nilpotents.html), for the spectral version
- [$M_2(\mathbb{C})$ Representation : The Peirce Coordinates and the Matrix Units](m2c-representation-the-peirce-coordinates-and-the-matrix-units.html), for the $2\times2$ system
- [Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the abstract decomposition
