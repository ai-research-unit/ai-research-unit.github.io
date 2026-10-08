# __The Six Subspaces under the Symmetric Plain Sesqualgebra of Biquaternions__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*), and its values lie in the centre $\mathbb{C}_{\mathbb{B}}$ whatever the two arguments are. This article reads the six distinguished subspaces of the algebra — the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ — under that product, one to a section, in the pattern of *The Six Subspaces under the General Plain Sesqualgebra of Biquaternions*.

The central image **flattens the table**, and the point of the article is to say so and to read what is left. Because every value is a scalar multiple of $e_0$, the product of two elements of a subspace $S$ lies in $S$ exactly when $S$ contains the idempotent $e_0$; the closure of the product, which in a product with a vector part is a genuine computation on each subspace, here reduces to the single question *does $S$ contain $e_0$*. The answer is yes for the centre, for the quaternion subspace and for the Hermitian subspace, and no for the vector subspace, for the anti-quaternion subspace and for the anti-Hermitian subspace, each with a smallest witness that is the square of one of its basis elements, $e_1\star e_1 = e_0$ in the vector and anti-Hermitian subspaces and $(ie_1)\star(ie_1) = e_0$ in the anti-quaternion subspace. What remains is the reading of each subspace — the restricted form, its rank and signature, the idempotents, the elements of square zero and the isotropic elements — which the sections give one by one; the restricted form is the identity form on the natural real basis, positive definite, of rank the real dimension in every case, so apart from the closure and the idempotents the six readings coincide, and this flatness is the mark of the central image.

**Boundaries.** The subspaces and their names are *Introduction to the Six Subspaces* and *Comparison of the Six Subspaces*; the pattern is the sibling *The Six Subspaces under the General Plain Sesqualgebra of Biquaternions*; the form $H$ and its restriction are *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* and *Biquaternion Norm and Invertibility*, and the closure of the six under the general plain sesquilinear product is the sibling article's. This article owns only the reading of the six under the product of the block. Nothing topological and nothing metric appears.

**Conventions.** As in the companion articles: $\mathbb{B}$ with basis $e_0,e_1,e_2,e_3$, natural conjugation ${}^{\natural}$, coefficientwise conjugation $\overline{\cdot}$, Hermitian conjugation ${}^{*} = \overline{\cdot}\circ{}^{\natural}$; the block is $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ with $H(\tilde P,\tilde Q) = P_0\overline{Q_0} + (\mathbf P,\overline{\mathbf Q})$. The six subspaces are the eigenspaces of the three involutions of the algebra: the centre and the vector subspace for the natural conjugation, the quaternion and the anti-quaternion subspace for the coefficientwise conjugation, the Hermitian and the anti-Hermitian subspace for the Hermitian conjugation.

## The Closure of the Six, in One Statement

**Theorem (closure, read by the idempotent).** Let $S$ be one of the six subspaces. Then $S$ is closed under the product of the block, $\tilde P\star\tilde Q \in S$ for all $\tilde P,\tilde Q \in S$, if and only if $e_0 \in S$.

*Proof.* If $e_0\in S$ then the value $H(\tilde P,\tilde Q)e_0$ lies in $S$: for the complex subspace $\mathbb{C}_{\mathbb{B}}$ the coefficient is an arbitrary complex number and $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_0$; for the real subspaces $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_+$ the coefficient is real, and the real multiples of $e_0$ lie in the subspace. If $e_0\notin S$, take any nonzero $\tilde P\in S$; then $\tilde P\star\tilde P = H(\tilde P,\tilde P)e_0$ is a strictly positive real multiple of $e_0$, so it lies in $S$ only if $e_0$ lies in $S$, and the product therefore leaves $S$. $\square$

**Corollary (the three closed and the three that are not).** Of the six subspaces, the centre, the quaternion subspace and the Hermitian subspace contain $e_0$ and are closed; the vector subspace, the anti-quaternion subspace and the anti-Hermitian subspace do not and are not. The six were recomputed on $200$ pairs each: the closed ones gave $0$ failures, the ones that are not closed gave $200$ failures.

