# __The Local Entropy Current__

## Introduction

**The second law is one divergence, and this article writes it on the current that carries the entropy of the fluid.** The current is

$$
\tilde J_{\Phi,\mathrm{ent}}=s_{\mathrm{ent}}\,\gamma\left(e_t+\vec\beta_{\mathrm{vel}}\right),
\qquad
\vec\beta_{\mathrm{vel}}=\frac{\vec v}{c},
$$

an element of the material sector with a real temporal coefficient and a real vector part, and the second law reads

$$
\mathrm{Sc}\left((\tilde\nabla_\Phi)^{\natural}\tilde J_{\Phi,\mathrm{ent}}\right)\ge 0 .
$$

**Everything in this article follows from those two displays plus one declaration: the current is Hermitian.** The declaration is what makes the inequality *real* — the scalar part of the divergence of a Hermitian element is a real number, and the scalar part of the divergence of an anti-Hermitian one is imaginary — and it is made once, here, and inherited by every article of the category that writes an entropy inequality, in particular [Causal Dissipative Hydrodynamics in Biquaternionic Form](causal-dissipative-hydrodynamics-in-biquaternionic-form.html), which does not write a fresh $\mathrm{Re}$.

**What this article absorbs and what it does not.** It absorbs only the pointwise objects: the entropy *density* as a field, the entropy *current* as an element, and the divergence that says whether the density grows. **It does not absorb the entropy functional, and it adds nothing that [Coarse-Graining and the Biquaternion Entropy Functional](coarse-graining-and-the-biquaternion-entropy-functional.html) already has.** That article owns the functional $\mathcal{S}(\tilde{Ϛ}_{\Psi})=-2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\log\tilde{Ϛ}_{\Psi})$ on the informational sector, its dependence on the biquaternion norm alone, its vanishing on the zero-divisor cone, and its monotonicity under coarse-graining. **This article cites all of that and repeats none of it.** The relation between the two articles is stated in the section on what is left to be said: the functional is a number attached to a state, the current is a field attached to a fluid, and the second law below is the statement that the field version's divergence has a sign.

**What the current is not.** It is not the entropy functional's gradient, and it is not the informational sector's state: it lives in $\mathbb{B}_\Phi$ and its coefficients are the fluid's own thermodynamic quantities. **The two sectors meet in the norm**, as they do throughout the corpus, and the meeting is stated where it occurs rather than assumed at the outset.

## The Current and Its Hermiticity

### The definition

**The entropy current is the proper entropy density carried along the flow, and the flow element supplies the direction.** With the flow element of [The Local Thermal State of a Fluid](the-local-thermal-state-of-a-fluid.html), $\tilde V_\Phi=\gamma c\left(ie_t+\vec\beta_{\mathrm{vel}}\right)$, and with $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$, the entropy current is the element

$$
\tilde J_{\Phi,\mathrm{ent}}=\frac{s_{\mathrm{ent}}}{c}\,\gamma c\left(e_t+\vec\beta_{\mathrm{vel}}\right)
=s_{\mathrm{ent}}\,\gamma\left(e_t+\vec\beta_{\mathrm{vel}}\right),
$$

whose components, written low on the pattern of $k_{\Phi,\mu}$, are

$$
J_{\Phi,\mathrm{ent},t}=s_{\mathrm{ent}}\,\gamma,
\qquad
J_{\Phi,\mathrm{ent},\eta}=s_{\mathrm{ent}}\,\gamma\,\beta_{\mathrm{vel},\eta}.
$$

**The temporal component is the density and the spatial ones are the flux, and the factor $i$ that the flow element carries has been dropped in passing from the flow to the current.** That is the whole of the construction, and it is worth being explicit about why the factor is dropped: a displacement is imaginary in its temporal slot because the corpus measures imaginary time, while a *density* is a real number per unit proper volume and its temporal slot is real. **The flow element and the current therefore differ by exactly one $i$**, and that difference is what the Hermiticity declaration formalises.

