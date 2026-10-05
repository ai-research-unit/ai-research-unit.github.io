# __The Real Forms of the Krein Form__

## Introduction

The Krein form $[\tilde P,\tilde Q]=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ is a Hermitian form on the biquaternion algebra; on the four real slices of the algebra it becomes a real symmetric form, and the four readings together are its real forms. This article records the real basis, the sign matrix $\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1)$, the signatures on the four slices, and the relation to the fundamental symmetry $J={}^{\natural}$.

## The Real Basis and the Sign Matrix

Write $\tilde Q=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu\,ie_\mu$ with $q_\mu,q'_\mu\in\mathbb R$. Because the Krein form is sesquilinear with the complex conjugation, its values on the real basis are

$$
[e_\mu,e_\nu]=\varepsilon_\mu\delta_{\mu\nu},\qquad
[e_\mu,ie_\nu]=-i\,\varepsilon_\mu\delta_{\mu\nu},\qquad
[ie_\mu,ie_\nu]=\varepsilon_\mu\delta_{\mu\nu}.
$$

The mixed entries are purely imaginary, so they do not contribute to the real symmetric form read on the real basis, and the sesquilinear form is real on each of the four real forms below. Its realified Gram matrix is therefore

$$
\operatorname{diag}(1,-1,-1,-1,\,1,-1,-1,-1),
$$

of **signature $(2,6)$**: positive on the two real directions $e_0$ and $ie_0$, negative on the six remaining real directions. This is the sign matrix of *The Krein Gram Matrix and the Restrictions of the Form*, read in the eight-dimensional real basis.

## The Four Real Forms

The **four real forms** of the algebra are the four real subspaces on which the Krein form is real-valued and symmetric: the quaternion subspace $\mathbb H_{\mathbb B}$, the anti-quaternion subspace $i\mathbb H_{\mathbb B}$, the Hermitian subspace $\mathbb M_+$ and the anti-Hermitian subspace $\mathbb M_-$. On each the restricted form is the one already found in *The Six Subspaces under the Krein Form*, and each carries signature $(1,3)$:

| Real form | Restricted form | Signature |
|---|---|---|
| Quaternion $\mathbb H_{\mathbb B}$ | $q_0^2-q_1^2-q_2^2-q_3^2$ | $(1,3)$ |
| Anti-quaternion $i\mathbb H_{\mathbb B}$ | $(q'_0)^2-q_1^2-q_2^2-q_3^2$ | $(1,3)$ |
| Hermitian $\mathbb M_+$ | $q_0^2-(q'_1)^2-(q'_2)^2-(q'_3)^2$ | $(1,3)$ |
| Anti-Hermitian $\mathbb M_-$ | $(q'_0)^2-q_1^2-q_2^2-q_3^2$ | $(1,3)$ |

Each real form is thus a four-dimensional Minkowski-type slice, with one positive and three negative directions. The four are exchanged in pairs by multiplication by $i$, and each contains isotropic elements but admits no totally isotropic subspace of dimension greater than one; the maximal totally isotropic subspaces of the algebra are cut across two of them, as *The Witt Index and the Maximal Isotropic Subspaces of the Krein Form* records.

## The Complex Subspaces

The two remaining distinguished subspaces are not real forms: the **centre** carries signature $(2,0)$, positive definite, and the **vector subspace** signature $(0,6)$, negative definite. They are the definite rows of the fundamental decomposition, and their pair of signs is the inertia $(2,6)$ of the form. Over the complex subspaces the Krein form is not a real pairing but a Hermitian one, and it is these two that close the algebra as $\mathbb C_{\mathbb B}\oplus\mathrm{Vect}(\mathbb B)$.

## The Relation to the Fundamental Symmetry

The real basis in which the form reads $\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1)$ is also the basis in which the **fundamental symmetry** $J={}^{\natural}$ is diagonal: $J$ fixes the centre and reverses the vector subspace, and the Krein form is the definite form twisted by $J$,

$$
[\tilde P,\tilde Q]=\langle\tilde P,J\tilde Q\rangle_* ,
$$

with $\langle\cdot,\cdot\rangle_*$ the positive definite Hermitian form. The four real forms are the slices on which this twisted form is real, and their common signature $(1,3)$ is the real shadow of the signature $(2,6)$.

## Summary

In the eight-dimensional real basis the Krein form has sign matrix $\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1)$, of signature $(2,6)$. Its real forms are the four real four-dimensional slices $\mathbb H_{\mathbb B}$, $i\mathbb H_{\mathbb B}$, $\mathbb M_+$ and $\mathbb M_-$, each of signature $(1,3)$; the centre is positive definite of signature $(2,0)$ and the vector subspace negative definite of signature $(0,6)$. The form is the definite Hermitian form twisted by the fundamental symmetry $J={}^{\natural}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1)$ | the sign matrix of the Krein form in the real basis |
| $(2,6)$ | its signature, the inertia of the form |
| $(1,3)$ | the signature of each of the four real forms |
| $[\tilde P,\tilde Q]=\langle\tilde P,J\tilde Q\rangle_*$ | the form as the definite form twisted by $J={}^{\natural}$ |

## Further Reading

- *The Biquaternion Krein Form and Its Signature* (`articles_maths/the-biquaternion-krein-form-and-its-signature.md`), for the form
- *The Six Subspaces under the Krein Form* (`articles_maths/the-six-subspaces-under-the-krein-form.md`), for the restriction table
- *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for $J={}^{\natural}$
