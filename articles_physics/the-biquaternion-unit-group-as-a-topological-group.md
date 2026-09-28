# __The Biquaternion Unit Group as a Topological Group__

## Introduction

This article describes the group of units $\mathbb{B}^\times$ of the biquaternion algebra as a topological group: its polar decomposition, its retractions onto the compact subgroups, the structure of those subgroups, and its homotopy groups. It uses the algebra and the unitary elements of *Biquaternion Algebra*, the biquaternion norm and the invertibility criterion of *Biquaternion Norm and Invertibility*, and the ambient topology and the null cone of *Biquaternion Topology*. The exponential and the Lie-group correspondence are *Biquaternion Lie Group and Exponential Structure*, and the motions the group carries are *Biquaternion Rotations and Lorentz Transformations*.

**Scope.** This is the topological part of the Lie-theoretic block. The Lie algebra is in *Biquaternion Lie Algebra*, the topology is here, and the Lie-group theory is in *Biquaternion Lie Group and Exponential Structure*; the motions the group generates are geometry. Nothing here is a statement about the smooth structure, which belongs with the Lie group.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$. The biquaternion norm is $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\sum_\mu Q_\mu^2$, and $\tilde{Q}$ is a unit exactly when $N(\tilde{Q})\neq0$. The conjugations are $\bar{\cdot}$ (quaternion), ${}^{*}$ (complex), ${}^{\dagger}=\bar{\cdot}{}^{*}$ (Hermitian), and the Hermitian form is $\tilde{Q}\tilde{Q}^\dagger$.

## The Group of Units

$$
\mathbb{B}^\times=\{\tilde{Q}\in\mathbb{B} : N(\tilde{Q})\neq0\}
$$

is a group under multiplication, because $N(\tilde{P}\tilde{Q})=N(\tilde{P})N(\tilde{Q})$ and $N(e_0)=1$: the product of two units has nonzero norm, and the inverse is $\tilde{Q}^{-1}=\bar{\tilde{Q}}/N(\tilde{Q})$. It is an open dense subset of $\mathbb{B}$ and its boundary is the null cone (*Biquaternion Topology*, §*The null cone as the boundary of the group of units*).

**Dimension.** $\mathbb{B}^\times$ has complex dimension $4$ and real dimension $8$; the units are exactly the elements of nonzero norm.

**The norm-one group.** Because $N$ is multiplicative and $N(e_0)=1$, the level set

$$
\mathbb{B}^\times_1=\{\tilde{Q}\in\mathbb{B} : N(\tilde{Q})=1\}
$$

is a subgroup, the **norm-one group**. It is a noncompact real $6$-manifold.

**Two unit spheres.** There are two candidate "unit spheres" in $\mathbb{B}$, and only one of them is a group. The Euclidean sphere $\|\tilde{Q}\|_E=1$ is a genuine sphere $S^7$ but is not a group, since $\|\cdot\|_E$ is not multiplicative and it contains zero divisors (*Biquaternion Topology*, §*The Euclidean unit sphere*). The level set $N(\tilde{Q})=1$ is a group but is neither Euclidean nor compact. The condition that makes a level set of a form on $\mathbb{B}$ a subgroup is $N=1$, not $\|\tilde{Q}\|_E=1$.

**Physical reading.** The invertible elements are the objects on which the motions act, and the norm-one slice is the slice in which the norm is normalised. The distinction between the two unit spheres is the distinction between the normalisation of a quantum state (Hermitian, $\|\cdot\|_E=1$) and the normalisation of a motion (biquaternion, $N=1$). The units are also what acts on the material four-position $\tilde{Q}=ict\,e_0+\mathbf{x}$: the boundary of $\mathbb{B}^\times$ is the null cone, whose intersection with that sector is the light cone $c^2t^2=\mathbf{x}^2$.

## The Retraction of $\mathbb{B}^\times$ onto Its Maximal Compact Subgroup

Every $\tilde{A}\in\mathbb{B}^\times$ has a unique polar decomposition $\tilde{A}=\tilde{U}\tilde{P}$, where $\tilde{U}$ is unitary ($\tilde{U}^\dagger\tilde{U}=e_0$) and $\tilde{P}=(\tilde{A}^\dagger\tilde{A})^{1/2}$ is Hermitian positive definite. For $t\in[0,1]$ put $\tilde{P}_t=(1-t)\tilde{P}+te_0$ and

$$
\tilde{H}(t,\tilde{A})=\tilde{U}\tilde{P}_t .
$$

