# __Relations between the Biquaternion Exponential and the Fourier Kernel__

## Introduction

Two constructions of the corpus meet at one formula: the exponential of a biquaternion and the Fourier kernel. Each is built from a root of $-1$ and a rate. The exponential of an element, in *Biquaternion Elementary Functions*, is

$$
\exp(\tilde Q)=\exp(Q_t)\bigl(\cos B\,e_t+\sin B\,\vec U\bigr),
\qquad
\vec U=\frac{\vec Q}{B},
$$

for $\vec Q^2=B^2\neq0$. The Fourier kernel, in *Biquaternion Continuous Harmonic Analysis*, is

$$
W(t,\omega)=\exp(-2\pi\rho\,\omega t),
\qquad
\rho^2=-e_t,
$$

with $\rho$ a root chosen once and for all. The two formulas agree once the root and the rate are identified. The element supplies the root, and its rate $B$ is the angular frequency of the kernel.

The dictionary is exact. A spectrally regular element has a root of its own, $\rho=\vec Q/B$, and its exponential is the kernel at $t=-\theta$ and $\omega=B/2\pi$:

$$
e^{\theta\tilde Q}=e^{\theta Q_t}\,W\!\left(-\theta,\frac{B}{2\pi}\right).
$$

The eigenvalues are the exponents of the two characters, the eigenbasis is a Fourier basis, and the spectral idempotents are the algebraic projections onto the two frequency components. The kernel article has to fix $\rho$ by hand because the algebra has no preferred root; a regular element supplies one, and this is the precise sense in which the two theories meet.

The article also corrects two identifications that the shared notation invites. **Normality is not unitarity.** A normal element has an orthogonal eigenbasis, but its flow need not have constant norm. And **a non-normal element does not necessarily grow**: its Hermitian norm oscillates between two bounds. Growth is produced by the central scalar part and by the imaginary part of $B$. The exact statements are in §*Normality, Unitarity and the Hermitian Norm of the Flow*.

The article proves the bridge, the kernel identity, the two unitarity criteria and the norm formula. The closed form of the exponential, the spectrum, the eigenbasis, the transform, its inversion and its Plancherel theorem are owned by the articles cited below, and none of them is reproved here.

## The Results It Uses

| Result | Source |
| --- | --- |
| The closed form of the exponential, the oscillatory and truncated regimes | [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), §*The Exponential* |
| The Hermitian norm of the flow, the norm deficit and the unitary and self-adjoint criteria | [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), §*The Hermitian Norm and the Unitary Flow* |
| The kernel as the exponential of a regular element | [Biquaternion Continuous Harmonic Analysis](biquaternion-continuous-harmonic-analysis.html), §*The Kernel as the Exponential of an Element* |
| The Fourier reading of the normalised Peirce basis | [The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), §*The Fourier Reading of the Basis* |
| The truncated exponential on the spectral cone | [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), §*The Exponential on the Cone* |
| The characteristic polynomial, the eigenvalues $Q_t\pm iB$ and the spectral criterion | [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), §*The Spectral Criterion* |
| The idempotents $\tilde\Pi_\pm$, the eigenspaces and the normalised Peirce basis | [The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), §*The Eigenbasis* |
| Normality, the Hermitian projectors and the orthogonal spectral resolution | [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), §*The Hermitian Case* |
| The Fourier kernel, the root-adapted basis and the factorization into complex transforms | [Biquaternion Continuous Harmonic Analysis](biquaternion-continuous-harmonic-analysis.html), §*The Fourier Kernel* and §*Factorization into Complex Fourier Transforms* |
| The expansion of every biquaternion in the eigenbasis | [The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), §*Expansion of Every Biquaternion* |
| The three families of roots of $-1$ | [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), §*The Roots of Minus One* |
| The conjugations $\natural$ and $*$ | [Conventions in Mathematics](conventions-in-mathematics.html), §*The Conjugations* |

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

**The flow.** For a fixed $\tilde Q$, the map $\theta\mapsto e^{\theta\tilde Q}$ is the one-parameter flow generated by $\tilde Q$. Its parameter is a complex number, and it is not a physical time until a dynamics identifies it with one. The article uses the word *flow* for this map and *kernel* for $W$, and it does not identify the two parameters beyond the identity proved in §*The Kernel Identity*.

### The Fourier Kernel

Fix a root $\rho$ of $-1$, that is, an element with $\rho^2=-e_t$. The kernel of *Biquaternion Continuous Harmonic Analysis*, §*The Fourier Kernel*, is

$$
W(t,\omega)=\exp(-2\pi\rho\,\omega t).
$$

Because $\rho^2=-e_t$, the series collapses to

$$
W(t,\omega)=\cos(2\pi\omega t)\,e_t-\sin(2\pi\omega t)\,\rho,
$$

and the inverse is $W(t,\omega)^{-1}=\cos(2\pi\omega t)\,e_t+\sin(2\pi\omega t)\,\rho$. The transform uses real $t$ and $\omega$. Both sides are entire in $(t,\omega)$ and agree on $\mathbb{R}^2$, so the identity holds for complex values as well; the transform itself uses the real ones.

