# __The Relativistic Two-Body Problem in Biquaternionic Form__

## Introduction

The companion article *Relativistic Mechanics in Biquaternionic Form* established the biquaternion dictionary for a single relativistic particle. The four-position, four-velocity, four-momentum, four-force, and four-current are elements of the anti-Hermitian subspace $\mathbb{M}_-$ of the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$; the mass-shell relation is the norm-form condition $\tilde{P}\bar{\tilde{P}} = -m^2c^2$; and the Lorentz transformation acts on four-vectors by rotor conjugation $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$, with $\tilde{\Lambda}$ a unit-norm biquaternion. The companion article *The Lorentz Transformation as a Biquaternionic Rotation* supplied the boost biquaternion and its relation to the four-velocity.

This article extends that dictionary to the simplest system of more than one body: **two relativistic bodies**. The two bodies carry four-momenta $\tilde{P}_1, \tilde{P}_2 \in \mathbb{M}_-$; their interaction is left unspecified, because the two-body problem at the level analysed here is a question of kinematics, and that is exactly the level at which it is a question about the algebra. Three features make the biquaternion formulation natural:

1. **The four-momenta add inside $\mathbb{M}_-$.** Since $\mathbb{M}_-$ is a real vector space, $\tilde{P} = \tilde{P}_1 + \tilde{P}_2$ is again an element of $\mathbb{M}_-$; its scalar–vector split is the split into total energy and total momentum.

2. **The pair's invariant mass is a norm form.** The mass of a single body is fixed by $N(\tilde{P}) = -m^2c^2$; the mass of the pair by the same operation applied to the sum, $N(\tilde{P}_1+\tilde{P}_2) = -M^2c^2$. No new primitive is needed.

3. **The centre-of-momentum frame is a rotor.** The frame in which the total three-momentum vanishes is reached by a single boost biquaternion built from $\tilde{P}_1+\tilde{P}_2$, exactly as the rest frame of a single particle is reached from its four-velocity.

The article is the foundation for the later exercise on the relativistic kinematics of a two-body decay, so the kinematics are worked out explicitly: the centre-of-momentum energies and momentum, the relative rapidity, the invariant mass, the boost to an arbitrary frame, and the reduction to an effective one-body problem. A decay is the special case in which the total four-momentum is that of a single body at rest.

The conventions are those of the companion articles: the algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$ and $e_k^2 = -e_0$; the scalar imaginary $i$ with $i^2 = -1$; the anti-Hermitian subspace $\mathbb{M}_-$ (imaginary scalar part, real vector part) and the Hermitian subspace $\mathbb{M}_+$; the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the complex subspace $\mathbb{C}_{\mathbb{B}}$; the norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$; and the rotor conjugation $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ with $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$, which implements the Lorentz transformation. Throughout, $c$ is the speed of light in the medium, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ the vacuum value; $\mathbf{v}$ denotes particle velocities.

## The Two Four-Momenta in the Material Sector

The first body has rest mass $m_1$, velocity $\mathbf{v}_1$, and four-momentum

$$
\tilde{P}_1 = m_1\tilde{U}_1 = i\frac{E_1}{c}\,e_0 + \mathbf{p}_1,
\qquad
E_1 = \gamma_1 m_1 c^2,
\qquad
\mathbf{p}_1 = \gamma_1 m_1 \mathbf{v}_1,
$$

with $\gamma_1 = (1 - \mathbf{v}_1^2/c^2)^{-1/2}$. The second body is described identically with label $2$. Since the scalar part is imaginary and the vector part is real, both $\tilde{P}_1$ and $\tilde{P}_2$ lie in the anti-Hermitian subspace $\mathbb{M}_-$, as required of every four-momentum.

Each four-momentum satisfies the **mass-shell relation**

$$
N(\tilde{P}_a) = \tilde{P}_a\bar{\tilde{P}}_a = -\frac{E_a^2}{c^2} + \mathbf{p}_a^2 = -m_a^2c^2,
\qquad a = 1, 2,
$$

which is the biquaternion form of $E_a^2 = \mathbf{p}_a^2c^2 + m_a^2c^4$. The **unit four-velocities** are

$$
\tilde{u}_a = \frac{\tilde{U}_a}{c} = \gamma_a\left(i\,e_0 + \frac{\mathbf{v}_a}{c}\right),
\qquad
N(\tilde{u}_a) = -1,
$$

which are the elements of $\mathbb{M}_-$ of unit negative norm.

### The Invariant Pairing on $\mathbb{M}_-$

