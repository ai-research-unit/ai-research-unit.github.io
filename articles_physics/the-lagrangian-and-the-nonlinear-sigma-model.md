# __The Lagrangian and the Nonlinear Sigma Model__

## Introduction

This article writes the nonlinear sigma model as an extremum of an action in the algebra, and reads what the action's structure gives. It is the action-first companion of *The Nonlinear Sigma Model in Biquaternionic Form*, which states the target geometry and the power counting as facts about a known model; this article asks the prior question, what functional has the sigma-model equation as its stationary condition, and what the algebra contributes to the answer.

The equation. The parent's equation is

$$
\frac{\partial}{\partial R_{\imath}}\Bigl(\tilde U^{\natural}\frac{\partial \tilde U}{\partial R_{\imath}}\Bigr)=0 ,
\qquad
\tilde U\in\mathbb{H}^1_{\mathbb{B}},
\qquad
\tilde U\tilde U^{\natural}=e_t ,
$$

the conservation of the Maurer–Cartan current of a group-valued field. The article asks what action has this equation as its Euler–Lagrange condition.

Three things are established.

*First, the action.* With $\tilde U$ varied subject to $\tilde U\tilde U^{\natural}=e_t$, and with $\mathrm{Sc}(\cdot)$ the scalar part,

$$
S[\tilde U]=-\frac{f^2}{2}\int d^4r\;\mathrm{Sc}\bigl(\bar j_{\imath} j_{\imath}\bigr),
\qquad
j_{\imath}=\tilde U^{\natural}\frac{\partial \tilde U}{\partial R_{\imath}},
\qquad
f=f_\pi,
$$

the Euler–Lagrange condition is exactly the conservation of $j_{\imath}$. The action is the unique term with two derivatives that is invariant under $\tilde U\mapsto g_L\tilde U g_R^{*}$, and the coefficient $f^2$ is the only free number in it.

*Second, the constraint is the model.* The unit-norm condition on $\tilde U$ is not imposed after the variation; it is what makes the action nonlinear. Varying freely inside the constraint surface gives three equations for three Goldstone fields, and the fourth direction of $\mathbb{H}$ is removed by the constraint rather than by a choice of representative.

*Third, the action's only content is the derivative expansion.* Every invariant of the target that can be written is a power of $\partial\tilde U$, so the classical action is the first term of a series whose successive terms are suppressed by $f$. That is why the model is predictive below $4\pi f$ and silent above it.

What is not new. The model, its target, its current and its power counting are standard. The physics is imported whole. What the algebra supplies is the carrier: the target is a submanifold of $\mathbb{H}$, the metric on it is the biquaternion norm, and the current is an algebra-valued one-form whose flatness is a commutator identity of the algebra.

## Conventions

The conventions are restated here so that every sign below is checkable from this page. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$, $\vec e_{\imath}^{2}=-e_t$ for $k=x,y,z$, and central scalar imaginary $i$. The material sector is $\mathbb{B}_\Phi$; the group-valued field takes values in the unit real quaternions $\mathbb{H}^1_{\mathbb{B}}=\{\tilde U:\tilde U\tilde U^{\natural}=e_t\}$.

The two products used. $\mathrm{Sc}(X)$ is the coefficient of $e_t$ in $X$; $\langle X\rangle_\natural=\mathrm{Sc}(X X^{\natural})$ is the Minkowski square of $X$. The spatial sum $\sum_{\imath}$ runs over $t,x,y,z$ with the corpus's sign rule $\sum_{\imath} X_{\imath} X_{\imath}=X_t^{2}-\sum_j X_j^{2}$.

The gradient. $\tilde\nabla_\Phi$ is the corpus's gradient, $\tilde\nabla_\Phi=e_t\partial/\partial r'_t+\sum_j\vec e_j\partial/\partial R_j$, and $\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$ is the central scalar d'Alembertian. The volume element is $d^4r=c\,dr'_t\,dr_x\,dr_y\,dr_z$.

The sign convention. The overall sign of the action is fixed once by requiring that the energy computed from it be positive, exactly as in the Skyrme article; with that sign the time derivative enters the kinetic term with a positive coefficient and the spatial gradients with a negative one. Every sign below follows from it and is not re-chosen.

## The Action in Element Form

The field. The sigma-model field is the chiral field of the pion,

