# __Physical Interpretation of Spectral Regularity and Degeneracy in the Biquaternion Algebra__

## Introduction

Spectral regularity is the condition that the two eigenvalues of a biquaternion can be told apart. It is a condition on the operator the element generates, not on a motion of the element. When it holds, the operator carries a complex structure: two invariant planes, a mode basis, a non-zero splitting. When it fails, the operator carries a nilpotent part: a flag, not a basis, and the element is a degeneracy.

The article reads the two cases physically. The regular case gives the mode picture: two complex frequencies, a mode frame, a normal-mode decomposition of every element. The degenerate case is not one phenomenon. The operator is $Q_t I+N$ with $N^2=0$, and the three normal forms — $N=0$, $Q_t=0$, and both non-zero — are the scalar line, the nilpotent stratum and the unipotent stratum. Each has its own interpretation: a pure rate with no direction; a null shift with no rate; a rate with a shear. On none of them is there a canonical mode basis, and the reason is the same in all three: no two-term spectral decomposition exists, and the Peirce idempotents are a gauge.

The vocabulary is the harmonic one, and it is exact. The regular element supplies the root of the Fourier kernel, and the degenerate cone is where that kernel stops oscillating. The two readings are the same construction seen from the spectrum and from the transform.

The mathematics is proved in *The Spectrum* and *The Eigenbasis of a Spectrally Regular Biquaternion*. The article belongs to *Biquaternion Physical Interpretation of Mathematics*: it interprets that mathematics, and it proves nothing. It identifies the physical objects, labels the interpretations, and states the boundary of each.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The characteristic polynomial, the discriminant $-4B^2$, the eigenvalues $Q_t\pm iB$ and the two spectral cases | [The Spectrum](../articles_maths/spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), §*The Spectral Criterion* and §*The Two Cases* |
| The norm $N=Q_t^2+B^2$, its multiplicativity and the null cone | [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), §*The Quaternionic Norm* and §*The $N$-degenerate case* |
| The operator form $L_{\tilde Q}=Q_t\,\mathrm{id}+L_{\vec Q}$ and $L_{\vec Q}^2=-B^2\mathrm{id}$ | [The Spectrum](../articles_maths/spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), §*The Operator Form of the Criterion* |
| The spectral idempotents $\tilde\Pi_\pm$, the two-term writing and its uniqueness | [The Spectrum](../articles_maths/spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), §*The Spectral Decomposition* |
| The eigenspaces of dimension two and the existence of an eigenbasis | [The Spectrum](../articles_maths/spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), §*The Eigenbasis of Left Multiplication* |
| The three strata, their minimal polynomials, centralisers and normal forms | [The Jordan Basis of a Spectrally Degenerate Biquaternion](../articles_maths/the-spectrally-degenerate-sector-and-construction-of-the-jordan-basis-of-a-biquaternion.html), §*The Three Strata* |
| The isotropic line, the canonical flag and the absence of a canonical complement | [The Spectrum](../articles_maths/spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), §*The Isotropic Line and the Flag* |
| The normalised Peirce basis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ and the unique expansion | [The Eigenbasis of a Spectrally Regular Biquaternion](../articles_maths/the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), §*The Eigenbasis* and §*Expansion of Every Biquaternion* |
| The four sectors $\Sigma_{ij}$ and the independence of $N\neq0$ and $B^2\neq0$ | [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), §*The Four Sectors* |
| The similarity classification on the cone | [The Spectrum](../articles_maths/spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), §*The Similarity Classification* |
| The exponential and the logarithm in the regular, nilpotent and unipotent regimes | [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html) |
| The Fourier kernel, the root and the root-adapted basis | [Biquaternion Continuous Harmonic Analysis](../articles_maths/biquaternion-continuous-harmonic-analysis.html), §*The Fourier Kernel* and §*Factorization into Complex Fourier Transforms* |
| The unitary character and the root criterion | [The Bochner Theorem for the Biquaternion Transform: the Hermitian Form and the Root](../articles_maths/the-bochner-theorem-for-the-biquaternion-transform-the-hermitian-form-and-the-root.html), §*Unitarity of the Character and the Root* |
| The degenerate characters and the non-oscillating transform | [Dual-Numbers Harmonic Analysis](../articles_maths/dual-numbers-harmonic-analysis.html), §*The Dual Characters* and §*The Structure of the Transform* |

The table is the contract: every physical statement below is an interpretation of a result in one of these rows. The physics companions are *The Spectral Reading of a Four-Vector*, *Exceptional Points and the Nilpotent Regime in the Biquaternion Spectrum*, *The Zero-Divisor Cone and the Massless Spectrum*, *The Square-Zero Element*, *Biorthogonal Quantum Mechanics and the Biquaternion Spectrum* and *The Exponential, the Logarithm and the Generator*; they are linked where their interpretations are used, and this article does not repeat them.

## The Spectral Condition

### The Discriminant

For $\tilde Q=Q_te_t+\vec Q$ the characteristic polynomial and its discriminant are

$$
p_{\tilde Q}(X)=X^2-2Q_tX+Q_t^2+B^2,
\qquad
\operatorname{disc}p_{\tilde Q}=-4B^2,
\qquad
B^2=(\vec Q,\vec Q)=Q_x^2+Q_y^2+Q_z^2,
$$

and the eigenvalues are

$$
\boxed{\;\lambda_\pm=Q_t\pm iB\;}.
$$

They coincide exactly when $B^2=0$, because their difference is $2iB$. The number $B$ is one of the two square roots of $B^2$; the other exchanges the two eigenvalues and changes nothing else. Every physical statement must therefore be written in terms of $B^2$, or in terms of the unordered pair $\{\lambda_+,\lambda_-\}$, and the sign of $B$ is a label.

| case | condition | spectrum | spectral decomposition | eigenbasis |
| --- | --- | --- | --- | --- |
| **spectrally regular** | $B^2\neq0$ | two distinct eigenvalues | two terms, unique | exists |
| **spectrally degenerate** | $B^2=0$ | one repeated eigenvalue $Q_t$ | one term iff $\vec Q=0$, none otherwise | every basis iff $\vec Q=0$, none otherwise |

**The first physical statement is a warning.** Regular does not mean invertible, and degenerate does not mean non-invertible. The norm $N=Q_t^2+B^2$ decides invertibility; $B^2$ decides whether the two eigenvalues can be told apart. The two conditions are independent, and the independence is the subject of §*The Four Sectors* below. A massless particle has $N=0$ and, away from the zero momentum, $B^2\neq0$: it is a zero divisor with a perfectly good mode basis. A unipotent element has $N=Q_t^2\neq0$ and $B^2=0$: it is a unit with no mode basis. The words *regular* and *degenerate* in this article always mean spectral regularity and spectral degeneracy, and never invertibility.

### The Operator Form: The Internal Complex Structure

The spectral condition is read on the operators of left and right multiplication. With $L_{\tilde Q}(\tilde X)=\tilde Q\tilde X$ and $R_{\tilde Q}(\tilde X)=\tilde X\tilde Q$,

$$
L_{\tilde Q}=Q_t\,\mathrm{id}+L_{\vec Q},
\qquad
R_{\tilde Q}=Q_t\,\mathrm{id}+R_{\vec Q},
\qquad
L_{\vec Q}^2=-B^2\,\mathrm{id},
\qquad
R_{\vec Q}^2=-B^2\,\mathrm{id}.
$$

The identity $L_{\vec Q}^2=-B^2\,\mathrm{id}$ is the algebraic core of the whole article. It says that the directional part of the operator is either a complex structure or a nilpotent, and nothing else.

