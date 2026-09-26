# __Causality and the Light Cone as an Information Barrier in Biquaternionic Form__

## Introduction

The special theory of relativity does more than relate the measurements of moving observers. It fixes which events can influence which other events, and it does so with a structure that is rigid, local, and independent of the particular interaction. Relative to a given event, spacetime divides into three regions: the events that can be reached from it, the events from which it can be reached, and the events that are causally disconnected from it. The boundary between them is the light cone. The reading of this structure adopted here is information-theoretic. The light cone is the barrier that separates the events a given event can signal, or be signalled by, from those it can neither signal nor be signalled by, and the causal order it defines is the order of possible influence.

The biquaternion framework expresses this structure in the algebra. In the material sector $\mathbb{M}_-$ the interval between two events is the norm form $N$ of their displacement biquaternion, and the light cone is the set on which $N$ vanishes. The companion article *The Light Cone as the Biquaternion Zero-Divisor Cone* establishes that this vanishing set is the material-sector part of the algebra's zero-divisor cone, and that the null directions are the directions in which the biquaternion wave operator propagates without dispersion. That result is taken as given below: the cone is not re-derived. What is developed here is what the cone does, and why it acts as a barrier to information.

The interval $N(\tilde{X}_{qp})$ classifies each pair of events as spacelike, null or timelike, and the null set is the light cone. On that structure the article establishes the following, all of it classical:

- the interval is invariant under the rotor conjugation, so no element of the Lorentz group can move a displacement from one causal class to another, and the invariant strata are the orbits of the restricted group;
- the complement of the cone has exactly three connected components, so a continuous worldline crosses from the future to the past or to the spacelike region only through the cone;
- the causal relation is a partial order, with transitivity proved by the triangle inequality in the algebra;
- the contraction of two future timelike four-velocities bounds the relative Lorentz factor below by unity, so no two observers can have a relative speed at or above $c$;
- the boosts form a one-parameter family with additive rapidity $\psi$ and velocity $\beta=\tanh\psi$, so the barrier at $\beta=1$ lies at infinite rapidity and is not attained by any finite composition;
- a causal bijection of Minkowski space is a Lorentz transformation composed with a translation and a positive dilation, so the cone and its time orientation characterize the relativity group rather than merely being preserved by it.

The cone is also the characteristic cone of the algebra's wave operator. The standard finite-speed-of-propagation theorem for hyperbolic operators then makes the barrier analytic as well as geometric: a signal generated in a compact region cannot reach a point outside the region's causal future, however the signal is shaped. These results are collected as eight numbered items in the Summary below.

The word "information" is used in its physical, signal-theoretic sense: a signal is a physical process passing from one event to another that can carry a message, and the question is which pairs of events can be joined by such a process. This is classical relativistic physics with a causal postulate. It is distinct from the operator-theoretic content of the Hermitian sector $\mathbb{M}_+$ treated in the companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; the two readings share the algebra and nothing else.

**Conventions.** The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$, and the central scalar imaginary $i$ with $i^2 = -1$. The material sector $\mathbb{M}_-$ is the anti-Hermitian subspace, with elements of the form $i\alpha\,e_0 + \mathbf{a}$, $\alpha \in \mathbb{R}$, $\mathbf{a} = a_1e_1+a_2e_2+a_3e_3$ real. The norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$, and the material coordinate is $\tilde{X} = ic\,t\,e_0 + \mathbf{x}$. The $ict$-coordinate metric is $\eta = \mathrm{diag}(-1,+1,+1,+1)$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value. Numerical statements below were checked in the four-component coefficient representation $\tilde{Q} = Q_0e_0+Q_1e_1+Q_2e_2+Q_3e_3$ with complex coefficients, and on generic configurations rather than on a single null direction.

## Events, Displacements and the Causal Order

### The Material Coordinate and the Interval

An event is an element of the material sector,

$$
\tilde{X} = ic\,t\,e_0 + \mathbf{x}, \qquad \mathbf{x} = x\,e_1 + y\,e_2 + z\,e_3,
$$

with $t, x, y, z \in \mathbb{R}$ and $c$ the local speed of light. The scalar part is purely imaginary and the vector part is real, so $\tilde{X} \in \mathbb{M}_-$. The displacement from an event $p$ to an event $q$ is

$$
\tilde{X}_{qp} = \tilde{X}_q - \tilde{X}_p = ic\,\Delta t\,e_0 + \Delta\mathbf{x},
\qquad
\Delta t = t_q - t_p, \quad \Delta\mathbf{x} = \mathbf{x}_q - \mathbf{x}_p,
$$

and its norm form is the invariant interval

$$
N(\tilde{X}_{qp}) = \tilde{X}_{qp}\bar{\tilde{X}}_{qp} = (ic\,\Delta t)^2 + |\Delta\mathbf{x}|^2 = -c^2(\Delta t)^2 + |\Delta\mathbf{x}|^2 .
$$

The minus sign in the time–time term is the algebraic consequence of $i^2 = -1$; it is not an independent postulate of the metric. The time orientation of the displacement is carried by the scalar projection,

$$
\mathrm{Sc}(\tilde{X}_{qp}) = ic\,\Delta t ,
$$

