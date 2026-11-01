# __$M_4(\mathbb{C})$ e-basis Representation__

## Introduction

**The subject.** The left and right regular matrices of a biquaternion, written in the e-basis, with their product, their trace, their determinant, their values on the six remarkable subspaces, the sixteen two-sided products, the coordinate matrix of an arbitrary endomorphism in that basis, and the reason the two invariants read from it do not depend on the frame.

**The e-basis.** The e-basis is the basis $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ of the biquaternion algebra. An element is
$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad Q_\mu\in\mathbb{C},
$$
and the entries of its regular matrices are these coefficients with the signs of the multiplication table. The other articles call $\mathcal{E}$ the coefficient basis. This article calls it the e-basis, and writes $L_\mu^{e}$ and $R_\mu^{e}$ for the matrices of the four units. The superscript $e$ is a label, not an exponent: $L_x^{e}$ is the left matrix of $\vec e_x$ in the e-basis, and its square is written $(L_x^{e})^2$.

**The algebra.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$; the central scalar imaginary is $i$. Write $Q_\mu=q_\mu+iq'_\mu$ with $q_\mu,q'_\mu\in\mathbb{R}$, and put $B^2=Q_x^2+Q_y^2+Q_z^2$ and $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2=Q_t^2+Q_x^2+Q_y^2+Q_z^2$.

**The result in one line.** The four left matrices $L_\mu^{e}$ are signed permutations and form a basis of the left copy $\mathbb{B}_L$; the four right matrices $R_\mu^{e}$ are signed permutations and form a basis of the right copy $\mathbb{B}_R$. The left matrix of a general element is displayed below. The product is multiplicative on the left and anti-multiplicative on the right. The trace is $4Q_t$. The determinant is $\langle\tilde Q\rangle_{\natural}^2=(Q_t^2+B^2)^2$. The eigenvalues are $Q_t\pm iB$, each twice.

**The two copies.** The left copy is $\mathbb{B}_L=\rho_L(\mathbb{B})$, the right copy is $\mathbb{B}_R=\rho_R(\mathbb{B})$, and both are four-dimensional subalgebras of the ambient $M_4(\mathbb{C})=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. The left multiplication is $\rho_L(\tilde Q)(\tilde X)=\tilde Q\tilde X$; the right multiplication is $\rho_R(\tilde Q)(\tilde X)=\tilde X\tilde Q$.

**The one idea that is not in the two lists above.** The sixteen products $T^{e}_{\mu\nu}=L^{e}_\mu R^{e}_\nu$ are a basis of the whole algebra $M_4(\mathbb{C})$, so an arbitrary endomorphism has a coordinate matrix $c(M)$ in that basis. The products are exactly the matrices of coefficient rank one, the least number of products summing to a matrix is $\operatorname{rank}c(M)$, and a change of the algebra basis carries $c$ to a congruence, so the rank and the length are properties of the operator rather than of the frame. §*The Coefficient Matrix and the Length* follows that chain, and its punchline is negative: the same array can display two operators of different length, and $E_{11}$ is the example.

**Boundaries.** The algebra, the multiplication table and the four conjugations are *The Biquaternion Algebra* and *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra*. The six subspaces are defined and decomposed in *Subspaces and Decompositions of the Biquaternion Algebra*; this article reads their images in the e-basis. The six subspaces as matrix conditions, in the same basis, are *$M_4(\mathbb{C})_{\mathbb{B}_L}$ Representation : The Six Subspaces as Matrix Conditions*. The same element in the standard Peirce frame is *$M_4(\mathbb{C})$ Standard Peirce Representation*.

## The e-Basis

**Definition.** The e-basis is the ordered basis
$$
\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z).
$$
It is the basis of the structure constants: the product of two basis elements is $\pm$ a basis element, and the sign is the sign of the quaternion multiplication. The coordinates of $\tilde Q$ in this basis are the four complex numbers $Q_t,Q_x,Q_y,Q_z$.

