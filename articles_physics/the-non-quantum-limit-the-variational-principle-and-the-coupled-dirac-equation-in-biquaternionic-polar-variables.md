# __The Non-Quantum Limit, the Variational Principle and the Coupled Dirac Equation in Biquaternionic Polar Variables__

## Introduction

**The limit in one sentence.** The parent prints two actions — one for the operator setting, with gradient terms, and one boxed for the constant setting, without — and the difference is exactly the quantum potential's terms in the spin-half-fluid form, so the boxed action *is* the non-quantum action.

**The two displays, side by side, and their difference.**

$$
S_{\mathrm{op}}=\int\mathrm{d}^{4}\varrho\;\Bigl[-\hbar c\,\rho_{\mathrm{num}}\,\partial_{r'_{t}}\theta_{\mathrm{pha}}-\rho_{\mathrm{num}} V-mc^{2}\varrho^{2}+\text{terms in }\vec\nabla_\Phi \varrho,\ \vec\nabla_\Phi\theta_{\mathrm{rpd}},\ \vec\nabla_\Phi\theta_{\mathrm{axr}}\Bigr],
$$

$$
S_{\mathrm{box}}=\int\mathrm{d}^{4}\varrho\;\Bigl[-\hbar c\,\rho_{\mathrm{num}}\,\partial_{r'_{t}}\theta_{\mathrm{pha}}-\rho_{\mathrm{num}} V-mc^{2}\varrho^{2}\Bigr],
\qquad
\rho_{\mathrm{num}}=\varrho^{2}\cosh\theta_{\mathrm{rpd}} .
$$

**The parent states that the gradient terms are the quantum potential's**, in the spin-half-fluid form, and that is the whole of the article's premise. **The boxed action is the operator-setting action with those terms deleted, and the deletion is the non-quantum limit.**

**Why this family is different from the two scalar ones, and the difference is worth stating carefully.** In the Klein–Gordon family the deleted term is the scale's kinetic term and it sits in the same display as the rest. **Here the deleted terms are the frame's gradients and the parent keeps them in a separate display**, so the two actions the limit relates are printed in the same article and the reader can see what the limit costs. **No other family in the corpus has that.**

**The coupling's two brackets, and the type table that fixes them.**

| bracket | type | temporal slot | what the potential does |
|---|---|---|---|
| scale | real central scalar | density | nothing |
| phase | central imaginary | guidance | shifts the momentum |
| boost | Hermitian | spatial slots | shifts the velocity |
| rotor | real vector part | none | nothing |

**Two of four, and the two are the momentum and the velocity.** The potential is central and Hermitian, so it joins the phase bracket where the momentum is read and the boost bracket where the velocity is read; it cannot join the scale's, which is real central, and it cannot join the rotor's, which is a real vector part. **The table says in advance which quantities the coupling can move and which it must leave alone.**

**What the article establishes, in five sentences.** The parent's boxed action is the operator-setting action with the frame's gradient terms deleted, and the deleted terms are the quantum potential's. The deletion leaves a constrained system whose seven momenta are zero or fixed, whose two evolution equations are the continuity equation and the guidance equation, and whose six remaining equations are the frame's constraints. The coupling enters the phase slot and the boost slot only, so the guidance equation is the mechanical mass shell and the density and the spin are untouched by it. The limit is therefore a truncation with a computable ledger: the deleted terms are gradient terms in three of the eight coordinates, and nothing else is dropped. The action does not derive the force; the force is read from the constraint surface and it is the equation-route companion's subject.

**What is not new.** The spin-half-fluid action with the frame's gradients, the constrained Hamiltonian reading, and the Madelung–Takabayasi correspondence are standard. Added here: the identification of the parent's boxed display with the non-quantum action, the ledger of what the limit deletes stated in coordinates, and the reading of the coupling's two-bracket reach as a statement about which quantities the limit may move.

**The restriction.** The word exists where $N(\tilde\Xi)\neq0$; the action is written in the eight real coordinates of the chart, and the limit is defined there.

**The signs.** The parent writes the coupling as $ϙ$ with $ϙ=-q$. The displays here keep the parent's letters and use $\vec\pi=\vec p-q\vec A$ and $\mathcal E=E-q\varphi$ when the mechanical variables are named.

**Conventions.** Those of the coupled variational polar parent: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_{t}=1$ and $\vec e_\mu^{2}=-e_{t}$; $\mathrm{Sc}$ the coefficient of $e_{t}$; the complete polar decomposition $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$; $\rho_{\mathrm{num}}=\varrho^{2}\cosh\theta_{\mathrm{rpd}}$; $V(\theta_{\mathrm{rpd}},\vec u_{\mathrm b},\theta_{\mathrm{axr}},\vec u_{\mathrm r})$ the frame potential including the mass function $\mathcal V$; $k_m=mc/\hbar$; $\epsilon=1/(\pi_{\Phi}L)$.

## The Coupling's Reach

**One potential, two brackets.** The potential is one element of $\mathbb{B}_\Phi$ with a temporal slot and a spatial vector slot, so it joins the phase bracket's temporal slot and the boost bracket's spatial slots. **No second rule is needed**, and the parent's statement that no sign can be chosen independently follows from the slots.

**What it cannot reach, and the reason is type.** The scale bracket is a real central scalar and the potential is not; the rotor bracket is a real vector part and the potential is central. **So the density and the spin direction are exactly invariant**, and that is a statement of the polar form and not of the physics: the potential does not change the density at a point and does not rotate the spin's axis.

**What follows for the limit's statements, in advance of any computation.** Order zero's polarisation condition is unaffected by the coupling; order one's density law is unaffected except through the velocity it carries; order one's velocity law is the one the coupling rewrites; order one's spin law is unaffected directly. **The table is a prediction of the limit's structure**, and the equation-route companion confirms each entry.

## The Constraint Structure

**Seven momenta and two evolution equations.** Of the eight conjugate momenta, seven vanish or are fixed functions of the coordinates; two Euler–Lagrange equations carry time derivatives, the continuity equation for $\rho_{\mathrm{num}}$ and the guidance equation; and six equations are constraints on the frame's variables.

**No multiplier is introduced, and the parent states the distinction.** The parameterisation is exact, so the unit conditions of the boost and the rotor hold identically and no Lagrange multiplier is needed for them. **The absence of multipliers is not the absence of constraints**: the six constraints are Euler–Lagrange equations of the chart, and the parent's sharpest technical point is that a parameterisation can remove the multipliers while leaving the constraints.

**What the constraints are in the limit's language.** They are the frame's algebra: the rapidity, the boost's axis and the rotor's three angles are determined by the coordinates they are conjugate to. **Order zero's polarisation is this algebra**, seen from the action rather than from the equation.

## The Deletion, Stated in Coordinates

**What is deleted.**

$$
\Delta S=-\int\mathrm{d}^{4}\varrho\;\bigl[\text{terms in }\vec\nabla_\Phi \varrho,\ \vec\nabla_\Phi\theta_{\mathrm{rpd}},\ \vec\nabla_\Phi\theta_{\mathrm{axr}}\bigr],
$$

three gradients and not eight: the phase's gradient is not among them, and neither are the rotor's angles, because those enter the one-form and not the potential.

**The ledger.**

| deleted | order | what it was |
|---|---|---|
| $\lvert\nabla \varrho\rvert^{2}$-type | $2$ | the density's curvature, the scalar quantum potential |
| $\lvert\nabla\theta_{\mathrm{rpd}}\rvert^{2}$-type | $2$ | the velocity field's curvature |
| $\lvert\nabla\theta_{\mathrm{axr}}\rvert^{2}$-type | $2$ | the spin field's curvature |

**All three are order two and all three are quadratic in gradients**, so the deletion removes the entire order-two content and nothing else. **The limit's accuracy claim in this family is exactly "the deleted terms are the curvature of three fields"**, and it is visible in the parent's own two displays.

**What survives.** One term linear in the phase's rate, the frame potential, and the mass term. **The surviving action is first order in the phase and algebraic in the frame**, so its Euler–Lagrange equations are the guidance equation and the constraints.

**The guidance equation in mechanical variables.** Varying $\theta_{\mathrm{pha}}$ returns the continuity equation with $\vec v$ the kinetic velocity; varying the frame's angles returns the constraints; and the constraint surface evaluated with the coupling is the mechanical mass shell. **The chain from the boxed action to the mechanical shell goes through the constraints and not through a second-order equation**, and that is why this family's limit is a constraint-and-flow split.

## What the Deletion Costs and What It Buys

**It costs the spin's curvature and the velocity's curvature.** The order-two terms deleted are the ones that would bend the density, the velocity field and the spin's frame. **Their size is the free size**: $\epsilon^{2}$ against the leading term, $\delta^{2}$ against the rest mass, because a curvature of a field varying on $L$ is $L^{-2}$.

**It costs nothing of the coupling.** The potential sits in the phase slot and the boost slot; the deleted terms are the gradients of the scale, the rapidity and the rotor angle. **The two sets are disjoint**, so the deletion leaves the coupling entire, as in every family.

**It buys the constraint structure as an exact statement.** The boxed action's equations are the frame's algebra and the guidance equation, and both are exact statements about the chart. **A variational principle that kept the gradients could not state them without invoking the discarded terms.**

**It buys a comparison the corpus can make and does not make elsewhere.** The two displays are printed in the same article, so the limit's ledger is not a reconstruction but an inspection. **This is the only family in the corpus where that is so**, and it is worth saying because the reader's natural question — what exactly does the limit throw away — has a printed answer here.

## What the Variational Route Does Not Do

**It does not derive the force.** The parent says so: the type table says where the potential acts and not what the resulting motion is. The force is read from the gradient of the mass shell, which is the equation-route companion's computation.

**It does not settle the constraint algebra.** Whether the six constraints are first class or second class is the parent's central open question, and the limit inherits it. **Until it is settled, the statement that the constrained flow is the coupled equation's flow is a conjecture**, and the parent names it.

**It does not produce a second current.** The action has one symmetry and the word has two flows; the limit inherits the mismatch and does not resolve it.

**It does not make the anomalous moment appear.** The rotor's bracket is unreachable by the coupling, so the boxed action has no slot for a moment that rotates the spin independently of the boost. **The deletion cannot create one**, and the article records the absence rather than importing it.

## Verification

**The two displays were compared term by term.** The boxed action and the operator-setting action differ by the bracket in $\vec\nabla_\Phi \varrho$, $\vec\nabla_\Phi\theta_{\mathrm{rpd}}$ and $\vec\nabla_\Phi\theta_{\mathrm{axr}}$, and by nothing else: the phase term, the frame potential and the mass term are identical in both. **The comparison is an inspection of the parent's own text.**

**The momentum count was checked against the coordinates.** One velocity, the phase's, appears linearly in the boxed action, so seven momenta vanish or are fixed and one is the coefficient of the phase's rate. **The count matches the parent's statement of seven and two.**

**The type table was checked against the brackets' definitions.** The potential is central imaginary in its temporal slot and Hermitian in its spatial slots, so it can join the phase and boost brackets and cannot join the scale or rotor brackets. **The exclusion is by type and is exact.**

**The mass shell was checked to follow from the constraints.** With the coupling in the phase slot, the guidance equation's constraint surface is $\mathcal E^{2}/c^{2}-\lvert\vec\pi\rvert^{2}=m^{2}c^{2}$, which is the equation-route companion's order zero. **The two routes agree term for term.**

**What was not checked.** No constraint algebra was computed, no flow of the constrained system was integrated, and the reconstruction conjecture was not tested. The claims are about the two displays, the count, and the types, and all three were verified.

## Summary

The parent prints two actions: one for the operator setting with the frame's gradient terms and one boxed without them. **The boxed action is the non-quantum action**, because the deleted terms are the quantum potential's in the spin-half-fluid form.

The deletion removes three quadratic gradient terms and nothing else: the curvature of the density, of the rapidity and of the rotor's angle. **All three are order two**, and their size is the free size, so the limit costs the free accuracy and no more.

The coupling enters the phase bracket and the boost bracket and no others, because the potential is central imaginary and Hermitian while the scale bracket is real central and the rotor bracket is a real vector part. **The table predicts, before any computation, that the density and the spin are untouched at a point and that the momentum and the velocity are rewritten**, and the equation-route companion confirms it.

The surviving system is a constrained one: seven momenta zero or fixed, two evolution equations, six constraints, and no multipliers because the parameterisation is exact. **The limit is a constraint-and-flow split, and its ledger is printed rather than reconstructed.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The polar word; defined where $N(\tilde\Xi)\neq0$ |
| $\rho_{\mathrm{num}}=\varrho^{2}\cosh\theta_{\mathrm{rpd}}$ | The density in the constant setting |
| $V(\theta_{\mathrm{rpd}},\vec u_{\mathrm b},\theta_{\mathrm{axr}},\vec u_{\mathrm r})$ | The frame potential, including the mass function $\mathcal V$ |
| $S_{\mathrm{op}}$, $S_{\mathrm{box}}$ | The operator-setting action; the boxed constant-setting action |
| $\vec\nabla_\Phi \varrho,\ \vec\nabla_\Phi\theta_{\mathrm{rpd}},\ \vec\nabla_\Phi\theta_{\mathrm{axr}}$ | The three gradients the limit deletes |
| $\tilde A_\Phi=i(\varphi/c)e_{t}+\vec A$ | The connection; $q$ its charge, the parent's $ϙ=-q$ |
| $\vec\pi=\vec p-q\vec A$, $\mathcal E=E-q\varphi$ | Mechanical momentum and energy |
| $\epsilon=1/(\pi_{\Phi}L)$, $\delta=1/(k_mL)$ | The two parameters of the deleted terms' size |

## Further Reading

- [The Variational Principle and the Coupled Dirac Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), the parent: the two actions, the type table, the constraint count and the reconstruction conjecture.
- [The Non-Quantum Limit and the Coupled Dirac Equation in Biquaternionic Polar Variables](the-non-quantum-limit-and-the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), the companion: the one addition to the wavevector, the kinetic frame and the three laws.
- [The Non-Quantum Limit, the Variational Principle and the Dirac Equation in Biquaternionic Polar Variables](the-non-quantum-limit-the-variational-principle-and-the-dirac-equation-in-biquaternionic-polar-variables.html), the free companion, where the same constraint reading applies without a potential.
- [The Non-Quantum Limit, the Variational Principle and the Coupled Klein–Gordon Equation in Biquaternionic Polar Variables](the-non-quantum-limit-the-variational-principle-and-the-coupled-klein-gordon-equation-in-biquaternionic-polar-variables.html), the scalar companion, where the deleted term is the scale's kinetic term.
- [The Non-Quantum Limit of the Biquaternion Model](the-non-quantum-limit-of-the-biquaternion-model.html), for the parameter and the difference between the limit and the approximation.
