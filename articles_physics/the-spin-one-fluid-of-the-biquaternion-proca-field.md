# __The Spin-One Fluid of the Biquaternion Proca Field__

## Introduction

**The Proca field's polar word gives a fluid, and the fluid is easier to read than either of the other two: the potential is the current, so the density is the norm of the field itself.** The word is [The Proca Equation in Biquaternionic Polar Variables](the-proca-equation-in-biquaternionic-polar-variables.html), and it is a *two*-factor word and not a four-factor one. A real four-vector has no phase, so the central angle is absent and with it the whole Madelung apparatus. What is written here is what remains, and it is not a smaller copy of the scalar fluid: it is a different object, with a force.

**Three statements make the article, and each is short.**

*The Lorenz condition is the continuity equation.* The four-potential is the density times the unit flow, $A_\mu=r\,u_\mu$, so the divergence the Lorenz condition sets to zero is $\partial_\mu(r u^\mu)$ and nothing else. The condition is not an analogue of continuity; it is continuity.

*The Euler equation has two forces, and only one of them is new.* The acceleration is the transverse gradient of the density's logarithm plus the field strength along the flow, $a_\mu=-\nabla_\mu\ln r-E_\mu/r$. The first is the pressure force of a fluid with $\epsilon=p=\frac12m^2r^2$, which is stiff; the second is the field strength, which no scalar and no spinor fluid has in this form.

*The field strength is the vorticity plus a baroclinic term.* Exactly, $F_{\mu\nu}=\partial_\mu r\,u_\nu-\partial_\nu r\,u_\mu+r\,\omega_{\mu\nu}$, so the vorticity is what is left of the field strength when the density gradient is subtracted. The spin-1 field is therefore the one case of the three in which the fluid's vorticity and the field's own spin are two readouts of one tensor.

**What the word cannot see is the spin, and that is the sharpest contrast with the spinor case.** The Dirac word carries eight parameters and the rotor is one of them, so the spin is in the fluid by construction. The Proca word carries four and none of them is an orientation: the spin lives in the complex structure of $\mathbb{B}_\Phi$, which the word does not touch. A fluid whose variables do not contain the spin cannot have a spin transport law, and this one does not.

**The article is a reading and not a derivation.** The word, its two branches, the logarithmic derivative, the two polar equations and the Lorenz display are the polar article's. What is added here is the fluid identification, the Euler equation, the decomposition of the field strength, the equation of state, and the comparison with the other two fluid articles of the block.

**A note on units.** The flow is normalised to $u^\mu u_\mu=-1$, so the corpus's four-velocity is $v^\mu_\Phi=c\,u^\mu$ and the acceleration displayed is $a^\mu=u^\nu\partial_\nu u^\mu$; the physical acceleration is $c^2a^\mu$. The subscript $\Phi$ of the material sector is dropped where no confusion arises.

## The Word, Read as Fluid Data

**The word has two branches and each carries four parameters for four components.** From the polar article, with $r>0$ the modulus of the quaternionic norm and $\varepsilon=\pm1$ the sign of the scalar potential,

$$
\tilde A_\Phi=\varepsilon\,i\,r\,\tilde U_{\Psi,\mathrm b}\quad(\langle\tilde A_\Phi\rangle_\natural<0),
\qquad
\tilde A_\Phi=r\,\tilde U_{\Psi,\mathrm b}\,\hat u\quad(\langle\tilde A_\Phi\rangle_\natural>0),
$$

and the lightlike set $\langle\tilde A_\Phi\rangle_\natural=0$ is outside both. On the timelike branch the boost is a velocity and the sign is a charge; on the spacelike branch there is a boost and a direction locked to it, and there is no velocity at all.

**Only the timelike branch is a fluid, and the reason is that a fluid needs a flow.** A spacelike four-potential has no timelike direction to be normalised into a velocity, so the second branch is a chart of the potential and not a fluid reading. The lightlike set is where the branch changes, and §*The Degenerate Set* treats it.

**On the timelike branch the potential *is* the current, and this is the fact that separates the case from the other two.** With $A_\mu$ the four components of $\varepsilon i r\tilde U_{\Psi,\mathrm b}$ in the components' spelling,

$$
\boxed{\;A_\mu=r\,u_\mu\;},
\qquad
r=\sqrt{-A_\mu A^\mu}>0,
\qquad
u_\mu u^\mu=-1 ,
$$

so that $r$ is read off the field's own norm and $u$ off its direction. In the scalar case the density is $r^{2}$ of a complex coefficient and the current is a separate bilinear; in the Dirac case the current is $\rho_{\mathrm{num}}\tilde V_\Phi$, a product of two factors and not an element of the field. Here the field is the current, and the Lorenz condition is therefore a statement about the current and not about a derived object.

**The two normalisations agree, and the check is one line.** Take $A_\mu$ from the word on the timelike branch with $\varepsilon=1$ and compute its norm: $\langle\tilde A_\Phi\rangle_\natural=-r^{2}$, so $r$ of the word and $r$ of the normalisation are the same number. The recovery was run on a field with $r=2+\sin r_x$, rapidity $r_x+r'_t r_y$ and direction in the $r_xr_y$ plane: $A_\mu A^\mu+r^{2}$ came out at exactly zero and $u_\mu u^\mu+1$ at exactly zero.

**Three fluid data at each event, and the fourth parameter is the charge's sign.**

