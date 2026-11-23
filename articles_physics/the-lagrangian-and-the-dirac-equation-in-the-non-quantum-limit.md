# __The Lagrangian and the Dirac Equation in the Non-Quantum Limit__

## Introduction
The parent's Dirac action is already first order in every velocity, so there is no kinetic term to delete: the non-quantum limit in this family is the statement that the three vanishing momenta are the order-zero constraints and that the flow they generate is order one.

The parent's action, and the fact that decides the whole article.

$$
S=\int\mathrm{d}t'\;\frac{h}{2\pi} c\,\Bigl\{\varrho^{2}\Bigl(\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\;\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}\Bigr)-\varrho^{2}k_m\,\mathcal{V}\Bigr\},
$$

with $\mathcal{V}$ a function of the boost, of the rotor and of the fixed direction, and with no dependence on $\varrho$ or on $\theta_{\mathrm{pha}}$. **The scale enters as $\varrho^{2}$ in both terms and never with its own derivative.** There is no $(\partial \varrho)^{2}$ here.

In the Klein–Gordon and Proca families the limit is the deletion of one term — the scale's kinetic term — and the deletion changes one Euler–Lagrange equation and leaves the other. **In this family no such term exists**, so the limit cannot be a deletion, and the variational statement of it must be something else. What it is: the action's constraint structure.

Every velocity enters linearly, so $\mathcal{L}=A_x(q)\dot q^{x}-U(q)$ with the eight coordinates $q=(\varrho,\theta_{\mathrm{pha}},\theta_{\mathrm{rpd}},\text{two angles of }\vec u_{\mathrm b},\text{three of }\tilde u_{\mathrm r})$. The eight momenta are the components of $A$, so three of them vanish identically and the Hessian vanishes identically: no velocity is recoverable from a momentum. The Euler–Lagrange equations are $\Omega_{xy}\dot q^{y}=\partial_x U$ with $\Omega=\mathrm{d}A$, a closed and degenerate two-form.

The vanishing momenta are the primary constraints, and their equations are the algebraic conditions — the mass shell and the polarisation of the frame. The flow $\Omega\dot q=\mathrm{d}U$ is first order in the coordinates and it transports the density, the velocity and the spin. The limit is therefore the split of one first-order system into constraints and flow, and the parameter $\epsilon$ is what separates them.

What the article does not claim. It does not claim that the action truncates, because it does not; and it does not claim that a quantum potential emerges from the action, because there is none to emerge: **the Dirac equation is first order, so the amplitude's curvature is not a term of this theory.** A variational treatment that promised a discarded term would be describing a different family.

The parent's action is a one-form plus a potential, with three vanishing momenta and a degenerate closed two-form. The limit reads the vanishing momenta as the order-zero constraints and the flow as the order-one transport, and the two together are the equation-route companion's algebraic frame plus its three transport laws. The mass term's fixed direction is not an extra assumption but a requirement: without it the mass bilinear vanishes on the chirality parts, and the direction that makes it non-zero is the frame's own third direction. The action contains no amplitude-curvature term, so the family has no quantum potential of the Klein–Gordon type, and the corpus's statements about one in this family are statements about the iterated equation. No multiplier is introduced by hand anywhere: the degenerate momenta are what a first-order Lagrangian gives, which is the parent's answer to the objection that constraint multipliers look ad hoc.

The first-order Lagrangian form of the Dirac equation, its primary constraints, and the fact that a mass bilinear needs a direction on the chirality parts are standard. Added here: the identification of the vanishing momenta with the order-zero conditions, the statement that the family has no deletion because it has no second derivative of the scale, and the reading of the mass term's fixed direction as the polarisation the limit inherits.

The word exists where $N(\tilde\Xi)\neq0$, and the action is written for the central class's complement — the eight parameters with the frame. The limit is defined on that domain.
## Conventions
The conventions are restated here so that every sign below is checkable from this page alone. Those of the variational polar parent: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_{t}=1$ and $\vec e_\mu^{2}=-e_{t}$; $\mathrm{Sc}$ the coefficient of $e_{t}$; the complete polar decomposition $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$; $S=\frac{h}{2\pi}\theta_{\mathrm{pha}}$; $k_m=\frac{2\pi mc}{h}$; $\vec\omega_{\mathrm r}$ the rotor's body angular velocity; $\hat n_{\mathrm{rot}}$ its axis; $\mathcal V$ the mass function of the frame; $\epsilon=1/(k_{\Phi}L)$.
## The Action in the Non-Quantum Limit: The One-Form

