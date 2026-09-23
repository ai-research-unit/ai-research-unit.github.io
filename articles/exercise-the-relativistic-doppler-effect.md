# __Exercise: The Relativistic Doppler Effect__

## Introduction

This is one of the exercises in the relativity series. It is a set of worked problems in the relativistic Doppler effect, using the framework and the notation of the companion articles *Relativistic Mechanics in Biquaternionic Form* and *The Lorentz Transformation as a Biquaternionic Rotation*. Those two articles are the parents of this exercise: they set up the four-vectors of $\mathbb{M}_-$ and the boost rotor that acts on them, and what follows applies them to the light of a moving source. Nothing new is introduced, and every result below is obtained from the tools already defined there.

**What is assumed.** The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$, and the scalar imaginary $i$ with $i^2 = -1$. The anti-Hermitian subspace $\mathbb{M}_-$ (imaginary scalar part, real vector part) and the Hermitian subspace $\mathbb{M}_+$. The norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ and the scalar projection $\mathrm{Sc}$. The four-wavevector $\tilde{K} = i\omega/c\,e_0 + \mathbf{k}$ from the table of four-vectors in *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*. The rotor conjugation $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ with $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$, and the boost biquaternion
$$
\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}},
\qquad
\tanh\psi = \frac{u}{c},
\qquad
\cosh\psi = \gamma,
\qquad
\sinh\psi = \gamma\beta .
$$
Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value; the numerical instance is in vacuum, $c = c_0$.

**What is to be shown.** The problems are: (1) the four-wavevector, its null norm form, its invariant phase, and an invariant expression for the frequency an observer measures; (2) the boost of the four-wavevector and the general Doppler formula; (3) the longitudinal case; (4) the transverse case — which is in fact *two* inequivalent cases; (5) aberration and the forward cone; (6) a numerical instance and the non-relativistic limit. Each problem is stated and then solved in full; the value of an exercise article is in the solutions.

**Notation for the problem.** A **source** is at rest in the *source frame* and emits monochromatic plane light of angular frequency $\omega_0$ and wavevector $\mathbf{k}_0 = (\omega_0/c)\hat{\mathbf{k}}_0$. An **observer** is at rest in the *observer frame*, which moves with constant velocity $\mathbf{u}$ relative to the source frame; $u = |\mathbf{u}|$, $\beta = u/c$, $\gamma = (1-\beta^2)^{-1/2}$. The angle $\theta$ is measured **in the source frame** between $\mathbf{u}$ and the propagation direction $\hat{\mathbf{k}}_0$. Primed quantities refer to the observer frame. A receding observer has $\theta = 0$; an approaching one has $\theta = \pi$.

## Problem 1: The Four-Wavevector, the Phase, and the Frequency Invariant

**Statement.** (a) Write $\tilde{K}$ and show that light has $N(\tilde{K}) = 0$. (b) Define the phase of the plane wave and show that it is invariant under a rotor conjugation. (c) Show that an observer of four-velocity $\tilde{U}$ measures the frequency
$$
\omega_{\mathrm{obs}} = -\,\mathrm{Sc}\!\left(\tilde{K}\bar{\tilde{U}}\right),
$$
and check the formula both in the observer's rest frame and in the source frame.

**Solution (a).** The four-wavevector is the element of $\mathbb{M}_-$
$$
\tilde{K} = \frac{i\omega}{c}\,e_0 + \mathbf{k},
\qquad
\mathbf{k} = k_1e_1 + k_2e_2 + k_3e_3,
\qquad
k = |\mathbf{k}| .
$$
Its norm form is
$$
N(\tilde{K}) = \tilde{K}\bar{\tilde{K}} = \left(\frac{i\omega}{c}\right)^2 + \mathbf{k}^2 = -\frac{\omega^2}{c^2} + k^2 .
$$
For light in a medium of local speed $c = 1/\sqrt{\epsilon\mu}$ the dispersion relation is $k = \omega/c$, so
$$
N(\tilde{K}) = 0 :
$$
the four-wavevector of light is a **null** element of $\mathbb{M}_-$, i.e. a zero divisor of the algebra, exactly as the light cone of Minkowski space is the zero-divisor cone (see *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and the mass-shell relation of *Relativistic Mechanics in Biquaternionic Form*). The contrast with matter is instructive: a massive de Broglie wave has $\tilde{K} = \tilde{P}/\hbar$ and hence $N(\tilde{K}) = -m^2c^2/\hbar^2$, a fixed negative norm form, whereas for light the norm form vanishes. The null condition is what makes the Doppler problem a one-parameter problem in each direction: the shift depends only on the direction of $\mathbf{k}$, through the angle $\theta$, and on $\beta$ — not on the magnitude $k$.

