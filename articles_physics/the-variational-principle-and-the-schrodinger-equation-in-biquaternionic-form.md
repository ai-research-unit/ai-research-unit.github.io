# __The Variational Principle and the Schrödinger Equation in Biquaternionic Form__

## Introduction

*The Schrödinger Equation in Biquaternionic Form* writes the equation as

$$
i\hbar\,c\,\partial/\partial r'_t\,\tilde\Xi=\tilde H_\Psi\,\tilde\Xi,
\qquad
\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi\in\mathbb{B}_{\Psi},
\qquad
\tilde\Xi\in\mathbb{B},
$$

with $h_t$ and $\vec h_\Psi$ numbers, so that the equation is an ordinary differential equation in the material time $r'_t=c\,t'$. The present article asks one question about it: which action has this equation as its Euler–Lagrange equation, and what do the symmetries of that action give?

The answer is short. One action has the equation as its Euler–Lagrange equation. Its two symmetries give two currents: the density, up to a factor of two, and the energy. Its reality and its centrality statement settle which of the parent's two writings carries the Hermitian coupling. These are the three items of the article, and each is a computation rather than an assertion.

Two boundaries are stated first, because both are ways of overclaiming.

**This is the element-form variational principle.** The field is one element $\tilde\Xi$ of $\mathbb{B}$ and the variation is over that element. The *polar* variational principle, in which the eight parameters of the word are the variables, is the companion article *The Variational Principle and the Schrödinger Equation in Biquaternionic Polar Variables*. It is genuinely different, because the word is nonlinear in the element, and the companion's action is not this action written in other letters.

**Nothing here is new in the physics.** The action is the standard first-order action of a complex field, rewritten in the algebra. It predicts nothing the parent does not predict and solves nothing the parent does not solve. What it supplies is a compact statement of the equation, one derivation of the two currents, and a variational reading of the parent's two writings. The honest ledger is the subject of the sixth section.

**The two settings are distinguished from the first line.** The parent has a constant-element setting, $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ with $h_t$ and $\vec h_\Psi$ fixed numbers, and an operator setting, $\tilde H_\Psi=\hat H\,e_t$ with $\hat H=-\hbar^{2}\Delta_\Phi/2m+V$. The action below is written in both, but every result about a solution is a result of the constant setting, and no result is transferred from one setting to the other.

The formalism is that of *Lagrangian and Hamiltonian Mechanics in Biquaternionic Form*, and the action principle is that of *The Action Principle and the Non-Quantum Limit in Biquaternionic Form*; this article applies the principle to the Schrödinger equation in its element form.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; $i$ is the central scalar imaginary, $i^{2}=-e_t$; $\mathbb{B}_{C}=\operatorname{span}_{\mathbb{R}}\{e_t,ie_t\}$ is the centre; $\mathbb{B}_{\Psi}$ is the Hermitian fixed subspace, the observables, and $\mathbb{B}_{\Phi}$ the anti-Hermitian one, the generators. The asterisk is Hermitian conjugation, the superscript $\natural$ is quaternion conjugation, $\mathrm{Sc}$ is the coefficient of $e_t$, and $\mathrm{Tr}=2\,\mathrm{Sc}$. The variable is $r'_t=c\,t'$ throughout; where a formula is more familiar in $t'$, the substitution $\mathrm{d}r'_t=c\,\mathrm{d}t'$ and $i\hbar\,c\,\partial/\partial r'_t=i\hbar\,\partial/\partial t'$ is exact and is not repeated.

## The Action in Element Form

The action is

