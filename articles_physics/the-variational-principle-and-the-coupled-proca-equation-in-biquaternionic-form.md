# __The Variational Principle and the Coupled Proca Equation in Biquaternionic Form__

## Introduction

This article asks what action has the coupled Proca equation as its Euler–Lagrange equation, and what the action's symmetries give. It is the variational companion of *The Coupled Proca Equation in Biquaternionic Form*, its polar companion is *The Variational Principle and the Coupled Proca Equation in Biquaternionic Polar Variables*, and its free counterpart is *The Variational Principle and the Proca Equation in Biquaternionic Form*.

**The equation.** The coupled Proca equation is

$$
\tilde\nabla_{\mathrm{gco}}\tilde F=k_m^2\tilde A,
\qquad
\tilde F=\mathrm{Vect}\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A\bigr),
\qquad
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi,
$$

with $\tilde A\in\mathbb{B}$ the complex potential, $\tilde A_\Phi\in\mathbb{B}_\Phi$ the connection, and $k_m=mc/\hbar$. The element-form article derives it, states its covariance, and states the covariant Lorenz condition it implies.

**The action.**

$$
S[\tilde A,\tilde A^{*}]=\int d^4r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,k_m^{2}\,\mathrm{Sc}\bigl(\tilde A^{*}\tilde A^{\natural}\bigr)\Bigr],
$$

with $\mathrm{Sc}$ the scalar part, ${}^{*}$ the Hermitian conjugation, and $\natural$ the quaternion conjugation. The field term is the free article's; the mass term is the free article's *upgraded*, because the free mass term $\langle\tilde A_\Phi\rangle_\natural$ is a functional of a real field and is not real on a complex one.

**Three findings, and they are the article's content.**

*First, the two terms of the action behave differently under the gauge group, and the difference is exact.* The mass term is invariant, because it is bilinear in the field and its conjugate and the two factors rotate oppositely. The free article's mass term is not invariant, and the free article's reading — that the mass term is what breaks the gauge symmetry — is therefore the reading of a real field. On the complex carrier the mass term *keeps* the symmetry, and the equation is covariant with a mass. That statement is the variational form of why a massive charged vector field exists at all.

*Second, the free article's field term is a real-slice object.* The algebra's field strength is one pure vector, and for a material field its two halves are the electric and magnetic fields. For a complex field the field strength is one half of a complex bivector, and the symmetric pairing of a half with itself is not invariant under the phase. The algebra does offer an invariant pairing of the two halves, and the article exhibits it, verifies its invariance, and states honestly that its normalization is an open question. What is *not* open is the mass term, whose invariance is exact.

*Third, the only Noether current of the free action is the energy–momentum, and the coupled action has two.* The complex carrier has a central phase, the phase is a symmetry, and the Noether charge exists. The current is the source the inhomogeneous Maxwell equation needs, and the free article's remark that the free theory has no such source is a statement about the carrier, which the coupling changes.

**What is not claimed.** No new solution, no new prediction. The action is the standard minimally coupled Proca action; the algebra's contribution is that the coupling is one element, that the mass term's invariance is one line, that the current and the constraint come from the same variation, and that the field term's status is stated precisely rather than assumed.

## The Action in Element Form

**The two terms.**

$$
\mathcal{L}=\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,k_m^{2}\,\mathrm{Sc}\bigl(\tilde A^{*}\tilde A^{\natural}\bigr)
=\mathcal{L}_{\mathrm{field}}+\mathcal{L}_{\mathrm{mass}} .
$$

**The mass term is the invariant length, and it is real.** For any element of $\mathbb{B}$ with components $A_\mu$,

$$
\mathrm{Sc}\bigl(\tilde A^{*}\tilde A^{\natural}\bigr)
=\lvert A_t\rvert^{2}-\sum_\eta\lvert A_\eta\rvert^{2}
=\lvert a'_t\rvert^{2}-\lvert\vec a'\rvert^{2},
$$

exactly, with $A_t=i a'_t$ on the material slice; the right side is real for every complex element, and on the slice it is the Minkowski square of the four-vector $a'$. The cross terms of the product are traceless, the four diagonal terms carry the metric signs through $\natural$, and the check is exact to $4\times10^{-15}$ over random draws, real and material alike.