The eigenvalues of $\tilde{P}_t$ are $(1-t)\lambda+t$ with $\lambda>0$, hence positive, so $\tilde{P}_t$ is positive definite and $\tilde{H}(t,\tilde{A})\in\mathbb{B}^\times$; the map $\tilde{H}$ is continuous. Moreover $\tilde{H}(0,\tilde{A})=\tilde{A}$, $\tilde{H}(1,\tilde{A})=\tilde{U}$, and $\tilde{H}(t,\tilde{U})=\tilde{U}$ for unitary $\tilde{U}$. So the unitary biquaternions form a strong deformation retract of $\mathbb{B}^\times$, and the two are homotopy equivalent, whence $\pi_n(\mathbb{B}^\times)\cong\pi_n(\mathrm{U}(\mathbb{B}))$ for all $n$, writing $\mathrm{U}(\mathbb{B})$ for the group of unitary biquaternions. Every $\tilde{A}$ is joined to a unitary element, and $\mathrm{U}(\mathbb{B})$ is connected, so $\mathbb{B}^\times$ is connected. The retraction takes $\mathbb{B}^\times$ onto its maximal compact subgroup,

$$
\mathrm{U}(\mathbb{B})=\{\tilde{Q}\in\mathbb{B} : \tilde{Q}^\dagger\tilde{Q}=e_0\} .
$$

**Physical reading.** The deformation is the removal of the boost: the Hermitian positive-definite factor $\tilde{P}$ carries the boost and the unitary factor $\tilde{U}$ the rotation and the phase, so retracting $\tilde{P}$ to the identity leaves the rotation and the phase untouched. This is why the topology of the motion group is the topology of its maximal compact subgroup, and why the non-compact directions contribute no homotopy. In the $ict$ convention the removal is the removal of the time–space mixing: on the material four-position $\tilde{Q}=ict\,e_0+\mathbf{x}$ the factor $\tilde{P}$ is what carries the rapidity and moves $ict$ toward $x_k$, and setting $\tilde{P}=e_0$ sets the rapidity to zero and leaves a pure rotation of $\mathbf{x}$.

## The Retraction of the Norm-One Group onto Its Maximal Compact Subgroup

Let $\tilde{A}\in\mathbb{B}^\times_1$ have polar decomposition $\tilde{A}=\tilde{U}\tilde{P}$. Then $1=N(\tilde{A})=N(\tilde{U})N(\tilde{P})$, with $N(\tilde{U})$ of modulus $1$ and $N(\tilde{P})$ a positive real, so $N(\tilde{U})=N(\tilde{P})=1$, that is $\tilde{U}$ lies in $S^3$. For $t\in[0,1]$ define

$$
\tilde{P}_t=\frac{(1-t)\tilde{P}+te_0}{N\big((1-t)\tilde{P}+te_0\big)^{1/2}} .
$$

The denominator is a positive real number, so $\tilde{P}_t$ is Hermitian positive definite of norm $1$. The map $\tilde{H}(t,\tilde{A})=\tilde{U}\tilde{P}_t$ is continuous, lies in $\mathbb{B}^\times_1$ since $N(\tilde{U}\tilde{P}_t)=1$, and satisfies $\tilde{H}(0,\tilde{A})=\tilde{A}$, $\tilde{H}(1,\tilde{A})=\tilde{U}\in S^3$, and $\tilde{H}(t,\tilde{U})=\tilde{U}$ for unitary $\tilde{U}$. Hence $S^3$ is a strong deformation retract of $\mathbb{B}^\times_1$.

Thus $\mathbb{B}^\times_1\simeq S^3$: it is connected and simply connected with $\pi_3\cong\mathbb{Z}$ and the homotopy type of $S^3$, but is not homeomorphic to $S^3$, being a noncompact real $6$-manifold. The norm-one group is therefore simply connected, of homotopy type $S^3$.

**Physical reading.** On the norm-one slice the norm is normalised, and the slice retracts onto the unit quaternions, so the topology that remains is that of the unit quaternions. A closed loop in $\mathbb{B}^\times_1$ is contractible, so the norm-one slice carries no winding number; the winding appears only in the full group, through the phase.

## The Structure of the Maximal Compact Subgroup

The unit quaternions form $S^3$; $S^3$ is compact, connected and simply connected.

Every unitary biquaternion $\tilde{U}$ is a scalar multiple of a unit quaternion: if $N(\tilde{U})=z\in S^1$ and $\zeta^2=z$, then $\tilde{A}=\zeta^{-1}\tilde{U}$ has $N(\tilde{A})=1$ and $\tilde{U}=\zeta\tilde{A}$. Hence

