

# __$\mathbb{M}_-$ as the Material Space__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ contains four distinguished real subspaces, characterized as the fixed-point sets of the four natural conjugations. Two of them are four-dimensional: the **anti-Hermitian subspace** $\mathbb{M}_-$ and the **Hermitian subspace** $\mathbb{M}_+$. This article is about $\mathbb{M}_-$.

The mathematical content of this article is standard: $\mathbb{M}_-$ is isomorphic, as a real vector space with a quadratic form, to Minkowski space $\mathbb{R}^{1,3}$, and it is the natural home of the four-vectors of relativistic physics. The physical content is also standard: the four-position, four-velocity, four-momentum, four-force, four-potential, and four-current of a relativistic system all lie in $\mathbb{M}_-$.

The **interpretation** of $\mathbb{M}_-$ as the "material" subspace is a reading of its structure, not a derivation. A general element of $\mathbb{M}_-$ has an **imaginary** scalar part and a **real** vector part. The real vector part corresponds to the three spatial dimensions — the directions in which material objects extend and move. The imaginary scalar part corresponds to the time coordinate $ict$, and its imaginary character reflects the fact that time, unlike space, is not itself a material object: it can be measured but not touched, not held, not moved through. We take this interpretation as the motivation for the name "material subspace", but the mathematics below stands on its own.

The companion article, *$\mathbb{M}_+$ as the Informational Space*, treats the complementary subspace. The present article is entirely within established physics.

The conventions are those of the companion articles: the biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, the scalar imaginary is $i$, and the biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$. Throughout, the symbol $c$ denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ denotes the **vacuum speed of light**, $c_0 = 1/\sqrt{\epsilon_0\mu_0}$. In vacuum, $c = c_0$. The symbol $\mathbf{v}$ is reserved for particle velocities.

## The Anti-Hermitian Subspace

### Definition and Basis

The **anti-Hermitian subspace** $\mathbb{M}_-$ is the fixed-point set of the anti-Hermitian conjugation:

$$
\mathbb{M}_- = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^\flat = \tilde{Q}\},
$$

where $\tilde{Q}^\flat = -\tilde{Q}^\dagger$ and $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$. Explicitly, a biquaternion is in $\mathbb{M}_-$ if and only if it has the form

$$
\tilde{Q} = i q_0\,e_0 + q_1\,e_1 + q_2\,e_2 + q_3\,e_3, \qquad q_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

The scalar part is **purely imaginary** and the vector part is **real**. Equivalently, if we write $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ with $Q_0 \in \mathbb{C}$ and $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$, then $\tilde{Q} \in \mathbb{M}_-$ iff $Q_0$ is purely imaginary and $Q_1, Q_2, Q_3$ are real.

A natural basis of $\mathbb{M}_-$ is

$$
\{i\,e_0,\; e_1,\; e_2,\; e_3\}.
$$

As a real vector space, $\mathbb{M}_-$ has dimension $4$. It is **not** a subalgebra of $\mathbb{B}$: the product of two elements of $\mathbb{M}_-$ is not necessarily in $\mathbb{M}_-$ (for example, $(ie_0)(ie_0) = -e_0 \in \mathbb{M}_+$).

### Properties

The subspace $\mathbb{M}_-$ has the following algebraic properties, established in the basic algebra article.

**Quadratic form.** The biquaternion **norm form** restricts to a real quadratic form on $\mathbb{M}_-$:

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = (iq_0)^2 + q_1^2 + q_2^2 + q_3^2 = -q_0^2 + q_1^2 + q_2^2 + q_3^2.
$$

This is a real quadratic form of **signature** $(3,1)$: three positive directions (the spatial components $q_1, q_2, q_3$) and one negative direction (the temporal component $q_0$). This is the Minkowski signature, expressed algebraically as a consequence of $i^2 = -1$.

**Zero divisors.** The norm form vanishes on the **light cone**

$$
q_0^2 = q_1^2 + q_2^2 + q_3^2,
$$

