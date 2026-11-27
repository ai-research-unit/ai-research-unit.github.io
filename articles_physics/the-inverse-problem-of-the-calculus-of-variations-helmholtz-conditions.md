# __The Inverse Problem of the Calculus of Variations: Helmholtz's Conditions__

## Introduction

**The claim.** Not every equation is some action's Euler–Lagrange equation, and the test that decides is a finite list of algebraic and differential identities on the equation itself. They are Helmholtz's conditions, and in this corpus they do two jobs. They make the phrase *the viscous term has no action* a theorem rather than a remark, and they grade [the criterion](criterion-for-a-fluid-equation-one-polar-coordinates-euler-lagrange-equation.html), which asks of one polar coordinate the question Helmholtz asks of a whole system.

**What is established.** Four things. First, the test is self-adjointness of the equation's linearisation, and for a second-order equation it is three conditions that can be checked by differentiation. Second, the linear damped oscillator fails the second condition exactly when its damping is nonzero, so the failure is arithmetic and not a matter of taste. Third, a multiplier repairs the failure only when the damping is algebraic in the velocity and carries no spatial derivative; the Caldirola–Kanai Lagrangian is written out, and the reason the corpus does not use it is stated. Fourth, the corpus's criterion is Helmholtz's test with the multiplier fixed at one and the equation fixed at one coordinate — stricter than Helmholtz, and the difference is exactly where the criterion earns its keep.

**What the corpus adds.** Nothing to the theorem, which is Helmholtz's of 1887 and is standard. What it adds is the ordering and the application: the theorem is stated *before* the criterion that uses it, the criterion is graded against it in one table, and the corpus's repeated sentence about the viscous term is replaced by the condition that actually fails. The three places that said the sentence were right about the conclusion and silent about the reason.

**Why it comes here.** The section this article sits in builds actions and varies them. This is the reverse direction — from an equation back to an action — and it is the only article in the block that runs that way. A reader who has the forward map and not the inverse will accept *this equation is not variational* as an assertion about the corpus's preferences; with the inverse map in hand it is a computation.

## The Problem

**Stated once.** Given a system of equations

$$
E_a\bigl(\xi,\partial_\imath\xi,\partial_\imath\partial_\jmath\xi\bigr)=0,\qquad a=1,\dots,N,
$$

decide whether there is a density $\mathcal L$ with

$$
E_a=\frac{\delta S}{\delta\xi_a},\qquad S=\int d^4r\;\mathcal L ,
$$

where $\delta/\delta\xi_a$ is the variational derivative. **The question is not whether a solution can be found** — every equation has solutions — **but whether the equation is the stationarity condition of a functional.**

**Why it is a question with a definite answer.** The variational derivative is not an arbitrary operation. Its linearisation is self-adjoint by construction, because it is the second variation of a number and mixed partials commute. **So an equation that is a variational derivative inherits a symmetry of its own linearisation**, and that symmetry is testable without knowing $\mathcal L$. This is the whole content of the theorem: the symmetry is necessary, and Helmholtz proved it sufficient.

**Why a reader of this corpus meets it early.** Every rung of the ladder is obtained by varying an action, so the forward direction is used everywhere and never questioned. The reverse direction is used in exactly one claim, and the claim is quoted in three sectors: *the viscous term has no action*. **That claim is the theorem's contrapositive**, and until the theorem is stated the claim is a report of what the corpus has failed to find.

## The Test

**The linearisation, and the pairing it must respect.** Let $u_a$ be a variation and let $DE$ be the linearisation of $E$ at a configuration,

$$
(DE\,u)_a=\sum_b\Bigl(\frac{\partial E_a}{\partial\xi_b}u_b+\frac{\partial E_a}{\partial(\partial_\imath\xi_b)}\partial_\imath u_b+\frac{\partial E_a}{\partial(\partial_\imath\partial_\jmath\xi_b)}\partial_\imath\partial_\jmath u_b\Bigr),
$$

