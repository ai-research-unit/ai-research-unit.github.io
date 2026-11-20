# __The Lagrangian and the Topologically Massive Gauge Field__

## Introduction

This article writes the topologically massive gauge field as one of the two eliminations of a single parent action, and shows that the mass it carries is topological because the term that carries it has one derivative and no metric. It is the action-first companion of *Dual Equivalence of the Dirac and Topologically Massive Gauge Fields*, which performs the two reductions and records the resulting pair of theories; this article asks what functional both theories come from, and why one functional can have two fields as its extremum.

**The equation.** The parent's equation is the pair of linear relations obtained by varying the two fields,

$$
\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\tilde\nabla_{\Phi,\nu}G_\lambda=\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\tilde\nabla_{\Phi,\nu}H_\lambda ,
\qquad
(m-a)G_\lambda=\sum_{\mu,\nu}\epsilon_\mu\epsilon_\nu\bigl(\tilde\nabla_{\Phi,\mu}H_\nu\bigr)^{*}i\check c_{\nu\mu\lambda},
$$

one linear in $H$ and one linear in $G$. Eliminating $H$ leaves the Dirac equation; eliminating $G$ leaves the topologically massive one.

**Three things are established.**

*First, the action.* With $G_\mu$ a complex four-vector (the s-vector), $H_\mu$ its dual potential and $\check c$ the corpus's structure-constant array,

$$
S_{GH}=\int d^4r\;\Bigl[\bigl(G_\nu+\tfrac12H_\nu\bigr)^{*}i\check c_{\nu\mu\lambda}\tilde\nabla_{\Phi,\mu}H_\lambda-\bigl(\tilde\nabla_{\Phi,\mu}H_\nu\bigr)^{*}i\check c_{\nu\mu\lambda}\bigl(G_\lambda+\tfrac12H_\lambda\bigr)+\tfrac{m-a}{2}\bigl(G\cdot G+G^{*}\cdot G^{*}\bigr)\Bigr],
$$

the stationarity conditions are the two relations above, and each elimination gives one of the two theories.

*Second, the mass is topological.* In three dimensions the reduced action is Maxwell plus a Chern–Simons term,

$$
\mathcal{L}_G=-\frac{1}{4m}\sum_{\mu,\lambda}\epsilon_\mu\epsilon_\lambda F_{\mu\lambda}F_{\mu\lambda}+\frac14\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda\,\check\varepsilon_{\nu\mu\lambda}B^{*}_\nu F_{\mu\lambda}+\text{(scalar sector)} ,
$$

whose mass term has one derivative, one power of $m$ and one Levi-Civita symbol. A mass of that shape is not a mass added to the action: it is a term whose gauge variation is a total derivative, so the equations are invariant while the Lagrangian is not.

*Third, the duality is exact and not approximate.* The two eliminations are Gaussian and exact; the parent action is linear in $H$ and quadratic in $G$, so neither reduction requires an expansion. The equivalence is therefore stronger than the usual strong-weak dualities of the corpus, and this article states precisely what it buys.

**What is not new.** The parent action, the four reductions and the topologically massive Lagrangian are the source's, recomputed in the corpus's notation. What this article adds is the reading of the structure: one functional, two extrema, and the derivative count that distinguishes a topological mass from a plain one.

**Declared omissions.** Slot 8 is omitted: the second variation of a first-order action is the invertibility of its kernel, which is the constraint section's subject and not a separate one. Slot 11 is omitted: there is no truncation here, because both reductions are exact.

## Conventions

**The conventions are the corpus's, restated so that every sign below is checkable from this page.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_\eta^{2}=-e_t$; $\mathrm{Sc}$ and $\langle\cdot\rangle_\natural$ are the scalar part and the Minkowski square.

**The structure constants.** $\check c_{\nu\mu\lambda}$ is the corpus's chirality-odd array, antisymmetric as $\check c_{\nu\mu\lambda}-\check c_{\lambda\mu\nu}=-2i\,\varepsilon_{\nu\mu\lambda\rho}j_\rho$, and $\check\varepsilon_{\nu\mu\lambda}=\sum_\rho\varepsilon_{\nu\mu\lambda\rho}j_\rho$ is the three-dimensional Levi-Civita symbol of the slice, nonzero only when all three indices lie on it.

