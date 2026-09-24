# __The Relativistic Particle in Biquaternionic Form__

## Introduction

The relativistic particle is the simplest physical object the biquaternion framework has to describe: a single point mass with no structure, moving on a worldline. Everything about it is kinematic. It has a position, a four-velocity, a four-momentum and a mass-shell relation; it has no spin, no internal coordinates, and no field of its own. This makes it the natural first object of the non-quantum theory, and it is the object against which every later construction is calibrated.

Two facts from the algebra organize the whole account, and they are worth stating at the outset.

**The interval is the norm form.** The material coordinate is the anti-Hermitian biquaternion $\tilde{X} = ict\,e_0 + \mathbf{x} \in \mathbb{M}_-$, with $\mathbf{x} = x e_1 + y e_2 + z e_3$, and the Minkowski interval of a displacement is the norm form

$$
N(d\tilde{X}) = d\tilde{X}\,d\overline{\tilde{X}} = (ic\,dt)^2 + d\mathbf{x}^2 = -c^2dt^2 + d\mathbf{x}^2 .
$$

The algebra therefore does not carry a metric that has to be attached to spacetime from outside; its own norm form, restricted to the real four-dimensional subspace $\mathbb{M}_-$, *is* the Minkowski form. This is the level-1 identity form $\mathrm{diag}(+1,+1,+1,+1)$ on $\mathbb{B}$, whose restriction to the real material slice is the level-2 form $\eta = \mathrm{diag}(-1,+1,+1,+1)$; both levels are fixed by the companion article *Conventions in the Biquaternion Universe*, and no metric is introduced here beyond them.

**The three causal types are the three signs of the norm form.** A displacement is timelike, null or spacelike according to whether $N$ is negative, zero or positive. The particle of this article is the timelike case: its tangent stays strictly inside the null cone, and the norm form of its tangent is a fixed negative constant. The null case, and the cone that separates the two, is the subject of the companion article *The Light Cone as the Biquaternion Zero-Divisor Cone*.

The article is organized as follows. The next section fixes the worldline and the proper time from the norm form. The third introduces the four-velocity and the rapidity. The fourth gives the four-momentum and the mass shell. The fifth treats composition of velocities. The sixth derives the free action and its equation of motion. The seventh takes the non-relativistic limit. The closing sections separate what the algebra supplies from what is transcribed, collect the open questions, and record the summary, the notation and the external literature.

**Conventions.** We use those of the read list unchanged. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_je_k = -\delta_{jk}e_0 + \varepsilon_{jkl}e_l$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian: imaginary scalar and real vector — the material sector), $\mathbb{M}_+$ (Hermitian: real scalar and imaginary vector — the informational sector), $\mathbb{H}_{\mathbb{B}}$ (the real-quaternion subspace) and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ (the complex scalar line, the center). The conjugations are $\bar{\cdot}$ (quaternion), ${}^*$ (complex), ${}^\dagger = \bar{\cdot}^{\,*}$ (Hermitian) and ${}^\flat = -\dagger$ (anti-Hermitian). The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \partial_{ict}^2 + \Delta$. The norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ its vacuum value; the symbol $\mathbf{v}$ is reserved for particle and frame velocities, as in the neighbouring articles. The trace formula is $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$.

## The Worldline and the Norm Form

A relativistic particle is described by a curve in the material sector,

$$
\tilde{X}(\lambda) : \lambda \longmapsto \tilde{X}(\lambda) = ic\,t(\lambda)\,e_0 + \mathbf{x}(\lambda) \in \mathbb{M}_- ,
$$

with $\lambda$ an arbitrary parameter. The physical content of the curve is not the arbitrary parametrization but the displacement one-form

$$
d\tilde{X} = ic\,dt\,e_0 + d\mathbf{x},
$$

whose norm form is

$$
N(d\tilde{X}) = d\tilde{X}\,d\overline{\tilde{X}} = -c^2dt^2 + d\mathbf{x}^2 .
$$
<!-- CONVENTION — norm form on the material sector: N(dX) = dX dXbar = -c^2 dt^2 + dx^2. The minus sign comes from the ict coordinate, (ic dt)^2 = -c^2 dt^2, not from a choice of metric. The level-1 identity form diag(+1,+1,+1,+1) on B restricts to the level-2 Minkowski form eta = diag(-1,+1,+1,+1) on the real material slice. Do not "correct" the sign by importing a direct Euclidean metric on (t,x). -->

