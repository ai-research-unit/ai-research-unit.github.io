# __$M_4(\mathbb{R})_{\mathbb{H}_L}$ Axis-Free Representation__

## Introduction

**The model.** The quaternion algebra acts on itself by left multiplication, and in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ that action is a $4\times4$ real matrix. The map

$$
\mathsf{M}_4:\mathbb{H}\longrightarrow M_4(\mathbb{R}),\qquad
\mathsf{M}_4(\tilde q)=\text{the matrix of }\tilde q_3\mapsto\tilde q\tilde q_3
$$

is the **left regular representation**, and it is the second and last model of the quaternion category. It is of size four over $\mathbb{R}$, against the size two over $\mathbb{C}$ of the companion article. The article is named **axis-free** because the frame is the algebra's own basis and not a frame chosen from outside, which is the name the biquaternion article *$M_4(\mathbb{C})$ Axis-Free Representation* gives to the same basis; *regular* names the representation and *axis-free* names the frame.

**The two models are one representation.** The regular model is the realification of the Pauli model: the image $\mathsf{M}_2(\mathbb{H})\subset M_2(\mathbb{C})$ is a four-real-dimensional space of complex-linear maps, and forgetting the complex structure turns each of them into a $4\times4$ real matrix, which is exactly $\mathsf{M}_4(\tilde q)$. Two consequences follow and they are the spine of the article.

- The trace doubles: $\operatorname{tr}_\mathbb{R}=2\operatorname{Re}\operatorname{tr}_\mathbb{C}$, and $\operatorname{tr}_\mathbb{C}=2q_t$, so $\operatorname{tr}\mathsf{M}_4(\tilde q)=4q_t$.
- The determinant is a squared modulus: $\det_\mathbb{R}=\lvert\det_\mathbb{C}\rvert^{2}$, so $\det\mathsf{M}_4(\tilde q)=N(\tilde q)^{2}$ and not $N$.

So the discrepancy between the two models is not an accident of two conventions. It is the discrepancy between a complex determinant and the determinant of its realification, and it is the single numerical difference between the two pairs of the category.

**What the regular model buys.** Three things the complex model cannot give. The model is a **real** algebra homomorphism, so its image is a genuine subalgebra of a real matrix algebra and no complex scalar is needed anywhere. The frame is the algebra's own basis, so the matrix entries are the structure constants of the multiplication table and the model is a dictionary rather than an embedding into a space of a different kind. And the two-sided structure becomes visible inside one ambient: the left and the right multiplication are two commuting four-dimensional families in the same $M_4(\mathbb{R})$, related by a signed transpose.

**What it costs.** The determinant is no longer the norm but its square, so the model cannot read the norm off a determinant without a square root. The determinant is also positive on every nonzero element, so it cannot distinguish $\tilde q$ from $-\tilde q$: the two have the same determinant and opposite traces, and the sign of an element is read by the trace alone. There is also no complex scalar in the model, so the Hermitian theory of the companion article has no canonical counterpart here; what replaces it is the transpose, which is an involution of the image and not an anti-linear map.

**Boundaries.** The algebra is *Quaternion Algebra*; the norm is *Norm and Invertibility in the Quaternion Algebra*; the spectrum is *Spectral Regularity and Degeneracy in the Quaternion Algebra*; the abstract operators are *The One-Sided Operators* and *Two-Sided Operators* on the quaternion algebra, which this article does not replace. The companion model is *$M_2(\mathbb{C})_{\mathbb{H}}$ Pauli Representation*, and the operators of this model are *$M_4(\mathbb{R})_{\mathbb{H}_L}$ Axis-Free Representation : Operators*. The biquaternion counterpart is *$M_4(\mathbb{C})$ Axis-Free Representation*, whose two displays are the same arrays over $\mathbb{C}$: this model is their real slice, §*The Real Slice of the Biquaternion Display*.

**Conventions.** The basis is $(e_t,\vec e_x,\vec e_y,\vec e_z)$ with $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ cyclically. The element is $\tilde q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, its conjugate is $\tilde q^{*}=q_te_t-\vec v$, and its norm is $N(\tilde q)=q_t^{2}+q_x^{2}+q_y^{2}+q_z^{2}$. The left and right multiplications are $L_{\tilde q},R_{\tilde q}$, and $\mathsf{M}_4$ is the matrix of $L_{\tilde q}$. The sign matrix is $D=\operatorname{diag}(1,-1,-1,-1)$.

## The Frame

**Definition.** The **Cayley matrix** of $\tilde q$ is the matrix whose $\mu$-th column is the coordinate column of $\tilde q\,\tilde e_\mu$:

$$
\mathsf{M}_4(\tilde q)=\bigl(\ \tilde q e_t\ \big|\ \tilde q\vec e_x\ \big|\ \tilde q\vec e_y\ \big|\ \tilde q\vec e_z\ \bigr)
=\begin{pmatrix}
q_t&-q_x&-q_y&-q_z\\
q_x&q_t&-q_z&q_y\\
q_y&q_z&q_t&-q_x\\
q_z&-q_y&q_x&q_t
\end{pmatrix}.
$$

**The reading of the display.** The first column is $\tilde q$ itself, so the map is injective by inspection: the element is recovered from the first column. The matrix is of the shape

$$
\mathsf{M}_4(\tilde q)=q_tI_4+q_xA_1+q_yA_2+q_zA_3,
$$

with the three matrices

$$
A_1=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\quad
A_2=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\quad
A_3=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix},
$$

which are antisymmetric and satisfy $A_1^{2}=A_2^{2}=A_3^{2}=-I_4$ and $A_1A_2=A_3$ cyclically. So the three generators behave as the imaginary units, and the four matrices $I_4,A_1,A_2,A_3$ span a four-dimensional subalgebra of the ambient.

