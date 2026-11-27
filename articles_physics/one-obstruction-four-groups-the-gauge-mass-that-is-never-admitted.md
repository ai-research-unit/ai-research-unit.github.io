# __One Obstruction, Four Groups: The Gauge Mass That Is Never Admitted__

## Introduction

**The claim.** The argument that forbids a mass term for the gluon forbids one identically for the photon, for the $W$ and the $Z$ before breaking, and for the fifteen generators of $\mathrm{SU}(4)$. **It is one argument with four instantiations, and the corpus states it four times without ever saying so.** This article states it once.

**Why the count matters.** An audit of the corpus's actions finds one genuine action per force, and the reason is not that the forces are similar. It is that **the same filter admits the same two candidates and rejects the same one**, so four sectors reach the same short list. A reader who takes the four sector sentences as four discoveries will look for the common cause and find, correctly, that the group is not it — the *invariance requirement* is. **This article is the evidence for that claim.**

**The shape of the article.** The argument once, in the invariants; then the four cases with their different indices; then the contrast that makes it sharp — Proca, where the same mass term *is* admitted; then the conclusion about what a mass term does to a connection that a mass term does not do to a field.

## The Argument, Once

**A connection transforms inhomogeneously.** For $\tilde g$ a local group element,

$$
A_\imath\longmapsto A_\imath^{\tilde g}=\tilde gA_\imath\tilde g^{-1}+\tilde g\,\partial_\imath\tilde g^{-1},
$$

and the second term is the whole of the difference between a connection and a **tensor**. **A mass term is quadratic in $A$ with no derivative**, so it is a tensor built from a connection, and it cannot be invariant for the same reason a coordinate cannot be a vector:

$$
m^2\sum_{\imath}A_\imath^{\tilde g}A_\imath^{\tilde g}=m^2\sum_\imath\Bigl(\tilde gA_\imath\tilde g^{-1}+\tilde g\partial_\imath\tilde g^{-1}\Bigr)\Bigl(\tilde gA_\imath\tilde g^{-1}+\tilde g\partial_\imath\tilde g^{-1}\Bigr).
$$

**Expand and the cross term survives.** The conjugation part gives back $m^2\sum A_\imath A_\imath$ by cyclicity of the trace; the derivative part gives a positive-definite contribution; and the cross term, linear in $\partial\tilde g^{-1}$, is nonzero whenever $\tilde g$ varies. **The failure is not a cancellation gone wrong — it is that the cross term has no partner**, because there is no second term in a mass term that could cancel it.

**The same statement in the infinitesimal form, which is what this section's filter actually runs.** With $\tilde g=e^{\alpha^a\tau_a}$ and $\tau_a$ anti-Hermitian, the infinitesimal variation is $\delta A_\imath=[A_\imath,\alpha]+\partial_\imath\alpha$, and the variation of the mass term is

$$
\delta\Bigl(m^2\sum_\imath A_\imath A_\imath\Bigr)=2m^2\sum_\imath A_\imath\bigl([A_\imath,\alpha]+\partial_\imath\alpha\bigr),
$$

**which vanishes for every $\alpha$ only if $m=0$.** That is [the invariance filter](which-terms-survive-invariance-as-a-linear-condition-on-a-density.html) applied to this candidate; the answer is the same in every group, and this is the point.

**One qualification, and it is the reason the argument is about a *connection* and not about a *vector*.** If $A$ were a tensor, the mass term would be admitted — that is Proca. **The obstruction is not the mass; it is the inhomogeneous term in the transformation.** Everything below is that sentence in four notations.

## The Four Cases

**U(1), the photon.** $\tilde g=e^{i\lambda}$ is abelian, so $[A,\alpha]=0$ and the variation reduces to $\delta A_\imath=\partial_\imath\lambda$. The mass term's variation is $2m^2A_\imath\partial_\imath\lambda$, which is a total derivative only when $\partial_\imath\lambda$ is constant — that is, never for a local $\lambda$. **So the photon's mass is forbidden by the abelian case of the same argument.** The abelian case is the *weakest* form: no commutator, and the obstruction survives on the derivative term alone.

**SU(2), the $W$ and the $Z$.** The variation has both pieces, and the commutator makes the failure worse and not better: $[A_\imath,\alpha]$ is generically nonzero, so even a constant $\alpha$ fails. **This is why the electroweak vector masses must come from a scalar's expectation and not from a mass term**, and why "spontaneous symmetry breaking" is not decoration: the mass term is not admitted, and the only route to a massive vector is a term that *is* admitted and produces an effective mass — the scalar's kinetic term with $\langle\Xi\rangle\neq0$.

