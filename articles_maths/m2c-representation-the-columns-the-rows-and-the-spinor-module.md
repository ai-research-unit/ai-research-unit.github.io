# __$M_2(\mathbb{C})$ Model : Columns, Rows and the Spinor Module__

## Introduction

The matrix model makes the ideal structure of the biquaternion algebra a statement about columns and rows. The two standard minimal left ideals are the two columns, the two standard minimal right ideals are the two rows, and the element acts on a column by matrix multiplication. Every minimal left ideal is a column in a suitable basis, and the family is a projective line. The column is the spinor module: not a space isomorphic to it, but the module itself, realised inside the algebra.

This article develops the column and row picture, the chirality of the two columns, and the module theory that the picture makes visible. It is the matrix form of *The Category of Modules* and of *The Peirce Decomposition*, §*The Decomposition into Minimal Left and Right Ideals* and §*The Lattice of Left Ideals*.

**Conventions.** The algebra and the fixed model are those of *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure*. The standard idempotents are $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$, the standard nilpotents are $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$ and $\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)$, and the matrix units are $E_{ij}$. The two spinor spaces are $S_\pm=\mathbb{B}\tilde\Pi_\pm$.

**Boundaries.** The abstract ideals and the Peirce decomposition are *The Peirce Decomposition*; the module theory is *The Category of Modules*; the matrix units are *$M_2(\mathbb{C})$ Representation : The Peirce Coordinates and the Matrix Units*; the eigenbasis labelling is *$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix*.

## The Left Ideals Are the Columns

**The two columns are two minimal left ideals, the standard ones.**

$$
\mathbb{B}\tilde\Pi_+=\mathbb{C}E_{11}\oplus\mathbb{C}E_{21},\qquad
\mathbb{B}\tilde\Pi_-=\mathbb{C}E_{12}\oplus\mathbb{C}E_{22}.
$$

The first is the set of matrices whose second column vanishes, the second the set whose first column vanishes, and

$$
\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-.
$$

*Proof.* Multiply the general matrix by $E_{11}$ on the right: the result keeps the first column and kills the second. The set of such matrices is $\mathbb{C}E_{11}\oplus\mathbb{C}E_{21}$. The same computation with $E_{22}$ gives the second column. The sum is direct because a matrix with both columns vanishing is zero.

**Minimality.** Each column is a nonzero left ideal containing no nonzero proper left ideal. A nonzero element of the first column has a nonzero first column; multiplying it on the left by a suitable matrix unit selects one of its nonzero entries and produces $E_{11}$ or $E_{21}$, so the ideal it generates is the whole column. The column has complex dimension two and is therefore a simple module.

**The left action is irreducible.** For $M\in M_2(\mathbb{C})$ and a column vector $\xi$, the product $M\xi$ is the left action. No proper subspace of $\mathbb{C}^2$ is stable under all $M$: the matrices $E_{11}$ and $E_{22}$ select the two coordinate lines, and a line stable under both would be one of them, but $E_{12}$ moves each coordinate line to the other. The column is therefore irreducible as a left module.

## The Rows Are the Right Ideals

**The two rows are two minimal right ideals, the standard ones.**

$$
\tilde\Pi_+\mathbb{B}=\mathbb{C}E_{11}\oplus\mathbb{C}E_{12},\qquad
\tilde\Pi_-\mathbb{B}=\mathbb{C}E_{21}\oplus\mathbb{C}E_{22}.
$$

The first is the set of matrices whose second row vanishes, the second the set whose first row vanishes, and

$$
\mathbb{B}=\tilde\Pi_+\mathbb{B}\oplus\tilde\Pi_-\mathbb{B}.
$$

The proof is the transpose of the column proof: multiplication by $E_{11}$ on the left keeps the first row and kills the second.

**The two groupings.** The four matrix units can be grouped by columns or by rows. The column grouping gives the left ideals; the row grouping gives the right ideals. The same four entries carry both structures, and the two groupings are different: the first column and the first row meet in $E_{11}$ and together span a three-dimensional space that is neither a left nor a right ideal. The Peirce table records the four corners, and the two groupings record which pairs of corners are closed on which side.

## Chirality and the Two Columns

**Left multiplication preserves each column.** For any $M$, the products $ME_{11}$ and $ME_{21}$ have vanishing second column, and $ME_{12}$ and $ME_{22}$ have vanishing first column. No left multiplication relates the two columns. This is the matrix statement that a left ideal is stable on the left.

**Right multiplication by $E_{12}$ exchanges the columns.** The product $ME_{12}$ has zero first column and second column equal to the first column of $M$:

$$
M E_{12}=\begin{pmatrix}0&M_{11}\\0&M_{21}\end{pmatrix}.
$$

It maps the first column onto the second and annihilates the second column. In the algebra, the element is $\vec\Upsilon_x$:

$$
\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)\longmapsto E_{12},
$$

