# __Matrix Representations Conventions__

## Introduction

The algebra is read in matrices in three ways, and the three answer different questions. The **axis-free representation** reads multiplication in the basis the algebra already carries, and writes the two operators $L^{\mathrm{axf}}(\tilde Q)$ and $R^{\mathrm{axf}}(\tilde Q)$; it needs no frame, its entries are the structure constants, and it is the display the body of the physics articles prints. The **Pauli representation** reads the same two operators in the Peirce frame of the standard pair; it costs the choice of a direction and buys the $2\times2$ block, the five-cell Clifford frame and the gamma matrices. The **$2\times2$ isomorphism** $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ reads the element itself as a complex matrix of the algebra's own size; it is not a regular representation at all, and it is the block from which the Pauli display is built.

The order of the article is that order, and it is the order of the mathematical article of the same name. The axis-free display comes first because it follows from the multiplication table alone, with nothing chosen. The Pauli display comes second because it needs the standard pair, and once it is written the switch between the two frames is one matrix and its inverse, §*The Switch Between the Two Frames*. The $2\times2$ isomorphism comes last because it is the algebra and not an operator on it, and it is read best after both $4\times4$ displays have shown what a matrix of an operator is. The rule that keeps the two legacy formulations out of every body section is stated before all three, in §*The Rule on Pauli and Gamma Matrices*.

**Three displays, two objects.** The two $4\times4$ displays are one operator in two bases: the same four-dimensional subalgebra $\mathbb{B}_L$ of the ambient $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, written twice. The $2\times2$ display is a different object, the algebra itself. A change of frame never changes the operator, and it never touches the $2\times2$ image, because that image carries no frame.

**The order renames nothing.** The corpus calls the Peirce frame the canonical frame, and this article keeps the name: the word names the frame, not its position here. The axis-free frame is the coefficient basis read as a frame, and its label is $\mathrm{axf}$. The physics articles of the series print $\mathrm{axf}$; the Peirce arrays are kept because they are the ones the gamma literature prints, and they are the second display, not the first.

**The algebra is $M_2(\mathbb{C})$, and it is never $M_4(\mathbb{C})$.** The ambient $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ is the operator algebra, it carries no biquaternion structure and takes no biquaternion name; the left and right copies are named $\mathbb{B}_L$ and $\mathbb{B}_R$, and the retired label $M_4(\mathbb{C})_L$ is read as $\mathbb{B}_L$.

The article assumes the base of *Algebra and Element Conventions*, the products of *Product and Form Conventions*, and the two coordinate frames of *Frame Conventions*, whose $\mathbb{B}$ and $\mathbb{M}_-$ readings the contractions below use. The Peirce convention is that of *Special Element and Peirce Conventions*, whose standard pair fixes the Pauli frame.

## The Rule on Pauli and Gamma Matrices

**The rule.** No Pauli matrix and no gamma matrix is written in the body of an article. The two formulations are legacy, and they appear in two places only: in a legacy section of an article, and in this article, which states them once so that a legacy section has something to refer to.

**What the rule forbids.** The arrays $\sigma_k$ and $\gamma_\mu$. A symbol built on them and used as an object of the algebra, such as $\gamma_5$ or $\sigma_3$. A sentence that reads a biquaternion off such an array by name.

**What the rule allows.** The names of the frames. The Pauli frame and the gamma frame are bases and not arrays, and the names stay. A reference to a legacy section stays, and so does a historical remark inside one.

**The replacement.** The cells. $L_aR_b$ writes an operator, $L^{\mathrm{axf}}$ and $R^{\mathrm{axf}}$ write a display in the axis-free frame, and $\mathsf{V}^{\mathrm{vol}}=-iL_{e_t}R_{\vec e_z}$ writes the chirality operator of a frame. Every array the rule forbids has a cell that says the same thing and names no axis.

**The test.** Open the article at a body section and read the symbols. A sigma or a gamma in a body section is a violation. The display is replaced by its cells before the article is published, and the array moves to the legacy section if it is worth keeping.

**Why this is a rule and not a taste.** An array carries a frame, a dimension and a signature inside a symbol, and the sentence that prints it does not say so. A cell carries none of the three. That is the defect stated in full in *Why AXF Matrices instead of Pauli and Gamma Matrices*, and it is the reason the two formulations are kept as a record and not used as a language.

## The Matrix Models

**Two kinds of matrix model read the algebra.** The **isomorphism** $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ reads the element itself as a $2\times2$ complex matrix, of the algebra's own size. The **regular representation** reads multiplication as a linear map on the algebra taken as a complex vector space; its target is $\mathrm{End}_{\mathbb{C}}(\mathbb{B})=M_4(\mathbb{C})$, and its image is a four-dimensional subspace $\mathbb{B}_L$ of that ambient algebra, not the ambient algebra. The two are different representations, not two sizes of one, and only $\mathsf{M}_2$ is an isomorphism of the algebra onto matrices of its own size.

**The matrices are the matrices of operators.** An array of this article is the matrix of a $\mathbb{C}$-linear operator of $\mathbb{B}$ read in a frame; the operator is the object, and the array is one display of it. The two elementary operators are the multiplications $L_{\tilde Q}$ and $R_{\tilde P}$ of *Operator and Calculus Conventions*, and their product is the **two-sided operator** of *Two-Sided Operators on the Biquaternion Algebra*,
$$
L_{\tilde Q}R_{\tilde P}:\mathbb{B}\longrightarrow\mathbb{B},
\qquad
L_{\tilde Q}R_{\tilde P}(X)=\tilde Q\,X\,\tilde P,
$$
whose matrix in a frame is the product of the two regular matrices of that frame,
$$
\mathsf{M}_{4L}(\tilde Q)\,\mathsf{M}_{4R}(\tilde P).
$$
Both families and their products are written here because the object displayed is an operator of that family, and the matrix is what a computation multiplies.

**The sixteen cells are the sixteen basis operators.** The pair $(\mu,\nu)$ names the basis two-sided operator $e_\mu[\,]e_\nu$, $X\mapsto e_\mu Xe_\nu$, and its matrix is the cell $L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}}$ in the axis-free frame and $L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}$ in the Peirce one. The sixteen cells are the matrices of a basis: by the generation theorem of that article, §*The Sixteen Products as a Basis*, they are linearly independent and they span the ambient $\operatorname{End}_{\mathbb{C}}(\mathbb{B})=M_4(\mathbb{C})$, of complex dimension sixteen. Every operator of $\mathbb{B}$ is a complex combination of the sixteen cells, and the sixteen coefficients are its coordinates in that basis.

**The coefficients of a two-sided operator are an outer product.** Expanding in the cells,
$$
L_{\tilde Q}R_{\tilde P}=\sum_{\mu,\nu}Q_\mu P_\nu\,L_{e_\mu}R_{e_\nu},
\qquad
c\bigl(L_{\tilde Q}R_{\tilde P}\bigr)=QP^{\mathsf T},
$$
so the coefficient array $c(T)$ of the operator, in the basis of the sixteen cells, has rank one and its length is $\ell(T)=\operatorname{rank}c(T)=1$. A general operator has $1\le\ell\le4$; a sum of two products is one product exactly when the two outer products add to a rank-one array; and the linear space of the sixteen coefficients is the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$, the cell $L_{e_\mu}R_{e_\nu}$ being the image of $e_\mu\otimes e_\nu^{\mathrm{opp}}$.

| object | writing | meaning |
|---|---|---|
| the algebra | $\mathbb{B}$ | $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ |
| the ambient | $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ | operators on the algebra as a vector space |
| the left copy | $\mathbb{B}_L=M_4(\mathbb{C})_{\mathbb{B}_L}=\rho_L(\mathbb{B})$ | four-dimensional subalgebra |
| the right copy | $\mathbb{B}_R=M_4(\mathbb{C})_{\mathbb{B}_R}=\rho_R(\mathbb{B})$ | the commutant of $\mathbb{B}_L$ |
| the isomorphism | $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | the element read as a $2\times2$ matrix |
| the axis-free matrix | $\mathsf{M}_{4L}^{\mathrm{axf}}(\tilde Q)$, $\mathsf{M}_{4R}^{\mathrm{axf}}(\tilde Q)$ | the regular matrices in the coefficient basis, written $L^{\mathrm{axf}}(\tilde Q)$, $R^{\mathrm{axf}}(\tilde Q)$ |
| the Pauli matrix | $\mathsf{M}_{4L}^{\mathrm{pau}}(\tilde Q)$, $\mathsf{M}_{4R}^{\mathrm{pau}}(\tilde Q)$ | the regular matrices in the Peirce frame, written $L^{\mathrm{pau}}(\tilde Q)$, $R^{\mathrm{pau}}(\tilde Q)$ |

The subscript names the copy: $M_4(\mathbb{C})_{\mathbb{B}_L}$ is the left copy, $M_4(\mathbb{C})_{\mathbb{B}_R}$ the right, and $M_4(\mathbb{C})_{\mathbb{B}_L,\mathbb{B}_R}$ both. A bare $M_4(\mathbb{C})$ is the ambient. The two cones are written $M_4(\mathbb{C})_{\mathcal{T}}$ for the two-sided operators and $M_4(\mathbb{C})_{\Theta}$ for the sandwiches, whose names are in *Conventions of the Operator Families*.

**The subscript names the action, not a tensor slot.** $L$ is left multiplication and $R$ is right multiplication, read as on $L_{\tilde Q}$ and $R_{\tilde Q}$ in *Operator and Calculus Conventions*, §*The Operators*. In the Peirce frame the left copy happens to be the second tensor factor and the right copy the first, and another frame exchanges the two slots without exchanging the two actions. A subscript naming a slot would therefore change meaning with the frame, and the action does not.

### General Matrix Conventions

**A matrix carries no tilde, and the ban is absolute.** The tilde marks an element of the algebra, not its image. The identity is $I_n$, with $\mathsf{M}_2(e_t)=I_2$ and $\mathsf{M}_{4L}(e_t)=I_4$, and the image of an element is written $\mathsf{M}_2(\tilde Q)$ or $\mathsf{M}_{4L}(\tilde Q)$, with the tilde inside the argument. **An array of biquaternions carries no tilde either.** A matrix whose entries are biquaternions is written $\mathsf{Q}=(\tilde Q_{\lambda\rho})\in\mathbb{B}^{n\times m}$: the tildes sit on the entries, and the array that holds them has none, whatever its size and whatever its entries. The identity matrix never takes a tilde; nor do the regular matrices $\mathsf{M}_{4L}$ and $\mathsf{M}_{4R}$, whose subscript gives the size first and the side of the multiplication second. The same ban covers a matrix of biquaternions and a colour matrix.

**The ban is on the array, not on its argument.** The writings $\mathsf{M}_2(\tilde Q)$ and $\mathsf{M}_{4L}(\tilde Q)$ are correct because the tilde stays inside the argument. A tilde on the array — $\tilde I_n$, $\tilde{\mathsf{M}}_2$, $\tilde{\mathcal Q}$, or $\tilde Q$ where the matrix $\mathsf{M}_2(\tilde Q)$ is meant — is forbidden and is a defect to be rewritten, not a variant to be read: no object is behind it, and the element it would name is already named by the argument.

**The letter $M$ belongs to matrices.** It names a matrix and nothing else: the images $\mathsf{M}_2(\tilde Q)$ and $\mathsf{M}_{4L}(\tilde Q)$, the matrix algebras $M_2(\mathbb{C})$ and $M_4(\mathbb{C})$, and an entrywise matrix in a proof. No element of the algebra is written $M$, with or without a tilde.

**The copy is named, the ambient is not.** The left copy is $\mathbb{B}_L=\rho_L(\mathbb{B})$, also written $M_4(\mathbb{C})_{\mathbb{B}_L}$, and the right copy is $\mathbb{B}_R=\rho_R(\mathbb{B})$, also written $M_4(\mathbb{C})_{\mathbb{B}_R}$. Each is a subalgebra of $M_4(\mathbb{C})$ isomorphic to $M_2(\mathbb{C})$, and each is the commutant of the other. $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ is the ambient operator algebra and is never called a biquaternion algebra. The writing $M_4(\mathbb{C})_L$, read as the name of an algebra, is retired and is read here as $M_4(\mathbb{C})_{\mathbb{B}_L}$; the same holds on the right.

**The frame label names the display.** $\mathsf{M}_{4L}$ names the operator and carries no frame. The array of that operator is written with the frame in the caret, $L^{\mathrm{axf}}(\tilde Q)$ and $L^{\mathrm{pau}}(\tilde Q)$, or with the frame named in the sentence; an array of no named frame is not written. A bare $\mathsf{M}_4$ is written for neither the operator's family nor the frame. The two symbols $L_{e_\mu}$ and $L_{e_\mu}^{\mathrm{axf}}$ are the multiplication and its matrix, and they are separated by the frame label alone.

## The $M_4(\mathbb{C})$ Axis-Free Representation

**The reading.** The $4\times4$ reading is the regular representation, and it answers a different question from the $2\times2$ isomorphism: it reads an element as the operator of multiplication on the algebra taken as a complex vector space. Left multiplication is $\rho_L:\mathbb{B}\to\mathrm{End}_{\mathbb{C}}(\mathbb{B})=M_4(\mathbb{C})$,
$$
\rho_L(\tilde Q_1)(\tilde Q_2)=\tilde Q_1\tilde Q_2,
$$
and right multiplication is $\rho_R(\tilde Q_1)(\tilde Q_2)=\tilde Q_2\tilde Q_1$. The image is the four-dimensional subspace $\mathbb{B}_L=\rho_L(\mathbb{B})$ of the ambient $M_4(\mathbb{C})$, not the ambient algebra, and likewise $\mathbb{B}_R$ on the right. Each copy is a subalgebra isomorphic to $M_2(\mathbb{C})$, and each is the commutant of the other.

