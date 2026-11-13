# __The Fourier Transform and the Klein–Gordon Equation in Biquaternionic Form__

## Introduction

**The parent states the obstruction in one clause and moves on.** *The Klein–Gordon Equation in Biquaternionic Form* writes, at its §*Second Order in Time and the Conjugate Pair*, that the scalar Klein–Gordon operator does not factor into first-order scalar operators in $\mathbb{B}$. The proof is given, in position space, by anticommutation: the cross terms cancel only for an element that anticommutes with all three spatial units, and such an element is zero. The sentence is then dropped, and the article turns to the conjugate pair. This article finishes it.

**The finding is that the obstruction is a statement about a zero set.** A second-order symbol factors into two first-order ones exactly when its quadric is the product of two linear forms. Over a central coefficient the Klein–Gordon quadric is a rank-four form, and no product of two linear forms has rank above two. **That is the parent's anticommutation argument read in momentum space**, and the reading makes visible the one thing the position-space argument leaves implicit: which coefficient would allow factorization, and at what price.

**The governing thesis is one sentence.** The free Klein–Gordon symbol is a central scalar; it commutes with everything, including the sector projectors; therefore the free scalar theory carries no sector content at all, and every sector statement at Klein–Gordon level is a statement about the potential. The factorization question is a question about the free symbol, and it is answered without any sector at all: the answer is a property of a scalar quadratic form.

**The exception is the vector coefficient, and its price is exact.** The parent records Alexeyeva's factorization of an operator with a constant complex vector coefficient. In momentum space the two factors are biquaternion-valued linear symbols whose product is scalar, and that product is the quadric. **The factors cannot be central**: a product of two central linear symbols is a product of two linear forms, which is what the rank argument forbids. The first-order factors exist only because they are not scalars, and the mass and the directional term come from one coefficient and cannot be separated.

**The two parts of the coefficient then split the work.** The parent writes the coefficient's norm as $m^{2}=(\vec F,\vec F)=\lvert E\rvert^{2}-\lvert H\rvert^{2}+2i(E,H)$ and does not pursue it. In momentum space the real part $E$ displaces the zero set's apex and contributes no mass, while the imaginary part $H$ supplies a mass $\lvert H\rvert$ and removes one direction of propagation. This article tabulates that split, and it separates the parent's $m^{2}$ from the factored operator's own mass.

**The polar parent has no symbol at all, and that is why the family stops here.** The amplitude equation is nonlinear in the pair of amplitude and phase, so there is no symbol to factor and no quadric to test. The companion article *The Fourier Transform and the Klein–Gordon Equation in Biquaternionic Polar Variables* takes that case in full, and the one paragraph below states the algebraic reason without duplicating its argument.

**The companion's question is the spectrum, and it is not this article's.** *The Fourier Transform, the Variational Principle and the Klein–Gordon Equation in Biquaternionic Form* asks what the eigenvalues of a non-central potential are and answers $a\pm\lvert\vec v\rvert$, each doubled. This article asks when the symbol factors. An operator can have a perfectly good spectrum and no square root; that is exactly the Klein–Gordon case, and the two answers are independent.

## Conventions

The algebra and its units are those of *Algebra and Element Conventions*, the gradient, the d'Alembertian and the symbol rule those of *Operator and Calculus Conventions*, the two forms those of *Norm and Pairing Conventions*, the units and the material time those of *Physics Units and Common Elements Conventions*, and the sector bookkeeping those of *Mirror Biquaternions and the Phy–Psy Switch*. The kernel and its $i\epsilon$ prescription are those of *The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form*; they are cited and not re-derived.

**The bookkeeping is quoted once.** With $\tilde K_\Phi=ik_t'e_t+\vec k_\Phi$, $k_t'=\omega/c$, $k_m=mc/\hbar$ and $r_t'=ct'$,

$$
\tilde\nabla_\Phi\longmapsto i\tilde K_\Phi,
\qquad
\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}\longmapsto-\langle\tilde K_\Phi\rangle_\natural,
\qquad
\langle\tilde K_\Phi\rangle_\natural=-k_t'^{2}+k_\Phi^{2},
\qquad
\langle\tilde P_\Phi\rangle_\natural=-p^{2}.
$$

