# __$M_2(\mathbb{C})_{\mathbb{H}}$ Pauli Representation__

## Introduction

**The model.** The quaternion algebra embeds in the $2\times2$ complex matrices as the four-real-dimensional subspace

$$
\mathsf{M}_2(\mathbb{H})=\left\{\begin{pmatrix}a&b\\-\overline{b}&\overline{a}\end{pmatrix}:a,b\in\mathbb{C}\right\},
$$

and the embedding is multiplicative. This article is the complex model of the quaternion category: the model of size two over $\mathbb{C}$, distinguished from its companion pair $M_4(\mathbb{R})_{\mathbb{H}_L}$, of size four over $\mathbb{R}$.

**Why the complex field is unavoidable.** There is no faithful $2\times2$ real model. A faithful real representation of degree two would embed a four-dimensional algebra into a four-dimensional algebra and hence be an isomorphism, and $M_2(\mathbb{R})$ has zero divisors while $\mathbb{H}$ does not. So the quaternion category is the first in Part VI where the model needs a larger scalar field, and the price is that the model is an embedding and not an isomorphism: the image has real dimension four inside the eight real dimensions of $M_2(\mathbb{C})$.

**What the embedding costs and what it buys.** It costs surjectivity, and with it the free ride of the split-quaternion category, where every matrix statement was a statement about the algebra. Here the image is a proper subspace, so each statement below has to be checked to stay inside it: multiplicativity, the adjugate, the inverse and the two-sided structure all do, and the spectral projectors do not — they are images of the complexified algebra and are named as such in §*The Spectral Projectors*. It buys three things the split case does not have. The determinant is positive definite, so there is no null cone and every nonzero element is a unit. The projectors are Hermitian, so the spectral theorem applies to the complexification and the eigenlines are orthogonal. And the eigenvalues are always a conjugate pair, so every element is diagonalisable over $\mathbb{C}$ and never defective.

**One contrast to keep in view.** In the split-quaternion algebra an idempotent exists over $\mathbb{R}$, because a pure vector can have square $+e_t$. In the quaternion algebra no pure vector has square $+e_t$, so the algebra has no nontrivial idempotent at all; the idempotents appear only in the complexified algebra, and they are the images of $\tfrac12(e_t\pm iu)$ with $u$ a pure unit quaternion, whose square is $+e_t$ because the extra scalar $i$ is available. This single difference governs the spectral section.

**Boundaries.** The algebra and its multiplication table are *Quaternion Algebra*; the conjugation, the norm and invertibility are *Quaternion Norm and Invertibility* and *The Quaternion Conjugation and the Involutions*; the spectrum is *Spectral Theory of the Quaternions*; the modules are *Quaternion Linear Representations*, which cite this article for the module of the model. The regular model, of size four over $\mathbb{R}$, is *$M_4(\mathbb{R})_{\mathbb{H}_L}$ Axis-Free Representation*. The operators of this model are the companion article *$M_2(\mathbb{C})_{\mathbb{H}}$ Pauli Representation : Operators*. The biquaternion counterpart is *$M_2(\mathbb{C})$ Pauli Representation*, whose display is the same array over $\mathbb{C}$; this model is its real slice, §*The Real Slice of the Biquaternion Display*.

**Conventions.** The basis of the algebra is $(e_t,\vec e_x,\vec e_y,\vec e_z)$ with

$$
\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t,\qquad
\vec e_x\vec e_y=\vec e_z,\quad \vec e_y\vec e_z=\vec e_x,\quad \vec e_z\vec e_x=\vec e_y,
$$

and the reversed products opposite. An element is $\tilde q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$; its scalar part is $q_t$, its pure part is $\vec v=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, its conjugate is $\tilde q^{*}=q_te_t-\vec v$, and its norm is

$$
N(\tilde q)=\tilde q\tilde q^{*}=q_t^2+q_x^2+q_y^2+q_z^2 .
$$

The scalar imaginary of the model is written $i$, so that $i^2=-1$ and $i$ commutes with the image; it is not an element of the algebra and must not be confused with $\vec e_z$, whose square is also $-e_t$. The conjugate transpose of a matrix is written $A^{\dagger}$, and the star ${}^{*}$ is kept for the conjugation of the algebra, so that $\mathsf{M}_2(\tilde q)^{\dagger}=\mathsf{M}_2(\tilde q^{*})$. The trace is $\operatorname{tr}$, the determinant is $\det$.

## The Frame

**Definition.** The **Pauli representation** of the quaternion algebra is the real-linear map

$$
\mathsf{M}_2:\mathbb{H}\longrightarrow M_2(\mathbb{C})
$$

fixed on the four units by

$$
\mathsf{M}_2(e_t)=I_2,\quad
\mathsf{M}_2(\vec e_x)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\quad
\mathsf{M}_2(\vec e_y)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
\mathsf{M}_2(\vec e_z)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.
$$

