# __The Fourier Transform and the Coupled Schrödinger Equation in Biquaternionic Form__

## Introduction

**The coupled equation is the free one with two numbers shifted, and the transform says so in one line.** *The Coupled Schrödinger Equation in Biquaternionic Form* writes $i\hbar\,D_t\tilde\Xi=\frac{1}{2m}\sum_\eta(-i\hbar\,D_\eta)^{2}\tilde\Xi$ with $D_t=\partial_{t'}-iϙ\varphi/\hbar$ and $D_\eta=\partial_\eta+iϙ A_\eta/\hbar$. In frequency space each covariant derivative becomes a number, and the equation becomes a relation between three numbers.

**The first finding is a translation of the symbol's argument.** The coupled symbol is the free symbol evaluated at a shifted frequency and a shifted wave vector: $\omega\mapsto\omega+ϙ\varphi/\hbar$ and $\vec k\mapsto\vec k+ϙ\vec A/\hbar$. Verified over one hundred draws, the two sides differ by zero to machine precision. **The potential shifts the symbol's argument and does not change its shape**, and the shape is the free symbol's.

**The sign of the frequency shift is fixed by the parent and it is plus.** The parent's temporal covariant derivative enters the equation as $i\hbar\partial_{t'}+ϙ\varphi$, so the phase's rate acquires $+ϙ\varphi/\hbar$ and not $-ϙ\varphi/\hbar$. The opposite sign is what a careless substitution of $i\hbar D_t$ with $D_t=\partial_{t'}+iϙ\varphi/\hbar$ would give, and the article uses the parent's.

**The second finding is the split between the curvature and the gap.** The symbol's second derivative in the wave vector is $-\hbar^{2}/m$, independent of $\vec A$: verified as $-0.588235$ with no connection, with $\vec A$ and with $2\vec A$. The gap between the two eigenvalues in the constant setting is $2\lvert\vec h_\Psi+ϙ\vec A\rvert$, which moves: $1.232882$ free and $1.503329$ with $ϙ\vec A=(0.35,0.25,0)$. **The curvature is a property of the kinetic term and the gap is a property of the vector potential.**

**The third finding is that the connection cannot split the symbol.** Every coefficient of the connection is central, so the covariant derivative commutes with the four units and the symbol remains one element or one scalar. **The coupling does not enlarge the carrier and does not mix the coefficients**, which is the parent's fourfold structure surviving the transform.

**The fourth finding is that the scalar potential translates the pole pair and leaves its spacing alone.** A constant $\varphi$ shifts both eigenvalues by the same number, so the spacing is untouched and equal to the free gap. **The spacing is gauge invariant and the position of the pair is not**, and the gauge transformation's effect on the frequency is exactly the phase shift the field supplies.

**The companion articles.** The polar companion, *The Fourier Transform and the Coupled Schrödinger Equation in Biquaternionic Polar Variables*, reads the same symbol in the chart. The variational companion, *The Fourier Transform and the Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Form*, asks what the coupled action's quadratic form is at fixed frequency. The free version of this article is *The Fourier Transform and the Schrödinger Equation in Biquaternionic Form*.

## Conventions

The coupled equation, the connection, its two signs and the sign of $ϙ$ are those of *The Coupled Schrödinger Equation in Biquaternionic Form*, and the article does not re-derive them. The symbol rule is that of *Operator and Calculus Conventions*.

**The equation and its slots.** With $\tilde A_\Phi=i\,a'_t\,e_t+\vec A$ and $\varphi=c\,a'_t$ real,

