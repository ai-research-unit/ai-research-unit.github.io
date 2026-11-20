# __The Lagrangian and the Dirac Equation in Momentum Space__

## Introduction

**In momentum space the Dirac action stops being a functional of neighbouring events and becomes an algebraic quadratic form at each wave number.** *The Lagrangian and the Dirac Equation* writes the action, varies it to the chiral pair, and derives the currents. This article performs the transform on that action and reads what the transform does to the three objects the variation rests on: the real part, the integration by parts and the Hessian.

**Three things happen, and each is exact.** The real part becomes redundant, because the momentum-space bracket is the expectation of a Hermitian element and is therefore real for every field; the verification covered one hundred random fields with generic complex coefficients, and the largest imaginary part was $2.2\times10^{-15}$. The integration by parts becomes unnecessary, because a multiplier needs none, so the action is evaluated at one wave number at a time with no time-slicing. And the second variation stops being an operator and becomes one central scalar, $\langle i\tilde K_\Phi\rangle_\natural-k_m^{2}=k^{2}-k_m^{2}$, so that the dispersion relation is a number's vanishing rather than a matrix's determinant.

**The last of the three closes the parent's third open question in one precise respect.** The parent records that "the action is the extremum's object; the path integral is the sum over configurations", and that the second is not attempted there. In momentum space the two objects stand in a definite relation: the variational output is the zero of the central scalar and the path integral's free propagator carries its pole. **Zero and pole are one object read twice**, and the relation is not an analogy.

**What the article does not do is construct the path integral.** The integral is the companion articles' work. What is added here is the momentum-space reading of the action and the statement that the two objects are one function's zero and its inverse.

**The denial is stated plainly.** The transform acts on $\mathbb{B}$-valued fields and returns $\mathbb{B}$-valued fields. The Hermiticity statements below are statements about the symbol's coefficients. **There is no new prediction and no new solution**; the action, the pair and the currents are the parent's.

## Conventions

The algebra and the invertibles are those of *Algebra and Element Conventions*, the gradient those of *Operator and Calculus Conventions*, the products those of *Product and Form Conventions*, the two forms those of *Norm and Pairing Conventions*, the invertibles and the material time those of *Physics Units and Common Elements Conventions*. The transform is the one of *Derivatives, Fields and Transforms*, with the symbol rule

$$
\tilde\nabla_\Phi\longmapsto i\tilde K_\Phi ,
\qquad
(\tilde\nabla_\Phi)^{\natural}\longmapsto i\tilde K_\Phi^{\natural},
\qquad
\tilde K_\Phi=ik_t'e_t+\vec k_\Phi ,
\qquad
k_t'=\frac{\omega}{c}.
$$

The parent's action is quoted once and not re-derived. It is

$$
S=\frac{\hbar c}{2}\int\mathrm{d}^4r\;\mathrm{Re}\,\mathrm{Sc}\Bigl[\tilde\Xi_L^{*}\,\tilde\nabla_\Phi^{\natural}\tilde\Xi_L+\tilde\Xi_R^{*}\,\tilde\nabla_\Phi\tilde\Xi_R-k_m\bigl(\tilde\Xi_L^{*}\tilde\Xi_R+\tilde\Xi_R^{*}\tilde\Xi_L\bigr)\Bigr],
$$

with $k_m=mc/\hbar$, the two parts $\tilde\Xi_L$ and $\tilde\Xi_R$ and the Hermitian pairing $\mathrm{Sc}(\cdot^{*}\cdot)$. The two parts are not values; the parent's warning applies unchanged, and no display below splits a value.

### The Constant-Coefficient Licence

**Constant coefficients.** The momentum-space action is a family of quadratic forms only where the symbol is constant. The mass is constant, so the free action transforms exactly and every display above is exact. With a potential the symbol depends on the position, the transform of the action is a convolution, the Hessian is an operator again, and the central-scalar statement stops. *The Lagrangian and the Coupled Dirac Equation* and *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* are where that case is treated, and nothing here anticipates them.

**Where the mass sits.** The second variation is $\langle i\tilde K_\Phi\rangle_\natural-k_m^{2}$, with the mass subtracted as a central number. It is not $\langle i\tilde K_\Phi-k_m\rangle_\natural$, and the difference is not small:

