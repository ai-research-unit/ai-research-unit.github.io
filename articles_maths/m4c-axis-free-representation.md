# __$M_4(\mathbb{C})$ Axis-Free Representation__

## Introduction

**The subject.** The two families of matrices of the biquaternion algebra in the coefficient basis, and the reason this basis alone gives the sixteen matrices a shape no other basis gives.

**The order of the article.** The left family is built first, from the multiplication of the algebra and from nothing else: §*The Left Family* writes the columns of the matrix as the products $\tilde Qe_\nu$, reads the multiplicativity off associativity, and displays the four matrices of the units. The right family is built second, by the same construction read on the other side (§*The Right Family*). The matrix that carries the left family onto the right one is then read off the transpose of the first (§*The Stitch Between the Two Families*). Every other frame is a conjugate of this one (§*Every Family Is a Conjugate of This One*), and the properties that this frame has and the others lack are listed, counted and weighed: the ten properties, the subring of the entries and the meaning of realness (§*What the Axis-Free Family Makes Simple*, §*The Real-Coefficient Question*), then the uniqueness of the frame among the frames with the same sparsity, and the difference between the unique operator and the conjugacy class of its matrices (§*No Other Basis Does the Same*, §*The Operator Is Unique, the Matrix Is a Class*). The product, the trace, the determinant and the six subspaces follow (§*The Product*, §*The Trace*, §*The Determinant*, §*The Six Subspaces*).

**The basis and the label.** The article works in the basis $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ of *The Biquaternion Algebra*, the one the other articles call the coefficient basis. An element is
$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad Q_\mu\in\mathbb{C},
$$
and the entries of its matrices are these coefficients with the signs of the multiplication table. §*The Axis-Free Basis* recalls the basis and says why this article renames it; the family carries the label $\mathrm{axf}$, as $L^{\mathrm{axf}}(\tilde Q)$ and $L_{e_\mu}^{\mathrm{axf}}$.

**The algebra.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$; the central scalar imaginary is $i$. Write $Q_\mu=q_\mu+iq'_\mu$ with $q_\mu,q'_\mu\in\mathbb{R}$, and put $B^2=Q_x^2+Q_y^2+Q_z^2$ and $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2=Q_t^2+Q_x^2+Q_y^2+Q_z^2$.

**The result in one line.** The four left matrices $L_{e_\mu}^{\mathrm{axf}}$ and the four right matrices $R_{e_\mu}^{\mathrm{axf}}$ are signed permutation matrices, with entries $0$ and $\pm1$ only, and each four is a basis of a four-dimensional subalgebra of $M_4(\mathbb{C})$. The left matrix of a general element is displayed in §*The Left Family*, the right matrix in §*The Right Family*, and the switch between them is the real sign matrix $D=\operatorname{diag}(1,-1,-1,-1)$. The trace is $4Q_t$, the determinant is $\langle\tilde Q\rangle_{\natural}^2=(Q_t^2+B^2)^2$, and the eigenvalues are $Q_t\pm iB$, each twice. Every other frame is $C^{-1}$ times this one times $C$, and this frame is the only one, up to relabelling the three directions and changing their signs, in which the sixteen matrices are real, integer-valued, signed permutations.

**Boundaries.** The algebra, the multiplication table and the four conjugations are *The Biquaternion Algebra* and *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra*. The general theory of the two families, of the change of frame and of the switch is *Families of Matrix Representations*; this article is one instance of it, worked out in full. The six subspaces are defined and decomposed in *Subspaces and Decompositions of the Biquaternion Algebra*; this article reads their images in the axis-free basis. The same element in the tensor-product display is *$M_4(\mathbb{C})$ Pauli Representation*, and at the element size it is *$M_2(\mathbb{C})$ Pauli Representation*.

## The Axis-Free Basis

**The basis is the one of *The Biquaternion Algebra*.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, and its basis is the tensor basis of §*The Basis and the Complexification* of *The Biquaternion Algebra*,
$$
e_t=1\otimes1,\qquad \vec e_x=1\otimes\vec e_x,\qquad \vec e_y=1\otimes\vec e_y,\qquad \vec e_z=1\otimes\vec e_z,
$$
the vector units on the right being those of $\mathbb{H}$, and the scalar imaginary $i=i\otimes1$ being central and occurring only as a coefficient. The four are a $\mathbb{C}$-basis. The element is $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with $Q_\mu=q_\mu+iq'_\mu$, which is the developed form of §*The Coordinate Systems* of *The Element, the Coordinates and the Conjugations*.

**Two names for one basis.** *Matrix Representations Conventions* calls this basis the coefficient basis, because its four coordinates are the coefficients of the developed form. This article calls the same basis axis-free, and writes the label on the family, $L^{\mathrm{axf}}(\tilde Q)$ and $L_{e_\mu}^{\mathrm{axf}}$, as that article prescribes. The superscript $\mathrm{axf}$ is a name in lowercase roman letters, not an exponent: $L_{\vec e_x}^{\mathrm{axf}}$ is the left matrix of $\vec e_x$, and its square is written $(L_{\vec e_x}^{\mathrm{axf}})^2$. The two names are not two objects; the first names the coordinates, the second names what the frame does not do.

**The structure constants.** In this basis the product is
$$
e_\mu e_\nu=\sum_\rho\varepsilon_{\mu\nu}^{\ \ \rho}\,e_\rho,\qquad
\varepsilon_{\mu\nu}^{\ \ \rho}\in\{0,+1,-1\},
$$
and the array $\varepsilon$ is the algebra: the table above is that array, written out. Every matrix below is built from $\varepsilon$ by one rule, and the rule is the one of §*The Left Family*; property (d) of §*What the Axis-Free Family Makes Simple* says that the entries of the sixteen matrices are $\varepsilon$ itself.

**The frame names no direction.** The three vector units enter every formula below by the same rule: none of them is singled out by the construction, and §*No Direction Is Privileged* develops the point. The price is that the idempotents of the algebra are not adapted to the basis. The gain is that the entries are integers and that the transpose is the conjugation (§*The Left Family*).

**The multiplication table.** The table of §*The Multiplication Table* of *The Biquaternion Algebra* is reproduced here, because the columns of the matrices built below are read from this table and from nothing else:

| $e_\mu e_\nu$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

Each of the sixteen products is $\pm$ one of the four basis elements, and the signs are those of the quaternion algebra: $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$. No complex number appears in the table, because $i$ is central and is carried by the coefficients. The two families of matrices below are this table read by columns, once with the element on the left of the column vector and once on the right, and nothing else enters their construction.

## The Left Family

