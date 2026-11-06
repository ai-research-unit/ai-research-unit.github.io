# __The Covariant Derivative and Gauge Connection in Biquaternionic Form__

## Introduction

The **gauge principle** article of the companion series localized the central phase symmetry of the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ and found that the price of locality is a connection and a new derivative. It established, and this article inherits unchanged, the transformation law of the connection,

$$
\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma,
$$

and the covariant derivative

$$
\tilde\nabla_{\mathrm{gco}} = \sum_\mu e_\mu \tilde\nabla_{\mathrm{gco},\mu} = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A}, \qquad \tilde\nabla_{\mathrm{gco},\mu} = \partial/\partial R_\mu + \frac{iϙ}{\hbar}A_\mu,
$$

together with the identification of the field strength with the curvature, $\tilde{F} = \mathrm{Vect}(\tilde{\nabla}^{\natural}\tilde{A})$. This article takes the connection $\tilde{A}$ and the covariant derivative $\tilde\nabla_{\mathrm{gco}}$ produced by that localization and studies them as objects in their own right. Nothing inherited from the gauge principle is rederived, renamed, or corrected here; the transformation law, the covariance, and the curvature identity are used as input.

**Notation, once.** The derivative letters are those of *Operator and Calculus Conventions*, §*The Gradient*: the biquaternionic gradient $\tilde\nabla$, its quaternion conjugate $\tilde\nabla^{\natural}$, the d'Alembertian $\Box$ the two compose, and the Laplacian $\Delta_Q$ in the three vector coordinates, read on the material sector as that section reads them. This article uses the four glyphs as the convention fixes them and adds no derivative of its own: every derivative below is one of them, or the covariant derivative $\tilde\nabla_{\mathrm{gco}}$ built on them and its quaternion conjugate $\tilde\nabla_{\mathrm{gco}}^{\natural}$. No other letter names a derivative.

The article develops the two objects in four directions that the gauge principle article did not pursue.

- **The derivative as an operator.** $\tilde\nabla_{\mathrm{gco}}$ is a first-order differential operator, not an element of $\mathbb{B}$. It is a derivation on the algebra of fields, and the connection is precisely the difference between $\tilde\nabla_{\mathrm{gco}}$ and $\tilde{\nabla}$: $[\tilde\nabla_{\mathrm{gco},\mu}, f] = \partial/\partial R_\mu f$ for a scalar function $f$.
- **The connection as an orbit.** Covariance does not merely hold for $\tilde\nabla_{\mathrm{gco}}$; it *determines* it. Requiring $\tilde\nabla_{\mathrm{gco},2}(\lambda\tilde{Ξ}_{\mathrm{sp}}) = \lambda \tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}}$ for a central phase $\lambda$ forces the transformation law $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$. The connection has no gauge-invariant local value — it can be gauged to zero at any one point — and only its curvature obstructs doing so on a neighbourhood.
- **The curvature as a commutator that closes on the algebra.** The commutator $[\tilde\nabla_{\mathrm{gco},\mu}, \tilde\nabla_{\mathrm{gco},\nu}]$ is multiplication by $\frac{iϙ}{\hbar}F_{\mu\nu}$; unlike $\tilde\nabla_{\mathrm{gco}}$ itself, it is an element of $\mathbb{B}$.
- **The covariant square.** With $\tilde\nabla_{\mathrm{gco}}^{\natural}$ the quaternion conjugate of $\tilde\nabla_{\mathrm{gco}}$, the exact operator identity splits into the covariant d'Alembertian in its scalar part and the curvature in its vector part:
$$
\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}} = \sum_{\mu\in\{t,x,y,z\}} \tilde\nabla_{\mathrm{gco},\mu}^{2} + \frac{iϙ}{\hbar}\tilde{F}
$$

The division between what is established and what is interpretation is kept explicit, as in the companion articles.

- **Established, and recomputed below.** The identities of the four bullets above; the flatness of pure-gauge connections; the reality condition that keeps $\tilde{A}$ in $\mathbb{B}_{\Phi}$; and the observation that the connection one-form $\sum_\mu A_\mu\,dx_\mu$ is a real quaternion.
- **Interpretation.** Reading $\tilde{A}$ as a connection on a bundle, the covariant derivative as parallel transport, and $\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}}$ as the biquaternion form of the identity "square of a Dirac operator equals Laplacian plus curvature" are geometric interpretations of algebraic content. They are labelled as interpretation wherever they occur.
- **Gaps, left visible.** The non-abelian extension, the reality and compactness conditions that would select a compact gauge algebra, and the covariant wave operator for a charged scalar are not settled here; each is stated as a gap where it arises and collected in the open questions.

## The Covariant Derivative and Its Components

In the abelian case the connection coefficients $A_\mu$ are complex scalars. Writing $\tilde{A} = \sum_\mu A_\mu e_\mu$, the covariant derivative is the first-order operator

$$
\tilde\nabla_{\mathrm{gco}} = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A}
  = \sum_{\mu\in\{t,x,y,z\}} e_\mu\left(\partial/\partial R_\mu + \frac{iϙ}{\hbar}A_\mu\right)
  =: \sum_{\mu\in\{t,x,y,z\}} e_\mu\, \tilde\nabla_{\mathrm{gco},\mu},
$$

where the coordinate is that of the material frame of *Frame and Metric Conventions*, $Q_t = i c r'_t$ and $Q_k = r_k$. Its action on a biquaternion-valued field $\tilde{Ξ}_{\mathrm{sp}}(\tilde{Q})$ is left multiplication by that operator,

$$
\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}} = \tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} + \frac{iϙ}{\hbar}\tilde{A}\tilde{Ξ}_{\mathrm{sp}},
\qquad
\tilde\nabla_{\mathrm{gco},\mu}\tilde{Ξ}_{\mathrm{sp}} = \partial/\partial R_\mu\,\tilde{Ξ}_{\mathrm{sp}} + \frac{iϙ}{\hbar}A_\mu\tilde{Ξ}_{\mathrm{sp}}.
$$

The two descriptions agree because $\sum_\mu e_\mu A_\mu = \tilde{A}$ and $\sum_\mu e_\mu\partial/\partial R_\mu = \tilde{\nabla}$: the component form of $\tilde\nabla_{\mathrm{gco}}$ is not an independent definition, it is the expansion of the same object in the quaternion basis.

Two points about the nature of $\tilde\nabla_{\mathrm{gco}}$ are worth stating before its algebra is used.

