# __The Centre Subspace under the Three Topologies__

## Introduction

The centre subspace $\mathbb{C}_{\mathbb{B}}$ is one of the six distinguished subspaces of the biquaternion algebra $\mathbb{B}$, defined and developed in *Introduction to the Six Subspaces* in the Algebra group. It reads the subspace for its basis, its defining involution, its algebra and module structure and its elements; this one reads it for its **topology**, and it does so three times.

The algebra carries three pairings of its elements — the **bilinear form** $B$, the **Hermitian form** $\langle\cdot,\cdot\rangle$ and the **Krein form** $[\cdot,\cdot]$ of *The Three Pairings of the Biquaternion Algebra*, built on the natural conjugation ${}^{\natural}$, the Hermitian conjugation ${}^{*}$ and the complex conjugation $\bar{\cdot}$. Each pairing restricts to the subspace, and each restriction is a form in its own right, with its own signature, its own definiteness, its own null set and its own group of isometries; each therefore induces its own topology on the subspace. The three are kept apart in three separate sections below, and they are compared in the table at the end.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the element $\tilde{Q}=\sum_{\mu}Q_{\mu}e_{\mu}$ with $Q_{\mu}=q_{\mu}+iq'_{\mu}$, units $e_0=1$ and $e_k^2=-e_0$, central scalar imaginary $i$, scalar part $\mathrm{Sc}$, sign vector $\varepsilon=(1,-1,-1,-1)$ and $E=\mathrm{diag}(1,-1,-1,-1)$.

## The Subspace

**Definition.** The **centre subspace** is the fixed space of quaternion conjugation, $\mathbb{C}_{\mathbb{B}}=\{\tilde{Q}:\tilde{Q}^{\natural}=\tilde{Q}\}$. It is the complex line $\mathbb{C}e_0$.

In real coordinates it is $\{q_0e_0+iq'_0e_0\}$, of real dimension $2$ and real basis $e_0,ie_0$; it is a subalgebra isomorphic to $\mathbb{C}$, and it is the centre of $\mathbb{B}$.

## The Topology Induced by the Bilinear Form

**Theorem (the restriction of the bilinear form).** On $\mathbb{C}_{\mathbb{B}}$ the bilinear form is

$$
B(\tilde{Q},\tilde{Q}) = N(\tilde{Q}) = Q_0^2 = q_0^2 - (q'_0)^2 ,
$$

a real form of signature $(1,1)$ on the 2 real dimensions of the subspace.

**Proof.** On the line $\mathbb{C}e_0$ one has $\tilde{Q}^{\natural}=\tilde{Q}$, so $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}=Q_0^2$; writing $Q_0=q_0+iq'_0$ gives the real form $q_0^2-(q'_0)^2$.

The restriction is a hyperbolic plane: it is indefinite, with one positive and one negative direction, and it is the smallest carrier of an indefinite form. This is the one topology on the centre that is not positive definite.

**The null set.** the two real lines $q_0=\pm q'_0$, that is $\mathbb{R}(e_0+ie_0)$ and $\mathbb{R}(e_0-ie_0)$; excepting the origin, none of their points is a zero divisor of the algebra, since $\mathbb{C}_{\mathbb{B}}$ is a field.

**The isometry group.** The restriction is a real form of signature $(1,1)$, so its group of **real-linear** isometries on $\mathbb{C}_{\mathbb{B}}$ is the orthogonal group $O(1,1)$; inside the ambient isometry group $O_4(\mathbb{C})$ of *The Three Pairings of the Biquaternion Algebra* the elements that preserve $\mathbb{C}_{\mathbb{B}}$ form the corresponding subgroup.

## The Topology Induced by the Hermitian Form

**Theorem (the restriction of the Hermitian form).** On $\mathbb{C}_{\mathbb{B}}$ the Hermitian form is

