# __The Coupled Dirac Equation in Biquaternionic Polar Variables__

## Introduction

This article substitutes the polar word into the coupled Dirac equation and reads what the substitution makes visible. It is the polar companion of *The Coupled Dirac Equation in Biquaternionic Form*, and it depends on three articles: the element form of the coupled equation for the equation, *The Dirac Equation in Biquaternionic Polar Variables* for the word and the four brackets, and *The Covariant Derivative and Gauge Connection in Biquaternionic Form* for the connection.

**The substitution.** Write

$$
\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
$$

with $r>0$, $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$, $\theta_{\mathrm{rpd}}\ge0$ the rapidity of the boost $\tilde U_{\Psi,\mathrm b}$, and $\theta_{\mathrm{axr}}\in[0,2\pi)$ the angle of the rotor $\tilde u_{\mathrm r}$. The word is a bijection onto the N-regular set, so the eight real parameters are coordinates on the units and no constraint is lost or added. The parent states this and the article uses it.

**The equation.** The coupled pair is

$$
\tilde\nabla_{\mathrm{gco}}\tilde\Xi_R=k_m\tilde\Xi_L,
\qquad
\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\Xi_L=k_m\tilde\Xi_R,
\qquad
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi .
$$

Here $\tilde A_\Phi=A_te_t+\sum_\eta A_\eta\vec e_\eta$ is the potential biquaternion, an element of the material sector $\mathbb{B}_\Phi$, with central scalar coefficients in the abelian case. That centality is the single fact the whole article turns on.

**Three things are established, and they are local statements.**

*First, the coupling enters the logarithmic derivative as one added four-vector.* Because each component of the connection is a central scalar, $\frac{iϙ}{\hbar}\tilde A_\Phi$ passes through $\tilde\Xi^{-1}$ and joins the four brackets without disturbing their types. It lands in the phase bracket and in the boost bracket and in neither of the other two.

*Second, the shift is the classical substitution, in one object.* The scalar potential and the vector potential are the temporal and spatial slots of one element, so $E\mapsto E+ϙ\phi$ and $\vec p\mapsto\vec p+ϙ\vec A$ are not two substitutions. They are the addition of $\frac{ϙ}{\hbar}\tilde A_\Phi$ to the covariant wavevector, and the algebra states them with one sign.

*Third, the spin transport is what the chart does and does not show.* The connection is central per component, so it multiplies the word and cannot rotate either frame factor. The rotor's own rate is the mass term's and the coupling leaves it alone. What the background does to the spin is indirect and is recorded as the chart's limit.

**Where the polar equation is closed, and where it is not.** The polar equation is the free pair rewritten in variables. It is exact, it is equivalent to the element form, and it closes for a plane wave in a constant background, where the frame is constant and the equation becomes algebraic in it. It does not close for a general field: the four brackets are coupled and the equation constrains them without fixing them. That underdetermination is the spin-fluid underdetermination of the parent and not a defect introduced by the coupling. The constraint structure proper enters when the *action* is asked for, and that is the variational polar companion.

**What is not here.** The action, the Euler–Lagrange equations and the constraint analysis are not in this article. The current is not derived here; the element-form companion settles it and this article states the polar reading of the same numbers in one paragraph. The article's subject is the equation and its variables.

## The Coupling in Polar Variables

Differentiate the word and divide by it, as the parent does, and add the connection. Because $\tilde A_\Phi$ is central per component, the two operations commute with the split.

**The logarithmic derivative, coupled.**

$$
\tilde\Xi^{-1}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi
=\tilde\Xi^{-1}\frac{\partial\tilde\Xi}{\partial R_\mu}+\frac{i\,ϙ}{\hbar}A_\mu
=\frac{1}{2}\frac{\partial\ln\rho}{\partial R_\mu}
+i\frac{\partial\theta_{\mathrm{pha}}}{\partial R_\mu}
+\frac{i\,ϙ}{\hbar}A_\mu
+\tilde u_{\mathrm r}^{-1}\Bigl(\tilde U_{\Psi,\mathrm b}^{-1}\frac{\partial\tilde U_{\Psi,\mathrm b}}{\partial R_\mu}\Bigr)\tilde u_{\mathrm r}
+\tilde u_{\mathrm r}^{-1}\frac{\partial\tilde u_{\mathrm r}}{\partial R_\mu}.
$$