$$
\tilde U=\exp\!\left(\frac{\vec\pi}{f}\right),
\qquad
\vec\pi=\sum_{\imath\in\{x,y,z\}} \pi_{\imath}\vec e_{\imath} ,
\qquad
\vec\pi^{\natural}=-\vec\pi ,
$$

which is a unit real quaternion because $\vec\pi$ is anti-Hermitian and the exponential of an anti-Hermitian quaternion has unit norm. In closed form,

$$
\tilde U=\cos\frac{|\pi|}{f}\,e_t+\frac{\sin(|\pi|/f)}{|\pi|}\,\vec\pi ,
\qquad
|\pi|=\sqrt{\sum_{\imath\in\{x,y,z\}}\pi_{\imath}\pi_{\imath}},
$$

the second form showing that the three $\pi_{\imath}$ are coordinates on the group and not linear fields.

The current. The Maurer–Cartan form is

$$
j_{\imath}=\tilde U^{\natural}\frac{\partial \tilde U}{\partial R_{\imath}}\in\mathfrak{su}(2)\subset\mathbb{B}_\Phi ,
$$

and it is flat,

$$
\frac{\partial j_{\jmath}}{\partial R_{\imath}}-\frac{\partial j_{\imath}}{\partial R_{\jmath}}+[j_{\imath},j_{\jmath}]=0 ,
$$

which is an identity for any group-valued field and holds for no other algebra-valued one-form. Flatness is what makes $j_{\imath}$ a pure connection, and it is the source of every distinctive property of the model below.

**The action at two derivatives.** The one invariant at this order is the norm of the current,

$$
\boxed{\;S[\tilde U]=-\frac{f^2}{2}\int d^4r\;\mathrm{Sc}\bigl(\bar j_{\imath} j_{\imath}\bigr)\;}
$$

with $\bar j_{\imath}=-j_{\imath}$ because $j_{\imath}$ is anti-Hermitian, so that $\mathrm{Sc}(\bar j_{\imath} j_{\imath})=-\mathrm{Sc}(j_{\imath} j_{\imath})=|j_{\imath}|^2\ge 0$ and the integrand is positive for the corpus's sign rule. Expanding to second order in $\vec\pi$,

$$
j_{\imath}=\frac{1}{f}\frac{\partial \vec\pi}{\partial R_{\imath}}+O(\pi^2),
\qquad
-\frac{f^2}{2}\mathrm{Sc}(j_{\imath} j_{\imath})=-\frac12\sum_{\imath\in\{x,y,z\}}\frac{\partial \pi_{\imath}}{\partial R_{\imath}}\frac{\partial \pi_{\imath}}{\partial R_{\imath}}+O(\pi^4),
$$

so that the quadratic part is the canonical kinetic term of three real fields with coefficient exactly one and no free parameter. The constant $f$ has cancelled between the coefficient and the current, and that cancellation is the statement that $f$ is the decay constant and not a coupling.

Why no potential term. A term $V(\tilde U)$ would have to be invariant under $\tilde U\mapsto g_L\tilde U g_R^{*}$, and the only invariant function of a unit quaternion is a constant. The absence of a potential is therefore not a choice of the model but a consequence of the target: on $\mathbb{H}^1$ there is no invariant to build one from, and a mass term for $\vec\pi$ requires a source outside the chiral group, which is the explicit breaking the Goldstone article treats.

The pairing. The pairing is the real scalar part, and it is forced. The integrand $\mathrm{Sc}(\bar j_{\imath} j_{\imath})$ is real because $\bar j_{\imath} j_{\imath}$ is the negative of a Hermitian norm: $j_{\imath}$ is anti-Hermitian, so $j_{\imath}^{\dagger}=-j_{\imath}$ and $\mathrm{Sc}(\bar j_{\imath} j_{\imath})=-\mathrm{Sc}(j_{\imath}^{\dagger}j_{\imath})=-\langle j_{\imath}\rangle_\natural$, a real number. No separate reality condition is needed, and no imaginary part survives the sum over $\mu$.

Why the pairing cannot be $\mathrm{Sc}(j_{\imath} j_{\imath})$. That form is the negative of the one above only when $j_{\imath}$ is anti-Hermitian, which it is, so the two differ by a sign and not by a defect. The genuine alternative, $\mathrm{Re}\,\mathrm{Sc}(j_{\imath} j_{\imath})$ without the conjugate, would fail to be invariant under $\tilde U\mapsto g_L\tilde U g_R^{*}$ because the left and right factors do not commute with $j_{\imath}$ in the same order; the conjugated pairing is the one that survives, and this is the same selection that fixes the Dirac bilinear in the element articles.

