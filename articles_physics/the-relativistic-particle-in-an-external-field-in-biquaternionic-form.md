# __The Relativistic Particle in an External Field, in Biquaternionic Form__

## Introduction

A particle of rest mass $m$ and charge $ϙ$ moving in a prescribed electromagnetic field is the simplest interacting system of classical relativistic mechanics. In the four-vector language its equation of motion is the Lorentz force, $dP_\mu/d\tau = ϙ\sum_\nu F_{\mu\nu}v_\nu$, and the field enters the dynamics through one prescription: **minimal coupling**, the replacement of the free four-momentum by $P \to P - ϙ\tilde{A}_{\Phi}$. This article develops that prescription inside the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, in the notation of the read-list articles, and makes explicit a distinction that is easy to pass over:

- **The canonical four-momentum is not the kinetic four-momentum once the potential is nonzero.** The two differ by $ϙ\tilde{A}_{\Phi}$. The kinetic momentum is gauge-invariant and is the object that satisfies the free mass-shell relation $\langle\tilde{P}_{\Phi}\rangle_{\natural} = -m^2c^2$; the canonical momentum is gauge-dependent and is the object that appears in the Hamiltonian. In the free limit the two coincide, and only there.
- **The prescription has a Lagrangian face as well as an algebraic one.** Written as the replacement of the canonical four-momentum in the mass-shell relation it reads $\langle\tilde P_{\Phi,\mathrm{can}} - ϙ\tilde{A}_{\Phi}\rangle_{\natural} = -m^2c^2$. Written as a prescription on the action it produces the canonical momentum $\tilde P_{\Phi,\mathrm{can}} = \tilde{P}_{\Phi} + ϙ\tilde{A}_{\Phi}$ directly, as the momentum conjugate to the four-position. The two faces are the same statement, and both are checked below.

Two limitations are stated at the outset, because they bound what is claimed.

**One particle, a prescribed field, and the proper-time derivative.** The field $\tilde{F}$ is *external*: it is a fixed function of the event $\tilde R_\Phi$, not a dynamical field with its own equation of motion. The four-force $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = d\tilde{P}_{\Phi}/d\tau$ is therefore a **proper-time** derivative, and for a single particle that is the correct form; the equation of motion is $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = ϙ\,F(\tilde{V}_{\Phi})$ and no conservation law is invoked. This matters because the proper-time form does **not** sum across bodies: the four-forces of two particles with different Lorentz factors are not the terms of a coordinate-time conservation law. That distinction, reported by the exercise *Four-Momentum Conservation in a Collision*, is the reason this article treats one particle only; a many-body or field-theoretic extension is a different problem and is not attempted here. Nothing in this article contradicts the exercise — the two statements concern different systems.

**The frame convention.** The read-list article on the Lorentz transformation builds the Lorentz rotor from the four-velocity as $\tilde U_{\Psi,\mathrm b} = \sqrt{-\frac{i}{c}\tilde{V}_{\Phi}^{\natural}}$, with the boost direction aligned with the particle velocity $\vec u = \vec u_v$. The rotor built from $+\vec v$ carries the **laboratory to the moving frame**, and its quaternion conjugate carries the moving frame back to the laboratory. This is the convention used throughout: whenever this article transforms to the instantaneous rest frame of the particle it uses $\tilde U_{\Psi,\mathrm b}$ built from $+\tilde{V}_{\Phi}$, and the inverse transformation is by $\tilde U_{\Psi,\mathrm b}^{\natural}$. The convention is stated because it is a genuine ambiguity — the oppositely-signed rotor implements the same Lorentz transformation on a different branch — and it is fixed here rather than left implicit.

The article is organized as follows. The next section recalls the free four-momentum. The section after that states the minimal-coupling prescription and derives the canonical momentum from the action. The following section separates the canonical and kinetic momenta. The next section derives the equation of motion. Two sections check it on a purely electric field and on a purely magnetic field. A short section records the proper-time restriction, and another fixes the boost convention. A section separates what the algebra supplies from what it only transcribes, and the article closes with open questions.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_\eta^2 = -e_t$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $\vec e_\mu$. The fixed-point subspaces are $\mathbb{B}_{\Phi}$ (anti-Hermitian, the material sector) and $\mathbb{B}_{\Psi}$ (Hermitian, the informational sector); $\mathbb{B}_{H}$ is the real-quaternion subspace and $\mathbb{B}_{C} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ is the complex scalar subspace, the centre of the algebra. The biquaternionic gradient is $\tilde{\nabla} = e_t\partial/\partial R_t + \vec e_x\partial/\partial R_x + \vec e_y\partial/\partial R_y + \vec e_z\partial/\partial R_z$, its quaternion conjugate is $\tilde{\nabla}^{\natural} = e_t\partial/\partial R_t - \vec e_x\partial/\partial R_x - \vec e_y\partial/\partial R_y - \vec e_z\partial/\partial R_z$, and $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla}$. The four-position is $\tilde R_\Phi = i r'_t\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ with $r'_t=c\,t'$ the temporal coefficient, a length, the four-velocity is $\tilde{V}_{\Phi} = \gamma(ic\,e_t + \vec v)$ with $\gamma = 1/\sqrt{1-\vec v^2/c^2}$, and the four-momentum is $\tilde{P}_{\Phi} = m\tilde{V}_{\Phi} = iE/c\,e_t + \vec p$; all live in $\mathbb{B}_{\Phi}$. The biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$, and the invariant pairing on $\mathbb{B}_{\Phi}$ is $\langle\tilde Q_3,\tilde Q_4\rangle = \mathrm{Sc}(\tilde Q_3\tilde Q_4^{\natural}) = -Q_{30}Q_{40} + \vec Q_3\cdot\vec Q_4$ for $\tilde Q_3 = iQ_{30}e_t + \vec Q_3$, $\tilde Q_4 = iQ_{40}e_t + \vec Q_4$. The four-potential is $\tilde{A}_{\Phi} = i\,a'_t\,e_t + \vec A \in \mathbb{B}_{\Phi}$ and the field strength is $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$, with four-current $\tilde J_{\Phi} = ic\rho\,e_t + \vec J$, source $\sqrt{\mu}\,\tilde{J}_{\Phi} = \frac{i\rho}{\sqrt{\epsilon}}e_t + \sqrt{\mu}\,\vec J$, and Maxwell equation $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}_{\Phi}$. The field tensor is $F_{\mu\nu} = \partial/\partial R_\mu A_\nu - \partial/\partial R_\nu A_\mu$, with $F_{0k} = iE_\eta/c$ and $F_{jk} = \epsilon_{j\eta l}B_l$ in the $i r'_t$ convention. Following the article *The Lorentz Force in Biquaternion Form*, the symbol $\tilde{F}$ is reserved for the field strength and the **four-force is written $\tilde{\mathcal F}_{\Phi,\mathrm{frc}}$**, so that $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = d\tilde{P}_{\Phi}/d\tau$ and $\tilde{\mathcal F}_{\Phi,\mathrm{frc}}\in\mathbb{B}_{\Phi}$. The dynamical equations are written against the clock $t'=r'_t/c$, in seconds, so that $\vec v=d\vec r/dt'$ and $\vec E=-\partial\vec A/\partial t'$; a rate that must keep the material coordinate carries the $c$ explicitly, $c\,d/dr'_t=d/dt'$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ its vacuum value; $\vec B = \mu\vec H$ is the magnetic induction. The plain form, read as the trace formula $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, is inherited unchanged.

