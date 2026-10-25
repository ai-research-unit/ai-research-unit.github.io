# __The General Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$__

## Introduction

The left regular representation $\mathsf{M}_4$ of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* is built from the multiplication and carries the Hermitian conjugation as the **conjugate transpose**, $\mathsf{M}_4(\tilde{Q}^{*})=\mathsf{M}_4(\tilde{Q})^{\dagger}$, so it is a $*$-representation of the sesqualgebra. This article is the companion of *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, and it reads the group *Topology on the Introduction to the General Plain Sesqualgebra of Biquaternions* on the regular matrices: the sesquilinear product becomes the product with the conjugate-transposed second factor, and the general plain sesquilinear form becomes the Hilbert–Schmidt pairing of the regular matrices, positive definite, with the Frobenius norm as its carrier and a double cover of the Lorentz group as its algebraic content.

The regular representation adds one thing to the $2\times2$ reading: the positive definite form makes the Hermitian subspace a definite space on which the norm-one group acts, and that action is the two-to-one cover $SL_2(\mathbb{C})\to SO^{+}(1,3)$ of the identity component of the Lorentz group. The Frobenius norm of the regular matrix is twice the definite norm of the element.

## The Representation

**Definition.** The **left regular matrix** is the isomorphism written $\mathsf{M}_4$. It converts a biquaternion into a $4 \times 4$ complex matrix,

$$
\mathsf{M}_4:\mathbb{B}\longrightarrow M_4(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity: in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ its $m$-th column is the coordinate column of the product $\tilde{Q}e_m$. It satisfies

$$
\mathsf{M}_4(\tilde{Q})\mathsf{M}_4(\tilde{Q}_2)=\mathsf{M}_4(\tilde{Q}\tilde{Q}_2),\qquad \mathsf{M}_4(\tilde{Q}^{*})=\mathsf{M}_4(\tilde{Q})^{\dagger},\qquad \operatorname{Tr}\mathsf{M}_4(\tilde{Q})=4Q_t,\qquad \det\mathsf{M}_4(\tilde{Q})=\langle\tilde{Q}\rangle_{\natural}^2 ,
$$

so $\mathsf{M}_4$ is a $*$-representation for the Hermitian conjugation and the conjugate transpose.

## The Sesquilinear Product in the Regular Representation

**Theorem (the product is the conjugate-transposed product of the regular matrices).** For all biquaternions,

$$
\boxed{\; \mathsf{M}_4(\tilde{Q}\star\tilde{Q}_2)=\mathsf{M}_4(\tilde{Q})\,\mathsf{M}_4(\tilde{Q}_2)^{\dagger} \;},
$$

so the sesquilinear product is read on the regular matrices by conjugating and transposing the second factor and multiplying.

*Proof.* $\tilde{Q}\star\tilde{Q}_2=\tilde{Q}\tilde{Q}_2^{*}$, the representation is multiplicative, and $\mathsf{M}_4(\tilde{Q}^{*})=\mathsf{M}_4(\tilde{Q})^{\dagger}$ by the $*$-property.

**The square and the unit.** At $\tilde{Q}_2=\tilde{Q}$ the theorem gives the square $\mathsf{M}_4(\tilde{Q}\star\tilde{Q})=\mathsf{M}_4(\tilde{Q})\mathsf{M}_4(\tilde{Q})^{\dagger}$, a positive semidefinite matrix whatever $\tilde{Q}$ is, which is the matrix form of the fact that $\tilde{Q}\tilde{Q}^{*}$ is a sum of Hermitian squares; the identity matrix $I_4=\mathsf{M}_4(e_t)$ is a **right unit alone** of the product, its left action being the conjugate transpose.

**The units.** The units of the algebra are the elements of non-zero determinant, so under $\mathsf{M}_4$ their images form the group $\mathsf{M}_4(\mathbb{B}^{\times})\cong GL_2(\mathbb{C})$ inside $GL_4(\mathbb{C})$; the norm-one group $\{\tilde{A}:\langle\tilde{A},\tilde{A}\rangle_{\natural}=1\}$ is $SL_2(\mathbb{C})$, whose regular matrices have determinant one.

## The General Plain Sesquilinear Form in the Regular Representation

**Theorem (the Hilbert–Schmidt pairing of the regular matrices).** For all biquaternions,

$$
\boxed{\; \tfrac12\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde{Q})^{\dagger}\mathsf{M}_4(\tilde{Q}_2)\bigr) = 2\,\langle\tilde{Q}_2,\tilde{Q}\rangle_{*} \;},
$$

so the Hilbert–Schmidt pairing of the regular matrices is twice the general plain sesquilinear form of the algebra.

*Proof.* $\mathsf{M}_4(\tilde{Q})^{\dagger}=\mathsf{M}_4(\tilde{Q}^{*})$, so the left-hand side is $\tfrac12\operatorname{Tr}(\mathsf{M}_4(\tilde{Q}^{*}\tilde{Q}_2))=2\,\mathrm{Sc}(\tilde{Q}^{*}\tilde{Q}_2)=2\langle\tilde{Q}_2,\tilde{Q}\rangle_{*}$, using $\operatorname{Tr}\mathsf{M}_4(\tilde{Q})=4\,\mathrm{Sc}(\tilde{Q})$.