$$
\langle i\tilde K_\Phi-k_m\rangle_\natural
=k^{2}+2k_mk_t'+k_m^{2},
$$

checked to $3.9\times10^{-16}$ over five momenta. On $k_t'=1$, $\vec k_\Phi=(0.6,0,0)$ and $k_m=0.7$ the wrong object is $2.53$ and the right one is $0.64-0.49=0.15$. The norm is not linear in its argument, so the mass cannot sit inside it; it is a coefficient of the action, and the composition of the pair subtracts it from a number.

**The measure.** The momentum-space measure's constant is the transform's convention, and the action's overall constant is the parent's $\frac{\hbar c}{2}$. No display above depends on either, and no normalization is claimed.

**The denial, once more.** The two parts remain elements of $\mathbb{B}$, the pair remains a pair of equations on elements, and the centrality of the second variation is a statement about one coefficient's behaviour. No sector flip occurs at any step.

## The Action in Momentum Space

**The transform of the action replaces each derivative by a multiplier and each integration by parts by nothing.** The action becomes

$$
S=\frac{\hbar c}{2}\int\frac{\mathrm{d}^4k}{(2\pi)^4}\;\mathrm{Sc}\Bigl[\tilde\Xi_L^{*}\,i\tilde K_\Phi^{\natural}\tilde\Xi_L+\tilde\Xi_R^{*}\,i\tilde K_\Phi\tilde\Xi_R-k_m\bigl(\tilde\Xi_L^{*}\tilde\Xi_R+\tilde\Xi_R^{*}\tilde\Xi_L\bigr)\Bigr],
$$

with $\tilde\Xi_{L}$ and $\tilde\Xi_{R}$ now the transforms of the two parts. The measure is the transform's own constant and no statement below depends on it; the four terms are the parent's four, in the same order, with the multipliers in place of the derivatives.

**Nothing differentiates anything.** The action is a sum of terms, each of which pairs the field at one wave number with the field at the same wave number through one element of $\mathbb{B}$. There is no coupling between different wave numbers in the free case, so the action is a family of quadratic forms indexed by $\tilde K_\Phi$, and the variation is algebraic at each index.

**That is what the transform buys, and it is a bookkeeping gain rather than a physical one.** The physics is the same equation. The gain is that three questions — is the bracket real, does it need a boundary term, what is the second variation — become questions about one element at one wave number instead of questions about a functional.

**The pairing. Settled once and inherited.** The pairing is $\mathrm{Sc}(\cdot^{*}\cdot)$, and the reality part of §*The Action* of *The Lagrangian and the Dirac Equation* is where the quaternionic alternative was rejected.

**The type of the coefficient. In position space the real part is a statement about the adjoint.** The parent's derivation shows that each kinetic density is real up to a divergence, that the divergence integrates away, and that the imaginary part of the bracket is therefore a surface term. One sentence of it is worth quoting: the $i$ inside the material time is what makes the temporal kinetic term self-adjoint without disturbing the spatial ones.

**In momentum space the real part is a statement about the multiplier, and it is the same statement.** Take any element $\tilde A$ of $\mathbb{B}$ with complex coefficients and a wave-number element $\tilde K_\Phi$ off the shell. Then

$$
\mathrm{Sc}\bigl(\tilde A^{*}\,i\tilde K_\Phi\,\tilde A\bigr)
=\overline{\mathrm{Sc}\bigl(\tilde A^{*}\,i\tilde K_\Phi\,\tilde A\bigr)} .
$$

because $i\tilde K_\Phi$ is Hermitian: $\mathrm{Sc}(\tilde A^{*}H\tilde A)$ is real for every Hermitian $H$ and every $\tilde A$. The check covered one hundred random $\tilde A$ and as many random momenta, and the largest imaginary part of the bracket was $2.2\times10^{-15}$. **So the $\mathrm{Re}$ of the momentum-space action removes nothing**, and writing it or not writing it is the same functional.

**The two readings are one mechanism seen twice.** In position space the central $i$ sits in the coordinate $R_t=ir_t'$ and splits the four derivative directions into one anti-Hermitian and three Hermitian; the real part then cancels the one imaginary contribution. In momentum space the same $i$ sits in front of the symbol and makes all four directions Hermitian at once; the real part then has nothing to cancel. **One element, used in one place at a time, and the real part is the trace of where it was used.**

