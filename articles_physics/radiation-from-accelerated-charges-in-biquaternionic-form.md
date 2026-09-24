# __Radiation from Accelerated Charges in Biquaternionic Form__

## Introduction

Radiation is the part of an electromagnetic field that does not remain attached to its source. A charge at rest, or in uniform motion, is surrounded by a field that is carried along with it; only the field of an accelerating charge has a piece that escapes to infinity at the speed of light. This article develops that distinction in the biquaternion framework, starting from the retarded solution of the biquaternionic Maxwell equation established in the companion article *Maxwell's Equations in the Biquaternionic Formulation*.

The biquaternion formulation is a natural language for radiation, for a reason that the companion article *The Field-Strength Biquaternion and Its Invariants* already anticipated. There the field-strength biquaternion

$$
\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}
$$

was shown to have a norm form $N(\tilde{F}) = \tilde{F}\bar{\tilde{F}}$ whose vanishing is exactly the condition that the field be null: $\mathbf{E}\perp\mathbf{B}$ and $|\mathbf{E}| = c|\mathbf{B}|$ pointwise. A null field strength is a **zero divisor** of the algebra $\mathbb{B}$. That null condition is the algebraic signature of a radiation field. The main result of this article is that it is realized, pointwise, by the acceleration part of the Liénard–Wiechert field: the radiation field is precisely the part of $\tilde{F}$ that squares to zero.

The conventions are those of the read-list articles throughout, and nothing in them is changed here. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$, and scalar imaginary $i$ commuting with the quaternion units. The subspaces are $\mathbb{M}_-$ (anti-Hermitian, imaginary scalar and real vector, the material sector), $\mathbb{M}_+$ (Hermitian, real scalar and imaginary vector, the informational sector), $\mathbb{H}_{\mathbb{B}}$ (real quaternions), and $\mathbb{C}_{\mathbb{B}}$ (scalars). The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, with $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta$, and the symbol $c = 1/\sqrt{\epsilon\mu}$ always denotes the speed of light in the medium, reducing to $c_0$ in vacuum. The charge whose field is being computed is written $q$, and its velocity is written $\mathbf{v}$ (the symbol $v$ is reserved for particle velocities, as in the companion articles).

The article is organized as follows. The first section recalls the retarded solution of the Maxwell article and specializes it to a point charge. The second introduces the retarded null biquaternion and writes the Liénard–Wiechert potentials in biquaternion form. The third computes the field and splits it into a velocity part and an acceleration part. The fourth identifies the acceleration part as the radiation field, and the fifth and sixth extract the radiated power and the angular distribution. A short section treats the radiation-reaction problem, and a closing section records how the two downstream exercises are applications of the construction.

Two later exercises use this article as their declared foundation: *Exercise: The Electromagnetic Field of a Moving Charge* and *Exercise: The Electromagnetic Field of a Uniformly Moving Charge*. The construction below is worked out explicitly enough that both are applications of it, R4 being the case of vanishing acceleration and E1 the general case.

## The Retarded Solution for a Point Source

The Maxwell article establishes that in the Lorenz gauge the potential biquaternion satisfies the biquaternionic wave equation

$$
\Box \tilde{A} = -\mu\,\tilde{R}', \qquad \tilde{R}' = ic\rho + \mathbf{J},
$$

and that the physically correct solution is the **retarded** one, built by convolution over the past light cone. The scalar Green's function of this second-order equation, distinct from the scalar part of that article's biquaternion-valued retarded Green's function (a first-order kernel of the opposite sign), is the familiar retarded kernel of the d'Alembertian,

$$
G_{\Box}(\tilde{X}) = \frac{1}{4\pi R}\,\delta\!\left(t - \frac{R}{c}\right), \qquad R = |\mathbf{x}|,
$$

so that

$$
\tilde{A}(\tilde{X}) = \mu\int G_{\Box}(\tilde{X} - \tilde{Y})\,\tilde{R}'(\tilde{Y})\,d^4Y .
$$

We do not re-derive this structure; we only specialize it. For a point charge $q$ on a worldline $\mathbf{r}_q(t)$, the source is

$$
\rho(\mathbf{y}, s) = q\,\delta^3\!\left(\mathbf{y} - \mathbf{r}_q(s)\right), \qquad
\mathbf{J}(\mathbf{y}, s) = q\,\mathbf{v}(s)\,\delta^3\!\left(\mathbf{y} - \mathbf{r}_q(s)\right),
$$

and therefore

$$
\tilde{R}'(\tilde{Y}) = q\left(ic\,e_0 + \mathbf{v}(s)\right)\delta^3\!\left(\mathbf{y} - \mathbf{r}_q(s)\right).
$$

Substituting this into the retarded convolution and integrating first over $\mathbf{y}$ localizes the source at $\mathbf{y} = \mathbf{r}_q(s)$; the remaining integral over $s$ localizes at the **retarded time** $t_r$ defined implicitly by

