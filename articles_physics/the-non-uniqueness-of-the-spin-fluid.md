# __The Non-Uniqueness of the Spin Fluid__

## Introduction

**The word is a section of a map and not the map, and "the spin fluid" is three choices made on top of it.** The map takes eight parameters to one element. The word chooses the ranges that make the map injective, and it chooses nothing else: every fluid variable is a function of the element and none of the element. That is what makes the reading a re-coordinatisation. What it does not do is fix the fluid, because a fluid also needs a density normalisation, a split of the current into a transport and a bound part, and a transport equation for the spin. The algebra supplies the first two up to a choice and does not supply the third at all.

**The three choices are independent and each has a literature.** The density can be the squared amplitude, the time component of the current or the Hermitian norm, and the three differ by factors of $\gamma$. The current splits into a convection part and a spin part by the Gordon identity, and the split is defined only up to a total divergence. The spin's transport equation is not implied by the field equation, and the tensor formulations close the system by adding a subsidiary condition whose choice is theirs. A reader who expects one spin fluid per field will find, at the end of this article, that there is one per choice of the three.

**None of the three is arbitrary, and that is the article's second point.** Each choice is constrained: the density must be the one the conservation law conserves, the split must reproduce the current, and the subsidiary condition must be compatible with the field equation. The freedom is a freedom of parametrisation inside a constraint, not a licence.

**The discrete label is not a fourth freedom.** The sign $\varepsilon$ that the polar articles carry looks like a choice and is not one: it is a function of four of the word's parameters, it is $\pm1$ exactly on the degenerate sector, a statement [The Sign ε and the Rigidity Constraint on Σ₁₀](the-sign-epsilon-and-the-rigidity-constraint-on-sigma-10.html)
turns into a theorem, and the continuous word does not carry it as data. The last section states this because a reader who has met the sign in the Dirac literature will expect it to be a branch label that a formulation may choose.

## The Map and the Section

### The Map

**The map takes the eight parameters to the element.** With $r>0$, $\theta_{\mathrm{pha}}\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$, $\theta_{\mathrm{rpd}}\ge0$ with a unit axis $\vec u_{\mathrm b}$, and $\theta_{\mathrm{axr}}\in[0,2\pi]$ with a unit axis $\vec u_{\mathrm r}$,

$$
(r,\theta_{\mathrm{pha}},\theta_{\mathrm{rpd}},\vec u_{\mathrm b},\theta_{\mathrm{axr}},\vec u_{\mathrm r})
\longmapsto
\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}.
$$

**The count is $1+1+3+3=8$ against the eight real components of an element, so the map is a map between spaces of the same dimension.** Equality of dimension is necessary for a bijection and is not sufficient for one. What makes it a bijection here is the choice of ranges together with the polar decomposition's uniqueness theorem, and the two degenerate loci are where the ranges have to work.

### The Fibres

**At $\theta_{\mathrm{rpd}}=0$ the boost axis is free, and the element does not see it.** The boost is $\cosh 0\,e_t+i\sinh 0\,\vec u_{\mathrm b}=e_t$ for every $\vec u_{\mathrm b}$, so a whole circle of parameter choices returns one element. The velocity is $-c^{2}$ times the inverse square of that boost, which is the same for all of them, so the fluid does not see the free axis either.

**At $\theta_{\mathrm{axr}}=0$ the rotor axis is free, and again the element does not see it.** The rotor is $\cos 0\,e_t+\sin 0\,\vec u_{\mathrm r}=e_t$, and the spin direction is $\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}=\vec e_z$ for every axis. Checked on two axes: with $\vec u_{\mathrm r}=\vec e_x$ and with $\vec u_{\mathrm r}=\vec e_y$ the spin direction is $(0,0,1)$ in both cases, to every printed digit.

**So the word is a section of a bundle whose fibres are circles at two loci, and the fluid variables are constant on the fibres.** That is the precise sense in which the non-uniqueness of the word is not a non-uniqueness of the fluid. The parameters that are free are exactly the parameters that no bilinear reads, and the ones that are read are the ones the ranges fix.

### What the Ranges Remove

**Dropping $r>0$ costs one discrete identification and no more.** With $r$ allowed negative, the element at $(-r,\theta_{\mathrm{pha}}+\pi)$ is the one at $(r,\theta_{\mathrm{pha}})$, because the two central factors multiply to the same complex number:

$$
(-r)e^{i(\theta_{\mathrm{pha}}+\pi)}=r\,e^{i\theta_{\mathrm{pha}}}.
$$

