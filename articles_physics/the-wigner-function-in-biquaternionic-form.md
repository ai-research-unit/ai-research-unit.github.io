# __The Wigner Function in Biquaternionic Form__

## Introduction

**The biquaternionic Wigner function is the standard $x$–$p$ Wigner transform of the field taken in the algebra, and its two marginal moments are the density and the current.** The definition is

$$
\tilde W_\Xi(r,\vec p)=\frac{1}{(2\pi\hbar)^{3}}\int d^{3}s\;e^{-i\vec p\cdot\vec s/\hbar}\;
\tilde\Xi^{*}\!\left(r-\frac{\vec s}{2}\right)\tilde\Xi\!\left(r+\frac{\vec s}{2}\right),
$$

an element of $\mathbb{B}$ at each point of the $(r,\vec p)$ space. Its zeroth moment in $\vec p$ is $\lVert\tilde\Xi\rVert^{2}=\rho_{\mathrm{num}}$, its first moment is the current density times the mass, and its $\hbar\to0$ limit is the phase-space density of the polar-form fluid on the mass shell.

**The article's claim is a claim about what is written in the letters, not about new physics.** The transform, its normalisation, its marginals, its negativity and its $\hbar$-expansion are all standard. What the corpus supplies is a definition in which the Wigner object is an element and not a matrix, and a reading of its two parts as the two quadratures of one angle. The article states both and is explicit about which is which.

**Where the standard function already lives in the corpus.** [The Bell Inequality for Continuous Variables in Biquaternionic Form](the-bell-inequality-for-continuous-variables-in-biquaternionic-form.html) uses the $x$–$p$ Wigner function of a two-mode squeezed state, in the normalisation in which one mode has $\int W\,d^{2}\alpha=\tfrac12$ and the vacuum is $\pi^{-1}\exp(-2\lvert\alpha\rvert^{2})$. That is the same function this article defines, in a phase-space variable $\alpha$ that absorbs the mass and the frequency; the corpus's normalisation there is the one in which $d^{2}\alpha=dq\,dp/2$ with $\hbar=1$. **This article keeps $\hbar$ explicit and uses the three-dimensional normalisation $\int d^{3}p\,\tilde W_\Xi=\rho_{\mathrm{num}}$**, which is the normalisation the fluid articles need. The relation between the two normalisations is a constant and is recorded in the notation table.

## The Standard Function, Stated First

### Definition and normalisation

**The Wigner function of a wave function is the Fourier transform of the density matrix in the relative coordinate.** For a complex-valued field $\Xi$ on $\mathbb{R}^{3}$ — the central case of the corpus's field, in which the vector part is zero —

$$
W(\vec r,\vec p)=\frac{1}{(2\pi\hbar)^{3}}\int d^{3}s\;e^{-i\vec p\cdot\vec s/\hbar}\,
\Xi^{*}\!\left(\vec r-\frac{\vec s}{2}\right)\Xi\!\left(\vec r+\frac{\vec s}{2}\right),
$$

and the conventions are worth stating because three of them are in circulation and they differ by signs and factors of two. This article takes:

- the relative coordinate $\vec s$ enters with a **half** offset, so that the two field arguments are symmetric about $\vec r$;
- the kernel is $e^{-i\vec p\cdot\vec s/\hbar}$ with the **momentum** $\vec p$ as the transform variable, so that a plane wave of momentum $\vec p_0$ is concentrated at $\vec p=\vec p_0$ and not at $-\vec p_0$;
- the conjugate field is the one at $\vec r-\vec s/2$, so that the ordering of the two arguments is fixed once and for all;
- the normalisation is $(2\pi\hbar)^{-3}$, so that $\int d^{3}p\,W=\Xi^{*}\Xi$ and $\int d^{3}r\,d^{3}p\,W=1$.

**The third and second conventions must be consistent, and the cost of getting them wrong is a sign in the momentum.** A definition that pairs $e^{-i\vec p\cdot\vec s/\hbar}$ with $\Xi^{*}(\vec r+\vec s/2)\Xi(\vec r-\vec s/2)$ is internally consistent but concentrates a plane wave of momentum $\vec p_0$ at $\vec p=-\vec p_0$; the error is invisible for a real wave function, which is exactly the case that cannot catch it. The check is the plane wave, and it is the first thing to run on any implementation. **This article's definition was checked this way**: with the convention above, a packet of mean momentum $p_0$ has its Wigner distribution centred at $p_0$, and the reverse convention puts it at $-p_0$.

### What it is, and what it is not

**The Wigner function is a real function that behaves like a phase-space density without being one.** Three facts, all standard:

1. **Its marginals are the density and the current.** Integrating over momentum gives the position density; integrating over position gives the momentum density; the first moment in momentum gives the current.
2. **It is not non-negative in general.** The ground state of an oscillator has a Gaussian Wigner function and is as positive as a distribution can be; a superposition of two levels has negative regions (Hudson's theorem: a pure state has a non-negative Wigner function if and only if it is Gaussian, and a mixed state if and only if it is a mixture of Gaussians).
3. **Its uncertainty is the quantum of phase-space area.** The second moment in momentum about the mean is $\hbar^{2}/(4\sigma^{2})$ for a Gaussian of position width $\sigma$, so the phase-space area it occupies is set by $\hbar$ and not by the state.

**The third fact is what makes it the right object for this category.** The fluid articles describe a quantum fluid by a density and a velocity, and the Wigner function is the object that says how far the fluid picture can be pushed: where the distribution is positive and narrow, a phase-space density exists and the fluid is classical; where it is negative or wide, the fluid picture is a description of the first two moments and nothing more. [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html) makes the same point from the stress, and the identity at the end of this article connects the two.

## The Biquaternionic Definition

### The definition

**The biquaternionic Wigner function is the same transform applied to the element, with the element's own conjugation.** Define

$$
\boxed{\;\tilde W_\Xi(r,\vec p)=\frac{1}{(2\pi\hbar)^{3}}\int d^{3}s\;e^{-i\vec p\cdot\vec s/\hbar}\;
\tilde\Xi^{*}\!\left(r-\frac{\vec s}{2}\right)\tilde\Xi\!\left(r+\frac{\vec s}{2}\right)\;}
$$

where $\tilde\Xi^{*}$ is the conjugate the polar-form article uses, and the product is the algebra's product and not a pointwise one. The result is an element of $\mathbb{B}$ for each $(r,\vec p)$, and the transform acts only on the coefficients: the algebra's multiplication is pointwise in $r$ and is untouched by the $s$-integration.

**Three properties follow immediately and they are the ones the article uses.**

- **The $s\to0$ point is the density.** At $\vec s=0$ the product is $\tilde\Xi^{*}(r)\tilde\Xi(r)=\lVert\tilde\Xi\rVert^{2}$, so the density is present in the definition before any integration.
- **The element is an element.** No matrix is introduced and no basis is chosen; the object is the product of two field values, and its decomposition into parts is the algebra's decomposition.
- **The definition is pointwise in the frame.** No derivative appears, so no frame choice and no metric enters. This is why the definition can be carried to the curved bookkeeping of [Curved-Spacetime KMS and Modular Flow](curved-spacetime-kms-and-modular-flow.html) without change, provided the relative coordinate $\vec s$ is taken along a geodesic and the offset is by half the proper length.

### Why this ordering, in these letters

**The ordering is fixed by the requirement that the momentum marginal reproduce the polar form's momentum.** The corpus writes the plane-wave phase as $\tilde\Xi\propto e^{iS_{\tilde\Xi}/\hbar}$ with $\vec\nabla_\Phi S_{\tilde\Xi}=\vec p$, because the derivative on the material sector is $\partial/\partial R_\eta=\partial/\partial r_\eta$ and $\vec\nabla_\Phi\tilde\Xi=(i/\hbar)\vec p\,\tilde\Xi$. So the combination whose $s$-dependence is $e^{+i\vec p\cdot\vec s/\hbar}$ is $\tilde\Xi^{*}(r-\vec s/2)\tilde\Xi(r+\vec s/2)$, and it is that combination that the kernel $e^{-i\vec p\cdot\vec s/\hbar}$ must multiply. Pairing the kernel with the other ordering puts the momentum at its negative, which is the sign error described above in its corpus form.

**The half-offset is fixed by the requirement that the first moment be the current and not twice it.** With the full offset, the transform reproduces the density after a rescaling but the first moment comes out with the wrong coefficient, and the wrong coefficient is a factor of two that no normalisation can repair. The half-offset is the standard choice and the corpus adopts it for the standard reason.

### Conjugation, and the two imaginary structures

**The definition uses the field's conjugate, and the corpus has two operations that a reader may take for one.** The polar-form article separates multiplication by the central $i$ from complex conjugation: the first translates the action by $\pi\hbar/2$ and preserves the mass-shell sheet, and the second reflects the action and exchanges the sheets. In the Wigner transform the conjugation is the second operation only — the complex conjugation of the coefficients — and the central $i$ is untouched, because the transform's kernel is complex and not quaternionic. So a reader who asks whether $\tilde W_\Xi$ is "the conjugate" of something should be told: it is the transform of the conjugate field, and the two conjugations of the corpus are not interchanged anywhere in this article.

**This matters for the reality of the marginal.** The zeroth moment is $\tilde\Xi^{*}\tilde\Xi$, which is the norm and is real and non-negative; there is no ambiguity. The first moment is a difference of two products and its reality depends on the ordering conventions, which is the subject of the next section.

## The Marginals Are Density and Current

### The zeroth moment

**Integrating the Wigner element over momentum gives the norm of the field.** The delta identity in the corpus's Fourier convention is

$$
\int d^{3}p\;e^{-i\vec p\cdot\vec s/\hbar}=(2\pi\hbar)^{3}\,\delta^{3}(\vec s),
$$

so that

$$
\int d^{3}p\;\tilde W_\Xi=\int d^{3}s\;\delta^{3}(\vec s)\,
\tilde\Xi^{*}\!\left(r-\frac{\vec s}{2}\right)\tilde\Xi\!\left(r+\frac{\vec s}{2}\right)
=\tilde\Xi^{*}(r)\tilde\Xi(r)=\lVert\tilde\Xi\rVert^{2}=\rho_{\mathrm{num}}(r).
$$

**The display is exact and needs no approximation.** The right-hand side is the amplitude squared, which the conventions write as $\lVert\tilde\Xi\rVert^{2}$ and never as a bare letter; it is real and non-negative by the definition of the norm, and it is the density the fluid articles call $\rho_{\mathrm{num}}$. So the momentum marginal of the Wigner element *is* the proper density, and a reader who wants the density of the fluid at an event can obtain it by integrating the Wigner element over momentum at that event.

**What the display does not say.** It does not say that the Wigner element is non-negative, so it does not say that a phase-space density exists. A positive marginal is compatible with a distribution that is negative somewhere, and the negativity is the subject of a later section. The marginal statement is the weakest of the properties and the one that survives unconditionally.

### The first moment, and the current

**The first moment of the Wigner element in momentum is the mass times the current density.** From $\int d^{3}p\,p_\eta\,e^{-i\vec p\cdot\vec s/\hbar}=i\hbar(2\pi\hbar)^{3}\partial_{\eta}\delta^{3}(\vec s)$ and one integration by parts,

$$
\int d^{3}p\;p_\eta\,\tilde W_\Xi
=\frac{\hbar}{2i}\left[\tilde\Xi^{*}\frac{\partial\tilde\Xi}{\partial r_\eta}
-\frac{\partial\tilde\Xi^{*}}{\partial r_\eta}\tilde\Xi\right].
$$

**The bracket is the polar form's momentum, in the corpus's letters.** The polar-form article proves the identity

$$
\tilde\Xi^{*}\frac{\partial\tilde\Xi}{\partial r_\eta}
-\tilde\Xi\frac{\partial\tilde\Xi^{*}}{\partial r_\eta}
=\frac{2i\lVert\tilde\Xi\rVert^{2}}{\hbar}\frac{\partial S_{\tilde\Xi}}{\partial r_\eta},
$$

so substituting and using $\partial S_{\tilde\Xi}/\partial r_\eta=p_\eta$,

$$
\mathrm{Sc}\int d^{3}p\;p_\eta\,\tilde W_\Xi
=\frac{\hbar}{2i}\cdot\frac{2i\lVert\tilde\Xi\rVert^{2}}{\hbar}\,p_\eta
=\lVert\tilde\Xi\rVert^{2}p_\eta=m\,j_\eta,
$$

with $j_\eta=\rho_{\mathrm{num}}p_\eta/m$ the current density of the polar-form article. **The scalar part is written because the two orderings of the quaternionic product differ by a commutator whose scalar part vanishes**, so the scalar part of the marginal is ordering-independent even where the element itself is not. This is the reason the identity is stated on $\mathrm{Sc}$ and not on the element: the current is a real vector and it is read from the scalar part.

**The two marginals together are the statement that the Wigner element reproduces the fluid's first two data.** Density from the zeroth moment, current from the first; the pressure needs the second moment, and the second moment is where the quantum potential enters.

### The temporal slot

**The temporal moment carries the factor $i$ that the element's temporal slot carries, and the statement is clean once the $i$ is put in the right place.** With $E=-c\,\partial S_{\tilde\Xi}/\partial r'_t$ and $\rho_{\mathrm{num}}=\lVert\tilde\Xi\rVert^{2}$,

$$
\int d^{3}p\;\frac{E}{c}\,\tilde W_\Xi=\frac{E}{c}\,\rho_{\mathrm{num}},
\qquad
J_{\Phi,t}=ic\gamma\rho_{\mathrm{num}}=\frac{iE}{mc^{2}}\,c\,\rho_{\mathrm{num}}=\frac{iE}{mc}\,\rho_{\mathrm{num}},
$$

where $\gamma=E/(mc^{2})$ is the polar-form article's boost factor, so that $mJ_{\Phi,t}=iE\rho_{\mathrm{num}}/c$ and the moment and the current's temporal slot differ by the factor $-i$. So

$$
\int d^{3}p\;\frac{E}{c}\,\tilde W_\Xi=-i\,m\,J_{\Phi,t},
$$

and the $-i$ is the element's own: the temporal slot of the current is imaginary because $v_{\Phi,t}=ic\gamma$, and the moment of the Wigner element is real because $E/c$ is real. Writing the two moments together,

$$
\int d^{3}p\;\left(\frac{E}{c},\,\vec p\right)\tilde W_\Xi
=m\left(-i\,J_{\Phi,t},\,\vec j\right),
$$

which is the four-current with the $i$ where the corpus's letters put it. A reader who wants a display with no $i$ should read it as two statements: the spatial moment is the current density times the mass, and the temporal moment is the same quantity with the temporal slot's $i$ restored.

### The check

**The marginals were checked numerically on a Gaussian packet, and the residuals are of the order of the grid error.** With $\hbar=1$, position width $\sigma=0.5$, mean position $x_0=0.3$ and mean momentum $p_0=1.7$, on a grid of $241$ positions, $301$ momenta and $2001$ relative coordinates spanning $\lvert s\rvert\le10$:

| quantity | value |
|---|---|
| $\max\bigl\lvert\int dp\,W-\Xi^{*}\Xi\bigr\rvert$ | $7.1\times10^{-7}$ |
| $\int dx\,dp\,W$ | $0.999\,999\,1$ |
| $\max\bigl\lvert\int dp\,p\,W-\Xi^{*}\Xi\,p_0\bigr\rvert$ | $4.0\times10^{-6}$ |
| $W(x_0,p_0)$ | $0.318\,309\,886\,183\,790\,7$ |
| $1/(\pi\hbar)$ | $0.318\,309\,886\,183\,790\,7$ |

The fourth and fifth rows are the exact value of a Gaussian's Wigner function at its centre, $1/(\pi\hbar)$, and the agreement is to the last digit a double can hold. **The peak value is the check that the normalisation is right**: an error of $\pi$ or of $2\pi$ in the normalisation moves it and nothing else in the table does.

## What the Element Carries

### The real part is the sum of the quadratures

**If the field is a fixed unit element times a complex coefficient, the real part of the Wigner element is the sum of the two quadratures' Wigner functions and the imaginary part is their antisymmetric cross term.** Write

$$
\tilde\Xi(r)=u\left(a(r)+i\,b(r)\right),
\qquad u^{*}u=1,
$$

with $a$ and $b$ real. Then $\tilde\Xi^{*}(r-\vec s/2)\tilde\Xi(r+\vec s/2)=\left(a_- -i b_-\right)\left(a_+ + i b_+\right)$ with the subscripts labelling the two offsets, so

$$
\tilde W_\Xi=\bigl(W[a]+W[b]\bigr)+i\bigl(W[a,b]-W[b,a]\bigr),
$$

where $W[a]$ is the Wigner transform of $a$ with itself and $W[a,b]$ the cross transform. **Both statements are exact**, and they are the content of the sentence that the algebra supplies a decomposition of the Wigner object into its two quadratures and their correlation. The real part is the total phase-space density of the pair of real fields; the imaginary part measures the local correlation of the two quadratures, and it vanishes for a field whose quadratures are uncorrelated at every scale.

**The polar form identifies the two quadratures.** The article on the polar form of the Klein–Gordon equation records that the material and informational parts of the element are the quadratures $\lVert\tilde\Xi\rVert\cos(S_{\tilde\Xi}/\hbar)$ and $\lVert\tilde\Xi\rVert\sin(S_{\tilde\Xi}/\hbar)$ of the one angle. Substituting,

$$
a=\lVert\tilde\Xi\rVert\cos\frac{S_{\tilde\Xi}}{\hbar},
\qquad
b=\lVert\tilde\Xi\rVert\sin\frac{S_{\tilde\Xi}}{\hbar},
\qquad
a^{2}+b^{2}=\lVert\tilde\Xi\rVert^{2}=\rho_{\mathrm{num}},
$$

so the two quadratures are the amplitude split by the phase into a cosine and a sine part, and their squares add to the density. **The real part of the Wigner element is therefore the phase-space image of the density, and the imaginary part is the phase-space image of the phase gradient's correlation** — which is the precise sense in which the algebra's two sectors appear in the Wigner picture.

### The rotating unit, and where the algebra goes beyond the complex number

**When the unit element varies from point to point the decomposition above is no longer the whole story, and that is where the algebra does more than a complex number.** The polar form writes the field with a rotor, $\tilde\Xi=\lVert\tilde\Xi\rVert\,\tilde U_{\mathrm{rot}}\,\xi$ in the notation of the spin-fluid article, and the rotor is an element and not a phase. In the Wigner transform the rotor appears twice, once conjugated at each offset, so the Wigner element carries $\tilde U_{\mathrm{rot}}^{*}(r-\vec s/2)\tilde U_{\mathrm{rot}}(r+\vec s/2)$, which for a slowly varying rotor is $1$ plus $\vec s\cdot(\text{rotor gradient})$ plus corrections. Two consequences:

- **A constant rotor cancels**, so a uniformly spinning field has the same Wigner function as a spinless one with the same density and phase. This is the Wigner-picture statement that a global spin rotation is not observable in the scalar marginals.
- **A varying rotor does not cancel**, so rotor gradients appear in the Wigner element at first order in $\vec s$ — that is, in the imaginary part, which is the part the first moment reads. The spin-fluid article's statement that the vorticity is sourced by rotor gradients is the same fact in the hydrodynamic variables.

**The Dirac case is where this becomes structural, and this article does not construct it.** The relativistic Wigner function of a spin-$\tfrac12$ field is a $4\times4$ matrix-valued distribution, and the matrix structure exists to carry the spin: the sixteen independent entries are the scalar, vector, tensor, axial and pseudoscalar components. In the biquaternion framework the corresponding object is an element whose two-sided action carries the rotor, and the claim that the two are equivalent is a claim about the algebra's representation theory that [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html) makes in the hydrodynamic language. **Constructing the Dirac Wigner element and proving the equivalence is not done here**, and the omission is recorded in the status section rather than smoothed over.

## The Classical Limit Is the Fluid

### The limit, in one line

**In the limit in which the phase varies slowly the Wigner element collapses onto the mass shell and becomes the fluid's phase-space density.** Write the field in the polar form's variables, $\tilde\Xi=\lVert\tilde\Xi\rVert\,e^{iS_{\tilde\Xi}/\hbar}u$ with $u$ a fixed unit element, and expand the two offsets to first order:

$$
\tilde\Xi^{*}\!\left(r-\frac{\vec s}{2}\right)\tilde\Xi\!\left(r+\frac{\vec s}{2}\right)
=\rho_{\mathrm{num}}(r)\,e^{i\,\vec s\cdot\vec\nabla_\Phi S_{\tilde\Xi}/\hbar}
\left(1+\mathcal{O}(s^{2})\right),
$$

where the amplitude's two offsets combine to $\rho_{\mathrm{num}}$ to this order because the correction is a derivative of a symmetric combination. Substituting,

$$
\tilde W_\Xi\;\longrightarrow\;\rho_{\mathrm{num}}(r)\,\delta^{3}\!\left(\vec p-\vec\nabla_\Phi S_{\tilde\Xi}\right)
\qquad\left(\hbar\to0\ \text{at fixed}\ r,\ \vec p\right),
$$

which is the statement that the fluid's phase-space density is supported on the momentum the flow carries. **The support is the mass shell** — the flow momentum is $\vec p=\vec\nabla_\Phi S_{\tilde\Xi}$ and the energy is fixed by the mass-shell relation of the polar-form article — so the classical limit of the Wigner element is a shell-supported density and not a diffuse one.

**Two things the limit says.** First, the fluid picture is the $\hbar\to0$ limit of the Wigner picture and not an independent description: density and velocity are the two moments of a distribution, and the limit is what makes the higher moments disappear. Second, the limit is a *limit*, and the parameter that controls the correction is the width of the distribution divided by the scale on which the potential varies — which is what the next two subsections measure.

### The width is the quantum, and it is the quantum potential

**The second moment of the Wigner element about the flow momentum is the phase-space area the state occupies, and for a Gaussian it is exactly the quantum potential.** With $\sigma$ the position width of a normalized Gaussian and $\hbar$ the action quantum,

$$
\mathrm{Var}(p)=\frac{\hbar^{2}}{4\sigma^{2}},
\qquad
Q_{\mathrm{qnt}}(r_0)=-\frac{\hbar^{2}}{2m}\frac{\Box_\Phi\lVert\tilde\Xi\rVert}{\lVert\tilde\Xi\rVert}\bigg|_{r_0}
=\frac{\hbar^{2}}{4m\sigma^{2}},
$$

at the centre $r_0$ of a packet at rest, where the box is the spatial Laplacian in that frame and the variance is taken along one direction. **The two are equal up to the mass**: $Q_{\mathrm{qnt}}(r_0)=\mathrm{Var}(p)/m$.

**One clause about the dimension, because the box and the variance must be counted the same way.** The display is one-dimensional. In three dimensions the Laplacian contributes one such term per direction, so the ratio at the centre is $-3/(2\sigma^{2})$ and the identity reads $Q_{\mathrm{qnt}}(r_0)=\mathrm{Var}_{\mathrm{tr}}(p)/m$, where $\mathrm{Var}_{\mathrm{tr}}(p)=\sum_{\eta}\mathrm{Var}(p_\eta)$ is the trace of the momentum covariance and not the variance along one axis. **Per component the three-dimensional identity carries a factor of three**, and a reader who compares a one-dimensional formula with a three-dimensional simulation will find exactly that factor and no other. The computation is one line: for $\lVert\tilde\Xi\rVert\propto e^{-(r-r_0)^{2}/(4\sigma^{2})}$ the ratio $\Box_\Phi\lVert\tilde\Xi\rVert/\lVert\tilde\Xi\rVert$ at the centre is $-1/(2\sigma^{2})$, and the minus signs of the quantum potential and of the second derivative cancel.

**The identity is the bridge to the stress.** The quantum potential is the term that modifies the mass shell in the corpus's polar form,

$$
\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2m\,Q_{\mathrm{qnt}},
$$

and the variance is the spread of the Wigner distribution about the flow momentum. So the modification of the shell by the quantum potential is the statement that the fluid's momentum is the *mean* of a distribution whose width is not zero, and the amount by which the mean sits off the classical shell is set by that width. [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html) reaches the same term from the stress and states that it is not a thermal pressure; the identification here is the phase-space statement of that sentence.

**The identity is exact for the Gaussian only.** For a general state the second moment about the flow momentum is not the quantum potential: the general relation involves the density's third derivatives as well, and the Gaussian is the family in which they vanish. This article states the Gaussian identity, uses it to fix the interpretation, and does not generalise it. The general $\hbar^{2}$ expansion of the Wigner element is [Relativistic Wigner Function and Quantum Kinetics](relativistic-wigner-function-and-quantum-kinetics.html)'s subject, and it is there that the higher terms appear.

### The numbers

**Both statements were checked numerically on the Gaussian used for the marginal table.** With $\hbar=1$, $\sigma=0.5$ and $m=1$:

| quantity | value |
|---|---|
| $\mathrm{Var}(p)$ from the Wigner distribution | $0.999\,978\,2$ |
| $\hbar^{2}/(4\sigma^{2})$ | $1$ |
| $Q_{\mathrm{qnt}}$ at the centre, from finite differences | $0.997\,781\,1$ |
| $\mathrm{Var}(p)/m$ | $0.999\,978\,2$ |

The two numerical values agree to about $2\times10^{-3}$, which is the accuracy of a second difference on a grid of spacing $0.033$; the two exact values agree identically, since both are $\hbar^{2}/(4\sigma^{2})$ with $m=1$. **The agreement is the check that the Wigner normalisation and the quantum potential's sign are consistent**: a plus sign on the quantum potential would give $-1$ in the third row, and the discrepancy would be visible at once.

### Negativity, and what it forbids

**The Wigner element of a non-Gaussian pure state is negative somewhere, and the negativity is the precise sense in which the fluid picture is incomplete.** For the superposition $(\lvert0\rangle+\lvert1\rangle)/\sqrt2$ of the first two oscillator levels, in units with $\hbar=m=\omega=1$:

| quantity | value |
|---|---|
| minimum of $W$ on the sampled grid | $-0.113\,359\,879\,579\,893\,8$ |
| fraction of the sampled grid with $W<0$ | $1.89\%$ |
| $\int dx\,dp\,W$ | $0.999\,400$ |

**The consequence for the fluid articles is that no equation of state can be exact.** A phase-space density is non-negative by definition; the Wigner element is not; so the fluid description is a projection of the Wigner description onto its first moments, and the projected-out part is not zero. The articles that follow use the projection and say where it fails: [Relativistic Wigner Function and Quantum Kinetics](relativistic-wigner-function-and-quantum-kinetics.html) for the expansion that organises the failure, and [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html) for what the pressure does with it.

## What the Algebra Supplies and What It Imports

**The accounting is a table, because the temptation to overstate the algebra's role is strongest in a definition section.**

| Imported unchanged | Supplied by the algebra |
|---|---|
| The Wigner transform and its normalisation | The object is an element, with no matrix and no basis |
| The half-offset and the relative coordinate | The conjugate is the algebra's, not an external star |
| The marginals as density and current | The quadratures are the material and informational parts |
| Hudson's theorem and the negativity | The rotor, which a complex number cannot carry |
| The width $\hbar/(2\sigma)$ of a minimum packet | The decomposition $\tilde W_\Xi=\bigl(W[a]+W[b]\bigr)+i\bigl(W[a,b]-W[b,a]\bigr)$ |
| The $\hbar$-expansion and the kinetic equation | The reading of the two parts as the two sectors of one angle |

**The two columns are not equally heavy, and the article says which is which.** The left column is the physics and it is entirely standard. The right column is a set of spellings and one genuine addition — the rotor — and even the rotor is an addition of *representation*: the standard treatment carries the same information in a matrix, and the corpus's claim is that the element is the natural carrier, not that a matrix cannot carry it. A reader who wants new predictions will not find them in this article, and the next section says so in the house's own terms.

**One awkwardness the algebra produces, recorded rather than hidden.** The product $\tilde\Xi^{*}(r-\vec s/2)\tilde\Xi(r+\vec s/2)$ is quaternionic, so its "real part" is not one real function but the coefficients of the element. The decomposition into $W[a]+W[b]$ and the cross term is the decomposition in a *fixed* unit element, and for a field whose unit element turns it is basis-dependent. The invariant objects are the scalar part and the norm, and those are what the marginals use: the zeroth moment is a norm and the first moment is a scalar part. A reader who wants an invariant two-function decomposition of a rotating field will not get it here, and the reason is structural.

## What Is Established and What Is Interpretation

**Established.** The definition of the biquaternionic Wigner element, and its reduction to the standard transform in the fixed-unit case. The zeroth and first moments as density and current, the first stated on the scalar part and justified by the vanishing of the commutator's scalar part. The temporal moment with the element's $i$ restored. The quadrature decomposition, exact in the fixed-unit case. The classical limit $\rho_{\mathrm{num}}\delta^{3}(\vec p-\vec\nabla_\Phi S_{\tilde\Xi})$ to leading order in the offset. The Gaussian identity $Q_{\mathrm{qnt}}(r_0)=\mathrm{Var}(p)/m$. The numerical checks: marginal residuals $7.1\times10^{-7}$ and $4.0\times10^{-6}$, the peak value $1/(\pi\hbar)$ to the last digit a double holds, $\mathrm{Var}(p)=0.999\,978\,2$ against $\hbar^{2}/(4\sigma^{2})=1$, $Q_{\mathrm{qnt}}(r_0)=0.997\,781\,1$, and the negativity minimum $-0.113\,359\,879\,579\,893\,8$ with $1.89\%$ of the grid negative.

**Interpretation.** That the Wigner element is the object that mediates between the quantum state and the fluid, and that the fluid description is the $\hbar\to0$ projection of it. Both are standard readings; the article's contribution is the letters in which they are written and the explicit separation of what is imported from what is supplied.

**Not claimed.** That the Wigner element is non-negative — it is not, and the negativity is quantified above. That the quadrature decomposition is basis-independent — it is not, and the invariant objects are named. That the Gaussian identity for the quantum potential holds for general states — it does not. That the Dirac Wigner element has been constructed in these letters — it has not, and the standard matrix statement is cited rather than reproduced.

## Summary

The biquaternionic Wigner function is the standard $x$–$p$ transform of the field taken in the algebra, $\tilde W_\Xi(r,\vec p)=(2\pi\hbar)^{-3}\int d^{3}s\,e^{-i\vec p\cdot\vec s/\hbar}\tilde\Xi^{*}(r-\vec s/2)\tilde\Xi(r+\vec s/2)$, with the conjugate at the lower offset and the momentum kernel of the corpus's Fourier convention. Both choices are fixed by the requirement that a plane wave of momentum $\vec p_0$ sit at $\vec p=\vec p_0$, which is the check that catches the sign error a real wave function cannot catch.

Its zeroth moment in momentum is the norm, $\int d^{3}p\,\tilde W_\Xi=\lVert\tilde\Xi\rVert^{2}=\rho_{\mathrm{num}}$, exactly. Its first moment is the mass times the current,

$$
\mathrm{Sc}\int d^{3}p\;p_\eta\,\tilde W_\Xi
=\frac{\hbar}{2i}\left[\tilde\Xi^{*}\frac{\partial\tilde\Xi}{\partial r_\eta}-\frac{\partial\tilde\Xi^{*}}{\partial r_\eta}\tilde\Xi\right]
=\lVert\tilde\Xi\rVert^{2}p_\eta=m\,j_\eta,
$$

by the polar form's identity for the bracket; the scalar part is taken because the two orderings differ by a commutator whose scalar part vanishes. Its temporal moment is $\int d^{3}p\,(E/c)\tilde W_\Xi=-i\,m\,J_{\Phi,t}$, with the $i$ where the element's temporal slot puts it. The three moments together reproduce the polar form's four-current.

In a fixed unit element the element splits exactly, $\tilde W_\Xi=\bigl(W[a]+W[b]\bigr)+i\bigl(W[a,b]-W[b,a]\bigr)$ with $a=\lVert\tilde\Xi\rVert\cos(S_{\tilde\Xi}/\hbar)$ and $b=\lVert\tilde\Xi\rVert\sin(S_{\tilde\Xi}/\hbar)$ the two quadratures, so the real part is the phase-space image of the density and the imaginary part the phase-space image of the quadrature correlation. A rotating unit adds rotor gradients at first order in the offset, which is the Wigner picture of the spin-fluid article's statement that the vorticity is sourced by rotor gradients.

The classical limit is the fluid: $\tilde W_\Xi\to\rho_{\mathrm{num}}\delta^{3}(\vec p-\vec\nabla_\Phi S_{\tilde\Xi})$, shell-supported, so the fluid picture is a projection of the Wigner picture and not an independent description. The width the projection discards is the quantum potential for a Gaussian, $Q_{\mathrm{qnt}}(r_0)=\mathrm{Var}(p)/m=\hbar^{2}/(4m\sigma^{2})$, and the part the projection cannot make positive is measured on a two-level superposition at $-0.113\,359\,879\,579\,893\,8$, with $1.89\%$ of the sampled phase space negative.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $\tilde\Xi$ | Scalar field, an element of $\mathbb{B}$ |
| $\tilde\Xi^{*}$ | Its conjugate |
| $\Xi$ | The central case of the field: complex-valued, vector part zero |
| $\lVert\tilde\Xi\rVert^{2}$ | Amplitude squared; never a bare letter |
| $\rho_{\mathrm{num}}=\lVert\tilde\Xi\rVert^{2}$ | Proper density |
| $S_{\tilde\Xi}$ | Action of the polar form, with $\vec\nabla_\Phi S_{\tilde\Xi}=\vec p$ |
| $\tilde W_\Xi(r,\vec p)$ | Biquaternionic Wigner element |
| $r$, $\vec s$ | Position and relative coordinate; the offsets are $\pm\vec s/2$ |
| $\vec p$, $p_\eta$ | Momentum, the transform variable, and its components |
| $\hbar$ | Action quantum |
| $m$, $c$ | Mass and speed of light in the medium |
| $E=-c\,\partial S_{\tilde\Xi}/\partial r'_t$ | Energy; $r'_t$ is the temporal coordinate, a length |
| $\tilde J_\Phi=ic\rho_{\mathrm{num}}E/(mc^{2})\,e_t+\vec j$ | Four-current of the polar form |
| $j_\eta=\rho_{\mathrm{num}}p_\eta/m$ | Current density |
| $\mathrm{Sc}$ | Scalar part |
| $\langle\ \rangle_{\natural}$ | Quaternionic norm |
| $W[a]$, $W[a,b]$ | Wigner transform of a real function, and the cross transform of two |
| $a$, $b$ | Quadratures, $\lVert\tilde\Xi\rVert\cos(S_{\tilde\Xi}/\hbar)$ and $\lVert\tilde\Xi\rVert\sin(S_{\tilde\Xi}/\hbar)$ |
| $u$ | A fixed unit element |
| $\tilde U_{\mathrm{rot}}$ | Rotor of the polar form |
| $Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\Box_\Phi\lVert\tilde\Xi\rVert/\lVert\tilde\Xi\rVert$ | Quantum potential, with the minus sign |
| $\sigma$ | Position width of a Gaussian packet |
| $\mathrm{Var}(p)$ | Second moment of the Wigner distribution about the flow momentum, along one direction |
| $\mathrm{Var}_{\mathrm{tr}}(p)$ | Its trace over the three directions, the three-dimensional reading |
| $\delta^{3}(\vec s)$ | Three-dimensional delta |
| $\alpha$ | Phase-space variable of the Bell article, with $d^{2}\alpha=dq\,dp/2$ |

## Further Reading

- E. Wigner, "On the quantum correction for thermodynamic equilibrium," *Physical Review* **40** (1932) 749–759, the original.
- M. Hillery, R. F. O'Connell, M. O. Scully and E. P. Wigner, "Distribution functions in physics: fundamentals," *Physics Reports* **106** (1984) 121–167, for the properties and the marginal theorems.
- R. L. Hudson, "When is the Wigner quasi-probability density non-negative?" *Reports on Mathematical Physics* **6** (1974) 249–252, for the non-negativity theorem.
- W. B. Case, "Wigner functions and Weyl transforms for pedestrians," *American Journal of Physics* **76** (2008) 937–946, for the conventions and the sign traps.
- C. Zachos, D. Fairlie and T. Curtright, *Quantum Mechanics in Phase Space* (World Scientific, 2005), for the systematic treatment.
- H.-T. Elze, M. Gyulassy and D. Vasak, "Transport equations for the Wigner function," *Nuclear Physics B* **276** (1986) 706–728, for the relativistic Wigner function and its expansion.
- D. Vasak, M. Gyulassy and H.-T. Elze, "Quantum transport equations for the quark-gluon plasma," *Annals of Physics* **173** (1987) 462–492, for the matrix-valued relativistic Wigner function of a spin-$\tfrac12$ field.
- The companion articles: [The Bell Inequality for Continuous Variables in Biquaternionic Form](the-bell-inequality-for-continuous-variables-in-biquaternionic-form.html), [The Polar Form of the Klein–Gordon Equation in Biquaternionic Form](the-polar-form-of-the-klein-gordon-equation-in-biquaternionic-form.html), [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html), and [Relativistic Wigner Function and Quantum Kinetics](relativistic-wigner-function-and-quantum-kinetics.html).