## The Free Particle

The free four-momentum and its mass-shell condition are inherited from *Relativistic Mechanics in Biquaternionic Form* and are recalled only to fix what the coupling will modify. The four-velocity and four-momentum are

$$
\tilde{V}_{\Phi} = \gamma\left(ic\,e_t + \vec v\right), \qquad
\tilde{P}_{\Phi} = m\tilde{V}_{\Phi} = i\,\frac{E}{c}\,e_t + \vec p,
\qquad E = \gamma mc^2, \quad \vec p = \gamma m\vec v,
$$

and both lie in $\mathbb{B}_{\Phi}$. The four-momentum satisfies the **mass-shell relation**

$$
\langle\tilde{P}_{\Phi}\rangle_{\natural} = \tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = -\frac{E^2}{c^2} + \vec p^2 = -m^2c^2,
$$

equivalently $E^2 = \vec p^2c^2 + m^2c^4$. In the free theory the momentum that appears in the mass-shell relation is the particle's kinetic (mechanical) momentum, and it is also the canonical momentum conjugate to the four-position, because there is no potential to shift it. Minimal coupling is precisely the statement that this coincidence fails once $\tilde{A}_{\Phi}\neq 0$.

## The Minimal-Coupling Prescription

The prescription is stated on the mass-shell relation and then translated into the action. Both forms are used below.

### The mass-shell form

**Minimal coupling replaces the canonical four-momentum by $\tilde P_{\Phi,\mathrm{can}} - ϙ\tilde{A}_{\Phi}$ in the mass-shell relation:**

$$
\boxed{\;\left\langle\tilde P_{\Phi,\mathrm{can}} - ϙ\tilde{A}_{\Phi}\right\rangle_{\natural} = -m^2c^2\;}.
$$

Here the four-momentum before the replacement is the **canonical** four-momentum $\tilde P_{\Phi,\mathrm{can}}$, and the shifted object is the **kinetic (mechanical)** four-momentum $\tilde{P}_{\Phi,\mathrm{kin}}$. In the free theory the two coincide; the coupling is what separates them. To keep them apart we write

$$
\tilde{P}_{\Phi,\mathrm{kin}} := \tilde P_{\Phi,\mathrm{can}} - ϙ\tilde{A}_{\Phi}\ \text{(kinetic)}, \qquad
\tilde P_{\Phi,\mathrm{can}} = \tilde{P}_{\Phi,\mathrm{kin}} + ϙ\tilde{A}_{\Phi}\ \text{(canonical)},
$$

so that the prescription reads $\tilde P_{\Phi,\mathrm{can}} \to \tilde P_{\Phi,\mathrm{can}} - ϙ\tilde{A}_{\Phi}$, and the mass-shell condition becomes $\langle\tilde{P}_{\Phi,\mathrm{kin}}\rangle_{\natural} = -m^2c^2$. In the free limit $\tilde{A}_{\Phi}\to0$ the kinetic momentum reduces to the free symbol $\tilde{P}_{\Phi} = m\tilde{V}_{\Phi}$ of the preceding section, and the notation is consistent: $\tilde{P}_{\Phi,\mathrm{kin}}$ is what $\tilde{P}_{\Phi}$ becomes once the field is switched on.

Expanding in components, with $\tilde P_{\Phi,\mathrm{can}} = i(E_{\mathrm{can}}/c)\,e_t + \vec p_{\mathrm{can}}$ and $\tilde{A}_{\Phi} = i\,a'_t\,e_t + \vec A$,

$$
\tilde{P}_{\Phi,\mathrm{kin}} = i\,\frac{E_{\mathrm{can}} - ϙ\xi}{c}\,e_t + \left(\vec p_{\mathrm{can}} - ϙ\vec A\right)
= i\,\frac{E}{c}\,e_t + \vec p,
$$

so the scalar coefficient is the kinetic energy divided by $c$ and the vector coefficient is the kinetic three-momentum:

$$
E = E_{\mathrm{can}} - ϙ\xi, \qquad \vec p = \vec p_{\mathrm{can}} - ϙ\vec A.
$$

The mass-shell relation $\langle\tilde{P}_{\Phi,\mathrm{kin}}\rangle_{\natural} = -m^2c^2$ then reads

$$
-\frac{\left(E_{\mathrm{can}} - ϙ\xi\right)^2}{c^2} + \left(\vec p_{\mathrm{can}} - ϙ\vec A\right)^2 = -m^2c^2,
$$

that is,

$$
\left(E_{\mathrm{can}} - ϙ\xi\right)^2 = \left(\vec p_{\mathrm{can}} - ϙ\vec A\right)^2c^2 + m^2c^4 .
$$

Solving for the canonical energy gives the **relativistic Hamiltonian**

$$
\boxed{\;E_{\mathrm{can}} = ϙ\xi + c\sqrt{\left(\vec p_{\mathrm{can}} - ϙ\vec A\right)^2 + m^2c^2}\;}.
$$

This is the standard result: the potential energy $ϙ\xi$ is added, and the kinetic energy is built from the kinetic momentum $\vec p_{\mathrm{can}} - ϙ\vec A$, not from the canonical momentum $\vec p_{\mathrm{can}}$. The kinetic energy in the bracket is the one that would be computed for a free particle whose momentum is $\vec p = \vec p_{\mathrm{can}} - ϙ\vec A$.

### The action form and the canonical momentum

The same prescription is forced by the action. Let $\tau$ be the proper time. The action of a charged particle in a prescribed field is

