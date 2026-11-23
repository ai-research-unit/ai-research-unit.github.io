# __The Lagrangian and Linearised Gravity__

## Introduction

The question, and the answer's shape. *Linearized Gravity in Biquaternionic Form* writes the linearised Einstein equation for a metric perturbation and exhibits its gauge freedom, its linearised curvature and its two polarisations. This article asks the family's question about it: is there an action whose Euler–Lagrange equation is that equation, what is its variation, and what does the variational principle add? The answer is yes at the level of the quadratic expansion of the Einstein–Hilbert action, and — this is the article's honest core — no at the level of a single biquaternion, because the perturbation is not one.

Three results. The action is the second variation of the Einstein–Hilbert action, a quadratic form in the perturbation with two derivatives. Its variation gives the linearised Einstein equation, its time-time component is a constraint and not an evolution equation, and its gauge orbit is the diffeomorphism's linearisation. The count that follows is ten minus four minus four, which is two.

Where the biquaternion enters and where it does not. The parent's structural finding is that the metric perturbation is carried by a frame perturbation $\delta\tilde E_{\Phi,\imath}$ — a family of four elements of $\mathbb{B}_\Phi$ — and not by the single element $\sum h_{\imath\jmath}\varepsilon_{\imath}\varepsilon_{\jmath}^{\natural}$, which is blind to the transverse-traceless part. So the action below is written on the frame perturbation, and its biquaternionic form is exact there. What the corpus does not have is the *non-linear* completion, the parent's stated gap, and this article does not close it.

What is not done. Nothing is quantised. There is no graviton operator, no Fock space, no propagator, no loop and no statement about renormalisability. The gravity articles this family draws on are classical, and the corpus's separate quantisation programme — *Canonical Quantization of the Biquaternion Graviton Field* — is a different construction and not this family's; the bridge article records what a quantisation would need.

## Conventions

**The conventions are the parent's, with one exception.** The interval's array is $\delta_{\imath\jmath}=\mathrm{diag}(-1,+1,+1,+1)$, and it is the one place in this article where a metric other than the corpus's $\delta_{\imath\jmath}=(1,1,1,1)$ is used: it is the interval's array, kept until the article is rewritten in the corpus's. It is in the length units of the material sector, with the interval $-c^{2}\mathrm{d}r'{}^{2}_{t}+\mathrm{d}r_x^{2}+\mathrm{d}r_y^{2}+\mathrm{d}r_z^{2}$. The perturbation is $h_{\imath\jmath}$, symmetric, with $\lvert h_{\imath\jmath}\rvert\ll1$; the trace is $h=\sum_{\imath}\delta_{\imath\imath}h_{\imath\imath}$ and the trace-reversed variable is $\bar h_{\imath\jmath}=h_{\imath\jmath}-\tfrac12\delta_{\imath\jmath}h$. A repeated low index is summed with the weight $\delta_{\imath\imath}$ of that index, so that $\partial_{\imath} h_{\imath\jmath}\partial_{\imath} h_{\imath\jmath}=\sum_{k,\imath,\jmath}\delta_{\rho\rho}\delta_{\imath\imath}\delta_{\jmath\jmath}(\partial_{\imath} h_{\imath\jmath})^{2}$; no index is raised.

The frame perturbation is $\delta\tilde E_{\Phi,\imath}\in\mathbb{B}_\Phi$, related to the metric by $h_{\imath\jmath}=\langle\varepsilon_{\imath},\delta\tilde E_{\Phi,\jmath}\rangle_{\natural}+\langle\delta\tilde E_{\Phi,\imath},\varepsilon_{\jmath}\rangle_{\natural}$, the parent's dictionary. The gravitational constant enters once, through $\kappa^{2}=16\pi G/c^{4}$, and this article does not re-derive its normalisation: the Einstein–Hilbert normalisation is the gravity articles' and is quoted.

The literature's letters. Where the standard form of the action is quoted, it is quoted in the tensor dictionary that the parent supplies, and every step below is a step in that dictionary. The biquaternionic translation of the quadratic form is exact on the frame perturbation; the translation of the *non-linear* action is not, and that is the gap.

## The Action in Element Form

