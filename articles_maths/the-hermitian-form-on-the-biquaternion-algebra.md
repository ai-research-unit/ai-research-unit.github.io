# __The Hermitian Form on the Biquaternion Algebra__

## Introduction

The second scalar pairing of the biquaternion algebra is built on the **Hermitian conjugation** ${}^{*} = {}^{\natural}\circ\bar{\cdot}$, which is $\mathbb{C}$-antilinear, so that the pairing is $\mathbb{C}$-**sesquilinear** rather than bilinear. This article defines that form and the inner product it induces, and gathers the metric readings that the Algebra group does not carry.

The form and the inner product are extracted here from *Biquaternions as a Vector Space over $\mathbb{C}$*, where they stood as §*The Hermitian Form* and §*The Inner Product*. They are forms: they are built from the conjugation ${}^{*}$, they are read for length and for sign, and their home is the Topology group. The Algebra articles keep the conjugation ${}^{*}$ itself and the Hermitian subspace $\mathbb{M}_+$ as its fixed space — those are involution-theoretic and need no form to exist.

## The Hermitian Form

The **Hermitian form** of a biquaternion $\tilde{Q}$ is the biquaternion

$$
\tilde{Q} \tilde{Q}^{*},
$$

where $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$ is the Hermitian conjugate.

- $\tilde{Q} \tilde{Q}^{*}$ is a **biquaternion**, not a real scalar in general. Its **scalar part** is

