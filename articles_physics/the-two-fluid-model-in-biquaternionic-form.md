# __The Two-Fluid Model in Biquaternionic Form__

## Introduction

**A quantum fluid at finite temperature is two fluids in one: a condensate that carries no entropy and a normal component that carries all of it and dissipates.** The two flows are elements,

$$
\tilde V_{\Phi,\mathrm{sup}}=\frac{\tilde P_{\Phi,\mathrm{sup}}}{m},
\qquad
\tilde V_{\Phi,\mathrm{nrm}}=\frac{\tilde P_{\Phi,\mathrm{nrm}}}{m},
\qquad
\langle\tilde V_{\Phi,\mathrm{sup}}\rangle_{\natural}=\langle\tilde V_{\Phi,\mathrm{nrm}}\rangle_{\natural}=-c^{2},
$$

**and the whole of the model is the statement that they are two, that only one of them carries the entropy current of [The Local Entropy Current](the-local-entropy-current.html), and that they exchange momentum.**

**The condensation is what makes the split necessary.** The polar form of [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html) describes a state with one flow and one rotor; a thermal state has, in addition, the excitations that the thermal circle supports, and those excitations carry the entropy and obey the dissipative equations. **The two-fluid model is therefore not a new theory but the statement that the field's state has two pieces whose hydrodynamics differ**, and the article's job is to write the two pieces and their coupling in the corpus's letters.

**The zero-temperature limit is the article's check.** At $T\to0$ the normal density vanishes, the entropy density vanishes with it, the normal flow becomes undefined because there is nothing to carry it, and the equations reduce exactly to the polar-form article's. **That limit is shown explicitly and in full, because a two-fluid model that does not reduce to the one-fluid model is not a model of the same substance.**

**What the article cites and what it does not repeat.** The stress-energy element is [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html)'s; the entropy current and its Hermiticity declaration are [The Local Entropy Current](the-local-entropy-current.html)'s; the equation of state is [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html)'s. **The article adds the second element, the split of the density, the exchange, and the limit.**

## The Two Elements

### The split of the density

**The proper density splits into two positive parts, and the split is a definition of the model rather than a consequence of the algebra.**

$$
\rho_{\mathrm{num}}=\rho_{\mathrm{num,sup}}+\rho_{\mathrm{num,nrm}},
\qquad
\rho_{\mathrm{num,sup}}\ge0,
\qquad
\rho_{\mathrm{num,nrm}}\ge0,
$$

with $\rho_{\mathrm{num}}=\lVert\tilde\Xi\rVert^{2}$ the proper density of [The Local Thermal State of a Fluid](the-local-thermal-state-of-a-fluid.html). **The condensate's part is the part of the amplitude squared that is in the state the polar form describes**; the normal part is the rest, and the rest is what has entropy.

**The split is not a split of the field, and this is worth saying once.** There is one field $\tilde\Xi$; the two densities are two contributions to its amplitude squared, not two fields. **A reader who writes two fields has left the framework and entered a two-scalar model**, which has different dynamics and, in particular, two mass shells rather than one. The corpus's two-fluid model is a description of one field's state, and the description is called two-fluid by analogy with the classical helium literature and not by structure.

**The two fractions, and the notation for them.** Writing $x_{\mathrm{sup}}=\rho_{\mathrm{num,sup}}/\rho_{\mathrm{num}}$ and $x_{\mathrm{nrm}}=1-x_{\mathrm{sup}}$ for the fractions, the two limits of the model are $x_{\mathrm{nrm}}=0$ (the pure state) and $x_{\mathrm{sup}}=0$ (the ordinary fluid, which is the limit in which the condensate has been destroyed). **Both limits must be reachable, and the article checks both.**

### The two elements and their norms

**Each flow is an element with the corpus's normalisation, and the normalisation is what makes the relative velocity well defined.** With the two elements at the head of the article, the relative flow is

$$
\tilde W_\Phi=\tilde V_{\Phi,\mathrm{nrm}}-\tilde V_{\Phi,\mathrm{sup}},
$$

an element whose norm is not fixed by the two normalisations alone. **The identity is the one every sum of squares obeys**, with the contraction of the two flows in place of the plain product's scalar part:

$$
\langle\tilde W_\Phi\rangle_{\natural}
=\langle\tilde V_{\Phi,\mathrm{nrm}}\rangle_{\natural}+\langle\tilde V_{\Phi,\mathrm{sup}}\rangle_{\natural}
-2\sum_\mu v_{\Phi,\mathrm{nrm},\mu}\,v_{\Phi,\mathrm{sup},\mu}
=2c^{2}\left(\gamma_{\mathrm{nrm}}\gamma_{\mathrm{sup}}\left(1-\vec\beta_{\mathrm{nrm}}\cdot\vec\beta_{\mathrm{sup}}\right)-1\right),
$$

