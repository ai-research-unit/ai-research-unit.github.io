# __The Coupled Klein–Gordon Equation in Biquaternionic Polar Variables__

## Introduction

This article substitutes the polar word into the coupled Klein–Gordon equation and reads what the substitution makes visible. It is the polar companion of *The Coupled Klein–Gordon Equation in Biquaternionic Form*, and it depends on that article for the equation, on *The Klein–Gordon Equation in Biquaternionic Polar Variables* for the word, the pair of real equations and the quantum potential, and on *The Polar Decomposition of an N-Regular Biquaternion* for the word itself.

**The substitution.**

$$
\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\bigl(\theta_{\mathrm{rpd}},\hat u_{\mathrm b}\bigr)\,\tilde u_{\mathrm r}\bigl(\theta_{\mathrm{axr}},\hat u_{\mathrm r}\bigr),
$$

with $r>0$, $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$, $\theta_{\mathrm{rpd}}\ge0$, $\hat u_{\mathrm b}\in S^{2}$, $\theta_{\mathrm{axr}}\in[0,2\pi)$, and $\hat u_{\mathrm r}\in S^{2}$. The word is a bijection from the eight parameters onto the $N$-regular set, so the parameters are coordinates on the units and the substitution loses nothing. The domain is unchanged by the coupling: the connection is a set of functions and the field's own regularity is what decides whether the word exists.

**Three things are established.**

*First, the connection enters the chart as one additive central term in the covariant bracket, and nothing else.* Because each $A_\mu$ is a complex scalar, it commutes with the whole word, so

$$
\tilde\Xi^{-1}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi
=\tilde\Xi^{-1}\partial_\mu\tilde\Xi+\frac{i\,ϙ}{\hbar}A_\mu ,
$$

with the connection's term added after the word has been differentiated and with no factor of $\tilde\Xi$ or $\tilde\Xi^{-1}$ attached to it. The separability is not an approximation: it is the algebraic signature of the abelian gauge group, whose parameter lies in the centre.

*Second, the connection therefore touches only the central slots, and the two-object pair survives.* A central scalar is either real or central imaginary in a given slot, and the four brackets of the word's logarithmic derivative contain exactly one bracket of each type: the scale is real and the phase is central imaginary. So the connection merges with those two and cannot reach the boost or the rotor, and for a central field the whole coupling is the substitution

$$
\partial_{r'_t}S_{\tilde\Xi}\ \mapsto\ \partial_{r'_t}S_{\tilde\Xi}-ϙ\,a'_t ,
\qquad
\nabla S_{\tilde\Xi}\ \mapsto\ \nabla S_{\tilde\Xi}+ϙ\,\vec A ,
$$

where $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ is the action and $\tilde A_\Phi=i a'_t e_t+\vec A$ the material connection. The two substitutions are the two classical replacements in one step, and the two signs are the metric's and not a convention.

*Third, the coupled pair is the parent's pair with that substitution and no other change.* The amplitude equation becomes the mass shell with the mechanical momentum and the same quantum potential; the transport equation becomes the divergence of the mechanical current; the quantum potential is untouched, because it depends on the density alone and the density is $r^{2}$ in both cases. The vorticity is *not* untouched: the free flow is a gradient flow and therefore irrotational, and the coupled flow has vorticity $ϙ\vec B$. That is the one qualitative change the chart exhibits, and §*The Current, the Vorticity and the Flux* computes it.

**Scope.** The connection is treated as an external field with a constant or a varying profile, and the equation is the component equation of the element companion — the one that decouples, that the action produces, and that the current belongs to. The element companion's other equation, $\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}\tilde\Xi=k_m^{2}\tilde\Xi$, is the subject of §*What the Chart Cannot Carry*, where the chart shows why it is not a two-function system. The operator setting, in which the amplitude and the action are functions of the coordinates and the equation becomes a PDE, is the Madelung problem of the standard literature and is cited rather than re-derived.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; $i$ is the central scalar imaginary; $^{*}$ is Hermitian conjugation and $^{\natural}$ quaternion conjugation; $\mathrm{Sc}$ is the coefficient of $e_t$ and $\mathrm{Tr}=2\,\mathrm{Sc}$. The pairing is $\mathrm{Sc}(\cdot^{*}\cdot)$ throughout. The material time is $r'_t=c\,t'$, the d'Alembertian is $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$, and $k_m=mc/\hbar$. The connection is $\tilde A_\Phi=i a'_t e_t+\vec A$ with $a'_t$ and $\vec A$ real, and the coupling is $ϙ$.

