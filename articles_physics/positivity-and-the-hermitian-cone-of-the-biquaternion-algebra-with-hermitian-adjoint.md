# __Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

The physics of the framework is written with one operator and one cone. The operator is the dagger sandwich $\Theta_{\tilde{Q}}(\tilde T)=\tilde{Q}\tilde T\tilde{Q}^{\dagger}$, and its value at the identity, $\Theta_{\tilde{Q}}(e_0)=\tilde{Q}\tilde{Q}^{\dagger}$, is the **state** prepared by the amplitude $\tilde{Q}$: the density matrix of the Born rule (*Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, *Completely Positive Maps of the Biquaternion Algebra with Hermitian Adjoint*). The cone is the set of those states, the positive semidefinite Hermitian elements of the informational sector, over which the channels are defined and inside which the Bloch ball sits (*The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, *The Bloch Ball as the Trace-One Slice of the Future Light Cone*).

This article is the physics companion of *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* of the mathematical series, where the positivity of the involution, the cone, the polar decomposition and the Cartan involution are proved with their algebra. Here the same objects are read physically: the involution is the Hilbert-space structure of the internal space, the cone is the state cone, the polar decomposition is the amplitude split into modulus and phase, and the Cartan involution is the internal conjugation whose fixed set is the internal symmetry group. The result that makes the reading possible, and the one trap it must not fall into, are stated first.

## Positivity is the Hilbert-Space Structure

**Theorem (the dagger is positive).** For every biquaternion $\tilde{Q}$,

$$
\mathrm{Sc}\bigl(\tilde{Q}^{\dagger}\tilde{Q}\bigr)=\sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2}\ \ge0 ,
$$

with equality only at $\tilde{Q}=0$; so the dagger is a positive involution and the scalar form $(\tilde R,\tilde T)=\mathrm{Sc}(\tilde R^{\dagger}\tilde T)$ is positive definite.

**Physical reading.** The internal space has a positive definite inner product, hence a Hilbert-space structure, and the positivity is the statement that no amplitude has negative norm. The quantity $\mathrm{Sc}(\tilde{Q}^{\dagger}\tilde{Q})$ is the squared Hilbert–Schmidt length of the amplitude, and the pairing $(H,K)=\mathrm{Sc}(HK)$ between two Hermitian elements is the **trace pairing of observables and states**: the expectation value of the observable $H$ in the state $K$, up to the trace. This is the internal form of the framework, and every statement of positivity, of the state cone and of the Bloch ball is a statement about it.

**The trap: positivity does not require a definite norm.** The biquaternion norm $N(\tilde{Q})=\sum_\mu Q_\mu^{2}$ is complex and indefinite, and its vanishing on the null cone is the light cone of the material sector (*Biquaternion Norm and Invertibility*, *The Clifford Structure of the Biquaternion Algebra*). It is tempting to conclude that the framework cannot be a quantum theory because its norm is not positive. The conclusion is wrong, and the reason is exact: $N$ and the scalar form belong to two different structures on the one algebra. The dagger of $\mathbb{B}$ is not the Clifford conjugation of the Minkowski structure but the **reversion** of the positive definite structure $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, and a positive definite Clifford form gives its cone through reversion, not through conjugation — the exchange of sides recorded in *Positivity and the Hermitian Cone of a Clifford Algebra with Hermitian Adjoint*. Positivity of the internal form and indefiniteness of the interval are therefore compatible statements about the same algebra, and using either one where the other belongs is the standard error of the framework.

## The State Cone

**Theorem (the cone).** The set of squares

$$
P=\bigl\{\tilde{Q}^{\dagger}\tilde{Q}:\tilde{Q}\in\mathbb{B}\bigr\}=\bigl\{\tilde{Q}\tilde{Q}^{\dagger}:\tilde{Q}\in\mathbb{B}\bigr\}
$$

is the cone of positive semidefinite Hermitian elements, the **state cone** of the informational sector. It is a closed convex cone of real dimension four, pointed, generating the sector, and self-dual for the trace pairing.

