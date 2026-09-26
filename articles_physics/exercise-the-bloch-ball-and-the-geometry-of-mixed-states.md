# __Exercise: The Bloch Ball and the Geometry of Mixed States__

## Introduction

This article is a **worked exercise** on the geometry of the qubit state space. It is a set of six problems on one theme, and it applies the state-space results established in the companion article *The Bloch Ball as the Trace-One Slice of the Future Light Cone*. The reader is assumed to have read that article; the exercise exists precisely to test it, so nothing is carried over except what that article establishes.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$, and $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$. The quaternion units are $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the scalar imaginary, $i^2 = -1$. The real-quaternion subspace is $\mathbb{H}_{\mathbb{B}}$ and the center is $\mathbb{C}_{\mathbb{B}}$. The trace of an element of $\mathbb{M}_+$ is twice its scalar part, $\mathrm{Tr}(\tilde{H}) = 2\,\mathrm{Sc}(\tilde{H})$.

**Assumed results.** From the parent article we take, without rederivation, the following. A state is an element

$$
\tilde{\rho} = \tfrac{1}{2}\bigl(e_0 + i\mathbf{r}\bigr), \qquad \mathbf{r} = r_1 e_1 + r_2 e_2 + r_3 e_3 \in \mathbb{R}^3,
$$

with $\mathbf{r}$ the **Bloch vector**; it is a state exactly when $|\mathbf{r}| \leq 1$, i.e. when it lies in the closed unit ball $B^3$. The norm form on the trace-one slice is $\tilde{\rho}\bar{\tilde{\rho}} = \tfrac{1}{4}(1 - |\mathbf{r}|^2)e_0$. The eigenvalues are $\lambda_\pm = \tfrac{1}{2}(1 \pm |\mathbf{r}|)$. The purity is $\mathrm{Tr}(\tilde{\rho}^2) = \tfrac{1}{2}(1 + |\mathbf{r}|^2)$ and the linear entropy is $S_{\mathrm{lin}}(\tilde{\rho}) = 1 - \mathrm{Tr}(\tilde{\rho}^2) = \tfrac{1}{2}(1 - |\mathbf{r}|^2)$. The von Neumann entropy is $S(\tilde{\rho}) = -\lambda_+\log\lambda_+ - \lambda_-\log\lambda_-$. The trace pairing on the slice is

$$
\mathrm{Tr}(\tilde{\rho}\tilde{\sigma}) = \tfrac{1}{2}\bigl(1 + \mathbf{r}\cdot\mathbf{s}\bigr), \qquad \tilde{\sigma} = \tfrac{1}{2}\bigl(e_0 + i\mathbf{s}\bigr),
$$

the squared Hilbert–Schmidt distance is $\mathrm{Tr}((\tilde{\rho}-\tilde{\sigma})^2) = \tfrac{1}{2}|\mathbf{r}-\mathbf{s}|^2$, the Uhlmann transition probability is $\tfrac{1}{2}(1 + \mathbf{r}\cdot\mathbf{s} + \sqrt{(1-|\mathbf{r}|^2)(1-|\mathbf{s}|^2)})$, and convex combinations act on Bloch vectors by the same weights. The pure states are the idempotents $\tilde{P}_\pm(\hat{\boldsymbol{\mu}}) = \tfrac{1}{2}(e_0 \pm i\hat{\boldsymbol{\mu}})$ with $|\hat{\boldsymbol{\mu}}| = 1$, forming the boundary sphere, and the maximally mixed state is the center $\mathbf{r} = 0$.

**What is to be shown.** Six problems: (1) the parametrisation of a mixed state by its Bloch vector; (2) purity, linear entropy, and von Neumann entropy for explicit states; (3) the geometry of convex combinations; (4) the metric and distinguishability structure; (5) the center and the boundary; (6) when two Bloch vectors give identical or orthogonal states. Each is solved in full, and numerical values are given where they aid the check.

## Problem 1: Parametrising a Mixed State by Its Bloch Vector

**Problem.** (a) A qubit is prepared by mixing the spin-up and spin-down states along the $z$-axis with probabilities $\tfrac34$ and $\tfrac14$. Write the state in the form $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$ and read off $\mathbf{r}$. (b) Conversely, for $\mathbf{r} = \tfrac12(e_1 + e_2)$, write $\tilde{\rho}$ and its spectral decomposition. (c) Verify that under the isomorphism $e_j \mapsto -i\sigma_j$ the state maps to $\tfrac12(I + \mathbf{r}\cdot\boldsymbol{\sigma})$, and identify the components $r_k$.

**Solution.** (a) The two pure states along $\pm z$ are the idempotents

$$
\tilde{P}_+(e_3) = \tfrac{1}{2}\bigl(e_0 + i e_3\bigr), \qquad \tilde{P}_-(e_3) = \tilde{P}_+(-e_3) = \tfrac{1}{2}\bigl(e_0 - i e_3\bigr).
$$

