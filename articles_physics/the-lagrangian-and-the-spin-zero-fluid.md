# __The Lagrangian and the Spin-Zero Fluid__

## Introduction

At the rung above, the velocity is on a shell, and the action makes the shell an equation rather than a hypothesis. [The Spin-Zero Fluid](the-spin-zero-fluid.html) derives the flow from a mass shell that it states as a constraint: $\sum_\mu V_{\Phi,\mu}V_{\Phi,\mu}=-c^{2}-2Q_{\mathrm{qnt}}/m$. Here the same relation is the Euler–Lagrange equation of the density, so the fluid's kinematics is a consequence of varying an action and not a condition imposed on it.

Three results.

*First, the action has two terms and both are energies per proper volume.* A dust term, $-\frac{m\rho_{\mathrm{num}}}{2}[\sum_\mu V_\mu V_\mu+c^{2}]$, which is the mass shell multiplied by a density, and a gradient energy, $-\frac{h^{2}}{8\pi^{2}m}\sum_\mu(\partial_\mu \varrho)^{2}$, which is the quantum term. The first term's bracket vanishes on shell, so the action's dust part measures the departure from the shell; the second term does not vanish anywhere.

*Second, the two variations give continuity and the shell, and the acceleration law is the shell's gradient.* Two real fields, $\varrho$ and $S_{\tilde\Xi}$, two equations, and no constraint. That is the count the block's article asserts and this article derives: the third equation is the second's gradient, and it is not independent.

*Third, the gradient energy is indefinite at this rung and positive at the rung below.* Because the operator is the d'Alembertian and not the Laplacian, the energy carried by the density's variation has one sign for the spatial gradients and the opposite sign for the temporal one. The relativistic fluid therefore has no positive-definite energy functional, and that is the action's way of saying what the block says in another place: the density is not positive definite and the fluid has two sheets.

Position in the block. This is the variational companion of [The Spin-Zero Fluid](the-spin-zero-fluid.html) and the third of the eight articles of this layer. It is the first in which the operator is the d'Alembertian, and the first in which the action's density and the current's density are different objects.

## Conventions

The conventions are restated here so that every sign below is checkable from this page alone. $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$, $\rho_{\mathrm{num}}=\varrho^{2}$, $S_{\tilde\Xi}=\frac{h}{2\pi}\theta_{\mathrm{pha}}$, $\tilde P_\Phi=\tilde\nabla_\Phi S_{\tilde\Xi}=i(E/c)e_t+\vec p$, $\tilde V_\Phi=\tilde P_\Phi/m$, $k_m=\frac{2\pi mc}{h}$, $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial{r'_{t}}^{2}$ with $r'_t=ct$. The temporal slot carries the $i$, so $\sum_\mu p_\mu p_\mu=-m^{2}c^{2}$ on the free shell. The pairing is $\mathrm{Sc}(\cdot^{*}\cdot)$ and the conjugations are $*$ and $^{\natural}$. The action is a functional over four-dimensional space with $\mathrm{d}^4\varrho=\mathrm{d}r'_t\,\mathrm{d}^3\varrho$.

## The Action in the Fluid Variables

The polar action is quadratic in the bracket, and in the scalar case the bracket is the phase's and the amplitude's derivatives. With $\mathcal A_\mu=\tilde\Xi^{-1}\partial_\mu\tilde\Xi=\partial_\mu\ln \varrho+i\partial_\mu\theta_{\mathrm{pha}}$,

$$
\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde\Xi\,\sum_\mu\varepsilon_\mu\mathcal A_\mu\mathcal A_\mu^{*}\bigr)=\rho_{\mathrm{fr}}\bigl[(\partial_\mu\ln \varrho)^{2}+(\partial_\mu\theta_{\mathrm{pha}})^{2}\bigr],
$$

