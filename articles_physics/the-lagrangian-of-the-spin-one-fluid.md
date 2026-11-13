# The Lagrangian of the Spin-One Fluid

## Introduction

**At this rung the fluid's variables are the field's own, and the action's mass term does double work.** The Proca field is $A_\mu=r\,u_\mu$: a magnitude and a direction, which are a density and a velocity. So the fluid is not a reading of a polar decomposition imposed from outside — it is the field's own parameterisation, and the action written in it is the Proca action and nothing else.

**Three results.**

*First, one term of the action does two things, and they are the same thing.* The mass term $\frac{k_m^{2}}{2}r^{2}$ removes the gauge freedom and supplies the Lorenz condition; the Lorenz condition in the fluid's variables is $\partial_\mu(ru^{\mu})=0$, which is continuity. **The Proca fluid's continuity is the replacement for its lost gauge freedom**, and both come from one term.

*Second, the density's variation and the direction's variation are the longitudinal and transverse parts of the field equation, and the Lorenz condition is neither: it is their consequence*, by the identity $\partial_\mu\partial_\nu F^{\nu\mu}=0$. The action therefore explains the block's phrase that the free incompressibility is the mass's gift: without the mass the identity has nothing to balance, and the condition does not arise.

*Third, this is the only action in the layer with no $\hbar$ in its derivative term, and correspondingly the only fluid in the block whose acceleration law has no quantum force.* The polar decomposition of a vector field produces no second derivative of the magnitude, and the action says why: $A=ru$ has one derivative and the Lagrangian is quadratic in it.

**Position in the block.** This is the variational companion of [The Spin-One Fluid of the Biquaternion Proca Field](the-spin-one-fluid-of-the-biquaternion-proca-field.html) and the seventh of the eight articles of this layer. It is the only one in which a Lagrange multiplier is genuinely needed, and the only one whose fluid is not a quantum fluid.

**Conventions.** $A_\mu=r\,u_\mu$ with $r>0$ and $u_\mu u^\mu=-1$; the temporal slot carries the $i$, so $A_\mu A^\mu=-r^{2}$. $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$; $k_m=mc/\hbar$; $\mathcal L=-\frac14F_{\mu\nu}F^{\mu\nu}-\frac{k_m^{2}}{2}A_\mu A^\mu$ in the corpus's signature, whose Euler–Lagrange equation is $\partial_\nu F^{\nu\mu}=k_m^{2}A^\mu$. The transverse derivative is $\nabla_\mu=\Delta_\mu{}^\nu\partial_\nu$ with $\Delta_{\mu\nu}=g_{\mu\nu}+u_\mu u_\nu$.

## The Action in the Field's Own Variables

**One substitution, and the field strength splits into a magnitude's part and a direction's part.** Since $A=ru$,

$$
F_{\mu\nu}=r\,\omega_{\mu\nu}+\bigl(\partial_\mu r\bigr)u_\nu-\bigl(\partial_\nu r\bigr)u_\mu,
\qquad
\omega_{\mu\nu}=\partial_\mu u_\nu-\partial_\nu u_\mu .
$$

**Three pieces, and each has a name in the fluid's language.** The first is the direction's vorticity times the density; the second and third are the density's gradient wedged with the velocity. The field strength therefore carries two independent objects: **the flow's vorticity and the density's gradient**, and the Proca fluid is the only one in this layer whose field strength is made of the fluid's own derivatives rather than of a potential's.

**The Lagrangian, with the mass term expanded.**

$$
\mathcal L=\frac{1}{2}\Bigl[\bigl(\partial_\mu r\bigr)^{2}-\bigl(u^\mu\partial_\mu r\bigr)^{2}\Bigr]-\frac{r^{2}}{4}\omega_{\mu\nu}\omega^{\mu\nu}-r\,\omega_{\mu\nu}\bigl(\partial^\mu r\bigr)u^\nu+\frac{k_m^{2}}{2}r^{2},
$$

obtained by expanding $-\frac14F^{2}$ and using $u^{2}=-1$. Four terms: the density's gradient energy, the vorticity's energy, a cross term, and the mass.

