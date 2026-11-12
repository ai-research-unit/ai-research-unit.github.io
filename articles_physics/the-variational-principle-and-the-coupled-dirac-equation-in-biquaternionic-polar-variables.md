# __The Variational Principle and the Coupled Dirac Equation in Biquaternionic Polar Variables__

## Introduction

This article substitutes the polar word into the coupled action of *The Variational Principle and the Coupled Dirac Equation in Biquaternionic Form* and reads what the substitution gives. It is the fourth member of the coupled quartet: the element equation, the polar equation, the element action, and this one.

**The substitution.** The word

$$
\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r}
$$

is a bijection onto the N-regular set, with $r>0$, $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$, $\theta_{\mathrm{rpd}}\ge0$, $\theta_{\mathrm{axr}}\in[0,2\pi)$. The action is a functional of the pair $(\tilde\Xi_L,\tilde\Xi_R)$; the word is one word for the whole element; and the substitution is therefore a change of variables on the functional and not a new functional. **That much is bookkeeping, and this article says so at the start.**

**What is not bookkeeping.** A change of variables can be invertible on the fields and still change what the variation *does*, because the action's derivatives are taken before the substitution. Substitute a word with eight parameters into a first-order functional and the functional becomes first order in eight parameters — and first order in eight parameters is a **constrained system**. Some of the eight velocities do not appear. Some of the eight conjugate momenta vanish identically. The Euler–Lagrange equations are then not eight evolution equations; they are two evolution equations and six constraints, and a variational principle of that shape requires a constraint analysis before its content can be read.

**Three things are established.**

*First, the action in the word.* The kinetic term becomes the phase's term and nothing else: the scale, the boost and the rotor contribute to it only through the density, and the density is a canonical function of the parameters. The potential term becomes the potential as a function of the six non-scale, non-phase parameters. The action is

