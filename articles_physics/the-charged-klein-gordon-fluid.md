# __The Charged Klein–Gordon Fluid: Vorticity Is the Field Strength__

## Introduction

**The coupling changes one property of the scalar fluid and leaves the rest, and the one it changes it changes exactly.** The free fluid is irrotational identically, and that is not an approximation: its velocity is a gradient, so its vorticity two-form vanishes for every solution. The charged fluid's vorticity is the field strength divided by the mass,

$$
\omega_{\mu\nu}=\frac{ϙ}{m}F_{\mu\nu},
$$

again identically, again for every solution, and with no quantum correction. **So the coupling does not give the scalar fluid a vorticity dynamics; it gives it a vorticity.** The free fluid had none because there was nothing to have; the charged fluid has one because the field strength is there, and in both cases the vorticity is read off the data and never transported. That distinction is the article's spine, and the two companion articles sharpen it from their own sides.

**The equation.** The coupled Klein–Gordon equation is the free one with covariant derivatives,

$$
\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}\tilde\Xi=k_m^{2}\tilde\Xi,
\qquad
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi,
\qquad
\tilde A_\Phi=i\,a'_t\,e_t+\vec A,
$$

with $a'_t$ and $\vec A$ real, so that $\tilde A_\Phi$ is an element of the material sector $\mathbb{B}_\Phi$ and its four coefficients are the scalar and the vector potential. **The connection is central per component in the abelian case**, which is the fact the whole article turns on: $\tilde\nabla_{\mathrm{gco},\mu}=\partial_\mu+\frac{iϙ}{\hbar}A_\mu$ is a central operator, it commutes with the word, and it adds one scalar to each bracket of the logarithmic derivative without disturbing the bracket's type.

**Three things are established.**

*First, the density is untouched and the velocity becomes mechanical.* The word is the free article's, $r\,e^{i\theta_{\mathrm{pha}}}\varepsilon$, and the scale is still $r$, so $\rho_{\mathrm{num}}=r^{2}$. What the coupling changes is the momentum the phase rate names: the phase gradient is replaced by $\partial_\mu S_{\tilde\Xi}+ϙA_\mu$, and the velocity the fluid carries is that over the mass. The free velocity was a gradient and was not gauge invariant; the mechanical velocity is not a gradient and is gauge invariant.

*Second, the vorticity becomes the field strength.* Because the mechanical one-form is a gradient plus a potential, its exterior derivative is the potential's alone, and that is $ϙF$. Everything the free article proved about the vanishing of $\omega$ survives as the statement $\vec E=\vec B=0$.

*Third, the force becomes the Lorentz force and the quantum force stays.* The gradient of the coupled mass shell gives the free article's acceleration law with one term added, and the added term is $-ϙ(\vec E+\vec v\times\vec B)$ in the spatial slots. The quantum potential is in the equation exactly as it was, because it depends on $r$ and its curvature and on nothing else.

**What is not here.** No new solution, no new prediction, no new particle. The article's subject is the fluid reading of the standard minimally coupled scalar field, and its work is to say which of the free article's properties are properties of the scalar field and which are properties of the connection it is coupled to. The answer is short: the irrotationality and the gauge non-invariance of the velocity are the connection's, and the density, the quantum stress, the absence of an equation of state and the nodal set are the field's.

**Position in the block.** This article is the charged companion of [The Klein–Gordon Fluid](the-klein-gordon-fluid.html). Its siblings are [The Charged Spin Fluid](the-charged-spin-fluid.html) and [The Charged Proca Fluid](the-charged-proca-fluid.html), and the three are compared side by side in §*The Three Charged Fluids*. The free article's own table of the three free fluids is in that article and in the two free companions, and the present table is its charged counterpart.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; $i$ is the central scalar imaginary; $^{*}$ is Hermitian conjugation and $^{\natural}$ quaternion conjugation; $\mathrm{Sc}$ is the coefficient of $e_t$ and $\mathrm{Tr}=2\,\mathrm{Sc}$. The material time is $r'_t=c\,t'$, the d'Alembertian is $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$, and $k_m=mc/\hbar$. The connection is $\tilde A_\Phi=i a'_t e_t+\vec A$ with $a'_t$ and $\vec A$ real, the coupling is $ϙ$, the action is $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$, and $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$. The pairing is $\mathrm{Sc}(\cdot^{*}\cdot)$ throughout.

## The Bracket the Connection Reaches

**The coupling enters the logarithmic derivative as one added central element, and the type table says where it can land.** Differentiating the word, dividing by it and adding the connection gives