**The basis is the one the algebra carries.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, and its basis is the tensor basis of *Algebra and Element Conventions*, §*The Algebra and Its Basis*,
$$
e_t=1\otimes1,\qquad \vec e_x=1\otimes\vec e_x,\qquad \vec e_y=1\otimes\vec e_y,\qquad \vec e_z=1\otimes\vec e_z,
$$
the vector units on the right being those of $\mathbb{H}$, and the scalar imaginary $i=i\otimes1$ being central and occurring only as a coefficient. The four are a $\mathbb{C}$-basis, and the element is
$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad Q_\mu=q_\mu+iq'_\mu,
$$
the developed form of *Algebra and Element Conventions*, §*The Element, the Coordinates and the Conjugations*. This basis is called the **coefficient basis**, because its four coordinates are the coefficients of the developed form, and it is called **axis-free**, because no one of the three vector directions enters by a rule of its own.

**The multiplication table.** Every matrix below is read from this table and from nothing else:

| $e_\mu e_\nu$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

Each of the sixteen products is $\pm$ one of the four basis elements, and the signs are those of the quaternion algebra, $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$. No complex number appears in the table, because $i$ is central and is carried by the coefficients. In the compact form,
$$
e_\mu e_\nu=\sum_\rho\varepsilon_{\mu\nu}^{\ \ \rho}\,e_\rho,\qquad
\varepsilon_{\mu\nu}^{\ \ \rho}\in\{0,+1,-1\},
$$
and the array $\varepsilon$ is the algebra: the table is that array written out.

**Why this frame is first, and why the physics articles print it.** The construction uses the multiplication of the algebra and nothing else: no idempotent is chosen, no direction is singled out, no root is fixed. The display is therefore unique once the basis is, and the basis is the one the algebra comes with. That is why it is the first display of the article, and why a computation that must not favour an axis starts here. The physics articles of the series print it for the same reason: a formula of general physics distinguishes no spatial direction, and a display that distinguishes one would carry a datum the formula does not contain. *Why AXF Matrices instead of Pauli and Gamma Matrices* makes that argument in full.

**The label.** Write $L^{\mathrm{axf}}(\tilde Q)$ and $L_{e_\mu}^{\mathrm{axf}}$, and $R^{\mathrm{axf}}(\tilde Q)$ and $R_{e_\mu}^{\mathrm{axf}}$. The label is a name in lowercase roman letters, like $\mathrm{opp}$ and $\mathrm{fop}$, not an exponent: $L_{\vec e_x}^{\mathrm{axf}}$ is the left matrix of $\vec e_x$, and its square is written $(L_{\vec e_x}^{\mathrm{axf}})^2$. The label is carried by the family and not by the entry, because the frame is a property of the carrier and the side is a property of the action.

### The Left Family

**The definition.** The $\nu$-th column of the left matrix is the coordinate column of the product $\tilde Qe_\nu$,
$$
L^{\mathrm{axf}}(\tilde Q)_{\mu\nu}=\bigl[\tilde Qe_\nu\bigr]_{\mu},\qquad
L^{\mathrm{axf}}(\tilde Q):=\bigl(\bigl[\tilde Qe_t\bigr]\;\bigl[\tilde Q\vec e_x\bigr]\;\bigl[\tilde Q\vec e_y\bigr]\;\bigl[\tilde Q\vec e_z\bigr]\bigr),
$$
which is the definition of *Element and Operator Representations: The Three Actions*, §*The Two Sides*, read in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$. The four matrices of the units are $L_{e_\mu}^{\mathrm{axf}}:=L^{\mathrm{axf}}(e_\mu)$.

**The display.** For $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$,
$$
L^{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&-Q_z&Q_y\\
Q_y&Q_z&Q_t&-Q_x\\
Q_z&-Q_y&Q_x&Q_t
\end{pmatrix}.
$$
The first column is $(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$, the coordinate column of $\tilde Q$ itself, because $\tilde Qe_t=\tilde Q$. The other three columns are the products of $\tilde Q$ with the three vector units, one rule applied to the other three columns of the table.

**The four left matrices.** On the units,
$$
L_{e_t}^{\mathrm{axf}}=\mathrm I_4,\qquad
L_{\vec e_x}^{\mathrm{axf}}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
$$
$$
L_{\vec e_y}^{\mathrm{axf}}=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
L_{\vec e_z}^{\mathrm{axf}}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$
Each is a column of the multiplication table written as an array: the $z$ matrix has $-1$ where the table sends $e_t\mapsto\vec e_z$, $\vec e_y\mapsto-\vec e_x$, $\vec e_z\mapsto-e_t$ and $\vec e_x\mapsto\vec e_y$.

**Signed permutations.** Each of the four is a signed permutation matrix: exactly one nonzero entry in each row and in each column, of modulus one, hence orthogonal with entries in $\{0,+1,-1\}$. Each has determinant $1$; the identity has trace $4$ and the three vector matrices have trace $0$. The four are linearly independent, since the assignment is injective and the four units are a basis, so they are a basis of $\mathbb{B}_L$.

**The group.** The four matrices together with their negatives are eight distinct signed permutation matrices forming a group isomorphic to the quaternion group $Q_8$: the vector matrices square to $-\mathrm I_4$, distinct ones anticommute up to sign, and the identity is the unit. The left family of this frame is a copy of $Q_8$ inside $O(4)\subset M_4(\mathbb{R})$.

**The law.** For all $\tilde Q_1,\tilde Q_2$,
$$
L^{\mathrm{axf}}(\tilde Q_1\tilde Q_2)=L^{\mathrm{axf}}(\tilde Q_1)L^{\mathrm{axf}}(\tilde Q_2),
$$
which is associativity and nothing else: the $\nu$-th column of the left side is the coordinate column of $(\tilde Q_1\tilde Q_2)e_\nu=\tilde Q_1(\tilde Q_2e_\nu)$, and the $\nu$-th column of the right side is $\tilde Q_1$ applied to the coordinate column of $\tilde Q_2e_\nu$. The first column recovers $\tilde Q$, so the assignment is injective, and its image is the four-dimensional complex subalgebra $\mathbb{B}_L$ of $M_4(\mathbb{C})$ whose unit is $\mathrm I_4$.

**The transpose is the conjugation.** In this frame,
$$
L^{\mathrm{axf}}(\tilde Q)^{\mathsf T}=L^{\mathrm{axf}}(\tilde Q^{\natural}),\qquad
\tilde Q^{\natural}=Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z,
$$
because transposing swaps the $(\mu,\nu)$ and the $(\nu,\mu)$ entries, and those two carry opposite signs exactly when $s_\mu s_\nu=-1$, with $s_t=1$ and $s_x=s_y=s_z=-1$; multiplying the three vector coefficients by $-1$ produces that sign pattern. The dagger gives the star conjugate, $L^{\mathrm{axf}}(\tilde Q)^{\dagger}=L^{\mathrm{axf}}(\tilde Q^{*})$, because the entrywise conjugate of the display is the display of the element with $\overline{Q_\mu}$ in place of $Q_\mu$. Both identities are properties of this frame and not of the operator: the Peirce frame has neither, §*The Two Tensor Factors*.

### The Right Family

**The definition.** The $\nu$-th column of the right matrix is the coordinate column of $\vec e_\nu\tilde Q$,
$$
R^{\mathrm{axf}}(\tilde Q)_{\mu\nu}=\bigl[\vec e_\nu\tilde Q\bigr]_{\mu},\qquad
R^{\mathrm{axf}}(\tilde Q):=\bigl(\bigl[e_t\tilde Q\bigr]\;\bigl[\vec e_x\tilde Q\bigr]\;\bigl[\vec e_y\tilde Q\bigr]\;\bigl[\vec e_z\tilde Q\bigr]\bigr),
$$
the same construction with the order of the two factors exchanged.

**The display.**
$$
R^{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&Q_z&-Q_y\\
Q_y&-Q_z&Q_t&Q_x\\
Q_z&Q_y&-Q_x&Q_t
\end{pmatrix}.
$$
The two displays agree on the diagonal, in the first row and in the first column, and differ in the sign of the six entries whose two indices are both vector. That is the difference between a left and a right multiplication, and it is a difference of six signs.

**The four right matrices.** On the units,
$$
R_{e_t}^{\mathrm{axf}}=\mathrm I_4,\qquad
R_{\vec e_x}^{\mathrm{axf}}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},
$$
$$
R_{\vec e_y}^{\mathrm{axf}}=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
R_{\vec e_z}^{\mathrm{axf}}=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$
Each is a signed permutation matrix of determinant $1$ and trace $4\delta_{\mu t}$, and the four are a basis of $\mathbb{B}_R$.

**The law is reversed.** For all $\tilde Q_1,\tilde Q_2$,
$$
R^{\mathrm{axf}}(\tilde Q_1\tilde Q_2)=R^{\mathrm{axf}}(\tilde Q_2)R^{\mathrm{axf}}(\tilde Q_1),
$$
because associativity turns $\vec e_\nu(\tilde Q_1\tilde Q_2)$ into $(\vec e_\nu\tilde Q_1)\tilde Q_2$, so the columns compose in the reverse order. Powers and inverses are not reversed, since they involve one element only: $R^{\mathrm{axf}}(\tilde Q^n)=R^{\mathrm{axf}}(\tilde Q)^n$ and $R^{\mathrm{axf}}(\tilde Q^{-1})=R^{\mathrm{axf}}(\tilde Q)^{-1}$. The products of the unit matrices follow the reverse order too, $R_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}}=R_{e_\nu e_\mu}^{\mathrm{axf}}$, so $R_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=-R_{\vec e_z}^{\mathrm{axf}}$, the opposite sign to the left family.

**The two families commute.** For all $\tilde Q_1,\tilde Q_2$,
$$
L^{\mathrm{axf}}(\tilde Q_1)R^{\mathrm{axf}}(\tilde Q_2)=R^{\mathrm{axf}}(\tilde Q_2)L^{\mathrm{axf}}(\tilde Q_1),
$$
because the two factors sit on opposite sides of the argument and never meet. The two families meet in the scalars: $L^{\mathrm{axf}}(\tilde Q)=R^{\mathrm{axf}}(\tilde Q)$ says that $\tilde Q$ commutes with every element, that is $\tilde Q\in\mathbb{C}e_t$, and then the common matrix is $\lambda\mathrm I_4$.

### The Stitch Between the Two Families

**The general rule.** In any frame the right matrix is the transpose of the left one between the switch matrix and its inverse,
$$
R(\tilde Q)=\mathsf W^{-1}L(\tilde Q)^{\mathsf T}\mathsf W,
$$
where $\mathsf W$ is the Gram matrix of the symmetric form $\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y)$ on the frame (*Element and Operator Representations: The Three Actions*, §*The Two Sides*).

**The switch of this frame.** On the four units, $\beta(e_\mu,e_\nu)=\operatorname{Sc}(e_\mu e_\nu)$ is $+1$ on $e_t$, $-1$ on the three vector units and $0$ off the diagonal, so
$$
\mathsf W=D=\operatorname{diag}(1,-1,-1,-1),
\qquad
R^{\mathrm{axf}}(\tilde Q)=D\,L^{\mathrm{axf}}(\tilde Q)^{\mathsf T}D,
\qquad
D=D^{\mathsf T}=D^{-1}.
$$
The same array $D$ is the sign vector $\varepsilon$ of the products: the transpose dictionary and the metric of the plain product are one object here. This is the cheapest stitch in the corpus, and it is the reason the transpose is the conjugation above. It is also the reason the metric sign vector of the $\mathbb{M}_-$ frame appears in a statement about matrices: $D$ is that sign vector, and no second array is introduced for it.

**The switch matrix, written out.** It is its own transpose and its own inverse,
$$
D=\begin{pmatrix}1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&0&-1\end{pmatrix},
\qquad
D^{\mathsf T}=D,
\qquad
D^{-1}=D .
$$
Entrywise the stitch reads
$$
\bigl(R^{\mathrm{axf}}(\tilde Q)\bigr)_{ij}=d_i\,d_j\,\bigl(L^{\mathrm{axf}}(\tilde Q)\bigr)_{ji},
\qquad d_1=1,\quad d_2=d_3=d_4=-1,
$$
so transposing already writes $R$ except in the bottom-right $3\times3$ block, and the two factors of $D$ negate that block and only that block. On the general element the two displays of §*The Left Family* and §*The Right Family* differ in exactly those six entries, and on the unit $\vec e_x$ the computation is
$$
D\,\bigl(L_{\vec e_x}^{\mathrm{axf}}\bigr)^{\mathsf T}D
=\begin{pmatrix}1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&0&-1\end{pmatrix}
\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}
\begin{pmatrix}1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&0&-1\end{pmatrix}
=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}
=R_{\vec e_x}^{\mathrm{axf}} .
$$
The four matrix displays of the two families are the same arrays read in the two ways, and nothing in the algebra is changed by the choice.

**The invariants.** The trace and the determinant are
$$
\operatorname{tr}L^{\mathrm{axf}}(\tilde Q)=4Q_t,\qquad
\det L^{\mathrm{axf}}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^{2},
$$
and the same values hold for $R$, since the stitch changes neither a trace nor a determinant. They are the values of the operator, not of the frame.

### The Sixteen Products in This Frame

**They are real.** The sixteen products $L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}}$ are real signed permutation matrices: four entries $\pm1$, one in each row and each column, of determinant $1$, of Hilbert–Schmidt norm two, and mutually orthogonal. Their entries are the structure constants themselves, so the product table of the algebra and the multiplication of the sixteen arrays are one table.

**The sixteen, one by one.** Each is a signed permutation matrix, with four entries $\pm1$, and each is written here with both factors named:

$$
L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}
$$

$$
L_{e_t}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}
$$

$$
L_{\vec e_x}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}
$$

$$
L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix},\qquad
L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\-1&0&0&0\\0&-1&0&0\end{pmatrix}
$$

$$
L_{\vec e_y}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix}
$$

$$
L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&-1&0\\0&0&0&1\end{pmatrix},\qquad
L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=\begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&-1&0\end{pmatrix}
$$

$$
L_{\vec e_z}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix},\qquad
L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=\begin{pmatrix}0&0&1&0\\0&0&0&-1\\1&0&0&0\\0&-1&0&0\end{pmatrix}
$$

$$
L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=\begin{pmatrix}0&-1&0&0\\-1&0&0&0\\0&0&0&-1\\0&0&-1&0\end{pmatrix},\qquad
L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix}
$$