so $\Delta t$ is recovered as $\mathrm{Im}\,\mathrm{Sc}(\tilde{X}_{qp})/c$, and the sign of $\Delta t$ is the sign of $\mathrm{Im}\,\mathrm{Sc}(\tilde{X}_{qp})$.

### The Three Classes of Separation

The interval has one of three signs, and these signs define the three causal classes of Minkowski space:

- **spacelike** ($N(\tilde{X}_{qp}) > 0$): the events are too far apart for any signal to join them;
- **null** ($N(\tilde{X}_{qp}) = 0$): the events can be joined by a light signal;
- **timelike** ($N(\tilde{X}_{qp}) < 0$): the events can be joined by a signal travelling more slowly than light.

The null displacements are the light cone. The companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* records the same classification, and the companion article *The Light Cone as the Biquaternion Zero-Divisor Cone* gives the algebraic characterization of the null set, which the next section recalls.

### The Causal Order

An event $p$ can influence an event $q$ only if a signal can pass from the first to the second. Special relativity places one structural condition on such a signal: it travels on or inside the light cone, and it travels forward in time. This condition is encoded in the displacement:

$$
p \preceq q
\quad\Longleftrightarrow\quad
N(\tilde{X}_{qp}) \le 0 \ \text{ and } \ \Delta t \ge 0 .
$$

The relation $\preceq$ is the **causal order**. It is reflexive, since $\tilde{X}_{pp} = 0$ has $N = 0$ and $\Delta t = 0$; the two remaining order properties are established in the sections after the next. Physically, $p \preceq q$ says that a signal emitted at $p$ can reach $q$, and the information carried by that signal can affect what happens at $q$. The converse reading — that a signal *is* the only way for $p$ to affect $q$ — is the causal postulate of the theory, and it is what gives the order its information-theoretic meaning.

## The Light Cone as the Zero-Divisor Cone

The vanishing set of the norm form on the material sector is the double cone

$$
\mathcal{Z} = \{\, \tilde{X} \in \mathbb{M}_- : \tilde{X} \ne 0,\ N(\tilde{X}) = 0 \,\}
= \{\, ic\,t\,e_0 + \mathbf{x} : |\mathbf{x}| = c\,|t| \,\},
$$

the light cone of Minkowski space. The companion article *The Light Cone as the Biquaternion Zero-Divisor Cone* proves the following, and it is quoted here rather than repeated.

**The cone is the zero-divisor set.** A nonzero biquaternion has $N(\tilde{Q}) = 0$ if and only if it is a zero divisor of $\mathbb{B}$: there is a nonzero $\tilde{R}$ with $\tilde{Q}\tilde{R} = 0$. The zero divisors split into a nilpotent family, whose scalar part vanishes, and a family of multiples of the algebra's idempotents, whose scalar part does not. On the real material slice the second family is the one that occurs: a nonzero null element with $ct \ne 0$ is a multiple of an idempotent by the purely imaginary scalar $2ict$,

$$
\tilde{X} = ict\left(e_0 - i\hat{\mathbf{x}}\right) = 2ict\,\tilde{P}(-\hat{\mathbf{x}}),
\qquad
\tilde{P}(-\hat{\mathbf{x}}) = \tfrac12\left(e_0 - i\hat{\mathbf{x}}\right),
\qquad
\hat{\mathbf{x}} = \frac{\mathbf{x}}{|\mathbf{x}|},
$$

so the material cone is the idempotent-multiple branch of $\mathcal{Z}$ realized over the reals, and the nilpotent branch would require complex spatial components. The cone is therefore the locus at which the algebra fails to be invertible. Off the cone the inverse exists explicitly,

$$
\tilde{Q}^{-1} = \frac{\bar{\tilde{Q}}}{N(\tilde{Q})}, \qquad N(\tilde{Q}) \ne 0,
$$

so every nonzero displacement is invertible except the null ones.

**The cone is the propagation locus.** The d'Alembertian of the algebra is the norm form of the gradient, $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$, and a four-wavevector $\tilde{K}$ solves the massless dispersion relation $N(\tilde{K}) = 0$ exactly when it is null. For a null $\tilde{K}$ every function of the phase $\mathrm{Sc}(\tilde{K}\bar{\tilde{X}})$ solves the wave equation, so the null directions are the directions in which the algebra propagates without dispersion.

Two features of $\mathcal{Z}$ are used below. First, it is the common boundary of the three regions of the classification: $N$ is a continuous real function on $\mathbb{M}_-$, its sign is locally constant off $\mathcal{Z}$, and a continuous path can change the sign only by passing through $\mathcal{Z}$. Second, the complement of $\mathcal{Z} \cup \{0\}$ has exactly three connected components: the spacelike region $N > 0$, and the two components of the timelike region $N < 0$, distinguished by the sign of $t$, called the **future** and the **past**. This is the standard three-component structure of Minkowski space; it is what makes the cone a separating surface and not merely a level set.

## The Barrier That the Rotor Group Preserves

### Invariance of the Norm Form

The Lorentz group acts on the material sector by the rotor conjugation