**The comparison with the thermal element, which is the same construction with the $i$ kept.** In [Equilibrium Partition Function in a Moving Frame](equilibrium-partition-function-in-a-moving-frame.html) the thermal element is $\tilde\beta_\Phi=\beta\gamma\left(ie_t+\vec\beta_{\mathrm{vel}}\right)$: same direction, same $\gamma$, but anti-Hermitian because it is a displacement along imaginary time. **The pair $\tilde\beta_\Phi$ and $\tilde J_{\Phi,\mathrm{ent}}$ are the two ways the corpus writes "the same direction, once for a length and once for a density"**, and a reader who has both in view will not confuse a period with an entropy.

### The Hermiticity declaration, and what it buys

**The current is declared Hermitian: $\tilde J_{\Phi,\mathrm{ent}}^{*}=\tilde J_{\Phi,\mathrm{ent}}$, with the star the corpus's conjugation that reverses the quaternion part and conjugates the central $i$.** On the components above this is the statement that all four coefficients are real, which they are by construction.

**The declaration buys exactly one thing: it makes the scalar part real.** For an element $\tilde Q$ with components $Q_\mu$, the corpus's divergence has the scalar part

$$
\mathrm{Sc}\left(\tilde\nabla^{\natural}\tilde Q\right)=\partial_\mu Q_\mu
$$

**for every element and not only for a Hermitian one** — the identity is a property of the operator and of nothing else, and the two $\varepsilon$ weights of the gradient and the two signs of the scalar part cancel in each slot. **What Hermiticity adds is the reality of the right-hand side.** With $\tilde Q^{*}=\tilde Q$ the four coefficients are real, so $\partial_\mu Q_\mu$ is a real number and it can be compared with zero. For an anti-Hermitian element the coefficients are pure imaginary, the same scalar part is $i$ times a real number, and an inequality written on it would compare an imaginary quantity with zero, which is meaningless. **The declaration is therefore not a convention about signs; it is the condition under which the second law has a truth value.**

**Why the corpus does not instead write $\mathrm{Re}$ everywhere.** The two spellings are equivalent — a fresh $\mathrm{Re}$ on every inequality gives the same set of true statements — and the corpus chooses the declaration because it is made once and inherited, whereas a $\mathrm{Re}$ has to be repeated at every display and can be silently dropped at one of them. **The rule for the reader is therefore: an entropy inequality in this corpus comes with one of two marks, a declared-Hermitian current or a written $\mathrm{Re}$, and never with neither.**

**The divergence's spelling.** The article uses $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde J_{\Phi,\mathrm{ent}})$, which is one of the two live spellings in the corpus, the other being $\langle\tilde\nabla_\Phi,\tilde J\rangle_{\natural}$. **No $\otimes$ appears in a divergence**: the tensor product is for algebra products, and the divergence is the algebra's own $\natural$-graded derivative contracted with the element. No raised star on the gradient either; the corpus has zero uses of that spelling.

### The contraction is the proper entropy density

**The current contracts to the square of the proper entropy density, and this is the check that the $\gamma$ factors are right.** With $J=a\,e_t+\vec b$ and $a=\gamma s_{\mathrm{ent}}$, $\vec b=\gamma s_{\mathrm{ent}}\vec\beta_{\mathrm{vel}}$,

$$
J_{\Phi,\mathrm{ent},t}^{\,2}-\lvert\vec J_{\Phi,\mathrm{ent}}\rvert^{2}
=a^{2}-\lvert\vec b\rvert^{2}
=\gamma^{2}s_{\mathrm{ent}}^{2}\left(1-\beta_{\mathrm{vel}}^{2}\right)=s_{\mathrm{ent}}^{2},
$$

using $\gamma^{2}(1-\beta_{\mathrm{vel}}^{2})=1$. **The contraction is boost invariant and equals the square of the entropy density in the fluid's own frame** — which is what an invariant should do, and what a naive current with the density in the temporal slot and no $\gamma$ would fail to do.

**The contraction is not $\langle\tilde J_{\Phi,\mathrm{ent}}\rangle_{\natural}$, and the article says so rather than conflating the two.** The quaternionic norm is a sum of squares, $\langle\tilde Q\rangle_{\natural}=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$, so on the real coefficients this current has it is $a^{2}+\lvert\vec b\rvert^{2}=\gamma^{2}s_{\mathrm{ent}}^{2}(1+\beta_{\mathrm{vel}}^{2})$ and it is not invariant. The sum equals the contraction exactly when the temporal coefficient is imaginary, $Q_t^{2}=-a^{2}$, which is the case for $\tilde V_\Phi$ and for $\tilde\beta_\Phi$ and not for this current, whose temporal coefficient is real by the Hermiticity declaration. **The invariant is the contraction, read with the corpus's $(1,-1,-1,-1)$ signature on the four slots**, and its positivity is what makes $s_{\mathrm{ent}}$ a density rather than a flux.