In order to combine the two four-momenta we need the symmetric bilinear form associated with the quadratic form $N$. For $\tilde{A}, \tilde{B} \in \mathbb{M}_-$ define

$$
\langle \tilde{A}, \tilde{B}\rangle := \mathrm{Sc}\!\left(\tilde{A}\bar{\tilde{B}}\right).
$$

For elements of $\mathbb{M}_-$ this is **real**: writing $\tilde{A} = i\alpha\,e_0 + \mathbf{a}$ and $\tilde{B} = i\beta\,e_0 + \mathbf{b}$ with real $\alpha, \beta$ and real $\mathbf{a}, \mathbf{b}$, one has

$$
\langle \tilde{A},\tilde{B}\rangle = (i\alpha)(i\beta) + \mathbf{a}\cdot\mathbf{b} = -\alpha\beta + \mathbf{a}\cdot\mathbf{b}.
$$

The pairing is symmetric, bilinear, and non-degenerate, and it reproduces the norm form on the diagonal:

$$
\langle \tilde{A}, \tilde{A}\rangle = N(\tilde{A}).
$$

Its signature is $(3,1)$ in the basis $\{ie_0, e_1, e_2, e_3\}$: the temporal direction contributes $-1$ and the three spatial directions contribute $+1$. This is the same signature as the norm form of $\mathbb{M}_-$.

For the four-momenta the pairing reads

$$
\langle \tilde{P}_1, \tilde{P}_2\rangle = -\frac{E_1E_2}{c^2} + \mathbf{p}_1\cdot\mathbf{p}_2,
$$

which is the Minkowski inner product of the two four-momenta in the $ict$ convention, with real time components $E_a/c$. In particular, for the unit four-velocities,

$$
\langle \tilde{u}_1, \tilde{u}_2\rangle = -\gamma_1\gamma_2\left(1 - \frac{\mathbf{v}_1\cdot\mathbf{v}_2}{c^2}\right).
$$

The pairing is invariant under rotor conjugation. Indeed $N$ is invariant, and $\langle\cdot,\cdot\rangle$ is the polarization of $N$; since rotor conjugation is linear on $\mathbb{M}_-$, the invariance of the quadratic form implies the invariance of its polarization.

## The Total Four-Momentum and Its Norm

The **total four-momentum** of the pair is the sum

$$
\tilde{P} = \tilde{P}_1 + \tilde{P}_2 = i\frac{E_1+E_2}{c}\,e_0 + (\mathbf{p}_1+\mathbf{p}_2).
$$

Because $\mathbb{M}_-$ is a real vector space, $\tilde{P} \in \mathbb{M}_-$: the total energy is $E_1+E_2$, the total momentum $\mathbf{p}_1+\mathbf{p}_2$. In the biquaternion formulation this is the statement that $\mathbb{M}_-$ is closed under addition.

The norm form is multiplicative on $\mathbb{B}$ but **not additive**. For any $\tilde{A}, \tilde{B} \in \mathbb{B}$,

$$
N(\tilde{A}+\tilde{B}) = (\tilde{A}+\tilde{B})(\bar{\tilde{A}}+\bar{\tilde{B}})
= N(\tilde{A}) + N(\tilde{B}) + \tilde{A}\bar{\tilde{B}} + \tilde{B}\bar{\tilde{A}}.
$$

Since $\tilde{B}\bar{\tilde{A}} = \overline{\tilde{A}\bar{\tilde{B}}}$ and a biquaternion plus its quaternion conjugate is twice its scalar part, the last two terms combine into $2\,\mathrm{Sc}(\tilde{A}\bar{\tilde{B}})$. For elements of $\mathbb{M}_-$ this gives the **polarization identity**

$$
N(\tilde{A}+\tilde{B}) = N(\tilde{A}) + N(\tilde{B}) + 2\langle \tilde{A}, \tilde{B}\rangle.
$$

The mixed term is the whole content of the two-body problem: it is the invariant that knows about the relative motion.

### The Invariant Mass of the Pair

The **invariant mass** $M$ of the pair is defined, exactly as for a single body, by the norm form of the total four-momentum:

$$
N(\tilde{P}) = \tilde{P}\bar{\tilde{P}} = -M^2c^2, \qquad M \ge 0.
$$

Using the polarization identity and the mass-shell relation $N(\tilde{P}_a) = -m_a^2c^2$, this is

$$
-M^2c^2 = -m_1^2c^2 - m_2^2c^2 + 2\langle \tilde{P}_1, \tilde{P}_2\rangle,
$$

or, equivalently,

$$
M^2c^2 = m_1^2c^2 + m_2^2c^2 - 2\langle \tilde{P}_1, \tilde{P}_2\rangle.
$$

