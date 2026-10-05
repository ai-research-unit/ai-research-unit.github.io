# __The 2×2 Matrix Representation under the Four Forms__

## Introduction

The algebra $\mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$ through the realization $\Phi$ of *Biquaternion 2×2 Matrix Element Representation*, and that article reads the isomorphism for the algebra it transports: the product, the trace, the determinant, the spectrum, the rank-one elements and the module. This article reads the same realization for its **topology**, and it does so four times, once for each of the four pairings of *The Four Pairings of the Biquaternion Algebra*.

Each pairing of the algebra is realized on the matrices as a pairing of the same formal type, with the trace taking the place of the scalar part and the adjugate and the conjugate transpose marking the two non-bilinear cases. The four pairings of the matrices are

$$
\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})\Phi(\tilde{Q})\bigr),
\qquad
\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q})\bigr),
\qquad
\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q})\bigr),
\qquad
\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q})\bigr),
$$

the plain product, the product adjugated in the second argument, the conjugate-transpose product and the adjugate of the conjugate transpose; they reproduce the complex bilinear, the quaternion bilinear, the complex sesquilinear and the quaternion sesquilinear form of the algebra respectively, the second preceded by adjugation and the fourth by the adjugate of the conjugate transpose. Each is a form on the matrix algebra with its own signature, its own definiteness, its own null set and its own group of isometries, so each induces its own topology on the representation; the four are kept apart in the four sections below.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the element $\tilde{Q}=\sum_{\mu}Q_{\mu}e_{\mu}$ with $Q_{\mu}=q_{\mu}+iq'_{\mu}$, units $e_0=1$ and $e_k^2=-e_0$, central scalar imaginary $i$, scalar part $\mathrm{Sc}$, sign vector $\varepsilon=(1,-1,-1,-1)$ and $E=\mathrm{diag}(1,-1,-1,-1)$; $\Phi$ is the $2\times2$ matrix realization $\Phi(e_0)=I$, $\Phi(e_k)=-i\sigma_k$ of *Biquaternion 2×2 Matrix Element Representation*.

## The Representation

**Definition.** The **matrix realization** is the $\mathbb{C}$-linear isomorphism

$$
\Phi:\mathbb{B}\longrightarrow M_2(\mathbb{C}), \qquad \Phi(e_0)=I, \qquad \Phi(e_k)=-i\sigma_k,
$$

with $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices, so that for $\tilde{Q}=Q_0e_0+\mathbf{Q}$,

$$
\Phi(\tilde{Q}) = \begin{pmatrix} Q_0-iQ_3 & -iQ_1-Q_2 \\ -iQ_1+Q_2 & Q_0+iQ_3 \end{pmatrix}.
$$

The trace is $\operatorname{Tr}\Phi(\tilde{Q})=2Q_0$ and the determinant is $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\det\Phi(\tilde{Q})$, the biquaternion determinant; the trace identity $\mathrm{Sc}(\tilde{R}\tilde{S})=\tfrac12\operatorname{Tr}(\Phi(\tilde{R})\Phi(\tilde{S}))$ is what makes the matrix trace the carrier of the scalar part, and $\Phi(\tilde{Q}^{\natural})=\operatorname{adj}\Phi(\tilde{Q})$ makes the adjugate the carrier of the natural conjugation.

## The Complex Bilinear Pairing of the Matrices

**Theorem (the complex bilinear pairing of the matrices).** For all biquaternions,

$$
\langle\tilde{P},\tilde{Q}\rangle = \tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})\Phi(\tilde{Q})\bigr),
$$

the plain pairing of the matrices, in which neither argument is adjugated or conjugated.

**Proof.** The trace identity $\mathrm{Sc}(\tilde{R}\tilde{S})=\tfrac12\operatorname{Tr}(\Phi(\tilde{R})\Phi(\tilde{S}))$ gives the right-hand side at once.

It is the pairing whose diagonal is the complex bilinear form of the element, $\langle\tilde{Q},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{Q}\tilde{Q})=\sum_\mu\varepsilon_\mu Q_\mu^2$; in the coefficient basis its Gram matrix is the sign matrix $E=\mathrm{diag}(1,-1,-1,-1)$, of real signature $(4,4)$ on the eight real coordinates.

