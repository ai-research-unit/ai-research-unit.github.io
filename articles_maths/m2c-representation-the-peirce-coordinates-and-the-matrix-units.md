# __$M_2(\mathbb{C})$ Representation : The Peirce Coordinates and the Matrix Units__

## Introduction

A Peirce decomposition with two primitive idempotents writes every biquaternion in four corners. Read as a matrix, the four corner coordinates are the four entries, and the four corner basis elements are the four matrix units. The coordinate model is therefore the same isomorphism as the fixed matrix model, read in the basis adapted to the idempotents rather than the basis adapted to the vector part.

This article develops the coordinate model, the systems of matrix units, and the rigidity statement that all such systems are conjugate. It is the matrix form of *Ideals and Peirce Decompositions of the Biquaternion Algebra*, §*The Peirce Coordinates and the Matrix Model* and §*Systems of Matrix Units*.

**Conventions.** The algebra and the fixed model are those of *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure*. The standard idempotent pair is

$$
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\qquad
\tilde\Pi_-=\tfrac12(e_t-i\vec e_z),
$$

and the two standard nilpotents are

$$
\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y),\qquad
\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y).
$$

The labels $x,y$ are the labels of the standard pair. The eigenbasis of a general element uses a different labelling, $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$, treated in *$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix*.

**Boundaries.** The Peirce decomposition is *Ideals and Peirce Decompositions of the Biquaternion Algebra*; the columns and rows are *$M_2(\mathbb{C})$ Representation : The Columns, the Rows and the Spinor Module*; the nilpotents are *Square Roots of Zero and the Nilpotents of the Biquaternion Algebra*; the inner automorphisms are *Biquaternion Automorphisms and Derivations*.

## The Peirce Table

**The four basis elements multiply as the four matrix units.**

| Product | Value |
|---|---|
| $\tilde\Pi_+^2$ | $\tilde\Pi_+$ |
| $\tilde\Pi_-^2$ | $\tilde\Pi_-$ |
| $\tilde\Pi_+\tilde\Pi_-$ | $0$ |
| $\vec\Upsilon_x^2$, $\vec\Upsilon_y^2$ | $0$ |
| $\vec\Upsilon_x\vec\Upsilon_y$ | $\tilde\Pi_+$ |
| $\vec\Upsilon_y\vec\Upsilon_x$ | $\tilde\Pi_-$ |
| $\tilde\Pi_+\vec\Upsilon_x=\vec\Upsilon_x\tilde\Pi_-$ | $\vec\Upsilon_x$ |
| $\tilde\Pi_-\vec\Upsilon_y=\vec\Upsilon_y\tilde\Pi_+$ | $\vec\Upsilon_y$ |

The table is the multiplication table of the four matrix units $E_{11},E_{12},E_{21},E_{22}$ under the correspondence

$$
\tilde\Pi_+\longmapsto E_{11},\qquad
\vec\Upsilon_x\longmapsto E_{12},\qquad
\vec\Upsilon_y\longmapsto E_{21},\qquad
\tilde\Pi_-\longmapsto E_{22}.
$$

Indeed $E_{12}E_{21}=E_{11}$ and $E_{21}E_{12}=E_{22}$, $E_{11}E_{12}=E_{12}=E_{12}E_{22}$, and the two off-diagonal units square to zero. The correspondence is the algebra table read in matrices.

## The Coordinate Isomorphism

**Proposition.** Every element has a unique expansion

$$
\tilde Q=a_{11}\tilde\Pi_++a_{12}\vec\Upsilon_x+a_{21}\vec\Upsilon_y+a_{22}\tilde\Pi_-,
\qquad a_{ij}\in\mathbb{C},
$$

and the map that sends $\tilde Q$ to the matrix $\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}$ is an isomorphism of $\mathbb{C}$-algebras $\mathbb{B}\to M_2(\mathbb{C})$.

*Proof.* The four basis elements are a $\mathbb{C}$-basis, since the change from $(e_t,\vec e_x,\vec e_y,\vec e_z)$ to $(\tilde\Pi_+,\vec\Upsilon_x,\vec\Upsilon_y,\tilde\Pi_-)$ is invertible: the matrix of the change has determinant $1/4$. The map is $\mathbb{C}$-linear and bijective. It is multiplicative because it sends the four basis elements to the four matrix units and the multiplication table above is the matrix-unit table. Bilinearity extends the identity to all elements.

**The corner coordinates.** The four coefficients are the four Peirce coordinates. They are recovered from the element by the trace pairing:

$$
a_{11}=\operatorname{Tr}(\tilde\Pi_+\tilde Q),\qquad
a_{12}=\operatorname{Tr}(\vec\Upsilon_y\tilde Q),\qquad
a_{21}=\operatorname{Tr}(\vec\Upsilon_x\tilde Q),\qquad
a_{22}=\operatorname{Tr}(\tilde\Pi_-\tilde Q),
$$

