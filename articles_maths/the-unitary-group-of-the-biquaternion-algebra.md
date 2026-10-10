# __The Unitary Group of the Biquaternion Algebra__

## Introduction

The general plain sesquilinear form $\tilde{Q}\tilde{Q}^{*}$ singles out, inside the group of units of the biquaternion algebra, the elements that leave it invariant: the **unitary biquaternions** $\tilde{U}$ with $\tilde{U}^{*}\tilde{U}=e_0$. This is the maximal compact subgroup $U(\mathbb{B})\cong U(2)$ of $\mathbb{B}^{\times}$, the compact real form of the algebra, and it is the single object through which the whole topology of the group of units is read: the polar decomposition gives a strong deformation retraction of $\mathbb{B}^{\times}$ onto $U(\mathbb{B})$ and of the norm-one group onto its compact part $S^{3}$, and the homotopy groups, the generators and the universal cover follow from the resulting homotopy equivalence $\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$.

This article collects the *Hermitian* half of the topology of the unit group: the unitary slice, its structure, the two retractions that the dagger supplies, and the homotopy invariants. The *bilinear* half — the units as the complement of the null cone, the centre, the distribution of the units among the three classes — is *The Biquaternion Unit Group as a Topological Group* and *Biquaternion Norm and Invertibility*, and the ambient Euclidean topology and the contractibility of the algebra are *The Euclidean Topology of the Biquaternion Algebra*.

**Conventions.** As in the sibling articles: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, $\tilde{Q}=\sum_\mu Q_\mu e_\mu$, $\|\tilde{Q}\|_E=(\sum_\mu|Q_\mu|^{2})^{1/2}$, $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^{2}$, dagger ${}^{*}={}^{\natural}\circ\bar{\cdot}$, and $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ the matrix isomorphism of *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$*, which carries the dagger to the conjugate transpose.

## The Unitary Biquaternions

**Definition.** The **unitary biquaternions** are

$$
U(\mathbb{B})=\{\tilde{U}\in\mathbb{B}:\tilde{U}^{*}\tilde{U}=e_0\}.
$$

**Theorem ($U(\mathbb{B})\cong U(2)$).** $\Phi$ restricts to an isomorphism of groups $\Phi:U(\mathbb{B})\to U(2)$. In particular $U(\mathbb{B})$ is a compact Lie group of real dimension four, and its elements are exactly the biquaternions of the form

$$
\tilde{U}=A\,\tilde{q},\qquad A\in\mathbb{C},\ |A|=1,\quad \tilde{q}\in\mathbb{H},\ \langle\tilde{q},\tilde{q}\rangle_{\natural}=1,
$$

that is, scalar multiples of unit quaternions by phases.

**Proof.** Since $\Phi$ is an algebra isomorphism and $\Phi(\tilde{Q}^{*})=\Phi(\tilde{Q})^{\dagger}$ (*Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$*, §*The Conjugations in Matrix Form*), the equation $\tilde{U}^{*}\tilde{U}=e_0$ is equivalent to $\Phi(\tilde{U})^{\dagger}\Phi(\tilde{U})=I$, which defines $U(2)$; the restriction of an injective homomorphism is an injective homomorphism onto that group. For the normal form: the identity $\langle\tilde{U},\tilde{U}\rangle_{\natural}=\det\Phi(\tilde{U})$ makes $|\langle\tilde{U},\tilde{U}\rangle_{\natural}|=1$, so if $\zeta^{2}=\langle\tilde{U},\tilde{U}\rangle_{\natural}$ then $\tilde{A}=\zeta^{-1}\tilde{U}$ has $\langle\tilde{A},\tilde{A}\rangle_{\natural}=1$; a norm-one element is a unit quaternion (*Biquaternion Norm and Invertibility*, §*The Relation to the Hermitian Decomposition*), and $\tilde{U}=\zeta\tilde{A}$.

**Corollary (the determinant and the norm coincide).** On $U(\mathbb{B})$ the biquaternion norm is the determinant through $\Phi$, and $N:U(\mathbb{B})\to S^{1}$ is a surjective homomorphism with kernel $S^{3}$, the unit quaternions. Hence $N$ realises an isomorphism $U(\mathbb{B})/S^{3}\cong S^{1}$.

