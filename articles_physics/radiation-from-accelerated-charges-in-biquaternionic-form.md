# __Radiation from Accelerated Charges in Biquaternionic Form__

## Introduction

Radiation is the part of an electromagnetic field that does not remain attached to its source. A charge at rest, or in uniform motion, is surrounded by a field that is carried along with it; only the field of an accelerating charge has a piece that escapes to infinity at the speed of light. This article develops that distinction in the biquaternion framework, starting from the retarded solution of the biquaternionic Maxwell equation established in the companion article *Maxwell's Equations in the Biquaternionic Formulation*.

The biquaternion formulation is a natural language for radiation, for a reason that the companion article *The Field-Strength Biquaternion and Its Invariants* already anticipated. There the field-strength biquaternion

$$
\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H
$$

was shown to have a biquaternion norm $\langle\tilde{F}\rangle_{\natural} = \tilde{F}\tilde{F}^{\natural}$ whose vanishing is exactly the condition that the field be null: $\vec E\perp\vec B$ and $|\vec E| = c|\vec B|$ pointwise. A null field strength is a **zero divisor** of the algebra $\mathbb{B}$. That null condition is the algebraic signature of a radiation field. The main result of this article is that it is realized, pointwise, by the acceleration part of the Liénard–Wiechert field: the radiation field is precisely the part of $\tilde{F}$ that squares to zero.

The conventions are those of the read-list articles throughout, and nothing in them is changed here. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_k^2 = -e_t$, and scalar imaginary $i$ commuting with the quaternion units. The subspaces are $\mathbb{M}_-$ (anti-Hermitian, imaginary scalar and real vector, the material sector), $\mathbb{M}_+$ (Hermitian, real scalar and imaginary vector, the informational sector), $\mathbb{H}_{\mathbb{B}}$ (real quaternions), and $\mathbb{C}_{\mathbb{B}}$ (scalars). The biquaternionic gradient is $\tilde{\nabla} = e_t\partial/\partial Q_t + \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z$, with $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial^2/\partial Q_t^2 + \Delta$, and the symbol $c = 1/\sqrt{\epsilon\mu}$ always denotes the speed of light in the medium, reducing to $c_0$ in vacuum. The charge whose field is being computed is written $ϙ$, and its velocity is written $\vec v$ (the symbol $v$ is reserved for particle velocities, as in the companion articles).

The article is organized as follows. The first section recalls the retarded solution of the Maxwell article and specializes it to a point charge. The second introduces the retarded null biquaternion and writes the Liénard–Wiechert potentials in biquaternion form, and adds the source's spinor square root and invariant retarded distance. The third computes the field and splits it into a velocity part and an acceleration part. The fourth identifies the acceleration part as the radiation field, and the fifth and sixth extract the radiated power and the angular distribution. A short section treats the radiation-reaction problem, and a closing section records how the two downstream exercises are applications of the construction.

Two later exercises use this article as their declared foundation: *Exercise: The Electromagnetic Field of a Moving Charge* and *Exercise: The Electromagnetic Field of a Uniformly Moving Charge*. The construction below is worked out explicitly enough that both are applications of it, R4 being the case of vanishing acceleration and E1 the general case.

## The Retarded Solution for a Point Source

The Maxwell article establishes that in the Lorenz gauge the potential biquaternion satisfies the biquaternionic wave equation

$$
\Box \tilde{A} = -\mu\,\tilde J, \qquad \tilde J = ic\rho\,e_t + \vec J,
$$

and that the physically correct solution is the **retarded** one, built by convolution over the past light cone. The scalar Green's function of this second-order equation, distinct from the scalar part of that article's biquaternion-valued retarded Green's function (a first-order kernel of the opposite sign), is the familiar retarded kernel of the d'Alembertian,

$$
G_{\Box}(\tilde{Q}) = \frac{1}{4\pi R}\,\delta\!\left(t - \frac{R}{c}\right), \qquad R = |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|,
$$

so that

$$
\tilde{A}(\tilde{Q}) = \mu\int G_{\Box}(\tilde{Q} - \tilde R_2)\,\tilde J(\tilde R_2)\,d^4R_2 .
$$

We do not re-derive this structure; we only specialize it. For a point charge $ϙ$ on a worldline $\vec r_q(t)$, the source is

$$
\rho(\vec y, s) = ϙ\,\delta^3\!\left(\vec y - \vec r_q(s)\right), \qquad
\vec J(\vec y, s) = ϙ\,\vec v(s)\,\delta^3\!\left(\vec y - \vec r_q(s)\right),
$$

and therefore

$$
\tilde J(\tilde R_2) = ϙ\left(ic\,e_t + \vec v(s)\right)\delta^3\!\left(\vec y - \vec r_q(s)\right).
$$

Substituting this into the retarded convolution and integrating first over $\vec y$ localizes the source at $\vec y = \vec r_q(s)$; the remaining integral over $s$ localizes at the **retarded time** $t_r$ defined implicitly by

$$
t_r = t - \frac{\left|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z - \vec r_q(t_r)\right|}{c}.
$$

Writing $h(s) = s + |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z - \vec r_q(s)|/c - t$, one has $\frac{dh}{ds}(s) = 1 - \vec u_R\cdot\vec\beta$, so the delta function contributes the Jacobian

$$
\delta\!\left(t - \frac{|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z - \vec r_q(s)|}{c} - s\right)
= \frac{1}{1 - \vec u_R\cdot\vec\beta}\,\delta(s - t_r).
$$

Collecting the pieces, the retarded solution is the **Liénard–Wiechert potential**

$$
\tilde{A} = \frac{\mu ϙ}{4\pi}\,\frac{ic\,e_t + \vec v(t_r)}{R - \vec R\cdot\vec\beta},
$$

where from here on all source quantities are understood to be evaluated at the retarded time, and

$$
\vec R = x\,\vec e_x+y\,\vec e_y+z\,\vec e_z - \vec r_q(t_r), \qquad R = |\vec R|, \qquad
\vec u_R = \frac{\vec R}{R}, \qquad \vec\beta = \frac{\vec v(t_r)}{c}.
$$

The single retardation of a point charge is thus the only place where the light-cone structure of the theory enters the radiation problem; everything that follows is algebra.

## The Retarded Null Biquaternion

It is convenient to name the two biquaternions that appear in the Liénard–Wiechert potential. The first is the **retarded separation**, the biquaternion

$$
iR\,e_t + \vec R,
$$

which is an element of the material subspace $\mathbb{M}_-$: its scalar part is imaginary and its vector part real. Its biquaternion norm is

