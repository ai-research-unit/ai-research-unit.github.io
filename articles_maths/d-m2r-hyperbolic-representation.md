# __$M_2(\mathbb{R})$ Hyperbolic Representation__

## Introduction

**The model.** Left multiplication by the split-complex number $Q=q+jq'$ in the basis $(1,j)$ is the $\mathbb{R}$-linear map $X\mapsto QX$ of the two-dimensional algebra, and its matrix is the **hyperbolic Cayley matrix**

$$
\mathsf{M}_2(Q)=\begin{pmatrix}q&q'\\ q'&q\end{pmatrix}=qI_2+q'J,\qquad J=\begin{pmatrix}0&1\\ 1&0\end{pmatrix},\qquad J^{2}=+I_2,
$$

the sign of the square of the generator being the whole difference from the complex model. The map is an injective $\mathbb{R}$-algebra homomorphism, and its image is the two-dimensional algebra of **hyperbolic** matrices.

**The same size as the algebra, and the first split model.** The algebra is two-dimensional and the ambient four-dimensional, as in the complex category; but the algebra is now $\mathbb{R}[j]/(j^{2}-1)\cong\mathbb{R}\times\mathbb{R}$, a product of two copies of the field, and the model displays the consequences one by one:

- two idempotents, hence a Peirce frame, two minimal ideals, two corners and a decomposition of every element;
- two null lines, hence zero divisors, and a rank that drops to one on them;
- a determinant that is indefinite, with zero set a pair of lines and not a point;
- a unit group with four components and a hyperbolic angle instead of a circle;
- the same two dimensions as the complex case, so that every difference between the two articles is a difference of the algebras and not of their sizes.

That last point is what makes this category the cleanest comparison in the block. The complex and split-complex models are the same map, $qI_2+q'J$, with $J^{2}=\pm I_2$; so the two articles can be read side by side, entry against entry, and the sign is the only parameter.

**A correction to the received picture, recorded here.** It is often said that at a zero divisor the two spectral projectors coalesce and the matrix is no longer diagonalisable. Both halves are false in this algebra, and the falsehood is instructive. The algebra is reduced, $x^{2}-1$ has distinct roots, so every element is semisimple and every matrix of the image is diagonalisable over $\mathbb{R}$, zero divisor or not. The projectors $\rho_\pm$ are the *fixed* matrices $\mathsf{M}_2(\Pi_\pm)$, independent of $Q$, and they never coalesce. What a zero divisor loses is the inverse, the modulus and the polar word — not the diagonalisation. The confusion comes from the nilpotent case, which belongs to the dual numbers and to the biquaternions and not here; the correct statement is made in the section on the spectral projectors.

**Boundaries.** The algebra, its idempotents, its ideals and the general representation theory are *Split-Complex Linear Representations*, *Ideals and Peirce Decomposition of the Split-Complex Algebra* and *Split-Complex Two-Component Element Representation*; the norm, the unit criterion and the null cone are *Norm and Invertibility in the Split-Complex Algebra*; the spectrum and the eigenbasis are *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number* and *Relations between the Split Norm and Spectral Regularity and Degeneracy*; the polar decomposition is *Modulus–Unit Polar Decomposition of Split-Complex Numbers* and *Exponential Polar Decomposition of Split-Complex Numbers*. The operators of this model are *$M_2(\mathbb{R})$ Hyperbolic Representation : Operators*.

**Conventions.** The basis is $(1,j)$ with $j^{2}=+1$; the element is $Q=q+jq'$; the conjugate is $\bar Q=q-jq'$; the norm is $\langle Q\rangle_{*}=Q\bar Q=q^{2}-q'^{2}$. The idempotents are $\Pi_\pm=\tfrac12(1\pm j)$ and the idempotent coordinates are $\lambda_\pm=q\pm q'$. The generator of the image is $J$ and the split form is $g=\operatorname{diag}(1,-1)$. The transpose is written $^{\mathsf T}$.

## The Frame

**Definition.** The **hyperbolic Cayley matrix** of $Q$ is the matrix whose columns are the coordinate columns of $Q\cdot1$ and $Q\cdot j$:

$$
\mathsf{M}_2(Q)=\bigl(\ Q\cdot1\ \big|\ Q\cdot j\ \bigr)=\begin{pmatrix}q&q'\\ q'&q\end{pmatrix}.
$$

**The reading.** The first column is $Q$ itself; the second is $Qj=q'+jq$, which is the first column with its two entries exchanged. So the matrix is **symmetric**, and the second column is obtained from the first by the transposition of the two coordinates, which is the reflection $j$ acting on the left. The map is injective by inspection, since $Q$ is the first column.

