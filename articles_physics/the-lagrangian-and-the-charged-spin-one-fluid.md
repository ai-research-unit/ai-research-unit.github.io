# __The Lagrangian and the Charged Spin-One Fluid__

## Introduction

The Proca action has a derivative term and an algebraic one; the coupling replaces $\partial_{\imath}$ by $D_{\imath}$ in the first and cannot touch the second, because the second is the magnitude's and a connection reaches derivatives. So the charged spin-one fluid keeps its pressure and loses its continuity, which is the reverse of what the other charged articles of this layer do.

*First, the free decomposition of the field strength survives with one word changed.* $F=r\,\omega+\mathrm{d}r\wedge u$ becomes $F=r\,\Omega+\mathrm{d}r\wedge u$ with $\Omega_{\imath\jmath}=D_{\imath} u_{\jmath}-D_{\jmath} u_{\imath}$: the vorticity becomes the covariant one, the density's gradient's term is untouched, and the rank stays two. The substitution is $\mathrm{d}\to D$ in one place and the structure is preserved.

*Second, the Lorenz condition ceases to be continuity and this is the article's main statement.* At the free rung $\sum_{\imath}\varepsilon_{\imath}\partial_{\imath} A_{\imath}=0$ is $\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}(ru_{\imath})=0$, the conservation of a real density by a real flow. Charged, the condition is $\sum_{\imath}\varepsilon_{\imath} D_{\imath} A_{\imath}=0$, and written with the ordinary divergence it carries a source that is phase-carrying and imaginary. The condition survives and its fluid reading does not: the density is no longer conserved by the flow alone, and the fluid is compressible by the field's action.

*Third, the mass term is coupling-blind, so the four statements it carried at the free rung become three.* It still removes the field's own shift freedom, still supplies the condition, still fixes the pressure to a constant. What it can no longer do is make that condition a conservation law.

Position in the block. This is the variational companion of [The Charged Spin-One Fluid](the-charged-spin-one-fluid.html) and the eighth and last of the articles of this layer. It is the only one in which the coupling degrades a statement rather than adding a force, and the only one in which the free rung's cleanest result is lost.

## Conventions

The conventions are restated here so that every sign below is checkable from this page alone. $A_{\imath}$ is complex, $F_{\imath\jmath}=D_{\imath} A_{\jmath}-D_{\jmath} A_{\imath}$, $D_{\imath}=\partial_{\imath}+\frac{2\pi iϙ}{h}A^{\mathrm{ext}}_{\imath}$, $\nu_m=\frac{mc}{h}$; $\mathcal L=-\frac14\sum_{\imath,\jmath}F^{*}_{\imath\jmath}F_{\imath\jmath}-\frac{4\pi^{2}\nu_m^{2}}{2}\sum_{\imath}\varepsilon_{\imath} A^{*}_{\imath} A_{\imath}$ in the corpus's signs, every index low. The external potential is written $\tilde A_\Phi=i a'_t e_t+\vec A$ and the coupling is $ϙ$, with $q=-ϙ$. The carrier's parameters are eight real ones; [The Charged Spin-One Fluid](the-charged-spin-one-fluid.html) records the doubling and this article does not re-derive it.

## The Action in the Fluid Variables

The derivative term is rebuilt and the algebraic term is not.

$$
\mathcal L=-\frac{1}{4}\sum_{\imath,\jmath}F^{*}_{\imath\jmath}F_{\imath\jmath}-\frac{4\pi^{2}\nu_m^{2}}{2}\lvert A\rvert^{2}
\;\longrightarrow\;
\mathcal L_{\mathrm{gco}}=-\frac{1}{4}F^{\mathrm{gco}*}_{\imath\jmath}F^{\mathrm{gco}}_{\imath\jmath}-\frac{4\pi^{2}\nu_m^{2}}{2}\lvert A\rvert^{2},
\qquad
F^{\mathrm{gco}}_{\imath\jmath}=D_{\imath} A_{\jmath}-D_{\jmath} A_{\imath} .
$$

$\lvert A\rvert^{2}$ carries no derivative, so no substitution reaches it; the connection is in $D$ and there is no $D$ there. This is the layer's one constant: in all four charged articles the coupling reaches derivatives and not magnitudes, and here the magnitude is the whole of the algebraic term.