Checked numerically: the two parameter sets give elements differing by $3.55\times10^{-16}$ in every component, which is the floating-point zero. The range $r>0$ removes exactly this identification, and the range $\theta_{\mathrm{pha}}\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ removes the corresponding shift by a half turn.

**The ranges are therefore doing real work and are not cosmetic.** A formulation that allowed a signed amplitude would carry a discrete label, an element and its negative, and would have to say which one it meant. The corpus's choice, positive amplitude with the phase's range a half turn, puts the label into the sign of the Hermitian norm instead, and the next section states where it lands.

## One Field, Three Fluids

### The Density

**Three names for densities are in use in the corpus, and they carry two distinct numbers.** The squared amplitude $\rho=r^{2}$ and the time-dilated density $\gamma\rho$. The third name, the Hermitian norm $\langle\tilde\Xi\rangle_{*}$, is numerically the same as the second: the identity $\langle\tilde\Xi\rangle_{*}=\gamma\rho$ holds on every element of the word, so no computation distinguishes them.

| density | value | what it is |
| --- | --- | --- |
| marker density | $\rho=r^{2}$ | the scale squared; nothing conserves it on its own |
| charge density | $\gamma\rho$ | the temporal slot of the current, $J^{0}/c$; conserved by the transport equation |
| Hermitian norm | $\gamma\rho$ | the form $\langle\tilde\Xi\rangle_{*}$; a scalar under the algebra's conjugations, and equal to the charge density |

**The distinction between the last two is nominal and the article says so.** The two coincide as numbers, so a reader may take either; what differs is the object's type, a component of a four-vector against a form on the algebra. The choice that moves a number is the first: $\rho$ against $\gamma\rho$, and the factor between them is the motion's time dilation.

**The choice is forced by what one wants conserved and not by taste.** For the scalar fluid, [The Klein–Gordon Fluid](the-klein-gordon-fluid.html) shows that the conserved density is $\gamma\rho$ and not $\rho$: the transport equation becomes a continuity equation for $\gamma\rho$ and for nothing else, and the marker density obeys a different equation that carries the time dilation. So a fluid whose density is the marker density has no continuity equation, and a fluid whose density is the charge density has one.

**The same field therefore supports two fluids that differ in what their density means.** The velocities are the same, the streamlines are the same, and the density that flows is different. That is the first of the three choices, and it is invisible in the word.

### The Velocity

**The velocity is the boost's or the phase gradient's, and the two agree only in form.** For the spinor case the velocity is $\tilde V_{\Phi}=ic\tilde U_{\Psi,\mathrm b}^{-2}$, the boost's own four-velocity. For the scalar case the boost collapses to $e_t$ and the physical velocity is $\tilde P_{\Phi}/m=\tilde\nabla_\Phi S/m$.

**The two are the same four-vector when the field is on shell, and they are defined on different data.** The boost's velocity is read from the frame, the phase gradient's from the action, and the field equation is what ties them. Off shell the two are independent, which is why a fluid built on one is not the same object as a fluid built on the other.

**This is the second place where the word does not decide.** The word carries both objects: the boost is a factor and the phase is a factor. The identification of one of them with "the velocity" is the reading's step, and it is taken differently in the two cases of this block.

### The Spin

**The spin has two candidate carriers and the word supplies both.** The rotor supplies the spin direction $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$, a unit spatial vector. The axial bilinear of the field supplies the same direction with a different normalisation, and the tensor bilinear $\bar{\tilde\Xi}\Sigma_{\mu\nu}\tilde\Xi$ supplies an antisymmetric pair.

**A direction and an antisymmetric pair are not the same data until the flow is chosen.** An antisymmetric pair has six components; contracted with the flow it has three, and those three are the direction. So the two carriers agree once the flow is fixed, and the choice between them is a choice of which object one writes the transport equation for.

**This is the third place where the word does not decide, and it is where the tensor formulations differ among themselves.** Takabayasi writes the spin as the spatial part of a unit four-vector orthogonal to the velocity; the reading of Halbwachs, Hillion and Vigier writes it as a frame that the fluid carries. Both are reductions of the same six components, and the corpus has not compared them term by term. The honest statement is that the reduction is a choice and that this article does not make it.

## The Gordon Split and Its Freedom

**The current splits into a convection part and a spin part, and the split is defined up to a total divergence.** The identity is the Gordon decomposition, and its content is that a solution's current equals a convection term plus the divergence of the tensor bilinear:

$$
J_{\Phi,\mu}=\frac{\rho}{m}P_{\Phi,\mu}+\frac{1}{k_m}\partial_\nu\bigl(\bar{\tilde\Xi}\Sigma_{\mu\nu}\tilde\Xi\bigr).
$$

