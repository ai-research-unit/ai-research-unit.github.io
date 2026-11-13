# __The Non-Quantum Limit of the Free Klein–Gordon Equation__

## Introduction

**The limit, in one sentence.** Write the field as an amplitude times a phase and let the phase's wave number grow against the length over which the amplitude varies; the phase then obeys the mass shell and the amplitude obeys a conservation law, and nothing else survives.

**What the second order changes.** The Schrödinger article's eikonal is an energy balance: one condition on the three-momentum. Here the eikonal is a normalisation: one condition on the four-momentum, and it says that the flow is a unit timelike vector. The classical object the limit produces is therefore not a particle with a given energy but a congruence of world lines with a given proper time, and that difference is the whole of what the second order adds.

**The criterion is the same one, and a second parameter appears beside it.** The criterion is $\epsilon=1/(k_\Phi L)$, unchanged, because the shift is measured by what it does to the momentum and the momentum is what the mass shell relates. A *second* ratio appears here and has no counterpart in the first-order family: the shift against the rest term, $\delta^{2}=1/(k_mL)^{2}$, which says the amplitude varies slowly on the Compton scale. That ratio is the one-particle condition and not the limit, and $\delta=\epsilon\lvert\vec p\rvert/(mc)$ makes the limit imply it and not the converse.

**What the article establishes, in five sentences.** The pair is exact. The eikonal is $\langle\tilde\nabla_\Phi S_{\tilde\Xi}\rangle_{\natural}=-m^{2}c^{2}$, the mass shell read as a norm, and its characters are timelike straight lines. The transport equation is exact and is the conservation of a proper density carried by a unit flow. The eikonal has two sheets and the limit does not choose between them, so the charge defect survives the limit and is classical. For a massless field the eikonal is the zero-divisor cone.

**What is not new.** The relativistic Madelung pair is Takabayasi's and the mass shell is the parent's. Added here: the separation of the criterion from the one-particle ratio $\delta=\epsilon\lvert\vec p\rvert/(mc)$, and the window between them, the norm reading of the mass shell as a normalisation rather than an energy balance, the measurement of the quantum potential as the failure of the flow to be unit, the two-sheet statement as a classical rather than a quantum defect, the massless case as the cone, and the non-commutativity of the two limits at the order of the discarded term.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; $i$ is central; $\mathbb{B}_{C}$ is the centre, $\mathbb{B}_{H}$ the real-quaternion subspace, $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ the Hermitian and anti-Hermitian sectors. The d'Alembertian is $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$ with $r'_t=c\,t'$, so every temporal derivative is a derivative in a length. The four-momentum is $\tilde P_\Phi=i(E/c)e_t+\vec p$ with $\vec p=\nabla S_{\tilde\Xi}$ and $E=-c\,\partial S_{\tilde\Xi}/\partial r'_t$. The norm is $\langle A\rangle_{\natural}=AA^{\natural}$, which is $+|\vec a|^{2}$ on a real vector and $-(E/c)^{2}$ on the temporal slot $i(E/c)e_t$. The mass wave number is $k_m=mc/\hbar$.

## The Word and the Pair

**The field.** On the central class the polar word collapses to three parameters,

$$
\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\varepsilon\,e_t ,
\qquad
r>0,
\qquad
\varepsilon=\pm1,
\qquad
S_{\tilde\Xi}=\hbar\,\theta_{\mathrm{pha}},
$$

with $r$ the amplitude, $\rho_{\mathrm{num}}=r^{2}$ the proper density and $\varepsilon$ the branch of the modulus. The angle is a coordinate and the sign is data.

**The pair, exact and not an approximation.** Substituting the word into $(\Box-k_m^{2})\Xi_t=0$ and separating the real from the imaginary part gives