and pair two variations by $\langle u,v\rangle=\int d^4r\,\sum_a u_a v_a$. **The test is**

$$
\boxed{\;E\text{ is variational at unit multiplier}\iff DE=(DE)^{\dagger}\;}
$$

with the adjoint taken in that pairing: $\langle u,DE\,v\rangle=\langle(DE)^\dagger u,v\rangle$ for all $u,v$ of compact support. The adjoint moves every derivative by integration by parts and changes its sign once per derivative, which is why the conditions below are differential identities and not algebraic ones.

**Why self-adjointness is the right statement.** If $E=\delta S/\delta\xi$ then $DE$ is the Hessian of $S$ at the configuration, and a Hessian is symmetric: $\langle u,DE\,v\rangle$ is the mixed second variation $\delta^2S/\delta\xi_a\delta\xi_b\,u_av_b$, and exchanging $u$ and $v$ exchanges the order of two derivatives of one number. **The converse is Helmholtz's theorem**, and it is the direction that is not obvious: a self-adjoint linearisation can be integrated, first along a path in field space to give $S$, and the integrability of that path integral is exactly the self-adjointness.

**A remark on locality.** The theorem holds for local equations, and it produces a local density when the equation is local and the multiplier is a function of the fields. A nonlocal equation may be variational with a nonlocal action, and the test still applies with the pairing over the nonlocal space; the corpus uses only the local case, and the word *action* in the corpus's sentences means a local density.

## The Three Conditions for a Second-Order System

**Written out, because they are checkable and the corpus checks one of them.** For a system second order in the derivatives, define the **mass matrix** and two derived matrices,

$$
\Lambda_{ab}:=\frac{\partial E_a}{\partial(\partial_\imath\partial_\jmath\xi_b)}\quad(\text{symmetrised in }\imath,\jmath),\qquad
A_{ab}:=\frac{\partial E_a}{\partial(\partial_\imath\xi_b)},\qquad
B_{ab}:=\frac{\partial E_a}{\partial\xi_b}.
$$

Then $E$ is variational at unit multiplier exactly when, for every $a,b$ and every direction $\imath$,

1. **symmetry of the mass matrix**, $\Lambda_{ab}=\Lambda_{ba}$;
2. **the damping condition**, $A_{ab}+A_{ba}=2\,\partial_\imath\Lambda_{ab}$;
3. **the curl condition**, $B_{ab}-B_{ba}=\tfrac12\,\partial_\imath\bigl(A_{ab}-A_{ba}\bigr)$.

**Each condition has a one-line reading.** The first says the second variation has a symmetric coefficient of the highest derivative, which is what a Hessian has. The second says the part of the equation that is first order in the velocity is the total derivative of the mass matrix — a term that can be removed by a total derivative in the density and cannot survive as a genuine damping. The third says the part that is algebraic in the field is a gradient, up to the antisymmetric piece that the first-order part is allowed to carry.

**What the conditions are not.** They are not equations of motion and they constrain no solution. They constrain the *form* of the equation, and a single counterexample to any of them settles the question for that equation with no search over candidate Lagrangians. That is the practical value: **the test is finite, and it is a differentiation.**

**In the field case the derivative is a divergence.** Replace $d/dt$ by $\partial_\imath$ and sum over the four directions; the conditions are unchanged in form, and the total derivative in condition 2 becomes a four-divergence. Nothing in the theorem depends on there being one independent variable. **A field equation and a mechanical equation are graded by the same list**, which is why the corpus can apply the theorem to a fluid equation and to an oscillator with the same sentence.

## The Failure the Corpus Quotes: Damping

**The damped oscillator, and the condition that fails.** Take

$$
E:=m\ddot\xi+\gamma\dot\xi+k\xi=0,\qquad m,k>0,\ \gamma\ge0 .
$$

The mass matrix is $\Lambda=m$, symmetric, so condition 1 holds. The damping matrix is $A=\gamma$, so condition 2 reads

