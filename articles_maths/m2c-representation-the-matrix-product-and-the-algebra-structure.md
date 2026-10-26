# __$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant__

## Introduction

The biquaternion algebra is a complex algebra of dimension four, and the whole of it is visible in the algebra of two-by-two complex matrices. The map is fixed on the basis by

$$
\mathsf{M}_2(e_t)=\mathrm I_2,\qquad
\mathsf{M}_2(\vec e_x)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf{M}_2(\vec e_y)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf{M}_2(\vec e_z)=\begin{pmatrix}-i&0\\0&i\end{pmatrix},
$$

and extended by $\mathbb{C}$-linearity. This article owns the assignment itself and the algebra structure it transports: the product, the unit, the centre, the units and their inverses, and the sense in which the assignment is a choice.

The three matrices are $-i$ times the Pauli matrices. The factor $i$ is forced by $\vec e_k^2=-e_t$, and the signs of the cross-relations are forced by $\vec e_x\vec e_y=\vec e_z$. Both are proved below, and neither is a convention of the representation: they are the algebra read in matrices.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$ and $\vec e_k^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The central scalar is $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ with $B^2=Q_x^2+Q_y^2+Q_z^2$, the scalar of $\tilde Q\tilde Q^{\natural}$. The matrices $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices, and $\epsilon=\mathsf{M}_2(-\vec e_y)=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$.

**Boundaries.** The four forms and the four products are *$M_2(\mathbb{C})$ Representation : The Four Words and the Four Traces*; the trace and the determinant are *$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm*; the Peirce coordinates and the matrix units are *$M_2(\mathbb{C})$ Representation : The Peirce Coordinates and the Matrix Units*; the columns and the spinor module are *$M_2(\mathbb{C})$ Representation : The Columns, the Rows and the Spinor Spaces*. The $4\times4$ regular representation is *Introduction to the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*. The algebra itself is *The Biquaternion Algebra*.

## The Assignment on the Basis

**The four units go to four matrices, and the four coefficients go to one matrix.**

| Unit | Matrix | Square | Determinant |
|---|---|---|---|
| $e_t$ | $\mathrm I_2$ | $\mathrm I_2$ | $1$ |
| $\vec e_x$ | $\begin{pmatrix}0&-i\\-i&0\end{pmatrix}$ | $-\mathrm I_2$ | $1$ |
| $\vec e_y$ | $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ | $-\mathrm I_2$ | $1$ |
| $\vec e_z$ | $\begin{pmatrix}-i&0\\0&i\end{pmatrix}$ | $-\mathrm I_2$ | $1$ |

A general element is therefore

$$
\mathsf{M}_2(\tilde Q)=
\begin{pmatrix}
Q_t-iQ_z&-iQ_x-Q_y\\
-iQ_x+Q_y&Q_t+iQ_z
\end{pmatrix}.
$$

The entries are linear combinations of two coefficients each. The four entries and the four coefficients carry the same data in two arrangements, and the arrangement is fixed by the assignment, not chosen per element.

**The inverse map.** Reading the coefficients back off the matrix,

$$
\mathsf{M}_2^{-1}:\begin{pmatrix}a&b\\c&d\end{pmatrix}\longmapsto
Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,
\qquad
Q_t=\tfrac{a+d}{2},\quad
Q_x=\tfrac{i(b+c)}{2},\quad
Q_y=\tfrac{c-b}{2},\quad
Q_z=\tfrac{i(a-d)}{2}.
$$

The four formulas are the inverse of the four basis matrices, and they are verified by substituting the general matrix.

## The Isomorphism

**Theorem.** The map $\mathsf{M}_2$ is an isomorphism of $\mathbb{C}$-algebras $\mathbb{B}\to M_2(\mathbb{C})$.

*Proof.* The map is $\mathbb{C}$-linear by construction. The three vector images satisfy the quaternion relations:

$$
\mathsf{M}_2(\vec e_x)^2=\mathsf{M}_2(\vec e_y)^2=\mathsf{M}_2(\vec e_z)^2=-\mathrm I_2,\qquad
\mathsf{M}_2(\vec e_x)\mathsf{M}_2(\vec e_y)=\mathsf{M}_2(\vec e_z),
$$