**The root is chosen, not found.** The article fixes $\rho$ because the algebra has none. The roots of $-1$ are the two central scalars $\pm i$, the pure real unit vectors $\pm\vec u$, and the genuinely biquaternionic roots $\rho=b\mu+d i\nu$ with $\mu\perp\nu$ real unit vectors and $b^2-d^2=1$; the classification is that of *Idempotents*. The transform changes with the family, and the choice of family is a choice of which imaginary direction is the frequency axis.

**The root the element supplies is always pure.** A root with a non-zero scalar part is $\pm i$, because the vector part of $\rho^2=-e_t$ is twice the scalar part times the vector part of $\rho$, and it vanishes. The root $\rho=\vec Q/B$ of a regular element is pure by construction. The dictionary therefore always lands in the pure-root families, and the exceptional central family of the transform is never the one a regular element supplies.

### The Root the Element Supplies

**Proposition 1 (the root).** Let $\tilde Q=Q_te_t+\vec Q$ with $B^2=(\vec Q,\vec Q)\neq0$, and fix a square root $B$ of $B^2$. Then $\rho=\vec Q/B$ is pure and

$$
\rho^2=-e_t,
\qquad
\tilde Q=Q_te_t+B\rho.
$$

*Proof.* The vector part squares to $\vec Q^2=-B^2e_t$, so $\rho^2=\vec Q^2/B^2=-e_t$. The scalar part of $\rho$ is zero because $\vec Q$ has none.

The other square root $-B$ gives $-\rho$ and exchanges $\lambda_+$ with $\lambda_-$. The identities below are invariant under the exchange, since $\cos$ is even and $\sin$ is odd, and the branch is a labelling and not a datum of the algebra. The root depends on the element: two regular elements generally supply different roots, and §*Global versus Element-Attached* states what is and what is not canonical.

## The Dictionary

### The Spectrum as Two Frequencies

The characteristic polynomial and the spectral criterion are those of *The Spectrum*, §*The Spectral Criterion*:

$$
p_{\tilde Q}(X)=X^2-2Q_tX+Q_t^2+B^2=(X-Q_t-iB)(X-Q_t+iB),
\qquad
\lambda_\pm=Q_t\pm iB.
$$

The eigenvalues are central, so they are ordinary complex numbers. The noncommutativity of $\mathbb{B}$ does not make the frequencies operator-valued: the two frequency components are scalar characters of the flow. The idempotents are the Lagrange idempotents of the two eigenvalues,

$$
\tilde\Pi_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp}
=\frac12\bigl(e_t\mp i\rho\bigr),
$$

and they satisfy

$$
\tilde\Pi_\pm^2=\tilde\Pi_\pm,
\qquad
\tilde\Pi_+\tilde\Pi_-=0,
\qquad
\tilde\Pi_++\tilde\Pi_-=e_t,
\qquad
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-.
$$

The spectral form of the exponential is therefore

$$
e^{\theta\tilde Q}
=e^{\theta\lambda_+}\tilde\Pi_++e^{\theta\lambda_-}\tilde\Pi_-
=e^{\theta Q_t}\bigl(e^{iB\theta}\tilde\Pi_++e^{-iB\theta}\tilde\Pi_-\bigr).
$$

The two terms are the two **characters** of the flow: on the eigenspace $E_\pm=\tilde\Pi_\pm\mathbb{B}$ left multiplication by $e^{\theta\tilde Q}$ is the scalar character $\theta\mapsto e^{\theta\lambda_\pm}$. The two frequencies coincide exactly when $B=0$: that is the spectral cone, treated in §*The Cone*. The gap is $\lambda_+-\lambda_-=2iB$, central, and purely imaginary exactly when $B$ is real.

### The Kernel Identity

**Theorem (the dictionary).** Let $B^2\neq0$, let $\rho=\vec Q/B$, and let $\theta\in\mathbb{C}$. Then

$$
e^{\theta\tilde Q}
=e^{\theta Q_t}\,W\!\left(-\theta,\frac{B}{2\pi}\right)
=e^{\theta Q_t}\,W\!\left(\theta,-\frac{B}{2\pi}\right).
$$

*Proof.* By the closed form of the kernel,

$$
W\!\left(-\theta,\frac{B}{2\pi}\right)
=\exp\!\left(-2\pi\rho\,\frac{B}{2\pi}\,(-\theta)\right)
=\exp(\rho B\theta).
$$

The element $\rho B\theta$ has square $-B^2\theta^2e_t$, so its exponential is $\cos(B\theta)e_t+\sin(B\theta)\rho$. Multiplying by $e^{\theta Q_t}$ and comparing with the closed form of §*The Exponential* gives the identity. The second form follows because $W(t,-\omega)=W(-t,\omega)$.

**The signs.** The flow is the kernel at negative time and positive frequency, or at positive time and negative frequency. The two flips are the two conventions for the sign of the exponent, and the identity is one statement written twice. With the complex convention $W(t,\omega)=e^{-2\pi i\omega t}$, the character of the flow is $e^{+\theta\lambda_\pm}$, so the time of the kernel is the negative of the flow parameter. A reader who uses the opposite convention for the transform reverses $\omega$ and keeps the identity.

