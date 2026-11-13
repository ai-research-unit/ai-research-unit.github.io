# __The Non-Quantum Limit of the Coupled Schrödinger Equation using the Variational Principle__

## Introduction

**The coupled limit taken on the action, and one correction it forces.** The substitution route writes the criterion as $\epsilon=1/(k_\Phi L)$ with $k_\Phi=\lvert\vec p\rvert/\hbar$. On the action that reading is too weak: the term the amplitude's gradient competes with is $r^{2}\lvert\vec\pi\rvert^{2}/(2m)$ with $\vec\pi=\nabla S_{\tilde\Xi}+ϙ\vec A$, so the wave number in the criterion is the **mechanical** one, $k_\pi=\lvert\vec\pi\rvert/\hbar$. **That is the only gauge-invariant wave number available**, because $\nabla S_{\tilde\Xi}$ moves under a gauge transformation and $\vec\pi$ does not. The criterion is therefore gauge invariant if and only if it is written on $\vec\pi$.

**Three further findings.**

*The truncation preserves gauge invariance exactly.* The dropped group is $\lvert\vec\nabla r\rvert^{2}$, which contains no connection, so it is invariant by itself. **Nothing in the passage mixes the connection into the amplitude's gradient, so the limit commutes with the gauge group.**

*The constraint is gauge invariant, and that is why the phase cannot be fixed by it.* The truncated Lagrangian is the density times the covariant bracket, and the bracket is invariant because the connection's two contributions cancel against the phase's two. So the eikonal determines the invariant combination and leaves the gauge free. Route one's rule that the expansion must be written on invariants is a consequence, not a prescription.

*The density is again a multiplier, and the current is unchanged.* The truncated Lagrangian has the form $r^{2}F_{\mathrm{gco}}(\theta,\nabla\theta)$ with $F_{\mathrm{gco}}$ the covariant constraint, so the density multiplies the constraint and its own equation is the transport. **And $-\partial\mathcal L^{\mathrm{trunc}}/\partial\vec A$ equals the exact current**, because the dropped term has no $\vec A$ in it.

**What the article does not do.** It does not re-derive the coupled polar Lagrangian, the three coupling pieces, the gauge direction or the current identity; those are *The Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Polar Variables*'s. It does not take a coupling expansion. **The limit orders $\epsilon$ and holds the field**, and the article is careful about the difference, because the two truncations are not the same one and only one of them is gauge invariant.

**Conventions.** Those of the free variational companion, with the connection $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$, $\varphi=c\,a'_t$, coupling $ϙ$, and the covariant derivative $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$. The charge $ϙ$ is minus the older electric charge, so the mechanical momentum is $\vec\pi=\vec p+ϙ\vec A$ and the potential energy enters as $-ϙ\varphi$. The word is $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$, $\rho=r^{2}$, $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$, and $\mathcal E=-\partial_{t'}S_{\tilde\Xi}+ϙ\varphi$ is the invariant energy.

## The Coupled Action in the Chart

**The action, in the operator setting.**

$$
S=\int\mathrm{d}t'\,\mathrm{d}^{3}x\;\Bigl\{-\hbar\,r^{2}\dot\theta_{\mathrm{pha}}
-\frac{\hbar^{2}}{2m}\Bigl(\lvert\vec\nabla r\rvert^{2}+r^{2}\Bigl\lvert\vec\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\Bigr\rvert^{2}\Bigr)
-r^{2}V_{\mathrm{op}}+ϙ\varphi\,r^{2}\Bigr\}.
$$

**Four groups, and the coupling sits in two of them.** The density times the phase rate; the density times the covariant kinetic term; the amplitude's gradient; the density times the potential energy. **The second group is where the connection does all of its work, and the third is where it does none**, because $\vec\nabla r$ carries no charge.