$$
S[\tilde\Xi,\tilde\Xi^{*}]=\int \mathrm{d}r'_t\;\mathrm{Sc}\Bigl[\frac{i\hbar\,c}{2}\bigl(\tilde\Xi^{*}\partial_{r'_t}\tilde\Xi-(\partial_{r'_t}\tilde\Xi^{*})\tilde\Xi\bigr)-\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi\Bigr].
$$

The choice of variable is the parent's, and the constant multiplying the derivative is $i\hbar\,c$. Four properties must be checked, and each is a line.

### The kinetic term is Hermitian

Write the kinetic density as

$$
T=\frac{i\hbar\,c}{2}\bigl(\tilde\Xi^{*}\partial\tilde\Xi-(\partial\tilde\Xi^{*})\tilde\Xi\bigr),
$$

with $\partial=\partial_{r'_t}$. Its conjugate is

$$
T^{*}=\frac{-i\hbar\,c}{2}\bigl((\partial\tilde\Xi)^{*}\tilde\Xi-\tilde\Xi^{*}\partial\tilde\Xi\bigr)
=\frac{i\hbar\,c}{2}\bigl(\tilde\Xi^{*}\partial\tilde\Xi-(\partial\tilde\Xi^{*})\tilde\Xi\bigr)=T,
$$

so $T$ is Hermitian. The scalar part of a Hermitian element is real, because $\mathrm{Sc}(X)^{*}=\mathrm{Sc}(X^{*})=\mathrm{Sc}(X)$ when $X^{*}=X$. Hence $\mathrm{Sc}(T)$ is real.

### The potential term is Hermitian

For $\tilde H_\Psi^{*}=\tilde H_\Psi$,

$$
\bigl(\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi\bigr)^{*}=\tilde\Xi^{*}\tilde H_\Psi^{*}\tilde\Xi=\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi,
$$

so the potential density is Hermitian and its scalar part is real. The hypothesis is used here and nowhere else: a non-Hermitian $\tilde H_\Psi$ would make the potential term non-real, and the action would not be a real functional.

### The action is real

Both densities are Hermitian and the scalar part of a Hermitian element is real, so the integrand is a sum of two real numbers. The action is real.

### The pairing is the Hermitian form

The bilinear in the action is the Hermitian form

$$
\langle X,Y\rangle=\mathrm{Sc}\bigl(X^{*}Y\bigr),
$$

which is conjugate-linear in the first argument, linear in the second, and satisfies $\langle X,Y\rangle^{*}=\langle Y,X\rangle$. Read on one element, the potential term is $\langle\tilde\Xi,\tilde H_\Psi\tilde\Xi\rangle=\mathrm{Sc}(\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi)$ and the kinetic term is built on $\langle\tilde\Xi,\partial\tilde\Xi\rangle$. The pairing is not the quaternion-conjugate one, $\mathrm{Sc}(\cdot^{\natural}\cdot)$. The reason is the parent's: the symbol $L_{\tilde H_\Psi}$, left multiplication by the Hermitian $\tilde H_\Psi$, is Hermitian for this form, since

$$
\langle\tilde H_\Psi X,Y\rangle=\mathrm{Sc}\bigl((\tilde H_\Psi X)^{*}Y\bigr)=\mathrm{Sc}\bigl(X^{*}\tilde H_\Psi^{*}Y\bigr)=\mathrm{Sc}\bigl(X^{*}\tilde H_\Psi Y\bigr)=\langle X,\tilde H_\Psi Y\rangle,
$$

and an action that reproduces the equation must be built on the form for which the symbol is Hermitian. The companion article uses the same pairing throughout, and the two articles' currents are therefore comparable term by term.

### The variation

Treat $\tilde\Xi$ and $\tilde\Xi^{*}$ as independent over $\mathbb{C}$, which is the standard device for a first-order action. Vary $\tilde\Xi^{*}$ and hold $\tilde\Xi$ fixed. The variation of the kinetic term is

$$
\frac{i\hbar\,c}{2}\int \mathrm{d}r'_t\;\mathrm{Sc}\bigl(\delta\tilde\Xi^{*}\partial\tilde\Xi-(\partial\delta\tilde\Xi^{*})\tilde\Xi\bigr)
=i\hbar\,c\int \mathrm{d}r'_t\;\mathrm{Sc}\bigl(\delta\tilde\Xi^{*}\partial\tilde\Xi\bigr)-\frac{i\hbar\,c}{2}\Bigl[\mathrm{Sc}\bigl(\delta\tilde\Xi^{*}\tilde\Xi\bigr)\Bigr]_{\mathrm{bdy}},
$$

where integrating the second term by parts has produced the doubled first term and the boundary term, and the boundary term vanishes because $\delta\tilde\Xi^{*}$ vanishes at both ends. The potential term gives $-\int\mathrm{d}r'_t\,\mathrm{Sc}(\delta\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi)$. Collecting,

$$
\delta S=\int \mathrm{d}r'_t\;\mathrm{Sc}\Bigl[\delta\tilde\Xi^{*}\bigl(i\hbar\,c\,\partial\tilde\Xi-\tilde H_\Psi\tilde\Xi\bigr)\Bigr].
$$

The condition is therefore

$$
\mathrm{Sc}\Bigl[\delta\tilde\Xi^{*}\bigl(i\hbar\,c\,\partial\tilde\Xi-\tilde H_\Psi\tilde\Xi\bigr)\Bigr]=0
\qquad\text{for every }\delta\tilde\Xi^{*}\in\mathbb{B},
$$

and the bracket vanishes as an element of $\mathbb{B}$. The implication uses the non-degeneracy of the pairing $(X,Y)\mapsto\mathrm{Sc}(XY)$ on $\mathbb{B}$, which is the trace pairing of $\mathbb{B}\cong M_2(\mathbb{C})$: if $\mathrm{Sc}(XE)=0$ for every $X\in\mathbb{B}$, then $E=0$, as one sees by taking $X=E^{*}$, which gives $\mathrm{Sc}(E^{*}E)=\sum_\mu\lvert E_\mu\rvert^{2}$, a sum that vanishes only for $E=0$. Hence

$$
i\hbar\,c\,\partial_{r'_t}\tilde\Xi=\tilde H_\Psi\tilde\Xi.
$$

**Why this is eight real equations and not four.** $\tilde\Xi$ has four complex coefficients, that is, eight real components, and $\mathbb{B}$ is a complex vector space of dimension four. The bracket $E=i\hbar\,c\,\partial\tilde\Xi-\tilde H_\Psi\tilde\Xi$ is one element of $\mathbb{B}$, whose vanishing is four complex conditions, which are eight real conditions. The counting is the parent's and no new condition is added.

**Why the variation of $\tilde\Xi$ is not needed.** Varying $\tilde\Xi$ and holding $\tilde\Xi^{*}$ fixed gives the conjugate statement, $\delta S=\int\mathrm{d}r'_t\,\mathrm{Sc}[(-i\hbar\,c\,\partial\tilde\Xi^{*}-\tilde\Xi^{*}\tilde H_\Psi)\delta\tilde\Xi]$, whose vanishing is the conjugate of the equation. Since the action is real, the two variations are conjugates and one of them carries the content. For a real trajectory variation, with $\delta\tilde\Xi^{*}=(\delta\tilde\Xi)^{*}$, the two halves combine into

$$
\delta S=2\,\mathrm{Re}\int \mathrm{d}r'_t\;\mathrm{Sc}\bigl[\delta\tilde\Xi^{*}E\bigr],
$$

a form the companion article uses, because there the parameters are real and the variation cannot be complexified.

**Why the kinetic term is antisymmetrized.** The symmetric combination $\mathrm{Sc}(\tilde\Xi^{*}\partial\tilde\Xi)$ is complex. Its real part is a total derivative, $\mathrm{Re}\,\mathrm{Sc}(\tilde\Xi^{*}\partial\tilde\Xi)=\tfrac14\partial\rho$ with $\rho=\mathrm{Tr}(\tilde\Xi^{*}\tilde\Xi)=2\,\mathrm{Sc}(\tilde\Xi\tilde\Xi^{*})$, and its imaginary part is the whole of the kinetic Lagrangian. The antisymmetrization keeps the imaginary part and discards the total derivative, which is the same device as in the standard action $\int\bigl[(i\hbar/2)(\psi^{*}\dot\psi-\dot\psi^{*}\psi)-\psi^{*}\hat H\psi\bigr]$. The companion uses the same identity once, in its kinetic term, and the identity is not repeated there.

## The Two Writings from the Action

The parent's two writings are not two actions. There is one real functional, and the two writings are two readings of it.

**Reality forces the $i$ onto the derivative.** The kinetic density without the $i$ is

$$
\frac{\hbar\,c}{2}\bigl(\tilde\Xi^{*}\partial\tilde\Xi-(\partial\tilde\Xi^{*})\tilde\Xi\bigr),
$$

and its conjugate is its negative, so it is anti-Hermitian and its scalar part is purely imaginary. A real action therefore needs the factor $i$ on the derivative, which is what the action carries. With the $i$ fixed there, the coupling must be Hermitian, that is, it must be $-\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi$ with $\tilde H_\Psi^{*}=\tilde H_\Psi$. The variational principle therefore selects the observable writing as the one whose coupling is Hermitian, and it explains why: a real functional cannot carry an anti-Hermitian coupling.

**The generator writing is the same functional.** Since $i$ is central and $i^{2}=-e_t$, the identity

$$
-\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi=-\tilde\Xi^{*}(i\tilde H_\Phi)\tilde\Xi=-i\,\tilde\Xi^{*}\tilde H_\Phi\tilde\Xi,
\qquad
\tilde H_\Phi=-i\tilde H_\Psi\in\mathbb{B}_{\Phi},
$$

holds as an identity of the algebra, and the right-hand side is the same real term. Its variation gives

$$
i\hbar\,c\,\partial\tilde\Xi-i\tilde H_\Phi\tilde\Xi=0
\qquad\Longleftrightarrow\qquad
\partial_{r'_t}\tilde\Xi=\frac{1}{\hbar\,c}\tilde H_\Phi\tilde\Xi,
$$

which is the parent's second writing. Equivalently $\hbar\,c\,\partial\tilde\Xi=\tilde H_\Phi\tilde\Xi$. So the second writing is available from the same action, and the only thing that changed is which factor of the coupling carries the $i$.

**What would break it.** If $i$ were replaced by a non-central root $\tilde Z$ of $-e_t$, the generator $-\tilde Z\tilde H_\Psi/(\hbar\,c)$ need not be anti-Hermitian, and the second writing need not exist. The action inherits the parent's verdict, and the verdict has two steps rather than one. **Reality costs only anti-Hermiticity.** The kinetic bracket $K=\tilde\Xi^{*}\partial\tilde\Xi-(\partial\tilde\Xi^{*})\tilde\Xi$ is anti-Hermitian, and $\mathrm{Sc}(\tilde ZK)$ is real for every anti-Hermitian $\tilde Z$, because $(\tilde ZK)^{*}=K\tilde Z$ and $\mathrm{Sc}(K\tilde Z)=\mathrm{Sc}(\tilde ZK)$. The roots used in this article — $\pm i$, the units $\pm\vec e_\mu$ and the real unit vectors $\vec u$ — are all anti-Hermitian, so the reality of the action does not by itself select the central one. **Centrality is what the rest costs.** The generator $-\tilde Z\tilde H_\Psi/(\hbar\,c)$ must be anti-Hermitian for *every* Hermitian $\tilde H_\Psi$, which holds exactly when $\tilde Z$ commutes with $\tilde H_\Psi$; and the phase rotation $\tilde\Xi\mapsto\exp(\tilde Z\alpha)\tilde\Xi$ leaves the potential term invariant under the same condition. Only a central $\tilde Z$ meets it for all $\tilde H_\Psi$. Unitarity, the second writing and the phase symmetry are what the central unit buys; the reality of the action is the weakest of the four requirements.

**The counterexample.** The parent's counterexample is the sharp one: with $\tilde Z=\vec e_z$ and $\tilde H_\Psi=i\vec e_x$,

$$
\tilde Z\tilde H_\Psi=\vec e_z\,(i\vec e_x)=i\,\vec e_z\vec e_x=i\,\vec e_y,
$$

and $i\vec e_y$ is Hermitian, so the generator $-\tilde Z\tilde H_\Psi/(\hbar\,c)$ is Hermitian and not anti-Hermitian; the minus sign flips nothing, because $-1$ is real and conjugation is antilinear. The corresponding flow is not norm-preserving, and the parent's explicit computation gives the failure at $r'_t=\pi\hbar\,c/2$, where the accumulated factor is $\exp(-i\pi\vec e_y)=\cosh\pi\,e_t-i\sinh\pi\,\vec e_y$, which is not $e_t$. Here the root is anti-Hermitian and the action is still real; what fails is the flow.

**Unitarity is the anti-Hermiticity read back.** The flow of the equation is $\tilde Q(r'_t)=\exp\bigl(\tilde H_\Phi r'_t/(\hbar\,c)\bigr)=\exp(-i\theta_{\mathrm{evo}})(\cos\theta\,e_t+\sin\theta\,\vec u_\Psi)$, and its $*$-unitarity is exactly $(\tilde H_\Phi/(\hbar\,c))^{*}=-\tilde H_\Phi/(\hbar\,c)$. That anti-Hermiticity is the centrality computation above, so the conservation of the norm is the variational principle's reality statement seen from the flow side. The two are one fact about $i$.

The angle is $\theta_{\mathrm{evo}}=h_t\,r'_t/(\hbar c)$, the scalar part of the generator times the interval over $\hbar$; the vector part of the generator contributes the separate rotor angle $\theta=|\vec h_\Psi|\,r'_t/(\hbar c)$. The generator is anti-Hermitian, not Hermitian, and the anti-Hermiticity is the whole content: a purely imaginary scalar part makes the phase a real angle, and a real vector part makes the rotor a unit rotor.

## The Noether Currents

Two symmetries of the constant-setting action give two currents. Each is computed, and the conservation is checked on solutions.

### The phase rotation

Let $\tilde\Xi\mapsto e^{i\alpha}\tilde\Xi$ and $\tilde\Xi^{*}\mapsto e^{-i\alpha}\tilde\Xi^{*}$ with $\alpha$ a real number. Since $i$ is central the factor passes through every element, the kinetic density is unchanged, and the potential density is unchanged. The Lagrangian is invariant.

The Noether charge is read off the derivative's coefficient. With $\partial L/\partial(\partial\tilde\Xi)=\tfrac{i\hbar\,c}{2}\tilde\Xi^{*}$ and $\partial L/\partial(\partial\tilde\Xi^{*})=-\tfrac{i\hbar\,c}{2}\tilde\Xi$, the charge for the variation $(\delta\tilde\Xi,\delta\tilde\Xi^{*})=(i\alpha\tilde\Xi,-i\alpha\tilde\Xi^{*})$ is

$$
Q=\frac{i\hbar\,c}{2}\tilde\Xi^{*}(i\alpha\tilde\Xi)-\frac{i\hbar\,c}{2}\tilde\Xi(-i\alpha\tilde\Xi^{*})
=-\frac{\hbar\,c\,\alpha}{2}\bigl(\tilde\Xi^{*}\tilde\Xi+\tilde\Xi\tilde\Xi^{*}\bigr),
$$

the two factors of $i$ in each term giving $i^{2}=-e_t$ and the two halves being equal. So the conserved quantity, with the constants and the parameter absorbed into the normalisation, is

$$
N=\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde\Xi\bigr).
$$

Its conservation is one line from the equation and its conjugate. The equation gives $\partial\tilde\Xi=-i\tilde H_\Psi\tilde\Xi/\hbar\,c$, and its conjugate gives $\partial\tilde\Xi^{*}=i\tilde\Xi^{*}\tilde H_\Psi/\hbar\,c$. Hence

$$
\partial N=\mathrm{Sc}\bigl(\partial\tilde\Xi^{*}\,\tilde\Xi\bigr)+\mathrm{Sc}\bigl(\tilde\Xi^{*}\partial\tilde\Xi\bigr)
=\frac{i}{\hbar\,c}\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi\bigr)-\frac{i}{\hbar\,c}\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi\bigr)=0.
$$

**The factor of two.** $N$ is the parent's density up to a factor of two,

$$
\rho=\mathrm{Tr}\bigl(\tilde\Xi^{*}\tilde\Xi\bigr)=2\,\mathrm{Sc}\bigl(\tilde\Xi\tilde\Xi^{*}\bigr)=2\,\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde\Xi\bigr)=2\sum_\mu\lvert\Xi_\mu\rvert^{2}=2N\;\ge\;0,
$$

and the factor is the $\mathrm{Sc}$ against $\mathrm{Tr}$ convention, $\mathrm{Tr}=2\,\mathrm{Sc}$, not a physical normalisation. So $N=\rho/2$, and the factor is stated once. In the word of the companion article, $N=r^{2}\cosh\theta_{\mathrm{rpd}}$, so the charge reads the scale and the rapidity, and the phase rotation leaves both alone, as it must.

### Time translation

Let $r'_t\mapsto r'_t+\varepsilon$ and suppose $\tilde H_\Psi$ constant, which is the setting of the parent's Section *The Equation in Polar Variables*. The Lagrangian has no explicit dependence on $r'_t$, so the canonical energy is conserved, and it is

$$
E=\mathrm{Sc}\left[\frac{i\hbar\,c}{2}\tilde\Xi^{*}\partial\tilde\Xi-\frac{i\hbar\,c}{2}(\partial\tilde\Xi^{*})\tilde\Xi-\left(\frac{i\hbar\,c}{2}\bigl(\tilde\Xi^{*}\partial\tilde\Xi-(\partial\tilde\Xi^{*})\tilde\Xi\bigr)-\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi\right)\right]
=\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi\bigr).
$$

