# __$M_2(\mathbb{R})$ Cayley Representation__

## Introduction

**The model.** The complex numbers are two-dimensional over $\mathbb{R}$, and left multiplication by $Q$ is an $\mathbb{R}$-linear map of a two-dimensional space. Its matrix in the basis $(1,i)$ is the **Cayley matrix**

$$
\mathsf{M}_2(Q)=\begin{pmatrix}q&-q'\\ q'&q\end{pmatrix}=qI_2+q'J,\qquad J=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix},\qquad J^{2}=-I_2,
$$

and the map $Q\mapsto\mathsf{M}_2(Q)$ is an injective $\mathbb{R}$-algebra homomorphism. Its image is the algebra of **conformal** matrices, of real dimension two inside the four of $M_2(\mathbb{R})$.

**The smallest model of the series, and the most degenerate.** This is the first category of Part VI, and it is the one in which the general theory has the least to say. Everything that the other categories spend sections on collapses here, and it is worth stating the collapse at the outset so that the rest of the article is not read as a list of missing theorems.

- The left and the right regular representations coincide, because the algebra is commutative. There is one copy of the algebra in the ambient, not two.
- There is no zero divisor, hence no idempotent but $0$ and $1$, hence no Peirce frame, no corners, no rank-one locus and no determinantal stratification.
- The determinant form is positive definite, hence there is no null cone and no spectral trichotomy: one spectral type, everywhere.
- The two-sided operators span a two-dimensional subspace of the four-dimensional ambient, so every member of their span is a single product, and the cone of the other categories is here a linear subspace.

So the article is short because the algebra is a field. Each absence is a statement about $\mathbb{C}$ and not a gap in the treatment, and each is recorded with the reason attached.

**What the model is good for.** Three things, and they are the reason the category exists.

- It is an **isomorphism onto its image**: the field $\mathbb{C}$ and the conformal matrices are the same object, so every algebraic question about $\mathbb{C}$ is a matrix question about a two-dimensional subspace of $M_2(\mathbb{R})$, and conversely.
- It makes the **involution visible as the transpose**: conjugation of the field is transposition of matrices, which is the sharpest form the involution takes anywhere in the series. In the quaternion models the transpose was a signed transpose or a conjugate transpose; here it is the plain one.
- It realises the **circle as the rotation group**: the units are $\mathrm{U}(1)$, their image is $SO(2)$, and the model is the classical isomorphism $\mathrm{U}(1)\cong SO(2)$ stated as a statement about matrices.

**Boundaries.** The algebra, its product, its classes and its specificities are *Complex Algebra*, *The Classes of Element of the Complex Algebra* and *The Specificities of the Complex Algebra*; the norm and the units are *Complex Norm and Invertibility*; the spectrum and the sectors are *Spectral Regularity and Degeneracy in the Complex Algebra*, *Eigenvalue Decomposition and Eigenbasis of a Complex Number* and *The Three Sectors of the Complex Algebra*; the geometry of the plane is *Rotations and Reflections in the Complex Plane* and *The Versors and the Orthogonal Group of the Complex Numbers*. The model of the algebra by matrices is also treated, for the second algebra of the block, in *The Matrix Element Representations of the Complexoid*. The operators of this model are *$M_2(\mathbb{R})$ Cayley Representation : Operators*.

**Conventions.** The basis is $(1,i)$ with $i^{2}=-1$; the element is $Q=q+iq'$, its conjugate is $\bar Q=q-iq'$, and its norm is $N(Q)=Q\bar Q=q^{2}+q'^{2}$. The real and imaginary subspaces are $\mathbb{R}_{\mathbb{C}}$ and $i\mathbb{R}_{\mathbb{C}}$. The structure matrix is $J$, and $\mathsf{M}_2$ is the Cayley map. The transpose is written $^{\mathsf T}$ and is taken in the basis $(1,i)$.

## The Frame

**Definition.** The **Cayley matrix** of $Q$ is the matrix whose columns are the coordinate columns of $Q\cdot 1$ and $Q\cdot i$:

$$
\mathsf{M}_2(Q)=\bigl(\ Q\cdot 1\ \big|\ Q\cdot i\ \bigr)
=\begin{pmatrix}q&-q'\\ q'&q\end{pmatrix}.
$$