Writing $A_{\imath}$ as a magnitude and a direction, $F^{\mathrm{gco}}=r\,\Omega+\mathrm{d}r\wedge u$ with

$$
\Omega_{\imath\jmath}=D_{\imath} u_{\jmath}-D_{\jmath} u_{\imath},
$$

and the identity behind the split is algebraic: $F(D)(r u)=r\,(Du)+\mathrm{d}r\wedge u$ for every connection. The free article's three pieces therefore survive: the covariant vorticity times the density, the density's gradient wedged with the velocity, and the cross term.

At the free rung $\omega=\mathrm{d}u$ and the vorticity is the direction's curl; here $\Omega=Du$ and the vorticity carries the connection. The fluid's rotation is no longer a property of the direction alone, and the difference is the field strength's contribution to it — which is the opposite of what happens at the scalar rung, where the coupling *is* the vorticity. The two are not in contradiction: the scalar velocity is a gradient and the vector velocity is a direction, so a connection shifts the first into the field and folds itself into the second.

The covariant vorticity of the congruence is the projected curl, $\Omega^{\perp}_{\imath\jmath}=\sum_{\alpha,\beta}\mathsf{P}_{\imath\alpha}\mathsf{P}_{\jmath\beta}\Omega_{\alpha\beta}$ with $\mathsf{P}_{\imath\jmath}=g_{\imath\jmath}+u_{\imath} u_{\jmath}$, and it annihilates $u$ by construction; a two-form on three dimensions is simple, so the rank is two wherever $\vec\Omega\ne0$. **The raw covariant curl is not transverse, and compatibility with the norm is not what would make it so**: $\sum_{\jmath}\varepsilon_{\jmath}\Omega_{\imath\jmath}u_{\jmath}=-\sum_{\jmath}\varepsilon_{\jmath} u_{\jmath} D_{\jmath} u_{\imath}$, the covariant acceleration, which is orthogonal to the flow because the norm is preserved and not because the curl is.

## The Variation

The chart's action is the free one with two covariant rates and with the mass block unchanged. Varying the density gives the continuity equation with the covariant phase rate; varying the phase gives the transport; varying the frame's angles gives the spin's transport and the two vanishing momenta $\varrho$ and $\theta_{\mathrm{rpd}}$ carry; varying the connection gives the Maxwell equation with the current as its source. No Lagrange multiplier appears, because the word is an exact parameterisation and the frame's unit conditions hold identically.

The covariant derivative carries the connection, which is fixed in the variation of the matter fields, so the integration by parts touches only the field's own derivatives and produces the usual surface term, killed by compact support.

The mass block has no derivative, so the scalar part of the connection's equation is the only constraint the system has; it is derived in the next section and it is not imposed here. The variation is what makes the distinction between an equation and a constraint visible: both are Euler–Lagrange equations of the same functional, and the difference is which coordinate they determine.

## The Constraints the Action Imposes: The Lorenz Condition Ceases to Be Continuity

Taking the covariant divergence of the field equation,

$$
\sum_{\jmath}\varepsilon_{\jmath} D_{\jmath} F_{\mathrm{gco},\jmath\imath}=4\pi^{2}\nu_m^{2}A_{\imath}
\qquad\Longrightarrow\qquad
0=\sum_{\jmath}\varepsilon_{\jmath} D_{\imath} D_{\jmath} F_{\mathrm{gco},\jmath\imath}=4\pi^{2}\nu_m^{2}\,\sum_{\imath}\varepsilon_{\imath} D_{\imath} A_{\imath},
$$

the first equality being the antisymmetry of $F$ and the second the field equation. So the condition is $\sum_{\imath}\varepsilon_{\imath} D_{\imath} A_{\imath}=0$, exactly as at the free rung with $\partial\to D$.

Written with the ordinary divergence, the condition has a source.

$$
\sum_{\imath}\varepsilon_{\imath} D_{\imath} A_{\imath}=0
\qquad\Longleftrightarrow\qquad
\sum_{\imath}\varepsilon_{\imath}\partial_{\imath} A_{\imath}=-\frac{2\pi iϙ}{h}\sum_{\imath}\varepsilon_{\imath} A_{\mathrm{ext},\imath}A_{\imath},
$$