The two kinetic pieces cancel and the potential term survives with its sign flipped, so $E=\mathrm{Sc}(\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi)$, the parent's energy, real because the potential density is Hermitian. The outer $\mathrm{Sc}$ is not decoration: the kinetic terms and the bracket are elements of $\mathbb{B}$, and only their scalar parts are numbers.

Conservation is again one line. With $\partial\tilde\Xi=-i\tilde H_\Psi\tilde\Xi/\hbar\,c$ and $\partial\tilde\Xi^{*}=i\tilde\Xi^{*}\tilde H_\Psi/\hbar\,c$,

$$
\partial E=\frac{i}{\hbar\,c}\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde H_\Psi^{2}\tilde\Xi\bigr)-\frac{i}{\hbar\,c}\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde H_\Psi^{2}\tilde\Xi\bigr)=0,
$$

The two factors of $\tilde H_\Psi$ sit in the same order because $\tilde H_\Psi$ is a single element. The conservation is a statement about the constant setting only: it is the variational shadow of the constancy of the generator, and in the operator setting the same computation gives the continuity equation of the local energy density instead of one conserved number.

### The stress tensor, and the operator setting

In the operator setting the action has a spatial density as well, and the translations and rotations of space give the stress tensor as their Noether current. That computation belongs to *Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form*, and it is named here only to place it: it is the same construction applied to the spatial argument of the field, and its energy component reduces to $\mathrm{Sc}(\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi)$ above. Nothing of it is used or derived in this article.