The action is the quadratic expansion, and it is the second variation of the Einstein–Hilbert term. Write the Einstein–Hilbert action with the cosmological term absent and expand $\sqrt{-g}R$ to second order in $h$. The first-order term is a total derivative on shell and drops; the second-order term is the quadratic action,

$$
S^{(2)}=\frac{1}{2\kappa^{2}}\int\mathrm{d}^{4}x\;\Bigl\{-\tfrac12\,\partial_{\imath} h_{\imath\jmath}\,\partial_{\imath} h_{\imath\jmath}+\partial_{\imath} h_{\imath\jmath}\,\partial_{\jmath} h-\partial_{\imath} h_{\imath\jmath}\,\partial_{\imath} h_{k\jmath}+\tfrac12\,\partial_{\imath} h\,\partial_{\imath} h\Bigr\},
$$

the Fierz–Pauli form with the mass set to zero. In the trace-reversed variable the same functional is one line shorter,

$$
S^{(2)}=\frac{1}{2\kappa^{2}}\int\mathrm{d}^{4}x\;\Bigl\{\tfrac12\,\partial_{\imath}\bar h_{\imath\jmath}\,\partial_{\imath}\bar h_{\imath\jmath}-\tfrac14\,\partial_{\imath}\bar h\,\partial_{\imath}\bar h\Bigr\}
+\text{(the de Donder total derivative)},
$$

because the trace-reversed variable absorbs the two cross terms up to a surface term. The two displays are one action written twice, and the second is the one the variation uses.

Its reality. In the frame perturbation the quadratic form is $\mathrm{Re}\,\mathrm{Sc}$ of a product of two derivatives of $\delta\tilde E_{\Phi}$, with the metric's signature carried by the frame; each factor is in $\mathbb{B}_\Phi$ and the pairing is real. That is the biquaternionic statement of the reality of $S^{(2)}$, and it is exact on the frame perturbation.

Its normalisation, quoted. The factor $1/2\kappa^{2}$ is the expansion of $c^{4}/16\pi G$; it is the same constant that makes the Newtonian limit come out and it is fixed in the gravity articles. This article uses it and does not re-derive it, and says so because a reader could otherwise expect a derivation.

**Why a quadratic action and not a linear one.** A linear action in $h$ would have a first variation that does not vanish at $h=0$, and $h=0$ is flat space, a solution. So the expansion starts at the second order, and the linearised theory's action is necessarily quadratic. That is the structural reason the graviton's action looks like a free field's and not like the Maxwell action's in $A$: it is a fluctuation's action.

## The Variation

One variation, two integrations by parts, and the linearised Einstein tensor. Varying $\bar h_{\imath\jmath}$ in the second display,

$$
\delta S^{(2)}=\frac{1}{2\kappa^{2}}\int\mathrm{d}^{4}x\;\Bigl\{\partial_{\imath}\bar h_{\imath\jmath}\,\partial_{\imath}\delta\bar h_{\imath\jmath}-\tfrac12\,\partial_{\imath}\bar h\,\partial_{\imath}\delta\bar h\Bigr\},
$$

and two integrations by parts move the derivatives onto the perturbation. The result is

$$
\delta S^{(2)}=-\frac{1}{2\kappa^{2}}\int\mathrm{d}^{4}x\;\delta\bar h_{\imath\jmath}\Bigl(\Box\bar h_{\imath\jmath}-\delta_{\imath\jmath}\Box\bar h-\partial_{\imath}\partial_{\imath}\bar h_{k\jmath}-\partial_{\jmath}\partial_{\imath}\bar h_{k\imath}+\delta_{\imath\jmath}\partial_{\imath}\partial_\rho\bar h_{k\rho}\Bigr),
$$

whose bracket is the linearised Einstein tensor in the trace-reversed variable, up to the factor that the trace reversal contributes. Stationarity gives $\delta G_{\imath\jmath}=0$, the parent's equation.

The boundary term. The action carries two derivatives and the surface term is a bilinear in $\partial\delta\bar h$; it is killed by holding both the perturbation and its normal derivative fixed, which is the standard condition for a second-order action and the same one the Klein–Gordon article uses.

What the variation gives that the equation does not. The Bianchi identity. The bracket's divergence vanishes identically, because it is built from a diffeomorphism-invariant functional; so the equation's left side is conserved without any use of the equation. In the parent's language, the linearised Bianchi identity is the statement that the gauge symmetry of the action has a Noether identity behind it, and the variational derivation makes that visible in one line.