**Proof.** $\langle\tilde{U}\tilde{V},\tilde{U}\tilde{V}\rangle_{\natural}=\langle\tilde{U},\tilde{U}\rangle_{\natural}\langle\tilde{V},\tilde{V}\rangle_{\natural}$ is the multiplicativity of the norm ($\det$ is multiplicative), $\langle e_0,e_0\rangle_{\natural}=1$, and $|\langle\tilde{U},\tilde{U}\rangle_{\natural}|=1$ by the theorem, so the image lies in $S^{1}$ and is a subgroup; it is all of $S^{1}$ because $A\mapsto Ae_0$ is unitary of norm $A$. The kernel is $\{N=1\}\cap U(\mathbb{B})$, which is the unit quaternions.

## The Structure of the Unitary Group

**Theorem (the product decomposition).** $U(\mathbb{B})=S^{1}\cdot S^{3}$ with $S^{1}\cap S^{3}=\{\pm e_0\}$, where $S^{1}=U(1)e_0$ is the centre circle and $S^{3}$ the unit quaternions; the multiplication map $S^{1}\times S^{3}\to U(\mathbb{B})$ is a surjective homomorphism with kernel $\{(e_0,e_0),(-e_0,-e_0)\}$, so

$$
U(\mathbb{B})\cong \bigl(S^{1}\times S^{3}\bigr)/\{\pm e_0\}
$$

with the diagonal action, and this quotient is homeomorphic to $S^{1}\times S^{3}$.

**Proof.** The normal form writes an element as $A\tilde q$ with $A\in S^{1}$ and $\tilde{q}\in S^{3}$, and the intersection of the two subgroups is $\{A\in S^{1}: A\in\mathbb{H}\}=\{\pm e_0\}$; the product map is a homomorphism because $S^{1}$ is central. The quotient description is the first isomorphism theorem for Lie groups, and the homeomorphism $U(\mathbb{B})\cong S^{1}\times S^{3}$ is the section $\tilde{U}\mapsto(\langle\tilde{U},\tilde{U}\rangle_{\natural},\langle\tilde{U},\tilde{U}\rangle_{\natural}^{-1/2}\tilde{U})$.

**Remark (not an isomorphism of groups).** The homeomorphism $U(\mathbb{B})\cong S^{1}\times S^{3}$ is not a group isomorphism: its centre is connected, that of $S^{1}\times S^{3}$ is not, and the product map above is two-to-one.

**Theorem (the maximal torus and the flag variety).** The central scalars of modulus one form a maximal torus $T^{2}\cong S^{1}\times S^{1}$; every element of $U(\mathbb{B})$ lies in some maximal torus; and

$$
U(\mathbb{B})/T^{2}\cong P^{1}\cong S^{2},
$$

so $U(\mathbb{B})$ is a fibre bundle over $S^{2}$ with fibre $T^{2}$. It does not deformation retract onto $T^{2}$.

**Proof.** The diagonal matrices are the maximal tori of $U(2)$, and $U(2)/T^{2}$ is the complete flag variety of $\mathbb{C}^{2}$, which is $P^{1}$; a retraction onto a maximal torus would force $\pi_1(U(\mathbb{B}))\cong\pi_1(T^{2})$, but these are $\mathbb{Z}$ and $\mathbb{Z}^{2}$.

## The Retraction of the Unit Group onto the Unitary Group

**Theorem (polar decomposition).** Every $\tilde{A}\in\mathbb{B}^{\times}$ has a unique decomposition

$$
\tilde{A}=\tilde{U}\tilde{P},\qquad \tilde{U}\in U(\mathbb{B}),\quad \tilde{P}\ \text{Hermitian and positive definite},
$$

with $\tilde{P}=(\tilde{A}^{*}\tilde{A})^{1/2}$; the map $\tilde{A}\mapsto(\tilde{U},\tilde{P})$ is a homeomorphism of $\mathbb{B}^{\times}$ onto $U(\mathbb{B})\times\{\text{Hermitian positive definite}\}$.

**Proof.** $\tilde{A}^{*}\tilde{A}$ is Hermitian and positive definite for $\tilde{A}$ a unit, because $\mathrm{Sc}(\tilde{A}^{*}\tilde{A})=\|\tilde{A}\|_E^{2}>0$ and the Hermitian elements that are positive for the dagger form the cone of the units (*Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, §*The Hermitian Cone*); a positive definite Hermitian element has a unique positive definite square root $\tilde{P}$, and $\tilde{U}=\tilde{A}\tilde{P}^{-1}$ satisfies $\tilde{U}^{*}\tilde{U}=\tilde{P}^{-1}\tilde{A}^{*}\tilde{A}\tilde{P}^{-1}=e_0$. Uniqueness is the standard argument: $\tilde{P}^{2}=\tilde{A}^{*}\tilde{A}$ has one positive definite root.

