# __The Covariant Derivative and Connection in Biquaternionic Form__

## Introduction

The **minimal coupling** article of the companion series localized the central phase symmetry of the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ and found that the price of locality is a connection and a new derivative. It established, and this article inherits unchanged, the transformation law of the connection,

$$
\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi} - \tilde\nabla_\Phi\Gamma,
$$

and the covariant derivative

$$
\tilde\nabla_{\mathrm{gco},\Phi} = \sum_{\imath}  e_{\imath} \tilde\nabla_{\mathrm{gco},\Phi,\imath} = \tilde\nabla_\Phi +i\kappa\tilde{A}_{\Phi}, \qquad \tilde\nabla_{\mathrm{gco},\Phi,\imath} = \partial/\partial R_{\imath} +i\kappa A_{\imath},
$$

together with the identification of the field strength with the curvature, $\tilde{F} = \mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi})$. This article takes the connection $\tilde{A}_{\Phi}$ and the covariant derivative $\tilde\nabla_{\mathrm{gco},\Phi}$ produced by that localization and studies them as objects in their own right. Nothing inherited from the minimal coupling is rederived, renamed, or corrected here; the transformation law, the covariance, and the curvature identity are used as input.

**Notation, once.** The derivative letters are those of *Operator and Calculus Conventions*, §*The Gradient*: the biquaternionic gradient $\tilde\nabla_\Phi$, its quaternion conjugate $(\tilde\nabla_\Phi)^{\natural}$, the d'Alembertian $\Box_\Phi$ the two compose, and the Laplacian $\Delta_\Phi$ in the three vector coordinates, read on the material sector as that section reads them. This article uses the four glyphs as the convention fixes them and adds no derivative of its own: every derivative below is one of them, or the covariant derivative $\tilde\nabla_{\mathrm{gco},\Phi}$ built on them and its quaternion conjugate $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}$. No other letter names a derivative. The coupling is $\kappa$, real, so the covariant derivative reads $\tilde\nabla_\Phi+i\kappa\tilde A_{\Phi}$; the relation of $\kappa$ to a charge is fixed where the action quantum is declared, not here.

The article develops the two objects in four directions that the minimal coupling article did not pursue.

- **The derivative as an operator.** $\tilde\nabla_{\mathrm{gco},\Phi}$ is a first-order differential operator, not an element of $\mathbb{B}$. It is a derivation on the algebra of fields, and the connection is precisely the difference between $\tilde\nabla_{\mathrm{gco},\Phi}$ and $\tilde\nabla_\Phi$: $[\tilde\nabla_{\mathrm{gco},\Phi,\imath}, f] = \partial/\partial R_{\imath} f$ for a scalar function $f$.
- **The connection as an orbit.** Covariance does not merely hold for $\tilde\nabla_{\mathrm{gco},\Phi}$; it *determines* it. Requiring $\tilde\nabla_{\mathrm{gco},\Phi,2}(\digamma_{\mathrm{cph}}\tilde{Ξ}) = \digamma_{\mathrm{cph}} \tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ}$ for a central phase $\digamma_{\mathrm{cph}}$ forces the transformation law $\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi} - \tilde\nabla_\Phi\Gamma$. The connection has no invariant local value — it can be set to zero by a choice of representative at any one point — and only its curvature obstructs doing so on a neighbourhood.
- **The curvature as a commutator that closes on the algebra.** The commutator $[\tilde\nabla_{\mathrm{gco},\Phi,\imath}, \tilde\nabla_{\mathrm{gco},\Phi,\jmath}]$ is multiplication by $i\kappa F_{\imath\jmath}$; unlike $\tilde\nabla_{\mathrm{gco},\Phi}$ itself, it is an element of $\mathbb{B}$.
- **The covariant square.** With $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}$ the quaternion conjugate of $\tilde\nabla_{\mathrm{gco},\Phi}$, the exact operator identity splits into the covariant d'Alembertian in its scalar part and the curvature in its vector part:
$$
(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi} = \sum_{\imath\in\{t,x,y,z\}}  \tilde\nabla_{\mathrm{gco},\Phi,\imath}^{2} +i\kappa\tilde{F}
$$

The division between what is established and what is interpretation is kept explicit, as in the companion articles.

- **Established, and recomputed below.** The identities of the four bullets above; the flatness of pure-connections; the reality condition that keeps $\tilde{A}_{\Phi}$ in $\mathbb{B}_{\Phi}$; and the observation that the connection one-form $\sum_{\imath} A_{\imath}\,dx_{\imath}$ is a real quaternion.
- **Interpretation.** Reading $\tilde{A}_{\Phi}$ as a connection on a bundle, the covariant derivative as parallel transport, and $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi}$ as the biquaternion form of the identity "square of a Dirac operator equals Laplacian plus curvature" are geometric interpretations of algebraic content. They are labelled as interpretation wherever they occur.
- **Gaps, left visible.** The non-abelian extension and the reality and compactness conditions that would select a compact algebra are not settled here. Nor is the charge-conjugation operation that a gauged scalar action turns out to need; that one is discovered below rather than assumed, in §*Does the Action Decide?*, and it is the only place where the article is forced to introduce an operation the algebra does not supply.

## The Covariant Derivative and Its Components

In the abelian case the connection coefficients $A_{\imath}$ are complex scalars. Writing $\tilde{A}_{\Phi} = \sum_{\imath} A_{\imath} e_{\imath}$, the covariant derivative is the first-order operator

$$
\tilde\nabla_{\mathrm{gco},\Phi} = \tilde\nabla_\Phi +i\kappa\tilde{A}_{\Phi}
  = \sum_{\imath\in\{t,x,y,z\}}  e_{\imath}\left(\partial/\partial R_{\imath} +i\kappa A_{\imath}\right)
  =: \sum_{\imath\in\{t,x,y,z\}}  e_{\imath}\, \tilde\nabla_{\mathrm{gco},\Phi,\imath},
$$

where the coordinate is that of the material frame of *Frame and Metric Conventions*, $Q_t=i q'_t$ and $Q_{\imath}=q_{\imath}$. Its action on a biquaternion-valued field $\tilde{Ξ}(\tilde{Q})$ is left multiplication by that operator,

$$
\tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ} = \tilde\nabla_\Phi\tilde{Ξ} +i\kappa\tilde{A}_{\Phi}\tilde{Ξ},
\qquad
\tilde\nabla_{\mathrm{gco},\Phi,\imath}\tilde{Ξ} = \partial/\partial R_{\imath}\,\tilde{Ξ} +i\kappa A_{\imath}\tilde{Ξ}.
$$

The two descriptions agree because $\sum_{\imath} e_{\imath} A_{\imath} = \tilde{A}_{\Phi}$ and $\sum_{\imath} e_{\imath}\partial/\partial R_{\imath} = \tilde\nabla_\Phi$: the component form of $\tilde\nabla_{\mathrm{gco},\Phi}$ is not an independent definition, it is the expansion of the same object in the quaternion basis.

Two points about the nature of $\tilde\nabla_{\mathrm{gco},\Phi}$ are worth stating before its algebra is used.

**$\tilde\nabla_{\mathrm{gco},\Phi}$ is an operator, not an algebra element.** The covariant derivative maps fields to fields; it carries the dimension of a derivative and does not belong to $\mathbb{B}$. Only its components $\tilde\nabla_{\mathrm{gco},\Phi,\imath}$ are scalar operators, and even they are not elements of the algebra. The connection $\tilde{A}_{\Phi}$, by contrast, is an element of $\mathbb{B}$ — indeed of $\mathbb{B}_{\Phi}$ — and it is the *coefficient* of the new term, not the derivative itself.

**The coefficients are central, so there is no ordering ambiguity.** In the abelian case each $A_{\imath}$ is a complex scalar and therefore commutes with every biquaternion and with the basis elements. Left and right multiplication by each coefficient $i\kappa A_{\imath}$ agree, and the derivation below never has to choose an order. This is the algebraic mark of the abelian symmetry group: the phase lies in the centre, and the connection has central coefficients.

The following table collects the components and their meanings.