and right multiplication by $\vec\Upsilon_x$ maps $S_+=\mathbb{B}\tilde\Pi_+$ onto $S_-=\mathbb{B}\tilde\Pi_-$ and kills $S_-$.

**The mass term must be a right multiplication.** A term that couples the two chiralities cannot be a left multiplication, because a left multiplication preserves each column. It must be a right multiplication, and the element that performs it is the one carried to an off-diagonal matrix unit. This is the structural reason the biquaternionic Dirac equation couples the chiralities on the right. The spinor module, not the whole algebra, is the carrier of the Dirac field, and the right action of $\vec\Upsilon_x$ is the coupling.

**The exchange is not an algebra automorphism.** Right multiplication by $E_{12}$ is not invertible and not an automorphism; it is a module map from $S_+$ to $S_-$ composed with the zero map on $S_-$. The two columns are isomorphic as left modules, and the isomorphism is right multiplication by a suitable element, but it is not canonical: it depends on the choice of the off-diagonal unit.

## The Spinor Module

**The defining module.** The left module $S=\mathbb{B}\tilde\Pi_+$ is the **spinor module**. As a complex vector space it is $\mathbb{C}^2$, with basis $(\tilde\Pi_+,\vec\Upsilon_y)$; a spinor of first chirality is

$$
\xi_+=Q_{11}\tilde\Pi_++Q_{21}\vec\Upsilon_y,
$$

with coordinates $(Q_{11},Q_{21})$ and matrix representative the first column $\begin{pmatrix}Q_{11}\\Q_{21}\end{pmatrix}$.

**The second chirality.** The module $S_-=\mathbb{B}\tilde\Pi_-$ has basis $(\vec\Upsilon_x,\tilde\Pi_-)$ and a spinor of second chirality is

$$
\xi_-=Q_{12}\vec\Upsilon_x+Q_{22}\tilde\Pi_-,
$$

with coordinates $(Q_{12},Q_{22})$ and matrix representative the second column.

**The two modules are isomorphic.** The map $\xi_+\mapsto\xi_+u$ with $u$ a unit carrying $\tilde\Pi_+$ to $\tilde\Pi_-$ is an isomorphism of left modules. The isomorphism is not unique: the stabiliser of $\tilde\Pi_+$ acts on the right, and the reciprocal scaling of the nilpotents changes the map. The two chiralities are therefore the same module in two copies, and the copy is a choice.

**The endomorphisms.** By Schur's lemma, the endomorphisms of the simple module $S$ are the scalars:

$$
\operatorname{End}_{\mathbb{B}}(S)=\mathbb{C}.
$$

In the matrix model an endomorphism of the column is a matrix commuting with every $M$, hence a scalar matrix; the scalar is the value by which the centre acts. The right action of the centre on $S$ is this scalar action, and it is the only right action that survives.

**The regular module.** As a left module,

$$
\mathbb{B}=S_+\oplus S_-,\qquad S_+\cong S_-\cong S,
$$

so the regular module is $S\oplus S$. It is free of rank one, because it is $\mathbb{B}$ itself, and it is not simple, because it is the direct sum of the two columns. It is projective because it is free; and it is a generator, because every simple module is a quotient of it. These are the properties collected in *The Category of Modules*, §*The Four Properties of the Regular Object*.

**Morita equivalence.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is Morita equivalent to $\mathbb{C}$. The equivalence sends the simple module $S$ to $\mathbb{C}$ and the algebra to the matrix algebra of the module. It is the reason the module theory of $\mathbb{B}$ is the module theory of a field, read through a two-dimensional space: the categories of left modules are equivalent, and the equivalence is not an isomorphism of algebras.

## The Endomorphisms of the Regular Module

**Right multiplications.** For $X\in M_2(\mathbb{C})$ let $R_X$ be right multiplication, $R_X(M)=MX$. It is a map of left $M_2(\mathbb{C})$-modules, because

$$
R_X(NM)=(NM)X=N(MX)=N R_X(M),
$$

and every left-module endomorphism of $M_2(\mathbb{C})$ is of this form: the image of $\mathrm I_2$ is $X$, and left linearity gives $T(M)=T(M\mathrm I_2)=MT(\mathrm I_2)=MX$. The assignment is an algebra isomorphism

$$
M_2(\mathbb{C})^{\mathrm{op}}\longrightarrow
\operatorname{End}_{M_2(\mathbb{C})}\bigl(M_2(\mathbb{C})\bigr),
\qquad X\longmapsto R_X,
$$

with composition $R_XR_Y=R_{YX}$. Composing with the transpose identifies the endomorphism ring with $M_2(\mathbb{C})$ itself, because

$$
R_{X^{\mathsf T}}R_{Y^{\mathsf T}}=R_{(XY)^{\mathsf T}}.
$$