and the right-hand side is not zero, is imaginary, and carries the carrier's phase. **That is the precise sense in which the condition ceases to be continuity**: the left-hand side is the divergence of the field and would be the flow's density balance, and the right-hand side is a source the flow does not supply.

[The Charged Spin-One Fluid](the-charged-spin-one-fluid.html) writes $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A)=-\frac{2\pi iϙ}{h}r^{2}e^{2i\theta_{\mathrm{pha}}}$: the divergence is imaginary, it is proportional to the coupling, and it carries twice the phase. Read as a continuity equation it says that the fluid's density is not conserved by the flow, and the $e^{2i\vartheta}$ says that what spoils the conservation is not a real rate but a phase-carrying quantity — a source that is not a scalar.

*The free rung's cleanest result is gone.* There the Lorenz condition was continuity and the fluid's continuity was the mass's gift; here the condition is a constraint that the flow cannot satisfy alone.

*The compressibility's origin is now visible and it is not the mass's.* At the free rung $\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}(ru_{\imath})=0$; charged, $\sum_{\imath}\varepsilon_{\imath}\partial_{\imath} A_{\imath}$ is the source. The difference is the connection's, so **the free fluid's incompressibility is the mass's gift and the charged fluid's compressibility is the charge's.**

*The count of equations changes in one place.* The free rung had four field components, four equations, and one of them a consequence of the others through an identity. The charged rung has the same four and the same identity, and the consequence is now a condition with a source rather than a conservation law. The count is the same and the content is not.

## The Structural Consequence: What the Mass Term Still Does

Three statements, and each is unchanged.

*It removes the field's own shift freedom.* $A_{\imath}\mapsto A_{\imath}+\partial_{\imath}\Gamma$ is not a symmetry of $\mathcal L_{\mathrm{gco}}$ at $\nu_m\ne0$, because $\lvert A\rvert^{2}$ is not invariant; and the coupling does not restore it, because $D\partial\Gamma\ne\partial$ unless $\Gamma$ is constant in the gauge-covariant sense.

*It supplies the condition.* The derivation above uses the mass term's coefficient: with $\nu_m=0$ the identity $\partial\partial F=0$ stands alone and says nothing about $A$.

*It fixes the stiffness.* The algebraic term is $\frac{\nu_m^{2}}{2}\lvert A\rvert^{2}$, and the pressure is read off it as at the free rung: energy density and pressure are equal, $\epsilon=p=\frac{4\pi^{2}\nu_m^{2}}{2}r^{2}$. **The charged spin-one fluid is stiff at both rungs, and the coupling does not touch the stiffness**, because the algebraic term carries no derivative for the connection to enter.

What the mass term no longer does is make the condition a conservation law. That is the fourth statement of the free rung and it is not available, for the reason the previous section gives: the source is there whether or not the mass is.

And the coupling does not break the external gauge symmetry. Under $A\mapsto\lambda A$ with $\lambda=\exp(\frac{2\pi iϙ\Gamma}{h})$ and $A^{\mathrm{ext}}_{\imath}\mapsto A^{\mathrm{ext}}_{\imath}-\partial_{\imath}\Gamma$, both terms are invariant: the derivative term because $D$ is, the algebraic term because $\lvert\lambda\rvert^{2}=1$. Two different freedoms must be kept apart: the field's own shift, which the mass breaks at both rungs, and the external group's phase rotation, which is a symmetry at the charged rung and is what makes the carrier complex.

## The Structural Consequence: What the Carrier's Doubling Costs

The free carrier has four real parameters; the charged one has eight, and the action says which term sees which. The block's charged article records the doubling and this article states its location: the derivative term sees all eight, the algebraic term sees one combination of them — the magnitude — and the external gauge redundancy removes one.

The density and the direction are therefore not enough to describe the carrier, and that is the difference from the other charged articles. At the scalar rung the carrier is one complex number and the fluid's variables exhaust it; at the spinor rung the carrier is one biquaternion and the word's eight parameters exhaust it; **here the carrier is a complex vector, the fluid's variables are a magnitude and a direction, and the count does not close.** The balance is the phase and the imaginary part of the direction, and the action puts the phase in the derivative term only.