**What it does not give.** The non-linear terms. The same procedure applied to the exact action gives the exact Einstein equation, but the expansion truncated at second order in $h$ cannot produce the terms of order $h^{2}$ in the equation, and the parent's gap is exactly there.

## The Constraints the Action Imposes

The time-time equation is a constraint. Of the ten equations $\delta G_{\imath\jmath}=0$, the $\mu=\jmath=0$ component carries no second time derivative of $h_{ij}$: it is

$$
\partial_j\partial_{\imath}\bigl(h_{j\imath}-\delta_{j\imath}h_{ll}\bigr)+\text{(terms with one time derivative)}=0 ,
$$

a condition on the initial data at every time. That is Gauss's law's counterpart: the field's temporal component is not dynamical, and the equation that would determine it is a constraint instead.

The gauge orbit. The action is invariant under the linearised diffeomorphism $h_{\imath\jmath}\mapsto h_{\imath\jmath}-\partial_{\imath}\zeta_{\jmath}-\partial_{\jmath}\zeta_{\imath}$, equivalently $\bar h_{\imath\jmath}\mapsto\bar h_{\imath\jmath}-\partial_{\imath}\zeta_{\jmath}-\partial_{\jmath}\zeta_{\imath}+\delta_{\imath\jmath}\partial_{\imath}\zeta_{\imath}$. Four functions, hence four directions in the kernel of the map from perturbation to linearised curvature.

The count. Ten components; four gauge directions; four constraints (the time-time and time-space equations, which are four conditions and not evolution equations); two remaining. The two are the transverse-traceless polarisations, and the parent's structural finding — that the single-biquaternion carrier is blind to exactly that part — is the statement that the algebra's naive carrier holds the trace and not the physics.

**What the constraints are not.** They are not the de Donder condition. The de Donder condition $\partial_{\imath}\bar h_{k\imath}=0$ is a *gauge choice*, used above to shorten the variation; the constraints are the equations' own content and hold in every gauge. Mixing the two is the standard error, and the article separates them because the count depends on it.

## The Structural Consequence: The Count Needs Both, and the Algebra Sees Only One

The claim. The linearised theory's two degrees of freedom come from ten minus four minus four, and the algebra's single-biquaternion carrier holds the trace's part of the ten and not the transverse-traceless part. So the biquaternionic action must be written on the frame perturbation, and the single-element action is not merely inconvenient — it is blind.

The hand check. Take $\sum_{\imath\jmath}h_{\imath\jmath}\varepsilon_{\imath}\varepsilon_{\jmath}^{\natural}$. The parent computes it: it equals $h\,e_t$, the trace times the time unit. A transverse-traceless perturbation has $h=0$, so its single-element image is zero, so any action written in that element assigns it zero action — including the two physical polarisations. That is a one-line refutation of the naive carrier, and it is why the action above is written on $\delta\tilde E_{\Phi,\imath}$.

What the frame perturbation holds. Sixteen components, of which six are the infinitesimal local Lorentz transformations and ten are the metric perturbation; the action is invariant under the six, so it is a functional of the ten. The biquaternionic writing is therefore exact, with the six-dimensional kernel an internal gauge freedom of the frame and not a physical sector.

**What the consequence forbids.** It forbids writing the graviton's action as a functional of one element, in the way the Proca action is a functional of one element. The vector case works because a vector's data is one element; the rank-two symmetric case does not, because the trace is the only part a single element can see, and the physics is in the rest.

## The Noether Currents and the Sign of the Charge

**There is no charge and there is a stress, and the stress is not a tensor.** The linearised action is invariant under diffeomorphisms, not under a phase rotation, so there is no conserved charge and no sign of a charge to fix. What translation invariance gives is the energy–momentum of the perturbation, and the honest statement is that it is gauge-dependent: a coordinate change moves energy between the perturbation and the background.

Why it is gauge-dependent. The perturbation is defined relative to a background, and the split of the metric into background plus perturbation is not invariant under the diffeomorphisms the action is invariant under. So the canonical stress computed from $S^{(2)}$ changes under a gauge transformation, and only its average over a region larger than the wavelength — the Isaacson stress — is meaningful.