**$\tilde\nabla_{\mathrm{gco}}$ is an operator, not an algebra element.** The covariant derivative maps fields to fields; it carries the dimension of a derivative and does not belong to $\mathbb{B}$. Only its components $\tilde\nabla_{\mathrm{gco},\mu}$ are scalar operators, and even they are not elements of the algebra. The connection $\tilde{A}$, by contrast, is an element of $\mathbb{B}$ — indeed of $\mathbb{B}_{\Phi}$ — and it is the *coefficient* of the new term, not the derivative itself.

**The coefficients are central, so there is no ordering ambiguity.** In the abelian case each $A_\mu$ is a complex scalar and therefore commutes with every biquaternion and with the basis elements. Left and right multiplication by each coefficient $\frac{iϙ}{\hbar}A_\mu$ agree, and the derivation below never has to choose an order. This is the algebraic signature of the abelian gauge group: the phase lies in the centre, and the connection has central coefficients.

The following table collects the components and their meanings.

| Object | Expression | Role |
|---|---|---|
| Gradient | $\tilde{\nabla}$ | The ordinary derivative of *Operator and Calculus Conventions* |
| Connection | $\tilde{A} = \sum_\mu A_\mu e_\mu \in \mathbb{B}_{\Phi}$ | Compensating field |
| Covariant derivative | $\tilde\nabla_{\mathrm{gco}} = \sum_\mu e_\mu \tilde\nabla_{\mathrm{gco},\mu}$ | $\tilde\nabla_{\mathrm{gco},\mu} = \partial/\partial R_\mu + \frac{iϙ}{\hbar}A_\mu$ |
| Time component $\mu = t$ | $\tilde\nabla_{\mathrm{gco},t} = \partial/\partial R_t + \frac{iϙ}{\hbar}A_t = \partial/\partial R_t - \frac{ϙ a'_t}{\hbar}$ | $A_t = i\,a'_t$ |
| Space components $\mu = k$ | $\tilde\nabla_{\mathrm{gco},k} = \partial/\partial r_k + \frac{iϙ}{\hbar}A_k$ | $A_k$ real |

The line $\mu=t$ is the only place where $i^2=-1$ is used. The coupling contributes one imaginary unit and the complex time component $A_t=i\,a'_t$ contributes the other; they multiply to $-1$, and the potential term of the time component is the real number $-\frac{ϙ a'_t}{\hbar}$. The three spatial components keep their imaginary unit, because $A_k$ is real.

## The Covariant Derivative as a Derivation

The properties collected here are the ones that make $\tilde\nabla_{\mathrm{gco}}$ a covariant derivative rather than an arbitrary first-order operator. They are stated for the abelian case.

**1. Linearity over constants.** For a central constant $\alpha$,

$$
\tilde\nabla_{\mathrm{gco}}(\alpha\tilde{Ξ}_{\mathrm{sp}}) = \alpha\, \tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}}, \qquad \tilde\nabla_{\mathrm{gco}}(\tilde{Ξ}_{\mathrm{sp}}\alpha) = (\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}})\,\alpha,
$$

because constants pass through $\tilde{\nabla}$ and commute with $\tilde{A}$.

**2. The Leibniz rule.** For a complex scalar function $f$,

$$
\tilde\nabla_{\mathrm{gco}}(f\tilde{Ξ}_{\mathrm{sp}}) = f\,\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}} + \left(\tilde{\nabla} f\right)\tilde{Ξ}_{\mathrm{sp}}.
$$

This is the Leibniz rule of the gradient corrected by the connection: $\tilde{\nabla}(f\tilde{Ξ}_{\mathrm{sp}}) = f\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} + (\tilde{\nabla} f)\tilde{Ξ}_{\mathrm{sp}}$, while the connection term is $f\frac{iϙ}{\hbar}\tilde{A}\tilde{Ξ}_{\mathrm{sp}}$ by centrality of $f$. The mirror identity for right multiplication, $\tilde\nabla_{\mathrm{gco}}(\tilde{\tilde{Ξ}_{\mathrm{sp}}}f) = (\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}})f + \tilde{Ξ}_{\mathrm{sp}}(\tilde{\nabla} f)$, does **not** hold in this two-term form: $\tilde{\nabla}(\tilde{\tilde{Ξ}_{\mathrm{sp}}}f) = (\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}})f + \sum_\nu e_\nu\tilde{Ξ}_{\mathrm{sp}}\,\partial/\partial R_\nu f$, and $e_\nu\tilde{Ξ}_{\mathrm{sp}}\ne\tilde{\tilde{Ξ}_{\mathrm{sp}}}e_\nu$ in general. $\tilde\nabla_{\mathrm{gco}}$ is therefore a *left* derivation; the mirror rule holds for constant $f$, or with the mirror derivative that acts on the right. The derivation below uses the left rule only.

**3. The commutator with a function is the ordinary derivative.** From the Leibniz rule,

$$
[\tilde\nabla_{\mathrm{gco},\mu}, f] = \partial/\partial R_\mu f,
$$

as an operator identity: $[\tilde\nabla_{\mathrm{gco},\mu},f]\tilde{Ξ}_{\mathrm{sp}} = \tilde\nabla_{\mathrm{gco},\mu}(f\tilde{Ξ}_{\mathrm{sp}}) - f\tilde\nabla_{\mathrm{gco},\mu}\tilde{Ξ}_{\mathrm{sp}} = (\partial/\partial R_\mu f)\tilde{Ξ}_{\mathrm{sp}}$. Equivalently, the connection is exactly the difference between the covariant and the ordinary derivative,

$$
\tilde\nabla_{\mathrm{gco},\mu} - \partial/\partial R_\mu = \frac{iϙ}{\hbar}A_\mu,
$$

and this is the precise sense in which the connection "compensates" for the ordinary derivative's failure to be gauge covariant.

**4. $\tilde\nabla_{\mathrm{gco}}$ is not closed under multiplication, but its commutator is.** The composition $\tilde\nabla_{\mathrm{gco},\mu} \tilde\nabla_{\mathrm{gco},\nu}$ is a second-order operator and is not an algebra element. The *commutator* $[\tilde\nabla_{\mathrm{gco},\mu},\tilde\nabla_{\mathrm{gco},\nu}]$, on the other hand, is first order and in fact has no derivative at all: it is multiplication by an element of $\mathbb{B}$. That element is the curvature, treated in its own section below. This is the structural reason the gauge field strength is the commutator of covariant derivatives rather than any single $\tilde\nabla_{\mathrm{gco},\mu}$.

## Gauge Covariance and What It Forces

The gauge principle article proves the covariance of the construction (inherited here, not rederived): with $\lambda = \exp(iϙ\Gamma(\tilde{Q})/\hbar)$ a central phase and $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$, the covariant derivative built from $\tilde{A}_2$ satisfies