**The reading of the display.** The first column is $Q$ itself, so the map is injective by inspection: the element is recovered from the first column. The second column is the first one rotated by a quarter turn, because $Qi=iQ$. The matrix has two independent entries against the four of the ambient, and it is the sum

$$
\mathsf{M}_2(Q)=q\,\mathsf{M}_2(1)+q'\,\mathsf{M}_2(i)=qI_2+q'J,
$$

with $\mathsf{M}_2(1)=I_2$ and $\mathsf{M}_2(i)=J$. The four entries of the display are the two coordinates, each appearing twice with a sign.

**The complex structure.** The matrix $J$ is the model's name for $i$: it is the counter-clockwise quarter turn, $J^{2}=-I_2$, and it is the unique member of the image with square $-I_2$. The identity $J^{2}=-I_2$ is the matrix form of $i^{2}=-1$, and it is the only place where the sign of the algebra enters the model.

**The frame, and the absence of a second.** There is one distinguished basis of the carrier, $(1,i)$, and one distinguished basis of the ambient in the model's own terms, $(I_2,J)$. A different choice of basis of the carrier conjugates the model, $P\mathsf{M}_2(Q)P^{-1}$, and the conjugated family is again a copy of the field; so the model is determined up to conjugacy and no second structure is at stake. This is the sharpest difference from the quaternion category, where the two-sided action produced a second family and a signed transpose $D$ was needed to relate the two.

**Theorem (the image is the centraliser of $J$).** For a real $2\times2$ matrix $M=\begin{pmatrix}p&n\\ s&t\end{pmatrix}$,

$$
MJ=JM\iff s=-n\ \text{and}\ p=t,
$$

so the centraliser of $J$ in $M_2(\mathbb{R})$ is exactly the image of $\mathsf{M}_2$, of dimension two.

**Proof.** Multiplying out, $MJ=\begin{pmatrix}n&-p\\ t&-s\end{pmatrix}$ and $JM=\begin{pmatrix}-s&-t\\ p&n\end{pmatrix}$; equality gives $n=-s$ and $p=t$.

**Three descriptions of one subspace.** The image is, equivalently:

- the matrices of the shape $qI_2+q'J$;
- the real matrices commuting with $J$;
- the matrices of the $\mathbb{R}$-linear maps $\mathbb{R}^{2}\to\mathbb{R}^{2}$ that are $\mathbb{C}$-linear under the identification $\mathbb{R}^{2}\cong\mathbb{C}$ obtained by reading a column as $x+iy$.

The equivalence of the first two is the theorem; the equivalence of the second and third is the definition of complex linearity. So the model answers the question *which real matrices are complex matrices* by a pair of linear equations, and this is the membership test of the whole category: it is linear, not determinantal.

**The uniqueness of the model.** Every two-dimensional faithful real representation of $\mathbb{C}$ is conjugate to this one. Indeed a representation is determined by the image $K$ of $i$, which is a real $2\times2$ matrix with $K^{2}=-I_2$; every such $K$ is conjugate to $J$, since $K$ has eigenvalues $\pm i$ with conjugate eigenlines and is therefore the matrix of a complex structure; and conjugating $K$ to $J$ conjugates the whole representation to $\mathsf{M}_2$. So there is one model, not a family of them, and this is the first category in which the uniqueness is absolute rather than up to the inner automorphisms of the algebra.

**The codimension.** The image is two-dimensional in a four-dimensional ambient, so half of $M_2(\mathbb{R})$ is outside it. The complement is described in the operators article and it is the space of the maps that reverse the complex structure; the model article needs only the dimension.

## The Left and the Right Matrices

**The two families coincide.** Since $\mathbb{C}$ is commutative, $Q_1Q=QQ_1$ for all $Q_1$, so the right multiplication is the left multiplication:

$$
R_Q=L_Q=\mathsf{M}_2(Q).
$$

**The reading.** There is one copy of the algebra in the ambient, of dimension two, and the left-right distinction is empty: there is no second family to compare with the first, no anti-homomorphism, and no analogue of the quaternion identity $R_{\tilde q}=D\mathsf{M}_4(\tilde q)^{\mathsf T}D$. The slot where that identity would sit is filled by the trivial statement $R_Q=L_Q$, and the article records it once rather than building a section on it.

**The double centraliser, in its degenerate form.** The centraliser of the image in $M_2(\mathbb{R})$ is the image itself, by the theorem of the previous section. So

