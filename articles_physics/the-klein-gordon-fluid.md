# __The Klein–Gordon Fluid__

## Introduction

**The scalar field's fluid is the simplest fluid the algebra supplies: a positive density, a single action, and one sign.** It is [The Relativistic Quantum
Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html)'s word read on the centre. Two of the word's four factors have nothing to carry on a central field, so the boost is the identity and the rotor is a sign. What is left is a scale, an angle and a branch, and the one complex equation separates into two real equations without remainder.

**The claim of this article is that those two equations are the whole of a fluid: a continuity equation and an energy equation, with no third equation and no equation of state.** The energy equation is the mass shell with the amplitude's curvature added. Its gradient is the acceleration law, and the acceleration law carries a factor $1/\gamma$ that the non-relativistic limit removes. What the fluid does not have is a pressure: the quantum term is an energy, not a pressure, and no function $p(\rho)$ reproduces it.

**The article is a reading and not a derivation.** The word, the pair and the current are [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html). This article takes them and asks what the object is, in the vocabulary a fluid is described by: what its density is, what its velocity is, what its acceleration is, what its vorticity is, and what plays the role of a pressure.

**Four statements are new here, and each is one line of algebra.**

- The conserved density is the charge density $\rho_{\mathrm{chg}}$, not the marker density $\rho_{\mathrm{num}}$.
- The gradient of the amplitude equation is the acceleration law, and it reads $\mathrm{d}\vec p/\mathrm{d}t=-\gamma^{-1}\nabla Q_{\mathrm{qnt}}$.
- The four-velocity is a gradient, so the vorticity 2-form vanishes; the curl of the three-velocity need not, and it is not vorticity.
- The quantum term admits a stress and not a pressure, so there is no equation of state at a point.

## The Word Collapses

**The field is taken central**, $\tilde\Xi=\Xi_t e_t$, so the whole field is one complex coefficient. Nothing in the central d'Alembertian couples that coefficient to the other three, so the restriction loses no structure of the equation; it is a choice of subject, and the general field is treated in the parent article's §*General Fields*.

**On a central field two factors have no data.** The boost needs a rapidity and an axis, and a central element supplies neither, so $\tilde U_{\Psi,\mathrm b}=e_t$. The rotor needs an angle and an axis, and a central element supplies neither, so $\tilde u_{\mathrm r}=\varepsilon e_t$, a sign. The word collapses to

$$
\boxed{\;\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\varepsilon\,e_t\;}
\qquad
\rho_{\mathrm{num}}=r^{2},\quad
S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}},\quad
\varepsilon=\frac{\Xi_t}{\Rho}=\pm1 .
$$

**The sign is $\pm1$ here because the centre is on $\Sigma_{10}$.** A central element has $B^{2}=0$, and the parent article's identity $\varepsilon=\cosh(\theta_{\mathrm{rpd}}/2)\cos(\theta_{\mathrm{axr}}/2)$ reads $1\cdot(\pm1)$ here: the boost is trivial and the rotor's angle is $0$ or $2\pi$. On the general field $\varepsilon$ is not $\pm1$, and the scalar case is the case in which the branch is a sign.

**Three data remain at each event, and they are the fluid's.** The scale is the marker density. The angle is the action. The branch is the sign that a half turn of the phase deposits, and it is read off the element rather than chosen.

| datum | range | symbol | what it is |
| --- | --- | --- | --- |
| scale | $r>0$ | $\rho_{\mathrm{num}}=r^{2}$ | proper density of the markers |
| angle | $\theta_{\mathrm{pha}}\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ | $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ | action, defined modulo $2\pi\hbar$ |
| branch | $\varepsilon=\pm1$ | $\varepsilon$ | sign of the coefficient, deposited by the half turn |

**The count closes.** Three real data against the two real components of one complex coefficient, and the third is the half turn that the angle's range excludes. A reader who counts two has forgotten that the angle runs over a half-turn and that the other half is the sign.

**The action is a coordinate and not a property.** A shift of the angle by a full turn leaves the field and every observable unchanged. Every statement below is therefore a statement about $r$, $\varepsilon$ and the gradient of $S_{\tilde\Xi}$, and none about $S_{\tilde\Xi}$ itself.

## The Pair

**Substituting the word into the Klein–Gordon equation replaces one complex equation by two real ones, exactly.** With $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$ on the material sector,

$$
\left(\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)^{2}-\lvert\nabla S_{\tilde\Xi}\rvert^{2}=m^{2}c^{2}-\hbar^{2}\frac{\Box_\Phi r}{r}
\qquad\text{and}\qquad
\nabla\cdot\!\left(\rho_{\mathrm{num}}\nabla S_{\tilde\Xi}\right)-\frac{\partial}{\partial r'_t}\!\left(\rho_{\mathrm{num}}\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)=0 .
$$

The first is the amplitude equation and the second is the transport equation. The equivalence runs both ways: every solution of the pair gives a solution of the equation, and every nowhere-zero solution of the equation gives a solution of the pair.

### The amplitude equation is the mass shell with a curvature term

**Write the momentum as the algebra writes it**, $\tilde P_{\Phi}=\tilde\nabla_\Phi S_{\tilde\Xi}=i(E/c)e_t+\vec p$, with $E=-c\,\partial S_{\tilde\Xi}/\partial r'_t$ and $\vec p=\nabla S_{\tilde\Xi}$. Then the amplitude equation is

$$
\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2mQ_{\mathrm{qnt}},
\qquad
Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box_\Phi r}{r}.
$$

**The only thing the amplitude does is shift the mass shell, and it shifts it by a curvature.** $Q_{\mathrm{qnt}}$ is the d'Alembertian of the amplitude divided by the amplitude. It is not a function of the density's value: by the parent article's identity it is $\tfrac12\Box_\Phi\ln\rho_{\mathrm{num}}+\tfrac14(\partial\ln\rho_{\mathrm{num}})^{2}$, so two fields with the same density at an event and different density gradients have different $Q_{\mathrm{qnt}}$ there. That single fact decides the last section of this article.