**The cross term is what makes the free Proca fluid's acceleration law as short as the block's.** $a_\mu=-\nabla_\mu\ln r-r^{-1}E_\mu$ has no quantum force because the two pieces of $F$ are first derivatives and no second derivative of $r$ survives the variation; the cross term is where the density's gradient and the vorticity meet, and it is the term that turns the field equation into a statement about the flow's acceleration.

**There is no $\hbar$ anywhere in the derivative terms.** The only place the quantum of action appears is inside $k_m$. So this rung's fluid is not a Madelung fluid: it is a classical field read as a medium, and the block's article says as much by giving an acceleration law with no quantum potential.

## The Mass Term Does Two Things

**The Euler–Lagrange equation is the field equation, and its divergence is an identity on one side.**

$$
\partial_\nu F^{\nu\mu}=k_m^{2}A^\mu
\qquad\Longrightarrow\qquad
0=\partial_\mu\partial_\nu F^{\nu\mu}=k_m^{2}\,\partial_\mu A^\mu,
$$

because $F$ is antisymmetric. **The Lorenz condition is therefore a consequence of the equation and not a condition imposed on it, and it exists exactly when $k_m\ne0$.**

**The same term removes the gauge freedom.** With $k_m=0$ the action is invariant under $A_\mu\mapsto A_\mu+\partial_\mu\Gamma$; with $k_m\ne0$ it is not, because the mass term is not. **One term supplies the condition and destroys the freedom the condition replaces**, and the two statements are the same statement seen from two sides: a massless vector has a redundancy and no condition, a massive one has a condition and no redundancy, and the count of physical components is the same in both cases.

**In the fluid's variables the condition is continuity.** With $A_\mu=r\,u_\mu$,

$$
\partial_\mu A^\mu=0
\qquad\Longleftrightarrow\qquad
\partial_\mu\bigl(r\,u^\mu\bigr)=0,
$$

which is the continuity equation for a density $r$ and a velocity $u^\mu$. **The Proca fluid therefore has a continuity equation that is not an equation of motion**: it is the integrability of the field equation, and it disappears with the mass.

**The block's phrase is exact and the action explains it.** [The Spin-One Fluid of the Biquaternion Proca Field](the-spin-one-fluid-of-the-biquaternion-proca-field.html) finds that the fluid's free incompressibility is the mass's gift. The action's version: nothing in the derivative terms forces $\partial_\mu(ru^\mu)$ to vanish, and the identity $\partial_\mu\partial_\nu F^{\nu\mu}=0$ has no right-hand side to balance until the mass supplies one. **The incompressibility is not a property of the flow; it is a property of the pair $(r,u)$ and of the mass.**

**And the flow's own expansion is not zero.** Differentiating $ru^\mu$ gives $\partial_\mu u^\mu=-u^\mu\partial_\mu\ln r$, so the velocity's divergence is the density's logarithmic derivative along the flow. The divergence-free object is the field, and reading it as continuity is what makes the density and the velocity into a fluid's.

## The Two Variations and the Multiplier

**The density's variation is the field equation contracted with the flow, and the direction's variation is its transverse part.** That is the cleanest way to state the pair, and it follows from the split of $\delta A_\mu=u_\mu\,\delta r+r\,\delta u_\mu$ into a longitudinal and a transverse piece.

The $r$ variation gives $u_\mu(\partial_\nu F^{\nu\mu}-k_m^{2}A^\mu)=0$, since $\partial F/\partial r$ along $u$ is the contraction; the $\delta u$ variation, restricted to $u\cdot\delta u=0$, gives the transverse part, $\Delta_{\mu}{}^{\nu}(\partial_\lambda F^{\lambda}{}_{\nu}-k_m^{2}A_\nu)=0$. **The two together are the field equation and neither alone is.**

**The unit condition is the one place in this layer where a multiplier is genuinely needed.** The word's parameterisation absorbs the unit conditions of the boost and the rotor — a unit element is a unit for every value of its parameters — but the Proca direction is a unit by declaration and not by parameterisation: $u_\mu$ is three functions subject to one constraint, and the constraint must be imposed. Written with a multiplier,

$$
\mathcal L_{\lambda}=\mathcal L+\lambda\bigl(u_\mu u^\mu+1\bigr),
$$