$$
\mathrm{U}(\mathbb{B})=S^1\cdot S^3,\qquad S^1\cap S^3=\{\pm e_0\},
$$

and the multiplication map $S^1\times S^3\to\mathrm{U}(\mathbb{B})$ is a surjective homomorphism with kernel $\{(e_0,e_0),(-e_0,-e_0)\}\cong\mathbb{Z}/2$, so

$$
\mathrm{U}(\mathbb{B})\cong(S^1\times S^3)/\{\pm e_0\},
$$

with $\{\pm e_0\}$ acting diagonally. The biquaternion norm $N:\mathrm{U}(\mathbb{B})\to S^1$ is a principal $S^3$-bundle, each fibre being a coset of $S^3$, and it admits a section, so $\mathrm{U}(\mathbb{B})\cong S^1\times S^3$ as spaces. This is a homeomorphism, not an isomorphism of Lie groups: the map above is two-to-one, while the centre of $\mathrm{U}(\mathbb{B})$ is connected but that of $S^1\times S^3$ is not.

The central scalars form a maximal torus $T^2\cong S^1\times S^1\subset\mathrm{U}(\mathbb{B})$. It is **not** true that $\mathrm{U}(\mathbb{B})$ deformation retracts onto $T^2$: that would give $\pi_1(\mathrm{U}(\mathbb{B}))\cong\pi_1(T^2)$, but these are $\mathbb{Z}$ and $\mathbb{Z}^2$. Every element of $\mathrm{U}(\mathbb{B})$ does lie in some maximal torus, and the quotient is $\mathrm{U}(\mathbb{B})/T^2\cong P^1\cong S^2$, so $\mathrm{U}(\mathbb{B})$ is a fibre bundle over $S^2$ with fibre $T^2$; and $\mathrm{U}(\mathbb{B})$ is not homotopy equivalent to $T^2$, being homeomorphic to $S^1\times S^3$.

**Physical reading.** The two factors of the maximal compact subgroup are the two things a unitary element carries: the $S^3$ factor is the unit quaternions, and the $S^1$ factor is the central phase, the global phase of a quantum state, the phase of the scalar line $\mathbb{C}e_0$, which is also the line that carries the two times $ct'$ and $ict$. The identification $\mathrm{U}(\mathbb{B})\cong S^1\times S^3$ therefore says that the compact part of the group is a unit quaternion together with a phase, and the two are not independent as a group, only as a space: the quotient by $\{\pm e_0\}$ is what turns the unit quaternion into a rotation and not a spinor. The maximal torus is the pair of commuting factors, of the phase and of an axis, and the sphere $\mathrm{U}(\mathbb{B})/T^2\cong S^2$ is the sphere of axes.

## Homotopy Groups and Generators

The retractions give $S^3$ for the unit quaternions, $\mathrm{U}(\mathbb{B})\cong S^1\times S^3$, $\mathbb{B}^\times_1\simeq S^3$, and $\mathbb{B}^\times\simeq\mathrm{U}(\mathbb{B})\simeq S^1\times S^3$. Hence

$$
\pi_1(S^3)=\pi_2(S^3)=0,\qquad \pi_3(S^3)\cong\mathbb{Z},
$$

$$
\pi_1(\mathrm{U}(\mathbb{B}))\cong\mathbb{Z},\qquad \pi_2(\mathrm{U}(\mathbb{B}))=0,\qquad \pi_3(\mathrm{U}(\mathbb{B}))\cong\mathbb{Z},
$$

and likewise $\pi_1(\mathbb{B}^\times_1)=0$, $\pi_1(\mathbb{B}^\times)\cong\mathbb{Z}$, with $\pi_2=0$ and $\pi_3\cong\mathbb{Z}$ for both.

**Generators.** The group $\pi_3(S^3)\cong\mathbb{Z}$ is generated by the class $[\operatorname{id}_{S^3}]$ of the identity map under $S^3=\{$unit quaternions$\}$, and $\pi_3(\mathrm{U}(\mathbb{B}))\cong\mathbb{Z}$ by the image of that class under the inclusion $S^3\hookrightarrow\mathrm{U}(\mathbb{B})$, which induces an isomorphism on $\pi_3$. The group $\pi_1(\mathrm{U}(\mathbb{B}))\cong\mathbb{Z}$ is generated by the central loop $\gamma(t)=e^{2\pi it}e_0$, $t\in[0,1]$, and $N_*:\pi_1(\mathrm{U}(\mathbb{B}))\to\pi_1(S^1)\cong\mathbb{Z}$ is an isomorphism, so a generator is a loop whose biquaternion norm winds once. The universal covers are

