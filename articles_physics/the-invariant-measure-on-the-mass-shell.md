# __The Invariant Measure on the Mass Shell__

## Introduction

A mass shell is a homogeneous space, and a homogeneous space of a unimodular group carries an invariant measure. For the Lorentz group that measure is the density $\frac{d^{3}p}{2p_0}$ on the hyperboloid, or equivalently the four-dimensional integral $d^{4}p\,\delta(N+m^{2}c^{2})\,\mathrm{H}_{\mathrm{hvs}}(p_0)$, with $\mathrm{H}_{\mathrm{hvs}}$ the Heaviside step that keeps the energy positive. Every Lorentz-invariant integral over momenta is written with it, and every normalisation convention in field theory is a convention about it.

This article constructs the measure, verifies its invariance, writes it in three coordinate systems, states the invariant integral and its delta-function form, fixes the normalisation, and treats the cases in which the construction degenerates.

The article assumes *Wigner's Classification: Two Casimirs, Three Orbits* for the orbits, *The Little Group of a Massive Particle: $\mathrm{SU}(2)$* and *The Little Group of a Null Momentum: $E(2)$* for the stabilisers, *The Null Cone: The Massless Boundary* for the cone, and *Aberration and the Sky: The Boost as a Möbius Flow* for the sphere of directions.

## The Orbit as a Homogeneous Space

### The Momentum and Its Stabiliser

For a momentum $\tilde P$ on the orbit $\mathcal{O}$, the stabiliser is $G_{\tilde P}$, and the map

$$
G\longrightarrow\mathcal{O},\qquad \tilde U\longmapsto\mathrm{Cg}_{\tilde U}(\tilde P)
$$

is surjective with fibre $G_{\tilde P}$. So the orbit is the quotient

$$
\mathcal{O}\cong G/G_{\tilde P},
$$

a homogeneous space.

### The Quotient

| orbit | stabiliser | quotient |
|---|---|---|
| timelike | $SU(2)$ | $\mathbb{H}^{3}$ |
| null | $E(2)$ | $\mathbb{R}_{>0}\times S^{2}$ |
| spacelike | $SU(1,1)$ | $S^{2}\times\mathbb{R}$ |

The three quotients have the dimensions the group theory demands: $6-3=3$ in each case.

### The Three Cases

The three are different manifolds with different geometry, but the construction of the measure is the same in all three. That is the point of the homogeneous-space formulation: the measure is not a special feature of the hyperboloid, it is a feature of the pair (group, stabiliser).

## The Invariant Measure

### What Invariance Means

A measure $\mu$ on $\mathcal{O}$ is invariant when

$$
\mu(\Lambda A)=\mu(A)
$$

for every Borel set $A$ and every $\Lambda$ in the group. Equivalently, for every integrable $f$,

$$
\int_{\mathcal{O}}f(\Lambda p)\,d\mu(p)=\int_{\mathcal{O}}f(p)\,d\mu(p).
$$

### The Construction

The invariant measure on $G$ descends to the quotient when the stabiliser is unimodular: one takes a measure on $G$, integrates out the fibre, and the result is invariant. Both the Lorentz group and each of its little groups are unimodular, so the construction goes through in all three cases.

That is the warrant: the existence of the measure is a unimodularity theorem, not a guess, and it is why the same construction works for the massive, the massless and the spacelike orbits.

### The Jacobian

In coordinates the invariance is a Jacobian identity. For a boost along $z$ with velocity $\beta$,

$$
p_z'=\gamma\bigl(p_z+\beta E\bigr),\qquad
E'=\gamma\bigl(E+\beta p_z\bigr),
$$

so the Jacobian of the map $\vec p\mapsto\vec p'$ is

$$
\det\frac{\partial\vec p'}{\partial\vec p}=\frac{E'}{E}.
$$

The identity is verified numerically to twelve digits at three different momenta: the determinant comes out $1.556186218$ and the ratio $E'/E$ comes out $1.556186218$ at $E=1.224745$, and the two agree at the other points as well.

So $\frac{d^{3}p'}{E'}=\frac{d^{3}p}{E}$, and the measure is invariant.