$$
\tilde\Xi^{-1}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi
=\frac{1}{2}\frac{\partial\ln\rho_{\mathrm{num}}}{\partial R_\mu}
+i\Bigl(\frac{\partial\theta_{\mathrm{pha}}}{\partial R_\mu}+\frac{ϙ}{\hbar}A_\mu\Bigr)
+\tilde u_{\mathrm r}^{-1}\Bigl(\tilde U_{\Psi,\mathrm b}^{-1}\frac{\partial\tilde U_{\Psi,\mathrm b}}{\partial R_\mu}\Bigr)\tilde u_{\mathrm r}
+\tilde u_{\mathrm r}^{-1}\frac{\partial\tilde u_{\mathrm r}}{\partial R_\mu},
$$

and the four terms are the free article's four brackets with the connection's share inside the second. **The share is a central scalar in every slot, and a central scalar can produce neither a real vector part nor a Hermitian vector.** So it can add to the scale bracket and to the phase bracket and to nothing else.

| bracket | type | the connection's share |
| --- | --- | --- |
| $\tfrac12\partial_\mu\ln r^{2}$ | real central scalar | none |
| $i\partial_\mu\theta_{\mathrm{pha}}+\frac{iϙ}{\hbar}A_\mu$ | central imaginary, with a real part | the whole slot |
| $\tilde u_{\mathrm r}^{-1}(\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b})\tilde u_{\mathrm r}$ | Hermitian | none |
| $\tilde u_{\mathrm r}^{-1}\partial_\mu\tilde u_{\mathrm r}$ | real vector part | none |

**The third and fourth rows are rows of zeros on the central field, and that is why the scalar case is the clean one.** The boost has no rapidity to carry and the rotor no axis, so both frame brackets vanish identically and the connection has only the two central brackets to reach. **On the central field the coupling is therefore exactly a shift of the phase rate, and nothing else of it survives in the kinematics.**

**What that says in the fluid's letters.** The phase bracket names the momentum, so the shift of the bracket is a shift of the momentum and hence of the velocity:

$$
\tilde P^{\mathrm{mech}}_\Phi=\tilde P_\Phi+ϙ\tilde A_\Phi,
\qquad
\tilde P_\Phi=i\frac{E}{c}e_t+\vec p,
$$

with $E=-\hbar c\,\partial\theta_{\mathrm{pha}}/\partial r'_t$ and $\vec p=\hbar\nabla\theta_{\mathrm{pha}}$ the free readings. Slot by slot the shift is $E\mapsto E+ϙc\,a'_t$ and $\vec p\mapsto\vec p+ϙ\vec A$ — one substitution in one element, with the two signs the metric's and not a convention.

**The one-line reason, and the reason it matters for the fluid.** A central connection acts on the word as a whole, so it can move the phase and cannot reach inside the product $e^{i\theta_{\mathrm{pha}}}\varepsilon$ to change the branch. **The branch $\varepsilon$ is untouched by the coupling**, and that is the first of the article's negative results: the charge does not repair the sign of the charge density.

## The Density and the Velocity

**The marker density is unchanged, and the conserved density is now gauge invariant.** The word's scale is $r$ and $\rho_{\mathrm{num}}=r^{2}$ in both cases; the free article's $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ survives with the mechanical $\gamma$,