The type of the coefficient. The coefficient is a squared decay constant, real and dimensionful. $f^2$ has dimension of mass squared, is real by construction, and its value is fixed by the pion decay constant $f_\pi=2.086\times10^{-11}\ \mathrm{J}$ in the corpus's normalization. It is not a coupling: it multiplies the whole action and cancels in the equation of motion, exactly as a coupling would not.

What that means for the count. Because $f$ cancels from the equation, the classical content of the model is $f$-independent, and $f$ enters only when the field is normalized canonically — that is, only in the interactions. This is the structural fact behind the statement that the sigma model has one parameter and no coupling.

The selection rule. The selection rule is invariance under the chiral group, and it leaves one term. The group acts by $\tilde U\mapsto g_L\tilde U g_R^{*}$ with constant unit quaternions; the current transforms as $j_{\imath}\mapsto g_R^{*}j_{\imath} g_R$, so $\mathrm{Sc}(\bar j_{\imath} j_{\imath})$ is invariant because the trace is cyclic. Of all the invariants that can be written with two derivatives, only this one exists at leading order, and the derivative expansion of the next section is the statement that all the others carry four or more.

What reality does not buy. Reality does not buy a potential, a mass, or a coupling. The action is real, and its reality is a statement about the integrand and not about the physics. Three things the reality of the action does not supply, stated so that the boundary is visible:

- *No mass for $\vec\pi$.* A mass term is not invariant under the shift $\vec\pi\to\vec\pi+\text{const}$, and the action has no place to put one.
- *No interaction strength.* The coefficient is $f^2$ and cancels; the strength of the four-pion vertex is fixed by $f$ in the canonical normalization and is not a new number.
- *No quantisation.* The action is classical. Its path integral is written in the companion article and is not part of this one.

## The Variation: The Current Is Conserved, and That Is the Equation

The variation. Write $\delta\tilde U=\tilde U\,\tilde\alpha$ with $\tilde\alpha\in\mathfrak{su}(2)$ vanishing at the boundary; the constraint $\tilde U\tilde U^{\natural}=e_t$ forces $\tilde\alpha$ anti-Hermitian, so the variation runs over the three directions of $\mathfrak{su}(2)$ and not over four. Then

$$
\delta j_{\imath}=\frac{\partial\tilde\alpha}{\partial R_{\imath}}+[j_{\imath},\tilde\alpha] ,
$$

which is the covariant derivative of $\tilde\alpha$ with $j_{\imath}$ as connection.

The variation of the action. Substituting and integrating by parts,

$$
\delta S=-f^2\int d^4r\;\mathrm{Sc}\Bigl(\bar j_{\imath}\Bigl(\frac{\partial\tilde\alpha}{\partial R_{\imath}}+[j_{\imath},\tilde\alpha]\Bigr)\Bigr)
=f^2\int d^4r\;\mathrm{Sc}\Bigl(\tilde\alpha\,\frac{\partial \bar j_{\imath}}{\partial R_{\imath}}\Bigr),
$$

where the commutator term drops because $\mathrm{Sc}(\bar j_{\imath}[j_{\imath},\tilde\alpha])$ is a trace of a commutator, and the boundary term drops because $\tilde\alpha$ vanishes there. The bracket vanishes for every $\tilde\alpha$ in the three-dimensional variation space, hence

$$
\boxed{\;\frac{\partial \bar j_{\imath}}{\partial R_{\imath}}=0\;}
\qquad\Longleftrightarrow\qquad
\frac{\partial}{\partial R_{\imath}}\Bigl(\tilde U^{\natural}\frac{\partial \tilde U}{\partial R_{\imath}}\Bigr)=0 ,
$$

which is the parent's equation. The equation and the conservation law are the same statement, and that coincidence is not an accident of this model: it is what flatness buys, because a flat connection's divergence is the equation of motion of its own norm.

The spatial form, to make it checkable. In components the equation reads $\partial_{\imath} j_{\imath}=0$ with the corpus's sign rule, so the time component is conserved with a plus sign and each spatial component with a minus sign; a static configuration therefore obeys $\sum_j\partial_j j_j=0$, and a configuration constant in space obeys $\partial_t j_t=0$. Both are immediate from the boxed form.

## The Constraints the Action Imposes: The Field Is Group-Valued