$$
\gamma+\gamma=2\frac{d}{dt}m=0 ,
$$

which fails for every $\gamma\ne0$. **The failure is one line, it is exact, and it is the whole of *the viscous term has no action* at the mechanical rung.** The term that makes the equation dissipative is precisely the term the condition excludes.

**Why the condition excludes it, in words.** A first-order term in the equation comes from a first-order term in the density, and a first-order term in a density is a total derivative unless it is contracted with something that breaks the integration by parts. In one variable there is nothing to contract with, so the term integrates away; **a damping that survives the integration by parts is therefore not the variation of anything.**

**The escape, written out honestly.** Multiply the equation by a nowhere-zero function $\mu(t)$ and ask whether $\mu E$ is variational. Condition 2 now reads $2\mu\gamma=2\dot\mu m$, so $\dot\mu=(\gamma/m)\mu$ and $\mu=e^{\gamma t/m}$. The Lagrangian is the Caldirola–Kanai one,

$$
\mathcal L=\tfrac12 e^{\gamma t/m}\bigl(m\dot\xi^2-k\xi^2\bigr),
$$

whose Euler–Lagrange equation is $e^{\gamma t/m}(m\ddot\xi+\gamma\dot\xi+k\xi)=0$, which is the damped equation. **So a multiplier exists, and the multiplier is a function of the time alone.**

**Why the corpus does not take the escape.** Three reasons, and only the third is decisive. The Lagrangian is explicitly time-dependent, so the energy it defines is not conserved and the Hamiltonian is not the physical energy. The multiplier depends on the absolute time and not on the state, so the action is not a functional of a history in the way the corpus's actions are. And **the escape does not survive the field case**: when the damping is a spatial operator rather than a number, the multiplier that condition 2 demands is