**The entries are the structure constants.** Write the product as $e_\mu e_\nu=\sum_\rho\varepsilon_{\mu\nu}^{\ \ \rho}e_\rho$, with $\varepsilon_{\mu\nu}^{\ \ \rho}\in\{0,+1,-1\}$. Then the $\nu$-th column of $\mathsf{M}_4(e_\mu)$ is the array $\varepsilon_{\mu\nu}^{\ \ \cdot}$, so the sixteen displays of the units are the multiplication table read by columns, and no entry is rescaled or rotated. The display above is the same table read with the four weights $q_\mu$: its $\nu$-th column is the coordinate column of the product $\tilde q e_\nu$.

**What the frame makes simple.** The five properties that the real coefficients leave of the biquaternion list (*$M_4(\mathbb{C})$ Axis-Free Representation*, §*What the Axis-Free Family Makes Simple*) hold here in the same words.

- The four unit matrices $I_4,A_1,A_2,A_3$ and, more, all sixteen products $L_{e_\mu}R_{e_\nu}$ of §*The Left and the Right Matrices* are **signed permutations**: exactly one nonzero entry in each row and each column, of modulus one.
- Each is **orthogonal**, $M^{\mathsf T}M=I_4$, and of determinant one, so the eight matrices $\pm I_4,\pm A_1,\pm A_2,\pm A_3$ are exactly the quaternion group $Q_8$ acting on $\mathbb{R}^4$ by signed permutations, one finite subgroup of the image of the unit sphere $\mathrm{Sp}(1)$.
- The **transpose is the conjugation**, $\mathsf{M}_4(\tilde q)^{\mathsf T}=\mathsf{M}_4(\tilde q^{*})$; the proof is the sparsity of the display, since a signed permutation matrix is orthogonal and its inverse is the matrix of the inverse element.
- The **stitch is real and diagonal**, $R_{\tilde q}=D\mathsf{M}_4(\tilde q)^{\mathsf T}D$ with $D=\operatorname{diag}(1,-1,-1,-1)$.
- The **three directions are cyclically symmetric**: a cyclic permutation $x\mapsto y\mapsto z\mapsto x$ conjugates every matrix by a permutation matrix, so no vector direction is privileged by the frame.

The last is the one that makes the first four cheap: a signed permutation matrix is orthogonal, its inverse is its transpose, and both facts are visible from the table without a computation. The transpose identity is the special case in which the inverse of the matrix of $e_\mu$ is the matrix of $e_\mu^{-1}=e_\mu^{*}$, extended to the whole image by linearity.

**The two meanings of $D$.** The matrix $D$ is not a bookkeeping device. It is the Gram matrix of the bilinear form $\beta(X,Y)=\operatorname{Sc}(XY)$ on the four units, since $\operatorname{Sc}(e_\mu e_\nu)=\delta_{\mu\nu}$ on the scalar and $-\delta_{\mu\nu}$ on the three vectors; and it is the matrix of the conjugation of the carrier in the same basis, since $\tilde q^{*}$ has coordinates $(q_t,-q_x,-q_y,-q_z)$. The stitch of §*The Left and the Right Matrices* is the statement that these two readings of one matrix are the same.

**The left and the right frames.** Two different bases of the ambient are in play and they must not be confused.

- The **Cayley frame** is the basis of the ambient as a space of operators, in which a matrix is written: the sixteen matrix units $E_{ij}$, or equivalently the entries of the display above.
- The **axis-free frame** is the basis of the carrier, $(e_t,\vec e_x,\vec e_y,\vec e_z)$, in which a matrix acts. It is the frame the columns are indexed by, it is the coefficient basis of *Matrix Representations Conventions*, and it is the frame the biquaternion article calls by the same name.

The two frames coincide in size but not in meaning, and the whole article is written with the second in the carrier and the first in the ambient. The operators article turns on the same distinction.

**Theorem (the model is unique up to conjugacy).** Every faithful real representation of the algebra by $4\times4$ matrices is equivalent to the regular one: if $\rho$ and $\rho'$ are two such, there is $P\in GL_4(\mathbb{R})$ with $\rho'(\tilde q)=P\rho(\tilde q)P^{-1}$ for all $\tilde q$.

**Proof.** A representation is determined by the images of $\vec e_x,\vec e_y,\vec e_z$, which generate a four-dimensional subalgebra of $M_4(\mathbb{R})$ isomorphic to $\mathbb{H}$. A four-dimensional real representation of a central simple algebra is a direct sum of copies of the unique irreducible one, so the two images are isomorphic as modules over the algebra, and an isomorphism of modules is the required change of basis.
So the regular model is not one choice among many: it is the only faithful real model of the minimal degree, and the minimal degree is four.

## The Left and the Right Matrices

**The left family.** $\mathsf{M}_4(\tilde q)$ **is** $L_{\tilde q}$, and the family

$$
L(\mathbb{H})=\{\mathsf{M}_4(\tilde q):\tilde q\in\mathbb{H}\}
$$

is a four-dimensional subalgebra of $M_4(\mathbb{R})$, closed under products and containing the identity. Every nonzero member is invertible, so $L(\mathbb{H})\setminus\{0\}\subset GL_4(\mathbb{R})$.

**The right family.** Right multiplication is the matrix of $\tilde q_3\mapsto\tilde q_3\tilde q$, and it is a second four-dimensional family

$$
R(\mathbb{H})=\{R_{\tilde q}\},
$$

which is also a subalgebra but is **not** the transpose of the first.

**The stitch.** With $D=\operatorname{diag}(1,-1,-1,-1)$,