### What is not here

There is no spin current. The Schrödinger equation has no spin; the field carries a rotor, but the rotor is a frame datum and carries no spin density in this equation. A "spin current" written for the Schrödinger case would be a confusion of the rotor's geometry with a conserved spin, and the Dirac spin current belongs to the polar article on the Dirac equation.

## The Two Settings

The parent's two settings are different equations, and the variational principle inherits the distinction.

**The constant setting.** $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ with $h_t$ and $\vec h_\Psi$ fixed numbers. The equation is an ordinary differential equation in $r'_t$, the action is an integral over that one variable, and its Euler–Lagrange equation is the equation. The solution is the closed form $\tilde Q(r'_t)=\exp(-i\theta_{\mathrm{evo}})$, and along it the two currents of the previous section are conserved. Everything in this article about solutions is about this setting.

**The operator setting.** $\tilde H_\Psi=\hat H\,e_t$ with $\hat H=-\hbar^{2}\Delta_\Phi/2m+V$. The equation is the ordinary Schrödinger equation, a partial differential equation. The action is the same expression with the operator in the coupling and an integral over $r'_t$ and the three space coordinates, and its Euler–Lagrange equation is the same equation, now a field equation. Its solution is not a finite product of exponentials, and the closed form of the constant setting does not apply.