**The same computation for the thermal element, for contrast, and the two routes are now visible side by side.** There $a=i\beta\gamma$, so the quaternionic norm is the sum $a^{2}+\lvert\vec b\rvert^{2}=-\beta^{2}\gamma^{2}+\beta^{2}\gamma^{2}\beta_{\mathrm{vel}}^{2}=-\beta^{2}\gamma^{2}(1-\beta_{\mathrm{vel}}^{2})=-\beta^{2}$, while the contraction of the physical components, $a^{2}-\lvert\vec b\rvert^{2}$, is $-\beta^{2}\gamma^{2}(1+\beta_{\mathrm{vel}}^{2})$. **The thermal element's invariant is the quaternionic norm and the current's is the contraction**, and the swap is the $i$ in the thermal element's temporal slot: with $Q_t$ imaginary the sum is negative and invariant, and with $Q_t$ real the difference is the invariant one.

**A number, because a contraction is the kind of thing that can be checked.** At $\beta_{\mathrm{vel}}=0.6$, $\gamma=1.25$ and $s_{\mathrm{ent}}=3$: $a=3.75$, $\lvert\vec b\rvert=2.25$, and $a^{2}-\lvert\vec b\rvert^{2}=14.0625-5.0625=9=s_{\mathrm{ent}}^{2}$ exactly. At $\beta_{\mathrm{vel}}=0.8$, $\gamma=1.666\,666\,667$ and $s_{\mathrm{ent}}=3$: $a=5.000\,000\,000$, $\lvert\vec b\rvert=4.000\,000\,000$, and $25-16=9$ exactly. **The two rows are the check that the $\gamma$ sits in the temporal slot and the $\gamma\beta_{\mathrm{vel}}$ in the spatial ones**, and a current written with $\gamma$ in both would fail at the second row.

## The Second Law

### The divergence, in components

**The second law is the statement that the scalar part of the divergence is non-negative, and written out it is the continuity equation with a source.** With the components above and the derivative $\partial_\mu=\partial/\partial R_\mu$,

$$
\mathrm{Sc}\left((\tilde\nabla_\Phi)^{\natural}\tilde J_{\Phi,\mathrm{ent}}\right)
=\partial_t\left(s_{\mathrm{ent}}\gamma\right)
+\partial_\eta\left(s_{\mathrm{ent}}\gamma\beta_{\mathrm{vel},\eta}\right)
=\sigma_{\mathrm{ent}}\ \ge 0,
$$

where $\sigma_{\mathrm{ent}}$ is the entropy production per unit coordinate volume and unit coordinate time. **The display is the whole of the second law in this formalism**: a divergence of a density-plus-flux with a sign. Every other statement of the second law in the category is an evaluation of this one.

**The two readings of the same display, and why both are needed.** Read as a balance, it says that the entropy in a region changes by the flux through the boundary plus the production inside. Read as an inequality, it says that the production cannot be negative, so entropy is not destroyed anywhere. **The first reading is the one the fluid equations use; the second is the one the state's monotonicity uses**, and the corpus keeps the two apart because the first holds for the fields and the second for the functional, which is [Coarse-Graining and the Biquaternion Entropy Functional](coarse-graining-and-the-biquaternion-entropy-functional.html)'s and is cited here rather than re-derived.

**The equality case, stated precisely.** The production vanishes identically when the current is divergence-free, $\partial_t(s_{\mathrm{ent}}\gamma)+\partial_\eta(s_{\mathrm{ent}}\gamma\beta_{\mathrm{vel},\eta})=0$, which is the statement that the total entropy of an isolated region is constant. **In equilibrium this is what happens**, and the mechanics of why is the next subsection's.

### Equilibrium: why an ideal fluid produces nothing