**The constraint is $\tilde U\tilde U^{\natural}=e_t$, and it removes one of four components.** The field lives on a three-dimensional surface inside a four-dimensional algebra. The variation therefore runs over three directions, and the four equations that a free variation would give reduce to three independent ones; the fourth is the constraint differentiated along the orbit.

What the constraint does to the equation. Differentiating $\tilde U\tilde U^{\natural}=e_t$ gives $\partial_{\imath}\tilde U\tilde U^{\natural}+\tilde U\partial_{\imath}\tilde U^{\natural}=0$, so $\partial_{\imath}\tilde U^{\natural}=-\tilde U^{\natural}\partial_{\imath}\tilde U\tilde U^{\natural}$ and the current satisfies $j_{\imath}^{\natural}=-j_{\imath}$ automatically. The anti-Hermiticity used in the variation is therefore not assumed; it is the constraint's consequence.

The degree-of-freedom count. Four components of $\mathbb{H}$ minus one constraint gives three fields, and three is the dimension of $\mathrm{SU}(2)$, which is the target's dimension. The count of degrees of freedom, the dimension of the target and the number of Goldstone bosons of the broken chiral group are the same number read three ways, and the equality is the content of Goldstone's theorem for this target.

The nonlinearity is the constraint, not an interaction added by hand. A linear sigma model would carry four fields and a potential with a Mexican hat; the nonlinear model is what remains when the radial field is removed by the constraint. The two descriptions agree below the radial mass and differ above it, which is why the sigma model is an effective theory and the linear model is the renormalizable one.

## The Structural Consequence: One Term Now, a Series Later

**The action is the first term of a series and not a complete theory.** Every invariant of the target built from derivatives has even degree, so

$$
\mathcal{L}=\mathcal{L}_2+\mathcal{L}_4+\mathcal{L}_6+\cdots,
\qquad
\mathcal{L}_{2n}\sim\frac{f^2}{\Lambda^{2n-2}}\,\partial^{2n},
$$

with $\Lambda$ the mass of the sector integrated out. In four spacetime dimensions a term with $2n\ge 4$ derivatives has dimension greater than four and is non-renormalizable in the power-counting sense, so the series is an expansion in $p/\Lambda$ and not a definition.

Why that is a consequence of the action and not an assumption. A renormalizable action in four dimensions needs terms of dimension at most four, and the target admits no dimension-two or dimension-zero invariant except a constant. The only action the target permits is therefore non-renormalizable, and the sigma model's status as an effective theory follows from the geometry of $\mathbb{H}^1$ and not from a choice.

What the algebra carries and what it does not. The target $\mathbb{H}^1$ is the group $\mathrm{SU}(2)$, which is inside the algebra's compact group $\mathrm{U}(2)$; the metric on it is the biquaternion norm; and the flat current is the algebra's own commutator. Those three are the algebra's contribution. The dimension count, the power counting and the divergence structure are standard and are not the algebra's, which is the boundary the companion's power-counting section records.

## The Noether Currents: Two Chiral Currents and One Broken

The two currents. Invariance under $\tilde U\mapsto g_L\tilde U g_R^{*}$ with $g_L,g_R$ constant gives a left and a right current,

$$
j^{(L)}_{\imath}=\frac{\partial \tilde U}{\partial R_{\imath}}\tilde U^{\natural},
\qquad
j^{(R)}_{\imath}=\tilde U^{\natural}\frac{\partial \tilde U}{\partial R_{\imath}},
$$

the second of which is the $j_{\imath}$ of the action. Both are conserved on shell, and their sum and difference are the vector and axial currents.

**The vector current is the unbroken one.** The diagonal $g_L=g_R=g_V$ leaves the vacuum invariant and gives a conserved current with no Goldstone boson; the axial combination is the one whose conservation fails in the presence of a mass, and whose would-be Goldstone is the $\vec\pi$ itself. The distinction between the two is a statement about which symmetry is realized linearly and which nonlinearly, and the action does not distinguish them: both currents follow from the same invariance.

Energy–momentum. Translation invariance gives the canonical tensor

$$
T_{\imath\jmath}=f^2\,\mathrm{Sc}\bigl(\bar j_{\imath} j_{\jmath}\bigr)-g_{\imath\jmath}\mathcal{L},
$$