**The freedom is the freedom to move a curl from one term to the other.** Adding $\partial_\nu A^{\mu\nu}$ to the first term with $A$ antisymmetric and subtracting it from the second leaves the current unchanged, because the two additions cancel identically. Different choices of $A$ give different convection momenta and different spin currents, with the same $J_{\Phi}$.

**The polar word makes one choice and calls it the frame.** With $P_{\Phi}=m\tilde V_{\Phi}$ and the density $\rho$, the convection term is the word's current and the spin term is what remains. That is a definite split, and it is the one the corpus uses. It is not the only one, and the article says so because a reader comparing two formulations will otherwise take a difference of convention for a difference of physics.

**What the freedom cannot touch is the total angular momentum.** The improvement moves the spin's contribution between the orbital and the intrinsic parts and leaves the sum fixed. That is the Belinfante statement, and it is the reason the corpus can say that its own separation of the two parts by construction is a simplification rather than a loss.

## The Subsidiary Condition

**The field equation does not fix the transport of the spin, and every formulation closes the system by adding a condition.** In the algebra the statement is the non-closure of the four brackets: the derivative of the word has four terms of four types and the equation constrains them jointly without fixing any one.

**Takabayasi's closure is a condition on the curl of the momentum.** His second subsidiary condition fixes $\partial_\mu k_\nu-\partial_\nu k_\mu$ in terms of the velocity, the spin and the field strength, which makes the system self-contained and determines $k_\mu$ up to a gradient. [The Dirac Fluid and the Takabayasi Correspondence](the-dirac-fluid-and-the-takabayasi-correspondence.html) states this and grades the correspondence.

**The other closures are conditions on the spin's transport.** A condition of Frenkel type fixes the spin's time component; a condition of Weyssenhoff type fixes the spin's relation to the velocity differently. Each gives a different evolution for the spin and the same evolution for the density and the current at the level of the conservation laws.

**Two fluids with different subsidiary conditions are therefore two solutions of the same field in different variables.** They agree on $\rho$ and $J_{\Phi}$ and disagree on how the spin is transported. That is the third choice, and it is the one the corpus leaves most open: no article derives which condition the biquaternion Dirac equation prefers.

## The Discrete Label

**The sign $\varepsilon=\Xi_t/\Rho$ is a function of four parameters and not an independent datum.** Its display is

$$
\varepsilon=\cosh\frac{\theta_{\mathrm{rpd}}}{2}\cos\frac{\theta_{\mathrm{axr}}}{2}
-i\,\kappa\,\sinh\frac{\theta_{\mathrm{rpd}}}{2}\sin\frac{\theta_{\mathrm{axr}}}{2},
\qquad
\kappa=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r},
$$

so it is complex off the orthogonal locus, it vanishes at a rotor angle of a half turn with orthogonal axes, and it is $\pm1$ exactly on the degenerate sector.

**A reader who expects a branch label is not wrong, and the label has moved.** In the standard spinor treatment the sign of the energy is a label of the solution, carried outside the spinor and chosen by the representation. Here the amplitude is positive and the phase's range is a half turn, so the sign has no separate slot: it appears as the sign of the scalar part relative to the modulus, which is $\varepsilon$. The word's ranges are what put it there.

**The consequence is that the word cannot be "continued" through $\varepsilon=0$ by a relabelling.** A formulation with a signed amplitude would pass through zero and change sign; this one has $r>0$ and the modulus $\Rho$ never vanishes on the $N$-regular set, so $\varepsilon$ has no zero to cross. The sign changes only on the locus where $\varepsilon$ is complex, and there it is not a sign.

**The article therefore counts three choices and not four.** The density, the split and the subsidiary condition are choices; the sign is derived. That is the whole of the article's answer to the question of how many spin fluids one field admits.

## What the Algebra Fixes and What the Reading Chooses

**The algebra fixes the values at a point.** The element, and therefore the current, the spin direction, the density and the phase up to the identifications of the word's fibres. Those are fixed by the field and not by the reader.

**The reading chooses the normalisation, the split and the closure.** Each choice is constrained and none is forced. The normalisation must conserve something, the split must reproduce the current, and the closure must be compatible with the field equation.

