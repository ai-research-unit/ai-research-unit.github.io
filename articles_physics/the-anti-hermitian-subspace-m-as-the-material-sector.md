# __The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector__

## Introduction

This article is about the **anti-Hermitian subspace** $\mathbb{M}_-$, the fixed space of the anti-Hermitian conjugation: its definition and basis, its algebraic properties, the physical reading of its quadratic form and light cone, its Lorentz action, and the four-vectors of relativistic physics that live in it.

The mathematical content of this article is standard: $\mathbb{M}_-$ is, as a real vector space with a quadratic form, isomorphic to Minkowski space $\mathbb{R}^{3,1}$ (three space-like directions and one time-like one), and it is the natural home of the four-vectors of relativistic physics. The physical content is also standard: the four-position, four-velocity, four-momentum, four-force, four-potential, and four-current of a relativistic system all lie in $\mathbb{M}_-$.

The **interpretation** of $\mathbb{M}_-$ as the "material" subspace is a reading of its structure, not a derivation. A general element of $\mathbb{M}_-$ has an **imaginary** scalar part and a **real** vector part. The real vector part corresponds to the three spatial dimensions — the directions in which material objects extend and move. The imaginary scalar part corresponds to the time coordinate $ict$, and its imaginary character reflects the fact that time, unlike space, is not itself a material object: it can be measured but not touched, not held, not moved through. We take this interpretation as the motivation for the name "material subspace", but the mathematics below stands on its own.

The present article is entirely within established physics.

The conventions are those of the companion articles: the biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, the scalar imaginary is $i$, and the biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$. Throughout, the symbol $c$ denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ denotes the **vacuum speed of light**, $c_0 = 1/\sqrt{\epsilon_0\mu_0}$. In vacuum, $c = c_0$. The symbol $\mathbf{v}$ is reserved for particle velocities.

## Basic Definition and Properties

### Definition and Basis

The **anti-Hermitian subspace** $\mathbb{M}_-$ is the fixed-point set of the anti-Hermitian conjugation:

$$
\mathbb{M}_- = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^\flat = \tilde{Q}\},
$$

where $\tilde{Q}^\flat = -\tilde{Q}^\dagger$ and $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$. Explicitly, a biquaternion is in $\mathbb{M}_-$ if and only if it has the form

$$
\tilde{Q} = i q'_0\,e_0 + q_1\,e_1 + q_2\,e_2 + q_3\,e_3, \qquad q'_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

The scalar part is **purely imaginary** and the vector part is **real**. Equivalently, if we write $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ with $Q_0 \in \mathbb{C}$ and $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$, then $\tilde{Q} \in \mathbb{M}_-$ iff $Q_0$ is purely imaginary and $Q_1, Q_2, Q_3$ are real — that is, $Q_0 = iq'_0$ and $Q_k = q_k$.

**The two writings.** The four real parameters $q'_0, q_1, q_2, q_3$ are the components of the material four-position, the temporal one scaled by $c$, so that the same element is written in the coordinates of physics as

$$
\tilde{Q} = iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 = ic\,t\,e_0 + x\,e_1 + y\,e_2 + z\,e_3, \qquad q'_0 = ct,\;\; q_1 = x,\;\; q_2 = y,\;\; q_3 = z .
$$

The left-hand writing is in the sector's own parameters and is the one used for algebraic statements; the right-hand one is in the coordinates of physics. The prime marks the coefficient that carries the $i$, which in $\mathbb{M}_-$ is the **scalar** $q'_0$ — the time. The four parameters are the real and imaginary parts of the four complex coefficients of a general biquaternion, $Q_\mu = q_\mu + iq'_\mu$, read off in the pattern that defines this sector: scalar imaginary, vector real.

A natural basis of $\mathbb{M}_-$ is

$$
\{i\,e_0,\; e_1,\; e_2,\; e_3\}.
$$