**The period.** The map $\theta\mapsto W(-\theta,B/2\pi)$ has period $2\pi/B$, since $\exp(2\pi\rho)=e_t$. For real $B$ this is the ordinary period $2\pi/\lvert B\rvert$ of the oscillation; for complex $B$ it is a complex period, and the flow is periodic as a map of the complex plane.

The dictionary is collected in one table.

| Flow | Kernel |
| --- | --- |
| flow parameter $\theta$ | time $t=-\theta$ |
| rate $B$ | angular frequency $2\pi\omega$ |
| frequency $B/2\pi$ | frequency $\omega$ |
| root $\rho=\vec Q/B$ | root $\rho$ of $-1$ |
| eigenvalue $\lambda_\pm=Q_t\pm iB$ | character exponent |
| idempotent $\tilde\Pi_\pm$ | algebraic projection onto one frequency component |
| eigenspace $E_\pm=\tilde\Pi_\pm\mathbb{B}$ | one of the two invariant planes |
| $\cos(B\theta)e_t+\sin(B\theta)\rho$ | $W(t,\omega)$ |

The table is a dictionary and not an identification of two physical objects. The flow is one element's one-parameter group; the kernel is the generating function of a transform. The identity says that the first is a value of the second, and that the value carries the element's own root and rate.

### The Eigenbasis Is a Fourier Basis

The transform is computed in a root-adapted basis. Choose pure $\nu$ and $\xi$ with

$$
\rho\perp\nu,
\qquad
\nu\perp\xi,
\qquad
\xi\perp\rho,
\qquad
\rho\nu=\xi,
$$

where the pairing is the complex bilinear form of the vector part. In the ordered basis $(e_t,\rho,\nu,\xi)$ left multiplication by $\rho$ is block diagonal, with the same two-by-two block on $(e_t,\rho)$ and on $(\nu,\xi)$: the block sends $e_t$ to $\rho$ and $\rho$ to $-e_t$, and it sends $\nu$ to $\xi$ and $\xi$ to $-\nu$. Its eigenvalues are $\pm i$.

**Proposition 2 (the eigenbasis in the Fourier basis).** In the notation above,

$$
\rho\tilde\Pi_\pm=\pm i\,\tilde\Pi_\pm,
\qquad
\rho u_-=+i\,u_-,
\qquad
\rho u_+=-i\,u_+,
\qquad
u_\mp=\frac12(\nu\mp i\xi),
$$

and $(\tilde\Pi_+,u_-,u_+,\tilde\Pi_-)$ is a basis of $\mathbb{B}$ in which $L_{\tilde Q}$ is diagonal, with the eigenvalues $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$.

*Proof.* The first identity is $\rho(e_t\mp i\rho)/2=(\rho\pm i e_t)/2=\pm i(e_t\mp i\rho)/2$. The second is $\rho(\nu\mp i\xi)/2=(\xi\pm i\nu)/2=\pm i(\nu\mp i\xi)/2$, using $\rho\nu=\xi$ and $\rho\xi=-\nu$. The two vectors of the first block are independent, the two of the second block are independent, and the two planes are complementary because $(e_t,\rho,\nu,\xi)$ is a basis (*Biquaternion Continuous Harmonic Analysis*, §*The Change of Basis*); so the four are a basis. Left multiplication by $\tilde Q$ is $Q_t\,\mathrm{id}+B\,L_\rho$, which gives the eigenvalues $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$.

The pair $(u_-,u_+)$ spans the two nilpotent lines of the eigenbasis. Those lines are determined up to the reciprocal rescaling $(\mu,\mu^{-1})$ of *The Eigenbasis*, §*The Transverse-Vector Construction*, and the normalisation of that article fixes $\mu$; the pair above is one representative. The idempotents and the four lines are the same.

**The two cuts are transverse.** The Fourier factorization cuts $\mathbb{B}$ into the two planes $\operatorname{span}\{e_t,\rho\}$ and $\operatorname{span}\{\nu,\xi\}$, each of which carries both signs of $i$. The spectral decomposition cuts it into the two eigenspaces $E_+=\operatorname{span}\{\tilde\Pi_+,u_-\}$ and $E_-=\operatorname{span}\{u_+,\tilde\Pi_-\}$, each of which takes one line from each plane. Neither cut refines the other. The Fourier factorization keeps the two blocks and applies an ordinary complex transform to each; the spectral decomposition regroups the four lines by eigenvalue. The first computes the transform of a function, the second the flow of one element, and both use the same root and the same complex structure.

### Which Frequency

The word *frequency* is exact in one case and a rate in the others, and the case is decided by $B$, not by normality.

| $B^2$ | $B$ | Flow | Name of $B/2\pi$ |
| --- | --- | --- | --- |
| real positive | real | ordinary oscillation, period $2\pi/\lvert B\rvert$ | frequency |
| real negative | purely imaginary | hyperbolic growth and decay | rapidity rate |
| non-real | genuinely complex | oscillation with an exponential envelope | complex rate |
| zero | zero | truncated, polynomial | none |