The consequence for what the fluid reading can be is a boundary and the article states it as one. [The Charged Spin-One Fluid](the-charged-spin-one-fluid.html) finds that the free incompressibility is revealed as the mass's gift, that the condition ceases to be continuity, and that the carrier doubles. A reader who wants to know whether the charged Proca field has a fluid reading at all is being told: it has a fluid reading of its magnitude and direction, and the carrier has four parameters more than those two supply. Whether the extra four can be read as a second fluid — a second density with its own phase — is not settled anywhere in the corpus.

## The Noether Currents: Charge, Spin and Stress

Three currents, and the constraint removes part of one. The charge current is $q\rho_{\mathrm{chg}}$ and $q\rho_{\mathrm{chg}}\vec v$ with the mechanical velocity; the spin current is the rotor's momentum, $-\frac{h}{2\pi} c\,\varrho^{2}\sinh\theta_{\mathrm{rpd}}\,\hat n_{\mathrm{rot}}$, transported by the flow; the stress is the translation current of the chart's Lagrangian.

What the constraint does to them. The Lorenz condition is the scalar part of the connection's equation, so it constrains the charge current's divergence and not the spin's. The spin current is conserved by the rotor's equation alone, and the mass term does not break its conservation — it changes what the spin means, by making the longitudinal polarisation physical.

The sign. The charge is $q\rho_{\mathrm{chg}}$ with $\rho_{\mathrm{chg}}=\varrho^{2}\cosh\theta_{\mathrm{rpd}}>0$, so the sign is $q$'s. The spin's sign is negative, the frame's, and the two signs are independent: a positive charge can carry a spin pointing either way. That independence is the reason the article treats the two currents separately and does not fold them into one.

## What the Principle Adds and What It Relabels: In the Fluid Chart

Adds. The location of the coupling in the action: the derivative term and not the algebraic one, hence the pressure's survival and the continuity's loss. The decomposition $F=r\Omega+\mathrm{d}r\wedge u$ as an algebraic identity with $D$ in place of $\mathrm{d}$, and with it the statement that the vorticity's source has changed while its structure has not. The condition's loss of its fluid reading, stated as the source term that $\partial\cdot A$ acquires. The separation of the two gauge freedoms. And the count's failure to close, located at the carrier's complex structure.

Does not add. No new equation. No new fluid: the reading of the magnitude and the direction survives and does not extend. No statement about the extra four parameters beyond their location. No thermodynamics. No quantum potential, at either rung, since the Proca action has no second derivative of the magnitude.

The layer's ledger, in one sentence per article. The scalar first-order rung has one substitution in two brackets; the scalar relativistic rung has a substitution that meets the shell; the spinor rung has a substitution whose image is the phase and the boost and never the rotor; the vector rung has a substitution that reaches the derivative term and leaves the pressure alone and takes the continuity away. Four charged articles, one connection, four different reaches — and the reaches are read off the connection's type in the algebra, which is the same argument in all four.

## What the Principle Adds and What It Relabels: The Fluid Alone

A charge and a constraint in the same fluid, and the article's claim is that they do not interact. The coupled Proca fluid has a charge because the phase is coupled, and it has a constraint because the scalar part of the conjugate gradient vanishes. The fluid reading is where the two are seen to be independent: the charge is the phase's conjugate, the constraint is the frame's, and neither equation contains the other.

What it adds: the constraint as a statement about the flow. In the element reading the constraint is a variation's result; in the fluid reading it says that **the fluid's velocity has no component along the direction the mass fixes**. That is a kinematic statement about a flow, and the article's section on the constraint is where it is made.

What it adds: the charge's frame independence under coupling. The connection enters the phase's bracket and the scale's bracket and not the frame's, so the charge density is the density and the current is the shifted gradient. The element reading has the same statement as a type fact; the fluid reading has it as the statement that the frame does not carry charge, which is the sentence the article's comparison section contains.

What it adds: the potential's two pressures. The temporal slot couples to the density through the rapidity and the spatial slot through the boost, so the coupling is a longitudinal pressure and a transverse one in the fluid's frame. The two are different pressures because the two slots have different types, and the article says so once.

What it does not add. No new equation. Every fluid equation is the element article's, and the first paragraph says so.

What it inherits. The constraint's exactness, the absent mass in the charge, and the frame's constrained character. **It does not inherit a torque**, because the spin-one fluid's frame is not a density of angular momentum, and the article's one sentence about that separates it from the spin-half family.