**the cross term being $\mathrm{Sc}(\tilde V_1\tilde V_2^{\natural})$ and not $\mathrm{Sc}(\tilde V_1\tilde V_2)$**: the quaternionic norm is a sum of squares, so it expands with a plus on the spatial contraction, and the plain product's scalar part carries a minus there. **The relative element's size measures how far the two flows are from coinciding**, it vanishes exactly at coincidence, and it is non-negative for two future-directed flows, since $\gamma_1\gamma_2(1-\vec\beta_1\cdot\vec\beta_2)\ge1$ for any pair of unit future timelike directions — checked on twenty thousand random pairs, with no negative value found. That is the object that all the dissipation is proportional to.

**The coincidence is the equilibrium condition and the model's most important special case.** When $\tilde V_{\Phi,\mathrm{sup}}=\tilde V_{\Phi,\mathrm{nrm}}$ the two fluids move together, no exchange occurs, and the entropy production of the mutual-friction channel vanishes; **the two-fluid system in that state is one fluid with an entropy density that is the normal component's.** Every laboratory two-fluid state is a small departure from this one.

**The components, low.** Writing $v_{\Phi,\mathrm{sup},\mu}$ and $v_{\Phi,\mathrm{nrm},\mu}$ for the components and $w_{\mu}=v_{\Phi,\mathrm{nrm},\mu}-v_{\Phi,\mathrm{sup},\mu}$ for the relative one, every index is low and the metric is $\delta_{\mu\nu}$, exactly as in the single-fluid articles. **The relative component $w_\mu$ is the only new vector in the article**, and the dissipation is written on it.

### Why two flows and not two temperatures

**The model has one temperature and two flows, and the choice is forced.** A thermal state has one period $\beta$: the imaginary-time circle is a property of the state and not of a component, so there is one temperature. **The two components differ in their flow, not in their temperature**, and a model with two temperatures is a model of two systems in partial equilibrium, which is a different and more elaborate object.

**The choice is also the one that keeps the entropy current simple.** With one temperature, the entropy current of [The Local Entropy Current](the-local-entropy-current.html) reads on the normal component alone,

$$
\tilde J_{\Phi,\mathrm{ent}}=s_{\mathrm{ent}}\,\gamma_{\mathrm{nrm}}\left(e_t+\vec\beta_{\mathrm{vel,nrm}}\right),
$$

with $\gamma_{\mathrm{nrm}}$ and $\vec\beta_{\mathrm{vel,nrm}}$ built from $\tilde V_{\Phi,\mathrm{nrm}}$, and it is Hermitian by the same argument as before. **The condensate contributes nothing to it**, and that single sentence is the model's thermodynamic core.

**A caution about the $\gamma$ factors in a two-fluid state.** The two components have different $\gamma$'s, so a display that writes $\gamma$ without a label in this article is ambiguous. **Every $\gamma$ in what follows carries a label**, and the article uses $\gamma_{\mathrm{nrm}}$ and $\gamma_{\mathrm{sup}}$ and never the bare letter.

## The Condensate and the Normal Component

### The condensate carries no entropy

**The condensate's entropy density is zero, and the reason is that the condensate is a pure state.** A pure state has no entropy — the corpus's functional $\mathcal{S}$ of [Coarse-Graining and the Biquaternion Entropy Functional](coarse-graining-and-the-biquaternion-entropy-functional.html) vanishes on the pure states, which sit on the zero-divisor cone — **so the entropy density of the sup component is zero by the functional's own definition and not by a modelling choice.**

$$
s_{\mathrm{ent,sup}}=0,
\qquad
s_{\mathrm{ent,nrm}}=s_{\mathrm{ent}} .
$$

**What the condensate carries instead is the quantum stress.** Its energy-momentum element has the scalar part $w_{\mathrm{fl,sup}}$ and its pressure is the $p_{\mathrm{qnt}}$ of [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html), the gradient correction. **So the two components differ in what they carry**: the condensate carries the quantum stress and no entropy, the normal component carries the entropy and the thermal pressure.

**The consequence for the second law, which [The Local Entropy Current](the-local-entropy-current.html) anticipated.** A state with $x_{\mathrm{nrm}}=0$ has a vanishing entropy current and a saturated second law; a state with $x_{\mathrm{nrm}}>0$ has an entropy current proportional to the normal fraction. **The production therefore vanishes with the normal fraction**, and the article's dissipation is proportional to $x_{\mathrm{nrm}}$ as well as to the relative flow — a product of two small quantities.

### The condensate's flow is a gradient

**The condensate's flow is the gradient of the phase, and this is the polar form's statement quoted.** From [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html), with the phase $S_{\tilde\Xi}$ of the field,

$$
m\,v_{\Phi,\mathrm{sup},\mu}=\partial_\mu S_{\tilde\Xi}+\hbar\,\chi_{\mu},
$$