In components, expanding the total four-momentum directly,

$$
M^2c^4 = (E_1+E_2)^2 - (\mathbf{p}_1+\mathbf{p}_2)^2c^2,
$$

which is the standard invariant mass of a two-body system. The name "invariant" is the statement that $N(\tilde{P})$ is unchanged by rotor conjugation; $Mc^2$ is also called the **centre-of-momentum energy** of the pair.

Two structural facts follow. First, the total four-momentum of two future-directed timelike four-momenta is again future-directed timelike; the future cone is convex. Second, the invariant mass of the pair is bounded below by the sum of the rest masses,

$$
M \ge m_1 + m_2,
$$

with equality if and only if $\mathbf{v}_1 = \mathbf{v}_2$. Both follow below from $\cosh\psi_{\rm rel}\ge1$.

## Conservation in the Biquaternion Formulation

For a system of two bodies that interact only with each other, the total four-momentum is conserved. In the biquaternion formulation the conservation law is a single equation for an element of $\mathbb{M}_-$:

$$
\tilde{P}_1 + \tilde{P}_2 = \text{constant}
\qquad\Longleftrightarrow\qquad
\frac{d}{dt}\left(\tilde{P}_1 + \tilde{P}_2\right) = 0,
$$

where $t$ is the time coordinate of a fixed inertial frame. Introducing the coordinate-time four-forces $\tilde{F}_a = d\tilde{P}_a/dt$, this reads

$$
\tilde{F}_1 + \tilde{F}_2 = 0.
$$

Because the decomposition into scalar (time) and vector (space) parts is by real-linear projections, the single biquaternion equation is equivalent to the separate conservation of total energy and total three-momentum in the chosen frame:

$$
\frac{d}{dt}(E_1+E_2) = 0,
\qquad
\frac{d}{dt}(\mathbf{p}_1+\mathbf{p}_2) = 0.
$$

Two comments are in order. First, the conservation law is **Lorentz covariant**: if $\tilde{P}_1 + \tilde{P}_2$ is constant in one inertial frame, then applying the same rotor conjugation to both sides, $\tilde{\Lambda}\tilde{P}_1\tilde{\Lambda}^\dagger + \tilde{\Lambda}\tilde{P}_2\tilde{\Lambda}^\dagger = \tilde{\Lambda}(\tilde{P}_1+\tilde{P}_2)\tilde{\Lambda}^\dagger$, shows that it is constant in every inertial frame. The statement of conservation is a statement about an element of $\mathbb{M}_-$, and the element transforms as a whole. Second, the four-forces above are differentiated with respect to a **common** coordinate time. Differentiating instead with respect to each body's proper time introduces the factors $\gamma_a$, since $d\tau_a = dt/\gamma_a$; the common coordinate time is the natural choice for a two-body conservation law.

When the two bodies are not isolated but are subject to external four-forces, the individual four-momenta change and the sum is no longer conserved. The external-field case is the subject of the companion article on the relativistic particle in an external field; here the sum is conserved and is the natural constant of the motion.

## The Centre-of-Momentum Frame

The **centre-of-momentum (COM) frame** is an inertial frame in which the total three-momentum vanishes:

$$
\mathbf{p}_1^* + \mathbf{p}_2^* = 0.
$$

Asterisks denote quantities in this frame. In the biquaternion formulation the condition is that the vector part of the total four-momentum vanishes, so that $\tilde{P}$ is a pure imaginary scalar:

$$
\tilde{P}^* = \tilde{\Lambda}_{\rm CM}\,\tilde{P}\,\tilde{\Lambda}_{\rm CM}^\dagger = iMc\,e_0.
$$

The sign is fixed by the physical branch $E^* = Mc^2 > 0$, possible because a future-timelike four-vector can always be rotated to the time axis by a boost. Writing $\tilde{u}_P = \tilde{P}/(Mc)$ for the unit four-velocity of the pair, the companion article's relation $\tilde{\Lambda} = \sqrt{-i\bar{\tilde{u}}}$ gives

$$
\tilde{\Lambda}_{\rm CM} = \sqrt{-\frac{i}{Mc}\,\bar{\tilde{P}}},
\qquad
\tilde{\Lambda}_{\rm CM}\bar{\tilde{\Lambda}}_{\rm CM} = e_0.
$$

