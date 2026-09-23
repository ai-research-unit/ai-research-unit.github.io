# __The Relativistic Particle in an External Field, in Biquaternionic Form__

## Introduction

A particle of rest mass $m$ and charge $q$ moving in a prescribed electromagnetic field is the simplest interacting system of classical relativistic mechanics. In the four-vector language its equation of motion is the Lorentz force, $dP^\mu/d\tau = q\,F^{\mu\nu}u_\nu$, and the field enters the dynamics through one prescription: **minimal coupling**, the replacement of the free four-momentum by $P \to P - q\tilde{A}$. This article develops that prescription inside the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, in the notation of the read-list articles, and makes explicit a distinction that is easy to pass over:

- **The canonical four-momentum is not the kinetic four-momentum once the potential is nonzero.** The two differ by $q\tilde{A}$. The kinetic momentum is gauge-invariant and is the object that satisfies the free mass-shell relation $N(\tilde{P}) = -m^2c^2$; the canonical momentum is gauge-dependent and is the object that appears in the Hamiltonian. In the free limit the two coincide, and only there.
- **The prescription has a Lagrangian face as well as an algebraic one.** Written as the replacement of the canonical four-momentum in the mass-shell relation it reads $N(\tilde{\Pi} - q\tilde{A}) = -m^2c^2$. Written as a prescription on the action it produces the canonical momentum $\tilde\Pi = \tilde{P} + q\tilde{A}$ directly, as the momentum conjugate to the four-position. The two faces are the same statement, and both are checked below.

Two limitations are stated at the outset, because they bound what is claimed.

**One particle, a prescribed field, and the proper-time derivative.** The field $\tilde{F}$ is *external*: it is a fixed function of the event $\tilde{X}$, not a dynamical field with its own equation of motion. The four-force $\tilde{K} = d\tilde{P}/d\tau$ is therefore a **proper-time** derivative, and for a single particle that is the correct form; the equation of motion is $\tilde{K} = q\,F(\tilde{U})$ and no conservation law is invoked. This matters because the proper-time form does **not** sum across bodies: the four-forces of two particles with different Lorentz factors are not the terms of a coordinate-time conservation law. That distinction, reported by the exercise *Four-Momentum Conservation in a Collision*, is the reason this article treats one particle only; a many-body or field-theoretic extension is a different problem and is not attempted here. Nothing in this article contradicts the exercise — the two statements concern different systems.

**The frame convention.** The read-list article on the Lorentz transformation builds the boost biquaternion from the four-velocity as $\tilde{\Lambda} = \sqrt{-\frac{i}{c}\bar{\tilde{U}}}$, with the boost direction aligned with the particle velocity $\hat{\mathbf{u}} = \hat{\mathbf{v}}$. The rotor built from $+\mathbf{v}$ carries the **laboratory to the moving frame**, and its quaternion conjugate carries the moving frame back to the laboratory. This is the convention used throughout: whenever this article transforms to the instantaneous rest frame of the particle it uses $\tilde{\Lambda}$ built from $+\tilde{U}$, and the inverse transformation is by $\bar{\tilde{\Lambda}}$. The convention is stated because it is a genuine ambiguity — the oppositely-signed rotor implements the same Lorentz transformation on a different branch — and it is fixed here rather than left implicit.

The article is organized as follows. The next section recalls the free four-momentum. The section after that states the minimal-coupling prescription and derives the canonical momentum from the action. The following section separates the canonical and kinetic momenta. The next section derives the equation of motion. Two sections check it on a purely electric field and on a purely magnetic field. A short section records the proper-time restriction, and another fixes the boost convention. A section separates what the algebra supplies from what it only transcribes, and the article closes with open questions.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the complex scalar subspace, the center of the algebra. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$. The four-position is $\tilde{X} = ict\,e_0 + \mathbf{x}$, the four-velocity is $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ with $\gamma = 1/\sqrt{1-\mathbf{v}^2/c^2}$, and the four-momentum is $\tilde{P} = m\tilde{U} = iE/c\,e_0 + \mathbf{p}$; all live in $\mathbb{M}_-$. The norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$, and the invariant pairing on $\mathbb{M}_-$ is $\langle\tilde{A},\tilde{B}\rangle = \mathrm{Sc}(\tilde{A}\bar{\tilde{B}}) = -a_0b_0 + \mathbf{a}\cdot\mathbf{b}$ for $\tilde{A} = ia_0e_0 + \mathbf{a}$, $\tilde{B} = ib_0e_0 + \mathbf{b}$. The four-potential is $\tilde{A} = i\phi/c\,e_0 + \mathbf{A} \in \mathbb{M}_-$ and the field strength is $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$, with source $\tilde{R} = \frac{i\rho}{\sqrt{\epsilon}}e_0 + \sqrt{\mu}\,\mathbf{J}$ and Maxwell equation $\tilde{\nabla}\tilde{F} = -\tilde{R}$. The field tensor is $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, with $F^{0k} = iE_k/c$ and $F^{jk} = \epsilon_{jkl}B_l$ in the $ict$ convention. Following the article *The Lorentz Force in Biquaternion Form*, the symbol $\tilde{F}$ is reserved for the field strength and the **four-force is written $\tilde{K}$**, so that $\tilde{K} = d\tilde{P}/d\tau$ and $\tilde{K}\in\mathbb{M}_-$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ its vacuum value; $\mathbf{B} = \mu\mathbf{H}$ is the magnetic induction. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged.

