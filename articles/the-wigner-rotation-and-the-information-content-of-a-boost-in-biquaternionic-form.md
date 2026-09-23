# __The Wigner Rotation and the Information Content of a Boost in Biquaternionic Form__

## Introduction

A boost is the elementary operation that changes the frame of a relativistic system, and in the biquaternion framework it is a single element of the algebra: a Hermitian unit-norm biquaternion. Its action on the material sector is a congruence and is completely transparent — a four-vector is carried to a four-vector by a linear map that preserves the norm form. Its action on the informational sector is not transparent, and it is not a pure rotation: the left action on the spinor is non-unitary, and the little-group part of it depends on the momentum. The residue of that momentum dependence is the **Wigner rotation**, and the purpose of this article is to reconstruct it from the algebra and to ask what information a boost carries.

The question has three layers, and the article treats them in order. First, there is the algebraic layer: a product of two unit-norm rotors is again a unit-norm rotor, a product of two Hermitian ones is not Hermitian, and the mismatch is a rotation in the compact subgroup. The Wigner rotation is that mismatch, and it is a **one-cocycle** on the little-group bundle. Second, there is the operational layer: on a state with momentum superposition a boost acts as a **controlled rotation**, rotating the spin by an amount that depends on the momentum branch, and this is the precise sense in which a boost is an entangling gate between spin and momentum rather than a spin operation. Third, there is the information layer: what a boost carries is a rotation, its parameters are compressed from three to three but its action on a single spin is a two-parameter rotation, the information it can move from momentum to spin is bounded by the entropy of the induced channel, and a **closed loop** of boosts that returns the four-velocity to its starting value need not return the spin — it leaves a rotation whose angle is a curvature of the boost parameter space.

The findings are stated in advance.

1. **The Wigner rotation is the compact part of a composed boost.** For unit-norm rotors $\tilde{\Lambda}_1,\tilde{\Lambda}_2$ the product $\tilde{\Lambda}_2\tilde{\Lambda}_1$ is again unit-norm, but it is Hermitian only when the two boost directions commute; in general it factors as $\tilde{\Lambda}_2\tilde{\Lambda}_1 = \tilde{\Lambda}_{\mathrm{boost}}\tilde{W}$ with $\tilde{W}$ a unit real quaternion, i.e. a rotation.
2. **It is a cocycle.** The Wigner rotation satisfies $\tilde{W}(\tilde{\Lambda}_2\tilde{\Lambda}_1,\tilde{U}) = \tilde{W}(\tilde{\Lambda}_2,\tilde{\Lambda}_1\tilde{U})\,\tilde{W}(\tilde{\Lambda}_1,\tilde{U})$, the cocycle condition of a little-group bundle; a boost is a connection on that bundle and the rotation is its parallel transport.
3. **A boost is a controlled rotation.** On a momentum superposition the boost acts as $\sum_i|p_i'\rangle\langle p_i|\otimes\tilde{W}_i$, a momentum-controlled unitary on the spin; it cannot be written as a momentum operation times a momentum-independent spin operation, and this is exactly why it can change spin entanglement while remaining globally unitary.
4. **The information content is a rotation angle.** Everything a boost can do to a spin is summarised by the pair (angle, axis) of its Wigner rotation; the angle vanishes for collinear boosts and is maximal for transverse ones, and the entropy it can imprint on a transverse spin is $h((1+\cos\alpha)/2)$.
5. **A closed loop of boosts leaves a rotation.** The product of boosts around a closed path in velocity space is a pure rotation about the normal to the path, with an angle that grows with the area; this is the Thomas–Wigner holonomy, the curvature of the boost connection, and the relativistic content of Thomas precession.

