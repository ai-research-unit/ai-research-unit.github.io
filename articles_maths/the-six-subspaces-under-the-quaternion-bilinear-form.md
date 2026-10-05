# __The Six Subspaces under the Quaternion Bilinear Form__

## Introduction

The quaternion bilinear form $\langle\tilde P,\tilde Q\rangle_{\natural}=\sum_\mu P_\mu Q_\mu$, whose diagonal is the biquaternion norm, is read here on the six distinguished real subspaces. This article records the six signatures, the two definite rows, the maximal definite subspaces, and the comparison with the complex bilinear form.

## The Six Signatures

With $\tilde Q=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu\,ie_\mu$, the norm on each subspace is diagonal and its signature is read at once:

| Subspace | Real dimension | Restricted norm | Signature |
|---|---|---|---|
| Centre $\mathbb C_{\mathbb B}$ | $2$ | $q_0^2-(q'_0)^2$ | $(1,1)$ |
| Vector $\mathrm{Vect}(\mathbb B)$ | $6$ | $\sum_k\bigl(q_k^2-(q'_k)^2\bigr)$ | $(3,3)$ |
| Quaternion $\mathbb H_{\mathbb B}$ | $4$ | $\sum_\mu q_\mu^2$ | $(4,0)$ |
| Anti-quaternion $i\mathbb H_{\mathbb B}$ | $4$ | $-\sum_\mu(q'_\mu)^2$ | $(0,4)$ |
| Hermitian $\mathbb M_+$ | $4$ | $q_0^2-\sum_k(q'_k)^2$ | $(1,3)$ |
| Anti-Hermitian $\mathbb M_-$ | $4$ | $\sum_kq_k^2-(q'_0)^2$ | $(3,1)$ |

## The Definite Rows and the Maximal Definite Subspaces

The **quaternion subspace** carries signature $(4,0)$ and the **anti-quaternion subspace** signature $(0,4)$: these are the definite rows, exchanged by multiplication by $i$, under which the norm changes sign,

$$
\langle i\tilde P,i\tilde Q\rangle_{\natural}=-\langle\tilde P,\tilde Q\rangle_{\natural}.
$$

The quaternion subspace is thus a maximal positive definite subspace of the norm, of dimension $4$, and the anti-quaternion subspace a maximal negative definite one; they are orthogonal complements, $\mathbb H_{\mathbb B}\oplus i\mathbb H_{\mathbb B}=\mathbb B$, and the norm is the positive form on the first and its negative on the second. This splitting is the polarisation the norm uses to decide invertibility, and it is the reason the two subspaces carry no zero divisor.

The remaining four rows are indefinite. The **centre** and the **vector subspace** carry $(1,1)$ and $(3,3)$; the two **real forms** carry the sign-mirror pair $(1,3)$ and $(3,1)$.

## Orthogonality and the Isotropic Elements

The six subspaces are pairwise orthogonal for this form exactly when their bases are orthogonal in the coefficient basis, and the diagonal table shows the splitting: the centre and the vector subspace are orthogonal complements, and so are the quaternion and anti-quaternion subspaces. On the **vector subspace** the norm is the complex quadratic $\sum_kQ_k^2$, whose isotropic set is the pure zero-divisor cone, of real dimension $4$; on the two **real forms** it is the real light cone of the Minkowski signature, of real dimension $3$, carrying the non-pure zero divisors; and on the two definite rows it vanishes only at the origin.

## Comparison with the Complex Bilinear Form

The complex bilinear form records the same six subspaces with the signatures $(1,1)$, $(3,3)$, $(1,3)$, $(3,1)$, $(4,0)$, $(0,4)$. The two tables agree on the centre and the vector subspace and are swapped on the four real forms: the definite sign of the plain form falls on the Hermitian subspace, of the $\natural$-form on the quaternion subspace. The comparison is carried in *The Six Subspaces under the Complex Bilinear Form*, and the four tables together are *The Real Reading of the Six Subspaces*.

## Summary

On the six distinguished real subspaces the quaternion bilinear form carries the signatures $(1,1)$, $(3,3)$, $(4,0)$, $(0,4)$, $(1,3)$ and $(3,1)$. The quaternion and anti-quaternion subspaces are the two definite rows, of dimension $4$ and maximal, and they are orthogonal complements; the centre and the vector subspace carry $(1,1)$ and $(3,3)$; the two real forms carry $(1,3)$ and $(3,1)$. The isotropic elements are the zero divisors on the vector subspace and the two real forms, and only the origin on the two definite subspaces.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(1,1),(3,3),(4,0),(0,4),(1,3),(3,1)$ | the six signatures of the norm |
| $\mathbb H_{\mathbb B}\oplus i\mathbb H_{\mathbb B}$ | the maximal definite splitting of the algebra |
| $\langle i\tilde P,i\tilde Q\rangle_{\natural}=-\langle\tilde P,\tilde Q\rangle_{\natural}$ | the sign change pairing the definite rows |

## Further Reading

- *The Quaternion Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), for the form and its restrictions
- *The Six Subspaces under the Complex Bilinear Form* (`articles_maths/the-six-subspaces-under-the-complex-bilinear-form.md`), for the companion table
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm and its real forms