$$
S=\int\mathrm{d}t'\;\Bigl\{\frac{h}{2\pi} c\,\varrho^{2}\Bigl[\cosh\theta_{\mathrm{rpd}}\,\mathrm{d}\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\;\hat n_{\mathrm{rot}}\cdot\bigl(\tilde u_{\mathrm r}^{-1}\mathrm{d}\tilde u_{\mathrm r}\bigr)\Bigr]-U\Bigr\},
\qquad
U=\frac{h}{2\pi} c\,k_m\,\varrho^{2}\,\mathcal{V}.
$$

The bracket is a one-form and it is the phase's momentum plus the spin's. Its first term is the phase rate weighted by $\cosh\theta_{\mathrm{rpd}}=\gamma$; its second is the rotor's body angular velocity weighted by $\sinh\theta_{\mathrm{rpd}}=\gamma\beta$. The two weights are the boost's two hyperbolic functions, so the one-form is the four-velocity contracted with the two rates.

The element action carries $\frac{h}{2\pi} c/2$ and the display carries $\frac{h}{2\pi} c$; the factor cancels from every Euler–Lagrange equation and is chosen so that the phase momentum comes out $\frac{h}{2\pi} c\rho_{\mathrm{num}}\gamma$, the temporal component of the current.

$p_x=A_x(q)$, so

$$
p_{\theta_{\mathrm{pha}}}=\frac{h}{2\pi} c\,\varrho^{2}\cosh\theta_{\mathrm{rpd}},
\qquad
p_{\tilde u_{\mathrm r}}=-\frac{h}{2\pi} c\,\varrho^{2}\sinh\theta_{\mathrm{rpd}}\,\hat n_{\mathrm{rot}},
\qquad
p_{\varrho}=p_{\theta_{\mathrm{rpd}}}=p_{\vec u_{\mathrm b}}=0 .
$$

Three momenta vanish and the Hessian vanishes for all eight. The first statement is the constraint content; the second is why the equations are first order in the coordinates and not in their rates.

$\Omega_{xy}\dot q^{y}=\partial_x U$ with $\Omega=\mathrm{d}A$ closed because $\mathrm{d}^{2}=0$ and degenerate for the same reason the Hessian is. Eight first-order equations, and the parent prints three of them at once.

The parent pairs with $\mathrm{Sc}(\cdot^{*}\cdot)$, and the two chiral densities carry $\tilde\nabla_\Phi$ and $(\tilde\nabla_\Phi)^{\natural}$ so that their sum is real. The limit's action keeps the density and the phase gradients and drops the block that carries the spin's second derivatives. Each kept term is real, and the deletion removes real terms, so the pair is untouched.

$k_m$ is real; the momentum-space counterpart of the same statement is that the symbol is Hermitian. The limit does not change the symbol's type, only the terms in which it appears.

The selection rule. Declared. No free potential; the action's coefficients are the mass and the metric's weights, and neither admits an inadmissible sector.

What reality does not buy. The truncated action is real and incomplete. Its densities are real exactly as the full action's are; what the truncation costs is accuracy and not reality, and the order of the cost is stated in *The Limits and the Truncation’s Error*.

### The Limits and the Truncation’s Error

**There is no truncation error because there is no truncation.** The limit removed nothing, so the difference between the parent action and the limit's action is zero, and the difference between the parent's equations and the limit's is zero as well. The error of this family's non-quantum limit is identically zero, and the article says so in one sentence rather than in a section — except that the sentence needs a section, because a zero error is easy to misread as a strong result.

A zero error means the limit is exact, and an exact limit carries no information about the small parameter. The Dirac family's limit cannot be used to justify dropping anything, because nothing was dropped; every later approximation — the envelope, the slowly varying frame, the neglect of the back-reaction — is a different approximation with its own error, and the article's other sections are where those are priced.

In the scalar family the limit's error is the quantum potential, and a reader who comes to the Dirac family expecting the same will look for a term that is absent from the parent. The polar word has no scale-kinetic block, so there is nothing to delete and nothing to restore, and the article's coordinates section is where that is shown.

The exactness is bought by the limit being vacuous as an approximation. The article's claim is not that the Dirac family's non-quantum limit is better than the others; it is that the limit is a different kind of object, a reading of an exact structure rather than a truncation of an approximate one.

