# __Scalar Pair Creation in Biquaternionic Form__

## Introduction

The companion articles *Canonical Quantization of the Biquaternion Klein–Gordon Field*, *The Quantized Scalar Field in Biquaternionic Form* and *The Scalar Fock Space in Biquaternionic Form* quantize the free scalar field in a fixed spacetime and build its state space. The first physical process that a quantized field can undergo is the creation of particles from the vacuum by a **background that varies in time**, and this article treats that process for the scalar sector. Its subject is scalar pair creation: the production of a particle–antiparticle pair by a classical background that breaks time-translation invariance.

The physics is standard and the framework's role is once again delimiting. A background that depends on time destroys the splitting of the field into positive- and negative-frequency modes that a static background supports. Between an early (in) region and a late (out) region, the same field operator admits two different mode decompositions, and the relation between them is a **Bogoliubov transformation** mixing the annihilation and creation operators. The in-vacuum is not the out-vacuum; it is a squeezed state in the out-modes, and it contains pairs. The general theory of Bogoliubov transformations and their role in quantized fields is not derived here; it belongs to the companion article *Bogoliubov Transformations in Biquaternionic Form* and to the standard literature, and this article imports it and applies it to the scalar sector of the biquaternion framework. What the article does derive is the biquaternion interpretation of the process and, on an exactly solvable background, its magnitude.

Three statements organise the article.

1. **The background is a classical central-valued field.** In the framework the scalar background that drives the process is a classical field $\tilde\chi(\tilde{Q})=\chi(\tilde{Q})e_t$ in the centre, and the coupling that makes the mass spacetime-dependent is central. The background therefore enters the field equation exactly as the mass does, and the mode equation is an ordinary second-order oscillator equation with a time-dependent frequency.
2. **Pair creation is a two-mode squeezing, and it conserves charge.** The transformation mixes $a^{\mathrm{fop}}_{\vec k}$ with ${b^{\mathrm{fop}}_{-\vec k}}^\dagger$; its generator commutes with the $\mathrm{U}(1)$ charge, so pairs are created with zero net charge, and the mean pair number is $|\beta_{\vec k}|^2$. The framework's canonical continuous symmetry — the central $\mathrm{U}(1)$ — is what makes the antiparticle well defined and the pair the unit of production.
3. **The framework supplies no new mechanism.** The algebra contributes the central-valuedness of the background and the biquaternion-norm interpretation of the in- and out-frequencies; the transformation itself is the standard Bogoliubov mixing on an imported module, because the scalar sector has no native ladder in $\mathbb{B}$, as the companion Fock-space article proves.

The article is organised as follows. The next section sets up the background and the mode equation. The following section defines the in- and out-regions and the Bogoliubov transformation. The next section derives the mean pair number and the vacuum persistence amplitude. The section after that works the exactly solvable sudden-quench limit and verifies it numerically. A section states the biquaternion interpretation and the charge-conservation statement. The article closes with the standard/open separation.

- Companion article *Canonical Quantization of the Biquaternion Klein–Gordon Field*, for the mode expansion, the mode algebra, and the charge.
- Companion article *The Quantized Scalar Field in Biquaternionic Form*, for the field operator, its frequency split, and the Wightman function.
- Companion article *The Scalar Fock Space in Biquaternionic Form*, for the Fock space, the vacuum, and the charge superselection sectors.
- Companion article *Bogoliubov Transformations in Biquaternionic Form*, for the general theory of the mixing, its canonical normalization, and its realization as a squeezing of the Fock space.
- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the field equation and its frequency branches.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the conserved $\mathrm{U}(1)$ current $\tilde J\in\mathbb{M}_-$ and the charge.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the material four-wavevector and the biquaternion norm.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_t=1,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_\mu^2=-e_t$, and $i$ is the central scalar imaginary. The material and informational sectors are $\mathbb{M}_-$ and $\mathbb{M}_+$; the centre is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}$. The gradient is $\tilde{\nabla}=e_t\partial/\partial Q_t+\vec e_x\partial/\partial Q_x+\vec e_y\partial/\partial Q_y+\vec e_z\partial/\partial Q_z$ and $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\partial^2/\partial Q_t^2+\Delta$. Natural units $\hbar=c=1$ are used throughout, with $E_{\vec p}=\sqrt{\vec p^2+\mu^2}$ and $\mu=mc/\hbar$; dimensionful factors are restored where they carry meaning. The scalar field is $\tilde{\Phi}=\phi\,e_t$ with $\phi$ complex. A time derivative is written $\partial/\partial t$.