$$
\tilde\nabla_{\mathrm{gco},2}(\lambda\tilde{Ξ}_{\mathrm{sp}}) = \lambda\,\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}}
$$

for every field $\tilde{Ξ}_{\mathrm{sp}}$, so the equation $\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}} = 0$ holds in every gauge when it holds in one. For the present article the important point is the converse direction, which the gauge principle article did not state: **covariance determines $\tilde\nabla_{\mathrm{gco}}$; the connection is forced, not chosen.**

To see this, suppose only that the field transforms as $\tilde{Ξ}_{\mathrm{sp}} \mapsto \lambda\tilde{Ξ}_{\mathrm{sp}}$ and that a derivative of the form $\tilde\nabla_{\mathrm{gco},2} = \tilde{\nabla} + \Omega_2$ is required to be covariant, $\tilde\nabla_{\mathrm{gco},2}(\lambda\tilde{Ξ}_{\mathrm{sp}}) = \lambda \tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}}$ for all $\tilde{Ξ}_{\mathrm{sp}}$, where $\Omega_2$ denotes multiplication by an element of $\mathbb{B}$. Expanding the left-hand side with the Leibniz rule,

$$
\tilde{\nabla}(\lambda\tilde{Ξ}_{\mathrm{sp}}) + \Omega_2\lambda\tilde{Ξ}_{\mathrm{sp}}
= \lambda\,\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} + \left(\tilde{\nabla}\lambda\right)\tilde{Ξ}_{\mathrm{sp}} + \Omega_2\lambda\tilde{Ξ}_{\mathrm{sp}},
$$

and comparing with $\lambda(\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} + \Omega\tilde{Ξ}_{\mathrm{sp}})$ leaves $\Omega_2\lambda = \lambda\Omega - \tilde{\nabla}\lambda$, that is

$$
\boxed{\;\Omega_2 = \lambda\,\Omega\,\lambda^{-1} - \left(\tilde{\nabla}\lambda\right)\lambda^{-1}
= \Omega - \left(\tilde{\nabla}\lambda\right)\lambda^{-1}\;}.
$$

The second form needs the centrality of $\lambda$, which lets it pass through $\Omega$; without a central phase only the first form survives.

For the exponential phase this is, by the chain rule $\tilde{\nabla}\lambda = \frac{iϙ}{\hbar}(\tilde{\nabla}\Gamma)\lambda$,

$$
\Omega_2 = \Omega - \frac{iϙ}{\hbar}\tilde{\nabla}\Gamma,
$$

which, with $\Omega = \frac{iϙ}{\hbar}\tilde{A}$, is the inherited transformation law. The compensating field is therefore not an assumption added to the theory: once the phase is localized, the requirement of covariance leaves no freedom in the transformation of the connection. The specialization of the chain rule to the exponential was checked by finite differences at a point not used to motivate it, and the algebraic form $\Omega_2 = \lambda\Omega\lambda^{-1} - (\tilde{\nabla}\lambda)\lambda^{-1}$ was checked exactly on random central phases in a truncated ring.

The forcing is stated within the left-action convention that the gauge principle produces; with a right action the same argument gives the mirror derivative, and the mixed insertion is not covariant at all. The parent's massive equation is written with the left action,

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R} = m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = m\tilde{Ξ}_{\mathrm{sp},R} ,
$$

and the linear mass term passes the central phase through, so the left action is the natural one for the charged massive field and it is the form the minimal-coupling article states. The choice between the left and right actions for a general matter field is a choice of matter representation, raised as an open question by that article and left open here.

The centrality of $\lambda$ is what makes the transformation law *additive*. Left and right multiplication by $\lambda$ agree, so no conjugation appears and the gauge group is abelian. It is the centre of $\mathbb{B}$ that supplies the group, and the centre is one complex dimension; the gauge group is $\mathrm{U}(1)$.

The reality of the gauge function is inherited as well. A real $\Gamma$ keeps $\tilde{A}$ in the material sector: $\tilde{\nabla}\Gamma$ has an imaginary scalar coefficient and real vector coefficients, exactly the membership condition of $\mathbb{B}_{\Phi}$; a complex $\Gamma$ would move the connection out of it.

## The Connection as a Gauge Orbit

The transformation law makes the connection's status precise.

**The connection is not gauge invariant.** Its entire gauge orbit is the set $\{\tilde{A} - \tilde{\nabla}\Gamma\}$. The scalar part of $\tilde{\nabla}^{\natural}\tilde{A}$,

$$
S = \mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{A}\right) = \partial/\partial R_t\,A_t + \mathrm{div}\,\vec A,
$$

transforms as $S_2 = S - \Box\Gamma$, so $S$ is a pure-gauge quantity; the Lorenz gauge $S = 0$ is a choice, not a condition. This is the gauge scalar of the Maxwell article, inherited unchanged.

**Pure-gauge connections are flat.** If $\tilde{A} = \tilde{\nabla}\Gamma$ for a scalar function $\Gamma$, then

$$
\tilde{F} = \mathrm{Vect}\!\left(\tilde{\nabla}^{\natural}\tilde{\nabla}\Gamma\right) = 0,
$$

because $\tilde{\nabla}^{\natural}\tilde{\nabla}\Gamma = \Box\Gamma\, e_t$ is a pure scalar and has no vector part. A connection that is a gradient carries no curvature. This was checked for complex as well as real $\Gamma$.

**A single point can always be made connection-free.** Given any connection $\tilde{A}$ and any point $\tilde{Q}_0$, choose the real, affine gauge function

$$
\Gamma(\tilde{Q}) = -a\,r'_t + A_x(\tilde{Q}_0)\,r_x + A_y(\tilde{Q}_0)\,r_y + A_z(\tilde{Q}_0)\,r_z,
\qquad a = -ic\,A_t(\tilde{Q}_0) = \xi(\tilde{Q}_0) \in \mathbb{R},
$$

so that $\partial/\partial R_\mu\,\Gamma(\tilde{Q}_0) = A_\mu(\tilde{Q}_0)$ and hence $\tilde{A}_2(\tilde{Q}_0) = 0$. The connection therefore has no gauge-invariant value at a point; whatever invariant content it has must be built from derivatives.

**The curvature is the obstruction to doing this on a neighbourhood.** A connection with $\tilde{F} = 0$ satisfies $F_{\mu\nu} = \partial/\partial R_\mu A_\nu - \partial/\partial R_\nu A_\mu = 0$, and the Poincaré lemma applied to the one-form $\sum_\mu A_\mu\,dx_\mu$ then supplies a local $\Gamma$ with $\tilde{A} = \tilde{\nabla}\Gamma$. The step from a closed one-form to an exact one is the Poincaré lemma; it is *invoked* here, not recomputed. The conclusion is that $\tilde{F}$ measures exactly what cannot be removed by a gauge transformation.