A limit that approximates nothing and deletes nothing cannot be used to argue that the theory is "almost classical" at large scales. The Dirac family's classical appearance is a property of its order count from the start, and the limit merely names it.

Nothing is deleted, so the limit is an assignment. The two statements it makes are:

| object | what it is | order |
|---|---|---|
| the vanishing momenta | three algebraic conditions on the eight coordinates | $0$ |
| the flow $\Omega\dot q=\mathrm{d}U$ | eight first-order transport equations | $1$ |
| products of two flow equations | quadratic in the connections | $2$ |

$p_r=0$ is the statement that the scale is not a dynamical variable, and its equation is the mass shell once $\mathcal V$ is evaluated on the constraint surface; $p_{\theta_{\mathrm{rpd}}}=0$ and $p_{\vec u_{\mathrm b}}=0$ are the conditions that fix the boost's rapidity and axis, that is the polarisation of the frame by the momentum. The algebraic frame of the companion article is the vanishing of three momenta.

The flow is first order and it carries the density, the velocity and the spin, because the eight coordinates are the density, the phase, the rapidity, the boost's axis and the rotor's three angles. Three transport laws and one phase rate, which is what the companion's order one is.

The products of two flow equations are what the iteration produces, and they are the amplitude's curvature combined with the frame's. **A variational principle on a first-order action cannot produce a second-derivative term**, and that is the structural reason this family has no quantum potential of the Klein–Gordon type.

## The Variation: The Momenta and the Flow
The action is $\int\mathrm{d}t'\,\bigl\{A_x(q)\dot q^{x}-U(q)\bigr\}$ with $A$ the one-form of the previous section. Varying it gives

$$
\delta S=\int\mathrm{d}t'\;\Bigl[\bigl(A_x\dot q^{x}-U\bigr)_{,y}\delta q^{y}-\frac{\mathrm{d}}{\mathrm{d}t'}\bigl(A_y\delta q^{y}\bigr)\Bigr],
$$

and the second term is a total derivative, so it contributes a boundary term at the endpoints and nothing else. Setting the first bracket to zero and using $\Omega=\mathrm{d}A$ gives

$$
p_y=A_y(q),
\qquad
\Omega_{yx}\dot q^{x}=\partial_y U ,
$$

which are the momenta and the eight first-order equations of the previous section. The two displays of the parent's are read here as one variation, and the reading is exact.

The action is linear in every rate, so $\partial^{2}S/\partial\dot q^{x}\partial\dot q^{y}=0$ identically and the Legendre transform is not invertible. That is the same fact as the vanishing of the three momenta, and it is the reason the equation is first order rather than second.

The mass term is inside $U$, so its variation contributes to $\partial_yU$ and to nothing else: the mass fixes the direction and does not enter the one-form. That is the content of the following section, and the variation is what makes the separation visible.

## The Constraints the Action Imposes: One Constraint, Because One Rate Is Missing

The one-form $\frac{h}{2\pi} c\,\varrho^{2}\bigl[\cosh\theta_{\mathrm{rpd}}\,\mathrm{d}\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\,\hat n_{\mathrm{rot}}\cdot(\tilde u_{\mathrm r}^{-1}\mathrm{d}\tilde u_{\mathrm r})\bigr]$ is linear in the rates, and the eighth parameter appears only through $U$, which carries none. Its conjugate momentum therefore vanishes identically on the whole of the chart's phase space.

A momentum that vanishes everywhere is a primary constraint, and it is the whole constraint content here. The truncation creates it rather than inheriting it: the parent's first-order action carries rates for all eight and its constraints are the pair the first-order form imposes, and deleting the frame's gradient terms removes a velocity. **A removed velocity is a constraint**, not a lost equation.

The mass term breaks the local invariance of the field it multiplies, so the constraint does not generate a transformation; it pairs with the gauge direction the chart inherits, and the count of degrees falls by one pair.

What the section does not claim. It does not build the Dirac bracket and it does not assert a Gauss law: the connection is fixed in this limit, so no constraint arrives from its equation, and the variation section states the same fact from the other side.

## The Structural Consequence: The Mass Term and the Fixed Direction
With $\tilde\Xi_L=\tilde\Xi\Pi_+$ and $\tilde\Xi_R=\tilde\Xi\Pi_-$,

