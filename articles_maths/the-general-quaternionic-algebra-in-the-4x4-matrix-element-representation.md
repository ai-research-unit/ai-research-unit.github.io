# __The General Quaternionic Algebra in the $4\times4$ Left Regular Representation__

## Introduction

The left regular representation reads the algebra acting on itself. In the canonical frame of *Conventions of the Matrix Models*, §*The Matrix Models*, the Peirce frame $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$, the matrix of left multiplication is block diagonal, $I_2\otimes\mathsf M_2(\tilde Q)$, and the natural conjugation ${}^{\natural}$ is the signed reversal of the four Peirce coordinates,
$$
\mathsf M_4^{L}(\tilde Q^{\natural})=C\,\mathsf M_4^{L}(\tilde Q)^{\mathsf T}C^{-1},\qquad C=-\sigma_2\otimes\sigma_2,
$$
not the plain transpose. This article is the companion of *$M_2(\mathbb C)$ Representation : The General Quaternionic Algebra of Biquaternions*, and it reads the group on the regular matrices: the quaternionic product becomes $C X_1^{\mathsf T}C^{-1}X_2$, and the general quaternionic bilinear form becomes the trace pairing with the same carrier.

The block form is the gain of the canonical frame. The regular matrix is two copies of the $2\times2$ matrix of the element, so the trace, the determinant and the form are read on the block, and the factor two of the module is explicit.

**Conventions.** The algebra is $\mathbb B=\mathbb C\otimes_{\mathbb R}\mathbb H$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$ and $\vec e_k^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb C$, and $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ is the algebraic norm. The $2\times2$ model is
$$
\mathsf M_2(\tilde Q)=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}.
$$
The involution $C$ is $C=-\sigma_2\otimes\sigma_2$; it satisfies $C^2=I_4$ and $C=C^{\dagger}$.

**Boundaries.** The representation and its first properties are *$M_4(\mathbb C)_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*; the operator reading of the same group is *Two-Sided Operators on the Biquaternion Algebra*. The $2\times2$ companion is *The General Quaternionic Algebra in the $2\times2$ Matrix Element Representation*. The form is *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

## The Representation

**Definition.** The **left regular matrix** $\mathsf M_4^{L}(\tilde Q)$ is the matrix of $x\mapsto\tilde Qx$ in the canonical frame; its $j$-th column is the coordinate column of $\tilde QP_j$, with $(P_1,P_2,P_3,P_4)=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$. Because the frame is the Peirce frame, the matrix is block diagonal:
$$
\boxed{\;\mathsf M_4^{L}(\tilde Q)=I_2\otimes\mathsf M_2(\tilde Q)
=\begin{pmatrix}A&0\\0&A\end{pmatrix},\qquad A=\mathsf M_2(\tilde Q)\;}
$$
The **right regular matrix** is the matrix of $x\mapsto x\tilde Q$,
$$
\mathsf M_4^{R}(\tilde Q)=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2 .
$$
The two families commute, $L_aR_b=R_bL_a$, because both send $x$ to $a\,x\,b$. The image $\mathbb B_L=\rho_L(\mathbb B)$ is a four-dimensional subalgebra of $M_4(\mathbb C)$ isomorphic to $\mathbb B$.

**The two involutions.** The natural conjugation is the carrier $C$ acting on the transpose, and the Hermitian conjugation is the conjugate transpose:
$$
\mathsf M_4^{L}(\tilde Q^{\natural})=C\,\mathsf M_4^{L}(\tilde Q)^{\mathsf T}C^{-1},\qquad
\mathsf M_4^{L}(\tilde Q^{*})=\mathsf M_4^{L}(\tilde Q)^{\dagger}.
$$
The first formula is the difference from the coefficient frame, where the natural conjugation is the plain transpose. The two frames are related by the change $S$ of *The Product, the Trace and the Determinant*, and $S$ does not preserve transposition, only the operator.

**The invariants.** The trace and the determinant read
$$
\operatorname{Tr}\mathsf M_4^{L}(\tilde Q)=4Q_t,\qquad
\det\mathsf M_4^{L}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^{2}.
$$
The trace is twice the trace $2Q_t$ of the block, and the determinant is the square of the determinant $\langle\tilde Q\rangle_{\natural}$ of the block, because the block occurs twice.

## The Quaternionic Product in the Regular Representation

