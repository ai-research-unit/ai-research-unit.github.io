# __$M_4(\mathbb{C})$ e-basis Representation : The Matrix Product, the Trace and the Determinant__

## Introduction

**The subject.** The left and right regular matrices of a biquaternion, written in the e-basis, with their product, their trace, their determinant and their values on the six remarkable subspaces.

**The e-basis.** The e-basis is the basis $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ of the biquaternion algebra. An element is
$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad Q_\mu\in\mathbb{C},
$$
and the entries of its regular matrices are these coefficients with the signs of the multiplication table. The other articles call $\mathcal{E}$ the coefficient basis. This article calls it the e-basis, and writes $L_\mu^{e}$ and $R_\mu^{e}$ for the matrices of the four units. The superscript $e$ is a frame label, not an exponent: $L_x^{e}$ is the left matrix of $\vec e_x$ in the e-basis, and its square is written $(L_x^{e})^2$.

**The result in one line.** The four left matrices $L_\mu^{e}$ are signed permutations and form a basis of the left copy $\mathbb{B}_L$; the four right matrices $R_\mu^{e}$ are signed permutations and form a basis of the right copy $\mathbb{B}_R$. The left matrix of a general element is displayed below. The product is multiplicative on the left and anti-multiplicative on the right. The trace is $4Q_t$. The determinant is $\langle\tilde Q\rangle_{\natural}^2=(Q_t^2+B^2)^2$. The eigenvalues are $Q_t\pm iB$, each twice.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$; the central scalar imaginary is $i$. Write $Q_\mu=q_\mu+iq'_\mu$ with $q_\mu,q'_\mu\in\mathbb{R}$, and put
$$
B^2=Q_x^2+Q_y^2+Q_z^2,\qquad
\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2=Q_t^2+Q_x^2+Q_y^2+Q_z^2 .
$$
The four conjugations are
$$
\tilde Q^{\natural}=Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z,\qquad
\overline{\tilde Q}=\bar Q_te_t+\bar Q_x\vec e_x+\bar Q_y\vec e_y+\bar Q_z\vec e_z,
$$
$$
\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\bar Q_te_t-\bar Q_x\vec e_x-\bar Q_y\vec e_y-\bar Q_z\vec e_z,\qquad
\tilde Q^{\flat}=-\tilde Q^{*}.
$$
The left copy is $\mathbb{B}_L=\rho_L(\mathbb{B})$, the right copy is $\mathbb{B}_R=\rho_R(\mathbb{B})$, and both are four-dimensional subalgebras of the ambient $M_4(\mathbb{C})=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. The left multiplication is $\rho_L(\tilde Q)(\tilde X)=\tilde Q\tilde X$; the right multiplication is $\rho_R(\tilde Q)(\tilde X)=\tilde X\tilde Q$.

**Boundaries.** The algebra, the multiplication table and the four conjugations are *The Biquaternion Algebra* and *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra*. The six subspaces are defined and decomposed in *Subspaces and Decompositions of the Biquaternion Algebra*; this article reads their images in the e-basis. The $2\times2$ isomorphism and the canonical Peirce frame are *Matrix Representations Conventions*; the product, trace and determinant in the canonical frame are *Matrix Representations : The Product, the Trace and the Determinant*.

## The e-Basis

**Definition.** The e-basis is the ordered basis
$$
\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z).
$$
It is the basis of the structure constants: the product of two basis elements is $\pm$ a basis element, and the sign is the sign of the quaternion multiplication. The coordinates of $\tilde Q$ in this basis are the four complex numbers $Q_t,Q_x,Q_y,Q_z$.

**Why the name.** The letter $e$ is the letter of the four basis vectors. The name records the basis, not an axis. The three vector units $\vec e_x,\vec e_y,\vec e_z$ each square to $-e_t$ and together generate the vector subspace, and the basis lists them without choosing one of them as the scalar direction. The canonical Peirce frame of the matrix model is built from the standard pair $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ and the mixed units $\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y)$, so it uses $\vec e_z$ and then $\vec e_x,\vec e_y$; the e-basis is prior to that choice. The two frames describe the same representation, and the change between them is written in §*The Switch of Basis*.