$$
S = -mc\int\sqrt{-\langle\,d\tilde R_\Phi/d\tau\rangle_{\natural}}\,d\tau \;+\; ϙ\int \mathrm{Sc}\!\left(\tilde{A}_{\Phi}\,\overline{d\tilde R_\Phi/d\tau}\right)d\tau,
$$

with Lagrangian

$$
\mathrm{Lag} = -mc\sqrt{-\langle\,d\tilde R_\Phi/d\tau\rangle_{\natural}} \;+\; ϙ\,\mathrm{Sc}\!\left(\tilde{A}_{\Phi}\,\overline{d\tilde R_\Phi/d\tau}\right)
= -mc\sqrt{-\langle\,d\tilde R_\Phi/d\tau\rangle_{\natural}} \;+\; ϙ\left\langle \tilde{A}_{\Phi}, d\tilde R_\Phi/d\tau\right\rangle .
$$

The first term is the free point-particle Lagrangian of the parent article; the second is the coupling, and its sign is fixed below by the requirement that the canonical momentum come out positive. The conjugate momentum is the element of $\mathbb{B}_{\Phi}$ defined by the first variation, $\delta \mathrm{Lag} = \langle \tilde P_{\Phi,\mathrm{can}}, \delta\left(d\tilde R_\Phi/d\tau\right)\rangle$. For the free term, using $\delta \langle\,d\tilde R_\Phi/d\tau\rangle_{\natural} = 2\langle \,d\tilde R_\Phi/d\tau, \delta\left(d\tilde R_\Phi/d\tau\right)\rangle$ and the on-shell normalization $\langle\,d\tilde R_\Phi/d\tau\rangle_{\natural} = -c^2$,

$$
\delta\!\left(-mc\sqrt{-\langle\,d\tilde R_\Phi/d\tau\rangle_{\natural}}\right)
= \frac{mc}{\sqrt{-\langle\,d\tilde R_\Phi/d\tau\rangle_{\natural}}}\left\langle \,d\tilde R_\Phi/d\tau, \delta\left(d\tilde R_\Phi/d\tau\right)\right\rangle
= m\left\langle \,d\tilde R_\Phi/d\tau, \delta\left(d\tilde R_\Phi/d\tau\right)\right\rangle,
$$

so the free term contributes $m\,d\tilde R_\Phi/d\tau = \tilde{P}_{\Phi}$. The coupling contributes $ϙ\langle\tilde{A}_{\Phi}, \delta\left(d\tilde R_\Phi/d\tau\right)\rangle$, hence $ϙ\tilde{A}_{\Phi}$. The conjugate momentum is therefore

$$
\boxed{\;\tilde P_{\Phi,\mathrm{can}} = m\,d\tilde R_\Phi/d\tau + ϙ\tilde{A}_{\Phi} = \tilde{P}_{\Phi} + ϙ\tilde{A}_{\Phi}\;},
$$

that is, **canonical = kinetic + $ϙ\tilde{A}_{\Phi}$**, which is exactly the component statement above. The prescription $\tilde P_{\Phi} \to \tilde P_{\Phi} - ϙ\tilde A_{\Phi}$ of the mass-shell form and the conjugate momentum of the action form are the same equation read in opposite directions.

**Sign convention.** The pair of signs used here is the one inherited from the gauge-principle article: the covariant derivative is $D = \tilde{\nabla} +\frac{k_m\,i\,ϙ}{m\,c}\tilde{A}_{\Phi}$ with gauge transformation $\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi} - \tilde{\nabla}\Gamma$, and at the classical level the corresponding canonical/kinetic relation is $\tilde P_{\Phi,\mathrm{can}} = \tilde{P}_{\Phi,\mathrm{kin}} + ϙ\tilde{A}_{\Phi}$, equivalently $\tilde{P}_{\Phi,\mathrm{kin}} = \tilde P_{\Phi,\mathrm{can}} - ϙ\tilde{A}_{\Phi}$. This is the standard classical sign (the interaction Lagrangian is $-ϙ\xi + ϙ\vec A\cdot\vec v$ in laboratory time), and it is *not* silently reversed anywhere below. The corpus's field-theoretic sign conventions for the Dirac field are recorded in the minimal-coupling article; the classical statement here is the same prescription on the same connection.

## Canonical Momentum Is Not Kinetic Momentum

Once $\tilde{A}_{\Phi}\neq 0$, two four-vectors that coincide in the free theory separate, and the difference is physical.

**Gauge behaviour.** Under a gauge transformation of the connection, $\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi} - \tilde{\nabla}\Gamma$ with $\Gamma$ a real scalar, the kinetic momentum is unchanged,

$$
\tilde{P}_{\Phi,\mathrm{kin},2} = \tilde P_{\Phi,\mathrm{can},2} - ϙ\tilde{A}_{\Phi,2} = \left(\tilde P_{\Phi,\mathrm{can}} - ϙ\tilde{\nabla}\Gamma\right) - ϙ\left(\tilde{A}_{\Phi} - \tilde{\nabla}\Gamma\right) = \tilde P_{\Phi,\mathrm{can}} - ϙ\tilde{A}_{\Phi} = \tilde{P}_{\Phi,\mathrm{kin}},
$$

while the canonical momentum shifts:

$$
\tilde P_{\Phi,\mathrm{can},2} = \tilde{P}_{\Phi,\mathrm{kin}} + ϙ\tilde{A}_{\Phi,2} = \tilde P_{\Phi,\mathrm{can}} - ϙ\tilde{\nabla}\Gamma .
$$

So **the kinetic momentum is gauge-invariant and the canonical momentum is not.** A physical four-momentum cannot be gauge-dependent; the kinetic momentum is the physical one. The canonical momentum is the variable conjugated to position, and it is the variable in which the Hamiltonian is written; it inherits the gauge freedom of $\tilde{A}_{\Phi}$ and is not itself observable.

**Free limit.** If $\tilde{A}_{\Phi} = 0$ then $\tilde P_{\Phi,\mathrm{can}} = \tilde{P}_{\Phi,\mathrm{kin}} = \tilde{P}_{\Phi}$ and every statement below reduces to the free ones of the parent article. The distinction is created by the coupling, not by the formalism.

**A concrete case: the uniform magnetic field.** The cleanest display of the difference is a particle in a uniform magnetic field, where the canonical momentum has conserved components that the kinetic momentum does not. Take $\vec B = B_0\vec u_z$ and the Landau gauge

$$
\tilde{A}_{\Phi} = B_0 x\,\vec e_y, \qquad \text{i.e.} \qquad \vec A = B_0 x\,\vec u_y .
$$

