# __The Relativistic Exchange of Information and Clock Synchronisation in Biquaternionic Form__

## Introduction

The companion article *Causality and the Light Cone as an Information Barrier in Biquaternionic Form* establishes what the causal structure of the material sector forbids. No admissible signal crosses a spacelike separation; the light cone is the invariant boundary between the events that can influence one another and those that cannot; the relative speed of two observers is strictly below $c$; and the cone is the characteristic cone of the algebra's wave operator. This article treats what is nevertheless possible within that barrier. One event can send a signal to another precisely when their displacement is null, and the round trip of a light signal is the operation by which observers who never share a clock establish a common time. The subject is therefore the relativistic exchange of information and the synchronisation of clocks, read in the biquaternion algebra.

The two themes are one. A signal is a null displacement, and a null displacement is a zero divisor of $\mathbb{B}$; the algebra's degenerate locus, which is the barrier of the companion article, is also the channel through which every exchange passes. A clock is an integral of the biquaternion norm along a worldline, and clocks in relative motion read different totals for the same pair of events; the radar procedure that repairs this is a definition of simultaneity built out of the very null displacements the algebra singles out. The companion article *The Light Cone as the Biquaternion Zero-Divisor Cone* gives the null cone as the material-sector part of the zero-divisor set; the present article uses that identification at every step and does not re-derive it.

The article develops the following.

