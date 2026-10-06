
# __The Biquaternion Algebra in the $2\times2$ Matrix Representation__

## Introduction

The reading group *Topology on the Biquaternions as an Algebra over $\mathbb{C}$* reads the algebra through one pairing, the complex bilinear form $\langle\tilde{P},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{P}\tilde{Q})=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$, through the plain product it polarises, and through the two-sided operators that product defines. This article reads that same group through the $2\times2$ matrix realization $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ of *Introduction to the $2\times2$ Matrix Representation of Biquaternions*, and it is the first of the two representation articles of the group: the companion *The Biquaternion Algebra in the $4\times4$ Regular Matrix Representation* repeats the reading on the left regular representation.

The plain product becomes the matrix product under $\Phi$, and the complex bilinear form becomes the plain trace pairing $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\Phi(\tilde{Q}))$. The two facts are the whole content of the group's topology on the matrices: the product transports because $\Phi$ is an algebra isomorphism, and the trace carries the scalar part because $\mathrm{Sc}(\tilde{R}\tilde{S})=\tfrac12\operatorname{Tr}(\Phi(\tilde{R})\Phi(\tilde{S}))$.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity and $e_k^2=-e_0$; a generic element is $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; the scalar part is $\mathrm{Sc}$, the sign vector is $\varepsilon=(1,-1,-1,-1)$, the natural conjugation ${}^{\natural}$ negates $e_1,e_2,e_3$, and the Hermitian conjugation is ${}^{*}={}^{\natural}\circ\bar{\cdot}$. All matrix claims of this article are recomputed in the verification script of the pass.

## The Representation

**Definition.** The **matrix realization** is the $\mathbb{C}$-linear isomorphism

$$
\Phi:\mathbb{B}\longrightarrow M_2(\mathbb{C}),\qquad \Phi(e_0)=I,\qquad \Phi(e_k)=-i\sigma_k ,
$$

with $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices, so that

$$
\Phi(\tilde{Q}) = \begin{pmatrix} Q_0-iQ_3 & -iQ_1-Q_2 \\ -iQ_1+Q_2 & Q_0+iQ_3 \end{pmatrix} .
$$

The realization is an isomorphism of algebras, and the three basic invariants are the trace, the determinant and the two conjugations,

$$
\operatorname{Tr}\Phi(\tilde{Q})=2Q_0,\qquad \det\Phi(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^2,\qquad \Phi(\tilde{Q}^{\natural})=\operatorname{adj}\Phi(\tilde{Q}),\qquad \Phi(\tilde{Q}^{*})=\Phi(\tilde{Q})^{\dagger} .
$$

## The Plain Product in the Representation

**Theorem (the product is the matrix product).** For all biquaternions,

$$
\Phi(\tilde{P})\Phi(\tilde{Q})=\Phi(\tilde{P}\tilde{Q}),
$$

so the plain product of the algebra is the product of the matrices.

*Proof.* $\Phi$ is the algebra isomorphism $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ defined on the generators by $\Phi(e_k)=-i\sigma_k$, and the Pauli matrices realise the quaternion relations $\sigma_k\sigma_l=\delta_{kl}I+i\sum_m\epsilon_{klm}\sigma_m$.

**The dictionary of the product.** The theorem transports every product-theoretic notion of the group into the matrix algebra:

- the centre of $\mathbb{B}$ is the scalar matrices $\mathbb{C} I$, so a biquaternion is central exactly when its matrix is a scalar;
- the group of units $\mathbb{B}^\times$ is $GL_2(\mathbb{C})$, and the unit group is the complement of the singular matrices;
- the zero divisors are the singular matrices, equivalently the rank-one matrices $\Phi(\tilde{Q})=uv^{\mathsf{T}}$;
- the two-sided operator $X\mapsto \tilde{Q}X\tilde{Q}^{-1}$ is the conjugation $M\mapsto \Phi(\tilde{Q})M\Phi(\tilde{Q})^{-1}$ of the matrix algebra.

## The Complex Bilinear Form in the Representation

**Theorem (the trace pairing).** For all biquaternions,

$$
\langle\tilde{P},\tilde{Q}\rangle = \tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})\Phi(\tilde{Q})\bigr),
$$

and the matrix trace is the carrier of the scalar part, $\mathrm{Sc}(\tilde{R}\tilde{S})=\tfrac12\operatorname{Tr}(\Phi(\tilde{R})\Phi(\tilde{S}))$.

*Proof.* The trace identity gives the right-hand side at once; it holds on the basis, where $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and $\operatorname{Tr}(\Phi(e_\mu)\Phi(e_\nu))=2\varepsilon_\mu\delta_{\mu\nu}$.

**Theorem (the diagonal).** On the diagonal the pairing is the complex bilinear form of the element,

$$
\langle\tilde{Q},\tilde{Q}\rangle = \tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{Q})^2\bigr) = \sum_\mu\varepsilon_\mu Q_\mu^2 .
$$

**The Gram matrix and the signature.** In the coefficient basis the Gram matrix of the pairing is the sign matrix $E=\operatorname{diag}(1,-1,-1,-1)$; over $\mathbb{R}$ the form has signature $(4,4)$ on the eight real coordinates, and it is indefinite.

