# __The Vector Subspace under the Three Topologies__

## Introduction

The vector subspace $\mathrm{Vect}(\mathbb{B})$ is one of the six distinguished subspaces of the biquaternion algebra $\mathbb{B}$, defined and developed in *Introduction to the Six Subspaces* in the Algebra group. It reads the subspace for its basis, its defining involution, its algebra and module structure and its elements; this one reads it for its **topology**, and it does so three times.

The algebra carries three pairings of its elements — the **bilinear form** $B$, the **Hermitian form** $\langle\cdot,\cdot\rangle$ and the **Krein form** $[\cdot,\cdot]$ of *The Three Pairings of the Biquaternion Algebra*, built on the natural conjugation ${}^{\natural}$, the Hermitian conjugation ${}^{*}$ and the complex conjugation $\bar{\cdot}$. Each pairing restricts to the subspace, and each restriction is a form in its own right, with its own signature, its own definiteness, its own null set and its own group of isometries; each therefore induces its own topology on the subspace. The three are kept apart in three separate sections below, and they are compared in the table at the end.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the element $\tilde{Q}=\sum_{\mu}Q_{\mu}e_{\mu}$ with $Q_{\mu}=q_{\mu}+iq'_{\mu}$, units $e_0=1$ and $e_k^2=-e_0$, central scalar imaginary $i$, scalar part $\mathrm{Sc}$, sign vector $\varepsilon=(1,-1,-1,-1)$ and $E=\mathrm{diag}(1,-1,-1,-1)$.

## The Subspace

**Definition.** The **vector subspace** is the anti-fixed space of quaternion conjugation, $\mathrm{Vect}(\mathbb{B})=\{\tilde{Q}:\tilde{Q}^{\natural}=-\tilde{Q}\}$. It is the complex three-space $\mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\}$.

