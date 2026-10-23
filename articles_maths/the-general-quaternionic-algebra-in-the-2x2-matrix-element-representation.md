
# __The General Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The reading group *Topology on the Introduction to the General Quaternionic Algebra of Biquaternions* reads the algebra through the **general quaternionic bilinear form** $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\natural})=\sum_\mu Q_{1,\mu} Q_{2,\mu}$ and through the **quaternionic product** $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$ that form polarises, whose algebra is *Introduction to the General Quaternionic Algebra*. This article reads that group through the $2\times2$ matrix realization $\mathsf{M}_2$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, and it is the first of the two representation articles of the group; the companion *The General Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* repeats the reading on the left regular representation.

The natural conjugation is the characteristic operation of the group, and in the model it is the **adjugate**: $\mathsf{M}_2(\tilde Q_2^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde Q_2)$. The quaternionic product is therefore the ordinary matrix product with the adjugate inserted in the first slot, $\mathsf{M}_2(\tilde Q_1\star\tilde Q_2)=\operatorname{adj}\mathsf{M}_2(\tilde Q_1)\,\mathsf{M}_2(\tilde Q_2)$, and the general quaternionic bilinear form is the adjugated trace pairing $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde Q_1)\operatorname{adj}\mathsf{M}_2(\tilde Q_2))$. The determinant is the norm, so the whole element theory of the group is read off the determinant of the matrix.

## The Representation

**Definition.** The **matrix realization** is the isomorphism written $\mathsf{M}_2$. It converts a biquaternion into a $2 \times 2$ complex matrix,

$$
\mathsf{M}_2:\mathbb{B}\longrightarrow M_2(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity: $\mathsf{M}_2(e_t)=I$ on the identity and $\mathsf{M}_2(\vec e_k)=-i\sigma_k$ on the three vector units.

On a general element it reads $\mathsf{M}_2(\tilde Q_2)=\begin{pmatrix} Q_{2t}-iQ_{2,z} & -iQ_{2,x}-Q_{2,y} \\ -iQ_{2,x}+Q_{2,y} & Q_{2t}+iQ_{2,z}\end{pmatrix}$. Its two invariants and its two conjugations are

$$
\operatorname{Tr}\mathsf{M}_2(\tilde Q_2)=2Q_{2t},\qquad \det \mathsf{M}_2(\tilde Q_2)=\langle\tilde Q_2\rangle_{\natural}=\sum_\mu Q_{2,\mu}^2,\qquad \mathsf{M}_2(\tilde Q_2^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde Q_2),\qquad \mathsf{M}_2(\tilde Q_2^{*})=\mathsf{M}_2(\tilde Q_2)^{\dagger} .
$$

The adjugate is also the conjugate of the transpose by a fixed matrix, $\operatorname{adj}\mathsf{M}_2(\tilde Q_2)=\mathsf{M}_2(-\vec e_y)\,\mathsf{M}_2(\tilde Q_2)^{\mathsf{T}}\,\mathsf{M}_2(-\vec e_y)^{-1}$, so the natural conjugation is a transposition and not a Hermitian transposition.

## The Quaternionic Product in the Model

**Theorem (the product is the adjugated matrix product).** For all biquaternions,

$$
\boxed{\; \mathsf{M}_2(\tilde Q_1\star\tilde Q_2)=\operatorname{adj}\mathsf{M}_2(\tilde Q_1)\,\mathsf{M}_2(\tilde Q_2) \;},
$$

the ordinary matrix product with the adjugate in the first slot.

*Proof.* $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$ and $\mathsf{M}_2$ is multiplicative, so $\mathsf{M}_2(\tilde Q_1\star\tilde Q_2)=\mathsf{M}_2(\tilde Q_1^{\natural})\mathsf{M}_2(\tilde Q_2)=\operatorname{adj}\mathsf{M}_2(\tilde Q_1)\,\mathsf{M}_2(\tilde Q_2)$.

**The adjugate reverses the order.** The mechanism of the whole reading is the reversal of the order under transposition. For all $A,B\in M_2(\mathbb{C})$,

$$
\operatorname{adj}(AB)=\operatorname{adj}(B)\operatorname{adj}(A),\qquad \operatorname{adj}(AB)\neq\operatorname{adj}(A)\operatorname{adj}(B)\ \text{in general},
$$

since $\operatorname{adj}(X)=\varepsilon X^{\mathsf{T}}\varepsilon^{-1}$ and $(AB)^{\mathsf{T}}=B^{\mathsf{T}}A^{\mathsf{T}}$. The inequality is seen on the images of the basis: $\operatorname{adj}\mathsf{M}_2(\vec e_x)\operatorname{adj}\mathsf{M}_2(\vec e_y)=\mathsf{M}_2(\vec e_x)\mathsf{M}_2(\vec e_y)=\mathsf{M}_2(\vec e_z)$, against $\operatorname{adj}\mathsf{M}_2(\vec e_x\vec e_y)=\operatorname{adj}\mathsf{M}_2(\vec e_z)=-\mathsf{M}_2(\vec e_z)$. Associativity of the product would require the adjugate inserted in the first slot to move across the other factors, and it does not, because a transpose does not commute with a product.

**Theorem (the trace and the determinant of a value).** For all biquaternions, with $\beta(\tilde Q_1,\tilde Q_2)=\sum_\mu Q_{1,\mu} Q_{2,\mu}$,

$$
\operatorname{Tr}\mathsf{M}_2(\tilde Q_1\star\tilde Q_2)=2\beta(\tilde Q_1,\tilde Q_2),\qquad \det \mathsf{M}_2(\tilde Q_1\star\tilde Q_2)=\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}\langle\tilde Q_2,\tilde Q_2\rangle_{\natural}.
$$