**The definition.** The $\nu$-th column of the left matrix is the coordinate column of the product $\tilde Qe_\nu$,
$$
L^{\mathrm{axf}}(\tilde Q)_{\mu\nu}=\bigl[\tilde Qe_\nu\bigr]_{\mu},\qquad
L^{\mathrm{axf}}(\tilde Q):=\bigl(\bigl[\tilde Qe_t\bigr]\;\bigl[\tilde Q\vec e_x\bigr]\;\bigl[\tilde Q\vec e_y\bigr]\;\bigl[\tilde Q\vec e_z\bigr]\bigr).
$$
This is the definition of §*The Two Sides* of *Families of Matrix Representations*, read in the frame $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$. Only the multiplication of the algebra is used: each column is read off the table of §*The Axis-Free Basis*, and no further choice is made. The four matrices of the units are $L_{e_\mu}^{\mathrm{axf}}:=L^{\mathrm{axf}}(e_\mu)$.

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
The first column is $(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$, the coordinate column of $\tilde Q$ itself, because $\tilde Qe_t=\tilde Q$. The other three columns are the products of $\tilde Q$ with the three vector units, and each of them is the same rule applied to another column of the table.

**The law, and where it comes from.** For all $\tilde Q_1,\tilde Q_2$,
$$
L^{\mathrm{axf}}(\tilde Q_1\tilde Q_2)=L^{\mathrm{axf}}(\tilde Q_1)L^{\mathrm{axf}}(\tilde Q_2).
$$
This is associativity and nothing else. The $\nu$-th column of the left side is the coordinate column of $(\tilde Q_1\tilde Q_2)e_\nu$, which is $\tilde Q_1(\tilde Q_2e_\nu)$ by associativity; the $\nu$-th column of the right side is $\tilde Q_1$ applied to the coordinate column of $\tilde Q_2e_\nu$, since the matrix of $\tilde Q_1$ acts on coordinate columns by the multiplication $\tilde X\mapsto\tilde Q_1\tilde X$. The two columns agree for each $\nu$, and a matrix is its columns.

**Faithfulness.** The first column recovers $\tilde Q$, so $L^{\mathrm{axf}}(\tilde Q)=0$ if and only if $\tilde Q=0$. The assignment is therefore injective, it preserves products, and its image is a four-dimensional complex subalgebra $\mathbb{B}_L$ of $M_4(\mathbb{C})$ whose unit is $\mathrm I_4$. An element is known by its left matrix alone.

**The four left matrices.** On the units,
$$
L_{e_t}^{\mathrm{axf}}=\mathrm I_4,\qquad
L_{\vec e_x}^{\mathrm{axf}}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
$$
$$
L_{\vec e_y}^{\mathrm{axf}}=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
L_{\vec e_z}^{\mathrm{axf}}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$
Each is the corresponding column of the multiplication table, written as an array: the $z$ matrix, for instance, has $-1$ where the table sends $e_t\mapsto\vec e_z$, $\vec e_y\mapsto-\vec e_x$, $\vec e_z\mapsto-e_t$ and $\vec e_x\mapsto\vec e_y$.

**Signed permutations.** Each of the four is a signed permutation matrix: exactly one nonzero entry in each row and in each column, of modulus one. Hence each is orthogonal, $M^{\mathsf T}M=\mathrm I_4$, with entries in $\{0,+1,-1\}$. Each has determinant $1$; the identity has trace $4$ and the three vector matrices have trace $0$. The four are linearly independent, because the assignment is injective and the four units are a basis, so they are a basis of $\mathbb{B}_L$.

**The group.** The four matrices together with their negatives,
$$
\{\pm L_{e_t}^{\mathrm{axf}},\pm L_{\vec e_x}^{\mathrm{axf}},\pm L_{\vec e_y}^{\mathrm{axf}},\pm L_{\vec e_z}^{\mathrm{axf}}\},
$$
are eight distinct signed permutation matrices forming a group isomorphic to the quaternion group $Q_8$: the vector matrices square to $-\mathrm I_4$, distinct ones anticommute up to sign, and the identity is the unit. The left family of this frame is therefore a copy of $Q_8$ sitting inside $O(4)\subset M_4(\mathbb{R})$.

**The products of the basis matrices.** Write $e_\mu e_\nu=\varepsilon e_{\mu\nu}$ with $\varepsilon=\pm1$. Then
$$
L_{e_\mu}^{\mathrm{axf}}L_{e_\nu}^{\mathrm{axf}}=\varepsilon L_{e_{\mu\nu}}^{\mathrm{axf}},
$$
so the four are closed under products up to sign and the signs are the signs of the table. For example $(L_{\vec e_x}^{\mathrm{axf}})^2=-\mathrm I_4$ and $L_{\vec e_x}^{\mathrm{axf}}L_{\vec e_y}^{\mathrm{axf}}=L_{\vec e_z}^{\mathrm{axf}}=-L_{\vec e_y}^{\mathrm{axf}}L_{\vec e_x}^{\mathrm{axf}}$.

**The transpose is the conjugation.** In this frame the transpose of a left matrix is the left matrix of the conjugate element:
$$
L^{\mathrm{axf}}(\tilde Q)^{\mathsf T}=L^{\mathrm{axf}}(\tilde Q^{\natural}),\qquad
\tilde Q^{\natural}=Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z .
$$
The reason is visible in the display. Transposing swaps the entries at the $(\mu,\nu)$ and $(\nu,\mu)$ positions, and those two entries carry opposite signs exactly when $s_\mu s_\nu=-1$, with $s_t=1$ and $s_x=s_y=s_z=-1$, so every entry of the transpose is $s_\mu s_\nu$ times the corresponding entry of the display. Multiplying the three vector coefficients by $-1$ produces exactly that sign pattern. The same identity holds for the right matrices. It is a property of this frame, not of the algebra: in a general frame the transpose of a left matrix is the conjugate of a right matrix, $L(\tilde Q)^{\mathsf T}=\mathsf W R(\tilde Q)\mathsf W^{-1}$, and it is a left matrix here because the switch is diagonal.

**The dagger.** The conjugate transpose gives the star conjugate,
$$
L^{\mathrm{axf}}(\tilde Q)^{\dagger}=L^{\mathrm{axf}}(\tilde Q^{*}),
$$
because the dagger is the entrywise conjugate followed by the transpose, and the entrywise conjugate of the display is the display of the element with $Q_\mu$ replaced by $\overline{Q_\mu}$, which is the star conjugation. Both identities are checked on the four units and extended by linearity.

### No Direction Is Privileged

**The three vector units enter by one rule.** In the left matrix, the $\nu$-th column is the coordinate column of $\tilde Qe_\nu$. The scalar column is the column of $\tilde Q$ itself, and each of the three vector columns is obtained from the same table by the same substitution. The display has $Q_t$ on the diagonal and the three vector coefficients off it, with no coefficient singled out by its position:
$$
L^{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&-Q_z&Q_y\\
Q_y&Q_z&Q_t&-Q_x\\
Q_z&-Q_y&Q_x&Q_t
\end{pmatrix}.
$$
The entries in the $x$, $y$ and $z$ positions have the same shape: one coefficient with a sign, and no sum. The right matrix has the same property.

**The symmetry is the cyclic one.** A cyclic permutation of the three directions, $x\mapsto y\mapsto z\mapsto x$, preserves the quaternion relations and is an algebra automorphism; the permutation matrix of that relabelling conjugates $L^{\mathrm{axf}}(\tilde Q)$ into itself. A transposition reverses the orientation: it sends $\vec e_x\vec e_y=\vec e_z$ to $\vec e_y\vec e_x=-\vec e_z$, so it changes the signs of the table. That sign is a property of the quaternion algebra, not a preference of the axis-free basis. The basis treats the three directions equally; the algebra itself has the cyclic orientation of the quaternion product.

**No axis is chosen.** The three vector units enter the display by the same rule, so no one of them is singled out by the construction. The basis names no direction as preferred, and the multiplication table is the only structure used. This is why the six subspaces are read entrywise in §*The Six Subspaces*: the real, imaginary, Hermitian and anti-Hermitian conditions do not depend on a choice of axis.

## The Right Family

**The definition.** The $\nu$-th column of the right matrix is the coordinate column of the product $\vec e_\nu\tilde Q$, with the element on the other side:
$$
R^{\mathrm{axf}}(\tilde Q)_{\mu\nu}=\bigl[\vec e_\nu\tilde Q\bigr]_{\mu},\qquad
R^{\mathrm{axf}}(\tilde Q):=\bigl(\bigl[e_t\tilde Q\bigr]\;\bigl[\vec e_x\tilde Q\bigr]\;\bigl[\vec e_y\tilde Q\bigr]\;\bigl[\vec e_z\tilde Q\bigr]\bigr).
$$
The construction is the same as the left one with the order of the two factors exchanged, and it uses the same table.

**The display.** In the same basis,
$$
R^{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&Q_z&-Q_y\\
Q_y&-Q_z&Q_t&Q_x\\
Q_z&Q_y&-Q_x&Q_t
\end{pmatrix}.
$$
The two displays agree on the diagonal and in the first column, and differ in the signs of the six entries where one index is scalar and the other is vector. They are different arrays for the same element.

**The law, and where it comes from.** For all $\tilde Q_1,\tilde Q_2$,
$$
R^{\mathrm{axf}}(\tilde Q_1\tilde Q_2)=R^{\mathrm{axf}}(\tilde Q_2)R^{\mathrm{axf}}(\tilde Q_1).
$$
The product is carried backwards. This is associativity read on the other side: the $\nu$-th column of the left side is the coordinate column of $\vec e_\nu(\tilde Q_1\tilde Q_2)$, and associativity turns it into $(\vec e_\nu\tilde Q_1)\tilde Q_2$, which is the action of $\tilde Q_2$ on the coordinate column of $\vec e_\nu\tilde Q_1$; the columns therefore compose in the reverse order. The powers and the inverses are not reversed, since they involve one element only:
$$
R^{\mathrm{axf}}(\tilde Q^n)=R^{\mathrm{axf}}(\tilde Q)^n,\qquad
R^{\mathrm{axf}}(\tilde Q^{-1})=R^{\mathrm{axf}}(\tilde Q)^{-1}.
$$

**The two families commute.** For all $\tilde Q_1,\tilde Q_2$,
$$
L^{\mathrm{axf}}(\tilde Q_1)R^{\mathrm{axf}}(\tilde Q_2)=R^{\mathrm{axf}}(\tilde Q_2)L^{\mathrm{axf}}(\tilde Q_1).
$$
The two factors sit on opposite sides of the argument and never meet: the left matrix acts by $\tilde Q_1$ on the left and the right matrix by $\tilde Q_2$ on the right, and the order of the two acts is immaterial. So $\mathbb{B}_L$ lies in the commutant of $\mathbb{B}_R$ and conversely.

**Faithfulness and the invariants.** The right assignment is injective for the same reason as the left one, since $\vec e_t\tilde Q=\tilde Q=\tilde Qe_t$, and its image is a four-dimensional complex subalgebra $\mathbb{B}_R$. The two families meet in the scalars: $L^{\mathrm{axf}}(\tilde Q)=R^{\mathrm{axf}}(\tilde Q)$ says that $\tilde Q$ commutes with every element, that is $\tilde Q\in\mathbb{C}e_t$, and then the common matrix is $\lambda\mathrm I_4$. The trace, the determinant, the characteristic polynomial and the rank are the same in the two families, because the switch of the next section is a transposition followed by a conjugation.

**The four right matrices.** On the units,
$$
R_{e_t}^{\mathrm{axf}}=\mathrm I_4,\qquad
R_{\vec e_x}^{\mathrm{axf}}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},
$$
$$
R_{\vec e_y}^{\mathrm{axf}}=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
R_{\vec e_z}^{\mathrm{axf}}=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$
Each is a signed permutation matrix of determinant $1$ and trace $4\delta_{\mu t}$, and the four are a basis of $\mathbb{B}_R$. The products follow the reverse order, $R_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}}=\varepsilon' R_{e_{\nu\mu}}^{\mathrm{axf}}$ with $e_\nu e_\mu=\varepsilon' e_{\nu\mu}$, so for instance $R_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=-R_{\vec e_z}^{\mathrm{axf}}$, the opposite sign to the left family. The four together with their negatives are again $Q_8$.