**The product closes on the cell.** They multiply by multiplying the left factors together and the right factors together,
$$
L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}}\,L_{e_\rho}^{\mathrm{axf}}R_{e_\sigma}^{\mathrm{axf}}
=L_{e_\mu e_\rho}^{\mathrm{axf}}R_{e_\sigma e_\nu}^{\mathrm{axf}},
$$
which is again a cell, so the sixteen span a sixteen-dimensional algebra: the whole ambient $M_4(\mathbb{C})$, as §*The Clifford Structure* reads it.

**The sixteen cells, named on the units.** Each cell acts on the basis as a signed permutation, so the four images of $(e_t,\vec e_x,\vec e_y,\vec e_z)$ carry the whole array, and the sixteen pairs are read off the arrays above:

| cell | images of $(e_t,\vec e_x,\vec e_y,\vec e_z)$ | cell | images of $(e_t,\vec e_x,\vec e_y,\vec e_z)$ |
|---|---|---|---|
| $L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | $(e_t,\vec e_x,\vec e_y,\vec e_z)$ | $L_{\vec e_y}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | $(\vec e_y,-\vec e_z,-e_t,\vec e_x)$ |
| $L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ | $(\vec e_x,-e_t,-\vec e_z,\vec e_y)$ | $L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ | $(-\vec e_z,-\vec e_y,-\vec e_x,-e_t)$ |
| $L_{e_t}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | $(\vec e_y,\vec e_z,-e_t,-\vec e_x)$ | $L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | $(-e_t,\vec e_x,-\vec e_y,\vec e_z)$ |
| $L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | $(\vec e_z,-\vec e_y,\vec e_x,-e_t)$ | $L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | $(\vec e_x,e_t,-\vec e_z,-\vec e_y)$ |
| $L_{\vec e_x}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | $(\vec e_x,-e_t,\vec e_z,-\vec e_y)$ | $L_{\vec e_z}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | $(\vec e_z,\vec e_y,-\vec e_x,-e_t)$ |
| $L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ | $(-e_t,-\vec e_x,\vec e_y,\vec e_z)$ | $L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ | $(\vec e_y,-\vec e_z,e_t,-\vec e_x)$ |
| $L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | $(\vec e_z,-\vec e_y,-\vec e_x,e_t)$ | $L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | $(-\vec e_x,-e_t,-\vec e_z,-\vec e_y)$ |
| $L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | $(-\vec e_y,-\vec e_z,-e_t,-\vec e_x)$ | $L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | $(-e_t,\vec e_x,\vec e_y,-\vec e_z)$ |

A column records where one basis unit goes, so the table is the multiplication table read column by column: the first column of $L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}}$, for instance, is the coordinate column of $e_\mu e_\nu$.

**The same sixteen cells in the Pauli frame.** A cell is an operator and does not change with the frame: the pair $(\mu,\nu)$ names one basis two-sided operator $e_\mu[\,]e_\nu$ in both displays, so the sixteen cells correspond one to one and index for index,
$$
L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}}\;\longleftrightarrow\;L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}},
\qquad \mu,\nu\in\{t,x,y,z\},
$$
and the coefficients $Q_\mu P_\nu$ of a two-sided operator are the same sixteen numbers in both frames. Only the arrays differ: here real signed permutations, in the Peirce frame complex arrays with entries in $\{0,\pm1,\pm i\}$. §*The Switch Between the Two Frames* writes the sixteen expressions one by one, each an equality of the Pauli cell with its axis-free partner conjugated, and §*The Legacy Pauli Gamma Formulation* reads the same sixteen as the products of the five frame cells.

**The cost.** No $2\times2$ block appears, no Peirce idempotent is visible, and the sixteen arrays are all of one kind, so no five of them are singled out. The frame that gives the transpose dictionary takes away the block and the gamma frame; the next sections buy them back.

**No gamma set is chosen here.** In the Peirce display the five frame cells are selected by hand from the sixteen products, and that selection is what writes a Clifford algebra and a gamma map that look like the printed ones. In the axis-free display the sixteen products are all real signed permutations of determinant $1$, and no five of them are marked out: the gamma map is a choice of frame, not a structure of the algebra. The metric sign vector $\varepsilon$ and the substitution $Q_t=ict'$ on the material sector are untouched by a change of frame, because a change of frame is a change of display.

**The index is written low in both frames.** The label of a frame cell is the coordinate index of its left multiplier, written low as in $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$, and the index is never raised or lowered, in either frame.

**The two articles of the frame.** *$M_4(\mathbb{C})$ Axis-Free Representation* gives the matrices, the product, the trace, the determinant and the six subspaces as matrix conditions; *$M_4(\mathbb{C})$ Axis-Free Representation : Operators* gives the operators at the three levels, the sixteen cells and the coefficient matrix.

## The $M_4(\mathbb{C})$ Pauli Representation

**A second frame, and what it buys.** The same two operators are displayed in the Peirce frame of the standard pair. The frame is a choice, and it is the choice the matrix literature makes: it is the frame in which the left matrix is a $2\times2$ block matrix, in which every cell is a Kronecker product of two $2\times2$ matrices, and in which five of them are the gamma matrices. Its label is $\mathrm{pau}$, and its arrays are the ones the gamma literature prints, so a reader who compares with a textbook compares arrays and not only operators.

**Its cost.** The frame singles out one direction through the idempotents, and that direction is the root $\vec\Xi=i\vec e_z$ of *Special Element and Peirce Conventions*, §*The Root*. The two mixed units pair $\vec e_x$ with $\vec e_y$ and leave $\vec e_z$ in the idempotents. The axis-free frame has no root and no block, and this frame has both. A statement about the algebra depends on neither, because the two displays are one operator, $L^{\mathrm{axf}}(\tilde Q)=C_{\Pi}L^{\mathrm{pau}}(\tilde Q)C_{\Pi}^{-1}$ with $C_{\Pi}$ of §*The Switch Between the Two Frames*.

### The Peirce Frame

**The two idempotents and the two mixed units.** The standard pair is
$$
\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z),\qquad
\tilde\Pi_+^2=\tilde\Pi_+,\quad \tilde\Pi_-^2=\tilde\Pi_-,\quad \tilde\Pi_+\tilde\Pi_-=0,\quad \tilde\Pi_++\tilde\Pi_-=e_t,
$$
and its two mixed units are
$$
\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y),\qquad
\vec\Upsilon_\pm^2=0,\quad \vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\quad \vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+ .
$$
So $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ is a Peirce basis, and the frame is that basis in that order: the two elements of $\mathbb{B}\tilde\Pi_+$ first and those of $\mathbb{B}\tilde\Pi_-$ second. The Peirce convention fixes no family (*Special Element and Peirce Conventions*, §*The Biquaternion Peirce Convention*); the choice here is not a preferred pair, it is the frame this display is written in, and the corpus calls it the canonical frame.

**The frame vectors over the basis.** Written in the coefficient basis, the four frame vectors are
$$
\tilde\Pi_+=\tfrac12\bigl(e_t+i\vec e_z\bigr),\qquad
\vec\Upsilon_+=\tfrac12\bigl(i\vec e_x+\vec e_y\bigr),\qquad
\vec\Upsilon_-=\tfrac12\bigl(i\vec e_x-\vec e_y\bigr),\qquad
\tilde\Pi_-=\tfrac12\bigl(e_t-i\vec e_z\bigr),
$$
so each is a combination of two units and the switch is two $2\times2$ blocks, as §*The Switch Between the Two Frames* writes it out.

### The Two Tensor Factors

**The Pauli matrices.** The $4\times4$ arrays of this frame are built from three $2\times2$ matrices, and they are fixed here once:
$$
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$
They are Hermitian, traceless, of determinant $-1$ and of square $I_2$, and they multiply by
$$
\sigma_1\sigma_2=i\sigma_3,\qquad \sigma_2\sigma_3=i\sigma_1,\qquad \sigma_3\sigma_1=i\sigma_2,
\qquad
\sigma_1\sigma_2\sigma_3=iI_2,
$$
so $\sigma_j\sigma_k=-\sigma_k\sigma_j$ for $j\ne k$ and $\{\sigma_j,\sigma_k\}=2\delta_{jk}I_2$. The image of the algebra is their complex linear combination,
$$
\mathsf{M}_2(\tilde Q)=Q_tI_2-i\bigl(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3\bigr)
=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix},
$$
and every $4\times4$ array of this frame is a Kronecker product of these three with $I_2$ or with each other. That is why each $4\times4$ display carries the same $2\times2$ arrays twice, and why the four left matrices below are read as $-i\sigma_k$ repeated in the two diagonal blocks, the four right ones as $-i\sigma_k^{\mathsf T}$ multiplying the four blocks of $I_2$.

**The left matrix.** In the Peirce frame the left matrix of $\tilde Q$ is the $2\times2$ matrix taken twice,
$$
\mathsf{M}_{4L}^{\mathrm{pau}}(\tilde Q)=L^{\mathrm{pau}}(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q),
$$
so its four blocks are $\mathsf{M}_2(\tilde Q)$, $0$, $0$, $\mathsf{M}_2(\tilde Q)$. The first factor is the multiplicity and the second the matrix of the element.

**The four left matrices.** Each is the image of a unit,
$$
L_{e_t}^{\mathrm{pau}}=\mathsf{M}_{4L}(e_t)=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
L_{\vec e_x}^{\mathrm{pau}}=\mathsf{M}_{4L}(\vec e_x)=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},
$$
$$
L_{\vec e_y}^{\mathrm{pau}}=\mathsf{M}_{4L}(\vec e_y)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
L_{\vec e_z}^{\mathrm{pau}}=\mathsf{M}_{4L}(\vec e_z)=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix},
$$
each equal to $I_2\otimes\mathsf{M}_2(\vec e_k)$, with $\mathsf{M}_2(\vec e_k)=-i\sigma_k$:
$$
L_{e_t}^{\mathrm{pau}}=\operatorname{diag}\bigl(I_2,I_2\bigr),\qquad
L_{\vec e_x}^{\mathrm{pau}}=\operatorname{diag}\bigl(-i\sigma_1,-i\sigma_1\bigr),\qquad
L_{\vec e_y}^{\mathrm{pau}}=\operatorname{diag}\bigl(-i\sigma_2,-i\sigma_2\bigr),\qquad
L_{\vec e_z}^{\mathrm{pau}}=\operatorname{diag}\bigl(-i\sigma_3,-i\sigma_3\bigr).
$$
The visible structure of the four arrays is the structure of the three Pauli matrices: $L_{\vec e_z}^{\mathrm{pau}}$ is diagonal because $\sigma_3$ is, $L_{\vec e_x}^{\mathrm{pau}}$ and $L_{\vec e_y}^{\mathrm{pau}}$ are off the diagonal inside each block because $\sigma_1$ and $\sigma_2$ are, and the factor $i$ is what makes each square $-I_4$. A general element is their linear combination,
$$
\mathsf{M}_{4L}(\tilde Q)=Q_tL_{e_t}^{\mathrm{pau}}+Q_xL_{\vec e_x}^{\mathrm{pau}}+Q_yL_{\vec e_y}^{\mathrm{pau}}+Q_zL_{\vec e_z}^{\mathrm{pau}}=I_2\otimes\mathsf{M}_2(\tilde Q).
$$

**The four right matrices.** Right multiplication is the transpose of left multiplication in the exchanged frame. Let $\mathsf S$ be the linear involution of the carrier that fixes the two idempotents and exchanges the two mixed Peirce units,
$$
\mathsf S\tilde\Pi_\pm=\tilde\Pi_\pm,\qquad
\mathsf S\vec\Upsilon_+=\vec\Upsilon_-,\qquad
\mathsf S\vec\Upsilon_-=\vec\Upsilon_+,
$$
the permutation of the second and third canonical coordinates. Its matrix there is
$$
\mathsf S=\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{pmatrix},
$$
symmetric and involutive, $\mathsf S^{\mathsf T}=\mathsf S=\mathsf S^{-1}$, of trace $2$ and determinant $-1$; in the coefficient basis the same operator is the reflection $\operatorname{diag}(1,1,-1,1)$, which fixes $e_t,\vec e_x,\vec e_z$ and negates $\vec e_y$. It is a linear involution of the carrier, not an algebra map, not one of the sixteen cells and not a one-sided multiplication. Then
$$
\mathsf M_{4R}(\tilde Q)=\mathsf S\,\mathsf M_{4L}(\tilde Q)^{\mathsf T}\mathsf S^{-1},\qquad
R_{e_\nu}^{\mathrm{pau}}=\mathsf S\,{L_{e_\nu}^{\mathrm{pau}}}^{\mathsf T}\,\mathsf S^{-1},
\qquad
\mathsf{M}_{4R}^{\mathrm{pau}}(\tilde Q)=R^{\mathrm{pau}}(\tilde Q)=\mathsf{M}_2(\tilde Q)^{\mathsf T}\otimes I_2 .
$$
Explicitly,
$$
R_{e_t}^{\mathrm{pau}}=\mathsf{M}_{4R}(e_t)=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
R_{\vec e_x}^{\mathrm{pau}}=\mathsf{M}_{4R}(\vec e_x)=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix},
$$
$$
R_{\vec e_y}^{\mathrm{pau}}=\mathsf{M}_{4R}(\vec e_y)=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
R_{\vec e_z}^{\mathrm{pau}}=\mathsf{M}_{4R}(\vec e_z)=\begin{pmatrix}-i&0&0&0\\0&-i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix}.
$$

**The same Pauli matrices, in the other slot.** The right matrices are
$$
R_{\vec e_k}^{\mathrm{pau}}=\mathsf{M}_2(\vec e_k)^{\mathsf T}\otimes I_2=\bigl(-i\sigma_k^{\mathsf T}\bigr)\otimes I_2,\qquad
R_{e_t}^{\mathrm{pau}}=I_2\otimes I_2=\operatorname{diag}(I_2,I_2),
$$
so the entry $\bigl(-i\sigma_k^{\mathsf T}\bigr)_{rc}$ of the $2\times2$ matrix multiplies the block $I_2$ sitting in the $(r,c)$ place. The exchange of the two factors is not a transposition of the array: it moves the Pauli matrix from the diagonal blocks to the block-scaling role, and its blocks become multiples of $I_2$ instead of $I_2$-multiples of the same $2\times2$ array.

