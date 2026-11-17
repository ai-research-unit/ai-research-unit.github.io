# __The Spectrum Does Not Determine the Frame__

## Introduction

A Lorentz rotor has a spectrum, and the spectrum is much smaller than the rotor. Two eigenvalues, whose product is one, carry two real numbers; the rotor carries six. The four that are missing are the axis, the orientation of the eigenbasis, and the sign of the sheet.

This article states the count, exhibits the ambiguity as a family rather than as a curiosity, and says what data must be added to the spectrum to fix the frame. The conclusion matters because the block derives physical statements — the boost factor, the redshift, the aberration — from eigenvalues, and every such derivation is a statement about the spectrum and not about the frame.

The article assumes *The Group of Unit-Norm Biquaternions* for the group, *A Frame Is a Boost Times a Rotation: The Cartan Word* for the factors, *The Two Eigenvalues Are the Two Weyl Weights* for the boost's spectrum, and *When the Axes Commute: The Normal Transformations* for the class of elements that are unitarily diagonalisable at all.

## The Spectrum of a Rotor

### The Eigenvalues

Let $\tilde U_{\mathrm{lor}}\in G$ and let $\mu_1,\mu_2$ be the eigenvalues of $\mathsf{M}_2(\tilde U_{\mathrm{lor}})$. Then

$$
\mu_1\mu_2=\det\mathsf{M}_2(\tilde U_{\mathrm{lor}})=1,
$$

so the spectrum is determined by the single complex number $\mu=\mu_1$, the other being $\mu^{-1}$, with $\mu\neq0$. In real terms the spectrum is **two** parameters.

### What the Two Parameters Are

Write $\mu=\varrho\,e^{i\theta_{\mathrm{pha}}}$ with $\varrho>0$, where $\theta_{\mathrm{pha}}$ is the corpus's name for the phase of the polar form, taken modulo a full turn. Then

- $\varrho\,e^{i\theta_{\mathrm{pha}}}$ is the modulus, and $\log\varrho\,e^{i\theta_{\mathrm{pha}}}$ is a rapidity-like number: it measures the boost part;
- $\theta_{\mathrm{pha}}$ is a phase, and it measures the rotation part; on a rotation it is half the rotation angle, $\theta_{\mathrm{pha}}=\theta_{\mathrm{axr}}/2$.

So the spectrum, read as $(\log\varrho\,e^{i\theta_{\mathrm{pha}}},\theta_{\mathrm{pha}})$, is one number of each kind: a boost magnitude and a rotation angle. That is exactly the intuition a reader brings — a Lorentz transformation has a boost magnitude and a rotation angle — and the surprise is that the intuition stops there.

### The Two Families

For the two families the spectrum is even smaller:

| element | eigenvalues | spectral parameters |
|---|---|---|
| boost of rapidity $\theta_{\mathrm{rpd}}$ | $e^{\pm\theta_{\mathrm{rpd}}/2}$, real positive | the modulus only, $\log\varrho\,e^{i\theta_{\mathrm{pha}}}=\theta_{\mathrm{rpd}}/2$ |
| rotation of angle $\theta_{\mathrm{axr}}$ | $e^{\pm i\theta_{\mathrm{axr}}/2}$, on the unit circle | the phase only, $\theta_{\mathrm{pha}}=\theta_{\mathrm{axr}}/2$ |
| general | $\mu$, $\mu^{-1}$ | both |

For a boost the spectrum is **one** real number; the other real number is the axis, and the spectrum is silent about it.

## The Diagonalising Unitary Is Not Unique

### The Statement

A **normal** element of the group — one satisfying $\tilde U\tilde U^{*}=\tilde U^{*}\tilde U$ — is unitarily diagonalisable:

$$
\mathsf{M}_2(\tilde U)=\mathsf{M}_2(\tilde V)\,D\,\mathsf{M}_2(\tilde V)^{*},
\qquad D=\operatorname{diag}(\mu_1,\mu_2),
$$