*Proof.* The determinant is multiplicative and $\det\operatorname{adj}(A)=\det A$, so $\det \mathsf{M}_2(\tilde Q_1\star\tilde Q_2)=\det \mathsf{M}_2(\tilde Q_1)\det \mathsf{M}_2(\tilde Q_2)=\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}\langle\tilde Q_2,\tilde Q_2\rangle_{\natural}$. For the trace, $\operatorname{Tr}\mathsf{M}_2(\tilde Q_1\star\tilde Q_2)=2\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)$ by the trace identity, and the scalar part of $\tilde Q_1^{\natural}\tilde Q_2$ is $Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)=\beta(\tilde Q_1,\tilde Q_2)$.

**The square and the idempotents.** The square of the product is the scalar matrix of the determinant,

$$
\mathsf{M}_2(\tilde Q_2\star\tilde Q_2)=\operatorname{adj}\mathsf{M}_2(\tilde Q_2)\mathsf{M}_2(\tilde Q_2)=\det \mathsf{M}_2(\tilde Q_2)\,I=\langle\tilde Q_2\rangle_{\natural}\,I ,
$$

so the idempotents of the quaternionic product are exactly $0$ and $e_t$, and the zero divisors of the product are exactly the singular matrices. No nontrivial projection of $M_2(\mathbb{C})$ survives as an idempotent: the Hermitian projections $\tfrac12\bigl(I+i\sum_ku_k\mathsf{M}_2(\vec e_k)\bigr)$ over the real unit vectors $\vec u=(u_x,u_y,u_z)$ are idempotent for the ordinary matrix product and are not idempotent here, becoming square-zero instead, $\operatorname{adj}(B)B=0$.

**The units and the norm.** The product has a unit exactly when the determinant does not vanish: the units of the algebra are the matrices of $GL_2(\mathbb{C})$, the elements with $\langle\tilde Q_2\rangle_{\natural}\neq0$, and the norm-one group is $SL_2(\mathbb{C})$.