**Theorem (strong deformation retraction).** For $t\in[0,1]$ put $\tilde{P}_t=(1-t)\tilde{P}+t e_0$ and $\tilde{H}(t,\tilde{A})=\tilde{U}\tilde{P}_t$. Then $\tilde{H}$ is a strong deformation retraction of $\mathbb{B}^{\times}$ onto $U(\mathbb{B})$:

$$
\tilde{H}(0,\tilde{A})=\tilde{A},\qquad \tilde{H}(1,\tilde{A})=\tilde{U},\qquad \tilde{H}(t,\tilde{U})=\tilde{U}\ \text{for}\ \tilde{U}\in U(\mathbb{B}).
$$

Hence $\mathbb{B}^{\times}\simeq U(\mathbb{B})$, and $\pi_n(\mathbb{B}^{\times})\cong\pi_n(U(\mathbb{B}))$ for all $n$.

**Proof.** The eigenvalues of $\tilde{P}_t$ are $(1-t)\lambda+t$ with $\lambda>0$, hence positive, so $\tilde{P}_t$ is positive definite and $\tilde{U}\tilde{P}_t\in\mathbb{B}^{\times}$; the positive definite square root depends continuously on $\tilde{A}$ (*Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, §*The Operator of an Element*), so $\tilde{H}$ is continuous; the three identities are immediate from $\tilde{P}_0=\tilde{P}$, $\tilde{P}_1=e_0$ and the fact that a unitary element has $\tilde{P}=e_0$.

**Corollary (connectedness).** $\mathbb{B}^{\times}$ is connected, and $U(\mathbb{B})$ is connected.

**Proof.** $\tilde{H}$ joins every unit to a unitary element, and $U(\mathbb{B})\cong(S^{1}\times S^{3})/\{\pm\}$ is a continuous image of the connected group $S^{1}\times S^{3}$.

## The Retraction of the Norm-One Group onto $S^{3}$

**Theorem.** The unit quaternions $S^{3}$ are a strong deformation retract of the norm-one group $\mathbb{B}^{\times}_1=\{N=1\}$, so $\mathbb{B}^{\times}_1\simeq S^{3}$: it is connected and simply connected, with $\pi_3\cong\mathbb{Z}$ and vanishing $\pi_1,\pi_2$.

**Proof.** Let $\tilde{A}\in\mathbb{B}^{\times}_1$ with polar decomposition $\tilde{A}=\tilde{U}\tilde{P}$. Then $1=\langle\tilde{A},\tilde{A}\rangle_{\natural}=\langle\tilde{U},\tilde{U}\rangle_{\natural}\langle\tilde{P},\tilde{P}\rangle_{\natural}$, with $|\langle\tilde{U},\tilde{U}\rangle_{\natural}|=1$ and $\langle\tilde{P},\tilde{P}\rangle_{\natural}$ a positive real, so $\langle\tilde{U},\tilde{U}\rangle_{\natural}=\langle\tilde{P},\tilde{P}\rangle_{\natural}=1$ and $\tilde{U}\in S^{3}$ by the normal form of the previous section. For $t\in[0,1]$ the element

$$
\tilde{P}_t=\frac{(1-t)\tilde{P}+te_0}{N\bigl((1-t)\tilde{P}+te_0\bigr)^{1/2}}
$$

is Hermitian positive definite of norm one (the denominator is a positive real), the map $\tilde{H}(t,\tilde{A})=\tilde{U}\tilde{P}_t$ is continuous and lands in $\mathbb{B}^{\times}_1$, and $\tilde{H}(0,\tilde{A})=\tilde{A}$, $\tilde{H}(1,\tilde{A})=\tilde{U}\in S^{3}$, $\tilde{H}(t,\tilde{U})=\tilde{U}$.

**Remark.** $\mathbb{B}^{\times}_1$ is not homeomorphic to $S^{3}$: it is a non-compact real $6$-manifold. It is a closed subgroup of $\mathbb{B}^{\times}$, of real dimension $6$ (*Biquaternion Lie Group and Exponential Structure*, §*The Subgroups and the Real Forms*).

## Homotopy Groups, Generators and the Universal Cover

**Theorem.** The homotopy invariants are

$$
\mathbb{B}^{\times}\simeq U(\mathbb{B})\simeq S^{1}\times S^{3},\qquad \mathbb{B}^{\times}_1\simeq S^{3},
$$