with the two cyclic companions. The first identity is the computation $\begin{pmatrix}0&-i\\-i&0\end{pmatrix}^2=-\mathrm I_2$, and the second is the matrix product. Hence $\mathsf{M}_2$ sends the multiplication table of the four units to the multiplication table of their images. Since the four matrices are linearly independent over $\mathbb{C}$, the map is injective; since both spaces have complex dimension four, it is bijective. Multiplicativity on general elements follows from bilinearity.

**Corollary (the image is everything).** Every two-by-two complex matrix is the image of exactly one biquaternion. The algebra and the matrix algebra are the same ring in two notations.

This is not the case for the split-complex and reduced biquaternion algebras, whose images are proper commutative subalgebras. There the matrix model retains only part of the matrix algebra; here it retains all of it, and every matrix identity is a biquaternion identity.

**Corollary (the centre).** The centre of $\mathbb{B}$ is the line $\mathbb{C}e_t$, and its image is the scalar matrices.

*Proof.* A matrix commuting with every matrix is a scalar matrix, and $\mathsf{M}_2(Q_te_t)=Q_t\mathrm I_2$.

## The Signs and the Pauli Matrices

**The factor $i$ is forced.** A real matrix squaring to $-\mathrm I_2$ is a complex structure; the three images must be three anticommuting complex structures. The assignment uses the Hermitian Pauli matrices multiplied by $-i$:

$$
\mathsf{M}_2(\vec e_k)=-i\sigma_k,\qquad
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

Each $\sigma_k$ is Hermitian and squares to $\mathrm I_2$, so $-i\sigma_k$ squares to $-\mathrm I_2$. The three anticommute, and their products reproduce the quaternion relations with the correct signs. The factor $i$ is not optional: a real matrix squaring to $-\mathrm I_2$ carries no real line to itself, and the complex structure it defines is the multiplication by $i$ that the representation must carry.

**The signs are forced by the cross-relations.** If $\mathsf{M}_2(\vec e_x)$ and $\mathsf{M}_2(\vec e_y)$ are chosen as above, the product is $\mathsf{M}_2(\vec e_z)$, not $-\mathsf{M}_2(\vec e_z)$. The alternative assignment $\vec e_k\mapsto-\mathsf{M}_2(\vec e_k)$ reverses the sign of every vector image and preserves the squares but reverses the cross-products; it is the composition of $\mathsf M_2$ with the anti-automorphism that negates the vector part, so it is an anti-isomorphism, not an algebra isomorphism on the same basis. The sign pattern is therefore determined once the three matrices are fixed, and the three matrices are determined up to conjugation.

**The null-cone basis.** A second family of models comes from the isotropic basis of the null cone, used in *The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation*. In that basis two of the four general products become ordinary matrix products, under the two maps

$$
M=\begin{pmatrix}\xi&\alpha\\\beta&\eta\end{pmatrix},
\qquad
F\longleftrightarrow\begin{pmatrix}f_\alpha&-f_\beta\\-f_\xi&f_\eta\end{pmatrix},
$$

the **outer** product under the first and the **diagonal** product under the second. In this model the images of the null-cone elements are rank-one matrices, square-zero exactly on the pure stratum, rather than Pauli matrices, and the two standard columns are the two coordinate columns. The source also claims a third, the **inner** product; no realization of it was found by exhaustive search, and the claim is not used.

The two maps differ from $\mathsf M_2$ by the change of basis between the isotropic basis and the corpus's basis, so the family is conjugate to the present model by a matrix in $GL_2(\mathbb{C})$, and the conjugating matrix is that change of basis. It is not used in this corpus as the fixed model, but it is the reason the rank-one matrices of *$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety* are the natural image of the null cone.

## The Algebra in Matrix Form

**The product is the matrix product.** For two elements $\tilde Q_1,\tilde Q_2$,

$$
\mathsf{M}_2(\tilde Q_1\tilde Q_2)=\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2),\qquad
\mathsf{M}_2(\tilde Q^n)=\mathsf{M}_2(\tilde Q)^n,\qquad
\mathsf{M}_2(\tilde Q^{-1})=\mathsf{M}_2(\tilde Q)^{-1}.
$$

The third identity holds when either side exists, that is when $\langle\tilde Q\rangle_{\natural}\neq0$.

**The unit and the centre.** The unit is $\mathrm I_2$. A matrix is central exactly when it is scalar, so the centre is $\mathbb{C}e_t$. The scalar matrix $Q_t\mathrm I_2$ is the image of the scalar part, and the traceless part is the image of the vector part.