and the multiplier enters the direction's equation as $\lambda u_\mu$, which is a force along the flow. **It plays the part a pressure plays in an incompressible fluid**, and the analogy is exact in one respect: it is the constraint's force and not the fluid's own.

**The contrast with the spin article is worth recording.** There the parameterisation removed the need for a multiplier and the constraints appeared as vanishing momenta; here the parameterisation cannot remove it and the constraints appear as a projection. **The difference is that a unit rotor has three parameters and a unit vector has two plus one constraint**: the word's frame is a group element, and a direction is a coset.

## What the Fluid Form Adds to the Block's Account

**Three statements, and the block makes each of them in the equations' language.**

*The vorticity is the direction's, and it is not the field strength.* $\omega=\mathrm{d}u$ and $F=r\,\mathrm{d}u+\mathrm{d}r\wedge u$, so the field strength carries the vorticity plus the density's gradient, and only in a region of constant density are the two the same object. The block's article states the vorticity and the self-dual split; the action states the decomposition that produces both.

*The rank of $\omega$ is two, and the reason is the dimension of the rest space.* The vorticity of a congruence is the curl projected onto the plane orthogonal to the flow, $\omega^{\perp}_{\mu\nu}=\Delta_\mu{}^\alpha\Delta_\nu{}^\beta\omega_{\alpha\beta}$ with $\Delta_{\mu\nu}=g_{\mu\nu}+u_\mu u_\nu$: $\omega^{\perp}$ annihilates $u$ by construction, and a two-form supported on three dimensions is simple, so its rank is at most two and is two wherever the vorticity is non-zero. **The raw curl is a different object, and its contraction with the flow is the acceleration**: $\omega_{\mu\nu}u^\nu=-a_\mu$, so $\mathrm{d}u$ is neither transverse nor always simple — the block's sentence that $\omega\wedge\omega=0$ for every unit timelike flow holds for $\omega^{\perp}$ and not for $\mathrm{d}u$. The first-order charged fluid has rank two for the other reason, that a three-vector curl cannot make a four-dimensional two-form; the spinor fluid's is rank two for every solution, as its own article establishes.

*The equation of state is the mass term's, and the action shows it as the only term without a derivative.* The mass term $\frac{k_m^{2}}{2}r^{2}$ is the one term in the action that carries the density and no gradient, and it fixes the pressure in one line: the energy density it contributes is $\epsilon=\frac{k_m^{2}}{2}r^{2}$ and the force it exerts is $-\nabla\ln r$, so $\mathrm{d}p/(\epsilon+p)=\mathrm{d}\ln r$ and $p=\epsilon$. **A Proca fluid is stiff, and the stiffness is the mass's**, which is the block's reading of the acceleration law; the action's addition is that no other law is available, because no other term of the action is free of derivatives.

## What the Fluid Variational Principle Adds and Does Not Add

**Adds.** The mass term's double role, stated once: it removes the gauge freedom and supplies the condition that replaces it, and in the fluid's variables that condition is continuity. The pair of variations as the field equation's longitudinal and transverse parts, with the Lorenz condition as their consequence by an identity. The multiplier's necessity and its reading as a pressure. The decomposition of the field strength into vorticity and density gradient. And the reason this rung has no quantum force: the action has no second derivative of the magnitude.

**Does not add.** No new equation: the four components are the field's. No new current: the Proca current is $k_m^{2}A^\mu$ up to the normalisation, and it is the field. No gauge invariance to discuss, because the mass removed it. No thermodynamics, and no quantum potential, since this rung has none. And no statement about the massless limit's fluid reading, which the block's article explicitly denies.

**The one thing the action says that the equations cannot.** The Lorenz condition, the loss of gauge freedom, the continuity equation and the stiffness of the flow are four statements about four different objects, and in the action they are one term. **That is the strongest case in the layer for writing the fluid's Lagrangian**: not a new result, but the location of four results in one coefficient.

## Open Questions

1. **The massless limit.** The action's derivative terms survive at $k_m=0$ and the fluid reading does not, because the field becomes pure gauge and $A=ru$ is then a gauge-dependent split. Whether some gauge-fixed chart makes the limit continuous is not settled, and the block's article denies the reading without stating the obstruction in these terms.