**Solution (b).** Fix the plane-wave convention $\propto e^{i\Phi}$ with
$$
\Phi = \mathrm{Sc}\!\left(\tilde{K}\bar{\tilde{X}}\right)
= \left(\frac{i\omega}{c}\right)(ic\,t) + \mathbf{k}\cdot\mathbf{x}
= \mathbf{k}\cdot\mathbf{x} - \omega t ,
\qquad
\tilde{X} = ic\,t\,e_0 + \mathbf{x} .
$$
Let $\tilde{\Lambda}$ be any unit-norm biquaternion and let $\tilde{K}' = \tilde{\Lambda}\tilde{K}\tilde{\Lambda}^\dagger$, $\tilde{X}' = \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$. Then
$$
\tilde{K}'\bar{\tilde{X}}'
= \tilde{\Lambda}\tilde{K}\tilde{\Lambda}^\dagger\;\overline{\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger}
= \tilde{\Lambda}\tilde{K}\tilde{\Lambda}^\dagger\,\overline{\tilde{\Lambda}^\dagger}\,\bar{\tilde{X}}\,\bar{\tilde{\Lambda}} .
$$
Since $\tilde{\Lambda}^\dagger = \bar{\tilde{\Lambda}}^*$ and quaternion and complex conjugation commute, $\overline{\tilde{\Lambda}^\dagger} = \overline{\bar{\tilde{\Lambda}}^*} = \tilde{\Lambda}^*$; hence the inner pair collapses,
$$
\tilde{\Lambda}^\dagger\overline{\tilde{\Lambda}^\dagger} = \bar{\tilde{\Lambda}}^*\,\tilde{\Lambda}^* = (\bar{\tilde{\Lambda}}\tilde{\Lambda})^* = \bar{\tilde{\Lambda}}\tilde{\Lambda} = e_0 ,
$$
so $\tilde{K}'\bar{\tilde{X}}' = \tilde{\Lambda}(\tilde{K}\bar{\tilde{X}})\bar{\tilde{\Lambda}}$. The scalar projection is cyclic, $\mathrm{Sc}(PAP) = \mathrm{Sc}(AP^2)$, and with $P\bar{P} = e_0$,
$$
\mathrm{Sc}\!\left(\tilde{\Lambda}\,(\tilde{K}\bar{\tilde{X}})\,\bar{\tilde{\Lambda}}\right)
= \mathrm{Sc}\!\left((\tilde{K}\bar{\tilde{X}})\,\bar{\tilde{\Lambda}}\tilde{\Lambda}\right)
= \mathrm{Sc}\!\left(\tilde{K}\bar{\tilde{X}}\right) .
$$
Hence $\Phi' = \Phi$: the phase is a scalar of the algebra and of the Lorentz group. This is the biquaternion form of the statement that the phase of a plane wave is an invariant, and it is what makes the transformation of the frequency a transformation of the four-wavevector alone.

**Solution (c).** Let the observer carry the timelike four-velocity $\tilde{U} = \gamma_u(ic\,e_0 + \mathbf{u}_{\mathrm{obs}})$, normalized by $N(\tilde{U}) = -c^2$. In the observer's rest frame $\tilde{U} = ic\,e_0$ and $\bar{\tilde{U}} = ic\,e_0$, so
$$
-\,\mathrm{Sc}\!\left(\tilde{K}\bar{\tilde{U}}\right)
= -\,\mathrm{Sc}\!\left(\left(\frac{i\omega}{c}e_0 + \mathbf{k}\right)(ic\,e_0)\right)
= -\,\mathrm{Sc}\!\left(-\,\omega\,e_0 + ic\,\mathbf{k}\right)
= \omega ,
$$
which is the frequency that frame assigns to the wave. In the source frame the same observer has four-velocity $\tilde{U} = \gamma(ic\,e_0 + \mathbf{u})$ with $\bar{\tilde{U}} = \gamma(ic\,e_0 - \mathbf{u})$, and
$$
\mathrm{Sc}\!\left(\tilde{K}\bar{\tilde{U}}\right)
= \left(\frac{i\omega_0}{c}\right)(\gamma ic) - \mathbf{k}_0\cdot(-\gamma\mathbf{u})
= -\gamma\omega_0 + \gamma\mathbf{k}_0\cdot\mathbf{u}
= -\gamma\omega_0\left(1 - \beta\cos\theta\right),
$$
using $\mathbf{k}_0\cdot\mathbf{u} = (\omega_0/c)u\cos\theta = \omega_0\beta\cos\theta$. Therefore
$$
\omega_{\mathrm{obs}} = -\,\mathrm{Sc}\!\left(\tilde{K}\bar{\tilde{U}}\right)
= \gamma\,\omega_0\left(1 - \beta\cos\theta\right).
$$
The frequency measured by an observer is thus an invariant contraction of the wave four-vector with the observer's four-velocity. This is the general Doppler formula, obtained without choosing a frame and without composing a boost; Problem 2 obtains the same result from the rotor, and the agreement is a check on the boost-direction convention.