**An ideal fluid has zero production, and the reason is that its entropy per particle is constant along each worldline.** With $s_{\mathrm{ent}}=\sigma_{\mathrm{spc}}n_{\mathrm{num}}$ and the particle current $\tilde J_{\Phi,\mathrm{num}}=n_{\mathrm{num}}\gamma(e_t+\vec\beta_{\mathrm{vel}})$ conserved,

$$
\partial_\mu J_{\Phi,\mathrm{num},\mu}=0
\quad\text{and}\quad
s_{\mathrm{ent}}=\sigma_{\mathrm{spc}}\,n_{\mathrm{num}}
\ \Longrightarrow\
\mathrm{Sc}\left((\tilde\nabla_\Phi)^{\natural}\tilde J_{\Phi,\mathrm{ent}}\right)
=n_{\mathrm{num}}\gamma\,\frac{d\sigma_{\mathrm{spc}}}{dR}
=0
$$

when $\sigma_{\mathrm{spc}}$ is constant along the flow. **The derivation is two lines and it is worth having**: the entropy current is the particle current times a number, so its divergence is the particle current times the gradient of that number, and the gradient is zero. **This is the local form of the statement that an ideal fluid is adiabatic**, and it identifies the one thing a dissipative fluid must break: either the conservation of the particle current, or the constancy of the entropy per particle.

**The rigidity condition enters here as the statement that this is consistent.** Under $\partial_\mu v_{\Phi,\nu}+\partial_\nu v_{\Phi,\mu}=0$ the flow is rigid, the local state is determined by the local data, and the adiabatic statement closes. **Off rigidity the closure fails and the production is a functional of the gradients**, which is the content of the dissipative article.

### Off equilibrium: the production and its sources

**Off equilibrium the production is a sum of squares, one per dissipative channel, and each square comes with a transport coefficient.** In the first-order form the display above evaluates to

$$
\sigma_{\mathrm{ent}}=\frac{1}{T}\left(\zeta\,\theta^{2}+2\eta_{\mathrm{sh}}\,\sigma^{\mathrm{sh}}_{\mu\nu}\sigma^{\mathrm{sh}}_{\mu\nu}
+\kappa_{\mathrm{th}}\,\frac{\partial_\eta T\,\partial_\eta T}{T}\right)+\cdots,
$$

with $\zeta$ the bulk viscosity, $\eta_{\mathrm{sh}}$ the shear viscosity and $\kappa_{\mathrm{th}}$ the thermal conductivity, $\sigma^{\mathrm{sh}}_{\mu\nu}$ the shear of the flow and $\theta$ its expansion. **Every term is a square multiplied by a coefficient that positivity requires to be non-negative**, so the inequality holds if and only if the transport coefficients are non-negative; that statement is the *content* of the second law at first order and not a decoration on it.

**The ellipsis, and where it matters.** The first-order form is not causal and is not stable, which is [Causal Dissipative Hydrodynamics in Biquaternionic Form](causal-dissipative-hydrodynamics-in-biquaternionic-form.html)'s subject: the ellipsis hides the relaxation terms that restore hyperbolicity. **This article writes the ellipsis and does not open it**, because the production's *form* — a sum of squares with non-negative coefficients — survives the relaxation structure and is the part that the rest of the category needs.

**A check on the sign that a reader can do.** For a pure shear, $\theta=0$ and $\partial_\eta T=0$, so $\sigma_{\mathrm{ent}}=2\eta_{\mathrm{sh}}\sigma^{\mathrm{sh}}_{\mu\nu}\sigma^{\mathrm{sh}}_{\mu\nu}/T\ge0$ for $\eta_{\mathrm{sh}}\ge0$: a sheared fluid heats and its entropy grows. **A negative shear viscosity would make the production negative and the inequality fail**, which is the standard argument that $\eta_{\mathrm{sh}}\ge0$ is not an assumption but a consequence.

## The Quantum Contribution

### What the quantum part could have contributed, and does not

**The quantum stress does not create entropy directly, and the reason is that the state that carries it has none.** On the solutions of the polar form the entropy density of the state is zero — the state is pure — so the entropy current of this article is the zero element and the second law reads $0\ge0$. **A reader who expects $Q_{\mathrm{qnt}}$ to appear as a source in the production will not find it**, and the absence is a statement: gradient corrections do not dissipate.