**The fields.** $G_\mu$ is a complex four-vector in the vector representation of the Dirac field; $H_\mu$ is the dual potential, a complex four-vector introduced as an auxiliary field; $B_\mu$ is the three-dimensional potential. The masses are $m$ and $a$, both real, and the combination $m-a$ is the one that survives the reductions.

**The derivative.** $\tilde\nabla_{\Phi,\mu}=\partial/\partial x_\mu$ in the neutral case, and $\tilde\nabla^{ea}_{\Phi,\mu}$ when the electromagnetic insertion $e$ and the second coupling $a$ are present. One $\epsilon_\mu$ accompanies each index in every sum, as in the corpus's sign rule.

## The Action in Element Form

**The parent action, and why it is written this way.** The integrand is linear in $H_\mu$ and quadratic in $G_\mu$, and the two fields enter symmetrically except for that half-shift:

$$
S_{GH}=\int d^4r\;\Bigl[\bigl(G_\nu+\tfrac12H_\nu\bigr)^{*}i\check c_{\nu\mu\lambda}\partial_\mu H_\lambda-\bigl(\partial_\mu H_\nu\bigr)^{*}i\check c_{\nu\mu\lambda}\bigl(G_\lambda+\tfrac12H_\lambda\bigr)+\tfrac{m-a}{2}\bigl(G\cdot G+G^{*}\cdot G^{*}\bigr)\Bigr].
$$

The shift $G+\tfrac12H$ is what makes the two eliminations give theories of the same mass; without it the reduced masses would differ by a factor. The structure is the standard first-order (parent) form: a field and its dual, with the auxiliary one entering linearly so that its equation is a constraint.

**Why linearity in one field is the whole device.** Because $S$ is linear in $H$, varying $H$ gives an equation with no derivatives of $H$ beyond the first, and that equation can be solved for $H$ in terms of $G$. Because $S$ is quadratic in $G$, varying $G$ gives a linear equation that can be solved for $G$ in terms of $H$. A functional with both properties has two exact eliminations, and that is why the duality is exact.

**The three-dimensional reduction.** Separating the scalar first and taking the duality between $(G_\mu;\xi)$ and $(B_\mu;\xi)$ with the same $\xi$,

$$
S_{G\xi B}=\int d^3r\;\Bigl[\tfrac12\bigl(G^{*}_\nu+\tfrac12B^{*}_\nu\bigr)i\check c_{\nu\mu\lambda}F_{\mu\lambda}+\tfrac{i}{2}\sum_\mu\epsilon_\mu\Bigl(G_\mu\frac{\partial\xi^{*}}{\partial x_\mu}-\xi^{*}\frac{\partial G_\mu}{\partial x_\mu}\Bigr)+\tfrac{m-a}{2}G\cdot G+\cdots\Bigr],
$$

and the elimination of $G$ leaves

$$
\boxed{\;\mathcal{L}_G=-\frac{1}{4m}\sum_{\mu,\lambda}\epsilon_\mu\epsilon_\lambda F_{\mu\lambda}F_{\mu\lambda}+\frac14\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda\,\check\varepsilon_{\nu\mu\lambda}B^{*}_\nu F_{\mu\lambda}+\text{(scalar sector)}\;}
$$

which is Maxwell plus a Chern–Simons mass. The normalization is the source's: the kinetic term carries $1/m$ and the topological term carries no $m$ at all, so rescaling $B$ or $F$ moves the mass from one term to the other without changing the physics.

**The derivative count, which is the point.** A plain mass term $m^2B_\mu B_\mu$ carries no derivative. The Chern–Simons term carries one derivative and one power of $m$, and that is the signature of a topological mass: the term is first order in momentum, so it contributes to the equation at the same order as the kinetic term rather than at a lower one. This is why the topologically massive field's dispersion relation is $p^2+m^2=0$ with a definite sign for one helicity and the opposite for the other, and it is the reason the theory has one degree of freedom and not three.

## The Variation: Two Eliminations, Two Theories

**Varying the auxiliary field.** $\delta S/\delta H_\mu=0$ gives the first relation of the introduction. Substituting it back leaves the Dirac Lagrangian in the vector representation,