$$
t_r = t - \frac{\left|\mathbf{x} - \mathbf{r}_q(t_r)\right|}{c}.
$$

Writing $h(s) = s + |\mathbf{x} - \mathbf{r}_q(s)|/c - t$, one has $h'(s) = 1 - \hat{\mathbf{R}}\cdot\boldsymbol{\beta}$, so the delta function contributes the Jacobian

$$
\delta\!\left(t - \frac{|\mathbf{x} - \mathbf{r}_q(s)|}{c} - s\right)
= \frac{1}{1 - \hat{\mathbf{R}}\cdot\boldsymbol{\beta}}\,\delta(s - t_r).
$$

Collecting the pieces, the retarded solution is the **Liénard–Wiechert potential**

$$
\tilde{A} = \frac{\mu q}{4\pi}\,\frac{ic\,e_0 + \mathbf{v}(t_r)}{R - \mathbf{R}\cdot\boldsymbol{\beta}},
$$

where from here on all source quantities are understood to be evaluated at the retarded time, and

$$
\mathbf{R} = \mathbf{x} - \mathbf{r}_q(t_r), \qquad R = |\mathbf{R}|, \qquad
\hat{\mathbf{R}} = \frac{\mathbf{R}}{R}, \qquad \boldsymbol{\beta} = \frac{\mathbf{v}(t_r)}{c}.
$$

The single retardation of a point charge is thus the only place where the light-cone structure of the theory enters the radiation problem; everything that follows is algebra.

## The Retarded Null Biquaternion

It is convenient to name the two biquaternions that appear in the Liénard–Wiechert potential. The first is the **retarded separation**

$$
\tilde{\mathcal{R}} = iR\,e_0 + \mathbf{R},
$$

which is an element of the material subspace $\mathbb{M}_-$: its scalar part is imaginary and its vector part real. Its norm form is

$$
N(\tilde{\mathcal{R}}) = \tilde{\mathcal{R}}\bar{\tilde{\mathcal{R}}} = (iR)^2 + |\mathbf{R}|^2 = -R^2 + R^2 = 0 .
$$

The retarded separation is therefore a **null** element of $\mathbb{M}_-$ — a point of the light cone, and hence a zero divisor of $\mathbb{B}$. This is the biquaternion expression of the elementary fact that the separation between an emission event and a later observation event on the light cone is null. The whole radiation problem is built on a zero divisor.

The second is the **coordinate velocity biquaternion**

$$
\tilde{V} = ic\,e_0 + \mathbf{v}(t_r) = \frac{d\tilde{X}_q}{dt}\bigg|_{\text{ret}} \in \mathbb{M}_-,
$$

whose norm form is

$$
N(\tilde{V}) = -c^2 + \mathbf{v}^2 = -c^2(1 - \beta^2) = -\frac{c^2}{\gamma^2},
\qquad \gamma = \frac{1}{\sqrt{1 - \beta^2}} .
$$

Multiplying by $\gamma$ gives the four-velocity $\tilde{U} = \gamma\tilde{V} = \gamma(ic\,e_0 + \mathbf{v})$ of the companion article on $\mathbb{M}_-$, with the standard invariant $N(\tilde{U}) = -c^2$. The retarded separation and the coordinate velocity together determine the potential through a single scalar:

$$
D \equiv R - \mathbf{R}\cdot\boldsymbol{\beta} = R\left(1 - \hat{\mathbf{R}}\cdot\boldsymbol{\beta}\right) = R\kappa, \qquad \kappa \equiv 1 - \hat{\mathbf{R}}\cdot\boldsymbol{\beta}.
$$

The scalar part of the biquaternion product $\tilde{V}\bar{\tilde{\mathcal{R}}}$ computes directly. Using $\bar{\tilde{\mathcal{R}}} = iR\,e_0 - \mathbf{R}$ and the rule that the scalar part of a product of two biquaternions is $A_0B_0 - \mathbf{A}\cdot\mathbf{B}$,

$$
\mathrm{Sc}\!\left(\tilde{V}\bar{\tilde{\mathcal{R}}}\right)
= (ic)(iR) - \mathbf{v}\cdot(-\mathbf{R})
= -cR + \mathbf{v}\cdot\mathbf{R}
= -c\left(R - \frac{\mathbf{R}\cdot\mathbf{v}}{c}\right)
= -cD .
$$

Hence

$$
D = -\frac{1}{c}\,\mathrm{Sc}\!\left(\tilde{V}\bar{\tilde{\mathcal{R}}}\right),
$$

and the Liénard–Wiechert potential takes the compact biquaternion form

$$
\tilde{A} = \frac{\mu q}{4\pi D}\,\tilde{V}
= -\frac{\mu q\,c}{4\pi}\,
\frac{\tilde{V}}{\mathrm{Sc}\!\left(\tilde{V}\bar{\tilde{\mathcal{R}}}\right)} .
$$

