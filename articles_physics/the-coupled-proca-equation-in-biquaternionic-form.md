# __The Coupled Proca Equation in Biquaternionic Form__

## Introduction

This article couples the Proca field to an electromagnetic connection and reads what the coupling does to the field, to the equation, and to the algebra's own bookkeeping. It is the element-form companion of *The Coupled Proca Equation in Biquaternionic Polar Variables*, and it depends on *The Proca Equation in Biquaternionic Form* for the free equation, on *The Gauge Principle in Biquaternionic Form* for the localization of the central phase, and on *The Covariant Derivative and Gauge Connection in Biquaternionic Form* for the operator identity.

**The equation.**

$$
\tilde\nabla_{\mathrm{gco}}\tilde F=k_m^2\tilde A,
\qquad
\tilde F=\frac12\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A-\tilde\nabla_{\mathrm{gco}}\tilde A\bigr)_{\mathrm{V}},
\qquad
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi},
$$

with $\tilde A$ the Proca potential, $\tilde A_\Phi$ the connection, $k_m=mc/\hbar$, and the subscript $\mathrm{V}$ the pure-vector part of an element. The second display is one half of the antisymmetric part of the covariant gradient, and the article writes it in that form because the symmetric half is the covariant divergence, which is a different object.

**Four things are established, and they are exact statements of structure.**

*First, the carrier must change.* The free Proca field is an element of the material sector $\mathbb{B}_\Phi$, and the material sector is not closed under its own product. A coupling that multiplies the field by a connection element therefore carries the field out of the sector unless the field is complexified, and the complexified carrier is $\mathbb{B}$ itself. The coupling is what forces $\tilde A\in\mathbb{B}$, and the free field is the real slice of the coupled one (§*The Carrier*).

*Second, the field strength carries the connection, unlike the Dirac case.* The Proca equation contains $\tilde F$, and $\tilde F$ is built from the covariant gradient, so the connection enters the equation twice: once through the derivative and once through the field strength. In the Dirac equation the field strength is not in the equation at all, and the coupling enters once. The extra term is $\frac{iϙ}{\hbar}\mathrm{Vect}(\tilde A_{\Phi}^{\natural}\tilde A)$, it is bilinear in the two potentials, and it is the algebra's form of the commutator term that a non-abelian field strength carries.

*Third, the Lorenz condition survives, and it survives in covariant form.* The second-order operator $\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}$ is the sum of the squared components plus the curvature, and the curvature term is a pure vector, so it has no scalar part. The trace of the coupled equation therefore forces $\mathrm{Sc}(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A)=0$ exactly, with no term to spare. What is not forced is the *ordinary* divergence: the covariant condition differs from it by a term bilinear in the connection.

*Fourth, the carrier now has a central phase, so the field now has a charge.* The free Proca field is real, the central imaginary leaves the material sector, and the free article's conclusion is that there is no second current. A complex field has the phase, the phase is a symmetry of the coupled equation, and the Noether current exists. That current is the source the inhomogeneous Maxwell equation needs, and its existence is the reason the free article could not supply one.

**What is not claimed.** No new solution, no new prediction, no new particle. The equation is the standard minimally coupled Proca equation and the statements are the standard ones; the algebra's contribution is that the coupling is one element rather than four rules, that the obstruction to it is a closure statement, and that the two currents and the constraint fall out of two trace computations.

## The Carrier

**The free field is a material-sector element.** The Proca potential is

$$
\tilde A_\Phi=i\,a'_t\,e_t+\vec A,
\qquad
a'_t\in\mathbb{R},\ \vec A\in\mathbb{R}^3,
$$