**The Pauli form of the two families.** With $\mathsf M_2(\vec e_k)=-i\sigma_k$,
$$
L_{e_t}^{\mathrm{pau}}=I_2\otimes I_2,\qquad
L_{\vec e_k}^{\mathrm{pau}}=-i\,I_2\otimes\sigma_k,\qquad
R_{e_t}^{\mathrm{pau}}=L_{e_t}^{\mathrm{pau}},\qquad
R_{\vec e_x}^{\mathrm{pau}}=-i\,\sigma_1\otimes I_2,\quad
R_{\vec e_y}^{\mathrm{pau}}=+i\,\sigma_2\otimes I_2,\quad
R_{\vec e_z}^{\mathrm{pau}}=-i\,\sigma_3\otimes I_2 .
$$
The plus on $R_{\vec e_y}^{\mathrm{pau}}$ is the transpose: $\sigma_2^{\mathsf T}=-\sigma_2$, while $\sigma_1$ and $\sigma_3$ are symmetric, so the right matrix carries $-i\sigma_k$ on $x$ and $z$ and $+i\sigma_k$ on $y$. The Pauli line is the evaluation of the $L$-based definition, never its replacement.

**What the exchange does, case by case.** $\sigma_1$ and $\sigma_2$ have zero diagonal, so $R_{\vec e_x}^{\mathrm{pau}}$ and $R_{\vec e_y}^{\mathrm{pau}}$ have both diagonal blocks zero and their two off-diagonal blocks equal to $-iI_2$. $\sigma_3$ is diagonal, so the two matrices differ only in the order of four diagonal entries,
$$
L_{\vec e_z}^{\mathrm{pau}}=\operatorname{diag}(-i,\,i,\,-i,\,i),\qquad
R_{\vec e_z}^{\mathrm{pau}}=\operatorname{diag}(-i,\,-i,\,i,\,i),
$$
which is the exchange written on the diagonal: the left array repeats $-i,i$ twice, the right array repeats $-i$ twice and then $i$ twice. The transposition itself leaves $R_{\vec e_x}^{\mathrm{pau}}$ and $R_{\vec e_z}^{\mathrm{pau}}$ as the exchange alone would give them, because $\sigma_1$ and $\sigma_3$ are symmetric, and it swaps the two off-diagonal blocks of $R_{\vec e_y}^{\mathrm{pau}}$ because $\sigma_2$ is antisymmetric: $\sigma_2^{\mathsf T}=-\sigma_2$.

**The laws and the invariants.** Both families obey the laws of the axis-free frame, with the same side conventions,
$$
L^{\mathrm{pau}}(\tilde Q_1\tilde Q_2)=L^{\mathrm{pau}}(\tilde Q_1)L^{\mathrm{pau}}(\tilde Q_2),\qquad
R^{\mathrm{pau}}(\tilde Q_1\tilde Q_2)=R^{\mathrm{pau}}(\tilde Q_2)R^{\mathrm{pau}}(\tilde Q_1),\qquad
L^{\mathrm{pau}}(\tilde Q_1)R^{\mathrm{pau}}(\tilde Q_2)=R^{\mathrm{pau}}(\tilde Q_2)L^{\mathrm{pau}}(\tilde Q_1),
$$
and the trace and determinant are the same numbers, $\operatorname{tr}L^{\mathrm{pau}}(\tilde Q)=4Q_t$ and $\det L^{\mathrm{pau}}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^2$, because they are properties of the operator. The dagger is the star conjugate, $L^{\mathrm{pau}}(\tilde Q)^{\dagger}=L^{\mathrm{pau}}(\tilde Q^{*})$. Transposition is not the conjugation in this frame: with the exchange it gives the other family, $R^{\mathrm{pau}}(\tilde Q)=\mathsf S L^{\mathrm{pau}}(\tilde Q)^{\mathsf T}\mathsf S^{-1}$, and the conjugation reads $L^{\mathrm{pau}}(\tilde Q^{\natural})=2Q_t\mathrm I_4-L^{\mathrm{pau}}(\tilde Q)$, which is a linear expression in the element and no transpose at all. The transpose is the conjugation in the axis-free frame alone, §*The Stitch Between the Two Families*.

**The block form of the element.** Since $\mathsf{M}_2(\tilde Q)=\begin{pmatrix}a&b\\ c&d\end{pmatrix}$ with
$$
a=Q_t-iQ_z,\qquad b=-iQ_x-Q_y,\qquad c=-iQ_x+Q_y,\qquad d=Q_t+iQ_z,
$$
the left matrix is
$$
L^{\mathrm{pau}}(\tilde Q)=\begin{pmatrix}a&b&0&0\\ c&d&0&0\\0&0&a&b\\0&0&c&d\end{pmatrix},
$$
so the algebra acts on each Peirce component by the same $2\times2$ matrix, and the two components never mix. This is the block the $2\times2$ display names, §*The $2\times2$ Pauli Representation*.

**The zero block is the point.** Every entry linking an index in $\{1,2\}$ to one in $\{3,4\}$ vanishes for every element. The Peirce frame does not block an arbitrary operator; it blocks the left copy $\mathbb{B}_L$, and the vanishing is the statement that left multiplication preserves the two Peirce components.

### The Sixteen Cells in the Peirce Frame

**The sixteen cells, entry by entry.** The cells multiply left multipliers with left multipliers and right with right,
$$
L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}\,L_{e_\rho}^{\mathrm{pau}}R_{e_\sigma}^{\mathrm{pau}}
=L_{e_\mu e_\rho}^{\mathrm{pau}}R_{e_\sigma e_\nu}^{\mathrm{pau}},
$$
so each cell is fixed by its left unit $e_\mu$ and its right unit $e_\nu$, and the four left matrices and the four right matrices generate all sixteen. In blocks of $2\times2$,
$$
L_{e_t}^{\mathrm{pau}}=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
L_{\vec e_x}^{\mathrm{pau}}=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
L_{\vec e_y}^{\mathrm{pau}}=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
L_{\vec e_z}^{\mathrm{pau}}=\begin{pmatrix}-i&0\\0&i\end{pmatrix},
$$
$$
R_{e_t}^{\mathrm{pau}}=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
R_{\vec e_x}^{\mathrm{pau}}=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
R_{\vec e_y}^{\mathrm{pau}}=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
R_{\vec e_z}^{\mathrm{pau}}=\begin{pmatrix}-i&0\\0&i\end{pmatrix},
$$
each a $2\times2$ block repeated twice, $I_2\otimes\mathsf{M}_2(e_\mu)=\operatorname{diag}\bigl(\mathsf{M}_2(e_\mu),\mathsf{M}_2(e_\mu)\bigr)$ for the left matrices and $\mathsf{M}_2(e_\nu)^{\mathsf T}\otimes I_2=\operatorname{diag}\bigl(\mathsf{M}_2(e_\nu)^{\mathsf T},\mathsf{M}_2(e_\nu)^{\mathsf T}\bigr)$ for the right ones.

**The sixteen cells are Kronecker products.** Combining the two tensor forms,
$$
L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}=\bigl(I_2\otimes\mathsf{M}_2(e_\mu)\bigr)\bigl(\mathsf{M}_2(e_\nu)^{\mathsf T}\otimes I_2\bigr)
=\mathsf{M}_2(e_\nu)^{\mathsf T}\otimes\mathsf{M}_2(e_\mu),
$$
so each cell is a Kronecker product: the right unit's matrix, transposed, in the first slot, and the left unit's matrix in the second. The left factor fixes the second slot and the right factor the first, and the cell is the pair $(\mu,\nu)$ read in the two slots:

| cell | $\mathsf{M}_2(e_\nu)^{\mathsf T}\otimes \mathsf{M}_2(e_\mu)$ | cell | $\mathsf{M}_2(e_\nu)^{\mathsf T}\otimes \mathsf{M}_2(e_\mu)$ |
|---|---|---|---|
| $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ | $I_2\otimes I_2$ | $L_{\vec e_y}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ | $I_2\otimes \mathsf{M}_2(\vec e_y)$ |
| $L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ | $\mathsf{M}_2(\vec e_x)^{\mathsf T}\otimes I_2$ | $L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ | $\mathsf{M}_2(\vec e_x)^{\mathsf T}\otimes \mathsf{M}_2(\vec e_y)$ |
| $L_{e_t}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ | $\mathsf{M}_2(\vec e_y)^{\mathsf T}\otimes I_2$ | $L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ | $\mathsf{M}_2(\vec e_y)^{\mathsf T}\otimes \mathsf{M}_2(\vec e_y)$ |
| $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ | $\mathsf{M}_2(\vec e_z)^{\mathsf T}\otimes I_2$ | $L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ | $\mathsf{M}_2(\vec e_z)^{\mathsf T}\otimes \mathsf{M}_2(\vec e_y)$ |
| $L_{\vec e_x}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ | $I_2\otimes \mathsf{M}_2(\vec e_x)$ | $L_{\vec e_z}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ | $I_2\otimes \mathsf{M}_2(\vec e_z)$ |
| $L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ | $\mathsf{M}_2(\vec e_x)^{\mathsf T}\otimes \mathsf{M}_2(\vec e_x)$ | $L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ | $\mathsf{M}_2(\vec e_x)^{\mathsf T}\otimes \mathsf{M}_2(\vec e_z)$ |
| $L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ | $\mathsf{M}_2(\vec e_y)^{\mathsf T}\otimes \mathsf{M}_2(\vec e_x)$ | $L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ | $\mathsf{M}_2(\vec e_y)^{\mathsf T}\otimes \mathsf{M}_2(\vec e_z)$ |
| $L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ | $\mathsf{M}_2(\vec e_z)^{\mathsf T}\otimes \mathsf{M}_2(\vec e_x)$ | $L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ | $\mathsf{M}_2(\vec e_z)^{\mathsf T}\otimes \mathsf{M}_2(\vec e_z)$ |

All sixteen are invertible, of rank four and of Hilbert–Schmidt norm two, because $\lVert X\otimes Y\rVert_{\mathrm{HS}}=\lVert X\rVert_{\mathrm{HS}}\lVert Y\rVert_{\mathrm{HS}}$ and every $\mathsf{M}_2(e_\mu)$ has norm $\sqrt2$; the only one of trace $4$ is $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=I_4$, and the other fifteen have trace $0$.

**The sixteen, one by one.** Written out in full:

$$
L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix}
$$

$$
L_{e_t}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=\begin{pmatrix}-i&0&0&0\\0&-i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix}
$$

$$
L_{\vec e_x}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},\qquad
L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix}
$$

$$
L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=\begin{pmatrix}0&0&0&-i\\0&0&-i&0\\0&i&0&0\\i&0&0&0\end{pmatrix},\qquad
L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=\begin{pmatrix}0&-1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}
$$

$$
L_{\vec e_y}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix}
$$

$$
L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&1&0&0\\-1&0&0&0\end{pmatrix},\qquad
L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=\begin{pmatrix}0&i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&i&0\end{pmatrix}
$$

$$
L_{\vec e_z}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix},\qquad
L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\-1&0&0&0\\0&1&0&0\end{pmatrix}
$$

$$
L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=\begin{pmatrix}0&0&-i&0\\0&0&0&i\\i&0&0&0\\0&-i&0&0\end{pmatrix},\qquad
L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix}
$$

Each has four nonzero entries, one in each row and each column, and in this display the nonzero entries are $\pm1$ or $\pm i$; each is invertible, of determinant $1$, of Hilbert–Schmidt norm $2$, and the sixteen are mutually orthogonal. In the axis-free display the same sixteen are real signed permutations, which is the plainest statement about them: the complex entries are a property of this display alone.

### The Pauli Form

**The Pauli form.** The matrices $I_2\otimes\mathsf{M}_2(\tilde Q)$ and $\mathsf{M}_2(\tilde Q)^{\mathsf T}\otimes I_2$ are the two tensor forms of the same element. The first reads the element on the left, the second on the right, and the exchange $\mathsf S$ is the difference between them:
$$
\mathsf{M}_2(\tilde Q)^{\mathsf T}\otimes I_2=\mathsf S\,\bigl(I_2\otimes\mathsf{M}_2(\tilde Q)^{\mathsf T}\bigr)\mathsf S^{-1}
=\mathsf S\,\bigl(I_2\otimes\mathsf{M}_2(\tilde Q)\bigr)^{\mathsf T}\mathsf S^{-1}.
$$
The five frame cells of this display, their products and their Clifford reading are in §*The Clifford Structure* and §*The Legacy Pauli Gamma Formulation*.

**No entry is read without the frame.** Another gauge or another order of the four basis elements gives another matrix of the same operator; the block formula holds in this display alone, and it is the reason the display is kept: the $2\times2$ image taken twice is what a reader of the matrix literature recognises. The mathematics articles of the corpus are written in this display unless they name the coefficient basis, and the physics articles are written in the axis-free one; $C_{\Pi}$ carries the one to the other. The copy and the element are what the frame does not change.

## The Switch Between the Two Frames

**One matrix, and its inverse.** The two frames are two bases of the same four-dimensional vector space, so the two displays of one operator are related by one change of matrix. Write $C_{\Pi}$ for the matrix whose columns are the coordinates of the frame vectors in the coefficient basis,
$$
C_{\Pi}=\tfrac12\begin{pmatrix}1&0&0&1\\0&i&i&0\\0&1&-1&0\\i&0&0&-i\end{pmatrix},
$$
the columns being $\tilde\Pi_+$, $\vec\Upsilon_+$, $\vec\Upsilon_-$, $\tilde\Pi_-$ in the order $(e_t,\vec e_x,\vec e_y,\vec e_z)$. Then for every element and every side,
$$
\boxed{\;L^{\mathrm{axf}}(\tilde Q)=C_{\Pi}\,L^{\mathrm{pau}}(\tilde Q)\,C_{\Pi}^{-1},\qquad
R^{\mathrm{axf}}(\tilde Q)=C_{\Pi}\,R^{\mathrm{pau}}(\tilde Q)\,C_{\Pi}^{-1}\;}
$$
and inversely $L^{\mathrm{pau}}(\tilde Q)=C_{\Pi}^{-1}L^{\mathrm{axf}}(\tilde Q)C_{\Pi}$, $R^{\mathrm{pau}}(\tilde Q)=C_{\Pi}^{-1}R^{\mathrm{axf}}(\tilde Q)C_{\Pi}$. The reason is one line: the $\nu$-th column of a regular matrix is the coordinate column of a product, and a change of basis rewrites every coordinate column by the same matrix. Neither side changes, and both displays change by the same conjugation. The direction is the one used throughout the series: the axis-free display is the one on the left of the equality and the Peirce display is its conjugate, so a formula written in $\mathrm{axf}$ and a formula written in $\mathrm{pau}$ are carried into each other without a second convention.