## Problem 2: The Boost of the Four-Wavevector and the General Formula

**Statement.** (a) State the rotor conjugation for a boost and the component action it induces on a general element of $\mathbb{M}_-$. (b) Apply it to $\tilde{K}$ and derive the frequency and wavevector in the observer frame. (c) Show that the transformed wavevector is again null. (d) Verify the result against the invariant formula of Problem 1.

**Solution (a).** The boost with velocity $\mathbf{u}$ is generated by the Hermitian unit-norm biquaternion of the Introduction, $\tilde{\Lambda}^\dagger = \tilde{\Lambda}$, so the rotor conjugation is $\tilde{A}' = \tilde{\Lambda}\tilde{A}\tilde{\Lambda}^\dagger = \tilde{\Lambda}\tilde{A}\tilde{\Lambda}$. Write a general element of $\mathbb{M}_-$ as $\tilde{A} = ia\,e_0 + \mathbf{A}$ with $a$ real and $\mathbf{A}$ real, and split
$$
A_\parallel = \hat{\mathbf{u}}\cdot\mathbf{A},
\qquad
\mathbf{A}_\parallel = A_\parallel\hat{\mathbf{u}},
\qquad
\mathbf{A}_\perp = \mathbf{A} - \mathbf{A}_\parallel .
$$
Then
$$
a' = \gamma\left(a - \beta A_\parallel\right),
\qquad
A_\parallel' = \gamma\left(A_\parallel - \beta a\right),
\qquad
\mathbf{A}_\perp' = \mathbf{A}_\perp .
$$
Equivalently, in vector form,
$$
a' = \gamma\left(a - \frac{\mathbf{u}\cdot\mathbf{A}}{c}\right),
\qquad
\mathbf{A}' = \mathbf{A} + \frac{\gamma-1}{u^2}\left(\mathbf{u}\cdot\mathbf{A}\right)\mathbf{u} - \gamma\frac{a}{c}\,\mathbf{u} .
$$
For the four-potential ($a = \phi/c$, $\mathbf{A}$ the vector potential) these are precisely the component formulas that the parent *The Lorentz Transformation as a Biquaternionic Rotation* verifies against the rotor conjugation. The same rotor acts on every element of $\mathbb{M}_-$ — the parent states this for the four-position, four-velocity, four-momentum, four-force, four-potential, and four-current — so the component action holds for any four-vector, and in particular for the four-wavevector.