where $\chi_\mu$ is the part the rotor contributes — zero for the scalar field and non-zero for the spinor, which is why [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html) is a different article. **For the scalar condensate the flow is a pure gradient**, so its vorticity $\omega_{\mu\nu}=\partial_\mu v_{\Phi,\mathrm{sup},\nu}-\partial_\nu v_{\Phi,\mathrm{sup},\mu}$ vanishes identically.

**The vanishing vorticity is the definition of superfluidity in this formalism, and it is the reason the two-fluid model has a superfluid at all.** A flow that is a gradient cannot be brought to rest by a boundary, because a gradient with a non-zero circulation is quantised and cannot decay continuously. **The circulation is [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html)'s subject**, and the article cites it rather than re-deriving the quantisation.

**The distinction from the normal component, in one line.** The normal component's flow is not a gradient, so its vorticity is free and it dissipates; **the condensate's is, so its vorticity is constrained and it does not.** That single structural difference is what the two-fluid model is for.

### The normal component carries the entropy and dissipates

**The normal component's equations are the single-fluid equations of the previous articles, read on its own flow.** Its energy-momentum element is the thermal one, its entropy current is the one above, and its production is the sum of squares of [The Local Entropy Current](the-local-entropy-current.html) evaluated with the normal flow. **No new equation is needed for it**, and the article writes none: the point of the two-fluid model is that the normal component is the ordinary fluid.

**Its stress is not conserved alone, and this is the coupling.** The normal component exchanges momentum with the condensate, so

$$
\tilde\nabla^{\natural}\tilde\Sigma_{\Psi,\mathrm{nrm}}=\tilde F_{\Phi,\mathrm{fr}},
\qquad
\tilde\nabla^{\natural}\tilde\Sigma_{\Psi,\mathrm{sup}}=-\tilde F_{\Phi,\mathrm{fr}},
\qquad
\tilde\nabla^{\natural}\left(\tilde\Sigma_{\Psi,\mathrm{nrm}}+\tilde\Sigma_{\Psi,\mathrm{sup}}\right)=0,
$$

with $\tilde F_{\Phi,\mathrm{fr}}$ the friction element. **The displays are element equations, and the corpus's divergence spelling applies to them slot by slot**: the scalar part of the first is $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\Sigma_{\Psi,\mathrm{nrm}})=\mathrm{Sc}(\tilde F_{\Phi,\mathrm{fr}})$, which is the declared form of [The Local Entropy Current](the-local-entropy-current.html), and the three vector slots repeat the same law with their own components. **The three displays say one thing: the total stress is conserved and each component's is not.** A reader who writes conservation for both components separately has written the wrong equations, and the error is the commonest one in the two-fluid literature.

## Mutual Friction

### The friction element

**The friction element is proportional to the relative flow and to the square root of the two densities, and its form is fixed by the requirement that it do no work when the two flows coincide.**

$$
\tilde F_{\Phi,\mathrm{fr}}=\frac{\rho_{\mathrm{num,sup}}\,\rho_{\mathrm{num,nrm}}}{\rho_{\mathrm{num}}}\,B_{\mathrm{frc}}\,\tilde W_\Phi ,
$$

with $B_{\mathrm{frc}}$ the friction coefficient — dimensionless in these letters because the density ratio already carries the dimensions of a density. **The element vanishes with either density, so a pure condensate has no friction to feel and an ordinary fluid has no condensate to feel it from**; both limits are correct and both are needed.

**The friction's work is what makes the entropy production, and the sign is fixed by the second law.** The rate at which the friction does work on the relative motion is the contraction of the friction element with the relative flow, and the entropy production is that rate divided by the temperature:

$$
\sigma_{\mathrm{ent}}=-\frac{1}{T}\,\mathrm{Sc}\left(\tilde F_{\Phi,\mathrm{fr}}\,\tilde W_\Phi\right)
=\frac{1}{T}\,\frac{\rho_{\mathrm{num,sup}}\,\rho_{\mathrm{num,nrm}}}{\rho_{\mathrm{num}}}\,B_{\mathrm{frc}}\left(\lvert\vec w\rvert^{2}-w_t^{2}\right)\ \ge 0,
$$

