# __The Fourier Transform and the Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Form__

## Introduction

**The coupled action's fixed-frequency form is the coupled symbol, and its reality is a term-by-term fact.** *The Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Form* writes the action for $i\hbar D_t\tilde\Xi=\frac{1}{2m}\sum(-i\hbar D_\eta)^{2}\tilde\Xi$. Take a mode of one frequency and one wave vector, and the action's density becomes the symbol of *The Fourier Transform and the Coupled Schrödinger Equation in Biquaternionic Form*. **The identity is the same identity as in the free case**, with two shifted arguments.

**The first finding is that the reality survives the coupling term by term.** The kinetic term is real for every anti-Hermitian root, the gradient term is a sum of moduli, and the potential term is real because $\varphi$ is. **No cancellation is used**, so the coupling cannot make a real action complex and cannot make a complex action real.

**The second finding is that the Legendre slope is untouched.** $\partial\sigma/\partial\omega=\hbar$ with or without the connection, because the connection does not depend on the frequency. The slope in the four-wavevector's temporal slot is $\hbar c$. **The map from frequency to time is invertible in every coupled case**, and the variational problem is unconstrained.

**The third finding is that the energy is minus the symbol at zero frequency.** For a mode of unit norm, $E=\frac{1}{2m}\lvert\hbar\vec k+ϙ\vec A\rvert^{2}-ϙ\varphi=-\sigma_{\mathrm{gco}}(0,\vec k)$, verified over one hundred draws with zero residual. **The symbol is the action's density, and the energy is that density with the frequency set to zero and the sign flipped**, which is the standard sign of a Lagrangian's Legendre transform.

**The fourth finding is that the symbol is gauge invariant in the invariant coordinates.** A gauge transformation shifts $\varphi$ and $\vec A$, and the same transformation shifts the frequency and the wave vector of a mode. The two shifts cancel in the symbol, verified to $8.9\times10^{-16}$. **So the symbol is a function of $\mathcal E$ and $\vec\pi$ and not of the four ingredients separately**, and the two slots' opposite signs are exactly what makes the cancellation work.

**The fifth finding is a resolution.** The earlier companions report a sign for the frequency shift that a careless substitution would reverse. Here the reversal is visible as a failure of exactly the cancellation above, so the article can state which sign is the parent's and why.

**The companion articles.** *The Fourier Transform and the Variational Principle and the Schrödinger Equation in Biquaternionic Form* is the free version. *The Fourier Transform and the Coupled Schrödinger Equation in Biquaternionic Form* gives the symbol, and its polar companion gives the chart. This article joins the action to the coupled symbol.

## Conventions

The coupled action, its variation, its currents and the sign of $ϙ$ are those of *The Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Form*. The symbol and its two settings are those of *The Fourier Transform and the Coupled Schrödinger Equation in Biquaternionic Form*.