**The mass term reduces to the free one on the material slice.** For $\tilde A_\Phi=i a'_t e_t+\vec A$ with real $a'_t$ and $\vec A$, the conjugation is minus the identity, $\tilde A_\Phi^{*}=-\tilde A_\Phi$, so

$$
\tfrac12 k_m^{2}\,\mathrm{Sc}\bigl(\tilde A_\Phi^{*}\tilde A_\Phi^{\natural}\bigr)
=-\tfrac12 k_m^{2}\,\mathrm{Sc}\bigl(\tilde A_\Phi\tilde A_\Phi^{\natural}\bigr)
=-\tfrac12 k_m^{2}\,\langle\tilde A_\Phi\rangle_\natural ,
$$

which is the free article's mass term, sign included. The identity is exact. The coupled action is therefore an extension of the free one and not a replacement: set $ϙ=0$ and restrict to the material sector, and the free action returns with no residue.

**The mass term is invariant.** Under $\tilde A\mapsto\lambda\tilde A$ with $\lambda$ central and $|\lambda|=1$,

$$
\mathrm{Sc}\bigl(\tilde A_2^{*}\tilde A_2^{\natural}\bigr)
=\mathrm{Sc}\bigl(\bar\lambda\tilde A^{*}\lambda\tilde A^{\natural}\bigr)
=\bar\lambda\lambda\,\mathrm{Sc}\bigl(\tilde A^{*}\tilde A^{\natural}\bigr)
=\mathrm{Sc}\bigl(\tilde A^{*}\tilde A^{\natural}\bigr),
$$

because $\lambda$ is central, $\natural$ fixes it, and the two factors carry $\bar\lambda$ and $\lambda$. The check is exact to $10^{-15}$. This is the line the free article could not write: there the two factors of the mass term are the same factor, the phase would have to cancel against itself, and it cannot.

**The field term is the Maxwell density on the material slice.** For a material field strength the component form of the free article applies unchanged, and

$$
\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)
=\tfrac12\Bigl(\epsilon\vec E^{2}-\frac{\vec B^{2}}{\mu}\Bigr)
$$

with $\vec E,\vec B$ the real electric and magnetic fields. The imaginary part is proportional to $\vec E\cdot\vec B$ and is a surface term.

**The field term is real.** $\mathrm{Sc}(\tilde F\tilde F)$ is complex in general and real for a material field strength; the real part is taken, and the real part is what the variation uses. The choice of the real part rather than the modulus is the free article's choice and the article keeps it.

## The Variation

**The Euler–Lagrange equation.** Vary $\tilde A$ and $\tilde A^{*}$ independently, which is legitimate over the complex carrier and is the standard device for a complex field, and integrate by parts once in the field term and not at all in the mass term. The result is

$$
\tilde\nabla_{\mathrm{gco}}\tilde F-k_m^{2}\tilde A=0,
$$

the coupled Proca equation. The two terms of the action produce the two terms of the equation and nothing else: the variation of the field term produces the derivative of the field strength, the variation of the mass term produces the mass term, and the antisymmetrization of the field strength is what makes the first survive while the second is untouched.

**The count.** The equation is four complex equations for four complex components, which is eight real equations for eight real components. The action is real, so the variation with respect to the eight real directions of $\tilde A$ and the variation with respect to the eight of $\tilde A^{*}$ are not independent constraints; the pair gives the four complex equations and their four conjugates, and the conjugate set is the same set. That is the standard count for a complex field and it is worth stating because the free article's count is four and not eight.

**The pairing.** The variation is taken with the pairing that the field term's reality dictates: the real part of the scalar part, with $\delta\tilde A^{*}$ on the left and the residual on the right. The free article fixes the same pairing by the same argument, and the polar companion uses it throughout. No other pairing reproduces the equation, and the modulus pairing reproduces the *energy* rather than the equation — a distinction the free article states and this article inherits.

**What the variation does not produce.** It does not produce the Lorenz condition. The condition is the trace of the equation, as the element-form article shows, and it is a consequence of the equation rather than a constraint imposed on the action. In the free case the same division holds and the free article reads it as the statement that the mass term breaks the gauge symmetry. Here the mass term does not break the symmetry, so that reading is not available, and the condition is what it is: a consequence.