## The Free Particle

The free four-momentum and its mass-shell condition are inherited from *Relativistic Mechanics in Biquaternionic Form* and are recalled only to fix what the coupling will modify. The four-velocity and four-momentum are

$$
\tilde{U} = \gamma\left(ic\,e_0 + \mathbf{v}\right), \qquad
\tilde{P} = m\tilde{U} = i\,\frac{E}{c}\,e_0 + \mathbf{p},
\qquad E = \gamma mc^2, \quad \mathbf{p} = \gamma m\mathbf{v},
$$

and both lie in $\mathbb{M}_-$. The four-momentum satisfies the **mass-shell relation**

$$
N(\tilde{P}) = \tilde{P}\bar{\tilde{P}} = -\frac{E^2}{c^2} + \mathbf{p}^2 = -m^2c^2,
$$

equivalently $E^2 = \mathbf{p}^2c^2 + m^2c^4$. In the free theory the momentum that appears in the mass-shell relation is the particle's kinetic (mechanical) momentum, and it is also the canonical momentum conjugate to the four-position, because there is no potential to shift it. Minimal coupling is precisely the statement that this coincidence fails once $\tilde{A}\neq 0$.

## The Minimal-Coupling Prescription

The prescription is stated on the mass-shell relation and then translated into the action. Both forms are used below.

### The mass-shell form

**Minimal coupling replaces the canonical four-momentum by $\tilde{\Pi} - q\tilde{A}$ in the mass-shell relation:**

$$
\boxed{\;N\!\left(\tilde{\Pi} - q\tilde{A}\right) = -m^2c^2.\;}
$$

Here the four-momentum before the replacement is the **canonical** four-momentum $\tilde\Pi$, and the shifted object is the **kinetic (mechanical)** four-momentum $\tilde{P}_{\mathrm{kin}}$. In the free theory the two coincide; the coupling is what separates them. To keep them apart we write

$$
\tilde{P}_{\mathrm{kin}} := \tilde\Pi - q\tilde{A}\ \text{(kinetic)}, \qquad
\tilde\Pi = \tilde{P}_{\mathrm{kin}} + q\tilde{A}\ \text{(canonical)},
$$

so that the prescription reads $\tilde{\Pi} \to \tilde{\Pi} - q\tilde{A}$, and the mass-shell condition becomes $N(\tilde{P}_{\mathrm{kin}}) = -m^2c^2$. In the free limit $\tilde{A}\to0$ the kinetic momentum reduces to the free symbol $\tilde{P} = m\tilde{U}$ of the preceding section, and the notation is consistent: $\tilde{P}_{\mathrm{kin}}$ is what $\tilde{P}$ becomes once the field is switched on.

Expanding in components, with $\tilde\Pi = i\Pi_0 e_0 + \boldsymbol{\Pi}$ and $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$,

$$
\tilde{P}_{\mathrm{kin}} = i\left(\Pi_0 - \frac{q\phi}{c}\right)e_0 + \left(\boldsymbol{\Pi} - q\mathbf{A}\right)
= i\,\frac{E}{c}\,e_0 + \mathbf{p},
$$

so the scalar coefficient $\Pi_0 - q\phi/c$ is the kinetic energy divided by $c$ and the vector coefficient $\boldsymbol{\Pi} - q\mathbf{A}$ is the kinetic three-momentum:

$$
E = c\,\Pi_0 - q\phi, \qquad \mathbf{p} = \boldsymbol{\Pi} - q\mathbf{A}.
$$

The mass-shell relation $N(\tilde{P}_{\mathrm{kin}}) = -m^2c^2$ then reads

$$
-\frac{\left(c\Pi_0 - q\phi\right)^2}{c^2} + \left(\boldsymbol{\Pi} - q\mathbf{A}\right)^2 = -m^2c^2,
$$

that is,

$$
\left(c\Pi_0 - q\phi\right)^2 = \left(\boldsymbol{\Pi} - q\mathbf{A}\right)^2c^2 + m^2c^4 .
$$

Solving for the canonical energy $E_{\mathrm{can}} := c\,\Pi_0$ gives the **relativistic Hamiltonian**

$$
\boxed{\;E_{\mathrm{can}} = q\phi + c\sqrt{\left(\boldsymbol{\Pi} - q\mathbf{A}\right)^2 + m^2c^2}.\;}
$$

This is the standard result: the potential energy $q\phi$ is added, and the kinetic energy is built from the kinetic momentum $\boldsymbol{\Pi} - q\mathbf{A}$, not from the canonical momentum $\boldsymbol{\Pi}$. The kinetic energy in the bracket is the one that would be computed for a free particle whose momentum is $\mathbf{p} = \boldsymbol{\Pi} - q\mathbf{A}$.

### The action form and the canonical momentum

The same prescription is forced by the action. Let $\tau$ be the proper time and $\dot{\tilde{X}} = d\tilde{X}/d\tau$. The action of a charged particle in a prescribed field is

$$
S = -mc\int\sqrt{-N(\dot{\tilde{X}})}\,d\tau \;+\; q\int \mathrm{Sc}\!\left(\tilde{A}\,\bar{\dot{\tilde{X}}}\right)d\tau,
$$