**The two copies.** The e-basis is a basis of the algebra $\mathbb{B}$. Left multiplication by $\tilde Q$ is an operator on $\mathbb{B}$, and its matrix in the e-basis is the left matrix $L^{e}(\tilde Q)$. Right multiplication is another operator on the same space, and its matrix is the right matrix $R^{e}(\tilde Q)$. The images of the four basis elements under $\rho_L$ are the four matrices $L_\mu^{e}$; the images under $\rho_R$ are the four matrices $R_\mu^{e}$. Each family is a basis of its copy because $\rho_L$ and $\rho_R$ are injective and the four $e_\mu$ are a basis.

### No Direction Is Privileged

**The three vector units enter by one rule.** In the left matrix, the $\mu$-th column is the coordinate column of $\tilde Qe_\mu$. The scalar column is the column of $\tilde Q$ itself, and each of the three vector columns is obtained from the same multiplication table by the same substitution. The display of a general element has $Q_t$ on the diagonal and the three vector coefficients in the off-diagonal positions, with no coefficient singled out by its position:
$$
L^{e}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&-Q_z&Q_y\\
Q_y&Q_z&Q_t&-Q_x\\
Q_z&-Q_y&Q_x&Q_t
\end{pmatrix}.
$$
The entries in the $x$, $y$ and $z$ positions have the same shape: one coefficient with a sign, and no sum. The right matrix has the same property.

**The symmetry is the cyclic one.** A cyclic permutation of the three directions, $x\mapsto y\mapsto z\mapsto x$, preserves the quaternion relations and is an algebra automorphism; it conjugates $L^{e}(\tilde Q)$ by the corresponding permutation matrix. A transposition reverses the orientation: it sends $\vec e_x\vec e_y=\vec e_z$ to $\vec e_y\vec e_x=-\vec e_z$, so it changes the signs of the structure constants. That sign is a property of the quaternion algebra, not a preference of the e-basis. The e-basis treats the three directions equally as a basis; the algebra itself has the cyclic orientation of the quaternion product.

**The contrast with the Peirce frame.** The Peirce frame uses $\vec e_z$ in the two idempotents and $\vec e_x,\vec e_y$ in the two mixed units. It is a convenient frame, and it makes the two Peirce planes literal diagonal blocks, but it distinguishes $z$. The e-basis is the frame in which no direction is distinguished by the construction. This is why the six subspaces are read entrywise in the e-basis: the real, imaginary, Hermitian and anti-Hermitian conditions do not depend on a choice of axis.

## The Left and Right Matrices

