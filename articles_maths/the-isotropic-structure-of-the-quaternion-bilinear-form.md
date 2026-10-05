# __The Isotropic Structure of the Quaternion Bilinear Form__

## Introduction

The quaternion bilinear form

$$
\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P\tilde Q^{\natural})=\sum_\mu P_\mu Q_\mu
$$

has for its null set the zero-divisor cone of the algebra. This article records the cone, its dimension, its ruling, its real dimension on each of the six distinguished subspaces, and the comparison with the null cone of the complex bilinear form.

## The Null Cone

**Definition.** The **null cone** of the quaternion bilinear form is

$$
\mathcal N_{\natural}=\{\tilde Q:\langle\tilde Q,\tilde Q\rangle_{\natural}=0\}=\Bigl\{\tilde Q:\sum_\mu Q_\mu^2=0\Bigr\}.
$$

On $\mathbb C^4\cong\mathbb B$ it is the complex quadric $\sum_\mu Q_\mu^2=0$, a complex hypersurface through the origin: of complex dimension $3$ and **real dimension $6$**. It is a cone, invariant under $\tilde Q\mapsto\lambda\tilde Q$ for $\lambda\in\mathbb C$; it is smooth off the apex, since the gradient $2(Q_0,Q_1,Q_2,Q_3)$ vanishes only at the origin. Its link is the complex quadric surface $Q^2$ of *Biquaternion Topology*.

The cone is exactly the zero-divisor set. An element is a zero divisor precisely when it is null, so $\mathcal N_{\natural}\setminus\{0\}$ is the union of the two families of zero divisors classified in *Biquaternion Zero Divisors*; the algebra fails to be a division algebra along it, and nowhere else. The projective picture of the cone, its two rulings, the Klein quadric and the Plücker embedding are *Biquaternion Topology*.

## The Dimension on the Six Subspaces

Intersected with the six distinguished real subspaces, the cone has the following real dimensions, read from the signatures of the restriction:

| Subspace | Restricted norm | Null set | Real dimension |
|---|---|---|---|
| Centre $\mathbb C_{\mathbb B}$ | $Q_0^2$ | $Q_0=0$ | $0$ |
| Vector $\mathrm{Vect}(\mathbb B)$ | $Q_1^2+Q_2^2+Q_3^2$ | the complex cone $\sum_kQ_k^2=0$ | $4$ |
| Quaternion $\mathbb H_{\mathbb B}$ | $\sum_\mu q_\mu^2$, signature $(4,0)$ | $\{0\}$ | $0$ |
| Anti-quaternion $i\mathbb H_{\mathbb B}$ | $-\sum_\mu(q'_\mu)^2$, signature $(0,4)$ | $\{0\}$ | $0$ |
| Hermitian $\mathbb M_+$ | $q_0^2-\sum_k(q'_k)^2$, signature $(1,3)$ | the real light cone | $3$ |
| Anti-Hermitian $\mathbb M_-$ | $\sum_kq_k^2-(q'_0)^2$, signature $(3,1)$ | the real light cone | $3$ |

Two features stand out. The restriction to the **quaternion subspace** is positive definite and to the **anti-quaternion subspace** negative definite, so neither contains a non-zero null element: these are the two subspaces on which the norm has a definite sign, and they are the reason the classical quaternion algebra is a division algebra. On the **vector subspace** the restricted form is the complex quadratic $\sum_kQ_k^2$, whose null set carries the *pure* zero divisors; on the two **real forms** it is the real light cone, whose null set carries the non-pure zero divisors. The centre carries none, being a field.

## Comparison with the Complex Bilinear Form

The complex bilinear form has null set

$$
\Bigl\{\tilde Q:\sum_\mu\varepsilon_\mu Q_\mu^2=0\Bigr\}=\{Q_0^2=Q_1^2+Q_2^2+Q_3^2\},
$$

also a smooth complex cone of real dimension $6$. As complex quadrics the two are equivalent, each being non-degenerate; their defining quadrics are in general position, so the two complex cones meet only at the origin. They differ as real forms, and their restrictions to the six subspaces differ accordingly. The $\natural$-cone meets the Krein null set in the doubly null lines $\mathbb C(e_0\pm ie_1)$ recorded in *The Isotropic Structure of the Krein Form*, and the comparison of the four null cones is the tabulated *The Real Isotropic Structure*.

## Summary

The null cone of the quaternion bilinear form is $\sum_\mu Q_\mu^2=0$, the zero-divisor cone of the algebra, of real dimension $6$ and smooth off the apex. On the six subspaces it has real dimension $0$, $4$, $0$, $0$, $3$, $3$; it is empty off the origin on the two definite subspaces, it is exactly the pure zero-divisor cone on the vector subspace, and it consists of non-pure zero divisors on the two real forms. As a complex quadric it is equivalent to the null cone of the complex bilinear form, which is also a smooth complex cone of real dimension $6$; the two differ as real forms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal N_{\natural}=\{\tilde Q:\sum_\mu Q_\mu^2=0\}$ | the null cone of the quaternion bilinear form |
| real dimension $6$ | its dimension in $\mathbb B$ |
| $\mathcal N_{\natural}\setminus\{0\}$ | the zero-divisor set of the algebra |

## Further Reading

- *The Quaternion Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), for the form
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the classification of the isotropic elements
- *The Isotropic Structure of the Complex Bilinear Form* (`articles_maths/the-isotropic-structure-of-the-complex-bilinear-form.md`), for the companion cone