2. **The constraint's class.** Whether the unit condition and the transverse projection produce a second-class system with a Dirac bracket that closes — the Proca fluid's analogue of the spin article's open problem — is not computed here.

3. **The multiplier's sign.** $\lambda$ is determined by the equations and its sign is the density's gradient's, so a region of decreasing density has a negative pressure in this reading. Whether that is physical or an artefact of the split is not settled.

## Summary

**The action.** $\mathcal L=\frac12[(\partial r)^{2}-(u\cdot\partial r)^{2}]-\frac{r^{2}}{4}\omega^{2}-r\,\omega_{\mu\nu}\partial^{\mu}r\,u^{\nu}+\frac{k_m^{2}}{2}r^{2}$, with $A=ru$ and $u^{2}=-1$.

**The mass term.** It removes the gauge freedom, supplies the Lorenz condition, and in the fluid's variables that condition is continuity $\partial_\mu(ru^\mu)=0$. One term, four statements.

**The variations.** The density's is the field equation's longitudinal part, the direction's its transverse part, and the Lorenz condition is their consequence by $\partial\partial F=0$.

**The multiplier.** The only genuine one in the layer; it is the unit condition's force and plays a pressure's part.

**The quantum sector.** Absent: no $\hbar$ in the derivative terms, no quantum potential, no quantum force. The Proca fluid is a classical field read as a medium.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A_\mu=r\,u_\mu$ | The field in the fluid's variables; $r$ the density, $u$ the velocity |
| $r>0$ | Density; the field's magnitude |
| $u_\mu$, $u_\mu u^\mu=-1$ | Unit four-velocity; three functions and one constraint |
| $\omega_{\mu\nu}=\partial_\mu u_\nu-\partial_\nu u_\mu$ | The raw curl, whose contraction with $u$ is $-a_\mu$; its projection $\omega^{\perp}$ is the vorticity and is rank two |
| $F_{\mu\nu}=r\omega_{\mu\nu}+\partial_\mu r\,u_\nu-\partial_\nu r\,u_\mu$ | The field strength; vorticity plus density gradient |
| $k_m=mc/\hbar$ | Mass wave number; the only place $\hbar$ appears |
| $\nabla_\mu=\Delta_\mu{}^\nu\partial_\nu$ | Transverse derivative; $\Delta_{\mu\nu}=g_{\mu\nu}+u_\mu u_\nu$ |
| $\lambda$ | Multiplier of the unit condition; a pressure |
| $E_\mu=F_{\mu\nu}u^\nu$ | The electric part along the flow |
| $a_\mu=u^\nu\partial_\nu u_\mu$ | The flow's acceleration |
| $\mathcal L$ | The Proca Lagrangian in the fluid variables |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Alexandru Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs," *Journal de Physique et le Radium* **7** (1936) 347–353, for the massive vector field and the condition its mass implies.
- John R. Oppenheimer and Julian S. Schwinger, "On the interaction of mesotrons and nuclear particles," *Physical Review* **60** (1941) 150, for the massive vector field's constraint structure.
- Clifford Truesdell and Richard Toupin, "The classical field theories," in *Handbuch der Physik* III/1 (Springer, 1960), for the polar decomposition of a vector field into magnitude and direction and the strain it induces.
- Friedrich W. Hehl, "On the kinematics of the torsion of space-time," *Foundations of Physics* **15** (1985) 451–471, for a unit vector field's vorticity, its transversality and its rank.
- The companion articles: [The Variational Principle and the Proca Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-proca-equation-in-biquaternionic-polar-variables.html), the same action in the chart and the branch's role; [The Spin-One Fluid of the Biquaternion Proca Field](the-spin-one-fluid-of-the-biquaternion-proca-field.html), the acceleration law without a quantum force and the Lorenz condition read as continuity; [The Third Polarization and the Self-Dual Split of the Massive Field Strength](the-third-polarization-and-the-self-dual-split-of-the-massive-field-strength.html), for the decomposition of $F$ that the substitution produces; and the charged companion [The Lagrangian of the Charged Proca Fluid](the-lagrangian-of-the-charged-proca-fluid.html), where the connection's divergence stops being zero and the condition stops being continuity.