$$
\pi_1(\mathbb{B}^{\times})\cong\mathbb{Z},\quad \pi_2(\mathbb{B}^{\times})=0,\quad \pi_3(\mathbb{B}^{\times})\cong\mathbb{Z},\qquad
\pi_1(\mathbb{B}^{\times}_1)=0,\quad \pi_2(\mathbb{B}^{\times}_1)=0,\quad \pi_3(\mathbb{B}^{\times}_1)\cong\mathbb{Z},
$$

and the universal covers are $\widetilde{\mathbb{B}^{\times}}\cong\widetilde{U(\mathbb{B})}\cong\mathbb{R}\times S^{3}$, while $S^{3}$ and $\mathbb{B}^{\times}_1$ are their own universal covers.

**Proof.** The two retractions give the homotopy equivalences; the homotopy groups of $S^{3}$ are $\pi_1=\pi_2=0$, $\pi_3\cong\mathbb{Z}$, and those of $S^{1}\times S^{3}$ follow by the product formula. The universal cover of $S^{1}\times S^{3}$ is $\mathbb{R}\times S^{3}$ because $S^{3}$ is simply connected, and the same holds for the group of units by the homotopy equivalence.

**Generators.** $\pi_3(U(\mathbb{B}))\cong\mathbb{Z}$ is generated by the image of the class of $\mathrm{id}_{S^{3}}$ under $S^{3}\hookrightarrow U(\mathbb{B})$, which induces an isomorphism on $\pi_3$; $\pi_1(U(\mathbb{B}))\cong\mathbb{Z}$ is generated by the central loop $\gamma(t)=e^{2\pi it}e_0$, and $N_*:\pi_1(U(\mathbb{B}))\to\pi_1(S^{1})$ is an isomorphism, so a generator is a loop along which the biquaternion norm winds once.

**Proof.** The inclusions $S^{3}\subset U(\mathbb{B})\subset\mathbb{B}^{\times}$ and the retractions give the first statement; the second is the identification of $\pi_1$ with the fundamental group of the centre circle via the bundle $S^{1}\to U(\mathbb{B})\to S^{3}$... precisely, $U(\mathbb{B})\cong(S^{1}\times S^{3})/\{\pm\}$ and the projection to the first factor realises $N$.

**Corollary (Hurewicz).** $H_1(\mathbb{B}^{\times})\cong H_1(U(\mathbb{B}))\cong\mathbb{Z}$, $H_1(S^{3})=H_1(\mathbb{B}^{\times}_1)=0$, and $\pi_n(U(\mathbb{B}))\cong\pi_n(S^{3})$ for $n\geq2$.

**Proof.** Immediate from the theorem and the Hurewicz theorem in degree one.

## The Unitary Group and the Lorentz Group

The compact slice is not only the compact real form of the algebra; it is the double cover of the rotation group of the Hermitian subspace.

**Theorem.** The inner conjugation $\tilde{U}\mapsto\Theta_{\tilde{U}}$, $\Theta_{\tilde{U}}(\tilde{R})=\tilde{U}\tilde{R}\tilde{U}^{\dagger}$, restricts to an action of $U(\mathbb{B})$ on the Hermitian subspace $\mathbb{M}_{+}$ by isometries of the interval form, and the map

$$
U(\mathbb{B})\longrightarrow SO(3),\qquad \tilde{U}\longmapsto \Theta_{\tilde{U}}|_{\mathbb{M}_{+}},
$$

is a surjective homomorphism with kernel $U(1)e_0$, so that $U(\mathbb{B})/U(1)\cong PU(2)\cong SO(3)$.

**Proof.** $\Theta_{\tilde{U}}$ is an algebra automorphism and a Euclidean isometry, and it preserves $\mathbb{M}_{+}$ because it preserves the dagger; it preserves the interval form because it is an algebra automorphism and the form is $N$ on $\mathbb{M}_{+}$. The kernel consists of the $\tilde{U}$ acting trivially on $\mathbb{M}_{+}$, and an automorphism fixing the Hermitian subspace is inner by a central element, so the kernel is the central circle; the quotient $PU(2)$ is the adjoint form of $U(2)$, isomorphic to $SO(3)$. On the unit quaternions the same map is the classical double cover $S^{3}\to SO(3)$.

**Remark (the two covers).** The unitary group therefore sits between the two classical double covers of the corpus: $S^{3}\to SO(3)$ on the compact slice, and $S^{3}\times S^{3}\to SO(4)$ for the two-sided action (*Biquaternion Rotations and Lorentz Transformations*). Its full conjugation action on $\mathbb{B}$ is the adjoint action of $U(2)$ on $M_2(\mathbb{C})$, whose orbits are the level sets of $\mathrm{Sc}$ and $N$.

## Worked Examples