The scalar component is easily checked directly. Because $\mathrm{Sc}$ is cyclic,
$$
\mathrm{Sc}(\tilde{A}') = \mathrm{Sc}\!\left(\tilde{\Lambda}\tilde{A}\tilde{\Lambda}\right) = \mathrm{Sc}\!\left(\tilde{A}\tilde{\Lambda}^2\right),
$$
and $\tilde{\Lambda}^2 = \cosh\psi + i\sinh\psi\,\hat{\mathbf{u}} = \gamma + i\gamma\beta\hat{\mathbf{u}}$. Hence
$$
\mathrm{Sc}\!\left((ia + \mathbf{A})(\gamma + i\gamma\beta\hat{\mathbf{u}})\right)
= i\gamma a + i\gamma\beta\,\mathrm{Sc}\!\left(\mathbf{A}\hat{\mathbf{u}}\right)
= i\gamma a - i\gamma\beta A_\parallel
= i\gamma\left(a - \beta A_\parallel\right),
$$
since the scalar part of $\mathbf{A}\hat{\mathbf{u}}$ is $-\mathbf{A}\cdot\hat{\mathbf{u}} = -A_\parallel$. This is the first of the component equations; the remaining two are obtained from the same multiplication and reproduce the standard Lorentz boost.

**Solution (b).** Apply the component action with $a = \omega_0/c$ and $\mathbf{A} = \mathbf{k}_0 = (\omega_0/c)\hat{\mathbf{k}}_0$. With $A_\parallel = (\omega_0/c)\cos\theta$,
$$
\frac{\omega'}{c} = \gamma\left(\frac{\omega_0}{c} - \beta\frac{\omega_0}{c}\cos\theta\right)
\quad\Longrightarrow\quad
\boxed{\;\omega' = \gamma\,\omega_0\left(1 - \beta\cos\theta\right)\;}
$$
and
$$
k_\parallel' = \gamma\left(\frac{\omega_0}{c}\cos\theta - \beta\frac{\omega_0}{c}\right)
= \frac{\omega_0}{c}\,\gamma\left(\cos\theta - \beta\right),
\qquad
\mathbf{k}_\perp' = \frac{\omega_0}{c}\,\hat{\mathbf{k}}_{0\perp} .
$$
In the longitudinal case $\theta = 0$ or $\pi$ the transverse part vanishes; in general a ray that is transverse in one frame acquires a longitudinal component in the other, which is the aberration of Problem 5.

**Solution (c).** The norm form is preserved because $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$:
$$
N(\tilde{K}') = \tilde{\Lambda}\tilde{K}\tilde{\Lambda}^\dagger\overline{\tilde{\Lambda}\tilde{K}\tilde{\Lambda}^\dagger}
= \tilde{K}\bar{\tilde{K}} = 0 .
$$
One may also check it in components, using $\gamma^2(\cos\theta-\beta)^2 + \sin^2\theta = \gamma^2(1-\beta\cos\theta)^2$, which follows from $1-\beta^2 = \gamma^{-2}$. Hence $k' = \omega'/c$: the observer sees a light wave propagating with the same local speed $c$, as required.

**Solution (d).** The observer's four-velocity in the source frame is $\tilde{U} = \gamma(ic\,e_0 + \mathbf{u})$, and Problem 1 gives
$$
-\,\mathrm{Sc}\!\left(\tilde{K}\bar{\tilde{U}}\right)
= \gamma\,\omega_0\left(1 - \beta\cos\theta\right) = \omega' ,
$$
in agreement with (b).

> **Remark on the boost-direction convention.** The rotor with vector part $+\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ carries the frame in which the four-vector components are given *to the frame moving with velocity $+\mathbf{u}$* relative to it. This is fixed by the parent's verification against the four-potential components, and it is the convention used throughout. Reversing it — using the inverse rotor $\bar{\tilde{\Lambda}} = \cosh\frac{\psi}{2} - i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ in place of $\tilde{\Lambda}$ — interchanges emission and reception: it flips the sign of the Doppler term, giving $\omega' = \gamma\omega_0(1+\beta\cos\theta)$ in place of $\omega' = \gamma\omega_0(1-\beta\cos\theta)$, so that a receding observer ($\theta = 0$) is blueshifted rather than redshifted. Reversing the rotor therefore turns every receding observer into an approaching one. A sibling exercise in this series has found a parent article applying a boost rotor in the inverse direction in exactly this way; the present exercise pins the direction down before using it.

## Problem 3: Longitudinal Doppler — The Two Factors

**Statement.** (a) Derive the observed frequency for $\theta = 0$ and $\theta = \pi$. (b) Show that the two factors are reciprocals. (c) Express the result as a redshift.

**Solution (a).** For $\theta = 0$ (the observer recedes along the propagation direction),
$$
\omega' = \gamma\omega_0(1-\beta) = \omega_0\sqrt{\frac{1-\beta}{1+\beta}} ,
$$
using $\gamma(1-\beta) = \frac{1-\beta}{\sqrt{1-\beta^2}} = \sqrt{(1-\beta)/(1+\beta)}$. For $\theta = \pi$ (the observer approaches),
$$
\omega' = \gamma\omega_0(1+\beta) = \omega_0\sqrt{\frac{1+\beta}{1-\beta}} .
$$

**Solution (b).** The product is
$$
\omega'(\theta=0)\;\omega'(\theta=\pi) = \gamma^2\omega_0^2(1-\beta)(1+\beta) = \gamma^2\omega_0^2\left(1-\beta^2\right) = \omega_0^2 .
$$
This is required by symmetry: the configuration with velocity $-\mathbf{u}$ is the same physical situation with emission and reception interchanged, or equivalently it is the $\theta\to\pi$ configuration of the original, so the two factors must be inverse.

**Solution (c).** Since $\lambda = 2\pi c/\omega$, the observed wavelength for a receding observer is
$$
\lambda' = \lambda_0\sqrt{\frac{1+\beta}{1-\beta}} ,
$$
and the redshift $z := (\lambda'-\lambda_0)/\lambda_0$ is
$$
1 + z = \sqrt{\frac{1+\beta}{1-\beta}} ,
\qquad
\beta = \frac{(1+z)^2 - 1}{(1+z)^2 + 1} .
$$
There is no transverse term here: the longitudinal result is exact at every $\beta$ and involves only the line-of-sight component of the relative velocity.

## Problem 4: Transverse Doppler — Two Distinct Effects

**Statement.** (a) Case A: the observer's velocity is perpendicular to the ray *in the source frame*, $\theta = \pi/2$. Show that $\omega' = \gamma\omega_0$. (b) Case B: the source's velocity is perpendicular to the line of sight *in the observer frame*, $\theta' = \pi/2$. Show that this corresponds to $\cos\theta = \beta$ in the source frame, and that $\omega' = \omega_0/\gamma$. (c) Show that the two results differ by $\gamma^2$ and explain why there is no contradiction.

**Solution (a).** With $\cos\theta = 0$, the general formula gives
$$
\omega'_A = \gamma\,\omega_0 .
$$
The observer's motion is transverse in the source frame, yet the received light is **blueshifted** by the Lorentz factor. The reason is aberration: a ray transverse in the source frame arrives from a direction tilted toward the observer's motion, so the observer is moving toward the source along the line of sight. Explicitly, the transformed wavevector has $k_\parallel' = -\,(\omega_0/c)\gamma\beta$, so in the observer frame $\cos\theta' = k_\parallel'/k' = -\beta < 0$ (Problem 5).

**Solution (b).** From the transformed wavevector,
$$
\cos\theta' = \frac{k_\parallel'}{k'} = \frac{\gamma(\omega_0/c)(\cos\theta-\beta)}{\gamma(\omega_0/c)(1-\beta\cos\theta)} = \frac{\cos\theta-\beta}{1-\beta\cos\theta} ,
$$
which is the aberration formula of Problem 5. The condition $\cos\theta' = 0$ is therefore $\cos\theta = \beta$, i.e. the source-frame ray is emitted into the forward cone at angle $\arccos\beta$ from the observer's velocity. Then
$$
\omega'_B = \gamma\,\omega_0\left(1 - \beta\cdot\beta\right) = \gamma\,\omega_0\left(1-\beta^2\right) = \frac{\omega_0}{\gamma} .
$$
The received light is **redshifted** by the Lorentz factor $\gamma$. This is the classic transverse Doppler effect: a source moving transversely, as seen by the observer, has its radiation time-dilated, and the transverse frequency is reduced by exactly the time-dilation factor.

**Solution (c).** The two transverse shifts are
$$
\omega'_A = \gamma\omega_0 ,
\qquad
\omega'_B = \frac{\omega_0}{\gamma} ,
\qquad
\frac{\omega'_A}{\omega'_B} = \gamma^2 .
$$
There is no contradiction because the word "transverse" refers to two different conditions in two different frames. In case A the relative velocity is perpendicular to the ray **in the source frame**; aberration then makes the source appear ahead along the line of sight, and the observer is moving toward it, so the frequency rises. In case B the transversality is imposed **in the observer frame**, so the observer sees no component of the source's velocity along the line of sight, and the only surviving effect is the time dilation of the source, which lowers the frequency by exactly $1/\gamma$; the condition $\theta' = \pi/2$ corresponds by aberration to emission at $\theta = \arccos\beta$ in the source frame. The two cases coincide only in the limit $\beta\to0$, where both reduce to $\omega_0(1 + O(\beta^2))$ with opposite signs of the $O(\beta^2)$ term. In particular:
$$
\omega'_A = \omega_0\left(1 + \tfrac12\beta^2 + O(\beta^4)\right),
\qquad
\omega'_B = \omega_0\left(1 - \tfrac12\beta^2 + O(\beta^4)\right).
$$
The phrase "the transverse Doppler effect" without a stated frame is therefore ambiguous; this exercise reports both cases rather than choosing one. The second-order term $\pm\tfrac12\beta^2$ is the effect measured in the Ives–Stilwell experiment (Problem 6), which realises case B.

## Problem 5: Aberration and the Forward Cone

**Statement.** (a) Derive the aberration formulas
$$
\cos\theta' = \frac{\cos\theta-\beta}{1-\beta\cos\theta},
\qquad
\sin\theta' = \frac{\sin\theta}{\gamma\left(1-\beta\cos\theta\right)} .
$$
(b) Show that the source-frame hemisphere $\theta \ge \pi/2$ — the one containing the direction opposite the observer's velocity, which is the source's direction of motion in the observer frame — maps into an observer-frame cone of half-angle $\arccos\beta$ about that forward direction. (c) Evaluate the half-angle for $\beta = 0.5, 0.9, 0.99$ and compare with $1/\gamma$.

**Solution (a).** The two formulas are the ratios $k_\parallel'/k'$ and $k_\perp'/k'$ computed in Problem 2(b). The second follows from $k_\perp' = k_\perp$ and $k' = \omega'/c = (\omega_0/c)\gamma(1-\beta\cos\theta)$. As a check, $\cos^2\theta' + \sin^2\theta' = 1$ for every $\theta$, which is just the identity used in Problem 2(c).

**Solution (b).** At $\theta = \pi/2$, $\cos\theta' = -\beta$. The source's direction of motion as seen in the observer frame is $-\hat{\mathbf{u}}$, so the angle of the received ray from the forward direction is $\pi - \theta'$, with
$$
\cos(\pi-\theta') = \beta ,
\qquad
\pi - \theta' = \arccos\beta .
$$
Since the emission is isotropic in the source frame, the hemisphere $\theta\ge\pi/2$ — half the emitted light, and the half that contains the forward direction $-\hat{\mathbf{u}}$ — arrives within the cone of half-angle $\arccos\beta$ about that forward direction. This is the relativistic beaming (headlight) effect. For $\beta\to1$, $\arccos\beta\approx\sqrt{2(1-\beta)}\approx1/\gamma$, the familiar forward cone of half-angle $1/\gamma$.

**Solution (c).** The half-angles are $60.00^\circ$ ($\beta=0.5$), $25.84^\circ$ ($\beta=0.9$), and $8.11^\circ$ ($\beta=0.99$); the corresponding values of $1/\gamma$ are $49.62^\circ$, $24.97^\circ$, and $8.08^\circ$. The approximation $\arccos\beta\approx1/\gamma$ is poor at $\beta=0.5$ but already accurate to a few per cent at $\beta=0.9$, and to a fraction of a per cent at $\beta=0.99$, as it must be since the two agree to leading order in $1/\gamma$. The forward cone is the same cone that sets the beaming of synchrotron radiation and the angular concentration of radiated energy by a fast charge.

## Problem 6: Numerical Instance and the Non-Relativistic Limit

**Statement.** (a) For a spectral line of rest wavelength $\lambda_0 = 656.281$ nm (H$\alpha$) and $\beta = 0.10$, tabulate the observed wavelength in the four configurations of Problems 3 and 4. (b) For $\beta = 0.05$, give the Ives–Stilwell fractional shift and compare $1-1/\gamma$ with $\beta^2/2$. (c) Expand the general formula for $\beta\ll1$ and identify the classical and the second-order terms.

**Solution (a).** With $\nu_0 = c_0/\lambda_0 = 4.568050\times10^{14}$ Hz and $\beta = 0.10$ (so $\gamma = 1.0050378$), $\lambda' = \lambda_0\,\nu_0/\nu'$:

| Configuration | $\nu'/\nu_0$ | $\lambda'$ (nm) | Shift (nm) |
|---|---|---|---|
| Receding, $\theta = 0$ | $0.9045340337$ | $725.545945$ | $+\,69.264945$ |
| Approaching, $\theta = \pi$ | $1.1055415968$ | $593.628500$ | $-\,62.652500$ |
| Transverse A, $\theta = \pi/2$ (source frame) | $1.0050378153$ | $652.991350$ | $-\,3.289650$ |
| Transverse B, $\theta' = \pi/2$ (observer frame) | $0.9949874371$ | $659.587222$ | $+\,3.306222$ |

The two transverse frequency ratios differ by $\gamma^2 = 1.0101$: their ratio is $\gamma^2$, so the two frequency shifts have opposite signs and unequal magnitudes. The longitudinal entries are the two reciprocal shifts of Problem 3. As a stronger instance, at $\beta = 0.5$ the receding wavelength is $1136.712$ nm and the approaching one is $378.904$ nm.

**Solution (b).** For a circular source observed from the centre of its orbit — the Ives–Stilwell geometry — the emission is perpendicular to the line of sight in the observer frame at every instant, so case B applies and
$$
\frac{\nu'}{\nu_0} = \frac{1}{\gamma} = \sqrt{1-\beta^2} .
$$
At $\beta = 0.05$, $1 - 1/\gamma = 1.250782\times10^{-3}$, against the leading approximation $\beta^2/2 = 1.250000\times10^{-3}$: the exact transverse shift is $0.063\%$ larger than the leading term, the correction being the $\beta^4/8$ term of the expansion. In the Ives–Stilwell experiment the shift is measured as a displacement of spectral lines, and this is the "second-order Doppler shift".

**Solution (c).** Expand
$$
\omega' = \omega_0\,\gamma\left(1-\beta\cos\theta\right)
= \omega_0\left(1 + \tfrac12\beta^2 + \tfrac38\beta^4 + \cdots\right)\left(1-\beta\cos\theta\right),
$$
so
$$
\omega' = \omega_0\left(1 - \beta\cos\theta + \tfrac12\beta^2 - \tfrac12\beta^3\cos\theta + O(\beta^4)\right).
$$
The first-order term $-\beta\cos\theta$ is the classical Doppler shift. The leading transverse effect is $O(\beta^2)$ and is absent from the classical (first-order) formula; its sign depends on which transverse case is meant, $+\tfrac12\beta^2$ for case A and $-\tfrac12\beta^2$ for case B. At $\beta = 0.10$ the case-A shift is $\gamma - 1 = 0.0050378$, against $\tfrac12\beta^2 = 0.0050000$, an error of $0.76\%$ in the leading approximation. The limit requires $\beta\ll1$; for the relativistic sources for which beaming and aberration matter, the expansion is useless and the exact factors of Problems 3 and 4 must be used.

## Further Problems

The following are left to the reader; none is fully worked out above, and the last four are applications that the parents do not treat.

1. **The invariant formula for arbitrary direction.** Verify $\omega_{\mathrm{obs}} = -\mathrm{Sc}(\tilde{K}\bar{\tilde{U}})$ directly for $\theta$ chosen so that $\cos\theta = \beta$, and show that it reproduces $\omega_0/\gamma$. Then verify it is invariant under a second boost applied to both $\tilde{K}$ and $\tilde{U}$.

2. **Closest approach and the retarded time.** A source moves uniformly with velocity $u\hat{\mathbf{x}}$ past an observer at the origin, at impact parameter $b$. The light received at the moment the source is at the point of closest approach was emitted earlier, from a retarded position; the light emitted from the point of closest approach is received later. Show that the two reception conventions give the two transverse results: the light received when the source is at the point of closest approach is *blueshifted* by $\omega' = \gamma\omega_0$ (case A), while the light showing the source at its apparent closest position is *redshifted* by $\omega' = \omega_0/\gamma$ (case B). This is the retarded-time resolution of the apparent paradox of Problem 4(c), and it is the reason the Ives–Stilwell source is placed on a circle rather than in linear motion.

3. **Dispersion.** In a medium with frequency-dependent $c(\omega) = 1/\sqrt{\epsilon(\omega)\mu(\omega)}$, the null condition $N(\tilde{K}) = 0$ uses the phase speed at the received frequency, and the boost of Problem 2 changes the frequency. Does the transformation remain internally consistent when the medium is dispersive, and does it matter whether the medium is at rest in the source frame or in the observer frame? The parents take the complex structure to be local but do not combine it with a moving dispersive medium; this is open here.

4. **Apparent superluminal motion.** Show that a source moving at small angle $\Theta$ to the line of sight — $\Theta$ the angle between the source velocity and the direction from the source to the observer, the same line-of-sight angle as in further problem 5 — has apparent transverse speed
$$
v_{\mathrm{app}} = \frac{\beta c\sin\Theta}{1-\beta\cos\Theta} ,
$$
and find the angle that maximises it. (For $\beta = 0.99$ and $\Theta = 0.1$ rad this gives $v_{\mathrm{app}} = 6.61\,c$.)

5. **The CMB dipole.** An observer moving with velocity $\mathbf{u}$ through an isotropic blackbody of temperature $T$ sees, in the direction making angle $\Theta$ with $\mathbf{u}$ (the angle to the line of sight, not to the propagation direction), a blackbody of temperature $T' = T\,/\left[\gamma(1-\beta\cos\Theta)\right]$. Expand for small $\beta$ and identify the dipole and quadrupole terms. Why is the observed CMB dipole usually attributed to the observer's motion rather than to a property of the source? (Note that at $\Theta = \pi/2$ this is the case-B redshift $T' = T/\gamma$; the apparently conflicting statement that a ray perpendicular to the motion in the *source* frame is blueshifted refers to the source-frame propagation angle, which aberration relates to $\Theta$.)

6. **Relativistic redshift inversion.** For a purely receding source, invert $1+z = \sqrt{(1+\beta)/(1-\beta)}$ to obtain $\beta$ as a function of $z$, and check that for small $z$ one recovers the classical $\beta\simeq z$.

## Summary

1. **Four-wavevector.** $\tilde{K} = i\omega/c\,e_0 + \mathbf{k}$ is an element of $\mathbb{M}_-$ with $N(\tilde{K}) = -\omega^2/c^2 + k^2$; for light $k = \omega/c$ and $N(\tilde{K}) = 0$, so light is a null element (zero divisor) of the algebra. The phase $\Phi = \mathrm{Sc}(\tilde{K}\bar{\tilde{X}}) = \mathbf{k}\cdot\mathbf{x}-\omega t$ is invariant under rotor conjugation.

2. **Frequency invariant.** An observer of four-velocity $\tilde{U}$ measures $\omega_{\mathrm{obs}} = -\mathrm{Sc}(\tilde{K}\bar{\tilde{U}})$; in the source frame this is $\gamma\omega_0(1-\beta\cos\theta)$.

3. **General Doppler formula.** Under the boost rotor $\tilde{\Lambda} = \cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$, with $\tanh\psi = u/c$, the four-wavevector transforms by $\tilde{K}' = \tilde{\Lambda}\tilde{K}\tilde{\Lambda}^\dagger$ and $\omega' = \gamma\omega_0(1-\beta\cos\theta)$, where $\theta$ is the source-frame angle between $\mathbf{u}$ and the propagation direction. The transformed wavevector is again null.

4. **Longitudinal.** $\omega' = \omega_0\sqrt{(1-\beta)/(1+\beta)}$ receding and $\omega_0\sqrt{(1+\beta)/(1-\beta)}$ approaching; the two factors are reciprocals, and $1+z = \sqrt{(1+\beta)/(1-\beta)}$.

5. **Transverse — two cases.** $\theta = \pi/2$ in the source frame gives $\omega' = \gamma\omega_0$ (blueshift); $\theta' = \pi/2$ in the observer frame, corresponding to $\cos\theta = \beta$, gives $\omega' = \omega_0/\gamma$ (redshift). The two differ by $\gamma^2$; only case B is the usual time-dilated transverse shift of the Ives–Stilwell type.

6. **Aberration and beaming.** $\cos\theta' = (\cos\theta-\beta)/(1-\beta\cos\theta)$; the source-frame hemisphere $\theta\ge\pi/2$ arrives in a forward cone of half-angle $\arccos\beta \approx 1/\gamma$.

7. **Numbers.** For H$\alpha$, $\lambda_0 = 656.281$ nm, $\beta = 0.10$: receding $725.546$ nm, approaching $593.629$ nm, transverse A $652.991$ nm, transverse B $659.587$ nm. The non-relativistic expansion is $\omega' = \omega_0(1-\beta\cos\theta+\tfrac12\beta^2+O(\beta^3))$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector): imaginary scalar, real vector |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector) |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathrm{Sc}$ | Scalar projection of a biquaternion |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $c$, $c_0$ | Speed of light in the medium, and in vacuum |
| $\tilde{X} = ict\,e_0 + \mathbf{x}$ | Four-position |
| $\tilde{K} = i\omega/c\,e_0 + \mathbf{k}$ | Four-wavevector, $N(\tilde{K}) = 0$ for light |
| $\tilde{U} = \gamma_u(ic\,e_0 + \mathbf{u})$ | Observer four-velocity, $N(\tilde{U}) = -c^2$ |
| $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ | Boost biquaternion (Hermitian, unit norm) |
| $\psi$ | Rapidity, $\tanh\psi = u/c$ |
| $\beta = u/c$, $\gamma = (1-\beta^2)^{-1/2}$ | Dimensionless speed and Lorentz factor |
| $\mathbf{u}$ | Observer-frame velocity relative to the source frame |
| $\hat{\mathbf{k}}_0$ | Source-frame propagation direction |
| $\theta$ | Source-frame angle between $\mathbf{u}$ and $\hat{\mathbf{k}}_0$ |
| $\theta'$ | Observer-frame angle between $\mathbf{u}$ and $\hat{\mathbf{k}}'$ |
| $\omega_0$, $\omega'$ | Source-frame and observer-frame angular frequency |
| $z = (\lambda'-\lambda_0)/\lambda_0$ | Redshift |

## Further Reading

- Albert Einstein, "Zur Elektrodynamik bewegter Körper," *Annalen der Physik* **17** (1905) 891–921, for the original derivation of the Doppler effect and the aberration of light.
- H. E. Ives and G. R. Stilwell, "An experimental study of the rate of a moving atomic clock," *Journal of the Optical Society of America* **28** (1938) 215–226, for the measurement of the transverse second-order shift.
- Christian Møller, *The Theory of Relativity* (Oxford, 1972), for the standard derivation of the Doppler effect and aberration from the Lorentz transformation.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the four-vector derivation of the Doppler effect and the beaming of radiation.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the Doppler effect, aberration, and relativistic beaming in electromagnetic problems.
- Hermann Bondi, *Relativity and Common Sense* (Doubleday, 1964), for the $k$-calculus derivation of the longitudinal Doppler factor.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), and Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the spacetime-algebra treatment of the wave four-vector and the Lorentz rotor.
- The companion articles of this series: *Relativistic Mechanics in Biquaternionic Form*, *The Lorentz Transformation as a Biquaternionic Rotation*, and *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*.
