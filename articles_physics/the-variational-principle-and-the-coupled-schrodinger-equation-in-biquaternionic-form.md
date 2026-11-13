# __The Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Form__

## Introduction

*The Variational Principle and the Schrödinger Equation in Biquaternionic Form* gives the free field's action, its variation and its two Noether currents. This article adds the electromagnetic connection to that action and asks what the addition changes: what the variation produces, what the symmetry delivers, and what the coupling costs.

**The action.**

$$
S=\int dt'\,d^{3}x\;\mathrm{Sc}\Big[\frac{i\hbar}{2}\big(\tilde\Xi^{*}\partial_{t'}\tilde\Xi-(\partial_{t'}\tilde\Xi^{*})\tilde\Xi\big)
-\frac{\hbar^{2}}{2m}\sum_\eta\big(D_\eta\tilde\Xi\big)^{*}\big(D_\eta\tilde\Xi\big)
+ϙ\varphi\,\tilde\Xi^{*}\tilde\Xi\Big],
$$

with $D_\eta=\partial_\eta+\frac{iϙ}{\hbar}A_\eta$ and $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$. It is the free action with two replacements: every spatial derivative becomes the covariant one, and one term in the potential is added. That is the whole of the coupling in the action, and it is the same one rule that the element-form companion states for the equation.

**Three findings.**

*First, the action is real for a general element, and the reality is structural.* The kinetic term is Hermitian, the gradient term is a sum of moduli and therefore a positive real number, and the potential term is Hermitian because $ϙ\varphi$ is a real scalar. $\mathrm{Sc}$ of a Hermitian element is real, so the three terms are real separately and no cancellation between them is needed (§*The Coupled Action*).

*Second, the connection enters the action in one place and the variation puts it in two.* The action carries the connection inside $D_\eta$ and inside $ϙ\varphi$; the equation carries it in the kinetic operator and in the potential. The two are one substitution seen from two sides, and the boundary-term identity that relates the gradient form to the operator form is what makes the variation produce the equation and not a different one (§*The Variation*).

*Third, the local phase transformation leaves the action invariant exactly, with no boundary term.* The kinetic term gains $-ϙ\,\partial_{t'}\Gamma\,n$ and the potential term gains $+ϙ\,\partial_{t'}\Gamma\,n$, and the two gains are equal and opposite. The gradient term is invariant by covariance. So the invariance is term by term, and it is the clearest statement of why the covariant derivative and the potential are one object (§*Gauge Invariance of the Action*).

**What is not claimed.** The action is not new: it is the standard action of a non-relativistic charged scalar field, written in the algebra's letters. The current it delivers is the element-form companion's current, not a second one. No new prediction and no new solution. The article's content is the closure of the variational statement — the action's reality, the variation's exactness, the invariance's exactness, and the current's identity with the equation's — and the honest record of the one thing it does not do, which is the local energy flux.

**Conventions.** The algebra, the two sectors, the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$, the two settings and the letters are the free variational companion's, with one addition: the connection $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$, the coupling $ϙ$, and the covariant derivative $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$. The charge $ϙ$ is minus the electric charge of the older convention, so the mechanical momentum is $\vec\pi=-i\hbar\nabla+ϙ\vec A$ and the potential energy is $-ϙ\varphi$. Time is $t'$ and $r'_t=c\,t'$ is the parent's material length.

## The Coupled Action

**The kinetic term is Hermitian.** Write $K=\frac{i\hbar}{2}\big(\tilde\Xi^{*}\partial_{t'}\tilde\Xi-(\partial_{t'}\tilde\Xi^{*})\tilde\Xi\big)$. Then

$$
K^{*}=-\frac{i\hbar}{2}\Big(\big(\partial_{t'}\tilde\Xi\big)^{*}\tilde\Xi-\tilde\Xi^{*}\partial_{t'}\tilde\Xi\Big)=K,
$$

so $K$ is Hermitian and $\mathrm{Sc}(K)$ is real. The antisymmetrisation is what does it: the two terms are conjugates of one another up to sign, and the difference of a number and its conjugate is imaginary, which the factor $i$ turns real. The coupling does not touch this term, and the reason is the metric: the connection's temporal coefficient is absorbed in $D_t$ and not in $\partial_{t'}$, so the kinetic term's structure is the free one.

**The gradient term is positive and real.** For each $\eta$,

$$
\mathrm{Sc}\big((D_\eta\tilde\Xi)^{*}(D_\eta\tilde\Xi)\big)=\sum_{\mu=0}^{3}\big|(D_\eta\tilde\Xi)_\mu\big|^{2}\ \ge 0,
$$