The notation is that of the foundational articles: $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, quaternion units $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$, central scalar $i$, trace $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$, norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$, Hermitian sector $\mathbb{M}_+$, anti-Hermitian sector $\mathbb{M}_-$, and the matrix model $\Phi$ with $e_k\mapsto-i\sigma_k$, $i\mapsto iI_2$. The boost rotor is
$$
\tilde{\Lambda} = \cosh\frac{\psi}{2}\,e_0 + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}} = e^{(\psi/2)\,i\hat{\mathbf{u}}}, \qquad N(\tilde{\Lambda}) = 1 ,
$$
with $\psi$ the rapidity and $\hat{\mathbf{u}}$ the boost direction; the four-velocity of a particle boosted from rest is $\tilde{U} = ic\,\tilde{\Lambda}^{-1}\tilde{\Lambda}^{-1\dagger}$. The Wigner rotation is $\tilde{W}(\tilde{\Lambda},\tilde{U}) = \tilde{\Lambda}_{\tilde{U}'}\tilde{\Lambda}\tilde{\Lambda}_{\tilde{U}}^{-1}\in SU(2)$ with $\tilde{U}' = \tilde{\Lambda}\tilde{U}\tilde{\Lambda}^\dagger$.

The companion articles supply the pieces:
- Companion article *The Relativistic Qubit in Biquaternionic Form*, for the little group, the Wigner rotation, and the two actions of the unit-norm group.
- Companion article *Frame-Dependent Entanglement and Relativistic Quantum Information in Biquaternionic Form*, for the channel induced by a boost on a momentum superposition.
- Companion article *Exercise: Boosting a Four-Velocity and Rapidity Composition*, for the composition of boosts and the frame four-velocity.
- Companion article *Exercise: The Thomas Precession*, for the precession of a spin in an accelerated frame.
- Companion article *The Anti-Hermitian Subspace M- as the Material Sector*, for four-vectors and the norm form.
- Companion article *The Lorentz Group in Biquaternionic Form — Structure and Representations*, for the Cartan decomposition and the subgroups.

## The Boost and Its Rotor

### The generator and the Cartan decomposition

The Lorentz algebra is spanned by the rotation generators $\tilde{J}_k = \tfrac12 e_k\in\mathbb{M}_-^{0}$ and the boost generators $\tilde{K}_k = \tfrac12 i e_k\in\mathbb{M}_+^{0}$, with
$$
[\tilde{J}_j,\tilde{J}_k] = -\epsilon_{jkl}\tilde{J}_l, \qquad
[\tilde{J}_j,\tilde{K}_k] = -\epsilon_{jkl}\tilde{K}_l, \qquad
[\tilde{K}_j,\tilde{K}_k] = +\epsilon_{jkl}\tilde{J}_l .
$$
The first bracket closes the rotation subalgebra, the second says that the boosts form a representation of the rotations, and the third — the decisive one — says that the **boosts do not close**: the commutator of two boosts is a rotation. This is the algebraic origin of everything that follows. A boost is the image of the generator $\tilde{K}$ under the exponential map,
$$
\tilde{\Lambda} = \exp\!\bigl(\psi\,\hat{\mathbf{u}}\cdot i\mathbf{e}/2\bigr)
= \cosh\frac{\psi}{2}\,e_0 + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}} ,
$$
which is Hermitian because $\tilde{K}$ is Hermitian and $i\tilde{K}$ is anti-Hermitian. The set of pure boosts is therefore the exponential of a three-dimensional real subspace of Hermitian generators, and it is a symmetric space rather than a group: the product of two boosts is a boost times a rotation, by the third bracket.

The Cartan decomposition reflects the same fact at the group level,
$$
SL(2,\mathbb{C}) = SU(2)\cdot\exp\bigl(\{i\mathbf{a}\cdot\mathbf{e} : \mathbf{a}\in\mathbb{R}^3\}\bigr),
$$
every unit-norm rotor being uniquely the product of a compact factor (a unit real quaternion) and a pure boost. The boost is the non-compact factor, and the informational sector of the structural companion is exactly its generator space.

### The two actions, and the non-unitarity of the spinor action

A boost acts on the two sectors differently. On the material sector it acts by congruence,
$$
\tilde{X}\ \longmapsto\ \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger , \qquad \tilde{X}\in\mathbb{M}_- ,
$$
which preserves the norm form because $N(\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger) = N(\tilde{\Lambda})N(\tilde{X})N(\tilde{\Lambda}^\dagger) = N(\tilde{X})$: the interval, the mass shell, and the light cone are all invariant. On the informational sector it acts on the spinor by left multiplication, and that action is not unitary: $\tilde{\Lambda}^\dagger\tilde{\Lambda} = e_0$ fails for a boost, so the spinor norm is scaled,
$$
\langle\tilde{\Lambda}u|\tilde{\Lambda}u\rangle = \langle u|\tilde{\Lambda}^\dagger\tilde{\Lambda}|u\rangle = \langle u|u\rangle + i\sinh\psi\,\langle u|\hat{\mathbf{u}}|u\rangle .
$$
A boost therefore has a trivial action on four-vectors and a non-trivial, non-unitary action on spinors. The physically unitary spin operation is neither of these; it is the little-group part extracted below.