**The inverse.** The inverse is
$$
C_{\Pi}^{-1}=\begin{pmatrix}1&0&0&-i\\0&-i&1&0\\0&-i&-1&0\\1&0&0&i\end{pmatrix}=2C_{\Pi}^{\dagger},
$$
so $C_{\Pi}^{\dagger}C_{\Pi}=\tfrac12\mathrm I_4$ and the change is a scaled unitary, not a unitary. Its determinant is $-\tfrac14$: the frame vectors are not normalised to modulus one, and no normalisation is imposed, because the frame is the Peirce basis and not an orthonormal basis.

**Two $2\times2$ blocks.** In $2\times2$ blocks over the splitting $(1,2)\mid(3,4)$,
$$
C_{\Pi}=\tfrac12\begin{pmatrix}
\begin{pmatrix}1&0\\0&i\end{pmatrix}&\begin{pmatrix}0&1\\i&0\end{pmatrix}\\[2pt]
\begin{pmatrix}0&1\\i&0\end{pmatrix}&\begin{pmatrix}-1&0\\0&-i\end{pmatrix}
\end{pmatrix},
\qquad
C_{\Pi}^{-1}=\begin{pmatrix}
\begin{pmatrix}1&0\\0&-i\end{pmatrix}&\begin{pmatrix}0&1\\-i&0\end{pmatrix}\\[2pt]
\begin{pmatrix}0&1\\-i&0\end{pmatrix}&\begin{pmatrix}-1&0\\0&i\end{pmatrix}
\end{pmatrix},
$$
and the two off-diagonal blocks are equal in each matrix: the switch does not mix the two Peirce components independently, it pairs them symmetrically. The block form is what makes the switch two $2\times2$ computations and not one $4\times4$ one.

**The eight unit matrices.** Apply the switch to each unit matrix, using $C_{\Pi}L_{e_\mu}^{\mathrm{axf}}C_{\Pi}^{-1}=L_{e_\mu}^{\mathrm{pau}}$ and $C_{\Pi}R_{e_\mu}^{\mathrm{axf}}C_{\Pi}^{-1}=R_{e_\mu}^{\mathrm{pau}}$. In the axis-free frame the four left matrices are real signed permutations and the four right ones are real signed permutations, and after the switch,
$$
L_{e_t}^{\mathrm{axf}}\mapsto L_{e_t}^{\mathrm{pau}}=\mathrm I_4,\qquad
L_{\vec e_x}^{\mathrm{axf}}\mapsto L_{\vec e_x}^{\mathrm{pau}},\qquad
L_{\vec e_y}^{\mathrm{axf}}\mapsto L_{\vec e_y}^{\mathrm{pau}},\qquad
L_{\vec e_z}^{\mathrm{axf}}\mapsto L_{\vec e_z}^{\mathrm{pau}},
$$
$$
R_{e_t}^{\mathrm{axf}}\mapsto R_{e_t}^{\mathrm{pau}}=\mathrm I_4,\qquad
R_{\vec e_x}^{\mathrm{axf}}\mapsto R_{\vec e_x}^{\mathrm{pau}},\qquad
R_{\vec e_y}^{\mathrm{axf}}\mapsto R_{\vec e_y}^{\mathrm{pau}},\qquad
R_{\vec e_z}^{\mathrm{axf}}\mapsto R_{\vec e_z}^{\mathrm{pau}},
$$
with the eight displays of §*The Two Tensor Factors*. The identity is the identity in both frames, and the seven others change. The two families agree on the identity and nowhere else, as they must: $L^{\mathrm{pau}}(\tilde Q)=R^{\mathrm{pau}}(\tilde Q)$ forces $\tilde Q\in\mathbb{C}e_t$.

**The sixteen cells, cell by cell.** The switch carries the cells one by one, and each cell of the Pauli frame is the conjugate of the cell of the same index in the axis-free frame. The sixteen expressions follow, and in each the Pauli cell stands on the left, the conjugation of the axis-free cell stands in the middle, and the computed Pauli array stands on the right:
$$
L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}
$$

$$
L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix}
$$

$$
L_{e_t}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{e_t}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix}
$$

$$
L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}-i&0&0&0\\0&-i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix}
$$

$$
L_{\vec e_x}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{\vec e_x}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix}
$$

$$
L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix}
$$

$$
L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}0&0&0&-i\\0&0&-i&0\\0&i&0&0\\i&0&0&0\end{pmatrix}
$$

$$
L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}0&-1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}
$$

$$
L_{\vec e_y}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{\vec e_y}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}
$$

$$
L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix}
$$

$$
L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&1&0&0\\-1&0&0&0\end{pmatrix}
$$

$$
L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}0&i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&i&0\end{pmatrix}
$$

$$
L_{\vec e_z}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{\vec e_z}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix}
$$

$$
L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\-1&0&0&0\\0&1&0&0\end{pmatrix}
$$

$$
L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}0&0&-i&0\\0&0&0&i\\i&0&0&0\\0&-i&0&0\end{pmatrix}
$$

$$
L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=C_{\Pi}^{-1}\,L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\,C_{\Pi}=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix}
$$

The sixteen equalities were checked by multiplying the three matrices of each line; the middle expression is the axis-free display of §*The Sixteen Products in This Frame* conjugated by $C_{\Pi}^{-1}$ on the left and $C_{\Pi}$ on the right, and the right-hand array is the Pauli display of §*The Sixteen Cells in the Peirce Frame*. The pair $(\mu,\nu)$ is the same operator on both sides of each line, $e_\mu[\,]e_\nu$, so the list is a dictionary of arrays and not a table of operators. Two of the sixteen have the same array in both frames, $L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=\mathrm I_4$ and $L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=\operatorname{diag}(-1,1,1,-1)$, two more differ by the single sign $L^{\mathrm{axf}}=-L^{\mathrm{pau}}$ at $(t,y)$ and $(z,x)$, and the other twelve differ in their entries. The explanation is commutation: $L_{e_t}R_{e_t}=\mathrm I_4$ commutes with everything, and $L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=\operatorname{diag}(-1,1,1,-1)$ commutes with $C_{\Pi}$, since both fix the two $2\times2$ blocks that $C_{\Pi}$ pairs. The two cells at $(t,y)$ and $(z,x)$ are the ones that anticommute with $C_{\Pi}$, which is why their two displays differ by $-1$ and not in their entries.

**A worked element.** Take $\tilde Q=e_t+\vec e_x$, so that $Q_t=Q_x=1$ and $Q_y=Q_z=0$. In the axis-free frame,
$$
L^{\mathrm{axf}}(e_t+\vec e_x)=L_{e_t}^{\mathrm{axf}}+L_{\vec e_x}^{\mathrm{axf}}
=\begin{pmatrix}1&-1&0&0\\1&1&0&0\\0&0&1&-1\\0&0&1&1\end{pmatrix},
$$
and in the Peirce frame the same element reads
$$
L^{\mathrm{pau}}(e_t+\vec e_x)=\mathsf{M}_{4L}(e_t)+\mathsf{M}_{4L}(\vec e_x)=\begin{pmatrix}1&-i&0&0\\-i&1&0&0\\0&0&1&-i\\0&0&-i&1\end{pmatrix},
$$
which is the block $\mathsf{M}_2(e_t+\vec e_x)=\begin{pmatrix}1&-i\\-i&1\end{pmatrix}$ written twice. The switch is checked by multiplying, $L^{\mathrm{pau}}= C_{\Pi}^{-1}L^{\mathrm{axf}}C_{\Pi}$, and it holds entry by entry. The right displays of the same element are obtained the same way, $R^{\mathrm{pau}}(e_t+\vec e_x)=\mathsf S\,L^{\mathrm{pau}}(e_t+\vec e_x)^{\mathsf T}\mathsf S^{-1}$.

**What the switch preserves, and what it does not.** It preserves the trace, the determinant, the spectrum, the ranks of all powers, and the algebra of the sixteen cells: it is a conjugation, so it is an isomorphism of the ambient $M_4(\mathbb{C})$ carrying $\mathbb{B}_L$ onto $\mathbb{B}_L$ and $\mathbb{B}_R$ onto $\mathbb{B}_R$. It does not preserve the transpose dictionary, the reality of the sixteen arrays, the vanishing of the cross blocks, or the property that a matrix is a signed permutation. Those four are properties of the axis-free frame; the vanishing of the cross blocks and the tensor form are properties of the Peirce frame.

**Where the $2\times2$ display sits.** The switch moves the $4\times4$ displays and leaves the $2\times2$ image alone: $\mathsf{M}_2(\tilde Q)$ appears as a block before the switch and after it, and it never meets $C_{\Pi}$. §*The $2\times2$ Pauli Representation* and its §*The Bridge to the $4\times4$ Displays* state the consequence.

## The Clifford Structure

**The Clifford algebra is the cell algebra.** The sixteen cells $L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}$ are linearly independent, and their complex span is all of $M_4(\mathbb{C})$. They multiply by multiplying the left multipliers together and the right multipliers together,
$$
L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}\,L_{e_\rho}^{\mathrm{pau}}R_{e_\sigma}^{\mathrm{pau}}
=L_{e_\mu e_\rho}^{\mathrm{pau}}R_{e_\sigma e_\nu}^{\mathrm{pau}};
$$
the result is again a left multiplication and a right multiplication, so the assignment $e_\mu\otimes e_\nu^{\mathrm{opp}}\mapsto L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}$ is an algebra isomorphism
$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\longrightarrow M_4(\mathbb{C})\cong\mathrm{Cl}_{1,3}(\mathbb{C}).
$$
The sixteen products of the five frame cells span over $\mathbb{R}$ the algebra $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$, of real dimension $16$, and the sixteen cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$, the opposite real form. The full Clifford structure, odd part included, is a structure of the two-sided operators themselves; it is not an external tool, and the even part is not a limitation. The Dirac, Weyl and Majorana matrices are three presentations of the same complex algebra, related by a change of frame; a change of frame is a change of basis, not a change of object.

**The five cells of the frame.** The five frame cells are
$$
\boxed{\;iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\qquad
iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}\;}
$$
Each is a unit multiple of a cell; the left factor is a unit and the right factor a spatial unit, written $\vec e_{\nu(\mu)}$ with $\nu(t)=x$ and $\nu(k)=y$. The order is timelike, the three spatial, chirality. For the first and the last the left factor is $e_t$, so the cell collapses to a single right multiplication, $iR_{\vec e_x}^{\mathrm{pau}}$ and $-iR_{\vec e_z}^{\mathrm{pau}}$, and the two spellings are the same operator. In the Peirce frame the five are monomial matrices, written out in §*The Legacy Pauli Gamma Formulation*; in the axis-free frame they are $i$ times real signed permutation matrices, displayed there too, and the conjugation of §*The Switch Between the Two Frames* carries the whole cell algebra with it.

**The anticommutation relations.**
$$
\{iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}},iL_{e_\nu}^{\mathrm{pau}}R_{\vec e_{\nu(\nu)}}^{\mathrm{pau}}\}=-2g_{\mu\nu}[\mathbb{M}_-]I_4,\qquad
(iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})^2=-I_4,
$$
$$
-iR_{\vec e_z}^{\mathrm{pau}}=i\,(iR_{\vec e_x}^{\mathrm{pau}})(iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})(iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})(iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}),
$$
with $g=\operatorname{diag}(-1,+1,+1,+1)$. No index is raised or lowered: the metric is the sign vector inside the product, not a tensor in the display. The relations are unchanged by the conjugation, so the same six lines hold with the label $\mathrm{axf}$ throughout, and that is the spelling the physics articles print.

**The sixteen products are the sixteen cells.** The five frame cells are five cells up to a factor $i$, and the sixteen products of the five are the sixteen cells:

| grade | cells |
|---|---|
| $0$ | $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ |
| $1$ | $L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$, $L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$, $L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$, $L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ |
| $2$ | $L_{\vec e_x}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$, $L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$, $L_{\vec e_y}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$, $L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$, $L_{\vec e_z}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$, $L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ |
| $3$ | $L_{e_t}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$, $L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$, $L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$, $L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ |
| $4$ | $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ |

Each row lists the cells of one grade, and the counts are $1+4+6+4+1=16$. The same sixteen lines with the label $\mathrm{axf}$ list the same sixteen operators: the grade is a property of the product and not of the display, and the physics articles read the table with $\mathrm{axf}$ labels. The frame is one frame among many: another orthogonal pair $(\beta,\delta)$ gives another five cells, the relations survive, and the cell labels do not. The proof, and the freedom in the choice of frame, are in *Two-Sided Operators on the Biquaternion Algebra*, §*Composition and the Two Closures*.

**A cell is written as its two multipliers, never as a letter.** The basis cell is $L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}$, for two unit indices, and the frame cell of the coordinate $x_\mu$ is $iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}$ with $\nu(t)=x$ and $\nu(k)=y$; the chirality cell is $-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$. The arrow follows the index: $\nu(\mu)$ is spatial for every $\mu$, so the right multiplier of a frame cell always carries one, $R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}$; the left multiplier carries one only when its index is written out as spatial, as in $L_{\vec e_k}^{\mathrm{pau}}$, while the generic $L_{e_\mu}^{\mathrm{pau}}$ stays plain because $\mu=t$ is the scalar unit $e_t=1$. No single letter stands for a frame cell in either part of the corpus: the letter collided with the basis cells and with the gauge generators $T_a=\tfrac12\vec e_a$ of the unification articles, and it is retired. The factor $i$ belongs to the cell, so a product of two cells multiplies the two multipliers on each side, $iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}\,iL_{e_\nu}^{\mathrm{pau}}R_{\vec e_{\nu(\nu)}}^{\mathrm{pau}}=-L_{e_\mu}^{\mathrm{pau}}L_{e_\nu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}R_{\vec e_{\nu(\nu)}}^{\mathrm{pau}}$, and the sign is carried by the product, not by a symbol.