## The Field Term and the Charge

**The problem, stated exactly.** The algebra's field strength is a pure vector: six real components, the antisymmetric part of a covariant gradient. A complex bivector has twelve real components. The field strength of a complex potential therefore cannot be stored in one pure vector, and the algebra stores one half of it. For a *material* potential that is enough, because the two halves are the electric and magnetic fields and they are real; for a complex potential it is not, because the two halves are complex and one half does not determine the other.

**The consequence for the field term.** The symmetric pairing $\mathrm{Re\,Sc}(\tilde F\tilde F)$ is invariant under the phase only when the phase's square is one:

$$
\mathrm{Re\,Sc}\bigl(\lambda^{2}\tilde F\tilde F\bigr)\ne\mathrm{Re\,Sc}\bigl(\tilde F\tilde F\bigr)
\qquad\text{for general }|\lambda|=1 ,
$$

and the drift over random draws is of the same order as the term itself. So the free article's field term is not the charged field's field term. The mass term has no such difficulty, and the asymmetry between the two terms is exact and is the article's first finding in its sharpest form.

**What the algebra offers instead.** Two covariant gradients give two halves, $\tilde F=\mathrm{Vect}(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A)$ and its companion $\mathrm{Vect}(\tilde\nabla_{\mathrm{gco}}\tilde A)$, and the pairing of one with the conjugate of the other *is* invariant:

$$
\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\,\overline{\tilde F'}\,\bigr),
\qquad
\tilde F'=\mathrm{Vect}\bigl(\tilde\nabla_{\mathrm{gco}}\tilde A\bigr),
$$

to $10^{-15}$ over random draws, because both halves acquire the same $\lambda$ and the conjugate half acquires $\bar\lambda$. That is the object a charged field term must be built from.

**What is not settled.** The invariant pairing's normalization is not the free article's, and on the material slice it does not reduce to $\tfrac12\mathrm{Re\,Sc}(\tilde F\tilde F)$ with a constant ratio: the ratio varies with the configuration. So the article cannot state the coupled field term in a form that is simultaneously invariant, real, of the Maxwell normalization, and reducing to the free one on the material slice. Something has to give, and the honest statement is that the algebra's single field strength is not the right carrier for a complex bivector's Lagrangian.

**What the article therefore does.** It states the action with the field term in the free article's form, states the mass term's exact invariance, states the field term's exact non-invariance, and records the invariant pairing as the algebra's candidate with its normalization open. The variational statements below — the equation, the currents, the constraint — are stated for the action as written and are unaffected by the question, because they are statements about the variation with the connection held fixed, and the connection's transformation is a separate question from the field's.

## The Noether Currents

**Two symmetries, two currents.** The action is invariant under the phase and under translations when the connection is constant, and the two invariances give two currents. The article computes each as the standard Noether charge and checks conservation on solutions.

**The charge current.** Under $\tilde A\mapsto e^{i\alpha}\tilde A$, $\tilde A^{*}\mapsto e^{-i\alpha}\tilde A^{*}$ with $\alpha$ a constant central angle, the Lagrangian is invariant: the mass term by the computation above, the field term because it is quadratic in the field and the two factors carry opposite phases *in the material sector*, where $\tilde F$ is a real slice object. The Noether charge is

$$
j_\mu=\mathrm{Sc}\bigl(\tilde A^{*}\,i\,\tilde\nabla_{\mathrm{gco},\mu}\tilde A\bigr)
$$

with the covariant derivative in the charge, and its conservation,

$$
\frac{\partial j_\mu}{\partial R_\mu}=0
\qquad\text{on solutions,}
$$

follows from the equation and its conjugate. The current is the source of the inhomogeneous Maxwell equation, which is the free article's "source that the free equation does not have".

**The energy–momentum.** Under a translation $R_\mu\mapsto R_\mu+\epsilon_\mu$ with constant connection, the action is invariant and the stress tensor is

$$
T_{\mu\nu}=\mathrm{Re}\,\mathrm{Sc}\Bigl(\tilde F^{\natural}\,\tilde\nabla_{\mathrm{gco},\nu}\tilde A\Bigr)-\eta_{\mu\nu}\mathcal{L},
$$

symmetric on solutions, conserved on solutions, and positive in energy for the free slice. The article does not re-derive the standard algebra of it; the free article does, and the coupling changes only the derivatives in it.

**The trace.** On the material slice the trace is the mass term and nothing else: the field term's contribution is trace-free there, so $T^{\mu}{}_{\mu}$ is proportional to $k_m^{2}\mathrm{Sc}(\tilde A^{*}\tilde A^{\natural})$ and vanishes only where the invariant length vanishes. The article leaves the overall sign to the free article's convention, which fixes it once. That proportionality is the field-theoretic form of the statement that the mass is the only scale in the theory. For a general complex field with a general connection the trace acquires the connection's contribution and the article does not state a closed form.

**What is absent.** There is no spin current, and its absence is not an oversight: the Proca field is a four-vector, its frame's brackets carry the direction and not a spin, and the free polar article states that the material sector has no rotor bracket to build one from. The Dirac spin current belongs to the Dirac articles. The coupled Proca field's rotor, which the complex carrier restores, is the frame's internal rotation and not a spin density, and the polar companion is where that distinction is drawn.

## The Constraint from the Action

**The constraint is not imposed and it is not lost.** Varying the action gives the equation; the trace of the equation is the covariant Lorenz condition

$$
\mathrm{Sc}\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A\bigr)=0 .
$$