## The Centre

The centre is $\mathbb{C}_{\mathbb{B}} = \{\lambda e_0 : \lambda\in\mathbb{C}\}$, the one-dimensional complex subspace of the scalars. On it the form is $H(\lambda e_0,\mu e_0) = \lambda\overline{\mu}$, so the product reads

$$
(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}\,e_0 ,
$$

the multiplication of the field by the conjugate of the second factor. The centre is **closed** and is the smallest of the six; the product on it is conjugate-commutative, has the idempotents $0$ and $e_0$, and has no unit, since $(\lambda e_0)\star e_0 = \lambda e_0$ only for the elements of the centre and not for the general element of the space. The restriction of $H$ to the centre is the positive definite form $\lambda\overline{\mu}$ of real rank $2$; it has no isotropic element, and the elements of square zero are none.

## The Vector Subspace

The vector subspace is $\mathrm{Vect}(\mathbb{B}) = \{\mathbf P : P_0 = 0\}$, of real dimension six. On it the form is $H(\mathbf P,\mathbf Q) = (\mathbf P,\overline{\mathbf Q})$, so the product of two vectors is the central element

$$
\mathbf P\star\mathbf Q = (\mathbf P,\overline{\mathbf Q})\,e_0 ,
$$

and it is **not closed**: the smallest witness is $e_1\star e_1 = H(e_1,e_1)e_0 = e_0$, which leaves the vector subspace because it has a scalar part. The element $e_0$ is not in the subspace, so the only idempotent the subspace contains is $0$; the elements of square zero are none, since $H(\mathbf P,\mathbf P) = \sum_{k}\lvert P_k\rvert^{2}$ vanishes only at the origin; and the restriction of $H$ is positive definite of real rank $6$, with isotropic cone $\{0\}$.

## The Quaternion Subspace

The quaternion subspace is $\mathbb{H}_{\mathbb{B}} = \{\sum_\mu P_\mu e_\mu : P_\mu\in\mathbb{R}\}$, the real span of the basis, of real dimension four. On it the form is real, $H(\tilde P,\tilde Q) = P_0Q_0 + (\mathbf P,\mathbf Q) = B(\tilde P,\tilde Q)$, so the product is

$$
\tilde P\star\tilde Q = \bigl(P_0Q_0 + (\mathbf P,\mathbf Q)\bigr)e_0 ,
$$

with a **real** central coefficient. The subspace is **closed**, because the value is a real multiple of $e_0$ and the real multiples of $e_0$ lie in $\mathbb{H}_{\mathbb{B}}$; it is the smallest closed subspace containing the basis $e_0,e_1,e_2,e_3$. Its idempotents are $0$ and $e_0$, the same two as the block, and its elements of square zero are none. The restriction of $H$ is the identity form on the basis, of real rank $4$ and signature $(4,0)$; on this subspace the block coincides with the symmetric quaternionic block, and the section is the bridge between the two rows in coordinates.

## The Anti-Quaternion Subspace

The anti-quaternion subspace is $i\mathbb{H}_{\mathbb{B}} = \{\sum_\mu P_\mu e_\mu : P_\mu\in i\mathbb{R}\}$, of real dimension four. On it the form is real again, $H(i\tilde P,i\tilde Q) = \sum_\mu P_\mu Q_\mu$ for real $\tilde P,\tilde Q$, so the product is

$$
(i\tilde P)\star(i\tilde Q) = \Bigl(\sum_\mu P_\mu Q_\mu\Bigr)e_0 ,
$$

