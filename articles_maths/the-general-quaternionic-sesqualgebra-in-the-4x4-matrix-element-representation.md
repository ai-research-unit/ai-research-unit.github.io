# __The General Quaternionic Sesqualgebra in the $4\times4$ Left Regular Representation $\mathbb{B}_L$__

## Introduction

The left regular representation carries the two conjugations of the algebra as two matrix operations. In the canonical frame of *Conventions in Mathematics*, §*The Matrix Models*, the natural conjugation is the signed reversal
$$
\mathsf M_4^{L}(\tilde Q^{\natural})=C\,\mathsf M_4^{L}(\tilde Q)^{\mathsf T}C^{-1},\qquad C=-\sigma_2\otimes\sigma_2,
$$
and the Hermitian conjugation is the conjugate transpose, $\mathsf M_4^{L}(\tilde Q^{*})=\mathsf M_4^{L}(\tilde Q)^{\dagger}$. This article is the companion of *$M_2(\mathbb C)$ Representation : The General Quaternionic Sesqualgebra of Biquaternions*, and it reads the group on the regular matrices: the general quaternionic sesquilinear product becomes $C X_1^{\mathsf T}C^{-1}X_2^{\dagger}$, and the general quaternionic sesquilinear form becomes the trace of the adjugated product.

The regular matrix is block diagonal, $I_2\otimes\mathsf M_2(\tilde Q)$. The adjugate is the norm times the natural conjugate, $\operatorname{adj}X=\langle\tilde Q\rangle_{\natural}C X^{\mathsf T}C^{-1}$, so the adjugate carries the factor of the norm in the form and disappears from it on the norm-one slice.

**Conventions.** The algebra is $\mathbb B=\mathbb C\otimes_{\mathbb R}\mathbb H$, with $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ and $\mathsf M_2(\tilde Q)=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}$. The natural conjugation is ${}^{\natural}$, the coefficientwise conjugation is $\bar{\cdot}$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The Krein form is $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$.

**Boundaries.** The representation is *$M_4(\mathbb C)$ Model : The Product, the Trace and the Determinant*; the operator reading is *Two-Sided Operators on the Biquaternion Algebra*. The $2\times2$ companion is *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation*; the form is *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the operators are *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*.

## The Representation

**Definition.** The left regular matrix is fixed by the multiplication in the canonical Peirce frame $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$:
$$
\mathsf M_4^{L}(\tilde Q)=I_2\otimes\mathsf M_2(\tilde Q)
=\begin{pmatrix}A&0\\0&A\end{pmatrix},\qquad A=\mathsf M_2(\tilde Q),
$$
and the right regular matrix is $\mathsf M_4^{R}(\tilde Q)=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$. It satisfies
$$
\mathsf M_4^{L}(\tilde Q^{\natural})=C\,\mathsf M_4^{L}(\tilde Q)^{\mathsf T}C^{-1},\qquad
\mathsf M_4^{L}(\tilde Q^{*})=\mathsf M_4^{L}(\tilde Q)^{\dagger},
$$
$$
\operatorname{Tr}\mathsf M_4^{L}(\tilde Q)=4Q_t,\qquad
\det\mathsf M_4^{L}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^{2}.
$$
The first line is the pair of conjugations, the second the two invariants. The natural conjugation is not the plain transpose in this frame; it is the transpose followed by the signed reversal $C$ of the four Peirce coordinates.

**The adjugate.** The inverse of an invertible regular matrix is $\mathsf M_4^{L}(\tilde Q)^{-1}=\mathsf M_4^{L}(\tilde Q^{\natural})/\langle\tilde Q\rangle_{\natural}$, so
$$
\operatorname{adj}\mathsf M_4^{L}(\tilde Q)=\langle\tilde Q\rangle_{\natural}\,\mathsf M_4^{L}(\tilde Q^{\natural})
=\langle\tilde Q\rangle_{\natural}\,C\,\mathsf M_4^{L}(\tilde Q)^{\mathsf T}C^{-1}.
$$
The adjugate is the natural conjugate multiplied by the norm; this is the regular form of the identity $\operatorname{adj}\mathsf M_2(\tilde Q)=\mathsf M_2(\tilde Q^{\natural})$ of the $2\times2$ model.