The Lagrangian does not depend on $y$ or $z$, so the conjugate momenta $p_{\mathrm{can},y}$ and $p_{\mathrm{can},z}$ are conserved:

$$
p_{\mathrm{can},y} = p_y + ϙB_0 x = \text{const}, \qquad p_{\mathrm{can},z} = p_z = \text{const}.
$$

The kinetic momentum, by contrast, is not conserved: it rotates in the plane perpendicular to $\vec B$, since the equation of motion $d\vec p/dt' = ϙ\,\vec v\times\vec B$ with $\vec v = \vec pc^2/E$ is circular motion. The conserved quantities are the canonical components, the gauge-dependent ones; the kinetic momentum is the gauge-invariant one, and it is the one that turns. Both statements were checked numerically (see the companion), and they are not in tension: a gauge-dependent quantity may be conserved while a gauge-invariant quantity is not. The angular-momentum version of the same pair is the subject of the companion article *The Kinetic Momentum and the Algebra That Does Not Close*: there the conserved generator is the orbital angular momentum, the kinetic one does not commute with the Hamiltonian, and the bracket of the kinetic generators does not close.

**What the distinction is not.** It is not a statement that the canonical momentum is unphysical. The canonical momentum is the generator of translations of the field and the variable of the Hamiltonian; its conservation is what makes the problem integrable in the Landau gauge. The point is only that it is *not* the momentum that appears in the velocity, $\vec v = \vec p_{\mathrm{kin}}c^2/E_{\mathrm{kin}}$, and *not* the momentum that obeys the free mass-shell relation.

## The Equation of Motion

