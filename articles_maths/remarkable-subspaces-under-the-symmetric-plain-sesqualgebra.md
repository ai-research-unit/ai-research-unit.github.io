# __Remarkable Subspaces under the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde Q_1\star\tilde Q_2 = \langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$ (*Introduction to the Symmetric Plain Sesqualgebra*), and its values lie in the centre $\mathbb{C}_{\mathbb{B}}$ whatever the two arguments are. This article reads the remarkable subspaces of the algebra — the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ — under that product, one to a section, in the pattern of *Remarkable Subspaces under the General Plain Sesqualgebra*.

The central image **flattens the table**, and the point of the article is to say so and to read what is left. Because every value is a scalar multiple of $e_t$, the product of two elements of a subspace $S$ lies in $S$ exactly when $S$ contains the idempotent $e_t$; the closure of the product, which in a product with a vector part is a genuine computation on each subspace, here reduces to the single question *does $S$ contain $e_t$*. The answer is yes for the centre, for the quaternion subspace and for the Hermitian subspace, and no for the vector subspace, for the anti-quaternion subspace and for the anti-Hermitian subspace, each with a smallest witness that is the square of one of its basis elements, $\vec e_x\star \vec e_x = e_t$ in the vector and anti-Hermitian subspaces and $(i\vec e_x)\star(i\vec e_x) = e_t$ in the anti-quaternion subspace. What remains is the reading of each subspace — the restricted form, its rank and signature, the idempotents, the elements of square zero and the isotropic elements — which the sections give one by one; the restricted form is the identity form on the natural real basis, positive definite, of rank the real dimension in every case, so apart from the closure and the idempotents the readings coincide, and this flatness is the mark of the central image.

## The Closure of the remarkable subspaces, in One Statement

**Theorem (closure, read by the idempotent).** Let $S$ be one of the remarkable subspaces. Then $S$ is closed under the product of the block, $\tilde Q_1\star\tilde Q_2 \in S$ for all $\tilde Q_1,\tilde Q_2 \in S$, if and only if $e_t \in S$.

*Proof.* If $e_t\in S$ then the value $\langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$ lies in $S$: for the complex subspace $\mathbb{C}_{\mathbb{B}}$ the coefficient is an arbitrary complex number and $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_t$; for the real subspaces $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_+$ the coefficient is real, and the real multiples of $e_t$ lie in the subspace. If $e_t\notin S$, take any nonzero $\tilde Q_1\in S$; then $\tilde Q_1\star\tilde Q_1 = \langle\tilde Q_1,\tilde Q_1\rangle_{*}e_t$ is a strictly positive real multiple of $e_t$, so it lies in $S$ only if $e_t$ lies in $S$, and the product therefore leaves $S$.

**Corollary (the three closed and the three that are not).** Of the remarkable subspaces, the centre, the quaternion subspace and the Hermitian subspace contain $e_t$ and are closed; the vector subspace, the anti-quaternion subspace and the anti-Hermitian subspace do not and are not.

## The Centre

The centre is $\mathbb{C}_{\mathbb{B}} = \{\lambda e_t : \lambda\in\mathbb{C}\}$, the one-dimensional complex subspace of the scalars. On it the form is $\langle \lambda e_t,\mu e_t\rangle_{*} = \lambda\overline{\mu}$, so the product reads

$$
(\lambda e_t)\star(\mu e_t) = \lambda\overline{\mu}\,e_t ,
$$

the multiplication of the field by the conjugate of the second factor. The centre is **closed** and is the smallest of the remarkable subspaces; the product on it is conjugate-commutative, has the idempotents $0$ and $e_t$, and has no unit, since $(\lambda e_t)\star e_t = \lambda e_t$ only for the elements of the centre and not for the general element of the space. The restriction of $\langle\cdot,\cdot\rangle_{*}$ to the centre is the positive definite form $\lambda\overline{\mu}$ of real rank $2$; it has no isotropic element, and the elements of square zero are none.

## The Vector Subspace