$$
C\bigl(\mathsf{M}_2(\mathbb{C})\bigr)=\mathsf{M}_2(\mathbb{C}),
$$

and the two roles that the other categories keep apart — the algebra and its centraliser — fall on one subspace. The image is therefore a **maximal commutative subalgebra** of $M_2(\mathbb{R})$: no larger commutative subalgebra contains it, because anything commuting with it is in it. In the quaternion category the corresponding two copies had dimensions $4$ and $4$ with a one-dimensional intersection, spanning seven; here they coincide, and the sum is two.

**What the collapse costs.** The two-sided operator of the general theory needs two independent families to be interesting, and there is only one. The whole operator layer of this category therefore collapses to a statement about the multiplication of the field, and this is the structural reason for the shortness of the companion article; it is stated there and not here.

**The trace of the collapse.** Since there is one copy, the algebra is *not* the endomorphism algebra of its regular module in the strong sense of the double centraliser theorem of the quaternion case. The endomorphism algebra of the regular module is $\operatorname{End}_{\mathbb{C}}(\mathbb{C})=\mathbb{C}$, which is the image again; so the theorem holds, and it holds trivially, with both sides equal to the field. This is the precise sense in which $\mathbb{C}$ is a field and $\mathbb{H}$ is not: the field is its own endomorphism ring as a module over itself.

## The Product

**Theorem (multiplicativity).** For all $Q,P$,

$$
\mathsf{M}_2(Q)\mathsf{M}_2(P)=\mathsf{M}_2(QP).
$$

**Proof.** Associativity of the algebra, exactly as in the other categories: the matrix of a composition is the product of the matrices, and the composition of the left multiplications is the left multiplication by the product. Concretely, for $Q=q+iq'$ and $P=p+ip'$,

$$
\begin{pmatrix}q&-q'\\ q'&q\end{pmatrix}\begin{pmatrix}p&-p'\\ p'&p\end{pmatrix}
=\begin{pmatrix}qp-q'p'&-(qp'+q'p)\\ qp'+q'p&qp-q'p'\end{pmatrix}
=\mathsf{M}_2(QP).
$$

**The image is closed.** The image is closed under products, sums and real scalars, so it is a real subalgebra of $M_2(\mathbb{R})$; it is two-dimensional and it is commutative. It contains $I_2$ and it is a field: every nonzero member is invertible, because the inverse is exhibited in the section on the adjugate.

**The image is not all of $M_2(\mathbb{R})$.** The ambient is four-dimensional and contains nilpotents, idempotents other than $0$ and $1$, and non-commuting pairs; the image contains none of these. The single condition $s=-n$, $p=t$ is the whole difference, and it is worth naming the three consequences:

- no nilpotent: $\mathsf{M}_2(Q)^{2}=0$ forces $N(Q)=0$ forces $Q=0$;
- no idempotent but $0$ and $I_2$: $\mathsf{M}_2(Q)^{2}=\mathsf{M}_2(Q)$ reads $Q^{2}=Q$, and a field has no idempotent but $0$ and $1$;
- the image is a field, so it has no zero divisor: $\mathsf{M}_2(Q)\mathsf{M}_2(P)=0$ forces $Q=0$ or $P=0$, and this is the statement $\det(\mathsf{M}_2(Q)\mathsf{M}_2(P))=\det\mathsf{M}_2(Q)\det\mathsf{M}_2(P)$ with a positive definite determinant.

**The module is simple.** A left ideal of the image is an ideal of the field, so it is $\{0\}$ or the whole algebra; hence the regular module has no proper nonzero invariant subspace, and the regular representation is irreducible over $\mathbb{R}$ as well as over $\mathbb{C}$. This is the reason there is no reduction into two minimal left ideals and no Peirce decomposition, and it is the first of the absences listed in the introduction.

## The Trace

**Theorem (the trace).** For every $Q$,

$$
\operatorname{tr}\mathsf{M}_2(Q)=2q=2\operatorname{Re}Q .
$$

**Proof.** The two diagonal entries of the display are both $q$.

**The scalar part.** It is recovered as $\tfrac12\operatorname{tr}$, and it vanishes on the imaginary subspace. So the scalar line and the imaginary line are separated by the trace:

$$
\operatorname{tr}\mathsf{M}_2(Q)=0\iff Q\in i\mathbb{R}_{\mathbb{C}} .
$$

The trace is therefore a projection of the algebra onto its real part, and the traceless subspace of the image is the imaginary line, of dimension one. Compare the quaternion models, where the trace was $2q_t$ or $4q_t$ and the traceless subspace was the three-dimensional pure part: the pattern is the same and the dimension is minimal.

**The trace form.** For the two basis elements,

$$
\operatorname{tr}\bigl(\mathsf{M}_2(1)^{2}\bigr)=2,\qquad
\operatorname{tr}\bigl(\mathsf{M}_2(1)\mathsf{M}_2(i)\bigr)=0,\qquad
\operatorname{tr}\bigl(\mathsf{M}_2(i)^{2}\bigr)=\operatorname{tr}(J^{2})=-2,
$$

so the Gram matrix of the form $(Q,P)\mapsto\operatorname{tr}(\mathsf{M}_2(Q)\mathsf{M}_2(P))$ is

$$
G=\operatorname{diag}(2,-2),\qquad\text{signature }(1,1),
$$

and in coordinates

$$
\operatorname{tr}\bigl(\mathsf{M}_2(Q)\mathsf{M}_2(P)\bigr)=2(qp-q'p').
$$

**The reading.** The trace form on $\mathbb{C}$ is the **Minkowski form of the plane**: positive on the real axis, negative on the imaginary axis, invariant under the inner automorphisms (which are trivial here), and indefinite. It is the smallest instance of the family of trace forms of the series, whose signature is $(1,1)$ here and $(1,3)$ for the quaternions. The formula $2(qp-q'p')$ shows that it is not the Euclidean pairing of the coordinates but the Lorentzian one: the two axes count with opposite signs.

**What the trace does not see.** The imaginary coordinate. Two elements with the same real part have the same trace, so the trace is a coordinate and not a classification, and the whole spectral information of the algebra is invisible to it. The modulus, not the trace, separates the elements.

## The Determinant

**Theorem (the determinant is the norm).** For every $Q$,

$$
\det\mathsf{M}_2(Q)=q^{2}+q'^{2}=N(Q).
$$