As a real vector space, $\mathbb{M}_-$ has dimension $4$. It is **not** a subalgebra of $\mathbb{B}$: the product of two elements of $\mathbb{M}_-$ need not lie in $\mathbb{M}_-$ — for example $(ie_0)(ie_0) = -e_0$, whose scalar part is real, so the product lies outside. It **is** closed under the commutator $[\tilde{Q},\tilde{Y}] = \tilde{Q}\tilde{Y} - \tilde{Y}\tilde{Q}$, so with that bracket $\mathbb{M}_-$ is a Lie algebra of dimension $4$. This is the structural reason the four-vectors have a Lie-algebraic life alongside their vector-space life.

### The Defining Involution

The subspace is the fixed space of the **anti-Hermitian conjugation**

$$
\tilde{Q}^\flat = -\tilde{Q}^\dagger = -\bar{\tilde{Q}}^{\,*},
$$

which is an involution: applying it twice returns the original element, $(\tilde{Q}^\flat)^\flat = \tilde{Q}$. Write the general biquaternion out in full, with the real and the imaginary part of each of its four coefficients,

$$
\tilde{Q} = (q_0 + iq'_0)\,e_0 + (q_1 + iq'_1)\,e_1 + (q_2 + iq'_2)\,e_2 + (q_3 + iq'_3)\,e_3, \qquad q_\mu, q'_\mu \in \mathbb{R}.
$$

The conjugation is the composite of quaternion conjugation and complex conjugation. Quaternion conjugation negates the three vector units and leaves the unit, the scalar imaginary, and every coefficient untouched,

$$
\bar{\tilde{Q}} = (q_0 + iq'_0)\,e_0 - (q_1 + iq'_1)\,e_1 - (q_2 + iq'_2)\,e_2 - (q_3 + iq'_3)\,e_3,
$$

and complex conjugation then replaces $i$ by $-i$ throughout, leaving the quaternion units fixed, so that

$$
\bar{\tilde{Q}}^{\,*} = (q_0 - iq'_0)\,e_0 - (q_1 - iq'_1)\,e_1 - (q_2 - iq'_2)\,e_2 - (q_3 - iq'_3)\,e_3 = \tilde{Q}^\dagger .
$$

Negating this gives the anti-Hermitian conjugation itself,

$$
\tilde{Q}^\flat = -\tilde{Q}^\dagger = (-q_0 + iq'_0)\,e_0 + (q_1 - iq'_1)\,e_1 + (q_2 - iq'_2)\,e_2 + (q_3 - iq'_3)\,e_3 ,
$$

so that the scalar coefficient is negated in its real part and each vector coefficient in its imaginary part. Coordinate by coordinate,

| | $q_0$ | $q'_0$ | $q_1$ | $q'_1$ | $q_2$ | $q'_2$ | $q_3$ | $q'_3$ |
|---|---|---|---|---|---|---|---|---|
| image under $\flat$ | $-q_0$ | $q'_0$ | $q_1$ | $-q'_1$ | $q_2$ | $-q'_2$ | $q_3$ | $-q'_3$ |
| $\tilde{Q}^\flat = \tilde{Q}$ requires | $q_0 = 0$ | free | free | $q'_1 = 0$ | free | $q'_2 = 0$ | free | $q'_3 = 0$ |

**The fixed space.** The two sides of $\tilde{Q}^\flat = \tilde{Q}$ must agree in each of the four units $e_0, e_1, e_2, e_3$, and within a unit they must agree separately in the real and the imaginary part. That is four complex conditions, hence eight real ones, and they read

$$
-q_0 + iq'_0 = q_0 + iq'_0 \iff q_0 = 0, \qquad
q_k - iq'_k = q_k + iq'_k \iff q'_k = 0 \qquad (k = 1, 2, 3),
$$

the first from the scalar unit and the remaining three from the vector units. The solutions are the elements with $q_0 = 0$ and $q'_1 = q'_2 = q'_3 = 0$, that is,