Off the null set, $N(d\tilde{X})$ has the sign of $-d\tau^2$ for a real number $d\tau$, and the **proper time** is defined by

$$
\boxed{\; c^2\,d\tau^2 = -\,N(d\tilde{X}) = c^2dt^2 - d\mathbf{x}^2 \;}
\qquad\Longrightarrow\qquad
d\tau = dt\sqrt{1 - \frac{\mathbf{v}^2}{c^2}},
\qquad \mathbf{v} = \frac{d\mathbf{x}}{dt} .
$$

The definition is real precisely when the worldline is timelike, $N(d\tilde{X}) < 0$, and it is the condition that fixes which curves describe a particle of nonzero rest mass. The three cases are the three signs of the norm form:

$$
\text{timelike: } N<0,
\qquad
\text{null: } N=0,
\qquad
\text{spacelike: } N>0 .
$$

Two structural remarks. First, $d\tau$ is real and positive for a future-directed timelike curve, and it is a scalar under the rotor conjugation that implements the Lorentz group (the companion article *The Lorentz Transformation as a Biquaternionic Rotation*), because $N$ is preserved by that action; this is what makes it a usable parameter. Second, the definition is invariant under reparametrization, so a worldline carries a canonical affine parameter up to an additive constant, and it is by $d\tau$ that the four-velocity is normalized below.

The curve is **causal** if $N(d\tilde{X}) \leq 0$ everywhere and **timelike** if the inequality is strict. A physical particle has a timelike worldline, and the statement that no signal exceeds $c$ is the statement that its tangent never leaves the interior of the null cone. Nothing in this article requires the curve to be straight; acceleration is admitted, and the four-force that produces it is treated in the companion articles *The Lorentz Force in Biquaternion Form* and *The Relativistic Particle in an External Field, in Biquaternionic Form*.

## The Four-Velocity and the Rapidity

The **four-velocity** is the tangent with respect to proper time,

$$
\tilde{U} = \frac{d\tilde{X}}{d\tau}
= \frac{dt}{d\tau}\left(ic\,e_0 + \frac{d\mathbf{x}}{dt}\right)
= \gamma\left(ic\,e_0 + \mathbf{v}\right),
\qquad
\gamma = \frac{dt}{d\tau} = \frac{1}{\sqrt{1-\mathbf{v}^2/c^2}} .
$$

It lies in $\mathbb{M}_-$ because both terms do: $ic\,e_0$ is the imaginary scalar direction of the material sector and $\mathbf{v}$ is a real vector. Its norm form is the defining normalization of the parameter:

$$
N(\tilde{U}) = \tilde{U}\,\overline{\tilde{U}}
= \gamma^2\left[(ic)^2 + \mathbf{v}^2\right]
= \gamma^2\left(-c^2 + \mathbf{v}^2\right)
= -c^2\gamma^2\left(1 - \frac{\mathbf{v}^2}{c^2}\right) = -c^2 .
$$

The four-velocity is therefore a **unit timelike vector**: its tip runs over the future sheet of the hyperboloid $N(\tilde{U}) = -c^2$ inside $\mathbb{M}_-$.

The relation between the four-velocity and the ordinary velocity is worth reading as a statement about the algebra rather than about motion. The two real data $\gamma$ and $\mathbf{v}$ combine into one element of $\mathbb{M}_-$; the constraint $N = -c^2$ removes one real degree of freedom, leaving the three components of $\mathbf{v}$ as the independent data, exactly as it must. The time component is then not independent: it is fixed by the three-velocity through

$$
\mathrm{Sc}(\tilde{U}) = ic\,\gamma = ic\,\frac{1}{\sqrt{1-\mathbf{v}^2/c^2}} .
$$

It is convenient to parametrize the hyperboloid by the **rapidity** $\psi$, defined by

$$
v = c\tanh\psi,
\qquad
\gamma = \cosh\psi,
\qquad
\gamma v = c\sinh\psi,
$$

so that