## The Word and Its Domain

**The collapse on a central field is the free article's and it is unchanged.** On the centre the boost has neither rapidity nor axis and the rotor has neither angle nor axis, so the word reduces to

$$
\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\varepsilon\,e_t ,
\qquad \varepsilon=\pm1,
$$

with the three parameters $(r,\theta_{\mathrm{pha}},\varepsilon)$ a bijection onto the nonzero complex scalars. The sign is data: the word's angle runs over a half-turn and the rotor's sign carries the other half. The action is $\hbar\theta_{\mathrm{pha}}$ modulo $2\pi\hbar$ and is a coordinate of the field.

**The coupling does not enlarge or shrink the domain.** The word needs $r>0$; the connection is a set of functions and contributes no condition on the field, so the parameter domain is the free article's and the word's bijection is unaffected. Whether the *flow* stays inside that domain is a separate question, and it is the free second-order article's: the covariant operator is the free one with central coefficients, so the coupling adds lower-order terms and no new mechanism, and the article inherits the free statement rather than proving it. What the coupling does add is a motion of the phase by a function, which is a reparameterisation and not a motion of the field.

**The four coefficients and the one pair.** The free polar article's §*General Fields* records that a general element's four coefficients obey four independent equations, so the polar pair describes one coefficient and the mixed case is the constant-polarization case $\tilde\Xi=\tilde Q_{\mathrm{amp}}g$. The coupling preserves that structure exactly: $A_\mu$ is central, it commutes with the constant $\tilde Q_{\mathrm{amp}}$, and

$$
\tilde\nabla_{\mathrm{gco},\mu}\big(\tilde Q_{\mathrm{amp}}g\big)=\tilde Q_{\mathrm{amp}}\,\tilde\nabla_{\mathrm{gco},\mu}g ,
$$

so the polarized field solves the coupled equation exactly when the scalar $g$ does. The polar chart of the coupled theory is therefore the chart of one charged scalar, and the fourfold multiplicity is a constant factor that the chart carries without seeing.

## The Covariant Bracket

**The identity.** Differentiate the word, divide by it, add the connection:

$$
\mathcal A^{\mathrm{gco}}_\mu:=\tilde\Xi^{-1}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi
=\underbrace{\frac{\partial_\mu r}{r}+i\,\partial_\mu\theta_{\mathrm{pha}}
+\tilde u_{\mathrm r}^{-1}\bigl(\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b}\bigr)\tilde u_{\mathrm r}
+\tilde u_{\mathrm r}^{-1}\partial_\mu\tilde u_{\mathrm r}}_{\text{the free bracket }\mathcal A_\mu}
+\frac{i\,ϙ}{\hbar}A_\mu .
$$

The four bracketed terms have four different algebraic types — a real central scalar, a central imaginary number, a Hermitian vector conjugated by the rotor, and a real vector part — and the connection's term is a fifth object of a fifth-and-a-half type: a complex central scalar, which is the sum of the first two types.

**Which bracket it joins, slot by slot.** For a material connection the temporal coefficient is imaginary, $A_t=i a'_t$, so

$$
\frac{i\,ϙ}{\hbar}A_t=-\frac{ϙ}{\hbar}a'_t
\qquad\text{(real central)},
\qquad
\frac{i\,ϙ}{\hbar}A_\eta=\frac{i\,ϙ}{\hbar}A_\eta
\qquad\text{(central imaginary)} .
$$

So in the temporal slot the connection adds to the *scale* bracket and in the spatial slots to the *phase* bracket. The Proca companion states the same fact in the same words, and it holds here for the same reason: the type of the connection's term is fixed by the reality of the potential's coefficients, not by the field. A table that assigns the connection to "the central imaginary bracket" is therefore right for the three spatial slots and wrong for the temporal one, and this article does not draw such a table.

**The physical reading.** The temporal slot's share is a real addition to $\partial_{r'_t}\ln r$ and the spatial slots' shares are imaginary additions to $\partial_\eta\theta_{\mathrm{pha}}$; together they are one substitution in the four-momentum,

