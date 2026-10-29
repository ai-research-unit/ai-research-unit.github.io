# __$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes__

## Introduction

A Peirce decomposition with two primitive idempotents writes every biquaternion in four corners. Read as a matrix, the four corner coordinates are the four entries, and the four corner basis elements are the four matrix units. The same four entries carry a second grouping: the two columns. Each column is one of the two Peirce planes $\mathbb{B}\tilde\Pi_\pm$, the spinor planes of *Spinors as Peirce Coordinates in the Biquaternion Algebra*, and the matrix shows the two groupings at once.

This article develops the Peirce table, the coordinate isomorphism, the systems of matrix units, the two planes and the left and right actions on them. It is the matrix form of *The Peirce Decomposition of the Biquaternion Algebra* and *Spinors as Peirce Coordinates in the Biquaternion Algebra*. It uses no form, no norm and no module.

**Conventions.** The algebra and the fixed model are those of *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. The standard idempotent pair is

$$
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\qquad
\tilde\Pi_-=\tfrac12(e_t-i\vec e_z),
$$

and the two standard nilpotents are

$$
\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y),\qquad
\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y).
$$

In the generic Peirce labelling of *Spinors as Peirce Coordinates in the Biquaternion Algebra*, $\vec\Upsilon_x=\vec\Upsilon_-$ and $\vec\Upsilon_y=\vec\Upsilon_+$. The labels $x,y$ are the labels of the standard pair; a general element uses the labelling $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$, treated in *$M_2(\mathbb{C})$ Model : The Eigenbasis and the Diagonalising Matrix*.

**Boundaries.** The abstract Peirce decomposition is *The Peirce Decomposition of the Biquaternion Algebra*; the two planes, their weight bases and the exchange are *Spinors as Peirce Coordinates in the Biquaternion Algebra*; the nilpotent cone is *Nilpotents*; the inner automorphisms are *Biquaternion Automorphisms and Derivations*. The module reading of the two planes is *The Minimal Left Ideals* and is not used here.

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

*Proof.* The four basis elements are a $\mathbb{C}$-basis, since the change from $(e_t,\vec e_x,\vec e_y,\vec e_z)$ to $(\tilde\Pi_+,\vec\Upsilon_x,\vec\Upsilon_y,\tilde\Pi_-)$ has determinant $1/4$ and is therefore invertible. The map is $\mathbb{C}$-linear and bijective. It is multiplicative because it sends the four basis elements to the four matrix units and the Peirce table above is the matrix-unit table. Bilinearity extends the identity to all elements.

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

The scalar part is the sum of the two diagonal corners, and the central scalar is the determinant of the corner matrix. The two symmetric functions of the corner coordinates are the two invariants of the algebra.

**The two groupings.** The four entries are grouped by columns and by rows. The columns give the two planes $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$; the rows give the two right Peirce rows $\tilde\Pi_+\mathbb{B}$ and $\tilde\Pi_-\mathbb{B}$. The same four entries carry both groupings, and the groupings differ: the first column and the first row meet in $E_{11}$, and together they span a three-dimensional space that is neither one of the two left planes nor one of the two right planes.

## The Coordinates in the Coefficients

The standard pair makes the Peirce coordinates equal to the entries of the fixed model. Expanding the general element in the four corner elements gives

$$
Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z
=a_{11}\tilde\Pi_++a_{12}\vec\Upsilon_x+a_{21}\vec\Upsilon_y+a_{22}\tilde\Pi_-,
$$

with

$$
a_{11}=Q_t-iQ_z,\qquad
a_{12}=-iQ_x-Q_y,\qquad
a_{21}=-iQ_x+Q_y,\qquad
a_{22}=Q_t+iQ_z .
$$

The four formulas are the inverse of the four definitions of the corner elements, and they give

$$
\mathsf M_2^{Q}(\tilde Q)=
\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}
=\mathsf M_2(\tilde Q).
$$

The fixed model is therefore the coordinate model attached to the standard pair, and the equality is the matrix form of the fact that the standard idempotents are the coordinate idempotents.

## Systems of Matrix Units

**Definition.** A system of $2\times2$ matrix units in $\mathbb{B}$ is a family $\{E_{11},E_{12},E_{21},E_{22}\}$ with

$$
E_{ij}E_{kl}=\delta_{jk}E_{il},\qquad
E_{11}+E_{22}=e_t,\qquad
E_{11}\neq0.
$$

The relations already imply that $E_{11}$ and $E_{22}$ are orthogonal idempotents summing to the unit, and that the two off-diagonal elements are square-zero.

