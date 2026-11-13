# __The Fourier Transform and the Charged Spin Fluid: A Phase Cannot Rotate a Rotor__

## Introduction

**The whole of the coupling's action on a mode is a translation of its label, in all four slots, and a translation of a label cannot reach the rotor.** That is the article's one sentence, and its reason is a counting argument rather than a type argument. The covariant label of a mode is $\tilde K_{\Phi,\mathrm{gco}}=ik_m\tilde U_{\Psi,\mathrm b}^{-2}$: a timelike element of $\mathbb{B}_\Phi$ of fixed norm, which is the boost multiplied by the mass wave number. **The label therefore has room for the momentum and the frame, and no room for the rotor.** The gauge acts on the label as a translation. So the gauge cannot turn the spin.

**The article's second result is that the loop invariant's two factors are not on the same footing in the momentum decomposition.** The charged fluid's loop invariant is a Lorentz transformation times a phase; at a mode the frame is constant, so the Lorentz factor is the identity and the invariant is the phase alone. **The product $\mathbb{C}^{*}\times SL(2,\mathbb{C})$ is therefore an inter-mode object: one factor is the diagonal's and the other is not**, and no single mode exhibits both.

**The third result is that the force is inter-mode.** A mode's label is a constant, so a mode does not accelerate and the Lorentz force vanishes at a mode identically. The force $ϙF^{\mu\nu}J_\nu$ is the statement about how the label responds to a curvature, and a curvature is exactly what a mode's connection does not have.

**Position in the block.** This is the charged companion of [The Fourier Transform and the Spin Fluid](the-fourier-transform-and-the-spin-fluid.html) and the Fourier companion of [The Charged Spin Fluid: The Force Takes the Charge and the Spin Does Not](the-charged-spin-fluid.html). The charged Schrödinger rung's Fourier article makes the same curvature argument with no frame, and §*The Four Rungs' One Invariant* says what the four share.

## Conventions

The charged companion's: $\tilde A_\Phi=i a_t'e_t+\vec A$ with $a_t'$ and $\vec A$ real, the coupling $ϙ$, the covariant derivative $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$, the gauge transformation $\lambda=\exp(iϙ\Gamma/\hbar)$ with $\Gamma$ real, and

$$
\tilde K_{\Phi,\mathrm{gco}}=\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_\Phi ,
\qquad
\tilde K_{\Phi,\mathrm{gco}}=ik_m\tilde U_{\Psi,\mathrm b}^{-2},
\qquad
k_m=\frac{mc}{\hbar}.
$$

The word is $r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ with $r>0$, $\theta_{\mathrm{rpd}}$ the rapidity, $\theta_{\mathrm{axr}}$ the rotor's angle, $\vec s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ the spin direction, and $\rho_{\mathrm{num}}=r^{2}$. The symbol rule is the spin fluid Fourier companion's.

## The Label, and the Rotor Outside It

**A mode is a point of the momentum space and a constant element of $\mathbb{B}_\Psi$.**

$$
\tilde\Xi(x)=\tilde w(\vec k_\Phi)\,e^{-i\theta_{\mathrm{pwp}}},
\qquad
\theta_{\mathrm{pwp}}=k_t'r_t'-\vec k_\Phi\cdot\vec r .
$$

**The covariant label is a boost and the amplitude is everything else.** The companion's identity $\tilde K_{\Phi,\mathrm{gco}}=ik_m\tilde U_{\Psi,\mathrm b}^{-2}$ is the article's hinge, and it says three things at once. The label's norm is fixed at $-k_m^{2}$, so the label carries no scale. The label's direction is the frame's, so the label carries the whole of the rapidity and the axis. And the label is a *timelike element of $\mathbb{B}_\Phi$*, which has four real components, so **there is no fifth component in which a rotor could live**.

$$
\underbrace{\tilde K_{\Phi,\mathrm{gco}}}_{\text{four numbers}}
\;=\;
\underbrace{k_m}_{\text{the norm}}\times
\underbrace{\tilde U_{\Psi,\mathrm b}^{-2}}_{\text{three numbers}}
\qquad\text{and}\qquad
\tilde u_{\mathrm r}\ \text{is not in the display at all}.
$$

