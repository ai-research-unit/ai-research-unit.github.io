# __The Biquaternion Unit Group as a Topological Group__

## Introduction

The group of units $\mathbb{B}^\times$ of the biquaternion algebra is an open subset of the algebra, hence a manifold, and it carries both a group structure and the topology of that manifold. This article reads the two together: the units as the complement of the null cone, the polar decomposition, the retraction of the group onto its maximal compact subgroup, and the homotopy groups, generators and universal cover that follow.

The article is one of the three the boundary draws out of the former joint treatment of the Lie theory: the Lie algebra is *Biquaternion Lie Algebra* in Algebra, the Lie-group theory and the exponential are *Biquaternion Lie Group and Exponential Structure* in Analysis, and the topology of the group is here. The ambient topology and the null cone are in *Biquaternion Topology*, and the norm and invertibility criterion are in *Biquaternion Norm and Invertibility*.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The biquaternion norm is $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\sum_\mu Q_\mu^2$, and $\tilde{Q}$ is a unit exactly when $N(\tilde{Q})\neq0$ (*Biquaternion Norm and Invertibility*). Throughout, a biquaternion is written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^3 Q_k e_k$.

---

## The Group of Units

The **group of units** of $\mathbb{B}$ is the set of invertible elements,

$$
\mathbb{B}^\times = \{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) \neq 0\},
$$

a group under multiplication with identity $e_0$.

**Dimension.** $\mathbb{B}^\times$ has complex dimension $4$ and real dimension $8$; the units are exactly the elements of nonzero norm.

The group $\mathbb{B}^\times$ is open (it is $N^{-1}(\mathbb{C}\setminus\{0\})$) and dense, its complement being the null cone, of real dimension $6$ (*Biquaternion Topology*); it is connected but not compact, and its center is $Z(\mathbb{B}^\times) = \mathbb{C}^\times e_0 \cong \mathbb{C}^\times$, a closed subgroup of real dimension $2$. Its Lie theory — the Lie algebra $\mathbb{B}$ with the commutator bracket, and the map induced on the algebra by the inverse — is *Biquaternion Lie Algebra* and *Biquaternion Lie Group and Exponential Structure*, and is not developed here.

**The norm-one group.** Because $N$ is multiplicative and $N(e_0)=1$, the level set

$$
\mathbb{B}^\times_1=\{\tilde{Q}\in\mathbb{B}:N(\tilde{Q})=1\}
$$

is a closed subgroup of $\mathbb{B}^\times$ of real dimension $6$, the **norm-one group**. It is noncompact, and it deformation retracts onto the unit quaternions $S^3$ (§*The Retraction of the Norm-One Group onto Its Maximal Compact Subgroup*); hence it is simply connected, of the homotopy type of $S^3$, with $\pi_3\cong\mathbb{Z}$. Its subgroups — the unit quaternions $S^3$ and the center $\{\pm e_0\}$ — are the subject of *Biquaternion Lie Group and Exponential Structure*, §*The Subgroups and the Real Forms*.

**Two unit spheres.** There are two candidate "unit spheres" in $\mathbb{B}$, and only one of them is a group. The Euclidean sphere $\|\tilde{Q}\|_E=1$ is a genuine sphere $S^7$ but is not a group, since $\|\cdot\|_E$ is not multiplicative and it contains zero divisors (*Biquaternion Topology*, §*The Euclidean unit sphere*). The level set $N(\tilde{Q})=1$ is a group but is neither Euclidean nor compact. The condition that makes a level set of a form on $\mathbb{B}$ a subgroup is $N=1$, not $\|\tilde{Q}\|_E=1$.

The group of units is an open subset of $\mathbb{B}$, hence a manifold of real dimension $8$, but its topology is far from that of a general open set in $\mathbb{R}^8$: it has the homotopy type of a compact group. The polar decomposition exhibits the maximal compact subgroup as a strong deformation retract, and with it determines the homotopy groups and the universal cover. Everything in this part is a statement about $\mathbb{B}^\times$ as a topological group; the topology of the ambient space and of the null cone is in *Biquaternion Topology*.

## The Retraction of $\mathbb{B}^\times$ onto Its Maximal Compact Subgroup

