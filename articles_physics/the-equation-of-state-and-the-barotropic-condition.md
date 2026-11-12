# __The Equation of State and the Barotropic Condition__

## Introduction

**The law of state is the datum the equations of motion do not supply.** Euler's equation and the continuity equation carry a pressure and never say what it is; the law of state is the extra relation that closes them, and the choice of that relation is the choice of a fluid. Without it the system is one equation short and the pressure is an independent unknown.

**The condition that removes it is barotropicity.** A fluid is barotropic when its pressure is a function of the density alone, so the entropy is not an independent datum and the count falls from five to four. That is the best an ordinary fluid can do, and this article states what it buys, what it costs and where it fails.

**The cost is that the condition creates the previous obstruction.** A baroclinic fluid — one whose pressure depends on a second variable — generates vorticity from rest, by the Bjerknes torque. So the two conditions are not independent: baroclinicity produces exactly the vorticity that [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html) removes. The coupling is stated below with its identity.

**The article also separates two things that a careless reading fuses.** A fluid's force is a pressure force plus whatever else the medium supplies — a body force, a capillary term, a second-gradient stress. Barotropicity is a condition on the pressure alone. It says nothing about the rest, and the rest need not be a local function of the density. That separation is what allows the later article to say that a barotropic fluid is necessary for the reverse map and still not in the map's image.

## The Two Variables

**The pressure of a general fluid depends on the density and on the entropy.** Write

$$
p_{\mathrm{th}}=p_{\mathrm{th}}\bigl(\rho_{\mathrm{mass}},s_{\mathrm{spc}}\bigr),
$$

with $\rho_{\mathrm{mass}}$ the mass density and $s_{\mathrm{spc}}$ the specific entropy. The partial derivatives have names: the square of the sound speed is

$$
c_{\mathrm{s}}^{2}=\left(\frac{\partial p_{\mathrm{th}}}{\partial\rho_{\mathrm{mass}}}\right)_{s_{\mathrm{spc}}},
$$

the derivative at fixed entropy, and the second derivative is the one that couples the pressure to the thermal variable.

**The count falls by one when the second derivative is dropped.** A general fluid has five continuous data at a point: the density, the three velocity components and the specific entropy. A barotropic fluid has four, because the entropy is no longer independent. That is the whole of the condition's content, and it is the reason the later article can speak of the count closing.

**The barotropic condition is a restriction on the fluid and not on its flow.** It does not say that the flow is isentropic; it says that the pressure does not care. A flow can be barotropic and still change its entropy locally through dissipation, and then the pressure is the same function of the density as before. The condition is about the constitutive law, not about the history.

## The Baroclinic Torque

**A baroclinic fluid generates vorticity from rest.** The vorticity equation of an inviscid fluid is