**The symmetrisation and the left multiplications.** The central coefficient of the symmetrisation is half the trace of the transported product, $\beta(\tilde Q_1,\tilde Q_2)=\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2)\bigr)$, and the symmetrised product itself is the scalar matrix $\beta(\tilde Q_1,\tilde Q_2)I=\tfrac12\bigl(\operatorname{adj}(A)B+\operatorname{adj}(B)A\bigr)$, which is the matrix form of the centrality of the symmetrisation. The left multiplication by $\tilde Q_1$ is the ordinary multiplication by the adjugate, $\mathsf{M}_2\bigl(L_{\tilde Q_1}(\tilde{Q}_3)\bigr)=\operatorname{adj}\mathsf{M}_2(\tilde Q_1)\,\mathsf{M}_2(\tilde{Q}_3)$, so the composition law $L_{\tilde Q_1}\circ L_{\tilde Q_4}=L_{\tilde Q_4\tilde Q_1}$ is the anti-automorphism property $\operatorname{adj}(A)\operatorname{adj}(C)=\operatorname{adj}(CA)$, and the monoid of left multiplications is the opposite of the multiplicative monoid of the matrices.

**The associator.** The associator of the transported product $A\star'B=\operatorname{adj}(A)B$ is

$$
(A\star'B)\star'C-A\star'(B\star'C)=\operatorname{adj}(B)AC-\operatorname{adj}(BA)C=\bigl(\operatorname{adj}(B)A-\operatorname{adj}(BA)\bigr)C ,
$$

the failure of the transpose-conjugation to be multiplicative in the same order: the adjugate sends $BA$ to $\operatorname{adj}(A)\operatorname{adj}(B)$, whereas the first term carries the transposed $\langle\cdot,\cdot\rangle_{\natural}$ past $A$ without reversing. This is the matrix form of the closed form $[\tilde Q_1,\tilde Q_2,\tilde Q_4]=(\tilde Q_2^{\natural}\tilde Q_1-\tilde Q_1^{\natural}\tilde Q_2^{\natural})\tilde Q_4$ of the group, and the non-associativity of the product is the elementary fact that a transpose does not commute with a product.

## The General Quaternionic Bilinear Form in the Model

**Theorem (the adjugated trace pairing).** For all biquaternions,

$$
\boxed{\; \langle\tilde Q_1,\tilde Q_2\rangle_{\natural} = \tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde Q_1)\operatorname{adj}\mathsf{M}_2(\tilde Q_2)\bigr) \;},
$$

the trace pairing in which the second argument is adjugated.

*Proof.* $\operatorname{adj}\mathsf{M}_2(\tilde Q_2)=\mathsf{M}_2(\tilde Q_2^{\natural})$, so the right-hand side is $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2^{\natural}))=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\natural})=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$ by the trace identity $\mathrm{Sc}(\tilde Q_4\tilde{S})=\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde Q_4)\mathsf{M}_2(\tilde{S}))$.

**Theorem (the diagonal is the determinant).** On the diagonal,

$$
\boxed{\; \langle\tilde Q_2,\tilde Q_2\rangle_{\natural} = \tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde Q_2)\operatorname{adj}\mathsf{M}_2(\tilde Q_2)\bigr) = \det \mathsf{M}_2(\tilde Q_2) = \sum_\mu Q_{2,\mu}^2 \;},
$$

so the form is the polarisation of the norm, and it is the determinant read as a quadratic form.

**The Gram matrix and the signature.** In the coefficient basis the Gram matrix of the form is the identity $I_4$; over $\mathbb{R}$ the form is the split form of signature $(4,4)$ on the eight real coordinates. It is indefinite and non-degenerate.

**The null set.** The form vanishes exactly on the singular matrices, $\det \mathsf{M}_2(\tilde Q_2)=0$, that is on the zero divisors of the algebra; this is a real cone of real dimension $6$ in $\mathbb{R}^8$, the vanishing of one complex quadratic. It is the null set of the general quaternionic bilinear form alone and is strictly smaller than the real isotropic cone of the realified form, of real dimension $7$.

**The restriction to the Hermitian and anti-Hermitian matrices.** The determinant also reads the restriction of the form to the two four-dimensional subspaces of matrices. On the Hermitian matrices $\begin{pmatrix}a&z\\\bar z&b\end{pmatrix}$ with $a,b\in\mathbb{R}$ and $z\in\mathbb{C}$ the determinant is $ab-|z|^2$, a form of signature $(1,3)$ on the real four-space $\mathbb{M}_+$; on the anti-Hermitian matrices $\begin{pmatrix}ia&z\\-\bar z&ib\end{pmatrix}$ the determinant is $|z|^2-ab$, a form of signature $(3,1)$ on $\mathbb{M}_-$. Both are that table read on the matrices, whose general form is in *Remarkable Subspaces under the General Quaternionic Algebra*.

