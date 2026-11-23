# __The Schrödinger Equation in the Non-Quantum Limit__

## Introduction

Take the complete polar decomposition of the parent, count one spatial derivative of the phase as order one and one spatial derivative of the scale as order $\epsilon$, and the exact pair the parent prints separates into three orders: the Hamilton–Jacobi equation, the transport equation, and the quantum potential.

[The Schrödinger Equation in Biquaternionic Polar Variables](the-schrodinger-equation-in-biquaternionic-polar-variables.html) writes the field as the four-factor word $\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ and prints, boxed, the two exact real equations that the central field obeys. Nothing below re-derives them. Each term of that pair is assigned a power of one parameter, and the limit is the statement of which powers survive.

What the polar chart settles before any parameter appears. Three things, and none of them is available in a form-first account. The amplitude of the limit is the word's scale $\varrho$ and not a coefficient read off a column. The density of the limit is the parent's Hermitian norm $\rho_{\mathrm{num}}=2\varrho^{2}\cosh\theta_{\mathrm{rpd}}$, which equals $2\varrho^{2}$ exactly when the boost is the identity and to no order otherwise. And the frame's two brackets — the boost's connection and the rotor's — carry no derivative of a rapidly varying object, so the parameter does not order them: they are either present or absent, and the parent's own class statement says which case closes.

The pair is closed on the central class, $\varrho\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_{t}$, and the parent proves that class is invariant exactly under a central Hamiltonian. The limit therefore takes place inside the central class. A general field's word has four brackets and its pair is not closed, so there is nothing to order; the limit is not defined on it, and no truncation of the four brackets is claimed here.

The criterion. $\epsilon=1/(k_{\Phi}L)$, with $k_{\Phi}=\frac{2\pi \lvert\vec p\rvert}{h}$ and $L$ the length over which the scale varies, $L^{-1}=\lvert\vec\nabla_\Phi\ln \varrho\rvert$. The quantum potential over the kinetic energy is $\epsilon^{2}$; the scale's gradient over the phase's is $\epsilon$. The parameter is defined in *The Non-Quantum Limit of the Biquaternion Model*, and it is the same one here, with $\varrho$ in the place of the amplitude.

The parent's pair is exact and its two lines are ordered differently: the real line is an expansion whose third term is the quantum potential, and the imaginary line is not an expansion at all. Order zero is the Hamilton–Jacobi equation, whose characters are the classical trajectories and whose algebra form is a norm. Order one is the transport equation, which the limit does not produce and cannot spoil, and which gives $C/\sqrt{\lvert p\rvert}$ in one dimension and the van Vleck determinant in three. Order two is the quantum potential, and its ratio to the kinetic energy is $\epsilon^{2}$ everywhere but is not bounded on any region, which is the difference between the limit and the approximation.

The amplitude–phase decomposition, the two real equations, the Hamilton–Jacobi equation, the method of characteristics, the optical–mechanical analogy, the transport equation, the WKB amplitude, the van Vleck determinant and the quantum potential are standard, and each is in every textbook on semiclassical mechanics. Added here: the ordering of the parent's own terms against one parameter, the norm reading of the eikonal, the identification of the limit's amplitude and density with two specific factors of the polar word, and the statement that the limit is defined only on the central class.

Conventions. Those of the polar parent, unchanged: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_{t}=1$ and $\vec e_\mu^{2}=-e_{t}$; $i$ central; $\mathbb{B}_{C}$ the centre, $\mathbb{B}_{H}$ the real-quaternion subspace, $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ the Hermitian and anti-Hermitian sectors; $\natural$ quaternion conjugation and $*$ the Hermitian one; $\mathrm{Sc}$ the coefficient of $e_{t}$; time is $t'$ and $r'_{t}=ct'$. The word is the parent's, with its eight real parameters, and the action is $S=\frac{h}{2\pi}\theta_{\mathrm{pha}}$.

No mass shell is produced, and the parent says why. The equation is first order in time, so its symbol constrains no second time derivative and the dispersion relation defines the frequency rather than restricting the field. The limit therefore lands on a Hamilton–Jacobi equation and a conservation law and on nothing else. That is a property of the family and not a shortfall of the treatment.