In real coordinates it is $\{q_ke_k+iq'_ke_k\}$, of real dimension $6$ and real basis $e_1,e_2,e_3,ie_1,ie_2,ie_3$. It is not a subalgebra; it is closed under the commutator and is a Lie algebra.

## The Topology Induced by the Bilinear Form

**Theorem (the restriction of the bilinear form).** On $\mathrm{Vect}(\mathbb{B})$ the bilinear form is

$$
B(\tilde{Q},\tilde{Q}) = N(\tilde{Q}) = Q_1^2+Q_2^2+Q_3^2 = \sum_k\bigl(q_k^2-(q'_k)^2\bigr) ,
$$

a real form of signature $(3,3)$ on the 6 real dimensions of the subspace.

**Proof.** On the subspace the scalar coefficient vanishes, so $N(\tilde{Q})=Q_1^2+Q_2^2+Q_3^2$; writing $Q_k=q_k+iq'_k$ gives $\sum_k(q_k^2-(q'_k)^2)$, with three positive and three negative directions.

The restriction is the split form of maximal index: three positive and three negative directions. It is symmetric between its two halves, the real vector triple $e_1,e_2,e_3$ being positive definite and the imaginary triple $ie_1,ie_2,ie_3$ negative definite, and they are mutual orthogonal complements.

**The null set.** the real isotropic cone $\sum_k(q_k^2-(q'_k)^2)=0$ of the split form, a real cone of dimension $5$ through the origin; it strictly contains the complex cone $\sum_kQ_k^2=0$, of real dimension $4$, whose non-zero points are exactly the zero divisors in the subspace, the *pure* zero divisors, which are nilpotent of index two.

**The isometry group.** The restriction is a real form of signature $(3,3)$, so its group of **real-linear** isometries on $\mathrm{Vect}(\mathbb{B})$ is the orthogonal group $O(3,3)$; inside the ambient isometry group $O_4(\mathbb{C})$ of *The Three Pairings of the Biquaternion Algebra* the elements that preserve $\mathrm{Vect}(\mathbb{B})$ form the corresponding subgroup.

## The Topology Induced by the Hermitian Form

**Theorem (the restriction of the Hermitian form).** On $\mathrm{Vect}(\mathbb{B})$ the Hermitian form is

$$
\langle\tilde{Q},\tilde{Q}\rangle = \sum_k|Q_k|^2 = \sum_k\bigl(q_k^2+(q'_k)^2\bigr) ,
$$

of signature $(6,0)$.

**Proof.** $\langle\tilde{Q},\tilde{Q}\rangle=\sum_\mu|Q_\mu|^2$ reduces to the three vector terms $|Q_k|^2$.

The restriction is the ordinary Euclidean square on the six real coordinates of the subspace, in which the real and the imaginary vector triples are orthogonal.

**The Euclidean topology.** The restriction is positive definite, so it is a Euclidean inner product on the 6 real dimensions of the subspace. It defines the Euclidean norm $\lVert\tilde{Q}\rVert_E$, the distance and the balls, and hence the Euclidean topology of the subspace; on the algebra as a whole this is the topology of *The Euclidean Topology of the Biquaternion Algebra*. Its group of **real-linear** isometries on $\mathrm{Vect}(\mathbb{B})$ is the compact orthogonal group $O(6)$, contained in the ambient unitary group $U(4)$ of *The Unitary Group of the Biquaternion Algebra*.

**The null set.** The form is positive definite, so $\langle\tilde{Q},\tilde{Q}\rangle=0$ holds only at $\tilde{Q}=0$: the subspace carries no isotropic vector for the Hermitian form.

## The Topology Induced by the Krein Form

**Theorem (the restriction of the Krein form).** On $\mathrm{Vect}(\mathbb{B})$ the Krein form is

$$
[\tilde{Q},\tilde{Q}] = -\sum_k|Q_k|^2 = -\sum_k\bigl(q_k^2+(q'_k)^2\bigr) ,
$$

of signature $(0,6)$.

**Proof.** $[\tilde{Q},\tilde{Q}]=\sum_\mu\varepsilon_\mu|Q_\mu|^2$ keeps only the three vector terms, each with the sign $\varepsilon_k=-1$.

The restriction is negative definite, the exact negative of the Hermitian restriction. The vector subspace is the maximal negative definite subspace of the Krein form, of negative index $6$, which is the full negative index of the ambient signature $(2,6)$.

**The null set.** The form is negative definite, so the origin is its only isotropic point. This contrasts sharply with the bilinear topology, where the same subspace carries a five-dimensional null cone.

**The isometry group.** The restriction is a real form of signature $(0,6)$, so its group of **real-linear** isometries on $\mathrm{Vect}(\mathbb{B})$ is $O(0,6)$; inside the ambient group $U(1,3)$ of *The Krein Isometry Group and Its $J$-Contractions* the elements preserving $\mathrm{Vect}(\mathbb{B})$ form the corresponding subgroup.

## The Three Topologies Compared

The three restrictions are collected in one table; each entry is a form on the same real vector space $\mathrm{Vect}(\mathbb{B})$, and the signatures are those of the underlying real form.

| topology | form | restriction on $\mathrm{Vect}(\mathbb{B})$ | signature | definiteness | null set | isometry group |
|---|---|---|---|---|---|---|
| bilinear | $B=\mathrm{Sc}(\tilde{Q}^{\natural}\tilde{Q})$ | $Q_1^2+Q_2^2+Q_3^2 = \sum_k\bigl(q_k^2-(q'_k)^2\bigr)$ | $(3,3)$ | indefinite (split) | $\sum_k(q_k^2-(q'_k)^2)=0$, containing $\sum_kQ_k^2=0$ | $O(3,3)$ |
| Hermitian | $\langle\tilde{Q},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{Q}^{*}\tilde{Q})$ | $\sum_k|Q_k|^2 = \sum_k\bigl(q_k^2+(q'_k)^2\bigr)$ | $(6,0)$ | positive definite | $\{0\}$ | $O(6)$ |
| Krein | $[\tilde{Q},\tilde{Q}]=\mathrm{Sc}(\bar{\tilde{Q}}\tilde{Q})$ | $-\sum_k|Q_k|^2 = -\sum_k\bigl(q_k^2+(q'_k)^2\bigr)$ | $(0,6)$ | negative definite | $\{0\}$ | $O(0,6)$ |

The three topologies are as different as they can be on one space: the bilinear form is the split form of signature $(3,3)$ whose null cone has real dimension $5$ and contains the four-dimensional complex cone of zero divisors, the Hermitian form is positive definite, and the Krein form is negative definite. The subspace is the maximal negative definite subspace of the Krein form, and at the same time the carrier of the largest null set of the bilinear form.

**Remark (real-linear and complex-linear isometries).** The groups in the table are those of the **real-linear** isometries of the underlying real form, and they exist for every subspace. On the vector subspace, which is a complex vector space, the complex-linear isometries form the smaller unitary subgroup, $O_3(\mathbb{C})$, $U(3)$ and $U(3)$, for the bilinear, the Hermitian and the Krein restriction respectively. On the four subspaces that are not complex vector spaces no complex-linear isometry group is defined, and the real-linear group is the whole of the isometry group.

## Summary

On the vector subspace the bilinear form restricts to the split form $\sum_k(q_k^2-(q'_k)^2)$ of signature $(3,3)$, with the real isotropic cone $\sum_k(q_k^2-(q'_k)^2)=0$ of real dimension $5$, containing the complex cone of zero divisors $\sum_kQ_k^2=0$ of real dimension $4$, as its null set; the Hermitian form restricts to the Euclidean square $\sum_k(q_k^2+(q'_k)^2)$ of signature $(6,0)$, positive definite; and the Krein form restricts to its negative, of signature $(0,6)$, negative definite, the maximal negative definite subspace of the ambient Krein form. The isometry groups are $O(3,3)$, $O(6)$ and $O(6)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, of real dimension $6$ |
| $B$, $\langle\cdot,\cdot\rangle$, $[\cdot,\cdot]$ | the bilinear, Hermitian and Krein forms of *The Three Pairings of the Biquaternion Algebra* |
| $(3,3)$ | the signature of the bilinear form on $\mathrm{Vect}(\mathbb{B})$ |
| $(6,0)$ | the signature of the Hermitian form on $\mathrm{Vect}(\mathbb{B})$, positive definite |
| $(0,6)$ | the signature of the Krein form on $\mathrm{Vect}(\mathbb{B})$ |
| $O(3,3)$, $O(6)$, $O(0,6)$ | the isometry groups of the three restrictions |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the subspace itself in the Algebra group
- *The Three Pairings of the Biquaternion Algebra* (`articles_maths/the-three-pairings-of-the-biquaternion-algebra.md`), for the three forms and the three Gram matrices
- *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), for the first pairing and its restrictions
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the second pairing and the Euclidean norm it defines
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the third pairing and the same six restrictions
- *Biquaternion Relations Between Subspaces* (`articles_maths/biquaternion-relations-between-subspaces.md`), for the six subspaces together and their intersections
- *Biquaternion Lie Algebras* (`articles_maths/biquaternion-lie-algebras.md`), for the Lie structure of the subspace