**A central element.** $\tilde{U}=Ae_0$ is unitary exactly when $|A|=1$, and then $\langle\tilde{U},\tilde{U}\rangle_{\natural}=A^{2}$, so the centre circle maps onto $S^{1}$ twice.

**A unit quaternion.** $\tilde{U}\in\mathbb{H}_{\mathbb{B}}$, $\langle\tilde{U},\tilde{U}\rangle_{\natural}=1$, is unitary, is fixed by $\Theta$ only when central, and generates the image of $\pi_3$.

**A null scalar multiple.** $\tilde{Q}=A(e_1+ie_2)$ with $A\neq0$ has $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0$, so it is not a unit and in particular not unitary; its Euclidean norm is $\sqrt2|A|$.

**A negative determinant.** $U(2)$ has determinant of modulus one; the slice $SU(2)=\{N=1\}\cap U(\mathbb{B})=S^{3}$ is the unit quaternions, the kernel of $N$, and the double cover of $SO(3)$.

## Summary

The **unitary biquaternions** $U(\mathbb{B})=\{\tilde{U}^{*}\tilde{U}=e_0\}$ are the maximal compact subgroup of $\mathbb{B}^{\times}$, isomorphic to $U(2)$ through the matrix model and equal to the scalar multiples of the unit quaternions by phases. The group splits as $U(\mathbb{B})=S^{1}\cdot S^{3}$ with intersection $\{\pm e_0\}$, so $U(\mathbb{B})\cong(S^{1}\times S^{3})/\{\pm\}\cong S^{1}\times S^{3}$ as spaces, with maximal torus $T^{2}$ and flag variety $U(\mathbb{B})/T^{2}\cong S^{2}$. The polar decomposition $\tilde{A}=\tilde{U}\tilde{P}$ supplies strong deformation retractions of $\mathbb{B}^{\times}$ onto $U(\mathbb{B})$ and of $\mathbb{B}^{\times}_1$ onto $S^{3}$, whence $\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$, $\mathbb{B}^{\times}_1\simeq S^{3}$, $\pi_1(\mathbb{B}^{\times})\cong\mathbb{Z}$, $\pi_2=0$, $\pi_3\cong\mathbb{Z}$, and universal cover $\mathbb{R}\times S^{3}$. The norm $N$ is the determinant and $U(\mathbb{B})/S^{3}\cong S^{1}$; the conjugation action gives $U(\mathbb{B})/U(1)\cong SO(3)$, the compact real form of the Lorentz group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $U(\mathbb{B})=\{\tilde{U}^{*}\tilde{U}=e_0\}$ | Unitary biquaternions; maximal compact subgroup $\cong U(2)$ |
| $U(\mathbb{B})=S^{1}\cdot S^{3}$ | Product decomposition with $S^{1}\cap S^{3}=\{\pm e_0\}$ |
| $T^{2}\cong S^{1}\times S^{1}$ | Central maximal torus |
| $U(\mathbb{B})/T^{2}\cong P^{1}\cong S^{2}$ | Complete flag variety |
| $\tilde{A}=\tilde{U}\tilde{P}$ | Polar decomposition; retraction onto $U(\mathbb{B})$ |
| $\mathbb{B}^{\times}\simeq U(\mathbb{B})\simeq S^{1}\times S^{3}$ | Homotopy type of the unit group |
| $\mathbb{B}^{\times}_1\simeq S^{3}$ | Homotopy type of the norm-one group |
| $N:U(\mathbb{B})\to S^{1}$, kernel $S^{3}$ | Determinant/norm; $U(\mathbb{B})/S^{3}\cong S^{1}$ |
| $\Theta_{\tilde{U}}:\mathbb{M}_{+}\to\mathbb{M}_{+}$, kernel $U(1)$ | $U(\mathbb{B})/U(1)\cong SO(3)$ |
| $\widetilde{\mathbb{B}^{\times}}\cong\mathbb{R}\times S^{3}$ | Universal cover of the unit group |

## Further Reading

- *The Biquaternion Unit Group as a Topological Group* (`articles_maths/the-biquaternion-unit-group-as-a-topological-group.md`), for the bilinear-side treatment of the group of units
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the ambient Euclidean structure the retractions use
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the form that defines the unitary slice
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the Hermitian cone and the positive square root
- *Biquaternion Lie Group and Exponential Structure* (`articles_maths/biquaternion-lie-group-and-exponential-structure.md`), for the subgroups and the real forms
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd edition (Springer, 2015), for the standard facts about $U(2)$, $SU(2)$ and their quotients
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the double covers of the rotation groups