$$
R_{\tilde q}=D\,\mathsf{M}_4(\tilde q)^{\mathsf T}D .
$$

**Proof.** The entry rule of the stitch is $\bigl(D\mathsf{M}_4(\tilde q)^{\mathsf T}D\bigr)_{\mu\nu}=s_\mu s_\nu\,\mathsf{M}_4(\tilde q)_{\nu\mu}$, with $s_t=+1$ and $s_k=-1$, so the two sides agree entry by entry exactly when

$$
R_{\mu\nu}=s_\mu s_\nu L_{\nu\mu},\qquad \mu,\nu\in\{t,x,y,z\},
$$

where $L_{\mu\nu}$ is the coefficient of $e_\mu$ in $\tilde q e_\nu$ and $R_{\mu\nu}$ the coefficient of $e_\mu$ in $e_\nu\tilde q$. For an element $X=\sum_\mu x_\mu e_\mu$ the coordinate is recovered from the scalar part by $x_\mu=s_\mu\operatorname{Sc}(e_\mu X)$, since $\operatorname{Sc}(e_\mu^{2})=s_\mu$. Applying this to $X=e_\nu\tilde q$ and using $\operatorname{Sc}(e_\mu e_\nu\tilde q)=\operatorname{Sc}(e_\nu\tilde q e_\mu)$,
$$
R_{\mu\nu}=s_\mu\operatorname{Sc}(e_\mu e_\nu\tilde q)
=s_\mu\operatorname{Sc}(e_\nu\tilde q e_\mu)
=s_\mu s_\nu L_{\nu\mu},
$$
the last step being the same coordinate formula applied to $X=\tilde q e_\mu$.

**The transpose is the conjugation.** The stitch has a companion, and it is the one the article uses more often:

$$
\mathsf{M}_4(\tilde q)^{\mathsf T}=\mathsf{M}_4(\tilde q^{*}),
\qquad\text{equivalently}\qquad
\mathsf{M}_4(\tilde q)^{\mathsf T}=D\,R_{\tilde q}\,D .
$$

**Proof.** Transposing the stitch gives $\mathsf{M}_4(\tilde q)^{\mathsf T}=D R_{\tilde q}D$, and the product $\tilde q_3\tilde q$ has scalar part $\langle\tilde q_3,\tilde q\rangle$ and vector part $q_t\vec v_3+q_{3,t}\vec v+\vec v_3\times\vec v$, whose cross term has the opposite sign to that of $\tilde q\tilde q_3$; so $D R_{\tilde q}D$ is left multiplication by $q_te_t-\vec v$.

The two statements are the regular form of the complex relation $R_{\tilde q}=C L_{\tilde q^{*}}C$, with the conjugate transpose replaced by the signed transpose, and they say the same thing in two languages: an anti-linear involution on the one hand, a signature matrix on the other.

**Three operations, one matrix.** The arrays obtained from $\mathsf{M}_4(\tilde q)$ by the transpose and by the two conjugations by $D$ are not equal, and it is worth naming which belongs where.

| | value | family |
|---|---|---|
| the transpose | $\mathsf{M}_4(\tilde q)^{\mathsf T}=\mathsf{M}_4(\tilde q^{*})$ | the left family, at the conjugate |
| the signed transpose | $D\mathsf{M}_4(\tilde q)^{\mathsf T}D=R_{\tilde q}$ | the right family, at the same element |
| conjugation by $D$ | $D\mathsf{M}_4(\tilde q)D=R_{\tilde q^{*}}$ | the right family, at the conjugate |

So the transpose is an involution **of the image**, and the two operations that carry $D$ carry the left family onto the right one. Nothing here is a failure of closure: the image is closed under the transpose, and it is the passage to the other family that the two $D$'s perform.

**The two copies.** They commute, because associativity gives $\tilde q_1(\tilde q_3\tilde q_2)=(\tilde q_1\tilde q_3)\tilde q_2$; their intersection is the scalar line,

$$
L(\mathbb{H})\cap R(\mathbb{H})=\mathbb{R}\,I_4 ,
$$

and their sum has dimension $4+4-1=7$. The double centraliser theorem holds in the sharpest form:

**Theorem (the double centraliser).** The centraliser of $L(\mathbb{H})$ in $M_4(\mathbb{R})$ is $R(\mathbb{H})$, and the centraliser of $R(\mathbb{H})$ is $L(\mathbb{H})$.

**Proof.** A matrix $X$ commuting with every $L_{\tilde q}$ is determined by its first column $Xe_t$, since $X\tilde q=XL_{\tilde q}e_t=L_{\tilde q}Xe_t=\tilde q\,(Xe_t)$; so $X=R_{Xe_t}$ and the centraliser is contained in $R(\mathbb{H})$, with the other inclusion by commutation. The dimension count gives equality, and the argument is symmetric.

**The invariants.** For a nonzero element,

$$
\operatorname{rank}\mathsf{M}_4(\tilde q)=4,\qquad
\operatorname{tr}\mathsf{M}_4(\tilde q)=4q_t,\qquad
\det\mathsf{M}_4(\tilde q)=N(\tilde q)^{2},\qquad
\langle\mathsf{M}_4(\tilde q)\rangle_*=4N(\tilde q).
$$

The Frobenius norm is computed from the display: the four columns are the images of the four units, they are orthogonal, and each is of squared length $N$, because $\lvert\tilde q\tilde x\rvert^{2}=N(\tilde q)N(\tilde x)$ and $\operatorname{Sc}(\tilde e_\mu^{*}\tilde e_\nu)=\delta_{\mu\nu}$. So $\operatorname{tr}(M^{\mathsf T}M)=4N$, and $\operatorname{tr}(M^{2})=4P$ by the same reading of the diagonal of $M^{2}$. Both are used in §*The Four Brackets*.