### The Consequence

$$
\frac{d^{3}p}{2E}
$$

is invariant, the factor $\tfrac12$ being a convention that makes the normalisation of states come out without fractions. Everything else in this article is a consequence of this one identity.

**The letter $E$ is the temporal component.** Throughout this article $E$ denotes $p_{t}$, the temporal coefficient of the momentum, so the four-momentum is $(E,\vec p)$ and the interval is $N=-E^{2}+\lvert\vec p\rvert^{2}=-m^{2}c^{2}$. The energy is $cE$. With that reading every formula below is dimensionally homogeneous, the boost law $p_z'=\gamma(p_z+\beta E)$ needs no factor of $c$, the velocity $\vec v=\vec p/E$ is measured in units of $c$, and the factor $\frac{1}{2E}$ is the delta function's Jacobian.

## The Density

### The Invariant Volume

The invariant volume element on the hyperboloid is

$$
d\mu=\frac{d^{3}p}{2p_0}\bigg|_{p_0=E_{\vec p}},
\qquad
E_{\vec p}=\sqrt{m^{2}c^{2}+\lvert\vec p\rvert^{2}} .
$$

It is positive, it is smooth on the interior of the orbit, and its total volume is infinite, as it must be for a non-compact space of finite dimension.

### The Velocity Form

In terms of the velocity $\vec v=\vec p/E$,

$$
\frac{d^{3}p}{2E}=\frac{m^{2}c^{2}}{2}\,\frac{d^{3}v}{(1-\lvert\vec v\rvert^{2})^{2}} .
$$

The check, with the velocity in units of $c$ and the momentum in units of $mc$: at $\vec v=(0.3,0.4,0.5)$ the Jacobian $\det(\partial\vec p/\partial\vec v)$ divided by $E$ is $4.000000000$, and $\frac{m^{2}c^{2}}{(1-\lvert\vec v\rvert^{2})^{2}}$ is $4.000000000$ at that velocity. The denominator is the square of the Lorentz factor's reciprocal, which is the hyperbolic volume form of the velocity ball: the ball with the metric of constant negative curvature.

### The Sky Form

In terms of the direction and the energy,

$$
\frac{d^{3}p}{2E}=\tfrac12\,p\,dE\,d\Omega ,
$$

where $d\Omega$ is the solid angle. The derivation is one line: writing $p=\lvert\vec p\rvert$, $d^{3}p=p^{2}dp\,d\Omega$ and $p\,dp=E\,dE$, the second because $\lvert\vec p\rvert^{2}=E^{2}-m^{2}c^{2}$.

So the measure factorises into a *radial* part and an *angular* part, and the angular part is the round measure on the sky of *Aberration and the Sky: The Boost as a Möbius Flow*. That factorisation is why the sky's measure is the one an observer integrates over in the cosmic microwave background.

### The Three Forms Compared

| coordinates | density | invariant? |
|---|---|---|
| $\vec p$ | $d^{3}p/(2E)$ | yes |
| $\vec v$ | $m^{2}c^{2}d^{3}v/2(1-v^{2})^{2}$ | yes |
| $E,\Omega$ | $\tfrac12\,p\,dE\,d\Omega$ | yes in the angular part only |

The third row's caveat is the point: $d\Omega$ alone is invariant under rotations but not under boosts, and $E$ transforms under boosts, so the factorisation is useful only for rotation-invariant integrands.

## The Lorentz-Invariant Integral

### The Standard Form

The invariant integral of a function on the shell is

$$
\int_{\mathcal{O}}f(p)\,d\mu(p)=\int\frac{d^{3}p}{2E_{\vec p}}\,f(E_{\vec p},\vec p).
$$

Every physical quantity integrated over momenta — a phase-space integral, a luminosity, a decay rate — is of this form, and the invariance is the statement that the result does not depend on the frame.

### The Delta-Function Form

The same integral in four dimensions is

$$
\int d^{4}p\;\delta\bigl(N(\tilde Q_{\Phi})+m^{2}c^{2}\bigr)\,\mathrm{H}_{\mathrm{hvs}}(p_0)\,f(p)
=\int\frac{d^{3}p}{2E_{\vec p}}\,f(E_{\vec p},\vec p),
$$