**Why the name.** The letter $e$ is the letter of the four basis vectors. The name records the basis, not an axis. The three vector units $\vec e_x,\vec e_y,\vec e_z$ each square to $-e_t$ and together generate the vector subspace, and the basis lists them without choosing one of them as a direction.

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

**No axis is chosen.** The three vector units enter the display by the same rule, so no one of them is singled out by the construction. The basis names no direction as preferred, and the multiplication table is the only structure used. This is why the six subspaces are read entrywise here: the real, imaginary, Hermitian and anti-Hermitian conditions do not depend on a choice of axis.

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

### The Image Is Not Everything

**The count.** The ambient algebra $M_4(\mathbb{C})$ has complex dimension sixteen; the left copy $\mathbb{B}_L$ has complex dimension four. The assignment $\rho_L$ is injective, so the image is a four-dimensional subalgebra, and twelve complex dimensions are transverse to it. The right copy has the same dimension, and the two copies meet in the scalars, so together they span seven dimensions of the sixteen.

**A matrix that is not an element.** No image has odd rank. The regular matrix is two copies of the $2\times2$ image, so
$$
\operatorname{rank}L^{e}(\tilde Q)=2\operatorname{rank}\mathsf M_2(\tilde Q)\in\{0,2,4\}.
$$
The matrix unit $E_{11}$ has rank one; it is not the left matrix of any element, and neither is any other matrix of rank one or three. A general $4\times4$ matrix is an endomorphism of the carrier, not an element of the algebra.

**What is lost.** Every quantitative statement of this article is a statement about the four-dimensional image: the trace $4Q_t$, the determinant $\langle\tilde Q\rangle_{\natural}^2$, the doubled eigenvalues and the six rows of matrix conditions hold there and fail on a general matrix. A reader who meets $M_4(\mathbb{C})$ in the operators articles meets all sixteen dimensions at once, and the twelve transverse ones belong to an endomorphism rather than to an element. The distance is measured below: a general matrix is a sum of at most four products $T_{\mu\nu}^{e}=L_\mu^{e}R_\nu^{e}$, and the number needed is its length (§*The Coefficient Matrix and the Length*).

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

## The Stitch Between the Left and the Right

**The switch matrix.** Quaternion conjugation acts on a coordinate column by the matrix
$$
D=
\begin{pmatrix}
1&0&0&0\\
0&-1&0&0\\
0&0&-1&0\\
0&0&0&-1
\end{pmatrix},
\qquad
D^2=\mathrm I_4,\quad \det D=-1 .
$$
Its entries are $s_t=1$ and $s_x=s_y=s_z=-1$, the signs of $e_\mu^{\natural}=s_\mu e_\mu$. The matrix $D$ is the switch between the left and the right: it acts on the left and on the right of the left matrix, and it produces the right matrix.

**The stitch.** The right matrix is obtained from the left by transposition and a sign on each side:
$$
R^{e}(\tilde Q)=D\,L^{e}(\tilde Q)^{\mathsf T}D
=D\,L^{e}(\tilde Q^{\natural})\,D .
$$
The second form uses the transpose identity $L^{e}(\tilde X)^{\mathsf T}=L^{e}(\tilde X^{\natural})$.

**The stitch in full.** The three steps are displayed on a general element. The transpose of the left matrix is
$$
L^{e}(\tilde Q)^{\mathsf T}=
\begin{pmatrix}
Q_t&Q_x&Q_y&Q_z\\
-Q_x&Q_t&Q_z&-Q_y\\
-Q_y&-Q_z&Q_t&Q_x\\
-Q_z&Q_y&-Q_x&Q_t
\end{pmatrix},
$$
the left multiplication by $D$ changes the sign of the last three rows,
$$
D\,L^{e}(\tilde Q)^{\mathsf T}=
\begin{pmatrix}
Q_t&Q_x&Q_y&Q_z\\
Q_x&-Q_t&-Q_z&Q_y\\
Q_y&Q_z&-Q_t&-Q_x\\
Q_z&-Q_y&Q_x&-Q_t
\end{pmatrix},
$$
and the right multiplication by $D$ changes the sign of the last three columns. Written with the switch matrix displayed on both sides,
$$
R^{e}(\tilde Q)=
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
The two multiplications by $D$ are the two sign changes: one on the rows, one on the columns. Reading the last display entry by entry,
$$
R^{e}(\tilde Q)_{\mu\nu}=s_\mu s_\nu\,L^{e}(\tilde Q)_{\nu\mu},
$$
so $R^{e}(\tilde Q)_{\mu\nu}$ is the transposed entry $L^{e}(\tilde Q)_{\nu\mu}$, kept when $\mu$ and $\nu$ are both scalar or both vector, and reversed when one is scalar and the other vector.