**Theorem (the Frobenius norm).** On the diagonal,

$$
\boxed{\; \lVert\mathsf{M}_4(\tilde{Q})\rVert_F^2=\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde{Q})^{\dagger}\mathsf{M}_4(\tilde{Q})\bigr)=4\sum_\mu|Q_\mu|^2=4\,\lVert\tilde{Q}\rVert_E^2 \;},
$$

so the Frobenius norm of the regular matrix is twice the definite norm of the element, and the Hilbert–Schmidt pairing reads the definite form of the algebra on the matrices.

**The signature and the null set.** The pairing is positive definite: on the sixteen complex coordinates of $M_4(\mathbb{C})$ it has signature $(32,0)$, and its null set is $\{0\}$ alone.

**The automorphism group.** The Hilbert–Schmidt pairing on $M_4(\mathbb{C})$ has automorphism group the unitary group $\mathrm{U}(16)$, of real dimension $256$; among these, the structure-preserving maps $X\mapsto UXV^{\dagger}$ form the subgroup $\mathrm{U}(4)\times \mathrm{U}(4)$ modulo the common centre, which is the part that also preserves the algebra structure.

**The two-sided action and the double cover.** The positive definite form makes the Hermitian subspace $\mathbb{M}_+$ a definite space of real dimension $4$, and the norm-one group $G=\{\tilde{A}:\langle\tilde{A}\rangle_{\natural}=1\}=SL_2(\mathbb{C})$ acts on it by $\tilde{Q}\mapsto\tilde{A}\tilde{Q}\tilde{A}^{*}$, preserving the determinant:

$$
\langle\tilde{A}\tilde{Q}\tilde{A}^{*},\tilde{A}\tilde{Q}\tilde{A}^{*}\rangle_{\natural}=\langle\tilde{Q},\tilde{Q}\rangle_{\natural},\qquad \tilde{A}\in G.
$$

The action defines the surjective homomorphism $SL_2(\mathbb{C})\to SO^{+}(1,3)$ with kernel $\{\pm e_t\}$, the two-to-one cover of the identity component of the orthogonal group of the restricted form; it is read on the module in *Modules over the Biquaternion Algebra*, and the group is *Biquaternion Rotations and Lorentz Transformations*.

**Proposition (the image is the identity component).** The image of the two-sided action is the identity component $SO^{+}(1,3)$.

*Proof.* The action $(\tilde{A},\tilde{Q})\mapsto\tilde{A}\tilde{Q}\tilde{A}^{*}$ has kernel $\{\pm e_t\}$ and its image is the subgroup of $SO^{+}(1,3)$ generated by the one-parameter families $\tilde{A}(t)=\exp(t\tilde{Q}_1)$, which are the rotations and boosts of the restricted form; the image is the whole identity component.

## Worked Examples

**The identity.** Let $\tilde{Q}=e_t$. Then $\mathsf{M}_4(e_t)=I_4$, $\lVert\mathsf{M}_4(e_t)\rVert_F^2=4=4\lVert e_t\rVert_E^2$, and $\tfrac12\operatorname{Tr}(I_4^{\dagger}I_4)=2=2\langle e_t,e_t\rangle_{*}$.

**A Hermitian element.** Let $\tilde{Q}=e_t+i\vec e_z$. Then $\tilde{Q}^{*}=\tilde{Q}$ and $\mathsf{M}_4(\tilde{Q})^{\dagger}=\mathsf{M}_4(\tilde{Q})$, so the regular matrix is Hermitian; the square is $\tilde{Q}\star\tilde{Q}=\tilde{Q}^2=e_t+2i\vec e_z+(i\vec e_z)^2=2e_t+2i\vec e_z=2\tilde{Q}$, a positive semidefinite element, and the pairing at the two equal arguments is $4\lVert\tilde{Q}\rVert_E^2=8$.

**A zero divisor.** Let $\tilde{Q}=e_t+i\vec e_x$. Then $\det\mathsf{M}_4(\tilde{Q})=\langle\tilde{Q}\rangle_{\natural}^2=0$ and the regular matrix is singular of rank two, while $\lVert\mathsf{M}_4(\tilde{Q})\rVert_F^2=4\lVert\tilde{Q}\rVert_E^2=8$: the element is a zero divisor and yet a definite one for the general plain sesquilinear form.

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

The general element has trace $4Q_t$ and determinant $\langle\tilde Q\rangle_{\natural}^2$, with the Hermitian conjugation carried to the conjugate transpose, $\mathsf{M}_4(\tilde Q^{*})=\mathsf{M}_4(\tilde Q)^{\dagger}$.