**A reader should not conclude that the real part was a decoration.** Without it the position-space functional is not real, and the variation is not the pair; the parent shows both. The claim here is narrower: the real part's work is done by the symbol's Hermiticity once the transform is taken, so the momentum-space action needs no boundary argument and no surface term.

**The selection rule. Not examined here.** The symbol is Hermitian by the article's licence; which potentials are admissible is the scalar family's question, where the potential is a free element and can be neither.

**What reality does not buy. Not at issue here.** The section establishes that the real part removes nothing at a mode. That is a statement about the $\mathrm{Re}$ device and not about the gap between a real action and a real spectrum, which the limit reading measures.

## The Variation

**The variation is algebraic, and that is the whole difference from position space.** The mode form $Q$ of the previous section is a quadratic form in the amplitude: it contains the amplitude and its conjugate and no derivative of either, because the transform has replaced every derivative by a multiplier. So the variation with respect to the conjugate amplitude is

$$
\delta Q=\mathrm{Sc}\bigl[\delta X^{*}\,\mathcal{S}(\omega,\vec k)X\bigr],
$$

with no integration by parts, no surface term and no boundary condition. A boundary term appears in a variational principle because a derivative is varied; here no derivative is varied, so none appears. That is not a convenience of the calculation, it is what the transform does to the principle.

**Stationarity is the symbol equation.** Vanishing for every $\delta X^{*}$ forces the bracket to vanish, by the same positivity argument as in the element article: choose $\delta X^{*}$ equal to the bracket and the scalar part becomes a sum of squared moduli. So

$$
\mathcal{S}(\omega,\vec k)\,X=0,
$$

the symbol equation the article solves. The passage from the action to the equation is one line and it is exact: the fixed-frequency action's stationarity and the symbol equation are the same statement.

**What is lost, and it must be said.** The variation at a mode cannot see a boundary condition, a topological charge or a spatially varying coefficient, because a mode is defined only where the coefficients are constant. Every statement in this section inherits the constant-coefficient licence that the section on limits makes explicit.

### The Second Variation: One Central Scalar

**Compose the two members of the pair and the operator's square is a number.** In momentum space the pair is

$$
i\tilde K_\Phi\,\tilde\Xi_R=k_m\tilde\Xi_L,
\qquad
i\tilde K_\Phi^{\natural}\,\tilde\Xi_L=k_m\tilde\Xi_R .
$$

Substituting the first into the second gives $i\tilde K_\Phi^{\natural}i\tilde K_\Phi\tilde\Xi_R=k_m^{2}\tilde\Xi_R$, and the left side is central:

$$
i\tilde K_\Phi^{\natural}\,i\tilde K_\Phi
=-\tilde K_\Phi^{\natural}\tilde K_\Phi
=-\tilde K_\Phi\tilde K_\Phi^{\natural}
=\langle i\tilde K_\Phi\rangle_\natural
=k^{2},
\qquad
k^{2}=k_t'^{2}-k_\Phi^{2},
$$

where both minus signs are $i^{2}$ and the middle step is the norm's order-independence. So the second variation of the action at a mode is the central scalar

$$
\langle i\tilde K_\Phi\rangle_\natural-k_m^{2}=k^{2}-k_m^{2}.
$$

**The check is exact and it covered three momenta.** On $k^{2}=7$ and on $k^{2}=0.4375$, $\langle\tilde K_\Phi\rangle_\natural$ came out $-k^{2}$, $\langle i\tilde K_\Phi\rangle_\natural$ came out $+k^{2}$, and $i\tilde K_\Phi^{\natural}i\tilde K_\Phi$ came out $+k^{2}$, each with zero imaginary part; on the null momentum $k^{2}=0$ all three vanished.

**Centrality is the point.** The second variation of a biquaternionic action is normally an element or an operator, because the Hessian of a functional on a non-commutative algebra is a bilinear form that need not be central. Here it is a number. **That is why the corpus can write the mass shell as a scalar equation** $\tilde K_\Phi\tilde K_\Phi^{\natural}=-k_m^{2}$ rather than as the vanishing of a determinant, and it is why the dispersion relation of the Dirac equation in this algebra is one equation and not a spectral problem.

