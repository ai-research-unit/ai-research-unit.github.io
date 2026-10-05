# __The Quaternion Subspace under the Four Forms__

## Introduction

The quaternion subspace $\mathbb{H}_{\mathbb{B}}$ is one of the six distinguished subspaces of the biquaternion algebra $\mathbb{B}$, defined and developed in *Introduction to the Six Subspaces* in the Algebra group. It reads the subspace for its basis, its defining involution, its algebra and module structure and its elements; this one reads it for its **topology**, and it does so four times.

The algebra carries four pairings of its elements — the **complex bilinear form** $\langle\cdot,\cdot\rangle$, the **quaternion bilinear form** $\langle\cdot,\cdot\rangle_{\natural}$, the **complex sesquilinear form** $\langle\cdot,\cdot\rangle_{*}$ and the **quaternion sesquilinear form** $\langle\cdot,\cdot\rangle_{\natural*}$ of *The Four Pairings of the Biquaternion Algebra*, built on the natural conjugation ${}^{\natural}$, the Hermitian conjugation ${}^{*}$ and the complex conjugation $\bar{\cdot}$. Each pairing restricts to the subspace, and each restriction is a form in its own right, with its own signature, its own definiteness, its own null set and its own group of isometries; each therefore induces its own topology on the subspace. The four are kept apart in four separate sections below, and they are compared in the table at the end.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the element $\tilde{Q}=\sum_{\mu}Q_{\mu}e_{\mu}$ with $Q_{\mu}=q_{\mu}+iq'_{\mu}$, units $e_0=1$ and $e_k^2=-e_0$, central scalar imaginary $i$, scalar part $\mathrm{Sc}$, sign vector $\varepsilon=(1,-1,-1,-1)$ and $E=\mathrm{diag}(1,-1,-1,-1)$.

## The Subspace

**Definition.** The **quaternion subspace** is the fixed space of complex conjugation, $\mathbb{H}_{\mathbb{B}}=\{\tilde{Q}:\bar{\tilde{Q}}=\tilde{Q}\}$. It is the set of elements with real coefficients.

It is $\mathrm{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3\}$, of real dimension $4$; it is a subalgebra isomorphic to the real quaternions $\mathbb{H}$.

## The Restriction of the Complex Bilinear Form

**Theorem (the restriction of the complex bilinear form).** On $\mathbb{H}_{\mathbb{B}}$ the complex bilinear form is

$$
\langle\tilde{Q},\tilde{Q}\rangle = q_0^2-q_1^2-q_2^2-q_3^2 ,
$$

a real form of signature $(1,3)$ on the 4 real dimensions of the subspace.

**Proof.** On the real quaternions $\bar{\tilde{Q}}=\tilde{Q}$, so the coefficients $q_\mu$ are real and $\langle\tilde{Q},\tilde{Q}\rangle=\sum_\mu\varepsilon_\mu q_\mu^2=q_0^2-\sum_kq_k^2$, one positive and three negative directions.

The restriction is Lorentzian of signature $(1,3)$: it is the interval form of Minkowski space on the four real coordinates, and it agrees with the quaternion sesquilinear form on this subspace, the coefficient conjugation acting trivially on the real coefficients.

**The null set.** the light cone $q_0^2=q_1^2+q_2^2+q_3^2$, of real dimension $3$: the timelike, lightlike and spacelike vectors of the interval form on the subspace.

**The isometry group.** The restriction is a real form of signature $(1,3)$, so its group of **real-linear** isometries on $\mathbb{H}_{\mathbb{B}}$ is $O(1,3)$; inside the ambient isometry group $O_4(\mathbb{C})$ of *The Four Pairings of the Biquaternion Algebra* the elements that preserve $\mathbb{H}_{\mathbb{B}}$ form the corresponding subgroup.

## The Restriction of the Quaternion Bilinear Form

**Theorem (the restriction of the quaternion bilinear form).** On $\mathbb{H}_{\mathbb{B}}$ the quaternion bilinear form is

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_\mu q_\mu^2 ,
$$

