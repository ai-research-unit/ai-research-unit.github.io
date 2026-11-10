# __Spin Hydrodynamics in Biquaternionic Form__

## Introduction

**A fluid whose elements carry spin has a second conserved quantity, and its hydrodynamics is the hydrodynamics of a fluid with two currents: the energy-momentum element and the spin element.** The new thermodynamic variable is the spin polarization, whose conjugate intensive quantity is the spin potential $\mu_{\mathrm{spn}}$:

$$
\mu_{\mathrm{spn}}=\mu_{\mathrm{spn}}\left(T,\ \mu_{\mathrm{chm}},\ \omega_{\lambda\nu}\right),
$$

**and the article's subject is what the fluid does when that variable is not in equilibrium** — when the polarization is not the one the local temperature and vorticity would give it.

**The spin polarization is an antisymmetric object with six independent components, and the corpus writes it as an element whose components are $\omega_{\lambda\nu}$.** Three of the six are spatial rotations and three are boosts; the rotation part is the one a fluid element's spin couples to, and the boost part is the one a spin current transports. **The article keeps every index low and labels the direction**, following the frame and metric conventions: $\omega_{\lambda\nu}$ is an antisymmetric array of numbers, not a tensor slot.

**The article's central caution is stated at the outset and derived later: the naive local relation is incomplete.**

$$
\frac{\partial p_{\mathrm{th}}}{\partial \omega_{\lambda\nu}}\neq \tilde S_{\Psi,\eta}\ \text{in general},
$$

**so the differential relations cannot close the equations.** The equality holds only in global thermal equilibrium, where the polarization is the one the temperature fixes; off equilibrium the pressure is not a function of the polarization alone, and a closure that assumes it is has assumed away the physics. **That is the article's most useful content and its warning against the most common shortcut in the spin-hydrodynamics literature.**

**What the article builds on.** The fluid's stress is [The Local Thermal State of a Fluid](the-local-thermal-state-of-a-fluid.html)'s, the entropy current and its Hermiticity declaration are [The Local Entropy Current](the-local-entropy-current.html)'s, the spin element is the rotor's, which is [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html)'s, and the conservation law the spin obeys is [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html)'s. **The article adds the polarization as a thermodynamic variable, its diffusion and its relaxation, and the closure caution.**

## The Spin Polarization and the Spin Potential

### The polarization element

**The spin polarization is the rotor's generator, read as a thermodynamic variable.** With the rotor $\tilde u_{\mathrm r}$ of the polar form and its generator $\tilde\omega_\Psi=\tfrac12\omega_{\lambda\nu}\tilde e_{\lambda\nu}$ — the antisymmetric part of the algebra's basis, with $\lambda<\nu$ — the polarization element is proportional to the generator:

$$
\tilde S_{\Psi,\eta}=\frac{\hbar}{2}\,\tilde u_{\mathrm r}\,\tilde e_{\lambda\nu}\,\tilde u_{\mathrm r}^{\natural}\,\omega_{\lambda\nu},
$$

**the rotor conjugating the generator into the fluid's frame and the factor $\hbar/2$ making the components angular momenta.** The display is the polar-form article's rotor read as a density: **the spin element is what the rotor looks like when it is summed over a volume.**

**The components, low.** Writing the six independent components $\omega_{\lambda\nu}=-\omega_{\nu\lambda}$ and the corresponding components $S_{\Psi,\eta,\lambda\nu}$ of the spin element, the article never raises an index; the pair $(\lambda,\nu)$ labels which rotation, and the array is antisymmetric in it. **The spin tensor's components are the angular momentum density in the $\lambda\nu$ plane**, and the flux of that component in the $\eta$ direction is written with $\eta$ last.

**The zero-divisor caution.** The rotor is an element of norm one, and the spin element it builds is regular as long as the rotor is; on the zero-divisor cone the quaternionic norm of the spin element vanishes and the polarization has no inverse. **The corpus states the restriction because the algebra's degenerate elements are where its structure changes**, and a hydrodynamic expansion around a degenerate polarization is not the same expansion.

### The two chemical potentials

**A spin fluid has two intensive variables conjugate to two conserved densities, and the local thermal state is a function of both.**

$$
d w_{\mathrm{fl}}=T\,d s_{\mathrm{ent}}+\mu_{\mathrm{chm}}\,d\rho_{\mathrm{num}}+\frac{1}{2}\omega_{\lambda\nu}\,dS_{\Psi,\eta,\lambda\nu},
$$