The vector subspace is $\mathrm{Vect}(\mathbb{B}) = \{\vec Q_1 : Q_{1t} = 0\}$, of real dimension six. On it the form is $\langle \vec Q_1,\vec Q_2\rangle_{*} = (\vec Q_1,\overline{\vec Q_2})$, so the product of two vectors is the central element

$$ \boxed{\; \vec Q_1\star\vec Q_2 = (\vec Q_1,\overline{\vec Q_2})\,e_t \;}, $$

and it is **not closed**: the smallest witness is $\vec e_x\star \vec e_x = \langle \vec e_x,\vec e_x\rangle_{*}e_t = e_t$, which leaves the vector subspace because it has a scalar part. The element $e_t$ is not in the subspace, so the only idempotent the subspace contains is $0$; the elements of square zero are none, since $\langle \vec Q_1,\vec Q_1\rangle_{*} = \sum_{k}\lvert Q_{1,k}\rvert^{2}$ vanishes only at the origin; and the restriction of $\langle\cdot,\cdot\rangle_{*}$ is positive definite of real rank $6$, with isotropic cone $\{0\}$.

## The Quaternion Subspace

The quaternion subspace is $\mathbb{H}_{\mathbb{B}} = \{\sum_\mu P_\mu e_\mu : P_\mu\in\mathbb{R}\}$, the real span of the basis, of real dimension four. On it the form is real and is the quaternion form, $\langle\tilde Q_1,\tilde Q_2\rangle_{*} = Q_{1t}Q_{2t} + (\vec Q_1,\vec Q_2) = \langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$, so the product is

$$ \boxed{\; \tilde Q_1\star\tilde Q_2 = \bigl(Q_{1t}Q_{2t} + (\vec Q_1,\vec Q_2)\bigr)e_t \;}, $$

with a **real** central coefficient. The subspace is **closed**, because the value is a real multiple of $e_t$ and the real multiples of $e_t$ lie in $\mathbb{H}_{\mathbb{B}}$; it is the smallest closed subspace containing the basis $e_t,\vec e_x,\vec e_y,\vec e_z$. Its idempotents are $0$ and $e_t$, the same two as the block, and its elements of square zero are none. The restriction of $\langle\cdot,\cdot\rangle_{*}$ is the identity form on the basis, of real rank $4$ and signature $(4,0)$; on this subspace the block coincides with the symmetric quaternionic block, and the section is the bridge between the two rows in coordinates.

## The Anti-Quaternion Subspace

The anti-quaternion subspace is $i\mathbb{H}_{\mathbb{B}} = \{\sum_\mu P_\mu e_\mu : P_\mu\in i\mathbb{R}\}$, of real dimension four. On it the form is real again, $\langle i\tilde Q_1,i\tilde Q_2\rangle_{*} = \sum_\mu Q_{1,\mu} Q_{2,\mu}$ for real $\tilde Q_1,\tilde Q_2$, so the product is

$$
(i\tilde Q_1)\star(i\tilde Q_2) = \Bigl(\sum_\mu Q_{1,\mu} Q_{2,\mu}\Bigr)e_t ,
$$

with a real central coefficient; the subspace is **not closed**, because its elements have a purely imaginary scalar coordinate and the value $e_t$ is real. The smallest witness is $(i\vec e_x)\star(i\vec e_x) = e_t$, with $i\vec e_x\in i\mathbb{H}_{\mathbb{B}}$ a basis element of the subspace; more sharply, the value of two anti-quaternion elements is always a **real** multiple of $e_t$, and lands in the quaternion subspace and not in $i\mathbb{H}_{\mathbb{B}}$. The idempotents contained are $0$ alone, and the elements of square zero are none. The restriction of $\langle\cdot,\cdot\rangle_{*}$ is the identity form in the imaginary basis $ie_t,i\vec e_x,i\vec e_y,i\vec e_z$, of real rank $4$ and signature $(4,0)$.

## The Hermitian Subspace

The Hermitian subspace is the fixed space of the Hermitian conjugation, $\mathbb{M}_+ = \{p_te_t + \sum_{k}p_k(i\vec e_k) : p_\mu\in\mathbb{R}\}$, of real dimension four, with real basis $e_t, i\vec e_x, i\vec e_y, i\vec e_z$. On it the form is real and is the identity form in this basis,