## Open Questions

The extra four parameters. Whether the carrier's remaining freedom can be read as a second fluid, with its own density and phase, is not settled.

## Summary

The action. $\mathcal L_{\mathrm{gco}}=-\frac14F^{\mathrm{gco}*}F^{\mathrm{gco}}-\frac{4\pi^{2}\nu_m^{2}}{2}\lvert A\rvert^{2}$: the derivative term rebuilt with $D$, the algebraic term untouched.

The decomposition. $F^{\mathrm{gco}}=r\,\Omega+\mathrm{d}r\wedge u$ with $\Omega=Du$; the vorticity is covariant and rank two, its transversality being the projection's and not the curl's; the density's gradient's term is unchanged.

The condition. $\sum_{\imath}\varepsilon_{\imath} D_{\imath} A_{\imath}=0$ still follows from the field equation, and written with the ordinary divergence it has a phase-carrying imaginary source. Continuity is lost and the fluid is compressible by the field's action.

The mass. Three of its four free statements survive: it breaks the field's own shift, supplies the condition, fixes the pressure. It no longer makes the condition a conservation law.

The carrier. Eight real parameters against the fluid's four; the action puts the coupling in the derivative term only, and the count's balance is the phase.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A_{\imath}$ | The complex Proca field; eight real parameters |
| $D_{\imath}=\partial_{\imath}+\frac{2\pi iϙ}{h}A^{\mathrm{ext}}_{\imath}$ | The covariant derivative; abelian |
| $F^{\mathrm{gco}}_{\imath\jmath}=D_{\imath} A_{\jmath}-D_{\jmath} A_{\imath}$ | The covariant field strength |
| $r$, $u_{\imath}$ | Magnitude and direction; $\sum_{\imath}\varepsilon_{\imath} u_{\imath} u_{\imath}=-1$ |
| $\Omega_{\imath\jmath}=D_{\imath} u_{\jmath}-D_{\jmath} u_{\imath}$ | Covariant curl, contracting to minus the covariant acceleration; its projection is the vorticity and is rank two |
| $F^{\mathrm{gco}}=r\,\Omega+\mathrm{d}r\wedge u$ | The decomposition of the field strength |
| $\lvert A\rvert^{2}$ | The algebraic term's argument; coupling-blind |
| $\nu_m=\frac{mc}{h}$ | Mass wave number |
| $ϙ$ | Coupling; minus the electric charge |
| $\lambda=\exp(\frac{2\pi iϙ\Gamma}{h})$ | The external gauge element; a symmetry |
| $\theta_{\mathrm{pha}}$ | The carrier's phase; appears squared in the divergence |
| $\mathcal L_{\mathrm{gco}}$ | The Lagrangian density in the fluid variables with the connection |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Alexandru Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs," *Journal de Physique et le Radium* **7** (1936) 347–353, for the massive vector field and the condition its mass implies.
- Wolfgang Pauli, "Relativistic field theories of elementary particles," *Reviews of Modern Physics* **13** (1941) 203–232, for the constraint counting of a massive vector field and the fate of its gauge freedom.
- John R. Oppenheimer and Julian S. Schwinger, "On the interaction of mesotrons and nuclear particles," *Physical Review* **60** (1941) 150, for the constraint structure of a massive vector coupled to an external field.
- Friedrich W. Hehl, "On the kinematics of the torsion of space-time," *Foundations of Physics* **15** (1985) 451–471, for a unit vector's covariant vorticity, its transversality and its rank.
- The companion articles: [The Lagrangian and the Coupled Proca Equation in Polar Variables](the-lagrangian-and-the-coupled-proca-equation-in-polar-variables.html), the same action in the chart and the branch's role; [The Charged Spin-One Fluid](the-charged-spin-one-fluid.html), the equations and the divergence $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A)=-\frac{2\pi iϙ}{h}r^{2}e^{2i\theta_{\mathrm{pha}}}$; [The Lagrangian and the Spin-One Fluid](the-lagrangian-and-the-spin-one-fluid.html), the free rung where the condition is continuity; and [The Lagrangian and the Charged Spin-Half Fluid](the-lagrangian-and-the-charged-spin-half-fluid.html), the rung where the coupling reaches neither the density's nor the spin's norm.