- **If $B^2\neq0$**, then

    $$
    J_{\tilde Q}=\frac{L_{\vec Q}}{B},
    \qquad
    J_{\tilde Q}^2=-\mathrm{id},
    \qquad
    L_{\tilde Q}=Q_t\,\mathrm{id}+B\,J_{\tilde Q}.
    $$

    The operator is a scalar rate plus a complex structure of rate $B$. The complex structure has two invariant two-dimensional subspaces, on which its eigenvalues are $+i$ and $-i$; the eigenvalues of $L_{\tilde Q}$ are $Q_t\pm iB$, each with multiplicity two. The one-parameter group is

    $$
    \exp(\theta L_{\tilde Q})
    =e^{\theta Q_t}\left(\cos(B\theta)\,\mathrm{id}+\sin(B\theta)\,J_{\tilde Q}\right).
    $$

- **If $B^2=0$**, then

    $$
    N_{\tilde Q}=L_{\vec Q},
    \qquad
    N_{\tilde Q}^2=0,
    \qquad
    L_{\tilde Q}=Q_t\,\mathrm{id}+N_{\tilde Q},
    \qquad
    \exp(\theta L_{\tilde Q})=e^{\theta Q_t}\left(\mathrm{id}+\theta N_{\tilde Q}\right).
    $$

    There is no complex structure and no period. The operator is a scalar rate plus a nilpotent shift.

This is the sense in which $B$ is **operator-linked**. It is the coefficient of the complex structure of the operator, not the speed of a motion of the element. The word *clock* is a name for that structure: $J_{\tilde Q}$ has period $2\pi$ in the flow parameter, and the element's rate $B$ converts the period to $2\pi/B$. At $B=0$ the clock stops, and the flow becomes a unipotent translation.

**Boundary.** The flow parameter $\theta$ is the parameter of the one-parameter group, not automatically a physical time. The identification $\theta=t$ is a separate, sector-dependent step: it is the Schrödinger evolution when the generator is $-i\tilde H$ in the convention $e^{-i\tilde Ht}$, and it is not a spacetime translation for a four-momentum — the translation is the central phase $e^{i\tilde P\cdot\tilde X}$, a different construction. The operator interpretation of $B$ is a statement about the spectrum and the invariant subspaces; it is not a dynamics. The complex structure $J_{\tilde Q}$ is internal: it is a root of $-\mathrm{id}$ on $\mathbb{B}$, not the local complex structure of the material sector, which is a choice of real slice and imaginary-time direction.

### The Four Sectors

The pair of predicates $(N\neq0,\ B^2\neq0)$ cuts the algebra into four sectors. Write $\Sigma_{ij}$ for the sector with $N\neq0$ if $i=1$ and $B^2\neq0$ if $j=1$. In the language of the N-regularity article, $\Sigma_{11}$ is N-regular and spectrally regular, $\Sigma_{10}$ is N-regular and spectrally degenerate, $\Sigma_{01}$ is N-degenerate and spectrally regular, and $\Sigma_{00}$ is N-degenerate and spectrally degenerate. The table is the physical map; it is the fastest way to see that the spectral question and the invertibility question are different questions.

| sector | conditions | spectrum | unit | mode basis | physical type |
| --- | --- | --- | --- | --- | --- |
| $\Sigma_{11}$ | $N\neq0$, $B^2\neq0$ | two distinct non-zero | yes | yes | generic two-mode unit |
| $\Sigma_{10}$ | $N\neq0$, $B^2=0$ | double non-zero | yes | no on the Jordan part; every basis on the scalar line | defective unit, or pure rate |
| $\Sigma_{01}$ | $N=0$, $B^2\neq0$ | two distinct, one zero | no | yes | null element with one live mode |
| $\Sigma_{00}$ | $N=0$, $B^2=0$ | double zero | no | no on the nilpotent part; every basis at the origin | nilpotent, or the origin |

**Interpretation.** The two columns *unit* and *mode basis* are independent. A physical object can be reversible without a mode basis ($\Sigma_{10}$), and it can have a mode basis without being reversible ($\Sigma_{01}$). The first is the defective unit; the second is the massless or pure-state case. The generic case $\Sigma_{11}$ has both. The doubly degenerate case $\Sigma_{00}$ has neither outside the origin; the origin itself is scalar and every basis is an eigenbasis.

**Boundary.** The names *massless* and *mass shell* are material-sector interpretations of $N=0$ and of its level sets; the algebraic statement is only $N=0$. The sector table is a partition of the algebra, not a classification of physical particles.

## The Regular Case: Two Modes and a Mode Basis

### The Splitting as a Gap

The difference of the eigenvalues is

$$
\lambda_+-\lambda_-=2iB.
$$

The complex number $2iB$ is the **complex splitting**. If the eigenvalues are written as complex frequencies in the convention of the evolution $e^{-i\lambda t}$,

$$
\lambda_\pm=\omega_\pm-i\gamma_\pm,
$$

then

$$
B=\frac{\gamma_--\gamma_+}{2}-\frac{i}{2}\left(\omega_+-\omega_-\right).
$$

The real part of $B$ is half the difference of the damping rates, in the order $\gamma_--\gamma_+$ for the convention $e^{-i\lambda t}$; the imaginary part is minus half the difference of the oscillation frequencies. The split is complex, and it is the general case. Normality makes the root real, not the half-gap: $B$ can be complex even when the eigenbasis is orthogonal. The Hermitian and material cases are two real slices of it.

| case | element | eigenvalues | interpretation of $B$ |
| --- | --- | --- | --- |
| material four-momentum | $i\frac{E}{c}e_t+\vec p$ | $i\left(\frac{E}{c}\pm\lvert\vec p\rvert\right)$ | $B=\lvert\vec p\rvert$: the momentum magnitude; the pair is the Doppler pair |
| Hermitian observable | $h_t+i\vec h$ | $h_t\mp\lvert\vec h\rvert$ | $B=i\lvert\vec h\rvert$: the half-gap is $\lvert\vec h\rvert$ |
| normal, real $B$ | $\vec Q$ real, $B$ real | $Q_t\pm iB$ | real half-gap; the damping sits in $Q_t$ |
| normal, complex $B$ | $\vec Q$ a complex multiple of a real vector, $B$ complex | complex | complex half-gap; orthogonal modes, growing norm |
| non-normal | $\vec Q$ not a complex multiple of a real vector | real or complex | biorthogonal modes; non-normality alone does not force growth |
| null idempotent multiple | $c\tilde\Pi$ | $c$ and $0$ | the eigenvalues are the amplitude and zero |

**Interpretation.** The same $B$ is interpreted as a **half-gap** in the informational sector, as a **momentum magnitude** in the material sector, and as a **complex half-splitting** for an element with complex $B$; a normal element with real $B$ has a real half-gap and carries its damping in $Q_t$. The algebra supplies one number; the sector supplies the physical name. The gap of a two-level system is $2\lvert B\rvert$ in the Hermitian case, and the beat frequency of the two modes is $2\lvert B\rvert$ in the general case. The massless case is the limit in which one of the two eigenvalues reaches zero.

**Boundary.** The identification of $\lambda_\pm$ with $\omega_\pm-i\gamma_\pm$ depends on the sign convention of the evolution; with $e^{+i\lambda t}$ the roles of the real and imaginary parts are exchanged. The algebra gives the eigenvalues, not the convention. For an observable the eigenvalues are outcomes, not frequencies, and the word *gap* is the difference of two outcomes; for a four-momentum they are light-cone frequencies, not energies. The table is a dictionary of readings, not one interpretation applied to every row.

### The Fourier Kernel and the Frequency

The word *frequency* is not borrowed. For $B^2\neq0$ put

$$
\rho=\frac{\vec Q}{B},
\qquad
\rho^2=-e_t .
$$

