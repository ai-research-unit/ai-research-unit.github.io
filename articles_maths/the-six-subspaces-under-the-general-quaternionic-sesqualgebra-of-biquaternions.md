
# __The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions__

## Introduction

The general quaternionic sesquilinear form $\langle\tilde Q,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde Q^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu|Q_\mu|^{2}$ of *The Krein Gram Matrix and the Restrictions of the Form*, of signature $(2,6)$, is read here on the six distinguished real subspaces of *Introduction to the Six Subspaces* — the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$.

The form is used, not re-derived. Its definition, its Krein signature $(2,6)$ and its automorphism group $U(1,3)$ are the matter of *The Krein Gram Matrix and the Restrictions of the Form*; its Gram matrices and the signature of each restriction are *The Krein Gram Matrix and the Restrictions of the Form*; its null set and its totally isotropic subspaces are *The Isotropic Structure of the General Quaternionic Sesqualgebra*; the six subspaces and their bases are *Introduction to the Six Subspaces*; and the companion readings of the same six by the other three pairings are *The Six Subspaces under the General Plain Algebra of Biquaternions*, *The Six Subspaces under the General Quaternionic Algebra of Biquaternions* and *The Six Subspaces under the General Plain Sesqualgebra of Biquaternions*. This article owns the restrictions themselves and the structure of each one.

## The Six Restriction Matrices

The form differs from the Euclidean square by the sign vector $\varepsilon=(1,-1,-1,-1)$ on the vector directions, so on the six subspaces it is either the Euclidean square, its negative, or a Lorentzian form. In the natural real basis of each subspace it is diagonal, and the diagonals are the sign strings below.