$$
\tilde{Q}^\flat = \tilde{Q} \iff \tilde{Q} = iq'_0\,e_0 + q_1\,e_1 + q_2\,e_2 + q_3\,e_3 .
$$

**Conversely**, every element of this form is fixed. For such an element $\bar{\tilde{Q}} = iq'_0\,e_0 - q_1\,e_1 - q_2\,e_2 - q_3\,e_3$, hence $\tilde{Q}^\dagger = \bar{\tilde{Q}}^{\,*} = -iq'_0\,e_0 - q_1\,e_1 - q_2\,e_2 - q_3\,e_3 = -\tilde{Q}$, and therefore $\tilde{Q}^\flat = -\tilde{Q}^\dagger = \tilde{Q}$. The two directions together say that the displayed set is *exactly* the fixed space. The coordinates that survive are the four $q'_0, q_1, q_2, q_3$, which is the parametrisation recorded above: the scalar coefficient is purely imaginary, the three vector coefficients are real, and the fixed space is this four-dimensional real subspace, carved out of the eight real coordinates by the four $\mathbb{R}$-linear equations $q_0 = 0$ and $q'_k = 0$.

### Properties

The subspace $\mathbb{M}_-$ has the following algebraic properties, established in the basic algebra article.

**Quadratic form.** The biquaternion **norm form** restricts to a real quadratic form on $\mathbb{M}_-$:

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = (iq'_0)^2 + q_1^2 + q_2^2 + q_3^2 = -q'^2_0 + q_1^2 + q_2^2 + q_3^2 = -c^2t^2 + x^2 + y^2 + z^2.
$$

This is a real quadratic form of **signature** $(3,1)$: three positive directions (the spatial components $q_1, q_2, q_3$) and one negative direction (the temporal one, whose coordinate is $ict$). This is the Minkowski signature, expressed algebraically as a consequence of $i^2 = -1$.

**Zero divisors.** The norm form vanishes on the **light cone**

$$
q'^2_0 = q_1^2 + q_2^2 + q_3^2, \qquad \text{that is} \qquad c^2t^2 = x^2 + y^2 + z^2,
$$

a double cone with apex at the origin. The nonzero elements of this cone are **zero divisors** of $\mathbb{B}$ (see the companion article on biquaternion zero divisors). The complement of the cone has three connected components: the space-like region, together with the two components of the time-like region, future and past.

**Not a division algebra.** The presence of the zero divisor cone means that $\mathbb{M}_-$ is not a division algebra: there are nonzero elements of $\mathbb{M}_-$ that have no inverse. The physical significance of this is discussed below.

**Basis of the four-dimensional real space.** Every element of $\mathbb{M}_-$ is uniquely written as a linear combination of $ie_0, e_1, e_2, e_3$ with real coefficients. We may therefore identify $\mathbb{M}_-$ with $\mathbb{R}^4$, with the quadratic form $N$ corresponding to the Minkowski metric in the $(ict, x, y, z)$ convention.

**The parameter pattern.** The defining property of the sector is visible in the parameters alone: the scalar coefficient is imaginary and the three vector coefficients are real. Each of the four complex coefficients $Q_\mu = q_\mu + iq'_\mu$ therefore contributes exactly one real number, and the prime selects which one — for the scalar it is the imaginary part $q'_0$, for the three vectors the real parts $q_1, q_2, q_3$. This is why a single conjugation carves a four-dimensional real subspace out of an eight-dimensional real algebra: it fixes one real number in each complex coefficient, in the pattern imaginary-scalar, real-vector.

## Physical Meaning

### The Invariant Interval and the Minkowski Metric

The **invariant interval** between two nearby events in spacetime is the quadratic form associated with the displacement biquaternion $d\tilde{Q} \in \mathbb{M}_-$:

$$
ds^2 = N(d\tilde{Q}) = d\tilde{Q} \, \overline{d\tilde{Q}} = -(dq'_0)^2 + dq_1^2 + dq_2^2 + dq_3^2 = (ic\,dt)^2 + dx^2 + dy^2 + dz^2 = -c^2\,dt^2 + d\mathbf{x}^2.
$$

This is the biquaternion expression of the Minkowski interval, and it is the norm form, in agreement with the expression for $N$ obtained above. The interval is *not* the square $d\tilde{Q} \, d\tilde{Q}$: for $\tilde{Q} = iq'_0e_0 + \mathbf{q}$ one has $\tilde{Q} \, \tilde{Q} = -(q'^2_0 + |\mathbf{q}|^2) + 2iq'_0\mathbf{q}$, which is a biquaternion rather than a scalar. The square therefore carries a vector part and is not the interval.

The Lorentzian signature of the interval is not postulated: it arises algebraically from $i^2 = -1$ in the time component. This is the content of the $ict$ convention (see the companion article on the $ict$ convention). The biquaternion formulation makes explicit that the Lorentzian structure of spacetime is a **consequence of a complex structure** on the time coordinate, not an independent axiom.

The interval $ds^2$ has the following three possible signs, defining the three classes of Minkowski intervals:

- **Timelike** ($ds^2 < 0$): the events can be connected by a physical trajectory.
- **Spacelike** ($ds^2 > 0$): the events are causally disconnected.
- **Null** ($ds^2 = 0$): the events are connected by a light signal.

The null interval is the **light cone**, which is the zero divisor set of $\mathbb{M}_-$ (as discussed above).

### The Light Cone and the Zero Divisors

The **light cone** is the set of four-vectors $\tilde{Q} \in \mathbb{M}_-$ with vanishing norm form:

$$
N(\tilde{Q}) = 0 \quad \Longleftrightarrow \quad q'^2_0 = q_1^2 + q_2^2 + q_3^2 \quad \Longleftrightarrow \quad c^2t^2 = x^2 + y^2 + z^2,
$$

where $q'_0$ is the (real) time component and $q_1, q_2, q_3$ are the spatial components — the sector-parameter writing on the left, the coordinate writing on the right. This is a double cone in $\mathbb{R}^4$ with apex at the origin.

The nonzero elements of the light cone are **zero divisors** of the biquaternion algebra: they are nonzero elements $\tilde{Q}$ for which there exists a nonzero $\tilde{Y}$ with $\tilde{Q}\tilde{Y} = 0$. The zero divisor structure is intrinsic to the biquaternion algebra and reflects the fact that the light cone is the **characteristic cone** of the wave operator $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$.

From the physical point of view, the zero divisors of $\mathbb{M}_-$ are the **null four-vectors**: the four-vectors of light signals, which have zero rest mass and propagate at the speed of light. The massless particles of relativistic physics correspond to the zero divisors of the biquaternion algebra. This is a structural fact of the algebra, not an additional assumption.

## Advanced Algebraic Properties

### The Lorentz Group

The four-vectors of physics transform under the Lorentz group by **rotor conjugation**:

$$
\tilde{Q}' = \tilde{\Lambda}\,\tilde{Q}\,\tilde{\Lambda}^\dagger,
$$

where $\tilde{\Lambda}$ is a **unit-norm biquaternion**, i.e. an element of the group $SL(2,\mathbb{C}) \subset \mathbb{B}$ satisfying $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$. The rotor $\tilde{\Lambda}$ is Hermitian (i.e. $\tilde{\Lambda}^\dagger = \tilde{\Lambda}$) for a pure boost, and a real quaternion for a pure spatial rotation. For a general Lorentz transformation, $\tilde{\Lambda}$ is a general unit-norm biquaternion in $\mathbb{B}$.

The full development of the Lorentz transformation, including the boost biquaternion, its relation to the four-velocity, and its action on the four-potential, is the subject of the companion article. Here we only recall that the rotor conjugation **preserves** $\mathbb{M}_-$: if $\tilde{Q} \in \mathbb{M}_-$ and $\tilde{\Lambda}$ is a unit-norm biquaternion, then $\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^\dagger \in \mathbb{M}_-$.

This is the biquaternion expression of the statement that the Lorentz group acts on the four-vector space and leaves it invariant. The rotor $\tilde{\Lambda}$ is a general unit-norm biquaternion in $\mathbb{B}$, Hermitian for pure boosts and real for pure rotations; the space on which the rotor acts is $\mathbb{M}_-$.

## Examples

The reason $\mathbb{M}_-$ is the "material subspace" is that the physical four-vectors of relativistic physics all lie in it. This is a structural fact: the four-vectors are elements of the same four-dimensional real vector space, with the same quadratic form, and the same transformation law under the Lorentz group.

The following table lists the seven physical four-vectors that live in $\mathbb{M}_-$. Each is expressed as an element of $\mathbb{M}_-$ with its standard physical interpretation.

| Four-vector | Biquaternion form | Components |
|---|---|---|
| Four-position | $\tilde{Q} = iq'_0e_0 + q_ke_k = ic\,t\,e_0 + \mathbf{x}$ | $(ict, \mathbf{x})$, i.e. $(q'_0, q_k) = (ct, x_k)$ |
| Four-velocity | $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ | $(\gamma ic, \gamma\mathbf{v})$ |
| Four-momentum | $\tilde{P} = m\tilde{U} = iE/c\,e_0 + \mathbf{p}$ | $(iE/c, \mathbf{p})$ |
| Four-force | $\tilde{F} = d\tilde{P}/d\tau$ | $(i\gamma\,\mathbf{f}\cdot\mathbf{v}/c, \gamma\mathbf{f})$ |
| Four-potential | $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$ | $(i\phi/c, \mathbf{A})$ |
| Four-current | $\tilde{J} = ic\rho\,e_0 + \mathbf{j}$ | $(ic\rho, \mathbf{j})$ |
| Four-wavevector | $\tilde{K} = i\omega/c\,e_0 + \mathbf{k}$ | $(i\omega/c, \mathbf{k})$ |