The root is pure, and the exponential of the element is

$$
\boxed{\;
e^{\theta\tilde Q}
=e^{\theta Q_t}\left(\cos(B\theta)\,e_t+\sin(B\theta)\,\rho\right)
=e^{\theta Q_t}\,W(-\theta,B/2\pi)\;},
$$

where

$$
W(t,\omega)=\exp(-2\pi\rho\,\omega t)
$$

is the biquaternion Fourier kernel of *Biquaternion Continuous Harmonic Analysis*. Left multiplication by the same identity gives the operator flow, $L_{e^{\theta\tilde Q}}=e^{\theta L_{\tilde Q}}$. The regular element therefore supplies the root that the Fourier transform otherwise fixes by hand: the kernel is the exponential of $\rho$, and $B$ is the rate of the flow relative to that root. This is the statement of *Derivatives, Fields and Transforms* that the root is the clock and the frequency is its rate.

**The eigenbasis is the Fourier basis.** The transform is computed in a root-adapted basis $\{e_t,\rho,\nu,\xi\}$, in which left multiplication by $\rho$ is block diagonal and the transform splits into ordinary complex Fourier transforms. The eigenbasis of $L_{\tilde Q}$ is that basis after the complex change that diagonalises the two blocks. The eigenvalues $\lambda_\pm=Q_t\pm iB$ are the two character exponents of the flow, and the spectral idempotents $\tilde\Pi_\pm$ are the elements that split the algebra into the two eigenspaces. In this sense the eigenbasis is the Fourier basis attached to $\tilde Q$, and the mode decomposition is the decomposition of the flow into its two characters.

**Which sector carries it.** The construction follows $B^2$ and not $N$: it is available on $\Sigma_{11}$ and on $\Sigma_{01}$, the massless zero divisors included, and unavailable on $\Sigma_{10}$ and $\Sigma_{00}$ except on the scalar line, where every basis is an eigenbasis but none is attached to the element. A massless momentum has the real root $\vec p/\lvert\vec p\rvert$ and a unitary Fourier character even though it is a zero divisor.

**Which character is unitary.** The kernel is unitary for the natural conjugation for every pure root, $\rho^{\natural}=-\rho$. The positive Hermitian form — the form the Born rule uses — is more restrictive: the character is unitary for it exactly when $\rho^{*}=-\rho$, which for a pure root means that $\rho$ is real (*The Bochner Theorem for the Biquaternion Transform*, §*Unitarity of the Character and the Root*). For $\rho=\vec Q/B$ this is equivalent to the normality of the vector part: $\operatorname{Re}\vec Q$ and $\operatorname{Im}\vec Q$ are parallel. The material vector part is real and the Hermitian vector part is purely imaginary, so both physical sectors are normal. The two sectors differ in the sign of $B^2$: for the material element $B$ is real and the flow oscillates, while for the Hermitian element $B=i\lvert\vec h\rvert$ is imaginary and the flow is a boost. A non-normal $\vec Q$ gives a non-real root and a non-unitary character, hence the biorthogonal modes of *Biorthogonal Quantum Mechanics and the Biquaternion Spectrum*; it does not by itself give damping. The unitarity criterion of the character is normality, not Hermiticity: it holds on both physical sectors and fails on a non-normal element. The unitarity of the flow is stronger: it is the material sector alone, $\tilde Q^*=-\tilde Q$. The self-adjoint flow is the Hermitian sector, $\tilde Q^*=\tilde Q$, and it is normal. Normality implies neither unitarity nor self-adjointness, and it does not make the norm constant.

**Boundary.** The flow parameter $\theta$ is not a physical time, and $B$ is the rate relative to the chosen root, not the Fourier variable of a signal. The transform is a change of description and not a measurement. The algebra supplies the kernel and the rate; it does not supply the dynamics, the signal or the clock.

### The Norm of the Flow and the Three Rates

The flow has a Hermitian norm, and its formula separates the three data. With $\rho=\vec Q/B$ and $\lVert\rho\rVert_E^2=\sum_k\lvert\rho_k\rvert^2$ — the Euclidean modulus sum, not the bilinear form $(\rho,\rho)=-1$ —

$$
\langle e^{\theta\tilde Q}\rangle_*
=\lvert e^{\theta Q_t}\rvert^2
\left(\lvert\cos(B\theta)\rvert^2+\lvert\sin(B\theta)\rvert^2\,\lVert\rho\rVert_E^2\right),
\qquad
\lVert\rho\rVert_E^2\ge1 .
$$

| source | factor | physical name |
| --- | --- | --- |
| $\operatorname{Re}Q_t$ | $e^{2\theta\operatorname{Re}Q_t}$ | damping or amplification of both modes |
| $\operatorname{Im}B$ | growth like $e^{2\lvert\operatorname{Im}B\rvert\lvert\theta\rvert}$ | boost, or complex rate |
| $\lVert\rho\rVert_E^2-1$ | amplitude factor, $\ge0$ | non-normality, not a rate |

The deficit $\lVert\rho\rVert_E^2-1$ vanishes exactly for a normal element, but it is an amplitude: a non-normal element oscillates between $1$ and $\lVert\rho\rVert_E^2$ when $B$ is real and $Q_t$ is purely imaginary. The element $i\vec e_x+\vec e_y+\vec e_z$ is not normal, has $B=1$, and its norm is $1+2\sin^2\theta$. The normal element $(1+i)\vec e_x$ has $B=1+i$ and norm $\cosh2\theta$. The first is bounded and the second grows, so non-normality is not a damping mechanism.

The two physical sectors are the two real slices of the algebra on which the flow is, respectively, unitary and self-adjoint. In the material sector $\tilde Q^*=-\tilde Q$: the flow is unitary and its Hermitian norm is $1$. In the Hermitian sector $\tilde Q^*=\tilde Q$: the flow is self-adjoint and, for a normal element, its Hermitian norm is $e^{2\theta Q_t}\cosh(2\lvert B\rvert\theta)$. Normality is weaker than both and gives the orthogonal eigenbasis, not a constant norm.

**Boundary.** The formula is the norm of the exponential, not the norm of a state. A physical state needs a sector projection and a normalisation; the algebra supplies neither.

### The Two-Term Writing

For $B^2\neq0$ the element is

$$
\boxed{\;\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,
\qquad
\tilde\Pi_\pm=\frac12\left(e_t\pm\vec\Xi\right),
\qquad
\vec\Xi=-\frac{i\vec Q}{B},
\qquad
\vec\Xi^2=e_t\;}.
$$

The idempotents are orthogonal, sum to the identity, and are unique. Each term is a complex multiple of a minimal idempotent, hence an element of the zero-divisor cone; the two terms are the two **spectral components** of the element. The sum of the coefficients is twice the scalar part, and their product is the norm:

$$
\lambda_++\lambda_-=2Q_t,
\qquad
\lambda_+\lambda_-=N.
$$

**Interpretation.** The two-term writing is the **mode decomposition**. The element is a sum of two components, each carrying one of the two frequencies and one of the two idempotents. The physical meaning of the terms depends on the sector, and the dependence is the content of the table.

| element type | $\tilde\Pi_\pm$ | interpretation of the two terms |
| --- | --- | --- |
| Hermitian observable | Hermitian projectors | the two outcomes; orthogonal; the Born rule applies |
| material four-momentum | Hermitian idempotents | the two null components; the Doppler pair |
| general non-normal element | non-Hermitian idempotents | two biorthogonal modes; no orthogonal basis |
| null element, $N=0$, $B^2\neq0$ | one coefficient zero | one live mode; the massless limit of the two-term writing |