## The Stitch Between the Two Families

**The general rule.** In any frame, the right matrix is the transpose of the left one between the switch matrix and its inverse,
$$
R(\tilde Q)=\mathsf W^{-1}L(\tilde Q)^{\mathsf T}\mathsf W,
$$
where $\mathsf W$ is the Gram matrix of the symmetric form $\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y)$ on the frame. This is the theorem of *Families of Matrix Representations*. The rest of this section computes $\mathsf W$ in the axis-free basis and displays the resulting identity.

**The switch of this frame.** The Gram matrix of $\beta$ on the four units is
$$
\beta(e_\mu,e_\nu)=\operatorname{Sc}(e_\mu e_\nu)=
\begin{cases}
1,&\mu=\nu=t,\\
-1,&\mu=\nu\in\{x,y,z\},\\
0,&\mu\neq\nu,
\end{cases}
$$
because the product of two distinct units is a third unit, of zero scalar part, and a vector unit squares to $-e_t$. So
$$
\mathsf W=D=\begin{pmatrix}1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&0&-1\end{pmatrix}=\operatorname{diag}(1,-1,-1,-1).
$$
The matrix $D$ is real, symmetric and diagonal, $D^2=\mathrm I_4$, and $\det D=-1$. It is also the matrix of the conjugation in this basis, since $\tilde Q^{\natural}$ is $\tilde Q$ with the three vector coefficients negated.

**The stitch.** With $\mathsf W=D$ the general rule reads
$$
R^{\mathrm{axf}}(\tilde Q)=D\,L^{\mathrm{axf}}(\tilde Q)^{\mathsf T}D
=D\,L^{\mathrm{axf}}(\tilde Q^{\natural})\,D,
$$
the second form using the transpose identity of §*The Left Family*. The switch is applied on the left and on the right, and no complex number appears in it.

**The entry rule.** Reading the identity entry by entry,
$$
R^{\mathrm{axf}}(\tilde Q)_{\mu\nu}=s_\mu s_\nu\,L^{\mathrm{axf}}(\tilde Q)_{\nu\mu},
\qquad s_t=1,\quad s_x=s_y=s_z=-1 .
$$
So the $(\mu,\nu)$ entry of the right matrix is the transposed left entry, kept when the two indices are both scalar or both vector, and reversed when one is scalar and the other vector. That is the whole difference between the two displays: six of the sixteen entries.

**The stitch in full.** The transpose of the left matrix is
$$
L^{\mathrm{axf}}(\tilde Q)^{\mathsf T}=
\begin{pmatrix}
Q_t&Q_x&Q_y&Q_z\\
-Q_x&Q_t&Q_z&-Q_y\\
-Q_y&-Q_z&Q_t&Q_x\\
-Q_z&Q_y&-Q_x&Q_t
\end{pmatrix},
$$
the left multiplication by $D$ changes the sign of the last three rows,
$$
D\,L^{\mathrm{axf}}(\tilde Q)^{\mathsf T}=
\begin{pmatrix}
Q_t&Q_x&Q_y&Q_z\\
Q_x&-Q_t&-Q_z&Q_y\\
Q_y&Q_z&-Q_t&-Q_x\\
Q_z&-Q_y&Q_x&-Q_t
\end{pmatrix},
$$
and the right multiplication by $D$ changes the sign of the last three columns. Written with $D$ on both sides,
$$
R^{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
1&0&0&0\\
0&-1&0&0\\
0&0&-1&0\\
0&0&0&-1
\end{pmatrix}
\begin{pmatrix}
Q_t&Q_x&Q_y&Q_z\\
-Q_x&Q_t&Q_z&-Q_y\\
-Q_y&-Q_z&Q_t&Q_x\\
-Q_z&Q_y&-Q_x&Q_t
\end{pmatrix}
\begin{pmatrix}
1&0&0&0\\
0&-1&0&0\\
0&0&-1&0\\
0&0&0&-1
\end{pmatrix}
=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&Q_z&-Q_y\\
Q_y&-Q_z&Q_t&Q_x\\
Q_z&Q_y&-Q_x&Q_t
\end{pmatrix}.
$$
The two multiplications by $D$ are the two sign changes: one on the rows, one on the columns.

**Why the stitch works.** The $\mu\nu$ entry of $L^{\mathrm{axf}}(\tilde Q)$ is the coefficient of $e_\mu$ in $\tilde Qe_\nu$; the $\mu\nu$ entry of $R^{\mathrm{axf}}(\tilde Q)$ is the coefficient of $e_\mu$ in $e_\nu\tilde Q$. Conjugating $\tilde Q^{\natural}e_\nu$ gives $(\tilde Q^{\natural}e_\nu)^{\natural}=s_\nu\,e_\nu\tilde Q$, so the coefficient of $e_\mu$ in $e_\nu\tilde Q$ is $s_\mu s_\nu$ times the coefficient of $e_\mu$ in $\tilde Q^{\natural}e_\nu$. Hence $R^{\mathrm{axf}}(\tilde Q)=DL^{\mathrm{axf}}(\tilde Q^{\natural})D$. The same computation in a general frame produces the general $\mathsf W$, which is why the switch is a Gram matrix and not a chosen array.

**An involution, and what it preserves.** Applying the stitch twice returns the left matrix, because $D^2=\mathrm I_4$ and transposition is an involution. The stitch preserves the trace and the determinant, since neither a transposition nor a conjugation by a fixed matrix changes them:
$$
\operatorname{Tr}R^{\mathrm{axf}}(\tilde Q)=\operatorname{Tr}L^{\mathrm{axf}}(\tilde Q),\qquad
\det R^{\mathrm{axf}}(\tilde Q)=\det L^{\mathrm{axf}}(\tilde Q).
$$

**The sixteen products.** The products $L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}}$ are again signed permutation matrices, and they form an orthogonal basis of $M_4(\mathbb{C})$:
$$
\operatorname{Tr}\bigl((L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}})^{\mathsf T}L_{e_\rho}^{\mathrm{axf}}R_{e_\sigma}^{\mathrm{axf}}\bigr)=4\,\delta_{\mu\rho}\delta_{\nu\sigma}.
$$
The transpose suffices because the sixteen are real. So every $4\times4$ matrix is a unique complex combination of the sixteen, with coefficients $\tfrac14\operatorname{Tr}((L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}})^{\mathsf T}M)$.