$$
\langle iR\,e_t+\vec R\rangle_{\natural} = (iR\,e_t+\vec R)(iR\,e_t+\vec R)^{\natural} = (iR)^2 + |\vec R|^2 = -R^2 + R^2 = 0 .
$$

The retarded separation is therefore a **null** element of $\mathbb{M}_-$ — a point of the light cone, and hence a zero divisor of $\mathbb{B}$. This is the biquaternion expression of the elementary fact that the separation between an emission event and a later observation event on the light cone is null. The whole radiation problem is built on a zero divisor.

The second is the **four-velocity biquaternion**, written in coordinate form as the coordinate velocity divided by $\gamma$

$$
\tilde{V}/\gamma = ic\,e_t + \vec v(t_r) = \frac{d\tilde{Q}_q}{dt}\bigg|_{\text{ret}} \in \mathbb{M}_- ,
\qquad
\tilde{V} = \gamma\left(ic\,e_t + \vec v(t_r)\right) = \frac{d\tilde{Q}_q}{d\tau}\bigg|_{\text{ret}} \in \mathbb{M}_- ,
$$

with biquaternion norms

$$
\langle\tilde{V}/\gamma\rangle_{\natural} = -c^2 + \vec v^2 = -c^2(1 - \beta^2) = -\frac{c^2}{\gamma^2},
\qquad
\langle\tilde{V}\rangle_{\natural} = \gamma^2\,\langle\tilde{V}/\gamma\rangle_{\natural} = -c^2 ,
\qquad \gamma = \frac{1}{\sqrt{1 - \beta^2}} .
$$

The four-velocity $\tilde{V}$ carries the standard invariant $\langle\tilde{V}\rangle_{\natural} = -c^2$ of the companion article on $\mathbb{M}_-$. The retarded separation and the four-velocity together determine the potential through a single scalar:

$$
D \equiv R - \vec R\cdot\vec\beta = R\left(1 - \vec u_R\cdot\vec\beta\right) = R\kappa, \qquad \kappa \equiv 1 - \vec u_R\cdot\vec\beta.
$$

The scalar part of the biquaternion product $(\tilde{V}/\gamma)(iR\,e_t+\vec R)^{\natural}$ computes directly. Using $(iR\,e_t+\vec R)^{\natural} = iR\,e_t - \vec R$ and the rule that the scalar part of a product of two biquaternions is $A_0B_0 - \vec A\cdot\vec B$,

$$
\mathrm{Sc}\!\left((\tilde{V}/\gamma)(iR\,e_t+\vec R)^{\natural}\right)
= (ic)(iR) - \vec v\cdot(-\vec R)
= -cR + \vec v\cdot\vec R
= -c\left(R - \frac{\vec R\cdot\vec v}{c}\right)
= -cD .
$$

Hence

$$
D = -\frac{1}{c}\,\mathrm{Sc}\!\left((\tilde{V}/\gamma)(iR\,e_t+\vec R)^{\natural}\right),
$$

and the Liénard–Wiechert potential takes the compact biquaternion form

$$
\tilde{A} = \frac{\mu ϙ}{4\pi D}\,\tilde{V}/\gamma
= -\frac{\mu ϙ\,c}{4\pi}\,
\frac{\tilde{V}/\gamma}{\mathrm{Sc}\!\left((\tilde{V}/\gamma)(iR\,e_t+\vec R)^{\natural}\right)} .
$$

This is the central object of the retarded theory. Its scalar part is the scalar potential and its vector part the vector potential:

$$
\tilde{A} = \frac{i\phi}{c}\,e_t + \vec A,
\qquad
\phi = \frac{ϙ}{4\pi\epsilon D}, \qquad
\vec A = \frac{\mu ϙ\,\vec v}{4\pi D} = \frac{\vec v}{c^2}\,\phi .
$$

The relation $\vec A = (\vec v/c^2)\phi$ is the standard one and uses $\epsilon\mu c^2 = 1$. The potential is thus a **single biquaternion built from two elements of $\mathbb{M}_-$**, one null ($iR\,e_t+\vec R$) and one timelike ($\tilde{V}/\gamma$), with the invariant denominator $D$ that measures their biquaternion pairing. In covariant language this is the familiar statement that the four-potential is proportional to the four-velocity divided by the invariant $\tilde V\cdot R$; the biquaternion form makes the pairing explicit as the scalar part of a biquaternion product.

## The Spinor Square Root and the Invariant Retarded Distance

Every zero divisor factorises, and the source's spinor treatment of the retarded field is such a factorisation, written in objects that this article has already defined. Three of them are the source's, and it is worth naming each once against the conventions here.

**The invariant retarded distance.** The source's scalar is

$$
\xi = -i\,\mathrm{Sc}\!\left(\frac{\tilde{V}}{ic}\,(iR\,e_t+\vec R)^{\natural}\right),
\qquad
\frac{\tilde{V}}{ic} = \gamma\left(e_t - i\vec\beta\right),
$$

where $\tilde{V}/(ic)$ is the four-velocity reduced to unit biquaternion norm. In the $ict$ convention, with $(iR\,e_t+\vec R)^{\natural} = iR\,e_t - \vec R$ and the scalar part of a product equal to $A_0B_0 - \vec A\cdot\vec B$,

$$
\mathrm{Sc}\!\left(\frac{\tilde{V}}{ic}\,(iR\,e_t+\vec R)^{\natural}\right)
= \gamma\,(iR) - (-i\gamma\vec\beta)\cdot(-\vec R)
= i\gamma\left(R - \vec R\cdot\vec\beta\right)
= i\gamma D ,
$$

so that

$$
\xi = \gamma D = \gamma R\left(1 - \vec u_R\cdot\vec\beta\right).
$$

The source's retarded distance is therefore the article's denominator $D$ multiplied by $\gamma$. Because $\tilde{V} = \gamma\,\tilde{V}/\gamma$, the Liénard–Wiechert potential of the previous section collapses to

$$
\tilde{A} = \frac{\mu ϙ}{4\pi D}\,\tilde{V}/\gamma = \frac{\mu ϙ}{4\pi\xi}\,\tilde{V},
$$

the four-velocity over the invariant retarded distance, with the factor of $\gamma$ moved rather than removed.

**The spinor square root.** The four-velocity is the square of a bireal spinor,

$$
\tilde{V} = ic\,B^2,
\qquad
B = \cosh\tfrac{y}{2}\,e_t - i\sinh\tfrac{y}{2}\,\vec u_\beta,
\qquad
B^+ = B,
$$

with rapidity $y$ fixed by $\cosh y = \gamma$ and $\vec u_\beta = \vec\beta/|\vec\beta|$. The spinor is bireal — fixed by Hermitian conjugation — and that is exactly what makes $B^2 = BB^+$: the square root of the four-velocity and the spinor decomposition of the four-velocity are the same operation. In these variables the potential reads

