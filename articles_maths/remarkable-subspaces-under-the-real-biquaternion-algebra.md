
# __Remarkable Subspaces under the Real Biquaternion Algebra__

## Introduction

The **trace form** of the real biquaternion algebra, $\tau(\tilde P,\tilde Q)=\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})=8\,\mathrm{Re}\langle\tilde P,\tilde Q\rangle$, is the canonical symmetric bilinear form the ring carries before any of the four complex forms is chosen, of signature $(4,4)$. It is read here on the remarkable real subspaces of *Introduction to the Remarkable Subspaces* — the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$.

The form is used, not re-derived. Its definition from the regular representation, its Gram matrix $8\cdot\operatorname{diag}(1,-1,-1,-1,-1,1,1,1)$, its signature $(4,4)$ and its invariance under the algebra automorphisms are the matter of *The Trace Form of the Real Biquaternion Algebra*; the realified reading of the four complex forms, of which this one is the eighth part, is *The Realification of the Four Forms*; the remarkable subspaces and their bases are *Introduction to the Remarkable Subspaces*; and the companion readings of the same six by the complex forms are *Remarkable Subspaces under the General Plain Algebra of Biquaternions*, *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions*, *Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions* and *Remarkable Subspaces under the General Quaternionic Sesqualgebra of Biquaternions*. This article owns the restrictions themselves and the structure of each one.

## The Restriction Matrices

The trace form is the realified general plain bilinear form rescaled by the factor $8$, so its restrictions are those of the general plain bilinear form rescaled, and their signatures are the same. In the natural real basis of each subspace the restriction is diagonal.