**The name.** The three imaginary images are $-i$ times the **Pauli matrices**

$$
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad\text{so that}\qquad
\mathsf{M}_2(\vec e_k)=-i\sigma_k ,
$$

and this is the reason the model is called the *Pauli* representation. The three arrays are Hermitian, traceless and of square $I_2$; they anticommute, $\sigma_j\sigma_k+\sigma_k\sigma_j=2\delta_{jk}I_2$, and they multiply by $\sigma_1\sigma_2=i\sigma_3$ cyclically. Both features of the display are then forced and not chosen. The factor $-i$ is what makes the square $-I_2$, since $\sigma_k$ squares to $+I_2$ while the map must send $\vec e_k^{2}=-e_t$ to $-I_2$. The sign is fixed by the cyclic relation, because
$$
(-i\sigma_1)(-i\sigma_2)=-\sigma_1\sigma_2=-i\sigma_3=\mathsf{M}_2(\vec e_z),
$$
whereas the opposite overall sign would give $+i\sigma_3$ for the product and lose the relation $\mathsf{M}_2(\vec e_x)\mathsf{M}_2(\vec e_y)=\mathsf{M}_2(\vec e_z)$. The factor and the signs are the algebra read in matrices, not conventions laid on it.

**The dictionary.** On a general element,

$$
\mathsf{M}_2(\tilde q)=\begin{pmatrix}q_t-iq_z&-iq_x-q_y\\ -iq_x+q_y&q_t+iq_z\end{pmatrix}
=\begin{pmatrix}z&w\\-\overline{w}&\overline{z}\end{pmatrix},
\qquad z=q_t-iq_z,\quad w=-q_y-iq_x .
$$

Two complex numbers $z,w$ carry the four real parameters, and the second row is not free: it is the conjugate of the first row, with a sign. That is the whole content of the embedding.

**The check.** The three images of the pure units satisfy the quaternion relations: squaring gives $-I_2$ three times, and multiplying gives $\mathsf{M}_2(\vec e_x)\mathsf{M}_2(\vec e_y)=\mathsf{M}_2(\vec e_z)$ together with its two cyclic variants. The three relations generate the algebra, so the real-linear extension is multiplicative.

**Theorem (the image is a real form).** The image is the subspace of the displayed shape, and it is exactly the fixed set of the anti-linear involution

$$
\varsigma(A)=J\overline{A}J^{-1},\qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
$$

**Proof.** For $A=\begin{pmatrix}z&w\\-\overline{w}&\overline{z}\end{pmatrix}$ one computes $J\overline{A}J^{-1}=A$; conversely the equation $J\overline{A}J^{-1}=A$ reads $A_{11}=\overline{A_{22}}$ and $A_{21}=-\overline{A_{12}}$, which is the displayed shape.

The involution $\varsigma$ is conjugate-linear and squares to the identity, so it is a real structure on $M_2(\mathbb{C})$, and the quaternion algebra is its fixed algebra:

$$
M_2(\mathbb{C})=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C},\qquad
\mathbb{H}=\{A:\varsigma(A)=A\}.
$$

**Corollary (no real model of degree two).** The algebra has no faithful real matrix representation of degree two, and the least real degree is four.

**Proof.** A faithful representation of degree two would be an isomorphism $\mathbb{H}\to M_2(\mathbb{R})$ by the dimension count $4=4$, and $M_2(\mathbb{R})$ has zero divisors, for instance $E_{11}E_{22}=0$ with both factors nonzero, while $\mathbb{H}$ is a division algebra. Degree four is attained by the regular representation.

**The price in one line.** The image has real dimension four inside the real dimension eight of $M_2(\mathbb{C})$, so half of the target is empty. Every statement below is therefore tested against the image, and the ones that fail the test are named as failures. The four-real-dimensionality is also the reason the model is an embedding and not an isomorphism: it displays the algebra as a subalgebra of a larger one, not as the whole of one.

### The Real Slice of the Biquaternion Display

**The same array over the two coefficient fields.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, and its $2\times2$ display in *$M_2(\mathbb{C})$ Pauli Representation* is fixed on the same four units by the same four arrays, the coefficients being allowed to be complex. The display of this article is that one at real coefficients: writing $Q_\mu=q_\mu+i0$ in
$$
\mathsf{M}_2(\tilde Q)=Q_tI_2-i\bigl(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3\bigr)
$$
gives exactly $\mathsf{M}_2(\tilde q)$ above. So the quaternion model is the real slice of the biquaternion model, and the two articles compute with one array.

**What the widening of the field does.** It separates the four brackets of §*The Four Brackets* into two pairs, because $|Q_\mu|^2$ is no longer $Q_\mu^2$; it makes the quaternionic bracket $Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ complex-valued, so that the one bracket which is positive definite here is not definite there; and it makes the image the whole of $M_2(\mathbb{C})$, since $\mathbb{B}\cong M_2(\mathbb{C})$ is an isomorphism. The quaternion article is the case in which the same display is an embedding, and every statement below is the specialisation of a biquaternion statement to a real four-dimensional slice, with the additional strength that the determinant is positive definite on it.