$$
\hbar c\,P_t=E+ϙ c\,a'_t,
\qquad
\hbar\vec P=\vec p+ϙ\vec A,
\qquad
E=-\hbar c\,\frac{\partial\theta_{\mathrm{pha}}}{\partial r'_t},
\quad
\vec p=\hbar\nabla\theta_{\mathrm{pha}} ,
$$

and the scalar and vector potentials are the two slots of one element, so the two classical substitutions are one substitution and no relative sign can be chosen. The signs as written are the metric's: the temporal slot enters the mass shell with a plus on the potential and the spatial slots with a plus on the potential too, and the two pluses look opposite because the temporal slot enters the shell with a minus overall.

**One $i$, in the temporal slot.** The bracket's temporal coefficient and the physical temporal momentum are not the same letter. The bracket is a sum of four types, and its temporal coefficient is central imaginary — the same $i$ that makes the temporal coefficient of $\tilde P_\Phi$ equal $i(E/c)$ in the free article. So $\kappa^{\mathrm{kin}}_t=-i\,P_t$ and $\kappa^{\mathrm{kin}}_\eta=P_\eta$: the physical momentum is the bracket's coefficient with the $i$ removed from the temporal slot. The square is therefore $\bigl(\kappa^{\mathrm{kin}}_t\bigr)^{2}=-P_t^{2}$, and the mass shell carries $P_t^{2}-\lvert\vec P\rvert^{2}$ with the minus in front of the temporal term coming from that $i$. The article uses $P$ for the physical components and $\kappa^{\mathrm{kin}}$ for the bracket's, and keeps them apart.

**What the type statement does not say.** It does not say that the potential cannot affect the frame. It says that the potential cannot affect the frame *through the additive term*, which is the only place the connection appears before the equation is used. The frame responds to the potential through the equation, because the equation relates the brackets to one another and a shift in one moves the others; the shift in the phase bracket moves the amplitude through the mass-shell relation, and the frame follows. The distinction is the difference between where the coupling sits and what it does, and the Proca companion draws the same distinction for the rotor.

## The Gauge Transformation Is a Phase Translation

**The exact infinitesimal statement.** Let $\lambda=\exp(i\vartheta_{\mathrm{gau}})$ with $\vartheta_{\mathrm{gau}}=ϙ\Lambda/\hbar$ and let $\tilde\Xi_2=\lambda\tilde\Xi$. Then

$$
\tilde\Xi_2=r\,e^{i(\theta_{\mathrm{pha}}+\vartheta_{\mathrm{gau}})}\,
\tilde U_{\Psi,\mathrm b}\bigl(\theta_{\mathrm{rpd}},\hat u_{\mathrm b}\bigr)\,
\tilde u_{\mathrm r}\bigl(\theta_{\mathrm{axr}},\hat u_{\mathrm r}\bigr),
$$

so the gauge transformation is the translation of $\theta_{\mathrm{pha}}$ by $ϙ\Lambda/\hbar$ with the other seven parameters fixed, and the identity is exact because a central unit passes to the left through the whole word and the phase factor is the leftmost factor.

**What it says about the connection.** For a pure-gauge connection $A_\mu=\partial_\mu\Lambda$ the added term is $\frac{iϙ}{\hbar}\partial_\mu\Lambda$, so

$$
i\frac{\partial\theta_{\mathrm{pha}}}{\partial R_\mu}+\frac{i\,ϙ}{\hbar}A_\mu
=i\frac{\partial}{\partial R_\mu}\Bigl(\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\Lambda\Bigr),
$$

and the whole effect of the potential is absorbed by a reparameterisation of one coordinate. That is the polar statement of gauge invariance: the connection's content in the chart is that one coordinate is not physical.

**The finite statement and its caveat.** For a finite shift the translated angle may leave $(-\pi/2,\pi/2]$, and then the first factor is no longer in the chart's normal form; the excess is absorbed by the other factors. The chart is therefore not closed under the gauge group although the field is, and the article states the infinitesimal identity as the exact statement and records the range as a property of the coordinates. The Proca companion records the same caveat in the same terms.

**What the coupling adds to this picture.** Nothing, and that is the point. The gauge transformation was already a phase translation; the coupling is what makes the translation *local*, because the connection's transformation law is what allows $\Lambda$ to depend on the coordinates. The chart shows the two facts as one: a local translation of one coordinate is a gauge transformation, and a global translation of it is a change of the field's phase.

## The Equation in Polar Variables: the Central Field

**The factorisation.** For a central field the covariant derivative factors exactly:

$$
\tilde\nabla_{\mathrm{gco},\mu}\bigl(r\,e^{i\theta_{\mathrm{pha}}}e_t\bigr)
=e^{i\theta_{\mathrm{pha}}}\Bigl(\partial_\mu r+i\,r\,\kappa^{\mathrm{kin}}_\mu\Bigr)e_t ,
\qquad
\kappa^{\mathrm{kin}}_\mu:=\partial_\mu\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}A_\mu .
$$

