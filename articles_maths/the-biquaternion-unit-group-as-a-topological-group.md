# __The Biquaternion Unit Group as a Topological Group__

## Introduction

The group of units $\mathbb{B}^\times$ of the biquaternion algebra is an open subset of the algebra, hence a manifold, and it carries both a group structure and the topology of that manifold. This article reads the two together: the units as the complement of the null cone, the norm-one group and its subgroups. The polar decomposition, the retractions onto the compact subgroups and the homotopy groups, generators and universal cover that follow are read on the Hermitian form and are *The Unitary Group of the Biquaternion Algebra*.

The article is one of the three the boundary draws out of the former joint treatment of the Lie theory: the Lie algebra is *Biquaternion Lie Algebras* in Algebra, the Lie-group theory and the exponential are *Biquaternion Lie Group and Exponential Structure* in Analysis, and this article owns the algebraic group of units. The topology of the group, read on the Hermitian form, is *The Unitary Group of the Biquaternion Algebra*; the Euclidean ambient space is *The Euclidean Topology of the Biquaternion Algebra*; the null cone is *Biquaternion Topology*; and the norm and invertibility criterion are *Biquaternion Norm and Invertibility*.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The biquaternion norm is $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$, and $\tilde{Q}$ is a unit exactly when $N(\tilde{Q})\neq0$ (*Biquaternion Norm and Invertibility*). Throughout, a biquaternion is written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^3 Q_k e_k$.

---

## The Group of Units

The **group of units** of $\mathbb{B}$ is the set of invertible elements,

$$
\mathbb{B}^\times = \{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) \neq 0\},
$$

a group under multiplication with identity $e_0$.

**Dimension.** $\mathbb{B}^\times$ has complex dimension $4$ and real dimension $8$; the units are exactly the elements of nonzero norm.

The group $\mathbb{B}^\times$ is open (it is $N^{-1}(\mathbb{C}\setminus\{0\})$) and dense, its complement being the null cone, of real dimension $6$ (*Biquaternion Topology*); it is connected but not compact, and its center is $Z(\mathbb{B}^\times) = \mathbb{C}^\times e_0 \cong \mathbb{C}^\times$, a closed subgroup of real dimension $2$. Its Lie theory — the Lie algebra $\mathbb{B}$ with the commutator bracket, and the map induced on the algebra by the inverse — is *Biquaternion Lie Algebras* and *Biquaternion Lie Group and Exponential Structure*, and is not developed here.

**The norm-one group.** Because $N$ is multiplicative and $N(e_0)=1$, the level set

$$
\mathbb{B}^\times_1=\{\tilde{Q}\in\mathbb{B}:N(\tilde{Q})=1\}
$$

is a closed subgroup of $\mathbb{B}^\times$ of real dimension $6$, the **norm-one group**. It is noncompact, and it deformation retracts onto the unit quaternions $S^3$ (*The Unitary Group of the Biquaternion Algebra*); hence it is simply connected, of the homotopy type of $S^3$, with $\pi_3\cong\mathbb{Z}$. Its subgroups — the unit quaternions $S^3$ and the center $\{\pm e_0\}$ — are the subject of *Biquaternion Lie Group and Exponential Structure*, §*The Subgroups and the Real Forms*.

**Two unit spheres.** There are two candidate "unit spheres" in $\mathbb{B}$, and only one of them is a group. The Euclidean sphere $\|\tilde{Q}\|_E=1$ is a genuine sphere $S^7$ but is not a group, since $\|\cdot\|_E$ is not multiplicative and it contains zero divisors (*The Euclidean Topology of the Biquaternion Algebra*, §*The Euclidean Unit Sphere*). The level set $N(\tilde{Q})=1$ is a group but is neither Euclidean nor compact. The condition that makes a level set of a form on $\mathbb{B}$ a subgroup is $N=1$, not $\|\tilde{Q}\|_E=1$.

The group of units is an open subset of $\mathbb{B}$, hence a manifold of real dimension $8$, and its topology is far from that of a general open set in $\mathbb{R}^8$: it has the homotopy type of a compact group. That topology is read through the *Hermitian* form — the polar decomposition, the retractions onto the compact subgroups and the homotopy groups — and is *The Unitary Group of the Biquaternion Algebra*; the ambient space and the null cone are *Biquaternion Topology*, and what this article owns is the algebraic group of units itself.

