# __The Non-Quantum Limit of the Free Dirac Equation using the Variational Principle__

## Introduction

**The variational route in the Dirac family reaches a different conclusion, and the conclusion is a negative one with content.** In the three other families the polar action is second order in something, and the limit is the deletion of one group of terms from it. Here the polar action is **first order in every velocity**: it is a one-form plus a potential, its Hessian vanishes identically, four of its eight momenta vanish identically, and the remaining four are fixed functions of the coordinates. **There is no term in the amplitude's gradient to delete**, because the amplitude enters the action through the overall density and never through its own derivative.

**So the limit cannot be a truncation here, and the article says what it is instead.** It is the replacement of a differential operator by its symbol, and the object that decides its accuracy is the failure of that replacement to be exact. In the free family the failure is the amplitude's curvature, at order $\epsilon^{2}$ in the eikonal, and there is no commutator because there is no connection.

**The positive result, and it is the article's main claim.** The action's structure is a constraint structure, and the limit does not create it: **the Dirac family's polar action already has the shape the other families' actions acquire only in the limit** — one velocity, the density as the phase's momentum, and a set of constraints on the frame. What the limit adds is a name for the extremum those constraints select: the frame's rapidity is the flow's rapidity and the frame's axis is the momentum's, and the eikonal is the mass potential's value at that extremum.

**So the non-quantum limit of this family, read on the action, is an extremum principle for the frame and not a truncation of a functional.** That is the sentence the article exists to establish, and it is why the twelve-article programme's Dirac pair had to be written from the equation and not from the action: **the action does not contain the term the other routes delete.**

**Conventions.** Those of *The Variational Principle and the Dirac Equation in Biquaternionic Polar Variables*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, $e_t=1$, $\vec e_\mu^{2}=-e_t$, $i$ central, $\mathrm{Sc}$ the coefficient of $e_t$, pairing $\mathrm{Sc}(\cdot^{*}\cdot)$, parameters $r>0$, $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$, $\theta_{\mathrm{rpd}}\ge0$, $\theta_{\mathrm{axr}}\in[0,2\pi)$, unit axes $\vec u_{\mathrm b}$ and $\vec u_{\mathrm r}$. The density is $\rho=r^{2}\cosh\theta_{\mathrm{rpd}}$, the frame's Lorentz factor is $\gamma=\cosh\theta_{\mathrm{rpd}}$, $k_m=mc/\hbar$, and the setting is the constant homogeneous one throughout, since that is the setting in which the parameters are coordinates on a fixed frame.

## The Action in the Chart

**The parent's display.**

$$
S=\int\mathrm{d}t'\;\hbar c\,\Bigl\{r^{2}\Bigl(\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\;\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}\Bigr)-r^{2}k_m\,\mathcal{V}\Bigr\},
$$

with $\vec\omega_{\mathrm r}=\tilde u_{\mathrm r}^{-1}\dot{\tilde u}_{\mathrm r}$ the rotor's body angular velocity and $\hat n_{\mathrm{rot}}=\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}$ the boost axis carried into the body frame.

**Read it as a one-form plus a potential.**

$$
\mathcal L=A_x(q)\,\dot q^{x}-U(q),
\qquad
A=\hbar c\,r^{2}\Bigl[\cosh\theta_{\mathrm{rpd}}\,d\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\;\hat n_{\mathrm{rot}}\cdot\bigl(\tilde u_{\mathrm r}^{-1}d\tilde u_{\mathrm r}\bigr)\Bigr],
\qquad
U=\hbar c\,k_m\,r^{2}\mathcal V .
$$

**Every velocity appears linearly.** So the Hessian $\partial^{2}\mathcal L/\partial\dot q^{x}\partial\dot q^{y}$ vanishes identically, no momentum can be inverted for a velocity, and the eight Euler–Lagrange equations are first order:

$$
\Omega_{xy}\,\dot q^{y}=\partial_x U,
\qquad
\Omega=\mathrm{d}A,\qquad \mathrm{d}\Omega=0 .
$$

**The momenta.** They are the components of $A$, and the parent's table is the statement of that.