$$
\tilde{U} = \cosh\psi\,(ic\,e_0) + \sinh\psi\,(c\,\hat{\mathbf{u}})
= ic\cosh\psi\,e_0 + c\sinh\psi\,\hat{\mathbf{u}},
$$

with $\hat{\mathbf{u}} = \mathbf{v}/v$ the unit direction of motion. In this parametrization the normalization $N(\tilde{U}) = -c^2$ reads $c^2(-\cosh^2\psi + \sinh^2\psi) = -c^2$, which is an identity. The rapidity is the additive parametrization of the velocity: for motion along a fixed direction the composition of two velocities corresponds to the sum of their rapidities,

$$
\psi_{\mathrm{tot}} = \psi_1 + \psi_2,
\qquad
\frac{v_1 + v_2}{1 + v_1v_2/c^2} = c\tanh(\psi_1+\psi_2),
$$

which is the standard velocity-addition law and is reproduced by the rotor composition of the next section. That the additive variable is a hyperbolic angle, and not the velocity itself, is the algebraic statement that the mass-shell hyperboloid is not a vector space.

## The Four-Momentum and the Mass Shell

The **four-momentum** of a particle of rest mass $m$ is the four-velocity scaled by the mass,

$$
\tilde{P} = m\tilde{U} = \gamma m\left(ic\,e_0 + \mathbf{v}\right)
= i\,\frac{E}{c}\,e_0 + \mathbf{p},
\qquad
E = \gamma mc^2,
\qquad
\mathbf{p} = \gamma m\mathbf{v},
$$

so that the energy is the imaginary scalar part multiplied by $-ic$ — equivalently, the physical energy is $E = -ic\,\mathrm{Sc}(\tilde{P})$ — and the momentum is the real vector part. The four-momentum lies in $\mathbb{M}_-$. Its norm form is the **mass-shell relation**:

$$
\boxed{\; N(\tilde{P}) = \tilde{P}\,\overline{\tilde{P}} = -\frac{E^2}{c^2} + \mathbf{p}^2 = -m^2c^2 \;}
\qquad\Longleftrightarrow\qquad
E^2 = \mathbf{p}^2c^2 + m^2c^4 .
$$

This is one of the few places in the framework where an equation of physics is *identical* to an algebraic statement about the norm form: the mass shell is the level set $N(\tilde{P}) = -m^2c^2$, and the dispersion relation is its coordinate form. The rest mass is, up to the factor $-c^2$, the norm form of the four-momentum; the massless case is where the norm form vanishes, which is the zero-divisor cone.

The geometric content is worth drawing out. In the four real coordinates $(E/c, p_x, p_y, p_z)$ the relation $E^2 = \mathbf{p}^2c^2 + m^2c^4$ is a two-sheeted hyperboloid, and only the future sheet $E \geq mc^2$ is the particle's. The four-momentum is future-directed and timelike:

$$
N(\tilde{P}) = -m^2c^2 < 0
\qquad (m > 0),
$$

and the invariant $N(\tilde{P})$ is what the Lorentz group preserves, so the classification of a particle as massive is frame-independent. The relation between the two energy equations is worth recording: in the rest frame $\mathbf{p} = 0$ and $E = mc^2$, so the imaginary scalar part of the four-momentum at rest is $i mc$, which is the rest energy in the $ict$ convention.

Two limits fix the picture. As $m\to 0$ with $\mathbf{p}$ held fixed the mass shell collapses onto the null cone $N(\tilde{P}) = 0$, and the particle becomes the zero divisor of the companion article *The Light Cone as the Biquaternion Zero-Divisor Cone*. As $v\ll c$ the energy separates into the rest energy and the kinetic term,

$$
E = \gamma mc^2 = mc^2 + \tfrac12 m\mathbf{v}^2 + O(\mathbf{v}^4/c^2),
$$

which is the subject of the penultimate section.

## Composition of Velocities

A Lorentz transformation acts on the material sector by **rotor conjugation**,

$$
\tilde{X}\ \longmapsto\ \tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^\dagger,
\qquad
\tilde{\Lambda}\in\mathbb{B},
\qquad
\tilde{\Lambda}\overline{\tilde{\Lambda}} = e_0,
$$