## The Product

**Theorem (multiplicativity).** For all $\tilde q,\tilde p$,

$$
\mathsf{M}_4(\tilde q)\mathsf{M}_4(\tilde p)=\mathsf{M}_4(\tilde q\tilde p).
$$

**Proof.** The matrix of a composition is the product of the matrices, and $L_{\tilde q}\circ L_{\tilde p}=L_{\tilde q\tilde p}$ because $\tilde q(\tilde p\tilde q_3)=(\tilde q\tilde p)\tilde q_3$. Associativity of the algebra is the single fact behind it.

**The reading.** This is the cleanest multiplicativity in the whole of Part VI: the model is the algebra acting on itself, so the multiplication of the algebra and the multiplication of the matrices are the same operation seen twice. In the split-quaternion category the same was true because the algebra was a matrix algebra; here it is true because the representation is regular. The two reasons are different and both are exact.

**The image.** The image is a four-dimensional subalgebra of the sixteen-dimensional ambient, and it is not an ideal: $M_4(\mathbb{R})$ is simple and the image is proper. The ambient is therefore much larger than the model, and the excess is where the operator layer of the companion article lives.

**The failure of complex scalar closure has no counterpart.** Here the scalars are real, so the image is closed under the scalar multiplication of the ambient, and there is no analogue of the failure noted in the complex model. Nothing fails in its place: the image is closed under the transpose as well, since $\mathsf{M}_4(\tilde q)^{\mathsf T}=\mathsf{M}_4(\tilde q^{*})$ by the transpose identity of §*The Left and the Right Matrices*. What the transpose is not is an operation of one family alone — it exchanges the two, $D\mathsf{M}_4(\tilde q)^{\mathsf T}D=R_{\tilde q}$, and that exchange is the content of the double centraliser and not a defect. The contrast with the complex model is therefore sharper than a failure: there the involution of the ambient was anti-linear and preserved the image, and here it is linear and preserves the image too, so the two models agree on this point and differ only in which involution of the ambient implements it.

## The Trace

**Theorem (the trace).** For every element,

$$
\operatorname{tr}\mathsf{M}_4(\tilde q)=4q_t .
$$

**Proof.** From the display, the four diagonal entries are $q_t$ four times.

**The scalar part.** It is recovered as $\tfrac14\operatorname{tr}$, and it vanishes on the pure quaternions. So the pure part is the trace-zero subspace of the image:

$$
\mathsf{M}_4(V)=\{\mathsf{M}_4(\tilde q):\operatorname{tr}\mathsf{M}_4(\tilde q)=0\},
$$

of dimension three. The trace splits the image into the scalar line and the traceless copy of the pure part, exactly as in the complex model, and with the same three-dimensional traceless piece.

**The factor of two.** The trace is twice the trace of the complex model. That is the general rule $\operatorname{tr}_\mathbb{R}(A)=\operatorname{Re}\operatorname{tr}_\mathbb{C}(A)+\operatorname{Re}\operatorname{tr}_\mathbb{C}(\overline{A})=2\operatorname{Re}\operatorname{tr}_\mathbb{C}(A)$ for the realification of a complex matrix, and it is the reason the two models cannot be compared entrywise. The trace of the regular model is not a different functional; it is the same one with the real dimension counted twice.

**The trace form.** On the image,

$$
\operatorname{tr}\bigl(\mathsf{M}_4(\tilde e_\mu)\mathsf{M}_4(\tilde e_\nu)\bigr)=\operatorname{diag}(4,-4,-4,-4),
$$

of signature $(1,3)$; the computation is the same as in the complex model, with every entry doubled, because the real trace doubles. So the trace form is again the Minkowski form of signature $(1,3)$, positive on the scalar part and negative on the pure part, and the factor $4$ against $2$ is the only change.

**What the trace does not see.** The trace is blind to the three vector coordinates: it records $q_t$ and nothing else, so $e_t+2\vec e_x$ and $e_t-3\vec e_y$ have the same trace and different norms, and the trace separates an element from its conjugate not at all. It is also blind to the sign that the determinant loses, since $\pm\tilde q$ have traces $\pm4q_t$ and equal determinants, so the pair $(\operatorname{tr},\det)$ determines the element up to nothing at all: two elements with the same trace and the same norm differ only in the direction of the vector part.

**Two invariants, one function.** The trace is a coordinate and the determinant is the square of the norm, so of the two classical invariants only the second is multiplicative. The trace is the one that carries the sign, the determinant is the one that carries the length, and the element is determined by neither alone: the sphere of radius $\sqrt N$ and the hyperplane $q_t=\operatorname{tr}/4$ meet in a two-sphere.

## The Determinant

**Theorem (the determinant is the square of the norm).** For every element,

$$
\det\mathsf{M}_4(\tilde q)=N(\tilde q)^{2}=\bigl(q_t^{2}+q_x^{2}+q_y^{2}+q_z^{2}\bigr)^{2}.
$$

**Proof.** Two proofs, and both are worth recording.

*By the realification.* $\mathsf{M}_4(\tilde q)$ is the real matrix of the complex-linear map $\mathsf{M}_2(\tilde q)$ acting on $\mathbb{C}^{2}$ read as $\mathbb{R}^{4}$; for a realification, $\det_\mathbb{R}=\lvert\det_\mathbb{C}\rvert^{2}$, and $\det_\mathbb{C}\mathsf{M}_2(\tilde q)=N$.

*By the eigenvalues.* The characteristic polynomial, computed below, is $(\lambda^{2}-2q_t\lambda+N)^{2}$, whose constant term is $N^{2}$ and is the determinant in dimension four.