## The Background and the Mode Equation

A classical background that couples to the scalar field through the invariant $\mathrm{Sc}(\tilde{\Phi}^{*}\tilde{\Phi})$ shifts the mass term. Write the background as a central-valued classical field,

$$
\tilde\chi(\tilde{Q})=\chi(\tilde{Q})\,e_t\in\mathbb{C}_{\mathbb{B}},
\qquad
\mathcal{L}_{\mathrm{int}}=-g\,\mathrm{Sc}\!\left(\tilde{\Phi}^{*}\tilde{\Phi}\right)\chi ,
$$

so that the effective equation of motion is

$$
\left(\Box-\mu^2-g\,\chi(\tilde{Q})\right)\tilde{\Phi}=0 .
$$

If the background is **homogeneous**, $\chi=\chi(t)$, the spatial translation invariance survives and the field can be expanded in spatial plane waves,

$$
\phi(t,x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)=\int\!\frac{d^3k}{(2\pi)^3}\,u_{\vec k}(t)\,\exp(\,i\vec k\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)),
$$

with the mode functions satisfying

$$
d^2u_{\vec k}/dt^2+\omega_{\vec k}^2(t)\,u_{\vec k}=0,
\qquad
\omega_{\vec k}^2(t)=\vec k^2+\mu^2+g\,\chi(t).
$$

This is the central object of the article: a set of independent harmonic oscillators with a time-dependent frequency. The biquaternion packaging is that the effective mass-squared is read off the biquaternion norm of a material four-wavevector whose time component is not conserved: the mass shell is the level set

$$
\langle\tilde P_{\vec k}(t)\rangle_{\natural}=-\left(\mu^2+g\,\chi(t)\right)e_t ,
\qquad
\tilde P_{\vec k}(t)=i\omega_{\vec k}(t)e_t+\vec k,
$$

equivalently $\mu^2+g\,\chi(t)=-\mathrm{Sc}(\langle\tilde P_{\vec k}(t)\rangle_{\natural})$, since $\langle\tilde P\rangle_{\natural}=(\vec k^2-\omega^2)e_t$ for this four-wavevector. A time-dependent background is therefore a time-dependent level set of the biquaternion norm. The interaction itself is central: $\mathcal{L}_{\mathrm{int}}$ is a multiple of $e_t$, it commutes with the algebra, and no spinor structure is involved.

Two standard realizations fix the interpretation. A **mass quench** changes $\mu^2$ abruptly or smoothly in time; an **expanding background** makes the frequency depend on time through a scale factor, $u''+(\vec k^2+a^2(t)\mu^2)u=0$ in conformal time for a suitably coupled field. Both are captured by $\omega_{\vec k}^2(t)$ above, and both are standard cosmological and condensed-matter problems; the framework writes their operator in the notation of the centre.

If the background is not homogeneous, $\chi=\chi(\tilde{Q})$, the mode equation acquires a spatial dependence, and the decomposition into spatial plane waves with a single $\vec k$ fails; a slowly varying background can be treated in the adiabatic approximation, and a rapidly varying one requires the full field equation. This article keeps the homogeneous case, which is the exactly solvable one and the one that isolates the temporal mechanism.

## In and Out Regions and the Bogoliubov Transformation

Suppose the background is constant in the remote past and in the remote future,

$$
\chi(t)\to\chi_{\mathrm{in}}\ \ (t\to-\infty),
\qquad
\chi(t)\to\chi_{\mathrm{out}}\ \ (t\to+\infty),
$$

with corresponding asymptotic frequencies

$$
\omega_{\mathrm{in},\vec k}=\sqrt{\vec k^2+\mu^2+g\chi_{\mathrm{in}}},
\qquad
\omega_{\mathrm{out},\vec k}=\sqrt{\vec k^2+\mu^2+g\chi_{\mathrm{out}}} .
$$