The added term is one central complex number per component, and the four terms after it are the parent's four brackets unchanged in form.

**Which brackets the connection touches.** Decompose the added term with $\tilde A_\Phi=A_te_t+\sum_\eta A_\eta\vec e_\eta$. Its temporal slot is $\frac{iϙ}{\hbar}A_t$, a central imaginary number; its spatial slots are $\frac{iϙ}{\hbar}A_\eta\vec e_\eta$, which are Hermitian vector parts because $i$ times a real vector is Hermitian. Hence

$$
\frac{i\,ϙ}{\hbar}\tilde A_\Phi
=\underbrace{\frac{i\,ϙ}{\hbar}A_t}_{\text{central imaginary}}
+\underbrace{\frac{i\,ϙ}{\hbar}\sum_\eta A_\eta\vec e_\eta}_{\text{Hermitian vector}} .
$$

The connection therefore adds to the **phase bracket** and to the **boost bracket** and to nothing else. The scale bracket and the rotor bracket are untouched, and that is a statement of type and not of size: a central scalar cannot produce a real vector part, and it cannot produce a scale.

**The type table, with the coupling in place.**

| bracket | type | the connection's share |
| --- | --- | --- |
| $\tfrac12\partial_\mu\ln r^{2}$ | real central scalar | none |
| $i\partial_\mu\theta_{\mathrm{pha}}+\frac{iϙ}{\hbar}A_\mu$ | central imaginary | the whole temporal slot of $\frac{iϙ}{\hbar}\tilde A_\Phi$ |
| $\tilde u_{\mathrm r}^{-1}(\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b})\tilde u_{\mathrm r}$ | Hermitian | the whole spatial slot of $\frac{iϙ}{\hbar}\tilde A_\Phi$ |
| $\tilde u_{\mathrm r}^{-1}\partial_\mu\tilde u_{\mathrm r}$ | real vector part | none |

**The one-line reason.** The connection is a material-sector element, and the material sector is the central imaginary plus the real vector; multiplying by $i$ carries it into the central imaginary plus the Hermitian vector, which are brackets two and three. The scale and the rotor are the two brackets a multiplication by a central scalar cannot reach.

**What that buys, and what it costs.** It buys a clean statement of where the potential can act: on the momentum and on the velocity, never on the density and never on the spin direction. It costs the expectation that the potential could turn the spin: in this chart it cannot, and §*The Spin Transport* records the consequence.

## The Kinetic Momentum

The phase gradient is the four-momentum, and the coupling shifts it.

**The gradient, with the connection.** Adding the temporal slot of $\frac{iϙ}{\hbar}\tilde A_\Phi$ to the phase bracket gives

$$
i\frac{\partial\theta_{\mathrm{pha}}}{\partial R_\mu}+\frac{i\,ϙ}{\hbar}A_\mu
=i\frac{\partial}{\partial R_\mu}\Bigl(\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\Lambda\Bigr)
\qquad\text{whenever}\qquad A_\mu=\frac{\partial\Lambda}{\partial R_\mu},
$$

so a pure-gauge potential is absorbed by a reparameterisation of the angle and by nothing else. That is the polar statement of gauge invariance, and it is a statement about the *angle* and not about the field.

**The momentum.** With $\vec p=\hbar\nabla\theta_{\mathrm{pha}}$ and $E=-\hbar c\,\partial\theta_{\mathrm{pha}}/\partial r'_t$ the free reading, the coupled reading is

$$
\tilde K_{\Phi,\mathrm{gco}}=\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_\Phi,
\qquad
\tilde K_\Phi=i\frac{E}{\hbar c}e_t+\frac{\vec p}{\hbar}.
$$

Slot by slot this is

$$
\hbar c\,\kappa_t=E+ϙ cA_t,
\qquad
\hbar\vec\kappa=\vec p+ϙ\vec A,
$$

where $\kappa_t$ and $\vec\kappa$ are the components of the covariant wavevector. **The whole of the classical substitution is one addition**, because the scalar and vector potentials are the temporal and spatial slots of one element of $\mathbb{B}_\Phi$. No second rule is needed and no sign can be chosen independently.

**Which of the two is the momentum.** The chart does not by itself decide whether $\tilde K_\Phi$ or $\tilde K_{\Phi,\mathrm{gco}}$ is "the" momentum; it states both and states their relation. The physical momentum is the one the velocity is built from, and the velocity is the boost's, which is §*The Kinetic Velocity*. The naming is settled there and not here.

