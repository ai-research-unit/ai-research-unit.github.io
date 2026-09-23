# __Scalar Pair Creation in Biquaternionic Form__

## Introduction

The companion articles *Canonical Quantization of the Biquaternion Klein–Gordon Field*, *The Quantized Scalar Field in Biquaternionic Form* and *The Scalar Fock Space in Biquaternionic Form* quantize the free scalar field in a fixed spacetime and build its state space. The first physical process that a quantized field can undergo is the creation of particles from the vacuum by a **background that varies in time**, and this article treats that process for the scalar sector. Its subject is scalar pair creation: the production of a particle–antiparticle pair by a classical background that breaks time-translation invariance.

The physics is standard and the framework's role is once again delimiting. A background that depends on time destroys the splitting of the field into positive- and negative-frequency modes that a static background supports. Between an early (in) region and a late (out) region, the same field operator admits two different mode decompositions, and the relation between them is a **Bogoliubov transformation** mixing the annihilation and creation operators. The in-vacuum is not the out-vacuum; it is a squeezed state in the out-modes, and it contains pairs. The general theory of Bogoliubov transformations and their role in quantized fields is not derived here; it belongs to the companion article *Bogoliubov Transformations in Biquaternionic Form* and to the standard literature, and this article imports it and applies it to the scalar sector of the biquaternion framework. What the article does derive is the biquaternion reading of the process and, on an exactly solvable background, its magnitude.

Three statements organise the article.

1. **The background is a classical central-valued field.** In the framework the scalar background that drives the process is a classical field $\tilde\sigma(\tilde X)=\sigma(\tilde X)e_0$ in the center, and the coupling that makes the mass spacetime-dependent is central. The background therefore enters the field equation exactly as the mass does, and the mode equation is an ordinary second-order oscillator equation with a time-dependent frequency.
2. **Pair creation is a two-mode squeezing, and it conserves charge.** The transformation mixes $\hat a_{\mathbf k}$ with $\hat b_{-\mathbf k}^\dagger$; its generator commutes with the $U(1)$ charge, so pairs are created with zero net charge, and the mean pair number is $|\beta_{\mathbf k}|^2$. The framework's canonical continuous symmetry — the central $U(1)$ — is what makes the antiparticle well defined and the pair the unit of production.
3. **The framework supplies no new mechanism.** The algebra contributes the central-valuedness of the background and the norm-form reading of the in- and out-frequencies; the transformation itself is the standard Bogoliubov mixing on an imported module, because the scalar sector has no native ladder in $\mathbb{B}$, as the companion Fock-space article proves.

The article is organised as follows. The next section sets up the background and the mode equation. The following section defines the in- and out-regions and the Bogoliubov transformation. The next section derives the mean pair number and the vacuum persistence amplitude. The section after that works the exactly solvable sudden-quench limit and verifies it numerically. A section states the biquaternion reading and the charge-conservation statement. The article closes with the standard/open separation.

- Companion article *Canonical Quantization of the Biquaternion Klein–Gordon Field*, for the mode expansion, the mode algebra, and the charge.
- Companion article *The Quantized Scalar Field in Biquaternionic Form*, for the field operator, its frequency split, and the Wightman function.
- Companion article *The Scalar Fock Space in Biquaternionic Form*, for the Fock space, the vacuum, and the charge superselection sectors.
- Companion article *Bogoliubov Transformations in Biquaternionic Form*, for the general theory of the mixing, its canonical normalization, and its realization as a squeezing of the Fock space.
- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the field equation and its frequency branches.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the conserved $U(1)$ current $\tilde J\in\mathbb{M}_-$ and the charge.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the material four-wavevector and the norm form.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$, and $i$ is the central scalar imaginary. The material and informational sectors are $\mathbb{M}_-$ and $\mathbb{M}_+$; the center is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$. The gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$ and $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$. Natural units $\hbar=c=1$ are used throughout, with $E_{\mathbf{p}}=\sqrt{\mathbf{p}^2+\mu^2}$ and $\mu=mc/\hbar$; dimensionful factors are restored where they carry meaning. The scalar field is $\tilde{\Phi}=\phi\,e_0$ with $\phi$ complex. A dot denotes $\partial_t$.