**The opposite algebra is written with three letters.** The opposite of an algebra, with the product reversed, carries the superscript $\mathrm{opp}$: the reversed product is $a\cdot^{\mathrm{opp}}b=ba$, and the opposite of $\mathbb{B}$ is $\mathbb{B}^{\mathrm{opp}}$. The two-letter form $\mathrm{op}$ is not used at all, neither for the opposite algebra nor for the operator norm, which is written $\lVert A\rVert$ (*Index, Notation and Corpus Conventions*, §*The Superscripts*). The competing norms keep their own labels, $\lVert A\rVert_{\mathrm{HS}}$, $\lVert A\rVert_{\mathrm{nuc}}$, $\lVert A\rVert_{F}$, $\lVert A\rVert_{*}$.

**The comparison map.** The $\mathbb{R}$-linear map $\iota_{\mathrm{Cl}}$ of the Dirac articles is read in cells as
$$
e_t\mapsto L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},\qquad
\vec e_x\mapsto L_{\vec e_x}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},\qquad
\vec e_y\mapsto L_{\vec e_y}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},\qquad
\vec e_z\mapsto L_{\vec e_z}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},\qquad
i\mapsto L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$
Its image is the real span of the eight cells $L_{e_\mu}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ and $L_{e_\mu}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$, of real dimension $8$, and it satisfies $\iota_{\mathrm{Cl}}(i\tilde Q)=L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}\,\iota_{\mathrm{Cl}}(\tilde Q)$. It is $\mathbb{R}$-linear and not $\mathbb{C}$-linear: it is the comparison with the even subalgebra of $\mathrm{Cl}_{1,3}$, not a second representation of $\mathbb{B}$. It agrees with left multiplication on the four real units and sends the scalar imaginary to right multiplication by $\vec e_z$. In the axis-free frame the same map reads $\iota_{\mathrm{Cl}}(e_\mu)=L_{e_\mu}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ and $\iota_{\mathrm{Cl}}(i)=L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, because the conjugation carries the whole cell algebra with it, and that is the spelling the physics articles print.

**The basis, read in cells.** On the eight real units the reading is

| $\tilde Q$ | cell | $\tilde Q$ | cell |
|---|---|---|---|
| $e_t$ | $L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | $i$ | $L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ |
| $\vec e_x$ | $L_{\vec e_x}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | $i\vec e_x$ | $L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ |
| $\vec e_y$ | $L_{\vec e_y}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | $i\vec e_y$ | $L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ |
| $\vec e_z$ | $L_{\vec e_z}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | $i\vec e_z$ | $L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ |

The three quaternion units become the three spacelike bivectors and the three imaginary units the three timelike bivectors, all with positive coefficients. The only minus in the reading sits on $i$ itself, $i\mapsto L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-i\,\omega$, and it is the freedom the correspondence carries: the sign of the pseudoscalar is a convention, and it fixes the sign of every entry in the last four rows.

**The odd part.** The reading lands in the even part. Multiplication by the fixed cell $iR_{\vec e_x}^{\mathrm{axf}}$ reaches the odd part, and the two real sectors separate: $iR_{\vec e_x}^{\mathrm{axf}}$ times the image of $\mathbb{M}_+$ is the vector space, and $iR_{\vec e_x}^{\mathrm{axf}}$ times the image of $\mathbb{M}_-$ the trivector space. So a four-vector is $iR_{\vec e_x}^{\mathrm{axf}}$ times the image of $w\in\mathbb{M}_+$, and a trivector is $iR_{\vec e_x}^{\mathrm{axf}}$ times the image of $w\in\mathbb{M}_-$. The cell $iR_{\vec e_x}^{\mathrm{axf}}$ is the one choice in the odd half of the reading, and it is fixed by the representation. The same holds with the Peirce label, $iR_{\vec e_x}^{\mathrm{pau}}$ times the image of $\mathbb{M}_\pm$.

**Lorentz generators.** For $\mu\neq\nu$ the two frame cells anticommute, $\{iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}\}=0$, so the commutator is twice the product, and
$$
\sigma_{\mu\nu}=\tfrac14\bigl[iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}\bigr]=\tfrac12\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\,iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}=-\tfrac12\,L_{e_\mu}^{\mathrm{axf}}L_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}
$$
is half a bivector. Read in cells and in biquaternions,

| generator | cell | biquaternion |
|---|---|---|
| $\sigma_{23}$ | $\tfrac12L_{\vec e_x}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | $\tfrac12\vec e_x$ |
| $\sigma_{31}$ | $\tfrac12L_{\vec e_y}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | $\tfrac12\vec e_y$ |
| $\sigma_{12}$ | $\tfrac12L_{\vec e_z}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | $\tfrac12\vec e_z$ |
| $\sigma_{01}$ | $\tfrac12L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | $\tfrac12 i\vec e_x$ |
| $\sigma_{02}$ | $\tfrac12L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | $\tfrac12 i\vec e_y$ |
| $\sigma_{03}$ | $\tfrac12L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | $\tfrac12 i\vec e_z$ |

The spacelike generators are the half quaternion units and the boosts the half imaginary units, again with positive signs. The half is not removable: the product of two frame cells is the bivector and the Lorentz generator is half of it.

**Reversal, conjugation and the two traces.** Clifford reversal, reading an ordered product of frame cells backwards, is quaternion conjugation under the reading: reversing the image of $\tilde Q$ gives the image of $\tilde Q^{\natural}$, checked on the eight real units, where both sides carry $+$ on $e_t$ and $i$ and $-$ on the six vector units. Hence the biquaternion norm is the Clifford norm built with the reversal: the image of $\tilde Q\tilde Q^{\natural}$ is the product of the image of $\tilde Q$ with its reversal.

Two traces must not be confused. The trace of the corpus formula is the $2\times2$ one, $\operatorname{Tr}$, and it equals twice the scalar part. The $4\times4$ trace of the image is $4\,\mathrm{Sc}(\tilde Q)$, complex in general, and its real part is twice the real part of the $2\times2$ trace,
$$
2\,\mathrm{Re}\operatorname{Tr}(\tilde Q)=4\,\mathrm{Re}\,\mathrm{Sc}(\tilde Q).
$$
The identity uses $\operatorname{Tr}(\tilde Q)=2\,\mathrm{Sc}(\tilde Q)$, which is the trace formula of §*The Isomorphism*. Both were checked on a general element with complex coefficients.

**A matrix frame is a coordinate, not an object.** The Dirac, Weyl and Majorana matrices are three bases of the same algebra, related by $\mathsf X\,(iL_{e_\mu}R_{\vec e_{\nu(\mu)}})\,\mathsf X^{-1}$ with $\mathsf X$ invertible. A change of frame is a change of basis, and the normal forms are those of §*The Operator $L_{\tilde Q}R_{\tilde P}$* in *Two-Sided Operators on the Biquaternion Algebra*. No statement of the corpus depends on the basis written.

**The presentation is the stronger one for the corpus's purpose.** Four things are carried by the algebra and not by a chosen matrix frame. The state is an element of $\mathbb{B}$, and the left regular module is the Dirac spinor space, so no column and no minimal left ideal has to be chosen. The pairing $\operatorname{Tr}(\tilde Q_1\tilde Q_2^{*})$ and the three involutions are fixed by the algebra, whereas the Dirac adjoint needs a chosen time generator. The two real sectors $\mathbb{M}_\pm$ and the $ict'$ metric are part of the data. The frame is internal: it is a set of cells, not an array of matrices carried from outside. The Clifford algebra is recovered from these data; the data are not recovered from the algebra.

**Remark (the two coordinate frames, $\mathbb{B}$ and $\mathbb{M}_-$).** The series has exactly two coordinate frames, and they are not to be mixed. Both are fixed, with their metrics and their table, in *Frame Conventions*, and neither is a matrix frame.

- The **$\mathbb{B}$ frame** is the biquaternion space read in its own coordinate, $Q_\mu\in\mathbb{C}$; on the material case $Q_t=ict'$ and $Q_k=q_k$, so $Q_t^2=-(ct')^2$. Its metric is $(1,1,1,1)$: every cell squares to $+I_4$.
- The **$\mathbb{M}_-$ frame** is the material real frame, $x_0=ct'$ and $x_k=q_k$, with $Q_t=ix_0$. Its metric is $(-1,1,1,1)$; the cells square to the opposite, $(1,-1,-1,-1)$.

The five frame cells are the ones of §*The Clifford Structure* in the $\mathbb{M}_-$ frame, and their three spatial squares are $-I_4$ there. In the $\mathbb{B}$ frame the four cells that all square to $+I_4$ are
$$
(iR_{\vec e_x}^{\mathrm{axf}})^2=+I_4,\qquad
(-L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^2=+I_4,\quad k=1,2,3 ,
$$
and §*The Legacy Pauli Gamma Formulation* prints the $\mathbb{M}_-$ arrays: the $\mathbb{B}$-frame ones follow by multiplying the three spatial generators by $i$, which replaces $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ by $-L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ and leaves $iR_{\vec e_x}^{\mathrm{axf}}$ unchanged.

The d'Alembertian is one operator, $\Box=\partial^2/\partial Q_t^2+\Delta_Q=\Delta-\partial^2/\partial x_0^2$, and only its reading in the frame changes. A frame display in the series is in the $\mathbb{M}_-$ frame unless it says otherwise. The other uses of the word are not coordinate frames: the five generators are the image of the Clifford map and are not a coordinate frame, the **axis-free** and **Peirce** frames are the two bases that fix the matrix display, and a **rest frame** is a physical observer.

**The slash is not used.** The Dirac slash is not part of the notation of the corpus. A contraction is written out with the index repeated in the same position, as the cell sum below for a momentum. No index is raised or lowered and no metric tensor enters: the metric of the series is the sign vector $\varepsilon$ inside the product, and $Q_t=ict'$ is substituted only on the material sector $\mathbb{M}_-$. A multi-slot object is written with every slot low, in the order of its definition: row or output first, column or input second; a tetrad is frame first, world second, and a structure constant is output first. An inverse matrix is written $X^{-1}$, so the inverse metric is $(g^{-1})_{\mu\nu}$ and never a second symbol $g_{\mu\nu}$. In both frames the momentum contraction is a cell sum,
$$
\sum_\mu iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}p_\mu=i\bigl(L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}p_t+L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_x+L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_y+L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_z\bigr),
$$
so the frame is visible in the formula.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra. The fifth is written $\gamma_5$ with no bracket and no frame, because it is the product of the four and not the image of a direction.

The gammas are the five frame cells of §*The Clifford Structure* written as arrays, and the section writes them in both frames: first the Peirce arrays, which are the ones the gamma literature prints, and then the axis-free ones, which are the display of the body.

**The five gammas.** The five Dirac matrices are two-sided operators of the frame,
$$
\boxed{\;\gamma_0[\mathbb{M}_-]=iR_{\vec e_x}^{\mathrm{pau}}=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\qquad
\gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}\;}
$$

**In the Peirce frame.**
$$
\gamma_0[\mathbb{M}_-]=\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
\gamma_1[\mathbb{M}_-]=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},
$$
$$
\gamma_2[\mathbb{M}_-]=\begin{pmatrix}0&0&0&-i\\0&0&i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},\qquad
\gamma_3[\mathbb{M}_-]=\begin{pmatrix}0&0&1&0\\0&0&0&-1\\-1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
\gamma_5=\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.
$$
They satisfy $\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=-2g_{\mu\nu}[\mathbb{M}_-]I_4$, $(\gamma_k[\mathbb{M}_-])^2=-I_4$ and $\gamma_5=i\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$. In the Pauli form the same five are
$$
\gamma_0[\mathbb{M}_-]=\sigma_1\otimes I_2,\qquad
\gamma_k[\mathbb{M}_-]=i\,\sigma_2\otimes\sigma_k,\qquad
\gamma_5=-\sigma_3\otimes I_2 .
$$
That form is what a textbook prints, and it is what makes the five recognisable to a reader of the Dirac literature: the first and the last are one Pauli matrix repeated, the three spatial ones are a single Pauli matrix crossed with the triplet.

**In the axis-free frame.** The conjugation of §*The Switch Between the Two Frames* carries them, and there they are $i$ times real signed permutation matrices,
$$
\gamma_0[\mathbb{M}_-]=i\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},\qquad
\gamma_1[\mathbb{M}_-]=i\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix},
$$
$$
\gamma_2[\mathbb{M}_-]=i\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&-1&0\\0&0&0&1\end{pmatrix},\qquad
\gamma_3[\mathbb{M}_-]=i\begin{pmatrix}0&-1&0&0\\-1&0&0&0\\0&0&0&-1\\0&0&-1&0\end{pmatrix},\qquad
\gamma_5=i\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&1&0&0\\-1&0&0&0\end{pmatrix}.
$$
The entries are $\pm i$ or $0$ in both frames, and the axis-free arrays are exactly the cells $iR_{\vec e_x}^{\mathrm{axf}}$, $iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ and $-iR_{\vec e_z}^{\mathrm{axf}}$: the same five cells, drawn in the other frame. No entry marks them out from the other eleven cells there.

**The display, and the relation between the two.** Both arrays of each of the five are printed above, and the reason is the same for both: the Peirce array is the one a reader can compare with a textbook, and the axis-free array is the one the physics articles multiply. The two arrays of one operator are conjugates,
$$
\gamma_\mu[\mathbb{M}_-]^{\mathrm{axf}}=C_{\Pi}\,\gamma_\mu[\mathbb{M}_-]^{\mathrm{pau}}\,C_{\Pi}^{-1},\qquad
\gamma_\mu[\mathbb{M}_-]^{\mathrm{pau}}=C_{\Pi}^{-1}\,\gamma_\mu[\mathbb{M}_-]^{\mathrm{axf}}\,C_{\Pi},
$$
with $C_{\Pi}$ the change of §*The Switch Between the Two Frames*, $\det C_{\Pi}=-\tfrac14$ and $C_{\Pi}^{-1}=2C_{\Pi}^{\dagger}$. Every identity of this section holds in both displays, because a conjugation preserves products, anticommutators, traces, determinants and spectra; what it does not preserve is the reading of a single entry. In the axis-free display $\gamma_0[\mathbb{M}_-]$ is $iR_{\vec e_x}^{\mathrm{axf}}$ and the four others are four more signed permutations times $i$, so the printed array shows nothing of the Pauli structure. The gamma map is therefore a display of the five cells and not the five cells themselves.