**Theorem (the carried product).** For all biquaternions,
$$
\boxed{\;\mathsf M_4^{L}(\tilde Q_1\star\tilde Q_2)
=C\,\mathsf M_4^{L}(\tilde Q_1)^{\mathsf T}C^{-1}\,\mathsf M_4^{L}(\tilde Q_2)\;}
$$
where $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$.

*Proof.* The representation is multiplicative and carries ${}^{\natural}$ to $C(\cdot)^{\mathsf T}C^{-1}$, so $\mathsf M_4^{L}(\tilde Q_1^{\natural}\tilde Q_2)=C\mathsf M_4^{L}(\tilde Q_1)^{\mathsf T}C^{-1}\mathsf M_4^{L}(\tilde Q_2)$. $\square$

**The square.** At $\tilde Q_1=\tilde Q_2=\tilde Q$ the theorem gives
$$
\mathsf M_4^{L}(\tilde Q\star\tilde Q)=C\,\mathsf M_4^{L}(\tilde Q)^{\mathsf T}C^{-1}\,\mathsf M_4^{L}(\tilde Q)
=\mathsf M_4^{L}(\tilde Q^{\natural})\mathsf M_4^{L}(\tilde Q)=\langle\tilde Q\rangle_{\natural}I_4,
$$
because $\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$. The square of the product is therefore the scalar matrix of the norm, and taking determinants gives $\det\mathsf M_4^{L}(\tilde Q)^2=\langle\tilde Q\rangle_{\natural}^{4}$, in agreement with $\det\mathsf M_4^{L}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^{2}$.

**The two-sided structure.** The right multiplications commute with the left ones, so the sixteen products $T_{\mu\nu}=\mathsf M_4^{L}(e_\mu)\mathsf M_4^{R}(e_\nu)$ need no ordering convention. In the canonical frame the left copy is the block-diagonal family $I_2\otimes A$ and the right copy the block-scalar family $A^{\mathsf T}\otimes I_2$; they are mutual commutants, and their intersection is the scalars.

## The General Quaternionic Bilinear Form in the Regular Representation

**Theorem (the trace pairing).** For all biquaternions,
$$
\boxed{\;\tfrac12\operatorname{Tr}\bigl(\mathsf M_4^{L}(\tilde Q_1)\,C\,\mathsf M_4^{L}(\tilde Q_2)^{\mathsf T}C^{-1}\bigr)
=2\,\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}\;}
$$
so the trace pairing with the carrier in the second slot is twice the general quaternionic bilinear form of the algebra.

*Proof.* The carrier identity gives $C\mathsf M_4^{L}(\tilde Q_2)^{\mathsf T}C^{-1}=\mathsf M_4^{L}(\tilde Q_2^{\natural})$, hence the left-hand side is $\tfrac12\operatorname{Tr}\mathsf M_4^{L}(\tilde Q_1\tilde Q_2^{\natural})=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\natural})$. The scalar part is symmetric under ${}^{\natural}$ and cyclic, so $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\natural})=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$. $\square$

**The diagonal.** At $\tilde Q_1=\tilde Q_2=\tilde Q$,
$$
\tfrac12\operatorname{Tr}\bigl(\mathsf M_4^{L}(\tilde Q)\,C\,\mathsf M_4^{L}(\tilde Q)^{\mathsf T}C^{-1}\bigr)
=2\langle\tilde Q\rangle_{\natural}=2\det\mathsf M_2(\tilde Q),
$$
while $\det\mathsf M_4^{L}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^{2}$. The factor two is the dimension of the module: the regular trace is four times the scalar part, where the $2\times2$ trace is twice it.

**The Gram matrix and the signature.** In the coefficient basis the Gram matrix of the form is $I_4$; in the canonical frame it is the congruent matrix $S^{\mathsf T}I_4S$, and the signature of the realification is unchanged, $(4,4)$. The form is indefinite and non-degenerate.

**The null set.** The form vanishes exactly when $\langle\tilde Q\rangle_{\natural}=0$, that is when the block $\mathsf M_2(\tilde Q)$ is singular. The regular matrix then has rank at most two, and the null set is the zero-divisor cone, of real dimension $6$ in $\mathbb R^8$. It is not the null set of the plain form, which is $\{0\}$.