with $\tilde V$ of unit norm and $*$-unitary. Boosts and rotations are normal, and so is any product of a boost and a rotation about the same axis; general elements are not, and for them the diagonalisation does not exist at all.

### The Residual Freedom

The diagonalising $\tilde V$ is not unique. If $\tilde V$ works then so does $\tilde V\tilde W$ for any diagonal unitary $\tilde W$, since $\tilde W D\tilde W^{-1}=D$. Modulo the overall phase, which is irrelevant to a conjugation, the residual freedom is

$$
\tilde W=\operatorname{diag}(e^{i\theta_{\mathrm{axr}}/2},e^{-i\theta_{\mathrm{axr}}/2}),\qquad \theta_{\mathrm{axr}}\in\mathbb{R}/2\pi\mathbb{Z},
$$

a circle. So the diagonalisation is determined up to one real parameter, and that parameter is precisely the one the spectrum cannot see.

### The Counting

For a normal element:

$$
\underbrace{4}_{\text{normal elements}}=\underbrace{2}_{\text{spectrum}}+\underbrace{2}_{\text{axis}}.
$$

For a general element of the group the diagonalisation does not exist, and the analogous count is

$$
\underbrace{6}_{\text{group}}=\underbrace{2}_{\text{spectrum}}+\underbrace{4}_{\text{everything else}}.
$$

Both counts are exact and both say the same thing: the spectrum is a small quotient.

### Why the Count Is Worth Doing

Because it tells a reader where to look for the missing information. For a boost the missing two parameters are the axis; for a general element they are the axis plus the two parameters that measure the failure of normality. The failure of normality is not small: it is the Thomas–Wigner rotation, and it is invisible to the spectrum.

## Why the Spectrum Is Insufficient

### What the Spectrum Determines

- The product of the boost magnitude and the rotation angle's sign, through $\mu\bar\mu$.
- The determinant, which is fixed.
- The trace, $\mu+\mu^{-1}$, and hence $\cosh$ or $\cos$ of the parameter.
- Whether the element is elliptic, hyperbolic or parabolic in the classification of *The Lorentz Group in Biquaternionic Form — Structure and Representations*.

### What It Does Not Determine

- **The axis.** Every boost of a given rapidity, in every direction, has the same spectrum. The set is a two-sphere, and it is not small.
- **The eigenbasis.** Even with the axis fixed, the two eigenprojectors are only determined up to the residual phase of the previous section.
- **The sheet.** $\tilde U$ and $-\tilde U$ give the same Lorentz transformation and different spectra: the eigenvalues of $-\tilde U$ are $-\mu_1,-\mu_2$, whose product is still one. So the spectrum distinguishes the two sheets, and the Lorentz transformation does not — the spectrum carries one bit that the transformation does not, and misses four real parameters that it does.
- **The order.** The spectrum is a set, and the two eigenvalues are interchangeable.

### The Counterexample

Take any rapidity $\theta_{\mathrm{rpd}}>0$ and any two distinct unit vectors $\vec u\neq\vec u'$. Then

$$
\tilde U=\exp\Bigl(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u\Bigr),\qquad
\tilde U'=\exp\Bigl(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u'\Bigr)
$$

have the same spectrum and are different elements. They are conjugate to one another by a rotation, so the whole family is one conjugacy class, and the conjugating element is precisely the frame change that the spectrum does not record. The family is two-dimensional.

The same statement for rotations: every rotation by a given angle has the same spectrum, and the family is an $S^{2}$.

## What Extra Data Fixes the Frame

### The Eigenprojectors

The spectrum plus the two **eigenprojectors** $\Pi_\pm$ fixes the element completely:

$$
\tilde U=\mu_+\Pi_++\mu_-\Pi_-,
\qquad
\Pi_\pm^{2}=\Pi_\pm,\quad \Pi_\pm^{*}=\Pi_\pm,\quad \operatorname{tr}\Pi_\pm=1,\quad \Pi_+\Pi_-=0 .
$$