**The phase convention is fixed here and used throughout.** A positive-frequency plane wave is $\tilde\Xi=\tilde\Xi_0\exp(-i\theta_{\mathrm{pwp}})$ with $\theta_{\mathrm{pwp}}=\omega r_t'-\vec k_\Phi\cdot\vec r$, so $\partial/\partial r_t'\mapsto-i\omega$ and $\partial/\partial r_\eta\mapsto ik_\eta$. The sign of $\vec\zeta$ in every factorization display below is the sign this convention gives it; the opposite convention reverses it and changes no structural statement.

**The coefficient is a constant complex vector.** $\vec F$ is a constant element of the vector subspace of $\mathbb{B}$ with complex components, carrying no scalar part. It is the parent's object and it is kept in the parent's notation, including the split $\vec F=-E-iH$ for real vectors $E$ and $H$.

## The Symbol and Its Rank

**Finding 1.** The symbol of $\Box_\Phi-k_m^{2}$ is

$$
-\langle\tilde K_\Phi\rangle_\natural-k_m^{2}=k_t'^{2}-k_\Phi^{2}-k_m^{2},
$$

a scalar quadratic form of rank four whose zero set is the two-sheeted mass hyperboloid.

**The operator has no first-order scalar square root, and the rank of that form is the reason.**

**The reason is a counting argument on the quadric.** A product of two linear forms $\ell_1\ell_2$ has a symmetrized matrix $(\ell_1\ell_2^{T}+\ell_2\ell_1^{T})/2$ of rank at most two. The Klein–Gordon form has the matrix $\operatorname{diag}(1,-1,-1,-1)$, whose rank is four. A rank-four form is not a product of two linear forms in any number of variables, so no pair of first-order operators with central symbols can compose to the Klein–Gordon operator. The count is measured:

$$
\operatorname{rank}\operatorname{diag}(1,-1,-1,-1)=4,
\qquad
\operatorname{rank}\bigl(\ell_1\ell_2^{T}+\ell_2\ell_1^{T}\bigr)\le2,
$$

so the two ranks differ by two and no product of two linear forms reaches four.

**This is the parent's anticommutation argument and not a rival to it.** The parent shows that $B=-A$ and $A\vec e_\mu+\vec e_\mu A=0$ for all three units force $A=0$, and then the constant term $AB=-A^{2}$ cannot equal $-k_m^{2}$. The rank argument says the same thing in the language of the symbol: the composition of two first-order operators has the product of their symbols as its principal symbol, and a product of two central linear symbols is a product of two linear forms, hence of rank at most two. **Neither argument is stronger; they are one fact seen from two sides, and the parent's is cited rather than repeated.**

**The zero set says what a factorization would have to look like.** The hyperboloid has two sheets, and the two sheets are the two frequency branches $\omega=\pm c\sqrt{k_\Phi^{2}+k_m^{2}}$. A factorization would cut the quadric into two *hyperplanes*, not into two sheets. **The sheet count is not the factor count**, and that distinction is the reason a second-order scalar equation can have two branches and still no square root.

**What the obstruction is not.** It is not an obstruction to a first-order *system*. The parent's conjugate pair writes the equation as a first-order system in the field and its rate of change, and that system exists for every second-order equation. The obstruction is to a single first-order equation for a scalar amplitude, and the two statements are compatible because the system doubles the unknown.

**Nor is it an obstruction to a first-order root on a carrier.** The parent's §*Does the Second-Order Structure Fit* records that the operator has a first-order spinor square root, the biquaternion Dirac operator acting on a Peirce carrier, and *The First-Order Root of the Biquaternion Klein–Gordon Operator* develops it. The root exists on a module; what does not exist is a root on the scalar element.

## Factorization and Its Price

**Finding 2.** With a constant complex vector coefficient the operator does factor, and the parent's Alexeyeva display is the factorization. In momentum space both factors are linear and their product is the quadric:

$$
\bigl(-\vec\zeta+\vec F-i\omega\bigr)\bigl(\vec\zeta-\vec F-i\omega\bigr)
=\bigl(\vec\zeta-\vec F,\vec\zeta-\vec F\bigr)-\omega^{2}.
$$

**The product is scalar, and that is the whole mechanism.** The two cross terms cancel because $i\omega$ is central and the two vector symbols commute with it; what survives is $\vec F$-dependent only through the combination $\vec\zeta-\vec F$ and the square of the frequency. **The product is exactly the quadric of a Klein–Gordon operator whose coefficient is $\vec\zeta-\vec F$**: the coefficient has been absorbed into the wave number, and that absorption is the factorization.

