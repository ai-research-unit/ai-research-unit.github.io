# __The Relativistic Qubit in Biquaternionic Form__

## Introduction

The elementary carrier of information in this framework is the qubit, and the qubit is not postulated: it is the defining module of the algebra. An algebra isomorphic to $M_2(\mathbb{C})$ has exactly one simple left module, the column space $S = \mathbb{C}^2$, and the rank-one projectors on $S$ are exactly the trace-one idempotents of the Hermitian sector $\mathbb{M}_+$. The state vectors are elements of $S$, the states in the statistical sense are positive trace-one elements of $\mathbb{M}_+$, and the two are related by the rank-one correspondence. What turns this qubit into a **relativistic** qubit is not a new carrier; it is the action on the carrier. The algebra's unit-norm elements form $SL(2,\mathbb{C})$, the double cover of the proper orthochronous Lorentz group, and they act on $S$ by left multiplication. The qubit's symmetry group is therefore the Lorentz group, not the unitary group, and the consequences of that fact are the subject of this article.

Three features distinguish the relativistic qubit from the non-relativistic one, and the article is organised around them. First, the left action of $SL(2,\mathbb{C})$ on $S$ is **not unitary**: it preserves the algebra's biquaternion norm but not the Hilbert-space norm of a spinor, so the state space of the qubit is invariant only under the compact subgroup $SU(2)$. Second, the pure states — the rays of $S$ — are the **celestial sphere**: the ratio of the two spinor components is a complex coordinate on $\mathbb{CP}^1$, the Lorentz group acts on it by Möbius transformations, and each ray determines a **future null four-vector** in the material sector $\mathbb{M}_-$, so that the pure informational states have a light-like geometric image. Third, the physically meaningful spin transformation at definite momentum is not the module action at all but the **little-group Wigner rotation**, a unitary element of $SU(2)$ that acts on the rest-frame qubit by a Bloch-sphere rotation; the non-unitary module action and the unitary physical rotation are two different objects, and keeping them apart is the main technical point of the article.

The article proceeds as follows. The carrier and its states are recalled. The Lorentz action on the carrier is set out, and its non-unitarity is derived. The pure states are identified with the celestial sphere, and the null-vector map is constructed and shown to intertwine the spinor action with the four-vector action. The mixed states and the little group are treated next, with the little group derived as the stabilizer of the four-velocity and the Wigner rotation defined algebraically. The two sectors are then read on the qubit's observables and generators, and the article closes with a summary.

The notation is that of the foundational articles: $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, quaternion units $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_k^2 = -e_t$ and $\vec e_x\vec e_y = \vec e_z$, central scalar $i$ with $i^2 = -1$, trace $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$, Hermitian conjugation ${}^{*}$, and biquaternion norm $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$. The matrix model is $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ with $e_t\mapsto I_2$, $\vec e_k\mapsto -i\sigma_k$, $i\mapsto iI_2$. The spinor module is $S = \mathbb{C}^2$ with the left action $\rho_S(\tilde{Q})|u\rangle = \mathsf{M}_2(\tilde{Q})|u\rangle$. The Hermitian sector is $\mathbb{M}_+$ and the anti-Hermitian sector $\mathbb{M}_-$.

The companion articles supply the pieces:
- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the defining module, its irreducibility, and the state correspondence.
- Companion article *Quantum Physics in Biquaternionic Form*, for the Hermitian sector, the idempotents, the Bloch ball, and the conjugation action.
- Companion article *The Bloch Ball as the Trace-One Slice of the Future Light Cone*, for the geometry of the state space.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for four-vectors, the biquaternion norm, and the interval.
- Companion article *The Lorentz Group in Biquaternionic Form — Structure and Representations*, for $SL(2,\mathbb{C})$, its subgroups, and the Wigner rotation.

## The Qubit as the Defining Module

### Carrier and states

