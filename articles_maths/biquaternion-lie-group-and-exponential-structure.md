# __Biquaternion Lie Group and Exponential Structure__

## Introduction

The group of units $\mathbb{B}^\times$ is a real Lie group, and its exponential map is the bridge between the group and the Lie algebra *Biquaternion Lie Algebra*. This article reads the Lie-group structure: the exponential and its parametrisation of the group, the cases of the exponential, the group law, the failure of surjectivity, and the real forms and subgroups the group carries.

The exponential itself — its series, its closed form, the logarithm and the power functions — is computed in *Biquaternion Elementary Functions*, and only its group-theoretic consequences are used here; the Lie algebra is in Algebra, and the topology of the group is in *The Biquaternion Unit Group as a Topological Group*. 

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The biquaternion norm is $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\sum_\mu Q_\mu^2$, and $\tilde{Q}$ is a unit exactly when $N(\tilde{Q})\neq0$ (*Biquaternion Norm and Invertibility*). Throughout, a biquaternion is written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^3 Q_k e_k$.

---

## The Unit Quaternions and Their Complexification

The **unit quaternions** are the elements of $\mathbb{H}_{\mathbb{B}}$ of norm $1$:

$$
S^3 = \{q \in \mathbb{H}_{\mathbb{B}} : N(q) = 1\},
$$

a compact, connected, simply connected real Lie group of real dimension $3$. Every such $q$ is $\cos\theta\, e_0 + \sin\theta\, \hat{n}$ with $\hat{n}$ a real unit vector part, the quaternion exponential.

Complexifying the coefficients turns $N(q) = 1$ into the same equation over $\mathbb{C}$, giving the **unit-norm subgroup**

$$
\mathbb{B}^\times_1 = \{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) = 1\},
$$

whose elements need not be real quaternions.

**Dimension.** The level set $N = 1$ has complex dimension $3$ and real dimension $6$, the biquaternion norm being a submersion wherever $N(\tilde{Q}) \neq 0$. The group $\mathbb{B}^\times_1$ is connected, simply connected, and non-compact, and it is the **complexification of the unit quaternions**: the trace-free subalgebra satisfies $\mathrm{B}_0 = \mathrm{K} \otimes_{\mathbb{R}} \mathbb{C}$ for the compact subalgebra $\mathrm{K}$ below, and $\mathbb{B}^\times_1$ complexifies the compact group $S^3$. Its center is

$$
Z(\mathbb{B}^\times_1) = \{\pm e_0\} \cong \mathbb{Z}/2.
$$

## The Subgroups and the Real Forms

The relevant subgroups are: $\mathbb{B}^\times$, the nonzero-norm elements (complex dimension $4$, real dimension $8$); $\mathbb{B}^\times_1$, the unit-norm elements (complex dimension $3$, real dimension $6$); the unit quaternions $S^3$ (real dimension $3$); and the center $\mathbb{C}^\times e_0$ of nonzero scalars (complex dimension $1$, real dimension $2$).

$S^3$ is the maximal compact subgroup of $\mathbb{B}^\times_1$, with Lie algebra the compact subalgebra $\mathrm{K}$ of *Biquaternion Lie Algebra*, §*The Trace-Free Subalgebra*. The center $\{\pm e_0\}$ is discrete, so the quotient $\mathbb{B}^\times_1/\{\pm e_0\}$ is a Lie group of real dimension $6$.

## The Unitary Subgroup and the Defining Module

The algebra acts on the defining module $\mathbb{C}^2$ by the defining representation, in which a biquaternion acts as its $2\times2$ matrix $\Phi(\tilde{Q})$ (*Biquaternion 2×2 Matrix Element Representation*). The elements that preserve the standard Hermitian form of $\mathbb{C}^2$ are exactly those with $\tilde{Q}^{\dagger}\tilde{Q}=e_0$, and they form a compact subgroup of the group of units,
$$
U(2)=\{\tilde{Q}\in\mathbb{B}^{\times}:\tilde{Q}^{\dagger}\tilde{Q}=e_0\},
$$
of real dimension $4$. The determinant-one elements inside it are the unit quaternions:
$$
U(2)\cap SL(2,\mathbb{C})=S^3=SU(2),
$$
consistently with the unit quaternions being the unitary part of the norm-one group. Every element of $U(2)$ is the product of a unit quaternion and a unit complex scalar, and the two factors meet in $\{\pm e_0\}$:
$$
U(2)=S^3\cdot U(1)\cong (SU(2)\times U(1))/\{\pm(1,1)\}.
$$

