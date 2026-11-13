# __The Coupled Schrödinger Equation in Biquaternionic Form__

## Introduction

*The Schrödinger Equation in Biquaternionic Form* writes

$$
i\hbar\,c\,\partial_{r'_t}\tilde\Xi=\tilde H_\Psi\,\tilde\Xi,
\qquad
\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi\in\mathbb{B}_{\Psi},
\qquad
\tilde\Xi\in\mathbb{B},
$$

with $h_t$ and $\vec h_\Psi$ fixed numbers. A fixed Hamiltonian has no room for a background that acts at the position of the field: the equation says what the field does under one operator, and there is nowhere for a second field to enter.

This article puts the electromagnetic connection into that equation. The replacement is one rule, the ordinary derivative becomes a covariant one,

$$
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi,
\qquad
\tilde A_\Phi=i\,\frac{\varphi}{c}\,e_t+\vec A,
$$

with $\varphi$ the electric potential and $\vec A$ the vector potential, both real, and $ϙ$ the coupling the gauge principle introduces. The coupled equation is

$$
\boxed{\;i\hbar\,D_t\tilde\Xi=\frac{1}{2m}\sum_\eta\big(-i\hbar\,D_\eta\big)^{2}\tilde\Xi,\;}
\qquad
D_t=\partial_{t'}-\frac{i\,ϙ}{\hbar}\varphi,
\qquad
D_\eta=\partial_\eta+\frac{i\,ϙ}{\hbar}A_\eta,
$$

which is the standard Schrödinger equation of a charged scalar field, written with the two slots of one covariant derivative.

**Four findings, and the first is the reason the article exists.**

*First, the current closes inside the algebra.* The phase symmetry of the free article survives the coupling, and its Noether current is the derivative bilinear with every derivative covariant. It is real, it is conserved, and it is gauge invariant, and it needs no ingredient from outside $\mathbb{B}$: no adjoint row, no fixed frame unit, no second carrier. This is where the scalar case differs from the spinor case. The coupled Dirac article records that the naive bilinear $i\tilde\Psi\tilde\Psi^{*}$ is gauge invariant and not conserved, and that the conserved object is a triple product with two fixed frame units; the Schrödinger current has neither defect. The contrast is stated once, in §*The Conserved Current*, and cited thereafter.

*Second, the coupling is one central operator in four slots and not four rules.* The connection's coefficients are complex scalars, so they commute with the units, pass through the field, and never reach a rotor. There is no ordering question, no commutator, and no relative sign to choose: the temporal slot and the three spatial slots are one substitution read four times (§*Conventions and the Sign Bookkeeping*).

*Third, gauge covariance is exact for a general element.* The gauge factor is a central unit, so it multiplies the field on either side, and it cancels between the two factors of a bilinear. Every statement of covariance below therefore holds for $\tilde\Xi\in\mathbb{B}$ and not only for a central field; the algebra's non-commutativity is not used and is not needed (§*Gauge Covariance*).

*Fourth, the constant setting's coupling is a shift of two numbers.* When $\tilde H_\Psi$ is a constant element and the connection is constant, the coupled equation is the free equation with

$$
h_t\longmapsto h_t-ϙ\varphi,
\qquad
\vec h_\Psi\longmapsto\vec h_\Psi+ϙ\vec A .
$$

The two shifts are the canonical-to-kinetic dictionary of the older literature, and the polar companion reads them off the word. They are the only content of "minimal coupling" in a setting with no derivatives, and they are stated in §*The Constant Setting*.

**What is not claimed.** No new prediction, no new solution, no new particle. The equation is the standard one of non-relativistic scalar electrodynamics, and its current, its gauge covariance and its non-relativistic limit are the standard ones. What the algebra contributes is that the coupling is one element rather than four rules, that the current is a bilinear of the algebra's own pairing, and that the sign bookkeeping of the two slots is the metric rather than a convention.

**One setting is not the other.** The free article distinguishes a constant-element setting, in which the equation is an ordinary differential equation with the closed-form propagator, from an operator setting, in which it is the ordinary Schrödinger equation. The coupling has a different face in each: a shift of two numbers in the first, a covariant Laplacian in the second. The two are kept apart below, and no result is transferred between them.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; $i$ is the central scalar imaginary, $i^{2}=-e_t$; $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ are the Hermitian and anti-Hermitian fixed subspaces; $*$ is Hermitian conjugation and $\natural$ quaternion conjugation; $\mathrm{Sc}$ is the coefficient of $e_t$ and $\mathrm{Tr}=2\,\mathrm{Sc}$; the density is $n=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ and the free article's $\rho=\mathrm{Tr}(\tilde\Xi^{*}\tilde\Xi)=2n$ is twice it. Time is $t'$ and the parent's material length is $r'_t=c\,t'$, so $\partial/\partial r'_t=c^{-1}\partial/\partial t'$ and $i\hbar c\,\partial_{r'_t}=i\hbar\,\partial_{t'}$; the article uses $t'$ and never mixes the two. The charge $ϙ$ is the gauge principle's coupling constant, a parameter the algebra does not fix; its value and its sign are inserted, as *The Electron in Biquaternionic Form* records.

## Conventions and the Sign Bookkeeping

**The connection.** The material-sector connection of *Maxwell's Equations in the Biquaternionic Formulation* is

$$
\tilde A_\Phi=i\,a'_t\,e_t+\vec A,
\qquad
a'_t\in\mathbb{R},\quad\vec A\in\mathbb{R}^{3},
$$

and the article writes $\varphi:=c\,a'_t$ for the electric potential, so that $ϙ\varphi$ is an energy. This is the same identification the Klein–Gordon companion makes when it writes the four-momentum shift as $\hbar c\,P_t=E+ϙ\varphi$ and $\hbar\vec P=\vec p+ϙ\vec A$; the letters differ and the object does not.

**The two signs, and why they differ.** In the $t'$ language the covariant derivative's slots are

$$
D_t=\partial_{t'}-\frac{i\,ϙ}{\hbar}\varphi,
\qquad
D_\eta=\partial_\eta+\frac{i\,ϙ}{\hbar}A_\eta,
\qquad
\eta\in\{x,y,z\}.
$$

The temporal slot carries a minus where the spatial slots carry a plus. The difference is not a choice of this article and it is not a sign error: $\tilde A_\Phi$'s temporal coefficient is imaginary, $\tilde\nabla_\Phi$'s temporal slot carries the metric $i$ of $\partial/\partial R_t=-i\partial_{r'_t}$, and after the two factors of $i$ are multiplied the temporal connection enters with the opposite sign to the spatial ones. The Klein–Gordon companion's four-momentum shift carries the same sign difference, and its covariant square carries it twice.

**Hermiticity.** Each $D_\eta$ is anti-Hermitian for the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$ when $A_\eta$ is real, since $D_\eta^{\dagger}=-D_\eta$; each $D_\eta^{2}$ is therefore Hermitian, and $(D_\eta\tilde\Xi)^{*}(D_\eta\tilde\Xi)$ is a sum of moduli. The temporal combination is Hermitian in the same sense, $i\hbar D_t=i\hbar\partial_{t'}+ϙ\varphi$, because the second term is a real multiplication. The two facts together are what make the equation's operator Hermitian and its action real.

**What the sign of $ϙ$ means.** With these conventions the mechanical momentum is $\vec\pi=-i\hbar\nabla+ϙ\vec A$ and the potential energy enters as $-ϙ\varphi$. That is the standard equation with the charge $-ϙ$: the older convention writes $\vec\pi=\vec p-q\vec A$ and $+q\varphi$, and the two agree when $ϙ=-q$. The article keeps the companions' sign and does not silently flip it; every formula below is written in terms of $ϙ$, so a reader who prefers the older letter reads $ϙ$ as minus the charge and nothing else changes.

## The Carrier and the Phase Symmetry

**The carrier does not change.** The field remains one element of $\mathbb{B}$. The free article's reason is unchanged and the coupling does not touch it: $\mathbb{B}_{\Psi}$ is not closed under left multiplication by a general Hermitian element, so the carrier must be $\mathbb{B}$. The coupling adds a term that is central in every slot, so left multiplication by it is a scalar multiplication; it neither enlarges nor shrinks the carrier, and the argument for $\mathbb{B}$ is the free one, cited and not repeated.

**The phase symmetry is the centre's.** For a constant real angle $\alpha$,

$$
\tilde\Xi\longmapsto e^{i\alpha}\tilde\Xi,
\qquad
\tilde\Xi^{*}\longmapsto e^{-i\alpha}\tilde\Xi^{*},
$$

leaves the free equation invariant, because $i$ is central and the Hamiltonian is Hermitian. The local form of the same symmetry is what forces the connection, and it is the gauge principle's construction. The free article's Noether charge is

$$
N=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)=n=\frac{\rho}{2},
$$

and its conservation is one line from the equation and its conjugate. The factor of two is the $\mathrm{Tr}=2\,\mathrm{Sc}$ convention and not a normalisation; it is stated once here and not again.

**The local version, and what it costs.** The gauge principle localises the centre's $\mathrm{U}(1)$: the angle becomes a real function $\Gamma$, the field acquires the factor $\lambda=\exp(iϙ\Gamma/\hbar)$, and the connection transforms as

$$
\tilde A_\Phi\longmapsto\tilde A_\Phi-\tilde\nabla_\Phi\Gamma,
\qquad\text{that is}\qquad
\vec A\longmapsto\vec A-\nabla\Gamma,
\qquad
\varphi\longmapsto\varphi+\partial_{t'}\Gamma .
$$

The two transformation laws are one law read in two slots, and they must be kept together: a covariant derivative is covariant for exactly one pair of them. The sign of $\varphi$'s shift is opposite to the sign of $\vec A$'s because $\varphi$ is the temporal component of a covector and $\partial_{t'}$ is the temporal derivative with the metric $i$ absorbed; it is the same fact as the opposite signs in $D_t$ and $D_\eta$.

## The Coupled Equation

**The equation.** Replacing the gradient by the covariant derivative slot by slot gives

$$
i\hbar\,D_t\tilde\Xi=\frac{1}{2m}\sum_\eta\big(-i\hbar\,D_\eta\big)^{2}\tilde\Xi,
$$

which written out is

$$
i\hbar\,\partial_{t'}\tilde\Xi+ϙ\varphi\,\tilde\Xi=\frac{1}{2m}\sum_\eta\Big(-i\hbar\,\partial_\eta+ϙ A_\eta\Big)^{2}\tilde\Xi .
$$

The left side is the covariant time derivative times $i\hbar$; the right side is the kinetic energy written with the mechanical momentum $\vec\pi_\eta=-i\hbar D_\eta=-i\hbar\partial_\eta+ϙA_\eta$. Both sides are built from the same object, and that is the whole of the prescription.

**Why the equation has four copies and no more.** $D_\eta$ has central coefficients, so it commutes with the units; the operator therefore acts on each of the four complex coefficients of $\tilde\Xi$ separately and identically. The coupled theory is four copies of the standard charged scalar field sharing one connection and one charge, with no equation relating the four coefficients. This is the free article's fourfold structure surviving the coupling, and it is the scalar case's answer to the carrier question: the coupling forces no enlargement because it is central.

**The equation is linear, and its operator is Hermitian.** The covariant derivative is complex-linear, so the equation is linear over $\mathbb{C}$ and no term is quadratic in $\tilde\Xi$. Since $D_\eta$ is anti-Hermitian and $D_\eta^{2}$ Hermitian, and since $i\hbar D_t$ is Hermitian, the operator on the right is Hermitian for the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$ and the flow it generates preserves $n$. The one hypothesis is that $\varphi$ and $\vec A$ are real, which is the material-sector condition on the connection and not a further assumption.

**What the equation is not.** It is not the second-order covariant d'Alembertian restricted to a slowly varying field. The Klein–Gordon companion records that the covariant square of the quaternion-conjugate gradient differs from the sum of the covariant squares by a curvature term; nothing of that kind arises here, because the Schrödinger equation is first order in time and the kinetic operator is a sum of squares of first-order operators with no $\natural$ on the outside. The curvature enters the Schrödinger equation only through the commutator of two covariant derivatives, and that commutator is a multiplication by $\frac{iϙ}{\hbar}(\partial_\eta A_\zeta-\partial_\zeta A_\eta)$, which is the field strength and is not a differential operator at all. The commutation of $D_\eta$ and $D_\zeta$ is therefore a magnetic-field statement and never a constraint on the carrier.

## Gauge Covariance

**The first derivative.** With primes marking the transformed objects and $D'_\eta=\partial_\eta+\frac{iϙ}{\hbar}A'_\eta$,

$$
D'_\eta\big(\lambda\tilde\Xi\big)
=\lambda\Big(\partial_\eta+\frac{iϙ}{\hbar}\partial_\eta\Gamma+\frac{iϙ}{\hbar}A_\eta-\frac{iϙ}{\hbar}\partial_\eta\Gamma\Big)\tilde\Xi
=\lambda\,D_\eta\tilde\Xi .
$$

The two gauge gradients cancel because one comes from the derivative of the central unit and the other from the transformation of the connection. Nothing else in the computation can cancel them, which is why the connection's transformation law is forced rather than chosen.

**The second derivative, and the temporal slot.** Applying $D'_\eta$ once more multiplies by $\lambda$ again, since $\lambda$ is central and passes through; and the temporal slot behaves the same way, with $\varphi$'s shift opposite to $\vec A$'s and the sign in $D_t$ opposite to the sign in $D_\eta$. Hence

$$
D'^{2}_\eta(\lambda\tilde\Xi)=\lambda\,D_\eta^{2}\tilde\Xi,
\qquad
D'_t(\lambda\tilde\Xi)=\lambda\,D_t\tilde\Xi,
$$

and the equation is form-invariant:

$$
i\hbar\,D'_t\tilde\Xi'=\frac{1}{2m}\sum_\eta\big(-i\hbar\,D'_\eta\big)^{2}\tilde\Xi'
\qquad\Longleftrightarrow\qquad
i\hbar\,D_t\tilde\Xi=\frac{1}{2m}\sum_\eta\big(-i\hbar\,D_\eta\big)^{2}\tilde\Xi .
$$

**What the covariance does not use.** It does not use the commutativity of the field with anything, the reality of the field, or the central field's collapse. It uses only the centrality of $\lambda$ and of the connection's coefficients, and it therefore holds for every element of $\mathbb{B}$ and for every connection in the material sector. The Dirac companion's covariance proof has the same three lines and one more: there the two members of the pair carry $\natural$, and the conjugate operator carries the conjugate connection. Here there is one equation and one operator, and no second member.

## The Conserved Current

**The current.** The phase symmetry's Noether current of the coupled equation is the free article's bilinear with every derivative covariant,

$$
j_\eta=\frac{\hbar}{2mi}\,\mathrm{Sc}\Big(\tilde\Xi^{*}D_\eta\tilde\Xi-\big(D_\eta\tilde\Xi\big)^{*}\tilde\Xi\Big)
=\frac{\hbar}{m}\,\mathrm{Im}\,\mathrm{Sc}\big(\tilde\Xi^{*}D_\eta\tilde\Xi\big),
$$

and the temporal component is the density,

$$
j_t=n=\mathrm{Sc}\big(\tilde\Xi^{*}\tilde\Xi\big),\qquad
\rho=2n .
$$

The second equality in the first line is an identity: the bracket is the difference of a number and its conjugate, so it is $2i$ times a real number, and dividing by $2i$ leaves the real part. The current is therefore real by construction and not by a check.

**Conservation.** With $\partial_\eta\tilde\Xi^{*}=(D_\eta\tilde\Xi)^{*}+\frac{iϙ}{\hbar}A_\eta\tilde\Xi^{*}$ and $\partial_\eta D_\eta\tilde\Xi=D_\eta^{2}\tilde\Xi-\frac{iϙ}{\hbar}A_\eta D_\eta\tilde\Xi$, the connection's terms cancel in pairs and

$$
\partial_{t'}n+\sum_\eta\partial_\eta j_\eta
=-\frac{1}{m}\,\mathrm{Im}\,\mathrm{Sc}\Big[\tilde\Xi^{*}\Big(\frac{1}{2m}\sum_\eta\big(-i\hbar D_\eta\big)^{2}-\big(i\hbar D_t\big)\Big)\tilde\Xi\Big],
$$

so the right side is the equation's residual contracted with the field and projected on the imaginary part of the scalar part: it vanishes on every solution and the continuity equation is exact off shell. The same identity in the free case is the free article's, with $D_\eta\to\partial_\eta$.

**Gauge invariance.** Under $\tilde\Xi\mapsto\lambda\tilde\Xi$ and $A_\eta\mapsto A_\eta-\partial_\eta\Gamma$, the two factors of the bilinear acquire $\lambda$ and $\lambda^{-1}$, and $\lambda$ is central, so they cancel; and each $D_\eta\tilde\Xi$ is multiplied by $\lambda$, so the two factors acquire $\lambda^{-1}$ and $\lambda$ and cancel again. The current is invariant, and so is the density. This is the property the free current lacks and the coupling supplies: for $ϙ=0$ a local phase shift changes $\vec j$ by a term in $\nabla\Gamma$, and with the connection in place the shift is absorbed.

**The charge current, and the source.** Multiplying by $ϙ$ gives the charge density $\varrho:=ϙ n$ and the charge current $\vec J:=ϙ\vec j$, and the continuity equation is theirs unchanged. That current is the source of the inhomogeneous Maxwell equation, in the form the Maxwell article and the coupled Klein–Gordon companion use,

$$
\tilde\nabla_\Phi\tilde F=-\mu\,\tilde J,
$$

so the conservation of $J$ is the integrability condition of the connection's own equation. The article states the identification and does not re-derive the Maxwell side.

**The contrast with the spinor case, stated once.** The coupled Dirac article records that the product $i\tilde\Psi\tilde\Psi^{*}$ is gauge invariant, of the density's sign, and not conserved: a product of the field with its conjugate carries no fixed unit, so the two chiral parts enter with the same sign, and the current needs them with opposite signs. The repaired object there is a triple product with two fixed frame units, which is the older literature's adjoint row in the algebra's spelling. Nothing of that structure appears here. The Schrödinger current is a derivative bilinear, the equation is first order in time, and the standard conservation argument applies without an adjoint row; the two factors are the field and the field, one differentiated and one not, and the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$ supplies the reality. The scalar case closes and the spinor case does not, and the difference is the order of the equation rather than the algebra.

**What the current does not repair.** The sign of $n$ cannot be negative, because $n=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ is a sum of moduli and the density is a norm, not the temporal slot of a current; a second-order equation's density is the temporal slot of its current and can change sign with the energy, and this one cannot. The coupling does not enter that statement and does not need to.

## The Constant Setting, and the Shift of the Two Coefficients

**The shift.** Let $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ be a constant Hermitian element and let the connection be constant. The coupled equation is then an ordinary differential equation, and it is the free equation with the Hamiltonian replaced by

$$
\tilde H^{\mathrm{gco}}_\Psi=\tilde H_\Psi-ϙ\varphi\,e_t+i\,ϙ\vec A
=\big(h_t-ϙ\varphi\big)e_t+i\big(\vec h_\Psi+ϙ\vec A\big).
$$

The element has the same form as $\tilde H_\Psi$, with two real numbers shifted, so every statement of the free article and of its polar companion applies to it unchanged. The phase runs at $-(h_t-ϙ\varphi)/\hbar$, the rotor's axis is $\vec h_\Psi+ϙ\vec A$, every carried direction turns at $2|\vec h_\Psi+ϙ\vec A|/\hbar$, and the frozen parameters are the field's scale and rapidity as before.

**How to read the two shifts.** $\vec h_\Psi$ is the free field's momentum and $h_t$ its energy; after the coupling the coefficients are the mechanical momentum and the canonical energy, $h_t-ϙ\varphi$. The first is the canonical-to-kinetic dictionary in the spatial slot, the second in the temporal one, and they carry opposite signs for the reason §*Conventions and the Sign Bookkeeping* gives. A constant potential therefore translates every frequency by $ϙ\varphi/\hbar$ and every rotor axis by $ϙ\vec A$, and it resizes nothing: the gap between the two eigenvalues is $2|\vec h_\Psi+ϙ\vec A|$ and depends on the vector potential alone.

**No gauge invariance is lost.** The two shifts are consistent with the gauge transformation, and the check is one line: under $\varphi\mapsto\varphi+\partial_{t'}\Gamma$ the phase rate would appear to change, but the field's phase changes by $ϙ\Gamma/\hbar$ in the same step, and the two changes are equal and opposite. In the constant setting the gauge function must be at most linear in $t'$ for the connection to stay constant, and for a linear one the shift of $\varphi$ is a constant translation of the phase rate — which is exactly the translation the field's own phase supplies.

## The Non-Relativistic Limit of the Coupled Klein–Gordon Equation

**The statement.** The coupled Schrödinger system is the non-relativistic limit of the coupled Klein–Gordon system — scalar electrodynamics — in the same sense in which the free Schrödinger equation is the non-relativistic limit of the free Klein–Gordon equation. The free statement is the free article's open question 4 and this article does not close it either; what the coupling adds is a check that the two limiting procedures agree.

**The two slots must agree.** Write the coupled Klein–Gordon equation in the component form of its companion, $\big(\sum_\mu D_\mu^{2}-k_m^{2}\big)\tilde\Xi=0$, and set $\tilde\Xi=e^{-ik_m r'_t}\tilde\Xi_{\mathrm{nr}}$ with $k_m=mc/\hbar$. The temporal slot then produces a term linear in $k_m$, which is the mass, and the balance of that term against the spatial covariant Laplacian gives

$$
i\hbar\,D_t\tilde\Xi_{\mathrm{nr}}\simeq\frac{1}{2m}\sum_\eta\big(-i\hbar D_\eta\big)^{2}\tilde\Xi_{\mathrm{nr}},
$$

with the same $D_\eta$ and the same $D_t$ as above. The sign check is the one that matters: the temporal slot of the Klein–Gordon equation carries $+\frac{iϙ}{\hbar}A_t$ with $A_t=i\varphi/c$, and after the mass phase is removed it becomes $\partial_{t'}-\frac{iϙ}{\hbar}\varphi$, which is this article's $D_t$. Had the metric sign been dropped, the potential would have entered with the wrong sign in one slot and the limit would not close.

**What the limit does not preserve.** The Klein–Gordon density is the temporal slot of its current and changes sign with the branch; the Schrödinger density is a norm. The limit therefore keeps the positive-frequency branch and discards the other, and the discarded branch is not a small correction — it is a second field. The same remark is the free article's, and the coupling does not alter it.

## What the Coupling Adds and What It Does Not

**Adds.** One equation and one covariant derivative in place of four substitution rules. A current that is real, conserved and gauge invariant, with no adjoint row. A covariance proof that is three lines and holds for a general element. The constant setting's dictionary, $h_t\mapsto h_t-ϙ\varphi$ and $\vec h_\Psi\mapsto\vec h_\Psi+ϙ\vec A$, as the whole of minimal coupling where there are no derivatives. And the closure statement, which is the article's structural result: the scalar case's $U(1)$ current lives inside the algebra.

**Does not add.** No new prediction; the equation is the standard one. No new solution; the coupled constant setting's solution is the free propagator with shifted numbers, and the operator setting's solutions are the standard ones. No enlargement of the carrier; the coupling is central and the four copies are the free four copies.

**The distinction that matters.** In the spinor case the current question is open and the article that settles it has to build an object the algebra does not hand over for free. In the scalar case the object is the derivative bilinear, the algebra hands it over, and the only work is to put the connection in the right places and to keep the two signs apart. That difference is not a difference of skill; it is a difference of order and of carrier.

## Open Questions

**1. The operator setting's domain.** The covariant Laplacian with a general connection is symmetric on the smooth compactly supported fields, but its self-adjoint extensions, and the effect of a singular connection — a flux tube, for instance — on the spectrum and on the domain of the flow, are not examined here. The free article leaves the operator setting's analysis to the hydrogen article; the coupled case has no such companion yet.

**2. A nonlinear coupling.** The Gross–Pitaevskii equation adds a term proportional to $|\tilde\Xi|^{2}\tilde\Xi$, and the reverse Madelung map and the condensate article treat the free nonlinear case. Whether the coupled nonlinear equation's current closes in the same way — the density-dependent term is Hermitian and contributes nothing to the continuity equation — is a one-line check that is not performed here.

**3. The many-field extension.** Four copies share one connection, and the natural next question is whether they couple to one another. The free article leaves the tensor product over $\mathbb{C}$ open; the coupling does not decide it, because a central connection cannot mix coefficients.

## Summary

The coupled Schrödinger equation is

$$
i\hbar\,D_t\tilde\Xi=\frac{1}{2m}\sum_\eta\big(-i\hbar D_\eta\big)^{2}\tilde\Xi,
\qquad
D_t=\partial_{t'}-\frac{i\,ϙ}{\hbar}\varphi,
\qquad
D_\eta=\partial_\eta+\frac{i\,ϙ}{\hbar}A_\eta,
$$

with $\tilde\Xi\in\mathbb{B}$ one general element, $ϙ$ the coupling and $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$ the material connection. The two signs of the two slots differ by the metric, not by a convention, and the mechanical momentum is $\vec\pi=-i\hbar\nabla+ϙ\vec A$.

The field remains one element of $\mathbb{B}$ and the coupling changes nothing about the carrier, because the connection's coefficients are central and left multiplication by them is scalar multiplication. The theory is four copies of the standard charged scalar field sharing one connection.

Gauge covariance is exact and holds for a general element: the central unit cancels between the two factors of every bilinear, and the connection's transformation law is forced by the cancellation of the two gauge gradients.

The current is

$$
j_\eta=\frac{\hbar}{2mi}\,\mathrm{Sc}\Big(\tilde\Xi^{*}D_\eta\tilde\Xi-\big(D_\eta\tilde\Xi\big)^{*}\tilde\Xi\Big),
\qquad
j_t=n=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi),
$$

real, conserved on solutions, and gauge invariant. It closes inside the algebra, with no adjoint row and no fixed frame unit, and that is where the scalar case separates from the spinor one.

In the constant setting the coupling is a shift of two numbers, $\tilde H^{\rm gco}_\Psi=(h_t-ϙ\varphi)e_t+i(\vec h_\Psi+ϙ\vec A)$, and the free flow applies to it unchanged. The coupled Schrödinger system is the non-relativistic limit of the coupled Klein–Gordon system, and the limit closes because the metric sign of the temporal slot is the same sign in both equations.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^{2}=-e_t$ |
| $i$ | Central scalar imaginary |
| $*,\ \natural$ | Hermitian conjugation, quaternion conjugation |
| $\mathrm{Sc},\ \mathrm{Tr}=2\,\mathrm{Sc}$ | Scalar part, trace |
| $t'$, $r'_t=c\,t'$ | The variable of the article and the parent's material time |
| $\tilde\Xi\in\mathbb{B}$ | The field: one general element, eight real components |
| $ϙ$ | The coupling constant; minus the electric charge of the older convention |
| $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$ | The material-sector connection; $\varphi$ and $\vec A$ real |
| $\varphi=c\,a'_t$ | The electric potential, so that $ϙ\varphi$ is an energy |
| $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$ | The covariant derivative |
| $D_t=\partial_{t'}-\frac{iϙ}{\hbar}\varphi$, $D_\eta=\partial_\eta+\frac{iϙ}{\hbar}A_\eta$ | Its slots in the $t'$ language |
| $\vec\pi_\eta=-i\hbar D_\eta=-i\hbar\partial_\eta+ϙA_\eta$ | The mechanical momentum |
| $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ | The free Hermitian Hamiltonian |
| $\tilde H^{\mathrm{gco}}_\Psi=(h_t-ϙ\varphi)e_t+i(\vec h_\Psi+ϙ\vec A)$ | The coupled Hamiltonian of the constant setting |
| $n=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ | The density; $\rho=2n$ is the free article's |
| $j_\eta$, $j_t=n$ | The particle current and its temporal component |
| $\varrho=ϙ n$, $\vec J=ϙ\vec j$ | The charge density and the charge current |
| $\lambda=e^{iϙ\Gamma/\hbar}$ | The gauge factor; $\Gamma$ real |
| $\Gamma$ | The gauge function; $\vec A\mapsto\vec A-\nabla\Gamma$, $\varphi\mapsto\varphi+\partial_{t'}\Gamma$ |

## Further Reading

- [The Schrödinger Equation in Biquaternionic Form](the-schrodinger-equation-in-biquaternionic-form.html), for the free equation, the carrier, the two writings and the centrality of $i$.
- [The Schrödinger Equation in Biquaternionic Polar Variables](the-schrodinger-equation-in-biquaternionic-polar-variables.html), for the word of the field and the flow that the constant setting's shift acts on.
- [The Coupled Schrödinger Equation in Biquaternionic Polar Variables](the-coupled-schrodinger-equation-in-biquaternionic-polar-variables.html), the polar companion, where the shift of the two coefficients is read as the kinetic momentum and the kinetic energy.
- [The Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Form](the-variational-principle-and-the-coupled-schrodinger-equation-in-biquaternionic-form.html), the variational companion, where the current of this article is the Noether charge of the coupled action.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localisation of the central phase and the forced transformation law.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html), for the operator's algebra and its commutator.
- [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), for the sign convention and the left-action convention that this article inherits.
- [The Coupled Dirac Equation in Biquaternionic Form](the-coupled-dirac-equation-in-biquaternionic-form.html), for the structural contrast: the bilinear that is gauge invariant and not conserved, and the repaired current.
- [The Coupled Klein–Gordon Equation in Biquaternionic Form](the-coupled-klein-gordon-equation-in-biquaternionic-form.html), for the relativistic parent whose non-relativistic limit this article is.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html), for the potential biquaternion and the four-current that this article's $J$ sources.
- [The Electron in Biquaternionic Form](the-electron-in-biquaternionic-form.html), for the value and the sign of $ϙ$, which the algebra does not fix.
- [Landau Levels in Biquaternionic Form](landau-levels-in-biquaternionic-form.html) and [The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case](the-hydrogen-atom-in-biquaternionic-form-the-non-relativistic-case.html), for the standard solutions of the operator setting with a constant magnetic field and with a Coulomb potential.
- [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html), for the stress tensor of the operator setting.
- [Noether's Theorem in Biquaternionic Form](noethers-theorem-in-biquaternionic-form.html), for the construction that produces the current.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard treatment of minimal coupling and the conserved current.
- L. D. Landau and E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory* (Pergamon, 1977), for the charged scalar field in a magnetic field and the gauge-invariant current.
