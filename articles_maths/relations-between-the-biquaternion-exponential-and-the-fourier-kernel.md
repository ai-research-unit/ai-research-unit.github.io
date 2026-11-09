# __Relations between the Biquaternion Exponential and the Fourier Kernel__

## Introduction

Two constructions of the corpus meet at one formula: the exponential of a biquaternion and the Fourier kernel. The kernel is built from a root of $1$ and the scalar imaginary, and the exponential of an element carries a rate. The exponential, in *Biquaternion Elementary Functions*, is

$$
\exp(\tilde Q)=\exp(Q_t)\bigl(\cos B\,e_t+\sin B\,\vec U\bigr),
\qquad
\vec U=\frac{\vec Q}{B},
$$

for $\vec Q^2=B^2\neq0$. The Fourier kernel, in *Biquaternion Continuous Harmonic Analysis*, is

$$
W(t,\omega)=\exp(-2\pi i\,\tilde{Ζ}\,\omega t),
\qquad
\tilde{Ζ}^2=e_t,
$$

with $\tilde{Ζ}$ a root chosen once and for all. The two formulas agree once the root and the rate are identified. The element supplies the root, and its rate $B$ is the angular frequency of the kernel.

**The dictionary is stated in roots of $1$.** A spectrally regular element supplies a root of its own, $\tilde{Ζ}=-i\vec Q/B$, and its exponential is the kernel at negative time and frequency $B/2\pi$:

$$
e^{\theta\tilde Q}=e^{\theta Q_t}\,W\!\left(-\theta,\frac{B}{2\pi}\right)
=e^{\theta Q_t}\bigl(\cos(B\theta)\,e_t+i\sin(B\theta)\,\tilde{Ζ}\bigr).
$$

The root is pure, the scalar $i$ carries the sign, and the idempotents are the standard pair $\tilde\Pi_\pm=\tfrac12(e_t\pm\tilde{Ζ})$. The eigenvalues are the exponents of the two characters, the eigenbasis is a Fourier basis, and the spectral idempotents are the algebraic projections onto the two frequency components. The kernel article has to fix $\tilde{Ζ}$ by hand because the algebra has no preferred root; a regular element supplies one, and this is the precise sense in which the two theories meet.

**The root of $1$ is the whole gain.** A root of $-1$ hides the sign inside the element, and every statement then carries a factor of $i$ that has to be tracked. Here the element carries only the square $e_t$, the sign sits in the scalar, and three results fall out without a case distinction: the idempotent pair is $\tfrac12(e_t\pm\tilde{Ζ})$ with no $i$, the transverse eigenvectors are $\tfrac12(\nu\pm\zeta)$ with no $i$ and no nilpotent, and the isometry criterion of the transform is exactly the normality criterion of the flow. What was a parametrised conic is a dichotomy, and what was a nilpotent pair is a pair of ordinary eigenvectors.

The article also corrects two identifications that the shared notation invites. **Normality is not unitarity.** A normal element has an orthogonal eigenbasis, but its flow need not have constant norm. And **a non-normal element does not necessarily grow**: its Hermitian norm oscillates between two bounds. Growth is produced by the central scalar part and by the imaginary part of $B$. The exact statements are in §*Normality, Unitarity and the Hermitian Norm of the Flow*.

The article proves the bridge, the kernel identity, the two unitarity criteria and the norm formula. The closed form of the exponential, the spectrum, the eigenbasis, the transform, its inversion and its Plancherel theorem are owned by the articles cited below, and none of them is reproved here.

## The Results It Uses

