# __The Direction of the Fluid-Wave Correspondence, Field by Field__

## Introduction

**The direction of the correspondence is fixed by which object carries the constant.** A wave equation carries one constant of dimension action per mass — $\hbar$ when the wave equation is the quantum one, $\sigma_{\mathrm{dsp}}$ when it is a classical dispersion relation — and the constant is what the map's exponential needs. A fluid carries no such constant, and its data never supply one. Where a wave equation is fundamental, the fluid is derived from it by the forward map, exactly and generally. Where a fluid equation is fundamental, no wave equation follows in general, and where one follows it is nonlinear. That asymmetry is not a technicality of the map; it is the statement that the two objects are not on the same footing.

**The article writes $\hbar$ wherever the constant appears, because the fields it examines are the ones where the wave equation is quantum.** The slot is the same one the previous articles write $\sigma_{\mathrm{dsp}}$, and every statement below holds with either name in it.

**The article applies the previous five to the fields that use ordinary fluid equations.** The claim is narrow and it is testable field by field: in none of them is there a hidden linear Schrödinger, Klein–Gordon or Dirac equation, except in the cases where the wave equation is the fundamental object and the fluid is what it produces.

**The strongest objection is the one the section must answer, and it is the pressureless case.** A pressureless irrotational inviscid fluid with the second-gradient term *is* the reading of a free linear wave equation, so a counterexample exists and it has the smallest possible equation of state. The answer is that such a fluid is not an ordinary fluid: it has no pressure, no temperature and no entropy, and its only force is the Korteweg term, which is a second-gradient stress and not a law of state. It is the free field in fluid variables, and calling it an ordinary fluid is the error the objection makes.

**The second objection is viscosity, and it is answered by the heat equation.** A viscous potential flow in one dimension is linearisable, exactly, by the Hopf–Cole transformation. What it linearises to is a diffusion equation and not a wave equation — the overdamped branch of a damped wave equation — so the objection establishes the section's qualified claim rather than refuting its unqualified one.

## The Two Directions

**The forward direction is exact and general.** Every solution of a linear wave equation gives a fluid by $\psi=\sqrt{\rho_{\mathrm{num}}}e^{iS/\hbar}$, away from the nodes. The map is a rewriting, it loses nothing, and its only exception is the set where the density vanishes.

**The reverse direction is conditional and its output is nonlinear.** It is defined on barotropic irrotational inviscid flows that carry the quantum term, and on that class its output is