A Hermitian idempotent of trace one is determined by a point of $S^{2}$ — it is $\tfrac12(e_t+\hat n\cdot\vec\sigma)$ in matrix language — so the eigenprojectors carry two real parameters. Two from the spectrum plus two from the projectors is four, which is the dimension of the normal elements.

### What the Projectors Are

Physically, $\Pi_+$ is the state that the boost stretches and $\Pi_-$ the state that it squeezes. For a boost along $\hat u$ they are the two spin states along $\hat u$. So "the frame" is exactly the choice of the two states, and the axis is the line that separates them.

### The Remaining Freedom

With the spectrum and the projectors fixed there is still the order (which eigenvalue goes with which projector) and the sheet. Those are discrete, and they are the subject of the last section.

### The Summary Table

| data | real parameters | what it fixes |
|---|---|---|
| spectrum $\{\mu,\mu^{-1}\}$ | $2$ | the boost magnitude and the rotation angle |
| eigenprojectors $\{\Pi_+,\Pi_-\}$ | $2$ | the axis |
| order | $1$ bit | which eigenvalue is associated with which projector |
| sheet | $1$ bit | the sign of the rotor, invisible to the Lorentz transformation |
| **total** | $4$ continuous | a normal element |

## The Equivalence Class of One Spectrum

### The Family

Fix a spectrum, i.e. fix the rapidity $\theta_{\mathrm{rpd}}$ of a boost or the rotation angle $\theta_{\mathrm{axr}}$ of a rotation. The frames with that spectrum are

$$
\{\tilde U(\vec n,\theta_{\mathrm{rpd}}):\ \lvert\vec n\rvert=1\}\times\mathbb{Z}_{2}
$$

for the boost case: every axis, in both sheets. The family is two-dimensional and connected apart from the sheet label, and it is one equivalence class of the relation "has the same spectrum".

### The Dimension Count

| | frame | spectrum | class |
|---|---|---|---|
| boost | $\vec n\in S^{2}$, $\theta_{\mathrm{rpd}}\in\mathbb{R}$ | one real number | $S^{2}\times\mathbb{Z}_{2}$ |
| rotation | $\vec n\in S^{2}$, $\theta_{\mathrm{axr}}\in(-\pi,\pi]$ | one real modulus | $S^{2}\times\mathbb{Z}_{2}$ |

So the spectrum discards two of the three continuous parameters and one of the two discrete ones. That is the quantitative form of the article's title: the loss is two-dimensional, and no amount of care with the spectrum recovers it.

### The Worked Element

The block's standard counterexample is the element

$$
\tilde Q=\bigl(1-\tfrac{i}{2}\bigr)e_t+\tfrac{1+i}{\sqrt2}\vec e_x+\tfrac{1}{\sqrt2}\vec e_y+\tfrac{i}{2}\vec e_z ,
$$

whose word has

$$
\theta_{\mathrm{rpd}}=1.762747,\quad \vec u_{\mathrm b}=\vec e_x,\quad
\theta_{\mathrm{axr}}=\tfrac{\pi}{2},\quad \vec u_{\mathrm r}=\tfrac{\vec e_x+\vec e_y}{\sqrt2},\quad c=\tfrac{1}{\sqrt2}.
$$

It is unit-norm, so its spectrum is a pair of reciprocals; computed from the matrix image it is

$$
\lambda_1=1.624811-1.300243i,\qquad \lambda_2=0.375189+0.300243i,
$$

with moduli $2.081019$ and $0.480534$ and arguments $\mp0.674889$. The sum is $2Q_t=2-i$, that is $Q_t=1-\tfrac{i}{2}$, and the product is $N=1$.

### The Normal-Case Reading of That Spectrum

The normal-case formulas read a spectrum as a rapidity and an angle: the rapidity is the logarithm of the ratio of the moduli, the angle is twice the argument. Here they return

$$
\log\frac{2.081019}{0.480534}=1.465715,\qquad 2\times0.674889=1.349778,
$$

