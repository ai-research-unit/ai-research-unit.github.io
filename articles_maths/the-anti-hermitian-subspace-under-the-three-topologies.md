# __The Anti-Hermitian Subspace under the Three Topologies__

## Introduction

The anti-Hermitian subspace $\mathbb{M}_-$ is one of the six distinguished subspaces of the biquaternion algebra $\mathbb{B}$, defined and developed in *Introduction to the Six Subspaces* in the Algebra group. It reads the subspace for its basis, its defining involution, its algebra and module structure and its elements; this one reads it for its **topology**, and it does so three times.

The algebra carries three pairings of its elements — the **bilinear form** $B$, the **Hermitian form** $\langle\cdot,\cdot\rangle$ and the **Krein form** $[\cdot,\cdot]$ of *The Three Pairings of the Biquaternion Algebra*, built on the natural conjugation ${}^{\natural}$, the Hermitian conjugation ${}^{*}$ and the complex conjugation $\bar{\cdot}$. Each pairing restricts to the subspace, and each restriction is a form in its own right, with its own signature, its own definiteness, its own null set and its own group of isometries; each therefore induces its own topology on the subspace. The three are kept apart in three separate sections below, and they are compared in the table at the end.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the element $\tilde{Q}=\sum_{\mu}Q_{\mu}e_{\mu}$ with $Q_{\mu}=q_{\mu}+iq'_{\mu}$, units $e_0=1$ and $e_k^2=-e_0$, central scalar imaginary $i$, scalar part $\mathrm{Sc}$, sign vector $\varepsilon=(1,-1,-1,-1)$ and $E=\mathrm{diag}(1,-1,-1,-1)$.

## The Subspace

**Definition.** The **anti-Hermitian subspace** is the anti-fixed space of Hermitian conjugation, equivalently the fixed space of the reversal $\flat$, $\mathbb{M}_-=\{\tilde{Q}:\tilde{Q}^{*}=-\tilde{Q}\}$. It is the set of elements with imaginary scalar part and real vector part.

It is $\mathrm{span}_{\mathbb{R}}\{ie_0,e_1,e_2,e_3\}$, of real dimension $4$; it is not a subalgebra, and it is a Lie algebra for the commutator.

## The Topology Induced by the Bilinear Form

**Theorem (the restriction of the bilinear form).** On $\mathbb{M}_-$ the bilinear form is

$$
B(\tilde{Q},\tilde{Q}) = N(\tilde{Q}) = (q_1^2+q_2^2+q_3^2)-(q'_0)^2 ,
$$

a real form of signature $(3,1)$ on the 4 real dimensions of the subspace.

**Proof.** On the subspace $Q_0=iq'_0$ and $Q_k=q_k$, so $N(\tilde{Q})=(q_1^2+q_2^2+q_3^2)-(q'_0)^2$, three positive and one negative direction.

The restriction is the negative of the Hermitian restriction, of signature $(3,1)$ rather than $(1,3)$; the two sectors are exchanged by multiplication by $i$.

