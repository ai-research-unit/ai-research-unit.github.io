
# __The General Quaternionic Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$__

## Introduction

The left regular representation $\mathsf{M}_4$ of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* carries the two conjugations of the algebra as two matrix operations: the natural conjugation is the **transposition**, $\mathsf{M}_4(\tilde Q^{\natural})=\mathsf{M}_4(\tilde Q)^{\mathsf{T}}$, and the Hermitian conjugation is the **conjugate transpose**, $\mathsf{M}_4(\tilde Q^{*})=\mathsf{M}_4(\tilde Q)^{\dagger}$. This article is the companion of *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, and it reads the group *Topology on the Introduction to the General Quaternionic Sesqualgebra of Biquaternions* on the regular matrices: the general quaternionic sesquilinear product becomes the transposed conjugate-transposed product, and the Krein form becomes the adjugated conjugate-transpose pairing of the regular matrices, of signature $(2,6)$ and with the adjugate appearing as the scalar factor $\langle\tilde Q\rangle_{\natural}$.

The regular representation has the advantage that the transposition is the operation it already carries, so the fundamental symmetry $J={}^{\natural}$ needs no adjugate here: it is the plain transposition of the regular matrix. The adjugate appears only in the form, where it contributes the factor $\langle\tilde Q\rangle_{\natural}$, and on the norm-one slice that factor is one and the pairing is exactly twice the general quaternionic sesquilinear form.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t$ the identity and $\vec e_k^2=-e_t$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; scalar part $\mathrm{Sc}$, sign matrix $E=\operatorname{diag}(1,-1,-1,-1)$; natural conjugation ${}^{\natural}$ negating $\vec e_x,\vec e_y,\vec e_z$, Hermitian conjugation ${}^{*}={}^{\natural}\circ\bar{\cdot}$; product $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*}$.

## The Representation

**Definition.** The **left regular matrix** is the isomorphism written $\mathsf{M}_4$. It converts a biquaternion into a $4 \times 4$ complex matrix,

$$
\mathsf{M}_4:\mathbb{B}\longrightarrow M_4(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity: in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ its $m$-th column is the coordinate column of the product $\tilde{Q}e_m$. It satisfies

$$
\mathsf{M}_4(\tilde{Q}^{\natural})=\mathsf{M}_4(\tilde{Q})^{\mathsf{T}},\qquad \mathsf{M}_4(\tilde{Q}^{*})=\mathsf{M}_4(\tilde{Q})^{\dagger},\qquad \operatorname{Tr}\mathsf{M}_4(\tilde{Q})=4Q_t,\qquad \det\mathsf{M}_4(\tilde{Q})=\langle\tilde{Q}\rangle_{\natural}^2 ,
$$

so the model carries the natural conjugation as the transposition and the Hermitian conjugation as the conjugate transpose.

## The General Quaternionic Sesquilinear Product in the Regular Representation

**Theorem (the transposed conjugate-transposed product).** For all biquaternions,

$$
\mathsf{M}_4(\tilde Q_1\star\tilde Q_2)=\mathsf{M}_4(\tilde Q_1)^{\mathsf{T}}\,\mathsf{M}_4(\tilde Q_2)^{\dagger} ,
$$

the product of the transposed first factor with the conjugate-transposed second factor.

*Proof.* $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*}$, the representation is multiplicative, and it carries the two conjugations to the transposition and the conjugate transpose.

**The fundamental symmetry.** The natural conjugation $J={}^{\natural}$ is the transposition on the regular matrices, $\mathsf{M}_4(\tilde{Q}^{\natural})=\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}$; it is an involution, it is self-adjoint for the Krein form, and its two eigenspaces are the Hermitian and anti-Hermitian subspaces, carried to the symmetric and antisymmetric parts of the regular matrix. The $J$-unitary operators are characterised in the coefficient basis by $\mathsf{M}_4(\tilde{Q})^{*}E\mathsf{M}_4(\tilde{Q})=E$.

## The General Quaternionic Sesquilinear Form in the Regular Representation

**Theorem (the adjugated conjugate-transpose pairing of the regular matrices).** For all biquaternions,

$$
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf{M}_4(\tilde Q_1)^{\dagger}\mathsf{M}_4(\tilde Q_2)\bigr) = 2\,\overline{\langle\tilde Q_1\rangle_{\natural}}\,\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*} ,
$$

the general quaternionic sesquilinear form of the algebra multiplied by twice the conjugate of the norm.

*Proof.* $\operatorname{adj}\mathsf{M}_4(\tilde Q_1)=\langle\tilde Q_1\rangle_{\natural}\mathsf{M}_4(\tilde Q_1^{\natural})$ because $\det\mathsf{M}_4(\tilde Q_1)=\langle\tilde Q_1\rangle_{\natural}^2$ and $\mathsf{M}_4(\tilde Q_1)^{-1}=\mathsf{M}_4(\tilde Q_1^{\natural})/\langle\tilde Q_1\rangle_{\natural}$; taking conjugate transposes and multiplying gives $\operatorname{adj}\mathsf{M}_4(\tilde Q_1)^{\dagger}\mathsf{M}_4(\tilde Q_2)=\overline{\langle\tilde Q_1\rangle_{\natural}}\,\mathsf{M}_4(\tilde Q_1^{\natural})\mathsf{M}_4(\tilde Q_1)^{\dagger}\mathsf{M}_4(\tilde Q_2)$, and the trace identity $\operatorname{Tr}\mathsf{M}_4(\tilde Q_1)=4\,\mathrm{Sc}(\tilde Q_1)$ gives the stated factor.