with $\mu_{\mathrm{chm}}$ the chemical potential and $\omega_{\lambda\nu}$ the angular velocity conjugate to the spin density. **The display is the first law for a spin fluid, and its third term is the one a spinless fluid does not have**; the factor of one half counts the antisymmetric pairs once.

**The spin potential is the intensive variable of the polarization, and it is not the angular velocity.** The spin potential $\mu_{\mathrm{spn}}$ is the Legendre transform's variable,

$$
\mu_{\mathrm{spn}}=\left(\frac{\partial w_{\mathrm{fl}}}{\partial \rho_{\mathrm{num,spn}}}\right)_{s_{\mathrm{ent}},\rho_{\mathrm{num}}},
$$

where $\rho_{\mathrm{num,spn}}$ is the number density of polarized elements; **it measures how much energy one more polarized element costs**, whereas $\omega_{\lambda\nu}$ measures how fast the frame turns. **The two are equal in equilibrium and different off it**, which is the distinction that the closure caution later turns on.

**The local thermal state with spin, written in the corpus's letters.** The state is specified by the pointwise temperature, the chemical potential and the spin potential, and the equation of state is [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html)'s with the third variable added:

$$
p_{\mathrm{eff}}=p_{\mathrm{th}}\left(\rho_{\mathrm{num}},\beta,\mu_{\mathrm{spn}}\right)+p_{\mathrm{qnt}}\left(\rho_{\mathrm{num}}\right),
$$

**the quantum part unchanged because it depends on the density alone** and the thermal part gaining a dependence on the spin potential through the polarization's contribution to the energy.

## Rotational Flow and Spin Gradients

### The vorticity of the flow and the polarization

**The flow's vorticity and the polarization are two different objects, and confusing them is the second commonest error in the subject.** The vorticity is

$$
\omega^{\mathrm{vrt}}_{\mu\nu}=\partial_\mu v_{\Phi,\nu}-\partial_\nu v_{\Phi,\mu},
$$

the antisymmetric part of the flow's gradient, **built from the flow element's components**; the polarization $\omega_{\lambda\nu}$ is a thermodynamic variable describing how the elements are spinning about their own centres. **A fluid can rotate without polarized elements and be polarized without rotating**, and the two names are distinguished in this article's notation by the label $\mathrm{vrt}$ on the vorticity.

**Local equilibrium ties the two together, and the tie is the source of the spin-rotation coupling.** In equilibrium a fluid element in a rotating flow is polarized in proportion to the rotation, with the standard result quoted:

$$
\mu_{\mathrm{spn}}^{\mathrm{eq}}=\frac{\hbar\,\omega^{\mathrm{vrt}}_{\mathrm{mag}}}{2},
\qquad
P_{\mathrm{pol}}=\tanh\left(\frac{\mu_{\mathrm{spn}}^{\mathrm{eq}}}{k_B T}\right),
$$

with $\omega^{\mathrm{vrt}}_{\mathrm{mag}}$ the magnitude of the rotation vector and $P_{\mathrm{pol}}$ the polarization of one element. **At $\hbar\omega^{\mathrm{vrt}}_{\mathrm{mag}}=0.019\,75\,\mathrm{GeV}$ and $k_BT=0.15\,\mathrm{GeV}$ the polarization is $0.065\,730$**, so a rotation fast by hadronic standards polarizes the fluid only weakly; at $\hbar\omega^{\mathrm{vrt}}_{\mathrm{mag}}=0.065\,82\,\mathrm{GeV}$ the polarization is $0.215\,950$. **The relation is the equilibrium one and is used only to identify the equilibrium polarization**; off equilibrium the two differ by the polarization's own relaxation.

**The coupling's energy, which is the interaction between the two.** With the polarization and the vorticity both present, the energy density gains

$$
e_{\mathrm{rot}}=-\,\frac{1}{2}\,\omega^{\mathrm{vrt}}_{\lambda\nu}\,S_{\Psi,\eta,\lambda\nu},
$$

the standard spin-rotation coupling: **a polarized element aligned with the rotation sits lower in energy, and a misaligned one sits higher.** The display is the third term of the first law with the angular velocity replaced by the flow's vorticity, and the replacement is valid only in local equilibrium — **which is the same restriction as before, and the article keeps track of it.**

### Spin gradients and the stress

**A gradient in the polarization is a gradient in the spin density, and it contributes to the stress the way any gradient of an intensive variable does.** The stress element gains a term