**the minus being forced and not chosen.** The plain product's scalar part is $\mathrm{Sc}(\tilde W_\Phi^{2})=w_t^{2}-\lvert\vec w\rvert^{2}$, which is negative for this element, because the temporal coefficient is imaginary and the spatial part real; a production written without the minus would therefore be negative for a positive coefficient. **The scalar part is real for a reason worth naming**: the temporal coefficients of both factors are imaginary and their spatial ones real, so $F_{\Phi,\mathrm{fr},t}W_{\Phi,t}$ is a product of two imaginary numbers and $\vec F_{\Phi,\mathrm{fr}}\cdot\vec W_\Phi$ a product of two real ones. **That product is negative**, $\mathrm{Sc}(\tilde F\tilde W)=(\rho_{\mathrm{num,sup}}\rho_{\mathrm{num,nrm}}/\rho)B_{\mathrm{frc}}\left[w_t^{2}-\lvert\vec w\rvert^{2}\right]$, which is why the display carries the minus: the dissipated quantity is $\lvert\vec w\rvert^{2}-w_t^{2}=c^{2}(\gamma_{\mathrm{nrm}}-\gamma_{\mathrm{sup}})^{2}+\lvert\vec w\rvert^{2}$, **a sum of two squares, positive and vanishing at coincidence**, the first being the relativistic correction and the second the square of the difference of the two current densities. **Damping of the relative motion heats the normal component, and the heat is exactly the kinetic energy of the relative drift** — that is the physical content of the display, and it is the standard mutual-friction mechanism of the helium literature quoted into the corpus's letters.

**The sign convention, stated once and used everywhere.** The norm of the relative element is quadratic in the relative motion but it is not the relative speed: for two collinear flows it is $2c^{2}(\cosh\delta\theta-1)$, which is $c^{2}(\delta\theta)^{2}$ to leading order and not $\lvert\vec w\rvert^{2}$. **The helium literature states its friction law on the relative speed** $w^{2}=\lvert\vec v_{\mathrm{nrm}}-\vec v_{\mathrm{sup}}\rvert^{2}$, and that quantity is a different one from $\lvert\vec w\rvert^{2}$: the element's spatial part is $\vec W_\Phi=\gamma_{\mathrm{nrm}}\vec v_{\mathrm{nrm}}-\gamma_{\mathrm{sup}}\vec v_{\mathrm{sup}}$, a difference of current densities and not of velocities. **The two coincide only in the non-relativistic limit**, which is the limit in which the two $\gamma$'s may be treated as one:

$$
\frac{\lvert\vec w\rvert^{2}-w_t^{2}}{\lvert\vec v_{\mathrm{nrm}}-\vec v_{\mathrm{sup}}\rvert^{2}}
=1.041\quad\text{at }(0.1c,\,0.101c),\qquad
=3.366\quad\text{at }(0.5c,\,0.55c),
$$

the first ratio being close to one and the second already three times one. **So the display below is the literature's form and not the corpus's**, and its use is confined to the arithmetic:

$$
\sigma_{\mathrm{ent}}=\frac{1}{T}\,\frac{\rho_{\mathrm{num,sup}}\,\rho_{\mathrm{num,nrm}}}{\rho_{\mathrm{num}}}\,B_{\mathrm{frc}}\,w^{2}\ \ge 0,
$$

which is manifestly non-negative for $B_{\mathrm{frc}}\ge0$. **The article uses the second display in the arithmetic and the first in the structural statements**, because the first shows the element and the second is the form the literature quotes; **a reader who takes the second for the exact statement will have a production that is wrong by the ratio tabulated above at relativistic relative speeds.**

### Numbers

**The friction was evaluated once, at $\rho_{\mathrm{num,sup}}=0.7$, $\rho_{\mathrm{num,nrm}}=0.3$, $\rho_{\mathrm{num}}=1$, $B_{\mathrm{frc}}=0.1$, $w=0.2$ and $T=2$.** The friction force is $0.7\times0.3\times0.1\times0.2=0.004\,200\,000\,000$ and the production is $0.004\,200\,000\,000\times0.2/2=0.000\,420\,000\,000$. **Both are positive, and the production scales as $w^{2}$** — doubling the relative speed quadruples it, which is the signature of a friction that is linear in the force and quadratic in the rate.

**The check that a reader can do on the same numbers.** With $w=0$ both vanish; with $x_{\mathrm{nrm}}=0$ both vanish; with $T\to\infty$ the production vanishes while the force does not. **The four limits are the four ways the display can degenerate, and each has a physical reading**: no relative motion, no normal component, no thermal coupling, no temperature.

### Why mutual friction and not viscosity

**Viscosity acts within a component; mutual friction acts between them, and the two are different channels of the same second law.** A state with a relative flow and no shear produces entropy through friction; a state with a shear and no relative flow produces it through viscosity. **Both appear as separate squares in the production of [The Local Entropy Current](the-local-entropy-current.html)**, and the two-fluid model adds the friction square to the list without modifying the others.

**The consequence for the counting of transport coefficients.** A two-fluid system has one more coefficient than a one-fluid system — $B_{\mathrm{frc}}$ beside $\zeta$, $\eta_{\mathrm{sh}}$ and $\kappa_{\mathrm{th}}$ — and no more. **A model with more is describing something else**, and the article names the count so that a reader can check a candidate model against it.

## The Josephson-Type Phase Coupling

### The coupling energy