**Physical reading.** The elements of $P$ are exactly the (unnormalised) **states**: positive semidefinite Hermitian operators, of real dimension four as a cone, whose trace-one slice is the Bloch ball of the two-state system. The square root in the identity $H=H^{1/2}(H^{1/2})^{\dagger}$ says that every state is prepared by an amplitude, which is the Born rule read backwards: the map $\tilde{Q}\mapsto\tilde{Q}\tilde{Q}^{\dagger}$ is onto the state cone. Self-duality is the statement that an observable is positive exactly when it has non-negative expectation in every state — the operational definition of a positive observable.

**Corollary (interior, boundary and pure states).** The interior of the cone is the set of positive definite elements,

$$
P^{\circ}=\bigl\{\tilde{Q}\tilde{Q}^{\dagger}:N(\tilde{Q})\neq0\bigr\}=\bigl\{\tilde{Q}\tilde{Q}^{\dagger}:\tilde{Q}\ \text{invertible}\bigr\},
$$

the **faithful** (full-rank) states, prepared by the amplitudes that are not null; the boundary consists of the rank-one states prepared by the null amplitudes, which are the **pure** states.

**Physical reading.** The causal structure of the state space is the cone: a state is faithful iff its amplitude is invertible, iff it lies off the null cone, iff it is prepared by a non-null amplitude. The boundary states are the pure states; in the matrix model they are the outer products $vv^{\dagger}$ of a spinor and its conjugate, parametrised up to a complex scalar by the projective line $\mathbb{P}^{1}(\mathbb{C})$, which is the Bloch sphere of the two-state system and the celestial sphere of the material sector at once (*Biquaternion Topology*, *Exercise: the Bloch Ball and the Geometry of Mixed States*). The cone's extreme rays are those pure states, so the convex geometry of the state space is the geometry of the pure states it generates.

**Remark (the two cones, again).** The cone of this article is the **future light cone** of the interval form on the informational sector: writing $H=te_0+i\mathbf{u}$ with real $t$ and $\mathbf{u}$, the condition is $t\ge\lvert\mathbf{u}\rvert$, of which the trace-one slice is the Bloch ball (*The Bloch Ball as the Trace-One Slice of the Future Light Cone*). The *isotropic cone* of the sector — the null set $t^{2}=\lvert\mathbf{u}\rvert^{2}$ — is the boundary of that cone together with its reflection, and it is the set of pure states read without the sign of the time component. The state cone is one half of the light cone of the informational sector, closed up at the apex; it is not the light cone of the material sector, which is a cone in a different subspace.

## The Amplitude, Its Modulus and Its Phase

**Theorem (the polar decomposition).** Every amplitude factorises as

$$
\tilde{Q}=U\lvert\tilde{Q}\rvert,
\qquad
\lvert\tilde{Q}\rvert=\bigl(\tilde{Q}^{\dagger}\tilde{Q}\bigr)^{1/2}\in P,
\qquad
U^{\dagger}U=e_0,
$$

with $\lvert\tilde{Q}\rvert$ a positive Hermitian element and $U$ unitary; the factorisation is unique exactly when $N(\tilde{Q})\neq0$, that is off the null cone.

**Physical reading.** The amplitude splits into a **modulus**, which is a state — modulo the normalisation, the state the amplitude prepares — and a **phase**, which is a unitary. The identity $N(\lvert\tilde{Q}\rvert)=\lvert N(\tilde{Q})\rvert\ge0$ makes the point exactly: the modulus is a positive element of the informational sector, and its norm there is the absolute value of the interval. Off the null cone the split is unambiguous and the phase is a well-defined unitary; on the null cone the modulus is a rank-one state and the phase is not defined, which is the operator form of the statement that a null amplitude prepares a pure state and carries no invariant phase. The polar element representation of the corpus separates the same amplitude into scale, central phase, boost and rotor (*Biquaternion Polar Element Representation*); the two factorisations exist on the same set — the algebra with the null cone removed — and differ in which unitaries the phase is allowed to be, the dagger decomposition allowing the whole internal group $U(2)$.