## The Background and the Mode Equation

A classical background that couples to the scalar field through the invariant $\mathrm{Sc}(\tilde{\Phi}^\dagger\tilde{\Phi})$ shifts the mass term. Write the background as a central-valued classical field,

$$
\tilde\sigma(\tilde{X})=\sigma(\tilde{X})\,e_0\in\mathbb{C}_{\mathbb{B}},
\qquad
\mathcal{L}_{\mathrm{int}}=-g\,\mathrm{Sc}\!\left(\tilde{\Phi}^\dagger\tilde{\Phi}\right)\sigma ,
$$

so that the effective equation of motion is

$$
\left(\Box-\mu^2-g\,\sigma(\tilde{X})\right)\tilde{\Phi}=0 .
$$

If the background is **homogeneous**, $\sigma=\sigma(t)$, the spatial translation invariance survives and the field can be expanded in spatial plane waves,

$$
\phi(t,\mathbf{x})=\int\!\frac{d^3k}{(2\pi)^3}\,u_{\mathbf k}(t)\,e^{\,i\mathbf{k}\cdot\mathbf{x}},
$$

with the mode functions satisfying

$$
\ddot u_{\mathbf k}+\omega_{\mathbf k}^2(t)\,u_{\mathbf k}=0,
\qquad
\omega_{\mathbf k}^2(t)=\mathbf{k}^2+\mu^2+g\,\sigma(t).
$$

This is the central object of the article: a set of independent harmonic oscillators with a time-dependent frequency. The biquaternion packaging is that the effective mass-squared is read off the norm form of a material four-wavevector whose time component is not conserved: the mass shell is the level set

$$
N(\tilde{K}_{\mathbf k}(t))=-\left(\mu^2+g\,\sigma(t)\right)e_0 ,
\qquad
\tilde{K}_{\mathbf k}(t)=i\omega_{\mathbf k}(t)e_0+\mathbf{k},
$$

equivalently $\mu^2+g\,\sigma(t)=-\mathrm{Sc}(N(\tilde{K}_{\mathbf k}(t)))$, since $N(\tilde{K})=(\mathbf{k}^2-\omega^2)e_0$ for this four-wavevector. A time-dependent background is therefore a time-dependent level set of the norm form. The interaction itself is central: $\mathcal{L}_{\mathrm{int}}$ is a multiple of $e_0$, it commutes with the algebra, and no spinor structure is involved.

Two standard realizations fix the interpretation. A **mass quench** changes $\mu^2$ abruptly or smoothly in time; an **expanding background** makes the frequency depend on time through a scale factor, $u''+(\mathbf k^2+a^2(t)\mu^2)u=0$ in conformal time for a suitably coupled field. Both are captured by $\omega_{\mathbf k}^2(t)$ above, and both are standard cosmological and condensed-matter problems; the framework writes their operator in the notation of the center.

If the background is not homogeneous, $\sigma=\sigma(\tilde X)$, the mode equation acquires a spatial dependence, and the decomposition into spatial plane waves with a single $\mathbf k$ fails; a slowly varying background can be treated in the adiabatic approximation, and a rapidly varying one requires the full field equation. This article keeps the homogeneous case, which is the exactly solvable one and the one that isolates the temporal mechanism.

## In and Out Regions and the Bogoliubov Transformation

Suppose the background is constant in the remote past and in the remote future,

$$
\sigma(t)\to\sigma_{\mathrm{in}}\ \ (t\to-\infty),
\qquad
\sigma(t)\to\sigma_{\mathrm{out}}\ \ (t\to+\infty),
$$

with corresponding asymptotic frequencies

$$
\omega_{\mathrm{in},\mathbf k}=\sqrt{\mathbf{k}^2+\mu^2+g\sigma_{\mathrm{in}}},
\qquad
\omega_{\mathrm{out},\mathbf k}=\sqrt{\mathbf{k}^2+\mu^2+g\sigma_{\mathrm{out}}} .
$$