**When the two components are two states of one field, their phases can lock, and the locking has a Josephson form.** With $S_{\tilde\Xi,\mathrm{sup}}$ and $S_{\tilde\Xi,\mathrm{nrm}}$ the phases of the two contributions and $\delta S=S_{\tilde\Xi,\mathrm{nrm}}-S_{\tilde\Xi,\mathrm{sup}}$ their difference, the coupling energy per unit proper volume is

$$
e_{\mathrm{cpl}}=-\,E_{J}\cos\left(\frac{\delta S}{\hbar}\right),
$$

with $E_{J}$ the coupling energy density. **The display is the standard Josephson form and is quoted**; what the corpus adds is the argument: the phase is the quantity that the polar form assigns to the rotor, and a coupling between the two components is a coupling between two phases.

**The current between the components follows by differentiation of the coupling energy with respect to the phase difference.** With $J_{\Phi,\mathrm{ex},\eta}$ the exchange current, the result is that **the exchange current is the critical current times the sine of the phase difference**, $J_{\Phi,\mathrm{ex},\eta}=J_{\mathrm{c}}\sin(\delta S/\hbar)$. The constant $J_{\mathrm{c}}$ is convention-dependent — it absorbs the normalisation of the phase, of the charge and of the density — and the corpus quotes the structural form rather than fixing a constant that the Josephson literature already fixes differently in different unit systems. **A reader who needs the numerical value of $J_{\mathrm{c}}$ for a specific system will find it in the references at the end.**

**What the phase difference does when the two flows coincide.** Then $\delta S$ is constant, the sine is constant, and the exchange current is a constant flow between the components with no relative acceleration — the DC case. **When the two flows differ, $\delta S$ advances at the rate $d(\delta S)/dR_t=\mu_{\mathrm{chm,nrm}}-\mu_{\mathrm{chm,sup}}$**, and the exchange current oscillates at the frequency

$$
\omega_{\mathrm{Jsn}}=\frac{\mu_{\mathrm{chm,nrm}}-\mu_{\mathrm{chm,sup}}}{\hbar},
$$

the AC case. **The frequency is fixed by the chemical potential difference and by nothing else**, and it is the cleanest experimental signature that the two components are two states of one field rather than two fluids.

**A number, for scale.** With a chemical potential difference of $1\,\mathrm{meV}$, $\omega_{\mathrm{Jsn}}=1.5193\times10^{12}\,\mathrm{s^{-1}}$, using $\hbar=6.582\,119\,569\times10^{-16}\,\mathrm{eV\,s}$. At $1\,\mu\mathrm{eV}$ the frequency is $1.5193\times10^{9}\,\mathrm{s^{-1}}$ and at $1\,\mathrm{neV}$ it is $1.5193\times10^{6}\,\mathrm{s^{-1}}$; **the three span the range from microwave to radio**, which is why the effect is measured electrically.

### What the coupling does to the entropy

**The phase coupling is conservative and produces no entropy by itself, and this is the difference between it and the friction.** A cosine potential's work along a closed cycle vanishes, so the exchange current does no net work on the state; **the production comes from the friction, and the coupling only moves the two components' flows relative to one another.** The article states the separation because a reader who merges the two mechanisms will double count the dissipation.

**The two mechanisms do meet, in the equations of motion.** The chemical potential difference that drives the phase is itself changed by the friction, which heats the normal component and changes $\mu_{\mathrm{chm,nrm}}$; **so the coupling's frequency is damped by the friction**, and the damped Josephson oscillation is the standard description of a two-component system relaxing to coincidence. **The article names the structure and does not solve the damped equation**, which is a calculation for a specific state and not a statement of the model.

## The Zero-Temperature Limit

### The limit, taken explicitly

**At $T\to0$ the normal density vanishes, the entropy density vanishes with it, and the two-fluid equations collapse to the polar-form equations. The article shows the collapse in four displays.**

**First, the densities.** With $\rho_{\mathrm{num,nrm}}\to0$ and $x_{\mathrm{nrm}}\to0$,

$$
\rho_{\mathrm{num}}\longrightarrow\rho_{\mathrm{num,sup}},
\qquad
s_{\mathrm{ent}}\longrightarrow0 ,
$$

the second being the statement that the entropy density is a function of the normal fraction and vanishes with it.

**Second, the friction.** $\tilde F_{\Phi,\mathrm{fr}}\to0$ because it carries $\rho_{\mathrm{num,nrm}}$ as a factor, so the two stress equations become

$$
\mathrm{Sc}\bigl(\tilde\nabla^{\natural}\tilde\Sigma_{\Psi,\mathrm{sup}}\bigr)=0,
\qquad\text{that is}\qquad
\tilde\nabla^{\natural}\tilde\Sigma_{\Psi,\mathrm{sup}}=0,
$$

in the element spelling of §*The two stress equations*, which is the form the article carries throughout; the scalar and spatial slots of that one display are the two conservation laws. **The normal component's equation is not a second condition**: its element is the zero element at $T=0$, so the equation reads $0=0$ and constrains nothing.