$$
\tilde{A} = \frac{i\mu ϙ c}{4\pi\xi}\,B^2 ,
$$

one spinor square and two invariants.

**The retarded separation as a spinor product.** With the primitive idempotent

$$
\sigma = \tfrac12\left(e_t + i\,\vec u\right),
\qquad
\sigma^2 = \sigma, \qquad \langle \sigma\rangle_{\natural} = 0,
$$

whose unit vector $\vec u$ is the line of sight in the charge's rest frame, taken from the observation point towards the charge,

$$
iR\,e_t+\vec R = 2i\xi\,B\,\sigma\,B^+ .
$$

This is the source's displayed relation for its separation $X - Z$. The product exhibits the two facts established separately in the retarded-null section: the separation is a zero divisor because it is built from the idempotent $\sigma$ and the invertible spinor $B$, and its magnitude is the invariant retarded distance $\xi$, not the coordinate distance $R$. The source takes its direction vector $\vec\nu$ from the charge to the observation point, which reverses the overall sign of the relation as printed; the corpus fixes the sign by the direction of $\vec u$ stated above, so that the coefficient of the idempotent is $+2i\xi$.

**The four-acceleration.** In the same variables the four-acceleration of the charge is the boost conjugate of its value in the instantaneous rest frame,

$$
\frac{d\tilde{V}}{d\tau} = B\,\vec a\,B^+,
\qquad
\vec a = a_1 \vec e_x + a_2 \vec e_y + a_3 \vec e_z,
$$

a real vector, and it is orthogonal to the four-velocity,

$$
\mathrm{Sc}\!\left(\frac{d\tilde{V}}{d\tau}\,\tilde{V}^{\natural}\right) = 0 ,
$$

which is the biquaternion statement that a four-acceleration is orthogonal to its worldline. The same conjugation makes the orthogonality immediate and fixes $\vec a$ as the acceleration in the instantaneous rest frame: at $\vec\beta = 0$ the spinor is the identity and the relation reads $d\tilde{V}/d\tau = \vec a$. The source prints its own acceleration relation with a minus, $d^2Z/dt_r^2 = -B\vec aB^+$; the minus is carried by its normalization of the position variable, since the corpus four-velocity and the source's differ by the constant factor $ic$, and the sign above is the one that reduces to the rest-frame acceleration at vanishing velocity.

These are the source's formulas, transcribed into the conventions of this article and checked component by component; no statement of the earlier sections changes. The spinor square root introduced here is the same decomposition that underlies Weiss's independent route to the Lorentz–Dirac equation in the radiation-reaction section below.

## The Field of the Retarded Potential

In the Lorenz gauge the gauge scalar $S = \mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$ vanishes, so the field strength is obtained from the potential by the biquaternionic differentiation rule of the Maxwell article,

$$
\tilde{F} = \tilde{\nabla}^{\natural}\tilde{A} - \mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{A}\right)
= \tilde{\nabla}^{\natural}\tilde{A},
$$

with the normalization caveat recorded there: the identification of $\vec F = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ with the vector part of $\tilde{\nabla}^{\natural}\tilde{A}$ fixes the field-strength normalization once and for all, and that is the definition used here. Differentiating the Liénard–Wiechert potential is the standard computation; in the biquaternion formulation it is a single differentiation rather than four, and the result separates into two terms of very different character:

$$
\vec E = \vec E_v + \vec E_a, \qquad
\vec B = \frac{1}{c}\,\vec u_R\times\vec E, \qquad
\vec H = \frac{\vec B}{\mu},
$$

with

$$
\vec E_v = \frac{ϙ}{4\pi\epsilon}\,
\frac{(1-\beta^2)\left(\vec u_R - \vec\beta\right)}{\kappa^3 R^2},
\qquad
\vec E_a = \frac{ϙ}{4\pi\epsilon c}\,
\frac{\vec u_R\times\left[\left(\vec u_R - \vec\beta\right)\times\,d\vec\beta/dt_r\right]}{\kappa^3 R}.
$$

Here the derivative is with respect to the **retarded time**, written $d/dt_r$, and every source quantity is evaluated at $t_r$. This derivative convention matters, and it is the one for which the formulas above are correct; the alternative of using the derivative with respect to the observer's time $t$ rescales $d\vec\beta/dt_r$ by the factor $\kappa = dt/dt_r$ and moves a power of $\kappa$ between the two display formulas. We use the retarded-time derivative throughout.

In biquaternion form the field strength splits in the same way,

$$
\tilde{F} = \tilde{F}_v + \tilde{F}_a,
\qquad
\tilde{F}_v = i\sqrt{\epsilon}\,\vec E_v - \sqrt{\mu}\,\vec H_v,
\qquad
\tilde{F}_a = i\sqrt{\epsilon}\,\vec E_a - \sqrt{\mu}\,\vec H_a ,
$$

with $\vec H_{v,a} = \vec B_{v,a}/\mu$. Both parts are pure-vector biquaternions with vanishing scalar part, like every field strength, and both satisfy $\tilde{F} = \tilde{\nabla}^{\natural}\tilde{A}$ collectively. The split is not merely a calculational device: as the next two sections show, $\tilde{F}_v$ and $\tilde{F}_a$ have completely different algebraic types.

## The Velocity Field

The field $\tilde{F}_v$ depends only on the position and velocity of the charge at the retarded time, not on its acceleration. It falls as $1/R^2$, exactly as a static field does, and it is the field that is "carried along" by the charge.

The factor $1-\beta^2 = 1/\gamma^2$ makes $\vec E_v$ a **contracted** Coulomb field: at $\vec\beta = 0$ it reduces to the ordinary Coulomb field

$$
\vec E_v \;\xrightarrow{\ \vec\beta=0\ }\; \frac{ϙ}{4\pi\epsilon}\frac{\vec u_R}{R^2},
$$

in agreement with the static solution of the Maxwell article, and in general the $1/\gamma^2$ factor and the replacement $\vec u_R\to\vec u_R-\vec\beta$ are precisely the Lorentz contraction of the Coulomb field in the direction of motion. The magnetic field is the accompanying $\vec u_R\times\vec E_v/c$; the whole structure is the boosted static field of the charge.

The velocity field is **not** a radiation field, and in the language of the companion article on invariants it is not null. Because $\vec B_v = \vec u_R\times\vec E_v/c$, the second invariant vanishes identically,

$$
I_{2,v} = \vec E_v\cdot\vec B_v = 0,
$$

while the first is positive:

$$
I_{1,v} = \vec E_v^2 - c^2\vec B_v^2
= (\vec u_R\cdot\vec E_v)^2
= \left(\frac{ϙ}{4\pi\epsilon}\frac{1-\beta^2}{\kappa^2 R^2}\right)^{\!2} > 0 .
$$

The biquaternion norm of $\tilde{F}_v$ is therefore nonzero, $\langle\tilde{F}_v\rangle_{\natural} = -\epsilon(I_{1,v} + 2ic\,I_{2,v}) = -\epsilon I_{1,v} \neq 0$, and $\tilde{F}_v$ is not a zero divisor. In the classification of the invariants article it is a field of **electric type**: there is a frame (the rest frame of the charge) in which the magnetic field vanishes and the field is purely electric. This is the algebraic statement that the velocity field is bound to the charge: at any event it can be reduced to a purely electric Coulomb field by passing to the instantaneous rest frame of the charge.

Two special cases are worth recording, because they are exactly the content of the two downstream exercises. When the charge moves with constant velocity, $d\vec\beta/dt_r = 0$ and $\tilde{F} = \tilde{F}_v$ alone: this is the field of a uniformly moving charge, the subject of *Exercise: The Electromagnetic Field of a Uniformly Moving Charge*. The result is the Heaviside ellipsoid field, obtained here either by specialising the Liénard–Wiechert formulas or, equivalently, by applying the boost rotor $\tilde U$ of the Maxwell article to the Coulomb field of the charge at rest. When the charge accelerates but the observation is made in the far zone, the $1/R^2$ velocity field is negligible compared with the $1/R$ acceleration field, and the radiation field alone survives.

## The Acceleration Field as the Radiation Field

The field $\tilde{F}_a$ is different in every structural respect. It is proportional to the acceleration of the charge, it falls as $1/R$ rather than $1/R^2$, and it is **transverse**:

$$
\vec u_R\cdot\vec E_a = 0,
$$

which is immediate from the double cross product in its definition. The magnetic field is perpendicular to both,

$$
\vec B_a = \frac{1}{c}\,\vec u_R\times\vec E_a,
\qquad
|\vec B_a| = \frac{1}{c}\,|\vec E_a|,
$$

and it follows that the acceleration field is **null**. Its two Lorentz invariants vanish:

$$
I_{1,a} = \vec E_a^2 - c^2\vec B_a^2 = 0,
\qquad
I_{2,a} = \vec E_a\cdot\vec B_a = 0 .
$$

In the biquaternion framework this is the statement that the biquaternion norm of $\tilde{F}_a$ vanishes:

$$
\langle\tilde{F}_a\rangle_{\natural} = \tilde{F}_a\tilde{F}^{\natural}_a = -\epsilon\left(I_{1,a} + 2ic\,I_{2,a}\right) = 0 .
$$

A nonzero pure-vector biquaternion with vanishing biquaternion norm is a zero divisor and is nilpotent, since for a pure vector $\tilde{F}_a^2 = -\vec F_a\cdot\vec F_a = -\langle\tilde{F}_a\rangle_{\natural}$. Hence

$$
\boxed{\ \tilde{F}_a^2 = 0\ }
$$

for the acceleration field. The radiation field of an accelerated charge is, algebraically, a **nilpotent element of $\mathbb{B}$**: it is the zero-divisor cone of the algebra, realized pointwise in spacetime. This is the precise sense in which the null-field remark of the invariants article is fulfilled by the radiation of an accelerated charge.

The same fact is visible in the Riemann–Silberstein description. The complex vector of the acceleration field is

$$
\vec N_a = \vec E_a + ic\,\vec B_a = \vec E_a + i\,\vec u_R\times\vec E_a,
$$

and since $\vec E_a\perp\vec u_R$,

$$
\vec N_a\cdot\vec N_a
= \vec E_a^2 - \left|\vec u_R\times\vec E_a\right|^2 + 2ic\,\vec E_a\cdot\left(\vec u_R\times\vec E_a\right)
= \vec E_a^2 - \vec E_a^2 + 0 = 0 .
$$

The Riemann–Silberstein vector of the radiation field is a **null complex vector**. The acceleration field is thus the pointwise realization of every one of the equivalent characterizations of a radiation field collected in the companion article: it is transverse, it is a null field, its biquaternion norm vanishes, its field-strength biquaternion is a zero divisor, and its Riemann–Silberstein vector is null.

The energy carried by the acceleration field is correspondingly unambiguous. Since $\vec E_a\perp\vec u_R$, the Poynting vector of the acceleration field is purely radial,

$$
\vec S_a = \vec E_a\times\vec H_a = \frac{|\vec E_a|^2}{\mu c}\,\vec u_R,
$$

so the energy flux through a sphere of radius $R$ is $R^2|\vec E_a|^2/(\mu c)$ per unit solid angle, independent of $R$: the energy does not fall off, and it escapes to infinity. The velocity field, by contrast, contributes a flux that falls as $1/R^2$ and so adds nothing to the energy radiated to infinity; the energy it carries is the bound field energy that travels with the charge.

## Radiated Power and the Relativistic Larmor Formula

The power crossing a large sphere per unit solid angle, per unit of the observer's time, is the radial Poynting flux times $R^2$:

$$
\frac{dP}{d\Omega} = R^2\,\vec S_a\cdot\vec u_R
= \frac{ϙ^2}{16\pi^2\epsilon c}\,
\frac{\left|\vec u_R\times\left[\left(\vec u_R-\vec\beta\right)\times\,d\vec\beta/dt_r\right]\right|^2}{\kappa^6},
$$

with the retarded-time derivative convention fixed above. This is the relativistic generalization of the Larmor angular distribution. Its integral over the sphere gives the total radiated power. Because $\vec\beta$, $d\vec\beta/dt_r$ and $\kappa$ are functions of the retarded time, the integral is most transparent in the invariant form: writing $\tilde{V} = d\tilde{Q}_q/d\tau$ for the four-velocity, the radiated power is

$$
P = \frac{ϙ^2}{6\pi\epsilon c^3}\,N\!\left(\frac{d\tilde{V}}{d\tau}\right)
= \frac{ϙ^2}{6\pi\epsilon c^3}\left(-\frac{du^\mu}{d\tau}\frac{du_\mu}{d\tau}\right),
$$

where in the second expression the index contraction uses the Minkowski metric. This is the **relativistic Larmor formula**, and the biquaternion statement is particularly clean: the radiated power is (up to a constant) the **biquaternion norm of the four-acceleration biquaternion**. The biquaternion norm is non-negative here because the four-acceleration is spacelike in the $(+,-,-,-)$ convention, and it vanishes precisely for unaccelerated motion, as it must.