The carrier of the qubit is the defining module $S$ introduced by the spinor-module article,
$$
S = \mathbb{C}^2, \qquad \rho_S(\tilde{Q})\,|u\rangle = \mathsf{M}_2(\tilde{Q})\,|u\rangle .
$$
It is the unique simple left $\mathbb{B}$-module up to isomorphism; it is complex two-dimensional; and every non-zero spinor is cyclic, so $S$ has no non-trivial submodules. The algebra's left regular module is two copies of it, $\mathbb{B}\cong S\oplus S$, which is the algebraic origin of the two-component spinor structure.

Two objects must be kept apart throughout. A **state vector** is an element $|u\rangle\in S$; a **state** in the statistical sense is a positive trace-one element $\tilde{Ϛ}\in\mathbb{M}_+$, i.e. an operator on $S$. The correspondence between them is the rank-one map
$$
|u\rangle \ \longleftrightarrow\ \tilde\Pi(u) = \frac{|u\rangle\langle u|}{\langle u|u\rangle} = \mathsf{M}_2^{-1}\!\left(\frac{|u\rangle\langle u|}{\langle u|u\rangle}\right)\in\mathbb{M}_+ ,
$$
and it is the ordinary relation between a ket and a density operator. A general state is
$$
\tilde{Ϛ} = \tfrac12\bigl(e_t + i\vec r\bigr), \qquad \vec r\in\mathbb{R}^3, \qquad |\vec r| = 1 \iff \tilde{Ϛ}\ \text{pure},
$$
so the state space is the Bloch ball $|\vec r|\leq1$, and the pure states are its boundary. The pure-state idempotents are
$$
\tilde\Pi_{1,2}(\vec u) = \tfrac12\bigl(e_t \pm i\vec u\bigr), \qquad |\vec u| = 1,
$$
and the Born pairing is $\mathrm{Tr}(\tilde{Ϛ}\tilde{H}) = h_0 + \vec r\cdot\vec h$. None of this uses relativity; it is the content of the quantum-mechanical companion, recalled here because the relativistic qubit is a structure imposed on this state space.

### Why the carrier is forced

The word *native* is exact and is worth one paragraph, because it is what makes the relativistic qubit a question about the algebra rather than about a choice. The algebra is simple and central, so by the classification of modules over a full matrix algebra it has exactly one irreducible representation, and that representation is on the column space $S$. There is no second two-dimensional carrier, no one-dimensional carrier, and no three-dimensional one. The qubit is therefore the elementary carrier the algebra has, and any relativistic structure the framework can carry must be an action on this carrier rather than a replacement for it. The remainder of the article is the study of that action.

## The Lorentz Action on the Carrier

### The two actions of the unit-norm group

A biquaternion of unit norm,
$$
\tilde U = \cosh\frac{\psi}{2}\,e_t + i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b} \quad(\text{boost}), \qquad
\tilde u = \cos\frac{\theta}{2}\,e_t + \sin\frac{\theta}{2}\,\vec u_{\mathrm r} \quad(\text{rotation}),
$$
satisfies $\langle\tilde U\rangle_{\natural} = 1$, hence $\tilde U^{-1} = \tilde U^{\natural}$, and the unit-norm elements form $SL(2,\mathbb{C})$, the double cover of the proper orthochronous Lorentz group. The same element acts on the two sectors by different formulas:

**On the module**, by left multiplication,
$$
|u\rangle \ \longmapsto\ \tilde U|u\rangle := \mathsf{M}_2(\tilde U)|u\rangle ;
$$
this is the **spinor representation**, complex two-dimensional and faithful, and the element $\pm\tilde U$ act identically, which is the double covering $SL(2,\mathbb{C})\to SO^+(1,3)$.

**On the material sector**, by congruence,
$$
\tilde{Q} \ \longmapsto\ \tilde U\tilde{Q}\tilde U^{*} , \qquad \tilde{Q}\in\mathbb{M}_- ;
$$
this is the **four-vector representation**. It preserves $\mathbb{M}_-$ by the sector identity of the companion structural article, and it preserves the biquaternion norm,
$$
N\bigl(\tilde U\tilde{Q}\tilde U^{*}\bigr) = \langle\tilde U\rangle_{\natural}\,\langle\tilde{Q}\rangle_{\natural}\,\langle\tilde U^{*}\rangle_{\natural} = \langle\tilde{Q}\rangle_{\natural},
$$
so it preserves the interval and the light cone.