| datum | range | symbol | what it is |
| --- | --- | --- | --- |
| scale | $r>0$ | $r=\sqrt{-A^{2}}$ | proper density of the current |
| direction | $u_\mu u^\mu=-1$ | $u_\mu=A_\mu/r$ | four-velocity, three parameters |
| branch | $\varepsilon=\pm1$ | $\varepsilon$ | sign of the scalar potential |

**The sign $\varepsilon$ is a label here, and this is the opposite of the spinor case.** In the Dirac word $\varepsilon$ is a *derived* function of the eight parameters, complex off the orthogonal locus, and [The Sign ε and the Rigidity Constraint on Σ₁₀](the-sign-epsilon-and-the-rigidity-constraint-on-sigma-10.html) proves it cannot be a label. In the material sector the field is real, the norm is real, and the sign of the scalar potential is genuinely discrete and genuinely free. The antiparticle of the spin-1 field is therefore visible in the word at the level of a sign, and the antiparticle of the spinor is not.

## The Lorenz Condition Is the Continuity Equation

**The condition the polar article displays as one divergence is the divergence of the four-potential, and the four-potential is the current.** With $S=\mathrm{Sc}\bigl((\tilde\nabla_\Phi)^\natural\tilde A_\Phi\bigr)$ the scalar part of the conjugate gradient,

$$
S=\partial_\mu A^\mu=\partial_\mu\bigl(r\,u^\mu\bigr) .
$$

**So the Lorenz condition is the continuity equation of the fluid, exactly and not by analogy.** It is one equation on four parameters, it removes one, and the three that remain are the three helicities of a massive spin-1 field — which is the count the polar article states and [The Third Polarization and the Self-Dual Split of the Massive Field Strength](the-third-polarization-and-the-self-dual-split-of-the-massive-field-strength.html) reads from the field side.

**What the polar article denies is the pair and not the single equation.** Its sentence that the Lorenz condition "is not a continuity equation" is a statement about the Madelung *pair*: in the scalar case the phase equation is continuity and the modulus equation is a Hamilton–Jacobi equation with the quantum potential, and the two close because the field is one complex function. Here the divergence is continuity and there is no second equation of that kind to pair it with, so the pair does not exist even though the first member does. **The distinction matters for what the fluid can be asked to do**: a continuity equation with no Hamilton–Jacobi partner carries no guidance and no quantum potential, which is §*The Scale and the Rapidity*.

**The conservation is the conservation of the field's own current, so the density is not a probability.** $J^\mu=A^\mu$ is conserved on the Lorenz surface and its time component is $\gamma\varepsilon r$, which changes sign with the branch. The fluid's proper density $r$ is positive by construction and the charge density is signed, and the two are different objects — the same split that the scalar fluid carries between $\rho_{\mathrm{num}}$ and $\rho_{\mathrm{chg}}$.

## The Euler Equation

**The acceleration is fixed by the density gradient and by the field strength, and the identity is exact.**

*Proposition.* Let $A_\mu=r u_\mu$ with $u_\mu u^\mu=-1$, let $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$, let $E_\mu=F_{\mu\nu}u^\nu$, and let $\nabla_\mu=\Delta_\mu{}^\nu\partial_\nu$ with $\Delta_{\mu\nu}=g_{\mu\nu}+u_\mu u_\nu$. Then

$$
\boxed{\;a_\mu=u^\nu\partial_\nu u_\mu=-\nabla_\mu\ln r-\frac{1}{r}E_\mu\;}
$$

*Proof.* Differentiate $A_\mu=r u_\mu$ and contract with $u^\nu$:

$$
u^\nu F_{\mu\nu}=u^\nu\partial_\mu\bigl(ru_\nu\bigr)-u^\nu\partial_\nu\bigl(ru_\mu\bigr)
=\partial_\mu r-\bigl(u^\nu\partial_\nu r\bigr)u_\mu-r\,a_\mu ,
$$

where $\partial_\mu(u^\nu u_\nu)=0$ removes the middle term. The last two terms are $-\nabla_\mu r-r a_\mu$, and dividing by $r$ gives the display.

**The residual was checked symbolically and it is zero in all four components.** The configuration was $r=2+\sin r_x$ with rapidity $r_x+r'_t r_y$ and direction in the $r_xr_y$ plane, chosen so that the density gradient, the flow and the vorticity are all non-trivial and mutually skew; $a_\mu+(E_\mu+\nabla_\mu r)/r$ vanished identically in each slot. The acceleration is orthogonal to the flow, $a_\mu u^\mu=0$, as it must be for a unit timelike field.

**The first force is a pressure force, and the equation of state it implies is stiff.** The gradient term is $-\nabla_\mu\ln r$, which is the enthalpy gradient of a fluid with

$$
\frac{\mathrm{d}p_{\mathrm{th}}}{\epsilon+p_{\mathrm{th}}}=\mathrm{d}\ln r .
$$

The mass term of the stress gives $\epsilon+p_{\mathrm{th}}=m^{2}r^{2}$ (§*The Stress*), so the equation integrates to $p_{\mathrm{th}}=\tfrac12m^{2}r^{2}$, up to a constant that is a choice of zero. **The density-gradient force of the Proca fluid is exactly the pressure force of a stiff fluid**, and the pressure is barotropic in $r$ by construction, since the force is a gradient of a function of $r$ alone.

**The second force is the field strength, and it is the only term that is not a gradient.** Its magnitude is the electric field along the flow divided by the density, it is transverse by antisymmetry, and it vanishes exactly when the field strength annihilates the flow. So the Proca fluid is a charged fluid whose charge density is its own density and whose field is its own field strength: a self-coupled medium, not a dust.

**The two cases at the ends of the identity are worth naming.**