Its rapidity $\Psi$ satisfies $\cosh\Psi = E_{\rm tot}/(Mc^2)$ and $\sinh\Psi\,\hat{\mathbf{u}} = \mathbf{P}_{\rm tot}/(Mc)$, so its velocity is $\mathbf{V}_{\rm CM} = \mathbf{P}_{\rm tot}c^2/E_{\rm tot}$; the branch with $\mathrm{Sc}(\tilde{\Lambda}_{\rm CM}) > 0$ is the physical one. The frame is unique up to spatial rotations, which leave $\tilde{P}^* = iMc\,e_0$ unchanged.

### Constituent Energies and Momentum

In the COM frame the two four-momenta are

$$
\tilde{P}_1^* = i\frac{E_1^*}{c}\,e_0 + \mathbf{p}^*,
\qquad
\tilde{P}_2^* = i\frac{E_2^*}{c}\,e_0 - \mathbf{p}^*,
$$

with $\mathbf{p}^* = \mathbf{p}_1^* = -\mathbf{p}_2^*$. Summing and comparing with $\tilde{P}^* = iMc\,e_0$ gives

$$
E_1^* + E_2^* = Mc^2.
$$

The mass-shell relations give

$$
E_1^{*2} = m_1^2c^4 + p^{*2}c^2,
\qquad
E_2^{*2} = m_2^2c^4 + p^{*2}c^2,
$$

where $p^{*2} = \mathbf{p}^*\cdot\mathbf{p}^*$. Subtracting the two shell relations eliminates $p^*$ and yields $E_1^{*2} - E_2^{*2} = (m_1^2-m_2^2)c^4 = (E_1^*-E_2^*)(E_1^*+E_2^*)$, so that $E_1^*-E_2^* = (m_1^2-m_2^2)c^2/M$. Combining this with $E_1^*+E_2^* = Mc^2$ gives the explicit energies

$$
E_1^* = \frac{\left(M^2 + m_1^2 - m_2^2\right)c^2}{2M},
\qquad
E_2^* = \frac{\left(M^2 + m_2^2 - m_1^2\right)c^2}{2M}.
$$

Substituting $E_1^*$ into the mass shell then gives the COM momentum magnitude

$$
p^* = \frac{c}{2M}\sqrt{\left[M^2 - (m_1+m_2)^2\right]\left[M^2 - (m_1-m_2)^2\right]}.
$$

The radicand is non-negative when $M \ge m_1+m_2$: a pair with relative motion has at least the rest energy of its constituents. At $M = m_1+m_2$ the momentum vanishes and the two bodies are at relative rest. The speeds are $v_a^* = p^*c^2/E_a^*$, so $\tanh\psi_a^* = p^*c/E_a^*$ for the individual COM rapidities.

## The Relative Four-Velocity and the Relative Rapidity

The COM frame exhibits the two bodies moving in opposite directions, but the invariant that governs the pair is the relative motion. The **relative four-velocity** is the four-velocity of body 2 as seen in the rest frame of body 1. It is obtained by rotor conjugation with the boost biquaternion $\tilde{\Lambda}_1 = \sqrt{-i\bar{\tilde{u}}_1}$ that carries body 1 to rest:

$$
\tilde{u}_{2|1} = \tilde{\Lambda}_1\,\tilde{u}_2\,\tilde{\Lambda}_1^\dagger
= i\gamma_{\rm rel}\,e_0 + \gamma_{\rm rel}\,\frac{\mathbf{v}_{\rm rel}}{c},
$$

where $\mathbf{v}_{\rm rel}$ is the velocity of body 2 in the rest frame of body 1 and

$$
\gamma_{\rm rel} = \frac{1}{\sqrt{1 - v_{\rm rel}^2/c^2}}
$$

is the corresponding Lorentz factor. The four-vector lies in $\mathbb{M}_-$ with $N(\tilde{u}_{2|1}) = -1$, hence is timelike.

Because the pairing is invariant under rotor conjugation, the relative Lorentz factor can be read off directly from the two four-velocities without performing the boost:

$$
\gamma_{\rm rel} = -\langle \tilde{u}_1, \tilde{u}_2\rangle
= \gamma_1\gamma_2\left(1 - \frac{\mathbf{v}_1\cdot\mathbf{v}_2}{c^2}\right).
$$

This quantity is $\ge 1$, since it is a Lorentz factor, and it equals $1$ exactly when $\mathbf{v}_1 = \mathbf{v}_2$. Introducing the **relative rapidity** $\psi_{\rm rel}$ by $\cosh\psi_{\rm rel} = \gamma_{\rm rel}$, the relative speed is $v_{\rm rel} = c\tanh\psi_{\rm rel}$. In terms of the two velocities in an arbitrary frame,