a sum of four moduli. This is the one place where the coupling changes the action's *sign structure* rather than its letters: the free gradient term is $\sum_\mu|\partial_\eta\tilde\Xi_\mu|^{2}$, also positive, and the covariant version is positive because $D_\eta$'s added term is anti-Hermitian and therefore does not disturb the modulus. The consequence is that the action's kinetic part is bounded below by zero and the energy is bounded below whenever $ϙ\varphi$ is, which is the diamagnetic statement in its variational form.

**The potential term is Hermitian.** $ϙ\varphi\,\tilde\Xi^{*}\tilde\Xi$ satisfies $[\cdot]^{*}=ϙ\varphi\,\tilde\Xi^{*}\tilde\Xi$ because $ϙ\varphi$ is real and $\tilde\Xi^{*}\tilde\Xi$ is Hermitian; its $\mathrm{Sc}$ is $ϙ\varphi\,n$ with $n=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)\ge0$. The sign is the companions': $+$ in the action, so that the variation gives $-ϙ\varphi$ in the equation, which is the Hamiltonian with the potential energy subtracted.

**The action is real.** Each of the three terms is Hermitian and $\mathrm{Sc}$ of a Hermitian element is real, so the integrand is real and $S$ is real. No term needs the other to cancel an imaginary part, and that is a stronger statement than reality of the sum.

**The pairing.** The action uses $\mathrm{Sc}(\cdot^{*}\cdot)$ and not $\mathrm{Sc}(\cdot^{\natural}\cdot)$. The reason is the free article's: the Hamiltonian is Hermitian for that pairing, and the action that reproduces the equation must use the pairing the equation's Hermiticity is stated in. The quaternion conjugate is used in the corpus where the corpus uses it — the quaternionic norm, the second-order operators of the Klein–Gordon article, the current of the Dirac article — and it is not used here.

**The two writings of the kinetic term.** The action's gradient term can be written as a modulus or as an operator sandwich,

$$
-\frac{\hbar^{2}}{2m}\sum_\eta\big(D_\eta\tilde\Xi\big)^{*}\big(D_\eta\tilde\Xi\big)
=\frac{\hbar^{2}}{2m}\sum_\eta\mathrm{Sc}\big(\tilde\Xi^{*}D_\eta^{2}\tilde\Xi\big)+\partial_\eta\,\mathrm{Sc}\big(\tilde\Xi^{*}D_\eta\tilde\Xi\big),
$$

because $D_\eta^{\dagger}=-D_\eta$. The two differ by a total divergence, so they give the same variation and the same equation, and the article uses the modulus form because it is manifestly positive and the operator form because it makes the variation one line.

## The Variation

**Varying the field.** Treating $\tilde\Xi$ and $\tilde\Xi^{*}$ as independent — legitimate over $\mathbb{C}$ — and integrating the gradient term by parts,