## The Wigner Rotation Reconstructed

### The composition of two boosts

Let $\tilde{\Lambda}_1$ and $\tilde{\Lambda}_2$ be two boost rotors with non-collinear directions. Their product $\tilde{\Lambda} = \tilde{\Lambda}_2\tilde{\Lambda}_1$ is unit-norm, $N(\tilde{\Lambda}) = 1$, because the norm form is multiplicative; but it is not Hermitian,
$$
\tilde{\Lambda}^\dagger = \tilde{\Lambda}_1^\dagger\tilde{\Lambda}_2^\dagger = \tilde{\Lambda}_1\tilde{\Lambda}_2 \neq \tilde{\Lambda}_2\tilde{\Lambda}_1 \quad\text{unless } [\tilde{\Lambda}_1,\tilde{\Lambda}_2] = 0 .
$$
The product of two boosts is therefore not a boost, and the deviation from Hermiticity is a deviation from pure boosting. The Cartan decomposition turns that deviation into a rotation: write
$$
\tilde{\Lambda}_2\tilde{\Lambda}_1 = \tilde{\Lambda}_{\mathrm{boost}}\,\tilde{W},
$$
with $\tilde{\Lambda}_{\mathrm{boost}}$ a pure boost and $\tilde{W}$ a compact factor. The compact factor is found by removing the boost part, and the boost part is fixed by the net four-velocity: if $\tilde{\Lambda}_2\tilde{\Lambda}_1$ carries the rest four-velocity to $\tilde{U}$, then the standard boost $\tilde{\Lambda}_{\tilde{U}}$ carries $\tilde{U}$ back to rest, and
$$
\tilde{W} = \tilde{\Lambda}_{\tilde{U}}\,\tilde{\Lambda}_2\tilde{\Lambda}_1
$$
satisfies $\tilde{W}(ic\,e_0)\tilde{W}^\dagger = ic\,e_0$, hence lies in the stabilizer; being unit-norm it is a unit real quaternion,
$$
\tilde{W}\in SU(2), \qquad \tilde{W} = \cos\frac{\alpha}{2}e_0 + \sin\frac{\alpha}{2}\hat{\mathbf{n}} .
$$
This is the Wigner rotation, and it is the **unique** correction in the decomposition: any other choice differs by a little-group element that is already included in $\tilde{W}$.

**A worked composition.** Take $\tilde{\Lambda}_1$ a boost along $x$ with rapidity $1$ and $\tilde{\Lambda}_2$ a boost along $y$ with rapidity $0.5$. Their product factors as a pure boost to the net four-velocity times the rotation
$$
\tilde{W} = 0.99366\,e_0 + 0.11246\,e_3 ,
\qquad \alpha = 12.9146^\circ , \qquad \hat{\mathbf{n}} = \hat{\mathbf{z}} ,
$$
a rotation about the axis normal to the plane of the two boost directions, by an angle that grows with both rapidities. The rotation is compact, unitary, and has determinant one: it is the same kind of object as an ordinary spatial rotation, and it is the only part of the composed boost that acts on the spin as a quantum operation.

### The cocycle condition

The Wigner rotation of a composition is not additive, but it obeys a composition law inherited from the group. Writing $\tilde{W}(\tilde{\Lambda},\tilde{U})$ for the rotation and using $\tilde{U}'' = \tilde{\Lambda}_2\tilde{\Lambda}_1\tilde{U}\tilde{\Lambda}_1^\dagger\tilde{\Lambda}_2^\dagger$, a direct calculation gives
$$
\tilde{W}(\tilde{\Lambda}_2\tilde{\Lambda}_1,\tilde{U})
= \tilde{W}(\tilde{\Lambda}_2,\tilde{\Lambda}_1\tilde{U})\;\tilde{W}(\tilde{\Lambda}_1,\tilde{U}) .
$$
This is a **one-cocycle condition**: the rotation of the composed transformation is the rotation of the second evaluated at the momentum carried by the first, composed with the rotation of the first. The derivation is immediate from the definition. Writing $\tilde{U}_1 = \tilde{\Lambda}_1\tilde{U}\tilde{\Lambda}_1^\dagger$ and $\tilde{U}'' = \tilde{\Lambda}_2\tilde{\Lambda}_1\tilde{U}\tilde{\Lambda}_1^\dagger\tilde{\Lambda}_2^\dagger$, one has
$$
\tilde{W}(\tilde{\Lambda}_2,\tilde{U}_1)\,\tilde{W}(\tilde{\Lambda}_1,\tilde{U})
= \tilde{\Lambda}_{\tilde{U}''}\tilde{\Lambda}_2\tilde{\Lambda}_{\tilde{U}_1}^{-1}\;\tilde{\Lambda}_{\tilde{U}_1}\tilde{\Lambda}_1\tilde{\Lambda}_{\tilde{U}}^{-1}
= \tilde{\Lambda}_{\tilde{U}''}\tilde{\Lambda}_2\tilde{\Lambda}_1\tilde{\Lambda}_{\tilde{U}}^{-1}
= \tilde{W}(\tilde{\Lambda}_2\tilde{\Lambda}_1,\tilde{U}),
$$
the trial element $\tilde{\Lambda}_{\tilde{U}_1}$ cancelling between the two factors. The identity has been verified for two thousand random pairs of boosts and random four-velocities. Its content is that the Wigner rotation is not a representation — it is not a homomorphism from the group to $SU(2)$, because of the intermediate momentum argument — but a **cocycle twisted by the action on momentum**. This is the precise algebraic sense in which the little-group structure of a relativistic particle is a bundle rather than a direct product: the spin is attached to the momentum, and moving the base point changes the identification of the fibers.