$$
v_{\rm rel} = \frac{\sqrt{\left|\mathbf{v}_1-\mathbf{v}_2\right|^2 - \frac{1}{c^2}\left|\mathbf{v}_1\times\mathbf{v}_2\right|^2}}{1 - \mathbf{v}_1\cdot\mathbf{v}_2/c^2},
$$

which reduces to the Galilean $|\mathbf{v}_2-\mathbf{v}_1|$ when both speeds are small compared with $c$. The rapidities compose additively along the common axis of relative motion:

$$
\psi_{\rm rel} = \psi_1^* + \psi_2^*,
\qquad
\tanh\psi_a^* = \frac{p^*c}{E_a^*},
$$

with the two bodies moving in opposite directions in the COM frame. This is the relativistic velocity-composition law: the relative rapidity is the sum of the two COM rapidities.

## The Invariant Mass of the Pair

Combining the mass-shell relations with the polarization identity gives the invariant mass of the pair in terms of the individual masses and the relative motion:

$$
M^2c^4 = m_1^2c^4 + m_2^2c^4 + 2m_1m_2c^4\cosh\psi_{\rm rel}.
$$

This is the central relation of the two-body kinematics. It exhibits the three contributions to the pair's rest energy: the two rest energies and the relative kinetic energy, the latter encoded in $\cosh\psi_{\rm rel}$. Since $\cosh\psi_{\rm rel} \ge 1$, it immediately gives the subadditivity bound

$$
M^2c^4 \ge \left(m_1^2 + m_2^2 + 2m_1m_2\right)c^4 = (m_1+m_2)^2c^4,
$$

hence $M \ge m_1+m_2$, with equality if and only if the relative rapidity vanishes, that is, if and only if the two bodies are at relative rest. The pair's mass is thus the invariant that measures the energy locked in the relative motion.

Two special cases are worth recording. First, if the two bodies are at relative rest, $\psi_{\rm rel} = 0$ and $M = m_1+m_2$: the masses add. Second, if body 2 is at rest in the chosen frame (a fixed-target configuration, with $\mathbf{v}_2 = 0$ and $\mathbf{v}_1 = \mathbf{v}$), then $\gamma_{\rm rel} = \gamma_1$ and

$$
M^2c^4 = m_1^2c^4 + m_2^2c^4 + 2m_2E_1c^2,
$$

where $E_1 = \gamma_1 m_1c^2$ is the energy of the incident body. This is the standard fixed-target invariant mass, expressed through the pairing as $\langle \tilde{P}_1, \tilde{P}_2\rangle = -E_1m_2c^2$. Both follow from the same norm-form identity.

## Two-Body Kinematics: The Decay Configuration

The two-body decay is the special case of the preceding kinematics in which the total four-momentum is that of a single body at rest. Let a body of mass $M$ decay into two bodies of masses $m_1$ and $m_2$:

$$
A \;\longrightarrow\; 1 + 2,
\qquad
\tilde{P}_A = \tilde{P}_1 + \tilde{P}_2.
$$

In the rest frame of $A$ the parent four-momentum is $\tilde{P}_A = iMc\,e_0$, so the rest frame of the parent **is** the COM frame of the two daughters, and the results above apply unchanged. The conservation law is the biquaternion equation $\tilde{P}_A = \tilde{P}_1+\tilde{P}_2$; its scalar and vector parts are energy and three-momentum conservation, and its norm form is $N(\tilde{P}_A) = -M^2c^2 = N(\tilde{P}_1+\tilde{P}_2)$.

The daughter quantities in the parent rest frame are therefore

$$
E_1^* = \frac{\left(M^2 + m_1^2 - m_2^2\right)c^2}{2M},
\qquad
E_2^* = \frac{\left(M^2 + m_2^2 - m_1^2\right)c^2}{2M},
$$

$$
\mathbf{p}_1^* = -\mathbf{p}_2^* = \mathbf{p}^*,
\qquad
p^* = \frac{c}{2M}\sqrt{\left[M^2 - (m_1+m_2)^2\right]\left[M^2 - (m_1-m_2)^2\right]},
$$

with speeds $v_a^* = p^*c^2/E_a^*$. The decay is kinematically allowed if and only if $M \ge m_1+m_2$; at $M = m_1+m_2$ the daughters emerge at rest (threshold), and for $M > m_1+m_2$ they emerge back to back with equal and opposite momenta. The **released energy** is

$$
Q = (M - m_1 - m_2)c^2 = \left(E_1^* - m_1c^2\right) + \left(E_2^* - m_2c^2\right),
$$

which is the total kinetic energy of the daughters in the parent rest frame, split in the ratio $(E_1^*-m_1c^2)/(E_2^*-m_2c^2) = m_2/m_1$ in the non-relativistic limit derived below.