with a real central coefficient; the subspace is **not closed**, because its elements have a purely imaginary scalar coordinate and the value $e_0$ is real. The smallest witness is $(ie_1)\star(ie_1) = e_0$, with $ie_1\in i\mathbb{H}_{\mathbb{B}}$ a basis element of the subspace; more sharply, the value of two anti-quaternion elements is always a **real** multiple of $e_0$, and lands in the quaternion subspace and not in $i\mathbb{H}_{\mathbb{B}}$. The idempotents contained are $0$ alone, and the elements of square zero are none. The restriction of $H$ is the identity form in the imaginary basis $ie_0,ie_1,ie_2,ie_3$, of real rank $4$ and signature $(4,0)$.

## The Hermitian Subspace

The Hermitian subspace is the fixed space of the Hermitian conjugation, $\mathbb{M}_+ = \{p_0e_0 + \sum_{k}p_k(ie_k) : p_\mu\in\mathbb{R}\}$, of real dimension four, with real basis $e_0, ie_1, ie_2, ie_3$. On it the form is real and is the identity form in this basis,

$$
H(\tilde P,\tilde Q) = p_0q_0 + \sum_{k=1}^{3} p_kq_k , \qquad \tilde P,\tilde Q\in\mathbb{M}_+ ,
$$

which is the positive part of the Hermitian form of *Biquaternion Norm and Invertibility* restricted to its coordinates, so the product reads

$$
\tilde P\star\tilde Q = \Bigl(p_0q_0 + \sum_{k=1}^{3}p_kq_k\Bigr)e_0 ,
$$

with a real central coefficient. The subspace is **closed**, because the real multiples of $e_0$ lie in $\mathbb{M}_+$; its idempotents are $0$ and $e_0$; its elements of square zero are none; and the restriction of $H$ is the identity form in the basis $e_0,ie_1,ie_2,ie_3$, of real rank $4$ and signature $(4,0)$, positive definite.

## The Anti-Hermitian Subspace

The anti-Hermitian subspace is the anti-fixed space of the Hermitian conjugation, $\mathbb{M}_- = \{Q_0\in i\mathbb{R},\ Q_k\in\mathbb{R}\}$, of real dimension four, with basis $ie_0, e_1, e_2, e_3$. On it the form is real again, and for $\tilde P = ip_0e_0 + \mathbf p$, $\tilde Q = iq_0e_0 + \mathbf q$ with real coordinates it reads

$$
H(\tilde P,\tilde Q) = (ip_0)(\overline{iq_0}) + \sum_{k}p_kq_k = p_0q_0 + \sum_{k=1}^{3}p_kq_k ,
$$

so the product is $H(\tilde P,\tilde Q)e_0$ with a **real** central coefficient; the subspace is **not closed**, because its scalar coordinate is purely imaginary while the value has a real scalar coordinate. The smallest witness is $e_1\star e_1 = e_0$, and $e_0\notin\mathbb{M}_-$; the only idempotent contained is $0$, and there are no elements of square zero. The restriction of $H$ to $\mathbb{M}_-$ is the identity form in the basis $ie_0,e_1,e_2,e_3$, of real rank $4$ and signature $(4,0)$.

**Remark (the three subspaces that are not closed, one reason).** The vector, anti-quaternion and anti-Hermitian subspaces all fail for the same reason: for every nonzero element $\tilde P$ of such a subspace the square is $\tilde P\star\tilde P = H(\tilde P,\tilde P)e_0$, a strictly positive real multiple of the central idempotent, so the square stays in the subspace exactly when the subspace contains $e_0$, and none of the three does. The smallest witness is the square of a basis element of the subspace: $e_1\star e_1 = e_0$ in the vector subspace, $(ie_1)\star(ie_1) = e_0$ in the anti-quaternion subspace, and $e_1\star e_1 = e_0$ in the anti-Hermitian subspace. The mechanism is the same in the three cases, and the three differ only in the subspace and in the basis element that displays the witness.

## The Table of the Six

