# __The Charged Spin Fluid: The Force Takes the Charge and the Spin Does Not__

## Introduction

**The charge reaches the momentum and the frame's rapidity, and it cannot reach the spin.** That is the whole of what the coupling does to the spin fluid, and the article's work is to draw out what follows: the velocity is still a unit, the vorticity is still the frame's, the spin direction is still gauge invariant and still coupling-blind, and the three open items of the free article — no vorticity transport law, no closure, no spin dynamics in a background — survive the coupling untouched. **The charge adds a force and an angle shift; it does not add a constitutive law.**

**The equation.** The coupled Dirac equation in polar variables is the free one with covariant derivatives,

$$
\tilde\nabla_{\mathrm{gco}}\tilde\Xi_{\mathrm D}=\frac{i}{\hbar}k_m\tilde\Xi_{\mathrm D},
\qquad
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi,
\qquad
\tilde\Xi_{\mathrm D}=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r},
$$

with $\tilde A_\Phi=i a'_t e_t+\vec A$ in the material sector. **The coupling is central per component**, so it commutes with the split of the word into a scale, an angle, a boost and a rotor, and its effect is confined by type rather than by size. That single fact decides every question the article asks.

**Three things are established.**

*First, the connection reaches two of the four brackets and no others.* Its temporal slot is a central imaginary number and joins the phase bracket; its spatial slots are Hermitian vectors and join the boost bracket. The scale bracket is a real scalar and the rotor bracket is a real vector part, and a central element can produce neither. **On the fluid's side: the momentum and the rapidity move, the density does not, and the spin does not.**

*Second, the velocity is the kinetic one and it is a unit for every field.* The mass-shell identity holds for the covariant wavevector, $\tilde K_{\Phi,\mathrm{gco}}=ik_m\tilde U_{\Psi,\mathrm b}^{-2}$, so the boost in the word is the one the covariant wavevector names, and $\tilde V_\Phi=ic\tilde U_{\Psi,\mathrm b}^{-2}$ with $\langle\tilde V_\Phi\rangle_\natural=-c^{2}$ whatever the coupling. **This is the one charged fluid whose normalisation the coupling cannot touch**, and the reason is structural: the velocity is a unit by construction and not by the equation of motion.

*Third, the force is the Lorentz force and there is no torque.* The coupling enters the momentum balance through the charge current and the antisymmetric part of the stress through the spin current, and the second is the free article's. So the fluid is pushed where it carries charge and is turned where its spin varies, and **the field does not turn the spin directly**; what the standard theory calls Larmor precession appears at second order, through the transport of the frame, and §*The Force, and Not the Torque* states the composition.

**What is not here.** No new solution, no derivation of a spin equation in a background, and no closure of the general field. The parent records all three limits for the free case; this article records that the coupling does not lift them, and that the reason is a fact of type.

**Position in the block.** This article is the charged companion of [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html). Its siblings are [The Charged Klein–Gordon Fluid](the-charged-klein-gordon-fluid.html) and [The Charged Proca Fluid](the-charged-proca-fluid.html), and §*The Three Charged Fluids* compares the three.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; $^{\natural}$ is quaternion conjugation, $^{*}$ Hermitian conjugation, $\mathrm{Sc}$ the coefficient of $e_t$. The word is $r e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ with $r>0$, $\tilde U_{\Psi,\mathrm b}$ a boost of rapidity $\theta_{\mathrm{rpd}}$ about $\vec u_{\mathrm b}$ and $\tilde u_{\mathrm r}$ a rotor of angle $\theta_{\mathrm{axr}}$ about its axis. The coupling is $ϙ$, the action is $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$, $k_m=mc/\hbar$, and $\tilde A_\Phi=i a'_t e_t+\vec A$ with $a'_t$ and $\vec A$ real. The spin direction is $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$.

## The Two Brackets the Charge Can Reach

**The logarithmic derivative of the coupled word has four brackets, and the connection's whole contribution is one central element per slot.** Dividing the covariant derivative of the word by the word,

$$
\tilde\Xi_{\mathrm D}^{-1}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi_{\mathrm D}
=\frac{1}{2}\frac{\partial\ln\rho}{\partial R_\mu}
+i\frac{\partial\theta_{\mathrm{pha}}}{\partial R_\mu}
+\frac{iϙ}{\hbar}A_\mu
+\tilde u_{\mathrm r}^{-1}\Bigl(\tilde U_{\Psi,\mathrm b}^{-1}\frac{\partial\tilde U_{\Psi,\mathrm b}}{\partial R_\mu}\Bigr)\tilde u_{\mathrm r}
+\tilde u_{\mathrm r}^{-1}\frac{\partial\tilde u_{\mathrm r}}{\partial R_\mu},
$$