## The Internal Conjugation

**Definition.** The **Cartan involution** of the group of units is

$$
\theta(\tilde{Q})=\bigl(\tilde{Q}^{\dagger}\bigr)^{-1}.
$$

**Proposition (definition and fixed set).** $\theta$ is an automorphism of order two of $\mathbb{B}^{\times}=GL(2,\mathbb{C})$, its fixed set is exactly the internal symmetry group of the module,

$$
\theta(\tilde{Q})=\tilde{Q}\iff\tilde{Q}\in U=U(2),
$$

and its differential is $-{}^{\dagger}$, positive on the generators (the material sector) and negative on the observables (the informational sector).

**Physical reading.** The internal conjugation is the operation that inverts an amplitude and conjugates it, and the group it fixes is the internal symmetry group: an amplitude is its own internal conjugate exactly when it is a symmetry. The Lie-theoretic form is the Cartan decomposition

$$
\mathfrak{gl}(2,\mathbb{C})=u(2)\oplus H_2(\mathbb{C}),
\qquad
[\mathbb{M}_-,\mathbb{M}_-]\subseteq\mathbb{M}_-,\quad
[\mathbb{M}_-,\mathbb{M}_+]\subseteq\mathbb{M}_+,\quad
[\mathbb{M}_+,\mathbb{M}_+]\subseteq\mathbb{M}_- :
$$

the generators close on themselves, the observables are rotated by the generators, and the commutator of two observables is a generator. At the group level every invertible amplitude is a symmetry times the exponential of an observable, $\mathbb{B}^{\times}=U(2)\cdot\exp(\mathbb{M}_+)$, and the quotient is the space of faithful states, $\mathbb{B}^{\times}/U(2)\cong P^{\circ}$. The internal conjugation is the symmetry that makes the state space a symmetric space, with the faithful states as its points and the internal group as its isometries.

**Remark (the trap of the real-quaternion slice).** On the real-quaternion slice the dagger is the quaternion conjugation, so $\tilde{Q}^{\dagger}\tilde{Q}=N(\tilde{Q})e_0$ is a real scalar and the modulus is a multiple of the identity: the state prepared by such an amplitude is proportional to the identity, that is unpolarised. The slice meets the state cone in the single ray $\mathbb{R}_{\ge0}e_0$, and on it the Cartan involution is $\tilde{Q}\mapsto\tilde{Q}/N(\tilde{Q})$, not the conjugation of the quaternions. Neither the state cone nor the internal conjugation restricts to the slice as it stands: they are operations of the full complexification, and a reader who fixes the real-quaternion slice first will misread both.

## Summary

The dagger of the biquaternion algebra is a **positive involution**: $\mathrm{Sc}(\tilde{Q}^{\dagger}\tilde{Q})=\sum_\mu\lvert Q_\mu\rvert^{2}$ is strictly positive off zero, so the internal space is a Hilbert space and $(H,K)=\mathrm{Sc}(HK)$ is the trace pairing of observables and states. This is compatible with the indefiniteness of the **interval** $N$, which belongs to the Minkowski structure and not to the internal one: the dagger is the reversion of the positive definite Clifford structure $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, and the exchange of sides is exactly what makes positivity hold. The **state cone** $P=\{\tilde{Q}^{\dagger}\tilde{Q}\}=\{\tilde{Q}\tilde{Q}^{\dagger}\}$ is the positive semidefinite Hermitian cone, the cone of unnormalised states, of real dimension four, self-dual for the trace pairing, with the **faithful** states as interior and the **pure** states — the rank-one outer products $vv^{\dagger}$, parametrised by $\mathbb{P}^{1}(\mathbb{C})$ — as boundary. In the interval form of the informational sector it is the forward light cone $t\ge\lvert\mathbf{u}\rvert$, whose trace-one slice is the Bloch ball; it is not the isotropic cone, which is its boundary together with its reflection.