**Why the square.** The determinant of a real matrix that happens to preserve a complex structure is the squared modulus of the complex determinant, because the complex structure pairs every eigenvalue with its conjugate. Here every eigenvalue of $\mathsf{M}_2$ is non-real unless the element is scalar, so every eigenvalue of $\mathsf{M}_4$ occurs twice, and the determinant is the square of the product of one representative of each pair. The square is therefore structural and not conventional: it is the arithmetic signature of the realification.

**The consequences.**

- The determinant is the fourth power of the modulus, $\det\mathsf{M}_4(\tilde q)=\lvert\tilde q\rvert^{4}$ with $\lvert\tilde q\rvert=\sqrt N$, so it is positive on every nonzero element, it equals $1$ on the unit sphere, and the model cannot distinguish $\tilde q$ from $-\tilde q$ by the determinant.
- The zero set is a point, so there is no null cone; the rank is four on every nonzero element and zero at the origin.
- The image of the unit sphere lies in $SL_4(\mathbb{R})$; the image of the whole algebra minus the origin lies in $GL_4^{+}(\mathbb{R})$, the component of the identity. This is the topological statement that the group of invertibles of the algebra is connected, which is true here and false in the split-quaternion category.
- The model is **conformal**, as the complex one was and for the same reason: $\mathsf{M}_4(\tilde q)^{\mathsf T}\mathsf{M}_4(\tilde q)=N I_4$, so the four singular values are $\sqrt N$ each. What differs is the reading. In the complex model $N$ was itself the determinant; here the determinant of $\mathsf{M}_4(\tilde q)$ is $N^{2}$, which is the determinant of $NI_4$ and therefore the fourth power of the common singular value.

**The unit criterion.** An element is invertible exactly when $N\neq0$, exactly when the determinant is nonzero, exactly when the matrix is invertible. So the three criteria of the algebra, of the norm and of the matrix coincide, and the model is faithful in the strongest sense: it detects invertibility.

## The Spectral Projectors

**The characteristic polynomial.** From the display, and from the realification,

$$
\chi(\lambda)=\bigl(\lambda^{2}-2q_t\lambda+N\bigr)^{2}
=\bigl((\lambda-q_t)^{2}+\lVert\vec v\rVert^{2}\bigr)^{2}.
$$

**The eigenvalues.** The roots are $q_t\pm i\lVert\vec v\rVert$, each with multiplicity two. Over $\mathbb{R}$ there are no eigenvalues at all unless the element is scalar; the model is therefore a real matrix with no real spectrum in general, which is the expected behaviour of a complex structure.

**The two invariant planes.** The multiplicity two is not a degeneracy: it is the complex dimension one of each eigenspace of the complex model, read as real dimension two. Concretely the carrier splits as a direct sum of two real planes on which $\mathsf{M}_4(\tilde q)$ acts by the same rotation-scaling block

$$
C=\begin{pmatrix}q_t&-\lVert\vec v\rVert\\ \lVert\vec v\rVert&q_t\end{pmatrix},
$$

and the matrix is similar over $\mathbb{R}$ to $\operatorname{diag}(C,C)$. The two planes are the two copies of $\mathbb{C}$ that the realification creates, and the complex structure $J$ of the carrier exchanges them.

**The displaying case.** For $\tilde q=e_t+\vec e_x$, the block structure is visible in the basis itself:

$$
\mathsf{M}_4(e_t+\vec e_x)=\begin{pmatrix}1&-1&0&0\\1&1&0&0\\0&0&1&-1\\0&0&1&1\end{pmatrix},
$$

the two identical blocks acting on $\operatorname{span}\{e_t,\vec e_x\}$ and on $\operatorname{span}\{\vec e_y,\vec e_z\}$. The first plane is the complex line of $\vec e_x$ and the second is its complement, and the equality of the two blocks is the statement that left multiplication by an element of a complex line acts identically on the line and on a complementary plane.

**The diagonalisation over $\mathbb{C}$.** Over $\mathbb{C}$ the matrix is diagonalisable, with diagonal form $\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$ where $\lambda_\pm=q_t\pm i\lVert\vec v\rVert$; the transition matrix is the matrix of the two complex eigenlines taken with their two real coordinates. So the model is diagonalisable over $\mathbb{C}$ for every element and never defective, and the whole of the spectral trichotomy of the split-quaternion category is absent: there is one spectral type, the elliptic one.

**The comparison.** The projectors of the companion model, $P_\pm=\tfrac12(I_2\mp i\mathsf{M}_2(u))$, are images of elements $\tfrac12(e_t\mp iu)$ of the complexified algebra, so they belong to the complexified image and not to the real form. Realified, each becomes a real projection of rank two on $\mathbb{R}^4$, of eigenvalues $1,1,0,0$; and it is not an element of the image $L(\mathbb{H})$, because no rank-two projection is, every nonzero member of the image being invertible. So the regular model displays the projectors of the complexified algebra but cannot contain them, and this is the exact sense in which the spectral theory of the algebra is a theory of the complexification.

## The Adjugate and the Inverse

**Theorem (the adjugate).** For every element,

$$
\operatorname{adj}\mathsf{M}_4(\tilde q)=N(\tilde q)\,\mathsf{M}_4(\tilde q^{*}),
$$

and therefore

$$
\mathsf{M}_4(\tilde q)^{-1}=\frac{\mathsf{M}_4(\tilde q^{*})}{N(\tilde q)}=\mathsf{M}_4\!\left(\frac{\tilde q^{*}}{N(\tilde q)}\right).
$$

**Proof.** The inverse is the left multiplication by $\tilde q^{-1}=\tilde q^{*}/N$, and the adjugate is the determinant times the inverse, with the determinant $N^{2}$.