| Result | Source |
| --- | --- |
| The closed form of the exponential, the oscillatory and truncated regimes | [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), §*The Exponential* |
| The Hermitian norm of the flow, the norm deficit and the star-unitary and self-adjoint criteria | [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the Hermitian norm of the flow and the two criteria |
| The kernel as the exponential of a regular element | [Biquaternion Continuous Harmonic Analysis](biquaternion-continuous-harmonic-analysis.html), §*The Kernel as the Exponential of an Element* |
| The roots of $1$, the pure root and the Hermitian root | [Biquaternion Continuous Harmonic Analysis](biquaternion-continuous-harmonic-analysis.html), §*The Root of One* |
| The Fourier reading of the normalised Peirce basis | [The Eigenbasis of a Spectrally Regular Biquaternion](the-eigenbasis-of-a-spectrally-regular-biquaternion.html), §*The Fourier Reading of the Basis* |
| The truncated exponential on the spectral cone | [The Jordan Basis of a Spectrally Degenerate Biquaternion](the-jordan-basis-of-a-spectrally-degenerate-biquaternion.html), §*Multiplication, Inversion, and the Exponential* |
| The characteristic polynomial, the eigenvalues $Q_t\pm iB$ and the spectral criterion | [The Spectrum](the-spectrum.html), §*The Spectral Criterion* |
| The idempotents $\tilde\Pi_\pm$, the eigenspaces and the normalised Peirce basis | [The Eigenbasis of a Spectrally Regular Biquaternion](the-eigenbasis-of-a-spectrally-regular-biquaternion.html), §*The Eigenbasis* |
| Normality, the Hermitian projectors and the orthogonal spectral resolution | [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), §*The Hermitian Case* |
| The Fourier kernel, the root-adapted basis and the factorization into complex transforms | [Biquaternion Continuous Harmonic Analysis](biquaternion-continuous-harmonic-analysis.html), §*The Fourier Kernel* and §*Factorization into Complex Fourier Transforms* |
| The expansion of every biquaternion in the eigenbasis | [The Eigenbasis of a Spectrally Regular Biquaternion](the-eigenbasis-of-a-spectrally-regular-biquaternion.html), §*Expansion of Every Biquaternion* |
| The halving map and the Peirce coordinates | [Special Element and Peirce Conventions](special-element-and-peirce-conventions.html), §*The Peirce Coordinates* |
| The conjugations $\natural$ and $*$ | [Conventions in Mathematics](algebra-and-element-conventions.html), §*The Conjugations* |

The table is the contract: every statement below is either an identity proved here or a restatement of one of these rows.

## The Two Objects

### The Exponential

For one element the powers commute, so the exponential is computed in the commutative subalgebra $\mathbb{C}[\tilde Q]$ generated by $\tilde Q$. The definition by the series and the two regimes are those of *Biquaternion Elementary Functions*, §*The Exponential*. Two facts are used below.

For $B^2\neq0$ and every $\theta\in\mathbb{C}$,

$$
e^{\theta\tilde Q}
=e^{\theta Q_t}\bigl(\cos(B\theta)\,e_t+\sin(B\theta)\,\vec U\bigr),
\qquad
\vec U=\frac{\vec Q}{B}.
$$

For $B^2=0$, with $\vec N=\vec Q$ and $\vec N^2=0$,

$$
e^{\theta\tilde Q}=e^{\theta Q_t}\bigl(e_t+\theta\vec N\bigr).
$$

The first is the oscillatory regime and the second is the truncated regime. The scalar case $\vec Q=0$ is the common degenerate case, in which the exponential is the ordinary complex exponential of $Q_t$.

**The flow.** For a fixed $\tilde Q$, the map $\theta\mapsto e^{\theta\tilde Q}$ is the one-parameter flow generated by $\tilde Q$. Its parameter is a complex number, and it is not a time until a dynamics identifies it with one. The article uses the word *flow* for this map and *kernel* for $W$, and it does not identify the two parameters beyond the identity proved in §*The Kernel Identity*.

### The Fourier Kernel

Fix a root of $1$, that is, an element with $\tilde{Ζ}^2=e_t$. The kernel of *Biquaternion Continuous Harmonic Analysis*, §*The Fourier Kernel*, is

$$
W(t,\omega)=\exp(-2\pi i\,\tilde{Ζ}\,\omega t).
$$

Because $\tilde{Ζ}^2=e_t$, the series collapses to

$$
W(t,\omega)=\cos(2\pi\omega t)\,e_t-i\sin(2\pi\omega t)\,\tilde{Ζ},
$$

and the inverse is $W(t,\omega)^{-1}=\cos(2\pi\omega t)\,e_t+i\sin(2\pi\omega t)\,\tilde{Ζ}=W(t,-\omega)$. The transform uses real $t$ and $\omega$. Both sides are entire in $(t,\omega)$ and agree on $\mathbb{R}^2$, so the identity holds for complex values as well; the transform itself uses the real ones.

**The root is chosen, not found.** The article fixes $\tilde{Ζ}$ because the algebra has none. The roots of $1$ are the central pair $\pm e_t$ and the pure elements $\vec{Ζ}$ with $(\vec{Ζ},\vec{Ζ})=-1$, and the classification is that of *Biquaternion Continuous Harmonic Analysis*, §*The Root of One*. The two families give two transforms, and the family decides whether the kernel is a complex scalar or a genuine biquaternion.

**The root the element supplies is always pure.** The root $\tilde{Ζ}=-i\vec Q/B$ is a complex multiple of $\vec Q$, so it has no scalar part, and the central pair is therefore never the root of a regular element. The dictionary always lands in the pure family, and the exceptional case of the transform is never the one a regular element supplies.

### The Root the Element Supplies

**Proposition 1 (the root).** Let $\tilde Q=Q_te_t+\vec Q$ with $B^2=(\vec Q,\vec Q)\neq0$, and fix a square root $B$ of $B^2$. Then

$$
\tilde{Ζ}=-\frac{i\vec Q}{B}
$$

is a pure root of $1$, and

$$
\tilde Q=Q_te_t+iB\,\tilde{Ζ}.
$$

*Proof.* The vector part squares to $\vec Q^2=-B^2e_t$ by the quaternion rule, so $\tilde{Ζ}^{2}=(-i)^{2}\vec Q^{2}/B^{2}=(-1)(-1)e_t=e_t$. The element $\tilde{Ζ}$ is a multiple of $\vec Q$, so its scalar part vanishes. The last identity is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=iB\tilde{Ζ}$.

**The two branches.** The other square root $-B$ gives $-\tilde{Ζ}$ and exchanges $\lambda_+$ with $\lambda_-$. The identities below are invariant under the exchange, since $\cos$ is even and $\sin$ is odd, and the branch is a labelling and not a datum of the algebra. The root depends on the element: two regular elements generally supply different roots, and §*Global versus Element-Attached* states what is and what is not canonical.

**The root is Hermitian exactly when the element is normal.** A pure root is Hermitian when its coefficients are purely imaginary, that is, when $\vec Q/B$ is real with a real $B$. That is the normality condition of §*Normality, Unitarity and the Hermitian Norm of the Flow*, so the criterion the transform states for its isometry and the criterion the algebra states for orthogonal diagonalisation are the same condition on the same element. This is the sharpest form of the bridge: §*The Plancherel Theorem* of *Biquaternion Continuous Harmonic Analysis* holds for exactly the flows that diagonalise orthogonally.

## The Dictionary

### The Spectrum as Two Frequencies

The characteristic polynomial and the spectral criterion are those of *The Spectrum*, §*The Spectral Criterion*:

$$
p_{\tilde Q}(X)=X^2-2Q_tX+Q_t^2+B^2=(X-Q_t-iB)(X-Q_t+iB),
\qquad
\lambda_\pm=Q_t\pm iB.
$$

The eigenvalues are central, so they are ordinary complex numbers. The noncommutativity of $\mathbb{B}$ does not make the frequencies operator-valued: the two frequency components are scalar characters of the flow. The idempotents are the Lagrange idempotents of the two eigenvalues, and in the root of $1$ they take the standard form

$$
\tilde\Pi_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp}
=\frac12\bigl(e_t\pm\tilde{Ζ}\bigr),
$$

