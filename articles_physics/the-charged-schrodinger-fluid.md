# __The Charged Schrödinger Fluid: The Vorticity Is the Magnetic Field__

## Introduction

**The claim of this article is that the coupling does three things and no more: it turns the vorticity from zero into the field, it adds the Lorentz force to the acceleration law, and it splits the momentum into a canonical and a kinetic half.** The free fluid's vorticity is zero identically; the charged fluid's is $\vec\omega=\varkappa\vec B/m$, the field itself, exactly and at every solution. Everything else is untouched: the density, the quantum potential and the quantum stress do not move. The reason is a fact of type — the connection is a central imaginary number in every slot, so it joins the phase bracket and cannot reach the scale — and the rest of the article is that fact read in fluid words.

**The article is the rung below [The Charged Klein–Gordon Fluid](the-charged-klein-gordon-fluid.html), and the comparison is the reason it exists.** There the velocity is the kinetic momentum over the mass, a four-vector whose norm the equation fixes, and it deserves the name of a velocity only where the quantum potential vanishes; the vorticity identity $\mathrm{d}V=(\varkappa/m)F$ therefore carries a qualification, and the vorticity reaches rank four whenever $\vec E\cdot\vec B\ne0$. Here the velocity is a velocity, the identity is unconditional, and the vorticity's rank is two at most. The two articles are one theorem at two values of the order of the equation, and the difference between them is the whole content of this rung.

**What the article supplies, in four statements.**

- The connection joins the phase bracket only, by its algebraic type, so the density, the quantum potential and the stress are untouched.
- The vorticity is the magnetic field: $\nabla\times\vec v=\varkappa\vec B/m$, exactly, with no normalisation caveat; and the electric field never enters it.
- The vorticity has no dynamics of its own: its rate is Faraday's law, $\partial_{t'}\vec\omega=-(\varkappa/m)\nabla\times\vec E$, with no velocity in the statement.
- The Lorentz force appears in the acceleration law as $-\varkappa(\vec E+\vec v\times\vec B)$, and the quantum force stays charge-blind.

**The article is a reading and not a derivation.** The covariant pair is [The Coupled Schrödinger Equation in Biquaternionic Polar Variables](the-coupled-schrodinger-equation-in-biquaternionic-polar-variables.html), §*The Central Field in the Operator Setting*: the covariant continuity equation, the covariant Hamilton–Jacobi equation, and the statement that the quantum potential is unchanged. This article takes them and asks what the object is in fluid words.

**Conventions.** The free companion's, and the coupled polar article's for the connection: $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$ with $\varphi$ and $\vec A$ real, the coupling $\varkappa$ being minus the electric charge, so that $\vec\pi=-i\hbar\nabla+\varkappa\vec A$ and the potential energy enters as $-\varkappa\varphi$. Time is $t'$, the density is $\rho_{\mathrm{num}}=r^{2}$, the action is $S=\hbar\theta_{\mathrm{pha}}$, and the quantum potential is $Q=-\hbar^{2}\Delta r/(2mr)$. The gauge transformation is $\lambda=\exp(i\varkappa\Gamma/\hbar)$ with $\Gamma$ real.

## The Word Collapses, and the Connection Joins the Phase

**The field is central**, $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon\,e_t$, and the covariant derivative is the free one with a central addition in each slot,

