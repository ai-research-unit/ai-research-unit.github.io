
# __The General Plain Sesqualgebra in the $4\times4$ Matrix Representation__

## Introduction

The left regular representation $\mathsf{M}_4$ of *Introduction to the $4\times4$ Matrix Representation $M_4(\mathbb{C})_L$ of Biquaternions* is built from the multiplication and carries the Hermitian conjugation as the **conjugate transpose**, $\mathsf{M}_4(\tilde{Q}^{*})=\mathsf{M}_4(\tilde{Q})^{\dagger}$, so it is a $*$-representation of the sesqualgebra. This article is the companion of *The General Plain Sesqualgebra in the $2\times2$ Matrix Representation*, and it reads the group *Topology on the Introduction to the General Plain Sesqualgebra of Biquaternions* on the regular matrices: the sesquilinear product becomes the product with the conjugate-transposed second factor, and the general plain sesquilinear form becomes the Hilbert–Schmidt pairing of the regular matrices, positive definite, with the Frobenius norm as its carrier and a double cover of the Lorentz group as its algebraic content.

The regular representation adds one thing to the $2\times2$ reading: the positive definite form makes the Hermitian subspace a definite space on which the norm-one group acts, and that action is the two-to-one cover $SL_2(\mathbb{C})\to SO^{+}(1,3)$ of the identity component of the Lorentz group. The Frobenius norm of the regular matrix is twice the definite norm of the element.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity and $e_k^2=-e_0$; $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; scalar part $\mathrm{Sc}$; natural conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$, Hermitian conjugation ${}^{*}={}^{\natural}\circ\bar{\cdot}$; sesquilinear product $\tilde{P}\star\tilde{Q}=\tilde{P}\tilde{Q}^{*}$; sign matrix $E=\operatorname{diag}(1,-1,-1,-1)$. All matrix claims of this article are recomputed in the verification script of the pass.

## The Representation

**Definition.** The **left regular representation** is the algebra homomorphism $L_{\tilde{Q}}(\tilde{R})=\tilde{Q}\tilde{R}$, with $\mathsf{M}_4(\tilde{Q})$ the $4\times4$ matrix of left multiplication in the basis $e_0,e_1,e_2,e_3$. It satisfies

$$
\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q})=\mathsf{M}_4(\tilde{P}\tilde{Q}),\qquad \mathsf{M}_4(\tilde{Q}^{*})=\mathsf{M}_4(\tilde{Q})^{\dagger},\qquad \operatorname{Tr}\mathsf{M}_4(\tilde{Q})=4Q_0,\qquad \det\mathsf{M}_4(\tilde{Q})=N(\tilde{Q})^2 ,
$$

so $\mathsf{M}_4$ is a $*$-representation for the Hermitian conjugation and the conjugate transpose.

## The Sesquilinear Product in the Regular Representation

**Theorem (the product is the conjugate-transposed product of the regular matrices).** For all biquaternions,

$$
\mathsf{M}_4(\tilde{P}\star\tilde{Q})=\mathsf{M}_4(\tilde{P})\,\mathsf{M}_4(\tilde{Q})^{\dagger} ,
$$

so the sesquilinear product is read on the regular matrices by conjugating and transposing the second factor and multiplying.

*Proof.* $\tilde{P}\star\tilde{Q}=\tilde{P}\tilde{Q}^{*}$, the representation is multiplicative, and $\mathsf{M}_4(\tilde{Q}^{*})=\mathsf{M}_4(\tilde{Q})^{\dagger}$ by the $*$-property.

**The square and the unit.** At $\tilde{P}=\tilde{Q}$ the theorem gives the square $\mathsf{M}_4(\tilde{Q}\star\tilde{Q})=\mathsf{M}_4(\tilde{Q})\mathsf{M}_4(\tilde{Q})^{\dagger}$, a positive semidefinite matrix whatever $\tilde{Q}$ is, which is the matrix form of the fact that $\tilde{Q}\tilde{Q}^{*}$ is a sum of Hermitian squares; the identity matrix $I_4=\mathsf{M}_4(e_0)$ is a **right unit alone** of the product, its left action being the conjugate transpose.