**The precise form of the statement, because it is easy to overstate.** The conservation of the stress is a separate equation from the second law. With $\tilde\Sigma_\Psi=w_{\mathrm{fl}}e_t+\tfrac{i}{c}\vec S_{\mathrm P}$ and with the quantum part of the stress included, the conservation law is

$$
\mathrm{Sc}\left((\tilde\nabla_\Phi)^{\natural}\tilde\Sigma_\Psi\right)=0
$$

on the fields that solve the equation of motion, and it holds *because* the flow obeys the mass shell that $Q_{\mathrm{qnt}}$ modifies,

$$
\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2m\,Q_{\mathrm{qnt}},
$$

quoted from [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html). **The quantum potential appears in the mass shell and not in the production**, and that placement is the content of the polar-form article's derivation: the correction is what the flow has to satisfy, not what the flow leaks.

**The negative statement, made positive.** The quantum term changes which flows conserve the stress; it does not change how much entropy a given flow produces. **A fluid whose density has a gradient is a fluid whose flow must obey a modified mass shell, and once it does, its stress is conserved and its entropy is constant.** That is the whole of the framework's statement about the quantum part of the second law, and it is a statement about the constraint and not about dissipation.

### Where entropy production does come from: the two components

**The quantum part can produce entropy indirectly, and the mechanism is friction between the component that carries the quantum stress and the component that carries the entropy.** In a state that is not pure — a state with a condensate and an excitation gas — the condensate's stress is the quantum one and the gas carries the entropy; the condensate's flow and the gas's flow are two elements, and their relative motion dissipates through mutual friction. **The dissipation is not proportional to $Q_{\mathrm{qnt}}$; it is proportional to the relative velocity and to a friction coefficient**, and $Q_{\mathrm{qnt}}$ enters only through the condensate's mass shell.

**This is the standard picture of a two-fluid system and it is [The Two-Fluid Model in Biquaternionic Form](the-two-fluid-model-in-biquaternionic-form.html)'s subject.** The article states the mechanism here for one reason: a reader who wants to know where the quantum part enters the second law should be told that it enters through the *coupling* and not through a source term. **The entropy current of this article remains the single-component one; the two-component version is written by adding a second current and letting the two exchange momentum.**

**What the corpus does not do, and says so.** It does not claim that mutual friction has been derived from the rotor's equation of motion in this framework. That derivation is not in the category, and [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html) is the nearest neighbour to it without being it. **The article stops at the mechanism and marks the derivation as open.**

### What is left to be said, and what is not

**Three things are said here and nothing else is.** First, that the entropy current is the density times the flow element with the $i$ dropped, and that its norm is the proper entropy density. Second, that its scalar divergence is a real number because the current is Hermitian, and that the second law is that number's sign. Third, that the quantum stress enters the constraint and not the production, so the pure state's entropy current vanishes and the second law is saturated.

**Three things are not said, and each belongs to another article.** The functional and its monotonicity belong to [Coarse-Graining and the Biquaternion Entropy Functional](coarse-graining-and-the-biquaternion-entropy-functional.html), which derives them from the logarithm of the informational sector's state and which this article does not duplicate. The relaxation structure that makes the production's sum of squares causal belongs to [Causal Dissipative Hydrodynamics in Biquaternionic Form](causal-dissipative-hydrodynamics-in-biquaternionic-form.html), which inherits this article's Hermiticity declaration and writes no fresh $\mathrm{Re}$. The spin contribution to the entropy current belongs to [Spin Hydrodynamics in Biquaternionic Form](spin-hydrodynamics-in-biquaternionic-form.html), where the spin potential $\mu_{\mathrm{spn}}$ supplies a second chemical potential and the current gains a term.

**The relation between the functional and the current, in one sentence.** The functional is a number attached to a state, the current is a field attached to a fluid, and the second law of this article is the statement that the field's divergence has a sign while the functional's monotonicity is the statement that the number's change has a sign under coarse-graining; **the two are not the same theorem, they are the two halves of one**, and the corpus's convention is that the half which is a field lives here and the half which is a state lives there.

## Numbers

**The identities of this article were evaluated at three velocities and one production table, and the residuals are recorded because they are the whole of the arithmetic.**