| Object | Expression | Role |
|---|---|---|
| Gradient | $\tilde\nabla_\Phi$ | The ordinary derivative of *Operator and Calculus Conventions* |
| Connection | $\tilde{A}_{\Phi} = \sum_{\imath} A_{\imath} e_{\imath} \in \mathbb{B}_{\Phi}$ | Compensating field |
| Covariant derivative | $\tilde\nabla_{\mathrm{gco},\Phi} = \sum_{\imath} e_{\imath} \tilde\nabla_{\mathrm{gco},\Phi,\imath}$ | $\tilde\nabla_{\mathrm{gco},\Phi,\imath} = \partial/\partial R_{\imath} +i\kappa A_{\imath}$ |
| Time component ${\imath} = t$ | $\tilde\nabla_{\mathrm{gco},\Phi,t} = \partial/\partial R_t +i\kappa A_t = \partial/\partial R_t -\kappa a'_{t}$ | $A_t = i\,a'_t$ |
| Space components $\mu = k$ | $\tilde\nabla_{\mathrm{gco},\Phi,k} = \partial/\partial r_{\imath} +i\kappa A_{\imath}$ | $A_{\imath}$ real |

The line ${\imath}=t$ is the only place where $i^2=-1$ is used. The coupling contributes one imaginary unit and the complex time component $A_t=i\,a'_t$ contributes the other; they multiply to $-1$, and the potential term of the time component is the real number $-\kappa a'_{t}$. The three spatial components keep their imaginary unit, because $A_{\imath}$ is real.

## The Covariant Derivative as a Derivation

The properties collected here are the ones that make $\tilde\nabla_{\mathrm{gco},\Phi}$ a covariant derivative rather than an arbitrary first-order operator. They are stated for the abelian case.

**1. Linearity over constants.** For a central constant $\alpha$,

$$
\tilde\nabla_{\mathrm{gco},\Phi}(\alpha\tilde{Ξ}) = \alpha\, \tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ}, \qquad \tilde\nabla_{\mathrm{gco},\Phi}(\tilde{Ξ}\alpha) = (\tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ})\,\alpha,
$$

because constants pass through $\tilde\nabla_\Phi$ and commute with $\tilde{A}_{\Phi}$.

**2. The Leibniz rule.** For a complex scalar function $f$,

$$
\tilde\nabla_{\mathrm{gco},\Phi}(f\tilde{Ξ}) = f\,\tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ} + \left(\tilde\nabla_\Phi f\right)\tilde{Ξ}.
$$

This is the Leibniz rule of the gradient corrected by the connection: $\tilde\nabla_\Phi(f\tilde{Ξ}) = f\tilde\nabla_\Phi\tilde{Ξ} + (\tilde\nabla_\Phi f)\tilde{Ξ}$, while the connection term is $i\kappa f\tilde{A}_{\Phi}\tilde{Ξ}$ by centrality of $f$. The mirror identity for right multiplication, $\tilde\nabla_{\mathrm{gco},\Phi}(\tilde{\tilde{Ξ}}f) = (\tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ})f + \tilde{Ξ}(\tilde\nabla_\Phi f)$, does **not** hold in this two-term form: $\tilde\nabla_\Phi(\tilde{\tilde{Ξ}}f) = (\tilde\nabla_\Phi\tilde{Ξ})f + \sum_{\jmath} e_{\jmath}\tilde{Ξ}\,\partial/\partial R_{\jmath} f$, and $e_{\jmath}\tilde{Ξ}\ne\tilde{\tilde{Ξ}}e_{\jmath}$ in general. $\tilde\nabla_{\mathrm{gco},\Phi}$ is therefore a *left* derivation; the mirror rule holds for constant $f$, or with the mirror derivative that acts on the right. The derivation below uses the left rule only.

**3. The commutator with a function is the ordinary derivative.** From the Leibniz rule,

$$
[\tilde\nabla_{\mathrm{gco},\Phi,\imath}, f] = \partial/\partial R_{\imath} f,
$$

as an operator identity: $[\tilde\nabla_{\mathrm{gco},\Phi,\imath},f]\tilde{Ξ} = \tilde\nabla_{\mathrm{gco},\Phi,\imath}(f\tilde{Ξ}) - f\tilde\nabla_{\mathrm{gco},\Phi,\imath}\tilde{Ξ} = (\partial/\partial R_{\imath} f)\tilde{Ξ}$. Equivalently, the connection is exactly the difference between the covariant and the ordinary derivative,

$$
\tilde\nabla_{\mathrm{gco},\Phi,\imath} - \partial/\partial R_{\imath} =i\kappa A_{\imath},
$$

and this is the precise sense in which the connection "compensates" for the ordinary derivative's failure to be covariant.

**4. $\tilde\nabla_{\mathrm{gco},\Phi}$ is not closed under multiplication, but its commutator is.** The composition $\tilde\nabla_{\mathrm{gco},\Phi,\imath} \tilde\nabla_{\mathrm{gco},\Phi,\jmath}$ is a second-order operator and is not an algebra element. The *commutator* $[\tilde\nabla_{\mathrm{gco},\Phi,\imath},\tilde\nabla_{\mathrm{gco},\Phi,\jmath}]$, on the other hand, is first order and in fact has no derivative at all: it is multiplication by an element of $\mathbb{B}$. That element is the curvature, treated in its own section below. This is the structural reason the connection strength is the commutator of covariant derivatives rather than any single $\tilde\nabla_{\mathrm{gco},\Phi,\imath}$.

## Covariance and What It Forces

The minimal coupling article proves the covariance of the construction (inherited here, not rederived): with $\digamma_{\mathrm{cph}} = \exp(i\theta_{\mathrm{cph}}\tilde{Q})$ a central phase and $\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi} - \tilde\nabla_\Phi\Gamma$, the covariant derivative built from $\tilde{A}_{\Phi,2}$ satisfies

$$
\tilde\nabla_{\mathrm{gco},\Phi,2}(\digamma_{\mathrm{cph}}\tilde{Ξ}) = \digamma_{\mathrm{cph}}\,\tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ}
$$

Here $\theta_{\mathrm{cph}}:=\kappa\Gamma$ is the connection angle: the coupling $\kappa$ and the phase function $\Gamma$ are real, so the exponent is $i$ times a real number and the link is a phase of modulus one. Where the point $\tilde{Q}$ stands beside the angle, it is a real coordinate and the phase keeps modulus one.

for every field $\tilde{Ξ}$, so the equation $\tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ} = 0$ holds in every representative when it holds in one. For the present article the important point is the converse direction, which the minimal coupling article did not state: **covariance determines $\tilde\nabla_{\mathrm{gco},\Phi}$; the connection is forced, not chosen.**

To see this, suppose only that the field transforms as $\tilde{Ξ} \mapsto \digamma_{\mathrm{cph}}\tilde{Ξ}$ and that a derivative of the form $\tilde\nabla_{\mathrm{gco},\Phi,2} = \tilde\nabla_\Phi + \Omega_2$ is required to be covariant, $\tilde\nabla_{\mathrm{gco},\Phi,2}(\digamma_{\mathrm{cph}}\tilde{Ξ}) = \digamma_{\mathrm{cph}} \tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ}$ for all $\tilde{Ξ}$, where $\Omega_2$ denotes multiplication by an element of $\mathbb{B}$. Expanding the left-hand side with the Leibniz rule,

$$
\tilde\nabla_\Phi(\digamma_{\mathrm{cph}}\tilde{Ξ}) + \Omega_2\digamma_{\mathrm{cph}}\tilde{Ξ}
= \digamma_{\mathrm{cph}}\,\tilde\nabla_\Phi\tilde{Ξ} + \left(\tilde\nabla_\Phi\digamma_{\mathrm{cph}}\right)\tilde{Ξ} + \Omega_2\digamma_{\mathrm{cph}}\tilde{Ξ},
$$

and comparing with $\digamma_{\mathrm{cph}}(\tilde\nabla_\Phi\tilde{Ξ} + \Omega\tilde{Ξ})$ leaves $\Omega_2\digamma_{\mathrm{cph}} = \digamma_{\mathrm{cph}}\Omega - \tilde\nabla_\Phi\digamma_{\mathrm{cph}}$, that is

$$
\boxed{\;\Omega_2 = \digamma_{\mathrm{cph}}\,\Omega\,\digamma_{\mathrm{cph}}^{-1} - \left(\tilde\nabla_\Phi\digamma_{\mathrm{cph}}\right)\digamma_{\mathrm{cph}}^{-1}
= \Omega - \left(\tilde\nabla_\Phi\digamma_{\mathrm{cph}}\right)\digamma_{\mathrm{cph}}^{-1}\;}.
$$