with $\tilde{\Lambda}$ a unit-norm biquaternion. Since the action is linear and preserves $N$, it maps a four-velocity to a four-velocity, and it maps the mass shell to itself; it is the framework's implementation of a change of inertial frame. For a **pure boost** the rotor is Hermitian and lives in $\mathbb{M}_+$,

$$
\tilde{\Lambda}(\psi,\hat{\mathbf{u}}) = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}},
\qquad
\overline{\tilde{\Lambda}} = \tilde{\Lambda}^\dagger ,
$$

with $\psi$ the rapidity and $\hat{\mathbf{u}}$ the boost direction. The convention for which rotor carries which frame is fixed by the companion article *The Lorentz Transformation as a Biquaternionic Rotation*, whose rotor for a particle of four-velocity $\tilde{U}$ is $\tilde{\Lambda} = \sqrt{-\tfrac{i}{c}\bar{\tilde{U}}}$, with the boost direction aligned with the particle velocity. With that rotor, the transformation $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ carries the four-velocity $\gamma(ic\,e_0+\mathbf{v})$ of a particle moving with velocity $\mathbf{v} = c\tanh\psi\,\hat{\mathbf{u}}$ to the rest four-velocity $ic\,e_0$.

Composition of two boosts is composition of their rotors. For two **collinear** boosts the rotors commute and their rapidities add: if the first has rapidity $\psi_1$ and the second $\psi_2$ along the same direction, the product is the boost of rapidity $\psi_1+\psi_2$, and the composed velocity is

$$
v_{\mathrm{tot}} = c\tanh(\psi_1+\psi_2) = \frac{v_1+v_2}{1+v_1v_2/c^2},
$$

which is the standard addition law. The verification is elementary in the quaternion algebra: the boost rotor of rapidity $\psi$ along $\hat{\mathbf{u}}$ acts on the rest four-velocity as

$$
\tilde{\Lambda}\,\bigl(ic\,e_0\bigr)\,\tilde{\Lambda}^\dagger
= ic\,e_0\,\tilde{\Lambda}^2
= ic\left(\cosh\psi\,e_0 + i\sinh\psi\,\hat{\mathbf{u}}\right)
= ic\cosh\psi\,e_0 - c\sinh\psi\,\hat{\mathbf{u}}
= \gamma\left(ic\,e_0 - \mathbf{v}\right),
$$

using that $ic\,e_0$ is central, that $\tilde{\Lambda}^\dagger = \tilde{\Lambda}$ for a pure boost, and that $\tilde{\Lambda}^2 = \cosh\psi + i\sinh\psi\,\hat{\mathbf{u}}$. The quaternion-conjugate rotor $\bar{\tilde{\Lambda}} = \cosh\frac{\psi}{2} - i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$, which is the boost of rapidity $-\psi$, carries the rest four-velocity to $\gamma(ic\,e_0+\mathbf{v})$ instead. Composing two such rotors and reading off the resulting rapidity gives the addition law above. The rapidity is additive because it is half the logarithm of the ratio of the light-cone coordinates, and that additivity is exactly what the hyperbolic parametrization was built to display.

For **non-collinear** boosts the rotors do not commute, and their product is not a pure boost: it is a boost together with a rotation. The rotation is the Thomas–Wigner rotation, and it is the group-theoretic statement that the boosts do not form a subgroup. It is not needed for the free particle's kinematics, and it is treated in its own right in the companion article *The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form*; here it is enough to record that the free four-velocity composes by rotor multiplication, and that the composition is associative while the velocity addition it induces is not.

## The Free Action

The action of a free relativistic particle is the invariant length of its worldline, measured in units of $mc$:

$$
S[\tilde{X}] = -mc\int\sqrt{-\,d\tilde{X}\,d\overline{\tilde{X}}}
= -mc\int\sqrt{-N(d\tilde{X})}
= -mc^2\int\frac{dt}{\gamma} .
$$

The sign is fixed by the requirement that a free particle move forward in time with positive energy, and the square root is real on a causal worldline by the definition of the proper time. In terms of the coordinate velocity the Lagrangian is

$$
L(\mathbf{v}) = -mc^2\sqrt{1-\mathbf{v}^2/c^2} = -\frac{mc^2}{\gamma} .
$$