**The local character of the statement.** The gradient of the angle is defined at each event, so the shift is a local statement and not an integrated one. This is the polar form's genuine addition over the element form: in the element form the potential appears as a term in the operator; here it appears as a shift of a gradient that can be read off at a point. The two are the same content and they are not the same display.

**What the polar statement does not say.** It does not say that the phase is observable. The angle is a coordinate of the word and the gauge transformation moves it; only differences of the covariant wavevector along a path, and the curvature, are invariant. §*The Gauge-Invariant Reparameterisation* states which combinations survive.

## The Kinetic Velocity

The boost is the velocity, and the coupling does not touch the boost.

**The velocity is read from the covariant wavevector.** The parent's mass-shell proposition says that a field whose wavevector satisfies $\tilde K_\Phi\tilde K_\Phi^{\natural}=-k_m^{2}$ has $\tilde K_\Phi=ik_m\tilde U_{\Psi,\mathrm b}^{-2}$ for a boost. With the coupling the same proposition applies to the covariant wavevector:

$$
\tilde K_{\Phi,\mathrm{gco}}=ik_m\,\tilde U_{\Psi,\mathrm b}^{-2},
\qquad
\tilde V_\Phi=ic\,\tilde U_{\Psi,\mathrm b}^{-2},
\qquad
\vec v=c\tanh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b},
\qquad
\gamma=\cosh\theta_{\mathrm{rpd}}.
$$

The boost in the word is therefore the one the *covariant* wavevector names. The canonical wavevector is the covariant one less the potential:

$$
\tilde K_\Phi=\tilde K_{\Phi,\mathrm{gco}}-\frac{ϙ}{\hbar}\tilde A_\Phi .
$$

**What that says in one sentence.** The velocity is kinetic: it is built from the wavevector the background leaves, and the potential sits entirely in the canonical wavevector. This is the classical statement $\vec p_{\mathrm{kin}}=\vec p_{\mathrm{can}}-ϙ\vec A$, and the chart states it as a property of which wavevector names the boost.

**Why the radius does not move.** The added term is central per component and of first degree in the field. It cannot rescale $r$, and it cannot change the magnitude of the boost's rapidity by itself: it shifts the wavevector, and the rapidity is then read from the shifted wavevector by the same mass-shell identity. The invariant is

$$
\tilde K_{\Phi,\mathrm{gco}}\tilde K_{\Phi,\mathrm{gco}}^{\natural}=\kappa_t^{2}-|\vec\kappa|^{2}=-k_m^{2},
$$

and in canonical components it is

$$
\Bigl(\frac{E+ϙcA_t}{\hbar c}\Bigr)^{2}-\Bigl|\frac{\vec p+ϙ\vec A}{\hbar}\Bigr|^{2}=-k_m^{2}.
$$

**The same translated hyperboloid as in the element form.** The radius is $k_m$ and the potential moves the centre. A constant potential therefore shifts every level and opens no gap, and the polar reason is the one-line reason of the element form: a shift of a variable cannot change a radius.

**The velocity is a unit for every field.** $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$ holds whatever the coupling, because the boost is a unit by construction and the density is a separate factor. The coupling does not enter that line at all, which is the chart's way of saying that the four-velocity is kinematical.

**The strongest objection, and the answer.** The objection is that the chart has merely renamed: the covariant wavevector is defined as the canonical one plus the potential, so saying that "the boost is carried by the covariant wavevector" is a definition and not a result. The objection is correct as far as it goes, and the answer is the one the parent gives for the mass shell: what the proposition fixes is the *direction of the reading*. Read from the potential to the frame, the coupling changes the boost, hence the velocity; read from the frame to the potential, the velocity is what survives when the potential is removed. The chart states the identity, and the physical naming is the corpus's convention and not a consequence of the algebra.

## The Gauge-Invariant Reparameterisation

The angle is a coordinate, so the gauge transformation is a change of coordinate on the same field. The invariant content is what survives it.

**The transformation in the chart.**

$$
\theta_{\mathrm{pha}}\longmapsto\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\Lambda,
\qquad
\tilde A_\Phi\longmapsto\tilde A_\Phi-\tilde\nabla_\Phi\Lambda,
\qquad
r,\ \tilde U_{\Psi,\mathrm b},\ \tilde u_{\mathrm r}\ \text{fixed}.
$$

