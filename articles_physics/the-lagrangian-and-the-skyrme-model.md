# __The Lagrangian and the Skyrme Model__

## Introduction

This article writes the Skyrme model as an extremum of an action in the algebra, and shows what the second term buys that the first cannot. It is the action-first companion of *The Skyrme Model and the Topological Baryon in Biquaternionic Form*, which states the two terms and the soliton; this article asks what functional has the Skyrme equation as its stationary condition, and why one term is not enough.

The equation. The parent's equation is the pair

$$
\frac{\partial}{\partial R_{\imath}}\Bigl(\tilde U^{\natural}\frac{\partial \tilde U}{\partial R_{\imath}}\Bigr)+\frac{1}{e^2}\frac{\partial}{\partial R_{\imath}}\bigl[\tilde U^{\natural}\partial_{\imath}\tilde U,[\tilde U^{\natural}\partial_{\jmath}\tilde U,\tilde U^{\natural}\partial_{\jmath}\tilde U]\bigr]=0 ,
\qquad
\tilde U\tilde U^{\natural}=e_t ,
$$

the stationarity of the two-term action over group-valued fields. The article asks what action produces it and what each term does.

Three things are established.

*First, the action.* With $j_{\imath}=\tilde U^{\natural}\partial_{\imath}\tilde U$ and $\mathrm{Sc}(\cdot)$ the scalar part,

$$
S[\tilde U]=\int d^4r\;\Bigl[-\frac{f^2}{2}\,\mathrm{Sc}\bigl(\bar j_{\imath} j_{\imath}\bigr)+\frac{1}{16e^2}\,\mathrm{Sc}\bigl([j_{\imath},j_{\jmath}][j_{\imath},j_{\jmath}]\bigr)\Bigr],
$$

the Euler–Lagrange condition is the parent's equation. The first term is the sigma model's; the second is the Skyrme term, and it is the unique four-derivative invariant that is at most quadratic in time derivatives.

*Second, one term has no soliton.* A static configuration of the two-derivative action is scale invariant in three dimensions: shrinking it lowers its energy without bound, because a two-derivative energy in $d=3$ scales as $1/L$ and the target's topology gives no gap. The Derrick argument is re-derived here as a statement about the action, and it is the reason the second term exists.

*Third, the second term is a commutator because the current is flat.* $[j_{\imath},j_{\jmath}]$ vanishes for a pure gauge field and it is precisely the flatness of $j_{\imath}$ that makes the commutator a measure of curvature rather than of the field's definition. The algebra gives the term its form; the standard classification gives it its uniqueness.

What is not new. The Skyrme model is standard, and its soliton, its topological charge and its baryon identification are imported. What the algebra supplies is that both terms are norms of one algebra-valued current and that the four-derivative combination is the norm of that current's commutator.

## Conventions

The conventions are restated here so that every sign below is checkable from this page. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$; the field is $\tilde U\in\mathbb{H}^1_{\mathbb{B}}$ with $\tilde U^{-1}=\tilde U^{\natural}=\tilde U^{*}$. $\mathrm{Sc}(X)$ is the coefficient of $e_t$; $\langle X\rangle_\natural=\mathrm{Sc}(XX^{\natural})$.

The static frame. Spatial coordinates are $\vec r=R_x\vec e_x+R_y\vec e_y+R_z\vec e_z$, the fields are static, $\partial\tilde U/\partial r'_t=0$, and configurations are pure gauge at spatial infinity, $\tilde U\to e_t$ as $|\vec r|\to\infty$, so that they extend to maps $\mathbb{S}^3\to\mathbb{S}^3$.

The two parameters. $f=f_\pi$ is the decay constant, dimension of mass; $e$ is dimensionless. The combination $1/e$ has dimension of length in the standard counting and sets the soliton's size; the ratio $f/e$ is not fixed by the action.

The sign convention. The overall sign is the one that makes the static energy positive, as in the parent; with it the two-derivative term gives a positive gradient energy and the four-derivative term gives a positive commutator energy.

## The Action in Element Form

The current, and its flatness. The Maurer–Cartan form

$$
j_{\imath}=\tilde U^{\natural}\frac{\partial \tilde U}{\partial R_{\imath}}\in\mathfrak{su}(2)\subset\mathbb{B}_\Phi
$$

is flat,

$$
\frac{\partial j_{\jmath}}{\partial R_{\imath}}-\frac{\partial j_{\imath}}{\partial R_{\jmath}}+[j_{\imath},j_{\jmath}]=0 ,
$$

and flatness is what the second term of the action measures the failure of. In the static frame $j_i=\tilde U^{\natural}\partial_i\tilde U$ and $[j_i,j_j]$ is the curvature of the spatial connection, nonzero for every non-constant $\tilde U$.