The canonical momentum conjugate to $\mathbf{x}$ is the vector part of the four-momentum,

$$
\frac{\partial L}{\partial\mathbf{v}}
= -mc^2\cdot\frac{-\mathbf{v}/c^2}{\sqrt{1-\mathbf{v}^2/c^2}}
= \gamma m\mathbf{v} = \mathbf{p},
$$

so the free Lagrangian's canonical momentum is the physical momentum. Its Legendre transform is the free energy $E = \mathbf{p}\cdot\mathbf{v} - L = \gamma mc^2$, and the equation of motion is the vanishing of the Euler–Lagrange derivative,

$$
\frac{d}{dt}\frac{\partial L}{\partial\mathbf{v}} - \frac{\partial L}{\partial\mathbf{x}} = \frac{d\mathbf{p}}{dt} = 0 ,
$$

so the free four-momentum $\tilde{P} = m\tilde{U}$ is constant. The same statement in the four-dimensional language is that the free worldline is the straight timelike line,

$$
\frac{d\tilde{P}}{d\tau} = m\frac{d^2\tilde{X}}{d\tau^2} = 0 ,
$$

the geodesic of flat $\mathbb{M}_-$. In the algebra the action is exactly the length functional of the norm form, and the four-momentum is exactly its Noether charge under translations; the companion article *Noether's Theorem in Biquaternionic Form* derives the charge from the translation invariance of this action.

The action has the two properties that make it the starting point of the theory. It is a Lorentz scalar, because $N(d\tilde{X})$ is preserved by rotor conjugation and $d\tau$ is the invariant parameter; and it is reparametrization invariant, so it depends on the worldline and not on the choice of $\lambda$. A particle with charge, or in an external field, adds the minimal-coupling term to this action, which is the content of *The Relativistic Particle in an External Field, in Biquaternionic Form*.

## The Non-Relativistic Limit

Expanding the four-velocity and the energy in powers of $\mathbf{v}^2/c^2$ recovers the non-relativistic description as the leading term of the algebra. The spatial part of the four-velocity is

$$
\tilde{U} = \gamma\left(ic\,e_0 + \mathbf{v}\right)
= ic\,e_0 + \mathbf{v} + O(\mathbf{v}^3/c^2),
$$

so the imaginary scalar component becomes the constant $ic$ and the vector component becomes the ordinary velocity. The four-momentum becomes

$$
\tilde{P} = i\,\frac{E}{c}\,e_0 + \mathbf{p}
= i\,mc\,e_0 + m\mathbf{v} + O(\mathbf{v}^3/c^2),
$$

with the mass shell reducing to

$$
E = mc^2 + \frac{\mathbf{p}^2}{2m} + O(p^4/m^3c^2),
\qquad
\mathbf{p} = m\mathbf{v} + O(v^3/c^2).
$$

The rest energy $mc^2$ is the constant imaginary scalar part; it is a constant of the motion in the non-relativistic limit and is dropped, leaving the kinetic energy $p^2/2m$. The norm form of the four-momentum is exactly $-m^2c^2$ in the relativistic theory, and the non-relativistic expansion preserves it through a cancellation between the two terms. Expanding each separately,

$$
-\frac{E^2}{c^2} = -m^2c^2 - m^2\mathbf{v}^2 + O(v^4/c^2),
\qquad
\mathbf{p}^2 = m^2\mathbf{v}^2 + O(v^4/c^2),
$$

so that

$$
N(\tilde{P}) = -\frac{E^2}{c^2} + \mathbf{p}^2 = -m^2c^2 + O(v^4/c^2).
$$

The leading corrections cancel because the mass shell is an exact relation: the kinetic energy $\tfrac12 m\mathbf{v}^2$ in $E$ and the momentum $\mathbf{p} = m\mathbf{v}$ are the two halves of the same invariant. The norm form does not vanish in the non-relativistic limit — the particle stays well inside the cone, at an invariant distance $m^2c^2$ from the apex — and the non-relativistic theory is in this sense the interior approximation of the relativistic one. It is the same comparison the companion article *The Light Cone as the Biquaternion Zero-Divisor Cone* draws from the momentum-space side.