**The companion's boxed dispersion relation is the constant-amplitude case.** A constant amplitude has $\Box_\Phi r=0$ — a plane wave is one instance and a wave with a uniform envelope is another — so $Q_{\mathrm{qnt}}=0$ and the shell is $\langle\tilde P_{\Phi}\rangle_{\natural}=-m^{2}c^{2}$. A general wave adds one term, and the term is the whole quantum content of the fluid.

### The transport equation is the continuity equation

**The transport equation is the divergence of the current.** With $\tilde J_{\Phi}=(\rho_{\mathrm{num}}/m)\tilde P_{\Phi}=\rho_{\mathrm{num}}\tilde V_{\Phi}$ and $\tilde V_{\Phi}=\tilde\nabla_\Phi S_{\tilde\Xi}/m$, the scalar part of the divergence is

$$
\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde J_{\Phi}\right)=\frac{1}{m}\left[\nabla\cdot\!\left(\rho_{\mathrm{num}}\nabla S_{\tilde\Xi}\right)-\frac{\partial}{\partial r'_t}\!\left(\rho_{\mathrm{num}}\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\right)\right],
$$

and the bracket is the transport equation. Conservation and the imaginary part of the equation are the same equation, not two that agree.

## The Density the Fluid Carries

**The current has a temporal component and a spatial part, and the two are different densities.** The temporal slot is the charge density, $\rho_{\mathrm{chg}}=\rho_{\mathrm{num}}E/(mc^{2})$, and the spatial part is $\rho_{\mathrm{num}}\vec p/m$. The four-current is

$$
\tilde J_{\Phi}=ic\rho_{\mathrm{chg}}\,e_t+\rho_{\mathrm{num}}\frac{\vec p}{m}
\qquad
\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}},\quad \gamma=\frac{E}{mc^{2}},\quad \vec v=\frac{\vec p}{m\gamma}.
$$

