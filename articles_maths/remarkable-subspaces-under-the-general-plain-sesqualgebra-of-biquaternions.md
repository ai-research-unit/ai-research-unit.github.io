
# __Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions__

## Introduction

The general plain sesquilinear form $\langle\tilde Q,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu|Q_\mu|^{2}$, positive definite on the algebra, is read here on the remarkable real subspaces of *Introduction to the Remarkable Subspaces* — the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$.

The form is used, not re-derived. Its definition, its Hermitian symmetry, its Gram matrix $\mathrm{I}_4$ in the coefficient basis and its unitary automorphism group $U(4)$ are the matter of *Biquaternion Norm and Invertibility*; the remarkable subspaces and their bases are *Introduction to the Remarkable Subspaces*; and the companion readings of the same remarkable subspaces by the other three pairings are *Remarkable Subspaces under the General Plain Algebra of Biquaternions*, *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* and *Remarkable Subspaces under the General Quaternionic Sesqualgebra of Biquaternions*. This article owns the restrictions themselves and the structure of each one.

## The Restriction Matrices

The form is positive definite on the whole algebra, so **every restriction is positive definite** and the only question for each subspace is its real dimension. The restriction is the Euclidean square of the coefficients, and because the form is diagonal in the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ with every entry $1$, each restriction is the identity matrix in the natural real basis of the subspace.