The second form needs the centrality of $\digamma_{\mathrm{cph}}$, which lets it pass through $\Omega$; without a central phase only the first form survives.

For the exponential phase this is, by the chain rule $\tilde\nabla_\Phi\digamma_{\mathrm{cph}} =i\kappa(\tilde\nabla_\Phi\Gamma)\digamma_{\mathrm{cph}}$,

$$
\Omega_2 = \Omega -i\kappa\tilde\nabla_\Phi\Gamma,
$$

which, with $\Omega =i\kappa\tilde{A}_{\Phi}$, is the inherited transformation law. The compensating field is therefore not an assumption added to the theory: once the phase is localized, the requirement of covariance leaves no freedom in the transformation of the connection. The specialization of the chain rule to the exponential was checked by finite differences at a point not used to motivate it, and the algebraic form $\Omega_2 = \digamma_{\mathrm{cph}}\Omega\digamma_{\mathrm{cph}}^{-1} - (\tilde\nabla_\Phi\digamma_{\mathrm{cph}})\digamma_{\mathrm{cph}}^{-1}$ was checked exactly on random central phases in a truncated ring.

The forcing is stated within the left-action convention that the minimal coupling produces; with a right action the same argument gives the mirror derivative, and the mixed insertion is not covariant at all. The parent's massive equation is written with the left action,

$$
\tilde\nabla_\Phi\tilde{Ξ}_{R} = 2\pi\nu_m\tilde{Ξ}_{L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L} = 2\pi\nu_m\tilde{Ξ}_{R} ,
$$

and the linear mass term passes the central phase through, so the left action is the natural one for the charged massive field and it is the form the minimal-coupling article states. The choice between the left and right actions for a general matter field is a choice of matter representation, raised as an open question by that article and left open here.

The centrality of $\digamma_{\mathrm{cph}}$ is what makes the transformation law *additive*. Left and right multiplication by $\digamma_{\mathrm{cph}}$ agree, so no conjugation appears and the symmetry group is abelian. It is the centre of $\mathbb{B}$ that supplies the group, and the centre is one complex dimension; the symmetry group is $\mathrm{U}(1)$.

The reality of the phase function is inherited as well. A real $\Gamma$ keeps $\tilde{A}_{\Phi}$ in the material sector: $\tilde\nabla_\Phi\Gamma$ has an imaginary scalar coefficient and real vector coefficients, exactly the membership condition of $\mathbb{B}_{\Phi}$; a complex $\Gamma$ would move the connection out of it.

## The Connection as an Orbit

The transformation law makes the connection's status precise.

**The connection is not invariant.** Its entire orbit is the set $\{\tilde{A}_{\Phi} - \tilde\nabla_\Phi\Gamma\}$. The scalar part of $(\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}$,

$$
S = \mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}\right) = \partial/\partial R_t\,A_t + \mathrm{div}\,\vec A,
$$

transforms as $S_2 = S - \Box_\Phi\Gamma$, so $S$ is a pure gradient quantity; the Lorenz fixing condition $S = 0$ is a choice, not a condition. This is the scalar part of the Maxwell article, inherited unchanged.

**Pure-connections are flat.** If $\tilde{A}_{\Phi} = \tilde\nabla_\Phi\Gamma$ for a scalar function $\Gamma$, then

$$
\tilde{F} = \mathrm{Vect}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\Gamma\right) = 0,
$$

because $(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\Gamma = \Box_\Phi\Gamma\, e_t$ is a pure scalar and has no vector part. A connection that is a gradient carries no curvature. This was checked for complex as well as real $\Gamma$.

**A single point can always be made connection-free.** Given any connection $\tilde{A}_{\Phi}$ and any point $\tilde{Q}_0$, choose the real, affine phase function

$$
\Gamma(\tilde{Q}) = -a\,r'_t + A_x(\tilde{Q}_0)\,r_x + A_y(\tilde{Q}_0)\,r_y + A_z(\tilde{Q}_0)\,r_z,
\qquad a = -i\,A_t(\tilde{Q}_0) = \xi(\tilde{Q}_0)\in\mathbb{R},
$$

so that $\partial/\partial R_{\imath}\,\Gamma(\tilde{Q}_0) = A_{\imath}(\tilde{Q}_0)$ and hence $\tilde{A}_{\Phi,2}(\tilde{Q}_0) = 0$. **The coefficient $a$ is $\xi$, the real scalar of $A_t = i\xi$, and no factor of $c$ enters**: $R_t = i r'_t$, so $\partial r'_t/\partial R_t = -i$ and $\partial\Gamma/\partial R_t = -a\,(-i) = ia = i\xi = A_t$. Writing $-ic\,A_t$ instead gives $c\xi$, one factor of $c$ too many, and leaves the connection unremoved by that factor; there is no $c$ in the coordinate, since $r'_t$ is already the length $ct$. The connection therefore has no invariant value at a point; whatever invariant content it has must be built from derivatives.

**The curvature is the obstruction to doing this on a neighbourhood.** A connection with $\tilde{F} = 0$ satisfies $F_{\imath\jmath} = \partial/\partial R_{\imath} A_{\jmath} - \partial/\partial R_{\jmath} A_{\imath} = 0$, and the Poincaré lemma applied to the one-form $\sum_{\imath} A_{\imath}\,dx_{\imath}$ then supplies a local $\Gamma$ with $\tilde{A}_{\Phi} = \tilde\nabla_\Phi\Gamma$. The step from a closed one-form to an exact one is the Poincaré lemma; it is *invoked* here, not recomputed. The conclusion is that $\tilde{F}$ measures exactly what cannot be removed by a local transformation.

**The connection one-form is a real quaternion.** One observation about the connection is worth recording. Pairing the connection with a coordinate displacement gives

$$
\sum_{\imath} A_{\imath}\,dx_{\imath} = A_t\,d(i r'_t) + \sum_{\imath\in\{x,y,z\}} A_{\imath}\,dr_{\imath} = -\xi\,dr'_t + \vec A\cdot d\vec r ,
\qquad
d\vec r = \vec e_x\,dr_x + \vec e_y\,dr_y + \vec e_z\,dr_z ,
$$

which is real. The time term is real because its two imaginary units cancel, $d(i r'_t) = i\,dr'_t$ and $A_t = i\,a'_t$ giving $i^2a'_t\,dr'_t = -\xi\,dr'_t$; the spatial terms are real because $A_{\imath}$ and $dr_{\imath}$ are separately real. **It is the same cancellation as in the charge density of *Noether's Theorem in Biquaternionic Form***, where $J_t = ic\rho$ pairs the imaginary unit of the time component with the imaginary unit of the density and leaves a real number: in both cases the imaginary unit is the one the $ir'_t$ convention puts on $R_t$, and in both cases spending it twice is what makes the object real. In the algebra this says $\sum_{\imath} A_{\imath}\,dx_{\imath} \in \mathbb{B}_{H}$, the real-quaternion subspace. Around a closed path the integral is invariant, because $\sum_{\imath} A_{\imath}\,dx_{\imath} \mapsto \sum_{\imath} A_{\imath}\,dx_{\imath} - d\Gamma$ and $\oint d\Gamma = 0$. Reading the exponential of this integral as a **holonomy** is a geometric interpretation of the algebraic fact; whether the real-quaternion character of the one-form carries content beyond this bookkeeping is not established here and is recorded as an open question.

## The Curvature as the Commutator of Covariant Derivatives

The curvature is the part of the covariant derivative that survives antisymmetrization. In the abelian case the connection coefficients commute, and the general commutator formula collapses to the curl:

$$
[\tilde\nabla_{\mathrm{gco},\Phi,\imath}, \tilde\nabla_{\mathrm{gco},\Phi,\jmath}] =i\kappa\left(\partial/\partial R_{\imath} A_{\jmath} - \partial/\partial R_{\jmath} A_{\imath}\right) =i\kappa F_{\imath\jmath},
\qquad
F_{\imath\jmath} = \partial/\partial R_{\imath} A_{\jmath} - \partial/\partial R_{\jmath} A_{\imath} .
$$

This is the minimal coupling article's commutator identity, inherited here. Three consequences are developed in the present article.

**The commutator closes on the algebra.** Although $\tilde\nabla_{\mathrm{gco},\Phi,\imath}$ is an operator and not an element of $\mathbb{B}$, its commutator with $\tilde\nabla_{\mathrm{gco},\Phi,\jmath}$ is multiplication by the biquaternion $i\kappa F_{\imath\jmath}$ — a scalar multiple of a field. The failure of covariant derivatives to commute is thus an algebraic object, not a differential one, and it can be contracted with the basis to form the field-strength biquaternion.

**The contraction is the field strength.** Reading off the components of $(\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}$ gives

$$
\tilde{F} = \mathrm{Vect}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}\right)
= \frac{1}{2}\sum_{\imath,\jmath\in\{t,x,y,z\}}  F_{\imath\jmath}\,e_{\imath}^{\natural} e_{\jmath},
\qquad
\tilde{F} =\frac{1}{2i\kappa}\sum_{\imath,\jmath\in\{t,x,y,z\}}[\tilde\nabla_{\mathrm{gco},\Phi,\imath}, \tilde\nabla_{\mathrm{gco},\Phi,\jmath}]\,e_{\imath}^{\natural} e_{\jmath} ,
$$

with $e_t^{\natural} = e_t$ and $e_{\imath}^{\natural} = -\vec e_{\imath}$. The first identity is purely algebraic in the derivatives and is the minimal coupling article's curvature identity; the second is its restatement as a commutator of covariant derivatives.

**The curvature is invariant and is not in the material sector.** Because $\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi} - \tilde\nabla_\Phi\Gamma$ and $\mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\Gamma) = 0$, $\tilde{F}$ is unchanged by a local transformation. It is nevertheless not an element of $\mathbb{B}_{\Phi}$: it has vanishing scalar part and a vector part that is neither purely real nor purely imaginary, as the Maxwell article records. The connection is a material-sector object; its curvature is not.