In each case, the scalar part is purely imaginary and the vector part is real, matching the structure of $\mathbb{M}_-$.

The formulas for these four-vectors and their mutual relations (the mass-shell relation, the conservation laws, the wave equations) are collected in the companion article on relativistic mechanics. Here we only note that **they all live in the same subspace**. This is the structural content of the observation that relativistic physics is naturally expressed in $\mathbb{M}_-$.

### The Common Structure

The four-vectors share the following structural features, which are the reasons they lie in $\mathbb{M}_-$.

**1. Imaginary scalar part.** The time component of each four-vector is written as $i$ times a real quantity: $ict$, $i\gamma c$, $iE/c$, $i\phi/c$, $ic\rho$, $i\omega/c$. The factor of $i$ is the marker that distinguishes the temporal component from the spatial components. This is the $ict$ convention, and it is the reason the metric on $\mathbb{M}_-$ has signature $(3,1)$ rather than being positive-definite.

**2. Real vector part.** The spatial components are real. They are the components in the three real directions $e_1, e_2, e_3$ of ordinary physical space.

**3. Lorentz covariance.** The four-vectors transform under the Lorentz group by the **rotor conjugation**

$$
\tilde{Q} \;\longmapsto\; \tilde{\Lambda}\,\tilde{Q}\,\tilde{\Lambda}^\dagger.
$$