The mixture is a convex combination, so its Bloch vector is the same weighted combination of $e_3$ and $-e_3$:

$$
\tilde{\rho} = \tfrac34 \tilde{P}_+(e_3) + \tfrac14 \tilde{P}_-(e_3)
= \tfrac{3}{8}\bigl(e_0 + ie_3\bigr) + \tfrac{1}{8}\bigl(e_0 - ie_3\bigr)
= \tfrac12 e_0 + \tfrac14 i e_3
= \tfrac12\Bigl(e_0 + i\,\tfrac12 e_3\Bigr).
$$

Hence $\mathbf{r} = \tfrac12 e_3$, with $|\mathbf{r}| = \tfrac12 \leq 1$. The state is mixed, as expected from a nontrivial mixture, and its eigenvalues are $\lambda_\pm = \tfrac12(1 \pm \tfrac12) = \tfrac34, \tfrac14$: the two preparation probabilities, recovered from the Bloch vector.

(b) For $\mathbf{r} = \tfrac12(e_1 + e_2)$ we have $|\mathbf{r}|^2 = \tfrac14 + \tfrac14 = \tfrac12$, so $|\mathbf{r}| = 1/\sqrt2$. The state is

$$
\tilde{\rho} = \tfrac12\Bigl(e_0 + i\,\tfrac12(e_1 + e_2)\Bigr) = \tfrac12 e_0 + \tfrac14 i(e_1 + e_2).
$$

With $\hat{\mathbf{r}} = \mathbf{r}/|\mathbf{r}| = (e_1 + e_2)/\sqrt2$ and $\lambda_\pm = \tfrac12(1 \pm 1/\sqrt2)$, the spectral decomposition is

$$
\tilde{\rho} = \lambda_+ \tilde{P}_+(\hat{\mathbf{r}}) + \lambda_- \tilde{P}_-(\hat{\mathbf{r}}),
\qquad
\tilde{P}_\pm(\hat{\mathbf{r}}) = \tfrac12\bigl(e_0 \pm i\hat{\mathbf{r}}\bigr).
$$

This is correct because the two idempotents reconstruct the state,

$$
\lambda_+ \tilde{P}_+(\hat{\mathbf{r}}) + \lambda_- \tilde{P}_-(\hat{\mathbf{r}})
= \tfrac12(\lambda_+ + \lambda_-)e_0 + \tfrac12(\lambda_+ - \lambda_-) i\hat{\mathbf{r}}
= \tfrac12 e_0 + \tfrac{1}{2\sqrt2}\, i\,\frac{e_1 + e_2}{\sqrt2}
= \tfrac12 e_0 + \tfrac14 i(e_1 + e_2),
$$

where we used $\lambda_+ + \lambda_- = 1$ and $\lambda_+ - \lambda_- = 1/\sqrt2$. Every mixed state is thus a mixture of two orthogonal pure states along its own Bloch direction, with weights fixed by the radius.

(c) Since $e_0 \mapsto I$ and $e_j \mapsto -i\sigma_j$, we have $i e_j \mapsto i(-i\sigma_j) = \sigma_j$, so

$$
\tilde{\rho} = \tfrac12\bigl(e_0 + i\textstyle\sum_j r_j e_j\bigr) \;\longmapsto\; \tfrac12\Bigl(I + \sum_j r_j \sigma_j\Bigr) = \tfrac12\bigl(I + \mathbf{r}\cdot\boldsymbol{\sigma}\bigr),
$$

the standard Bloch parametrisation of a qubit density matrix. The components are the Pauli expectations: using the trace pairing with the observable $i e_k \mapsto \sigma_k$,

$$
r_k = \mathrm{Tr}\bigl(\tilde{\rho}\,(i e_k)\bigr) = \langle \sigma_k\rangle_{\tilde{\rho}},
$$

so the Bloch vector *is* the vector of single-qubit expectation values, $\mathbf{r} = (\langle\sigma_1\rangle, \langle\sigma_2\rangle, \langle\sigma_3\rangle)$. In particular, measuring the spin along a unit direction $\hat{\mathbf{n}}$ gives outcomes with probabilities $p_\pm = \tfrac12(1 \pm \hat{\mathbf{n}}\cdot\mathbf{r})$, so the projection of $\mathbf{r}$ along $\hat{\mathbf{n}}$ is the bias of the measurement.

## Problem 2: Purity, Linear Entropy, and von Neumann Entropy

**Problem.** For each of the following states compute the purity $\mathrm{Tr}(\tilde{\rho}^2)$, the linear entropy $S_{\mathrm{lin}}$, and the von Neumann entropy $S(\tilde{\rho})$: (a) the pure state with $\hat{\mathbf{n}} = (1,1,1)/\sqrt3$; (b) the maximally mixed state; (c) the state with $\mathbf{r} = \tfrac12 e_3$; (d) the state with $\mathbf{r} = \tfrac12(e_1 + e_2)$. Confirm that all three quantities depend on the state only through $|\mathbf{r}|$.