What survives without averaging. The sign, in the sense that the energy of a transverse-traceless wave is positive for either polarisation, and the flux, in the sense that the averaged Poynting-like quantity is positive and directed along the wave's propagation. Those two statements are the content of "gravity waves carry positive energy", and the corpus can state them while admitting that the local density is not a tensor.

The contrast with the Maxwell article. There the stress is a tensor and the energy density is positive pointwise. Here it is not, and the difference is not a defect of the calculation: it is the statement that the gravitational field's energy is not localisable in a background-dependent split. The article records the contrast rather than hiding it.

## What the Principle Adds and What It Relabels

Adds. The variational derivation of the linearised equation, the Bianchi identity as a Noether identity, and the count as a consequence of an action's symmetries rather than of a list of conditions. Those are genuine gains: the constraint and the orbit are separated by their origin, and the count follows.

Relabels. The parent's equation, its gauge freedom, its curvature and its polarisations. Nothing predictive is added, and no constant is determined that the gravity articles did not already fix.

**What it does not reach, and this family does not either.** Two things. The non-linear completion: the parent names it as the gap, and the quadratic truncation cannot supply it. And the quantisation: a graviton's Fock space, its propagator and its ultraviolet behaviour are not in the corpus, and the bridge article states what would be needed. The first gap is the corpus's own subject; the second is the boundary the corpus shares with every other member of the family.

## Summary

The linearised gravitational field's action is the second variation of the Einstein–Hilbert action, a quadratic form with two derivatives, given above in both the metric and the trace-reversed variables. Its variation gives the linearised Einstein equation and the Bianchi identity; its time-time component is a constraint; its gauge orbit is the linearised diffeomorphism; and the count is ten minus four minus four, which is two. The biquaternionic writing is exact on the frame perturbation and blind on a single element, which is the parent's structural finding read from the action side. The non-linear completion and the quantisation are both absent.

$$
S^{(2)}=\frac{1}{2\kappa^{2}}\int\mathrm{d}^{4}x\;\Bigl\{\tfrac12\,\partial_{\imath}\bar h_{\imath\jmath}\,\partial_{\imath}\bar h_{\imath\jmath}-\tfrac14\,\partial_{\imath}\bar h\,\partial_{\imath}\bar h\Bigr\},
\qquad
\bar h_{\imath\jmath}=h_{\imath\jmath}-\tfrac12\delta_{\imath\jmath}h,
\qquad
\kappa^{2}=\frac{16\pi G}{c^{4}}.
$$

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\delta_{\imath\jmath}$ | The interval's array, $\mathrm{diag}(-1,+1,+1,+1)$; an exception |
| $h_{\imath\jmath}$ | Metric perturbation, symmetric, small |
| $h=\sum_{\imath}\delta_{\imath\imath}h_{\imath\imath}$ | Trace |
| $\bar h_{\imath\jmath}=h_{\imath\jmath}-\tfrac12\delta_{\imath\jmath}h$ | Trace-reversed perturbation |
| $\delta\tilde E_{\Phi,\imath}$ | Frame perturbation, the exact carrier |
| $\zeta_{\imath}$ | Gauge parameter of the linearised diffeomorphism |
| $\kappa^{2}=16\pi G/c^{4}$ | Gravitational coupling |
| $S^{(2)}$ | Quadratic (linearised) action |
| $\delta G_{\imath\jmath}$ | Linearised Einstein tensor |

## Further Reading

- *Linearized Gravity in Biquaternionic Form*, the parent, for the dictionary, the gauge freedom and the polarization content.
- *The Einstein Field Equations in the Biquaternion Framework: The Linearised Dictionary and the Non-Linear Gap*, for the gap this article does not close.
- *Canonical Quantization of the Biquaternion Graviton Field*, for the corpus's quantisation of the linearised field, which is a different programme and is not this family's.
- *The Lagrangian and the Electromagnetic Field*, for the contrast between a localisable stress and this one.
- Charles W. Misner, Kip S. Thorne and John A. Wheeler, *Gravitation*, for the quadratic action and the Isaacson stress.
- Robert M. Wald, *General Relativity*, for the constraint structure and the initial-value formulation.