**The connection one-form is a real quaternion.** One observation about the connection is worth recording. Pairing the connection with a coordinate displacement gives

$$
\sum_\mu A_\mu\,dx_\mu = A_t\,d(i c r'_t) + \sum_k A_k\,dr_k = -\xi\,dr'_t + \vec A\cdot d\vec r ,
\qquad
d\vec r = \vec e_x\,dr_x + \vec e_y\,dr_y + \vec e_z\,dr_z ,
$$

which is real. The time term is real because its two imaginary units cancel, $d(i c r'_t) = ic\,dr'_t$ and $A_t = i\,a'_t$ giving $-\xi\,dr'_t$; the spatial terms are real because $A_k$ and $dr_k$ are separately real. In the algebra this says $\sum_\mu A_\mu\,dx_\mu \in \mathbb{B}_{H}$, the real-quaternion subspace. Around a closed path the integral is gauge invariant, because $\sum_\mu A_\mu\,dx_\mu \mapsto \sum_\mu A_\mu\,dx_\mu - d\Gamma$ and $\oint d\Gamma = 0$. Reading the exponential of this integral as a **holonomy** is a geometric interpretation of the algebraic fact; whether the real-quaternion character of the one-form carries content beyond this bookkeeping is not established here and is recorded as an open question.

## The Curvature as the Commutator of Covariant Derivatives

The curvature is the part of the covariant derivative that survives antisymmetrization. In the abelian case the connection coefficients commute, and the general commutator formula collapses to the curl:

$$
[\tilde\nabla_{\mathrm{gco},\mu}, \tilde\nabla_{\mathrm{gco},\nu}] = \frac{iϙ}{\hbar}\left(\partial/\partial R_\mu A_\nu - \partial/\partial R_\nu A_\mu\right) = \frac{iϙ}{\hbar}F_{\mu\nu},
\qquad
F_{\mu\nu} = \partial/\partial R_\mu A_\nu - \partial/\partial R_\nu A_\mu .
$$

This is the gauge principle article's commutator identity, inherited here. Three consequences are developed in the present article.

**The commutator closes on the algebra.** Although $\tilde\nabla_{\mathrm{gco},\mu}$ is an operator and not an element of $\mathbb{B}$, its commutator with $\tilde\nabla_{\mathrm{gco},\nu}$ is multiplication by the biquaternion $\frac{iϙ}{\hbar}F_{\mu\nu}$ — a scalar multiple of a field. The failure of covariant derivatives to commute is thus an algebraic object, not a differential one, and it can be contracted with the basis to form the field-strength biquaternion.

**The contraction is the field strength.** Reading off the components of $\tilde{\nabla}^{\natural}\tilde{A}$ gives

$$
\tilde{F} = \mathrm{Vect}\!\left(\tilde{\nabla}^{\natural}\tilde{A}\right)
= \frac{1}{2}\sum_{\mu,\nu\in\{t,x,y,z\}} F_{\mu\nu}\,e_\mu^{\natural} e_\nu,
\qquad
\tilde{F} = \frac{\hbar}{2iϙ}\sum_{\mu,\nu\in\{t,x,y,z\}}[\tilde\nabla_{\mathrm{gco},\mu}, \tilde\nabla_{\mathrm{gco},\nu}]\,e_\mu^{\natural} e_\nu ,
$$

with $e_t^{\natural} = e_t$ and $e_\mu^{\natural} = -\vec e_\mu$. The first identity is purely algebraic in the derivatives and is the gauge principle article's curvature identity; the second is its restatement as a commutator of covariant derivatives.

**The curvature is gauge invariant and is not in the material sector.** Because $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$ and $\mathrm{Vect}(\tilde{\nabla}^{\natural}\tilde{\nabla}\Gamma) = 0$, $\tilde{F}$ is unchanged by a gauge transformation. It is nevertheless not an element of $\mathbb{B}_{\Phi}$: it has vanishing scalar part and a vector part that is neither purely real nor purely imaginary, as the Maxwell article records. The connection is a material-sector object; its curvature is not.

Because $\tilde{F}$ is built from $\tilde{A}$ by differentiation, the homogeneous Maxwell equations are identities rather than equations of motion — the Bianchi identity of the connection. The biquaternion form of that identity and the non-abelian completion of the curvature are the subjects of separate planned companions and are not claimed here. (In particular, the one-line equation $\tilde{\nabla}\tilde{F} = 0$ is *not* the Bianchi identity; it is the full source-free Maxwell system. This was checked and recorded in the gauge principle companion so that it is not written by mistake.)

## The Covariant Square and the Curvature Term

The commutator of two covariant derivatives is first order. The *square* of the covariant derivative is second order, and in the biquaternion algebra its scalar and vector parts separate cleanly.

Define the **quaternion conjugate** of the covariant derivative by conjugating the basis:

$$
\tilde\nabla_{\mathrm{gco}}^{\natural} := \sum_\mu e_\mu^{\natural} \tilde\nabla_{\mathrm{gco},\mu} = \tilde{\nabla}^{\natural} + \frac{iϙ}{\hbar}\tilde{A}^{\natural},
$$

the conjugation $\natural$ being that of *Product and Form Conventions*, applied to the basis elements, the central coefficients $\tilde\nabla_{\mathrm{gco},\mu}$ passing through untouched. Here $\tilde{A}^{\natural} \neq -\tilde{A}$ in general; quaternion conjugation is not charge conjugation, and $\tilde\nabla_{\mathrm{gco}}^{\natural}$ is the quaternion conjugate of the operator, not the operator for the opposite charge. With this definition the exact operator identity

$$
\boxed{\;\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}} = \sum_{\mu\in\{t,x,y,z\}} \tilde\nabla_{\mathrm{gco},\mu}^{2} + \frac{iϙ}{\hbar}\tilde{F}\;}
$$

holds, where $\tilde\nabla_{\mathrm{gco},\mu}^2$ means $\tilde\nabla_{\mathrm{gco},\mu} \tilde\nabla_{\mathrm{gco},\mu}$ and $\sum_\mu \tilde\nabla_{\mathrm{gco},\mu}^2 = \sum_\mu\left(\partial/\partial R_\mu + \frac{iϙ}{\hbar}A_\mu\right)^2$ is the **covariant d'Alembertian**. The identity was checked on random connections and random fields, on constant and on non-constant potentials, and reduces to $\tilde{\nabla}^{\natural}\tilde{\nabla} = \Box$ when $\tilde{A} = 0$.