This is the matrix form of $\operatorname{End}_{\mathbb{B}}({}_{\mathbb{B}}\mathbb{B})\cong\mathbb{B}^{\mathrm{op}}$ of *The Category of Modules*, §*The Endomorphisms of the Regular Object*.

**The bimodule endomorphisms.** An endomorphism that is also right $M_2(\mathbb{C})$-linear satisfies $T(M)=T(\mathrm I_2M)=T(\mathrm I_2)M$, while left linearity gives $T(M)=MT(\mathrm I_2)$. Hence $T(\mathrm I_2)$ is central, and the bimodule endomorphisms are the scalar multiplications:

$$
\operatorname{End}_{M_2-M_2}\bigl(M_2(\mathbb{C})\bigr)\cong\mathbb{C}.
$$

In the algebra this is the centre $\mathbb{C}e_t$, and the statement is that the regular bimodule has no non-scalar endomorphisms.

**The two columns.** The left ideal $I_{L_\infty}=\mathbb{C}\{E_{11},E_{21}\}$ consists of the matrices whose image lies in the first coordinate line. Right multiplication replaces the two columns by combinations of themselves, so the image remains in that line; the left action therefore preserves the ideal. A left ideal is a submodule of the regular left module, while right multiplication is an endomorphism of it.

## The Lattice of Left Ideals

**Every minimal left ideal is a column in some basis.** A minimal left ideal of $\mathbb{B}$ is $\mathbb{B}\tilde\Pi$ for a primitive idempotent $\tilde\Pi$, and every primitive idempotent is conjugate to $\tilde\Pi_+$. Conjugating the standard column by the unit that carries $\tilde\Pi_+$ to $\tilde\Pi$ gives the ideal. The set of minimal left ideals is therefore the set of conjugates of one column.

**The projective line.** In the matrix model a minimal left ideal is the set of matrices whose rows lie in a fixed line $L$ of the dual space; equivalently, after a change of basis adapted to $L$, it is one of the two columns. The line $L$ is a point of the projective line $\mathbb{P}^1(\mathbb{C})$, and the minimal left ideals are parametrised by that line. The two standard columns correspond to the two coordinate lines of the dual. Two ideals coincide exactly when the lines coincide. The right ideals are the same construction with the column space in place of the row space, and their projective line is the dual one.

**The lattice.** The left ideals of $\mathbb{B}$ are $0$, the minimal left ideals, and $\mathbb{B}$. There are no intermediate left ideals, because the algebra is of length two. The lattice is therefore a projective line with a bottom and a top adjoined; the minimal elements are the points of $\mathbb{P}^1(\mathbb{C})$, and the whole lattice is the set of subspaces of a two-dimensional space, read as left ideals.

**The right ideals.** The same statements hold on the right, with the column space in place of the row space and the dual projective line in place of the primal one. The left and right lattices are isomorphic but not canonically identified: an identification is a choice of a system of matrix units.

## Summary

The columns of the matrix model are the two standard minimal left ideals, and the rows are the two standard minimal right ideals. Each column is a simple left module of complex dimension two, the spinor module; the two columns are isomorphic, and the isomorphism is a choice. Left multiplication preserves each column, so chirality-changing terms must act on the right; the off-diagonal unit $E_{12}$ performs the exchange. The endomorphisms of the spinor module are the scalars, the regular module is $S\oplus S$, and the algebra is Morita equivalent to $\mathbb{C}$. The minimal left ideals are the points of $\mathbb{P}^1(\mathbb{C})$, and the two columns are the two coordinate points.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the standard minimal left ideals, the two columns |
| $\tilde\Pi_\pm\mathbb{B}$ | the standard minimal right ideals, the two rows |
| $E_{ij}$ | the matrix units |
| $S=\mathbb{B}\tilde\Pi_+$ | the spinor module, $\mathbb{C}^2$ |
| $\operatorname{End}_{\mathbb{B}}(S)=\mathbb{C}$ | the endomorphisms of the spinor module |
| $\mathbb{P}^1(\mathbb{C})$ | the lattice of minimal left ideals |
| $E_{12}=\mathsf{M}_2(\vec\Upsilon_x)$ | the exchange of the two columns |

## Further Reading

- [Modules over the Biquaternion Algebra](modules-over-the-biquaternion-algebra.html), for the regular module and Morita equivalence
- [Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the ideals and the lattice
- [$M_2(\mathbb{C})$ Representation : The Peirce Coordinates and the Matrix Units](m2c-representation-the-peirce-coordinates-and-the-matrix-units.html), for the corner coordinates
- [$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix](m2c-representation-the-eigenbasis-and-the-diagonalising-matrix.html), for the eigenbasis columns
- [Modules over the Biquaternion Algebra](modules-over-the-biquaternion-algebra.html), for the abstract spinor module
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the action on spinors
- [Matrix Algebras](matrix-algebras.html), for the module theory of $M_n(\mathbb{C})$
