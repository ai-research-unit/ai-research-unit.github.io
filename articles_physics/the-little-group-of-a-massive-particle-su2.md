# __The Little Group of a Massive Particle: $\mathrm{SU}(2)$__

## Introduction

A massive particle's little group is the set of Lorentz transformations that leave its momentum alone. In the rest frame the momentum is $(m,\vec 0)$ and the condition "leave it alone" is "do not boost": the little group is the rotation group, and in this algebra it is $SU(2)$ exactly, with no double cover needed, because the group the block works with is already the cover.

This article identifies the little group, defines the spin label from its representations, computes the Wigner rotation that a general transformation produces, states its cocycle, and explains what the two-to-one cover does to states.

The article assumes *Wigner's Classification: Two Casimirs, Three Orbits* for the orbit picture, *The Little Group of a Null Momentum: $E(2)$* for the contrast, *The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form* for the cover, and *Why Boosts Are Not Additive: The Bracket Table* for the Thomas–Wigner rotation.

## The Rest Frame

### The Momentum

In the rest frame the four-momentum is

$$
\tilde P_{\mathrm{rest}}=mc\,e_t ,
$$

a real element of the Hermitian slice with zero vector part. Its interval is $q_t^{2}-\lvert\vec q\rvert^{2}=m^{2}c^{2}$, and the corresponding material element $imc\,e_t$ has quaternionic norm $\langle\tilde P\rangle_{\natural}=-m^{2}c^{2}$; the sign is the slice convention of *$P$, $T$ and the Representation Labels*, and nothing here depends on it.

### The Stabiliser

$$
G_{\tilde P_{\mathrm{rest}}}=\{\tilde U\in G:\mathrm{Cg}_{\tilde U}(\tilde P_{\mathrm{rest}})=\tilde P_{\mathrm{rest}}\}.
$$

Since $e_t$ is the identity of the algebra, $\mathrm{Cg}_{\tilde U}(e_t)=\tilde U\tilde U^{*}$, so the condition is simply $\tilde U\tilde U^{*}=e_t$.

### The Identification

The elements satisfying the condition are exactly the **unit-norm quaternions with real components**:

$$
G_{\tilde P_{\mathrm{rest}}}=\{\tilde U\in G:\tilde U=\bar{\tilde U}\}\cong SU(2).
$$

The real unit quaternions are the unit three-sphere $S^{3}$, and $S^{3}$ as a group is $SU(2)$.

### Why the Answer Is Not $SO(3)$

The group $G$ of the block *is* the double cover of the Lorentz group, so its compact subgroup is the double cover of the rotation group, which is $SU(2)$. The map to $SO(3)$ is two-to-one, and the kernel is $\{\pm e_t\}$, both of which fix the rest momentum. So the block's little group is $SU(2)$ on the nose, and a reader who expects $SO(3)$ has forgotten which group the block is using.

This is the general pattern: every little group in the block is the *cover* of the corresponding classical little group, and the cover is the one that carries spinors.

## The Spin Label

### The Representations

The irreducible unitary representations of $SU(2)$ are labelled by

$$
j\in\{0,\tfrac12,1,\tfrac32,\dots\},
\qquad
\dim=2j+1,
$$

and the label is the eigenvalue of the Casimir $\vec J^{2}=\hbar^{2}j(j+1)$. That is the spin.

### The Consistency With $C_2$

The Pauli–Lubanski Casimir on the rest frame is $C_2=m^{2}c^{2}\vec S^{2}$, so the spin label derived from the little group and the label derived from the Casimir agree identically. That agreement is the reason the two readings of *$P$, $T$ and the Representation Labels* can be used interchangeably.

### The Counting

Each momentum has $2j+1$ states, and each state is labelled by the eigenvalue of $J_z$ along a chosen axis. So the fibre over the orbit is $(2j+1)$-dimensional, and the module is the space of sections of that fibre bundle.

### The Values in the Block

| $j$ | dimension | carrier in the algebra |
|---|---|---|
| $0$ | $1$ | the centre $Z=\mathbb{C}e_t$ |
| $\tfrac12$ | $2$ | the Peirce planes $S_\pm$ |
| $1$ | $3$ | the traceless part $V$ |

The table is the carrier list of *The Determination of the Possible Spins in Biquaternionic Form*: the algebra's own modules realise the first three spins of the little group and no more, because the regular module is four-dimensional.

## The Wigner Rotation

### The Definition

Choose for each momentum $\tilde P$ a **standard boost** $L_{\tilde P}$ taking the rest momentum to it. For a Lorentz transformation $\Lambda$, define

$$
W(\Lambda,\tilde P)=L_{\Lambda\tilde P}^{-1}\,\Lambda\,L_{\tilde P}.
$$

By construction it takes the rest momentum to itself:

$$
W(\Lambda,\tilde P)\,\tilde P_{\mathrm{rest}}=\tilde P_{\mathrm{rest}},
$$

