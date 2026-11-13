# __The Non-Quantum Limit of the Free Schrödinger Equation__

## Introduction

**The limit, in one sentence.** Write a solution as an amplitude times a phase, and let the wavelength of the phase shrink against the length over which the amplitude varies; the phase then obeys the Hamilton–Jacobi equation and the amplitude obeys a transport equation, and no other equation survives.

**The two objects the article keeps apart.** The *limit* is the formal passage, and it produces two equations and no error. The *approximation* is that passage stopped at a stated order, and it produces a remainder and a region. *The Non-Quantum Limit of the Biquaternion Model* defines the two and fixes the criterion; this article carries them out for the free Schrödinger equation.

**The parameter is one inverse length.** Throughout, $\epsilon=1/(k_{\Phi}L)$ with $k_{\Phi}=\lvert\vec p\rvert/\hbar$ and $L$ the length over which the amplitude varies. The quantum potential over the kinetic energy is $\epsilon^{2}$, so the limit is the statement that this ratio goes to zero and the approximation is the statement that it stays below a stated size on a stated region.

**What the article establishes, in four sentences.** The decomposition is exact. The pair it produces is exact. Dropping the quantum potential gives the eikonal, whose characters are the classical trajectories. The transport equation gives the amplitude, in one dimension as $C/\sqrt{\lvert p\rvert}$ and in three as the van Vleck determinant.

**What is not new.** The amplitude–phase decomposition, the two real equations, the Hamilton–Jacobi equation, the method of characteristics, the optical–mechanical analogy, the transport equation, the WKB amplitude, the van Vleck determinant and the quantum potential are standard. Added here: the ordering of the three terms against one parameter, the biquaternion-norm reading of the eikonal, the sector location of every object the limit keeps, and the statement of where the approximation stops holding.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and $\vec e_\mu^{2}=-e_t$; $i$ is central; $\mathbb{B}_{C}$ is the centre, $\mathbb{B}_{H}$ the real-quaternion subspace, $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ the Hermitian and anti-Hermitian sectors; the state module is $\mathbb{B}\tilde\Pi\cong\mathbb{C}^{2}$. Time is $t'$ and $r'_t=c\,t'$ is the material length. The Hamiltonian is $\tilde H_\Psi=(-\frac{\hbar^{2}}{2m}\Delta_\Phi+V)e_t$, central. The mass wave number is $k_m=mc/\hbar$.

## The State and the Criterion

**The word.** A solution of the free equation is written

$$
\tilde\Xi=A\exp\!\left(i\theta_{\mathrm{act}}\right)\xi,
\qquad
\theta_{\mathrm{act}}=\frac{S}{\hbar}\in\mathbb{R},
\qquad
A>0,
\qquad
S\in\mathbb{R},
\qquad
\xi\ \text{constant},
$$

with a real positive amplitude and a real action. The exponential is central, so it commutes with $\xi$ and with everything else; the amplitude is real and therefore central too. Under the isomorphism $\mathsf M_2$ the state is a scalar phase multiplying both components equally, and $\xi$ is a spectator.

**The decomposition is exact, and that is the first point.** Every solution of the free equation with no nodal surface can be written this way, and the two equations below are then equivalent to the equation itself. Nothing is dropped in the writing.

**The criterion is the ratio of two gradients.** The momentum acting on the word separates into a real part and an imaginary part,

$$
\tilde p\,\tilde\Xi=\Big[\vec\nabla_\Phi S-i\,\hbar\,\vec\nabla_\Phi\ln A\Big]\tilde\Xi ,
$$

and the two terms have different sizes. Against the leading term,

$$
\frac{\lvert\hbar\vec\nabla_\Phi\ln A\rvert}{\lvert\vec\nabla_\Phi S\rvert}\sim\epsilon ,
\qquad
\frac{1}{k_{\Phi}^{2}}\left\lvert\frac{\Delta_\Phi A}{A}\right\rvert\sim\epsilon^{2} .
$$

**The second ratio is the one the limit uses.** It is the quantum potential over the kinetic energy, and it is a square where the first is linear. The limit keeps the leading term of the momentum, the first correction keeps the amplitude gradient, and the exact rewriting keeps all three.