$$ \boxed{\; \langle\tilde Q_1,\tilde Q_2\rangle_{*} = p_tq_t + \sum_{k\in\{x,y,z\}} p_kq_k , \qquad \tilde Q_1,\tilde Q_2\in\mathbb{M}_+ \;}, $$

which is the positive part of the Hermitian form of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* restricted to its coordinates, so the product reads

$$
\tilde Q_1\star\tilde Q_2 = \Bigl(p_tq_t + \sum_{k\in\{x,y,z\}}p_kq_k\Bigr)e_t ,
$$

with a real central coefficient. The subspace is **closed**, because the real multiples of $e_t$ lie in $\mathbb{M}_+$; its idempotents are $0$ and $e_t$; its elements of square zero are none; and the restriction of $\langle\cdot,\cdot\rangle_{*}$ is the identity form in the basis $e_t,i\vec e_x,i\vec e_y,i\vec e_z$, of real rank $4$ and signature $(4,0)$, positive definite.

## The Anti-Hermitian Subspace

The anti-Hermitian subspace is the anti-fixed space of the Hermitian conjugation, $\mathbb{M}_- = \{Q_t\in i\mathbb{R},\ Q_k\in\mathbb{R}\}$, of real dimension four, with basis $ie_t, \vec e_x, \vec e_y, \vec e_z$. On it the form is real again, and for $\tilde Q_1 = ip_te_t + \vec p$, $\tilde Q_2 = iq_te_t + \vec q$ with real coordinates it reads

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*} = (ip_t)(\overline{iq_t}) + \sum_{k}p_kq_k = p_tq_t + \sum_{k\in\{x,y,z\}}p_kq_k ,
$$

so the product is $\langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$ with a **real** central coefficient; the subspace is **not closed**, because its scalar coordinate is purely imaginary while the value has a real scalar coordinate. The smallest witness is $\vec e_x\star \vec e_x = e_t$, and $e_t\notin\mathbb{M}_-$; the only idempotent contained is $0$, and there are no elements of square zero. The restriction of $\langle\cdot,\cdot\rangle_{*}$ to $\mathbb{M}_-$ is the identity form in the basis $ie_t,\vec e_x,\vec e_y,\vec e_z$, of real rank $4$ and signature $(4,0)$.

**Remark (the three subspaces that are not closed, one reason).** The vector, anti-quaternion and anti-Hermitian subspaces all fail for the same reason: for every nonzero element $\tilde Q_1$ of such a subspace the square is $\tilde Q_1\star\tilde Q_1 = \langle\tilde Q_1,\tilde Q_1\rangle_{*}e_t$, a strictly positive real multiple of the central idempotent, so the square stays in the subspace exactly when the subspace contains $e_t$, and none of the three does. The smallest witness is the square of a basis element of the subspace: $\vec e_x\star \vec e_x = e_t$ in the vector subspace, $(i\vec e_x)\star(i\vec e_x) = e_t$ in the anti-quaternion subspace, and $\vec e_x\star \vec e_x = e_t$ in the anti-Hermitian subspace. The mechanism is the same in the three cases, and the three differ only in the subspace and in the basis element that displays the witness.

## The Table of the Remarkable Subspaces

| subspace | real dimension | closed under $\star$ | smallest witness off | idempotents contained | square-zero elements |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | yes | — | $0, e_t$ | none |
| $\mathrm{Vect}(\mathbb{B})$ | $6$ | no | $\vec e_x\star \vec e_x = e_t$ | $0$ | none |
| $\mathbb{H}_{\mathbb{B}}$ | $4$ | yes | — | $0, e_t$ | none |
| $i\mathbb{H}_{\mathbb{B}}$ | $4$ | no | $(i\vec e_x)\star(i\vec e_x) = e_t$ | $0$ | none |
| $\mathbb{M}_+$ | $4$ | yes | — | $0, e_t$ | none |
| $\mathbb{M}_-$ | $4$ | no | $\vec e_x\star \vec e_x = e_t$ | $0$ | none |

## Worked Examples