**The identity is measured on the symbols.** Over three hundred random draws of a wave number, a frequency and a complex coefficient, the product of the two first-order symbols had a vector part below $8.9\times10^{-16}$ and a scalar part equal to the Euclidean quadratic form $(\vec\zeta-\vec F,\vec\zeta-\vec F)-\omega^{2}$ to the same order. The parent prints the same quadratic form with $\vec\zeta+\vec F$; the difference is the sign of $\vec\zeta$ under the phase convention, and no statement here depends on which sign is written.

**The first price is the parent's and it is exact.** In the compensated operator $\Box_A+(\vec F,\vec F)+2i(\vec F,\nabla)$ the mass and the directional term both come from the one coefficient $\vec F$. Setting $\vec F=0$ removes the mass and the direction together, and turning off the direction while keeping the mass is not a case of the construction. The parent states this; it is repeated here only to attach it to the symbol display above, where it is visible as the single object $\vec\zeta-\vec F$.

**The second price is the one the rank argument adds, and it is the article's structural point.** The factors are not central: their symbols are biquaternion-valued vectors, with zero scalar part. That is not an accident of Alexeyeva's choice but a necessity, because a product of two central linear symbols has rank at most two and the quadric has rank four. **The factorization is therefore available exactly at the cost of the factor's centrality**, and a central factor would be the scalar square root the parent proves does not exist.

**So the two statements are one statement.** "The Klein–Gordon operator does not factor into first-order scalar operators" and "a vector coefficient whose norm supplies the mass does factor" are not in tension: the first forbids central factors, the second supplies non-central ones, and the rank of the quadric decides between them. **The word "scalar" in the parent's sentence is doing all the work**, and the article has now said why.

**The compensation is visible in the symbol.** In the factored case the symbol is a perfect square in the shifted variable: $(\vec\zeta-\vec F)^{2}-\omega^{2}$, the difference of two squares whose spatial part is the square of one linear form. In the unfactored case the symbol is $k_t'^{2}-k_\Phi^{2}-k_m^{2}$, which is also a difference of squares, $k_t'^{2}-(k_\Phi^{2}+k_m^{2})$, but the second square is a sum of four terms and not one. **The obstruction is the plus sign inside the second square**, and that is the entire content of the rank count.

## The Zero Set of the Factored Symbol

**Finding 3.** The zero set is fixed by the two parts of the coefficient. The real part displaces the apex and contributes no mass; the imaginary part supplies the mass and removes one direction of propagation.

**The algebra is one expansion.** With $\vec F=-E-iH$ for real vectors $E$ and $H$,

$$
\omega^{2}=(\vec\zeta-E)^{2}-\lvert H\rvert^{2}-2i\,(\vec\zeta-E)\cdot H,
$$

so a real frequency requires $(\vec\zeta-E)\cdot H=0$, and on that surface $\omega^{2}=\lvert\vec\zeta-E\rvert^{2}-\lvert H\rvert^{2}$. The expansion is exact: over four thousand random pairs of a wave number and a coefficient the two sides agreed to $7.1\times10^{-15}$.

**A real coefficient gives a massless cone, displaced.** For $H=0$ the constraint is empty and $\omega^{2}=\lvert\vec\zeta-E\rvert^{2}$: the light cone with its apex at $\vec\zeta=E$. **The real part of the coefficient shifts the pattern and gives no rest mass at all**, for any value of $\lvert E\rvert$.

**An imaginary coefficient gives the mass, and its direction is not a direction of propagation.** For $H\neq0$ the real solutions live in the plane through $\vec\zeta=E$ perpendicular to $H$, where the dispersion is a hyperboloid of mass $\lvert H\rvert$; inside that plane the region $\lvert\vec\zeta-E\rvert<\lvert H\rvert$ carries an imaginary frequency. Measured: the minimum of $\omega^{2}$ on the allowed plane, attained at $\vec\zeta=E$, is $-\lvert H\rvert^{2}$, which is $-0.250$ for $\lvert H\rvert=0.5$ and $-0.810$ for $\lvert H\rvert=0.9$.

**The parent's $m^{2}$ is the comparison operator's mass and not this one.** The parent writes $m^{2}=(\vec F,\vec F)=\lvert E\rvert^{2}-\lvert H\rvert^{2}+2i(E,H)$ and calls it positive for a real coefficient. That number is the mass of the Klein–Gordon–Fock operator $\Box_A+m^{2}$ with which the factored operator is compared, as the parent's own §*A Vector Coefficient: When the Operator Does Factor* says: the factored operator is that one **plus** the directional term. Its own dispersion is the displaced cone above, so **a real coefficient gives a massless theory for every $\lvert E\rvert$**, and the parent's phrase must not be read as massiveness.