**Corollary (the norm-one slice).** On the group $\langle\cdot\rangle_{\natural}=1$ the identity is $\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_4(\tilde Q_1)^{\dagger}\mathsf{M}_4(\tilde Q_2))=2\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$, exactly twice the general quaternionic sesquilinear form, as in the $2\times2$ representation.

**The diagonal and the signature.** On the diagonal the factor is $\overline{\langle\tilde{Q}\rangle_{\natural}}$, so the form is $\sum_\mu\varepsilon_\mu|Q_\mu|^2$ up to that factor; it has complex inertia $(1,3)$ and real signature $(2,6)$ on the coefficient space, and its isotropic set is the real cone $\sum_\mu\varepsilon_\mu|Q_\mu|^2=0$, of real dimension $7$, distinct from the set of singular regular matrices.

**The automorphism group.** The form is the general quaternionic sesquilinear form of signature $(1,3)$, so its automorphism group is $\mathrm{U}(1,3)$; the operators that preserve it are the $J$-unitary operators of *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*, and the realification has automorphism group $O(2,6)$.

## Worked Examples

**The identity.** Let $\tilde{Q}=e_t$. Then $\mathsf{M}_4(e_t)=I_4$, $\operatorname{adj}I_4=I_4$ and $\langle e_t\rangle_{\natural}=1$, so the identity reads $\tfrac12\operatorname{Tr}(I_4)=2=2\langle e_t,e_t\rangle_{\natural*}$.

**A transposed element.** Let $\tilde{Q}=\vec e_x$. Then $\mathsf{M}_4(\vec e_x)^{\mathsf{T}}=\mathsf{M}_4(\vec e_x^{\natural})=-\mathsf{M}_4(\vec e_x)$, so the transposition is realised as a sign change, and $\langle \vec e_x,\vec e_x\rangle_{\natural*}=-1$.

**A Krein-isotropic unit.** Let $\tilde{Q}=e_t+\vec e_x$. Then $\langle\tilde{Q}\rangle_{\natural}=2\neq0$, so $\tilde{Q}$ is a unit and the regular matrix is invertible, while $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1-1=0$: the element is isotropic for the Krein form and a unit, which the general plain sesquilinear form of the other group does not allow.

## The Matrices

**The generators.** The regular model is fixed on the basis by four matrices:

$$
\mathsf{M}_4(e_t)=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
\mathsf{M}_4(\vec e_x)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
$$
$$
\mathsf{M}_4(\vec e_y)=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
\mathsf{M}_4(\vec e_z)=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

A general element is the block matrix

$$
\mathsf{M}_4(\tilde Q)=\begin{pmatrix}A&B\\-B&A\end{pmatrix},\qquad
A=\begin{pmatrix}Q_t&-Q_x\\Q_x&Q_t\end{pmatrix},\qquad
B=\begin{pmatrix}-Q_y&-Q_z\\-Q_z&Q_y\end{pmatrix},
$$

The general element has trace $4Q_t$ and determinant $\langle\tilde Q\rangle_{\natural}^2$.

**The two conjugations, entry by entry.** The transposition and the conjugate transpose agree on the real vector units, which are traceless and anti-Hermitian, $\mathsf{M}_4(\vec e_x)^{\mathsf T}=-\mathsf{M}_4(\vec e_x)=\mathsf{M}_4(\vec e_x)^{\dagger}$; they separate in general, $\mathsf{M}_4(\tilde Q)^{\mathsf T}=\mathsf{M}_4(\tilde Q^{\natural})$ against $\mathsf{M}_4(\tilde Q)^{\dagger}=\mathsf{M}_4(\tilde Q^{*})$, that is $X^{\mathsf T}=\tfrac12(\operatorname{Tr}X)I_4-X$ against the conjugate of that expression.

**The product, entry by entry.** The product is the transposed conjugate-transposed product, and at the pair $\vec e_x,\vec e_y$ the two sign changes cancel,

$$
\mathsf{M}_4(\vec e_x\star \vec e_y)=\mathsf{M}_4(\vec e_x)^{\mathsf T}\mathsf{M}_4(\vec e_y)^{\dagger}
=(-\mathsf{M}_4(\vec e_x))(-\mathsf{M}_4(\vec e_y))=\mathsf{M}_4(\vec e_x)\mathsf{M}_4(\vec e_y)=\mathsf{M}_4(\vec e_z),
$$