**The automorphisms.** The isometry group is the complex orthogonal group $O_4(\mathbb C)$, of complex dimension $6$, whose realification is the split group $O(4,4)$. The transposition-carrier $C(\cdot)^{\mathsf T}C^{-1}$ is an isometry, and the conjugations by the units form its inner part.

## Worked Examples

**The identity.** For $\tilde Q=e_t$, $\mathsf M_4^{L}(e_t)=I_4$ and $\tfrac12\operatorname{Tr}(I_4)=2=2\langle e_t\rangle_{\natural}$; also $\det\mathsf M_4^{L}(e_t)=1=\langle e_t\rangle_{\natural}^{2}$.

**A basis element.** For $\tilde Q=\vec e_x$,
$$
\mathsf M_4^{L}(\vec e_x)=-i\,I_2\otimes\sigma_1
=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},
$$
and $C\mathsf M_4^{L}(\vec e_x)^{\mathsf T}C^{-1}=-\mathsf M_4^{L}(\vec e_x)$. The product theorem at $\vec e_x\star\vec e_x=\vec e_x^{\natural}\vec e_x=-\vec e_x^{2}=e_t$ reads
$$
C\,X^{\mathsf T}C^{-1}X=(-X)X=-X^{2}=I_4,
$$
and $\langle\vec e_x\rangle_{\natural}=1$.

**A zero divisor.** For $\tilde Q=e_t+i\vec e_x$ the norm is $\langle\tilde Q\rangle_{\natural}=1+i^{2}=0$, so $\mathsf M_2(\tilde Q)=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ is singular, the regular matrix has rank two, and the pairing at the two equal arguments is zero. The element is isotropic for the quaternionic form, unlike its behaviour for the plain bilinear form.

## The Matrices

**The generators.** In the canonical frame the four units go to
$$
\mathsf M_4^{L}(e_t)=I_4,\qquad
\mathsf M_4^{L}(\vec e_x)=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},
$$
$$
\mathsf M_4^{L}(\vec e_y)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
\mathsf M_4^{L}(\vec e_z)=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix}.
$$
A general element is the block matrix
$$
\mathsf M_4^{L}(\tilde Q)=\begin{pmatrix}A&0\\0&A\end{pmatrix},\qquad
A=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix},
$$
with trace $4Q_t$ and determinant $\langle\tilde Q\rangle_{\natural}^{2}$.

**The involution, entry by entry.** The carrier $C$ is
$$
C=\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix},
$$
and the involution is the trace complement
$$
C\,X^{\mathsf T}C^{-1}=2Q_tI_4-X,
$$
because $X+\mathsf M_4^{L}(\tilde Q^{\natural})=\mathsf M_4^{L}(\tilde Q+\tilde Q^{\natural})=2Q_tI_4$. At the unit $\vec e_x$ the matrix is symmetric and the involution returns its negative, $C X^{\mathsf T}C^{-1}=-X=\mathsf M_4^{L}(\vec e_x^{\natural})$.

**The product, entry by entry.** At the pair $\vec e_x,\vec e_y$,
$$
\mathsf M_4^{L}(\vec e_x\star\vec e_y)=C\,X_x^{\mathsf T}C^{-1}X_y=(-X_x)X_y=-X_xX_y=-\mathsf M_4^{L}(\vec e_z),
$$
which is $\vec e_x\star\vec e_y=-\vec e_z$. The square is the scalar matrix of the norm,
$$
C\,X_x^{\mathsf T}C^{-1}X_x=(-X_x)X_x=-X_x^{2}=I_4=\langle\vec e_x\rangle_{\natural}I_4 .
$$

**The four words.** The four general products are four words in $X=\mathsf M_4^{L}(\tilde Q_1)$ and $Y=\mathsf M_4^{L}(\tilde Q_2)$:

| product | first slot | second slot | the word |
|---|---|---|---|
| general plain | $X$ | $Y$ | $XY$ |
| general quaternionic | $C X^{\mathsf T}C^{-1}$ | $Y$ | $C X^{\mathsf T}C^{-1}Y$ |
| general plain sesquilinear | $X$ | $Y^{\dagger}$ | $XY^{\dagger}$ |
| general quaternionic sesquilinear | $C X^{\mathsf T}C^{-1}$ | $Y^{\dagger}$ | $C X^{\mathsf T}C^{-1}Y^{\dagger}$ |

