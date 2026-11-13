# __The Non-Quantum Limit, the Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Polar Variables__

## Introduction

**The limit in one sentence.** Write the parent's coupled polar action, delete the one term carrying a spatial derivative of the scale, and the two variations of what is left are the covariant Hamilton–Jacobi equation and the covariant continuity equation.

**The parent supplies the action and its split into three coupling pieces.** [The Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-schrodinger-equation-in-biquaternionic-polar-variables.html) writes the coupled Lagrangian, shows that the connection enters the kinetic term through one covariant replacement, and separates that term into the free, paramagnetic and diamagnetic pieces. Its Euler–Lagrange equations are the covariant pair. This article orders the terms and deletes one.

**The deletion is the free one and it is the only one.** The term deleted here is the same term deleted in the free variational companion, $-\frac{\hbar^{2}}{2m}\lvert\vec\nabla_\Phi r\rvert^{2}$, and the connection does not touch it: it carries no $\theta_{\mathrm{pha}}$ and no $\vec A$. **One term, the same term, in both families.**

**The article's central clarification is about the coupling, and it is a warning.** The parent's split into free, paramagnetic and diamagnetic pieces invites a second expansion, in powers of $q$. That expansion is not this limit and it is not compatible with it. All three pieces carry the same order in $\epsilon$, because the parameter counts derivatives of the scale and none of the three has one. **The coupling is not small in this limit; it is leading**, and a reader who treats $q\vec A$ as a perturbation is computing a different approximation of a different equation.

**The consequence for the leading term.** The leading term is the full covariant kinetic energy $\lvert\vec\nabla_\Phi S-q\vec A\rvert^{2}/2m$, not the free one plus corrections. The limit's leading equation changes value when the potential is switched on and its order never does, which is the same statement the equation-route companion makes and the reason the two agree term for term.

**What the article establishes, in five sentences.** The parent's action has five terms, three of order zero in the phase and one of order two in the scale, and the fifth is the potential energy. The single deletion leaves the covariant classical action, whose variation with respect to the scale is the eikonal in the kinetic momentum and whose variation with respect to the phase is the covariant continuity equation, the second unchanged by the deletion. The truncated action is gauge invariant exactly, with the phase translated and the potential shifted, and the invariance is the parent's statement that the gauge group is one coordinate of the chart. The three coupling pieces are of one order, so the coupling enters the leading term and no expansion in it exists.

**What is not new.** The covariant Madelung action, the paramagnetic–diamagnetic split, the covariant continuity equation and the derivation of the covariant Hamilton–Jacobi equation from an action are standard, and the split is in every textbook on the hydrodynamical formulation of a charged field. Added here: the ordering of the parent's five terms against one parameter, the statement that all three coupling pieces are leading, and the reading of the truncated action's gauge invariance on the chart.

**The restriction is the free one.** The action is the central field's, $\theta_{\mathrm{rpd}}=0$ and $\tilde u_{\mathrm r}=\varepsilon e_{t}$, and the parent proves that class is invariant exactly under a central Hamiltonian. The limit is defined there and nowhere else, in this family as in the other three.

**The sign, stated once.** The parent's coupling is $ϙ$ with $ϙ=-q$; its action carries $+ϙ\varphi\,r^{2}$, which is $-q\varphi\,r^{2}$ here, and its covariant gradient is $\vec\nabla_\Phi\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A$, which is $(\vec\nabla_\Phi S-q\vec A)/\hbar$ here. Every display below uses $q$, the electric charge, and $\vec\pi=\vec\nabla_\Phi S-q\vec A$.

**Conventions.** Those of the coupled variational polar parent: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_{t}=1$ and $\vec e_\mu^{2}=-e_{t}$; $\mathrm{Sc}$ the coefficient of $e_{t}$; the word $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$; the connection $\tilde A_\Phi=i(\varphi/c)e_{t}+\vec A$; the operator $\hat H^{\mathrm{gco}}=\tilde{\vec\pi}^{\,2}/2m+q\varphi+\hat V$ with $\tilde{\vec\pi}=-i\hbar\nabla-q\vec A$; $S=\hbar\theta_{\mathrm{pha}}$; $\Delta_\Phi$ the Laplacian of the material sector.