$$
\tilde\Sigma_{\Psi,\mathrm{spn}}=-\left(\partial_\lambda \mu_{\mathrm{spn}}\right)\tilde S_{\Psi,\eta}\ \text{in the first-order form},
$$

**whose divergence is the force that a polarization gradient exerts on the flow.** The display is schematic in its indices — the spin element is antisymmetric and contracts with the gradient in the $\lambda$ slot — and **the article states the structure and does not write the index algebra in full**, because the full algebra is bookkeeping without physics.

**The structure is worth having, because it is what couples the flow to the spin.** A fluid with a polarization gradient is a fluid whose momentum balance feels the spin, so the flow and the spin cannot be solved separately; **the two are one system, and that is the sense in which spin hydrodynamics is not ordinary hydrodynamics with an extra field.**

**The entropy production of the spin channel, written with the inherited Hermiticity.** The spin contributes a term to the production of [The Local Entropy Current](the-local-entropy-current.html),

$$
\sigma_{\mathrm{ent,spn}}=\frac{1}{T}\,\kappa_{\mathrm{spn}}\left(\partial_\lambda \mu_{\mathrm{spn}}\right)\left(\partial_\lambda \mu_{\mathrm{spn}}\right)\ \ge 0,
$$

with $\kappa_{\mathrm{spn}}$ the spin diffusion coefficient. **The current remains Hermitian and the inequality remains real**, so the declaration made in the entropy article covers this term without a fresh $\mathrm{Re}$; the term is a square, and its sign is the non-negativity of $\kappa_{\mathrm{spn}}$.

## Spin Diffusion and Spin Relaxation

### Diffusion

**A polarization gradient drives a spin current, and the current's law is Fick's law in the corpus's letters.**

$$
J_{\Psi,\mathrm{spn},\lambda}=-\,\kappa_{\mathrm{spn}}\,\partial_\lambda\mu_{\mathrm{spn}},
$$

with $\kappa_{\mathrm{spn}}$ the same coefficient as in the production. **The two appearances are one fact**: a current proportional to a gradient produces entropy proportional to the gradient squared, and the coefficient's sign is fixed by the second law's inequality.

**Combining the current with the conservation law gives the diffusion equation.** With the spin density's conservation off equilibrium — its source is the relaxation, next subsection —

$$
\partial_t S_{\Psi,\eta,\lambda\nu}=\partial_\lambda\left(\kappa_{\mathrm{spn}}\,\partial_\lambda \mu_{\mathrm{spn}}\right)+\text{relaxation},
$$

**the standard diffusion equation with a source.** Its diffusion length over a time $\tau$ is $\ell_{\mathrm{spn}}=\sqrt{\kappa_{\mathrm{spn}}\tau}$, **which is the length over which a polarization disturbance is felt** and the number that decides whether a given fluid element is polarized by its neighbours.

### Relaxation

**The polarization relaxes to its local equilibrium value on a time scale $\tau_{\mathrm{spn}}$, and the relaxation is the spin channel's answer to the shear's viscosity.**

$$
\frac{d}{dt}\left(S_{\Psi,\eta,\lambda\nu}-S_{\Psi,\eta,\lambda\nu}^{\mathrm{eq}}\right)=-\,\frac{1}{\tau_{\mathrm{spn}}}\left(S_{\Psi,\eta,\lambda\nu}-S_{\Psi,\eta,\lambda\nu}^{\mathrm{eq}}\right),
$$

**the relaxation-time approximation, which is the standard closure and is quoted as such.** Its solution is exponential, and its content is one number: how long a polarized element remembers its polarization.

**A number, for scale.** With $\tau_{\mathrm{spn}}=0.5\,\mathrm{fm}/c=1.667\,820\,476\times10^{-24}\,\mathrm{s}$, the surviving fraction after $0.5\,\mathrm{fm}/c$ is $e^{-1}=0.367\,879$, after $1\,\mathrm{fm}/c$ it is $0.135\,335$, after $2\,\mathrm{fm}/c$ it is $0.018\,316$, and after $5\,\mathrm{fm}/c$ it is $4.540\times10^{-5}$. **The polarization is gone after a few relaxation times**, which is why spin hydrodynamics is a description of the early stage of a collision and not of its late stage.

**The relaxation is dissipative and its production is positive.** The relaxation term contributes to $\sigma_{\mathrm{ent}}$ a piece proportional to the departure squared over $\tau_{\mathrm{spn}}T$, **so the decay of the polarization heats the fluid**, exactly as the decay of a shear does. **The two channels — spin relaxation and shear — are separate squares of the same second law**, and the article counts them separately.

