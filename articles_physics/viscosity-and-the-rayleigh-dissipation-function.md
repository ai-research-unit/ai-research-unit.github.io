# __Viscosity and the Rayleigh Dissipation Function__

## Introduction

**Viscosity is the one obstruction of the section that counting does not see.** The vorticity of the previous article removes two data and the law of state removes one; viscosity removes none. A viscous fluid at a point carries the same density and the same three velocity components as an inviscid one. So the count of [The Euler and Continuity Equations in Biquaternionic Form](the-euler-and-continuity-equations-in-biquaternionic-form.html) closes for both, and the obstruction that viscosity raises has to be found somewhere else.

**It is found in the action.** The viscous force is not the variation of a functional of the flow, so there is no action to vary and no phase to read off it. The energy falls at a rate the Rayleigh dissipation function fixes, the fall has a sign in time, and a term with a sign in time has no place in an action that is even in the velocities. That is the obstruction, and it is structural rather than numerical.

**The sharpest test of the thesis is that a linear equivalent nevertheless exists.** In one dimension, Burgers' equation is carried by the Hopf–Cole transformation into the heat equation, which is linear. So the claim that a viscous flow has no linear equivalent is false as stated. What is true is narrower and stronger: the linear equation it reaches is a diffusion equation, not a wave equation. That distinction is the reason the section's thesis is worded "no linear *wave* equivalent" throughout.

**The article therefore does two things.** It states the viscous stress and its dissipation exactly, and it shows what the linearisation that does exist gives. The second half is not a complication; it is what makes the first half's claim precise.

## The Stress

**The Newtonian stress is a symmetric tensor linear in the strain rate.** The strain rate is the symmetric part of the velocity gradient,

$$
S_{ij}=\tfrac12\bigl(\partial_iv_j+\partial_jv_i\bigr),
$$

and its trace is the divergence, $\delta_{ij}S_{ij}=\nabla\cdot\vec v$. The stress is

$$
\sigma_{ij}=-p_{\mathrm{th}}\,\delta_{ij}+2\eta_{\mathrm{shr}}S_{ij}+\zeta_{\mathrm{blk}}\,\delta_{ij}\,\nabla\cdot\vec v ,
$$

with $\eta_{\mathrm{shr}}$ the shear viscosity and $\zeta_{\mathrm{blk}}$ the bulk viscosity. The first term is the pressure of the inviscid case; the second is the shear stress, which opposes the shearing of the flow; the third is the resistance to compression.

**The stress has three parts and each has a different status.** The pressure is a datum fixed by the law of state. The shear term is what makes a fluid stick to a wall, and it is the term that carries the fluid's viscosity in ordinary language. The bulk term is the one that survives in a purely compressive flow, and it vanishes for a monatomic ideal gas at the level of the kinetic theory.

**The equation of motion is the divergence of the stress.** Euler's equation gains one term,