If the parent is moving in the laboratory frame with velocity $\mathbf{V}$, the daughter four-momenta are obtained from their rest-frame values by the rotor conjugation $\tilde{P}_a = \tilde{\Lambda}\tilde{P}_a^*\tilde{\Lambda}^\dagger$, where $\tilde{\Lambda}$ is the **inverse** of the rotor that carries the laboratory frame to the parent rest frame — the quaternion conjugate of $\tilde{\Lambda}_{\rm CM}$ of the preceding section:

$$
\tilde{\Lambda} = \bar{\tilde{\Lambda}}_{\rm CM} = \cosh\frac{\Psi}{2} - i\sinh\frac{\Psi}{2}\,\hat{\mathbf{V}},
\qquad
\tanh\Psi = \frac{V}{c},
$$

the sign of the vector part being opposite to that of the lab-to-rest rotor. The direction resides in that sign alone, and cannot be reversed by transposing the conjugation: a pure boost rotor is Hermitian, $\tilde{\Lambda}^\dagger = \tilde{\Lambda}$, so $\tilde{\Lambda}\tilde{P}_a^*\tilde{\Lambda}^\dagger$ and $\tilde{\Lambda}^\dagger\tilde{P}_a^*\tilde{\Lambda}$ are the same expression. Note also that the quaternion conjugate is *not* the Hermitian conjugate here, since $\bar{\tilde{\Lambda}}_{\rm CM} \neq \tilde{\Lambda}_{\rm CM}^\dagger$ for a pure boost.

In components this is the standard Lorentz transformation of a four-momentum,

$$
E_a = \gamma\left(E_a^* + \mathbf{V}\cdot\mathbf{p}_a^*\right),
\qquad
\mathbf{p}_a = \mathbf{p}_a^* + \frac{\gamma-1}{V^2}\left(\mathbf{V}\cdot\mathbf{p}_a^*\right)\mathbf{V} + \gamma\frac{E_a^*}{c^2}\mathbf{V},
$$

with $\gamma = \cosh\Psi$. Writing $\cos\theta_a^*$ for the angle between $\mathbf{V}$ and $\mathbf{p}_a^*$, the lab energy takes the compact form

$$
E_a = \gamma E_a^*\left(1 + \frac{Vv_a^*}{c^2}\cos\theta_a^*\right),
$$

so that for a given daughter the lab energy ranges from $\gamma E_a^*(1 - Vv_a^*/c^2)$ (emitted backward) to $\gamma E_a^*(1 + Vv_a^*/c^2)$ (emitted forward). These translate a decay computed in the parent rest frame into the laboratory frame.

## Reduction to the Effective One-Body Problem

The invariance of $M$ suggests a reduction of the two-body kinematics to a one-body problem. The reduction that is exact and convention-free is kinematic. In the COM frame the pair is described by the single relative momentum $\mathbf{p}^*$, and the individual momenta are fixed by $\mathbf{p}_1^* = -\mathbf{p}_2^* = \mathbf{p}^*$ together with the mass-shell constraints. The pair's invariant mass is then the energy of that single relative degree of freedom:

$$
Mc^2 = E_1^* + E_2^*
= \sqrt{m_1^2c^4 + p^{*2}c^2} + \sqrt{m_2^2c^4 + p^{*2}c^2}.
$$

This is an exact one-body dispersion relation for the relative motion, and it can be inverted for the relative momentum:

$$
p^{*2} = \frac{\left[M^2 - (m_1+m_2)^2\right]\left[M^2 - (m_1-m_2)^2\right]c^2}{4M^2}.
$$

The single degree of freedom $\mathbf{p}^*$, with the dispersion relation above, is the kinematic content of "the two-body problem reduces to an effective one-body problem". The total (COM) motion is free, since $\tilde{P}$ is conserved; only the relative motion carries dynamical information.

In the non-relativistic limit the dispersion relation becomes that of a particle of the **reduced mass**

$$
\mu = \frac{m_1m_2}{m_1+m_2},
$$

since expanding the two square roots gives

$$
Mc^2 = (m_1+m_2)c^2 + \frac{p^{*2}}{2\mu} + O\!\left(p^{*4}\right).
$$

Thus the leading non-relativistic reduction is the familiar one: a fictitious body of mass $\mu$ carrying the relative momentum $\mathbf{p}^*$ and the relative kinetic energy. The exact dynamical reduction of two **interacting** relativistic bodies to a single one-body equation is more delicate: the interaction must be specified together with a synchronisation convention between the two worldlines, and different conventions give inequivalent effective equations. The kinematic reduction above is independent of such choices and is all that is required for the decay kinematics.

