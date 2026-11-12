# __The Coupled Proca Equation in Biquaternionic Polar Variables__

## Introduction

This article substitutes the polar word into the coupled Proca equation and reads what the substitution makes visible. It is the polar companion of *The Coupled Proca Equation in Biquaternionic Form*, and it depends on three articles: the element form of the coupled equation for the equation, *The Proca Equation in Biquaternionic Polar Variables* for the free word and the two brackets, and *The Polar Decomposition of an N-Regular Biquaternion* for the word that the complex carrier requires.

**The substitution.**

$$
\tilde A=r\,e^{i\vartheta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\bigl(\theta_{\mathrm{rpd}},\hat u_{\mathrm b}\bigr)\,\tilde u_{\mathrm r}\bigl(\theta_{\mathrm{axr}},\hat u_{\mathrm r}\bigr),
$$

with $r>0$, $\vartheta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$, $\theta_{\mathrm{rpd}}\ge0$ the rapidity of the boost, $\hat u_{\mathrm b}\in S^2$ its axis, $\theta_{\mathrm{axr}}\in[0,2\pi)$ the angle of the rotor, and $\hat u_{\mathrm r}\in S^2$ its axis. The factors carry eight real parameters and the word is a bijection onto the N-regular set, which is the complement of the zero-divisor cone; the eight parameters are therefore coordinates on the units and no constraint is lost or added.

**The word is not the free article's word, and the difference is the article's first point.** The free Proca field is real, its word has two factors and four parameters, and it splits into two branches according to the sign of the Minkowski square. The coupled field is complex, its square is not a sign, the branch split has nothing to split, and the word that replaces it has four factors and eight parameters. The two factors the free word had to drop — the central phase and the rotor — return with the charge, and §*The Word* proves that in the algebra rather than asserting it.

**Three things are established.**

*First, the coupling enters the logarithmic derivative as one central scalar per slot.* Because each component of the connection is a central scalar, $\frac{iϙ}{\hbar}A_\mu$ passes through $\tilde A^{-1}$ and joins the logarithmic derivative without disturbing its types. It merges with the two central brackets — the scale and the phase — and it cannot reach either of the two frame brackets. That is a statement of type and not of size: a central scalar cannot produce a real vector part and cannot produce a Hermitian vector.

*Second, the gauge transformation is a translation of one parameter.* Multiplication of the field by a central unit multiplies the word and acts on $\vartheta_{\mathrm{pha}}$ alone. Infinitesimally that is exact with every other parameter fixed; the check is exact to machine precision. The chart therefore linearises the gauge group, and the connection's whole content in the chart is that one coordinate is not physical.

*Third, the equation in the chart is second order and not first order, and that is where this article parts company with the Dirac and Schrödinger companions.* Those fields are first order in the material time, their actions are first order, and the chart exposes a constrained system whose momenta partly vanish. The Proca field is second order in the material time, its action is second order, and no momentum vanishes identically. The chart therefore has no primary constraint to exhibit, and the honest statement of this article is that the polar form of the coupled Proca theory is a change of coordinates on a second-order problem and not a constraint analysis.

**What is not here.** The action, the Noether currents and the Euler–Lagrange equations are the variational companion's subject. This article's subject is the equation and its variables, and it states the polar reading of the same numbers in the places where the chart is sharper.

## The Word

**The free word had two factors.** The free article's result is

$$
\tilde A_\Phi=
\begin{cases}
\varepsilon\,i\,r\,\tilde U_{\Psi,\mathrm b}(\theta_{\mathrm{rpd}},\hat u_{\mathrm b}), & \langle\tilde A_\Phi\rangle_\natural=-r^{2}<0,\\[2pt]
r\,\tilde U_{\Psi,\mathrm b}(\theta_{\mathrm{rpd}},\hat u)\,, & \langle\tilde A_\Phi\rangle_\natural=+r^{2}>0,
\end{cases}
$$

with the rapidity signed on the spacelike branch and the axis locked to the direction of $\vec A$ there. Four parameters on each branch, and the two branches keyed to the sign of a real norm.

**Why the free word had to drop the phase.** The central phase factor $e^{i\vartheta}$ maps the material sector off itself: $i$ times an anti-Hermitian element is Hermitian, so a phase-rotated material element is not a material element. The phase is therefore not available to a real field, and the free word's missing factor is missing for that reason and no other. The free article states the same fact as the absence of a central bracket in the logarithmic derivative.

**Why the free word had to drop the rotor's axis.** The real field's frame has one vector in it, the boost's, and the direction of $\vec A$ is that vector; the rotor has nothing left to rotate, so it collapses to the direction on one branch and to a sign on the other. The count is exact: four components, four parameters.

**The coupled word restores both.** On the complex carrier the phase is available, because $\mathbb{B}$ is closed under multiplication by $i$; and the frame is a full unit rather than a boost, so the rotor keeps its axis. The count is exact again: eight real components, eight parameters. The two restorations are one restoration, and the statement of it is a norm computation.

**The norm of the word.** The quaternionic norm of the coupled word is the phase squared times the scale squared:

$$
\langle\tilde A\rangle_\natural=\tilde A\tilde A^{\natural}=r^{2}e^{2i\vartheta_{\mathrm{pha}}},
$$

exactly, for every value of the other six parameters. The check is exact to machine precision on random draws. Two consequences follow and they are the article's structural core.

**The N-regular set is $r>0$ and nothing else.** The norm vanishes only at $r=0$, so the chart's domain is the open half-line in $r$ times the six angular parameters, and the zero-divisor cone is the boundary $r=0$. The free article's cone was reached by a lightlike four-vector and it was a genuine boundary of the field; here it is the origin of the polar chart and only that.

**The phase is the argument of the norm, and that is why the charge exists.** For a real field the norm is real and its argument is a sign, which is the free article's $\varepsilon$. For a complex field the norm is a complex number of modulus $r^{2}$ and its argument is $2\vartheta_{\mathrm{pha}}$, a continuous coordinate. The free field's discrete sign and the coupled field's continuous phase are the same slot of the same word, read on the two carriers; the charge is what that slot becomes when it can move continuously.

**The two branches are gone and nothing replaces them.** The free article's branch split is the sign of the norm, and the coupled norm has no sign. There is no third word and no second chart: the four-factor word covers the whole N-regular set of $\mathbb{B}$, both the elements whose Minkowski square is positive and those whose square is negative and those whose square is neither, because the square is now a complex number and complex numbers have no sign.

## The Covariant Logarithmic Derivative

**The identity.** Differentiate the word and divide by it, and add the connection:

$$
\tilde A^{-1}\tilde\nabla_{\mathrm{gco},\mu}\tilde A
=\tilde A^{-1}\frac{\partial\tilde A}{\partial R_\mu}+\frac{i\,ϙ}{\hbar}A_\mu
=\frac{\partial\ln r}{\partial R_\mu}
+i\frac{\partial\vartheta_{\mathrm{pha}}}{\partial R_\mu}
+\tilde A^{-1}\frac{\partial\tilde A}{\partial R_\mu}\Big|_{\text{frame}}
+\frac{i\,ϙ}{\hbar}A_\mu .
$$

The last written term is the frame's share, and the point of the display is that the connection's term is separable: it is one central scalar per component, added after the word has been differentiated, with no factor of $\tilde A$ or $\tilde A^{-1}$ attached to it. That separability is not an approximation. It follows from $\tilde A_\Phi$ having central scalar coefficients, which is the abelian case, and it fails the moment the connection's coefficients are elements rather than scalars.

**The frame's share in the four-factor word.** Write $\tilde U$ for the boost and $\tilde u$ for the rotor, and $\Gamma_\mu=\tilde U^{-1}\partial_\mu\tilde U$, $\rho_\mu=\tilde u^{-1}\partial_\mu\tilde u$. Then

$$
\tilde A^{-1}\partial_\mu\tilde A
=\frac{\partial_\mu r}{r}+i\partial_\mu\vartheta_{\mathrm{pha}}
+\tilde u^{-1}\Gamma_\mu\tilde u+\rho_\mu .
$$

The four terms have four different algebraic types: a real central scalar; a central imaginary number; a Hermitian vector conjugated by the rotor; a real vector part. Those are the four brackets of the polar corpus, and the word's four factors produce them one for one.

**The connection touches two of the four.** The added term's temporal slot is $\frac{iϙ}{\hbar}A_t=-\frac{ϙ}{\hbar}a'_t$ for a material connection $A_t=i a'_t$, a *real* central number; its spatial slots are $\frac{iϙ}{\hbar}A_\eta$, central imaginary numbers because $A_\eta$ is real. So in every slot the connection is central, real in the temporal one and imaginary in the spatial ones, and the central scalars are spanned by the scale bracket and the phase bracket. The connection therefore merges with those two and with nothing else. In particular it cannot produce a Hermitian vector, so it cannot reach the boost bracket, and it cannot produce a real vector part, so it cannot reach the rotor bracket.

**The physical reading of that type statement.** The connection shifts the four-momentum and does nothing else at this order. Slot by slot,

$$
\hbar c\,\kappa_t=E+ϙ c\,a'_t,
\qquad
\hbar\vec\kappa=\vec p+ϙ\vec A,
$$

with $E=-\hbar c\,\partial\vartheta_{\mathrm{pha}}/\partial r'_t$ and $\vec p=\hbar\nabla\vartheta_{\mathrm{pha}}$ the free readings. The scalar and vector potentials are the two slots of one element, so the two classical substitutions are one substitution and no relative sign can be chosen. That is the coupled Dirac article's statement in the bosonic case, and it holds here for the same reason: the connection is one element and its slots are the algebra's.

**What the type statement does not say.** It does not say that the potential cannot affect the frame. It says that the potential cannot affect the frame *at the level of the logarithmic derivative*, that is, not through the additive term. The frame responds to the potential through the equation, because the equation relates the brackets to each other and a shift in one moves the others. The distinction is the difference between the coupling's location and its consequences, and the free Dirac polar article makes the same distinction for the spin.

**A warning about the types.** The central scalars of the temporal slot and of the spatial slots are not the same type: the temporal slot's share is real and the spatial slots' share is imaginary, because the material connection's temporal coefficient is imaginary and its spatial coefficients are real. A table that assigns the connection to "the central imaginary bracket" is therefore right for the spatial slots and wrong for the temporal one, and the article does not draw such a table.

## The Gauge Transformation Is a Phase Translation

**The exact infinitesimal statement.** Let $\lambda=\exp(i\vartheta_{\mathrm{gau}})$ be a constant central unit and let $\tilde A_2=\lambda\tilde A$. Then

$$
\tilde A_2=r\,e^{i(\vartheta_{\mathrm{pha}}+\vartheta_{\mathrm{gau}})}\,
\tilde U_{\Psi,\mathrm b}\bigl(\theta_{\mathrm{rpd}},\hat u_{\mathrm b}\bigr)\,
\tilde u_{\mathrm r}\bigl(\theta_{\mathrm{axr}},\hat u_{\mathrm r}\bigr),
$$

so the gauge transformation is the translation of $\vartheta_{\mathrm{pha}}$ by $\vartheta_{\mathrm{gau}}$ with the other seven parameters fixed. The identity is exact and the numerical check is exact to $10^{-16}$.

**Why it is exact.** $\lambda$ is central, so it passes to the left through the whole word and multiplies the leftmost factor; and the leftmost factor is the phase factor, whose argument is additive. No other factor is touched, because no other factor carries a central scalar.

**What it says about the connection.** For a pure-gauge connection, $A_\mu=\partial_\mu\Lambda$, the added term is $\frac{iϙ}{\hbar}\partial_\mu\Lambda$, so

$$
i\frac{\partial\vartheta_{\mathrm{pha}}}{\partial R_\mu}+\frac{i\,ϙ}{\hbar}A_\mu
=i\frac{\partial}{\partial R_\mu}\Bigl(\vartheta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\Lambda\Bigr),
$$

and the whole effect of the potential is absorbed by a reparameterisation of one coordinate. That is the polar statement of gauge invariance, and it is a statement about the angle and not about the field.

**The finite statement and its one caveat.** For a finite shift the translated angle may leave the interval $(-\pi/2,\pi/2]$, and then the word's first factor is no longer in the chart's normal form: $e^{i(\vartheta+\vartheta_{\mathrm{gau}})}$ with the sum outside the range is a unit whose real part is negative, and the chart's phase factor is the one with positive real part. The excess is absorbed by the other factors, and the chart is therefore not closed under the gauge group as a chart, although the field is. The article states the infinitesimal identity as the exact statement and records the range as a property of the coordinates.

**The contrast with the element form.** In the element form the gauge transformation multiplies the field by a central unit and that is that. In the chart the same operation is the motion of one coordinate, and the coordinate is the argument of the norm. The two statements are the same statement, and the second is the reason the operation is called a phase transformation.

## The Equation in the Chart

**The second-order operator.** The coupled equation is second order once the field strength is eliminated, and in the chart the elimination reads

$$
\tilde A^{-1}\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}\tilde A
=\sum_\mu\bigl(\tilde A^{-1}e_\mu^{\natural}\tilde A\bigr)\,
\tilde\nabla_{\mathrm{gco},\mu}\Bigl(\tilde A^{-1}\tilde\nabla_{\mathrm{gco}}\tilde A\Bigr)
+\text{(the frame's derivative terms)} ,
$$

that is: the second-order operator becomes the first-order brackets contracted with the units as the field's own frame sees them, $\tilde A^{-1}e_\mu^{\natural}\tilde A$. The identity is exact and it is the chart's version of the element form's statement that the covariant derivatives are central: the units are conjugated by the field, the derivatives are not.

**What the frame conjugation does.** The four units conjugated by $\tilde A$ are the field's own tetrad. The contraction is therefore a contraction with a *field-dependent* frame, and that is the chart's real content: the equation is the free one written in the field's frame, with the connection shifted. The free article's two displays — one real equation for the modulus and one traceless equation for the frame — are the two halves of that contraction, and the coupling shifts both.

**The mass term in the chart.** The invariant length is a function of the scale and of the four frame angles, and the chart makes two facts about it exact.

*The rotor is what costs.* With the rotor trivial the length is the square of the scale,

$$
\mathrm{Sc}\bigl(\tilde A^{*}\tilde A^{\natural}\bigr)=r^{2}
\qquad\text{whenever } \theta_{\mathrm{axr}}=0,
$$

for every rapidity and every boost axis, to $10^{-14}$ over random draws. The reason is that the boost is a Lorentz transformation of the four-vector and the invariant length is Lorentz invariant, so the rapidity cannot enter.

*The rapidity costs nothing when the two axes are collinear.* With the rotor engaged and its axis parallel or antiparallel to the boost's axis, the ratio $\mathrm{Sc}(\tilde A^{*}\tilde A^{\natural})/r^{2}$ is independent of the rapidity: it is $0.7648$ at rapidity $0$, $2$, and $5$ alike for $\theta_{\mathrm{axr}}=0.7$. With the axes perpendicular the same angle gives $0.7648$ at zero rapidity, $0.7010$ at rapidity $1$, and $0.4401$ at rapidity $2$.

**What the chart does not give.** The general value is not displayed here as a closed expression in the six angles: it is the scalar part of a product of four units, and its interpolation between the two limits above is the frame's business rather than the scale's. What the chart does give is the division: the mass term is the one object in the action that sees the frame's non-Lorentz part, and it sees it only through the angle between the rotor's axis and the boost's.

**The constraint in the chart.** The trace of the equation is the covariant Lorenz condition, and in the chart it is one real equation among the eight:

$$
\mathrm{Sc}\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A\bigr)=0,
$$

which is the statement that the covariant divergence of the word vanishes. The element form computes it; the chart's contribution is the reading: the divergence is built from the scale and phase brackets and from the connection's temporal slot, so the constraint is a relation among the three central objects and the modulus, and the frame's brackets do not enter it. That is why the constraint is exactly the one the element form finds: the curvature is traceless, and the trace is blind to the frame.

## What the Chart Shows and What It Hides

**Shows.**

- The count: eight parameters, eight components, and the four-factor word matching the four types of the logarithmic derivative.
- The phase as the argument of the norm, and the free article's discrete sign as the real slice of it.
- The connection's location: two central slots and no others, with the temporal slot real and the spatial ones imaginary.
- The gauge transformation as one coordinate's translation, infinitesimally exact.
- The mass term's dependence on the frame's non-Lorentz part, and its independence of the rapidity when the rotor's axis lies along the boost's.

**Hides.**

- The constraint structure. The Proca field is second order in the material time and no momentum vanishes identically, so the chart has no primary constraint to exhibit. The Schrödinger and Dirac companions' constrained systems have no analogue here, and the difference is the order of the equation and not the choice of variables.
- The field strength. $\tilde F$ is a derived object in the chart, built from the brackets and the frame's conjugation, and the chart does not simplify its bilinear dependence on the connection.
- The current. The charge current is a bilinear in the field and its conjugate, and the chart's expression for it is longer than the element form's without being more informative.

**The honest ledger.** The chart is a coordinate system, and its virtue is that the gauge group becomes one visible coordinate and the coupling becomes four visible slots. Its cost is that the equation becomes a contraction with a field-dependent frame, and every statement about the field strength becomes a statement about that frame. Neither form is simpler; the chart is *sharper about the coupling* and the element form is *sharper about the algebra*.

## Open Questions

**Whether the chart's mass-term formula has a closed form in all six angular parameters.** The article states the exact reduction to $\mathrm{Sc}(\tilde u^{-2}\tilde U^{-2})$ and the exact value $r^{2}$ on the trivial-rotor slice. The general expression is a product of two unit elements' squares and it is not displayed; whether it factorises into a rapidity part and an angle part is not settled here.

**Whether the constraint is the whole constraint.** The trace of the equation is one real equation. Whether the traceless part of the equation, together with it, is equivalent to the four real equations of the element form in every configuration — and not merely on the Lorenz surface — is the chart's version of the free article's question about the two displays, and it is not answered here.

**The operator setting.** The article treats a constant connection and a general field. The operator setting, in which the connection is a function and the field strength has curvature, is the variational companion's subject, and the chart's treatment of a general connection is not attempted.

## Summary

The coupled Proca field is written

$$
\tilde A=r\,e^{i\vartheta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
$$

with eight real parameters and the word a bijection onto the N-regular set. The free field's two-factor word is the real slice of this one: the phase and the rotor are the two factors that reality removes and the charge restores, and the norm $\langle\tilde A\rangle_\natural=r^{2}e^{2i\vartheta_{\mathrm{pha}}}$ is the single line that shows it.

The connection is central per slot, so it merges with the scale and the phase brackets and cannot touch the boost or the rotor; the four-momentum shift $\hbar c\kappa_t=E+ϙca'_t$, $\hbar\vec\kappa=\vec p+ϙ\vec A$ is one substitution in one element. The gauge transformation is the translation of $\vartheta_{\mathrm{pha}}$ alone, exact infinitesimally. The equation is second order, the chart exhibits no primary constraint, and that is the difference between this sector and the first-order sectors of the Schrödinger and Dirac companions. The mass term is $r^{2}$ exactly when the rotor is trivial, because the boost is a Lorentz transformation and the rotor is not.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde A=r\,e^{i\vartheta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The word: scale, central phase, boost, rotor |
| $r>0$ | Scale; $\langle\tilde A\rangle_\natural=r^{2}e^{2i\vartheta_{\mathrm{pha}}}$ |
| $\vartheta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ | Central phase; the gauge-dependent coordinate |
| $\theta_{\mathrm{rpd}}\ge0,\ \hat u_{\mathrm b}\in S^{2}$ | Rapidity and axis of the boost |
| $\theta_{\mathrm{axr}}\in[0,2\pi),\ \hat u_{\mathrm r}\in S^{2}$ | Angle and axis of the rotor |
| $\mathbb{B}$, $\mathbb{B}_\Phi$, $\mathbb{B}_\Psi$ | The algebra, its material and informational sectors |
| $\tilde A_\Phi=A_te_t+\sum_\eta A_\eta\vec e_\eta$ | The connection; $A_t=i a'_t$ imaginary, $A_\eta$ real in the material case |
| $\tilde\nabla_{\mathrm{gco},\mu}=\partial_\mu+\frac{iϙ}{\hbar}A_\mu$ | The central per-component covariant derivative |
| $\Gamma_\mu=\tilde U^{-1}\partial_\mu\tilde U$, $\rho_\mu=\tilde u^{-1}\partial_\mu\tilde u$ | The frame's two logarithmic derivatives |
| $\tilde A^{-1}\partial_\mu\tilde A$ | The four brackets: scale, phase, boost, rotor |
| $\tilde K_{\Phi,\mathrm{gco}}=\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_\Phi$ | Covariant wavevector; the one substitution |
| $\kappa_t,\vec\kappa$ | Its components; $\hbar c\kappa_t=E+ϙca'_t$, $\hbar\vec\kappa=\vec p+ϙ\vec A$ |
| $\lambda=\exp(i\vartheta_{\mathrm{gau}})$ | Central gauge unit; $\vartheta_{\mathrm{gau}}=ϙ\Lambda/\hbar$ |
| $\tilde F$ | Curvature of the connection; traceless, so blind to the constraint |
| $k_m=mc/\hbar$ | Mass wave number |

## Further Reading

- [The Coupled Proca Equation in Biquaternionic Form](the-coupled-proca-equation-in-biquaternionic-form.html), the element form this article re-coordinatises.
- [The Proca Equation in Biquaternionic Polar Variables](the-proca-equation-in-biquaternionic-polar-variables.html), for the free two-factor word, the two branches and the two brackets.
- [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the four-factor word and its parameter count.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localization of the central phase.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html), for the operator identity with the curvature.
- [The Coupled Dirac Equation in Biquaternionic Polar Variables](the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), for the same type statement in the first-order sector.
- [The Variational Principle and the Coupled Proca Equation in Biquaternionic Form](the-variational-principle-and-the-coupled-proca-equation-in-biquaternionic-form.html), for the action and the currents in the element form.
- [The Variational Principle and the Coupled Proca Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-proca-equation-in-biquaternionic-polar-variables.html), for the action in the chart.
- [The Variational Principle and the Proca Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-proca-equation-in-biquaternionic-polar-variables.html), for the free action in the chart.
- [Spin Hydrodynamics in Biquaternionic Form](spin-hydrodynamics-in-biquaternionic-form.html), for the frame's brackets as fluid variables.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor and the frame in geometric algebra.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the standard coupled massive vector field.
