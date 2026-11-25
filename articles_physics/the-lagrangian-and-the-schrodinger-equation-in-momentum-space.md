# __The Lagrangian and the Schrödinger Equation in Momentum Space__

## Introduction

The action is a functional of the field, and the transform turns it into a quadratic form. *The Lagrangian and the Schrödinger Equation* writes one real functional whose Euler–Lagrange equation is the parent's equation. Take a field of one frequency, $\tilde\Xi=e^{-i\omega t'}\tilde X$, and the functional becomes a quadratic form in $\tilde X$ whose kernel is the symbol of *The Fourier Transform and the Schrödinger Equation in Biquaternionic Form*. The symbol is not a second object beside the action; it is the action's density at fixed frequency, and that identity is the first thing below.

The second finding is that the reality of the action is a weaker requirement than the reality of the spectrum. The parent requires the flow to be unitary, which forces the unit to commute with every Hermitian Hamiltonian, and that forces $\pm i$. The action needs less: it stays real for every anti-Hermitian root, because the kinetic coefficient's type is what makes its scalar part real. A real action therefore certifies the equation and does not certify the frequencies, and the two counts differ by a wide margin.

The numbers are the measure of the gap. All four roots give a real action, verified on a grid of sixty-four points to $8.7\times10^{-16}$ on the imaginary part. The spectrum is real in one hundred draws out of one hundred for $i$, and in $32$, $30$ and $37$ out of one hundred for $\vec e_z$, $\vec e_x$ and $(\vec e_x+\vec e_z)/\sqrt2$. The first number is a theorem and the others are cones.

The third finding is that Parseval is the Noether charge's transform. The parent's charge is the spatial integral of $n=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$. In frequency space it is the sum of the moduli squared of the coefficients, and the energy is the same sum weighted by the frequencies. Both are one normalisation of one identity.

The fourth finding is that the Legendre structure is trivial and non-degenerate. The symbol is affine in $\omega$ with slope $\frac{h}{2\pi}$, for every Hamiltonian. So the frequency is conjugate to time and the map is invertible; a first-order equation has no constraint to impose, and the variational principle has no multiplier to introduce.

The companion articles. *The Fourier Transform and the Schrödinger Equation in Biquaternionic Form* gives the symbol; its polar companion gives the same object in the word. The coupled version of this article adds a connection and keeps the structure; §*The Limits and the Truncation’s Error* states what the connection does not change.

## Conventions

The action, its variation and its two currents are those of *The Lagrangian and the Schrödinger Equation*, and the article does not re-derive them. The symbol, its trace and its determinant are those of *The Fourier Transform and the Schrödinger Equation in Biquaternionic Form*.