**The left matrix.** The left matrix $L^{e}(\tilde Q)$ is the $4\times4$ matrix whose $\mu$-th column is the coordinate column of $\tilde Qe_\mu$ in the e-basis. For $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$,
$$
L^{e}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&-Q_z&Q_y\\
Q_y&Q_z&Q_t&-Q_x\\
Q_z&-Q_y&Q_x&Q_t
\end{pmatrix}.
$$
The first column is $(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$, so it recovers $\tilde Q$. The assignment is injective and multiplicative:
$$
L^{e}(\tilde Q_1\tilde Q_2)=L^{e}(\tilde Q_1)L^{e}(\tilde Q_2),\qquad
L^{e}(\tilde Q)=0\iff\tilde Q=0.
$$
The image is the four-dimensional complex subalgebra $\mathbb{B}_L$ of $M_4(\mathbb{C})$, and its unit is $\mathrm I_4$.

**The right matrix.** The right matrix $R^{e}(\tilde Q)$ has $\mu$-th column the coordinate column of $e_\mu\tilde Q$. In the same basis,
$$
R^{e}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&Q_z&-Q_y\\
Q_y&-Q_z&Q_t&Q_x\\
Q_z&Q_y&-Q_x&Q_t
\end{pmatrix}.
$$
The right matrix is anti-multiplicative, and it commutes with the left matrix:
$$
R^{e}(\tilde Q_1\tilde Q_2)=R^{e}(\tilde Q_2)R^{e}(\tilde Q_1),\qquad
L^{e}(\tilde Q_1)R^{e}(\tilde Q_2)=R^{e}(\tilde Q_2)L^{e}(\tilde Q_1).
$$
The two identities are the two ways of reading the associative law $(\tilde X\tilde Q_1)\tilde Q_2=\tilde X(\tilde Q_1\tilde Q_2)$ and $\tilde Q_1(\tilde X\tilde Q_2)=(\tilde Q_1\tilde X)\tilde Q_2$.

**An example.** For $\tilde Q=(2+i)e_t+(1-i)\vec e_x+3\vec e_y+i\vec e_z$,
$$
L^{e}(\tilde Q)=
\begin{pmatrix}
2+i&-1+i&-3&-i\\
1-i&2+i&-i&3\\
3&i&2+i&-1+i\\
i&-3&1-i&2+i
\end{pmatrix}.
$$
The trace is $8+4i=4(2+i)$, and the determinant is $117+44i=(11+2i)^2$, with $\langle\tilde Q\rangle_{\natural}=11+2i$. The first column is the coordinate column of $\tilde Q$, and the second column is the coordinate column of $\tilde Q\vec e_x$.

**The transpose and the dagger.** In the e-basis,
$$
L^{e}(\tilde Q)^{\mathsf T}=L^{e}(\tilde Q^{\natural}),\qquad
L^{e}(\tilde Q)^{\dagger}=L^{e}(\tilde Q^{*}),
$$
and the same identities hold for $R^{e}$. The first is the reason the e-basis is kept for the transpose dictionary: quaternion conjugation is transposition. The second is the Hermitian adjoint: $\dagger$ is the conjugate transpose. Both identities are checked on the four units and extended by linearity.

## The L and R Bases

**The left basis.** The four matrices $L_\mu^{e}=L^{e}(e_\mu)$ are
$$
L_t^{e}=\mathrm I_4,\qquad
L_x^{e}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
$$
$$
L_y^{e}=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
L_z^{e}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$
Each is a signed permutation matrix. Each has determinant $1$; the identity has trace $4$, and the three vector matrices have trace $0$. Since $\rho_L$ is injective and the four units are a basis of $\mathbb{B}$, the four matrices are linearly independent and span $\mathbb{B}_L$: they are a basis of the left copy.

**The right basis.** The four matrices $R_\mu^{e}=R^{e}(e_\mu)$ are
$$
R_t^{e}=\mathrm I_4,\qquad
R_x^{e}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},
$$
$$
R_y^{e}=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
R_z^{e}=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$
Each is a signed permutation matrix, of determinant $1$ and trace $4\delta_{\mu t}$; the four are a basis of $\mathbb{B}_R$. The two bases are bases of two different four-dimensional subspaces of $M_4(\mathbb{C})$, not two bases of one space.

**The product of two basis matrices.** Write the two orders of the quaternion product as $e_\mu e_\nu=\varepsilon e_{\mu\nu}$ and $e_\nu e_\mu=\varepsilon' e_{\nu\mu}$, with $\varepsilon,\varepsilon'=\pm1$ and $e_{\mu\nu},e_{\nu\mu}$ units. Then
$$
L_\mu^{e}L_\nu^{e}=\varepsilon L_{\mu\nu}^{e},\qquad
R_\mu^{e}R_\nu^{e}=\varepsilon' R_{\nu\mu}^{e}.
$$
The left product follows the order of the units; the right product reverses it, because $R_aR_b=R_{ba}$. For example,
$$
(L_x^{e})^2=(R_x^{e})^2=-\mathrm I_4,\qquad
L_x^{e}L_y^{e}=L_z^{e},\qquad
L_y^{e}L_x^{e}=-L_z^{e},
$$
and on the right $R_x^{e}R_y^{e}=-R_z^{e}$, $R_y^{e}R_x^{e}=R_z^{e}$. The basis is closed under products up to sign, and the signs are the signs of the multiplication table. The products $L_\mu^{e}L_\nu^{e}$ and $R_\mu^{e}R_\nu^{e}$ need not be distinct; the set of the four left matrices together with their negatives is the quaternion group of order eight, and the same holds for the right matrices.