**Why the stitch works.** The $\mu\nu$ entry of $L^{e}(\tilde Q)$ is the coefficient of $e_\mu$ in $\tilde Qe_\nu$; the $\mu\nu$ entry of $R^{e}(\tilde Q)$ is the coefficient of $e_\mu$ in $e_\nu\tilde Q$. Conjugating $\tilde Q^{\natural}e_\nu$ gives $(\tilde Q^{\natural}e_\nu)^{\natural}=s_\nu\,e_\nu\tilde Q$, so the coefficient of $e_\mu$ in $e_\nu\tilde Q$ is $s_\mu s_\nu$ times the coefficient of $e_\mu$ in $\tilde Q^{\natural}e_\nu$. Hence
$$
R^{e}(\tilde Q)_{\mu\nu}=s_\mu s_\nu\,L^{e}(\tilde Q^{\natural})_{\mu\nu}
=D\,L^{e}(\tilde Q^{\natural})\,D .
$$

**The stitch on the bases.** On the four units, $R_\mu^{e}=D(L_\mu^{e})^{\mathsf T}D$. Applying the formula twice returns $L^{e}(\tilde Q)$, because $D^2=\mathrm I_4$ and transposition is an involution. The stitch preserves the trace and the determinant, since neither transposition nor conjugation by a fixed matrix changes them:
$$
\operatorname{Tr}R^{e}(\tilde Q)=\operatorname{Tr}L^{e}(\tilde Q),\qquad
\det R^{e}(\tilde Q)=\det L^{e}(\tilde Q).
$$

## The Switch Between the Two Representations

**The change matrix.** The columns of
$$
S=\frac12
\begin{pmatrix}
1&0&0&1\\
0&i&i&0\\
0&1&-1&0\\
i&0&0&-i
\end{pmatrix}
$$
are the four vectors of the standard Peirce frame in the e-basis, the frame built from the root $\vec\Xi=i\vec e_z$:
$$
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\quad
\vec\Upsilon_+=\tfrac12(i\vec e_x+\vec e_y),\quad
\vec\Upsilon_-=\tfrac12(i\vec e_x-\vec e_y),\quad
\tilde\Pi_-=\tfrac12(e_t-i\vec e_z).
$$
The inverse is
$$
S^{-1}=
\begin{pmatrix}
1&0&0&-i\\
0&-i&1&0\\
0&-i&-1&0\\
1&0&0&i
\end{pmatrix},
\qquad
\det S=-\tfrac14 .
$$
The determinant is the normalisation of the four frame vectors, not an invariant of the algebra. The matrix satisfies $S^{\dagger}S=\tfrac12\mathrm I_4$ and $S^{-1}=2S^{\dagger}$; the factor $\tfrac12$ is the common squared norm of the frame vectors.