the second expression following from $\tilde Q-\lambda_\mp e_t=iB\tilde{Ζ}\pm iB e_t$ and $\lambda_+-\lambda_-=2iB$. They satisfy

$$
\tilde\Pi_\pm^2=\tilde\Pi_\pm,
\qquad
\tilde\Pi_+\tilde\Pi_-=0,
\qquad
\tilde\Pi_++\tilde\Pi_-=e_t,
\qquad
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_- .
$$

No factor of $i$ enters the idempotents, and no sign has to be watched: $\tilde\Pi_+$ is the projection on the eigenvalue $Q_t+iB$ and $\tilde\Pi_-$ on $Q_t-iB$, and the root is their difference, $\tilde{Ζ}=\tilde\Pi_+-\tilde\Pi_-$.

The spectral form of the exponential is therefore

$$
e^{\theta\tilde Q}
=e^{\theta\lambda_+}\tilde\Pi_++e^{\theta\lambda_-}\tilde\Pi_-
=e^{\theta Q_t}\bigl(e^{iB\theta}\tilde\Pi_++e^{-iB\theta}\tilde\Pi_-\bigr).
$$

The two terms are the two **characters** of the flow: on the eigenspace $E_\pm=\tilde\Pi_\pm\mathbb{B}$ left multiplication by $e^{\theta\tilde Q}$ is the scalar character $\theta\mapsto e^{\theta\lambda_\pm}$. The two frequencies coincide exactly when $B=0$: that is the spectral cone, treated in §*The Cone*. The gap is $\lambda_+-\lambda_-=2iB$, central, and purely imaginary exactly when $B$ is real.

### The Kernel Identity

**Theorem (the dictionary).** Let $B^2\neq0$, let $\tilde{Ζ}=-i\vec Q/B$, and let $\theta\in\mathbb{C}$. Then

$$
e^{\theta\tilde Q}
=e^{\theta Q_t}\,W\!\left(-\theta,\frac{B}{2\pi}\right)
=e^{\theta Q_t}\,W\!\left(\theta,-\frac{B}{2\pi}\right).
$$

*Proof.* By the closed form of the kernel,

$$
W\!\left(-\theta,\frac{B}{2\pi}\right)
=\exp\!\left(-2\pi i\,\tilde{Ζ}\,\frac{B}{2\pi}\,(-\theta)\right)
=\exp\bigl(iB\theta\,\tilde{Ζ}\bigr),
$$

and $\exp(iB\theta\tilde{Ζ})=\cos(B\theta)e_t+i\sin(B\theta)\tilde{Ζ}$ because $(iB\theta\tilde{Ζ})^{2}=-B^{2}\theta^{2}e_t$. Multiplying by $e^{\theta Q_t}$ and comparing with the closed form of §*The Exponential* gives the identity. The second form follows because $W(t,-\omega)=W(-t,\omega)$.

**In Peirce coordinates the identity is two lines.** Substituting the Peirce form of the kernel, $W(t,\omega)=e^{-2\pi i\omega t}\tilde\Pi_++e^{2\pi i\omega t}\tilde\Pi_-$, and the Peirce form of the flow, the identity becomes

$$
e^{\theta(Q_t+iB)}\,\tilde\Pi_+ + e^{\theta(Q_t-iB)}\,\tilde\Pi_-
= e^{\theta Q_t}\left(e^{iB\theta}\,\tilde\Pi_+ + e^{-iB\theta}\,\tilde\Pi_-\right),
$$

which is the same identity twice on the two ideals, with the frequencies $B/2\pi$ and $-B/2\pi$. The root drops out of the computation entirely, and what remains is the classical statement that the two characters of a complex flow of one frequency are the kernel read at that frequency and its negative.

**The signs.** The flow is the kernel at negative time and positive frequency, or at positive time and negative frequency. The two flips are the two conventions for the sign of the exponent, and the identity is one statement written twice. A reader who reverses the sign of the kernel reverses $\omega$ and keeps the identity.

**The period.** The map $\theta\mapsto W(-\theta,B/2\pi)$ has period $2\pi/B$, since $\exp(2\pi i\tilde{Ζ})=e_t$. For real $B$ this is the ordinary period $2\pi/\lvert B\rvert$ of the oscillation; for complex $B$ it is a complex period, and the flow is periodic as a map of the complex plane.

The dictionary is collected in one table.

| Flow | Kernel |
| --- | --- |
| flow parameter $\theta$ | time $t=-\theta$ |
| rate $B$ | angular frequency $2\pi\omega$ |
| frequency $B/2\pi$ | frequency $\omega$ |
| root $\tilde{Ζ}=-i\vec Q/B$ | root $\tilde{Ζ}$ of $1$ |
| eigenvalue $\lambda_\pm=Q_t\pm iB$ | character exponent |
| idempotent $\tilde\Pi_\pm=\tfrac12(e_t\pm\tilde{Ζ})$ | algebraic projection onto one frequency component |
| eigenspace $E_\pm=\tilde\Pi_\pm\mathbb{B}$ | one of the two invariant planes |
| $\cos(B\theta)e_t+i\sin(B\theta)\tilde{Ζ}$ | $W(t,\omega)$ |

The table is a dictionary and not an identification of two objects. The flow is one element's one-parameter group; the kernel is the generating function of a transform. The identity says that the first is a value of the second, and that the value carries the element's own root and rate.