**Solution.** All three quantities are functions of the radius alone:

$$
\mathrm{Tr}(\tilde{\rho}^2) = \tfrac12\bigl(1 + |\mathbf{r}|^2\bigr), \qquad
S_{\mathrm{lin}} = 1 - \mathrm{Tr}(\tilde{\rho}^2) = \tfrac12\bigl(1 - |\mathbf{r}|^2\bigr),
$$

$$
S(\tilde{\rho}) = -\lambda_+\log\lambda_+ - \lambda_-\log\lambda_-, \qquad \lambda_\pm = \tfrac12\bigl(1 \pm |\mathbf{r}|\bigr),
$$

so that states of equal radius — the concentric spheres of the ball — are equally pure and equally entropic.

**(a) Pure state, $|\mathbf{r}| = 1$.** The purity is $\tfrac12(1+1) = 1$, the linear entropy is $0$, the eigenvalues are $\lambda_\pm = 1, 0$, and $S = -1\log 1 - 0 = 0$. Purity is the boundary condition.

**(b) Maximally mixed state, $|\mathbf{r}| = 0$.** The purity is $\tfrac12(1+0) = \tfrac12$, the linear entropy is $\tfrac12$, the eigenvalues are $\lambda_\pm = \tfrac12, \tfrac12$, and

$$
S = -\tfrac12\log\tfrac12 - \tfrac12\log\tfrac12 = \log 2 \approx 0.693147 \ \text{nats} = 1 \ \text{bit}.
$$

This is the maximum on the ball.

**(c) $\mathbf{r} = \tfrac12 e_3$, $|\mathbf{r}| = \tfrac12$.** The purity is $\tfrac12(1 + \tfrac14) = \tfrac58$, the linear entropy is $1 - \tfrac58 = \tfrac38$, and the eigenvalues are $\lambda_\pm = \tfrac34, \tfrac14$, so

$$
S = -\tfrac34\log\tfrac34 - \tfrac14\log\tfrac14
= \tfrac34\log\tfrac43 + \tfrac14\log 4
\approx 0.562335 \ \text{nats} \approx 0.811278 \ \text{bits}.
$$

**(d) $\mathbf{r} = \tfrac12(e_1+e_2)$, $|\mathbf{r}| = 1/\sqrt2$.** The purity is $\tfrac12(1 + \tfrac12) = \tfrac34$, the linear entropy is $\tfrac14$, and with $\lambda_\pm = \tfrac12(1 \pm 1/\sqrt2) \approx 0.853553, 0.146447$,

$$
S \approx 0.416496 \ \text{nats} \approx 0.600876 \ \text{bits}.
$$

Comparing (c) and (d) illustrates the monotonicity: as the radius grows from $\tfrac12$ to $1/\sqrt2$, the purity grows from $\tfrac58$ to $\tfrac34$ and the entropy falls from about $0.5623$ to about $0.4165$ nats. As in the parent article, the base of the logarithm is a convention; natural logarithms (nats) are used here, and the bit values are the same numbers divided by $\log 2$.

## Problem 3: Convex Combinations and Where Mixtures Land

**Problem.** (a) Show that a convex combination of states is a state whose Bloch vector is the same convex combination of the Bloch vectors. (b) For a mixture of two pure states with Bloch directions $\hat{\boldsymbol{\mu}}, \hat{\boldsymbol{\nu}}$ at angle $\theta$, with weights $p$ and $1-p$, compute the radius and the purity of the mixture. (c) Determine exactly when such a mixture is again pure. (d) Evaluate the mixture of the pure states along $z$ and along $x$ with equal weights, and the mixture with weights $\tfrac34, \tfrac14$.

**Solution.** (a) Write $\tilde{\rho}_i = \tfrac12(e_0 + i\mathbf{r}_i)$ and let $p_i \geq 0$ with $\sum_i p_i = 1$. Then

$$
\sum_i p_i \tilde{\rho}_i = \tfrac12\sum_i p_i e_0 + \tfrac12 i \sum_i p_i \mathbf{r}_i = \tfrac12\Bigl(e_0 + i \sum_i p_i \mathbf{r}_i\Bigr).
$$

Since each $\tilde{\rho}_i$ is Hermitian of trace one, so is the combination, and its Bloch vector is $\mathbf{r} = \sum_i p_i \mathbf{r}_i$. By convexity of the ball, $|\mathbf{r}| \leq \sum_i p_i |\mathbf{r}_i| \leq 1$, so the combination is again a state. The map $\mathbf{r} \leftrightarrow \tilde{\rho}$ is affine, so the ball is a faithful affine model of the state space.

