# __The Lagrangian and the Schrödinger Equation in the Non-Quantum Limit__

**Declared omissions.** The reality of the action is settled inside the action section and not in a section named for it, so slot 5 is omitted. The constraint is the parent's and the limit neither adds nor removes one, so slot 6 is omitted. The second variation is not computed, so slot 8 is omitted. The two settings are not contrasted, so slot 10 is omitted. No comparison beyond the parent is attempted, so slot 13 is omitted. No open question is separated from the verification, so slot 14 is omitted.

## Introduction

**The limit in one sentence.** Write the parent's polar action, delete the one term that carries a spatial derivative of the scale, and the two variations of what is left are the eikonal and the transport equation — the limit as a deletion, and the two surviving equations as the two variations.

**The parent supplies the action, and this article deletes a term from it.** [The Lagrangian and the Schrödinger Equation in Polar Variables](the-lagrangian-and-the-schrodinger-equation-in-polar-variables.html) writes the central field's action in the operator setting and shows that its two Euler–Lagrange equations are the continuity equation and the Hamilton–Jacobi equation with the quantum potential. That action has three kinds of term. This article orders them, deletes one, and reads the two variations of the survivor.

**The gain over the equation route is of one specific kind.** The order count is the term count: nothing has to be estimated and no sensitivity argument is needed, because the parameter appears as the number of derivatives in a term and the truncation is a subtraction. The companion article *The Schrödinger equation in the Non-Quantum Limit* takes the same limit on the parent's pair and has to say which term of an equation is small; here the term is deleted and the equations follow.

**What the deletion does, stated exactly, because it is the article's result.** The parent's action has one term with $\lvert\vec\nabla_\Phi \varrho\rvert^{2}$ and no other term carrying a derivative of the scale. Varying the phase gives the transport equation, and that variation is unchanged by the deletion: the same divergence, term for term. Varying the scale gives the quantum-potential equation when the term is present and the eikonal when it is absent. **One deletion changes one equation and leaves the other identical**, and that asymmetry is the variational form of the statement that the limit truncates the real line and leaves the imaginary one exact.

**What the truncated action is, in one line.** It is the action of an irrotational pressureless fluid whose velocity is the phase gradient over the mass, and its two variations are that fluid's continuity equation and its Hamilton–Jacobi equation. The deleted term is the only one that would give the fluid a pressure, and the quantum potential is exactly that pressure's potential.

**The restriction, imported from the parent and not removable.** The action below is the central field's, $\theta_{\mathrm{rpd}}=0$ and $\tilde u_{\mathrm r}=\varepsilon e_{t}$, and the parent proves that class is invariant exactly under a central Hamiltonian. The same restriction governs the companion's equation route, so the two articles are restricted in the same place and for the same reason.

**One caution the parent supplies, and it matters here.** The parent proves that on the central field the cross term of the general action vanishes identically, so the central case cannot detect an error in it: *every statement about the central field in that section would survive the error of dropping the cross term*. The limit inherits the blindness, and it is harmless here for a reason worth one sentence: the limit is defined on the central class, so a term that vanishes identically there cannot enter the truncated action at any order.

**What the article establishes, in five sentences.** The parent's action splits into orders $0$ and $2$ and no term of order $1$. The single order-$2$ term is the scale's gradient, which is the quantum potential's origin. Its deletion leaves an action whose variation with respect to the scale is the eikonal and whose variation with respect to the phase is the transport equation, the second of which is unchanged by the deletion. The truncated action is gauge invariant under a constant phase shift and is the hydrodynamical action of a potential flow. What the route does not supply is the size of the discarded term, which is the companion's subject.

**What is not new.** That the semiclassical limit of a wave equation is a truncation of its action, that the leading-order action is the Hamilton–Jacobi action, and that the transport equation is its phase variation are standard results of semiclassical mechanics. Added here: the identification of the deleted term with one factor of the complete polar decomposition, the exact statement that the phase variation is invariant under the deletion, and the reading of the truncated action as a pressureless fluid's.

## Conventions