with the two nilpotents exchanged in the dual basis because $\operatorname{Tr}(\vec\Upsilon_x\vec\Upsilon_y)=1$ and $\operatorname{Tr}(\vec\Upsilon_y\vec\Upsilon_x)=1$. The exchange is the matrix statement that the dual basis of $(\tilde\Pi_+,\vec\Upsilon_x,\vec\Upsilon_y,\tilde\Pi_-)$ is $(\tilde\Pi_+,\vec\Upsilon_y,\vec\Upsilon_x,\tilde\Pi_-)$.

**The two invariants.** In the coordinates,

$$
\operatorname{Tr}\mathsf{M}_2^{Q}(\tilde Q)=a_{11}+a_{22}=2Q_t,\qquad
\det\mathsf{M}_2^{Q}(\tilde Q)=a_{11}a_{22}-a_{12}a_{21}=\langle\tilde Q\rangle_{\natural}.
$$

The scalar part is the sum of the two diagonal corners, and the quaternionic norm is the determinant of the corner matrix. The two symmetric functions of the corner coordinates are the two invariants of the algebra.

**The ideals in the coordinates.** The first column $\mathbb{C}E_{11}\oplus\mathbb{C}E_{21}$ is the image of $\mathbb{B}\tilde\Pi_+$, and the second column is the image of $\mathbb{B}\tilde\Pi_-$. The first row is the image of $\tilde\Pi_+\mathbb{B}$, and the second row is the image of $\tilde\Pi_-\mathbb{B}$. The columns are the left ideals and the rows are the right ideals; the coordinate model makes the two groupings of the same four entries visible at once.

## Systems of Matrix Units

**Definition.** A system of $2\times2$ matrix units in $\mathbb{B}$ is a family $\{E_{11},E_{12},E_{21},E_{22}\}$ with

$$
E_{ij}E_{kl}=\delta_{jk}E_{il},\qquad
E_{11}+E_{22}=e_t,\qquad
E_{11}\neq0.
$$

The relations already imply that $E_{11}$ and $E_{22}$ are orthogonal idempotents summing to the unit, and that the two off-diagonal elements are square-zero.

**Proposition.** A system of matrix units is the same data as a Peirce decomposition with two primitive idempotents, together with a basis of each mixed corner normalised by $E_{12}E_{21}=E_{11}$.

*Proof.* Given the system, put $\tilde\Pi=E_{11}$ and $\tilde\Pi'=E_{22}$. The relations give $\tilde\Pi^2=\tilde\Pi$, $\tilde\Pi'^2=\tilde\Pi'$, $\tilde\Pi\tilde\Pi'=0$, and $E_{12}\in\tilde\Pi\mathbb{B}\tilde\Pi'$, $E_{21}\in\tilde\Pi'\mathbb{B}\tilde\Pi$. Conversely, given a primitive idempotent $\tilde\Pi$ and a nonzero $u\in\tilde\Pi\mathbb{B}\tilde\Pi'$, a nonzero $w\in\tilde\Pi'\mathbb{B}\tilde\Pi$ can be rescaled so that $uw=\tilde\Pi$; then $E_{11}=\tilde\Pi$, $E_{22}=\tilde\Pi'$, $E_{12}=u$, $E_{21}=w$ satisfy the relations.

**The reciprocal scaling.** The pair $(u,w)$ is not determined by $\tilde\Pi$. Replacing $u$ by $\mu u$ and $w$ by $\mu^{-1}w$ with $\mu\in\mathbb{C}^{\times}$ leaves every product of the system unchanged. A fixed primitive idempotent therefore carries a reciprocal $\mathbb{C}^{\times}$ of normalised mixed bases.

**Theorem (uniqueness up to conjugation).** Every system of $2\times2$ matrix units of $\mathbb{B}$ is the image of the standard system under an inner automorphism: there is a unit $\tilde U$ with $E_{ij}=\tilde U\tilde E_{ij}\tilde U^{-1}$.

*Proof.* By the coordinate isomorphism the question is the corresponding statement for $M_2(\mathbb{C})$. A primitive idempotent $P$ of $M_2(\mathbb{C})$ is the projector onto a line $\ell$ along a complementary line $m$. Choose a basis with first vector in $\ell$ and second in $m$, and let $G$ be the matrix of that basis; then $GPG^{-1}=E_{11}$. The stabiliser of $E_{11}$ is the diagonal torus, since a conjugation fixing $E_{11}$ preserves its image and its kernel; conjugating by $\operatorname{diag}(a,d)$ multiplies $E_{12}$ by $a/d$ and $E_{21}$ by $d/a$. In a system with $E_{11}$ and $E_{22}$ fixed, the two off-diagonal elements lie in the one-dimensional mixed spaces and satisfy $E_{12}E_{21}=E_{11}$, so they are determined by a single scalar, and the diagonal conjugation is transitive on that scalar. The unit group of $\mathbb{B}$ acts by algebra automorphisms, and every automorphism of $\mathbb{B}$ is inner, so the matrix statement transports back.