**Trace and determinant of a basis matrix.** Every basis matrix is invertible, with
$$
\det L_\mu^{e}=\det R_\mu^{e}=1,\qquad
\operatorname{Tr}L_\mu^{e}=\operatorname{Tr}R_\mu^{e}=4\delta_{\mu t}.
$$
A sum of basis matrices need not be invertible: $L_x^{e}+R_x^{e}$ has rank $2$, for instance. The algebra is simple and has zero divisors, and the invertibility of each basis vector does not extend to the complex span.

## The Switch of Basis

**The exchange of the left and right bases.** Let
$$
D=\operatorname{diag}(1,-1,-1,-1).
$$
The matrix $D$ is the matrix of quaternion conjugation in the e-basis: the coordinate column of $\tilde Q^{\natural}$ is $D$ times the coordinate column of $\tilde Q$. It satisfies $D^2=\mathrm I_4$ and $\det D=-1$. The two families are exchanged by
$$
R^{e}(\tilde Q)=D\,L^{e}(\tilde Q)^{\mathsf T}D
=D\,L^{e}(\tilde Q^{\natural})\,D .
$$
The relation follows from the two definitions; the second form uses the transpose identity. The same formula holds on the four basis matrices, $R_\mu^{e}=D(L_\mu^{e})^{\mathsf T}D$, so the exchange is a switch between the two bases. It is an involution: applying it twice returns $L^{e}(\tilde Q)$.

**The change to the Peirce frame.** The Peirce frame of the matrix model is the basis
$$
(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-),\qquad
\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z),\quad
\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y),
$$
in that order. The change matrix is
$$
S=\frac12
\begin{pmatrix}
1&0&0&1\\
0&i&i&0\\
0&1&-1&0\\
i&0&0&-i
\end{pmatrix},
\qquad
\det S=-\tfrac14,
$$
whose columns are the four frame vectors in the e-basis. In the Peirce frame the two regular matrices are the two tensor displays
$$
S^{-1}L^{e}(\tilde Q)S=\mathrm I_2\otimes\mathsf M_2(\tilde Q),\qquad
S^{-1}R^{e}(\tilde Q)S=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes\mathrm I_2,
$$
where $\mathsf M_2$ is the $2\times2$ isomorphism of *Matrix Representations Conventions*. Equivalently,
$$
L^{e}(\tilde Q)=S\bigl(\mathrm I_2\otimes\mathsf M_2(\tilde Q)\bigr)S^{-1},\qquad
R^{e}(\tilde Q)=S\bigl(\mathsf M_2(\tilde Q)^{\mathsf T}\otimes\mathrm I_2\bigr)S^{-1}.
$$
The change is a change of frame, not a change of operator: the trace and the determinant below are the same in the two displays.

**The inverse change.** The change $S$ sends Peirce coordinates to e-coordinates, and $S^{-1}$ sends e-coordinates to Peirce coordinates; the columns of $S^{-1}$ are the Peirce coordinates of the four e-basis vectors. The determinant of $S$ is $-\tfrac14$, a fixed normalisation of the frame vectors, not a property of the algebra.

**The choice inside the change.** The matrix $S$ uses $\vec e_z$ and $\vec e_x,\vec e_y$; it is one of the three Peirce frames obtained by choosing one of the three directions for the idempotents. The e-basis does not make that choice. The three changes are related by the cyclic permutation of the directions, and no one of them is the e-basis.

## The Product