$$
\left(\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)^{2}-\lvert\nabla S_{\tilde\Xi}\rvert^{2}=m^{2}c^{2}-\hbar^{2}\frac{\Box_\Phi r}{r} ,
\qquad
\nabla\cdot\left(\rho_{\mathrm{num}}\nabla S_{\tilde\Xi}\right)-\frac{\partial}{\partial r'_t}\left(\rho_{\mathrm{num}}\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)=0 .
$$

The first is the amplitude equation and the second the transport equation, and together they are equivalent to the equation for a field of this form, away from the nodal set.

**On the four-momentum the first equation is a mass shell with a shift.**

$$
\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2mQ ,
\qquad
Q=-\frac{\hbar^{2}}{2m}\,\frac{\Box_\Phi r}{r} .
$$

**Three terms and their orders.** The criterion sizes the shift against the rest term, and the rest term is the one the amplitude is compared with:

| object | size | survives the limit |
|---|---|---|
| $\dfrac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}$ | $m^{2}c^{2}$, order $1$ by definition | yes |
| $2mQ$ | $\hbar^{2}/L^{2}$; order $\epsilon^{2}$ against the sensitivity | no |
| the transport equation | exact, contains no $\hbar$ | yes, untouched |

**The second row is the only thing the limit drops.** The first row is kept because it is the statement the equation makes, and the third is kept because it never carried $\hbar$. A reader who drops both the shift and the transport equation has kept a normalisation and thrown away a conservation law, and has not taken this limit.

## The Criterion, and a Second Parameter

**The shift is measured by what it does to the momentum.** The mass shell is a difference of terms each of size $m^{2}c^{2}$ for a slow particle, so the size of the shift against the largest term is not the error of the relation. Hold $E$ fixed and shift the right side by $2mQ$; the momentum moves by $\delta p$ with $2p\,\delta p=2mQ$, so

$$
\frac{\delta p}{p}=\frac{mQ}{p^{2}}=\frac{Q}{2T_{\mathrm{kin}}}\sim\frac{\epsilon^{2}}{2},
\qquad
\epsilon=\frac{1}{k_\Phi L},
\qquad
k_\Phi=\frac{\lvert\vec p\rvert}{\hbar}.
$$

**The criterion is $\epsilon$, and the mass does not enter it.** It is the Schrödinger criterion, for the reason the audit's *The Rule* gives: the discarded term is measured against the term that carries the change, and here that term is the momentum. A criterion built on $k_m$ would measure the shift against a constant, and a constant shifts nothing.

**A second ratio, and it is not the criterion.** Against the rest term the same shift is

$$
\frac{2m\lvert Q\rvert}{m^{2}c^{2}}=\frac{\hbar^{2}}{m^{2}c^{2}L^{2}}=\delta^{2},
\qquad
\delta=\frac{1}{k_mL}=\frac{\hbar}{mcL},
$$

which is the Compton wavelength over the amplitude's length. **$\delta\ll1$ says the amplitude varies slowly on the Compton scale**, so the region is large against the length at which pairs are made. It is the condition for the one-particle description, and the audit records it as a precondition of quantum mechanics and not as its removal.

**The two are nested, and the nesting is exact.**

$$
\delta=\epsilon\,\frac{k_\Phi}{k_m}=\epsilon\,\frac{\lvert\vec p\rvert}{mc}<\epsilon .
$$

**So the limit implies the one-particle condition and the one-particle condition does not imply the limit.** A field cannot be semiclassical and pair-producing at once: the non-quantum limit of a second-order field always sits inside the window in which the one-particle reading is available. That is a statement about the two criteria and not about the field, and it is why the limit never has to be qualified by a no-pair condition.

**The window between them is a real regime.** With $\delta\ll1\ll\epsilon$ the amplitude varies slowly on the Compton scale and fast on the de Broglie scale: the mass shell's *value* is essentially exact, and the momentum it predicts is wrong by order one. The state there has a spiky density and an energy dominated by the quantum term, and it is not a ray. **The audit's verdict on $1/(k_mL)$ is this regime**, and the article agrees with it: $\delta\ll1$ is the one-particle window and $\epsilon\ll1$ is the limit.

**The three terms, with the right competitor named.**

| object | compared with | ratio | name |
|---|---|---|---|
| $2mQ$ | $2mT_{\mathrm{kin}}$, the sensitivity | $\epsilon^{2}$ | the criterion; the limit is $\epsilon\to0$ |
| $2mQ$ | $m^{2}c^{2}$, the largest term | $\delta^{2}$ | the one-particle window; implied, not the limit |
| the transport equation | nothing; it carries no $\hbar$ | $0$ | exact |