**What does not transfer.** The Peirce frame, the two families, the sixteen basis operators and the gamma set are structures of the biquaternion article; here the algebra has no idempotent and the display of the element needs no frame. The four images are the images of the units and not the entries of a matrix read in a basis, and the frame enters only in the $4\times4$ model of the companion article, where the operators are acted on.

## The Left and the Right Matrices

**Definition.** Left and right multiplication by $\tilde q$ are the maps of the carrier

$$
L_{\tilde q}(\tilde x)=\tilde q\tilde x,\qquad R_{\tilde q}(\tilde x)=\tilde x\tilde q,
$$

and in the model they read

$$
L_{\tilde q}:\ A\longmapsto \mathsf{M}_2(\tilde q)\,A,\qquad
R_{\tilde q}:\ A\longmapsto A\,\mathsf{M}_2(\tilde q).
$$

**Both stay inside the image.** If $A$ is in the image and $B$ is in the image, then $AB$ is in the image, because the image is a subalgebra. So $L$ and $R$ are operators of the carrier, and each is a faithful copy of $\mathbb{H}$ inside $\operatorname{End}_{\mathbb{R}}(\mathbb{H})\cong M_4(\mathbb{R})$:

$$
L:\mathbb{H}\to M_4(\mathbb{R}),\qquad R:\mathbb{H}\to M_4(\mathbb{R}),
$$

both injective, both of image of real dimension four.

**The two copies.** They commute, $L_{\tilde q}R_{\tilde p}=R_{\tilde p}L_{\tilde q}$, which is associativity; each is the centraliser of the other inside $M_4(\mathbb{R})$, by the double centraliser theorem applied to a division algebra; and they intersect in the scalars, $L_{\tilde q}=R_{\tilde q}$ exactly for $\tilde q\in\mathbb{R}e_t$.

**The relation by the conjugate transpose.** With $C(A)=A^{\dagger}$ the conjugate transpose,

$$
R_{\tilde q}=C\,L_{\tilde q^{*}}\,C .
$$

**Proof.** $C L_{\tilde q^{*}}C(A)=\bigl(\mathsf{M}_2(\tilde q^{*})A^{\dagger}\bigr)^{\dagger}=A\,\mathsf{M}_2(\tilde q^{*})^{\dagger}=A\,\mathsf{M}_2(\tilde q)=R_{\tilde q}(A)$, using $\mathsf{M}_2(\tilde q)^{\dagger}=\mathsf{M}_2(\tilde q^{*})$.

The identity is the complex form of the statement that the two copies are the two sides of the same product: the right copy is the left copy read through the adjoint, and $C$ is conjugate-linear, which is why the two copies are genuinely different and do not coincide.

**The invariants.** For every $\tilde q$,

$$
\operatorname{rank}L_{\tilde q}=\operatorname{rank}R_{\tilde q}=4\ \ (\tilde q\neq0),\qquad
\det L_{\tilde q}=\det R_{\tilde q}=N(\tilde q)^{2},\qquad
\operatorname{tr}L_{\tilde q}=4q_t .
$$

The trace is computed in the real basis of the carrier $(e_t,\vec e_x,\vec e_y,\vec e_z)$, where each basis vector $\tilde e_\nu$ is sent to $\tilde q\tilde e_\nu$ and the coefficient of $\tilde e_\nu$ in that product is $q_t$.

**The absence.** There is no $2\times2$ real matrix of either family, since there is no real model at all; the left and right matrices are genuinely $4\times4$, one size above the model. This is the first of the two places where the complex model and the operator layer have different sizes, and the operators article is organised around it.

## The Product

**Theorem (multiplicativity).** For all $\tilde q,\tilde p$,

$$
\mathsf{M}_2(\tilde q\tilde p)=\mathsf{M}_2(\tilde q)\,\mathsf{M}_2(\tilde p).
$$

**Proof.** Both sides are bilinear over $\mathbb{R}$, so it suffices to check the sixteen products of basis elements, which reduces to the three relations $M_1M_2=M_3$, $M_2M_3=M_1$, $M_3M_1=M_2$ and $M_k^2=-I$.

**The image is closed.** The product of two matrices of the displayed shape is again of that shape, so the image is a subalgebra; it is not an ideal, since $M_2(\mathbb{C})$ is simple and the image is proper.

**What the product sees.** The product of the model is the matrix product, and the four-real-dimensional image is closed under it. The failure is elsewhere: the image is not closed under complex scalar multiplication. For $A$ in the image and $\lambda\in\mathbb{C}$ not real, $\lambda A$ is not in the image unless $A=0$, because the shape ties the second row to the conjugate of the first. So the image is an $\mathbb{R}$-subspace and not a $\mathbb{C}$-subspace, and that is the exact sense in which the model is four-real-dimensional inside eight.