with $\rho_{\mathrm{fr}}=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)=\varrho^{2}\cosh\theta_{\mathrm{rpd}}=\varrho^{2}$ the scalar part of the frame density, the frame's rapidity being trivial at this rung, so the frame density and $\rho_{\mathrm{num}}$ are the same number. The two squares are separate because the bracket's real and imaginary parts are of different types and do not mix under the scalar part. Substituting $\rho_{\mathrm{fr}}=\rho_{\mathrm{num}}$ and multiplying by $\frac{h^{2}}{4\pi^{2}}/2m$ to put the terms in the fluid's units,

$$
\boxed{\;\mathcal L_{\mathrm{fl}}=-\frac{m\rho_{\mathrm{num}}}{2}\Bigl[\sum_\mu V_{\Phi,\mu}V_{\Phi,\mu}+c^{2}\Bigr]-\frac{h^{2}}{8\pi^{2}m}\sum_\mu(\partial_\mu \varrho)^{2}\;}
$$

with $V_{\Phi,\mu}=\partial_\mu S_{\tilde\Xi}/m=\partial_\mu\theta_{\mathrm{pha}}/k_m$.

The dust term's bracket is the shell's left-hand side. That is not a coincidence of notation: the bracket is $\sum_\mu V_\mu V_\mu+c^{2}$, which the block's article sets equal to $-2Q_{\mathrm{qnt}}/m$, so the first term is $-\frac{m\rho_{\mathrm{num}}}{2}\cdot(-2Q_{\mathrm{qnt}}/m)=\rho_{\mathrm{num}}Q_{\mathrm{qnt}}$ on shell. **The dust term is not zero on shell and the action is not a constraint generator in disguise**: what vanishes on the free shell is the bracket at $Q_{\mathrm{qnt}}=0$, and the quantum potential is exactly what the bracket measures.

The two terms are energies per proper volume, and the current is not. $\rho_{\mathrm{num}}$ is the proper density and the action is written against proper volume; the current's temporal component is $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$, the charge density, and it is measured against lab volume. The factor $\gamma$ between them is a Jacobian and not a dynamical statement, and it is why the block's notation table carries two densities with one action. At the rung below there is one density because there is no norm for a $\gamma$.

There is no term in $\rho_{\mathrm{num}}$ alone apart from the mass term, and that is why the fluid has no equation of state. A barotropic fluid's pressure is the derivative of an energy with respect to the density at fixed entropy; here the only such derivative is $mc^{2}$, a constant per particle, so the bulk pressure vanishes identically. What survives is the gradient energy's pressure, which is the block's $\sigma^{Q}_{ij}$. The absence of an equation of state is visible in the action as the absence of a term, and the block's denial of one is the same statement made about the equations.

## The Variation: Two of Them

Varying the phase gives continuity of the current. $\mathcal L_{\mathrm{fl}}$ depends on $S_{\tilde\Xi}$ only through $\sum_\mu V_\mu V_\mu$, so

$$
\partial_\mu\frac{\partial\mathcal L_{\mathrm{fl}}}{\partial(\partial_\mu S_{\tilde\Xi})}=0
\qquad\Longrightarrow\qquad
\partial_\mu\bigl(\rho_{\mathrm{num}}V_{\Phi,\mu}\bigr)=0,
$$

which is $\partial_\mu J_{\Phi,\mu}=0$ with $\tilde J_\Phi=\rho_{\mathrm{num}}\tilde V_\Phi$. The current is the Noether current of the phase shift and the continuity equation is its conservation, and the shift is global: nothing here is a gauge redundancy, so the current is a charge.

Varying the amplitude gives the mass shell, and the shell contains the quantum potential through the d'Alembertian. The gradient term varies as

$$
\delta\int-\frac{h^{2}}{8\pi^{2}m}\sum_\mu(\partial_\mu \varrho)^{2}=+\frac{h^{2}}{(2\pi)^{2} m}\int\Box_\Phi \varrho\,\delta \varrho,
$$

and $\delta \varrho=\delta\rho_{\mathrm{num}}/(2\varrho)$, so the contribution per unit $\delta\rho_{\mathrm{num}}$ is $\frac{h^{2}\Box_\Phi \varrho}{8\pi^{2}m\varrho}=-Q_{\mathrm{qnt}}$. The dust term contributes $-\frac{m}{2}[\sum_\mu V_\mu V_\mu+c^{2}]$. Hence