| $\beta_{\mathrm{vel}}$ | $\gamma$ | $a=\gamma s_{\mathrm{ent}}$ | $\lvert\vec b\rvert=\gamma\beta_{\mathrm{vel}}s_{\mathrm{ent}}$ | $a^{2}-\lvert\vec b\rvert^{2}$ |
|---|---|---|---|---|
| $0.6$ | $1.250\,000\,000$ | $3.750\,000\,000$ | $2.250\,000\,000$ | $9.000\,000\,000\,000$ |
| $0.8$ | $1.666\,666\,667$ | $5.000\,000\,000$ | $4.000\,000\,000$ | $9.000\,000\,000\,000$ |
| $0.979\,795\,897$ | $5.000\,000\,000$ | $15.000\,000\,000$ | $14.696\,938\,457$ | $9.000\,000\,000\,000$ |

**The last column is $s_{\mathrm{ent}}^{2}=9$ in every row**, which is the numerical form of the contraction $J_{\Phi,\mathrm{ent},t}^{2}-\lvert\vec J_{\Phi,\mathrm{ent}}\rvert^{2}=s_{\mathrm{ent}}^{2}$ and the check on where the $\gamma$ sits.

**The production, evaluated once.** With $\zeta=0.1$, $\theta=0.5$, $\eta_{\mathrm{sh}}=0.2$, $\sigma^{\mathrm{sh}}_{\mu\nu}\sigma^{\mathrm{sh}}_{\mu\nu}=0.3$, $\kappa_{\mathrm{th}}=0.05$, $\partial_\eta T\,\partial_\eta T=0.4$ and $T=2$: the three terms of the first-order production are $\zeta\theta^{2}/T=0.012\,500$, $2\eta_{\mathrm{sh}}\sigma^{\mathrm{sh}}_{\mu\nu}\sigma^{\mathrm{sh}}_{\mu\nu}/T=0.060\,000$ and $\kappa_{\mathrm{th}}\partial_\eta T\,\partial_\eta T/T^{2}=0.005\,000$, and the total is $0.077\,500$. **Every term is positive and the sum is positive**, so the display's sign is not a coincidence of the chosen numbers but the consequence of each coefficient being positive.

**What the numbers do not check.** They do not check that $\sigma_{\mathrm{ent}}\ge0$ for *every* flow — that is a theorem about the transport coefficients and not an arithmetic fact. They do not check the quantum stress's conservation, which is the polar-form article's. **They check the two identities of this article — the norm and the decomposition of the production — and nothing further.**

## What Is Established and What Is Interpretation

**Established, and standard.** That the entropy current is $s_{\mathrm{ent}}\gamma(e_t+\vec\beta_{\mathrm{vel}})$, with components low and no $i$ in the temporal slot; that it is Hermitian; that its self-contraction is $s_{\mathrm{ent}}^{2}$; that the scalar part of its divergence is the ordinary divergence of its four components and is real; that the second law is that divergence's non-negativity; that an ideal fluid has zero production because its entropy per particle is constant along each worldline; that the first-order production is a sum of squares over the dissipative channels with non-negative coefficients.

**The framework's contribution, and it is one line.** The corpus writes the entropy current as an *element* whose Hermiticity is the statement that its temporal slot is a density and not a displacement, and it writes the second law as the scalar part of the algebra's own divergence. **The declaration is what makes the inequality real, and the declaration is the article's**, in the sense that this is where the category makes it and every later article inherits it.

**Interpretation, and marked as such.** That the quantum stress enters the constraint and not the production. This follows from the placement of $Q_{\mathrm{qnt}}$ in the mass shell, which is the polar-form article's result, and from the vanishing of the pure state's entropy; it is the corpus's reading of a standard fact about gradient corrections and it is not a new theorem.

**Not claimed.** That the production's first-order form is the whole story — it is not, and the relaxation structure is the dissipative article's. That the entropy current of a spin fluid is this one — it is not, and the spin article adds a term. That mutual friction has been derived here — it has not. That the functional of the coarse-graining article and the current of this article are the same object — they are not, and the section above says how they differ.

## Summary