*The flow is geodesic exactly when the field strength balances the density gradient.* $a_\mu=0$ if and only if $E_\mu=-\nabla_\mu r$. The field strength is then the unique transverse field that a density gradient requires, and the flow falls freely.

*An irrotational flow is geodesic.* If $u_\mu=\partial_\mu\phi$ then $a_\mu=u^\nu\partial_\mu\partial_\nu\phi=\tfrac12\partial_\mu(u^\nu u_\nu)=0$, because the norm is constant. Conversely an irrotational flow has $A_\mu=r\partial_\mu\phi$ and $E_\mu=-\nabla_\mu r$ by the identity above, so the two statements are the same statement. **No irrotational Proca flow accelerates**, and that is the sharpest difference from the scalar fluid, whose acceleration is the gradient of the quantum potential and need not vanish.

## The Field Strength Is the Vorticity Plus a Baroclinic Term

**The product rule separates the field strength into two pieces, and the second is the fluid's vorticity.**

$$
\boxed{\;F_{\mu\nu}=\partial_\mu r\,u_\nu-\partial_\nu r\,u_\mu+r\,\omega_{\mu\nu}\;}
\qquad
\omega_{\mu\nu}=\partial_\mu u_\nu-\partial_\nu u_\mu .
$$

The first two terms are the wedge of the density gradient with the flow: a two-form whose legs are the gradient and the velocity. The last is the vorticity weighted by the density. The identity was checked symbolically and the difference vanished in all sixteen slots.

**Read the display as a definition and it says what the vorticity is.** The vorticity is the part of the field strength that is not the density gradient, divided by the density:

$$
r\,\omega_{\mu\nu}=F_{\mu\nu}-\bigl(\partial_\mu r\,u_\nu-\partial_\nu r\,u_\mu\bigr) .
$$

In the scalar case the vorticity is identically zero because the velocity is a gradient; in the Dirac case it is the antisymmetrised gradient of the frame and is a separate object from the spin. Here the two are the two halves of one tensor, and no third object appears.

**The baroclinic reading is exact, and the term is the fluid layer's own.** In a classical fluid the vorticity is generated from rest by the baroclinic torque $\nabla\rho_{\mathrm{mass}}\times\nabla p_{\mathrm{th}}/\rho_{\mathrm{mass}}^{2}$, which is nonzero exactly when the density gradient and the pressure gradient are not parallel — the content of [The Equation of State and the Barotropic Condition](the-equation-of-state-and-the-barotropic-condition.html). Here the pressure is barotropic, so that torque vanishes identically, and the generator is the other force: the vorticity is generated by $E_\mu/r$, which is not a gradient whenever $E$ is not proportional to $\nabla r$. **The Proca fluid is therefore the one fluid of the three with a genuinely non-gradient force, and therefore the one that generates vorticity from rest.**

**A counting remark fixes the size of the term.** The force is $E_\mu/r$, and $E$ has three independent components in the rest frame; the density gradient has three; the vorticity has three. The relation $\nabla\wedge(E/r)\ne0$ is one scalar condition on the pair, and the flows for which the vorticity is not generated are exactly those where $E$ is parallel to $\nabla r$ in the rest frame.

**The vorticity is always simple and the field strength is not, and the difference is the density-gradient term.** For any unit timelike flow $\omega\wedge\omega=0$, because the vorticity annihilates the flow and a two-form on the three dimensions of the rest space is simple — the proof is [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html)'s. The field strength inherits no such protection, because the sum of two simple forms need not be simple, and the four-form is

$$
F\wedge F=2r\;\bigl(\partial r\wedge u\bigr)\wedge\omega .
$$

Both statements were checked: $\omega\wedge\omega$ vanished identically on the field above, while a generic configuration with $r=2+\sin(r_xr_z)$, rapidity $r_xr_z$ and a direction depending on $r'_t r_x$ gave $\det F=0.3176$ and $\vec E_{\mathrm{vrt}}\cdot\vec B_{\mathrm{vrt}}=-0.5636$ at a generic event. **So the fluid's vorticity is rank two for every solution, while the field's own tensor reaches the rank the vorticity cannot** — and the Clebsch pair represents the first and not the second.

## The Scale and the Rapidity

**The polar equations read as a density equation and a conservation law, and neither is a Hamilton–Jacobi equation.** With $\Gamma_\mu=\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b}$ the frame's connection, the polar article's two equations are

$$
\bigl(\Box_\Phi-k_m^{2}\bigr)r+r\sum_\mu\mathrm{Sc}\bigl(\Gamma_\mu^{2}\bigr)=0,
\qquad
\sum_\mu\Bigl(\partial_\mu\Gamma_\mu+\Gamma_\mu^{2}-\mathrm{Sc}\bigl(\Gamma_\mu^{2}\bigr)\Bigr)+2\sum_\mu\partial_\mu\ln r\,\Gamma_\mu=0 .
$$

**The first is the density's equation and its source is the connection's square.** For a fixed boost axis $\Gamma_\mu=\tfrac12\partial_\mu\theta_{\mathrm{rpd}}\,i\hat u_{\mathrm{b}}$ and $\mathrm{Sc}(\Gamma_\mu^{2})=\tfrac14(\partial_\mu\theta_{\mathrm{rpd}})^{2}$, so

$$
\bigl(\Box_\Phi-k_m^{2}\bigr)r+\tfrac14\,r\sum_\mu\bigl(\partial_\mu\theta_{\mathrm{rpd}}\bigr)^{2}=0 .
$$