**The conventions are the corpus's, restated here so that every sign below is checkable from this page alone.** Those of the variational polar parent: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_{t}=1$ and $\vec e_\mu^{2}=-e_{t}$; $\mathrm{Sc}$ the coefficient of $e_{t}$; the word $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ with its eight real parameters; the central field $\theta_{\mathrm{rpd}}=0$, $\tilde u_{\mathrm r}=\varepsilon e_{t}$; the operator setting $\tilde H_\Psi=\hat H e_{t}$ with $\hat H=-\hbar^{2}\Delta_\Phi/2m+V_{\mathrm{op}}(\vec x)$; $\Delta_\Phi$ the Laplacian of the material sector; $S=\hbar\theta_{\mathrm{pha}}$.

## The Action in the Non-Quantum Limit: The Two Orders

**The parent's action for the central field in the operator setting.**

$$
S_{\mathrm{central}}=\int \mathrm{d}t'\,\mathrm{d}^{3}x\;\Bigl[-\hbar\,\varrho^{2}\dot\theta_{\mathrm{pha}}-\frac{\hbar^{2}}{2m}\bigl(\lvert\vec\nabla_\Phi \varrho\rvert^{2}+\varrho^{2}\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}\rvert^{2}\bigr)-\varrho^{2}V_{\mathrm{op}}\Bigr],
$$

with $\dot\theta_{\mathrm{pha}}=\partial_{t'}\theta_{\mathrm{pha}}$ and $V_{\mathrm{op}}$ a function of position. Four terms, and the parent's display is reproduced without change.

**Every term is one of the word's factors squared, multiplied by zero, one or two derivatives.** The table is the article's premise, and its third column is the whole of the limit.

| term | what it carries | order in $\epsilon$ |
|---|---|---|
| $-\hbar\,\varrho^{2}\dot\theta_{\mathrm{pha}}$ | scale squared, one time derivative of the phase | $0$ |
| $-\frac{\hbar^{2}}{2m}\varrho^{2}\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}\rvert^{2}$ | scale squared, two spatial derivatives of the phase | $0$ |
| $-\frac{\hbar^{2}}{2m}\lvert\vec\nabla_\Phi \varrho\rvert^{2}$ | two spatial derivatives of the scale | $2$ |
| $-\varrho^{2}V_{\mathrm{op}}$ | scale squared, no derivative | $0$ |

**Only one term is of order two, and it is the only one carrying a derivative of the scale.** The parameter counts derivatives of the scale, one power each, and no other term of the parent's action has one. There is no term of order one and no term of order three: the action has two orders and a gap between them.

**The time derivative is not ordered.** The action is first order in time, so the term $-\hbar \varrho^{2}\dot\theta_{\mathrm{pha}}$ carries a time derivative of the phase and no power of $\epsilon$ at all. This is the variational form of the statement that the equation is first order in time and has no mass shell: the action's time structure is a legendre transform of a first-order system, not an expansion.

**Why the phase's gradient is order zero and the scale's is order one.** In the phase, a spatial derivative brings down $k_{\Phi}=\lvert\vec p\rvert/\hbar$, which is the large number. In the scale, a spatial derivative brings down $L^{-1}$, which is small against it. The ratio is the parameter, $\epsilon=1/(k_{\Phi}L)$, and the distinction is exactly the one the companion states: only derivatives of the scale are ordered.

## The Limit: The Deletion

**Delete the order-two term.** That is the whole of the limit in this route:

$$
S_{\mathrm{cl}}=\int \mathrm{d}t'\,\mathrm{d}^{3}x\;\Bigl[-\hbar\,\varrho^{2}\dot\theta_{\mathrm{pha}}-\frac{\hbar^{2}}{2m}\varrho^{2}\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}\rvert^{2}-\varrho^{2}V_{\mathrm{op}}\Bigr].
$$

**The subscript is the claim.** $S_{\mathrm{cl}}$ is the classical action: its variations are the equations of a fluid with no pressure, and the two equations it produces are the two orders the companion's pair produces by truncating an equation.

**Nothing else is deleted, and nothing is added.** The other three terms are kept with their coefficients unchanged, and no term is moved from one order to another by a redefinition. The deletion is a subtraction and it is exact in the sense that the parameter's power is a property of the term and not of the field.