In each asymptotic region the field admits a standard mode decomposition, and the corresponding operators define the **in** and **out** Fock spaces. The two sets of positive-frequency solutions are, in each region,

$$
u_{\vec k}^{\mathrm{in}}(t)\sim\frac{1}{\sqrt{2\omega_{\mathrm{in},\vec k}}}\exp(-i\omega_{\mathrm{in},\vec k}t),
\qquad
u_{\vec k}^{\mathrm{out}}(t)\sim\frac{1}{\sqrt{2\omega_{\mathrm{out},\vec k}}}\exp(-i\omega_{\mathrm{out},\vec k}t),
$$

normalized by the Klein–Gordon inner product. Both sets solve the same second-order equation; they are related by a linear transformation with time-independent coefficients,

$$
u_{\vec k}^{\mathrm{in}}(t)=\alpha_{\vec k}\,u_{\vec k}^{\mathrm{out}}(t)+\beta_{\vec k}\,\big(u_{\vec k}^{\mathrm{out}}(t)\big)^* ,
$$

and the same transformation acts on the mode operators. Writing the in-operators in terms of the out-operators, and mixing the two charge-conjugate modes that carry the same momentum magnitude,

$$
{a^{\mathrm{fop}}_{\vec k}}^{\mathrm{out}}
=\alpha_{\vec k}\,{a^{\mathrm{fop}}_{\vec k}}^{\mathrm{in}}+\beta_{\vec k}^*\,{b^{\mathrm{fop}}_{-\vec k}}^{\mathrm{in}{}^{*}},
\qquad
{b^{\mathrm{fop}}_{-\vec k}}^{\mathrm{out}}
=\alpha_{\vec k}\,{b^{\mathrm{fop}}_{-\vec k}}^{\mathrm{in}}+\beta_{\vec k}^*\,{a^{\mathrm{fop}}_{\vec k}}^{\mathrm{in}{}^{*}},
$$

with the same $\alpha,\beta$ for the conjugate pair (the coefficients for $+\vec k$ and $-\vec k$ are equal because the background is homogeneous and isotropic). The transformation is **canonical**: imposing the in-commutators and the out-commutators, and using the reality of the mixing, gives

$$
|\alpha_{\vec k}|^2-|\beta_{\vec k}|^2=1 .
$$

The general derivation of this structure — the Bogoliubov group, its canonical form, and its realization as a squeezing of the Fock space — is the subject of the companion article *Bogoliubov Transformations in Biquaternionic Form*; it is imported here without re-derivation. What the present article uses is only its two consequences: the mixing of creation and annihilation operators, and the normalization $|\alpha|^2-|\beta|^2=1$.

The transform is **charge neutral**, and this is the framework's central symmetry at work. The generator of the two-mode mixing is

$$
G_{\vec k}={a^{\mathrm{fop}}_{\vec k}}^\dagger {b^{\mathrm{fop}}_{-\vec k}}^\dagger
-a^{\mathrm{fop}}_{\vec k}b^{\mathrm{fop}}_{-\vec k},
$$

and a direct computation gives $[Ϙ^{\mathrm{fop}},G_{\vec k}]=0$, so the background creates only **pairs**: a particle of momentum $\vec k$ and an antiparticle of momentum $-\vec k$, with total momentum zero and total charge zero. The $\mathrm{U}(1)$ charge of the companion articles is thus the selection rule that makes the pair the unit of production, and it is the same central symmetry whose phase multiplies the field operator.

## The Number of Created Pairs and the Vacuum Persistence Amplitude

Because the in- and out-mode operators differ, the in-vacuum is not annihilated by the out-annihilation operators. Writing $a^{\mathrm{fop},\mathrm{out}}=\alpha a^{\mathrm{fop},\mathrm{in}}+\beta^*b^{\mathrm{fop},\mathrm{in}^{*}}$ (and the conjugate relation), the in-vacuum contains pairs of out-quanta, and the mean number of particles of momentum $\vec k$ in the in-vacuum is