**The term that stands where a quantum potential stands is quadratic in the rapidity's gradient and not in the density's curvature.** In the scalar case the corresponding term is $-\hbar^{2}\Box_\Phi r/(2mr)$, which carries two derivatives of $r$ and vanishes for a uniform density; here the term carries two derivatives of an angular parameter and vanishes for a rigid flow. So the two are not the same object under another name, and the polar article says so. **The consequence for the fluid is that a uniform Proca fluid with a varying rapidity is not a solution of the mass-shell equation**: the rapidity's gradient acts as a source for the density, and there is no classical fluid in which a shear feeds the mass term this way.

**The second reduces to a conservation law with the density's square as its charge.** On the fixed axis the traceless equation is

$$
\sum_\mu\partial_\mu\Bigl(r^{2}\partial_\mu\theta_{\mathrm{rpd}}\Bigr)=0 ,
$$

verified in the polar article to $10^{-9}$ on a smooth configuration. **The rapidity's gradient flows with density $r^{2}$**, and this is the closest the case comes to a transport equation for the flow's parameter.

**That current is not the number current, and the difference is the whole reason the case is not a Madelung fluid.** The number current is $r u^\mu$, whose divergence is the Lorenz condition; the rapidity current is $r^{2}\partial^\mu\theta_{\mathrm{rpd}}$, which is not parallel to $u^\mu$ and has no continuity equation to be paired with in the frame's other components. **A flow whose rapidity gradient is a pure gradient in time has a rapidity current with no spatial part**, so the two currents are genuinely different objects and neither is a rewriting of the other. What the pair of equations gives is a density and a rapidity that determine each other, and not a phase that guides a particle.

## The Stress, and What the Word Cannot See

**The stress splits into a perfect-fluid part and a field-strength part, and the split is exact.** With the Proca stress of the element form,

$$
T_{\mu\nu}=-F_{\mu\alpha}F_\nu{}^{\alpha}+\tfrac14g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}
+m^{2}\bigl(A_\mu A_\nu-\tfrac12 g_{\mu\nu}A^{2}\bigr),
$$

the mass term alone is the perfect-fluid form. Projecting it with $u^\mu u^\nu$ and with $\Delta^{\mu\nu}$, and using $A_\mu u^\mu=-r$, $A^{2}=-r^{2}$ and $u^{2}=-1$,

$$
\epsilon_{\mathrm{mass}}=m^{2}\Bigl(\bigl(A_\mu u^\mu\bigr)^{2}-\tfrac12u^{2}A^{2}\Bigr)=\tfrac12m^{2}r^{2},
\qquad
p_{\mathrm{mass}}=\tfrac13m^{2}\Bigl(A_\mu A_\nu\Delta^{\mu\nu}-\tfrac12 g_{\mu\nu}\Delta^{\mu\nu}A^{2}\Bigr)=\tfrac12m^{2}r^{2}.
$$

**So the mass term is a stiff fluid: $\epsilon=p=\tfrac12m^{2}r^{2}$ and the sound speed is $c$.** This is the equation of state that §*The Euler Equation* read off the density-gradient force, and the agreement is the check that the force and the stress are the same object.

**The field-strength part is traceless, transverse-anisotropic, and invisible to the word.** It is quadratic in $F$, its trace vanishes identically, and its transverse traceless projection is nonzero wherever the field strength's own transverse part is — so the stress is that of a perfect fluid only where $F$ is negligible against the mass, which is the long-wavelength limit. **The word has no parameter that could carry this part**: the four parameters are a scale, a direction and a sign, and the anisotropy is a function of the field strength's three electric and three magnetic components in the flow frame.

**This is the sharpest structural difference from the spinor case, and it goes the opposite way from what a reader might expect.** The Dirac word *over*-describes the fluid: eight parameters for a medium whose stress needs six, which is why [The Spin Energy-Momentum Tensor](the-spin-energy-momentum-tensor.html) has to cut the count and why the antisymmetric part is the residue. The Proca word *under*-describes its field: four parameters for a field whose stress carries six more, because the spin is in the algebra's complex structure and not in the polar decomposition. **The spin-1 spin is present in the theory and absent from the word, and the spin-½ spin is present in both.**

**The two facts are consistent because the two words are decompositions of different objects.** The Dirac word is a decomposition of an element of $\mathbb{B}$ into four factors, and the algebra's complex structure is used to write the factorisation; the residual structure lives in the factors' relation. The Proca word is a decomposition of a real four-vector, and the complex structure is what the reality *excludes*. That is why the central factor of the Dirac word is absent here identically: it is not that the Proca field's phase is constant, it is that a real four-vector has no phase slot at all.

## The Properties, Listed

**Twelve statements, each one line, and each with its reason. This is what the Proca fluid is.**