(b) Let $\hat{\boldsymbol{\mu}}, \hat{\boldsymbol{\nu}}$ be unit vectors with $\hat{\boldsymbol{\mu}}\cdot\hat{\boldsymbol{\nu}} = \cos\theta$, and set $\mathbf{r} = p\hat{\boldsymbol{\mu}} + (1-p)\hat{\boldsymbol{\nu}}$. Then

$$
|\mathbf{r}|^2 = p^2 + (1-p)^2 + 2p(1-p)\cos\theta
= 1 - 2p(1-p)\bigl(1 - \cos\theta\bigr).
$$

The mixture therefore lies on the chord joining $\hat{\boldsymbol{\mu}}$ and $\hat{\boldsymbol{\nu}}$, at the point that divides it in the ratio $(1-p) : p$. Its purity and linear entropy are

$$
\mathrm{Tr}(\tilde{\rho}^2) = \tfrac12\bigl(1 + |\mathbf{r}|^2\bigr) = 1 - p(1-p)\bigl(1-\cos\theta\bigr),
\qquad
S_{\mathrm{lin}} = p(1-p)\bigl(1-\cos\theta\bigr).
$$

(c) From the second form, $|\mathbf{r}| = 1$ requires $p(1-p)(1-\cos\theta) = 0$, i.e. $p = 0$, or $p = 1$, or $\cos\theta = 1$ (the two pure states coincide). Apart from these degenerate cases the mixture is **strictly interior**: $|\mathbf{r}| < 1$, and the ball is strictly convex. In particular, a nontrivial mixture of two distinct pure states is never pure.

(d) Take $\hat{\boldsymbol{\mu}} = e_3$ and $\hat{\boldsymbol{\nu}} = e_1$, so $\theta = \pi/2$ and $\cos\theta = 0$. With $p = \tfrac12$,

$$
\mathbf{r} = \tfrac12(e_1 + e_3), \qquad |\mathbf{r}|^2 = 1 - 2\cdot\tfrac14\cdot 1 = \tfrac12, \qquad |\mathbf{r}| = 1/\sqrt2,
$$

so the purity is $\tfrac34$, the linear entropy is $\tfrac14$, and the entropy is about $0.416496$ nats — the value found in Problem 2(d), as it must be. With $p = \tfrac34$,

$$
\mathbf{r} = \tfrac34 e_3 + \tfrac14 e_1, \qquad |\mathbf{r}|^2 = 1 - 2\cdot\tfrac34\cdot\tfrac14 = \tfrac58,
$$

so the purity is $\tfrac12(1 + \tfrac58) = \tfrac{13}{16}$ and the linear entropy is $\tfrac{3}{16}$. A useful special case is $\theta = \pi$ (complementary pure states $\hat{\boldsymbol{\nu}} = -\hat{\boldsymbol{\mu}}$): then $\mathbf{r} = (2p-1)\hat{\boldsymbol{\mu}}$, $|\mathbf{r}| = |2p-1|$, and the equal mixture $p = \tfrac12$ gives $\mathbf{r} = 0$, the maximally mixed state, independently of the axis $\hat{\boldsymbol{\mu}}$.

## Problem 4: The Metric and Distinguishability Structure

**Problem.** (a) Compute the squared Hilbert–Schmidt distance $\mathrm{Tr}((\tilde{\rho}-\tilde{\sigma})^2)$ in terms of the Bloch vectors. (b) Compute the trace distance $D(\tilde{\rho},\tilde{\sigma}) = \tfrac12\mathrm{Tr}|\tilde{\rho}-\tilde{\sigma}|$, verify the parent's formula for the distance to the center, and relate the two distances. (c) Evaluate both for $\mathbf{r} = \tfrac12 e_3$ and $\mathbf{s} = \tfrac12 e_1$, and compute the trace distance between two pure states as a function of the angle. (d) State the range of $D$ on the ball.

**Solution.** (a) The difference of two states is

$$
\tilde{\rho} - \tilde{\sigma} = \tfrac12 i(\mathbf{r} - \mathbf{s}), \qquad \mathbf{r} - \mathbf{s} \in \mathbb{H}_{\mathbb{B}} \text{ a pure real quaternion.}
$$

For a pure real quaternion $\mathbf{u} = \mathbf{r} - \mathbf{s}$ one has $\mathbf{u}^2 = -|\mathbf{u}|^2 e_0$, hence

$$
(\tilde{\rho} - \tilde{\sigma})^2 = \tfrac14 (i\mathbf{u})^2 = -\tfrac14 \mathbf{u}^2 = \tfrac14 |\mathbf{r}-\mathbf{s}|^2\, e_0 .
$$