$$
\mathcal{L}_D=\tfrac12\Bigl[\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda\Bigl(\bigl(\tilde\nabla_\mu G_\nu\bigr)^{*}i\check c_{\nu\mu\lambda}G_\lambda-G^{*}_\nu i\check c_{\nu\mu\lambda}\tilde\nabla_\mu G_\lambda\Bigr)+m\sum_\nu\epsilon_\nu\bigl(G_\nu G_\nu+G^{*}_\nu G^{*}_\nu\bigr)\Bigr],
$$

up to the total divergence the corpus's $Z_0$ removes. The mass couples $G$ to $G^{*}$, that is, the two chiral halves, and that coupling is why the s-vector is not two independent complex vectors.

**Varying the Dirac field.** $\delta S/\delta G_\nu=0$ gives the second relation, $(m-a)G_\lambda=\sum\epsilon\epsilon(\tilde\nabla H)^{*}i\check c$, and substituting it back leaves a second-order Lagrangian for $H_\mu$ with a kinetic term and a one-derivative term. At $a=e=0$ and after the rescaling $H_\mu\mapsto bH_\mu$ that restores the canonical normalization, it becomes the topologically massive form above.

**Why the two eliminations cannot both be applied.** Each elimination uses the other field's equation; applying both would impose both equations simultaneously, which is consistent only on shell. The correct reading is that the parent action defines one theory with two descriptions, and a description is chosen by which field is integrated out. The choice is not a gauge choice, because the two descriptions have different fields; it is a choice of which variable is fundamental.

**The check that would catch a sign.** The three-dimensional topological equation

$$
\sum_\nu\epsilon_\nu\frac{\partial F_{\nu\mu}}{\partial x_\nu}+\frac{m}{2}\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check\varepsilon_{\mu\nu\lambda}F^{*}_{\nu\lambda}=0
$$

must be invariant under the gauge transformation of $B_\mu$, and it is, because the variation of the Chern–Simons term is a total derivative. If the factor $\tfrac{m}{2}$ were $\tfrac{m}{4}$, the equation would not reduce to the Proca equation in the appropriate limit; the boxed coefficient is the check.

## The Reality of the Action

### The Pairing

**The pairing is the corpus's star bilinear, and it is what makes the two terms real.** Each term pairs a field with the conjugate of the other, so the integrand is a sum of a term and its conjugate, real by construction. The mass term pairs $G$ with $G^{*}$, which is the only way a mass can be written for a complex vector without breaking the reality of the action.

**Why the star is on the derivative in one term and on the field in the other.** The two terms of the parent differ by which factor carries the conjugate, and the difference is what makes the varied equations independent. If both terms carried the conjugate on the same factor, the variation would give one equation twice.

### The Type of the Coefficient

**One mass $m$ and one shift $a$, and the combination $m-a$ is what survives.** Both are real and have dimension of mass. The three-dimensional Maxwell term carries $1/m$ and the Chern–Simons term carries $1$, so $m$ is a scale in the denominator and the numerator at once — the sign that it is not a coupling in the usual sense.

**What the shift $a$ does.** The second coupling $a$ enters the derivative as a conjugation and shifts the effective mass to $m-a$. It is a parameter of the parent and not of either reduced theory, and its presence is what makes the parent's two eliminations give masses that agree. Setting $a=0$ recovers the plain case.

### The Selection Rule

**The selection rule is gauge invariance of the equations, and it is satisfied by a term that breaks the Lagrangian's invariance.** The Chern–Simons term's variation is a total derivative, so the action changes by a boundary term and the equations do not change. That is a weaker selection than exact invariance, and it is the reason a topological mass is possible at all: as an exact invariant the term does not exist in three dimensions.

### What Reality Does Not Buy

**Reality does not buy a local mass term, a positive-definite Hamiltonian, or uniqueness.** Three things the reality of the action does not supply:

- *No local gauge-invariant mass.* The Chern–Simons term is the only mass available, and it is not an invariant of the Lagrangian.
- *No positive-definite energy without a sign condition.* The Hamiltonian is positive for one sign of $m$ only, and the sign is a choice the action permits both ways.
- *No uniqueness of the reduction.* Which field is eliminated is a choice, and the two choices give different-looking theories.

## The Constraints the Action Imposes: One Degree of Freedom from Three Components

**The count.** In three dimensions a vector has three components. The gauge symmetry removes one and the Chern–Simons term makes the remaining two into one massive mode, so the count is one. A plain massive vector in three dimensions would also have two polarizations, but with both helicities at the same mass; the topological mass splits the sign, and the theory keeps one.