**What the image is.** The ambient $M_4(\mathbb{C})$ has complex dimension sixteen and $\mathbb{B}_L$ has complex dimension four, so twelve dimensions are transverse to the image. No image has odd rank: the rank is twice the rank of the $2\times2$ matrix of the element, hence $0$, $2$ or $4$. A matrix of rank one or three is a general matrix of the ambient and not the left matrix of any element.

## Every Family Is a Conjugate of This One

**The change of frame.** Let $\mathcal{F}'$ be another basis and $\mathsf C$ the matrix whose columns are its vectors in the axis-free basis, so that the coordinate columns change by $[x]_{\mathcal{E}}=\mathsf C[x]_{\mathcal{F}'}$. Then
$$
L_{\mathcal{F}'}(\tilde Q)=\mathsf C^{-1}L^{\mathrm{axf}}(\tilde Q)\,\mathsf C,\qquad
R_{\mathcal{F}'}(\tilde Q)=\mathsf C^{-1}R^{\mathrm{axf}}(\tilde Q)\,\mathsf C,\qquad
\mathsf W_{\mathcal{F}'}=\mathsf C^{\mathsf T}D\,\mathsf C .
$$
One matrix serves both families, because the frame is a property of the carrier and the side is a property of the action; and the switch moves by congruence, because it is the matrix of a bilinear form.

**A single orbit.** Every family of left matrices and every family of right matrices arises this way, from one $\mathsf C\in GL_4(\mathbb{C})$. So the families form one orbit, and what changes from frame to frame is the display: the entries, the sparsity, the subring of $\mathbb{C}$ in which the entries lie, the subspaces $\mathbb{B}_L$ and $\mathbb{B}_R$ of $M_4(\mathbb{C})$, and the switch. What does not change is the element: the trace $4Q_t$, the determinant $\langle\tilde Q\rangle_{\natural}^2$, the characteristic polynomial, the spectrum, the rank and the dimensions of the two annihilators are the same in every frame, as the table of *Families of Matrix Representations* records. No property of an element can be true in one frame and false in another; only a property of the display can.

**A caution about identities.** An identity that holds in one frame need not hold in another. The transpose identity is the example: $L^{\mathrm{axf}}(\tilde Q)^{\mathsf T}=L^{\mathrm{axf}}(\tilde Q^{\natural})$ holds here and fails in a frame whose switch is not $D$. What survives every frame is the general relation $L(\tilde Q)^{\mathsf T}=\mathsf W R(\tilde Q)\mathsf W^{-1}$, with $\mathsf W$ the switch of the frame at hand. So the transpose is the conjugation only where $\mathsf W=D$, and that is one reason this frame is kept.

## What the Axis-Free Family Makes Simple

**The ten properties.** In the axis-free basis the sixteen matrices $L_{e_\mu}^{\mathrm{axf}}$ and $R_{e_\nu}^{\mathrm{axf}}$ have all of the following at once.

**(a) The entries are integers.** Every entry lies in $\{0,+1,-1\}\subset\mathbb{Z}\subset\mathbb{R}$. No imaginary unit appears anywhere.

**(b) They are signed permutation matrices.** Exactly one nonzero entry in each row and in each column, of modulus one.

**(c) They are orthogonal over $\mathbb{R}$.** Each satisfies $M^{\mathsf T}M=\mathrm I_4$, so the left family lies in $O(4)$; being real, each is also unitary.

**(d) The entries are the structure constants.** The matrices are the array $\varepsilon$ of §*The Axis-Free Basis*, read by columns. Nothing is rescaled and nothing is rotated.

**(e) The transpose is the conjugation.** $L(\tilde Q)^{\mathsf T}=L(\tilde Q^{\natural})$, and the same for $R$.

**(f) The switch is real and diagonal.** $R=DL^{\mathsf T}D$ with $D=\operatorname{diag}(1,-1,-1,-1)\in M_4(\mathbb{R})$.

**(g) The quaternion group sits on $\mathbb{R}^4$.** The eight matrices $\pm L_{e_\mu}^{\mathrm{axf}}$ are exactly $Q_8$, as signed permutations of the four coordinates.

**(h) The three directions are cyclically symmetric.** A cyclic permutation $x\mapsto y\mapsto z\mapsto x$ conjugates every matrix by a permutation matrix, and no vector direction is singled out.

**(i) The real slice is preserved.** A quaternion, that is an element with real coefficients, has a real matrix; $\mathbb{H}\subset\mathbb{B}$ lands in $M_4(\mathbb{R})$.

**(j) The determinant is one and the trace is $4\delta_{\mu t}$.** $\det L_{e_\mu}^{\mathrm{axf}}=\det R_{e_\mu}^{\mathrm{axf}}=1$, and the trace is $4$ on the identity and $0$ on the three vector matrices.

**Ten readings of one fact.** The root is (b) together with (d): the basis is multiplicative, $e_\mu e_\nu=\pm e_{\mu\nu}$, so the columns of the matrices are signed basis vectors and the entries are $\pm1$. From that, (a) and (c) follow at once, and (d) holds by construction. Property (e) is the sign bookkeeping of the transpose, computed in §*The Left Family* and re-read in §*The Real-Coefficient Question*; (f) is the computation of the Gram matrix of $\beta$, and it gives $D$ because the units are orthogonal for $\beta$ with norms $1$ and $-1$; (g) is the closure of the four matrices under products up to sign; (h) is the cyclic symmetry of the quaternion relations; (i) is the reality of the table; (j) is the trace and the determinant of a signed permutation. The ten are one structure seen ten ways.

### The Real-Coefficient Question

**The question.** Whether the sixteen arrays have real entries, and what that property costs and buys.

**The ladder of subrings.** The entries lie in $\{0,+1,-1\}\subset\mathbb{Z}$, and both signs occur, so the entries generate $\mathbb{Z}$ and no smaller subring of $\mathbb{C}$ can hold them. A change of frame by a matrix $\mathsf C$ whose entries and whose inverse's entries lie in a subring $R$ gives entries in $R$, because $\mathsf C^{-1}L\mathsf C$ is a sum of products of such entries; a generic $\mathsf C$ gives $\mathbb{C}$. The subring of the entries is therefore a property of the change matrix and not of the algebra, and the ladder $\mathbb{Z}\subset\mathbb{Z}[i]\subset\mathbb{C}$ classifies the frames by how far the change matrix has travelled from the identity.

**Realness is a consequence, not a characterisation.** Every real change of frame of this one is another real frame (§*No Other Basis Does the Same*), so realness alone names no frame. What names this one is the simultaneous bundle (a)–(j), and the bundle says that the basis is the multiplication table itself.

**What realness buys.** Property (a) and property (c) together give (b): an integer matrix whose columns are orthonormal has each column an integer vector of squared length one, that is, a single entry $\pm1$; an integer orthogonal matrix is a signed permutation. Property (b) alone gives (e): a signed permutation matrix is orthogonal, so its transpose is its inverse, and the inverse of $L_{e_\mu}^{\mathrm{axf}}$ is $L_{e_\mu^{-1}}^{\mathrm{axf}}=L_{e_\mu^{\natural}}^{\mathrm{axf}}$. The transpose identity for every element follows by linearity. So the transpose is the conjugation is not an extra computation: it is the sparsity of the display, read twice.

**What realness does not buy.** It gives no privileged frame and no new invariant. The trace, the determinant and the spectrum are the same over the whole orbit (§*Every Family Is a Conjugate of This One*), and realness is one row of the list and not the list.

## No Other Basis Does the Same

**The statement.** Let $\mathcal{F}$ be a basis of $\mathbb{B}$ in which all sixteen matrices of the four units are signed permutations. Then, after a relabelling of the indices,
$$
f_t=\pm e_t,\qquad f_k=\pm e_{\sigma(k)}\quad(k=x,y,z),\qquad \sigma\in S_3 .
$$
So such a basis is the axis-free basis up to a permutation of the three vector directions and a sign change of each basis element.

**The count.** The sign choices give $2^4$ and the permutations of the three directions give $3!$. With the scalar unit in the first slot, as the axis-free basis has it, there are $3!\cdot2^4=96$ such bases; if the scalar unit is also fixed at $+e_t$ there are $3!\cdot2^3=48$; and if the four slots are free there are $4!\cdot2^4=384$ orderings. Every one of them is the axis-free family conjugated by a signed permutation matrix, so every one of them is the same family relabelled.

**The first step of the proof.** Each column of $L_{f_\mu}$ is a signed basis vector, so
$$
f_\mu f_\nu=\varepsilon_{\mu\nu}f_{\sigma_\mu(\nu)},\qquad
\varepsilon_{\mu\nu}=\pm1,\quad\sigma_\mu\in S_4,
$$
for each $\mu$. Write $e_t=\sum_\nu a_\nu f_\nu$ and multiply on the left by $f_\mu$:
$$
f_\mu=\sum_\nu a_\nu f_\mu f_\nu=\sum_\nu a_\nu\varepsilon_{\mu\nu}f_{\sigma_\mu(\nu)} .
$$
Comparing the coefficients of the basis on the two sides gives $a_{\sigma_\mu^{-1}(\rho)}\varepsilon_{\mu,\sigma_\mu^{-1}(\rho)}=\delta_{\mu\rho}$, so for each $\mu$ the array $a$ is supported at the single index $\sigma_\mu^{-1}(\mu)$. One array cannot have four different supports, so that index is the same for all $\mu$: there is a $\nu_0$ with $\sigma_\mu(\nu_0)=\mu$ for every $\mu$. Then $e_t=a_{\nu_0}f_{\nu_0}$, that is $f_{\nu_0}=a_{\nu_0}^{-1}e_t$, and substituting into $f_\mu f_{\nu_0}=\varepsilon_{\mu\nu_0}f_\mu$ gives $a_{\nu_0}^{-1}=\pm1$. Hence one basis element is $\pm e_t$.

**The rest.** From there the check is finite: the three remaining vectors are fixed by their own sixteen products, and the sign patterns that remain return only $\pm\vec e_x,\pm\vec e_y,\pm\vec e_z$ in some order. The converse is immediate: if $f_t=\pm e_t$ and $f_k=\pm e_{\sigma(k)}$, the products $f_\mu f_\nu$ are again $\pm$ a basis vector, by the table of the algebra.

**Among the real frames, no uniqueness.** Every real change of basis $C\in GL_4(\mathbb{R})$ applied to the axis-free basis gives another real frame, with $L'=C^{-1}LC$. The real frames are therefore a sixteen-dimensional family, and their entries are in general arbitrary real numbers. Realness alone does not characterise the axis-free frame; realness together with sparsity — signed permutations — does.

**Among all the frames, no uniqueness at all.** Every basis gives a family, so there are as many families as bases, and they are one orbit under $GL_4(\mathbb{C})$. The axis-free basis is distinguished by the simultaneous presence of (a)–(j), not by being the only family with real entries.

**What the statement does not say.** It does not say that the axis-free family is "the" matrix representation of the algebra, and it gives the frame no privileged role in the computation of an element: the element is the same in all frames. It says that if the arrays are to be the multiplication table, real, integer-valued and signed permutations, then there is exactly one way to have it, and the axis-free basis is that way.

### The Operator Is Unique, the Matrix Is a Class

**The map has no frame.** Left multiplication, $\rho_L(\tilde Q)(\tilde X)=\tilde Q\tilde X$, is defined by the product alone. It is the same linear map of $\mathbb{B}$ in every frame, and no array enters its definition.

**The array has a frame.** The matrix $L(\tilde Q)$ is the array of that map in one frame, and a change of frame conjugates it. So the matrices of one element over all frames form one conjugacy class and not one matrix: the trace, the determinant and the spectrum are the same in all of them, the entries are not, and a statement about entries is a statement about a display.

**The canonical representative.** Inside the class the axis-free family is the unique representative, up to the $96$ bases counted above, whose sixteen arrays are signed permutations. The frame is canonical in this precise sense: not the only frame and not the only real frame, but the only one in which the structure constants are the entries.

**The trade.** A change of frame whose matrix leaves $\mathbb{Z}$ costs the integers first, and with them the sparsity, the orthogonality and the real diagonal switch; the transpose identity goes with the switch. What survives every frame is the operator, and the operator is the subject of the article.

**Two lines.** The operator is unique. The matrix is a conjugacy class. The axis-free family is the representative of the class in which the structure constants are read off the display.

## The Product

**The left and the right products.** For all $\tilde Q_1,\tilde Q_2$,
$$
L^{\mathrm{axf}}(\tilde Q_1\tilde Q_2)=L^{\mathrm{axf}}(\tilde Q_1)L^{\mathrm{axf}}(\tilde Q_2),\qquad
R^{\mathrm{axf}}(\tilde Q_1\tilde Q_2)=R^{\mathrm{axf}}(\tilde Q_2)R^{\mathrm{axf}}(\tilde Q_1).
$$
The left family is multiplicative and the right family is anti-multiplicative. The difference is the order of the factors, and it is the same difference as between $\tilde Q_1\tilde Q_2$ and $\tilde Q_2\tilde Q_1$. Both identities are the associativity of the product, read on one side or the other.

**The powers and the inverse.** For every $\tilde Q$ and every integer $n$,
$$
L^{\mathrm{axf}}(\tilde Q^n)=L^{\mathrm{axf}}(\tilde Q)^n,\qquad
R^{\mathrm{axf}}(\tilde Q^n)=R^{\mathrm{axf}}(\tilde Q)^n,
$$
and for invertible $\tilde Q$,
$$
L^{\mathrm{axf}}(\tilde Q^{-1})=L^{\mathrm{axf}}(\tilde Q)^{-1},\qquad
R^{\mathrm{axf}}(\tilde Q^{-1})=R^{\mathrm{axf}}(\tilde Q)^{-1},
$$
the last when $\tilde Q$ is invertible. The powers and the inverse are not reversed, since they involve one element only.

**The two families commute.** For all $\tilde Q_1,\tilde Q_2$,
$$
L^{\mathrm{axf}}(\tilde Q_1)R^{\mathrm{axf}}(\tilde Q_2)=R^{\mathrm{axf}}(\tilde Q_2)L^{\mathrm{axf}}(\tilde Q_1).
$$
The identity is the associativity of the product, read on the two sides. It says that $\mathbb{B}_L$ and $\mathbb{B}_R$ are mutual commutants inside the ambient matrix algebra.

## The Trace

**The trace is the scalar part.** For every $\tilde Q$,
$$
\operatorname{Tr}L^{\mathrm{axf}}(\tilde Q)=\operatorname{Tr}R^{\mathrm{axf}}(\tilde Q)=4Q_t.
$$
The trace is the sum of the four diagonal entries, each equal to $Q_t$; the factor $4$ is the dimension of $\mathbb{B}$. The trace sees the scalar part and no vector coefficient.

**The trace of a basis matrix.** On the basis,
$$
\operatorname{Tr}L_{e_t}^{\mathrm{axf}}=\operatorname{Tr}R_{e_t}^{\mathrm{axf}}=4,\qquad
\operatorname{Tr}L_{\vec e_x}^{\mathrm{axf}}=\operatorname{Tr}L_{\vec e_y}^{\mathrm{axf}}=\operatorname{Tr}L_{\vec e_z}^{\mathrm{axf}}=0,
\qquad
\operatorname{Tr}R_{\vec e_x}^{\mathrm{axf}}=\operatorname{Tr}R_{\vec e_y}^{\mathrm{axf}}=\operatorname{Tr}R_{\vec e_z}^{\mathrm{axf}}=0.
$$
The trace is $\mathbb{C}$-linear and additive. It is not multiplicative; the trace of a product is not the product of the traces.

**The trace of a product.** For all $\tilde Q_1,\tilde Q_2$,
$$
\operatorname{Tr}\bigl(L^{\mathrm{axf}}(\tilde Q_1)L^{\mathrm{axf}}(\tilde Q_2)\bigr)
=4\operatorname{Sc}(\tilde Q_1\tilde Q_2),
$$
where $\operatorname{Sc}$ is the scalar part. The identity is the trace of the left matrix of the product, read through the preceding formula. The same identity holds for two right matrices. A left and a right matrix give
$$
\operatorname{Tr}\bigl(L^{\mathrm{axf}}(\tilde Q_1)R^{\mathrm{axf}}(\tilde Q_2)\bigr)=4Q_{1t}Q_{2t};
$$
the mixed trace sees the two scalar parts only.

## The Determinant

**The determinant is the square of the central scalar.** For every $\tilde Q$,
$$
\det L^{\mathrm{axf}}(\tilde Q)=\det R^{\mathrm{axf}}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^2
=(Q_t^2+B^2)^2.
$$
The determinant is the square of the $2\times2$ determinant, since the $2\times2$ image has determinant $\langle\tilde Q\rangle_{\natural}$. It is a quartic in the four coefficients, and it vanishes exactly on the null cone $\langle\tilde Q\rangle_{\natural}=0$.

**The characteristic polynomial.** The characteristic polynomial of $L^{\mathrm{axf}}(\tilde Q)$ is
$$
\chi_{L^{\mathrm{axf}}(\tilde Q)}(\lambda)
=\bigl(\lambda^2-2Q_t\lambda+\langle\tilde Q\rangle_{\natural}\bigr)^2
=\bigl((\lambda-Q_t)^2+B^2\bigr)^2 .
$$
The eigenvalues are $\lambda_\pm=Q_t\pm iB$, where $B$ is a square root of $B^2=Q_x^2+Q_y^2+Q_z^2$, each with algebraic multiplicity two. Their sum is $4Q_t$, their product is $\langle\tilde Q\rangle_{\natural}^2$, and the two facts are the trace and the determinant. The same polynomial is the characteristic polynomial of $R^{\mathrm{axf}}(\tilde Q)$, because the two matrices are conjugate by $D$ and transposition.

**The determinant is multiplicative.** For all $\tilde Q_1,\tilde Q_2$,
$$
\det L^{\mathrm{axf}}(\tilde Q_1\tilde Q_2)=\det L^{\mathrm{axf}}(\tilde Q_1)\det L^{\mathrm{axf}}(\tilde Q_2),
$$
and the same identity holds for $R^{\mathrm{axf}}$. The determinant is the multiplicative invariant of the algebra; the trace is the additive one.

**The basis determinants.** Every basis matrix has determinant $1$:
$$
\det L_{e_\mu}^{\mathrm{axf}}=\det R_{e_\mu}^{\mathrm{axf}}=1\qquad(\mu=t,x,y,z).
$$
The determinant of a sum is not the sum of the determinants; a sum of two invertible matrices can be singular, as $L_{\vec e_x}^{\mathrm{axf}}+R_{\vec e_x}^{\mathrm{axf}}$ shows.

**The invertibility and the rank.** The following are equivalent: $\tilde Q$ is invertible; $\langle\tilde Q\rangle_{\natural}\neq0$; $\mathsf M_2(\tilde Q)$ is invertible; $L^{\mathrm{axf}}(\tilde Q)$ is invertible; $R^{\mathrm{axf}}(\tilde Q)$ is invertible. When $\langle\tilde Q\rangle_{\natural}=0$, the rank of the $4\times4$ matrix is $0$, $2$ or $4$, never $1$ or $3$, because the matrix is two equal copies of the $2\times2$ image. The rank is twice the rank of $\mathsf M_2(\tilde Q)$.

**The doubling rule.** Every quantity of the $2\times2$ size changes in one of three ways at the $4\times4$ size.

| Quantity | Entry size | Regular size | Rule |
|---|---|---|---|
| trace | $2Q_t$ | $4Q_t$ | double |
| determinant | $\langle\tilde Q\rangle_{\natural}$ | $\langle\tilde Q\rangle_{\natural}^2$ | square |
| characteristic polynomial | degree $2$ | its square | square |
| spectrum | $\lambda_\pm$, once each | each twice | repeat |
| rank | $r$ | $2r$ | double |
| adjugate | $(\operatorname{Tr}A)\mathrm I_2-A$ | $\langle\tilde Q\rangle_{\natural}M^{\mathsf T}$ | changes shape |
| inverse | $\operatorname{adj}A/\det A$ | $M^{\mathsf T}/\langle\tilde Q\rangle_{\natural}$ | changes shape |
| minimal polynomial | degree $2$ | degree $2$ | unchanged |

The first five rows are the block form: the $4\times4$ matrix is two copies of the $2\times2$ image, so additive quantities double, multiplicative ones square, and the spectrum is repeated. The last three are not consequences of the block form, and each is a place where a formula must be rewritten rather than rescaled. The minimal polynomial is the striking case: the characteristic polynomial squares and the minimal polynomial does not, because the square of the characteristic polynomial is not the minimal polynomial.

**The adjugate.** The adjugate of the $4\times4$ matrix is
$$
\operatorname{adj}M=\det(M)M^{-1}=\langle\tilde Q\rangle_{\natural}M^{\mathsf T},
$$
using the identity $M^{-1}=M^{\mathsf T}/\langle\tilde Q\rangle_{\natural}$ above. It is of degree three in the entries of $M$, and it is not $(\operatorname{Tr}M)\mathrm I_4-M$, which is linear. The iteration is
$$
\operatorname{adj}\bigl(\operatorname{adj}M\bigr)=\langle\tilde Q\rangle_{\natural}^4M,
$$
so the adjugate is not an involution at this size, in contrast with the $2\times2$ size, where $\operatorname{adj}(\operatorname{adj}A)=A$. It remains an anti-automorphism, $\operatorname{adj}(M_1M_2)=\operatorname{adj}M_2\operatorname{adj}M_1$, and it is not one of the four words $M$, $M^{\mathsf T}$, $M^{*}$, $M^{\dagger}$: it is $\langle\tilde Q\rangle_{\natural}$ times the first of them.

**The transpose is used here, and not elsewhere.** Both formulas above use $M^{\mathsf T}=M^{\natural}$, which holds in the axis-free basis. In a frame where the transpose is another word, the same adjugate is $\langle\tilde Q\rangle_{\natural}$ times the matrix of $\natural$, and the transpose must be replaced by the conjugation.

## The Four Norms

**Four quarter-traces.** The determinant is one of four quadratic invariants of the element. Each is the quarter-trace of a word in $M$, and the quarter is the price of the block: a trace of the $4\times4$ matrix is twice the trace of the $2\times2$ matrix, so a quadratic word in the $4\times4$ matrix has four times the $2\times2$ value.

| Norm | Algebra value | Matrix formula | Value ring | Definite |
|---|---|---|---|---|
| Plain $P$ | $Q_t^2-B^2$ | $\tfrac14\operatorname{Tr}(M^2)$ | $\mathbb{C}$ | no |
| Quaternionic $N$ | $Q_t^2+B^2$ | $\tfrac14\operatorname{Tr}(M^{\mathsf T}M)$ | $\mathbb{C}$ | no |
| Hermitian $H$ | $\sum_\mu\lvert Q_\mu\rvert^2$ | $\tfrac14\operatorname{Tr}(M^{\dagger}M)$ | $\mathbb{R}$ | yes |
| Krein $K$ | $\lvert Q_t\rvert^2-\sum_k\lvert Q_k\rvert^2$ | $\tfrac14\operatorname{Tr}(M^{\mathsf T}M^{\dagger})$ | $\mathbb{R}$ | no |

**The plain norm.** The identity $\operatorname{Tr}(\mathsf M_2(\vec Q)^2)=-2B^2$, together with $\operatorname{Tr}(\mathsf M_2(\vec Q))=0$ and $\operatorname{Tr}\mathrm I_4=4$, gives
$$
\operatorname{Tr}(M^2)=4(Q_t^2-B^2)=4P .
$$
The word is the square of the $4\times4$ matrix closed by a trace. Since $\operatorname{Tr}(M^2)=2\operatorname{Tr}(A^2)$ and $\operatorname{Tr}(A^2)=2P$ for the $2\times2$ image $A$, the factor $4$ is the product of the repetition of the block and the factor $2$ of the trace of $A^2$.

**The quaternionic norm.** In this basis $M^{\mathsf T}=M^{\natural}$, so
$$
M^{\mathsf T}M=M(\tilde Q^{\natural}\tilde Q)=M\bigl(\langle\tilde Q\rangle_{\natural}e_t\bigr)=\langle\tilde Q\rangle_{\natural}\mathrm I_4,
$$
and the quarter-trace is $N$. The determinant is the square of the same number, and it is the only one of the four that is multiplicative.

**The Hermitian norm.** The dagger is the entrywise conjugate transpose, so
$$
\operatorname{Tr}(M^{\dagger}M)=\sum_{ij}\lvert M_{ij}\rvert^2=2\sum_{ij}\lvert\mathsf M_2(\tilde Q)_{ij}\rvert^2=4H .
$$
It is a quarter of the square of the Hilbert–Schmidt norm of the $4\times4$ matrix and a half of the square of that of the $2\times2$ matrix, and it is the only one of the four that is positive definite on the complex algebra.

**The Krein norm.** The mixed word is the one of the $2\times2$ model in the same basis,
$$
\operatorname{Tr}(M^{\mathsf T}M^{\dagger})=\operatorname{Tr}\bigl(M(\tilde Q^{\natural})M(\tilde Q^{*})\bigr)=4K,
$$
because the product of the two conjugates has scalar part $K$. The norm is positive on the centre and negative on the vector subspace, of signature $(2,6)$ on the real algebra.

**The basis again.** The second and fourth rows use $M^{\mathsf T}=M^{\natural}$, which is a property of the axis-free basis and not of the algebra. In a frame where the transpose is another word, the two words must be written with the conjugation, and $\tfrac14\operatorname{Tr}(M^{\mathsf T}M)$ is then none of the four norms: the entries of the transposed matrix are not the coefficients of the conjugate element, and the quarter-trace is a different quadratic form.

## The Six Subspaces

**The table.** The six remarkable subspaces are defined in *Subspaces and Decompositions of the Biquaternion Algebra*. On the image of the axis-free representation they become the conditions of the table. Write $\vec q=(q_x,q_y,q_z)$ and $\vec q'=(q'_x,q'_y,q'_z)$ for the split $Q_\mu=q_\mu+iq'_\mu$, and recall $B^2=Q_x^2+Q_y^2+Q_z^2$. In the third column, $\overline M$ is the entrywise complex conjugate of $M$ and $M^{\dagger}=\overline M^{\mathsf T}$; $\mathsf M_2(\tilde Q)$ is the $2\times2$ image of $\tilde Q$. The table gives the condition on $M=L^{\mathrm{axf}}(\tilde Q)$ inside the image $\mathbb{B}_L$, the real dimension of the subspace, the trace of $M$, and the determinant of the $2\times2$ image. In the first row, $\lambda=Q_t$.

| Subspace | Defining condition | Condition on $M$ in the image | Real dim. | Trace | $\det\mathsf M_2(\tilde Q)$ |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\tilde Q^{\natural}=\tilde Q$ | $M=\lambda\mathrm I_4$ | $2$ | $4Q_t$ | $Q_t^2$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\tilde Q^{\natural}=-\tilde Q$ | $\operatorname{Tr}M=0$ | $6$ | $0$ | $B^2$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde Q}=\tilde Q$ | $M=\overline M$ | $4$ | $4q_t$ | $\sum q_\mu^2$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde Q}=-\tilde Q$ | $M=-\overline M$ | $4$ | $4iq'_t$ | $-\sum(q'_\mu)^2$ |
| $\mathbb{M}_+$ | $\tilde Q^{*}=\tilde Q$ | $M=M^{\dagger}$ | $4$ | $4q_t$ | $q_t^2-\lvert\vec q'\rvert^2$ |
| $\mathbb{M}_-$ | $\tilde Q^{\flat}=\tilde Q$ | $M=-M^{\dagger}$ | $4$ | $4iq'_t$ | $-(q'_t)^2+\lvert\vec q\rvert^2$ |