For comparison with the standard literature, the same power can be written in terms of the acceleration measured in the observer's time. With the derivative taken this time with respect to $t$ (not $t_r$),

$$
P = \frac{ϙ^2\gamma^6}{6\pi\epsilon c}\left[\left(d\vec\beta/dt\right)^{2} - \left(\vec\beta\times\,d\vec\beta/dt\right)^2\right].
$$

Two special cases are standard and useful. For **linear acceleration**, $d\vec\beta/dt_r\parallel\vec\beta$ and

$$
P_{\text{lin}} = \frac{ϙ^2\gamma^6\left(d\beta/dt_r\right)^{2}}{6\pi\epsilon c},
$$

the well-known $\gamma^6$ enhancement. For **circular motion**, $d\vec\beta/dt_r\perp\vec\beta$ and

$$
P_{\text{circ}} = \frac{ϙ^2\gamma^4\left(d\beta/dt_r\right)^{2}}{6\pi\epsilon c},
$$

a $\gamma^4$ enhancement, because for the same $|d\vec\beta/dt_r|$ the radiated power from transverse acceleration is smaller than that from longitudinal acceleration by a factor of $\gamma^2$. Both follow from the invariant expression; no new physics is introduced by the biquaternion formulation, but the way the power is organized — one biquaternion norm instead of a three-vector combination — is the characteristic simplification of the algebraic language.

## The Angular Distribution

The angular distribution inherits the same factor. It is convenient to introduce the angle $\theta$ between $\vec u_R$ and $\vec\beta$, so that

$$
\kappa = 1 - \beta\cos\theta ,
$$

and an azimuthal angle $\phi$ that measures the orientation of $\vec u_R$ around the direction of $\vec\beta$.

For **linear acceleration**, $d\vec\beta/dt_r\parallel\vec\beta$, the vector triple product collapses. Since $\vec\beta\times\,d\vec\beta/dt_r = 0$, one has $\left(\vec u_R-\vec\beta\right)\times\,d\vec\beta/dt_r = \vec u_R\times\,d\vec\beta/dt_r$ and therefore

$$
\left|\vec u_R\times\left[\left(\vec u_R-\vec\beta\right)\times\,d\vec\beta/dt_r\right]\right|^2
= \left(d\beta/dt_r\right)^{2}\sin^2\theta .
$$

The distribution is

$$
\frac{dP}{d\Omega} = \frac{ϙ^2\left(d\beta/dt_r\right)^{2}\sin^2\theta}{16\pi^2\epsilon c\,\kappa^6},
$$

which is the non-relativistic dipole pattern $\sin^2\theta$ distorted by the forward-beaming factor $\kappa^{-6}$. There is no radiation along the direction of acceleration ($\theta = 0$) or opposite to it ($\theta = \pi$): the angular distribution vanishes on the two directions collinear with the motion. For $\beta\to 0$ the factor $\kappa^{-6}\to 1$ and the total power reduces to the Larmor value $\frac{ϙ^2\left(d\beta/dt_r\right)^{2}}{6\pi\epsilon c}$.

For **circular motion**, $d\vec\beta/dt_r\perp\vec\beta$. Choosing $\vec\beta$ along the polar axis and $d\vec\beta/dt_r$ in the equatorial plane, the same algebra gives

$$
\left|\vec u_R\times\left[\left(\vec u_R-\vec\beta\right)\times\,d\vec\beta/dt_r\right]\right|^2
= \left(d\beta/dt_r\right)^{2}\left[\kappa^2 - \frac{\sin^2\theta\cos^2\phi}{\gamma^2}\right],
$$

and hence

$$
\frac{dP}{d\Omega} = \frac{ϙ^2\left(d\beta/dt_r\right)^{2}}{16\pi^2\epsilon c\,\kappa^6}
\left[\kappa^2 - \frac{\sin^2\theta\cos^2\phi}{\gamma^2}\right].
$$

Like the linear case, the pattern is forward-beamed by the factor $\kappa^{-6}$, so at high speed the emission is concentrated in a narrow cone around the instantaneous velocity. The term in $\gamma^{-2}$ is the correction that distinguishes circular from linear motion: since $\phi$ vanishes for directions lying in the orbital plane (the plane containing $\vec\beta$ and $d\vec\beta/dt_r$), that term suppresses radiation emitted within the orbital plane relative to directions perpendicular to it, by a relative amount of order $\gamma^{-2}$ at angles away from the forward direction.

**A remark on the temporal convention.** The distributions above are written per unit of the observer's time $t$ and with $d\vec\beta/dt_r$ the retarded-time derivative; hence the power of $\kappa$ in the denominator is six. The same distributions are often written per unit of the retarded time $t_r$; because $dt = \kappa\,dt_r$, that convention multiplies the distributions by $\kappa$ and produces the more familiar-looking denominators $\kappa^5$ (general), $\kappa^5$ (linear), and $\kappa^3$ (circular, after the identity above is used to cancel two powers). No physical quantity depends on the choice; only the bookkeeping of the distribution does. The physical total power is the same in either convention; the two distributions themselves are not, since they differ pointwise by the direction-dependent factor $\kappa$, so the sphere integral must be taken with that factor in the retarded-time form.

**Forward beaming.** The factor $\kappa^{-6}$ is the entire content of relativistic beaming. For $\beta\to1$, $\kappa$ is small only within the forward cone $\theta\lesssim1/\gamma$; outside it, the distribution is suppressed by many powers of $\gamma$. The radiated energy is therefore concentrated in a narrow forward cone of half-angle of order $1/\gamma$, the same cone that controls the relativistic Doppler effect and the synchrotron spectrum. As $\beta\to1$, the angular distribution becomes an increasingly sharp forward spike: the charge radiates almost entirely along its direction of motion.

## Radiation Reaction and the Self-Force

A charge that radiates loses energy and momentum, and the loss must appear as a force acting on the charge itself. In the point-particle idealization the standard result is the **Abraham–Lorentz–Dirac** equation,

$$
m\frac{du^\mu}{d\tau} = f^\mu_{\text{ext}}
+ \frac{ϙ^2}{6\pi\epsilon c^3}\left(\frac{d^2u^\mu}{d\tau^2} + \frac{u^\mu}{c^2}\frac{du^\nu}{d\tau}\frac{du_\nu}{d\tau}\right).
$$

The bracketed term is the radiation-reaction four-force. In tensor form it reads

$$
K^\mu_{\mathrm{rad}}
= \frac{ϙ^2}{6\pi\epsilon c^3}\left(\frac{d^2u^\mu}{d\tau^2} + \frac{u^\mu}{c^2}\frac{du^\nu}{d\tau}\frac{du_\nu}{d\tau}\right),
$$

