# __The Anti-Quaternion Subspace under the Three Topologies__

## Introduction

The anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ is one of the six distinguished subspaces of the biquaternion algebra $\mathbb{B}$, defined and developed in *Biquaternion Anti-Quaternion Subspace* in the Algebra group. That article reads the subspace for its basis, its defining involution, its algebra and module structure and its elements; this one reads it for its **topology**, and it does so three times.

The algebra carries three pairings of its elements — the **bilinear form** $B$, the **Hermitian form** $\langle\cdot,\cdot\rangle$ and the **Krein form** $[\cdot,\cdot]$ of *The Three Pairings of the Biquaternion Algebra*, built on the natural conjugation ${}^{\natural}$, the Hermitian conjugation ${}^{*}$ and the complex conjugation $\bar{\cdot}$. Each pairing restricts to the subspace, and each restriction is a form in its own right, with its own signature, its own definiteness, its own null set and its own group of isometries; each therefore induces its own topology on the subspace. The three are kept apart in three separate sections below, and they are compared in the table at the end.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the element $\tilde{Q}=\sum_{\mu}Q_{\mu}e_{\mu}$ with $Q_{\mu}=q_{\mu}+iq'_{\mu}$, units $e_0=1$ and $e_k^2=-e_0$, central scalar imaginary $i$, scalar part $\mathrm{Sc}$, sign vector $\varepsilon=(1,-1,-1,-1)$ and $E=\mathrm{diag}(1,-1,-1,-1)$.

## The Subspace

**Definition.** The **anti-quaternion subspace** is the anti-fixed space of complex conjugation, $i\mathbb{H}_{\mathbb{B}}=\{\tilde{Q}:\bar{\tilde{Q}}=-\tilde{Q}\}$. It is the set of elements with purely imaginary coefficients.

It is $\mathrm{span}_{\mathbb{R}}\{ie_0,ie_1,ie_2,ie_3\}$, of real dimension $4$; it is $i$ times the quaternion subspace, and it is not a subalgebra.

## The Topology Induced by the Bilinear Form

**Theorem (the restriction of the bilinear form).** On $i\mathbb{H}_{\mathbb{B}}$ the bilinear form is

