# __The Gram Matrix of the Complex Bilinear Form__

## Introduction

The complex bilinear form

$$
\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu,\qquad \varepsilon=(1,-1,-1,-1),
$$

of *The Complex Bilinear Form on the Biquaternion Algebra* is read from a single matrix once a basis is fixed. In the coefficient basis $(e_0,e_1,e_2,e_3)$ its Gram matrix is the **sign matrix**

$$
D=\operatorname{diag}(1,-1,-1,-1),
$$

of determinant $-1$; on the eight real basis elements $(e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3)$ the realified matrix is the block-diagonal $\operatorname{diag}(D,-D)$, of signature $(4,4)$. This article records the two matrices, the six restriction matrices, and the comparison with the quaternion bilinear form, whose matrix is $\mathrm{I}_4$.

## The Gram Matrix in the Coefficient Basis

**Definition.** The Gram matrix of the form in the coefficient basis is

$$
G_{ij}=\langle e_i,e_j\rangle=\varepsilon_i\,\delta_{ij},
\qquad
G=\operatorname{diag}(1,-1,-1,-1)=D.
$$

Its properties are read off at once. It is symmetric, $D^{\mathsf T}=D$, as a bilinear form must be; it is non-degenerate, $\det D=-1\neq0$; and its inertia is $(1,3)$, so the form is indefinite. The diagonal of the form is the quadratic form

$$
\langle\tilde Q,\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^2=Q_0^2-Q_1^2-Q_2^2-Q_3^2,
$$

and the form is its polarisation. The centre spans the positive direction and the vector subspace the negative one, which is the whole of the inertia.

## The Realified Gram Matrix

Write a biquaternion on the eight real basis elements as $\tilde Q=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu\,ie_\mu$, with $q_\mu,q'_\mu\in\mathbb R$. Because the form is $\mathbb C$-bilinear, its values on the real basis are

$$
\langle e_\mu,e_\nu\rangle=\varepsilon_\mu\delta_{\mu\nu},\qquad
\langle e_\mu,ie_\nu\rangle=i\,\varepsilon_\mu\delta_{\mu\nu},\qquad
\langle ie_\mu,ie_\nu\rangle=-\varepsilon_\mu\delta_{\mu\nu}.
$$

The middle entries are purely imaginary, so they do not contribute to the realified symmetric form, whose Gram matrix is therefore block-diagonal,

$$
\operatorname{diag}(D,-D)=\operatorname{diag}(1,-1,-1,-1,\,-1,1,1,1),
$$

of signature $(4,4)$. The sign flip between the two blocks is the signature of the complex structure: a complex bilinear form reads $+1$ on a real direction and $-1$ on the same direction multiplied by $i$.

## The Restriction Matrices

On each of the six distinguished real subspaces the form restricts to a real symmetric bilinear form, and its Gram matrix in the natural real basis of the subspace is again diagonal:

| Subspace | Real basis | Gram matrix | Signature |
|---|---|---|---|
| Centre $\mathbb C_{\mathbb B}$ | $e_0,\,ie_0$ | $\operatorname{diag}(1,-1)$ | $(1,1)$ |
| Vector $\mathrm{Vect}(\mathbb B)$ | $e_k,\,ie_k$ | $\operatorname{diag}(-1,-1,-1,1,1,1)$ | $(3,3)$ |
| Quaternion $\mathbb H_{\mathbb B}$ | $e_0,e_1,e_2,e_3$ | $\operatorname{diag}(1,-1,-1,-1)$ | $(1,3)$ |
| Anti-quaternion $i\mathbb H_{\mathbb B}$ | $ie_0,ie_1,ie_2,ie_3$ | $\operatorname{diag}(-1,1,1,1)$ | $(3,1)$ |
| Hermitian $\mathbb M_+$ | $e_0,ie_1,ie_2,ie_3$ | $\operatorname{diag}(1,1,1,1)$ | $(4,0)$ |
| Anti-Hermitian $\mathbb M_-$ | $ie_0,e_1,e_2,e_3$ | $\operatorname{diag}(-1,-1,-1,-1)$ | $(0,4)$ |

The two complex subspaces carry the indefinite pair $(1,1)$ and $(3,3)$; the four real forms carry $(1,3)$, $(3,1)$, $(4,0)$ and $(0,4)$. The Hermitian subspace is the positive definite one and the anti-Hermitian the negative definite one, so no subspace of dimension greater than four is definite. The table is recomputed in *The Six Subspaces under the Complex Bilinear Form*, where the same numbers are read subspace by subspace.

## Comparison with the Quaternion Bilinear Form

The quaternion bilinear form $\langle\tilde P,\tilde Q\rangle_{\natural}=\sum_\mu P_\mu Q_\mu$ has Gram matrix $\mathrm I_4$ in the same coefficient basis, so the two bilinear forms differ by the sign vector $\varepsilon$ and by nothing else,

$$
\langle\tilde P,\tilde Q\rangle=\sum_\mu\varepsilon_\mu P_\mu Q_\mu,\qquad
\langle\tilde P,\tilde Q\rangle_{\natural}=\sum_\mu P_\mu Q_\mu .
$$

Both realify to signature $(4,4)$, but on the six subspaces they disagree wherever the sign matters: the quaternion subspace carries $(1,3)$ for the plain form against $(4,0)$ for the $\natural$-form, and the Hermitian subspace carries $(4,0)$ against $(1,3)$. The two matrices $D$ and $\mathrm I_4$ are the whole of the distinction, and the tabulation of the four forms together is *The Gram Matrices of the Four Forms*.

## Summary

The complex bilinear form has Gram matrix $D=\operatorname{diag}(1,-1,-1,-1)$, of determinant $-1$ and inertia $(1,3)$, and realified Gram matrix $\operatorname{diag}(D,-D)$, of signature $(4,4)$. Its restrictions carry signatures $(1,1)$, $(3,3)$, $(1,3)$, $(3,1)$, $(4,0)$ and $(0,4)$ on the centre, the vector, the quaternion, the anti-quaternion, the Hermitian and the anti-Hermitian subspaces. It differs from the quaternion bilinear form by the sign vector $\varepsilon$ alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $D=\operatorname{diag}(1,-1,-1,-1)$ | Gram matrix of the complex bilinear form in the coefficient basis |
| $\operatorname{diag}(D,-D)$ | its realified Gram matrix, of signature $(4,4)$ |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector, the whole difference from the $\natural$-bilinear form |

## Further Reading

- *The Complex Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-complex-bilinear-form-on-the-biquaternion-algebra.md`), for the form itself
- *The Gram Matrices of the Four Forms* (`articles_maths/the-gram-matrices-of-the-four-forms.md`), for the four matrices together
- *The Quaternion Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), for the companion matrix $\mathrm I_4$