**Why relaxation is not optional.** A first-order theory with a diffusive spin current and no relaxation is parabolic and therefore acausal, exactly as the first-order heat conduction is; **the relaxation time is what makes the spin channel hyperbolic**, and [Causal Dissipative Hydrodynamics in Biquaternionic Form](causal-dissipative-hydrodynamics-in-biquaternionic-form.html) is where that structure is written for the fluid as a whole.

## The Caution: Why the Differential Relations Do Not Close

### The identity and its domain

**The relation $\partial p_{\mathrm{th}}/\partial\omega_{\lambda\nu}=S_{\Psi,\eta,\lambda\nu}$ is a thermodynamic identity of the equilibrium state, and it is not an identity of the hydrodynamic equations.** In equilibrium the pressure is a function of the complete set of state variables, the polarization among them, and the derivative is a genuine partial derivative of a function. **Off equilibrium the pressure is not a function of those variables at all** — it is a functional of the state's history through the relaxation — so the derivative on the left is not defined as a partial derivative, and the equality has no content.

**Written with the corpus's letters, the caution is**

$$
\frac{\partial p_{\mathrm{th}}}{\partial \omega_{\lambda\nu}}\neq \tilde S_{\Psi,\eta}
\qquad\text{when }\omega_{\lambda\nu}\neq\omega_{\lambda\nu}^{\mathrm{eq}},
$$

**and the inequality is the statement that the two sides are different objects rather than two values of one.** The left side is the derivative of the equation of state along the equilibrium surface; the right side is the actual spin density, which relaxes towards that surface at its own rate. **They agree only on the surface.**

### Why the closure fails

**The differential relations are a system with more unknowns than equations, and the missing equations are the relaxation equations and not the equilibrium identity.**

| Quantity | Count |
|---|---|
| Components of the flow element | $4$ |
| Temperature and chemical potential | $2$ |
| Components of the spin density | $6$ |
| The pressure and the energy density | $2$ |
| **Unknowns** | **$14$** |
| Conservation of the energy-momentum element | $4$ |
| Conservation of the spin element | $6$ |
| The equation of state, one relation | $1$ |
| The second law, one inequality | $0$ (it constrains, it does not determine) |
| **Equations** | **$11$** |

**The count is the article's argument in one table: eleven equations for fourteen unknowns, so three relations are missing.** The three are the constitutive relations for the dissipative fluxes — the bulk and shear stresses and the heat flux, or in the spin sector the spin current and its relaxation — and **they cannot be supplied by the equilibrium identity, because the identity would replace six unknowns by the derivative of one function and would leave the relaxation time undetermined.**

**What happens if the identity is used anyway, which is what the shortcut does.** Substituting $S_{\Psi,\eta,\lambda\nu}=\partial p_{\mathrm{th}}/\partial\omega_{\lambda\nu}$ closes the system at eleven equations and eleven unknowns, and the resulting theory is the one in which the polarization is slaved to the flow instantaneously. **It is parabolic, it is acausal, and it has the wrong sign for the spin's contribution to the shear stress in the regime where the spin is not equilibrated** — three defects, each of which is fatal to a description of a system that is not in equilibrium by construction.

**The identity's correct use, which the article keeps.** It is a *diagnostic*: on the equilibrium surface it relates the equation of state to the spin density, so a measurement of one checks the other; and it is the *target* of the relaxation equation, which drives the spin density towards the value the identity gives. **Using it as a definition is the error; using it as the relaxation's fixed point is the method.**

### What the spin sector needs instead

**Three equations, and the article names them without solving them.** The spin current's constitutive relation with its diffusion coefficient, the relaxation equation for the polarization with its time scale, and the coupling between the spin current and the flow's vorticity. **The first two are written above; the third is the spin-rotation coupling of the earlier section, which enters the energy balance.**

**The count after the three are supplied: fourteen equations for fourteen unknowns, with the three transport coefficients $\kappa_{\mathrm{spn}}$, $\tau_{\mathrm{spn}}$ and the spin-rotation coupling as parameters.** The system is then closed and hyperbolic, and the second law's inequality constrains the three coefficients' signs. **That is the standard Israel–Stewart counting applied to the spin sector**, and the article's contribution is to say so in the corpus's letters rather than to re-derive the counting.