1. **The field is the current.** $A_\mu=r u_\mu$, so the density is the field's own norm and the velocity its own direction. No bilinear, no separate construction.
2. **The density is positive wherever the chart exists.** $r=\sqrt{-A^{2}}>0$ by construction, and it cannot vanish: the chart fails first, on the lightlike set. The scalar fluid can be zero at a point; this one cannot.
3. **The continuity equation is the Lorenz condition.** $\partial_\mu(ru^\mu)=0$ is not an analogue of continuity but the condition itself, and it removes one of the four parameters, leaving the three helicities.
4. **The acceleration is kinematic, not dynamical.** $a_\mu=-\nabla_\mu\ln r-E_\mu/r$ holds for every potential of the form $A=ru$, whether or not it solves anything. The dynamics is in the closure of §*The Correspondence, Compared with the Other Two*.
5. **It carries a stiff pressure.** $p=\epsilon=\tfrac12m^{2}r^{2}$ and the sound speed is $c$, read off the density-gradient force and confirmed by projecting the mass term of the stress.
6. **It carries a transverse force that no other field fluid has.** $E_\mu/r$ is the only non-gradient force in the three cases, and it is what makes the flow non-geodesic.
7. **An irrotational flow is geodesic.** $u=\partial\phi$ forces $a=0$; equivalently $E=-\nabla r$. A fluid with a stiff pressure that falls freely.
8. **It generates vorticity although it is barotropic.** The baroclinic torque vanishes, since $p$ is a function of $r$ alone, and yet $\nabla\wedge(E/r)\ne0$ generates vorticity wherever $E$ is not parallel to $\nabla r$. No classical fluid does this.
9. **Its vorticity is always rank two, and its field strength is not.** $\omega\wedge\omega=0$ for every unit timelike flow; $\det F$ is nonzero generically. The Clebsch pair reaches the first and not the second.
10. **It has no spin variable.** Four parameters, no orientation. The spin is in the complex structure of $\mathbb{B}_\Phi$ and shows up in $F$, not in the word.
11. **It has no phase, and therefore no guidance and no Bohm potential.** The term that stands where the quantum potential stands is $\tfrac14r(\partial\theta_{\mathrm{rpd}})^{2}$, quadratic in a rapidity's gradient and not in a density's curvature.
12. **Its stress is perfect only where the mass dominates.** The mass term is a perfect fluid; the field-strength term is traceless and anisotropic and is not representable in the word's four parameters.

## The Three Fluids

**The three fluid articles of the block can be put side by side, and the table is the shortest statement of what each field's fluid is.** The table is the same in all three articles; what changes from one to the next is which column is the article's own.

| | Klein–Gordon | Proca | Dirac |
| --- | --- | --- | --- |
| word | $r\,e^{i\theta_{\mathrm{pha}}}\varepsilon$ | $\varepsilon\,i\,r\,\tilde U_{\Psi,\mathrm b}$ | $r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r}$ |
| parameters | $2$ | $4$ | $8$ |
| real equations | $2$ | $4$ | $8$ |
| density | $\rho_{\mathrm{num}}=r^{2}$, a bilinear | $r=\sqrt{-A^{2}}$, the field's own norm | $\rho_{\mathrm{num}}$, a factor of the word |
| velocity | $\partial_\mu S/m$, a gradient | $A_\mu/r$, the field's direction | $ic\tilde U^{-2}$, the frame |
| continuity | the imaginary part of the wave equation | the Lorenz condition | the conservation of $\tilde J$, a separate statement |
| force | $-\gamma^{-1}\nabla Q_{\mathrm{qnt}}$, a gradient | $-\nabla\ln r-E_\mu/r$ | the divergence of the stress, antisymmetric part included |
| vorticity | zero identically | $r\,\omega=F-\mathrm{d}r\wedge u$ | the antisymmetrised frame gradient |
| spin in the word | none | none | the rotor |
| equation of state | none; a Korteweg stress | $p=\epsilon=\tfrac12m^{2}r^{2}$ | none; the spin's transport closes the system |
| reverse condition | barotropic, irrotational and inviscid | none; closure is $J^{\mu}=m^{2}A^{\mu}$ | the Frenkel condition, or a free constitutive law |
| classical medium | a Korteweg fluid | a London plasma | a Cosserat medium |
| degenerate set | $r=0$, codimension two | the lightlike set, codimension one | $r=0$, codimension two |

**The force row is the article's substance.** A fluid whose only force is a gradient has no vorticity generation and no baroclinic torque, and the scalar case is that fluid. A fluid whose force has a transverse part generates vorticity, and the Proca case is that fluid with the simplest possible transverse force. A fluid whose stress has an antisymmetric part is a third thing again, and the Dirac case is that. **The three cases are not three approximations of one another; they are three positions on a list of what a force can be.**

**The density row is the article's surprise.** In the scalar and spinor cases the density is a bilinear or a factor and the current is a separate construction; in the Proca case the field is the current, so the fluid's density is not something the field has but something the field is. That is why the Lorenz condition does double duty here — as the gauge condition of the element form and as the continuity equation of the fluid — and it is why the case has no non-uniqueness of the kind [The Non-Uniqueness of the Spin Fluid](the-non-uniqueness-of-the-spin-fluid.html) records: there is no choice of which density is conserved, because there is only one candidate.

## The Correspondence, Compared with the Other Two

**There is a correspondence, and its structure is the same as the other two in its skeleton and different in its joint. The skeleton is three steps: the word is exact, the reverse map is defined on a class, and membership of that class is the extra structure that makes the fluid classical rather than merely a relabelling.**

**The correspondence, stated.** The field is a fluid, and the fluid is a field, and the two directions are not of the same strength:

$$
\text{field}\;\longrightarrow\;\text{fluid}\quad\text{(exact, total, no conditions)},
\qquad
\text{fluid}\;\longrightarrow\;\text{field}\quad\text{(total, but only solutions close)} .
$$

**The forward arrow is total here in a way it is not for the other two.** Any four-potential on the timelike branch gives a density and a flow by $r=\sqrt{-A^{2}}$ and $u=A/r$; nothing is asked of it. This is the same exactness the scalar and spinor words have, and it is what §*The Word, Read as Fluid Data* establishes.