The entropy current is $\tilde J_{\Phi,\mathrm{ent}}=s_{\mathrm{ent}}\gamma(e_t+\vec\beta_{\mathrm{vel}})$, with $J_{\Phi,\mathrm{ent},t}=s_{\mathrm{ent}}\gamma$ and $J_{\Phi,\mathrm{ent},\eta}=s_{\mathrm{ent}}\gamma\beta_{\mathrm{vel},\eta}$, every index low, and it is **declared Hermitian**: all four coefficients real, the star conjugation fixing the element. Hermiticity is exactly the condition under which $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde J)=\partial_\mu J_\mu$ is a real number, which is why the declaration is the corpus's mechanism for making entropy inequalities meaningful; the alternative spelling with a written $\mathrm{Re}$ is equivalent and is not used here.

The self-contraction is the proper entropy density squared, $J_{\Phi,\mathrm{ent},t}^{2}-\lvert\vec J_{\Phi,\mathrm{ent}}\rvert^{2}=\gamma^{2}s_{\mathrm{ent}}^{2}(1-\beta_{\mathrm{vel}}^{2})=s_{\mathrm{ent}}^{2}$, checked at three velocities with $s_{\mathrm{ent}}=3$ where the value is $9$ in every frame; the quaternionic norm of the same element is $\gamma^{2}s_{\mathrm{ent}}^{2}(1+\beta_{\mathrm{vel}}^{2})$ and is not the invariant, the two coinciding only when the temporal slot carries an $i$. The thermal element of the moving-frame article has the quaternionic norm $-\beta^{2}$, the sign difference being exactly that $i$.

The second law is one divergence, $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde J_{\Phi,\mathrm{ent}})=\partial_t(s_{\mathrm{ent}}\gamma)+\partial_\eta(s_{\mathrm{ent}}\gamma\beta_{\mathrm{vel},\eta})=\sigma_{\mathrm{ent}}\ge0$. An ideal fluid has $\sigma_{\mathrm{ent}}=0$ because $\sigma_{\mathrm{spc}}$ is constant along the flow; off equilibrium the production is $\sigma_{\mathrm{ent}}=T^{-1}(\zeta\theta^{2}+2\eta_{\mathrm{sh}}\sigma^{\mathrm{sh}}_{\mu\nu}\sigma^{\mathrm{sh}}_{\mu\nu}+\kappa_{\mathrm{th}}\partial_\eta T\,\partial_\eta T/T)$ plus relaxation terms, a sum of squares whose sign is the non-negativity of the transport coefficients. Evaluated once at $T=2$, the three terms of the bracket are $\zeta\theta^{2}=0.025\,000$, $2\eta_{\mathrm{sh}}\sigma^{\mathrm{sh}}_{\mu\nu}\sigma^{\mathrm{sh}}_{\mu\nu}=0.120\,000$ and $\kappa_{\mathrm{th}}\partial_\eta T\,\partial_\eta T/T=0.010\,000$, which is $\sigma_{\mathrm{ent}}=0.077\,500$ after the division by $T$.

The quantum part does not enter the production. It enters the mass shell, $E^{2}/c^{2}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2mQ_{\mathrm{qnt}}$, and the stress is conserved on the flows that obey it; the pure state has no entropy, so its current vanishes and the second law is saturated. Entropy from a quantum fluid comes from friction between the component that carries the quantum stress and the component that carries the entropy, which is [The Two-Fluid Model in Biquaternionic Form](the-two-fluid-model-in-biquaternionic-form.html)'s subject and is not derived here.