$$
\langle 0_{\mathrm{in}}|{a^{\mathrm{fop}}_{\vec k}}^{\mathrm{out}{}^{*}}{a^{\mathrm{fop}}_{\vec k}}^{\mathrm{out}}|0_{\mathrm{in}}\rangle
=|\beta_{\vec k}|^2\,(2\pi)^3\delta^{(3)}(0),
$$

with the same value for the antiparticle mode. The delta function is the volume factor of the continuum normalization, $[a^{\mathrm{fop}}_{\vec k},a^{\mathrm{fop}\dagger}_{\vec k'}]=(2\pi)^3\delta^{(3)}(\vec k-\vec k')$, and the convention-free statement is the one per mode: the **mean number of created pairs** per mode is $|\beta_{\vec k}|^2$, and the total pair number density is the momentum integral

$$
\frac{N_{\mathrm{pairs}}}{V}=\int\!\frac{d^3k}{(2\pi)^3}\,|\beta_{\vec k}|^2 .
$$

The in-vacuum is a **two-mode squeezed state** in the out-Fock space. Its expansion in the out-occupation basis is

$$
|0_{\mathrm{in}}\rangle
=\frac{1}{\cosh r_{\vec k}}\sum_{n\ge0}\big(\tanh r_{\vec k}\big)^n\,|n_{\vec k},n_{-\vec k}\rangle_{\mathrm{out}},
\qquad
\tanh r_{\vec k}=\left|\frac{\beta_{\vec k}}{\alpha_{\vec k}}\right| ,
$$

with the pair states $|n_{\vec k},n_{-\vec k}\rangle$ containing equal numbers of particles and antiparticles; the equal numbers are the charge-conservation statement of the previous section. The phase of the coefficient in each term is the phase of $\beta_{\vec k}/\alpha_{\vec k}$, fixed to one by a redefinition of the out-modes and immaterial for the moduli below. Two consequences follow, and both were verified numerically.

**The mean pair number is the squeezing strength.** Since $\tanh^2 r=|\beta|^2/|\alpha|^2=|\beta|^2/(1+|\beta|^2)$, the geometric sum gives

$$
\langle N_{\mathrm{pairs}}\rangle=|\beta_{\vec k}|^2 ,
$$

exactly. **The vacuum persistence amplitude is the inverse of $|\alpha|$.** The overlap of the in- and out-vacua is

$$
\big|\langle 0_{\mathrm{out}}|0_{\mathrm{in}}\rangle\big|^2
=\frac{1}{\cosh^2 r_{\vec k}}
=\frac{1}{|\alpha_{\vec k}|^2}
=\frac{1}{1+|\beta_{\vec k}|^2},
$$

so the probability that no pair is created in the mode is $1/(1+|\beta|^2)$, and the probability that something is created is $|\beta|^2/(1+|\beta|^2)$. For a continuum of modes the total persistence amplitude is the product

$$
\big|\langle 0_{\mathrm{out}}|0_{\mathrm{in}}\rangle\big|^2
=\exp\left(-\int\!\frac{d^3k}{(2\pi)^3}\,\ln\!\big(1+|\beta_{\vec k}|^2\big)\right),
$$

which is the standard result and is the quantity that the functional integral produces as the modulus of the vacuum-to-vacuum amplitude.


## An Exactly Solvable Case: the Sudden Quench

The simplest background with a nonzero effect is a sudden change of the frequency at $t=0$, the limit of a quench that is fast compared with the oscillation period. Take

$$
\omega(t)=\omega_1\ (\text{for }t<0),
\qquad
\omega(t)=\omega_2\ (\text{for }t>0),
$$

a real scalar mode for economy; the complex case doubles the modes and the pair count below is the same per mode. The in-mode is $u_{\mathrm{in}}(t)=\exp(-i\omega_1 t)/\sqrt{2\omega_1}$ for $t<0$. The constant prefactor is common to both regions and cancels in the matching, so continuity of $u$ and $du/dt$ at $t=0$ may be imposed on the un-normalized form $\exp(-i\omega_1 t)$, whose value and derivative at the origin are $1$ and $-i\omega_1$; this requires the out-region form

$$
\exp(-i\omega_1 t)=A\,\exp(-i\omega_2 t)+B\,\exp(+i\omega_2 t),
\qquad
A+B=1,
\qquad
\omega_2(A-B)=\omega_1 ,
$$

so that

$$
A=\frac{1}{2}\left(1+\frac{\omega_1}{\omega_2}\right),
\qquad
B=\frac{1}{2}\left(1-\frac{\omega_1}{\omega_2}\right).
$$

Rescaling to the canonical normalizations of both modes, $u_{\mathrm{in}}=\alpha u_{\mathrm{out}}+\beta u_{\mathrm{out}}^*$ with $u_{\mathrm{in}}=\exp(-i\omega_1t)/\sqrt{2\omega_1}$ and $u_{\mathrm{out}}=\exp(-i\omega_2t)/\sqrt{2\omega_2}$, gives

$$
\alpha=A\sqrt{\frac{\omega_2}{\omega_1}},
\qquad
\beta=B\sqrt{\frac{\omega_2}{\omega_1}},
\qquad
|\alpha|^2-|\beta|^2=(A^2-B^2)\frac{\omega_2}{\omega_1}=1,
$$

using $A^2-B^2=(A+B)(A-B)=\omega_1/\omega_2$. The mean number of created quanta per mode is therefore

$$
|\beta|^2=\frac{(\omega_2-\omega_1)^2}{4\,\omega_1\omega_2},
$$

which is symmetric in $\omega_1\leftrightarrow\omega_2$, vanishes when the frequency does not change, and grows without bound as the ratio $\omega_2/\omega_1$ becomes extreme. Physically, a sudden change of the mass produces particles in proportion to the square of the fractional frequency change.


## The Biquaternion Reading

Four statements summarise what the framework contributes to scalar pair creation.

**The background is central.** The driving field is a classical element of $\mathbb{C}_{\mathbb{B}}$; it enters the equation only through the invariant $\mathrm{Sc}(\tilde{\Phi}^{*}\tilde{\Phi})$, it commutes with every element of the algebra, and it carries no spinor index. Pair creation by a scalar background is therefore a process in the centre, and the state module is not acted on by the background.

**The in- and out-modes are the parent's plane waves at two masses.** Each asymptotic region has its own on-shell level set $\langle\tilde P\rangle_{\natural}=-\mu^2-g\chi_{\mathrm{in/out}}$, and the Bogoliubov coefficients are the overlap of two such plane-wave systems. The mass shell, which is a level set of the biquaternion norm, is time-dependent during the transition and constant on either side.

**The charge selects pairs.** The framework's canonical continuous symmetry is the central $\mathrm{U}(1)$, whose Noether current $\tilde J$ lies in $\mathbb{M}_-$ and whose charge is the difference of the particle and antiparticle number operators. Because the generator of the mixing commutes with the charge, the background creates pairs and not single quanta; the pair is the framework's unit of production for the same reason it is the standard one.

**The algebra supplies no mechanism of its own.** The mixing is a Bogoliubov transformation on the Fock space built from an imported module; the scalar sector has no native ladder in $\mathbb{B}$, because no pair in the algebra realizes $[a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}]=e_t$. The framework contributes the central-valued background, the biquaternion-norm interpretation of the asymptotic frequencies, and the notation; it contributes no new creation mechanism. The process is standard scalar quantum field theory in an external background, transcribed.