The two physical real forms give the first two rows. For the material sector the vector part is real, so $B^2=\lvert\vec Q\rvert^2>0$ and the flow oscillates. For the Hermitian sector the vector part is purely imaginary, so $B^2=-\lvert\vec Q\rvert^2<0$ and the flow is hyperbolic. The general element has a genuinely complex $B$ and a frequency with an envelope. The element $(1+i)\vec e_x$ of §*Worked Examples* is normal and has a complex $B$: normality does not make the frequency real.

## The Two Conjugations

### Natural Conjugation

The natural conjugation $\natural$ fixes $e_t$ and sends every vector to its negative. For a pure root, $\rho^\natural=-\rho$. Because $\natural$ is complex linear,

$$
W(t,\omega)^\natural=\exp(2\pi\rho\,\omega t)=W(t,\omega)^{-1}.
$$

The kernel is therefore on the natural unit sphere identically, for every pure root and with no further condition. The flow carries the scalar factor, and the same computation gives

$$
\bigl(e^{\theta\tilde Q}\bigr)^\natural\bigl(e^{\theta\tilde Q}\bigr)=e^{2\theta Q_t}e_t,
$$

so the quaternionic norm of the flow is $N(e^{\theta\tilde Q})=e^{2\theta Q_t}$, in agreement with *Biquaternion Elementary Functions*, §*The Exponential*. The flow is natural-unitary for all $\theta$ exactly when $Q_t=0$.

### Hermitian Conjugation

The Hermitian conjugation is $*=\bar{\natural}$. For a pure root, $\rho^*=-\bar\rho$. Then

$$
W(t,\omega)^*=\exp(2\pi\bar\rho\,\omega t),
\qquad
W(t,\omega)W(t,\omega)^*=\exp\bigl(-2\pi(\rho-\bar\rho)\omega t\bigr),
$$

and the kernel is unitary for the positive Hermitian form exactly when $\rho=\bar\rho$, that is, when $\rho$ is real. This is the criterion of *The Bochner Theorem for the Biquaternion Transform: the Hermitian Form and the Root*, §*Unitarity of the Character and the Root*, read on the root the element supplies.

**Proposition 3 (unitarity and self-adjointness of the flow).** Let $B^2\neq0$ and let $\theta$ be real. The following are equivalent:

- $e^{\theta\tilde Q}$ is unitary for the Hermitian form for every $\theta$;
- $\tilde Q^*=-\tilde Q$;
- $Q_t\in i\mathbb{R}$ and $\vec Q\in\mathbb{R}^3$.

The following are also equivalent:

- $e^{\theta\tilde Q}$ is self-adjoint for every $\theta$;
- $\tilde Q^*=\tilde Q$;
- $Q_t\in\mathbb{R}$ and $\vec Q\in i\mathbb{R}^3$.

*Proof.* If $E=e^{\theta\tilde Q}$ is unitary for every $\theta$, differentiating $EE^*=e_t$ at $\theta=0$ gives $\tilde Q+\tilde Q^*=0$. Conversely, if $\tilde Q^*=-\tilde Q$ then $E^*=e^{\theta\tilde Q^*}=e^{-\theta\tilde Q}=E^{-1}$. The equivalence with the coordinate conditions is the computation of $*$ on $Q_te_t+\vec Q$: the scalar part is conjugated and the vector part is negated and conjugated, so $\tilde Q^*=-\tilde Q$ means $\bar Q_t=-Q_t$ and $\overline{\vec Q}=\vec Q$. The self-adjoint case is the same computation with the opposite signs.

The first family is the material sector and the second is the Hermitian sector. Unitarity is strictly stronger than normality, because $\tilde Q^*=-\tilde Q$ implies $\tilde Q\tilde Q^*=\tilde Q^*\tilde Q$; the converse fails.

### Normality, Unitarity and the Hermitian Norm of the Flow

The normality theorem is that of *The Biquaternion Eigenvalue Decomposition*, §*The Hermitian Case*, with $\vec U=\vec Q/B=\rho$. For $B^2\neq0$, the following are equivalent:

- $\tilde Q$ is normal, $\tilde Q\tilde Q^*=\tilde Q^*\tilde Q$;
- $\vec Q\times\overline{\vec Q}=0$, with the complex bilinear cross product;
- $\operatorname{Re}\vec Q$ and $\operatorname{Im}\vec Q$ are parallel;
- $\rho$ is real;
- $\tilde\Pi_\pm$ are Hermitian;
- $E_+$ and $E_-$ are orthogonal for the Hermitian form.

The criterion involves the vector part alone. The scalar part is free, and this is the first source of confusion: a normal element can have any complex rate $Q_t$.

**Corollary 1.** Normality does not imply unitarity. The element $\tilde Q=(1+i)\vec e_x$ is normal, since $\rho=\vec e_x$ is real, but $\tilde Q^*\neq-\tilde Q$ and $\tilde Q^*\neq\tilde Q$. Its flow is neither unitary nor self-adjoint.