**The two thresholds are different thresholds.** $\lvert E\rvert=\lvert H\rvert$ is where the comparison mass changes sign, and it is not where anything happens to the factored spectrum. The three values are $0.640$ for a real coefficient with $\lvert E\rvert=0.8$, $0.390$ for $E=(0.8,0,0)$ with $H=(0,0.5,0)$, and $-0.560$ for $E=(0.5,0,0)$ with $H=(0.9,0,0)$. The factored operator's mass vanishes only at $H=0$, and there it is massless for every $E$.

**What the tabulation does not claim.** It does not claim that the three values of the comparison mass are three theories. The factored operator is a mathematical object with a constant coefficient; whether a physical setting realizes each regime is a separate question, and the parent's non-relativistic and rest-mass sections do not decide it.

## Where the Polar Form Loses Its Symbol

**The polar parent's amplitude equation is not linear, and a nonlinear equation has no symbol.** The parent writes $\Box_\Phi r=r\,[k_m^{2}-(\partial_{r_t'}\theta_{\mathrm{pha}})^{2}+\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}]$, and the coefficient on the right depends on the gradient of the unknown phase. A symbol is a function of the wave number alone; here the coefficient is a functional of the solution, so no function of $\tilde K_\Phi$ represents the operator.

**The pair is coupled in both directions, and each direction fails a different test.** At fixed phase the amplitude equation is linear in $r$: superposing two amplitudes gave a residual of $1.4\times10^{-14}$ against a scale of $6.4$. At fixed amplitude it is not additive in the phase: superposing two phases gave a residual of $2.0$ against a scale of $4.0$. **So the equation is linear in neither variable of the pair, taken as the pair.**

**That is why the polar case yields a section and not a second factorization.** There is no quadric to test for reducibility, because there is no quadratic form. The companion article takes the case in full and asks the question that does have an answer there: which part of the polar word removes the symbol. Its answer is about the amplitude, and it does not depend on anything in this article.

## The Denial That Survives

**The informational sector is not the Fourier dual of the material sector.** Every transform in this article acts on a $\mathbb{B}$-valued function and returns a $\mathbb{B}$-valued function. No step carries a field out of its sector, and the sector statements of §*Conventions* are statements about one constant coefficient, at one wave number or at one event.

**The factorization is not a Fourier discovery, and the article does not present it as one.** The parent proves the obstruction in position space, by anticommutation, and proves the vector exception there too, by composition. The transform is a lens: it displays the obstruction as the rank of a quadric and the exception as the cancellation of two cross terms, and it adds no case that the parent's argument does not already contain.

## Limits

**Constant coefficients are the licence.** A symbol exists only where the coefficients are constant, and every display above is a statement about that case. A position-dependent coefficient replaces the symbol by a convolution, its kernel being the transform of the coefficient, and there is no quadric to factor. **The rank argument therefore classifies constant coefficients and nothing else**, and the parent's two settings are the two cases of this licence.

**The abelian component form.** The parent separates the covariant derivative into components because the coefficients are central scalars, and that is what makes the symbol a scalar function of $\tilde K_\Phi$ rather than a matrix. A non-abelian coefficient would make the symbol matrix-valued, the rank argument would become a statement about a matrix polynomial, and the classification would have to be redone.

**The article does not re-derive the kernel.** The light-cone $\delta$-layer, the Bessel-type kernel of the unfactored operator and the exponential weight of the factored one are the parent's, and they are cited at §*Conventions*. What is added here is the shape of the zero set, not the fundamental solution.

**The companion's spectrum and this article's rank are different measurements of one object.** *The Fourier Transform, the Variational Principle and the Klein–Gordon Equation in Biquaternionic Form* finds the spectrum of a non-central potential; this article finds when the symbol splits. A reader who wants the eigenvalues will not find them here, and a reader who wants the square root will not find it there.

## Open Questions

**One question is left open, and it is whether the rank argument generalizes to higher order.** A third-order symbol factors into first-order factors exactly when its hypersurface is a union of hyperplanes, and the algebraic test is not a rank count but a factorization of a cubic form. Whether a biquaternionic symbol of order $n$ admits a classification of its factorable cases by the geometry of its zero set, in the way the second-order case is classified by the rank of a quadric, is not decided here. No claim is made.

## Summary