**The product, entry by entry.** A vector unit is anti-Hermitian, so $\mathsf{M}_4(\vec e_y)^{\dagger}=-\mathsf{M}_4(\vec e_y)$, and the product at the pair $\vec e_x,\vec e_y$ is

$$
\mathsf{M}_4(\vec e_x)\mathsf{M}_4(\vec e_y)^{\dagger}=-\mathsf{M}_4(\vec e_x)\mathsf{M}_4(\vec e_y)=-\mathsf{M}_4(\vec e_z),
$$

which is $\vec e_x\star \vec e_y=\vec e_x\vec e_y^{*}=-\vec e_z$, the relation $\vec e_x\vec e_y=\vec e_z$ and the anti-Hermiticity of $\vec e_y$ carrying the sign.

**The right unit, entry by entry.** The identity matrix is a right unit and not a left one, $I_4\star Y=Y^{\dagger}$ against $Y\star I_4=Y$; at $Y=\mathsf{M}_4(\vec e_x)$ the two differ, the left action returning the negative, $\mathsf{M}_4(\vec e_x)^{\dagger}=-\mathsf{M}_4(\vec e_x)\neq\mathsf{M}_4(\vec e_x)$.

**The Frobenius norm, entry by entry.** The regular matrix of a vector unit has four entries $\pm1$ and the remaining twelve zero, so $\lVert\mathsf{M}_4(\vec e_x)\rVert_F^2=4$, in agreement with the general $\lVert\mathsf{M}_4(\tilde Q)\rVert_F^2=4\sum_\mu\lvert Q_\mu\rvert^2$; the value of the square is the positive semidefinite matrix $\mathsf{M}_4(\tilde Q)\mathsf{M}_4(\tilde Q)^{\dagger}$.

## Summary

The left regular representation is a $*$-representation, $\mathsf{M}_4(\tilde{Q}^{*})=\mathsf{M}_4(\tilde{Q})^{\dagger}$, and it reads the sesquilinear product as the product with the conjugate-transposed second factor, $\mathsf{M}_4(\tilde{Q}\star\tilde{Q}_2)=\mathsf{M}_4(\tilde{Q})\mathsf{M}_4(\tilde{Q}_2)^{\dagger}$, whose square is always positive semidefinite. The general plain sesquilinear form of the group is the Hilbert–Schmidt pairing $\tfrac12\operatorname{Tr}(\mathsf{M}_4(\tilde{Q})^{\dagger}\mathsf{M}_4(\tilde{Q}_2))=2\langle\tilde{Q}_2,\tilde{Q}\rangle_{*}$, positive definite of signature $(32,0)$ on the matrices, with Frobenius norm $\lVert\mathsf{M}_4(\tilde{Q})\rVert_F=2\lVert\tilde{Q}\rVert_E$ and null set $\{0\}$; its automorphism group is $\mathrm{U}(16)$, whose algebra-preserving part is $\mathrm{U}(4)\times \mathrm{U}(4)$ modulo the centre. The two-sided action of the norm-one group $SL_2(\mathbb{C})$ on the Hermitian subspace gives the double cover $SL_2(\mathbb{C})\to SO^{+}(1,3)$, and the units of the algebra appear as the matrices of $GL_2(\mathbb{C})$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde{Q})$ | the $4\times4$ regular matrix, $\operatorname{Tr}\mathsf{M}_4(\tilde{Q})=4Q_t$ |
| $\mathsf{M}_4(\tilde{Q}^{*})=\mathsf{M}_4(\tilde{Q})^{\dagger}$ | the Hermitian conjugation is the conjugate transpose |
| $\mathsf{M}_4(\tilde{Q}\star\tilde{Q}_2)=\mathsf{M}_4(\tilde{Q})\mathsf{M}_4(\tilde{Q}_2)^{\dagger}$ | the sesquilinear product on the regular matrices |
| $\tfrac12\operatorname{Tr}(\mathsf{M}_4(\tilde{Q})^{\dagger}\mathsf{M}_4(\tilde{Q}_2))=2\langle\tilde{Q}_2,\tilde{Q}\rangle_{*}$ | the general plain sesquilinear form as the Hilbert–Schmidt pairing |
| $\lVert\mathsf{M}_4(\tilde{Q})\rVert_F=2\lVert\tilde{Q}\rVert_E$ | the Frobenius norm of the regular matrix |
| $SL_2(\mathbb{C})\to SO^{+}(1,3)$ | the double cover of the two-sided action on the Hermitian subspace |

## Further Reading

- [Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions](introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html), for the representation and its first properties
- [Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions](introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html), for the further reading of the regular representation
- [Introduction to the General Plain Sesqualgebra](introduction-to-the-general-plain-sesqualgebra.html), for the sesquilinear product on the algebra
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the form on the algebra
- [The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$](the-general-plain-sesqualgebra-in-the-2x2-matrix-element-representation.html), for the companion reading of the group
- [Remarkable Subspaces under the General Plain Sesqualgebra](remarkable-subspaces-under-the-general-plain-sesqualgebra.html), for the restriction theory of the form