**Proposition.** A system of matrix units is the same data as a Peirce decomposition with two primitive idempotents, together with a basis of each mixed corner normalised by $E_{12}E_{21}=E_{11}$.

*Proof.* Given the system, put $\tilde\Pi=E_{11}$ and $\tilde\Pi'=E_{22}$. The relations give $\tilde\Pi^2=\tilde\Pi$, $\tilde\Pi'^2=\tilde\Pi'$, $\tilde\Pi\tilde\Pi'=0$, and $E_{12}\in\tilde\Pi\mathbb{B}\tilde\Pi'$, $E_{21}\in\tilde\Pi'\mathbb{B}\tilde\Pi$. Conversely, given a primitive idempotent $\tilde\Pi$ and a nonzero $u\in\tilde\Pi\mathbb{B}\tilde\Pi'$, the product of two nonzero elements of opposite mixed corners is a nonzero multiple of $\tilde\Pi$, so a nonzero $w\in\tilde\Pi'\mathbb{B}\tilde\Pi$ can be rescaled so that $uw=\tilde\Pi$; then $E_{11}=\tilde\Pi$, $E_{22}=\tilde\Pi'$, $E_{12}=u$, $E_{21}=w$ satisfy the relations.

**The reciprocal scaling.** The pair $(u,w)$ is not determined by $\tilde\Pi$. Replacing $u$ by $\mu u$ and $w$ by $\mu^{-1}w$ with $\mu\in\mathbb{C}^{\times}$ leaves every product of the system unchanged. A fixed primitive idempotent therefore carries a reciprocal $\mathbb{C}^{\times}$ of normalised mixed bases.

**Theorem (uniqueness up to conjugation).** Every system of $2\times2$ matrix units of $\mathbb{B}$ is the image of the standard system under an inner automorphism: there is a unit $\tilde U$ with $E_{ij}=\tilde U\tilde E_{ij}\tilde U^{-1}$.

*Proof.* By the coordinate isomorphism the question is the corresponding statement for $M_2(\mathbb{C})$. A primitive idempotent $P$ of $M_2(\mathbb{C})$ is the projector onto a line $\ell$ along a complementary line $m$. Choose a basis with first vector in $\ell$ and second in $m$, and let $G$ be the matrix of that basis; then $GPG^{-1}=E_{11}$. The stabiliser of $E_{11}$ is the diagonal torus, since a conjugation fixing $E_{11}$ preserves its image and its kernel; conjugating by $\operatorname{diag}(a,d)$ multiplies $E_{12}$ by $a/d$ and $E_{21}$ by $d/a$. In a system with $E_{11}$ and $E_{22}$ fixed, the two off-diagonal elements lie in the one-dimensional mixed spaces and satisfy $E_{12}E_{21}=E_{11}$, so they are determined by a single scalar, and the diagonal conjugation is transitive on that scalar. The unit group of $\mathbb{B}$ acts by algebra automorphisms, and every automorphism of $\mathbb{B}$ is inner, so the matrix statement transports back.

**The stabiliser.** The common stabiliser of the two standard idempotents in the unit group is the torus

$$
\{a\tilde\Pi_++b\tilde\Pi_-:a,b\in\mathbb{C}^{\times}\},
$$

acting on the mixed elements by $\vec\Upsilon_x\mapsto(a/b)\vec\Upsilon_x$ and $\vec\Upsilon_y\mapsto(b/a)\vec\Upsilon_y$. This is the reciprocal scaling again, now as the diagonal torus of the matrix model.

## The Nilpotents as Off-Diagonal Units

**Proposition.** Every nontrivial idempotent of $\mathbb{B}$ is a product of two nilpotents.

*Proof.* Let $\tilde\Pi$ be a nontrivial idempotent and $\tilde\Pi'=e_t-\tilde\Pi$ its complement. The two mixed corners are square-zero, so every nonzero $u\in\tilde\Pi\mathbb{B}\tilde\Pi'$ and every nonzero $w\in\tilde\Pi'\mathbb{B}\tilde\Pi$ is nilpotent. By the construction above, $uw=\lambda\tilde\Pi$ for some $\lambda\in\mathbb{C}^{\times}$; replacing $w$ by $\lambda^{-1}w$ keeps it in the corner, nonzero and square-zero, and gives $uw=\tilde\Pi$.

The trivial idempotent $e_t$ is the exception: if $uv=e_t$ then $u$ is a unit, and a nilpotent is not a unit. The zero idempotent is $0\cdot0$.

**The strictly triangular form.** Under the fixed model, a nonzero nilpotent is a nonzero trace-free singular matrix. Such a matrix has square zero, trace zero and determinant zero, and it is conjugate to the strictly triangular matrix

