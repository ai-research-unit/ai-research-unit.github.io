# __The Real Reading of the Six Subspaces__

## Introduction

The four forms of the algebra are complex; read on the eight-dimensional real vector space they give four real symmetric forms, and their values on the six distinguished real subspaces are gathered here in one table. This article is the comparative counterpart of the four separate subspace articles; it records the four tables side by side, the definite and indefinite rows, and the totally isotropic subspaces of each form.

## The Four Tables Side by Side

The four realified forms are the complex bilinear form, the quaternion bilinear form $N$, the Hermitian (complex sesquilinear) form and the Krein form, of signatures $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$. On the six subspaces their signatures are:

| Subspace | Complex bilinear | Quaternion bilinear | Hermitian | Krein |
|---|---|---|---|---|
| Centre $\mathbb C_{\mathbb B}$ | $(1,1)$ | $(1,1)$ | $(2,0)$ | $(2,0)$ |
| Vector $\mathrm{Vect}(\mathbb B)$ | $(3,3)$ | $(3,3)$ | $(6,0)$ | $(0,6)$ |
| Quaternion $\mathbb H_{\mathbb B}$ | $(1,3)$ | $(4,0)$ | $(4,0)$ | $(1,3)$ |
| Anti-quaternion $i\mathbb H_{\mathbb B}$ | $(3,1)$ | $(0,4)$ | $(4,0)$ | $(1,3)$ |
| Hermitian $\mathbb M_+$ | $(4,0)$ | $(1,3)$ | $(4,0)$ | $(1,3)$ |
| Anti-Hermitian $\mathbb M_-$ | $(0,4)$ | $(3,1)$ | $(4,0)$ | $(1,3)$ |

Every entry is read from the diagonal of the restricted form in the natural real basis of the subspace, and the four tables are the ones computed in the four subspace articles *The Six Subspaces under the Complex Bilinear Form*, *... under the Quaternion Bilinear Form* and *... under the Krein Form*, together with the definite table of *The Hermitian Form on the Biquaternion Algebra*.

## The Definite and the Indefinite Rows

Each form has its own definite row. The **Hermitian form** is positive definite on every subspace: all six rows are $(2,0)$ or $(n,0)$, and the form is the Euclidean structure of the algebra. The **complex bilinear form** is definite on the Hermitian subspace $(4,0)$ and the anti-Hermitian subspace $(0,4)$. The **quaternion bilinear form** is definite on the quaternion subspace $(4,0)$ and the anti-quaternion subspace $(0,4)$. The **Krein form** is definite on the two complex subspaces, positive on the centre $(2,0)$ and negative on the vector subspace $(0,6)$.

The pattern is exact: the passage from the Hermitian form to the Krein form moves the definite rows from the four real forms to the two complex subspaces; the passage from the Hermitian form to the two bilinear forms moves the definite rows to the pairs $(\mathbb M_+,\mathbb M_-)$ and $(\mathbb H_{\mathbb B},i\mathbb H_{\mathbb B})$ respectively.

## The Totally Isotropic Subspaces

A form of signature $(p,q)$ has maximal totally isotropic subspaces of dimension $\min(p,q)$. Read on the whole algebra:

- the **Hermitian form** is definite, so its only isotropic element is $0$;
- the **complex bilinear** and the **quaternion bilinear** forms have signature $(4,4)$ and admit totally isotropic subspaces of real dimension $4$;
- the **Krein form** has signature $(2,6)$ and admits totally isotropic subspaces of real dimension $2$.

The isotropic cones themselves are hypersurfaces of the eight-dimensional space, of real dimension $7$, for the three indefinite forms. The complex null cone $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ of the complex bilinear form and the $\natural$-cone $\sum_\mu Q_\mu^2=0$ of the quaternion bilinear form are two different complex cones of real dimension $6$ inside the eight-dimensional space; their realified cones are the real hypersurfaces tabulated here, and the comparison of the four is *The Real Isotropic Structure*.

## Summary

The four realified forms read the six subspaces with the four tables above. The Hermitian form is positive definite everywhere; the complex bilinear form is definite on the Hermitian and anti-Hermitian subspaces; the quaternion bilinear form is definite on the quaternion and anti-quaternion subspaces; and the Krein form is definite on the centre and the vector subspace. The maximal totally isotropic dimensions are $0$, $4$, $4$ and $2$ respectively.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(4,4),(4,4),(8,0),(2,6)$ | the four realified signatures |
| $0,\,4,\,4,\,2$ | the maximal totally isotropic dimensions of the four forms |
| definite rows | centre and vector (Krein), Hermitian and anti-Hermitian (complex bilinear), quaternion and anti-quaternion ($\natural$-bilinear) |

## Further Reading

- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the four signatures
- *The Six Subspaces under the Complex Bilinear Form* (`articles_maths/the-six-subspaces-under-the-complex-bilinear-form.md`), *... under the Quaternion Bilinear Form*, *... under the Krein Form*, for the three tables
- *The Real Isotropic Structure* (`articles_maths/the-real-isotropic-structure.md`), for the four cones