where the norm is $N(\tilde Q_{\Phi})=-p_0^{2}+\lvert\vec p\rvert^{2}$ on the free material element $\tilde Q_{\Phi}$, the norm being the plain sum $\sum_{\imath} P_{\imath}^{2}$ under the unit metric $\delta_{\imath\jmath}=(1,1,1,1)$, whose one minus on the time slot is the square of the $i$ in $P_t=iE$. The particle's own momentum is the fixed comparison point, with $N(\tilde P_{\Phi})=-m^{2}c^{2}$. The argument of the delta is therefore $\mathcal{M}(\tilde Q_{\Phi})=N(\tilde Q_{\Phi})-N(\tilde P_{\Phi})$, and the mass shell it selects is $N(\tilde Q_{\Phi})=-m^{2}c^{2}$. The root contributes the factor $\frac{1}{2E}$:

$$
\delta\bigl(N(\tilde Q_{\Phi})+m^{2}c^{2}\bigr)=\frac{1}{2E}\Bigl[\delta\bigl(p_0-E\bigr)+\delta\bigl(p_0+E\bigr)\Bigr],
$$

and the step function keeps the positive-energy root. So the $\frac{1}{2E}$ is not a convention but the Jacobian of the delta function, and the convention is only the choice of writing it inside or outside.

### The Two-Point Function

The simplest invariant integral is

$$
\int\frac{d^{3}p}{2E_{\vec p}}\,e^{-ip\cdot x},
$$

which is the positive-frequency part of the invariant delta function. Its Lorentz invariance follows from the measure's. The function itself does not vanish outside the light cone — it decays exponentially — but its antisymmetric combination does: the commutator, which is the difference of the positive- and negative-frequency integrals, is supported on the light cone and vanishes at spacelike separation. That vanishing is the microcausality statement, and it too follows from the measure's invariance.

## The Normalisation

### The Choice

There are three standard normalisations, and they differ by powers of $2E$ and $2\pi$:

| convention | inner product of momentum states |
|---|---|
| covariant with $(2\pi)^{3}$ | $\langle\vec p\vert\vec q\rangle=2E_{\vec p}(2\pi)^{3}\delta^{3}(\vec p-\vec q)$ |
| covariant without $(2\pi)^{3}$ | $\langle\vec p\vert\vec q\rangle=2E_{\vec p}\delta^{3}(\vec p-\vec q)$ |
| non-relativistic | $\langle\vec p\vert\vec q\rangle=\delta^{3}(\vec p-\vec q)$, with the amplitude $N_{\vec p}$ absorbed into the state, $N_{\vec p}^{2}=2E_{\vec p}$ |

The three are related by absorbing the amplitude $N_{\vec p}$ into the state's normalisation, $N_{\vec p}^{2}=2E_{\vec p}$, and by a power of $2\pi$; the root itself is a half power of the base units and is never printed. The block uses the covariant one, because it makes the measure's invariance manifest: the identity operator reads

$$
1=\int\frac{d^{3}p}{2E_{\vec p}}\,|p\rangle\langle p| ,
$$

with no extra factor.

### Why It Matters

A normalisation error is a factor of $2E$ per external leg, and it is the most common error in a calculation that mixes conventions. So the block states the convention once, here, and every other article refers to it.

### The Normalisation of the Measure Itself

$\frac{d^{3}p}{2E}$ has the dimension of a momentum squared, $M^{2}L^{2}T^{-2}$, because $d^{3}p$ is a momentum cubed and $E$ a momentum. A reader who wants a dimensionless measure divides by $(2\pi)^{3}$ and multiplies by the volume, which is the phase-space counting convention of statistical mechanics.

## The Exceptional Cases

### The Vertex

At $p=0$ the orbit degenerates to a point and its stabiliser is the whole group. The measure on a point is the counting measure, and the invariant "integral" over it is the evaluation at zero: the zero-momentum state is the vacuum, and its measure is not a density at all.

That is the one place where the homogeneous-space description fails, and it fails because the quotient $G/G$ is a point and not a manifold.