**The null set.** The set on which the pairing vanishes is the isotropic cone $\sum_\mu\varepsilon_\mu Q_\mu^2=0$, a complex cone of real dimension $6$ in $\mathbb{R}^8$; it meets the determinant null set on the zero divisors and is not the null set of any of the other three pairings.

**The isometry group.** The pairing has Gram matrix $E$, so its group of isometries on the coefficient space is the complex orthogonal group $O_4(\mathbb{C})$ of *The Four Pairings of the Biquaternion Algebra*; on the matrix side it is the group of linear maps preserving the plain trace pairing, and the real
part of the form is a real bilinear form of signature $(4,4)$ with isometry group $O(4,4)$.

## The Quaternion Bilinear Pairing of the Matrices

**Theorem (the quaternion bilinear pairing of the matrices).** For all biquaternions,

$$
\langle\tilde{P},\tilde{Q}\rangle_{\natural} = \tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q})\bigr),
$$

the quaternion bilinear pairing of the matrices in which the second argument is adjugated.

**Proof.** $\operatorname{adj}\Phi(\tilde{Q})=\Phi(\tilde{Q}^{\natural})$, so the right-hand side is $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\Phi(\tilde{Q}^{\natural}))=\mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})=\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ by the trace identity.

It is the pairing whose diagonal is the determinant, $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\det\Phi(\tilde{Q})$; in the coefficient basis its Gram matrix is $\mathrm{I}_4$, of real signature $(4,4)$ on the eight real coordinates, the split form.

**The null set.** The set on which the pairing vanishes, $\det\Phi(\tilde{Q})=0$, is the singular matrices; these are exactly the rank-one matrices $\Phi(\tilde{Q})=uv^{T}$, that is the zero divisors of the algebra. It is a real cone of real dimension $6$ in $\mathbb{R}^8$, the vanishing of one complex quadratic; it is contained in the isotropic cone of the underlying real form, a hypersurface of real dimension $7$, which is the largest of the null sets of the four topologies.

**The isometry group.** The pairing has Gram matrix $\mathrm{I}_4$, so its group of isometries on the coefficient space is the complex orthogonal group $O_4(\mathbb{C})$ of *The Four Pairings of the Biquaternion Algebra*; on the matrix side it is the group of linear maps preserving the adjugated pairing, and the real part
of the form is the split real bilinear form of signature $(4,4)$, with isometry group the split
orthogonal group $O(4,4)$.

## The Complex Sesquilinear Pairing of the Matrices

**Theorem (the complex sesquilinear pairing of the matrices).** For all biquaternions,

$$
\langle\tilde{Q},\tilde{P}\rangle_{*} = \tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q})\bigr),
$$

the **Hilbert–Schmidt pairing** of the matrices.

**Proof.** $\Phi(\tilde{P})^{\dagger}=\Phi(\tilde{P}^{*})$ because $\Phi$ is a $*$-homomorphism for the Hermitian conjugation and the conjugate transpose, so the right-hand side is $\tfrac12\operatorname{Tr}(\Phi(\tilde{P}^{*})\Phi(\tilde{Q}))=\mathrm{Sc}(\tilde{P}^{*}\tilde{Q})=\langle\tilde{Q},\tilde{P}\rangle_{*}$.

**Theorem (the Frobenius norm).** The diagonal of the pairing is one half of the squared Frobenius norm,

$$
\langle\tilde{Q},\tilde{Q}\rangle_{*} = \tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{Q})^{\dagger}\Phi(\tilde{Q})\bigr) = \tfrac12\bigl\lVert\Phi(\tilde{Q})\bigr\rVert_F^2 = \sum_\mu|Q_\mu|^2 = \lVert\tilde{Q}\rVert_E^2 ,
$$

so that $\lVert\Phi(\tilde{Q})\rVert_F=\sqrt2\,\lVert\tilde{Q}\rVert_E$.

**Proof.** The first equality is the diagonal case of the theorem above, the second is the definition of the Frobenius norm of the matrix, and the square root gives the norm identity.

