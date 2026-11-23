# __The Lagrangian and the Coupled Dirac Equation in the Non-Quantum Limit__

## Introduction
The limit in one sentence. The parent prints two actions — one for the operator setting, with gradient terms, and one boxed for the constant setting, without — and the difference is exactly the quantum potential's terms in the spin-half-fluid form, so the boxed action *is* the non-quantum action.

What the article establishes, in five sentences. The parent's boxed action is the operator-setting action with the frame's gradient terms deleted, and the deleted terms are the quantum potential's. The deletion leaves a constrained system whose seven momenta are zero or fixed, whose two evolution equations are the continuity equation and the guidance equation, and whose six remaining equations are the frame's constraints. The coupling enters the phase slot and the boost slot only, so the guidance equation is the mechanical mass shell and the density and the spin are untouched by it. The limit is therefore a truncation with a computable ledger: the deleted terms are gradient terms in three of the eight coordinates, and nothing else is dropped. The action does not derive the force; the force is read from the constraint surface and it is the equation-route companion's subject.

What is not new. The spin-half-fluid action with the frame's gradients, the constrained Hamiltonian reading, and the Madelung–Takabayasi correspondence are standard. Added here: the identification of the parent's boxed display with the non-quantum action, the ledger of what the limit deletes stated in coordinates, and the reading of the coupling's two-bracket reach as a statement about which quantities the limit may move.

The restriction. The word exists where $N(\tilde\Xi)\neq0$; the action is written in the eight real coordinates of the chart, and the limit is defined there.

The signs. The parent writes the coupling as $ϙ$ with $ϙ=-q$. The displays here keep the parent's letters and use $\vec\pi=\vec p-q\vec A$ and $\mathcal E=E-q\omicron_{\mathrm{pot}}$ when the mechanical variables are named.
## Conventions
The conventions are restated here so that every sign below is checkable from this page alone. Those of the coupled variational polar parent: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_{t}=1$ and $\vec e_{\imath}^{2}=-e_{t}$; $\mathrm{Sc}$ the coefficient of $e_{t}$; the complete polar decomposition $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$; $\rho_{\mathrm{num}}=\varrho^{2}\cosh\theta_{\mathrm{rpd}}$; $V(\theta_{\mathrm{rpd}},\vec u_{\mathrm b},\theta_{\mathrm{axr}},\vec u_{\mathrm r})$ the frame potential including the mass function $\mathcal V$; $\nu_m=\frac{mc}{h}$; $\epsilon=1/(\pi_{\Phi}L)$.
## The Action in the Non-Quantum Limit
The two displays, side by side, and their difference.