**Proof.** If $\tilde{Q}\in U(2)$ then $|\det\Phi(\tilde{Q})|=1$, so $P=\tilde{Q}\,(\det\Phi(\tilde{Q}))^{-1/2}\in U(2)$ has determinant one, hence lies in $S^3$ by the identification of the determinant-one unitary elements with the unit quaternions; the scalar $(\det\Phi(\tilde{Q}))^{1/2}$ is a unit complex number. The intersection $\{\pm e_0\}$ is the set of scalars $\lambda e_0$ of determinant $\lambda^2=1$, and the kernel of $S^3\times U(1)\to U(2)$, $(q,\lambda)\mapsto\lambda q$, is $\{\pm(1,1)\}$.

**Remark.** The norm-one group $\mathbb{B}^{\times}_1\cong SL(2,\mathbb{C})$ is strictly larger: it acts on the defining module too, but it does not preserve the Hermitian form, and unlike $U(2)$ it is non-compact.

## Surjectivity and Its Failure for the Subgroups

The exponential of the full unit group is surjective (*Biquaternion Elementary Functions*, §*The Logarithm*), but the two distinguished subgroups behave differently.

**The compact subgroup: surjective.** Every unit quaternion is $\cos\theta\, e_0 + \sin\theta\,\hat{n} = \exp(\theta\hat{n})$, so $\exp : \mathrm{K} \to S^3$ is surjective; this is the general fact that a connected compact Lie group has a surjective exponential map.

**The full group: not surjective.** The exponential $\exp : \mathrm{B}_0 \to \mathbb{B}^\times_1$ is **not** surjective: $\mathbb{B}^\times_1$ is not exponential. The element of $\mathbb{B}^\times_1$ with scalar part $-1$ and non-semi-simple behaviour, corresponding to the non-diagonalizable norm-one element with the repeated eigenvalue $-1$, is

$$
\tilde{Q} = -e_0 + \frac{i}{2}e_1 - \frac{1}{2}e_2, \qquad N(\tilde{Q}) = 1 + \left(\frac{i}{2}\right)^2 + \left(-\frac{1}{2}\right)^2 = 1.
$$

Its scalar part is $Q_0 = -1$ and its vector part has $B = 0$, so the element is non-semi-simple with the repeated eigenvalue $-1$. If $\tilde{Q} = \exp(\tilde{R})$ with $\tilde{R} \in \mathrm{B}_0$, then $R_0 = 0$, and $\tilde{R} = \mu e_0 + \tilde{N}$ with $\tilde{N}$ nilpotent and $e^\mu = -1$, hence $\mu \in i\pi(2\mathbb{Z}+1)$ and $\mathrm{Tr}(\tilde{R}) = 2\mu \neq 0$, a contradiction. The same obstruction makes $\exp$ non-surjective on the real group $SL(2,\mathbb{R})$.

**Generation versus surjectivity.** Failure of surjectivity does not mean the exponentials fail to generate: since $\mathbb{B}^\times_1$ is connected and $\exp$ is a local diffeomorphism at $0$, the image $\exp(\mathrm{B}_0)$ contains a neighbourhood of the identity and generates the group, while remaining a proper subset. Nor does simple connectivity force surjectivity: $\mathbb{B}^\times_1$ is simply connected, yet $\exp$ is not onto. The classical criteria (connected compact, connected nilpotent, or $GL(n,\mathbb{C})$) are sufficient, not necessary.

---