**The Euclidean topology.** The pairing is positive definite of signature $(8,0)$ on the eight real dimensions; it is the Hilbert–Schmidt inner product of the matrix algebra, and through $\Phi$ it is the Euclidean inner product of $\mathbb{B}$. It induces the Euclidean topology on the representation, the same topology that *The Euclidean Topology of the Biquaternion Algebra* reads on the algebra.

**The isometry group and the unit groups.** The Hilbert–Schmidt pairing lives on the four complex coordinates, so its isometry group is the unitary group $U(4)$, of real dimension $16$; among these, the maps $X\mapsto UXV^{\dagger}$ form the subgroup $U(2)\times U(2)$ modulo the common centre, which is the part that also preserves the algebra structure of $M_2(\mathbb{C})$. Under $\Phi$ the group of units of the algebra is the general linear group $GL_2(\mathbb{C})$, and the group $\{\tilde{A}:\langle\tilde{A},\tilde{A}\rangle_{\natural}=1\}$ is the special linear group $SL_2(\mathbb{C})$; the maximal compact subgroup is $U(2)$, and its special part is $SU(2)\cong\mathrm{Spin}(3)$. These are the groups of *The Unit Group and the Frobenius Norm in the Matrix Representation*.

## The Quaternion Sesquilinear Pairing of the Matrices

**Theorem (the quaternion sesquilinear pairing of the matrices).** For all biquaternions,

$$
\langle\tilde{Q},\tilde{P}\rangle_{\natural*} = \tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q})\bigr),
$$

the pairing in which the conjugate transpose of the first argument is adjugated.

**Proof.** $\operatorname{adj}\Phi(\tilde{P})^{\dagger}=\Phi(\tilde{P}^{\natural})^{\dagger}=\Phi\bigl((\tilde{P}^{\natural})^{*}\bigr)=\Phi(\bar{\tilde{P}})$, since $(\tilde{P}^{\natural})^{*}=\bar{\tilde{P}}$; the right-hand side is then $\tfrac12\operatorname{Tr}(\Phi(\bar{\tilde{P}})\Phi(\tilde{Q}))=\mathrm{Sc}(\bar{\tilde{P}}\tilde{Q})=\langle\tilde{Q},\tilde{P}\rangle_{\natural*}$.

It is the pairing whose Gram matrix in the coefficient basis is the sign matrix $E=\mathrm{diag}(1,-1,-1,-1)$, of real signature $(2,6)$ and complex inertia $(1,3)$; the adjugate and the conjugate transpose together are what distinguish this case from the other three.

**The null set and the fundamental symmetry.** The set on which the pairing vanishes is the isotropic cone of the form $\sum_\mu\varepsilon_\mu|Q_\mu|^2=0$, which is not the null set of any of the other three pairings: an element may be a zero divisor and definite for the quaternion sesquilinear form, or isotropic and a unit. The natural conjugation $J={}^{\natural}$ is an isometry of all four pairings, and in the matrix picture it is the adjugation $\Phi(\tilde{Q})\mapsto\operatorname{adj}\Phi(\tilde{Q})$.

**The isometry group.** The form $\langle\cdot,\cdot\rangle_{\natural*}$ is the quaternion sesquilinear form of signature $(1,3)$ on $\mathbb{C}^4$, so its isometry group is the indefinite unitary group $U(1,3)$ of *The Krein Isometry Group and Its $J$-Contractions*; on the matrix side it is the group preserving the adjugated conjugate-transpose pairing, whose realification has isometry group $O(2,6)$.

## The Four Forms Compared

| form | matrix pairing | signature over $\mathbb{R}$ | definiteness | null set | isometry group |
|---|---|---|---|---|---|
| complex bilinear | $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\Phi(\tilde{Q}))$ | $(4,4)$ | indefinite | $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ | $O_4(\mathbb{C})$; realification $O(4,4)$ |
| quaternion bilinear | $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q}))$ | $(4,4)$ | indefinite (split) | $\det\Phi(\tilde{Q})=0$ | $O_4(\mathbb{C})$; realification $O(4,4)$ |
| complex sesquilinear | $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))$ | $(8,0)$ | positive definite | $\{0\}$ | $U(4)$; $U(2)\times U(2)$ preserves the algebra |
| quaternion sesquilinear | $\tfrac12\operatorname{Tr}(\operatorname{adj}\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))$ | $(2,6)$ | indefinite | $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^2=0$ | $U(1,3)$; real form $O(2,6)$ |

