# The Lagrangian of the Schrödinger Fluid

## Introduction

**This article writes the action in the fluid's variables and varies them.** [The Schrödinger Fluid](the-schrodinger-fluid.html) reads the equation and names the density, the velocity and the quantum potential. Here the same field is written as an action over the density and the phase, and the Euler–Lagrange equations are read. Nothing about the equation changes; what changes is which object is primitive.

**Three results, and each is a computation.**

*First, the action has two terms and the fluid's two ingredients are those terms.* Written in $\rho_{\mathrm{num}}$ and $S$, the Lagrangian density is

$$
\mathcal L_{\mathrm{fl}}=-\rho_{\mathrm{num}}\Bigl(\partial_{t'}S+\frac{(\nabla S)^{2}}{2m}+V\Bigr)-\frac{\hbar^{2}}{2m}(\nabla r)^{2},
$$

a phase term, a kinetic term, a gradient energy and an external potential. There is no quantum potential in it and no barotropic pressure: no term is a function of the density alone. The quantum potential appears only after the variation, as the derivative of the third term, and the pressure that term implies is a Korteweg stress.

*Second, the two variations give the fluid's two equations directly.* Varying $S$ gives continuity; varying $r$ gives the quantum Hamilton–Jacobi equation; the acceleration law is its gradient and is not a third equation. The wave equation is nowhere in the derivation, and the fluid's equations are not a reading of it here but its Euler–Lagrange content in another chart.

*Third, the velocity is not canonical.* No time derivative of $\vec v$ appears, so its conjugate momentum vanishes identically on every configuration. That is the fluid form of the four vanishing momenta of [The Variational Principle and the Dirac Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-dirac-equation-in-biquaternionic-polar-variables.html), at the rung where only one of the four survives to be stated.

**Position in the block.** This is the variational companion of [The Schrödinger Fluid](the-schrodinger-fluid.html), and the first of the eight articles that write the action in the fluid variables. It sits at the bottom of the scalar ladder: at this rung the velocity has no norm, the density is the charge density, and the quantum potential carries the Laplacian, so every statement below is unconditional.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, $e_t=1$, $\vec e_\mu^{2}=-e_t$, $i$ central, $\mathrm{Sc}$ the coefficient of $e_t$, $\mathrm{Tr}=2\,\mathrm{Sc}$. The conjugations are $*$ and $^{\natural}$; the pairing is $\mathrm{Sc}(\cdot^{*}\cdot)$ throughout. The field is the central one, $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon\,e_t$ with $r>0$ and $\varepsilon=\pm1$, so $\rho_{\mathrm{num}}=r^{2}$ and $S=\hbar\theta_{\mathrm{pha}}$. The time variable is $t'$ and the material time is $r'_t=ct'$; at this rung only $t'$ appears, because the equation has one time derivative. The action is a functional of two real fields over $(t',\vec r)$, and the domain is $r>0$, which excludes the nodal set.

## The Action in the Fluid Variables

**The element action is the one the polar companion varies, and the substitution is the word.** With $\tilde\Xi=r e^{i\theta}\varepsilon e_t$, the three bilinears that appear are

$$
\mathrm{Re}\,\mathrm{Sc}\bigl[i\tilde\Xi^{*}\partial_{t'}\tilde\Xi\bigr]=-\rho_{\mathrm{num}}\,\partial_{t'}\theta_{\mathrm{pha}},
\qquad
\mathrm{Re}\,\mathrm{Sc}\bigl[\partial_j\tilde\Xi^{*}\partial_j\tilde\Xi\bigr]=(\partial_jr)^{2}+r^{2}(\partial_j\theta_{\mathrm{pha}})^{2},
\qquad
\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde\Xi\bigr)=\rho_{\mathrm{num}} .
$$

The first is the whole of the kinetic term: the scale contributes $\pm ir\dot r$, which is imaginary and drops out of the real part, so the density carries no inertia at this rung. The second splits cleanly into the amplitude's gradient and the phase's gradient, and the split is exact because the two factors of the word commute — $\varepsilon$ is central and $e^{i\theta}$ is central, so no cross term survives. The third is the density and nothing else, because the phase cancels against its conjugate and $\varepsilon^{2}=1$.

**Substituting and multiplying by $\hbar$ gives the Lagrangian in the fluid's variables.**

$$
\boxed{\;\mathcal L_{\mathrm{fl}}=-\rho_{\mathrm{num}}\Bigl(\partial_{t'}S+\frac{(\nabla S)^{2}}{2m}+V\Bigr)-\frac{\hbar^{2}}{2m}(\nabla r)^{2}\;}
$$

The four terms are, in order, the phase term, the kinetic energy of the flow, the external potential's energy, and the energy stored in the density's gradient. The last is the only term that survives when the phase is constant, and it is the whole of the quantum effect: a fluid at rest with a non-uniform density has an energy, and a classical fluid at rest does not.

**The coefficient of the gradient energy is fixed by the mass and by nothing else.** It is $\hbar^{2}/2m$ per unit of $(\nabla r)^{2}$, which is $\hbar^{2}/8m$ per unit of $(\nabla\rho)^{2}/\rho_{\mathrm{num}}$. The two forms are the same number and not merely the same up to a total derivative, by the chain rule $\nabla\rho_{\mathrm{num}}=2r\nabla r$, and the second is the form in which the term appears in the Korteweg literature. No other coefficient is available: the term must have two derivatives, must be even in $r$, and must be the only scalar the amplitude can make at that order.

**What is absent is as informative as what is present.** There is no term in $\dot r$ and no term in $\nabla\theta$ that is not inside the square. The first absence is why the density has no kinetic energy of its own; the second is why the flow's energy is the square of a gradient and therefore why the vorticity vanishes identically rather than by a constraint. Both are properties of the first-order rung. At the rung above, the two densities appear and the second absence disappears.

## The Two Variations

**Varying the phase gives continuity, and the variation is one line.** Since $\mathcal L_{\mathrm{fl}}$ depends on $S$ only through $\partial_{t'}S$ and $\nabla S$,

$$
\partial_{t'}\frac{\partial\mathcal L_{\mathrm{fl}}}{\partial(\partial_{t'}S)}+\sum_j\partial_j\frac{\partial\mathcal L_{\mathrm{fl}}}{\partial(\partial_jS)}=0
\qquad\Longrightarrow\qquad
\partial_{t'}\rho_{\mathrm{num}}+\sum_j\partial_j\bigl(\rho_{\mathrm{num}}v_j\bigr)=0,
$$

with $\vec v=\nabla S/m$. The current that appears is the canonical one, $\vec j=\rho_{\mathrm{num}}\vec v$, and it is also the Noether current of the phase shift: the Lagrangian is invariant under $S\mapsto S+\text{constant}$, and the associated density is exactly $\rho_{\mathrm{num}}$. **At this rung the conserved density and the charge density are the same object**, which is why the article can speak of one continuity equation and the relativistic articles cannot.

**Varying the amplitude gives the quantum Hamilton–Jacobi equation.** The variation is taken in $r$ and not in $\rho_{\mathrm{num}}$, because $r$ is the coordinate and $\rho_{\mathrm{num}}=r^{2}$ is a function of it. The gradient term varies as

$$
\delta\int-\frac{\hbar^{2}}{2m}(\nabla r)^{2}=\frac{\hbar^{2}}{m}\int\Delta r\,\delta r,
$$

and the three remaining terms vary as $2r\,\delta r\,[-\partial_{t'}S-\frac{(\nabla S)^{2}}{2m}-V]$. Dividing the Euler–Lagrange equation by $2r$ and using $Q=-\hbar^{2}\Delta r/(2mr)$,

$$
\partial_{t'}S+\frac{(\nabla S)^{2}}{2m}+V+Q=0 .
$$

**That is the fluid's energy equation and it is one equation, not two.** Its gradient is the acceleration law,

$$
\frac{\mathrm{D}\vec v}{\mathrm{D}t}=-\frac{1}{m}\nabla(V+Q),
\qquad
\frac{\mathrm{D}}{\mathrm{D}t}=\partial_{t'}+\vec v\cdot\nabla,
$$

because $\nabla(\nabla S)^{2}/2m=(\vec v\cdot\nabla)\vec v$ when the vorticity vanishes. The two displays are one statement differentiated, and the block's article says the same: continuity, energy and acceleration over-determine a fluid, and here the third is the second's gradient.

**The pair is closed and the count is right.** Two real fields and two real equations, with the velocity a function of the phase. The action has no constraint and needs no multiplier, and that is the first-order rung's privilege: the word has two factors, the two factors are the two fields, and the map is a bijection away from $r=0$. At the rung above, the word has four factors and the count breaks.

## The Quantum Potential Is a Functional Derivative

**The third term of the Lagrangian is the whole of the quantum effect, and the quantum potential is its derivative.** Write the gradient energy as a functional of the density,

$$
\mathcal E_{\mathrm{grad}}[\rho_{\mathrm{num}}]=\frac{\hbar^{2}}{8m}\int\frac{(\nabla\rho_{\mathrm{num}})^{2}}{\rho_{\mathrm{num}}}=\frac{\hbar^{2}}{2m}\int(\nabla r)^{2},
$$

the equality of the two forms being the chain rule, $\nabla\rho_{\mathrm{num}}=2r\nabla r$. Then

$$
\frac{\delta\mathcal E_{\mathrm{grad}}}{\delta\rho_{\mathrm{num}}}=Q .
$$

*Proof.* Varying the first form,

$$
\delta\mathcal E_{\mathrm{grad}}=\frac{\hbar^{2}}{8m}\int\Bigl[\frac{2\nabla\rho_{\mathrm{num}}\cdot\nabla\delta\rho_{\mathrm{num}}}{\rho_{\mathrm{num}}}-\frac{(\nabla\rho_{\mathrm{num}})^{2}}{\rho_{\mathrm{num}}^{2}}\,\delta\rho_{\mathrm{num}}\Bigr],
$$

and one integration by parts turns the first bracket into $-2\delta\rho_{\mathrm{num}}\,[\Delta\rho_{\mathrm{num}}/\rho_{\mathrm{num}}-(\nabla\rho_{\mathrm{num}})^{2}/\rho_{\mathrm{num}}^{2}]$, which with the second leaves $-\delta\rho_{\mathrm{num}}\,[2\Delta\rho_{\mathrm{num}}/\rho_{\mathrm{num}}-(\nabla\rho_{\mathrm{num}})^{2}/\rho_{\mathrm{num}}^{2}]$. With $\Delta\rho_{\mathrm{num}}/\rho_{\mathrm{num}}=2\Delta r/r+2(\nabla r)^{2}/r^{2}$ and $(\nabla\rho_{\mathrm{num}})^{2}/\rho_{\mathrm{num}}^{2}=4(\nabla r)^{2}/r^{2}$, the bracket including its sign is $-4\Delta r/r$ — the two gradient-squared pieces cancel — and the variation is

$$
\delta\mathcal E_{\mathrm{grad}}=-\frac{\hbar^{2}}{2m}\int\delta\rho_{\mathrm{num}}\,\frac{\Delta r}{r}=\int\delta\rho_{\mathrm{num}}\,Q . \qquad\blacksquare
$$

**Three things follow, and they are the article's reason for existing.**

*The quantum potential is not a potential.* It is the chemical potential of a density-gradient energy: the change in the fluid's energy when a particle is added at fixed volume. A potential in the usual sense is a function of position given from outside; this one is a functional of the density and disappears when the density is uniform. The distinction is not verbal — a potential can be subtracted by a gauge choice and this cannot, because it is a property of the state.

*The quantum stress is the same object read as a pressure.* The block's identity $\partial_j\sigma^{Q}_{ij}=-\rho_{\mathrm{num}}\partial_iQ$ is, in this language, the statement that a gradient energy has a stress and that the force is its divergence. The action makes the identity a definition: $\mathcal E_{\mathrm{grad}}$ is a functional of $\rho_{\mathrm{num}}$ and its gradients, so it has a functional derivative $Q$ and a stress tensor $\sigma^{Q}_{ij}$, and the two are related because the energy is a scalar. The block computes the identity directly from the wave equation; here it is the Euler–Lagrange structure's.

*The fluid is of Korteweg type and not of Euler type.* A Korteweg fluid is one whose stress depends on the gradients of the density, and that is exactly what the third term supplies. The literature on quantum hydrodynamics says this, and the action says why: the gradient energy is the only term the algebra permits at that order.

**The sign is the sign of a pressure.** $Q$ is positive at the centre of a localised packet and falls as the density falls, so $\nabla Q$ points inward there and the force $-\nabla Q$ points outward. The packet spreads. Nothing in the action chooses this; it is the sign of the $\hbar^{2}$ term, which is the sign that makes the energy positive.

## The Velocity Is Not Canonical

**No time derivative of the velocity appears, and that is a statement about the chart and not about the fluid.** In the action above the velocity is $\nabla S/m$: a function of the phase and not a field. If it is promoted to an independent field, the action becomes

$$
\mathcal L_{\mathrm{fl}}=\rho_{\mathrm{num}}\Bigl(-\partial_{t'}S-\frac{m\vec v^{2}}{2}-V\Bigr)-\frac{\hbar^{2}}{2m}(\nabla r)^{2}+\vec\lambda\cdot\Bigl(\vec v-\frac{\nabla S}{m}\Bigr),
$$

and the three variations are these. Varying $\vec\lambda$ returns the definition, so the constraint is the chart's and carries no physics. Varying $\vec v$ fixes the multiplier, $\vec\lambda=\rho_{\mathrm{num}}m\vec v$, which is the momentum density and nothing else. Varying $S$ gives continuity with $\vec j=\vec\lambda/m$, which is the same equation as before. **The promotion buys a name and no equation**, and the multiplier is not an independent field: it is determined by the equation that would have defined it.

**What the promotion does buy is the correct statement of the constraint.** At the rungs above, the velocity's place is taken by the rapidity, and its momentum vanishes identically — the relativistic companion computes $\partial\mathcal L/\partial\dot\theta_{\mathrm{rpd}}=0$ on every configuration. Here the same fact is $p_{\vec v}=0$ once the velocity is promoted: it is then a coordinate with no kinetic term, so its conjugate is zero rather than small. **The two statements are the same statement in two charts**, and the fluid chart is the one in which it is visible without algebra; at this rung the density's momentum $p_r=0$ is the same fact in the chart that needs no promotion.

**A rotational fluid needs two more fields and cannot be written with $\vec v$ alone.** If the flow is not a gradient, the velocity must be represented as $\vec v=\nabla\phi_{\mathrm{clb}}+\alpha_{\mathrm{clb}}\nabla\beta_{\mathrm{clb}}$, the Clebsch form, and the action acquires the pair $(\alpha_{\mathrm{clb}},\beta_{\mathrm{clb}})$ and their constraint. [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html) states the representation and the rank it carries. At this rung the vorticity is zero identically, so the pair is absent and the action's two fields suffice; that is the fluid form of the statement that the phase is one function's worth of data.

## What the Fluid Variational Principle Adds and Does Not Add

**Adds.** The two-term structure of the Lagrangian, which names the fluid's two ingredients as the two terms. The identification of the quantum potential as a functional derivative, which turns the block's computed identity into a definition and places the fluid in the Korteweg class. The direct derivation of continuity and the energy equation, with the acceleration law as a gradient and no wave equation in between. The statement that the velocity is not canonical, in the chart where it is a one-line count. And the identification of the reverse map's hypotheses with the action's structure: the flow is irrotational because the velocity is a gradient, inviscid because no time derivative of the velocity appears, and barotropic in the extended sense because the pressure is the gradient energy's and depends on the density and its gradients alone.

**Does not add.** No new equation: the Euler–Lagrange equations are the block's two, and the third is their gradient. No new solution: the flow is the block's flow. No closure of anything, because nothing is open at this rung. No thermodynamics: the action's energy is the mechanical one, and a temperature requires a state and a trace, which is the third category's subject. And no claim that the fluid's variables are more fundamental than the field's: the map between them is a bijection away from the nodes and the action is one functional written two ways.

**The one asymmetry worth stating.** The polar action carries four vanishing momenta; the fluid action carries one. That is not a loss of content, because at this rung three of the polar variables are absent altogether: the boost is the identity and the rotor is the identity, so their momenta have nothing to be the momentum of. The count agrees once the variables are counted.

## The Action Is the Same Functional in Two Charts

**The statement that organizes the eight articles of this layer.** The action is a functional of the field. Written in the field's components it is the element action; written in the polar parameters it is the polar companion's; written in the density, the phase and the velocity it is this article's. The three are one functional, and the maps between the charts are the word and its derivatives.

**The consequence is a statement about the nodal set.** The word is a bijection from the eight parameters onto the $N$-regular elements, and it fails at $r=0$: the phase is undefined there and the chart is singular. The action does not fail — it is a functional of the field, and the field may vanish — but the fluid chart does. So the variational principle in fluid variables is stated on the complement of the nodal set, and [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html) is the article that says what happens on the excluded set. **The exclusion is the price of the chart and not a defect of the action**, and it is the same exclusion the reverse map carries.

**And the direction of the map matters here as it does there.** The forward map from the fluid's data to the field is exact away from the nodes: given $\rho_{\mathrm{num}}$ and $S$, the element is $r e^{i\theta}\varepsilon e_t$ and there is nothing to solve. The reverse map, from an arbitrary barotropic irrotational inviscid flow to a wave, holds only on the image. The action sits on the fluid side and its stationarity conditions are the fluid's equations, so it does not need the reverse map at all; what it inherits is the map's domain. [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html) states the map and its qualification, and [The Direction of the Fluid-Wave Correspondence, Field by Field](the-direction-of-the-fluid-wave-correspondence-field-by-field.html) states which direction is exact in which row. This article adds the observation that the action is the object the two directions share.

## Summary

**The action.** $\mathcal L_{\mathrm{fl}}=-\rho_{\mathrm{num}}(\partial_{t'}S+\frac{(\nabla S)^{2}}{2m}+V)-\frac{\hbar^{2}}{2m}(\nabla r)^{2}$, four terms, no quantum potential and no barotropic pressure.

**The two variations.** The phase gives continuity, $\partial_{t'}\rho_{\mathrm{num}}+\nabla\cdot(\rho_{\mathrm{num}}\vec v)=0$. The amplitude gives $\partial_{t'}S+\frac{(\nabla S)^{2}}{2m}+V+Q=0$, and its gradient is the acceleration law with the quantum force the only force.

**The quantum potential.** $Q=\delta\mathcal E_{\mathrm{grad}}/\delta\rho_{\mathrm{num}}$, a chemical potential of a density-gradient energy; the stress $\sigma^{Q}_{ij}$ is that energy's pressure tensor; the fluid is of Korteweg type.

**The velocity.** Not canonical: no time derivative, so $p_{\vec v}=0$ identically. Promoting it to a field adds a multiplier that is the momentum density and a constraint that is the chart's definition. A rotational fluid needs the Clebsch pair.

**The chart.** One action, three charts — element, polar, fluid — with the word the map between them, and the nodal set the singular set of the third.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon\,e_t$ | The central field, in its word |
| $r$ | Amplitude; $r>0$; the chart's coordinate |
| $\rho_{\mathrm{num}}=r^{2}=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ | Density; here also the conserved and the charge density |
| $S=\hbar\theta_{\mathrm{pha}}$ | Phase; canonically conjugate to the density |
| $\vec v=\nabla S/m$ | Three-velocity; a gradient, not a field |
| $Q=-\hbar^{2}\Delta r/(2mr)$ | Quantum potential; $Q=\delta\mathcal E_{\mathrm{grad}}/\delta\rho_{\mathrm{num}}$ |
| $\mathcal E_{\mathrm{grad}}$ | Gradient energy; $\frac{\hbar^{2}}{2m}\int(\nabla r)^{2}=\frac{\hbar^{2}}{8m}\int\frac{(\nabla\rho_{\mathrm{num}})^{2}}{\rho_{\mathrm{num}}}$ |
| $\sigma^{Q}_{ij}$ | The gradient energy's stress tensor; $\partial_j\sigma^{Q}_{ij}=-\rho_{\mathrm{num}}\partial_iQ$ |
| $V$ | External potential; $V=0$ for the free field |
| $\vec\lambda$ | Multiplier of the promoted constraint; equal to $m\vec j$ |
| $\phi_{\mathrm{clb}},\alpha_{\mathrm{clb}},\beta_{\mathrm{clb}}$ | Clebsch potentials; needed only for a rotational flow |
| $\mathcal L_{\mathrm{fl}}$ | The Lagrangian density in the fluid variables |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1926) 322–326, for the pair of equations this article varies.
- David Bohm, "A suggested interpretation of the quantum theory in terms of hidden variables," *Physical Review* **85** (1952) 166–193, for the quantum potential read as a force, with the caveat that this block takes the action and not the ontology.
- Takehiko Takabayasi, "On the formulation of the Schrödinger theory in terms of the hydrodynamical quantities," *Progress of Theoretical Physics* **8** (1952) 143–164, for the variational formulation of the same fluid and for the velocity treated as an independent variable.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), chapter 3, for the Lagrangian in the fluid variables and the count of its fields.
- Diederik J. Korteweg, "Sur la forme que prennent les équations du mouvement des fluides si l'on tient compte des forces capillaires causées par des variations de densité considérables mais continues," *Archives Néerlandaises des Sciences Exactes et Naturelles* **6** (1901) 1–24, for the class of fluids whose stress depends on the density's gradients — the class this action places the fluid in.
- The companion articles: [The Variational Principle and the Schrödinger Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-schrodinger-equation-in-biquaternionic-polar-variables.html), the same action in the polar chart; [The Schrödinger Fluid](the-schrodinger-fluid.html), the equations this action varies; [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html), where the stress is computed rather than derived from an energy; [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html), for the map whose domain the chart inherits; and the charged companion [The Lagrangian of the Charged Schrödinger Fluid](the-lagrangian-of-the-charged-schrodinger-fluid.html), where the connection enters the same two terms.
