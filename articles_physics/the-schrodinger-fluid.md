# __The Schrödinger Fluid__

## Introduction

**The Schrödinger equation's fluid is the one member of the block on which the fluid reading closes with no qualification at all.** [The Klein–Gordon Fluid](the-klein-gordon-fluid.html) meets the reverse map's criterion with two qualifications, and both are consequences of its equation being second order in time: its four-velocity is a unit only where the quantum potential vanishes, and its acceleration law carries the factor $\gamma^{-1}$. In the first-order case the two qualifications are not repaired, they are absent. The velocity is a velocity, the force is a gradient, and nothing has to be added to say so.

**The article is the rung below the scalar fluid, and it is placed here for that reason.** The block is grouped by spin, so the scalar field's fluid belongs with the scalar field's fluids; the relativistic member is not the only one, it is the higher one. The ladder is Euler, then the free and the charged first-order fluids, then the free and the charged Klein–Gordon fluids, and each rung is the one above it with one structure removed rather than one structure corrected.

**What the article supplies, in five statements.**

- The velocity is the phase gradient over the mass, and its acceleration is minus one gradient: $\mathrm{D}\vec v/\mathrm{D}t=-\nabla(V+Q)/m$, with inertia $m$ and no factor of $\gamma$.
- The density the fluid carries is the conserved density. The marker density and the conserved density coincide here, which is the only rung on which they do, and there is one sheet rather than two.
- The quantum term is an exact stress, $\sigma^{Q}_{ij}=\frac{\hbar^{2}}{4m}\rho_{\mathrm{num}}\,\partial_{i}\partial_{j}\ln\rho_{\mathrm{num}}$, whose divergence is the force. It is neither isotropic nor a function of the density's value, so the absence of an equation of state is a theorem and not a convention.
- The vorticity is the curl of the three-velocity and needs no frame caveat, because the three-velocity is a three-vector and not the spatial part of a four-vector. The flow is irrotational, and the statement is unconditional.
- The second-order article's argument against viscosity does not transfer as stated. What transfers is the reversibility, and it survives as an anti-linear involution rather than as a parity.

**The article is a reading and not a derivation.** The word, the pair and the current are [The Schrödinger Equation in Biquaternionic Polar Variables](the-schrodinger-equation-in-biquaternionic-polar-variables.html), §*The Central Field*. This article takes them and asks what the object is in the vocabulary a fluid is described by: what its density is, what its velocity is, what accelerates it, what its vorticity is, and what plays the role of a pressure. Nothing here is a new solution, and the pair is not re-derived.

**Conventions.** The algebra and the word are the polar article's: $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon\,e_t$ on a central field, with $r>0$, $\theta_{\mathrm{pha}}\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ and $\varepsilon=\pm1$ the branch. The density is $\rho_{\mathrm{num}}=r^{2}=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$, the action is $S=\hbar\theta_{\mathrm{pha}}$, and the quantum potential is $Q=-\hbar^{2}\Delta r/(2mr)$. Time is $t'$; $\nabla$ and $\Delta$ are the flat spatial operators of the material sector; $\hbar$ is written explicitly and no wave number is used. Where the companion's relativistic letters appear they are the companion's: $\rho_{\mathrm{chg}}$, $\gamma$, $\tilde V_{\Phi}$.

## The Word Collapses

**The field is taken central**, $\tilde\Xi=\Xi_t e_t$, so the whole field is one complex coefficient. The restriction loses no structure of the equation, because nothing in a central Hamiltonian couples that coefficient to the other three; it is a choice of subject, and the general field is the polar article's.

**Two factors have no data.** The boost needs a rapidity and an axis, and a central element supplies neither, so $\tilde U_{\Psi,\mathrm b}=e_t$. The rotor needs an angle and an axis, and a central element supplies neither, so $\tilde u_{\mathrm r}=\varepsilon e_t$, a sign. The word collapses to