In each asymptotic region the field admits a standard mode decomposition, and the corresponding operators define the **in** and **out** Fock spaces. The two sets of positive-frequency solutions are, in each region,

$$
u_{\mathbf k}^{\mathrm{in}}(t)\sim\frac{1}{\sqrt{2\omega_{\mathrm{in},\mathbf k}}}e^{-i\omega_{\mathrm{in},\mathbf k}t},
\qquad
u_{\mathbf k}^{\mathrm{out}}(t)\sim\frac{1}{\sqrt{2\omega_{\mathrm{out},\mathbf k}}}e^{-i\omega_{\mathrm{out},\mathbf k}t},
$$

normalized by the Klein–Gordon inner product. Both sets solve the same second-order equation; they are related by a linear transformation with time-independent coefficients,

$$
u_{\mathbf k}^{\mathrm{in}}(t)=\alpha_{\mathbf k}\,u_{\mathbf k}^{\mathrm{out}}(t)+\beta_{\mathbf k}\,\big(u_{\mathbf k}^{\mathrm{out}}(t)\big)^* ,
$$

and the same transformation acts on the mode operators. Writing the in-operators in terms of the out-operators, and mixing the two charge-conjugate modes that carry the same momentum magnitude,

$$
\hat a_{\mathbf k}^{\mathrm{out}}
=\alpha_{\mathbf k}\,\hat a_{\mathbf k}^{\mathrm{in}}+\beta_{\mathbf k}^*\,\hat b_{-\mathbf k}^{\mathrm{in}\dagger},
\qquad
\hat b_{-\mathbf k}^{\mathrm{out}}
=\alpha_{\mathbf k}\,\hat b_{-\mathbf k}^{\mathrm{in}}+\beta_{\mathbf k}^*\,\hat a_{\mathbf k}^{\mathrm{in}\dagger},
$$

with the same $\alpha,\beta$ for the conjugate pair (the coefficients for $+\mathbf k$ and $-\mathbf k$ are equal because the background is homogeneous and isotropic). The transformation is **canonical**: imposing the in-commutators and the out-commutators, and using the reality of the mixing, gives

$$
|\alpha_{\mathbf k}|^2-|\beta_{\mathbf k}|^2=1 .
$$

The general derivation of this structure — the Bogoliubov group, its canonical form, and its realization as a squeezing of the Fock space — is the subject of the companion article *Bogoliubov Transformations in Biquaternionic Form*; it is imported here without re-derivation. What the present article uses is only its two consequences: the mixing of creation and annihilation operators, and the normalization $|\alpha|^2-|\beta|^2=1$.

The transform is **charge neutral**, and this is the framework's central symmetry at work. The generator of the two-mode mixing is

$$
\hat G_{\mathbf k}=\hat a_{\mathbf k}^\dagger\hat b_{-\mathbf k}^\dagger
-\hat a_{\mathbf k}\hat b_{-\mathbf k},
$$

and a direct computation gives $[\hat Q,\hat G_{\mathbf k}]=0$, so the background creates only **pairs**: a particle of momentum $\mathbf k$ and an antiparticle of momentum $-\mathbf k$, with total momentum zero and total charge zero. The $U(1)$ charge of the companion articles is thus the selection rule that makes the pair the unit of production, and it is the same central symmetry whose phase multiplies the field operator.

## The Number of Created Pairs and the Vacuum Persistence Amplitude

Because the in- and out-mode operators differ, the in-vacuum is not annihilated by the out-annihilation operators. Writing $\hat a^{\mathrm{out}}=\alpha\hat a^{\mathrm{in}}+\beta^*\hat b^{\mathrm{in}\dagger}$ (and the conjugate relation), the in-vacuum contains pairs of out-quanta, and the mean number of particles of momentum $\mathbf k$ in the in-vacuum is