- **Signals are null displacements.** Two events are joined by a light signal exactly when their displacement is a zero divisor. Writing the signal direction as $\vec u_{\mathrm s}$, the null condition is $\Delta(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \pm c\,\Delta t'\,\vec u_{\mathrm s}$, and the retarded and advanced combinations $t'_{\mathrm{ret}} = t' - \vec u_{\mathrm s}\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)/c$, $t'_{\mathrm{adv}} = t' + \vec u_{\mathrm s}\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)/c$ are constant along the outgoing and incoming rays.
- **Clocks read proper time.** The proper time of a worldline is the integral of $\sqrt{-\langle d\tilde{R}\rangle_{\natural}}/c$, and the clock four-velocity is $\tilde{V} = d\tilde{R}/d\tau$ with $\langle\tilde{V}\rangle_{\natural} = -c^2$.
- **Einstein synchronisation is the round trip.** The reflection event is assigned the mid-time, $t'_2 = (t'_1+t'_3)/2$, and the distance is $L = c(t'_3-t'_1)/2$. The assignment fixes the one-way speed of light by convention; only the round-trip speed is directly measured.
- **The exchange of frequency is the k-factor.** The ratio of received to emitted intervals between two relatively moving observers is Bondi's $k = \sqrt{(1+\beta)/(1-\beta)}$, the reciprocal of the longitudinal Doppler factor of the companion article *Exercise: The Relativistic Doppler Effect*, and $k$-factors multiply under composition.
- **Simultaneity is frame-dependent.** Under a boost the scalar component of a displacement transforms so that a set of clocks synchronised in one frame is desynchronised in another by $\Delta t' = \gamma v_b\,\Delta x_2/c^2$.
- **A transported clock runs slow.** The interpretation of a clock carried along a worldline is the proper time of that worldline, $\Delta\tau = \int\sqrt{1-\vec v^2/c^2}\,dt' \le t'_B-t'_A$, so a clock carried away and back reads less than one that stayed, and the inertial worldline between two events maximizes the proper time.
- **Synchronisation is not transitive on a rotating platform.** The Sagnac effect makes the round trip directional, $\Delta t' \simeq 4\vec\Omega\cdot\vec A/c^2$, so synchronising around a closed loop in the two directions gives two different results.

The exchange discussed here is the classical exchange of signals. It is not the operator-theoretic content of the Hermitian sector $\mathbb{M}_+$ treated in the companion article *The Informational Sector: States, Observables and Probability*; the two share the algebra, and the information in question is carried by null displacements of $\mathbb{M}_-$.

**Conventions.** The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_\mu^2 = -e_t$, and central scalar imaginary $i$ with $i^2 = -1$. The material sector $\mathbb{M}_-$ is the anti-Hermitian subspace, with elements $i\alpha\,e_t+\vec a$ of imaginary scalar part and real vector part. The biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$, the material coordinate is $\tilde{R} = ic\,t'\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, and the $ict'$-coordinate metric is $\eta = \mathrm{diag}(-1,+1,+1,+1)$. The biquaternionic gradient is $\tilde{\nabla} = e_t\partial/\partial Q_t+\nabla$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value. Numerical statements were checked in the four-component coefficient representation $\tilde{Q} = Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with complex coefficients, and the frequency exchange was checked on a superposition of two wavevectors.

## Signals as Null Displacements

### The Null Condition Between Two Events

Let an emitter be at the event $A$ with coordinate $\tilde{Q}_A = ic\,t'_A\,e_t + x_A\,\vec e_x+y_A\,\vec e_y+z_A\,\vec e_z$, and a receiver at the event $B$ with $\tilde{Q}_B = ic\,t'_B\,e_t + x_B\,\vec e_x+y_B\,\vec e_y+z_B\,\vec e_z$. The displacement is

$$
\tilde{Q}_{BA} = \tilde{Q}_B - \tilde{Q}_A = ic\,\Delta t'\,e_t + \Delta(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z),
\qquad \Delta t' = t'_B - t'_A, \quad \Delta(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = x_B\,\vec e_x+y_B\,\vec e_y+z_B\,\vec e_z - (x_A\,\vec e_x+y_A\,\vec e_y+z_A\,\vec e_z),
$$

with biquaternion norm $\langle\tilde{Q}_{BA}\rangle_{\natural} = -c^2(\Delta t')^2 + |\Delta(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)|^2$. A light signal travelling from $A$ to $B$ covers the spatial separation at speed $c$, so

$$
|\Delta(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)| = c\,\Delta t',
\qquad
\langle\tilde{Q}_{BA}\rangle_{\natural} = 0 :
$$

**an exchange of information between two events along a light signal is possible exactly when their displacement is null.** Because a null displacement is a zero divisor of $\mathbb{B}$ (companion article *The Light Cone as the Biquaternion Zero-Divisor Cone*), the channel through which signals pass is the algebra's degenerate locus. The barrier of the companion article and the channel of this one are the same set; the cone forbids the spacelike separations and carries the null ones.

Writing the propagation direction as the real unit vector $\vec u_{\mathrm s}$, the null condition becomes the vector equation

$$
\Delta(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \pm c\,\Delta t'\,\vec u_{\mathrm s},
$$

the sign selecting whether the signal travels from $A$ to $B$ along $+\vec u_{\mathrm s}$ or along $-\vec u_{\mathrm s}$. The two directional solutions are the two sheets of the local cone, and the sign is the time orientation: with $\Delta t' > 0$ the displacement is future-directed.

### Retarded and Advanced Coordinates

It is useful to package the two directions into the retarded and advanced coordinates

$$
t'_{\mathrm{ret}} = t' - \frac{\vec u_{\mathrm s}\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)}{c},
\qquad
t'_{\mathrm{adv}} = t' + \frac{\vec u_{\mathrm s}\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)}{c}.
$$

Along an outgoing signal propagating in the $+\vec u_{\mathrm s}$ direction the coordinate $t'_{\mathrm{ret}}$ is constant, and along an incoming signal propagating in the $-\vec u_{\mathrm s}$ direction the coordinate $t'_{\mathrm{adv}}$ is constant. The verification is one line: if $x(t')\,\vec e_x+y(t')\,\vec e_y+z(t')\,\vec e_z = x_0\,\vec e_x+y_0\,\vec e_y+z_0\,\vec e_z + c(t'-t'_0)\vec u_{\mathrm s}$ then

$$
t'_{\mathrm{ret}}(t') = t' - \frac{\vec u_{\mathrm s}\cdot(x_0\,\vec e_x+y_0\,\vec e_y+z_0\,\vec e_z)}{c} - (t'-t'_0) = t'_0 - \frac{\vec u_{\mathrm s}\cdot(x_0\,\vec e_x+y_0\,\vec e_y+z_0\,\vec e_z)}{c},
$$

independent of $t'$, while $t'_{\mathrm{adv}}$ increases at rate $2$; and conversely for the incoming ray.

For a displacement whose spatial part is collinear with $\vec u_{\mathrm s}$ — which is the case for a signal along $\vec u_{\mathrm s}$ — the biquaternion norm factorizes in these coordinates:

$$
\langle\tilde{Q}_{BA}\rangle_{\natural} = -c^2\,\Delta t'_{\mathrm{ret}}\,\Delta t'_{\mathrm{adv}} .
$$

A signal therefore satisfies $\Delta t'_{\mathrm{ret}} = 0$ or $\Delta t'_{\mathrm{adv}} = 0$, and a null plane wave has a phase proportional to one of them. For a wave of four-wavevector $\tilde P = i\omega/c\,e_t + \vec k$ propagating along $\vec u_k$, the phase of the companion article *Exercise: The Relativistic Doppler Effect*,

$$
\Phi = \mathrm{Sc}\!\left(\tilde P\tilde{Q}^{\natural}\right) = \vec k\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) - \omega t' = -\omega\left(t' - \frac{\vec u_k\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)}{c}\right) = -\omega\,t'_{\mathrm{ret}},
$$

is the retarded coordinate multiplied by the frequency. The algebra's phase invariant is thus the statement that an exchange is labelled by a single null coordinate, and it is this coordinate that the signal carries from emitter to receiver.

### Relays and Superpositions