**The left product.** For all $\tilde Q_1,\tilde Q_2$,
$$
L^{e}(\tilde Q_1\tilde Q_2)=L^{e}(\tilde Q_1)L^{e}(\tilde Q_2),\qquad
L^{e}(\tilde Q^n)=L^{e}(\tilde Q)^n,\qquad
L^{e}(\tilde Q^{-1})=L^{e}(\tilde Q)^{-1},
$$
the last when $\tilde Q$ is invertible. The identity is the multiplicativity of $\rho_L$.

**The right product.** For all $\tilde Q_1,\tilde Q_2$,
$$
R^{e}(\tilde Q_1\tilde Q_2)=R^{e}(\tilde Q_2)R^{e}(\tilde Q_1),\qquad
R^{e}(\tilde Q^n)=R^{e}(\tilde Q)^n,\qquad
R^{e}(\tilde Q^{-1})=R^{e}(\tilde Q)^{-1}.
$$
The order is reversed because the right multiplication acts on the right factor; the powers and the inverse are not reversed, since they involve one element only.

**The two families commute.** For all $\tilde Q_1,\tilde Q_2$,
$$
L^{e}(\tilde Q_1)R^{e}(\tilde Q_2)=R^{e}(\tilde Q_2)L^{e}(\tilde Q_1).
$$
The identity is the associativity of the product, read on the two sides. It says that the left copy and the right copy are mutual commutants inside the ambient matrix algebra.

**The product of a left and a right basis matrix.** The products $L_\mu^{e}R_\nu^{e}$ are again signed permutations, and the product of two such matrices is a signed permutation. A left matrix and a right matrix commute, and this commutation is the defining property of the two copies.

## The Trace

**The trace is the scalar part.** For every $\tilde Q$,
$$
\operatorname{Tr}L^{e}(\tilde Q)=\operatorname{Tr}R^{e}(\tilde Q)=4Q_t.
$$
The trace is the sum of the four diagonal entries, each equal to $Q_t$. The factor $4$ is $2\cdot2$: the $2\times2$ image has trace $2Q_t$, and in the Peirce frame the regular matrix is two copies of it. The trace sees the scalar part and no vector coefficient.

**The trace of a basis matrix.** On the basis,
$$
\operatorname{Tr}L_t^{e}=\operatorname{Tr}R_t^{e}=4,\qquad
\operatorname{Tr}L_x^{e}=\operatorname{Tr}L_y^{e}=\operatorname{Tr}L_z^{e}=0,
\qquad
\operatorname{Tr}R_x^{e}=\operatorname{Tr}R_y^{e}=\operatorname{Tr}R_z^{e}=0.
$$
The trace is $\mathbb{C}$-linear and additive. It is not multiplicative; the trace of a product is not the product of the traces.

**The trace of a product.** For all $\tilde Q_1,\tilde Q_2$,
$$
\operatorname{Tr}\bigl(L^{e}(\tilde Q_1)L^{e}(\tilde Q_2)\bigr)
=4\operatorname{Sc}(\tilde Q_1\tilde Q_2),
$$
where $\operatorname{Sc}$ is the scalar part. The identity is the trace of the left matrix of the product, read through the preceding formula. The same identity holds for two right matrices. A left and a right matrix give
$$
\operatorname{Tr}\bigl(L^{e}(\tilde Q_1)R^{e}(\tilde Q_2)\bigr)=4Q_{1t}Q_{2t};
$$
the mixed trace sees the two scalar parts only.

## The Determinant

**The determinant is the square of the central scalar.** For every $\tilde Q$,
$$
\det L^{e}(\tilde Q)=\det R^{e}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^2
=(Q_t^2+B^2)^2.
$$
The determinant is the square of the $2\times2$ determinant, because in the Peirce frame the regular matrix is two copies of the $2\times2$ image. It is a quartic in the four coefficients, and it vanishes exactly on the null cone $\langle\tilde Q\rangle_{\natural}=0$.