$$
\tilde{X} \;\longmapsto\; \tilde{X}' = \tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^\dagger,
\qquad
\tilde{\Lambda} \in \mathbb{B}, \quad \tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0,
$$

as developed in the companion article *The Lorentz Transformation as a Biquaternionic Rotation*. The norm form is multiplicative, $N(\tilde{Q}\tilde{R}) = N(\tilde{Q})N(\tilde{R})$, and complex conjugation supplies $N(\tilde{\Lambda}^\dagger) = N(\tilde{\Lambda})^*$. Hence

$$
N(\tilde{X}') = N(\tilde{\Lambda}) \, N(\tilde{X}) \, N(\tilde{\Lambda}^\dagger)
= N(\tilde{\Lambda})\,N(\tilde{X})\,N(\tilde{\Lambda})^*
= N(\tilde{X}),
$$

because $N(\tilde{\Lambda}) = e_0$ as a coefficient, that is $N(\tilde{\Lambda}) = 1$ in $\mathbb{C}$. The interval is invariant, and with it the sign of the interval. A rotor cannot map a timelike displacement to a spacelike one, or a null displacement to a non-null one; the three causal classes are invariant under every Lorentz transformation. This is the algebraic form of the statement that the light cone is preserved, and it is the first sense in which the cone is a barrier: the group of allowed changes of frame cannot move a displacement across it.

### The Three Regions Are Orbits

The invariance is sharpened by the orbit structure. Under the restricted Lorentz group $SO^+(1,3) \cong SL(2,\mathbb{C})/\{\pm e_0\}$, realized by the rotor conjugation, the future-directed nonzero null elements of $\mathbb{M}_-$ form a single orbit and their past-directed counterparts form a second, the future-directed timelike elements of a fixed norm form form a single orbit, the past-directed timelike elements of that norm form form a single orbit, and the spacelike elements of a fixed norm form form a single orbit. The automorphism reading of the group is developed in the companion article *The Lorentz Group as Biquaternion Norm-Form Automorphisms*, and the covering and topology in *The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form*.

The orbit statement is exactly the statement that the regions are the algebra's invariant strata. Two events with a timelike separation can be brought to a standard form by a rotor; two events with a spacelike separation cannot be brought to that form, and no rotor relates them. There is no continuous Lorentz transformation that interpolates between the two cases, because the invariant $N$ would have to change sign while remaining equal to itself.

### Why the Barrier Is a Barrier

Combining the two preceding subsections: the sign of $N$ is invariant under the rotor group, and it is locally constant off the cone. A physical process that transforms a configuration continuously — a sequence of boosts and rotations, a worldline, the propagation of a wavefront — therefore cannot carry a displacement from one component of the complement of $\mathcal{Z}$ to another. To pass from the future to the past, or from either to the spacelike region, such a process must land on $\mathcal{Z}$. The cone is not a wall that a process is forbidden to touch; it is the unique surface through which a continuous causal process can change its causal character, and a signal that reaches a spacelike-separated event must have left the cone at some point. The physical postulate that signals do not do so is the causal postulate. The algebra supplies the invariant structure on which the postulate acts.

## Transitivity and Antisymmetry of the Causal Order

The causal order of a physical theory must be transitive: if a signal can pass from $p$ to $q$ and another from $q$ to $r$, then $p$ can influence $r$, by a relay if not directly. In the biquaternion algebra this is a statement about sums of future-directed nonspacelike displacements, and it follows from the triangle inequality.

Write a future-directed nonspacelike displacement in the form

$$
\tilde{a} = i\alpha_a\,e_0 + \mathbf{a}, \qquad \alpha_a = c\,\Delta t_a > 0, \qquad |\mathbf{a}| \le \alpha_a,
$$

the last inequality being $N(\tilde{a}) = -\alpha_a^2 + |\mathbf{a}|^2 \le 0$. Let $\tilde{b} = i\alpha_b\,e_0 + \mathbf{b}$ be a second such displacement. Then

$$
\tilde{a} + \tilde{b} = i(\alpha_a + \alpha_b)\,e_0 + (\mathbf{a} + \mathbf{b}),
$$

and the triangle inequality for the real vector part gives

$$
|\mathbf{a} + \mathbf{b}| \le |\mathbf{a}| + |\mathbf{b}| \le \alpha_a + \alpha_b .
$$

Squaring,

$$
N(\tilde{a} + \tilde{b}) = -(\alpha_a+\alpha_b)^2 + |\mathbf{a}+\mathbf{b}|^2 \le 0,
$$

while the scalar coefficient has $\alpha_a + \alpha_b > 0$, so the sum is future-directed. Hence the sum of two future-directed nonspacelike displacements is future-directed nonspacelike: if $p \preceq q$ and $q \preceq r$, then $p \preceq r$ and the causal order is transitive. Equality $N(\tilde{a}+\tilde{b}) = 0$ occurs only when both displacements are null and their spatial parts are parallel and equally oriented, so that the relay is itself a light signal; two null displacements in non-parallel or oppositely oriented directions sum to a strictly timelike one.

The order is also antisymmetric. If $p \preceq q$ and $q \preceq p$ then $\Delta t \ge 0$ and $\Delta t \le 0$, so $\Delta t = 0$, and $N(\tilde{X}_{qp}) \le 0$ then gives $|\Delta\mathbf{x}| \le 0$, hence $\Delta\mathbf{x} = 0$ and $p = q$. Together with reflexivity and transitivity this makes $\preceq$ a **partial order** on the events: the structure of possible influence is an order, not a graph with cycles, and distinct events are ordered in at most one direction. This is what forbids a signal loop that closes on itself and returns to its own emission event; a closed causal curve in flat spacetime would require a strict part of the order to hold in both directions.

## The Relative-Velocity Barrier

### The Invariant Relative Lorentz Factor

The causal order is between events. A second barrier stands between observers, and it is expressed by the four-velocity biquaternion. For an observer with velocity $\mathbf{v}$, the four-velocity is

$$
\tilde{U} = \gamma\left(ic\,e_0 + \mathbf{v}\right),
\qquad
\gamma = \left(1 - \frac{\mathbf{v}^2}{c^2}\right)^{-1/2},
\qquad
N(\tilde{U}) = -c^2,
$$

as in the companion article *Relativistic Mechanics in Biquaternionic Form*. For two observers with four-velocities $\tilde{U}_1, \tilde{U}_2$, the contraction

$$
-\,\frac{1}{c^2}\,\mathrm{Sc}\!\left(\tilde{U}_1\bar{\tilde{U}}_2\right)
= \gamma_1\gamma_2\left(1 - \frac{\mathbf{v}_1\cdot\mathbf{v}_2}{c^2}\right)
= \gamma_1\gamma_2\left(1 - \beta_1\beta_2\cos\theta\right)
\equiv \gamma_{\mathrm{rel}}
$$

is the Lorentz factor of their relative motion, where $\beta_i = |\mathbf{v}_i|/c$ and $\theta$ is the angle between the two velocities. The computation is the direct product of the two four-velocities in the coefficient representation; it uses $\bar{\tilde{U}}_2 = \gamma_2(ic\,e_0 - \mathbf{v}_2)$ and $\mathrm{Sc}((ic\,e_0+\mathbf{v}_1)\cdot(ic\,e_0-\mathbf{v}_2)) = -c^2 + \mathbf{v}_1\cdot\mathbf{v}_2$. The result is frame-independent because it is built from the invariant norm form, as it must be.

### The Inequality That Makes the Barrier

The barrier is the statement that $\gamma_{\mathrm{rel}} \ge 1$, with equality only for identical velocities. Squaring the definition,

$$
\gamma_{\mathrm{rel}}^2 - 1
= \frac{\beta_1^2 + \beta_2^2 - 2\beta_1\beta_2\cos\theta - \beta_1^2\beta_2^2\sin^2\theta}{(1-\beta_1^2)(1-\beta_2^2)}
\equiv \frac{g(\theta)}{(1-\beta_1^2)(1-\beta_2^2)} .
$$

The denominator is positive, so it suffices to show $g \ge 0$. Put $x = \cos\theta \in [-1,1]$ and expand $\sin^2\theta = 1-x^2$:

$$
g(x) = \beta_1^2\beta_2^2\,x^2 - 2\beta_1\beta_2\,x + \beta_1^2 + \beta_2^2 - \beta_1^2\beta_2^2 .
$$

If either speed vanishes then $g(\theta)$ is the square of the other and the bound is immediate, so assume $\beta_1\beta_2 \ne 0$. This is then a quadratic in $x$ with positive leading coefficient $\beta_1^2\beta_2^2$, so it is decreasing up to its vertex, which sits at

$$
x_0 = \frac{2\beta_1\beta_2}{2\beta_1^2\beta_2^2} = \frac{1}{\beta_1\beta_2} > 1
$$

because $\beta_1\beta_2 < 1$. The interval $[-1,1]$ therefore lies entirely on the decreasing branch, and the minimum on it is at $x = 1$, that is at $\theta = 0$:

$$
g(\theta) \ge g(1) = \beta_1^2 + \beta_2^2 - 2\beta_1\beta_2 = (\beta_1 - \beta_2)^2 \ge 0 .
$$

Hence $\gamma_{\mathrm{rel}} \ge 1$, and equality holds only if $\beta_1 = \beta_2$ and $\theta = 0$, that is only if $\mathbf{v}_1 = \mathbf{v}_2$. Since the relative speed is

$$
v_{\mathrm{rel}} = c\sqrt{1 - \gamma_{\mathrm{rel}}^{-2}},
$$

the inequality says $v_{\mathrm{rel}} < c$ for every pair of distinct observers, with $v_{\mathrm{rel}} = 0$ for coincident velocities. The contraction of two future timelike four-velocities is bounded below by $-c^2$, and the bound is attained only in the rest frame common to both. No pair of observers can be in relative motion at the speed of light or beyond, and the bound is an algebraic consequence of the norm form rather than an extra dynamical assumption.

### Two Evaluations

The formula and its bound are worth checking on the two configurations in which the answer is fixed by symmetry. For $\mathbf{v}_1 = 0.6c\,\hat{e}_1$ and $\mathbf{v}_2 = 0.8c\,\hat{e}_1$, collinear,

$$
\gamma_{\mathrm{rel}} = \gamma_1\gamma_2(1-\beta_1\beta_2) = \frac{5}{4}\cdot\frac{5}{3}\left(1-\frac{12}{25}\right) = \frac{25}{12}\cdot\frac{13}{25} = \frac{13}{12} \approx 1.0833333,
$$

giving $v_{\mathrm{rel}} = c\sqrt{1-(12/13)^2} = \frac{5}{13}c \approx 0.3846154\,c$, which is the velocity-subtraction value $(0.8-0.6)/(1-0.48)c$. For $\mathbf{v}_1 = 0.6c\,\hat{e}_1$ and $\mathbf{v}_2 = 0.6c\,\hat{e}_2$, orthogonal and of equal speed, $\cos\theta = 0$ and

$$
\gamma_{\mathrm{rel}} = \gamma_1\gamma_2 = \left(\frac{5}{4}\right)^2 = \frac{25}{16} = 1.5625,
\qquad
v_{\mathrm{rel}} = c\sqrt{1-\frac{256}{625}} = \frac{\sqrt{369}}{25}\,c \approx 0.7683749\,c .
$$

This is the equal-rapidity orthogonal instance worked in the companion article *Exercise: Boosting a Four-Velocity and Rapidity Composition*, which obtains the same $0.7683749\,c$ both as the composed speed $c\tanh\Psi$ of the product rotor and from the velocity-addition formula applied twice. For equal orthogonal rapidities the relative speed and the composed speed coincide, $\gamma_{\mathrm{rel}} = \cosh\Psi$, so the agreement of the invariant contraction with the explicitly composed rotor is a check on the sign and direction conventions of the boost.

## The Rapidity Barrier

The barrier at $v = c$ has a second, group-theoretic expression, and it is the one that shows why the speed of light is unreachable rather than merely unexceeded. A boost is generated by the Hermitian unit-norm biquaternion

$$
\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}},
\qquad
\tanh\psi = \frac{u}{c},
\qquad
\cosh\psi = \gamma,
\qquad
\sinh\psi = \gamma\beta,
$$