$$
\hat\mu=\exp\Bigl(\frac{1}{m}\int^{t}\hat\gamma\,dt'\Bigr)
$$

with $\hat\gamma$ an operator on the spatial dependence, which is not a function of the event and is not local. **A multiplier that is nonlocal in space repairs the equation only by an action that is nonlocal in space**, and the corpus's actions are densities.

**This is the distinction the corpus needs and did not have.** A damping that is algebraic in the velocity — Rayleigh's $\mathcal R=\tfrac12\gamma\dot\xi^2$, whose force is $\partial\mathcal R/\partial\dot\xi$ — can be absorbed by a time-only multiplier. A damping that is a spatial operator — the $\nu\nabla^2\vec v$ of viscosity — cannot be absorbed by any local multiplier, because the operator it must invert is the Laplacian. **Rayleigh's function and viscosity are two different objects, and the theorem is what separates them.** [Viscosity and the Rayleigh Dissipation Function](viscosity-and-the-rayleigh-dissipation-function.html) writes the function; this article says why it cannot be a density.

## The Multiplier, and What the Criterion Adds

**Helmholtz allows a multiplier and the corpus's criterion does not.** The general statement is: $E$ is variational *up to a multiplier* when there is an invertible matrix $M_{ab}$ of functions on the jet with

$$
M_{ab}E_b=\frac{\delta S}{\delta\xi_a}.
$$

**The multiplier is an integrating factor, and it is where the two statements part.** The criterion of the fluid block asks a strictly narrower question:

> Is this equation the Euler–Lagrange equation of *this* coordinate, at multiplier one?

**Three grades, and the corpus uses all three.**

| grade | what holds | what it means in the corpus |
| --- | --- | --- |
| unit multiplier, named coordinate | $E_a=\delta S/\delta\xi_a$ for the coordinate in question | the criterion passes: the equation is that coordinate's momentum balance |
| nonzero multiplier | $M_{ab}E_b=\delta S/\delta\xi_a$ with $M\ne1$ | Helmholtz passes, the criterion fails: variational, but not as that coordinate's momentum, so it carries no conjugate charge |
| no multiplier | no $M$ and no $S$ | neither passes: the equation is not a stationarity condition at all |

**The middle grade is the interesting one and the corpus meets it twice.** The Caldirola–Kanai oscillator is the mechanical case: the damped equation is variational, and its multiplier is not the identity, so the equation is nobody's momentum balance. The **combination** of the criterion article is the field case: the real part of the field equation multiplied by the conjugate is a genuine equation and is not one coordinate's variation, which is why the criterion calls it a consequence of two coordinate equations rather than a fluid equation. **Helmholtz tells you that such an object may still be variational; the criterion tells you that being variational is not enough.**

**Why the narrower question is the right one for a fluid.** A fluid equation is a statement about a current: continuity is the divergence of a momentum. A multiplier destroys that reading, because it multiplies the current by a matrix that is not the identity, so the object whose divergence vanishes is no longer the momentum of the named coordinate. **At multiplier one the equation's own left side is the divergence; at any other multiplier it is a linear combination of divergences**, and the charge a shift symmetry would give it is a combination too.

## What the Theorem Grades, and What It Does Not

**It grades the criterion, and it does so in one direction.** The criterion implies Helmholtz at unit multiplier: an equation that is one coordinate's Euler–Lagrange equation has a self-adjoint linearisation. **The converse fails**, and the failing case is the middle grade of the table above. So the criterion is strictly stronger, and every failure of Helmholtz is a failure of the criterion while not every failure of the criterion is a failure of Helmholtz.

**It makes one of the corpus's sentences exact, and the sentence was already right.** *The viscous term has no action* becomes: the viscous term's equation fails Helmholtz's condition 2 at every multiplier that is a local function of the event. The three places that state the sentence can now cite the condition instead of the conclusion.

**It does not decide four things.**

- *The sign and the normalisation.* A variational equation has infinitely many actions, differing by a constant, a total derivative and a positive factor. The theorem produces one and fixes none.
- *Stability.* A variational equation may have an energy unbounded below; that is a separate test, and [Ostrogradsky's](ostrogradsky-or-why-no-rung-goes-past-two-derivatives.html) is its statement.
- *A single history.* Dissipation has no action on one history; it has an action on two branches, which [the closed-time-path article](the-closed-time-path-action-one-action-on-two-branches.html) writes. **The two statements are not in conflict**: the doubled action's variation gives the dissipative equation together with its noise, and the price is a field doubled and a history given up.
- *Uniqueness of the multiplier.* When a multiplier exists it is not unique, because any constant multiple of an admissible multiplier is admissible. **The multiplier is a gauge choice of the inverse problem**, and the corpus's criterion fixes the gauge by fixing the multiplier at one.

**A last caution, and it is the one a reader is most likely to need.** Helmholtz's conditions are *local* integrability conditions, and a system can satisfy them locally and fail to have a global action — the same distinction as a closed form that is not exact. **The corpus's actions are global by construction**, written down and integrated, so the local theorem is enough for every use here; a reader who applies the theorem to a patched object, such as a connection on a nontrivial bundle, must state which patch.

## Summary

An equation is some action's Euler–Lagrange equation exactly when its linearisation is self-adjoint in the pairing of the fields, and for a second-order system that is three conditions on the coefficients: the mass matrix is symmetric, the first-order part is the total derivative of the mass matrix, and the algebraic part is a gradient up to the antisymmetric piece the first-order part may carry. **The test is finite, local and checkable by differentiation.**

The damped oscillator fails the second condition for every nonzero damping, which is the exact content of *the viscous term has no action*. A multiplier $e^{\gamma t/m}$ repairs the algebraic damping and produces the Caldirola–Kanai Lagrangian at the price of an explicit time dependence and a non-conserved energy; a damping that is a spatial operator, such as $\nu\nabla^2\vec v$, demands a multiplier that is an operator on space and therefore a nonlocal action. **Rayleigh's function and viscosity are separated by exactly this difference.**

The corpus's criterion is Helmholtz's test at multiplier one and at one named coordinate. Three grades follow — unit multiplier, nonzero multiplier, no multiplier — and the middle grade, variational but not as that coordinate's momentum, is the one the criterion exists to exclude. **The criterion is strictly stronger than the theorem, and the theorem is what makes the criterion's failures meaningful.**

The theorem fixes no sign, no normalisation, no stability and no single-history reading of dissipation. It fixes which equations can be varied, and that is the question the corpus's criterion asks.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $E_a=0$ | The system of equations, second order in the derivatives, indexed by $a=1,\dots,N$ |
| $\xi_a$ | The field or coordinate the system is written in |
| $S=\int d^4r\,\mathcal L$ | The action, when it exists |
| $\delta S/\delta\xi_a$ | The variational derivative; the equation is variational when $E_a$ equals it |
| $DE$ | The linearisation of $E$ at a configuration, the Fréchet derivative |
| $(DE)^\dagger$ | Its adjoint in the pairing $\langle u,v\rangle=\int d^4r\,\sum_a u_av_a$ |
| $\Lambda_{ab}$ | The mass matrix, $\partial E_a/\partial(\partial_\imath\partial_\jmath\xi_b)$ symmetrised |
| $A_{ab}$ | $\partial E_a/\partial(\partial_\imath\xi_b)$, the first-order coefficient |
| $B_{ab}$ | $\partial E_a/\partial\xi_b$, the algebraic coefficient |
| $M_{ab}$ | The multiplier, an invertible matrix of functions on the jet; the identity at unit multiplier |
| $\mu(t)=e^{\gamma t/m}$ | The Caldirola–Kanai multiplier of the damped oscillator |
| $\mathcal R=\tfrac12\gamma\dot\xi^2$ | Rayleigh's dissipation function; its force is $\partial\mathcal R/\partial\dot\xi$ |
| $\hat\gamma$, $\hat\mu$ | A damping that is a spatial operator and the nonlocal multiplier it would demand |

## Further Reading

- Hermann von Helmholtz, "Über die physikalische Bedeutung des Prinzips der kleinsten Wirkung," *Journal für die reine und angewandte Mathematik* 100 (1887), 137–166, the original statement of the conditions.
- Peter J. Olver, *Applications of Lie Groups to Differential Equations* (2nd ed., Springer, 1993), Chapter 5, for the variational bicomplex, the self-adjointness test and the global obstruction stated as a cohomology.
- Ian M. Anderson, *The Variational Bicomplex* (technical report, Utah State University, 1989), for the field-theoretic form of the conditions and the multiplier.
- Ruggero Maria Santilli, *Foundations of Theoretical Mechanics I: The Inverse Problem in Newtonian Mechanics* (Springer, 1978), for the multiplier as an integrating factor and the classification of admissible dampings.
- P. Caldirola, "Forze non conservative nella meccanica quantistica," *Il Nuovo Cimento* 18 (1941), 393–400, and E. Kanai, "On the quantization of the dissipative systems," *Progress of Theoretical Physics* 3 (1948), 440–442, for the time-dependent Lagrangian of the damped oscillator.
- Herbert Goldstein, Charles P. Poole and John L. Safko, *Classical Mechanics* (3rd ed., Addison-Wesley, 2002), for Rayleigh's dissipation function and its place beside the Lagrangian.
- [Criterion for a Fluid Equation](criterion-for-a-fluid-equation-one-polar-coordinates-euler-lagrange-equation.html), the criterion this theorem grades.
- [Viscosity and the Rayleigh Dissipation Function](viscosity-and-the-rayleigh-dissipation-function.html), the dissipation function the theorem separates from a density.
- [The Closed-Time-Path Action: One Action on Two Branches](the-closed-time-path-action-one-action-on-two-branches.html), where a dissipative equation acquires an action by being doubled.
- [Ostrogradsky, or Why No Rung Goes Past Two Derivatives](ostrogradsky-or-why-no-rung-goes-past-two-derivatives.html), the stability test that the existence of an action does not supply.