## What Is Established and What Is Interpretation

**Established, and standard.** That a spin fluid's thermodynamics has two intensive variables, the temperature and the spin potential, and that its first law carries the term $\tfrac12\omega_{\lambda\nu}dS_{\Psi,\eta,\lambda\nu}$; that the polarization diffuses with a coefficient whose sign the second law fixes; that it relaxes to its local equilibrium value on a time scale $\tau_{\mathrm{spn}}$; that the relaxation is dissipative and produces entropy; that the equilibrium identity between the pressure's derivative and the spin density holds on the equilibrium surface and does not close the equations off it.

**The framework's contribution.** The spin element is the rotor's generator conjugated into the fluid's frame, so the polarization is a property of the rotor and not an independent field; the spin's contribution to the stress and to the entropy current is written on elements, with every index low; and the entropy inequality that constrains the spin channel inherits [The Local Entropy Current](the-local-entropy-current.html)'s Hermiticity declaration, so no fresh $\mathrm{Re}$ is written.

**Interpretation, and marked as such.** That the spin element is $\tfrac{\hbar}{2}$ times the conjugated generator with the components read as angular momenta is the corpus's normalisation and not a derivation. That the relaxation is exponential is the relaxation-time approximation and is quoted, not derived.

**Not claimed.** That the transport coefficients have been computed — they have not. That the full index algebra of the spin stress has been written — it has not, and the article says so where the display is schematic. That the spin conservation law has been derived from the rotor's equation of motion — that is [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html)'s subject, and this article cites it. That the theory is causal — that is [Causal Dissipative Hydrodynamics in Biquaternionic Form](causal-dissipative-hydrodynamics-in-biquaternionic-form.html)'s, and the spin channel's hyperbolicity is asserted here on the strength of its relaxation equation rather than proved.

## Summary

A spin fluid has two intensive variables. The spin potential $\mu_{\mathrm{spn}}$ is conjugate to the spin polarization, whose element is the rotor's generator conjugated into the fluid's frame, $\tilde S_{\Psi,\eta}=\tfrac{\hbar}{2}\tilde u_{\mathrm r}\tilde e_{\lambda\nu}\tilde u_{\mathrm r}^{\natural}\omega_{\lambda\nu}$, with the six components $\omega_{\lambda\nu}$ antisymmetric and every index low. The first law gains one term, $dw_{\mathrm{fl}}=Tds_{\mathrm{ent}}+\mu_{\mathrm{chm}}d\rho_{\mathrm{num}}+\tfrac12\omega_{\lambda\nu}dS_{\Psi,\eta,\lambda\nu}$, and the equation of state gains one argument.

Rotational flow and spin gradients couple. The vorticity $\omega^{\mathrm{vrt}}_{\mu\nu}=\partial_\mu v_{\Phi,\nu}-\partial_\nu v_{\Phi,\mu}$ is not the polarization, and in equilibrium $\mu_{\mathrm{spn}}^{\mathrm{eq}}=\hbar\omega^{\mathrm{vrt}}_{\mathrm{mag}}/2$ with $P_{\mathrm{pol}}=\tanh(\mu_{\mathrm{spn}}^{\mathrm{eq}}/k_BT)$, which is $0.065\,730$ at $\hbar\omega^{\mathrm{vrt}}_{\mathrm{mag}}=0.019\,75\,\mathrm{GeV}$ and $0.215\,950$ at $0.065\,82\,\mathrm{GeV}$ for $k_BT=0.15\,\mathrm{GeV}$. The spin-rotation energy is $e_{\mathrm{rot}}=-\tfrac12\omega^{\mathrm{vrt}}_{\lambda\nu}S_{\Psi,\eta,\lambda\nu}$ and the spin gradient contributes to the stress.

Spin diffusion is $J_{\Psi,\mathrm{spn},\lambda}=-\kappa_{\mathrm{spn}}\partial_\lambda\mu_{\mathrm{spn}}$, with the production $\sigma_{\mathrm{ent,spn}}=T^{-1}\kappa_{\mathrm{spn}}(\partial_\lambda\mu_{\mathrm{spn}})(\partial_\lambda\mu_{\mathrm{spn}})\ge0$, real by the inherited declaration. Spin relaxation drives the polarization to its equilibrium value on the time scale $\tau_{\mathrm{spn}}$; with $\tau_{\mathrm{spn}}=0.5\,\mathrm{fm}/c$ the surviving fraction is $0.367\,879$ after $0.5\,\mathrm{fm}/c$ and $4.540\times10^{-5}$ after $5\,\mathrm{fm}/c$.