**Corollary 2.** Normality does not imply a constant norm. The same element has $\lvert B\rvert=\sqrt2$ and $\operatorname{Im}B=1$, and its Hermitian norm grows as $\cosh(2\theta)$.

**Corollary 3.** Non-normality does not imply growth. The element $\tilde Q=i\vec e_x+\vec e_y+\vec e_z$ has $\rho=(i,1,1)$ and is not normal, but its Hermitian norm is

$$
\bigl\langle e^{\theta\tilde Q}\bigr\rangle_*=\cos^2\theta+3\sin^2\theta=1+2\sin^2\theta,
$$

which oscillates between $1$ and $3$ and never grows.

The general formula is the following.

**Proposition 4 (the Hermitian norm of the flow).** Let $B^2\neq0$ and let $\theta$ be real. Put $\lVert\rho\rVert^2=\sum_k\lvert\rho_k\rvert^2$. Then

$$
\bigl\langle e^{\theta\tilde Q}\bigr\rangle_*
=\lvert e^{\theta Q_t}\rvert^2
\left(\lvert\cos(B\theta)\rvert^2+\lvert\sin(B\theta)\rvert^2\,\lVert\rho\rVert^2\right).
$$

*Proof.* Write $E=e^{\theta Q_t}(a e_t+b\rho)$ with $a=\cos(B\theta)$ and $b=\sin(B\theta)$. Since $\rho$ is pure, the scalar part of $\rho\rho^*$ is $\lVert\rho\rVert^2e_t$, and the cross terms $a\bar b\rho^*+b\bar a\rho$ are pure vectors; hence the scalar part of $EE^*$ is $\lvert e^{\theta Q_t}\rvert^2(\lvert a\rvert^2+\lvert b\rvert^2\lVert\rho\rVert^2)$.

**Proposition 5 (the norm deficit).** $\lVert\rho\rVert^2\ge1$, with equality exactly when $\rho$ is real, that is, exactly when $\tilde Q$ is normal.

*Proof.* $\lvert B\rvert^2=\lvert B^2\rvert=\lvert\sum_kQ_k^2\rvert\le\sum_k\lvert Q_k\rvert^2$, with equality exactly when the non-zero squares $Q_k^2$ have one argument. Dividing by $\lvert B\rvert^2$ gives the inequality. If they do, $Q_k=\zeta r_k$ with $r_k\in\mathbb{R}$ and $\zeta^2$ that argument, so $B=\pm\zeta R$ with $R^2=\sum_kr_k^2$ and $\rho=\pm(r_x,r_y,r_z)/R$ is real; the converse is immediate.

The three quantities $Q_t$, $B$ and $\lVert\rho\rVert^2$ govern the norm independently.

| Quantity | Role in $\langle e^{\theta\tilde Q}\rangle_*$ | Condition for its neutral value |
| --- | --- | --- |
| $\operatorname{Re}Q_t$ | dilation rate $e^{2\theta\operatorname{Re}Q_t}$ | $\operatorname{Re}Q_t=0$ |
| $\operatorname{Im}B$ | envelope rate, growth as $e^{2\lvert\operatorname{Im}B\rvert\lvert\theta\rvert}$ | $B$ real |
| $\lVert\rho\rVert^2$ | oscillation amplitude, $\ge1$ | $\lVert\rho\rVert^2=1$, i.e. normal |

**Corollary 4 (bounded and unbounded flows).** If $B$ is real and $\operatorname{Re}Q_t=0$, the Hermitian norm is bounded between $1$ and $\lVert\rho\rVert^2$. If $\operatorname{Re}Q_t\neq0$, it is unbounded on one side. If $\operatorname{Im}B\neq0$, it is unbounded on both sides.

A non-normal element has a larger oscillation amplitude, not a decay. A decay is a negative real part of $Q_t$ in the convention $e^{+\theta\tilde Q}$, and a boost is a non-zero imaginary part of $B$. The norm deficit measures how far the element is from normal, and it is an amplitude, not a rate.

## The Cone

### No Root, No Frequency

On the spectral cone $B^2=0$ the two eigenvalues coincide at $Q_t$ and the root $\rho=\vec Q/B$ does not exist. Write $\vec N=\vec Q$. Then $\vec N^2=-B^2e_t=0$, so $\vec N$ is square-zero, and the operator is $L_{\tilde Q}=Q_t\,\mathrm{id}+L_{\vec N}$ with $L_{\vec N}^2=0$. There is no frequency to read off and no root to substitute in the kernel.

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

the right-hand side is entire in $B$ and its value at $B=0$ is $e^{\theta Q_t}(e_t+\theta\vec Q)$. The closed form therefore has a limit at the cone even though $B$ and $\rho$ do not. The kernel $W(t,\omega)$ itself has no limit, because it is a function of a root that does not exist; the combination that the flow uses does.

### The Three Strata

The cone carries three normal forms, those of *The Spectrum*, §*The Degenerate Case: The Cone*, and each has its own exponential.