The parenthesis is a central element, so it commutes with $e_t$ and the whole factorisation is at the level of scalars. The identity is exact for every connection, not only for a material one; the material case enters only when the two slots are read as the four-momentum.

**The pair.** Applying the operator twice and separating real and imaginary parts — which the free article does once and which the coupling does not disturb, because $\kappa^{\mathrm{kin}}_\mu$ is the only place the potential appears and it appears inside the same square — gives

$$
\boxed{\;
\bigl(\partial_{r'_t}S_{\tilde\Xi}-ϙ\,a'_t\bigr)^{2}-\bigl\lvert\nabla S_{\tilde\Xi}+ϙ\vec A\bigr\rvert^{2}
=m^{2}c^{2}-\hbar^{2}\frac{\Box_\Phi r}{r}\;}
$$
$$
\boxed{\;
\nabla\cdot\Bigl(\rho_{\mathrm{num}}\bigl(\nabla S_{\tilde\Xi}+ϙ\vec A\bigr)\Bigr)
-\frac{\partial}{\partial r'_t}\Bigl(\rho_{\mathrm{num}}\bigl(\partial_{r'_t}S_{\tilde\Xi}-ϙ\,a'_t\bigr)\Bigr)=0\;}
$$

with $\rho_{\mathrm{num}}=r^{2}$ and $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$. The first is the amplitude equation and the second the transport equation, and both are the parent's with the two substitutions of the introduction and with nothing else changed.

**The first equation is the mass shell with the mechanical momentum.** Writing $E=-\hbar c\,\partial_{r'_t}\theta_{\mathrm{pha}}$ and $\vec p=\hbar\nabla\theta_{\mathrm{pha}}$ and dividing by $\hbar^{2}c^{2}$,

$$
\frac{\bigl(E+ϙ c\,a'_t\bigr)^{2}}{c^{2}}-\bigl\lvert\vec p+ϙ\vec A\bigr\rvert^{2}=m^{2}c^{2}+2mQ_{\mathrm{qnt}},
\qquad
Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box_\Phi r}{r},
$$

so the sum $E+ϙca'_t$ is the mechanical energy and $\vec p+ϙ\vec A$ the mechanical momentum, and the mass shell is shifted by the quantum potential exactly as in the free article. The quantum potential is unchanged because it is $-\frac{\hbar^{2}}{2m}\Box r/r$ and $r$ is not touched by the coupling; in the logarithmic form of the free article it is a functional of $\rho_{\mathrm{num}}$ alone, and the density is the density.

**The second equation is the continuity of the mechanical current.** Dividing by $m$ and reading the two factors as the density and the current, it is

$$
\frac{\partial\rho_{\mathrm{chg}}}{\partial r'_t}+\nabla\cdot\vec j_{\mathrm{mech}}=0,
\qquad
\vec j_{\mathrm{mech}}=\frac{\rho_{\mathrm{num}}}{m}\bigl(\vec p+ϙ\vec A\bigr),
$$

with the temporal slot carrying $c\rho_{\mathrm{chg}}$ as in the free article. The current is the density times the mechanical four-velocity, and the statement is the same divergence form because the potential's contribution is a divergence of a product and not a source.

**What the coupling does not change.** The quantum potential, the density $r^{2}$, the sign of the charge, the nodal set, and the exactness of the equivalence between the pair and the equation. What it changes is the relation between the phase gradient and the momentum, and therefore everything that reads a momentum.

## The Current, the Vorticity and the Flux

**The current.** The free article's $\tilde J_\Phi=\rho_{\mathrm{num}}\tilde P_\Phi/m$ becomes

$$
\tilde J_\Phi=\frac{\rho_{\mathrm{num}}}{m}\,\tilde P^{\mathrm{mech}}_\Phi ,
\qquad
\tilde P^{\mathrm{mech}}_\Phi=i\,\frac{E+ϙ c\,a'_t}{c}\,e_t+\bigl(\vec p+ϙ\vec A\bigr),
$$

and it is gauge invariant: the phase's shift and the potential's shift cancel inside each component, which is the chart's form of the element companion's statement that every derivative in the current is covariant. The free current was not gauge invariant, and the coupling repairs that. It does not repair the sign: on the negative-frequency branch the temporal component is negative, and the positive definiteness of $\rho$ is exactly as absent as it was.

**The vorticity.** The free flow is the gradient of the action and is therefore irrotational. The coupled flow is not:

$$
\nabla\times\bigl(\vec p+ϙ\vec A\bigr)=\nabla\times\nabla S_{\tilde\Xi}+ϙ\nabla\times\vec A=ϙ\,\vec B ,
$$

exactly, with no approximation and no quantum correction. So the mechanical flow's vorticity is the magnetic field times the coupling, and the statement "the flow is a gradient" becomes "the flow is a gradient plus the vector potential": the free article's irrotationality is the statement $\vec B=0$, and it is not a property of the scalar field but a property of the connection it is coupled to.

**The flux and the circulation.** Integrate the relation around a closed loop:

$$
\oint\bigl(\vec p+ϙ\vec A\bigr)\cdot\mathrm{d}\vec l
=\oint\vec p\cdot\mathrm{d}\vec l+ϙ\oint\vec A\cdot\mathrm{d}\vec l
=2\pi\hbar\,n+ϙ\,\Phi_B ,
$$

the first term because $\vec p=\hbar\nabla\theta$ is a gradient and its circulation is quantized in units of $2\pi\hbar$, the second because the circulation of the vector potential is the magnetic flux through the loop. The mechanical circulation is therefore quantized *up to the flux*, which is the chart's exact statement of the flux-quantization and Aharonov–Bohm structure: a loop that encloses flux $\Phi_B$ has a mechanical circulation shifted by $ϙ\Phi_B$, and the shift is visible to the phase even where the field strength vanishes on the loop.

**What the chart shows here that the element form does not.** The element form's current is a bilinear and its gauge invariance is a cancellation between two terms. The chart's current is the density times a four-vector, its gauge invariance is a cancellation inside one component, and its vorticity is one curl. The three statements are the same statement, and the chart is the one that exhibits the vorticity, because the vorticity is a statement about a vector field and the chart is where the vector field is written.

## What the Chart Cannot Carry

**The other element equation.** The element companion distinguishes two coupled equations, $\Box_{\mathrm{gco}}\tilde\Xi=k_m^{2}\tilde\Xi$ and $\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}\tilde\Xi=k_m^{2}\tilde\Xi$, which agree in the free theory and differ by the curvature. The chart's pair is the chart of the first. The second's residual in the chart is

$$
\tilde\Xi^{-1}\Bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}-k_m^{2}\Bigr)\tilde\Xi
=\tilde\Xi^{-1}\Bigl(\Box_{\mathrm{gco}}-k_m^{2}\Bigr)\tilde\Xi
+\frac{i\,ϙ}{\hbar}\,\tilde\Xi^{-1}\tilde F\,\tilde\Xi ,
$$

and the second term is the field strength conjugated by the field.

**Why the conjugation matters.** In the algebra $\tilde F$ is a pure vector, and its four brackets are one type. Conjugating it by the field changes its type: $\tilde\Xi^{-1}\tilde F\tilde\Xi$ is a general element, whose components in the bracket basis are all four brackets in general, because the conjugation by $\tilde U_{\Psi,\mathrm b}$ mixes the Hermitian and the real-vector directions and the central phase does not undo the mixing. So the curvature term, which is one bracket in the element form, is four brackets in the chart, and a two-function pair cannot represent it.

**The honest conclusion.** The chart carries the coupled theory exactly when the curvature term is absent or when it is projected away, and those are the same condition: the chart carries the component equation, whose curvature term is zero by construction, and it cannot carry the algebra's equation, whose curvature term is the obstruction. This is the polar face of the element companion's prohibition: a central field is forbidden wherever the field strength is nonzero, and a two-function chart is a central field's chart.

**What the chart does carry for a general element.** The component equation itself, with a general element and a general connection. The covariant bracket is $\mathcal A_\mu+\frac{iϙ}{\hbar}A_\mu$, the frame density is $\tilde\Xi^{*}\tilde\Xi$, the kinetic Lagrangian is $\mathrm{Sc}\big[\tilde\Xi^{*}\tilde\Xi\,\mathcal A^{\mathrm{gco}}_\mu(\mathcal A^{\mathrm{gco}}_\mu)^{*}\big]$, and the eight parameter equations are the Jacobian image of the component equation, which is exact because the word is a bijection with a smooth inverse. No constraint appears and no multiplier is needed, because the parameterisation of the units is exact; the two-function pair is a restriction of this chart and not a different chart. The variational companion computes the metric of the eight-parameter chart; this article's subject is the two-function pair, which is the central case and the constant-polarization case.

## What the Chart Shows and What It Hides

**Shows.**

- The count: the connection enters as one central scalar per slot and therefore touches two of the four brackets, with the temporal slot real and the spatial slots imaginary.
- The one substitution: $\hbar cP_t=E+ϙca'_t$ and $\hbar\vec P=\vec p+ϙ\vec A$, the two classical replacements in one element, with the bracket's temporal coefficient equal to $-iP_t$.
- The gauge transformation as the translation of one coordinate, exact infinitesimally.
- The pair of equations as the parent's pair with the mechanical momentum and the same quantum potential.
- The vorticity, $ϙ\vec B$, and the circulation, $2\pi\hbar n+ϙ\Phi_B$: the two statements that the coupling changes the qualitative character of the flow rather than only its numbers.

**Hides.**

- The fourfold multiplicity. The chart describes one coefficient, and the constant polarization is the only case in which four coefficients share one phase; the multiplicity is a constant factor the chart does not see.
- The algebra's second equation. Its curvature term is a general element in the chart, so the chart cannot represent it and the element form is the place where it is written.
- The field strength. $\tilde F$ does not appear in the pair at all, because the pair is the chart of the component equation, whose only use of the connection is the four-momentum shift. The chart therefore *hides the very object that separates the two equations*, and that is the sharpest statement of what a coordinate system can and cannot show.

**The honest ledger.** The chart is sharper about the coupling: one additive term, two bracket types touched, one substitution, one curl. The element form is sharper about the algebra: the carrier, the closure, the two equations and the curvature. Neither is simpler; the chart is *the place where the coupling looks like classical mechanics*, and the element form is the place where it looks like a derivative.

## Open Questions

**Whether the curvature term's chart components have a closed form.** The conjugation $\tilde\Xi^{-1}\tilde F\tilde\Xi$ is one product of three elements, and its eight components in the bracket basis are not displayed here. Whether they factorise into a scale part, a phase part and a frame part — and whether the frame part is the projection of the field strength on the boost axis, as the free article's four-bracket expansion suggests — is not settled.

**Whether the constant-polarization case is the whole of the chart's reach.** The article uses the fact that a constant polarization factors through the central connection, and it uses the central field as the two-function case. Whether an intermediate case exists — a polarization that varies on a scale slow compared with the phase, so that its derivatives enter at a different order — is the chart's version of a WKB question and is not attempted.

**The operator setting.** The article treats the connection as an external field with a varying profile but keeps the amplitude and the action as the primary objects; the operator setting, in which the equation is a PDE for a field, is the standard quantum-hydrodynamics problem with a magnetic field. Whether the chart's vorticity statement survives there with $\vec B$ a function, and whether the flux quantization becomes a statement about the field's nodal lines, is not answered here.

## Summary

The coupled Klein–Gordon equation in polar variables is the free pair with the mechanical momentum. The word is the parent's, its domain is unchanged, and the connection enters the logarithmic derivative as one additive central term,

$$
\tilde\Xi^{-1}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi=\tilde\Xi^{-1}\partial_\mu\tilde\Xi+\frac{i\,ϙ}{\hbar}A_\mu ,
$$

so it touches the scale bracket in the temporal slot and the phase bracket in the spatial ones and cannot reach the boost or the rotor. For a central field the covariant derivative factors exactly, $\tilde\nabla_{\mathrm{gco},\mu}(re^{i\theta}e_t)=e^{i\theta}(\partial_\mu r+ir\kappa^{\mathrm{kin}}_\mu)e_t$, and the pair becomes

$$
\bigl(\partial_{r'_t}S_{\tilde\Xi}-ϙa'_t\bigr)^{2}-\bigl\lvert\nabla S_{\tilde\Xi}+ϙ\vec A\bigr\rvert^{2}=m^{2}c^{2}-\hbar^{2}\frac{\Box_\Phi r}{r},
\qquad
\nabla\cdot\bigl(\rho_{\mathrm{num}}(\nabla S_{\tilde\Xi}+ϙ\vec A)\bigr)-\frac{\partial}{\partial r'_t}\bigl(\rho_{\mathrm{num}}(\partial_{r'_t}S_{\tilde\Xi}-ϙa'_t)\bigr)=0 .
$$

The quantum potential and the density are unchanged; the momentum is not, the current is gauge invariant, the vorticity is $ϙ\vec B$, and the circulation is $2\pi\hbar n+ϙ\Phi_B$. The chart carries the component equation and cannot carry the algebra's equation, whose curvature term is a general element after conjugation by the field; that is the polar face of the element companion's prohibition on central fields in a nonzero field strength.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Xi=r e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The word: scale, central phase, boost, rotor |
| $r>0$ | Scale; $\rho_{\mathrm{num}}=r^{2}$ |
| $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ | Central phase; $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ is the action |
| $\theta_{\mathrm{rpd}}\ge0,\ \hat u_{\mathrm b}$ | Rapidity and axis of the boost |
| $\theta_{\mathrm{axr}}\in[0,2\pi),\ \hat u_{\mathrm r}$ | Angle and axis of the rotor |
| $\mathcal A_\mu=\tilde\Xi^{-1}\partial_\mu\tilde\Xi$ | The free bracket, four types |
| $\mathcal A^{\mathrm{gco}}_\mu=\mathcal A_\mu+\frac{iϙ}{\hbar}A_\mu$ | The covariant bracket |
| $\tilde A_\Phi=i a'_t e_t+\vec A$ | The connection; $a'_t$ and $\vec A$ real |
| $ϙ$ | The coupling |
| $\hbar cP_t=E+ϙca'_t$, $\hbar\vec P=\vec p+ϙ\vec A$ | The mechanical four-momentum |
| $\kappa^{\mathrm{kin}}_\mu=\partial_\mu\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}A_\mu$ | The covariant bracket's coefficient; $\kappa^{\mathrm{kin}}_t=-iP_t$ |
| $E=-\hbar c\,\partial_{r'_t}\theta_{\mathrm{pha}}$, $\vec p=\hbar\nabla\theta_{\mathrm{pha}}$ | The free four-momentum |
| $Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box_\Phi r}{r}$ | The quantum potential; unchanged by the coupling |
| $\vec j_{\mathrm{mech}}=\frac{\rho_{\mathrm{num}}}{m}(\vec p+ϙ\vec A)$ | The mechanical current |
| $\vartheta_{\mathrm{gau}}=ϙ\Lambda/\hbar$ | The gauge phase translation |
| $\tilde F$ | The field strength; one type in the algebra, four brackets in the chart |
| $k_m=mc/\hbar$ | The mass wave number |

## Further Reading

- [The Coupled Klein–Gordon Equation in Biquaternionic Form](the-coupled-klein-gordon-equation-in-biquaternionic-form.html), the element form this article re-coordinatises.
- [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the free word, the pair and the quantum potential.
- [The Variational Principle and the Coupled Klein–Gordon Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the action in the chart and the charge as a momentum.
- [The Variational Principle and the Klein–Gordon Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the free polar action and its metric.
- [The Coupled Proca Equation in Biquaternionic Polar Variables](the-coupled-proca-equation-in-biquaternionic-polar-variables.html), for the same type statement in the vector sector.
- [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the four-factor word and its parameter count.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localization of the central phase.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html), for the operator identity with the curvature.
- [The Klein–Gordon Fluid](the-klein-gordon-fluid.html), for the hydrodynamic reading of the pair.
- [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html), for the free flow's irrotationality that the coupling breaks.
- [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), for the quantization of the circulation in units of $2\pi\hbar$.
- [Landau Levels in Biquaternionic Form](landau-levels-in-biquaternionic-form.html), for the magnetic spectrum that the vorticity statement presupposes.
- E. Madelung, "Quantentheorie in hydrodynamischer Form", *Zeitschrift für Physik* **40** (1927), for the pair.
- Takehiko Takabayasi, "On the formulation of quantum mechanics associated with classical pictures", *Progress of Theoretical Physics* **8** (1952), for the relativistic pair.