Because $\tilde{F}$ is built from $\tilde{A}_{\Phi}$ by differentiation, the homogeneous Maxwell equations are identities rather than equations of motion — the Bianchi identity of the connection. The biquaternion form of that identity and the non-abelian completion of the curvature are the subjects of separate planned companions and are not claimed here. (In particular, the one-line equation $\tilde\nabla_\Phi\tilde{F} = 0$ is *not* the Bianchi identity; it is the full source-free Maxwell system. This was checked and recorded in the minimal coupling companion so that it is not written by mistake.)

The shape recurs one rank up. The commutator of two kinetic angular momenta is a third one plus a multiplication operator quadratic in position, so it too leaves the span of the operators it starts from and lands on multiplication. The companion article *The Kinetic Momentum: A Bracket That Does Not Close* records that bracket and reads it against the curvature: the mechanical momentum is the spatial part of the connection, the field strength is its curvature, and the kinetic angular momentum is the cross product of position with the connection.

## The Covariant Square and the Curvature Term

The commutator of two covariant derivatives is first order. The *square* of the covariant derivative is second order, and in the biquaternion algebra its scalar and vector parts separate cleanly.

Define the **quaternion conjugate** of the covariant derivative by conjugating the basis:

$$
(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} := \sum_{\imath}  e_{\imath}^{\natural} \tilde\nabla_{\mathrm{gco},\Phi,\imath} = (\tilde\nabla_\Phi)^{\natural}+i\kappa\tilde{A}_{\Phi}^{\natural},
$$

the conjugation $\natural$ being that of *Product and Form Conventions*, applied to the basis elements, the central coefficients $\tilde\nabla_{\mathrm{gco},\Phi,\imath}$ passing through untouched. Here $\tilde{A}_{\Phi}^{\natural} \neq -\tilde{A}_{\Phi}$ in general; quaternion conjugation is not charge conjugation, and $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}$ is the quaternion conjugate of the operator, not the operator for the opposite charge.

**The two conjugates differ, and by how much.** It is tempting to identify this operator with the one that would act on the conjugate field, $\tilde{Ξ}^{*}$. It is not the same operator, and the discrepancy is exact:

$$
(\tilde\nabla_\Phi)^{\natural}+\lambda\,\tilde{A}_{\Phi}^{\natural}\quad\text{(basis conjugated)}\qquad\text{against}\qquad(\tilde\nabla_\Phi)^{\natural}-\lambda\,\tilde{A}_{\Phi}\quad\text{(charge flipped)},
$$

with $\lambda:=i\kappa$. For $\tilde{A}_{\Phi}\in\mathbb{B}_{\Phi}$ the two differ by $\lambda(\tilde{A}_{\Phi}^{\natural}+\tilde{A}_{\Phi}) = 2\lambda\,i\,a'_t\,e_t$: they agree on the three spatial components and disagree on the time component alone. The reason is that $\lambda\tilde{A}_{\Phi}$ is fixed by $^{*}$ — the conjugation negates $\lambda$ and negates $\tilde{A}_{\Phi}$, and the two minus signs cancel — so the algebra's own conjugation cannot flip a charge. §*Does the Action Decide?* is where this difference has consequences: it is exactly the difference between a real and a complex Lagrangian. With this definition the exact operator identity

$$
\boxed{\;(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi} = \sum_{\imath\in\{t,x,y,z\}}  \tilde\nabla_{\mathrm{gco},\Phi,\imath}^{2} +i\kappa\tilde{F}\;}
$$

holds, where $\tilde\nabla_{\mathrm{gco},\Phi,\imath}^2$ means $\tilde\nabla_{\mathrm{gco},\Phi,\imath} \tilde\nabla_{\mathrm{gco},\Phi,\imath}$ and $\sum_{\imath}  \tilde\nabla_{\mathrm{gco},\Phi,\imath}^2 = \sum_{\imath}\left(\partial/\partial R_{\imath} +i\kappa A_{\imath}\right)^2$ is the **covariant d'Alembertian**. The identity was checked on random connections and random fields, on constant and on non-constant potentials, and reduces to $(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi = \Box_\Phi$ when $\tilde{A}_{\Phi} = 0$.

The derivation is short. Expanding the product,

$$
(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi} = \sum_{\imath,\jmath} e_{\imath}^{\natural} e_{\jmath}\, \tilde\nabla_{\mathrm{gco},\Phi,\imath} \tilde\nabla_{\mathrm{gco},\Phi,\jmath} .
$$

The diagonal terms give $e_t\sum_{\imath} \tilde\nabla_{\mathrm{gco},\Phi,\imath}^2$, since $e_{\imath}^{\natural} e_{\imath} = e_t$ for every $\mu$. For each pair with ${\imath}\neq\jmath$ the two ordered terms combine, because $\tilde\nabla_{\mathrm{gco},\Phi,\imath} \tilde\nabla_{\mathrm{gco},\Phi,\jmath} = \tfrac12\{\tilde\nabla_{\mathrm{gco},\Phi,\imath},\tilde\nabla_{\mathrm{gco},\Phi,\jmath}\}+\tfrac12[\tilde\nabla_{\mathrm{gco},\Phi,\imath},\tilde\nabla_{\mathrm{gco},\Phi,\jmath}]$ while $\tilde\nabla_{\mathrm{gco},\Phi,\jmath} \tilde\nabla_{\mathrm{gco},\Phi,\imath} = \tfrac12\{\tilde\nabla_{\mathrm{gco},\Phi,\imath},\tilde\nabla_{\mathrm{gco},\Phi,\jmath}\}-\tfrac12[\tilde\nabla_{\mathrm{gco},\Phi,\imath},\tilde\nabla_{\mathrm{gco},\Phi,\jmath}]$:

$$
e_{\imath}^{\natural} e_{\jmath}\,\tilde\nabla_{\mathrm{gco},\Phi,\imath} \tilde\nabla_{\mathrm{gco},\Phi,\jmath} + e_{\jmath}^{\natural} e_{\imath}\,\tilde\nabla_{\mathrm{gco},\Phi,\jmath} \tilde\nabla_{\mathrm{gco},\Phi,\imath}
= \left(e_{\imath}^{\natural} e_{\jmath}+e_{\jmath}^{\natural} e_{\imath}\right)\tfrac12\{\tilde\nabla_{\mathrm{gco},\Phi,\imath},\tilde\nabla_{\mathrm{gco},\Phi,\jmath}\}
+ \left(e_{\imath}^{\natural} e_{\jmath}-e_{\jmath}^{\natural} e_{\imath}\right)\tfrac12[\tilde\nabla_{\mathrm{gco},\Phi,\imath},\tilde\nabla_{\mathrm{gco},\Phi,\jmath}]
= e_{\imath}^{\natural} e_{\jmath}\,[\tilde\nabla_{\mathrm{gco},\Phi,\imath},\tilde\nabla_{\mathrm{gco},\Phi,\jmath}] .
$$