**Proof.** $q\cdot q-(-q')\cdot q'=q^{2}+q'^{2}$; equivalently, the determinant of $qI_2+q'J$ is $q^{2}+q'^{2}$ because $J$ has eigenvalues $\pm i$ and the determinant is the product of the eigenvalues $q\pm iq'$.

**The reading.** This is the only model in the series in which the determinant **is** the Euclidean form of the algebra and not a power of it. The quaternion regular model had $\det=N^{2}$, a square that had to be undone; the split models have indefinite determinants; here the determinant is the norm itself, positive definite, and the algebra is a Euclidean plane.

**The consequences.**

- The zero set of the determinant in the algebra is the single point $0$: there is no null cone and no isotropic direction.
- The determinant is positive on every nonzero element, so the image of $\mathbb{C}^{\times}$ lies in $GL_2^{+}(\mathbb{R})$, the component of the identity. The unit group is connected, and it is not merely connected but a circle.
- The unit criterion collapses: $Q$ is a unit $\iff N(Q)\neq0\iff\det\mathsf{M}_2(Q)\neq0\iff\mathsf{M}_2(Q)$ is invertible. All four statements are the same statement, and the model detects invertibility exactly.
- The determinant is multiplicative, so the model carries the multiplicative property of the norm without correction: $\det(\mathsf{M}_2(Q)\mathsf{M}_2(P))=N(Q)N(P)=N(QP)$.

**The geometric reading.** The determinant is the area scaling of the map $\mathsf{M}_2(Q)$, and the modulus is its length scaling. The two are related by $\det=N=\lvert Q\rvert^{2}$ because both singular values of $\mathsf{M}_2(Q)$ are $\lvert Q\rvert$: the matrix is a similarity, so it scales lengths by $\lvert Q\rvert$ and areas by $\lvert Q\rvert^{2}$. The identity $\det=\lvert Q\rvert^{2}$ is therefore the statement that $\mathsf{M}_2(Q)$ is conformal, and it is why the image is called the conformal matrices.

**The comparison with the neighbouring categories.** In the split-complex algebra the determinant $q^{2}-q'^{2}$ is indefinite and its zero set is the pair of null lines; in the dual numbers it is degenerate and its zero set is a line. Here the zero set is a point, and this is the whole of the difference between a field and the two algebras with zero divisors: the geometry of the determinant's zero set *is* the algebraic trichotomy of Part VI's first three categories.

## The Spectral Projectors

**No real idempotent but $0$ and $I_2$.** An idempotent of the image is an idempotent of the field, hence $0$ or $1$; so the image contains no nontrivial projection, and there is no Peirce decomposition, no corner algebra and no rank-one locus inside it. This is the sharpest absence of the category, and every other absence follows from it.

**The eigenvalues.** The characteristic polynomial is

$$
\chi(\lambda)=\lambda^{2}-2q\lambda+N=(\lambda-q)^{2}+q'^{2},
$$

whose roots are $\lambda=q+iq'$ and $\bar\lambda=q-iq'$. They are real only when $q'=0$, in which case the matrix is $qI_2$ and the two roots coincide. So a non-real element of the image has no real eigenvalue, and the two eigenvalues are exchanged by conjugation. The trace is their sum, $2q$, and the determinant their product, $N$.

**The projectors over $\mathbb{C}$.** In the complexified ambient the algebra has the two idempotents

$$
P_{\pm}=\tfrac12\bigl(I_2\mp iJ\bigr),\qquad P_{+}+P_{-}=I_2,\qquad P_{+}P_{-}=0,\qquad P_{\pm}^{2}=P_{\pm},
$$

each of rank one, and the element decomposes as

$$
\mathsf{M}_2(Q)=\lambda P_{+}+\bar\lambda P_{-},\qquad \lambda=q+iq' .
$$

**The reading.** The Peirce frame of $\mathbb{C}$ exists, and it exists **only after complexification**: $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$, and the two factors are the two idempotents. Over $\mathbb{R}$ the algebra is a field and has no frame; over $\mathbb{C}$ it splits as a product of two copies of itself. The two idempotents are the two points of the spectrum, and the decomposition of the element is the Lagrange interpolation at those two points.

**The frame is the model.** The two idempotents are not new objects: their real and imaginary parts are the Cayley frame,

$$
P_{+}+P_{-}=I_2,\qquad P_{+}-P_{-}=-iJ,
$$

so the complex span of $P_{+}$ and $P_{-}$ is the complexification of the image, and their real span is the image itself. The Peirce frame of the complexified algebra and the basis of the model are the same two vectors, one read over $\mathbb{C}$ and one over $\mathbb{R}$. This is the exact sense in which the smallest algebra has a Peirce frame with two points and no corners: the frame exists, but it indexes the two points of the spectrum and not a decomposition of a matrix space.

**The eigenbasis and the diagonalising matrix.** The eigenvectors are

$$
v_{\pm}=\tfrac{1}{\sqrt2}\begin{pmatrix}1\\ \mp i\end{pmatrix},
$$

with $\mathsf{M}_2(Q)v_{+}=\lambda v_{+}$ and $\mathsf{M}_2(Q)v_{-}=\bar\lambda v_{-}$. The diagonalising matrix is

$$
U=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\ -i&i\end{pmatrix},\qquad
U^{*}\mathsf{M}_2(Q)U=\operatorname{diag}(\lambda,\bar\lambda),
$$

which is unitary and of determinant $i$, and which is the model's own discrete Fourier transform of order two.

**What the diagonalising matrix is.** It is not an arbitrary unitary. Its two columns are the two eigenvectors, and they are the **isotropic lines** of the complexified norm: over $\mathbb{C}$ the quadratic form $q^{2}+q'^{2}=(q+iq')(q-iq')$ factors as a product of two linear forms, so the complexified plane is a split quadratic space and its two null lines are exactly the two eigenlines. The diagonalisation of a rotation is therefore the statement that the complexified Euclidean plane is a hyperbolic plane, that the two eigenvalues are the two coordinate functions in its null coordinates, and that the rotation acts as a scaling in those coordinates.

**Two readings of the same matrix.** Over $\mathbb{R}$, $U$ is an orthogonal matrix of $\mathbb{R}^{4}$: it is the real matrix of the complex-linear map $(z_1,z_2)\mapsto\bigl((z_1+z_2)/\sqrt2,\ i(z_2-z_1)/\sqrt2\bigr)$, and it is the change of basis from the coordinate frame to the frame of the two points of the spectrum. Over $\mathbb{C}$ it is the matrix of the isomorphism $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\to\mathbb{C}\times\mathbb{C}$ that the two idempotents define. The two readings are one matrix, and the second is the reason the first exists.

## The Adjugate and the Inverse

**Theorem (the adjugate is the transpose).** For every $Q$,

$$
\operatorname{adj}\mathsf{M}_2(Q)=\mathsf{M}_2(Q)^{\mathsf T}=\mathsf{M}_2(\bar Q),
$$

and therefore

$$
\mathsf{M}_2(Q)^{-1}=\frac{\mathsf{M}_2(\bar Q)}{N(Q)}=\mathsf{M}_2\!\left(\frac{\bar Q}{N(Q)}\right).
$$

**Proof.** The adjugate of $\begin{pmatrix}a&b\\ c&d\end{pmatrix}$ is $\begin{pmatrix}d&-b\\ -c&a\end{pmatrix}$; applied to the display it gives $\begin{pmatrix}q&q'\\ -q'&q\end{pmatrix}$, which is both the transpose and the Cayley matrix of $\bar Q$.

**The triple coincidence.** In this model, three operations that are distinct in every other category are the same operation:

$$
\text{adjugate}=\text{transpose}=\text{the Cayley matrix of the conjugate}.
$$

The reason is that the ambient is two-dimensional and commutative and the determinant is the norm: the cofactor formula produces the conjugate, and the conjugate is what transposition gives. In the quaternion model the adjugate was $N\mathsf{M}_4(\tilde q^{*})$ and the conjugate transpose was a different matrix; here the factor $N$ is absent because the determinant is already the norm, and the two formulas merge.

**The consequence for the geometry.** The identity $\operatorname{adj}=\,^{\mathsf T}$ reads $\mathsf{M}_2(Q)^{-1}=\mathsf{M}_2(Q)^{\mathsf T}/N$, that is

$$
\mathsf{M}_2(Q)^{\mathsf T}\mathsf{M}_2(Q)=N(Q)I_2 .
$$

So every member of the image is a **conformal normal matrix**, with both singular values equal to $\lvert Q\rvert$, and the image of the units is the orthogonal group:

$$
\mathsf{M}_2(\mathrm{U}(1))=SO(2).
$$

**The polar decomposition.** Since the matrix is conformal, its polar decomposition is the scalar-times-rotation factorisation

$$
\mathsf{M}_2(Q)=\lvert Q\rvert\, R_\theta,\qquad R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix},\qquad Q=\lvert Q\rvert e^{i\theta},
$$