### The module action is not unitary

The decisive property of the spinor action is its failure to be unitary, and it is a two-line computation. The Hermitian form on $S$ is $\langle u|v\rangle = \langle u|\cdot|v\rangle$ in the matrix model, and
$$
\langle \tilde Uu\,|\,\tilde Uv\rangle
= \langle u|\,\mathsf{M}_2(\tilde U)^\dagger\mathsf{M}_2(\tilde U)\,|v\rangle
= \langle u|\,\mathsf{M}_2(\tilde U^{*}\tilde U)\,|v\rangle .
$$
The form is preserved for all spinors if and only if
$$
\tilde U^{*}\tilde U = e_t ,
$$
which is the unitarity condition. Among the unit-norm elements, $\tilde U^{*}\tilde U = e_t$ together with $\langle\tilde U\rangle_{\natural} = 1$ is exactly the condition that $\tilde U$ is a unit real quaternion, i.e. an element of $SU(2)$. Therefore
$$
\text{the spinor norm is preserved by } SU(2) \text{ and by no other subgroup of } SL(2,\mathbb{C}).
$$
A boost fails the condition maximally: for $\tilde U$ Hermitian one has $\tilde U^{*}\tilde U = \tilde U^2 = e_t + i\sinh\psi\,\vec u_{\mathrm b}$, so
$$
\langle\tilde Uu|\tilde Uu\rangle = \langle u|u\rangle + i\sinh\psi\,\langle u|\vec u_{\mathrm b}|u\rangle \neq \langle u|u\rangle .
$$
The norm is scaled by a positive factor rather than rotated, so the ray is preserved but the normalization is not.

The state space is the boundary of the Bloch ball, and this computation says that a boost does not preserve it: only the compact subgroup $SU(2)$ acts on the pure states as a symmetry. The Lorentz group acts on the carrier, but the carrier's Hilbert-space geometry is not Lorentz invariant. That is the first relativistic feature of the qubit, and it is the origin of the distinction between the module action and the physical spin transformation drawn below.

### The compact subgroup and the phase

The intersection of the two normalization conditions is worth recording, since it is where the relativistic and the quantum actions coincide:
$$
SU(2) = \bigl\{\tilde U : \langle\tilde U\rangle_{\natural} = 1\bigr\}\cap\bigl\{\tilde{U} : \tilde{U}\tilde{U}^{*} = e_t\bigr\}.
$$
Inside $SU(2)$ the left action is unitary and the conjugation action is an automorphism, and a central phase acts trivially on rays. The two conditions are independent outside it: a boost has unit norm but is not unitary, and a general unitary element of $\mathrm{U}(2)$ need not have unit norm. The relativistic qubit therefore has a symmetry group $SL(2,\mathbb{C})$ and a *unitary* symmetry group $SU(2)$, and the quotient structure between them — the space of boosts modulo rotations — is the hyperbolic part of the group in which the frame dependence resides.

## Pure States: The Celestial Sphere

### Rays and the Möbius action

A pure state vector is defined up to complex scale, so the pure states of the relativistic qubit are the rays, i.e. the points of the complex projective line. Writing $|u\rangle = (u_t, u_x)^{\mathsf T}$ and using the ratio
$$
z = \frac{u_x}{u_t}\in\mathbb{C}\cup\{\infty\},
$$
the left action of $\tilde U$ on the spinor induces on $z$ the fractional-linear map
$$
|u\rangle \ \longmapsto\ \tilde U|u\rangle
\quad\Longrightarrow\quad
z \ \longmapsto\ \frac{\Lambda_{10} + \Lambda_{11}z}{\Lambda_{00} + \Lambda_{01}z},
\qquad \mathsf{M}_2(\tilde U) = \begin{pmatrix}\Lambda_{00} & \Lambda_{01}\\ \Lambda_{10} & \Lambda_{11}\end{pmatrix}.
$$
This is the standard Möbius action of $GL(2,\mathbb{C})$ on $\mathbb{CP}^1$, and on the quotient by the centre it is the action of
$$
PSL(2,\mathbb{C}) \cong SO^+(1,3).
$$
The pure-state space of the relativistic qubit is therefore the Riemann sphere, on which the Lorentz group acts as the group of Möbius transformations — the same group that acts on the celestial sphere of null directions at a point of Minkowski space. This is the first appearance of the material sector inside the purely informational description, and it is made exact by the null-vector map.