a double cone with apex at the origin. The nonzero elements of this cone are **zero divisors** of $\mathbb{B}$ (see the companion article on biquaternion zero divisors). The complement of the cone has two connected components, corresponding to the future and past components of the time-like region.

**Not a division algebra.** The presence of the zero divisor cone means that $\mathbb{M}_-$ is not a division algebra: there are nonzero elements of $\mathbb{M}_-$ that have no inverse. The physical significance of this is discussed below.

**Basis of the four-dimensional real space.** Every element of $\mathbb{M}_-$ is uniquely written as a linear combination of $ie_0, e_1, e_2, e_3$ with real coefficients. We may therefore identify $\mathbb{M}_-$ with $\mathbb{R}^4$, with the quadratic form $N$ corresponding to the Minkowski metric in the $(ict, x, y, z)$ convention.

## The Four-Vectors of Physics

The reason $\mathbb{M}_-$ is the "material subspace" is that the physical four-vectors of relativistic physics all lie in it. This is a structural fact: the four-vectors are elements of the same four-dimensional real vector space, with the same quadratic form, and the same transformation law under the Lorentz group.

The following table lists the seven physical four-vectors that live in $\mathbb{M}_-$. Each is expressed as an element of $\mathbb{M}_-$ with its standard physical interpretation.

| Four-vector | Biquaternion form | Components |
|---|---|---|
| Four-position | $\tilde{X} = ic\,t\,e_0 + \mathbf{x}$ | $(ict, \mathbf{x})$ |
| Four-velocity | $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ | $(\gamma ic, \gamma\mathbf{v})$ |
| Four-momentum | $\tilde{P} = m\tilde{U} = iE/c\,e_0 + \mathbf{p}$ | $(iE/c, \mathbf{p})$ |
| Four-force | $\tilde{F} = d\tilde{P}/d\tau$ | $(iP/c, \gamma\mathbf{f})$ |
| Four-potential | $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$ | $(i\phi/c, \mathbf{A})$ |
| Four-current | $\tilde{J} = ic\rho\,e_0 + \mathbf{j}$ | $(ic\rho, \mathbf{j})$ |
| Four-wavevector | $\tilde{K} = i\omega/c\,e_0 + \mathbf{k}$ | $(i\omega/c, \mathbf{k})$ |

In each case, the scalar part is purely imaginary and the vector part is real, matching the structure of $\mathbb{M}_-$.

The formulas for these four-vectors and their mutual relations (the mass-shell relation, the conservation laws, the wave equations) are collected in the companion article on relativistic mechanics. Here we only note that **they all live in the same subspace**. This is the structural content of the observation that relativistic physics is naturally expressed in $\mathbb{M}_-$.

### The Common Structure

The four-vectors share the following structural features, which are the reasons they lie in $\mathbb{M}_-$.

**1. Imaginary scalar part.** The time component of each four-vector is written as $i$ times a real quantity: $ict$, $i\gamma c$, $iE/c$, $i\phi/c$, $ic\rho$, $i\omega/c$. The factor of $i$ is the marker that distinguishes the temporal component from the spatial components. This is the $ict$ convention, and it is the reason the metric on $\mathbb{M}_-$ has signature $(3,1)$ rather than being positive-definite.

**2. Real vector part.** The spatial components are real. They are the components in the three real directions $e_1, e_2, e_3$ of ordinary physical space.

**3. Lorentz covariance.** The four-vectors transform under the Lorentz group by the **rotor conjugation** (see the companion article on the Lorentz transformation). The rotors are elements of the complementary subspace $\mathbb{M}_+$, and their action on $\mathbb{M}_-$ is the biquaternion form of the Lorentz transformation.