| Subspace | Natural real basis | Restricted trace form | Restriction matrix | Signature |
|---|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | $e_0,\,ie_0$ | $8\bigl(q_0^{2}-(q'_0)^{2}\bigr)$ | $8\operatorname{diag}(1,-1)$ | $(1,1)$ |
| Vector $\mathrm{Vect}(\mathbb{B})$ | $e_1,e_2,e_3,\,ie_1,ie_2,ie_3$ | $8\bigl(\sum_k(q'_k)^{2}-\sum_kq_k^{2}\bigr)$ | $8\operatorname{diag}(-1,-1,-1,1,1,1)$ | $(3,3)$ |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | $e_0,e_1,e_2,e_3$ | $8\bigl(q_0^{2}-q_1^{2}-q_2^{2}-q_3^{2}\bigr)$ | $8\mathrm{E}$ | $(1,3)$ |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $ie_0,ie_1,ie_2,ie_3$ | $8\bigl(-(q'_0)^{2}+(q'_1)^{2}+(q'_2)^{2}+(q'_3)^{2}\bigr)$ | $-8\mathrm{E}$ | $(3,1)$ |
| Hermitian $\mathbb{M}_+$ | $e_0,ie_1,ie_2,ie_3$ | $8\bigl(q_0^{2}+(q'_1)^{2}+(q'_2)^{2}+(q'_3)^{2}\bigr)$ | $8\mathrm{I}_4$ | $(4,0)$ |
| Anti-Hermitian $\mathbb{M}_-$ | $ie_0,e_1,e_2,e_3$ | $-8\bigl((q'_0)^{2}+q_1^{2}+q_2^{2}+q_3^{2}\bigr)$ | $-8\mathrm{I}_4$ | $(0,4)$ |

**Proposition (the matrices).** In the natural real basis displayed the restriction is the matrix tabulated, each restriction is non-degenerate, and its Gram determinant is $\pm8^{\dim}$.

*Proof.* The values of the trace form on the real basis are $\tau(e_\mu,e_\nu)=8\varepsilon_\mu\delta_{\mu\nu}$, $\tau(e_\mu,ie_\nu)=0$ and $\tau(ie_\mu,ie_\nu)=-8\varepsilon_\mu\delta_{\mu\nu}$, so in the real basis of the algebra the form is $8\cdot\operatorname{diag}(1,-1,-1,-1,-1,1,1,1)$. The natural real basis of each subspace is a subset of the algebra's real basis, so the restriction is the corresponding principal submatrix, of the stated size; the diagonal values of the table follow by substituting the real coordinates of the subspace. Each matrix is invertible because every diagonal entry is $\pm8$.

**Remark (the same table as the general plain bilinear form).** The trace form is the realified general plain bilinear form in the units the regular representation provides, and the two tables differ by the factor $8$ in every entry: a subspace has the same signature for $\tau$ as for $\mathrm{Re}\langle\cdot,\cdot\rangle$, and the same automorphism group. The complex-bilinear reading of the table, with the complex form and the complex automorphism groups, is *Remarkable Subspaces under the General Plain Algebra of Biquaternions*; the entry point of the reading here is that no conjugation and no complex scalar enters the definition, only the trace of a product of left multiplications.

## The Definite Rows and the Orthogonal Splitting

The four positive directions of the trace form on the algebra are $e_0,ie_1,ie_2,ie_3$ and the four negative directions are $e_1,e_2,e_3,ie_0$. The positive directions are exactly the natural basis of the **Hermitian subspace** $\mathbb{M}_+$ and the negative directions exactly the natural basis of the **anti-Hermitian subspace** $\mathbb{M}_-$.

**Theorem (the definite rows).** On $\mathbb{M}_+$ the trace form is positive definite, of signature $(4,0)$, and on $\mathbb{M}_-$ it is negative definite, of signature $(0,4)$; the two are orthogonal,

$$
\mathbb{B}=\mathbb{M}_+\perp\mathbb{M}_-,
\qquad \tau(\tilde P,\tilde R)=\tau(\tilde P_+,\tilde R_+)+\tau(\tilde P_-,\tilde R_-),
$$

on the splitting of an element into its Hermitian and anti-Hermitian parts, and the signature $(4,4)$ of the algebra is the sum $(4,0)+(0,4)$ of the two.

*Proof.* The restriction to $\mathbb{M}_+$ is $8\sum$ of four squares and the restriction to $\mathbb{M}_-$ is $-8\sum$ of four squares by the table, so the first is positive definite and the second negative definite; the mixed values $\tau(e_\mu,ie_\nu)$ vanish, so each Hermitian basis direction is orthogonal to each anti-Hermitian one, and the splitting is orthogonal. The signatures add because the decomposition is orthogonal and covers the algebra.

**Proposition (the maximal definite dimensions).** The maximal dimension of a positive definite subspace of the trace form is $4$, attained by $\mathbb{M}_+$, and the maximal dimension of a negative definite subspace is $4$, attained by $\mathbb{M}_-$; the remarkable subspaces contain definite subspaces of dimension $4$ on the quaternion subspace, $1$ on the centre, $3$ on the vector subspace and $2$ on the anti-quaternion subspace.

*Proof.* The bounds are the two inertia indices $4,4$ of the form, attained on the two rows; on a restriction of signature $(p,q)$ the maximal definite dimensions are $p$ and $q$, read from the signatures $(1,1)$, $(3,3)$, $(1,3)$ and $(3,1)$ of the four indefinite rows.

## The Null Cones of the Indefinite Rows

Four of the restrictions are indefinite, of signatures $(1,1)$, $(3,3)$, $(1,3)$ and $(3,1)$, and their null sets are the realified cone of the general plain bilinear form, read on the subspace; their real dimensions are one less than the dimension of the subspace.

| Subspace | Signature | Null element | Null cone, real dimension |
|---|---|---|---|
| Centre | $(1,1)$ | $e_0+ie_0$ | $1$, the two lines $\mathbb{R}(e_0\pm ie_0)$ |
| Vector | $(3,3)$ | $e_1+ie_1$ | $5$ |
| Quaternion | $(1,3)$ | $e_0+e_1$ | $3$ |
| Anti-quaternion | $(3,1)$ | $ie_0+ie_1$ | $3$ |

*Proof.* Each displayed element is null for the restriction of its row: on the centre $8(1-1)=0$, on the vector subspace $8(1-1)=0$, on the quaternion subspace $8(1-1)=0$ and on the anti-quaternion subspace $8(-1+1)=0$. On an indefinite form of signature $(p,q)$ the null set of the diagonal is the zero set of a non-constant homogeneous quadratic polynomial, of real dimension one less than the space. The two definite rows have no null element beyond the origin.

**Remark (the null cones are not the zero-divisor cone).** The four cones lie in the realified null cone $\{\tau=0\}$ of the algebra, of real dimension $7$, which is not the zero-divisor cone of the norm: on the quaternion subspace the zero-divisor condition $\sum_\mu Q_\mu^{2}=0$ has no nonzero real solution, while the trace-form null cone there is the $(1,3)$ cone $q_0^{2}=\sum_kq_k^{2}$ computed above. The two cones of the algebra are compared in *The Four Pairings of the Biquaternion Algebra*, §*The Null Sets Compared*. On the two definite rows the trace-form null set is the origin.

## The Automorphism Groups of the Restrictions

**Definition.** For each subspace $V$ of the remarkable subspaces, the **automorphism group of the restriction** is the group of real-linear maps of $V$ preserving the restriction. Since a rescaling of a form does not change its automorphisms, the groups are those of the realified general plain bilinear form; since each restriction is non-degenerate, the group is the real orthogonal group of its signature.

| Subspace | Signature | Automorphism group | Real dimension |
|---|---|---|---|
| Centre | $(1,1)$ | $O(1,1)$ | $1$ |
| Vector | $(3,3)$ | $O(3,3)$ | $15$ |
| Quaternion | $(1,3)$ | $O(1,3)$ | $6$ |
| Anti-quaternion | $(3,1)$ | $O(3,1)\cong O(1,3)$ | $6$ |
| Hermitian | $(4,0)$ | $O(4)$ | $6$ |
| Anti-Hermitian | $(0,4)$ | $O(4)$ | $6$ |

**Proof.** The automorphisms of $\tau$ and of $\mathrm{Re}\langle\cdot,\cdot\rangle=\tfrac18\tau$ are the same group, since a scalar multiple of a form has the same preserving maps; the groups of the realified general plain bilinear form are the ones tabulated, by the computation of *Remarkable Subspaces under the General Plain Algebra of Biquaternions*.

**Remark (the automorphisms of the algebra inside the orthogonal group).** The trace form is built from the ring alone, and every automorphism of the real algebra preserves it: $\tau(\varphi\tilde P,\varphi\tilde Q)=\tau(\tilde P,\tilde Q)$ for $\varphi\in\mathrm{Aut}(\mathbb{B})$, since $\varphi$ conjugates the left multiplications. The automorphism group is therefore a subgroup of the orthogonal group $O(4,4)$ of the form, and its elements carry the remarkable subspaces to subspaces of the same signature; the form is the real-algebra analogue of the invariance of the four complex forms under their own automorphism groups. The automorphisms themselves are *The Automorphisms and Derivations of the Real Biquaternion Algebra*.

## Worked Examples

**The trace of a unit.** The value on a real basis element is $\tau(e_0,e_0)=8$, $\tau(e_1,e_1)=-8$, $\tau(ie_0,ie_0)=-8$ and $\tau(ie_1,ie_1)=8$, the four signs of the diagonal $8\cdot\operatorname{diag}(1,-1,-1,-1,-1,1,1,1)$.

**A null element of the centre.** For $\tilde Q=e_0+ie_0$ the value is $8(1-1)=0$, on the two real lines $\mathbb{R}(e_0\pm ie_0)$; the element is a unit of the algebra and a null element of the trace form, which is the general fact that the trace form is indefinite.

**A null element of the vector subspace.** For $\tilde Q=e_1+ie_1$ the value is $8(1-1)=0$, and the real plane $\mathrm{span}_{\mathbb{R}}\{e_1+ie_1,e_2+ie_2,e_3+ie_3\}$ is totally isotropic of dimension $3$, the maximal one for signature $(3,3)$.

**A null element of the quaternion subspace.** For $\tilde Q=e_0+e_1$ the value is $8(1-1)=0$, on the cone $q_0^{2}=q_1^{2}+q_2^{2}+q_3^{2}$; the element is a zero divisor of the algebra, since $\sum_\mu Q_\mu^{2}=1-1=0$ for the norm as well.

**A null element of the anti-quaternion subspace.** For $\tilde Q=ie_0+ie_1$ the value is $8(-1+1)=0$, on the cone $(q'_0)^{2}=(q'_1)^{2}+(q'_2)^{2}+(q'_3)^{2}$ of the row.

**The two definite rows.** For $\tilde Q=e_0+ie_1$ in $\mathbb{M}_+$ the value is $8(1+1)=16$, and for $\tilde Q=ie_0+e_1$ in $\mathbb{M}_-$ it is $-8(1+1)=-16$: the two elements are of opposite signs, and no nonzero element of either row is null.

**The factor eight.** On $\mathbb{H}_{\mathbb{B}}$ the restricted trace form is $8$ times the interval form $q_0^{2}-q_1^{2}-q_2^{2}-q_3^{2}$, and the same factor relates the two Gram matrices on each of the rows; the factor is the real dimension $8$ of the carrier of the regular representation, and the complex-bilinear reading of the same restriction is *Remarkable Subspaces under the General Plain Algebra of Biquaternions*.

## Summary

On the remarkable real subspaces the trace form carries the restrictions $8\operatorname{diag}(1,-1)$ on the centre, $8\operatorname{diag}(-1,-1,-1,1,1,1)$ on the vector subspace, $8\mathrm{E}$ on the quaternion subspace, $-8\mathrm{E}$ on the anti-quaternion subspace, $8\mathrm{I}_4$ on the Hermitian subspace and $-8\mathrm{I}_4$ on the anti-Hermitian subspace, of signatures $(1,1)$, $(3,3)$, $(1,3)$, $(3,1)$, $(4,0)$ and $(0,4)$. The Hermitian subspace is the maximal positive definite one and the anti-Hermitian the maximal negative definite one, both of dimension $4$, and they are the orthogonal splitting of the algebra realising the signature $(4,4)$; the four remaining rows are indefinite, with null cones of real dimensions $1$, $5$, $3$ and $3$ and the null elements $e_0+ie_0$, $e_1+ie_1$, $e_0+e_1$ and $ie_0+ie_1$. The automorphism groups are $O(1,1)$, $O(3,3)$, $O(1,3)$, $O(3,1)$, $O(4)$ and $O(4)$, and the automorphisms of the algebra form a subgroup of $O(4,4)$ preserving the form. The table is the table of the realified general plain bilinear form rescaled by the dimension $8$; its complex-bilinear reading is *Remarkable Subspaces under the General Plain Algebra of Biquaternions*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau(\tilde P,\tilde Q)=\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})=8\,\mathrm{Re}\langle\tilde P,\tilde Q\rangle$ | the trace form of the real algebra |
| $8\operatorname{diag}(1,-1,-1,-1,-1,1,1,1)$ | its Gram matrix in the real basis |
| $(1,1),(3,3),(1,3),(3,1),(4,0),(0,4)$ | the signatures of the restrictions |
| $e_0,ie_1,ie_2,ie_3$ | the four positive directions, the basis of $\mathbb{M}_+$ |
| $e_1,e_2,e_3,ie_0$ | the four negative directions, the basis of $\mathbb{M}_-$ |
| $\mathbb{M}_+\perp\mathbb{M}_-$ | the orthogonal splitting $(4,0)+(0,4)$ |
| $O(1,1),O(3,3),O(1,3),O(3,1),O(4)$ | the automorphism groups of the restrictions |
| $\mathrm{Aut}(\mathbb{B})\subset O(4,4)$ | the automorphisms inside the orthogonal group of the form |

## Further Reading

- *The Trace Form of the Real Biquaternion Algebra* (`articles_maths/the-trace-form-of-the-real-biquaternion-algebra.md`), for the form, its Gram matrix and its signature
- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the realified reading of the four forms, of which this is the eighth part
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the remarkable real subspaces and their bases
- *Remarkable Subspaces under the General Plain Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-plain-algebra-of-biquaternions.md`), for the complex-bilinear reading of the same table
- *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), for the norm reading of the same six
- *The Automorphisms and Derivations of the Real Biquaternion Algebra* (`articles_maths/the-automorphisms-and-derivations-of-the-real-biquaternion-algebra.md`), for the automorphisms preserving the form
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms on the remarkable subspaces side by side