$$
\partial_{t'}\vec\omega_{\mathrm{vrt}}
=\nabla\times\bigl(\vec v\times\vec\omega_{\mathrm{vrt}}\bigr)
+\frac{\nabla\rho_{\mathrm{mass}}\times\nabla p_{\mathrm{th}}}{\rho_{\mathrm{mass}}^{2}} .
$$

The last term is the baroclinic torque, and it is the only source of vorticity in a flow that starts from rest. It vanishes exactly when the two gradients are parallel, which is the case for a barotropic fluid whose pressure is a function of the density: then $\nabla p_{\mathrm{th}}=(\mathrm{d}p_{\mathrm{th}}/\mathrm{d}\rho_{\mathrm{mass}})\nabla\rho_{\mathrm{mass}}$ and the cross product is zero.

**The exact condition is the Gibbs–Duhem relation, and barotropicity is the strong form of it.** The pressure force per unit mass is

$$
\frac{1}{\rho_{\mathrm{mass}}}\nabla p_{\mathrm{th}}=\nabla h-T\nabla s_{\mathrm{spc}} ,
$$

with $h$ the specific enthalpy, $\mathrm{d}h=T\,\mathrm{d}s_{\mathrm{spc}}+\mathrm{d}p_{\mathrm{th}}/\rho_{\mathrm{mass}}$. So the pressure force is a gradient exactly when the flow is isentropic, $\nabla s_{\mathrm{spc}}=\vec 0$; and a barotropic law makes it a gradient whatever the entropy field does, because then $h=h(\rho_{\mathrm{mass}})$ and $\nabla h$ is a function of the density alone. That is why the condition is stated on the law and not on the flow: a barotropic fluid needs no knowledge of its entropy field to be gradient-forced. [The Direction of the Fluid-Wave Correspondence, Field by Field](the-direction-of-the-fluid-wave-correspondence-field-by-field.html) uses this form as the force half of its criterion.

**The identity is exact and it is checked by expansion.** Substituting Euler's equation into the curl of the velocity, in two dimensions for definiteness, gives the two terms on the right and nothing else: the pressure gradient contributes the baroclinic term, and the convective term contributes the vorticity transport. No term is dropped and the coefficient of the cross product is $1/\rho_{\mathrm{mass}}^{2}$.

**So the two obstructions are coupled and the coupling runs one way.** A baroclinic flow started from rest becomes rotational, so barotropicity is a sufficient condition for a flow to stay irrotational if it starts irrotational. The converse fails: a barotropic flow can be rotational, because vorticity can be given at the initial time or by a boundary. So barotropicity does not imply irrotationality, and the two conditions are not one condition.

**This is the first place the section's conditions are seen to be a system.** The three obstructions are usually stated as three independent hypotheses. They are not: baroclinicity manufactures vorticity, and viscosity manufactures entropy. A fluid that fails one of them tends to fail another, and the clean case — inviscid, barotropic, irrotational — is a case that has to be maintained rather than assumed.

## The Barotropic Families

**Four families cover the physics, and each has a name and an exponent.** Write the polytropic law as $p_{\mathrm{th}}=\kappa\rho_{\mathrm{mass}}^{\gamma}$ with $\kappa$ a constant. Then the sound speed follows from the exponent alone, $c_{\mathrm{s}}^{2}=\kappa\gamma\rho_{\mathrm{mass}}^{\gamma-1}$, and the families differ in $\gamma$.

| Fluid | $\gamma$ | $p_{\mathrm{th}}$ | $c_{\mathrm{s}}^{2}$ |
|---|---|---|---|
| Isothermal gas | $1$ | $\kappa\rho_{\mathrm{mass}}$ | $\kappa$ |
| Degenerate electron gas, relativistic | $4/3$ | $\kappa\rho_{\mathrm{mass}}^{4/3}$ | $\frac43\kappa\rho_{\mathrm{mass}}^{1/3}$ |
| Degenerate electron gas, non-relativistic | $5/3$ | $\kappa\rho_{\mathrm{mass}}^{5/3}$ | $\frac53\kappa\rho_{\mathrm{mass}}^{2/3}$ |
| Quadratic law | $2$ | $\kappa\rho_{\mathrm{mass}}^{2}$ | $2\kappa\rho_{\mathrm{mass}}$ |

**The isothermal case is the one with a constant sound speed.** A gas held at one temperature has $p_{\mathrm{th}}=\rho_{\mathrm{mass}}k_BT/(\mu_{\mathrm{mol}}m_u)$ with $\mu_{\mathrm{mol}}$ the molar mass in atomic units, so $\gamma=1$ and $c_{\mathrm{s}}^{2}=k_BT/(\mu_{\mathrm{mol}}m_u)$. The constant sound speed is what makes the linear wave equation exact for small disturbances, and the later article returns to it.

**The two middle cases are the ones a stellar interior supplies.** Degeneracy pressure in a dense core has $\gamma=5/3$ when the electrons are non-relativistic and $\gamma=4/3$ when they are ultra-relativistic, and the two exponents give the Chandrasekhar mass its value: the star is stable at $5/3$ and marginal at $4/3$. The pressure is barotropic to excellent accuracy because the temperature is negligible against the degeneracy energy, so the entropy does not enter.

**The quadratic case is the law of a medium with a pairwise interaction.** A contact interaction gives $p_{\mathrm{th}}=\frac{g}{2}\rho_{\mathrm{num}}^{2}$, which is $p_{\mathrm{th}}=\frac{g}{2m_{\mathrm{mrk}}^{2}}\rho_{\mathrm{mass}}^{2}$, so $\gamma=2$ with $\kappa=g/(2m_{\mathrm{mrk}}^{2})$. It is the case in which the later article's nonlinear wave equation is the cubic one, and [Superfluids and BECs: The Gross–Pitaevskii Equation as the Nonlinear Reverse Map](superfluids-and-becs-the-gross-pitaevskii-equation-as-the-nonlinear-reverse-map.html) works it out.

**The four rows are one family with one parameter, and the physics is in which parameter nature picks.** That is why the later article can write the nonlinear wave equation with a single function $V(\rho_{\mathrm{num}})$: the exponent is the only thing that changes from one fluid to another.

## Where the Condition Fails

**Barotropicity fails wherever a second thermodynamic variable is carried and matters.** Combustion carries the mixture fraction, and the pressure depends on the composition as well as on the density. A stellar interior carries the radiative flux, and the pressure depends on the temperature gradient, which is not a function of the density. The ocean carries salinity and temperature, and the pressure depends on both.

**Each failure has the same shape: an extra advected scalar.** The failing fluid carries a quantity $\chi$ with its own equation $\partial_{t'}\chi+\vec v\cdot\nabla\chi=\text{(source)}$, and the pressure is $p_{\mathrm{th}}(\rho_{\mathrm{mass}},\chi)$. The count is five again, and the fluid is outside the barotropic class for as long as the source does not drive $\chi$ to a function of $\rho_{\mathrm{mass}}$.

**So the condition is a statement about closure, not about thermodynamics.** A fluid is barotropic when its state is one-dimensional. A fluid whose state needs two variables is a fluid with one more degree of freedom than the count of the previous article allows, and the extra degree of freedom has no target in the field.

## The Two Terms of the Force

**A medium can supply a force that is not a pressure.** A fluid's force per unit mass is the pressure's gradient plus whatever else acts. Three cases are classical and worth naming. A body force, such as gravity, is a function of position and not of the density. A capillary stress, such as Korteweg's, depends on the gradients of the density and gives a force with two derivatives in it. A viscous stress depends on the strain rate and gives a force with one derivative in it. None of the three is a function of the density's value.

**So barotropicity constrains one term and not the force.** It says the pressure is a function of the density alone; it says nothing about the other terms. The separation is exact and it is what makes the later article's caveat necessary: the reverse map needs the pressure to be local in the density because its nonlinear term is local in the modulus, and it needs the second-gradient term because that term is what the Laplacian becomes. A fluid with the first and not the second is a first-order fluid and lies outside the image; a fluid with the second and not the first is a medium without a law of state.

$$
-\frac{1}{\rho_{\mathrm{mass}}}\nabla p_{\mathrm{th}}-\nabla Q_{\mathrm{kor}} ,
$$

with $Q_{\mathrm{kor}}$ the second-gradient term of [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html). The first term is the pressure's and the second is the medium's, and barotropicity is a statement about the first alone.

**The distinction is also why a barotropic fluid can fail the map and still be a fluid.** A pressureless medium is barotropic in the strongest sense, with $p_{\mathrm{th}}=0$ everywhere, and it can still carry a force that is not local in the density. Barotropicity is therefore a necessary condition of the image and not a sufficient one, and the gap between the two is the second-gradient term.

## The Count

**The ladder from five to two has three rungs and two conditions.** Each rung removes data, and each removal is one article of this section.

| Rung | Data | Removed by |
|---|---|---|
| General fluid | $5$ | — |
| Barotropic fluid | $4$ | this article: no independent entropy |
| Barotropic irrotational fluid | $2$ | the vorticity article: velocity is a gradient |

**Two rungs and not one, because neither condition implies the other.** A barotropic fluid can be rotational; an irrotational fluid can be baroclinic. The ladder is a conjunction, and the later article's map is defined on the bottom rung only.

**The bottom rung is the count of a complex amplitude.** An amplitude has two real data, a modulus and an argument, and the bottom rung has the density and the potential. The correspondence of counts is the whole of the reverse map's scope, and the articles of the next blocks are where the amplitude's other components are given names.

## What Is Established and What Is Interpretation

**Established.** That the pressure force per unit mass is $\nabla h-T\nabla s_{\mathrm{spc}}$ by Gibbs–Duhem, so it is a gradient exactly when the flow is isentropic, and that barotropicity is the sufficient form of that condition. That a general fluid's state needs two variables and a barotropic fluid's needs one, with the count falling from five to four. That the baroclinic torque is $\nabla\rho_{\mathrm{mass}}\times\nabla p_{\mathrm{th}}/\rho_{\mathrm{mass}}^{2}$ and vanishes for a barotropic fluid, by expansion. That the polytropic exponent fixes the sound speed, and that the four families of the table are the ones the physics supplies. That the field's fluid has no thermodynamic pressure and a quantum force that is not local in the density.

**Interpretation.** That the barotropic condition is a *closure* condition rather than a thermodynamic one, and that it is the fluid's best approximation to having no thermodynamics at all. That the coupling of the obstructions should be read as evidence that the clean case is fragile is a reading of the Bjerknes identity, not a theorem about fluids.

**Not claimed.** It is not claimed that barotropic fluids are rare. They are the norm in the applications that use them, and the table is short because the physics is short. It is not claimed that a baroclinic fluid has no wave equivalent; it is claimed that it is outside the class on which the map of the next article is defined. It is not claimed that the second-gradient term is a pressure: it is the divergence of a stress, which is a different object, and the stress is computed where the medium that carries it is treated.

## Summary

A fluid's pressure depends on two variables in general, the density and the specific entropy, and a barotropic fluid's depends on the density alone. The count falls from five to four.

The baroclinic torque is the source of vorticity in a fluid started from rest, and it vanishes exactly when the pressure is a function of the density. So barotropicity keeps an irrotational flow irrotational, and the converse does not hold.

By Gibbs–Duhem the pressure force is $\nabla h-T\nabla s_{\mathrm{spc}}$, a gradient exactly when the flow is isentropic. Barotropicity is the stronger hypothesis that makes it a gradient without any knowledge of the entropy field.

The barotropic families are the polytropes, and the exponent is the whole of the difference between them: $\gamma=1$ isothermal, $\gamma=4/3$ and $\gamma=5/3$ for the degenerate electron gas, $\gamma=2$ for a pairwise interaction.

The condition fails wherever a second advected scalar matters: combustion, a stellar interior, the ocean. The failure has one shape, an extra variable with its own equation.

Barotropicity is a condition on the pressure alone, and a medium can carry a force that is not a pressure: a body force, a capillary stress, a viscous stress. The capillary stress is the one the map's image needs, so barotropicity and the second-gradient term are conditions on two different terms of one force, and the map of the next article needs both.

The ladder from five data to two has two rungs, and neither condition implies the other.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $p_{\mathrm{th}}$ | Thermodynamic pressure |
| $\rho_{\mathrm{mass}},\ \rho_{\mathrm{num}}$ | Mass density and number density |
| $s_{\mathrm{spc}}$ | Specific entropy |
| $c_{\mathrm{s}}^{2}=(\partial p_{\mathrm{th}}/\partial\rho_{\mathrm{mass}})_{s_{\mathrm{spc}}}$ | Square of the sound speed |
| $\kappa$ | Polytropic constant |
| $\gamma$ | Polytropic exponent |
| $\mu_{\mathrm{mol}}$ | Molar mass in atomic units |
| $m_u$ | Atomic mass constant |
| $T$ | Temperature |
| $\vec\omega_{\mathrm{vrt}}$ | Vorticity, the curl of the velocity |
| $Q_{\mathrm{kor}}$ | Second-gradient term; the Korteweg term of the map's image |
| $g$ | Pairwise-interaction coupling of the quadratic law |
| $\chi$ | The second thermodynamic variable of a baroclinic fluid |
| $h$ | Specific enthalpy; $\mathrm{d}h=T\,\mathrm{d}s_{\mathrm{spc}}+\mathrm{d}p_{\mathrm{th}}/\rho_{\mathrm{mass}}$ |

## Further Reading

- Vilhelm Bjerknes, *Vorlesungen über hydrodynamische Fernkräfte nach C. A. Bjerknes' Theorie* (Barth, Leipzig, 1900–1902), for the circulation theorem and the torque that a baroclinic fluid exerts.
- Subrahmanyan Chandrasekhar, *An Introduction to the Study of Stellar Structure* (University of Chicago Press, 1939), ch. X, for the polytropes and for the degenerate electron gas at $\gamma=4/3$ and $\gamma=5/3$.
- Lev D. Landau and Evgeny M. Lifshitz, *Fluid Mechanics*, 2nd ed. (Pergamon, 1987), §§2, 4 and 7, for the law of state, the sound speed and the isentropic conditions.
- George K. Batchelor, *An Introduction to Fluid Dynamics* (Cambridge University Press, 1967), §3.5, for barotropic and baroclinic flows.
- François Golse, "The Boltzmann equation and its hydrodynamic limits," in *Handbook of Mathematical Fluid Dynamics*, vol. II (North-Holland, 2003), for the closure problem that barotropicity short-circuits.
- The companion articles: [The Euler and Continuity Equations in Biquaternionic Form](the-euler-and-continuity-equations-in-biquaternionic-form.html), [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html), [Viscosity and the Rayleigh Dissipation Function](viscosity-and-the-rayleigh-dissipation-function.html), [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html).
- The application of both terms to a quantum medium is in the spin-zero block of the index, where the second-gradient term is the quantum potential and its stress is computed.