**The automorphisms.** The form has Gram matrix $I_4$, so its automorphism group on the coefficient space is the complex orthogonal group $O_4(\mathbb{C})$, of complex dimension $6$ and real dimension $12$; the real part of the form is the split real bilinear form of signature $(4,4)$, with automorphism group the split orthogonal group $O(4,4)$. The natural conjugation is an automorphism of the form, since the adjugate preserves the adjugated trace pairing.

**The congruence with the general plain bilinear form.** The natural conjugation reverses the pairing, $\langle\tilde Q_1^{\natural},\tilde Q_2^{\natural}\rangle_{\natural}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1,\tilde Q_2\rangle$ read on $\tilde Q_1^{\natural},\tilde Q_2^{\natural}$, so with $J=\operatorname{diag}(1,i,i,i)$ the coefficient matrices are congruent,
$$
J^{\mathsf T}\,D\,J=\mathrm{I}_4,\qquad D=\operatorname{diag}(1,-1,-1,-1),
$$
and the two forms share the automorphism group $O_4(\mathbb{C})$; the transport of the four pairings is the dictionary of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*.

## Worked Examples

**A zero divisor.** Let $\tilde Q_2=e_t+i\vec e_x$. Then $\langle\tilde Q_2\rangle_{\natural}=1+i^2=0$, so $\tilde Q_2$ is a zero divisor and $\mathsf{M}_2(\tilde Q_2)=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ is singular; the quaternionic square is $\tilde Q_2\star\tilde Q_2=\langle\tilde Q_2\rangle_{\natural}e_t=0$.

**A basis element.** Let $\tilde Q_1=\vec e_x$. Then $\operatorname{adj}\mathsf{M}_2(\vec e_x)=\mathsf{M}_2(\vec e_x^{\natural})=-\mathsf{M}_2(\vec e_x)$, and $\mathsf{M}_2(\vec e_x\star\tilde Q_2)=-\mathsf{M}_2(\vec e_x)\mathsf{M}_2(\tilde Q_2)$; the form at the two equal arguments is $\langle \vec e_x,\vec e_x\rangle_{\natural}=1$.

**A product read off the determinant.** Let $\tilde Q_1=e_t+\vec e_y$ and $\tilde Q_2=e_t-\vec e_y$. Then $\langle\tilde Q_1\rangle_{\natural}=\langle\tilde Q_2\rangle_{\natural}=2$ and $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=1-1=0$, so the two are isotropic to each other although both are units; the corresponding matrices have determinants $2$ and are isotropic for the adjugated trace pairing.

## The Matrices

**The generators.** The realization is fixed on the basis by four matrices:

$$
\mathsf{M}_2(e_t)=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
\mathsf{M}_2(\vec e_x)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf{M}_2(\vec e_y)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf{M}_2(\vec e_z)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.
$$

The general element has trace $2Q_{2t}$ and determinant $\sum_\mu Q_{2,\mu}^2$. The model is onto $M_2(\mathbb{C})$, so the whole element theory of the group is read on the matrices.

**The involution, entry by entry.** The adjugate is the involution read on the coefficients, $\mathsf{M}_2(\tilde Q_2^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde Q_2)$, and it is the trace-complement of the matrix, $\operatorname{adj}X=(\operatorname{Tr}X)I-X$. At the unit $\vec e_x$,

$$
\operatorname{adj}\mathsf{M}_2(\vec e_x)=\begin{pmatrix}0&i\\i&0\end{pmatrix}=-\mathsf{M}_2(\vec e_x)=\mathsf{M}_2(\vec e_x^{\natural}),
$$

the two entries off the diagonal being the negation of the two entries of the matrix.

**The product, entry by entry.** The product $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$ is the matrix product with the adjugate in the first slot, and at the pair $\vec e_x,\vec e_y$ it is