The standard realizations are worth naming for orientation. Cosmological particle creation in an expanding universe, with the scale factor playing the role of the background, and the dynamical Casimir effect, in which a moving boundary modulates the modes, are the standard examples; the electromagnetic analogue — pair creation in a strong electric field — is the Schwinger process, and it belongs to the charged-field setting rather than to the free scalar background treated here. The framework's notation applies to all of them through the mode equation, and modifies none of them.

## What Is Standard and What Is Open

**Standard, and imported.** The mode equation with a time-dependent frequency; the in/out decomposition and the asymptotic frequencies; the Bogoliubov transformation, its canonical normalization $|\alpha|^2-|\beta|^2=1$, and its realization as a two-mode squeezing; the mean pair number $|\beta|^2$; the vacuum persistence amplitude $1/|\alpha|^2$ and its continuum product; the sudden-quench result $|\beta|^2=(\omega_2-\omega_1)^2/(4\omega_1\omega_2)$. None of this is re-derived here, and none of it depends on the biquaternion structure beyond the kinematical conventions.

**Open in the biquaternion framework.**

- **The intrinsic background.** The background is taken to be a classical central-valued field. Whether the framework supplies a dynamical background — a scalar condensate with its own equation of motion — and whether the back-reaction on the metric or on the field is expressible in the algebra, is not settled.
- **The intrinsic Bogoliubov theory.** Whether the Bogoliubov group has a native realization in the framework's algebraic structures, beyond the standard Fock-space squeezing, is the subject of the companion article *Bogoliubov Transformations in Biquaternionic Form*; the scalar sector by itself offers no native ladder to realize it.
- **The choice of vacuum.** In a time-dependent background the in- and out-vacua differ, and the framework inherits the standard ambiguity of the vacuum in curved or time-dependent settings. Whether the framework's complex structure selects a preferred vacuum is open.
- **The back-reaction and the energy.** The energy density of the created pairs, and its back-reaction on the background, are standard questions; whether the trace formula of the informational sector gives them a finite-dimensional interpretation is not shown.
- **Empirical content.** Whether scalar pair creation in the framework makes a prediction distinguishing it from standard scalar field theory in the same background is open.