with Lagrangian

$$
L = -mc\sqrt{-N(\dot{\tilde{X}})} \;+\; q\,\mathrm{Sc}\!\left(\tilde{A}\,\bar{\dot{\tilde{X}}}\right)
= -mc\sqrt{-N(\dot{\tilde{X}})} \;+\; q\left\langle \tilde{A}, \dot{\tilde{X}}\right\rangle .
$$

The first term is the free point-particle Lagrangian of the parent article; the second is the coupling, and its sign is fixed below by the requirement that the canonical momentum come out positive. The conjugate momentum is the element of $\mathbb{M}_-$ defined by the first variation, $\delta L = \langle \tilde\Pi, \delta\dot{\tilde{X}}\rangle$. For the free term, using $\delta N(\dot{\tilde{X}}) = 2\langle \dot{\tilde{X}}, \delta\dot{\tilde{X}}\rangle$ and the on-shell normalization $N(\dot{\tilde{X}}) = -c^2$,

$$
\delta\!\left(-mc\sqrt{-N(\dot{\tilde{X}})}\right)
= \frac{mc}{\sqrt{-N(\dot{\tilde{X}})}}\left\langle \dot{\tilde{X}}, \delta\dot{\tilde{X}}\right\rangle
= m\left\langle \dot{\tilde{X}}, \delta\dot{\tilde{X}}\right\rangle,
$$

so the free term contributes $m\dot{\tilde{X}} = \tilde{P}$. The coupling contributes $q\langle\tilde{A}, \delta\dot{\tilde{X}}\rangle$, hence $q\tilde{A}$. The conjugate momentum is therefore

$$
\boxed{\;\tilde\Pi = m\dot{\tilde{X}} + q\tilde{A} = \tilde{P} + q\tilde{A},\;}
$$

that is, **canonical = kinetic + $q\tilde{A}$**, which is exactly the component statement above. The prescription $P \to P - qA$ of the mass-shell form and the conjugate momentum of the action form are the same equation read in opposite directions.

**Sign convention.** The pair of signs used here is the one inherited from the gauge-principle article: the covariant derivative is $D = \tilde{\nabla} + \frac{iq}{\hbar}\tilde{A}$ with gauge transformation $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$, and at the classical level the corresponding canonical/kinetic relation is $\tilde\Pi = \tilde{P}_{\mathrm{kin}} + q\tilde{A}$, equivalently $\tilde{P}_{\mathrm{kin}} = \tilde\Pi - q\tilde{A}$. This is the standard classical sign (the interaction Lagrangian is $-q\phi + q\mathbf{A}\cdot\mathbf{v}$ in laboratory time), and it is *not* silently reversed anywhere below. The corpus's field-theoretic sign conventions for the Dirac field are recorded in the minimal-coupling article; the classical statement here is the same prescription on the same connection.

## Canonical Momentum Is Not Kinetic Momentum

Once $\tilde{A}\neq 0$, two four-vectors that coincide in the free theory separate, and the difference is physical.

**Gauge behaviour.** Under a gauge transformation of the connection, $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ with $\Gamma$ a real scalar. The kinetic momentum is unchanged,

$$
\tilde{P}_{\mathrm{kin}}' = \tilde\Pi' - q\tilde{A}' = \left(\tilde\Pi - q\tilde{\nabla}\Gamma\right) - q\left(\tilde{A} - \tilde{\nabla}\Gamma\right) = \tilde\Pi - q\tilde{A} = \tilde{P}_{\mathrm{kin}},
$$

while the canonical momentum shifts:

$$
\tilde\Pi' = \tilde{P}_{\mathrm{kin}} + q\tilde{A}' = \tilde\Pi - q\tilde{\nabla}\Gamma .
$$

So **the kinetic momentum is gauge-invariant and the canonical momentum is not.** A physical four-momentum cannot be gauge-dependent; the kinetic momentum is the physical one. The canonical momentum is the variable conjugated to position, and it is the variable in which the Hamiltonian is written; it inherits the gauge freedom of $\tilde{A}$ and is not itself observable.

**Free limit.** If $\tilde{A} = 0$ then $\tilde\Pi = \tilde{P}_{\mathrm{kin}} = \tilde{P}$ and every statement below reduces to the free ones of the parent article. The distinction is created by the coupling, not by the formalism.

**A concrete case: the uniform magnetic field.** The cleanest display of the difference is a particle in a uniform magnetic field, where the canonical momentum has conserved components that the kinetic momentum does not. Take $\mathbf{B} = B_0\hat{\mathbf{e}}_3$ and the Landau gauge

$$
\tilde{A} = B_0 x\,e_2, \qquad \text{i.e.} \qquad \mathbf{A} = B_0 x\,\hat{\mathbf{e}}_2 .
$$

The Lagrangian does not depend on $y$ or $z$, so the conjugate momenta $\Pi_2$ and $\Pi_3$ are conserved:

$$
\Pi_2 = p_y + qB_0 x = \text{const}, \qquad \Pi_3 = p_z = \text{const}.
$$

The kinetic momentum, by contrast, is not conserved: it rotates in the plane perpendicular to $\mathbf{B}$, since the equation of motion $d\mathbf{p}/dt = q\,\mathbf{v}\times\mathbf{B}$ with $\mathbf{v} = \mathbf{p}c^2/E$ is circular motion. The conserved quantities are the canonical components, the gauge-dependent ones; the kinetic momentum is the gauge-invariant one, and it is the one that turns. Both statements were checked numerically (see the companion), and they are not in tension: a gauge-dependent quantity may be conserved while a gauge-invariant quantity is not.