**The characteristic polynomial.** The characteristic polynomial of $L^{e}(\tilde Q)$ is
$$
\chi_{L^{e}(\tilde Q)}(\lambda)
=\bigl(\lambda^2-2Q_t\lambda+\langle\tilde Q\rangle_{\natural}\bigr)^2
=\bigl((\lambda-Q_t)^2+B^2\bigr)^2 .
$$
The eigenvalues are $\lambda_\pm=Q_t\pm iB$, where $B$ is a square root of $B^2=Q_x^2+Q_y^2+Q_z^2$, each with algebraic multiplicity two. Their sum is $4Q_t$, their product is $\langle\tilde Q\rangle_{\natural}^2$, and the two facts are the trace and the determinant. The same polynomial is the characteristic polynomial of $R^{e}(\tilde Q)$, because the two matrices are conjugate by $D$ and transposition.

**The determinant is multiplicative.** For all $\tilde Q_1,\tilde Q_2$,
$$
\det L^{e}(\tilde Q_1\tilde Q_2)=\det L^{e}(\tilde Q_1)\det L^{e}(\tilde Q_2),
$$
and the same identity holds for $R^{e}$. The determinant is the multiplicative invariant of the algebra; the trace is the additive one.

**The basis determinants.** Every basis matrix has determinant $1$:
$$
\det L_\mu^{e}=\det R_\mu^{e}=1\qquad(\mu=t,x,y,z).
$$
The determinant of a sum is not the sum of the determinants; a sum of two invertible matrices can be singular, as $L_x^{e}+R_x^{e}$ shows.

**The invertibility and the rank.** The following are equivalent: $\tilde Q$ is invertible; $\langle\tilde Q\rangle_{\natural}\neq0$; $\mathsf M_2(\tilde Q)$ is invertible; $L^{e}(\tilde Q)$ is invertible; $R^{e}(\tilde Q)$ is invertible. When $\langle\tilde Q\rangle_{\natural}=0$, the rank of the regular matrix is $0$, $2$ or $4$, never $1$ or $3$, because the matrix is two equal copies of the $2\times2$ image. The rank is twice the rank of $\mathsf M_2(\tilde Q)$.

## The Six Subspaces

**The table.** The six remarkable subspaces are defined in *Subspaces and Decompositions of the Biquaternion Algebra*. On the image of the e-basis representation they become the conditions of the table. Write $\vec q=(q_x,q_y,q_z)$ and $\vec q'=(q'_x,q'_y,q'_z)$, and recall $Q_\mu=q_\mu+iq'_\mu$, $B^2=Q_x^2+Q_y^2+Q_z^2$. In the third column, $\overline M$ is the entrywise complex conjugate of $M$ and $M^{\dagger}=\overline M^{\mathsf T}$. The table gives the condition on $M=L^{e}(\tilde Q)$ inside the image $\mathbb{B}_L$, the real dimension of the subspace, the trace of $M$, and the determinant of the $2\times2$ image. In the first row, $\lambda=Q_t$.

| Subspace | Defining condition | Condition on $M$ in the image | Real dim. | Trace | $\det\mathsf M_2(\tilde Q)$ |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\tilde Q^{\natural}=\tilde Q$ | $M=\lambda\mathrm I_4$ | $2$ | $4Q_t$ | $Q_t^2$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\tilde Q^{\natural}=-\tilde Q$ | $\operatorname{Tr}M=0$ | $6$ | $0$ | $B^2$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde Q}=\tilde Q$ | $M=\overline M$ | $4$ | $4q_t$ | $\sum q_\mu^2$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde Q}=-\tilde Q$ | $M=-\overline M$ | $4$ | $4iq'_t$ | $-\sum(q'_\mu)^2$ |
| $\mathbb{M}_+$ | $\tilde Q^{*}=\tilde Q$ | $M=M^{\dagger}$ | $4$ | $4q_t$ | $q_t^2-\lvert\vec q'\rvert^2$ |
| $\mathbb{M}_-$ | $\tilde Q^{\flat}=\tilde Q$ | $M=-M^{\dagger}$ | $4$ | $4iq'_t$ | $-(q'_t)^2+\lvert\vec q\rvert^2$ |