$$
\mathsf{M}_2(\vec e_x\star \vec e_y)=\operatorname{adj}\mathsf{M}_2(\vec e_x)\mathsf{M}_2(\vec e_y)
=\begin{pmatrix}0&i\\i&0\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}
=\begin{pmatrix}i&0\\0&-i\end{pmatrix}=-\mathsf{M}_2(\vec e_z),
$$

which is $\vec e_x\star \vec e_y=-\vec e_x\vec e_y=-\vec e_z$. The square of the product is the scalar matrix of the norm,

$$
\operatorname{adj}\mathsf{M}_2(\vec e_x)\,\mathsf{M}_2(\vec e_x)
=\begin{pmatrix}0&i\\i&0\end{pmatrix}\begin{pmatrix}0&-i\\-i&0\end{pmatrix}
=\begin{pmatrix}1&0\\0&1\end{pmatrix}=\langle \vec e_x\rangle_{\natural}I,
$$

which is $\mathsf{M}_2(\vec e_x\star \vec e_x)$ with $\langle \vec e_x\rangle_{\natural}=1$.

**The form, entry by entry.** The general quaternionic bilinear form is the adjugated trace pairing $\tfrac12\operatorname{Tr}(X\operatorname{adj}Y)$, and at the pair $\vec e_x,\vec e_x$ the trace reads the unit, $\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_2(\vec e_x)\mathsf{M}_2(\vec e_x))=\tfrac12\operatorname{Tr}I=1=\langle \vec e_x,\vec e_x\rangle_{\natural}$.

**The four words.** The twelve operations of the two chapters are built from four products, and each product is a word in the two matrices $X=\mathsf{M}_2(\tilde Q_1)$ and $Y=\mathsf{M}_2(\tilde Q_2)$ and in the two involutions of the model, the adjugate and the conjugate transpose:

| product | first slot | second slot | the word |
|---|---|---|---|
| general plain | $X$ | $Y$ | $XY$ |
| general quaternionic | $\operatorname{adj}X$ | $Y$ | $\operatorname{adj}X\,Y$ |
| general plain sesquilinear | $X$ | $Y^{\dagger}$ | $XY^{\dagger}$ |
| general quaternionic sesquilinear | $\operatorname{adj}X$ | $Y^{\dagger}$ | $\operatorname{adj}X\,Y^{\dagger}$ |

The symmetric part of a product is the half-sum of its word and of the word with the two slots exchanged, and the antisymmetric part is the half-difference.

**The four traces.** The four products are four matrix traces, and the four forms of the algebra are read from them:

$$
\tfrac12\operatorname{Tr}(XY)=\langle\tilde Q_1,\tilde Q_2\rangle,\qquad
\tfrac12\operatorname{Tr}(\operatorname{adj}X\,Y)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural},\qquad
\tfrac12\operatorname{Tr}(XY^{\dagger})=\langle\tilde Q_1,\tilde Q_2\rangle_{*},\qquad
\tfrac12\operatorname{Tr}(\operatorname{adj}X\,Y^{\dagger})=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*},
$$

the plain, the quaternionic, the Hermitian and the Krein form, in the two slots the table of the words prescribes.

## Summary