The two terms.

$$
\mathcal{L}_2=-\frac{f^2}{2}\,\mathrm{Sc}\bigl(\bar j_{\imath} j_{\imath}\bigr),
\qquad
\mathcal{L}_4=\frac{1}{16e^2}\,\mathrm{Sc}\bigl([j_{\imath},j_{\jmath}][j_{\imath},j_{\jmath}]\bigr).
$$

Both are norms: the first of the current, the second of its commutator. The second is negative-definite before the overall sign is applied, because $[j_{\imath},j_{\jmath}]$ is anti-Hermitian, so $\mathrm{Sc}([j,j][j,j])=-\langle[j,j]\rangle_\natural\le 0$, and the coefficient carries the sign that makes the energy positive.

Why there are exactly two terms at this order. At two derivatives the target admits one invariant; at four it admits two, of which the second is a total derivative and contributes nothing. The Skyrme combination is the one that is at most quadratic in time derivatives, which is the condition that a Hamiltonian exists and that the soliton has finite energy; the alternative, four time derivatives, would give Ostrogradsky ghosts and no stable configuration. The selection is therefore the physics of the Hamiltonian and not a convention.

The topological term, and why it is not in the action. The winding number

$$
N=\frac{1}{24\pi^2}\int d^3r\;\varepsilon_{\imath\jmath\ell}\,\mathrm{Sc}\bigl(j_i[j_j,j_{\imath}]\bigr)
$$

is a total derivative and an integer; adding it to the action multiplies the path integral by a phase and changes no classical equation. It is a parameter of the quantum theory, not a term of the classical action, and the $\theta$ angle it defines is the same object as the QCD vacuum angle.

The pairing. Both pairings are the real scalar part, and both integrands are real. $\mathrm{Sc}(\bar j_{\imath} j_{\imath})$ is real because $j_{\imath}$ is anti-Hermitian; $\mathrm{Sc}([j_{\imath},j_{\jmath}][j_{\imath},j_{\jmath}])$ is real because the commutator of two anti-Hermitian elements is anti-Hermitian, and the square of an anti-Hermitian element is negative-Hermitian with a real scalar part. No reality condition is imposed; both follow from the carrier.

Why the same pairing serves both terms. The two terms differ in the object whose norm is taken — the current, and the current's commutator — and not in the pairing. That uniformity is what allows the two coefficients $f^2$ and $1/e^2$ to be compared, and it is the reason the model has one metric and not two.

The type of the coefficient. Two coefficients of different dimension, one dimensionless ratio. $f^2$ has dimension of mass squared; $1/e^2$ is dimensionless. Their ratio $f^2e^2$ has dimension of mass squared and fixes the soliton's mass scale; the dimensionless combination that sets its size is $1/(ef)$.

Neither coefficient is a coupling in the perturbative sense. Both multiply the whole action and both cancel from the classical equation; the equation depends on $e$ and $f$ only through $1/(ef)^2$, which is the scale. This is the same structural fact the sigma model's article records, now with two coefficients instead of one.

**The selection rule. Invariance under $\tilde U\mapsto g_L\tilde U g_R^{*}$ leaves exactly these two terms at this order.** The current transforms as $j_{\imath}\mapsto g_R^{*}j_{\imath} g_R$, the commutator as $[j_{\imath},j_{\jmath}]\mapsto g_R^{*}[j_{\imath},j_{\jmath}]g_R$, and the scalar part of either square is invariant because the trace is cyclic. Everything the group allows at two and four derivatives is here, and nothing else is.

What reality does not buy. Reality does not buy stability; the topology and the scaling do. Three things the reality of the action does not supply:

- *No soliton from one term.* The two-derivative action is real and scale invariant, and both facts are compatible with no stable configuration existing.
- *No fixed size.* The minimiser's size is set by $1/(ef)$, and the action fixes neither number.
- *No quantisation.* The soliton's spin and statistics come from quantising the collective coordinates, which the action makes possible and does not perform.

## The Variation: Two Terms, One Equation

The variation. Write $\delta\tilde U=\tilde U\tilde\alpha$ with $\tilde\alpha\in\mathfrak{su}(2)$ vanishing at the boundary. Then $\delta j_{\imath}=\partial_{\imath}\tilde\alpha+[j_{\imath},\tilde\alpha]$ and $\delta[j_{\imath},j_{\jmath}]=[\partial_{\imath}\tilde\alpha+[j_{\imath},\tilde\alpha],j_{\jmath}]+[j_{\imath},\partial_{\jmath}\tilde\alpha+[j_{\jmath},\tilde\alpha]]$, a Jacobi-identity rearrangement.