## The General Quaternionic Sesquilinear Product in the Regular Representation

**Theorem (the carried sesquilinear product).** For all biquaternions,
$$
\boxed{\;\mathsf M_4^{L}(\tilde Q_1\star\tilde Q_2)
=C\,\mathsf M_4^{L}(\tilde Q_1)^{\mathsf T}C^{-1}\,\mathsf M_4^{L}(\tilde Q_2)^{\dagger}\;}
$$
where $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*}$.

*Proof.* The representation is multiplicative, carries ${}^{\natural}$ to $C(\cdot)^{\mathsf T}C^{-1}$ and ${}^{*}$ to the dagger, so the image of $\tilde Q_1^{\natural}\tilde Q_2^{*}$ is the displayed word. $\square$

**The fundamental symmetry.** The natural conjugation $J={}^{\natural}$ is an involution commuting with the complex coefficients. It is the fundamental symmetry of the Krein form: its $+1$ eigenspace is the complex scalar line, of real dimension $2$, and its $-1$ eigenspace is the vector subspace, of real dimension $6$. On the regular matrices the same involution is $X\mapsto C X^{\mathsf T}C^{-1}$, and the two eigenspaces are the scalar matrices and the traceless part of the left copy. The $J$-unitary operators are the isometries of the Krein form, the group $\mathrm U(1,3)$ of *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*.

**The identity.** The identity matrix is neither a left nor a right unit of this product. At $\tilde Q_2=e_t$ the product is $\tilde Q_1^{\natural}$, and at $\tilde Q_1=e_t$ it is $\tilde Q_2^{*}$:
$$
I_4\star Y=Y^{\dagger},\qquad Y\star I_4=Y^{\natural}.
$$
The two agree exactly on the real elements, where the coefficientwise conjugation is the identity, and then both return $\tilde Q^{\natural}$.

## The General Quaternionic Sesquilinear Form in the Regular Representation

**Theorem (the trace of the adjugated product).** For all biquaternions,
$$
\boxed{\;\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf M_4^{L}(\tilde Q_1)\;\mathsf M_4^{L}(\tilde Q_2)^{\dagger}\bigr)
=2\,\langle\tilde Q_1\rangle_{\natural}\,\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}\;}
$$
the general quaternionic sesquilinear form multiplied by twice the algebraic norm of the first factor.

*Proof.* The adjugate is $\langle\tilde Q_1\rangle_{\natural}\mathsf M_4^{L}(\tilde Q_1^{\natural})$, and the dagger of the second factor is $\mathsf M_4^{L}(\tilde Q_2^{*})$. The product is $\langle\tilde Q_1\rangle_{\natural}\mathsf M_4^{L}(\tilde Q_1^{\natural}\tilde Q_2^{*})$, whose trace is $4\langle\tilde Q_1\rangle_{\natural}\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})=4\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$. Half of it is the statement. $\square$

**Corollary (the norm-one slice).** On $\langle\tilde Q_1\rangle_{\natural}=1$ the adjugate is the natural conjugate and the identity is
$$
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf M_4^{L}(\tilde Q_1)\mathsf M_4^{L}(\tilde Q_2)^{\dagger}\bigr)
=2\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*},
$$
exactly twice the form, as in the $2\times2$ model.

**The diagonal and the signature.** At the two equal arguments the factor is the norm and
$$
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf M_4^{L}(\tilde Q)\mathsf M_4^{L}(\tilde Q)^{\dagger}\bigr)
=2\langle\tilde Q\rangle_{\natural}\sum_\mu\varepsilon_\mu|Q_\mu|^{2},
$$
with $\varepsilon=(1,-1,-1,-1)$. The algebraic norm of the form is $\sum_\mu\varepsilon_\mu|Q_\mu|^{2}$, of complex inertia $(1,3)$ and real signature $(2,6)$; its isotropic set is the real cone $\sum_\mu\varepsilon_\mu|Q_\mu|^{2}=0$, of real dimension $7$. It is not the set of singular matrices: $e_t+\vec e_x$ is a unit and is isotropic.