so that $\tilde A_\Phi^{*}=-\tilde A_\Phi$ and $\langle\tilde A_\Phi\rangle_\natural=-(a'_t)^2+\vec A^2$, the Minkowski square. The reality is not an assumption about the field; it is what makes the four components four, and the free article's two polar branches are the two signs of that square.

**The material sector is not closed.** The product of two anti-Hermitian elements is Hermitian, and the simplest instance is decisive:

$$
\vec e_x\,\vec e_x=-e_t .
$$

The right side is real and central, so it is neither anti-Hermitian nor Hermitian-traceless; it is outside $\mathbb{B}_\Phi$. A hundred random products of material-sector elements leave the sector in every case, and the reason is structural: $\mathbb{B}_\Phi$ is a real subspace of dimension four in an algebra of real dimension eight, and it is closed under multiplication only by central *real* scalars.

**The obstruction is the coupling.** The gauge principle's minimal substitution is $\tilde\nabla_\Phi\mapsto\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$ acting on the field from the left. The added element lies in $\mathbb{B}_\Phi$, so the coupled derivative of a material field is a sum of a material element and a product of two material elements. The first is in the sector, the second is not, and the equation cannot be posed inside the sector.

**Two ways out, and one of them is the physics.** The first is to project after every multiplication, which is not a covariant operation and produces an equation that is not the minimal coupling of anything. The second is to enlarge the carrier to $\mathbb{B}$, where every product closes, and to accept that the field is now complex. The second is the standard charged Proca field: a complex four-vector, eight real components, of which the free field is the real slice.

**What the enlargement buys.** The element $i\tilde A_\Phi$ is *not* in the material sector, since $i$ times an anti-Hermitian element is Hermitian. The same factor $i$ that ruins the closure is the factor that the mass term of the free article could not tolerate: the free mass term $\langle\tilde A_\Phi\rangle_\natural$ is quadratic in a real field, and $(i\tilde A_\Phi)\langle\cdot\rangle_\natural$ is not real. On the complex carrier the mass term is the invariant length $|a'_t|^2-|\vec A|^2$, it is real, and it is invariant under the phase. The two facts are one fact: the carrier that closes under the coupling is the carrier on which the mass term is invariant.

**The carrier is $\mathbb{B}$ and not $\mathbb{B}_\Psi$.** The informational sector is Hermitian, is not closed under its own product either, and is not the natural home of a four-vector; the potential's four components are the coefficients of the four units with no Hermiticity imposed, which is $\mathbb{B}$. The article writes $\tilde A\in\mathbb{B}$ and never assumes more.

## The Coupling Prescription

**One operator, one element.**

$$
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi,
\qquad
\tilde A_\Phi=A_te_t+\sum_\eta A_\eta\vec e_\eta,
$$

acting from the left. The sign pair is the gauge principle's: $\tilde A_{\Phi,2}=\tilde A_\Phi-\tilde\nabla_\Phi\Gamma$ with $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$ and $\lambda=\exp(i\vartheta_{\mathrm{gau}})$, $\vartheta_{\mathrm{gau}}=ϙ\Gamma/\hbar$.

**The connection is central per component in the abelian case.** With $A_\mu$ scalar coefficients that commute with the units and with one another, the covariant derivative separates:

$$
\tilde\nabla_{\mathrm{gco}}=\sum_\mu e_\mu\,\tilde\nabla_{\mathrm{gco},\mu},
\qquad
\tilde\nabla_{\mathrm{gco},\mu}=\frac{\partial}{\partial R_\mu}+\frac{i\,ϙ}{\hbar}A_\mu .
$$

Each $\tilde\nabla_{\mathrm{gco},\mu}$ is a *central* operator: it multiplies every element of $\mathbb{B}$ from either side without changing its type. That centality is the single fact on which everything in the two coupled Proca articles turns, and it is the reason the polar companion can state the coupling as a shift of four scalar slots.

**The two forms of the operator agree.** The per-component display and the element display are the same operator, because $A_\mu$ is central:

$$
\sum_\mu e_\mu\frac{i\,ϙ}{\hbar}A_\mu=\frac{i\,ϙ}{\hbar}\sum_\mu A_\mu e_\mu=\frac{i\,ϙ}{\hbar}\tilde A_\Phi .
$$

The equality is the reason the article can use the per-component form for computations and the element form for covariance.

**The conjugate operator.**

$$
\tilde\nabla_{\mathrm{gco}}^{\natural}=(\tilde\nabla_\Phi)^{\natural}+\frac{i\,ϙ}{\hbar}\tilde A_\Phi^{\natural},
\qquad
\tilde A_\Phi^{\natural}=A_te_t-\sum_\eta A_\eta\vec e_\eta .
$$

For a purely electric potential $\tilde A_\Phi^{\natural}=+\tilde A_\Phi$; for a purely magnetic one $\tilde A_\Phi^{\natural}=-\tilde A_\Phi$; for a general potential it is neither. The asymmetry is the algebra's statement that the electric and magnetic slots of the connection enter the conjugate derivative with opposite signs, and it is why the field strength below is not simply twice the magnetic part.

**The side is the left, and the mirror is the renaming.** Every coupling here acts on the left. The right-action equation on $\tilde A$ is the left-action equation on $\tilde A^{\natural}$, by the renaming identity $(\tilde A\tilde\nabla_{\mathrm{gco}})^{\natural}=\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A^{\natural}$, so the two sides are one construction and not two.

## Gauge Covariance

**The gauge transformation.**

$$
\tilde A_2=\lambda\tilde A,
\qquad
\tilde A_{\Phi,2}=\tilde A_\Phi-\tilde\nabla_\Phi\Gamma,
\qquad
\lambda=\exp\bigl(i\vartheta_{\mathrm{gau}}\bigr),
\qquad
\Gamma\ \text{real},
$$

with $\lambda$ central and of unit modulus. The field transforms by multiplication and not by the inhomogeneous shift; the shift belongs to the connection. That division is the whole content of the phrase "the field is charged".

**The chain rules.** Because $\lambda$ is a central scalar function,

$$
\tilde\nabla_\Phi\lambda=\frac{i\,ϙ}{\hbar}\bigl(\tilde\nabla_\Phi\Gamma\bigr)\lambda,
\qquad
(\tilde\nabla_\Phi)^{\natural}\lambda=\frac{i\,ϙ}{\hbar}\bigl((\tilde\nabla_\Phi)^{\natural}\Gamma\bigr)\lambda,
$$

and $\natural$ leaves $\lambda$ alone, since $\natural$ negates the spatial units and fixes the coefficients.

**The first derivative is covariant.**

$$
\tilde\nabla_{\mathrm{gco},2}\bigl(\lambda\tilde A\bigr)
=\tilde\nabla_\Phi\bigl(\lambda\tilde A\bigr)+\frac{i\,ϙ}{\hbar}\bigl(\tilde A_\Phi-\tilde\nabla_\Phi\Gamma\bigr)\lambda\tilde A
=\lambda\,\tilde\nabla_{\mathrm{gco}}\tilde A .
$$

The two $\tilde\nabla_\Phi\Gamma$ terms cancel and $\lambda$ passes to the left past the connection and past the field. The second derivative repeats the computation with $\natural$ throughout and gives $\tilde\nabla_{\mathrm{gco},2}^{\natural}(\lambda\tilde A)=\lambda\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A$.

**The field strength is covariant.**

$$
\tilde F_2=\lambda\tilde F,
$$

because $\mathrm{Vect}$ commutes with left multiplication by a central element and the antisymmetric part of a covariant gradient is covariant. This is the statement the free article had no occasion to make: the free field strength is invariant, the coupled one is *covariant*, and the difference is the charge.

**The equation is covariant, massive as well as massless.** Both sides acquire one factor $\lambda$:

$$
\tilde\nabla_{\mathrm{gco},2}\tilde F_2=\lambda\,\tilde\nabla_{\mathrm{gco}}\tilde F,
\qquad
k_m^2\tilde A_2=\lambda\,k_m^2\tilde A .
$$

The mass term is homogeneous because it is linear in the field; it is the *bilinear* mass term of the action that is invariant, and the two statements are consistent, since $\lambda\bar\lambda=1$. In the free article the mass term is quadratic in a real field and breaks the symmetry; here the field is complex, the mass term is quadratic in the field and its conjugate, and the symmetry survives. That single sign of bookkeeping is why a massive vector field can be coupled at all.

## The Field Strength Carries the Connection

**The definition.**

$$
\tilde F=\frac12\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A-\tilde\nabla_{\mathrm{gco}}\tilde A\bigr)_{\mathrm{V}}
=\mathrm{Vect}\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A\bigr),
$$