The $2\times2$ realization turns the natural conjugation into the adjugate and the quaternionic product into the adjugated matrix product, $\mathsf{M}_2(\tilde Q_1\star\tilde Q_2)=\operatorname{adj}\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2)$, with square the scalar matrix of the determinant, $\mathsf{M}_2(\tilde Q_2\star\tilde Q_2)=\langle\tilde Q_2\rangle_{\natural}I$. The adjugate reverses the order, $\operatorname{adj}(AB)=\operatorname{adj}(B)\operatorname{adj}(A)$, which is why the product is not associative: the associator is $\bigl(\operatorname{adj}(B)A-\operatorname{adj}(BA)\bigr)C$. The determinant of a value is the product of the norms, $\det \mathsf{M}_2(\tilde Q_1\star\tilde Q_2)=\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}\langle\tilde Q_2,\tilde Q_2\rangle_{\natural}$, and its trace is twice the symmetrisation coefficient, $\operatorname{Tr}\mathsf{M}_2(\tilde Q_1\star\tilde Q_2)=2\beta(\tilde Q_1,\tilde Q_2)$; the symmetrised product is the scalar matrix $\beta(\tilde Q_1,\tilde Q_2)I$, and the left multiplications are the multiplications by the adjugates, forming the opposite monoid. The general quaternionic bilinear form of the group is the adjugated trace pairing $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde Q_1)\operatorname{adj}\mathsf{M}_2(\tilde Q_2))$, whose diagonal is the determinant, whose coefficient Gram matrix is the identity $I_4$, of real signature $(4,4)$, whose null set is the cone of singular matrices of real dimension $6$, and whose automorphism group is $O_4(\mathbb{C})$ on the coefficients and the split group $O(4,4)$ on the realification. The units are the matrices of non-zero determinant, the group $SL_2(\mathbb{C})$ is the norm-one slice, and the idempotents are $0$ and $e_t$ alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2(\tilde Q_2)$ | the $2\times2$ matrix of the realization, $\operatorname{Tr}\mathsf{M}_2(\tilde Q_2)=2Q_{2t}$, $\det \mathsf{M}_2(\tilde Q_2)=\langle\tilde Q_2\rangle_{\natural}$ |
| $\mathsf{M}_2(\tilde Q_2^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde Q_2)$ | the natural conjugation is the adjugate |
| $\operatorname{adj}(AB)=\operatorname{adj}(B)\operatorname{adj}(A)$ | the adjugate reverses the order |
| $\mathsf{M}_2(\tilde Q_1\star\tilde Q_2)=\operatorname{adj}\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2)$ | the quaternionic product is the adjugated matrix product |
| $\operatorname{Tr}\mathsf{M}_2(\tilde Q_1\star\tilde Q_2)=2\beta(\tilde Q_1,\tilde Q_2)$, $\det \mathsf{M}_2(\tilde Q_1\star\tilde Q_2)=\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}\langle\tilde Q_2,\tilde Q_2\rangle_{\natural}$ | the trace and the determinant of a value |
| $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde Q_1)\operatorname{adj}\mathsf{M}_2(\tilde Q_2))=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$ | the general quaternionic bilinear form |
| $I_4$, split of signature $(4,4)$ | the coefficient Gram matrix and the real signature |
| $\det \mathsf{M}_2(\tilde Q_2)=0$ | the null set, the singular matrices, of real dimension $6$ |

## Further Reading

- Israel M. Gelfand, *Lectures on Linear Algebra* (Dover, 1989), for the trace, the determinant and the adjugate of a two-by-two matrix.
- Werner Greub, *Linear Algebra* (Springer, fourth edition, 1975), for the transpose as an anti-automorphism of an endomorphism algebra and its order reversal.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the identification of a full matrix algebra with its endomorphism algebra and for the structure of its units and its singular elements.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the two conjugations of an algebra, the transpose and the Hermitian transpose, and the distinction between them.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the description of a split algebra by matrices, with the reduced norm as the determinant and the reduced trace as the trace.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the reading of a twisted product as a product with an anti-automorphism inserted and the defect of its associativity.
- [Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions](introduction-to-the-2x2-matrix-element-representation-of-biquaternions.html), for the realization and its first properties
- [Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions](introduction-to-the-2x2-matrix-element-representation-of-biquaternions.html), for the further reading of the isomorphism
- [Introduction to the General Quaternionic Algebra](introduction-to-the-general-quaternionic-algebra.html), for the quaternionic product on the algebra
- [The 4 Forms over the Biquaternion $\mathbb{C}$ Space](the-4-forms-over-the-biquaternion-c-space.html), for the form on the algebra
- [The General Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$](the-general-quaternionic-algebra-in-the-4x4-matrix-element-representation.html), for the companion reading of the group
- [Remarkable Subspaces under the General Quaternionic Algebra](remarkable-subspaces-under-the-general-quaternionic-algebra.html), for the restriction theory of the form