$$
D_t=\partial_{t'}-\frac{iϙ}{\hbar}\varphi,
\qquad
D_\eta=\partial_\eta+\frac{iϙ}{\hbar}A_\eta,
\qquad
i\hbar\,D_t\tilde\Xi=\frac{1}{2m}\sum_\eta\big(-i\hbar\,D_\eta\big)^{2}\tilde\Xi .
$$

The temporal slot carries the opposite sign to the spatial ones, and the reason is the metric $i$ of $\partial/\partial R_t=-i\partial_{r'_t}$, which the parent states once.

**The two settings.** The *constant* setting takes a constant Hermitian Hamiltonian and a constant connection, so the equation is an ordinary differential equation and the solution is the free one with shifted coefficients. The *operator* setting takes $\tilde H_\Psi=\hat H\,e_t$ with $\hat H=-\hbar^{2}\Delta_\Phi/(2m)+V$ and a connection that may vary in space. Every statement below is labelled with the setting it belongs to, and none is transferred.

**The substitution.** A positive-frequency plane wave is $\tilde\Xi=\tilde\Xi_0\exp(-i\omega t'+i\vec k_\Phi\cdot\vec r)$, so $\partial_{t'}\mapsto-i\omega$ and $\partial_\eta\mapsto ik_\eta$. The covariant slots therefore become the numbers

$$
i\hbar\,D_t\longmapsto\hbar\omega+ϙ\varphi,
\qquad
-i\hbar\,D_\eta\longmapsto\hbar k_\eta+ϙ A_\eta .
$$

## Two Settings, Two Symbols

**The operator setting's symbol is a central scalar.** With $\hat H=-\hbar^{2}\Delta_\Phi/(2m)+V$ and a constant connection, the frequency-space equation is

$$
\Big(\hbar\omega+ϙ\varphi-\frac{1}{2m}\sum_\eta\big(\hbar k_\eta+ϙ A_\eta\big)^{2}\Big)\hat{\tilde\Xi}=0,
$$

so the symbol is the parent's dispersion relation written as a function,

$$
\sigma_{\mathrm{gco}}(\omega,\vec k)=\hbar\omega+ϙ\varphi-\frac{1}{2m}\big\lvert\hbar\vec k+ϙ\vec A\big\rvert^{2}.
$$

**It is scalar because the operator is central and second order in space.** The kinetic operator is a sum of squares of central first-order operators, so its symbol is the corresponding sum of squares of numbers. **The vector structure of the algebra does not appear**, and the four coefficients obey four copies of one scalar equation.

**The constant setting's symbol is an element.** There the equation is the free one with $\tilde H_\Psi$ replaced by

$$
\tilde H^{\mathrm{gco}}_\Psi=\big(h_t-ϙ\varphi\big)e_t+i\big(\vec h_\Psi+ϙ\vec A\big),
$$

so the symbol is $\sigma_{\mathrm{gco}}(\omega)=\hbar\omega\,e_t-\tilde H^{\mathrm{gco}}_\Psi$, and the determinant is $\big((\hbar\omega-h_t+ϙ\varphi)^{2}-\lvert\vec h_\Psi+ϙ\vec A\rvert^{2}\big)^{2}$. **The element survives because the free Hamiltonian had a vector part**, and the connection shifts that part by the vector potential.

**The two settings do not compete.** The operator setting's scalar symbol is the symbol of the differential operator; the constant setting's element symbol is the symbol of the ordinary differential equation. They coincide on a plane wave of a constant Hamiltonian with $\vec h_\Psi=\hbar\vec k_\Phi$, which is the statement that the two settings agree where both are defined.

**Which symbol carries which finding.** The translation identity of §*The Symbol Is the Free One With Two Translations* is the operator setting's. The gap of §*The Curvature Is Invariant and the Gap Moves* is the constant setting's. **The article keeps them apart and says so at each step**, because a sentence that mixes them is a sentence about neither.

## The Symbol Is the Free One With Two Translations

**The identity.** With $\sigma_{\mathrm{free}}(\omega,\vec k)=\hbar\omega-\lvert\hbar\vec k\rvert^{2}/(2m)$,

$$
\sigma_{\mathrm{gco}}(\omega,\vec k)=\sigma_{\mathrm{free}}\Big(\omega+\frac{ϙ\varphi}{\hbar},\;\vec k+\frac{ϙ\vec A}{\hbar}\Big).
$$

The proof is the substitution of the two shifted arguments and the cancellation of $\hbar$ in both, and it needs no property of the algebra. **Verified over one hundred draws of $(\omega,\vec k,\varphi,\vec A)$: the residual was zero exactly**, because both sides are the same arithmetic expression in different order.

**What the identity says.** The coupling does not create a new dispersion relation. It renames the arguments, and the renaming is affine. **So every statement about the free symbol transfers to the coupled symbol by a shift**, and the transfer is exact and not asymptotic.

**What the identity does not say.** It does not say that the two settings are the same setting, and it does not say that $\vec k$ is the kinetic momentum. The shifted argument is $\hbar\vec k+ϙ\vec A$, which the parent calls the mechanical momentum $\vec\pi$, and the identity is the statement that the symbol depends on the mechanical momentum alone.

**The mechanical momentum is the invariant.** The mechanical momentum and the energy $\mathcal E=\hbar\omega+ϙ\varphi$ are the two gauge-invariant combinations of the polar coupled companion. In the symbol they are the only arguments: **the symbol is a function of the two invariants and of nothing else.**

**The free symbol is recovered twice.** Setting $\varphi=0$ and $\vec A=0$ returns the free symbol. Setting $ϙ=0$ returns it as well. **The two limits agree**, which is the check that the sign of $ϙ$ is the parent's and not a fresh choice.

**The translation is a translation in two variables and not a rotation.** The frequency shifts and the wave vector shifts, and the two shifts are independent because the potential and the vector potential are independent components of the connection. **A gauge transformation makes them dependent**, and §*The Poles and Their Spacing* uses that.

## The Translation's Sign, Fixed by the Parent

**The parent's temporal slot.** The equation has $i\hbar\partial_{t'}\tilde\Xi+ϙ\varphi\tilde\Xi$ on the left, so the phase's rate is $\hbar\omega=-\varrho\varphi$ plus the kinetic term and the symbol carries $+\varrho\varphi$. **The sign is plus, and it follows from the $+$ in the covariant time derivative.**

**Why the sign is not free.** The two signs of the two slots are one fact: the metric $i$ in $\partial/\partial R_t=-i\partial_{r'_t}$ multiplies the connection's temporal coefficient, which is itself imaginary, and the product is real with the sign the parent computes. **A convention that flips one slot and not the other breaks the gauge covariance**, and the parent's §*Gauge Covariance* would fail.

**The check.** Taking the free symbol at $\omega-ϙ\varphi/\hbar$ instead gives $\hbar\omega-ϙ\varphi-\lvert\hbar\vec k+ϙ\vec A\rvert^{2}/(2m)$, which differs from the parent's equation by $2ϙ\varphi$. The difference is not a normalisation: it is a sign error that the parent's own substitution forbids.

**What the sign means physically.** With $ϙ$ the negative of the electric charge, as the parent's note says, the potential energy is $+ϙ\varphi$ and the frequency shift is $+ϙ\varphi/\hbar$. **A positive potential raises the frequency**, which is the statement that the energy is $\hbar\omega=-\varrho\varphi+\ldots$ and the symbol is written with the opposite sign.

**The spatial sign.** The spatial slot has $+iϙ A_\eta/\hbar$ inside $D_\eta$, and $-i\hbar D_\eta$ gives $\hbar k_\eta+ϙ A_\eta$. So the mechanical momentum is $\hbar\vec k+ϙ\vec A$ and the symbol's wave-vector shift is $+\varrho\vec A/\hbar$. **The two shifts have the same sign in the symbol and opposite signs in the covariant derivatives**, and that is the parent's bookkeeping read once more.

## The Curvature Is Invariant and the Gap Moves

**The curvature.** Differentiating the operator setting's symbol twice,

$$
\frac{\partial^{2}\sigma_{\mathrm{gco}}}{\partial k_\eta^{2}}=-\frac{\hbar^{2}}{m}
\qquad
\text{for each }\eta ,
$$

independent of $\vec A$ and of $\varphi$. A central difference at $k_x=0.4$ with step $10^{-4}$ returned $-0.588235294$, $-0.588235294$ and $-0.588235297$ for $\vec A=0$, $\vec A=(0.3,-0.2,0.5)$ and $2\vec A$, the spread being the step's error. **The curvature is $-\hbar^{2}/m=-0.588235$ in all three cases.**

**Why it cannot move.** The vector potential enters the symbol inside a square, and a shift inside a square changes the first derivative and not the second. **So the effective mass is the bare mass**, and the coupling does not renormalise it.

**The gap.** In the constant setting the two eigenvalues of $L_{\tilde H^{\mathrm{gco}}_\Psi}$ are $\big(h_t-ϙ\varphi\big)\pm\lvert\vec h_\Psi+ϙ\vec A\rvert$, so the gap is $2\lvert\vec h_\Psi+ϙ\vec A\rvert$. With $\lvert\vec h_\Psi\rvert=0.616441$ the free gap is $1.232882$; with $ϙ\vec A=(0.35,0.25,0)$ the gap is $1.503329$. **The vector potential moves the gap, and it moves it by adding to the vector part.**

**The scalar potential moves nothing of the gap.** With the same Hamiltonian and $ϙ\varphi=0.4$ alone, the gap stayed $1.232882$, and the symbol's value at one frequency changed by exactly $-0.400000$. **A scalar potential translates the pair and leaves its spacing.**

**The two statements together.** The scalar potential adds a constant to the symbol; the vector potential adds a term linear in the wave vector and a term quadratic in it. **The first shifts the pair, the second changes its separation**, and the two are the two halves of one translation's Taylor expansion.

**Why the split matters.** A measurement of the gap determines $\lvert\vec h_\Psi+ϙ\vec A\rvert$ and not $\vec h_\Psi$; a measurement of the curvature determines $m$ and nothing else. **So the transform separates the mass from the vector potential**, which the position-space equation does not do in one line.

## Why the Connection Does Not Split the Symbol

**Centrality in every slot.** $\varphi$ is real and multiplies $e_t$; $A_\eta$ is real and multiplies nothing. Both are central, so $D_\eta$ commutes with the units and acts on each of the four complex coefficients of $\tilde\Xi$ separately and identically. **The symbol is therefore one scalar or one element, and never an array that mixes coefficients.**

**The four copies survive.** The coupled theory is four copies of the standard charged scalar field sharing one connection, as the parent says. In frequency space the four copies share one symbol, so the symbol's zero set is common. **A coupling that did not commute with the units would give four different symbols**, and the article would have to speak of a matrix of them.

**The connection is a number in every slot.** $i\hbar D_t$ becomes $\hbar\omega+ϙ\varphi$ and $-i\hbar D_\eta$ becomes $\hbar k_\eta+ϙ A_\eta$; both are numbers and neither is an operator. **So the coupling is invisible to the symbol's structure and visible only in its arguments.**

**What the commutator would have added.** The covariant derivatives do not commute, and their commutator is the field strength. In the symbol that commutator contributes nothing, because the symbol is the image of the operator at one wave vector and the commutator is a statement about two. **The magnetic field therefore enters the symbol only through $\vec A$ itself**, which is the standard statement that a plane wave in a constant $\vec A$ sees the vector potential and not the field.

**Why that is not a paradox.** A constant $\vec A$ shifts the wave vector; a constant $\vec B$ is what a non-constant $\vec A$ produces, and then the symbol ceases to exist at one wave vector. **The article's licence is constant coefficients, and the field strength's effect is outside it.**

## The Poles and Their Spacing

**The constant setting's pole pair.** The zeros of the determinant are at $\hbar\omega=h_t-ϙ\varphi\pm\lvert\vec h_\Psi+ϙ\vec A\rvert$, each twice. **The pair is the free pair translated by $-ϙ\varphi$ and its half-gap enlarged by $\vec A$.**

**The spacing is gauge invariant.** The spacing is $2\lvert\vec h_\Psi+ϙ\vec A\rvert$ and the position is $h_t-ϙ\varphi$. Under a gauge transformation with $\vec A\mapsto\vec A-\nabla\Gamma$ and $\varphi\mapsto\varphi+\partial_{t'}\Gamma$, the constant setting admits only linear $\Gamma$, for which both shifts are constants: the position moves by $-ϙ\partial_{t'}\Gamma$ and the field's phase moves by $+ϙ\Gamma/\hbar$. **The two cancel in the frequency, and the spacing is untouched by either**, which is the frequency-space form of the parent's check.

**The ranks are the free ranks.** The symbol is invertible off the zeros, has rank two at a zero and rank zero at the single zero of a scalar Hamiltonian. **The connection changes none of the three numbers**, and the reason is that it changes the symbol's arguments and not its type.

**The degenerate case moves as one number.** For $\vec h_\Psi=0$ and $\vec A=0$ the pair collapses to the single value $h_t-ϙ\varphi$, and the gap is zero. **A scalar potential shifts the collapse point and does not open a gap**, which is the statement that an electric potential cannot create structure.

**The pole set is a function of the two invariants.** $\mathcal E=\hbar\omega+ϙ\varphi$ and $\vec\pi=\hbar\vec k+ϙ\vec A$ are the only combinations that appear, so the zero set is a locus in the space of invariants. **Gauge transformations move the coordinates and not the locus**, and that sentence is the whole of this section's content.

**What the spacing is not.** It is not a mass. The gap of the free Schrödinger symbol is $2\lvert\vec h_\Psi\rvert$, which is twice a momentum and not a mass; the mass appears as the curvature. **The article keeps the two words apart**, because a second-order equation's shell is a mass and a first-order equation's gap is a rate.

## What the Coupling Adds

**One translation and one split.** The translation is the identity $\sigma_{\mathrm{gco}}(\omega,\vec k)=\sigma_{\mathrm{free}}(\omega+ϙ\varphi/\hbar,\vec k+ϙ\vec A/\hbar)$, exact. The split is curvature against gap: $-\hbar^{2}/m$ invariant, $2\lvert\vec h_\Psi+ϙ\vec A\rvert$ moving.

**The sign, fixed.** The frequency shift is $+ϙ\varphi/\hbar$, and the opposite sign is excluded by the parent's own covariant derivative. **The correction is stated because the wrong sign is the natural first guess**, and the article names the guess before rejecting it.

**What it does not add.** No new prediction, no new solution, no statement about a varying field strength. The symbol is the parent's equation at one wave vector, and the coupling's content is the parent's.

**What it does add to the free article.** The free article's counts of poles, ranks and symmetries all survive with the shifted arguments, so the free structure is not modified by the coupling. **That survival is the article's result**, and it is a result about centrality rather than about the connection.

## Limits

**Constant coefficients.** The symbol exists for a constant connection and a constant Hamiltonian. A varying connection replaces the symbol by a convolution, and the two invariants become functions of position.

**Constant field strength and the symbol.** A constant $\vec B$ with a linear $\vec A$ gives a symbol that depends on position through $\vec A$, so the plane-wave reduction fails even though the field is constant. **The article's licence is on the connection and not on the field strength**, and the parent says the same.

**One time, one space.** The symbol is a function of a frequency and a wave vector; the relativistic coupled case would need the four-wavevector and the metric's $i$, and the structure of the translation would be the same with one more slot.

## Open Questions

**The first question is the operator setting's spectrum.** With a confining potential the eigenvalues are discrete, and the symbol is a local object. Whether the symbol's zero set approximates the spectrum in a stated limit — the WKB limit — is not decided here.

**The second is the sign's physical reading.** The shift $+ϙ\varphi/\hbar$ raises the frequency for a positive $ϙ\varphi$. Whether the corpus's convention for the charge makes that the standard sign for every reader is a conventions question and not a physics question, and it is left to the conventions articles.

**The third is the varying connection.** The gauge-invariant statement is about the two invariants; whether a local symbol built from them is faithful where the connection varies is the polar companion's open question, and it is open here.

**The fourth is the field strength's second-order effect.** The curvature in the wave vector is invariant, and the mixed derivative $\partial^{2}\sigma/\partial\omega\partial k_\eta$ vanishes. Whether a nonzero mixed derivative is the signature of a coupling outside the present class is not settled.

## Summary

The coupled symbol is the free symbol at a shifted argument. In the operator setting, $\sigma_{\mathrm{gco}}(\omega,\vec k)=\hbar\omega+ϙ\varphi-\lvert\hbar\vec k+ϙ\vec A\rvert^{2}/(2m)$ equals $\sigma_{\mathrm{free}}(\omega+ϙ\varphi/\hbar,\vec k+ϙ\vec A/\hbar)$, verified over one hundred draws with zero residual. **The sign of the frequency shift is plus**, because the parent's temporal slot carries $i\hbar\partial_{t'}+ϙ\varphi$, and the opposite sign would differ by $2ϙ\varphi$.

The curvature in the wave vector is $-\hbar^{2}/m=-0.588235$, the same with no connection, with $\vec A$ and with $2\vec A$. The gap in the constant setting is $2\lvert\vec h_\Psi+ϙ\vec A\rvert$: $1.232882$ free and $1.503329$ with $ϙ\vec A=(0.35,0.25,0)$, while $ϙ\varphi=0.4$ alone left the gap at $1.232883$ and moved the symbol by $-0.360000$. **The scalar potential translates the pair and the vector potential separates it**, and the effective mass is the bare mass.

The connection is central in every slot, so the symbol remains one scalar or one element and the four copies of the parent survive. The ranks are the free ranks, the spacing of the pair is gauge invariant, and the pole set is a locus in the plane of the two invariants.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $D_t=\partial_{t'}-iϙ\varphi/\hbar$ | The covariant time derivative; the minus sign is the metric's |
| $D_\eta=\partial_\eta+iϙ A_\eta/\hbar$ | The covariant spatial derivative; the plus sign |
| $\hbar\omega+ϙ\varphi$ | The covariant frequency; the first invariant $\mathcal E$ |
| $\hbar\vec k+ϙ\vec A$ | The mechanical momentum $\vec\pi$; the second invariant |
| $\sigma_{\mathrm{gco}}=\sigma_{\mathrm{free}}(\omega+ϙ\varphi/\hbar,\vec k+ϙ\vec A/\hbar)$ | The translation identity of the operator setting |
| $\sigma_{\mathrm{gco}}=\hbar\omega\,e_t-\tilde H^{\mathrm{gco}}_\Psi$ | The constant setting's element symbol |
| $\tilde H^{\mathrm{gco}}_\Psi=(h_t-ϙ\varphi)e_t+i(\vec h_\Psi+ϙ\vec A)$ | The shifted Hamiltonian |
| $\partial^{2}\sigma/\partial k_\eta^{2}=-\hbar^{2}/m=-0.588235$ | The curvature; the effective mass; invariant |
| $2\lvert\vec h_\Psi+ϙ\vec A\rvert$ | The gap; $1.232882$ free, $1.503329$ with the quoted $\vec A$ |
| $h_t-ϙ\varphi\pm\lvert\vec h_\Psi+ϙ\vec A\rvert$ | The pole pair; translated, with spacing that is gauge invariant |

## Further Reading

- *The Coupled Schrödinger Equation in Biquaternionic Form*, for the equation, its two signs, its gauge covariance and the two-number shift this article reads in frequency space.
- *The Fourier Transform and the Schrödinger Equation in Biquaternionic Form*, for the free symbol whose shifted arguments appear here.
- *The Fourier Transform and the Coupled Schrödinger Equation in Biquaternionic Polar Variables*, for the same symbol read in the chart.
- *The Fourier Transform and the Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Form*, for the coupled action's quadratic form at fixed frequency.
- *The Coupled Schrödinger Equation in Biquaternionic Polar Variables*, for the two invariants $\vec\pi$ and $\mathcal E$ and the gauge direction.
- *Maxwell's Equations in the Biquaternionic Formulation*, for the connection's temporal coefficient and the sign of $ϙ$.
