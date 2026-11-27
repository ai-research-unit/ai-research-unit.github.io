# __The Coupled Schrödinger Equation in Biquaternionic Polar Variables__

## Introduction

*The Schrödinger Equation in Biquaternionic Polar Variables* writes the field as a word,

$$
\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,b}\,u_r,
\qquad
\varrho>0,\quad \theta_{\mathrm{pha}}\in\Big(-\frac{\pi}{2},\frac{\pi}{2}\Big],\quad \theta_{\mathrm{rpd}}\ge 0,\quad \theta_{\mathrm{axr}}\in[0,2\pi],
$$

with $\tilde U_{\Psi,b}=\exp(i\theta_{\mathrm{rpd}}\,\vec u_b)$ the Hermitian boost along the unit real vector $\vec u_b$ and $u_r$ the rotor about the unit real vector $\vec u_r$. The word is a bijection from the eight parameters onto the $N$-regular set, so the parameters are coordinates, and the free equation reads on them as a flow: the scale and the rapidity frozen, the phase advancing at minus the mean eigenvalue, every carried direction precessing at the gap.

**The endpoint $2\pi$.** At $\theta_{\mathrm{axr}}=2\pi$ the rotor is $-e_t$, so the angle's range is closed at that point. Without the endpoint the word misses every element whose rotor factor is $-e_t$, the negative real axis $-\varrho e_t$ among them.

This article couples the same field to the electromagnetic connection and asks what the word does with it. The equation is the element form's,

$$
i \frac{h}{2\pi}\,D_t\tilde\Xi=\frac{1}{2m}\sum_{\imath\in\{x,y,z\}}\big(-i \frac{h}{2\pi}\,D_{\imath}\big)^{2}\tilde\Xi,
\qquad
D_t=\partial_{t'}-\frac{2\pi i\,ϙ}{h}\omicron_{\mathrm{pot}},
\qquad
D_{\imath}=\partial_{\imath}+\frac{2\pi i\,ϙ}{h}A_{\imath},
$$

with $\tilde A_\Phi=i(\omicron_{\mathrm{pot}}/c)e_t+\vec A$ the material connection, and the whole of the article is the translation of that one operator into the chart.

**Three findings, and the first is the article's structural point.**

*First, the connection is a central-imaginary number in every slot, so it joins the phase bracket and nothing else.* The free article decomposes $\tilde\Xi^{-1}\partial_{t'}\tilde\Xi$ into four objects of four algebraic types — a real scalar, a central imaginary, a Hermitian element, a real vector — and the equation reads each of them separately. The covariant bracket is the free one plus $-\frac{2\pi iϙ}{h}\omicron_{\mathrm{pot}}$ in the temporal slot and $+\frac{2\pi iϙ}{h}A_{\imath}$ in each spatial slot. Every one of those additions is a central imaginary number, so each joins the second bracket; the scale, the boost and the rotor cannot receive anything. The consequence is exact and it is the article's sharpest statement: the connection moves the phase and only the phase, so in the central field the quantum potential is untouched by it (§*The Covariant Logarithmic Derivative*).

*Second, in the constant setting the coupling is a shift of the two eigenvalues and of the axis.* The free flow's numbers are the mean $h_t$ and the vector $\vec h_\Psi$; the coupled flow's are $h_t-ϙ\omicron_{\mathrm{pot}}$ and $\vec h_\Psi-q\vec A$. The scale and the rapidity are still frozen, the phase still advances at minus the mean of the shifted pair, and the carried directions still precess at the gap of the shifted pair. The kinetic momentum is the shifted vector, the canonical momentum the unshifted one, and the difference between them is the vector potential (§*The General Element in the Constant Setting*).

*Third, in the operator setting the word reproduces the covariant Madelung pair, and the connection enters only where the pair can carry it.* The continuity equation gets the kinetic momentum in place of the gradient, the Hamilton–Jacobi equation gets the kinetic energy in place of the kinetic term and $-ϙ\omicron_{\mathrm{pot}}$ in place of nothing, and the quantum potential is written with the ordinary gradient of the scale because the connection cannot touch it. The plate is standard quantum fluid physics; the biquaternionic form of it is what the article supplies (§*The Central Field in the Operator Setting*).

**What is not claimed.** No new prediction and no new solution: the equation is the element form's and the flow is its consequence. The polar chart does not decouple the four brackets from the parameters, does not simplify the equation, and does not supply a second constant of motion. What it supplies is the reading: which bracket the connection joins, which coordinate the symmetry group translates, and which invariants the coupling leaves alone.

**Conventions.** The algebra, the pairing, the sectors, the two settings and the parameter ranges are the free polar article's and are not restated. Time is $t'$, so that $i \frac{h}{2\pi}\partial_{t'}=i \frac{h}{2\pi} c\,\partial_{r'_t}$ and the element form's $r'_t=c\,t'$ is the parent's material length; the polar article uses $t'$ throughout, and so does this one. The connection is $\tilde A_\Phi=i(\omicron_{\mathrm{pot}}/c)e_t+\vec A$ with $\omicron_{\mathrm{pot}}=c\,a'_t$ and $\vec A$ real, and the coupling is $ϙ$, which is minus the electric charge of the older convention: the mechanical momentum is $\vec\pi=-i \frac{h}{2\pi}\nabla-q\vec A$ and the potential energy enters as $-ϙ\omicron_{\mathrm{pot}}$. The density is $n=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)=\rho_{\mathrm{num}}/2$, and the word gives $n=\varrho^{2}\cosh\theta_{\mathrm{rpd}}$.

## The Covariant Logarithmic Derivative

**The object.** The free article's bracket is $\mathcal A_{\imath}=\tilde\Xi^{-1}\partial_{\imath}\tilde\Xi$ in the spatial slots and $\mathcal A_t=\tilde\Xi^{-1}\partial_{t'}\tilde\Xi$ in the temporal one. The covariant version is the same object with the connection added inside the derivative,