**The subscript on an element.** Chirality is the subscript: an element is $L$ or $R$, and those are the two values. The chirality of an operator is its slot, and the cell that reads the subscript is $\mathsf{V}^{\mathrm{vol}}$ of *Special Element Conventions*, §*The Chirality Convention*, printed here $\gamma_5$ with the rest of the gamma display. The letters are the Dirac ones. In the Peirce display $\gamma_5=\operatorname{diag}(-I_2,I_2)$, so $\tilde Q_L$ is the upper block, which is $\psi=(\psi_L,\psi_R)$; a display moves the entries and not the values. Every element is a sum of one of each, only the zero element is both, a product takes the letter of its right factor, and left multiplication keeps the letter. The subscript is a function of the element and of the declared frame, so a unit, a product and a general element carry it as well as a state.

**The three uses of the two letters.** $L_a$ and $R_b$ are the left and the right multiplier, an operator. $\mathsf M_4^{L}$ and $\mathsf M_4^{R}$ are the left and the right regular matrix, an array. $\tilde Q_L$, $\tilde Q_R$, $\psi_L$ and $\psi_R$ are the chirality of an element, and only the third applies to every element of the algebra.

**The coordinate frames of the five.** The $\mathbb{M}_-$ frame carries these matrices; the $\mathbb{B}$-frame generators are $\gamma_0[\mathbb{B}]=\gamma_0[\mathbb{M}_-]$ and $\gamma_k[\mathbb{B}]=i\gamma_k[\mathbb{M}_-]$, all squaring to $+I_4$. The two sets differ by the sign of the three spatial cells, as §*The Clifford Structure* records, and a formula that mixes them belongs to neither frame.

**The sixteen products.** The five frame cells are five of the sixteen products up to a factor $i$, and their products in increasing grade are the sixteen cells:

| grade | $\gamma$-product | Peirce cell | Peirce equality | axis-free cell |
|---|---|---|---|---|
| $0$ | $1$ | $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ | $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=I_4$ | $L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $1$ | $\gamma_0[\mathbb{M}_-]$ | $L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ | $L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=-i\,\gamma_0[\mathbb{M}_-]$ | $L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ |
| $1$ | $\gamma_1[\mathbb{M}_-]$ | $L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ | $L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=-i\,\gamma_1[\mathbb{M}_-]$ | $L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ |
| $1$ | $\gamma_2[\mathbb{M}_-]$ | $L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ | $L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=-i\,\gamma_2[\mathbb{M}_-]$ | $L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ |
| $1$ | $\gamma_3[\mathbb{M}_-]$ | $L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ | $L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=-i\,\gamma_3[\mathbb{M}_-]$ | $L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ |
| $2$ | $\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]$ | $L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ | $L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]$ | $L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ |
| $2$ | $\gamma_0[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]$ | $L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ | $L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=\gamma_0[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]$ | $L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ |
| $2$ | $\gamma_0[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ | $L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ | $L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=\gamma_0[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ | $L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ |
| $2$ | $\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]$ | $L_{\vec e_z}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ | $L_{\vec e_z}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]$ | $L_{\vec e_z}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $2$ | $\gamma_1[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ | $L_{\vec e_y}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ | $L_{\vec e_y}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=-\gamma_1[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ | $L_{\vec e_y}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $2$ | $\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ | $L_{\vec e_x}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ | $L_{\vec e_x}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ | $L_{\vec e_x}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $3$ | $\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]$ | $L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ | $L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=-i\,\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]$ | $L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ |
| $3$ | $\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ | $L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ | $L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=i\,\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ | $L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ |
| $3$ | $\gamma_0[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ | $L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ | $L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}=-i\,\gamma_0[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ | $L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ |
| $3$ | $\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ | $L_{e_t}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ | $L_{e_t}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=i\,\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ | $L_{e_t}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ |
| $4$ | $\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ | $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ | $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=i\,\gamma_5=-\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ | $L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ |

Each row reads the cell as a unit coefficient times the $\gamma$-product; the inverse reading carries the conjugate coefficient, since $c\in\{1,-1,i,-i\}$. The last column is the same operator in the axis-free frame, and it is the one the body writes: the pair $(\mu,\nu)$ is the same in both columns, and only the array changes.

**The Clifford reading in gammas.**
$$
e_t\mapsto I_4,\qquad
\vec e_x\mapsto\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-],\qquad
\vec e_y\mapsto\gamma_3[\mathbb{M}_-]\gamma_1[\mathbb{M}_-],\qquad
\vec e_z\mapsto\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-],\qquad
i\mapsto-\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-] .
$$
The only minus sits on $i$ itself, and it fixes the sign of the last four rows of the cell table. Multiplication by the fixed generator $\gamma_0[\mathbb{M}_-]$ reaches the odd part: $\gamma_0[\mathbb{M}_-]$ times the image of $\mathbb{M}_+$ is the vector space, and $\gamma_0[\mathbb{M}_-]$ times the image of $\mathbb{M}_-$ the trivector space.

**Lorentz generators and reversal.**
$$
\sigma_{\mu\nu}=\tfrac14[\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]]=\tfrac12\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\quad(\mu\neq\nu),
$$
and Clifford reversal, $\mathrm{rev}(\gamma_{\mu_1}[\mathbb{M}_-]\cdots\gamma_{\mu_k}[\mathbb{M}_-])=\gamma_{\mu_k}[\mathbb{M}_-]\cdots\gamma_{\mu_1}[\mathbb{M}_-]$, is quaternion conjugation under the reading.

**The contractions.** In gamma notation a momentum contraction is $\sum_\mu \gamma_\mu[\mathbb{M}_-] p_\mu=i(L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}p_t+L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}p_x+L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}p_y+L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}p_z)$, a derivative contraction is $i\sum_\mu \gamma_\mu[\mathbb{M}_-]\partial/\partial x_\mu$ with $x_0=q'_t$, and a $\mathbb{B}$-frame contraction is $\sum_\mu \gamma_\mu[\mathbb{B}]\partial/\partial Q_\mu$. The mixed form $i\sum_\mu \gamma_\mu[\mathbb{M}_-]\partial/\partial Q_\mu$ belongs to neither frame. The axis-free spelling of the same sums is the one with the $\mathrm{axf}$ cells, and it is the one the body writes.

Over $\mathbb{R}$ the products of the five span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the cells,
$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k[\mathbb{M}_-])^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5\}=0,
$$
$$
[\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]]=2\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\quad(\mu\ne\nu),\qquad
[\gamma_a[\mathbb{M}_-],S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d[\mathbb{M}_-]-\varepsilon_a\delta_{ad}\gamma_c[\mathbb{M}_-],\qquad
S_{cd}=\tfrac14[\gamma_c[\mathbb{M}_-],\gamma_d[\mathbb{M}_-]],
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-])=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu[\mathbb{M}_-]=-\varepsilon_\mu\gamma_\mu[\mathbb{M}_-]$, so that $\sum_\mu\gamma^\mu[\mathbb{B}]\gamma_\mu[\mathbb{B}]=-4I_4$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\alpha[\mathbb{M}_-]$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]$.
## The $2\times2$ Pauli Representation

**Read last, and not because it is small.** The $2\times2$ display is the algebra itself, not an operator on it. It is placed last because it is best read after both $4\times4$ displays have shown what a matrix of an operator is, and because its matrices are the block of the Pauli display: the object it displays is the one the other two displays act on.

### The Isomorphism

**The map.** The isomorphism is $\mathbb{C}$-linear, multiplicative and bijective,
$$
\mathsf{M}_2:\mathbb{B}\longrightarrow M_2(\mathbb{C}),\qquad
\mathsf{M}_2(\tilde Q_1+\tilde Q_2)=\mathsf{M}_2(\tilde Q_1)+\mathsf{M}_2(\tilde Q_2),\qquad
\mathsf{M}_2(\tilde Q_1\tilde Q_2)=\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2),
$$
and it is the reading every numerical check in the corpus is performed with.

**The four unit images.** The images of the units are fixed once, because every article depends on them agreeing:
$$
\mathsf{M}_2(e_t)=I_2,\qquad
\mathsf{M}_2(\vec e_x)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}=-i\sigma_1,\qquad
\mathsf{M}_2(\vec e_y)=\begin{pmatrix}0&-1\\1&0\end{pmatrix}=-i\sigma_2,\qquad
\mathsf{M}_2(\vec e_z)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}=-i\sigma_3,
$$
with $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices of §*The Two Tensor Factors*. The central scalar is $\mathsf{M}_2(i)=iI_2$, and $\mathbb{C}$-linearity gives the Hermitian units, $\mathsf{M}_2(i\vec e_k)=i\,\mathsf{M}_2(\vec e_k)$. A general element is
$$
\mathsf{M}_2(\tilde Q)=
\begin{pmatrix}
Q_t-iQ_z&-iQ_x-Q_y\\
-iQ_x+Q_y&Q_t+iQ_z
\end{pmatrix}
=\begin{pmatrix}a&b\\ c&d\end{pmatrix},
$$
which is the $a,b,c,d$ of §*The Two Tensor Factors*, and the reason the Pauli display has that block.

**The assignment is forced, not chosen.** $\vec e_k^2=-e_t$ requires the factor $i$ and $\vec e_x\vec e_y=\vec e_z$ fixes the sign, so neither the factor nor the sign in the three vector images could have been otherwise. A reviewer must not "correct" the assignment by making the three images real, nor by negating all three. *Introduction to the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})_{\mathbb{H}}$ of Quaternions* derives both.

**No frame is needed.** The isomorphism is a map of algebras and does not depend on a frame of $\mathbb{B}$. The four matrices above are the images of the units, not the entries of a matrix read in a basis, and no Peirce family enters. The frame enters only in the two $4\times4$ displays, which read operators on the algebra.

**The trace is the trace of this image.** The Hermitian form is defined on the algebra and needs no matrix. The trace is defined only here, on the image, and it is a reading of the Hermitian form in this presentation, not a second pairing. The corpus writes
$$
\operatorname{Tr}(\tilde Q):=\operatorname{Tr}\mathsf{M}_2(\tilde Q).
$$
On the units $\operatorname{Tr}(e_t)=2$ and $\operatorname{Tr}(\vec e_k)=0$, so on a general element $2\,\mathrm{Sc}(\tilde Q)=\operatorname{Tr}(\tilde Q)$. That factor $2$ is not a normalisation but a consequence of $\mathsf{M}_2(e_t)=I_2$: it comes with the four images above and cannot be divided out. The probability pairing is written in the Hermitian form and read in the trace where the $2\times2$ image is used, the Born rule among them,
$$
2\langle\tilde Q_1,\tilde Q_2\rangle_{*}=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\operatorname{Tr}(\tilde Q_1\tilde Q_2^{*}),\qquad 2\,\mathrm{Sc}(\tilde Q)=\operatorname{Tr}(\tilde Q),
$$
and this is the only place in the article where the trace appears. An unsubscripted trace means this one; a regular matrix has its own, written with its subscript, $\operatorname{tr}L(\tilde Q)$. The identity $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)=\operatorname{Tr}(\tilde Q_1\tilde Q_2)$ is the same reading applied to the plain form, not a probability statement. The same element in the regular $4\times4$ representation has trace $4\,\mathrm{Sc}(\tilde Q)$, twice the trace of the $2\times2$ image: the factor belongs to the presentation, not to the element.

**The determinant is the norm.** The determinant of the image is the biquaternion norm, $\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$, and it is multiplicative, which is what makes the matrix model compute every norm in the series. The invertibility criterion, the group of units and the unit-norm group are read from it; the derivations are *Introduction to the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})_{\mathbb{H}}$ of Quaternions*.

**Never conjugate the matrix entries on their own.** Conjugating the entries of $\mathsf{M}_2(\tilde Q)$ is *not* the image of any involution of the algebra: it negates the images of $\vec e_x$ and $\vec e_z$ while leaving $\mathsf{M}_2(\vec e_y)$, which has real entries, untouched, and so it destroys the sector dictionary. The four conjugations $\natural$, $\bar{\phantom{Q}}$, ${}^{*}$ and $\flat$ are evaluated through the matrix formulas recorded in *Element and Operator Representations: The Three Actions*, never by conjugating entries.

**The realisation is a convention of presentation, not of content.** The isomorphisms that preserve the subspace dictionary are the $\mathsf{M}_{2,\mathrm{S}}=S\mathsf{M}_2S^{-1}$ with $S$ $*$-unitary up to a nonzero complex scalar, and an arbitrary invertible $S$ destroys the dictionary. The practical consequence is that a mistake of translation between the algebra and its matrices is repaired **here**, by correcting the assignment or the explicit factors of $i$, and never by altering the biquaternion norm, the $ict'$ assignment or the sector split.

**Two models multiply.** A product of two algebras is read through the product of their images,
$$
\mathsf{M}_2\otimes\mathsf{M}_2:\ \mathbb{B}\otimes\mathbb{B}\longrightarrow M_2(\mathbb{C})\otimes M_2(\mathbb{C})\cong M_4(\mathbb{C}),
$$
and the trace factorises over the two factors,
$$
\operatorname{Tr}(x\otimes y)=\operatorname{Tr}(x)\,\operatorname{Tr}(y),\qquad
\operatorname{Tr}(e_t)=2,\qquad \operatorname{Tr}(\vec e_k)=0 .
$$
A subscript names the factor it traces, $\operatorname{Tr}_\mathbb{B}(e_t)=2$ and $\operatorname{Tr}_\mathbb{B}(\vec e_k)=0$, and an unsubscripted $\operatorname{Tr}$ on $\mathbb{B}\otimes\mathbb{B}$ is the trace of the $4\times4$ image: on the units $\operatorname{Tr}(e_t\otimes e_t)=4$ and $\operatorname{Tr}(\vec e_j\otimes\vec e_k)=0$. The two-qubit arena of the exercises is this algebra and is read with this trace; it needs no second trace convention.