**The matrix units.** The algebra is a division algebra, so it has no nontrivial idempotent and therefore no system of matrix units: the Peirce decomposition of the split-quaternion category has no counterpart here. What replaces it is the pair of idempotents of the complexified algebra, $\tfrac12(e_t\pm iu)$, of the next-but-one section; they are not elements of $\mathbb{H}$.

**The two products that differ.** In the split-quaternion category the model is an isomorphism, so $\mathsf{M}_2(\tilde q\tilde p)$ and $\mathsf{M}_2(\tilde p\tilde q)$ are two matrices with the same spectrum, and everything about them is read off the spectrum. Here the same is true and stronger: the two products are conjugate to each other, because $\tilde p\tilde q=\tilde q^{-1}(\tilde q\tilde p)\tilde q$ for a unit $\tilde q$, so they have the same trace and the same determinant identically and not merely numerically.

## The Trace

**Theorem (the trace).** For every quaternion,

$$
\operatorname{tr}\mathsf{M}_2(\tilde q)=2q_t=2\operatorname{Re}z .
$$

**Proof.** The diagonal entries are $z$ and $\overline{z}$, whose sum is $2\operatorname{Re}z=2q_t$.

**The traceless part.** The trace vanishes exactly on the pure quaternions:

$$
\mathsf{M}_2(V)=\mathfrak{su}(2)=\{A\in\mathsf{M}_2(\mathbb{H}):\operatorname{tr}A=0\},
$$

spanned by the three images of $\vec e_x,\vec e_y,\vec e_z$, which are anti-Hermitian. So the traceless part of the image is a three-dimensional real space of anti-Hermitian matrices, and the scalar part is recovered as $\tfrac12\operatorname{tr}$.

**The trace is real and it is not a criterion.** The trace of a matrix in the image is real, whatever the element, because the two diagonal entries are conjugate. It is blind to the three vector coordinates, so it separates the elements by $q_t$ alone: $e_t+2\vec e_x$ and $e_t-3\vec e_y$ have the same trace and different norms. Its role is to split the image into the scalar line and the traceless part, and the second is the Lie algebra of the unit group.

**The trace form.** The bilinear form $\langle A,B\rangle_{\operatorname{tr}}=\operatorname{tr}(AB)$ restricted to the image has the Gram matrix

$$
\operatorname{tr}\bigl(\mathsf{M}_2(\tilde e_\mu)\mathsf{M}_2(\tilde e_\nu)\bigr)=\operatorname{diag}(2,-2,-2,-2),
$$

of signature $(1,3)$. So the trace form is the Minkowski form on the four real coordinates, positive on the scalar part and negative on the pure part. This is the exact opposite of the split-quaternion case, where the determinant was the indefinite form and the trace form had signature $(3,1)$; here the determinant is definite and the trace form is the Lorentzian one.

## The Determinant

**Theorem (the determinant is the norm).** For every quaternion,

$$
\det\mathsf{M}_2(\tilde q)=|z|^{2}+|w|^{2}=q_t^2+q_x^2+q_y^2+q_z^2=N(\tilde q).
$$

**Proof.** $z\overline{z}+w\overline{w}=|z|^{2}+|w|^{2}=(q_t^2+q_z^2)+(q_y^2+q_x^2)$.

**The form is definite.** The determinant is a positive definite quadratic form in the four real coordinates, so its zero set is a point:

$$
\{\tilde q:\det\mathsf{M}_2(\tilde q)=0\}=\{0\}.
$$

There is no null cone, no isotropic line and no zero divisor. The rank of the matrix is therefore two for every nonzero quaternion and zero only at the origin, and the rank stratification of the split-quaternion category collapses to two strata.

| condition | stratum | dimension | elements |
|---|---|---|---|
| $\det\neq0$ | units | $4$ | every nonzero element |
| $\tilde q=0$ | the origin | $0$ | the zero matrix |

**The unit criterion.** An element is a unit exactly when its matrix is invertible, which here is exactly when it is nonzero; the group of units is $\mathbb{H}^{\times}=\mathbb{H}\setminus\{0\}$, and its image is $\mathsf{M}_2(\mathbb{H})\setminus\{0\}$. The determinant is multiplicative, so the units of norm one form the subgroup of matrices of determinant one inside the image, which is the group $SU(2)$ of the section on the norms.

**What the determinant hides.** A definite determinant cannot show the difference between the quaternion algebra and the matrix algebra in the way the indefinite one did, because on a definite form all nonzero vectors look alike. The structures that the split case read off the null cone — the minimal left ideals, the rulings, the projective geometry — have no counterpart here; what replaces them is the spectral decomposition, which the split case could not make uniform precisely because its discriminant changes sign.