**The gauge acts on the label and on nothing else.** The covariant derivative is a derivative plus $\frac{iϙ}{\hbar}\tilde A_\Phi$, so at a constant connection a plane wave remains a plane wave with

$$
\tilde K_\Phi\longmapsto\tilde K_\Phi-\frac{ϙ}{\hbar}\tilde A_\Phi ,
$$

a translation of four numbers. **So the coupling's whole effect on a mode is a shift of four numbers**, and the four numbers are the label's. The amplitude, the rotor and the spin direction are outside the shifted object by the counting above, and not by an argument about the connection's type.

**The two arguments agree and they are different arguments.** The companion's is algebraic: the connection's temporal slot is a central imaginary and joins the phase bracket, its spatial slots are Hermitian vectors and join the boost bracket, and the rotor bracket is a real vector part that a central element cannot produce. This article's is bookkeeping: the shifted object is the label, and the rotor is not a component of the label. **The second is the stronger one in the momentum space**, because it survives any connection and any profile: whatever the connection does, it does to $\tilde K_{\Phi,\mathrm{gco}}$, and $\tilde K_{\Phi,\mathrm{gco}}$ has no rotor slot.

**The stated objection, and the answer.** The objection is that a general connection is not constant, so its action is a convolution and not a translation, and a convolution can do anything. The answer is that a convolution of the label is still a convolution of the label: an operator acting on the covariant wave number cannot produce a component in a slot the wave number does not have. **The rotor's independence of the connection is a statement about the carrier and not about the operator**, and that is why it holds for every profile and not only for the constant one.

## The Loop Invariant, One Factor at a Time

**The companion's loop invariant is a Lorentz transformation times a phase, and the article asks which factor a mode supplies.**