| Subspace | Natural real basis | Restricted form | Restriction matrix | Signature |
|---|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | $e_0,\,ie_0$ | $\lvert Q_0\rvert^{2}=q_0^{2}+(q'_0)^{2}$ | $\mathrm{I}_2$ | $(2,0)$ |
| Vector $\mathrm{Vect}(\mathbb{B})$ | $e_1,e_2,e_3,\,ie_1,ie_2,ie_3$ | $\sum_k\lvert Q_k\rvert^{2}$ | $\mathrm{I}_6$ | $(6,0)$ |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | $e_0,e_1,e_2,e_3$ | $\sum_\mu q_\mu^{2}$ | $\mathrm{I}_4$ | $(4,0)$ |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $ie_0,ie_1,ie_2,ie_3$ | $\sum_\mu(q'_\mu)^{2}$ | $\mathrm{I}_4$ | $(4,0)$ |
| Hermitian $\mathbb{M}_+$ | $e_0,ie_1,ie_2,ie_3$ | $q_0^{2}+\sum_k(q'_k)^{2}$ | $\mathrm{I}_4$ | $(4,0)$ |
| Anti-Hermitian $\mathbb{M}_-$ | $ie_0,e_1,e_2,e_3$ | $(q'_0)^{2}+\sum_kq_k^{2}$ | $\mathrm{I}_4$ | $(4,0)$ |

**Proposition (the matrices).** In the natural real basis displayed the restriction of the form is the identity matrix of the stated size; in particular every restriction is non-degenerate, with Gram determinant $1$.

*Proof.* In the real basis of the algebra the form is $\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu|Q_\mu|^{2}$, and on $e_\mu$ and $ie_\mu$ its values are $\delta_{\mu\nu}$ and $\langle ie_\mu,ie_\nu\rangle_{*}=|i|^{2}\delta_{\mu\nu}=\delta_{\mu\nu}$, while the mixed entries $\langle e_\mu,ie_\nu\rangle_{*}$ are the real parts of purely imaginary numbers and vanish. The natural real basis of each subspace is a subset of the algebra's real basis, in a different order, so the restriction is the corresponding principal submatrix, which is the identity. The diagonal values of the table follow by substituting the real coordinates of each subspace.

**Remark (the form distinguishes nothing among the remarkable subspaces).** The general plain sesquilinear form is positive definite on all remarkable subspaces, so it gives no intrinsic distinction among them: unlike the general plain bilinear, the general quaternionic bilinear and the general quaternionic sesquilinear forms, which are definite on some rows and indefinite on others, it equips all six with the same definite structure and differs from one row to the next only by the dimension. It is the **definite companion** of the general quaternionic sesquilinear form, and the comparison of the two readings of the remarkable subspaces is *The Four Pairings of the Biquaternion Algebra*, §*The Two Readings*.

## The Definite Character and the Maximal Definite Subspaces

The form is positive definite on the algebra, of signature $(8,0)$, so the algebra itself is a maximal positive definite subspace, of real dimension $8$, and every subspace of the remarkable subspaces is positive definite, hence a positive definite subspace of dimension its real dimension. The six dimensions are $2$, $6$, $4$, $4$, $4$ and $4$.

**Proposition (the maximal definite dimensions).** The maximal dimension of a positive definite subspace of the algebra is $8$, attained by the algebra; among the remarkable subspaces the positive definite dimensions are $2$ on the centre, $6$ on the vector subspace and $4$ on each of the four-dimensional subspaces.

*Proof.* A subspace is positive definite exactly when the restriction is positive definite, which here holds for all six by the table; the dimension of a positive definite subspace is bounded by the positive index $8$ of the ambient form, and the bound is attained by the algebra.

**Remark (the definite reading of the remarkable subspaces).** Because the form is definite, no subspace of the remarkable subspaces is totally isotropic, no nonzero element of any of them is null, and the remarkable subspaces carry the ordinary definite structure of $\mathbb{R}^{2}$, $\mathbb{R}^{6}$ and four copies of $\mathbb{R}^{4}$. The form is the **algebra reading** of the remarkable subspaces: it is the one pairing whose restrictions are all positive definite, and the comparison with the indefinite reading by the general quaternionic sesquilinear form is *The Four Pairings of the Biquaternion Algebra*, §*The Two Readings*.

## The Definite Structure and the Automorphism Groups

**Definition.** For each subspace $V$ of the remarkable subspaces, the **automorphism group of the restriction** is the group of real-linear maps of $V$ preserving the restriction,

$$
\mathrm{Isom}\bigl(V,\langle\cdot,\cdot\rangle_{*}\bigr)=\{S\in GL_{\mathbb{R}}(V):\langle Sv,Sw\rangle_{*}=\langle v,w\rangle_{*}\ \text{for all }v,w\in V\}.
$$

It is the real orthogonal group of the dimension of $V$.

| Subspace | Signature | Real-linear automorphism group | Real dimension | Complex-linear subgroup |
|---|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | $(2,0)$ | $O(2)$ | $1$ | $U(1)$ |
| Vector $\mathrm{Vect}(\mathbb{B})$ | $(6,0)$ | $O(6)$ | $15$ | $U(3)$ |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | $(4,0)$ | $O(4)$ | $6$ | — |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $(4,0)$ | $O(4)$ | $6$ | — |
| Hermitian $\mathbb{M}_+$ | $(4,0)$ | $O(4)$ | $6$ | — |
| Anti-Hermitian $\mathbb{M}_-$ | $(4,0)$ | $O(4)$ | $6$ | — |

**Proof.** The restriction is the standard positive definite form of $\mathbb{R}^{n}$, whose automorphism group is $O(n)$ of real dimension $n(n-1)/2$, giving $1$, $15$ and $6$ for $n=2,6,4$. The complexes of the centre and the vector subspace are preserved by the complex structure $i$, and the complex-linear automorphisms of $\lvert Q\rvert^{2}$ on $\mathbb{C}^{1}$ and $\mathbb{C}^{3}$ are $U(1)$ and $U(3)$; on the four real subspaces a complex-linear map need not preserve the real subspace, so no complex-linear subgroup is singled out.

The definite norm of the algebra is $\lVert\tilde Q\rVert_—$, of *The Euclidean Topology of the Biquaternion Algebra*, and the restriction of the form is the square of the restriction of the norm; the rows are therefore the remarkable definite subspaces of the ambient space, of dimensions $2$, $6$ and $4$.

**Remark (the ambient unitary group and the restriction groups).** The complex-linear automorphism group of the whole form is the unitary group $U(4)$ of *Biquaternion Norm and Invertibility*, of real dimension $16$. The real-linear automorphism group of the realified form is the larger $O(8)$, and the complex-linear automorphisms of a subspace restriction need not extend to the algebra, nor an automorphism of the algebra preserve the subspace; the groups of the table are the largest groups preserving the restriction.

**Remark (the orthogonality of the remarkable subspaces).** The form is diagonal in the coefficient basis $e_0,e_1,e_2,e_3$, so two of the remarkable subspaces are orthogonal exactly when their coefficient supports are disjoint. The centre has support $\{0\}$ and the vector subspace support $\{1,2,3\}$, while the quaternion, anti-quaternion and Hermitian subspaces have full support; the centre and the vector subspace are therefore orthogonal complements, and they are the only orthogonal pair among the remarkable subspaces, exactly as for the other three pairings. The common orthogonal pair of the four pairings is *The Four Pairings of the Biquaternion Algebra*.

## Worked Examples

**The standard basis is orthonormal.** On the whole algebra the eight real basis elements $e_\mu$, $ie_\mu$ are orthonormal for the form, so the eight are an orthonormal basis and the Gram matrix is $\mathrm{I}_8$ in that basis.

**The centre in coordinates.** With $\tilde Q=Ae_0$, $A=q_0+iq'_0$, the restriction is $q_0^{2}+(q'_0)^{2}=\lvert A\rvert^{2}$, the square of the modulus of $A$; the element $e_0+ie_0$ has norm squared $2$, and no nonzero element of the centre is null.

**The quaternion row.** For $\tilde Q=h=h_0e_0+\dots+h_3e_3$ the restriction is $\sum_\mu h_\mu^{2}$, the Euclidean square of $\mathbb{R}^{4}$; it coincides with the general quaternionic bilinear restriction of the same row, which is positive definite there, so on the quaternion subspace the two forms agree.

**The anti-quaternion row.** For $\tilde Q=ih$ the restriction is $\sum_\mu h_\mu^{2}$, again the Euclidean square; it is the negative of the general quaternionic bilinear restriction, which is $(0,4)$ on this row, and the two differ by the sign $i^{2}=-1$.

**The two Hermitian rows.** On $\mathbb{M}_+$ the restriction is $q_0^{2}+(q'_1)^{2}+(q'_2)^{2}+(q'_3)^{2}$ and on $\mathbb{M}_-$ it is $(q'_0)^{2}+q_1^{2}+q_2^{2}+q_3^{2}$, the standard inner products of $\mathbb{R}^{4}$ in the two orders of the coordinates; each is the square of the definite norm of the subspace, and neither has a null direction.

**The vector row and the vanishing of the cross terms.** On the vector subspace the restriction is $\sum_k(q_k^{2}+(q'_k)^{2})$, the Euclidean square of the six real coordinates: a real vector direction $e_k$ and its imaginary companion $ie_k$ are orthogonal, since the mixed value $\langle e_k,ie_l\rangle_{*}$ has real part zero.

**Every restriction is definite.** No element of any of the remarkable subspaces is isotropic: for $\tilde Q$ in any of them the value $\langle\tilde Q,\tilde Q\rangle_{*}=\sum_\mu|Q_\mu|^{2}$ is a sum of squares of real numbers, which vanishes only when every coefficient vanishes. The four indefinite restrictions of the other three pairings, by contrast, have the cones of the companion articles.

## Summary

On the remarkable real subspaces the general plain sesquilinear form carries the restrictions $\mathrm{I}_2$, $\mathrm{I}_6$ and four copies of $\mathrm{I}_4$ in the natural real bases, of signatures $(2,0)$, $(6,0)$ and $(4,0)$, so that **every restriction is positive definite** and the form distinguishes nothing among the remarkable subspaces. The remarkable subspaces are therefore Euclidean subspaces of dimensions $2$, $6$ and $4$, and the form is the definite companion of the general quaternionic sesquilinear form, which is indefinite on four of the same six. The real-linear automorphism groups are $O(2)$, $O(6)$ and four copies of $O(4)$, with the complex-linear subgroups $U(1)$ on the centre and $U(3)$ on the vector subspace; the centre and the vector subspace are the only orthogonal pair among the remarkable subspaces, as for every pairing. The comparison with the indefinite reading of the same remarkable subspaces is *The Four Pairings of the Biquaternion Algebra*, §*The Two Readings*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde P,\tilde Q\rangle_{*}=\sum_\mu P_\mu\overline{Q_\mu}$ | the general plain sesquilinear form |
| $\mathrm{I}_2,\mathrm{I}_6,\mathrm{I}_4$ | the restriction matrices on the centre, the vector subspace and each four-dimensional subspace |
| $(2,0),(6,0),(4,0)$ | the signatures of the restrictions |
| $\lVert\tilde Q\rVert_—^{2}=\sum_\mu\lvert Q_\mu\rvert^{2}$ | the definite norm the form defines |
| $O(2),O(6),O(4)$ | the real-linear automorphism groups of the restrictions |
| $U(1),U(3)$ | the complex-linear automorphism groups of the centre and the vector subspace |
| $U(4)$ | the complex-linear automorphism group of the form on the algebra |

## Further Reading

- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the form, its Hermitian symmetry and its unitary group
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the definite norm and the topology it defines
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the remarkable real subspaces and their bases
- *Remarkable Subspaces under the General Plain Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-plain-algebra-of-biquaternions.md`), for the indefinite reading of the same six by the general plain bilinear form
- *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), for the general quaternionic bilinear reading of the same six
- *Remarkable Subspaces under the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the indefinite sesquilinear reading of the same six
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms on the remarkable subspaces side by side