**The closure is the choice of a section, and the need for one is a general feature of a fluid with an orientation.** A medium whose velocity is a frame and whose orientation is independent has more kinematic freedom than equations, so a transport law must be supplied and the equation does not supply it; the same statement is made in the language of continuum mechanics, where a Cosserat medium needs a constitutive law for its couple stress and the balance laws alone do not fix one. **The non-uniqueness recorded here is therefore not a defect of the word; it is the price of the general case**, and the scalar fluid escapes it only because it has four parameters and four equations. [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html) places the two cases in one family.

**The strongest objection is that this makes the fluid arbitrary.** The answer is that the three choices are not free in the way the objection suggests: two fluids that differ in all three have the same streamlines, the same total angular momentum and the same conserved charges, and differ in what they say about the internal motion. A choice that changes no observable is not an arbitrariness of the physics; it is a choice of coordinates on the same state.

**The second objection is that the corpus should have made the choice once and for all.** That is a fair request and this article does not satisfy it. What it does is state where the choice is made, so that a later article can make it explicitly rather than by silence.

## What Is Established and What Is Interpretation

**Established.** That the map from parameters to elements is injective on the stated ranges except at $\theta_{\mathrm{rpd}}=0$ and $\theta_{\mathrm{axr}}=0$, where a circle of parameter choices returns one element and the fluid variables are constant on the circle. That the ranges remove the identification $(r,\theta_{\mathrm{pha}})\sim(-r,\theta_{\mathrm{pha}}+\pi)$, checked to $3.55\times10^{-16}$. That the Gordon split is defined up to a total divergence. That the sign $\varepsilon$ is a function of four parameters.

**Interpretation.** That the choice of density is a choice of fluid and not a renaming, since the two values $\rho$ and $\gamma\rho$ obey different equations. That the choice of subsidiary condition is a choice of spin fluid. That the sign's relocation into $\varepsilon$ is a consequence of the ranges rather than a convention. Each is argued here and none is proved.

**Not claimed.** It is not claimed that any of the three choices is better; the corpus has not compared them on a solution. It is not claimed that the fibre structure exhausts the non-uniqueness of the word; only the two degenerate loci are exhibited. It is not claimed that Takabayasi's and Halbwachs–Hillion's readings are equivalent; the corpus has not compared them.

## Summary

The word is a section of a map from eight parameters to one element. The map is injective on the stated ranges except at two loci, a vanishing rapidity and a vanishing rotor angle, where a circle of parameter choices returns one element. The fluid variables are constant on those circles, so the fibres cost the fluid nothing.

The ranges do real work: a signed amplitude would identify $(r,\theta_{\mathrm{pha}})$ with $(-r,\theta_{\mathrm{pha}}+\pi)$, and the corpus's choice of a positive amplitude and a half-turn phase range removes that identification.

On top of the word a fluid needs three choices: which density is conserved, how the current is split into a transport and a bound part, and which subsidiary condition closes the spin's transport. Each choice is constrained and none is forced. The sign $\varepsilon$ is not a fourth choice; it is a function of four parameters, and it is $\pm1$ only on the degenerate sector.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The element and its word |
| $r>0$, $\theta_{\mathrm{pha}}\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ | The ranges that make the map injective |
| $\rho=r^{2}$, $\gamma\rho$ | Marker density and charge density |
| $\Rho=r\,e^{i\theta_{\mathrm{pha}}}$ | Modulus of the norm |
| $\varepsilon=\Xi_t/\Rho$ | Sign, a function of four parameters |
| $\kappa=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ | Cosine between the two axes |
| $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ | Spin direction |
| $\Sigma_{\mu\nu}$ | Spin generator |
| $k_m=mc/\hbar$ | Mass wave number |

## Further Reading

- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter, Part I. General theory," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the spin fluid and its subsidiary conditions.
- F. Halbwachs, P. Hillion and J.-P. Vigier, "Lagrangian formulation of the rotational hydrodynamical model of spinning particles," *Il Nuovo Cimento* **33** (1964) 221, for the spin fluid's kinematics in a different variable set.
- Walter Gordon, "Der Comptoneffekt nach der Schrödingerschen Theorie," *Zeitschrift für Physik* **40** (1926) 117–133, for the decomposition whose freedom the split inherits.
- David Hestenes, "Space–time structure of the Dirac theory," in *Clifford Algebras and their Applications in Mathematical Physics* (Reidel, 1986), for the rotor reading of the spinor.
- The companion articles: [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html), [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html), [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html), [The Dirac Fluid and the Takabayasi Correspondence](the-dirac-fluid-and-the-takabayasi-correspondence.html), [The Current Algebra](the-current-algebra.html), [The Sign ε and the Rigidity Constraint on Σ₁₀](the-sign-epsilon-and-the-rigidity-constraint-on-sigma-10.html).