$$
\mathcal H=\mathrm{P}\exp\oint\Bigl(\Gamma_\mu+\frac{iϙ}{\hbar}A_\mu\Bigr)\mathrm{d}x^\mu
=\underbrace{\mathcal H_{SL(2,\mathbb{C})}}_{\text{the frame's}}\cdot
\underbrace{\exp\Bigl(\frac{iϙ\Phi_B}{\hbar}\Bigr)}_{\text{the phase's}} .
$$

**At a mode the frame is constant, so $\Gamma_\mu=0$ and the first factor is the identity.**

$$
\mathcal H_{\text{mode}}=\exp\Bigl(\frac{iϙ\Phi_B}{\hbar}\Bigr),
\qquad
\mathcal H_{SL(2,\mathbb{C})}=1 .
$$

**So the frozen-frame sector's circulation is the phase, and the frozen-frame sector is exactly the set of modes.** The companion states the first clause as a remark on a sector; this article states the identification, and the identification is what makes the second factor's absence a result rather than a coincidence. **A single mode exhibits one factor of the product and never the other**, and a superposition exhibits both.

**The counting of the two factors matches the two brackets the fluid does not read at a mode.** The $SL(2,\mathbb{C})$ factor is the boost and the rotor's transport; a mode's boost and rotor are constants, so the factor is trivial. The $\mathbb{C}^{*}$ factor is the phase's, and the phase is the one bracket a mode occupies. **The product's two factors are therefore the label's and the frame's, and a mode has one of the two by construction.**

**What that says about quantisation is the companion's and it is repeated because it is easy to misread.** Nothing in either factor is quantised: the phase is a real number modulo $2\pi$ and the Lorentz factor is a continuous element. **A mode's loop datum is a phase and not an integer**, and the integer that appears at the scalar rung comes from a nodal set, which a mode does not have.

## Both Slots Are Translations, and the Force Is Inter-Mode

**At a constant connection the coupling is a translation in all four slots.** The temporal slot shifts $k_t'$ by $ϙa_t'/(\hbar c)$ and the spatial slots shift $\vec k_\Phi$ by $ϙ\vec A/\hbar$, and neither is a rotation, a dilation or a turn.

**A mode's label is constant, so a mode's velocity is constant, so a mode does not accelerate.**

$$
\tilde V_\Phi=ic\,\tilde U_{\Psi,\mathrm b}^{-2}
\quad\text{with}\quad
\tilde U_{\Psi,\mathrm b}\ \text{constant}
\qquad\Longrightarrow\qquad
a^\mu=u^\nu\partial_\nu u^\mu=0 .
$$

**Therefore the Lorentz force vanishes at a mode identically, and the force is an inter-mode object.** The companion's momentum balance $\partial_\nu T^{\mu\nu}=ϙF^{\mu\nu}J_\nu+$ the free spin term is an equation between quantities that a mode holds constant, so at a mode it reads $0=0$. **What it constrains is the off-diagonal part of the field**, and the article's claim is that the phrase "the force takes the charge and the spin does not" is, in the momentum space, the statement that the label is shifted and the rotor is not.

**The two halves of the phrase are therefore of different kinds.** "The force takes the charge" is a statement about the label: the charge is a coefficient of the potential, the potential shifts the label, and the label is the frame, so the force moves the velocity. "The spin does not" is a statement about the carrier: the rotor is not in the label, so nothing that acts on the label can move it. **One half is dynamics and the other is bookkeeping**, and the momentum-space reading separates them for the first time.

**The vorticity follows the same rule and needs no new argument.** At a mode the connection is constant, so $\tilde F=0$ and the companion's vorticity $\omega=ϙF/m$ vanishes; and a curvature is not a multiplier, so no mode carries a vorticity at all. That is the charged Schrödinger rung's result with the frame present, and it is unchanged by the frame.

## The Four Rungs' One Invariant

**Every charged rung of the block has one gauge-invariant object in the momentum-space reading, and it is the curvature.**

| rung | the mode's label | what the gauge does | the invariant |
| --- | --- | --- | --- |
| Schrödinger | $\hbar\vec k$ | shifts it | $\vec B$ |
| Klein–Gordon | $\hbar\tilde K_\Phi$ | shifts it | $\tilde F$ |
| spinor | $ik_m\tilde U_{\Psi,\mathrm b}^{-2}$ | shifts it | $\tilde F$ |
| vector | $r\,u_\mu$ with $u$ constant | shifts it and turns the chart | the coupled field strength |

**The third row is this article's, and it is the row with the least room in it.** The scalar label has four numbers and no frame; the spinor label has four numbers and is the frame; the vector label has four numbers and *is* the field. **So the spinor rung is the one rung whose label is exactly the frame**, and that is why the rotor's independence of the gauge is a counting statement there and an algebraic one elsewhere.

**What the table says in one line.** A gauge is a translation of a label, a translation cannot change a norm, and the norm is the invariant only when the label has nothing else in it. **On the spinor rung the label has a great deal else in it — the whole frame — and the gauge still cannot touch it, because the frame is the label.** That is the precise content of "a phase cannot rotate a rotor".

## Limits

**Constant coefficients.** The translation reading of the gauge needs a constant connection. The counting argument of §*The Label, and the Rotor Outside It* does not: it is a statement about the carrier, and it holds for every profile.

**A single mode against a general field.** §*The Loop Invariant, One Factor at a Time* is exact at a mode. The general field's invariant is the product, and no statement is made about the size of either factor there.

**The denial.** The transform carries $\mathbb{B}_\Psi$-valued fields to $\mathbb{B}_\Psi$-valued fields. The label is an element of $\mathbb{B}_\Phi$ and the amplitude an element of $\mathbb{B}_\Psi$, and no step carries either out of its sector.

## Open Questions

1. **Whether the rotor has any momentum-space datum at all.** The label has no rotor slot, so the rotor is a function of the mode's label only through the amplitude $\tilde w$. Whether the transform of the rotor can be written as a functional of the amplitude's direction alone, in the way the velocity is a functional of the label alone, is not settled.

2. **The size of the Lorentz factor off the diagonal.** A superposition's loop invariant has both factors. Whether the $SL(2,\mathbb{C})$ factor's departure from the identity is bounded by the vorticity of the pair, as the free companion's structure suggests, is not known.

3. **A non-constant connection on a mode.** A uniform field admits no mode at all, so the statement that the force is inter-mode has no mode-based counterexample to offer. Whether the Landau-like structure of the coupled equation in a uniform field is a statement about a basis of non-plane-wave modes, and whether the rotor is still outside the label in that basis, is open.

## Summary

A mode is a point of the momentum space and a constant element of the spinor carrier. Its covariant label is $ik_m\tilde U_{\Psi,\mathrm b}^{-2}$: four numbers, of fixed norm, equal to the boost up to the mass wave number.

The label has room for the momentum and the frame and no room for the rotor. The gauge acts on the label and on nothing else, so at a constant connection the whole effect of the coupling on a mode is a translation of four numbers, and a translation cannot reach the rotor. **That is the counting form of the companion's type argument, and it holds for every profile and not only for the constant one.**

The loop invariant is a Lorentz transformation times a phase. At a mode the frame is constant, so the Lorentz factor is the identity and the invariant is the phase $\exp(iϙ\Phi_B/\hbar)$ alone. The frozen-frame sector is exactly the set of modes, so the product $\mathbb{C}^{*}\times SL(2,\mathbb{C})$ is an inter-mode object with one factor on the diagonal.

Both slots of the connection are translations at a mode, so a mode's velocity is constant, its acceleration is zero and the Lorentz force vanishes identically. **The force is inter-mode**, and the phrase "the force takes the charge and the spin does not" is a dynamical statement about the label followed by a bookkeeping statement about the carrier.

The vorticity is $ϙF/m$ and a constant connection has no curvature, so a mode is irrotational. Across the four charged rungs the only gauge-invariant object of the momentum-space reading is the curvature, and the spinor rung is the one whose label is exactly the frame.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $ϙ$ | The coupling |
| $\tilde A_\Phi=i a_t'e_t+\vec A$ | The connection |
| $\tilde K_{\Phi,\mathrm{gco}}=\tilde K_\Phi+ϙ\tilde A_\Phi/\hbar$ | The covariant label |
| $\tilde K_{\Phi,\mathrm{gco}}=ik_m\tilde U_{\Psi,\mathrm b}^{-2}$ | The label as the boost |
| $k_m=mc/\hbar$ | The mass wave number |
| $\tilde w(\vec k_\Phi)$ | The carrier's element at a mode |
| $\theta_{\mathrm{pwp}}=k_t'r_t'-\vec k_\Phi\cdot\vec r$ | The phase of a mode |
| $\theta_{\mathrm{rpd}}$, $\theta_{\mathrm{axr}}$ | The rapidity and the rotor's angle |
| $\vec s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ | The spin direction |
| $\mathcal H=\mathcal H_{SL(2,\mathbb{C})}\exp(iϙ\Phi_B/\hbar)$ | The loop invariant |
| $\Phi_B$ | The flux through the loop's spanning surface |
| $\lambda=\exp(iϙ\Gamma/\hbar)$ | The gauge element; central |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Yakir Aharonov and David Bohm, "Significance of electromagnetic potentials in the quantum theory," *Physical Review* **115** (1959) 485–491, for the phase factor of a mode on a loop.
- Michael Berry, "Quantal phase factors accompanying adiabatic changes," *Proceedings of the Royal Society A* **392** (1984) 45–57, for the product of a phase and a frame's transport, which §*The Loop Invariant, One Factor at a Time* splits.
- Alexander J. Silenko, "Spin precession in a magnetic field and the Lorentz force," *Physics of Particles and Nuclei Letters* **14** (2017) 256–259, for the standard statement that the field turns the spin only through the transport of the frame.
- The companion articles: [The Charged Spin Fluid: The Force Takes the Charge and the Spin Does Not](the-charged-spin-fluid.html), for the type table, the loop invariant and the force without torque; [The Fourier Transform and the Spin Fluid](the-fourier-transform-and-the-spin-fluid.html), the free rung's four brackets and the vorticity's inter-mode character; [The Fourier Transform and the Charged Schrödinger Fluid](the-fourier-transform-and-the-charged-schrodinger-fluid.html), the same curvature argument with no frame; and [The Fourier Transform and the Dirac Equation in Biquaternionic Polar Variables](the-fourier-transform-and-the-dirac-equation-in-biquaternionic-polar-variables.html), for the mode count and the mass's off-diagonal action in the part label.