**What the distinction is not.** It is not a statement that the canonical momentum is unphysical. The canonical momentum is the generator of translations of the field and the variable of the Hamiltonian; its conservation is what makes the problem integrable in the Landau gauge. The point is only that it is *not* the momentum that appears in the velocity, $\mathbf{v} = \mathbf{p}_{\mathrm{kin}}c^2/E_{\mathrm{kin}}$, and *not* the momentum that obeys the free mass-shell relation.

## The Equation of Motion

The equation of motion follows from the action by the Euler–Lagrange equations, and it is the Lorentz force. Written in components $\tilde{X} = \sum_\mu X_\mu e_\mu$ (with $X_0 = ict$), $\tilde{A} = \sum_\nu A_\nu e_\nu$, the Lagrangian is

$$
L = -mc\sqrt{-\sum_\mu \dot{X}_\mu^2} \;+\; q\sum_\nu A_\nu(X)\,\dot{X}_\nu,
\qquad \dot{X}_\mu = \frac{dX_\mu}{d\tau},
$$

because $\mathrm{Sc}(\tilde{A}\bar{\dot{\tilde{X}}}) = \sum_\nu A_\nu\dot{X}_\nu$ in the $ict$ convention. The conjugate momentum is $\Pi_\mu = \partial L/\partial\dot{X}_\mu$, with $\Pi_0 = m\dot{X}_0 + qA_0$ and $\Pi_k = m\dot{X}_k + qA_k$ up to the on-shell normalization $\sqrt{-\sum_\mu\dot{X}_\mu^2} = c$. Differentiating $\Pi_\mu$ along the worldline and using the Euler–Lagrange equation $\frac{d}{d\tau}\Pi_\mu = \partial L/\partial X_\mu$,

$$
\frac{d}{d\tau}\left(m\dot{X}_\mu + qA_\mu\right) = q\sum_\nu \frac{\partial A_\nu}{\partial X_\mu}\dot{X}_\nu,
$$

and therefore

$$
\frac{d}{d\tau}\left(m\dot{X}_\mu\right)
= q\sum_\nu\left(\frac{\partial A_\nu}{\partial X_\mu} - \frac{\partial A_\mu}{\partial X_\nu}\right)\dot{X}_\nu
= q\sum_\nu F_{\mu\nu}\dot{X}_\nu .
$$

Since $m\dot{X}_\mu = P_{\mathrm{kin},\mu}$ on shell and $\dot{X}_\nu = U_\nu$, this is the standard contraction

$$
\boxed{\;\frac{dP_{\mathrm{kin}}^\mu}{d\tau} = q\,F^{\mu\nu}U_\nu , \qquad \tilde{K} = \frac{d\tilde{P}_{\mathrm{kin}}}{d\tau}.\;}
$$

The contraction $\tilde{K} = q\,F(\tilde{U})$ is an element of $\mathbb{M}_-$, as it must be, and it is the **component form** of the Lorentz four-force. In components, with $F^{0k} = iE_k/c$ and $F^{jk} = \epsilon_{jkl}B_l$, the contraction is exactly the four-force of the read-list article,

$$
\tilde{K} = i\,\frac{\gamma q}{c}\left(\mathbf{E}\cdot\mathbf{v}\right)e_0 + \gamma q\left(\mathbf{E} + \mathbf{v}\times\mathbf{B}\right),
$$

whose scalar part is the power and whose vector part is the relativistic three-force. The equation was checked against this component form at random fields and velocities; the agreement is exact (to machine precision), not approximate.

**The biquaternion product form.** The same four-force has the representation, established in *The Lorentz Force in Biquaternion Form*, as the anti-Hermitian projection of the product of the four-velocity and the field strength:

$$
\tilde{K} = -\,q\sqrt{\mu}\;P_{\mathbb{M}_-}\!\left(\tilde{U}\tilde{F}\right),
\qquad
P_{\mathbb{M}_-}(X) = \tfrac{1}{2}\left(X - X^\dagger\right).
$$

This article does not re-derive that formula; it records that the two routes agree, because the minimal-coupling contraction $qF^{\mu\nu}U_\nu$ and the projection formula are the same element of $\mathbb{M}_-$. The minimal-coupling route exhibits the force as the derivative of a momentum; the product route exhibits it as a bilinear in $\tilde{U}$ and $\tilde{F}$ that is manifestly covariant.

**Two structural consequences.** First, the force is orthogonal to the kinetic four-momentum. Differentiating the mass shell $N(\tilde{P}_{\mathrm{kin}}) = -m^2c^2$ along the worldline gives

$$
\tilde{K}\bar{\tilde{P}}_{\mathrm{kin}} + \tilde{P}_{\mathrm{kin}}\bar{\tilde{K}} = 0,
$$

the biquaternion form of $K^\mu P_\mu = 0$: the Lorentz force rotates the four-momentum in $\mathbb{M}_-$ but does not change its norm form, so the rest mass is preserved. Second, because $\tilde{K}=d\tilde{P}_{\mathrm{kin}}/d\tau$ is a **proper-time** derivative, the equation is a statement about one worldline; the rest-mass preservation above is the statement that the norm of *that* four-momentum is constant, and it is not a conservation law for a system of bodies (see the closing section on the proper-time restriction).