$$
c\,\rho_{\mathrm{chg}}=\frac{\rho_{\mathrm{num}}}{m}\bigl(E+ϙc\,a'_t\bigr),
\qquad
\gamma=-\frac{1}{c}\,V^{t},
$$

and the bracket is invariant under $\theta_{\mathrm{pha}}\mapsto\theta_{\mathrm{pha}}+ϙ\Lambda/\hbar$, $\tilde A_\Phi\mapsto\tilde A_\Phi-\tilde\nabla_\Phi\Lambda$, because the two shifts cancel inside it. **The free current was not gauge invariant and the coupling repairs that**; the repair is a cancellation inside one bracket, where the element form's is a cancellation between two terms of a bilinear.

**The velocity is the mechanical one and it is the only velocity the fluid has.** Write

$$
\tilde V_\Phi=\frac{1}{m}\tilde P^{\mathrm{mech}}_\Phi,
\qquad
\tilde P^{\mathrm{mech}}_\Phi\tilde P^{\mathrm{mech}\natural}_\Phi=-m^{2}c^{2}-2mQ_{\mathrm{qnt}},
\qquad
\tilde V_\Phi\tilde V_\Phi^{\natural}=-c^{2}-\frac{2Q_{\mathrm{qnt}}}{m}.
$$

The last display is the free article's statement with the potential folded in, and it says what it said before: **the four-velocity is a unit exactly where the quantum potential vanishes**, and nowhere else. The coupling does not change that and cannot: a shift of the momentum cannot change the relation between the momentum's norm and the mass.

**What changes is that the velocity is no longer a gradient.** The free velocity was $\tilde\nabla_\Phi S_{\tilde\Xi}/m$, so its one-form was closed by the symmetry of second derivatives and nothing else. The mechanical velocity is

$$
\tilde V_\Phi=\frac{1}{m}\Bigl(\tilde\nabla_\Phi S_{\tilde\Xi}+ϙ\tilde A_\Phi\Bigr),
$$

whose one-form is closed iff the potential is pure gauge. **The free article's irrotationality is therefore the statement $F=0$**, and it is a statement about the connection the field is coupled to rather than about the field.

**A gauge transformation moves the two terms and not the sum.** The angle and the potential shift in opposite directions, the mechanical momentum is fixed, and the velocity with it. So the velocity is an observable of the chart, which the free velocity was not. The free article records that its current was not gauge invariant; this one is, and the reason is that the velocity now carries the potential the phase used to leave behind.

## The Vorticity

**The vorticity is the field strength over the mass, and the computation is one line.** With $\tilde V_\Phi=\tilde P^{\mathrm{mech}}_\Phi/m$ and $\tilde P^{\mathrm{mech}}_\Phi=\tilde\nabla_\Phi S_{\tilde\Xi}+ϙ\tilde A_\Phi$,

$$
\omega_{\mu\nu}=\partial_\mu V_\nu-\partial_\nu V_\mu
=\frac{1}{m}\Bigl(\partial_\mu\partial_\nu S_{\tilde\Xi}-\partial_\nu\partial_\mu S_{\tilde\Xi}\Bigr)
+\frac{ϙ}{m}\Bigl(\partial_\mu A_\nu-\partial_\nu A_\mu\Bigr)
=\frac{ϙ}{m}F_{\mu\nu}.
$$

The first bracket vanishes because the action is a function and not a one-form, and the second is the definition of the field strength. **No term is dropped, no order is taken, and no quantum correction appears**: the quantum potential enters the *norm* of the velocity and not its curl, because it is a function of the density and the density cancels out of the velocity.

**So the charged scalar fluid is irrotational exactly where the field strength vanishes.** The free article's "the vorticity vanishes identically, off the nodes" is the case $\vec E=\vec B=0$ of this display, and its qualifier is unchanged: the velocity is defined wherever $r\ne0$, and the vorticity with it.

**The rank of the vorticity is the rank of the field strength, and that is a genuinely new ingredient.** A two-form on four dimensions has even rank, so $\omega$ has rank $0$, $2$ or $4$, and the rank is four exactly where the invariant $\vec E\cdot\vec B$ is non-zero, since $\det F$ is $(\vec E\cdot\vec B)^{2}$ up to the convention's factor. The check was run on three configurations and the vorticity matrix's singular values were taken:

| field strength | singular values of $\omega$ | rank |
| --- | --- | --- |
| $\vec E=0$, $\vec B=0$ | $0,\ 0,\ 0,\ 0$ | $0$ |
| $\vec E=(0.7,0,0)$, $\vec B=0$ | $0.7,\ 0.7,\ 0,\ 0$ | $2$ |
| $\vec E=(0.7,0,0)$, $\vec B=(0.9,0,0)$ | $0.921,\ 0.921,\ 0.632,\ 0.632$ | $4$ |

**The third row is the article's sharpest single statement about the rest of the block.** The spin companion proves that its *vorticity proper* — the part that annihilates the velocity — is rank two for every solution, a two-form on the three dimensions of the rest space, and that only its *raw* derivative reaches rank four, and only through the acceleration. **The scalar fluid's vorticity is the field strength itself.** It is rank four wherever $\vec E\cdot\vec B\ne0$, with no acceleration and no frame, and its rank is a property of the connection rather than of the flow. So the two fluids reach the rank-four row of [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html) by different routes, and only one of them reaches it with its vorticity.

**The rung below states the same identity with no qualifier and with a lower rank.** [The Charged Schrödinger Fluid](the-charged-schrodinger-fluid.html) has $\nabla\times\vec v=ϙ\vec B/m$ exactly, because its velocity is a three-velocity and not a normalised four-vector, and there the rank is two for every field: a non-relativistic velocity has no time component, so the electric half of $F$ has nowhere to enter the vorticity. The two statements together measure what the second order of the equation adds — the normalisation of the velocity and the mixing of $\vec E$ and $\vec B$ — and both are absent one rung down.

**What the vorticity is not, in this fluid.** It is not a dynamical variable: it is a function of the connection and of nothing else, and the fluid carries no vorticity equation, no Helmholtz transport and no conserved helicity. It is also not a spin, because the scalar sector has no spin: the word's last factor is the branch, and a branch is not an orientation.

## The Circulation

**The circulation is the canonical winding plus the flux, and the two terms have different origins.** Integrate the mechanical one-form around a closed loop:

$$
\oint\tilde P^{\mathrm{mech}}\cdot\mathrm{d}\vec l
=\oint\vec p\cdot\mathrm{d}\vec l+ϙ\oint\vec A\cdot\mathrm{d}\vec l
=2\pi\hbar\,n+ϙ\,\Phi_B,
$$

the first term because $\vec p=\hbar\nabla\theta_{\mathrm{pha}}$ is a gradient and the phase's single valuedness makes its circulation an integer multiple of $2\pi\hbar$, the second because the circulation of the vector potential is the magnetic flux through any surface the loop bounds.

**The canonical quantisation is untouched and the mechanical one is shifted.** [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html) proves that a loop linking a nodal line carries $\oint\vec p\cdot\mathrm{d}\vec l=2\pi\hbar n$, and that the circulation of $\vec p/m$ is $hn/m$. That statement is unchanged, because it is a statement about the angle and the nodes and neither the coupling nor the connection enters it. **What the coupling changes is the fluid's circulation, and it changes it by the flux**: $\omega=ϙF/m$, so the loop integral of the velocity is $2\pi\hbar n/m+ϙ\Phi_B/m$.

**The flux term survives where the field strength vanishes on the loop.** A loop encircling a solenoid has $\vec B=0$ on itself and $\Phi_B\ne0$ through it, so its mechanical circulation is shifted while its vorticity is zero at every point it passes. **The fluid's circulation is therefore not determined by the vorticity it carries**, because the potential is not determined by the field. The free article's identification of circulation with the winding of one function is exactly what the coupling breaks, and the break is topological and not dynamical.

**What that earns and what it does not.** The relation $2\pi\hbar n+ϙ\Phi_B$ is the flux-quantisation condition of a charged condensate, and the free article refuses the superfluid identification on the ground that the object is one element and not a condensate. **The charged fluid earns the kinematic half of that identification and not the dynamical half**: its vorticity is locked to the flux and its circulation is quantised up to the flux, and it still has no order parameter, no condensate and no second sound. The analogy is with a charged fluid carrying its own field, which is the same conclusion the Proca article of the block reaches from the other end.

## The Force

**The gradient of the coupled mass shell gives the Lorentz force and the free quantum force, and the two terms come from the one gradient.** The mass shell is

$$
\tilde P^{\mathrm{mech}}\cdot\tilde P^{\mathrm{mech}}=-m^{2}c^{2}-2mQ_{\mathrm{qnt}},
$$

and differentiating it and contracting with the velocity gives, in four-vector form,

$$
m\frac{\mathrm{d}V_\mu}{\mathrm{d}\tau}=-ϙF_{\mu\nu}V^{\nu}-\partial_\mu Q_{\mathrm{qnt}},
$$

whose spatial slots are the display a reader expects:

$$
\frac{\mathrm{d}\vec p^{\mathrm{mech}}}{\mathrm{d}t}
=-ϙ\bigl(\vec E+\vec v\times\vec B\bigr)-\gamma^{-1}\nabla Q_{\mathrm{qnt}},
\qquad
\vec p^{\mathrm{mech}}=\vec p+ϙ\vec A .
$$

**The sign of the four-vector form is the metric's and the spatial form is the check.** With a lower index, the Lorentz term is $-ϙF_{\mu\nu}V^{\nu}$, whose spatial slots are $-ϙE_i\gamma-ϙ(\vec v\times\vec B)_i\gamma$; dividing by the $\gamma$ that converts $\mathrm{d}/\mathrm{d}\tau$ to $\mathrm{d}/\mathrm{d}t$ leaves the display above with both of its sub-terms at order zero in $\gamma$. **With $ϙ$ the negative of the electric charge the display reads $q(\vec E+\vec v\times\vec B)-\gamma^{-1}\nabla Q_{\mathrm{qnt}}$**, which is the standard force on a charge $q$: the sign is the coupling's, and the mass shell is what fixes it, because the potential energy is $-ϙ\varphi$. The free article's $-ϙ\to0$ case is its own acceleration law, term for term.

**The check was carried out symbolically and it is exact.** Taking an arbitrary action $S$ and an arbitrary potential $A_\mu$ in one time and one space dimension, defining $Q_{\mathrm{qnt}}$ by the mass shell above and $V=\tilde P^{\mathrm{mech}}/m$, the identity

$$
V^{\nu}\partial_\nu P^{\mathrm{mech}}_\mu+ϙF_{\mu\nu}V^{\nu}+\partial_\mu Q_{\mathrm{qnt}}=0
$$

was verified to hold in both slots with no residual term. Each of the three terms has a reading: the first is the acceleration, the second is the Lorentz force with the sign the metric gives a lower index, and the third is the free article's quantum gradient, unchanged.

**The Lorentz force is a force and not a stress, and that is the structural statement.** A flow whose only force is a gradient has no transverse force and therefore generates no vorticity; the free article says exactly this, and it is why the free scalar fluid cannot rotate. **The coupling adds a transverse force without adding a stress**, because the field is external: the quantum stress is computed from $r$ and its derivatives, the connection does not enter it, and the field's own stress belongs to the field. So the charged scalar fluid has a prescribed vorticity, a transverse force, and still one stress.

**The quantum potential is untouched, and the reason is worth stating.** $Q_{\mathrm{qnt}}=-\hbar^{2}\Box_\Phi r/(2mr)$ depends on the amplitude and its second derivatives. The coupling shifts the momentum and not the amplitude; the amplitude equation is the mass shell with the mechanical momentum and the same curvature term. So the third-order character of the force survives, and with it the free article's "no equation of state", which this article does not restate because nothing in it moves.

## The Sign, the Threshold and the Klein Paradox

**The potential moves the zero of the mechanical energy, and the charge density follows it.** On the negative-frequency branch $E<0$, and the bracket $E+ϙc\,a'_t$ changes sign where $|ϙc\,a'_t|=|E|$. **On a fixed branch the charge density can therefore be positive at large potential and negative at small**, and the surface where it vanishes is where the negative-frequency solution has become a positive-charge one.

**That surface is the pair-threshold, and the article claims the kinematics and no more.** The number density $r^{2}$ never changes sign and never vanishes there; what changes sign is the charge density, which is the number density times the mechanical phase rate. So the free article's "two defects are one defect" — the sign of the charge and the indefiniteness of the density — is unchanged in structure: the coupling moves the boundary and does not remove it. **The field theory of the boundary, in which a negative-frequency branch stopped by a sufficiently strong electric potential is a pair-producing configuration, is [The Klein Paradox in Biquaternionic Form](the-klein-paradox-in-biquaternionic-form.html)'s subject**, and the present article's contribution is the fluid statement: a fluid whose charge density is a positive number density times a mechanical phase rate has a charge-sign boundary wherever that rate vanishes, and a constant potential translates the boundary without abolishing it.

**The gauge transformation does not move the boundary.** The bracket is gauge invariant, so the surface $E+ϙc\,a'_t=0$ is a gauge-invariant set, and the worry that the threshold is a gauge artefact is answered in one line.

## The Reverse Map

**The free article's class was irrotational barotropic flows with a Korteweg stress, and the charged fluid has left that class.** Irrotationality was one of the four items of the criterion and the mechanical velocity is not a gradient. **What replaces the item is a pair of conditions**: the vorticity is closed, which is automatic for a field strength, and its periods are the fluxes, which is §*The Circulation*'s formula. The class the charged reverse map is defined on is therefore

$$
\Bigl\{(\rho,S_{\tilde\Xi},A)\;:\;\rho>0,\ \ \tilde V_\Phi=\tfrac{1}{m}\bigl(\tilde\nabla_\Phi S_{\tilde\Xi}+ϙ\tilde A_\Phi\bigr),\ \ \mathrm{d}\bigl(m\tilde V_\Phi\bigr)=ϙF\Bigr\},
$$

and the third member is not a condition on the flow alone: **the flow and the connection are one datum, and neither determines the other.** That is what the coupling does to the correspondence, and it is a change of the domain and not of the strength of either arrow.

**The two arrows are still of different strengths, and the asymmetry is now a quotient.** The field gives a density, an action and a mechanical momentum, exactly and with no conditions. The reverse direction takes a positive density, an action and a connection and returns $\tilde\Xi=r e^{iS_{\tilde\Xi}/\hbar}\varepsilon$, but two triples differing by a gauge transformation give the same field. **The map is well defined on gauge orbits and not on triples**, and the free article's bijection on the $N$-regular set is the $ϙ=0$ slice of a bijection on orbits. Nothing is lost and nothing is gained: the count of the field's data is unchanged, because the connection was never the field's datum.

**A reader's objection, and the answer.** The objection is that the mechanical velocity is defined as the canonical one plus the potential, so "the vorticity is the field strength" is a definition and not a result. The objection is right about the definition and wrong about the content: what the display fixes is that the fluid's vorticity is *not an independent variable*, and that is a statement about the fluid and not about the letters. A free fluid could have had a vorticity of its own and did not; this one has the field's and cannot have another.

## The Properties, Listed

**Twelve statements, each one line, and each with its reason. This is what the charged scalar fluid is.**

1. **The word is unchanged and the coupling is a shift, not a parameter.** The scale, the angle and the branch; the connection enters the phase bracket, and the count of the field's data is the free article's.
2. **The marker density is $r^{2}$ and the conserved density is the mechanical phase rate times it.** $c\rho_{\mathrm{chg}}=\rho_{\mathrm{num}}(E+ϙca'_t)/m$, and it is gauge invariant, which the free one was not.
3. **The velocity is the mechanical momentum over the mass**, and it is the only velocity the fluid has. It is a unit exactly where $Q_{\mathrm{qnt}}$ vanishes, as before.
4. **The flow is irrotational exactly where the field strength vanishes.** $\omega=ϙF/m$, exact, with no quantum correction.
5. **The vorticity's rank is the field strength's**: $0$, $2$ or $4$, and $4$ exactly where $\vec E\cdot\vec B\ne0$. No free fluid of the block reaches rank four with its vorticity proper.
6. **The circulation is $2\pi\hbar n+ϙ\Phi_B$**, and the flux term survives on a loop where the field strength vanishes.
7. **The canonical circulation is untouched.** $\oint\vec p\cdot\mathrm{d}\vec l=2\pi\hbar n$ still comes from the nodes and the coupling does not enter it.
8. **The force is the Lorentz force plus the free quantum gradient**, and the free acceleration law is the $ϙ=0$ case of the coupled one, term for term.
9. **There is no new stress.** The quantum stress is the free article's Korteweg stress, unchanged, and the field's stress is the field's.
10. **There is still no equation of state.** $Q_{\mathrm{qnt}}$ carries two derivatives of $\ln r$, and no function of the density's value produces it.
11. **The charge density's sign can change on a fixed branch**, at $|ϙca'_t|=|E|$, and the number density's cannot: the boundary moves and does not vanish.
12. **The degenerate set is unchanged.** $r=0$, codimension two, and the connection cannot reach it because the connection cannot reach the scale.

## The Three Charged Fluids

**The three relativistic charged articles can be put side by side, and the table is the shortest statement of what the charge does to each.** The table is the same in all three; what changes from one to the next is which column is the article's own. **The block has a fourth charged fluid at the rung below**, [The Charged Schrödinger Fluid](the-charged-schrodinger-fluid.html), and it differs from the charged scalar column in two rows only: its velocity is a three-vector and not a four-vector, so the unit row does not apply to it, and its vorticity is a three-vector curl, so its rank is $2$ wherever the field is present and never $4$.

| | charged scalar | charged spin | charged vector |
| --- | --- | --- | --- |
| the carrier | a complex function: two parameters | a word of four factors: eight parameters | the same word: eight parameters |
| the density | $\rho_{\mathrm{num}}=\lvert\Xi\rvert^{2}$ | $\rho$, read from the word | the scale, which is not a norm |
| the velocity | $\tilde P^{\mathrm{mech}}/m$ | the frame, $ic\tilde U_{\Psi,\mathrm b}^{-2}$ | the field's direction, $\tilde A/r$ |
| is it a unit? | only where the quantum potential vanishes | always, $\langle\tilde V_\Phi\rangle_\natural=-c^{2}$ | its boost is; the element is not a four-vector |
| the vorticity | the field strength, $ϙF/m$ | the frame's gradient, and not $ϙF/m$ | not established; the free case's is $F$ minus a radial term |
| the vorticity's rank | $0$, $2$ or $4$ | $2$ for the proper part | the free case's is $2$ |
| the loop invariant | $2\pi\hbar n/m+ϙ\Phi_B/m$ | a Lorentz transformation times a phase | for $ϙ=0$ an integer; for $ϙ\ne0$, not known |
| the force | the Lorentz force, plus a quantum potential | the Lorentz force, and no torque | the covariant divergence, self-acting |
| the stress | the quantum potential is in it; no EOS | the antisymmetric part is in it; no EOS | its own field strength is in it; stiff on $F=0$ |
| the degenerate set | $r=0$, codimension two | $r=0$, codimension two | $r=0$; the free case's lightlike wall is gone |
| what the charge does | turns the vorticity into the field strength | pushes and does not torque | doubles the carrier and opens the constraint |

**This article's column is the first, and it is the only column where the charge changes the vorticity's nature.** That one fact explains four rows at once: the vorticity is a field strength rather than a frame gradient or the curl of a direction, the circulation is a winding plus a flux, the force is a Lorentz force rather than a stress divergence, and the stress is untouched because the field is external. **The scalar fluid is the one case in which the coupling is pure kinematics.**

**The row that separates it from the other two is the velocity's.** Here the velocity is the mechanical momentum over the mass, a gradient plus a potential, so $\mathrm{d}V$ is exactly $F$. In the spin case the velocity is the frame, which is a unit and not a gradient, so $\mathrm{d}V$ carries the frame's logarithmic derivative and no $F$ at all; in the vector case the velocity is the field's own direction, and the free case's $\mathrm{d}V$ is $F$ minus a radial term while the charged case's is not computed in this block. **Three velocities, three curls, and only one of them is the field strength.**

**Two rows are the same in all three columns and deserve a sentence.** Every one of the three fluids has a degenerate set at $r=0$ and none of them has an equation of state; those are properties of the word and not of the connection, which is why the three articles state them once and do not re-derive them.

## What the Charge Does to the Correspondence

**The correspondence still has three steps, and the charge changes the second.** The word is exact; the reverse map is defined on a class; membership of that class is the extra structure that makes the fluid a medium rather than a relabelling of a wave. The free article's version of the three steps is in its own §*The Correspondence*; here is the charged version.

**The forward arrow is unchanged and exact.** Any nowhere-zero solution of the coupled equation gives a positive density, an action and a mechanical momentum, by the polar substitution, and the substitution is a bijection on the $N$-regular set. The connection is a datum of the equation and not of the solution, so it costs the arrow nothing.

**The reverse arrow now takes three data and returns one field.** Given $(\rho,S_{\tilde\Xi},A)$ with $\rho>0$, the field is $r e^{iS_{\tilde\Xi}/\hbar}\varepsilon$, and it solves the coupled equation iff the pair of §*The Force* and §*The Vorticity* holds. **The extra structure is therefore no longer a constitutive law internal to the fluid; it is a connection external to it**, and the classical object it names is a charged fluid with a prescribed field.

| | the word's data | what the reverse map needs beyond it | the medium it makes |
| --- | --- | --- | --- |
| charged scalar | $r$, $\theta_{\mathrm{pha}}$ | the energy equation, which is the Hamiltonian | a charged Madelung fluid |
| charged spin | eight parameters | the connection, and a closure of the frame's transport | a charged Cosserat medium |
| charged vector | the same eight | the connection, which is the field itself | a self-acting compressible medium |

**The free correspondence's three kinds of extra structure were the three ways a medium exceeds a dust; the charged correspondence's third column names what exceeds the dust now: a field.** That is the sense in which the charge adds no fluid of a fourth kind but adds a fourth kind of datum, and the table's first row is this article's.

**What the correspondence supports and what it does not.** It supports the claim that the coupled Klein–Gordon equation is the equation of motion of a recognizable classical medium, and it supports the twelve properties of §*The Properties, Listed* item by item. It does not support the claim that the charged fluid is a superfluid, that its vorticity is a dynamical variable, or that its density is positive definite: the first is refused in §*The Circulation*, the second in §*The Vorticity*, and the third is the free article's defect, which the charge moves and does not repair.

## What Is Established and What Is Interpretation

**Established.** The type table, and with it the statement that the coupling can reach the scale and the phase brackets and no others. The mechanical momentum as the canonical one plus the potential, and the velocity as that over the mass. The gauge invariance of the velocity, the charge density and the current, from a cancellation inside one bracket. The vorticity as $ϙF/m$, exactly, with the rank statement and the three-row singular-value table. The circulation as $2\pi\hbar n+ϙ\Phi_B$, and the survival of the flux term where the field strength vanishes on the loop. The acceleration law as the free one plus the Lorentz term, with the identity verified symbolically in both slots. The invariance of the quantum potential, the Korteweg class of the stress, and the absence of an equation of state. The movement of the charge-sign boundary with the potential, and its gauge invariance. The reverse map's domain as a set of triples, well defined on gauge orbits.

**The comparison is established as a table and not as a claim.** Every entry of §*The Three Charged Fluids* is a statement proved in one of the three charged articles, and the entries are what make the comparison systematic: the word's count, the density, the velocity, the vorticity's form and rank, the circulation, where the charge lands, the stress, the equation of state, the compressibility, the degenerate set, and what closes the system.

**Interpretation.** That the mechanical velocity *is* a fluid's velocity rather than a rewriting. The warrant is the count, the types and the free article's reading, and the coupling does not touch the warrant. That the flux-quantisation relation is the kinematic half of superconductivity is a reading of the analogy, supported by the exactness of the circulation formula and not proved by it.

**Not claimed.** It is not claimed that the charged fluid has a vorticity dynamics: its vorticity is a function of the connection and obeys no transport law. It is not claimed that it is a superfluid, a condensate, or a plasma in the dynamical sense. It is not claimed that the quantum stress is a pressure, or that the charge repairs the sign of the charge density. It is not claimed that the connection supplies the missing closure of the general field: the general field's brackets are underdetermined in the free case, and the coupling, being central, does not change that.

## Summary

The charged Klein–Gordon equation is $\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}\tilde\Xi=k_m^{2}\tilde\Xi$ with $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$, and the word is the free article's $r e^{i\theta_{\mathrm{pha}}}\varepsilon$ substituted into it.

The connection is central per component, so it merges with the scale and the phase brackets and cannot reach the branch. On the central field the kinematics is therefore exactly a shift of the phase rate, and the shift is the classical substitution in one element: $\tilde P^{\mathrm{mech}}_\Phi=\tilde P_\Phi+ϙ\tilde A_\Phi$.

The density is $r^{2}$ and the conserved density is the mechanical phase rate times it, gauge invariant where the free one was not. The velocity is $\tilde P^{\mathrm{mech}}/m$, a unit exactly where the quantum potential vanishes and no longer a gradient.

The vorticity is $ϙF/m$ exactly, so the fluid is irrotational exactly where the field strength vanishes. Its rank is $0$, $2$ or $4$, and four exactly where $\vec E\cdot\vec B\ne0$, which is the rank no free fluid of the block reaches with its vorticity proper. The circulation is $2\pi\hbar n+ϙ\Phi_B$, and the flux term survives where the field strength vanishes on the loop.

The force is the Lorentz force plus the free quantum gradient, $\mathrm{d}\vec p^{\mathrm{mech}}/\mathrm{d}t=-ϙ(\vec E+\vec v\times\vec B)-\gamma^{-1}\nabla Q_{\mathrm{qnt}}$, and it comes from the one gradient of the coupled mass shell. The quantum potential, the Korteweg stress and the absence of an equation of state are untouched, because the field is external and the amplitude is untouched.

The charge-sign boundary moves with the potential at $|ϙca'_t|=|E|$ and is gauge invariant, and the number density's sign never moves. The degenerate set is $r=0$, as it was. The reverse map's domain is now a set of triples — density, action, connection — and it is well defined on gauge orbits rather than on triples.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon$ | The word; the free article's, unchanged by the coupling |
| $r>0$ | Scale; $\rho_{\mathrm{num}}=r^{2}$ |
| $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ | The phase coordinate; moves under a gauge transformation |
| $\varepsilon$ | The branch; untouched by the connection |
| $\tilde A_\Phi=i a'_t e_t+\sum_\eta A_\eta\vec e_\eta$ | The connection; $a'_t$ and $\vec A$ real, so $\tilde A_\Phi\in\mathbb{B}_\Phi$ |
| $\tilde\nabla_{\mathrm{gco},\mu}=\partial_\mu+\frac{iϙ}{\hbar}A_\mu$ | The covariant derivative; central per component |
| $ϙ$ | The coupling |
| $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ | The action |
| $\tilde P_\Phi=i\frac{E}{c}e_t+\vec p$ | The canonical momentum; $E=-\hbar c\,\partial_{r'_t}\theta_{\mathrm{pha}}$, $\vec p=\hbar\nabla\theta_{\mathrm{pha}}$ |
| $\tilde P^{\mathrm{mech}}_\Phi=\tilde P_\Phi+ϙ\tilde A_\Phi$ | The mechanical momentum; gauge invariant |
| $\tilde V_\Phi=\tilde P^{\mathrm{mech}}_\Phi/m$ | The four-velocity; $\tilde V_\Phi\tilde V_\Phi^{\natural}=-c^{2}-2Q_{\mathrm{qnt}}/m$ |
| $\rho_{\mathrm{chg}}$ | The conserved density; $c\rho_{\mathrm{chg}}=\rho_{\mathrm{num}}(E+ϙca'_t)/m$ |
| $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ | The field strength; $\det F$ is $(\vec E\cdot\vec B)^{2}$ up to a factor |
| $\omega_{\mu\nu}$ | The vorticity; $\omega=ϙF/m$ |
| $\Phi_B$ | The flux through a loop; $\oint\vec A\cdot\mathrm{d}\vec l$ |
| $Q_{\mathrm{qnt}}=-\hbar^{2}\Box_\Phi r/(2mr)$ | The quantum potential; untouched by the coupling |
| $k_m=mc/\hbar$ | The mass wave number |

## Further Reading

- [The Klein–Gordon Fluid](the-klein-gordon-fluid.html), the free companion, whose twelve properties these twelve answer.
- [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the word, the pair, the quantum potential and the nodal set.
- [The Variational Principle and the Klein–Gordon Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the action and the current in the chart.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html), for the central connection and the curvature.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localisation that produces the coupling.
- [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), for the winding the flux is added to.
- [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html), for the rank table this fluid fills differently.
- [The Equation of State and the Barotropic Condition](the-equation-of-state-and-the-barotropic-condition.html), for the criterion the charged fluid still fails.
- [The Klein Paradox in Biquaternionic Form](the-klein-paradox-in-biquaternionic-form.html), for the field theory of the charge-sign boundary.
- [The Charged Spin Fluid](the-charged-spin-fluid.html) and [The Charged Proca Fluid](the-charged-proca-fluid.html), the two companions.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge University Press, 2003), for the covariant derivative in geometric algebra.
- Alexander Altland and Ben Simons, *Condensed Matter Field Theory* (Cambridge University Press, 2nd edition, 2010), for the charged condensate and the London response.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the minimally coupled scalar field and its stress tensor.