The action. With $\partial=\partial_{t'}$ and the Hermitian pairing $\langle X,Y\rangle=\mathrm{Sc}(X^{*}Y)$,

$$
S[\tilde\Xi,\tilde\Xi^{*}]=\int\mathrm{d}t'\;\mathrm{Sc}\!\left[\frac{i h}{4\pi}\big(\tilde\Xi^{*}\partial\tilde\Xi-(\partial\tilde\Xi^{*})\tilde\Xi\big)-\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi\right].
$$

The parent writes it in $r'_t$ with a factor $c$; the substitution $i \frac{h}{2\pi}\,c\,\partial_{r'_t}=i \frac{h}{2\pi}\,\partial_{t'}$ is exact and is used here once.

The two kinds of coefficient. A *Hermitian coefficient* is $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ with real numbers. A *root* is $\tilde Z$ with $\tilde Z^{2}=-e_t$; the four used below are $i$, $\vec e_z$, $\vec e_x$ and $(\vec e_x+\vec e_z)/\sqrt2$. Every root is anti-Hermitian, because $\vec e_{\imath}^{*}=-\vec e_{\imath}$ and $i^{*}=-i$.

### The Constant-Coefficient Licence

Constant coefficients. Every statement about the symbol needs a constant Hamiltonian, and the operator setting replaces the symbol by a convolution. The action remains real there, term by term, for the same reason; what fails is the fixed-frequency reduction, not the reality.

Hermitian coefficients. The counts are counts over Hermitian Hamiltonians. A non-Hermitian coefficient makes the action non-real at the potential term and the argument in the reality part of §*The Action* does not apply to the potential.

One-time functionals. The action here is an integral over $t'$ and not over space, so the transform is in one variable. A four-dimensional action would need the transform in four, and the symbol would be a function of the four-wavevector; the structure of the argument would be unchanged.

## The Action in Momentum Space: The Quadratic Form at Fixed Frequency

One substitution. Put $\tilde\Xi=e^{-i\omega t'}\tilde X$ with $\tilde X$ constant. Then $\partial\tilde\Xi=-i\omega\tilde\Xi$, the antisymmetrised kinetic density is $hf_{\mathrm{frq}}\,\mathrm{Sc}(\tilde X^{*}\tilde X)$, and the action becomes

$$
S_\omega[\tilde X]=\int\mathrm{d}t'\;\mathrm{Sc}\Big[\tilde X^{*}\big(hf_{\mathrm{frq}}\,e_t-\tilde H_\Psi\big)\tilde X\Big]
=\int\mathrm{d}t'\;\big\langle\tilde X,\sigma(\omega)\tilde X\big\rangle .
$$

The kernel is the symbol. The quadratic form's kernel is the symbol of the companion, element for element. Verified over one hundred draws of $(\tilde X,h_t,\vec h_\Psi,\omega)$: the difference between the two sides is zero to machine precision, because the two expressions are the same expression.

The form is the action's density, not its value. The action of a one-frequency field is the density times the interval, so the form's coefficient is what remains after the interval is divided out. The frequency is a parameter of the functional and not a variable of it, which is why the form is a form on $\tilde X$ alone.

Stationarity returns the equation. Varying $\tilde X^{*}$ in $S_\omega$ gives $\sigma(\omega)\tilde X=0$, which is the companion's frequency-space equation. So the two articles' objects are related by variation: the symbol is the Euler–Lagrange operator of the fixed-frequency action.

On shell the form vanishes. A solution has $\sigma(\omega)\tilde X=0$, so $S_\omega[\tilde X]=0$. That is the standard statement that an action evaluated on a solution is stationary and, for a homogeneous quadratic form, zero; it is not a statement about the energy, which is a different functional.

What the substitution does not do. It does not discretise, and it does not assume a single frequency for a general field. A general field is a sum of such terms, and the action is the sum of the forms plus the cross terms that the transform's orthogonality removes. The cross terms are the interference, and they are what makes a superposition's density not the sum of densities.

The pairing. Settled once and inherited. The pairing is $\mathrm{Sc}(\cdot^{*}\cdot)$, the Hermitian form, and the quaternionic alternative was rejected in the reality part of §*The Action* of *The Lagrangian and the Schrödinger Equation*. The coefficient examined below is what replaces the $i$ there, and the pairing is not.

The type of the coefficient. The equation with a root. Write $\frac{h}{2\pi}\,c\,\tilde Z\,\partial_{r'_t}\tilde\Xi=\tilde H_\Psi\tilde\Xi$ with $\tilde Z^{2}=-e_t$, in the parent's own form. The action that produces it has the kinetic coefficient $\frac{h}{2\pi} c\,\tilde Z$ in place of $i \frac{h}{2\pi} c$, because the variation must return the equation's own operator.

The reality condition. With $K=\frac{h c}{4\pi}\big(\tilde\Xi^{*}\tilde Z\partial\tilde\Xi-(\partial\tilde\Xi^{*})\tilde Z\tilde\Xi\big)$,

$$
K^{*}=\frac{h c}{4\pi}\Big((\partial\tilde\Xi^{*})\tilde Z^{*}\tilde\Xi-\tilde\Xi^{*}\tilde Z^{*}\partial\tilde\Xi\Big),
$$

so $K^{*}=K$ exactly when $\tilde Z^{*}=-\tilde Z$. **The action is real exactly when the root is anti-Hermitian**, and every root of $-e_t$ is.

The equivalent statement in one line. $\tilde Z$ anti-Hermitian is the same as $i\tilde Z$ Hermitian, and the quadratic form $\mathrm{Sc}(\tilde X^{*}(i\tilde Z)\tilde X)$ is real for every $\tilde X$. Verified over one hundred draws for each of the four roots: the largest imaginary part was $7.5\times10^{-16}$ for $(\vec e_x+\vec e_z)/\sqrt2$, $6.9\times10^{-16}$ for $\vec e_x$, $5.2\times10^{-16}$ for $\vec e_z$ and $2.2\times10^{-16}$ for $i$.

The functional itself, not only its density. The density's reality at one time is weaker than the functional's reality, because the kinetic term is antisymmetrised and integrated. On a grid of sixty-four points with a four-component field of three frequencies, the imaginary part of the whole action was at most $8.7\times10^{-16}$ for each of the four roots, against real values of order ten. The action is real, and it is real for all four roots.

What the reality does not use. It does not use the centrality of the root, and it does not use any commutation with the Hamiltonian. It uses one thing: the root's type. That is the whole content of this section, and it is why the next section can report a gap.

The selection rule. Not examined here. The Hamiltonian is Hermitian by the article's licence, so no sector is excluded; the anti-Hermitian potential and its complex frequency are the scalar family's, where the potential is a free element.

What reality does not buy. The stronger requirement. The parent requires the generator $-\frac{2\pi \tilde Z\tilde H_\Psi}{h\,c}$ to be anti-Hermitian for every Hermitian $\tilde H_\Psi$, so that the flow preserves the norm. In $t'$ the generator is $\frac{2\pi}{h}\tilde Z^{-1}\tilde H_\Psi$, and its anti-Hermiticity is

$$
\big(\tilde Z^{-1}\tilde H_\Psi\big)^{*}=-\tilde Z^{-1}\tilde H_\Psi
\qquad\Longleftrightarrow\qquad
\tilde H_\Psi\,\tilde Z^{-1}=\tilde Z^{-1}\tilde H_\Psi,
$$

which is commutativity of the Hamiltonian with the root. The parent's uniformity requirement is a commutant condition, and only the central root satisfies it for every Hamiltonian.

The spectrum's condition is the same condition. The frequencies are the zeros of $\det\big(hf_{\mathrm{frq}}(-i\tilde Z)-\tilde H_\Psi\big)$, and for $\tilde Z=\vec e_z$ the determinant is

$$
\Big(h_t^{2}-\big(hf_{\mathrm{frq}}+h_z\big)^{2}-h_\perp^{2}\Big)^{2},
$$

with $h_\perp^{2}=h_x^{2}+h_y^{2}$, verified to $1.4\times10^{-14}$. The zeros are $hf_{\mathrm{frq}}=-h_z\pm\sqrt{h_t^{2}-h_\perp^{2}}$, real exactly on the cone $h_t^{2}\ge h_x^{2}+h_y^{2}$.

The counts. One hundred draws of a Hermitian Hamiltonian with coefficients uniform in $[-1,1]$: all roots real in $100$ draws for $i$, $32$ for $\vec e_z$, $30$ for $\vec e_x$ and $37$ for $(\vec e_x+\vec e_z)/\sqrt2$. For $\vec e_z$ the cone held in exactly the same $32$ draws, and on the cone the closed form matched to $2.0\times10^{-15}$.

So the two requirements are different requirements. The action is real in $100$ draws out of $100$ for each root. The spectrum is real in $100$, $32$, $30$ and $37$. A variational principle that produces the equation therefore says nothing about whether the frequencies are real, and the gap between the two counts is the measure of how much it says nothing.

Why the two differ. The action's reality is a statement about the kinetic coefficient's type: one of four types, decided by the root's Hermiticity. The spectrum's reality is a statement about the pencil $hf_{\mathrm{frq}}(-i\tilde Z)-\tilde H_\Psi$: two self-adjoint arrays, one of them indefinite, and an indefinite pencil has complex zeros. Type is weaker than definiteness, and the article's finding is that sentence.

What the parent's argument really establishes. The parent's uniqueness theorem is about the *flow*, and its conclusion is about the norm. Read here, it says that only the central root keeps the pencil positive for every Hamiltonian. The variational companion of this article does not contradict it and does not repeat it; it separates the two requirements that the parent's single argument carries.

A caveat in the other direction. Reality of the spectrum does not imply that the action with that root is real for a non-Hermitian Hamiltonian, and the article makes no such claim. Both statements are about Hermitian coefficients, and both are about different objects: one about a functional, one about a pencil.

## The Variation: The Boundary Term

The boundary term. Varying $\tilde\Xi^{*}$ and integrating the kinetic term by parts gives

$$
\delta S=\int\mathrm{d}t'\;\mathrm{Sc}\Big[\delta\tilde\Xi^{*}\big(\frac{h}{2\pi} c\,\tilde Z\,\partial\tilde\Xi-\tilde H_\Psi\tilde\Xi\big)\Big]
-\frac{h c}{4\pi}\Big[\mathrm{Sc}\big(\delta\tilde\Xi^{*}\tilde Z\tilde\Xi\big)\Big]_{\mathrm{bdy}},
$$

and the boundary term vanishes when $\delta\tilde\Xi^{*}$ vanishes at both ends. **The boundary condition is a condition on the field's variation and not on its value**, and it is the same condition for every root.

Reality is what makes the second variation redundant. Because the action is real, the variation with respect to $\tilde\Xi$ is the conjugate of the variation with respect to $\tilde\Xi^{*}$, and one of them carries the content. The parent's identity for a real variation is

$$
\delta S=2\,\mathrm{Re}\int\mathrm{d}t'\;\mathrm{Sc}\big[\delta\tilde\Xi^{*}E\big],
\qquad
E=\frac{h}{2\pi} c\,\tilde Z\,\partial\tilde\Xi-\tilde H_\Psi\tilde\Xi,
$$

and it holds for every anti-Hermitian root, for the same reason the action is real. Two variations for the price of one is the payoff of the reality established above.

What the identity is not. It is not a proof that the equation is variational for a complex root. For a root that is neither Hermitian nor anti-Hermitian the kinetic term's scalar part has an imaginary piece, the boundary term does not vanish with a real variation, and the argument fails at the first line.

The vanishing of the bracket is the equation. Since the pairing $\mathrm{Sc}(XY)$ is non-degenerate on $\mathbb{B}$, the bracket vanishes as an element. The non-degeneracy is the parent's, and it is not the same as the definiteness of the Hermitian form: it is a Hermitian pairing, and it needs no positivity.

Why the Hermitian pairing is enough. For $X=E^{*}$ the pairing gives $\mathrm{Sc}(E^{*}E)=\sum_{\imath}\lvert E_{\imath}\rvert^{2}$, a sum of moduli, so it vanishes only for $E=0$. The argument is the parent's and it is quoted once here.

### Zero, Pole and the On-Shell Action

The kernel of the fixed-frequency form. The action at frequency $\omega$ is $S_\omega[\tilde X]=\int\mathrm{d}t'\,\langle\tilde X,\sigma(\omega)\tilde X\rangle$, so the form's kernel is the symbol and the symbol's zero is the condition that a non-zero amplitude costs nothing. That condition is the dispersion relation, and in this reading it is not an assumption: it is the vanishing of the form's kernel.

Zero and pole. The resolvent at the frequency is the form's inverse, and it fails exactly at the zero. The pole of the resolvent and the zero of the form are one locus read from two sides, and the article uses whichever side the sentence needs.

Why the pole is simple here. The Schrödinger symbol is first order in the frequency, so its zero is one linear condition and the pole is simple. A simple pole has a residue, and the residue is the density per mode: $\frac{h}{2\pi}$ times the norm, which is the article's statement that the Legendre slope is $\frac{h}{2\pi}$ and the mixed derivative vanishes. A quadratic symbol would give two branches and a residue that is a difference; this one gives one branch and a residue that is a product.

The on-shell action. On a solution the amplitude is a kernel vector, so $\langle\tilde X,\sigma\tilde X\rangle=0$ and the mode action vanishes. The action is zero on shell because the action is the form, and this is the one place where the reading's identification is tested: a reader who thought the action was an energy would find the answer zero and ask why.

The free case's degeneracy. The free symbol's zero is not degenerate, but the free *spectrum* is: every root of $-e_t$ gives the same symbol because the symbol depends on the Hamiltonian and not on the root. That is the one degeneracy this reading has, and it is why the article separates the reality of the form from the reality of the whole action: the form is real for every amplitude, and the action is real because the root is anti-Hermitian.

What the section does not claim. It does not claim that the zero is a bound state. A zero of the form is a propagation condition, and whether the propagating mode is normalisable is a question about the boundary conditions that this reading does not supply.

### The Legendre Transform

The slope. $\partial\sigma/\partial\omega=\frac{h}{2\pi}$ for every $\tilde H_\Psi$, because the Hamiltonian does not depend on the frequency. A central difference on the scalar part at $\omega=0.7$ returned $1.000000000000$ at a step of $10^{-2}$ and $10^{-4}$, and $1.000000000029$ at $10^{-6}$, which is the roundoff of the step and not a deviation of the slope. The frequency is conjugate to time with slope $\frac{h}{2\pi}$, and the slope is the same for every Hamiltonian.

Non-degeneracy. $\frac{h}{2\pi}\neq0$, so the Legendre map from the frequency to the time derivative is invertible everywhere. There is no constraint surface and no multiplier: the variational principle for a first-order equation is unconstrained, which is what the polar variational companion means when it says no multiplier is needed for the unit conditions.

The symbol is affine, so the transform is trivial. A function affine in $\omega$ is its own Legendre transform up to a total derivative. So the frequency-space action and the time-domain action are related by the elementary transform and not by a nontrivial dualisation. The nontrivial dualisations in this corpus are in the second-order articles, where the symbol is quadratic and the derivative of the symbol is the velocity.

The velocity and the momentum. For a first-order equation the velocity is the field's time derivative and the momentum is the field's conjugate, and the two are not related by the symbol's derivative. The symbol's derivative is $\frac{h}{2\pi}$ times the identity, so the "velocity" the transform returns is the same for every mode: that is the statement that a first-order equation has no dispersion to invert.

What the slope fixes. The slope fixes the normalisation of the transform and therefore the normalisation of $Q_N$ and $E$. One choice of $\frac{h}{2\pi}$ fixes both, and no second convention enters.

## The Constraints the Action Imposes: The Constraint Is the Frequency

At fixed frequency the variation is algebraic. The substitution $\tilde\Xi=e^{-i\omega t'}\tilde X$ has removed the derivative, so the action $S_\omega$ is a quadratic form in the constant amplitude. Stationarity forces its bracket to vanish, and where the bracket is invertible the only stationary amplitude is zero.

The condition is the eigenvalue problem the action section states. The bracket is $hf_{\mathrm{frq}}\,\mathrm{Sc}(\tilde X^{*}\tilde X)-\mathrm{Sc}\bigl[\tilde X^{*}\tilde H_\Psi\tilde X\bigr]$, so its singularity is exactly the statement that $\omega$ is an eigenvalue of $\frac{2\pi \tilde H_\Psi}{h}$. **The constraint is a condition on the frequency and on nothing else**; the amplitude is left free up to normalisation, which is not a restriction the action imposes.

The set is the spectrum's zero set. At $\nu_m=0$ it is the paraboloid; a constant potential translates it, and the connection's temporal slot translates it again by its own amount. The shape is fixed by the kinetic term alone, which is why the constraint of this chart can be read off the first line of the action.

What is absent. No Gauss law, because the connection is fixed at a mode; no boundary condition, because a variation at one frequency cannot see one; no constraint on the amplitude at a root. The constraint is purely kinematic, and the structural consequence's claim is exactly that nothing further is imposed.

## The Structural Consequence: The Symbol Is the Quadratic Form

Two readings of one identity. Read as an operator, $\sigma(\omega)$ is an array; read as a quadratic form, it is $\tilde X\mapsto\langle\tilde X,\sigma(\omega)\tilde X\rangle$. The two agree on the diagonal and differ off it; the form determines the self-adjoint part of the array, and that is all the action can see.

Reality of the form is self-adjointness. $S_\omega[\tilde X]$ is real for every $\tilde X$ exactly when $\sigma(\omega)$ is self-adjoint for the pairing, which is exactly when $hf_{\mathrm{frq}}\,e_t-\tilde H_\Psi$ is Hermitian, which is exactly when $\tilde H_\Psi$ is. **So the reality of the fixed-frequency action at every frequency is the Hermiticity of the Hamiltonian**, verified over one hundred draws on random $\tilde X$.

What the form cannot see. An anti-Hermitian part of the array contributes a purely imaginary value to the form and cancels in the sum with its conjugate. So the action is blind to the anti-Hermitian part, and its blindness is the reason the next section's statement is possible.

The trace is the form on a basis. Summing the form over an orthonormal basis of the coefficient space gives $\operatorname{tr}\sigma(\omega)=4(hf_{\mathrm{frq}}-h_t)$. The action's trace is four times the mean frequency, and the determinant, which the form cannot see, is the square of the gap.

## The Noether Currents: The Charge Per Mode

The charge at a mode. The Noether charge is the spatial integral of the temporal component of the current, and by Parseval it becomes a sum over modes. At one mode the summand is the bilinear of the amplitude,

$$
\mathcal{Q}(\vec\nu_{\Phi})=\frac{h}{2\pi}\,\mathrm{Sc}\bigl[X^{*}(\vec\nu_{\Phi})X(\vec\nu_{\Phi})\bigr],
$$

up to the normalisation the element article fixes, so that the total charge is the integral of this density over the wave numbers. The step from the position-space charge to this display is Parseval's identity and nothing else; the companion article *The Lagrangian and the Schrödinger Equation in Momentum Space* proves it in that case and the proof transfers, because it uses only the transform and the Hermitian pairing.

The energy. The energy is the symbol evaluated at zero frequency, $E=\mathcal{S}(0,2\pi\vec\nu_{\Phi})$, which is the statement that the Hamiltonian is the generator of the frequency. On the shell the two agree with the dispersion relation, and off the shell the symbol is the energy the mode would have if it were on it.

What the mass term does to the two. The mass term shifts neither the charge nor the reality of the bilinear: it enters the symbol and leaves the pairing alone. What it does is remove the zero-frequency mode from the spectrum, and that removal is the count of degrees of freedom the article's structural section states.

## The Noether Currents: Parseval Is the Charge's Transform

The charge. The parent's phase symmetry gives the current whose temporal component is $n=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$, and the conserved charge is $Q_N=\int\mathrm{d}t'\,n$. The factor of two against $\rho=2\,\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ is the $2\,\mathrm{Sc}(\tilde Q)=2Q_t$ convention and is not a normalisation.

Its transform. Write the field as a sum of modes, $\tilde\Xi=\sum_jc_j e^{-i\omega_jt'}\tilde X_j$ with orthonormal $\tilde X_j$ of unit Hermitian norm. Then the charge is

$$
Q_N=\sum_j\lvert c_j\rvert^{2},
$$

which is Parseval's identity read as a charge. On a grid of $4096$ points a superposition of three integer modes gave $\sum_j\lvert c_j\rvert^{2}=1.562500000000$ and a grid norm equal to that number to the last printed digit. The norm is the charge, and the transform diagonalises it.

The energy. The parent's constant-setting energy is $E=\mathrm{Sc}(\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi)$, which on a mode is $hf_{\mathrm{frq},j}$ times the mode's norm. So

$$
E=\sum_j hf_{\mathrm{frq},j}\lvert c_j\rvert^{2},
$$

and the same grid gave $4.867427$ against $4.867500$ from the coefficients, the difference $7.3\times10^{-5}$ being the finite-difference gradient's error and not a structural one. Two functionals, one normalisation, and both diagonal in the transform.

The weights are the spectrum. The energy's weights are the eigenvalues of the symbol, so the energy's transform is the symbol's value weighted by the charge. That is the sense in which the symbol is the action's Legendre transform, and the next section makes the statement exact.

A first-order reading of the two. $Q_N$ counts and $E$ weighs. A first-order equation conserves both because the flow is unitary, and neither is the temporal slot of a current in the second-order sense. The pair $(Q_N,E)$ is the whole of the Noether content of the phase symmetry and time translation.

What Parseval does not say. It does not say that the coefficients are probabilities, and it does not normalise them. **The charge is a real number and the algebra supplies no probability rule**; the corpus's measurement articles are where that reading is made, and this article does not make it.

## What the Principle Adds and What It Relabels: In Momentum Space

One identity and one separation. The identity is that the symbol is the fixed-frequency action's kernel, so the two companion articles describe one object. The separation is that the reality of the action and the reality of the spectrum are different requirements, with different strengths and different counts.

The count of roots. All four roots are variational, and only one of them gives a real spectrum for every Hamiltonian. That is the sharpest statement of the article, and it is a statement the element-form and polar companions cannot make, because the action is what carries the root.

The transform of the two functionals. Parseval and the energy identity are one normalisation of the charge and of the energy, and both are diagonal in the transform. **No new conservation law appears**, and none is claimed.

What it does not add. No new prediction, no new solution, no closure of the operator setting. The variational principle is the parent's and the transform is the companion's; the article joins them.

## Open Questions

Whether a weaker reality suffices for a unitary flow. The action is real for every anti-Hermitian root, and the flow is unitary for none of the non-central ones. Whether some other functional distinguishes them is not settled.

The second-order root. The Dirac and Klein–Gordon articles factor their operators and ask about a square root; the Schrödinger operator has a square root trivially, because it is first order. Whether the variational argument has a second-order analogue in which the root's type is again the deciding condition is open.

The operator setting's Legendre structure. With a position-dependent Hamiltonian the slope in $\omega$ is still $\frac{h}{2\pi}$, and the dual variable is still a time. Whether the position dependence can be absorbed into a local frequency with a Legendre structure of its own is open.

## Summary

The fixed-frequency action is a quadratic form whose kernel is the symbol: $S_\omega[\tilde X]=\int\mathrm{d}t'\,\langle\tilde X,\sigma(\omega)\tilde X\rangle$, exact by construction and verified over one hundred draws. The reality of that form for every $\tilde X$ is the Hermiticity of the Hamiltonian, and the trace of the form on a basis is four times the mean frequency.

The reality of the whole action is a weaker condition: it holds exactly when the root is anti-Hermitian, which every root of $-e_t$ is. Verified on a grid of sixty-four points, the imaginary part of the action was at most $8.7\times10^{-16}$ for all four roots. **The spectrum, by contrast, is real in $100$ draws out of $100$ for $i$ and in $32$, $30$ and $37$ for the three quaternion roots**, and for $\vec e_z$ the cone $h_t^{2}\ge h_x^{2}+h_y^{2}$ accounts for the count exactly. So the variational principle certifies the equation and not the frequencies.

Parseval is the Noether charge's transform, $Q_N=\sum_j\lvert c_j\rvert^{2}$, exact to the last digit on a grid of $4096$ points, and the energy is the same sum weighted by the eigenvalues, $4.867427$ against $4.867500$. The Legendre slope is $\partial\sigma/\partial\omega=\frac{h}{2\pi}$ for every Hamiltonian, so the transform is invertible and the variational problem is unconstrained.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $S_\omega[\tilde X]=\int\mathrm{d}t'\,\langle\tilde X,\sigma(\omega)\tilde X\rangle$ | The action at fixed frequency; the quadratic form whose kernel is the symbol |
| $\sigma(\omega)=hf_{\mathrm{frq}}\,e_t-\tilde H_\Psi$ | The symbol; the Euler–Lagrange operator of $S_\omega$ |
| $\tilde Z^{2}=-e_t$, $\tilde Z^{*}=-\tilde Z$ | A root; anti-Hermitian, hence the action is real |
| $\frac{h}{2\pi} c\,\tilde Z$ | The kinetic coefficient of the action with a root |
| $E=\frac{h}{2\pi} c\,\tilde Z\partial\tilde\Xi-\tilde H_\Psi\tilde\Xi$ | The Euler–Lagrange bracket; its vanishing is the equation |
| $100$, $32$, $30$, $37$ | Draws with a real spectrum, out of one hundred, for $i$, $\vec e_z$, $\vec e_x$, $(\vec e_x+\vec e_z)/\sqrt2$ |
| $h_t^{2}\ge h_\perp^{2}$ | The cone on which the pencil has real zeros |
| $Q_N=\sum_j\lvert c_j\rvert^{2}$ | The charge; Parseval's identity |
| $E=\sum_j hf_{\mathrm{frq},j}\lvert c_j\rvert^{2}$ | The energy; the charge weighted by the spectrum |
| $\partial\sigma/\partial\omega=\frac{h}{2\pi}$ | The Legendre slope; invertible, hence unconstrained |

## Further Reading

- *The Lagrangian and the Schrödinger Equation*, for the action, its reality, its variation and its two currents, all cited here and not repeated.
- *The Fourier Transform and the Schrödinger Equation in Biquaternionic Form*, for the symbol, its determinant and the counts of poles.
- *The Fourier Transform and the Schrödinger Equation in Biquaternionic Polar Variables*, for the same identity read in the word.
- *The Lagrangian and the Schrödinger Equation in Polar Variables*, for the unconstrained variation and the vanishing multipliers.
- *The Lagrangian and the Coupled Schrödinger Equation in Momentum Space*, for the same structure with a connection.
- *The Non-Quantum Limit of the Action Principle and the Lagrangian*, for the principle this article applies.