**4. Invariant norm.** Each four-vector has an invariant norm under the Lorentz group, equal to the norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ evaluated on the four-vector. This is the biquaternion expression of the relativistic invariants: the interval for the four-position, $-c^2$ for the four-velocity, $-m^2 c^2$ for the four-momentum, $0$ for the four-potential (in the Lorenz gauge), $0$ for the four-current (as a consequence of charge conservation), and $0$ for the four-wavevector (for light).

## The Invariant Interval and the Minkowski Metric

The **invariant interval** between two nearby events in spacetime is the quadratic form associated with the displacement biquaternion $d\tilde{X} \in \mathbb{M}_-$:

$$
ds^2 = d\tilde{X} \circ d\tilde{X} = (ic\,dt)^2 + dx^2 + dy^2 + dz^2 = -c^2\,dt^2 + d\mathbf{x}^2.
$$

This is the biquaternion expression of the Minkowski interval. Note that the interval uses the **square** $d\tilde{X} \circ d\tilde{X}$, not the norm form $d\tilde{X}\bar{d\tilde{X}}$. For an element of $\mathbb{M}_-$, the two differ by the sign of the vector part: $d\tilde{X} \circ d\tilde{X} = (ic\,dt)^2 + d\mathbf{x}^2$, while $d\tilde{X}\bar{d\tilde{X}} = (ic\,dt)^2 - d\mathbf{x}^2$. The interval uses the square, giving the standard Minkowski form $-c^2 dt^2 + d\mathbf{x}^2$.

The Lorentzian signature of the interval is not postulated: it arises algebraically from $i^2 = -1$ in the time component. This is the content of the $ict$ convention (see the companion article on the $ict$ convention). The biquaternion formulation makes explicit that the Lorentzian structure of spacetime is a **consequence of a complex structure** on the time coordinate, not an independent axiom.

The interval $ds^2$ has the following three possible signs, defining the three classes of Minkowski intervals:

- **Timelike** ($ds^2 < 0$): the events can be connected by a physical trajectory.
- **Spacelike** ($ds^2 > 0$): the events are causally disconnected.
- **Null** ($ds^2 = 0$): the events are connected by a light signal.

The null interval is the **light cone**, which is the zero divisor set of $\mathbb{M}_-$ (as discussed above).

## The Lorentz Transformation on $\mathbb{M}_-$

The four-vectors of physics transform under the Lorentz group by **rotor conjugation**:

$$
\tilde{X}' = \tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^\dagger,
$$

where $\tilde{\Lambda}$ is the **boost biquaternion** (an element of the complementary subspace $\mathbb{M}_+$), and $\tilde{\Lambda}^\dagger = \tilde{\Lambda}$ for a pure boost. The rotor conjugation is the biquaternion form of the standard Lorentz transformation of a four-vector.

The full development of the Lorentz transformation, including the boost biquaternion, its relation to the four-velocity, and its action on the four-potential, is the subject of the companion article. Here we only recall that the rotor conjugation **preserves** $\mathbb{M}_-$: if $\tilde{X} \in \mathbb{M}_-$ and $\tilde{\Lambda} \in \mathbb{M}_+$ (or, more generally, $\tilde{\Lambda}$ is a unit-norm biquaternion), then $\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger \in \mathbb{M}_-$.

This is the biquaternion expression of the statement that the Lorentz group acts on the four-vector space and leaves it invariant. The rotors themselves lie in $\mathbb{M}_+$ (for pure boosts) or in the unit-norm group of $\mathbb{B}$ (for general Lorentz transformations); the space on which they act is $\mathbb{M}_-$.

## The Light Cone and the Zero Divisors

The **light cone** is the set of four-vectors $\tilde{X} \in \mathbb{M}_-$ with vanishing norm form:

$$
N(\tilde{X}) = 0 \quad \Longleftrightarrow \quad q_0^2 = q_1^2 + q_2^2 + q_3^2,
$$

where $q_0$ is the (real) time component and $q_1, q_2, q_3$ are the spatial components. This is a double cone in $\mathbb{R}^4$ with apex at the origin.

