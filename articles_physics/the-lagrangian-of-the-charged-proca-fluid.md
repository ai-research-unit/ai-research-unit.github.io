# The Lagrangian of the Charged Proca Fluid

## Introduction

**The connection enters one of the two terms and it enters it as a derivative.** The Proca action has a derivative term and an algebraic one; the coupling replaces $\partial_\mu$ by $D_\mu$ in the first and cannot touch the second, because the second is the magnitude's and a connection reaches derivatives. **So the charged Proca fluid keeps its pressure and loses its continuity**, which is the reverse of what the other charged articles of this layer do.

**Three results.**

*First, the free decomposition of the field strength survives with one word changed.* $F=r\,\omega+\mathrm{d}r\wedge u$ becomes $F=r\,\Omega+\mathrm{d}r\wedge u$ with $\Omega_{\mu\nu}=D_\mu u_\nu-D_\nu u_\mu$: the vorticity becomes the covariant one, the density's gradient's term is untouched, and the rank stays two. **The substitution is $\mathrm{d}\to D$ in one place and the structure is preserved.**

*Second, the Lorenz condition ceases to be continuity and this is the article's main statement.* At the free rung $\partial_\mu A^\mu=0$ is $\partial_\mu(ru^\mu)=0$, the conservation of a real density by a real flow. Charged, the condition is $D_\mu A^\mu=0$, and written with the ordinary divergence it carries a source that is phase-carrying and imaginary. **The condition survives and its fluid reading does not**: the density is no longer conserved by the flow alone, and the fluid is compressible by the field's action.

*Third, the mass term is coupling-blind, so the four statements it carried at the free rung become three.* It still removes the field's own shift freedom, still supplies the condition, still fixes the pressure to a constant. What it can no longer do is make that condition a conservation law.

**Position in the block.** This is the variational companion of [The Charged Proca Fluid](the-charged-proca-fluid.html) and the eighth and last of the articles of this layer. It is the only one in which the coupling degrades a statement rather than adding a force, and the only one in which the free rung's cleanest result is lost.

**Conventions.** $A_\mu$ is complex, $F_{\mu\nu}=D_\mu A_\nu-D_\nu A_\mu$, $D_\mu=\partial_\mu+\frac{iϙ}{\hbar}A^{\mathrm{ext}}_\mu$, $k_m=mc/\hbar$; $\mathcal L=-\frac14F^{*}_{\mu\nu}F^{\mu\nu}-\frac{k_m^{2}}{2}A^{*}_\mu A^\mu$ in the corpus's signature. The external potential is written $\tilde A_\Phi=i a'_t e_t+\vec A$ and the coupling is $ϙ$, with $q=-ϙ$. The carrier's parameters are eight real ones; [The Charged Proca Fluid](the-charged-proca-fluid.html) records the doubling and this article does not re-derive it.

## The Action in the Fluid Variables

**The derivative term is rebuilt and the algebraic term is not.**

$$
\mathcal L=-\frac{1}{4}F^{*}_{\mu\nu}F^{\mu\nu}-\frac{k_m^{2}}{2}\lvert A\rvert^{2}
\;\longrightarrow\;
\mathcal L_{\mathrm{gco}}=-\frac{1}{4}F^{\mathrm{gco}*}_{\mu\nu}F^{\mathrm{gco}\,\mu\nu}-\frac{k_m^{2}}{2}\lvert A\rvert^{2},
\qquad
F^{\mathrm{gco}}_{\mu\nu}=D_\mu A_\nu-D_\nu A_\mu .
$$

**The second term is the same term.** $\lvert A\rvert^{2}$ carries no derivative, so no substitution reaches it; the connection is in $D$ and there is no $D$ there. **This is the layer's one constant: in all four charged articles the coupling reaches derivatives and not magnitudes**, and here the magnitude is the whole of the algebraic term.

**The first term's decomposition is the free one with $\mathrm{d}$ replaced by $D$.** Writing $A_\mu$ as a magnitude and a direction, $F^{\mathrm{gco}}=r\,\Omega+\mathrm{d}r\wedge u$ with

$$
\Omega_{\mu\nu}=D_\mu u_\nu-D_\nu u_\mu,
$$