**Boundary.** The two terms are not two particles and not two energies. They are two spectral components of one element; the sum of their coefficients is twice the scalar part, not the energy, and the product of their coefficients is the norm, not a second mass-shell condition. The interpretation of the terms as *outcomes* is licensed only for a Hermitian element; the interpretation as *null components* only for the material four-momentum; the interpretation as *biorthogonal modes* only for a non-normal element, where the two dual bases differ. The algebra gives the decomposition in all three cases; it does not give one physical interpretation of it.

### The Mode Frame

The eigenspaces of $L_{\tilde Q}$ are the right ideals

$$
\ker\left(L_{\tilde Q}-\lambda_\pm\right)=\tilde\Pi_\pm\mathbb{B},
$$

each of complex dimension two. The two ideals are the two **mode spaces**. Any basis of each is an eigenbasis; the normalised Peirce basis

$$
\mathcal B(\tilde Q)=\left(\tilde\Pi_+,\ \vec\Upsilon_-,\ \vec\Upsilon_+,\ \tilde\Pi_-\right),
\qquad
\vec\Upsilon_-\in\tilde\Pi_+\mathbb{B}\tilde\Pi_-,
\qquad
\vec\Upsilon_+\in\tilde\Pi_-\mathbb{B}\tilde\Pi_+,
$$

is the representative fixed by the normalisation, and in it

$$
\mathsf M\big(L_{\tilde Q}\big)=\operatorname{diag}\left(\lambda_+,\lambda_+,\lambda_-,\lambda_-\right),
\qquad
\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-.
$$

**Interpretation.** The Peirce basis is the **normal-mode frame** of the element. The expansion is the statement that every element of the algebra has coordinates in that frame; the coordinates are the amplitudes of the four components. The two eigenvalues appear twice because left multiplication sees both columns of the matrix model: the multiplicity two is the **spinor doubling**, not a second physical mode. The physical mode count is two; each mode carries a two-component spinor.

**Boundary.** The mode frame is attached to the element, so it changes when the element changes; it is not a fixed laboratory frame. The two eigenspaces are unique, but the vectors inside each are not: an invertible change of basis on each eigenspace gives another eigenbasis. The Peirce normalisation fixes a representative; it is a convention, not a physical preferred frame. A physical statement may use the eigenspaces and the eigenvalues; it may use the Peirce vectors only after saying which normalisation it has chosen.

### What the Spectrum Does Not Fix

The spectrum is two complex numbers; the element is eight real parameters. The spectrum fixes the trace and the norm,

$$
\lambda_++\lambda_-=2Q_t,
\qquad
\lambda_+\lambda_-=N,
$$

and it fixes nothing else about the vector part. The axis $\vec\Xi$ has two free complex angles, four real parameters, and the two eigenvalues are blind to them. At $B^2=0$ the axis is not defined, and the two-term spectral decomposition does not exist except on the scalar line.

**Interpretation.** A spectral measurement reads the two frequencies and leaves the frame free. The set of elements with a given spectrum is the set of elements obtained by changing the axis; for a four-momentum it is the two-sphere of directions at fixed energy and momentum magnitude. The spectrum is therefore a **frame-blind** observable: it sees the splitting and the mean, not the orientation.

**Boundary.** *Not fixed* is not *not constrained*. The spectrum constrains the element to a quadric, and for a four-momentum to a sphere. The claim is that the spectrum is insufficient to determine the element, not that it is uninformative. A measurement that resolves the idempotents as well is a different measurement, and it reads the frame.

### Spectral Regularity Is Not Invertibility

The sector table has two off-diagonal entries, and they are the two physical warnings.

- **$\Sigma_{01}$: a null element with distinct eigenvalues.** A massless four-momentum has $N=0$ and $B^2=\lvert\vec p\rvert^2\neq0$ away from $\vec p=0$. Its two eigenvalues are $2iE/c$ and $0$. The second coefficient vanishes, so only one term of the two-term writing survives, but the **basis still exists**: the zero eigenvalue has a two-dimensional eigenspace, and the element's component along it is zero. The mode is present in the basis and absent from the element. The physical interpretation is a massless particle with one live light-cone mode; the zero mode is a genuine spectral direction, not a failure of the decomposition.
- **$\Sigma_{10}$: a unit with no mode basis.** A unipotent element has $N=Q_t^2\neq0$ and $B^2=0$. It is invertible, its inverse is $Q_t^{-1}(e_t-\vec\Upsilon)$, and it has no eigenbasis. The physical interpretation is a reversible process with a defective mode; the reversibility is the norm, the defect is the spectrum, and neither implies the other.

**Interpretation.** *Having a mode basis* and *being reversible* are independent properties. The first is spectral, the second is the norm. The generic element has both; the massless element has the first without the second; the unipotent element has the second without the first; the nilpotent has neither.

**Boundary.** The identification of $N=0$ with *massless* is the material-sector interpretation; the algebraic statement is $N=0$. The identification of $N\neq0$ with *reversible* is the algebraic unit group; a physical process described by a unit can still be dissipative when the unit is not the whole story, for example when the complex scalar part carries a decay rate.

### Genericity and the Codimension of the Cone

The spectral-degenerate set is the cone

$$
\mathcal S=\{\tilde Q:\ B^2=0\}=\{Q_t\in\mathbb{C},\ \vec Q\in\mathbb{C}^3:\ Q_x^2+Q_y^2+Q_z^2=0\}.
$$

It is one complex equation in four complex variables, hence a complex hypersurface of complex dimension three and real dimension six. Its gradient with respect to $\vec Q$ is $2\vec Q$, so it is smooth off the scalar line $\vec Q=0$; the scalar line is its singular locus, the vertex. Inside $\mathcal S$ the unipotent stratum is dense, the nilpotent stratum is a complex cone of one lower dimension, and the scalar line is the vertex.

**Interpretation.** A generic element has a mode basis: the regular set is open and dense. A degeneracy is a complex hypersurface, of real codimension two in the full algebra; two real conditions must be tuned to reach it. This is the algebraic reason an exceptional point needs two parameters, and it is the reason the mode picture is the generic picture and the degeneracy is the exception.

**Boundary.** *Generic* is a statement about the algebra, not about a physical ensemble. The cone is thin in the algebra and physically important: the rest frame of a massive particle, the null field of radiation, and the exceptional point of a non-Hermitian system all lie on it or on its relatives. A thin set is not a negligible set.

## The Degenerate Case: The Clock Stops

### The Three Strata

On the cone the two eigenvalues have coalesced at $Q_t$, the complex structure is gone, and the operator is $Q_t\,\mathrm{id}+N$ with $N=L_{\vec Q}$ and $N^2=0$. On the unipotent stratum write $\vec\Upsilon=\vec Q/Q_t$. The three normal forms are the three ways this operator can look.

| stratum | conditions | normal form | minimal polynomial | unit | $\operatorname{rank}L_{\tilde Q}$ | physical type |
| --- | --- | --- | --- | --- | --- | --- |
| **scalar** | $\vec Q=0$ | $Q_te_t$ | $X-Q_t$ | iff $Q_t\neq0$ | $4$, or $0$ at the origin | pure rate; rest frame; trivial observable |
| **nilpotent** | $\vec Q\neq0$, $Q_t=0$ | $\vec N$, $\vec N^2=0$ | $X^2$ | no | $2$ | null field; null shift; zero-frequency coupling |
| **unipotent** | $\vec Q\neq0$, $Q_t\neq0$ | $Q_t(e_t+\vec\Upsilon)$, $\vec\Upsilon^2=0$ | $(X-Q_t)^2$ | yes | $4$ | defective resonance; locked modes; reversible non-normal |