Four matrix operations carry the four topologies, and they are read off one another: the plain product gives the complex bilinear pairing and the complex bilinear form, the adjugate gives the quaternion bilinear pairing and the determinant, the conjugate transpose gives the complex sesquilinear pairing and the Frobenius norm, and the adjugate of the conjugate transpose gives the quaternion sesquilinear pairing and the sign matrix. The four diagonal identities $\langle\tilde{Q},\tilde{Q}\rangle=\sum_\mu\varepsilon_\mu Q_\mu^2$, $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\det\Phi(\tilde{Q})$, $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\lVert\tilde{Q}\rVert_E^2$ and $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\sum_\mu\varepsilon_\mu|Q_\mu|^2$ are the diagonal readings of the four.

## Summary

Each of the four pairings of the algebra becomes a pairing of the matrices through the trace of *Biquaternion 2×2 Matrix Element Representation*. The complex bilinear form is the plain pairing $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\Phi(\tilde{Q}))$ of real signature $(4,4)$, with the sign matrix $E$ as Gram matrix and the cone $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ as null set; the quaternion bilinear form is $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q}))$, the pairing with the second argument adjugated, of real signature $(4,4)$, whose diagonal is the determinant and whose null set is the singular matrices; the complex sesquilinear form is the Hilbert–Schmidt pairing $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))$, positive definite of signature $(8,0)$, one half of the squared Frobenius norm, with $\lVert\Phi(\tilde{Q})\rVert_F=\sqrt2\lVert\tilde{Q}\rVert_E$; and the quaternion sesquilinear form is $\tfrac12\operatorname{Tr}(\operatorname{adj}\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))$, of signature $(2,6)$, with the sign matrix $E$ as Gram matrix and the adjugate of the conjugate transpose as its characteristic operation. The four isometry groups are $O_4(\mathbb{C})$, $O_4(\mathbb{C})$, $U(4)$ and $U(1,3)$; inside them, the algebra-preserving part of $U(4)$ is $U(2)\times U(2)$ modulo the centre.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi(\tilde{Q})$ | the $2\times2$ matrix of the realization, $\det\Phi(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ |
| $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\Phi(\tilde{Q}))$ | the complex bilinear pairing of the matrices, the plain product |
| $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q}))$ | the quaternion bilinear pairing of the matrices |
| $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))$ | the complex sesquilinear pairing, the Hilbert–Schmidt pairing |
| $\tfrac12\operatorname{Tr}(\operatorname{adj}\Phi(\tilde{P})^{\dagger}\Phi(\tilde{Q}))$ | the quaternion sesquilinear pairing of the matrices |
| $\lVert\Phi(\tilde{Q})\rVert_F=\sqrt2\,\lVert\tilde{Q}\rVert_E$ | the Frobenius norm and the Euclidean norm |
| $(4,4)$, $(4,4)$, $(8,0)$, $(2,6)$ | the four signatures over $\mathbb{R}$ |

## Further Reading

- *Biquaternion 2×2 Matrix Element Representation* (`articles_maths/biquaternion-2x2-matrix-element-representation.md`), for the realization in the Algebra group
- *The Forms in the Matrix Representation of the Biquaternion Algebra* (`articles_maths/the-forms-in-the-matrix-representation-of-the-biquaternion-algebra.md`), for the four pairings of the matrices in full
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the adjugated trace pairings used here
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms of the algebra and their isometry groups
- *The Complex Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-complex-bilinear-form-on-the-biquaternion-algebra.md`), for the plain pairing and its isotropic structure
- *The Unit Group and the Frobenius Norm in the Matrix Representation* (`articles_maths/the-unit-group-and-the-frobenius-norm-in-the-matrix-representation.md`), for the matrix form of the unit group and the topology of the algebra