whose trace in four dimensions vanishes for the two-derivative action, which is the statement that the classical sigma model is conformally invariant. A mass term or a four-derivative term would break it, and the trace anomaly of the quantised model is the companion article's.

What there is not. No current carries a central phase, because the carrier has none; there is no $\mathrm{U}(1)$ current to compare with the Dirac one. The model's currents are all chiral, and that is the structural difference from every element article in the family.

## What the Principle Adds and What It Relabels

Adds.

- *A variational origin for current conservation.* The parent states $\partial_{\imath} j_{\imath}=0$ as a property of the model; the action makes it the stationarity of one functional, and the flatness of the current becomes the reason the two coincide.
- *A reason for the coefficient's cancellation.* The appearance of $f^2$ multiplying an action that does not depend on $f$ is visible only when the action is written; the equation alone hides it.
- *A single place where the constraint enters.* In the equation the constraint is implicit in the field's definition; in the action it is the restricted variation, and the degree-of-freedom count follows from it directly.

Relabels.

- *The "nonlinear" of the model's name.* It is not a nonlinearity added to a linear theory; it is the constraint, and the linear sigma model is the unconstrained version with one more field.
- *The derivative expansion.* It is not an approximation scheme laid over a known action; it is the complete list of terms the target admits, ordered by dimension.
- *The decay constant.* It is not a coupling; it is the coefficient of the only term, and it cancels from the classical equation.

The distinction that matters. The action is local in content and integral in form: the integrand is a function of the field and its first derivative at a point, and the equation is a differential identity at each point. What the integral adds is the selection principle — the constraint on the variation — and that is what makes the difference between a current that happens to be conserved and one that must be.

## Open Questions

Is the four-derivative term singled out? At four derivatives the target admits more than one invariant, and the Skyrme term is the combination that is at most quadratic in time derivatives. Whether that condition is forced by the algebra or is a choice within the standard classification is not settled; the Skyrme article states the condition and uses it.

## Summary

The action. $S=-\frac{f^2}{2}\int d^4r\,\mathrm{Sc}(\bar j_{\imath} j_{\imath})$ with $j_{\imath}=\tilde U^{\natural}\partial_{\imath}\tilde U$ and $\tilde U\tilde U^{\natural}=e_t$. Varying inside the constraint gives $\partial_{\imath}\bar j_{\imath}=0$, which is the parent's equation.

The three findings. The constraint is the nonlinearity and gives the three degrees of freedom. The coefficient $f^2$ cancels from the classical equation and enters only in the interactions. The target admits no invariant but the derivative series, so the model is an effective theory by geometry and not by choice.

The boundary. The target, the metric and the flat current are the algebra's; the power counting, the divergence structure and the value of $f$ are not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde U\in\mathbb{H}^1_{\mathbb{B}}$ | sigma-model field, a unit real quaternion |
| $\vec\pi$ | the three Goldstone coordinates, $\vec\pi^{\natural}=-\vec\pi$ |
| $f=f_\pi$ | decay constant, $2.086\times10^{-11}\ \mathrm{J}$ |
| $j_{\imath}=\tilde U^{\natural}\partial_{\imath}\tilde U$ | Maurer–Cartan current, flat, anti-Hermitian |
| $\mathrm{Sc}(\cdot)$, $\langle\cdot\rangle_\natural$ | scalar part; Minkowski square |
| $g_L,g_R$ | constant unit quaternions acting on the left and right |
| $\Lambda$ | mass of the integrated-out radial sector |
| $d^4r$ | $c\,dr'_t\,dr_x\,dr_y\,dr_z$ |

## Further Reading

- [The Nonlinear Sigma Model in Biquaternionic Form](the-nonlinear-sigma-model-in-biquaternionic-form.html) — the parent: the target, the power counting and the two-dimensional exception.
- [The Chiral Theory and the Lagrangian: The Pion and the Decay Constant](the-chiral-theory-and-the-lagrangian-the-pion-and-the-decay-constant.html) — the same action read as the pion theory, with the explicit-breaking terms.
- [The Lagrangian and the Skyrme Model](the-lagrangian-and-the-skyrme-model.html) — the four-derivative term that stabilises a soliton.
- [Goldstone's Theorem in Biquaternionic Form](goldstones-theorem-in-biquaternionic-form.html) — why the three fields are massless, and the soft limit.
- [The Lagrangian and the Interacting Scalar Field](the-lagrangian-and-the-interacting-scalar-field.html) — the linear model this one is the constrained limit of.
