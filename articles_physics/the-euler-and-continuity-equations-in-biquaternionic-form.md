# __The Euler and Continuity Equations in Biquaternionic Form__

## Introduction

**An ordinary fluid carries five real numbers at each point, and none of them is a wave function's amplitude or phase.** The five are a density, a velocity with three components, and a thermodynamic state. The equations that close them are the continuity equation, the Euler equation and a law of state. This article writes that system in the notation of the algebra, and the writing is exact: each equation below is the classical equation with no term added, dropped or rescaled.

**The objection is that the writing is empty.** Euler's equation is a vector equation, the algebra has a vector part, and any notation that can write a vector can write Euler. A translation that changes nothing has explained nothing.

**The answer is that the translation buys a count, and the count is what the rest of this section spends.** The field of the block is one element of $\mathbb{B}$ at each event, and that element carries eight real data. The fluid carries five. The difference is not a defect of the writing; it is the distance between a fluid and a wave equation, and it is the subject of the eight articles that follow this one. The count is exact, it is stated here once, and every later article names which of the five data it discards and why.

**The algebra's complex structure is not used anywhere in this article.** That absence is the first measurement. The fluid's equations are one real scalar equation and one real vector equation; a wave equation is one complex equation whose unknown occupies all four slots of the element. A reader who expects the second will not find it here, and the reason is structural: the temporal slot of the flow element is the constant $ic$, so the scalar slot carries no unknown for an equation to act on.

**Nothing in this article is quantum and nothing is relativistic.** There is no $\hbar$, no mass shell and no Lorentz transformation. The flow element introduced in §*The Flow Element* is the Galilean one, and the relativistic normalisation is one factor away, a factor that no equation written here reads.

## The Data

**The fluid at a point is a density, a velocity, a pressure and an entropy per unit mass.** The density is the number density $\rho_{\mathrm{num}}$, the count of markers per unit volume, and the mass density is $\rho_{\mathrm{mass}}=m\rho_{\mathrm{num}}$ with $m$ the mass of one marker. The velocity is $\vec v$, a vector of $\mathbb{B}_V$ with three real components. The pressure is $p_{\mathrm{th}}$, the thermodynamic pressure, and the entropy is the specific entropy $s_{\mathrm{spc}}$, entropy per unit mass, with the entropy density $s_{\mathrm{ent}}=\rho_{\mathrm{mass}}s_{\mathrm{spc}}$.

**The pressure is not an independent datum once a law of state is given.** The law of state is the relation

$$
p_{\mathrm{th}}=p_{\mathrm{th}}\bigl(\rho_{\mathrm{mass}},s_{\mathrm{spc}}\bigr),
$$

and it is data of the fluid, not a consequence of the other equations. A fluid without a law of state is not a fluid but a family of fluids. The distinction is the whole of §*The Count*, and it returns in [The Equation of State and the Barotropic Condition](the-equation-of-state-and-the-barotropic-condition.html).

**The three equations are these.** In the flat coordinates and with $t'=r'_t/c$ the time in seconds,