**The units.** The units of the algebra are the elements of non-zero determinant, so under $\mathsf{M}_4$ their images form the group $\mathsf{M}_4(\mathbb{B}^{\times})\cong GL_2(\mathbb{C})$ inside $GL_4(\mathbb{C})$; the norm-one group $\{\tilde{A}:\langle\tilde{A},\tilde{A}\rangle_{\natural}=1\}$ is $SL_2(\mathbb{C})$, whose regular matrices have determinant one.

## The General Plain Sesquilinear Form in the Regular Representation

**Theorem (the Hilbert–Schmidt pairing of the regular matrices).** For all biquaternions,

$$
\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde{P})^{\dagger}\mathsf{M}_4(\tilde{Q})\bigr) = 2\,\langle\tilde{Q},\tilde{P}\rangle_{*} ,
$$

so the Hilbert–Schmidt pairing of the regular matrices is twice the general plain sesquilinear form of the algebra.

*Proof.* $\mathsf{M}_4(\tilde{P})^{\dagger}=\mathsf{M}_4(\tilde{P}^{*})$, so the left-hand side is $\tfrac12\operatorname{Tr}(\mathsf{M}_4(\tilde{P}^{*}\tilde{Q}))=2\,\mathrm{Sc}(\tilde{P}^{*}\tilde{Q})=2\langle\tilde{Q},\tilde{P}\rangle_{*}$, using $\operatorname{Tr}\mathsf{M}_4(\tilde{R})=4\,\mathrm{Sc}(\tilde{R})$.

**Theorem (the Frobenius norm).** On the diagonal,

$$
\lVert\mathsf{M}_4(\tilde{Q})\rVert_F^2=\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde{Q})^{\dagger}\mathsf{M}_4(\tilde{Q})\bigr)=4\sum_\mu|Q_\mu|^2=4\,\lVert\tilde{Q}\rVert_E^2 ,
$$

so the Frobenius norm of the regular matrix is twice the definite norm of the element, and the Hilbert–Schmidt pairing reads the definite form of the algebra on the matrices.

**The signature and the null set.** The pairing is positive definite: on the sixteen complex coordinates of $M_4(\mathbb{C})$ it has signature $(32,0)$, and its null set is $\{0\}$ alone.

**The automorphism group.** The Hilbert–Schmidt pairing on $M_4(\mathbb{C})$ has automorphism group the unitary group $U(16)$, of real dimension $256$; among these, the structure-preserving maps $X\mapsto UXV^{\dagger}$ form the subgroup $U(4)\times U(4)$ modulo the common centre, which is the part that also preserves the algebra structure.

**The two-sided action and the double cover.** The positive definite form makes the Hermitian subspace $\mathbb{M}_+$ a definite space of real dimension $4$, and the norm-one group $\tilde{G}=\{\tilde{A}:N(\tilde{A})=1\}=SL_2(\mathbb{C})$ acts on it by $\tilde{Q}\mapsto\tilde{A}\tilde{Q}\tilde{A}^{*}$, preserving the determinant:

$$
\langle\tilde{A}\tilde{Q}\tilde{A}^{*},\tilde{A}\tilde{Q}\tilde{A}^{*}\rangle_{\natural}=\langle\tilde{Q},\tilde{Q}\rangle_{\natural},\qquad \tilde{A}\in\tilde{G}.
$$

The action defines the surjective homomorphism $SL_2(\mathbb{C})\to SO^{+}(1,3)$ with kernel $\{\pm e_0\}$, the two-to-one cover of the identity component of the orthogonal group of the restricted form; it is read on the module in *Biquaternion Spin Geometry*.

**Proposition (the image is the identity component).** The image of the two-sided action is the identity component $SO^{+}(1,3)$.

*Proof.* The action $(\tilde{A},\tilde{Q})\mapsto\tilde{A}\tilde{Q}\tilde{A}^{*}$ has kernel $\{\pm e_0\}$ and its image is the subgroup of $SO^{+}(1,3)$ generated by the one-parameter families $\tilde{A}(t)=\exp(t\tilde X)$, which are the rotations and boosts of the restricted form; the image is the whole identity component. $\square$

## Worked Examples

**The identity.** Let $\tilde{Q}=e_0$. Then $\mathsf{M}_4(e_0)=I_4$, $\lVert\mathsf{M}_4(e_0)\rVert_F^2=4=4\lVert e_0\rVert_E^2$, and $\tfrac12\operatorname{Tr}(I_4^{\dagger}I_4)=2=2\langle e_0,e_0\rangle_{*}$.