## The Action and Its Orders

**The parent's action for the central field in the operator setting.**

$$
S_{\mathrm{cpl}}=\int \mathrm{d}t'\,\mathrm{d}^{3}x\;\Bigl[-\hbar\,r^{2}\dot\theta_{\mathrm{pha}}
-\frac{\hbar^{2}}{2m}\Bigl(\lvert\vec\nabla_\Phi r\rvert^{2}+r^{2}\Bigl\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\Bigr\rvert^{2}\Bigr)
-r^{2}V_{\mathrm{op}}+ϙ\varphi\,r^{2}\Bigr],
$$

with $ϙ=-q$. Five terms, and the parent's display is reproduced without change.

**Every term in the article's letters, with its order.**

| term | what it carries | order in $\epsilon$ |
|---|---|---|
| $-\hbar\,r^{2}\dot\theta_{\mathrm{pha}}$ | scale squared, one time derivative of the phase | $0$ |
| $-\frac{\hbar^{2}}{2m}r^{2}\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}\rvert^{2}$ | scale squared, two spatial derivatives of the phase | $0$ |
| $-\frac{\hbar q}{m}r^{2}\,\vec A\cdot\vec\nabla_\Phi\theta_{\mathrm{pha}}$ | scale squared, one spatial derivative of the phase and the potential | $0$ |
| $-\frac{q^{2}}{2m}r^{2}\lvert\vec A\rvert^{2}$ | scale squared, the potential only | $0$ |
| $-\frac{\hbar^{2}}{2m}\lvert\vec\nabla_\Phi r\rvert^{2}$ | two spatial derivatives of the scale | $2$ |
| $-r^{2}V_{\mathrm{op}}-q\varphi\,r^{2}$ | scale squared, no derivative | $0$ |

**The three middle rows are the parent's one term, split.** The parent separates $-\frac{\hbar^{2}}{2m}r^{2}\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\rvert^{2}$ into the free kinetic term, the paramagnetic term linear in $\vec A$, and the diamagnetic term quadratic in $\vec A$, and gives the sign of the third as the reason the energy is bounded below: the quadratic term is positive for every $\vec A$.

**All three carry order zero, and that is the article's sharpest statement about the coupling.** The parameter counts spatial derivatives of the scale. None of the three pieces has one. **The paramagnetic term is linear in the phase's gradient and linear in the potential, and it is leading**, which is the variational face of the companion's rule that the criterion is written on the mechanical momentum: $\vec\pi$ contains $\vec A$, so a piece of $\lvert\vec\pi\rvert^{2}$ that is linear in $\vec A$ is part of the leading term and not a correction to it.

**There is no expansion in $q$, and the reason is one sentence.** An expansion in $q$ would order the three pieces as $q^{0}$, $q^{1}$, $q^{2}$, which is a bookkeeping in the coupling rather than in the derivatives; the limit's parameter is the derivative count and the two bookkeepings are different. **A truncated series in $q$ would truncate the leading term of this limit**, and that is a different approximation of the same equation.

## The Deletion

**Delete the only order-two term.** That is the whole of the limit:

$$
S_{\mathrm{cl}}=\int \mathrm{d}t'\,\mathrm{d}^{3}x\;\Bigl[-\hbar\,r^{2}\dot\theta_{\mathrm{pha}}
-\frac{\hbar^{2}}{2m}r^{2}\Bigl\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\Bigr\rvert^{2}
-r^{2}V_{\mathrm{op}}+ϙ\varphi\,r^{2}\Bigr].
$$

**Nothing else changes, and no term is resealed.** The connection sits in the kinetic term exactly where the parent put it, and the potential energy keeps its coefficient.

**What the truncated action is.** The action of a charged, irrotational, pressureless fluid: density $r^{2}$, velocity $\vec\pi/m=(\vec\nabla_\Phi S-q\vec A)/m$, no pressure, and a body force from $\varphi$ and $\vec A$. The deleted term is the fluid's pressure, as it is in the free case, and it is the only pressure the theory has.