### The null-vector map

Let $|u\rangle$ be normalized and let
$$
\tilde\Pi(u) = \mathsf{M}_2^{-1}\!\bigl(|u\rangle\langle u|\bigr)\in\mathbb{M}_+
$$
be the corresponding pure state. Define
$$
\tilde{\mathcal L}(u) = i\,\tilde\Pi(u)\in\mathbb{M}_- .
$$
Two elementary facts identify $\tilde{\mathcal L}$ as a future null four-vector.

**It is null.** The determinant of a rank-one matrix vanishes, and under the matrix model the determinant is the biquaternion norm, so
$$
N\bigl(\tilde\Pi(u)\bigr) = \det\mathsf{M}_2\bigl(\tilde\Pi(u)\bigr) = \det\bigl(|u\rangle\langle u|\bigr) = 0 ,
\qquad
N\bigl(\tilde{\mathcal L}(u)\bigr) = i^2 N\bigl(\tilde\Pi(u)\bigr) = 0 .
$$

**It is future-directed and of definite normalization.** Writing $\tilde\Pi(u) = \tfrac12(e_t + i\vec r)$ with $|\vec r| = 1$, the element $\tilde{\mathcal L}(u) = i\tilde\Pi(u)$ has the form
$$
\tilde{\mathcal L}(u) = \tfrac{i}{2}\,e_t - \tfrac12\,\vec r ,
$$
so in the four-vector coordinates $\tilde{R} = ict\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ its time component is $ct = \tfrac12 > 0$ and its spatial direction is
$$
\vec u_p = -\vec u_r .
$$
The map takes a pure state of the informational sector to the unit-length future-directed null four-vector of its own Bloch direction, reversed in space; it is a bijection from the Bloch sphere onto the celestial sphere.

**It is equivariant.** The map intertwines the spinor action with the four-vector action,
$$
\tilde{\mathcal L}\bigl(\tilde Uu\bigr)
= i\,\mathsf{M}_2^{-1}\!\bigl(\mathsf{M}_2(\tilde U)|u\rangle\langle u|\mathsf{M}_2(\tilde U)^\dagger\bigr)
= \tilde U\,\tilde{\mathcal L}(u)\,\tilde U^{*} ,
$$
which is the statement that the diagram of the two actions commutes: the informational ray and its material null direction are carried by the same Lorentz transformation. The verification is the associativity of the matrix product together with $\mathsf{M}_2(\tilde U^{*}) = \mathsf{M}_2(\tilde U)^\dagger$.

### The material image of an informational state

The null-vector map gives the relativistic qubit a geometric face and is the precise sense in which the two sectors of the structural companion are linked at the level of a single state. A pure spinor state *is* a light direction; the material sector receives an image of the informational state, and the image transforms covariantly. The correspondence is the biquaternion form of the standard spinor–helicity construction, in which a two-component Weyl spinor is the square root of a null momentum, and the celestial sphere of the pure states is the sphere of null directions. It is worth noting what the map is not: it is defined for pure states, it takes the ray and not the spinor (the two spinors $\pm|u\rangle$ give the same $\tilde{\mathcal L}$), and it carries no information about the normalization, which the boost changes. For mixed states there is no analogous map, because the element $i\tilde{Ϛ}$ of $\mathbb{M}_-$ is not null except on the boundary, and the natural invariant of a mixed state is $\langle\tilde{Ϛ}\rangle_{\natural} = \tfrac14(1-|\vec r|^2)\geq0$, which measures the distance from the pure boundary rather than a direction.