## The Spectral Projectors

**The characteristic polynomial.** The matrix of the image is $\begin{pmatrix}z&w\\-\overline{w}&\overline{z}\end{pmatrix}$, so

$$
\chi_A(\lambda)=\lambda^{2}-2\operatorname{Re}(z)\,\lambda+\bigl(|z|^{2}+|w|^{2}\bigr)
=\lambda^{2}-2q_t\lambda+N(\tilde q).
$$

**The discriminant.** Its discriminant is

$$
4q_t^{2}-4N(\tilde q)=-4\bigl(q_x^{2}+q_y^{2}+q_z^{2}\bigr)=-4\lVert\vec v\rVert^{2}\le0,
$$

so the eigenvalues are

$$
\lambda_\pm=q_t\pm i\lVert\vec v\rVert ,
$$

a conjugate pair, real and equal only when the element is scalar. This is the sharp contrast with the split-quaternion category, where the discriminant $4(q_y^{2}+q_z^{2}-q_x^{2})$ changes sign and produces three spectral types. Here there is one type.

| condition | eigenvalues | spectrum | centraliser |
|---|---|---|---|
| $\vec v=0$ | the double real $q_t$ | the matrix is scalar | all of $M_2(\mathbb{C})$ |
| $\vec v\neq0$ | $q_t\pm i\lVert\vec v\rVert$ | one conjugate pair, distinct | $\cong\mathbb{C}$, of complex dimension $2$ |

**Theorem (the projectors are Hermitian).** Put $u=\vec v/\lVert\vec v\rVert$ for a non-scalar element. Then $u$ is a pure unit quaternion, $(iu)^{2}=e_t$ in the complexified algebra, and

$$
P_\pm=\tfrac12\bigl(I_2\mp i\,\mathsf{M}_2(u)\bigr)=\mathsf{M}_2\bigl(\tfrac12(e_t\mp iu)\bigr)
$$

satisfy

$$
P_+^{2}=P_+,\quad P_-^{2}=P_-,\quad P_+P_-=0,\quad P_++P_-=I_2,\quad P_\pm^{\dagger}=P_\pm,
$$

and

$$
\mathsf{M}_2(\tilde q)=\bigl(q_t+i\lVert\vec v\rVert\bigr)P_++\bigl(q_t-i\lVert\vec v\rVert\bigr)P_- .
$$

**Proof.** $iu$ has square $(iu)^{2}=i^{2}u^{2}=(-1)(-e_t)=e_t$, so $\tfrac12(e_t\mp iu)$ is idempotent in the complexified algebra and the two are complementary and orthogonal; the map $\mathsf{M}_2$ extends to the complexification and preserves the identities. The Hermitian property is $\mathsf{M}_2(u)^{\dagger}=\mathsf{M}_2(u^{*})=-\mathsf{M}_2(u)$, since $u$ is pure and of unit norm, so $i\mathsf{M}_2(u)$ is Hermitian. Finally $-i\mathsf{M}_2(u)=P_+-P_-$, so $\mathsf{M}_2(u)=i(P_+-P_-)$, and with $I_2=P_++P_-$ the spectral formula follows.

**The label.** The sign is chosen so that $P_\pm$ belongs to $\lambda_\pm$, as in the biquaternion article, where $\rho_\pm=\tfrac12(I_2\pm\mathsf{M}_2(\vec\Zeta))$ with $\vec\Zeta=-iu$ is the same pair.

**The reading.** The projectors are rank one, of trace one and determinant zero, and they are **orthogonal** projections, which the split-quaternion projectors were not: there the trace form was indefinite and the two eigenlines were not orthogonal. The spectral theorem applies to the whole image, and the eigenvalues are exactly the two numbers $q_t\pm i\lVert\vec v\rVert$.

**The diagonalising matrix.** The eigenvector of $\lambda_+=q_t+i\lVert\vec v\rVert$ is $\begin{pmatrix}w\\ \lambda_+-z\end{pmatrix}$, and the eigenvector of $\lambda_-$ is the same with $\lambda_-$ in place of $\lambda_+$. The matrix

$$
S=\begin{pmatrix}w&w\\ \lambda_+-z&\lambda_--z\end{pmatrix},
\qquad
\det S=-2i\lVert\vec v\rVert\,w,
$$

is invertible whenever $w\neq0$ and $\vec v\neq0$, and then $\mathsf{M}_2(\tilde q)=S\operatorname{diag}(\lambda_+,\lambda_-)S^{-1}$. When $w=0$ the matrix is already diagonal, so every non-scalar element is diagonalisable and none is defective.

**Why no defect.** A defective matrix has a repeated eigenvalue and a one-dimensional eigenspace. Here a repeated eigenvalue forces $\lVert\vec v\rVert=0$, that is a scalar, and a scalar matrix is diagonal. So the image contains no Jordan block of size two other than the scalars, and the split-quaternion parabolic stratum has no counterpart.