$$
\begin{pmatrix}0&1\\0&0\end{pmatrix}.
$$

The two standard nilpotents are the two off-diagonal matrix units, and every other nilpotent is a conjugate of one of them. The statement is the matrix form of the fact that the nilpotent cone of $\mathbb{B}$ is the zero element together with a single conjugacy class, with the two nilpotent lines corresponding to the two off-diagonal positions.

**The two nilpotent lines.** The two off-diagonal units are not conjugate by a diagonal element of the standard torus; they are exchanged by the Weyl element $\begin{pmatrix}0&1\\1&0\end{pmatrix}$, which is the image of a unit of $\mathbb{B}$ exchanging the two idempotents. The exchange is an inner automorphism, so the two nilpotents are conjugate in $M_2(\mathbb{C})$; the labels $x$ and $y$ are a choice of which is which. The two positions are the two Peirce copies, not two chiralities: the chirality of the biquaternion Dirac field is the central sign $\chi=ij$ of *Chirality: The Conjugate Pair*, which grades $S$ against $S^{\mathrm{c}}$.

## The Two Spinor Planes

**The two planes of the frame are the first and the second column, and each is spanned by one idempotent and one nilpotent.**

In the Peirce basis the planes are

$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_y,
\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_x\oplus\mathbb{C}\tilde\Pi_-,
$$

so that

$$
S_+\longmapsto\mathbb{C}E_{11}\oplus\mathbb{C}E_{21},
\qquad
S_-\longmapsto\mathbb{C}E_{12}\oplus\mathbb{C}E_{22}.
$$

The basis $(\tilde\Pi_+,\vec\Upsilon_y)$ of $S_+$ and the basis $(\vec\Upsilon_x,\tilde\Pi_-)$ of $S_-$ are the two weight bases of *Spinors as Peirce Coordinates in the Biquaternion Algebra*, written with the standard labels.

**The direct sum.** Every element satisfies $\tilde X=\tilde X\tilde\Pi_++\tilde X\tilde\Pi_-$, so the two planes span. Their intersection is zero: if $\tilde Y=\tilde Y\tilde\Pi_+=\tilde Y\tilde\Pi_-$, then $\tilde Y=\tilde Y\tilde\Pi_+=\tilde Y\tilde\Pi_-\tilde\Pi_+=0$. Hence

$$
\mathbb{B}=S_+\oplus S_-.
$$

### The Left Action on a Couple

**Proposition.** Let $\tilde P=a_{11}\tilde\Pi_++a_{12}\vec\Upsilon_x+a_{21}\vec\Upsilon_y+a_{22}\tilde\Pi_-$. In the basis $\mathcal{C}_+$ of $S_+$ and in the basis $\mathcal{C}_-$ of $S_-$, left multiplication by $\tilde P$ has the same matrix,

$$
L_{\tilde P}|_{S_+}=L_{\tilde P}|_{S_-}=\mathsf M_2(\tilde P)
=\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}.
$$

*Proof.* From the Peirce table,

$$
\tilde P\tilde\Pi_+=a_{11}\tilde\Pi_++a_{21}\vec\Upsilon_y,
\qquad
\tilde P\vec\Upsilon_y=a_{12}\tilde\Pi_++a_{22}\vec\Upsilon_y,
$$

so the two columns in $\mathcal{C}_+$ are $(a_{11},a_{21})$ and $(a_{12},a_{22})$. In the same way,

$$
\tilde P\vec\Upsilon_x=a_{11}\vec\Upsilon_x+a_{21}\tilde\Pi_-,
\qquad
\tilde P\tilde\Pi_-=a_{12}\vec\Upsilon_x+a_{22}\tilde\Pi_-,
$$

so the two columns in $\mathcal{C}_-$ are again $(a_{11},a_{21})$ and $(a_{12},a_{22})$. In each couple the first basis vector has the first column of $\mathsf M_2(\tilde P)$ and the second has the second.

Left multiplication preserves each plane, $\mathbb{B}S_\pm\subseteq S_\pm$, because $S_\pm=\mathbb{B}\tilde\Pi_\pm$ and the product is associative. Left multiplication therefore never mixes the two planes.

**Remark.** Inside a couple, left multiplication mixes the idempotent and the nilpotent whenever $a_{12}$ or $a_{21}$ is nonzero. A basis spinor is carried to a multiple of itself exactly when the coefficient that couples it to the other member of its couple vanishes.

### The Right Action and the Exchange

**Right multiplication is the operation that relates the two planes, and the mixed units exchange them.**

For $X\in M_2(\mathbb{C})$ the right product is