$$
i\hbar\,\partial_{t'}\psi=-\frac{\hbar^{2}}{2m}\Delta\psi+V(\rho_{\mathrm{num}})\psi ,
\qquad
\frac{\mathrm{d}V}{\mathrm{d}\rho_{\mathrm{num}}}=\frac{1}{\rho_{\mathrm{num}}}\frac{\mathrm{d}p_{\mathrm{th}}}{\mathrm{d}\rho_{\mathrm{num}}} ,
$$

which is linear exactly when the pressure is constant. Both statements are in [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html).

**The two directions are therefore not inverse in the sense of a change of variables.** A change of variables is available in both directions on the same class. Here the forward map is defined everywhere and the reverse only on a subclass, and on that subclass the reverse does not return the equation the forward map started from unless the pressure vanishes. The failure is not a loss of information; it is that the fluid's pressure is a term the wave equation does not have, and the reverse map has to invent a nonlinearity to hold it.

## The Three Conditions Are One

**"Irrotational, inviscid, barotropic" is not three hypotheses. It is one criterion cut into three pieces by the way it is usually stated.** The forward map produces a velocity that is a gradient and a force that is a gradient. The reverse map needs both properties back:

$$
\vec v=\frac{1}{m}\nabla S ,
\qquad
\mathrm{D}_{\mathrm{mat}}\vec v=-\nabla\Phi_{\mathrm{acc}} ,
$$

with $\Phi_{\mathrm{acc}}$ an acceleration potential, a scalar of dimension velocity squared.

**Given the two, the Hamilton–Jacobi equation is a definition and not an assumption.** Take the gradient of $\partial_{t'}S+\lvert\nabla S\rvert^{2}/2m+\Phi_{\mathrm{acc}}$ with $\vec v=\nabla S/m$: the first term contributes $\nabla\partial_{t'}S$, the second contributes $(\nabla S\cdot\nabla)\nabla S/m$ — the curl term of $\nabla(\lvert\vec v\rvert^{2}/2)$ vanishes because $\vec v$ is a gradient — and the third contributes $-\mathrm{D}_{\mathrm{mat}}\vec v$. The sum is zero by the second property, so the bracket is a function of time alone, and a function of time is absorbed into $S$. So $S$ exists and satisfies the equation, and nothing beyond the two properties is assumed.

**The first property is on the velocity, and it is irrotationality.** A gradient has no curl, so $\nabla\times\vec v=\vec 0$ is necessary, and on a simply connected domain it is sufficient. On a domain with a hole it is sufficient up to the period, which is the winding of [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html).

**The first property is the rank-zero member of a family, and the family is indexed by the rank of the vorticity.** A rotational velocity is not without potentials: the Clebsch form writes it with three functions, $\vec v=\nabla\phi_{\mathrm{clb}}/m+\alpha_{\mathrm{clb}}\nabla\beta_{\mathrm{clb}}/m$, and the pair $(\alpha_{\mathrm{clb}},\beta_{\mathrm{clb}})$ carries the whole vorticity. So what the reverse map needs is not the absence of vorticity but a vorticity whose rank the target can hold, and a single complex unknown holds one rank and no more. [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html) states the hierarchy, and states the medium whose data do carry a pair: the spinning fluid of the Dirac block.

**The second property is on the force, and the other two folk conditions are its two failure modes.** The force has three parts and each can fail to be a gradient on its own. The pressure part is a gradient exactly when the flow is isentropic, by the Gibbs–Duhem relation of [The Equation of State and the Barotropic Condition](the-equation-of-state-and-the-barotropic-condition.html), and barotropicity is the *stronger* hypothesis that makes it a gradient whatever the entropy field does. The viscous part is a gradient only in special flows — the unidirectional one is the case — and in general it is not, which is the inviscid condition. The external part is a gradient exactly when the external field is conservative.

**So the folk statement is one condition on the velocity and two on the force, and every one of them is necessary.** None is sufficient, and the insufficiency is the part the folk statement loses.

**What is missing is a condition on the potential and not on the flow.** With $\Phi_{\mathrm{acc}}$ arbitrary, the $\psi$ built from the flow obeys a Schrödinger equation whose potential is whatever $\Phi_{\mathrm{acc}}$ happens to be. For the fluid to be the reading of a wave equation of the theory's form, the potential must be

$$
\Phi_{\mathrm{acc}}=\frac{V(\rho_{\mathrm{num}})}{m}+\frac{Q_{\mathrm{qnt}}}{m} ,
$$

a function of the density plus the quantum term. Miss the first and the fluid is the reading of an equation with an external potential, which is linear and is not a law of the fluid; miss the second and the equation is nonlocal. [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html) exhibits the first failure with a number.

**There is a fourth distinction and it is not about shape but about sign.** A wave equation's potential is an energy and its $S$ is real; a dissipative flow's potential is a rate and its $S$ is imaginary. The map runs in both cases and produces two different kinds of equation. §*The One Liquid Case That Is Linear* is where this is used, and it is why the inviscid condition is not merely a condition about gradients.

## The Table

**The table is the article's content, and the reason column is the warrant.** Each row names a field, the status of a wave equivalent in it, and the reason the previous articles supply.

| Field | Wave equivalent | Reason |
|---|---|---|
| Irrotational inviscid barotropic hydrodynamics | yes, nonlinear | the reverse map; $V$ from $p_{\mathrm{th}}$ |
| The same, pressureless | yes, linear | the free wave equation; no pressure to hold |
| Irrotational inviscid, pressure not a function of the density | a linear equation with an external potential | the potential is of position, not of the density |
| Rotational hydrodynamics | no | vorticity, two data with no target |
| Viscous flow, Navier–Stokes | no wave; a diffusion equation in $1$D | dissipation has no action |
| Baroclinic flow | no | the state needs two variables |
| Geophysical flows, shallow water | no; KdV in a limit | rotational, baroclinic, weakly nonlinear |
| Plasma and magnetohydrodynamics | no; nonlinear analogues | structured, rotational, non-barotropic |
| Engineering computational fluid dynamics | no | viscous, rotational, often turbulent |
| Classical astrophysics | no | viscous or rotational, general state law |
| Wave dark matter | reversed | the Klein–Gordon equation is fundamental |
| Superfluids and condensates | reversed | the Gross–Pitaevskii equation is fundamental |
| Relativistic quantum plasmas | reversed | the Dirac equation is fundamental |

**The rows are of three kinds, and the third row of the first kind is the one that decides the thesis.** The first ten rows are fluids that carry a fluid equation as their fundamental law, and in none of them is a *free* linear wave equation hidden, the linear cases among them carrying an external potential instead. The third of them is the irrotational, inviscid, non-barotropic case: it passes the three conditions and its inversion is still a linear equation, with an external potential that the fluid's own pressure field produces and no law of state reproduces. The last three rows are fields in which a wave equation is fundamental and the fluid is derived. The pressureless row is the only place a free linear equation appears from a fluid, and it is not an ordinary fluid.

## The Reasons

**Rotational hydrodynamics has no wave equivalent because the vorticity has no target.** The Helmholtz decomposition splits the velocity into a gradient and a curl, and the curl's two independent components are data that a scalar wave function cannot hold. A fluid with vorticity conserves and amplifies a quantity that the field does not contain.

**The vorticity can be carried by potentials and that does not repair the row, which is why the row is about the size of the target and not about the existence of a representation.** The Clebsch pair supplies the two missing functions, and the wave function has exactly two and spends them on the modulus and the phase of the same flow. A rotational flow is therefore representable and unassignable at once: the pair exists and there is nowhere to put it. The same count is what makes the Dirac fluid possible, because a bispinor carries four factors and the velocity's frame is one of them; the three functions are then carried by a factor rather than by two potentials, and whether that leaves the vorticity of rank two is the question the Clebsch article states and does not answer. That is the content of [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html), and it is why the rotational row of the table is a row about scalars.

**Viscous flow has no wave equivalent because dissipation has no action.** The viscous term is odd under reversal of time and has a fixed sign, so no functional of the flow alone varies to it. The linearisation that does exist reaches a diffusion equation, which is the wave equation's imaginary-time continuation and not a wave.

**Baroclinic flow has no wave equivalent because its state is two-dimensional.** The pressure depends on the density and on a second advected variable, so the nonlinear term of the reverse map has no function to be; and the pressure force is not a gradient, so even the phase fails to exist.

**The non-barotropic row is the subtler failure and it is worth separating from the baroclinic one.** An incompressible irrotational flow is gradient-forced even when its pressure is not a function of the density, because a uniform density makes $(1/\rho_{\mathrm{mass}})\nabla p_{\mathrm{th}}$ a gradient by inspection. So the phase exists, the map runs, and the equation it produces has a potential that is a function of position. That is a wave equation with an external field, which is linear and is not a law of the fluid: the reverse map has produced a solution of somebody else's equation.

**The applied fields inherit the obstruction and add one of their own.** Geophysical flows are rotational and baroclinic at once, and their wave-like behaviour is the KdV equation of a weakly nonlinear long-wave limit, which is nonlinear and which exists because the limit discards the rotation. Plasma models carry a magnetic field and a velocity field coupled to each other, and their wave-like behaviour is a nonlinear mode coupling, not a linear equation. Computational fluid dynamics solves the Navier–Stokes equation directly, and its turbulence is the statement that the discarded nonlinearity is the whole of the interesting behaviour.

**Classical astrophysics is the field where the barotropic approximation is best and the wave equivalent is still absent.** A stellar interior is barotropic to excellent accuracy, and it is neither irrotational nor inviscid: it rotates and it radiates. The barotropic condition alone does not give the map.

## The Three Reversed Cases

**Wave dark matter is the cleanest reversal, because the wave equation is the fundamental law and the fluid is a derived description of it.** An ultralight scalar field obeys the Klein–Gordon equation, and its non-relativistic limit is a Schrödinger equation with a self-interaction. The fluid — density, velocity, quantum pressure — is the Madelung reading of that field, and [The Klein–Gordon Fluid](the-klein-gordon-fluid.html) is the block's account of it.

**Superfluids and condensates are the second reversal, and there the derived fluid is measured.** A dilute condensate obeys the Gross–Pitaevskii equation; its density and phase obey the Madelung pair; and the pair is what the two-fluid model of the condensate is built from. The linear Schrödinger equation is the non-interacting limit of the Gross–Pitaevskii equation, not the fundamental law.

**Relativistic quantum plasmas are the third, and there the derived fluid carries a spin.** The Dirac equation is the fundamental law for the constituent particles, and the fluid description — a density, a velocity, a spin density and a current — is derived from it. The fluid does not give an equation that looks like the Dirac equation; the Dirac equation gives the fluid, and the fluid's spin terms are the trace of it. **The derived fluid is a spinning fluid in the technical sense**, a Cosserat medium with an orientation at each point, so its rotationality is not a defect of the derivation but the general case: the classical fluid is the constrained member of that family, as [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html) sets out.

**In all three cases the direction of explanation is the same, and it is the direction the section has been arguing.** The wave equation is written first, because it is the law; the fluid is read from it, because it is the description. The fluids of these fields look like the fluids of the previous rows and they are not: their data include the field's own, and their equations are the forward map's output.

## The One Liquid Case That Is Linear

**The Hopf–Cole transformation is the only exact linearisation of a fluid equation the section uses, and read as a map it is the reverse map with an imaginary action quantum.** Burgers' equation in one dimension is carried by $u=-2\nu_{\mathrm{kin}}\partial_x\ln\psi$ into $\partial_{t'}\psi=\nu_{\mathrm{kin}}\partial_{xx}\psi$. The transformation is exact, and its output has an imaginary frequency, a positive kernel and an arrow of time.