$$
\mathrm{Sc}\!\left(\tilde{Q} \tilde{Q}^{*}\right) = \sum_{\mu=0}^{3} |Q_\mu|^2 = \sum_{\mu=0}^{3} \left(q_\mu^2 + (q'_\mu)^2\right),
$$

with $Q_\mu = q_\mu + i q'_\mu$. This scalar part is non-negative and vanishes if and only if $\tilde{Q} = 0$. The vector part of $\tilde{Q} \tilde{Q}^{*}$ does not in general vanish: for example, for $\tilde{Q} = e_0 + ie_1$, one has $\tilde{Q}^{*} = e_0 + ie_1$ and

$$
\tilde{Q} \tilde{Q}^{*} = (e_0 + ie_1)^2 = 2e_0 + 2ie_1,
$$

which has a nonzero vector part $2ie_1$.

- The Hermitian form is **not** multiplicative with respect to the biquaternion product, and its scalar part does not in general equal the biquaternion norm $N(\tilde{Q}) = \sum_\mu Q_\mu^2$.
- The Hermitian form is **Hermitian** in the sense that $(\tilde{Q} \tilde{Q}^{*})^{\dagger} = \tilde{Q} \tilde{Q}^{*}$: the Hermitian form of any biquaternion is a Hermitian element of $\mathbb{B}$, that is, an element of $\mathbb{M}_+$.

## The Inner Product

The **inner product** of two biquaternions is the complex scalar

$$
\langle \tilde{P}, \tilde{Q} \rangle = \sum_{\mu=0}^{3} P_{\bar{\mu}} Q_\mu
= \sum_{\mu=0}^{3} \left(p_\mu q_\mu + p'_\mu q'_\mu\right) + i \sum_{\mu=0}^{3} \left(p_\mu q'_\mu - p'_\mu q_\mu\right),
$$

with $Q_\mu = q_\mu + i q'_\mu$. It is **sesquilinear**, linear in the second argument and conjugate-linear in the first,

$$
\langle \lambda \tilde{P}, \tilde{Q} \rangle = \bar{\lambda} \langle \tilde{P}, \tilde{Q} \rangle, \qquad
\langle \tilde{P}, \lambda \tilde{Q} \rangle = \lambda \langle \tilde{P}, \tilde{Q} \rangle, \qquad \lambda \in \mathbb{C},
$$

and **Hermitian**, $\langle \tilde{P}, \tilde{Q} \rangle^* = \langle \tilde{Q}, \tilde{P} \rangle$. It is **non-degenerate**: if $\langle \tilde{P}, \tilde{Q} \rangle = 0$ for every $\tilde{Q}$, then $\tilde{P} = 0$, since testing against the units gives $P_{\bar{\mu}} = 0$.

The inner product pairs the algebra with its conjugate and is complex-valued in general. Its diagonal value

$$
\langle \tilde{Q}, \tilde{Q} \rangle = \sum_{\mu=0}^{3} |Q_\mu|^2 = \mathrm{Sc}\!\left(\tilde{Q} \tilde{Q}^{*}\right)
$$

is the scalar part of the Hermitian form and vanishes only at $\tilde{Q} = 0$.

## The Euclidean Structure

The diagonal of the inner product is a positive definite real quadratic form on $\mathbb{B} \cong \mathbb{R}^8$, and it defines the **Euclidean norm**

$$
\|\tilde{Q}\|_E = \sqrt{\mathrm{Sc}\!\left(\tilde{Q} \tilde{Q}^{*}\right)} = \sqrt{\sum_{\mu=0}^{3} |Q_\mu|^2}.
$$

It is a genuine norm: positive definite, subadditive, homogeneous of degree one, and **not** multiplicative with respect to the biquaternion product. The Hermitian form therefore equips the algebra with its Hilbert-space structure, and it is this form, not the bilinear one, that the topological statements about $\mathbb{B}$ use.

Three consequences are read from it and are developed in their own articles.

- **The positive definiteness of the quaternion subspace.** On $\mathbb{H}_{\mathbb{B}}$ the norm $N$ is the sum of four real squares, hence positive definite, whereas on $i\mathbb{H}_{\mathbb{B}}$ it is the negative of such a sum; the pair is the real-and-imaginary coefficient splitting of the algebra. The positivity is the content that the Algebra article *Introduction to the Six Subspaces* now records only as the algebraic fact that every non-zero element is a unit.
- **The Euclidean topology.** The linear isometry onto $\mathbb{R}^8$, the contractibility of $\mathbb{B}$ and the Euclidean unit sphere $S^7$ are *The Euclidean Topology of the Biquaternion Algebra*.
- **The unitary group.** The maximal compact subgroup $U(2)$ of the unit group, onto which $\mathbb{B}^\times$ retracts, is *The Unitary Group of the Biquaternion Algebra*.

The comparison of this form with the bilinear one is the table of *Biquaternion Norm and Invertibility*, §*Relation Between the Biquaternion Norm and the Hermitian Form*: the two coincide exactly on the quaternion subspace, and on the anti-quaternion subspace they differ by a sign.

## Summary

The Hermitian form of the biquaternion algebra is $\tilde{Q}\tilde{Q}^{*}$, built on the antilinear conjugation ${}^{*}$; its scalar part is $\sum_\mu |Q_\mu|^2$, non-negative and vanishing only at the origin, and its vector part need not vanish. It induces the sesquilinear **inner product** $\langle \tilde{P},\tilde{Q}\rangle = \sum_\mu P_{\bar\mu}Q_\mu$, conjugate-linear in the first argument, Hermitian and non-degenerate. The diagonal of the inner product is a positive definite real form on $\mathbb{B}\cong\mathbb{R}^8$, and it defines the Euclidean norm, hence the Hilbert-space and topological structure of the algebra. Positive definiteness is carried by the quaternion subspace and its negative by the anti-quaternion subspace. This article holds the form and the inner product that *Biquaternions as a Vector Space over $\mathbb{C}$* formerly carried as §*The Hermitian Form* and §*The Inner Product*; the sesquilinear companion of the bilinear form is *The Bilinear Form on the Biquaternion Algebra*, and the indefinite variant is *The Biquaternion Krein Form and Its Signature*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{Q} \tilde{Q}^{*}$ | The Hermitian form; a Hermitian biquaternion |
| $\mathrm{Sc}(\tilde{Q} \tilde{Q}^{*}) = \sum_\mu \lvert Q_\mu\rvert^2$ | Scalar part of the Hermitian form; positive definite |
| $\langle \tilde{P}, \tilde{Q} \rangle = \sum_\mu P_{\bar\mu} Q_\mu$ | The inner product; a complex scalar, sesquilinear and non-degenerate |
| $\|\tilde{Q}\|_E = \sqrt{\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*})}$ | The Euclidean norm |

## Further Reading

- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the Euclidean norm, the real forms and the comparison of the two forms
- *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), for the $\mathbb{C}$-bilinear companion
- *Biquaternions as a Vector Space over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-vector-space-over-c.md`), for the conjugation ${}^{*}$ and the Hermitian subspace $\mathbb{M}_+$
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the topology this form induces
- *The Unitary Group of the Biquaternion Algebra* (`articles_maths/the-unitary-group-of-the-biquaternion-algebra.md`), for the compact group this form singles out