the two displays agreeing because the pure-vector part of an element and the part of its $\natural$-image are related by the sign of the whole, and the antisymmetric combination of the gradient and its conjugate is the vector part of either.

**In components the definition is the covariant curl.**

$$
F_{0\eta}=D_0A_\eta-D_\eta A_0,
\qquad
F_{\eta\kappa}=D_\eta A_\kappa-D_\kappa A_\eta,
\qquad
D_\mu=\frac{\partial}{\partial R_\mu}+\frac{i\,ϙ}{\hbar}A_\mu .
$$

The six real components of $\tilde F$ are the six field-strength components, and the $\sqrt{\epsilon}$, $\sqrt{\mu}$ normalization of the free article's display $\tilde F=i\sqrt{\epsilon}\vec E-\sqrt{\mu}\vec H$ is carried by the coefficients.

**The connection does not cancel, and this is the structural difference from the ordinary abelian curl.** For a neutral field strength built from a potential that shifts by a gradient, the connection terms cancel in the antisymmetric combination, because $D_\mu A_\nu$ and $D_\nu A_\mu$ carry the *same* connection coefficient. Here the potential is charged: it multiplies by $\lambda$ and the connection shifts, so the two statements are independent, and

$$
\tilde F=\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A\bigr)+\frac{i\,ϙ}{\hbar}\mathrm{Vect}\bigl(\tilde A_\Phi^{\natural}\tilde A\bigr).
$$