The derivation is short. Expanding the product,

$$
\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}} = \sum_{\mu,\nu} e_\mu^{\natural} e_\nu\, \tilde\nabla_{\mathrm{gco},\mu} \tilde\nabla_{\mathrm{gco},\nu} .
$$

The diagonal terms give $e_t\sum_\mu \tilde\nabla_{\mathrm{gco},\mu}^2$, since $e_\mu^{\natural} e_\mu = e_t$ for every $\mu$. For each pair with $\mu\neq\nu$ the two ordered terms combine, because $\tilde\nabla_{\mathrm{gco},\mu} \tilde\nabla_{\mathrm{gco},\nu} = \tfrac12\{\tilde\nabla_{\mathrm{gco},\mu},\tilde\nabla_{\mathrm{gco},\nu}\}+\tfrac12[\tilde\nabla_{\mathrm{gco},\mu},\tilde\nabla_{\mathrm{gco},\nu}]$ while $\tilde\nabla_{\mathrm{gco},\nu} \tilde\nabla_{\mathrm{gco},\mu} = \tfrac12\{\tilde\nabla_{\mathrm{gco},\mu},\tilde\nabla_{\mathrm{gco},\nu}\}-\tfrac12[\tilde\nabla_{\mathrm{gco},\mu},\tilde\nabla_{\mathrm{gco},\nu}]$:

$$
e_\mu^{\natural} e_\nu\,\tilde\nabla_{\mathrm{gco},\mu} \tilde\nabla_{\mathrm{gco},\nu} + e_\nu^{\natural} e_\mu\,\tilde\nabla_{\mathrm{gco},\nu} \tilde\nabla_{\mathrm{gco},\mu}
= \left(e_\mu^{\natural} e_\nu+e_\nu^{\natural} e_\mu\right)\tfrac12\{\tilde\nabla_{\mathrm{gco},\mu},\tilde\nabla_{\mathrm{gco},\nu}\}
+ \left(e_\mu^{\natural} e_\nu-e_\nu^{\natural} e_\mu\right)\tfrac12[\tilde\nabla_{\mathrm{gco},\mu},\tilde\nabla_{\mathrm{gco},\nu}]
= e_\mu^{\natural} e_\nu\,[\tilde\nabla_{\mathrm{gco},\mu},\tilde\nabla_{\mathrm{gco},\nu}] .
$$

The first coefficient vanishes term by term and the second is $2e_\mu^{\natural} e_\nu$. Summing over the pairs with $\mu<\nu$ and using $[\tilde\nabla_{\mathrm{gco},\mu},\tilde\nabla_{\mathrm{gco},\nu}]=\frac{iϙ}{\hbar}F_{\mu\nu}$ leaves $\frac{iϙ}{\hbar}\sum_{\mu<\nu}F_{\mu\nu}e_\mu^{\natural} e_\nu$, which is $\frac{iϙ}{\hbar}\tilde{F}$ by the definition of $\tilde{F}$ above. The scalar and vector parts of the result are therefore

$$
\mathrm{Sc}\!\left(\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}}\right) = \sum_{\mu\in\{t,x,y,z\}} \tilde\nabla_{\mathrm{gco},\mu}^{2},
\qquad
\mathrm{Vect}\!\left(\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}}\right) = \frac{iϙ}{\hbar}\tilde{F}.
$$

The square of the covariant derivative contains the curvature in its vector part. Two consequences follow.

**The second-order consequence of the massless equation.** If $\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}} = 0$ then $\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}} = 0$: the field satisfies a covariant wave equation with a curvature term,

$$
\left(\sum_\mu \tilde\nabla_{\mathrm{gco},\mu}^{2}\right)\tilde{Ξ}_{\mathrm{sp}} + \frac{iϙ}{\hbar}\tilde{F}\tilde{Ξ}_{\mathrm{sp}} = 0 .
$$

The structural similarity to the identity that the square of a Dirac operator is a Laplacian plus a curvature term is an **interpretation** of this result, not a claim that the biquaternion operator is the standard Dirac operator.

**A gap for the charged scalar.** The gauge principle article's clean realization of the global symmetry was the complex scalar biquaternion field $\tilde{Ξ} = \xi\,e_t$ obeying the massive Klein–Gordon equation $(\Box - \lambda_m^{-2})\tilde{Ξ} = 0$; the free equation is examined in the Klein–Gordon article, which does not gauge it. Covariantizing the *scalar operator* gives $\left(\sum_\mu \tilde\nabla_{\mathrm{gco},\mu}^2 - \lambda_m^{-2}\right)\xi\,e_t = 0$, which is consistent. But $\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}}(\xi e_t) = \left(\sum_\mu \tilde\nabla_{\mathrm{gco},\mu}^2\xi\right)e_t + \frac{iϙ}{\hbar}\xi\,\tilde{F}$, and the second term is a pure vector whenever $\tilde{F} \neq 0$. A purely scalar field therefore cannot satisfy $\left(\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}} - \lambda_m^{-2}\right)\tilde{Ξ} = 0$ in a region of nonzero curvature; only the scalar projection $\mathrm{Sc}(\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}})$ acts on scalars, or the charged scalar must acquire vector components. Which of these the framework intends is **not settled here**. It is a genuine gap: the minimal coupling of a scalar is not the same statement as the minimal coupling of a biquaternion, and the difference is the curvature. Here $\lambda_m=\hbar/(mc)$ is the mass length.

### The Chiral Pair and Why the Mass Couples Two Fields

One equation carries the mass under these conventions, and it is the chiral pair.

**The chiral pair** on the algebra. Both members act by left multiplication, the second is the quaternion conjugate of the first, and the mass couples the $L$ part to the $R$ part:

$$
\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp},R} = m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = m\tilde{Ξ}_{\mathrm{sp},R} .
$$

Squaring its first member with the second gives the boxed identity on the $R$ part, $\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp},R} = m^2\tilde{Ξ}_{\mathrm{sp},R}$. The second member is not a new equation: it is the first written on the conjugate field, $\natural$ is what separates them, and both act from the left.