$$
\frac{\delta S}{\delta\tilde\Xi^{*}}
=i\hbar\,\partial_{t'}\tilde\Xi+\frac{\hbar^{2}}{2m}\sum_\eta D_\eta^{2}\tilde\Xi+ϙ\varphi\,\tilde\Xi
=\;i\hbar\,\partial_{t'}\tilde\Xi-\frac{1}{2m}\sum_\eta\big(-i\hbar D_\eta\big)^{2}\tilde\Xi+ϙ\varphi\,\tilde\Xi .
$$

Setting it to zero and multiplying by $-1$ gives

$$
i\hbar\,\partial_{t'}\tilde\Xi=\frac{1}{2m}\sum_\eta\big(-i\hbar D_\eta\big)^{2}\tilde\Xi-ϙ\varphi\,\tilde\Xi,
$$

which is the companion's equation, with $\vec\pi_\eta=-i\hbar D_\eta$ the mechanical momentum. The two signs in the residual are worth one check: the gradient term's plus sign in $\delta S/\delta\tilde\Xi^{*}$ is the boundary-term identity of the preceding section read backwards, and the potential term's plus sign is the sign of $+ϙ\varphi$ in the action. Both signs are the free article's and the coupling only renames the letters.

**Eight real equations, not one.** $\delta\tilde\Xi^{*}$ ranges over the eight real components of $\mathbb{B}$, and $\mathrm{Sc}$ is non-degenerate, so the vanishing of the bracket for every variation is the vanishing of the bracket as an element of $\mathbb{B}$. The eight components of the residual are the eight real Euler–Lagrange equations; they are not independent statements but one statement in eight coordinates, and the article states it once. The polar companion is the same statement in the chart's eight coordinates, and its §*The Euler–Lagrange Equations* is where the coordinate version of this paragraph lives.

**The conjugate variation.** Varying $\tilde\Xi$ instead of $\tilde\Xi^{*}$ gives the conjugate of the residual, so no second equation is produced: the action is real and the two variations are conjugates. This is the free article's observation, and the coupling does not change it, because the connection's coefficients are real scalars and the action's reality is term by term.

**What the variation does not produce.** It does not produce a Maxwell equation. The connection is a fixed background here, and varying it would produce the inhomogeneous Maxwell equation with the current of §*The Noether Current* as source; that step belongs to the Maxwell article's action-and-source section and is not repeated. It also does not produce a constraint on the field's amplitude: the equation is linear, so the variation is a linear equation and the space of solutions is a vector space.

## Gauge Invariance of the Action

**The transformation.** Let $\Gamma$ be a real function, $\lambda=\exp(iϙ\Gamma/\hbar)$, and let the field and the connection transform as

$$
\tilde\Xi\longmapsto\lambda\tilde\Xi,
\qquad
\vec A\longmapsto\vec A-\nabla\Gamma,
\qquad
\varphi\longmapsto\varphi+\partial_{t'}\Gamma .
$$

**The gradient term.** $D_\eta\tilde\Xi\mapsto\lambda D_\eta\tilde\Xi$ by the covariance identity, and $\lambda$ is a central unit, so $|D_\eta\tilde\Xi|^{2}$ is invariant. The term contributes nothing to the variation of the action.

**The kinetic term, and its gain.** With $\vartheta=ϙ\Gamma/\hbar$ the two halves of the kinetic term become

$$
\tilde\Xi'^{*}\partial_{t'}\tilde\Xi'=\tilde\Xi^{*}\partial_{t'}\tilde\Xi+i\,\partial_{t'}\vartheta\,\tilde\Xi^{*}\tilde\Xi,
\qquad
(\partial_{t'}\tilde\Xi')^{*}\tilde\Xi'=(\partial_{t'}\tilde\Xi^{*})\tilde\Xi-i\,\partial_{t'}\vartheta\,\tilde\Xi^{*}\tilde\Xi,
$$

because the central factors cancel in pairs and the derivative of the unit contributes once in each. The antisymmetrised combination therefore gains

$$
\Delta K=\frac{i\hbar}{2}\cdot 2i\,\partial_{t'}\vartheta\,\tilde\Xi^{*}\tilde\Xi
=-\hbar\,\partial_{t'}\vartheta\,\tilde\Xi^{*}\tilde\Xi
=-ϙ\,\partial_{t'}\Gamma\,\tilde\Xi^{*}\tilde\Xi,
$$

and taking $\mathrm{Sc}$ gives $-ϙ\,\partial_{t'}\Gamma\,n$.

**The potential term, and its gain.** $ϙ\varphi$ becomes $ϙ(\varphi+\partial_{t'}\Gamma)$, so the term gains $+ϙ\,\partial_{t'}\Gamma\,n$. **The two gains are equal and opposite, and the action is invariant exactly.** There is no boundary term to discard and no improvement to make: the local transformation is a symmetry of the Lagrangian and not only of the action.

**Why the two gains match, and what it says.** The kinetic gain is the derivative of the gauge function times the density, with the coupling's sign; the potential gain is the same object with the opposite sign. The matching is the statement that the covariant time derivative and the potential energy are one object split across two terms of the action — the split that the element-form companion records as the opposite signs of $D_t$ and $D_\eta$. A reader who wants a single sentence: *the action is invariant because the potential's shift and the phase's shift are the same shift.*

**What the invariance does not say.** It says nothing about the operator setting's domains or about large gauge functions with nonzero winding; those are the polar companion's open question 2 and the flux discussion, and the action's invariance is local and does not decide them.

## The Noether Current

**The global symmetry.** For constant $\alpha$ the transformation is $\tilde\Xi\mapsto e^{i\alpha}\tilde\Xi$ and the action is invariant. The Noether construction gives the current of the element-form companion,

$$
j_\eta=\frac{\hbar}{2mi}\,\mathrm{Sc}\Big(\tilde\Xi^{*}D_\eta\tilde\Xi-\big(D_\eta\tilde\Xi\big)^{*}\tilde\Xi\Big),
$$

and the temporal component is the density $n=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$. The derivation is the free article's with every derivative covariant, and the connection's terms cancel in pairs; the article does not repeat it.

**The current is the action's derivative with respect to the connection.** A shorter route, and the one that shows the object is not a coincidence:

$$
-\frac{\partial L}{\partial A_\eta}
=\frac{\hbar^{2}}{2m}\cdot 2\,\mathrm{Re}\sum_\mu\frac{iϙ}{\hbar}\,\overline{\big(D_\eta\tilde\Xi\big)_\mu}\,\tilde\Xi_\mu
=-\frac{\hbar ϙ}{m}\,\mathrm{Im}\,\mathrm{Sc}\big((D_\eta\tilde\Xi)^{*}\tilde\Xi\big)
=ϙ\,j_\eta,
$$

where the second equality uses $\mathrm{Re}(iZ)=-\mathrm{Im}Z$. So the charge current is minus the derivative of the Lagrangian with respect to the vector potential, which is the variational statement that the current is what the connection couples to. The sign is fixed by the action's sign for $A_\eta$ inside $D_\eta$ and by the minus sign in front of the gradient term; with the opposite sign of $ϙ$ the current changes sign with it and the identity stands.

**What the identity is good for.** It says that the current of this article and the source of the Maxwell equation are the same object, and it says it without a separate computation. It also says why the current must be gauge invariant: the Lagrangian's dependence on $\vec A$ is only through $D_\eta$, and $D_\eta$ is covariant, so $\partial L/\partial A_\eta$ transforms like a connection-independent vector. The free article's current lacks that property because the free Lagrangian's dependence on $\vec A$ is not there at all.

**The factor and the letters.** $j_\eta$ is the particle current; $ϙ j_\eta$ is the charge current. The element-form companion writes the charge current as $\vec J=ϙ\vec j$ and identifies it as the source of $\tilde\nabla_\Phi\tilde F=-\mu\tilde J$; the article uses that identification and does not re-derive it. The normalisation of $j$ is the free article's and is a convention, as it records.

## The Energy and the Two Settings

**The constant setting.** With $\tilde H_\Psi$ and the connection constant, the Lagrangian is the free one with the two coefficients shifted and the energy is the free article's,

$$
E=\mathrm{Sc}\big(\tilde\Xi^{*}\tilde H^{\mathrm{gco}}_\Psi\tilde\Xi\big),
\qquad
\tilde H^{\mathrm{gco}}_\Psi=(h_t-ϙ\varphi)e_t+i(\vec h_\Psi+ϙ\vec A),
$$

and it is conserved because $\tilde H^{\mathrm{gco}}_\Psi$ commutes with itself: $\frac{d}{dt'}E=\mathrm{Sc}(\partial_{t'}\tilde\Xi^{*}\tilde H^{\rm gco}_\Psi\tilde\Xi+\tilde\Xi^{*}\tilde H^{\rm gco}_\Psi\partial_{t'}\tilde\Xi)=0$ on solutions. This is the free article's computation with the shifted element, and it needs no new argument.

**The operator setting.** The energy density is

$$
e=\frac{\hbar^{2}}{2m}\sum_\eta\mathrm{Sc}\big((D_\eta\tilde\Xi)^{*}(D_\eta\tilde\Xi)\big)-ϙ\varphi\,n,
$$

which is the free article's density with the covariant gradient and the potential energy. Its spatial integral is the expectation of $\hat H^{\mathrm{gco}}$ on solutions, up to a boundary term, and **it is conserved for a time-independent connection**: the potential's contribution to the time derivative is exactly the work the field does against the potential, and the two cancel in the integral.

**What the article does not do.** It does not print the local energy flux. The local conservation law $\partial_{t'}e+\nabla\cdot\vec s=0$ holds, but the flux that makes it hold is not the naive one and it carries a term in the potential's gradient; the article states the density, states the global conservation, and leaves the flux to the stress-energy article, which is where the improvement terms are treated. This is a deliberate omission and not a lemma: a wrong flux would be worse than none.

**The positivity.** The first term of $e$ is positive and the second is positive or negative according to the sign of $ϙ\varphi$; so the energy is bounded below whenever $ϙ\varphi$ is bounded above, which is the diamagnetic statement again and the reason the operator setting's flow is well posed for a confining potential.

## The Lorentz Force

**The statement.** The divergence of the stress tensor of the coupled field is the Lorentz force density,

$$
\partial_{t'}\mathcal P_\eta+\sum_\zeta\partial_\zeta T_{\zeta\eta}=-\varrho\big(\vec E+\vec v\times\vec B\big)_\eta,
\qquad
\mathcal P_\eta=\hbar\,\mathrm{Im}\,\mathrm{Sc}\big(\tilde\Xi^{*}D_\eta\tilde\Xi\big)=m\,j_\eta,
$$

with $\mathcal P$ the momentum density, $T$ the stress tensor, $\varrho:=ϙn$ the charge density, $\vec E=-\nabla\varphi-\partial_{t'}\vec A$ and $\vec B=\nabla\times\vec A$. The overall minus sign is the coupling's: the corpus's $ϙ$ is minus the electric charge, so a charge density $\varrho$ feels $-\varrho(\vec E+\vec v\times\vec B)$ in these letters, which is $+q(\vec E+\vec v\times\vec B)$ in the older ones.

**The status of the statement.** It is the standard identity for the Schrödinger field, and the article states it and does not perform it: the computation requires the stress tensor's improvement term, and the free article's §*The Noether Currents* already points at the stress-energy article for that object. It is recorded here because it is the one place where the coupling's two entries in the equation — the covariant derivative and the potential — appear together in a single conservation law, and because §*Open Questions* lists it as the check that would close the article's variational ledger.

**What the identity would show.** That the field's momentum is not conserved, that the rate at which it is not conserved is the Lorentz force, and that the force is the sum of an electric part from the potential's gradient and a magnetic part from the current crossed with the field. The free article has no such statement because a free field has no force to feel.

## What the Principle Adds and What It Relabels

**Adds.** The action in one line, and the equation as one variation. The current twice: as the phase symmetry's Noether charge and as the connection's derivative, with the two identified. The invariance of the action under the local transformation, exactly and term by term. The positivity of the kinetic part, and with it the boundedness of the energy. The potential's sign fixed by the action rather than by a convention. And the identity of the current with the Maxwell source, which is the closure statement the element-form companion states and this article derives.

**Relabels.** The equation, whose derivation is the free one with covariant letters. The current, which is the free one with covariant derivatives. The energy, which is the free one with the shifted element in the constant setting and with the covariant gradient in the operator setting. Nothing here is a new physical principle; the action is the standard one and the algebra is its notation.

**The distinction that matters.** The free variational article's ledger is short because the free theory has one symmetry and one current. The coupled theory's ledger is longer in exactly one place: the connection gives the current a second definition, as the derivative of the Lagrangian, and that definition is what makes the current the source. That is the whole of what the coupling adds to the variational statement, and it is a genuine closure rather than a relabelling.

## Open Questions

**1. The local energy flux.** The density and the global conservation are stated; the flux is not. The missing computation is the standard one, with the potential's gradient term, and it belongs with the stress tensor's improvement. Until it is done, the article's energy statement is global in the operator setting and exact only in the constant setting.

**2. The connection's own variation.** Varying $\tilde A_\Phi$ in this action produces the inhomogeneous Maxwell equation with $\vec J$ as source, and it also produces a constraint on $\vec A$ from the temporal variation. The Maxwell article derives the equation from its own action; whether the two actions are one action with two variations, and whether the constraint is the Gauss law or its conjugate, is not examined here.

**3. The operator setting's boundary conditions.** The action's variation discards a boundary term, which is legitimate for fields that vanish at infinity and not for fields on a torus or with a flux tube. The self-adjointness of $\hat H^{\rm gco}$ under such conditions, and the effect of a singular connection, are the element-form companion's open questions and are inherited here.

## Summary

The coupled action is

$$
S=\int dt'\,d^{3}x\;\mathrm{Sc}\Big[\frac{i\hbar}{2}\big(\tilde\Xi^{*}\partial_{t'}\tilde\Xi-(\partial_{t'}\tilde\Xi^{*})\tilde\Xi\big)
-\frac{\hbar^{2}}{2m}\sum_\eta\big(D_\eta\tilde\Xi\big)^{*}\big(D_\eta\tilde\Xi\big)
+ϙ\varphi\,\tilde\Xi^{*}\tilde\Xi\Big],
$$

and its variation with respect to $\tilde\Xi^{*}$ is the coupled Schrödinger equation. The action is real term by term: the kinetic term is Hermitian, the gradient term is a sum of moduli and positive, and the potential term is Hermitian because $ϙ\varphi$ is real.

The local phase transformation leaves the action invariant exactly, with the kinetic term gaining $-ϙ\partial_{t'}\Gamma\,n$ and the potential term gaining $+ϙ\partial_{t'}\Gamma\,n$. The two gains match because the potential's shift and the phase's shift are the same shift.

The current is the free article's with covariant derivatives,

$$
j_\eta=\frac{\hbar}{2mi}\,\mathrm{Sc}\Big(\tilde\Xi^{*}D_\eta\tilde\Xi-\big(D_\eta\tilde\Xi\big)^{*}\tilde\Xi\Big),
\qquad
j_t=n,
$$

and it has a second definition, $ϙj_\eta=-\partial L/\partial A_\eta$, which identifies it as the source of the Maxwell equation and shows why it is gauge invariant.

The energy is $E=\mathrm{Sc}(\tilde\Xi^{*}\tilde H^{\rm gco}_\Psi\tilde\Xi)$ in the constant setting, exactly conserved; the operator setting's energy density is the covariant modulus of the gradient minus $ϙ\varphi n$, with the integral conserved for a time-independent connection. The local flux is not printed here, and §*Open Questions* says so.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t,\ \vec e_\mu$ | Quaternion basis, $\vec e_\mu^{2}=-e_t$ |
| $i$ | Central scalar imaginary |
| $*$, $\natural$ | Hermitian conjugation, quaternion conjugation |
| $\mathrm{Sc}$, $\mathrm{Tr}=2\,\mathrm{Sc}$ | Scalar part, trace |
| $t'$, $r'_t=c\,t'$ | Time variable, parental material length |
| $\tilde\Xi\in\mathbb{B}$ | The field |
| $ϙ$ | The coupling; minus the electric charge of the older convention |
| $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$ | The material connection; $\varphi$ and $\vec A$ real |
| $D_\eta=\partial_\eta+\frac{iϙ}{\hbar}A_\eta$ | The spatial covariant derivative |
| $\vec\pi_\eta=-i\hbar D_\eta=-i\hbar\partial_\eta+ϙA_\eta$ | The mechanical momentum |
| $S$ | The action; $L$ its density per unit $t'$ |
| $n=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ | The density; $\rho=2n$ is the free article's |
| $j_\eta$, $j_t=n$ | The particle current |
| $ϙj_\eta$, $\varrho=ϙn$ | The charge current and the charge density |
| $\tilde H^{\mathrm{gco}}_\Psi=(h_t-ϙ\varphi)e_t+i(\vec h_\Psi+ϙ\vec A)$ | The coupled Hamiltonian of the constant setting |
| $e$ | The energy density of the operator setting |
| $\Gamma$, $\lambda=e^{iϙ\Gamma/\hbar}$ | The gauge function and factor |
| $\vec E=-\nabla\varphi-\partial_{t'}\vec A$, $\vec B=\nabla\times\vec A$ | The fields of the connection |

## Further Reading

- [The Variational Principle and the Schrödinger Equation in Biquaternionic Form](the-variational-principle-and-the-schrodinger-equation-in-biquaternionic-form.html), the free companion whose structure this article extends.
- [The Coupled Schrödinger Equation in Biquaternionic Form](the-coupled-schrodinger-equation-in-biquaternionic-form.html), for the equation, the current and the two settings.
- [The Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-schrodinger-equation-in-biquaternionic-polar-variables.html), where the same action is written in the chart and the gauge direction is named.
- [The Schrödinger Equation in Biquaternionic Form](the-schrodinger-equation-in-biquaternionic-form.html), for the carrier and the pairing the action is written with.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localisation of the central phase and the forced transformation law.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html), for the covariance identities the invariance proof uses.
- [Noether's Theorem in Biquaternionic Form](noethers-theorem-in-biquaternionic-form.html), for the construction of the current from the symmetry.
- [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html), for the stress tensor and the improvement terms that §*The Energy and the Two Settings* leaves out.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html), for the equation that this article's current sources.
- [The Coupled Klein–Gordon Equation in Biquaternionic Form](the-coupled-klein-gordon-equation-in-biquaternionic-form.html), for the second-order case, where the same identities have a different completion.
- [The Coupled Dirac Equation in Biquaternionic Form](the-coupled-dirac-equation-in-biquaternionic-form.html) and [The Variational Principle and the Coupled Dirac Equation in Biquaternionic Form](the-variational-principle-and-the-coupled-dirac-equation-in-biquaternionic-form.html), for the spinor case, where the current is not a derivative bilinear.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard action, current and minimal coupling.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the stress tensor and the Lorentz force as its divergence.