and the two factors are the modulus and the unit of the algebra. So the polar decomposition of the algebra and the polar decomposition of the matrix are the same decomposition, read once in $\mathbb{C}$ and once in $M_2(\mathbb{R})$.

**The reflections.** The transpose realises the involution, so the anti-linear maps of the plane are the matrices $\mathsf{M}_2(Q)E$ with $E=\operatorname{diag}(1,-1)$,

$$
\mathsf{M}_2(u)E=\begin{pmatrix}\cos2\alpha&\sin2\alpha\\ \sin2\alpha&-\cos2\alpha\end{pmatrix},\qquad u=e^{2i\alpha},
$$

of determinant $-1$, trace $0$ and eigenvalues $\pm1$: these are the reflections, and the orthogonal group of the plane is $O(2)=\mathsf{M}_2(\mathrm{U}(1))\cup\mathsf{M}_2(\mathrm{U}(1))E$. The reflections are therefore **not** in the image, and the reason is the determinant: an anti-linear map has negative determinant, and the image has positive determinant everywhere except at the origin. This is the first appearance of the complement of the image, and it is the complement that the operators article identifies as the unreachable half of the ambient.

## The Norms

**Three forms.**

| form | definition | Gram matrix on $(1,i)$ | signature | multiplicative |
|---|---|---|---|---|
| determinant form | $\det\mathsf{M}_2(Q)=N$ | $I_2$ | $(2,0)$ | yes |
| trace form | $\operatorname{tr}(\mathsf{M}_2(Q)\mathsf{M}_2(P))$ | $\operatorname{diag}(2,-2)$ | $(1,1)$ | no |
| Frobenius form | $\operatorname{tr}(\mathsf{M}_2(Q)^{\mathsf T}\mathsf{M}_2(P))$ | $2I_2$ | $(2,0)$ | no |
| modulus | $\lvert Q\rvert=\sqrt{\det}$ | — | — | yes |