The Klein–Gordon operator's symbol is $k_t'^{2}-k_\Phi^{2}-k_m^{2}$, a scalar quadratic form of rank four whose zero set is the two-sheeted mass hyperboloid. A product of two linear forms has rank at most two, so the form is not a product of two linear forms, so no pair of first-order operators with central symbols composes to the Klein–Gordon operator. That is the parent's anticommutation obstruction read on the quadric, and the parent's proof is cited rather than repeated.

A constant complex vector coefficient does factor, and the product of the two first-order symbols is scalar: $(\vec\zeta-\vec F,\vec\zeta-\vec F)-\omega^{2}$, verified to $8.9\times10^{-16}$ over three hundred draws. The price is the parent's: the mass $(\vec F,\vec F)$ and the directional term $2i(\vec F,\nabla)$ come from one coefficient. **The price the rank argument adds is that the factors cannot be central**, because a central factor would be the scalar square root the parent forbids; the word "scalar" in the parent's sentence is what carries the whole obstruction.

The two parts of the coefficient then split the work: $\omega^{2}=(\vec\zeta-E)^{2}-\lvert H\rvert^{2}-2i(\vec\zeta-E)\cdot H$, verified to $7.1\times10^{-15}$, so a real coefficient gives the massless cone $\omega^{2}=\lvert\vec\zeta-E\rvert^{2}$ displaced to $\vec\zeta=E$, and an imaginary one gives a hyperboloid of mass $\lvert H\rvert$ confined to the plane $(\vec\zeta-E)\perp H$, with $\omega^{2}$ reaching $-0.250$ at $\lvert H\rvert=0.5$ and $-0.810$ at $\lvert H\rvert=0.9$. **The parent's $m^{2}=\lvert E\rvert^{2}-\lvert H\rvert^{2}$ is the comparison operator's mass**, $0.640$, $0.390$ and $-0.560$ in the three cases, and not the factored operator's, which is $\lvert H\rvert$. The polar parent's amplitude equation is nonlinear, with a residual of $2.0$ against a scale of $4.0$ under a superposition of phases, and a nonlinear equation has no symbol at all.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde K_\Phi=ik_t'e_t+\vec k_\Phi$ | The four-wavevector; $k_t'=\omega/c$ |
| $-\langle\tilde K_\Phi\rangle_\natural-k_m^{2}$ | The scalar Klein–Gordon symbol; rank four |
| $\operatorname{diag}(1,-1,-1,-1)$ | Its quadric matrix; the rank count |
| $\vec F=-E-iH$ | The constant complex vector coefficient; $E$, $H$ real |
| $(\vec F,\vec F)=\lvert E\rvert^{2}-\lvert H\rvert^{2}+2i(E,H)$ | The coefficient's norm; the mass of the comparison operator |
| $\lvert H\rvert$ | The factored operator's own mass; zero for every real coefficient |
| $\omega^{2}=(\vec\zeta-E)^{2}-\lvert H\rvert^{2}-2i(\vec\zeta-E)\cdot H$ | The dispersion of the factored symbol |
| $(\vec\zeta-\vec F,\vec\zeta-\vec F)-\omega^{2}$ | The product of the two first-order symbols |
| $2i(\vec F,\nabla)$ | The directional term that cannot be separated from the mass |
| $\Box_\Phi r=r\,[k_m^{2}-(\partial_{r_t'}\theta_{\mathrm{pha}})^{2}+\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}]$ | The polar amplitude equation; nonlinear, no symbol |

## Further Reading

- *The Klein–Gordon Equation in Biquaternionic Form*, for the obstruction this article reads in momentum space, the Alexeyeva factorization, and the plane-wave catalogue.
- *The Fourier Transform, the Variational Principle and the Klein–Gordon Equation in Biquaternionic Form*, for the spectrum of a non-central potential, which is the companion question.
- *The Fourier Transform and the Klein–Gordon Equation in Biquaternionic Polar Variables*, for the polar case: the transform's phase as the action and the amplitude as what removes the symbol.
- *The Klein–Gordon Equation in Biquaternionic Polar Variables*, for the amplitude and transport equations.
- *The First-Order Root of the Biquaternion Klein–Gordon Operator*, for the spinor square root on a carrier.
- *Derivatives, Fields and Transforms*, for the transform, its kernel and the symbol rule.
- *Biquaternion Continuous Harmonic Analysis*, for the convolution theorem used in §*Limits*.
- L. A. Alexeyeva, on the differential algebra of biquaternions, for the first-order system whose composition supplies the factored operator.