Taking the trace, $\mathrm{Tr}((\tilde{\rho}-\tilde{\sigma})^2) = 2\cdot\tfrac14|\mathbf{r}-\mathbf{s}|^2 = \tfrac12|\mathbf{r}-\mathbf{s}|^2$, which is the parent's Hilbert–Schmidt formula. Since $(\tilde{\rho}-\tilde{\sigma})^2$ is a scalar multiple of $e_0$, the traceless difference $\tilde{\rho}-\tilde{\sigma}$ has eigenvalues $\pm\tfrac12|\mathbf{r}-\mathbf{s}|$.

(b) The absolute value is

$$
|\tilde{\rho}-\tilde{\sigma}| = \sqrt{(\tilde{\rho}-\tilde{\sigma})^2} = \tfrac12|\mathbf{r}-\mathbf{s}|\,e_0,
$$

the positive square root in $\mathbb{M}_+$. Hence

$$
D(\tilde{\rho},\tilde{\sigma}) = \tfrac12\mathrm{Tr}|\tilde{\rho}-\tilde{\sigma}|
= \tfrac12\cdot\tfrac12|\mathbf{r}-\mathbf{s}|\cdot\mathrm{Tr}(e_0)
= \tfrac12|\mathbf{r}-\mathbf{s}| .
$$

Setting $\mathbf{s} = 0$ recovers the parent's statement $D(\tilde{\rho},\tfrac12 e_0) = \tfrac12|\mathbf{r}|$. Comparing with (a), the trace distance and the Hilbert–Schmidt distance carry the same information on a qubit,

$$
\mathrm{Tr}\bigl((\tilde{\rho}-\tilde{\sigma})^2\bigr) = 2\,D(\tilde{\rho},\tilde{\sigma})^2,
\qquad
D = \sqrt{\tfrac12\,\mathrm{Tr}\bigl((\tilde{\rho}-\tilde{\sigma})^2\bigr)} .
$$

Both are monotone functions of the Euclidean separation $|\mathbf{r}-\mathbf{s}|$; the trace distance is the one with the operational meaning, being half the trace-norm difference of the two states.

(c) For $\mathbf{r} = \tfrac12 e_3$ and $\mathbf{s} = \tfrac12 e_1$, $|\mathbf{r}-\mathbf{s}| = \tfrac12\sqrt2 = 1/\sqrt2$, so the Hilbert–Schmidt distance squared is $\tfrac12\cdot\tfrac12 = \tfrac14$, and

$$
D = \tfrac12\cdot\tfrac1{\sqrt2} = \frac{1}{2\sqrt2} \approx 0.353553 .
$$

For two pure states $\mathbf{r} = \hat{\boldsymbol{\mu}}$, $\mathbf{s} = \hat{\boldsymbol{\nu}}$ at angle $\theta$, $|\mathbf{r}-\mathbf{s}| = \sqrt{2 - 2\cos\theta} = 2\sin(\theta/2)$, so

$$
D\bigl(\tilde{P}(\hat{\boldsymbol{\mu}}), \tilde{P}(\hat{\boldsymbol{\nu}})\bigr) = \sin\frac{\theta}{2}.
$$

Together with the transition probability $\mathrm{Tr}(\tilde{P}(\hat{\boldsymbol{\mu}})\tilde{P}(\hat{\boldsymbol{\nu}})) = \cos^2(\theta/2)$ this gives the clean pair

$$
D^2 + \mathrm{Tr}(\tilde{P}\tilde{Q}) = 1 \qquad \text{for pure states,}
$$

so the two notions of separation are complementary on the boundary: coincident directions give $D = 0$ and transition probability $1$, antipodal directions give $D = 1$ and transition probability $0$.

(d) Since $|\mathbf{r}-\mathbf{s}| \leq |\mathbf{r}| + |\mathbf{s}| \leq 2$, we have $0 \leq D \leq 1$. The upper bound is attained exactly when $|\mathbf{r}| = |\mathbf{s}| = 1$ and $\mathbf{s} = -\mathbf{r}$, the case of orthogonal states treated in Problem 6. The trace distance is thus bounded by the information-theoretic maximum $1$, the probability of perfectly distinguishing the two states, and it reaches it only at the two ends of a diameter.

## Problem 5: The Centre and the Boundary

**Problem.** (a) Characterize the center of the ball and compute its purity, entropies, and norm form. (b) Characterize the boundary and show that a boundary state is an extreme point that cannot be written as a nontrivial convex combination. (c) Show that the elements of the trace-one hyperplane with $|\mathbf{r}| > 1$ are not states.

**Solution.** (a) The center is $\mathbf{r} = 0$, i.e.

$$
\tilde{\rho} = \tfrac12 e_0,
$$