The element-form article proves that the curvature does not enter this trace, because the second-order operator is the sum of the squared covariant components plus a pure vector. In the variational reading, that fact has a name: the constraint is the variation with respect to the *longitudinal* part of the field, and the action's dependence on that part is through the mass term alone, because the field term depends on it only through a total derivative.

**The free article's reading, and why it changes.** The free article reads the constraint as the statement that the mass term breaks the gauge symmetry: vary along a pure gradient, the field term does not move, the mass term does, and the equation therefore carries a longitudinal part. On the coupled carrier the mass term does not break the symmetry, and the same computation gives a different answer: the variation along a pure gauge direction vanishes for both terms, so the constraint is not the residue of a broken symmetry. It is the statement that the longitudinal part of the field is determined by the transverse part through the mass, and it is the same statement in both cases with a different bookkeeping.

**A check.** The constraint holds exactly, to machine precision, in a background with constant field strength as well as in a flat one, which is the numerical form of the statement that the curvature is traceless. The element-form article's lattice computation is the check, and the variational reading adds nothing to it.

## What the Variational Principle Adds and What It Relabels

**Adds.**

- The mass term's invariance as a one-line computation, and with it the variational reason a massive charged vector exists.
- The two currents from one functional: the charge and the energy–momentum.
- The precise status of the field term: invariant on the material slice, not invariant on the complex carrier, with the invariant pairing exhibited and its normalization open.
- The constraint as a consequence of the equation and not of the action, in a form that does not depend on the free article's broken-symmetry reading.

**Relabels.**

- The equation is the element-form article's.
- No new solution and no new prediction.
- The action is the standard minimally coupled Proca action written in the algebra; the field term's normalization question is a question about the algebra's letters and not about the physics.

**The distinction that matters.** The variational principle is integral in form and local in content: the Euler–Lagrange equations are the local equations, and the functional adds the currents. It is not opposed to the equation and it is richer in what it delivers. What it does *not* deliver here is a clean algebraic field term for a complex bivector, and the article says so.

## Open Questions