the radiation-reaction counterpart of the electromagnetic four-force $K^\mu$ of *The Lorentz Force in Biquaternion Form*. Its defining property is that it is **orthogonal to the worldline**:

$$
K^\mu_{\mathrm{rad}}u_\mu = 0 .
$$

This orthogonality is the statement that the reaction force does no work in the instantaneous rest frame; it follows from $u^\mu u_\mu = c^2$ being constant, which gives $u_\mu\,d^2u^\mu/d\tau^2 = -\frac{du^\nu}{d\tau}\frac{du_\nu}{d\tau}$.

Two caveats should be stated plainly. First, the framework does not resolve the well-known pathologies of the equation — the runaway solutions and the pre-acceleration that follow from treating the self-force as a local differential expression. Second, the equation above is the standard result, not a derivation of the self-force from the biquaternion framework, and the point-charge self-energy divergence is untouched by the change of language. The radiation-reaction problem is thus **represented** cleanly in the framework, but it is not solved by it. A rigorous derivation from Maxwell's theory does exist, however, and it is the subject of the next paragraph.

**A rigorous derivation exists outside the framework.** Whether the point-charge self-force can be derived from Maxwell's theory without adding anything has a positive answer, due to A. Gsponer. The method is to define the retarded potentials, fields and currents as **nonlinear generalized functions** and to carry out every calculation in a **Colombeau algebra** — an algebra in which the product of singular fields is defined, which is indispensable here because the energy–momentum tensor is quadratic in the field and the fields diverge on the worldline. The biquaternion spinor representation of electrodynamics is what makes the four-dimensional integrations exact and closed-form. With those tools the total rate of energy–momentum radiated through a surface enclosing the worldline is shown to be rigorously equal to minus the self-interaction force on the charge,

$$
\left(dP/dt_r\right)(\Sigma) = -\mathcal{Q},
$$

the general self-interaction force is obtained in closed form with limits that reproduce the Abraham–von Laue expression, and the Lorentz–Dirac equation of motion follows from it. The paper also identifies why the Schott term was missing or wrong in the customary derivations: the self-energy of a point charge is not the Coulomb self-energy but an integral over a $\delta^2$ function, and that integral contributes a finite part to the Schott term; the same cancellation removes the 4/3 discrepancy between the Coulomb and the electromagnetic self-masses. Nothing in Maxwell's theory is changed — the modification is the class of functions and the algebra used to compute with them — and a by-product of the method is that the worldline condition $dZ/dt_r\circ\,dZ/dt_r = 1$ fixes the relevant Colombeau moment to $C^{[1]} = 1$, which is exactly the value that makes the derived reaction term the standard one. The corpus records this as an external result: a derivation from Maxwell's theory by a rigorous analytic method, in which the biquaternion algebra plays the same computational role it plays in the retarded-potential sections above.

**An independent quaternion route to the same equation.** The rigorous derivation above is not the first route to the Lorentz–Dirac equation through the algebra. In 1941 Paul Weiss, a student of Max Born, took the quaternion spinor decomposition of the four-velocity, $\tilde{V}=BB^{+}$ — the square root of the four-velocity, which he explicitly did *not* identify with Dirac's bispinors — obtained explicit formulas for the four-acceleration and for the retarded null separation $X-Z=2i\xi B\sigma B^{+}$ (whose translation into the conventions of this article is worked out in the section on the spinor square root above), and asked for the worldlines on which the energy–momentum flow through a hypersurface enclosing the charge is stationary. The resulting equation of motion is the Lorentz–Dirac equation. That is plausibly the first significant use of spinors in classical physics, and it is independent of the Colombeau derivation above. The source's own historical note adds that the equation had been derived before Dirac's 1938 paper by Myron Mathisson (1931), by a method the commentators regard as more satisfactory. The corpus records all three as history; the framework's own content is the transcription of the reaction force given above.

**The divergence is a property of the inhomogeneous equation, and one classical programme attacks it head-on.** A charge that appears on the right-hand side of Maxwell's equations carries the infinite self-energy above; a charge read instead as a **singularity of the homogeneous (vacuum) equation** need not. That is the interpretation of Lanczos's electrodynamics reconstructed by Gsponer and Hurni: the homogeneous Maxwell equation is taken as the biquaternion generalisation of the Cauchy–Riemann regularity conditions — a function theory of four complex variables — and a charged particle is a singular set of that equation rather than a source. Deriving the usual action integral of classical electrodynamics from Lanczos's action, the authors find no divergence in the self-interaction: the mass term is finite for a proper boundary tube of finite retarded radius $\xi_y$, the standard infinite point-charge mass returns only in the limit $\xi_y\to0$, and the opposite limit $\xi_y\to\infty$, which encloses the singularities of the whole universe, gives zero masses and destroys the derivation, so the finite result is an intermediate-scale effect. The interaction term requires in addition that the external field vary slowly over the tube, of the order of the classical electron radius $r_e$, which the authors identify with the usual conditions for the internal consistency of classical electrodynamics rather than with a new cutoff. The model is **not** the Abraham–Lorentz extended electron: the singularities carry no finite structure, and the potential and field are not discontinuous at the boundary. The corpus records this as a programme of its own rather than as a result of the framework above — it is the one biquaternion route that confronts the self-energy divergence directly, and it does so outside the point-source idealisation in which the rest of this article works.

**The point charge is an idealisation, and the classical electron carries more.** Gsponer's own conclusion draws the boundary that his derivation makes precise: the classical electrodynamics of point charges is mathematically an internally consistent theory once potentials, fields and currents are nonlinear generalized functions, but the mathematical point charge — a simple pole of the potential — is an idealisation. A classical point-electron carries, besides its electric charge, an intrinsic magnetic dipole moment and a spin, described by a four-potential that superposes the Coulomb term with a dipole term. Gsponer suggests applying the same method to that potential, which would yield an equation of motion generalising Lorentz–Dirac's for a classical electron with magnetic moment and spin. That is precisely the question left open in *The Classical Spinning Particle: The Bargmann–Michel–Telegdi Equation in Biquaternionic Form*, where the coupling of the spin to the radiation-reaction force is listed as unresolved; the two articles meet here. As elsewhere in the corpus, the internal consistency of the mathematics does not fix the mass, and the algebra does not supply the electron's moment and spin; those are inputs, not consequences.

## Relation to the Two Exercises

The construction above is the declared foundation for two downstream exercises, and it is worth recording explicitly which parts each one uses.