The nonzero elements of the light cone are **zero divisors** of the biquaternion algebra: they are nonzero elements $\tilde{X}$ for which there exists a nonzero $\tilde{Y}$ with $\tilde{X}\tilde{Y} = 0$. The zero divisor structure is intrinsic to the biquaternion algebra and reflects the fact that the light cone is the **characteristic cone** of the wave operator $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$.

From the physical point of view, the zero divisors of $\mathbb{M}_-$ are the **null four-vectors**: the four-vectors of light signals, which have zero rest mass and propagate at the speed of light. The massless particles of relativistic physics correspond to the zero divisors of the biquaternion algebra. This is a structural fact of the algebra, not an additional assumption.

## What Is Not in $\mathbb{M}_-$

Not every physical object is a four-vector, and not every biquaternion lies in $\mathbb{M}_-$. Two important counterexamples illustrate the limits of the subspace.

### The Field-Strength Biquaternion

The **field-strength biquaternion** of the electromagnetic field is

$$
\tilde{F} = \sqrt{\epsilon}\,\mathbf{E} + i\sqrt{\mu}\,\mathbf{H},
$$

which is a biquaternion with **vanishing scalar part** and a **mixed real/imaginary vector part**. This is not an element of $\mathbb{M}_-$: the vector part is neither purely real nor purely imaginary, but a specific combination of a real part ($\sqrt{\epsilon}\mathbf{E}$) and an imaginary part ($i\sqrt{\mu}\mathbf{H}$). The field strength is not a four-vector but a **rank-2 antisymmetric tensor** $F^{\mu\nu}$, and it transforms under the Lorentz group by a more general rule than the four-vector rotor conjugation.

### The Energy–Momentum Biquaternion

The **energy–momentum biquaternion** is

$$
\tilde{W} = W + \frac{1}{c}\mathbf{S},
$$

with a **real** scalar part (the energy density) and a **real** vector part (the Poynting vector). This is an element of the **quaternion subspace** $\mathbb{H}_\mathbb{B}$, not of $\mathbb{M}_-$ or $\mathbb{M}_+$. The energy–momentum is a component of a **rank-2 symmetric tensor** $T^{\mu\nu}$, and it transforms under the Lorentz group by a still more general rule.

These counterexamples illustrate that $\mathbb{M}_-$ is specifically the **vector representation** of the Lorentz group, not the full tensor algebra. The four-vectors live in $\mathbb{M}_-$; the antisymmetric tensors (field strengths) and symmetric tensors (energy–momentum) do not.

## The Complementary Subspace $\mathbb{M}_+$

The subspace $\mathbb{M}_-$ is one of two four-dimensional real subspaces of $\mathbb{B}$ complementary under the Hermitian decomposition:

$$
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-.
$$

The other subspace, $\mathbb{M}_+$, is the **Hermitian subspace**:

$$
\mathbb{M}_+ = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^\dagger = \tilde{Q}\},
$$

with elements of the form

$$
\tilde{Q} = q_0\,e_0 + i q_1\,e_1 + i q_2\,e_2 + i q_3\,e_3, \qquad q_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

The scalar part is **real** and the vector part is **purely imaginary**. The norm form on $\mathbb{M}_+$ has signature $(1,3)$ (one positive, three negative), the mirror image of the signature on $\mathbb{M}_-$.

The two subspaces are related by multiplication by $i$: $i\mathbb{M}_+ = \mathbb{M}_-$ and $i\mathbb{M}_- = \mathbb{M}_+$. The quaternion conjugation swaps them: $\overline{\mathbb{M}_+} = \mathbb{M}_-$ and $\overline{\mathbb{M}_-} = \mathbb{M}_+$.

The subspace $\mathbb{M}_+$ contains the **boost biquaternions** $\tilde{\Lambda} = \cosh(\psi/2) + i\sinh(\psi/2)\hat{\mathbf{u}}$ that act on $\mathbb{M}_-$ by rotor conjugation. It also contains the **Hermitian forms** $\tilde{Q}\tilde{Q}^\dagger$ for any $\tilde{Q}$, the **idempotents** $P_\pm = \tfrac{1}{2}(e_0 \pm \mu i)$ from real roots of $-1$, and the identity $e_0$. These objects are the subject of the companion article on the informational space.