| group | term | the connection | the limit |
|---|---|---|---|
| the phase's rate | $-\hbar\,r^{2}\dot\theta_{\mathrm{pha}}$ | not here; $\varphi$ enters separately as $+ϙ\varphi r^{2}$ | keeps |
| the covariant kinetic term | $-\frac{\hbar^{2}}{2m}r^{2}\bigl\lvert\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\bigr\rvert^{2}$ | all of it, in three pieces | keeps |
| the amplitude's gradient | $-\frac{\hbar^{2}}{2m}\lvert\vec\nabla r\rvert^{2}$ | **nothing** | **drops** |
| the potential | $-r^{2}V_{\mathrm{op}}+ϙ\varphi r^{2}$ | the scalar potential | keeps |

**The three pieces of the second group.** Expanding the covariant square,

$$
-\frac{\hbar^{2}}{2m}r^{2}\Bigl\lvert\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\Bigr\rvert^{2}
=-\frac{\hbar^{2}}{2m}r^{2}\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}
-\frac{\hbar ϙ}{m}r^{2}\,\vec A\cdot\nabla\theta_{\mathrm{pha}}
-\frac{ϙ^{2}}{2m}r^{2}\lvert\vec A\rvert^{2},
$$

**the free term, the paramagnetic term and the diamagnetic term.** The parent records that the three are one object read at three orders, and that the third's sign is what bounds the kinetic energy below.

**The one fact the limit turns on.** The amplitude's gradient is the only group with no connection in it. **That is not an accident of the central word**: $\vec\nabla r$ is a real gradient of a real magnitude, and the covariant derivative acts on the phase and on the frame, not on the scale. The whole of the article's gauge statement follows from this one observation.

## The Criterion, and Which Wave Number

**Every surviving term is a density times a scalar, and the scalars are invariants.**