## What the Algebra Supplies and What It Transcribes

**Supplied by the algebra.** The identification of the interval with the norm form, and therefore the identity of the causal trichotomy with the sign of $N$; the placement of the worldline, the four-velocity and the four-momentum in the material sector $\mathbb{M}_-$; the normalization $N(\tilde{U}) = -c^2$ as an algebraic unit condition rather than a separate postulate; and the packaging of the velocity and the frame transformation in a single rotor. The mass shell $N(\tilde{P}) = -m^2c^2$ is a level set of the algebra's own form.

**Transcribed from standard physics.** The proper-time definition, the Lorentz factor, the velocity-addition law, the Lagrangian $L = -mc^2/\gamma$, the canonical momentum, the dispersion relation and the non-relativistic expansion are standard relativistic mechanics, and the biquaternion formulation reproduces them rather than replacing them. The parameter $c$ and the mass $m$ are inputs; the algebra supplies the home of each object but not its value.

**Interpretation.** The reading of $\mathbb{M}_-$ as the material sector, and of a timelike worldline in it as a physical particle, is the framework's structural hypothesis, stated in the foundational articles *Introduction to the Biquaternion Universe* and *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*. The kinematic statements above are exact and standard; the hypothesis is what gives them their sector reading.

## Open Questions

1. **The action's normalization in a medium.** The medium speed $c = 1/\sqrt{\epsilon\mu}$ enters the proper time and the action as the local scale. Is the free-particle action in a medium strictly the length functional of the local norm form, or does a dispersive medium require the particle's mass to be renormalized to the local $c$? The framework treats $c$ as local but does not fix the dynamical origin of the medium.

2. **Accelerated worldlines and the cone.** A uniformly accelerated worldline has a horizon — the Rindler horizon — which is a null surface. Does the zero-divisor cone of the next article acquire a distinguished role for accelerated observers, and can the horizon be written as a level set of a Killing norm form in $\mathbb{M}_-$?

3. **The many-particle problem.** The four-velocity and four-momentum here are those of a single particle. The proper-time normalization does not sum across particles with different Lorentz factors; the multi-particle conservation statement requires the coordinate-time form of the companion article *Exercise: Four-Momentum Conservation in a Collision*, and a clean biquaternion many-body kinematics is not developed here.

4. **Rest mass as a norm.** The identity $N(\tilde{P}) = -m^2c^2$ makes the rest mass the norm form of the momentum. Does the framework constrain the possible mass spectrum in any way, or is $m$ an arbitrary parameter of the same kind as in the standard theory?

5. **Coupling to the informational sector.** The particle is described entirely in $\mathbb{M}_-$. Whether there is a kinematical coupling between a worldline and the informational sector $\mathbb{M}_+$ — beyond the Lorentz action of the rotor — is not addressed here; it is the central open question of the foundational article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, and it is outside the scope of a classical kinematic account.

The conventions of the construction are those of the following companion articles:

- Companion article *Introduction to the Biquaternion Universe*, for the notation, the norm form and the sector structure.
- Companion article *Conventions in the Biquaternion Universe*, for the algebra and basis, the four conjugations, the real subspaces and the metric at its three levels.
- Companion article *The Lorentz Transformation as a Biquaternionic Rotation*, for the boost rotor and the transformation of the four-vector.
- Companion article *The Lorentz Force in Biquaternion Form*, for the equation of motion in an external field.
- Companion article *The Relativistic Particle in an External Field, in Biquaternionic Form*, for the coupled particle–field system.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the conserved currents of the particle and the field.
- Companion article *Exercise: Four-Momentum Conservation in a Collision*, for the conservation kinematics used above.

## Summary

The relativistic particle is a timelike worldline in the material sector $\mathbb{M}_-$,

$$
\tilde{X}(\tau) = ic\,t\,e_0 + \mathbf{x},
\qquad
d\tau^2 = -\frac{1}{c^2}N(d\tilde{X}) = dt^2 - \frac{d\mathbf{x}^2}{c^2},
$$

along which the four-velocity

$$
\tilde{U} = \frac{d\tilde{X}}{d\tau} = \gamma\left(ic\,e_0 + \mathbf{v}\right),
\qquad
\gamma = \frac{1}{\sqrt{1-\mathbf{v}^2/c^2}},
$$