which is $\vec e_x\star \vec e_y=\vec e_x^{\natural}\vec e_y^{*}=(-\vec e_x)(-\vec e_y)=\vec e_z$, as in the realization.

**The product of a unit with the identity, entry by entry.** The identity is a right unit and not a left one, $I_4\star Y=Y^{\dagger}$ against $Y\star I_4=Y$, and at $Y=\mathsf{M}_4(\vec e_x)$ the left action returns the negative, $\mathsf{M}_4(\vec e_x)^{\dagger}=-\mathsf{M}_4(\vec e_x)$.

**The four words.** The four general products are the four ways of inserting the two conjugations into the two slots of the matrix product, and each is a word in the two regular matrices $X=\mathsf{M}_4(\tilde Q_1)$, $Y=\mathsf{M}_4(\tilde Q_2)$:

| product | first slot | second slot | the word |
|---|---|---|---|
| plain | $X$ | $Y$ | $XY$ |
| general quaternionic | $X^{\mathsf T}$ | $Y$ | $X^{\mathsf T}Y$ |
| general plain sesquilinear | $X$ | $Y^{\dagger}$ | $XY^{\dagger}$ |
| general quaternionic sesquilinear | $X^{\mathsf T}$ | $Y^{\dagger}$ | $X^{\mathsf T}Y^{\dagger}$ |

the transposition replacing the adjugate of the realization and the fourth word carrying one transposition and one conjugate transpose.

**The form, entry by entry.** The form is the adjugated conjugate-transpose pairing of the regular matrices, $\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf{M}_4(\tilde Q_1)^{\dagger}\mathsf{M}_4(\tilde Q_2)\bigr)=2\overline{\langle\tilde Q_1\rangle_{\natural}}\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$, and at the pair $\vec e_x,\vec e_x$, where the norm is one, it reads $\tfrac12\operatorname{Tr}(\mathsf{M}_4(\vec e_x)\mathsf{M}_4(\vec e_x))=\tfrac12\operatorname{Tr}(-I_4)=-2=2\langle \vec e_x,\vec e_x\rangle_{\natural*}$, the factor two being the ratio of the traces of the two models.

## Summary

The left regular representation carries the natural conjugation as the transposition and the Hermitian conjugation as the conjugate transpose, so the general quaternionic sesquilinear product is the transposed conjugate-transposed product $\mathsf{M}_4(\tilde Q_1\star\tilde Q_2)=\mathsf{M}_4(\tilde Q_1)^{\mathsf{T}}\mathsf{M}_4(\tilde Q_2)^{\dagger}$, whose fundamental symmetry is the plain transposition. The general quaternionic sesquilinear form of the group is the adjugated conjugate-transpose pairing $\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_4(\tilde Q_1)^{\dagger}\mathsf{M}_4(\tilde Q_2))=2\overline{\langle\tilde Q_1\rangle_{\natural}}\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$, which on the norm-one slice is exactly twice the form; it has complex inertia $(1,3)$ and real signature $(2,6)$, its isotropic set is the real cone of real dimension $7$, and its automorphism group is the indefinite unitary group $\mathrm{U}(1,3)$, of realification $O(2,6)$. The invariants of the regular matrix are the trace $4Q_t$ and the determinant $\langle\tilde Q\rangle_{\natural}^2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde{Q})$ | the $4\times4$ regular matrix, $\operatorname{Tr}\mathsf{M}_4(\tilde{Q})=4Q_t$, $\det\mathsf{M}_4(\tilde{Q})=\langle\tilde{Q}\rangle_{\natural}^2$ |
| $\mathsf{M}_4(\tilde{Q}^{\natural})=\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}$ | the natural conjugation is the transposition, the fundamental symmetry |
| $\mathsf{M}_4(\tilde Q_1\star\tilde Q_2)=\mathsf{M}_4(\tilde Q_1)^{\mathsf{T}}\mathsf{M}_4(\tilde Q_2)^{\dagger}$ | the general quaternionic sesquilinear product |
| $\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_4(\tilde Q_1)^{\dagger}\mathsf{M}_4(\tilde Q_2))=2\overline{\langle\tilde Q_1\rangle_{\natural}}\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$ | the general quaternionic sesquilinear form on the regular matrices |
| $(1,3)$ over $\mathbb{C}$, $(2,6)$ over $\mathbb{R}$ | the inertia and the real signature |
| $\mathrm{U}(1,3)$, $O(2,6)$ | the automorphism group and its realification |

## Further Reading

- [Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions](introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html), for the representation and its first properties
- [Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions](introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html), for the further reading of the regular representation
- [The Krein Gram Matrix and the Restrictions of the Form](the-krein-gram-matrix-and-the-restrictions-of-the-form.html), for the form on the algebra
- [J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra](j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra.html), for the operators of the form
- [The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$](the-general-quaternionic-sesqualgebra-in-the-2x2-matrix-element-representation.html), for the companion reading of the group
- [Remarkable Subspaces under the General Quaternionic Sesqualgebra](remarkable-subspaces-under-the-general-quaternionic-sesqualgebra.html), for the restriction theory of the form