**The contrast with the complex model.** There the adjugate was the conjugate transpose, which is an involution of the ambient; here it is $N$ times the left multiplication by the conjugate, which is again an element of the image. The two formulas are the two faces of the same fact: the inverse of a quaternion is its conjugate over its norm, and the model transports that formula either through the conjugate transpose or through the adjugate, depending on which ambient it is embedded in.

**Two formulas, two involutions.** The adjugate and the stitch must be kept apart. The adjugate stays inside the image and encodes the conjugation,

$$
\operatorname{adj}\mathsf{M}_4(\tilde q)=N(\tilde q)\,\mathsf{M}_4(\tilde q^{*}),
$$

while the transpose leaves the image and takes it to the right family,

$$
\mathsf{M}_4(\tilde q)^{\mathsf T}=D\,R_{\tilde q}\,D .
$$

So the conjugation is read by the adjugate and the reversal of the product by the transpose, and the two are not interchangeable: the first gives an element of $L(\mathbb{H})$, the second an element of $R(\mathbb{H})$.

**The normality.** Since $\mathsf{M}_4(\tilde q)^{\mathsf T}\mathsf{M}_4(\tilde q)=N I_4$, every matrix of the image is **normal and conformal**, with all singular values equal to $\sqrt N$. The image of the invertibles is therefore a four-dimensional submanifold of $SO(4)$:

$$
\mathsf{M}_4(\mathbb{H}^{\times})=\mathbb{R}_{>0}\cdot\mathsf{M}_4(SU(2)),
$$

and the compact part is a copy of $SU(2)$ inside $SO(4)$, acting on the carrier by left multiplication.

## The Norms

**Three forms, and one of them is the square of another.** The model carries the same three forms as the complex model, and the differences are the factor two on the trace and the square on the determinant.

| form | definition | Gram matrix on the four units | signature | multiplicative |
|---|---|---|---|---|
| determinant form | $\det\mathsf{M}_4(\tilde q)=N^{2}$ | — (quartic) | — | yes |
| norm form | $\sqrt{\det}=N$ | $I_4$ | $(4,0)$ | yes |
| trace form | $\operatorname{tr}(\mathsf{M}_4(\tilde q)\mathsf{M}_4(\tilde p))$ | $\operatorname{diag}(4,-4,-4,-4)$ | $(1,3)$ | no |
| Frobenius form | $\operatorname{tr}(\mathsf{M}_4(\tilde q)^{\mathsf T}\mathsf{M}_4(\tilde p))$ | $4I_4$ | $(4,0)$ | no |

**The determinant is not a quadratic form.** The single most important difference from the complex model: on the four real coordinates the determinant is a quartic, so the model does not carry the Euclidean form as a determinant. The Euclidean form is its square root, and the square root is the norm, which is not a polynomial in the matrix entries. This is why the regular model cannot be used to compute the norm by a determinant, and why the complex model is the one used for the spectral and polar theory.

**The trace form is the Lorentzian one.** It is of signature $(1,3)$ and invariant under the inner automorphisms, $\operatorname{tr}(gAg^{-1}gBg^{-1})=\operatorname{tr}(AB)$; it is the form under which the group of invertibles acts by isometries, and it is the same form as in the complex model up to the factor $4$ against $2$.

**The Frobenius form is the metric.** It is positive definite, equal to $4$ times the Euclidean form on the coordinates, and it is the inner product with respect to which the transpose is the adjoint. Its restriction to the image is $4N$, so the image is a conformal copy of $\mathbb{R}^{4}$ inside the ambient.

**The absence.** The model carries no **canonical** complex Hermitian form, because it carries no complex scalar. Complex structures are present — $\mathsf{M}_4(u)$ for a pure unit $u$ is an operator of square $-I_4$ in the image — and each of them determines a Hermitian form of its own on the carrier, but the frame singles out none of them, so no one of those forms is the Hermitian structure of the model. The Hermitian/anti-Hermitian splitting of the complex model is replaced here by the symmetric/antisymmetric splitting with respect to the transpose, of the next section: both are $1+3$, and they differ in the involution that defines them, the conjugate transpose there and the transpose here.

### The Four Brackets

**The table.** The four quadratic brackets of the corpus, read on the regular model with $M=\mathsf{M}_4(\tilde q)$:

| bracket | value | matrix formula | definite |
|---|---|---|---|
| Plain $P$ | $q_t^{2}-\lVert\vec v\rVert^{2}$ | $\tfrac14\operatorname{tr}(M^{2})$ | no |
| Quaternionic $N$ | $q_t^{2}+\lVert\vec v\rVert^{2}$ | $\sqrt{\det M}$ | yes |
| Hermitian $H$ | $q_t^{2}+\lVert\vec v\rVert^{2}$ | $\tfrac14\operatorname{tr}(M^{\dagger}M)$ | yes |
| Krein $K$ | $q_t^{2}-\lVert\vec v\rVert^{2}$ | $\tfrac14\operatorname{tr}(M^{\mathsf T}M^{\dagger})$ | no |

**The plain bracket.** The square of the display has trace $4(q_t^{2}-\lVert\vec v\rVert^{2})$: each of the two rotation-scaling blocks contributes $2(q_t^{2}-\lVert\vec v\rVert^{2})$ to the trace, because the trace of the square of a $2\times2$ block $\begin{pmatrix}q_t&-b\\ b&q_t\end{pmatrix}$ is $2(q_t^{2}-b^{2})$. The word is the same as in the complex model, closed by one trace, and the factor $\tfrac14$ replaces the $\tfrac12$ because the real dimension is twice the complex one.