$$
MX=\begin{pmatrix}M_{11}X_{11}+M_{12}X_{21}&M_{11}X_{12}+M_{12}X_{22}\\
M_{21}X_{11}+M_{22}X_{21}&M_{21}X_{12}+M_{22}X_{22}\end{pmatrix}.
$$

With $X=E_{12}$ the first column is killed and the second column becomes the first column of $M$:

$$
ME_{12}=\begin{pmatrix}0&M_{11}\\0&M_{21}\end{pmatrix}.
$$

The product lies in the second column for every $M$, so right multiplication by $E_{12}$ maps $S_+$ into $S_-$ and kills $S_-$. With $X=E_{21}$ the roles are exchanged, and right multiplication by $E_{21}$ maps $S_-$ into $S_+$ and kills $S_+$.

In the algebra the elements are the mixed units:

$$
\vec\Upsilon_x\longmapsto E_{12},\qquad
\vec\Upsilon_y\longmapsto E_{21},
$$

and the two maps are inverse on the two planes, because for $\xi\in S_+$ and $\eta\in S_-$

$$
(\xi\vec\Upsilon_x)\vec\Upsilon_y=\xi(\vec\Upsilon_x\vec\Upsilon_y)=\xi\tilde\Pi_+=\xi,
\qquad
(\eta\vec\Upsilon_y)\vec\Upsilon_x=\eta(\vec\Upsilon_y\vec\Upsilon_x)=\eta\tilde\Pi_-=\eta .
$$

The exchange is a bijection of two planes. It is neither a left multiplication nor an algebra automorphism, and it is not canonical: the normalisation of the mixed basis is free up to the reciprocal scaling of §*Systems of Matrix Units*.

**Peirce index.** Left multiplication preserves each column; right multiplication mixes them. A term that couples the two Peirce copies therefore cannot be a left multiplication. It must be a right multiplication, and the element that performs it is the one carried to an off-diagonal matrix unit.

### The Star

**The star carries a spinor plane to a right Peirce row, not to the other plane.**

The star acts on the plane generated on the left by an idempotent by $(X\tilde\Pi_+)^{*}=\tilde\Pi_+^{*}X^{*}$. The standard pair is Hermitian, $\tilde\Pi_\pm^{*}=\tilde\Pi_\pm$, so

$$
S_+^{*}=\tilde\Pi_+\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_x,
$$

the first row. It is not $S_-$ and it is not a plane closed on the left.

## Summary

The Peirce coordinates of the standard pair are the matrix entries, and the four corner elements are the four matrix units. Trace is the sum of the diagonal corners and determinant is the determinant of the corner matrix. A system of matrix units is a Peirce decomposition with a normalised mixed basis, and it carries a reciprocal $\mathbb{C}^{\times}$ of choices. All systems are conjugate by inner automorphisms, and every nontrivial idempotent is a product of two nilpotents. The two columns are the two spinor planes; left multiplication acts on each by the same matrix, right multiplication by the mixed units exchanges them, and the star carries the first plane to the first row.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | the standard idempotent pair |
| $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$, $\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)$ | the standard nilpotents; $\vec\Upsilon_x=\vec\Upsilon_-$, $\vec\Upsilon_y=\vec\Upsilon_+$ |
| $a_{ij}$ | the Peirce coordinates |
| $E_{ij}$ | the matrix units; $E_{ij}E_{kl}=\delta_{jk}E_{il}$ |
| $\mathsf{M}_2^{Q}$ | the coordinate model attached to the pair |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the two spinor planes, the two columns |
| $\mathcal{C}_+=(\tilde\Pi_+,\vec\Upsilon_y)$, $\mathcal{C}_-=(\vec\Upsilon_x,\tilde\Pi_-)$ | the two couples, bases of the planes |
| $\mathbb{C}^{\times}$ | the reciprocal scaling of the mixed basis |

## Further Reading

- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the corners, the Peirce table and the systems of matrix units
- [Spinors as Peirce Coordinates in the Biquaternion Algebra](spinors-as-peirce-coordinates-in-the-biquaternion-algebra.html), for the two planes, their weight bases and the exchange
- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the fixed model
- [Nilpotents](nilpotents.html), for the nilpotent cone
- [$M_2(\mathbb{C})$ Model : The Eigenbasis and the Diagonalising Matrix](m2c-model-the-eigenbasis-and-the-diagonalising-matrix.html), for the eigenbasis labelling
- [Biquaternion Automorphisms and Derivations](biquaternion-automorphisms-and-derivations.html), for the inner automorphisms
- [Matrix Algebras](matrix-algebras.html), for systems of matrix units