**No transfer.** A statement about the constant setting is not a statement about the operator setting. The conserved energy of the previous section is a number in the first and a density in the second. The closed-form propagator of the first has no counterpart in the second. The variational principle is stated for the constant setting here; the operator setting's action is the standard field-theoretic one with a central operator, and its working out belongs to *The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case* and to the companion article's Madelung section.

## What the Variational Principle Adds and What It Relabels

**Adds.** A compact statement of the equation, one action and one variation. The two currents in one derivation. The variational reading of the two writings: one functional, and the choice of which factor carries the central $i$. And the variational status of the two settings, which the action makes explicit rather than implicit.

**Relabels.** No new prediction; the equation is the parent's. No new solution; the solution is the parent's closed form. No new principle; the action is the standard first-order action of a complex field with a Hermitian symbol, and its reality and its Noether currents are the standard ones.

**The distinction that matters.** The variational principle is integral in form and local in content. It is a functional on the whole trajectory, and its Euler–Lagrange equation is a local differential equation. It is therefore not opposed to the local equation; it is equivalent to it, and it is richer in what it delivers, because a symmetry of the functional delivers a current that the equation alone does not name.

**One claim of the parent is sharpened.** The parent says the second writing is available because $i$ is central. The action says why that availability is not a convenience: a real functional needs the $i$ on the derivative and a Hermitian coupling, so the observable writing is the one the action is written in, and the generator writing is the same functional read with the switch. The centrality of $i$ is what makes the two readings coincide, and no non-central root does.