**The reverse arrow is where the three cases part, and the Proca case is the most permissive.** Given any unit timelike flow $u$ and any positive $r$, the potential $A_\mu=ru_\mu$ exists. There is no barotropicity to assume, no irrotationality, no orientation to constrain, no constitutive function to choose. **The Proca reverse map is defined on the whole of the fluid state space**, which is not true of either of the other two: the scalar case needs an irrotational barotropic flow, and the spinor case needs the Frenkel condition or a free constitutive law.

**What is conditional is not membership of a class but closure.** The potential built from $(r,u)$ solves the Proca equation only if the flow obeys

$$
\partial_\nu F^{\nu\mu}=m^{2}A^{\mu}=m^{2}r\,u^{\mu},
$$

which is Maxwell's equation with the fluid's own number current as its source, weighted by the mass squared. **So the extra structure is not a constitutive law but a source**: the fluid carries a field and the field is generated by the fluid's own current. The classical object this names is a *charged fluid*, and the response $J^{\mu}=m^{2}A^{\mu}$ is the London response of a collisionless plasma or a superconductor, where the mass term is the Meissner mass.

**So the three correspondences are three different kinds of extra structure, and the list is short and complete.**

| field | the fluid it is | the extra structure | the classical object |
| --- | --- | --- | --- |
| Klein–Gordon | a barotropic irrotational flow | a stress that depends on the density's gradient | a Korteweg fluid |
| Proca | a flow with a density | a source carried by the flow itself | a London plasma |
| Dirac | a flow with an orientation | an internal degree of freedom | a Cosserat medium |

**The three structures are the three ways a classical medium can differ from a dust**: by remembering the gradient of its state (Korteweg), by carrying an internal field of its own (London), or by carrying an internal orientation (Cosserat). Each field picks exactly one. That is the sense in which the correspondence is systematic and not a pile of coincidences.

**The Madelung pair generalizes, but into a pair of a different shape.** In the scalar case the two real equations are both scalar — continuity and a Hamilton–Jacobi equation with the quantum potential — and they close because the field is one complex function. Here the pair is one scalar and one vector:

$$
\underbrace{\partial_\mu\bigl(r u^{\mu}\bigr)=0}_{\text{one scalar}}
\qquad\text{and}\qquad
\underbrace{\partial_\nu F^{\nu\mu}=m^{2}r\,u^{\mu}}_{\text{three components}} .
$$

**The second member is a field equation and not a Hamilton–Jacobi equation, and that is the honest statement of what is missing.** A Hamilton–Jacobi equation is an equation for a phase, and there is no phase: the material sector is real. What stands in its place is the vector equation for the field strength, which is *more* than a Hamilton–Jacobi equation in the sense that it has three components and not one.

**The count is one equation per parameter in all three cases, and the numbers double.**

| case | parameters | real equations | shape of the pair |
| --- | --- | --- | --- |
| Klein–Gordon | $r$, $\theta_{\mathrm{pha}}$ — two | two | scalar and scalar |
| Proca | $r$ and three of the boost — four | four | scalar and vector |
| Dirac | $r$, $\theta_{\mathrm{pha}}$, three of the boost, three of the rotor — eight | eight | scalar, vector, and two more |

**The doubling is the doubling of the algebra's real dimension at each step**, and the equation count tracks it exactly. That is the cleanest evidence that none of the three is a truncation of another.

**The sharpest structural difference, and it is a difference in what the continuity equation *is*.** In the Klein–Gordon case the current is a Noether current and the continuity equation holds for every $m$, including $m=0$; the density is a genuine charge. Here the continuity equation is *forced by the mass*: the Proca equation contracts against $\partial_\mu$ to give $0=m^{2}\partial_\mu A^{\mu}$, so the Lorenz condition holds if and only if $m\ne0$. **In the massless limit the fluid's continuity equation evaporates**, and the reason is that a massless potential is a gauge field with no gauge-invariant density to conserve — the photon has no fluid. So the Proca fluid's density is not a charge in the Noether sense; it is a quantity that the mass makes available.

**The quantum correspondence runs the other way, and this is worth stating because a reader will ask.** For the Klein–Gordon and Dirac equations the fluid reading is the Bohmian one, and the quantum content is a second-gradient term in the fluid: $Q_{\mathrm{qnt}}=-\hbar^{2}\Box r/(2mr)$ in the scalar case, and the spin's own transport in the spinor case. **For the Proca field the fluid reading is not Bohmian, because there is no phase to guide anything.** The quantum content is instead the term $\tfrac14r(\partial\theta_{\mathrm{rpd}})^{2}$ in the scale equation, which is a classical object with a classical meaning: it is the energy stored in the shearing of the flow's frame, the analogue of the centrifugal term in a rotating flow. The literature this belongs to is not Bohmian mechanics but the quantum hydrodynamic model of a plasma — the Schrödinger–Maxwell and Schrödinger–Poisson systems, where a charged fluid carries its own field and the quantum correction enters the momentum balance as a density-gradient stress. **That is the correct contemporary home for a Proca fluid**, and the correspondence with the other two articles of the block is by analogy of role and not by identity of term.

**What the analogy supports and what it does not.** It supports the claim that each of the three field equations is the equation of motion of a recognizable classical medium, and it supports the count, the forces and the equation-of-state readings item by item — those are the content of §§*The Euler Equation*–*The Stress, and What the Word Cannot See*. It does not support the claim that the Proca fluid's spin is a fluid variable, that its stress is perfect, or that a phase exists to be guided: those three absences are proved above and are not repairs to be made later.

## The Degenerate Set

