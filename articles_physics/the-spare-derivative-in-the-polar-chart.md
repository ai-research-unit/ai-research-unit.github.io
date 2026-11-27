# __The Spare Derivative in the Polar Chart: Manufacturing the Acceleration Law from the Guidance Relation__

## Introduction

Every fluid in this corpus has an acceleration law, and at no rung is that law one of the action's variations. At the Schrödinger rung the two coordinates are the scale and the phase, and their two Euler–Lagrange equations are the amplitude's equation and continuity. Euler is neither. It is obtained by differentiating something else, and the something else is what this article is about.

**The claim.** The polar word does not treat the coordinates alike: it leaves some of them *cyclic*, appearing in the action only through their derivatives, and those coordinates' Euler–Lagrange equations are therefore conservation laws that carry one derivative fewer than the field equation's. **A coordinate whose equation is one order low has a derivative still unspent, and the acceleration law is made from that spare derivative.** The law is manufactured, not varied. Three operations do the manufacturing — differentiating the guidance relation at the gradient rungs, differentiating the algebraic guidance relation at the matrix rung, and projecting the frame's second-order equation at the vector rung — and the article says which rung takes which.

**Why this is a step and not a remark.** The corpus states the fact in passing, correctly, in a sentence: "Euler is not varied; it is differentiated." The sentence is doing more work than it appears to. It says that the acceleration slot of a fluid is not one of the equations the action supplies, and that the derivation therefore has a step whose content is a manipulation rather than a variation. **If that step is not stated, the reader is entitled to ask where Euler came from, and the honest answer is that it came from a conserved quantity and one derivative.**