**The identification is exact and it is the sharpest statement in the article.** Put $\hbar=-2im\nu_{\mathrm{kin}}$ and $V=0$ in the reverse map's output. Then $i\hbar=2m\nu_{\mathrm{kin}}$ and $-\hbar^{2}/2m=2m\nu_{\mathrm{kin}}^{2}$, so the equation reads $2m\nu_{\mathrm{kin}}\partial_{t'}\psi=2m\nu_{\mathrm{kin}}^{2}\partial_{xx}\psi$, which is $\partial_{t'}\psi=\nu_{\mathrm{kin}}\partial_{xx}\psi$. An imaginary action quantum turns the wave equation into the heat equation, exactly and with no remainder.

**So the failure of the viscous case is not a failure of the gradient test.** In one dimension the viscous force *is* a gradient, $\nu_{\mathrm{kin}}\partial_{xx}u=\partial_x(\nu_{\mathrm{kin}}\partial_xu)$, so a potential exists and the map runs. What fails is that the potential is a rate and not an energy: the Hopf–Cole $\psi=\exp(-\int u\,\mathrm{d}x/(2\nu_{\mathrm{kin}}))$ has a real logarithm, so the map's $S$ is imaginary. A conservative force gives a real action and an oscillating equation; a dissipative force gives a rate and a decaying one.

**So the exception does not produce a wave equation and it does not produce a linear fluid.** It produces a linear equation whose solutions do not oscillate, and whose physical content is the smoothing of a shock into a layer of width $\nu_{\mathrm{kin}}/u$. A reader who counts it as a wave equivalent has counted the heat equation as a wave equation.

**The second exact linearisation is a scattering problem, and it is not a solution map either.** The Korteweg–de Vries equation is integrable by the inverse scattering transform, whose auxiliary problem is the linear Schrödinger equation $-\varphi_{xx}+u\varphi=\lambda\varphi$. There the fluid $u$ is the *potential* of a linear equation and the unknown is an auxiliary wave function that is not the fluid. Integrability is not linearity, and the linear problem's unknown is not the flow.

**The two cases together are the honest boundary of the section's claim.** A fluid equation can be linearised, and when it is, the linear equation is either parabolic or a scattering problem. Neither is the free linear wave equation of the trilogy, and neither produces a fluid that looks like the trilinear fluid.

## What This Means for the Block

**The fluid layer is a reading of the field, not a model of a fluid.** The block's title says hydrodynamics because its variables are a fluid's, and the previous five articles have measured how far that vocabulary reaches. It reaches exactly as far as the field's data reach, and it stops where the pressure, the vorticity and the viscosity begin.

**Two of the block's denials become one statement.** [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html) denies that the reading is a superfluid and denies that it is a linear wave equivalent. The two denials are the two halves of this article's conclusion: the reading is not a superfluid because a superfluid's fluid is derived from an order parameter, and it is not a wave equivalent because the wave equation comes first. The block's order is the reverse of the order that would make either denial a problem.

**The direction also fixes what the block can and cannot borrow.** The vocabulary of circulation, vorticity and spin can be borrowed from fluid mechanics, because those are the variables the algebra supplies. The vocabulary of pressure, temperature and dissipation cannot, because those are variables the algebra does not supply. The block borrows the first and not the second, and this article is the statement of why the line falls where it does.

## What Is Established and What Is Interpretation

**Established.** That the reverse map's requirements are one integrability condition on the velocity and one on the force, the Hamilton–Jacobi equation following from the two by taking a gradient, and that the pressure part of the force is a gradient exactly when the flow is isentropic by Gibbs–Duhem, so that barotropicity is sufficient and not necessary. That the Hopf–Cole transformation is the reverse map with $\hbar=-2im\nu_{\mathrm{kin}}$, verified by substitution. That the forward map is exact and general away from nodes, and that the reverse map is defined only on a class and returns a nonlinear equation on it. That the linear output requires a pressureless fluid, which is not an ordinary fluid. That viscosity's exact linearisation reaches a diffusion equation and not a wave equation, and that the KdV's linear auxiliary problem has the fluid as its potential. That the fields in the table's last three rows are ones in which the wave equation is fundamental.

**Interpretation.** That the direction of explanation — wave to fluid — is a statement about which object carries the constants, and therefore about which object is the law. That the table's first nine rows support the thesis is a judgement about what counts as a wave equivalent; the article's criterion is stated, and a reader who accepts a different criterion will read the table differently.

**Not claimed.** It is not claimed that a fluid can never be fundamental. It is claimed that no field in the table has a fluid as its fundamental law and a linear wave equation as a consequence. It is not claimed that the table is exhaustive; it is the list of the fields whose equations are the ones this section has analysed. It is not claimed that the nonlinearities of the applied fields are of the Gross–Pitaevskii form; their nonlinearities are their own, and the reason column says only that they are not linear.

## Summary

The forward map, wave to fluid, is exact and general. The reverse map, fluid to wave, is conditional and its output is nonlinear.

Its conditions are one on the velocity and one on the force. The velocity must be a gradient, which is irrotationality. Every force must be a gradient, which needs the pressure force to be isentropic — barotropicity being its sufficient form — the viscous force to be absent in general, and the external field to be conservative.

So the three conditions of the folk statement are necessary and not sufficient. The missing condition is on the potential: it must be a function of the density plus the quantum term. Miss the density and the fluid reads as an equation with an external potential; miss the quantum term and the equation is nonlocal.

And the potential must be an energy and not a rate. With an imaginary action quantum the same map gives a diffusion equation, which is exactly the Hopf–Cole case and exactly why it is not a wave equivalent.

On the class the conditions fix, the wave equation's nonlinear term is the pressure law, and the equation is linear exactly when the pressure is constant. The free linear equations of the trilogy are the pressureless member, and the pressureless member is a dust whose only force is the quantum potential.

In the fields that use ordinary fluid equations there is no hidden linear wave equation. Where a wave equivalent exists it is nonlinear; where the fluid is pressureless it is the free equation, and the fluid is not ordinary; where the fluid is viscous the linearisation reaches a diffusion equation and not a wave.

The three exceptions run the other way. In wave dark matter, in condensates and in relativistic quantum plasmas the wave equation is fundamental and the fluid is derived. The direction of explanation follows the constants, and the constants are in the wave equation.

The block's two denials are one statement: the reading is a re-coordinatisation of the field, so it is neither a superfluid's fluid nor a source of wave equations.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\psi=\sqrt{\rho_{\mathrm{num}}}e^{iS/\hbar}$ | Wave function; the field's reading |
| $\rho_{\mathrm{num}}$ | Number density |
| $S$ | Action; the phase is $S/\hbar$ |
| $V(\rho_{\mathrm{num}})$ | Nonlinear term of the reverse map |
| $p_{\mathrm{th}}$ | Thermodynamic pressure |
| $Q_{\mathrm{qnt}}$ | Quantum potential |
| $\vec\omega_{\mathrm{vrt}}$ | Vorticity |
| $\nu_{\mathrm{kin}}$ | Kinematic viscosity |
| $\varphi$ | Auxiliary wave function of the KdV scattering problem |
| $u$ | Velocity of the one-dimensional flow; also the KdV field |
| $\lambda$ | Spectral parameter of the scattering problem |
| $\hbar,\ m$ | The two constants the wave equation carries |
| $c_{\mathrm{s}}$ | Sound speed |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1926) 322–326, for the forward direction.
- Edward A. Spiegel, "Fluid dynamical form of the linear and nonlinear Schrödinger equations," *Physica D* **1** (1980) 236–240, for the hydrodynamic reading of the nonlinear equation and its linear limit.
- Gérald B. Whitham, *Linear and Nonlinear Waves* (Wiley, 1974), ch. 12–13 and 17, for the shallow-water limit and for the KdV equation as its weakly nonlinear reduction.
- Vladimir E. Zakharov, "Collapse of Langmuir waves," *Soviet Physics JETP* **35** (1972) 908–914, for the nonlinear plasma model whose wave description is a nonlinear Schrödinger equation.
- Rémi Hakim, *Introduction to Relativistic Statistical Mechanics: Classical and Quantum* (World Scientific, 2011), ch. 9, for the fluid description derived from the Dirac equation in a relativistic plasma.
- Lam Hui, Jeremiah P. Ostriker, Scott Tremaine and Edward Witten, "Ultralight scalars as cosmological dark matter," *Physical Review D* **95** (2017) 043541, and Hsi-Yu Schive, Tzihong Chiueh and Tom Broadhurst, "Cosmic structure as the quantum interference of a coherent dark wave," *Nature Physics* **10** (2014) 496–499, for the wave-first direction in cosmology.
- The companion articles: [The Euler and Continuity Equations in Biquaternionic Form](the-euler-and-continuity-equations-in-biquaternionic-form.html), [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html), [Viscosity and the Rayleigh Dissipation Function](viscosity-and-the-rayleigh-dissipation-function.html), [The Equation of State and the Barotropic Condition](the-equation-of-state-and-the-barotropic-condition.html), [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html), [Superfluids and BECs: The Gross–Pitaevskii Equation as the Nonlinear Reverse Map](superfluids-and-becs-the-gross-pitaevskii-equation-as-the-nonlinear-reverse-map.html).
- [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html), for the two denials this article unifies.
