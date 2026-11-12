# __The One-Dimensional Reverse Map: Characteristics, KdV, Hopf__

## Introduction

**One dimension is the most favourable case for the reverse map, and it is still not linear.** Every one-dimensional flow is irrotational, because a velocity that depends on one coordinate has a curl that vanishes identically. So the obstruction of [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html) is vacuous, the count closes at two data for any barotropic inviscid flow, and the reverse map of [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html) is defined on the whole class. What the map returns is nonlinear, and this article shows why in three successive approximations: the inviscid case, the viscous case and the dispersive case.

**The article exists because a reader is entitled to ask what the best case gives.** If a linear wave equivalent is anywhere, it is here: one dimension, no rotation, no baroclinicity. The answer is that the best case gives three nonlinear equations and two linear objects, and the two linear objects are a diffusion equation and a scattering problem, neither of which is the fluid's wave equivalent.

**The three equations are Hopf's, Burgers' and Korteweg–de Vries', and they are the same fluid under three different additions.** Hopf's equation has no pressure and no viscosity; Burgers' adds viscosity; KdV adds dispersion. Each addition changes the character of the solution and none of them produces a linear wave equation.

## Why One Dimension Is the Favourable Case

**A one-dimensional flow is irrotational for free.** Take $\vec v=u(x)\,\vec e_x$, a velocity with one component depending on one coordinate. Its curl is

$$
\nabla\times\vec v=\bigl(\partial_yu_z-\partial_zu_y\bigr)\vec e_x+\dots=0,
$$

because every transverse derivative of every component vanishes. So the potential exists, $\vec v=\nabla S/m$ reduces to $u=(1/m)\,\partial_xS$, and the first condition of the reverse map costs nothing.

**The count closes at two and the map is therefore defined everywhere on the barotropic class.** The data are the density and the potential, which is exactly a wave function's modulus and argument. So one dimension is the case in which the reverse map has no obstruction of counting at all.

**What remains is the pressure, and the pressure is the whole of the difficulty.** A barotropic one-dimensional flow with a non-constant pressure maps to a nonlinear wave equation by the previous article's formula, and the formula is not optional. So the favourable case isolates the obstruction that counting cannot see.

## The Two Families and the Characteristics

**The one-dimensional system is two equations for two unknowns.** Written on the density and the velocity,