**The determinant of $M$.** On every row the determinant of the $4\times4$ matrix is the square of the last column, $\det M=(\det\mathsf M_2(\tilde Q))^2$. The last column is the quadratic determinant of the $2\times2$ image; the determinant of the $4\times4$ matrix is the quartic obtained by squaring it.

**The warning.** Apart from the centre, the conditions in the third column are not sufficient in the ambient $M_4(\mathbb{C})$. The real matrices form a real space of dimension $16$, the purely imaginary matrices another, the Hermitian matrices another and the anti-Hermitian matrices another; the traceless matrices form a complex space of dimension $15$, of real dimension $30$. The image selects a four-dimensional real subspace in each of the real, purely imaginary, Hermitian and anti-Hermitian cases, and a three-dimensional complex subspace in the traceless case. The conditions are exact only inside the image.

### The Centre Subspace

**The scalar matrices.** For $\tilde Q=Q_te_t$,
$$
L^{\mathrm{axf}}(Q_te_t)=Q_t\mathrm I_4,\qquad
\operatorname{Tr}M=4Q_t,\qquad
\det M=Q_t^4,\qquad
\det\mathsf M_2(\tilde Q)=Q_t^2.
$$
The image is the complex line $\mathbb{C}\mathrm I_4$, of real dimension $2$. It meets $\mathbb{M}_+$ in the real line $\mathbb{R}\mathrm I_4$ and $\mathbb{M}_-$ in the imaginary line $i\mathbb{R}\mathrm I_4$. It is the only subspace of real dimension $2$ and the only commutative one.