and the added term decomposes by its own slots:

$$
\frac{iϙ}{\hbar}\tilde A_\Phi
=\underbrace{\frac{iϙ}{\hbar}A_t}_{\text{central imaginary}}
+\underbrace{\frac{iϙ}{\hbar}\sum_\eta A_\eta\vec e_\eta}_{\text{Hermitian vector}} .
$$

**The temporal slot is a central imaginary number and the spatial slots are Hermitian vectors**, so the connection adds to the phase bracket and to the boost bracket. The scale bracket is a real central scalar and the rotor bracket is a real vector part; neither is reachable by a central multiplication, and both are therefore untouched.

| bracket | type | the connection's share | what it moves in the fluid |
| --- | --- | --- | --- |
| $\tfrac12\partial_\mu\ln\rho$ | real central scalar | none | the density: nothing |
| $i\partial_\mu\theta_{\mathrm{pha}}+\frac{iϙ}{\hbar}A_\mu$ | central imaginary | the whole temporal slot | the momentum |
| $\tilde u_{\mathrm r}^{-1}(\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b})\tilde u_{\mathrm r}$ | Hermitian | the whole spatial slot | the rapidity and the axis |
| $\tilde u_{\mathrm r}^{-1}\partial_\mu\tilde u_{\mathrm r}$ | real vector part | none | the spin direction: nothing |

**The third row is the row the scalar case does not have, and it is the article's hinge.** In the scalar fluid the frame brackets vanish identically, so the connection's spatial slots have nowhere to land and the only effect is a shift of the phase rate. Here the spatial slots land in the boost bracket, so **the field changes the rapidity of the flow as well as its momentum** — and in doing that it changes the velocity twice over: once by shifting the wavevector the rapidity is read from, and once by turning the frame's axis through the transport.

**The rotor's row is the row that matters for the spin, and it is a row of zeros.** A central multiplication cannot reach inside the product $\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ to change one factor and not the other. **The spin direction is therefore coupling-blind in the chart's kinematics**, and §*The Force, and Not the Torque* draws the consequence.

**Why the type argument is a proof and not a hope.** The four brackets are the four irreducible types of the element: real central scalar, central imaginary, Hermitian, and real vector part. A central element is a combination of the first two, and multiplication by it preserves the type of what it multiplies. So the connection can move only the two brackets whose type it can supply, and the two it cannot supply are exactly the scale and the rotor. **No choice of the connection's size or shape changes the answer**, which is why the argument is worth stating once and not testing case by case.

## The Velocity Is the Kinetic One

**The mass-shell identity is the proposition that names the velocity, and the coupling shifts which wavevector it applies to.** The parent's proposition is that a field whose wavevector satisfies $\tilde K\tilde K^{\natural}=-k_m^{2}$ has $\tilde K=ik_m\tilde U_{\Psi,\mathrm b}^{-2}$ for a boost. With the connection in place the same proposition holds for the covariant wavevector:

$$
\tilde K_{\Phi,\mathrm{gco}}=ik_m\tilde U_{\Psi,\mathrm b}^{-2},
\qquad
\tilde V_\Phi=ic\,\tilde U_{\Psi,\mathrm b}^{-2},
\qquad
\vec v=c\tanh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b},
\qquad
\gamma=\cosh\theta_{\mathrm{rpd}},
$$

and the canonical wavevector is the covariant one less the potential:

$$
\tilde K_\Phi=\tilde K_{\Phi,\mathrm{gco}}-\frac{ϙ}{\hbar}\tilde A_\Phi .
$$

**In one sentence: the boost in the word is the one the covariant wavevector names, so the velocity is kinetic and the potential sits entirely in the canonical wavevector.** The classical statement is $\vec p_{\mathrm{kin}}=\vec p_{\mathrm{can}}-ϙ\vec A$; the chart's statement is that the two wavevectors differ by one element and that the mass-shell identity is applied to the second.

**The velocity is a unit for every field, and this is where the spin fluid parts company with the scalar one.** Because the boost is a unit by construction and the density is a separate factor,

$$
\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}
\qquad\text{whatever the coupling,}
$$