a real form of signature $(4,0)$ on the 4 real dimensions of the subspace.

**Proof.** On the subspace every coefficient is real, $Q_\mu=q_\mu$, so $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_\mu q_\mu^2$ is a sum of four real squares.

The restriction is positive definite. This is the one of the six subspaces on which the quaternion bilinear form is a sum of squares with no sign beside it, and it is the reason the subspace is a division algebra.

**The null set.** The form is positive definite, so the origin is its only isotropic point; the subspace carries no zero divisor and no nilpotent element.

**The isometry group.** The restriction is a real form of signature $(4,0)$, so its group of **real-linear** isometries on $\mathbb{H}_{\mathbb{B}}$ is the orthogonal group $O(4)$; inside the ambient isometry group $O_4(\mathbb{C})$ of *The Four Pairings of the Biquaternion Algebra* the elements that preserve $\mathbb{H}_{\mathbb{B}}$ form the corresponding subgroup.

## The Restriction of the Complex Sesquilinear Form

**Theorem (the restriction of the complex sesquilinear form).** On $\mathbb{H}_{\mathbb{B}}$ the complex sesquilinear form is

$$
\langle\tilde{Q},\tilde{Q}\rangle_{*} = \sum_\mu q_\mu^2 ,
$$

of signature $(4,0)$.

**Proof.** $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu|Q_\mu|^2$ equals $\sum_\mu q_\mu^2$ because each $Q_\mu$ is real.

The complex sesquilinear restriction coincides with the quaternion bilinear one: on the quaternion subspace the two forms agree, so the two topologies induce the same Euclidean structure.

**The Euclidean topology.** The restriction is positive definite, so it is a Euclidean inner product on the 4 real dimensions of the subspace. It defines the Euclidean norm $\lVert\tilde{Q}\rVert_E$, the distance and the balls, and hence the Euclidean topology of the subspace; on the algebra as a whole this is the topology of *The Euclidean Topology of the Biquaternion Algebra*. Its group of **real-linear** isometries on $\mathbb{H}_{\mathbb{B}}$ is the compact orthogonal group $O(4)$, contained in the ambient unitary group $U(4)$ of *The Unitary Group of the Biquaternion Algebra*.

**The null set.** The form is positive definite, so $\langle\tilde{Q},\tilde{Q}\rangle_{*}=0$ holds only at $\tilde{Q}=0$: the subspace carries no isotropic vector for the complex sesquilinear form.

## The Restriction of the Quaternion Sesquilinear Form

**Theorem (the restriction of the quaternion sesquilinear form).** On $\mathbb{H}_{\mathbb{B}}$ the quaternion sesquilinear form is

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural*} = q_0^2-q_1^2-q_2^2-q_3^2 ,
$$

of signature $(1,3)$.

**Proof.** $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\sum_\mu\varepsilon_\mu q_\mu^2$ with $\varepsilon=(1,-1,-1,-1)$ gives one positive and three negative directions.

The quaternion sesquilinear restriction is a Lorentzian form, the interval form of Minkowski space on the four real coordinates; it agrees with the complex bilinear restriction on this subspace.

**The null set.** the light cone $q_0^2=q_1^2+q_2^2+q_3^2$, of real dimension $3$: the timelike, lightlike and spacelike vectors of the Minkowski form on the subspace.

**The isometry group.** The restriction is a real form of signature $(1,3)$, so its group of **real-linear** isometries on $\mathbb{H}_{\mathbb{B}}$ is $O(1,3)$; inside the ambient group $U(1,3)$ of *The Krein Isometry Group and Its $J$-Contractions* the elements preserving $\mathbb{H}_{\mathbb{B}}$ form the corresponding subgroup.

## The Four Forms Compared

The four restrictions are collected in one table; each entry is a form on the same real vector space $\mathbb{H}_{\mathbb{B}}$, and the signatures are those of the underlying real form.

