# __The Six Subspaces under the Krein Form__

## Introduction

The Krein form

$$
[\tilde P,\tilde Q]=\mathrm{Sc}(\tilde P^{\natural*}\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu},\qquad \varepsilon=(1,-1,-1,-1),
$$

of *The Biquaternion Krein Form and Its Signature* is read here on the six distinguished real subspaces. On each it is real-valued and symmetric, and this article records the six signatures, the two definite rows, the totally isotropic subspaces, the fundamental decomposition, and the comparison with the definite Hermitian form.

## The Six Signatures

With $\tilde Q=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu\,ie_\mu$, the Krein form on the six subspaces is diagonal and the signatures are read at once:

| Subspace | Real dimension | Restricted form | Signature |
|---|---|---|---|
| Centre $\mathbb C_{\mathbb B}$ | $2$ | $q_0^2+(q'_0)^2$ | $(2,0)$ |
| Vector $\mathrm{Vect}(\mathbb B)$ | $6$ | $-\sum_k\bigl(q_k^2+(q'_k)^2\bigr)$ | $(0,6)$ |
| Quaternion $\mathbb H_{\mathbb B}$ | $4$ | $q_0^2-q_1^2-q_2^2-q_3^2$ | $(1,3)$ |
| Anti-quaternion $i\mathbb H_{\mathbb B}$ | $4$ | $(q'_0)^2-q_1^2-q_2^2-q_3^2$ | $(1,3)$ |
| Hermitian $\mathbb M_+$ | $4$ | $q_0^2-(q'_1)^2-(q'_2)^2-(q'_3)^2$ | $(1,3)$ |
| Anti-Hermitian $\mathbb M_-$ | $4$ | $(q'_0)^2-q_1^2-q_2^2-q_3^2$ | $(1,3)$ |

## The Two Definite Rows and the Fundamental Decomposition

Two rows are definite. On the **centre** the form is positive definite, of signature $(2,0)$; on the **vector subspace** it is negative definite, of signature $(0,6)$. The centre and the vector subspace are Krein-orthogonal,

$$
[\tilde P,\tilde Q]=0\quad\text{for }\tilde P\in\mathbb C_{\mathbb B},\ \tilde Q\in\mathrm{Vect}(\mathbb B),
$$

and together they fill the algebra, $\mathbb C_{\mathbb B}\oplus\mathrm{Vect}(\mathbb B)=\mathbb B$. This is the **fundamental decomposition** of the algebra for the Krein form: a positive definite part of dimension $2$ and a negative definite part of dimension $6$, whose signs are the inertia $(2,6)$ of *The Biquaternion Krein Form and Its Signature*. The corresponding fundamental symmetry is $J={}^{\natural}$, the natural conjugation, whose $+1$-eigenspace is the centre and whose $-1$-eigenspace is the vector subspace.

## The Totally Isotropic Subspaces

The four real forms carry signature $(1,3)$ each, so each contains isotropic elements but no totally isotropic subspace of dimension greater than one within itself; the totally isotropic subspaces of the algebra are cut across the rows. The Krein form is non-degenerate, and by Sylvester's law its **Witt index** is the minimum of the inertia, $\min(2,6)=2$: the algebra contains totally isotropic subspaces of real dimension $2$, and none larger. The maximal isotropic complex line and the maximal isotropic real plane are described in *The Witt Index and the Maximal Isotropic Subspaces of the Krein Form*; the isotropic lines form a copy of $S^5$, the boundary of the complex hyperbolic ball, as *The Isotropic Structure of the Krein Form* records. The centre and the vector subspace, being definite, contain no isotropic element beyond the origin.

## Comparison with the Definite Hermitian Form

The Hermitian form $\langle\tilde P,\tilde Q\rangle_*=\sum_\mu P_\mu\overline{Q_\mu}$ of *The Hermitian Form on the Biquaternion Algebra* is positive definite, of signature $(8,0)$, and its table is $(2,0)$, $(6,0)$, $(4,0)$, $(4,0)$, $(4,0)$, $(4,0)$. The Krein form differs from it by the sign vector $\varepsilon$, and the difference is confined to the vector subspace and the four real forms: the centre is positive definite for both, and the vector subspace is definitively **negative** for the Krein form against positive for the Hermitian one. That single sign change is the whole of the passage from the Hilbert structure to the Pontryagin structure.

## Summary

On the six distinguished real subspaces the Krein form carries the signatures $(2,0)$ on the centre, $(0,6)$ on the vector subspace and $(1,3)$ on each of the quaternion, anti-quaternion, Hermitian and anti-Hermitian subspaces. The centre and the vector subspace are its definite rows and form the fundamental decomposition, with fundamental symmetry $J={}^{\natural}$; the Witt index is $2$, the four real forms each carry signature $(1,3)$, and the form differs from the positive definite Hermitian form by the sign vector $\varepsilon$ on the vector subspace and the four real forms alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(2,0),(0,6),(1,3)$ | the signatures on the six subspaces |
| $\mathbb C_{\mathbb B}\oplus\mathrm{Vect}(\mathbb B)$ | the fundamental decomposition, $J={}^{\natural}$ |
| $\min(2,6)=2$ | the Witt index |

## Further Reading

- *The Biquaternion Krein Form and Its Signature* (`articles_maths/the-biquaternion-krein-form-and-its-signature.md`), for the form
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the Gram matrix and the restrictions
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the definite companion