The caution is the article's centre: $\partial p_{\mathrm{th}}/\partial\omega_{\lambda\nu}\neq\tilde S_{\Psi,\eta}$ off the equilibrium surface, so the differential relations do not close — eleven equations for fourteen unknowns — and the three missing relations are the constitutive ones, not the equilibrium identity. **Using the identity as a closure gives a parabolic, acausal theory with the wrong sign; using it as the relaxation's fixed point is the method.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mu_{\mathrm{spn}}$ | Spin potential |
| $\mu_{\mathrm{spn}}^{\mathrm{eq}}$ | Its equilibrium value |
| $\mu_{\mathrm{chm}}$ | Chemical potential |
| $\omega_{\lambda\nu}=-\omega_{\nu\lambda}$ | Spin polarization components |
| $\omega^{\mathrm{vrt}}_{\mu\nu}$ | Vorticity of the flow |
| $\omega^{\mathrm{vrt}}_{\mathrm{mag}}$ | Magnitude of the rotation vector |
| $\tilde S_{\Psi,\eta}$ | Spin element |
| $S_{\Psi,\eta,\lambda\nu}$ | Its components, low |
| $S_{\Psi,\eta,\lambda\nu}^{\mathrm{eq}}$ | Its equilibrium value |
| $\tilde u_{\mathrm r}$ | Rotor of the polar form |
| $\tilde e_{\lambda\nu}$ | Antisymmetric basis element |
| $\rho_{\mathrm{num}}=\lVert\tilde\Xi\rVert^{2}$ | Proper density |
| $\rho_{\mathrm{num,spn}}$ | Density of polarized elements |
| $w_{\mathrm{fl}}$, $p_{\mathrm{th}}$, $p_{\mathrm{qnt}}$, $p_{\mathrm{eff}}$ | Energy density and pressures |
| $s_{\mathrm{ent}}$ | Entropy density |
| $T$, $\beta$ | Temperature, imaginary-time circumference |
| $P_{\mathrm{pol}}$ | Polarization of one element |
| $e_{\mathrm{rot}}$ | Spin-rotation energy density |
| $J_{\Psi,\mathrm{spn},\lambda}$ | Spin current |
| $\kappa_{\mathrm{spn}}$ | Spin diffusion coefficient |
| $\tau_{\mathrm{spn}}$ | Spin relaxation time |
| $\ell_{\mathrm{spn}}$ | Spin diffusion length |
| $\sigma_{\mathrm{ent}}$, $\sigma_{\mathrm{ent,spn}}$ | Entropy production, its spin part |
| $\tilde\Sigma_{\Psi,\mathrm{spn}}$ | Spin contribution to the stress |
| $v_{\Phi,\nu}$ | Components of the flow element |
| $\hbar$, $k_B$, $c$ | Planck constant, Boltzmann constant, speed of light |

## Further Reading

- F. Becattini, "Covariant statistical mechanics and the stress-energy tensor," *Physical Review Letters* **108** (2012) 244502, for the spin potential and the equilibrium density operator with angular momentum.
- F. Becattini and L. Tinti, "The ideal relativistic rotating gas as a perfect fluid with spin," *Annals of Physics* **325** (2010) 1566–1594, for the thermodynamics of a rotating spin fluid.
- W. Florkowski, B. Friman, A. Jaiswal and E. Speranza, "Relativistic fluid dynamics with spin," *Physical Review C* **97** (2018) 041901, for the spin hydrodynamics equations used here as the standard reference.
- W. Israel and J. M. Stewart, "Transient relativistic thermodynamics and kinetic theory," *Annals of Physics* **118** (1979) 341–372, for the relaxation-time closure and the counting argument.
- L. D. Landau and E. M. Lifshitz, *Statistical Physics, Part 1* (Pergamon, 1980), for the thermodynamics of a system in rotation.
- F. Becattini, L. Bucciantini, E. Grossi and L. Tinti, "Local thermodynamical equilibrium and the $\beta$ frame for a quantum relativistic fluid," *European Physical Journal C* **75** (2015) 191, for the local-equilibrium density operator and the frame dependence.
- The companion articles: [The Local Entropy Current](the-local-entropy-current.html), [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html), [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html), and [Causal Dissipative Hydrodynamics in Biquaternionic Form](causal-dissipative-hydrodynamics-in-biquaternionic-form.html).