## The Adjugate and the Inverse

**Theorem (the adjugate is the conjugate transpose).** For every quaternion,

$$
\operatorname{adj}\mathsf{M}_2(\tilde q)=\mathsf{M}_2(\tilde q)^{\dagger}=\mathsf{M}_2(\tilde q^{*}),
\qquad
\mathsf{M}_2(\tilde q)\,\mathsf{M}_2(\tilde q)^{\dagger}=N(\tilde q)\,I_2 .
$$

**Proof.** The adjugate of $\begin{pmatrix}z&w\\-\overline{w}&\overline{z}\end{pmatrix}$ is $\begin{pmatrix}\overline{z}&-w\\ \overline{w}&z\end{pmatrix}$, which is the conjugate transpose and is the image of $\tilde q^{*}$; the product identity is the definition of the norm.

**The inverse.** On a nonzero element,

$$
\mathsf{M}_2(\tilde q)^{-1}=\frac{\mathsf{M}_2(\tilde q)^{\dagger}}{N(\tilde q)}=\mathsf{M}_2\bigl(\tilde q^{*}/N(\tilde q)\bigr),
$$

so the inverse is again in the image, as it must be.

**The normality.** The two identities $\mathsf{M}_2(\tilde q)\mathsf{M}_2(\tilde q)^{\dagger}=N I_2$ and $\mathsf{M}_2(\tilde q)^{\dagger}\mathsf{M}_2(\tilde q)=N I_2$ say that every matrix of the image is **normal** and, more, **conformal**: its two singular values are equal, both $\sqrt N$. The image is therefore not an arbitrary four-dimensional subspace of $M_2(\mathbb{C})$ but a very special one, and the following characterisation records it:

$$
\mathsf{M}_2(\mathbb{H})\setminus\{0\}=\mathbb{R}_{>0}\cdot SU(2),
$$

the cone on the special unitary group. The polar decomposition of a quaternion is then a statement about a matrix: $\mathsf{M}_2(\tilde q)=\sqrt N\,U$ with $U=\mathsf{M}_2(\tilde q)/\sqrt N\in SU(2)$.

## The Norms

**Three forms.** The model carries three natural forms, and the determinant is one of them.

| form | definition | Gram matrix on the four units | signature | invariant under |
|---|---|---|---|---|
| determinant form | $N=\det\mathsf{M}_2(\tilde q)$ | $I_4$ | $(4,0)$ | the product |
| trace form | $\langle A,B\rangle_{\operatorname{tr}}=\operatorname{tr}(AB)$ | $\operatorname{diag}(2,-2,-2,-2)$ | $(1,3)$ | conjugation by units |
| Frobenius form | $\langle A,B\rangle_F=\operatorname{tr}(A^{\dagger}B)$ | $2I_4$ | $(4,0)$ | the unitary group, not the product |

**The determinant form is Euclidean.** Its Gram matrix is the identity in the basis of the four units, so it is the ordinary Euclidean form of $\mathbb{R}^{4}$ under the coordinates $(q_t,q_x,q_y,q_z)$, and its group of isometries is $O(4)$. Multiplicativity then says that the model embeds the units into $O(4)$ up to scale, which is the double cover $SU(2)\to SO(3)$ operating on the pure part.

**The trace form is Minkowski.** Its Gram matrix is $\operatorname{diag}(2,-2,-2,-2)$, of signature $(1,3)$, and it is invariant under the inner automorphisms, $\operatorname{tr}(gAg^{-1}gBg^{-1})=\operatorname{tr}(AB)$. It is the form of the Minkowski space of signature $(1,3)$ that the quaternion algebra acts on by Lorentz transformations, and it is **not** the determinant form.

**The Frobenius form is a Hermitian metric.** $\operatorname{tr}(A^{\dagger}B)$ is a positive definite Hermitian form on $M_2(\mathbb{C})$, its restriction to the image is $2$ times the Euclidean form, and it is the inner product with respect to which the conjugate transpose is the adjoint. The three forms therefore play three different roles: the determinant is algebraic and multiplicative, the trace form is the invariant of the group action, and the Frobenius form is the metric of the matrix space.

**The absence of a Hermitian structure on the algebra.** The product and the norm do not make $\mathbb{H}$ a complex Hilbert space, because the scalar field is $\mathbb{R}$; what the model shows is that the complex structure $A\mapsto iA$ does not preserve the image, so the complex Hermitian metric of $M_2(\mathbb{C})$ restricts to a real Euclidean metric and no more.

### The Four Brackets

**The table.** The four algebraic brackets of the corpus are four quadratic invariants of the element, each read from a word in $A$, its adjugate and its conjugate transpose:

| bracket | value | matrix formula | definite |
|---|---|---|---|
| Plain $P$ | $q_t^{2}-\lVert\vec v\rVert^{2}$ | $\tfrac12\operatorname{tr}(A^{2})$ | no |
| Quaternionic $N$ | $q_t^{2}+\lVert\vec v\rVert^{2}$ | $\det A$ | yes |
| Hermitian $H$ | $q_t^{2}+\lVert\vec v\rVert^{2}$ | $\tfrac12\operatorname{tr}(A^{\dagger}A)$ | yes |
| Krein $K$ | $q_t^{2}-\lVert\vec v\rVert^{2}$ | $\tfrac12\operatorname{tr}(\operatorname{adj}(A)A^{\dagger})$ | no |

**The plain bracket.** With $A=q_tI_2+\mathsf{M}_2(\vec v)$ and $\operatorname{tr}(\mathsf{M}_2(\vec v)^{2})=-2\lVert\vec v\rVert^{2}$,
$$
\tfrac12\operatorname{tr}(A^{2})=q_t^{2}-\lVert\vec v\rVert^{2}=P .
$$
The word is the square of the matrix closed by a trace, and it is the trace form of §*The Trace* read on one element.

**The collapse to two.** Over $\mathbb{R}$ the coefficients are real, so $\lvert q_\mu\rvert^{2}=q_\mu^{2}$ and the four brackets are two: $H=N$ and $K=P$. The Hermitian bracket is the quaternionic one because the conjugation of the coefficients is trivial here, and the two that remain are the ones the article has already named: $N$ is the determinant, multiplicative and definite, and $P$ is the trace form on one element, indefinite of signature $(1,3)$. In the biquaternion algebra the coefficients are complex and the four are distinct; the widening of $\mathbb{R}$ to $\mathbb{C}$ is exactly what separates them, as §*The Real Slice of the Biquaternion Display* records.

## The Subspaces

**The tabulation.** The distinguished subspaces of the algebra are subspaces of the image, and the dictionary converts between the two descriptions.

| subspace | algebra condition | matrix condition | dimension |
|---|---|---|---|
| scalar line | $\vec v=0$ | $A=\lambda I_2$, $\lambda\in\mathbb{R}$ | $1$ |
| pure part $V$ | $q_t=0$ | $\operatorname{tr}A=0$, that is $A^{\dagger}=-A$ | $3$ |
| complex line $L_x$ | $q_y=q_z=0$ | $A=\begin{pmatrix}a&-ib\\ -ib&a\end{pmatrix}$, $a,b\in\mathbb{R}$ | $2$ |
| complex line $L_y$ | $q_x=q_z=0$ | $A=\begin{pmatrix}a&-b\\ b&a\end{pmatrix}$, a scaled rotation | $2$ |
| complex line $L_z$ | $q_x=q_y=0$ | $A=\operatorname{diag}(z,\overline{z})$ | $2$ |
| Hermitian part | — | $\tfrac12(A+A^{\dagger})=q_tI_2$ | $1$ |
| anti-Hermitian part | $q_t=0$ | $\tfrac12(A-A^{\dagger})=A$ | $3$ |

**The Hermitian part is scalar.** This is the sharpest structural difference from the split-quaternion category. There, $\tfrac12(\mathsf{M}_2(\tilde q)+\mathsf{M}_2(\tilde q)^{\dagger})$ was the general symmetric matrix, a three-dimensional space, and the Hermitian/symmetric decomposition split the algebra into a two-parameter and a two-parameter part. Here

$$
\tfrac12\bigl(A+A^{\dagger}\bigr)=q_tI_2,\qquad \tfrac12\bigl(A-A^{\dagger}\bigr)=\mathsf{M}_2(\vec v),
$$

so the Hermitian part is the scalar part, of dimension one, and the anti-Hermitian part is the whole pure part, of dimension three. The decomposition still splits the four real dimensions as $1+3$, but the two pieces are the scalar line and the traceless part, and the splitting is exactly the splitting by trace.

**The reason.** A matrix of the image satisfies $A^{\dagger}=\operatorname{adj}A$, so its Hermitian part is $\tfrac12(A+\operatorname{adj}A)=\tfrac12(\operatorname{tr}A)I_2$ by the Cayley–Hamilton identity in dimension two. The scalar Hermitian part is therefore a consequence of the conformal normality of the image, and it is not a coincidence of the choice of basis.

**The complex lines.** Each two-dimensional subspace $\operatorname{span}\{e_t,\vec e_k\}$ is a copy of the complex numbers inside $\mathbb{H}$, and the model sends it to a two-real-dimensional subspace of the image on which the determinant restricts to $|z|^{2}$; the three of them are the three complex structures of $\mathbb{R}^{4}$ compatible with the quaternion multiplication, and they correspond to the three almost complex structures $J_1,J_2,J_3$ of the model.