**The automorphism group.** The form is of signature $(1,3)$ over $\mathbb C$, so its isometry group is the indefinite unitary group $\mathrm U(1,3)$, of real dimension $16$; its realification has automorphism group $O(2,6)$.

## Worked Examples

**The identity.** For $\tilde Q=e_t$, $\mathsf M_4^{L}(e_t)=I_4$, $\operatorname{adj}I_4=I_4$ and $\langle e_t\rangle_{\natural}=1$, so the identity reads $\tfrac12\operatorname{Tr}(I_4)=2=2\langle e_t,e_t\rangle_{\natural*}$.

**A vector unit.** For $\tilde Q=\vec e_x$, $\mathsf M_4^{L}(\vec e_x)=-\sigma_1\otimes I_2$ is anti-Hermitian, so $\mathsf M_4^{L}(\vec e_x)^{\dagger}=-\mathsf M_4^{L}(\vec e_x)$ and $\operatorname{adj}\mathsf M_4^{L}(\vec e_x)=-\mathsf M_4^{L}(\vec e_x)$. Hence
$$
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}X\,X^{\dagger}\bigr)
=\tfrac12\operatorname{Tr}\bigl((-X)(-X)\bigr)=\tfrac12\operatorname{Tr}(X^{2})=-2=2\langle\vec e_x,\vec e_x\rangle_{\natural*},
$$
since $\langle\vec e_x\rangle_{\natural}=1$ and $\langle\vec e_x,\vec e_x\rangle_{\natural*}=-1$.

**A Krein-isotropic unit.** For $\tilde Q=e_t+\vec e_x$ the norm is $\langle\tilde Q\rangle_{\natural}=2$, so the element is a unit and the regular matrix is invertible, while $\langle\tilde Q,\tilde Q\rangle_{\natural*}=1-1=0$. The element is isotropic for the Krein form and invertible, which the general plain sesquilinear form does not allow.

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

**The two conjugations, entry by entry.** The natural conjugation is $C X^{\mathsf T}C^{-1}=2Q_tI_4-X$, and the Hermitian conjugation is $X^{\dagger}$. On the vector units the two agree, because such a matrix is anti-Hermitian and the carrier returns its negative:
$$
C\,\mathsf M_4^{L}(\vec e_x)^{\mathsf T}C^{-1}=-\mathsf M_4^{L}(\vec e_x)=\mathsf M_4^{L}(\vec e_x)^{\dagger}.
$$
They separate on a general element: the first is $\mathbb C$-linear and the second is conjugate-linear.

**The product, entry by entry.** At the pair $\vec e_x,\vec e_y$ the two sign changes cancel,
$$
\mathsf M_4^{L}(\vec e_x\star\vec e_y)=C\,X_x^{\mathsf T}C^{-1}X_y^{\dagger}
=(-X_x)(-X_y)=X_xX_y=\mathsf M_4^{L}(\vec e_z),
$$
which is $\vec e_x\star\vec e_y=\vec e_x^{\natural}\vec e_y^{*}=(-\vec e_x)(-\vec e_y)=\vec e_z$.

**The identity, entry by entry.** At $Y=\mathsf M_4^{L}(\vec e_x)$ the left action returns the conjugate transpose and the right action the natural conjugate,
$$
I_4\star Y=Y^{\dagger}=-Y,\qquad Y\star I_4=Y^{\natural}=-Y,
$$
so the two agree on this anti-Hermitian unit but not on a general element.

**The four words.** The four general products are four words in $X=\mathsf M_4^{L}(\tilde Q_1)$ and $Y=\mathsf M_4^{L}(\tilde Q_2)$:

| product | first slot | second slot | the word |
|---|---|---|---|
| plain | $X$ | $Y$ | $XY$ |
| general quaternionic | $C X^{\mathsf T}C^{-1}$ | $Y$ | $C X^{\mathsf T}C^{-1}Y$ |
| general plain sesquilinear | $X$ | $Y^{\dagger}$ | $XY^{\dagger}$ |
| general quaternionic sesquilinear | $C X^{\mathsf T}C^{-1}$ | $Y^{\dagger}$ | $C X^{\mathsf T}C^{-1}Y^{\dagger}$ |