**Units and inverses.** A biquaternion is a unit exactly when its matrix is invertible, and the inverse is the classical adjugate divided by the determinant:

$$
\mathsf{M}_2(\tilde Q)^{-1}=\frac{\operatorname{adj}\mathsf{M}_2(\tilde Q)}{\det\mathsf{M}_2(\tilde Q)},\qquad
\operatorname{adj}\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.
$$

The identity $\mathsf{M}_2(\tilde Q)\operatorname{adj}\mathsf{M}_2(\tilde Q)=\det\mathsf{M}_2(\tilde Q)\,\mathrm I_2$ is the matrix form of $\tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}e_t$. The adjugate is the image of quaternion conjugation.

**Powers and the exponential.** Powers are matrix powers, and the exponential is the matrix exponential.

## The Structure Map, the Presentation and the Real Form

**The structure map.** The scalars act through

$$
\varphi:\mathbb{C}\longrightarrow Z\bigl(M_2(\mathbb{C})\bigr),\qquad
\varphi(A)=A\mathrm I_2,
$$

whose image is the line of scalar matrices. The scalar action is $M\mapsto AM$, and it is compatible with the product because $A\mathrm I_2$ is central. In the algebra the same map is $\varphi(A)=Ae_t$ of *The Biquaternion Algebra*, §*The Structure Map*; the matrix form shows that its image is exactly the centre.

**The presentation.** The images $X=\mathsf{M}_2(\vec e_x)$ and $Y=\mathsf{M}_2(\vec e_y)$ generate $M_2(\mathbb{C})$ as a $\mathbb{C}$-algebra with unit, because $\vec e_x$ and $\vec e_y$ generate $\mathbb{B}$ and $\mathsf{M}_2$ is an isomorphism. They satisfy

$$
X^2=Y^2=-\mathrm I_2,\qquad XY+YX=0,
$$

and these are the defining relations. The algebra with two generators and those relations is the quaternion algebra over $\mathbb{C}$, of dimension four; the map from it to $M_2(\mathbb{C})$ is nonzero, hence injective because the quaternion algebra is simple, and it is onto for dimension reasons. The matrix reading is that two anticommuting complex structures generate the whole matrix algebra.

**The real form.** Read over $\mathbb{R}$, the algebra $M_2(\mathbb{C})$ has real dimension eight, and

$$
J:M_2(\mathbb{C})\longrightarrow M_2(\mathbb{C}),\qquad J(M)=iM,
$$

is a central complex structure, $J^2=-\mathrm{id}$, commuting with both one-sided multiplications. It is the image of multiplication by the central imaginary $i$ of $\mathbb{B}$, and the complex basis $(\mathrm I_2,-i\sigma_1,-i\sigma_2,-i\sigma_3)$ is the image of the complex basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$; together with $i$ times it, it gives a real basis of the eight real dimensions. The complex algebra and its realification therefore carry the same product; the complex structure is the extra operator that records which real endomorphisms are multiplication by a complex scalar.

**Simple and without division.** The algebra $M_2(\mathbb{C})$ is simple. A nonzero two-sided ideal contains a nonzero matrix $A$; some entry $a_{ij}$ is nonzero, the product $E_{ji}AE_{ij}=a_{ij}E_{jj}$ lies in the ideal, and the matrix units then generate the identity. It is not a division algebra, since $E_{11}E_{22}=0$ with both factors nonzero. This is the matrix form of the central simplicity and the absence of division proved in *The Biquaternion Algebra*, §*Central Simplicity and the Absence of Division*.

## The Choice of Model

**Any two isomorphisms differ by conjugation.** Let $\mathsf{M}_2'$ be another $\mathbb{C}$-algebra isomorphism $\mathbb{B}\to M_2(\mathbb{C})$. Then $T=\mathsf{M}_2'\circ\mathsf{M}_2^{-1}$ is an automorphism of $M_2(\mathbb{C})$, and every automorphism of a full matrix algebra is inner:

$$
T(M)=PMP^{-1},\qquad P\in GL_2(\mathbb{C}).
$$

So the set of models is a single orbit of $GL_2(\mathbb{C})$ acting by conjugation. The fixed model is one representative, chosen so that $\mathsf{M}_2(\vec e_z)$ is diagonal and the two standard diagonal matrix units are fixed. A different choice moves the diagonal axis and the two columns, and it changes which matrix is diagonal, but it does not change the algebra.