and the identity behind the split is algebraic: $F(D)(r u)=r\,(Du)+\mathrm{d}r\wedge u$ for every connection. **The free article's three pieces therefore survive**: the covariant vorticity times the density, the density's gradient wedged with the velocity, and the cross term.

**What changes is the vorticity's definition and hence its source.** At the free rung $\omega=\mathrm{d}u$ and the vorticity is the direction's curl; here $\Omega=Du$ and the vorticity carries the connection. **The fluid's rotation is no longer a property of the direction alone**, and the difference is the field strength's contribution to it — which is the opposite of what happens at the scalar rung, where the coupling *is* the vorticity. The two are not in contradiction: the scalar velocity is a gradient and the vector velocity is a direction, so a connection shifts the first into the field and folds itself into the second.

**The rank is still two, and the reason is still the dimension of the rest space.** The covariant vorticity of the congruence is the projected curl, $\Omega^{\perp}_{\mu\nu}=\Delta_\mu{}^\alpha\Delta_\nu{}^\beta\Omega_{\alpha\beta}$ with $\Delta_{\mu\nu}=g_{\mu\nu}+u_\mu u_\nu$, and it annihilates $u$ by construction; a two-form on three dimensions is simple, so the rank is two wherever $\vec\Omega\ne0$. **The raw covariant curl is not transverse, and compatibility with the norm is not what would make it so**: $\Omega_{\mu\nu}u^\nu=-u^\nu D_\nu u_\mu$, the covariant acceleration, which is orthogonal to the flow because the norm is preserved and not because the curl is.

## The Lorenz Condition Ceases to Be Continuity

**The identity survives and the conclusion changes.** Taking the covariant divergence of the field equation,

$$
D_\nu F^{\mathrm{gco}\,\nu\mu}=k_m^{2}A^\mu
\qquad\Longrightarrow\qquad
0=D_\mu D_\nu F^{\mathrm{gco}\,\nu\mu}=k_m^{2}\,D_\mu A^\mu,
$$

the first equality being the antisymmetry of $F$ and the second the field equation. So the condition is $D_\mu A^\mu=0$, exactly as at the free rung with $\partial\to D$.

**Written with the ordinary divergence, the condition has a source.**

$$
D_\mu A^\mu=0
\qquad\Longleftrightarrow\qquad
\partial_\mu\bigl(A^\mu\bigr)=-\frac{iϙ}{\hbar}A^{\mathrm{ext}}_\mu A^\mu,
$$

and the right-hand side is not zero, is imaginary, and carries the carrier's phase. **That is the precise sense in which the condition ceases to be continuity**: the left-hand side is the divergence of the field and would be the flow's density balance, and the right-hand side is a source the flow does not supply.

**The block's display is this statement in the algebra.** [The Charged Proca Fluid](the-charged-proca-fluid.html) writes $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde A)=-\frac{iϙ}{\hbar}r^{2}e^{2i\vartheta_{\mathrm{pha}}}$: the divergence is imaginary, it is proportional to the coupling, and it carries twice the phase. **Read as a continuity equation it says that the fluid's density is not conserved by the flow**, and the $e^{2i\vartheta}$ says that what spoils the conservation is not a real rate but a phase-carrying quantity — a source that is not a scalar.

**Three consequences, and the article states them as losses.**

*The free rung's cleanest result is gone.* There the Lorenz condition was continuity and the fluid's continuity was the mass's gift; here the condition is a constraint that the flow cannot satisfy alone.

*The compressibility's origin is now visible and it is not the mass's.* At the free rung $\partial_\mu(ru^\mu)=0$; charged, $\partial_\mu(A^\mu)$ is the source. The difference is the connection's, so **the free fluid's incompressibility is the mass's gift and the charged fluid's compressibility is the charge's.**

*The count of equations changes in one place.* The free rung had four field components, four equations, and one of them a consequence of the others through an identity. The charged rung has the same four and the same identity, and the consequence is now a condition with a source rather than a conservation law. **The count is the same and the content is not.**

## What the Mass Term Still Does

**Three statements, and each is unchanged.**

*It removes the field's own shift freedom.* $A_\mu\mapsto A_\mu+\partial_\mu\Gamma$ is not a symmetry of $\mathcal L_{\mathrm{gco}}$ at $k_m\ne0$, because $\lvert A\rvert^{2}$ is not invariant; and the coupling does not restore it, because $D\partial\Gamma\ne\partial$ unless $\Gamma$ is constant in the gauge-covariant sense.