| coordinate | momentum | why |
|---|---|---|
| $r$ | $0$ | the scale enters only through $r^{2}$ |
| $\theta_{\mathrm{rpd}}$ | $0$ | the rapidity's rate cancels between $\cosh$ and $\sinh$ |
| the two angles of $\vec u_{\mathrm b}$ | $0$ | the boost axis enters through $\hat n_{\mathrm{rot}}$ and not through a rate |
| $\theta_{\mathrm{pha}}$ | $\hbar c\,r^{2}\cosh\theta_{\mathrm{rpd}}$ | the phase's rate |
| the three rotor coordinates | $-\hbar c\,r^{2}\sinh\theta_{\mathrm{rpd}}\,\hat n_{\mathrm{rot}}$ | a closed form, not a projector |

**Four zeros and four fixed functions.** No momentum is a free variable, so the phase space is not the cotangent bundle: it is the base with a two-form on it, and the dynamics is the one-form's.

**What the parent's mass term costs, and why it is worth recording.** The mass bilinear vanishes identically on the frame's parts, because the two parts sit in complementary right ideals and $\mathrm{Sc}$ is cyclic. It returns only when the bilinear carries a fixed unit direction, the frame's third direction reversed, and the direction is fixed and not chosen. **So the potential $U$ depends on the frame through a function $\mathcal V$ of the rapidity, the axis, the rotor and the fixed direction, and it depends on neither $r$ nor $\theta_{\mathrm{pha}}$.** That independence is the reason two of the four vanishing momenta vanish, and it is the structure the limit will have to read.

## There Is No Term to Drop

**The argument, from the first-order form.** The element action is quadratic in the field and linear in the derivative, so in the chart the amplitude's derivative can only enter as $\tilde\Xi^{*}\partial\tilde\Xi=r\,\partial r\times(\ldots)$: **linear in $\partial r$ and carrying one power of $r$, never as $\lvert\partial r\rvert^{2}$.** There is no term of the form the three other families delete.

**What the three other families delete, for comparison.**

| family | the deleted group | why it exists there |
|---|---|---|
| Schrödinger | $-\frac{\hbar^{2}}{2m}\lvert\vec\nabla r\rvert^{2}$ | a second-order spatial operator acting on $r$ |
| Klein–Gordon | $(\partial r)^{2}$ | a second-order operator in time and space acting on $r$ |
| Dirac, free | **none** | the action is first order, so $\partial r$ enters linearly |

**The consequence, stated bluntly.** A limit that is defined as "delete the amplitude's gradient group" has nothing to delete in this family. **The definition of the limit has to be given in a form that does not presuppose a second-order action**, and the form that works is the operator's: the limit is the statement that the differential operator in the action is, to relative order $\epsilon$, the multiplication by its symbol.

**What that form is, exactly.** Acting on the word, the gradient is

$$
\tilde\nabla_\Phi\tilde\Xi=i\tilde K_{\Psi}\tilde\Xi+\mathcal{O}(\epsilon)\cdot\tilde\Xi,
\qquad
\tilde K_{\Psi}=\frac{1}{\hbar}\Bigl(\frac{E}{c}e_{t}+i\vec p\cdot\vec e\Bigr),
$$

and with a derivative that is a multiplication the action is algebraic. **The action is the same functional before and after**; what changes is that its arguments are evaluated on the symbol's eigenvector and the derivative's error is pushed into a remainder.

**So the corpus's three names for the limit are one name.** "The phase dominates", "the amplitude's gradient is dropped", "the operator is its symbol" are the same statement in three grammars, and this family is the one in which only the third grammar can be written.

## The Criterion

**Unchanged, and it enters through the remainder rather than through a term.**

$$
\epsilon=\frac{1}{k_{\Phi}L}=\frac{\hbar}{\lvert\vec p\rvert L},
$$

with $L$ the length over which the frame's parameters vary. In the homogeneous setting there is no $L$ and therefore no $\epsilon$; **the criterion is a property of the region and the parent's setting has none.** That is not a defect of the parent — it is the reason the parent's flow is exactly the equation's flow — and it is the reason this article must say where $\epsilon$ would enter if the setting had a length.