### The Eigenbasis Is a Fourier Basis

The transform is computed in a root-adapted basis. Take $\tilde{Ζ}$ pure, so $(\tilde{Ζ},\tilde{Ζ})=-1$, and choose pure $\nu$ and $\zeta$ with

$$
(\tilde{Ζ},\nu)=(\nu,\zeta)=(\zeta,\tilde{Ζ})=0,
\qquad
\tilde{Ζ}\nu=\zeta,
\qquad
\tilde{Ζ}\zeta=\nu ,
$$

where the pairing is the complex bilinear form of the vector part and the last identity is $\tilde{Ζ}^{2}\nu=\nu$. In the ordered basis $(e_t,\tilde{Ζ},\nu,\zeta)$ left multiplication by $\tilde{Ζ}$ is block diagonal, with the same two-by-two block on $(e_t,\tilde{Ζ})$ and on $(\nu,\zeta)$: the block sends $e_t$ to $\tilde{Ζ}$ and $\tilde{Ζ}$ to $e_t$, and it sends $\nu$ to $\zeta$ and $\zeta$ to $\nu$. Its eigenvalues are $\pm1$.

**Proposition 2 (the eigenbasis in the Fourier basis).** In the notation above,

$$
\tilde{Ζ}\tilde\Pi_\pm=\pm\tilde\Pi_\pm,
\qquad
\tilde{Ζ}u_\pm=\pm u_\pm,
\qquad
u_\pm=\frac12(\nu\pm\zeta),
$$

and $(\tilde\Pi_+,u_+,u_-,\tilde\Pi_-)$ is a basis of $\mathbb{B}$ in which $L_{\tilde Q}$ is diagonal, with the eigenvalues $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$.

*Proof.* The first identity is $\tilde{Ζ}(e_t\pm\tilde{Ζ})/2=(\tilde{Ζ}\pm e_t)/2=\pm(e_t\pm\tilde{Ζ})/2$. The second is $\tilde{Ζ}(\nu\pm\zeta)/2=(\zeta\pm\nu)/2=\pm(\nu\pm\zeta)/2$, using $\tilde{Ζ}\nu=\zeta$ and $\tilde{Ζ}\zeta=\nu$. The two vectors of the first block are independent, the two of the second block are independent, and the two planes are complementary because $(e_t,\tilde{Ζ},\nu,\zeta)$ is a basis (*Biquaternion Continuous Harmonic Analysis*, §*The Change of Basis*); so the four are a basis. Left multiplication by $\tilde Q$ is $Q_t\,\mathrm{id}+iB\,L_{\tilde{Ζ}}$, which gives the eigenvalues $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$.

**The eigenvectors are not nilpotent.** The old parameter, a root of $-1$, put the two transverse eigenvectors at the eigenvalues $\pm i$ and made them a nilpotent pair; the root of $1$ puts them at $\pm1$, so they are ordinary eigenvectors of a diagonalisable operator. The four lines are determined up to the reciprocal rescaling $(\mu,\mu^{-1})$ of *The Eigenbasis of a Spectrally Regular Biquaternion*, §*The Transverse-Vector Construction*, and the normalisation of that article fixes $\mu$; the pair above is one representative. The idempotents and the four lines are the same.

**The two cuts are transverse.** The Fourier factorization cuts $\mathbb{B}$ into the two planes $\operatorname{span}\{e_t,\tilde{Ζ}\}$ and $\operatorname{span}\{\nu,\zeta\}$, each of which carries both signs of the eigenvalue. The spectral decomposition cuts it into the two eigenspaces $E_+=\operatorname{span}\{\tilde\Pi_+,u_+\}$ and $E_-=\operatorname{span}\{u_-,\tilde\Pi_-\}$, each of which takes one line from each plane. Neither cut refines the other. The Fourier factorization keeps the two blocks and applies an ordinary complex transform to each; the spectral decomposition regroups the four lines by eigenvalue. The first computes the transform of a function, the second the flow of one element, and both use the same root.

### Which Frequency

The word *frequency* is exact in one case and a rate in the others, and the case is decided by $B$, not by normality.

| $B^2$ | $B$ | Flow | Name of $B/2\pi$ |
| --- | --- | --- | --- |
| real positive | real | ordinary oscillation, period $2\pi/\lvert B\rvert$ | frequency |
| real negative | purely imaginary | hyperbolic growth and decay | rapidity rate |
| non-real | genuinely complex | oscillation with an exponential envelope | complex rate |
| zero | zero | truncated, polynomial | none |

The two real forms give the first two rows. When the vector part is real, $B^2=\lvert\vec Q\rvert^2>0$ and the flow oscillates. When the vector part is purely imaginary, so $B^2=-\lvert\vec Q\rvert^2<0$ and the flow is hyperbolic. The general element has a genuinely complex $B$ and a frequency with an envelope. The element $(1+i)\vec e_x$ of §*Worked Examples* is normal and has a complex $B$: normality does not make the frequency real.

## The Two Conjugations

### Quaternion Conjugation

The quaternion conjugation $\natural$ fixes $e_t$ and sends every vector to its negative. For a pure root, $\tilde{Ζ}^\natural=-\tilde{Ζ}$. Because $\natural$ is complex linear and reverses the sign of the root,

$$
W(t,\omega)^\natural=\exp\left(2\pi i\,\tilde{Ζ}\,\omega t\right)=W(t,-\omega)=W(t,\omega)^{-1}.
$$

The kernel is therefore on the natural unit sphere identically, for every pure root and with no further condition. The flow carries the scalar factor, and the same computation gives

$$
\bigl(e^{\theta\tilde Q}\bigr)^\natural\bigl(e^{\theta\tilde Q}\bigr)=e^{2\theta Q_t}e_t,
$$