**The chart fails on the lightlike set of field values, and the set is one dimension larger than the scalar case's.** In the scalar case the word fails where the complex coefficient vanishes, $r=0$, which is a codimension-two set in spacetime. Here the word fails wherever the local four-vector is null, $\langle\tilde A_\Phi\rangle_\natural=0$, and that is a three-dimensional family of surfaces for a generic solution. **The set where the fluid reading is unavailable is therefore a hypersurface, and the density is not a non-negative function with nodal points but a positive function that fails to exist on a wall.**

**A plane wave shows the wall and the reading on each side of it.** With $\tilde A_\Phi=\tilde A_0\cos\theta_{\mathrm{pwp}}$ and $\tilde A_0$ constant and timelike, the polar article's word is $r=\lvert\cos\theta_{\mathrm{pwp}}\rvert\sqrt{-\langle\tilde A_0\rangle_\natural}$, a constant frame, and $\varepsilon=\mathrm{sign}\cos\theta_{\mathrm{pwp}}$. So the flow is rigid, the density vanishes on the nodal hyperplanes, and the branch flips at each of them.

**The rigid flow is geodesic, and the check closes the article's Euler equation against its own word.** A constant $u$ has $a_\mu=0$, so by the Euler equation $E_\mu=-\nabla_\mu r$. The field strength of the plane wave is $F_{\mu\nu}=u_\nu\partial_\mu r-u_\mu\partial_\nu r$ because the frame is constant, so $E_\mu=F_{\mu\nu}u^\nu=-(\partial_\mu r+u_\mu u\cdot\partial r)=-\nabla_\mu r$ identically. **The identity holds and the two routes agree**: the rigid flow is the one whose field strength is exactly the density gradient, which is §*The Euler Equation*'s geodesic condition read on a plane wave.

**The flow does not accelerate and the medium is not stress-free, and the two facts together are the article's most counter-intuitive consequence.** A plane wave has $a_\mu=0$ identically, so its flow falls freely; its stress is not zero, and its equation of state is stiff, $\epsilon=p=\tfrac12m^{2}r^{2}$. What balances the pressure gradient is the field-strength force $E_\mu/r$, which for an irrotational flow is exactly $-\nabla_\mu\ln r$. So an irrotational Proca fluid is a medium with a stiff pressure that nevertheless moves on geodesics, because the pressure it carries is not the pressure that pushes it: the two forces cancel term by term. The nearest classical picture is a force-free magnetic configuration, where the stress is nonzero and nothing accelerates, and the analogy is exact at the level of the Euler equation and not at the level of the constitutive law.

**The stress was computed on a plane wave to make the point.** With $k$ along one axis and a transverse potential the stress is anisotropic: $T_{00}=0.0777$, $T_{11}=0.1014$ and $T_{33}=-0.1153$ at one event, so $T_{11}/T_{00}=1.30$ and the stress is not that of a perfect fluid. The mass term alone would give $T_{11}/T_{00}=1$. The difference is the field-strength part, and it is of the same order as the mass part even for a mode whose wavelength is a few Compton lengths.

**What the plane wave is not is a moving fluid.** Its velocity is constant in spacetime, its vorticity is zero, and the whole of its structure is a standing density pattern whose sign flips at the nodes. **The fluid reading of a plane wave is therefore a reading of the density and not of a motion**, which is the reverse of the scalar case, where a plane wave's fluid is a uniform flow with a linear phase.

## What Is Established and What Is Interpretation

**Established.** That on the timelike branch the four-potential is the density times the unit flow, $A_\mu=ru_\mu$ with $r=\sqrt{-A^{2}}$, checked to vanish identically on a non-trivial configuration. That the Lorenz condition is the divergence of that current and therefore the continuity equation. That the acceleration is $a_\mu=-\nabla_\mu\ln r-E_\mu/r$, checked symbolically to zero in all four components. That $a_\mu u^\mu=0$, and that an irrotational flow is geodesic, by the two-line argument from $u=\partial\phi$. That the field strength decomposes as $F=\mathrm{d}r\wedge u+r\omega$, checked to zero in all sixteen slots. That $\omega\wedge\omega=0$ for every unit timelike flow while $\det F\ne0$ generically, the numerical values being $0$ and $0.3176$ on the two configurations used. That the mass term of the stress is a perfect fluid with $\epsilon=p=\tfrac12m^{2}r^{2}$, by direct projection with $u\otimes u$ and $\Delta$.

**Not claimed.** That the Proca fluid is a Bohmian fluid; it is not, and its quantum content is a shear energy and not a guidance term. That the correspondence makes the fluid self-contained; it does not, since the force is its own field. That the Proca fluid's equation of state is $p=\epsilon$ beyond the mass term; the field-strength part is not a fluid and the full stress is not perfect. That the transverse force $E_\mu/r$ has a thermodynamic reading; it is a force and not a pressure gradient. That the two polar equations have a fluid closure in the general frame; the fixed-axis reduction is the polar article's and the general case is open there. That the spacelike branch has a fluid reading; this article gives none and argues that none is available.

**Interpretation.** That the Proca field's fluid is best called a charged fluid. The identification is of the current, the force and the equation of state, and the word "charged" names the fact that the force is the field strength and not a gradient — it does not assert that the medium carries an independent charge density.

## Summary

**The Proca word is a two-factor word, and read as fluid data it gives a scale, a direction and a sign.** The scale is the field's own norm, the direction is the field's own direction, and the sign is the branch. Four parameters for four components, exactly, and the lightlike set is outside the chart.

**The potential is the current, which is true of no other field in the block.** $A_\mu=ru_\mu$, so the Lorenz condition is $\partial_\mu(ru^\mu)=0$ and is the continuity equation outright. There is no choice of which density is conserved, and no bilinear to compute.