$$
\mathrm{Sc}\bigl[\tilde\Xi_L^{*}\tilde\Xi_R\bigr]=\mathrm{Sc}\bigl[\Pi_+\tilde\Xi^{*}\tilde\Xi\Pi_-\bigr]=\mathrm{Sc}\bigl[\Pi_-\Pi_+\tilde\Xi^{*}\tilde\Xi\bigr]=0 ,
$$

using $\Pi_+^{*}=\Pi_+$, the cyclicity of $\mathrm{Sc}$, and $\Pi_-\Pi_+=0$. No assumption enters, so the vanishing needs no sample.

Right multiplication by $i\vec v$ with $\vec v$ a fixed unit spatial direction reverses the value, since $\vec v\vec e_z=-\vec e_z\vec v$ for $\vec v\perp\vec e_z$. So $\mathrm{Sc}[\tilde\Xi_L^{*}\tilde\Xi_R\,i\vec v]\neq0$ for $\vec v\perp\vec e_z$ and zero for $\vec v\parallel\vec e_z$: **only the directions that reverse the value give a mass, and they are the ones transverse to the frame's third direction.**

The direction is the spin axis's own frame direction, so the mass term and the spin's axis are one object in this action. The polarisation the companion's order zero fixes is not an extra assumption: it is what the mass term requires, and the limit inherits it unchanged.

The parent says that reading the pair's letters as values gives no non-zero solution, and that the value-consistent display carries the direction $i\vec v$. The action says the same from the other side: a mass term that couples the two chirality parts vanishes identically unless the direction is there. Two statements, one fact.
## The Noether Currents: The Density, the Spin and the Energy
The phase rotation is a symmetry, and its conserved quantity is the momentum that the one-form carries, $p_{\theta_{\mathrm{pha}}}=\frac{h}{2\pi} c\,\varrho^{2}\cosh\theta_{\mathrm{rpd}}$. Division by $\frac{h}{2\pi} c$ gives the density $\rho_{\mathrm{num}}$, positive, and the current is $\rho_{\mathrm{num}}$ times the transport velocity.

The rotor's momentum is $-\frac{h}{2\pi} c\,\varrho^{2}\sinh\theta_{\mathrm{rpd}}\,\hat n_{\mathrm{rot}}$, a vector along the boost axis weighted by the rapidity. Its conservation is the statement that the spin direction is transported without precession in the free theory, and the mass term is what couples the spin direction to the momentum, so the free conservation is exact and the coupled one is not.

The Legendre transform of a first-order action is $E=U$, because $p\dot q=A\dot q$ cancels the kinetic term. So the energy of a configuration is the mass term evaluated on it, $U=\frac{h}{2\pi} c\,k_m\varrho^{2}\mathcal V$, and the equation of motion is the statement that the flow is tangent to the level surfaces of $U$ in the symplectic form $\Omega$. The energy carries the mass and the density does not, which is the limit's version of the split the element article makes.
## What the Principle Adds and What It Relabels: By the Variational Route

*The order-zero conditions are momenta and not assumptions.* The mass shell and the polarisation are the vanishing of $p_r$, $p_{\theta_{\mathrm{rpd}}}$ and $p_{\vec u_{\mathrm b}}$. A reader who wants to know why the frame is algebraic at leading order finds the answer in the Lagrangian's linearity, not in an argument about the field's slow variation.

*No multiplier is introduced by hand.* A first-order Lagrangian's degenerate momenta *are* the constraints, and the parent's section on Takabayasi's multipliers records this: the multipliers the spin-fluid literature introduces are the components of the one-form here, and nothing has to be added.

*The mass term's direction is the polarisation.* The one object that a naive reading would take as a free choice — the spin's axis — is fixed by the requirement that the mass bilinear not vanish.

*No discarded term and therefore no accuracy estimate.* There is nothing to size, so the variational route cannot say how good the limit is. The equation route's statement that the corrections are order $\epsilon$ has no variational counterpart here, and that is not a defect of the treatment: for a first-order equation there is no amplitude-curvature term whose size could be the measure.

*No quantum potential.* The corpus's other families discard one and could in principle recover it as a term of the action. Here it is absent by construction, and the statements the corpus makes about it in this family are statements about the iterated equation.

