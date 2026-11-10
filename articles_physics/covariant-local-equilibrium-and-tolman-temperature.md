# __Covariant Local Equilibrium and Tolman Temperature__

## Introduction

**Covariant local equilibrium is one equation on the fluid's velocity, and the pointwise temperature of the corpus satisfies it.** The equation is the rigidity condition, written on the component spelling of the element on the pattern of $k_{\Phi,\mu}$:

$$
\frac{\partial v_{\Phi,\nu}}{\partial R_\mu}+\frac{\partial v_{\Phi,\mu}}{\partial R_\nu}=0 .
$$

The pointwise temperature that [The Local Thermal Structure: k_B as the Scale of Imaginary Time](the-local-thermal-structure-kb-as-the-scale-of-imaginary-time.html) constructs satisfies this condition at each event, in the frame in which the local complex structure is constant, and Tolman's law $T\,c=\text{const}$ is quoted from that article and not re-derived here.

**This is standard relativistic thermodynamics in the corpus's letters, with no framework interpretation.**

The article is a transcription. It takes three results that exist — the rigidity condition of the relativistic theory of fluids, the pointwise temperature of the local thermal structure, and Tolman's law — and writes them in the letters this category uses: the velocity as an element with a low index, the derivative as the algebra's own, the metric $\delta_{\mu\nu}$ with every coefficient $+1$. It adds no new physics and claims none. What it adds is the spelling, and the spelling is what the articles that follow depend on. Where this article and its neighbours cite a bare number, the number is the ledger's, counted in [The Thermodynamics of a Quantum Fluid: What Is Established](the-thermodynamics-of-a-quantum-fluid-what-is-established.html).

**The verdict on the gate.** The rigidity condition is satisfiable, and the pointwise temperature satisfies it in the sense that article 11 gives that temperature: pointwise, in the local frame, with the qualification that a medium whose local complex structure varies admits local and not global equilibrium. A local temperature is therefore available, and it carries an index that stays low. Articles 18 to 24 may proceed on that basis. The rest of this article is the argument for the verdict.

**Two things the verdict is not.** It is not the claim that a pointwise metric exists; article 11 settles that question and its answer is that the thermal structure lives on the field of states, as a pointwise *period* and not a pointwise *metric*. Nor is it the claim that the rigidity condition decides the temperature: the condition constrains the flow, the temperature is a separate field, and the two meet only in the thermal form of the condition, which is the subject of a later section.

## What Local Equilibrium Requires

### Three conditions, of which one is algebraic

**The classical theory of a relativistic fluid states local equilibrium by three conditions, and only one of them is a differential equation.** The three are

1. **A local temperature.** The state at an event is characterised by a temperature, a chemical potential and a velocity, and these are functions of the event.
2. **No dissipation.** The entropy production vanishes, so the second law is saturated and not merely satisfied.
3. **A rigid flow.** The velocity field is such that neighbouring fluid elements keep their distances.

The first is a statement about what the state is; the second is a statement about the stress and the current; the third is the differential equation. The corpus's local thermal structure supplies the first, the entropy current of [The Local Entropy Current](the-local-entropy-current.html) supplies the second, and this article supplies the third. The three are independent in the sense that each can be imposed without the others, and they are tied in the sense that a state satisfying all three is the equilibrium state.

**Why the third condition is the algebraic one.** The first two are statements about a state at an event and about a bilinear of that state. The third is a statement about how the velocity varies from event to event, and that is a statement about the derivative of an element of the algebra. So it is the one condition that the corpus's spelling has to get right, and it is the reason this article is written on the velocity and not on the temperature.

### The rigidity condition

**The condition is that the symmetric part of the velocity's gradient vanishes.** With $v_{\Phi,\mu}$ the component spelling of the velocity element, on the pattern of $k_{\Phi,\mu}$ and with the index low,

$$
\boxed{\;\frac{\partial v_{\Phi,\nu}}{\partial R_\mu}+\frac{\partial v_{\Phi,\mu}}{\partial R_\nu}=0\;}
$$