Every $\tilde{A} \in \mathbb{B}^\times$ has a unique polar decomposition $\tilde{A} = \tilde{U}\tilde{P}$, where $\tilde{U}$ is unitary ($\tilde{U}^\dagger\tilde{U} = e_0$) and $\tilde{P} = (\tilde{A}^\dagger\tilde{A})^{1/2}$ is Hermitian positive definite. For $t\in[0,1]$ put $\tilde{P}_t=(1-t)\tilde{P}+t e_0$ and

$$
\tilde{H}(t,\tilde{A})=\tilde{U}\tilde{P}_t.
$$

The eigenvalues of $\tilde{P}_t$ are $(1-t)\lambda+t$ with $\lambda>0$, hence positive, so $\tilde{P}_t$ is positive definite and $\tilde{H}(t,\tilde{A})\in \mathbb{B}^\times$; the map $\tilde{H}$ is continuous because the positive-definite square root depends continuously on $\tilde{A}$. Moreover

$$
\tilde{H}(0,\tilde{A})=\tilde{A},\qquad \tilde{H}(1,\tilde{A})=\tilde{U},\qquad \tilde{H}(t,\tilde{U})=\tilde{U}\ \text{ for unitary } \tilde{U}.
$$

So the unitary biquaternions form a strong deformation retract of $\mathbb{B}^\times$, and the two are homotopy equivalent, whence $\pi_n(\mathbb{B}^\times)\cong\pi_n(\mathrm{U}(\mathbb{B}))$ for all $n$, writing $\mathrm{U}(\mathbb{B})$ for the group of unitary biquaternions. Every $\tilde{A}$ is joined to a unitary element, and $\mathrm{U}(\mathbb{B})$ is connected (§*The Structure of the Maximal Compact Subgroup*), so $\mathbb{B}^\times$ is connected, in agreement with *Biquaternion Norm and Invertibility*. (The statement that there are two components distinguished by the sign of the determinant concerns the real algebra, not the complex one.) The retraction takes $\mathbb{B}^\times$ onto its maximal compact subgroup, the **unitary biquaternions**

$$
\mathrm{U}(\mathbb{B}) = \{\tilde{Q}\in\mathbb{B}:\tilde{Q}^\dagger\tilde{Q}=e_0\}.
$$

## The Retraction of the Norm-One Group onto Its Maximal Compact Subgroup

Let $\tilde{A}\in \mathbb{B}^\times_1$ have polar decomposition $\tilde{A}=\tilde{U}\tilde{P}$. Then $1=N(\tilde{A})=N(\tilde{U})N(\tilde{P})$, with $N(\tilde{U})$ of modulus $1$ and $N(\tilde{P})$ a positive real, so $N(\tilde{U})=N(\tilde{P})=1$, that is $\tilde{U}$ lies in $S^3$. For $t\in[0,1]$ define

$$
\tilde{P}_t=\frac{(1-t)\tilde{P}+t e_0}{N\big((1-t)\tilde{P}+t e_0\big)^{1/2}}.
$$

The denominator is a positive real number, so $\tilde{P}_t$ is Hermitian positive definite of norm $1$. The map $\tilde{H}(t,\tilde{A})=\tilde{U}\tilde{P}_t$ is continuous, lies in $\mathbb{B}^\times_1$ since $N(\tilde{U}\tilde{P}_t)=1$, and satisfies $\tilde{H}(0,\tilde{A})=\tilde{A}$, $\tilde{H}(1,\tilde{A})=\tilde{U}\in S^3$, and $\tilde{H}(t,\tilde{U})=\tilde{U}$ for unitary $\tilde{U}$. Hence $S^3$ is a strong deformation retract of $\mathbb{B}^\times_1$.

Thus $\mathbb{B}^\times_1\simeq S^3$: it is connected and simply connected with $\pi_3\cong\mathbb{Z}$ and the homotopy type of $S^3$, but is not homeomorphic to $S^3$, being a noncompact real $6$-manifold. The norm-one group $\mathbb{B}^\times_1$ of §*The Group of Units* is therefore simply connected, of homotopy type $S^3$.