**SU(3), the gluon.** The same computation with the eight Gell-Mann generators. **The corpus's sentence is the audit's cleanest quote**: "A mass term $m^2\sum_a\sum_\imath G_{a,\imath}G_{a,\imath}$ is not admitted, because it is not invariant; the gluon is therefore massless by what the action permits and not because its mass happens to be small." **Note what the sentence does and does not say.** It does not say the gluon's mass is unobserved; it says the action has no place to put one. That is the difference between a measurement and a theorem about the candidate space.

**SU(4), the fifteen.** The primordial sector states it in a single line of its own inventory: "**No mass for the fifteen.** A mass term $\tfrac12m^2\sum_{a,\imath}A_{a,\imath}A_{a,\imath}$ is not invariant, and none is written. The masses come from $\langle\Xi\rangle$ and are the transition's." **Four sectors, four sentences, one computation, and the group's dimension never enters it.** The $\mathrm{SU}(4)$ case is the one that makes it visible: fifteen generators, sixteen arrays, and the count of either is irrelevant to whether the mass term survives.

**What changes across the four.** Only the index range: $1$, $3$, $8$, $15$. **What does not change**: the inhomogeneous term, the cross term it produces, and the verdict. **This is the one place where four groups agree, and the agreement must be stated precisely, because it is not the claim that the group is irrelevant.** The mass term is excluded by the *form* of the transformation law, which $\mathrm{U}(1)$ and every non-abelian group share. **What the group decides is everything else in the density**, and the next section states where.

## The Contrast That Makes It Sharp: Proca

**The Proca field carries the same carrier and admits the mass term.** That is not a contradiction; it is the definition of the difference.

**A Proca field is not a connection.** It is a vector field transforming as a tensor — no inhomogeneous term — so the mass term is invariant under the only transformations the field has, and the Proca density is

$$
\mathcal L_{\mathrm{Proca}}=-\tfrac14\sum F_{\imath\jmath}F_{\imath\jmath}+\tfrac12m^2\sum_\imath A_\imath A_\imath ,
$$

with both terms admitted. **The same symbol $A$, the same carrier, the same dimension, and the opposite verdict** — because the transformation law differs.

**And the mass term does two jobs there, which is why the Proca field needs no gauge fixing.** Varying the mass term produces $m^2\partial_\imath A_\imath=0$ as part of the field equation, so **the Lorenz condition is a consequence of the action and not an extra constraint**. In the gauge theory the same role is played by the gauge choice, imposed by hand because no admitted term imposes it. **One term, admitted in one theory and forbidden in the other, carries the constraint in the one and cannot in the other.**

**The corollary the audit's count rests on.** **The Proca action is the anti-gauge action**: its mass is precisely the candidate the gauge filter rejects. That is why a massive vector and a gauge field cannot be the same object, why the electroweak vector masses require breaking, and why the corpus can present Proca and Maxwell as two actions on one carrier without either being a mistake.

## What the Groups Do Decide

**The exclusion is group-blind; the survivor set is not.** Having established that the mass term is gone for all four, the sharper fact is that **the remaining terms are group-specific, and the mechanism is the group's invariant ring.** This is the section's first claim, and it is visible here because the mass term is the one candidate the four groups agree on.

**The invariant polynomials of the adjoint are generated by $\operatorname{tr}F^k$ for $k=2,\dots,N$**, with $N$ the size of the defining representation. **$\mathrm{SU}(2)$ has no cubic: $d_{abc}\equiv0$, so $\operatorname{tr}F^3\equiv0$ identically.** $\mathrm{SU}(3)$ has a nonzero cubic, generated by $d_{abc}$; $\mathrm{SU}(4)$ has the cubic and a quartic. **The number of admissible terms at a given dimension is therefore a function of the group, and the function is the rank.**

**Where that bites, and where it does not.** At dimension four it does not bite: $\operatorname{tr}F^3$ has dimension six and the Pauli term dimension five, so the four groups' dimension-four lists coincide and the corpus's *one action per force* is a fact about dimension four and not about groups. **At dimension six — where a higher-derivative theory would place $\operatorname{tr}F^3$ — the term is admitted by $\mathrm{SU}(3)$ and $\mathrm{SU}(4)$ and forbidden by $\mathrm{SU}(2)$**, with the carrier, the transformation law and the dimension all unchanged. **That verdict is the group's and no other filter's.**