$$
S_{\mathrm{op}}=\int\mathrm{d}^{4}\varrho\;\Bigl[-\frac{h}{2\pi} c\,\rho_{\mathrm{num}}\,\partial_{r'_{t}}\theta_{\mathrm{pha}}-\rho_{\mathrm{num}} V-mc^{2}\varrho^{2}+\text{terms in }\vec\nabla_\Phi \varrho,\ \vec\nabla_\Phi\theta_{\mathrm{rpd}},\ \vec\nabla_\Phi\theta_{\mathrm{axr}}\Bigr],
$$

$$
S_{\mathrm{box}}=\int\mathrm{d}^{4}\varrho\;\Bigl[-\frac{h}{2\pi} c\,\rho_{\mathrm{num}}\,\partial_{r'_{t}}\theta_{\mathrm{pha}}-\rho_{\mathrm{num}} V-mc^{2}\varrho^{2}\Bigr],
\qquad
\rho_{\mathrm{num}}=\varrho^{2}\cosh\theta_{\mathrm{rpd}} .
$$

The parent states that the gradient terms are the quantum potential's, in the spin-half-fluid form, and that is the whole of the article's premise. **The boxed action is the operator-setting action with those terms deleted, and the deletion is the non-quantum limit.**

Why this family is different from the two scalar ones, and the difference is worth stating carefully. In the Klein–Gordon family the deleted term is the scale's kinetic term and it sits in the same display as the rest. Here the deleted terms are the frame's gradients and the parent keeps them in a separate display, so the two actions the limit relates are printed in the same article and the reader can see what the limit costs. No other family in the corpus has that.

The coupling's two brackets, and the type table that fixes them.

| bracket | type | temporal slot | what the potential does |
|---|---|---|---|
| scale | real central scalar | density | nothing |
| phase | central imaginary | guidance | shifts the momentum |
| boost | Hermitian | spatial slots | shifts the velocity |
| rotor | real vector part | none | nothing |

The potential is central and Hermitian, so it joins the phase bracket where the momentum is read and the boost bracket where the velocity is read; it cannot join the scale's, which is real central, and it cannot join the rotor's, which is a real vector part. The table says in advance which quantities the coupling can move and which it must leave alone.

The coupling in the one-form. The two displays above carry the free action's letters; with the connection present the phase's differential is the covariant one,
$$
\mathrm{d}\theta_{\mathrm{pha}}\ \longmapsto\ \mathrm{d}\theta_{\mathrm{pha}}-\frac{2\pi ϙ}{h}\tilde A_\Phi ,
$$
and that is the only change. The one-form's rotor term is untouched, because the connection is central and the rotor bracket is a real vector part.

What is deleted.

$$
\Delta S=-\int\mathrm{d}^{4}\varrho\;\bigl[\text{terms in }\vec\nabla_\Phi \varrho,\ \vec\nabla_\Phi\theta_{\mathrm{rpd}},\ \vec\nabla_\Phi\theta_{\mathrm{axr}}\bigr],
$$

three gradients and not eight: the phase's gradient is not among them, and neither are the rotor's angles, because those enter the one-form and not the potential.

The ledger.

| deleted | order | what it was |
|---|---|---|
| $\lvert\nabla \varrho\rvert^{2}$-type | $2$ | the density's curvature, the scalar quantum potential |
| $\lvert\nabla\theta_{\mathrm{rpd}}\rvert^{2}$-type | $2$ | the velocity field's curvature |
| $\lvert\nabla\theta_{\mathrm{axr}}\rvert^{2}$-type | $2$ | the spin field's curvature |

All three are order two and all three are quadratic in gradients, so the deletion removes the entire order-two content and nothing else. The limit's accuracy claim in this family is exactly "the deleted terms are the curvature of three fields", and it is visible in the parent's own two displays.

What survives. One term linear in the phase's rate, the frame potential, and the mass term. The surviving action is first order in the phase and algebraic in the frame, so its Euler–Lagrange equations are the guidance equation and the constraints.

The guidance equation in mechanical variables. Varying $\theta_{\mathrm{pha}}$ returns the continuity equation with $\vec v$ the kinetic velocity; varying the frame's angles returns the constraints; and the constraint surface evaluated with the coupling is the mechanical mass shell. The chain from the boxed action to the mechanical shell goes through the constraints and not through a second-order equation, and that is why this family's limit is a constraint-and-flow split.

### The Limits and the Truncation’s Error

It costs the spin's curvature and the velocity's curvature. The order-two terms deleted are the ones that would bend the density, the velocity field and the spin's frame. Their size is the free size: $\epsilon^{2}$ against the leading term, $\delta^{2}$ against the rest mass, because a curvature of a field varying on $L$ is $L^{-2}$.

It costs nothing of the coupling. The potential sits in the phase slot and the boost slot; the deleted terms are the gradients of the scale, the rapidity and the rotor angle. The two sets are disjoint, so the deletion leaves the coupling entire, as in every family.

It buys the constraint structure as an exact statement. The boxed action's equations are the frame's algebra and the guidance equation, and both are exact statements about the chart. A variational principle that kept the gradients could not state them without invoking the discarded terms.

It buys a comparison the corpus can make and does not make elsewhere. The two displays are printed in the same article, so the limit's ledger is not a reconstruction but an inspection. This is the only family in the corpus where that is so, and it is worth saying because the reader's natural question — what exactly does the limit throw away — has a printed answer here.

The constraints survive, and they are the limit's whole content. The truncated functional's variations give the mass-shell relation at the shifted frequency, the condition that fixes the frame's polarisation, and the vanishing of the three momenta that the polar word never gave a kinetic term. None of these is an approximation: they are the parent's conditions, and the limit is their statement.

The frame's transport survives. Varying the frame gives the transport that rotates the polarisation along the flow, with the connection inside the covariant bracket. It survives unchanged, because no frame block was touched — the article's whole point is that nothing was.

The charge and the spin survive. The phase's variation gives the charge and the frame's variation gives the spin density, with the connection entering only through the covariant derivative. Both expressions are the parent's, and the article's section on the charge and the spin is where they are displayed.

The gauge covariance survives. The parent action is gauge invariant and the limit touches no term, so the truncated functional is gauge invariant. The truncation cannot break the gauge symmetry, because there is no truncation; the section says so once and does not labour it.

What does not survive, and this is the honest part. Nothing is lost, and nothing is gained: **the limit does not select a class of solutions, because it is not an approximation to anything**. The article's claim is that the order-zero structure is exact, and that the "non-quantum" name describes an exact structure rather than a limit of one.

Why the family is worth its own article, then. Because the exact structure is not the classical point-particle theory: the frame is a dynamical variable, the spin is a density, and the transport is not a geodesic equation. The non-quantum limit of the Dirac family is the closest thing the corpus has to a classical spinning particle, and it is exact, which is why the family's three articles each end with what survives rather than with what is lost.

## The Variation
Seven momenta and two evolution equations, from one variation. The boxed action is first order in seven of the eight coordinates: it contains $\partial_{r'_t}\theta_{\mathrm{pha}}$ and no other rate. Varying it with respect to the coordinates gives two kinds of equation. The seven coordinates whose rates are absent give

$$
p_x=A_x(q)=0 \ \text{or fixed},
$$

the momenta read off the one-form; the phase gives the one non-trivial momentum,

$$
p_{\theta_{\mathrm{pha}}}=-\frac{h}{2\pi} c\,\rho_{\mathrm{num}},
$$

and the Euler–Lagrange equation of the density and of the guidance angle gives the two evolution equations the next section counts.

The boundary term is absent. A first-order action has no second derivative to integrate by parts, so the variation produces no surface term and no boundary condition. That is why the limit's variational principle is a set of first-order transport equations and not a boundary-value problem, and it is the single largest difference between this family and the two scalar ones.

The equation is recovered, not assumed. The two evolution equations are the Euler–Lagrange equations of the boxed display, and the six remaining equations are the vanishing momenta. Both statements are read off the variation and neither is imported from the parent.
## The Constraints the Action Imposes: The Structure
Seven momenta and two evolution equations. Of the eight conjugate momenta, seven vanish or are fixed functions of the coordinates; two Euler–Lagrange equations carry time derivatives, the continuity equation for $\rho_{\mathrm{num}}$ and the guidance equation; and six equations are constraints on the frame's variables.

No multiplier is introduced, and the parent states the distinction. The parameterisation is exact, so the unit conditions of the boost and the rotor hold identically and no Lagrange multiplier is needed for them. **The absence of multipliers is not the absence of constraints**: the six constraints are Euler–Lagrange equations of the chart, and the parent's sharpest technical point is that a parameterisation can remove the multipliers while leaving the constraints.

What the constraints are in the limit's language. They are the frame's algebra: the rapidity, the boost's axis and the rotor's three angles are determined by the coordinates they are conjugate to. Order zero's polarisation is this algebra, seen from the action rather than from the equation.
## The Structural Consequence: The Coupling's Reach
One potential, two brackets. The potential is one element of $\mathbb{B}_\Phi$ with a temporal slot and a spatial vector slot, so it joins the phase bracket's temporal slot and the boost bracket's spatial slots. No second rule is needed, and the parent's statement that no sign can be chosen independently follows from the slots.

What it cannot reach, and the reason is type. The scale bracket is a real central scalar and the potential is not; the rotor bracket is a real vector part and the potential is central. **So the density and the spin direction are exactly invariant**, and that is a statement of the polar form and not of the physics: the potential does not change the density at a point and does not rotate the spin's axis.

What follows for the limit's statements, in advance of any computation. Order zero's polarisation condition is unaffected by the coupling; order one's density law is unaffected except through the velocity it carries; order one's velocity law is the one the coupling rewrites; order one's spin law is unaffected directly. The table is a prediction of the limit's structure, and the equation-route companion confirms each entry.
## The Noether Currents: The Charge and the Spin in the Limit
The charge is the density, and the coupling does not touch it. The phase's momentum is $-\frac{h}{2\pi} c\,\rho_{\mathrm{num}}$, so the particle density is $\rho_{\mathrm{num}}=\varrho^{2}\cosh\theta_{\mathrm{rpd}}$ and the charge density is $q\rho_{\mathrm{num}}$, with $q=-ϙ$ the parent's charge. The current is $\rho_{\mathrm{num}}\vec v$ with $\vec v$ the transport velocity of the guidance equation, and the continuity equation of the limit is the conservation of this current.

The spin current, unchanged. The rotor's bracket is a real vector part and the connection is central, so the spin current is the free one: the rotor's conjugate momentum $-\frac{h}{2\pi} c\,\varrho^{2}\sinh\theta_{\mathrm{rpd}}\,\hat n_{\mathrm{rot}}$, transported by the same flow. The statement is exact and not an approximation of the limit: it is exact in the parent and the limit does not touch it.

What the mass term does. It removes the phase from the dynamics of the density and puts it into the guidance equation, so that the charge is conserved without the mass appearing in its conservation law. The energy carries the mass; the charge does not. That split is the limit's form of the element article's *The Charge Has No Mass and the Energy Has Mass-Squared*, and it is the reason the two currents are computed separately here.
## What the Principle Adds and What It Relabels: What the Route Does Not Do
It does not derive the force. The parent says so: the type table says where the potential acts and not what the resulting motion is. The force is read from the gradient of the mass shell, which is the equation-route companion's computation.

It does not settle the constraint algebra. Whether the six constraints are first class or second class is the parent's central open question, and the limit inherits it. Until it is settled, the statement that the constrained flow is the coupled equation's flow is a conjecture, and the parent names it.

It does not produce a second current. The action has one symmetry and the word has two flows; the limit inherits the mismatch and does not resolve it.

It does not make the anomalous moment appear. The rotor's bracket is unreachable by the coupling, so the boxed action has no slot for a moment that rotates the spin independently of the boost. The deletion cannot create one, and the article records the absence rather than importing it.
## Summary
The parent prints two actions: one for the operator setting with the frame's gradient terms and one boxed without them. The boxed action is the non-quantum action, because the deleted terms are the quantum potential's in the spin-half-fluid form.

The deletion removes three quadratic gradient terms and nothing else: the curvature of the density, of the rapidity and of the rotor's angle. All three are order two, and their size is the free size, so the limit costs the free accuracy and no more.

The coupling enters the phase bracket and the boost bracket and no others, because the potential is central imaginary and Hermitian while the scale bracket is real central and the rotor bracket is a real vector part. The table predicts, before any computation, that the density and the spin are untouched at a point and that the momentum and the velocity are rewritten, and the equation-route companion confirms it.

The surviving system is a constrained one: seven momenta zero or fixed, two evolution equations, six constraints, and no multipliers because the parameterisation is exact. **The limit is a constraint-and-flow split, and its ledger is printed rather than reconstructed.**
## Summary of Notation
| Symbol | Meaning |
|---|---|
| $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The polar word; defined where $N(\tilde\Xi)\neq0$ |
| $\rho_{\mathrm{num}}=\varrho^{2}\cosh\theta_{\mathrm{rpd}}$ | The density in the constant setting |
| $V(\theta_{\mathrm{rpd}},\vec u_{\mathrm b},\theta_{\mathrm{axr}},\vec u_{\mathrm r})$ | The frame potential, including the mass function $\mathcal V$ |
| $S_{\mathrm{op}}$, $S_{\mathrm{box}}$ | The operator-setting action; the boxed constant-setting action |
| $\vec\nabla_\Phi \varrho,\ \vec\nabla_\Phi\theta_{\mathrm{rpd}},\ \vec\nabla_\Phi\theta_{\mathrm{axr}}$ | The three gradients the limit deletes |
| $\tilde A_\Phi=i(\omicron_{\mathrm{pot}}/c)e_{t}+\vec A$ | The connection; $q$ its charge, the parent's $ϙ=-q$ |
| $\vec\pi=\vec p-q\vec A$, $\mathcal E=E-q\omicron_{\mathrm{pot}}$ | Mechanical momentum and energy |
| $\epsilon=1/(\pi_{\Phi}L)$, $\delta=1/(2\pi\nu_mL)$ | The two parameters of the deleted terms' size |
## Further Reading
- [The Lagrangian and the Coupled Dirac Equation in Polar Variables](the-lagrangian-and-the-coupled-dirac-equation-in-polar-variables.html), the parent: the two actions, the type table, the constraint count and the reconstruction conjecture.
- [The Coupled Dirac Equation in the Non-Quantum Limit](the-coupled-dirac-equation-in-the-non-quantum-limit.html), the companion: the one addition to the wavevector, the kinetic frame and the three laws.
- [The Lagrangian and the Dirac Equation in the Non-Quantum Limit](the-lagrangian-and-the-dirac-equation-in-the-non-quantum-limit.html), the free companion, where the same constraint reading applies without a potential.
- [The Lagrangian and the Coupled Klein–Gordon Equation in the Non-Quantum Limit](the-lagrangian-and-the-coupled-klein-gordon-equation-in-the-non-quantum-limit.html), the scalar companion, where the deleted term is the scale's kinetic term.
- [The Non-Quantum Limit of the Biquaternion Model](the-non-quantum-limit-of-the-biquaternion-model.html), for the parameter and the difference between the limit and the approximation.
## Verification
The two displays were compared term by term. The boxed action and the operator-setting action differ by the bracket in $\vec\nabla_\Phi \varrho$, $\vec\nabla_\Phi\theta_{\mathrm{rpd}}$ and $\vec\nabla_\Phi\theta_{\mathrm{axr}}$, and by nothing else: the phase term, the frame potential and the mass term are identical in both. The comparison is an inspection of the parent's own text.

The momentum count was checked against the coordinates. One velocity, the phase's, appears linearly in the boxed action, so seven momenta vanish or are fixed and one is the coefficient of the phase's rate. The count matches the parent's statement of seven and two.

The type table was checked against the brackets' definitions. The potential is central imaginary in its temporal slot and Hermitian in its spatial slots, so it can join the phase and boost brackets and cannot join the scale or rotor brackets. **The exclusion is by type and is exact.**

The mass shell was checked to follow from the constraints. With the coupling in the phase slot, the guidance equation's constraint surface is $\mathcal E^{2}/c^{2}-\lvert\vec\pi\rvert^{2}=m^{2}c^{2}$, which is the equation-route companion's order zero. The two routes agree term for term.

What was not checked. No constraint algebra was computed, no flow of the constrained system was integrated, and the reconstruction conjecture was not tested. The claims are about the two displays, the count, and the types, and all three were verified.