$$
\mathcal A^{\mathrm{gco}}_t=\tilde\Xi^{-1}D_t\tilde\Xi=\mathcal A_t-\frac{2\pi i\,ϙ}{h}\omicron_{\mathrm{pot}},
\qquad
\mathcal A^{\mathrm{gco}}_{\imath}=\tilde\Xi^{-1}D_{\imath}\tilde\Xi=\mathcal A_{\imath}+\frac{2\pi i\,ϙ}{h}A_{\imath},
$$

and the simplification is the whole of it: in each slot the connection is a scalar multiple of the identity — $A_t=i\omicron_{\mathrm{pot}}/c$ in the temporal slot and the real $A_{\imath}$ in the spatial ones — so it commutes with the field, needs no conjugation, and no reordering. There is no $\natural$ in this section and no second carrier.

**Which bracket receives it.** The four brackets of the free article are the four algebraic types into which a general element splits: a real scalar, a central imaginary, a Hermitian element and a real vector. The connection's addition in each slot is $i$ times a real number, because $\omicron_{\mathrm{pot}}$ and $A_{\imath}$ are real; that is a central imaginary number, and it therefore lies in the second bracket and in no other. The scale bracket is a real scalar and receives nothing; the boost bracket is Hermitian and receives nothing; the rotor bracket is a real vector and receives nothing. **The connection reaches the phase and only the phase.**

**One spelling difference from the second-order companion.** The coupled Klein–Gordon article records that the connection's temporal addition is *real* and joins the scale bracket. That is the same statement as this one: its temporal derivative is $\partial/\partial R_t=-i\partial_{t'}$, and multiplication by $-i$ exchanges the real and the imaginary part, so its real addition to the $R_t$ bracket is this article's imaginary addition to the $t'$ bracket. The invariant content of both spellings is physical and identical: the potential shifts the phase's rate and leaves the density's rate alone.

**What that means in the chart.** For a central field the statement is one line and it is worth writing,