Only the angle moves. The scale, the boost and the rotor are gauge invariant by inspection, because a central scalar phase cannot change a modulus, cannot change a rapidity and cannot turn a rotor.

**The covariant wavevector is invariant.**

$$
\tilde K_{\Phi,\mathrm{gco}}\longmapsto\tilde\nabla_\Phi\Bigl(\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\Lambda\Bigr)+\frac{ϙ}{\hbar}\bigl(\tilde A_\Phi-\tilde\nabla_\Phi\Lambda\bigr)=\tilde K_{\Phi,\mathrm{gco}} .
$$

**The invariant is the curvature.** Define $\tilde F:=\tilde\nabla_\Phi^{\natural}\tilde\nabla_{\mathrm{gco}}$ restricted to its vector part; the operator identity of the covariant-derivative article gives

$$
\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}=\sum_\mu\tilde\nabla_{\mathrm{gco},\mu}^{2}+\frac{i\,ϙ}{\hbar}\tilde F,
$$

and $\tilde F$ is unchanged by the transformation, since a gradient can be absorbed and a field strength cannot. In the abelian case $\tilde F$ is the Maxwell biquaternion of *Maxwell's Equations in the Biquaternionic Formulation*.

**What the chart's invariants are, in one list.** The radius $r$; the rapidity $\theta_{\mathrm{rpd}}$ and the axis $\vec u_{\mathrm b}$; the rotor angle $\theta_{\mathrm{axr}}$ and its axis; the covariant wavevector $\tilde K_{\Phi,\mathrm{gco}}$; and the curvature $\tilde F$. The angle $\theta_{\mathrm{pha}}$ is a coordinate and not an invariant, and its gauge class is the physical statement.

**The field's frame factor is gauge invariant and this is the chart's cleanest sentence.** Since the gauge transformation multiplies the word by a central scalar, the frame factors $\tilde U_{\Psi,\mathrm b}$ and $\tilde u_{\mathrm r}$ are untouched. The three things the chart calls frame — the boost, the rotor, and their product — are therefore exactly the gauge-invariant part of the field's decomposition, and the phase is exactly the gauge-dependent part. That is a sharper statement than the element form can make, and it is the reason the polar chart is worth having.

**One qualification.** The word is a bijection onto the N-regular set and the transformation preserves the set, so the transformed field is again N-regular and again has a word. No chart breaks under the transformation. What can break is the *smoothness*: a transformation with a singularity in $\Lambda$ gives a word that leaves the chart's range at a point, and the parent records the range restrictions for that reason.

## The Spin Transport

The rotor is the spin and the coupling does not turn it.

**The parent's statement.** The spin direction is $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$, the rotor's bracket is the fourth of the four, and the rotor's own rate is set by the mass term: in a moving frame the rotor precesses relative to the boost, and at rest it does not. The parent states the precession, its rate, and the frame in which it is canonical.

**What the connection can do to it.** Nothing direct. The connection is central per component, and a central multiplication acts on the word as a whole; it cannot reach inside the product $e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ to change one factor and not the others. The fourth bracket is therefore untouched by the coupling, as the type table of §*The Coupling in Polar Variables* records.

**The consequence, stated plainly.** In this chart the magnetic moment is not a rotor rotation. The coupling enters the momentum bracket and the boost bracket; the spin's own transport is the free one. A reader who expects the chart to show Larmor precession as a rotor equation will not find it, and the absence is structural rather than an oversight.

**What the background does to the spin is indirect.** It curves the boost, and the spin's transport follows the boost's. Where the trajectory bends, the frame in which the rotor's rate is zero bends with it, and the observed precession is the composition of the rotor's own rate with the transport of the frame. That composition is what the standard theory calls Thomas precession, and the biquaternionic account of it is *The Classical Origin of $g=2$ in Biquaternionic Form*, where the expansion is carried out and the two contributions are shown to combine to the Larmor rate with the ratio two.

**Why the chart cannot do more.** The chart's variables are four brackets of four types, and the coupling is confined to two of them by type. A precession of the spin direction would have to be a term in the fourth bracket, and no central element can produce one. The polar chart therefore does not derive the spin's dynamics in a background; it locates the spin and the momentum in different brackets and leaves the coupling to the momentum. That is a real limit on what the polar equation says, and the article prefers to state it rather than to dress it up.