The rotor $\tilde{\Lambda}$ is a unit-norm biquaternion, i.e. an element of the group $SL(2,\mathbb{C}) \subset \mathbb{B}$. The group lives in the full algebra $\mathbb{B}$, not in any single subspace (since $\mathbb{M}_-$ and $\mathbb{M}_+$ are not closed under multiplication). The different types of Lorentz transformation have rotors in different subspaces: **pure boosts** have rotors in $\mathbb{M}_+$ (they are Hermitian), **pure spatial rotations** have rotors in $\mathbb{H}_{\mathbb{B}}$ (they are real quaternions), and **general Lorentz transformations** have rotors in the full algebra $\mathbb{B}$.

**4. Invariant norm.** Each four-vector has an invariant norm under the Lorentz group, equal to the norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ evaluated on the four-vector. This is the biquaternion expression of the relativistic invariants: the interval for the four-position, $-c^2$ for the four-velocity, $-m^2 c^2$ for the four-momentum, and $0$ for the four-wavevector of light. The four-potential and the four-current are different in kind: the invariant statements associated with them are the gauge condition $\partial_\mu A^\mu = 0$ and the conservation law $\partial_\mu J^\mu = 0$, which constrain the divergence of the four-vector, not its norm form. The norm form $\tilde{A}\bar{\tilde{A}}$ vanishes only for a radiation field in the null gauge, and $\tilde{J}\bar{\tilde{J}}$ vanishes only for a null current, $|\mathbf{j}| = c\rho$.