**Where it would enter.** Not in the action's term list, where the amplitude appears only through $r^{2}$ and $\rho$, but in the remainder of the substitution $\tilde\nabla_\Phi\to i\tilde K_{\Psi}$. The remainder is built from the second derivatives of the frame's parameters, so it is of order $\epsilon$ as an operator statement and of order $\epsilon^{2}$ in the eikonal.

**The second ratio.** $1/(k_mL)=\hbar/(mcL)$ is the Compton length over $L$, the boundary of the one-particle reading, and in this family it has the sharper meaning the route-one companion gives it: it is the scale at which the eikonal's two branches stop being separable. **It is not the criterion and the limit does not need it to be.**

**The table, in the form the family allows.**

| object | the limit's treatment | the accuracy |
|---|---|---|
| the one-form $A$ | untouched; it is linear in the derivatives | exact |
| the potential $U$ | evaluated at the frame the constraints select | the eikonal's order |
| the mass term | kept whole; it is the potential | exact |
| the substitution $\tilde\nabla\to i\tilde K$ | the limit itself | $O(\epsilon)$ as an operator, $O(\epsilon^{2})$ in the eikonal |
| the constraint count | unchanged | exact |

**Read the first and fifth rows together.** They are the family's statement: **nothing is truncated and nothing is added**, and the limit's whole content is the identification of the frame at which the potential is to be evaluated.

## The Limit as a Symbol Replacement

**What the substitution does to the functional.** With the derivative replaced by a multiplication, the one-form's components become numbers and the potential becomes a function of those numbers, so the functional becomes algebraic in the symbol's entries; its variation then gives two algebraic statements rather than eight first-order equations:

$$
\langle\tilde K_{\Psi}\rangle_{\natural}=k_{m}^{2},
\qquad
\frac{\partial U_{0}}{\partial q}=0\ \text{for every frame coordinate},
$$

**with $U_{0}$ the potential evaluated on the symbol's frame. The first is the mass shell and the second is the frame's position, and they are one statement**: the potential's dependence on the frame is the mass term's, so the eikonal is the mass term's value at the frame's extremum. The two are displayed separately only because one is a statement about the momentum and the other about the frame's coordinates.

**Why the free remainder has no commutator.** The commutator of two derivatives vanishes on a scalar amplitude in the absence of a connection, so the remainder is the amplitude's curvature alone — the quantum potential's — and it is real and of order $\epsilon^{2}$. **The first-order family's free limit is therefore accurate to $\epsilon^{2}$ in the eikonal, exactly as the Klein–Gordon family's**, and the two reach the same order by different routes: one by dropping a group of order $\epsilon^{2}$ from the action, the other by keeping every term and bounding the substitution's error.

**The two are the same accuracy and not the same statement.** A truncation declares what it has dropped; a substitution declares what it has replaced and by how much it missed. **In this family only the second declaration is available**, and that is a fact about the action's order and not about the method.

## The Extremum Principle for the Frame

**The potential's frame dependence.** $\mathcal V$ is a function of $\theta_{\mathrm{rpd}}$, $\vec u_{\mathrm b}$, $\theta_{\mathrm{axr}}$ and $\vec u_{\mathrm r}$, and the parent's constraints are that the frame sits where the potential is extremal in those variables.

**The limit gives the extremum a name.** On the symbol's frame the rapidity is the flow's,

$$
\cosh\theta_{\mathrm{rpd}}=\gamma=\frac{E}{mc^{2}},
\qquad
\tanh\theta_{\mathrm{rpd}}=\frac{\lvert\vec p\rvert c}{E}=\frac{\lvert\vec v\rvert}{c},
$$

**and the axis is the momentum's direction**, because the fixed direction the mass term needs is the spin's and the spin's axis on the flow is the helicity's. So the extremum the constraints select is the frame a particle of momentum $\vec p$ carries, and the eikonal is the value of the mass potential there.

**This is the article's claim in its final form.** The non-quantum limit of the free Dirac family, read on the action, says: **of all frames the word admits, the limit keeps the one whose rapidity is the flow's and whose axis is the momentum's, and the eikonal is the mass potential at that frame.** That is an extremum principle and not a truncation, and it explains why the route-one article could find the limit from the equation and not from the action: the equation's symbol already is the frame's condition.