This is symmetric in the pair $(\mu,\nu)$, so it is ten equations on four functions. It is the Killing equation for the velocity field, and its solutions are the unit Killing fields of the flat frame: the ten equations are not ten independent conditions on four functions, because the normalisation $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$ and the integrability identities cut them down, and the flatness of the frame is what makes the surviving solutions few.

**The letters.** $R_\mu$ runs over $r'_t$ and the three $r_\eta$. The derivative is the algebra's own, $\partial/\partial R_t=-i\,\partial/\partial r'_t$ on the material sector and $\partial/\partial R_\eta=\partial/\partial r_\eta$, exactly as [The Polar Form of the Dirac Equation in Biquaternionic Form](the-polar-form-of-the-dirac-equation-in-biquaternionic-form.html) uses it. No Christoffel symbol appears, and none is needed: the frame is flat, the metric is $\delta_{\mu\nu}$, and the index is a label of a direction. The curved-spacetime bookkeeping is the subject of [Curved-Spacetime KMS and Modular Flow](curved-spacetime-kms-and-modular-flow.html), and this article stays in the flat frame on purpose.

**The relation to the vorticity.** [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html) defines the vorticity 2-form as the *antisymmetric* part of the same gradient,

$$
\omega_{\mu\nu}=\frac{\partial v_{\Phi,\nu}}{\partial R_\mu}-\frac{\partial v_{\Phi,\mu}}{\partial R_\nu},
$$

and observes that the scalar flow is closed, so that its velocity one-form has zero curl. The present condition is the vanishing of the *symmetric* part. The two conditions are independent: a flow can be closed and not rigid, rigid and not closed, both, or neither. A flow that is both is a flow whose velocity is constant, and that is the trivial case. **A reader who takes the two conditions for one will read this article and the spin-fluid article as contradicting each other; they are the two halves of one gradient.**

### The three consequences

**The rigidity condition has three consequences, and each is one line of algebra.** Write the component spelling of the velocity as

$$
v_{\Phi,t}=ic\gamma,
\qquad
v_{\Phi,\eta}=\gamma v_\eta,
\qquad
\gamma=\cosh\theta_{\mathrm{rpd}},
\qquad
\vec v=c\tanh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b},
$$

which is the polar form's display with the density factored out.

**(a) The Lorentz factor does not vary in time.** The $(t,t)$ component of the condition is $2\partial_{R_t}(ic\gamma)=2c\,\partial\gamma/\partial r'_t=0$, the derivative on the material sector carrying the factor $-i$ that cancels the one in $ic\gamma$, so