$$
-\hbar\,r^{2}\dot\theta_{\mathrm{pha}}+ϙ\varphi\,r^{2}=r^{2}\bigl(-\partial_{t'}S_{\tilde\Xi}+ϙ\varphi\bigr)=r^{2}\mathcal E,
\qquad
-\frac{\hbar^{2}}{2m}r^{2}\Bigl\lvert\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\Bigr\rvert^{2}=r^{2}\frac{\lvert\vec\pi\rvert^{2}}{2m}.
$$

**The dropped group is the second times $\epsilon^{2}$, with $\epsilon$ built on the mechanical wave number.**

$$
\frac{\frac{\hbar^{2}}{2mL^{2}}}{\frac{\lvert\vec\pi\rvert^{2}}{2m}}=\frac{\hbar^{2}}{\lvert\vec\pi\rvert^{2}L^{2}}=\frac{1}{(k_\pi L)^{2}}=\epsilon^{2},
\qquad
k_\pi=\frac{\lvert\vec\pi\rvert}{\hbar}.
$$

**And $k_\pi$ is the only choice that is gauge invariant.** Under $\tilde\Xi\mapsto e^{iϙ\Gamma/\hbar}\tilde\Xi$ the phase moves by $ϙ\Gamma/\hbar$ and the vector potential moves by $-\vec\nabla\Gamma$, so $\vec\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A$ is invariant while $\vec\nabla\theta_{\mathrm{pha}}$ is not. **A criterion written on $k_\Phi=\lvert\nabla S_{\tilde\Xi}\rvert/\hbar$ would change value under a gauge transformation and would therefore not be a criterion at all.**

**What that does to the earlier statement.** The substitution article writes $\epsilon=1/(k_\Phi L)$ and is right in the free case, where the two wave numbers coincide. In the coupled case it is right in order of magnitude and wrong in principle, and the correction is one letter:

$$
\epsilon=\frac{1}{k_\pi L},
\qquad
k_\pi=\frac{\lvert\vec p+ϙ\vec A\rvert}{\hbar}.
$$

**A corollary, and it is worth stating because it is counter-intuitive.** A strong vector potential raises $k_\pi$ and lowers $\epsilon$, so **a strong field makes the limit easier to satisfy and not harder**. That is not a statement about the field being weak; it is the statement that the short-wavelength parameter is set by the mechanical momentum, which is what the surviving kinetic term is built from.

**The field's own ratios are chart statements.** The paramagnetic term against the free term is $ϙ\lvert\vec A\rvert/\lvert\vec p\rvert$, and neither factor is invariant: a gauge transformation moves both. **The split into three pieces is a chart statement, and only the sum is physical.** So no criterion can be built on "the coupling is small", and the article does not build one. The limit orders one ratio, $\epsilon$, and leaves the field's magnitude entirely free.

**The second ratio.** $1/(k_mL)$ with $k_m=mc/\hbar$ is the Compton length over $L$, the one-particle window as in the free companion, and it is not the criterion. Here it is also the only surviving non-invariant-looking quantity that is in fact invariant, since $m$ and $L$ carry no charge.

**The table.**

| comparison | ratio | invariant? | ordered by the limit |
|---|---|---|---|
| amplitude's gradient against the covariant kinetic term | $\epsilon^{2}=1/(k_\pi L)^{2}$ | **yes** | yes; the limit is $\epsilon\to0$ |
| amplitude's gradient against the rest term's analogue | $1/(k_mL)^{2}$ | yes | implied; the one-particle window |
| paramagnetic against free kinetic | $ϙ\lvert\vec A\rvert/\lvert\vec p\rvert$ | no | **no** |
| diamagnetic against free kinetic | $(ϙ\lvert\vec A\rvert/\lvert\vec p\rvert)^{2}$ | no | **no** |

**Read the last two rows as one.** They are the two halves of a single invariant, $\lvert\vec\pi\rvert^{2}=\lvert\vec p\rvert^{2}+2ϙ\vec A\cdot\vec p+ϙ^{2}\lvert\vec A\rvert^{2}$, and a statement about either half alone is a statement about a chart.

## The Truncated Action

**Delete the amplitude's gradient, and only it.**

$$
S^{\mathrm{trunc}}=\int\mathrm{d}t'\,\mathrm{d}^{3}x\;r^{2}F_{\mathrm{gco}},
\qquad
F_{\mathrm{gco}}=-\hbar\dot\theta_{\mathrm{pha}}
-\frac{\hbar^{2}}{2m}\Bigl\lvert\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\Bigr\rvert^{2}-V_{\mathrm{op}}+ϙ\varphi .
$$

**The bracket is the covariant constraint.** In terms of the invariants,

$$
F_{\mathrm{gco}}=-\mathcal E-\frac{\lvert\vec\pi\rvert^{2}}{2m}-V_{\mathrm{op}},
$$

**so $F_{\mathrm{gco}}=0$ is $\mathcal E=\lvert\vec\pi\rvert^{2}/(2m)+V_{\mathrm{op}}$**, the eikonal of the substitution article, exactly.

**Varying the phase.**

$$
\frac{\partial}{\partial t'}\bigl(\hbar\,r^{2}\bigr)+\vec\nabla\cdot\Bigl(\frac{\hbar^{2}}{m}r^{2}\Bigl(\vec\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\Bigr)\Bigr)=0
\qquad\Longleftrightarrow\qquad
\frac{\partial\rho}{\partial t'}+\vec\nabla\cdot\Bigl(\rho\frac{\vec\pi}{m}\Bigr)=0 .
$$

**The covariant continuity equation, exact.** The truncation cannot touch it, because the discarded term contains no $\theta_{\mathrm{pha}}$.

**Varying the amplitude.**

$$
-\hbar\dot\theta_{\mathrm{pha}}-\frac{\hbar^{2}}{2m}\Bigl\lvert\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\Bigr\rvert^{2}-V_{\mathrm{op}}+ϙ\varphi=0 ,
$$

**which is the eikonal and nothing else.** The quantum potential was this term's variation and went with it.

**The checks, with a constant connection $\vec A=(0.6,0,0)$ and $ϙ\varphi=0.175$.** On a $31\times31$ grid against central differences of the discrete action: the amplitude variation matches to $3\times10^{-6}$ relative in the exact and in the truncated functional; the phase variation matches to $1\times10^{-7}$ and is **identical in the two functionals to $10^{-6}$**, which is the numerical statement that the discarded term is $\theta$-independent.

**One sentence.** The limit drops the only gauge-invariant group that has no connection in it, and leaves a Lagrangian that is the density times the covariant constraint.

## The Density Is the Multiplier, and the Constraint Is Invariant

**The multiplier form.**

$$
\mathcal L^{\mathrm{trunc}}=r^{2}F_{\mathrm{gco}},
\qquad
\frac{\delta S^{\mathrm{trunc}}}{\delta r}=2rF_{\mathrm{gco}} .
$$

**So $r^{2}$ multiplies the covariant constraint**, and the phase's equation is the transport of the multiplier by the constraint's current. The structure is the free companion's, with covariant letters.

**$F_{\mathrm{gco}}$ is gauge invariant, term by term.** The phase rate and the scalar potential move by opposite amounts, $-\hbar\dot\theta_{\mathrm{pha}}\mapsto-\hbar\dot\theta_{\mathrm{pha}}-ϙ\dot\Gamma$ and $ϙ\varphi\mapstoϙ\varphi+ϙ\dot\Gamma$; and the covariant gradient is invariant by construction. **So the constraint is invariant, and the two invariances are one: the phase's two appearances are the two halves of the covariant derivative in time.**

**The consequence, and it explains a rule the substitution route had to impose.** A constraint that is invariant can only determine invariants. So the eikonal fixes $\mathcal E$ and not $\theta_{\mathrm{pha}}$, and the phase's residual freedom is the gauge freedom. **The substitution article's rule — write the expansion on invariants — is therefore not a methodological preference but a consequence of what the truncated action can say.** The phase is one coordinate of a redundant description, and a constraint on the description cannot fix a redundant coordinate.

**What the multiplier does not do.** It does not become a Lagrange multiplier for a gauge constraint. The gauge direction is a redundancy of the *field*, and the constraint $F_{\mathrm{gco}}=0$ is the *limit's* constraint; the two are different objects and the article keeps them apart. The first says that two parameter sets describe one field; the second says that the classical field's phase obeys an equation of first order.

**The counting.** One primary constraint, $p_r=0$, in the parent and in the truncation, exactly as in the free companion; one secondary constraint which is the amplitude's equation, second order in space in the parent and algebraic in the truncation; and the gauge direction, which is a redundancy and not a degree of freedom in either. **The coupling changes none of the three counts.** That is the parent's finding — the coupling neither creates a constraint nor removes one — carried through the limit.

## Gauge Invariance Is Preserved Exactly

**The argument is one line, and it is the reason the truncation is legitimate.** The dropped group is $-\frac{\hbar^{2}}{2m}\lvert\vec\nabla r\rvert^{2}$. It contains $r$ and its gradient and nothing else, and $r\mapsto r$ under the gauge group. **So the dropped group is invariant, the truncation of an invariant action by an invariant subgroup is invariant, and the limit commutes with the gauge transformation.**

**Why the three coupling pieces must go together.** They are one square, and a truncation that kept the free term and the paramagnetic term and dropped the diamagnetic one would (i) not be this limit, since it would be an expansion in $ϙ\vec A$ and not in $\epsilon$, and (ii) not be gauge invariant, since the three pieces are not separately invariant. **The kinetic energy would also not be bounded below**, because the quadratic term is the positive one. So the coupling expansion is a different limit, and the difference is visible in the action and not only in the answers.

**What the limit and the gauge group have in common.** Both act on the phase; neither acts on the scale. That is why they commute, and it is worth saying in that form: **the limit is a statement about the scale, the gauge group is a statement about the phase, and the two coordinates are independent in the chart.** In the general element the frame would be involved and the statement would need the frame's brackets, which is the parent's cross-term warning; on the central field the two coordinates are all there is.

**A test the article can perform and the substitution route cannot.** Take a gauge transformation with a constant $\Gamma$: it shifts the phase everywhere and leaves the field unchanged. In the parent action the shift changes the kinetic term and the potential term by equal and opposite amounts, and the total is unchanged up to no boundary because $\Gamma$ is constant. In the truncated action the same happens with $r^{2}$ in place of $r^{2}\cosh\theta_{\mathrm{rpd}}$. **So the truncated action is invariant under the same group, with the same mechanism, and the multiplier is invariant.**

## The Current and the Vorticity

**The current is the action's derivative, and it is unchanged by the truncation.**

$$
-\frac{\partial\mathcal L}{\partial\vec A}=\frac{\hbar^{2}}{2m}r^{2}\cdot2\Bigl(\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\Bigr)\frac{ϙ}{\hbar}
=ϙ\,\frac{\rho\,\vec\pi}{m}=ϙ\,\vec j ,
$$

**in the exact and in the truncated Lagrangian alike**, because the only $\vec A$-dependence of either is the covariant square. The identity was verified numerically at a sample point.

**The reading.** The current's three pieces — gradient, linear, quadratic — are one object, and only the sum is invariant. In the truncated theory the same three pieces are present and the same identity holds, so **the limit does not deform the current**. A conservation law that is a variation survives a truncation that leaves the variation alone.

**The vorticity.** The velocity is $\vec\pi/m$, and its curl is

$$
\vec\nabla\times\vec v=\frac{ϙ}{m}\vec B ,
$$

**exactly, in both theories.** In the parent this is a property of the pair; in the truncated theory it is the statement that the dust is rotational exactly where the field is, because the constraint's gradient is the Lorentz force and the curl of that force is the field. The integral form is the circulation quantum $\oint\vec v\cdot d\vec l=(2\pi\hbar n+ϙ\Phi_B)/m$, which contains no $\epsilon$ at all and is therefore inherited by the limit rather than produced by it.

**What the limit adds to the vorticity statement.** Nothing, and that is the point: a topological statement about a loop cannot be ordered in $\epsilon$, so any limit that changed it would be wrong. The circulation is the corpus's sharpest test of a limit, and this one passes it because the phase's Euler–Lagrange equation is untouched.

## The Triangular Structure, With the Field

**After the truncation, in order.**

1. The eikonal fixes the invariant energy: $\mathcal E=\lvert\vec\pi\rvert^{2}/(2m)+V_{\mathrm{op}}$, with $\mathcal E=-\partial_{t'}S_{\tilde\Xi}+ϙ\varphi$ and $\vec\pi=\nabla S_{\tilde\Xi}+ϙ\vec A$.
2. The flow is $\vec v=\vec\pi/m$, and its acceleration is the Lorentz force, which follows from taking the gradient of the eikonal once.
3. The covariant continuity equation transports $\rho$ along that flow.
4. Nothing else is required.

**Step one is one equation for one invariant**, and the gauge freedom is what makes that possible: a scalar equation cannot fix a coordinate that has a redundancy, so the equation must be for the invariant, and it is.

**Before the truncation step one needs $Q$**, which needs $\Delta_\Phi r$, and the four steps do not close. The limit is what makes them an algorithm, in this family exactly as in the three others.

## What the Variational Route Adds

**Four things, in order of importance.**

*The wave number.* The criterion is $\epsilon=1/(k_\pi L)$ with $k_\pi=\lvert\vec\pi\rvert/\hbar$, and this is the only gauge-invariant reading. The substitution route's $k_\Phi$ is correct only in the free case. **This is the article's correction to the route-one statement**, and it is not a refinement of notation: a criterion that moves under gauge transformations is not a criterion.

*The gauge invariance of the truncation, proved rather than checked.* The dropped group is invariant because it carries no charge, so the limit commutes with the gauge group. The substitution route can verify this on the resulting equations; the action shows why.

*Why the expansion must be written on invariants.* The truncated constraint is invariant, so it can only determine invariants; the phase's freedom is the gauge freedom. The rule that route one states as a requirement is, on this route, a consequence of the form of $\mathcal L^{\mathrm{trunc}}$.

*The difference between the two truncations.* Dropping the amplitude's gradient and expanding in the coupling are different operations with different properties: the first is invariant and bounded below, the second is neither. **The action is the only place where the two are visibly different**, because the object that distinguishes them is the single square $\lvert\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\rvert^{2}$.

**What it does not add.** No new solution, no new prediction, no new constraint. The pair is the substitution article's pair.

## Summary

The coupled polar action in the operator setting has four groups, and the connection sits entirely in one of them: the covariant kinetic square, whose three pieces are the free term, the paramagnetic term and the diamagnetic term. The amplitude's gradient is the only group with no connection in it, and it is the group the limit drops. Because every surviving term is a density times an invariant, the criterion is read directly off the action as $\epsilon=1/(k_\pi L)$ with $k_\pi=\lvert\vec\pi\rvert/\hbar$ — **the mechanical wave number, which is the only gauge-invariant one**, so that the substitution article's $k_\Phi$ is right only in the free case, and a strong field makes the limit easier rather than harder.

The truncated action is the density times the covariant constraint, so the density is the Lagrange multiplier of $\mathcal E=\lvert\vec\pi\rvert^{2}/(2m)+V_{\mathrm{op}}$ and its own equation is the covariant continuity equation. The constraint is gauge invariant term by term, which is why it can fix $\mathcal E$ and cannot fix the phase, and that is the origin of the rule that the expansion must be written on invariants. The truncation preserves gauge invariance exactly, because the dropped group carries no charge; the current $-\partial\mathcal L/\partial\vec A=ϙ\rho\vec\pi/m$ and the vorticity $ϙ\vec B/m$ are unchanged, and the circulation quantum is inherited rather than produced. $p_r=0$ in the parent and in the truncation, so the limit creates no constraint and only turns a second-order spatial equation into an algebraic one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S$ | The coupled polar action in the operator setting; four groups |
| $r^{2}\lvert\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\rvert^{2}\hbar^{2}/2m$ | The covariant kinetic group; all of the connection is here |
| $\lvert\vec\nabla r\rvert^{2}\hbar^{2}/2m$ | The amplitude's gradient; the only group dropped; carries no charge |
| $+ϙ\varphi\,r^{2}$ | The scalar potential's term; pairs with $-\hbar r^{2}\dot\theta_{\mathrm{pha}}$ |
| $\vec\pi=\hbar\nabla\theta_{\mathrm{pha}}+ϙ\vec A$ | The mechanical momentum; invariant |
| $\mathcal E=-\hbar\dot\theta_{\mathrm{pha}}+ϙ\varphi$ | The invariant energy |
| $\epsilon=1/(k_\pi L)$, $k_\pi=\lvert\vec\pi\rvert/\hbar$ | The parameter of the limit; the only invariant choice |
| $1/(k_mL)$ | The one-particle window; not the limit |
| $F_{\mathrm{gco}}=-\mathcal E-\lvert\vec\pi\rvert^{2}/2m-V_{\mathrm{op}}$ | The covariant constraint the density multiplies |
| $-\partial\mathcal L/\partial\vec A=ϙ\rho\vec\pi/m$ | The current, identical in both theories |
| $\vec\nabla\times\vec v=ϙ\vec B/m$ | The vorticity, identical in both theories |
| $p_r=0$ | The primary constraint, in the parent and in the truncation |
| $ϙ\lvert\vec A\rvert/\lvert\vec p\rvert$ | A chart ratio; not a criterion |

## Further Reading

- E. Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the hydrodynamic action.
- T. Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8** (1952) 143–182, for the hydrodynamic reading of a charged fluid.
- F. London, "Zur Theorie der supraelitenden Zustände," *Zeitschrift für Physik* **54** (1929) 408–421, for the rigidity of the wave function's phase and the current as the action's derivative with respect to the potential.
- M. V. Berry, "Quantum phase corrections from adiabatic iteration," *Proceedings of the Royal Society of London A* **414** (1987) 31–46, for the gauge invariance of the invariant combinations and the covariance of the phase.
- P. A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for primary and secondary constraints and a multiplier that is a field.
- C. M. Bender and S. A. Orszag, *Advanced Mathematical Methods for Scientists and Engineers* (Springer, 1999), chapter 10, for the short-wavelength expansion with a vector potential and the role of the mechanical rather than the canonical momentum.
- M. V. Berry and K. E. Mount, "Semiclassical approximations in wave mechanics," *Reports on Progress in Physics* **35** (1972) 315–397, for the gauge-invariant form of the short-wavelength parameter.