| Stratum | Normal form | Exponential | Root | Eigenbasis |
| --- | --- | --- | --- | --- |
| scalar | $Q_te_t$ | $e^{\theta Q_t}e_t$ | none | every basis, none canonical |
| nilpotent | $\vec N$, $\vec N^2=0$ | $e_t+\theta\vec N$ | none | none |
| unipotent | $Q_t(e_t+\vec\Upsilon)$, $\vec\Upsilon^2=0$ | $e^{\theta Q_t}(e_t+\theta Q_t\vec\Upsilon)$ | none | none |

The scalar stratum is a central character with no direction. The nilpotent stratum is a null translation with no rate. The unipotent stratum is a scaled null translation: a rate and a shear, with no frequency. None of the three has a root of $-1$, and none has an oscillatory character.

## Global versus Element-Attached

**What is canonical.** For a regular element, the pair of eigenspaces $\{E_+,E_-\}$ is unique, and the eigenvalues are determined up to the exchange of the two branches. The vectors inside each eigenspace are a gauge: multiplying a vector of $E_+$ by a non-zero scalar and a vector of $E_-$ by another leaves the eigenspaces unchanged. The normalised Peirce basis of *The Eigenbasis* fixes that gauge; the root-adapted basis of §*The Eigenbasis Is a Fourier Basis* fixes it differently.

**Every element expands in the basis of a given regular element.** The four vectors of Proposition 2 form a basis of $\mathbb{B}$, so every biquaternion has coordinates in it; the spectral decomposition of the given element is diagonal in those coordinates. This is the sense in which a regular element supplies a frame for the whole algebra — a frame attached to the element, not a frame of the algebra.

**No global eigenbasis.** A basis that diagonalized every $L_{\tilde Q}$ would make every $L_{\tilde Q}$ diagonal in one basis, hence would make any two of them commute; then every two elements of $\mathbb{B}$ would commute, which is false. The obstruction is the noncommutativity, not the choice of root.

**No canonical root.** A non-central root $\rho$ is moved by an inner automorphism: if $U$ is a unit with $U\rho\neq\rho U$, then $U\rho U^{-1}$ is another root of $-1$. The central roots $\pm i$ are fixed by every inner automorphism, but they are not pure and no regular element supplies them. The algebra therefore has no root that is both canonical and available to the dictionary.

**On the cone.** The scalar line has every basis as an eigenbasis and none as a canonical one. The nilpotent and unipotent strata have no eigenbasis. The global statement is the one of the introduction: the eigenbasis exists on the open dense set $B^2\neq0$, is attached to the element, and is not canonical as a global object.

## Worked Examples

The table reads five elements through the dictionary. The last three columns record whether the flow is normal, unitary and self-adjoint.

| $\tilde Q$ | $B^2$, $B$ | $\rho$ | $\lambda_\pm$ | $e^{\theta\tilde Q}$ | $\langle e^{\theta\tilde Q}\rangle_*$ | normal | unitary | self-adjoint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\vec e_x$ | $1$, $1$ | $\vec e_x$ | $\pm i$ | $\cos\theta\,e_t+\sin\theta\,\vec e_x$ | $1$ | yes | yes | no |
| $i\vec e_x$ | $-1$, $i$ | $\vec e_x$ | $\mp1$ | $\cosh\theta\,e_t+i\sinh\theta\,\vec e_x$ | $\cosh2\theta$ | yes | no | yes |
| $(1+i)\vec e_x$ | $2i$, $1+i$ | $\vec e_x$ | $\mp(1-i)$ | $\cos((1+i)\theta)e_t+\sin((1+i)\theta)\vec e_x$ | $\cosh2\theta$ | yes | no | no |
| $i\vec e_x+\vec e_y+\vec e_z$ | $1$, $1$ | $(i,1,1)$ | $\pm i$ | $\cos\theta\,e_t+\sin\theta\,\rho$ | $1+2\sin^2\theta$ | no | no | no |
| $(1+i)e_t+\vec e_x$ | $1$, $1$ | $\vec e_x$ | $1\pm2i$ | $e^{(1+i)\theta}(\cos\theta\,e_t+\sin\theta\,\vec e_x)$ | $e^{2\theta}$ | yes | no | no |

The first two rows are the two real forms. The first is the material case: real $B$, real root, unitary flow, constant norm. The second is the Hermitian case: imaginary $B$, real root, self-adjoint flow, hyperbolic norm.

The third row is normal, with a real root, and is neither unitary nor self-adjoint; its $B$ is genuinely complex and its norm grows. It shows that normality is orthogonal diagonalisation and nothing more. The fourth row is not normal, and its norm oscillates between $1$ and $3$; it shows that non-normality is not a decay. The fifth row is normal and grows because of the scalar rate $Q_t=1+i$.

The kernel identity is visible in the first row: $e^{\theta\vec e_x}=W(-\theta,1/2\pi)$, since $Q_t=0$ and $B=1$. In the second row the same kernel with an imaginary frequency gives the hyperbolic form, because $\cos(i\theta)=\cosh\theta$ and $\sin(i\theta)=i\sinh\theta$.