## Case I: A Purely Electric Field

The first independent check is a purely electric field. This case is *not* the one that suggested the formula — the derivation above used a general field — but it isolates the scalar potential and the electric contribution to the force.

Take $\mathbf{B} = 0$ and a static, uniform electric field $\mathbf{E} = E_0\hat{\mathbf{e}}_1$, described by the potential $\phi = -E_0 x$, $\mathbf{A} = 0$, so that $\tilde{A} = -(iE_0/c)\,x\,e_0$. In this gauge the vector potential vanishes, so the canonical and kinetic momenta coincide in all three spatial components, $\Pi_k = p_k$, and differ only in the time component: $E_{\mathrm{can}} = E + q\phi$. The contraction $\tilde{K} = qF^{\mu\nu}U_\nu$ gives

$$
\frac{d\mathbf{p}}{dt} = q\mathbf{E} = qE_0\,\hat{\mathbf{e}}_1,
\qquad
\frac{dE}{dt} = q\,\mathbf{E}\cdot\mathbf{v} = qE_0\,v_x .
$$

The first equation is exact and undamped by $\gamma$: the kinetic three-momentum grows linearly in laboratory time, $p_x = qE_0 t$ for a particle released from rest at $t=0$, and the energy follows from the mass shell,

$$
E(t) = \sqrt{\left(qE_0t\right)^2c^2 + m^2c^4},
\qquad
v_x(t) = \frac{p_xc^2}{E} = \frac{qE_0tc^2}{\sqrt{\left(qE_0t\right)^2c^2 + m^2c^4}},
$$

so the worldline is hyperbolic and $v_x\to c$ as $t\to\infty$ without reaching it. The energy is not constant — an electric field does work — and its rate of change is the second equation above. The numerical solution of $d\mathbf{p}/dt = q\mathbf{E}$ with $\mathbf{v} = \mathbf{p}c^2/E$ reproduced $p_x = qE_0t$ to the integration accuracy and the mass-shell energy exactly.

Two remarks. The relation $d\mathbf{p}/dt = q\mathbf{E}$ holds for the **kinetic** momentum; had one differentiated the canonical momentum $\boldsymbol{\Pi} = \mathbf{p} + q\mathbf{A}$ instead, the vanishing of $\mathbf{A}$ in this gauge would hide the distinction, and a time-dependent $\mathbf{A}$ with $\mathbf{B}=0$ (a pure gauge field, or a field with $\mathbf{E} = -\partial_t\mathbf{A}$) would show it: then $\boldsymbol{\Pi}$ and $\mathbf{p}$ differ by $q\mathbf{A}$, and the force equation is the one for $\mathbf{p}$, not for $\boldsymbol{\Pi}$. This is the electric-field face of the canonical/kinetic distinction.

## Case II: A Purely Magnetic Field

The second independent check is a purely magnetic field. This is the case in which the canonical and kinetic momenta differ most visibly, because the conserved canonical components coexist with a rotating kinetic momentum.

Take $\mathbf{E} = 0$ and a static, uniform magnetic induction $\mathbf{B} = B_0\hat{\mathbf{e}}_3$. The contraction gives

$$
\frac{d\mathbf{p}}{dt} = q\,\mathbf{v}\times\mathbf{B},
\qquad
\frac{dE}{dt} = q\,\mathbf{E}\cdot\mathbf{v} = 0 .
$$

The energy is constant, hence $\gamma$ and $|\mathbf{p}|$ are constant, and the motion in the plane perpendicular to $\mathbf{B}$ is circular with the relativistic cyclotron frequency

$$
\omega_c = \frac{qB_0}{\gamma m}.
$$

The field does no work: a pure magnetic field changes the direction of the kinetic momentum but not its magnitude or the energy. Both statements follow from the contraction alone, without solving the equations.

The canonical momentum behaves differently, as the preceding section anticipated. In the Landau gauge $\mathbf{A} = B_0x\,\hat{\mathbf{e}}_2$, the components $\Pi_2 = p_y + qB_0x$ and $\Pi_3 = p_z$ are conserved, while the kinetic momentum $\mathbf{p}$ rotates: at any instant its components change, and only its magnitude is fixed. A numerical integration of $d\mathbf{p}/dt = q\mathbf{v}\times\mathbf{B}$ with $\mathbf{v} = \mathbf{p}c^2/E$ kept $E$ and $|\mathbf{p}|$ fixed to the integration accuracy, held $\Pi_2$ and $\Pi_3$ constant to machine precision, and produced the circular motion whose period is $2\pi/\omega_c$. This is the sharpest display of the article's main distinction: the conserved quantities are the gauge-dependent canonical components; the gauge-invariant kinetic momentum is not conserved.

**The two checks are independent.** The electric case tests the scalar-potential (time-component) part of the coupling, where the field does work; the magnetic case tests the vector-potential (space-component) part, where it does not. A formula fitted to one would not pass the other — the electric case would accept $d\mathbf{p}/dt = q\mathbf{E} + (\text{anything antisymmetric in }\mathbf{v},\mathbf{B})$ only if the magnetic term vanished for $\mathbf{B}=0$, and the magnetic case would accept a wrong coefficient of the electric term only if $\mathbf{E}=0$. The general derivation and the two cases agreeing on the *same* $\tilde{K} = qF^{\mu\nu}U_\nu$ is the content of the verification.