the maximally mixed state. Its purity is $\mathrm{Tr}(\tilde{\rho}^2) = \tfrac12(1+0) = \tfrac12$, the minimum on the ball; its linear entropy is $\tfrac12$, the maximum; its norm form is $\tilde{\rho}\bar{\tilde{\rho}} = \tfrac14 e_0$, whose scalar coefficient $\tfrac14$ is the largest attainable on the slice; and its von Neumann entropy is $\log 2$, the maximum. In the spectral form it is the equal mixture $\tfrac12\tilde{P}_+(\hat{\boldsymbol{\mu}}) + \tfrac12\tilde{P}_-(\hat{\boldsymbol{\mu}})$ of the complementary idempotents along **any** axis, and it is the unique state invariant under the full unitary group $U(2)$, which acts on the ball by rotations. It is also the barycenter: the uniform average of the pure states over the boundary sphere is

$$
\frac{1}{4\pi}\int_{S^2}\tilde{P}(\hat{\boldsymbol{\mu}})\,d\Omega
= \tfrac12\Bigl(e_0 + i\,\frac{1}{4\pi}\int_{S^2}\hat{\boldsymbol{\mu}}\,d\Omega\Bigr)
= \tfrac12 e_0,
$$

because the mean of the unit vector over the sphere vanishes.

(b) The boundary is $|\mathbf{r}| = 1$. For these states the norm form vanishes,

$$
\tilde{\rho}\bar{\tilde{\rho}} = \tfrac14(1 - |\mathbf{r}|^2)e_0 = 0 \quad\Longleftrightarrow\quad |\mathbf{r}| = 1,
$$

so a boundary state is a zero divisor of $\mathbb{B}$; the deviation from idempotency,

$$
\tilde{\rho}^2 - \tilde{\rho} = \tfrac14\bigl(|\mathbf{r}|^2 - 1\bigr)e_0,
$$

vanishes exactly there, so a boundary state is an idempotent, hence a rank-one projection; and its eigenvalues are $\lambda_\pm = 1, 0$, so its purity is $1$ and its entropy $0$. The boundary is parametrized by the unit sphere $S^2$: $\mathbf{r} = \hat{\boldsymbol{\mu}}$ gives the idempotent $\tilde{P}_+(\hat{\boldsymbol{\mu}})$, and $-\hat{\boldsymbol{\mu}}$ gives its orthogonal complement $\tilde{P}_-(\hat{\boldsymbol{\mu}})$, with $\tilde{P}_+ + \tilde{P}_- = e_0$ and $\tilde{P}_+\tilde{P}_- = 0$.

A boundary state is an **extreme point** of the ball. Suppose $\tilde{P} = \lambda\tilde{\rho}_1 + (1-\lambda)\tilde{\rho}_2$ with $0 < \lambda < 1$. Then $\mathbf{r} = \lambda\mathbf{r}_1 + (1-\lambda)\mathbf{r}_2$ with $|\mathbf{r}_1|, |\mathbf{r}_2| \leq 1$ and $|\mathbf{r}| = 1$. By the strict convexity of the Euclidean norm, equality $|\mathbf{r}| = 1$ forces $\mathbf{r}_1 = \mathbf{r}_2 = \mathbf{r}$, so $\tilde{\rho}_1 = \tilde{\rho}_2 = \tilde{P}$: no boundary state is a nontrivial mixture. Conversely, every interior state is a nontrivial mixture (Problem 3), so the extreme points of the ball are exactly the pure states.

(c) On the trace-one hyperplane an element $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$ has eigenvalues $\lambda_\pm = \tfrac12(1 \pm |\mathbf{r}|)$. If $|\mathbf{r}| > 1$ then $\lambda_- = \tfrac12(1 - |\mathbf{r}|) < 0$, so $\tilde{\rho}$ is Hermitian of trace one but not positive semidefinite, and is not a state. Its norm form is $\tfrac14(1 - |\mathbf{r}|^2)e_0$ with negative scalar coefficient, so it lies in the spacelike region outside the future cone. For instance $\mathbf{r} = 2e_3$ gives $\lambda_\pm = \tfrac32, -\tfrac12$. The ball $|\mathbf{r}| \leq 1$ is thus exactly the positivity domain on the slice.

## Problem 6: Identical and Orthogonal States

**Problem.** (a) Determine when two states are identical. (b) Determine when two states have orthogonal support, i.e. when $\mathrm{Tr}(\tilde{\rho}\tilde{\sigma}) = 0$. (c) Specialize to pure states and express the result in terms of the angle. (d) Show that the Uhlmann transition probability vanishes under the same condition.

**Solution.** (a) Two states are identical exactly when their Bloch vectors are equal: from $\tilde{\rho} - \tilde{\sigma} = \tfrac12 i(\mathbf{r}-\mathbf{s})$ we have $\tilde{\rho} = \tilde{\sigma}$ iff $\mathbf{r} = \mathbf{s}$. In that case the Hilbert–Schmidt and trace distances vanish, the transition probability is $1$, and all radius-dependent quantities (purity, entropies) coincide. Conversely, equal purity does **not** imply identical states: by Problem 2 all states of a given radius share the same purity and entropy, and they are rotated into one another by $U(2)$.