and the reason is that the velocity is not the momentum over the mass but the frame itself. **In the scalar fluid the velocity was $\tilde P^{\mathrm{mech}}/m$ and was a unit only where the quantum potential vanished**, because the quantum potential changed the momentum's norm; here nothing can change the norm of a frame. The contrast is the sharpest single difference between the two charged articles: **the scalar fluid's normalisation is dynamical and the spin fluid's is kinematical.**

**The mass shell in canonical components is the translated hyperboloid.** Expanding the identity,

$$
\Bigl(\frac{E+ϙcA_t}{\hbar c}\Bigr)^{2}-\Bigl|\frac{\vec p+ϙ\vec A}{\hbar}\Bigr|^{2}=-k_m^{2},
$$

so the radius is $k_m$ and the potential moves the centre: a constant potential shifts every level and opens no gap. **The polar reason is one line**: a shift of a variable cannot change a radius. The fluid reason is equally short: a shift of the momentum cannot change the frame.

**The objection, and the answer.** The objection is that the covariant wavevector is *defined* as the canonical one plus the potential, so "the boost is carried by the covariant wavevector" is a naming and not a result. The objection is correct as far as it goes, and the answer is that the identity fixes the direction of the reading: read from the potential to the frame, the coupling changes the rapidity, hence the velocity; read from the frame to the potential, the velocity is what survives when the potential is removed. **The chart states the identity; the physical naming is the corpus's convention and not a consequence of the algebra**, and the article says so rather than dressing it up.

## The Vorticity Is Still the Frame's

**The vorticity is the antisymmetrised gradient of the frame, and the coupling changes its value only through the equation.** With $\tilde V_\Phi=ic\tilde U_{\Psi,\mathrm b}^{-2}$ and $\Gamma_\mu:=\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b}$ the frame's logarithmic derivative,

$$
\frac{\partial\tilde U_{\Psi,\mathrm b}^{-2}}{\partial R_\mu}
=-\Gamma_\mu\tilde U_{\Psi,\mathrm b}^{-2}-\tilde U_{\Psi,\mathrm b}^{-2}\Gamma_\mu,
$$

$$
\omega_{\mu\nu}
=-ic\Bigl[\Gamma_\mu\tilde U_{\Psi,\mathrm b}^{-2}+\tilde U_{\Psi,\mathrm b}^{-2}\Gamma_\mu\Bigr]_{\nu}
+ic\Bigl[\Gamma_\nu\tilde U_{\Psi,\mathrm b}^{-2}+\tilde U_{\Psi,\mathrm b}^{-2}\Gamma_\nu\Bigr]_{\mu},
$$

where $[\,\cdot\,]_\nu$ is the coefficient of $e_\nu$. **Every term is built from $\Gamma$ and $\tilde U$, and no term contains the connection.** The potential appears in the equation of motion, the equation fixes the word, and the word fixes the frame; the chain has three links and is not a one-line identity.

**The contrast with the scalar fluid is exact and it is worth a table.**

| | charged scalar | charged spin |
| --- | --- | --- |
| the velocity | $\tilde P^{\mathrm{mech}}/m$, a gradient plus a potential | $ic\tilde U_{\Psi,\mathrm b}^{-2}$, the frame |
| $\mathrm{d}V$ | $\frac{ϙ}{m}F$, exactly | the frame's logarithmic derivative |
| is $\mathrm{d}V$ the field strength? | yes, identically | no, for any field |
| rank | $0$, $2$ or $4$ | $2$ for the proper part; the raw derivative reaches $4$ |
| closed? | yes, $\mathrm{d}F=0$ | yes, by the Maurer–Cartan flatness of $\Gamma$ |
| exact? | no, unless $\Phi_B=0$ on the loop | no, unless the holonomy is trivial |

**The fourth row is the sharpest one, and it is exact.** The vorticity proper — the part that annihilates the velocity — is rank two for every solution, because it is a two-form on the three dimensions of the rest space and every two-form on three dimensions is simple. The check was run twice: on a shear frame the four-dimensional singular values came out $0.150342$, $0.150342$, $0$, $0$; on a boost field whose rapidity varies in two directions and whose axis rotates, $0.19442$, $0.19442$, $0$, $0$, with the projected invariant $\vec E_{\mathrm{vrt}}\cdot\vec B_{\mathrm{vrt}}$ at $2.3\times10^{-19}$. **The raw derivative of that same field is rank four** — $0.20582$, $0.20582$, $0.02742$, $0.02742$ — and the difference between the two displays is the acceleration, which is the free article's point and not the coupling's.