## The Proper-Time Restriction, Stated Explicitly

The equation of motion derived above is $\tilde{K} = d\tilde{P}_{\mathrm{kin}}/d\tau$, a **proper-time** derivative, and for one particle in a prescribed field this is the correct and standard form. It is worth stating what it does *not* license, because the point has been recorded elsewhere in the corpus.

For two particles with different Lorentz factors $\gamma_1\neq\gamma_2$,

$$
\tilde{K}_1 + \tilde{K}_2 = \gamma_1\frac{d\tilde{P}_1}{dt} + \gamma_2\frac{d\tilde{P}_2}{dt}
\;\neq\; \frac{d}{dt}\left(\tilde{P}_1 + \tilde{P}_2\right),
$$

so the sum of four-forces is **not** the coordinate-time derivative of the total four-momentum, and $\tilde{K}_1 + \tilde{K}_2 = 0$ is not a conservation law. The collision exercise *Four-Momentum Conservation in a Collision* reports exactly this: the four-force symbol of the mechanics article cannot be carried to a multi-body system without the $\gamma$ factors, and the conservation law is a statement about the total four-momentum, not about the sum of proper-time derivatives. This article is the complementary case — **one** particle, whose four-force is correctly $\tilde{K} = d\tilde{P}_{\mathrm{kin}}/d\tau$ — and it makes no conservation claim. The two articles do not disagree: the proper-time derivative is right for one worldline and insufficient for a sum of worldlines, and that is the whole of the matter.

## Frames and the Boost Rotor

The read-list article on the Lorentz transformation relates the boost biquaternion to the four-velocity,

$$
\tilde{\Lambda} = \sqrt{-\frac{i}{c}\,\bar{\tilde{U}}},
\qquad \tilde\Lambda\bar{\tilde\Lambda} = e_0,
$$

with the boost direction $\hat{\mathbf{u}}$ aligned with the particle velocity $\hat{\mathbf{v}}$, and implements the transformation of a four-vector by rotor conjugation $\tilde{X}' = \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$.

**Convention, stated once.** The rotor built from $+\tilde{U}$ carries the **laboratory to the moving (rest) frame**: acting on the four-velocity it gives

$$
\tilde{\Lambda}\,\tilde{U}\,\tilde{\Lambda}^\dagger = ic\,e_0,
$$

the four-velocity in the particle's rest frame, and the inverse transformation back to the laboratory is by the quaternion conjugate $\bar{\tilde{\Lambda}}$. This was checked numerically on boosts along and off the coordinate axes, including the sign branch selected by $\mathrm{Sc}(\tilde\Lambda)>0$; the rotor built by the same recipe from the velocity-reversed four-velocity $\bar{\tilde{U}} = \gamma(ic\,e_0 - \mathbf{v})$ carries the rest frame back to the laboratory and is the quaternion conjugate $\bar{\tilde{\Lambda}} = \sqrt{-\frac{i}{c}\tilde{U}}$. The convention matters because the two choices are not related by a relabelling of $\mathbf{v}$ alone — the sign branch and the direction of the transformation can be confused — and it is fixed here so that every use of $\tilde{\Lambda}$ below is unambiguous.

With that convention the four-velocity, the four-momentum, and the four-force all transform by the **vector** rule, $\tilde{Q}' = \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^\dagger$, because all three lie in $\mathbb{M}_-$. The field strength does **not**: it transforms by the **bivector** rule $\tilde{F}' = \bar{\tilde{\Lambda}}\tilde{F}\tilde{\Lambda}$, the same rule used in the Lorentz-force article. The product formula $\tilde{K} = -q\sqrt{\mu}\,P_{\mathbb{M}_-}(\tilde{U}\tilde{F})$ is covariant under the *pair* of rules, and the minimal-coupling equation $\tilde{K} = d\tilde{P}_{\mathrm{kin}}/d\tau$ is covariant because both sides are four-vectors. In the particle's rest frame, where $\tilde{U} = ic\,e_0$, the force reduces to $\tilde{K} = q\,\mathbf{E}_{\mathrm{rest}}$, the rest-frame electric field; this is the frame in which the electric and magnetic contributions to the force are cleanly separated, and it uses the convention above.

## What the Framework Supplies and What It Only Transcribes

**Supplied by the algebra.**

- *A single home for the four-vectors of the problem.* The four-position, four-velocity, kinetic four-momentum, canonical four-momentum, four-potential, and four-force all lie in the same four-dimensional real subspace $\mathbb{M}_-$, and the minimal-coupling shift $\tilde\Pi = \tilde{P}_{\mathrm{kin}} + q\tilde{A}$ is an equation inside that subspace.
- *A constraint, not an extra postulate.* The mass-shell relation $N(\tilde{P}_{\mathrm{kin}}) = -m^2c^2$ is the norm-form condition on $\mathbb{M}_-$; with minimal coupling it *is* the relativistic Hamiltonian, and it delivers both the canonical/kinetic relation and the form of the energy in one equation.
- *A canonical momentum from the action.* The conjugate momentum $\tilde\Pi = \tilde{P} + q\tilde{A}$ follows from the first variation of the biquaternion action with the pairing $\langle\tilde{A},\dot{\tilde{X}}\rangle$, with no index apparatus.
- *The form of the force.* The contraction $\tilde{K} = qF^{\mu\nu}U_\nu$ reassembles into the $\mathbb{M}_-$-valued four-force, and it agrees with the projection formula $ -q\sqrt{\mu}\,P_{\mathbb{M}_-}(\tilde{U}\tilde{F})$ of the Lorentz-force article.