The symmetric part of a product is the half-sum of its word and of the word with the two slots exchanged, and the antisymmetric part is the half-difference.

**The four traces.** The four forms are the four traces:
$$
\tfrac14\operatorname{Tr}(XY)=\langle\tilde Q_1,\tilde Q_2\rangle,\qquad
\tfrac14\operatorname{Tr}(C X^{\mathsf T}C^{-1}Y)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural},
$$
$$
\tfrac14\operatorname{Tr}(XY^{\dagger})=\langle\tilde Q_1,\tilde Q_2\rangle_{*},\qquad
\tfrac14\operatorname{Tr}(C X^{\mathsf T}C^{-1}Y^{\dagger})=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*},
$$
the plain, the quaternionic, the Hermitian and the Krein form. The factor is $\tfrac14$ where the $2\times2$ model has $\tfrac12$, because the regular trace is four times the scalar part where the $2\times2$ trace is twice it.

## Summary

The left regular representation in the canonical frame is $\mathsf M_4^{L}(\tilde Q)=I_2\otimes\mathsf M_2(\tilde Q)$, with trace $4Q_t$ and determinant $\langle\tilde Q\rangle_{\natural}^{2}$. The natural conjugation is the signed reversal $\mathsf M_4^{L}(\tilde Q^{\natural})=C\mathsf M_4^{L}(\tilde Q)^{\mathsf T}C^{-1}$ with $C=-\sigma_2\otimes\sigma_2$, and the Hermitian conjugation is the conjugate transpose. The quaternionic product is the carried product $\mathsf M_4^{L}(\tilde Q_1\star\tilde Q_2)=C\mathsf M_4^{L}(\tilde Q_1)^{\mathsf T}C^{-1}\mathsf M_4^{L}(\tilde Q_2)$, whose square is the scalar matrix $\langle\tilde Q\rangle_{\natural}I_4$. The general quaternionic bilinear form is the trace pairing $\tfrac12\operatorname{Tr}(\mathsf M_4^{L}(\tilde Q_1)C\mathsf M_4^{L}(\tilde Q_2)^{\mathsf T}C^{-1})=2\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$; its diagonal is twice the algebraic norm, its realification has signature $(4,4)$, its null set is the zero-divisor cone of real dimension $6$, and its isometry group is $O_4(\mathbb C)$, of realification $O(4,4)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf M_4^{L}(\tilde Q)=I_2\otimes\mathsf M_2(\tilde Q)$ | the $4\times4$ left regular matrix, $\operatorname{Tr}=4Q_t$, $\det=\langle\tilde Q\rangle_{\natural}^{2}$ |
| $\mathsf M_4^{R}(\tilde Q)=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$ | the right regular matrix, the commuting partner |
| $C=-\sigma_2\otimes\sigma_2$ | the carrier of the natural conjugation, $C^2=I_4$, $C=C^{\dagger}$ |
| $\mathsf M_4^{L}(\tilde Q^{\natural})=C\mathsf M_4^{L}(\tilde Q)^{\mathsf T}C^{-1}$ | the natural conjugation |
| $\mathsf M_4^{L}(\tilde Q_1\star\tilde Q_2)=C\mathsf M_4^{L}(\tilde Q_1)^{\mathsf T}C^{-1}\mathsf M_4^{L}(\tilde Q_2)$ | the quaternionic product |
| $\tfrac12\operatorname{Tr}(\mathsf M_4^{L}(\tilde Q_1)C\mathsf M_4^{L}(\tilde Q_2)^{\mathsf T}C^{-1})=2\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$ | the general quaternionic bilinear form |
| $O_4(\mathbb C)$, $O(4,4)$ | the isometry group and its realification |

## Further Reading

- [$M_4(\mathbb C)_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant](m4c-model-the-product-the-trace-and-the-determinant.html), for the representation and its first properties
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the operator reading of the same group
- [Introduction to the General Quaternionic Algebra](introduction-to-the-general-quaternionic-algebra.html), for the quaternionic product on the algebra
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the form on the algebra
- [$M_2(\mathbb C)$ Representation : The General Quaternionic Algebra of Biquaternions](the-general-quaternionic-algebra-in-the-2x2-matrix-element-representation.html), for the companion reading of the group
- [Remarkable Subspaces under the General Quaternionic Algebra](remarkable-subspaces-under-the-general-quaternionic-algebra.html), for the restriction theory of the form