The group of units is an open subset of $\mathbb{B}$, hence a smooth real manifold of dimension $8$, but its topology is far from that of a general open set in $\mathbb{R}^8$: it has the homotopy type of a compact group. The polar decomposition exhibits the maximal compact subgroup as a strong deformation retract, and with it determines the homotopy groups and the universal cover. Everything in this part is a statement about $\mathbb{B}^\times$ as a topological group; the topology of the ambient space and of the null cone is in *Biquaternion Topology*.

## The Correspondence with the Lie Algebra

The exponential is the correspondence between the group and the algebra. Its differential at the identity is the identity, so it is a local diffeomorphism onto a neighbourhood of $e_0$, and the inverse function theorem makes it a chart of $\mathbb{B}^\times$ near the identity; the tangent space at the identity is the whole algebra, since $\mathbb{B}^\times$ is open, with the commutator as bracket (*Biquaternion Lie Algebra*). The Baker–Campbell–Hausdorff series of the algebra converges near the origin and reproduces the group law there, and the group law $\exp(\tilde A)\exp(\tilde C)$ against $\exp(\tilde A+\tilde C)$ of *Biquaternion Elementary Functions* is its first two terms. The subgroups correspond to the subalgebras: the compact subalgebra $\mathrm{K}=\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ to $S^3$, the trace-free part $\mathrm{B}_0$ to the norm-one group $\mathbb{B}^\times_1$, and the centre $\mathbb{C}e_0$ to $\mathbb{C}^\times e_0$.

## Summary

The group of units $\mathbb{B}^\times$ is a real Lie group of real dimension $8$, and the exponential map is its link with the Lie algebra: it is a local diffeomorphism at the identity, but it is not surjective onto the group. The unit quaternions $S^3=\{q\in\mathbb{H}_{\mathbb{B}}:N(q)=1\}$ form a compact connected simply connected subgroup of real dimension $3$, whose complexification is the norm-one group $\mathbb{B}^\times_1$ of real dimension $6$ and centre $\{\pm e_0\}$.

The subgroups are $\mathbb{B}^\times$, $\mathbb{B}^\times_1$, the unit quaternions $S^3$ and the centre $\mathbb{C}^\times e_0$; the maximal compact subgroup of $\mathbb{B}^\times_1$ is $S^3$, and the quotient by the centre $\mathbb{B}^\times_1/\{\pm e_0\}$ is a Lie group of real dimension $6$. Over the reals these are the real forms of the group, and the correspondence with the Lie algebra attaches each subgroup to its subalgebra: $S^3$ to $\mathrm{K}$, $\mathbb{B}^\times_1$ to $\mathrm{B}_0$, and $\mathbb{C}^\times e_0$ to the centre.

Surjectivity is not uniform. The exponential is surjective onto $S^3$, a connected compact group, and not surjective onto $\mathbb{B}^\times_1$: the norm-one group is not exponential, the obstruction a non-semi-simple element with the repeated eigenvalue $-1$, and the same obstruction occurs in $SL(2,\mathbb{R})$. The image still contains a neighbourhood of the identity and generates the connected group, so failure of surjectivity is not failure of generation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}^\times$ | Group of units; real Lie group of real dimension $8$ |
| $\exp$ | Exponential map; closed form in *Biquaternion Elementary Functions* |
| $S^3=\{q\in\mathbb{H}_{\mathbb{B}}:N(q)=1\}$ | Unit quaternions; compact subgroup of real dimension $3$ |
| $\mathbb{B}^\times_1=\{N=1\}$ | Norm-one group; complexification of $S^3$; real dimension $6$ |
| $\{\pm e_0\}$ | Centre of $\mathbb{B}^\times_1$; the quotient is a Lie group of real dimension $6$ |
| $\mathrm{B}_0$ | Lie algebra of $\mathbb{B}^\times_1$; trace-free part |
| $\mathrm{K}=\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ | Lie algebra of $S^3$; compact subalgebra |
| $\mathbb{C}^\times e_0$ | Centre of $\mathbb{B}^\times$; Lie algebra $\mathbb{C}e_0$ |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed. 2015).
- John Stillwell, *Naive Lie Theory* (Springer, 2008).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997).