**Third, the flow.** $\tilde V_{\Phi,\mathrm{nrm}}$ becomes undefined — its defining density is zero, so the element it is built from is the zero element divided by zero — and the only surviving flow is the condensate's, $\tilde V_{\Phi,\mathrm{sup}}$, whose equation is the polar form's own with the quantum stress as its energy-momentum. **The undefined normal flow is the correct limit and not a defect**: a component with no density has no velocity, and the article says so rather than letting the reader divide.

**Fourth, the entropy current.** $\tilde J_{\Phi,\mathrm{ent}}\to0$, the second law reads $0\ge0$, and the state is the pure state whose fluid [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html) builds. **All four displays together are the statement that the $T\to0$ limit of the two-fluid model is the one-fluid model of the polar form**, and the limit is exact and not asymptotic because every term that disappears carries a positive power of $\rho_{\mathrm{num,nrm}}$ or of the fraction.

### The limit's subtlety

**The limit is exact in the densities and singular in the flow, and the singularity is physical.** The normal velocity is undefined at $T=0$ because there is nothing that moves; a reader who insists on a value is asking for the velocity of an absence. **The polar-form article has one flow, and the two-fluid model's second flow does not tend to it — it ceases to exist**, which is a stronger and correct statement.

**The other end of the range, $x_{\mathrm{sup}}\to0$, is the ordinary fluid.** There the condensate's density vanishes, the friction vanishes with the product, the phase coupling has no condensate to couple to, and the equations are the single-fluid dissipative equations of [Causal Dissipative Hydrodynamics in Biquaternionic Form](causal-dissipative-hydrodynamics-in-biquaternionic-form.html). **Both ends are limits of the same two-fluid equations**, which is the check that the model interpolates and does not merely add.

**A table of the entropy density against the normal fraction**, with the illustrative law $s_{\mathrm{ent}}=s_{0}\,x_{\mathrm{nrm}}^{2/3}$, which is the behaviour of a non-relativistic excitation gas:

| $x_{\mathrm{nrm}}$ | $s_{\mathrm{ent}}/s_{0}$ |
|---|---|
| $0.5$ | $0.629\,961$ |
| $0.3$ | $0.448\,140$ |
| $0.1$ | $0.215\,443$ |
| $0.01$ | $0.046\,416$ |

**The table is not a derivation of the law and is not offered as one**; it is the arithmetic of the limit, showing that the entropy density goes to zero with the normal fraction at a rate that is steeper than linear. **The law itself is a property of the excitation gas and belongs to a statistical-mechanical article, not to this one.**

## What the Algebra Supplies and What It Does Not

**The algebra supplies one thing that the component formulation has to state as an assumption: the two flows are elements with a common normalisation and a relative element that has a norm.** Once that is written, "the two components move together" is the statement $\tilde W_\Phi=0$, "the friction is proportional to the relative flow" is a statement about an element, and the $T\to0$ limit is a limit of a coefficient in front of an element. **In components, the same three statements are three separate conventions about index placement, and keeping them consistent is the part of the calculation that goes wrong.**

**The algebra does not supply the split itself.** That $\rho_{\mathrm{num}}$ decomposes into a condensate part and a normal part is a statement about the state's excitation spectrum, and no amount of algebra produces the decomposition or the fractions. **The corpus marks the split as imported, with the helium literature as its source, and the article's contribution is the two elements and their coupling.**

**The algebra does not supply the friction coefficient either.** $B_{\mathrm{frc}}$ is a transport coefficient like the viscosity, and the second law constrains its sign and nothing else. **A derivation of $B_{\mathrm{frc}}$ from the rotor's equation of motion is not in the category**, and [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html) is the nearest article to that derivation without being it.

## What Is Established and What Is Interpretation

**Established, and standard.** That a quantum fluid at finite temperature admits a two-fluid description with a condensate that carries no entropy and a normal component that carries all of it; that the condensate's flow is a gradient and therefore irrotational; that the two components exchange momentum and that only the total stress is conserved; that mutual friction produces entropy at a rate proportional to the square of the relative speed to leading order in that speed, and vanishing when the two flows coincide; that a phase coupling between the two components has the Josephson form, with a DC exchange current proportional to the sine of the phase difference and an AC frequency equal to the chemical potential difference over $\hbar$; that the $T\to0$ limit is the one-fluid model.

**The framework's contribution.** The two flows are elements with a common normalisation, the relative flow is their difference and its quaternionic norm measures the departure from coincidence, and the $T\to0$ limit is exact because every term that disappears carries a positive power of the normal density. **The articles' contribution is structural: it makes the model's two central statements — the split and the coupling — statements about elements rather than about index conventions.**