**The four entries.** Two independent entries against four, as in the complex case, and the shape condition is the same shape condition read with the other sign: $q$ on the diagonal and $q'$ on both off-diagonal positions, where the complex model had $-q'$ and $+q'$.

**The hyperbolic unit.** The matrix

$$
J=\mathsf{M}_2(j)=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}
$$

is the swap, $J^{2}=I_2$, of eigenvalues $+1$ and $-1$ and of determinant $-1$. It is the model's name for $j$, and the identity $J^{2}=I_2$ is the matrix form of $j^{2}=1$. Its two eigenlines are the diagonal and the anti-diagonal, which are the **two null directions**: the eigenvectors of $J$ are $v_+=(1,1)$ and $v_-=(1,-1)$, and they are exactly the null vectors of the split form, and exactly the coordinate lines of the Peirce frame. This coincidence is the content of the whole article, and it is the reason the split model is diagonalised by a single matrix whereas the complex model needs a complex change of basis.

**The image.** The image is

$$
M_2(\mathbb{D})=\left\{\begin{pmatrix}q&q'\\ q'&q\end{pmatrix}:q,q'\in\mathbb{R}\right\}=\mathbb{R}[J],
$$

of dimension two, commutative, with $I_2$ and $J^{2}=I_2$; it is $\mathbb{R}[x]/(x^{2}-1)\cong\mathbb{R}\times\mathbb{R}$. So the image is a **split semisimple** algebra: it is a product of two copies of $\mathbb{R}$, not a field, and the two factors are the two idempotents. This is the first place where the series produces an algebra with a nontrivial Peirce frame at the smallest possible size.

**Theorem (the image is the centraliser of $J$).** For $C=\begin{pmatrix}p&n\\ s&t\end{pmatrix}$,

$$
CJ=JC\iff n=s\ \text{and}\ p=t,
$$

so the centraliser of $J$ in $M_2(\mathbb{R})$ is the image, of dimension two.

**Proof.** $CJ=\begin{pmatrix}n&p\\ t&s\end{pmatrix}$ and $JC=\begin{pmatrix}s&t\\ p&n\end{pmatrix}$; equality gives the two conditions.

**The Peirce frame, and the change that reaches it.** The idempotents of the algebra are $\Pi_\pm=\tfrac12(1\pm j)$, and their images are the two rank-one projectors

$$
\rho_+=\mathsf{M}_2(\Pi_+)=\frac12\begin{pmatrix}1&1\\ 1&1\end{pmatrix},\qquad
\rho_-=\mathsf{M}_2(\Pi_-)=\frac12\begin{pmatrix}1&-1\\ -1&1\end{pmatrix}.
$$

The change of basis from $(1,j)$ to $(\Pi_+,\Pi_-)$ is the Hadamard matrix

$$
H=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\ 1&-1\end{pmatrix},\qquad H^{2}=I_2,\qquad H^{\mathsf T}=H,\qquad \det H=-1,
$$

and it diagonalises the whole image at once:

$$
H\,\mathsf{M}_2(Q)\,H=\operatorname{diag}(\lambda_+,\lambda_-),\qquad \lambda_\pm=q\pm q'.
$$

**The reading of the change.** Three properties are worth separating.

- Because $H^{-1}=H^{\mathsf T}=H$, the diagonalisation is **at the same time a similarity and a congruence**: the map $M\mapsto HMH$ is both, so the change of basis and the change of quadratic form are one operation. In the complex case the diagonalising matrix was unitary and there was no real congruence formula at all; here the congruence exists and it is the statement.
- The congruence sends the split form to the generator: $HgH=J$, so the Peirce frame is the frame in which the norm's matrix becomes the algebra's own generator. The two null lines of $g$ become the two coordinate axes, which is what a Peirce frame is.
- The matrix $H$ is **orthogonal**, hence an isometry of the Euclidean plane, and it is **not** in the image: its diagonal entries are $\pm1/\sqrt2$, unequal. So the Peirce frame is not reached by a conformal map of the split form; it is reached by a Euclidean reflection. The reflection axis is the line at $\pi/8$, half of the quarter turn between the frame and the null lines. That is the only place in the category where a half angle appears, and it is an angle of the plane and not a weight of a representation.

**The two readings of the frame.** The basis $(1,j)$ is the **element frame**: its coordinates are the coefficients of $Q$, and the matrix in it is the Cayley matrix. The basis $(\Pi_+,\Pi_-)$ is the **spectral frame**: its coordinates are the idempotent coordinates $\lambda_\pm$, and the matrix in it is diagonal. The first frame is the same for every element, and so is the second: the algebra is commutative, so the two frames do not depend on $Q$. This is the sharpest operational difference from the matrix algebras of the block, where the spectral frame moves with the element.

**The complexified model of size four, as a closing subsection.** Extending scalars to $\mathbb{C}$ gives $\mathbb{D}_{\mathbb{C}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{D}\cong\mathbb{C}[j]/(j^{2}-1)\cong\mathbb{C}\times\mathbb{C}$, of real dimension four, and its real regular representation in the basis $1,i,j,ij$ is

$$
\mathsf{M}_4(X)=\begin{pmatrix}a&-b&c&-d\\ b&a&d&c\\ c&-d&a&-b\\ d&c&b&a\end{pmatrix},\qquad X=q+jq',\quad q=a+ib,\quad q'=c+id,
$$

with

$$
\operatorname{tr}\mathsf{M}_4(X)=4a,\qquad \det\mathsf{M}_4(X)=\lvert q^{2}-q'^{2}\rvert^{2}=\lvert\lambda_+\lambda_-\rvert^{2},
$$

and the four real eigenvalues $\lambda_+,\overline{\lambda_+},\lambda_-,\overline{\lambda_-}$. This is **not a second model of $\mathbb{D}$**: it is the regular representation of the complexification, which is the reduced biquaternion algebra $\mathbb{C}\times\mathbb{C}$, and the $2\times2$ model of this article is the model of $\mathbb{D}$ itself. It is recorded here as a section because the determinant is a square, $N_{\mathbb{C}}^{2}$, exactly as in the quaternion regular model, and because it shows the pattern of the series: realifications square the determinant and double the size.

## The Left and the Right Matrices

**The two families coincide.** The algebra is commutative, so

$$
R_Q=L_Q=\mathsf{M}_2(Q),
$$

and there is one copy of the algebra in the ambient, of dimension two.

**The double centraliser, in its degenerate form.** By the centraliser theorem the centraliser of the image is the image, so

$$
C\bigl(\mathsf{M}_2(\mathbb{D})\bigr)=\mathsf{M}_2(\mathbb{D}),
$$

and the image is a **maximal commutative subalgebra** of $M_2(\mathbb{R})$: no larger commutative subalgebra contains it, because anything commuting with it is already in it. So the algebra, its centraliser and its bicommutant are one subspace of dimension two, and the double centraliser theorem holds with all three terms equal.

**Why the collapse.** The map $A\otimes A^{\mathrm{opp}}\to\operatorname{End}_{\mathbb{R}}(A)$, $(a,b)\mapsto L_aR_b$, has for its image the two-sided family and for its domain a space of dimension four. Here the map factors through the multiplication $A\otimes A\to A$ because the algebra is commutative, so its image is the product of the family with itself, which is the family: dimension two, not four. The general theorem — the map is an isomorphism exactly when $A$ is central simple — fails here at the first hypothesis, since $\mathbb{R}\times\mathbb{R}$ is commutative and therefore has a nontrivial centre. The operator article draws the consequence.

**The involution is not the transpose.** In the complex model the conjugation of the algebra was transposition of matrices. Here it is not, and the reason is that every matrix of the image is already symmetric:

$$
\mathsf{M}_2(Q)^{\mathsf T}=\mathsf{M}_2(Q),\qquad \mathsf{M}_2(\bar Q)=\begin{pmatrix}q&-q'\\ -q'&q\end{pmatrix}=g\,\mathsf{M}_2(Q)^{\mathsf T}g,
$$

with $g=\operatorname{diag}(1,-1)$. So the transpose does nothing, and the involution that produces the conjugate is the transpose **conjugated by the split form**. The complex category had adjugate $=$ transpose $=$ image of the conjugate; here only the last two hold with the correction of $g$, and the adjugate is $g\mathsf{M}_2(Q)^{\mathsf T}g$ as well. This is the first appearance in the series of a **signed transpose**, and it is the same device the quaternion models needed.

## The Product

**Theorem (multiplicativity).** For all $Q,P$,

$$
\mathsf{M}_2(Q)\mathsf{M}_2(P)=\mathsf{M}_2(QP).
$$

**Proof.** Associativity of the algebra. Concretely, with $P=p+jp'$,

$$
\begin{pmatrix}q&q'\\ q'&q\end{pmatrix}\begin{pmatrix}p&p'\\ p'&p\end{pmatrix}
=\begin{pmatrix}qp+q'p'&qp'+q'p\\ qp'+q'p&qp+q'p'\end{pmatrix}
=\mathsf{M}_2(QP).
$$

**The image is closed** under products, sums and real scalars, contains $I_2$, is two-dimensional, commutative and semisimple, and is not a field.

**The Peirce arithmetic in the image.** With $\rho_\pm=\mathsf{M}_2(\Pi_\pm)$,

$$
\rho_+^{2}=\rho_+,\qquad \rho_-^{2}=\rho_-,\qquad \rho_+\rho_-=0,\qquad \rho_++\rho_-=I_2,\qquad \rho_\pm^{\mathsf T}=\rho_\pm,
$$

and for every element

$$
\mathsf{M}_2(Q)=\lambda_+\rho_++\lambda_-\rho_- .
$$

So the image contains a **complete system of two orthogonal rank-one projectors summing to the identity**, and every member of the image is a linear combination of them. The off-diagonal matrix units $E_{12}$ and $E_{21}$ are not in the image, because the image is commutative; so the image is a *commutative* Peirce frame, of the diagonal type, and the ambient's full system of four matrix units is not reachable.

**The zero divisors.** Since $\mathsf{M}_2(QP)=\mathsf{M}_2(Q)\mathsf{M}_2(P)$ and the determinant is multiplicative,

$$
\mathsf{M}_2(Q)\mathsf{M}_2(P)=0\iff\det\mathsf{M}_2(Q)\det\mathsf{M}_2(P)=0,
$$

so the image has zero divisors exactly on the two null lines, and they multiply by the rule $\rho_+\rho_-=0$: a null element of one line annihilates the other line and nothing else. The ambient has nilpotents ($E_{12}^{2}=0$); the image has none, because $x^{2}-1$ is squarefree.

## The Trace

**Theorem (the trace).** For every $Q$,

$$
\operatorname{tr}\mathsf{M}_2(Q)=2q=2\operatorname{Re}Q=\lambda_++\lambda_- .
$$

**Proof.** Both diagonal entries are $q$.

**The scalar part.** It is recovered as $\tfrac12\operatorname{tr}$, and

$$
\operatorname{tr}\mathsf{M}_2(Q)=0\iff Q\in j\mathbb{R}_{\mathbb{D}},
$$

so the trace projects onto the real line and its kernel is the $j$-line. In the spectral frame the trace is the sum of the two eigenvalues, which is the general statement; in the complex case the same formula held, with complex eigenvalues.

**The trace form.** With $P=p+jp'$,

$$
\operatorname{tr}\bigl(\mathsf{M}_2(Q)\mathsf{M}_2(P)\bigr)=2(qp+q'p'),
$$

so the Gram matrix of the form $(Q,P)\mapsto\operatorname{tr}(\mathsf{M}_2(Q)\mathsf{M}_2(P))$ is

$$
G_{\operatorname{tr}}=2I_2,\qquad\text{signature }(2,0).
$$

**The reading, and the reversal.** The trace form of the split-complex algebra is **positive definite**: it is the Euclidean form of the coefficient plane, twice the standard inner product. In the complex category the trace form was the Minkowski form $\operatorname{diag}(2,-2)$ and the determinant was the Euclidean one; here the two forms have exchanged roles. This is the sharpest single contrast of the block, and it is worth stating as a rule:

| | determinant form | trace form |
|---|---|---|
| $\mathbb{C}$ | Euclidean, $(2,0)$ | Minkowski, $(1,1)$ |
| $\mathbb{D}$ | Minkowski, $(1,1)$ | Euclidean, $(2,0)$ |

**Why the exchange happens.** The trace of the square is the sign of the algebra: $\operatorname{tr}\mathsf{M}_2(1)^{2}=+2$ and $\operatorname{tr}\mathsf{M}_2(j)^{2}=\operatorname{tr}(J^{2})=+2$ here, whereas for the complex model $\operatorname{tr}(J^{2})=\operatorname{tr}(-I_2)=-2$. The trace form reads the sign of $j^{2}$ **positively on both generators**, since both are $+I_2$; the determinant reads it **negatively on the second**, since $\det J=-1$. So the two forms of the plane are the two ways of signing the same data, and the algebra chooses the split signature for the multiplicative form and the definite one for the trace.

**What the trace does not see.** The $j$-coordinate, exactly as in the complex case: the trace is a coordinate. It is blind to the sign of the norm and to the null cone.

## The Determinant

**Theorem (the determinant is the split norm).**

$$
\det\mathsf{M}_2(Q)=q^{2}-q'^{2}=\langle Q\rangle_{*}=\lambda_+\lambda_- .
$$

**Proof.** $q^{2}-q'^{2}$ from the display; also the determinant is the product of the eigenvalues $q\pm q'$.

**The reading.** This is the indefinite determinant. Its zero set in the algebra is the pair of lines $q=\pm q'$, which is the **null cone** of the split form and the **zero-divisor set** of the algebra. The determinant is therefore not a norm in the analytic sense: it is negative on the region $\lvert q\rvert<\lvert q'\rvert$, and it vanishes on two lines rather than at a point.

**The four consequences.**

- **Signature.** The determinant form on the algebra has Gram matrix $g=\operatorname{diag}(1,-1)$ and signature $(1,1)$: it is the Minkowski form of the plane, and the algebra is a Lorentzian plane with the two null lines for light rays.
- **Rank drop.** On the null lines the matrix has rank one, not zero: a null element $Q=\lambda_+\Pi_+$ gives $\mathsf{M}_2(Q)=\lambda_+\rho_+$, of image the line $\mathbb{R}\Pi_+$ and kernel the line $\mathbb{R}\Pi_-$. So the image of the model contains matrices of rank two, one and zero, and the rank is one exactly on the null cone.
- **Unit criterion.** $Q$ is a unit $\iff\langle Q\rangle_{*}\neq0\iff\det\mathsf{M}_2(Q)\neq0\iff\mathsf{M}_2(Q)$ is invertible. As in the complex case all four statements coincide; what changes is that the first set is now the complement of two lines rather than of a point.
- **Multiplicativity.** $\det(\mathsf{M}_2(Q)\mathsf{M}_2(P))=\langle Q\rangle_{*}\langle P\rangle_{*}=\langle QP\rangle_{*}$, without correction.

**The geometry.** The determinant is the signed area scaling, and it is indefinite because the image contains reflections: $\mathsf{M}_2(j)=J$ has determinant $-1$ and reverses orientation. So the image meets both components of $GL_2(\mathbb{R})$, and the unit group has four components rather than two.

**The comparison with the two neighbouring categories.** In the complex algebra the zero set of the determinant was a point and the algebra a field. In the dual numbers, treated next in Part VI, the determinant is degenerate and its zero set a whole line, with nilpotents. Here the zero set is a pair of lines and the algebra is reduced. So the sign of the determinant's zero set — none, two lines, one line — is the whole trichotomy of the first three categories, and the model displays it as the sign of $J^{2}$.

## The Spectral Projectors

**The eigenvalues.** The characteristic polynomial is

$$
\chi(\lambda)=\lambda^{2}-2q\lambda+(q^{2}-q'^{2})=(\lambda-\lambda_+)(\lambda-\lambda_-),\qquad \lambda_\pm=q\pm q',
$$

with discriminant $4q'^{2}$. The eigenvalues are real for every $Q$, and they are distinct exactly when $q'\neq0$; they coincide exactly when $Q$ is a scalar $q$, in which case $\mathsf{M}_2(Q)=qI_2$.

**The projectors.** The two idempotents give the two projectors

$$
\rho_+=\frac12\begin{pmatrix}1&1\\ 1&1\end{pmatrix},\qquad \rho_-=\frac12\begin{pmatrix}1&-1\\ -1&1\end{pmatrix},
$$

of rank one, with $\rho_++\rho_-=I_2$ and $\rho_+\rho_-=0$, and the spectral decomposition

$$
\mathsf{M}_2(Q)=\lambda_+\rho_++\lambda_-\rho_-
$$

holds for **every** $Q$, including the scalar case, where the formula reads $q(\rho_++\rho_-)=qI_2$ and the two coefficients are equal. So the two projectors never coalesce; what fails at $q'=0$ is only the *uniqueness* of the decomposition, not its existence.

**The Peirce frame.** The two projectors are the images of the two idempotents, and they are the diagonal matrix units of the model in its own spectral frame:

$$
H\rho_+H=\begin{pmatrix}1&0\\ 0&0\end{pmatrix}=E_{11},\qquad H\rho_-H=\begin{pmatrix}0&0\\ 0&1\end{pmatrix}=E_{22}.
$$

So the image is, up to conjugation by the Euclidean reflection $H$, the diagonal subalgebra of $M_2(\mathbb{R})$. The Peirce frame, the diagonal matrix units and the spectral projectors are here one object in three notations, and this is the first category in which that identification is exact and complete.

**The zero divisor case, stated correctly.** Let $Q\neq0$ be null, say $Q=\lambda_+\Pi_+$ with $\lambda_+\neq0$. Then

$$
\mathsf{M}_2(Q)=\lambda_+\rho_+,\qquad \operatorname{rank}=1,\qquad \operatorname{im}=\mathbb{R}\Pi_+,\qquad \ker=\mathbb{R}\Pi_-,
$$

the eigenvalues are $\lambda_+$ and $0$, they are **distinct**, and the matrix is **diagonalisable**, with the same fixed projectors as every other element. The claim that the projectors coalesce or that the matrix is not diagonalisable is false: there is no nilpotent in the image, and the Jordan form is diagonal at every element. What the zero divisor loses is the inverse, the modulus and the polar decomposition; it does not lose the eigenbasis. The nilpotent case belongs to the dual numbers, where $j^{2}=0$ and the discriminant vanishes identically.

**The eigenbasis.** The eigenvectors are

$$
u_+=\frac{1}{\sqrt2}\begin{pmatrix}1\\ 1\end{pmatrix},\qquad u_-=\frac{1}{\sqrt2}\begin{pmatrix}1\\ -1\end{pmatrix},
$$

the two null directions, orthonormal for the Euclidean trace form and both null for the split form. The diagonalising matrix has them for columns, and it is $H$.

**The two spinor lines.** The two eigenspaces are the two minimal ideals

$$
S_+=\mathbb{D}\Pi_+=\mathbb{R}\Pi_+,\qquad S_-=\mathbb{D}\Pi_-=\mathbb{R}\Pi_-,\qquad \mathbb{D}=S_+\oplus S_-\cong\mathbb{R}\oplus\mathbb{R},
$$

each of dimension one, and the algebra is the direct sum of them. In the model they are the two coordinate axes of the spectral frame, and they are also the two null lines of the split form. So the algebraic decomposition and the geometric null structure are the same pair of lines, which is the identity that the whole split-complex story rests on.

## The Adjugate and the Inverse

**Theorem (the adjugate is the signed transpose).**

$$
\operatorname{adj}\mathsf{M}_2(Q)=\begin{pmatrix}q&-q'\\ -q'&q\end{pmatrix}=\mathsf{M}_2(\bar Q)=g\,\mathsf{M}_2(Q)^{\mathsf T}g,
$$

and therefore

$$
\mathsf{M}_2(Q)^{-1}=\frac{\mathsf{M}_2(\bar Q)}{\langle Q\rangle_{*}}=\mathsf{M}_2\!\left(\frac{\bar Q}{\langle Q\rangle_{*}}\right),\qquad \langle Q\rangle_{*}\neq0 .
$$

**Proof.** The cofactor formula applied to the symmetric display gives $\begin{pmatrix}q&-q'\\ -q'&q\end{pmatrix}$; the two other expressions are the definitions.

**The comparison with the complex case.** There the adjugate, the transpose and the image of the conjugate were one matrix. Here they are two objects and a correction: the transpose is the matrix itself, the adjugate is the signed transpose, and the image of the conjugate is the adjugate. So the model separates the three operations that the complex model identifies, and the separating device is the split form $g$. This is the same device that relates the two one-sided families in the quaternion category, in the form $D\mathsf{M}D$; it appears here for the first time and at the smallest size.

**The conformal identity.** Multiplying the identity $\operatorname{adj}M=gM^{\mathsf T}g$ by $M$ gives

$$
M^{\mathsf T}gM=\det(M)\,g,
$$

that is

$$
\mathsf{M}_2(Q)^{\mathsf T}g\,\mathsf{M}_2(Q)=\langle Q\rangle_{*}\,g .
$$

**The reading.** Every matrix of the image is **conformal for the split form**, with conformal factor the norm. It is the exact analogue of the complex identity $M^{\mathsf T}M=NI_2$, and it is the statement that the image lies in the conformal group of the Minkowski plane:

$$
\mathsf{M}_2(\mathbb{D}^{\times})\subset CO(1,1),\qquad \mathsf{M}_2(\{Q:\langle Q\rangle_{*}=\pm1\})=O(1,1).
$$

**The four components.** The unit group is

$$
\mathbb{D}^{\times}=\{Q:\langle Q\rangle_{*}\neq0\}\cong(\mathbb{Z}/2\mathbb{Z})^{2}\times\mathbb{R}^{2},
$$

with components labelled by the pair of signs of the two idempotent coordinates $(\operatorname{sgn}\lambda_+,\operatorname{sgn}\lambda_-)$; in the matrix picture they are the four components of $O(1,1)$, distinguished by the sign of the determinant and by the timelike or spacelike nature of the two columns. The identity component is

$$
SO^{+}(1,1)=\left\{\begin{pmatrix}\cosh\phi&\sinh\phi\\ \sinh\phi&\cosh\phi\end{pmatrix}:\phi\in\mathbb{R}\right\}=\{\mathsf{M}_2(e^{\phi j})\},
$$

the one-parameter group of hyperbolic rotations, which is the **boost**. So $O(1,1)$ is to this category what $SO(2)$ was to the complex one, and the exponential of $j\phi$ is the parametrisation of its identity component.

**The non-compactness.** $SO^{+}(1,1)$ is homeomorphic to a line, not a circle: the boost is unbounded, and the level set $\langle Q\rangle_{*}=1$ has two branches, the future and the past hyperbola. The complex unit circle is compact and connected; here the definite level set is neither. The whole topology of the group of units follows from the signature of the determinant.

## The Norms

**The four forms.**

| form | definition | Gram on $(1,j)$ | signature | multiplicative |
|---|---|---|---|---|
| split norm | $\langle Q\rangle_{*}=\det\mathsf{M}_2(Q)$ | $\operatorname{diag}(1,-1)$ | $(1,1)$ | yes |
| trace form | $\operatorname{tr}(\mathsf{M}_2(Q)\mathsf{M}_2(P))$ | $2I_2$ | $(2,0)$ | no |
| Frobenius form | $\operatorname{tr}(\mathsf{M}_2(Q)^{\mathsf T}\mathsf{M}_2(P))$ | $2I_2$ | $(2,0)$ | no |
| modulus | $\lvert Q\rvert=\sqrt{\lvert\langle Q\rangle_{*}\rvert}$ | — | — | yes |

**The split norm is Minkowski.** Its Gram matrix is $g$, its signature $(1,1)$, its zero set two lines. It is the only multiplicative form, and it is indefinite.

**The trace and Frobenius forms coincide here.** Both have Gram $2I_2$, because every matrix of the image is symmetric, so $M^{\mathsf T}=M$ and the two forms agree on the image. In the complex model the two forms differed, because the image contained skew matrices. So the split category has one Euclidean form and not two, and the two coincide for the structural reason that the image is a space of symmetric matrices.

**The conformal parameter.** The identity $M^{\mathsf T}gM=\langle Q\rangle_{*}g$ says that the image acts on the Minkowski plane by similarities of factor $\langle Q\rangle_{*}$; the Euclidean form is not preserved and is not conformal for the image in general, since $\operatorname{tr}(M^{\mathsf T}M)=2(q^{2}+q'^{2})\neq2\langle Q\rangle_{*}$ unless $qq'=0$. So the two forms of the plane play strictly different roles: the definite one measures the coefficients, the indefinite one is the one the algebra respects.

**The absence of a Hermitian form.** As in the complex model there is no Hermitian form on the image, and the involution is the signed transpose. The symmetric/skew splitting of the image is degenerate here: every member is symmetric, so the skew part of the image is zero. What replaces the splitting is the Peirce splitting into the two null lines.

## The Subspaces

**The tabulation.**

| subspace | algebra condition | matrix condition | dimension |
|---|---|---|---|
| real line $\mathbb{R}_{\mathbb{D}}$ | $q'=0$ | $qI_2$, scalar | $1$ |
| $j$-line $j\mathbb{R}_{\mathbb{D}}$ | $q=0$ | $q'J$, the swap | $1$ |
| null line $S_+$ | $\lambda_-=0$ | $\lambda_+\rho_+$, rank one | $1$ |
| null line $S_-$ | $\lambda_+=0$ | $\lambda_-\rho_-$, rank one | $1$ |
| fixed set of the conjugation | $q'=0$ | symmetric with equal diagonal and $q'=0$ | $1$ |
| anti-fixed set | $q=0$ | $q'J$ | $1$ |
| the image | — | $CJ=JC$, symmetric with equal diagonal | $2$ |
| the ambient | — | — | $4$ |

**The count.** The involution group of $\mathbb{D}$ has two elements, so it produces the pair of subspaces $\mathbb{R}_{\mathbb{D}}$ and $j\mathbb{R}_{\mathbb{D}}$, of dimensions one each; but the algebra also carries two **idempotent lines** and two **null lines**, which the complex algebra does not have at all. So the distinguished-subspace count is four rather than two, and the two extra subspaces are the ones the Peirce frame creates. Against the six of the biquaternion algebra the count is still smaller, but the structure is no longer trivial.

**The image inside the symmetric matrices.** The image is a two-dimensional subspace of the three-dimensional space of symmetric matrices; the missing direction is the traceless diagonal line

$$
\left\{\begin{pmatrix}a&0\\ 0&-a\end{pmatrix}:a\in\mathbb{R}\right\}=\mathbb{R}\,g,
$$

spanned by the split form. So

$$
\operatorname{Sym}_2(\mathbb{R})=M_2(\mathbb{D})\oplus\mathbb{R}g,
$$

and the complement is exactly the matrix of the norm. The ambient then splits as

$$
M_2(\mathbb{R})=\underbrace{M_2(\mathbb{D})}_{\text{hyperbolic, dim }2}\oplus\underbrace{\mathbb{R}g}_{\text{traceless diagonal}}\oplus\underbrace{\mathfrak{so}(2)}_{\text{skew, dim }1},
$$

of dimensions $2+1+1$, and the three summands are the conformal part, the norm and the rotation. In the complex model the corresponding split was conformal plus anti-conformal; here there is a third piece, and it is the one that carries the sign of the determinant.

**The units.** The level set $\langle Q\rangle_{*}=\pm1$ is the hyperbola pair, of dimension one, and its image is $O(1,1)$; the level set $\langle Q\rangle_{*}=1$ has two components, the future and past branches, and its identity component is the boost group. The model realises $O(1,1)$ as an equality of matrix sets, exactly as the complex model realised $SO(2)$, and the difference of topology — one component against four — is the difference of signature.

**The comparison with the ambient.** The image contains no nilpotent, no skew matrix, no traceless matrix and no off-diagonal matrix unit; the ambient contains all of them. The passage from the ambient to the algebra is the passage from an arbitrary linear map to a hyperbolic similarity, and it is the imposition of two linear conditions $CJ=JC$.

## Summary

1. The hyperbolic Cayley matrix $\mathsf{M}_2(Q)=qI_2+q'J$ with $J^{2}=I_2$ is the matrix of left multiplication in the basis $(1,j)$, and $\mathsf{M}_2(Q)\mathsf{M}_2(P)=\mathsf{M}_2(QP)$.
2. The image is the two-dimensional algebra $\mathbb{R}[J]\cong\mathbb{R}\times\mathbb{R}$ of matrices symmetric with equal diagonal, characterised by $CJ=JC$; it is a split semisimple algebra and not a field.
3. The left and right multiplications coincide, the centraliser of the image is the image, and the image is a maximal commutative subalgebra of $M_2(\mathbb{R})$.
4. The trace is $2q$, the four entries are the two coefficients, and the trace form is the Euclidean form $2I_2$; the determinant is the split norm and the determinant form is Minkowski, so the two forms exchange roles against the complex category.
5. The determinant is $q^{2}-q'^{2}$, indefinite, with zero set the two null lines; on those lines the rank is one, and they are exactly the zero divisors.
6. The image contains the complete pair of orthogonal rank-one projectors $\rho_\pm=\mathsf{M}_2(\Pi_\pm)$, and every element is $\lambda_+\rho_++\lambda_-\rho_-$; the spectral frame is fixed and independent of $Q$.
7. The diagonalising matrix is the orthogonal reflection $H$ of determinant $-1$, which is at once a similarity and a congruence, sends the split form to $J$ and does not belong to the image.
8. Every element is diagonalisable, including the zero divisors; there are no nilpotents; the projectors never coalesce; the claim that a zero divisor breaks the diagonalisation is false.
9. The adjugate is the signed transpose $gM^{\mathsf T}g$, so the image is conformal for the split form, $M^{\mathsf T}gM=\langle Q\rangle_{*}g$, and the units map onto $O(1,1)$ with four components.
10. The distinguished subspaces are four — the real line, the $j$-line and the two null lines — and the ambient splits as the image plus the traceless diagonal line plus the skew line.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathsf{M}_2$ | the hyperbolic Cayley map $\mathbb{D}\to M_2(\mathbb{R})$ | this article |
| $J$ | $\mathsf{M}_2(j)=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $J^{2}=I_2$ | this article |
| $Q=q+jq'$ | a split-complex number, conjugate $\bar Q=q-jq'$ | *Split-Complex Linear Representations* |
| $\langle Q\rangle_{*}=q^{2}-q'^{2}$ | the split norm, equal to $\det\mathsf{M}_2(Q)$ | *Norm and Invertibility in the Split-Complex Algebra* |
| $\Pi_\pm=\tfrac12(1\pm j)$ | the two idempotents | *Ideals and Peirce Decomposition of the Split-Complex Algebra* |
| $\lambda_\pm=q\pm q'$ | the idempotent coordinates, the eigenvalues | *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number* |
| $\rho_\pm=\mathsf{M}_2(\Pi_\pm)$ | the two spectral projectors, of rank one | this article |
| $H=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ | the diagonalising reflection, $HM_QH=\operatorname{diag}(\lambda_+,\lambda_-)$ | this article |
| $g=\operatorname{diag}(1,-1)$ | the split form; $\operatorname{adj}M=gM^{\mathsf T}g$ | this article |
| $S_\pm=\mathbb{R}\Pi_\pm$ | the two minimal ideals, the two null lines | this article |
| $SO^{+}(1,1)$ | the boost group, the identity component of the units | *Modulus–Unit Polar Decomposition of Split-Complex Numbers* |
| $\mathsf{M}_4$ | the regular matrix of the complexification in the basis $1,i,j,ij$ | this article |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition, systems of matrix units and the regular representation.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the double centraliser theorem and the hypothesis of central simplicity that fails here.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for congruence, the Hadamard matrix, the cofactor formula and the rank of a product.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for $O(1,1)$, the boost matrices and the topology of the components.