$$
\boxed{\;\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\varepsilon\,e_t\;}
\qquad
\rho_{\mathrm{num}}=r^{2},\quad
S=\hbar\theta_{\mathrm{pha}},\quad
\varepsilon=\pm1 .
$$

**Three data remain at each event, and they are the fluid's.**

| datum | range | symbol | what it is |
| --- | --- | --- | --- |
| scale | $r>0$ | $\rho_{\mathrm{num}}=r^{2}$ | density of the markers |
| angle | $\theta_{\mathrm{pha}}\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ | $S=\hbar\theta_{\mathrm{pha}}$ | action, defined modulo $2\pi\hbar$ |
| branch | $\varepsilon=\pm1$ | $\varepsilon$ | sign of the coefficient, deposited by the half turn |

**The count closes.** Three real data against the two real components of one complex coefficient, and the third is the half turn that the angle's range excludes. A reader who counts two has forgotten that the angle runs over a half-turn and that the other half is the sign.

**The branch is a datum and not a variable of the flow.** Nothing in the pair moves it: the continuity equation is even in $\varepsilon$ and the Hamilton–Jacobi equation does not contain it, so the sign is constant along the flow and can change only where the density vanishes. That is the nodal set, and it is the next rung's subject as much as this one's.

**There is no gauge freedom to fix and no free function to choose.** The field has eight real components, the word has eight real parameters, and the equation is first order in time with one complex equation per coefficient, that is eight real equations. The word is therefore exactly determined by the field. The four parameters that Madelung's form does not show are the boost's three and the rotor's angle, and they are zero because the field is central, not because a choice was made.

## The Pair

**Substituting the word into the equation replaces one complex equation by two real ones, exactly.** With $S=\hbar\theta_{\mathrm{pha}}$,