**Why the mass couples two fields.** A first-order equation on a single field does not close on a second-order equation for that field. Write $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}} = m\tilde{Ξ}_{\mathrm{sp}}$ and apply $\tilde\nabla^{\natural}$: the result is $\Box\tilde{Ξ}_{\mathrm{sp}} = m\,\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp}}$, an equation in two different objects, and nothing reduces it to $\Box\tilde{Ξ}_{\mathrm{sp}} = m^2\tilde{Ξ}_{\mathrm{sp}}$, because $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp}} = m\tilde{Ξ}_{\mathrm{sp}}$ is the second equation and not a consequence of the first. If both members were imposed on one field, their difference would give $2\sum_k\vec e_k\,\partial/\partial R_k\tilde{Ξ}_{\mathrm{sp}} = 0$, so the field would not vary in space and the remaining time equation would be exponential rather than oscillatory: no wave survives. Two fields close the system instead, and applying $\tilde\nabla_{\mathrm{gco}}^{\natural}$ to $\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp},R} = m\tilde{Ξ}_{\mathrm{sp},L}$ returns $\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp},R} = m\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = m^2\tilde{Ξ}_{\mathrm{sp},R}$, which is the boxed identity.

The square of the gradient, the operator left when the connection is switched off, is not scalar, and it is not $\Box$. On a scalar function it reads

$$
\tilde\nabla^2=\frac{\partial^2}{\partial R_t^2}-\Delta_Q+2\sum_k\vec e_k\,\frac{\partial^2}{\partial R_t\partial R_k},
$$

which is $\Box$ with the sign of $\Delta_Q$ reversed and a vector part added. The expression is derived here from the squares of the units, and it was checked with residual $0$ on random polynomial scalar functions. The Laplacian enters with opposite signs because the spatial legs of $\tilde\nabla$ square to $-e_t$ while $e_\mu^{\natural} e_\mu = e_t$ for every $\mu$, and the mixed derivatives leave a vector part wherever they do not vanish. Writing $\tilde\nabla^2 = \Box$ would therefore be wrong by $2\Delta_Q$ in the scalar part and by that vector part.

**The minimal coupling** replaces $\tilde\nabla$ by $\tilde\nabla_{\mathrm{gco}}$ and $\tilde\nabla^{\natural}$ by $\tilde\nabla_{\mathrm{gco}}^{\natural}$ in the pair, which is the coupled pair of *Gauge Covariance and What It Forces*. The replacement holds term by term because the coefficients $A_\mu$ are central and pass through the units.

## What the Algebra Supplies, Transcribes, and Only Interprets

The boundary can be drawn as in the companion articles.

**What it supplies.** The centre $\mathbb{B}_{C}$ supplies the abelian gauge group $\mathrm{U}(1)$ canonically. The algebra makes the transformation law forced rather than assumed, makes the connection a material-sector object, makes the commutator of covariant derivatives an element of the algebra, and makes the covariant square split into a wave operator and a curvature term without any extra structure. It also preserves the sector decomposition under a real gauge function.

**What it only transcribes.** The global-to-local argument itself, the form of minimal coupling, and the covariant derivative are the standard constructions, written in the algebra's notation. The algebra provides a home and makes the identities transparent; it does not supply a reason for a connection to exist, and it does not fix the coupling constant $ϙ$.

**What is interpretation.** The bundle picture — connection as parallel transport, curvature as infinitesimal holonomy — is a consistent interpretation of the algebraic content. The one-form $\sum_\mu A_\mu\,dx_\mu$ lies in the real-quaternion subspace and its loop integral is gauge invariant by the fundamental theorem of calculus ($\oint d\Gamma = 0$); the geometric interpretation of those two facts is interpretation, and the identity $\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}} = \sum_\mu \tilde\nabla_{\mathrm{gco},\mu}^2 + \frac{iϙ}{\hbar}\tilde{F}$ is what makes the interpretation precise.

## The Gauge Connection and the Gravitational Connection

The word "connection" is used in the framework for two different objects, and conflating them is an error worth naming.

The connection of this article is **one-sided**: $\tilde\nabla_{\mathrm{gco},\mu} = \partial/\partial R_\mu + \frac{iϙ}{\hbar}A_\mu$ acts by left multiplication, and it can be written this way only because the abelian connection is central, so left and right multiplication agree. The connection of the curved-spacetime article of the corpus is **two-sided**: a biquaternionic covariant derivative on the material sector must be written $\tilde\nabla_{\mathrm{gco},\mu}\tilde{Q} = \partial/\partial R_\mu\,\tilde{Q} + \vec\Gamma_\mu\tilde{Q} + \tilde{Q}\vec\Gamma_\mu^{*}$, because the Lorentz generators act on $\mathbb{B}_{\Phi}$ by the two-sided infinitesimal action $G\tilde{Q} + \tilde{Q}G^{*}$ and not by the commutator; the two differ precisely for the boosts. The gauge connection of this article is a $\mathrm{U}(1)$ connection of the centre; the gravitational connection lies in the six-dimensional traceless subspace of $\mathbb{B}$. They are distinct objects that happen to share a name, and no relation between them is asserted here.

The distinction has a consequence the corpus had not recorded, and an external source names it. For an internal gauge force, the abelian case of this article, the substitution $\partial/\partial R_\mu \to \tilde\nabla_{\mathrm{gco},\mu}$ gives the same physics whether it is applied to the action or to the Euler–Lagrange equations, because the connection is central: it multiplies from the side the derivative already multiplies from, and it passes through every unit. For the standard gravitational coupling in the vierbein formulation, the two procedures **do not commute**: the varied equation acquires an anticommutator term between the frame element and the Lorentz generator, which the substituted equation does not have. The difference is settled by one test, whether the generator commutes with the four units, and the test separates the two cases cleanly. The centre of $\mathbb{B}$ is the real span of $e_t$ and $ie_t$, so the six-dimensional traceless subspace, where the Lorentz generator lives, contains no central element at all; the traceless units themselves do not even commute with one another, $[\vec e_x,\vec e_y]=2\vec e_z$ and cyclically, whereas the central element commutes with everything,

$$
[\vec e_x,\vec e_y]=2\vec e_z\neq0,
\qquad
[ie_t,\tilde Q]=0\ \text{ for every } \tilde Q\in\mathbb{B}.
$$

J. Fredsted (arXiv:1906.12200v3 [physics.gen-ph], 2019) proves the mismatch and reads it as a tension with the equivalence principle; the construction is recorded, with its world-index repair, in *Curved Spacetime and the Biquaternion Framework*. It is the sharpest available answer to the question this section raises: the one-sided central connection of this article is exactly the case in which localization is unambiguous, and the two-sided gravitational connection is exactly the case in which it is not.