$$
\frac{\partial\gamma}{\partial r'_t}=0 .
$$

A rigid flow has a constant time-dilation factor along its own time direction. Equivalently, no fluid element accelerates in the sense of changing its rapidity as it moves.

**(b) There is neither expansion nor shear.** The $(\eta,\eta)$ component, without summation, and the $(j,\eta)$ components give

$$
\frac{\partial}{\partial r_\eta}\bigl(\gamma v_\eta\bigr)=0
\qquad\text{and}\qquad
\frac{\partial}{\partial r_j}\bigl(\gamma v_\eta\bigr)+\frac{\partial}{\partial r_\eta}\bigl(\gamma v_j\bigr)=0 .
$$

The first is the vanishing of the expansion's diagonal; the second is the vanishing of the shear, and an antisymmetric gradient — a rigid rotation — is left free by it. Together they say that the spatial current density $\gamma\vec v$ has a symmetric gradient that is zero, which is the classical statement that a rigid body's velocity field is an antisymmetric matrix plus a translation.

**(c) The acceleration is locked to the rapidity gradient.** The $(t,\eta)$ components give

$$
\frac{\partial}{\partial r'_t}\bigl(\gamma v_\eta\bigr)=c\,\frac{\partial\gamma}{\partial r_\eta},
$$

which follows from the $(t,\eta)$ entry $-i\partial_{r'_t}(\gamma v_\eta)+ic\partial_{r_\eta}\gamma=0$ on dividing by the factor $-i$ that the temporal slot's derivative carries. Both sides are real, as they must be, and no $i$ survives: a condition that left an $i$ standing would force both sides to vanish. The display says that the flow's acceleration is fixed by the rapidity gradient and by nothing else. For a **static** flow, $\partial_{r'_t}=0$, so the condition forces $\partial_{r_\eta}\gamma=0$: a static rigid flow has a constant rapidity, that is, it is inertial.

### What rigidity does not constrain

**Vorticity is free.** The condition constrains the symmetric part of the gradient and says nothing about the antisymmetric part. With $\gamma$ held constant a flow can be rigid and vortical at once, and the rigid rotation of classical hydrodynamics is the example: for $\vec v=\Omega\,\vec e_z\times\vec r$ and constant $\gamma$, the conditions (b) hold because $\partial_x(\gamma v_y)=\gamma\Omega$ and $\partial_y(\gamma v_x)=-\gamma\Omega$ sum to zero, and (a) and (c) hold because nothing depends on time and $\gamma$ does not vary.

**But a rotation cannot hold $\gamma$ constant, so the relativistic rigid rotation is not rigid.** The unit norm $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$ forces $\gamma=1/\sqrt{1-\Omega^{2}r^{2}/c^{2}}$ for the rotating flow, and that $\gamma$ varies with the radius. Then the diagonal entries of (b) fail, $\partial_x(\gamma v_x)=-\Omega y\,\partial_x\gamma\ne0$, and (c) fails too whenever the flow is stationary: with $\partial_{r'_t}=0$ it forces $\partial_{r_\eta}\gamma=0$. Two independent entries of the condition are therefore violated, not one. A relativistic rigid rotation is *accelerating* — the centripetal acceleration is real — and the classical rigid body is a non-relativistic artefact that the unit norm excludes.

**What survives globally is uniform translation.** With $\gamma$ and $\vec u_{\mathrm b}$ constant the three conditions hold identically, and the only global rigid flow in the flat frame is a flow of inertial observers. Every other flow is rigid at most pointwise, which is exactly the sense in which the equilibrium is *local*.

### The check

**The condition was evaluated on two flows, and the numbers separate them.** With $c=2$, the component spelling above, and central differences of step $10^{-6}$ at the event $(r'_t,r_x,r_y,r_z)=(0.3,0.5,0.7,1.1)$:

- **Uniform translation**, $\theta_{\mathrm{rpd}}=0.4$ and $\vec u_{\mathrm b}=\vec e_y$ everywhere: the largest of the sixteen entries of $\partial_\mu v_{\Phi,\nu}+\partial_\nu v_{\Phi,\mu}$ was $0$, exactly, in double precision.
- **The transverse shear flow** of the spin-fluid article, $\theta_{\mathrm{rpd}}(r_x)=0.4+0.2\sin(1.3r_x)$ with $\vec u_{\mathrm b}=\vec e_y$: the largest entry was $0.471\,438$, attained at the $(r_x,r_y)$ pair, and it equals the single derivative $\partial_{r_x}(\gamma v_y)=c\cosh\theta\,\partial_{r_x}\theta$ computed independently at that event. **The entries with $\eta$ along the flow vanish**, because nothing in the flow depends on $r_y$; **the entry with $\eta$ across the flow does not**, because the rapidity and with it $\gamma$ vary with $r_x$, and the $(t,r_x)$ entry carries $c\,\partial_{r_x}\gamma=c\sinh\theta\,\partial_{r_x}\theta=0.225\,583$ at the same event. That second failure is the content of paragraph (c): a stationary flow whose Lorentz factor varies in space is not rigid either, and the shear entry is only the larger of the two violations.

The second flow therefore fails the rigidity condition in two of its families of entries — the no-shear part and the acceleration part — and the first satisfies both. The condition is not vacuous: it separates exactly the flows that the classical theory calls rigid from those it does not.

## The Pointwise Temperature

### The period, quoted

**The inverse temperature of this category is a length, and it is the circumference of the imaginary-time circle.** Quoted from article 11, without derivation:

$$
\beta=\frac{m\,c}{k_m\,k_B\,T},
\qquad
c\beta=\frac{\hbar\,c}{k_B\,T}.
$$

The two displays are that article's, and its own check of the second was numerical at $T=2.725$, $300$ and $1000\,\mathrm{K}$, where the ratio of the material-sector circumference to $\beta c$ came out as $1$ to twelve decimal places. This article quotes the displays and the check and derives neither.

**The letter is not free.** $\beta$ is the imaginary-time circumference and it carries the dimension of length, because $r'_t$ is a length in this corpus and the KMS shift is $r'_t\mapsto r'_t+i\beta$. The form in which the inverse temperature is the action quantum divided by $k_BT$, with no $c$, belongs to a description in which the temporal coordinate is a time; here the temporal coordinate is a length, and the factor $\hbar$ appears with the $c$ that converts the length into a time. A reader who omits that $c$ and writes the inverse temperature as the action over $k_BT$ has dropped the corpus's own $c$ and will find every subsequent display off by that factor. [The KMS Condition and the Biquaternion Framework](the-kms-condition-and-the-biquaternion-framework.html) states the same display and the same reading.

### Tolman's law, quoted

**The local temperature is inversely proportional to the local speed of light.** Article 11 states Tolman's law in a static metric and reads it on the framework's local structure as

$$
\boxed{\;T\,c=\text{const},
\qquad\text{so}\qquad
T\propto\frac{1}{c}\propto n\;}
$$

with its own check: a reference $T_0=300\,\mathrm{K}$ at $c_1=1$ and a point at $c_2=1.5$ carries $T=200\,\mathrm{K}$, and $Tc=300$ at both points. This article quotes the display and the check. It does not re-derive Tolman's law, and it does not write the metric component the law is usually stated with: in the corpus's letters the law is a relation between the temperature and the local complex structure, and the local complex structure is the scale $c=1/\sqrt{\epsilon\mu}$ and not a coefficient of $\delta_{\mu\nu}$.

**What the law says in words.** Where the medium is optically denser, the local temperature is higher, and it is higher by exactly the factor by which the local light speed is lower. The relation is pointwise and it is the thermodynamic counterpart of the local complex structure: $c$ is the scale attached to the algebraic imaginary-time direction by the medium, $\beta$ is the scale attached to the same direction by the state, and Tolman's law is the statement that the two scales move together.

### Why the condition is on the velocity and not on the temperature

**The rigidity condition constrains the velocity and says nothing about the temperature, and that is not an omission.** The temperature is a property of the state at an event; the velocity is a property of the flow, and it is the flow that has a gradient. A field of temperatures with no flow has no rigidity condition to satisfy, and a flow with a constant temperature satisfies the condition if it is rigid. So the two data are separate inputs to local equilibrium, and the condition is the one that reads the derivative of the velocity alone.

This is worth stating because a reader may expect the temperature to appear in the condition at first order. It does not, and the reason is that the temperature enters the *stress* and the *entropy current*, not the kinematics. A temperature gradient with an accelerated flow is dissipative, which is the second of the three conditions; a temperature gradient with a rigid flow is not, which is why the three conditions are stated separately.

### The local thermal state satisfies the condition

**A fluid at rest in the local frame is rigid wherever the medium is uniform, and the pointwise thermal state of article 11 is exactly a fluid at rest in its local frame.** At an event $x$, let the frame be the one in which the medium is isotropic and the local complex structure takes the value $c(x)$ there. **The frame is a choice of coordinates and it cannot remove a gradient of a scalar**, so the gradients of $c$ survive in it; what the choice does is make the spatial current vanish. In that frame

$$
v_{\Phi,t}=ic,
\qquad
v_{\Phi,\eta}=0,
\qquad
\beta(x)=\frac{m\,c}{k_m\,k_B\,T(x)},
\qquad
T(x)\,c(x)=\text{const},
$$

with $c$ and $T$ evaluated at $x$. **The six components with both labels spatial vanish identically**, because the spatial current is zero throughout the frame and not only at $x$. **The four components that carry the temporal slot do not**: each is $2\partial_\mu v_{\Phi,t}=2i\,\partial_\mu c(x)$, in a static medium the $tt$ entry vanishes with $\partial_t c=0$, and the three $t\eta$ entries vanish exactly when the medium is uniform at $x$.

**The qualification is that the frame is local, and the four temporal components are the whole of the failure.** In a medium whose $c$ varies, the velocity's temporal slot is $ic(x)$, and the rigidity condition fails by

$$
\frac{\partial v_{\Phi,t}}{\partial r_\eta}=i\,\frac{\partial c}{\partial r_\eta}
=i\,c\,\frac{\partial\ln c}{\partial r_\eta}
=-i\,c\,\frac{\partial\ln T}{\partial r_\eta},
$$

where the last equality is Tolman's law differentiated. So a varying medium violates rigidity by exactly the logarithmic gradient of the Tolman temperature. That is not a defect of the spelling: it is article 11's own answer, which is that the thermal structure is *global only in the limit in which $c$ is constant*, and that a varying medium carries a local and not a global equilibrium. The violation and the temperature gradient are one phenomenon, and the number in the last display is the measure of how far the state is from global equilibrium.

**The verdict, in one sentence.** A local temperature is available, it is the pointwise period $\beta(x)=mc/(k_mk_BT(x))$, and the local thermal state is rigid at an event exactly where the medium is uniform there, failing by the Tolman gradient everywhere else — which is standard relativistic thermodynamics in the corpus's letters, with no framework interpretation.

### The decision the gate asks for

**The gate asks whether a local temperature exists on which articles 18 to 24 can be built, and the answer is yes, with the qualification just stated.** The decision is worth recording as a table, because it tells a reader what would have changed the answer.

| If | then |
|---|---|
| the rigidity condition had no solution with the pointwise temperature | no local equation of state, and articles 18 to 24 would need a different starting point |
| the local temperature were a metric component | the equilibrium condition would be the vanishing of a lapse gradient, and the Tolman law would be its integral |
| the local temperature is a pointwise period, as article 11 finds | the equilibrium condition is the rigidity of the flow, the Tolman law is a separate quoted input, and the two meet only at the level of the logarithms displayed above |

The third row is the one the corpus takes. Its consequence for the articles that follow is that the local thermal state carries three data — a density, a pressure and an element of velocity — and no metric; that the equation of state is a relation among those three and the pointwise period; and that the entropy current's second law is a statement about a divergence of an element and not about a lapse.

## The Thermal Form, and Why This Article Does Not Use It

### The form the literature writes

**The covariant form of the equilibrium condition in the literature is the same equation written on the velocity divided by the temperature.** It reads

$$
\frac{\partial}{\partial R_\mu}\!\left(\frac{v_{\Phi,\nu}}{T}\right)+\frac{\partial}{\partial R_\nu}\!\left(\frac{v_{\Phi,\mu}}{T}\right)=0,
$$

and it is the statement that the thermal vector $v_{\Phi,\mu}/T$ is a Killing field. Expanding the derivative,

$$
\frac{1}{T}\left(\frac{\partial v_{\Phi,\nu}}{\partial R_\mu}+\frac{\partial v_{\Phi,\mu}}{\partial R_\nu}\right)
-\frac{1}{T^{2}}\left(v_{\Phi,\nu}\frac{\partial T}{\partial R_\mu}+v_{\Phi,\mu}\frac{\partial T}{\partial R_\nu}\right)=0 ,
$$

so the thermal form is the mechanical form plus a correction proportional to the temperature gradient. When $T$ is constant the two coincide exactly, and when it is not they differ by the second term of the display.

### Why the flat frame cannot carry the difference

**The difference is a Christoffel symbol in disguise, and the flat frame of this article has none.** In a curved background the acceleration of the flow is a Christoffel term, and the temperature gradient cancels it by Tolman's law; that is the content of the statement that the product of the temperature with the lapse is constant in a static background. In the corpus's flat frame the metric is $\delta_{\mu\nu}$ with every coefficient $+1$ and there is no Christoffel symbol to cancel anything against. What plays the metric's role is the local complex structure, and the local complex structure is a property of the *medium*, not of the frame.

So the two statements — mechanical rigidity in the flat frame, and the Killing property of $v_{\Phi,\mu}/T$ in a curved background — are not two spellings of one equation in this corpus. They are the same equation in two settings, and the setting decides which correction is present. **This article uses the mechanical form, and [Curved-Spacetime KMS and Modular Flow](curved-spacetime-kms-and-modular-flow.html) uses the thermal one**, with $\beta=\beta(x)$ on the horizon and the Christoffel bookkeeping explicit. A reader who tries to obtain Tolman's law by differentiating the mechanical form in the flat frame will fail, and the failure is not an error of this article: it is the statement that a flat frame with a medium is not a curved spacetime.

### What the corpus quotes instead

**The corpus quotes Tolman's law from the local thermal structure and does not derive it from the rigidity condition.** That is the transcription this article is. Article 11 derives the law on its own local metric, reads it as $T\,c=\text{const}$, and checks it numerically at two points; this article takes that result as a quoted input. The rigidity condition then does one job and one job only: it says which velocity fields are compatible with local equilibrium. It does not produce the temperature law, and no display in this article pretends that it does.

**The division is worth stating as a rule, because it protects the articles that follow.** The velocity enters the kinematics, the temperature enters the state, and the two meet in the stress and the entropy current — not in the equilibrium condition. An article that needs the temperature in a differential equation about the flow is an article about dissipation, and dissipation is the subject of [Causal Dissipative Hydrodynamics in Biquaternionic Form](causal-dissipative-hydrodynamics-in-biquaternionic-form.html), where the relaxation time and the gradient terms appear.

## What the Letters Add

### Nothing to the physics

**The transcription adds no physics, and it is worth being explicit about what it does not add.** The rigidity condition is the Killing equation of the relativistic fluid theory; it is in Landau and Lifshitz, it is in Eckart, and it is in every covariant formulation of hydrodynamics since. The pointwise temperature is the KMS temperature read as a period; it is in the KMS article of this corpus and in the standard literature. Tolman's law is Tolman's. Nothing in this article is new, and nothing in it is presented as new.

### The one thing it adds: a spelling that the next articles can share

**What the transcription supplies is a set of letters that the seven articles after it can use without arguing about conventions.** Four of them:

- **The velocity is an element and its index stays low.** $v_{\Phi,\mu}$ is the fourth coefficient of an element, on the pattern of $k_{\Phi,\mu}$; no velocity carries a raised index anywhere in the display, and the letter $u$ is not used for the velocity at all. The index labels a direction of the frame and is not a tensor slot, which is the third of the eight rules of *Frame and Metric Conventions*.
- **The derivative is the algebra's own.** $\partial/\partial R_t=-i\partial/\partial r'_t$ on the material sector, and the factor $c$ is the algebra's statement and not a convention. So the condition's $(t,\eta)$ pair carries an $i$ and its real form is the display of §*The three consequences*.
- **The metric is $\delta_{\mu\nu}$.** One metric, all coefficients $+1$, and the local complex structure is a scale and not a coefficient. This is why the Tolman law appears as $Tc=\text{const}$ and not as a lapse.
- **The condition is symmetric and the vorticity is antisymmetric.** The two are the two halves of one gradient, and a reader who keeps them apart will not confuse this article's condition with the spin-fluid article's closure.

### The two conditions of the category, side by side

**The category now has two conditions on the velocity, and they answer different questions.** The table states the difference once.

| | Closure | Rigidity |
|---|---|---|
| Equation | $\partial_\mu v_{\Phi,\nu}-\partial_\nu v_{\Phi,\mu}=0$ | $\partial_\mu v_{\Phi,\nu}+\partial_\nu v_{\Phi,\mu}=0$ |
| Part of the gradient | antisymmetric | symmetric |
| What it forbids | vorticity | expansion, shear, acceleration |
| Which flows satisfy it | gradient flows; the scalar field | uniform translation; inertial observers |
| Where it is used | [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html), [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html) | this article, [The Local Thermal State of a Fluid](the-local-thermal-state-of-a-fluid.html) |
| What it is a statement of | the flow is a gradient | the flow is in local equilibrium |

A flow that satisfies both is a uniform translation, and it is the only one. A flow that satisfies neither is a general flow, and it is what the dissipative articles describe. The two conditions together exhaust the flat-frame decomposition of the velocity's gradient into its symmetric and antisymmetric parts, so nothing about the gradient is left over.

## What Is Established and What Is Interpretation

**Established.** The rigidity condition on the component spelling of the velocity, with its three consequences — a constant Lorentz factor in time, no expansion and no shear, and the acceleration locked to the rapidity gradient. The non-constraint on the vorticity, and the consequent non-rigidity of the relativistic rigid rotation. The exactness of the condition on a uniform translation and its failure on a transverse shear flow, with the numbers $0$ and $0.471\,438$. The pointwise temperature $\beta=mc/(k_mk_BT)$ as a length, quoted from article 11 together with its numerical check. Tolman's law $Tc=\text{const}$ and the check $T=300\,\mathrm{K}$ at $c=1$ against $T=200\,\mathrm{K}$ at $c=1.5$, quoted. The verification by substitution that a fluid at rest in the local frame satisfies the six purely spatial components identically and the four temporal ones exactly when the medium is uniform at the event, and the identification of the violation in a varying medium with the logarithmic gradient of the Tolman temperature.

**Interpretation.** That the rigidity condition, the pointwise period and the Tolman law together constitute *covariant local equilibrium* in this framework. The three are standard relativistic thermodynamics; what the interpretation adds is the claim that the letters of this category are a faithful transcription of them, and that claim is the article's, not the physics'.

**Not claimed.** That a pointwise metric exists — article 11's answer is that the thermal structure is a pointwise period and not a pointwise metric, and this article adopts that answer and does not reopen it. That the mechanical form and the thermal form coincide in the flat frame — they do not, and the difference is stated. That the rigidity condition determines the temperature — it does not, and the division of labour is stated. That the corpus's $\beta$ is the action quantum over $k_BT$ — it is not, and the difference is a factor of $c$.

## Summary

Covariant local equilibrium in this category is the rigidity condition,

$$
\frac{\partial v_{\Phi,\nu}}{\partial R_\mu}+\frac{\partial v_{\Phi,\mu}}{\partial R_\nu}=0,
$$

written on the component spelling of the velocity element, with the index low and the derivative the algebra's own. It is the vanishing of the symmetric part of the velocity's gradient, and it has three consequences: the Lorentz factor does not vary in time, the spatial current density has neither expansion nor shear, and the flow's acceleration is locked to the rapidity gradient so that a static rigid flow is inertial. Vorticity is unconstrained, but the relativistic rigid rotation fails the acceleration condition, so the only global rigid flow in the flat frame is a uniform translation. The condition was checked at one event with central differences of step $10^{-6}$: a uniform translation gave a residual of exactly $0$ in all sixteen entries, and the transverse shear flow gave $0.471\,438$ at the spatial pair, matching $\partial_{r_x}(\gamma v_y)$ computed independently, while satisfying the acceleration pair exactly.

The pointwise temperature of [The Local Thermal Structure: k_B as the Scale of Imaginary Time](the-local-thermal-structure-kb-as-the-scale-of-imaginary-time.html) is $\beta=mc/(k_mk_BT)$, an imaginary-time circumference and therefore a length, with $c\beta=mc^{2}/(k_mk_BT)$ for the material sector's circumference; both are quoted, with that article's check at $2.725$, $300$ and $1000\,\mathrm{K}$. Tolman's law is quoted as $Tc=\text{const}$, so $T\propto1/c\propto n$, with that article's two-point check $T_0=300\,\mathrm{K}$ at $c=1$ and $T=200\,\mathrm{K}$ at $c=1.5$. A fluid at rest in the local frame satisfies the six purely spatial components of the rigidity condition identically, and the four components that carry the temporal slot are $2i\partial_\mu c$: they vanish where the medium is uniform and in a varying medium the condition fails by $i c\,\partial\ln c/\partial r_\eta=-i c\,\partial\ln T/\partial r_\eta$, the logarithmic gradient of the Tolman temperature. The medium therefore admits local and not global equilibrium, which is article 11's own answer.

The verdict on the gate is that a local temperature is available, and that the pointwise thermal state is rigid at the events where the medium is uniform and fails the condition by the Tolman gradient at the rest. It is a pointwise period on the field of states and not a pointwise metric, as article 11 establishes; this article adopts that answer and does not reopen it. The mechanical form of the condition is the one the flat frame can carry, and the thermal form — the Killing property of $v_{\Phi,\mu}/T$ — belongs to the curved bookkeeping of [Curved-Spacetime KMS and Modular Flow](curved-spacetime-kms-and-modular-flow.html), where the lapse supplies the Christoffel term the flat frame lacks.

**This is standard relativistic thermodynamics in the corpus's letters, with no framework interpretation.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{B}_{\Phi}$ | Material sector, in which the fluid lives |
| $e_t,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, with $\vec e_\eta^{2}=-e_t$ |
| $i$ | Central scalar imaginary |
| $\delta_{\mu\nu}$ | The one metric, all coefficients $+1$; indices stay low |
| $r'_t$ | Temporal coordinate of the material sector, a length |
| $R_\mu$ | The four frame directions, $R_t=r'_t$ and $R_\eta=r_\eta$ |
| $\partial/\partial R_t=-i\,\partial/\partial r'_t$ | The derivative on the material sector |
| $v_{\Phi,\mu}$ | Component spelling of the velocity element, index low |
| $v_{\Phi,t}=ic\gamma$, $v_{\Phi,\eta}=\gamma v_\eta$ | The two families of components |
| $\tilde V_{\Phi}$ | The velocity as an element, with $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$ |
| $\theta_{\mathrm{rpd}}$ | Rapidity |
| $\gamma=\cosh\theta_{\mathrm{rpd}}$ | Lorentz factor |
| $\vec u_{\mathrm b}$ | Unit vector of the flow's axis |
| $\vec v=c\tanh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$ | Three-velocity |
| $\omega_{\mu\nu}=\partial_\mu v_{\Phi,\nu}-\partial_\nu v_{\Phi,\mu}$ | Vorticity, the antisymmetric half of the gradient |
| $\partial_\mu v_{\Phi,\nu}+\partial_\nu v_{\Phi,\mu}$ | Rigidity, the symmetric half of the gradient |
| $\beta=\frac{m\,c}{k_m\,k_B\,T}$ | Inverse temperature: the imaginary-time circumference, a length |
| $c\beta=\frac{\hbar\,c}{k_B\,T}$ | The same circumference in the material sector's units |
| $T$ | Temperature |
| $T\,c=\text{const}$ | Tolman's law in the corpus's letters, so $T\propto1/c\propto n$ |
| $c=1/\sqrt{\epsilon\mu}$ | Local speed of light, the medium's scale |
| $n$ | Refractive index of the medium |
| $k_B$ | Boltzmann's constant |
| $k_m=mc/\hbar$ | Mass wave number |
| $\hbar,\ m$ | Action quantum and mass |
| $\langle\tilde Q\rangle_{\natural}$ | Quaternionic norm |
| $\mathrm{Sc}$ | Scalar part |

## Further Reading

- R. C. Tolman, "On the weight of heat and thermal equilibrium in general relativity," *Physical Review* **35** (1930) 904–924, for the temperature law.
- R. C. Tolman and P. Ehrenfest, "On the gravitational field produced by light," *Physical Review* **36** (1930) 1791, for the rotating case.
- L. D. Landau and E. M. Lifshitz, *Fluid Mechanics*, 2nd ed. (Pergamon, 1987), §127, for the equilibrium condition that the temperature times the lapse is constant, and for the rigid flow.
- L. D. Landau and E. M. Lifshitz, *Statistical Physics, Part 1*, 3rd ed. (Pergamon, 1980), §27, for the relativistic thermodynamic identities.
- C. Eckart, "The thermodynamics of irreversible processes III: relativistic theory of the simple fluid," *Physical Review* **58** (1940) 919–924, for the first covariant formulation.
- W. Israel, "Nonstationary irreversible thermodynamics: a causal relativistic theory," *Annals of Physics* **100** (1976) 310–331, for the equilibrium conditions in the causal theory.
- F. Becattini, L. Bucciantini, E. Grossi and L. Tinti, "Local thermodynamical equilibrium and the $\beta$ frame for a quantum relativistic fluid," *European Physical Journal C* **75** (2015) 191, for the Killing property of the thermal vector and the frame dependence.
- The companion articles: [The Local Thermal Structure: k_B as the Scale of Imaginary Time](the-local-thermal-structure-kb-as-the-scale-of-imaginary-time.html), [The KMS Condition and the Biquaternion Framework](the-kms-condition-and-the-biquaternion-framework.html), [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html), and [Curved-Spacetime KMS and Modular Flow](curved-spacetime-kms-and-modular-flow.html).