**The determinant of $M$.** On every row the determinant of the $4\times4$ matrix is the square of the last column, $\det M=(\det\mathsf M_2(\tilde Q))^2$. The last column is the quadratic determinant of the $2\times2$ image; the determinant of the regular matrix is the quartic obtained by squaring it.

**The warning.** Apart from the centre, the conditions in the third column are not sufficient in the ambient $M_4(\mathbb{C})$. The real matrices form a real space of dimension $16$, the purely imaginary matrices another, the Hermitian matrices another and the anti-Hermitian matrices another; the traceless matrices form a complex space of dimension $15$, of real dimension $30$. The image selects a four-dimensional real subspace in each of the real, purely imaginary, Hermitian and anti-Hermitian cases, and a three-dimensional complex subspace in the traceless case. The conditions are exact only inside the image.

### The Centre Subspace

**The scalar matrices.** For $\tilde Q=Q_te_t$,
$$
L^{e}(Q_te_t)=Q_t\mathrm I_4,\qquad
\operatorname{Tr}M=4Q_t,\qquad
\det M=Q_t^4,\qquad
\det\mathsf M_2(\tilde Q)=Q_t^2.
$$
The image is the complex line $\mathbb{C}\mathrm I_4$, of real dimension $2$. It meets $\mathbb{M}_+$ in the real line $\mathbb{R}\mathrm I_4$ and $\mathbb{M}_-$ in the imaginary line $i\mathbb{R}\mathrm I_4$. It is the only subspace of real dimension $2$ and the only commutative one.

### The Vector Subspace

**The traceless matrices.** For $\tilde Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$,
$$
L^{e}(\tilde Q)=
\begin{pmatrix}
0&-Q_x&-Q_y&-Q_z\\
Q_x&0&-Q_z&Q_y\\
Q_y&Q_z&0&-Q_x\\
Q_z&-Q_y&Q_x&0
\end{pmatrix}.
$$
The matrix is traceless and skew-symmetric, $M^{\mathsf T}=-M$. The image is the complex span of $L_x^{e},L_y^{e},L_z^{e}$, of real dimension $6$. The trace is $0$, the determinant of the $2\times2$ image is $B^2$, and the determinant of $M$ is $B^4$. Inside the image, the trace condition is equivalent to skew-symmetry, because the transpose is quaternion conjugation and $\tilde Q^{\natural}=-\tilde Q$ exactly when $Q_t=0$. The image is closed under the commutator and not under the product.

### The Quaternion Subspace

**The real matrices.** For $\tilde Q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ with real coefficients,
$$
L^{e}(\tilde Q)=\overline{L^{e}(\tilde Q)},\qquad
\operatorname{Tr}M=4q_t,\qquad
\det\mathsf M_2(\tilde Q)=\sum_{\mu}q_\mu^2=q_t^2+q_x^2+q_y^2+q_z^2 .
$$
The image is the space of real matrices of the regular form, of real dimension $4$. The quadratic determinant is positive definite, and it vanishes only at $\tilde Q=0$. The image is closed under multiplication and is a division algebra.

### The Anti-Quaternion Subspace