**What the principle does not say.** It does not say the frame is a dynamical variable. The rapidity and the rotor are coordinates of the word, and the constraint that fixes them is a constraint of the action and not an equation of motion. **The frame's values are read off the flow, and the flow is read off the phase**; nothing in the passage gives the frame its own dynamics, and nothing should, since the spin's precession is the order-$\epsilon$ term of the coupled family and not a feature of this one.

**A check on the name.** At $\vec p=0$ the rapidity vanishes, $\cosh\theta_{\mathrm{rpd}}=1$, and the density $\rho=r^{2}\cosh\theta_{\mathrm{rpd}}$ reduces to $r^{2}$ — the rest-frame statement the parent makes when it says the spin's momentum vanishes at rest. **The extremum's value at the rest frame is the free action's density**, and that is the sharpest consistency check the homogeneous setting admits.

## The Spin's Momentum, Read Variationally

**The parent's closed form.** The rotor's momentum is $-\hbar c\,r^{2}\sinh\theta_{\mathrm{rpd}}\,\hat n_{\mathrm{rot}}$, **proportional to the boost and vanishing at rest however fast the rotor turns.**

**That is the variational form of a statement the route-one article makes algebraically.** There the spin is absent at order zero because the leading eikonal is a norm and a norm is central; here its canonical momentum vanishes when the frame is not boosted. **The two statements are the same fact seen from two sides**: a central object cannot act on a spinor, and a coordinate whose conjugate momentum vanishes at rest is not a dynamical variable of the rest frame.

**What the equivalence buys.** It tells us that "the spin is order one" is not a statement about $\hbar$'s smallness but about the word's structure: the rotor's momentum carries $\sinh\theta_{\mathrm{rpd}}$, which is $\lvert\vec v\rvert/c$ to leading order, so **the spin's momentum is itself of order $\beta$ and the spin's dynamics is relativistic by construction.** A nonrelativistic limit would then have to treat the rotor as slow, which is the Bargmann–Michel–Telegdi problem's starting point and not this article's.

**What the variational route does not show.** It does not produce the spin term's coefficient. The parent's action has no field strength in it, so there is nothing for the spin to couple to; the $g=2$ term is a coupled-family object and the coupled companion locates it.

## The Constraint Count Does Not Move

**Before the limit.** The Hessian vanishes identically; four momenta vanish; four are fixed functions of the coordinates; the eight equations are $\Omega\dot q=\mathrm{d}U$ and are first order.

**After the limit.** The Hessian still vanishes, because the limit replaces the operator by a number and cannot raise a derivative's order. The four momenta vanish for the same reason: the scale still enters only through $r^{2}$ and the rapidity still has no rate. **The count is unchanged and the reason is structural**: a system whose Lagrangian is a one-form cannot have a second-order term created in it by an approximation that adds no derivative.

**Why this is worth stating.** In the Klein–Gordon family the limit *creates* the primary constraint — the second time derivative of $r$ is dropped and $p_r=0$ appears. In the Schrödinger family the limit *completes* a constraint that was half present. **Here the constraint was fully present before the limit and the limit is what tells us where the frame sits.** Three families, three relations between the limit and the constraint structure, and the Dirac family's is the empty one — which is a result, because it says the family's classical content is already a constrained system and that the limit cannot be blamed for the constraints.

**A caution the parent already gives.** The constraints are primary and their class has not been determined: whether they are first or second class needs the brackets, and the parent leaves that open. **The article adopts the parent's caution and adds nothing to it**, since a limit that changes no constraint cannot settle a question about their class.

## What the Variational Route Adds

**Three things, and one that it does not.**

*The negative result.* There is no group to delete, so the definition of the limit cannot be "drop the amplitude's gradient" in this family. **That is a constraint on the corpus's own vocabulary**, and it is the reason the Dirac articles of route one had to be derived from the equation.

*The extremum principle.* The limit names the frame: rapidity equal to the flow's, axis equal to the momentum's, eikonal equal to the mass potential there. The equation route can state the same thing only as "the eikonal is $\langle\tilde K_\Psi\rangle_\natural=k_m^{2}$".

*The variational reading of the spin's order.* Its momentum is proportional to $\sinh\theta_{\mathrm{rpd}}$, so it vanishes at rest; the algebraic statement that a central norm cannot act on a spinor has a canonical counterpart.