**Two vectors.** $\vec e_x\star \vec e_y = \langle \vec e_x,\vec e_y\rangle_{*}e_t = 0$, and $\vec e_x\star \vec e_x = e_t$; the product of two vectors is the central pairing of their coordinates, and the vector parts never reappear.

**Two Hermitian elements.** $(e_t+i\vec e_z)\star(e_t+i\vec e_z) = \langle e_t+i\vec e_z,e_t+i\vec e_z\rangle_{*}e_t = 2e_t$, the Hermitian subspace being closed.

**Two anti-quaternion elements.** $(i\vec e_x)\star(i\vec e_y) = \langle i\vec e_x,i\vec e_y\rangle_{*}e_t = 0$ and $(i\vec e_x)\star(i\vec e_x) = e_t$; the value is real and leaves $i\mathbb{H}_{\mathbb{B}}$.

## Summary

Under the product of the symmetric plain sesqualgebra every value is central, and the table of the remarkable subspaces is read by one criterion: a subspace is closed exactly when it contains the idempotent $e_t$. The centre, the quaternion subspace and the Hermitian subspace are **closed**; the vector subspace, the anti-quaternion subspace and the anti-Hermitian subspace are **not**, each with a smallest witness the square of one of its basis elements, $\vec e_x\star \vec e_x = e_t$ in the vector and anti-Hermitian subspaces and $(i\vec e_x)\star(i\vec e_x) = e_t$ in the anti-quaternion subspace. On each of the remarkable subspaces the restricted form $\langle\cdot,\cdot\rangle_{*}$ is **positive definite of rank the real dimension**, with isotropic cone $\{0\}$ and no element of square zero; the idempotents contained are $0$ and $e_t$ in the three closed subspaces and only $0$ in the three that are not. On the quaternion subspace the block coincides with the symmetric quaternionic block, and on the Hermitian subspace the restricted form is the positive part of the Hermitian form of the algebra; on the other four the block is read through the same restricted form and no vector part ever appears. The flatness of the table is the mark of the central image, and only the closure and the idempotents separate the remarkable subspaces.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}} = \{\lambda e_t\}$ | the centre; closed |
| $\mathrm{Vect}(\mathbb{B}) = \{Q_{1t} = 0\}$ | the vector subspace; not closed, witness $\vec e_x\star \vec e_x = e_t$ |
| $\mathbb{H}_{\mathbb{B}}$ | the real span of the basis; closed |
| $i\mathbb{H}_{\mathbb{B}}$ | the purely imaginary span; not closed |
| $\mathbb{M}_+$ | the Hermitian subspace; closed |
| $\mathbb{M}_-$ | the anti-Hermitian subspace; not closed |
| $\vec Q_1\star\vec Q_2 = (\vec Q_1,\overline{\vec Q_2})e_t$ | the product on the vector subspace |
| $\tilde Q_1\star\tilde Q_2 = \bigl(Q_{1t}Q_{2t} + (\vec Q_1,\vec Q_2)\bigr)e_t$ | the product on the quaternion and Hermitian subspaces |
| $S$ closed $\iff e_t\in S$ | the closure criterion for the remarkable subspaces |

## Further Reading

- [Introduction to the Symmetric Plain Sesqualgebra](introduction-to-the-symmetric-plain-sesqualgebra.html), for the product and its central image.
- [The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra](the-hermitian-form-as-a-product-on-the-symmetric-plain-sesqualgebra.html), for the restriction of the form to the remarkable subspaces.
- [Remarkable Subspaces under the General Plain Sesqualgebra](remarkable-subspaces-under-the-general-plain-sesqualgebra.html), the sibling article whose pattern this one follows.
- [The Six Subspaces](the-six-subspaces.html), for the subspaces and their definitions.
- [The Subspaces and Their Relations](the-subspaces-and-their-relations.html), for the relations between them.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the forms restricted to the remarkable real subspaces.
- [Remarkable Subspaces and the Four General Products, Forms and Norms](remarkable-subspaces-and-the-four-general-products-forms-and-norms.html), for the closure of the remarkable subspaces under the four general products of the space.