**The conserved density is the charge density and not the marker density.** Writing the transport equation in physical time, with $\partial_{r'_t}=c^{-1}\partial_t$, gives

$$
\partial_{t}\rho_{\mathrm{chg}}+\nabla\cdot\!\left(\rho_{\mathrm{chg}}\vec v\right)=0 .
$$

The algebra is one line: $\nabla\cdot(\rho_{\mathrm{num}}\vec p)=m\nabla\cdot(\rho_{\mathrm{chg}}\vec v)$ because $\vec p=\gamma m\vec v$ and $\rho_{\mathrm{num}}\gamma=\rho_{\mathrm{chg}}$, and $\partial_{r'_t}(\rho_{\mathrm{num}}\partial_{r'_t}S_{\tilde\Xi})=-mc\,\partial_{r'_t}\rho_{\mathrm{chg}}$.

**The marker density obeys a different equation, and the difference is the time dilation.** $\rho_{\mathrm{num}}$ is the density in the fluid's own frame; $\rho_{\mathrm{chg}}$ is the density in the frame in which the flow is measured. They differ by $\gamma$, and $\gamma$ is not constant along the flow. A reader who writes $\partial_t\rho_{\mathrm{num}}+\nabla\cdot(\rho_{\mathrm{num}}\vec v)=0$ has written the continuity equation of a different fluid; the correct statement carries $\rho_{\mathrm{chg}}$ on both occurrences.

**The scalar field has no boost factor, so $\gamma$ is signed.** $\gamma=E/(mc^{2})$ and on the negative sheet $E<0$, so $\gamma<0$ and the four-velocity is past-directed. This is not a pathology of the notation; it is the sign defect of the charge density that the parent article records, in the fluid's own terms.

## The Euler Equation

**A fluid's acceleration law is the gradient of its energy equation, and here that gradient is one line.** Differentiating the mass shell in space, with $\vec p=\nabla S_{\tilde\Xi}$ and $E=-\partial_t S_{\tilde\Xi}$ so that $\partial_jE=-\partial_tp_j$, and using $\partial_jp_k=\partial_kp_j$,

$$
\frac{E}{c^{2}}\partial_jE-p_k\partial_jp_k=m\partial_jQ_{\mathrm{qnt}}
\qquad\Longrightarrow\qquad
\left(\partial_t+\vec v\cdot\nabla\right)p_j=-\frac{1}{\gamma}\partial_jQ_{\mathrm{qnt}} .
$$

**The result is the acceleration law of the fluid**, written with the momentum and not the velocity,

$$
\boxed{\;\frac{\mathrm{d}\vec p}{\mathrm{d}t}=-\frac{1}{\gamma}\nabla Q_{\mathrm{qnt}}\;}
\qquad
\frac{\mathrm{d}}{\mathrm{d}t}=\partial_t+\vec v\cdot\nabla,\quad \vec p=m\gamma\vec v .
$$

**The factor $1/\gamma$ is the relativistic inertia, and it is the point of the display.** The force is the gradient of one scalar, so the flow is accelerated by a potential and by nothing else: no pressure gradient, no baroclinic term, no shear source. The inertia is $\gamma m$ rather than $m$, which is why the same gradient accelerates a fast flow less. At $\gamma\approx1$ the equation is the Bohm acceleration law of the non-relativistic fluid.

**The sign is the sign of a force down the potential.** $Q_{\mathrm{qnt}}$ enters the mass shell with a plus sign, so the fluid is pushed towards lower $Q_{\mathrm{qnt}}$. A localised packet has $Q_{\mathrm{qnt}}>0$ inside its core and $Q_{\mathrm{qnt}}\to0$ far out, so the force points outward and the packet spreads. That is the quantum spreading, in the fluid's language.

**This is the third equation, and it is not an independent one.** It is the gradient of the amplitude equation, so the pair plus this display is still the pair. The count is right: two real equations for two real unknowns, $r$ and $S_{\tilde\Xi}$, with the acceleration law a consequence. A fluid whose equations are continuity, energy and acceleration over-determines itself; here the three are two.

## The Vorticity

**The velocity is a gradient, so the vorticity is zero wherever the action is twice differentiable.** The vorticity is the 2-form of the four-velocity,

$$
\omega_{\mu\nu}=\partial_\mu v_{\Phi,\nu}-\partial_\nu v_{\Phi,\mu},
\qquad
v_{\Phi,\mu}=\frac{1}{m}\partial_\mu S_{\tilde\Xi},
$$

and it vanishes identically on the $N$-regular set, because partial derivatives commute.

**The circulation of the momentum is quantised only by a node.** For a closed loop that links no nodal line, $\oint\vec p\cdot\mathrm{d}\vec l=\oint\nabla S_{\tilde\Xi}\cdot\mathrm{d}\vec l=0$, because $S_{\tilde\Xi}$ is single-valued there. For a loop that links a nodal line the action is multivalued and the integral is $2\pi\hbar n$. Divided by $m$ the second is $hn/m$, and that is the circulation of $\vec p/m$, the quantity [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html) calls the circulation quantum. **It is the circulation of $\vec p/m$ and not of the three-velocity.** The physical three-velocity is $\vec v=\vec p/(m\gamma)$, so $\oint\vec v\cdot\mathrm{d}\vec l=hn/(m\gamma)$ only when $\gamma$ is constant along the loop, and on a loop across which $\gamma$ varies the integral is not quantised at all. The agreement of the two formulas is therefore an agreement about $\vec p/m$, and it is an agreement and not a derivation.

**The curl of the three-velocity is not the vorticity, and the difference is worth one paragraph.** Since $\vec v=\vec p/(m\gamma)$ and $\vec p$ is a gradient,

$$
\nabla\times\vec v=\nabla\!\left(\frac{1}{m\gamma}\right)\times\vec p ,
$$

which need not vanish. A flow that is accelerated from rest develops a non-zero curl of $\vec v$ even though $\omega_{\mu\nu}=0$. The reason is that $\vec v$ is not the spatial part of a four-vector; $\gamma\vec v$ is. The vorticity of a relativistic fluid is the 2-form of the four-velocity, and that one is zero. A reader who computes the curl of $\vec v$ and reports vorticity has computed a frame artefact.

**The consequence for the scalar case is strong and it is the sharpest difference from the spinor case.** The scalar fluid is irrotational in the covariant sense, always, off the nodes. The spinor fluid is not: its velocity is a unit element squared rather than a gradient, so its vorticity 2-form is the antisymmetrised gradient of the frame element. That is the technical content of the phrase *spin fluid*, and the comparison is drawn in [The Dirac Fluid and the Takabayasi Correspondence](the-dirac-fluid-and-the-takabayasi-correspondence.html).

## No Equation of State

**A fluid has an equation of state when its pressure is a function of its density at the same event.** The scalar fluid has no such function, and the reason is the curvature in $Q_{\mathrm{qnt}}$.

**The objection is that the quantum term looks like a pressure.** In the non-relativistic fluid the term $-\nabla Q$ is conventionally called the quantum pressure, and the name suggests a $p(\rho)$. The name is a misnomer twice over. First, $Q_{\mathrm{qnt}}$ depends on the density's first and second derivatives and not on its value, so a barotropic pressure would have to be a differential operator rather than a function: $Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}[\tfrac12\Box_\Phi\ln\rho_{\mathrm{num}}+\tfrac14(\partial\ln\rho_{\mathrm{num}})^{2}]$. Second, the force is the gradient of an energy and not the gradient of a pressure over a density: $-\gamma^{-1}\nabla Q_{\mathrm{qnt}}$ is not $-\rho^{-1}\nabla p$ for any function $p$ of the density's value.

**The class the fluid belongs to has a name, and naming it is the honest statement.** A fluid whose stress depends on the gradients of its density rather than on the density alone is a Korteweg fluid, and a Korteweg fluid has no equation of state in the algebraic sense and a perfectly definite stress. This fluid is of that class, and the parent article's identity is what shows it: its pressure is a function of $\rho_{\mathrm{num}}$ and of the first two derivatives of $\rho_{\mathrm{num}}$, and of nothing else.

**What does exist is a stress, and the stress is not a pressure.** The quantum force has the divergence form $\partial_\eta\sigma_{j\eta}$ with the tensor $\sigma$ exhibited in [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html), and that tensor is not isotropic: it is not $p\,\delta_{ij}$ for any scalar $p$. A divergence of an anisotropic stress is a force, not a pressure. So the fluid is one with a quantum stress and without an equation of state, and the two statements are consistent because a stress tensor carries more than a scalar pressure.

**The reader's check is the order of the derivatives.** A barotropic pressure makes the force density $-\nabla p(\rho_{\mathrm{num}})=-p'(\rho_{\mathrm{num}})\nabla\rho_{\mathrm{num}}$, a term along the density's gradient and first order in it. The force density here is $\rho_{\mathrm{num}}\gamma^{-1}\nabla Q_{\mathrm{qnt}}$, and $Q_{\mathrm{qnt}}$ already carries two derivatives of $\ln\rho_{\mathrm{num}}$, so the force is third order. No function of the density's value can turn two derivatives into none.

**This is where the scalar fluid differs from the thermal fluid.** A thermal fluid at a point has an equation of state, because its state is a density operator with a temperature and the pressure is a functional of that state. The scalar fluid of this block has no temperature and no state; it has a density and an action. The equation of state appears in *Biquaternion Relativistic Quantum Thermodynamics* and it is not anticipated here.

## The Criterion Applied

**The reverse map's criterion has four items, and the scalar fluid meets all four when the conditions are read on four-vectors, and three of them when the same conditions are read in a frame.** The criterion is derived in [The Direction of the Fluid-Wave Correspondence, Field by Field](the-direction-of-the-fluid-wave-correspondence-field-by-field.html): the velocity must be a gradient, the flow must be vorticity-free, every force must be a gradient, and the potential must be a function of the density plus the quantum term. The audit is short enough to tabulate.

**The criterion being met here in full is what makes this fluid the lowest member of the rank hierarchy and not the whole of it.** A gradient is the rank-zero case of a velocity one-form, and a rotational flow of rank two is still a potential flow, with a Clebsch pair in place of the single scalar. The scalar fluid has no pair to spend because its unknown carries a modulus and a phase and nothing else; a bispinor carries a frame, and the frame is where a pair can live. [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html) states the hierarchy and locates the Dirac fluid in it, so the four items below are the conditions of the lowest member and the Dirac block does not contradict them.

| Item of the criterion | The scalar fluid | Where it is shown |
| --- | --- | --- |
| the velocity is a gradient | yes, for $\tilde V_\Phi$; for $\vec v$ only up to $\gamma$ | §*The Vorticity* |
| the flow is irrotational | yes, identically off the nodes | §*The Vorticity* |
| every force is a gradient | yes, covariantly, with $\Phi_{\mathrm{acc}}=Q_{\mathrm{qnt}}/m$ | §*The Euler Equation* |
| the potential is a function of the density | yes, degenerately: $V=0$ | §*No Equation of State* |
| no viscous term | yes, and stronger: no first-order time derivative can exist | below |

**The force item is exact in the four-vector form, and the derivation is one line of the mass shell.** Every index is written low, as the conventions require: the temporal slot of $\tilde\nabla_\Phi$ carries the $-i$, so $\partial_\mu p_\nu=\partial_\nu p_\mu$ holds with no metric in sight and no index to raise. Differentiating $\sum_\nu p_\nu p_\nu=-m^{2}c^{2}-2mQ_{\mathrm{qnt}}$ with $p_\mu=\partial_\mu S_{\tilde\Xi}$,

$$
\sum_{\nu}p_{\nu}\,\partial_{\nu}p_{\mu}=-m\,\partial_{\mu}Q_{\mathrm{qnt}}
\qquad\Longrightarrow\qquad
\sum_{\nu}V_{\nu}\,\partial_{\nu}V_{\mu}=-\partial_{\mu}\frac{Q_{\mathrm{qnt}}}{m},
\qquad
\sum_{\nu}V_{\nu}V_{\nu}=-c^{2}-\frac{2Q_{\mathrm{qnt}}}{m} .
$$

**The normalisation is a unit only where the quantum potential vanishes, and the display says so.** The mass shell fixes the norm of $\tilde V_\Phi=\tilde P_\Phi/m$ at $-c^{2}-2Q_{\mathrm{qnt}}/m$, so the four-velocity is a unit on the free shell and on nothing else; the flow is bounded by $\lvert\vec v\rvert<c$ exactly while the shell stays timelike, that is while $Q_{\mathrm{qnt}}>-mc^{2}/2$. **That is the qualification the first-order rung removes**, and it is the reason the non-relativistic fluid's acceleration law carries no $\gamma$: with no norm there is no bound, and a velocity that nothing bounds has no Lorentz factor to carry.

**The four-acceleration is minus the gradient of one scalar per unit mass, with no remainder.** That is the criterion's third item verbatim, and the potential it names is $\Phi_{\mathrm{acc}}=Q_{\mathrm{qnt}}/m$: the quantum term alone, with $V=0$. The scalar fluid is therefore the pressureless member of the reverse map's family, and the family's nonlinear term is absent rather than small.

**The two frame failures carry $\gamma$ for one reason, and the reason is already in §The Vorticity.** $\vec v$ is not the spatial part of a four-vector, $\gamma\vec v$ is, so a criterion written in $\vec v$ is a criterion written in a frame, and a projection costs a factor of $\gamma$ at each step. The four-velocity is $\tilde V_\Phi=\gamma\vec v+i\gamma c\,e_t$, so $\sum_\nu V_\nu\partial_\nu=\gamma c\,\partial_{r'_t}+\gamma\vec v\cdot\nabla=\gamma\,\mathrm{D}$: the covariant derivative and the frame's differ by the single factor $\gamma$. Applying it to $p_j$ and then to $v_j=p_j/(m\gamma)$ gives

$$
\mathrm{D}p_j=-\frac{1}{\gamma}\partial_jQ_{\mathrm{qnt}},
\qquad
m\,\mathrm{D}v_j=-\frac{1}{\gamma^{2}}\partial_jQ_{\mathrm{qnt}}-m\,v_j\,\mathrm{D}\ln\gamma ,
\qquad
\mathrm{D}=\partial_t+\vec v\cdot\nabla .
$$

**The right side of the first line is a gradient multiplied by the scalar $\gamma^{-1}$, and a scalar multiple of a gradient is not a gradient.** So the third item survives the projection as a statement of *direction* and not of integrability: the force is longitudinal and has no transverse part, but it is not the gradient of a potential unless $\gamma$ is constant along the flow. The second line adds a further term, and that term is not a gradient either. Both failures are the same $\gamma$, and they are the same $\gamma$ that makes $\nabla\times\vec v$ non-zero while $\omega_{\mu\nu}$ vanishes.

**Where $\gamma$ is constant along the flow the frame form closes, and there the potential is $\Phi_{\mathrm{acc}}=Q_{\mathrm{qnt}}/(m\gamma^{2})$.** The non-relativistic limit is such a case, and so is any flow of uniform rapidity. The criterion is a statement about four-vectors; read in a frame it is exact only where the frame and the flow agree, and the agreement is $\mathrm{D}\gamma=0$.

**The fourth item is met degenerately, and the degeneracy is worth naming.** A barotropic fluid has $p_{\mathrm{th}}=p_{\mathrm{th}}(\rho_{\mathrm{mass}})$; here $p_{\mathrm{th}}=0$, and the constant function is a function of the density. The barotropic condition is satisfied vacuously rather than by a law of state, and the criterion is met as a statement about a *potential* and not as a statement about a *law*.

**The distinction matters because the pressure of the family and the potential of the criterion are not the same object.** $V(\rho_{\mathrm{num}})$ is a function of the density's value; $Q_{\mathrm{qnt}}$ is not, as §*No Equation of State* shows in three ways. So the scalar fluid closes the criterion with a potential that the criterion's own third clause does not anticipate: a function of the density's derivatives. The closure is local and it is not barotropic in the constitutive sense.

**The consequence is linearity, and the reason is the sharpest statement in this article.** With $V=0$ the reverse map has nothing left to add; the only potential in sight is $Q_{\mathrm{qnt}}$, and $Q_{\mathrm{qnt}}$ is not a term of the equation at all. It is $-\hbar^{2}/(2m)$ times $\Box_\Phi r$ over $r$, which is the kinetic operator acting on the amplitude and divided by it. In the variable $\psi$ that operator is linear and no potential appears; in the variables $(r,S_{\tilde\Xi})$ the same operator produces a term that looks like a potential and is not one. So the fluid's potential is the free equation's own curvature, and the test of whether a fluid is the reading of a *free* equation is whether a $V$ is added on top of it. Here none is, and with $k_m=mc/\hbar$ the equation is

$$
\left(\Box_\Phi-k_m^{2}\right)\psi=0 .
$$

**The substitution returns the pair exactly, in both parts and with no term dropped.** With $\psi=re^{iS_{\tilde\Xi}/\hbar}$,

$$
\hbar^{2}\frac{\Box_\Phi\psi}{\psi}
=\hbar^{2}\frac{\Box_\Phi r}{r}+\Bigl[\Bigl(\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\Bigr)^{2}-\lvert\nabla S_{\tilde\Xi}\rvert^{2}\Bigr]
+\frac{i\hbar}{r}\Bigl[2\nabla r\cdot\nabla S_{\tilde\Xi}-2\frac{\partial r}{\partial r'_t}\frac{\partial S_{\tilde\Xi}}{\partial r'_t}+r\,\Box_\Phi S_{\tilde\Xi}\Bigr] .
$$

**The real part is the amplitude equation term by term, and the imaginary part is the transport equation.** Set equal to $m^{2}c^{2}$ the first returns the mass shell with the curvature added; set equal to zero the second is $r^{-1}$ times $\nabla\cdot(\rho_{\mathrm{num}}\nabla S_{\tilde\Xi})-\partial_{r'_t}(\rho_{\mathrm{num}}\partial_{r'_t}S_{\tilde\Xi})$. So the two directions of the map meet here with no remainder: the pair is the linear equation read in fluid variables, and the linear equation is the pair written in one complex unknown.

**That exactness is what the block's other articles cannot have, and it is worth saying why.** For the Gross–Pitaevskii fluid the map runs the other way and the equation it produces is nonlinear; for a classical fluid the equation its $\psi$ obeys is nonlocal and is not a wave equation at all. The scalar fluid is the one case in the block where both directions close on a local linear equation, and the reason is that $V=0$ is the only member of the family in which nothing is added to the free operator.

**Linearity of the equation is not linearity of the fluid, and the gap is the interference term.** Superposition holds for $\psi$: $\psi_1+\psi_2$ solves. It fails for the fluid's data, because $\rho_{\mathrm{num}}=\lvert\psi\rvert^{2}$ and

$$
\rho_{\mathrm{num}}=\rho_1+\rho_2+2\sqrt{\rho_1\rho_2}\cos\!\Bigl(\frac{S_1-S_2}{\hbar}\Bigr) .
$$

**Two plane waves give a density modulated at the beat of the two actions, while the two densities taken separately are uniform.** A reader who calls the scalar fluid linear has confused the unknown of the equation with the data of the fluid; the data obey a nonlinear system even here.

**The viscosity item is met more strongly than the criterion asks, and the strength is a structural fact.** The criterion asks that no viscous force be present. Here no first-order time derivative can appear at all: $\Box_\Phi$ is second order and even in $\partial_{r'_t}$, and the coefficient is real, so the equation is invariant under $r'_t\to-r'_t$ and under complex conjugation. A viscous term is first order in time, odd under the reversal, and carries a fixed sign; the operator $\Box_\Phi-k_m^{2}$ admits none. The obstruction of [Viscosity and the Rayleigh Dissipation Function](viscosity-and-the-rayleigh-dissipation-function.html) therefore has nowhere to enter, and the dissipation function $F_{\mathrm{rlh}}$ has no counterpart in this fluid. The scalar fluid is not merely inviscid; it is barred from being viscous.

**What the audit fixes is the block's order.** The scalar fluid is the relativistic member of the direction article's pressureless row, and the Gross–Pitaevskii fluid is the non-relativistic member with $V\ne0$: one is linear with no law of state, the other nonlinear with one. The scalar case is the case in which the criterion closes exactly, and that is why it is the block's first fluid and the standard against which the spinor fluid is read.

## The Two Sheets

**The mass shell is two-sheeted, and both sheets carry the same fluid.**

| sheet | $E$ | $\rho_{\mathrm{chg}}$ | $\rho_{\mathrm{num}}$ | the four-velocity |
| --- | --- | --- | --- | --- |
| positive frequency | $>0$ | $>0$ | $>0$ | future-directed |
| negative frequency | $<0$ | $<0$ | $>0$ | past-directed |

**The amplitude is positive on both sheets and the energy is not.** The density of markers is $r^{2}$, which cannot be negative, so the sign has to come from somewhere else, and it comes from the temporal component of the four-velocity. The charge density changes sign because the flow reverses in time and not because the markers become negative.

**The two defects of the parent article are one mechanism, and this is it.** The parent records that the Klein–Gordon charge density is not positive definite and that it has the sign of the energy. In the fluid's terms there is one density, positive, and one direction of flow, which can point either way in time. The second-order equation does not organize its solutions by particle number, and the fluid's two sheets are the two signs of that direction.

**The transport equation cannot tell the sheets apart.** It is linear in $\partial S_{\tilde\Xi}/\partial r'_t$ and invariant under $S_{\tilde\Xi}\to-S_{\tilde\Xi}$, and both rows satisfy it with the same amplitude. The identification of particles needs a further structure, and that structure is the second quantization of *Biquaternion Quantum Fields*, not this block.

## The Limits

### The non-relativistic limit

**With the rest energy removed the pair becomes the Madelung system.** The action carries $mc^{2}t$, the amplitude equation becomes the quantum Hamilton–Jacobi equation with the WKB potential $Q_{\mathrm{qnt}}\to-\frac{\hbar^{2}}{2m}\frac{\nabla^{2}r}{r}$, and the transport equation becomes the continuity equation of the Schrödinger fluid. The factor $1/\gamma$ of the acceleration law goes to one. The parent article carries the derivation and this article does not repeat it.

**The limit is the check on the reading.** A fluid reading that did not reproduce the Madelung pair in the non-relativistic limit would be a different fluid. It does, term by term, and that is the warrant for calling the relativistic object a fluid at all.

**The limit has an article of its own, and it is not a footnote.** [The Schrödinger Fluid](the-schrodinger-fluid.html) reads the same pair as a fluid in its own right and states what the mass shell was supplying: the normalisation that bounds the velocity and puts $\gamma$ into the inertia, the sign that makes the density two-sheeted, and the dispersion constraint that the pair does not have. Read as a ladder, the first-order fluid is the bottom rung and this one is the rung above, and the table of the three quantities is the measure of the step.

### The cosmological reading

**The same pair is the fluid of a light scalar field in cosmology.** The variable $\rho_{\mathrm{num}}=r^{2}$ is the squared amplitude and not the energy density; in the non-relativistic regime of structure formation it plays the role of the mass density, and the field's energy density is $mc^{2}\rho_{\mathrm{num}}$ plus a kinetic term and the gradient term $\hbar^{2}\lvert\nabla r\rvert^{2}/(2m)$, the last being the one that is dropped above the de Broglie scale. The phase gradient is the bulk momentum, and $Q_{\mathrm{qnt}}$ is the term that suppresses structure below the de Broglie wavelength. That is the wave dark-matter reading, and it is the one place where the scalar fluid of this block is measured rather than written.

**The reading is not a claim of this corpus.** The corpus's field is a first-quantized element with one mass; a cosmological scalar is a classical field with a potential. What the two share is the pair of equations and the identification of the variables, and the sharing is worth one paragraph because it tells a reader where to look for the physics.

## The Properties, Listed

**Twelve statements, each one line, and each with its reason. This is what the scalar fluid is.**

1. **The word carries two parameters and a sign.** The scale, the action and the branch, and the count closes: three data against the two components of one complex coefficient plus the half turn the angle's range excludes.
2. **The density is a bilinear and the conserved density is not it.** $\rho_{\mathrm{num}}=r^{2}$ is the density in the fluid's frame; the conserved quantity is $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$, and $\gamma$ is signed on the negative sheet.
3. **Continuity is the imaginary part of the wave equation**, and the equivalence runs both ways: every solution gives a pair, every nowhere-zero solution of the pair gives a field.
4. **The velocity is a gradient**, $v_{\Phi,\mu}=\partial_\mu S_{\tilde\Xi}/m$, and it is a unit only where $Q_{\mathrm{qnt}}$ vanishes. **No other field fluid has a velocity that is a gradient.**
5. **There is one force and it is a gradient.** $\mathrm{d}\vec p/\mathrm{d}t=-\gamma^{-1}\nabla Q_{\mathrm{qnt}}$, and the factor $1/\gamma$ is the relativistic inertia: the same gradient accelerates a fast flow less.
6. **There is no equation of state, and the class has a name.** The stress is a Korteweg stress — a function of the density and its first two derivatives — and the force is third order in $\nabla\ln\rho_{\mathrm{num}}$, so no function of the density's value can produce it.
7. **A stress exists and is not a pressure.** The quantum stress is anisotropic, and a divergence of an anisotropic stress is a force and not $-\rho^{-1}\nabla p$.
8. **The flow is irrotational identically, off the nodes.** The vorticity 2-form of the four-velocity vanishes for every solution, and that is stronger than the statement that a particular flow is curl-free.
9. **The circulation is quantised by the nodes and not by the flow.** $\oint\vec p\cdot\mathrm{d}\vec l=2\pi\hbar n$ around a loop that links a nodal line, and $hn/m$ is the circulation of $\vec p/m$ and not of $\vec v$.
10. **The curl of the three-velocity need not vanish, and it is not vorticity.** $\nabla\times\vec v=\nabla(1/m\gamma)\times\vec p$: a frame artefact, since $\gamma\vec v$ and not $\vec v$ is the spatial part of a four-vector.
11. **The degenerate set is the nodal set**, $r=0$, of codimension two, and it is where the word, the fluid reading and the quantised circulation all begin.
12. **Its non-relativistic limit is the Madelung–Bohm fluid**, with $\gamma\to1$, and it is the only one of the three whose classical counterpart is a textbook quantum fluid rather than a textbook continuum medium.

## The Three Fluids

**The three fluid articles of the block can be put side by side, and the table is the shortest statement of what each field's fluid is.** The table is the same in all three articles; what changes from one to the next is which column is the article's own.

| | Klein–Gordon | Proca | Dirac |
| --- | --- | --- | --- |
| word | $r\,e^{i\theta_{\mathrm{pha}}}\varepsilon$ | $\varepsilon\,i\,r\,\tilde U_{\Psi,\mathrm b}$ | $r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r}$ |
| parameters | $2$ | $4$ | $8$ |
| real equations | $2$ | $4$ | $8$ |
| density | $\rho_{\mathrm{num}}=r^{2}$, a bilinear | $r=\sqrt{-A^{2}}$, the field's own norm | $\rho_{\mathrm{num}}$, a factor of the word |
| velocity | $\partial_\mu S/m$, a gradient | $A_\mu/r$, the field's direction | $ic\tilde U^{-2}$, the frame |
| continuity | the imaginary part of the wave equation | the Lorenz condition | the conservation of $\tilde J$, a separate statement |
| force | $-\gamma^{-1}\nabla Q_{\mathrm{qnt}}$, a gradient | $-\nabla\ln r-E_\mu/r$ | the divergence of the stress, antisymmetric part included |
| vorticity | zero identically | $r\,\omega=F-\mathrm{d}r\wedge u$ | the antisymmetrised frame gradient |
| spin in the word | none | none | the rotor |
| equation of state | none; a Korteweg stress | $p=\epsilon=\tfrac12m^{2}r^{2}$ | none; the spin's transport closes the system |
| reverse condition | barotropic, irrotational and inviscid | none; closure is $J^{\mu}=m^{2}A^{\mu}$ | the Frenkel condition, or a free constitutive law |
| classical medium | a Korteweg fluid | a London plasma | a Cosserat medium |
| degenerate set | $r=0$, codimension two | the lightlike set, codimension one | $r=0$, codimension two |

**This article's column is the first, and it is the only column whose fluid is a gradient flow.** That single fact explains four rows of the table at once: the vorticity is zero, the circulation is fixed by the winding of one function, the force is a gradient because it is the gradient of the energy equation, and the equation of state is absent because a Korteweg stress cannot be written as a function of the density's value. The price is that the fluid cannot rotate at all: rank-zero is the whole of what one function can carry, and a rotational flow needs a second function that the scalar word does not have.

## The Correspondence, Compared with the Other Two

**The correspondence has three steps, and all three fields walk them in the same order.** The word is exact; the reverse map is defined on a class; membership of that class is the extra structure that makes the fluid a classical medium rather than a relabelling of a wave.

$$
\text{field}\;\longrightarrow\;\text{fluid}\quad(\text{exact, total, no conditions}),
\qquad
\text{fluid}\;\longrightarrow\;\text{field}\quad(\text{total, but only solutions close}).
$$

**The forward arrow is exact in all three cases, and exact for the same reason.** Any nowhere-zero solution gives a density and an action by the polar substitution, and the substitution is a bijection on the $N$-regular set, so the fluid's data are the field's data and nothing is lost in the passage.

**The reverse arrow is where the cases part.** Give the fluid a positive density and an action whose gradient is its velocity, and the field is $r\,e^{iS_{\tilde\Xi}/\hbar}\varepsilon$. The class is the irrotational barotropic flows of the fluid layer's own articles, and the extra structure is the second-gradient stress — the Korteweg term — that the fluid must carry if a density's curvature is to produce a force. A first-order barotropic fluid cannot hold this field, and that is the content of [The Equation of State and the Barotropic Condition](the-equation-of-state-and-the-barotropic-condition.html)'s negative result.

**The third step names the medium, and there are exactly three kinds of extra structure.**

| field | the fluid it is | the extra structure | the classical object |
| --- | --- | --- | --- |
| Klein–Gordon | a barotropic irrotational flow | a stress that depends on the density's gradient | a Korteweg fluid |
| Proca | a flow with a density | a source carried by the flow itself | a London plasma |
| Dirac | a flow with an orientation | an internal degree of freedom | a Cosserat medium |

**The three structures are the three ways a classical medium can differ from a dust**: by remembering the gradient of its state, by carrying an internal field of its own, or by carrying an internal orientation. Each field picks exactly one, and none picks two. That is why the correspondence is systematic and not a pile of coincidences.

**The Madelung pair generalizes, and the count is what stays fixed.** One real equation per parameter in every case: two and two for the scalar, four and four for the Proca, eight and eight for the Dirac, whose four brackets are $1+1+3+3$. The shape of the pair changes in one direction only — scalar and scalar, then scalar and vector, then two more — and the doubling at each step is the doubling of the algebra's real dimension. **No case is a truncation of another.**

**What the correspondence supports and what it does not.** It supports the claim that each field equation is the equation of motion of a recognizable classical medium, and it supports the properties of §*The Properties, Listed* item by item. It does not support the claim that the scalar fluid's "quantum pressure" is a pressure, that its density can be read off its velocity, or that a rotational flow of the same fluid exists: the first is refuted in §*No Equation of State*, the second is refuted by $\gamma$, and the third is refuted by the gradient structure.

## What Is Established and What Is Interpretation

**Established.** The collapse of the word to three data. The pair, exactly, with no term dropped. The mass shell with $2mQ_{\mathrm{qnt}}$, and $Q_{\mathrm{qnt}}$ as the d'Alembertian of the amplitude over the amplitude. The current as $\rho_{\mathrm{num}}\tilde V_{\Phi}$, with the charge density as its temporal component. The continuity equation for $\rho_{\mathrm{chg}}$, derived in one line. The acceleration law, by the gradient of the mass shell, with the factor $\gamma^{-1}$. The vanishing of $\omega_{\mu\nu}$ off the nodes, and the quantisation of circulation at a node. The non-vanishing of $\nabla\times\vec v$ as a frame artefact. The absence of an algebraic equation of state, from $Q_{\mathrm{qnt}}$ carrying two derivatives of the density. That the four items of the reverse map's criterion are met, the force item exactly in the four-vector form, $\sum_\nu V_\nu\partial_\nu V_\mu=-\partial_\mu(Q_{\mathrm{qnt}}/m)$, every index low, and the velocity item up to the factor $\gamma$. That $(\Box_\Phi-k_m^{2})\psi=0$ returns the pair by substitution, the real part the amplitude equation and the imaginary part the transport equation, verified term by term. That the pressureless condition is what makes the output linear.

**The comparison is established as a table and not as a claim.** Every entry of §*The Three Fluids* is a statement already proved in one of the three articles, and the entries are what makes the identification systematic: the count of parameters and equations, the gradient structure of the velocity, the vanishing of the vorticity, the Korteweg class of the stress, the absence of an equation of state, and the codimension of the degenerate set. The correspondence of §*The Correspondence, Compared with the Other Two* rests on those entries.

**Interpretation.** That the pair *is* a fluid's equations rather than a rewriting with fluid words. The warrant is the count, the types of the factors and the non-relativistic limit; the identification of the variables with a fluid's is the programme's step. That the quantum term is best read as an energy rather than as a pressure is also a reading, and it is supported by the two failures of the pressure reading rather than proved by them.

**Not claimed.** It is not claimed that the fluid's linear equation makes its data linear: they obey the nonlinear system above, and the interference term is the measure. It is not claimed that the barotropic condition is met by a law of state; it is met by $p_{\mathrm{th}}=0$. It is not claimed that the fluid is a superfluid. The circulation of $\vec p/m$ agrees with a superfluid's and the object is one element, not a condensate. It is not claimed that the quantum stress is a pressure; the companion article says the opposite and this one agrees. It is not claimed that the fluid has a thermodynamics; it has no temperature and no state.

## Summary

The scalar field's word collapses to a scale, an angle and a branch, so the fluid carries three data at each event: the marker density $\rho_{\mathrm{num}}=r^{2}$, the action $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$, and the sign $\varepsilon$.

The one complex equation separates into two real equations without remainder. The amplitude equation is the mass shell with the amplitude's curvature added, $E^{2}/c^{2}-p^{2}=m^{2}c^{2}+2mQ_{\mathrm{qnt}}$ with $Q_{\mathrm{qnt}}=-\hbar^{2}\Box_\Phi r/(2mr)$. The transport equation is the conservation of the current $\tilde J_{\Phi}=\rho_{\mathrm{num}}\tilde V_{\Phi}$.

The conserved density is the charge density $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$, not the marker density, and the continuity equation is $\partial_t\rho_{\mathrm{chg}}+\nabla\cdot(\rho_{\mathrm{chg}}\vec v)=0$.

The gradient of the mass shell is the acceleration law, $\mathrm{d}\vec p/\mathrm{d}t=-\gamma^{-1}\nabla Q_{\mathrm{qnt}}$, with $\vec p=m\gamma\vec v$. The force is a gradient and nothing else, and the inertia is $\gamma m$.

The four-velocity is a gradient, so the vorticity 2-form vanishes off the nodes. The curl of the three-velocity need not vanish, and it is a frame artefact. The circulation of the momentum is zero around a loop that links no node, and $2\pi\hbar n$ around one that does.

There is no equation of state in the algebraic sense. $Q_{\mathrm{qnt}}$ carries two derivatives of $\ln\rho_{\mathrm{num}}$, so no function of the density's value reproduces the force. What exists is an anisotropic quantum stress, whose divergence is the force, and a stress is not a pressure.

The mass shell is two-sheeted, and both sheets carry a positive marker density. The sign of the charge density is the sign of the energy, which is the direction of the flow in time.

The fluid meets the reverse map's criterion. Its four-velocity is a gradient, so it is irrotational; its four-acceleration is minus the gradient of one scalar, $\sum_\nu V_\nu\partial_\nu V_\mu=-\partial_\mu(Q_{\mathrm{qnt}}/m)$; its potential is $V=0$, a function of the density degenerately; and it carries no first-order time derivative, so it is not merely inviscid but barred from being viscous. The frame form of the criterion acquires factors of $\gamma$, and they are the same $\gamma$ that makes $\nabla\times\vec v$ non-zero.

Compared with the block's other two fluids, this one is the only gradient flow. Its density is a bilinear and not the field, its vorticity is zero rather than read off a frame or from a field strength, and its force is one gradient where the Proca fluid has two forces and the Dirac fluid has a stress. What it shares with them is the skeleton of the correspondence: an exact word, a reverse map onto a class, and a piece of extra structure — here a Korteweg stress — that makes the fluid a classical medium. The three fields pick the three ways a medium can exceed a dust, and the scalar case picks the gradient of the state.

With $V=0$ the reverse map's output is linear, and it is $(\Box_\Phi-k_m^{2})\psi=0$. The substitution $\psi=re^{iS_{\tilde\Xi}/\hbar}$ returns the pair exactly: the real part is the amplitude equation and the imaginary part is the transport equation. So the scalar fluid is the one case in the block where both directions close on a local linear equation, and the linearity is of the equation and not of the data, since $\rho_{\mathrm{num}}$ carries the interference term $2\sqrt{\rho_1\rho_2}\cos((S_1-S_2)/\hbar)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$ | The central field, in its word |
| $r$ | Amplitude; $r>0$ |
| $\rho_{\mathrm{num}}=r^{2}$ | Proper density of the markers |
| $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ | Action of the scalar field |
| $\varepsilon=\Xi_t/\Rho=\pm1$ | Branch of the modulus; $\pm1$ because the centre lies on $\Sigma_{10}$; $\Rho=r e^{i\theta_{\mathrm{pha}}}$ |
| $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial{r'_{t}}^{2}$ | Central d'Alembertian on the material sector |
| $r'_t=ct$ | Material time coordinate, a length |
| $\tilde P_{\Phi}=\tilde\nabla_\Phi S_{\tilde\Xi}=i(E/c)e_t+\vec p$ | Four-momentum |
| $\tilde V_{\Phi}=\tilde P_{\Phi}/m$ | Four-velocity, with $v_{\Phi,\mu}$ its components |
| $\vec p=\nabla S_{\tilde\Xi}$ | Three-momentum; also $\gamma m\vec v$ |
| $\vec v=\vec p/(m\gamma)$ | Three-velocity |
| $\gamma=E/(mc^{2})$ | Signed Lorentz factor, $\cosh\theta$ on the future sheet |
| $\tilde J_{\Phi}=\rho_{\mathrm{num}}\tilde V_{\Phi}$ | The current |
| $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ | Charge density, the temporal component of $\tilde J_{\Phi}$ |
| $Q_{\mathrm{qnt}}=-\hbar^{2}\Box_\Phi r/(2mr)$ | Quantum potential |
| $\omega_{\mu\nu}=\partial_\mu v_{\Phi,\nu}-\partial_\nu v_{\Phi,\mu}$ | Vorticity 2-form |
| $k_m=mc/\hbar$ | Mass wave number |
| $\Phi_{\mathrm{acc}}=Q_{\mathrm{qnt}}/m$ | Acceleration potential of the criterion |
| $\langle\tilde Q\rangle_{\natural}$ | Quaternionic norm |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |
| $c$ | Speed of light in the medium |

## Further Reading

- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter, Part I. General theory," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the spin-$0$ system that the pair is.
- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1926) 322–326, for the non-relativistic limit.
- David Bohm, "A suggested interpretation of the quantum theory in terms of hidden variables," *Physical Review* **85** (1952) 166–193, for the guidance equation and the quantum potential, with the caveat that this block takes the algebra and not the ontology.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), §9, for the relativistic spin-$0$ fluid and its acceleration law.
- Diederik J. Korteweg, "Sur la forme que prennent les équations du mouvement des fluides si l'on tient compte des forces capillaires causées par des variations de densité considérables mais continues," *Archives Néerlandaises des Sciences Exactes et Naturelles* **6** (1901) 1–24, for the class of fluids whose stress depends on the gradients of the density.
- Lam Hui, Jeremiah P. Ostriker, Scott Tremaine and Edward Witten, "Ultralight scalars as cosmological dark matter," *Physical Review D* **95** (2017) 043541, for the cosmological reading of the same pair.
- The companion articles: [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html), [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html), [The Direction of the Fluid-Wave Correspondence, Field by Field](the-direction-of-the-fluid-wave-correspondence-field-by-field.html), [The Dirac Fluid and the Takabayasi Correspondence](the-dirac-fluid-and-the-takabayasi-correspondence.html), [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html), [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html), and the charged companion [The Charged Klein–Gordon Fluid](the-charged-klein-gordon-fluid.html), which reads the same fluid with a central connection.