| object | order in $\epsilon$ | kept by the limit | kept by the first correction |
|---|---|---|---|
| $\vec\nabla_\Phi S$ | $1$ | yes | yes |
| $\hbar\,\vec\nabla_\Phi\ln A$ | $\epsilon$ | no | yes |
| $\hbar^{2}\,\Delta_\Phi A/A$ | $\epsilon^{2}$ | no | no |

**One warning about the word "order".** The continuity equation below survives the limit untouched and is not an expansion; a reader who truncates both equations at order zero deletes the density and keeps the phase. The limit truncates one equation and leaves the other exact, and that asymmetry is the whole content of the pair.

## The Two Real Equations

**Apply the Hamiltonian and collect.** From $\tilde H_\Psi\tilde\Xi=E\tilde\Xi$,

$$
\left[\frac{\lvert\vec\nabla_\Phi S\rvert^{2}}{2m}+V-E\right]A
-\frac{i\,\hbar}{2m}\Big(2\,\vec\nabla_\Phi A\cdot\vec\nabla_\Phi S+A\,\Delta_\Phi S\Big)
-\frac{\hbar^{2}}{2m}\Delta_\Phi A=0 .
$$

The first bracket is real, the middle term is purely imaginary, the last term is real. The separation is forced, because the centre of the algebra is $\mathbb{C}$ and the three pieces lie in different parts of it.

**The imaginary part is the transport equation.**

$$
\vec\nabla_\Phi\cdot\left(A^{2}\,\vec\nabla_\Phi S\right)=0 .
$$

**The real part is the quantum Hamilton–Jacobi equation.**

$$
\frac{\lvert\vec\nabla_\Phi S\rvert^{2}}{2m}+V+Q=E ,
\qquad
Q=-\frac{\hbar^{2}}{2m}\,\frac{\Delta_\Phi A}{A} .
$$

**Both are exact and both are central.** $A$ is central and real, $S$ is central and real, so every object in the pair lies in $\mathbb{B}_{C}$. The non-central structure of the algebra does not enter at any order, for a spin-zero free particle.

**The sector statement is worth one line.** The phase is a central $*$-unitary element, the amplitude is a central real one, and the phase gradient is a real quaternion in $\mathbb{B}_{H}$, the algebra's copy of space. The limit therefore takes a state spread over the full algebra to a state in the centre times a real vector, and that contraction of support is what it means to become a ray.

## The Eikonal

**Drop the third term.** What remains of the real equation is

$$
\frac{\lvert\vec\nabla_\Phi S\rvert^{2}}{2m}+V=E ,
$$

the Hamilton–Jacobi equation for a particle of energy $E$ in the potential $V$.

**In the algebra it is a norm.** The phase gradient is the real quaternion $\vec\nabla_\Phi S=\sum_\mu(\partial S/\partial R_\mu)\vec e_\mu$, and

$$
\langle\vec\nabla_\Phi S\rangle_{\natural}=\lvert\vec\nabla_\Phi S\rvert^{2},
$$

because $\vec\nabla_\Phi S\,\vec\nabla_\Phi S^{\natural}=\lvert\vec\nabla_\Phi S\rvert^{2}e_t$. The eikonal is then the statement in the centre

$$
\boxed{\ \frac{1}{2m}\langle\vec\nabla_\Phi S\rangle_{\natural}=E-V\ }
$$

that **the kinetic energy is the biquaternion norm of the phase gradient**.

**Two consequences follow at once.** The right side is positive where $E>V$, and the norm of a real vector is positive, so the equation is solvable in the allowed region. Where $E<V$ the right side is negative, no real phase gradient solves it, and the momentum turns imaginary; that is the algebraic statement of the forbidden region, and it needs no separate discussion of exponential behaviour. The vanishing norm would be a zero divisor, and the phase gradient never reaches one, because its norm is fixed by the energy defect and vanishes only where the particle stops.

**The characters are the trajectories.** Writing $\vec p=\vec\nabla_\Phi S$, the characteristic system is