**The switch.** The two representations are the same operator read in two frames:
$$
L^{e}(\tilde Q)=S\,L^{P}(\tilde Q)\,S^{-1},\qquad
R^{e}(\tilde Q)=S\,R^{P}(\tilde Q)\,S^{-1},
$$
and conversely
$$
L^{P}(\tilde Q)=S^{-1}L^{e}(\tilde Q)S,\qquad
R^{P}(\tilde Q)=S^{-1}R^{e}(\tilde Q)S.
$$
On the four units,
$$
L_\mu^{e}=S\,L_\mu^{P}S^{-1},\qquad
R_\mu^{e}=S\,R_\mu^{P}S^{-1}.
$$
The coordinate columns change by
$$
p=S^{-1}q_e,\qquad q_e=S\,p,
$$
where $q_e=(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$ and $p=(P_+,X_+,X_-,P_-)^{\mathsf T}$ are the coefficients in the e-basis and in the Peirce frame.

**A change of frame, not of operator.** The switch conjugates the matrix and leaves the trace, the determinant and the characteristic polynomial unchanged. It is not a change of the algebra element and not a change of the left or right action; it is the same action written in the other basis. The two representations are therefore two displays of one representation, and the formulas of the product, the trace and the determinant below hold in both.

## The Coefficient Matrix and the Length

**The sixteen products.** Write $T^{e}_{\mu\nu}=L^{e}_\mu R^{e}_\nu$. The sixteen are the signed permutation matrices of §*The Product*, and they are an orthogonal basis of $M_4(\mathbb{C})$:
$$
\operatorname{Tr}\bigl((T^{e}_{\mu\nu})^{\mathsf T}T^{e}_{\rho\sigma}\bigr)
=4\,\delta_{\mu\rho}\delta_{\nu\sigma}.
$$
The transpose suffices because the sixteen are real. Hence every matrix has a unique expansion
$$
M=\sum_{\mu,\nu}c_{\mu\nu}T^{e}_{\mu\nu},\qquad
c_{\mu\nu}=\tfrac14\operatorname{Tr}\bigl((T^{e}_{\mu\nu})^{\mathsf T}M\bigr).
$$
The array $c(M)=(c_{\mu\nu})$ is the **coefficient matrix** of $M$. It is not the matrix: $M$ is the display of an endomorphism in the frame, $c(M)$ is the array of that endomorphism's coordinates in the sixteen-dimensional basis. The map $c$ is a linear isomorphism of $M_4(\mathbb{C})$ onto itself, and it is not an algebra map.

**The length.** The **length** $\ell(M)$ is the least number of products $L(\tilde Q)R(\tilde P)$ summing to $M$, with $\ell(0)=0$. The coefficient matrix of one product is $[Q][P]^{\mathsf T}$, of rank one; conversely every rank-one array is of that form. A sum of $r$ products therefore has coefficient rank at most $r$, and a rank factorization $c=UV$ of a coefficient array of rank $r$ reads off $r$ pairs. Hence
$$
\ell(M)=\operatorname{rank}c(M),
$$
the values are $0,1,2,3,4$, and $\ell(M)=4$ exactly when $\det c(M)\neq0$.

**Why the question arises.** The left side of that identity never mentions a basis: a product is $\tilde Q X\tilde P$ on the algebra, and a sum of products is a sum of operators. The right side does. The coefficient matrix is computed from the sixteen $T^{e}_{\mu\nu}$, which are built from the four *basis elements* $e_\mu$, so another basis of $\mathbb{B}$ produces another array for the same $M$. Two bases must return the same rank, or the length would be a property of the frame and not of the operator. This frame is the one in which the question is sharpest, because the sixteen products are also the matrices of $M_4(\mathbb{R})$ and the frame is chosen for the real structure, not for the length.

### The Change of Frame Is a Congruence

**The change.** Let $f_\alpha=\sum_\mu C_{\mu\alpha}e_\mu$ be another basis of $\mathbb{B}$, with $C$ invertible, and put $B_{\alpha\beta}=L(f_\alpha)R(f_\beta)$.

**Proposition.** (i) $B_{\alpha\beta}=\sum_{\mu\nu}C_{\mu\alpha}C_{\nu\beta}T^{e}_{\mu\nu}$. (ii) If $c'$ is the coefficient matrix of $M$ in the basis $B$, then
$$
c'(M)=C^{-1}c(M)\,C^{-\mathsf T}.
$$
(iii) Consequently $\operatorname{rank}c'(M)=\operatorname{rank}c(M)$, and the two bases return one length.

*Proof.* (i) $L$ and $R$ are linear in the element, so $L(f_\alpha)=\sum_\mu C_{\mu\alpha}L(e_\mu)$ and $R(f_\beta)=\sum_\nu C_{\nu\beta}R(e_\nu)$. (ii) Expand the same $M$ in the two bases and substitute (i):
$$
\sum_{\mu\nu}c_{\mu\nu}T^{e}_{\mu\nu}
=\sum_{\alpha\beta}c'_{\alpha\beta}B_{\alpha\beta}
=\sum_{\mu\nu}\Bigl(\sum_{\alpha\beta}C_{\mu\alpha}c'_{\alpha\beta}C_{\nu\beta}\Bigr)T^{e}_{\mu\nu},
$$
so $c=Cc'C^{\mathsf T}$ by linear independence of the sixteen. (iii) $\det C\neq0$, and multiplication on the left and on the right by invertible matrices preserves the rank.

**Only the determinant is used.** The change of this article is $S$ of §*The Switch Between the Two Representations*, and it is not orthogonal: $S^{\dagger}S=\tfrac12\mathrm I_4$ and $\det S=-\tfrac14$. None of this enters the proof. The orthogonality of the $T^{e}_{\mu\nu}$ is what makes $\tfrac14\operatorname{Tr}(T^{\mathsf T}M)$ an extraction formula in *this* frame; it plays no part in the invariance.

**The two displays of the corpus.** The Peirce operators are built from the same four units $e_\mu$, in the same order, so the abstract basis is common and only the display moves:
$$
T^{P}_{\mu\nu}=S^{-1}T^{e}_{\mu\nu}S,\qquad
M^{P}=S^{-1}M^{e}S .
$$
The coefficient matrix is therefore literally unchanged, and the two operator articles compute one number. The congruence answers a different question: what happens when the sixteen are built from another basis of *elements*, for instance from the four Peirce elements themselves. That basis is not orthogonal, so the extraction formula no longer applies to it and the dual basis must be used; the rank, and with it the length, is unchanged by (iii).

**An array is not an operator.** The same array read in two frames names two different operators, and the lengths can differ. The array $E_{11}$ has length four here and one in the Peirce frame. Both statements are true. Here $E_{11}$ is $X\mapsto\operatorname{Sc}(X)e_t$, which keeps the scalar coordinate and discards the vector part; there it is the projector onto $\tilde\Pi_+$ along the other three frame vectors, a single product. The two operators are conjugates of one another, and each keeps its length in every frame. So "the length of a matrix" means "the length of the operator whose display it is in the frame at hand", and no array has a length on its own.

**What the invariance buys.** The stratum $\{\ell\le r\}$ is cut by the $(r+1)$-minors of $c$, and a vanishing condition on minors of a congruence is basis-free. The cone $\{\ell\le1\}$ is one subvariety of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ and not two, the stratification by length is frame-free, and the length is an invariant of the endomorphism rather than of the display.

### The Sixteen Lengths

**The statement.** In this frame every matrix unit has the maximal length:
$$
\ell(E_{ij})=4,\qquad 1\le i,j\le4 .
$$
The worked case $E_{11}$ is therefore typical, and the sixteen units are the arrays furthest from the cone of products while their matrix rank is one.

**The proof.** Since $\operatorname{Tr}(A^{\mathsf T}E_{ij})=A_{ij}$ for every $A$,
$$
c(E_{ij})_{\mu\nu}
=\tfrac14\operatorname{Tr}\bigl((T^{e}_{\mu\nu})^{\mathsf T}E_{ij}\bigr)
=\tfrac14\,(T^{e}_{\mu\nu})_{ij},
$$
so $c(E_{ij})$ is a quarter of the array $W$ whose $(\mu,\nu)$ entry is the $(i,j)$ entry of $T^{e}_{\mu\nu}$. Now
$$
W_{\mu\nu}=\sum_k (L^{e}_\mu)_{ik}(R^{e}_\nu)_{kj}.
$$
Multiplication by a unit permutes the e-basis up to sign, so for fixed $i$ the nonzero entries of the four matrices $L^{e}_\mu$ in row $i$ stand in four different columns: there is exactly one $k=k(\mu)$ with $(L^{e}_\mu)_{ik}\neq0$, and $\mu\mapsto k(\mu)$ is a bijection. For the same reason, for fixed $j$ there is exactly one $k=k'(\nu)$ with $(R^{e}_\nu)_{kj}\neq0$, and $\nu\mapsto k'(\nu)$ is a bijection. Hence $W_{\mu\nu}\neq0$ exactly when $k(\mu)=k'(\nu)$, and then $W_{\mu\nu}=\pm1$. So $W$ has one nonzero entry in each row and each column, of modulus one, and $\det W=\pm1$. Therefore $\operatorname{rank}c(E_{ij})=4$ and $\ell(E_{ij})=4$.

**The table.**

| $i\backslash j$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|
| $1$ | $4$ | $4$ | $4$ | $4$ |
| $2$ | $4$ | $4$ | $4$ | $4$ |
| $3$ | $4$ | $4$ | $4$ | $4$ |
| $4$ | $4$ | $4$ | $4$ | $4$ |

**Two controls.** The identity has length one, because $\mathrm I_4=L^{e}(e_t)=T^{e}_{e_t,e_t}$ is a single product; and $\ell(E_{11})=4$. The value four is the maximum, so the sixteen units are as far from the cone as four independent directions can be.

**The other frame.** In the Peirce frame the same sixteen arrays have length one, not four. The arrays name different operators, and §*The Change of Frame Is a Congruence* is the reason both counts are right. There the products are monomial and every unit is a product; here the products are monomial too and every unit is maximally long. A monomial display therefore decides nothing about the length: only the position of the coordinate axes relative to the cone does. The e-basis is the frame of the real slice and of the signed permutations; it is not the frame of the short coordinate units.


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
The trace is the sum of the four diagonal entries, each equal to $Q_t$; the factor $4$ is the dimension of $\mathbb{B}$. The trace sees the scalar part and no vector coefficient.

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
The determinant is the square of the $2\times2$ determinant, since the $2\times2$ image has determinant $\langle\tilde Q\rangle_{\natural}$. It is a quartic in the four coefficients, and it vanishes exactly on the null cone $\langle\tilde Q\rangle_{\natural}=0$.

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

**The doubling rule.** Every quantity of the entry size changes in one of three ways at the regular size.

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

The first five rows are the block form: the regular matrix is two copies of the $2\times2$ image, so additive quantities double, multiplicative ones square, and the spectrum is repeated. The last three are not consequences of the block form, and each is a place where a formula must be rewritten rather than rescaled. The minimal polynomial is the striking case: the characteristic polynomial squares and the minimal polynomial does not, because the square of the characteristic polynomial is not the minimal polynomial.

**The adjugate.** The adjugate of the regular matrix is
$$
\operatorname{adj}M=\det(M)M^{-1}=\langle\tilde Q\rangle_{\natural}M^{\mathsf T},
$$
using the identity $M^{-1}=M^{\mathsf T}/\langle\tilde Q\rangle_{\natural}$ above. It is of degree three in the entries of $M$, and it is not $(\operatorname{Tr}M)\mathrm I_4-M$, which is linear. The iteration is
$$
\operatorname{adj}\bigl(\operatorname{adj}M\bigr)=\langle\tilde Q\rangle_{\natural}^4M,
$$
so the adjugate is not an involution at this size, in contrast with the entry size, where $\operatorname{adj}(\operatorname{adj}A)=A$. It remains an anti-automorphism, $\operatorname{adj}(M_1M_2)=\operatorname{adj}M_2\operatorname{adj}M_1$, and it is not one of the four words $M$, $M^{\mathsf T}$, $M^{*}$, $M^{\dagger}$: it is $\langle\tilde Q\rangle_{\natural}$ times the first of them.

**The transpose is used here, and not elsewhere.** Both formulas above use $M^{\mathsf T}=M^{\natural}$, which holds in the e-basis. In a frame where the transpose is another word, the same adjugate is $\langle\tilde Q\rangle_{\natural}$ times the matrix of $\natural$, and the transpose must be replaced by the conjugation.

## The Four Norms

**Four quarter-traces.** The determinant is one of four quadratic invariants of the element. Each is the quarter-trace of a word in $M$, and the quarter is the price of the block: a trace of the regular matrix is twice the trace of the entry matrix, so a quadratic word in the regular matrix has four times the entry-size value.

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
The word is the square of the regular matrix closed by a trace. Since $\operatorname{Tr}(M^2)=2\operatorname{Tr}(A^2)$ and $\operatorname{Tr}(A^2)=2P$ for the $2\times2$ image $A$, the factor $4$ is the product of the repetition of the block and the factor $2$ of the trace of $A^2$.

**The quaternionic norm.** In this basis $M^{\mathsf T}=M^{\natural}$, so
$$
M^{\mathsf T}M=M(\tilde Q^{\natural}\tilde Q)=M\bigl(\langle\tilde Q\rangle_{\natural}e_t\bigr)=\langle\tilde Q\rangle_{\natural}\mathrm I_4,
$$
and the quarter-trace is $N$. The determinant is the square of the same number, and it is the only one of the four that is multiplicative.

**The Hermitian norm.** The dagger is the entrywise conjugate transpose, so
$$
\operatorname{Tr}(M^{\dagger}M)=\sum_{ij}\lvert M_{ij}\rvert^2=2\sum_{ij}\lvert\mathsf M_2(\tilde Q)_{ij}\rvert^2=4H .
$$
It is a quarter of the square of the Hilbert–Schmidt norm of the regular matrix and a half of the square of that of the entry matrix, and it is the only one of the four that is positive definite on the complex algebra.

**The Krein norm.** The mixed word is the one of the $2\times2$ model in the same basis,
$$
\operatorname{Tr}(M^{\mathsf T}M^{\dagger})=\operatorname{Tr}\bigl(M(\tilde Q^{\natural})M(\tilde Q^{*})\bigr)=4K,
$$
because the product of the two conjugates has scalar part $K$. The norm is positive on the centre and negative on the vector subspace, of signature $(2,6)$ on the real algebra.

**The basis again.** The second and fourth rows use $M^{\mathsf T}=M^{\natural}$, which is a property of the e-basis and not of the regular representation. In a frame where the transpose is another word, the two words must be written with the conjugation, and $\tfrac14\operatorname{Tr}(M^{\mathsf T}M)$ is then none of the four norms: the entries of the transposed matrix are not the coefficients of the conjugate element, and the quarter-trace is a different quadratic form.

## The Six Subspaces

**The table.** The six remarkable subspaces are defined in *Subspaces and Decompositions of the Biquaternion Algebra*. On the image of the e-basis representation they become the conditions of the table. Write $\vec q=(q_x,q_y,q_z)$ and $\vec q'=(q'_x,q'_y,q'_z)$ for the split $Q_\mu=q_\mu+iq'_\mu$, and recall $B^2=Q_x^2+Q_y^2+Q_z^2$. In the third column, $\overline M$ is the entrywise complex conjugate of $M$ and $M^{\dagger}=\overline M^{\mathsf T}$; $\mathsf M_2(\tilde Q)$ is the $2\times2$ image of $\tilde Q$. The table gives the condition on $M=L^{e}(\tilde Q)$ inside the image $\mathbb{B}_L$, the real dimension of the subspace, the trace of $M$, and the determinant of the $2\times2$ image. In the first row, $\lambda=Q_t$.

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

The trace is $4Q_t$, the determinant is $\langle\tilde Q\rangle_{\natural}^2$, and the eigenvalues are $Q_t\pm iB$, each twice. The stitch between the two matrices is $R^{e}(\tilde Q)=D L^{e}(\tilde Q)^{\mathsf T}D$, with $D$ the switch matrix displayed in §*The Stitch Between the Left and the Right*. The switch from the Peirce frame to the e-basis is $L^{e}=S L^{P}S^{-1}$, $R^{e}=S R^{P}S^{-1}$, with $\det S=-\tfrac14$. The six subspaces are the scalar, traceless, real, purely imaginary, Hermitian and anti-Hermitian matrices of the image, of real dimensions $2,6,4,4,4,4$, with the traces and determinants of the table. The image is four-dimensional inside the sixteen of $M_4(\mathbb{C})$, most of the ambient matrix is not an element, and the four norms are the four quarter-traces of the words in the regular matrix.

The sixteen products $T^{e}_{\mu\nu}=L^{e}_\mu R^{e}_\nu$ are an orthogonal basis of $M_4(\mathbb{C})$, and the coefficient matrix $c(M)$ collects the coordinates of a matrix in that basis. The length is the least number of products summing to a matrix, and it equals $\operatorname{rank}c(M)$. The coefficient matrix depends on the frame and its rank does not: a change of the algebra basis sends $c$ to $C^{-1}cC^{-\mathsf T}$, a congruence. So the length belongs to the operator and not to the array that displays it, and the sixteen matrix units all have length four here while the same sixteen arrays have length one in the Peirce frame.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ | the e-basis |
| $\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ | the standard Peirce frame, built from $\vec\Xi=i\vec e_z$ |
| $\vec\Xi=i\vec e_z$ | the root, $\vec\Xi^2=e_t$ |
| $L_\mu^{e}$, $R_\mu^{e}$ | the left and right matrices of the four units |
| $L^{e}(\tilde Q)$, $R^{e}(\tilde Q)$ | the left and right matrices of $\tilde Q$ |
| $D$, entries $(1,-1,-1,-1)$ on the diagonal | the switch matrix, quaternion conjugation in the e-basis |
| $S$ | the change matrix, columns the frame vectors in the e-basis |
| $P_\pm$, $X_\pm$ | the coefficients in the Peirce frame |
| $s_\mu$ | the sign of $e_\mu^{\natural}=s_\mu e_\mu$, the diagonal entry of $D$ |
| $\mathsf M_2(\tilde Q)$ | the $2\times2$ image of $\tilde Q$ |
| $\langle\tilde Q\rangle_{\natural}$ | $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ |
| $B^2$ | $Q_x^2+Q_y^2+Q_z^2$ |
| $q_\mu$, $q'_\mu$ | the real and imaginary parts of $Q_\mu$ |
| $T^{e}_{\mu\nu}=L^{e}_\mu R^{e}_\nu$ | the sixteen products, an orthogonal basis of $M_4(\mathbb{C})$ of norm two |
| $c(M)$ | the coefficient matrix, $c_{\mu\nu}=\tfrac14\operatorname{Tr}((T^{e}_{\mu\nu})^{\mathsf T}M)$ |
| $\ell(M)$ | the length, the least number of products summing to $M$; equal to $\operatorname{rank}c(M)$ |
| $C$, $B_{\alpha\beta}$ | a change of algebra basis, $f_\alpha=\sum_\mu C_{\mu\alpha}e_\mu$, and the products $L(f_\alpha)R(f_\beta)$ |

## Further Reading

- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the six subspaces and the three decompositions.
- [The Element, the Coordinates and the Conjugations in the Biquaternion Algebra](the-element-the-coordinates-and-the-conjugations.html), for the four conjugations and the coordinate systems.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra and the multiplication table.
- [$M_4(\mathbb{C})$ Standard Peirce Representation](m4c-standard-peirce-representation-the-matrix-product-the-trace-and-the-determinant.html), for the same content in the standard Peirce frame, the pure swap stitch and the tensor displays.
- [$M_4(\mathbb{C})$ e-basis Representation : Operators](m4c-e-basis-representation-operators.html), for the operators on the algebra and the sixteen products in the e-basis.
- [$M_4(\mathbb{C})_{\mathbb{B}_L}$ Representation : The Six Subspaces as Matrix Conditions](m4c-model-the-six-subspaces-as-matrix-conditions.html), for the six subspaces read in the e-basis.
- [$M_4(\mathbb{C})_{\mathbb{B}_L}$ Representation : The Product, the Trace and the Determinant](m4c-model-the-product-the-trace-and-the-determinant.html), for the same invariants in the matrix model.