$$
\langle 0_{\mathrm{in}}|\hat a_{\mathbf k}^{\mathrm{out}\dagger}\hat a_{\mathbf k}^{\mathrm{out}}|0_{\mathrm{in}}\rangle
=|\beta_{\mathbf k}|^2\,(2\pi)^3\delta^{(3)}(0),
$$

with the same value for the antiparticle mode. The delta function is the volume factor of the continuum normalization, $[\hat a_{\mathbf k},\hat a^\dagger_{\mathbf k'}]=(2\pi)^3\delta^{(3)}(\mathbf k-\mathbf k')$, and the convention-free statement is the one per mode: the **mean number of created pairs** per mode is $|\beta_{\mathbf k}|^2$, and the total pair number density is the momentum integral

$$
\frac{N_{\mathrm{pairs}}}{V}=\int\!\frac{d^3k}{(2\pi)^3}\,|\beta_{\mathbf k}|^2 .
$$

The in-vacuum is a **two-mode squeezed state** in the out-Fock space. Its expansion in the out-occupation basis is

$$
|0_{\mathrm{in}}\rangle
=\frac{1}{\cosh r_{\mathbf k}}\sum_{n\ge0}\big(\tanh r_{\mathbf k}\big)^n\,|n_{\mathbf k},n_{-\mathbf k}\rangle_{\mathrm{out}},
\qquad
\tanh r_{\mathbf k}=\left|\frac{\beta_{\mathbf k}}{\alpha_{\mathbf k}}\right| ,
$$

with the pair states $|n_{\mathbf k},n_{-\mathbf k}\rangle$ containing equal numbers of particles and antiparticles; the equal numbers are the charge-conservation statement of the previous section. The phase of the coefficient in each term is the phase of $\beta_{\mathbf k}/\alpha_{\mathbf k}$, fixed to one by a redefinition of the out-modes and immaterial for the moduli below. Two consequences follow, and both were verified numerically.

**The mean pair number is the squeezing strength.** Since $\tanh^2 r=|\beta|^2/|\alpha|^2=|\beta|^2/(1+|\beta|^2)$, the geometric sum gives

$$
\langle\hat N_{\mathrm{pairs}}\rangle=|\beta_{\mathbf k}|^2 ,
$$

exactly. **The vacuum persistence amplitude is the inverse of $|\alpha|$.** The overlap of the in- and out-vacua is

$$
\big|\langle 0_{\mathrm{out}}|0_{\mathrm{in}}\rangle\big|^2
=\frac{1}{\cosh^2 r_{\mathbf k}}
=\frac{1}{|\alpha_{\mathbf k}|^2}
=\frac{1}{1+|\beta_{\mathbf k}|^2},
$$

so the probability that no pair is created in the mode is $1/(1+|\beta|^2)$, and the probability that something is created is $|\beta|^2/(1+|\beta|^2)$. For a continuum of modes the total persistence amplitude is the product

$$
\big|\langle 0_{\mathrm{out}}|0_{\mathrm{in}}\rangle\big|^2
=\exp\left(-\int\!\frac{d^3k}{(2\pi)^3}\,\ln\!\big(1+|\beta_{\mathbf k}|^2\big)\right),
$$

which is the standard result and is the quantity that the functional integral produces as the modulus of the vacuum-to-vacuum amplitude.

**Verification.** On the truncated two-mode Fock space the charge commutes with the pair generator to machine precision, and the geometric expansion above was checked against $|\beta|^2$ for $|\beta|^2=0,0.25,1,3,12$: the mean occupation and the overlap agreed with $|\beta|^2$ and $1/(1+|\beta|^2)$ to ten decimal places in every case.

## An Exactly Solvable Case: the Sudden Quench

The simplest background with a nonzero effect is a sudden change of the frequency at $t=0$, the limit of a quench that is fast compared with the oscillation period. Take

$$
\omega(t)=\omega_1\ (\text{for }t<0),
\qquad
\omega(t)=\omega_2\ (\text{for }t>0),
$$

a real scalar mode for economy; the complex case doubles the modes and the pair count below is the same per mode. The in-mode is $u_{\mathrm{in}}(t)=e^{-i\omega_1 t}/\sqrt{2\omega_1}$ for $t<0$. The constant prefactor is common to both regions and cancels in the matching, so continuity of $u$ and $\dot u$ at $t=0$ may be imposed on the un-normalized form $e^{-i\omega_1 t}$, whose value and derivative at the origin are $1$ and $-i\omega_1$; this requires the out-region form

$$
e^{-i\omega_1 t}=A\,e^{-i\omega_2 t}+B\,e^{+i\omega_2 t},
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

Rescaling to the canonical normalizations of both modes, $u_{\mathrm{in}}=\alpha u_{\mathrm{out}}+\beta u_{\mathrm{out}}^*$ with $u_{\mathrm{in}}=e^{-i\omega_1t}/\sqrt{2\omega_1}$ and $u_{\mathrm{out}}=e^{-i\omega_2t}/\sqrt{2\omega_2}$, gives

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

**Verification.** Direct mode matching gives $|\beta|^2=0.125$ for $(\omega_1,\omega_2)=(1,2)$, in agreement with $(\omega_2-\omega_1)^2/(4\omega_1\omega_2)$; for $(3.7,1.1)$ it gives $0.4152334$; for $(0.5,0.9)$ it gives $0.0888889$; and for $(2,2)$ it gives zero. In every case $|\alpha|^2-|\beta|^2=1$ to fifteen decimal places. The formula is the standard sudden-limit result for a scalar field mode, and its biquaternion content is only that $\omega_1,\omega_2$ are the two asymptotically constant level sets of the norm form.

## The Biquaternion Reading

Four statements summarise what the framework contributes to scalar pair creation.

**The background is central.** The driving field is a classical element of $\mathbb{C}_{\mathbb{B}}$; it enters the equation only through the invariant $\mathrm{Sc}(\tilde{\Phi}^\dagger\tilde{\Phi})$, it commutes with every element of the algebra, and it carries no spinor index. Pair creation by a scalar background is therefore a process in the center, and the state module is not acted on by the background.

**The in- and out-modes are the parent's plane waves at two masses.** Each asymptotic region has its own on-shell level set $N(\tilde{K})=-\mu^2-g\sigma_{\mathrm{in/out}}$, and the Bogoliubov coefficients are the overlap of two such plane-wave systems. The mass shell, which is a level set of the norm form, is time-dependent during the transition and constant on either side.

**The charge selects pairs.** The framework's canonical continuous symmetry is the central $U(1)$, whose Noether current $\tilde J$ lies in $\mathbb{M}_-$ and whose charge is the difference of the particle and antiparticle number operators. Because the generator of the mixing commutes with the charge, the background creates pairs and not single quanta; the pair is the framework's unit of production for the same reason it is the standard one.

**The algebra supplies no mechanism of its own.** The mixing is a Bogoliubov transformation on the Fock space built from an imported module; the scalar sector has no native ladder in $\mathbb{B}$, because no pair in the algebra realizes $[\tilde a,\tilde a^\dagger]=e_0$. The framework contributes the central-valued background, the norm-form reading of the asymptotic frequencies, and the notation; it contributes no new creation mechanism. The process is standard scalar quantum field theory in an external background, transcribed.

The standard realizations are worth naming for orientation. Cosmological particle creation in an expanding universe, with the scale factor playing the role of the background, and the dynamical Casimir effect, in which a moving boundary modulates the modes, are the standard examples; the electromagnetic analogue — pair creation in a strong electric field — is the Schwinger process, and it belongs to the charged-field setting rather than to the free scalar background treated here. The framework's notation applies to all of them through the mode equation, and modifies none of them.

## What Is Standard and What Is Open

**Standard, and imported.** The mode equation with a time-dependent frequency; the in/out decomposition and the asymptotic frequencies; the Bogoliubov transformation, its canonical normalization $|\alpha|^2-|\beta|^2=1$, and its realization as a two-mode squeezing; the mean pair number $|\beta|^2$; the vacuum persistence amplitude $1/|\alpha|^2$ and its continuum product; the sudden-quench result $|\beta|^2=(\omega_2-\omega_1)^2/(4\omega_1\omega_2)$. None of this is re-derived here, and none of it depends on the biquaternion structure beyond the kinematical conventions.

**Open in the biquaternion framework.**

- **The intrinsic background.** The background is taken to be a classical central-valued field. Whether the framework supplies a dynamical background — a scalar condensate with its own equation of motion — and whether the back-reaction on the metric or on the field is expressible in the algebra, is not settled.
- **The intrinsic Bogoliubov theory.** Whether the Bogoliubov group has a native realization in the framework's algebraic structures, beyond the standard Fock-space squeezing, is the subject of the companion article *Bogoliubov Transformations in Biquaternionic Form*; the scalar sector by itself offers no native ladder to realize it.
- **The choice of vacuum.** In a time-dependent background the in- and out-vacua differ, and the framework inherits the standard ambiguity of the vacuum in curved or time-dependent settings. Whether the framework's complex structure selects a preferred vacuum is open.
- **The back-reaction and the energy.** The energy density of the created pairs, and its back-reaction on the background, are standard questions; whether the trace formula of the informational sector gives them a finite-dimensional reading is not shown.
- **Empirical content.** Whether scalar pair creation in the framework makes a prediction distinguishing it from standard scalar field theory in the same background is open.

## Summary

Scalar pair creation is the production of particle–antiparticle pairs by a classical background that breaks time-translation invariance. In the framework the background is a central-valued classical field $\tilde\sigma=\sigma e_0$ coupling through $\mathrm{Sc}(\tilde{\Phi}^\dagger\tilde{\Phi})$, so a homogeneous background makes the frequency time-dependent, $\ddot u_{\mathbf k}+\omega_{\mathbf k}^2(t)u_{\mathbf k}=0$ with $\omega_{\mathbf k}^2=\mathbf{k}^2+\mu^2+g\sigma(t)$, and the effective mass-squared is the time-dependent level set of the norm form of the material four-wavevector, $\mu^2+g\sigma=-\mathrm{Sc}(N(\tilde{K}))$. The in- and out-mode decompositions are related by a Bogoliubov transformation mixing $\hat a_{\mathbf k}$ with $\hat b_{-\mathbf k}^\dagger$, with $|\alpha_{\mathbf k}|^2-|\beta_{\mathbf k}|^2=1$.

The transformation is charge neutral: its generator $\hat G_{\mathbf k}=\hat a_{\mathbf k}^\dagger\hat b_{-\mathbf k}^\dagger-\hat a_{\mathbf k}\hat b_{-\mathbf k}$ commutes with the $U(1)$ charge, so the background creates pairs and not single quanta. The in-vacuum is a two-mode squeezed state, the mean number of created pairs per mode is $|\beta_{\mathbf k}|^2$, and the vacuum persistence amplitude is $|\langle0_{\mathrm{out}}|0_{\mathrm{in}}\rangle|^2=1/|\alpha_{\mathbf k}|^2=1/(1+|\beta_{\mathbf k}|^2)$, with the continuum product $\exp\big(-\int\frac{d^3k}{(2\pi)^3}\ln(1+|\beta_{\mathbf k}|^2)\big)$. On the sudden-quench background $\omega_1\to\omega_2$ the result is $|\beta|^2=(\omega_2-\omega_1)^2/(4\omega_1\omega_2)$, verified numerically, with $|\alpha|^2-|\beta|^2=1$ to fifteen decimal places.

The process is standard scalar quantum field theory in an external background, transcribed into the framework's notation. The framework contributes the central-valued background, the norm-form reading of the asymptotic frequencies, and the charge selection rule; it contributes no creation mechanism of its own, because the scalar sector has no native ladder in $\mathbb{B}$. The general Bogoliubov theory is imported from the standard literature and from the generalities of the second-quantized framework, and is not re-derived here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary |
| $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ | Center; value space of the background |
| $\tilde{\Phi}=\phi\,e_0$, $\tilde\sigma=\sigma\,e_0$ | Scalar field and central background |
| $\mathcal{L}_{\mathrm{int}}=-g\,\mathrm{Sc}(\tilde{\Phi}^\dagger\tilde{\Phi})\sigma$ | Central interaction |
| $\omega_{\mathbf k}^2(t)=\mathbf{k}^2+\mu^2+g\sigma(t)$ | Time-dependent frequency |
| $\tilde{K}_{\mathbf k}(t)=i\omega_{\mathbf k}(t)e_0+\mathbf{k}$ | Material four-wavevector; $N(\tilde{K})$ its norm form |
| $\omega_{\mathrm{in}},\omega_{\mathrm{out}}$ | Asymptotic frequencies |
| $\alpha_{\mathbf k},\beta_{\mathbf k}$ | Bogoliubov coefficients, $\vert\alpha\vert^2-\vert\beta\vert^2=1$ |
| $r_{\mathbf k}$, $\tanh r_{\mathbf k}=\vert\beta_{\mathbf k}/\alpha_{\mathbf k}\vert$ | Squeezing parameter |
| $\hat G_{\mathbf k}=\hat a_{\mathbf k}^\dagger\hat b_{-\mathbf k}^\dagger-\hat a_{\mathbf k}\hat b_{-\mathbf k}$ | Pair-creation generator; $[\hat Q,\hat G_{\mathbf k}]=0$ |
| $\vert 0_{\mathrm{in}}\rangle=(1/\cosh r_{\mathbf k})\sum_n(\tanh r_{\mathbf k})^n\,\vert n_{\mathbf k},n_{-\mathbf k}\rangle_{\mathrm{out}}$ | In-vacuum as a two-mode squeezed state |
| $\langle\hat N_{\mathrm{pairs}}\rangle=\vert\beta_{\mathbf k}\vert^2$ | Mean number of created pairs per mode |
| $\vert\langle0_{\mathrm{out}}\vert0_{\mathrm{in}}\rangle\vert^2=1/\vert\alpha_{\mathbf k}\vert^2$ | Vacuum persistence amplitude |
| $\vert\beta\vert^2=(\omega_2-\omega_1)^2/(4\omega_1\omega_2)$ | Sudden-quench result |
| $\hat Q=\int\frac{d^3p}{(2\pi)^3}(\hat a^\dagger\hat a-\hat b^\dagger\hat b)$ | Conserved $U(1)$ charge; pairs have $Q=0$ |
| $\mathrm{Tr}(e_0)=2$, $\mathrm{Tr}[\tilde A,\tilde B]=0$ | Trace identity; no bosonic mode in $\mathbb{B}$ |

## Further Reading

- N. N. Bogoliubov, "On a new method in the theory of superconductivity," *Nuovo Cimento* **7** (1958) 794–805, for the canonical transformation mixing creation and annihilation operators.
- N. N. Bogoliubov and D. V. Shirkov, *Introduction to the Theory of Quantized Fields* (Interscience, 1959), for the Bogoliubov transformation in quantum field theory and the in/out formalism.
- L. Parker, "Particle creation in expanding universes," *Physical Review Letters* **21** (1968) 562–564, and "Quantized fields and particle creation in expanding universes. I," *Physical Review* **183** (1969) 1057–1068, for particle creation by a time-dependent background.
- S. A. Fulling, *Aspects of Quantum Field Theory in Curved Space-Time* (Cambridge, 1989), for the in/out decomposition, the vacuum persistence amplitude, and the ambiguity of the vacuum.
- N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space* (Cambridge, 1982), for the mode equation, the Bogoliubov coefficients, and the sudden and adiabatic limits.
- J. Schwinger, "On gauge invariance and vacuum polarization," *Physical Review* **82** (1951) 664–679, for pair creation in a strong electric field, the electromagnetic analogue.
- G. T. Moore, "Quantum theory of the electromagnetic field in a variable-length one-dimensional cavity," *Journal of Mathematical Physics* **11** (1970) 2679–2691, for the dynamical Casimir effect.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), and S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the mode expansion and the charge whose conservation selects pairs.