satisfies the unit-norm condition $N(\tilde{U}) = -c^2$. The four-momentum

$$
\tilde{P} = m\tilde{U} = i\,\frac{E}{c}\,e_0 + \mathbf{p},
\qquad
E = \gamma mc^2,
\quad
\mathbf{p} = \gamma m\mathbf{v},
$$

satisfies the mass-shell relation $N(\tilde{P}) = -m^2c^2$, equivalently $E^2 = \mathbf{p}^2c^2 + m^2c^4$. The rapidity $\psi$, with $v = c\tanh\psi$ and $\gamma = \cosh\psi$, makes the four-velocity $\tilde{U} = ic\cosh\psi\,e_0 + c\sinh\psi\,\hat{\mathbf{u}}$ and makes collinear velocity addition the sum of rapidities. The free action is the invariant length

$$
S[\tilde{X}] = -mc\int\sqrt{-\,d\tilde{X}\,d\overline{\tilde{X}}}
= -mc^2\int\frac{dt}{\gamma},
\qquad
L(\mathbf{v}) = -\frac{mc^2}{\gamma},
$$

whose canonical momentum is $\mathbf{p} = \gamma m\mathbf{v}$ and whose equation of motion is $\tilde{P} = \mathrm{const}$. The non-relativistic limit gives $\tilde{U} = ic\,e_0 + \mathbf{v}$, $E = mc^2 + \mathbf{p}^2/2m$ and $N(\tilde{P}) = -m^2c^2 + O(v^4/c^2)$.

The interval is the norm form, the mass shell is its level set, the causal trichotomy is its sign, and the frame transformation is a rotor conjugation; the rest is standard relativistic mechanics transcribed into the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra; quaternion basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}, \mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; complex scalar line (center) |
| $\bar{\cdot},\ {}^*,\ {}^\dagger=\bar{\cdot}^{\,*},\ {}^\flat=-\dagger$ | Quaternion, complex, Hermitian, anti-Hermitian conjugations |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form (level 1: identity on $\mathbb{C}$) |
| $\tilde{X} = ict\,e_0 + \mathbf{x}$ | Four-position, in $\mathbb{M}_-$ |
| $d\tau^2 = -N(d\tilde{X})/c^2$ | Proper time |
| $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$, $N(\tilde{U}) = -c^2$ | Four-velocity, unit timelike |
| $\gamma = 1/\sqrt{1-\mathbf{v}^2/c^2}$ | Lorentz factor |
| $\psi$, $v = c\tanh\psi$, $\gamma=\cosh\psi$ | Rapidity |
| $\tilde{P} = m\tilde{U} = iE/c\,e_0 + \mathbf{p}$ | Four-momentum |
| $E = \gamma mc^2$, $\mathbf{p} = \gamma m\mathbf{v}$ | Energy and momentum |
| $N(\tilde{P}) = -m^2c^2$ | Mass-shell relation |
| $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$, $\tilde{\Lambda}\bar{\tilde{\Lambda}}=e_0$ | Boost rotor, in $\mathbb{M}_+$ |
| $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ | Rotor conjugation on $\mathbb{M}_-$ |
| $S = -mc\int\sqrt{-d\tilde{X}\,d\bar{\tilde{X}}}$, $L = -mc^2/\gamma$ | Free action and Lagrangian |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the relativistic particle's action, proper time, four-momentum and mass shell.
- Wolfgang Rindler, *Relativity: Special, General, and Cosmological* (Oxford, 2006), for the worldline formulation, rapidity and velocity addition.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the relativistic kinematics of a particle and the relativistic Lagrangian.
- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the four-dimensional formulation of particle kinematics.
- Ludwik Silberstein, *The Theory of Relativity* (Macmillan, 1914), for the quaternion and complex-vector treatment of relativistic kinematics.
- E. T. Whittaker, *A History of the Theories of Aether and Electricity*, Vol. 2 (Nelson, 1953), for the historical development of relativistic particle dynamics.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of Lorentz transformations and the proper-time parametrization of worldlines.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the even-subalgebra treatment of relativistic kinematics.