*The gauge orbit of the parametrisation.* The first-order Lagrangian is degenerate, so the velocities are not determined by the momenta and the parametrisation has a freedom. Whether that freedom is the same as the gauge group, and what it does to the limit's statements, is not settled in the corpus.
## Summary
The parent's Dirac action is a one-form plus a potential: every velocity enters linearly, three momenta vanish, and the Euler–Lagrange equations are $\Omega\dot q=\mathrm{d}U$ with a closed and degenerate two-form. The scale enters as $\varrho^{2}$ in both terms and never with its own derivative, so there is no kinetic term to delete.

The limit is therefore a reading and not a truncation: the vanishing momenta are the order-zero constraints — the mass shell and the polarisation of the frame — and the flow is the order-one transport of the density, the velocity and the spin. The algebraic frame of the equation-route companion is the vanishing of three momenta, and its three transport laws are the flow.

The mass term needs a fixed transverse direction, and the direction it needs is the frame's own third: the polarisation and the mass are one object, and the limit inherits both.

The price is exact: with no discarded term there is no accuracy estimate, and with a first-order action there is no quantum potential. The corpus's statements about the latter in this family are about the iterated equation, and the article says so instead of importing them.
## Summary of Notation
| Symbol | Meaning |
|---|---|
| $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The polar word; defined where $N(\tilde\Xi)\neq0$ |
| $\varrho>0$, $\rho_{\mathrm{num}}=\varrho^{2}$ | The scale; the density |
| $\theta_{\mathrm{rpd}}$, $\tilde u_{\mathrm b}$ | The boost's rapidity and axis |
| $\vec\omega_{\mathrm r}$, $\hat n_{\mathrm{rot}}$ | The rotor's body angular velocity and axis |
| $A_x(q)$ | The one-form whose components are the eight momenta |
| $U=\frac{h}{2\pi} ck_m \varrho^{2}\mathcal V$ | The mass potential |
| $\mathcal V$ | The mass function of the frame, independent of $\varrho$ and $\theta_{\mathrm{pha}}$ |
| $i\vec v$ | The fixed direction, transverse to $\vec e_z$, that the mass term requires |
| $\Omega=\mathrm{d}A$ | The closed, degenerate two-form |
| $\epsilon=1/(k_{\Phi}L)$ | The parameter of the ordering |
## Further Reading
- [The Lagrangian and the Dirac Equation in Polar Variables](the-lagrangian-and-the-dirac-equation-in-polar-variables.html), the parent: the action, the one-form, the mass term's fixed direction and Takabayasi's multipliers.
- [The Dirac Equation in the Non-Quantum Limit](the-dirac-equation-in-the-non-quantum-limit.html), the companion: the four brackets, the algebraic frame and the three transport laws.
- [Relativistic Mechanics from the Dirac Wave](relativistic-mechanics-from-the-dirac-wave.html), for the velocity's transport and the precession read from the wave.
- [The Lagrangian and the Klein–Gordon Equation in the Non-Quantum Limit](the-lagrangian-and-the-klein-gordon-equation-in-the-non-quantum-limit.html), the second-order companion, where a term is deleted and the accuracy can be sized.
- [The Non-Quantum Limit of the Biquaternion Model](the-non-quantum-limit-of-the-biquaternion-model.html), for the parameter and the difference between the limit and the approximation.
## Verification
Every occurrence of a velocity in the Lagrangian is linear: $\dot\theta_{\mathrm{pha}}$ enters once with the coefficient $\frac{h}{2\pi} c \varrho^{2}\cosh\theta_{\mathrm{rpd}}$, and $\vec\omega_{\mathrm r}$ enters once through $\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}$ with the coefficient $-\frac{h}{2\pi} c \varrho^{2}\sinh\theta_{\mathrm{rpd}}$. **No velocity is squared and none appears twice**, so the Hessian vanishes and the momenta are the one-form's components.

The Lagrangian contains no $\dot \varrho$, no $\dot\theta_{\mathrm{rpd}}$ and no rate of the boost's axis, so the three conjugate momenta vanish identically. The check is an inspection and it is exact.

The trace computation uses only $\Pi_+^{*}=\Pi_+$, cyclicity, and $\Pi_-\Pi_+=0$, so it holds for every element and not only for the word.

For $\vec v\perp\vec e_z$ the value reverses and the bilinear is non-zero; for $\vec v\parallel\vec e_z$ it does not and the bilinear vanishes. Both cases were checked on the frame's own units.

No solution of the eight first-order equations was integrated, and the constraint analysis was not carried past the primary constraints. The claims are about structure and identities, and both were verified.