## The Structure of the Maximal Compact Subgroup

The unit quaternions form $S^3$; $S^3$ is compact, connected and simply connected.

Every unitary biquaternion $\tilde{U}$ is a scalar multiple of a unit quaternion: if $N(\tilde{U})=z\in S^1$ and $\zeta^2=z$, then $\tilde{A}=\zeta^{-1}\tilde{U}$ has $N(\tilde{A})=1$ and $\tilde{U}=\zeta\tilde{A}$. Hence

$$
\mathrm{U}(\mathbb{B})=S^1\cdot S^3,\qquad S^1\cap S^3=\{\pm e_0\},
$$

and the multiplication map $S^1\times S^3\to \mathrm{U}(\mathbb{B})$ is a surjective homomorphism with kernel $\{(e_0,e_0),(-e_0,-e_0)\}\cong\mathbb{Z}/2$, so by the first isomorphism theorem for Lie groups

$$
\mathrm{U}(\mathbb{B})\cong(S^1\times S^3)/\{\pm e_0\},
$$

with $\{\pm e_0\}$ acting diagonally. The biquaternion norm $N:\mathrm{U}(\mathbb{B})\to S^1$ is a principal $S^3$-bundle, each fibre being a coset of $S^3$, and it admits a section, so

$$
\mathrm{U}(\mathbb{B})\cong S^1\times S^3
$$

as spaces. This is a homeomorphism, not an isomorphism of Lie groups: the map above is two-to-one, while the centre of $\mathrm{U}(\mathbb{B})$ is connected but that of $S^1\times S^3$ is not.

The central scalars form a maximal torus $T^2\cong S^1\times S^1\subset \mathrm{U}(\mathbb{B})$. It is **not** true that $\mathrm{U}(\mathbb{B})$ deformation retracts onto $T^2$: that would give $\pi_1(\mathrm{U}(\mathbb{B}))\cong\pi_1(T^2)$, but these are $\mathbb{Z}$ and $\mathbb{Z}^2$. Every element of $\mathrm{U}(\mathbb{B})$ does lie in some maximal torus, and the quotient is the complete flag variety

$$
\mathrm{U}(\mathbb{B})/T^2\cong P^1\cong S^2,
$$

so $\mathrm{U}(\mathbb{B})$ is a fibre bundle over $S^2$ with fibre $T^2$; and $\mathrm{U}(\mathbb{B})$ is not homotopy equivalent to $T^2$, being homeomorphic to $S^1\times S^3$.

## Homotopy Groups and Generators

The retractions give $S^3$ for the unit quaternions, $\mathrm{U}(\mathbb{B})\cong S^1\times S^3$, $\mathbb{B}^\times_1\simeq S^3$, and $\mathbb{B}^\times\simeq \mathrm{U}(\mathbb{B})\simeq S^1\times S^3$. Hence

$$
\pi_1(S^3)=\pi_2(S^3)=0,\qquad\pi_3(S^3)\cong\mathbb{Z},
$$

$$
\pi_1(\mathrm{U}(\mathbb{B}))\cong\mathbb{Z},\qquad\pi_2(\mathrm{U}(\mathbb{B}))=0,\qquad\pi_3(\mathrm{U}(\mathbb{B}))\cong\mathbb{Z},
$$

and likewise $\pi_1(\mathbb{B}^\times_1)=0$, $\pi_1(\mathbb{B}^\times)\cong\mathbb{Z}$, with $\pi_2=0$ and $\pi_3\cong\mathbb{Z}$ for both.

**Generators.** The group $\pi_3(S^3)\cong\mathbb{Z}$ is generated by the class $[\operatorname{id}_{S^3}]$ of the identity map under $S^3=\{\text{unit quaternions}\}$, and $\pi_3(\mathrm{U}(\mathbb{B}))\cong\mathbb{Z}$ by the image of that class under the inclusion $S^3\hookrightarrow \mathrm{U}(\mathbb{B})$, which induces an isomorphism on $\pi_3$. The group $\pi_1(\mathrm{U}(\mathbb{B}))\cong\mathbb{Z}$ is generated by the central loop $\gamma(t)=e^{2\pi i t}e_0$, $t\in[0,1]$, and $N_*:\pi_1(\mathrm{U}(\mathbb{B}))\to\pi_1(S^1)\cong\mathbb{Z}$ is an isomorphism, so a generator is a loop whose biquaternion norm winds once. The universal covers are