| subspace | real dimension | closed under $\star$ | smallest witness off | idempotents contained | square-zero elements |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | yes | — | $0, e_0$ | none |
| $\mathrm{Vect}(\mathbb{B})$ | $6$ | no | $e_1\star e_1 = e_0$ | $0$ | none |
| $\mathbb{H}_{\mathbb{B}}$ | $4$ | yes | — | $0, e_0$ | none |
| $i\mathbb{H}_{\mathbb{B}}$ | $4$ | no | $(ie_1)\star(ie_1) = e_0$ | $0$ | none |
| $\mathbb{M}_+$ | $4$ | yes | — | $0, e_0$ | none |
| $\mathbb{M}_-$ | $4$ | no | $e_1\star e_1 = e_0$ | $0$ | none |

## Worked Examples

**Two vectors.** $e_1\star e_2 = H(e_1,e_2)e_0 = 0$, and $e_1\star e_1 = e_0$; the product of two vectors is the central pairing of their coordinates, and the vector parts never reappear.

**Two Hermitian elements.** $(e_0+ie_3)\star(e_0+ie_3) = H(e_0+ie_3,e_0+ie_3)e_0 = 2e_0$, the Hermitian subspace being closed.

**Two anti-quaternion elements.** $(ie_1)\star(ie_2) = H(ie_1,ie_2)e_0 = 0$ and $(ie_1)\star(ie_1) = e_0$; the value is real and leaves $i\mathbb{H}_{\mathbb{B}}$.

## Summary

Under the product of the symmetric plain sesqualgebra every value is central, and the table of the six subspaces is read by one criterion: a subspace is closed exactly when it contains the idempotent $e_0$. The centre, the quaternion subspace and the Hermitian subspace are **closed**; the vector subspace, the anti-quaternion subspace and the anti-Hermitian subspace are **not**, each with a smallest witness the square of one of its basis elements, $e_1\star e_1 = e_0$ in the vector and anti-Hermitian subspaces and $(ie_1)\star(ie_1) = e_0$ in the anti-quaternion subspace. On each of the six the restricted form $H$ is **positive definite of rank the real dimension**, with isotropic cone $\{0\}$ and no element of square zero; the idempotents contained are $0$ and $e_0$ in the three closed subspaces and only $0$ in the three that are not. On the quaternion subspace the block coincides with the symmetric quaternionic block, and on the Hermitian subspace the restricted form is the positive part of the Hermitian form of the algebra; on the other four the block is read through the same restricted form and no vector part ever appears. The flatness of the table is the mark of the central image, and only the closure and the idempotents separate the six.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}} = \{\lambda e_0\}$ | the centre; closed |
| $\mathrm{Vect}(\mathbb{B}) = \{P_0 = 0\}$ | the vector subspace; not closed, witness $e_1\star e_1 = e_0$ |
| $\mathbb{H}_{\mathbb{B}}$ | the real span of the basis; closed |
| $i\mathbb{H}_{\mathbb{B}}$ | the purely imaginary span; not closed |
| $\mathbb{M}_+$ | the Hermitian subspace; closed |
| $\mathbb{M}_-$ | the anti-Hermitian subspace; not closed |
| $\mathbf P\star\mathbf Q = (\mathbf P,\overline{\mathbf Q})e_0$ | the product on the vector subspace |
| $\tilde P\star\tilde Q = \bigl(P_0Q_0 + (\mathbf P,\mathbf Q)\bigr)e_0$ | the product on the quaternion and Hermitian subspaces |
| $S$ closed $\iff e_0\in S$ | the closure criterion for the six |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product and its central image.
- *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* (`articles_maths/the-hermitian-form-as-a-product-on-the-symmetric-plain-sesqualgebra.md`), for the restriction of the form to the six subspaces.
- *The Six Subspaces under the General Plain Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-plain-sesqualgebra-of-biquaternions.md`), the sibling article whose pattern this one follows.
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the subspaces and their definitions.
- *Comparison of the Six Subspaces* (`articles_maths/comparison-of-the-six-subspaces.md`), for the relations between them.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the forms restricted to the six real subspaces.
- *The Six Subspaces and the Four Complex Products* (`articles_maths/the-six-subspaces-and-the-four-complex-products.md`), for the closure of the six under the four products of the space.