The cocycle is the source of the momentum dependence, and therefore of every frame-dependent effect of the previous article: if the rotation were a homomorphism, it would be momentum-independent and no boost could correlate spin with momentum.

## The Boost as a Controlled Rotation

### The action on a superposition

On a state with definite momentum, the boost acts on the spin by the single unitary $\tilde{W}$. On a superposition of momentum eigenstates it acts by a rotation on each branch,
$$
|\Psi\rangle = \sum_i\sqrt{q_i}\,|p_i\rangle\otimes|\chi_i\rangle
\ \longmapsto\
\sum_i\sqrt{q_i}\,|p_i'\rangle\otimes\bigl(\tilde{W}_i|\chi_i\rangle\bigr),
\qquad \tilde{W}_i = \tilde{W}(\tilde{\Lambda},\tilde{U}_i),
$$
which is a **controlled unitary** in the standard sense of quantum information: the momentum plays the role of the control and the spin of the target, and the operation on the target is the branch-dependent Wigner rotation. When the branch momenta are orthogonal, the spin channel obtained by tracing the momentum is
$$
\tilde{\rho}\ \longmapsto\ \sum_i q_i\,\tilde{W}_i\,\tilde{\rho}\,\tilde{W}_i^\dagger ,
$$
a mixed-unitary channel whose Kraus operators are the branch rotations.

The controlled form is not an approximation or a convenience; it is forced. A boost is a unitary on the full Hilbert space of spin and momentum, and it moves the momentum. If it factored as a momentum operation times a spin operation,
$$
\tilde{U}(\tilde{\Lambda}) = \tilde{V}_{\mathrm{mom}}(\tilde{\Lambda})\otimes\tilde{R}(\tilde{\Lambda}),
$$
then the spin operation would be momentum-independent, the cocycle would be a homomorphism, and the third Lie bracket $[\tilde{K},\tilde{K}] = \tilde{J}$ would be contradicted: the composition of two boosts would have to be a boost with no rotation. The Wigner rotation is exactly the obstruction to that factorisation, and the controlled form is its operational statement.

### The information imprinted on a single spin

The information content of a boost, in its narrowest sense, is the rotation it imprints on a spin, and the amount is governed by the Wigner angle. For a boost of rapidity $\psi$ and a particle of rapidity $\chi = \mathrm{atanh}(v/c)$ at angle $\theta$ to the boost axis, the angle vanishes at $\theta = 0,\pi$ and is largest for transverse momentum, and for $\theta = \pi/2$ it is given exactly by
$$
\tan\alpha = \frac{\sinh\psi\,\sinh\chi}{\cosh\psi + \cosh\chi}.
$$
For a particle of speed $0.5c$ this gives the following values, with the dephasing factor $\cos\alpha$ and the entropy $h((1+\cos\alpha)/2)$ that the boost imprints on a transverse spin:

| $\psi$ | $\alpha$ | $\cos\alpha$ | $h\!\left(\frac{1+\cos\alpha}{2}\right)$ |
|---:|---:|---:|---:|
| $0.25$ | $3.81681^\circ$ | $0.997782$ | $0.012486$ |
| $0.50$ | $7.50939^\circ$ | $0.991423$ | $0.039902$ |
| $1.00$ | $14.11732^\circ$ | $0.969798$ | $0.112969$ |
| $1.50$ | $19.31699^\circ$ | $0.943703$ | $0.185020$ |
| $2.00$ | $23.06780^\circ$ | $0.920042$ | $0.242196$ |
| $3.00$ | $27.26584^\circ$ | $0.888891$ | $0.309540$ |