**The cone.** Take $\vec N=\vec e_x+i\vec e_y$. Then $\vec N^2=(-1)+(-1)(i^2)=0$ and $e^{\theta\vec N}=e_t+\theta\vec N$. Adjoining a scalar, $\tilde Q=Q_te_t+\vec N$ gives $e^{\theta\tilde Q}=e^{\theta Q_t}(e_t+\theta\vec N)$. The element is unipotent when $Q_t\neq0$ and nilpotent when $Q_t=0$; the exponential is polynomial in both cases, and no root is available.

## The Boundary

The article states an algebraic dictionary. It does not supply a dynamics: $\theta$ is a flow parameter, and $B/2\pi$ is a rate of that flow, not the frequency of a signal, until an equation of motion identifies the two. The identification is the work of the physics companions and is not made here.

It does not reprove the transform theory. Inversion, Plancherel, the convolution theorem and the vanishing-norm issue are those of *Biquaternion Continuous Harmonic Analysis*, and nothing in the dictionary decides them. The identity is pointwise in the element and does not commute with an integral.

It does not claim a canonical root or a global basis. The root is attached to the element, and §*Global versus Element-Attached* states the two obstructions: noncommutativity for a global basis, and the inner automorphisms for a canonical root.

It does not identify normality with unitarity, nor non-normality with damping. Proposition 3 gives the exact unitarity criterion, Proposition 4 the exact norm formula, and Proposition 5 the exact deficit. In particular the deficiency $\lVert\rho\rVert^2-1$ is an amplitude, and the decay rate is $\operatorname{Re}Q_t$.

The sign convention is conventional. The theorem is stated with the exponent $+\theta\tilde Q$ and the kernel $e^{-2\pi\rho\omega t}$; the other convention flips both signs and leaves the content unchanged.

The cone is not a limit of the regular kernel in the ordinary sense. The closed form of the flow extends to $B=0$, and §*The Truncated Kernel* says exactly what extends and what does not: the formula extends, the root and the frequency do not.

## Summary

A regular element $\tilde Q=Q_te_t+\vec Q$ supplies the root $\rho=\vec Q/B$ of the Fourier kernel, and its exponential is the kernel at negative time:

$$
e^{\theta\tilde Q}
=e^{\theta Q_t}\left(\cos(B\theta)e_t+\sin(B\theta)\rho\right)
=e^{\theta Q_t}W\!\left(-\theta,\frac{B}{2\pi}\right).
$$

The eigenvalues $\lambda_\pm=Q_t\pm iB$ are the character exponents, the idempotents $\tilde\Pi_\pm=\tfrac12(e_t\mp i\rho)$ are the algebraic projections onto the two frequency components, and the eigenbasis is the root-adapted Fourier basis diagonalized block by block. The Fourier factorization keeps the two invariant planes; the spectral decomposition regroups their four lines by eigenvalue; the two cuts are transverse.

The kernel is natural-unitary for every pure root, and Hermitian-unitary exactly when the root is real. The flow is Hermitian-unitary exactly in the material sector, and Hermitian-self-adjoint exactly in the Hermitian sector. Normality is the orthogonality of the eigenbasis: it is a condition on $\vec Q$ alone, it is weaker than unitarity, and it does not make the norm constant.

The Hermitian norm of the flow is

$$
\bigl\langle e^{\theta\tilde Q}\bigr\rangle_*
=\lvert e^{\theta Q_t}\rvert^2
\left(\lvert\cos(B\theta)\rvert^2+\lvert\sin(B\theta)\rvert^2\lVert\rho\rVert^2\right),
\qquad
\lVert\rho\rVert^2\ge1,
$$

with equality exactly when the element is normal. The three sources of norm change are independent: the dilation $\operatorname{Re}Q_t$, the envelope $\operatorname{Im}B$, and the oscillation amplitude $\lVert\rho\rVert^2$. Damping is the dilation, a boost is the envelope, and the third is neither.

On the cone there is no root and no frequency. The exponential is the truncated $e^{\theta Q_t}(e_t+\theta\vec N)$, the dual-number kernel, and the three strata are the central character, the null translation and the scaled null translation. The closed form of the flow extends to $B=0$; the root and the frequency do not.

### Main Results