**Two further facts that are the group's.** **The reality type of the fundamental**: $\mathrm{SU}(2)$'s is pseudo-real, so a single doublet admits a Majorana mass; $\mathrm{SU}(3)$'s is complex, so a triplet alone does not, and the term requires a triplet–antitriplet pair. **And the Casimir**, which fixes the normalisation the group assigns to a term the group admits: the same $\operatorname{tr}F^2$ carries a different coefficient at each force, and the coefficient is not a convention — it is the group's index.

**So the correct pair of statements, and they must be held together.** The *gauge-mass obstruction* is group-blind, which is why four sectors state it identically. **The *survivor set* is group-specific**, which is why the four sectors' actions are not one action with a different index range. **A reader who takes this article as saying the group never decides has half the fact**: the group does not decide whether a mass term is admitted, and it decides essentially everything else.

## What This Article Does Not Claim

**It does not claim that every group forbids every mass.** A group acting on a field that is a tensor forbids nothing, and a *global* symmetry forbids nothing either — the whole of the argument is the locality of the transformation. **A mass term is forbidden by a local symmetry, not by a symmetry.**

**It does not claim the obstruction is dynamical.** Nothing here says a massive gluon is unstable or inconsistent; it says the density cannot contain the term. **Whether the resulting theory is healthy is a separate question and is not asked here.**

**It does not explain the masses that do occur.** The $W$'s, the $Z$'s and the fifteen's come from a scalar's expectation, which is a different mechanism and a different article. **This article explains the absence and only the absence.**

## Summary

A connection transforms with an inhomogeneous derivative term, so a mass term built from it cannot be invariant: the cross term produced by the derivative part has no partner to cancel it. **In the infinitesimal form the variation of $m^2\sum A_\imath A_\imath$ vanishes for every generator only when $m=0$** — the same computation in $\mathrm{U}(1)$, $\mathrm{SU}(2)$, $\mathrm{SU}(3)$ and $\mathrm{SU}(4)$, differing only in the index range $1$, $3$, $8$, $15$.

The abelian case is the weakest form and the obstruction survives on the derivative term alone; the non-abelian cases fail on the commutator as well. The corpus states the result four times — the photon's mass, the $W$'s before breaking, "the gluon is therefore massless by what the action permits and not because its mass happens to be small", and "**No mass for the fifteen**" — and never says it is one argument. **The group's dimension never enters the mass-term verdict — which shows that this one verdict is invariance's and not the group's, and is not a claim that the group decides nothing: the survivor set outside the mass term is group-specific, and §*What the Groups Do Decide* states how.**

Proca is the contrast that makes it sharp: the same carrier, the same mass term, admitted — because a Proca field is a tensor and not a connection, and the mass term there also imposes the Lorenz condition, which in the gauge theory must be imposed by hand. **The Proca action is the anti-gauge action**, and that is why a massive vector needs a broken symmetry to exist.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A_\imath$ | A connection; transforms inhomogeneously |
| $\tilde g$, $\alpha$, $\tau_a$ | A local group element, its infinitesimal parameter and generator |
| $m^2\sum A_\imath A_\imath$ | The mass term; the candidate the filter rejects |
| $a$ | The generator index: $1$, $3$, $8$, $15$ for $\mathrm{U}(1)$, $\mathrm{SU}(2)$, $\mathrm{SU}(3)$, $\mathrm{SU}(4)$ |
| $\mathcal L_{\mathrm{Proca}}$ | The Proca density; both terms admitted |
| $\langle\Xi\rangle$ | The scalar's expectation; where the electroweak and primordial masses come from |

## Further Reading

- [Which Terms Survive: Invariance as a Linear Condition on a Density](which-terms-survive-invariance-as-a-linear-condition-on-a-density.html) — the filter this article instantiates four times.
- [The Lagrangian and Quantum Chromodynamics: The Triplet, the Octet and the Feynman Rules](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html) — the gluon sentence.
- [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html) — "No mass for the fifteen."
- [The Lagrangian and the Proca Equation](the-lagrangian-and-the-proca-equation.html) — the contrast: a tensor, not a connection.
- [Electroweak Symmetry Breaking: The Doublet, the Potential and the Vector Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-vector-boson-masses.html) — the route to a massive vector once the mass term is excluded.
- [Two Filters That Never Meet: Invariance and Helmholtz](two-filters-that-never-meet-invariance-and-helmholtz.html) — why this exclusion is not a statement about the existence of an action.