The first coefficient vanishes term by term and the second is $2e_{\imath}^{\natural} e_{\jmath}$. Summing over the pairs with ${\imath}<\jmath$ and using $[\tilde\nabla_{\mathrm{gco},\Phi,\imath},\tilde\nabla_{\mathrm{gco},\Phi,\jmath}]=i\kappa F_{\imath\jmath}$ leaves $i\kappa\sum_{\imath<\jmath} F_{\imath\jmath}e_{\imath}^{\natural} e_{\jmath}$, which is $i\kappa\tilde{F}$ by the definition of $\tilde{F}$ above. The scalar and vector parts of the result are therefore

$$
\mathrm{Sc}\!\left((\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi}\right) = \sum_{\imath\in\{t,x,y,z\}}  \tilde\nabla_{\mathrm{gco},\Phi,\imath}^{2},
\qquad
\mathrm{Vect}\!\left((\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi}\right) =i\kappa\tilde{F}.
$$

The square of the covariant derivative contains the curvature in its vector part. Two consequences follow.

**The second-order consequence of the massless equation.** If $\tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ} = 0$ then $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ} = 0$: the field satisfies a covariant wave equation with a curvature term,

$$
\left(\sum_{\imath}  \tilde\nabla_{\mathrm{gco},\Phi,\imath}^{2}\right)\tilde{Ξ} +i\kappa\tilde{F}\tilde{Ξ} = 0 .
$$

The structural similarity to the identity that the square of a Dirac operator is a Laplacian plus a curvature term is an **interpretation** of this result, not a claim that the biquaternion operator is the standard Dirac operator.

**The charged scalar: two candidate operators.** The minimal coupling article's clean realization of the global symmetry was the complex scalar biquaternion field $\tilde{Ξ} = \xi\,e_t$ obeying the massive Klein–Gordon equation $(\Box_\Phi - 4\pi^{2}\nu_m^{2})\tilde{Ξ} = 0$; the free equation is examined in the Klein–Gordon article, which states it and does not derive it from an action. Covariantizing the *scalar operator* gives $\left(\sum_{\imath} \tilde\nabla_{\mathrm{gco},\Phi,\imath}^2 - 4\pi^{2}\nu_m^{2}\right)\xi\,e_t = 0$, which is consistent. But $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi}(\xi e_t) = \left(\sum_{\imath}  \tilde\nabla_{\mathrm{gco},\Phi,\imath}^2\xi\right)e_t +i\kappa\xi\,\tilde{F}$, and the second term is a pure vector whenever $\tilde{F} \neq 0$. A purely scalar field therefore cannot satisfy $\left((\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi} - 4\pi^{2}\nu_m^{2}\right)\tilde{Ξ} = 0$ in a region of nonzero curvature; only the scalar projection $\mathrm{Sc}((\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi})$ acts on scalars, or the charged scalar must acquire vector components. Which of the two the framework's own action produces is settled in §*Does the Action Decide?* immediately below; what it costs to write that action is not. The distinction is genuine: the minimal coupling of a scalar is not the same statement as the minimal coupling of a biquaternion, and the difference is the curvature. Here $\nu_m$ is the mass wave number, the inverse of the mass length up to $2\pi$.

### Does the Action Decide?

The two operators offered above are separated by the action of the stationary-action article, and the answer is the scalar projection — but not because the pairing projects anything away, and the way the action decides is worth recording.

Minimal coupling in the action means the replacement $\tilde\nabla_\Phi\to\tilde\nabla_{\mathrm{gco},\Phi}$ in $\mathcal{L}$. Take $\tilde\Xi=\xi e_t$. Because $e_t$ is central, only the diagonal terms survive the scalar part, and the Lagrangian becomes a sum over the four indices,

$$
\mathcal{L} = \sum_{\imath}\big(\partial_\imath\xi^{*}+\lambda\,A_\imath\,\xi^{*}\big)\big(\partial_\imath\xi+\lambda\,A_\imath\,\xi\big) + m_0^{2}\,\xi^{*}\xi,
\qquad \lambda:=i\kappa,\quad m_0:=2\pi\nu_m .
$$

**With the same charge on the two factors this is not real**, and the time index is why. Under $^{*}$ the derivative flips sign, $\bigl(\partial/\partial R_t\,\xi\bigr)^{*} = -\,\partial/\partial R_t\,\xi^{*}$, because $\partial/\partial R_t = -i\,\partial/\partial r'_t$ and the imaginary unit changes sign; the potential term does not flip, because $\lambda\,\tilde{A}_{\Phi}$ is fixed by $^{*}$ as §*The Covariant Square* records. So the factor on the conjugate field is neither the conjugate of the other factor nor its negative, and the pair fails to be a modulus.

**Flipping the charge on the conjugate factor repairs it.** Differentiating $\tilde\Xi^{*}$ with $-\lambda\,A_{\imath}$ rather than $+\lambda\,A_{\imath}$ turns the same display into

$$
\mathcal{L} = -\bigl|D_t\xi\bigr|^{2}+\sum_{\imath\in\{x,y,z\}}\bigl|D_{\imath}\xi\bigr|^{2}+m_0^{2}\lvert\xi\rvert^{2},
\qquad D_{\imath}:=\partial/\partial R_{\imath}+\lambda\,A_{\imath},
$$

which is real, is the standard gauged scalar Lagrangian with the metric's signature, and is invariant because the conjugate field carries the inverse phase. Its Euler–Lagrange equation follows from one derivative and one integration by parts,

$$
\Bigl(\sum_{\imath\in\{t,x,y,z\}}\tilde\nabla_{\mathrm{gco},\Phi,\imath}^{2}-m_0^{2}\Bigr)\xi = 0 ,
$$

which is the scalar projection — the scalar part of the covariant square — and not the full square. Both displays were checked at a point with a non-constant potential: the opposite-charge functional is real to machine precision and equals the modulus form, while the same-charge functional has a nonzero imaginary part there.

**What this settles, and what it leaves.** The gap closes on the side of the projection. The framework's action never produces the inconsistent full-square equation for a scalar, because a scalar has no vector component for the curvature term to act on; $i\kappa\xi\tilde{F}$ is then not an equation the field must satisfy but the statement that a scalar field is not an eigenfield of the covariant square, and the difference *is* the curvature. What the derivation leaves is an operation rather than an equation: the conjugate factor of the action needs the opposite charge, and the section above has just recorded that $^{*}$ does not supply it, since it fixes $\lambda\tilde{A}_{\Phi}$. A gauged scalar action here therefore has to name a charge-conjugation insertion. Whether the algebra supplies one as an involution — negating $\lambda\tilde{A}_{\Phi}$ while leaving $i$ alone — is open, and it is the same operation a charged antiparticle would require.

### The Chiral Pair and Why the Mass Couples Two Fields

One equation carries the mass under these conventions, and it is the chiral pair.

**The chiral pair** on the algebra. Both members act by left multiplication, the second is the quaternion conjugate of the first, and the mass couples the $L$ part to the $R$ part:

$$
\tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ}_{R} = 2\pi\nu_m\tilde{Ξ}_{L},
\qquad
(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}\tilde{Ξ}_{L} = 2\pi\nu_m\tilde{Ξ}_{R} .
$$

Squaring its first member with the second gives the boxed identity on the $R$ part, $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ}_{R} = 4\pi^{2}\nu_m^{2}\tilde{Ξ}_{R}$. The second member is not a new equation: it is the first written on the conjugate field, $\natural$ is what separates them, and both act from the left.