**The sharpest form of the claim, and the one the article defends.** *The second derivative of the fast coordinate appears in the force slot and nowhere else.* Continuity has only first derivatives. The quantum Hamilton–Jacobi equation has only first derivatives of the phase. The acceleration law is the only equation in the rung that contains $\partial_{t'}\partial_{\imath}S$, and it contains it because the guidance relation was differentiated. **That is a statement about the system's order accounting, and it is checkable by inspection of the three equations.**

**What this article is not.** It is not a derivation of a new equation. Every object it displays is in a sibling article. It is the fourth step of [Five Steps from a Lagrangian to Fluid Equations](five-steps-from-a-lagrangian-to-fluid-equations.html), stated once and at no particular rung, with the rung-by-rung differences made explicit. A reader who has not read the anchor article needs only its S1 to S3; those are restated in the conventions section to the extent this article uses them.

## Conventions

The algebra and the word are [The Algebraic Vocabulary](the-algebraic-vocabulary-element-conjugations-six-subspaces-and-two-ledgers.html) and [The Two Sectors](the-two-sectors-the-hermitian-split-and-the-four-bridges.html). Three symbols recur.

$$
\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad
S=\frac{h}{2\pi}\,\theta_{\mathrm{pha}},
\qquad
\mathcal A_{\imath}=\tilde\Xi^{-1}\partial_{\imath}\tilde\Xi .
$$

$\varrho>0$ is the scale, $S$ the action and $\theta_{\mathrm{pha}}$ the phase, and $\mathcal A_{\imath}$ the logarithmic derivative. The material sector's gradient is $\partial_{\imath}$ with $\imath\in\{t,x,y,z\}$, and the temporal coordinate is $r'_{t}$ where the distinction matters.

**The order of an equation is the order of its highest derivative of the field's data.** This is the article's only technical convention and it is the quantity everything else is about. An equation is *second order* if it contains a second derivative of some coordinate; *first order* if it contains only first derivatives; *algebraic* if it contains none. The field equations of the corpus are second order, with the stated exception of the first-order Schrödinger action, and the article flags that exception where it occurs.

**The Euler–Lagrange equation of a coordinate, and where its order comes from.** For an action $S=\int L$, the equation for the coordinate $q$ is

$$
\frac{\partial L}{\partial q}-\partial_{\imath}\frac{\partial L}{\partial(\partial_{\imath}q)}=0 .
$$

**The second term is always second order in $q$, because it is a divergence of something first order.** The first term is the one that decides the equation's total order. If $\partial L/\partial q$ is nonzero, the equation equates a second-order object to a zeroth-order one and the equation is second order. **If $\partial L/\partial q$ vanishes — if $q$ appears in $L$ only through its derivatives — the equation is $\partial_{\imath}J^{\imath}=0$, a divergence of a first-order current, and it is first order.** That is the whole mechanism, and it is Noether's theorem read as an order statement: a cyclic coordinate's equation is the conservation of its conjugate momentum.

**The word "cyclic" is the article's, and it is the standard one.** A coordinate is cyclic when the Lagrangian does not contain it, only its derivatives. The phase is cyclic at every rung where it exists as a coordinate. The scale is not. The frame is cyclic at the scalar, spinor and matrix rungs, and the rung where it is not is the one this article has to be careful about.

## The Order Accounting of the Word

**The word's four factors divide into two classes, and the division is what the rest of the article runs on.** Two of them — the scale and the phase — are central, and they differ in one respect that decides everything: the algebraic term depends on the scale and not on the phase.

| factor | appears in the kinetic term as | appears in the algebraic term as | cyclic? |
| --- | --- | --- | --- |
| scale $\varrho$ | $\partial_{\imath}\ln\varrho$ | $\varrho$ itself | **no** |
| phase $\theta_{\mathrm{pha}}$ | $\partial_{\imath}\theta_{\mathrm{pha}}$ | nothing | **yes** |
| boost $\tilde U_{\Psi,\mathrm b}$ | $\tilde U^{-1}\partial_{\imath}\tilde U$ | nothing | **yes** |
| rotor $\tilde u_{\mathrm r}$ | $\tilde u^{-1}\partial_{\imath}\tilde u$ | nothing | **yes** |

**The table is a statement about the action's form, and the form is forced by S1.** The algebraic term is a scalar function of the field, and a scalar function of a unitary frame's factor is constant — a unit element contributes only through its derivatives, because any invariant built from it is fixed. **So the frame is cyclic for a structural reason: there is nothing invariant to build from a unit element.** The phase is cyclic for the same reason, one level down: $e^{i\theta}$ is unitary, so no scalar can depend on $\theta$ alone. The scale is the only factor with an invariant to build from, and it is the only one that is not cyclic.

**Three of four coordinates cyclic, and the field equation is second order — so the rung carries three first-order equations and one second-order one.** That sentence is the article's accounting, and it is exact where the action has the S1 form. The next three sections take the three cyclic coordinates in turn and state what the spare derivative does at each.

## The Scale: Why Its Equation Is Second Order

**The scale's equation is the rung's second-order equation, and it is the one that carries the quantum potential.** Because $\partial L/\partial\varrho\neq0$, the variation equates the divergence term to an algebraic term and the result is second order in $\varrho$. At the Klein–Gordon rung it is the mass shell with the quantum potential; at the Schrödinger rung it is the same object with the non-relativistic kinetic term.

$$
\Box_{\Phi}\varrho-\varrho\,\bigl(\partial_{\imath}\theta\bigr)\bigl(\partial^{\imath}\theta\bigr)+\nu_m^{2}\varrho+\frac{\partial V}{\partial\varrho}=0 ,
$$

which is schematic but has the right structure: a second derivative of $\varrho$, a term in the phase's gradient squared, and the algebraic term's derivative. **The second-order character is the scale's, and it is the reason the scale's equation is not a conservation law.**

**The consequence that matters for S4 is a negative one.** Because the scale's equation is second order, there is no spare derivative in it. **The acceleration law cannot be made from the scale's equation directly** — it can only be made from it by taking a *gradient*, which is a different operation and the one the scalar rungs actually use. The distinction is worth stating because "differentiate the equation" and "take its gradient" sound alike and are not: a gradient lowers nothing, it raises the tensor rank, and the acceleration law at the scalar rungs is the gradient of the scale's equation in a specific sense the next section states.

## The Phase: Why Its Equation Is First Order

**The phase is cyclic, so its equation is continuity, and continuity is first order.** Varying $\theta_{\mathrm{pha}}$ gives $\partial_{\imath}J^{\imath}=0$ with $J$ first order in the field, which is [the corpus's continuity equation](the-euler-and-continuity-equations-in-biquaternionic-form.html) at the rung. **The equation is not an approximation and it is not a combination: it is the phase's Euler–Lagrange equation, obtained by the same variation as any other, and its order is one because the phase is cyclic.**

**What continuity does not contain, and this is the article's sharpest negative statement.** Continuity contains the density and the velocity, and the velocity is the phase's gradient — but it contains the phase's gradient *once*, linearly, and it contains no second derivative of the phase. **A first-order equation cannot contain a second derivative**, which sounds trivial and is the hinge of the whole argument: the spare derivative is real only because continuity is first order, and if continuity had been second order the spare derivative would not exist.

**Where the phase's conjugate momentum goes.** The current $J^{\imath}$ is the phase's conjugate momentum, and continuity says it is conserved. **That is the exact content of the first-order equation: a conservation law.** [Noether's Theorem](noethers-theorem-in-biquaternionic-form.html) derives the current from the invariance, and the order statement here is the same fact read as a count: an invariance gives a current, a current is first order, and a first-order equation leaves a derivative.

**The honesty about what continuity conserves, because it changes up the ladder.** At the gradient rungs it conserves the proper density and is a strict conservation law. At the spinor rung it conserves the charge and not the fluid's density. At the vector rung it fails as a conservation law, because the word has no phase coordinate and continuity is an identity whose divergence does not vanish. **The order statement survives all three: in each case the equation is first order. What degrades is what the equation conserves, not its order.** The two facts are independent, and the article keeps them so.

## The Manufacturing, at the Gradient Rungs

**The operation is one line and it is exact.** The guidance relation is

$$
\vec v=\frac{1}{m}\vec\nabla_{\Phi}S ,
$$

first order in $S$. Differentiating it with respect to the time $r'_{t}$ and using the field equation to eliminate $\partial_{t'}S$,

$$
\partial_{t'}\vec v=\frac{1}{m}\vec\nabla_{\Phi}\,\partial_{t'}S
=\frac{1}{m}\vec\nabla_{\Phi}\Bigl(-\frac{1}{2m}\lvert\vec\nabla_{\Phi}S\rvert^{2}-V-Q\Bigr)
=-\bigl(\vec v\cdot\vec\nabla_{\Phi}\bigr)\vec v-\frac{1}{m}\vec\nabla_{\Phi}(V+Q),
$$

which is Euler with the quantum force. **Each equality is a step and each is worth naming.** The first is the guidance relation differentiated — nothing else; it is where the second derivative of $S$ enters. The second substitutes the quantum Hamilton–Jacobi equation, which is the scale's equation. The third identifies $\vec\nabla_{\Phi}S/m$ with $\vec v$ and the gradient of $\tfrac12\lvert\vec\nabla S\rvert^{2}/m^{2}$ with the convective term.

**The three equalities show exactly where the force comes from.** The right-hand side's first term is the convective term — the transport of the velocity by itself; the second is the gradient of the potential and the quantum potential. **The force is the gradient of the scale's equation, and the acceleration is the derivative of the phase's guidance relation, and the two meet in the convective term.** That is the whole of S4 at the gradient rungs, and it is why the corpus's sentence is compressed: "Euler is not varied; it is differentiated" says the first equality, and the rest is substitution.

**The exactness, stated plainly.** The chain is an identity on solutions of the field equation, and it involves no approximation: the substitution in the second equality is the field equation itself, and the third is a renaming. **The article therefore quotes no residual.** There is no numerical check to run, because there is no approximation to test — the identity is algebraic once the field equation is imposed, and a numerical residual would measure the finite-difference step and not the identity.

**The order balance, which is the point.** The guidance relation is first order; its derivative is second order; the field equation is second order; and the third equality replaces a second-order object by another. **The number of derivatives is conserved across the manufacturing, and the reason it can be is that one was spare at the start.** That is what "spare derivative" means and it is the article's name for it.

### What the Third Equality Hides, and Why It Must Be Stated

**The third equality is a renaming, and a renaming can hide a mistake.** It replaces $\vec\nabla_{\Phi}S/m$ by $\vec v$, which is legitimate only where the guidance relation holds — that is, where the phase's gradient *is* the velocity. At a node the phase is undefined and the renaming fails; at a crossing the matrix rung's analogue fails. **The acceleration law therefore inherits the chart's singular locus**, and the article states it because a display that divides by $\varrho$ without saying so is the corpus's most common slip.

**A second thing the renaming hides: the gradient and the derivative do not commute with the flow.** $\partial_{t'}\vec\nabla_{\Phi}S$ and $\vec\nabla_{\Phi}\partial_{t'}S$ agree because partial derivatives commute, and that is not a physical statement but a statement about the chart. In a chart where the flow's velocity depends on position, the material derivative $\mathrm{D}/\mathrm{D}t=\partial_{t'}+\vec v\cdot\vec\nabla_{\Phi}$ is the object that appears, and the convective term is exactly the difference between the material and the partial derivative. **The manufacturing produces the material derivative by itself**, from the product rule, and that is the third of the three kinds of term the next section separates.

## The Three Kinds of Term

**Differentiating a product produces three kinds of term, and the article insists on the separation because merging them is the error the corpus logs.** Take a transport law for a quantity $\mathcal Q$ carried by a flow $v$,

$$
\partial_{t'}\mathcal Q+\partial_{\imath}\bigl(\mathcal Q\,v^{\imath}\bigr)=0 ,
$$

and differentiate it once more. The product rule gives

$$
\partial^{2}_{t'}\mathcal Q+\bigl(\partial_{\imath}\mathcal Q\bigr)\partial_{t'}v^{\imath}+\mathcal Q\,\partial_{\imath}\partial_{t'}v^{\imath}+\dots ,
$$

and the terms are of three kinds.

| kind | the term | what it is | what it is not |
| --- | --- | --- | --- |
| **acceleration** | the second derivative of the transported quantity | the rate of change of the rate of change | — |
| **transport** | the first derivative of $\mathcal Q$ times the flow's derivative | the quantity being carried along a changing flow | — |
| **product-rule** | the term from both $\mathcal Q$ and $v$ varying | a bookkeeping term of the chart | **never a force term** |

**The prohibition, and the reason it is a prohibition rather than a preference.** The product-rule term arises because the differentiation was applied to a product, and it exists in any chart where the transported quantity and the flow both vary. **It is not a force**: it does not vanish when the force vanishes, and it does not appear when the transport law is differentiated in a chart where the flow is constant. **A display that calls it a force term has attributed a chart artefact to the physics**, and the corpus's error log records one such display and its repair.

**At the matrix rung the three kinds have their own names, and the correspondence is exact.** The acceleration is the derivative of the pair momentum; the transport is the commutator with the connection; the product-rule term is the connection's own variation, $\Omega_{kl}\,\partial_{\imath}q_{kl}$. **The third is the one that must not be called a force**, and [The Primordial Force Law](the-primordial-force-law-and-the-two-wong-terms.html) states the three-term balance with the assignment made article by article. The correspondence is worth stating because it shows the three kinds are not a feature of one rung: they are what any differentiation of a transport law produces.

## The Frame Rungs: The Manufacturing Is a Projection

**At the vector and spinor rungs the acceleration law is not a derivative, and the article states this rather than forcing it into the pattern.** The rung's equation is second order in the field, the frame's coordinates are cyclic, and the fluid's acceleration law is the component of the frame's equation *transverse to the flow*.

**Why a projection and not a differentiation, in one paragraph.** The velocity at these rungs is a direction and not a gradient: $A_{\imath}/\varrho$ at the Proca rung, $ic\tilde U_{\Psi,\mathrm b}^{-2}$ at the Dirac rung. **A direction has no potential to differentiate.** There is no $S$ whose gradient is the velocity, so there is no guidance relation of the gradient kind to differentiate, and the spare derivative is not spent the same way. What the rung does have is a second-order equation for the field, and the fluid's acceleration law is its part along the directions the flow selects. **It is a projection because the equation is already second order and the projection is what extracts the fluid's content from it.**

**The projection's price, stated as the fluid article states it.** A projection is defined only where the frame exists and only along the directions the flow selects. **It is therefore the weakest of the three fillings**, and the corpus says so: at the scalar rungs the acceleration law is a variation's consequence, at the frame rungs it is a projection, and only the first is close to a coordinate's equation. The three fillings are not three strengths of one operation; they are three operations, and the article's claim is only that all three are manufacturing rather than variation.

**What the Proca rung's mass term does to the accounting, because it is the sharpest single fact of this section.** The mass term is algebraic in the field and depends on the scale, so the scale is not cyclic and its equation is second order. **The direction is cyclic, so its own equation is a transport — and the rung's Euler equation is the transverse part of the second-order equation for the field.** Two equations of two orders, and the fluid reads the acceleration from the second-order one because the first-order one is the transport. **The article does not claim the projection is a differentiation**, and a reader who wants the projection derived will find it in [The Spin-One Fluid](the-spin-one-fluid.html).

## The Limiting Case: When the Separation Is Total

**At the matrix rung the separation is total, and the spare derivative is spent on a balance.** The word is $\Xi=U_{\mathrm{frm}}PU_{\mathrm{frm}}^{\dagger}$ with $P=\mathrm{diag}(\rho_{1},\dots,\rho_{4})$. The algebraic term is a potential in the eigenvalues, $V(P)$, and it contains no frame. **So the frame is cyclic and the eigenvalues are not** — the same division as at the scalar rungs, one group up, with the frame in the phase's role and the eigenvalues in the scale's.

> The frame's Euler–Lagrange equation is the guidance equation, and it is **algebraic** rather than a divergence: $\Omega_{\imath,kl}=M_{kl}/q_{kl}$ with $M_{kl}$ the pair momentum and $q_{kl}=\rho_{k}-\rho_{l}$. The eigenvalues' equation is second order, $\Box_{\Phi}\rho_{k}$ sourced by the frame.

**Why the frame's equation is algebraic here, and not a divergence as at the scalar rungs.** At the scalar rungs the phase enters through $\partial_{\imath}\theta$, and $\partial_{\imath}\theta$ is a gradient whose divergence is the equation. At the matrix rung the frame enters through the *first-order* covariant derivative $D_{\imath}P$, and the variation with respect to the frame gives an equation relating $\Omega_{\imath}$ to $D_{\imath}P$ *algebraically*. **The equation is first order in the sense that matters — it contains no second derivative — and it is not a divergence, because the object it solves for is a connection and not a gradient.** That is the one place in the ladder where the first-order equation's *shape* differs, and the reason is the rung's action being first order in the frame.

**The manufacturing at the matrix rung is the derivative of that algebraic guidance.** Differentiate $\Omega_{\imath,kl}=M_{kl}/q_{kl}$ and use the eigenvalues' second-order equation, and the result is the pair's momentum balance,

$$
\partial_{\jmath}\Pi_{\imath,kl}=\bigl(\text{curvature term}\bigr)+\bigl(\text{transport term}\bigr)+\bigl(\text{product-rule term}\bigr),
$$

with the three kinds of term assigned exactly as the previous section's table says. **The spare derivative is spent the same way it is at the scalar rungs, on an equation that is first order; only the shape of the first-order equation has changed.**

**And at the matrix rung the manufactured equation is a balance and not a law, which is S5's business and not S4's.** The article says this to keep the steps apart: **S4 produced the equation, and S5 will say what kind of equation it is.** The manufacturing does not know whether the flow is internal; it produces an equation in either case. [Base-Valued versus Internal Flow Velocity](base-valued-versus-internal-flow-velocity-a-test-separating-force-laws-from-momentum-balances.html) is the article that reads the result.

## The Counterfactual: What Happens if the Phase Is Not Cyclic

**A coordinate that appears algebraically in the algebraic term is not cyclic, and the article can say exactly what that costs because the corpus has a case.** A phase with a potential — $V$ containing $\cos\theta_{\mathrm{pha}}$, as a Josephson or an axionic coupling would — makes $\partial L/\partial\theta\neq0$, so the phase's equation is no longer $\partial_{\imath}J^{\imath}=0$ but

$$
\partial_{\imath}J^{\imath}=\frac{\partial V}{\partial\theta_{\mathrm{pha}}} .
$$

**The equation is still first order, and the source is algebraic.** The spare derivative survives, because the right-hand side carries no derivative of $\theta$. **So the counterfactual's answer is narrow and it is worth stating precisely: a phase potential does not destroy the spare derivative, it gives continuity a source.** The acceleration law is unchanged in its structure and gains the potential's gradient in the force.

**A stronger counterfactual, which does destroy the spare derivative.** If the phase entered the kinetic term *twice differentiated* — a higher-derivative action — then its equation would be second order and continuity would not be a conservation law. **The corpus has no such rung**, and the article states the counterfactual only to mark where the argument's premise is used: the spare derivative exists because the kinetic term is first order in every cyclic coordinate, and a rung that broke that would break S4.

**The general statement, and it is the article's conclusion in one line.** *The order of a coordinate's equation is decided by whether the action contains the coordinate, and the acceleration law is manufactured from the coordinates it does not contain.* A rung's force slot is therefore a statement about the action's algebraic term: the more coordinates the algebraic term touches, the fewer spare derivatives the rung has, and the weaker its acceleration law's warrant.

## The Classical Layer: Where There Is Nothing to Spend

**The ordinary fluid is the case in which S4 has a first-order equation and still manufactures nothing, and the reason is worth stating because it fixes what "manufactured" means.** The classical equations are the base — *The fluid's equations and their solutions* in *Biquaternion Universe Non Relativistic Non Quantum Approximation* — and they are written on a flow element whose temporal slot carries the constant $ic$:

$$
\tilde V_\Phi=i c\,e_t+\vec v .
$$

There is no phase coordinate in that element and therefore no coordinate whose equation sits one order below anything. What the classical fluid has instead is a *trajectory*, and the derivative along it is the pairing

$$
\bigl\langle\tilde V_\Phi,\tilde\nabla_\Phi f\bigr\rangle_{\natural}=\partial_{t'}f+\vec v\cdot\nabla f=\mathrm{D}_{\mathrm{mat}}f ,
$$

which is the material derivative for every differentiable $f$ and every flow. Euler's equation is then $\mathrm{D}_{\mathrm{mat}}\tilde V_\Phi=-\vec\nabla_\Phi p_{\mathrm{th}}/\rho_{\mathrm{mass}}+\vec f_{\mathrm{ext}}$, and it holds because the left-hand side *is* the acceleration of the markers by definition. So the manufacturing step at the classical layer returns a definition, and the whole content of the equation is on the right-hand side. That is the degenerate case of S4, and it is why a classical fluid needs the pressure as an extra datum: nothing in the algebra supplies it.

**The difference from the field is the constant on the temporal slot, and it is the whole difference.** When the slot carries a phase, its time derivative is a frequency, the guidance relation is first order in that phase, and differentiating it produces a second-order equation with a force slot to fill. When the slot carries $ic$, the first-order statement is continuity — a divergence of a current — and differentiating a divergence does not produce an acceleration law. The spare derivative is not scarce in the first case and not present at all in the second, and this is the same fact as the empty temporal slot of the count.

**The algebra's product says the same thing from the other side.** The quaternion product of the flow with the gradient is $c\partial_{r'_t}f-\vec v\cdot\nabla f$, the material derivative with the convective term reversed, and that is why the fluid's natural bilinear is the pairing $\langle\cdot,\cdot\rangle_{\natural}$ and not the product. The product is the operation that, acting on an element, manufactures a law from a first-order statement; a classical fluid cannot use it, and the object that can is the one the fluid will be replaced by.

**Viscosity is the second classical statement, and it is the opposite failure.** The dissipative term has a fixed sign under $t'\mapsto-t'$ while any term manufactured from an action is even under it, so no differentiation of a first-order transport law can produce it; the force is inserted on the right-hand side, with Rayleigh's dissipation function as the symbol of the insertion. So the classical layer exhibits both boundaries of S4 — a first-order equation with nothing below it, and a term with nothing above it — and the two are one absence seen twice: there is no action whose phase could be the spare coordinate.

**The one-dimensional linearisations do not restore a spare derivative, and it is worth saying so because they look as if they do.** Hopf's transformation carries Burgers' equation into the heat equation, and the Korteweg–de Vries soliton into a linear problem at the other end; both are changes of variable, not variations, and the Burgers case works only for potential flow, because the vector identity it uses is the gradient of the scalar one and a rotational flow is untouched by it. A change of variable that solves an equation is not a spare derivative that produces one, and the criterion of this section is about production.

## The Order Table Across the Ladder

**The article's accounting is one table, and the table is the reason the ladder's five fluids look as different as they do.** Read down a row and it is one rung's order structure; read across a column and it is one order property at five rungs.

| rung | cyclic coordinates | the first-order equation | the second-order equation | the manufacturing |
| --- | --- | --- | --- | --- |
| Schrödinger | phase | continuity | amplitude, the quantum Hamilton–Jacobi equation | gradient of the amplitude's equation, after differentiating the guidance relation |
| Klein–Gordon | phase | continuity | amplitude, the mass shell | the same, with $\gamma^{-1}$ in the force |
| Dirac | phase, rotor | charge continuity; the rotor's transport | the bispinor's equation (rank 3 of 4) | projection of the frame's equation along the flow |
| Proca | the direction | the direction's transport | the field's equation, second order in $A$ | transverse projection of the frame's equation |
| $\mathrm{SU}(4)$ | the frame | the guidance equation, algebraic | the eigenvalues' equation, $\Box_{\Phi}\rho_{k}$ sourced | derivative of the algebraic guidance |

**One column shows the pattern and the other shows the exceptions, and the article needs both.** The *cyclic coordinates* column has one entry at the scalar rungs, two at the spinor rung, one at the vector rung and one at the matrix rung. **The number of first-order equations is the number of cyclic coordinates, at every rung**, and that is the accounting's only invariant. The *manufacturing* column has three different operations and no invariant — which is the article's honesty: the spare derivative is always there, and what is done with it is a fact about how the rung encodes the velocity.

**The Dirac rung is the one entry that needs a footnote, and the footnote is about rank rather than order.** Its action is first order, so its Hessian vanishes and the order language must be replaced by the kinetic matrix's rank; the rotor's transport is first order and the bispinor's equation has rank three of four. **The accounting survives — there is a first-order equation and a spare derivative — and the test that decides whether the rung closes is the rank test, which is [the criterion's](criterion-for-a-fluid-equation-one-polar-coordinates-euler-lagrange-equation.html) subject and not this article's.** The article flags it rather than absorbing it, because a claim that the order accounting covers the spinor rung would be a claim about rank that the order accounting cannot make.

**What the table shows that no single rung's derivation shows.** That the acceleration law's *warrant* is a function of the order structure alone: every rung with a cyclic coordinate has a spare derivative, and every rung spends it on the acceleration law. **The three operations differ because the rungs encode the velocity differently, and not because the rungs differ in how much they can prove.** A reader who thought the scalar rungs' Euler was "more derived" than the vector rung's Euler now has the precise sense in which that is true: the scalar rung's manufacturing is a differentiation of an equation of motion, and the vector rung's is a projection of one.

## What This Article Does Not Claim

**That "Euler is differentiated" is a derivation of a new law.** It is a derivation of an equation already implied by the rung, and the implication is exact. The article's claim is about where the equation comes from, not about whether it is true.

**That every rung's acceleration law is obtained by differentiation.** The vector and spinor rungs' is a projection, and the article states this three times because a reader who takes "manufacturing" as a synonym for "differentiation" will misread the table.

**That the spare derivative is a conserved quantity in any deeper sense.** The phrase names an order count: a first-order equation has one derivative fewer than a second-order one, and the article uses the phrase as bookkeeping. It is not a Noether charge, and no conservation law is claimed for it. **What is conserved is the number of derivatives across the manufacturing**, and that is an identity about the operations, not a physical conservation law.

**That the order accounting replaces the rank test.** The Dirac rung passes the order accounting and fails rank; the article states this and does not repair it. **A complete declension runs both tests**, and the corpus's ladder table is where both verdicts are recorded.

**That the counterfactual with a phase potential is a corpus result.** The Josephson-type coupling is named as the shape a non-cyclic phase would take, and the corpus does not contain such a rung. The counterfactual is stated to mark the premise, not to claim a derivation.

**That the three kinds of term are exhaustive.** The three are what differentiating a transport law of the displayed form produces. A transport law with a source, a nonlocal term or a constraint produces others, and the prohibition the article states — the product-rule term is never a force — is the part that survives.

## Open Questions

**Does the order accounting extend to a rung whose algebraic term depends on the frame?** A potential built from a unit element is constant, so the frame is cyclic for a structural reason — but a term depending on the frame through a *non-invariant* contraction, or through an auxiliary field, could break that. Whether such a term is admissible in the corpus's action is not settled, and if it were, S4 would have one fewer spare derivative at that rung.

**What is the manufacturing at a rung with two cyclic coordinates of different types?** The Dirac rung has the phase and the rotor, and their first-order equations are of different shapes — a divergence and a transport. **The rung therefore has two spare derivatives, and the article has not said how they are spent.** The fluid article treats the rotor's transport as the spin's equation and the phase's as charge continuity, and whether the spin's contribution to the acceleration comes from the rotor's spare derivative or from the projection is not stated anywhere.

**Is the projection at the vector rung a limit of the differentiation at the scalar rungs?** A gradient is a direction in the degenerate sense that it is parallel to itself, and a projection onto the transverse part is the operation that extracts the part orthogonal to the flow. **If the gradient rungs' manufacturing were the transverse projection of the quantum Hamilton–Jacobi equation's gradient, the three operations would be two**, and the article's claim would be stronger. The corpus does not have the computation, and the article does not assume the answer.

**Does the accounting survive a background that is not flat?** The material sector's gradient is flat in every rung of the corpus, and a curved background would replace $\partial_{\imath}$ by a covariant derivative and introduce a connection in the scale's equation. **Whether the cyclic/acyclic division is then still a division of coordinates, or becomes a division of covariant derivatives, is open.**

## What This Article Adds and What It Relabels

**Adds.** The spare derivative as a named object, with its definition as the order count a cyclic coordinate's equation leaves unspent; the **order accounting of the word** — three of four coordinates cyclic, one not, and the structural reason the frame and the phase are cyclic while the scale is not; the **order of an equation read off the Euler–Lagrange equation's first term**, so that cyclicity and order are the same statement; the **three manufacturing operations** stated side by side with the rung that takes each; the **sharpest negative statement** — the second derivative of the fast coordinate appears in the force slot and nowhere else; the **three kinds of term** with the product-rule prohibition and its matrix-rung correspondence; the **order table across the ladder** with the invariant (first-order equations equal cyclic coordinates) and the non-invariant (the manufacturing operation); and the **counterfactual** that a phase potential sources continuity without raising its order, while a twice-differentiated phase would destroy the spare derivative.

**Does not add.** No new equation, no new solution, no numerical residual. The chain in the manufacturing section is an identity on solutions and the article says so rather than quoting a check.

**Relabels.** *"Euler is the gradient of the Hamilton–Jacobi equation"* — true and incomplete: it is the gradient of the scale's equation *after* the guidance relation has been differentiated, and the differentiation is where the second derivative of the phase enters. *"The phase's equation is continuity"* — true, and its content is that the phase is cyclic; the article makes the cyclicity the reason and the continuity the consequence. *"The frame is cyclic"* — true at four rungs of five, and the article names the exception rather than generalising.

## Summary

**The acceleration law of every fluid in this corpus is manufactured, not varied, and the manufacturing consumes a derivative that the polar word left spare.** The word makes the phase and the frame cyclic: they appear in the action only through their derivatives, so their Euler–Lagrange equations are conservation laws one order below the field equation's. The scale is not cyclic, because the algebraic term depends on it, so its equation has the field equation's order. **A first-order equation leaves one derivative unspent, and the acceleration law is made from it.**

**Three operations do the manufacturing, and the article states which rung takes which.** At the gradient rungs the guidance relation $\vec v=\vec\nabla S/m$ is differentiated and the quantum Hamilton–Jacobi equation substituted, and the result is Euler with the quantum force. At the matrix rung the algebraic guidance $\Omega_{kl}=M_{kl}/q_{kl}$ is differentiated and the eigenvalues' equation substituted, and the result is the pair's momentum balance. At the vector and spinor rungs the field's second-order equation is projected transverse to the flow, because a direction has no potential to differentiate.

**The sharpest form of the claim is a negative one.** The second derivative of the fast coordinate appears in the force slot and nowhere else: continuity has only first derivatives, the quantum Hamilton–Jacobi equation has only first derivatives of the phase, and the acceleration law is the only equation that contains $\partial_{t'}\partial_{\imath}S$.

**The three kinds of term a differentiation produces are not interchangeable, and the product-rule term is never a force.** At the matrix rung the three are the derivative of the pair momentum, the commutator with the connection, and $\Omega_{kl}\partial_{\imath}q_{kl}$, and the last is the one the corpus logs as having been mislabelled.

**The order table is the article's accounting and its honesty.** The number of first-order equations equals the number of cyclic coordinates at every rung, and that is the invariant. The manufacturing operation is not invariant, and the article says so: the spare derivative is always there, and what is done with it is a fact about how the rung encodes the velocity.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\varrho$, $\theta_{\mathrm{pha}}$, $S$ | the scale, the phase and the action $S=\tfrac{h}{2\pi}\theta_{\mathrm{pha}}$ |
| $\tilde U_{\Psi,\mathrm b}$, $\tilde u_{\mathrm r}$ | the boost and the rotor; cyclic at every rung where they exist |
| $q$, $\partial L/\partial q$ | a coordinate and the term that decides its equation's order |
| $J^{\imath}$ | a cyclic coordinate's conjugate current; first order by construction |
| cyclic | a coordinate the Lagrangian does not contain, only its derivatives |
| spare derivative | the one derivative a first-order equation leaves unspent |
| $Q$ | the quantum potential; the scale's equation's contribution to the force |
| $\Omega_{\imath}$, $M_{kl}$, $q_{kl}$ | the matrix rung's internal velocity, pair momentum and inertia |
| $\Pi_{\imath,kl}$ | the matrix rung's pair momentum flux |

## Further Reading

- [Five Steps from a Lagrangian to Fluid Equations](five-steps-from-a-lagrangian-to-fluid-equations.html), where this article is S4 and the order accounting is one step of five.
- [Differentiating a First-Order Transport Law: Force, Transport and Product-Rule Terms](differentiating-a-first-order-transport-law-force-transport-and-product-rule-terms.html), the three kinds of term in full, with the prohibition stated as a rule.
- [Criterion for a Fluid Equation](criterion-for-a-fluid-equation-one-polar-coordinates-euler-lagrange-equation.html), the rank test this article sets aside, and the ladder table where both verdicts are recorded.
- [The Euler and Continuity Equations in Biquaternionic Form](the-euler-and-continuity-equations-in-biquaternionic-form.html), the classical layer's acceleration law, against which the scalar rungs' manufacturing is read.
- [Noether's Theorem in Biquaternionic Form](noethers-theorem-in-biquaternionic-form.html), the invariance that gives a cyclic coordinate its current, and therefore its first-order equation.
- [The Spin-One Fluid](the-spin-one-fluid.html), the transverse projection derived, which this article does not derive.