so it is an element of the little group. That element is the **Wigner rotation**.

### The Computation

The computation is verified numerically with the block's own model. Take a random momentum, a random transformation, and the standard boost reconstructed from the transformed momentum; then the Wigner element comes out real, of unit norm, and stabilising the rest momentum, to machine precision in every sample. Its rotation angle comes out between $0$ and $\pi$, and its quaternion scalar part is $\cos(\theta_{\mathrm{wgn}}/2)$ with $\theta_{\mathrm{wgn}}$ its rotation angle.

### Why It Is a Rotation and Not a Boost

A transformation that maps a momentum to itself in the rest frame cannot boost, because a boost changes the momentum's length's direction in the time-space plane. So the stabiliser is compact, and the Wigner element is a rotation by construction — the construction forces it, and the numerical check confirms that the force works.

### What It Does

The Wigner rotation is the frame-dependent part of a Lorentz transformation's effect on a spinning state. A state is defined relative to the standard frame at its momentum; after the transformation the new momentum has its own standard frame, and the two standard frames differ by exactly $W$. So the spin is transported around the orbit by $W$.

### The Thomas Precession

The Wigner rotation for a sequence of boosts is the Thomas–Wigner rotation of *Why Boosts Are Not Additive: The Bracket Table*, and the precession of a spin under acceleration is its physical consequence. So the little-group cocycle is the same object as the non-additivity of boosts, seen from the representation side rather than from the group side.

## The Composition

### The Cocycle

For two transformations,

$$
W(\Lambda_2\Lambda_1,\tilde P)=W(\Lambda_2,\Lambda_1\tilde P)\,W(\Lambda_1,\tilde P).
$$

The identity is verified numerically in the same model, to machine precision. It is the statement that the Wigner element is a **cocycle** for the action of the Lorentz group on the orbit, and it is what makes the induced representation a representation: the map $\Lambda\mapsto W(\Lambda,\tilde P)$ is not a homomorphism, but it is a homomorphism up to the momentum-dependent factor that the next transformation absorbs.

### Why It Is Not a Homomorphism

A naive reader expects $W(\Lambda_2\Lambda_1)=W(\Lambda_2)W(\Lambda_1)$, and it fails because the standard frames at $\tilde P$ and at $\Lambda_1\tilde P$ are different. The failure is the content of the cocycle, and it is the same failure that makes boosts non-additive.

### The Reading

The induced representation can be written

$$
U(\Lambda)|p,\sigma\rangle=\sum_{\sigma'}D_{\sigma\sigma'}\bigl(W(\Lambda,p)\bigr)|\Lambda p,\sigma'\rangle,
$$

and the cocycle identity is exactly what makes $U(\Lambda_2\Lambda_1)=U(\Lambda_2)U(\Lambda_1)$. So the little group's representation $D$ and the cocycle $W$ are the two ingredients, and the group law of the big group holds because the cocycle's defect is absorbed by the fibre's transformation.

### The Frame Dependence

$W$ depends on the choice of standard section $L_{\tilde P}$. Change the section by a little-group element $k(\tilde P)$ and $W$ changes by a coboundary. So the rotation angle is *not* an invariant of $\Lambda$; only the cohomology class is. That is why the Thomas–Wigner angle is frame-dependent and why experiments measure it only against a specified frame convention.

## The Wigner Angle Measured

### The Two-Boost Case

The standard case is a product of two boosts, of rapidities $\theta_{\mathrm{rpd},1}$ and $\theta_{\mathrm{rpd},2}$, whose directions make an angle $\theta$. The product is not a boost when $\theta\neq0$, and its little-group part is a rotation about the normal to the two directions. Its angle $\theta_{\mathrm{wgn}}$ is the Thomas–Wigner angle.

### The Small-Rapidity Limit

For equal small rapidities $\theta_{\mathrm{rpd}}$ and angle $\theta$ between the directions,

$$
\theta_{\mathrm{wgn}}\ \approx\ \tfrac12\,\theta_{\mathrm{rpd}}^{2}\sin\theta ,
$$

which is second order in the rapidity. The value is verified numerically: at $\theta_{\mathrm{rpd}}=0.05$ and $\theta=\pi/2$ the measured angle is $1.24948\times10^{-3}$ against $\theta_{\mathrm{rpd}}^{2}/2=1.25\times10^{-3}$, and the ratio tends to one as $\theta_{\mathrm{rpd}}\to0$.

### Why Second Order

A single boost is a pure boost. Two parallel boosts compose into one boost, by the additivity of rapidities along one axis. Two non-parallel boosts fail to compose into a boost, and the failure is a rotation. The failure vanishes to first order because the first-order part of the product is the sum of the two generators, which is again a boost generator; the rotation appears only in the commutator, which is second order. That is the bracket table of *Why Boosts Are Not Additive: The Bracket Table*, and the Wigner angle is its integrated consequence.

