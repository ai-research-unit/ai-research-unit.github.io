# __The Six Subspaces under the Complex Bilinear Form__

## Introduction

The complex bilinear form $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ is read on each of the six distinguished real subspaces of *Introduction to the Six Subspaces* — the centre, the vector subspace, the quaternion subspace, the anti-quaternion subspace, the Hermitian subspace and the anti-Hermitian subspace. On each, the realified form is real symmetric, and this article records the six signatures, the definite and indefinite rows, the orthogonalities, and the comparison with the $\natural$-bilinear reading of the same six subspaces.

## The Six Signatures

With $\tilde Q=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu\,ie_\mu$, the form on the six subspaces is diagonal and the signatures are read at once:

| Subspace | Real dimension | Restricted form | Signature |
|---|---|---|---|
| Centre $\mathbb C_{\mathbb B}$ | $2$ | $q_0^2-(q'_0)^2$ | $(1,1)$ |
| Vector $\mathrm{Vect}(\mathbb B)$ | $6$ | $\sum_k\bigl((q'_k)^2-q_k^2\bigr)$ | $(3,3)$ |
| Quaternion $\mathbb H_{\mathbb B}$ | $4$ | $q_0^2-q_1^2-q_2^2-q_3^2$ | $(1,3)$ |
| Anti-quaternion $i\mathbb H_{\mathbb B}$ | $4$ | $-(q'_0)^2+(q'_1)^2+(q'_2)^2+(q'_3)^2$ | $(3,1)$ |
| Hermitian $\mathbb M_+$ | $4$ | $q_0^2+(q'_1)^2+(q'_2)^2+(q'_3)^2$ | $(4,0)$ |
| Anti-Hermitian $\mathbb M_-$ | $4$ | $-\bigl((q'_0)^2+q_1^2+q_2^2+q_3^2\bigr)$ | $(0,4)$ |

(The coordinates are the real coordinates of the subspace; the anti-quaternion row is written in the primed coordinates $q'_\mu$.)

## The Definite and the Indefinite Rows

Two rows are definite. On the **Hermitian subspace** the form is positive definite, of signature $(4,0)$, the maximal positive definite dimension of the algebra; on the **anti-Hermitian subspace** it is negative definite, of signature $(0,4)$. The two are exchanged by multiplication by $i$, under which the form changes sign,

$$
\langle i\tilde P,i\tilde Q\rangle=-\langle\tilde P,\tilde Q\rangle,
$$

which is why $(4,0)$ and $(0,4)$ come as a pair.

The four remaining rows are indefinite. The **quaternion** and **anti-quaternion** subspaces carry the sign-mirror pair $(1,3)$ and $(3,1)$, again exchanged by multiplication by $i$. The **centre** and the **vector subspace** carry $(1,1)$ and $(3,3)$: on the centre the real direction $e_0$ is positive and the imaginary direction $ie_0$ negative, and on the vector subspace each of the three quaternion directions is negative while its imaginary companion is positive.

No subspace is totally isotropic. The form is non-degenerate everywhere, and each row has both signs except the two definite rows, so the isotropic set of the restriction is a cone of codimension one in the subspace whenever the row is indefinite, and is $\{0\}$ on the two definite rows.

## Orthogonality and the Pairings

The form pairs the six subspaces in a pattern read from its diagonal. Since the restricted form is diagonal in the natural bases, the **centre** and the **vector subspace** are orthogonal to each other and together fill the algebra: $\mathbb C_{\mathbb B}\perp\mathrm{Vect}(\mathbb B)$ and $\mathbb C_{\mathbb B}\oplus\mathrm{Vect}(\mathbb B)=\mathbb B$ is an orthogonal decomposition of the whole algebra. On the four real forms the restriction of the form is the pairing already visible in the matrix model, and the quaternion and Hermitian rows differ in sign: $\langle\tilde Q,\tilde R\rangle=q_0r_0-\mathbf q\cdot\mathbf r$ on the quaternion subspace, against $q_0r_0+\mathbf q'\cdot\mathbf r'$ on the Hermitian one, where $\mathbf q'$ collects the imaginary spatial coordinates.

## Comparison with the Quaternion Bilinear Form

The $\natural$-bilinear form $\sum_\mu P_\mu Q_\mu$ reads the same six subspaces with the table $(1,1)$, $(3,3)$, $(4,0)$, $(0,4)$, $(1,3)$, $(3,1)$. The two tables are the transpose of one another on the four real forms — the complex bilinear form puts the definite sign on the Hermitian subspace, the $\natural$-form puts it on the quaternion subspace — and they agree on the centre and the vector subspace. The comparison is tabulated in *The Six Subspaces under the Quaternion Bilinear Form*.

## Summary

On the six distinguished real subspaces the complex bilinear form carries the signatures $(1,1)$, $(3,3)$, $(1,3)$, $(3,1)$, $(4,0)$ and $(0,4)$. The Hermitian subspace is the positive definite one and the anti-Hermitian the negative definite one, the quaternion and anti-quaternion rows are the sign-mirror pair $(1,3)$, $(3,1)$, and the centre and vector rows are $(1,1)$, $(3,3)$. No subspace is totally isotropic, and the centre and the vector subspace are orthogonal complements in the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(1,1),(3,3),(1,3),(3,1),(4,0),(0,4)$ | the signatures on the six subspaces |
| $\mathbb C_{\mathbb B}\perp\mathrm{Vect}(\mathbb B)$ | the orthogonal splitting of the algebra |
| $\langle i\tilde P,i\tilde Q\rangle=-\langle\tilde P,\tilde Q\rangle$ | the sign change that pairs $(1,3)$ with $(3,1)$ and $(4,0)$ with $(0,4)$ |

## Further Reading

- *The Gram Matrix of the Complex Bilinear Form* (`articles_maths/the-gram-matrix-of-the-complex-bilinear-form.md`), for the matrices behind the table
- *The Complex Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-complex-bilinear-form-on-the-biquaternion-algebra.md`), for the form
- *The Six Subspaces under the Quaternion Bilinear Form* (`articles_maths/the-six-subspaces-under-the-quaternion-bilinear-form.md`), for the companion table