so the quaternionic norm of the flow is $N(e^{\theta\tilde Q})=e^{2\theta Q_t}$, in agreement with *Biquaternion Elementary Functions*, §*The Exponential*. The flow is quaternion-unitary for all $\theta$ exactly when $Q_t=0$.

### Hermitian Conjugation

The Hermitian conjugation is $*=\bar{\natural}$. For a pure root, $\tilde{Ζ}^*=-\bar{\tilde{Ζ}}$. Then

$$
W(t,\omega)^*=\exp\left(-2\pi i\,\bar{\tilde{Ζ}}\,\omega t\right),
\qquad
W(t,\omega)W(t,\omega)^*=\exp\bigl(-2\pi i(\tilde{Ζ}+\bar{\tilde{Ζ}})\omega t\bigr),
$$

and the kernel is $*$-unitary for the positive Hermitian form exactly when $\tilde{Ζ}+\bar{\tilde{Ζ}}=0$, that is, when the root is Hermitian. This is the criterion of *The Bochner Theorem for the Biquaternion Transform: the Hermitian Form and the Root*, §*Unitarity of the Character and the Root*, read on the root the element supplies.

**Proposition 3 (unitarity and self-adjointness of the flow).** Let $B^2\neq0$ and let $\theta$ be real. The following are equivalent:

- $e^{\theta\tilde Q}$ is $*$-unitary for the Hermitian form for every $\theta$;
- $\tilde Q^*=-\tilde Q$;
- $Q_t\in i\mathbb{R}$ and $\vec Q\in\mathbb{R}^3$.

The following are also equivalent:

- $e^{\theta\tilde Q}$ is self-adjoint for every $\theta$;
- $\tilde Q^*=\tilde Q$;
- $Q_t\in\mathbb{R}$ and $\vec Q\in i\mathbb{R}^3$.

*Proof.* If $E=e^{\theta\tilde Q}$ is $*$-unitary for every $\theta$, differentiating $EE^*=e_t$ at $\theta=0$ gives $\tilde Q+\tilde Q^*=0$. Conversely, if $\tilde Q^*=-\tilde Q$ then $E^*=e^{\theta\tilde Q^*}=e^{-\theta\tilde Q}=E^{-1}$. The equivalence with the coordinate conditions is the computation of $*$ on $Q_te_t+\vec Q$: the scalar part is conjugated and the vector part is negated and conjugated, so $\tilde Q^*=-\tilde Q$ means $\bar Q_t=-Q_t$ and $\overline{\vec Q}=\vec Q$. The self-adjoint case is the same computation with the opposite signs.

The first family is the real one and the second is the Hermitian one. Unitarity is strictly stronger than normality, because $\tilde Q^*=-\tilde Q$ implies $\tilde Q\tilde Q^*=\tilde Q^*\tilde Q$; the converse fails.

### Normality, Unitarity and the Hermitian Norm of the Flow

The normality theorem is that of *The Biquaternion Eigenvalue Decomposition*, §*The Hermitian Case*. For $B^2\neq0$, the following are equivalent:

- $\tilde Q$ is normal, $\tilde Q\tilde Q^*=\tilde Q^*\tilde Q$;
- $\vec Q\times\overline{\vec Q}=0$, with the complex bilinear cross product;
- $\operatorname{Re}\vec Q$ and $\operatorname{Im}\vec Q$ are parallel;
- the root $\tilde{Ζ}=-i\vec Q/B$ is Hermitian;
- $\tilde\Pi_\pm$ are Hermitian;
- $E_+$ and $E_-$ are orthogonal for the Hermitian form.

The criterion involves the vector part alone. The scalar part is free, and this is the first source of confusion: a normal element can have any complex rate $Q_t$.

**Corollary 1.** Normality does not imply unitarity. The element $\tilde Q=(1+i)\vec e_x$ is normal, since its root $\tilde{Ζ}=-i\vec e_x$ is Hermitian, but $\tilde Q^*\neq-\tilde Q$ and $\tilde Q^*\neq\tilde Q$. Its flow is neither $*$-unitary nor self-adjoint.

**Corollary 2.** Normality does not imply a constant norm. The same element has $\lvert B\rvert=\sqrt2$ and $\operatorname{Im}B=1$, and its Hermitian norm grows as $\cosh(2\theta)$.

**Corollary 3.** Non-normality does not imply growth. The element $\tilde Q=i\vec e_x+\vec e_y+\vec e_z$ has the root

$$
\tilde{Ζ}=-i\vec Q=\vec e_x-i\vec e_y-i\vec e_z,
$$

which is pure with $(\tilde{Ζ},\tilde{Ζ})=1-1-1=-1$, and it is not Hermitian, so the element is not normal. Its Hermitian norm is

$$
\bigl\langle e^{\theta\tilde Q}\bigr\rangle_*=\cos^2\theta+3\sin^2\theta=1+2\sin^2\theta,
$$

which oscillates between $1$ and $3$ and never grows.

The general formula is the following.

**Proposition 4 (the Hermitian norm of the flow).** Let $B^2\neq0$ and let $\theta$ be real. Put $\lVert\tilde{Ζ}\rVert^2=\sum_k\lvert\tilde{Ζ}_k\rvert^2$ over the four coordinates of the root. Then

$$
\bigl\langle e^{\theta\tilde Q}\bigr\rangle_*
=\lvert e^{\theta Q_t}\rvert^2
\left(\lvert\cos(B\theta)\rvert^2+\lvert\sin(B\theta)\rvert^2\,\lVert\tilde{Ζ}\rVert^2\right).
$$