### The Null Orbit

On the null orbit $E=\lvert\vec p\rvert$, so the density $\frac{d^{3}p}{2E}$ has a singularity at the vertex and is not integrable there. The correct statement keeps the vertex out of the orbit and uses

$$
d^{4}p\;\delta\bigl(N\bigr)\,\mathrm{H}_{\mathrm{hvs}}(p_0),
$$

which on the cone becomes $\frac12E\,dE\,d\Omega$ with $E>0$: a genuine density, since $E$ is now the radial coordinate of the cone.

So the massless measure exists and is perfectly well behaved away from the vertex; what fails is the *massive* form's limit, because the massive form's $E$ does not vanish as $m\to0$.

### The Boundary Between

The massless orbit is the boundary of the massive ones in the orbit space, and the measure's behaviour reflects that: as $m\to0$ the density's normalisation $m^{2}c^{2}/2$ in the velocity form vanishes, so the massive measure degenerates to zero on the velocity ball and the whole mass moves to the boundary. That is the measure-theoretic form of the statement that a massless particle is not a limit of massive ones with a finite mass.

### The Spacelike Orbit

The spacelike measure is $\frac{d^{3}p}{2\lvert p_3\rvert}$ with $p_3$ the component chosen as the coordinate, because the one-sheeted hyperboloid meets each line of constant $(p_0,p_1,p_2)$ twice and the delta function $\delta(N-\mu^{2})$ has two roots, at $p_3=\pm\sqrt{\mu^{2}+p_0^{2}-p_1^{2}-p_2^{2}}$. The step function of the timelike case is replaced by a choice of branch, and the invariant density is $\frac{d^{3}p}{2\lvert p_3\rvert}$ on the branch. So the construction is the same and the physical interpretation is different.

## Summary

A mass shell is a homogeneous space $G/G_{\tilde P}$, and because the group and its little groups are unimodular it carries an invariant measure. In momentum coordinates the measure is $d^{3}p/(2E)$, verified invariant by the Jacobian identity $\det(\partial\vec p'/\partial\vec p)=E'/E$; in velocity coordinates it is $\frac{m^{2}c^{2}}{2}\frac{d^{3}v}{(1-v^{2})^{2}}$; in energy and angle it is $\frac12E\,dE\,d\Omega$. The four-dimensional form $d^{4}p\,\delta(N+m^{2}c^{2})\mathrm{H}_{\mathrm{hvs}}(p_0)$ is the same measure, and its $\frac{1}{2E}$ is the delta function's Jacobian. The block normalises states covariantly so that the identity operator is $\int\frac{d^{3}p}{2E}|p\rangle\langle p|$. The vertex is a degenerate orbit, the null orbit needs the cone form, and the massive measure degenerates to zero as the mass goes to zero.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathcal{O}\cong G/G_{\tilde P}$ | the orbit as a homogeneous space |
| $E_{\vec p}=\sqrt{m^{2}c^{2}+\lvert\vec p\rvert^{2}}$ | the temporal momentum on the shell, the energy over $c$ |
| $d^{3}p/(2E)$ | the invariant density |
| $\vec v=\vec p/E$ | the velocity |
| $d\Omega$ | the solid angle on the sky |
| covariant normalisation | $\langle p\lvert q\rangle=2E(2\pi)^{3}\delta^{3}$ |

## Further Reading

- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1, Cambridge University Press, 1995, §2.5 and §4.1 — the invariant measure, the covariant normalisation and the identity operator.
- A. O. Barut and R. Rączka, *Theory of Group Representations and Applications*, PWN, 1977 — invariant measures on homogeneous spaces and the unimodularity condition.
- N. Bourbaki, *Integration II*, Springer, 2004 — the general construction of the quotient measure, in the form the article paraphrases.
- V. S. Varadarajan, *Geometry of Quantum Theory*, 2nd ed., Springer, 1985 — the orbit method with the measures written out.
- *Wigner's Classification: Two Casimirs, Three Orbits* — the orbits whose measures these are.
- *Aberration and the Sky: The Boost as a Möbius Flow* — the angular factor $d\Omega$ and its transformation.