where $\psi$ is the **rapidity** and $\hat{\mathbf{u}}$ the boost direction. The rapidity is an additive coordinate on the boost group: two boosts along a common direction compose to a boost of summed rapidity,

$$
\tilde{\Lambda}_2\tilde{\Lambda}_1
= \cosh\frac{\psi_1+\psi_2}{2} + i\sinh\frac{\psi_1+\psi_2}{2}\hat{\mathbf{u}},
$$

as verified in the companion article *Exercise: Boosting a Four-Velocity and Rapidity Composition*. The corresponding velocities compose by the hyperbolic addition law

$$
w = c\tanh(\psi_1+\psi_2)
= \frac{u_1+u_2}{1+u_1u_2/c^2} .
$$

The velocity is therefore a bounded, monotone function of the rapidity,

$$
\frac{u}{c} = \beta = \tanh\psi \in (-1,1) \quad \text{for every finite } \psi \in \mathbb{R},
$$

and the bound is approached only as $\psi \to \infty$:

$$
1 - \tanh\psi = \frac{2}{e^{2\psi}+1} \;\longrightarrow\; 0 .
$$

A finite composition of boosts has a finite total rapidity $\psi_1+\cdots+\psi_n$, hence a speed strictly below $c$; to reach the cone one would need an infinite rapidity, and no finite sequence of subluminal operations supplies it. This is the sense in which the light cone lies at infinity in the group parameter. The barrier is not a ceiling that a process approaches and stops at; it is a limit that is approached but never attained, and the group is non-compact precisely because its boost parameter is unbounded. The check is elementary: composing the subluminal speed $\beta = 0.9$ with itself $n$ times in the hyperbolic sense gives $\beta_n = \tanh(n\,\mathrm{atanh}\,0.9)$, for which $1-\beta_n \approx 2e^{-2n\,\mathrm{atanh}\,0.9}$; at $n = 5$ the deficit is $8.08\times10^{-7}$, at $n = 10$ it is $3.26\times10^{-13}$, and it remains positive for every finite $n$, becoming indistinguishable from zero in double precision only when the deficit falls below the representable range, near $n = 13$.