| Subspace | Natural real basis | Restricted form | Restriction matrix | Signature | Character |
|---|---|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | $e_0,\,ie_0$ | $\lvert Q_0\rvert^{2}=q_0^{2}+(q'_0)^{2}$ | $\operatorname{diag}(1,1)$ | $(2,0)$ | positive definite |
| Vector $\mathrm{Vect}(\mathbb{B})$ | $e_1,e_2,e_3,\,ie_1,ie_2,ie_3$ | $-\sum_k\lvert Q_k\rvert^{2}$ | $-\mathrm{I}_6$ | $(0,6)$ | negative definite |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | $e_0,e_1,e_2,e_3$ | $q_0^{2}-q_1^{2}-q_2^{2}-q_3^{2}$ | $\mathrm{E}$ | $(1,3)$ | indefinite |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $ie_0,ie_1,ie_2,ie_3$ | $(q'_0)^{2}-(q'_1)^{2}-(q'_2)^{2}-(q'_3)^{2}$ | $\mathrm{E}$ | $(1,3)$ | indefinite |
| Hermitian $\mathbb{M}_+$ | $e_0,ie_1,ie_2,ie_3$ | $q_0^{2}-(q'_1)^{2}-(q'_2)^{2}-(q'_3)^{2}$ | $\mathrm{E}$ | $(1,3)$ | indefinite |
| Anti-Hermitian $\mathbb{M}_-$ | $ie_0,e_1,e_2,e_3$ | $(q'_0)^{2}-q_1^{2}-q_2^{2}-q_3^{2}$ | $\mathrm{E}$ | $(1,3)$ | indefinite |

**Proposition (the matrices).** In the natural real basis displayed the restriction is diagonal with entries $\varepsilon_\mu$ on the four-dimensional rows and with entries $1,1$ on the centre and $-1$ on the vector subspace; each restriction is non-degenerate, with Gram determinant $\pm1$.

*Proof.* In the real basis of the algebra the form is diagonal with the signs $\varepsilon,\varepsilon$, since $\langle e_\mu,e_\nu\rangle_{\natural*}=\varepsilon_\mu\delta_{\mu\nu}$ and $\langle ie_\mu,ie_\nu\rangle_{\natural*}=\varepsilon_\mu|i|^{2}\delta_{\mu\nu}=\varepsilon_\mu\delta_{\mu\nu}$, while the mixed entries have vanishing real part. The natural real basis of each subspace is a subset of the algebra's real basis, so each restriction is the corresponding principal submatrix. On the centre the basis is $\{e_0,ie_0\}$, giving $\operatorname{diag}(1,1)$; on the vector subspace it is $\{e_k,ie_k\}$, where the signs are all $-1$; and on each four-dimensional subspace the basis selects one direction of each complex coordinate, giving the sign string $\varepsilon$ in a different order.

**Remark (the four real forms carry the interval form).** On each of the four four-dimensional real subspaces the restriction is a Lorentzian form of signature $(1,3)$: it is the interval form of Minkowski space, with one timelike and three spacelike directions. The four selections of the timelike direction are the four real subspaces: the real scalar direction $e_0$ on $\mathbb{H}_{\mathbb{B}}$, the imaginary scalar direction $ie_0$ on $i\mathbb{H}_{\mathbb{B}}$, the real scalar direction again on $\mathbb{M}_+$, and the imaginary scalar direction again on $\mathbb{M}_-$.

## The Definite Rows and the Fundamental Decomposition

Two of the six rows are definite. On the **centre** the form is positive definite, of signature $(2,0)$, and on the **vector subspace** it is negative definite, of signature $(0,6)$. The two are the **fundamental decomposition** of the Krein space,

$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\perp^{+}\mathrm{Vect}(\mathbb{B}),
\qquad (2,0)+(0,6)=(2,6),
$$

and they realise the whole positive index $2$ and the whole negative index $6$ of the ambient signature.

**Proposition (the maximal definite dimensions).** The maximal dimension of a positive definite subspace of the form is $2$, attained by the centre, and the maximal dimension of a negative definite subspace is $6$, attained by the vector subspace; the four remaining subspaces are indefinite of signature $(1,3)$.

*Proof.* The positive index of the form is $2$ and its negative index $6$, so a definite subspace has dimension at most the corresponding index; the centre and the vector subspace attain the bounds, being definite of those dimensions by the table. The four remaining rows are indefinite of signature $(1,3)$, so they contain directions of both signs.

Each of the four indefinite rows carries a **real light cone**, of real dimension $3$, which is the cone of the nonzero null elements of the row and the cone of the zero divisors that lie in it:

| Subspace | Null cone | Real dimension |
|---|---|---|
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | $q_0^{2}=q_1^{2}+q_2^{2}+q_3^{2}$ | $3$ |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $(q'_0)^{2}=(q'_1)^{2}+(q'_2)^{2}+(q'_3)^{2}$ | $3$ |
| Hermitian $\mathbb{M}_+$ | $q_0^{2}=(q'_1)^{2}+(q'_2)^{2}+(q'_3)^{2}$ | $3$ |
| Anti-Hermitian $\mathbb{M}_-$ | $(q'_0)^{2}=q_1^{2}+q_2^{2}+q_3^{2}$ | $3$ |

**Remark (the isotropic lines of a row).** On each indefinite row the null cone is a quadratic cone of real dimension $3$, whose isotropic real lines are parametrised by the real unit directions; the maximal dimension of a totally isotropic subspace is $1$ on each row, since the signature is $(1,3)$ and the Witt index of a Lorentzian form is $1$. On the two definite rows there is no isotropic element, and on the centre and the vector subspace the form is definite, so the origin is the only isotropic point. The isotropic structure of the form on the whole algebra, where the Witt index over $\mathbb{R}$ is $2$, is *The Isotropic Structure of the General Quaternionic Sesqualgebra*.

## The Coincidences with the Other Three Forms

On the six subspaces the general quaternionic sesquilinear form coincides with one of the other pairings, up to a sign, on every row:

| Subspace | Coincidence |
|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | equals the general plain sesquilinear form, $\lvert Q_0\rvert^{2}$ |
| Vector $\mathrm{Vect}(\mathbb{B})$ | equals the negative of the general plain sesquilinear form |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | equals the general plain bilinear form |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | equals the general plain bilinear form |
| Hermitian $\mathbb{M}_+$ | equals the general quaternionic bilinear form |
| Anti-Hermitian $\mathbb{M}_-$ | equals the negative of the general quaternionic bilinear form |

**Proof.** On the centre the sign $\varepsilon_0=1$ leaves $\lvert Q_0\rvert^{2}$, which is the general plain sesquilinear restriction; on the vector subspace the three signs $\varepsilon_k=-1$ give $-\sum_k\lvert Q_k\rvert^{2}$, the negative of the general plain sesquilinear restriction. On $\mathbb{H}_{\mathbb{B}}$ the coefficients are real, so $\lvert Q_\mu\rvert^{2}=Q_\mu^{2}$ and the form reads $\sum_\mu\varepsilon_\mu Q_\mu^{2}$, which is the general plain bilinear restriction; on $i\mathbb{H}_{\mathbb{B}}$ the coefficients are $iq'_\mu$, so $\lvert Q_\mu\rvert^{2}=(q'_\mu)^{2}$ and the form reads $\sum_\mu\varepsilon_\mu(q'_\mu)^{2}$, again the general plain bilinear restriction, the two signs of $i^{2}$ cancelling. On $\mathbb{M}_+$ the scalar coefficient is real and the vector coefficients are $ip_k$, so the form reads $q_0^{2}-\sum_kp_k^{2}$, which is the general quaternionic bilinear restriction $\sum_\mu Q_\mu^{2}=q_0^{2}+\sum_k(ip_k)^{2}$; on $\mathbb{M}_-$ the scalar coefficient is $ib_0$ and the vector coefficients are real, so the form reads $b_0^{2}-\sum_kq_k^{2}$ while the general quaternionic bilinear restriction reads $-b_0^{2}+\sum_kq_k^{2}$, the negative.

**Remark (the coincidence is not an identity).** The coincidences are accidental to the subspace and do not extend to the algebra: the four forms are pairwise distinct there, of signatures $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$. The comparison of the four on the same six subspaces is *The Four Pairings of the Biquaternion Algebra*.

## The Automorphism Groups of the Restrictions

**Definition.** For each subspace $V$ of the six, the **automorphism group of the restriction** is the group of real-linear maps of $V$ preserving the restriction. Since each restriction is non-degenerate, it is the real orthogonal group of its signature.

| Subspace | Signature | Automorphism group | Real dimension | Definite |
|---|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | $(2,0)$ | $O(2)$ | $1$ | yes |
| Vector $\mathrm{Vect}(\mathbb{B})$ | $(0,6)$ | $O(6)$ | $15$ | yes |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | $(1,3)$ | $O(1,3)$ | $6$ | no |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $(1,3)$ | $O(1,3)$ | $6$ | no |
| Hermitian $\mathbb{M}_+$ | $(1,3)$ | $O(1,3)$ | $6$ | no |
| Anti-Hermitian $\mathbb{M}_-$ | $(1,3)$ | $O(1,3)$ | $6$ | no |

**Proof.** A real-linear automorphism of a non-degenerate real symmetric form of signature $(p,q)$ is an element of $O(p,q)$, of real dimension $n(n-1)/2$ with $n=p+q$, giving $1$, $15$ and $6$; the two definite rows give $O(2)$ and $O(6)\cong O(0,6)$, and the four Lorentzian rows give $O(1,3)$ four times.

**Remark (the ambient Krein group).** The complex-linear automorphism group of the form on the algebra is the indefinite unitary group $U(1,3)$ of real dimension $16$, of *The Krein Gram Matrix and the Restrictions of the Form*; the real-linear automorphism group of the realified form is the larger $O(2,6)$. The groups of the table are the largest groups preserving the restriction of the form to a subspace, and they are not induced by the ambient group: an automorphism of the ambient form need not preserve a given subspace.

## Worked Examples

**A positive central element.** For $\tilde Q=e_0$ the value is $\varepsilon_0|1|^{2}=1$, and for $\tilde Q=e_0+ie_0$ it is $1+1=2$, in agreement with the positive definiteness of the centre and its signature $(2,0)$.

**A negative vector element.** For $\tilde Q=e_1$ the value is $\varepsilon_1|1|^{2}=-1$, and for $\tilde Q=e_1+ie_1$ it is $-1-1=-2$; the vector subspace is negative definite, and it realises the negative index $6$ of the form.

**The null element of the quaternion row.** For $\tilde Q=e_0+e_1$ the value is $1-1=0$, and the element lies on the light cone $q_0^{2}=q_1^{2}+q_2^{2}+q_3^{2}$ of the quaternion subspace; it is a zero divisor of the algebra, and the Peirce lines it carries are those of *The Isotropic Structure of the General Quaternionic Sesqualgebra*.

**The null element of the anti-quaternion row.** For $\tilde Q=ie_0+ie_1$ the value is $1-1=0$, on the cone $(q'_0)^{2}=\sum_k(q'_k)^{2}$ of the anti-quaternion subspace; the sign of the scalar coefficient is the one the row prescribes.

**The null element of the Hermitian row.** For $\tilde Q=e_0+ie_1$ the value is $1-1=0$, on the cone $q_0^{2}=\sum_k(q'_k)^{2}$ of $\mathbb{M}_+$; the same element is null for the general quaternionic bilinear form, with which the form coincides on this row.

**The null element of the anti-Hermitian row.** For $\tilde Q=ie_0+e_1$ the value is $1-1=0$, on the cone $(q'_0)^{2}=\sum_kq_k^{2}$ of $\mathbb{M}_-$.

**A maximal totally isotropic real plane.** On the quaternion subspace the span $\mathbb{R}\{e_0+e_1,\ i(e_0+e_1)\}$ is a totally isotropic real plane, of the maximal dimension $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$ that the Witt index of the form allows; the complex line $\mathbb{C}(e_0+e_1)$ is one of its isotropic lines.

**The centre is not isotropic.** For a central element $Ae_0$ with $A=q_0+iq'_0$ the value is $\lvert A\rvert^{2}=q_0^{2}+(q'_0)^{2}$, which vanishes only at $A=0$: the centre is the positive definite half of the fundamental decomposition, and its only isotropic point is the origin.

## Summary

On the six distinguished real subspaces the general quaternionic sesquilinear form carries the signatures $(2,0)$, $(0,6)$ and four copies of $(1,3)$, with the restriction matrices $\operatorname{diag}(1,1)$ on the centre, $-\mathrm{I}_6$ on the vector subspace and $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$ on each of the four four-dimensional subspaces. The centre and the vector subspace are the definite rows, of dimensions $2$ and $6$ and opposite signs, and they are the fundamental decomposition of the Krein space, realising the positive index $2$ and the negative index $6$ of the ambient signature. The four remaining rows are Lorentzian, each with a real light cone of dimension $3$ whose isotropic lines are parametrised by the real unit directions; the maximal totally isotropic dimension is $1$ on each of them, and the form is definite on the two remaining rows. On all six the form coincides with one of the other pairings, up to a sign: with the general plain sesquilinear form on the centre, with the negative of it on the vector subspace, with the general plain bilinear form on the quaternion and anti-quaternion subspaces, and with the general quaternionic bilinear form, up to a sign, on the two Hermitian subspaces. The automorphism groups are $O(2)$, $O(6)$ and four copies of $O(1,3)$. The comparison with the three other pairings on the same six subspaces is *The Four Pairings of the Biquaternion Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde P,\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the general quaternionic sesquilinear form |
| $(2,0),(0,6),(1,3)$ | the signatures of the six restrictions |
| $\operatorname{diag}(1,1)$, $-\mathrm{I}_6$, $\mathrm{E}$ | the restriction matrices on the centre, the vector subspace and the four four-dimensional subspaces |
| $\mathbb{C}_{\mathbb{B}}\perp^{+}\mathrm{Vect}(\mathbb{B})$ | the fundamental decomposition $(2,0)+(0,6)$ |
| $q_0^{2}=\sum_kq_k^{2}$, etc. | the four light cones, of real dimension $3$ |
| $O(2),O(6),O(1,3)$ | the automorphism groups of the restrictions |
| $U(1,3)$ | the complex-linear automorphism group of the form on the algebra |

## Further Reading

- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the Gram matrices and the signature of each restriction
- *The Isotropic Structure of the General Quaternionic Sesqualgebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-sesqualgebra.md`), for the null set, the isotropic lines and the Witt index
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six distinguished real subspaces and their bases
- *The Six Subspaces under the General Plain Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-plain-sesqualgebra-of-biquaternions.md`), for the definite companion reading of the same six
- *The Six Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), for the norm reading of the same six
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms on the six subspaces side by side