**Interpretation, and marked as such.** That the entropy density is a function of the normal fraction alone, with the illustrative $x_{\mathrm{nrm}}^{2/3}$ of the table, is the corpus's reading of the excitation-gas result and not a derivation. That the phase coupling's frequency is damped by the friction is stated as a structure and not solved.

**Not claimed.** That the split has been derived from the field's equation of motion — it has not. That the friction coefficient has been computed — it has not. That the two-fluid equations have been shown to be causal — that is [Causal Dissipative Hydrodynamics in Biquaternionic Form](causal-dissipative-hydrodynamics-in-biquaternionic-form.html)'s subject, and the two-fluid model's relaxation structure is not written here. That the model applies to a specific laboratory system — it does not claim to.

## Summary

The two-fluid model writes two flow elements, $\tilde V_{\Phi,\mathrm{sup}}=\tilde P_{\Phi,\mathrm{sup}}/m$ and $\tilde V_{\Phi,\mathrm{nrm}}=\tilde P_{\Phi,\mathrm{nrm}}/m$, each with $\langle\tilde V\rangle_{\natural}=-c^{2}$, built from a split $\rho_{\mathrm{num}}=\rho_{\mathrm{num,sup}}+\rho_{\mathrm{num,nrm}}$ of the proper density. The relative element $\tilde W_\Phi=\tilde V_{\Phi,\mathrm{nrm}}-\tilde V_{\Phi,\mathrm{sup}}$ vanishes exactly when the two components move together, which is the equilibrium condition and the state in which no entropy is produced.

The condensate carries no entropy, $s_{\mathrm{ent,sup}}=0$, because it is a pure state and the corpus's functional vanishes there; it carries the quantum stress instead, with $p_{\mathrm{qnt}}$ its pressure. The normal component carries all the entropy, $s_{\mathrm{ent,nrm}}=s_{\mathrm{ent}}$, and its equations are the single-fluid equations read on its own flow. Neither component's stress is conserved alone: $\tilde\nabla^{\natural}\tilde\Sigma_{\Psi,\mathrm{nrm}}=\tilde F_{\Phi,\mathrm{fr}}=-\tilde\nabla^{\natural}\tilde\Sigma_{\Psi,\mathrm{sup}}$, and only the sum is conserved.

Mutual friction is $\tilde F_{\Phi,\mathrm{fr}}=(\rho_{\mathrm{num,sup}}\rho_{\mathrm{num,nrm}}/\rho_{\mathrm{num}})B_{\mathrm{frc}}\tilde W_\Phi$, with the exact production $\sigma_{\mathrm{ent}}=-T^{-1}\mathrm{Sc}(\tilde F_{\Phi,\mathrm{fr}}\tilde W_\Phi)=T^{-1}(\rho_{\mathrm{num,sup}}\rho_{\mathrm{num,nrm}}/\rho_{\mathrm{num}})B_{\mathrm{frc}}(\lvert\vec w\rvert^{2}-w_t^{2})\ge0$, which reduces to $T^{-1}(\rho_{\mathrm{num,sup}}\rho_{\mathrm{num,nrm}}/\rho_{\mathrm{num}})B_{\mathrm{frc}}w^{2}$ to leading order in the relative speed. Evaluated once at $\rho_{\mathrm{num,sup}}=0.7$, $\rho_{\mathrm{num,nrm}}=0.3$, $B_{\mathrm{frc}}=0.1$, $w=0.2$ and $T=2$, the force is $0.004\,200\,000\,000$ and the production is $0.000\,420\,000\,000$.

The phase coupling is $e_{\mathrm{cpl}}=-E_{J}\cos(\delta S/\hbar)$, an exchange current $J_{\mathrm{c}}\sin(\delta S/\hbar)$ and an AC frequency $\omega_{\mathrm{Jsn}}=\delta\mu_{\mathrm{chm}}/\hbar$, which is $1.5193\times10^{12}\,\mathrm{s^{-1}}$ for $1\,\mathrm{meV}$. The coupling is conservative and produces no entropy; the friction does, and the two meet only through the chemical potential difference that the friction changes.