$$
\partial_{t'}\vec v+\bigl(\vec v\cdot\nabla\bigr)\vec v=-\frac{1}{\rho_{\mathrm{mass}}}\nabla p_{\mathrm{th}}+\frac{1}{\rho_{\mathrm{mass}}}\partial_j\sigma_{\mathrm{vsc},ij}+\vec f_{\mathrm{ext}},
$$

with $\sigma_{\mathrm{vsc},ij}=2\eta_{\mathrm{shr}}S_{ij}+\zeta_{\mathrm{blk}}\delta_{ij}\nabla\cdot\vec v$ the viscous part. For constant $\eta_{\mathrm{shr}}$ and an incompressible flow this is $\nu_{\mathrm{kin}}\Delta\vec v$ with the kinematic viscosity

$$
\nu_{\mathrm{kin}}=\frac{\eta_{\mathrm{shr}}}{\rho_{\mathrm{mass}}},
$$

and with that term the equation is the Navier–Stokes equation.

## The Dissipation Function

**The rate at which the stress does work on the flow is twice the dissipation function.** Define

$$
F_{\mathrm{rlh}}=\eta_{\mathrm{shr}}\,S_{ij}S_{ij}+\tfrac12\zeta_{\mathrm{blk}}\bigl(\nabla\cdot\vec v\bigr)^{2},
$$

the continuum form of Rayleigh's dissipation function. Then

$$
\sigma_{\mathrm{vsc},ij}\,\partial_jv_i=2F_{\mathrm{rlh}},
$$

by expansion: the shear part contributes $2\eta_{\mathrm{shr}}S_{ij}S_{ij}$ because $\sum_{ij}(\partial_jv_i)S_{ij}=\sum_{ij}S_{ij}S_{ij}$, and the bulk part contributes $\zeta_{\mathrm{blk}}(\nabla\cdot\vec v)^{2}$. The identity is exact for every differentiable flow, and it is the continuum reading of $\mathrm{d}E/\mathrm{d}t'=-2F$ in [Lagrangian and Hamiltonian Mechanics in Biquaternionic Form](lagrangian-and-hamiltonian-mechanics-in-biquaternionic-form.html).

**The energy of an isolated viscous flow decreases.** With no external force and no flux through the boundary,

$$
\frac{\mathrm{d}E}{\mathrm{d}t'}=-2\int F_{\mathrm{rlh}}\,\mathrm{d}^{3}r\le0,
$$

and the equality holds only at rest. The functional $F_{\mathrm{rlh}}$ is a sum of squares, so it is non-negative, and it vanishes exactly when the strain rate and the divergence vanish together.

**The same quantity is the entropy production.** With no heat conduction, the internal energy balance is $\rho_{\mathrm{mass}}T\,\mathrm{d}s_{\mathrm{spc}}/\mathrm{d}t'=2F_{\mathrm{rlh}}$, so

$$
\partial_{t'}s_{\mathrm{ent}}+\nabla\cdot\bigl(s_{\mathrm{ent}}\vec v\bigr)=\frac{2F_{\mathrm{rlh}}}{T}\ge0 .
$$

The sign is fixed and it is the sign of the second law. A term with a fixed sign cannot be the variation of a functional that is even in the velocities, and that is the obstruction in one sentence.

## Why There Is No Action

**Rayleigh's device inserts the force; it does not derive it.** The classical device keeps the equations in Lagrangian form by putting the viscous force on the right-hand side,

$$
\frac{\mathrm{d}}{\mathrm{d}t'}\frac{\partial\mathrm{Lag}}{\partial(\mathrm{d}q_i/\mathrm{d}t')}-\frac{\partial\mathrm{Lag}}{\partial q_i}=-\frac{\partial F}{\partial(\mathrm{d}q_i/\mathrm{d}t')},
$$

and [Lagrangian and Hamiltonian Mechanics in Biquaternionic Form](lagrangian-and-hamiltonian-mechanics-in-biquaternionic-form.html) states what this costs: the force is added by hand, the energy stops being conserved, and the formalism's symmetry is not restored. The equation is Lagrange's equation plus a term, not the variation of one functional.

**A variational formulation exists and it is not the one that matters.** Doubling the variables, adding an auxiliary field, or using a principle with a dissipation functional all reproduce the viscous equations. They do so at a price: the action is not a function of the flow alone, and its conjugate momentum is not the flow's momentum. An action that needs an auxiliary field describes a larger system, and whatever is read from its phase belongs to the larger system. The viscous fluid is then a projection of that system and not its solution.

**The time-reversal argument is the cleanest statement.** The viscous term is odd under $t'\mapsto-t'$, and it has a fixed sign. An action built from the flow alone is even in the time derivatives, because the Lagrangian is a function of positions and velocities and a reversal of time reverses the velocities twice. So no action of the flow alone can produce a term whose sign is fixed under reversal. This is not a failure of ingenuity; it is a parity mismatch.

**So viscosity removes the phase and not a datum.** The four data of the barotropic fluid are untouched, and the count of the section is unchanged. What is gone is the object whose gradient would be the velocity: the phase exists when the flow extremises an action, and a dissipative flow does not.

## The One-Dimensional Exception

**In one dimension the viscosity obstruction is removable, and the equation it reaches is linear.** Burgers' equation is

$$
\partial_{t'}u+u\,\partial_xu=\nu_{\mathrm{kin}}\,\partial_{xx}u ,
$$

the one-dimensional Navier–Stokes equation for a flow with no pressure. The Hopf–Cole transformation

$$
u=-2\nu_{\mathrm{kin}}\,\partial_x\ln\psi
$$

carries it into the heat equation

$$
\partial_{t'}\psi=\nu_{\mathrm{kin}}\,\partial_{xx}\psi ,
$$

which is linear. The check is a differentiation: with $\psi$ solving the heat equation, $u$ as defined solves Burgers' equation identically, and the check is exact for every positive $\nu_{\mathrm{kin}}$.

**The check is worth writing on a case.** Take the heat kernel $\psi=(t')^{-1/2}\exp(-x^{2}/(4\nu_{\mathrm{kin}}t'))$. Then

$$
u=-2\nu_{\mathrm{kin}}\,\partial_x\ln\psi=\frac{x}{t'},
$$

which solves Burgers' equation with no pressure: $\partial_{t'}u=-x/t'^{2}$, $u\partial_xu=x/t'^{2}$, and $\nu_{\mathrm{kin}}\partial_{xx}u=0$. The three terms cancel pairwise, and the solution is the inviscid rarefaction written in similarity variables.

**In three dimensions the transformation survives only for potential flow.** With $\vec v=-2\nu_{\mathrm{kin}}\nabla\ln\psi$ and $\psi$ solving $\partial_{t'}\psi=\nu_{\mathrm{kin}}\Delta\psi$, the vector Burgers equation holds identically, because the two identities used in one dimension are the gradient of the scalar ones. A flow with a non-vanishing curl is not of this form, and for it no such transformation is known. So even the exceptional linearisation is a potential-flow statement, and the vorticity obstruction of [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html) is untouched.

## Why the Heat Equation Is Not a Wave Equation

**The dispersion relation decides it.** A mode of the heat equation is $\exp(i(kx-\omega t'))$ with

$$
-i\omega=-\nu_{\mathrm{kin}}k^{2},
\qquad
\omega=-i\nu_{\mathrm{kin}}k^{2},
$$

a purely imaginary frequency. A mode of a wave equation is $\omega=\pm ck$, real. The first decays at a rate proportional to $k^{2}$ and does not oscillate; the second oscillates and does not decay. No solution of the heat equation interferes in the sense a wave interferes, because interference is the addition of two phases and a decaying amplitude has no phase to add.

**The kernel shows the same thing from the other side.** The heat kernel is positive everywhere for $t'>0$, so a disturbance at one point is felt everywhere immediately, with an amplitude that decays. A wave equation's kernel is supported on the cone: a disturbance is felt at a point only after the wave has had time to arrive. The two kernels are different objects and no change of variables turns one into the other.

**The heat equation is the overdamped limit of a damped wave equation.** Take

$$
\partial_{t'}^{2}u+\frac{1}{\tau_{\mathrm{dmp}}}\partial_{t'}u=c^{2}\Delta u ,
$$

a wave equation with a friction term of relaxation time $\tau_{\mathrm{dmp}}$. For disturbances slow on the scale $\tau_{\mathrm{dmp}}$ the second derivative is negligible against the first and the equation closes to $\partial_{t'}u=\tau_{\mathrm{dmp}}c^{2}\Delta u$, which is the heat equation with $\nu_{\mathrm{kin}}=\tau_{\mathrm{dmp}}c^{2}$.

**The limit is a statement about spectra, and it is why the exception is real but narrow.** A damped wave equation has complex frequencies, $\omega=-i/(2\tau_{\mathrm{dmp}})\pm\sqrt{c^{2}k^{2}-1/(4\tau_{\mathrm{dmp}}^{2})}$, so it oscillates while it decays and its over-damped branch does not. At long wavelength the branch that survives is the diffusive one, and at short wavelength the two branches are the two waves. So the heat equation is the long-wavelength face of a wave equation, not a different equation reached from a different fluid.

**So the exception confirms the thesis instead of breaking it.** A viscous flow does have a linear equivalent, and the equivalent is a diffusion equation, which is the overdamped face of a damped wave equation. What viscosity removes is the sustained oscillation, and with it the phase that a wave reading needs. The claim the section needs is therefore the one it has been making: no linear *wave* equivalent that stays oscillatory.

## What Is Established and What Is Interpretation

**Established.** That the Newtonian stress is linear in the strain rate and has three parts of different status. That $\sigma_{\mathrm{vsc},ij}\partial_jv_i=2F_{\mathrm{rlh}}$ and $\mathrm{d}E/\mathrm{d}t'=-2\int F_{\mathrm{rlh}}$, both by expansion, and that the entropy production equals $2F_{\mathrm{rlh}}/T$. That the Hopf–Cole transformation carries Burgers' equation into the heat equation exactly, in one dimension always and in three dimensions for potential flow. That the heat equation's dispersion relation is imaginary while a wave equation's is real.

**Interpretation.** That the absence of an action is *the* obstruction, rather than a symptom of one. The parity argument is exact; that parity is the property an oscillatory reading requires is the programme's reading of what a phase is. That the heat equation should count as "not a wave equation" is a definition, and this article takes the oscillatory spectrum and the cone-supported kernel as the two marks that make it.

**Not claimed.** It is not claimed that no variational principle exists for a viscous fluid. Several do, and §*Why There Is No Action* names the price they pay. It is not claimed that the Hopf–Cole transformation is available for a general three-dimensional flow; it is available for potential flow and it is not available for a rotational one. It is not claimed that viscosity is the only source of dissipation in a fluid; heat conduction produces entropy too, and the article's entropy balance assumes it away.

## Summary

The Newtonian stress is $-p_{\mathrm{th}}\delta_{ij}+2\eta_{\mathrm{shr}}S_{ij}+\zeta_{\mathrm{blk}}\delta_{ij}\nabla\cdot\vec v$, and the Navier–Stokes equation is its divergence.

Its work rate is twice the Rayleigh dissipation function, $\sigma_{\mathrm{vsc},ij}\partial_jv_i=2F_{\mathrm{rlh}}$ with $F_{\mathrm{rlh}}=\eta_{\mathrm{shr}}S_{ij}S_{ij}+\frac12\zeta_{\mathrm{blk}}(\nabla\cdot\vec v)^{2}$. The energy of an isolated flow falls at $2F_{\mathrm{rlh}}$, and the entropy rises at the same rate over the temperature.

The obstruction is the absence of an action. The viscous term is odd under reversal of time and has a fixed sign, so no functional of the flow alone varies to it. Rayleigh's device inserts the force on the right-hand side of Lagrange's equation, which is the statement that it is inserted and not derived. Doubling the variables restores a variational principle for a larger system, and the phase then belongs to the larger system.

The count does not see viscosity. A viscous fluid carries the same four data as an inviscid one, and what viscosity removes is the phase rather than a datum.

In one dimension the obstruction is removable and the result is linear: the Hopf–Cole transformation carries Burgers' equation into the heat equation, exactly, with the kernel giving $u=x/t'$. In three dimensions it does so only for potential flow.

The heat equation is not a wave equation. Its frequency is $-i\nu_{\mathrm{kin}}k^{2}$, purely imaginary; its kernel is positive rather than cone-supported; and it is the long-wavelength branch of a damped wave equation, $\nu_{\mathrm{kin}}=\tau_{\mathrm{dmp}}c^{2}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma_{ij}$ | Stress tensor |
| $\sigma_{\mathrm{vsc},ij}$ | Its viscous part |
| $S_{ij}=\frac12(\partial_iv_j+\partial_jv_i)$ | Strain rate |
| $\eta_{\mathrm{shr}}$ | Shear viscosity |
| $\tau_{\mathrm{dmp}}$ | Relaxation time of the damping term in the damped wave equation |
| $\zeta_{\mathrm{blk}}$ | Bulk viscosity |
| $\nu_{\mathrm{kin}}=\eta_{\mathrm{shr}}/\rho_{\mathrm{mass}}$ | Kinematic viscosity |
| $F_{\mathrm{rlh}}$ | Rayleigh dissipation function |
| $p_{\mathrm{th}}$ | Thermodynamic pressure |
| $s_{\mathrm{spc}},\ s_{\mathrm{ent}}$ | Specific entropy and entropy density |
| $T$ | Temperature |
| $u$ | Velocity of the one-dimensional flow |
| $\psi$ | Hopf–Cole potential |
| $E$ | Kinetic energy of the flow |
| $\rho_{\mathrm{mass}}$ | Mass density |

## Further Reading

- Lord Rayleigh, *The Theory of Sound*, 2nd ed. (Macmillan, 1894), vol. I, ch. IV, for the dissipation function and for the statement that it is half the rate at which the energy falls.
- Claude-Louis Navier, "Mémoire sur les lois du mouvement des fluides," *Mémoires de l'Académie Royale des Sciences* **6** (1822) 389–440, and George Gabriel Stokes, "On the theories of the internal friction of fluids in motion," *Transactions of the Cambridge Philosophical Society* **8** (1845) 287–305, for the stress of this article.
- Johannes M. Burgers, "A mathematical model illustrating the theory of turbulence," *Advances in Applied Mechanics* **1** (1948) 171–199, for the equation that carries his name.
- Eberhard Hopf, "The partial differential equation $u_t+uu_x=\mu u_{xx}$," *Communications on Pure and Applied Mathematics* **3** (1950) 201–230, and Julian D. Cole, "On a quasi-linear parabolic equation occurring in aerodynamics," *Quarterly of Applied Mathematics* **9** (1951) 225–236, for the transformation that linearises it.
- Carl Eckart, "The thermodynamics of irreversible processes III: relativistic theory of the simple fluid," *Physical Review* **58** (1940) 919–924, for the entropy production of a viscous fluid.
- Lev D. Landau and Evgeny M. Lifshitz, *Fluid Mechanics*, 2nd ed. (Pergamon, 1987), §§16, 49, for the dissipation function and the entropy balance.
- The companion articles: [The Euler and Continuity Equations in Biquaternionic Form](the-euler-and-continuity-equations-in-biquaternionic-form.html), [The Vorticity Form and the Irrotational Condition](the-vorticity-form-and-the-irrotational-condition.html), [The Equation of State and the Barotropic Condition](the-equation-of-state-and-the-barotropic-condition.html), [The One-Dimensional Reverse Map: Characteristics, KdV, Hopf](the-one-dimensional-reverse-map-characteristics-kdv-hopf.html).
- [Lagrangian and Hamiltonian Mechanics in Biquaternionic Form](lagrangian-and-hamiltonian-mechanics-in-biquaternionic-form.html), for Rayleigh's device; [Interpretation of the Wick Rotation in the Biquaternion Universe](interpretation-of-the-wick-rotation-in-the-biquaternion-universe.html), for the continuation that turns the wave equation into the heat equation.