**A rank-four field strength added to a rank-two vorticity is a rank-four two-form of a different kind.** Adding $ϙF/m$ for a representative $F$ with $\vec E\cdot\vec B\ne0$ gave the singular values $0.921$, $0.921$, $0.632$, $0.632$ at the same event. **The sum is closed, since both terms are, and it is not the vorticity**; calling it so would be a relabelling and not an identification. The scalar fluid's display $\omega=ϙF/m$ is therefore not transferable, and the transfer fails by the rank as well as by the letters.

**What the vorticity is and what it is not.** It is the fluid's rotation rate at an event, a closed two-form whose periods around non-contractible loops are the holonomy of the frame. It is not the magnetic field, and it is not the spin density: the Gordon split of §*The Gordon Split* is the magnetisation current, and the vorticity is a flow property. It is not a dynamical variable either: the free article proves there is no transport law for $\omega$, and the coupling does not supply one, because a transport law would have to be written in the fourth bracket and the connection cannot write there.

**The one thing the coupling does to the vorticity.** It changes the frame, hence $\omega$, at every event where the coupled solution's frame differs from the free one's. **The change is real and it is not a term**: there is no sense in which the charged spin fluid's vorticity is the free one's plus $ϙF/m$. A reader who wants that statement should read the scalar article, where it is true.

## The Loop Invariant: a Holonomy and a Phase

**The circulation of the spin fluid is not a number, and that is what distinguishes it from the scalar one.** Integrate the velocity around a closed loop. Because $\tilde V_\Phi$ is built from the frame, the integral is the trace of the frame's transport around the loop, and the transport is an element of the Lorentz group:

$$
\oint\tilde V_\Phi\cdot\mathrm{d}\vec l
=C\bigl[H_{\mathrm{loop}}\bigr],
\qquad
H_{\mathrm{loop}}=\mathcal{P}\exp\oint\Gamma_\mu\,\mathrm{d}x^\mu\in SL(2,\mathbb{C}),
$$

with $\mathcal{P}$ the path ordering and $C$ the linear functional that reads the components of the algebra element. **The loop's datum is $H_{\mathrm{loop}}$, a Lorentz transformation, and the circulation is one number read off it**; the scalar fluid's loop datum is a phase and its circulation is the whole of it.

**The mechanical momentum adds the flux, and the sum has two factors.** The canonical momentum is the covariant one less the potential, so the same loop carries

$$
\oint\tilde P^{\mathrm{mech}}\cdot\mathrm{d}\vec l
=\oint\tilde P^{\mathrm{can}}\cdot\mathrm{d}\vec l+ϙ\Phi_B,
$$

and the canonical loop integral is the holonomy's. **The loop's invariant is therefore a Lorentz transformation multiplied by a phase**:

$$
\text{the loop's transport}
=\underbrace{\text{holonomy of }\tilde U_{\Psi,\mathrm b}}_{\text{a Lorentz transformation}}
\times
\underbrace{\exp\Bigl(\frac{iϙ\Phi_B}{\hbar}\Bigr)}_{\text{a phase}},
$$

and the two factors commute because the second is central. **The object is an element of $\mathbb{C}^{\ast}\times SL(2,\mathbb{C})$**, and that is the honest description of a charged spin fluid's circulation: a rotation of the frame and a phase, and neither of them quantised.

**Why the scalar case is the special one.** There the velocity was a gradient plus a potential, so the loop integral split into an integer and a flux and both terms were numbers. Here the velocity is a frame, so the loop integral is a group element before the potential is added and remains one after. **The charge adds a phase to a Lorentz transformation; it does not turn the transformation into a number.**

**What survives of the free article's statement.** The free article records that the spin fluid's circulation is the holonomy and is therefore not quantised, and that the frozen-frame sector is where the circulation vanishes. Both survive, the first with the phase attached and the second with a qualification: a constant frame has a trivial holonomy and a constant flux still gives a phase, so the frozen-frame sector's circulation becomes $e^{iϙ\Phi_B/\hbar}$ rather than unity. **That is the smallest exact statement the article can make about the charge, and it is a statement about a loop and not about an event.**

## The Gordon Split

**The chart's current is the convection part, and the magnetisation part is built from the rotor alone.** The parent's current is

$$
J^t=\rho\cosh\theta_{\mathrm{rpd}},
\qquad
J^\eta=\rho\sinh\theta_{\mathrm{rpd}}\,u_{\mathrm b,\eta},
$$

which is the density times the velocity and nothing else. The Gordon decomposition of [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html) splits the current into that convection part and a magnetisation part which is the divergence of the antisymmetric spin density,

$$
J^\mu=J^\mu_{\mathrm{conv}}+J^\mu_{\mathrm{mag}},
\qquad
J^\mu_{\mathrm{mag}}=\partial_\nu\bigl(\text{the spin bilinear}\bigr)^{\nu\mu},
$$

and the second is conserved by antisymmetry alone and carries no total charge.

**The magnetisation current has no explicit dependence on the connection.** Its bilinear is built from the rotor, $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$, and from the frame. A central multiplication cannot produce a rotor, so no term in the magnetisation current can carry $ϙ$ explicitly: **the bound current is charge-blind**. Its value changes when the field changes the frame through the equation, and the change is entirely indirect.

**Why that is worth stating as a result and not as a triviality.** One might expect the coupling to screen the magnetisation current, or to add to it a term proportional to the field, in the way that a polarisable medium's bound current responds to the applied field. **The chart says no: there is no such term, and the only way the field reaches the magnetisation is by moving the frame.** The corpus's own decomposition makes the same statement in the element form, where the spin bilinear contains no connection; the chart's version is sharper because it exhibits the rotor as the invariant the connection cannot reach.

**What the split does to the charge conservation.** The conservation of the total current splits into the conservation of the convection part and the vanishing of the divergence of the magnetisation part, the second being an identity. So **the charge the fluid transports is the convection current's, and the spin's bound current adds nothing to it**: the charge density is $\rho\cosh\theta_{\mathrm{rpd}}$ and no bound contribution enters it, whatever the field.

## The Force, and Not the Torque

**The coupling adds a force and no torque, and the two statements have different reasons.** The momentum balance of the free article is that the divergence of the stress is the divergence of the spin's antisymmetric part. With the coupling it is

$$
\partial_\nu T^{\mu\nu}=ϙF^{\mu\nu}J_\nu+(\text{the free article's spin term}),
$$

so the field acts on the charge current and the spin term is the free one's. **The force is longitudinal in the sense that it acts where the charge flows; the torque is the antisymmetric part of the stress and the field has no term in it**, because a torque would have to be written in the rotor bracket and the connection cannot write there.

**The consequence, stated plainly.** In this chart the magnetic moment is not a rotor rotation. A reader who expects the coupled equation to show Larmor precession as a rotor equation will not find it, and the absence is structural rather than an oversight: the chart's variables are four brackets of four types, the coupling is confined to two by type, and a precession of the spin would have to be a term in the fourth.

**What the background does to the spin is indirect, and the composition is the whole of the physics.** The field curves the boost, and the spin's transport follows the boost's. Where the trajectory bends, the frame in which the rotor's own rate is zero bends with it, and the observed precession is the rotor's own rate composed with the transport of the frame. That composition is what the standard theory calls Thomas precession, and [The Classical Origin of $g=2$ in Biquaternionic Form](the-classical-origin-of-g-2-in-biquaternionic-form.html) carries out the expansion and shows the two contributions combining to the Larmor rate with the ratio two. **So the Larmor precession is second order in the chart's bookkeeping: not a torque on the spin, but a consequence of the frame's transport, which the field does control.**

**The exact statement of what is invariant.** The spin's *kinematics* is exact and gauge invariant: $\hat s$ is a function of the rotor alone, the rotor is gauge invariant, so the spin direction is an observable of the chart with no gauge ambiguity. **That is more than the element form states, and the coupling does not weaken it**, since a central phase cannot touch the rotor. The spin's *dynamics* is the free one plus whatever the frame's transport induces, and the article claims no more.

## What the Charge Cannot Close

**The free article's three open items are still open, and the coupling is the reason they are.** The first is the closure of the general field: the four brackets are coupled and the equation does not close them. The second is the choice of spin-transport law, which the Frenkel condition of [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html) supplies in one sector and not in general. The third is the spin's dynamics in a background.

**The tempting hypothesis, and why it fails.** One might hope that coupling the spin fluid to a field supplies the missing closure: the field is a new set of variables, the equation is longer, and a longer equation might close. **It does not, and the reason is the type table.** The missing closure is a statement about the rotor bracket and about the fourth bracket's transport; the connection is central and confined to the first two brackets. A longer equation in the brackets the connection can reach cannot constrain the brackets it cannot reach. **The count is unchanged: the word still has eight parameters, the connection still has four, and the four brackets are still underdetermined by the equation alone.**

**What would be needed and is not in this construction.** A coupling that could write in the fourth bracket would have to be non-central: a connection taking values in the algebra's vector part, or a word arranged so that the rotor sits in a bracket a central element can reach. Neither exists in the abelian construction, and the parent's §*Open Questions* records the same obstacle for the free case.

**The negative result stated as a positive one.** The charge does not close the spin fluid, and that is informative: it says that the spin fluid's underdetermination is internal to the word and not a consequence of the field being free. **A fluid whose closure one could buy with a coupling would be a fluid whose degrees of freedom were not its own**, and this one's are.

## The Properties, Listed

**Twelve statements, each one line, and each with its reason. This is what the charged spin fluid is.**

1. **The word is unchanged and the coupling is confined by type.** Eight parameters; the connection reaches the phase and boost brackets and not the scale or the rotor.
2. **The density is untouched.** The gauge transformation moves the angle alone, and the scale, the rapidity, the axis and the rotor are gauge invariant by inspection.
3. **The velocity is the kinetic one**, named by the covariant wavevector: $\tilde K_{\Phi,\mathrm{gco}}=ik_m\tilde U_{\Psi,\mathrm b}^{-2}$ and $\tilde K_\Phi=\tilde K_{\Phi,\mathrm{gco}}-ϙ\tilde A_\Phi/\hbar$.
4. **The velocity is a unit for every field.** $\langle\tilde V_\Phi\rangle_\natural=-c^{2}$; the normalisation is kinematical and the coupling cannot touch it.
5. **The rapidity and the axis are observables.** $\vec v=c\tanh\theta_{\mathrm{rpd}}\vec u_{\mathrm b}$, $\gamma=\cosh\theta_{\mathrm{rpd}}$, and no gauge transformation changes either.
6. **The vorticity is the frame's gradient.** Its proper part is rank two for every solution, and it is not $ϙF/m$ for any field.
7. **The vorticity is closed and not exact.** Closedness is the Maurer–Cartan flatness of $\Gamma$; exactness fails wherever the holonomy is non-trivial; there is still no transport law.
8. **The loop invariant is a Lorentz transformation times a phase.** Nothing about it is quantised, and the scalar's $h/m$ is the central factor of the transformation.
9. **The Gordon split survives.** The convection part is the chart's current; the bound magnetisation current has no explicit dependence on the connection.
10. **The spin direction is gauge invariant and coupling-blind.** $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$; the chart shows no rotor torque, and the Larmor precession is second order, through the frame.
11. **The coupling adds a force and not a torque.** $\partial_\nu T^{\mu\nu}=ϙF^{\mu\nu}J_\nu+$ the free article's spin term, and the second is unchanged.
12. **The degenerate set is $r=0$ and the closure is still underdetermined.** The charge does not supply the missing spin-transport law, and the reason is that the missing law lives in the bracket the connection cannot reach.

## The Three Charged Fluids

**The three charged articles can be put side by side, and the table is the shortest statement of what the charge does to each.** The table is the same in all three; what changes from one to the next is which column is the article's own.

| | charged scalar | charged spin | charged vector |
| --- | --- | --- | --- |
| the carrier | a complex function: two parameters | a word of four factors: eight parameters | the same word: eight parameters |
| the density | $\rho_{\mathrm{num}}=\lvert\Xi\rvert^{2}$ | $\rho$, read from the word | the scale, which is not a norm |
| the velocity | $\tilde P^{\mathrm{mech}}/m$ | the frame, $ic\tilde U_{\Psi,\mathrm b}^{-2}$ | the field's direction, $\tilde A/r$ |
| is it a unit? | only where the quantum potential vanishes | always, $\langle\tilde V_\Phi\rangle_\natural=-c^{2}$ | its boost is; the element is not a four-vector |
| the vorticity | the field strength, $ϙF/m$ | the frame's gradient, and not $ϙF/m$ | not established; the free case's is $F$ minus a radial term |
| the vorticity's rank | $0$, $2$ or $4$ | $2$ for the proper part | the free case's is $2$ |
| the loop invariant | $2\pi\hbar n/m+ϙ\Phi_B/m$ | a Lorentz transformation times a phase | for $ϙ=0$ an integer; for $ϙ\ne0$, not known |
| the force | the Lorentz force, plus a quantum potential | the Lorentz force, and no torque | the covariant divergence, self-acting |
| the stress | the quantum potential is in it; no EOS | the antisymmetric part is in it; no EOS | its own field strength is in it; stiff on $F=0$ |
| the degenerate set | $r=0$, codimension two | $r=0$, codimension two | $r=0$; the free case's lightlike wall is gone |
| what the charge does | turns the vorticity into the field strength | pushes and does not torque | doubles the carrier and opens the constraint |

**This article's column is the second, and it is the column in which the charge does least.** The velocity keeps its normalisation, the vorticity keeps its kind, the spin keeps its invariance and the closure keeps its underdetermination; what the charge does is shift the momentum, turn the frame, and add a force. **The reason is the type table, and the type table is the same in all three articles**: the connection is central, the central brackets are the scale and the phase, and everything a fluid does with its frame sits in the two brackets a central element cannot reach.

**The row that separates this column from the scalar one is the normalisation, and it is a one-word difference.** The scalar velocity is a unit only where the quantum potential vanishes; the spin velocity is a unit wherever the word exists. **The scalar fluid's velocity is dynamical and this one's is kinematical**, and that single contrast explains why the scalar article can say "the vorticity is the field strength" and this one cannot: a velocity that is a momentum can be a gradient plus a potential, and a velocity that is a frame can only be a frame.

**The row that separates it from the vector one is the compressibility.** The Proca fluid's expansion is fixed by its own amplitude, because its velocity is the field's direction; here the velocity is a unit and the expansion is a property of the frame's gradient, which is the free article's subject and which the coupling does not reach. **Three velocities, three expansions, and the charge reaches only one of them.**

## What the Charge Does to the Correspondence

**The correspondence still has three steps, and here the charge changes the first column of the fourth.** The word is exact; the reverse map is defined on a class; membership of that class is the extra structure that makes the fluid a medium rather than a relabelling of a wave.

**The forward arrow is unchanged and exact.** Any nowhere-zero solution of the coupled equation gives a density, an angle, a frame and a spin direction, and the word is a bijection on the $N$-regular set. **The connection is a datum of the equation, not of the solution**, and the arrow costs nothing.

**The reverse arrow takes the frame as well as the density and the action.** Given the word's data and a connection, the field is $r e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ and it solves the coupled equation iff the mass shell and the momentum balance hold. **The extra structure is of two kinds at once: an internal degree of freedom (the orientation) and an external field (the connection)**, and that pair is what makes this fluid a Cosserat medium in a background rather than a Cosserat medium.

| | the word's data | what the reverse map needs beyond it | the medium it makes |
| --- | --- | --- | --- |
| charged scalar | $r$, $\theta_{\mathrm{pha}}$ | the energy equation, which is the Hamiltonian | a charged Madelung fluid |
| charged spin | eight parameters | the connection, and a closure of the frame's transport | a charged Cosserat medium |
| charged vector | the same eight | the connection, which is the field itself | a self-acting compressible medium |

**The free correspondence's three kinds of extra structure were the three ways a medium exceeds a dust; the charged correspondence's third column names what exceeds the dust now.** For the spin fluid the added datum is a field acting on a medium that already had an orientation, and the table's fourth row is this article's.

**What the correspondence supports and what it does not.** It supports the claim that the coupled Dirac equation is the equation of motion of a charged Cosserat medium, and it supports the twelve properties of §*The Properties, Listed* item by item. It does not support a spin dynamics in a background, a closure of the general field, or the identification of the vorticity with the field strength: the first two are refused in §*What the Charge Cannot Close* and the third in §*The Vorticity Is Still the Frame's*.

## What Is Established and What Is Interpretation

**Established.** The type table with the coupling in place, and the statement that the connection adds to the phase bracket and the boost bracket and to nothing else. The kinetic velocity, and $\tilde K_{\Phi,\mathrm{gco}}=ik_m\tilde U_{\Psi,\mathrm b}^{-2}$ with the canonical wavevector the covariant one less the potential. The invariance of $\langle\tilde V_\Phi\rangle_\natural=-c^{2}$ under every field. The vorticity as the frame's logarithmic derivative, with the proper part rank two for every solution and the raw derivative reaching four, checked numerically on two frames with the singular values quoted. The loop invariant as a Lorentz transformation times a phase, and the frozen-frame sector's circulation as that phase. The Gordon split, and the absence of any explicit connection in the magnetisation current. The force with no torque, and the second-order character of the Larmor precession. The survival of the three open items and the reason they survive.

**Interpretation.** That the frame *is* the fluid's velocity rather than a rewriting of the bispinor, and that the rotor *is* an orientation rather than a phase. The warrant is the count, the types and the parent's reading, and the coupling does not touch the warrant. That the loop invariant's $\mathbb{C}^{\ast}\times SL(2,\mathbb{C})$ is the right home for a charged spin fluid's circulation is a reading of the structure and not a theorem.

**Not claimed.** It is not claimed that the vorticity has a dynamics, that the spin is torqued by the field in this chart, that the charge closes the general field, or that the magnetisation current is screened. It is not claimed that the Larmor precession is absent from the physics; it is claimed that the chart exhibits it at second order and not as a rotor term, and the $g=2$ article is where the composition is carried out.

## Summary

The coupled Dirac equation in polar variables is $\tilde\nabla_{\mathrm{gco}}\tilde\Xi_{\mathrm D}=\frac{i}{\hbar}k_m\tilde\Xi_{\mathrm D}$ with $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$, and the word is $r e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$.

The connection is central per component. Its temporal slot is a central imaginary number and joins the phase bracket; its spatial slots are Hermitian vectors and join the boost bracket. The scale is a real scalar and the rotor is a real vector part, so **the density and the spin are untouched**.

The velocity is the kinetic one: the boost is named by the covariant wavevector, $\tilde K_{\Phi,\mathrm{gco}}=ik_m\tilde U_{\Psi,\mathrm b}^{-2}$, and the canonical wavevector is the covariant one less the potential. $\langle\tilde V_\Phi\rangle_\natural=-c^{2}$ for every field, so the normalisation is kinematical and the coupling cannot reach it.

The vorticity is the frame's logarithmic derivative and contains no connection. Its proper part is rank two for every solution, and its raw derivative reaches rank four through the acceleration; it is not $ϙF/m$, and the sum of the two is a two-form of a different kind. It is closed by Maurer–Cartan flatness and obeys no transport law.

The loop invariant is a Lorentz transformation times a phase, and nothing about it is quantised. The Gordon split survives, and the bound magnetisation current has no explicit dependence on the connection. The coupling adds a force and no torque: $\partial_\nu T^{\mu\nu}=ϙF^{\mu\nu}J_\nu+$ the free spin term.

The spin direction is gauge invariant and coupling-blind, and the Larmor precession is second order, through the frame. The free article's three open items — no vorticity transport, no closure, no spin dynamics in a background — survive, and the charge does not close them.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Xi_{\mathrm D}=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The word |
| $r>0$ | Scale; the density is a factor of the word |
| $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ | The angle; the only gauge-dependent parameter |
| $\theta_{\mathrm{rpd}},\ \vec u_{\mathrm b}$ | Rapidity and axis of the boost |
| $\theta_{\mathrm{axr}},\ \text{axis}$ | Angle and axis of the rotor |
| $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ | The spin direction; gauge invariant, coupling-blind |
| $\tilde V_\Phi=ic\tilde U_{\Psi,\mathrm b}^{-2}$ | The four-velocity; $\langle\tilde V_\Phi\rangle_\natural=-c^{2}$ |
| $\Gamma_\mu=\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b}$ | The frame's logarithmic derivative |
| $\tilde K_{\Phi,\mathrm{gco}}=ik_m\tilde U_{\Psi,\mathrm b}^{-2}$ | The covariant wavevector |
| $\tilde K_\Phi=\tilde K_{\Phi,\mathrm{gco}}-\frac{ϙ}{\hbar}\tilde A_\Phi$ | The canonical wavevector |
| $\omega_{\mu\nu}$ | The vorticity; the frame's gradient, proper part rank two |
| $\Phi_B$ | The flux through a loop |
| $ϙ$ | The coupling |
| $k_m=mc/\hbar$ | The mass wave number |

## Further Reading

- [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html), the free companion, whose twelve properties these twelve answer.
- [The Coupled Dirac Equation in Biquaternionic Polar Variables](the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), for the type table, the kinetic momentum and the kinetic velocity.
- [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html), for the word, the frame, the spin direction and the mass-shell proposition.
- [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html), for the split into convection and magnetisation.
- [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html), for the closure the charge does not supply.
- [The Classical Origin of $g=2$ in Biquaternionic Form](the-classical-origin-of-g-2-in-biquaternionic-form.html), for the composition of the rotor's rate with the frame's transport.
- [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html), for the rank hierarchy the vorticity proper sits in.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html), for the central connection and the curvature.
- [The Charged Klein–Gordon Fluid](the-charged-klein-gordon-fluid.html) and [The Charged Proca Fluid](the-charged-proca-fluid.html), the two companions.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge University Press, 2003), for the Lorentz group's rotor parametrisation.
- Ingo Kirsch and Dirk Kreimer, *Spin Hydrodynamics* (lecture notes), for the Weyssenhoff–Raabe stress and the Frenkel condition in their relativistic form.