$$
\widetilde{\mathrm{U}(\mathbb{B})}\cong\widetilde{\mathbb{B}^\times}\cong\mathbb{R}\times S^3,
$$

while $S^3$ and $\mathbb{B}^\times_1$ are their own universal covers. By Hurewicz, $H_1(\mathrm{U}(\mathbb{B}))\cong H_1(\mathbb{B}^\times)\cong\mathbb{Z}$ and $H_1(S^3)=H_1(\mathbb{B}^\times_1)=0$; and $\pi_n(\mathrm{U}(\mathbb{B}))\cong\pi_n(S^3)$ for $n\ge2$.

**Physical reading.** The factor $\pi_1(\mathbb{B}^\times)\cong\mathbb{Z}$ is the winding of the phase, the homotopy invariant that a closed loop of transformations can carry, and it is the topological home of the winding numbers the framework uses. The factor $\pi_3\cong\mathbb{Z}$ is the winding of the unit quaternions, the invariant of a Skyrme field, and it is generated by the identity map of the unit quaternions because a unit quaternion *is* a map from the spatial sphere to the group. The universal cover $\mathbb{R}\times S^3$ is the statement that unwinding the phase and unwinding the rotation are independent: the first gives the real line, the second gives the spin cover.

## Summary

The group of units $\mathbb{B}^\times$ is the complement of the null cone, of real dimension $8$; it is connected, and it deformation retracts onto its maximal compact subgroup $\mathrm{U}(\mathbb{B})$, so it is homotopy equivalent to $S^1\times S^3$. The norm-one group $\mathbb{B}^\times_1$ is a noncompact real $6$-manifold of the homotopy type of $S^3$: connected, simply connected, with $\pi_3\cong\mathbb{Z}$. The compact group is $\mathrm{U}(\mathbb{B})\cong(S^1\times S^3)/\{\pm e_0\}$, homeomorphic to $S^1\times S^3$, with the $S^3$ factor the rotations and the $S^1$ factor the central phase. In homotopy, $\pi_1(\mathbb{B}^\times)\cong\mathbb{Z}$ generated by the winding of the phase, $\pi_3\cong\mathbb{Z}$ generated by the identity of the unit quaternions, $\pi_2=0$, and the universal cover of the full group is $\mathbb{R}\times S^3$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}^\times=\{\tilde{Q} : N(\tilde{Q})\neq0\}$ | Group of units; open and dense, boundary the null cone |
| $\mathbb{B}^\times_1=\{\tilde{Q} : N(\tilde{Q})=1\}$ | Norm-one group; noncompact real $6$-manifold, $\simeq S^3$ |
| $\mathrm{U}(\mathbb{B})=\{\tilde{Q} : \tilde{Q}^\dagger\tilde{Q}=e_0\}$ | Unitary biquaternions, the maximal compact subgroup |
| $\tilde{A}=\tilde{U}\tilde{P}$ | Polar decomposition; $\tilde{U}$ unitary, $\tilde{P}$ Hermitian positive definite |
| $\mathrm{U}(\mathbb{B})\cong(S^1\times S^3)/\{\pm e_0\}$ | Maximal compact subgroup as a group |
| $\mathrm{U}(\mathbb{B})\cong S^1\times S^3$ | Homeomorphism, not a group isomorphism |
| $S^1$ factor | Central phase; the phase of the scalar line $\mathbb{C}e_0$ that carries $ct'+ict$ |
| $\tilde{Q}=ict\,e_0+\mathbf{x}$ | Material four-position; its light cone $c^2t^2=\mathbf{x}^2$ is the boundary of $\mathbb{B}^\times$ |
| $S^3$ factor | Unit quaternions |
| $T^2\cong S^1\times S^1$ | Maximal torus; not a deformation retract |
| $\pi_1(\mathbb{B}^\times)\cong\mathbb{Z}$ | Winding of the phase |
| $\pi_3\cong\mathbb{Z}$ | Winding of the unit quaternions; the Skyrme invariant |
| $\widetilde{\mathbb{B}^\times}\cong\mathbb{R}\times S^3$ | Universal cover |

## Further Reading

- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the group of units of the complexified quaternions and its polar decomposition.
- Morton L. Curtis and others on the classical groups, and Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge, 1995), for the maximal compact subgroups of the classical groups and the unitary group of a complex quadratic space.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, vol. 1 (Cambridge, 1984), for the double cover of the rotation group and the topology of the Lorentz group.
- Norman Steenrod, *The Topology of Fibre Bundles* (Princeton, 1951), for principal bundles, sections and the homotopy of the classical groups.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the unitary elements of a complex Clifford algebra and the spin groups.