$$
\boxed{\;\frac{\partial S}{\partial t'}+\frac{\lvert\nabla S\rvert^{2}}{2m}+V+Q=0,\qquad
\frac{\partial \rho_{\mathrm{num}}}{\partial t'}+\nabla\cdot\Bigl(\rho_{\mathrm{num}}\frac{\nabla S}{m}\Bigr)=0,\;}
$$

with

$$
Q=-\frac{\hbar^{2}}{2m}\frac{\Delta r}{r}
=-\frac{\hbar^{2}}{4m}\Bigl(\Delta\ln\rho_{\mathrm{num}}+\tfrac12\lvert\nabla\ln\rho_{\mathrm{num}}\rvert^{2}\Bigr).
$$

The first is a Hamilton–Jacobi equation with one extra term and the second is the conservation of the density along the flow it defines. The pair is equivalent to the equation in both directions: every solution gives a pair, and every nowhere-zero solution of the pair gives a field. The equivalence is exact and no term is an approximation.

**The operator in $Q$ is the Laplacian and not the d'Alembertian**, because the equation is first order in time and second order in space. This is the whole of the difference between this fluid's quantum term and the companion's, and it is a difference of operator and not of coefficient.

**The pair is the reverse Madelung map at zero pressure.** [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html) builds $\psi$ from a barotropic irrotational inviscid flow and finds that the equation it produces is linear exactly when the pressure is constant. This fluid is that case, with the Korteweg term carried as the second-gradient stress the map requires. The map's own caveat applies and is not evaded: the pressureless member is not an ordinary fluid, and what it is, is a dust whose only force is the second-gradient one.

**The direction article's pressureless row is this fluid, and its third row is this fluid's equation with $V\ne0$.** The pressureless row is the only place in that table where a fluid produces a free linear equation, and this article is that row's instance. The third row is the irrotational inviscid flow whose pressure is not a function of the density, whose inverted equation is linear with a potential of position: this fluid with $V\ne0$ has exactly that equation, with one difference of mechanism — its potential is imposed from outside rather than produced by the fluid's own pressure. One output, two routes, and [The Direction of the Fluid-Wave Correspondence, Field by Field](the-direction-of-the-fluid-wave-correspondence-field-by-field.html) states the output abstractly.

**The pair is unconstrained.** One equation defines the phase's rate and one defines the density's, and neither restricts the other's initial function. That is the structural difference from the companion, where the four-velocity is a unit and the flow is therefore bounded: here nothing fixes $\lvert\vec v\rvert$, and the velocity is whatever the phase's gradient is.

## The Density the Fluid Carries

**There is one density and it is both the marker density and the conserved density.**

$$
\rho_{\mathrm{num}}=r^{2}>0,
\qquad
\frac{\partial\rho_{\mathrm{num}}}{\partial t'}+\nabla\cdot\bigl(\rho_{\mathrm{num}}\vec v\bigr)=0,
\qquad
\vec v=\frac{\nabla S}{m},
\qquad
\vec j=\rho_{\mathrm{num}}\vec v .
$$

**The two densities of the companion are one quantity here, and the reason is the order of the equation.** In the second-order case the temporal slot of the current is $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$, a signed quantity that differs from the marker density by the Lorentz factor; here the density is a norm and not the temporal slot of a current, so it has no sign to lose and no factor to acquire. The identification $\gamma\to1$ is not an approximation made for convenience; it is that there is no $\gamma$ in the equation to be one.

**Consequences, and they are three.** The density is positive by construction, because it is $\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ and that Hermitian form is positive. It cannot change sign, so there is no second sheet and the fluid has no antiparticle in its data. And the continuity equation is the imaginary part of the wave equation, so conservation and the equation are one statement rather than two that agree.

**What the fluid does not carry is a charge.** There is no sign, no sheet and no antiparticle, and the reason is that the first-order equation organizes its solutions by nothing: it fixes the evolution of the density and says nothing about what the density counts. The counting is the second quantization's, and it is not this block's.

## The Euler Equation

**A fluid's acceleration law is the gradient of its energy equation, and here that gradient is one line.** Differentiating the Hamilton–Jacobi equation in space, with $\vec v=\nabla S/m$ and $\nabla\partial_{t'}S=m\,\partial_{t'}\vec v$,

$$
\frac{\mathrm{D}\vec v}{\mathrm{D}t}\equiv\frac{\partial\vec v}{\partial t'}+\bigl(\vec v\cdot\nabla\bigr)\vec v
=-\frac{1}{m}\nabla\bigl(V+Q\bigr).
$$

**The inertia is $m$ and there is no factor of $\gamma$.** The companion's law is $\mathrm{d}\vec p/\mathrm{d}t=-\gamma^{-1}\nabla Q_{\mathrm{qnt}}$ with $\vec p=m\gamma\vec v$, and the $\gamma^{-1}$ is the relativistic inertia: the same gradient accelerates a fast flow less. Here the gradient accelerates every flow equally, and the reason is that the velocity is not bounded and not normalised.

**The velocity is a velocity and not a momentum.** In the companion the flow variable is $\tilde P_{\Phi}/m$, a four-vector whose norm the equation fixes, and it deserves the name of a velocity only where the quantum potential vanishes. Here $\vec v=\nabla S/m$ is the three-velocity and there is nothing for it to be a unit of. That is the first of the two qualifications removed, and the removal is not an improvement of the analysis: it is that the first-order equation has no norm to impose.

**The acceleration is minus the gradient of one scalar, and the scalar is $V+Q$.** So the reverse map's force item is met exactly, with no factor and no frame qualifier, and the potential item is met degenerately by $V=0$, and where $V$ is an external function of position the item is met by a potential of position and not of the density — the concession the direction article's third row makes. The four items of the criterion are therefore met as follows: the velocity is a gradient, so the flow is irrotational; the acceleration is minus the gradient of $V+Q$; the potential is $V=0$ or an external field; and the viscosity item is treated separately below, because it is the one item whose argument changes.

## The Vorticity, and Why There Is No Frame Artefact

**The velocity is a gradient, so the vorticity vanishes wherever the action is twice differentiable.**

$$
\vec\omega=\nabla\times\vec v=\frac{1}{m}\nabla\times\nabla S=0
$$

**This is the vorticity and not a frame artefact, and that is a difference of kind from the companion.** There, only $\gamma\vec v$ is the spatial part of a four-vector, so $\nabla\times\vec v=\nabla(1/m\gamma)\times\vec p$ need not vanish and is not the vorticity. Here $\vec v$ is a three-vector in its own right, its curl is the vorticity by definition, and the statement needs no qualifier. It is the only rung of the block on which the vanishing of $\nabla\times\vec v$ is itself the vorticity statement, and not a remark about a quantity that is something else.

**The circulation is quantised by the nodes and not by the flow.** Around a loop that links a nodal line,

$$
\oint\vec v\cdot\mathrm{d}\vec l=\frac{2\pi\hbar\,n}{m},
$$

with $n$ the winding of the phase, and around a loop that links none it is zero. That is [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html)'s statement read on $\vec v$, and the coupling of the companion article adds the flux term that this rung cannot have.

**The rank is zero and the price is the same as in the companion.** A flow whose vorticity vanishes carries no rotation, and the helicity $\vec v\cdot\vec\omega$ vanishes identically. One function cannot hold two data, and the scalar field has one function; the price is paid at every rung of the ladder that carries a scalar, and it is repaid only by the spinor's rotor.

## The Quantum Term Is a Stress, Exactly

**The quantum force is the divergence of a symmetric tensor, and the tensor is two derivatives of the logarithm of the density.**

$$
\sigma^{Q}_{ij}=\frac{\hbar^{2}}{4m}\rho_{\mathrm{num}}\,\partial_{i}\partial_{j}\ln\rho_{\mathrm{num}},
\qquad
\partial_{j}\sigma^{Q}_{ij}=-\rho_{\mathrm{num}}\,\partial_{i}Q .
$$

*Proof.* With $f=\ln\rho_{\mathrm{num}}$, so that $\partial_{i}\rho_{\mathrm{num}}=\rho_{\mathrm{num}}f_{i}$,

$$
\partial_{j}\sigma^{Q}_{ij}=\frac{\hbar^{2}}{4m}\bigl(\rho_{\mathrm{num}}f_{j}f_{ij}+\rho_{\mathrm{num}}\partial_{i}\Delta f\bigr),
\qquad
-\rho_{\mathrm{num}}\partial_{i}Q=\frac{\hbar^{2}}{4m}\rho_{\mathrm{num}}\bigl(f_{j}f_{ij}+\partial_{i}\Delta f\bigr),
$$

using $\Delta r/r=\tfrac12\Delta f+\tfrac14\lvert\nabla f\rvert^{2}$, and the two agree term by term. The identity was also checked symbolically on a general smooth density, with all three components of the divergence vanishing identically.

**Its trace is not the quantum potential, and that is the measure of its anisotropy.**

$$
\sigma^{Q}_{ii}=-\rho_{\mathrm{num}}Q-\frac{\hbar^{2}}{8m}\rho_{\mathrm{num}}\lvert\nabla\ln\rho_{\mathrm{num}}\rvert^{2},
$$

so the trace is $-\rho_{\mathrm{num}}Q$ corrected by a gradient-squared term, and the mean stress equals minus the quantum potential only where the density is uniform. A fluid whose stress is isotropically $-Q$ would have a pressure; this one does not.

**No function of the density's value reproduces the force.** $\sigma^{Q}_{ij}$ carries two derivatives of $\ln\rho_{\mathrm{num}}$, so two density fields that agree at an event and differ in curvature have different stresses and different forces there. There is therefore no equation of state in the algebraic sense, and the absence is the same theorem as the companion's, at the rung where the Korteweg term is the whole of the stress.

**The stress is the companion's three-by-three block, and the identity is unconditional at this rung.** [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html) writes the stress as one element of $\mathbb{B}$ with an energy density, a stress and a flux in it, and the block it exhibits is the same tensor written here: $\sigma_{j\eta}=\frac{\hbar^{2}}{4m}\rho_{\mathrm{num}}\partial_j\partial_\eta\ln\rho_{\mathrm{num}}$ is that article's $\frac{\hbar^{2}}{4m}[\partial_j\partial_\eta\rho_{\mathrm{num}}-\rho_{\mathrm{num}}^{-1}\partial_j\rho_{\mathrm{num}}\partial_\eta\rho_{\mathrm{num}}]$ with the logarithm written out. **What changes is the operator, and with it the scope of the identity.** The companion's quantum potential carries the d'Alembertian, so its divergence identity holds for an amplitude stationary in the material time; here the quantum potential carries the Laplacian, so the identity holds for every solution and no static caveat is needed. The flux and the energy density have no separate existence at this rung — the equation has one time derivative — and the three-by-three block is all the stress there is.

## The Anti-Viscosity Argument Does Not Transfer

**The companion's bar against viscosity is an argument from the parity of the operator, and this equation does not have that parity.** There $\Box_\Phi$ is second order and even in $\partial_{t'}$, with a real coefficient, so the equation is invariant under $t'\to-t'$ and under complex conjugation separately; a viscous term is first order in time, odd under the reversal and of fixed sign, so no such term can appear. Here the first-order term *is* the leading term of the equation, and the parity argument, taken literally, has nothing to say.

**What survives is the reversibility, and it survives as an anti-linear involution.** The equation is invariant under $t'\to-t'$ together with $i\to-i$, that is under $\mathcal{T}:\tilde\Xi(t')\mapsto\tilde\Xi^{*}(-t')$. The involution is anti-linear. A dissipative term is not invariant under it, so the fluid is non-dissipative — but the bar is now a bar in the complex structure and not a bar in the order of the operator.

**The distinction is worth its paragraph because the naive transfer gets the reason wrong and the conclusion right.** A reader who says "the Schrödinger equation is first order in time, therefore the viscosity argument fails" has concluded that the fluid might be viscous, which it is not; a reader who says "the algebra bars viscosity at every rung" has transferred an argument that does not apply. The correct statement is the one above: the fluid is inviscid, and the reason is that the equation's only involution is anti-linear, which is a weaker structure than the scalar field's parity and is nevertheless enough to exclude a dissipation function. [Viscosity and the Rayleigh Dissipation Function](viscosity-and-the-rayleigh-dissipation-function.html) needs a term that is odd under reversal; there is none here, and none can be added without breaking the involution.

## What the Mass Shell Was Doing

**Three quantities are removed in passing from the companion to this rung, and each removal is a visible feature of the fluid.**

| what the second-order equation supplies | what it does in the relativistic fluid | what its absence means here |
| --- | --- | --- |
| the normalisation of the four-velocity, $\tilde V\tilde V^{\natural}=-c^{2}-2Q_{\mathrm{qnt}}/m$ | bounds the flow at $\lvert\vec v\rvert<c$ wherever the shell stays timelike, and puts $\gamma$ into the inertia and into the density | no norm, no bound and no $\gamma$: $\mathrm{D}\vec v/\mathrm{D}t=-\nabla(V+Q)/m$ and $\rho_{\mathrm{chg}}=\rho_{\mathrm{num}}$ |
| the sign of the temporal slot of the current | two sheets, one future-directed and one past-directed, hence the antiparticle | one sheet; the density is a norm and cannot change sign |
| a dispersion constraint on the four-momentum | the mass shell, $E^{2}/c^{2}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2mQ_{\mathrm{qnt}}$ | none: the Hamilton–Jacobi equation defines the phase's rate and constrains nothing, and the mass enters only through the kinetic term |

**The table is the article's negative content, and it is the reason the rung is worth having.** Each row is a property that the relativistic fluid has and this one does not, and each is a property that a reader of the companion might mistake for a property of the correspondence rather than of the equation. The correspondence is the same at both rungs: an exact word, a reverse map defined on a class, and a piece of extra structure — a Korteweg stress — that makes the fluid a classical medium.

**The ladder, stated once.** The pressureless Euler equation is the $\hbar\to0$ limit of this fluid, the quantum stress vanishing with $\hbar^{2}$; the classical layer's pressure is a datum the field does not have, and the limit returns the dust rather than the general fluid. This fluid is the $\gamma\to1$ limit of the Klein–Gordon fluid, and the Klein–Gordon fluid is the charged one at $\varkappa=0$. Each limit is a deletion of one structure and not a change of kind, and the rungs together are the block's answer to the question of what a scalar field's fluid is at each order of the equation.

## What Is Established and What Is Interpretation

**Established.** The collapse of the word to three data, by the polar article's substitution. The pair, exactly, with the Laplacian in the quantum potential and no term dropped. That the marker density and the conserved density coincide, from $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ and the absence of $\gamma$. The continuity equation as the imaginary part of the wave equation. The acceleration law $\mathrm{D}\vec v/\mathrm{D}t=-\nabla(V+Q)/m$, by the gradient of the Hamilton–Jacobi equation, with inertia $m$ and no factor. The vanishing of the vorticity as the curl of the three-velocity, which is not a frame artefact because the three-velocity is a three-vector. The quantised circulation at a node, $2\pi\hbar n/m$. The stress identity $\partial_{j}\sigma^{Q}_{ij}=-\rho_{\mathrm{num}}\partial_{i}Q$ with $\sigma^{Q}_{ij}=\frac{\hbar^{2}}{4m}\rho_{\mathrm{num}}\partial_{i}\partial_{j}\ln\rho_{\mathrm{num}}$, verified term by term and symbolically. Its trace and its anisotropy. The absence of an algebraic equation of state, from the two derivatives in the stress. That the second-order anti-viscosity argument does not transfer as stated, and that the reversibility survives as an anti-linear involution.

**Interpretation.** That the pair *is* a fluid's equations rather than a rewriting with fluid words: the warrant is the count, the types of the factors, and the fact that the pair is the reverse map's pressureless case, not a proof. That the third row of the mass-shell table — the absence of a constraint — is best read as the fluid's freedom rather than as the fluid's poverty. That the flow's irrotationality is a property of the phase rather than of the algebra is the polar article's reading and is adopted, not proved, here.

**Not claimed.** It is not claimed that the fluid is linear because its equation is: the data obey a nonlinear system, with the interference term $2\sqrt{\rho_{1}\rho_{2}}\cos((S_{1}-S_{2})/\hbar)$. It is not claimed that the quantum stress is a pressure; the trace computation says the opposite. It is not claimed that the fluid has a thermodynamics: it has no temperature and no state. It is not claimed that this rung is a new physical theory; it is the same equation read one rung lower, and its value is that it shows which of the companion's properties belong to the correspondence and which belong to the order of the equation.

## Summary

The scalar field's word collapses to a scale, an action and a branch, and the fluid carries three data at each event: the density $\rho_{\mathrm{num}}=r^{2}$, the action $S=\hbar\theta_{\mathrm{pha}}$, and the sign $\varepsilon$.

The equation separates into two real equations without remainder: a Hamilton–Jacobi equation with $Q=-\hbar^{2}\Delta r/(2mr)$ and a continuity equation for $\rho_{\mathrm{num}}$. The pair is unconstrained in both directions.

The density is at once the marker density and the conserved density, because the equation is first order in time and the density is a norm rather than the temporal slot of a current. There is one sheet, no sign and no antiparticle in the data.

The velocity is $\vec v=\nabla S/m$ and its acceleration is $\mathrm{D}\vec v/\mathrm{D}t=-\nabla(V+Q)/m$, with inertia $m$ and no factor of $\gamma$. Both of the companion's qualifications are removed, and their removal is the absence of a mass shell rather than an improvement of the analysis.

The velocity is a gradient, so the vorticity vanishes identically and the statement needs no frame caveat: $\vec v$ is a three-vector and its curl is the vorticity. The circulation is $2\pi\hbar n/m$ around a loop that links a node and zero around one that does not. The rank is zero and the helicity vanishes.

The quantum term is an exact stress, $\sigma^{Q}_{ij}=\frac{\hbar^{2}}{4m}\rho_{\mathrm{num}}\partial_{i}\partial_{j}\ln\rho_{\mathrm{num}}$, whose divergence is $-\rho_{\mathrm{num}}\nabla Q$. Its trace is not the quantum potential, and no function of the density's value reproduces it, so there is no equation of state.

The second-order anti-viscosity argument does not transfer as stated: the bar is now an anti-linear involution rather than a parity, and it still excludes a dissipation function.

The reverse map's four items are met without qualification, which is the rung's whole distinction: the velocity is a gradient, the acceleration is minus the gradient of one scalar, the potential is an external function of position — the direction article's third row, instantiated — and the flow is non-dissipative under the involution.

Three quantities of the companion are removed: the normalisation of the four-velocity, the sign of the density, and the dispersion constraint. Each removal is a feature of this fluid, and the table of the three is the article's negative content.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon\,e_t$ | The central field, in its word |
| $r$ | Amplitude; $r>0$ |
| $\rho_{\mathrm{num}}=r^{2}=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ | Density; here also the conserved density |
| $S=\hbar\theta_{\mathrm{pha}}$ | Action |
| $\varepsilon=\pm1$ | Branch of the modulus |
| $\vec v=\nabla S/m$ | Three-velocity; a gradient |
| $\vec j=\rho_{\mathrm{num}}\vec v$ | Current |
| $Q=-\hbar^{2}\Delta r/(2mr)$ | Quantum potential |
| $V$ | External potential; $V=0$ for the free field |
| $\sigma^{Q}_{ij}=\frac{\hbar^{2}}{4m}\rho_{\mathrm{num}}\partial_{i}\partial_{j}\ln\rho_{\mathrm{num}}$ | Quantum stress; $\partial_{j}\sigma^{Q}_{ij}=-\rho_{\mathrm{num}}\partial_{i}Q$ |
| $\vec\omega=\nabla\times\vec v$ | Vorticity; zero identically |
| $\mathcal{T}:\tilde\Xi(t')\mapsto\tilde\Xi^{*}(-t')$ | The anti-linear time reversal |
| $\Delta$, $\nabla$ | Laplacian and gradient on the material sector |
| $\hbar$, $m$ | Reduced Planck constant, mass |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1926) 322–326, for the pair in its original form.
- David Bohm, "A suggested interpretation of the quantum theory in terms of hidden variables," *Physical Review* **85** (1952) 166–193, for the guidance equation and the quantum potential, with the caveat that this block takes the algebra and not the ontology.
- Takehiko Takabayasi, "On the formulation of the Schrödinger theory in terms of the hydrodynamical quantities," *Progress of Theoretical Physics* **8** (1952) 143–164, for the quantum stress and its divergence read as the fluid's force.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), chapters 3 and 4, for the non-relativistic fluid's kinematics and its stress.
- Diederik J. Korteweg, "Sur la forme que prennent les équations du mouvement des fluides si l'on tient compte des forces capillaires causées par des variations de densité considérables mais continues," *Archives Néerlandaises des Sciences Exactes et Naturelles* **6** (1901) 1–24, for the class of fluids whose stress depends on the gradients of the density.
- Giovanni Manfredi, "How to model quantum plasmas," *Fields Institute Communications* **46** (2005) 263–287, for the quantum hydrodynamic model in which the stress $\sigma^{Q}_{ij}$ carries the whole of the quantum correction — the spinless, non-relativistic fluid of this article, and not the Proca fluid.
- The companion articles: [The Schrödinger Equation in Biquaternionic Polar Variables](the-schrodinger-equation-in-biquaternionic-polar-variables.html), [The Klein–Gordon Fluid](the-klein-gordon-fluid.html), [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html), [The Direction of the Fluid-Wave Correspondence, Field by Field](the-direction-of-the-fluid-wave-correspondence-field-by-field.html), [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html), and the charged companion [The Charged Schrödinger Fluid](the-charged-schrodinger-fluid.html), which adds the connection and finds that it reaches the phase and nothing else.