### The Vector Subspace

**The traceless matrices.** For $\tilde Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$,
$$
L^{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
0&-Q_x&-Q_y&-Q_z\\
Q_x&0&-Q_z&Q_y\\
Q_y&Q_z&0&-Q_x\\
Q_z&-Q_y&Q_x&0
\end{pmatrix}.
$$
The matrix is traceless and skew-symmetric, $M^{\mathsf T}=-M$. The image is the complex span of $L_{\vec e_x}^{\mathrm{axf}},L_{\vec e_y}^{\mathrm{axf}},L_{\vec e_z}^{\mathrm{axf}}$, of real dimension $6$. The trace is $0$, the determinant of the $2\times2$ image is $B^2$, and the determinant of $M$ is $B^4$. Inside the image, the trace condition is equivalent to skew-symmetry, because the transpose is quaternion conjugation and $\tilde Q^{\natural}=-\tilde Q$ exactly when $Q_t=0$. The image is closed under the commutator and not under the product.

### The Quaternion Subspace

**The real matrices.** For $\tilde Q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ with real coefficients,
$$
L^{\mathrm{axf}}(\tilde Q)=\overline{L^{\mathrm{axf}}(\tilde Q)},\qquad
\operatorname{Tr}M=4q_t,\qquad
\det\mathsf M_2(\tilde Q)=\sum_{\mu}q_\mu^2=q_t^2+q_x^2+q_y^2+q_z^2 .
$$
The image is the space of real matrices of this form, of real dimension $4$. The quadratic determinant is positive definite, and it vanishes only at $\tilde Q=0$. The image is closed under multiplication and is a division algebra.

### The Anti-Quaternion Subspace

**The purely imaginary matrices.** For $\tilde Q=iq'_te_t+iq'_x\vec e_x+iq'_y\vec e_y+iq'_z\vec e_z$,
$$
L^{\mathrm{axf}}(\tilde Q)=-\overline{L^{\mathrm{axf}}(\tilde Q)},\qquad
\operatorname{Tr}M=4iq'_t,\qquad
\det\mathsf M_2(\tilde Q)=-\sum_{\mu}(q'_\mu)^2 .
$$
The image is the space of purely imaginary matrices of this form, of real dimension $4$. The quadratic determinant is non-positive, and it vanishes only at $\tilde Q=0$. The image is not closed under multiplication: the product of two purely imaginary matrices is real.

### The Hermitian Subspace

**The Hermitian matrices.** For $\tilde Q=q_te_t+iq'_x\vec e_x+iq'_y\vec e_y+iq'_z\vec e_z$,
$$
L^{\mathrm{axf}}(\tilde Q)=L^{\mathrm{axf}}(\tilde Q)^{\dagger},\qquad
\operatorname{Tr}M=4q_t,\qquad
\det\mathsf M_2(\tilde Q)=q_t^2-\lvert\vec q'\rvert^2 .
$$
The image is the space of Hermitian matrices of this form, of real dimension $4$. The condition is exact inside the image because $L^{\mathrm{axf}}(\tilde Q)^{\dagger}=L^{\mathrm{axf}}(\tilde Q^{*})$ and $L^{\mathrm{axf}}$ is injective. The quadratic determinant is indefinite: it is positive when $q_t^2>\lvert\vec q'\rvert^2$ and negative when $q_t^2<\lvert\vec q'\rvert^2$. The image is not a subalgebra.

### The Anti-Hermitian Subspace

**The anti-Hermitian matrices.** For $\tilde Q=iq'_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$,
$$
L^{\mathrm{axf}}(\tilde Q)=-L^{\mathrm{axf}}(\tilde Q)^{\dagger},\qquad
\operatorname{Tr}M=4iq'_t,\qquad
\det\mathsf M_2(\tilde Q)=-(q'_t)^2+\lvert\vec q\rvert^2 .
$$
The image is the space of anti-Hermitian matrices of this form, of real dimension $4$. The condition is $\tilde Q^{\flat}=\tilde Q$, that is $\tilde Q^{*}=-\tilde Q$. The quadratic determinant is indefinite, with the sign opposite to the Hermitian determinant. The image is a Lie algebra under the commutator, not a subalgebra under the product.

### The Three Splits

**The three decompositions.** The six subspaces pair into the three decompositions
$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})
=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}
=\mathbb{M}_+\oplus\mathbb{M}_-,
$$
of real dimensions $2+6$, $4+4$ and $4+4$. The first is the scalar–vector split. The second is the real–imaginary split. The third is the Hermitian–anti-Hermitian split. No one of the three refines another.