**What survives exactly.** The spin's *kinematics* is exact and gauge invariant: $\hat s$ is a function of the rotor alone, the rotor is gauge invariant, and the spin direction is therefore an observable of the chart with no gauge ambiguity at all. That is more than the element form states, and it is the polar form's contribution to the spin question.

## What the Polar Form Adds, and What It Does Not

**Adds.**

- A local reading of the kinetic momentum: the potential shifts the phase gradient, and the shift is visible at each event (§*The Kinetic Momentum*).
- One object for the whole classical substitution: $\frac{ϙ}{\hbar}\tilde A_\Phi$ carries the scalar and the vector potential together, and the two signs cannot be chosen independently (§*The Kinetic Momentum*).
- A direct statement of the kinetic velocity: the boost is named by the covariant wavevector, and the canonical one is the covariant one less the potential (§*The Kinetic Velocity*).
- The gauge-invariant split of the field: the phase is the gauge-dependent part, the three frame factors are the gauge-invariant part (§*The Gauge-Invariant Reparameterisation*).
- The type table, which says in advance where a central connection can act and where it cannot (§*The Coupling in Polar Variables*).

**Does not add.**

- No new solution. The field is the element form's and the word is a re-coordinatisation of it.
- No new prediction. The equation is the coupled equation of the element form, written in eight real coordinates.
- No derivation of the current beyond the element form's: the chart's current is $J^t=\rho\cosh\theta_{\mathrm{rpd}}$, $J^\eta=\rho\sinh\theta_{\mathrm{rpd}}u_{\mathrm b,\eta}$, which is the same object in the chart's letters.
- No spin dynamics in a background, as §*The Spin Transport* states.
- No closure of the general case: the four brackets are coupled and the chart does not close them.

**The ledger in one paragraph.** The polar coupled equation is the element coupled equation with the word substituted, and the substitution buys three things: the potential as a shift of a gradient, the velocity as the kinetic one, and the field's split into a gauge part and a gauge-invariant part. It buys nothing else. In particular it does not buy a spin equation in the background, and it does not buy any statement about the constraint structure of the field, which is a property of the action and not of the equation. The article that follows this one in the coupled quartet substitutes the word into the *action* instead, and the constraint structure appears there.

## Open Questions

**The spin in the background.** Whether a polar formulation exists in which the fourth bracket carries a coupling term is not settled. The obstacle is stated here as a fact of type: a central connection cannot produce a real-vector contribution, so any such term would need a non-central connection or a different arrangement of the word, and both are beyond the abelian construction. Whether the arrangement exists is open.

**The general field.** The four brackets are coupled and the equation does not close them. The parent records the same underdetermination in the free case. Whether a closure condition can be added — a spin-transport equation chosen on principle rather than by convenience — is the parent's open question and the coupling does not settle it.

**The word's range under gauge transformations.** A gauge transformation with a singular $\Lambda$ carries the word out of its chart's range at the singular set. Whether the range restrictions have a physical reading, or whether they are an artefact of the chart, is not settled here.

**The relative phase and the chart's parameter count.** The mass breaks the relative phase of the two parts (§*The Field and Its Phase Symmetry* of the element companion), and the word has no parameter for that phase. Whether the absence is a genuine statement — that the relative phase is not a degree of freedom of the N-regular set — or a limitation of the chosen bijection is open.

## Summary

The coupled Dirac equation in polar variables is the pair $\tilde\nabla_{\mathrm{gco}}\tilde\Xi_R=k_m\tilde\Xi_L$ and $\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\Xi_L=k_m\tilde\Xi_R$ with $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$, and the word $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ substituted into it.

The coupling enters the logarithmic derivative as one added element, $\frac{iϙ}{\hbar}\tilde A_\Phi$. Because that element is central per component, it lands in the phase bracket and in the boost bracket and in neither of the other two. The scale and the rotor are untouched by type, not by accident.

The phase bracket carries the momentum, and the coupling shifts it: $\tilde K_{\Phi,\mathrm{gco}}=\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_\Phi$, which is $E\mapsto E+ϙcA_t$ and $\vec p\mapsto\vec p+ϙ\vec A$ in the slots. One element, one sign, no independent choice.

The boost bracket carries the velocity, and the boost is named by the covariant wavevector, so the velocity is the kinetic one and the canonical wavevector is the covariant one less the potential. The mass shell is $\kappa_t^{2}-|\vec\kappa|^{2}=-k_m^{2}$, a translated hyperboloid of unchanged radius: no constant potential opens a gap.