*Exercise: The Electromagnetic Field of a Uniformly Moving Charge* is the case of vanishing acceleration. Setting $d\vec\beta/dt_r = 0$ in the field formulas of the section "The Field of the Retarded Potential" leaves $\tilde{F} = \tilde{F}_v$; the exercise is then the evaluation of $\vec E_v = \frac{ϙ}{4\pi\epsilon}\frac{(1-\beta^2)(\vec u_R-\vec\beta)}{\kappa^3R^2}$ and $\vec B_v = \vec u_R\times\vec E_v/c$, and the identification of the result as the Heaviside ellipsoid field, equivalently as the boost of the Coulomb field. The pieces needed are the Liénard–Wiechert potential of "The Retarded Null Biquaternion" and the velocity field of "The Velocity Field".

*Exercise: The Electromagnetic Field of a Moving Charge* is the general case. It uses the full Liénard–Wiechert potential, the field split $\tilde{F} = \tilde{F}_v + \tilde{F}_a$ of "The Field of the Retarded Potential", and the two component expressions of "The Velocity Field" and "The Acceleration Field as the Radiation Field". The exercise is then the evaluation of both parts for a specified worldline, and the demonstration that the far-zone field is the radiation field alone.

## Summary

The radiation from an accelerated charge is treated in the biquaternion framework by specializing the retarded solution of the biquaternionic Maxwell equation to a point source. The retarded convolution localizes on the worldline and produces the Liénard–Wiechert potential in the compact form

$$
\tilde{A} = \frac{\mu ϙ}{4\pi D}\,\tilde{V}/\gamma,
\qquad
\tilde{V}/\gamma = ic\,e_t + \vec v(t_r),
\qquad
D = R - \vec R\cdot\vec\beta
= -\frac{1}{c}\,\mathrm{Sc}\!\left((\tilde{V}/\gamma)(iR\,e_t+\vec R)^{\natural}\right),
$$

built from the null retarded separation $iR\,e_t + \vec R$ and the four-velocity $\tilde{V} = \gamma\left(ic\,e_t + \vec v(t_r)\right)$, both in $\mathbb{M}_-$.

The same potential can be written with the invariant retarded distance $\xi = -i\,\mathrm{Sc}\!\left(\frac{\tilde{V}}{ic}(iR\,e_t+\vec R)^{\natural}\right) = \gamma D$ and the spinor square root of the four-velocity, $B = \cosh\tfrac{y}{2}e_t - i\sinh\tfrac{y}{2}\vec u_\beta$ with $\tilde{V} = ic\,B^2$:

$$
\tilde{A} = \frac{\mu ϙ}{4\pi\xi}\,\tilde{V} = \frac{i\mu ϙ c}{4\pi\xi}\,B^2,
$$

and the null separation factorises through the primitive idempotent $\sigma = \tfrac12(e_t + i\vec u)$ as $iR\,e_t+\vec R = 2i\xi\,B\sigmaB^+$. In the same variables the four-acceleration is the boost conjugate of the rest-frame acceleration, $d\tilde{V}/d\tau = B\vec aB^+$.

The field strength splits into a velocity part and an acceleration part, $\tilde{F} = \tilde{F}_v + \tilde{F}_a$. The velocity field $\tilde{F}_v$ falls as $1/R^2$, has vanishing second invariant and positive first invariant, $I_{1,v} = (\vec u_R\cdot\vec E_v)^2 > 0$, and is of electric type; it is the field of a uniformly moving charge and is not radiation. The acceleration field $\tilde{F}_a$ falls as $1/R$, is transverse, and is **null**:

$$
I_{1,a} = I_{2,a} = 0,
\qquad
\langle\tilde{F}_a\rangle_{\natural} = 0,
\qquad
\tilde{F}_a^2 = 0,
$$

so that the radiation field is a **zero divisor and a nilpotent element** of $\mathbb{B}$. This is the concrete realization of the null-field characterization anticipated in the companion article on the field-strength invariants.

The radiated power is the biquaternion norm of the four-acceleration biquaternion,

$$
P = \frac{ϙ^2}{6\pi\epsilon c^3}\,N\!\left(\frac{d\tilde{V}}{d\tau}\right),
$$

the relativistic Larmor formula, with the standard $\gamma^6$ (linear) and $\gamma^4$ (circular) enhancements as special cases. The angular distribution carries the forward-beaming factor $\kappa^{-6}$, which concentrates the radiation into a cone of half-angle of order $1/\gamma$ at high speed. The radiation-reaction force $K^\mu_{\mathrm{rad}}$ is orthogonal to the worldline, though the standard pathologies of the point-charge self-force remain. An external derivation of the Lorentz–Dirac equation from Maxwell's theory — in a Colombeau algebra of nonlinear generalized functions, with the biquaternion representation supplying the closed-form integrations — gives the rigorous balance between the radiated energy–momentum rate and the self-interaction force and identifies the correct point-charge self-energy as a $\delta^2$ integral rather than the Coulomb one.

