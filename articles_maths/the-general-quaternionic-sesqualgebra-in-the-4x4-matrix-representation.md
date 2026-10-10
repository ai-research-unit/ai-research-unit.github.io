
# __The General Quaternionic Sesqualgebra in the $4\times4$ Matrix Representation__

## Introduction

The left regular representation $\mathsf{M}_4$ of *Introduction to the $4\times4$ Matrix Representation $M_4(\mathbb{C})_L$ of Biquaternions* carries the two conjugations of the algebra as two matrix operations: the natural conjugation is the **transposition**, $\mathsf{M}_4(\tilde{Q}^{\natural})=\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}$, and the Hermitian conjugation is the **conjugate transpose**, $\mathsf{M}_4(\tilde{Q}^{*})=\mathsf{M}_4(\tilde{Q})^{\dagger}$. This article is the companion of *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Representation*, and it reads the group *Topology on the Introduction to the General Quaternionic Sesqualgebra of Biquaternions* on the regular matrices: the general quaternionic sesquilinear product becomes the transposed conjugate-transposed product, and the Krein form becomes the adjugated conjugate-transpose pairing of the regular matrices, of signature $(2,6)$ and with the adjugate appearing as the scalar factor $N(\tilde{P})$.

The regular representation has the advantage that the transposition is the operation it already carries, so the fundamental symmetry $J={}^{\natural}$ needs no adjugate here: it is the plain transposition of the regular matrix. The adjugate appears only in the form, where it contributes the factor $N(\tilde{P})$, and on the norm-one slice that factor is one and the pairing is exactly twice the general quaternionic sesquilinear form.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity and $e_k^2=-e_0$; $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; scalar part $\mathrm{Sc}$, sign matrix $E=\operatorname{diag}(1,-1,-1,-1)$; natural conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$, Hermitian conjugation ${}^{*}={}^{\natural}\circ\bar{\cdot}$; product $\tilde{P}\star\tilde{Q}=\tilde{P}^{\natural}\tilde{Q}^{*}$. All matrix claims of this article are recomputed in the verification script of the pass.

## The Representation

**Definition.** The **left regular matrix** is the isomorphism written $\mathsf{M}_4$. It converts a biquaternion into a $4 \times 4$ complex matrix,

$$
\mathsf{M}_4:\mathbb{B}\longrightarrow M_4(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity: in the basis $e_0,e_1,e_2,e_3$ its $m$-th column is the coordinate column of the product $\tilde{Q}e_m$. It satisfies

$$
\mathsf{M}_4(\tilde{Q}^{\natural})=\mathsf{M}_4(\tilde{Q})^{\mathsf{T}},\qquad \mathsf{M}_4(\tilde{Q}^{*})=\mathsf{M}_4(\tilde{Q})^{\dagger},\qquad \operatorname{Tr}\mathsf{M}_4(\tilde{Q})=4Q_0,\qquad \det\mathsf{M}_4(\tilde{Q})=N(\tilde{Q})^2 ,
$$

so the model carries the natural conjugation as the transposition and the Hermitian conjugation as the conjugate transpose.

## The General Quaternionic Sesquilinear Product in the Regular Representation

**Theorem (the transposed conjugate-transposed product).** For all biquaternions,

$$
\mathsf{M}_4(\tilde{P}\star\tilde{Q})=\mathsf{M}_4(\tilde{P})^{\mathsf{T}}\,\mathsf{M}_4(\tilde{Q})^{\dagger} ,
$$

the product of the transposed first factor with the conjugate-transposed second factor.

*Proof.* $\tilde{P}\star\tilde{Q}=\tilde{P}^{\natural}\tilde{Q}^{*}$, the representation is multiplicative, and it carries the two conjugations to the transposition and the conjugate transpose.

**The fundamental symmetry.** The natural conjugation $J={}^{\natural}$ is the transposition on the regular matrices, $\mathsf{M}_4(\tilde{Q}^{\natural})=\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}$; it is an involution, it is self-adjoint for the Krein form, and its two eigenspaces are the Hermitian and anti-Hermitian subspaces, carried to the symmetric and antisymmetric parts of the regular matrix. The $J$-unitary operators are characterised in the coefficient basis by $\mathsf{M}_4(\tilde{Q})^{*}E\mathsf{M}_4(\tilde{Q})=E$.

## The General Quaternionic Sesquilinear Form in the Regular Representation

**Theorem (the adjugated conjugate-transpose pairing of the regular matrices).** For all biquaternions,

$$
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf{M}_4(\tilde{P})^{\dagger}\mathsf{M}_4(\tilde{Q})\bigr) = 2\,\overline{N(\tilde{P})}\,\langle\tilde{P},\tilde{Q}\rangle_{\natural*} ,
$$

the general quaternionic sesquilinear form of the algebra multiplied by twice the conjugate of the norm.