**The number is the one the variational parent's action was built to produce.** The parent's variation gives the pair; composing the pair gives this scalar; the scalar's vanishing is the shell. The action therefore knows the shell twice, once through each member, and the two readings agree because the norm is central.

### Zero, Pole and the On-Shell Action: Zero and Pole Are One Object

**The variational output is the zero.** The pair's compatibility condition is $(k^{2}-k_m^{2})\tilde\Xi_R=0$, so the solutions of the equation of motion are supported exactly where the central scalar vanishes. The variational principle's content in momentum space is therefore: on the shell, any amplitude solves the pair; off it, none does.

**The path integral's free propagator has the pole.** The path-integral companion writes the free Dirac kernel in momentum space with the denominator $\langle\tilde K_\Phi\rangle_\natural+k_m^{2}$, which is $-k^{2}+k_m^{2}$, the negative of the second variation. The kernel is large exactly where the scalar vanishes, and its residue there is the numerator the companion computes.

**The two are one function, read at its zero and at its inverse.** Writing $N(\tilde K_\Phi)=k^{2}-k_m^{2}$, the variational statement is $N=0$ and the propagator is proportional to $1/N$. Neither statement is more fundamental, and neither implies the other without the construction in between: the zero selects the support and the pole gives the weight.

**This is the precise sense in which the parent's third open question is closed.** The parent asked for the path integral and did not attempt it. The answer attempted here is not the integral; it is the observation that the two objects the parent separated — the extremum's object and the sum over configurations — meet in one momentum-space function, one at its zero and the other at its pole. **The construction of the sum is the companion articles' work, and the relation is the reason the two articles describe one theory.**

### The Legendre Transform

**A first-order form has a degenerate transform.** The mode action is linear in the frequency, so its derivative with respect to $\omega$ does not contain $\omega$; the transform therefore does not invert, and it returns a condition on the amplitude rather than an energy. **That is not a defect of this reading: it is the same statement the element article makes when it says that three momenta vanish identically.**

**What the condition is.** The derivative of the form with respect to $\omega$ is the density, and the requirement that the density be the conjugate of the frequency is the constraint. **At a fixed wave number the constraint is one condition on four amplitudes**, and the remaining three are the energy's carriers. So the transform gives one constraint and three degrees of freedom, which is the Dirac field's count in the mode language.

**Where the two branches are, then.** They are the two eigenvalues of the Hamiltonian at that wave number, not two roots of a quadratic. **The reading distinguishes the two by the sign of the eigenvalue and not by the sign of the root**, and the distinction is the same one in either language.

**The transform's one number.** The slope of the action with respect to the frequency is $\hbar$ times the norm, which is the density per mode. **The transform is therefore the map from the form's argument to the form's density**, and it is injective on the amplitude and constant on the frequency.

**Why the article still needs it.** Because the momentum reading's claim is that the mode action *is* the symbol, and a reader can test that claim only by differentiating: if the derivative in the frequency is the density and the derivative in the amplitude is the symbol, the identification is complete. **The transform is the test, not a new result.**

**One caution.** On shell the form vanishes, so the transform of the on-shell form is zero. **The transform must be taken before the equation is imposed**, and the article says so once, because the opposite order gives a trivial answer that looks like a contradiction.

## The Constraints the Action Imposes: The Constraint Is the Frequency Condition

**At a mode the variation is algebraic and the constraint falls on the momentum.** The transform has replaced $\tilde\nabla_\Phi$ by $i\tilde K_\Phi$ and its adjoint by $i\tilde K_\Phi^{\natural}$, so the density is a quadratic form in the amplitude with no derivative left. Stationarity forces the form's bracket to vanish, and where the form is invertible the only stationary amplitude is zero.

**The condition is an eigenvalue statement, and it is satisfied twice.** The vanishing of the bracket's determinant is a quadratic in the frequency, because the two kinetic terms carry one power of it each and the mass couples them without one. Each root is a frequency at which a nonzero mode exists, so the singular set carries two frequencies per momentum, which is the momentum-space form of the two-sidedness the element article reads off the action.

**The set is the dispersion surface and the connection translates it.** At $k_m=0$ the two sheets meet on the cone; at finite mass they separate by $2k_m$. The connection's temporal slot shifts the frequency and its spatial slots rotate the wave vector, so the sheet separation is a property of the mass alone.