**The Euler equation carries two forces.** The gradient of the density's logarithm is the pressure force of a stiff fluid, $p=\epsilon=\tfrac12m^{2}r^{2}$, and the field strength along the flow is the only non-gradient force in any of the three field fluids. An irrotational flow is geodesic; a flow that accelerates does so because its field strength is not the density gradient.

**The field strength is the vorticity plus the density gradient's wedge with the flow.** $F=\mathrm{d}r\wedge u+r\omega$, so the vorticity is a readout of the field strength and the spin is the rest of it. The vorticity is rank two for every solution and the field strength is not, which is the precise sense in which the field's tensor carries more than the fluid's.

**The correspondence exists, and its skeleton is the other two's.** The forward arrow is exact and total: any timelike potential is a density and a flow. The reverse arrow is total as well — every unit flow with a positive density gives a potential — which makes the Proca case the most permissive of the three; what is conditional is only closure. The closure is $\partial_\nu F^{\nu\mu}=m^{2}ru^{\mu}$, Maxwell's equation with the fluid's own current as source, and the response $J=m^{2}A$ is the London response of a charged fluid. The three fields therefore pick the three ways a medium can exceed a dust: a gradient of the state (Korteweg), an internal source (London), an internal orientation (Cosserat). The pair is one scalar plus one vector, four equations for four parameters, and the counts run $2,4,8$.

**The word cannot see the spin, and that is the contrast with the spinor case.** The Dirac word over-describes its fluid and the Proca word under-describes its field; the spin-½ spin is in both and the spin-1 spin is in neither the word nor the fluid. The stress says so: its mass term is perfect and its field-strength term is anisotropic and unrepresentable in four parameters.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde A_\Phi$ | the Proca potential, an element of $\mathbb{B}_\Phi$ |
| $A_\mu$ | its four components in the frame |
| $r=\sqrt{-A^{2}}$ | the proper density, positive on the timelike branch |
| $u_\mu=A_\mu/r$ | the unit four-velocity, $u_\mu u^\mu=-1$ |
| $\varepsilon=\pm1$ | the branch label, the sign of the scalar potential |
| $\tilde U_{\Psi,\mathrm b}$ | the boost of the word |
| $\Gamma_\mu=\tilde U^{-1}\partial_\mu\tilde U$ | the frame's connection, the Maurer–Cartan form |
| $\theta_{\mathrm{rpd}}$ | the rapidity, the flow's parameter on a fixed axis |
| $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ | the field strength |
| $E_\mu=F_{\mu\nu}u^\nu$ | the field strength along the flow |
| $\omega_{\mu\nu}=\partial_\mu u_\nu-\partial_\nu u_\mu$ | the vorticity two-form |
| $a_\mu=u^\nu\partial_\nu u_\mu$ | the acceleration, orthogonal to the flow |
| $\Delta_{\mu\nu}=g_{\mu\nu}+u_\mu u_\nu$ | the projector onto the rest space |
| $\nabla_\mu=\Delta_\mu{}^\nu\partial_\nu$ | the transverse gradient |
| $S=\mathrm{Sc}((\tilde\nabla_\Phi)^\natural\tilde A_\Phi)$ | the Lorenz scalar, equal to $\partial_\mu A^\mu$ |
| $k_m=mc/\hbar$ | the mass wave number |
| $\langle\tilde Q\rangle_\natural$ | the quaternionic norm |

## Further Reading

- Alexandru Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs," *Journal de Physique et le Radium* **7** (1936) 347–353, for the massive spin-1 equation and its subsidiary condition.
- Jean-Pierre Serre, *Cohomologie galoisienne*, or any account of the Maurer–Cartan form, for the flatness identity that makes the frame's connection the source of the polar equations.
- A. Clebsch, *Über eine allgemeine Transformation der hydrodynamischen Gleichungen*, J. Reine Angew. Math. **54** (1857), 293–312, for the potential representation of a rotational velocity that §*The Field Strength Is the Vorticity Plus a Baroclinic Term* uses in its rank remark.
- James Clerk Maxwell, "On stresses in rarified gases arising from inequalities of temperature," *Philosophical Transactions of the Royal Society* **170** (1879) 231–256, for the stress of a medium whose anisotropy is not a pressure.
- Clifford M. Will, *Theory and Experiment in Gravitational Physics* (Cambridge University Press, 1993), §4, for the stiff equation of state $p=\epsilon$ and its role as the limiting causal fluid.
- Fritz London and Heinz London, "Supraleitung und Diamagnetismus," *Physica* **2** (1935) 341–354, for the response $J^{\mu}\propto A^{\mu}$ that the Proca mass term is, and hence for the reading of the mass as a Meissner mass.
- Giovanni Manfredi, "How to model quantum plasmas," *Fields Institute Communications* **46** (2005) 263–287, for the quantum hydrodynamic model in which a charged fluid carries its own field and the quantum correction enters the momentum balance as a density-gradient stress — the correct home for a Proca fluid, as opposed to the Bohmian one.
- The companion articles: [The Proca Equation in Biquaternionic Polar Variables](the-proca-equation-in-biquaternionic-polar-variables.html), [The Proca Equation: Massive Spin 1 in Biquaternionic Form](the-proca-equation-massive-spin-1-in-biquaternionic-form.html), [The Klein–Gordon Fluid](the-klein-gordon-fluid.html), [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html), [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html), [The Third Polarization and the Self-Dual Split of the Massive Field Strength](the-third-polarization-and-the-self-dual-split-of-the-massive-field-strength.html).