**A worked instance.** Take the spin-up state along $z$, $|u\rangle = (1,0)^{\mathsf T}$, and boost along $x$ with rapidity $\psi = 0.6$. The spinor becomes
$$
\tilde U|u\rangle = \bigl(\cosh 0.3,\ \sinh 0.3\bigr)^{\mathsf T} = \bigl(1.04534,\ 0.30452\bigr)^{\mathsf T},
$$
whose norm is $1.34986 = \exp(0.3)$, not $1$: the boost has scaled the spinor, as the non-unitarity computation predicts. The ray, however, has moved, and the Bloch vector of the normalized state is
$$
\vec u_r: \ (0,0,1) \ \longmapsto\ (0.53705,\ 0,\ 0.84355),
$$
a Möbius displacement from the north pole toward $+x$. The null four-vector is correspondingly
$$
\tilde{\mathcal L} = \bigl(\tfrac{i}{2},\ -\tfrac12\vec u_r\bigr): \
\bigl(0.5i,\ 0,\ 0,\ -0.5\bigr) \ \longmapsto\ \bigl(0.59273i,\ -0.31833,\ 0,\ -0.5\bigr),
$$
which remains null, $\langle\tilde{\mathcal L}\rangle_{\natural} = 0$ in both frames, and is carried by the same rotor. A boost along the spin's own axis, by contrast, leaves the ray fixed — $|u\rangle = (1,1)^{\mathsf T}/\sqrt2$ boosted along $x$ returns the ray of $(1,1)^{\mathsf T}$ with the norm scaled by $\exp(0.3)$ — because a Möbius map fixing its own fixed point on the sphere only scales the coordinate. These two behaviours, the displacement of a transverse spin and the scaling of a longitudinal one, are the elementary kinematics of the relativistic qubit.

## Mixed States and the Little Group

### The congruence is not the physical state transformation

The state space of the qubit is the Bloch ball, and the obvious guess for the action of a Lorentz transformation on a state is the congruence
$$
\tilde{Ϛ} \ \longmapsto\ \tilde U\tilde{Ϛ}\tilde U^{*} .
$$
This has the right formal properties — it preserves Hermiticity and the inertia of the matrix, hence positivity — but it is not a transformation of states. It does not preserve the trace: for the maximally mixed state,
$$
\tilde U\,\tfrac12 e_t\,\tilde U^{*} = \tfrac12\tilde U^2 ,
\qquad
\mathrm{Tr}\bigl(\tilde U\tfrac12 e_t\tilde U^{*}\bigr) = \cosh\psi \neq 1 ,
$$
and after normalizing, the centre of the Bloch ball is carried to the point
$$
\vec r = \tanh\psi\ \vec u_{\mathrm b},
$$
not to itself. A transformation that moves the maximally mixed state while scaling the trace is not a channel, and the reason is structural: the congruence by a non-unitary element is a map on the *algebra*, not an operation on the *state space*, and the companion quantum-mechanical article records the same fact from the group side — the trace pairing, on which the Born rule rests, is preserved exactly by the unitary group and by no larger one.

The congruence is nevertheless the correct action on the spinor ray and on the pure-state projectors considered as elements of the algebra. The resolution of the apparent conflict is to distinguish two objects that the non-relativistic formalism identifies: the **spinor** of a particle and the **spin state** of a particle at definite momentum. They transform by different formulas, and the second is the physically observable one.

### The little group as a stabilizer

Let the particle have four-velocity $\tilde{V}$, a future-directed timelike element of $\mathbb{M}_-$ normalized by $\langle\tilde{V}\rangle_{\natural} = -c^2$. Its **little group** is the subgroup of $SL(2,\mathbb{C})$ that fixes it,
$$
\mathrm{Little}(\tilde{V}) = \bigl\{\tilde U : \tilde U\tilde{V}\tilde U^{*} = \tilde{V}\bigr\}.
$$
Because the congruence preserves the biquaternion norm, the stabilizer of the timelike direction $\tilde{V}$ is conjugate to the stabilizer of the rest four-velocity $ic\,e_t$; and the stabilizer of $ic\,e_t$ consists of the elements with $\tilde U\tilde U^{*} = e_t$ (the central factor cancels), which is $\mathrm{U}(2)$, whose unit-determinant part is $SU(2)$. Hence
$$
\mathrm{Little}(\tilde{V}) \cong \mathrm{U}(2), \qquad \text{its unit-norm part} = SU(2),
$$
and this is the little group of a **massive** particle. Its representations are the spin representations: the spin-$\tfrac12$ representation is the defining two-dimensional one, and the qubit at rest is the carrier of that representation.