$$
S=\int\mathrm{d}^{4}r\;\Bigl[-\hbar c\,\rho\,\partial_{r'_t}\theta_{\mathrm{pha}}-\rho\,V\Bigr]
$$

with $\rho=r^{2}\cosh\theta_{\mathrm{rpd}}$ and $V$ the potential's scalar part in the frame, and it carries no velocity for any parameter other than the phase.

*Second, the constraint structure.* Six of the eight Euler–Lagrange equations contain no time derivative and are constraints on the parameters; the two that do are the evolution of $r$ and of $\theta_{\mathrm{pha}}$. The constraints are not optional and they are not multipliers: the parameterisation is exact, so no Lagrange multiplier is needed for the unit conditions, and the constraints are *equations of motion* of the constrained system. Getting this distinction right is the article's main technical point.

*Third, the honest limit.* Whether the constrained system's solutions are the coupled pair's solutions is **not established here**. The equivalence is formal — the word is a bijection, so the variation of the action in the eight parameters and the variation in the element are the same variation — but the *flow* that the constrained system generates has not been shown to be the pair's flow. That is the article's open question and it is stated as such, not concealed.

**The two settings.** The connection is taken constant, with constant coefficients, because that is the setting in which the parameters are coordinates on a fixed frame. In the operator setting the word's rapidity and rotor angle become fields and the action acquires gradient terms for them; the structure is the standard one of the quantum hydrodynamics of a spin fluid, and the article states it in §*The Operator Setting* without deriving it.

## The Action in the Word

Substituting the word into the coupled action is a computation in three parts: the kinetic terms, the mass terms and the potential. The first two are the parent polar article's and the third is the coupling's.

**The kinetic terms.** The parent's identity is

$$
\mathrm{Sc}\Bigl[\tilde\Xi_L^{*}\tilde\nabla_\Phi^{\natural}\tilde\Xi_L+\tilde\Xi_R^{*}\tilde\nabla_\Phi\tilde\Xi_R\Bigr]
=\tilde\Xi\text{-bilinear}\;\Longrightarrow\;
-\rho\,\partial_{r'_t}\theta_{\mathrm{pha}}+\text{a total divergence},
$$

and its content is a statement about types. Differentiate the word, divide by it, and the four brackets appear: the scale bracket, the phase bracket, the boost bracket and the rotor bracket. The pairing takes the scalar part, and the scalar part of a product of brackets vanishes unless the types match. The scale bracket is a real scalar and contributes with the phase bracket's central imaginary part; the boost bracket is Hermitian and the rotor bracket is a real vector, and the two of them pair with each other. What survives the temporal slot is the phase's derivative times the density, and the rest is a divergence.

**The statement, in the chart's letters.**

$$
\frac{\hbar c}{2}\int\mathrm{d}^{4}r\;\mathrm{Re}\,\mathrm{Sc}\Bigl[\tilde\Xi_L^{*}\tilde\nabla_\Phi^{\natural}\tilde\Xi_L+\tilde\Xi_R^{*}\tilde\nabla_\Phi\tilde\Xi_R\Bigr]
=-\hbar c\int\mathrm{d}^{4}r\;\rho\,\partial_{r'_t}\theta_{\mathrm{pha}}+\text{boundary},
$$

with $\rho=r^{2}\cosh\theta_{\mathrm{rpd}}$. **The coefficient is $\cosh\theta_{\mathrm{rpd}}$ and not one**, and the reason is the one the element article's Noether current already gives: the density of this field is not $r^{2}$ but $r^{2}\cosh\theta_{\mathrm{rpd}}$, because the four-velocity's temporal slot is $\cosh\theta_{\mathrm{rpd}}$ and the density is the temporal slot of the current. The boost's rapidity is therefore in the kinetic term, and the article writes it out rather than absorbing it, because the absorption would hide the only place where the boost enters the action.

**Why the rotor contributes nothing to the kinetic term.** The rotor's bracket is a real vector and its only partner in the scalar part is the boost bracket, which is Hermitian; the product of a Hermitian and a real vector is a material-sector element whose scalar part vanishes in the temporal slot. The rotor's dynamics therefore enters the action only through the potential term's dependence on $\theta_{\mathrm{axr}}$, and that is a fact about the pairing and not a choice.

**The mass terms.** The mass term is $\tilde\Xi_L^{*}\tilde\Xi_R+\tilde\Xi_R^{*}\tilde\Xi_L$, and in the chart it is a function of the parameters with no derivative. The parent polar article's mass-term proposition gives the relation between the parts, $\tilde\Xi_0^{L}=-\mathcal B_\Psi\tilde\Xi_0^{R}$ with $\mathcal B_\Psi=\tilde U_{\Psi,\mathrm b}^{-2}$, and the scalar part of the mass term is therefore a fixed multiple of $r^{2}$. The mass enters the action as an algebraic term and never as a velocity; that is the reason the action has one velocity and not four.

**The potential.** The coupling replaces $\tilde\nabla_\Phi$ by $\tilde\nabla_{\mathrm{gco}}$, and because $\tilde A_\Phi$ is central per component it passes through $\tilde\Xi^{-1}$:

$$
\tilde\Xi^{-1}\tilde\nabla_{\mathrm{gco}}\tilde\Xi=\tilde\Xi^{-1}\tilde\nabla_\Phi\tilde\Xi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi .
$$

So the potential adds one algebraic term and no derivative, and the action's potential term is

$$
-\rho\,V,\qquad
V=\text{the scalar part of the frame's image of }\tfrac{ϙ}{\hbar}\tilde A_\Phi,
$$

with $V$ a real function of $\theta_{\mathrm{rpd}}$, $\vec u_{\mathrm b}$, $\theta_{\mathrm{axr}}$ and $\vec u_{\mathrm r}$ and independent of $r$ and $\theta_{\mathrm{pha}}$. **The independence of $r$ is what makes the scale's momentum vanish** and it is §*The Constraint Structure*'s first fact.

**Which slots of the potential reach which bracket.** Decompose as in the polar companion: the temporal slot $\frac{iϙ}{\hbar}A_t$ is central imaginary, the spatial slots $\frac{iϙ}{\hbar}A_\eta\vec e_\eta$ are Hermitian. The potential therefore adds to the *phase bracket* and to the *boost bracket*, and it cannot reach the scale bracket or the rotor bracket. In the action that shows up as the structure of $V$: it depends on the boost's rapidity and axis through the Hermitian slot, and it depends on $\theta_{\mathrm{pha}}$ not at all.

**The action, written once.**

$$
\boxed{\;S=\int\mathrm{d}^{4}r\;\Bigl[-\hbar c\,\rho\,\partial_{r'_t}\theta_{\mathrm{pha}}-\rho\,V(\theta_{\mathrm{rpd}},\vec u_{\mathrm b},\theta_{\mathrm{axr}},\vec u_{\mathrm r})-m c^{2}\,r^{2}\Bigr]\;}
$$

with $\rho=r^{2}\cosh\theta_{\mathrm{rpd}}$. The third term is the mass's, written in the chart's letters; the second is the potential's; the first is the only term with a velocity.

**One caution about the first term's coefficient.** The coefficient $\hbar c\rho$ contains the rapidity, so the action is *not* linear in the velocities in the naive sense: $\rho$ depends on $\theta_{\mathrm{rpd}}$, and $\theta_{\mathrm{rpd}}$ is one of the parameters whose velocity does not appear. The action is linear in $\partial_{r'_t}\theta_{\mathrm{pha}}$ with a coefficient that depends on a coordinate. That is the standard shape of a first-order constrained system and it is the reason the Dirac analysis is needed rather than a Legendre transform.

## The Constraint Structure

The action is first order in eight parameters, one of which has its velocity in the action. That single fact fixes the whole constraint structure.

**The conjugate momenta.** With $\mathcal{L}$ the integrand,

$$
\pi_{r}=\frac{\partial\mathcal{L}}{\partial(\partial_{r'_t}r)}=0,
\qquad
\pi_{\theta_{\mathrm{pha}}}=-\hbar c\,\rho,
\qquad
\pi_{\theta_{\mathrm{rpd}}}=\pi_{\theta_{\mathrm{axr}}}=\pi_{u_{\mathrm b}}=\pi_{u_{\mathrm r}}=0 .
$$

**Seven of the eight momenta either vanish or are fixed functions of the coordinates.** Only $\pi_{\theta_{\mathrm{pha}}}$ is a genuine momentum, and even it is not independent: it is $-\hbar c\rho$, a function of $r$ and $\theta_{\mathrm{rpd}}$.

**The count.** Eight parameters, eight Euler–Lagrange equations, of which two carry a time derivative — the equation of $r$ and the equation of $\theta_{\mathrm{pha}}$ — and six do not. The six without a time derivative are **constraints**, and their number is the number of parameters whose velocity the action does not contain.

**The constraint equations.** Varying the six parameters whose velocities are absent gives

$$
\frac{\partial}{\partial p}\bigl(\rho V\bigr)=0
\qquad\text{for}\qquad p\in\{\theta_{\mathrm{rpd}},\vec u_{\mathrm b},\theta_{\mathrm{axr}},\vec u_{\mathrm r}\},
$$

which is six equations on six parameters because the two axes are unit vectors and are counted with their own conditions. The content is that the potential's frame-dependence must be stationary: the frame sits where the potential is extremal in the frame variables.

**The two evolution equations.** Varying $r$ and $\theta_{\mathrm{pha}}$ gives

$$
-\hbar c\cosh\theta_{\mathrm{rpd}}\,\partial_{r'_t}\theta_{\mathrm{pha}}-V-mc^{2}=0,
\qquad
\partial_{r'_t}\bigl(r^{2}\cosh\theta_{\mathrm{rpd}}\bigr)=0 .
$$

The second is the continuity equation with the density $\rho$; the first is the guidance equation with the potential and the mass added. In the chart's letters these are the Madelung pair with a boost factor, and the boost factor is the density's.

**No Lagrange multipliers for the unit conditions.** This is the point on which the polar parameterisation earns its place. The boost $\tilde U_{\Psi,\mathrm b}$ and the rotor $\tilde u_{\mathrm r}$ are units *by construction*, because they are exponentials of a rapidity times an axis and of an angle times an axis; the axes are unit vectors and the parameterisation respects that. No condition $\tilde U\tilde U^{\natural}=e_t$ has to be imposed, so no multiplier is needed for it. **The tensor formulations of the spin fluid need three multipliers for exactly these conditions**, and the article's contribution is to record that the exact parameterisation removes them.

**No multipliers is not no constraints.** The six equations above are constraints, and they are Euler–Lagrange equations of the same functional; they are not multipliers and they are not optional. A reader who takes "no multipliers" for "no constraints" has the wrong picture, and the distinction is the article's main technical point.

**What kind of constraints.** They are primary: they follow from the momenta's vanishing, not from the equations of motion. Whether they are first class or second class — whether they generate gauge transformations or restrict the initial data — has not been determined. That determination requires the Poisson brackets of the constraints among themselves, and the brackets are the ones the four-bracket structure suggests and not the ones a canonical analysis of the parameters would give. The article does not carry the computation out, and §*Open Questions* says so.

## Which Currents the Word Produces

The word has a phase, and a phase has a current. The current the word produces is not the current the element action produces, and the difference is the subject of this section.

**The phase current.** Because the action depends on $\theta_{\mathrm{pha}}$ only through its derivative, the phase is a cyclic coordinate and the conjugate momentum is conserved:

$$
\pi_{\theta_{\mathrm{pha}}}=-\hbar c\,\rho=\text{constant},
\qquad
\partial_{r'_t}\rho=0 .
$$

This is the Noether current of the word's phase symmetry, and it is the statement that the density is conserved along the flow.

**What the element action produces.** The element action's local-phase Noether current is the display of the element companion: a sum over the parts in the temporal slot and a difference in the spatial slots, which is the Gordon pairing and which equals the chart's $\rho\cosh\theta_{\mathrm{rpd}}$ and $\rho\sinh\theta_{\mathrm{rpd}}u_{\mathrm b,\eta}$.

**The two are not the same object, and the difference is a spatial slot.** The word's phase current is the temporal slot of the element current and nothing else. The element current's spatial slots come from the boost, not from the phase, and the word's parameterisation does not produce them from the phase's symmetry: it produces them from the boost's. A variational principle in the word therefore has *two* symmetries where the element action has one — the phase's and the boost's — and the element action's current is the combination of the two.

**Why this matters, stated plainly.** The element companion's desired transformation is a phase rotating at one rate and a boost at another. In the word, that transformation is available as two independent one-parameter flows, because the phase and the rapidity are independent parameters. In the element action it is not: the action's symmetry is the phase alone, and the boost is not a symmetry of the action but a coordinate of the field.

**The consequence for the reconstruction question.** If the polar variational principle is to reproduce the element action's current — the one the equation needs — then the boost's flow must be the second half of it, and the two flows must combine with the two rates. The word supplies both flows; the action supplies one symmetry. Whether the constrained system's Dirac analysis supplies the second is exactly the reconstruction question, and the article states it as a conjecture in the next section and does not prove it.

**What is not claimed.** Nothing in this section says the word's phase current is wrong. It is the correct current of the current that the word's phase generates. What it is not is the element action's current, and the article declines to identify the two.

## The Reconstruction Conjecture

**The statement.** Suppose the coupled equation, written for a general element, has a conserved current; suppose further that the current is the one the field's own parameters define, that is, the phase current together with the boost current; then the local symmetry that the current generates is a local phase flow combined with a local boost, and the flow's operator is the word's boost and rotor. **The conjecture is that the constrained system of §*The Constraint Structure*, once its Dirac brackets are computed, generates exactly this flow.**

**Why it is a conjecture and not a theorem.** The equivalence of the two functionals is formal and follows from the bijection. What does not follow is that the *flow* generated by the constrained system's brackets is the flow the equation defines. A degenerate action can be equivalent to a non-degenerate one as a functional and still fail to reproduce its flow, because the constraint surface can be too small or the brackets can differ from the Poisson brackets by terms that do not vanish on it.

**The strongest objection.** Any conserved current can be presented as the current of *some* symmetry: given a current, one can always write down a transformation that generates it. So the conjecture's hypothesis — "the current is the one the field's own parameters define" — does not single out a current from all possible currents, and a construction that does not single out its object has not derived anything.

**The partial answer, and its limit.** The objection is correct, and the partial answer is the one the element companion gives: the requirement is not merely that the current be conserved but that it be the *pairing* the algebra supplies, with the two parts entering with opposite signs. In the word, that requirement is the requirement that the phase flow and the boost flow combine at the two rates. The partial answer's limit is that it replaces one selection problem by another: the pairing is the algebra's, but the choice of frame units inside the pairing is the frame's (§*The Current* of the element companion). So the conjecture is well posed only relative to a frame.

**What would settle it.** The Dirac brackets of the six constraints, computed with the four-bracket structure in place of the parameter structure, and the verification that the resulting flow reproduces $\partial_{r'_t}\tilde\Xi=-i\tilde K_\Phi\tilde\Xi$ up to the gauge factor. This is a finite computation on a system with eight parameters and six constraints, and it is not attempted here.

**What the article claims without the conjecture.** Everything in §*The Action in the Word* and §*The Constraint Structure* stands without the conjecture: the action, the momenta, the two evolution equations, the six constraints, and the absence of multipliers for the unit conditions. The conjecture is what would connect them to the equation, and the connection is what is missing.

## The Bracket Expansion

The four brackets are the decomposition of the logarithmic derivative, and the coupling acts on two of them. That statement is exact, it does not depend on the conjecture, and it is the article's clearest structural result.

**The four brackets, with the coupling.** For each component,

$$
\tilde\Xi^{-1}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi
=\frac{1}{2}\partial_\mu\ln\rho
+i\Bigl(\partial_\mu\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}A_\mu^{\,t}\Bigr)
+\tilde u_{\mathrm r}^{-1}\bigl(\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b}\bigr)\tilde u_{\mathrm r}
+\frac{i\,ϙ}{\hbar}A_\mu^{\,\eta}\vec e_\eta
+\tilde u_{\mathrm r}^{-1}\partial_\mu\tilde u_{\mathrm r},
$$

where $A_\mu^{\,t}$ and $A_\mu^{\,\eta}$ are the temporal and spatial slots of the component's potential, and where the two added terms have been written beside the brackets they join.

**The type table.**

| bracket | type | coupling's share | meaning |
| --- | --- | --- | --- |
| scale | real central scalar | none | continuity |
| phase | central imaginary | temporal slot | guidance |
| boost | Hermitian | spatial slots | velocity transport |
| rotor | real vector | none | spin transport |

**Two of four, and the two are the momentum and the velocity.** The potential joins the phase bracket, where the momentum is read, and the boost bracket, where the velocity is read. It cannot join the scale bracket, where the density is read, and it cannot join the rotor bracket, where the spin is read. That is the polar statement of what a central connection can and cannot do, and it is a statement of algebraic type: a central scalar times a field cannot produce a real vector part.

**Why the two-bracket structure is the one to read the coupling from.** It says in advance which physical quantities the potential can shift and which it must leave alone. The density is untouched because the potential is central; the spin direction is untouched for the same reason. The momentum and the velocity are shifted because the potential's two slots have exactly the two types those brackets carry. No computation of the potential's effect on the field is needed beyond the type table.

**The limit of the statement.** The type table says where the potential acts; it does not say what the resulting motion is. For a constant potential the motion is a gauge phase and the shift is unobservable; for a non-constant one the shift is the Lorentz force at the level of the momentum, and the article does not derive the force from the brackets. That derivation belongs to the element companion's forces and to *Relativistic Mechanics from the Dirac Wave*.

## The Operator Setting

The chart's parameters become fields, and the action acquires gradient terms.

**What changes.** In the operator setting the rapidity $\theta_{\mathrm{rpd}}$ and the rotor angle $\theta_{\mathrm{axr}}$ are functions of position, so the boost bracket and the rotor bracket contribute to the spatial slots of the kinetic term and not only to the temporal one. The action becomes

$$
S=\int\mathrm{d}^{4}r\;\Bigl[-\hbar c\,\rho\,\partial_{r'_t}\theta_{\mathrm{pha}}-\rho V-mc^{2}r^{2}+\text{terms in }\nabla r,\ \nabla\theta_{\mathrm{rpd}},\ \nabla\theta_{\mathrm{axr}}\Bigr],
$$

and the gradient terms are the quantum potential's, in the spin-fluid form.

**The standard counterpart.** The scalar case of this structure is Madelung's variational principle, and the spin case is the Takabayasi–Bohm–Holland hydrodynamics with the spin's own transport law. Both are established in the literature and this article does not derive them: the scalar case is the central-field limit of the parent polar article, and the spin case is the subject of *Spin Hydrodynamics in Biquaternionic Form*.

**The one thing this article adds to the standard account.** The standard derivations impose the unit conditions with Lagrange multipliers and then impose the spin-transport law as an additional equation, chosen from a family. Here the parameterisation imposes the unit conditions exactly, so the multipliers are absent, and the spin-transport law is the rotor bracket's equation and not an addition. That is a genuine simplification of the *presentation* and not of the *physics*: the family of admissible spin-transport laws is still there, in the choice of which parameter is taken as the spin's phase.

**The step that is not taken.** The article does not show that the operator setting's action reduces to the standard one in every case, and it does not show that the constraints close in the operator setting any better than in the constant one. Both are open.

## What the Polar Variational Principle Adds

**Adds.**

- The action in eight real coordinates, with the coupling in the two brackets it can reach and in no others.
- The constraint structure: seven momenta vanishing or fixed, two evolution equations, six constraints.
- The statement that the parameterisation is exact, so no multiplier is needed for the unit conditions — in contrast with the tensor formulations, which need three.
- The distinction, stated sharply, between *no multipliers* and *no constraints*.
- The type table, which says in advance where the potential can act.

**Does not add.**

- No new solution. The fields are the element companion's, and the word is a change of variables.
- No new prediction. The functional is the element companion's.
- No proof that the constrained system's flow is the coupled equation's flow. That is the conjecture of §*The Reconstruction Conjecture* and it is not settled.
- No second current from the action. The word has two flows and the action has one symmetry; the combination is the conjecture's business.
- No resolution of the constraint algebra: first class or second class is not determined.

**The ledger in one paragraph.** The polar variational principle is the element variational principle in eight coordinates, and the substitution buys one thing that the element form cannot state as cleanly: the constraints are visible, they are Euler–Lagrange equations, and the exact parameterisation removes the multipliers that the tensor formulations need. It buys nothing else, and in particular it does not buy a derivation of the equation's flow, because that derivation needs the Dirac brackets and they are not computed.

## Open Questions

**The constraint algebra.** Whether the six constraints are first class or second class, and what brackets they obey, is the article's central open question. The computation is finite and is not attempted here. Until it is done, the reconstruction conjecture cannot be tested.

**The reconstruction conjecture.** §*The Reconstruction Conjecture* states it, states the strongest objection to it, and states what would settle it. The objection — that a conserved current can always be presented as some symmetry's current — is not answered in general, and the partial answer relative to a frame is the most the article can say.

**The two flows and the one symmetry.** The word has a phase flow and a boost flow; the action has one symmetry. Whether the constrained system supplies the second flow is the same question as the conjecture's, approached from the other side. A computation of the boost's Noether charge in the constrained system, and its comparison with the pairing's spatial slots, would settle it.

**The frame's role.** The pairing needs fixed frame units and the word's parameters are read in a fixed frame. Whether the frame's choice is a gauge freedom of the polar formulation, or a genuine datum, is not settled and is the same question the element companion's open questions record.

**The operator setting's closure.** Whether the constraint structure closes in the operator setting, where the rapidity and the rotor angle are fields, is not attempted. The standard spin-fluid literature suggests it does not close without an additional transport law, and the corpus has not settled which law the biquaternionic arrangement selects.

## Summary

The polar coupled action is the coupled action with the word substituted, and in the chart it is

$$
S=\int\mathrm{d}^{4}r\;\Bigl[-\hbar c\,\rho\,\partial_{r'_t}\theta_{\mathrm{pha}}-\rho V-mc^{2}r^{2}\Bigr],
\qquad
\rho=r^{2}\cosh\theta_{\mathrm{rpd}},
$$

with one velocity, the phase's, and a coefficient that carries the boost's rapidity.

The action is a constrained system. Seven of the eight conjugate momenta vanish or are fixed functions of the coordinates; two Euler–Lagrange equations carry time derivatives, the continuity equation for $\rho$ and the guidance equation, and six are constraints on the frame variables.

The parameterisation is exact, so the unit conditions need no Lagrange multiplier. The six constraints are nonetheless there and they are Euler–Lagrange equations. The absence of multipliers is not the absence of constraints, and the distinction is the article's main technical point.

The word's phase current is the temporal slot of the element action's current and not the whole of it. The element current's spatial slots come from the boost, so the word has two flows where the action has one symmetry, and combining them at two rates is the reconstruction conjecture.

The conjecture is stated, its strongest objection is stated, and it is not proved. What would prove it is the Dirac analysis of the six constraints, and that analysis is not carried out here.

The coupling's place is exact and independent of the conjecture: the potential joins the phase bracket and the boost bracket and neither of the other two, by algebraic type alone. The density and the spin direction are what a central connection cannot touch.

The polar variational principle's genuine gain is therefore structural and not dynamical: the constraints are visible, the multipliers are gone, and the coupling's reach is read off a table of types.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The word; a bijection onto the N-regular set |
| $r>0$ | Scale; the density is not $r^{2}$ |
| $\theta_{\mathrm{pha}}$ | Phase; the only parameter with a velocity in the action |
| $\theta_{\mathrm{rpd}}\ge0,\ \vec u_{\mathrm b}$ | Rapidity and axis of the boost |
| $\theta_{\mathrm{axr}}\in[0,2\pi)$ | Rotor angle |
| $\rho=r^{2}\cosh\theta_{\mathrm{rpd}}$ | Density; the temporal slot of the current |
| $V$ | Potential's scalar part in the frame; independent of $r$ and $\theta_{\mathrm{pha}}$ |
| $S$ | The polar action; one velocity, six constraints |
| $\pi_{\theta_{\mathrm{pha}}}=-\hbar c\rho$ | The only genuine momentum; conserved |
| $\pi_{r},\pi_{\theta_{\mathrm{rpd}}},\pi_{\theta_{\mathrm{axr}}},\pi_{u_{\mathrm b}},\pi_{u_{\mathrm r}}$ | Zero; the primary constraints' origin |
| $\partial(\rho V)/\partial p=0$ | The six constraint equations |
| $\partial_{r'_t}(r^{2}\cosh\theta_{\mathrm{rpd}})=0$ | Continuity |
| $-\hbar c\cosh\theta_{\mathrm{rpd}}\partial_{r'_t}\theta_{\mathrm{pha}}-V-mc^{2}=0$ | Guidance |
| scale, phase, boost, rotor | The four brackets; real scalar, central imaginary, Hermitian, real vector |
| $\mathcal B_\Psi=\tilde U_{\Psi,\mathrm b}^{-2}$ | Four-vector factor; the mass term's operator |

## Further Reading

- [The Variational Principle and the Coupled Dirac Equation in Biquaternionic Form](the-variational-principle-and-the-coupled-dirac-equation-in-biquaternionic-form.html), the action this article re-coordinatises.
- [The Coupled Dirac Equation in Biquaternionic Polar Variables](the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), the equation in the chart, without the action.
- [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html), for the word, the four brackets and the mass-term proposition.
- [The Variational Principle and the Dirac Equation in Biquaternionic Form](the-variational-principle-and-the-dirac-equation-in-biquaternionic-form.html), for the free action's structure and the count of the pair.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localization that produces the coupling.
- [Spin Hydrodynamics in Biquaternionic Form](spin-hydrodynamics-in-biquaternionic-form.html), for the four brackets as the spin fluid's transport laws.
- [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html), for the scalar limit in which the brackets collapse to two.
- [The Classical Origin of $g=2$ in Biquaternionic Form](the-classical-origin-of-g-2-in-biquaternionic-form.html), for the spin's transport in a background.
- [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html), for the pairing's two frame units.
- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the scalar variational principle.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the tensor formulation and its three multipliers.
- David Bohm, "A suggested interpretation of the quantum theory in terms of hidden variables," *Physical Review* **85** (1952) 166–193, for the quantum potential.
- Paul A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for constraint analysis and the classification of constraints.