**The null set.** the cone $\sum_kq_k^2=(q'_0)^2$, of real dimension $3$, the zero divisors of the subspace, none of which is nilpotent.

**The isometry group.** The restriction is a real form of signature $(3,1)$, so its group of **real-linear** isometries on $\mathbb{M}_-$ is the orthogonal group $O(3,1)$; inside the ambient isometry group $O_4(\mathbb{C})$ of *The Three Pairings of the Biquaternion Algebra* the elements that preserve $\mathbb{M}_-$ form the corresponding subgroup.

## The Topology Induced by the Hermitian Form

**Theorem (the restriction of the Hermitian form).** On $\mathbb{M}_-$ the Hermitian form is

$$
\langle\tilde{Q},\tilde{Q}\rangle = (q'_0)^2+q_1^2+q_2^2+q_3^2 ,
$$

of signature $(4,0)$.

**Proof.** $\langle\tilde{Q},\tilde{Q}\rangle=\sum_\mu|Q_\mu|^2=|iq'_0|^2+\sum_kq_k^2$.

The restriction is the Euclidean square on the four real coordinates, positive definite, exactly as on the Hermitian sector.

**The Euclidean topology.** The restriction is positive definite, so it is a Euclidean inner product on the 4 real dimensions of the subspace. It defines the Euclidean norm $\lVert\tilde{Q}\rVert_E$, the distance and the balls, and hence the Euclidean topology of the subspace; on the algebra as a whole this is the topology of *The Euclidean Topology of the Biquaternion Algebra*. Its group of **real-linear** isometries on $\mathbb{M}_-$ is the compact orthogonal group $O(4)$, contained in the ambient unitary group $U(4)$ of *The Unitary Group of the Biquaternion Algebra*.

**The null set.** The form is positive definite, so $\langle\tilde{Q},\tilde{Q}\rangle=0$ holds only at $\tilde{Q}=0$: the subspace carries no isotropic vector for the Hermitian form.

## The Topology Induced by the Krein Form

**Theorem (the restriction of the Krein form).** On $\mathbb{M}_-$ the Krein form is

$$
[\tilde{Q},\tilde{Q}] = (q'_0)^2-q_1^2-q_2^2-q_3^2 ,
$$

of signature $(1,3)$.

**Proof.** $[\tilde{Q},\tilde{Q}]=\sum_\mu\varepsilon_\mu|Q_\mu|^2=(q'_0)^2-\sum_kq_k^2$, the signs $\varepsilon_k=-1$ falling on the real vector directions.

The Krein restriction is the negative of the bilinear restriction, of signature $(1,3)$ rather than $(3,1)$; the passage between them is again the sign vector $\varepsilon$.

**The null set.** the cone $(q'_0)^2=\sum_kq_k^2$, of real dimension $3$, the light cone of the Lorentzian form on the subspace.

**The isometry group.** The restriction is a real form of signature $(1,3)$, so its group of **real-linear** isometries on $\mathbb{M}_-$ is $O(1,3)$; inside the ambient group $U(1,3)$ of *The Krein Isometry Group and Its $J$-Contractions* the elements preserving $\mathbb{M}_-$ form the corresponding subgroup.

## The Three Topologies Compared

The three restrictions are collected in one table; each entry is a form on the same real vector space $\mathbb{M}_-$, and the signatures are those of the underlying real form.

| topology | form | restriction on $\mathbb{M}_-$ | signature | definiteness | null set | isometry group |
|---|---|---|---|---|---|---|
| bilinear | $B=\mathrm{Sc}(\tilde{Q}^{\natural}\tilde{Q})$ | $(q_1^2+q_2^2+q_3^2)-(q'_0)^2$ | $(3,1)$ | indefinite (Lorentzian) | $\sum_kq_k^2=(q'_0)^2$ | $O(3,1)$ |
| Hermitian | $\langle\tilde{Q},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{Q}^{*}\tilde{Q})$ | $(q'_0)^2+q_1^2+q_2^2+q_3^2$ | $(4,0)$ | positive definite | $\{0\}$ | $O(4)$ |
| Krein | $[\tilde{Q},\tilde{Q}]=\mathrm{Sc}(\bar{\tilde{Q}}\tilde{Q})$ | $(q'_0)^2-q_1^2-q_2^2-q_3^2$ | $(1,3)$ | indefinite (Lorentzian) | $(q'_0)^2=\sum_kq_k^2$ | $O(1,3)$ |

The two indefinite topologies are negatives of one another — signatures $(3,1)$ for the bilinear form and $(1,3)$ for the Krein form — and the Hermitian topology is positive definite. The subspace is the negative counterpart of the Hermitian sector in all three topologies at once.

## Summary

On the anti-Hermitian subspace the bilinear form restricts to $\sum_kq_k^2-(q'_0)^2$ of signature $(3,1)$, with the cone $\sum_kq_k^2=(q'_0)^2$ as null set; the Hermitian form to the Euclidean square $(q'_0)^2+\sum_kq_k^2$ of signature $(4,0)$, positive definite; and the Krein form to $(q'_0)^2-\sum_kq_k^2$ of signature $(1,3)$, the negative of the bilinear restriction. The isometry groups are $O(3,1)$, $O(4)$ and $O(1,3)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{M}_-$ | the anti-Hermitian subspace, of real dimension $4$ |
| $B$, $\langle\cdot,\cdot\rangle$, $[\cdot,\cdot]$ | the bilinear, Hermitian and Krein forms of *The Three Pairings of the Biquaternion Algebra* |
| $(3,1)$ | the signature of the bilinear form on $\mathbb{M}_-$ |
| $(4,0)$ | the signature of the Hermitian form on $\mathbb{M}_-$, positive definite |
| $(1,3)$ | the signature of the Krein form on $\mathbb{M}_-$ |
| $O(3,1)$, $O(4)$, $O(1,3)$ | the isometry groups of the three restrictions |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the subspace itself in the Algebra group
- *The Three Pairings of the Biquaternion Algebra* (`articles_maths/the-three-pairings-of-the-biquaternion-algebra.md`), for the three forms and the three Gram matrices
- *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), for the first pairing and its restrictions
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the second pairing and the Euclidean norm it defines
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the third pairing and the same six restrictions
- *Biquaternion Relations Between Subspaces* (`articles_maths/biquaternion-relations-between-subspaces.md`), for the six subspaces together and their intersections
- *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra* (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-biquaternion-algebra.md`), for the operators attached to the third topology