$$
\sum_\mu V_{\Phi,\mu}V_{\Phi,\mu}=-c^{2}-\frac{2Q_{\mathrm{qnt}}}{m},
$$

which is the block's display, arrived at as an equation of motion.

The acceleration law is the gradient of the shell and is not a third equation. Differentiating the display in space, with $\partial_jp_k=\partial_kp_j$ and $\partial_jE=-\partial_tp_j$, gives

$$
\frac{\mathrm{d}\vec p}{\mathrm{d}t}=-\frac{1}{\gamma}\vec\nabla_\Phi Q_{\mathrm{qnt}},
\qquad
\frac{\mathrm{d}}{\mathrm{d}t}=\partial_t+\vec v\cdot\nabla,
$$

which is the block's boxed law. The action's contribution to this display is not the algebra but the status: the shell is what the variation produced, so the force law is the gradient of an equation of motion and not of a constraint. In the polar chart the rapidity is a coordinate and the shell appears as a relation among momenta; here the density is a coordinate and the shell is what its variation says.

The count is therefore two and two, with nothing left over. No multiplier, no subsidiary condition, no constraint surface to reduce. The rung below has the same count and reaches it differently; the rung above loses it.

### The Second Variation: The Gradient Energy Is Indefinite

The sign of the second term is not uniform, and the reason is the operator's. With the corpus's conventions the temporal component of a four-gradient carries an $i$, so