## Summary

The anti-Hermitian subspace $\mathbb{M}_-$ is a four-dimensional real subspace of the biquaternion algebra, consisting of elements with imaginary scalar part and real vector part. Its norm form has signature $(3,1)$, matching the Minkowski metric in the $ict$ convention. The Lorentzian signature is not postulated: it arises algebraically from $i^2 = -1$ in the imaginary scalar part.

The subspace $\mathbb{M}_-$ is the natural home of the four-vectors of relativistic physics:

- The four-position $\tilde{Q} = iq'_0e_0 + q_ke_k = ict\,e_0 + \mathbf{x}$, with $q'_0 = ct$ and $q_k = x_k$.
- The four-velocity $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$.
- The four-momentum $\tilde{P} = m\tilde{U}$.
- The four-force $\tilde{F} = d\tilde{P}/d\tau$.
- The four-potential $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$.
- The four-current $\tilde{J} = ic\rho\,e_0 + \mathbf{j}$.
- The four-wavevector $\tilde{K} = i\omega/c\,e_0 + \mathbf{k}$.

Each has an imaginary scalar part (the time component) and a real vector part (the spatial components). Each transforms under the Lorentz group by rotor conjugation, with the rotor a general unit-norm biquaternion in $\mathbb{B}$ (Hermitian for a pure boost, a real quaternion for a pure spatial rotation).

The **light cone** of Minkowski space is the zero divisor cone of $\mathbb{M}_-$: the null four-vectors of light-like propagation are exactly the zero divisors of the biquaternion algebra. This is a structural fact of the algebra, not an additional assumption.

The subspace $\mathbb{M}_-$ is specifically the **vector representation** of the Lorentz group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector): imaginary scalar, real vector; parameters $q'_0, q_1, q_2, q_3$, with $q'_0 = ct$ |
| $Q_\mu = q_\mu + iq'_\mu$ | Complex coefficient of $e_\mu$: $q_\mu$ its real part, $q'_\mu$ its imaginary part |
| $\tilde{Q} = iq'_0e_0 + q_ke_k = ict\,e_0 + \mathbf{x}$ | Material element, both writings; $q'_0 = ct$, $q_k = x_k$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $s^2 = N(d\tilde{Q}) = d\tilde{Q}\,\overline{d\tilde{Q}}$ | Invariant interval |
| $\tilde{\Lambda} \in \mathbb{B}$, $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$ | Lorentz rotor (unit-norm biquaternion) |
| $\tilde{Q}' = \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^\dagger$ | Rotor conjugation |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the original four-dimensional formulation of spacetime.
- Albert Einstein, *The Meaning of Relativity* (Princeton, 1922), for the $ict$ formulation of special relativity.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the standard four-vector formulation of relativistic physics.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the four-vector and tensor formulation of electromagnetism.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection between Clifford algebras and Minkowski space.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra formulation of special relativity.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of spacetime algebra.
- *Conventions in the Biquaternion Universe* and *Relations Between Subspaces*, the companion articles, for the notation and for the place of $\mathbb{M}_-$ among the six subspaces.