The structural relation between the two subspaces is:

- $\mathbb{M}_-$ is the space of **states** — the four-vectors that describe the configuration of a physical system.
- $\mathbb{M}_+$ is the space of **operators** — the Hermitian biquaternions that act on the states.

The action is the rotor conjugation $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$, with $\tilde{\Lambda} \in \mathbb{M}_+$ (for pure boosts) and $\tilde{X} \in \mathbb{M}_-$.

This complementarity is the algebraic content of the interpretation of $\mathbb{M}_-$ as the "material" or "state" space and $\mathbb{M}_+$ as the "informational" or "operator" space. The present article focuses on the material side; the informational side is treated in the companion article.

## Summary

The anti-Hermitian subspace $\mathbb{M}_-$ is a four-dimensional real subspace of the biquaternion algebra, consisting of elements with imaginary scalar part and real vector part. Its norm form has signature $(3,1)$, matching the Minkowski metric in the $ict$ convention. The Lorentzian signature is not postulated: it arises algebraically from $i^2 = -1$ in the imaginary scalar part.

The subspace $\mathbb{M}_-$ is the natural home of the four-vectors of relativistic physics:

- The four-position $\tilde{X} = ict\,e_0 + \mathbf{x}$.
- The four-velocity $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$.
- The four-momentum $\tilde{P} = m\tilde{U}$.
- The four-force $\tilde{F} = d\tilde{P}/d\tau$.
- The four-potential $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$.
- The four-current $\tilde{J} = ic\rho\,e_0 + \mathbf{j}$.
- The four-wavevector $\tilde{K} = i\omega/c\,e_0 + \mathbf{k}$.

Each has an imaginary scalar part (the time component) and a real vector part (the spatial components). Each transforms under the Lorentz group by rotor conjugation, with the rotor biquaternion living in the complementary subspace $\mathbb{M}_+$.

The **light cone** of Minkowski space is the zero divisor cone of $\mathbb{M}_-$: the null four-vectors of light-like propagation are exactly the zero divisors of the biquaternion algebra. This is a structural fact of the algebra, not an additional assumption.

Not every physical object is a four-vector: the field-strength biquaternion (antisymmetric rank-2 tensor) and the energy–momentum biquaternion (symmetric rank-2 tensor) do not lie in $\mathbb{M}_-$. The subspace $\mathbb{M}_-$ is specifically the **vector representation** of the Lorentz group.

The complementary subspace $\mathbb{M}_+$ is the Hermitian subspace, consisting of elements with real scalar part and imaginary vector part. It contains the boost biquaternions, the Hermitian forms, the idempotents, and the identity. It acts on $\mathbb{M}_-$ by rotor conjugation. The complementarity $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ is the algebraic content of the interpretation of $\mathbb{M}_-$ as "material" (states) and $\mathbb{M}_+$ as "informational" (operators). The latter interpretation is the subject of the companion article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material space): imaginary scalar, real vector |
| $\mathbb{M}_+$ | Hermitian subspace (informational space): real scalar, imaginary vector |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $s^2 = d\tilde{X}\circ d\tilde{X}$ | Invariant interval |
| $\tilde{\Lambda} \in \mathbb{M}_+$ | Boost biquaternion |
| $\tilde{X}' = \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ | Rotor conjugation |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the original four-dimensional formulation of spacetime.
- Albert Einstein, *The Meaning of Relativity* (Princeton, 1922), for the $ict$ formulation of special relativity.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the standard four-vector formulation of relativistic physics.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the four-vector and tensor formulation of electromagnetism.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection between Clifford algebras and Minkowski space.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra formulation of special relativity.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of spacetime algebra.