$$
\sum_\mu(\partial_\mu \varrho)^{2}=\sum_j(\partial_jr)^{2}-\bigl(\partial_{r'_t}\varrho\bigr)^{2},
$$

and the quadratic form is a difference and not a sum. The gradient energy is therefore bounded neither above nor below, and the fluid has no positive-definite energy functional.

Three consequences, and the block states each of them in another language.

*The quantum potential changes sign.* $Q_{\mathrm{qnt}}=-\frac{h^{2}}{4\pi^{2}}\Box_\Phi \varrho/(2m\varrho)$ with an indefinite $\Box_\Phi$, so a density that varies in time contributes with the opposite sign to one that varies in space. The non-relativistic quantum potential is $\Delta_\Phi$'s and is negative at a maximum of $\varrho$; this one is not sign-definite at all.

*The action cannot see the sign $\varepsilon$.* The block's charged article names the density's indefinite sign as the free article's defect which the coupling moves and does not repair. In the action it is one line: $\varepsilon$ is central and $\varepsilon^{2}=1$, so it cancels in $\tilde\Xi^{*}\tilde\Xi$ and in $\mathcal A_\mu$, and the two branches $\varepsilon=\pm1$ give the same Lagrangian. The action is blind to the branch and the charge density's sign is what blindness costs.

*The functional has no ground state, and that is not a defect of the fluid reading.* A field theory with an indefinite quadratic form has no lowest configuration, which is why the relativistic object of this block is a field and not a fluid with a rest state. The action says this before any quantization, and the second category's Fock space is where the two signs become particles and antiparticles.

At the rung below the form is definite and the difference is the whole of the difference between the two rungs. The Schrödinger fluid's gradient energy is $\frac{h^{2}}{8\pi^{2}m}\int(\vec\nabla_\Phi \varrho)^{2}$, a sum of squares, and its quantum potential is a Laplacian's. One operator, one sign, one sheet.

## The Constraints the Action Imposes: There Is No Subsidiary Condition

Two fields, two equations, and nothing left over. The phase's variation gives continuity, the amplitude's gives the energy relation, and the acceleration law is the gradient of the second rather than a third equation. No multiplier appears, no subsidiary condition is imposed, and no constraint surface restricts the variation.

The velocity's definition is the relation that is mistaken for one. It is a function of the phase's gradient and the potential, so it is fixed by the fields rather than constrained alongside them. A definition carried into the action is not a condition the action imposes, and the count of this layer depends on keeping the two apart.

**The mass term adds a determination and not a constraint.** It fixes the amplitude through the energy relation and leaves the phase's rate free, so the count of two and two survives the coupling. A quadratic mass in a chart with no independent direction field has nowhere to put a constraint.

What the section does not claim. It does not claim the fluid equals the element form in its canonical structure: the equivalence is the chart's, and the chart's velocity is what makes the counts agree. It claims that this action, in these variables, imposes nothing beyond its own two equations.

## The Structural Consequence: Two Fields, Two Equations, and the Third as a Gradient

**The article's claim is a count, and the count is exact.** Two real fields, $\varrho$ and $S_{\tilde\Xi}$, give two Euler–Lagrange equations: continuity, from the phase, and the mass shell, from the density. There is no constraint, because no momentum vanishes: both fields are canonical. The acceleration law that the block's article states as a separate equation is not a third equation here — it is the gradient of the shell.

The hand check. The shell is $\sum_\mu V_\mu V_\mu=-c^{2}-2Q_{\mathrm{qnt}}/m$ with $V_\mu=\partial_\mu S/m$. Differentiating it with respect to the spatial coordinates and using $\partial_{r'_t}V_\mu=\partial_\mu V_{r'_t}$ gives

$$
\frac{\partial\vec V}{\partial r'_t}+(\vec V\cdot\vec\nabla_\Phi)\vec V=-\vec\nabla_\Phi\Bigl(\frac{Q_{\mathrm{qnt}}}{m}\Bigr),
$$

which is the acceleration law with the quantum potential as its only force beyond inertia. One differentiation, no new postulate, and the third equation is the second's gradient.

Why the count matters. A Lagrangian with two fields and two equations is not over-determined, and a fluid whose acceleration is a consequence of its shell is a fluid with no independent pressure. Both statements are what the family needs in order to say that the scalar fluid at this rung is dust plus a quantum stress.

## The Noether Currents: The Stress as the Translation Current

The action is invariant under translations, so it has a stress, and the stress is the block's up to an improvement. The canonical tensor is

$$
T_{\mu\nu}=\bigl(\partial_\nu S_{\tilde\Xi}\bigr)\frac{\partial\mathcal L_{\mathrm{fl}}}{\partial(\partial_\mu S_{\tilde\Xi})}+\bigl(\partial_\nu \varrho\bigr)\frac{\partial\mathcal L_{\mathrm{fl}}}{\partial(\partial_\mu \varrho)}-\eta_{\mu\nu}\mathcal L_{\mathrm{fl}},
$$

and it splits into the two terms the action has. The first is the dust's: $\partial\mathcal L_{\mathrm{fl}}/\partial(\partial_\mu S_{\tilde\Xi})=-\rho_{\mathrm{num}}V_{\Phi,\mu}$, so that term is $-m\rho_{\mathrm{num}}V_{\Phi,\mu}V_{\Phi,\nu}$, the stress of a pressureless flow, whose time–time component is $\gamma^{2}\rho_{\mathrm{num}}mc^{2}$ because the density and the energy are both boosted. The second is the gradient energy's, and it is the block's $\sigma^{Q}_{ij}$ extended to four dimensions. Two cautions about the sum. It is the canonical tensor, and the block's $w_{\mathrm{fl}}$ is the improved one: the two differ by an improvement term, so the comparison below is of structure and not of normalisation. And it is not the fluid's stress in the sense of a one-particle distribution, because the dust term is quadratic in the velocity where a fluid's action is linear in a density.

What the action adds here is the reason the block's identity holds. [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html) proves $\partial_j\sigma^{Q}_{j\eta}=-\rho_{\mathrm{num}}\partial_\eta Q_{\mathrm{qnt}}$ by a direct computation on the wave equation, and it records the caveat that the identity needs an amplitude stationary in the material time. Here the same identity is the translation invariance's conservation law together with the shell, and the caveat is visible: the four-dimensional stress is the divergence-free object, and the three-by-three block is a projection of it whose divergence carries the temporal derivative only when that derivative vanishes. **The action does not repair the caveat; it explains where it comes from.**

And it explains the asymmetry between the two rungs. At the first-order rung the stress has no flux and no energy density separate from the block, because the action has one time derivative; there is nothing to project away and the identity is unconditional. Here there is a full four-dimensional stress and the projection costs.

## What the Principle Adds and What It Relabels: In the Fluid Chart

Adds. The mass shell as an equation of motion rather than a constraint, and with it the correct status of the acceleration law. The absence of an equation of state as the absence of a term. The identification of $\rho_{\mathrm{num}}$ and $\rho_{\mathrm{chg}}$ as one action's density and one current's component, with $\gamma$ as the Jacobian. The indefiniteness of the gradient energy, which is the action's version of the rung's missing positivity, and its blindness to $\varepsilon$, which is the action's version of the two branches. And the stress as a translation current, with the block's identity read as its conservation and the static caveat explained rather than removed.

Does not add. No new equation: continuity and the shell are the block's pair, and the boxed law is their gradient. No new solution. No closure, because nothing is open at this rung. No thermodynamics: the action's energy is mechanical and indefinite, and a thermal state is a different object in a different category. No claim that the fluid's variables are more fundamental than the field's: the map is a bijection away from the nodes, and the action is one functional in two charts.

The one comparison worth making with the polar companion. That article finds the polar action to be quadratic in the bracket with a metric that depends on the point, and it computes the metric for the four scalar parameters with both axes held fixed. The fluid chart replaces the rapidity by the velocity, so the metric's dependence on the point becomes the shell's dependence on $Q_{\mathrm{qnt}}$: **the point-dependent metric and the quantum potential are one object read in two charts**, and the fluid chart is the one in which it appears as an energy rather than as a metric.

## What the Principle Adds and What It Relabels: The Fluid Alone

The full element is a fluid with a frame that is not a spin. The biquaternion scalar field's polar word carries the boost and the rotor as well as the scale and the phase, so its fluid has a local frame in which the rapidity is an anisotropy and the rotor is a rotation of the frame about itself. The element reading calls these parameters; the fluid reading calls the frame a state of the medium, and the second naming is what lets a reader ask what the medium's anisotropy does to the pressure.

What it adds: the two-sided pressure. The stress has a longitudinal and a transverse component, and they differ because the frame distinguishes a preferred direction at each point. The element reading has the same two components in its stress, but nothing there says which is the direction of propagation; the fluid reading does, and the anisotropy of the pressure is the article's contribution.

What it adds: the second-order formulation as a fluid statement. The field equation is second order in the element, and in the fluid reading that order is the statement that the medium carries a stress and not only a flow. A first-order fluid carries a momentum density; a second-order fluid carries a stress, and the article's section on the two orders is where the distinction is made.

What it does not add. No new equation and no new solution. Every equation in this article is the element article's, and the article says so in its first paragraph so that no reader looks for a new prediction.

What it inherits. The uncharged character, the gauge invariance of the scale, and the nodal exception. **The rotor is not a charge**, and the article's comparison with the charged Schrödinger fluid is a single sentence making that point.

One thing it inherits worse. The frame's meaning is clearer here than in the element reading, but its *determination* is not: the frame is reconstructed from the element and not fixed by a potential, so the fluid reading has less to say about it than the coupled fluids do.

## Open Questions

The two sheets and the action's domain. $\varepsilon$ does not appear in the action, so the two branches $\varepsilon=\pm1$ are one functional's two images and the action selects neither. Whether they are two sectors of one functional or two functionals that agree on the boundary is not settled, and it is the same question the block's article poses about the density's sign.

The nodal set in four dimensions. The chart fails at $\varrho=0$, and at this rung the failure is on a timelike surface as well as a spacelike one. Whether the action needs a condition there, and whether the circulation's quantisation supplies it, is open; [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html) describes the surface and the integral.

## Summary

The action. $\mathcal L_{\mathrm{fl}}=-\frac{m\rho_{\mathrm{num}}}{2}[\sum_\mu V_{\Phi,\mu}V_{\Phi,\mu}+c^{2}]-\frac{h^{2}}{8\pi^{2}m}\sum_\mu(\partial_\mu \varrho)^{2}$, a dust term and a gradient energy, both per proper volume.

The variations. The phase gives $\partial_\mu(\rho_{\mathrm{num}}V_{\Phi,\mu})=0$; the amplitude gives $\sum_\mu V_\mu V_\mu=-c^{2}-2Q_{\mathrm{qnt}}/m$; the gradient of the second is $\mathrm{d}\vec p/\mathrm{d}t=-\gamma^{-1}\vec\nabla_\Phi Q_{\mathrm{qnt}}$.

The shell. An equation of motion and not a hypothesis; two fields, two equations, no constraint.

The energy. Indefinite, because $\sum_\mu(\partial_\mu \varrho)^{2}$ is a difference; hence no ground state; and $\varepsilon$ absent from every term, so the two branches are one functional — the action's version of what the block states about the density and what the second category states about the vacuum.

The stress. The translation current, dust plus gradient; the block's three-by-three identity is its conservation projected, and the static caveat is the projection's.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$ | The word; the scalar case, two parameters |
| $\rho_{\mathrm{num}}=\varrho^{2}$ | Proper density; the action's density |
| $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ | Charge density; the current's temporal component |
| $S_{\tilde\Xi}=\frac{h}{2\pi}\theta_{\mathrm{pha}}$ | Phase; the current's potential |
| $\tilde P_\Phi=\tilde\nabla_\Phi S_{\tilde\Xi}$ | Four-momentum; $\tilde P_\Phi=i(E/c)e_t+\vec p$ |
| $\tilde V_\Phi=\tilde P_\Phi/m$ | Four-velocity; on shell $\sum_\mu V_\mu V_\mu=-c^{2}-2Q_{\mathrm{qnt}}/m$ |
| $Q_{\mathrm{qnt}}=-\frac{h^{2}}{4\pi^{2}}\Box_\Phi \varrho/(2m\varrho)$ | Quantum potential; indefinite |
| $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial{r'_{t}}^{2}$ | Central d'Alembertian; $r'_t=ct$ |
| $\mathcal E_{\mathrm{grad}}=-\frac{h^{2}}{8\pi^{2}m}\int\sum_\mu(\partial_\mu \varrho)^{2}$ | Gradient energy; indefinite |
| $T_{\mu\nu}$ | Canonical stress; $T_{00}=\rho_{\mathrm{chg}}mc^{2}$ on shell |
| $\gamma=E/(mc^{2})$ | Signed Lorentz factor; the Jacobian between the two densities |
| $k_m=\frac{2\pi mc}{h}$ | Mass wave number |
| $\varepsilon=\pm1$ | The branch; the action does not select it |
| $\mathcal L_{\mathrm{fl}}$ | The Lagrangian density in the fluid variables |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1926) 322–326, for the non-relativistic pair whose relativistic form this article varies.
- Louis de Broglie, *La mécanique ondulatoire du photon et la théorie quantique des champs* (Gauthier-Villars, 1949), for the relativistic fluid reading and the density's indefinite sign.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 2–35, part I, for the relativistic scalar fluid and its stress.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), chapter 12, for the relativistic fluid's velocity normalisation and the role of the quantum potential in it.
- Clifford Truesdell and Richard Toupin, "The classical field theories," in *Handbuch der Physik* III/1 (Springer, 1960), for the canonical stress and the boundary between a dust's and a Korteweg fluid's terms.
- The companion articles: [The Lagrangian and the Klein–Gordon Equation in Polar Variables](the-lagrangian-and-the-klein-gordon-equation-in-polar-variables.html), the same action in the polar chart with its point-dependent metric; [The Spin-Zero Fluid](the-spin-zero-fluid.html), the equations varied here; [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html), where the stress and its caveat are computed; [The Lagrangian and the Schrödinger Fluid](the-lagrangian-and-the-schrodinger-fluid.html), the rung below, where the gradient energy is definite; and [The Lagrangian and the Charged Spin-Zero Fluid](the-lagrangian-and-the-charged-spin-zero-fluid.html), where a connection meets the shell.