*Proof.* Write $E=e^{\theta Q_t}(a e_t+b\tilde{Ζ})$ with $a=\cos(B\theta)$ and $b=i\sin(B\theta)$. Since $\tilde{Ζ}$ is pure, the scalar part of $\tilde{Ζ}\tilde{Ζ}^*$ is $\lVert\tilde{Ζ}\rVert^2e_t$ and the cross terms $a\bar b\tilde{Ζ}^*+b\bar a\tilde{Ζ}$ are pure vectors; hence the scalar part of $EE^*$ is $\lvert e^{\theta Q_t}\rvert^2(\lvert a\rvert^2+\lvert b\rvert^2\lVert\tilde{Ζ}\rVert^2)$.

**Proposition 5 (the norm deficit).** $\lVert\tilde{Ζ}\rVert^2\ge1$, with equality exactly when $\tilde{Ζ}$ is Hermitian, that is, exactly when $\tilde Q$ is normal. Writing the root in real and imaginary parts, $\tilde{Ζ}=\vec p+i\vec p'$, the deficit is $2\lVert\vec p\rVert^2$.

*Proof.* $\lvert B\rvert^2=\lvert B^2\rvert=\lvert\sum_kQ_k^2\rvert\le\sum_k\lvert Q_k\rvert^2$, with equality exactly when the non-zero squares $Q_k^2$ have one argument. Dividing by $\lvert B\rvert^2$ gives the inequality, since $\lVert\tilde{Ζ}\rVert^2=\lVert\vec Q\rVert^2/\lvert B\rvert^2$. If the arguments agree, $Q_k=\varkappa_{\mathrm{phs}} r_k$ with $r_k\in\mathbb{R}$, so $B=\pm\varkappa_{\mathrm{phs}}R$ with $R^2=\sum_kr_k^2$ and the root is Hermitian; the converse is immediate. The second form of the deficit follows from $(\tilde{Ζ},\tilde{Ζ})=\lVert\vec p\rVert^2-\lVert\vec p'\rVert^2=-1$.

The three quantities $Q_t$, $B$ and $\lVert\tilde{Ζ}\rVert^2$ govern the norm independently.

| Quantity | Role in $\langle e^{\theta\tilde Q}\rangle_*$ | Condition for its neutral value |
| --- | --- | --- |
| $\operatorname{Re}Q_t$ | dilation rate $e^{2\theta\operatorname{Re}Q_t}$ | $\operatorname{Re}Q_t=0$ |
| $\operatorname{Im}B$ | envelope rate, growth as $e^{2\lvert\operatorname{Im}B\rvert\lvert\theta\rvert}$ | $B$ real |
| $\lVert\tilde{Ζ}\rVert^2$ | oscillation amplitude, $\ge1$ | $\lVert\tilde{Ζ}\rVert^2=1$, i.e. normal |

**Corollary 4 (bounded and unbounded flows).** If $B$ is real and $\operatorname{Re}Q_t=0$, the Hermitian norm is bounded between $1$ and $\lVert\tilde{Ζ}\rVert^2$. If $\operatorname{Re}Q_t\neq0$, it is unbounded on one side. If $\operatorname{Im}B\neq0$, it is unbounded on both sides.

A non-normal element has a larger oscillation amplitude, not a decay. A decay is a negative real part of $Q_t$ in the convention $e^{+\theta\tilde Q}$, and a boost is a non-zero imaginary part of $B$. The norm deficit measures how far the element is from normal, and it is an amplitude, not a rate.

## The Cone

### No Root, No Frequency

On the spectral cone $B^2=0$ the two eigenvalues coincide at $Q_t$ and the root $\tilde{Ζ}=-i\vec Q/B$ does not exist. Write $\vec N=\vec Q$. Then $\vec N^2=-B^2e_t=0$, so $\vec N$ is square-zero, and the operator is $L_{\tilde Q}=Q_t\,\mathrm{id}+L_{\vec N}$ with $L_{\vec N}^2=0$. There is no frequency to read off and no root to substitute in the kernel.

### The Truncated Kernel

The exponential is

$$
e^{\theta\tilde Q}=e^{\theta Q_t}\bigl(e_t+\theta\vec N\bigr),
$$

the dual-number exponential $e^{a+b\varepsilon}=e^a(1+b\varepsilon)$ in the algebra generated by $\vec N$, with $\varepsilon=\vec N$ and $b=\theta$. The model is the dual character of *Dual Numbers Harmonic Analysis*, §*The Dual Characters*: the exponential of a nilpotent is truncated, not oscillatory.

**The formula extends, the parametrisation does not.** Written without the root,

$$
e^{\theta\tilde Q}
=e^{\theta Q_t}\left(\cos(B\theta)\,e_t+\frac{\sin(B\theta)}{B}\,\vec Q\right),
$$

the right-hand side is entire in $B$ and its value at $B=0$ is $e^{\theta Q_t}(e_t+\theta\vec Q)$. The closed form therefore has a limit at the cone even though $B$ and $\tilde{Ζ}$ do not. The kernel $W(t,\omega)$ itself has no limit, because it is a function of a root that does not exist; the combination that the flow uses does.

### The Three Strata

The cone carries three normal forms, those of *The Jordan Basis of a Spectrally Degenerate Biquaternion*, §*The Three Strata*, and each has its own exponential.

| Stratum | Normal form | Exponential | Root | Eigenbasis |
| --- | --- | --- | --- | --- |
| scalar | $Q_te_t$ | $e^{\theta Q_t}e_t$ | none | every basis, none canonical |
| nilpotent | $\vec N$, $\vec N^2=0$ | $e_t+\theta\vec N$ | none | none |
| unipotent | $Q_t(e_t+\vec\Upsilon)$, $\vec\Upsilon^2=0$ | $e^{\theta Q_t}(e_t+\theta Q_t\vec\Upsilon)$ | none | none |