**The four terms have a reading, and it is worth one line each.** The first is the phase's rate times the density, and it is what makes the action first order. The second is the kinetic energy of the flow, $\rho_{\mathrm{num}}\lvert\vec v\rvert^{2}/2$ with $\rho_{\mathrm{num}}=\varrho^{2}$ and $\vec v=\hbar\vec\nabla_\Phi\theta_{\mathrm{pha}}/m$. The third, deleted, is the only term quadratic in the scale's gradient. The fourth is the potential energy times the density.

## The Variation: Varying the Scale: the Eikonal

**The scale's variation, on the truncated action.** With $\partial L_{\mathrm{cl}}/\partial(\partial_\mu \varrho)=0$ because no term of $L_{\mathrm{cl}}$ carries a derivative of $\varrho$, the Euler–Lagrange equation is algebraic:

$$
-2\varrho\Bigl(\hbar\,\dot\theta_{\mathrm{pha}}+\frac{\hbar^{2}}{2m}\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}\rvert^{2}+V_{\mathrm{op}}\Bigr)=0 ,
$$

that is, away from the node $\varrho=0$,

$$
\boxed{\ \hbar\,\dot\theta_{\mathrm{pha}}+\frac{\hbar^{2}}{2m}\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}\rvert^{2}+V_{\mathrm{op}}=0\ }
$$

**This is the Hamilton–Jacobi equation with $S=\hbar\theta_{\mathrm{pha}}$**, and it is the same equation the companion calls order zero.

**On the full action the same variation carries the quantum potential.** Keeping the deleted term, $\partial L/\partial(\partial_{i}\varrho)=-\frac{\hbar^{2}}{m}\partial_{i}\varrho$, so the Euler–Lagrange equation gains a divergence and reads

$$
-2\varrho\Bigl(\hbar\dot\theta_{\mathrm{pha}}+\frac{\hbar^{2}}{2m}\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}\rvert^{2}+V_{\mathrm{op}}\Bigr)+\frac{\hbar^{2}}{m}\Delta_\Phi \varrho=0 ,
$$

which is the parent's quantum-potential equation with $Q=-\hbar^{2}\Delta_\Phi \varrho/(2m\varrho)$. **The two equations differ by exactly the deleted term and by nothing else.**

**The eikonal is therefore the statement that the amplitude is a Lagrange multiplier.** On the truncated action the scale has no momentum, so it enters as a multiplier of the constraint and its variation returns the constraint. The parent says the same thing from the other side: on the central field the density is conserved and the phase rate is fixed, and the scale's equation is the one that constrains.

**In the algebra the constraint is a norm.** Writing $\vec\nabla_\Phi S=\hbar\vec\nabla_\Phi\theta_{\mathrm{pha}}$ as a real quaternion, $\langle\vec\nabla_\Phi S\rangle_{\natural}=\lvert\vec\nabla_\Phi S\rvert^{2}$, so the constraint reads

$$
\frac{1}{2m}\langle\vec\nabla_\Phi S\rangle_{\natural}=E-V_{\mathrm{op}}
$$

for a stationary state, and the leading-order equation is the vanishing of a quadratic form the algebra already carries.

## The Structural Consequence: Varying the Phase: the Transport, Unchanged

**The phase's variation, on the truncated action.**