The $T\to0$ limit is exact and shown in four displays: $\rho_{\mathrm{num}}\to\rho_{\mathrm{num,sup}}$, $s_{\mathrm{ent}}\to0$, $\tilde F_{\Phi,\mathrm{fr}}\to0$ so that $\tilde\nabla^{\natural}\tilde\Sigma_{\Psi,\mathrm{sup}}=0$, and $\tilde J_{\Phi,\mathrm{ent}}\to0$ with the second law saturated. The normal flow does not tend to the condensate's flow; it ceases to exist. **The remaining flow is the polar-form article's, and the two-fluid model is its finite-temperature extension.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde V_{\Phi,\mathrm{sup}}=\tilde P_{\Phi,\mathrm{sup}}/m$ | Condensate flow element |
| $\tilde V_{\Phi,\mathrm{nrm}}=\tilde P_{\Phi,\mathrm{nrm}}/m$ | Normal-component flow element |
| $\chi_\mu$ | Rotor contribution to the superfluid momentum, zero for the scalar field |
| $e_t$ | Unit temporal direction |
| $\tilde W_\Phi$ | Relative flow element |
| $v_{\Phi,\mathrm{sup},\mu}$, $v_{\Phi,\mathrm{nrm},\mu}$ | Components of the two flows, low |
| $w_\mu=v_{\Phi,\mathrm{nrm},\mu}-v_{\Phi,\mathrm{sup},\mu}$ | Relative component, low; its temporal entry $w_t$ is imaginary |
| $w^{2}=\lvert\vec v_{\mathrm{nrm}}-\vec v_{\mathrm{sup}}\rvert^{2}$ | Squared relative speed, the literature's variable; not $\lvert\vec w\rvert^{2}$ |
| $\rho_{\mathrm{num}}=\lVert\tilde\Xi\rVert^{2}$ | Proper density |
| $\rho_{\mathrm{num,sup}}$, $\rho_{\mathrm{num,nrm}}$ | Its condensate and normal parts |
| $x_{\mathrm{sup}}$, $x_{\mathrm{nrm}}$ | The two fractions |
| $s_{\mathrm{ent}}$, $s_{\mathrm{ent,sup}}$, $s_{\mathrm{ent,nrm}}$ | Entropy densities |
| $\tilde J_{\Phi,\mathrm{ent}}$ | Entropy current, Hermitian |
| $\tilde\Sigma_{\Psi,\mathrm{sup}}$, $\tilde\Sigma_{\Psi,\mathrm{nrm}}$ | The two energy–momentum elements |
| $\tilde F_{\Phi,\mathrm{fr}}$ | Friction element |
| $B_{\mathrm{frc}}$ | Friction coefficient |
| $\sigma_{\mathrm{ent}}$ | Entropy production |
| $T$, $\beta$ | Temperature, imaginary-time circumference |
| $E_{J}$, $e_{\mathrm{cpl}}$ | Coupling energy density and density per volume |
| $\delta S=S_{\tilde\Xi,\mathrm{nrm}}-S_{\tilde\Xi,\mathrm{sup}}$ | Phase difference |
| $J_{\Phi,\mathrm{ex},\eta}$, $J_{\mathrm{c}}$ | Exchange current and critical current |
| $\omega_{\mathrm{Jsn}}$ | Josephson frequency |
| $\mu_{\mathrm{chm,sup}}$, $\mu_{\mathrm{chm,nrm}}$ | Chemical potentials |
| $\zeta$, $\eta_{\mathrm{sh}}$, $\kappa_{\mathrm{th}}$ | Viscosities and conductivity |
| $Q_{\mathrm{qnt}}$, $p_{\mathrm{qnt}}$ | Quantum potential and quantum pressure |
| $\gamma_{\mathrm{sup}}$, $\gamma_{\mathrm{nrm}}$ | Boost factors of the two components |
| $\langle\ \rangle_{\natural}$, $\mathrm{Sc}$ | Quaternionic norm, scalar part |
| $\hbar$, $m$, $c$ | Planck constant, mass, speed of light |

## Further Reading

- W. Israel, "Relativistic Thermodynamics, Thermofield Statistics and Superfluids," *Journal of Non-Equilibrium Thermodynamics* **11** (1986) 295, for the two-fluid thermodynamics in a relativistic setting, which is this article's background.
- L. D. Landau, "Theory of the superfluidity of helium II," *Physical Review* **60** (1941) 356–358, for the original two-fluid model.
- L. Tisza, "Transport phenomena in helium II," *Nature* **141** (1938) 913, for the two-fluid hypothesis.
- I. M. Khalatnikov, *An Introduction to the Theory of Superfluidity* (Benjamin, 1965), for the mutual friction and the normal-component hydrodynamics.
- W. F. Vinen, "Mutual friction in a heat current in liquid helium II," *Proceedings of the Royal Society A* **240** (1957) 114–127, for the friction coefficient's experimental form.
- B. D. Josephson, "Possible new effects in superconductive tunnelling," *Physics Letters* **1** (1962) 251–253, for the phase coupling and the AC frequency.
- P. W. Anderson, "Considerations on the flow of superfluid helium," *Reviews of Modern Physics* **38** (1966) 298–310, for the Josephson relation in the neutral superfluid.
- D. T. Son, "Hydrodynamics of relativistic systems with broken continuous symmetries," *International Journal of Modern Physics A* **16** (2001) 1284–1286, for the relativistic superfluid's hydrodynamics.
- The companion articles: [The Local Entropy Current](the-local-entropy-current.html), [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html), [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), and [Causal Dissipative Hydrodynamics in Biquaternionic Form](causal-dissipative-hydrodynamics-in-biquaternionic-form.html).