The functional of [Coarse-Graining and the Biquaternion Entropy Functional](coarse-graining-and-the-biquaternion-entropy-functional.html) is cited and not duplicated: it owns the state's entropy, this article owns the field's current, and the Hermiticity declaration made here is inherited by [Causal Dissipative Hydrodynamics in Biquaternionic Form](causal-dissipative-hydrodynamics-in-biquaternionic-form.html), which writes no fresh $\mathrm{Re}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde J_{\Phi,\mathrm{ent}}=s_{\mathrm{ent}}\gamma(e_t+\vec\beta_{\mathrm{vel}})$ | Entropy current, Hermitian |
| $J_{\Phi,\mathrm{ent},t}=s_{\mathrm{ent}}\gamma$ | Its temporal component, the density |
| $J_{\Phi,\mathrm{ent},\eta}$ | Its spatial components, the flux |
| $s_{\mathrm{ent}}$ | Entropy density |
| $\sigma_{\mathrm{spc}}$ | Entropy per particle |
| $\sigma_{\mathrm{ent}}$ | Entropy production |
| $n_{\mathrm{num}}$, $\tilde J_{\Phi,\mathrm{num}}$ | Number density and particle current |
| $\tilde V_\Phi$ | Flow element, $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$ |
| $\vec\beta_{\mathrm{vel}}=\vec v/c$ | Dimensionless velocity |
| $\gamma=(1-\beta_{\mathrm{vel}}^{2})^{-1/2}$ | Boost factor |
| $\langle\ \rangle_{\natural}$ | Quaternionic norm, $\langle\tilde Q\rangle_{\natural}=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$, a sum of squares |
| $J_{\Phi,\mathrm{ent},t}^{2}-\lvert\vec J_{\Phi,\mathrm{ent}}\rvert^{2}$ | The contraction of the current with itself, the invariant this article uses |
| $\tilde Q$, $Q_t$, $Q_\eta$ | A general element and its temporal and spatial coefficients |
| $\mathrm{Sc}$ | Scalar part |
| $\tilde\nabla^{\natural}$ | The algebra's divergence operator |
| $\tilde Q^{*}$ | The conjugation; $\tilde Q^{*}=\tilde Q$ is Hermiticity |
| $\tilde\Sigma_\Psi=w_{\mathrm{fl}}e_t+\tfrac{i}{c}\vec S_{\mathrm P}$ | Energy–momentum element |
| $w_{\mathrm{fl}}$, $p_{\mathrm{th}}$ | Energy density, thermal pressure |
| $Q_{\mathrm{qnt}}$ | Quantum potential, with the minus sign |
| $\zeta$, $\eta_{\mathrm{sh}}$, $\kappa_{\mathrm{th}}$ | Bulk viscosity, shear viscosity, conductivity |
| $\theta=\partial_\mu v_{\Phi,\mu}$ | Expansion |
| $\sigma^{\mathrm{sh}}_{\mu\nu}$ | Shear of the flow, indices low |
| $T$ | Temperature |
| $E$, $\vec p$, $m$, $c$ | Energy, momentum, mass, speed of light |
| $\tilde\beta_\Phi$ | Thermal element, for contrast |
| $\mathcal{S}(\tilde{Ϛ}_\Psi)$ | Entropy functional, cited from the coarse-graining article |

## Further Reading

- C. Eckart, "The thermodynamics of irreversible processes III: Relativistic theory of the simple fluid," *Physical Review* **58** (1940) 919–924, for the entropy current and the first-order production.
- L. D. Landau and E. M. Lifshitz, *Fluid Mechanics* (Pergamon, 1987), §127, for the relativistic entropy current and its divergence.
- W. Israel, "Nonstationary irreversible thermodynamics: a causal relativistic theory," *Annals of Physics* **100** (1976) 310–331, for the relaxation terms behind the ellipsis.
- W. Israel and J. M. Stewart, "Transient relativistic thermodynamics and kinetic theory," *Annals of Physics* **118** (1979) 341–372, for the systematic construction of the causal production.
- I. Müller, "Zum Paradoxon der Wärmeleitungstheorie," *Zeitschrift für Physik* **198** (1967) 329–344, for the origin of the causality problem in the first-order theory.
- D. Jou, J. Casas-Vázquez and G. Lebon, *Extended Irreversible Thermodynamics* (Springer, 2010), chapters 1–2, for the classification of the dissipative channels used here.
- L. D. Landau and E. M. Lifshitz, *Statistical Physics, Part 2* (Pergamon, 1980), §§77–79, for the entropy of a superfluid and the mutual-friction mechanism.
- The companion articles: [Coarse-Graining and the Biquaternion Entropy Functional](coarse-graining-and-the-biquaternion-entropy-functional.html), [The Local Thermal State of a Fluid](the-local-thermal-state-of-a-fluid.html), [Causal Dissipative Hydrodynamics in Biquaternionic Form](causal-dissipative-hydrodynamics-in-biquaternionic-form.html), and [The Two-Fluid Model in Biquaternionic Form](the-two-fluid-model-in-biquaternionic-form.html).