## Open Questions

**1. A potential with a vector part.** The action's reality needs only $\tilde H_\Psi^{*}=\tilde H_\Psi$, and the polar parent records that a Hamiltonian with $\vec h_\Psi\ne0$ carries a central field off the centre at once. The variational principle inherits the question in its own terms: whether the carrier's closure under the flow, and the reality of the action, survive a potential whose vector part is not aligned with a fixed axis. Nothing here settles it.

**2. The stress tensor, as a check.** The energy component of the operator action's stress tensor should reproduce the tensor of *Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form*. This is a check and not a derivation, and it is not performed here.

**3. The relation to the path integral.** The variational principle is the extremum of an action; the path integral is the sum over configurations. Both are integral in form and they are different objects. The path-integral version belongs to *The Path Integral and the Schrödinger Equation in Biquaternionic Form*, and the relation between the two is not attempted here.

## Summary

One action has the parent's equation as its Euler–Lagrange equation,

$$
S=\int \mathrm{d}r'_t\;\mathrm{Sc}\Bigl[\frac{i\hbar\,c}{2}\bigl(\tilde\Xi^{*}\partial_{r'_t}\tilde\Xi-(\partial_{r'_t}\tilde\Xi^{*})\tilde\Xi\bigr)-\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi\Bigr],
$$

with $\tilde H_\Psi\in\mathbb{B}_{\Psi}$ Hermitian and $\tilde\Xi\in\mathbb{B}$ one general element. The action is real because both densities are Hermitian and the scalar part of a Hermitian element is real. The pairing is the Hermitian form $\mathrm{Sc}(\cdot^{*}\cdot)$, which is the form for which left multiplication by $\tilde H_\Psi$ is Hermitian.

The variation of $\tilde\Xi^{*}$ returns the equation, and the non-degeneracy of the trace pairing makes the return exact. The two writings are one functional: the reality of the action puts the central $i$ on the derivative and forces a Hermitian coupling, and the generator writing is the same term written with $\tilde H_\Phi=-i\tilde H_\Psi$. The centrality of $i$ is what makes the two readings coincide, and the parent's counterexample with $\vec e_z$ shows that no non-central root does.

Two symmetries give two currents. The phase rotation gives $N=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)=\rho/2$, the parent's density up to the $\mathrm{Tr}=2\,\mathrm{Sc}$ convention. The time translation, in the constant setting, gives $E=\mathrm{Sc}(\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi)$, the parent's energy. Each conservation is one line from the equation and its conjugate. There is no spin current, because the equation has no spin.

The article adds a compact statement, one derivation of the two currents, and a variational reading of the two writings. It adds no prediction and no solution. The polar variational principle is the companion article, and it is genuinely different.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^{2}=-e_t$ |
| $i$ | Central scalar imaginary, $i^{2}=-e_t$ |
| $\mathbb{B}_{C}$ | Centre, $\operatorname{span}_{\mathbb{R}}\{e_t,ie_t\}$ |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace, the observables |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian subspace, the generators |
| $*,\ \natural$ | Hermitian conjugation, quaternion conjugation |
| $\mathrm{Sc},\ \mathrm{Tr}=2\,\mathrm{Sc}$ | Scalar part, trace |
| $r'_t=c\,t'$ | Material time; the variable of the element form |
| $\tilde\Xi\in\mathbb{B}$ | The field: one general element, eight real components |
| $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ | Hermitian Hamiltonian; the observable |
| $\tilde H_\Phi=-i\tilde H_\Psi$ | The switch image; the generator, up to the real scale $\hbar\,c$ |
| $S$ | The action; $L$ its Lagrangian density |
| $\partial_{r'_t}$ | Derivative with respect to the material time |
| $N=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ | Phase Noether charge; $\rho=2N$ |
| $\rho=\mathrm{Tr}(\tilde\Xi^{*}\tilde\Xi)=2\sum_\mu\lvert\Xi_\mu\rvert^{2}\ge0$ | The parent's density |
| $E=\mathrm{Sc}(\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi)$ | Energy; the time-translation charge |
| $\tilde Q(r'_t)=\exp(-i\theta_{\mathrm{evo}})(\cos\theta\,e_t+\sin\theta\,\vec u_\Psi)$ | Propagator of the constant setting; $\theta_{\mathrm{evo}}=h_t r'_t/(\hbar c)$, $\theta=\lvert\vec h_\Psi\rvert r'_t/(\hbar c)$ |
| $h_t,\ \vec h_\Psi$ | Scalar and vector parts of $\tilde H_\Psi$, numbers in the constant setting |
| $\hat H$ | The operator of the operator setting |

## Further Reading

- [The Schrödinger Equation in Biquaternionic Form](the-schrodinger-equation-in-biquaternionic-form.html), for the equation, its two writings, the carrier and the centrality of $i$.
- [The Schrödinger Equation in Biquaternionic Polar Variables](the-schrodinger-equation-in-biquaternionic-polar-variables.html), for the word of the field, the two norms and Madelung's pair.
- [The Variational Principle and the Schrödinger Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-schrodinger-equation-in-biquaternionic-polar-variables.html), the companion, where the parameters of the word are the variables.
- [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html), for the stress tensor named in the fourth section.
- [Noether's Theorem in Biquaternionic Form](noethers-theorem-in-biquaternionic-form.html), for the general statement of the construction used twice here.
- [Lagrangian and Hamiltonian Mechanics in Biquaternionic Form](lagrangian-and-hamiltonian-mechanics-in-biquaternionic-form.html), for the action and the Legendre transform in the non-quantum setting.
- [The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case](the-hydrogen-atom-in-biquaternionic-form-the-non-relativistic-case.html), for the operator setting.
- [Unitarity from Centrality: The Biquaternion Norm-Preservation Theorem](unitarity-from-centrality-the-biquaternion-norm-preservation-theorem.html), for the anti-Hermiticity that the flow's unitarity is.
- [Mirror Biquaternions and the Phy–Psy Switch](mirror-biquaternions-and-the-phy-psy-switch.html), for the pair $\tilde H_\Psi$, $\tilde H_\Phi$.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the standard action and the standard variation.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the first-order Schrödinger action and its antisymmetrisation.
- E. Noether, "Invariante Variationsprobleme," *Nachrichten der Gesellschaft der Wissenschaften zu Göttingen* (1918) 235–257, for the construction that produces the two currents.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, §8, for the tensor formulation of the polar variational principle, which the companion article contrasts with the biquaternionic one.