$$
\langle\tilde{Q},\tilde{Q}\rangle = |Q_0|^2 = q_0^2 + (q'_0)^2 ,
$$

of signature $(2,0)$.

**Proof.** $\langle\tilde{Q},\tilde{Q}\rangle=\sum_\mu|Q_\mu|^2$ reduces to the single term $|Q_0|^2$.

The Hermitian form is the square of the complex absolute value on the line; it is the Euclidean form of $\mathbb{C}$.

**The Euclidean topology.** The restriction is positive definite, so it is a Euclidean inner product on the 2 real dimensions of the subspace. It defines the Euclidean norm $\lVert\tilde{Q}\rVert_E$, the distance and the balls, and hence the Euclidean topology of the subspace; on the algebra as a whole this is the topology of *The Euclidean Topology of the Biquaternion Algebra*. Its group of **real-linear** isometries on $\mathbb{C}_{\mathbb{B}}$ is the compact orthogonal group $O(2)$, contained in the ambient unitary group $U(4)$ of *The Unitary Group of the Biquaternion Algebra*.

**The null set.** The form is positive definite, so $\langle\tilde{Q},\tilde{Q}\rangle=0$ holds only at $\tilde{Q}=0$: the subspace carries no isotropic vector for the Hermitian form.

## The Topology Induced by the Krein Form

**Theorem (the restriction of the Krein form).** On $\mathbb{C}_{\mathbb{B}}$ the Krein form is

$$
[\tilde{Q},\tilde{Q}] = |Q_0|^2 = q_0^2 + (q'_0)^2 ,
$$

of signature $(2,0)$.

**Proof.** $[\tilde{Q},\tilde{Q}]=\sum_\mu\varepsilon_\mu|Q_\mu|^2$ reduces to $\varepsilon_0|Q_0|^2=|Q_0|^2$, the signs of the vector directions being absent.

On the centre the Krein form and the Hermitian form agree, and both are positive definite; the centre is the maximal positive definite subspace of the Krein form, realising the whole positive index $2$ of the ambient signature $(2,6)$.

**The null set.** The form is positive definite, so the origin is its only isotropic point: no non-zero central element is Krein-isotropic.

**The isometry group.** The restriction is a real form of signature $(2,0)$, so its group of **real-linear** isometries on $\mathbb{C}_{\mathbb{B}}$ is $O(2)$; inside the ambient group $U(1,3)$ of *The Krein Isometry Group and Its $J$-Contractions* the elements preserving $\mathbb{C}_{\mathbb{B}}$ form the corresponding subgroup.

## The Three Topologies Compared

The three restrictions are collected in one table; each entry is a form on the same real vector space $\mathbb{C}_{\mathbb{B}}$, and the signatures are those of the underlying real form.

| topology | form | restriction on $\mathbb{C}_{\mathbb{B}}$ | signature | definiteness | null set | isometry group |
|---|---|---|---|---|---|---|
| bilinear | $B=\mathrm{Sc}(\tilde{Q}^{\natural}\tilde{Q})$ | $Q_0^2 = q_0^2 - (q'_0)^2$ | $(1,1)$ | indefinite | $q_0=\pm q'_0$ | $O(1,1)$ |
| Hermitian | $\langle\tilde{Q},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{Q}^{*}\tilde{Q})$ | $|Q_0|^2 = q_0^2 + (q'_0)^2$ | $(2,0)$ | positive definite | $\{0\}$ | $O(2)$ |
| Krein | $[\tilde{Q},\tilde{Q}]=\mathrm{Sc}(\bar{\tilde{Q}}\tilde{Q})$ | $|Q_0|^2 = q_0^2 + (q'_0)^2$ | $(2,0)$ | positive definite | $\{0\}$ | $O(2)$ |

The two definite topologies coincide: the Hermitian and the Krein forms are the same positive definite form on the centre, and only the bilinear form is indefinite. The centre is the only one of the six subspaces on which the Krein form is positive definite, and for this reason it is the maximal positive definite subspace of that form.

**Remark (real-linear and complex-linear isometries).** The groups in the table are those of the **real-linear** isometries of the underlying real form, and they exist for every subspace. On the centre, which is a complex vector space, the complex-linear isometries form the smaller unitary subgroup, $O_1(\mathbb{C})=\{\pm 1\}$, $U(1)$ and $U(1)$, for the bilinear, the Hermitian and the Krein restriction respectively. On the four subspaces that are not complex vector spaces no complex-linear isometry group is defined, and the real-linear group is the whole of the isometry group.

## Summary

On the centre subspace the three pairings give: the bilinear form $q_0^2-(q'_0)^2$ of signature $(1,1)$, a hyperbolic plane whose null set is the pair of lines $q_0=\pm q'_0$; the Hermitian form $|Q_0|^2$ of signature $(2,0)$, positive definite, the Euclidean form of the line $\mathbb{C}e_0$; and the Krein form $|Q_0|^2$, again of signature $(2,0)$ and positive definite, the maximal positive definite subspace of the Krein form. The two definite topologies coincide, the bilinear one is indefinite, and the three isometry groups are $O(1,1)$, $O(2)$ and $O(2)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | the centre subspace, of real dimension $2$ |
| $B$, $\langle\cdot,\cdot\rangle$, $[\cdot,\cdot]$ | the bilinear, Hermitian and Krein forms of *The Three Pairings of the Biquaternion Algebra* |
| $(1,1)$ | the signature of the bilinear form on $\mathbb{C}_{\mathbb{B}}$ |
| $(2,0)$ | the signature of the Hermitian form on $\mathbb{C}_{\mathbb{B}}$, positive definite |
| $(2,0)$ | the signature of the Krein form on $\mathbb{C}_{\mathbb{B}}$ |
| $O(1,1)$, $O(2)$, $O(2)$ | the isometry groups of the three restrictions |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the subspace itself in the Algebra group
- *The Three Pairings of the Biquaternion Algebra* (`articles_maths/the-three-pairings-of-the-biquaternion-algebra.md`), for the three forms and the three Gram matrices
- *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), for the first pairing and its restrictions
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the second pairing and the Euclidean norm it defines
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the third pairing and the same six restrictions
- *Biquaternion Relations Between Subspaces* (`articles_maths/biquaternion-relations-between-subspaces.md`), for the six subspaces together and their intersections
- *Biquaternion Involution Lattice* (`articles_maths/biquaternion-involution-lattice.md`), for the four involutions