## Varying the Scale: the Covariant Eikonal

**The scale's variation of the truncated action.** No term of $S_{\mathrm{cl}}$ carries a derivative of $r$, so the Euler–Lagrange equation is algebraic:

$$
-2r\Bigl(\hbar\,\dot\theta_{\mathrm{pha}}+\frac{\hbar^{2}}{2m}\Bigl\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\Bigr\rvert^{2}+V_{\mathrm{op}}-ϙ\varphi\Bigr)=0 ,
$$

that is, away from the node $r=0$,

$$
\boxed{\ \partial_{t'}S+\frac{\lvert\vec\nabla_\Phi S-q\vec A\rvert^{2}}{2m}+q\varphi+V_{\mathrm{op}}=0\ }
$$

with $S=\hbar\theta_{\mathrm{pha}}$ and $ϙ=-q$. **This is the covariant Hamilton–Jacobi equation**, and it is the companion's order zero.

**With the term kept, the same variation carries the quantum potential.** Then $\partial L/\partial(\partial_{i}r)=-\frac{\hbar^{2}}{m}\partial_{i}r$ and the equation gains a divergence:

$$
-2r\Bigl(\hbar\dot\theta_{\mathrm{pha}}+\frac{\hbar^{2}}{2m}\Bigl\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\Bigr\rvert^{2}+V_{\mathrm{op}}-ϙ\varphi\Bigr)+\frac{\hbar^{2}}{m}\Delta_\Phi r=0 ,
$$

which divided by $-2r$ is the parent's Hamilton–Jacobi equation with $Q=-\hbar^{2}\Delta_\Phi r/(2mr)$. **The two differ by exactly the deleted term and by nothing else**, and the potential's coefficient is the same in both.

**The quantum potential does not carry the connection, and the action shows why.** The deleted term is $\lvert\vec\nabla_\Phi r\rvert^{2}$, a function of the scale alone. The scale is invariant under the gauge group, so its gradient is too, and the divergence that follows from it is $Q$ and nothing more. **This is the variational form of the parent's first finding**, which the equation route obtains by inspection.

## Varying the Phase: the Covariant Transport, Unchanged

**The phase's variation of the truncated action.**

$$
\hbar\,\partial_{t'}r^{2}+\frac{\hbar}{m}\vec\nabla_\Phi\cdot\Bigl(r^{2}\bigl(\vec\nabla_\Phi S-q\vec A\bigr)\Bigr)=0 ,
$$

that is

$$
\boxed{\ \frac{\partial r^{2}}{\partial t'}+\vec\nabla_\Phi\cdot\Bigl(r^{2}\frac{\vec\pi}{m}\Bigr)=0\ }
$$

the covariant continuity equation, whose current is the kinetic momentum over the mass.

**It is identical on the full action, and the reason is again the deleted term's content.** The deleted term contains no $\theta_{\mathrm{pha}}$ and no $\vec A$, so both derivatives of the Lagrangian with respect to the phase are unchanged. **The transport equation is not an order of an expansion**: it is invariant under the deletion, and that invariance is the variational statement that the connection changes the current's carrier and not its structure.

**The paramagnetic term is what puts $\vec A$ into the current.** Differentiating $\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\rvert^{2}$ with respect to $\vec\nabla_\Phi\theta_{\mathrm{pha}}$ returns the covariant gradient, so the momentum conjugate to the phase is $\hbar r^{2}(\vec\nabla_\Phi\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A)=r^{2}\vec\pi$, the current. **The piece that looks like a perturbation in the action is the piece that makes the current gauge invariant**, and that is why it cannot be dropped.

## Gauge Invariance of the Truncated Action

**The transformation on the chart.** With $\Gamma$ real, the phase is translated, the vector potential shifted, and the scalar potential shifted:

$$
\theta_{\mathrm{pha}}\longmapsto\theta_{\mathrm{pha}}+\frac{q}{\hbar}\Gamma,
\qquad
\vec A\longmapsto\vec A+\vec\nabla_\Phi\Gamma,
\qquad
\varphi\longmapsto\varphi-\partial_{t'}\Gamma .
$$

**Two combinations are invariant and the action is built from them.** The covariant gradient is unchanged, because the phase's shift and the potential's shift cancel inside one bracket:

$$
\vec\nabla_\Phi\theta_{\mathrm{pha}}-\frac{q}{\hbar}\vec A\ \longmapsto\ \vec\nabla_\Phi\theta_{\mathrm{pha}}+\frac{q}{\hbar}\vec\nabla_\Phi\Gamma-\frac{q}{\hbar}\vec A-\frac{q}{\hbar}\vec\nabla_\Phi\Gamma=\vec\nabla_\Phi\theta_{\mathrm{pha}}-\frac{q}{\hbar}\vec A ,
$$

and so is the kinetic energy, because the rate's shift and the scalar potential's shift cancel in the same way:

$$
\hbar\dot\theta_{\mathrm{pha}}+q\varphi\ \longmapsto\ \hbar\dot\theta_{\mathrm{pha}}+q\dot\Gamma+q\varphi-q\dot\Gamma=\hbar\dot\theta_{\mathrm{pha}}+q\varphi .
$$

**The two canceling pairs are the two terms that carry the time derivative.** In the action the first term shifts by $-q r^{2}\dot\Gamma$ and the potential-energy term by $+q r^{2}\dot\Gamma$, term for term and pointwise, so no boundary term is produced and no integration by parts is needed. **The truncated action is gauge invariant exactly**, and the parent's reading is the reason it must be: the gauge group translates one coordinate of the word and leaves the other seven, so a term built from the scale and the invariant combination of the phase cannot see it.

**The limit and the gauge transformation commute.** The deletion is the removal of a term built from the scale alone, so it removes a gauge invariant quantity. **Deleting and gauging in either order gives the same action**, and that is a one-line statement here and a computation in an equation-first account.

## What the Variational Route Adds

**Three things, and the third is the coupling's.**

*The order is a property of a term.* $\lvert\vec\nabla_\Phi r\rvert^{2}$ is order two for every field of the class, and that is a statement about the term and not about a solution. The companion has to argue the smallness of $Q$ from the field; here the term's power is exact.

*One deletion gives both equations.* No second truncation and no consistency check between the two halves: the variation of the survivor produces the eikonal and the transport, and the pairing is structural.

*The coupling's status is visible as a term count.* The three coupling pieces are of one order, so the coupling is leading. **In an equation-first account the same fact has to be argued from $\vec\pi$; here it is read off the table**, and a reader who wanted to expand in $q$ can see exactly why the table forbids it.

**What it does not add, and the list is short.**

*The size of the discarded term.* The action route says the term is order two and says nothing about where the approximation stops. That is the companion's table.

*The slow-connection hypothesis.* The action's leading term contains $\vec\nabla_\Phi S-q\vec A$, so a connection varying as fast as the phase makes the leading term vary as fast as the scale. The truncated action cannot see the condition, because it is a statement about the field's variation and not about a term. **No article in the corpus states it as a hypothesis**, and this one records the gap.

*The boundary terms.* The deletion changes the natural boundary condition on the scale: an action with $\lvert\vec\nabla_\Phi r\rvert^{2}$ needs a Neumann datum on it and the truncated one does not. The corpus states the limit on the whole of space and does not examine the boundary.

## Verification

**Both Euler–Lagrange systems were computed, with the term and without it.**

| variation | full action | truncated action |
|---|---|---|
| with respect to $r$ | covariant eikonal with $+\frac{\hbar^{2}}{m}\Delta_\Phi r$ | covariant eikonal alone |
| with respect to $\theta_{\mathrm{pha}}$ | $\partial_{t'}r^{2}+\vec\nabla_\Phi\cdot(r^{2}\vec\pi/m)=0$ | the same, identically |

**The second row was compared symbolically and is equal as written.** The deleted term carries neither $\theta_{\mathrm{pha}}$ nor $\vec A$, so the two derivatives of the Lagrangian with respect to the phase are the same expression, and no rearrangement is needed to see it.

**The first row was checked as a function of the potentials.** Keeping the term, the $r$-equation divided by $-2r$ is the companion's Hamilton–Jacobi equation with $Q=-\hbar^{2}\Delta_\Phi r/(2mr)$; deleting the term removes the divergence and leaves the bracket. The coefficients of $q\varphi$ and of $\lvert\vec A\rvert^{2}$ were checked against the parent's $+ϙ\varphi$ with $ϙ=-q$ and agree.

**The current was checked to be the conjugate momentum.** Differentiating the kinetic term with respect to $\vec\nabla_\Phi\theta_{\mathrm{pha}}$ returns $r^{2}\vec\pi$, and its Euler–Lagrange equation is the divergence of that current. The paramagnetic term is what makes the conjugate momentum the kinetic one and not the canonical one.

**What was not checked.** No boundary-value problem was solved and no flux was computed. The claims are about terms and identities, and both were verified as algebra.

## Summary

The parent's coupled action has five terms: the phase's rate times the density, the covariant kinetic energy split into free, paramagnetic and diamagnetic pieces, the potential energy times the density, and the scale's gradient squared. The parameter counts spatial derivatives of the scale, so every term but the last is order zero and the last is order two.

The limit is the deletion of that one term, and the deletion is a subtraction. Varying the scale of the truncated action gives the covariant Hamilton–Jacobi equation; varying the phase gives the covariant continuity equation, unchanged term for term. **One deletion changes one equation and leaves the other untouched**, in this family as in the free one.

The three coupling pieces are of one order, so the coupling is leading and there is no expansion in it. The paramagnetic piece is what makes the conjugate momentum the kinetic one, and dropping it would destroy the current's gauge invariance. The truncated action is gauge invariant exactly, and the deletion and the gauge transformation commute because the deleted term is built from the scale alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The parent's polar word |
| $r>0$ | The scale; the density is $r^{2}$ on the central field |
| $\theta_{\mathrm{pha}}$, $S=\hbar\theta_{\mathrm{pha}}$ | The central angle; the action |
| $\varepsilon e_{t}$ | The rotor on the central field |
| $\tilde A_\Phi=i(\varphi/c)e_{t}+\vec A$ | The connection |
| $q$; the parent's $ϙ=-q$ | The electric charge; the parent's coupling |
| $\vec\pi=\vec\nabla_\Phi S-q\vec A$ | Mechanical momentum; the conjugate momentum over $r^{2}$ |
| $S_{\mathrm{cpl}}$, $S_{\mathrm{cl}}$ | The parent's action; the truncated classical one |
| $\epsilon=1/(\pi_{\Phi}L)$ | The parameter; one power per derivative of the scale |
| $Q=-\hbar^{2}\Delta_\Phi r/(2mr)$ | Quantum potential; the deleted term's equation |

## Further Reading

- [The Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-schrodinger-equation-in-biquaternionic-polar-variables.html), the parent: the coupled Lagrangian, the three coupling pieces, and the gauge direction of the chart.
- [The Non-Quantum Limit and the Coupled Schrödinger Equation in Biquaternionic Polar Variables](the-non-quantum-limit-and-the-coupled-schrodinger-equation-in-biquaternionic-polar-variables.html), the companion: the same limit on the parent's pair, the Lorentz force, the vorticity and the circulation.
- [The Non-Quantum Limit, the Variational Principle and the Schrödinger Equation in Biquaternionic Polar Variables](the-non-quantum-limit-the-variational-principle-and-the-schrodinger-equation-in-biquaternionic-polar-variables.html), the free variational companion.
- [The Coupled Schrödinger Equation in Biquaternionic Polar Variables](the-coupled-schrodinger-equation-in-biquaternionic-polar-variables.html), for the covariant logarithmic derivative and the pair.
- [The Non-Quantum Limit of the Biquaternion Model](the-non-quantum-limit-of-the-biquaternion-model.html), for the parameter and the difference between the limit and the approximation.