## The Non-Relativistic Limit

The non-relativistic limit provides an independent consistency check against the known Newtonian two-body results. Let $\mathbf{v}_1, \mathbf{v}_2$ be small compared with $c$.

**Invariant mass.** Expanding $\cosh\psi_{\rm rel} = 1 + \psi_{\rm rel}^2/2 + O(\psi_{\rm rel}^4)$ with $\psi_{\rm rel} \approx v_{\rm rel}/c$,

$$
M^2c^4 = (m_1+m_2)^2c^4 + m_1m_2c^4\,\psi_{\rm rel}^2 + O\!\left(v_{\rm rel}^4\right),
$$

and taking the square root,

$$
Mc^2 = (m_1+m_2)c^2 + \frac{1}{2}\mu v_{\rm rel}^2 + O\!\left(v_{\rm rel}^4/c^2\right).
$$

The invariant mass is the rest energy plus the relative kinetic energy computed with the reduced mass — exactly the Newtonian energy of the relative motion.

**COM frame.** The COM boost velocity is $\mathbf{V}_{\rm CM} = \mathbf{P}_{\rm tot}c^2/E_{\rm tot}$. Expanding with $\mathbf{p}_a \approx m_a\mathbf{v}_a$ and $E_{\rm tot} \approx (m_1+m_2)c^2$,

$$
\mathbf{V}_{\rm CM} \approx \frac{m_1\mathbf{v}_1 + m_2\mathbf{v}_2}{m_1+m_2},
$$

the Newtonian centre-of-mass velocity. In this frame the individual velocities are $\mathbf{v}_1^* \approx -m_2\mathbf{v}_{\rm rel}/(m_1+m_2)$ and $\mathbf{v}_2^* \approx m_1\mathbf{v}_{\rm rel}/(m_1+m_2)$, and the total kinetic energy $\tfrac12m_1v_1^{*2} + \tfrac12m_2v_2^{*2} = \tfrac12\mu v_{\rm rel}^2$ is the relative kinetic energy with the reduced mass.

**Momentum and energies.** The COM momentum is $p^* \approx \mu v_{\rm rel}$, and the individual kinetic energies are

$$
E_1^* - m_1c^2 \approx \frac{m_2}{m_1+m_2}\cdot\frac{1}{2}\mu v_{\rm rel}^2,
\qquad
E_2^* - m_2c^2 \approx \frac{m_1}{m_1+m_2}\cdot\frac{1}{2}\mu v_{\rm rel}^2,
$$

which sum to the total relative kinetic energy.

**Decay.** For a decay with $M = m_1+m_2+Q/c^2$ and $Q \ll (m_1+m_2)c^2$, the non-relativistic partition of the released energy is

$$
E_1^* - m_1c^2 \approx \frac{m_2}{m_1+m_2}\,Q,
\qquad
E_2^* - m_2c^2 \approx \frac{m_1}{m_1+m_2}\,Q,
$$

the light daughter carrying the larger share. The conservation law $\tilde{P}_A = \tilde{P}_1+\tilde{P}_2$ likewise reduces to the separate Galilean conservation of mass plus kinetic energy, and of three-momentum. Every Newtonian two-body result is recovered.

## Summary

The relativistic two-body problem in the biquaternion framework is expressed entirely through the three operations of the algebra restricted to the material sector $\mathbb{M}_-$: addition, the norm form, and the rotor conjugation. The two four-momenta $\tilde{P}_1, \tilde{P}_2$ are elements of $\mathbb{M}_-$; their sum $\tilde{P} = \tilde{P}_1+\tilde{P}_2$ is again in $\mathbb{M}_-$, with norm $N(\tilde{P}) = -M^2c^2$, which defines the invariant mass $M$ of the pair. Conservation of four-momentum is the single equation $\tilde{P}_1+\tilde{P}_2 = \text{constant}$, whose scalar and vector parts are energy and momentum conservation.

The centre-of-momentum frame is reached by the boost biquaternion $\tilde{\Lambda}_{\rm CM} = \sqrt{-i\bar{\tilde{P}}/(Mc)}$, which rotates the total four-momentum to $iMc\,e_0$; in that frame the pair has back-to-back momenta and energies $E_1^*$ and $E_2^*$ fixed by the masses. The relative motion is characterised by the relative rapidity $\psi_{\rm rel}$, defined by $\cosh\psi_{\rm rel} = -\langle\tilde{u}_1,\tilde{u}_2\rangle$; the invariant mass satisfies $M^2c^4 = m_1^2c^4+m_2^2c^4+2m_1m_2c^4\cosh\psi_{\rm rel}$. The kinematic reduction to an effective one-body problem is the exact dispersion relation $Mc^2 = \sqrt{m_1^2c^4+p^{*2}c^2}+\sqrt{m_2^2c^4+p^{*2}c^2}$, whose non-relativistic limit is the reduced-mass kinetic energy.