**The determinant is the Euclidean form.** The first row is the distinguishing feature of the category: the determinant is a positive definite quadratic form on the algebra, and it is the Euclidean form of the plane. The Frobenius form is twice it, and the equality $\mathsf{M}_2(Q)^{\mathsf T}\mathsf{M}_2(Q)=N I_2$ is the reason.

**The trace form is Lorentzian.** The second row is indefinite of signature $(1,1)$, with the real axis positive and the imaginary axis negative. It is the form under which the algebra is a Minkowski plane, and it is not equivalent to the determinant form: the two have different signatures and there is no linear change of coordinates taking one to the other. So $\mathbb{C}$ carries two inequivalent invariant forms, the Euclidean one of the norm and the Lorentzian one of the trace, and the model displays both as restrictions of forms of the ambient.

**The Frobenius form is the metric of the ambient.** On the image it is $2N$, so it is a positive definite form proportional to the determinant form; on the whole ambient it is the standard inner product $\operatorname{tr}(A^{\mathsf T}B)$, with respect to which the transpose is the adjoint.

**The absence.** There is no Hermitian form on the image other than through the complexification, because the model is real and its only involution is the transpose. The Hermitian/anti-Hermitian splitting of the complex models of the quaternion category has no counterpart; what replaces it is the symmetric/skew splitting of the next section, and the two coincide in effect, because for a conformal matrix the symmetric part is scalar and the skew part is imaginary.

## The Subspaces

**The tabulation.**

| subspace | algebra condition | matrix condition | dimension |
|---|---|---|---|
| real axis $\mathbb{R}_{\mathbb{C}}$ | $q'=0$ | $\mathsf{M}_2(Q)=qI_2$, scalar | $1$ |
| imaginary axis $i\mathbb{R}_{\mathbb{C}}$ | $q=0$ | $\mathsf{M}_2(Q)=q'J$, skew and traceless | $1$ |
| symmetric part | — | $\tfrac12(\mathsf{M}_2+\mathsf{M}_2^{\mathsf T})=qI_2$ | $1$ |
| skew part | $q=0$ | $\tfrac12(\mathsf{M}_2-\mathsf{M}_2^{\mathsf T})=q'J$ | $1$ |
| units | $N=1$ | $SO(2)$, and $\det=1$, $\operatorname{tr}=2\cos\theta$ | $1$ |
| the image | — | $MJ=JM$ | $2$ |
| the ambient | — | — | $4$ |

**The symmetric part is scalar.** For a conformal matrix,

$$
\tfrac12\bigl(\mathsf{M}_2(Q)+\mathsf{M}_2(Q)^{\mathsf T}\bigr)=qI_2,\qquad
\tfrac12\bigl(\mathsf{M}_2(Q)-\mathsf{M}_2(Q)^{\mathsf T}\bigr)=q'J,
$$

so the image splits as the direct sum of its symmetric part and its skew part, of dimensions one and one, and the two summands are the real and the imaginary axes. The splitting is orthogonal for both the trace form and the Frobenius form. In the quaternion models the same statement held with dimensions one and three; here it is one and one, and it is the whole of the image.

**The count.** The distinguished subspaces of the algebra are the fixed and anti-fixed spaces of its involutions, and the count is the count of the involution group. Here the group generated by the conjugation has two elements, and it produces the two subspaces $\mathbb{R}_{\mathbb{C}}$ and $i\mathbb{R}_{\mathbb{C}}$, of dimensions one each. The biquaternion algebra, whose involution group has four elements, produces six such subspaces. So the count is two against six, and it is the smallest count in the series.

**The units.** The unit circle is the model's only nonlinear distinguished set,

$$
\mathsf{M}_2(\mathrm{U}(1))=SO(2)=\{\mathsf{M}_2(Q):N(Q)=1\},
$$

of dimension one, and it is the level set of the determinant. The model realises $\mathrm{U}(1)\cong SO(2)$ as an equality of matrix sets, and the isomorphism of Lie groups is multiplicativity restricted to the level set. The reflections are the other component of $O(2)$ and they lie outside the image, as the previous section showed.