**Interpretation.** The three strata are not three degrees of one phenomenon. They are the three normal forms of a nilpotent perturbation of a scalar: no perturbation ($N=0$), a perturbation with no scalar ($Q_t=0$), and a perturbation carried by a scalar ($Q_t\neq0$). The scalar line is the vertex of the cone; the nilpotent stratum is the zero-frequency subcone; the unipotent stratum is the generic part of the cone. The physical names follow the same division: a pure rate, a pure shift, and a rate with a shift.

**Boundary.** The table is a classification of elements, not of processes. A physical system may pass through a stratum, or be approximated by one, without being an element of it; the passage needs a family and a dynamics, and neither is in the table.

**In Fourier terms.** The root that the regular case reads off the element, $\rho=\vec Q/B$, does not exist on the cone: $\vec Q^2=0$, so there is no $B$ to divide by. The kernel cannot be trigonometric. The exponential is

$$
e^{\theta\tilde Q}=e^{\theta Q_t}\left(e_t+\theta\vec N\right),
$$

which is the dual-number exponential $e^{a+b\varepsilon}=e^a(1+b\varepsilon)$ in the algebra generated by $\vec N$, with $\varepsilon=\vec N$ and $b=\theta$. Its character has nilpotent deviation from the identity and does not oscillate; the model is the dual-number transform of *Dual-Numbers Harmonic Analysis*, not the oscillatory Fourier transform. The three normal forms are the three degenerate characters: the scalar line is the central character $e^{\theta Q_t}$ with no direction; the nilpotent is $e_t+\theta\vec N$, a null translation; the unipotent is $e^{\theta Q_t}(e_t+\theta\vec\Upsilon)$, a scaled null translation, the defective analogue of a character. On the nilpotent and unipotent strata there is no Fourier basis attached to the element; on the scalar line every basis diagonalises the flow, but the element supplies no root and no direction.

### The Scalar Line: A Pure Rate

For $\tilde Q=Q_te_t$ the operator is $L_{\tilde Q}=Q_t\,\mathrm{id}$. Every vector is an eigenvector with eigenvalue $Q_t$, every basis is an eigenbasis, and the only spectral writing is the one-term $\tilde Q=Q_te_t$.

**Interpretation 1: a global phase and a scale.** Write $Q_t=q_t+iq_t'$. Then