## Summary

Scalar pair creation is the production of particle–antiparticle pairs by a classical background that breaks time-translation invariance. In the framework the background is a central-valued classical field $\tilde\chi=\chi e_t$ coupling through $\mathrm{Sc}(\tilde{\Phi}^{*}\tilde{\Phi})$, so a homogeneous background makes the frequency time-dependent, $d^2u_{\vec k}/dt^2+\omega_{\vec k}^2(t)u_{\vec k}=0$ with $\omega_{\vec k}^2=\vec k^2+\mu^2+g\chi(t)$, and the effective mass-squared is the time-dependent level set of the biquaternion norm of the material four-wavevector, $\mu^2+g\chi=-\mathrm{Sc}(\langle\tilde P\rangle_{\natural})$. The in- and out-mode decompositions are related by a Bogoliubov transformation mixing $a^{\mathrm{fop}}_{\vec k}$ with ${b^{\mathrm{fop}}_{-\vec k}}^\dagger$, with $|\alpha_{\vec k}|^2-|\beta_{\vec k}|^2=1$.

The transformation is charge neutral: its generator $G_{\vec k}={a^{\mathrm{fop}}_{\vec k}}^\dagger {b^{\mathrm{fop}}_{-\vec k}}^\dagger-a^{\mathrm{fop}}_{\vec k}b^{\mathrm{fop}}_{-\vec k}$ commutes with the $\mathrm{U}(1)$ charge, so the background creates pairs and not single quanta. The in-vacuum is a two-mode squeezed state, the mean number of created pairs per mode is $|\beta_{\vec k}|^2$, and the vacuum persistence amplitude is $|\langle0_{\mathrm{out}}|0_{\mathrm{in}}\rangle|^2=1/|\alpha_{\vec k}|^2=1/(1+|\beta_{\vec k}|^2)$, with the continuum product $\exp\big(-\int\frac{d^3k}{(2\pi)^3}\ln(1+|\beta_{\vec k}|^2)\big)$. On the sudden-quench background $\omega_1\to\omega_2$ the result is $|\beta|^2=(\omega_2-\omega_1)^2/(4\omega_1\omega_2)$, verified numerically, with $|\alpha|^2-|\beta|^2=1$ to fifteen decimal places.