**The two contributions.** The two-derivative term gives, after one integration by parts, the term $\partial_{\imath}\bar j_{\imath}$ of the parent's equation. The four-derivative term gives the divergence of the double commutator, $-\frac{1}{4e^2}\partial_{\imath}[\bar j_{\jmath},[\bar j_{\imath},\bar j_{\jmath}]]$-type contributions, and the two together are the boxed equation of the parent. Neither vanishes alone, and the equation is not the sum of two independent equations: the two terms couple through the same current.

The check that would catch a sign. For a hedgehog configuration $\tilde U=\cos F(r)e_t+\sin F(r)\,\vec r/|\vec r|$ with $F(0)=\pi$ and $F(\infty)=0$, the two-derivative energy is proportional to $\int dr\,(r^2F'{}^2+2\sin^2F)$ and the four-derivative energy to $\int dr\,(\sin^2F/r^2)(2r^2F'{}^2+\sin^2F)$. Both are positive, and the Euler–Lagrange equation for $F$ has the two terms with opposite signs under scaling, which is what makes the minimiser exist.

Why the boundary condition is part of the variation. The field must approach a constant at spatial infinity for the energy to be finite; the variation must respect that, so $\tilde\alpha\to0$ at infinity. The topological charge is then fixed during the variation, and the variation explores one sector at a time. Without that restriction the equation has constant solutions in every sector and no soliton.

## The Constraints the Action Imposes: Derrick's Argument and the Second Term

The scaling argument, re-derived here because it is the reason for the action's shape. Scale a static configuration by $\digamma_{\mathrm{skr}}$: $\tilde U_{\imath}(\vec r)=\tilde U(\vec r/\digamma_{\mathrm{skr}})$. Then the two-derivative energy scales as

$$
E_2(\digamma_{\mathrm{skr}})=\frac{1}{\digamma_{\mathrm{skr}}}E_2(1),
$$

because one gradient in three dimensions gives $1/\digamma_{\mathrm{skr}}$, and the four-derivative energy scales as

$$
E_4(\digamma_{\mathrm{skr}})=\digamma_{\mathrm{skr}}\,E_4(1),
$$

because four gradients in three dimensions give $\digamma_{\mathrm{skr}}$. A stationary configuration must satisfy $dE/d\digamma_{\mathrm{skr}}=0$ at $\digamma_{\mathrm{skr}}=1$, hence

$$
-E_2(1)+E_4(1)=0 .
$$

**What the identity says.** With only the two-derivative term, $E_2(1)=0$, which forces $E_2=0$ and hence a constant field: no soliton. With both terms the identity is a virial relation, not an obstruction, and a minimiser exists with $E_4=E_2$. The two-derivative term alone is not merely inconvenient; it is provably solitonless in three dimensions.

Why the Skyrme term specifically and not any four-derivative term. A term with four time derivatives would also scale as $\digamma_{\mathrm{skr}}$, but it would give a Hamiltonian unbounded below and ghosts in the propagator. The condition "at most quadratic in time derivatives" selects the commutator term among the four-derivative invariants, and that condition is what a Hamiltonian theory requires. This is the sharpest statement of why the model has the shape it has.

The finite-energy constraint. $\tilde U\to e_t$ at infinity is what makes both energies finite and what fixes the topological sector. Without it the integrals diverge and the scaling argument does not apply.

## The Structural Consequence: A Soliton Whose Charge Is a Winding Number

The configuration space is disconnected, and that is the physics. Maps $\mathbb{S}^3\to\mathbb{S}^3$ fall into classes labelled by an integer, $\pi_3(\mathbb{S}^3)=\mathbb{Z}$, and the integer is the integral of the topological density. Two configurations in different classes cannot be deformed into one another, so the model has stable sectors that no energy argument produces.

**The bound.** Completing the square in the static energy gives

$$
E\ge 6\pi^2\frac{f}{e}\,|N| ,
$$

with equality for a self-dual configuration. The bound is the model's version of a Bogomolny bound; it is saturated only approximately by the true minimiser, and the gap is a few percent for the physical pion mass.

Why this is a structural consequence and not a solution. The action tells us that a stable sector exists and that its energy is bounded below by its winding number. It does not give the profile; that requires solving the Euler–Lagrange equation for $F(r)$, and the solution is the parent's. The distinction between what the action guarantees and what it does not is the boundary this section draws.

The baryon identification, and its status. $N$ is identified with baryon number because the model's soliton has the quantum numbers of a baryon, and that identification is a hypothesis of the programme and not a consequence of the action. The corpus records it as such.

## The Noether Currents: Chiral Currents Plus a Winding Current

The chiral currents. The two terms are both invariant under $\tilde U\mapsto g_L\tilde U g_R^{*}$, so both contribute to the left and right currents and both are conserved. The vector current's conservation is the unbroken symmetry; the axial current's is the one that a mass term would break.