**The intersections.** The centre meets $\mathbb{M}_+$ in $\mathbb{R}\mathrm I_4$ and $\mathbb{M}_-$ in $i\mathbb{R}\mathrm I_4$. The vector subspace meets $\mathbb{H}_{\mathbb{B}}$ in the real pure quaternions, of real dimension $3$, and $i\mathbb{H}_{\mathbb{B}}$ in the imaginary pure quaternions, of real dimension $3$. It meets $\mathbb{M}_+$ in $i$ times the real vector triple, and $\mathbb{M}_-$ in the real vector triple. The quaternion and anti-quaternion subspaces meet only at $0$, and so do the Hermitian and anti-Hermitian subspaces.

**The closure.** The centre and the quaternion subspace are subalgebras. The vector subspace is a Lie subalgebra under the commutator, not a subalgebra under the product. The anti-quaternion subspace and the two Hermitian subspaces are neither. Multiplication by $i$ exchanges $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and it exchanges $\mathbb{M}_+$ and $\mathbb{M}_-$.

## Summary

The left family is built first, from the multiplication alone: the $\nu$-th column of $L^{\mathrm{axf}}(\tilde Q)$ is the coordinate column of $\tilde Qe_\nu$, associativity makes the assignment multiplicative, and the first column recovers the element, so the image is a four-dimensional subalgebra $\mathbb{B}_L$ with unit $\mathrm I_4$. The four matrices of the units are signed permutations, with entries $0$ and $\pm1$, of determinant $1$ and trace $4\delta_{\mu t}$, and together with their negatives they are a copy of $Q_8$ inside $O(4)$. The transpose is the conjugation, $L^{\mathrm{axf}}(\tilde Q)^{\mathsf T}=L^{\mathrm{axf}}(\tilde Q^{\natural})$, and the dagger is the star.