The construction is explicit enough that the two downstream exercises are direct applications: R4 is the case $d\vec\beta/dt_r = 0$, and E1 is the general case.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) subspaces |
| $\mathbb{H}_{\mathbb{B}}, \mathbb{C}_{\mathbb{B}}$ | Real-quaternion and scalar subspaces |
| $\tilde{\nabla}, \tilde{\nabla}^{\natural}, \Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ | Biquaternionic gradient, conjugate, d'Alembertian |
| $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ | Field-strength biquaternion |
| $\tilde{F}_v, \tilde{F}_a$ | Velocity part and acceleration (radiation) part of the field |
| $\tilde{A} = i\phi/c\,e_t + \vec A$ | Potential biquaternion (Liénard–Wiechert) |
| $\tilde J = ic\rho\,e_t + \vec J$ | Four-current of the potential wave equation |
| $t_r$ | Retarded time, $t_r = t - \lvert x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec r_q(t_r)\rvert/c$ |
| $\vec R = x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec r_q(t_r)$, $R = \lvert\vec R\rvert$ | Retarded separation |
| $\vec u_R = \vec R/R$ | Unit retarded direction |
| $iR\,e_t + \vec R$ | Retarded null biquaternion, $\langle iR\,e_t+\vec R\rangle_{\natural}=0$ |
| $\tilde{V}/\gamma = ic\,e_t + \vec v(t_r)$ | Coordinate velocity, the four-velocity divided by $\gamma$ |
| $\tilde{V} = \gamma\left(ic\,e_t + \vec v(t_r)\right)$ | Four-velocity biquaternion, $\langle\tilde{V}\rangle_{\natural} = -c^2$ |
| $\vec\beta = \vec v(t_r)/c$, $\beta = \lvert\vec\beta\rvert$ | Dimensionless retarded velocity |
| $\gamma = (1-\beta^2)^{-1/2}$ | Lorentz factor |
| $\kappa = 1-\vec u_R\cdot\vec\beta$ | Retardation factor |
| $D = R-\vec R\cdot\vec\beta = R\kappa$ | Retarded distance, $D = -\frac{1}{c}\mathrm{Sc}((\tilde{V}/\gamma)(iR\,e_t+\vec R)^{\natural})$ |
| $\xi = \gamma D = -i\,\mathrm{Sc}\!\left(\frac{\tilde{V}}{ic}(iR\,e_t+\vec R)^{\natural}\right)$ | Invariant retarded distance (the source's $\xi$) |
| $B$, $B^2 = \tilde{V}/(ic)$, $B^+ = B$ | Bireal spinor square root of the four-velocity |
| $\sigma = \tfrac12(e_t + i\vec u)$ | Primitive idempotent; $\vec u$ the line of sight in the charge's rest frame |
| $\vec a = a_1\vec e_x + a_2\vec e_y + a_3\vec e_z$ | Rest-frame acceleration, a pure vector, $d\tilde{V}/d\tau = B\vec aB^+$ |
| $d\vec\beta/dt_r$ | Retarded-time acceleration ($d/dt_r$ in the field formulas) |
| $\vec E_v, \vec B_v, \vec H_v$ | Velocity-part fields |
| $\vec E_a, \vec B_a, \vec H_a$ | Acceleration-part (radiation) fields |
| $I_1 = \vec E^2 - c^2\vec B^2$, $I_2 = \vec E\cdot\vec B$ | Field invariants |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm |
| $dP/d\Omega$ | Power per unit solid angle (per observer time) |
| $\theta, \phi$ | Polar angle from $\vec\beta$, azimuthal angle |
| $\epsilon, \mu$, $c = 1/\sqrt{\epsilon\mu}$ | Medium permittivity, permeability, speed of light |
| $ϙ, m$ | Charge and mass of the radiating particle |
| $K^\mu_{\mathrm{rad}}$ | Radiation-reaction four-force, $K^\mu_{\mathrm{rad}}u_\mu = 0$, the counterpart of the Lorentz four-force $K^\mu$ |
| $P(\Sigma)$, $\mathcal{Q}$ | Radiated energy–momentum rate and self-interaction force (Gsponer), $\left(dP/dt_r\right)(\Sigma) = -\mathcal{Q}$ |
| $C^{[0]}, C^{[1]}$ | Colombeau moments of the mollifier; the worldline condition fixes $C^{[1]} = 1$ |

## Further Reading

- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the Liénard–Wiechert potentials, the velocity–acceleration split, and the relativistic Larmor formula.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the Liénard–Wiechert fields, the angular distributions, and the radiation-reaction equation.
- D. J. Griffiths, *Introduction to Electrodynamics* (Cambridge, 2017), for a careful elementary derivation of the Liénard–Wiechert potentials and fields.
- F. Rohrlich, *Classical Charged Particles* (World Scientific, 2007), for the Abraham–Lorentz–Dirac equation and the consistency of radiation reaction with energy conservation.
- P. A. M. Dirac, "Classical Theory of Radiating Electrons", *Proceedings of the Royal Society A* 167 (1938) 148–169, for the original derivation of the radiation-reaction force.
- P. Weiss, "On Some Applications of Quaternions to Restricted Relativity and Classical Radiation Theory", *Proceedings of the Royal Irish Academy* **46** (1941) 129–168, for the quaternion spinor decomposition of the four-velocity, the explicit four-acceleration and retarded-null formulas, and the derivation of the Lorentz–Dirac equation from a stationary energy–momentum flow.
- M. Mathisson, "Die Mechanik des Materieteilchens in der allgemeinen Relativitätstheorie", *Zeitschrift für Physik* **67** (1931) 826–844, for the derivation of the radiation-reaction equation of motion that preceded Dirac's (recorded as such by Gsponer and Hurni).
- A. Gsponer, "Derivation of the Self-Interaction Force on an Arbitrarily Moving Point-Charge and of its Related Energy-Momentum Radiation Rate: The Lorentz–Dirac Equation of Motion in a Colombeau Algebra", arXiv:0812.4812 [physics.class-ph] (2008), for the rigorous identity between the radiated energy–momentum rate and the self-interaction force, the closed-form general self-interaction force, the $\delta^2$ self-energy and the Schott term, and the unambiguous derivation of the Lorentz–Dirac equation; and the short companion, "The self-interaction force on an arbitrarily moving point-charge and its energy-momentum radiation rate: A mathematically rigorous derivation of the Lorentz–Dirac equation of motion", arXiv:0812.3493 (2008).
- J. F. Colombeau, *New Generalized Functions and Multiplication of Distributions*, North-Holland Mathematics Studies 84 (North-Holland, 1984), and *Elementary Introduction to New Generalized Functions*, North-Holland Mathematics Studies 113 (North-Holland, 1985), for the algebra of nonlinear generalized functions and the multiplication of distributions used in that derivation.
- D. Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the spacetime-algebra treatment of the electromagnetic field and its sources.
- C. Doran and A. Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra derivation of radiation from moving charges.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic formulation of the field equations and their retarded solutions.
- Cornelius Lanczos, *The Functional Theoretical Relationships of the Maxwell Aether Equations* (doctoral dissertation, Budapest, handwritten 1919), for the interpretation of the homogeneous Maxwell equation as a quaternion function theory and the charged particle as its singularity.
- A. Gsponer and J.-P. Hurni, "Cornelius Lanczos's Derivation of the Usual Action Integral of Classical Electrodynamics," *Foundations of Physics* **35** (2005) 865–880, for the derivation of the standard action from Lanczos's and the finite self-interaction and mass of the singularity model; and their "Lanczos's Functional Theory of Electrodynamics: A Commentary on Lanczos's PhD Dissertation" (1998).
- A. Gsponer and J.-P. Hurni, "The Physical Heritage of Sir W. R. Hamilton", arXiv:math-ph/0201058, for the biquaternion dictionary (the conjugations, the four-position $X = [ict;x\,\vec e_x+y\,\vec e_y+z\,\vec e_z]$ and the four-velocity), the spinor square root of the four-velocity, Synge's *minquat* and *nullquat* names, and the historical record of Weiss's retarded-null factorisation.
- A. Waser, "Application of Bi-Quaternions in Physics" (2000, updated 2007), for biquaternionic treatments of the electromagnetic field and its energy–momentum.
- I. Białynicki-Birula and Z. Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* 46 (2013) 053001, for the null complex-vector characterization of radiation.