**Only transcribed.** The minimal-coupling *principle* itself — that the canonical four-momentum should be replaced by $\tilde{\Pi} - q\tilde{A}$ — is not derived from the algebra; it is the standard prescription carried into it, and the algebra supplies a home and a compact expression rather than a reason. The sign conventions are inherited from the parent articles and are conventions, not results. The non-relativistic limit likewise reproduces the Newtonian Lorentz force, as it must, and does not test the relativistic part of the construction.

**Interpretation.** Reading $\tilde{A}$ as a connection and $\tilde{P}_{\mathrm{kin}} = \tilde\Pi - q\tilde{A}$ as the horizontal (gauge-covariant) momentum is a geometric reading of an algebraic statement; the algebra supplies the statement, and the bundle picture is a consistent reading of it, as in the gauge-principle and covariant-derivative articles. The claim here is not that the algebra forces the geometric reading.

**Gaps, left visible.** The extension to a *dynamical* field (in which $\tilde{A}$ obeys its own equation and the particle back-reacts) is not treated; that is a field-theoretic problem. The many-body conservation law is not treated (it belongs to the exercise and to *Noether's Theorem in Biquaternionic Form*). The relation of the classical canonical momentum to the quantized momentum of the canonical-quantization articles is not pursued.

## Open Questions

1. **Radiation reaction.** The field here is prescribed and does no back-reaction on the particle. What is the biquaternion form of the self-force of an accelerated charge, and does the algebra's structure (the null cone as the zero-divisor set) simplify the Larmor or Abraham–Lorentz analysis?

2. **The Lagrangian and Hamiltonian in the presence of a dynamical field.** The action written here couples the particle to a fixed connection. What is the joint action of particle and field, and does its biquaternion form exhibit the canonical structure more cleanly than the four-vector form?

3. **The canonical momentum and quantization.** The canonical momentum is the variable of the Hamiltonian and the natural quantization variable. How does the biquaternion canonical momentum of this article relate to the quantized momenta of the canonical-quantization articles, and does the sector assignment (which article finds $\tilde{A}\in\mathbb{M}_-$ with a conjugate momentum in $\mathbb{M}_+$) appear already at the level of the classical particle?

4. **Gauge choice and integrability.** In the uniform magnetic field the Landau gauge makes two canonical components conserved. Is there a biquaternion-natural gauge criterion — a condition on $S = \mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})$ or on the field strength — that selects the separable gauge for a given field, and is it the same as the standard one?

5. **The sign of the charge and the corpus's conventions.** The classical relation $\tilde\Pi = \tilde{P}_{\mathrm{kin}} + q\tilde{A}$ and the corpus's covariant derivative $D = \tilde{\nabla} + \frac{iq}{\hbar}\tilde{A}$ have been aligned here by the standard classical signs. Is there a corpus-wide convention that fixes the relative sign of the phase $\lambda = e^{iq\Gamma/\hbar}$ and the classical canonical momentum once and for all, or is it irreducibly a choice of the sign of $q$?

6. **Empirical content.** As everywhere in the framework, the unresolved question is whether any of this yields a prediction distinguishing it from standard relativistic electrodynamics. The construction as presented is a reformulation.

## Summary

A particle of charge $q$ and rest mass $m$ in a prescribed external field is described in biquaternionic form by the **minimal-coupling prescription**, the replacement of the canonical four-momentum by $\tilde{\Pi} \to \tilde{\Pi} - q\tilde{A}$ in the mass-shell relation:

$$
N\!\left(\tilde{\Pi} - q\tilde{A}\right) = -m^2c^2 .
$$

The object $\tilde{\Pi} - q\tilde{A}$ is the **kinetic** four-momentum and $\tilde{\Pi}$ is the **canonical** four-momentum, $\tilde{\Pi} = \tilde{P}_{\mathrm{kin}} + q\tilde{A}$. The prescription has two faces, and they agree: on the mass-shell relation it yields the relativistic Hamiltonian $E_{\mathrm{can}} = q\phi + c\sqrt{(\boldsymbol{\Pi}-q\mathbf{A})^2 + m^2c^2}$; on the action $S = -mc\int\sqrt{-N(d\tilde{X})} + q\int\mathrm{Sc}(\tilde{A}\,\bar{d\tilde{X}})$ it yields the conjugate momentum $\tilde\Pi = m\dot{\tilde{X}} + q\tilde{A}$. The two distinctions that carry the physical content are that the **kinetic momentum is gauge-invariant** and the **canonical momentum is not**, and that the kinetic, not the canonical, momentum is the one that obeys the free mass-shell relation and appears in the velocity $\mathbf{v} = \mathbf{p}c^2/E$.

The equation of motion is the Lorentz force in its contracted form,