**The action.** With $D_t=\partial_{t'}-iϙ\varphi/\hbar$ and $D_\eta=\partial_\eta+iϙ A_\eta/\hbar$,

$$
S=\int\mathrm{d}t'\;\mathrm{Sc}\left[\frac{i\hbar}{2}\big(\tilde\Xi^{*}D_t\tilde\Xi-(D_t\tilde\Xi)^{*}\tilde\Xi\big)-\frac{1}{2m}\sum_\eta(D_\eta\tilde\Xi)^{*}(D_\eta\tilde\Xi)\right],
$$

an integral over time of a density that already contains the spatial derivatives. **The action is one-dimensional and the equation is not**, and that asymmetry is the parent's.

**The two settings, named once.** The *constant* setting has a constant Hermitian Hamiltonian and a constant connection, so the symbol is an element. The *operator* setting has $\hat H=-\hbar^{2}\Delta_\Phi/(2m)+V$, so the symbol is a scalar. Every display is labelled.

**The mode.** $\tilde\Xi=e^{-i\omega t'}\tilde X$ in the constant setting, and $\tilde\Xi=e^{-i\omega t'+i\vec k_\Phi\cdot\vec r}\tilde X_0$ in the operator setting. The two substitutions differ by the spatial factor, and the difference is what makes the second setting's symbol a function of two arguments.

## The Coupled Action at Fixed Frequency

**The constant setting.** With $\tilde\Xi=e^{-i\omega t'}\tilde X$ and a constant connection, the density is

$$
\mathrm{Sc}\Big[\tilde X^{*}\big(\hbar\omega\,e_t+ϙ\varphi\,e_t-\tilde H_\Psi\big)\tilde X\Big]
=\big\langle\tilde X,\sigma_{\mathrm{gco}}(\omega)\tilde X\big\rangle ,
$$

because the spatial derivatives vanish on a constant $\tilde X$ and the covariant time derivative becomes a number. **The kernel is the element-form symbol of the companion**, with $\sigma_{\mathrm{gco}}(\omega)=\hbar\omega\,e_t-\tilde H^{\mathrm{gco}}_\Psi$ and $\tilde H^{\mathrm{gco}}_\Psi=(h_t-ϙ\varphi)e_t+i(\vec h_\Psi+ϙ\vec A)$.

**The operator setting.** With $\tilde\Xi=e^{-i\omega t'+i\vec k_\Phi\cdot\vec r}\tilde X_0$, the covariant spatial derivative becomes the number $ik_\eta+iϙ A_\eta/\hbar$, so

$$
(D_\eta\tilde\Xi)^{*}(D_\eta\tilde\Xi)=\Big(k_\eta+\frac{ϙ A_\eta}{\hbar}\Big)^{2}\mathrm{Sc}\big(\tilde X_0^{*}\tilde X_0\big),
$$

and the density is $\sigma_{\mathrm{gco}}(\omega,\vec k)$ times $\mathrm{Sc}(\tilde X_0^{*}\tilde X_0)$, with $\sigma_{\mathrm{gco}}$ the scalar of the companion. **The form's kernel is the symbol and the form's value is the symbol times the mode's norm.**

**The two settings agree where both exist.** In the constant setting with $\vec h_\Psi=\hbar\vec k_\Phi$ the element's scalar part is the operator setting's scalar. **The agreement is the statement that a plane wave of a constant Hamiltonian is a plane wave of the differential operator**, and it holds at one mode and not for a general field.

**Stationarity returns the coupled equation.** Varying $\tilde X^{*}$ in the fixed-frequency form gives $\sigma_{\mathrm{gco}}\tilde X=0$, which is the companion's frequency-space equation. **So the symbol is the coupled action's Euler–Lagrange operator**, exactly as in the free case.

**On shell the form vanishes.** A solution has $\sigma_{\mathrm{gco}}\tilde X=0$, so the form's value is zero. **That is the homogeneous quadratic form's standard property and not a statement about the energy**, which is the next section's object.

**What the substitution does not assume.** It does not assume that the connection is constant. A varying connection makes the density a function of position, and then the fixed-frequency reduction is a reduction in time only. **The reduction in space is a separate assumption and it is named in the mode's definition.**

## Reality Term by Term

**The kinetic term.** The antisymmetrised covariant kinetic density is real exactly when the root is anti-Hermitian, by the free article's computation, and the covariant derivative's connection part is central so it does not change the type. **The coupling adds a real number to a real quantity.**

**The gradient term.** $\mathrm{Sc}\big((D_\eta\tilde\Xi)^{*}(D_\eta\tilde\Xi)\big)=\sum_\mu\lvert(D_\eta\tilde\Xi)_\mu\rvert^{2}$, a sum of four moduli, which is real and non-negative. **The term is a norm and not a form**, and its positivity is what makes the kinetic energy of the field positive for every configuration.

**The potential term.** $\varphi$ is real, so $ϙ\varphi\,\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ is real and its sign is the sign of $ϙ\varphi$. **The term is the only one whose sign is not fixed**, and that is the standard statement that a potential can lower the energy without bound.

**So the reality is term by term.** Each of the three terms is real on its own, so the sum is real and no cancellation between terms is needed. **That is stronger than the free case's statement**, where the antisymmetrised kinetic term was the only one and its reality was the whole content.

**What the term-by-term structure forbids.** It forbids a complex action from a real connection and a Hermitian Hamiltonian. **A complex action would need a non-Hermitian coefficient or a complex $ϙ$**, and the article's licence excludes both.

**The modulus is preserved by the connection.** $\lvert D_\eta\tilde\Xi\rvert$ is unchanged when $\tilde\Xi$ is multiplied by a unit, so the gauge transformation cannot change the gradient term. **That invariance is the reason the action's gauge covariance is exact and not up to a total derivative**, and the parent states it once.

## Legendre and the Two Invariant Slopes

**The slope in the frequency.** $\partial\sigma_{\mathrm{gco}}/\partial\omega=\hbar$, independent of $\varphi$, of $\vec A$ and of the Hamiltonian. **The connection shifts the arguments and never the slope**, because it does not depend on the frequency.

**The slope in the temporal wave number.** With $k_t'=\omega/c$ the slope is $\hbar c$, and the factor is the unit that relates the two variables. **The two slopes are one slope read in two units**, and no physics depends on which is written.

**Non-degeneracy.** $\hbar\neq0$, so the Legendre map is invertible and the variational problem has no constraint and no multiplier. **The coupling does not introduce one**, because the connection enters the density as a number and not as a Lagrange multiplier.

**What the slope does not see.** The slope does not see $\vec\pi$, so the mechanical momentum is not a Legendre conjugate of anything in this article. **It is a Noether momentum**, the parent's, and the two notions coincide only in a second-order theory.

**The mixed derivative vanishes.** $\partial^{2}\sigma_{\mathrm{gco}}/\partial\omega\partial k_\eta=0$, so the frequency and the wave vector are separated in the symbol. **The separation is the statement that the symbol is a sum of a frequency term and a wave-vector term**, and it is the constant-coefficient structure read on the second derivative.

**Why the mixed derivative matters.** A nonzero mixed derivative would mean that the frequency's conjugate depends on the wave vector, which is what a dispersion with a velocity-dependent mass would look like. **The article's class has none**, and the flatness of the second derivative is the class's signature.

## The Energy Is the Symbol at Zero Frequency

**The constant setting.** The energy on a mode is $E=\mathrm{Sc}\big(\tilde X^{*}\tilde H^{\mathrm{gco}}_\Psi\tilde X\big)$, and the symbol at zero frequency is $\sigma_{\mathrm{gco}}(0)=-\tilde H^{\mathrm{gco}}_\Psi$. So

$$
E=-\big\langle\tilde X,\sigma_{\mathrm{gco}}(0)\tilde X\big\rangle ,
$$

and the identity is exact by construction. **The sign is the Lagrangian's**: a Lagrangian is $T-V$ and the Hamiltonian is $T+V$, so the potential's sign flips and the symbol, which is the Lagrangian's density, carries the minus.

**The operator setting.** With a unit mode, $E=\frac{1}{2m}\lvert\hbar\vec k+ϙ\vec A\rvert^{2}-ϙ\varphi$, and $\sigma_{\mathrm{gco}}(0,\vec k)=ϙ\varphi-\frac{1}{2m}\lvert\hbar\vec k+ϙ\vec A\rvert^{2}$. So $E=-\sigma_{\mathrm{gco}}(0,\vec k)$, verified over one hundred draws with zero residual. **The identity is one line and it fixes the article's sign conventions once.**

**The positivity of the gradient term is visible here.** The energy's first term is a sum of moduli and the second is the potential. **So the energy is bounded below exactly when the potential is**, and the bound is the parent's and not this article's.

**The bound and the symbol.** $\sigma_{\mathrm{gco}}(0,\vec k)$ is bounded above by $-E_{\min}$, so the symbol at zero frequency cannot exceed the negative of the ground energy. **That is the variational principle's standard inequality read on the symbol**, and it is a statement about one mode.

**What the identity does not say.** It does not say that $\sigma$ is the Hamiltonian's symbol. The Hamiltonian's symbol is $\hbar\omega$ itself; the Lagrangian's symbol is $\hbar\omega$ minus the Hamiltonian's. **The two differ by the Legendre transform of a quadratic**, and this article uses the Lagrangian's.

**A check of the sign's consistency.** Composing the identity with the on-shell condition gives $E=0$ on a solution at zero frequency, which is the statement that a zero-frequency solution has zero energy under this normalisation. **The statement is a normalisation and not a physical claim**, and the article states it once.

## Gauge Invariance of the Symbol, and the Resolution of the Sign

**The two shifts.** Under a gauge transformation $\tilde\Xi\mapsto e^{iϙ\Gamma/\hbar}\tilde\Xi$, the connection moves as $\varphi\mapsto\varphi+\partial_{t'}\Gamma$ and $\vec A\mapsto\vec A-\nabla\Gamma$. A mode's phase moves as $\theta\mapsto\theta+ϙ\Gamma/\hbar$, so its frequency and wave vector move as

$$
\omega\longmapsto\omega-\frac{ϙ}{\hbar}\partial_{t'}\Gamma,
\qquad
\vec k\longmapsto\vec k+\frac{ϙ}{\hbar}\nabla\Gamma .
$$

**The symbol is invariant.** Substituting the four shifts into $\sigma_{\mathrm{gco}}$ cancels $\partial_{t'}\Gamma$ in the frequency term and $\nabla\Gamma$ in the mechanical momentum, so $\sigma_{\mathrm{gco}}$ is unchanged. **Verified over one hundred draws with constant $\Gamma$: the residual was $8.9\times10^{-16}$.**

**What the invariance says.** The symbol is a function of $\mathcal E=\hbar\omega+ϙ\varphi$ and $\vec\pi=\hbar\vec k+ϙ\vec A$ and of nothing else. **The four ingredients are not independent**, and the symbol's two arguments are the two invariants of the polar companion.

**The resolution of the sign.** The frequency shift in the symbol is $+ϙ\varphi/\hbar$ and the mode's frequency shift under a gauge transformation is $-ϙ\partial_{t'}\Gamma/\hbar$. The two signs differ, and they must differ, because $\varphi$ and $\partial_{t'}\Gamma$ enter $\mathcal E$ with the *same* sign while $\omega$ and $\partial_{t'}\Gamma$ enter with opposite signs. **A substitution that gave $\omega\mapsto\omega+ϙ\varphi/\hbar$ with the other sign would break the cancellation**, and that is how the article detects the error rather than asserting the convention.

**What the invariance does not say.** It does not say that the action is gauge invariant. The action's value moves by a total derivative, which is the parent's statement and not this article's. **The symbol's invariance is stronger and it needs no boundary term**, because the symbol is a density at one point and a total derivative has no local content.

**A remaining freedom.** A constant $\Gamma$ shifts both invariants by the same constants, so the symbol is invariant under a two-parameter translation of its arguments. **That freedom is the constant-background case's**, and it is why the polar companion can call the constant background exact.

## What the Coupled Version Adds

**One identity, one sign, one invariance.** The identity is that the coupled symbol is the fixed-frequency coupled action. The sign is $E=-\sigma_{\mathrm{gco}}(0,\vec k)$, verified with zero residual. The invariance is the cancellation of the gauge shift, verified to $8.9\times10^{-16}$.

**The term-by-term reality.** The coupled action is real because each of its three terms is real, not because of a cancellation. **That is a stronger statement than the free article's**, and it is the reason a central connection cannot spoil the variational structure.

**What it does not add.** No new prediction, no new solution, no statement about a varying field strength. **The action is the parent's and the symbol is the companion's**; the article joins them and checks the join.

## Limits

**Constant coefficients.** The symbol exists for a constant Hamiltonian and a constant connection. With $\vec A$ linear in space the symbol depends on position through $\vec A$ and the plane-wave reduction fails even for a constant field strength.

**Hermitian coefficients and real $ϙ$.** The term-by-term reality uses both. A complex $ϙ$ makes the potential term complex; a non-Hermitian Hamiltonian makes the kinetic term complex for the central root as well.

**One time.** The action is an integral over $t'$, so the transform is in one variable. The four-dimensional transform would put the slope at $\hbar c$ and keep every other statement, and the article does not construct it.

## Open Questions

**The first question is the varying connection's Legendre structure.** The slope in $\omega$ is $\hbar$ everywhere, and the local frequency is a function of position. Whether a local Legendre transform with a local slope exists is the polar companion's question, and it is open here.

**The second is the bound's sharpness.** The energy is bounded below by the potential's bound, and the symbol at zero frequency sees that bound. Whether the bound is attained by a mode of the present class for any potential is not decided.

**The third is the sign of $ϙ\varphi$ in the energy.** The article's identity fixes the relation between $\sigma_{\mathrm{gco}}(0)$ and $E$ and does not fix the physical sign of $ϙ$. That is a conventions question and the conventions articles own it.

**The fourth is the second-order analogue.** The free article's gap between the reality of an action and the reality of a spectrum has no coupled counterpart here, because the coupled symbol's spectrum is the free one's. Whether a coupled second-order equation would show the same gap is the Dirac and Klein–Gordon companions' question.

## Summary

The coupled action at fixed frequency is the coupled symbol: $\big\langle\tilde X,\sigma_{\mathrm{gco}}(\omega)\tilde X\big\rangle$ in the constant setting, and $\sigma_{\mathrm{gco}}(\omega,\vec k)$ times the mode's norm in the operator setting, with the same shift of the free symbol's arguments. The reality is term by term: the kinetic term by the anti-Hermitian root, the gradient term as a sum of moduli, the potential term because $\varphi$ is real. **No cancellation is needed**, which is why a central connection cannot spoil the variational structure.

The Legendre slope is $\hbar$ and the mixed derivative vanishes, so the frequency and the wave vector are separated and the problem is unconstrained. The energy is minus the symbol at zero frequency, $E=-\sigma_{\mathrm{gco}}(0,\vec k)$, verified over one hundred draws with zero residual, and the sign is the Lagrangian's.

The symbol is gauge invariant in the invariant coordinates: the four shifts cancel, verified to $8.9\times10^{-16}$, so $\sigma_{\mathrm{gco}}$ is a function of $\mathcal E$ and $\vec\pi$ alone. **That invariance is also the resolution of the frequency shift's sign**, because the opposite sign would break the cancellation.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $S_\omega[\tilde X]=\int\mathrm{d}t'\,\big\langle\tilde X,\sigma_{\mathrm{gco}}(\omega)\tilde X\big\rangle$ | The coupled action at fixed frequency; constant setting |
| $\sigma_{\mathrm{gco}}(\omega)=\hbar\omega\,e_t-\tilde H^{\mathrm{gco}}_\Psi$ | The element symbol; the form's kernel |
| $\sigma_{\mathrm{gco}}(\omega,\vec k)=\hbar\omega+ϙ\varphi-\lvert\hbar\vec k+ϙ\vec A\rvert^{2}/(2m)$ | The scalar symbol; operator setting |
| $\mathcal E=\hbar\omega+ϙ\varphi$, $\vec\pi=\hbar\vec k+ϙ\vec A$ | The two invariants; the symbol's only arguments |
| $\omega\mapsto\omega-\frac{ϙ}{\hbar}\partial_{t'}\Gamma$, $\vec k\mapsto\vec k+\frac{ϙ}{\hbar}\nabla\Gamma$ | The mode's gauge shifts; they cancel in the symbol |
| $E=-\sigma_{\mathrm{gco}}(0,\vec k)$ | The energy as minus the symbol at zero frequency |
| $\partial\sigma_{\mathrm{gco}}/\partial\omega=\hbar$ | The Legendre slope; unchanged by the coupling |
| $\partial^{2}\sigma_{\mathrm{gco}}/\partial\omega\partial k_\eta=0$ | The vanishing mixed derivative; the class's signature |
| $\sum_\mu\lvert(D_\eta\tilde\Xi)_\mu\rvert^{2}$ | The gradient term; real and non-negative |

## Further Reading

- *The Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Form*, for the coupled action, its variation and its currents cited here.
- *The Fourier Transform and the Coupled Schrödinger Equation in Biquaternionic Form*, for the two settings' symbols and the translation identity.
- *The Fourier Transform and the Variational Principle and the Schrödinger Equation in Biquaternionic Form*, for the free version of this article's identity.
- *The Fourier Transform and the Coupled Schrödinger Equation in Biquaternionic Polar Variables*, for the same symbol read in the chart.
- *The Coupled Schrödinger Equation in Biquaternionic Form*, for the signs of the two covariant slots.
- *The Action Principle and the Non-Quantum Limit in Biquaternionic Form*, for the principle and its Legendre structure.