**Base change.** A model is a basis of $\mathbb{C}^2$. Let $C\in GL_2(\mathbb{C})$ have as columns the new basis vectors written in the old basis. The matrix of the same element in the new basis is

$$
\mathsf{M}_2^{C}(\tilde Q)=C^{-1}\mathsf{M}_2(\tilde Q)C,
\qquad
\mathsf{M}_2(\tilde Q)=C\,\mathsf{M}_2^{C}(\tilde Q)\,C^{-1}.
$$

This is $T(M)=PMP^{-1}$ with $P=C^{-1}$. Two changes compose,

$$
(C_1C_2)^{-1}M(C_1C_2)=C_2^{-1}\bigl(C_1^{-1}MC_1\bigr)C_2,
$$

so the models form the single orbit described above. The trace and the determinant are unchanged; the columns, the diagonal axis and the entries are not.

**What the choice fixes.** The choice fixes the two columns, the diagonal axis, the matrix $\epsilon$, and the explicit entries of every element. None of these is invariant under conjugation, and none of them is needed to state the algebra. The invariants — the trace and the determinant — are unchanged by the choice, and they are the subject of the articles that follow.

**The matrix model is a change of coordinates.** It adds no relation and loses no information. Its value is that the coordinate statements are matrix statements: the scalar part is a trace, the central scalar is a determinant, invertibility is a nonzero determinant, the zero divisors are the singular matrices, and the two standard columns are the two columns of the model. These are collected in *$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm* and in *$M_2(\mathbb{C})$ Representation : The Columns, the Rows and the Spinor Spaces*.

## Summary

The assignment $\mathsf{M}_2$ sends $e_t$ to $\mathrm I_2$ and the three vector units to $-i\sigma_1,-i\sigma_2,-i\sigma_3$, and extends by linearity. It is an isomorphism of complex algebras, and its image is the whole of $M_2(\mathbb{C})$. The unit is $\mathrm I_2$, the centre is the scalar matrices, units are invertible matrices, and the inverse is the adjugate divided by the determinant. The factor $i$ and the signs of the cross-relations are forced by the quaternion relations. The model is unique up to conjugation by $GL_2(\mathbb{C})$, and the fixed choice is the one in which the standard pair is diagonal.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis; $e_t$ the unit, $\vec e_k^2=-e_t$ |
| $\tilde Q=Q_te_t+\vec Q$ | an element and its scalar–vector split |
| $\mathsf{M}_2$ | the fixed $2\times2$ matrix model |
| $\sigma_1,\sigma_2,\sigma_3$ | the Pauli matrices; $\mathsf{M}_2(\vec e_k)=-i\sigma_k$ |
| $\epsilon=\mathsf{M}_2(-\vec e_y)$ | the matrix $\epsilon$ |
| $Q_t=\tfrac12\operatorname{Tr}\mathsf{M}_2(\tilde Q)$ | the scalar part as half the trace |
| $\operatorname{adj}$ | the classical adjugate, the image of ${}^{\natural}$ |
| $GL_2(\mathbb{C})$ | the group of models, acting by conjugation |

## Further Reading

- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the algebra and its two products
- [$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm](m2c-representation-trace-determinant-and-the-biquaternion-norm.html), for the two invariants
- [$M_2(\mathbb{C})$ Representation : The Peirce Coordinates and the Matrix Units](m2c-representation-the-peirce-coordinates-and-the-matrix-units.html), for the coordinate model
- [$M_2(\mathbb{C})$ Representation : Worked Examples](m2c-representation-worked-examples.html), for the eight matrices computed in the model
- [$M_2(\mathbb{C})$ Representation : The Columns, the Rows and the Spinor Spaces](m2c-representation-the-columns-the-rows-and-the-spinor-spaces.html), for the ideals as columns and rows
- [$M_2(\mathbb{C})$ Representation : The Conjugations and the Adjoints](m2c-representation-the-conjugations-and-the-adjoints.html), for the four involutions
- [Introduction to the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions](m4c-representation-the-matrix-product-and-the-algebra-structure.html), for the regular representation
- [Matrix Algebras](matrix-algebras.html), for the structure of $M_n(\mathbb{C})$
- [The Realification of the General Quaternionic Algebra](the-realification-of-the-general-quaternionic-algebra.html), for the real reading of the complex model
- F. R. Gantmacher, *The Theory of Matrices* (Chelsea, 1959).