A second external source goes further and puts the two objects into one. J. Fredsted (arXiv:0811.1357v4 [math-ph], 2009) constructs a formalism on a biquaternionic basis $s_\mu \in \mathbb{B}_{\Phi}$ with the metric $g_{\mu\nu} = \langle s_\mu, s_\nu\rangle$ and a **single** connection $\omega_\mu \in \mathbb{C}\otimes\mathbb{H}$ subject only to $\mathrm{Sc}(\omega_\mu + \bar{\omega}_\mu^*) = 0$; the imaginary-scalar part of $\omega_\mu$ is a local $\mathrm{U}(1)$ and its vector part is the Lorentz connection, so the two connections of this section are two parts of one algebra-valued object. The corpus records the construction — it is the same frame route the curved-spacetime article builds, reached from the other end — but does not adopt it, and continues to assert no relation between its central $\mathrm{U}(1)$ connection and its traceless gravitational connection. What the external construction shows is that the two are not forbidden to be one; what the corpus lacks is any reason to identify them.

## Open Questions

1. **The covariant wave operator for a charged scalar.** Does the framework use $\mathrm{Sc}(\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}}) = \sum_\mu \tilde\nabla_{\mathrm{gco},\mu}^2$ as the covariant d'Alembertian for a scalar, or must a charged scalar be a general biquaternion with vector components induced by the curvature? The two interpretations differ by the term $\frac{iϙ}{\hbar}\tilde{F}\xi$, which is nonzero wherever the field strength is.

2. **The non-abelian extension.** The commutator of covariant derivatives acquires $[A_\mu,A_\nu]$ when the connection is $\mathbb{B}$-valued, and the algebra already contains the required non-commutativity. What is not derived is a reality and tracelessness condition that would select a compact gauge algebra; the commutator algebra of $\mathbb{B}$ is $\mathfrak{gl}(2,\mathbb{C})$, not compact. The reality conditions natural in the biquaternion framework, and which simple gauge algebras they admit, are left to the planned companions on non-abelian fields and Yang–Mills.

3. **The matter representation.** The covariant derivative acts by left multiplication, and in the abelian case left and right agree. For the charged massive field the parent's linear chiral pair is written with the left action, which makes the left action the natural one there. For a non-abelian connection the two differ, and the representation carried by the matter field must be specified; what fixes it for a general matter field is open, and the chiral-fermion article's treatment of the two values of the subscript and the minimal-coupling article's left/right analysis are the concrete settings in which the question is posed.

4. **Dynamical content of the covariant square.** The curvature term $\frac{iϙ}{\hbar}\tilde{F}$ in $\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}}$ is structurally the biquaternion analogue of the curvature term in the square of a Dirac operator. Does it carry observable content — a magnetic-moment coupling — or is it a rewriting of the commutator identity with no independent consequence?

5. **The one-form and the holonomy.** The connection one-form $\sum_\mu A_\mu\,dx_\mu$ is a real quaternion, the loop integral is gauge invariant, and the curvature measures its infinitesimal holonomy. Is the real-quaternion character content-bearing, or is it the $i c r'_t$ convention in disguise? No answer is offered here.

6. **Gauge fixing.** The canonical-quantization article establishes that the framework cannot fix the gauge. The present article does not supply a selection principle either; the gauge orbit of the connection is exactly as large as the local phases allow.

7. **Empirical contact.** As everywhere in the framework, the open question is whether any of this yields a prediction distinguishing it from standard gauge theory. The construction above is a reformulation; the question of empirical contact is untouched by it.

## Summary

The connection and the covariant derivative produced by localizing the central phase of the biquaternion algebra are studied here as objects in their own right. The covariant derivative is the first-order operator

$$
\tilde\nabla_{\mathrm{gco}} = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A} = \sum_{\mu\in\{t,x,y,z\}} e_\mu \tilde\nabla_{\mathrm{gco},\mu},
\qquad
\tilde\nabla_{\mathrm{gco},\mu} = \partial/\partial R_\mu + \frac{iϙ}{\hbar}A_\mu,
$$

with $\tilde{A} = \sum_\mu A_\mu e_\mu \in \mathbb{B}_{\Phi}$ the connection. It is not an element of the algebra; it is a derivation on fields, with Leibniz rule $\tilde\nabla_{\mathrm{gco}}(f\tilde{Ξ}_{\mathrm{sp}}) = f\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}} + (\tilde{\nabla} f)\tilde{Ξ}_{\mathrm{sp}}$ and commutator $[\tilde\nabla_{\mathrm{gco},\mu},f] = \partial/\partial R_\mu f$, so that the connection is exactly the difference $\tilde\nabla_{\mathrm{gco},\mu} - \partial/\partial R_\mu = \frac{iϙ}{\hbar}A_\mu$.

Covariance determines the connection rather than merely holding for it: the requirement $\tilde\nabla_{\mathrm{gco},2}(\lambda\tilde{Ξ}_{\mathrm{sp}}) = \lambda \tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}}$ forces $\Omega_2 = \lambda\Omega\lambda^{-1} - (\tilde{\nabla}\lambda)\lambda^{-1}$, which for $\lambda = \exp(iϙ\Gamma/\hbar)$ is the inherited law $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$. The connection is a gauge orbit, not a value: it can be gauged to zero at any single point, a gradient connection is flat, and the curvature $\tilde{F}$ is exactly the obstruction to removing it on a neighbourhood. The one-form $\sum_\mu A_\mu\,dx_\mu$ lies in the real-quaternion subspace and has a gauge-invariant loop integral.

The curvature is the commutator of covariant derivatives, $[\tilde\nabla_{\mathrm{gco},\mu},\tilde\nabla_{\mathrm{gco},\nu}] = \frac{iϙ}{\hbar}F_{\mu\nu}$, and contracts to the field strength $\tilde{F} = \frac{\hbar}{2iϙ}\sum_{\mu\nu}[\tilde\nabla_{\mathrm{gco},\mu},\tilde\nabla_{\mathrm{gco},\nu}]e_\mu^{\natural} e_\nu$. Unlike $\tilde\nabla_{\mathrm{gco},\mu}$, the commutator is an element of the algebra. The covariant square separates cleanly,

$$
\boxed{\;\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}} = \sum_{\mu\in\{t,x,y,z\}} \tilde\nabla_{\mathrm{gco},\mu}^{2} + \frac{iϙ}{\hbar}\tilde{F},
\qquad
\mathrm{Sc}(\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}}) = \sum_\mu \tilde\nabla_{\mathrm{gco},\mu}^2, \quad \mathrm{Vect}(\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}}) = \frac{iϙ}{\hbar}\tilde{F}\;},
$$

with the scalar part the covariant d'Alembertian and the vector part the curvature. Two gaps are left visible: the covariant wave operator for a charged scalar is ambiguous between the scalar projection and a bivector-valued field, and the non-abelian extension still needs a reality condition selecting a compact gauge algebra. The gauge connection of this article is one-sided and abelian; it is not the two-sided gravitational connection of the curved-spacetime article.