**The null set.** The pairing vanishes on the isotropic cone $\sum_\mu\varepsilon_\mu Q_\mu^2=0$, a complex cone of real dimension $6$ in $\mathbb{R}^8$; it is the null set of neither the determinant nor the quaternion bilinear form.

**The isometries.** The isometry group on the matrices is the group preserving the plain trace pairing; on the coefficients it is the complex orthogonal group $O_4(\mathbb{C})$, of complex dimension $12$, and the real part of the form is a real bilinear form of signature $(4,4)$ with isometry group $O(4,4)$. The conjugation $M\mapsto UMU^{-1}$ by a unit and the transposition $M\mapsto M^{\mathsf{T}}$ are isometries, since $\operatorname{Tr}(UMU^{-1}\cdot UNU^{-1})=\operatorname{Tr}(MN)$ and $\operatorname{Tr}(M^{\mathsf{T}}N^{\mathsf{T}})=\operatorname{Tr}(MN)$; the inner automorphisms and the transposition together form a proper subgroup of the full group $O_4(\mathbb{C})$.

## Worked Examples

**A zero divisor that is not isotropic.** Let $\tilde{Q}=e_0+ie_1$. Then $N(\tilde{Q})=1+i^2=0$, so $\tilde{Q}$ is a zero divisor, and $\Phi(\tilde{Q})=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ is singular of rank one; but $\langle\tilde{Q},\tilde{Q}\rangle=Q_0^2-Q_1^2=1-i^2=2$, so $\tilde{Q}$ is not isotropic for the complex bilinear form.

**An isotropic pair.** Let $\tilde{P}=e_0+ie_1$ and $\tilde{Q}=e_0-ie_1$. Then $\langle\tilde{P},\tilde{Q}\rangle=1+(-1)(i)(-i)=1-1=0$, so the two are isotropic to each other while both matrices are singular.

**A central element.** Let $\tilde{Q}=\lambda e_0$. Then $\Phi(\tilde{Q})=\lambda I$ and $\langle\tilde{Q},\tilde{Q}\rangle=\lambda^2$, while $\det\Phi(\tilde{Q})=\lambda^2$; the two invariants agree on the centre and separate off it.

## Summary

The matrix realization $\Phi$ turns the plain product of the algebra into the matrix product, by the isomorphism theorem $\Phi(\tilde{P})\Phi(\tilde{Q})=\Phi(\tilde{P}\tilde{Q})$, and the scalar part into the half trace, $\mathrm{Sc}(\tilde{R}\tilde{S})=\tfrac12\operatorname{Tr}(\Phi(\tilde{R})\Phi(\tilde{S}))$. The complex bilinear form of the group is therefore the plain trace pairing $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\Phi(\tilde{Q}))$, whose diagonal is the complex bilinear form $\sum_\mu\varepsilon_\mu Q_\mu^2$ of the element, whose coefficient Gram matrix is the sign matrix $E$, of real signature $(4,4)$, whose null set is the isotropic cone of real dimension $6$, and whose isometry group is $O_4(\mathbb{C})$ on the coefficients and $O(4,4)$ on the realification. The units are $GL_2(\mathbb{C})$, the zero divisors are the singular matrices, and the trace and determinant are the two invariants $2Q_0$ and $\sum_\mu Q_\mu^2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi(\tilde{Q})$ | the $2\times2$ matrix of the realization, $\Phi(e_0)=I$, $\Phi(e_k)=-i\sigma_k$ |
| $\Phi(\tilde{P})\Phi(\tilde{Q})=\Phi(\tilde{P}\tilde{Q})$ | the plain product is the matrix product |
| $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\Phi(\tilde{Q}))=\langle\tilde{P},\tilde{Q}\rangle$ | the complex bilinear form as the plain trace pairing |
| $E=\operatorname{diag}(1,-1,-1,-1)$ | the coefficient Gram matrix, real signature $(4,4)$ |
| $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ | the isotropic cone, of real dimension $6$ |
| $O_4(\mathbb{C})$, $O(4,4)$ | the isometry group and its realification |

## Further Reading

- *Introduction to the $2\times2$ Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`), for the realization and its first properties
- *Biquaternion 2×2 Matrix Element Representation* (`articles_maths/biquaternion-2x2-matrix-element-representation.md`), for the further reading of the isomorphism
- *The Complex Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-complex-bilinear-form-on-the-biquaternion-algebra.md`), for the form on the algebra
- *Association and the Transpose on the Biquaternion Algebra* (`articles_maths/association-and-the-transpose-on-the-biquaternion-algebra.md`), for the operators of this group
- *The Biquaternion Algebra in the $4\times4$ Regular Matrix Representation* (`articles_maths/the-biquaternion-algebra-in-the-4x4-regular-matrix-representation.md`), for the companion reading of the group
- *The Six Subspaces under the Complex Bilinear Form* (`articles_maths/the-six-subspaces-under-the-complex-bilinear-form.md`), for the restriction theory of the form