| Result | Expression |
| --- | --- |
| Root supplied by the element | $\rho=\vec Q/B$, $\rho^2=-e_t$, $\tilde Q=Q_te_t+B\rho$ |
| Closed form | $e^{\theta\tilde Q}=e^{\theta Q_t}(\cos(B\theta)e_t+\sin(B\theta)\rho)$ |
| Kernel identity | $e^{\theta\tilde Q}=e^{\theta Q_t}W(-\theta,B/2\pi)$ |
| Eigenvalues | $\lambda_\pm=Q_t\pm iB$ |
| Idempotents | $\tilde\Pi_\pm=\tfrac12(e_t\mp i\rho)$ |
| Spectral form | $e^{\theta\tilde Q}=e^{\theta Q_t}(e^{iB\theta}\tilde\Pi_++e^{-iB\theta}\tilde\Pi_-)$ |
| Eigenspaces | $E_\pm=\tilde\Pi_\pm\mathbb{B}$ |
| Fourier eigenbasis | $(\tilde\Pi_+,u_-,u_+,\tilde\Pi_-)$, $u_\mp=\tfrac12(\nu\mp i\xi)$ |
| Natural unitarity of the kernel | $W^\natural=W^{-1}$ for every pure root |
| Hermitian unitarity of the kernel | $W^*=W^{-1}$ iff $\rho$ real |
| Unitary flow | $\tilde Q^*=-\tilde Q$ iff $Q_t\in i\mathbb{R}$, $\vec Q\in\mathbb{R}^3$ |
| Self-adjoint flow | $\tilde Q^*=\tilde Q$ iff $Q_t\in\mathbb{R}$, $\vec Q\in i\mathbb{R}^3$ |
| Normal element | $\tilde Q\tilde Q^*=\tilde Q^*\tilde Q$ iff $\rho$ real iff $\operatorname{Re}\vec Q\parallel\operatorname{Im}\vec Q$ iff $\tilde\Pi_\pm$ Hermitian |
| Hermitian norm | $\lvert e^{\theta Q_t}\rvert^2(\lvert\cos(B\theta)\rvert^2+\lvert\sin(B\theta)\rvert^2\lVert\rho\rVert^2)$ |
| Norm deficit | $\lVert\rho\rVert^2\ge1$, equality iff normal |
| Bounded Hermitian norm | iff $B$ real and $\operatorname{Re}Q_t=0$ |
| Cone | $e^{\theta\tilde Q}=e^{\theta Q_t}(e_t+\theta\vec N)$, $\vec N^2=0$ |
| No global basis | noncommutativity of $\mathbb{B}$ |
| No canonical root | inner automorphisms move the non-central roots |

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion, $Q_t\in\mathbb{C}$, $\vec Q\in\mathbb{C}^3$ |
| $B^2=(\vec Q,\vec Q)=Q_x^2+Q_y^2+Q_z^2$ | the bilinear square of the vector part |
| $B$ | a fixed square root of $B^2$; the other is $-B$ |
| $\rho=\vec Q/B$ | the root of $-1$ supplied by the element |
| $\vec\Xi=-i\rho$ | the root of $+1$ used by the spectral articles |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues, the character exponents |
| $\tilde\Pi_\pm=\tfrac12(e_t\mp i\rho)$ | the spectral idempotents |
| $E_\pm=\tilde\Pi_\pm\mathbb{B}$ | the eigenspaces of left multiplication |
| $W(t,\omega)=\exp(-2\pi\rho\omega t)$ | the biquaternion Fourier kernel |
| $\nu,\xi$ | pure directions completing $\rho$ to a root-adapted basis |
| $u_\mp=\tfrac12(\nu\mp i\xi)$ | the nilpotent pair of the eigenbasis |
| $\vec N=\vec Q$ on the cone, $\vec N^2=0$ | the nilpotent part of a degenerate element |
| $\natural$ | the natural conjugation, $e_t\mapsto e_t$, $\vec e_k\mapsto-\vec e_k$ |
| $*$ | the Hermitian conjugation, $\bar{\natural}$ |
| $\langle X\rangle_*=XX^*$ | the positive Hermitian form |
| $N(X)=XX^\natural$ | the quaternionic norm |
| $\lVert\rho\rVert^2=\sum_k\lvert\rho_k\rvert^2$ | the Euclidean square of the root |
| $\theta$ | the flow parameter |
| $t,\omega$ | the kernel time and frequency |

## Further Reading

- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential, the logarithm, the kernel and the principal branch.
- [Biquaternion Continuous Harmonic Analysis](biquaternion-continuous-harmonic-analysis.html), for the kernel, the transform pair, inversion, Plancherel and the factorization into complex transforms.
- [Biquaternion Discrete Harmonic Analysis](biquaternion-discrete-harmonic-analysis.html), for the discrete transform and the condition on the root.
- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), §*The Hermitian Case*, for normality, the Hermitian projectors and the orthogonal spectral resolution.
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the spectral criterion, the cone and the three strata.
- [The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), for the normalised Peirce basis, the unique expansion and the spinor spaces.
- [The Bochner Theorem for the Biquaternion Transform: the Hermitian Form and the Root](the-bochner-theorem-for-the-biquaternion-transform-the-hermitian-form-and-the-root.html), for the unitarity criterion of the character.
- [Dual Numbers Harmonic Analysis](dual-numbers-harmonic-analysis.html), for the non-oscillating characters of the truncated regime.
- [Harmonic Analysis over Hypercomplex Systems](harmonic-analysis-over-hypercomplex-systems.html), for the place of the transform among the eight systems.
- [Relations between Quaternionic Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors and the independence of the two conditions.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-biquaternion.html), for the companion dictionary between the exponential and the spectrum.
- [Physical Interpretation of Spectral Regularity and Degeneracy in the Biquaternion Algebra](../articles_physics/physical-interpretation-of-spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the physical interpretation of the two cases.
- [Derivatives, Fields and Transforms](../articles_physics/derivatives-fields-and-transforms.html), for the root as the clock and the frequency as its rate.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation and the conjugations.