**Why the constraint survives the mass.** A plain mass term $m^2B_\mu B_\mu$ would make the temporal component propagate and would give a second degree of freedom; the Chern–Simons term does not, because it is first order and its equation is a constraint on the field strength rather than a second-order equation for the potential. The constraint's survival is the same fact as the derivative count.

**The invertibility of the kinetic operator.** The parent's kernel in $G$ is $(m-a)I$ plus derivative terms, invertible for $m\neq a$; the reduced kinetic operator's invertibility is the condition for the propagator to exist, and it fails at $m=0$, where the theory is pure Maxwell and the topological term has vanished.

## The Two Settings

**The four-dimensional setting.** The parent action is four-dimensional, $G_\mu$ and $H_\mu$ are four-vectors, and the mass $m$ couples the two chiral halves of the s-vector. The reduction gives the Dirac theory in the vector representation, and the mass is a plain Dirac mass.

**The three-dimensional setting.** The parent is three-dimensional, the duality is taken between the pairs $(G_\mu;\xi)$ and $(B_\mu;\xi)$, and the reduction gives Maxwell plus Chern–Simons with a scalar spectator. The mass is topological.

**Why the two settings differ in the mass's character and not in the method.** In four dimensions the antisymmetric symbol has four indices and the one-derivative term $H^{*}\check c\,\partial H$ reduces to the Dirac mass; in three the symbol has three, the one-derivative term survives as the Chern–Simons term, and the mass stays first order. The method is the same elimination; the dimension decides whether the mass is plain or topological.

**What the comparison shows.** The duality is a statement about the parent, not about the dimension. The same parent structure, read in four or in three dimensions, gives two theories whose masses differ in character, and that is the cleanest demonstration in the corpus that a mass's shape is a consequence of the term that carries it.

## The Structural Consequence: A Mass with One Derivative Is a Mass That Cannot Be Removed

**The statement.** The topological mass is fixed by the gauge structure and not by a parameter in the potential. It cannot be tuned to zero without the theory changing its degree-of-freedom count, and it cannot be given a sign without choosing an orientation.

**Why it is called topological.** The Chern–Simons term is the integral of a three-form built from the connection, and its variation is a boundary term; its value on a closed manifold is quantised. The mass it gives is therefore tied to the topology of the gauge bundle and not to a scalar's vacuum value.

**The consequence for the corpus's classification.** The family's other masses come from a scalar's expectation or from a Dirac bilinear; this one comes from a term with no metric. It is the third kind of mass in the corpus, and its existence is a statement about three dimensions that has no four-dimensional analogue in the family.

**What the structure does not give.** It does not give a four-dimensional topological mass; the Chern–Simons term exists only in odd dimensions. It does not explain why a theory would have one; it describes one that does.

## The Noether Currents: The Gauge Current and the Chern–Simons Current

**The gauge current.** The reduced action is invariant under $B_\mu\mapsto B_\mu+\partial_\mu\Lambda$ up to a boundary term, and the conserved current is the field strength's divergence, $\partial_\nu F_{\nu\mu}$, which vanishes on shell in the absence of sources. With a source the current is the source, as in the Maxwell article.

**The Chern–Simons current.** The topological term defines

$$
J_{\mathrm{CS},\mu}=\varepsilon_{\mu\nu\lambda\rho}F_{\nu\lambda}B_\rho ,
$$

whose divergence is $F\tilde F$; it is conserved identically in three dimensions because the term is a total derivative. The current is the three-dimensional analogue of the QCD Chern–Simons current, and its conservation is a Bianchi identity.

**Energy–momentum.** Translation invariance gives $T_{\mu\nu}$ with a contribution from each term, and the static energy is positive for one sign of $m$. The trace is nonzero because the Chern–Simons term is not conformally invariant, and that is the three-dimensional analogue of the mass term's trace in the vector articles.

**What there is not.** No central phase, no second gauge current, no topological charge of the winding kind. The sector's current content is one gauge current and one identically conserved topological current.

## Comparisons with Other Formulations

**Dirac versus topologically massive.** The two reduced theories are not the same theory in two notations: they have different fields, different dimensions and different masses. They are the same *parent* read two ways, and the comparison's content is that a single functional can have two physically distinct extrema.