The scalar stratum is a central character with no direction. The nilpotent stratum is a null translation with no rate. The unipotent stratum is a scaled null translation: a rate and a shear, with no frequency. None of the three has a root of $1$, and none has an oscillatory character.

## Global versus Element-Attached

**What is canonical.** For a regular element, the pair of eigenspaces $\{E_+,E_-\}$ is unique, and the eigenvalues are determined up to the exchange of the two branches. The vectors inside each eigenspace are a gauge: multiplying a vector of $E_+$ by a non-zero scalar and a vector of $E_-$ by another leaves the eigenspaces unchanged. The normalised Peirce basis of *The Eigenbasis of a Spectrally Regular Biquaternion* fixes that gauge; the root-adapted basis of §*The Eigenbasis Is a Fourier Basis* fixes it differently.

**Every element expands in the basis of a given regular element.** The four vectors of Proposition 2 form a basis of $\mathbb{B}$, so every biquaternion has coordinates in it; the spectral decomposition of the given element is diagonal in those coordinates. This is the sense in which a regular element supplies a frame for the whole algebra — a frame attached to the element, not a frame of the algebra.

**No global eigenbasis.** A basis that diagonalized every $L_{\tilde Q}$ would make any two left multiplications diagonal in one basis, hence would make any two of them commute; then every two elements of $\mathbb{B}$ would commute, which is false. The obstruction is the noncommutativity, not the choice of root.

**No canonical root.** A non-central root of $1$ is moved by an inner automorphism: if $U$ is invertible then $U\tilde{Ζ}U^{-1}$ is again a root of $1$, and it differs from $\tilde{Ζ}$ unless $U$ commutes with $\tilde{Ζ}$. The central roots $\pm e_t$ are fixed by every inner automorphism, but they are not pure and no regular element supplies them. The algebra therefore has no root that is both canonical and available to the dictionary.

**On the cone.** The scalar line has every basis as an eigenbasis and none as a canonical one. The nilpotent and unipotent strata have no eigenbasis. The global statement is the one of the introduction: the eigenbasis exists on the open dense set $B^2\neq0$, is attached to the element, and is not canonical as a global object.

## Worked Examples

The table reads five elements through the dictionary. The last three columns record whether the flow is normal, $*$-unitary and self-adjoint.

| $\tilde Q$ | $B^2$, $B$ | $\tilde{Ζ}$ | $\lambda_\pm$ | $e^{\theta\tilde Q}$ | $\langle e^{\theta\tilde Q}\rangle_*$ | normal | $*$-unitary | self-adjoint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\vec e_x$ | $1$, $1$ | $-i\vec e_x$ | $\pm i$ | $\cos\theta\,e_t+\sin\theta\,\vec e_x$ | $1$ | yes | yes | no |
| $i\vec e_x$ | $-1$, $i$ | $-i\vec e_x$ | $\mp1$ | $\cosh\theta\,e_t+i\sinh\theta\,\vec e_x$ | $\cosh2\theta$ | yes | no | yes |
| $(1+i)\vec e_x$ | $2i$, $1+i$ | $-i\vec e_x$ | $\mp(1-i)$ | $\cos((1+i)\theta)e_t+\sin((1+i)\theta)\vec e_x$ | $\cosh2\theta$ | yes | no | no |
| $i\vec e_x+\vec e_y+\vec e_z$ | $1$, $1$ | $\vec e_x-i\vec e_y-i\vec e_z$ | $\pm i$ | $\cos\theta\,e_t+i\sin\theta\,\tilde{Ζ}$ | $1+2\sin^2\theta$ | no | no | no |
| $(1+i)e_t+\vec e_x$ | $1$, $1$ | $-i\vec e_x$ | $1\pm2i$ | $e^{(1+i)\theta}(\cos\theta\,e_t+\sin\theta\,\vec e_x)$ | $e^{2\theta}$ | yes | no | no |

The first two rows are the two real forms. The first is the case of real $B$: Hermitian root, $*$-unitary flow, constant norm. The second is the Hermitian case: imaginary $B$, the same Hermitian root, self-adjoint flow, hyperbolic norm. The root of $1$ makes the coincidence visible: the two rows share one root and differ in the sign of $B^{2}$ alone.

The third row is normal, with a Hermitian root, and is neither $*$-unitary nor self-adjoint; its $B$ is genuinely complex and its norm grows. It shows that normality is orthogonal diagonalisation and nothing more. The fourth row is not normal, its root is not Hermitian, and its norm oscillates between $1$ and $3$: non-normality is not a decay. The fifth row is normal and grows because of the scalar rate $Q_t=1+i$.

The kernel identity is visible in the first row: $e^{\theta\vec e_x}=W(-\theta,1/2\pi)$, since $Q_t=0$ and $B=1$. In the second row the same kernel with an imaginary frequency gives the hyperbolic form, because $\cos(i\theta)=\cosh\theta$ and $\sin(i\theta)=i\sinh\theta$.

**The cone.** Take $\vec N=\vec e_x+i\vec e_y$. Then $\vec N^2=(-1)+(-1)(i^2)=0$ and $e^{\theta\vec N}=e_t+\theta\vec N$. Adjoining a scalar, $\tilde Q=Q_te_t+\vec N$ gives $e^{\theta\tilde Q}=e^{\theta Q_t}(e_t+\theta\vec N)$. The element is unipotent when $Q_t\neq0$ and nilpotent when $Q_t=0$; the exponential is polynomial in both cases, and no root is available.

## The Boundary

The article states an algebraic dictionary. It does not supply a dynamics: $\theta$ is a flow parameter, and $B/2\pi$ is a rate of that flow, not the frequency variable of the transform, until an equation of motion identifies the two. The identification is not made here, and nothing below uses it.