$$
\mathcal A^{\mathrm{gco}}_{\imath}=\partial_{\imath}\ln \varrho+i\Big(\partial_{\imath}\theta_{\mathrm{pha}}+\frac{2\pi ϙ}{h}A_{\imath}\Big),
\qquad
\mathcal A^{\mathrm{gco}}_t=\partial_{t'}\ln \varrho+i\Big(\partial_{t'}\theta_{\mathrm{pha}}-\frac{2\pi ϙ}{h}\omicron_{\mathrm{pot}}\Big),
$$

so the scale gradient is untouched and the phase gradients are translated: by $+\frac{2\pi ϙ}{h}\vec A$ in space and by $-\frac{2\pi ϙ}{h}\omicron_{\mathrm{pot}}$ in time. Multiplying by $\frac{h}{2\pi}$ gives the two invariants of the coupled theory,

$$
\vec\pi=\frac{h}{2\pi}\nabla\theta_{\mathrm{pha}}-q\vec A,
\qquad
\mathcal E=-\frac{h}{2\pi}\,\partial_{t'}\theta_{\mathrm{pha}}+ϙ\omicron_{\mathrm{pot}},
$$

which are the kinetic momentum and the kinetic energy. Both are invariant under the local transformation of §*The Local Transformation Read on the Word*, term by term: the phase gradient shifts by $+\frac{2\pi ϙ}{h}\vec\nabla_\Phi\Gamma$ and $\vec A$ by $-\vec\nabla_\Phi\Gamma$; the phase rate shifts by $-\frac{2\pi ϙ}{h}\partial_{t'}\Gamma$ and $\omicron_{\mathrm{pot}}$ by $+\partial_{t'}\Gamma$.

**The same statement for the general element, and its limit.** For a general element the bracket's central-imaginary part carries the phase rate and the boost's contribution, and the connection adds to the sum and cannot tell the two apart. That is not a defect: it is the exact statement that the potential shifts the phase and does not touch the rapidity, because the rapidity is the modulus of the Hermitian part and the added number is not Hermitian. The constant setting makes the same point in the flow's own numbers, and it is where the article turns next.

## The General Element in the Constant Setting

**The equation.** Let $\tilde H_\Psi=h_te_t+i\vec h_\Psi$ be constant and let the connection be constant. The coupled equation is the free equation with the element shifted,

$$
i \frac{h}{2\pi}\,\partial_{t'}\tilde\Xi=\tilde H^{\mathrm{gco}}_\Psi\,\tilde\Xi,
\qquad
\tilde H^{\mathrm{gco}}_\Psi=\tilde H_\Psi-ϙ\omicron_{\mathrm{pot}}\,e_t+i\,ϙ\vec A
=\big(h_t-ϙ\omicron_{\mathrm{pot}}\big)e_t+i\big(\vec h_\Psi-q\vec A\big).
$$

The shifted element is Hermitian, of the same form as the unshifted one, with two real numbers changed. That is the whole of minimal coupling in a setting with no derivatives, and it is why the article can state the coupled flow without a new derivation.

**The flow.** Every statement of the free polar article applies to $\tilde H^{\mathrm{gco}}_\Psi$ with the letters changed:

- the scale $\varrho$ and the rapidity $\theta_{\mathrm{rpd}}$ are constant, because the free article's flow freezes them and the shift changes no structural property of the element;
- the phase advances at minus the mean of the shifted pair,
  $$\partial_{t'}\theta_{\mathrm{pha}}=-\frac{2\pi h_t-ϙ\omicron_{\mathrm{pot}}}{h},$$
  so a constant potential translates the frequency by $\frac{2\pi ϙ\omicron_{\mathrm{pot}}}{h}$ and does nothing else;
- every carried direction precesses at the shifted gap,
  $$|\vec\Omega|=\frac{2\pi 2\,|\vec h_\Psi-q\vec A|}{h},$$
  so a constant vector potential translates the axis about which the precession happens and changes its rate;
- the density $n=\varrho^{2}\cosh\theta_{\mathrm{rpd}}$ is constant, and so is the charge density $ϙn$.

**The two momenta.** The unshifted $\vec h_\Psi$ is the canonical momentum and the shifted $\vec h_\Psi-q\vec A$ is the kinetic momentum, which is the vector that appears in the precession rate. The relation is the spatial half of the dictionary; the temporal half is $h_t$ and $h_t-ϙ\omicron_{\mathrm{pot}}$, and the two halves carry opposite signs for the metric reason the element-form companion states. In the free case $\vec h_\Psi$ is the field's momentum and $h_t$ its energy; after the coupling the pair $(\vec h_\Psi-q\vec A,\,h_t-ϙ\omicron_{\mathrm{pot}})$ is the mechanical pair, and the pair $(\vec h_\Psi,h_t)$ is what the canonical equations of the variational companion conjugate.

**What the shift cannot do.** It cannot change the rapidity, and therefore it cannot change the density's relation to $\varrho$; it cannot change the rotor's type, so a carried direction stays carried; and it cannot turn a real-vector bracket into a Hermitian one. In the flow's terms: a constant potential displaces the spectrum rigidly and rotates the rotor's axis, and it leaves the two-scale structure — one rate for the phase, one for each carried direction — exactly as it was.

**One check of the sign.** Take $\vec A=0$ and $\omicron_{\mathrm{pot}}$ constant and positive, and let the field be central, $\tilde\Xi=\varrho e^{i\theta_{\mathrm{pha}}}e_t$. The equation is $i \frac{h}{2\pi}\partial_{t'}\tilde\Xi=(h_t-ϙ\omicron_{\mathrm{pot}})\tilde\Xi$, so $\partial_{t'}\theta_{\mathrm{pha}}=-(h_t-ϙ\omicron_{\mathrm{pot}})\frac{2\pi}{h}$. With $ϙ$ the negative of the electric charge, this is the standard statement that a positive potential lowers the frequency of a positive charge by $\frac{2\pi q\omicron_{\mathrm{pot}}}{h}$ and raises that of a negative one; the sign is the coupling's and the algebra does not choose it.

## The Central Field in the Operator Setting

**The word collapses.** With $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\epsilon\,e_t$, where $\epsilon=\pm1$ is the branch, the boost is trivial and the rotor is trivial, and the three surviving parameters are the scale, the phase and the sign. The equation is now the operator setting's, $\hat H=-\frac{h^{2}}{4\pi^{2}}\Delta_\Phi/2m+V$ with the connection in it, and the article writes

$$
\hat H^{\mathrm{gco}}=\frac{\tilde{\vec\pi}^{\,2}}{2m}-ϙ\omicron_{\mathrm{pot}}+\hat V,
\qquad
\tilde{\vec\pi}=-i \frac{h}{2\pi}\nabla-q\vec A .
$$

**The continuity equation.** Varying the phase gives the covariant continuity equation,

$$
\partial_{t'}\big(\varrho^{2}\big)+\vec\nabla_\Phi\cdot\Big(\varrho^{2}\,\frac{\vec\nabla_\Phi S-q\vec A}{m}\Big)=0,
\qquad
S=\frac{h}{2\pi}\,\theta_{\mathrm{pha}},
$$

so the current is $\varrho^{2}(\vec\nabla_\Phi S-q\vec A)/m=\varrho^{2}\vec\pi/m$, which is the free current with the kinetic momentum in place of the gradient. Nothing else changes: the density is $\varrho^{2}$, the velocity is $\vec\pi/m$, and the equation is the statement that the density is transported by the kinetic velocity and not by the canonical one.

**The Hamilton–Jacobi equation.** Collecting the real part of the equation for $\varrho$ gives

$$
\partial_{t'}S+\frac{|\vec\nabla_\Phi S-q\vec A|^{2}}{2m}-ϙ\omicron_{\mathrm{pot}}+Q=0,
\qquad
Q=-\frac{hc}{8\pi^{2}\nu_m}\frac{\Delta_\Phi \varrho}{\varrho},
$$

the quantum Hamilton–Jacobi equation of the coupled field. The three changes from the free equation are the kinetic momentum in the kinetic term, the potential energy, and nothing else. **The quantum potential is unchanged**, and the reason is the article's first finding read on the scale: $Q$ is built from $\varrho$ and its ordinary Laplacian, and the connection cannot enter the scale gradient because it is central imaginary.

**The kinetic energy.** The combination

$$
\mathcal E=-\frac{h}{2\pi}\,\partial_{t'}\theta_{\mathrm{pha}}+ϙ\omicron_{\mathrm{pot}}
$$

is the kinetic energy of the flow, and it is invariant. In terms of the phase and the potential it is the free kinetic energy plus the potential, which is the classical statement that the total energy minus the potential energy is the kinetic one. The local invariance is worth one line: $\theta_{\mathrm{pha}}$ shifts by $+\frac{2\pi ϙ\Gamma}{h}$ and $\omicron_{\mathrm{pot}}$ by $+\partial_{t'}\Gamma$, so the two halves of $\mathcal E$ move in the same direction and by the same amount, and the article records that the phase rate alone is not invariant — only the combination is.

**The vorticity.** The velocity is $\vec v=\vec\pi/m=(\vec\nabla_\Phi S-q\vec A)/m$, and its curl is

$$
\vec\nabla_\Phi\times\vec v=\frac{ϙ}{m}\,\vec B,
$$

because $\vec\nabla_\Phi\times\nabla S$ vanishes identically. So the canonical flow is irrotational — that is the free article's statement, and it is exact — while the kinetic flow is rotational exactly where the magnetic field is, and nowhere else. With $ϙ$ the negative of the electric charge this is $\vec\nabla_\Phi\times\vec v=-(q/m)\vec B$, the standard sign for a positive charge. The same identity is what the flux quantization of §*Flux and Circulation* integrates.

**The two limits of the same word.** In the constant setting the vector potential shifts the rotor's axis, and in the operator setting it enters the phase gradient. The two are one statement: the rotor's axis is the direction of the momentum, and the phase gradient is the momentum's value. What differs is which of them the equation uses, and that depends on whether the operator has spatial derivatives.

## The Local Transformation Read on the Word

**The transformation.** With $\digamma_{\mathrm{cph}}=\exp(\frac{2\pi iϙ\Gamma}{h})$ and $\Gamma$ real, the field becomes $\digamma_{\mathrm{cph}}\tilde\Xi$, and since $\digamma_{\mathrm{cph}}$ is central and commutes with every invertible element, the word's factors transform one at a time:

$$
\varrho\longmapsto \varrho,
\qquad
\theta_{\mathrm{pha}}\longmapsto\theta_{\mathrm{pha}}+\frac{2\pi ϙ}{h}\Gamma,
\qquad
\tilde U_{\Psi,b}\longmapsto\tilde U_{\Psi,b},
\qquad
u_r\longmapsto u_r .
$$

**The symmetry group is the translation of one coordinate.** Seven of the eight parameters are inert under the symmetry group and one is translated, by a function of the spacetime point. That is the polar form of the statement that the symmetry group is the centre's $\mathrm{U}(1)$: on the chart, the centre acts as the additive group of the phase. The element-form companion says the same thing from the other side — the transformation touches the connection and the field's central phase and no other parameter — and the polar statement is the sharper one because it names the coordinate.

**What is invariant.** Everything built from $\vec\nabla_\Phi\theta_{\mathrm{pha}}+\frac{2\pi ϙ}{h}\vec A$, from $\partial_{t'}\theta_{\mathrm{pha}}-\frac{2\pi ϙ}{h}\omicron_{\mathrm{pot}}$, and from the other six parameters. The scale, the rapidity, the two axes, the density, the rapidity's rate and the gap are invariant, and the two combinations of the phase with the connection are invariant. The phase itself is not, and neither is its rate alone.

**The free article's "no redundancy" and what the coupling does to it.** The free polar article records that the free equation fixes the phase's rate and that there is no redundancy to fix: $\theta_{\mathrm{pha}}$ is a physical coordinate whose evolution is determined. The coupling does not contradict that; it splits the statement in two. The *rate* of the phase is still determined, and it is the invariant combination $\mathcal E$ that is determined; the phase itself acquires an arbitrary additive function, and the equation determines only the differences. So a coordinate that was physical becomes a coordinate with a redundant direction, and the direction is exactly the one whose conjugate momentum is the density.

**Why that is consistent with the flow.** The flow's rate statement, $\partial_{t'}\theta_{\mathrm{pha}}=-(h_t-ϙ\omicron_{\mathrm{pot}})\frac{2\pi}{h}$, is invariant when read correctly: $h_t$ is the free coefficient, a property of the free element and not of the potential, while the potential's shift of $\omicron_{\mathrm{pot}}$ is compensated by the field's own phase shift. In the constant setting the phase functions that keep the connection constant are the linear ones, and for those the two changes are constants that cancel.

## Flux and Circulation

**The loop.** Let $\vec B=0$ in a region that is not simply connected and let the field be central there. The phase is single valued on the field, so its gradient integrates to $h n$ around a loop, with $n$ the winding; and the kinetic circulation is

$$
\oint\vec v\cdot d\vec l=\frac{h\,n+ϙ\,\digamma_{\mathrm{flx}}}{m},
\qquad
\digamma_{\mathrm{flx}}=\oint\vec A\cdot d\vec l=\int_{\Sigma}\vec B\cdot d\vec S,
$$

with $\Sigma$ any surface bounded by the loop. With $ϙ$ the negative of the electric charge this is $\big(h n-q\digamma_{\mathrm{flx}}\big)/m$, the standard statement that a magnetic flux shifts every circulation quantum. The derivation is one line from the vorticity of the preceding section, and the physical content — that the vector potential is invisible locally and visible on a loop — is the Aharonov–Bohm statement in the polar chart's letters.

**Where the loop statement lives.** It is a statement about the phase gradient, so it belongs to the operator setting, where a gradient exists. In the constant setting there is no loop and the vector potential acts as the shift of the rotor's axis; the two statements agree on a plane wave, where the rotor's axis and the phase gradient are the same momentum.

**What the loop does not need.** It does not need the connection to be weak, the field to be slow, or the region to be free of the field: it needs only $\vec B=0$ on $\Sigma$. In regions where $\vec B\ne0$ the circulation is not quantized, because the phase's gradient need not be single valued there — the same limitation the nodal-set article records for the free case, and the coupling neither removes nor creates it.

## What the Polar Chart Adds and What It Does Not

**Adds.** The type statement: the connection is central imaginary in every slot, joins the phase bracket, and cannot reach the scale, the boost or the rotor. The coordinate statement: the symmetry group translates $\theta_{\mathrm{pha}}$ and nothing else, and the density is its conjugate momentum. The invariance statement: $\vec\pi$ and $\mathcal E$ are the two invariant combinations, and the quantum potential is untouched because the scale is untouched. The limit statement: the same shift of the two coefficients reads as a frequency shift and an axis shift in the constant setting, and as a kinetic momentum and a potential energy in the operator setting. And the loop statement, which is one line from the vorticity.

**Does not add.** No new solution and no new constant of motion. The free article's frozen scale, frozen rapidity, phase rate and gap survive with shifted numbers and are not multiplied by the coupling. The word does not become a solution method for the coupled equation; it is a chart in which the equation's structure is visible.

**The one thing the coupling changes in kind.** The free chart has no redundant direction: all eight parameters are physical. The coupled chart has one, and it is a direction along which the chart is degenerate — a whole line of parameters, one for each function $\Gamma$, describes the same field and the same connection up to representative. That is the only structural change, and it is the one the variational companion uses.

## Open Questions

**1. The operator setting for the general element.** The article's operator statements are the central field's. For a general element with spatial derivatives — a boost that varies from point to point, a rotor that twists — the covariant bracket's central-imaginary part and the boost bracket both carry gradient information, and the way the connection distributes between them is not examined here.

**2. The global structure of the word.** The word is a bijection on the $N$-regular set, which is contractible in the unit directions but has the phase's range $(-\pi/2,\pi/2]$; whether a phase function with nonzero winding forces a chart that leaves the range, and how the chart must be patched, is not examined here.

**3. The nonlinear case.** The condensate article's Gross–Pitaevskii term is a function of the density alone, and the polar chart writes it as a function of $\varrho$ and $\theta_{\mathrm{rpd}}$; whether the coupled nonlinear flow keeps the scale frozen is a one-line check that is not performed here.

## Summary

The coupled Schrödinger equation in the chart is the free equation with the covariant logarithmic derivative in place of the ordinary one,

$$
\mathcal A^{\mathrm{gco}}_t=\mathcal A_t-\frac{2\pi i\,ϙ}{h}\omicron_{\mathrm{pot}},
\qquad
\mathcal A^{\mathrm{gco}}_{\imath}=\mathcal A_{\imath}+\frac{2\pi i\,ϙ}{h}A_{\imath} .
$$

Each addition is a central imaginary number, so the connection joins the phase bracket and reaches no other: the scale, the rapidity, the boost's axis and the rotor's axis are untouched by it in type, and the symmetry group acts on the chart as the translation of $\theta_{\mathrm{pha}}$ alone.

In the constant setting the coupled element is $\tilde H^{\mathrm{gco}}_\Psi=(h_t-ϙ\omicron_{\mathrm{pot}})e_t+i(\vec h_\Psi-q\vec A)$ and the free flow applies with two numbers shifted: the scale and the rapidity frozen, the phase advancing at $-(h_t-ϙ\omicron_{\mathrm{pot}})\frac{2\pi}{h}$, every carried direction precessing at $2|\vec h_\Psi-q\vec A|\frac{2\pi}{h}$. The unshifted vector is the canonical momentum, the shifted one the kinetic momentum.

In the operator setting, for the central field,

$$
\partial_{t'}\varrho^{2}+\vec\nabla_\Phi\cdot\Big(\varrho^{2}\frac{\vec\nabla_\Phi S-q\vec A}{m}\Big)=0,
\qquad
\partial_{t'}S+\frac{|\vec\nabla_\Phi S-q\vec A|^{2}}{2m}-ϙ\omicron_{\mathrm{pot}}+Q=0,
$$

the covariant Madelung pair, with the quantum potential $Q=-\frac{h^{2}}{4\pi^{2}}\Delta_\Phi \varrho/2m\varrho$ unchanged. The kinetic momentum is invariant, the kinetic energy $-\frac{h}{2\pi}\partial_{t'}\theta_{\mathrm{pha}}+ϙ\omicron_{\mathrm{pot}}$ is invariant, the vorticity is $ϙ\vec B/m$, and the circulation around a loop is $\big(h n+ϙ\digamma_{\mathrm{flx}}\big)/m$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,b}u_r$ | The word; $\tilde U_{\Psi,b}=\exp(i\theta_{\mathrm{rpd}}\vec u_b)$ |
| $\varrho>0$ | The scale |
| $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ | The central phase; the coordinate the symmetry group translates |
| $\theta_{\mathrm{rpd}}\ge0$, $\vec u_b$ | The rapidity and axis of the Hermitian boost |
| $\theta_{\mathrm{axr}}\in[0,2\pi]$, $\vec u_r$ | The angle and axis of the rotor |
| $\mathcal A_{\imath}=\tilde\Xi^{-1}\partial_{\imath}\tilde\Xi$ | The free logarithmic derivative |
| $\mathcal A^{\mathrm{gco}}_{\imath}$ | The covariant one: $\mathcal A_t-\frac{2\pi iϙ}{h}\omicron_{\mathrm{pot}}$ and $\mathcal A_{\imath}+\frac{2\pi iϙ}{h}A_{\imath}$ |
| $ϙ$ | The coupling; minus the electric charge of the older convention |
| $\omicron_{\mathrm{pot}}$, $\vec A$ | The electric potential, $\omicron_{\mathrm{pot}}=c\,a'_t$, and the vector potential |
| $\vec\pi=\frac{h}{2\pi}\nabla\theta_{\mathrm{pha}}-q\vec A$ | The kinetic momentum |
| $\mathcal E=-\frac{h}{2\pi}\partial_{t'}\theta_{\mathrm{pha}}+ϙ\omicron_{\mathrm{pot}}$ | The kinetic energy |
| $S=\frac{h}{2\pi}\theta_{\mathrm{pha}}$ | The action of the flow |
| $Q=-\frac{h^{2}}{4\pi^{2}}\Delta_\Phi \varrho/2m\varrho$ | The quantum potential |
| $n=\varrho^{2}\cosh\theta_{\mathrm{rpd}}$ | The density; $\rho_{\mathrm{num}}=2n$ |
| $h_t$, $\vec h_\Psi$ | The canonical energy and momentum of the constant setting |
| $h_t-ϙ\omicron_{\mathrm{pot}}$, $\vec h_\Psi-q\vec A$ | The kinetic energy and momentum |
| $\digamma_{\mathrm{flx}}$ | The magnetic flux through a loop |
| $\Gamma$, $\digamma_{\mathrm{cph}}=e^{\frac{2\pi iϙ\Gamma}{h}}$ | The phase function and factor |

## Further Reading

- [The Schrödinger Equation in Biquaternionic Polar Variables](the-schrodinger-equation-in-biquaternionic-polar-variables.html), for the word, the four brackets and the free flow that this article shifts.
- [The Coupled Schrödinger Equation in Biquaternionic Form](the-coupled-schrodinger-equation-in-biquaternionic-form.html), the element-form companion, for the equation, the sign bookkeeping of the two slots and the current.
- [The Lagrangian and the Coupled Schrödinger Equation in Polar Variables](the-lagrangian-and-the-coupled-schrodinger-equation-in-polar-variables.html), where the redundant direction of the chart is what the action's symmetry acts on.
- [The Schrödinger Equation in Biquaternionic Form](the-schrodinger-equation-in-biquaternionic-form.html), for the carrier, the two settings and the centrality of $i$.
- [The Minimal Coupling in Biquaternionic Form](the-minimal-coupling-in-biquaternionic-form.html), for the localisation of the centre that this article reads as a translation of $\theta_{\mathrm{pha}}$.
- [The Covariant Derivative and Connection in Biquaternionic Form](the-covariant-derivative-and-connection-in-biquaternionic-form.html), for the operator whose two slots the chart reads.
- [The Coupled Klein–Gordon Equation in Biquaternionic Polar Variables](the-coupled-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the same construction in the second-order case, where the chart's redundant direction is one coordinate among several.
- [The Coupled Dirac Equation in Biquaternionic Polar Variables](the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), for the case in which the connection reaches all four brackets.
- [The Complete Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-complete-polar-decomposition-of-an-n-regular-biquaternion.html), for the word and its bijection.
- [The N-Regular Sector](../articles_maths/the-n-regular-sector.html) and [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the domain the chart covers.
- [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), for the free-case loop statements that §*Flux and Circulation* couples.
- [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html) and [Superfluids and BECs: The Gross–Pitaevskii Equation as the Nonlinear Reverse Map](superfluids-and-becs-the-gross-pitaevskii-equation-as-the-nonlinear-reverse-map.html), for the fluid reading of the pair.
- [Landau Levels in Biquaternionic Form](landau-levels-in-biquaternionic-form.html), for the operator setting with a constant magnetic field.
- E. Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40**, 322 (1927), for the pair in its original form.
- T. Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8**, 143 (1952), for the fluid formulation with the quantum potential.