**Why the mass couples two fields.** A first-order equation on a single field does not close on a second-order equation for that field. Write $\tilde\nabla_\Phi\tilde{Ξ} = 2\pi\nu_m\tilde{Ξ}$ and apply $(\tilde\nabla_\Phi)^{\natural}$: the result is $\Box_\Phi\tilde{Ξ} = m\,(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}$, an equation in two different objects, and nothing reduces it to $\Box_\Phi\tilde{Ξ} = 4\pi^{2}\nu_m^{2}\tilde{Ξ}$, because $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ} = 2\pi\nu_m\tilde{Ξ}$ is the second equation and not a consequence of the first. If both members were imposed on one field, their difference would give $2\sum_{\imath\in\{x,y,z\}}\vec e_{\imath}\,\partial/\partial R_{\imath}\tilde{Ξ} = 0$, so the field would not vary in space and the remaining time equation would be exponential rather than oscillatory: no wave survives. Two fields close the system instead, and applying $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}$ to $\tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ}_{R} = 2\pi\nu_m\tilde{Ξ}_{L}$ returns $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ}_{R} = m(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}\tilde{Ξ}_{L} = 4\pi^{2}\nu_m^{2}\tilde{Ξ}_{R}$, which is the boxed identity.

The square of the gradient, the operator left when the connection is switched off, is not scalar, and it is not $\Box_\Phi$. On a scalar function it reads

$$
\tilde\nabla_\Phi^2=\frac{\partial^2}{\partial R_t^2}-\Delta_\Phi+2\sum_{\imath\in\{x,y,z\}}\vec e_{\imath}\,\frac{\partial^2}{\partial R_t\partial R_{\imath}},
$$

which is $\Box_\Phi$ with the sign of $\Delta_\Phi$ reversed and a vector part added. The expression is derived here from the squares of the invertibles, and it was checked with residual $0$ on random polynomial scalar functions. The Laplacian enters with opposite signs because the spatial legs of $\tilde\nabla_\Phi$ square to $-e_t$ while $e_{\imath}^{\natural} e_{\imath} = e_t$ for every $\mu$, and the mixed derivatives leave a vector part wherever they do not vanish. Writing $\tilde\nabla_\Phi^2 = \Box_\Phi$ would therefore be wrong by $2\Delta_\Phi$ in the scalar part and by that vector part.

**The minimal coupling** replaces $\tilde\nabla_\Phi$ by $\tilde\nabla_{\mathrm{gco},\Phi}$ and $(\tilde\nabla_\Phi)^{\natural}$ by $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}$ in the pair, which is the coupled pair of *Covariance and What It Forces*. The replacement holds as an algebraic substitution, term by term, because the coefficients $A_{\imath}$ are central and pass through the invertibles. What an algebraic substitution does not carry on its own is the reality of the functional it produces; that is the subject of the next subsection, and it is where the coupled action is actually fixed.

## What the Algebra Supplies, Transcribes, and Only Interprets

The boundary can be drawn as in the companion articles.

**What it supplies.** The centre $\mathbb{B}_{C}$ supplies the abelian symmetry group $\mathrm{U}(1)$ canonically. The algebra makes the transformation law forced rather than assumed, makes the connection a material-sector object, makes the commutator of covariant derivatives an element of the algebra, and makes the covariant square split into a wave operator and a curvature term without any extra structure. It also preserves the sector decomposition under a real phase function.

**What it only transcribes.** The global-to-local argument itself, the form of minimal coupling, and the covariant derivative are the standard constructions, written in the algebra's notation. The algebra provides a home and makes the identities transparent; it does not supply a reason for a connection to exist, and it does not fix the coupling constant $\kappa$.

**What is interpretation.** The bundle picture — connection as parallel transport, curvature as infinitesimal holonomy — is a consistent interpretation of the algebraic content. The one-form $\sum_{\imath} A_{\imath}\,dx_{\imath}$ lies in the real-quaternion subspace and its loop integral is invariant by the fundamental theorem of calculus ($\oint d\Gamma = 0$); the geometric interpretation of those two facts is interpretation, and the identity $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi} = \sum_{\imath}  \tilde\nabla_{\mathrm{gco},\Phi,\imath}^2 +i\kappa\tilde{F}$ is what makes the interpretation precise.

## The Connection and the Gravitational Connection

The word "connection" is used in the framework for two different objects, and conflating them is an error worth naming.

The connection of this article is **one-sided**: $\tilde\nabla_{\mathrm{gco},\Phi,\imath} = \partial/\partial R_{\imath} +i\kappa A_{\imath}$ acts by left multiplication, and it can be written this way only because the abelian connection is central, so left and right multiplication agree. The connection of the curved-spacetime article of the corpus is **two-sided**: a biquaternionic covariant derivative on the material sector must be written $\tilde\nabla_{\mathrm{gco},\Phi,\imath}\tilde{Q} = \partial/\partial R_{\imath}\,\tilde{Q} + \vec\Gamma_{\imath}\tilde{Q} + \tilde{Q}\vec\Gamma_{\imath}^{*}$, because the Lorentz generators act on $\mathbb{B}_{\Phi}$ by the two-sided infinitesimal action $G\tilde{Q} + \tilde{Q}G^{*}$ and not by the commutator; the two differ precisely for the boosts. The connection of this article is a $\mathrm{U}(1)$ connection of the centre; the gravitational connection lies in the six-dimensional scalar-free subspace of $\mathbb{B}$. They are distinct objects that happen to share a name, and no relation between them is asserted here.

The distinction has a consequence the corpus had not recorded, and an external source names it. For an internal connection force, the abelian case of this article, the substitution $\partial/\partial R_{\imath} \to \tilde\nabla_{\mathrm{gco},\Phi,\imath}$ gives the same physics whether it is applied to the action or to the Euler–Lagrange equations, because the connection is central: it multiplies from the side the derivative already multiplies from, and it passes through every invertible element. For the standard gravitational coupling in the vierbein formulation, the two procedures **do not commute**: the varied equation acquires an anticommutator term between the frame element and the Lorentz generator, which the substituted equation does not have. The difference is settled by one test, whether the generator commutes with the four units, and the test separates the two cases cleanly. The centre of $\mathbb{B}$ is the real span of $e_t$ and $ie_t$, so the six-dimensional scalar-free subspace, where the Lorentz generator lives, contains no central element at all; the scalar-free units themselves do not even commute with one another, $[\vec e_x,\vec e_y]=2\vec e_z$ and cyclically, whereas the central element commutes with everything,

$$
[\vec e_x,\vec e_y]=2\vec e_z\neq0,
\qquad
[ie_t,\tilde Q]=0\ \text{ for every } \tilde Q\in\mathbb{B}.
$$

J. Fredsted (arXiv:1906.12200v3 [physics.gen-ph], 2019) proves the mismatch and reads it as a tension with the equivalence principle; the construction is recorded, with its world-index repair, in *Curved Spacetime and the Biquaternion Framework*. It is the sharpest available answer to the question this section raises: the one-sided central connection of this article is exactly the case in which localization is unambiguous, and the two-sided gravitational connection is exactly the case in which it is not.

A second external source goes further and puts the two objects into one. J. Fredsted (arXiv:0811.1357v4 [math-ph], 2009) constructs a formalism on a biquaternionic basis $s_{\imath} \in \mathbb{B}_{\Phi}$ with the metric $g_{\imath\jmath} = \langle s_{\imath}, s_{\jmath}\rangle$ and a **single** connection $\omega_{\imath} \in \mathbb{C}\otimes\mathbb{H}$ subject only to $\mathrm{Sc}(\omega_{\imath} + \bar{\omega}_{\imath}^*) = 0$; the imaginary-scalar part of $\omega_{\imath}$ is a local $\mathrm{U}(1)$ and its vector part is the Lorentz connection, so the two connections of this section are two parts of one algebra-valued object. The corpus records the construction — it is the same frame route the curved-spacetime article builds, reached from the other end — but does not adopt it, and continues to assert no relation between its central $\mathrm{U}(1)$ connection and its traceless gravitational connection. What the external construction shows is that the two are not forbidden to be one; what the corpus lacks is any reason to identify them.

## Open Questions

1. **The charge-conjugation insertion.** §*Does the Action Decide?* settles the equation: minimally coupling the action gives the scalar projection, $\sum_{\imath}\tilde\nabla_{\mathrm{gco},\Phi,\imath}^2\xi = m_0^{2}\xi$, for a charged scalar, and the curvature term $i\kappa\xi\tilde{F}$ is a statement about the covariant square rather than an equation for the field. What that derivation needs, and what is open, is the operation: the conjugate factor of the action must carry the opposite charge, which the algebra's $^{*}$ does not supply, because $^{*}$ fixes $\lambda\tilde{A}_{\Phi}$. Whether the framework can define a charge conjugation — negating $\lambda\tilde{A}_{\Phi}$ and leaving $i$ alone — and whether it is an involution compatible with the other conjugations, is the open point. It is the same operation a charged antiparticle would require, so it is not an idle one.