The same bound appears in the contraction of a null wavevector with an observer, treated in the companion article *Exercise: The Relativistic Doppler Effect*: the measured frequency $-\mathrm{Sc}(\tilde{K}\bar{\tilde{U}})$ is strictly positive for every future timelike $\tilde{U}$ and every future null $\tilde{K}$, so a light signal cannot be brought to zero frequency by a change of observer. The impossibility of bringing that contraction to zero, the impossibility of closing the relative-velocity deficit, and the vanishing of $N(\tilde{K})$ are three faces of the same cone.

## The Cone as the Characteristic Cone of the Wave Operator

The barrier has an analytic form, and it is the form in which the algebra itself enforces it. The biquaternionic gradient and its conjugate are

$$
\tilde{\nabla} = e_0\,\partial_{ict} + \nabla,
\qquad
\bar{\tilde{\nabla}} = e_0\,\partial_{ict} - \nabla,
\qquad
\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta = \Delta - \frac{1}{c^2}\partial_t^2,
$$

the series' d'Alembertian. For a wave whose phase is the scalar $s = \mathrm{Sc}(\tilde{K}\bar{\tilde{X}}) = -\omega t + \mathbf{k}\cdot\mathbf{x}$, the chain rule gives the corpus identity

$$
\Box f(s) = N(\tilde{K})\,f''(s),
\qquad
N(\tilde{K}) = -\frac{\omega^2}{c^2} + |\mathbf{k}|^2,
$$