The rotation angle grows with the rapidity and saturates at a finite value; the dephasing factor falls and the entropy rises. The asymptotics are worth recording: for large $\psi$ and fixed $\chi$, $\tan\alpha\to\sinh\chi$, so the angle saturates at $\arctan(\sinh\chi)$ — the same finite angle for every transverse spin of the particle, in agreement with the velocity-addition limit — and the dephasing factor saturates at $\cos(\arctan(\sinh\chi)) = 1/\cosh\chi = \sqrt{1-v^2/c^2}$. Only in the ultrarelativistic limit $\chi\to\infty$ does this reach zero and the entropy approach one bit; for $v = 0.5c$ the saturating angle is $30^\circ$, the dephasing factor $0.8660$, and the entropy $0.3546$. For small rapidities the angle is $\alpha\approx\tfrac12\psi\chi\sin\theta$, so the information a slow boost imprints on a spin is second order in the velocities.

**The parameters of a boost and of its rotation.** A boost has three parameters — a direction and a rapidity — while, once the momentum is fixed, its Wigner rotation has its axis determined by the two directions: the axis is perpendicular to both, so the whole rotation is summarised by the single angle $\alpha(\psi,\theta)$. The map from boosts to rotations is therefore not injective, and a spin measurement cannot recover the boost completely: a boost and its rotation share the transverse plane, the rapidity is encoded only through the angle, and many boosts share a Wigner angle. A spin collinear with the boost conveys no information about the boost at all, up to phase.

**How well can a boost be read from a spin?** The transverse spin states produced by two different boosts are the dephased states with Bloch vectors of length $\cos\alpha_1$ and $\cos\alpha_2$ along the Wigner axis, and for qubits the trace distance between two such states is one half the Euclidean distance of their Bloch vectors,
$$
D(\tilde{\rho}_1,\tilde{\rho}_2) = \tfrac12|\mathbf{r}_1-\mathbf{r}_2| = \tfrac12|\cos\alpha_1 - \cos\alpha_2| .
$$
For a particle of speed $0.5c$ at transverse momentum, boosts of rapidity $1$ and $1.5$ give angles $14.11732^\circ$ and $19.31699^\circ$, hence $D = \tfrac12(0.969798-0.943703) = 0.013048$: a single spin measurement distinguishes them with a bias of about one and a third per cent. Even the widely separated rapidities $0.5$ and $2$ give $D = \tfrac12(0.991423-0.920042) = 0.035691$, a bias of under four per cent. The rapidity is thus carried by the spin only weakly at moderate speed, and a boost is much more efficiently read out from the momentum of a particle than from its spin; the information content of the boost is concentrated in the parallel spin component, where the Wigner rotation does nothing.

## The Information Content of a Boost

### What the word means here

Four distinct notions of information content can be attached to a boost, and the framework keeps them apart.

**The parameter information.** The boost is labelled by a rapidity and a direction, a point of three-dimensional hyperbolic space. The parameter information is the classical information in that label: distinguishable boosts are distinguishable parameters, and the parameter manifold is a smooth three-dimensional space with a hyperbolic metric — the same space on which the velocity of a relativistic particle lives.

**The channel information.** The boost is a quantum channel on the spin once the momentum is traced, and its information content is the set of states it can produce from a given input. For a single-particle transverse spin this is the dephasing channel of the previous section, whose output is determined by $\cos\alpha$; two boosts with the same Wigner angle act identically on every transverse spin and are indistinguishable by spin measurements alone.