This is the central object of the retarded theory. Its scalar part is the scalar potential and its vector part the vector potential:

$$
\tilde{A} = \frac{i\phi}{c}\,e_0 + \mathbf{A},
\qquad
\phi = \frac{q}{4\pi\epsilon D}, \qquad
\mathbf{A} = \frac{\mu q\,\mathbf{v}}{4\pi D} = \frac{\mathbf{v}}{c^2}\,\phi .
$$

The relation $\mathbf{A} = (\mathbf{v}/c^2)\phi$ is the standard one and uses $\epsilon\mu c^2 = 1$. The potential is thus a **single biquaternion built from two elements of $\mathbb{M}_-$**, one null ($\tilde{\mathcal{R}}$) and one timelike ($\tilde{V}$), with the invariant denominator $D$ that measures their biquaternion pairing. In covariant language this is the familiar statement that the four-potential is proportional to the four-velocity divided by the invariant $u\cdot R$; the biquaternion form makes the pairing explicit as the scalar part of a biquaternion product.

## The Field of the Retarded Potential

In the Lorenz gauge the gauge scalar $S = \mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})$ vanishes, so the field strength is obtained from the potential by the biquaternionic differentiation rule of the Maxwell article,

$$
\tilde{F} = \bar{\tilde{\nabla}}\tilde{A} - \mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{A}\right)
= \bar{\tilde{\nabla}}\tilde{A},
$$