**The stabiliser.** The stabiliser of the standard pair in the unit group is the torus

$$
\{a\tilde\Pi_++b\tilde\Pi_-:a,b\in\mathbb{C}^{\times}\},
$$

acting on the mixed elements by $\vec\Upsilon_x\mapsto(a/b)\vec\Upsilon_x$ and $\vec\Upsilon_y\mapsto(b/a)\vec\Upsilon_y$. This is the reciprocal scaling again, now as the diagonal torus of the matrix model.

## The Nilpotents as Off-Diagonal Units

**Proposition.** Every nontrivial idempotent of $\mathbb{B}$ is a product of two nilpotents.

*Proof.* Let $\tilde\Pi$ be a nontrivial idempotent and $\tilde\Pi'=e_t-\tilde\Pi$ its complement. The two mixed corners are square-zero, so every nonzero $u\in\tilde\Pi\mathbb{B}\tilde\Pi'$ and every nonzero $w\in\tilde\Pi'\mathbb{B}\tilde\Pi$ is nilpotent. By the construction above, $uw=\lambda\tilde\Pi$ for some $\lambda\in\mathbb{C}^{\times}$; replacing $w$ by $\lambda^{-1}w$ keeps it in the corner, nonzero and square-zero, and gives $uw=\tilde\Pi$.

The trivial idempotent $e_t$ is the exception: if $uv=e_t$ then $u$ is a unit, and a nilpotent is not a unit. The zero idempotent is $0\cdot0$.

**The Jordan block.** Under the fixed model, a nonzero nilpotent is a nonzero trace-free singular matrix. Such a matrix has only the eigenvalue zero and is conjugate to the single Jordan block

$$
\begin{pmatrix}0&1\\0&0\end{pmatrix}.
$$

The two standard nilpotents are the two off-diagonal matrix units, and every other nilpotent is a conjugate of one of them. The statement is the matrix form of the fact that the nilpotent cone of $\mathbb{B}$ is a single conjugacy class up to scale, with the two chiralities corresponding to the two off-diagonal positions.

**The two chiralities.** The two off-diagonal units are not conjugate by a diagonal element of the standard torus; they are exchanged by the Weyl element $\begin{pmatrix}0&1\\1&0\end{pmatrix}$, which is the image of a unit of $\mathbb{B}$ exchanging the two idempotents. The exchange is an inner automorphism, so the two nilpotents are conjugate in $M_2(\mathbb{C})$; the labels $x$ and $y$ are a choice of which is which.

## Summary

The Peirce coordinates of the standard pair are the matrix entries, and the four corner elements are the four matrix units. Trace is the sum of the diagonal corners and determinant is the determinant of the corner matrix. A system of matrix units is a Peirce decomposition with a normalised mixed basis, and it carries a reciprocal $\mathbb{C}^{\times}$ of choices. All systems are conjugate by inner automorphisms, and every nontrivial idempotent is a product of two nilpotents. In the matrix model the nilpotents are the nonzero trace-free singular matrices, conjugate to the Jordan block.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | the standard idempotent pair |
| $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$, $\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)$ | the standard nilpotents |
| $a_{ij}$ | the Peirce coordinates |
| $E_{ij}$ | the matrix units; $E_{ij}E_{kl}=\delta_{jk}E_{il}$ |
| $\mathsf{M}_2^{Q}$ | the coordinate model attached to the pair |
| $\mathbb{C}^{\times}$ | the reciprocal scaling of the mixed basis |
| $\operatorname{diag}(a,d)$ | the stabiliser torus of $E_{11}$ |

## Further Reading

- [Ideals and Peirce Decompositions of the Biquaternion Algebra](ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), for the Peirce decomposition and its uniqueness
- [Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html), for the nilpotent cone
- [$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure](m2c-representation-the-matrix-product-and-the-algebra-structure.html), for the fixed model
- [$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix](m2c-representation-the-eigenbasis-and-the-diagonalising-matrix.html), for the eigenbasis labelling
- [$M_2(\mathbb{C})$ Representation : The Columns, the Rows and the Spinor Module](m2c-representation-the-columns-the-rows-and-the-spinor-module.html), for the ideals as columns and rows
- [Biquaternion Automorphisms and Derivations](biquaternion-automorphisms-and-derivations.html), for the inner automorphisms
- [Matrix Algebras](matrix-algebras.html), for systems of matrix units