**A bare $\mathsf{M}_2$ means this isomorphism and nothing else.** A plain $\mathsf{M}_2$, with no subscript, superscript or tilde, is reserved throughout the series for this isomorphism alone. The other uses a reader may meet are marked differently: $\varphi$ is an abstract homomorphism on the mathematics pages and an angle in the Thomas-precession exercise, $\tilde\Phi=\varphi\,e_t$ is the central scalar field of the Higgs articles, and $\Phi_{\tilde U}$ is the quantum channel of the gates article. None of these is the isomorphism, and a bare $\mathsf{M}_2$ is not any of them.

### The Bridge to the $4\times4$ Displays

**The block.** In the Pauli frame the left regular matrix is $I_2\otimes\mathsf{M}_2(\tilde Q)$, so the $2\times2$ image is the block of the $4\times4$ display, and the right regular matrix is $\mathsf{M}_2(\tilde Q)^{\mathsf T}\otimes I_2$, the same block transposed in the other slot. This is the whole reason the Peirce frame earns its root: it turns a $4\times4$ operator into a $2\times2$ matrix written twice.

**The frame moves the block, not the image.** In the axis-free frame the same operator reads
$$
L^{\mathrm{axf}}(\tilde Q)=C_{\Pi}\,\bigl(I_2\otimes\mathsf{M}_2(\tilde Q)\bigr)\,C_{\Pi}^{-1},
$$
so the axis-free display is the conjugated block. The $2\times2$ image $\mathsf{M}_2(\tilde Q)$ is untouched by $C_{\Pi}$: a change of frame conjugates the $4\times4$ displays and leaves the $2\times2$ display alone.

**The determinant squares, the trace doubles.** From the block form, $\det L(\tilde Q)=\det\mathsf{M}_2(\tilde Q)^2=\langle\tilde Q\rangle_{\natural}^2$ and $\operatorname{tr}L(\tilde Q)=2\operatorname{Tr}\mathsf{M}_2(\tilde Q)=4Q_t$, in either frame. The two invariants of the operator are the invariants of the element, counted twice.

## Summary

The algebra is displayed in three ways, in the order in which the displays are built.

**The axis-free representation comes first.** Its basis is the tensor basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, its product is the multiplication table, and its two matrices are read off that table by columns:
$$
L^{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&-Q_z&Q_y\\
Q_y&Q_z&Q_t&-Q_x\\
Q_z&-Q_y&Q_x&Q_t
\end{pmatrix},
\qquad
R^{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&Q_z&-Q_y\\
Q_y&-Q_z&Q_t&Q_x\\
Q_z&Q_y&-Q_x&Q_t
\end{pmatrix}.
$$
Its eight unit matrices are real signed permutations, its stitch is $R^{\mathrm{axf}}=D(L^{\mathrm{axf}})^{\mathsf T}D$ with $D=\operatorname{diag}(1,-1,-1,-1)$, its transpose is the conjugation, and its sixteen products are real. Nothing is chosen but the basis the algebra already carries. This is the display of record for the physics articles of the series, because a formula of general physics distinguishes no spatial direction.

**The Pauli representation comes second.** Its frame is the Peirce basis $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ of the standard pair, and in it the left matrix is $I_2\otimes\mathsf{M}_2(\tilde Q)$ and the right one $\mathsf{M}_2(\tilde Q)^{\mathsf T}\otimes I_2=\mathsf S L(\tilde Q)^{\mathsf T}\mathsf S^{-1}$. The four left matrices $L_{e_\mu}^{\mathrm{pau}}$, the four right matrices $R_{e_\nu}^{\mathrm{pau}}$ and the sixteen cells $L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}$ are written out. It is the display the gamma literature prints: $\gamma_0[\mathbb{M}_-]=\sigma_1\otimes I_2$, $\gamma_k[\mathbb{M}_-]=i\sigma_2\otimes\sigma_k$ and $\gamma_5=-\sigma_3\otimes I_2$, five cells of the frame, written in both frames in §*The Legacy Pauli Gamma Formulation*.

**The switch comes between them, and belongs to both.** It is $C_{\Pi}$ and its inverse, of determinant $-\tfrac14$ and normalisation $C_{\Pi}^{\dagger}C_{\Pi}=\tfrac12I_4$, with $L^{\mathrm{axf}}=C_{\Pi}L^{\mathrm{pau}}C_{\Pi}^{-1}$ and $R^{\mathrm{axf}}=C_{\Pi}R^{\mathrm{pau}}C_{\Pi}^{-1}$. It is two $2\times2$ blocks, it carries the eight unit matrices and the sixteen cells, and it leaves the trace $4Q_t$ and the determinant $\langle\tilde Q\rangle_{\natural}^2$ alone. What it does not carry is a single entry: the transpose dictionary, the reality of the sixteen arrays and the disappearance of the cross blocks are properties of the axis-free frame, the block form and the monomial five are properties of the Peirce frame.

**The Clifford structure is the algebra of the two-sided operators.** $e_\mu\otimes e_\nu^{\mathrm{opp}}\mapsto L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}}$ is an isomorphism onto $M_4(\mathbb{C})\cong\mathrm{Cl}_{1,3}(\mathbb{C})$, the sixteen products of the five frame cells span $\mathrm{Cl}_{1,3}(\mathbb{R})$ and the sixteen cells span $\mathrm{Cl}_{3,1}(\mathbb{R})$. The five frame cells are $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$, $iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ and $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, and a change of frame is a change of basis. The Clifford reading is the $\mathbb{R}$-linear comparison with the even subalgebra; in the axis-free frame $e_\mu\mapsto L_{e_\mu}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ and $i\mapsto L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$. On the eight real units it sends the three vector units to the spacelike bivectors and the three imaginary units to the timelike ones, and the odd part is reached by the fixed cell: $iR_{\vec e_x}^{\mathrm{axf}}$ times the image of $\mathbb{M}_+$ is the vector space, and $iR_{\vec e_x}^{\mathrm{axf}}$ times the image of $\mathbb{M}_-$ the trivector space. The Lorentz generators are half the corresponding bivectors, $\sigma_{\mu\nu}=\tfrac12\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\,iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}$ for $\mu\neq\nu$, Clifford reversal is quaternion conjugation, and the $4\times4$ trace has real part $2\,\mathrm{Re}\operatorname{Tr}=4\,\mathrm{Re}\,\mathrm{Sc}$, twice the real part of the $2\times2$ trace.

**No five of the sixteen products are singled out in the axis-free display**, so the gamma map is a display and not a structure of the algebra; §*The Switch Between the Two Frames* pairs each of the sixteen with its Peirce array through $L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}=C_{\Pi}^{-1}L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}}C_{\Pi}$.

**The $2\times2$ isomorphism comes last.** It is $\mathsf{M}_2(e_t)=I_2$, $\mathsf{M}_2(\vec e_k)=-i\sigma_k$ and $\mathsf{M}_2(i)=iI_2$, forced by $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, with $\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ and $\operatorname{Tr}(\tilde Q)=2Q_t$. It needs no frame, and it is the block of the Pauli display: the change of frame moves the block and never the image. Conjugating entries on its own is not an involution of the algebra, a bare $\mathsf{M}_2$ names this isomorphism and nothing else, and the realisation is fixed up to a star-unitary change of basis and a central scalar.

**The coordinate frames are two, and neither is a matrix frame.** The $\mathbb{B}$ frame reads $Q_\mu$ with $Q_t=ict'$ and metric $(1,1,1,1)$; the $\mathbb{M}_-$ frame reads $x_0=ct'$ with metric $(-1,1,1,1)$ and carries the printed gammas. A contraction stays in one frame, and the d'Alembertian is one operator in both.

**The label $M_4(\mathbb{C})_L$ is retired.** It named a matrix set rather than an algebra, and it changed meaning with the basis. An older article that writes it is read as $\mathbb{B}_L$, and an older $M_4(\mathbb{C})_R$ as $\mathbb{B}_R$. A bare $\mathsf{M}_4$ is not written for a regular matrix, which carries the family letter $L$ or $R$ in its subscript and the frame label $\mathrm{axf}$ or $\mathrm{pau}$ in its caret.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | The isomorphism of the element; $\mathsf{M}_2(e_t)=I_2$, $\mathsf{M}_2(\vec e_k)=-i\sigma_k$ |
| $\operatorname{Tr}(\tilde Q)=\operatorname{tr}\mathsf{M}_2(\tilde Q)$ | The trace, twice the scalar part |
| $\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ | The determinant, the biquaternion norm |
| $\rho_L,\rho_R$ | Left and right multiplication as linear maps, $\rho_L(\tilde Q_1)(\tilde Q_2)=\tilde Q_1\tilde Q_2$, $\rho_R(\tilde Q_1)(\tilde Q_2)=\tilde Q_2\tilde Q_1$ |
| $\mathbb{B}_L=M_4(\mathbb{C})_{\mathbb{B}_L}$ | The left copy, $\rho_L(\mathbb{B})$; $\mathbb{B}_R$ is its commutant |
| $L^{\mathrm{axf}}(\tilde Q)$, $L_{e_\mu}^{\mathrm{axf}}$ | The left regular matrix and the matrix of the unit $e_\mu$ in the axis-free frame, the display of record |
| $R^{\mathrm{axf}}(\tilde Q)$, $R_{e_\mu}^{\mathrm{axf}}$ | The right regular matrix in the axis-free frame |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | The stitch of the axis-free frame, $R^{\mathrm{axf}}=D(L^{\mathrm{axf}})^{\mathsf T}D$; the Gram matrix of $\operatorname{Sc}(XY)$ there |
| $L^{\mathrm{pau}}(\tilde Q)=\mathsf{M}_{4L}(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q)$ | The left regular matrix in the Peirce display |
| $R^{\mathrm{pau}}(\tilde Q)=\mathsf{M}_{4R}(\tilde Q)=\mathsf{M}_2(\tilde Q)^{\mathsf T}\otimes I_2=\mathsf S\mathsf{M}_{4L}(\tilde Q)^{\mathsf T}\mathsf S^{-1}$ | The right regular matrix in the Peirce display |
| $\mathsf S$ | The exchange of $\vec\Upsilon_+$ and $\vec\Upsilon_-$ fixing $\tilde\Pi_\pm$; the swap of the second and third Peirce coordinates, $\operatorname{diag}(1,1,-1,1)$ in the coefficient basis |
| $L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}}$, $L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}$ | The sixteen cells in the two frames; their complex span is $M_4(\mathbb{C})\cong\mathrm{Cl}_{1,3}(\mathbb{C})$ |
| $e_\mu[\,]e_\nu$, $L_{e_\mu}R_{e_\nu}$ | The basis two-sided operator $X\mapsto e_\mu Xe_\nu$ and its matrix, the cell |
| $c(T)$, $\ell(T)=\operatorname{rank}c(T)$ | The coefficient array of an operator $T$ in the basis of the sixteen cells and its length; $c(L_{\tilde Q}R_{\tilde P})=QP^{\mathsf T}$ |
| $C_{\Pi}$ | The change between the two displays, $L^{\mathrm{axf}}=C_{\Pi}L^{\mathrm{pau}}C_{\Pi}^{-1}$; $\det C_{\Pi}=-\tfrac14$, $C_{\Pi}^{-1}=2C_{\Pi}^{\dagger}$ |
| $\tilde\Pi_\pm$, $\vec\Upsilon_\pm$ | The standard pair and its two mixed units, which fix the Peirce frame |
| $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$, $iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | The five frame cells, timelike, three spatial, chirality; the gammas in the axis-free spelling |
| $\gamma_0[\mathbb{M}_-],\gamma_1[\mathbb{M}_-],\gamma_2[\mathbb{M}_-],\gamma_3[\mathbb{M}_-],\gamma_5$ | The same five as arrays, $iR_{\vec e_x}^{\mathrm{pau}}$, $iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$, $iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$, $iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$, $-iR_{\vec e_z}^{\mathrm{pau}}$ |
| $\tilde Q_L$, $\tilde Q_R$ | The two parts of an element, $\tfrac12(\mathrm I\mp\mathsf{V}^{\mathrm{vol}})\tilde Q$, of dimension two each; the Dirac subscript $\psi_L,\psi_R$, available on every element |
| $\iota_{\mathrm{Cl}}$ | The $\mathbb{R}$-linear comparison with the even subalgebra; $\iota_{\mathrm{Cl}}(e_\mu)=L_{e_\mu}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, $\iota_{\mathrm{Cl}}(i)=L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ |
| $\sigma_{\mu\nu}=\tfrac12\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\,iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}$ ($\mu\neq\nu$) | The Lorentz generators; half the bivectors of the table |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html), for the algebra and the element glyphs.
- [Conventions of the Products and the Forms](product-and-form-conventions.html), for the products the matrix product mirrors.
- [Conventions of the Operators and the Calculus](operator-and-calculus-conventions.html), for the left and right multiplications these matrices represent.
- [Frame Conventions](frame-conventions.html), for the two coordinate frames, their metrics and their table.
- [Element and Operator Representations: The Three Actions](element-and-operator-representations-the-three-actions.html), companion article, for the coefficient space and the three actions.
- [$M_4(\mathbb{C})$ Axis-Free Representation](../articles_maths/m4c-axis-free-representation.html) and [its Operators companion](../articles_maths/m4c-axis-free-representation-operators.html), for the matrices, the product, the trace, the determinant and the sixteen cells in the coefficient basis.
- [$M_4(\mathbb{C})$ Pauli Representation](../articles_maths/m4c-pauli-representation.html) and [its Operators companion](../articles_maths/m4c-pauli-representation-operators.html), for the Peirce frame, the switch and the same objects in it.
- [Two-Sided Operators on the Biquaternion Algebra](../articles_maths/two-sided-operators-on-the-biquaternion-algebra.html), for the sixteen cells, the frames of the normal form and the proof of the cell table.
- [Index, Notation and Corpus Conventions](../articles_maths/index-notation-and-corpus-conventions.html), for the superscripts, the labels and the retired names.