$$
\frac{dP_{\mathrm{kin}}^\mu}{d\tau} = q\,F^{\mu\nu}U_\nu,
\qquad
\tilde{K} = \frac{d\tilde{P}_{\mathrm{kin}}}{d\tau}
= -\,q\sqrt{\mu}\;P_{\mathbb{M}_-}\!\left(\tilde{U}\tilde{F}\right),
$$

with $\tilde{K} = i\frac{\gamma q}{c}(\mathbf{E}\cdot\mathbf{v})e_0 + \gamma q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ in components. It preserves the rest mass, $\tilde{K}\bar{\tilde{P}}_{\mathrm{kin}} + \tilde{P}_{\mathrm{kin}}\bar{\tilde{K}} = 0$, and it is a proper-time equation about a single worldline. Two independent cases were checked — a purely electric field, where $d\mathbf{p}/dt = q\mathbf{E}$ and the field does work, and a purely magnetic field, where $d\mathbf{p}/dt = q\mathbf{v}\times\mathbf{B}$, the energy is constant, and the motion is circular at $\omega_c = qB_0/(\gamma m)$ — together with the general contraction at random fields. The two cases test the time-like and space-like parts of the coupling separately, so agreement on both is not agreement on the case that suggested the formula.

The algebra supplies the common home $\mathbb{M}_-$ of the four-vectors, the norm-form mass shell that doubles as the Hamiltonian, the conjugate momentum of the action, and the reassembly of the contraction into the four-force; it does not supply the minimal-coupling principle itself, the sign conventions, or the geometric reading, which are carried in or interpreted. The proper-time form is correct for this single-particle problem and is explicitly not a many-body conservation law, and the boost rotor is fixed by the convention that its $+\mathbf{v}$ branch carries the laboratory to the moving frame.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; complex scalar subspace (center) |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\langle\tilde{A},\tilde{B}\rangle = \mathrm{Sc}(\tilde{A}\bar{\tilde{B}})$ | Invariant pairing on $\mathbb{M}_-$ |
| $\tilde{X} = ict\,e_0 + \mathbf{x}$ | Four-position |
| $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ | Four-velocity, $N(\tilde{U}) = -c^2$ |
| $\tilde{P} = m\tilde{U} = iE/c\,e_0 + \mathbf{p}$ | Kinetic four-momentum, $N(\tilde{P}) = -m^2c^2$ |
| $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$ | Four-potential (material-sector connection) |
| $\tilde\Pi = \tilde{P} + q\tilde{A}$ | Canonical four-momentum |
| $\tilde{P}_{\mathrm{kin}} = \tilde\Pi - q\tilde{A} = \tilde{P}$ | Kinetic four-momentum (gauge-invariant) |
| $q$ | Charge (coupling constant, not fixed by the algebra) |
| $N(\tilde{P}_{\mathrm{kin}}) = -m^2c^2$ | Minimal-coupling mass-shell relation |
| $E_{\mathrm{can}} = c\Pi_0$ | Canonical energy; $E_{\mathrm{can}} = q\phi + c\sqrt{(\boldsymbol\Pi - q\mathbf{A})^2 + m^2c^2}$ |
| $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ | Field tensor; $F^{0k} = iE_k/c$, $F^{jk} = \epsilon_{jkl}B_l$ |
| $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ | Field-strength biquaternion |
| $\tilde{K} = d\tilde{P}_{\mathrm{kin}}/d\tau$ | Four-force; $\tilde{K} = qF^{\mu\nu}U_\nu = -q\sqrt{\mu}P_{\mathbb{M}_-}(\tilde{U}\tilde{F})$ |
| $P_{\mathbb{M}_-}(X) = \tfrac12(X - X^\dagger)$ | Projection onto $\mathbb{M}_-$ |
| $\tilde{\Lambda} = \sqrt{-\frac{i}{c}\bar{\tilde{U}}}$ | Boost rotor; $+\mathbf{v}$ branch: laboratory to moving frame |
| $\gamma = 1/\sqrt{1-\mathbf{v}^2/c^2}$ | Lorentz factor |
| $\omega_c = qB_0/(\gamma m)$ | Relativistic cyclotron frequency |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace pairing of the informational sector |

## Further Reading

- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the canonical momentum, the Lorentz force, and the motion of a charge in uniform electric and magnetic fields.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the relativistic Hamiltonian, the minimal-coupling form of the interaction, and cyclotron motion.
- Herbert Goldstein, Charles Poole, and John Safko, *Classical Mechanics* (Addison-Wesley, 2002), for the Lagrangian and Hamiltonian formulation of a charged particle in an external field.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1958), for the minimal substitution and the canonical-momentum convention in the quantum theory.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the spacetime-algebra treatment of the Lorentz force and the gauge-covariant derivative.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of Lorentz transformations and the geometric reading of minimal coupling.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the biquaternion algebra with the even subalgebra of $\mathrm{Cl}_{1,3}$.
- Companion articles: *Relativistic Mechanics in Biquaternionic Form*; *The Lorentz Force in Biquaternion Form*; *The Lorentz Transformation as a Biquaternionic Rotation*; *The Field-Strength Biquaternion and Its Invariants*; *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*; *The Gauge Principle in Biquaternionic Form*; *The Covariant Derivative and Gauge Connection in Biquaternionic Form*; *Exercise: Four-Momentum Conservation in a Collision*; *The Relativistic Two-Body Problem in Biquaternionic Form*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.