### The Large-Rapidity Limit

At large rapidity the angle does not grow without bound: it tends to a value fixed by the geometry, because the product becomes a loxodromic element whose rotation part is bounded. So the Thomas–Wigner angle is a small kinematic effect at ordinary speeds and a bounded one at extreme speeds, which is why it is measured in atomic fine structure and in the precession of orbiting gyroscopes rather than in high-energy collisions.

### What It Measures

The angle is the difference between "boost then rotate" and "rotate then boost". A measurement of the Thomas precession therefore measures the non-commutativity of the boost generators, that is, the structure constant of the bracket table, and not any dynamical quantity. That is why it is present for a free particle with no forces acting on its spin.

## The Fibre and Its Transformation

### The States

A state of the massive module is a section of the fibre bundle whose fibre over $\tilde P$ is the spin-$j$ module $V_j$. In the rest frame's trivialisation a state is a vector $v\in V_j$, and a general state is $(v,\tilde P)$ modulo the little group's action.

### The Action on the Fibre

Under a Lorentz transformation the momentum moves and the vector is transformed by the little-group element:

$$
(v,\tilde P)\longmapsto\bigl(D(W(\Lambda,\tilde P))\,v,\ \Lambda\tilde P\bigr).
$$

So the fibre's transformation is not $\Lambda$'s action on $V_j$ — that action does not exist, since $V_j$ is a representation of the little group and not of the whole Lorentz group. It is $W$'s action, and the Wigner rotation is what makes the statement consistent.

### The Invariance

$D(W)$ is unitary because $W$ is in the compact group $SU(2)$, so the fibre's inner product is preserved by every transformation. That is why the massive module is unitary even though the finite-dimensional Lorentz representations are not: the fibre only ever sees the compact part.

## The Two-to-One Cover

### The Kernel

$\{\pm e_t\}$ acts trivially on momentum — both elements fix every momentum — and on the spin-$j$ fibre it acts as $(-1)^{2j}$. So the little group's action on states is two-to-one for half-integer spin and one-to-one for integer spin.

### What It Means for States

A rotation by $2\pi$ is the element $-e_t$. On a spin-$\tfrac12$ state it gives $-1$; on a spin-$1$ state it gives $+1$. So a spinor state is not a function on the rotation group but a section of a nontrivial bundle over it, and the sign is observable in interference, not in probabilities.

### The Observable

The sign flip is measurable when two paths in the rotation group are compared: one that returns by $2\pi$ and one that returns by $4\pi$. The two give amplitudes of opposite sign and the interference pattern differs. That is the neutron interferometry experiment, and it is the physical verification that the little group is $SU(2)$ and not $SO(3)$.

### The Consistency of the Block

The block uses $SU(2)$ as the little group throughout, and its two-to-one relation to the rotation group is the same two-to-one relation that *The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form* describes for the whole Lorentz group. There is one cover, not two, and the little group's is its restriction.

## Summary

A massive particle's little group is the stabiliser of its momentum, and in the rest frame that stabiliser is the set of real unit quaternions, which is $SU(2)$ exactly because the block's group is already the double cover. Its irreducible representations give the spin label $j$ with $2j+1$ states, in agreement with the Pauli–Lubanski Casimir's value. A general Lorentz transformation produces a Wigner rotation $W=L_{\Lambda p}^{-1}\Lambda L_p$ in the little group, verified numerically to be a rotation that fixes the rest momentum, and it satisfies the cocycle identity $W(\Lambda_2\Lambda_1)=W(\Lambda_2,\Lambda_1p)W(\Lambda_1)$, which is what makes the induced representation a representation. The kernel $\{\pm e_t\}$ acts as $(-1)^{2j}$, so half-integer states are two-valued and the sign is observable in interference.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P_{\mathrm{rest}}=mc\,e_t$ | the rest momentum |
| $G_{\tilde P}$ | the little group, here $SU(2)$ |
| $L_{\tilde P}$ | the standard boost section |
| $W(\Lambda,\tilde P)$ | the Wigner rotation |
| $j$ | the spin label |
| $\{\pm e_t\}$ | the kernel of the cover |

## Further Reading

- E. P. Wigner, "On unitary representations of the inhomogeneous Lorentz group", *Annals of Mathematics* 40 (1939) 149 — the little group and the spin label.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1, Cambridge University Press, 1995, §2.5 — the Wigner rotation and its cocycle in the physicist's notation.
- H. Rauch et al., "Verification of coherent spinor rotation of fermions", *Physics Letters A* 54 (1975) 425 — the $4\pi$ periodicity measured with neutrons.
- *Why Boosts Are Not Additive: The Bracket Table* — the Thomas–Wigner rotation from the group side.
- *The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form* — the cover whose restriction is this little group.
- *The Determination of the Possible Spins in Biquaternionic Form* — the carrier table that realises $j=0,\tfrac12,1$.