$$
\frac{d\vec r}{dt'}=\frac{\vec p}{m},
\qquad
\frac{d\vec p}{dt'}=-\vec\nabla_\Phi V ,
$$

against the clock $t'$. The wave fronts $S=\text{const}$ are the surfaces of constant phase, the rays are the trajectories, and the phase gradient is the ray direction at each point.

**The free case is the plane wave.** For the free particle the complete integral is

$$
S=\vec p\cdot\vec r-E\,t',
\qquad
E=\frac{\lvert\vec p\rvert^{2}}{2m},
$$

whose gradient is the constant $\vec p$ and whose phase is $\mathrm{Sc}(\tilde K_\Phi\tilde R_\Phi^{\natural})$ with $\tilde K_\Phi=\tilde P_\Phi/\hbar$. The limit has then changed nothing, because a plane wave is semiclassical exactly: its amplitude is constant and its ratio $\epsilon$ vanishes. **The limit acts only where the amplitude varies**, and a plane wave is the case in which it has nothing to do.

**The separable case.** For $V=\sum_\eta V_\eta(x_\eta)$ the equation separates, $S=\sum_\eta S_\eta$, each term obeying $\frac{1}{2m}(dS_\eta/dx_\eta)^{2}+V_\eta=E_\eta$ with $\sum_\eta E_\eta=E$, so that

$$
S_\eta(x_\eta)=\pm\int^{x_\eta}\sqrt{2m\left(E_\eta-V_\eta(\zeta)\right)}\;d\zeta .
$$

The two signs are the two directions of motion, and the turning points $E_\eta=V_\eta$ are where the branches meet and the amplitude below diverges.

## The Transport and the Amplitude

**The transport equation is a conservation law.** Since $\vec\nabla_\Phi S=m\vec v$ is the classical momentum, the equation $\vec\nabla_\Phi\cdot(A^{2}\vec\nabla_\Phi S)=0$ says that the current $\vec J=A^{2}\vec\nabla_\Phi S/m$ is divergence-free. It is the stationary continuity equation, and it is exact: the limit did not produce it and cannot spoil it.

**In one dimension it integrates.** $A^{2}\,dS/dx=\text{const}$, so

$$
A(x)=\frac{C}{\sqrt{\lvert p(x)\rvert}},
\qquad
p(x)=\sqrt{2m\left(E-V(x)\right)} .
$$

The wave is large where the particle moves slowly, and small where it moves fast. That is the whole of the WKB amplitude, and it follows from the exact equation and not from an expansion.

**In three dimensions it gives the van Vleck determinant.**

$$
\boxed{\ A\ \propto\ \left\lvert\det\left(\frac{\partial^{2}S_{\mathrm{cl}}}{\partial x_{i}\,\partial x_{f}}\right)_{i,f=1}^{3}\right\rvert^{1/2}\ }
$$

The determinant is the Jacobian of the map from initial to final position, so $A^{2}$ is the density of the ray congruence and the amplitude measures its focusing. Where the congruence crosses itself the determinant vanishes, the amplitude diverges, and the approximation has left its region; that is a caustic, and it is the second place where the article has to say that the result stops.

**Why the amplitude may be taken real.** A complex $A$ would put the amplitude in $\mathbb{B}_{C}$ and not in $\mathbb{R}e_t$, and the separation into real and imaginary parts would have to be redone. The real positive choice is the gauge in which $A^{2}$ is a density and the transport equation is a continuity equation; it is a choice and not an assumption, and it is the same choice the corpus makes everywhere.

## The Error

**The discarded term is the quantum potential, and its size is a function of position.** With $A=\exp(-x^{2}/4\sigma^{2})$ and $\epsilon=1/(k_\Phi\sigma)$,

$$
\rho(x)=\frac{\lvert Q\rvert}{E-V}=\epsilon^{2}\left\lvert\frac{x^{2}}{4\sigma^{2}}-\frac{1}{2}\right\rvert .
$$

| $\lvert x\rvert/\sigma$ | $0$ | $1$ | $\sqrt{2}$ | $2$ | $3$ |
|---|---|---|---|---|---|
| $\rho/\epsilon^{2}$ | $0.500$ | $0.250$ | $0$ | $0.500$ | $1.750$ |

**The table is the argument.** The ratio vanishes at $\sqrt 2\,\sigma$ and grows as $x^{2}$ beyond it, so for every $\epsilon$ it reaches one at $x\simeq2\sigma/\epsilon$. No value of the parameter makes the expansion uniform: the limit is a statement about equations, and the approximation is a statement about a region of one solution.

**This is where the two words part.** The limit needs no region and has no remainder. The approximation needs both, and the table is what a claim of approximation has to carry: the order kept and the place where it stops.

**What the limit does not commute with.** Two plane waves of wave numbers $k_\Phi$ and $k_\Phi+\delta k$ are each semiclassical exactly, and their sum has envelope wave number $\delta k$ and parameter $1/(\delta k\,L)$, which is large when the two are close. So

$$
\lim\left(\tilde\Xi_1+\tilde\Xi_2\right)\neq\lim\tilde\Xi_1+\lim\tilde\Xi_2 ,
$$

and the difference is the interference term. The limit is not a map on the state space: it takes a wave to its rays, and a ray with a density is not an element of the module.

## Where the Approximation Stops

**Three failures, and each is a place and not an order.**

**At a turning point.** $p\to0$, the amplitude $C/\sqrt{\lvert p\rvert}$ diverges, and the eikonal's two branches meet. The repair is a uniform approximation on an Airy scale, which the algebra does not supply; the standard methods are used unchanged.

**At a caustic.** The van Vleck determinant vanishes and the ray congruence folds. The same repair applies, and the same statement holds: the algebra supplies the location of the failure, not its cure.

**Where the amplitude varies as fast as the phase.** There $\epsilon$ is not small anywhere and the limit has no claim to make. That is the interior of a nodal region, and the density vanishes there.

**One thing the limit never does.** It does not select a subalgebra and it does not produce a state. The centre of the algebra is a canonical classical sector, and the limit does not land there; it selects a state-dependent slice, with $L$ as the context made quantitative. That refusal is the subject of *The Non-Quantum Limit of the Biquaternion Model* and is recorded here only so that the free case is not read as a contraction of the algebra.

## What the Biquaternion Form Adds

**Standard quantum physics, transcribed.** Every formula in this article is in every textbook. The decomposition, the pair, the eikonal, the characteristics, the optical–mechanical analogy, the transport amplitude, the van Vleck determinant and the quantum potential are not new, and the ordering by $\epsilon$ is the standard semiclassical ordering.

**Three things the notation supplies.**

*The eikonal is a norm.* $\frac{1}{2m}\langle\vec\nabla_\Phi S\rangle_{\natural}=E-V$ is one line, and it ties the leading-order equation to the same quadratic form whose vanishing defines the zero-divisor cone. The forbidden region then needs no separate postulate: it is where a real vector would need a negative norm.

*The phase gradient has a home.* It is a real quaternion in $\mathbb{B}_{H}$, while the momentum operator is Hermitian in $\mathbb{B}_{\Psi}$. The correspondence between them is the semiclassical statement that the operator's value on a ray is the classical vector, and it is a statement about sectors and not about limits.

*The whole expansion is central.* Phase, amplitude, quantum potential and the transport current all lie in $\mathbb{B}_{C}$, so the semiclassical expansion of a spin-zero particle never leaves the centre. That is why the free case is the clean one, and why the spin cases need a second step.

**What it does not supply.** A uniform approximation at turning points and caustics; a branch rule for a complex action; and any prediction that distinguishes the reformulation from scalar WKB.

## Summary

The state is $\tilde\Xi=A\exp(i\theta_{\mathrm{act}})\xi$ with a central phase, a real central amplitude and a constant module element. The momentum acts as $\tilde p\tilde\Xi=[\vec\nabla_\Phi S-i\hbar\vec\nabla_\Phi\ln A]\tilde\Xi$, with the leading term a real quaternion in $\mathbb{B}_{H}$. Separating the equation gives the exact pair

$$
\vec\nabla_\Phi\cdot\left(A^{2}\vec\nabla_\Phi S\right)=0 ,
\qquad
\frac{\lvert\vec\nabla_\Phi S\rvert^{2}}{2m}+V+Q=E ,
\qquad
Q=-\frac{\hbar^{2}}{2m}\frac{\Delta_\Phi A}{A} .
$$

Dropping $Q$ gives the eikonal $\frac{1}{2m}\langle\vec\nabla_\Phi S\rangle_{\natural}=E-V$, whose characters are the classical trajectories. The transport equation is untouched by the limit and gives $A=C/\sqrt{\lvert p\rvert}$ in one dimension and the van Vleck determinant in three. The error is the quantum potential over the kinetic energy, $\epsilon^{2}\lvert x^{2}/4\sigma^{2}-\frac12\rvert$ for a Gaussian, and it reaches one at $x\simeq2\sigma/\epsilon$ for every $\epsilon$, so the approximation holds on a region and never on a solution. The limit does not commute with superposition, and the failure at turning points and caustics is a place and not an order.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{B}_{C}$, $\mathbb{B}_{H}$ | Centre; real-quaternion subspace |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ | Hermitian and anti-Hermitian sectors |
| $\tilde\Xi=A\exp(i\theta_{\mathrm{act}})\xi$ | The state in amplitude and phase; $A>0$ real, $S$ real, $\xi$ constant |
| $\theta_{\mathrm{act}}=S/\hbar$ | The angle of the action |
| $\vec\nabla_\Phi S$ | Phase gradient; real quaternion in $\mathbb{B}_{H}$ |
| $\langle\vec\nabla_\Phi S\rangle_{\natural}=\lvert\vec\nabla_\Phi S\rvert^{2}$ | Its biquaternion norm |
| $\epsilon=1/(k_{\Phi}L)$ | The parameter of the limit |
| $k_{\Phi}=\lvert\vec p\rvert/\hbar$, $k_m=mc/\hbar$ | Momentum and mass wave numbers |
| $Q=-\frac{\hbar^{2}}{2m}\Delta_\Phi A/A$ | Quantum potential; central real scalar |
| $\frac{1}{2m}\langle\vec\nabla_\Phi S\rangle_{\natural}=E-V$ | The eikonal, as a norm |
| $\vec\nabla_\Phi\cdot(A^{2}\vec\nabla_\Phi S)=0$ | Transport equation; exact |
| $A=C/\sqrt{\lvert p\rvert}$ | Amplitude in one dimension |
| $\lvert\det\partial^{2}S_{\mathrm{cl}}/\partial x_i\partial x_f\rvert^{1/2}$ | Van Vleck determinant |
| $\rho=\lvert Q\rvert/(E-V)$ | The error of the approximation |

## Further Reading

- H. Goldstein, C. P. Poole, and J. L. Safko, *Classical Mechanics* (Addison-Wesley, 2002), for the Hamilton–Jacobi equation, its characteristics and the optical–mechanical analogy.
- L. D. Landau and E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory* (Pergamon, 1977), for the semiclassical expansion and the transport equation.
- A. Messiah, *Quantum Mechanics* (North-Holland, 1961), for the amplitude–phase separation and the quantum potential.
- M. V. Berry and K. E. Mount, "Semiclassical approximations in wave mechanics," *Reports on Progress in Physics* **35** (1972) 315–397, for the uniform approximations and the failure at caustics.
- R. G. Littlejohn, "The semiclassical evolution of wave packets," *Physics Reports* **138** (1986) 193–291, for the error estimates that replace a closed-form remainder.
- D. Bohm, "A Suggested Interpretation of the Quantum Theory in Terms of 'Hidden' Variables," *Physical Review* **85** (1952) 166–193, for the quantum potential and the trajectory reading.
- J. H. Van Vleck, "The correspondence principle in the statistical interpretation of quantum mechanics," *Proceedings of the National Academy of Sciences* **14** (1928) 178–188, for the determinant that carries the amplitude.