A two-body decay is the special case in which the total four-momentum is $\tilde{P}_A = iMc\,e_0$; the general results then give the daughter energies, the common momentum magnitude $p^*$, the threshold condition $M \ge m_1+m_2$, and the boost to the laboratory frame. The non-relativistic limit reproduces the Newtonian centre-of-mass motion, the reduced mass, and the partition of the released energy, confirming that the framework reduces correctly to the established theory.

## Open Questions

1. **Many-body systems.** The total four-momentum of $n$ bodies is again in $\mathbb{M}_-$, and the norm-form construction defines an $n$-body invariant mass. Whether the COM reduction extends usefully beyond $n=2$ is not developed here.

2. **Massless constituents and null totals.** If the total four-momentum is null — massless constituents, or collinear momenta — no COM frame exists in the sense used here and $\tilde{\Lambda}_{\rm CM}$ is undefined; such degenerate pairs (for instance two collinear photons) need separate treatment.

3. **The relativistic dynamical reduction.** The reduction of two interacting relativistic bodies to a single one-body equation depends on the synchronisation convention and quasipotential, and different choices are inequivalent. This article deliberately does not select a convention.

4. **The role of the informational sector.** The account above uses only $\mathbb{M}_-$ and the rotor conjugation. What role the Hermitian sector $\mathbb{M}_+$ plays for a two-body system — for instance through constituent spin — is open.

5. **Bound states.** A bound pair has a discrete spectrum of invariant masses below the threshold $m_1+m_2$, unreachable by the free-particle kinematics above; its relation to the biquaternion hydrogen-atom articles is open.

6. **Interactions and the medium.** In a medium the local speed of light varies, and with it the pair's invariant mass. The consequences of the local complex structure for two-body kinematics are not worked out.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector): imaginary scalar, real vector |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector) |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\langle\tilde{A},\tilde{B}\rangle = \mathrm{Sc}(\tilde{A}\bar{\tilde{B}})$ | Invariant pairing on $\mathbb{M}_-$ |
| $\tilde{P}_a = m_a\tilde{U}_a = iE_a/c\,e_0+\mathbf{p}_a$ | Four-momentum of body $a$ |
| $\tilde{u}_a = \tilde{U}_a/c$ | Unit four-velocity, $N(\tilde{u}_a) = -1$ |
| $\tilde{P} = \tilde{P}_1+\tilde{P}_2$ | Total four-momentum |
| $N(\tilde{P}) = -M^2c^2$ | Invariant mass of the pair |
| $\tilde{u}_{2|1}$ | Relative four-velocity (body 2 in the rest frame of body 1) |
| $\gamma_{\rm rel} = \cosh\psi_{\rm rel} = -\langle\tilde{u}_1,\tilde{u}_2\rangle$ | Relative Lorentz factor |
| $\psi_{\rm rel}$ | Relative rapidity, $v_{\rm rel} = c\tanh\psi_{\rm rel}$ |
| $\tilde{\Lambda}_{\rm CM} = \sqrt{-i\bar{\tilde{P}}/(Mc)}$ | Boost biquaternion to the centre-of-momentum frame |
| $E_a^*,$ $\mathbf{p}_a^*$ | Energy and momentum in the centre-of-momentum frame |
| $p^*$ | Common momentum magnitude, $\mathbf{p}_1^* = -\mathbf{p}_2^* = \mathbf{p}^*$ |
| $\mu = m_1m_2/(m_1+m_2)$ | Non-relativistic reduced mass |
| $Q = (M-m_1-m_2)c^2$ | Released energy of a two-body decay |

## Further Reading

- Albert Einstein, "Zur Elektrodynamik bewegter Körper," *Annalen der Physik* **17** (1905) 891–921, for the original special relativity.
- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the four-dimensional formulation.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the standard relativistic two-body kinematics and the invariant mass.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the fixed-target invariant mass and the Lorentz transformation of four-momenta.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra treatment of relativistic rotors and multiparticle kinematics.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original spacetime-algebra formulation of relativistic mechanics.
- P. A. M. Dirac, "Forms of relativistic dynamics," *Reviews of Modern Physics* **21** (1949) 392–399, for the problem of defining a relativistic dynamics of several interacting bodies.