because $s$ is linear and $\Box s = 0$. The exponential $e^{s}$ is therefore an eigenfunction with eigenvalue $N(\tilde{K})$, and the oscillatory positive-frequency wave $e^{is}$ has eigenvalue $-N(\tilde{K})$, the two differing by the overall sign that leaves the kernel unchanged. In either case the characteristic variety, the set on which the symbol vanishes, is exactly the null cone $\mathcal{Z}$. The cone is therefore the characteristic cone of the algebra's own wave operator, and the companion article *The Light Cone as the Biquaternion Zero-Divisor Cone* records the equivalent zero-divisor statement.

The standard theory of hyperbolic operators now supplies the propagation bound. A second-order linear hyperbolic equation with the characteristic cone $\mathcal{Z}$ has finite propagation speed: if a source $\tilde{S}$ is supported in a compact set $K$ at time $t = 0$, then the solution of $\Box\tilde{\Phi} = \tilde{S}$ is supported at time $t$ inside the set of points that lie within distance $ct$ of $K$, that is, inside the union of the light cones erected on $K$. This is a theorem of the classical theory of partial differential equations, not a property of the biquaternion formulation, and it is cited as standard. Its content here is that the barrier is not imposed on the algebra from outside: the wave operator that the algebra naturally carries has the cone as its characteristic surface, so a field generated in a bounded region propagates only into that region's causal future. The algebraic zero-divisor cone, the geometric light cone and the analytic characteristic cone are the same set.

## Causal Automorphisms and the Time Orientation

The invariance of the norm form identifies the Lorentz group as a group of transformations preserving the cone. The converse is a classical theorem, and it is what makes the cone the complete invariant of the causal structure. A bijection of Minkowski space that preserves the causal order, in the sense that

$$
p \preceq q \quad\Longleftrightarrow\quad f(p) \preceq f(q),
$$

is the composition of a Lorentz transformation, a translation, and a positive dilation. This is the theorem of Aleksandrov and Zeeman; it is cited as a standard result of the causal structure of Minkowski space. In the biquaternion formulation the Lorentz part is the rotor conjugation $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ with $N(\tilde{\Lambda}) = e_0$, and the translation is the addition of a fixed displacement $\tilde{T} \in \mathbb{M}_-$:

$$
\tilde{X} \;\longmapsto\; \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger + \tilde{T}.
$$

The theorem says that the cone, together with the time orientation, determines the allowed transformations up to these two operations. Nothing beyond the causal order is needed to recover the kinematics of the frame changes; the barrier is not only preserved by the relativity group, it characterizes it.

Within the full Lorentz group, the proper orthochronous component is the one realized by the rotor conjugation with $N(\tilde{\Lambda}) = e_0$, namely $SO^+(1,3) \cong SL(2,\mathbb{C})/\{\pm e_0\}$. This is the identity component, and it is the component that preserves the distinction between future and past: a composition of boosts and spatial rotations maps a future-directed timelike displacement to a future-directed timelike displacement, never to a past-directed one. The discrete transformations that exchange the sheets — time reversal and the combined parity–time reversal — are not rotor conjugations, and in the biquaternion reading they are not elements of the connected group at all. The immediate physical consequence is that a process built from continuous changes of frame cannot reverse a causal arrow, and the two timelike components of the complement of $\mathcal{Z}$, though related by an inadmissible reflection, are not connected by any allowed motion.

## The Barrier in Information-Theoretic Form

It is now possible to state the result in the language for which the article is named. Relative to an event $p$, define

$$
J^+(p) = \{\, q : p \preceq q \,\},
\qquad
J^-(p) = \{\, q : q \preceq p \,\},
\qquad
E(p) = \mathbb{M}_- \setminus \big(J^+(p) \cup J^-(p)\big).
$$

$J^+(p)$ and $J^-(p)$ are the **causal future** and **causal past** of $p$, and $E(p)$ is its **elsewhere**, the set of events with a spacelike separation from $p$. In terms of the displacement $\tilde{X}_{qp}$, membership in $J^+(p)$ is the condition $N(\tilde{X}_{qp}) \le 0$ with $\mathrm{Im}\,\mathrm{Sc}(\tilde{X}_{qp}) \ge 0$; membership in $J^-(p)$ is the same norm condition with the opposite sign of the scalar part; and $E(p)$ is the set on which $N(\tilde{X}_{qp}) > 0$. Each of the three sets is a union of orbits of the rotor group, and their common boundary is the light cone through $p$.

The information-theoretic content is the following pair of statements.