2. **The non-abelian extension.** The commutator of covariant derivatives acquires $[A_{\imath},A_{\jmath}]$ when the connection is $\mathbb{B}$-valued, and the algebra already contains the required non-commutativity. What is not derived is a reality and tracelessness condition that would select a compact algebra; the commutator algebra of $\mathbb{B}$ is $\mathfrak{gl}(2,\mathbb{C})$, not compact. The candidates are easy to name: the compact real forms of $\mathfrak{gl}(2,\mathbb{C})$ are $\mathfrak{u}(2)=\mathfrak{u}(1)\oplus\mathfrak{su}(2)$, the $\mathfrak{u}(1)$ being the centre already in use, and the only compact simple real form inside $\mathbb{B}$ is $\mathfrak{su}(2)=\mathrm{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$, whose brackets are $[i\vec e_a,i\vec e_b]=2i\varepsilon_{abc}\,i\vec e_c$. What an $SU(2)$ connection would cost is already visible in §*The Connection and the Gravitational Connection*: its generators are not central, so left and right multiplication no longer agree, localization and Euler–Lagrange variation no longer commute, and the matter representation must be specified. Building that connection with an explicit representation, and checking whether the ordering problem of the two-sided case reappears there, is the concrete form the gap leaves.

3. **The matter representation.** The covariant derivative acts by left multiplication, and in the abelian case left and right agree. For the charged massive field the parent's linear chiral pair is written with the left action, which makes the left action the natural one there. For a non-abelian connection the two differ, and the representation carried by the matter field must be specified; what fixes it for a general matter field is open, and the chiral-fermion article's treatment of the two parts named by the subscript and the minimal-coupling article's left/right analysis are the concrete settings in which the question is posed.

4. **Dynamical content of the covariant square.** The curvature term $i\kappa\tilde{F}$ in $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi}$ is structurally the biquaternion analogue of the curvature term in the square of a Dirac operator. Does it carry observable content — a magnetic-moment coupling — or is it a rewriting of the commutator identity with no independent consequence? The standard analogy is worth naming: squaring the Dirac operator produces $\sigma^{\mu\nu}F_{\mu\nu}$, the magnetic-moment term, so a curvature term in the square of a first-order operator is where such a coupling lives. Whether the biquaternion analogue becomes one depends on identifying a spin structure inside the algebra, which this article does not do; the structural similarity alone does not supply it.

5. **The one-form and the holonomy.** The connection one-form $\sum_{\imath} A_{\imath}\,dx_{\imath}$ is a real quaternion, the loop integral is invariant, and the curvature measures its infinitesimal holonomy. Is the real-quaternion character content-bearing, or is it the $i r'_t$ convention in disguise? No answer is offered here.

6. **Fixing the representative.** The canonical-quantization article establishes that the framework cannot fix the representative. The present article does not supply a selection principle either; the orbit of the connection is exactly as large as the local phases allow.

7. **Empirical contact.** As everywhere in the framework, the open question is whether any of this yields a prediction distinguishing it from standard connection theory. The honest answer at this level is no, and it is worth saying plainly rather than hedging: the construction is a restatement of standard connection theory in the algebra's notation, and the one place where it is more than a restatement — the charge-conjugation requirement of §*Does the Action Decide?* — changes nothing observable either, since the repaired Lagrangian is the standard gauged scalar one. A distinction would have to come from somewhere else in the corpus, not from this article.

## Summary

The connection and the covariant derivative produced by localizing the central phase of the biquaternion algebra are studied here as objects in their own right. The covariant derivative is the first-order operator

$$
\tilde\nabla_{\mathrm{gco},\Phi} = \tilde\nabla_\Phi +i\kappa\tilde{A}_{\Phi} = \sum_{\imath\in\{t,x,y,z\}}  e_{\imath} \tilde\nabla_{\mathrm{gco},\Phi,\imath},
\qquad
\tilde\nabla_{\mathrm{gco},\Phi,\imath} = \partial/\partial R_{\imath} +i\kappa A_{\imath},
$$

with $\tilde{A}_{\Phi} = \sum_{\imath} A_{\imath} e_{\imath} \in \mathbb{B}_{\Phi}$ the connection. It is not an element of the algebra; it is a derivation on fields, with Leibniz rule $\tilde\nabla_{\mathrm{gco},\Phi}(f\tilde{Ξ}) = f\tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ} + (\tilde\nabla_\Phi f)\tilde{Ξ}$ and commutator $[\tilde\nabla_{\mathrm{gco},\Phi,\imath},f] = \partial/\partial R_{\imath} f$, so that the connection is exactly the difference $\tilde\nabla_{\mathrm{gco},\Phi,\imath} - \partial/\partial R_{\imath} =i\kappa A_{\imath}$.

Covariance determines the connection rather than merely holding for it: the requirement $\tilde\nabla_{\mathrm{gco},\Phi,2}(\digamma_{\mathrm{cph}}\tilde{Ξ}) = \digamma_{\mathrm{cph}} \tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ}$ forces $\Omega_2 = \digamma_{\mathrm{cph}}\Omega\digamma_{\mathrm{cph}}^{-1} - (\tilde\nabla_\Phi\digamma_{\mathrm{cph}})\digamma_{\mathrm{cph}}^{-1}$, which for $\digamma_{\mathrm{cph}} = \exp(i\theta_{\mathrm{cph}})$ is the inherited law $\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi} - \tilde\nabla_\Phi\Gamma$. The connection is an orbit, not a value: it can be set to zero by a choice of representative at any single point, a gradient connection is flat, and the curvature $\tilde{F}$ is exactly the obstruction to removing it on a neighbourhood. The one-form $\sum_{\imath} A_{\imath}\,dx_{\imath}$ lies in the real-quaternion subspace and has an invariant loop integral.

The curvature is the commutator of covariant derivatives, $[\tilde\nabla_{\mathrm{gco},\Phi,\imath},\tilde\nabla_{\mathrm{gco},\Phi,\jmath}] =i\kappa F_{\imath\jmath}$, and contracts to the field strength $\tilde{F} =\frac{1}{2i\kappa}\sum_{\imath\jmath}[\tilde\nabla_{\mathrm{gco},\Phi,\imath},\tilde\nabla_{\mathrm{gco},\Phi,\jmath}]e_{\imath}^{\natural} e_{\jmath}$. Unlike $\tilde\nabla_{\mathrm{gco},\Phi,\imath}$, the commutator is an element of the algebra. The covariant square separates cleanly,

$$
\boxed{\;(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi} = \sum_{\imath\in\{t,x,y,z\}}  \tilde\nabla_{\mathrm{gco},\Phi,\imath}^{2} +i\kappa\tilde{F},
\qquad
\mathrm{Sc}((\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi}) = \sum_{\imath}  \tilde\nabla_{\mathrm{gco},\Phi,\imath}^2, \quad \mathrm{Vect}((\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi}) =i\kappa\tilde{F}\;},
$$

with the scalar part the covariant d'Alembertian and the vector part the curvature. The charged-scalar question is settled by the action rather than left open: the minimally coupled Lagrangian is real only when the conjugate factor carries the opposite charge, and its Euler–Lagrange equation is the scalar projection, so a charged scalar obeys the covariant d'Alembertian and the curvature term of the full square is not an equation for it. What that leaves is the charge-conjugation insertion itself, which the algebra's conjugation does not supply, and the non-abelian extension, which still needs a reality condition selecting a compact algebra — $\mathfrak{su}(2)$ being the only compact simple candidate inside $\mathbb{B}$. The connection of this article is one-sided and abelian; it is not the two-sided gravitational connection of the curved-spacetime article.