The transposition is replaced by the carried transposition, and the fourth word carries one carrier and one conjugate transpose.

**The form, entry by entry.** The form is the trace of the adjugated product. At the pair $\vec e_x,\vec e_x$ the norm is one and
$$
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}X\,X^{\dagger}\bigr)
=\tfrac12\operatorname{Tr}(-I_4)=-2=2\langle\vec e_x,\vec e_x\rangle_{\natural*},
$$
the factor two being the ratio of the regular trace to the scalar part.

## Summary

In the canonical frame the left regular representation is $\mathsf M_4^{L}(\tilde Q)=I_2\otimes\mathsf M_2(\tilde Q)$, with trace $4Q_t$ and determinant $\langle\tilde Q\rangle_{\natural}^{2}$. The natural conjugation is $C\mathsf M_4^{L}(\tilde Q)^{\mathsf T}C^{-1}$ with $C=-\sigma_2\otimes\sigma_2$, and the Hermitian conjugation is the dagger. The general quaternionic sesquilinear product is the carried sesquilinear product $\mathsf M_4^{L}(\tilde Q_1\star\tilde Q_2)=C\mathsf M_4^{L}(\tilde Q_1)^{\mathsf T}C^{-1}\mathsf M_4^{L}(\tilde Q_2)^{\dagger}$, whose fundamental symmetry is $J={}^{\natural}$, with $+1$ eigenspace the complex scalar line and $-1$ eigenspace the vector subspace. The general quaternionic sesquilinear form is the trace of the adjugated product, $\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf M_4^{L}(\tilde Q_1)\mathsf M_4^{L}(\tilde Q_2)^{\dagger})=2\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$, which on the norm-one slice is twice the form; it has complex inertia $(1,3)$, real signature $(2,6)$, the real cone of real dimension $7$ as isotropic set, and automorphism group $\mathrm U(1,3)$, of realification $O(2,6)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf M_4^{L}(\tilde Q)=I_2\otimes\mathsf M_2(\tilde Q)$ | the regular matrix, $\operatorname{Tr}=4Q_t$, $\det=\langle\tilde Q\rangle_{\natural}^{2}$ |
| $C=-\sigma_2\otimes\sigma_2$ | the carrier of the natural conjugation |
| $\mathsf M_4^{L}(\tilde Q^{\natural})=C\mathsf M_4^{L}(\tilde Q)^{\mathsf T}C^{-1}$ | the natural conjugation, the fundamental symmetry $J$ |
| $\mathsf M_4^{L}(\tilde Q^{*})=\mathsf M_4^{L}(\tilde Q)^{\dagger}$ | the Hermitian conjugation |
| $\operatorname{adj}\mathsf M_4^{L}(\tilde Q)=\langle\tilde Q\rangle_{\natural}\mathsf M_4^{L}(\tilde Q^{\natural})$ | the adjugate |
| $\mathsf M_4^{L}(\tilde Q_1\star\tilde Q_2)=C\mathsf M_4^{L}(\tilde Q_1)^{\mathsf T}C^{-1}\mathsf M_4^{L}(\tilde Q_2)^{\dagger}$ | the general quaternionic sesquilinear product |
| $\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf M_4^{L}(\tilde Q_1)\mathsf M_4^{L}(\tilde Q_2)^{\dagger})=2\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$ | the general quaternionic sesquilinear form |
| $\mathrm U(1,3)$, $O(2,6)$ | the automorphism group and its realification |

## Further Reading

- [$M_4(\mathbb C)$ Model : The Product, the Trace and the Determinant](m4c-model-the-product-the-trace-and-the-determinant.html), for the representation and its first properties
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the operator reading
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the form on the algebra
- [J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra](j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra.html), for the operators of the form
- [$M_2(\mathbb C)$ Representation : The General Quaternionic Sesqualgebra of Biquaternions](the-general-quaternionic-sesqualgebra-in-the-2x2-matrix-element-representation.html), for the companion reading of the group
- [Remarkable Subspaces under the General Quaternionic Sesqualgebra](remarkable-subspaces-under-the-general-quaternionic-sesqualgebra.html), for the restriction theory of the form