**A Hermitian element.** Let $\tilde{Q}=e_0+ie_3$. Then $\tilde{Q}^{*}=\tilde{Q}$ and $\mathsf{M}_4(\tilde{Q})^{\dagger}=\mathsf{M}_4(\tilde{Q})$, so the regular matrix is Hermitian; the square is $\tilde{Q}\star\tilde{Q}=\tilde{Q}^2=e_0+2ie_3+(ie_3)^2=2e_0+2ie_3=2\tilde{Q}$, a positive semidefinite element, and the diagonal of the pairing is $4\lVert\tilde{Q}\rVert_E^2=8$.

**A zero divisor.** Let $\tilde{Q}=e_0+ie_1$. Then $\det\mathsf{M}_4(\tilde{Q})=N(\tilde{Q})^2=0$ and the regular matrix is singular of rank two, while $\lVert\mathsf{M}_4(\tilde{Q})\rVert_F^2=4\lVert\tilde{Q}\rVert_E^2=8$: the element is a zero divisor and yet a definite one for the general plain sesquilinear form.

## Summary

The left regular representation is a $*$-representation, $\mathsf{M}_4(\tilde{Q}^{*})=\mathsf{M}_4(\tilde{Q})^{\dagger}$, and it reads the sesquilinear product as the product with the conjugate-transposed second factor, $\mathsf{M}_4(\tilde{P}\star\tilde{Q})=\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q})^{\dagger}$, whose square is always positive semidefinite. The general plain sesquilinear form of the group is the Hilbert–Schmidt pairing $\tfrac12\operatorname{Tr}(\mathsf{M}_4(\tilde{P})^{\dagger}\mathsf{M}_4(\tilde{Q}))=2\langle\tilde{Q},\tilde{P}\rangle_{*}$, positive definite of signature $(32,0)$ on the matrices, with Frobenius norm $\lVert\mathsf{M}_4(\tilde{Q})\rVert_F=2\lVert\tilde{Q}\rVert_E$ and null set $\{0\}$; its automorphism group is $U(16)$, whose algebra-preserving part is $U(4)\times U(4)$ modulo the centre. The two-sided action of the norm-one group $SL_2(\mathbb{C})$ on the Hermitian subspace gives the double cover $SL_2(\mathbb{C})\to SO^{+}(1,3)$, and the units of the algebra appear as the matrices of $GL_2(\mathbb{C})$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde{Q})$ | the $4\times4$ regular matrix, $\operatorname{Tr}\mathsf{M}_4(\tilde{Q})=4Q_0$ |
| $\mathsf{M}_4(\tilde{Q}^{*})=\mathsf{M}_4(\tilde{Q})^{\dagger}$ | the Hermitian conjugation is the conjugate transpose |
| $\mathsf{M}_4(\tilde{P}\star\tilde{Q})=\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q})^{\dagger}$ | the sesquilinear product on the regular matrices |
| $\tfrac12\operatorname{Tr}(\mathsf{M}_4(\tilde{P})^{\dagger}\mathsf{M}_4(\tilde{Q}))=2\langle\tilde{Q},\tilde{P}\rangle_{*}$ | the general plain sesquilinear form as the Hilbert–Schmidt pairing |
| $\lVert\mathsf{M}_4(\tilde{Q})\rVert_F=2\lVert\tilde{Q}\rVert_E$ | the Frobenius norm of the regular matrix |
| $SL_2(\mathbb{C})\to SO^{+}(1,3)$ | the double cover of the two-sided action on the Hermitian subspace |

## Further Reading

- *Introduction to the 4×4 Matrix Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-representation-of-biquaternions.md`), for the representation and its first properties
- *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/biquaternion-4x4-matrix-element-representation.md`), for the further reading of the regular representation
- *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the sesquilinear product on the algebra
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the form on the algebra
- *The General Plain Sesqualgebra in the $2\times2$ Matrix Representation* (`articles_maths/the-general-plain-sesqualgebra-in-the-2x2-matrix-representation.md`), for the companion reading of the group
- *The Six Subspaces under the General Plain Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-plain-sesqualgebra-of-biquaternions.md`), for the restriction theory of the form