**The purely imaginary matrices.** For $\tilde Q=iq'_te_t+iq'_x\vec e_x+iq'_y\vec e_y+iq'_z\vec e_z$,
$$
L^{e}(\tilde Q)=-\overline{L^{e}(\tilde Q)},\qquad
\operatorname{Tr}M=4iq'_t,\qquad
\det\mathsf M_2(\tilde Q)=-\sum_{\mu}(q'_\mu)^2 .
$$
The image is the space of purely imaginary matrices of the regular form, of real dimension $4$. The quadratic determinant is non-positive, and it vanishes only at $\tilde Q=0$. The image is not closed under multiplication: the product of two purely imaginary matrices is real.

### The Hermitian Subspace

**The Hermitian matrices.** For $\tilde Q=q_te_t+iq'_x\vec e_x+iq'_y\vec e_y+iq'_z\vec e_z$,
$$
L^{e}(\tilde Q)=L^{e}(\tilde Q)^{\dagger},\qquad
\operatorname{Tr}M=4q_t,\qquad
\det\mathsf M_2(\tilde Q)=q_t^2-\lvert\vec q'\rvert^2 .
$$
The image is the space of Hermitian matrices of the regular form, of real dimension $4$. The condition is exact inside the image because $L^{e}(\tilde Q)^{\dagger}=L^{e}(\tilde Q^{*})$ and $L^{e}$ is injective. The quadratic determinant is indefinite: it is positive when $q_t^2>\lvert\vec q'\rvert^2$ and negative when $q_t^2<\lvert\vec q'\rvert^2$. The image is not a subalgebra.

### The Anti-Hermitian Subspace

**The anti-Hermitian matrices.** For $\tilde Q=iq'_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$,
$$
L^{e}(\tilde Q)=-L^{e}(\tilde Q)^{\dagger},\qquad
\operatorname{Tr}M=4iq'_t,\qquad
\det\mathsf M_2(\tilde Q)=-(q'_t)^2+\lvert\vec q\rvert^2 .
$$
The image is the space of anti-Hermitian matrices of the regular form, of real dimension $4$. The condition is $\tilde Q^{\flat}=\tilde Q$, that is $\tilde Q^{*}=-\tilde Q$. The quadratic determinant is indefinite, with the sign opposite to the Hermitian determinant. The image is a Lie algebra under the commutator, not a subalgebra under the product.

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

The e-basis is the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$; the three vector units enter the left and right matrices by one rule, and no direction is privileged. The four left matrices $L_\mu^{e}$ and the four right matrices $R_\mu^{e}$ are signed permutations and form bases of the left and right copies. The left matrix of a general element is the coefficient display with the signs of the multiplication table; the right matrix is obtained from it by transposition and the sign matrix $D$. The product is multiplicative on the left, anti-multiplicative on the right, and the two families commute.

The trace is $4Q_t$, the determinant is $\langle\tilde Q\rangle_{\natural}^2$, and the eigenvalues are $Q_t\pm iB$, each twice. The change to the Peirce frame is the matrix $S$; the exchange of the left and right matrices is $R^{e}(\tilde Q)=D L^{e}(\tilde Q)^{\mathsf T}D$, with $D=\operatorname{diag}(1,-1,-1,-1)$. The six subspaces are the scalar, traceless, real, purely imaginary, Hermitian and anti-Hermitian matrices of the image, of real dimensions $2,6,4,4,4,4$, with the traces and determinants of the table.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ | the e-basis |
| $L_\mu^{e}$, $R_\mu^{e}$ | the left and right matrices of the four units |
| $L^{e}(\tilde Q)$, $R^{e}(\tilde Q)$ | the left and right matrices of $\tilde Q$ |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | the matrix of quaternion conjugation in the e-basis |
| $S$ | the change matrix to the Peirce frame, $\det S=-\tfrac14$ |
| $\mathsf M_2(\tilde Q)$ | the $2\times2$ image of $\tilde Q$ |
| $\langle\tilde Q\rangle_{\natural}$ | $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ |
| $B^2$ | $Q_x^2+Q_y^2+Q_z^2$ |
| $q_\mu$, $q'_\mu$ | the real and imaginary parts of $Q_\mu$ |

## Further Reading

- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the six subspaces and the three decompositions.
- [The Element, the Coordinates and the Conjugations in the Biquaternion Algebra](the-element-the-coordinates-and-the-conjugations.html), for the four conjugations and the coordinate systems.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra and the multiplication table.
- [Matrix Representations Conventions](conventions-of-the-matrix-models.html), for the $2\times2$ isomorphism, the canonical Peirce frame and the labels $\mathbb{B}_L$, $\mathbb{B}_R$.
- [Matrix Representations : The Product, the Trace and the Determinant](matrix-representations-the-product-the-trace-and-the-determinant.html), for the same invariants in the canonical frame.
- [Matrix Representations : The Six Subspaces as Matrix Conditions](matrix-representations-the-six-subspaces-as-matrix-conditions.html), for the six subspaces read in the canonical frame.