It does not reprove the transform theory. Inversion, Plancherel, the convolution theorem and the vanishing-norm issue are those of *Biquaternion Continuous Harmonic Analysis*, and nothing in the dictionary decides them. The identity is pointwise in the element and does not commute with an integral.

It does not claim a canonical root or a global basis. The root is attached to the element, and §*Global versus Element-Attached* states the two obstructions: noncommutativity for a global basis, and the inner automorphisms for a canonical root.

It does not identify normality with unitarity, nor non-normality with damping. Proposition 3 gives the exact unitarity criterion, Proposition 4 the exact norm formula, and Proposition 5 the exact deficit. In particular the deficiency $\lVert\tilde{Ζ}\rVert^2-1$ is an amplitude, and the decay rate is $\operatorname{Re}Q_t$.

The sign convention is conventional. The theorem is stated with the exponent $+\theta\tilde Q$ and the kernel $e^{-2\pi i\tilde{Ζ}\omega t}$; the other convention flips both signs and leaves the content unchanged.

The cone is not a limit of the regular kernel in the ordinary sense. The closed form of the flow extends to $B=0$, and §*The Truncated Kernel* says exactly what extends and what does not: the formula extends, the root and the frequency do not.

## Summary

A regular element $\tilde Q=Q_te_t+\vec Q$ supplies the root $\tilde{Ζ}=-i\vec Q/B$ of the Fourier kernel, and its exponential is the kernel at negative time:

$$
e^{\theta\tilde Q}
=e^{\theta Q_t}\left(\cos(B\theta)e_t+i\sin(B\theta)\tilde{Ζ}\right)
=e^{\theta Q_t}W\!\left(-\theta,\frac{B}{2\pi}\right).
$$

The root of $1$ is what makes the dictionary exact. The idempotents $\tilde\Pi_\pm=\tfrac12(e_t\pm\tilde{Ζ})$ carry no scalar, the eigenvalues $\lambda_\pm=Q_t\pm iB$ are the character exponents, and the eigenbasis is diagonal in blocks of two. The Fourier factorization keeps the two invariant planes; the spectral decomposition regroups their four lines by eigenvalue; the two cuts are transverse.

The normality of the element, the Hermiticity of the root and the existence of an orthogonal eigenbasis are one condition, and it is the condition under which the transform of *Biquaternion Continuous Harmonic Analysis* is an isometry. Unitarity is stronger, and it is the condition $\tilde Q^*=-\tilde Q$. The norm of the flow is $\lvert e^{\theta Q_t}\rvert^{2}(\lvert\cos B\theta\rvert^{2}+\lvert\sin B\theta\rvert^{2}\lVert\tilde{Ζ}\rVert^{2})$, the deficit $\lVert\tilde{Ζ}\rVert^{2}-1$ is an amplitude and not a rate, and on the cone the root disappears while the closed form of the flow survives.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion, scalar part and vector part |
| $B^2=(\vec Q,\vec Q)$ | the squared vector part, a complex scalar |
| $B$ | a chosen square root of $B^2$ |
| $\vec U=\vec Q/B$ | the normalised vector part of the exponential |
| $\tilde{Ζ}=-i\vec Q/B$ | the root of $1$ the element supplies |
| $\vec{Ζ}$ | a pure root of $1$, $(\vec{Ζ},\vec{Ζ})=-1$ |
| $\vec p, \vec p'$ | the real and imaginary parts of $\vec{Ζ}=\vec p+i\vec p'$ |
| $\lambda_\pm=Q_t\pm iB$ | the two eigenvalues, central |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\tilde{Ζ})$ | the two spectral idempotents |
| $E_\pm=\tilde\Pi_\pm\mathbb{B}$ | the two eigenspaces |
| $W(t,\omega)=\exp(-2\pi i\tilde{Ζ}\omega t)$ | the biquaternion Fourier kernel |
| $\nu, \zeta$, $u_\pm=\tfrac12(\nu\pm\zeta)$ | the transverse basis of the root |
| $\lVert\tilde{Ζ}\rVert^2$ | the Euclidean square of the root, $\ge1$ |
| $\vec N$ | the square-zero vector part on the cone |
| $\natural$, $*=\bar{\natural}$ | quaternion and Hermitian conjugation |

## Further Reading

- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential, its two regimes and the Hermitian norm of the flow.
- [Biquaternion Continuous Harmonic Analysis](biquaternion-continuous-harmonic-analysis.html), for the kernel, the root of one, the Peirce factorization and the analytic theorems.
- [The Eigenbasis of a Spectrally Regular Biquaternion](the-eigenbasis-of-a-spectrally-regular-biquaternion.html), for the eigenbasis, the normalised Peirce basis and the Fourier reading of the basis.
- [The Spectrum](the-spectrum.html), for the characteristic polynomial and the spectral criterion.
- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), for the normality theorem and the orthogonal spectral resolution.
- [The Jordan Basis of a Spectrally Degenerate Biquaternion](the-jordan-basis-of-a-spectrally-degenerate-biquaternion.html), for the three strata of the cone.
- [Special Element and Peirce Conventions](special-element-and-peirce-conventions.html), for the root glyph, the halving map and the Peirce coordinates.
- [Idempotents](idempotents.html), for the idempotents of the biquaternion algebra and their classification.
- [The Bochner Theorem for the Biquaternion Transform: the Hermitian Form and the Root](the-bochner-theorem-for-the-biquaternion-transform-the-hermitian-form-and-the-root.html), for the unitarity criterion of the character.
- [Dual Numbers Harmonic Analysis](dual-numbers-harmonic-analysis.html), for the truncated character at the cone.