(b) The trace pairing on the slice is $\mathrm{Tr}(\tilde{\rho}\tilde{\sigma}) = \tfrac12(1 + \mathbf{r}\cdot\mathbf{s})$. Because $\tilde{\rho},\tilde{\sigma}$ are positive and of trace one, orthogonality of their supports is equivalent to the vanishing of this pairing. Thus

$$
\mathrm{Tr}(\tilde{\rho}\tilde{\sigma}) = 0
\quad\Longleftrightarrow\quad \mathbf{r}\cdot\mathbf{s} = -1 .
$$

Since $|\mathbf{r}\cdot\mathbf{s}| \leq |\mathbf{r}|\,|\mathbf{s}| \leq 1$, the equality $\mathbf{r}\cdot\mathbf{s} = -1$ forces both Cauchy–Schwarz and the ball bounds to be saturated:

$$
|\mathbf{r}| = |\mathbf{s}| = 1, \qquad \mathbf{s} = -\mathbf{r}.
$$

So two qubit states have orthogonal supports **if and only if** they are the two complementary pure states along a common axis.

(c) For pure states $\mathbf{r} = \hat{\boldsymbol{\mu}}$, $\mathbf{s} = \hat{\boldsymbol{\nu}}$, the transition probability is the trace pairing,

$$
\mathrm{Tr}\bigl(\tilde{P}(\hat{\boldsymbol{\mu}})\tilde{P}(\hat{\boldsymbol{\nu}})\bigr)
= \tfrac12\bigl(1 + \hat{\boldsymbol{\mu}}\cdot\hat{\boldsymbol{\nu}}\bigr) = \cos^2\frac{\theta}{2},
$$

where $\theta$ is the angle between the Bloch directions. It equals $1$ for $\theta = 0$ (identical states) and $0$ for $\theta = \pi$ (orthogonal states, $\hat{\boldsymbol{\nu}} = -\hat{\boldsymbol{\mu}}$). Equivalently, $\hat{\boldsymbol{\mu}}\cdot\hat{\boldsymbol{\nu}} = -1$, the same condition as in (b). As a concrete check, take $\hat{\boldsymbol{\mu}} = e_3$, $\hat{\boldsymbol{\nu}} = -e_3$: then $\tilde{P}_+(e_3)\tilde{P}_-(e_3) = 0$ and $\mathrm{Tr}(\tilde{P}_+(e_3)\tilde{P}_-(e_3)) = \tfrac12(1 - 1) = 0$, while $\tilde{P}_+ + \tilde{P}_- = e_0$.

(d) For general states the relevant overlap is the Uhlmann transition probability,

$$
T(\tilde{\rho},\tilde{\sigma})
= \tfrac12\Bigl(1 + \mathbf{r}\cdot\mathbf{s} + \sqrt{\bigl(1-|\mathbf{r}|^2\bigr)\bigl(1-|\mathbf{s}|^2\bigr)}\Bigr),
$$

which for mixed states differs from the Hilbert–Schmidt pairing $\mathrm{Tr}(\tilde{\rho}\tilde{\sigma})$. Setting $T = 0$ gives

$$
\mathbf{r}\cdot\mathbf{s} = -1 - \sqrt{\bigl(1-|\mathbf{r}|^2\bigr)\bigl(1-|\mathbf{s}|^2\bigr)} \leq -1 .
$$

Combined with $\mathbf{r}\cdot\mathbf{s} \geq -|\mathbf{r}|\,|\mathbf{s}| \geq -1$, every inequality is an equality, so $|\mathbf{r}| = |\mathbf{s}| = 1$, $\mathbf{r}\cdot\mathbf{s} = -1$, and $\mathbf{s} = -\mathbf{r}$ — the same pure antipodal pair. Hence the transition probability vanishes under exactly the same condition as orthogonal support, and for mixed states it is strictly positive: a mixed state is never perfectly distinguishable from another. For example, with $\mathbf{r} = \tfrac12 e_3$ and $\mathbf{s} = \tfrac12 e_1$ one has $\mathbf{r}\cdot\mathbf{s} = 0$ and $\sqrt{(1-\tfrac14)(1-\tfrac14)} = \tfrac34$, so $T = \tfrac12(1 + \tfrac34) = \tfrac78$, consistent with the nonzero trace distance $D = 1/(2\sqrt2)$ found in Problem 4.

## Summary

We have worked six problems on the geometry of the qubit state space, using only the state-space results of the parent article.