The identity is the square of the chiral pair $\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp},R} = m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = m\tilde{Ξ}_{\mathrm{sp},R}$, written on the algebra by left multiplication, the second member being the first on the conjugate field. It is not the square of a single field: the conjugate derivative applied to $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}} = m\tilde{Ξ}_{\mathrm{sp}}$ returns $\Box\tilde{Ξ}_{\mathrm{sp}} = m\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp}}$, a second-order equation in two objects rather than one, and $\tilde\nabla^2$ is not $\Box$ — its scalar part is $\partial^2/\partial R_t^2-\Delta_Q$ against the $\partial^2/\partial R_t^2+\Delta_Q$ of $\Box$, and its vector part does not vanish. That is why the mass couples two fields.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{B}_{\Phi}, \mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_{H}$ | Real-quaternion subspace |
| $\mathbb{B}_{C} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Centre of the algebra; source of the abelian gauge group |
| $\tilde{\nabla} = e_t\partial/\partial R_t + \sum_{k=x,y,z}\vec e_k\,\partial/\partial R_k$ | Biquaternionic gradient |
| $\tilde{\nabla}^{\natural} = e_t\partial/\partial R_t - \sum_{k=x,y,z}\vec e_k\,\partial/\partial R_k$ | Quaternion-conjugate gradient |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla}$ | d'Alembertian |
| $\tilde\nabla^2=\frac{\partial^2}{\partial R_t^2}-\Delta_Q+2\sum_k\vec e_k\frac{\partial^2}{\partial R_t\partial R_k}$ | Square of the gradient; not scalar, and not $\Box$ |
| $\Delta_Q=\sum_k\partial^2/\partial R_k^2$ | Laplacian in the three vector coordinates |
| $\tilde{A} = \sum_\mu A_\mu e_\mu = i\,a'_t\,e_t + \vec A$ | Connection / potential biquaternion, in $\mathbb{B}_{\Phi}$ |
| $\Gamma$ | Real scalar gauge function |
| $\lambda = \exp(iϙ\Gamma/\hbar)$ | Local central phase (abelian) |
| $ϙ$ | Coupling constant (charge), not fixed by the algebra |
| $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$ | Gauge transformation of the connection |
| $m$ | Mass of the parent's Dirac field |
| $\tilde\nabla_{\mathrm{gco}} = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A} = \sum_\mu e_\mu \tilde\nabla_{\mathrm{gco},\mu}$ | Covariant derivative |
| $\tilde\nabla_{\mathrm{gco},\mu} = \partial/\partial R_\mu + \frac{iϙ}{\hbar}A_\mu$ | Components; $\partial/\partial R_t = \partial/\partial(i c r'_t)$ |
| $\tilde\nabla_{\mathrm{gco}}^{\natural} = \tilde{\nabla}^{\natural} + \frac{iϙ}{\hbar}\tilde{A}^{\natural}$ | Quaternion conjugate of $\tilde\nabla_{\mathrm{gco}}$ |
| $\tilde{A}^{\natural}$ | Quaternion conjugate of the connection, by *Product and Form Conventions* |
| $[\tilde\nabla_{\mathrm{gco},\mu}, f] = \partial/\partial R_\mu f$ | Derivation property |
| $S = \mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$, $S_2 = S - \Box\Gamma$ | Gauge scalar; pure gauge |
| $\tilde{F} = \mathrm{Vect}(\tilde{\nabla}^{\natural}\tilde{A}) = \frac{1}{2}\sum_{\mu\nu}F_{\mu\nu}e_\mu^{\natural} e_\nu$ | Field strength = curvature, gauge invariant |
| $F_{\mu\nu} = \partial/\partial R_\mu A_\nu - \partial/\partial R_\nu A_\mu$ | Abelian curvature components |
| $[\tilde\nabla_{\mathrm{gco},\mu}, \tilde\nabla_{\mathrm{gco},\nu}] = \frac{iϙ}{\hbar}F_{\mu\nu}$ | Curvature as commutator |
| $\sum_\mu \tilde\nabla_{\mathrm{gco},\mu}^2 = \mathrm{Sc}(\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}})$ | Covariant d'Alembertian |
| $\tilde\nabla_{\mathrm{gco}}^{\natural} \tilde\nabla_{\mathrm{gco}} = \sum_\mu \tilde\nabla_{\mathrm{gco},\mu}^2 + \frac{iϙ}{\hbar}\tilde{F}$ | Covariant square identity |
| $e_t^{\natural} = e_t, e_\mu^{\natural} = -\vec e_\mu$ | Conjugate basis |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Trace reading of the plain form on the informational sector |

## Further Reading

- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html) — the origin of the connection, the transformation law, the covariance, and the curvature identity inherited here.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html) — the potential, the field strength, the gauge scalar $S$, and the Maxwell equation.
- [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html) — the gauge-invariant content of $\tilde{F}$, which this article uses but does not develop.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) — the massless field equation $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} = 0$ and the minimal-coupling question.
- [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html) — the coupled Dirac equation, the left/right matter-representation question, and the companion that names the covariant-derivative article.
- [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html) — the free scalar equation $(\Box - \lambda_m^{-2})\tilde{Ξ} = 0$ whose covariantization is the gap discussed here.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) — the covariant derivative read on the two values of the subscript, and the charge-operator representation.
- [Canonical Quantization of the Biquaternion Maxwell Field](canonical-quantization-of-the-biquaternion-maxwell-field.html) — the framework's inability to fix the gauge, which bounds the gauge orbit treated here.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) and [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html) — the sector decomposition, the four-vectors, and the trace formula.
- [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html) — the two-sided gravitational connection, distinct from the one-sided gauge connection of this article, and the record of the Lorentz-gauging / Euler–Lagrange ambiguity.
- J. Fredsted, "Obtaining consistent Lorentz gauging for a gravitationally coupled fermion," arXiv:1906.12200v3 [physics.gen-ph] (2019), for the external result recorded in *The Gauge Connection and the Gravitational Connection*: the non-commutativity of internal-gauge localization (which this article's abelian construction enjoys) with the Euler–Lagrange variation when the gauge group is the Lorentz group, and the world-index formalism in which they commute again. Cited as an external claim and not adopted.
- J. Fredsted, "Spinor fields without Lorentz frames in curved spacetime using complexified quaternions," arXiv:0811.1357v4 [math-ph] (2009), for the external construction, also recorded in *The Gauge Connection and the Gravitational Connection*, in which one algebra-valued connection carries both the local $\mathrm{U}(1)$ and the Lorentz connection; cited as evidence that the two connections of this section are not forbidden to be one, with no reason to identify them asserted here.
- [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html) — the multiplication rule, the conjugations, and the centre.