**The counting is the same in both families.** In the Schrödinger family the sensitivity is $T_{\mathrm{kin}}$ and the ratio is $\epsilon^{2}$; here the sensitivity is also $T_{\mathrm{kin}}$, because the mass shell's sensitivity to a shift of its right side is the kinetic energy and not the rest energy. **The criterion is one number for the whole corpus, and the second-order family adds a ratio and not a parameter.**

## The Eikonal Is the Mass Shell

**Drop the shift.**

$$
\left(\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)^{2}-\lvert\nabla S_{\tilde\Xi}\rvert^{2}=m^{2}c^{2} .
$$

**In the algebra it is a norm.** With $\tilde\nabla_\Phi S_{\tilde\Xi}$ the phase-gradient four-vector, whose temporal slot is $i(E/c)$ and whose spatial slots are $\vec p$,

$$
\boxed{\ \langle\tilde\nabla_\Phi S_{\tilde\Xi}\rangle_{\natural}=-m^{2}c^{2}\ }
$$

because the temporal slot contributes $-(E/c)^{2}$ and the spatial slots contribute $+\lvert\vec p\rvert^{2}$. **The eikonal is the mass shell, and the mass shell is a norm.**

**What kind of statement that is.** The Schrödinger eikonal is an energy balance: $\langle\vec\nabla_\Phi S\rangle_{\natural}/(2m)=E-V$, one condition on the three-momentum with the energy on the other side. The Klein–Gordon eikonal is a normalisation: one condition on the four-momentum, with no quantity on the other side but the mass. The first says how fast; the second says how long, and it says it by fixing the norm.

**The reading of the norm as a normalisation of the flow.** Divide by $m^{2}$:

$$
\langle\tilde V_\Phi\rangle_{\natural}=-c^{2},
\qquad
\tilde V_\Phi=\frac{\tilde\nabla_\Phi S_{\tilde\Xi}}{m}=\frac{\tilde P_\Phi}{m} .
$$

The flow's four-velocity is a unit timelike vector, future-directed on one sheet and past-directed on the other. **The limit's classical object is a congruence of world lines of fixed proper time, and not a trajectory with a given energy.**

**The quantum potential measures the failure of that normalisation.** Restoring the shift,

$$
\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}+\frac{\hbar^{2}}{m^{2}}\,\frac{\Box_\Phi r}{r},
$$

so the flow is exactly unit only where $\Box_\Phi r=0$, and the amount by which it fails is $Q$. **The quantum potential is the amount by which the classical reading of the flow as a congruence of unit world lines misses.** That is the sharpest one-line statement of what the limit discards in this family, and it has no counterpart in the first-order case, where the flow's norm is not what the eikonal fixes.

**The characters are dust.** The characteristic system of $\langle\nabla S\rangle_{\natural}=-m^{2}c^{2}$ is $\dot{\vec r}=\vec p/m$ with $\vec p$ constant, so the rays are straight timelike lines and the flow is pressureless. The transport equation then says that the density is carried without compression along those lines. **Relativistic dust is the classical limit of the free Klein–Gordon field**, and it is dust and not a gas because the free eikonal has no force in it.

**A plane wave is the case in which nothing is dropped.** For $S_{\tilde\Xi}=\vec p\cdot\vec r-E\,r'_t/c$ with the mass shell exact, the amplitude is constant, $\Box_\Phi r=0$, and both $\epsilon$ and $\delta$ vanish identically. The limit is again empty where it is exact, exactly as in the Schrödinger case: it acts only where the amplitude varies.

## The Transport Is Exact

**It was never an expansion.** $\nabla\cdot(\rho_{\mathrm{num}}\nabla S)-\partial_{r'_t}(\rho_{\mathrm{num}}\partial_{r'_t}S)=0$ contains no $\hbar$ and no $Q$, so the limit neither produces it nor spoils it. It is the divergence of the four-current