| form | expression | restriction on $\mathbb{H}_{\mathbb{B}}$ | signature | definiteness | null set | isometry group |
|---|---|---|---|---|---|---|
| complex bilinear | $\langle\tilde{Q},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{Q}\tilde{Q})$ | $q_0^2-\sum_kq_k^2$ | $(1,3)$ | indefinite (Lorentzian) | $q_0^2=\sum_kq_k^2$ | $O(1,3)$ |
| quaternion bilinear | $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\mathrm{Sc}(\tilde{Q}^{\natural}\tilde{Q})$ | $\sum_\mu q_\mu^2$ | $(4,0)$ | positive definite | $\{0\}$ | $O(4)$ |
| complex sesquilinear | $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*})$ | $\sum_\mu q_\mu^2$ | $(4,0)$ | positive definite | $\{0\}$ | $O(4)$ |
| quaternion sesquilinear | $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\mathrm{Sc}(\tilde{Q}^{\natural}\tilde{Q}^{*})$ | $q_0^2-\sum_kq_k^2$ | $(1,3)$ | indefinite (Lorentzian) | $q_0^2=\sum_kq_k^2$ | $O(1,3)$ |

The four restrictions fall into two pairs: the complex bilinear form and the quaternion sesquilinear form coincide and are the Lorentzian form $q_0^2-\sum_kq_k^2$ of signature $(1,3)$ with the light cone $q_0^2=\sum_kq_k^2$ as null set, and the quaternion bilinear form and the complex sesquilinear form coincide and are the Euclidean square $\sum_\mu q_\mu^2$ of signature $(4,0)$. The subspace is the fixed space of the coefficient conjugation, which is why the bilinear and the sesquilinear readings meet there.
## Summary

On the quaternion subspace the four forms give two pairs: the complex bilinear form and the quaternion sesquilinear form coincide and are the Lorentzian interval form $q_0^2-\sum_kq_k^2$ of signature $(1,3)$, with the light cone $q_0^2=\sum_kq_k^2$ as null set; and the quaternion bilinear form and the complex sesquilinear form coincide and are the Euclidean square $\sum_\mu q_\mu^2$ of signature $(4,0)$, positive definite. The isometry groups are $O(1,3)$, $O(4)$, $O(4)$ and $O(1,3)$.
## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{B}}$ | the quaternion subspace, of real dimension $4$ |
| $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$ | the complex bilinear, quaternion bilinear, complex sesquilinear and quaternion sesquilinear forms of *The Four Pairings of the Biquaternion Algebra* |
| $(1,3)$ | the signature of the complex bilinear form on $\mathbb{H}_{\mathbb{B}}$, indefinite (Lorentzian)
| $(4,0)$ | the signature of the quaternion bilinear form on $\mathbb{H}_{\mathbb{B}}$, positive definite
| $(4,0)$ | the signature of the complex sesquilinear form on $\mathbb{H}_{\mathbb{B}}$, the same form
| $(1,3)$ | the signature of the quaternion sesquilinear form on $\mathbb{H}_{\mathbb{B}}$, the same form as the complex bilinear form
| $O(1,3)$, $O(4)$, $O(4)$, $O(1,3)$ | the isometry groups of the four restrictions |
## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the subspace itself in the Algebra group
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms and the four Gram matrices
- *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), for the quaternion bilinear pairing and its restrictions
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the complex sesquilinear pairing and the Euclidean norm it defines
- *The Complex Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-complex-bilinear-form-on-the-biquaternion-algebra.md`), for the complex bilinear pairing and its isotropic structure
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the quaternion sesquilinear pairing and the same six restrictions
- *Comparison of the Six Subspaces* (`articles_maths/comparison-of-the-six-subspaces.md`), for the six subspaces together and their intersections
- *Biquaternion Lorentzian and Conformal Geometry* (`articles_maths/biquaternion-lorentzian-and-conformal-geometry.md`), for the Lorentzian reading in the large