**What is absent, and why the absence is a statement about the chart.** No Gauss law, because the connection is fixed at a mode; no boundary condition, because a variation at one momentum cannot see one; no restriction on the amplitude at a singular momentum. The constraint content is one determinant, and the structural consequence is a claim about what that determinant leaves free.

## The Structural Consequence: The Three Objects Are One Number

**The claim.** The zero of the mode action, the pole of the free kernel and the residue that normalises that pole are three readings of one central scalar, and none of them is an independent input. **An article that fixed the shell from the equation and the normalisation from a commutator would be importing one number it already has**, and this reading does not need the import.

**Why one number is enough.** The second variation at a mode is the central scalar $N(\tilde K_\Phi)=k^{2}-k_m^{2}$ of *The Second Variation Is One Central Scalar*. The variational statement is $N=0$; a Gaussian sum over the mode's amplitude returns a power of $N$; the kernel's residue at the pole is therefore fixed by the same $N$, up to the numerator the companion writes. **Zero, pole and residue are one function read at three places**, and the centrality is what makes the third follow from the first two.

**What the centrality buys, and what it would cost to lose it.** A Hessian on the algebra is normally an element, so the three objects would sit on different footings and the normalisation would be a free choice. Here the Hessian is a number, so the choice is not free. **That is the precise content of the article's claim, and it is a statement about the algebra and not about the sum.**

**What it does not claim.** It does not evaluate the integral, compute a residue, or promote a bracket: the free normalisation is read, and the promotion of the bracket to a commutator remains the next category's step. It does not extend to an interacting mode, where the Hessian is no longer one number and the three objects separate.

**What it corrects.** *Zero and Pole Are One Object* states that the two are one function; this section states the consequence the article owns, that the third object is not a third assumption. **A reader who takes the normalisation as an input has added a postulate the action did not need.**

## The Noether Currents: The Charge Per Mode

**The charge at a mode.** The Noether charge is the spatial integral of the temporal component of the current, and by Parseval it becomes a sum over modes. At one mode the summand is the bilinear of the amplitude,

$$
\mathcal{Q}(\vec k)=\hbar\,\mathrm{Sc}\bigl[X^{*}(\vec k)X(\vec k)\bigr],
$$

up to the normalisation the element article fixes, so that the total charge is the integral of this density over the wave numbers. The step from the position-space charge to this display is Parseval's identity and nothing else; the companion article *The Lagrangian and the Schrödinger Equation in Momentum Space* proves it in that case and the proof transfers, because it uses only the transform and the Hermitian pairing.

**The energy.** The energy is the symbol evaluated at zero frequency, $E=\mathcal{S}(0,\vec k)$, which is the statement that the Hamiltonian is the generator of the frequency. On the shell the two agree with the dispersion relation, and off the shell the symbol is the energy the mode would have if it were on it.

**What the mass term does to the two.** The mass term shifts neither the charge nor the reality of the bilinear: it enters the symbol and leaves the pairing alone. What it does is remove the zero-frequency mode from the spectrum, and that removal is the count of degrees of freedom the article's structural section states.

## What the Principle Adds and What It Relabels: In Momentum Space

**What the transform adds.** One identity: the action at a fixed frequency is the quadratic form whose kernel is the symbol. That identity is worth having, because it turns the variational principle into linear algebra and the equation into a null space, and because it makes the reality of the action and the Hermiticity of the symbol one statement seen twice.

**What it relabels.** The variational principle itself: nothing is added to the physics, no new current appears, and no equation is solved that the parent did not already solve. The word *action* at a mode is a density in the frequency and the wave number, not an integral over a region, and calling it an action is a shorthand that this section keeps because the shorthand is the point.

**What it cannot reach.** The boundary term, the varying coefficient and the operator ordering. The first two need position space; the third is invisible at a constant symbol, where left and right multiplication agree. Each of those is named where the article meets it, and none is repaired by the transform.

## Open Questions

**Whether the zero-pole relation survives when the symbol is an operator.** That is, whether the path integral of the coupled theory is the inverse of the coupled action's Hessian in the same sense. It is a question about the coupled articles, stated here because the free case makes it precise, and it is not answered here.

## Summary