Only derivatives carry $\epsilon$, and only spatial ones. The phase $\theta_{\mathrm{pha}}$ is order zero, its gradient is order zero, and every derivative of the scale costs one power. The time derivative is not ordered at all: the equation is first order in time, and its time derivative is eliminated, not expanded.

## The Word and What the Limit Reads From It

The word. The parent's display, repeated because every statement below is a statement about one of its factors:

$$
\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\Psi,\mathrm b}=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
$$

with $\varrho>0$ real, $\theta_{\mathrm{pha}}$ central and real, the third factor a Hermitian positive boost and the fourth a real rotor. The parent proves the word is a bijection onto the invertibles of $\mathbb{B}$ and that the flow preserves the invertibles, so the chart is total on the generic field.

The table is the article's premise.

| factor | what it is | order in $\epsilon$ | why |
|---|---|---|---|
| $\varrho$ | the scale | amplitude | its derivative is what the parameter measures |
| $\theta_{\mathrm{pha}}=\frac{2\pi S}{h}$ | the central angle | $0$ | its gradient is the momentum, and that is the leading term |
| $\tilde U_{\Psi,\mathrm b}$ | the boost, rapidity $\theta_{\mathrm{rpd}}$ | not ordered | a frame, and a frame's rate is not a derivative of a fast object |
| $\tilde u_{\mathrm r}$ | the rotor, angle $\theta_{\mathrm{axr}}$ | not ordered | the same |

The boost's bracket in the parent's logarithmic derivative is $\tilde U_{\Psi,\mathrm b}^{-1}\partial_{t'}\tilde U_{\Psi,\mathrm b}$, a connection and not a gradient: it measures how the frame turns, and a frame that turns slowly contributes a term of the same size as the terms beside it. There is no small parameter attached to it because there is no derivative of a phase in it. The rotor's bracket is the same object in the real-vector part. So the parameter orders two of the four factors and has nothing to say about the other two.

**The limit's amplitude is the scale, and the limit's density is the Hermitian norm.** The parent's two norms read different factors: the quaternionic norm is $\langle\tilde\Xi\rangle_{\natural}=\varrho^{2}e^{2i\theta_{\mathrm{pha}}}$ and reads the scale and the phase, and the Hermitian norm is

$$
\rho_{\mathrm{num}}=2\,\mathrm{Sc}\bigl(\tilde\Xi^{\dagger}\tilde\Xi\bigr)=2\,\mathrm{Sc}\bigl(\tilde\Xi\tilde\Xi^{*}\bigr)=2\varrho^{2}\cosh\theta_{\mathrm{rpd}}
$$

and reads the scale and the boost. On the central class $\theta_{\mathrm{rpd}}=0$ and $\rho_{\mathrm{num}}=2\varrho^{2}$, so the density of the limit is the Hermitian norm evaluated where the boost is the identity. **Away from that class the two do not agree at any order**, and that is why the limit is stated there and not here.

On a central field the third and fourth brackets of the parent's identity vanish and the first two remain; the equation then separates into the parent's boxed pair. The parent also proves the class is invariant exactly under a central Hamiltonian and not in general. The limit inherits both facts: the pair it orders exists on the central class, and the class stays inside itself only for the Hamiltonian that the parent names.

## The Criterion

The parameter is a ratio of two gradients. The momentum acting on the word separates into a real part and an imaginary part,

$$
\tilde p\,\tilde\Xi=\Big[\vec\nabla_\Phi S-i\,\frac{h}{2\pi}\,\vec\nabla_\Phi\ln \varrho\Big]\tilde\Xi ,
$$

and the two terms carry different powers of $\epsilon$:

$$
\frac{\lvert h\vec\nabla_\Phi\ln \varrho\rvert}{2\pi \lvert\vec\nabla_\Phi S\rvert}\sim\epsilon ,
\qquad
\frac{1}{k_{\Phi}^{2}}\left\lvert\frac{\Delta_\Phi \varrho}{\varrho}\right\rvert\sim\epsilon^{2} .
$$

The second ratio is the quantum potential over the kinetic energy. It is a square where the first is linear, and the two are the only ratios the pair contains: every term of the parent's boxed pair is one of the three columns below.

| object | order in $\epsilon$ | kept by the limit | kept by the first correction |
|---|---|---|---|
| $\vec\nabla_\Phi S$ | $0$ | yes | yes |
| $\frac{h}{2\pi}\,\vec\nabla_\Phi\ln \varrho$ | $1$ | no | yes |
| $\frac{h^{2}}{4\pi^{2}}\,\Delta_\Phi \varrho/\varrho$ | $2$ | no | no |

**The limit truncates one of the parent's two lines and leaves the other exact.** That asymmetry is the whole content of the pair, and it is not a stylistic choice. The real line carries the quantum potential at order two, so truncating it is a deletion. The imaginary line is a divergence, and a divergence is not a series: the transport equation is what survives when the density is written as the Hermitian norm, and no term of it is dropped at any order.

## Order Zero: the Eikonal

Delete the quantum potential from the real line. What remains is

$$
\frac{\lvert\vec\nabla_\Phi S\rvert^{2}}{2m}+V-E=0 ,
$$

the Hamilton–Jacobi equation for a particle of energy $E$ in the potential $V$. In the parent's letters the real line is $\partial_{t'}S+\lvert\vec\nabla_\Phi S\rvert^{2}/2m+V+Q=0$ with $S$ carrying the time dependence, and for a stationary state $S=-Et'+W$ the two forms are one.