The topological current. The winding density

$$
B_{\imath}=\frac{1}{24\pi^2}\varepsilon_{\imath\jmath k\rho}\,\mathrm{Sc}\bigl(j_{\jmath}[j_{\imath},j_\rho]\bigr)
$$

is conserved identically, not on shell, because it is a total derivative. Its conservation is a Bianchi identity and not a symmetry's consequence; it holds for every field, whether or not the equation of motion is satisfied. The distinction between a conserved current that follows from an equation and one that follows from an identity is the sharpest structural point of this section.

Energy–momentum. Translation invariance gives $T_{\imath\jmath}$ with contributions from both terms, and the static energy is its time–time component. The virial identity $E_4=E_2$ is the statement that the trace of the spatial part vanishes for the minimiser, which is the scale invariance of the two-term action restored by the balance of the two terms.

**What there is not.** No $\mathrm{U}(1)$ current, no central phase, no second independent current beyond the chiral pair and the topological one.

## What the Principle Adds and What It Relabels

Adds.

- *A derivation of the second term's necessity.* The Derrick identity is a statement about the action's scaling, and it is available only when the action is written as a functional of a scaling family.
- *A reason for the commutator.* The second term is the norm of the current's commutator, and that is visible in the action and invisible in the equation.
- *The virial relation.* A relation between the two energies that no single equation displays.

Relabels.

- *The "Skyrme term" itself.* In the corpus it is not an extra term appended to a model; it is the second term of the derivative expansion, and the expansion is the reason it is there.
- *The topological charge.* It is not a charge of a symmetry; it is the degree of a map, and its conservation is an identity.
- *Stability.* It is not a dynamical statement about perturbations; at the level of the action it is the statement that the energy is bounded below by the winding number.

The distinction that matters. The action is real and the physics is topological. What the variational principle adds is the ability to separate the two: the equation of motion is local and the charge is global, and the bound sits between them.

## Open Questions

Is the fourth-order coefficient fixed by the algebra? $e$ is a parameter of the model and nothing in the algebra fixes it. Whether the algebra's commutator structure imposes a relation between $e$ and $f$ is not established; the two are independent in the standard model and in the corpus.

## Summary

The action. $S=\int d^4r\,[-\frac{f^2}{2}\mathrm{Sc}(\bar j_{\imath} j_{\imath})+\frac{1}{16e^2}\mathrm{Sc}([j_{\imath},j_{\jmath}][j_{\imath},j_{\jmath}])]$ with $j_{\imath}=\tilde U^{\natural}\partial_{\imath}\tilde U$ flat on $\mathbb{H}^1$. Varying inside the constraint gives the parent's equation.

The three findings. One term is solitonless by the Derrick identity, and the second term is exactly what cancels the obstruction. The second term is a commutator because the current is flat, and the "at most quadratic in time" condition selects it among the four-derivative invariants. Stability at the level of the action is the bound $E\ge 6\pi^2(f/e)|N|$.

**The boundary.** The two norms and the commutator are the algebra's; the coefficients $f$ and $e$, the baryon identification and the profile are not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde U\in\mathbb{H}^1_{\mathbb{B}}$ | Skyrme field, unit real quaternion, pure gauge at infinity |
| $j_{\imath}=\tilde U^{\natural}\partial_{\imath}\tilde U$ | flat Maurer–Cartan current |
| $f=f_\pi$ | decay constant |
| $e$ | dimensionless Skyrme parameter |
| $N$ | winding number, $\pi_3(\mathbb{S}^3)=\mathbb{Z}$ |
| $B_{\imath}$ | topological (baryon) current, conserved identically |
| $E_2,E_4$ | two- and four-derivative energies |
| $\digamma_{\mathrm{skr}}$ | scale factor of a configuration |

## Further Reading

- [The Skyrme Model and the Topological Baryon in Biquaternionic Form](the-skyrme-model-and-the-topological-baryon-in-biquaternionic-form.html) — the parent: the soliton, the profile, the quantisation.
- [The Lagrangian and the Nonlinear Sigma Model](the-lagrangian-and-the-nonlinear-sigma-model.html) — the two-derivative term alone, and why it needs the second.
- [The Chiral Theory and the Lagrangian: The Pion and the Decay Constant](the-chiral-theory-and-the-lagrangian-the-pion-and-the-decay-constant.html) — the pion reading of the first term.
- [The Lagrangian and the Central Scalar Field](the-lagrangian-and-the-central-scalar-field.html) — the classical scalar action, for comparison of the wave-operator structure.
- [Topological Charge, Self-Duality and the Bogomolny Bound](topological-charge-self-duality-and-the-bogomolny-bound-in-biquaternionic-form.html) — bounds of the same kind in the gauge sector.