In momentum space the Dirac action of the variational parent becomes one algebraic quadratic form per wave number, with each derivative replaced by a multiplier and no integration by parts anywhere. The real part of the position-space action becomes redundant, because the bracket is $\mathrm{Sc}(\tilde A^{*}i\tilde K_\Phi\tilde A)$ for a Hermitian multiplier, which is real for every field: one hundred random fields gave a largest imaginary part of $2.2\times10^{-15}$.

The second variation is a single central scalar. Composing the pair gives $i\tilde K_\Phi^{\natural}i\tilde K_\Phi=\langle i\tilde K_\Phi\rangle_\natural=k^{2}$, so the second variation at a mode is $k^{2}-k_m^{2}=\langle i\tilde K_\Phi\rangle_\natural-k_m^{2}$, with no imaginary part and no matrix left to diagonalise. That centrality is why the mass shell is a scalar equation in this algebra and not a spectral condition.

The variational output is the zero of that scalar and the free propagator is proportional to its inverse: the path-integral companion's denominator $\langle\tilde K_\Phi\rangle_\natural+k_m^{2}$ is its negative. Zero and pole are one object, and that relation is the precise sense in which the variational parent's unattempted path integral is accounted for, without the integral being constructed here. The mass is subtracted as a coefficient and does not enter the norm: $\langle i\tilde K_\Phi-k_m\rangle_\natural=k^{2}+2k_mk_t'+k_m^{2}$, which is not the dispersion relation.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $S$ | The parent's action, four terms, coefficient $\frac{\hbar c}{2}$ |
| $i\tilde K_\Phi$, $i\tilde K_\Phi^{\natural}$ | The symbols of the gradient and its conjugate; Hermitian |
| $\mathrm{Sc}(\tilde A^{*}i\tilde K_\Phi\tilde A)$ | The momentum-space kinetic bracket; real for every $\tilde A$ |
| $\langle i\tilde K_\Phi\rangle_\natural=k^{2}$ | The symbol's norm; central, real, equal to the interval |
| $k^{2}=k_t'^{2}-k_\Phi^{2}$ | The interval in wave numbers |
| $\langle i\tilde K_\Phi\rangle_\natural-k_m^{2}$ | The second variation at a mode; one central scalar |
| $\langle i\tilde K_\Phi-k_m\rangle_\natural=k^{2}+2k_mk_t'+k_m^{2}$ | The wrong object; the mass inside the norm |
| $\langle\tilde K_\Phi\rangle_\natural+k_m^{2}=-(k^{2}-k_m^{2})$ | The propagator's denominator; the pole |
| $N(\tilde K_\Phi)=k^{2}-k_m^{2}$ | One function, read at its zero and at its pole |

## Further Reading

- *The Lagrangian and the Dirac Equation*, for the action, the variation, the currents and the three open questions.
- *The Fourier Transform and the Dirac Equation in Biquaternionic Form*, for the symbol, its Hermiticity and the light cone as the idempotent variety.
- *The Dirac Equation in Biquaternionic Form*, for the chiral pair and the mass coefficient.
- *The Path Integral and the Dirac Equation in Biquaternionic Form*, for the free propagator whose denominator is read here as a pole.
- *The Path Integral and the Dirac Equation in Biquaternionic Polar Variables*, for the same kernel in the polar word.
- *The Lagrangian and the Coupled Dirac Equation*, for the case in which the symbol is not constant.
- *Derivatives, Fields and Transforms*, for the transform and its symbol rule.
- *Norm and Pairing Conventions*, for the two forms, the norm's centrality and the Hermitian pairing.
- P. A. M. Dirac, "The Lagrangian in quantum mechanics," *Physikalische Zeitschrift der Sowjetunion* **3** (1933) 64–72, for the action's place in the integral and its relation to the classical extremum.
- R. P. Feynman, "Space-time approach to non-relativistic quantum mechanics," *Reviews of Modern Physics* **20** (1948) 367–387, for the sum over configurations the relation is about.
- J. H. Van Vleck, "The correspondence principle in the statistical interpretation of quantum mechanics," *Proceedings of the National Academy of Sciences* **14** (1928) 178–188, for the fluctuation determinant that a second variation produces in the position-space form.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), Chapter 2, for the free Dirac propagator's denominator and its residue in the standard language.