$$
\tilde\Xi^{-1}D_{t'}\tilde\Xi=\partial_{t'}\ln r+i\Bigl(\partial_{t'}\theta_{\mathrm{pha}}-\frac{\varkappa}{\hbar}\varphi\Bigr),
\qquad
\tilde\Xi^{-1}D_{\eta}\tilde\Xi=\partial_{\eta}\ln r+i\Bigl(\partial_{\eta}\theta_{\mathrm{pha}}+\frac{\varkappa}{\hbar}A_{\eta}\Bigr).
$$

**The addition is a central imaginary number, so it has one place to go.** The logarithmic derivative splits into a real scalar, a central imaginary, a Hermitian element and a real vector; $-\frac{i\varkappa}{\hbar}\varphi$ and $+\frac{i\varkappa}{\hbar}A_\eta$ are central imaginary, so they join the second part and no other. On a central field there is no third and no fourth part to receive anything; on a general field there is, and they still receive nothing, because the addition's type does not depend on the field.

**Three quantities are therefore invariant before any calculation.** The scale is: $\partial_\eta\ln r$ is untouched. The density is, because it is a function of the scale. The quantum potential is, because it is built from $r$ and its ordinary Laplacian, and the gradient the connection could shift is the phase's and not the scale's. The statement is exact and it is the article's sharpest one: *the field cannot make a quantum fluid denser or its quantum pressure stronger; it can only turn the phase.*

**The two gauge-invariant combinations are the kinetic momentum and the kinetic energy.**

$$
\vec\pi=\hbar\nabla\theta_{\mathrm{pha}}+\varkappa\vec A=\nabla S+\varkappa\vec A,
\qquad
\mathcal E=-\hbar\,\partial_{t'}\theta_{\mathrm{pha}}+\varkappa\varphi .
$$

Both are invariant term by term: the phase's gradient shifts by $\varkappa\nabla\Gamma$ and $\vec A$ by $-\nabla\Gamma$; the phase's rate shifts by $-\varkappa\partial_{t'}\Gamma$ and $\varphi$ by $+\partial_{t'}\Gamma$. Neither the phase nor its rate is invariant alone, and the pairing is the statement that the fluid's data are the invariants and the chart's coordinates are not.

## The Pair

**The substitution is the free one with the kinetic momentum in place of the gradient.**

$$
\boxed{\;\frac{\partial S}{\partial t'}+\frac{\lvert\nabla S+\varkappa\vec A\rvert^{2}}{2m}-\varkappa\varphi+Q=0,\qquad
\frac{\partial\rho_{\mathrm{num}}}{\partial t'}+\nabla\cdot\Bigl(\rho_{\mathrm{num}}\frac{\nabla S+\varkappa\vec A}{m}\Bigr)=0,\;}
$$

with $Q$ exactly the free article's. The two changes in the Hamilton–Jacobi equation are the kinetic momentum in the kinetic term and the potential energy; the change in the continuity equation is the kinetic velocity in place of the canonical one. There is no third change, and the absence of a third is the type argument of the previous section read on the pair.

**The pair is the free pair written on two invariants.** $\vec\pi/m$ is the velocity and $\mathcal E$ is the energy, and both are gauge invariant; $S$ and $\theta_{\mathrm{pha}}$ are not. So the fluid's equations are statements about invariants, and the gauge freedom acts on a coordinate that the equations use only through its derivatives.

**What the pair is not.** It is not the free pair with a force added: the magnetic term is in the kinetic term and in the velocity, so it changes the kinematics as well as the dynamics. A field that shifted only the potential would leave the vorticity zero; this one does not, and the next two sections are that difference.

## The Two Momenta and the Two Currents

**There are two momenta and one velocity.**

$$
\vec p_{\mathrm{can}}=\nabla S,
\qquad
\vec\pi=\nabla S+\varkappa\vec A,
\qquad
\vec v=\frac{\vec\pi}{m},
\qquad
\vec j=\rho_{\mathrm{num}}\vec v .
$$

The canonical momentum is a gradient and the kinetic momentum is a gradient plus a potential; the velocity is the second over the mass. **The velocity is the physical one**, and it is not a gradient, which is the whole of the difference from the free article.

**There are two currents and they are proportional, so there is one conservation law.** The mass current is $\vec j=\rho_{\mathrm{num}}\vec v$ and the electric current is $\varkappa\vec j$; both are conserved by the same continuity equation, and the charge density is $\varkappa\rho_{\mathrm{num}}$. Nothing has to be added: a charged fluid with one species has one conservation law, and the charge's is the mass's times a constant.

**The density is gauge invariant and the phase is not, and the pair respects it.** $\rho_{\mathrm{num}}=r^{2}$ is invariant because the gauge transformation is unitary and central. $\vec v$ is invariant because $\vec\pi$ is. $S$ is not, and the continuity equation does not contain it except through $\vec v$. So the conservation law is a statement about invariants and the gauge freedom never enters it.

**One consequence for the count.** The free article has three data at each event; the coupling adds no fourth, and it adds a redundancy: the phase is translated by an arbitrary function, so a line of chart coordinates describes one field. The polar companion calls this the one structural change the coupling makes in kind, and in fluid terms it is the statement that the velocity, not the potential, is the fluid's datum.

## The Euler Equation Is the Lorentz Force

**The gradient of the Hamilton–Jacobi equation is the acceleration law, and the magnetic term turns it into the Lorentz force.** With $\vec v=\vec\pi/m$ and $\vec E=-\nabla\varphi-\partial_{t'}\vec A$, $\vec B=\nabla\times\vec A$,

$$
\frac{\mathrm{D}\pi_{i}}{\mathrm{D}t}\equiv\frac{\partial\pi_{i}}{\partial t'}+v_{j}\partial_{j}\pi_{i}
=-\varkappa\bigl(\vec E+\vec v\times\vec B\bigr)_{i}-\partial_{i}Q .
$$

*Proof.* Differentiating the Hamilton–Jacobi equation in space gives $\partial_{t'}\partial_{i}S=-(v_{j}\partial_{i}\pi_{j})+\varkappa\partial_{i}\varphi-\partial_{i}Q$; adding $\varkappa\partial_{t'}A_{i}$ and $v_{j}\partial_{j}\pi_{i}$, and using $\partial_{j}\pi_{i}-\partial_{i}\pi_{j}=-\varkappa\varepsilon_{ijk}B_{k}$ and $\partial_{i}\varphi+\partial_{t'}A_{i}=-E_{i}$, gives the display. The identity was also checked component by component with a symbolic algebra system, on an arbitrary $S$, $\vec A$ and $\varphi$.

**With $\varkappa$ the negative of the electric charge, this is the standard force.** Writing $q=-\varkappa$, the right-hand side is $q(\vec E+\vec v\times\vec B)-\nabla Q$: the Lorentz force of a charge $q$ plus the quantum force. The two are separate objects and neither modifies the other. The Lorentz force is odd in the coupling and vanishes at $\varkappa=0$; the quantum force does not contain the coupling at all, and it is the whole of the free article's Euler equation.

**The quantum force is charge-blind.** $\nabla Q$ carries $r$ and its Laplacian and nothing else, so a charged and a neutral fluid with the same density have the same quantum force at the same event. The statement is the type argument's consequence and it is worth isolating: of the two forces on a fluid element, one is the field's and one is the density's, and the field cannot reach the density's.

**The inertia is still $m$ and there is still no factor of $\gamma$.** The companion's law carries $\gamma^{-1}$ because its flow variable is normalised; this one does not, and the coupling does not introduce one. A relativistic charged fluid's acceleration law has two reasons for a $\gamma$ — the normalisation and the field's part in the four-velocity — and the first-order fluid has neither.

## The Vorticity Is the Field

**The velocity is a gradient plus a potential, so its curl is the field.**

$$
\vec\omega=\nabla\times\vec v=\frac{\varkappa}{m}\,\vec B,
\qquad
\nabla\times\vec p_{\mathrm{can}}=0 .
$$

The canonical flow is irrotational, exactly as in the free article; the kinetic flow is rotational exactly where the magnetic field is and nowhere else. With $\varkappa$ the negative of the electric charge this reads $\vec\omega=-(q/m)\vec B$, which is the cyclotron angular velocity of a charge $q$: the fluid's vorticity *is* the cyclotron frequency, and the Larmor rate needs no separate calculation at this rung.

**This is the unconditional form of the identity the charged Klein–Gordon article states with a qualification.** There the velocity is the kinetic momentum over the mass, a four-vector whose norm the equation fixes, and it is a velocity only where $Q$ vanishes; the identity $\mathrm{d}V=(\varkappa/m)F$ is therefore exact and its *reading as the vorticity of a flow* is not. Here the velocity is a velocity, $\vec\omega$ is the vorticity, and the identity is exact in both senses. It is the cleanest instance of the identity in the block, and it is clean because the rung is the lowest one that has a charge.

**Three consequences follow, and the first is a constraint on the flow.**

*The fluid cannot rotate where the field is zero.* In a region with $\vec B=0$ the flow is irrotational, so the fluid's rotation is not a degree of freedom but a response. This is the non-relativistic form of the statement that a charged quantum fluid's circulation is fixed by the flux, and it is why the loop statements of the next section are about the flux and not about the flow.

*The vorticity cannot carry a monopole.* $\vec\omega$ is a curl by construction, so $\nabla\cdot\vec\omega=0$ identically; combined with $\vec\omega=\varkappa\vec B/m$ this says $\nabla\cdot\vec B=0$. The chart therefore cannot represent a magnetic monopole, and the statement is an identity of the chart and not an extra equation: a vorticity that is a curl has no divergence to carry.

*The vorticity has no dynamics of its own.* Since $\vec\omega$ is a function of $\vec B$ and of nothing else, its rate is

$$
\frac{\partial\vec\omega}{\partial t'}=\frac{\varkappa}{m}\frac{\partial\vec B}{\partial t'}=-\frac{\varkappa}{m}\nabla\times\vec E ,
$$

which is Faraday's law and contains no velocity. The Helmholtz vorticity equation of a classical fluid — transport, stretching and tilting — has no independent content here: the vorticity is slaved to the field, and what a classical fluid would call its vortex dynamics is the field's own equation read on a derived quantity.

**The rank is two, and the electric field never enters.** $\vec\omega$ is a three-vector, so it has at most two independent components; the vorticity 2-form has no time-space part because the non-relativistic velocity has no time component. This is the sharpest structural difference from the charged Klein–Gordon fluid, whose vorticity reaches rank four exactly when $\vec E\cdot\vec B\ne0$. The relativistic vorticity mixes the two halves of $F$ because a boost mixes them, and the rank-four condition is precisely the invariant that has no Galilean image. **Here $\vec E$ accelerates and $\vec B$ rotates, and the two never swap.**

## Circulation, Flux and the Loop

**The canonical circulation is quantised always and the kinetic circulation only where the flux vanishes.** Around a loop that links a nodal line,

$$
\oint\vec v\cdot\mathrm{d}\vec l=\frac{2\pi\hbar\,n+\varkappa\,\Phi_{B}}{m},
\qquad
\Phi_{B}=\oint\vec A\cdot\mathrm{d}\vec l=\int_{\Sigma}\vec B\cdot\mathrm{d}\vec S,
$$

with $n$ the winding of the phase. The derivation is one line: $\vec v=(\nabla S+\varkappa\vec A)/m$, the phase is single valued on the field so its gradient integrates to $2\pi\hbar n$, and the potential integrates to the flux. With $\varkappa$ the negative of the electric charge this is $(2\pi\hbar n-q\Phi_{B})/m$, the standard statement that a magnetic flux shifts every circulation quantum.

**So the flux shifts the circulation and does not quantise it.** The kinetic circulation is a multiple of $2\pi\hbar/m$ exactly when $\varkappa\Phi_{B}$ is one too — in particular where $\vec B$ vanishes on a spanning surface — and otherwise it takes the flux's value and is not a multiple of anything. The canonical circulation, being $\nabla S$'s, is a multiple always.

**What the loop statement needs is only one phase, single valued on the loop.** It does not need the connection to be weak, the flow to be slow, or the region to be free of the field's effects; and it does not need a condensate. The single-particle fluid's circulation is quantised for the same reason a superfluid's is, and the reason is the single-valuedness of one phase, not the presence of a macroscopic occupation.

**The Aharonov–Bohm statement and the fluxoid are the same identity read twice.** The potential is invisible locally — the pair contains it only in $\vec\pi$ and $\mathcal E$, both of which are gauge invariant — and visible on a loop, where it integrates to the flux. The polar companion records the two settings of the same fact, and this article's contribution is only to say which fluid quantity carries it: the velocity does, and the phase does not.

## What the Coupling Does Not Change

**Density, quantum potential and stress are untouched, and the reason is one type.** $\rho_{\mathrm{num}}=r^{2}$ is the scale's; $Q$ is the scale's Laplacian; $\sigma^{Q}_{ij}=\frac{\hbar^{2}}{4m}\rho_{\mathrm{num}}\partial_{i}\partial_{j}\ln\rho_{\mathrm{num}}$ is the scale's second derivatives. The connection is central imaginary, joins the phase bracket, and cannot reach the scale. So the stress identity of the free article holds verbatim, with the same tensor and the same force:

$$
\partial_{j}\sigma^{Q}_{ij}=-\rho_{\mathrm{num}}\,\partial_{i}Q,
$$

and the force it produces is the second term of the Euler equation and not the first.

**The equation of state remains absent, and for the same reason.** $\sigma^{Q}_{ij}$ carries two derivatives of $\ln\rho_{\mathrm{num}}$, so no function of the density's value reproduces it; the coupling does not supply one, because a function of the field is not a function of the density.

**One sheet remains one sheet.** The density is a norm, the equation is first order in time, and there is no sign to lose and no antiparticle in the data. The charged Klein–Gordon fluid has two sheets and its charge density changes sign with the energy; here the charge density is $\varkappa\rho_{\mathrm{num}}$, its sign is the coupling's, and it is the same at every event of a solution.

**In the constant setting the coupling is a rigid displacement.** With a constant Hamiltonian and a constant connection the coupled flow is the free flow with $h_{t}\to h_{t}-\varkappa\varphi$ and $\vec h_{\Psi}\to\vec h_{\Psi}+\varkappa\vec A$: the phase advances at minus the mean of the shifted pair, every carried direction precesses at the shifted gap, and the scale and the rapidity stay frozen. The polar companion states it, and in fluid terms it is that a constant potential shifts the frequency and a constant vector potential rotates the axis of the precession, with no change to the density.

## The Ladder

**The vorticity is the quantity the ladder orders, and the ordering is by the order of the equation and by the charge.**

| rung | velocity | vorticity | rank |
| --- | --- | --- | --- |
| Euler, $\hbar\to0$ | $\nabla\Phi$, a gradient | $0$ | $0$ |
| Schrödinger | $\nabla S/m$, a gradient | $0$ | $0$ |
| charged Schrödinger | $\vec\pi/m$, a gradient plus a potential | $\varkappa\vec B/m$ | $2$ |
| Klein–Gordon | $\tilde P_{\Phi}/m$, a gradient | $0$ | $0$ |
| charged Klein–Gordon | $\tilde P^{\mathrm{mech}}/m$, a four-vector whose norm the shell fixes | $\mathrm{d}V=(\varkappa/m)F$ | $4$ iff $\vec E\cdot\vec B\ne0$ |

**Two arrows run through the table.** Adding the charge turns a zero into the field's own curl, and adding the second order of the equation turns a three-vector into a two-form and lets the electric half in. The two additions are independent: the charged Schrödinger fluid has a charge and rank two, the free Klein–Gordon fluid has the second order and rank zero.

**The rank is the count of what the flow can hold.** Rank zero is one function's worth, which is what a scalar phase carries. Rank two is a curl's worth, which is what a vector potential carries. Rank four is the whole of an antisymmetric tensor, and only a fluid whose velocity is a four-vector with the shell's norm can reach it — which is to say, only a relativistic fluid can have a vorticity that knows both halves of the field. The ladder's last row is not a stronger statement than the third; it is a statement of a different kind, and the difference is the equation's order.

## What Is Established and What Is Interpretation

**Established.** That the connection is central imaginary in every slot and joins the phase bracket only, by its type. That the density, the quantum potential and the quantum stress are therefore invariant under the coupling. The covariant pair, with the kinetic momentum in the continuity equation and in the kinetic term, and $-\varkappa\varphi$ in the potential. The gauge invariance of $\vec\pi$ and $\mathcal E$, term by term. That the velocity is $\vec\pi/m$ and is not a gradient. That the Lorentz force appears as $-\varkappa(\vec E+\vec v\times\vec B)$ in the acceleration law, verified component by component, with the quantum force charge-blind and additive. The vorticity identity $\vec\omega=\varkappa\vec B/m$, exact and unconditional, with the canonical flow irrotational. That $\nabla\cdot\vec\omega=0$ combined with the identity gives $\nabla\cdot\vec B=0$. That the vorticity's rate is Faraday's law, with no velocity in it. That the kinetic circulation is $(2\pi\hbar n+\varkappa\Phi_{B})/m$ and the canonical one is $2\pi\hbar n/m$. That the stress identity and the absence of a state law survive the coupling unchanged. That the vorticity's rank is at most two, and that $\vec E\cdot\vec B$ therefore has no non-relativistic image.

**Interpretation.** That the vorticity's being the field is best read as the statement that the fluid's rotation is a response and not a degree of freedom: the warrant is that $\vec\omega$ is a function of $\vec B$ alone, and the reading is the programme's step. That the rank table orders the block by the equation's order rather than by the field's spin is an observation about the table and not a theorem; the spin-one and spinor fluids of the block are not in it. That the identity's unconditional form at this rung is a *gain* is a judgement; the companion's qualified statement is not refuted by it.

**Not claimed.** It is not claimed that the fluid is a superconductor or a condensate: the circulation is quantised for a single particle's fluid, and the condensate's version is [Superfluids and BECs](superfluids-and-becs-the-gross-pitaevskii-equation-as-the-nonlinear-reverse-map.html). It is not claimed that $\nabla\cdot\vec B=0$ is derived from fluid mechanics; it is an identity of a chart in which the vorticity is a curl. It is not claimed that the flow is curl-free in a region where $\vec B\ne0$; there the vorticity is the field's. It is not claimed that the coupling modifies the quantum potential in any limit, because it does not modify it at all.

## Summary

The connection is a central imaginary number in every slot, so it joins the phase bracket and no other; the scale, the density, the quantum potential and the quantum stress are untouched.

The pair is the free pair on two invariants: the kinetic momentum $\vec\pi=\nabla S+\varkappa\vec A$ in the continuity equation and in the kinetic term, and $-\varkappa\varphi$ in the potential, with $Q$ exactly the free quantum potential.

There are two momenta and one velocity. The canonical momentum is a gradient and the canonical flow is irrotational; the kinetic momentum is a gradient plus a potential, and the velocity is the second over the mass.

The acceleration law is the Euler equation with the Lorentz force: $\mathrm{D}\pi_{i}/\mathrm{D}t=-\varkappa(\vec E+\vec v\times\vec B)_{i}-\partial_{i}Q$, with inertia $m$, no factor of $\gamma$, and a quantum force that does not contain the coupling.

The vorticity is the field: $\vec\omega=\varkappa\vec B/m$, exactly and at every solution, with no normalisation caveat. The fluid cannot rotate where the field is zero; the vorticity is divergence-free and so carries no monopole; and its rate is Faraday's law, with no velocity in the statement.

The rank is two, and the electric field never enters the vorticity. The charged Klein–Gordon fluid's rank four when $\vec E\cdot\vec B\ne0$ has no non-relativistic image, because a boost mixes the two halves of the field and there is no boost here.

The kinetic circulation is $(2\pi\hbar n+\varkappa\Phi_{B})/m$ around a loop that links a node, and the canonical circulation is $2\pi\hbar n/m$ unconditionally; the kinetic one is a multiple of $2\pi\hbar/m$ only where the flux is. The flux term is the same statement as the Aharonov–Bohm phase.

The density is a norm with one sign, so the charge density $\varkappa\rho_{\mathrm{num}}$ has one sign too, and there is no second sheet.

The stress identity, the absence of an equation of state and the non-dissipativity all survive the coupling unchanged, and each survives for the same reason: the connection cannot reach the scale.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon\,e_t$ | The central field, in its word |
| $\varkappa$ | Coupling; minus the electric charge, $q=-\varkappa$ |
| $\varphi$, $\vec A$ | Scalar and vector potentials |
| $S=\hbar\theta_{\mathrm{pha}}$ | Action; gauge dependent |
| $\vec p_{\mathrm{can}}=\nabla S$ | Canonical momentum; a gradient |
| $\vec\pi=\nabla S+\varkappa\vec A$ | Kinetic momentum; gauge invariant |
| $\vec v=\vec\pi/m$ | Velocity; gauge invariant |
| $\mathcal E=-\hbar\partial_{t'}\theta_{\mathrm{pha}}+\varkappa\varphi$ | Kinetic energy; gauge invariant |
| $\rho_{\mathrm{num}}=r^{2}$ | Density; gauge invariant |
| $\vec j=\rho_{\mathrm{num}}\vec v$ | Current; the charge current is $\varkappa\vec j$ |
| $Q=-\hbar^{2}\Delta r/(2mr)$ | Quantum potential; unchanged by the coupling |
| $\sigma^{Q}_{ij}=\frac{\hbar^{2}}{4m}\rho_{\mathrm{num}}\partial_{i}\partial_{j}\ln\rho_{\mathrm{num}}$ | Quantum stress; unchanged by the coupling |
| $\vec\omega=\nabla\times\vec v$ | Vorticity; $\varkappa\vec B/m$ |
| $\vec E=-\nabla\varphi-\partial_{t'}\vec A$, $\vec B=\nabla\times\vec A$ | Field strengths |
| $\Phi_{B}=\oint\vec A\cdot\mathrm{d}\vec l$ | Magnetic flux through a spanning surface |
| $\lambda=\exp(i\varkappa\Gamma/\hbar)$ | Gauge transformation |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1926) 322–326, for the free pair that the coupling is added to.
- Fritz London and Heinz London, "Supraleitung und Diamagnetismus," *Physica* **2** (1935) 341–354, for the response of a charged quantum fluid to a vector potential, and hence for the loop statement of §*Circulation, Flux and the Loop*.
- Yakir Aharonov and David Bohm, "Significance of electromagnetic potentials in the quantum theory," *Physical Review* **115** (1959) 485–491, for the phase on a loop.
- Giovanni Manfredi, "How to model quantum plasmas," *Fields Institute Communications* **46** (2005) 263–287, for the quantum hydrodynamic model with a self-consistent field, whose spinless non-relativistic form is this article's fluid.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), §5, for the charged fluid's Lorentz force and its quantum force.
- Lars Onsager, "Statistical hydrodynamics," *Il Nuovo Cimento* **6** (1949) 279–287, and Richard Feynman, "Application of quantum mechanics to liquid helium," in *Progress in Low Temperature Physics* I (1955), for the circulation quantum that §*Circulation, Flux and the Loop* carries over to a single particle's fluid.
- The companion articles: [The Coupled Schrödinger Equation in Biquaternionic Polar Variables](the-coupled-schrodinger-equation-in-biquaternionic-polar-variables.html), [The Schrödinger Fluid](the-schrodinger-fluid.html), [The Charged Klein–Gordon Fluid: Vorticity Is the Field Strength](the-charged-klein-gordon-fluid.html), [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), [Superfluids and BECs: The Gross–Pitaevskii Equation as the Nonlinear Reverse Map](superfluids-and-becs-the-gross-pitaevskii-equation-as-the-nonlinear-reverse-map.html), [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html), and [The Direction of the Fluid-Wave Correspondence, Field by Field](the-direction-of-the-fluid-wave-correspondence-field-by-field.html).