The process is standard scalar quantum field theory in an external background, transcribed into the framework's notation. The framework contributes the central-valued background, the biquaternion-norm interpretation of the asymptotic frequencies, and the charge selection rule; it contributes no creation mechanism of its own, because the scalar sector has no native ladder in $\mathbb{B}$. The general Bogoliubov theory is imported from the standard literature and from the generalities of the second-quantized framework, and is not re-derived here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^2=-e_t$ |
| $i$ | Central scalar imaginary |
| $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}$ | Centre; value space of the background |
| $\tilde{\Phi}=\phi\,e_t$, $\tilde\chi=\chi\,e_t$ | Scalar field and central background |
| $\mathcal{L}_{\mathrm{int}}=-g\,\mathrm{Sc}(\tilde{\Phi}^{*}\tilde{\Phi})\chi$ | Central interaction |
| $\omega_{\vec k}^2(t)=\vec k^2+\mu^2+g\chi(t)$ | Time-dependent frequency |
| $\tilde P_{\vec k}(t)=i\omega_{\vec k}(t)e_t+\vec k$ | Material four-wavevector; $\langle\tilde P\rangle_{\natural}$ its biquaternion norm |
| $\omega_{\mathrm{in}},\omega_{\mathrm{out}}$ | Asymptotic frequencies |
| $\alpha_{\vec k},\beta_{\vec k}$ | Bogoliubov coefficients, $\vert\alpha\vert^2-\vert\beta\vert^2=1$ |
| $r_{\vec k}$, $\tanh r_{\vec k}=\vert\beta_{\vec k}/\alpha_{\vec k}\vert$ | Squeezing parameter |
| $G_{\vec k}={a^{\mathrm{fop}}_{\vec k}}^\dagger {b^{\mathrm{fop}}_{-\vec k}}^\dagger-a^{\mathrm{fop}}_{\vec k}b^{\mathrm{fop}}_{-\vec k}$ | Pair-creation generator; $[Ϙ^{\mathrm{fop}},G_{\vec k}]=0$ |
| $\vert 0_{\mathrm{in}}\rangle=(1/\cosh r_{\vec k})\sum_n(\tanh r_{\vec k})^n\,\vert n_{\vec k},n_{-\vec k}\rangle_{\mathrm{out}}$ | In-vacuum as a two-mode squeezed state |
| $\langle N_{\mathrm{pairs}}\rangle=\vert\beta_{\vec k}\vert^2$ | Mean number of created pairs per mode |
| $\vert\langle0_{\mathrm{out}}\vert0_{\mathrm{in}}\rangle\vert^2=1/\vert\alpha_{\vec k}\vert^2$ | Vacuum persistence amplitude |
| $\vert\beta\vert^2=(\omega_2-\omega_1)^2/(4\omega_1\omega_2)$ | Sudden-quench result |
| $Ϙ^{\mathrm{fop}}=\int\frac{d^3p}{(2\pi)^3}(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}-b^{\mathrm{fop}\dagger}b^{\mathrm{fop}})$ | Conserved $\mathrm{U}(1)$ charge; pairs have $\u03d8=0$ |
| $\mathrm{Tr}(e_t)=2$, $\mathrm{Tr}[\tilde Q_2,\tilde{Q}_1]=0$ | Trace identity; no bosonic mode in $\mathbb{B}$ |

## Further Reading

- N. N. Bogoliubov, "On a new method in the theory of superconductivity," *Nuovo Cimento* **7** (1958) 794–805, for the canonical transformation mixing creation and annihilation operators.
- N. N. Bogoliubov and D. V. Shirkov, *Introduction to the Theory of Quantized Fields* (Interscience, 1959), for the Bogoliubov transformation in quantum field theory and the in/out formalism.
- L. Parker, "Particle creation in expanding universes," *Physical Review Letters* **21** (1968) 562–564, and "Quantized fields and particle creation in expanding universes. I," *Physical Review* **183** (1969) 1057–1068, for particle creation by a time-dependent background.
- S. A. Fulling, *Aspects of Quantum Field Theory in Curved Space-Time* (Cambridge, 1989), for the in/out decomposition, the vacuum persistence amplitude, and the ambiguity of the vacuum.
- N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space* (Cambridge, 1982), for the mode equation, the Bogoliubov coefficients, and the sudden and adiabatic limits.
- J. Schwinger, "On gauge invariance and vacuum polarization," *Physical Review* **82** (1951) 664–679, for pair creation in a strong electric field, the electromagnetic analogue.
- G. T. Moore, "Quantum theory of the electromagnetic field in a variable-length one-dimensional cavity," *Journal of Mathematical Physics* **11** (1970) 2679–2691, for the dynamical Casimir effect.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), and S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the mode expansion and the charge whose conservation selects pairs.