## The Topology of the Group

The topology of $\mathbb{B}^\times$ is read through the Hermitian form. The polar decomposition $\tilde{A}=\tilde{U}\tilde{P}$ with $\tilde{U}$ unitary and $\tilde{P}=(\tilde{A}^{*}\tilde{A})^{1/2}$ Hermitian positive definite gives a strong deformation retraction of $\mathbb{B}^\times$ onto the maximal compact subgroup $U(\mathbb{B})=\{\tilde{Q}^{*}\tilde{Q}=e_0\}\cong U(2)$, and a second retraction takes the norm-one group $\mathbb{B}^\times_1$ onto the unit quaternions $S^3$. The structure of $U(\mathbb{B})=S^1\cdot S^3\cong S^1\times S^3$, the retractions, the homotopy groups, the generators and the universal cover are in *The Unitary Group of the Biquaternion Algebra*; the results are collected here for the algebraic group.

$$
\mathbb{B}^\times\simeq U(\mathbb{B})\simeq S^1\times S^3,\qquad
\mathbb{B}^\times_1\simeq S^3,\qquad
\pi_1(\mathbb{B}^\times)\cong\mathbb{Z},\quad \pi_2(\mathbb{B}^\times)=0,\quad \pi_3(\mathbb{B}^\times)\cong\mathbb{Z},\qquad
\widetilde{\mathbb{B}^\times}\cong\mathbb{R}\times S^3 .
$$

**Remark (why the dagger enters).** Every statement above uses the Hermitian form, through the dagger and the positive definite square root. The bilinear norm $N$ alone defines the group, $\mathbb{B}^\times=\{N\neq0\}$, but not its topology: $N$ is complex-valued and indefinite, and the level set $N=1$ is a group that is not compact. The corpus therefore keeps the algebraic group of units here, at the bilinear layer, and places its topology in the Hermitian layer.

## Summary

The group of units $\mathbb{B}^\times=\{N\neq0\}$ is the complement of the null cone in $\mathbb{B}$: open and dense, connected and non-compact, of real dimension $8$, with centre $\mathbb{C}^\times e_0\cong\mathbb{C}^\times$. The norm-one group $\mathbb{B}^\times_1=\{N=1\}$ is a closed subgroup of real dimension $6$, non-compact, with the unit quaternions $S^3$ and the centre $\{\pm e_0\}$ among its subgroups. The two spherical level sets of the algebra are the Euclidean sphere $\|\tilde{Q}\|_E=1$, which is a genuine $S^7$ but not a group and contains zero divisors, and the algebraic level set $N=1$, which is a group; only the second is a subgroup of $\mathbb{B}^\times$. The topology of the group — the polar decomposition, the retractions onto $U(\mathbb{B})\cong U(2)$ and onto $S^3$, the homotopy groups, the generators and the universal cover $\mathbb{R}\times S^3$ — is read through the Hermitian form and is *The Unitary Group of the Biquaternion Algebra*. This article owns the algebraic group of units and its norm-one subgroup, which is the bilinear face of the same group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}^\times=\{N\neq0\}$ | Group of units; open dense, complement of the null cone; real dimension $8$ |
| $\mathbb{B}^\times_1=\{N=1\}$ | Norm-one group; closed subgroup of real dimension $6$ |
| $\mathbb{C}^\times e_0$ | Centre of $\mathbb{B}^\times$; nonzero complex scalars |
| $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm; multiplicative, complex-valued |
| $S^3$ (unit quaternions) | Subgroup of $\mathbb{B}^\times_1$; its maximal compact part |
| $U(\mathbb{B})=\{\tilde{Q}^{*}\tilde{Q}=e_0\}$ | Maximal compact subgroup; topology in *The Unitary Group of the Biquaternion Algebra* |
| $\mathbb{B}^\times\simeq S^1\times S^3$ | Homotopy type; proved in *The Unitary Group of the Biquaternion Algebra* |

## Further Reading

- *The Unitary Group of the Biquaternion Algebra* (`articles_maths/the-unitary-group-of-the-biquaternion-algebra.md`), for the polar decomposition, the retractions, the homotopy groups and the universal cover, all read on the Hermitian form.
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the Euclidean sphere and the contractibility of the ambient space.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed. 2015).
- John Stillwell, *Naive Lie Theory* (Springer, 2008).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997).
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636.