The right family is built second, by the same rule with the factors exchanged: the $\nu$-th column of $R^{\mathrm{axf}}(\tilde Q)$ is the coordinate column of $\vec e_\nu\tilde Q$. The assignment is anti-multiplicative, the right matrices commute with the left ones, and the two families meet in the scalar matrices only. The switch between the two is the real sign matrix $D=\operatorname{diag}(1,-1,-1,-1)$, which is the Gram matrix of the form $\beta(\tilde X,\tilde Y)=\operatorname{Sc}(\tilde X\tilde Y)$ on the four units, and the identity is $R^{\mathrm{axf}}(\tilde Q)=DL^{\mathrm{axf}}(\tilde Q)^{\mathsf T}D$, that is $R_{\mu\nu}=s_\mu s_\nu L_{\nu\mu}$, and the sixteen products $L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}}$ are an orthogonal basis of $M_4(\mathbb{C})$ of norm two.

Every other frame is a conjugate of this one, $L'=\mathsf C^{-1}L\mathsf C$, $R'=\mathsf C^{-1}R\mathsf C$, with the switch carried by the congruence $\mathsf W'=\mathsf C^{\mathsf T}D\mathsf C$. The families are one orbit. What varies is the display — the entries, the sparsity, the subring, the two subspaces and the switch — and what does not vary is the element: trace $4Q_t$, determinant $\langle\tilde Q\rangle_{\natural}^2$, characteristic polynomial $((X-Q_t)^2+B^2)^2$, spectrum $Q_t\pm iB$ twice, rank $0$, $2$ or $4$.

This frame is the only one in which the sixteen matrices are at once real, integer-valued, signed permutations, orthogonal, and read off the multiplication table. Its entries lie in $\mathbb{Z}$, the smallest subring of $\mathbb{C}$ that can carry the table; a frame built for the tensor display trades the integers for $\mathbb{Z}[i]$ and keeps a tensor-product display; a generic frame has none of them. The signed-permutation frames are exactly the signed permutations of the axis-free basis, so this frame is unique up to relabelling the three directions and changing their signs, and the count is $3!\cdot2^4=96$ with the scalar unit first, or $48$ with the scalar unit fixed at $+e_t$. Realness alone gives nothing, since every real change of basis gives another real frame; realness with sparsity characterises it. The operator is unique and its matrix is a conjugacy class; this frame is the canonical representative of the class, the one in which the structure constants are the entries.

The six subspaces are the scalar, traceless, real, purely imaginary, Hermitian and anti-Hermitian matrices of the image, of real dimensions $2,6,4,4,4,4$, with the traces and determinants of the table, and the four norms are the four quarter-traces of the words in the matrix.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ | the coefficient basis, called axis-free in this article |
| $\mathrm{axf}$ | the label of the frame, on the family: $L^{\mathrm{axf}}$, $R^{\mathrm{axf}}$ |
| $L_{e_\mu}^{\mathrm{axf}}$, $R_{e_\mu}^{\mathrm{axf}}$ | the left and right matrices of the four units |
| $L^{\mathrm{axf}}(\tilde Q)$, $R^{\mathrm{axf}}(\tilde Q)$ | the left and right matrices of $\tilde Q$ |
| $\mathbb{B}_L$, $\mathbb{B}_R$ | the two families, as subalgebras of $M_4(\mathbb{C})$ |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | the switch of this frame, the Gram matrix of $\beta$, and the matrix of the conjugation |
| $s_\mu$ | the sign of $e_\mu^{\natural}=s_\mu e_\mu$, the diagonal entry of $D$ |
| $\beta(\tilde X,\tilde Y)$ | $\operatorname{Sc}(\tilde X\tilde Y)$, the symmetric form whose Gram matrix is the switch |
| $\mathsf C$ | the matrix of a change of frame, its columns the new frame vectors |
| $\mathsf W$, $\mathsf W'$ | the switch of a general frame, related by $\mathsf W'=\mathsf C^{\mathsf T}D\mathsf C$ |
| $\mathsf M_2(\tilde Q)$ | the $2\times2$ matrix of $\tilde Q$ |
| $\langle\tilde Q\rangle_{\natural}$ | $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ |
| $B^2$ | $Q_x^2+Q_y^2+Q_z^2$ |
| $q_\mu$, $q'_\mu$ | the real and imaginary parts of $Q_\mu$ |
| $L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}}$ | the sixteen products, an orthogonal basis of $M_4(\mathbb{C})$ of norm two |

## Further Reading

- [Families of Matrix Representations](families-of-matrix-representations.html), for the general theory of the two families, of the change of frame and of the switch.
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the conventions used across the category.
- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the six subspaces and the three decompositions.
- [The Element, the Coordinates and the Conjugations in the Biquaternion Algebra](the-element-the-coordinates-and-the-conjugations.html), for the four conjugations and the coordinate systems.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra and the multiplication table.
- [$M_4(\mathbb{C})$ Pauli Representation](m4c-pauli-representation.html), for the same content in another frame, with the tensor-product display and the pure swap.
- [$M_2(\mathbb{C})$ Pauli Representation](m2c-pauli-representation.html), for the element size and the compression.