**Parametrisation.** A state is $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$ with $|\mathbf{r}| \leq 1$; the components of $\mathbf{r}$ are the single-qubit expectation values $r_k = \langle\sigma_k\rangle$, and a measurement along $\hat{\mathbf{n}}$ has outcomes $\tfrac12(1 \pm \hat{\mathbf{n}}\cdot\mathbf{r})$.

**Purity and entropy.** Purity, linear entropy, and von Neumann entropy are functions of the radius alone: $\mathrm{Tr}(\tilde{\rho}^2) = \tfrac12(1+|\mathbf{r}|^2)$, $S_{\mathrm{lin}} = \tfrac12(1-|\mathbf{r}|^2)$, and $S = -\sum_\pm\lambda_\pm\log\lambda_\pm$ with $\lambda_\pm = \tfrac12(1\pm|\mathbf{r}|)$.

**Convex combinations.** A mixture of two pure states lies on the chord joining them, with $|\mathbf{r}|^2 = 1 - 2p(1-p)(1-\cos\theta)$ and linear entropy $p(1-p)(1-\cos\theta)$; it is pure only in the degenerate cases $p \in \{0,1\}$ or coincident directions.

**Metric.** The trace distance is $D = \tfrac12|\mathbf{r}-\mathbf{s}|$ and the squared Hilbert–Schmidt distance is $2D^2$. For pure states $D = \sin(\theta/2)$ and the transition probability is $\cos^2(\theta/2)$, so $D^2 + \mathrm{Tr}(\tilde{P}\tilde{Q}) = 1$.

**Centre and boundary.** The center is the maximally mixed state $\tfrac12 e_0$, with minimal purity $\tfrac12$ and maximal entropy $\log 2$; the boundary $|\mathbf{r}| = 1$ consists of the pure states, equivalently the idempotents, the zero divisors, and the extreme points. Elements with $|\mathbf{r}| > 1$ are not states.

**Identical and orthogonal.** Two states are identical iff $\mathbf{r} = \mathbf{s}$; they have orthogonal supports — and the Uhlmann transition probability vanishes — iff $\mathbf{r}\cdot\mathbf{s} = -1$, which forces $|\mathbf{r}| = |\mathbf{s}| = 1$ and $\mathbf{s} = -\mathbf{r}$. Only the two ends of a diameter are perfectly distinguishable.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathbb{C}_{\mathbb{B}}$ | Center of $\mathbb{B}$ |
| $\mathbb{M}_+$ | Hermitian subspace (states and observables) |
| $\mathbb{M}_-$ | Anti-Hermitian subspace, $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ |
| $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$ | State with Bloch vector $\mathbf{r}$ |
| $\tilde{P}_\pm(\hat{\boldsymbol{\mu}}) = \tfrac12(e_0 \pm i\hat{\boldsymbol{\mu}})$ | Pure-state idempotent, $|\hat{\boldsymbol{\mu}}| = 1$ |
| $\mathbf{r}\in B^3$, $|\mathbf{r}|\leq 1$ | Bloch ball |
| $\mathrm{Tr}(\tilde{\rho}^2) = \tfrac12(1+|\mathbf{r}|^2)$ | Purity |
| $S_{\mathrm{lin}} = 1-\mathrm{Tr}(\tilde{\rho}^2) = \tfrac12(1-|\mathbf{r}|^2)$ | Linear entropy |
| $S(\tilde{\rho}) = -\sum_\pm\lambda_\pm\log\lambda_\pm$ | Von Neumann entropy, $\lambda_\pm = \tfrac12(1\pm|\mathbf{r}|)$ |
| $\mathrm{Tr}(\tilde{\rho}\tilde{\sigma}) = \tfrac12(1+\mathbf{r}\cdot\mathbf{s})$ | Trace pairing |
| $D(\tilde{\rho},\tilde{\sigma}) = \tfrac12\mathrm{Tr}|\tilde{\rho}-\tilde{\sigma}| = \tfrac12|\mathbf{r}-\mathbf{s}|$ | Trace distance |
| $T(\tilde{\rho},\tilde{\sigma}) = \tfrac12(1+\mathbf{r}\cdot\mathbf{s}+\sqrt{(1-|\mathbf{r}|^2)(1-|\mathbf{s}|^2)})$ | Uhlmann transition probability |

## Further Reading

- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Bloch ball, the trace distance, and the fidelity.
- Ingemar Bengtsson and Karol Życzkowski, *Geometry of Quantum States* (Cambridge, 2006), for the convex and metric geometry of the state space.
- Asher Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for the operational meaning of distinguishability and the trace distance.
- Richard Jozsa, "Fidelity for mixed quantum states," *Journal of Modern Optics* **41** (1994) 2315–2323, for the closed-form Uhlmann transition probability of a qubit.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the spin-1/2 formalism and the Bloch vector.
- The companion article of this series: *The Bloch Ball as the Trace-One Slice of the Future Light Cone*, whose state-space results are applied throughout.