$$
B(\tilde{Q},\tilde{Q}) = N(\tilde{Q}) = -\sum_\mu(q'_\mu)^2 ,
$$

a real form of signature $(0,4)$ on the 4 real dimensions of the subspace.

**Proof.** On the subspace $Q_\mu=iq'_\mu$, so $N(\tilde{Q})=\sum_\mu(iq'_\mu)^2=-\sum_\mu(q'_\mu)^2$ is a negative sum of four real squares.

The restriction is negative definite, the exact negative of the restriction to the quaternion subspace, the two being exchanged by multiplication by $i$.

**The null set.** The form is negative definite, so the origin is its only isotropic point; the subspace carries no zero divisor and no nilpotent element.

**The isometry group.** The restriction is a real form of signature $(0,4)$, so its group of **real-linear** isometries on $i\mathbb{H}_{\mathbb{B}}$ is the orthogonal group $O(0,4)$; inside the ambient isometry group $O_4(\mathbb{C})$ of *The Three Pairings of the Biquaternion Algebra* the elements that preserve $i\mathbb{H}_{\mathbb{B}}$ form the corresponding subgroup.

## The Topology Induced by the Hermitian Form

**Theorem (the restriction of the Hermitian form).** On $i\mathbb{H}_{\mathbb{B}}$ the Hermitian form is

$$
\langle\tilde{Q},\tilde{Q}\rangle = \sum_\mu(q'_\mu)^2 ,
$$

of signature $(4,0)$.

**Proof.** $\langle\tilde{Q},\tilde{Q}\rangle=\sum_\mu|Q_\mu|^2=\sum_\mu|iq'_\mu|^2=\sum_\mu(q'_\mu)^2$.

The Hermitian restriction is positive definite and is the negative of the bilinear one: the two forms differ by exactly the sign $i^2=-1$ on the subspace.

**The Euclidean topology.** The restriction is positive definite, so it is a Euclidean inner product on the 4 real dimensions of the subspace. It defines the Euclidean norm $\lVert\tilde{Q}\rVert_E$, the distance and the balls, and hence the Euclidean topology of the subspace; on the algebra as a whole this is the topology of *The Euclidean Topology of the Biquaternion Algebra*. Its group of **real-linear** isometries on $i\mathbb{H}_{\mathbb{B}}$ is the compact orthogonal group $O(4)$, contained in the ambient unitary group $U(4)$ of *The Unitary Group of the Biquaternion Algebra*.

**The null set.** The form is positive definite, so $\langle\tilde{Q},\tilde{Q}\rangle=0$ holds only at $\tilde{Q}=0$: the subspace carries no isotropic vector for the Hermitian form.

## The Topology Induced by the Krein Form

**Theorem (the restriction of the Krein form).** On $i\mathbb{H}_{\mathbb{B}}$ the Krein form is

$$
[\tilde{Q},\tilde{Q}] = (q'_0)^2-(q'_1)^2-(q'_2)^2-(q'_3)^2 ,
$$

of signature $(1,3)$.

**Proof.** $[\tilde{Q},\tilde{Q}]=\sum_\mu\varepsilon_\mu|Q_\mu|^2=\sum_\mu\varepsilon_\mu(q'_\mu)^2$ with $\varepsilon=(1,-1,-1,-1)$.

The restriction is Lorentzian of signature $(1,3)$, a second copy of Minkowski space, this time with the time direction the imaginary scalar line $i\mathbb{R}e_0$.

**The null set.** the cone $(q'_0)^2=(q'_1)^2+(q'_2)^2+(q'_3)^2$, of real dimension $3$, the light cone of the Minkowski form carried by the imaginary coefficients.

**The isometry group.** The restriction is a real form of signature $(1,3)$, so its group of **real-linear** isometries on $i\mathbb{H}_{\mathbb{B}}$ is $O(1,3)$; inside the ambient group $U(1,3)$ of *The Krein Isometry Group and Its $J$-Contractions* the elements preserving $i\mathbb{H}_{\mathbb{B}}$ form the corresponding subgroup.

## The Three Topologies Compared

The three restrictions are collected in one table; each entry is a form on the same real vector space $i\mathbb{H}_{\mathbb{B}}$, and the signatures are those of the underlying real form.

| topology | form | restriction on $i\mathbb{H}_{\mathbb{B}}$ | signature | definiteness | null set | isometry group |
|---|---|---|---|---|---|---|
| bilinear | $B=\mathrm{Sc}(\tilde{Q}^{\natural}\tilde{Q})$ | $-\sum_\mu(q'_\mu)^2$ | $(0,4)$ | negative definite | $\{0\}$ | $O(0,4)$ |
| Hermitian | $\langle\tilde{Q},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{Q}^{*}\tilde{Q})$ | $\sum_\mu(q'_\mu)^2$ | $(4,0)$ | positive definite | $\{0\}$ | $O(4)$ |
| Krein | $[\tilde{Q},\tilde{Q}]=\mathrm{Sc}(\bar{\tilde{Q}}\tilde{Q})$ | $(q'_0)^2-(q'_1)^2-(q'_2)^2-(q'_3)^2$ | $(1,3)$ | indefinite (Lorentzian) | $(q'_0)^2=\sum_k(q'_k)^2$ | $O(1,3)$ |

The pattern is the mirror image of the quaternion subspace: the bilinear topology is negative definite and the Hermitian one positive definite, differing by a sign, while the Krein topology is Lorentzian. It is the Krein form, and only it, that gives the subspace a null cone.

## Summary

On the anti-quaternion subspace the bilinear form restricts to $-\sum_\mu(q'_\mu)^2$ of signature $(0,4)$, negative definite; the Hermitian form to $\sum_\mu(q'_\mu)^2$ of signature $(4,0)$, positive definite, the two differing by a sign; and the Krein form to $(q'_0)^2-\sum_k(q'_k)^2$ of signature $(1,3)$, Lorentzian, with a three-dimensional light cone. The isometry groups are $O(4)$, $O(4)$ and $O(1,3)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $i\mathbb{H}_{\mathbb{B}}$ | the anti-quaternion subspace, of real dimension $4$ |
| $B$, $\langle\cdot,\cdot\rangle$, $[\cdot,\cdot]$ | the bilinear, Hermitian and Krein forms of *The Three Pairings of the Biquaternion Algebra* |
| $(0,4)$ | the signature of the bilinear form on $i\mathbb{H}_{\mathbb{B}}$ |
| $(4,0)$ | the signature of the Hermitian form on $i\mathbb{H}_{\mathbb{B}}$, positive definite |
| $(1,3)$ | the signature of the Krein form on $i\mathbb{H}_{\mathbb{B}}$ |
| $O(0,4)$, $O(4)$, $O(1,3)$ | the isometry groups of the three restrictions |

## Further Reading

- *Biquaternion Anti-Quaternion Subspace* (`articles_maths/biquaternion-anti-quaternion-subspace.md`), for the subspace itself in the Algebra group
- *The Three Pairings of the Biquaternion Algebra* (`articles_maths/the-three-pairings-of-the-biquaternion-algebra.md`), for the three forms and the three Gram matrices
- *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), for the first pairing and its restrictions
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the second pairing and the Euclidean norm it defines
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the third pairing and the same six restrictions
- *Biquaternion Relations Between Subspaces* (`articles_maths/biquaternion-relations-between-subspaces.md`), for the six subspaces together and their intersections
- *Biquaternion Quaternion Subspace* (`articles_maths/biquaternion-quaternion-subspace.md`), the companion of the same decomposition, and *Biquaternion Square Roots of Minus One, Zero and Plus One* (`articles_maths/biquaternion-square-roots-of-minus-one-zero-and-plus-one.md`), for the root sets of the subspace