so $1.466$ and $1.350$ — not the true $1.763$ and $1.571$. The gap is not a rounding effect: the two readings differ by $0.3$ in the rapidity and $0.22$ in the angle, which is a quarter of a radian in each case.

### The Cross Term Is the Missing Datum

The reason is visible in the scalar part. For a word whose axes make an angle $\gamma$,

$$
Q_t=\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}\cos\tfrac{\theta_{\mathrm{axr}}}{2}
-i\,\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}\sin\tfrac{\theta_{\mathrm{axr}}}{2}\,c,
\qquad c=\cos\gamma ,
$$

and the two angles do not fix $Q_t$ unless $c$ is known. For the element above, $\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}=\sqrt2$ and $\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}=1$, so the real part is $\sqrt2\cdot\tfrac{1}{\sqrt2}=1$ and the imaginary part is $\tfrac{1}{\sqrt2}\cdot\tfrac{1}{\sqrt2}=\tfrac12$, giving $Q_t=1-\tfrac{i}{2}$ as computed. A reader who uses the parallel-axis formula $\cosh\frac{\theta_{\mathrm{rpd}}}{2}\cos\frac{\theta_{\mathrm{axr}}}{2}$ gets the real part $1$ and misses the imaginary part entirely, hence a real spectrum where the element has a complex one.

So the two named angles are not functions of the spectrum. The spectrum carries $(\log\varrho\,e^{i\theta_{\mathrm{pha}}},\theta_{\mathrm{pha}})$; the frame carries $(\theta_{\mathrm{rpd}},\theta_{\mathrm{axr}},\vec u_{\mathrm b},\vec u_{\mathrm r})$ up to the sheet. The direction between the axes is the datum that the spectrum does not carry, and the worked element is the smallest case in which its absence is visible.

### The One-Parameter Family About the Boost Axis

The class has a symmetry that the axis count alone hides. Conjugating a frame by a rotation about its own boost axis preserves the spectrum:

$$
\tilde U\ \longmapsto\ \tilde R_\phi\,\tilde U\,\tilde R_\phi^{*},
\qquad
\tilde R_\phi=\exp\Bigl(\tfrac{\phi}{2}\vec u_{\mathrm b}\Bigr).
$$

The conjugation fixes the boost factor, because $\tilde R_\phi$ commutes with $\tilde U_\Psi$; it carries the rotation axis $\vec u_{\mathrm r}$ to $R_\phi\vec u_{\mathrm r}$, that is, it rotates the rotation axis about the boost axis; and it preserves the eigenvalues, because a conjugate matrix has the same eigenvalues. So one spectrum carries a one-parameter family of frames in which only the azimuth of the rotation axis about the boost axis changes.

For the worked element, with $\vec u_{\mathrm b}=\vec e_x$, the eigenvalues are $1.624811-1.300243i$ and $0.375189+0.300243i$ at $\phi=0$, $0.3$, $1$ and $2.5$ radians alike, to six decimal places. The frames differ; the spectrum does not.

### The Verification

Take $\theta_{\mathrm{rpd}}=0.8$ and the two axes $\vec e_x$ and $\vec e_y$. The two frames' eigenvalues are both

$$
e^{\theta_{\mathrm{rpd}}/2}=1.491825,\qquad e^{-\theta_{\mathrm{rpd}}/2}=0.670320,
$$

to six places, so the spectra are equal. The matrices differ, and the difference has norm $0.821505$ — not a small discrepancy but a difference of the same order as the elements themselves.

So the counterexample is not exotic: two of the three coordinate axes give it, and every pair of distinct axes does.

### What the Class Means

The class is the set of observers who agree on "how fast" but not on "in which direction". That is a real physical situation: two observers moving at the same speed in different directions have the same dilation factor and different frames, and no measurement of their clock rates alone tells them apart.

### Why the Count Is the Answer

The question "does the spectrum determine the frame" is answered by the dimension of the class: a positive-dimensional class means no, and the dimension says by how much. So the article's answer is not merely negative but quantitative, and the number is two.

## The Two Discrete Choices