*It supplies the condition.* The derivation above uses the mass term's coefficient: with $k_m=0$ the identity $\partial\partial F=0$ stands alone and says nothing about $A$.

*It fixes the stiffness.* The algebraic term is $\frac{k_m^{2}}{2}\lvert A\rvert^{2}$, and the pressure is read off it as at the free rung: energy density and pressure are equal, $\epsilon=p=\frac{k_m^{2}}{2}r^{2}$. **The charged Proca fluid is stiff at both rungs, and the coupling does not touch the stiffness**, because the algebraic term carries no derivative for the connection to enter.

**What the mass term no longer does is make the condition a conservation law.** That is the fourth statement of the free rung and it is not available, for the reason the previous section gives: the source is there whether or not the mass is.

**And the coupling does not break the external gauge symmetry.** Under $A\mapsto\lambda A$ with $\lambda=\exp(iϙ\Gamma/\hbar)$ and $A^{\mathrm{ext}}_\mu\mapsto A^{\mathrm{ext}}_\mu-\partial_\mu\Gamma$, both terms are invariant: the derivative term because $D$ is, the algebraic term because $\lvert\lambda\rvert^{2}=1$. **Two different freedoms must be kept apart**: the field's own shift, which the mass breaks at both rungs, and the external group's phase rotation, which is a symmetry at the charged rung and is what makes the carrier complex.

## What the Carrier's Doubling Costs

**The free carrier has four real parameters; the charged one has eight, and the action says which term sees which.** The block's charged article records the doubling and this article states its location: the derivative term sees all eight, the algebraic term sees one combination of them — the magnitude — and the external gauge redundancy removes one.

**The density and the direction are therefore not enough to describe the carrier, and that is the difference from the other charged articles.** At the scalar rung the carrier is one complex number and the fluid's variables exhaust it; at the spinor rung the carrier is one biquaternion and the word's eight parameters exhaust it; **here the carrier is a complex vector, the fluid's variables are a magnitude and a direction, and the count does not close.** The balance is the phase and the imaginary part of the direction, and the action puts the phase in the derivative term only.

**The consequence for what the fluid reading can be is a boundary and the article states it as one.** [The Charged Proca Fluid](the-charged-proca-fluid.html) finds that the free incompressibility is revealed as the mass's gift, that the condition ceases to be continuity, and that the carrier doubles. A reader who wants to know whether the charged Proca field has a fluid reading at all is being told: **it has a fluid reading of its magnitude and direction, and the carrier has four parameters more than those two supply.** Whether the extra four can be read as a second fluid — a second density with its own phase — is not settled anywhere in the corpus.

## What the Fluid Variational Principle Adds and Does Not Add

**Adds.** The location of the coupling in the action: the derivative term and not the algebraic one, hence the pressure's survival and the continuity's loss. The decomposition $F=r\Omega+\mathrm{d}r\wedge u$ as an algebraic identity with $D$ in place of $\mathrm{d}$, and with it the statement that the vorticity's source has changed while its structure has not. The condition's loss of its fluid reading, stated as the source term that $\partial\cdot A$ acquires. The separation of the two gauge freedoms. And the count's failure to close, located at the carrier's complex structure.

**Does not add.** No new equation. No new fluid: the reading of the magnitude and the direction survives and does not extend. No statement about the extra four parameters beyond their location. No thermodynamics. No quantum potential, at either rung, since the Proca action has no second derivative of the magnitude.

**The layer's ledger, in one sentence per article.** The scalar first-order rung has one substitution in two brackets; the scalar relativistic rung has a substitution that meets the shell; the spinor rung has a substitution whose image is the phase and the boost and never the rotor; the vector rung has a substitution that reaches the derivative term and leaves the pressure alone and takes the continuity away. **Four charged articles, one connection, four different reaches** — and the reaches are read off the connection's type in the algebra, which is the same argument in all four.

## Open Questions

1. **The extra four parameters.** Whether the carrier's remaining freedom can be read as a second fluid, with its own density and phase, is not settled. The block's article records the doubling and leaves it.