**What can be exchanged.** A signal emitted at $p$ can be received exactly at the events of $J^+(p)$. Within that set the delay is bounded below by the straight-line light travel time, $\Delta t \ge |\Delta\mathbf{x}|/c$, with equality exactly for a null displacement. For two events in $J^+(p)$ the relay of the transitivity section shows that a chain of causal segments is again a causal segment, so the reachable set is closed under relays. Nothing in this statement distinguishes one interaction from another: the reachable set is fixed by the causal order alone.

**What cannot be exchanged.** No admissible signal connects $p$ to any event of $E(p)$. A process that starts inside the cone and is built from continuous causal steps remains inside the cone, as the connectivity and invariance arguments of the preceding sections show, so it cannot arrive at a spacelike-separated event. Equivalently, an influence that reached $E(p)$ would have to leave the cone at some intermediate event, which is the negation of the causal postulate.

The honest qualification is that the second statement is a physical postulate, not a theorem of the algebra. The algebra contains spacelike elements of $\mathbb{M}_-$ with $N > 0$, and it assigns them an inverse and a well-defined norm; it does not by itself exclude a process that propagates on them. What the algebra does is fix the structure on which the postulate is imposed: the three invariant strata, the partial order, the relative-velocity bound and the characteristic cone. Given the postulate that physical signals travel on or inside the cone, the barrier is then complete: the elsewhere is informationally inert, the cone is its boundary, and no change of frame moves the boundary. The sharpness of the barrier is the sharpness of the postulate, and the clean separation of the two — the algebra's invariant structure on the one hand, the causal postulate on the other — is the contribution of the biquaternion reading.

There is no corresponding barrier for observers at a single event: two observers may coincide at an event and separate thereafter, and each later event of either worldline lies in the causal future of that coincidence, though events on the two worldlines after the coincidence need not be causally related to one another. The barrier is between events and between velocities, not between observers as such. What the relative-velocity bound adds is that the two observers' worldlines remain inside each other's cones forever, and no finite sequence of frame changes can bring either worldline onto the cone of the other.

The conventions and the results taken over from the relativity series are those of the following companion articles:

- Companion article *Introduction to the Biquaternion Universe*, for the notation, the norm form and the causal trichotomy.
- Companion article *Conventions in the Biquaternion Universe*, for the algebra and basis, the four conjugations, the real subspaces and the metric at its three levels.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the material four-vector, the interval and the causal classification.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the Hermitian sector and its distinct informational reading.
- Companion article *The Light Cone as the Biquaternion Zero-Divisor Cone*, for the zero-divisor criterion, the idempotent form of the real cone and the dispersionless propagation locus.
- Companion article *The Lorentz Transformation as a Biquaternionic Rotation*, for the rotor conjugation and its component action.
- Companion article *The Lorentz Group as Biquaternion Norm-Form Automorphisms*, for the orbit structure of the causal classes.
- Companion article *The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form*, for the topology of the boost group and the two sheets.
- Companion article *Relativistic Mechanics in Biquaternionic Form*, for the four-velocity, the proper-time integral and the invariant interval.
- Companion article *Exercise: Boosting a Four-Velocity and Rapidity Composition*, for the additive composition of rapidities and the composed velocity.
- Companion article *Exercise: The Relativistic Doppler Effect*, for the four-wavevector, the invariant phase and the frequency measured by an observer.

## Summary

The causal structure of the material sector $\mathbb{M}_-$ is the structure of the norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ and of its vanishing set, the light cone.

1. **The interval and its sign.** For the displacement $\tilde{X}_{qp} = ic\,\Delta t\,e_0 + \Delta\mathbf{x}$, the interval is $N(\tilde{X}_{qp}) = -c^2(\Delta t)^2 + |\Delta\mathbf{x}|^2$, and its sign divides Minkowski space into the spacelike, null and timelike regions. The null set is the light cone, which the companion article *The Light Cone as the Biquaternion Zero-Divisor Cone* identifies with the material-sector part of the zero-divisor set of the algebra.

2. **The causal order.** The relation $p \preceq q$, defined by $N(\tilde{X}_{qp}) \le 0$ with $\Delta t \ge 0$, is a partial order. Transitivity follows from the triangle inequality: a sum of future-directed nonspacelike displacements is future-directed nonspacelike, with equality in $N$ only for null segments that are parallel and equally oriented.

3. **Invariance.** The norm form is invariant under the rotor conjugation, $N(\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger) = N(\tilde{X})$ for $N(\tilde{\Lambda}) = e_0$, so the causal classes are invariant, and the invariant strata — the two sheets of the null cone, the two timelike sheets of a fixed norm form, and the spacelike region of that norm form — are the orbits of the restricted Lorentz group.

4. **The topological barrier.** The complement of the cone has three connected components, and $N$ can change sign along a continuous path only at the cone. A continuous causal process therefore reaches the elsewhere only by leaving the cone.

5. **The relative-velocity barrier.** The invariant contraction of two future timelike four-velocities satisfies $-\mathrm{Sc}(\tilde{U}_1\bar{\tilde{U}}_2)/c^2 = \gamma_1\gamma_2(1-\beta_1\beta_2\cos\theta) = \gamma_{\mathrm{rel}} \ge 1$, with equality only for equal velocities; the relative speed is strictly below $c$.