$$
\partial_{t'}\rho_{\mathrm{mass}}+\nabla\cdot\bigl(\rho_{\mathrm{mass}}\vec v\bigr)=0,
$$

$$
\partial_{t'}\vec v+\bigl(\vec v\cdot\nabla\bigr)\vec v=-\frac{1}{\rho_{\mathrm{mass}}}\nabla p_{\mathrm{th}}+\vec f_{\mathrm{ext}},
$$

$$
\partial_{t'}s_{\mathrm{spc}}+\vec v\cdot\nabla s_{\mathrm{spc}}=0 .
$$

The first is the continuity equation, the second is Euler's equation with an external force per unit mass $\vec f_{\mathrm{ext}}$, and the third says that the specific entropy is carried by the flow. A barotropic fluid drops the third equation and the entropy with it, and the pressure becomes a function of the density alone.

**The dissipation is absent, and its absence is a hypothesis.** The Euler equation has no term that turns kinetic energy into heat. A fluid with such a term obeys the Navier–Stokes equation instead, and the difference is the subject of [Viscosity and the Rayleigh Dissipation Function](viscosity-and-the-rayleigh-dissipation-function.html). Here the flow is inviscid, and that is a choice made at the start rather than a result.

## The Flow Element

**The flow assembles into one element of $\mathbb{B}_{\Phi}$ with the speed as its unit.** The four coefficients of an element share one unit, so the temporal slot must carry a speed and not a length, and the element is

$$
\tilde V_\Phi=i c\,e_t+\vec v,
\qquad
\vec v=v_x\,\vec e_x+v_y\,\vec e_y+v_z\,\vec e_z .
$$

The $i$ on the temporal slot is the one the corpus puts on every material element: the temporal coefficient of $\tilde R_\Phi$ is $i r'_t$, and the derivative with respect to that coefficient is $-i\partial_{r'_t}$. The flow element is the displacement over a unit of material time, and the $c$ is what makes its four coefficients commensurable.

**The element's norm is the Lorentz factor, in the inverse.** The quaternionic norm of the flow element is

$$
\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}+\lvert\vec v\rvert^{2}=-\frac{c^{2}}{\gamma^{2}},
\qquad
\gamma=\frac{1}{\sqrt{1-\lvert\vec v\rvert^{2}/c^{2}}} .
$$

So the Galilean flow element is not a unit element, and its norm is the reciprocal square of the Lorentz factor rather than $-c^{2}$. The block's relativistic articles normalise the flow to $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$, and the element they use is

$$
\tilde V_{\Phi,\mathrm{rel}}=\gamma\,\tilde V_\Phi=i c\gamma\,e_t+\gamma\vec v .
$$

**The two differ by one factor on the whole element, and no equation in this article reads it.** Multiplying an element by a central real scalar multiplies all four coefficients, so the difference between the two writings is a single number at each point. Euler's equation below is Galilean, so it is written on the unnormalised element; the block's relativistic articles write it on the normalised one. An article that mixed the two would carry a factor $\gamma$ that no term accounts for, and this one does not mix them.

**The velocity is the vector part and not the spatial part of a four-vector.** This is the distinction that the block's relativistic articles make and that a classical fluid does not have. For the Galilean element, $\vec v$ is the vector part; for the normalised one, $\gamma\vec v$ is. The two are not related by a relabelling, because $\gamma$ is a function of position, and §*The Vorticity* of [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html) draws the consequence for the curl.

## The Material Derivative Is a Pairing

**The material derivative is the scalar product of the flow with the gradient.** With the material gradient $\tilde\nabla_\Phi=-i e_t\,\partial_{r'_t}+\vec\nabla$ and the general quaternionic bilinear form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\sum_\mu Q_{1\mu}Q_{2\mu}$, the identity is

$$
\bigl\langle\tilde V_\Phi,\tilde\nabla_\Phi f\bigr\rangle_{\natural}=c\,\partial_{r'_t}f+\vec v\cdot\nabla f
$$

for every differentiable scalar $f$. The right-hand side is the derivative along the flow, $\mathrm{D}_{\mathrm{mat}}f$ with $\mathrm{D}_{\mathrm{mat}}=c\,\partial_{r'_t}+\vec v\cdot\nabla=\partial_{t'}+\vec v\cdot\nabla$.

**The identity is exact and it is checked by expansion.** The temporal slot contributes $ic\cdot(-i\partial_{r'_t}f)=+c\partial_{r'_t}f$, because $(-i)(i)=+1$; the three spatial slots contribute $v_\eta\partial_\eta f$ each, and the sum is the convective term. No term is dropped and no sign is chosen: the $+1$ of the temporal slot and the $+1$ of each spatial slot are the same $+1$, the one of the pairing.

**The pairing is not the product, and the difference is the sign that a fluid cannot afford.** In the quaternion product the scalar part is $a_tb_t-\vec a\cdot\vec b$, because $\vec e_\eta^{2}=-e_t$, so the product of the flow with the gradient gives $c\partial_{r'_t}f-\vec v\cdot\nabla f$, the material derivative with the convective term reversed. The pairing gives the sum. A fluid's convective term is a sum and not a difference, so the fluid's natural bilinear in this algebra is $\langle\cdot,\cdot\rangle_{\natural}$, and the product is reserved for the object that will replace the fluid, in [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html).

## Continuity Is One Pairing

**The current element is the flow weighted by the density.** It is

$$
\tilde J_\Phi=\rho_{\mathrm{num}}\,\tilde V_\Phi=i c\rho_{\mathrm{num}}\,e_t+\rho_{\mathrm{num}}\vec v,
$$

the four-current of the markers, with the temporal slot carrying $c\rho_{\mathrm{num}}$ and the vector part carrying the flux $\rho_{\mathrm{num}}\vec v$.

**The continuity equation is the vanishing of one pairing.** The identity

$$
\bigl\langle\tilde\nabla_\Phi,\tilde J_\Phi\bigr\rangle_{\natural}
=c\,\partial_{r'_t}\rho_{\mathrm{num}}+\nabla\cdot\bigl(\rho_{\mathrm{num}}\vec v\bigr)
$$

holds, and the continuity equation is its vanishing. The check is the same expansion: the temporal slot gives $(-i\partial_{r'_t})(ic\rho_{\mathrm{num}})=+c\partial_{r'_t}\rho_{\mathrm{num}}$, and the three spatial slots give the divergence.

**The rest of the product is not an equation of the fluid, and it is worth naming so that nobody imposes it.** The element $\tilde\nabla_\Phi\tilde J_\Phi$ has a vector part as well as a scalar part, and its vanishing would be the statement that the current is harmonic in a stronger sense than conservation. A fluid conserves markers; it does not require its current to be harmonic. So the continuity equation is one component of one element identity, and the block never writes the other three as a law.

## Euler Is One Element Equation

**The material derivative of the flow element is a pure vector, and Euler is the statement of what it equals.** Since the temporal coefficient $ic$ is a constant, $\mathrm{D}_{\mathrm{mat}}\tilde V_\Phi$ has no scalar part and

$$
\mathrm{D}_{\mathrm{mat}}\tilde V_\Phi
=-\frac{1}{\rho_{\mathrm{mass}}}\nabla p_{\mathrm{th}}+\vec f_{\mathrm{ext}} .
$$

The left-hand side is the element whose vector part is $\mathrm{D}_{\mathrm{mat}}\vec v$ and whose scalar part is zero; the right-hand side is a pure vector because both terms are gradients and forces. The equation is therefore three real equations, one per spatial slot, and the temporal slot reads $0=0$.

**The equation is one element equation and the fluid is two.** Continuity is one pairing, a scalar; Euler is one element equation carrying three. Together they are four real equations, and §*The Count* says what they close.

## The Count

**The count is the article's content, and it is stated as a table.** The element of the field and the fluid are counted in the same currency, the real numbers each carries at a point.

| Object | Continuous data at a point | What they are |
|---|---|---|
| The field element $\tilde\Xi$ | $8$ | scale, phase, boost $(3)$, rotor $(3)$ |
| The scalar field in its word | $2$ | scale, phase |
| A general fluid | $5$ | $\rho_{\mathrm{num}}$, $\vec v$, $s_{\mathrm{spc}}$ |
| A barotropic fluid | $4$ | $\rho_{\mathrm{num}}$, $\vec v$ |
| A barotropic irrotational fluid | $2$ | $\rho_{\mathrm{num}}$, the potential $S$ |

**The field's eight are the block's own count, and the fluid's five are the classical count.** The first row is the count of [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html), $1+1+3+3=8$. The third row is the count of this article: one density, three velocity components, one thermodynamic datum, with the pressure a function of the last two.

**The difference is three data, and each of them is a datum the field does not have.** The fluid's velocity has three components where the field's phase has one, and that excess is the vorticity, removed in [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html). The fluid's entropy is a second thermodynamic datum, and the field has no thermodynamic datum at all; that excess is removed in [The Equation of State and the Barotropic Condition](the-equation-of-state-and-the-barotropic-condition.html). The pressure itself is the third, and it is not a datum that can be removed by counting: it is a *term*, and its removal is the subject of [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html).

**The last two rows are the same two numbers, and that coincidence is not one.** A barotropic irrotational fluid carries $\rho_{\mathrm{num}}$ and the potential $S$; a scalar wave function carries a modulus and an argument. The two counts agree at two, and the agreement is exact rather than approximate: the map between them is a bijection wherever both exist. What the agreement does not give is a linear equation, and the reason is in the next section.

## What the Algebra Does Not Do

**The complex structure is unused, and the reason is the constant on the temporal slot.** A wave equation is one equation for one unknown that occupies all four slots of an element. The fluid's pair is not: the unknown $\vec v$ occupies three slots, the unknown $\rho_{\mathrm{num}}$ occupies none of them, and the temporal slot is occupied by the constant $ic$. So no multiplication by $i$ of an unknown, no second-order operator and no phase appear in the two equations.

**This is why the pair cannot be fused into one complex equation.** A fusion would require the two real equations to be the real and imaginary parts of one equation, which requires the two unknowns to be the two parts of one complex number. The fluid's unknowns are a scalar and a vector, and the vector is three-dimensional, so there is no complex number whose parts they are. The fusion exists for the field, not for the fluid, and the map that performs it is the reverse map of the later article.

**What the algebra does supply is the count and the signs.** The two identities of this article are exact statements about the algebra's bilinear form, they fix the sign of the convective term, and they exhibit the temporal slot as the slot the fluid does not use. A reader who wants the algebra to add something to Euler will be disappointed; a reader who wants the reason the fluid is not a wave equation will find it in the empty slot.

## What Is Established and What Is Interpretation

**Established.** That the continuity equation is the vanishing of the pairing $\langle\tilde\nabla_\Phi,\tilde J_\Phi\rangle_{\natural}$, and that the material derivative is the pairing $\langle\tilde V_\Phi,\tilde\nabla_\Phi\,\cdot\,\rangle_{\natural}$, both by expansion. That the flow element's norm is $-c^{2}/\gamma^{2}$ in the Galilean writing and $-c^{2}$ in the normalised one, the two differing by the factor $\gamma$ on the whole element. That the fluid closes on five data in general and on four in the barotropic case, and that the field carries eight.

**Interpretation.** That the count is the right measure of the distance between the fluid and the field. The count is exact; that it *should* decide whether a wave equivalent exists is the programme's step, and the later articles take it and find that the count is necessary and not sufficient. That the bilinear form used for the fluid is the natural one is also a reading: the algebra supplies the pairing, and the fluid's convective term singles it out.

**Not claimed.** It is not claimed that the fluid's equations are approximations of the field's. They are the classical equations, exact in their own domain, and the field's equations are a different system. It is not claimed that the algebra improves the classical theory: every identity here is a rewriting, and a rewriting that adds no prediction is what it is.

## Summary

An ordinary fluid carries five real data at each point — a number density, a velocity, a specific entropy — and the pressure is fixed by a law of state. Continuity, Euler and the advection of entropy close them.

In the algebra the flow is one element, $\tilde V_\Phi=i c\,e_t+\vec v$, with the speed as the unit of its four coefficients and the norm $-c^{2}/\gamma^{2}$. The relativistic normalisation multiplies the whole element by $\gamma$ and changes no equation written here.

The material derivative is the pairing $\langle\tilde V_\Phi,\tilde\nabla_\Phi f\rangle_{\natural}=c\partial_{r'_t}f+\vec v\cdot\nabla f$. The product would reverse the sign of the convective term, because $\vec e_\eta^{2}=-e_t$, so the fluid's bilinear is the pairing and not the product.

Continuity is the vanishing of one pairing, $\langle\tilde\nabla_\Phi,\tilde J_\Phi\rangle_{\natural}=0$ with $\tilde J_\Phi=\rho_{\mathrm{num}}\tilde V_\Phi$. Euler is one element equation whose scalar slot reads $0=0$ and whose three vector slots are the three components of the acceleration law.

The count is five against eight. A barotropic fluid has four, an irrotational barotropic fluid two, and a scalar wave function two. The two at the end agree, and the agreement is a bijection of states and not a linearity of equations.

The complex structure is unused. The temporal slot holds the constant $ic$, so no unknown occupies it, and the pair cannot be the real and imaginary parts of one complex equation. That empty slot is the structural difference between a fluid and a wave equation, and it is what the reverse map has to fill.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_{\mathrm{num}}$ | Number density of markers |
| $\rho_{\mathrm{mass}}=m\rho_{\mathrm{num}}$ | Mass density |
| $\vec v$ | Three-velocity, the vector part of $\tilde V_\Phi$ |
| $p_{\mathrm{th}}$ | Thermodynamic pressure |
| $s_{\mathrm{spc}}$ | Specific entropy, entropy per unit mass |
| $s_{\mathrm{ent}}=\rho_{\mathrm{mass}}s_{\mathrm{spc}}$ | Entropy density |
| $\vec f_{\mathrm{ext}}$ | External force per unit mass |
| $\tilde V_\Phi=i c\,e_t+\vec v$ | Galilean flow element |
| $\tilde V_{\Phi,\mathrm{rel}}=\gamma\tilde V_\Phi$ | Normalised, relativistic flow element |
| $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}/\gamma^{2}$ | Its quaternionic norm |
| $\gamma=1/\sqrt{1-\lvert\vec v\rvert^{2}/c^{2}}$ | Lorentz factor |
| $\tilde J_\Phi=\rho_{\mathrm{num}}\tilde V_\Phi$ | Current element |
| $\tilde\nabla_\Phi=-i e_t\partial_{r'_t}+\vec\nabla$ | Material gradient |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\sum_\mu Q_{1\mu}Q_{2\mu}$ | General quaternionic bilinear form |
| $\mathrm{D}_{\mathrm{mat}}=c\partial_{r'_t}+\vec v\cdot\nabla$ | Material derivative |
| $r'_t=c t'$ | Material time coordinate, a length |
| $m$ | Mass of one marker |
| $c$ | Limiting speed of the frame structure |

## Further Reading

- Leonhard Euler, "Principes généraux du mouvement des fluides," *Mémoires de l'Académie des Sciences de Berlin* **11** (1757) 274–315, for the equation that carries his name and for the pressure as the gradient of a scalar.
- Claude-Louis Navier, "Mémoire sur les lois du mouvement des fluides," *Mémoires de l'Académie Royale des Sciences* **6** (1822) 389–440, and George Gabriel Stokes, "On the theories of the internal friction of fluids in motion," *Transactions of the Cambridge Philosophical Society* **8** (1845) 287–305, for the viscous term whose absence this article assumes.
- Hermann von Helmholtz, "Über Integrale der hydrodynamischen Gleichungen, welche den Wirbelbewegungen entsprechen," *Journal für die reine und angewandte Mathematik* **55** (1858) 25–55, for the vorticity theorems that the next article reads as an obstruction.
- Lev D. Landau and Evgeny M. Lifshitz, *Fluid Mechanics*, 2nd ed. (Pergamon, 1987), §§2, 4 and 15, for the system of this article and for the counting of its data.
- George K. Batchelor, *An Introduction to Fluid Dynamics* (Cambridge University Press, 1967), ch. 3, for the stress and the equations of motion.
- The companion articles: [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html), [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html), [Viscosity and the Rayleigh Dissipation Function](viscosity-and-the-rayleigh-dissipation-function.html), [The Equation of State and the Barotropic Condition](the-equation-of-state-and-the-barotropic-condition.html), [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html).
- [Lagrangian and Hamiltonian Mechanics in Biquaternionic Form](lagrangian-and-hamiltonian-mechanics-in-biquaternionic-form.html), for the classical formalism whose fluid limit this system is, and [The Klein–Gordon Fluid](the-klein-gordon-fluid.html), for the same variables read from the field.