If $A \rightsquigarrow B$ and $B \rightsquigarrow C$ are two light exchanges, the sum $\tilde{Q}_{BA}+\tilde{Q}_{CB}$ is the displacement from $A$ to $C$ by a relay, and by the transitivity result of the companion article it is future-directed nonspacelike. It is strictly timelike unless the two legs are collinear and in the same direction, in which case it is null; a bent light path through $B$ no longer covers its ends at speed $c$, which is why a relay of two signals can carry information from $A$ to $C$ only within the cone. The linearity of the wave operator makes the same point for superpositions: since the transformation $\tilde P \mapsto \tilde U\tilde P\tilde U^{*}$ is linear, a superposition of two wavevectors transforms componentwise, and each component carries its own Doppler factor. A numerical check on a two-component superposition confirms that the transformed superposition is the sum of the transformed components, so the frequency exchange below applies to each monochromatic component of a general signal independently.

## Clocks and Proper Time

### Proper Time from the Biquaternion Norm

A clock is a physical system that measures the interval along its own worldline. If the worldline is $\tilde{R}(\lambda)$, the **proper time** is defined by

$$
c\,d\tau = \sqrt{-\,\langle d\tilde{R}\rangle_{\natural}}
= \sqrt{-\left(ic\,dt'\right)^2 -(dx^2+dy^2+dz^2)}
= \sqrt{c^2\,d{t'}^2 -(dx^2+dy^2+dz^2)},
$$

the positive root being taken because $d\tilde{R}$ is timelike along a physical worldline, so that $\langle d\tilde{R}\rangle_{\natural} < 0$ and $-\langle d\tilde{R}\rangle_{\natural} > 0$. Factoring the coordinate time,

$$
d\tau = \sqrt{1 - \frac{\vec v^2}{c^2}}\;dt' = \frac{dt'}{\gamma},
\qquad
\vec v = \frac{d(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)}{dt'},
\qquad
\gamma = \left(1-\frac{\vec v^2}{c^2}\right)^{-1/2},
$$

which is the standard time-dilation relation. The interpretation of the clock between two events on the worldline is the integral

$$
\Delta\tau = \int_{A}^{B}\frac{\sqrt{-\,\langle d\tilde{R}\rangle_{\natural}}}{c}
= \int_{t'_A}^{t'_B}\sqrt{1-\frac{\vec v(t')^2}{c^2}}\;dt' .
$$

The biquaternion form has one structural advantage over the component form: the integrand is the biquaternion norm of the displacement, so the invariance of $\Delta\tau$ under a change of frame is the invariance of $\langle\cdot\rangle_{\natural}$ under the rotor conjugation, established in the companion articles *The Material Sector: Four-Vectors, Interval and Lorentz Action* and *Relativistic Mechanics in Biquaternionic Form*. No separate transformation law for the clock is needed; the clock is an integral of the algebra's own quadratic form.

### The Clock Four-Velocity

Differentiating the worldline with respect to proper time gives the **four-velocity**

$$
\tilde{V} = \frac{d\tilde{R}}{d\tau}
= \frac{d\tilde{R}}{dt'}\frac{dt'}{d\tau}
= \gamma\left(ic\,e_t + \vec v\right),
$$

an element of $\mathbb{M}_-$ whose biquaternion norm is fixed:

$$
\langle\tilde{V}\rangle_{\natural} = \gamma^2\left((ic)^2 + \vec v^2\right) = \gamma^2\left(-c^2+\vec v^2\right) = -c^2 .
$$

Every clock, whatever its state of motion, carries a four-velocity of the same biquaternion norm $-c^2$. This normalization is the algebraic statement that proper time is the parameter with respect to which the four-velocity is a unit vector of $\mathbb{M}_-$, and it is the object in terms of which the frequency exchange of the next sections is written. A clock at rest has $\tilde{V} = ic\,e_t$; a clock moving with velocity $\vec v$ has the four-velocity above. The two are related by the boost rotor, and the relation between their interpretations is the content of the twins' effect below.

## The Radar Method and Einstein Synchronisation

### The Round Trip

Two clocks at different places cannot be compared directly; they must be compared through signals. The **radar method** is the standard procedure. A signal leaves a clock at $A$ at the time $t'_1$, is reflected by a mirror at $B$, and returns to $A$ at the time $t'_3$. The reflection event at $B$ is at time $t'_2$, and the two legs are null displacements:

$$
\langle\tilde{Q}_B - \tilde{Q}_A\rangle_{\natural} = 0,
\qquad
\langle\tilde Q_{A,2} - \tilde{Q}_B\rangle_{\natural} = 0,
$$

with $\tilde Q_{A,2} = ic\,t'_3\,e_t+x_A\,\vec e_x+y_A\,\vec e_y+z_A\,\vec e_z$ the reception event at the mirror's home position. Since $x_{A,2}\,\vec e_x+y_{A,2}\,\vec e_y+z_{A,2}\,\vec e_z = x_A\,\vec e_x+y_A\,\vec e_y+z_A\,\vec e_z$, the spatial separation is the same on both legs, $|x_B\,\vec e_x+y_B\,\vec e_y+z_B\,\vec e_z-(x_A\,\vec e_x+y_A\,\vec e_y+z_A\,\vec e_z)| = L$, and the null conditions read

$$
c^2(t'_2-t'_1)^2 = L^2,
\qquad
c^2(t'_3-t'_2)^2 = L^2 .
$$

Taking the positive roots and equating the two expressions for $L$ gives $t'_2-t'_1 = t'_3-t'_2$, hence the two results of the radar method:

$$
\boxed{\;t'_2 = \frac{t'_1+t'_3}{2}\;},
\qquad
\boxed{\;L = \frac{c\,(t'_3-t'_1)}{2}\;}.
$$

The distance to the mirror is half the round-trip time multiplied by the speed of light, and the reflection event is assigned the **mid-time** of emission and reception. This assignment is the **Einstein synchronisation** of the clock at $B$ with the clock at $A$. It is the definition of simultaneity at a distance, and it is built entirely from the null displacements that the algebra selects.

### Simultaneity Defined by Exchange

The mid-time rule is a definition of simultaneity at a distance: the reflection event at $B$, at time $t'_2$, is declared simultaneous with the event at $A$ at the mid-time $(t'_1+t'_3)/2$. Its operational content is that the one-way speed of light is set to $c$ in both directions by definition. The Reichenbach parametrisation makes the freedom explicit: the reflection time may be assigned

$$
t'_2 = t'_1 + \varepsilon\,(t'_3-t'_1),
$$

with $\varepsilon \in (0,1)$, and the standard Einstein choice is $\varepsilon = \tfrac12$. Every value of $\varepsilon$ reproduces the same round-trip time $t'_3-t'_1$ and therefore the same measurable two-way speed; only the split between the outgoing and incoming one-way speeds changes. With $\varepsilon = \tfrac12$ the two one-way speeds are equal, $c_+ = c_- = c$; with $\varepsilon \ne \tfrac12$ they are $c_+ = c/[2\varepsilon]$ and $c_- = c/[2(1-\varepsilon)]$, whose harmonic combination is $c$. The round trip is insensitive to $\varepsilon$ because

$$
\frac{L}{c_+} + \frac{L}{c_-} = \frac{2L\varepsilon}{c} + \frac{2L(1-\varepsilon)}{c} = \frac{2L}{c},
$$

independent of $\varepsilon$. The one-way speed of light is therefore conventional, and the convention is fixed by the synchronisation; the two-way speed is not conventional and equals $c$. The information-theoretic interpretation is that an exchange of signals determines only the round-trip data, and a convention is needed to convert those data into a statement about distant simultaneity.

### Two Frames, Two Conventions

A second consequence of defining simultaneity by exchange is that two inertial frames generally adopt incompatible conventions. If frame $S_2$ moves with velocity $\vec v_b$ along $\vec e_x$ relative to $S$, and each frame synchronises its own clocks by the radar rule with $\varepsilon = \tfrac12$, then the hypersurface $t'_2 = \mathrm{const}$ is not a hypersurface $t' = \mathrm{const}$. The discrepancy is computed in the next section from the boost, and it is the relativity of simultaneity. It is not an imperfection of the radar method; it is the statement that the method is frame-relative, and it is why the exchange of information between frames must be described by a Lorentz transformation rather than by a Galilean one.

## The k-Factor and the Exchange of Frequency

### The Doppler Factor as an Exchange Ratio

Consider two observers receding from one another with relative speed $v_b$, and let them exchange light signals only. Observer $A$ emits a pulse at proper time $\tau_A$ and the next at $\tau_A + \Delta\tau_A$; observer $B$ receives them at an interval $\Delta\tau_B$. The ratio

$$
k = \frac{\Delta\tau_B}{\Delta\tau_A}
$$

is Bondi's **k-factor**. It is the complete description of the exchange between two inertial observers in relative motion: from $k$ alone, and the direction of the exchange, both the relative speed and the relative clock rate are recovered. Its value follows from the longitudinal Doppler factor of the companion article *Exercise: The Relativistic Doppler Effect*. A receding observer receives the frequency

$$
\omega_{\mathrm{rec}} = \gamma\,\omega_0\,(1-\beta),
$$

so the received interval is longer by the reciprocal factor,

$$
k = \frac{1}{\gamma(1-\beta)} = \sqrt{\frac{1+\beta}{1-\beta}},
\qquad
\beta = \frac{v_b}{c},
$$

where the last equality uses $\gamma(1-\beta) = \sqrt{(1-\beta)/(1+\beta)}$. An approaching observer ($\theta = \pi$) receives at the reciprocal factor $k^{-1} = \sqrt{(1-\beta)/(1+\beta)}$. The two cases are the two signs of the exchange, and their product is unity, as it must be since reversing the relative velocity interchanges emission and reception.

The k-factor also determines the velocity without any need for a clock at the other end:

$$
\beta = \frac{k^2-1}{k^2+1},
$$

which is the inversion of the relation above. The exchange of a train of pulses therefore measures the relative velocity; no rigid rods and no transported clocks are required.

A round trip is described by two k-factors. If $A$ emits and $B$ reflects, then $A$ receives the echo at an interval $k^2\,\Delta\tau_A$ after emission, because the signal is stretched by $k$ on the outward leg and by a further $k$ on the return leg. This single number, the round-trip factor $k^2$, is what the radar method of the preceding section measures; the square root that would give the one-way factor requires the synchronisation convention.

### Composition of Exchanges

If a signal passes from $A$ to $B$ with factor $k_1$ and then from $B$ to $C$ with factor $k_2$, all three collinear and receding in a common sense, the total factor is the product:

$$
k_{AC} = k_{AB}\,k_{BC} = k_1k_2 .
$$

This is because each leg multiplies the interval by its own factor. The composition law for $k$ is equivalent to the velocity-addition law. Indeed, if $k_i = \sqrt{(1+\beta_i)/(1-\beta_i)}$ and $\beta = (k_1^2k_2^2-1)/(k_1^2k_2^2+1)$, a short rearrangement gives

$$
\beta = \frac{\beta_1+\beta_2}{1+\beta_1\beta_2},
$$

the standard relativistic addition formula; as a check, $k(0.5)k(0.6) = 3.4641016\ldots = k(0.8461538\ldots)$, and $0.8461538\ldots = (0.5+0.6)/(1+0.5\cdot0.6)$ is the composed velocity computed in the companion article *Exercise: Boosting a Four-Velocity and Rapidity Composition*. In rapidities the multiplication of $k$-factors is the addition of rapidities, since $k = \exp(\psi)$; the exchange of signals composes the same abelian group as the boosts. There is no value of $\beta_1,\beta_2$ with $|\beta_i| < 1$ for which the composed speed reaches $1$, which is the exchange form of the barrier of the companion article.

The k-factor is a Lorentz scalar in the following limited sense: it is the ratio of two proper-time intervals and is therefore independent of any coordinate system, though it depends on the pair of observers. It is the invariant content of the exchange, the coordinate-free datum that the two observers can agree on without synchronising their clocks.

## Synchronising a Moving Frame

### The Relativity of Simultaneity

Let frame $S_2$ move with velocity $\vec v_b = v_b\,\vec u_x$ relative to frame $S$, and let each frame synchronise its clocks by the Einstein rule. The transformation from the coordinates of $S_2$ to those of $S$ is the rotor conjugation with the boost biquaternion

$$
\tilde U = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\vec u_x,
\qquad
\tanh\psi = \frac{v_b}{c},
$$

of the companion article *The Lorentz Transformation as a Biquaternionic Rotation*. For a displacement $\tilde{A} = i a\,e_t + \vec A$ of $\mathbb{M}_-$, with $a = c\,\Delta t'$ and $\vec A = \Delta(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$, the scalar component transforms by the component action verified in the companion article *Exercise: Boosting a Four-Velocity and Rapidity Composition*:

$$
a = \gamma\left(a_2 + \beta A_{2,\parallel}\right),
\qquad
A_{2,\parallel} = \vec u_x\cdot\vec A_2,
$$

the inverse of the relations $a_2 = \gamma(a-\beta A_\parallel)$, $A_{2,\parallel} = \gamma(A_\parallel-\beta a)$. The sign is the direction convention of the parent articles: the rotor with vector part $+\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ carries $S$ to the frame moving with $+\vec v_b$, and the inverse relation above carries $S_2$ back to $S$.

Now apply this to two events that are simultaneous in $S_2$ and separated along the boost direction by $\Delta x_2$. Then $a_2 = c\,\Delta t'_2 = 0$ and $A_{2,\parallel} = \Delta x_2$, so

$$
\Delta t' = \frac{\gamma\,\beta\,\Delta x_2}{c} = \frac{\gamma\,v_b\,\Delta x_2}{c^2}.
$$

The two events are not simultaneous in $S$: their time separation is proportional to their spatial separation in $S_2$. A direct rotor computation in the coefficient representation reproduces this value for $\beta = 0.3, 0.6, -0.8$ and both signs of $\Delta x_2$, so the sign convention of the boost is fixed consistently with the Doppler article. In SI units, two clocks one metre apart in a frame moving at $\beta = 0.6$ are desynchronised, as seen from the frame at rest, by $\gamma v_b/c^2 \cdot 1\,\mathrm{m} \approx 2.5\times10^{-9}\,\mathrm{s}$.

### What the Desynchronisation Means

The relation $\Delta t' = \gamma v_b\,\Delta x_2/c^2$ is the quantitative form of the **relativity of simultaneity**. Its content is that the set of events that $S_2$ calls simultaneous — a surface of constant $t'_2$ — is tilted with respect to the surfaces of constant $t'$, by an amount proportional to the separation along the motion. A grid of clocks that $S_2$ has synchronised by the radar method is therefore not a grid of synchronised clocks as judged by $S$, and the two judgements differ by a term that is first order in $v_b/c$ and linear in the separation. This is the reason a boost cannot be a Galilean transformation, and the reason the composition of two non-collinear boosts carries a rotation; the latter belongs to the kinematics of the relativity series and is not developed here.

There is one invariant statement that survives the frame dependence: the round-trip time between two clocks is the same in every frame, and so is the proper time along a given worldline. The relativity of simultaneity is the price of converting these invariants into a global time coordinate, and the conversion is a convention. Once the convention is fixed by the radar rule in each frame, the two frames differ by exactly the desynchronisation computed above.

## Clock Transport and the Twin Effect

### Proper Time Along a Worldline

The radar method synchronises clocks without moving them. The alternative is to synchronise by **transporting** a clock from one place to another, and the transport has a cost: the transported clock reads the proper time of its own worldline, which is generally less than the coordinate time of the frame. From the proper-time integral,

$$
\Delta\tau = \int_{A}^{B}\sqrt{1-\frac{\vec v(t')^2}{c^2}}\;dt'
\;\le\; \int_{A}^{B} dt' = t'_B - t'_A,
$$

because the integrand is at most unity, with equality if and only if the clock is at rest in the frame throughout. A clock carried from $A$ to $B$ and back to $A$ therefore reads less than a clock that stayed at $A$, and the deficit is

$$
t'_B - t'_A - \Delta\tau
= \int\left(1-\sqrt{1-\frac{\vec v^2}{c^2}}\right)dt'
\;\approx\; \int\frac{\vec v^2}{2c^2}\,dt'
$$

for a slow journey. For a clock whose velocity is $v(t') = 0.8c\,\sin(2\pi t'/T)$ over a coordinate interval $T = 10$, which carries the clock away from $A$ and back to $A$ at $t' = T$, a direct quadrature gives $\Delta\tau \approx 8.125496$, against the staying clock's $T = 10$: the travelled clock reads about $1.87$ units less. The two clocks meet again at the same event, so the deficit is a proper-time difference between two worldlines with the same endpoints and needs no synchronisation convention to be interpreted. The biquaternion content of the computation is that $\Delta\tau$ is the integral of the biquaternion norm and is therefore automatically frame-independent; the twin effect is the statement that this invariant depends on the path, and not only on its endpoints.

This is the **twin effect**, and it is a statement about worldlines, not about frames: the two clocks are not symmetric, because only one of them is accelerated in the sense of having a worldline that is not a single inertial straight line. The inertial worldline between two timelike-separated events maximizes the proper time, which is the reverse triangle inequality for the Minkowski biquaternion norm; the elementary return-to-origin case is the inequality displayed above. The general statement is standard, and the companion article *Relativistic Mechanics in Biquaternionic Form* records the proper-time integral from which it follows.

### Transport Versus Radar Synchronisation

The transport procedure gives a synchronisation that depends on the transported clock's history, so it is not by itself a definition of distant simultaneity. In the limit of arbitrarily slow transport the accumulated time dilation vanishes and the transport convention agrees with the Einstein convention; this is the standard **slow clock transport** result. Over a distance $L$ and at transport speed $v$ the transported clock loses an amount of order $vL/c^2$, which tends to zero as $v\to0$, so the two conventions coincide in the limit even though they differ at any finite transport speed. The radar convention is preferred in the relativistic setting not because transport is wrong, but because the radar rule is defined directly in terms of the null exchanges that the algebra supplies, while transport introduces an additional dynamical assumption about the clock's response to acceleration.

## Non-Transitivity: The Sagnac Effect

In an inertial frame the radar method is transitive: if the clock at $B$ is synchronised with the clock at $A$ and the clock at $C$ with that at $B$, then the clock at $C$ is synchronised with that at $A$, because the round-trip times are the same in both directions. On a rotating platform this fails, and the failure is the **Sagnac effect**. It is the sharpest statement of the difference between an exchange of information and a global synchronisation.

Consider light travelling around a circular loop of radius $R$ on a platform that rotates with angular velocity $\Omega$ about the normal to the loop. In the inertial frame the light travels at $c$ in both senses, but the two beams must traverse different path lengths, because the platform moves while they propagate. To first order in $\Omega R/c$ the co-rotating beam takes

$$
t'_+ = \frac{2\pi R}{c - \Omega R},
\qquad
t'_- = \frac{2\pi R}{c + \Omega R}
$$

for the counter-rotating beam, and the difference is

$$
\Delta t' = t'_+ - t'_- = \frac{4\pi R^2\,\Omega}{c^2}\left(1 + O\!\left(\frac{\Omega^2R^2}{c^2}\right)\right)
= \frac{4\,\vec\Omega\cdot\vec A}{c^2},
$$

where $\vec A = \pi R^2\,\vec u_{\mathrm s}$ is the vector area of the loop. For $R = 1\,\mathrm{m}$ and $\Omega = 1\,\mathrm{rad\,s^{-1}}$ direct evaluation gives $\Delta t' \approx 1.398\times10^{-16}\,\mathrm{s}$, corresponding to an optical phase $2\pi c\,\Delta t'/\lambda \approx 0.416\,\mathrm{rad}$ at $\lambda = 632.8\,\mathrm{nm}$; the first-order formula reproduces the exact round-trip difference to better than one part in $10^{7}$, the residual being floating-point cancellation in the difference of the two nearly equal times.

The consequence for clock synchronisation is immediate. Take a ring of clocks around the loop and synchronise each neighbouring pair by the Einstein rule, going once around in one direction; then the closure of the chain disagrees with the initial clock by $\Delta t'$, and synchronising in the opposite direction gives the opposite disagreement. There is no assignment of clock readings that is Einstein-synchronised around both directions at once, so **Einstein synchronisation on a rotating platform is not transitive**. The exchange of information is perfectly well defined for every pair, and the round-trip times are measurable; what fails is the global conversion of the round-trip data into a single-valued time coordinate. On a rotating platform the failure is physical and not merely a convention, because the two directions are physically distinguishable by the interference of the two beams. The effect is the standard Sagnac effect, and its relativistic treatment is cited below.

The moral is the one the whole article has developed. An exchange of information requires only the null displacements, and they are local, directed, and always available inside the cone. A global common time requires in addition that the exchange be integrated into a single-valued coordinate, and that integration is a convention which can succeed globally only when the round-trip data are reciprocal. Inertially they are; on a rotating platform they are not.

The conventions and the results taken over from the relativity series are those of the following companion articles:

- Companion article *Introduction to the Biquaternion Universe*, for the notation, the biquaternion norm and the causal trichotomy.
- Companion article *Conventions in the Biquaternion Universe*, for the algebra and basis, the four conjugations, the real subspaces and the metric (its three levels are ruled on in *The Four Forms and the Four Algebraic Norms*).
- Companion article *The Material Sector: Four-Vectors, Interval and Lorentz Action*, for the material four-vector, the interval and the proper-time parametrization.
- Companion article *The Informational Sector: States, Observables and Probability*, for the Hermitian sector and its distinct informational interpretation.
- Companion article *Causality and the Light Cone as an Information Barrier in Biquaternionic Form*, for the causal order, the relative-velocity bound and the cone as the characteristic cone of the wave operator.
- Companion article *The Light Cone as the Biquaternion Zero-Divisor Cone*, for the zero-divisor criterion and the idempotent form of the null displacements.
- Companion article *The Lorentz Transformation as a Biquaternionic Rotation*, for the boost rotor and the transformation of the scalar component.
- Companion article *Exercise: Boosting a Four-Velocity and Rapidity Composition*, for the component action of the boost and the additive composition of rapidities.
- Companion article *Exercise: The Relativistic Doppler Effect*, for the four-wavevector, the invariant phase and the longitudinal frequency factors.
- Companion article *Relativistic Mechanics in Biquaternionic Form*, for the four-velocity and the proper-time integral.

## Summary

The exchange of information and the synchronisation of clocks are built from the same objects: the null displacements of the material sector and the biquaternion norm along worldlines.

1. **Signals are null displacements.** Two events are joined by a light signal exactly when their displacement is null, $|\Delta(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)| = c\,\Delta t'$, that is, when it is a zero divisor of $\mathbb{B}$. The signal direction satisfies $\Delta(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \pm c\,\Delta t'\,\vec u_{\mathrm s}$, and the retarded coordinate $t'_{\mathrm{ret}} = t'-\vec u_{\mathrm s}\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)/c$ is constant along an outgoing ray. A null plane wave has phase $\Phi = -\omega t'_{\mathrm{ret}}$.

2. **Clocks read proper time.** The proper time is $\Delta\tau = \int\sqrt{-\langle d\tilde{R}\rangle_{\natural}}/c = \int\sqrt{1-\vec v^2/c^2}\,dt'$, and the clock four-velocity is $\tilde{V} = d\tilde{R}/d\tau = \gamma(ic\,e_t+\vec v)$ with $\langle\tilde{V}\rangle_{\natural} = -c^2$.

3. **Einstein synchronisation is the round trip.** For emission at $t'_1$, reflection at $t'_2$, reception at $t'_3$, the null conditions give $t'_2 = (t'_1+t'_3)/2$ and the distance $L = c(t'_3-t'_1)/2$. The split of the round trip into one-way times is fixed by the convention $t'_2 = t'_1+\varepsilon(t'_3-t'_1)$; the round-trip time is independent of $\varepsilon$, and only the two-way speed of light is measured.

4. **The k-factor.** The ratio of received to emitted intervals is $k = 1/[\gamma(1-\beta)] = \sqrt{(1+\beta)/(1-\beta)}$ for a receding pair, with reciprocal $k^{-1}$ for an approaching pair. The velocity is recovered as $\beta = (k^2-1)/(k^2+1)$, a round trip gives the factor $k^2$, and $k$-factors multiply: $k_{AC} = k_{AB}k_{BC}$, which reproduces the relativistic velocity-addition law.

5. **Simultaneity is frame-dependent.** Under a boost the scalar component of a displacement transforms so that two events simultaneous in the moving frame are separated in time in the rest frame by $\Delta t' = \gamma v_b\,\Delta x_2/c^2$. A synchronised grid in one frame is desynchronised in another.

6. **Transport and the twin effect.** A transported clock reads $\Delta\tau = \int\sqrt{1-\vec v^2/c^2}\,dt' \le t'_B-t'_A$, with equality only for a clock at rest. Between two timelike-separated events the inertial worldline maximizes the proper time. Slow transport agrees with Einstein synchronisation in the limit of vanishing transport speed.

7. **Non-transitivity on a rotating platform.** The Sagnac round-trip difference is $\Delta t' = 4\vec\Omega\cdot\vec A/c^2$ to first order, so Einstein synchronisation is not transitive around a closed loop and no single-valued global time exists on the rotating platform, although every individual exchange remains well defined.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector): imaginary scalar, real vector |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector) |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^2=-e_t$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $c$, $c_0$ | Speed of light in the medium, and in vacuum |
| $\tilde{R} = ic\,t'\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | Material four-position |
| $\tilde{Q}_{BA} = \tilde{Q}_B-\tilde{Q}_A$ | Displacement from $A$ to $B$ |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Biquaternion norm |
| $\eta = \mathrm{diag}(-1,+1,+1,+1)$ | $ict'$-coordinate metric |
| $\mathrm{Sc}$ | Scalar projection |
| $\vec u_{\mathrm s}$ | Propagation direction |
| $t'_{\mathrm{ret}} = t'-\vec u_{\mathrm s}\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)/c$, $t'_{\mathrm{adv}} = t'+\vec u_{\mathrm s}\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)/c$ | Retarded and advanced radar coordinates |
| $\tilde P = i\omega/c\,e_t+\vec k$ | Four-wavevector |
| $\Phi = \mathrm{Sc}(\tilde P\tilde{Q}^{\natural}) = -\omega t'_{\mathrm{ret}}$ | Plane-wave phase |
| $\tau$, $\Delta\tau$ | Proper time |
| $\tilde{V} = \gamma(ic\,e_t+\vec v)$, $\langle\tilde{V}\rangle_{\natural}=-c^2$ | Clock four-velocity |
| $\beta = v_b/c$, $\gamma = (1-\beta^2)^{-1/2}$ | Dimensionless speed and Lorentz factor |
| $\tilde U = \cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ | Boost rotor, $\tanh\psi=\beta$ |
| $t'_1,t'_2,t'_3$ | Emission, reflection and reception times of the radar round trip |
| $\varepsilon$ | Reichenbach synchronisation parameter, $t'_2=t'_1+\varepsilon(t'_3-t'_1)$ |
| $k = \sqrt{(1+\beta)/(1-\beta)}$ | Bondi k-factor |
| $\Delta t' = \gamma v_b\,\Delta x_2/c^2$ | Desynchronisation of a moving frame |
| $\vec\Omega$, $\vec A$ | Angular velocity and vector area of a rotating loop |
| $\Delta t' = 4\vec\Omega\cdot\vec A/c^2$ | Sagnac round-trip difference (first order) |

## Further Reading

- Albert Einstein, "Zur Elektrodynamik bewegter Körper," *Annalen der Physik* **17** (1905) 891–921, for the original definition of simultaneity by light signals and the synchronisation procedure.
- Hermann Bondi, *Relativity and Common Sense* (Doubleday, 1964), for the k-calculus and the radar method.
- Hans Reichenbach, *The Philosophy of Space and Time* (Dover, 1958), for the conventionality of the one-way speed of light and the synchronisation parameter.
- Christian Møller, *The Theory of Relativity* (Oxford, 1972), for clock synchronisation, the relativity of simultaneity and the twin effect.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for proper time, clock transport and the maximality of inertial proper time.
- Wolfgang Rindler, *Relativity: Special, General, and Cosmological* (Oxford, 2006), for synchronisation, the k-factor and the twin paradox.
- John D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the Doppler effect and the four-vector treatment of wave propagation.
- H. E. Ives and G. R. Stilwell, "An experimental study of the rate of a moving atomic clock," *Journal of the Optical Society of America* **28** (1938) 215–226, for the transverse second-order shift.
- G. Sagnac, "L'éther lumineux démontré par l'effet du vent relatif d'éther dans un interféromètre en rotation uniforme," *Comptes Rendus de l'Académie des Sciences* **157** (1913) 708–710, for the original observation of the rotational round-trip difference.
- E. J. Post, "Sagnac effect," *Reviews of Modern Physics* **39** (1967) 475–493, for the relativistic treatment of the Sagnac effect and clock synchronisation on a rotating platform.
- G. B. Malykin, "The Sagnac effect: correct and incorrect explanations," *Physics-Uspekhi* **43** (2000) 1229–1252, for the modern understanding of the effect and its relation to synchronisation.
- Domenico Giulini, "Uniqueness of simultaneity," *British Journal for the Philosophy of Science* **52** (2001) 651–670, for the analysis of the synchronisation conventions and their uniqueness assumptions.