**The collapse to two.** Over $\mathbb{R}$ the coefficients are real, so $\lvert q_\mu\rvert^{2}=q_\mu^{2}$ and the four brackets are two: $H=N$ and $K=P$, the matrix being real and $M^{\dagger}=M^{\mathsf T}$. What remains is the pair the article has already used, $N$ multiplicative and definite and $P$ indefinite of signature $(1,3)$. On this model the two survivors are the two traces already met, $\tfrac14\operatorname{tr}(M^{\mathsf T}M)=N$ and $\tfrac14\operatorname{tr}(M^{2})=P$, and the other two are the same two numbers under another name. The collapse is the same in the companion model; it is caused by the reality of the coefficients and not by the size of the matrix, and it is undone by passing to the biquaternion algebra, where the coefficients are complex and the four are distinct.

## The Subspaces

**The tabulation.** The distinguished subspaces of the algebra as matrix conditions in the regular model:

| subspace | algebra condition | matrix condition | dimension |
|---|---|---|---|
| scalar line | $\vec v=0$ | $\mathsf{M}_4(\tilde q)=q_tI_4$ | $1$ |
| pure part $V$ | $q_t=0$ | $\operatorname{tr}=0$ and $\mathsf{M}_4(\tilde q)^{\mathsf T}=-\mathsf{M}_4(\tilde q)$ | $3$ |
| complex line $L_x$ | $q_y=q_z=0$ | the matrix of the element $q_te_t+q_x\vec e_x$ | $2$ |
| complex line $L_y$ | $q_x=q_z=0$ | the matrix of $q_te_t+q_y\vec e_y$ | $2$ |
| complex line $L_z$ | $q_x=q_y=0$ | the matrix of $q_te_t+q_z\vec e_z$ | $2$ |
| symmetric part | — | $\tfrac12(\mathsf{M}_4+\mathsf{M}_4^{\mathsf T})=q_tI_4$ | $1$ |
| antisymmetric part | $q_t=0$ | $\tfrac12(\mathsf{M}_4-\mathsf{M}_4^{\mathsf T})=\mathsf{M}_4(\vec v)$ | $3$ |

**The symmetric part is scalar.** This is the exact analogue of the statement, in the complex model, that the Hermitian part of an element of the image is scalar. The decomposition is $1+3$ in both models, and in both it is the decomposition into the scalar line and the traceless part; what differs is the involution used to define it, the conjugate transpose there and the ordinary transpose here.

**Proof of the symmetric part.** A Cayley matrix is $q_tI_4$ plus an antisymmetric part, because the three generators $A_1,A_2,A_3$ are antisymmetric. Hence $\tfrac12(\mathsf{M}_4+\mathsf{M}_4^{\mathsf T})=q_tI_4$ and $\tfrac12(\mathsf{M}_4-\mathsf{M}_4^{\mathsf T})=\mathsf{M}_4(\vec v)$.

**The complex lines are not matrix subalgebras of the ambient.** The image of $L_x$ is a two-dimensional subspace of the ambient consisting of matrices commuting with $\mathsf{M}_4(\vec e_x)$; it is a subalgebra of the image, and hence a copy of $\mathbb{C}$, but it is not a subalgebra of $M_4(\mathbb{R})$ closed under transposition. The distinction matters for the operators article, where the complex lines index the strata of the length.

**The double centraliser, restated.** The subspace $L(\mathbb{H})$ and the subspace $R(\mathbb{H})$ are mutual centralisers, of dimension four each, meeting in the scalar line and spanning seven dimensions. So the image is the first of the two copies and the second copy is its centraliser, and the pair together is a seven-dimensional subspace of the ambient. This is the structural statement that the complex model could not make, because there the two copies were related by an anti-linear map and not by commutation inside one real ambient: there the pair spanned a space of operators on a different space.

## The Real Slice of the Biquaternion Display

**One array, two names.** *$M_4(\mathbb{C})$ Axis-Free Representation* displays the left family of the biquaternion algebra in the same basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ of $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ and calls the display $L_{\mathrm{axf}}$. Its array at $Q_\mu=q_\mu+0i$ is the array of this article, entry for entry, because the multiplication table is the same table and no complex number occurs in it. So the regular model of the quaternion algebra is the real slice of the axis-free display of the biquaternion algebra, and the two articles compute with one array under two names: *regular* names the representation, *axis-free* names what the frame does not do.

**Why nothing degrades.** The properties of §*The Frame* — entries in $\{0,\pm1\}$, signed permutations, transpose equal to conjugation, real diagonal stitch — are proved in the biquaternion article from the multiplication table alone (*$M_4(\mathbb{C})$ Axis-Free Representation*, §*What the Axis-Free Family Makes Simple*), and the table knows nothing about the coefficients. The real slice therefore keeps all of them, and the entries stay integers on the slice as they are off it. The three-direction symmetry, the quaternion group $Q_8$ and the uniqueness of the frame up to signs and permutations are likewise properties of the table, and they transfer without change.

**What the slice adds.** The coefficients are real, so the quaternionic bracket becomes a positive definite form, $N=\sum_\mu\lvert q_\mu\rvert^{2}=\sum_\mu q_\mu^{2}$, and the determinant becomes its square, positive on every nonzero element. Over $\mathbb{C}$ the same bracket is complex-valued and the determinant is the square of a complex number, so the real slice is the case in which the two models can be compared by inequalities and not only by identities. This is the gain that the companion model has over the biquaternion one, and it is the reason the quaternion category uses the $2\times2$ display for the spectral and polar theory and the $4\times4$ display for the operators.