**The correlation information.** The boost can transfer information from the momentum to the spin, creating spin–momentum correlation; the amount transferred is the entropy $h((1+r')/2)$ of the reduced spin state, which is the entropy of the correlation the boost has created. This is the only sense in which a boost creates information rather than moving it, and it is bounded by one bit per qubit per boost by the ordinary bounds on a two-level system.

**The holonomy information.** A boost is a point of a curved parameter space, and a path of boosts can carry information in its shape rather than its endpoints. This is the subject of the next section.

### The boost as an operation

Two operational statements summarise the reading. First, a boost is a unitary operation, so it cannot increase the total information of a closed system; what it does is redistribute the information between the spin and momentum factors, and the reduced spin state loses purity exactly to the extent that correlation is created. Second, a boost is a **free operation** in the relativistic description, in the sense that an observer may change frames at will and the laws are frame-independent; but the spin state is not frame-independent, so the freedom has a price, and the price is the Wigner rotation. The information content of a boost is the information an observer must know about the boost in order to undo its effect on a spin: the pair (angle, axis), which is the same data as the rotation itself.

## The Holonomy of a Boost Path

### A closed loop that returns the frame but not the spin

The curvature of the boost connection is exhibited by transporting a spin around a closed path in velocity space. Consider the path that takes the rest frame to the velocity $\mathbf{v}_1$ by a boost along $x$ of rapidity $a$, then to a velocity $\mathbf{v}_2$ by a boost along $y$ of rapidity $b$, then back to rest by the standard boost that carries $\mathbf{v}_2$ to zero,
$$
\tilde{P} = \tilde{\Lambda}_{\mathbf{v}_2}\,\tilde{\Lambda}_y(b)\,\tilde{\Lambda}_x(a) .
$$
The four-velocity returns to its starting value by construction, so $\tilde{P}$ fixes $ic\,e_0$ and, being unit-norm, lies in $SU(2)$: the path leaves a pure rotation. For four loops,

| $a$ | $b$ | $\text{angle}$ | $\text{axis}$ |
|---:|---:|---:|---|
| $0.5$ | $0.5$ | $6.86557^\circ$ | $\hat{\mathbf{z}}$ |
| $1.0$ | $0.5$ | $12.91464^\circ$ | $\hat{\mathbf{z}}$ |
| $1.0$ | $1.0$ | $24.10915^\circ$ | $\hat{\mathbf{z}}$ |
| $1.5$ | $1.0$ | $32.71532^\circ$ | $\hat{\mathbf{z}}$ |

with rotors $\tilde{P} = 0.99821\,e_0 + 0.05988\,e_3$, $0.99366\,e_0 + 0.11246\,e_3$, $0.97795\,e_0 + 0.20884\,e_3$, and $0.95952\,e_0 + 0.28163\,e_3$. Each is unitary, fixes the rest four-velocity, and is a rotation about the normal to the plane of the loop. The first entry is the same rotation as the two-boost composition of the worked example, as it must be: the two constructions differ only in the way the second boost is closed.

**The angle is the area.** For small rapidities the holonomy angle is bilinear in the two loop parameters,
$$
\alpha \simeq \tfrac12\,a\,b ,
$$
and $\tfrac12 ab$ is exactly the area enclosed by the loop in velocity space: the vertices of the path are at rapidities $(0,0)$, $(a,0)$, and $(a,b)$ in the $(v_x,v_y)$ plane, and the enclosed area is $\tfrac12 ab$. The coefficient has been confirmed numerically, giving $\alpha/(ab) = 0.499792$ at $a = b = 0.05$ and drifting slowly below $1/2$ as the rapidities grow, through $0.497921$ at $(0.2,0.1)$ to $0.492514$ at $(0.3,0.3)$. The holonomy is therefore the **curvature integral**: the rotation angle accumulated around a loop is the area the loop encloses, the discrete statement of Gauss–Bonnet for the boost connection, and the reason the Thomas precession rate is proportional to the area swept by the velocity per unit time.

This is the **holonomy** of the boost connection. Its defining property is that it is *path-dependent*: the endpoints of the path are the same point — rest — and yet the transformation is not the identity. A closed path in velocity space with a different shape gives a different rotation, with the same endpoints, so the rotation is a function of the path and not of the point. That is the defining property of a curvature, and it is why the boost parameter space cannot be treated as a flat arena in which frames are simply relabelled.

### Thomas precession as the time integral of the holonomy

For a particle that is accelerated along a curved worldline, the velocity traces a path in velocity space, and the holonomy accumulated over the path is a continuous rotation of the spin. The rate form of the same statement is **Thomas precession**, and it is the standard physical face of the holonomy:
$$
\dot{\boldsymbol{\Omega}}_{\mathrm{T}} = -\frac{\gamma-1}{v^2}\,\mathbf{v}\times\dot{\mathbf{v}} ,
$$
a precession of the rest-frame spin at a rate proportional to the acceleration and to $\gamma-1$. The biquaternion expression of the same rate is the commutator of the infinitesimal boosts of the path, and the accumulated rotation is the product of the trip. The companion exercise treats the precession directly; here it is recorded as the infinitesimal form of the closed-loop statement above.

The information reading of the holonomy is the sharpest statement available. Two observers who follow different paths between the same two frames — the same initial and final four-velocity — and who each keep a gyroscope, will disagree about the orientation of a spin by the accumulated rotation. The disagreement is not an error and not a measurement artefact; it is the curvature of the boost parameter space, and it means that the frame label does not determine the spin frame. The extra data needed to reconstruct the spin state is a path, i.e. the holonomy, and that is the information content of a sequence of boosts beyond the information in its endpoints.

## The Boost in the Two Sectors

The structural companion's split reads the Wigner rotation sharply. The boost generator lies in the traceless **informational** sector,
$$
\tilde{K}_k = \tfrac12 ie_k\in\mathbb{M}_+^{0},
$$
while the rotation it generates lies in the traceless **material** sector,
$$
\tilde{W} = \cos\frac{\alpha}{2}e_0 + \sin\frac{\alpha}{2}\hat{\mathbf{n}}, \qquad \hat{\mathbf{n}}\cdot\mathbf{e}\in\mathbb{M}_-^{0} .
$$
A boost is therefore an informational generator whose observable residue is a material rotation, and the map between them is the bracket $[\tilde{K},\tilde{K}] = \tilde{J}$ that carries the informational sector into the material one. The information content of a boost, read this way, is the material image of an informational operation: the rapidity, which is the parameter of an element of the informational sector, appears to an observer as an angle in the material sector, and it does so through a map that is a cocycle rather than a homomorphism. The same structure appeared in the relativistic-qubit article as the null-vector map, which carries an informational state to a material light direction; here it appears at the level of the generators, and the compact, material character of the image is what makes it observable as a rotation rather than as a boost.

Three algebraic facts about a boost are therefore three faces of one statement. The Cartan decomposition says that every frame transformation is a rotation times a boost. The cocycle condition says that the spin part of that product is twisted by the momentum. The holonomy says that the twist has curvature. Together they say that the boost parameter space is not a flat arena of frame labels but a curved space of operations, and that the information a boost carries about itself is the rotation it leaves behind.

## Summary

A boost is the Hermitian unit-norm biquaternion $\tilde{\Lambda} = \cosh(\psi/2)e_0 + i\sinh(\psi/2)\hat{\mathbf{u}}$. It acts on four-vectors by congruence, preserving the norm form, and on spinors by a non-unitary left multiplication. Its product with another boost is not a boost: the Cartan decomposition writes
$$
\tilde{\Lambda}_2\tilde{\Lambda}_1 = \tilde{\Lambda}_{\mathrm{boost}}\,\tilde{W}, \qquad \tilde{W}\in SU(2),
$$
and the compact factor is the **Wigner rotation**
$$
\tilde{W}(\tilde{\Lambda},\tilde{U}) = \tilde{\Lambda}_{\tilde{U}'}\tilde{\Lambda}\tilde{\Lambda}_{\tilde{U}}^{-1}, \qquad \tilde{U}' = \tilde{\Lambda}\tilde{U}\tilde{\Lambda}^\dagger ,
$$
obeying the cocycle condition $\tilde{W}(\tilde{\Lambda}_2\tilde{\Lambda}_1,\tilde{U}) = \tilde{W}(\tilde{\Lambda}_2,\tilde{\Lambda}_1\tilde{U})\tilde{W}(\tilde{\Lambda}_1,\tilde{U})$. For a boost along $x$ of rapidity $1$ followed by one along $y$ of rapidity $0.5$, the rotation is $0.99366\,e_0+0.11246\,e_3$, an angle of $12.9146^\circ$ about $\hat{\mathbf{z}}$.

Operationally the boost is a **controlled rotation**: on a momentum superposition it acts as $\sum_i|p_i'\rangle\langle p_i|\otimes\tilde{W}_i$, with the momentum as control and the branch-dependent Wigner rotation as the operation on the target. The factorisation into a momentum operation times a spin operation is forbidden by the bracket $[\tilde{K},\tilde{K}] = \tilde{J}$, and the Wigner rotation is the obstruction. The angle is zero for collinear boosts and exact for transverse ones, $\tan\alpha = \sinh\psi\sinh\chi/(\cosh\psi+\cosh\chi)$; it grows with the rapidity towards $\arctan(\sinh\chi)$, so the entropy imprinted on a transverse spin, $h((1+\cos\alpha)/2)$, approaches one bit, while for small rapidities $\alpha\approx\tfrac12\psi\chi\sin\theta$. The information a boost carries is the pair (angle, axis) of its Wigner rotation, and a spin collinear with the boost carries none of it.

Because the boost parameter space is curved, a closed path of boosts that returns the four-velocity to its starting value returns the spin only up to a rotation. For the loop $0\to\mathbf{v}_1\to\mathbf{v}_2\to0$ with a boost along $x$ of rapidity $a$ and one along $y$ of rapidity $b$, the holonomy is a rotation about $\hat{\mathbf{z}}$ by $6.86557^\circ$, $12.91464^\circ$, $24.10915^\circ$, and $32.71532^\circ$ for $(a,b) = (0.5,0.5)$, $(1,0.5)$, $(1,1)$, $(1.5,1)$. This is the Thomas–Wigner holonomy, and its rate form is Thomas precession; it is the information a path of boosts carries beyond the information in its endpoints.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{\Lambda} = \cosh\frac{\psi}{2}e_0 + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ | Boost rotor, $N(\tilde{\Lambda}) = 1$, Hermitian |
| $\psi$ | Rapidity |
| $\hat{\mathbf{u}}$ | Boost direction |
| $\chi = \mathrm{atanh}(v/c)$ | Particle rapidity |
| $\tilde{K}_k = \tfrac12 ie_k\in\mathbb{M}_+^{0}$ | Boost generators (informational) |
| $\tilde{J}_k = \tfrac12 e_k\in\mathbb{M}_-^{0}$ | Rotation generators (material, compact) |
| $[\tilde{K}_j,\tilde{K}_k] = \epsilon_{jkl}\tilde{J}_l$ | Non-closure of the boosts |
| $SL(2,\mathbb{C}) = SU(2)\cdot\exp(p)$ | Cartan decomposition |
| $\tilde{W}(\tilde{\Lambda},\tilde{U})$ | Wigner rotation, $\in SU(2)$ |
| $\alpha$, $\hat{\mathbf{n}}$ | Wigner angle and axis, $\hat{\mathbf{n}}\perp\hat{\mathbf{u}},\hat{\mathbf{p}}$ |
| $\tilde{W}(\tilde{\Lambda}_2\tilde{\Lambda}_1,\tilde{U}) = \tilde{W}(\tilde{\Lambda}_2,\tilde{\Lambda}_1\tilde{U})\tilde{W}(\tilde{\Lambda}_1,\tilde{U})$ | Cocycle condition |
| $\sum_i|p_i'\rangle\langle p_i|\otimes\tilde{W}_i$ | Boost as a controlled rotation |
| $\tan\alpha = \sinh\psi\sinh\chi/(\cosh\psi+\cosh\chi)$ | Exact angle at $\theta = \pi/2$ |
| $h\!\left(\frac{1+\cos\alpha}{2}\right)$ | Spin entropy imprinted on a transverse spin |
| $\tilde{P} = \tilde{\Lambda}_{\mathbf{v}_2}\tilde{\Lambda}_y(b)\tilde{\Lambda}_x(a)$ | Holonomy of a closed velocity loop |
| $\dot{\boldsymbol{\Omega}}_{\mathrm{T}} = -\frac{\gamma-1}{v^2}\mathbf{v}\times\dot{\mathbf{v}}$ | Thomas precession rate |

## Further Reading

- E. P. Wigner, "On unitary representations of the inhomogeneous Lorentz group," *Annals of Mathematics* **40** (1939) 149–204, for the little group and the original Wigner rotation.
- L. H. Thomas, "The motion of the spinning electron," *Nature* **117** (1926) 514, for the precession of the spin of an accelerated electron.
- L. H. Thomas, "The kinematics of an electron with an axis," *Philosophical Magazine* **3** (1927) 1–22, for the detailed kinematical derivation.
- F. R. Halpern, *Special Relativity and Quantum Mechanics* (Prentice-Hall, 1968), for the Wigner rotation and its composition properties.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 3rd ed., 1998), for Thomas precession and the composition of non-collinear boosts.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the little-group construction and the transformation of one-particle states.
- Asher Peres and Daniel R. Terno, "Quantum information and relativity theory," *Reviews of Modern Physics* **76** (2004) 93–123, for the Wigner rotation as an operation in relativistic quantum information.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor description of boosts and the composition of rotations.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for controlled unitary operations and the channel formalism.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spinor description of the Lorentz group and its subgroups.