$$
\widetilde{\mathrm{U}(\mathbb{B})}\cong\widetilde{\mathbb{B}^\times}\cong\mathbb{R}\times S^3,
$$

while $S^3$ and $\mathbb{B}^\times_1$ are their own universal covers. By Hurewicz, $H_1(\mathrm{U}(\mathbb{B}))\cong H_1(\mathbb{B}^\times)\cong\mathbb{Z}$ and $H_1(S^3)=H_1(\mathbb{B}^\times_1)=0$; and $\pi_n(\mathrm{U}(\mathbb{B}))\cong\pi_n(S^3)$ for $n\geq2$.

## Summary

The group of units $\mathbb{B}^\times=\{N\neq0\}$ is open and dense in $\mathbb{B}$, its complement the null cone; it is connected and non-compact, of real dimension $8$, with centre $\mathbb{C}^\times e_0$.

Its topology is that of a compact group. The polar decomposition $\tilde{A}=\tilde{U}\tilde{P}$ gives a strong deformation retraction of $\mathbb{B}^\times$ onto the unitary biquaternions $\mathrm{U}(\mathbb{B})=\{\tilde{Q}^\dagger\tilde{Q}=e_0\}$, and a second retraction takes the norm-one group $\mathbb{B}^\times_1$ onto $S^3$. Hence $\mathbb{B}^\times\simeq\mathrm{U}(\mathbb{B})\simeq S^1\times S^3$ and $\mathbb{B}^\times_1\simeq S^3$, with
$$
\pi_1(\mathbb{B}^\times)\cong\mathbb{Z},\quad \pi_2(\mathbb{B}^\times)=0,\quad \pi_3(\mathbb{B}^\times)\cong\mathbb{Z},
$$
and $\mathbb{B}^\times_1$, $S^3$ simply connected with $\pi_3\cong\mathbb{Z}$. The universal cover is $\widetilde{\mathbb{B}^\times}\cong\mathbb{R}\times S^3$, generated by the identity class of $S^3$ and the central loop $e^{2\pi it}e_0$; $S^3$ and $\mathbb{B}^\times_1$ are their own universal covers. This is the content of the three retraction sections, and it is the topological face of the same group whose Lie algebra and exponential belong to Algebra and Analysis.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}^\times=\{N\neq0\}$ | Group of units; open and dense, complement of the null cone; real dimension $8$ |
| $\mathbb{B}^\times_1=\{N=1\}$ | Norm-one group; closed subgroup of real dimension $6$ |
| $\mathbb{C}^\times e_0$ | Centre of $\mathbb{B}^\times$; nonzero complex scalars |
| $\mathrm{U}(\mathbb{B})=\{\tilde{Q}^\dagger\tilde{Q}=e_0\}$ | Unitary biquaternions; maximal compact subgroup of $\mathbb{B}^\times$ |
| $\tilde{A}=\tilde{U}\tilde{P}$ | Polar decomposition; retraction onto $\mathrm{U}(\mathbb{B})$ |
| $S^3$ | Unit quaternions; maximal compact subgroup of $\mathbb{B}^\times_1$ |
| $\mathrm{U}(\mathbb{B})\cong S^1\times S^3$ | Homeomorphism; the maximal compact subgroup |
| $\mathbb{B}^\times\simeq\mathrm{U}(\mathbb{B})\simeq S^1\times S^3$ | Homotopy type of the group of units |
| $\mathbb{B}^\times_1\simeq S^3$ | Homotopy type of the norm-one group |
| $\widetilde{\mathbb{B}^\times}\cong\mathbb{R}\times S^3$ | Universal cover of the group of units |
| $\pi_1\cong\mathbb{Z},\ \pi_2=0,\ \pi_3\cong\mathbb{Z}$ | Homotopy of $\mathbb{B}^\times$ |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed. 2015).
- John Stillwell, *Naive Lie Theory* (Springer, 2008).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997).
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636.