**What is not on the slice.** The imaginary scalar. Over $\mathbb{C}$ the coefficient $Q_t=i$ is an element of the algebra and its image is $iI_4$, so the axis-free display of the biquaternion algebra is a complex subspace of $M_4(\mathbb{C})$ and carries a complex structure inside the image. Over $\mathbb{R}$ there is no imaginary coefficient, $iI_4$ is not in the image, and the ambient is real; the symmetry that replaces it is the transpose, of §*The Left and the Right Matrices*. Everything else in the biquaternion display — the two families, the stitch, the structure constants, the group — survives the restriction verbatim.

**The comparison with the complex case.**

| | $M_2(\mathbb{C})_{\mathbb{H}}$ | $M_4(\mathbb{R})_{\mathbb{H}_L}$ |
|---|---|---|
| size | $2$ over $\mathbb{C}$ | $4$ over $\mathbb{R}$ |
| trace | $2q_t$ | $4q_t$ |
| determinant | $N$ | $N^{2}$ |
| Euclidean form | the determinant | the square root of the determinant |
| the involution of the image | the conjugate transpose | the transpose |
| the symmetric/Hermitian part | scalar, via the conjugate transpose | scalar, via the transpose |
| the two-sided structure | two families exchanged by an anti-linear map | two families exchanged by the linear matrix $D$ |
| the four brackets | four, the coefficients being complex | two, $H=N$ and $K=P$ |
| the spectral projectors | images of the complexified algebra | outside the image |
| the coefficients | complex, so $iI_2$ is in the image | real, so $iI_4$ is not |

Two models, one representation, and the table is the complete dictionary between them. The determinants differ by a square and the traces by a factor two. The involutions differ in that one is anti-linear and one is linear, and both preserve the image, which is why the transpose plays on the right the role the conjugate transpose plays on the left. The brackets differ in number because the coefficients differ in field. Nothing else differs.

## Summary

1. The regular representation $\mathsf{M}_4$ is the matrix of left multiplication in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, and the Cayley matrix is displayed entrywise.
2. It is the minimal faithful real model, and it is the realification of the Pauli model; that single fact explains the factor two on the trace and the square on the determinant.
3. Multiplicativity is associativity, and the image is a four-dimensional subalgebra of $M_4(\mathbb{R})$.
4. The trace is $4q_t$, the pure part is the trace-zero subspace, and the trace form has signature $(1,3)$ with Gram $\operatorname{diag}(4,-4,-4,-4)$.
5. The determinant is $N^{2}$, the fourth power of the modulus, positive on all nonzero elements, with no null cone; the model detects invertibility exactly.
6. The characteristic polynomial is $(\lambda^{2}-2q_t\lambda+N)^{2}$, the eigenvalues are $q_t\pm i\lVert\vec v\rVert$ each twice, and the matrix is similar to two identical rotation-scaling blocks.
7. The adjugate is $N\mathsf{M}_4(\tilde q^{*})$, the inverse is $\mathsf{M}_4(\tilde q^{*})/N$, and every member of the image is conformal normal with singular values $\sqrt N$ four times.
8. The right multiplication is the signed transpose of the left one, $R_{\tilde q}=D\mathsf{M}_4(\tilde q)^{\mathsf T}D$, and the two families are mutual centralisers meeting in the scalars.
9. The symmetric part of a Cayley matrix is scalar and the antisymmetric part is the pure part, which is the regular form of the Hermitian/anti-Hermitian splitting of the complex model.
10. The transpose is the conjugation, $\mathsf{M}_4(\tilde q)^{\mathsf T}=\mathsf{M}_4(\tilde q^{*})$, and it preserves the image; conjugation by $D$ and the signed transpose carry the left family onto the right one, at the conjugate and at the element respectively.
11. The two models are one representation read twice; the table of the last section is the complete dictionary between them, and the display is the real slice of the axis-free display of the biquaternion algebra.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathsf{M}_4$ | the left regular, that is the axis-free, representation $\mathbb{H}\to M_4(\mathbb{R})$ | this article |
| $L_{\tilde q}$ | left multiplication, equal to $\mathsf{M}_4(\tilde q)$ | this article |
| $R_{\tilde q}$ | right multiplication, equal to $D\mathsf{M}_4(\tilde q)^{\mathsf T}D$ | this article |
| $D$ | the sign matrix $\operatorname{diag}(1,-1,-1,-1)$, the Gram matrix of $\beta(X,Y)=\operatorname{Sc}(XY)$ and the matrix of the conjugation | this article |
| $A_1,A_2,A_3$ | the Cayley matrices of $\vec e_x,\vec e_y,\vec e_z$ | this article |
| $N$ | the norm, equal to $\sqrt{\det\mathsf{M}_4(\tilde q)}$ | *Norm and Invertibility in the Quaternion Algebra* |
| $\lVert\vec v\rVert$ | the modulus of the pure part | *Quaternion Algebra* |
| $C$ | the rotation-scaling block $\begin{pmatrix}q_t&-\lVert\vec v\rVert\\ \lVert\vec v\rVert&q_t\end{pmatrix}$ | this article |
| $SU(2)$ | the invertibles of norm one, whose image lies in $SO(4)$ | *The Pin and Spin Groups of the Quaternion Algebra* |
| $V$ | the pure part, the trace-zero subspace of the image | this article |

## Further Reading

- Arthur Albert, *Structure of Algebras* (American Mathematical Society, 1939), for the regular representation of a central simple algebra and its minimal faithful degree.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the Cayley matrix of a quaternion and the two-sided action of $\mathbb{H}$.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the double centraliser theorem and its use in the structure theory.
- Fuzhen Zhang, *Matrix Theory* (Springer, 2011), for the realification of a complex matrix, the identities $\operatorname{tr}_\mathbb{R}=2\operatorname{Re}\operatorname{tr}_\mathbb{C}$ and $\det_\mathbb{R}=\lvert\det_\mathbb{C}\rvert^{2}$, and the real Jordan form.