For a **massless** particle the four-velocity is replaced by the null four-vector $\tilde{\mathcal L}$ with $\langle\tilde{\mathcal L}\rangle_{\natural} = 0$. The stabilizer of a null element in $SL(2,\mathbb{C})$ is larger: it is the two-dimensional Euclidean group $E(2)$, generated by one rotation about the spatial momentum and two null translations, and it is non-compact. Its finite-dimensional unitary representations are one-dimensional and labelled by the helicity. The massless relativistic qubit therefore does not have a rest-frame two-state structure; it has a helicity label and a single state per momentum, which is the group-theoretic statement that a massless spin-$\tfrac12$ particle has one helicity state rather than two spin states. The distinction between the massive and the massless qubit is thus a distinction between the two little groups,
$$
SU(2)\ (\text{massive, spin}), \qquad E(2)\ (\text{massless, helicity}),
$$
and it is the standard little-group classification of Wigner, realized here inside the single group of unit-norm biquaternions.

### The Wigner rotation

The physical transformation of a spin state is constructed from the little group as follows. Choose, for each four-velocity $\tilde{V}$, a **standard boost** $\tilde U_{\tilde{V}}$ carrying it to the rest four-velocity,
$$
\tilde U_{\tilde{V}}\,\tilde{V}\,\tilde U_{\tilde{V}}^{*} = ic\,e_t
\qquad\Longleftrightarrow\qquad
\tilde{V} = \tilde U_{\tilde{V}}^{-1}\,(ic\,e_t)\,\tilde U_{\tilde{V}}^{-1{}^{*}},
$$
which for a Hermitian unit-norm rotor means $\tilde U_{\tilde{V}} = \tilde U^{\natural}_{\tilde{V}}$ and $\tilde U_{\tilde{V}}^{-1} = \tilde U^{\natural}_{\tilde{V}}$. Under a Lorentz transformation $\tilde U$ the four-velocity goes to
$$
\tilde{V}' = \tilde U\tilde{V}\tilde U^{*} ,
$$
and the element
$$
\tilde{W}(\tilde U,\tilde{V}) = \tilde U_{\tilde{V}'}\,\tilde U\,\tilde U_{\tilde{V}}^{-1}
$$
carries the rest frame to the rest frame:
$$
\tilde{W}\,(ic\,e_t)\,\tilde{W}^{*}
= \tilde U_{\tilde{V}'}\tilde U\tilde U_{\tilde{V}}^{-1}\,(ic\,e_t)\,\tilde U_{\tilde{V}}^{-1{}^{*}}\tilde U^{*}\tilde U_{\tilde{V}'}^\dagger
= \tilde U_{\tilde{V}'}\,\tilde U\,\tilde{V}\,\tilde U^{*}\,\tilde U_{\tilde{V}'}^\dagger
= \tilde U_{\tilde{V}'}\,\tilde{V}'\,\tilde U_{\tilde{V}'}^\dagger
= ic\,e_t .
$$
By the stabilizer computation, $\tilde{W}$ is an element of the little group, and for a massive particle it is a unit-norm element with $\tilde{W}\tilde{W}^{*} = e_t$: a **unit real quaternion**, i.e. an element of $SU(2)$. This is the **Wigner rotation**. It is unitary, so it acts on the spin state by a genuine quantum operation,
$$
\tilde{Ϛ} \ \longmapsto\ \tilde{W}\tilde{Ϛ}\tilde{W}^{*} , \qquad \tilde{W}\in SU(2),
$$
which preserves the trace, the Hermiticity, the positivity, and — because it is a rotation — the Bloch radius. The maximally mixed state is fixed. The observable spin transformation at definite momentum is therefore a Bloch-sphere rotation by the Wigner angle, and not the non-unitary congruence of the previous subsection; the two agree only when $\tilde U$ is itself a rotation, in which case the standard boosts can be chosen so that $\tilde{W} = \tilde U$.

The frame dependence of everything that follows enters through the momentum argument of $\tilde{W}$. For a particle with a sharp four-velocity the boost applies the single unitary $\tilde{W}(\tilde U,\tilde{V})$ to the spin state and no entanglement with momentum can appear; for a momentum superposition the operator $\tilde{W}$ depends on the branch, and the boost acts as a momentum-controlled rotation, correlating spin with momentum. That mechanism — the momentum dependence of a unitary little-group element — is the content of the next three articles, and it is worth naming here as the reason the relativistic qubit is a *family* of qubits labelled by momentum rather than a single two-state system with an enlarged symmetry group.

## Observables, Generators, and the Two Sectors

**Observables.** The observables of the qubit are the Hermitian elements $\tilde{H} = h_0e_t + i\vec h$, with the spin operators
$$
\tilde{S}_k = \frac{\hbar}{2}\,i \vec e_k , \qquad [\tilde{S}_j,\tilde{S}_k] = i\hbar\,\epsilon_{jkl}\tilde{S}_l ,
$$
and the Born pairing $\mathrm{Tr}(\tilde{Ϛ}\tilde{H})$. The four-momentum is the material element $\tilde{P} = m\tilde{V}\in\mathbb{M}_-$, with $\tilde{P}\tilde{P}^{\natural} = -m^2c^2$; it is not an observable but the frame datum that labels which little-group qubit is in question.

**Generators.** The generators of the two transformation groups lie in the two sectors. The rotation generators are the traceless anti-Hermitian elements, the pure vectors
$$
\tfrac12 \vec e_k\in\mathbb{M}_-^{0},
$$
and the boost generators are the traceless Hermitian ones, the pure elements
$$
\tfrac12 i \vec e_k\in\mathbb{M}_+^{0},
$$
and $[\tfrac12 i\vec e_j,\tfrac12 i\vec e_k] = -\epsilon_{jkl}\tfrac12\vec e_l$: the commutator of two boosts is a rotation. The relativistic qubit's *observables* are the Hermitian elements of $\mathbb{M}_+$ and its *frame generators* are the Hermitian traceless elements of the same sector, while its *rotations* — the compact operations and the material generators — lie in $\mathbb{M}_-$. This is the Cartan decomposition of the structural companion read on the qubit: the informational sector supplies the boosts and the observables, the material sector supplies the rotations, and the bracket $[\text{boost},\text{boost}] = \text{rotation}$ is the algebraic source of the Wigner rotation.

## Summary

The relativistic qubit is the defining module $S$ of $\mathbb{B}$ with the left action of the unit-norm group $SL(2,\mathbb{C})$, together with the little-group structure that the action induces at fixed four-velocity. Its state vectors are the spinors, its states are the positive trace-one elements of $\mathbb{M}_+$, and its pure states are the rays, i.e. the points of $\mathbb{CP}^1$, on which the Lorentz group acts by Möbius transformations with $PSL(2,\mathbb{C})\cong SO^+(1,3)$.

The left action is not unitary. The spinor norm is preserved if and only if $\tilde U^{*}\tilde U = e_t$, which selects $SU(2)$ inside $SL(2,\mathbb{C})$; a boost scales the norm and leaves the ray transformed by a Möbius map. Each pure state determines a future null four-vector
$$
\tilde{\mathcal L}(u) = i\,\mathsf{M}_2^{-1}\bigl(|u\rangle\langle u|\bigr) = \tfrac{i}{2}e_t - \tfrac12\vec r, \qquad \langle\tilde{\mathcal L}\rangle_{\natural} = 0, \qquad \tilde{\mathcal L}(\tilde Uu) = \tilde U\tilde{\mathcal L}(u)\tilde U^{*} ,
$$
so the informational ray and its material null direction are carried by the same Lorentz transformation; the pure-state Bloch sphere is the celestial sphere, with the spatial direction of the null vector opposite the Bloch direction. The map exists for pure states only.

The physical spin state at definite four-velocity transforms not by the non-unitary congruence but by the little-group **Wigner rotation**
$$
\tilde{W}(\tilde U,\tilde{V}) = \tilde U_{\tilde{V}'}\tilde U\tilde U_{\tilde{V}}^{-1}\in SU(2), \qquad \tilde{V}' = \tilde U\tilde{V}\tilde U^{*} ,
$$
which fixes the rest four-velocity, is a unit real quaternion, and acts on the Bloch ball by a rotation. The massive little group is $SU(2)$ and carries spin; the massless little group is $E(2)$ and carries helicity, so the massless qubit has one state per momentum. The congruence by a non-unitary element is a map on the algebra that moves the maximally mixed state and scales the trace, and the physical state transformation is the unitary Wigner rotation; the two coincide only on the compact subgroup. Because $\tilde{W}$ depends on the four-velocity, the relativistic qubit is a momentum-labelled family of qubits, and a boost acts as a momentum-controlled rotation — the mechanism behind the frame-dependent entanglement of the next article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | Matrix model, $\vec e_k\mapsto-i\sigma_k$, $i\mapsto iI_2$ |
| $S = \mathbb{C}^2$ | Defining (spinor) module, the qubit carrier |
| $|u\rangle\in S$ | State vector (spinor) |
| $\tilde{Ϛ} = \tfrac12(e_t + i\vec r)$ | State, Bloch vector $\vec r$, $|\vec r|\leq1$ |
| $\tilde\Pi_{1,2}(\vec u) = \tfrac12(e_t\pm i\vec u)$ | Pure-state idempotent |
| $\tilde U$, $\langle\tilde U\rangle_{\natural} = 1$ | Unit-norm biquaternion, element of $SL(2,\mathbb{C})$ |
| $SU(2)$ | Unit real quaternions, unitary subgroup |
| $z = u_x/u_t$ | Möbius coordinate on the pure-state sphere $\mathbb{CP}^1$ |
| $\tilde{\mathcal L}(u) = i\mathsf{M}_2^{-1}(|u\rangle\langle u|)$ | Future null four-vector of a pure state, $\langle\tilde{\mathcal L}\rangle_{\natural} = 0$ |
| $\vec u_p = -\vec u_r$ | Null direction opposite the Bloch direction |
| $\tilde{V} = \gamma(ic\,e_t + \vec v)$ | Four-velocity, $\langle\tilde{V}\rangle_{\natural} = -c^2$ |
| $\mathrm{Little}(\tilde{V})$ | Stabilizer of $\tilde{V}$: $\mathrm{U}(2)$ massive, $E(2)$ massless |
| $\tilde U_{\tilde{V}}$ | Standard boost carrying $\tilde{V}$ to rest |
| $\tilde{W}(\tilde U,\tilde{V}) = \tilde U_{\tilde{V}'}\tilde U\tilde U_{\tilde{V}}^{-1}$ | Wigner rotation, $\in SU(2)$ |
| $\tilde{S}_k = \tfrac{\hbar}{2}i\vec e_k$ | Spin operators |
| $\tfrac12\vec e_k\in\mathbb{M}_-^{0}$ | Rotation generators (pure elements, material, compact) |
| $\tfrac12 i\vec e_k\in\mathbb{M}_+^{0}$ | Boost generators (pure elements, informational) |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- E. P. Wigner, "On unitary representations of the inhomogeneous Lorentz group," *Annals of Mathematics* **40** (1939) 149–204, for the little-group classification and the Wigner rotation.
- Eugene P. Wigner, "Relativistic invariance and quantum phenomena," *Reviews of Modern Physics* **29** (1957) 255–268, for the physical interpretation of the little group and superselection.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the Lorentz and Poincaré representations and the little-group construction of one-particle states.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spinor–null-vector correspondence and the celestial sphere.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the relation between the spinor module, the Möbius action, and the Lorentz group.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor description of boosts and rotations and the projective action on the sphere.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Bloch ball and the standard qubit formalism.
- Ingemar Bengtsson and Karol Życzkowski, *Geometry of Quantum States* (Cambridge, 2006), for the geometry of the qubit state space and its symmetry groups.
- Asher Peres and Daniel R. Terno, "Quantum information and relativity theory," *Reviews of Modern Physics* **76** (2004) 93–123, for the physical setting of the relativistic qubit and its frame dependence.