### The Order

The two eigenvalues are $\mu$ and $\mu^{-1}$ and the two projectors are $\Pi_+$ and $\Pi_-$; nothing in the spectrum says which goes with which. Exchanging them replaces $\mu$ by $\mu^{-1}$, that is, reverses the sign of the parameter. So the order is the choice of sign of the rapidity or of the angle, and the block fixes it by requiring $\theta_{\mathrm{rpd}}\ge0$.

For a boost this is not a symmetry of the parametrisation but a convention: the boost along $\vec u$ with rapidity $\theta_{\mathrm{rpd}}$ equals the boost along $-\vec u$ with rapidity $-\theta_{\mathrm{rpd}}$, and the spectrum is the same for both.

### The Sheet

$\tilde U$ and $-\tilde U$ are different elements of $G$ with different spectra and the same Lorentz transformation. The block's rule is that the rotor is the physical object and the transformation is its congruence class: so a statement about the spectrum is a statement about the rotor and not about the transformation, and the sheet must be fixed separately, by positivity of the boost factor.

### Why Both Are Discrete

Neither ambiguity is continuous: one is a swap of two labels, the other a global sign. That is why the two-to-one cover and the ordering ambiguity are harmless in a formula that computes a *magnitude* and fatal in a formula that computes a *phase*. The interference experiments of *The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form* are the experiments that see the difference.

## Summary

The spectrum of a rotor is two eigenvalues whose product is one, that is two real parameters: a modulus and a phase. The rotor has six. For the normal elements — boosts, rotations, and products about commuting axes — the spectrum plus the two eigenprojectors is exactly the element, four parameters, and the projectors supply the axis that the spectrum cannot. For a general element even that fails, because there is no eigenbasis, and the failure is the Thomas–Wigner rotation. Two discrete choices remain in every case: the order of the eigenvalues, fixed by requiring a non-negative rapidity, and the sheet, fixed by positivity. A computation that uses only the spectrum is a computation of a magnitude, and a computation that needs a direction needs the projectors.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mu_\pm$ | the two eigenvalues of a rotor, $\mu_+\mu_-=1$ |
| $\varrho\,e^{i\theta_{\mathrm{pha}}}$, $\theta_{\mathrm{pha}}$ | modulus and phase of $\mu$, with $\theta_{\mathrm{pha}}=\theta_{\mathrm{axr}}/2$ on a rotation |
| $N=Q_t^{2}+B^{2}$ | the norm, the product of the two eigenvalues |
| $Q_t$, $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | scalar part and squared vector part of the rotor |
| $\Pi_\pm$ | the eigenprojectors, Hermitian idempotents of trace one |
| $\tilde V$ | the diagonalising unitary |
| $\tilde W=\operatorname{diag}(e^{i\theta_{\mathrm{axr}}/2},e^{-i\theta_{\mathrm{axr}}/2})$ | the residual freedom of the diagonalisation, a rotation through $\theta_{\mathrm{axr}}$ |

## Further Reading

- R. A. Horn and C. R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press, 2012 — the spectral theorem for normal matrices, the non-uniqueness of the diagonalising unitary, and the classification of normal forms.
- S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Academic Press, 1978 — conjugacy classes of $SL(2,\mathbb{C})$ and the elliptic, hyperbolic and parabolic trichotomy.
- P. Lounesto, *Clifford Algebras and Spinors*, 2nd ed., Cambridge University Press, 2001 — spectral decompositions in Clifford algebras, with the idempotents written explicitly.
- *The Two Eigenvalues Are the Two Weyl Weights* — the spectrum of the boost family computed.
- *When the Axes Commute: The Normal Transformations* — the class of elements for which a diagonalising unitary exists.
- *The Complete Polar Decomposition of an N-Regular Biquaternion* — the source of the worked element and of the normal-case reading compared here.
- *Relations between the Complete Polar Decomposition and Eigenbasis of an N-Regular Biquaternion* — the general case and the one-parameter family, in the mathematics corpus.