**The projection.** The projection onto the Hermitian part is $A\mapsto\tfrac12(A+A^{\dagger})$, which here is the map $A\mapsto(\operatorname{Re}\operatorname{tr}A/2)I_2$, and the projection onto the anti-Hermitian part is $A\mapsto\tfrac12(A-A^{\dagger})$. Both are real-linear and neither is complex-linear, which is again the statement that the image is a real form and not a complex subspace.

## Summary

1. The model is the embedding $\mathsf{M}_2:\mathbb{H}\to M_2(\mathbb{C})$ with image $\{A:A_{21}=-\overline{A_{12}},\ A_{22}=\overline{A_{11}}\}$, a real form of $M_2(\mathbb{C})$ fixed by the anti-linear involution $A\mapsto J\overline{A}J^{-1}$.
2. There is no faithful real model of degree two, and the least real degree is four; the image has real dimension four inside eight.
3. Left and right multiplication stay inside the image and are two commuting copies of the algebra in $M_4(\mathbb{R})$, related by $R_{\tilde q}=C L_{\tilde q^{*}}C$ with $C$ the conjugate transpose, intersecting in the scalars.
4. The trace is $2q_t$ and the traceless part is the three-dimensional space of anti-Hermitian matrices.
5. The determinant is the norm $N$, positive definite, with no null cone; every nonzero element is a unit and the rank is two or zero.
6. The discriminant is $-4\lVert\vec v\rVert^{2}$, so the eigenvalues are the conjugate pair $q_t\pm i\lVert\vec v\rVert$ and every non-scalar element is diagonalisable.
7. The spectral projectors are $\tfrac12(I_2\mp i\mathsf{M}_2(u))$, Hermitian, rank one, orthogonal, they are the images of the idempotents $\tfrac12(e_t\mp iu)$ of the complexified algebra, and $P_\pm$ belongs to $\lambda_\pm$.
8. The adjugate is the conjugate transpose, every element of the image is conformal normal, and $\mathsf{M}_2(\mathbb{H})\setminus\{0\}=\mathbb{R}_{>0}\cdot SU(2)$.
9. Three forms coexist: the determinant, a quadratic form of signature $(4,0)$, equal to the norm and multiplicative; the trace form, of signature $(1,3)$ and invariant under the inner automorphisms; the Frobenius form $\operatorname{tr}(A^{\dagger}B)$, positive definite and Hermitian, twice the restriction of the Euclidean form.
10. The Hermitian part of an element of the image is scalar, and the Hermitian/anti-Hermitian splitting is the splitting by trace.
11. The four brackets collapse to two, $H=N$ and $K=P$, and the display is the real slice of the biquaternion $\mathsf{M}_2$ at $Q_\mu=q_\mu$.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathsf{M}_2$ | the Pauli representation $\mathbb{H}\to M_2(\mathbb{C})$ | this article |
| $\sigma_1,\sigma_2,\sigma_3$ | the Pauli matrices, $\mathsf{M}_2(\vec e_k)=-i\sigma_k$ | this article |
| ${}^{\dagger}$ | the conjugate transpose of a matrix | this article |
| $z,w$ | the two complex entries, $z=q_t-iq_z$, $w=-q_y-iq_x$ | this article |
| $N$ | the norm $q_t^2+q_x^2+q_y^2+q_z^2$, equal to $\det\mathsf{M}_2(\tilde q)$ | *Quaternion Norm and Invertibility* |
| $\tilde q^{*}$ | the conjugate $q_te_t-\vec v$ | *The Quaternion Conjugation and the Involutions* |
| $L_{\tilde q},R_{\tilde q}$ | left and right multiplication on the carrier, $4\times4$ real matrices | this article |
| $C$ | the conjugate transpose $A\mapsto A^{\dagger}$ | this article |
| $u$ | the pure unit $\vec v/\lVert\vec v\rVert$ | this article |
| $P_\pm$ | the Hermitian projectors $\tfrac12(I_2\mp i\mathsf{M}_2(u))$, of $\lambda_\pm$ | this article |
| $SU(2)$ | the units of norm one, that is $\mathsf{M}_2(\mathbb{H})\cap SL_2(\mathbb{C})$ | *Quaternion Exponential and Lie Group Structure* |
| $\varsigma$ | the anti-linear involution $A\mapsto J\overline{A}J^{-1}$ defining the real form | this article |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for $\mathbb{H}\cong\mathrm{Cl}_{0,2}$, the Cayley matrix of a quaternion and the $2\times2$ complex model.
- Wolfgang Pauli, "Zur Quantenmechanik des magnetischen Elektrons", *Zeitschrift für Physik* **43** (1927), for the three matrices that give the model its name.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the double centraliser theorem and the simplicity of a full matrix algebra.
- Fuzhen Zhang, *Matrix Theory* (Springer, 2011), for the real forms of $M_2(\mathbb{C})$, the conjugate transpose and the conformal normal matrices.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the two-sided action of the quaternions and the relation $R_{\tilde q}=C L_{\tilde q^{*}}C$.