$$
\tilde J_\Phi=\rho_{\mathrm{num}}\tilde V_\Phi=\frac{\rho_{\mathrm{num}}}{m}\,\tilde P_\Phi ,
$$

and its content is one sentence: the proper density is carried by the unit flow, and the current is the density times the four-velocity.

**Its temporal component is the charge and it is indefinite.** $\rho_{\mathrm{chg}}=\rho_{\mathrm{num}}E/(mc^{2})$ has the sign of $E$, so the positive sheet carries positive charge and the negative sheet negative, with the same positive $r^{2}$ on both. **The amplitude carries no sign anywhere**, which is why the defect is one sign and not two.

**The flow is irrotational off the nodes.** The velocity is a gradient, so $\nabla\times\vec v=0$ wherever the action is twice differentiable, and the exception is a nodal line around which the action is multivalued. The limit inherits both statements unchanged, because neither contains the amplitude's length.

## The Limit Does Not Choose a Sheet

**Two sheets and one equation.** The eikonal $\langle\tilde P_\Phi\rangle_{\natural}=-m^{2}c^{2}$ is a two-sheeted hyperboloid in momentum space. Its two sheets are the two signs of $E$, and both solve it.

**The limit keeps both.** Dropping $Q$ does not select a sheet, because $Q$ is a functional of $r$ alone and is therefore invariant under $S_{\tilde\Xi}\to-S_{\tilde\Xi}$, which is the map between the sheets while $r$ is unchanged. So

$$
\lim\left(\text{positive sheet}\right)\ \text{and}\ \lim\left(\text{negative sheet}\right)
$$

are two dusts, with opposite charge densities and the same density, and both are classical.

**What follows, and it is the article's sharpest negative statement.** The indefinite charge is not a quantum defect that the classical limit removes; it is a **classical** defect of a second-order field, and it is visible in the limit as the existence of two classical dusts. A one-particle reading is not available in the limit either. What removes the second sheet is not a limit but a change of theory: second quantisation, where the two sheets become one field's particle and antiparticle.

**The statement in the algebra's letters.** The mass shell constrains the norm and not the sign of the time component. The norm is a quadratic form, so it cannot see a sign, and any statement that does must come from somewhere else — from the initial data, or from the coupling, or from the second-quantised theory. The corpus says this of the equation; the article says it of the limit, and the two statements are the same statement.

## The Massless Case: the Eikonal Is the Cone

**Set $m=0$.** The equation is $\Box_\Phi\Xi_t=0$, the wave equation, and the amplitude equation loses its rest term:

$$
\left(\frac{\partial S}{\partial r'_t}\right)^{2}-\lvert\nabla S\rvert^{2}=-\hbar^{2}\frac{\Box_\Phi r}{r},
\qquad
\langle\tilde\nabla_\Phi S\rangle_{\natural}=\hbar^{2}\frac{\Box_\Phi r}{r} .
$$

**The limit is the vanishing of a norm.**

$$
\langle\tilde\nabla_\Phi S\rangle_{\natural}=0 .
$$

**That is the zero-divisor cone.** A nonzero element whose norm vanishes is a zero divisor, so the eikonal of the massless field says that the phase-gradient four-vector is a zero divisor at every point. The light cone of the classical wave is the cone of the algebra, and no separate postulate is needed to identify them: the mass shell with $m=0$ *is* the cone.

**This is the one case in which the limit lands on a locus the algebra already names.** For $m\neq0$ the phase gradient is never on the cone, because its norm is fixed at $-m^{2}c^{2}$. For $m=0$ it is on the cone everywhere, and the classical characteristic surfaces of the wave equation are the surfaces the cone generates. **The corpus defines the cone as the locus of the non-invertible elements; the massless limit identifies it as the locus of the lightlike momenta**, and that identification is a result of the limit and not a definition.

**What the quantum term does there.** The shift is now the whole of the right side, so the exact statement is that the phase gradient's norm is $\hbar^{2}\Box r/r$ and not zero. The approximation sets it to zero, and $\delta$ does not exist because there is no $k_m$ to build it from; the criterion in the massless case is the Schrödinger one, $\epsilon=1/(k_\Phi L)$, since the surviving term is now the phase's own norm.

## The Error

**The error is the shift, and its size is a function of position.** With a planar Gaussian amplitude $r=\exp(-x^{2}/4\sigma^{2})$, static,

$$
\Delta_\Phi r/r=\frac{x^{2}}{4\sigma^{4}}-\frac{1}{2\sigma^{2}},
\qquad
\frac{\lvert\delta p\rvert}{p}=\frac{\lvert Q\rvert}{2T_{\mathrm{kin}}}=\frac{\epsilon^{2}}{2}\left\lvert\frac{x^{2}}{4\sigma^{2}}-\frac{1}{2}\right\rvert .
$$

| $\lvert x\rvert/\sigma$ | $0$ | $1$ | $\sqrt{2}$ | $2$ | $3$ |
|---|---|---|---|---|---|
| $2\lvert Q\rvert/T_{\mathrm{kin}}$, the momentum error, in units of $\epsilon^{2}$ | $0.500$ | $0.250$ | $0$ | $0.500$ | $1.750$ |
| $2\lvert Q\rvert/(m^{2}c^{2})$ in units of $\delta^{2}$ | $0.500$ | $0.250$ | $0$ | $0.500$ | $1.750$ |

**The two rows are the same numbers and they are not the same claim.** The first is the error of the approximation and the second is the one-particle ratio; they coincide numerically because both are $2\lvert Q\rvert$ in different units, and they separate as criteria because $\delta=\epsilon\lvert\vec p\rvert/(mc)$.

**The error reaches one at $x\simeq2\sigma/\epsilon$.** No value of the parameter makes the expansion uniform, and the limit is a statement about the equation while the approximation is a statement about a region of one solution.

**What the limit does not commute with.** Two plane waves are each semiclassical exactly, and their sum is not, because the envelope's wave number is the difference of theirs. So the limit does not distribute over superposition, for the same reason as in the first-order case and with the same consequence: it is not a map on the state space.

## The Two Limits and Their Order

**Two limits, and the second one is not this one.** The nonrelativistic limit is $\beta=\lvert\vec v\rvert/c\to0$; it is the parent's, and it divides out the rest phase $S_{\tilde\Xi}=-mc\,r'_t+\sigma$ and drops $T_{\mathrm{kin}}^{2}/c^{2}$ against $T_{\mathrm{kin}}$. The limit of this article is $\epsilon\to0$. Both are needed to reach Newton, and the question is whether their order matters. **$\delta\to0$ is not a third limit**: it is the one-particle window, it is weaker than $\epsilon\to0$, and taking it alone leaves the quantum Madelung fluid with a mass shell that is right only in its value.

**At leading order they commute.** Taking $\epsilon$ first leaves the relativistic eikonal and the exact transport; taking $\beta$ on that pair gives $T_{\mathrm{kin}}=\lvert\vec p\rvert^{2}/2m$ with $\vec p=\nabla\sigma$ and the continuity equation for $\rho_{\mathrm{num}}$. Taking $\beta$ first leaves the Schrödinger pair with $Q=-\hbar^{2}\Delta_\Phi r/(2mr)$; taking $\epsilon$ on that pair gives the same two equations. **The final pair is the same in both orders.**

**At the order of the discarded term they do not commute.** The two paths discard different objects and in different sequence:

| path | first discarded | second discarded | what is left of $Q$ at the end |
|---|---|---|---|
| $\epsilon$ then $\beta$ | $2mQ$ against $2mT_{\mathrm{kin}}$ | $T^{2}/c^{2}$ against $T$ | nothing; $Q$ was dropped first |
| $\beta$ then $\epsilon$ | $T^{2}/c^{2}$ and $\partial^{2}_{r'_t}r$ against $\Delta r$ | $Q$ against $T$ | nothing; $Q$ was dropped last |

**The difference is in the middle, and it is visible.** Halfway along the first path the object is relativistic dust with no quantum term; halfway along the second it is the quantum Madelung fluid with $Q$. A claim that the equations are semiclassical and nonrelativistic must say which path it took, because the intermediate equations differ and the term that is small differs.

**One relation orders all three parameters.** $\delta=\epsilon\,\lvert\vec p\rvert/(mc)$: the one-particle ratio is the criterion times the momentum over the rest momentum, so the criterion is always the larger of the two and the limit always lies inside the window. A field can be inside the window and outside the criterion — the case $\lvert\vec p\rvert\ll mc$, $\epsilon\sim1$ — and that is a nonrelativistic field with a large quantum potential, which is the ordinary quantum-mechanical regime.

## Where the Approximation Stops

**Three places, and each is a place.**

**Where the momentum vanishes.** The branch $p=\sqrt{(E-V)^{2}/c^{2}-m^{2}c^{2}}$ turns where the kinetic energy vanishes, and there the amplitude diverges and the two branches of the eikonal meet. A potential supplies such a point; the free equation does not, so this article has no turning point to repair and the phase-integral apparatus of the nonrelativistic family has no free-space counterpart here.

**At a caustic.** Neighbouring dust lines cross, the density diverges, and the map from initial to final position loses rank. The lines are straight, so the crossing is a property of the initial velocity field and not of a force: a uniform flow has no caustic and a sheared one does.

**Where the amplitude varies on the Compton scale.** There $\delta$ is not small, the region is no longer one in which the one-particle reading is available, and the limit has no claim. That is the pair-creation regime, and the fact that the limit's failure region is the Compton scale is the reason the second sheet cannot be discarded: the region where the dust picture fails is the region where the two sheets meet.

## What the Biquaternion Form Adds

**Standard relativistic hydrodynamics, transcribed.** The pair, the mass shell, the dust reading, the charge sign and the four-current are Takabayasi's and the parent's. The ordering by $\epsilon$ is the standard semiclassical ordering; $\delta$ is the one-particle ratio beside it.

**Four things the notation supplies.**

*The mass shell is a norm, and the eikonal is the mass shell.* $\langle\tilde\nabla_\Phi S\rangle_{\natural}=-m^{2}c^{2}$ is one line, and it identifies the leading-order equation as the normalisation of a four-vector rather than as a balance of energies. The two families' eikonals are then the two things a quadratic form can do to a vector: fix its value against an energy, or fix its norm against a mass.

*The failure of the normalisation is the quantum potential.* $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}+\hbar^{2}\Box r/(m^{2}r)$ puts $Q$ where a physical reading can see it: it is the amount by which the flow is not a unit congruence, and the limit is the statement that the congruence is unit.

*The cone is reached only at $m=0$.* For $m\neq0$ the phase gradient's norm is fixed away from zero by the mass, so the limit cannot land on the zero-divisor locus. At $m=0$ it lands on it exactly, and the light cone becomes the algebra's cone. That is the cleanest contact between the corpus's algebraic locus and a classical characteristic surface.

*The two sheets are two norms and one sign.* The norm is quadratic, so it cannot distinguish the sheets, and the algebra exhibits the reason the defect survives the limit: the only object in the pair that is odd in the action is the temporal component of the current.

**What it does not supply.** A branch rule; any reason to prefer one sheet; a uniform approximation at a turning point; and any prediction distinguishing the reformulation from the standard relativistic Madelung fluid.

## Summary

The field is $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$ with $\rho_{\mathrm{num}}=r^{2}$, and the exact pair is

$$
\left(\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)^{2}-\lvert\nabla S_{\tilde\Xi}\rvert^{2}=m^{2}c^{2}-\hbar^{2}\frac{\Box_\Phi r}{r},
\qquad
\nabla\cdot\left(\rho_{\mathrm{num}}\nabla S_{\tilde\Xi}\right)-\frac{\partial}{\partial r'_t}\left(\rho_{\mathrm{num}}\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)=0 .
$$

The criterion is $\epsilon=1/(k_\Phi L)$, unchanged from the first-order family, because the shift is measured by what it does to the momentum. A second ratio, $\delta=1/(k_mL)$, appears in this family and is the condition that the amplitude varies slowly on the Compton scale; it is the one-particle window, it satisfies $\delta=\epsilon\lvert\vec p\rvert/(mc)$, and the limit implies it. Dropping the shift gives the eikonal $\langle\tilde\nabla_\Phi S_{\tilde\Xi}\rangle_{\natural}=-m^{2}c^{2}$, which is the mass shell read as a norm and whose characters are straight timelike lines carrying a proper density. The quantum potential is the amount by which the flow fails to be the unit timelike congruence the eikonal asserts. The transport equation is exact and carries the indefinite charge. The eikonal has two sheets and the limit chooses neither, so the charge defect is classical and survives; only second quantisation removes it. At $m=0$ the eikonal is the zero-divisor cone. The error is $\epsilon^{2}\lvert x^{2}/4\sigma^{2}-\frac12\rvert$ for a planar Gaussian, reaching one at $x\simeq2\sigma/\epsilon$. The nonrelativistic and non-quantum limits commute at leading order and not at the order of the discarded term, and a claim of approximation must name the path.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{B}_{C}$, $\mathbb{B}_{H}$ | Centre; real-quaternion subspace |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ | Hermitian and anti-Hermitian sectors |
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$ | The central word; scale, angle, branch |
| $\rho_{\mathrm{num}}=r^{2}$ | Proper density |
| $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ | The action, modulo $2\pi\hbar$ |
| $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$ | The d'Alembertian; $r'_t=c\,t'$ |
| $k_m=mc/\hbar$ | Mass wave number |
| $\tilde P_\Phi=i(E/c)e_t+\vec p$ | Four-momentum; $E=-c\,\partial S_{\tilde\Xi}/\partial r'_t$, $\vec p=\nabla S_{\tilde\Xi}$ |
| $\langle A\rangle_{\natural}=AA^{\natural}$ | The norm; $+\lvert\vec a\rvert^{2}$ on a vector, $-(E/c)^{2}$ on the temporal slot |
| $\langle\tilde\nabla_\Phi S_{\tilde\Xi}\rangle_{\natural}=-m^{2}c^{2}$ | The eikonal: the mass shell as a norm |
| $\tilde V_\Phi=\tilde P_\Phi/m$ | Four-velocity; unit exactly where $\Box_\Phi r=0$ |
| $Q=-\frac{\hbar^{2}}{2m}\Box_\Phi r/r$ | Quantum potential; the failure of the normalisation |
| $\epsilon=1/(k_\Phi L)$ | The parameter of the limit |
| $\delta=1/(k_mL)$, $\delta=\epsilon\lvert\vec p\rvert/(mc)$ | The one-particle ratio; implied by the limit |
| $\lvert\delta p\rvert/p=\frac{\epsilon^{2}}{2}\lvert x^{2}/4\sigma^{2}-\frac12\rvert$ | The error, planar Gaussian |
| $\langle\tilde\nabla_\Phi S\rangle_{\natural}=0$ | The massless eikonal: the cone |

## Further Reading

- T. Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 2–80, and "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8** (1952) 143–182, for the relativistic Madelung pair.
- E. Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the non-relativistic pair.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the mass shell, the characteristic surfaces of the wave equation and the light cone.
- H. Goldstein, C. P. Poole, and J. L. Safko, *Classical Mechanics* (Addison-Wesley, 2002), for the Hamilton–Jacobi equation and its characteristics as a congruence.
- J. B. Keller, "Corrected Bohr–Sommerfeld quantum conditions for nonseparable systems," *Annals of Physics* **4** (1958) 180–188, for the characteristic reading of an eikonal.
- M. V. Berry and K. E. Mount, "Semiclassical approximations in wave mechanics," *Reports on Progress in Physics* **35** (1972) 315–397, for the failure of the short-wavelength expansion where an amplitude varies on the scale of the wavelength.
- A. Messiah, *Quantum Mechanics* (North-Holland, 1961), for the Klein–Gordon charge density and its indefiniteness.
- H. Feshbach and F. Villars, "Elementary relativistic wave mechanics of spin 0 and spin 1/2 particles," *Reviews of Modern Physics* **30** (1958) 24–45, for the two-sheet structure read as a two-component theory.