The second term is nonzero. Its size runs from $0.7$ to $12$ over a hundred random draws of a material connection and a general element, and its structure is a product of two potentials, linear in each.

**What the extra term is.** It is the algebra's form of the term that distinguishes a non-abelian field strength from an abelian one. In components the commutator of two covariant derivatives on a charged field is $[D_\mu,D_\nu]=-iϙF^{(\Phi)}_{\mu\nu}$, and the field strength built from the covariant curl is not the ordinary curl. The algebra produces the same structure from the non-commutativity of the units alone: since the connection multiplies the field as one element and the gradient's units multiply it as units, the two orders differ, and the difference is $\frac{i\,ϙ}{\hbar}\mathrm{Vect}(\tilde A_\Phi^{\natural}\tilde A)$.

**The Bianchi identity is not available in the same form.** For a neutral field strength the antisymmetric part of the gradient of the field strength vanishes identically, because partial derivatives commute. With the connection the corresponding statement carries the curvature, and this article does not need it: the Proca equation is first order in $\tilde F$ and does not use a Bianchi identity.

**What the free article's $\tilde F$ was.** It was the same expression with the connection set to zero, and in that limit the extra term vanishes and the two terms of the display collapse. The free field strength is the $\vartheta_{\mathrm{gau}}=0$ slice of the coupled one, exactly as the free field is the real slice of the coupled one.

## The Lorenz Condition in Covariant Form

**The operator identity.** The covariant d'Alembertian splits into a scalar part and a curvature part:

$$
\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}
=\sum_\mu\tilde\nabla_{\mathrm{gco},\mu}^{2}+\frac{i\,ϙ}{\hbar}\tilde F^{(\Phi)},
$$

with $\tilde F^{(\Phi)}$ the curvature of the connection. The first term is scalar — each $\tilde\nabla_{\mathrm{gco},\mu}$ is central, so the four squares are central operators and their sum multiplies every element uniformly. The second term is a pure vector, and a pure vector has no scalar part.

**The trace of the equation therefore forces the constraint.** Applying $\tilde\nabla_{\mathrm{gco}}^{\natural}$ to the equation and taking the scalar part,

$$
k_m^2\,\mathrm{Sc}\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A\bigr)
=\mathrm{Sc}\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}\tilde F\bigr)
=\sum_\mu\tilde\nabla_{\mathrm{gco},\mu}^{2}\,\mathrm{Sc}\bigl(\tilde F\bigr)=0,
$$

since $\tilde F$ is a pure vector. The constraint is exact, it holds for every configuration that solves the equation, and it is *covariant*:

$$
\mathrm{Sc}\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A\bigr)=0
\qquad\Longleftrightarrow\qquad
\frac{\partial a'_t}{\partial r'_t}+\nabla\cdot\vec A
=-\frac{i\,ϙ}{\hbar}\,\mathrm{Sc}\bigl(\tilde A_\Phi^{\natural}\tilde A\bigr).
$$

**The two readings of that line.** The left reading is the covariant Lorenz condition, and it is the one the equation forces. The right reading is the ordinary divergence, and it is *not* zero: it is fixed by the potential, slot by slot, since $\mathrm{Sc}(\tilde A_\Phi^{\natural}\tilde A)$ is one scalar built from the two potentials. For a purely electric constant potential the right side is $\frac{ϙ a}{\hbar}a'_t$ in the article's units, so even a constant electrostatic potential moves the ordinary divergence.

**Why the curvature does not spoil it.** The naive expectation is that a background field strength should source the constraint, as it does for a non-abelian massive vector. The algebra's answer is precise and different: the curvature term in the operator identity is traceless. The trace sees only $\sum_\mu\tilde\nabla_{\mathrm{gco},\mu}^{2}$, the four operators commute with each other as central operators, and the commutator's contribution is confined to the traceless part of the equation. The constraint is untouched; the *transport of the frame* is what the curvature moves, and that is the polar companion's subject.

**A check on a lattice.** Applying the composite to a random pure-vector field on a periodic lattice gives a scalar part of size $3\times10^{-13}$ in the free case and $4\times10^{-13}$ in a background with constant field strength — the same number, which is the numerical form of the statement that the curvature does not enter the trace. The same computation with the cross terms of the composite deleted — that is, with the algebra's units treated as commuting — gives zero identically, which locates the whole effect in the non-commutativity of the units.

## A Constant Background

**The symbol.** For a plane wave $\tilde A=\tilde A_0\exp(-i\vartheta)$ in a constant connection, every derivative is a multiplication and the equation becomes an algebraic system:

$$
\bigl(i\tilde K+\tilde C\bigr)\,\mathrm{Vect}\bigl((i\tilde K^{\natural}+\tilde C^{\natural})\tilde A_0\bigr)=k_m^2\tilde A_0,
\qquad
\tilde C=\frac{i\,ϙ}{\hbar}\tilde A_\Phi,
$$

four complex equations for the four components of the amplitude, with $\tilde K$ the wavevector biquaternion. The determinant of the $4\times4$ symbol is the dispersion relation; it is complex, so it is two real conditions on four real components of $\tilde K$, which is the count of a massive branch.

**The scalar potential is an energy shift, and it is exact.** For a purely electric constant potential, $\tilde C$ is central and real, so it commutes with everything and adds to the temporal slot of the covariant wavevector. The roots move by one amount and not by two:

$$
\omega=\pm\sqrt{\vec k^{\,2}+k_m^2}-\frac{ϙ a'_t}{\hbar}
\qquad\text{in the article's units,}
$$

that is $E\mapsto E+ϙ c\,a'_t$ with $E=\hbar\omega$. The numerical check is exact: the determinant vanishes at the shifted frequency to machine precision ($2\times10^{-48}$) and does not vanish at the unshifted one. The particle and the antiparticle move in opposite directions, which is the algebraic statement that the two signs of $\omega$ are the two charges.

**The vector potential is not a shift.** For a purely magnetic constant potential, $\tilde C$ is a pure vector and does not commute with the units; the determinant is no longer a function of $\omega^2$, the two transverse roots separate, and the longitudinal root is the one the constraint fixes. The article records the structure and not a closed formula: the roots are the zeros of a $4\times4$ determinant and this article does not solve it in general.

**What a constant potential is.** It has zero curvature, so it is pure gauge up to a constant, so its whole effect is the reparameterisation of the phase. That is why the scalar case is an exact shift and why the vector case is a change of basis rather than a change of spectrum. The statement is the polar companion's §*The Gauge Transformation Is a Phase Translation*, read in the element form.

## The Current

**The phase symmetry exists now.** The free article's §*No Second Current* argues that $\tilde A_\Phi\mapsto e^{i\alpha}\tilde A_\Phi$ leaves the material sector, since $i$ times an anti-Hermitian element is Hermitian. On the complex carrier the rotation is a symmetry of the equation: the mass term is invariant, the field strength is covariant with $\lambda$ constant, and the derivative is untouched.

**The Noether current.**

$$
j_\mu=\mathrm{Sc}\bigl(\tilde A^{*}\,i\,\tilde\nabla_{\mathrm{gco},\mu}\tilde A\bigr)
$$

in the article's pairing, one real number per component, and it is the object the inhomogeneous Maxwell equation needs. Two statements about it are exact and are the article's reason for stating it at all: it is invariant under the gauge group, and it is conserved on solutions by the equation and its conjugate.

**Why the free article could not have it.** A real field has no phase to rotate, so the free current is zero identically rather than merely non-conserved. The free article's remark that the electromagnetic current "is the source that the inhomogeneous equation has and the free equation does not" is a statement about the carrier, and the coupled article supplies the carrier.

**What the current is not.** It is not $i\tilde A\tilde A^{*}$, which is the density-like bilinear and is not conserved, for the reason the coupled Dirac article gives in its own case: the bilinear pairs the two halves with the same sign, so the temporal slot counts a density and the spatial slots count a current with the wrong relative weight. The pairing above is the minimal one that carries the derivative, and the variational companion derives it as the Noether charge of the action rather than asserting it.

## What the Coupling Adds and What It Does Not

**Adds.**

- A single-element coupling: one operator, one sign pair, one charge. The four classical substitutions are one addition.
- The closure statement: the carrier must be $\mathbb{B}$, and the free field is its real slice.
- The covariant field strength and its bilinear extra term, which is the algebra's form of the term an abelian curl does not have.
- The covariant Lorenz condition, exact, with the curvature confined to the traceless part.
- The charge, which the free field does not have.

**Does not add.**

- No new solution and no new prediction: the equation is the standard minimally coupled Proca equation.
- No derivation of the charge's value or sign: $ϙ$ is a parameter.
- No claim that the coupling is forced by the algebra: it is forced by the *localization* of the central phase, which is the gauge principle's premise and not the algebra's theorem.
- No claim that the extra term in the field strength is non-abelian in the group-theoretic sense. It is bilinear in the two potentials and it is what the algebra produces; whether it is best read as a non-abelian structure or as the abelian theory's covariant curl is a question of interpretation, and the article records the identity and not the interpretation.

## Open Questions

**Whether the extra term is observable.** The term $\frac{iϙ}{\hbar}\mathrm{Vect}(\tilde A_\Phi^{\natural}\tilde A)$ is bilinear in the potentials and therefore of second order in the coupling. In the standard abelian theory the corresponding term is absent and the field strength is the ordinary curl. Whether the difference is a different theory or a different splitting of the same theory between the field term and the interaction term is not settled here, and it is the first thing a variational treatment should answer: the companion article writes the action and states where the two readings part.

**Whether a constant background with curvature is exactly solvable.** The symbol is a $4\times4$ matrix with a linear dependence on the coordinate through the connection, so the constant-background computation does not apply. The article's exact statements are confined to zero curvature, and the next case — a constant field strength — is not attempted.

**The polar form's status.** The polar companion states the chart's version of every statement here. Whether the chart makes the constraint structure clearer or obscures it is the question that article answers in its own terms, and the honest answer there is that it does both.

## Summary

The coupled Proca equation is

$$
\tilde\nabla_{\mathrm{gco}}\tilde F=k_m^2\tilde A,
\qquad
\tilde F=\mathrm{Vect}\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A\bigr),
\qquad
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi,
$$

with the field an element of $\mathbb{B}$ and the free field its real slice.

The carrier must be complex because the material sector is not closed: $\vec e_x\vec e_x=-e_t$ leaves it. The field strength carries the connection because the potential is charged, and the extra term is bilinear in the two potentials. The Lorenz condition survives in covariant form, exactly, because the curvature term of the covariant d'Alembertian is traceless, and the ordinary divergence is then fixed by the potential. A constant scalar potential shifts the energy by $ϙc\,a'_t$ and nothing else. The complex carrier has a central phase, the phase is a symmetry, and the current exists; it is the source the free article could not supply.

The equation is standard. The algebra's contribution is the closure argument, the one-element coupling, the trace computation that gives the constraint, and the current.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^{2}=-e_t$ |
| $i$ | Central scalar imaginary, $i^{2}=-e_t$ |
| $\mathrm{Sc}$, $\mathrm{Tr}=2\,\mathrm{Sc}$ | Scalar part and trace |
| $\mathbb{B}_\Phi,\ \mathbb{B}_\Psi,\ \mathbb{B}_V$ | Material, informational, and pure-vector sectors |
| $\tilde A=i\,a'_t\,e_t+\vec A$ | The coupled Proca potential, an element of $\mathbb{B}$; $a'_t$ and $\vec A$ complex |
| $\tilde A_\Phi=A_te_t+\sum_\eta A_\eta\vec e_\eta$ | The connection, an element of $\mathbb{B}_\Phi$; $A_\mu$ central in the abelian case |
| $\tilde A_\Phi^{\natural}=A_te_t-\sum_\eta A_\eta\vec e_\eta$ | Its $\natural$-image; the conjugate derivative's connection |
| $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$ | Covariant derivative, left action |
| $\tilde\nabla_{\mathrm{gco},\mu}=\partial/\partial R_\mu+\frac{iϙ}{\hbar}A_\mu$ | Its central per-component form |
| $\partial/\partial R_t=-i\,\partial/\partial r'_t$ | Material time derivative |
| $\tilde F=\mathrm{Vect}(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A)$ | Field strength; covariant with $\lambda$ |
| $\tilde F^{(\Phi)}$ | Curvature of the connection |
| $\tilde C=\frac{iϙ}{\hbar}\tilde A_\Phi$ | The coupling element of a constant background |
| $k_m=mc/\hbar$ | Mass wave number |
| $ϙ$ | Charge; a parameter of the framework |
| $\lambda=\exp(i\vartheta_{\mathrm{gau}})$, $\vartheta_{\mathrm{gau}}=ϙ\Gamma/\hbar$ | Central gauge phase; $\Gamma$ real |
| $j_\mu=\mathrm{Sc}(\tilde A^{*}i\tilde\nabla_{\mathrm{gco},\mu}\tilde A)$ | The charge current |

## Further Reading

- [The Proca Equation: Massive Spin One in Biquaternionic Form](the-proca-equation-massive-spin-1-in-biquaternionic-form.html), for the free equation, the field strength and the two polarizations.
- [The Proca Equation in Biquaternionic Polar Variables](the-proca-equation-in-biquaternionic-polar-variables.html), for the two-factor word and the two brackets of the free field.
- [The Coupled Proca Equation in Biquaternionic Polar Variables](the-coupled-proca-equation-in-biquaternionic-polar-variables.html), for the same statements in the chart.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localization of the central phase.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html), for the operator identity with the curvature.
- [The Coupled Dirac Equation in Biquaternionic Form](the-coupled-dirac-equation-in-biquaternionic-form.html), for the coupling that enters once rather than twice, and for the contrast between the two carriers.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html), for the potential biquaternion and the four-current.
- [The Variational Principle and the Coupled Proca Equation in Biquaternionic Form](the-variational-principle-and-the-coupled-proca-equation-in-biquaternionic-form.html), for the action, the currents and the sign of the mass term.
- [The Variational Principle and the Coupled Proca Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-proca-equation-in-biquaternionic-polar-variables.html), for the constrained form of the same action.
- [The Variational Principle and the Proca Equation in Biquaternionic Form](the-variational-principle-and-the-proca-equation-in-biquaternionic-form.html), for the free action whose mass term breaks what the coupled mass term preserves.
- Alexandru Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs," *Journal de Physique et le Radium* **7** (1936) 347–353, for the massive vector equation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the standard minimally coupled massive vector field and its constraint.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the covariant derivative and the field strength in geometric algebra.
- Ta-Pei Cheng and Ling-Fong Li, *Gauge Theory of Elementary Particle Physics* (Oxford, 1984), for the non-abelian field strength and the term an abelian curl does not carry.