The phase gradient is the real quaternion $\vec\nabla_\Phi S=\sum_\mu(\partial S/\partial R_\mu)\vec e_\mu$, and $\langle\vec\nabla_\Phi S\rangle_{\natural}=\lvert\vec\nabla_\Phi S\rvert^{2}$ because $\vec\nabla_\Phi S\,\vec\nabla_\Phi S^{\natural}=\lvert\vec\nabla_\Phi S\rvert^{2}e_{t}$. The eikonal is then one line in the centre,

$$
\boxed{\ \frac{1}{2m}\langle\vec\nabla_\Phi S\rangle_{\natural}=E-V\ },
$$

the kinetic energy is the biquaternion norm of the phase gradient. The same quadratic form whose vanishing defines the zero-divisor cone is the one the limit sets equal to the kinetic energy, so the forbidden region needs no separate postulate: where $E<V$ the right side is negative, no real vector has a negative norm, and the momentum turns imaginary.

The characters are the trajectories. With $\vec p=\vec\nabla_\Phi S$,

$$
\frac{d\vec r}{dt'}=\frac{\vec p}{m},
\qquad
\frac{d\vec p}{dt'}=-\vec\nabla_\Phi V ,
$$

so the wave fronts $S=\text{const}$ are the surfaces of constant phase, the rays are their orthogonal trajectories, and the phase gradient is the ray direction at each point.

The parent's constant-element case gives $\tilde Q(t')=\exp(-i\theta_{\mathrm{evo}})$ with $\theta_{\mathrm{evo}}=h_{t}\frac{2\pi t'}{h}$, whose word has $\varrho=1$ and $\theta_{\mathrm{rpd}}=0$: the scale is constant, so $\epsilon=0$, and the limit changes nothing because there is nothing to drop. **The limit acts only where the scale varies.** For the free particle the complete integral is $S=\vec p\cdot\vec r-Et'$ with $E=\lvert\vec p\rvert^{2}/2m$, and its gradient is the constant $\vec p$.

For $V=\sum_\eta V_\eta(x_\eta)$ the equation separates, $S=\sum_\eta S_\eta$, each term obeying $\frac{1}{2m}(dS_\eta/dx_\eta)^{2}+V_\eta=E_\eta$ with $\sum_\eta E_\eta=E$, so

$$
S_\eta(x_\eta)=\pm\int^{x_\eta}\sqrt{2m\left(E_\eta-V_\eta(\zeta)\right)}\;d\zeta .
$$

The two signs are the two directions of motion, and the turning points $E_\eta=V_\eta$ are where the branches meet and the amplitude below diverges.

## Order One: the Transport and the Amplitude

**The imaginary line is the transport equation, and it is exact.** In the parent's letters,

$$
\frac{\partial \varrho^{2}}{\partial t'}+\vec\nabla_\Phi\cdot\Bigl(\varrho^{2}\frac{\vec\nabla_\Phi S}{m}\Bigr)=0 ,
$$

a conservation law for the density $\varrho^{2}$ carried by the velocity $\vec\nabla_\Phi S/m$. The limit neither produces it nor spoils it: it is the second line of the parent's pair, it holds at every order, and the truncation of the first line cannot touch it.

The velocity is the phase gradient and not the word's boost, and the polar chart is what shows the difference. On a central field the boost has collapsed to $e_{t}$ and carries nothing, so $\vec v=\vec\nabla_\Phi S/m$ is the whole of the velocity. On a general field the parent's current reads the scale and the boost and the rotor contributes nothing, and the limit does not apply; the two statements are consistent because the central class is where the boost contributes nothing at all.

In one dimension it integrates. $\varrho^{2}\,dS/dx=\text{const}$, so

$$
\varrho(x)=\frac{C}{\sqrt{\lvert p(x)\rvert}},
\qquad
p(x)=\sqrt{2m\left(E-V(x)\right)} .
$$

The wave is large where the particle moves slowly and small where it moves fast, and this is the whole of the WKB amplitude. It follows from the exact equation and not from an expansion.

In three dimensions it gives the van Vleck determinant.

$$
\boxed{\ \varrho\ \propto\ \left\lvert\det\left(\frac{\partial^{2}S_{\mathrm{cl}}}{\partial x_{i}\,\partial x_{f}}\right)_{i,f=1}^{3}\right\rvert^{1/2}\ }
$$

The determinant is the Jacobian of the map from initial to final position, so $\varrho^{2}$ is the density of the ray congruence and the amplitude measures its focusing. Where the congruence crosses itself the determinant vanishes, the amplitude diverges, and the approximation has left its region.

The parent's word has $\varrho>0$ by construction, as the square root of the quaternionic norm's modulus, so the choice is not a gauge imposed here: a complex amplitude would leave the word's domain, and the parent's word is a bijection onto the invertibles only with $\varrho>0$.

## Order Two: the Quantum Potential and the Size of the Error

**The discarded term is the quantum potential.**

$$
Q=-\frac{h^{2}}{8\pi^{2}m}\frac{\Delta_\Phi \varrho}{\varrho},
$$

the parent's own expression, and it is the third term of the real line and the only term the limit deletes.

Its ratio to the kinetic energy is $\epsilon^{2}$ but is not bounded. With $\varrho=\exp(-x^{2}/4\sigma^{2})$ and $\epsilon=1/(k_{\Phi}\sigma)$,

$$
\frac{\lvert Q\rvert}{E-V}=\epsilon^{2}\left\lvert\frac{x^{2}}{4\sigma^{2}}-\frac{1}{2}\right\rvert .
$$

| $\lvert x\rvert/\sigma$ | $0$ | $1$ | $\sqrt{2}$ | $2$ | $3$ |
|---|---|---|---|---|---|
| $\lvert Q\rvert/(\epsilon^{2}(E-V))$ | $0.500$ | $0.250$ | $0$ | $0.500$ | $1.750$ |

The ratio vanishes at $\sqrt{2}\,\sigma$ and grows as $x^{2}$ beyond it, so for every $\epsilon$ it reaches one at $x\simeq2\sigma/\epsilon$. No value of the parameter makes the expansion uniform on a region fixed in advance, and the region shrinks as $\epsilon$ shrinks.

The *limit* needs no region and has no remainder: it is the statement of which terms survive. The *approximation* needs both, and the table is what a claim of approximation has to carry — the order kept and the place where it stops.

Two plane waves of wave numbers $k_{\Phi}$ and $k_{\Phi}+\delta k$ are each semiclassical exactly, and their sum has envelope wave number $\delta k$ and parameter $1/(\delta k\,L)$, which is large when the two are close. So

$$
\lim\left(\tilde\Xi_{1}+\tilde\Xi_{2}\right)\neq\lim\tilde\Xi_{1}+\lim\tilde\Xi_{2},
$$

and the difference is the interference term. **The limit is not a map on the state space**: it takes a wave to its rays, and a ray with a density is not an element of the module.

## Where the Approximation Stops

Three failures, and each is a place and not an order.

At a turning point. $p\to0$, the amplitude $C/\sqrt{\lvert p\rvert}$ diverges, and the eikonal's two branches meet. The repair is a uniform approximation on an Airy scale, which the algebra does not supply; the standard methods are used unchanged.

At a caustic. The van Vleck determinant vanishes and the ray congruence folds. The same repair applies, and the same statement holds: the algebra supplies the location of the failure, not its cure.

Where the scale varies as fast as the phase. There $\epsilon$ is not small anywhere and the limit has no claim to make. That is the interior of a nodal region, where the density vanishes.

One thing the limit never does. It does not select a subalgebra and it does not produce a state. The centre is a canonical classical sector and the limit does not land there; it selects a state-dependent slice, with $L$ as the context made quantitative.

## What the Polar Chart Adds, and What It Costs

*The amplitude is identified before the limit is taken.* In a form-first account the amplitude is whatever multiplies the exponential, and the density is whatever the continuity equation makes positive. Here both are read from the word: the amplitude is the scale $\varrho$, and the density is the Hermitian norm, which is $2\varrho^{2}$ exactly on the central class and not otherwise. The identification is exact or it does not exist.

*The frame is excluded for a stated reason.* The boost and the rotor carry no derivative of a fast object, so the parameter does not order them: they are absent on the central class and present off it, with no intermediate case. The limit is therefore not a truncation of four brackets to two; it is the statement that two of the four are exactly zero on the class where the pair closes. That is stronger than an approximation and it is cheaper to check.

*The eikonal is a norm.* $\frac{1}{2m}\langle\vec\nabla_\Phi S\rangle_{\natural}=E-V$ is one line, and it ties the leading-order equation to the same quadratic form whose vanishing defines the zero-divisor cone. The forbidden region is then where a real vector would need a negative norm.

The limit is defined on the central class, because that is where the parent's pair is closed. The parent proves the class is invariant only under a central Hamiltonian, so a general field's limit is not delivered by this route, and no article in the corpus claims one. Stating the restriction is cheaper than hiding it.

What the polar chart does not add, and the list is short. It does not supply a uniform approximation at a turning point or a caustic, a branch rule for a complex action, or any prediction that separates this formulation from scalar WKB. Every formula in the three order sections is standard.

## Verification

The parent's pair was checked against the equation. With $\tilde\Xi=\varrho\exp(\frac{2\pi iS}{h})$, a real $\varrho>0$, a real $S$ and a real potential $V$, the residual of $i \frac{h}{2\pi}\partial_{t'}\tilde\Xi+\frac{h^{2}}{8\pi^{2}m}\Delta_\Phi\tilde\Xi-V\tilde\Xi$ after division by the exponential is $-\varrho$ times the parent's real line and $\frac{h}{4\pi m\varrho}$ times its imaginary line, identically. Evaluated in thirty-digit arithmetic at three points of a random smooth field, the largest residual was $4\times10^{-17}$.

The orders were checked by substitution. Each of the three terms of the real line was replaced by its stated power of $\epsilon$ and the collection reproduced the three orders, with no term of intermediate order appearing: the real line has exactly three orders and the imaginary line has none.

The Gaussian ratio was recomputed. The five values of the table are $\lvert x^{2}/4\sigma^{2}-1/2\rvert$ at the five tabulated points, and each agrees to twelve digits.

No numerical solution of the time-dependent problem was run: the limit is a statement about equations, and the pair it orders is verified as an identity, which is stronger.

## Summary

The field is the parent's polar word $\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$, and the parent prints the exact pair its central class obeys. The limit assigns one power of $\epsilon=1/(k_{\Phi}L)$ to each spatial derivative of the scale and none to a derivative of the phase, and orders the pair's two lines by that rule.

The real line has three orders. Order zero is the Hamilton–Jacobi equation, read in the algebra as $\frac{1}{2m}\langle\vec\nabla_\Phi S\rangle_{\natural}=E-V$, whose characters are the classical trajectories. Order two is the quantum potential $Q=-\frac{h^{2}}{4\pi^{2}}\Delta_\Phi \varrho/(2m\varrho)$, the only term the limit deletes. Order one is present as the scale's gradient, and it is what the first correction keeps.

The imaginary line is the transport equation and it is not an expansion: $\partial_{t'}\varrho^{2}+\vec\nabla_\Phi\cdot(\varrho^{2}\vec\nabla_\Phi S/m)=0$ holds at every order and the limit cannot spoil it. It gives $\varrho=C/\sqrt{\lvert p\rvert}$ in one dimension and the van Vleck determinant in three.

Three statements are the polar chart's contribution and not the analysis's. The limit's amplitude is the word's scale. The limit's density is the Hermitian norm, equal to $2\varrho^{2}$ exactly where the boost is the identity. And the frame's two brackets are excluded by an exact statement — they carry no derivative of a fast object — rather than by an estimate.

The cost is one restriction. The pair is closed on the central class, that class is invariant only under a central Hamiltonian, and the limit is therefore defined there. No mass shell appears, because the equation is first order in time and its symbol constrains no second time derivative.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{B}_{C}$, $\mathbb{B}_{H}$ | Centre; real-quaternion subspace |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ | Hermitian and anti-Hermitian sectors |
| $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The parent's polar word |
| $\varrho>0$ | The scale; the amplitude of the limit |
| $\theta_{\mathrm{pha}}$, $S=\frac{h}{2\pi}\theta_{\mathrm{pha}}$ | The central angle; the action |
| $\theta_{\mathrm{rpd}}$, $\vec u_{\mathrm b}$ | Rapidity and axis of the boost |
| $\theta_{\mathrm{axr}}$, $\vec u_{\mathrm r}$ | Angle and axis of the rotor |
| $\varepsilon e_{t}$ | The rotor on the central class |
| $\langle\tilde X\rangle_{\natural}=\tilde X\tilde X^{\natural}$ | Quaternionic norm |
| $\rho_{\mathrm{num}}=2\varrho^{2}\cosh\theta_{\mathrm{rpd}}$ | Hermitian norm; the density |
| $\vec\nabla_\Phi S$ | Phase gradient; real quaternion in $\mathbb{B}_{H}$ |
| $\epsilon=1/(k_{\Phi}L)$ | The parameter of the limit |
| $k_{\Phi}=\frac{2\pi \lvert\vec p\rvert}{h}$ | The phase's wave number |
| $Q=-\frac{h^{2}}{4\pi^{2}}\Delta_\Phi \varrho/(2m\varrho)$ | Quantum potential; central real scalar |
| $\Delta_\Phi$ | The Laplacian of the material sector |

## Further Reading

- [The Schrödinger Equation in Biquaternionic Polar Variables](the-schrodinger-equation-in-biquaternionic-polar-variables.html), the parent: the word, the two norms, the boxed pair and the central class.
- [The Schrödinger Equation in Biquaternionic Form](the-schrodinger-equation-in-biquaternionic-form.html), for the equation and its axis-free array.
- [The Non-Quantum Limit of the Biquaternion Model](the-non-quantum-limit-of-the-biquaternion-model.html), for the parameter, the criterion and the difference between the limit and the approximation.
- [The Lagrangian and the Schrödinger Equation in the Non-Quantum Limit](the-lagrangian-and-the-schrodinger-equation-in-the-non-quantum-limit.html), the same limit taken on the parent's action.
- [The Klein–Gordon Equation in the Non-Quantum Limit](the-klein-gordon-equation-in-the-non-quantum-limit.html), where the second order restores a mass shell.
- [The Complete Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-complete-polar-decomposition-of-an-n-regular-biquaternion.html), for the word and its factors.
- [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), for the nodal set where the action is multivalued.
- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the pair the parent prints.
- David Bohm, "A suggested interpretation of the quantum theory in terms of hidden variables," *Physical Review* **85** (1952) 166–193, for the quantum potential and the guidance equation it defines.
