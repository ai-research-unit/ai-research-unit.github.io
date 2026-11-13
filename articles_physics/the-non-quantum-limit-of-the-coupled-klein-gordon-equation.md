# __The Non-Quantum Limit of the Coupled Klein–Gordon Equation__

## Introduction

**What the connection does to a second-order limit.** It shifts the four-momentum, and it does nothing else. The eikonal becomes the mass shell of the mechanical four-momentum, the transport equation carries the mechanical current, and the quantum potential is exactly what it was in the free case. The limit's classical object is again a unit timelike congruence, now with the Lorentz force as its acceleration.

**Why the connection is more visible here than in the first-order family.** In the Schrödinger family the connection is central imaginary in every slot and joins the phase bracket alone. Here the temporal slot's addition is *real* in the spelling the second-order articles use, so it joins the scale bracket, and the naive statement "the connection cannot reach the amplitude" is false. The amplitude equation is nevertheless unchanged in its quantum term, and the reason is not a type argument but a translation: the shift is absorbed into the phase's rate, and the quantum potential depends on $r$ and its ordinary d'Alembertian, which no translation of the phase touches.

**The parameter.** $\epsilon=1/(k_\Phi L)$, unchanged, with $k_\Phi=\lvert\vec p\rvert/\hbar$ and $L$ the length over which the amplitude varies. The one-particle ratio $\delta=1/(k_mL)=\epsilon\lvert\vec p\rvert/(mc)$ sits beside it and is weaker, as in the free companion. **The connection contributes no parameter and is not ordered by the limit.** A vector potential comparable with the momentum is kept at full strength, and the limit's smallness is the smallness of the amplitude's variation alone.

**What the article establishes, in five sentences.** The pair is exact. The eikonal is the mass shell of the mechanical four-momentum, so the flow is unit and the force is the Lorentz force. The transport equation is the conservation of a gauge-invariant current, which the free current was not. The quantum potential is untouched, so the error of the approximation is the free error, and the reason it is untouched is a translation of the phase rate and not a type statement. The circulation $2\pi\hbar n+ϙ\Phi_B$ is exact and contains no $\delta$.

**What is not new.** The charged Madelung pair is standard, and the Lorentz force from an eikonal is textbook. Added here: the two spellings of the connection's type and which of them is invariant, the theorem that the quantum potential is unchanged with its correct argument, the statement that the coupling is not a small parameter of the limit, and the circulation as an exact invariant of the pair rather than a result of the limit.

**Conventions.** Those of the free companion, with the connection added. The connection is $\tilde A_\Phi=i a'_t e_t+\vec A$ with $a'_t$ and $\vec A$ real; the coupling is $ϙ$, which is minus the electric charge, so the mechanical momentum is $\vec\pi=-i\hbar\nabla+ϙ\vec A$ and the potential energy enters as $-ϙ\varphi$ with $\varphi=c\,a'_t$. The word is $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$ with $\rho_{\mathrm{num}}=r^{2}$ and $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$. The d'Alembertian is $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$ with $r'_t=c\,t'$, and $k_m=mc/\hbar$.

## The Word and the Covariant Bracket

**The bracket and its addition.**

$$
\mathcal A^{\mathrm{gco}}_\mu=\tilde\Xi^{-1}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi
=\underbrace{\partial_\mu\ln r+i\,\partial_\mu\theta_{\mathrm{pha}}}_{\text{the free bracket}}+\frac{i\,ϙ}{\hbar}A_\mu .
$$

For a central field the free bracket is the sum of a real central scale rate and a central imaginary phase rate, and the connection's term is a complex central number that adds to the two of them.

**Slot by slot, and the sign that matters.** With $A_t=i a'_t$,

$$
\frac{i\,ϙ}{\hbar}A_t=-\frac{ϙ}{\hbar}\,a'_t
\qquad\text{(real)},
\qquad
\frac{i\,ϙ}{\hbar}A_\eta=\frac{i\,ϙ}{\hbar}A_\eta
\qquad\text{(imaginary)} .
$$