*Proof.* $\operatorname{adj}\mathsf{M}_4(\tilde{P})=N(\tilde{P})\mathsf{M}_4(\tilde{P}^{\natural})$ because $\det\mathsf{M}_4(\tilde{P})=N(\tilde{P})^2$ and $\mathsf{M}_4(\tilde{P})^{-1}=\mathsf{M}_4(\tilde{P}^{\natural})/N(\tilde{P})$; taking conjugate transposes and multiplying gives $\operatorname{adj}\mathsf{M}_4(\tilde{P})^{\dagger}\mathsf{M}_4(\tilde{Q})=\overline{N(\tilde{P})}\,\mathsf{M}_4(\tilde{P}^{\natural})\mathsf{M}_4(\tilde{P})^{\dagger}\mathsf{M}_4(\tilde{Q})$, and the trace identity $\operatorname{Tr}\mathsf{M}_4(\tilde{R})=4\,\mathrm{Sc}(\tilde{R})$ gives the stated factor.

**Corollary (the norm-one slice).** On the group $N=1$ the identity is $\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_4(\tilde{P})^{\dagger}\mathsf{M}_4(\tilde{Q}))=2\langle\tilde{P},\tilde{Q}\rangle_{\natural*}$, exactly twice the general quaternionic sesquilinear form, as in the $2\times2$ representation.

**The diagonal and the signature.** On the diagonal the factor is $\overline{N(\tilde{Q})}$, so the form is $\sum_\mu\varepsilon_\mu|Q_\mu|^2$ up to that factor; it has complex inertia $(1,3)$ and real signature $(2,6)$ on the coefficient space, and its isotropic set is the real cone $\sum_\mu\varepsilon_\mu|Q_\mu|^2=0$, of real dimension $7$, distinct from the set of singular regular matrices.

**The automorphism group.** The form is the general quaternionic sesquilinear form of signature $(1,3)$, so its automorphism group is $U(1,3)$; the operators that preserve it are the $J$-unitary operators of *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*, and the realification has automorphism group $O(2,6)$.

## Worked Examples

**The identity.** Let $\tilde{Q}=e_0$. Then $\mathsf{M}_4(e_0)=I_4$, $\operatorname{adj}I_4=I_4$ and $N(e_0)=1$, so the identity reads $\tfrac12\operatorname{Tr}(I_4)=2=2\langle e_0,e_0\rangle_{\natural*}$.

**A transposed element.** Let $\tilde{Q}=e_1$. Then $\mathsf{M}_4(e_1)^{\mathsf{T}}=\mathsf{M}_4(e_1^{\natural})=-\mathsf{M}_4(e_1)$, so the transposition is realised as a sign change, and $\langle e_1,e_1\rangle_{\natural*}=-1$.

**A Krein-isotropic unit.** Let $\tilde{Q}=e_0+e_1$. Then $N(\tilde{Q})=2\neq0$, so $\tilde{Q}$ is a unit and the regular matrix is invertible, while $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=1-1=0$: the element is isotropic for the Krein form and a unit, which the general plain sesquilinear form of the other group does not allow.

## Summary

The left regular representation carries the natural conjugation as the transposition and the Hermitian conjugation as the conjugate transpose, so the general quaternionic sesquilinear product is the transposed conjugate-transposed product $\mathsf{M}_4(\tilde{P}\star\tilde{Q})=\mathsf{M}_4(\tilde{P})^{\mathsf{T}}\mathsf{M}_4(\tilde{Q})^{\dagger}$, whose fundamental symmetry is the plain transposition. The general quaternionic sesquilinear form of the group is the adjugated conjugate-transpose pairing $\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_4(\tilde{P})^{\dagger}\mathsf{M}_4(\tilde{Q}))=2\overline{N(\tilde{P})}\langle\tilde{P},\tilde{Q}\rangle_{\natural*}$, which on the norm-one slice is exactly twice the form; it has complex inertia $(1,3)$ and real signature $(2,6)$, its isotropic set is the real cone of real dimension $7$, and its automorphism group is the indefinite unitary group $U(1,3)$, of realification $O(2,6)$. The invariants of the regular matrix are the trace $4Q_0$ and the determinant $N(\tilde{Q})^2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde{Q})$ | the $4\times4$ regular matrix, $\operatorname{Tr}\mathsf{M}_4(\tilde{Q})=4Q_0$, $\det\mathsf{M}_4(\tilde{Q})=N(\tilde{Q})^2$ |
| $\mathsf{M}_4(\tilde{Q}^{\natural})=\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}$ | the natural conjugation is the transposition, the fundamental symmetry |
| $\mathsf{M}_4(\tilde{P}\star\tilde{Q})=\mathsf{M}_4(\tilde{P})^{\mathsf{T}}\mathsf{M}_4(\tilde{Q})^{\dagger}$ | the general quaternionic sesquilinear product |
| $\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_4(\tilde{P})^{\dagger}\mathsf{M}_4(\tilde{Q}))=2\overline{N(\tilde{P})}\langle\tilde{P},\tilde{Q}\rangle_{\natural*}$ | the general quaternionic sesquilinear form on the regular matrices |
| $(1,3)$ over $\mathbb{C}$, $(2,6)$ over $\mathbb{R}$ | the inertia and the real signature |
| $U(1,3)$, $O(2,6)$ | the automorphism group and its realification |

## Further Reading

- *Introduction to the 4×4 Matrix Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-representation-of-biquaternions.md`), for the representation and its first properties
- *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/biquaternion-4x4-matrix-element-representation.md`), for the further reading of the regular representation
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the form on the algebra
- *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the operators of the form
- *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Representation* (`articles_maths/the-general-quaternionic-sesqualgebra-in-the-2x2-matrix-representation.md`), for the companion reading of the group
- *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the restriction theory of the form