with the normalization caveat recorded there: the identification of $\mathbf{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ with the vector part of $\bar{\tilde{\nabla}}\tilde{A}$ fixes the field-strength normalization once and for all, and that is the definition used here. Differentiating the Liénard–Wiechert potential is the standard computation; in the biquaternion formulation it is a single differentiation rather than four, and the result separates into two terms of very different character:

$$
\mathbf{E} = \mathbf{E}_v + \mathbf{E}_a, \qquad
\mathbf{B} = \frac{1}{c}\,\hat{\mathbf{R}}\times\mathbf{E}, \qquad
\mathbf{H} = \frac{\mathbf{B}}{\mu},
$$

with

$$
\mathbf{E}_v = \frac{q}{4\pi\epsilon}\,
\frac{(1-\beta^2)\left(\hat{\mathbf{R}} - \boldsymbol{\beta}\right)}{\kappa^3 R^2},
\qquad
\mathbf{E}_a = \frac{q}{4\pi\epsilon c}\,
\frac{\hat{\mathbf{R}}\times\left[\left(\hat{\mathbf{R}} - \boldsymbol{\beta}\right)\times\dot{\boldsymbol{\beta}}\right]}{\kappa^3 R}.
$$

Here the dot denotes the derivative with respect to the **retarded time**,

$$
\dot{\boldsymbol{\beta}} = \frac{d\boldsymbol{\beta}}{dt_r},
$$

and every source quantity is evaluated at $t_r$. This derivative convention matters, and it is the one for which the formulas above are correct; the alternative of using the derivative with respect to the observer's time $t$ rescales $\dot{\boldsymbol{\beta}}$ by the factor $\kappa = dt/dt_r$ and moves a power of $\kappa$ between the two display formulas. We use the retarded-time derivative throughout.

In biquaternion form the field strength splits in the same way,

$$
\tilde{F} = \tilde{F}_v + \tilde{F}_a,
\qquad
\tilde{F}_v = i\sqrt{\epsilon}\,\mathbf{E}_v - \sqrt{\mu}\,\mathbf{H}_v,
\qquad
\tilde{F}_a = i\sqrt{\epsilon}\,\mathbf{E}_a - \sqrt{\mu}\,\mathbf{H}_a ,
$$

with $\mathbf{H}_{v,a} = \mathbf{B}_{v,a}/\mu$. Both parts are pure-vector biquaternions with vanishing scalar part, like every field strength, and both satisfy $\tilde{F} = \bar{\tilde{\nabla}}\tilde{A}$ collectively. The split is not merely a calculational device: as the next two sections show, $\tilde{F}_v$ and $\tilde{F}_a$ have completely different algebraic types.

## The Velocity Field

The field $\tilde{F}_v$ depends only on the position and velocity of the charge at the retarded time, not on its acceleration. It falls as $1/R^2$, exactly as a static field does, and it is the field that is "carried along" by the charge.

The factor $1-\beta^2 = 1/\gamma^2$ makes $\mathbf{E}_v$ a **contracted** Coulomb field: at $\boldsymbol{\beta} = 0$ it reduces to the ordinary Coulomb field

$$
\mathbf{E}_v \;\xrightarrow{\ \boldsymbol{\beta}=0\ }\; \frac{q}{4\pi\epsilon}\frac{\hat{\mathbf{R}}}{R^2},
$$

in agreement with the static solution of the Maxwell article, and in general the $1/\gamma^2$ factor and the replacement $\hat{\mathbf{R}}\to\hat{\mathbf{R}}-\boldsymbol{\beta}$ are precisely the Lorentz contraction of the Coulomb field in the direction of motion. The magnetic field is the accompanying $\hat{\mathbf{R}}\times\mathbf{E}_v/c$; the whole structure is the boosted static field of the charge.

The velocity field is **not** a radiation field, and in the language of the companion article on invariants it is not null. Because $\mathbf{B}_v = \hat{\mathbf{R}}\times\mathbf{E}_v/c$, the second invariant vanishes identically,

$$
I_{2,v} = \mathbf{E}_v\cdot\mathbf{B}_v = 0,
$$

while the first is positive:

$$
I_{1,v} = \mathbf{E}_v^2 - c^2\mathbf{B}_v^2
= (\hat{\mathbf{R}}\cdot\mathbf{E}_v)^2
= \left(\frac{q}{4\pi\epsilon}\frac{1-\beta^2}{\kappa^2 R^2}\right)^{\!2} > 0 .
$$

The norm form of $\tilde{F}_v$ is therefore nonzero, $N(\tilde{F}_v) = -\epsilon(I_{1,v} + 2ic\,I_{2,v}) = -\epsilon I_{1,v} \neq 0$, and $\tilde{F}_v$ is not a zero divisor. In the classification of the invariants article it is a field of **electric type**: there is a frame (the rest frame of the charge) in which the magnetic field vanishes and the field is purely electric. This is the algebraic statement that the velocity field is bound to the charge: at any event it can be reduced to a purely electric Coulomb field by passing to the instantaneous rest frame of the charge.

Two special cases are worth recording, because they are exactly the content of the two downstream exercises. When the charge moves with constant velocity, $\dot{\boldsymbol{\beta}} = 0$ and $\tilde{F} = \tilde{F}_v$ alone: this is the field of a uniformly moving charge, the subject of *Exercise: The Electromagnetic Field of a Uniformly Moving Charge*. The result is the Heaviside ellipsoid field, obtained here either by specialising the Liénard–Wiechert formulas or, equivalently, by applying the boost rotor $\tilde{\Lambda}$ of the Maxwell article to the Coulomb field of the charge at rest. When the charge accelerates but the observation is made in the far zone, the $1/R^2$ velocity field is negligible compared with the $1/R$ acceleration field, and the radiation field alone survives.

## The Acceleration Field as the Radiation Field

The field $\tilde{F}_a$ is different in every structural respect. It is proportional to the acceleration of the charge, it falls as $1/R$ rather than $1/R^2$, and it is **transverse**:

$$
\hat{\mathbf{R}}\cdot\mathbf{E}_a = 0,
$$

which is immediate from the double cross product in its definition. The magnetic field is perpendicular to both,

$$
\mathbf{B}_a = \frac{1}{c}\,\hat{\mathbf{R}}\times\mathbf{E}_a,
\qquad
|\mathbf{B}_a| = \frac{1}{c}\,|\mathbf{E}_a|,
$$

and it follows that the acceleration field is **null**. Its two Lorentz invariants vanish:

$$
I_{1,a} = \mathbf{E}_a^2 - c^2\mathbf{B}_a^2 = 0,
\qquad
I_{2,a} = \mathbf{E}_a\cdot\mathbf{B}_a = 0 .
$$

In the biquaternion framework this is the statement that the norm form of $\tilde{F}_a$ vanishes:

$$
N(\tilde{F}_a) = \tilde{F}_a\bar{\tilde{F}}_a = -\epsilon\left(I_{1,a} + 2ic\,I_{2,a}\right) = 0 .
$$

A nonzero pure-vector biquaternion with vanishing norm form is a zero divisor and is nilpotent, since for a pure vector $\tilde{F}_a^2 = -\mathbf{F}_a\cdot\mathbf{F}_a = -N(\tilde{F}_a)$. Hence

$$
\boxed{\ \tilde{F}_a^2 = 0\ }
$$

for the acceleration field. The radiation field of an accelerated charge is, algebraically, a **nilpotent element of $\mathbb{B}$**: it is the zero-divisor cone of the algebra, realized pointwise in spacetime. This is the precise sense in which the null-field remark of the invariants article is fulfilled by the radiation of an accelerated charge.

The same fact is visible in the Riemann–Silberstein description. The complex vector of the acceleration field is

$$
\mathbf{V}_a = \mathbf{E}_a + ic\,\mathbf{B}_a = \mathbf{E}_a + i\,\hat{\mathbf{R}}\times\mathbf{E}_a,
$$

and since $\mathbf{E}_a\perp\hat{\mathbf{R}}$,

$$
\mathbf{V}_a\cdot\mathbf{V}_a
= \mathbf{E}_a^2 - \left|\hat{\mathbf{R}}\times\mathbf{E}_a\right|^2 + 2ic\,\mathbf{E}_a\cdot\left(\hat{\mathbf{R}}\times\mathbf{E}_a\right)
= \mathbf{E}_a^2 - \mathbf{E}_a^2 + 0 = 0 .
$$

The Riemann–Silberstein vector of the radiation field is a **null complex vector**. The acceleration field is thus the pointwise realization of every one of the equivalent characterizations of a radiation field collected in the companion article: it is transverse, it is a null field, its norm form vanishes, its field-strength biquaternion is a zero divisor, and its Riemann–Silberstein vector is null.

The energy carried by the acceleration field is correspondingly unambiguous. Since $\mathbf{E}_a\perp\hat{\mathbf{R}}$, the Poynting vector of the acceleration field is purely radial,

$$
\mathbf{S}_a = \mathbf{E}_a\times\mathbf{H}_a = \frac{|\mathbf{E}_a|^2}{\mu c}\,\hat{\mathbf{R}},
$$

so the energy flux through a sphere of radius $R$ is $R^2|\mathbf{E}_a|^2/(\mu c)$ per unit solid angle, independent of $R$: the energy does not fall off, and it escapes to infinity. The velocity field, by contrast, contributes a flux that falls as $1/R^2$ and so adds nothing to the energy radiated to infinity; the energy it carries is the bound field energy that travels with the charge.

## Radiated Power and the Relativistic Larmor Formula

The power crossing a large sphere per unit solid angle, per unit of the observer's time, is the radial Poynting flux times $R^2$:

$$
\frac{dP}{d\Omega} = R^2\,\mathbf{S}_a\cdot\hat{\mathbf{R}}
= \frac{q^2}{16\pi^2\epsilon c}\,
\frac{\left|\hat{\mathbf{R}}\times\left[\left(\hat{\mathbf{R}}-\boldsymbol{\beta}\right)\times\dot{\boldsymbol{\beta}}\right]\right|^2}{\kappa^6},
$$

with the retarded-time derivative convention fixed above. This is the relativistic generalization of the Larmor angular distribution. Its integral over the sphere gives the total radiated power. Because $\boldsymbol{\beta}$, $\dot{\boldsymbol{\beta}}$ and $\kappa$ are functions of the retarded time, the integral is most transparent in the invariant form: writing $\tilde{U} = d\tilde{X}_q/d\tau$ for the four-velocity, the radiated power is

$$
P = \frac{q^2}{6\pi\epsilon c^3}\,N\!\left(\frac{d\tilde{U}}{d\tau}\right)
= \frac{q^2}{6\pi\epsilon c^3}\left(-\frac{du^\mu}{d\tau}\frac{du_\mu}{d\tau}\right),
$$

where in the second expression the index contraction uses the Minkowski metric. This is the **relativistic Larmor formula**, and the biquaternion statement is particularly clean: the radiated power is (up to a constant) the **norm form of the four-acceleration biquaternion**. The norm form is non-negative here because the four-acceleration is spacelike in the $(+,-,-,-)$ convention, and it vanishes precisely for unaccelerated motion, as it must.

For comparison with the standard literature, the same power can be written in terms of the acceleration measured in the observer's time. With $\dot{\boldsymbol{\beta}} = d\boldsymbol{\beta}/dt$ taken this time with respect to $t$ (not $t_r$),

$$
P = \frac{q^2\gamma^6}{6\pi\epsilon c}\left[\dot{\boldsymbol{\beta}}^2 - \left(\boldsymbol{\beta}\times\dot{\boldsymbol{\beta}}\right)^2\right].
$$

Two special cases are standard and useful. For **linear acceleration**, $\dot{\boldsymbol{\beta}}\parallel\boldsymbol{\beta}$ and

$$
P_{\text{lin}} = \frac{q^2\gamma^6\dot{\beta}^2}{6\pi\epsilon c},
$$

the well-known $\gamma^6$ enhancement. For **circular motion**, $\dot{\boldsymbol{\beta}}\perp\boldsymbol{\beta}$ and

$$
P_{\text{circ}} = \frac{q^2\gamma^4\dot{\beta}^2}{6\pi\epsilon c},
$$

a $\gamma^4$ enhancement, because for the same $|\dot{\boldsymbol{\beta}}|$ the radiated power from transverse acceleration is smaller than that from longitudinal acceleration by a factor of $\gamma^2$. Both follow from the invariant expression; no new physics is introduced by the biquaternion formulation, but the way the power is organized — one norm form instead of a three-vector combination — is the characteristic simplification of the algebraic language.

## The Angular Distribution

The angular distribution inherits the same factor. It is convenient to introduce the angle $\theta$ between $\hat{\mathbf{R}}$ and $\boldsymbol{\beta}$, so that

$$
\kappa = 1 - \beta\cos\theta ,
$$

and an azimuthal angle $\phi$ that measures the orientation of $\hat{\mathbf{R}}$ around the direction of $\boldsymbol{\beta}$.

For **linear acceleration**, $\dot{\boldsymbol{\beta}}\parallel\boldsymbol{\beta}$, the vector triple product collapses. Since $\boldsymbol{\beta}\times\dot{\boldsymbol{\beta}} = 0$, one has $\left(\hat{\mathbf{R}}-\boldsymbol{\beta}\right)\times\dot{\boldsymbol{\beta}} = \hat{\mathbf{R}}\times\dot{\boldsymbol{\beta}}$ and therefore

$$
\left|\hat{\mathbf{R}}\times\left[\left(\hat{\mathbf{R}}-\boldsymbol{\beta}\right)\times\dot{\boldsymbol{\beta}}\right]\right|^2
= \dot{\beta}^2\sin^2\theta .
$$

The distribution is

$$
\frac{dP}{d\Omega} = \frac{q^2\dot{\beta}^2\sin^2\theta}{16\pi^2\epsilon c\,\kappa^6},
$$

which is the non-relativistic dipole pattern $\sin^2\theta$ distorted by the forward-beaming factor $\kappa^{-6}$. There is no radiation along the direction of acceleration ($\theta = 0$) or opposite to it ($\theta = \pi$): the angular distribution vanishes on the two directions collinear with the motion. For $\beta\to 0$ the factor $\kappa^{-6}\to 1$ and the total power reduces to the Larmor value $\frac{q^2\dot{\beta}^2}{6\pi\epsilon c}$.

For **circular motion**, $\dot{\boldsymbol{\beta}}\perp\boldsymbol{\beta}$. Choosing $\boldsymbol{\beta}$ along the polar axis and $\dot{\boldsymbol{\beta}}$ in the equatorial plane, the same algebra gives

$$
\left|\hat{\mathbf{R}}\times\left[\left(\hat{\mathbf{R}}-\boldsymbol{\beta}\right)\times\dot{\boldsymbol{\beta}}\right]\right|^2
= \dot{\beta}^2\left[\kappa^2 - \frac{\sin^2\theta\cos^2\phi}{\gamma^2}\right],
$$

and hence

$$
\frac{dP}{d\Omega} = \frac{q^2\dot{\beta}^2}{16\pi^2\epsilon c\,\kappa^6}
\left[\kappa^2 - \frac{\sin^2\theta\cos^2\phi}{\gamma^2}\right].
$$

Like the linear case, the pattern is forward-beamed by the factor $\kappa^{-6}$, so at high speed the emission is concentrated in a narrow cone around the instantaneous velocity. The term in $\gamma^{-2}$ is the correction that distinguishes circular from linear motion: since $\phi$ vanishes for directions lying in the orbital plane (the plane containing $\boldsymbol{\beta}$ and $\dot{\boldsymbol{\beta}}$), that term suppresses radiation emitted within the orbital plane relative to directions perpendicular to it, by a relative amount of order $\gamma^{-2}$ at angles away from the forward direction.

**A remark on the temporal convention.** The distributions above are written per unit of the observer's time $t$ and with $\dot{\boldsymbol{\beta}}$ the retarded-time derivative; hence the power of $\kappa$ in the denominator is six. The same distributions are often written per unit of the retarded time $t_r$; because $dt = \kappa\,dt_r$, that convention multiplies the distributions by $\kappa$ and produces the more familiar-looking denominators $\kappa^5$ (general), $\kappa^5$ (linear), and $\kappa^3$ (circular, after the identity above is used to cancel two powers). No physical quantity depends on the choice; only the bookkeeping of the distribution does. The physical total power is the same in either convention; the two distributions themselves are not, since they differ pointwise by the direction-dependent factor $\kappa$, so the sphere integral must be taken with that factor in the retarded-time form.

**Forward beaming.** The factor $\kappa^{-6}$ is the entire content of relativistic beaming. For $\beta\to1$, $\kappa$ is small only within the forward cone $\theta\lesssim1/\gamma$; outside it, the distribution is suppressed by many powers of $\gamma$. The radiated energy is therefore concentrated in a narrow forward cone of half-angle of order $1/\gamma$, the same cone that controls the relativistic Doppler effect and the synchrotron spectrum. As $\beta\to1$, the angular distribution becomes an increasingly sharp forward spike: the charge radiates almost entirely along its direction of motion.

## Radiation Reaction and the Self-Force

A charge that radiates loses energy and momentum, and the loss must appear as a force acting on the charge itself. In the point-particle idealization the standard result is the **Abraham–Lorentz–Dirac** equation,

$$
m\frac{du^\mu}{d\tau} = f^\mu_{\text{ext}}
+ \frac{q^2}{6\pi\epsilon c^3}\left(\frac{d^2u^\mu}{d\tau^2} + \frac{u^\mu}{c^2}\frac{du^\nu}{d\tau}\frac{du_\nu}{d\tau}\right).
$$

The bracketed term is the radiation-reaction four-force. It can be transcribed into the biquaternion objects of this article without change of content. With $\tilde{U}$ the four-velocity biquaternion, $\dot{\tilde{U}} = d\tilde{U}/d\tau$, and using $N(\dot{\tilde{U}}) = -\frac{du^\mu}{d\tau}\frac{du_\mu}{d\tau}$, the reaction term becomes

$$
\tilde{f}_{\text{rad}}
= \frac{q^2}{6\pi\epsilon c^3}\left(\ddot{\tilde{U}} - \frac{1}{c^2}N\!\left(\dot{\tilde{U}}\right)\tilde{U}\right),
$$

an element of $\mathbb{M}_-$ whose defining property is that it is **orthogonal to the worldline**:

$$
\mathrm{Sc}\!\left(\tilde{f}_{\text{rad}}\bar{\tilde{U}}\right) = 0 .
$$

This orthogonality is the biquaternion form of the statement that the reaction force does no work in the instantaneous rest frame; it follows from $N(\tilde{U}) = -c^2$ being constant, which gives $\mathrm{Sc}(\ddot{\tilde{U}}\bar{\tilde{U}}) = -N(\dot{\tilde{U}})$.

Two caveats should be stated plainly. First, the reformulation does not resolve the well-known pathologies of the equation — the runaway solutions and the pre-acceleration that follow from treating the self-force as a local differential expression. Second, the equation above is a transcription of the standard result into the biquaternion notation; it is not a derivation of the self-force from the biquaternion framework, and the point-charge self-energy divergence is untouched by the change of language. The radiation-reaction problem is thus **represented** cleanly in the framework, but it is not solved by it.

## Relation to the Two Exercises

The construction above is the declared foundation for two downstream exercises, and it is worth recording explicitly which parts each one uses.

*Exercise: The Electromagnetic Field of a Uniformly Moving Charge* is the case of vanishing acceleration. Setting $\dot{\boldsymbol{\beta}} = 0$ in the field formulas of the section "The Field of the Retarded Potential" leaves $\tilde{F} = \tilde{F}_v$; the exercise is then the evaluation of $\mathbf{E}_v = \frac{q}{4\pi\epsilon}\frac{(1-\beta^2)(\hat{\mathbf{R}}-\boldsymbol{\beta})}{\kappa^3R^2}$ and $\mathbf{B}_v = \hat{\mathbf{R}}\times\mathbf{E}_v/c$, and the identification of the result as the Heaviside ellipsoid field, equivalently as the boost of the Coulomb field. The pieces needed are the Liénard–Wiechert potential of "The Retarded Null Biquaternion" and the velocity field of "The Velocity Field".

*Exercise: The Electromagnetic Field of a Moving Charge* is the general case. It uses the full Liénard–Wiechert potential, the field split $\tilde{F} = \tilde{F}_v + \tilde{F}_a$ of "The Field of the Retarded Potential", and the two component expressions of "The Velocity Field" and "The Acceleration Field as the Radiation Field". The exercise is then the evaluation of both parts for a specified worldline, and the demonstration that the far-zone field is the radiation field alone.

## Summary

The radiation from an accelerated charge is treated in the biquaternion framework by specializing the retarded solution of the biquaternionic Maxwell equation to a point source. The retarded convolution localizes on the worldline and produces the Liénard–Wiechert potential in the compact form

$$
\tilde{A} = \frac{\mu q}{4\pi D}\,\tilde{V},
\qquad
\tilde{V} = ic\,e_0 + \mathbf{v}(t_r),
\qquad
D = R - \mathbf{R}\cdot\boldsymbol{\beta}
= -\frac{1}{c}\,\mathrm{Sc}\!\left(\tilde{V}\bar{\tilde{\mathcal{R}}}\right),
$$

built from the null retarded separation $\tilde{\mathcal{R}} = iR\,e_0 + \mathbf{R}$ and the timelike coordinate velocity $\tilde{V}$, both in $\mathbb{M}_-$.

The field strength splits into a velocity part and an acceleration part, $\tilde{F} = \tilde{F}_v + \tilde{F}_a$. The velocity field $\tilde{F}_v$ falls as $1/R^2$, has vanishing second invariant and positive first invariant, $I_{1,v} = (\hat{\mathbf{R}}\cdot\mathbf{E}_v)^2 > 0$, and is of electric type; it is the field of a uniformly moving charge and is not radiation. The acceleration field $\tilde{F}_a$ falls as $1/R$, is transverse, and is **null**:

$$
I_{1,a} = I_{2,a} = 0,
\qquad
N(\tilde{F}_a) = 0,
\qquad
\tilde{F}_a^2 = 0,
$$

so that the radiation field is a **zero divisor and a nilpotent element** of $\mathbb{B}$. This is the concrete realization of the null-field characterization anticipated in the companion article on the field-strength invariants.

The radiated power is the norm form of the four-acceleration biquaternion,

$$
P = \frac{q^2}{6\pi\epsilon c^3}\,N\!\left(\frac{d\tilde{U}}{d\tau}\right),
$$

the relativistic Larmor formula, with the standard $\gamma^6$ (linear) and $\gamma^4$ (circular) enhancements as special cases. The angular distribution carries the forward-beaming factor $\kappa^{-6}$, which concentrates the radiation into a cone of half-angle of order $1/\gamma$ at high speed. The radiation-reaction force can be transcribed as an element of $\mathbb{M}_-$ orthogonal to the worldline, though the standard pathologies of the point-charge self-force remain.

The construction is explicit enough that the two downstream exercises are direct applications: R4 is the case $\dot{\boldsymbol{\beta}} = 0$, and E1 is the general case.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) subspaces |
| $\mathbb{H}_{\mathbb{B}}, \mathbb{C}_{\mathbb{B}}$ | Real-quaternion and scalar subspaces |
| $\tilde{\nabla}, \bar{\tilde{\nabla}}, \Box = \tilde{\nabla}\bar{\tilde{\nabla}}$ | Biquaternionic gradient, conjugate, d'Alembertian |
| $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ | Field-strength biquaternion |
| $\tilde{F}_v, \tilde{F}_a$ | Velocity part and acceleration (radiation) part of the field |
| $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$ | Potential biquaternion (Liénard–Wiechert) |
| $\tilde{R}' = ic\rho + \mathbf{J}$ | Source biquaternion of the potential wave equation |
| $t_r$ | Retarded time, $t_r = t - |\mathbf{x}-\mathbf{r}_q(t_r)|/c$ |
| $\mathbf{R} = \mathbf{x}-\mathbf{r}_q(t_r)$, $R = |\mathbf{R}|$ | Retarded separation |
| $\hat{\mathbf{R}} = \mathbf{R}/R$ | Unit retarded direction |
| $\tilde{\mathcal{R}} = iR\,e_0 + \mathbf{R}$ | Retarded null biquaternion, $N(\tilde{\mathcal{R}})=0$ |
| $\tilde{V} = ic\,e_0 + \mathbf{v}(t_r)$ | Coordinate velocity biquaternion |
| $\tilde{U} = \gamma\tilde{V}$ | Four-velocity biquaternion |
| $\boldsymbol{\beta} = \mathbf{v}(t_r)/c$, $\beta = |\boldsymbol{\beta}|$ | Dimensionless retarded velocity |
| $\gamma = (1-\beta^2)^{-1/2}$ | Lorentz factor |
| $\kappa = 1-\hat{\mathbf{R}}\cdot\boldsymbol{\beta}$ | Retardation factor |
| $D = R-\mathbf{R}\cdot\boldsymbol{\beta} = R\kappa$ | Retarded distance, $D = -\frac{1}{c}\mathrm{Sc}(\tilde{V}\bar{\tilde{\mathcal{R}}})$ |
| $\dot{\boldsymbol{\beta}} = d\boldsymbol{\beta}/dt_r$ | Retarded-time acceleration (dot = $d/dt_r$ in the field formulas) |
| $\mathbf{E}_v, \mathbf{B}_v, \mathbf{H}_v$ | Velocity-part fields |
| $\mathbf{E}_a, \mathbf{B}_a, \mathbf{H}_a$ | Acceleration-part (radiation) fields |
| $I_1 = \mathbf{E}^2 - c^2\mathbf{B}^2$, $I_2 = \mathbf{E}\cdot\mathbf{B}$ | Field invariants |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $dP/d\Omega$ | Power per unit solid angle (per observer time) |
| $\theta, \phi$ | Polar angle from $\boldsymbol{\beta}$, azimuthal angle |
| $\epsilon, \mu$, $c = 1/\sqrt{\epsilon\mu}$ | Medium permittivity, permeability, speed of light |
| $q, m$ | Charge and mass of the radiating particle |

## Further Reading

- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the Liénard–Wiechert potentials, the velocity–acceleration split, and the relativistic Larmor formula.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the Liénard–Wiechert fields, the angular distributions, and the radiation-reaction equation.
- D. J. Griffiths, *Introduction to Electrodynamics* (Cambridge, 2017), for a careful elementary derivation of the Liénard–Wiechert potentials and fields.
- F. Rohrlich, *Classical Charged Particles* (World Scientific, 2007), for the Abraham–Lorentz–Dirac equation and the consistency of radiation reaction with energy conservation.
- P. A. M. Dirac, "Classical Theory of Radiating Electrons", *Proceedings of the Royal Society A* 167 (1938) 148–169, for the original derivation of the radiation-reaction force.
- D. Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the spacetime-algebra treatment of the electromagnetic field and its sources.
- C. Doran and A. Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra derivation of radiation from moving charges.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic formulation of the field equations and their retarded solutions.
- A. Waser, "Application of Bi-Quaternions in Physics" (2000, updated 2007), for biquaternionic treatments of the electromagnetic field and its energy–momentum.
- I. Białynicki-Birula and Z. Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* 46 (2013) 053001, for the null complex-vector characterization of radiation.