**The comparison with the ambient.** The two-dimensional image contains no nilpotent, no idempotent and no rank-one matrix; the four-dimensional ambient contains all three. The passage from the ambient to the algebraic structure is therefore the passage from an arbitrary linear map to a similarity, and the four entries of an arbitrary matrix are four parameters of which the algebra uses two.

## Summary

1. The Cayley matrix $\mathsf{M}_2(Q)=qI_2+q'J$ is the matrix of left multiplication by $Q$ in the basis $(1,i)$, and $\mathsf{M}_2(Q)\mathsf{M}_2(P)=\mathsf{M}_2(QP)$.
2. The image is the two-dimensional subalgebra of conformal matrices, characterised by $MJ=JM$, by the shape $qI_2+q'J$, and by being the real matrices of the complex-linear maps of the plane.
3. The left and right multiplications coincide, the centraliser of the image is the image, and the image is a maximal commutative subalgebra of $M_2(\mathbb{R})$.
4. The trace is $2q$, the traceless part is the imaginary line, and the trace form is the Minkowski form of signature $(1,1)$ with Gram $\operatorname{diag}(2,-2)$.
5. The determinant is the norm $q^{2}+q'^{2}$, positive definite, with zero set the single point $0$; the unit criterion is the same as the invertibility criterion and the same as the non-vanishing of the determinant.
6. There is no idempotent but $0$ and $I_2$, so there is no Peirce frame over $\mathbb{R}$; over $\mathbb{C}$ the frame exists, with the two idempotents $P_{\pm}=\tfrac12(I_2\mp iJ)$ and the two isotropic eigenlines.
7. The eigenvalues are $\lambda=q+iq'$ and $\bar\lambda$, the diagonalising matrix is the unitary $U$ of the second-order Fourier transform, and it is a rotation by $-45^{\circ}$ on the real plane.
8. The adjugate, the transpose and the Cayley matrix of the conjugate are one matrix, so $\mathsf{M}_2(Q)^{\mathsf T}\mathsf{M}_2(Q)=N I_2$; every member of the image is a conformal normal matrix, and the units are $SO(2)$.
9. The image carries the determinant form, positive definite, and the trace form, Lorentzian; the two are inequivalent, and there is no further invariant form.
10. The image splits as the scalar line plus the imaginary line, and the distinguished subspaces are two, against the six of the biquaternion algebra.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathsf{M}_2$ | the Cayley map $\mathbb{C}\to M_2(\mathbb{R})$ | this article |
| $J$ | $\mathsf{M}_2(i)=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, the complex structure | this article |
| $Q=q+iq'$ | a complex number, with conjugate $\bar Q$ | *Complex Algebra* |
| $N(Q)=q^{2}+q'^{2}$ | the norm, equal to $\det\mathsf{M}_2(Q)$ | *Complex Norm and Invertibility* |
| $\lambda=q+iq'$ | the eigenvalue of $\mathsf{M}_2(Q)$ on $v_+$ | *Eigenvalue Decomposition and Eigenbasis of a Complex Number* |
| $P_{\pm}=\tfrac12(I_2\mp iJ)$ | the two idempotents of the complexified algebra | this article |
| $U$ | the diagonalising matrix, a scaled second-order Fourier transform | this article |
| $R_\theta$ | the rotation matrix $\mathsf{M}_2(e^{i\theta})$ | *Rotations and Reflections in the Complex Plane* |
| $E=\operatorname{diag}(1,-1)$ | the matrix of conjugation; reflections are $\mathsf{M}_2(u)E$ | *The Versors and the Orthogonal Group of the Complex Numbers* |
| $\mathbb{R}_{\mathbb{C}},i\mathbb{R}_{\mathbb{C}}$ | the real and imaginary axes, imaged as the scalar and the skew lines | this article |
| $\mathrm{U}(1)$ | the unit circle, imaged as $SO(2)$ | *Complex Norm and Invertibility* |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the regular representation and the double centraliser theorem, whose degenerate case is the field.
- Frank B. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 1992), for the regular module over a division ring and the simplicity of the regular representation.
- Tristan Needham, *Visual Complex Analysis* (Oxford University Press, 1997), for the conformal reading of multiplication and the rotation structure of the plane.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the real representation of a complex matrix, the conformal matrices and the adjugate.
