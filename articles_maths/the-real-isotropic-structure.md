# __The Real Isotropic Structure__

## Introduction

Read on the eight-dimensional real vector space, the four forms of the algebra give four real symmetric forms, and each indefinite one has a null cone. This article records the four cones, their dimensions, the totally isotropic subspaces, and the distinction between the realified cone and the complex null cone of the same form.

## The Four Realified Forms and Their Cones

With $\tilde Q=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu\,ie_\mu$, the four realified forms and their null sets are:

| Form | Signature | Realified form | Null set |
|---|---|---|---|
| Complex bilinear | $(4,4)$ | $q_0^2-q_1^2-q_2^2-q_3^2-q_0'^2+q_1'^2+q_2'^2+q_3'^2$ | hypersurface, real dim $7$ |
| Quaternion bilinear | $(4,4)$ | $q_0^2-q_0'^2+q_1^2-q_1'^2+q_2^2-q_2'^2+q_3^2-q_3'^2$ | hypersurface, real dim $7$ |
| Hermitian | $(8,0)$ | $\sum_\mu\bigl(q_\mu^2+q_\mu'^2\bigr)$ | $\{0\}$ |
| Krein | $(2,6)$ | $q_0^2+q_0'^2-\sum_k\bigl(q_k^2+q_k'^2\bigr)$ | hypersurface, real dim $7$ |

The **Hermitian** form is positive definite and has no non-zero isotropic element. The other three are indefinite, and each null set is a real hypersurface of dimension $7$ through the origin, smooth off the apex. The **Krein** cone is the real light cone of signature $(2,6)$; the two **bilinear** cones are the split cones of signature $(4,4)$, and they are different cones because their signs fall on different coordinates.

## The Totally Isotropic Subspaces

A real form of signature $(p,q)$ has maximal totally isotropic subspaces of dimension $\min(p,q)$. The values for the four forms are:

- the **complex bilinear** and the **quaternion bilinear** forms, of signature $(4,4)$: totally isotropic subspaces of real dimension $4$;
- the **Krein** form, of signature $(2,6)$: totally isotropic subspaces of real dimension $2$;
- the **Hermitian** form: no isotropic element but $0$.

The realifications of the two rulings of its complex cone give maximal totally isotropic subspaces of the complex bilinear form, of real dimension $4$; the maximal totally isotropic subspaces of the Krein form, of real dimension $2$, are the real planes recorded in *The Witt Index and the Maximal Isotropic Subspaces of the Krein Form*.

## The Realified Cone and the Complex Cone

The realified cone is not the complex null cone of the same form, and the two must be distinguished. The **complex** null cone of the complex bilinear form, $\{\tilde Q:\sum_\mu\varepsilon_\mu Q_\mu^2=0\}$, is a complex cone of real dimension $6$ inside the eight-dimensional space; the realified cone computed here is the hypersurface $\{\mathrm{Re}\sum_\mu\varepsilon_\mu Q_\mu^2=0\}$ of real dimension $7$, which is one real equation and not two. The complex cone is the common zero set of the real and the imaginary parts, and so sits inside the realified cone as a real codimension-one subcone,

$$
\{\mathrm{Re}=0\}\cap\{\mathrm{Im}=0\}\ \subsetneq\ \{\mathrm{Re}=0\}.
$$

The same distinction holds for the quaternion bilinear form: its complex cone $\sum_\mu Q_\mu^2=0$ is of real dimension $6$, its realified cone of real dimension $7$. The complex cones are the isotropic structures of the complex forms, recorded in *The Isotropic Structure of the Complex Bilinear Form* and *The Isotropic Structure of the Quaternion Bilinear Form*; the realified cones are the real isotropic structures of the present article, and the four together are the isotropic counterpart of *The Real Reading of the Six Subspaces*.

## Summary

The Hermitian form is definite and has no non-zero isotropic element; the complex bilinear, the quaternion bilinear and the Krein forms have null cones that are real hypersurfaces of dimension $7$ in $\mathbb R^8$, of signatures $(4,4)$, $(4,4)$ and $(2,6)$. Their maximal totally isotropic subspaces have real dimensions $4$, $4$ and $2$. The realified cones are strictly larger than the complex null cones of the same forms, which are of real dimension $6$ and sit inside them as real codimension-one subcones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| real dim $7$ | the dimension of each indefinite realified null cone |
| $4$, $4$, $2$, $0$ | the maximal totally isotropic dimensions of the four forms |
| $\{\mathrm{Re}=0\}\supsetneq\{\mathrm{Re}=0\}\cap\{\mathrm{Im}=0\}$ | the realified cone and the complex cone inside it |

## Further Reading

- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the four signatures
- *The Isotropic Structure of the Complex Bilinear Form* (`articles_maths/the-isotropic-structure-of-the-complex-bilinear-form.md`) and *The Isotropic Structure of the Quaternion Bilinear Form*, for the complex cones
- *The Real Reading of the Six Subspaces* (`articles_maths/the-real-reading-of-the-six-subspaces.md`), for the companion tables