6. **The rapidity barrier.** Boosts compose additively in rapidity, $\beta = \tanh\psi$, so the barrier $\beta = 1$ lies at $\psi = \infty$ and is attained by no finite composition.

7. **The analytic barrier.** The cone is the characteristic cone of $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$, and the standard finite-speed-of-propagation theorem confines the support of a solution to the causal future of its source.

8. **The uniqueness of the structure.** A causal bijection of Minkowski space is a Lorentz transformation composed with a translation, up to a positive dilation (Aleksandrov–Zeeman), so the cone and its time orientation characterize the relativity group rather than merely being preserved by it. The proper orthochronous component is the one realized by the rotor conjugation, and it preserves the time orientation.

The information-theoretic reading is that $J^+(p)$ is the set of events that $p$ can signal, $J^-(p)$ the set that can signal $p$, and $E(p)$ the set that can neither signal $p$ nor be signalled by it. The algebra fixes the structure; the causal postulate that signals travel on or inside the cone makes the boundary of the reachable set an information barrier.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector): imaginary scalar, real vector |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector) |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $c$, $c_0$ | Speed of light in the medium, and in vacuum |
| $\bar{\tilde{Q}}, \tilde{Q}^* , \tilde{Q}^\dagger = \bar{\tilde{Q}}^{*}$ | Quaternion, complex and Hermitian conjugation |
| $\tilde{X} = ic\,t\,e_0 + \mathbf{x}$ | Material four-position |
| $\tilde{X}_{qp} = \tilde{X}_q - \tilde{X}_p$ | Displacement from $p$ to $q$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form; the interval on $\mathbb{M}_-$ |
| $\eta = \mathrm{diag}(-1,+1,+1,+1)$ | $ict$-coordinate metric |
| $\mathrm{Sc}$ | Scalar projection of a biquaternion |
| $\mathcal{Z}$ | Light cone: the $N=0$ locus of $\mathbb{M}_-$, the material-sector part of the zero-divisor set of $\mathbb{B}$ |
| $p \preceq q$ | Causal order: $N(\tilde{X}_{qp})\le 0$ and $\Delta t\ge 0$ |
| $J^+(p)$, $J^-(p)$, $E(p)$ | Causal future, causal past, and elsewhere of $p$ |
| $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$, $N(\tilde{\Lambda})=e_0$ | Boost rotor (unit-norm biquaternion) |
| $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ | Rotor conjugation |
| $\tilde{U} = \gamma(ic\,e_0+\mathbf{v})$, $N(\tilde{U})=-c^2$ | Four-velocity |
| $\beta = |\mathbf{v}|/c$, $\gamma = (1-\beta^2)^{-1/2}$ | Dimensionless speed and Lorentz factor |
| $\psi$, $\tanh\psi=\beta$ | Rapidity |
| $\gamma_{\mathrm{rel}} = \gamma_1\gamma_2(1-\beta_1\beta_2\cos\theta)$ | Relative Lorentz factor, $= -\mathrm{Sc}(\tilde{U}_1\bar{\tilde{U}}_2)/c^2$ |
| $\tilde{\nabla}, \bar{\tilde{\nabla}}$ | Biquaternionic gradient and its conjugate |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2+\Delta$ | d'Alembertian, series convention |
| $SO^+(1,3)\cong SL(2,\mathbb{C})/\{\pm e_0\}$ | Restricted Lorentz group |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the light cone and the four-dimensional formulation of the causal structure.
- Albert Einstein, "Zur Elektrodynamik bewegter Körper," *Annalen der Physik* **17** (1905) 891–921, for the relativity principle and the invariant interval.
- E. C. Zeeman, "Causality implies the Lorentz group," *Journal of Mathematical Physics* **5** (1964) 490–493, for the theorem that the causal order determines the Lorentz group.
- A. D. Aleksandrov, "Mappings of spaces with families of cones and space–time transformations," *Annali di Matematica Pura ed Applicata* **103** (1975) 229–257, for the Aleksandrov–Zeeman theorem in its general form.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the interval, the light cone and the causal classification.
- Christian Møller, *The Theory of Relativity* (Oxford, 1972), for the causal structure and the impossibility of superluminal signalling.
- Stephen W. Hawking and George F. R. Ellis, *The Large Scale Structure of Space-Time* (Cambridge, 1973), for the future and past sets, the causal order and the three-component structure of Minkowski space.
- Robert M. Wald, *General Relativity* (Chicago, 1984), for the causal structure and the proofs of the order properties.
- Richard Courant and David Hilbert, *Methods of Mathematical Physics*, Vol. II (Interscience, 1962), for the characteristic cone of the wave operator.
- F. G. Friedlander, *The Wave Equation on a Curved Space-Time* (Cambridge, 1975), for the finite speed of propagation and the support of retarded solutions.
- Stefano Liberati, Sebastiano Sonego and Matt Visser, "Faster-than-c signals, special relativity, and causality," *Annals of Physics* **298** (2002) 167–185, for the relation between superluminal signalling and the failure of the causal order.