**What it does not add.** No solution, no new equation, no accuracy better than the substitution's $\epsilon^{2}$. **And no statement about the spatial structure**: the parent's setting is homogeneous, and the gradient terms the word acquires in the operator setting are the spin fluid's standard ones and are stated there without derivation. This article keeps to the parent's setting and says so, because a claim about a truncated functional would need a functional that does not exist in the parent.

## Summary

The free polar Dirac action is a one-form plus a potential, $\mathcal L=A_x\dot q^{x}-U$, with the density $\rho=r^{2}\cosh\theta_{\mathrm{rpd}}$ in the one-form's phase component and the mass as the potential. Its Hessian vanishes identically, four of its eight momenta vanish and four are fixed functions of the coordinates, and its eight equations are $\Omega\dot q=\mathrm{d}U$ and first order. **The action is first order, so the amplitude's derivative enters it linearly and there is no $\lvert\partial r\rvert^{2}$ term: the non-quantum limit of this family cannot be a deletion, and the article's first result is that negative one.**

What the limit is instead is the replacement of a differential operator by its symbol, $\tilde\nabla_\Phi\to i\tilde K_\Psi$, with a remainder of order $\epsilon$ as an operator and $\epsilon^{2}$ in the eikonal, and with no commutator because there is no connection. The criterion is $\epsilon=1/(k_\Phi L)$, it enters through the remainder and not through a term, and the homogeneous parent has no $L$ and therefore no $\epsilon$ — which is why the parent's flow is exactly the equation's flow. The limit's positive content is an **extremum principle for the frame**: of all frames the word admits, the limit keeps the one whose rapidity is the flow's and whose axis is the momentum's, and the eikonal is the mass potential's value there. The constraint count does not move, because a replacement that adds no derivative cannot create one, and that is the third of the three relations the corpus's families bear to their constraints.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S=\int\hbar c\{r^{2}(\cosh\theta_{\mathrm{rpd}}\dot\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r})-r^{2}k_m\mathcal V\}$ | The free polar action |
| $A_x\dot q^{x}-U$ | Its form: a one-form plus a potential |
| $A=\hbar c r^{2}[\cosh\theta_{\mathrm{rpd}}d\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\hat n_{\mathrm{rot}}\cdot(\tilde u_{\mathrm r}^{-1}d\tilde u_{\mathrm r})]$ | The one-form; its components are the momenta |
| $U=\hbar c\,k_m\,r^{2}\mathcal V$ | The potential; the mass |
| $\rho=r^{2}\cosh\theta_{\mathrm{rpd}}$ | The density; the phase momentum over $\hbar c$ |
| $\Omega=\mathrm{d}A$ | The two-form; closed; $\Omega\dot q=\mathrm{d}U$ is the system |
| $\gamma=\cosh\theta_{\mathrm{rpd}}$ | The frame's Lorentz factor; the flow's on the limit's frame |
| $\epsilon=1/(k_\Phi L)$ | The criterion; enters through the substitution's remainder |
| $1/(k_mL)$ | The boundary of the one-particle reading |
| $-\hbar c r^{2}\sinh\theta_{\mathrm{rpd}}\hat n_{\mathrm{rot}}$ | The rotor's momentum; vanishes at rest |
| $\langle\tilde K_\Psi\rangle_\natural=k_m^{2}$ | The eikonal, at the frame the constraints select |

## Further Reading

- T. Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the spin fluid and its constraints.
- P. A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for primary constraints, degenerate Lagrangians and the treatment of a one-form Lagrangian.
- J. L. Synge, *Classical Dynamics* (Springer, 1960), for a system whose Lagrangian is a one-form and whose equations are $\Omega\dot q=\mathrm{d}U$.
- Michael V. Berry and K. E. Mount, "Semiclassical approximations in wave mechanics," *Reports on Progress in Physics* **35** (1972) 315–397, for the symbol of a first-order operator and the size of its remainder.
- Robert G. Littlejohn, "The semiclassical evolution of wave packets," *Physics Reports* **138** (1986) 193–291, for the symbol calculus and the frame a semiclassical spinor carries.