**The Proca formulation.** The family's massive vector articles write a plain mass term and count three modes in four dimensions. The topologically massive theory writes a first-order mass and counts one mode in three. The two are not variants of one another; the difference in the derivative count is the difference between them, and this article's boxed Lagrangian displays it.

**The Stueckelberg formulation.** A Stueckelberg mass is invariant by a field redefinition; a topological mass is invariant only up to a boundary term. Both avoid the Proca obstruction, and they avoid it in opposite ways: one by adding a field, the other by weakening the invariance.

**What the comparison settles.** The corpus has three ways to give a vector a mass — a scalar's expectation, a Stueckelberg field, and a Chern–Simons term — and the derivative count separates them cleanly. That classification is the comparison's result.

## What the Principle Adds and What It Relabels

**Adds.**

- *One functional behind two theories.* The duality is visible as a single action with two eliminations, and that is stronger than a matching of equations.
- *The exactness of the equivalence.* Both eliminations are Gaussian and exact, and the action shows why: linearity in one field and quadraticity in the other.
- *The derivative count as the definition of "topological".* The property is readable from the action's terms and not from a name.

**Relabels.**

- *The "dual".* It is not a strong-weak duality; it is an exact change of variable in one functional.
- *The topological mass.* It is not a mass added with a special name; it is a mass carried by a one-derivative term.
- *The auxiliary field.* It is not a physical field; it is the variable whose elimination defines which theory one is describing.

**The distinction that matters.** The parent is exact and the descriptions are partial. Each reduced theory is the parent with one field solved for, and neither reduction is privileged except by which field one calls physical.

## Open Questions

**Is the parent action itself derivable from the algebra?** The action is the source's and is written in the algebra's structure constants; whether the parent form is forced by the algebra's chirality structure, or is one choice among several, is open.

**Does the duality extend to four-dimensional topological mass terms?** The Chern–Simons term exists only in odd dimensions, so the topological mass has no four-dimensional analogue in this construction. Whether another term plays the role is not known.

**What fixes $m$ and $a$?** Nothing in the action; they are parameters, and the reduced theories depend on $m-a$ alone.

## Summary

**The action.** A parent functional linear in the dual potential $H_\mu$ and quadratic in the s-vector $G_\mu$. Varying $H$ and eliminating it gives the Dirac theory in the vector representation; varying $G$ and eliminating it gives Maxwell plus Chern–Simons.

**The three findings.** The duality is exact because the parent is linear in one field and quadratic in the other. The topological mass is topological because its term has one derivative and no metric, so its variation is a boundary term. The reduced theory has one degree of freedom, and the count follows from the derivative structure.

**The boundary.** The parent's form is the source's; the corpus's contribution is the structure-constant writing and the derivative-count reading.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G_\mu$ | complex four-vector, the s-vector of the Dirac field |
| $H_\mu$ | dual potential, auxiliary field of the parent |
| $B_\mu$ | three-dimensional gauge potential |
| $\check c_{\nu\mu\lambda}$ | chirality-odd structure-constant array |
| $\check\varepsilon_{\nu\mu\lambda}$ | three-dimensional Levi-Civita of the slice |
| $m$, $a$ | mass and second coupling; $m-a$ survives |
| $F_{\mu\lambda}$ | field strength of $B_\mu$ |
| $J_{\mathrm{CS},\mu}$ | Chern–Simons current |

## Further Reading

- [Dual Equivalence of the Dirac and Topologically Massive Gauge Fields](dual-equivalence-of-the-dirac-and-topologically-massive-gauge-fields.html) — the parent: the four reductions, the three-dimensional form, the topological mass.
- [The Lagrangian and the Proca Equation](the-lagrangian-and-the-proca-equation.html) — the plain massive vector, for the derivative-count comparison.
- [The Lagrangian and the Stueckelberg Mechanism](the-lagrangian-and-the-stueckelberg-mechanism.html) — the other way to avoid the Proca obstruction.
- [The Lagrangian and the Dirac Equation](the-lagrangian-and-the-dirac-equation.html) — the Dirac theory whose vector representation is one of the two reductions.
- [Topological Charge, Self-Duality and the Bogomolny Bound](topological-charge-self-duality-and-the-bogomolny-bound-in-biquaternionic-form.html) — topological terms and their conservation identities.