$$
\hbar\,\partial_{t'}\varrho^{2}+\frac{\hbar^{2}}{m}\vec\nabla_\Phi\cdot\bigl(\varrho^{2}\vec\nabla_\Phi\theta_{\mathrm{pha}}\bigr)=0 ,
$$

that is, with $S=\hbar\theta_{\mathrm{pha}}$,

$$
\boxed{\ \frac{\partial \varrho^{2}}{\partial t'}+\vec\nabla_\Phi\cdot\Bigl(\varrho^{2}\frac{\vec\nabla_\Phi S}{m}\Bigr)=0\ }
$$

the transport equation, a conservation law for the density $\varrho^{2}$ carried by the velocity $\vec\nabla_\Phi S/m$.

**This equation is identical on the full action, term for term, and that is the article's sharpest statement.** The deleted term carries no $\theta_{\mathrm{pha}}$, so $\partial L/\partial\theta_{\mathrm{pha}}$ and $\partial L/\partial(\partial_\mu\theta_{\mathrm{pha}})$ are the same on $L$ and on $L_{\mathrm{cl}}$. **The transport equation is not an order of an expansion: it is invariant under the deletion**, which is the variational form of the companion's statement that the imaginary line survives the limit untouched.

**The two variations are the two orders, and the pairing is structural.** Varying the scale returns the constraint, which is the deleted order's equation; varying the phase returns the conservation law, which no order touches. In the equation route the same two statements are a real line and an imaginary line of one complex equation. **The variational route makes the pairing a consequence of which variable appears in the deleted term**, and that is the whole of its gain.

**What the truncated action describes.** A fluid of density $\varrho^{2}$ and velocity $\vec\nabla_\Phi S/m$, irrotational because the velocity is a gradient, with no pressure and with a body force $-\vec\nabla_\Phi V_{\mathrm{op}}$. Its two equations are the two the limit produces, and the deleted term is exactly the pressure: $-\frac{\hbar^{2}}{2m}\lvert\vec\nabla_\Phi \varrho\rvert^{2}$ is the internal energy of a fluid whose pressure potential is the quantum potential, since $\frac{\hbar^{2}}{2m}\lvert\vec\nabla_\Phi\ln \varrho\rvert^{2}$ differentiated gives the quantum force.

**The symmetry that survives.** A constant shift $\theta_{\mathrm{pha}}\to\theta_{\mathrm{pha}}+\theta_{0}$ leaves the truncated action invariant, because only the derivative appears. A shift depending on position does not, because the kinetic term is not invariant under it; the action is not gauge invariant and the free Schrödinger equation is not either. **The truncation therefore preserves exactly the symmetry the parent's action has**, and no symmetry is broken or gained by the deletion.

## The Noether Currents: Density, Charge and Energy

**The current is the density times the transport velocity, and the limit makes that literal.** The phase's momentum is the density,
$$
\rho=\varrho^{2}\cosh\theta_{\mathrm{rpd}}\ \longrightarrow\ \varrho^{2}\quad\text{in the non-quantum limit},
$$
and the phase's Euler–Lagrange equation is the continuity equation $\partial_{r'_t}\rho+\vec\nabla_\Phi\cdot(\rho\vec v)=0$ with $\vec v$ the transport velocity. The limit does not change the equation; it removes the terms that made $\rho$ differ from $\varrho^{2}$.

**The charge and the energy.** The charge is the integral of $\rho$, times the coupling where the field is charged, and it carries no mass. The energy is the mass shell's value, and it carries the mass. The split is exact in the parent and survives the limit unchanged, which is why this article's verification section can check both in one line each.

**What the deletion does to the two.** The deleted term is a gradient of the scale, and a gradient cannot change a charge; it can change the energy's value at a given configuration but not its conservation. So the limit's currents are the parent's currents with the density's correction dropped, and the error in each is the order of the deleted block.

## The Limit: The Truncation and Its Error

**The deleted block, and its order.** The limit drops $(\nabla\varrho)^{2}/(2m\varrho)$, which carries two spatial derivatives and no time derivative. **Its order is two and its coefficient is $\hbar^{2}/2m$**, so the error is second order in the parameter and first order in $\hbar$ — a quantum correction in the literal sense.

**Restoring it.** The restored term enters the equation for the velocity field and not the equation for the phase, and it is the gradient of the quantum potential. **It is large where the density is small**, and the article's nodal exception is the statement of where the truncated theory stops.

**The error is a functional of the density alone.** The block contains no phase and no potential, so the correction cannot move the eikonal. **The eikonal therefore survives exactly and the velocity equation survives only to order $\epsilon^{2}$**, and the asymmetry is the whole of the truncation's cost.

**Why the truncation is not covariant.** The block is a spatial gradient, so it distinguishes the slicing, and the truncated theory inherits the frame the Schrödinger equation already picks. **The article says so plainly**: the free Schrödinger family's non-quantum limit is not Lorentz covariant and was never meant to be.

**What the error is not.** No bound and no rate. **The expansion is asymptotic and the article does not claim convergence**, so "second order" is a statement about the term's size for slowly varying densities and not about the distance between solutions.

**Why the section follows the deletion.** Because the deletion names the term and this section prices it, and the price is what a reader needs before reading the surviving equations as exact.

## The Limit: What Survives

**The eikonal, exactly.** The scale's variation of the truncated action gives the eikonal equation, and it is not an approximation to the parent's: **it is the parent's equation with the quantum potential set to zero**, and the difference is the deleted block alone.

**The transport, unchanged.** The phase's variation gives the transport, and the deleted block contains no phase, so the transport is identical. **The current is the transport's own consequence**, and it survives with the parent's expression.

**The density and the energy.** The conjugate quantities of the truncated action are the parent's first integrals with the density's correction removed. **Density, flux and energy keep their signs**, and the only quantity that changes is the one that depends on the density's curvature.

**The frame, and the one thing that is lost.** The truncated theory inherits the slicing the Schrödinger equation already picks, so **the eikonal-plus-transport system is not Lorentz covariant and cannot be made so by a choice of variables**. The article states this as a loss and not as a technicality.

**The nodal exception.** Where the density vanishes the quantum potential diverges, so the truncated theory's own equations fail there even before the parent's correction is considered. **The article's one sentence about nodes is in the section on the deletion**, and this section does not repeat it.

**Why the list is short.** One block is deleted and four are kept, so the truncated theory is the eikonal plus the transport plus the currents. **That is the whole of the non-quantum limit of the Schrödinger family**, and the article's summary says exactly that in one line.

## What the Principle Adds and What It Relabels: By the Variational Route

**Three things, and each is a statement about the terms that the equation route can only make about equations.**

*The order is a property of a term and not of a solution.* In the companion, the smallness of a term has to be argued from the field: $\lvert\hbar\vec\nabla_\Phi\ln \varrho\rvert/\lvert\vec\nabla_\Phi S\rvert\sim\epsilon$ is a statement about a solution. Here $\lvert\vec\nabla_\Phi \varrho\rvert^{2}$ is order two because it carries two derivatives, and that is true of the term for every field in the class. **The count is exact where the estimate is not.**

*The deletion is one operation and it produces both equations.* No second truncation and no consistency condition between the two halves: the variation of the survivor is taken and the two equations come out. In the equation route the two lines are truncated separately and the claim that they are consistent has to be checked.

*The quantum potential is identified as a term and not as a correction.* It is the only term of the action carrying a derivative of the scale, so the statement "the limit deletes the quantum potential" becomes "the limit deletes the scale's kinetic term". **That is the sharper form**, because it says what the term is rather than what it costs.

**What it does not add, and the list is short.**

*The size of the discarded term.* The action route says the term is order two and does not say where the expansion stops. That is the companion's table, and its ratio $\lvert Q\rvert/(E-V)=\epsilon^{2}\lvert x^{2}/4\sigma^{2}-1/2\rvert$ is a statement about a solution that no term count supplies.

*The boundary terms.* The deletion changes the natural boundary conditions: an action with $\lvert\vec\nabla_\Phi \varrho\rvert^{2}$ needs a Neumann datum on the scale at the boundary, and the truncated one does not. The corpus states the limit on the whole of space and does not examine the boundary, which is honest and is a gap.

*The interaction with a connection.* The coupled families' action carries the connection, and the truncation there is not a single deletion, because the connection's term distributes over the two variations. That is the coupled companion's subject, not this article's.

## Verification

**Both Euler–Lagrange systems were computed, with the term and without it.** The parent's action was varied with respect to $\varrho$ and $\theta_{\mathrm{pha}}$, and so was the truncated action. The results are exact and the difference is one term.

| variation | full action | truncated action |
|---|---|---|
| with respect to $\varrho$ | eikonal with $+\frac{\hbar^{2}}{m}\Delta_\Phi \varrho$ | eikonal alone |
| with respect to $\theta_{\mathrm{pha}}$ | $\partial_{t'}\varrho^{2}+\vec\nabla_\Phi\cdot(\varrho^{2}\vec\nabla_\Phi S/m)=0$ | the same, identically |

**The second row is the check that matters.** The phase's Euler–Lagrange equation was computed twice and compared symbolically; the two expressions are equal as written and no rearrangement is needed, because the deleted term contains no $\theta_{\mathrm{pha}}$.

**The first row was checked for the sign.** Keeping the term, the $\varrho$-equation is $-2\varrho(\hbar\dot\theta_{\mathrm{pha}}+\frac{\hbar^{2}}{2m}\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}\rvert^{2}+V_{\mathrm{op}})+\frac{\hbar^{2}}{m}\Delta_\Phi \varrho=0$, which divided by $-2\varrho$ is the companion's real line with $Q=-\hbar^{2}\Delta_\Phi \varrho/(2m\varrho)$. Deleting the term removes the divergence and leaves the bracket. The two differ by $Q$ and by nothing else.

**The order table was checked by substitution.** Each of the four terms was inspected for the number of spatial derivatives it carries on the scale and on the phase; the counts are $0,0,2,0$ and no term was found with an intermediate count.

**What was not checked.** No numerical minimisation of the truncated action was run, and no boundary-value problem was solved. The article's claims are about the terms and the two variations, and both were verified as algebra.

## Summary

The parent's polar action for the central field has four terms: the phase's rate times the density, the flow's kinetic energy, the scale's gradient squared, and the potential times the density. The parameter counts spatial derivatives of the scale, so three terms are order zero and one is order two.

The limit is the deletion of the order-two term, and the deletion is a subtraction and nothing more. Varying the scale of the truncated action gives the Hamilton–Jacobi equation, which is the companion's order zero; varying the phase gives the transport equation, which the deletion leaves identical term for term. **One deletion changes one equation and leaves the other untouched.**

The truncated action is the action of an irrotational pressureless fluid of density $\varrho^{2}$ and velocity $\vec\nabla_\Phi S/m$, and the deleted term is its pressure. The eikonal is then the statement that the scale is a Lagrange multiplier of the constraint, and the transport equation is the fluid's conservation law.

Three gains over the equation route: the order is a property of a term rather than an estimate about a solution, one deletion produces both equations, and the quantum potential is identified as the scale's kinetic term rather than as a correction. The restriction is the parent's: the action is the central field's, and the class is invariant only under a central Hamiltonian.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The parent's polar word |
| $\varrho>0$ | The scale; the density is $\varrho^{2}$ on the central field |
| $\theta_{\mathrm{pha}}$, $S=\hbar\theta_{\mathrm{pha}}$ | The central angle; the action |
| $\varepsilon e_{t}$ | The rotor on the central field |
| $V_{\mathrm{op}}(\vec x)$ | The operator's scalar potential |
| $S_{\mathrm{central}}$ | The parent's action |
| $S_{\mathrm{cl}}$ | The truncated action; the classical, pressureless one |
| $\epsilon=1/(k_{\Phi}L)$ | The parameter; one power per derivative of the scale |
| $k_{\Phi}=\lvert\vec p\rvert/\hbar$ | The phase's wave number |
| $Q=-\hbar^{2}\Delta_\Phi \varrho/(2m\varrho)$ | The quantum potential; the deleted term's equation |
| $\Delta_\Phi$ | The Laplacian of the material sector |

## Further Reading

- [The Lagrangian and the Schrödinger Equation in Polar Variables](the-lagrangian-and-the-schrodinger-equation-in-polar-variables.html), the parent: the action, its two currents, and the cross-term caution.
- [The Schrödinger equation in the Non-Quantum Limit](the-schrodinger-equation-in-the-non-quantum-limit.html), the companion: the same limit on the parent's pair, and the size of the discarded term.
- [The Schrödinger Equation in Biquaternionic Polar Variables](the-schrodinger-equation-in-biquaternionic-polar-variables.html), for the word and the exact pair the action reproduces.
- [The Non-Quantum Limit of the Biquaternion Model](the-non-quantum-limit-of-the-biquaternion-model.html), for the parameter and the difference between the limit and the approximation.
- [The Lagrangian and the Klein–Gordon Equation in the Non-Quantum Limit](the-lagrangian-and-the-klein-gordon-equation-in-the-non-quantum-limit.html), where the second order restores a mass shell.
- [The Complete Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-complete-polar-decomposition-of-an-n-regular-biquaternion.html), for the word and its factors.