$$
\exp(Q_t)=e^{q_t}e^{iq_t'}.
$$

The real part is a dilation, the imaginary part a phase. Both are central: they commute with every element and every operator of the algebra. The physical interpretation is a **global phase and a choice of scale** — the phase invisible on rays, the scale a unit convention. The element acts on the algebra by scalar multiplication, not by a rotation of a frame.

**Boundary.** A global phase is not an observable, and a scale is not a physical field. The interpretation is licensed for the centre; it does not say that every scalar is a gauge transformation, and it does not supply a gauge field.

**Interpretation 2: the rest frame and time-only displacement.** In the material sector the scalar is $Q_t=ict'$, so

$$
\tilde X=ict'e_t,
\qquad
\langle\tilde X\rangle_{\natural}=-c^2t'^2.
$$

The element is a purely temporal displacement: a worldline with no spatial part. The four-velocity of a particle at rest is the same kind of element, $ic\,e_t$. The physical interpretation is **time only**: a clock reading with no direction in space, and no spatial momentum. For a four-momentum it is the rest frame, because $B^2=\lvert\vec p\rvert^2$ vanishes exactly at $\vec p=0$; for a general material element it is the whole time axis.

**Boundary.** A rest frame exists only for a massive particle; the algebra gives the interval, not the mass. The scalar $ict'$ is a displacement, not a duration measured by a particular clock; the identification of $t'$ with a physical time is the material-sector dictionary, not a consequence of the spectrum.

**Interpretation 3: the trivial observable and the maximally mixed state.** In the informational sector a Hermitian scalar $h_te_t$ is a multiple of the identity. Every state is an eigenstate with the same outcome $h_t$, and no measurement basis is selected. The trace-one scalar $\tfrac12e_t$ is the maximally mixed state; the scalar line is where the Bloch vector vanishes.

**Boundary.** The observable interpretation and the state interpretation are two identifications of the same central element, not one derivation of the other. The spectrum alone says *central*; it does not say *observable* or *state*. The state interpretation belongs to *The Informational Sector: States, Observables and Probability*.

**Interpretation 4: superselection and no preferred basis.** A central element is fixed by every inner automorphism. On the unitary slice, where the frame changes live, this reads $\tilde U\tilde Q\tilde U^{*}=\tilde Q$ for every unitary $\tilde U$. No frame is selected, every basis is an eigenbasis, and the choice of basis carries no information about the element. The physical interpretation is a **superselection charge**: a conserved central quantity with respect to which every basis is equivalent.

**Boundary.** *No preferred basis* does not mean *no basis*. A basis can be chosen, and in it the element is $Q_tI$; the point is that the choice is a gauge, not a property of the element.

### The Nilpotent Stratum: A Null Shift

For $\tilde Q=\vec N$ with $\vec N^2=0$ and $\vec N\neq0$, the operator is $L_{\vec N}$ with $L_{\vec N}^2=0$. It has rank two, spectrum $\{0\}$, kernel and image equal, and

$$
\exp(\theta L_{\vec N})=\mathrm{id}+\theta L_{\vec N},
\qquad
\exp(\theta\vec N)=e_t+\theta\vec N.
$$

The last identity is the sharp one: the element $\vec N$ is a zero divisor, but its exponential is a unit for every finite $\theta$. The nilpotent is the **velocity** of a null translation, not a point of the unit group.

**Interpretation 1: a null field.** A pure element with isotropic vector part is the algebraic form of a radiative field strength. For the electromagnetic field, the two invariants vanish exactly when $\vec E\perp\vec B$ and $\lvert\vec E\rvert=c\lvert\vec B\rvert$, and the field is a nilpotent: rank one in the matrix model, no rest frame, no invariant intensity. The physical interpretation is a **null plane wave**.

**Boundary.** The nilpotent is a field strength, not a four-momentum. The physical null momentum is a zero divisor with a non-zero square, an imaginary multiple of a Hermitian idempotent; it is not pure, and it is not a nilpotent. The physical null field has real $\vec E$ and $\vec B$, and its biquaternion representative is complex-pure; that is the slice of the complex nilpotent cone the identification uses, not the whole cone.

**Interpretation 2: a null translation.** The identity $\vec N^2=0$ says that the displacement is square-zero: the generator applied twice vanishes, so the exponential truncates at first order. The exponential $e_t+\theta\vec N$ is a one-parameter group of unipotent transformations whose generator is a zero divisor. The physical interpretation is a **reversible translation with a non-invertible generator**: the motion can be undone, the velocity cannot be inverted.

**Boundary.** The physical lightlike displacement is real and has $Q_t=ict'\neq0$ and $B=\lvert\vec x\rvert\neq0$ away from the origin; it is spectrally regular, not nilpotent. The nilpotent is the complex isotropic model of a null direction; the two must not be identified. This is the same distinction as *the nilpotent is not a four-momentum*, stated for displacements rather than momenta.

**Interpretation 3: a zero-frequency one-way coupling.** The matrix normal form is a Jordan block at zero,

$$
\mathsf M_2(\vec N)\sim\begin{pmatrix}0&1\\0&0\end{pmatrix}.
$$

The nilpotent maps the missing direction onto the surviving one and has no inverse. The physical interpretation is a **one-way coupling at zero frequency**: a mode that feeds another with no return, and a system with a single eigenline at zero. It is the normal form at the exceptional point with $Q_t=0$.

**Boundary.** The element alone is a Jordan block, not an exceptional point. An exceptional point is a property of a family; the $\sqrt{\epsilon}$ splitting law needs a family and a direction, and the algebra supplies neither. The zero-frequency coupling is the normal form, not the measured response.

**Interpretation 4: a flag, not a basis.** The canonical data are the isotropic line and the flag

$$
0\subset\mathbb{C}\vec N\subset\ker L_{\vec N}\subset\mathbb{B},
\qquad
\ker L_{\vec N}=\operatorname{im}L_{\vec N}.
$$

The line has no canonical complement, so there is no canonical pair of complementary subspaces and no eigenbasis. The physical interpretation is a **nested polarization**: a lightlike line, a screen through it, and the whole space — a flag, not a frame.

**Boundary.** A flag is not a basis. A basis can be chosen by adding a complement, but the complement is a gauge; the physical content of the element is the flag.

**Interpretation 5: a fermionic mode.** A pair of nilpotents with anticommutator $e_t$ is the one-site fermionic ladder; the square-zero property is the exclusion principle at the level of one mode. The physical interpretation is a **mode**, not a field. The details are in *The Square-Zero Element*; this article uses the interpretation only to locate the stratum.

**Boundary.** The algebra supplies the mode and the local corner, not the field, the lattice, the dynamics or the physical null momentum.

### The Unipotent Stratum: A Rate with a Shear

For $B^2=0$, $\vec Q\neq0$, $Q_t\neq0$, put $\vec\Upsilon=\vec Q/Q_t$. Then $\vec\Upsilon^2=0$, $\vec\Upsilon\neq0$, and

$$
\boxed{\;\tilde Q=Q_t\left(e_t+\vec\Upsilon\right),
\qquad
\tilde Q^{-1}=Q_t^{-1}\left(e_t-\vec\Upsilon\right),
\qquad
\exp(\theta\tilde Q)=e^{\theta Q_t}\left(e_t+\theta\vec Q\right)\;}.
$$

The element is a unit. It has the repeated eigenvalue $Q_t$, the minimal polynomial $(X-Q_t)^2$, a two-dimensional eigenspace $\ker L_{\vec\Upsilon}$, and no eigenbasis. The exponential is a phase and a scale at rate $Q_t$, multiplied by a drift linear in $\theta$.

**Interpretation 1: a defective resonance and a secular drift.** The exponential $e^{\theta Q_t}(e_t+\theta\vec Q)$ is the algebraic form of a **double pole in the mode sum**: a mode whose amplitude grows linearly in the flow parameter on top of its phase. In the non-Hermitian language it is the Jordan-block dynamics of an exceptional point, the $t e^{-i\omega t}$ term that appears when two resonances coalesce. The physical interpretation is a **defective resonance**: one frequency, one eigenline, and a secular term.

**Boundary.** The flow is the exponential of the element, not a solution of a specified equation of motion. The linear growth is algebraic; a physical secular term needs a driving, an initial condition or a non-Hermitian Hamiltonian, and the algebra supplies none of them.

**Interpretation 2: two coalesced modes with locked hands.** In the matrix model the element has one eigenline and one generalised eigenvector; the two modes have the same complex frequency and are coupled one way. The physical interpretation is a **clock with locked hands**: the two hands have the same rate and cannot be separated, because the second is not an eigenvector. The Petermann factor of the pair diverges as the coalescence is approached, which is the quantitative form of the locking.

**Boundary.** The interpretation needs a non-Hermitian description. No Hermitian element and no real-vector element lies on the stratum: for a Hermitian $H$, $B^2=-\lvert\vec h\rvert^2$ vanishes only at $\vec h=0$, which is the scalar line; for a real vector part, $B^2=\lvert\vec Q\rvert^2$ vanishes only at $\vec Q=0$. The stratum is complex.

**Interpretation 3: reversible but not normal.** The element is a unit, so its action can be undone; it is not diagonalisable, so it has no orthogonal eigenbasis. The physical interpretation is a **reversible process with no normal mode basis**: the inverse exists, and it is defective too, $Q_t^{-1}(e_t-\vec\Upsilon)$. Reversibility is not diagonalisability.

**Boundary.** Invertibility is an algebraic property. A physical process described by the element can still be dissipative when the complex scalar $Q_t$ has a real part, and the word *reversible* then refers to the algebraic inverse, not to the thermodynamics of the process.

**Interpretation 4: a null field with an amplitude and a phase.** The scalar $Q_t$ is a complex amplitude and phase; the nilpotent direction $\vec\Upsilon$ is the null polarization. The element is a **null-polarized plane wave with an amplitude**: a classical radiation field with a complex scalar prefactor, one eigenvalue, and no rest frame. The nilpotent stratum is the same wave at zero scalar; the unipotent stratum is the wave with its amplitude turned on.

**Boundary.** The amplitude is a complex scalar, not an intensity; the phase is not a gauge phase; the field is complex-pure plus a scalar, not a general field. The identification of $Q_t$ with an amplitude is an interpretation of the scalar coefficient, not a normalization of the field.

**Interpretation 5: the generator exists.** The logarithm is

$$
\operatorname{Log}\tilde Q=\operatorname{Log}Q_t\,e_t+\frac{\vec Q}{Q_t},
$$

on the principal branch. The unipotent element has a generator; the nilpotent does not, because it is not a unit. The physical interpretation is that a **reversible defective process has a generator**, while a non-invertible one has none.

**Boundary.** The logarithm is defined up to the branches of the logarithm; the branch matters, and the formula is the principal branch. The existence of a generator is algebraic; it does not supply a physical Hamiltonian.

### No Two-Term Spectral Decomposition on the Cone

On the nilpotent and unipotent strata the centraliser of $\tilde Q$ is the algebra of dual numbers,

$$
\mathbb{C}[\tilde Q]=\left\{ae_t+b\vec Q\right\},
$$

and its only idempotents are $0$ and $e_t$. A two-term spectral decomposition needs two non-trivial orthogonal idempotents summing to $e_t$; there are none. The spectrum is a single number, the one-term writing $\tilde Q=Q_te_t$ exists only on the scalar line, and the Born rule has nothing to project on. On the scalar line the centraliser is the whole algebra, but the element is central: every idempotent commutes with it, and the spectral decomposition is the one-term writing with $e_t$.

The idempotents outside the centraliser are the **Peirce idempotents**

$$
e_b=e+b\vec Q,
\qquad
f_b=e_t-e_b,
\qquad
b\in\mathbb{C},
$$

where $e$ is a rank-one idempotent with $e\vec Q=\vec Q$ and $\vec Qe=0$. They satisfy $e_b^2=e_b$, $e_bf_b=0$, $e_b+f_b=e_t$, and they give the Peirce form

$$
e_b\tilde Qe_b=Q_te_b,
\qquad
e_b\tilde Qf_b=\vec Q,
\qquad
f_b\tilde Qe_b=0,
\qquad
f_b\tilde Qf_b=Q_tf_b
$$

on the unipotent stratum, with $Q_t=0$ on the nilpotent one. The family is affine, the corner line rotates with $b$, and the choice of $e$ — equivalently, the scale of the corner vector — is a second parameter. The two parameters are a **gauge**.

**Interpretation.** A defective element does not select a state basis. The Peirce pair $(e_b,f_b)$ is a choice of **polarization** or of **detector**: every choice gives the same element and the same flag, and none is selected by the element. The physical statement is the flag, not the basis. The two-parameter family is the freedom of the polarization frame.

**Boundary.** *No two-term spectral decomposition* does not mean *no idempotent*. On the defective strata the Peirce idempotents exist; they are not spectral idempotents, they do not commute with $\tilde Q$, and they are not eigenstates of the element. They are nevertheless non-trivial idempotents: every non-trivial idempotent of the algebra has $N=0$ and $B^2=-\tfrac14$, so every one lies on $\Sigma_{01}$, the spectrally regular part of the null cone, not on $\mathcal S$. The Peirce idempotents are pure states of the algebra in this sense, but they are not states of the element. The spectral cone is not the idempotent locus.

### The Two Sides and the Absence of a Simultaneous Basis

The left and right actions commute, and on the cone they share very little. The common eigenspace is the single line

$$
\ker L_{\vec N}\cap\ker R_{\vec N}=\mathbb{C}\vec N
\quad\text{(nilpotent)},
\qquad
\ker\left(L_{\tilde Q}-Q_t\right)\cap\ker\left(R_{\tilde Q}-Q_t\right)=\mathbb{C}\vec\Upsilon
\quad\text{(unipotent)}.
$$

The left action has a two-dimensional eigenspace, the right action has a two-dimensional eigenspace, and their intersection is one line. A simultaneous eigenbasis would need four common eigenvectors; there is one.

**Interpretation.** The two mode spaces of the defective element share only the null direction. There is no biorthogonal mode basis either: the biorthogonal construction needs two distinct eigenprojections, and they do not exist. The physical interpretation is that a defective element has **two flags and one line**, not two bases.

**Boundary.** The two-sided action does not repair the defect. It gives a second flag and a second Peirce family, and it leaves the eigenbasis absent. The biorthogonal interpretation of *Biorthogonal Quantum Mechanics and the Biquaternion Spectrum* is licensed on $B^2\neq0$; on the cone it has no eigenprojectors to use.

## Physical Interpretations

- **Spectral regularity is the mode picture.** Two distinct eigenvalues, two invariant two-dimensional subspaces, a normal-mode frame, and a unique expansion of every element. The interpretation is a two-mode system with a non-zero complex splitting.
- **The splitting is the gap.** $\lambda_+-\lambda_-=2iB$. In the Hermitian sector the gap is $2\lvert B\rvert$; in the material sector $B$ is the momentum magnitude; in a normal element with complex $B$ it is a complex half-gap with an orthogonal eigenbasis, in a non-normal element it is a complex half-splitting with biorthogonal modes, and a normal element with real $B$ has a real half-gap and carries its damping in $Q_t$.
- **The spectrum is the Fourier spectrum.** The eigenvalues are the two character exponents of the flow, the eigenbasis is the Fourier basis of the root $\rho=\vec Q/B$, and $B$ is the rate relative to that root. The regular element supplies the root that the Fourier transform otherwise postulates.
- **The two-term writing is the mode decomposition.** The element is a sum of two spectral components; the terms are not two particles, two energies or an antiparticle pair. The sum of their coefficients is twice the scalar part and the product of their coefficients is the norm.
- **The eigenbasis is a frame attached to the element.** The two eigenspaces are unique, and the normalised Peirce vectors are unique; without that normalisation, the vectors inside each eigenspace are a gauge. The frame is not a laboratory frame.
- **Spectral regularity is not invertibility.** A massless element has a mode basis and is a zero divisor; a unipotent element is a unit and has no mode basis. The two conditions are independent.
- **The regular set is generic.** The spectral cone is a complex hypersurface of real codimension two; a generic element has a mode basis, and a degeneracy needs two real conditions.
- **The scalar line is a pure rate.** A central element is a global phase and a scale, a rest frame and a time-only displacement, a trivial observable or the maximally mixed state, and a superselection charge. Every basis is an eigenbasis, and none is preferred.
- **The nilpotent stratum is a null shift.** A pure isotropic element is a null field, a null translation, a zero-frequency one-way coupling, and a flag. It has no frequency and no eigenbasis.
- **The unipotent stratum is a rate with a shear.** A non-zero scalar times a null shift is a defective resonance with a secular drift, two coalesced modes with locked hands, a reversible process with no normal mode basis, and a null wave with an amplitude and a phase. It has a generator and no eigenbasis.
- **The cone has no two-term spectral decomposition.** The only spectral decomposition on it is the one-term writing with $e_t$ on the scalar line; elsewhere there is none. The Peirce idempotents are a two-parameter gauge, not an eigenbasis. The pure states lie on the spectrally regular part of the null cone, not on the spectral cone.
- **The cone is the non-oscillating regime.** At $B=0$ the root disappears, the exponential degenerates to the dual-number kernel $e^{\theta Q_t}(e_t+\theta N)$, and the characters have nilpotent deviation: there is no oscillation and no Fourier basis attached to the element.
- **The defective element has a flag, not a basis.** The left and right actions share only the null line; there is no simultaneous eigenbasis and no biorthogonal mode basis.
- **The algebra gives normal forms, not dynamics.** The interpretations locate the physical object; they do not supply an equation of motion, a particle content or a mass spectrum.

## Limits

The article reads one element at one point. It does not supply a dynamics, an equation of motion, a Lagrangian or a time evolution; the flow $e^{\theta L_{\tilde Q}}$ is the one-parameter group of the operator, and its parameter is a physical time only after a sector-dependent identification.

The article does not count particles. The two terms of the regular writing are spectral components of one element; the two eigenvalues are not two energies; the zero eigenvalue of a massless element is a spectral direction, not a second particle.

The article does not derive a mass, a spin or a coupling. The norm is read as the mass shell in the material sector, but the numerical mass is an input; the spinor doubling is the module structure, not a spin value; the strata are normal forms, not a particle classification.

The interpretations are sector-dependent. The same element can be read as an observable, as a four-momentum or as a general non-Hermitian generator, and the three interpretations use different dictionaries. The algebra supplies the common structure; it does not choose the dictionary.

The algebra is complex. The real material and informational sectors are slices, and the exceptional points, the nilpotent stratum and the unipotent stratum need complex coefficients. A physical interpretation that requires a real slice cannot use the whole cone.

The cone carries no non-trivial probability rule. Off the scalar line there are no two orthogonal spectral idempotents, so the Born rule has nothing to project on; on the scalar line every idempotent is spectral, but all outcomes are the same, so the rule is trivial. The biorthogonal rule needs $B^2\neq0$. The Peirce idempotents are a gauge, not a measurement.

*Generic* is an algebraic word. The regular set is open and dense in the algebra, but the cone is physically important: the rest frame, the null field and the exceptional point all lie on it or on its relatives. A thin set is not a negligible set.

The article does not claim that the three strata exhaust the physics of the cone. They exhaust the normal forms of the element. A physical system can approach a stratum along a family, and the family, the rate and the direction are extra data.

## Summary

- The spectral condition is $B^2=(\vec Q,\vec Q)\neq0$; the eigenvalues are $\lambda_\pm=Q_t\pm iB$, and they coincide exactly when $B^2=0$.
- The condition is operator-linked: $L_{\tilde Q}=Q_t\,\mathrm{id}+L_{\vec Q}$ and $L_{\vec Q}^2=-B^2\,\mathrm{id}$, so the directional part is a complex structure for $B^2\neq0$ and a nilpotent for $B^2=0$.
- For $B^2\neq0$ there are two invariant two-dimensional subspaces, two distinct complex frequencies, two eigenspaces of dimension two and an eigenbasis.
- The two-term writing is the mode decomposition; the terms are spectral components, not two particles; the sum of their coefficients is twice the scalar part and the product of their coefficients is the norm.
- The eigenbasis is unique as a pair of eigenspaces and unique as a normalised Peirce basis; the vectors inside each eigenspace are a gauge.
- The regular case is the harmonic case: $e^{\theta\tilde Q}=e^{\theta Q_t}W(-\theta,B/2\pi)$ with the root $\rho=\vec Q/B$, the eigenbasis is a root-adapted Fourier basis, and the eigenvalues are the two character exponents of the flow. On the cone there is no root, and the kernel degenerates to the dual-number form $e^{\theta Q_t}(e_t+\theta\vec N)$.
- The Hermitian norm of the flow separates three independent data: the scalar rate $\operatorname{Re}Q_t$ (damping), the imaginary half-gap $\operatorname{Im}B$ (boost), and the norm deficit $\lVert\rho\rVert_E^2-1$ (non-normality, an amplitude). Non-normality is not a damping mechanism.
- The unique eigenbasis exists exactly on the spectrally regular part $B^2\neq0$; on the spectral cone there is no eigenbasis on the nilpotent and unipotent strata, and on the scalar line every basis is an eigenbasis but none is attached to the element.
- Spectral regularity and invertibility are independent: a massless element has a mode basis and is a zero divisor; a unipotent element is a unit and has no mode basis.
- For $B^2\neq0$ the regular set is open and dense, and the spectral cone is a complex hypersurface of real codimension two.
- For $B^2=0$ the operator is $Q_t\,\mathrm{id}+N$ with $N^2=0$, and there are three strata: the scalar line, the nilpotent stratum and the unipotent stratum.
- The scalar line is a pure rate: a global phase and a scale, a rest frame and a time-only displacement, a trivial observable or the maximally mixed state, and a superselection charge. Every basis is an eigenbasis.
- The nilpotent stratum is a null shift: a null field, a null translation, a zero-frequency one-way coupling and a flag. It has no frequency and no eigenbasis.
- The unipotent stratum is a rate with a shear: a defective resonance with a secular drift, two coalesced modes with locked hands, a reversible process with no normal mode basis, and a null wave with an amplitude and a phase. It has a generator and no eigenbasis.
- The cone has no two-term spectral decomposition; the only spectral decomposition on it is the one-term writing with $e_t$ on the scalar line. The Peirce idempotents are a two-parameter gauge, not an eigenbasis; the pure states lie on the spectrally regular part of the null cone.
- The defective element has two flags and one common line, not two bases.
- The algebra gives normal forms, not dynamics, particle content or a mass spectrum.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde Q=Q_te_t+\vec Q$ | a general biquaternion, $Q_t\in\mathbb{C}$, $\vec Q\in\mathbb{C}^3$ |
| $(\vec X,\vec Y)$ | the complex bilinear form $X_xY_x+X_yY_y+X_zY_z$ on the vector part |
| $B^2=(\vec Q,\vec Q)$ | the vector-part square; the discriminant is $-4B^2$ |
| $B$ | a fixed complex square root of $B^2$; the other root exchanges the eigenvalues |
| $\lambda_\pm=Q_t\pm iB$ | the two eigenvalues |
| $N=Q_t^2+B^2$ | the quaternionic norm; $N=0$ is the null cone |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\Sigma_{ij}$ | the sector with $N\neq0$ if $i=1$ and $B^2\neq0$ if $j=1$ |
| $L_{\tilde Q}$, $R_{\tilde Q}$ | left and right multiplication by $\tilde Q$ |
| $J_{\tilde Q}=L_{\vec Q}/B$ | the internal complex structure, defined for $B^2\neq0$ |
| $\rho=\vec Q/B$ | the pure root of $-1$ of the regular case, $\rho^2=-e_t$ |
| $\lVert\rho\rVert_E^2=\sum_k\lvert\rho_k\rvert^2$ | Euclidean square of the root, $\ge1$; not the bilinear form $(\rho,\rho)=-1$ |
| $W(t,\omega)=\exp(-2\pi\rho\omega t)$ | the biquaternion Fourier kernel |
| $N_{\tilde Q}=L_{\vec Q}$ | the nilpotent part of the operator, $N_{\tilde Q}^2=0$ when $B^2=0$ |
| $\vec\Xi=-i\vec Q/B$ | the root of $+1$ of the regular case, $\vec\Xi^2=e_t$ |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ | the spectral idempotents of the regular case |
| $\vec\Upsilon=\vec Q/Q_t$ | the nilpotent direction of the unipotent stratum |
| $e_b=e+b\vec Q$ | the Peirce idempotents of the defective strata, a gauge |
| $\operatorname{rank}L_{\tilde Q}$ | $4$ on the units, $2$ on the nilpotent stratum, $0$ at the origin |

## Further Reading

- [The Spectrum](../articles_maths/spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the criterion, the two cases, the three strata and the flag.
- [The Eigenbasis of a Spectrally Regular Biquaternion](../articles_maths/the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), for the normalised Peirce basis, the unique expansion and the spinor interpretation.
- [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html), for the spectrum, the eigenprojections and the matrix model.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors and the independence of the two conditions.
- [The N-Regular, Spectrally Regular Sector](../articles_maths/the-n-regular-spectrally-regular-sector.html), for the eigenbasis, the Peirce corners and the spinor structure of $\Sigma_{11}$.
- [The N-Regular, Spectrally Degenerate Sector](../articles_maths/the-n-regular-spectrally-degenerate-sector.html), for the unipotent stratum, its flag and its Peirce corners.
- [The N-Degenerate, Spectrally Regular Sector](../articles_maths/the-n-degenerate-spectrally-regular-sector.html), for the massless zero divisors and the one live mode of $\Sigma_{01}$.
- [The N-Degenerate, Spectrally Degenerate Sector](../articles_maths/the-n-degenerate-spectrally-degenerate-sector.html), for the nilpotent stratum and the origin of $\Sigma_{00}$.
- [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html), for the exponential and the logarithm in the defective regimes.
- [Biquaternion Continuous Harmonic Analysis](../articles_maths/biquaternion-continuous-harmonic-analysis.html), for the Fourier kernel, the root-adapted basis and the factorization into complex transforms.
- [Relations between the Biquaternion Exponential and the Fourier Kernel](../articles_maths/relations-between-the-biquaternion-exponential-and-the-fourier-kernel.html), for the exponential as the kernel at negative time, the root supplied by the element, the character exponents, the Hermitian norm of the flow and the exact unitarity criterion.
- [The Bochner Theorem for the Biquaternion Transform: the Hermitian Form and the Root](../articles_maths/the-bochner-theorem-for-the-biquaternion-transform-the-hermitian-form-and-the-root.html), for the unitarity criterion and the normal/non-normal root.
- [Dual-Numbers Harmonic Analysis](../articles_maths/dual-numbers-harmonic-analysis.html), for the non-oscillating characters of the nilpotent stratum.
- [Harmonic Analysis over Hypercomplex Systems](../articles_maths/harmonic-analysis-over-hypercomplex-systems.html), for the reduction to complex transforms and the degenerate systems.
- [Derivatives, Fields and Transforms](derivatives-fields-and-transforms.html), for the Fourier transform as a change of description and *the root is the clock*.
- [The Spectral Reading of a Four-Vector](the-spectral-reading-of-a-four-vector.html), for the four-momentum as the Doppler pair.
- [Exceptional Points and the Nilpotent Regime in the Biquaternion Spectrum](exceptional-points-and-the-nilpotent-regime-in-the-biquaternion-spectrum.html), for the defective strata as exceptional points and the $\sqrt{\epsilon}$ law.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the null cone, the massless spectrum and the null field.
- [The Square-Zero Element: Nilpotency as Mode, Differential and Supercharge](the-square-zero-element-nilpotency-as-mode-differential-and-supercharge.html), for the nilpotent as a fermionic mode and the nine interpretations.
- [Biorthogonal Quantum Mechanics and the Biquaternion Spectrum](biorthogonal-quantum-mechanics-and-the-biquaternion-spectrum.html), for the non-normal mode basis on the regular set.
- [The Exponential, the Logarithm and the Generator](the-exponential-the-logarithm-and-the-generator.html), for the generator of a defective but reversible process.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), for the material-sector dictionary and the rest frame.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the observable and state interpretations of the scalar line.