2. **The condition's source and the current.** The source term in $\partial_\mu A^\mu$ is $-\frac{iϙ}{\hbar}A^{\mathrm{ext}}\cdot A$; whether it is the divergence of a current the fluid can name — as the scalar rung's $ϙ\vec j$ is — is not computed here.

3. **The massless limit.** As at the free rung, the fluid reading does not survive $k_m=0$, and the charged case adds a second reason: the condition's source is present at $k_m=0$ as well, so the limit loses both the condition and the reading.

## Summary

**The action.** $\mathcal L_{\mathrm{gco}}=-\frac14F^{\mathrm{gco}*}F^{\mathrm{gco}}-\frac{k_m^{2}}{2}\lvert A\rvert^{2}$: the derivative term rebuilt with $D$, the algebraic term untouched.

**The decomposition.** $F^{\mathrm{gco}}=r\,\Omega+\mathrm{d}r\wedge u$ with $\Omega=Du$; the vorticity is covariant and rank two, its transversality being the projection's and not the curl's; the density's gradient's term is unchanged.

**The condition.** $D_\mu A^\mu=0$ still follows from the field equation, and written with the ordinary divergence it has a phase-carrying imaginary source. **Continuity is lost** and the fluid is compressible by the field's action.

**The mass.** Three of its four free statements survive: it breaks the field's own shift, supplies the condition, fixes the pressure. It no longer makes the condition a conservation law.

**The carrier.** Eight real parameters against the fluid's four; the action puts the coupling in the derivative term only, and the count's balance is the phase.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A_\mu$ | The complex Proca field; eight real parameters |
| $D_\mu=\partial_\mu+\frac{iϙ}{\hbar}A^{\mathrm{ext}}_\mu$ | The covariant derivative; abelian |
| $F^{\mathrm{gco}}_{\mu\nu}=D_\mu A_\nu-D_\nu A_\mu$ | The covariant field strength |
| $r$, $u_\mu$ | Magnitude and direction; $u_\mu u^\mu=-1$ |
| $\Omega_{\mu\nu}=D_\mu u_\nu-D_\nu u_\mu$ | Covariant curl, contracting to minus the covariant acceleration; its projection is the vorticity and is rank two |
| $F^{\mathrm{gco}}=r\,\Omega+\mathrm{d}r\wedge u$ | The decomposition of the field strength |
| $\lvert A\rvert^{2}$ | The algebraic term's argument; coupling-blind |
| $k_m=mc/\hbar$ | Mass wave number |
| $ϙ$ | Coupling; minus the electric charge |
| $\lambda=\exp(iϙ\Gamma/\hbar)$ | The external gauge element; a symmetry |
| $\vartheta_{\mathrm{pha}}$ | The carrier's phase; appears squared in the divergence |
| $\mathcal L_{\mathrm{gco}}$ | The Lagrangian density in the fluid variables with the connection |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Alexandru Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs," *Journal de Physique et le Radium* **7** (1936) 347–353, for the massive vector field and the condition its mass implies.
- Wolfgang Pauli, "Relativistic field theories of elementary particles," *Reviews of Modern Physics* **13** (1941) 203–232, for the constraint counting of a massive vector field and the fate of its gauge freedom.
- John R. Oppenheimer and Julian S. Schwinger, "On the interaction of mesotrons and nuclear particles," *Physical Review* **60** (1941) 150, for the constraint structure of a massive vector coupled to an external field.
- Friedrich W. Hehl, "On the kinematics of the torsion of space-time," *Foundations of Physics* **15** (1985) 451–471, for a unit vector's covariant vorticity, its transversality and its rank.
- The companion articles: [The Variational Principle and the Coupled Proca Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-proca-equation-in-biquaternionic-polar-variables.html), the same action in the chart and the branch's role; [The Charged Proca Fluid](the-charged-proca-fluid.html), the equations and the divergence $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde A)=-\frac{iϙ}{\hbar}r^{2}e^{2i\vartheta_{\mathrm{pha}}}$; [The Lagrangian of the Spin-One Fluid](the-lagrangian-of-the-spin-one-fluid.html), the free rung where the condition is continuity; and [The Lagrangian of the Charged Spin Fluid](the-lagrangian-of-the-charged-spin-fluid.html), the rung where the coupling reaches neither the density's nor the spin's norm.