The identity is the square of the chiral pair $\tilde\nabla_{\mathrm{gco},\Phi}\tilde{Ξ}_{R} = 2\pi\nu_m\tilde{Ξ}_{L}$, $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}\tilde{Ξ}_{L} = 2\pi\nu_m\tilde{Ξ}_{R}$, written on the algebra by left multiplication, the second member being the first on the conjugate field. It is not the square of a single field: the conjugate derivative applied to $\tilde\nabla_\Phi\tilde{Ξ} = 2\pi\nu_m\tilde{Ξ}$ returns $\Box_\Phi\tilde{Ξ} = m(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}$, a second-order equation in two objects rather than one, and $\tilde\nabla_\Phi^2$ is not $\Box_\Phi$ — its scalar part is $\partial^2/\partial R_t^2-\Delta_\Phi$ against the $\partial^2/\partial R_t^2+\Delta_\Phi$ of $\Box_\Phi$, and its vector part does not vanish. That is why the mass couples two fields.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_{\imath}^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{B}_{\Phi}, \mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_{H}$ | Real-quaternion subspace |
| $\mathbb{B}_{C} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Centre of the algebra; source of the abelian symmetry group |
| $\tilde\nabla_\Phi = e_t\partial/\partial R_t + \sum_{\imath\in\{x,y,z\}}\vec e_{\imath}\,\partial/\partial R_{\imath}$ | Biquaternionic gradient |
| $(\tilde\nabla_\Phi)^{\natural} = e_t\partial/\partial R_t - \sum_{\imath\in\{x,y,z\}}\vec e_{\imath}\,\partial/\partial R_{\imath}$ | Quaternion-conjugate gradient |
| $\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= (\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi$ | d'Alembertian |
| $\tilde\nabla_\Phi^2=\frac{\partial^2}{\partial R_t^2}-\Delta_\Phi+2\sum_{\imath\in\{x,y,z\}}\vec e_{\imath}\frac{\partial^2}{\partial R_t\partial R_{\imath}}$ | Square of the gradient; not scalar, and not $\Box_\Phi$ |
| $\Delta_\Phi=\sum_{\imath\in\{x,y,z\}}\partial^2/\partial R_{\imath}^2$ | Laplacian in the three vector coordinates |
| $\tilde{A}_{\Phi} = \sum_{\imath} A_{\imath} e_{\imath} = i\,a'_t\,e_t + \vec A$ | Connection / potential biquaternion, in $\mathbb{B}_{\Phi}$ |
| $\Gamma$ | Real scalar phase function |
| $\digamma_{\mathrm{cph}} = \exp(i\theta_{\mathrm{cph}})$ | Local central phase (abelian) |
| $\kappa$ | Coupling constant (charge), not fixed by the algebra |
| $\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi} - \tilde\nabla_\Phi\Gamma$ | Local transformation of the connection |
| $m$ | Mass of the parent's Dirac field |
| $\tilde\nabla_{\mathrm{gco},\Phi} = \tilde\nabla_\Phi +i\kappa\tilde{A}_{\Phi} = \sum_{\imath}  e_{\imath} \tilde\nabla_{\mathrm{gco},\Phi,\imath}$ | Covariant derivative |
| $\tilde\nabla_{\mathrm{gco},\Phi,\imath} = \partial/\partial R_{\imath} +i\kappa A_{\imath}$ | Components; $\partial/\partial R_t = \partial/\partial(i r'_t)$ |
| $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} = (\tilde\nabla_\Phi)^{\natural}+i\kappa\tilde{A}_{\Phi}^{\natural}$ | Quaternion conjugate of $\tilde\nabla_{\mathrm{gco},\Phi}$ |
| $\tilde{A}_{\Phi}^{\natural}$ | Quaternion conjugate of the connection, by *Product and Form Conventions* |
| $[\tilde\nabla_{\mathrm{gco},\Phi,\imath}, f] = \partial/\partial R_{\imath} f$ | Derivation property |
| $S = \mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi})$, $S_2 = S - \Box_\Phi\Gamma$ | Scalar part; pure gradient |
| $\tilde{F} = \mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}) = \frac{1}{2}\sum_{\imath\jmath}F_{\imath\jmath}e_{\imath}^{\natural} e_{\jmath}$ | Field strength = curvature, invariant |
| $F_{\imath\jmath} = \partial/\partial R_{\imath} A_{\jmath} - \partial/\partial R_{\jmath} A_{\imath}$ | Abelian curvature components |
| $[\tilde\nabla_{\mathrm{gco},\Phi,\imath}, \tilde\nabla_{\mathrm{gco},\Phi,\jmath}] =i\kappa F_{\imath\jmath}$ | Curvature as commutator |
| $\sum_{\imath} \tilde\nabla_{\mathrm{gco},\Phi,\imath}^2 = \mathrm{Sc}((\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi})$ | Covariant d'Alembertian |
| $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural} \tilde\nabla_{\mathrm{gco},\Phi} = \sum_{\imath}  \tilde\nabla_{\mathrm{gco},\Phi,\imath}^2 +i\kappa\tilde{F}$ | Covariant square identity |
| $e_t^{\natural} = e_t, e_{\imath}^{\natural} = -\vec e_{\imath}$ | Conjugate basis |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum. Not to be confused with the coupling, written $\lambda$ below |
| $\lambda = i\kappa$ | Coupling coefficient of the covariant derivative; $i$ times the inverse length per unit potential |
| $D_{\imath} = \partial/\partial R_{\imath}+\lambda A_{\imath}$ | Compact name for the covariant derivative components of §*Does the Action Decide?* |
| $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Scalar-part reading of the plain form on the informational sector: the pairing $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2) = \langle\tilde Q_1,\tilde Q_2\rangle_{*}$ of *Four-Vectors and the Interval*, read on $\mathbb{B}_{\Psi}$ |

## Further Reading

- [The Minimal Coupling in Biquaternionic Form](the-minimal-coupling-in-biquaternionic-form.html) — the origin of the connection, the transformation law, the covariance, and the curvature identity inherited here.
- [The Relativistic Particle and the Lagrangian: The Stationary-Action Principle](the-relativistic-particle-and-the-lagrangian-the-stationary-action-principle.html) — the Lagrangian that §*Does the Action Decide?* minimally couples and varies, with the sign convention used there.
- [Noether's Theorem in Biquaternionic Form](noethers-theorem-in-biquaternionic-form.html) — the current whose gauged version is the natural companion to this article, and the charge density $J_t=ic\rho$ whose reality is the same cancellation as the one-form's.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html) — the potential, the field strength, the scalar part $S$, and the Maxwell equation.
- [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html) — the invariant content of $\tilde{F}$, which this article uses but does not develop.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) — the massless field equation $\tilde\nabla_\Phi\tilde{Ξ} = 0$ and the minimal-coupling question.
- [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html) — the coupled Dirac equation, the left/right matter-representation question, and the companion that names the covariant-derivative article.
- [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html) — the free scalar equation $(\Box_\Phi - 4\pi^{2}\nu_m^{2})\tilde{Ξ} = 0$ whose covariantization is the gap discussed here.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) — the covariant derivative read on the two parts named by the subscript, and the charge-operator representation.
- [Canonical Quantization of the Biquaternion Maxwell Field](canonical-quantization-of-the-biquaternion-maxwell-field.html) — the framework's inability to fix the representative, which bounds the orbit treated here.
- [Four-Vectors and the Interval](four-vectors-and-the-interval.html) and [States, Observables and the Born Weight](states-observables-and-the-born-weight.html) — the sector decomposition, the four-vectors, and the pairing formula.
- [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html) — the two-sided gravitational connection, distinct from the one-sided connection of this article, and the record of the Lorentz-making local / Euler–Lagrange ambiguity.
- J. Fredsted, "Obtaining consistent Lorentz gauging for a gravitationally coupled fermion," arXiv:1906.12200v3 [physics.gen-ph] (2019), for the external result recorded in *The Connection and the Gravitational Connection*: the non-commutativity of internal-gauge localization (which this article's abelian construction enjoys) with the Euler–Lagrange variation when the symmetry group is the Lorentz group, and the world-index formalism in which they commute again. Cited as an external claim and not adopted.
- J. Fredsted, "Spinor fields without Lorentz frames in curved spacetime using complexified quaternions," arXiv:0811.1357v4 [math-ph] (2009), for the external construction, also recorded in *The Connection and the Gravitational Connection*, in which one algebra-valued connection carries both the local $\mathrm{U}(1)$ and the Lorentz connection; cited as evidence that the two connections of this section are not forbidden to be one, with no reason to identify them asserted here.
- [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html) — the multiplication rule, the conjugations, and the centre.