$$
\partial_{t'}\rho_{\mathrm{mass}}+\partial_x\bigl(\rho_{\mathrm{mass}}u\bigr)=0,
\qquad
\partial_{t'}u+u\,\partial_xu=-\frac{1}{\rho_{\mathrm{mass}}}\partial_xp_{\mathrm{th}} .
$$

For a barotropic fluid the pressure is a function of the density, so the second equation closes and the system is hyperbolic with two characteristic speeds.

**The characteristic speeds are the sound speed carried by the flow.** Linearising about a uniform state with density $\rho_0$ and sound speed $c_{\mathrm{s}}$, the two speeds are

$$
\lambda_{\pm}=u\pm c_{\mathrm{s}},
$$

and the corresponding Riemann invariants are constant along the two families of characteristics. A simple wave is a solution in which one invariant is uniform, and its characteristics are straight lines.

**The linear wave equation's characteristics are the same two speeds in one case only.** A linear wave equation has characteristics $\mathrm{d}x/\mathrm{d}t'=\pm c_0$ with $c_0$ constant, which is the linearisation about a state at rest with constant sound speed. So the linear equation is the characteristics' *linearised* form, not their exact form. The distinction matters because a Riemann invariant is constant along a characteristic, and the constancy is what makes the exact solution nonlinear: two characteristics of the same family carry different invariants and therefore move at different speeds.

**That is the mechanism by which a smooth solution breaks.** If the speed of a point depends on the value carried there, a profile with a decreasing speed steepens, and the steepening is the gradient catastrophe of the next section. A linear equation has no such mechanism, because its characteristic speeds are the same everywhere.

## The Inviscid Case Is Not Linear

**With no pressure and no viscosity the system reduces to Hopf's equation.** Set $p_{\mathrm{th}}=0$ and take a uniform density, so that the continuity equation decouples. Then

$$
\partial_{t'}u+u\,\partial_xu=0 ,
$$

whose solution is implicit,

$$
u(x,t')=f\bigl(x-u(x,t')\,t'\bigr),
$$

with $f$ the initial profile.

**The implicit solution is exact and it breaks in finite time.** Differentiating with respect to $x$ gives

$$
\partial_xu=\frac{f'}{1+f'\,t'},
$$

so the gradient diverges at $t'_{c}=-1/\inf f'$ whenever the initial slope is negative somewhere. The solution stays single-valued until $t'_{c}$ and after it the implicit equation has several branches. The fluid's answer is a shock, and the shock is not a solution of the differential equation but a solution of the conservation law in the weak sense.

**The solution is a Legendre transform and not a linear superposition.** Writing $u=\partial_x\phi$ turns Hopf's equation into $\partial_{t'}\phi+\frac12(\partial_x\phi)^{2}=0$, whose viscosity solution is

$$
\phi(x,t')=\min_{y}\left[\phi_0(y)+\frac{(x-y)^{2}}{2t'}\right],
$$

the Hopf–Lax formula. The formula is exact, it is a minimum over the initial data, and it is the closest a fluid comes to a superposition principle: the minimum replaces the sum, and the envelope replaces the interference.

**So the inviscid favourable case gives a nonlinear equation, a finite-time catastrophe and a variational formula.** None of the three is a linear wave equation, and the reason is that the characteristic speed is the unknown itself.

## The Viscous Case Linearises to a Diffusion Equation

**Adding viscosity gives Burgers' equation, and Burgers' equation is exactly linearisable.** With $\nu_{\mathrm{kin}}>0$,

$$
\partial_{t'}u+u\,\partial_xu=\nu_{\mathrm{kin}}\,\partial_{xx}u ,
$$

and the Hopf–Cole transformation $u=-2\nu_{\mathrm{kin}}\partial_x\ln\psi$ carries it into $\partial_{t'}\psi=\nu_{\mathrm{kin}}\partial_{xx}\psi$. The check is a differentiation and it is exact, as [Viscosity and the Rayleigh Dissipation Function](viscosity-and-the-rayleigh-dissipation-function.html) verifies on the heat kernel, where $u=x/t'$.

**The linearisation smooths the catastrophe instead of removing the nonlinearity's origin.** The shock of the inviscid case becomes a layer of width of order $\nu_{\mathrm{kin}}/u$, and the layer's profile is the heat kernel's logarithm. So the viscous case has a linear equivalent and the equivalent is parabolic: its frequency is imaginary, its kernel is positive, and its solutions do not oscillate.

**The point of the example is that linearity and waving come apart.** A reader who equates "linearisable" with "has a wave equivalent" will take Burgers' equation as a counterexample to the section. It is not: it is the case that shows the section's thesis must be stated about *wave* equations, which is how it is stated.

## The Dispersive Case Is Nonlinear and Integrable

**Adding dispersion instead of viscosity gives the Korteweg–de Vries equation.** In the weakly nonlinear long-wave limit of a shallow layer of depth $H_0$, the surface elevation obeys

$$
\partial_{t'}\eta+c_0\,\partial_x\eta+\tfrac32\frac{c_0}{H_0}\eta\,\partial_x\eta+\tfrac16c_0H_0^{2}\,\partial_{xxx}\eta=0,
\qquad
c_0=\sqrt{g_{\mathrm{gr}}H_0},
$$

with $g_{\mathrm{gr}}$ the gravitational acceleration. Rescaling puts it in the standard form

$$
\partial_{t'}u+6u\,\partial_xu+\partial_{xxx}u=0 .
$$

**The balance of steepening against dispersion gives a travelling pulse whose width and speed are fixed by its amplitude.** The solution is

$$
u=u_0\,\mathrm{sech}^{2}\!\left(\sqrt{\frac{u_0}{2}}\,\bigl(x-2u_0t'\bigr)\right),
$$

and it is checked by differentiating: the three terms cancel identically for every $u_0>0$. The speed is twice the amplitude, so the taller pulse travels faster. That is the opposite of a linear dispersive wave, whose speed is fixed by the medium, and it is the signature that the balance is nonlinear.

**The equation is integrable and its integrability is not linearity.** The Korteweg–de Vries equation has a Lax pair,

$$
L=-\partial_x^{2}+u,
\qquad
P=-4\partial_x^{3}+6u\,\partial_x+3\,\partial_xu,
\qquad
\partial_{t'}L=[P,L],
$$

and the pair's first operator is a Schrödinger operator whose potential is the fluid. The inverse scattering transform solves the initial-value problem by evolving the scattering data linearly and reconstructing the potential, so the *method* is linear and the *equation* is not.

**The auxiliary problem is where a linear Schrödinger equation appears, and its unknown is not the fluid.** The scattering problem is $-\varphi_{xx}+u\varphi=\lambda\varphi$: the fluid $u$ is the potential, and $\varphi$ is an auxiliary wave function that has no fluid reading. So the linear equation of the pair is linear in the wrong variable, and a reader who takes it for the fluid's wave equivalent has taken the potential for the solution. The error is the same one the previous articles name in another place: reading a term of an equation for the unknown.

## What One Dimension Teaches

**The best case gives no linear wave equation, and the reason is structural.** In one dimension the vorticity obstruction is vacuous and the count closes, so the reverse map is defined on the whole barotropic class. Its output is nonlinear whenever the pressure is non-constant, and the three approximate equations of this article are what the nonlinearity does in three regimes: a catastrophe, a smoothed catastrophe and a dispersive balance.

**The two linear objects that do appear are of two other kinds.** The heat equation of the viscous case is parabolic: it is the wave equation continued to imaginary time, and its solutions do not oscillate. The scattering problem of the integrable case is linear in an auxiliary function and has the fluid as its potential. Neither is the fluid's wave equivalent.

**So the article closes the section's argument at its most favourable point.** A reader who wants the linear trilogy to be recoverable from a fluid must produce it here, in one dimension with no obstruction. The article has produced, in its place, a catastrophe, a diffusion equation and a scattering transform, and the verdict is that the recoverability is not there.

## What Is Established and What Is Interpretation

**Established.** That a one-dimensional flow is irrotational identically, so the reverse map's first condition costs nothing. That the characteristic speeds of a barotropic flow are $u\pm c_{\mathrm{s}}$ and that the linear wave equation's characteristics are their linearisation about a state at rest. That Hopf's equation's implicit solution breaks at $t'_{c}=-1/\inf f'$ and that its viscosity solution is the Hopf–Lax minimum. That the Hopf–Cole transformation is exact. That the KdV soliton of the stated form solves the equation, and that its Lax pair has the fluid as the potential of a Schrödinger operator.

**Interpretation.** That the three equations are the three regimes of one fluid is a reading of their derivations, and each derivation has its own small parameter. That the Lax pair's linear problem should be read as "linearity in the wrong variable" is a reading of the inverse scattering transform, not a theorem about it: the transform is a linearisation of the solution method by construction.

**Not claimed.** It is not claimed that the KdV equation is the only dispersive reduction of a shallow layer; it is the leading one in the long-wave limit. It is not claimed that Burgers' equation's linearisation extends to three dimensions; it does so for potential flow only. It is not claimed that integrability is rare or common; the article uses one integrable equation and says nothing about how many there are.

## Summary

In one dimension every flow is irrotational, so the reverse map's first condition is vacuous and the count closes at two data. The remaining obstruction is the pressure.

The characteristic speeds of a barotropic flow are $u\pm c_{\mathrm{s}}$, and the linear wave equation's characteristics are their linearisation about rest. The exact characteristics carry the unknowns, which is why a smooth profile steepens.

With no pressure and no viscosity the flow obeys Hopf's equation. Its implicit solution breaks at $t'_{c}=-1/\inf f'$, its weak continuation is a shock, and its viscosity solution is the Hopf–Lax minimum over the initial data.

With viscosity the flow obeys Burgers' equation, which the Hopf–Cole transformation carries exactly into the heat equation. The linearisation is exact and the equation is parabolic, so the shock becomes a layer and the solution does not oscillate.

With dispersion the flow obeys the Korteweg–de Vries equation, whose soliton $u_0\,\mathrm{sech}^{2}$ balances steepening against dispersion and whose speed is twice its amplitude. The equation is integrable through a Lax pair whose first operator is a Schrödinger operator with the fluid as its potential.

The two linear objects of the article are a diffusion equation and a scattering problem. Neither is the fluid's wave equivalent, and the best case therefore gives no linear wave equation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $u$ | One-dimensional velocity; also the KdV field |
| $\rho_{\mathrm{mass}}$ | Mass density |
| $p_{\mathrm{th}}$ | Thermodynamic pressure |
| $c_{\mathrm{s}}$ | Sound speed |
| $\lambda_{\pm}=u\pm c_{\mathrm{s}}$ | Characteristic speeds |
| $f$ | Initial velocity profile |
| $t'_{c}=-1/\inf f'$ | Time of the gradient catastrophe |
| $\phi$ | Potential with $u=\partial_x\phi$; Hopf–Lax function |
| $\psi$ | Hopf–Cole potential |
| $\nu_{\mathrm{kin}}$ | Kinematic viscosity |
| $c_0=\sqrt{g_{\mathrm{gr}}H_0}$ | Long-wave speed of the shallow layer |
| $H_0$ | Rest depth of the layer |
| $g_{\mathrm{gr}}$ | Gravitational acceleration |
| $u_0$ | Amplitude of the KdV soliton; speed $2u_0$ |
| $L,\ P$ | Lax pair of the KdV equation |
| $\varphi$ | Auxiliary wave function of the scattering problem |
| $\lambda$ | Spectral parameter |

## Further Reading

- Eberhard Hopf, "The partial differential equation $u_t+uu_x=\mu u_{xx}$," *Communications on Pure and Applied Mathematics* **3** (1950) 201–230, for the equation, the transformation and the explicit solution.
- Peter D. Lax, "Hyperbolic systems of conservation laws II," *Communications on Pure and Applied Mathematics* **10** (1957) 537–566, for the formula that carries his name and for the weak solutions of the inviscid equation.
- Diederik J. Korteweg and Gustav de Vries, "On the change of form of long waves advancing in a rectangular canal, and on a new type of long stationary waves," *Philosophical Magazine* **39** (1895) 422–443, for the equation and the solitary wave.
- Norman J. Zabusky and Martin D. Kruskal, "Interaction of 'solitons' in a collisionless plasma and the recurrence of initial states," *Physical Review Letters* **15** (1965) 240–243, for the numerical discovery of the elastic collision of the pulses.
- Clifford S. Gardner, John M. Greene, Martin D. Kruskal and Robert M. Miura, "Method for solving the Korteweg–de Vries equation," *Physical Review Letters* **19** (1967) 1095–1097, and Peter D. Lax, "Integrals of nonlinear equations of evolution and solitary waves," *Communications on Pure and Applied Mathematics* **21** (1968) 467–490, for the inverse scattering transform and the Lax pair.
- Gérald B. Whitham, *Linear and Nonlinear Waves* (Wiley, 1974), ch. 12–13, for the shallow-water reduction and its characteristic structure.
- The companion articles: [Viscosity and the Rayleigh Dissipation Function](viscosity-and-the-rayleigh-dissipation-function.html), [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html), [The Direction of the Fluid-Wave Correspondence, Field by Field](the-direction-of-the-fluid-wave-correspondence-field-by-field.html).