The equation of motion follows from the action by the Euler–Lagrange equations, and it is the Lorentz force. Written in components $\tilde R_\Phi = \sum_\mu Q_\mu e_\mu$ (with $Q_t = i r'_t$), $\tilde{A}_{\Phi} = \sum_\nu A_\nu e_\nu$, the Lagrangian is

$$
\mathrm{Lag} = -mc\sqrt{-\sum_\mu \left(dR_{\mu}/d\tau\right)^{2}} \;+\; ϙ\sum_\nu A_\nu(\tilde R_\Phi)\,dQ_{\nu}/d\tau,
\qquad dX_\mu/d\tau = dR_\mu/d\tau,
$$

because $\mathrm{Sc}(\tilde{A}_{\Phi}\overline{d\tilde R_\Phi/d\tau}) = \sum_\nu A_\nu\,dQ_{\nu}/d\tau$ in the $i r'_t$ convention. The conjugate momentum is the element $\tilde P_{\Phi,\mathrm{can}} = \sum_\mu P_{\mathrm{can},\mu}e_\mu$, with $P_{\mathrm{can},\mu} = \partial \mathrm{Lag}/\partial\left(dR_{\mu}/d\tau\right)$ and, using the on-shell normalization $\sqrt{-\sum_\mu\left(dR_{\mu}/d\tau\right)^{2}} = c$, $P_{\mathrm{can},0} = m\,dQ_{0}/d\tau + ϙA_0 = iE_{\mathrm{can}}/c$ and $P_{\mathrm{can},k} = m\,dQ_{\eta}/d\tau + ϙA_\eta = p_{\mathrm{can},k}$. Differentiating $P_{\mathrm{can},\mu}$ along the worldline and using the Euler–Lagrange equation $\frac{d}{d\tau}P_{\mathrm{can},\mu} = \partial \mathrm{Lag}/\partial R_\mu$,

$$
\frac{d}{d\tau}\left(mdR_{\mu}/d\tau + ϙA_\mu\right) = ϙ\sum_\nu \frac{\partial A_\nu}{\partial R_\mu}dQ_{\nu}/d\tau,
$$

and therefore

$$
\frac{d}{d\tau}\left(mdX_{\mu}/d\tau\right)
= ϙ\sum_\nu\left(\frac{\partial A_\nu}{\partial R_\mu} - \frac{\partial A_\mu}{\partial R_\nu}\right)dQ_{\nu}/d\tau
= ϙ\sum_\nu F_{\mu\nu}dX_{\nu}/d\tau .
$$

Since $mdX_{\mu}/d\tau = P_{\mathrm{kin},\mu}$ on shell and $dX_{\nu}/d\tau = U_\nu$, this is the standard contraction

$$
\boxed{\;\frac{dP_{\mathrm{kin},\mu}}{d\tau} = ϙ\,\sum_\nu F_{\mu\nu}U_\nu , \qquad \tilde{\mathcal F}_{\Phi,\mathrm{frc}} = \frac{d\tilde{P}_{\Phi,\mathrm{kin}}}{d\tau}\;}.
$$

The contraction $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = ϙ\,F(\tilde{V}_{\Phi})$ is an element of $\mathbb{B}_{\Phi}$, as it must be, and it is the **component form** of the Lorentz four-force. In components, with $F_{0k} = iE_\eta/c$ and $F_{jk} = \epsilon_{j\eta l}B_l$, the contraction is exactly the four-force of the read-list article,

$$
\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = i\,\frac{\gamma ϙ}{c}\left(\vec E\cdot\vec v\right)e_t + \gamma ϙ\left(\vec E + \vec v\times\vec B\right),
$$

whose scalar part is the power and whose vector part is the relativistic three-force. The equation was checked against this component form at random fields and velocities; the agreement is exact (to machine precision), not approximate.

**The biquaternion product form.** The same four-force has the representation, established in *The Lorentz Force in Biquaternion Form*, as the anti-Hermitian projection of the product of the four-velocity and the field strength:

$$
\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = -\,ϙ\sqrt{\mu}\;P_{\mathbb{B}_{\Phi}}\!\left(\tilde{V}_{\Phi}\tilde{F}\right),
\qquad
P_{\mathbb{B}_{\Phi}}(\tilde{Q}) = \tfrac{1}{2}\left(\tilde{Q} - \tilde{Q}^{*}\right).
$$

This article does not re-derive that formula; it records that the two routes agree, because the minimal-coupling contraction $ϙ\sum_\nu F_{\mu\nu}U_\nu$ and the projection formula are the same element of $\mathbb{B}_{\Phi}$. The minimal-coupling route exhibits the force as the derivative of a momentum; the product route exhibits it as a bilinear in $\tilde{V}_{\Phi}$ and $\tilde{F}$ that is manifestly covariant.

**Two structural consequences.** First, the force is orthogonal to the kinetic four-momentum. Differentiating the mass shell $\langle\tilde{P}_{\Phi,\mathrm{kin}}\rangle_{\natural} = -m^2c^2$ along the worldline gives

$$
\tilde{\mathcal F}_{\Phi,\mathrm{frc}}\tilde{P}_{\Phi}^{\natural}{}_{\mathrm{kin}} + \tilde{P}_{\Phi,\mathrm{kin}}\tilde{\mathcal F}_{\Phi,\mathrm{frc}}^{\natural} = 0,
$$

the biquaternion form of $\sum_\mu\varepsilon_\mu F_{\mathrm{lor},\mu} P_\mu = 0$: the Lorentz force rotates the four-momentum in $\mathbb{B}_{\Phi}$ but does not change its biquaternion norm, so the rest mass is preserved. Second, because $\tilde{\mathcal F}_{\Phi,\mathrm{frc}}=d\tilde{P}_{\Phi,\mathrm{kin}}/d\tau$ is a **proper-time** derivative, the equation is a statement about one worldline; the rest-mass preservation above is the statement that the norm of *that* four-momentum is constant, and it is not a conservation law for a system of bodies (see the closing section on the proper-time restriction).

## Case I: A Purely Electric Field

The first independent check is a purely electric field. This case is *not* the one that suggested the formula — the derivation above used a general field — but it isolates the scalar potential and the electric contribution to the force.

Take $\vec B = 0$ and a static, uniform electric field $\vec E = E_0\vec u_x$, described by the potential $\xi = -E_0 x$, $\vec A = 0$, so that $\tilde{A}_{\Phi} = -(iE_0/c)\,r_x\,e_t$. In this gauge the vector potential vanishes, so the canonical and kinetic momenta coincide in all three spatial components, $p_{\mathrm{can},k} = p_\eta$, and differ only in the time component: $E_{\mathrm{can}} = E + ϙ\xi$. The contraction $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = ϙ\sum_\nu F_{\mu\nu}U_\nu$ gives

$$
\boxed{\;\frac{d\vec p}{dt'} = ϙ\vec E = ϙE_0\,\vec u_x,
\qquad
\frac{dE}{dt'} = ϙ\,\vec E\cdot\vec v = ϙE_0\,v_x\;}.
$$

The first equation is exact and undamped by $\gamma$: the kinetic three-momentum grows linearly in laboratory time, $p_x = ϙE_0 t' = ϙE_0 r'_t/c$ for a particle released from rest at $t'=0$, and the energy follows from the mass shell,

$$
E(r'_t) = \sqrt{\left(ϙE_0r'_t/c\right)^2c^2 + m^2c^4},
\qquad
v_x(r'_t) = \frac{p_xc^2}{E} = \frac{ϙE_0 r'_t c}{\sqrt{\left(ϙE_0r'_t/c\right)^2c^2 + m^2c^4}},
$$

so the worldline is hyperbolic and $v_x\to c$ as $r'_t\to\infty$ without reaching it. The energy is not constant — an electric field does work — and its rate of change is the second equation above. The numerical solution of $d\vec p/dt' = ϙ\vec E$ with $\vec v = \vec pc^2/E$ reproduced $p_x = ϙE_0t'$ to the integration accuracy and the mass-shell energy exactly.

Two remarks. The relation $d\vec p/dt' = ϙ\vec E$ holds for the **kinetic** momentum; had one differentiated the canonical momentum $\vec p_{\mathrm{can}} = \vec p + ϙ\vec A$ instead, the vanishing of $\vec A$ in this gauge would hide the distinction, and a time-dependent $\vec A$ with $\vec B=0$ (a pure gauge field, or a field with $\vec E = -\partial\vec A/\partial t'$ would show it: then $\vec p_{\mathrm{can}}$ and $\vec p$ differ by $ϙ\vec A$, and the force equation is the one for $\vec p$, not for $\vec p_{\mathrm{can}}$. This is the electric-field face of the canonical/kinetic distinction.

## Case II: A Purely Magnetic Field

The second independent check is a purely magnetic field. This is the case in which the canonical and kinetic momenta differ most visibly, because the conserved canonical components coexist with a rotating kinetic momentum.

Take $\vec E = 0$ and a static, uniform magnetic induction $\vec B = B_0\vec u_z$. The contraction gives

$$
\frac{d\vec p}{dt'} = ϙ\,\vec v\times\vec B,
\qquad
\frac{dE}{dt'} = ϙ\,\vec E\cdot\vec v = 0 .
$$

The energy is constant, hence $\gamma$ and $|\vec p|$ are constant, and the motion in the plane perpendicular to $\vec B$ is circular with the relativistic cyclotron frequency

$$
\boxed{\;\omega_c = \frac{ϙB_0}{\gamma m}\;}.
$$

The field does no work: a pure magnetic field changes the direction of the kinetic momentum but not its magnitude or the energy. Both statements follow from the contraction alone, without solving the equations.

The canonical momentum behaves differently, as the preceding section anticipated. In the Landau gauge $\vec A = B_0x\,\vec u_y$, the components $p_{\mathrm{can},y} = p_y + ϙB_0x$ and $p_{\mathrm{can},z} = p_z$ are conserved, while the kinetic momentum $\vec p$ rotates: at any instant its components change, and only its magnitude is fixed. A numerical integration of $d\vec p/dt' = ϙ\vec v\times\vec B$ with $\vec v = \vec pc^2/E$ kept $E$ and $|\vec p|$ fixed to the integration accuracy, held $p_{\mathrm{can},y}$ and $p_{\mathrm{can},z}$ constant to machine precision, and produced the circular motion whose period is $2\pi/\omega_c$. This is the sharpest display of the article's main distinction: the conserved quantities are the gauge-dependent canonical components; the gauge-invariant kinetic momentum is not conserved.

**The two checks are independent.** The electric case tests the scalar-potential (time-component) part of the coupling, where the field does work; the magnetic case tests the vector-potential (space-component) part, where it does not. A formula fitted to one would not pass the other — the electric case would accept $d\vec p/dt' = ϙ\vec E + (\text{anything antisymmetric in }\vec v,\vec B)$ only if the magnetic term vanished for $\vec B=0$, and the magnetic case would accept a wrong coefficient of the electric term only if $\vec E=0$. The general derivation and the two cases agreeing on the *same* $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = ϙ\sum_\nu F_{\mu\nu}U_\nu$ is the content of the verification.

## The Proper-Time Restriction, Stated Explicitly

The equation of motion derived above is $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = d\tilde{P}_{\Phi,\mathrm{kin}}/d\tau$, a **proper-time** derivative, and for one particle in a prescribed field this is the correct and standard form. It is worth stating what it does *not* license, because the point has been recorded elsewhere in the corpus.

For two particles with different Lorentz factors $\gamma_1\neq\gamma_2$,

$$
\tilde{\mathcal F}_{\mathrm{frc},1} + \tilde{\mathcal F}_{\mathrm{frc},2} = \gamma_1\frac{d\tilde{P}_{\Phi,1}}{dt'} + \gamma_2\frac{d\tilde{P}_{\Phi,2}}{dt'}
\;\neq\; \frac{d}{dt'}\left(\tilde{P}_{\Phi,1} + \tilde{P}_{\Phi,2}\right),
$$

so the sum of four-forces is **not** the coordinate-time derivative of the total four-momentum, and $\tilde{\mathcal F}_{\mathrm{frc},1} + \tilde{\mathcal F}_{\mathrm{frc},2} = 0$ is not a conservation law. The collision exercise *Four-Momentum Conservation in a Collision* reports exactly this: the four-force symbol of the mechanics article cannot be carried to a multi-body system without the $\gamma$ factors, and the conservation law is a statement about the total four-momentum, not about the sum of proper-time derivatives. This article is the complementary case — **one** particle, whose four-force is correctly $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = d\tilde{P}_{\Phi,\mathrm{kin}}/d\tau$ — and it makes no conservation claim. The two articles do not disagree: the proper-time derivative is right for one worldline and insufficient for a sum of worldlines, and that is the whole of the matter.

## Frames and the Boost Rotor

The read-list article on the Lorentz transformation relates the boost biquaternion to the four-velocity,

$$
\tilde U_{\Psi,\mathrm b} = \sqrt{-\frac{i}{c}\,\tilde{V}_{\Phi}^{\natural}},
\qquad \tilde U_{\Psi,\mathrm b}\tilde U_{\Psi,\mathrm b}^{\natural} = e_t,
$$

with the boost direction $\vec u$ aligned with the particle velocity $\vec u_v$, and implements the transformation of a four-vector by rotor conjugation $\tilde{Q}_{\mathrm{lor}} = \tilde U_{\Psi,\mathrm b}\tilde{Q}\tilde U_{\Psi,\mathrm b}^{*}$.

**Convention, stated once.** The rotor built from $+\tilde{V}_{\Phi}$ carries the **laboratory to the moving (rest) frame**: acting on the four-velocity it gives

$$
\tilde U_{\Psi,\mathrm b}\,\tilde{V}_{\Phi}\,\tilde U_{\Psi,\mathrm b}^{*} = ic\,e_t,
$$

the four-velocity in the particle's rest frame, and the inverse transformation back to the laboratory is by the quaternion conjugate $\tilde U_{\Psi,\mathrm b}^{\natural}$. This was checked numerically on boosts along and off the coordinate axes, including the sign branch selected by $\mathrm{Sc}(\tilde U_{\Psi,\mathrm b})>0$; the rotor built by the same recipe from the velocity-reversed four-velocity $\tilde{V}_{\Phi}^{\natural} = \gamma(ic\,e_t - \vec v)$ carries the rest frame back to the laboratory and is the quaternion conjugate $\tilde U_{\Psi,\mathrm b}^{\natural} = \sqrt{-\frac{i}{c}\tilde{V}_{\Phi}}$. The convention matters because the two choices are not related by a relabelling of $\vec v$ alone — the sign branch and the direction of the transformation can be confused — and it is fixed here so that every use of $\tilde U_{\Psi,\mathrm b}$ below is unambiguous.

With that convention the four-velocity, the four-momentum, and the four-force all transform by the **vector** rule, $\tilde{Q}_{\mathrm{lor}} = \tilde U_{\Psi,\mathrm b}\tilde{Q}\tilde U_{\Psi,\mathrm b}^{*}$, because all three lie in $\mathbb{B}_{\Phi}$. The field strength does **not**: it transforms by the **bivector** rule $\tilde{F}_2 = \tilde U_{\Psi,\mathrm b}^{\natural}\tilde{F}\tilde U_{\Psi,\mathrm b}$, the same rule used in the Lorentz-force article. The product formula $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = -ϙ\sqrt{\mu}\,P_{\mathbb{B}_{\Phi}}(\tilde{V}_{\Phi}\tilde{F})$ is covariant under the *pair* of rules, and the minimal-coupling equation $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = d\tilde{P}_{\Phi,\mathrm{kin}}/d\tau$ is covariant because both sides are four-vectors. In the particle's rest frame, where $\tilde{V}_{\Phi} = ic\,e_t$, the force reduces to $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = ϙ\,\vec E_{\mathrm{rest}}$, the rest-frame electric field; this is the frame in which the electric and magnetic contributions to the force are cleanly separated, and it uses the convention above.

**A rotor that grows in time.** The rotor used here is fixed. The rest-to-lab rotor $\tilde U^{\natural}$ carried along the worldline, and allowed to depend on proper time, is the **eigenspinor** of the companion article *The Eigenspinor: The Lorentz Rotor as a Function of Proper Time*, and the equation of motion of this article is then its linear evolution equation $d\tilde U/d\tau = \tfrac12\vec\Omega_{\mathrm{LT}}\tilde U$ with $\vec\Omega_{\mathrm{LT}} = -(ϙ/m)\tilde{F}^{*}$ and the rest-to-lab sign. In a uniform field the eigenspinor integrates in closed form and reproduces the two cases below as its degenerate limits; in a general field it is a path-ordered exponential. The cross-reference is recorded here because the fixed rotor of this section is the special case $\tilde U(0)$ of the evolving one, and the two articles should be read together.

## What the Framework Supplies and What It Only Transcribes

**Supplied by the algebra.**

- *A single home for the four-vectors of the problem.* The four-position, four-velocity, kinetic four-momentum, canonical four-momentum, four-potential, and four-force all lie in the same four-dimensional real subspace $\mathbb{B}_{\Phi}$, and the minimal-coupling shift $\tilde P_{\Phi,\mathrm{can}} = \tilde{P}_{\Phi,\mathrm{kin}} + ϙ\tilde{A}_{\Phi}$ is an equation inside that subspace.
- *A constraint, not an extra postulate.* The mass-shell relation $\langle\tilde{P}_{\Phi,\mathrm{kin}}\rangle_{\natural} = -m^2c^2$ is the biquaternion-norm condition on $\mathbb{B}_{\Phi}$; with minimal coupling it *is* the relativistic Hamiltonian, and it delivers both the canonical/kinetic relation and the form of the energy in one equation.
- *A canonical momentum from the action.* The conjugate momentum $\tilde P_{\Phi,\mathrm{can}} = \tilde{P}_{\Phi} + ϙ\tilde{A}_{\Phi}$ follows from the first variation of the biquaternion action with the pairing $\langle\tilde{A}_{\Phi},d\tilde R_\Phi/d\tau\rangle$, with no index apparatus.
- *The form of the force.* The contraction $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = ϙ\sum_\nu F_{\mu\nu}U_\nu$ reassembles into the $\mathbb{B}_{\Phi}$-valued four-force, and it agrees with the projection formula $ -ϙ\sqrt{\mu}\,P_{\mathbb{B}_{\Phi}}(\tilde{V}_{\Phi}\tilde{F})$ of the Lorentz-force article.

**Only transcribed.** The minimal-coupling *principle* itself — that the canonical four-momentum should be replaced by $\tilde P_{\Phi,\mathrm{can}} - ϙ\tilde{A}_{\Phi}$ — is not derived from the algebra; it is the standard prescription carried into it, and the algebra supplies a home and a compact expression rather than a reason. The sign conventions are inherited from the parent articles and are conventions, not results. The non-relativistic limit likewise reproduces the Newtonian Lorentz force, as it must, and does not test the relativistic part of the construction.

**Interpretation.** Reading $\tilde{A}_{\Phi}$ as a connection and $\tilde{P}_{\Phi,\mathrm{kin}} = \tilde P_{\Phi,\mathrm{can}} - ϙ\tilde{A}_{\Phi}$ as the horizontal (gauge-covariant) momentum is a geometric interpretation of an algebraic statement; the algebra supplies the statement, and the bundle picture is a consistent interpretation of it, as in the gauge-principle and covariant-derivative articles. The claim here is not that the algebra forces the geometric interpretation.

**Gaps, left visible.** The extension to a *dynamical* field (in which $\tilde{A}_{\Phi}$ obeys its own equation and the particle back-reacts) is not treated; that is a field-theoretic problem. The many-body conservation law is not treated (it belongs to the exercise and to *Noether's Theorem in Biquaternionic Form*). The relation of the classical canonical momentum to the quantized momentum of the canonical-quantization articles is not pursued.

## Open Questions

1. **Radiation reaction.** The field here is prescribed and does no back-reaction on the particle. What is the biquaternion form of the self-force of an accelerated charge, and does the algebra's structure (the null cone as the zero-divisor set) simplify the Larmor or Abraham–Lorentz analysis?

2. **The Lagrangian and Hamiltonian in the presence of a dynamical field.** The action written here couples the particle to a fixed connection. What is the joint action of particle and field, and does its biquaternion form exhibit the canonical structure more cleanly than the four-vector form?

3. **The canonical momentum and quantization.** The canonical momentum is the variable of the Hamiltonian and the natural quantization variable. How does the biquaternion canonical momentum of this article relate to the quantized momenta of the canonical-quantization articles, and does the sector assignment (which article finds $\tilde{A}_{\Phi}\in\mathbb{B}_{\Phi}$ with a conjugate momentum in $\mathbb{B}_{\Psi}$) appear already at the level of the classical particle?

4. **Gauge choice and integrability.** In the uniform magnetic field the Landau gauge makes two canonical components conserved. Is there a biquaternion-natural gauge criterion — a condition on $S = \mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A}_{\Phi})$ or on the field strength — that selects the separable gauge for a given field, and is it the same as the standard one?

5. **The sign of the charge and the corpus's conventions.** The classical relation $\tilde P_{\Phi,\mathrm{can}} = \tilde{P}_{\Phi,\mathrm{kin}} + ϙ\tilde{A}_{\Phi}$ and the corpus's covariant derivative $D = \tilde{\nabla} +\frac{k_m\,i\,ϙ}{m\,c}\tilde{A}_{\Phi}$ have been aligned here by the standard classical signs. Is there a corpus-wide convention that fixes the relative sign of the phase $\lambda = \exp(\frac{k_m\,i\,ϙ\,\Gamma}{m\,c})$ and the classical canonical momentum once and for all, or is it irreducibly a choice of the sign of $ϙ$?

6. **Empirical content.** As everywhere in the framework, the unresolved question is whether any of this yields a prediction distinguishing it from standard relativistic electrodynamics. The construction as presented is a reformulation.

## Summary

A particle of charge $ϙ$ and rest mass $m$ in a prescribed external field is described in biquaternionic form by the **minimal-coupling prescription**, the replacement of the canonical four-momentum by $\tilde P_{\Phi,\mathrm{can}} \to \tilde P_{\Phi,\mathrm{can}} - ϙ\tilde{A}_{\Phi}$ in the mass-shell relation:

$$
\left\langle\tilde P_{\Phi,\mathrm{can}} - ϙ\tilde{A}_{\Phi}\right\rangle_{\natural} = -m^2c^2.
$$

The object $\tilde P_{\Phi,\mathrm{can}} - ϙ\tilde{A}_{\Phi}$ is the **kinetic** four-momentum and $\tilde P_{\Phi,\mathrm{can}}$ is the **canonical** four-momentum, $\tilde P_{\Phi,\mathrm{can}} = \tilde{P}_{\Phi,\mathrm{kin}} + ϙ\tilde{A}_{\Phi}$. The prescription has two faces, and they agree: on the mass-shell relation it yields the relativistic Hamiltonian $E_{\mathrm{can}} = ϙ\xi + c\sqrt{(\vec p_{\mathrm{can}}-ϙ\vec A)^2 + m^2c^2}$; on the action $S = -mc\int\sqrt{-\langle d\tilde R_\Phi/d\tau\rangle_{\natural}}\,d\tau + ϙ\int\mathrm{Sc}(\tilde{A}_{\Phi}\,\overline{d\tilde R_\Phi/d\tau})\,d\tau$ it yields the conjugate momentum $\tilde P_{\Phi,\mathrm{can}} = m\,d\tilde R_\Phi/d\tau + ϙ\tilde{A}_{\Phi}$. The two distinctions that carry the physical content are that the **kinetic momentum is gauge-invariant** and the **canonical momentum is not**, and that the kinetic, not the canonical, momentum is the one that obeys the free mass-shell relation and appears in the velocity $\vec v = \vec pc^2/E$.

The equation of motion is the Lorentz force in its contracted form,

$$
\boxed{\;\frac{dP_{\mathrm{kin},\mu}}{d\tau} = ϙ\,\sum_\nu F_{\mu\nu}U_\nu,
\qquad
\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = \frac{d\tilde{P}_{\Phi,\mathrm{kin}}}{d\tau}
= -\,ϙ\sqrt{\mu}\;P_{\mathbb{B}_{\Phi}}\!\left(\tilde{V}_{\Phi}\tilde{F}\right)\;},
$$

with $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = i\frac{\gamma ϙ}{c}(\vec E\cdot\vec v)e_t + \gamma ϙ(\vec E+\vec v\times\vec B)$ in components. It preserves the rest mass, $\tilde{\mathcal F}_{\Phi,\mathrm{frc}}\tilde{P}_{\Phi}^{\natural}{}_{\mathrm{kin}} + \tilde{P}_{\Phi,\mathrm{kin}}\tilde{\mathcal F}_{\Phi,\mathrm{frc}}^{\natural} = 0$, and it is a proper-time equation about a single worldline. Two independent cases were checked — a purely electric field, where $d\vec p/dt' = ϙ\vec E$ and the field does work, and a purely magnetic field, where $d\vec p/dt' = ϙ\vec v\times\vec B$, the energy is constant, and the motion is circular at $\omega_c = ϙB_0/(\gamma m)$ — together with the general contraction at random fields. The two cases test the time-like and space-like parts of the coupling separately, so agreement on both is not agreement on the general case.

The algebra supplies the common home $\mathbb{B}_{\Phi}$ of the four-vectors, the biquaternion-norm mass shell that doubles as the Hamiltonian, the conjugate momentum of the action, and the reassembly of the contraction into the four-force; it does not supply the minimal-coupling principle itself, the sign conventions, or the geometric interpretation, which are carried in or interpreted. The proper-time form is correct for this single-particle problem and is explicitly not a many-body conservation law, and the boost rotor is fixed by the convention that its $+\vec v$ branch carries the laboratory to the moving frame.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\mu^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_{H}$, $\mathbb{B}_{C}$ | Real-quaternion subspace; complex scalar subspace (centre) |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm |
| $\langle\tilde Q_3,\tilde Q_4\rangle = \mathrm{Sc}(\tilde Q_3\tilde Q_4^{\natural})$ | Invariant pairing on $\mathbb{B}_{\Phi}$ |
| $\tilde R_\Phi = i r'_t\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | Four-position |
| $\tilde{V}_{\Phi} = \gamma(ic\,e_t + \vec v)$ | Four-velocity, $\langle\tilde{V}_{\Phi}\rangle_{\natural} = -c^2$ |
| $\tilde{P}_{\Phi} = m\tilde{V}_{\Phi} = iE/c\,e_t + \vec p$ | Kinetic four-momentum, $\langle\tilde{P}_{\Phi}\rangle_{\natural} = -m^2c^2$ |
| $\tilde{A}_{\Phi} = i\,a'_t\,e_t + \vec A$ | Four-potential (material-sector connection) |
| $\tilde P_{\Phi,\mathrm{can}} = \tilde{P}_{\Phi} + ϙ\tilde{A}_{\Phi} = i(E_{\mathrm{can}}/c)\,e_t + \vec p_{\mathrm{can}}$ | Canonical four-momentum (gauge-dependent) |
| $\tilde{P}_{\Phi,\mathrm{kin}} = \tilde P_{\Phi,\mathrm{can}} - ϙ\tilde{A}_{\Phi} = \tilde{P}_{\Phi}$ | Kinetic four-momentum (gauge-invariant) |
| $ϙ$ | Charge (coupling constant, not fixed by the algebra) |
| $\langle\tilde{P}_{\Phi,\mathrm{kin}}\rangle_{\natural} = -m^2c^2$ | Minimal-coupling mass-shell relation |
| $E_{\mathrm{can}} = ϙ\xi + c\sqrt{(\vec p_{\mathrm{can}} - ϙ\vec A)^2 + m^2c^2}$ | Canonical energy; $\vec p_{\mathrm{can}}$ the canonical three-momentum |
| $F_{\mu\nu} = \partial/\partial R_\mu A_\nu - \partial/\partial R_\nu A_\mu$ | Field tensor; $F_{0k} = iE_\eta/c$, $F_{jk} = \epsilon_{j\eta l}B_l$ |
| $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ | Field-strength biquaternion |
| $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = d\tilde{P}_{\Phi,\mathrm{kin}}/d\tau$ | Four-force; $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = ϙ\sum_\nu F_{\mu\nu}U_\nu = -ϙ\sqrt{\mu}P_{\mathbb{B}_{\Phi}}(\tilde{V}_{\Phi}\tilde{F})$ |
| $P_{\mathbb{B}_{\Phi}}(\tilde{Q}) = \tfrac12(\tilde{Q} - \tilde{Q}^{*})$ | Projection onto $\mathbb{B}_{\Phi}$ |
| $\tilde U_{\Psi,\mathrm b} = \sqrt{-\frac{i}{c}\tilde{V}_{\Phi}^{\natural}}$ | Boost rotor; $+\vec v$ branch: laboratory to moving frame |
| $\gamma = 1/\sqrt{1-\vec v^2/c^2}$ | Lorentz factor |
| $\omega_c = ϙB_0/(\gamma m)$ | Relativistic cyclotron frequency |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Trace reading of the plain form on the informational sector |

## Further Reading

- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the canonical momentum, the Lorentz force, and the motion of a charge in uniform electric and magnetic fields.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the relativistic Hamiltonian, the minimal-coupling form of the interaction, and cyclotron motion.
- Herbert Goldstein, Charles Poole, and John Safko, *Classical Mechanics* (Addison-Wesley, 2002), for the Lagrangian and Hamiltonian formulation of a charged particle in an external field.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1958), for the minimal substitution and the canonical-momentum convention in the quantum theory.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the spacetime-algebra treatment of the Lorentz force and the gauge-covariant derivative.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of Lorentz transformations and the geometric interpretation of minimal coupling.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the biquaternion algebra with the even subalgebra of $\mathrm{Cl}_{1,3}$.
- Companion articles: [Relativistic Mechanics in Biquaternionic Form](relativistic-mechanics-in-biquaternionic-form.html); [The Lorentz Force in Biquaternion Form](the-lorentz-force-in-biquaternion-form.html); [The Lorentz Transformation as a Biquaternionic Rotation](the-lorentz-transformation-as-a-biquaternionic-rotation.html); [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html); [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html); [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html); [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html); [Exercise: Four-Momentum Conservation in a Collision](exercise-four-momentum-conservation-in-a-collision.html); [The Relativistic Two-Body Problem in Biquaternionic Form](the-relativistic-two-body-problem-in-biquaternionic-form.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html).