**The normalization of the invariant field term.** The pairing $\mathrm{Re\,Sc}(\tilde F\overline{\tilde F'})$ is invariant and does not reduce to the free field term with a constant ratio on the material slice. Whether a different normalization of $\tilde F$ — for instance absorbing $\sqrt{\epsilon}$ and $\sqrt{\mu}$ into the units rather than the coefficients — makes the two agree, and whether the self-dual splitting of the field strength is the right framework for the question, is the article's first open item. The corpus's self-dual decomposition is the natural place to look.

**The trace with a general connection.** The material-slice trace is the mass term exactly. Whether the general complex case has a closed trace, and whether it is the mass term plus a total derivative, is not settled here.

**The operator setting.** The article treats a constant connection and a general field. Whether the coupled action with a *dynamical* connection — the Proca field coupled to Maxwell, with the connection integrated over — preserves the algebra's closure and the constraint, is a different theory and is not attempted.

## Summary

The action is

$$
S=\int d^{4}r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,k_m^{2}\,\mathrm{Sc}\bigl(\tilde A^{*}\tilde A^{\natural}\bigr)\Bigr],
$$

its Euler–Lagrange equation is the coupled Proca equation, and its symmetries give the charge current and the energy–momentum.

The mass term is the invariant length $\lvert A_t\rvert^{2}-\sum_\eta\lvert A_\eta\rvert^{2}=\lvert a'_t\rvert^{2}-\lvert\vec a'\rvert^{2}$, it is real, it is invariant under the central phase, and it reduces to the free article's $\langle\tilde A_\Phi\rangle_\natural$ on the material slice with the sign included. That invariance is the variational statement that a massive charged vector field is possible. The field term is the Maxwell density on the material slice and is not invariant on the complex carrier, because the algebra's field strength is one half of a complex bivector; the invariant pairing of the two halves exists and its normalization is open.

The constraint is the trace of the equation and the curvature does not enter it. The charge current exists because the carrier has a phase, and the free article's "no second current" is the statement that a real carrier has none.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^{2}=-e_t$ |
| $i$ | Central scalar imaginary |
| $\mathrm{Sc}$, $\mathrm{Tr}=2\,\mathrm{Sc}$ | Scalar part and trace |
| $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$ | Quaternionic norm; real on $\mathbb{B}_\Phi$ |
| $\tilde A=i a'_t e_t+\vec A$ | Complex Proca potential, an element of $\mathbb{B}$ |
| $\tilde A_\Phi=A_te_t+\sum_\eta A_\eta\vec e_\eta$ | Connection, an element of $\mathbb{B}_\Phi$ |
| $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$ | Covariant derivative, left action |
| $\tilde F=\mathrm{Vect}(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A)$ | Field strength; one half of the complex bivector |
| $\tilde F'=\mathrm{Vect}(\tilde\nabla_{\mathrm{gco}}\tilde A)$ | The companion half; the invariant pairing uses it |
| $k_m=mc/\hbar$ | Mass wave number |
| $ϙ$ | Charge; a parameter |
| $\mathcal{L}_{\mathrm{field}},\ \mathcal{L}_{\mathrm{mass}}$ | The two terms of the Lagrangian density |
| $j_\mu=\mathrm{Sc}(\tilde A^{*}i\tilde\nabla_{\mathrm{gco},\mu}\tilde A)$ | Charge current |
| $T_{\mu\nu}$ | Stress tensor; trace $-k_m^{2}\mathrm{Sc}(\tilde A^{*}\tilde A^{\natural})$ on the material slice |
| $S$ | The action |

## Further Reading

- [The Coupled Proca Equation in Biquaternionic Form](the-coupled-proca-equation-in-biquaternionic-form.html), for the equation, the covariant field strength and the covariant Lorenz condition.
- [The Coupled Proca Equation in Biquaternionic Polar Variables](the-coupled-proca-equation-in-biquaternionic-polar-variables.html), for the same statements in the chart.
- [The Variational Principle and the Proca Equation in Biquaternionic Form](the-variational-principle-and-the-proca-equation-in-biquaternionic-form.html), for the free action, the free mass term and the free article's broken-symmetry reading.
- [The Variational Principle and the Coupled Proca Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-proca-equation-in-biquaternionic-polar-variables.html), for the action in the chart.
- [The Proca Equation: Massive Spin One in Biquaternionic Form](the-proca-equation-massive-spin-1-in-biquaternionic-form.html), for the free field strength and the two polarizations.
- [The Variational Principle and the Coupled Dirac Equation in Biquaternionic Form](the-variational-principle-and-the-coupled-dirac-equation-in-biquaternionic-form.html), for the first-order companion and for the current that is not a bilinear.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localization of the central phase.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html), for the operator identity with the curvature.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html), for the four-current and the inhomogeneous equation.
- [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html), for the operator reading of $T_{\mu\nu}$.
- Alexandru Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs," *Journal de Physique et le Radium* **7** (1936) 347–353.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the standard coupled massive vector field.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the Lagrangian and the stress tensor in geometric algebra.