The gauge transformation moves the angle and nothing else, so the covariant wavevector and the frame factors are gauge invariant and the phase is not. The invariant is the curvature.

The spin is the rotor, the rotor is gauge invariant, and the connection cannot turn it. The spin's transport in a background is indirect, through the boost, and the polar chart does not derive it; that is the chart's honest limit and the g=2 article's subject.

The polar equation is the free pair in variables. It closes for a plane wave in a constant background and it does not close for a general field. The constraint structure enters when the action is asked for, in *The Variational Principle and the Coupled Dirac Equation in Biquaternionic Polar Variables*.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The word: scale, central phase, boost, rotor |
| $r>0$ | Scale; $\rho=r^{2}\cosh\theta_{\mathrm{rpd}}$ is the density |
| $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ | Central phase; **the gauge-dependent coordinate** |
| $\theta_{\mathrm{rpd}}\ge0,\ \vec u_{\mathrm b}$ | Rapidity and axis of the boost $\tilde U_{\Psi,\mathrm b}$ |
| $\theta_{\mathrm{axr}}\in[0,2\pi)$ | Angle of the rotor $\tilde u_{\mathrm r}$; $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ |
| $\tilde A_\Phi=A_te_t+\sum_\eta A_\eta\vec e_\eta$ | Potential biquaternion; material sector; coefficients central in the abelian case |
| $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$ | Covariant derivative, left action |
| $\frac{iϙ}{\hbar}\tilde A_\Phi$ | The added element: central imaginary slot plus Hermitian vector slot |
| $\tilde K_\Phi=i\frac{E}{\hbar c}e_t+\frac{\vec p}{\hbar}$ | Canonical wavevector, from $\tilde\nabla_\Phi\theta_{\mathrm{pha}}$ |
| $\tilde K_{\Phi,\mathrm{gco}}=\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_\Phi$ | Covariant wavevector; gauge invariant; names the boost |
| $\kappa_t,\vec\kappa$ | Components of $\tilde K_{\Phi,\mathrm{gco}}$; $\kappa_t^{2}-|\vec\kappa|^{2}=-k_m^{2}$ |
| $\tilde V_\Phi=ic\,\tilde U_{\Psi,\mathrm b}^{-2}=\gamma(ic\,e_t+\vec v)$ | Four-velocity; kinetic |
| $\mathcal B_\Psi=\tilde U_{\Psi,\mathrm b}^{-2}$ | Four-vector factor; $\tilde K_{\Phi,\mathrm{gco}}=ik_m\mathcal B_\Psi$ |
| $i\partial_\mu\theta_{\mathrm{pha}}+\frac{iϙ}{\hbar}A_\mu$ | The coupled phase bracket |
| $\tilde u_{\mathrm r}^{-1}(\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b})\tilde u_{\mathrm r}$ | The boost bracket; receives the Hermitian slot |
| $\tilde F$ | Curvature; the gauge invariant |
| $\Lambda$ | Gauge function; $\theta_{\mathrm{pha}}\mapsto\theta_{\mathrm{pha}}+ϙ\Lambda/\hbar$ |

## Further Reading

- [The Coupled Dirac Equation in Biquaternionic Form](the-coupled-dirac-equation-in-biquaternionic-form.html), the element form this article re-coordinatises.
- [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html), for the word, the four brackets and the mass-shell proposition.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html), for the operator identity with the curvature.
- [The Variational Principle and the Coupled Dirac Equation in Biquaternionic Form](the-variational-principle-and-the-coupled-dirac-equation-in-biquaternionic-form.html), for the action and the current.
- [The Variational Principle and the Coupled Dirac Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), where the constraint structure appears.
- [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html), for the current as a pairing.
- [The Classical Origin of $g=2$ in Biquaternionic Form](the-classical-origin-of-g-2-in-biquaternionic-form.html), for the spin's transport in a background.
- [Spin Hydrodynamics in Biquaternionic Form](spin-hydrodynamics-in-biquaternionic-form.html), for the spin-fluid reading of the four brackets.
- [The Gauge Extension of the Central Phase: Why the Centre Caps the Group](the-gauge-extension-of-the-central-phase-why-the-centre-caps-the-group.html), for the localization that produces the coupling.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the covariant derivative in geometric algebra.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the spin-fluid variables and their underdetermination.