So in the temporal slot the addition is real and joins the **scale** rate; in the three spatial slots it is imaginary and joins the **phase** rate.

**The two spellings, and why both are right.** The first-order family differentiates against $t'$, where the same connection adds $-\frac{iϙ}{\hbar}\varphi$ and is imaginary in every slot. This family differentiates against $R_t$, and multiplication by $-i$ exchanges the real and the imaginary part, so what is imaginary there is real here. **The type of the additive term is a property of the chart and not of the physics.** The invariant statement is the one the two spellings share: the connection shifts the temporal component of the mechanical four-momentum.

**The invariant statement, written out.**

$$
\hbar c\,P^{\mathrm{mech}}_t=E+ϙ c\,a'_t ,
\qquad
\hbar\vec P^{\mathrm{mech}}=\vec p+ϙ\vec A ,
\qquad
E=-\hbar c\,\frac{\partial\theta_{\mathrm{pha}}}{\partial r'_t} ,
\quad
\vec p=\hbar\nabla\theta_{\mathrm{pha}} .
$$

**No relative sign can be chosen**, because the scalar and the vector potential are the two slots of one element and the shift is one substitution. That is the same statement the polar companion makes, and it is the article's only import.

**What the type statement cannot be used for.** It cannot be used to argue that the coupling is absent from the amplitude equation, because in the temporal slot it sits beside $\partial\ln r$ and can move it. Whether the amplitude equation actually changes is a question about the equation and not about the bracket, and §*The Pair* answers it by computation.

## The Pair

**Exact, with the mechanical momentum in both slots.**

$$
\left(\partial_{r'_t}S_{\tilde\Xi}-ϙ\,a'_t\right)^{2}-\left\lvert\nabla S_{\tilde\Xi}+ϙ\vec A\right\rvert^{2}
=m^{2}c^{2}-\hbar^{2}\frac{\Box_\Phi r}{r}
$$

$$
\nabla\cdot\left(\rho_{\mathrm{num}}\left(\nabla S_{\tilde\Xi}+ϙ\vec A\right)\right)
-\frac{\partial}{\partial r'_t}\left(\rho_{\mathrm{num}}\left(\partial_{r'_t}S_{\tilde\Xi}-ϙ\,a'_t\right)\right)=0
$$

**The first equation, on the mechanical four-momentum.**

$$
\frac{\left(E+ϙ c\,a'_t\right)^{2}}{c^{2}}-\left\lvert\vec p+ϙ\vec A\right\rvert^{2}=m^{2}c^{2}+2mQ ,
\qquad
Q=-\frac{\hbar^{2}}{2m}\,\frac{\Box_\Phi r}{r} .
$$

**Three changes from the free pair, and the list is complete.** The temporal slot carries $-{ϙ}a'_t$ beside the phase rate; the spatial slots carry $+{ϙ}\vec A$ beside the phase gradient; and the transport equation carries the mechanical current. Nothing else moves: not $r^{2}$, not the nodal set, not the exactness of the equivalence, and not $Q$.

**Why $Q$ is untouched, stated correctly.** In the temporal slot the connection does reach the scale rate, so the argument is not that the amplitude is unreachable. The argument is a computation. Writing $\kappa^{\mathrm{kin}}_t=\partial_{r'_t}\theta_{\mathrm{pha}}-ϙ a'_t/\hbar$ and applying the covariant operator twice to $r\,e^{i\theta_{\mathrm{pha}}}$,

$$
\tilde\nabla^{\mathrm{gco}}_t\tilde\nabla^{\mathrm{gco}}_t\left(r\,e^{i\theta_{\mathrm{pha}}}\right)
=e^{i\theta_{\mathrm{pha}}}\Big[\partial^{2}_{r'_t}r-r\bigl(\kappa^{\mathrm{kin}}_t\bigr)^{2}+i\bigl(2\kappa^{\mathrm{kin}}_t\,\partial_{r'_t}r+r\,\partial_{r'_t}\kappa^{\mathrm{kin}}_t\bigr)\Big],
$$

so the real part keeps $\partial^{2}_{r'_t}r$ beside the squared *shifted* rate and nothing else. The connection reaches the scale rate in the first derivative and cancels out of the second. What survives beside $r$ is the ordinary d'Alembertian of $r$, because the connection is a function with no second derivative of the field in it. **A gauge field cannot change the size of the quantum potential of a scalar state**, here as in the first-order family, and the two arguments are different arguments for one theorem.

| object | free | coupled | changed |
|---|---|---|---|
| temporal slot of the bracket | $\partial_{r'_t}\ln r$ | $\partial_{r'_t}\ln r-ϙ a'_t/\hbar$ | yes, and it is real |
| spatial slots of the bracket | $\nabla\ln r+i\nabla\theta$ | $+\frac{iϙ}{\hbar}\vec A$ | yes, and it is imaginary |
| transport current | $\rho_{\mathrm{num}}\nabla S/m$ | $\rho_{\mathrm{num}}(\nabla S+ϙ\vec A)/m$ | yes |
| quantum potential | $-\frac{\hbar^{2}}{2m}\frac{\Box_\Phi r}{r}$ | the same | **no** |
| mass shell's rest term | $m^{2}c^{2}$ | $m^{2}c^{2}$ | no |

## The Eikonal

**Drop the shift.**

$$
\left(\partial_{r'_t}S_{\tilde\Xi}-ϙ\,a'_t\right)^{2}-\left\lvert\nabla S_{\tilde\Xi}+ϙ\vec A\right\rvert^{2}=m^{2}c^{2} .
$$

**In the algebra it is a norm, and the momentum is mechanical.**

$$
\boxed{\ \left\langle\tilde P^{\mathrm{mech}}_\Phi\right\rangle_{\natural}=-m^{2}c^{2}\ }
$$

**The eikonal's content is that the mechanical four-momentum is on shell.** The phase's gradient is not on shell and need not be; the difference is the potential, and the potential is a translation in momentum space by $-ϙ\tilde A_\Phi$.

**The flow is unit and its acceleration is the Lorentz force.** Dividing by $m^{2}$ gives $\langle\tilde V^{\mathrm{mech}}\rangle_{\natural}=-c^{2}$ exactly, so the classical object is a unit timelike congruence, as in the free case. Differentiating the eikonal and using that the curl of a gradient vanishes gives, against the clock $t'$,

$$
\frac{d\vec\pi}{dt'}=-ϙ\left(\vec E+\vec v\times\vec B\right),
\qquad
\vec v=\frac{\vec\pi}{m},
\qquad
\vec E=-\nabla a'_t-\partial_{t'}\vec A ,
$$

which is $q(\vec E+\vec v\times\vec B)$ with $q=-ϙ$. **The force law is one gradient away from the eikonal and needs no postulate**, and it is the same equation the first-order family's limit produces, because the mechanical momentum is the same object in both.

**A uniform potential moves nothing.** With $\vec A=0$ and $a'_t$ constant, the eikonal is the free eikonal with $E$ shifted by $-ϙ c a'_t$; the trajectories are identical, the phase's rate is shifted, and the density's rate is untouched. In the polar companion's flow language the constant potential translates the frequency and leaves the rapidity, the gap and the density exactly as they were.

**The vorticity is the field, exactly.** The kinetic flow is not a gradient:

$$
\nabla\times\left(\vec p+ϙ\vec A\right)=ϙ\,\vec B ,
$$

with no approximation and no quantum correction. **The free flow's irrotationality is the statement $\vec B=0$**, and it is a property of the connection and not of the scalar field.

**The circulation is exact.** Around a loop with $\vec B=0$ on a spanning surface,

$$
\oint\left(\vec p+ϙ\vec A\right)\cdot d\vec l=2\pi\hbar\,n+ϙ\,\Phi_B ,
\qquad
\Phi_B=\oint\vec A\cdot d\vec l .
$$

**This is an invariant of the pair and not a result of the limit.** It follows from the vorticity identity integrated over a surface, it holds for any state of the polar form, and no $\delta$ appears in it. A circulation is a statement about a loop and the criterion is a statement about a length, so the two cannot meet.

## The Transport

**The equation is exact and its current is gauge invariant.**

$$
\vec j_{\mathrm{mech}}=\frac{\rho_{\mathrm{num}}}{m}\left(\vec p+ϙ\vec A\right),
\qquad
\frac{\partial\rho_{\mathrm{chg}}}{\partial r'_t}+\nabla\cdot\vec j_{\mathrm{mech}}=0 ,
$$

with $c\rho_{\mathrm{chg}}=\rho_{\mathrm{num}}(E+ϙ c\,a'_t)/m$. The free current $\rho_{\mathrm{num}}\vec p/m$ was not gauge invariant; the mechanical one is, term by term, because the phase's shift and the potential's shift cancel inside one bracket.

**Its content is one sentence.** The density is carried by the mechanical velocity, and the difference between the mechanical and the canonical velocity is $ϙ\vec A/m$ — the whole of the coupling's effect on where the density goes.

**The charge, and what the potential does to its sign.**

$$
\rho_{\mathrm{chg}}=\frac{\rho_{\mathrm{num}}}{mc^{2}}\left(E+ϙ c\,a'_t\right) .
$$

The bracket is the mechanical energy, and the potential shifts the value at which it changes sign. **The potential moves the boundary between the two signs of the charge and does not remove the sign change**: the free article's defect is one defect, and the coupling relocates it rather than addressing it. The positive definiteness of $\rho_{\mathrm{num}}$ is a statement about the number density and not about the charge.

## The Error

**The error is the free error.** $Q$ is untouched, so the momentum error is the free one,

$$
\frac{\lvert\delta p\rvert}{p}=\frac{\lvert Q\rvert}{2T_{\mathrm{kin}}}=\frac{\epsilon^{2}}{2}\left\lvert\frac{x^{2}}{4\sigma^{2}}-\frac{1}{2}\right\rvert
$$

for a planar Gaussian, exactly as in the free article, and the table there applies unchanged.

**The connection can shrink the region without appearing in the ratio.** A magnetic field focuses a bundle of dust lines, so $L$ shrinks along the bundle and both ratios grow; neither ratio carries $\vec A$ or $a'_t$. The two statements are consistent: the criterion is a property of the amplitude, and a connection acts on the amplitude through the focusing of the congruence and not through the coefficients of the equation.

**That is the sharpest structural difference between the two coupled limits.** The relativistic limit's error is a number that the algebra's entries fix. The non-quantum error is an operator that changes sign, and a connection can move its zeros only by moving the amplitude.

## The Criterion Does Not Order the Connection

**The potential is not a small quantity.** A vector potential is comparable with the momentum in any laboratory field, and the limit's parameter is $\epsilon$ and not $ϙ\lvert\vec A\rvert/\lvert\vec p\rvert$. Nothing in the derivation expands in the coupling: the mechanical momentum enters the eikonal at full strength, and the covariant transport equation is exact.

**What follows for the truncation.** The term the limit drops is $2mQ$, which is a functional of $r$ and its ordinary d'Alembertian, hence gauge invariant by itself. **The truncated pair inherits the gauge invariance of the exact pair**, and the reason is that the discarded term carries no connection. Had the limit dropped a term containing $\vec A$ or $a'_t$ without its partner, gauge invariance would be lost at the first order.

**One rule of the writing, stated here for the second-order family.** The expansion variable must be the mechanical four-momentum $\tilde P^{\mathrm{mech}}_\Phi$ and never the canonical $\tilde P_\Phi$, because the canonical momentum shifts under a gauge transformation while the mechanical one does not. A truncated equation written in $\tilde P_\Phi$ would be gauge dependent even where the exact equation is not. The first-order family's companion states the same rule for $\mathcal E$ and $\vec\pi$.

## The Two Limits and Their Order

**Two parameters.** The nonrelativistic limit is $\beta\to0$ with $S_{\tilde\Xi}=-mc\,r'_t+\sigma$; the non-quantum limit is $\epsilon\to0$. Both are needed to reach Newton, and the coupling changes neither.

**At leading order they commute.** Taking $\epsilon$ first leaves the mechanical mass shell and the mechanical transport equation; taking $\beta$ on that pair gives $T_{\mathrm{kin}}=\lvert\vec\pi\rvert^{2}/2m-ϙ\varphi$ with the mechanical current. Taking $\beta$ first leaves the coupled Schrödinger pair with $Q=-\hbar^{2}\Delta_\Phi r/(2mr)$; taking $\delta$ on that pair gives the same two equations. **The final pair is the same in both orders**, and it is the pair of *The Non-Quantum Limit of the Coupled Schrödinger Equation*.

**At the order of the discarded term they do not commute.** The two paths discard different objects in a different sequence, so halfway along the first the object is a Lorentz dust with no quantum term and halfway along the second it is a charged quantum fluid with $Q$. A claim that the equations are charged, semiclassical and nonrelativistic must name the path, because the intermediate objects differ.

**One inequality summarises the coupling's place.** The potential enters the mechanical energy and not the criterion, so a field can be deep in the semiclassical regime and dominated by its connection at the same time — which is the ordinary situation for a charged particle in a strong field, and the reason the coupled limit is worth writing separately from the free one.

## What the Biquaternion Form Adds

**Standard charged hydrodynamics, transcribed.** The pair, the mechanical four-momentum, the Lorentz force, the vorticity identity, the circulation quantum, the charge density and the quantum potential are all standard. The ordering by $\epsilon$ is the free ordering.

**Four things the notation supplies.**

*One shift, two slots, one statement.* The scalar and vector potentials are the two slots of one element $\tilde A_\Phi$, so the two classical substitutions are one substitution. The article's table of the two slots is then a statement about the algebra and not a mnemonic: the signs cannot be chosen independently because the slots belong to one object.

*The type of the connection's term is chart-dependent, and the corpus exhibits both charts.* The temporal addition is real against $R_t$ and imaginary against $t'$, and the two polar companions write the two spellings. Reading either as a statement about the physics rather than about the chart produces the false inference that the coupling cannot touch the amplitude; the equation then contradicts the inference, and the resolution is the translation of the phase rate.

*The eikonal is a norm on the mechanical momentum.* $\langle\tilde P^{\mathrm{mech}}\rangle_{\natural}=-m^{2}c^{2}$ is one line, and the potential's presence in it is a translation and not a curvature. The classical statement "a charge in a field has mechanical four-momentum on shell" and the free statement "a particle has four-momentum on shell" are then the same sentence with different letters.

*The circulation is exact and the limit adds nothing to it.* $\oint(\vec p+ϙ\vec A)\cdot d\vec l=2\pi\hbar n+ϙ\Phi_B$ has no $\delta$ in it, so it is inherited rather than derived. The limit's job there is to leave it alone, and it does.

**What it does not supply.** No branch rule for the charge, no removal of the second sheet, no uniform approximation at a turning point, and no prediction distinguishing the reformulation from the standard charged Madelung fluid.

## Summary

The word is $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$, the coupling is $ϙ$, and the mechanical four-momentum is the one whose temporal component is $E+ϙ c a'_t$ and whose spatial part is $\vec p+ϙ\vec A$. The exact pair is

$$
\left(\partial_{r'_t}S_{\tilde\Xi}-ϙ a'_t\right)^{2}-\left\lvert\nabla S_{\tilde\Xi}+ϙ\vec A\right\rvert^{2}=m^{2}c^{2}-\hbar^{2}\frac{\Box_\Phi r}{r},
\qquad
\nabla\cdot\left(\rho_{\mathrm{num}}\left(\nabla S_{\tilde\Xi}+ϙ\vec A\right)\right)-\frac{\partial}{\partial r'_t}\left(\rho_{\mathrm{num}}\left(\partial_{r'_t}S_{\tilde\Xi}-ϙ a'_t\right)\right)=0 .
$$

With the criterion $\epsilon=1/(k_\Phi L)$, dropping the shift gives the eikonal $\langle\tilde P^{\mathrm{mech}}\rangle_{\natural}=-m^{2}c^{2}$: the mechanical four-momentum is on shell, the flow is a unit timelike congruence, and its acceleration is the Lorentz force. The transport equation is exact and its current is gauge invariant, which the free current was not. The quantum potential is untouched by the connection, so the error of the approximation is the free error, and the argument for that is a translation of the phase rate and not a type statement — the type of the connection's term is a property of the chart, and the corpus writes both spellings. The circulation $2\pi\hbar n+ϙ\Phi_B$ is exact and carries no $\delta$. The connection is not a small parameter of the limit and the limit does not order it; the truncated pair stays gauge invariant because the discarded term is gauge invariant by itself; and the nonrelativistic and semiclassical limits commute at leading order and not at the order of the discarded term.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$ | The central word |
| $\rho_{\mathrm{num}}=r^{2}$ | Proper density |
| $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ | The action |
| $ϙ$ | The coupling; minus the electric charge |
| $\tilde A_\Phi=i a'_t e_t+\vec A$ | The material connection; $\varphi=c\,a'_t$ |
| $\vec p=\hbar\nabla\theta_{\mathrm{pha}}$, $E=-\hbar c\,\partial_{r'_t}\theta_{\mathrm{pha}}$ | Canonical momentum and energy |
| $\vec\pi=\vec p+ϙ\vec A$, $\mathcal E=E+ϙ c\,a'_t$ | Mechanical momentum and energy |
| $\mathcal A^{\mathrm{gco}}_\mu$ | The covariant bracket; the connection adds real in $R_t$, imaginary in $r'_t$ |
| $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$ | The d'Alembertian |
| $Q=-\frac{\hbar^{2}}{2m}\Box_\Phi r/r$ | Quantum potential; unchanged by the connection |
| $\epsilon=1/(k_\Phi L)$ | The parameter of the limit |
| $\delta=1/(k_mL)=\epsilon\lvert\vec p\rvert/(mc)$ | The one-particle ratio; implied |
| $\langle\tilde P^{\mathrm{mech}}\rangle_{\natural}=-m^{2}c^{2}$ | The eikonal: mechanical mass shell |
| $\nabla\times(\vec p+ϙ\vec A)=ϙ\vec B$ | Vorticity, exact |
| $\oint(\vec p+ϙ\vec A)\cdot d\vec l=2\pi\hbar n+ϙ\Phi_B$ | Circulation, exact |

## Further Reading

- T. Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 2–80, for the relativistic Madelung pair and its charged form.
- E. Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the non-relativistic pair.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the Lorentz force, the four-potential and the mass shell.
- Y. Aharonov and D. Bohm, "Significance of electromagnetic potentials in the quantum theory," *Physical Review* **115** (1959) 485–491, for the loop statement.
- H. Feshbach and F. Villars, "Elementary relativistic wave mechanics of spin 0 and spin 1/2 particles," *Reviews of Modern Physics* **30** (1958) 24–45, for the two-sheet structure of the charged scalar.
- W. Pauli, "Relativistic field theories of elementary particles," *Reviews of Modern Physics* **13** (1941) 203–232, for the coupling of a charged scalar and the sign of its charge density.