Every amplitude factorises as $\tilde{Q}=U\lvert\tilde{Q}\rvert$, a **phase** times a **modulus**, the modulus positive and of norm $\lvert N(\tilde{Q})\rvert$, the decomposition unique exactly off the null cone; a null amplitude prepares a pure state and carries no invariant phase. The **internal conjugation** $\theta(\tilde{Q})=(\tilde{Q}^{\dagger})^{-1}$ is an automorphism of order two of the group of units with fixed set the internal symmetry group $U(2)$ and differential $-{}^{\dagger}$, and its eigen-decomposition is the Cartan decomposition $\mathfrak{gl}(2,\mathbb{C})=u(2)\oplus H_2(\mathbb{C})$ with the three bracket inclusions; at the group level $\mathbb{B}^{\times}=U(2)\cdot\exp(\mathbb{M}_+)$ and $\mathbb{B}^{\times}/U(2)\cong P^{\circ}$, the faithful states. The real-quaternion slice is the exceptional case for both constructions: there the modulus is a scalar and the conjugation is not the quaternionic one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{M}_+,\mathbb{M}_-$ | Informational (observables) and material (generators) sectors |
| $\mathrm{Sc}(\tilde{Q}^{\dagger}\tilde{Q})=\sum_\mu\lvert Q_\mu\rvert^{2}$ | Positivity; the internal Hilbert-space form |
| $(H,K)=\mathrm{Sc}(HK)$ | Trace pairing of observables and states |
| $P=\{\tilde{Q}^{\dagger}\tilde{Q}\}=\{\tilde{Q}\tilde{Q}^{\dagger}\}$ | State cone; positive semidefinite Hermitian elements |
| $P^{\circ}=\{N(\tilde{Q})\neq0\}$ | Faithful states; prepared by invertible amplitudes |
| $vv^{\dagger}$ up to scalar | Pure states; $\mathbb{P}^{1}(\mathbb{C})$; Bloch sphere |
| $t\ge\lvert\mathbf{u}\rvert$ | The state cone as the forward light cone; Bloch ball at trace one |
| $\tilde{Q}=U\lvert\tilde{Q}\rvert$ | Amplitude as phase times modulus; unique off the null cone |
| $\theta(\tilde{Q})=(\tilde{Q}^{\dagger})^{-1}$ | Internal conjugation; fixed set $U(2)$ |
| $\mathbb{B}^{\times}=U(2)\cdot\exp(\mathbb{M}_+)$ | Symmetry times observable; faithful states as the quotient |

## Further Reading

- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), the mathematical companion, for the positivity of the involution, the cone, the polar decomposition and the Cartan involution.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* (`articles_physics/the-hermitian-subspace-m-plus-as-the-informational-sector.md`), for the observables, the state cone and the trace-one slice.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* (`articles_physics/the-anti-hermitian-subspace-m-as-the-material-sector.md`), for the four-vectors, the generators and the interval.
- *The Bloch Ball as the Trace-One Slice of the Future Light Cone* (`articles_physics/the-bloch-ball-as-the-trace-one-slice-of-the-future-light-cone.md`), for the state space, its pure points and its geometry.
- *Exercise: the Bloch Ball and the Geometry of Mixed States* (`articles_physics/exercise-the-bloch-ball-and-the-geometry-of-mixed-states.md`), for the worked geometry of the state cone.
- *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_physics/two-sided-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the sandwich, the amplitude-to-state map and the observables.
- *Completely Positive Maps of the Biquaternion Algebra with Hermitian Adjoint* (`articles_physics/completely-positive-maps-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the channels defined over the state cone.
- *Biquaternion Polar Element Representation* (`articles_maths/biquaternion-polar-element-representation.md`), for the other factorisation of an amplitude.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the interval, the null cone and the invertibility criterion.
- *The Clifford Structure of the Biquaternion Algebra* (`articles_physics/biquaternion-clifford-structure.md`), for the two Clifford structures and the identification of the dagger with the Euclidean reversion.
