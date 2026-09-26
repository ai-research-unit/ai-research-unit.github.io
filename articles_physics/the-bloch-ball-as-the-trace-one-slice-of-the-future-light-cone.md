# __The Bloch Ball as the Trace-One Slice of the Future Light Cone__

## Introduction

The companion articles established that the Hermitian subspace $\mathbb{M}_+$ of the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ carries the operator algebra of a two-state quantum system. Its Hermitian elements are the observables, its positive trace-one elements are the states, and the trace formula

$$
\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})
$$

is the Born rule. This article is about the **geometry** of that state space. Its subject is one structural fact, developed in full:

> The state space of a qubit — the Bloch ball — is the intersection of the affine hyperplane $\{\mathrm{Sc} = \tfrac{1}{2}\}$ in $\mathbb{M}_+$ with the future light cone of the norm form $N(\tilde{H}) = \tilde{H}\bar{\tilde{H}}$.

In the standard formalism the Bloch ball is assembled state by state: one takes the set of positive trace-one operators on a two-dimensional Hilbert space and derives the condition $|\mathbf{r}| \leq 1$ from the positivity of a $2 \times 2$ matrix. In the biquaternion framework the same object appears as a **slice of a cone by a hyperplane**. The three conditions that look independent in the matrix formalism — Hermitian, positive, trace one — become, in the algebra, membership in $\mathbb{M}_+$, a trace normalization, and a single quadratic inequality that is the causal condition of a Lorentzian form. Purity becomes a boundary condition; mixedness becomes the interior of the ball; and the zero divisors of the algebra at trace one, which elsewhere in the series describe light-like propagation, here describe the pure states.

The article is organized as follows. First the Hermitian subspace, its trace, and its norm form are recalled, together with the light cone and the zero divisors. Then the trace-one hyperplane is described and coordinatized by the Bloch vector. Then the Bloch ball is obtained as the slice of the future cone by that hyperplane, and the positivity of a state is identified with its causality. Then the pure states are characterized as the boundary of the ball — idempotents, extreme rays, and zero divisors at trace one — and the mixed states as its interior. Then purity, the Bloch radius, entropy, and fidelity are expressed in these terms. The article closes with the symmetries of the slice, with what the picture shows, and with open questions.

The conventions are those of the companion articles: the biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the scalar imaginary. The four fixed-point subspaces are $\mathbb{C}_{\mathbb{B}}$ (the complex subspace, the center of $\mathbb{B}$), $\mathbb{H}_{\mathbb{B}}$ (the real-quaternion subspace), and the two complementary four-dimensional subspaces $\mathbb{M}_+$ (Hermitian) and $\mathbb{M}_-$ (anti-Hermitian), with $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$. The trace is $\mathrm{Tr}(\tilde{H}) = 2\,\mathrm{Sc}(\tilde{H})$.

## The Hermitian Subspace and the Norm Form

### Coordinates and Trace

An element of the Hermitian subspace is written

$$
\tilde{H} = h_0\,e_0 + i\,\mathbf{h}, \qquad h_0 \in \mathbb{R}, \qquad \mathbf{h} = h_1 e_1 + h_2 e_2 + h_3 e_3,
$$

where $\mathbf{h}$ is a pure real quaternion, identified with the vector $(h_1, h_2, h_3) \in \mathbb{R}^3$. The scalar part $h_0 e_0$ lies in the center $\mathbb{C}_{\mathbb{B}}$; here it is real, and the imaginary vector part $i\mathbf{h}$ carries the three remaining real coordinates. A natural basis of $\mathbb{M}_+$ over $\mathbb{R}$ is

$$
\{e_0,\; i e_1,\; i e_2,\; i e_3\},
$$

so that $\mathbb{M}_+$ is a four-dimensional real vector space and the fixed-point set of the Hermitian conjugation $\dagger$. Its **trace** is twice the scalar part:

$$
\mathrm{Tr}(\tilde{H}) = 2 h_0 .
$$

### The Norm Form

The quaternion conjugate $\bar{\tilde{H}} = h_0 e_0 - i\mathbf{h}$ is again Hermitian, so quaternion conjugation preserves $\mathbb{M}_+$; it leaves the scalar part and negates the imaginary vector part. The **norm form** is

$$
N(\tilde{H}) = \tilde{H}\bar{\tilde{H}} = \bigl(h_0^2 - |\mathbf{h}|^2\bigr) e_0 ,
$$

a real-valued quadratic form on $\mathbb{M}_+$, of **signature $(1,3)$**: the scalar direction $e_0$ is positive, the three imaginary directions $i e_1, i e_2, i e_3$ are negative. This is the mirror image of the signature $(3,1)$ that the same norm form carries on the anti-Hermitian subspace $\mathbb{M}_-$.

The norm form is not the trace pairing. The trace pairing

$$
\mathrm{Tr}(\tilde{H}\tilde{K}) = 2\bigl(h_0 k_0 + \mathbf{h}\cdot\mathbf{k}\bigr)
$$

is positive-definite, of signature $(4,0)$; it is the analogue of the Hilbert–Schmidt inner product. The norm form and the trace pairing are distinct quadratic structures on the same four-dimensional space, and keeping them apart is essential: positivity of a state is a condition on the norm form, while the Born rule is a condition on the trace pairing.

### The Light Cone and the Zero Divisors

The vanishing of the norm form defines the **light cone** of $\mathbb{M}_+$:

$$
N(\tilde{H}) = 0 \quad\Longleftrightarrow\quad h_0^2 = |\mathbf{h}|^2 ,
$$

a double cone in $\mathbb{R}^4$ with apex at the origin. The complement of the cone has three connected components: the spacelike region $N < 0$ (a single component), and the two components of the timelike region $N > 0$, namely $h_0 > |\mathbf{h}|$ and $h_0 < -|\mathbf{h}|$. The first of these, $h_0 > |\mathbf{h}|$, is the **future** component.

Under the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ that maps $e_0 \mapsto I$ and $e_j \mapsto -i\sigma_j$, a Hermitian element $\tilde{H} = h_0 e_0 + i\mathbf{h}$ maps to the Hermitian matrix $h_0 I + \mathbf{h}\cdot\boldsymbol{\sigma}$, whose determinant is $h_0^2 - |\mathbf{h}|^2$. The norm form is therefore the determinant form:

$$
N(\tilde{H}) \;\longmapsto\; \det\bigl(h_0 I + \mathbf{h}\cdot\boldsymbol{\sigma}\bigr) I .
$$

Consequently the nonzero elements of the light cone are exactly the **zero divisors** of $\mathbb{B}$ that lie in $\mathbb{M}_+$: $N(\tilde{H}) = 0$ with $\tilde{H} \neq 0$ means the corresponding matrix is singular, hence a zero divisor. Conversely every zero divisor in $\mathbb{M}_+$ has vanishing norm form. This is the same zero-divisor cone that, in $\mathbb{M}_-$, describes null four-vectors; here it will describe the pure states.

### The Positive Cone Is the Future Light Cone

The decisive structural fact is that, in $\mathbb{M}_+$, the algebra's positive cone and the geometry's future cone are the same set. A Hermitian element $\tilde{H} = h_0 e_0 + i\mathbf{h}$ has eigenvalues $h_0 \pm |\mathbf{h}|$ (they are the eigenvalues of $h_0 I + \mathbf{h}\cdot\boldsymbol{\sigma}$), so it is positive semidefinite precisely when the smaller eigenvalue is non-negative. This gives:

**Proposition.** For $\tilde{H} \in \mathbb{M}_+$,

$$
\tilde{H} \geq 0 \quad\Longleftrightarrow\quad N(\tilde{H}) = h_0^2 - |\mathbf{h}|^2 \geq 0 \ \ \text{and}\ \ h_0 \geq 0 .
$$

The right-hand side is exactly the statement that $\tilde{H}$ lies in the closed future cone of the norm form. Thus the **positive cone of $\mathbb{M}_+$ coincides with the future light cone**, region for region, boundary included. In particular the positive cone is the future cone of a form of signature $(1,3)$, and the rank-one projections — the extreme rays of the positive cone — are precisely its null generators, $N(\tilde{H}) = 0$.

This is why the qubit state space is a canonical object of the algebra rather than a postulated set: one starts with a quadratic form that the algebra supplies, and one reads off a cone; positivity and causality are then two names for the same condition. Note also that the positive cone is exactly the set of squares of Hermitian elements: every $\tilde{H} \geq 0$ has a Hermitian square root $\sqrt{\tilde{H}} \in \mathbb{M}_+$, and conversely $A^2 = AA^\dagger \geq 0$ for Hermitian $A$.

## The Trace-One Hyperplane

The **trace-one hyperplane** is the affine hyperplane

$$
\mathcal{S} = \bigl\{\tilde{H} \in \mathbb{M}_+ : \mathrm{Sc}(\tilde{H}) = \tfrac{1}{2}\bigr\} = \bigl\{\tilde{H} \in \mathbb{M}_+ : \mathrm{Tr}(\tilde{H}) = 1\bigr\},
$$

the two descriptions being equivalent by $\mathrm{Tr} = 2\,\mathrm{Sc}$. In coordinates it is the level set $h_0 = \tfrac{1}{2}$. It is an affine hyperplane of real dimension three, with direction space the traceless subspace

$$
\{\tilde{H} \in \mathbb{M}_+ : h_0 = 0\} = \operatorname{span}_\mathbb{R}\{i e_1, i e_2, i e_3\}.
$$

The hyperplane does not contain the origin, and its normal direction is $e_0$. Since $N(e_0) = 1 > 0$, the normal is timelike and the hyperplane is **spacelike**; the quadratic form induced on it by (minus) the norm form is positive-definite. The slice is therefore a Euclidean three-space, and the ball that it will be found to contain is a genuine round ball in that Euclidean structure.

Every element of $\mathcal{S}$ is written uniquely as

$$
\tilde{\rho} = \tfrac{1}{2}\bigl(e_0 + i\,\mathbf{r}\bigr), \qquad \mathbf{r} = (r_1, r_2, r_3) \in \mathbb{R}^3 ,
$$

where $\mathbf{r} = 2\mathbf{h}$. The map $\mathbf{r} \mapsto \tilde{\rho}$ is an affine isomorphism $\mathbb{R}^3 \to \mathcal{S}$, and $\mathbf{r}$ is the **Bloch vector**. In this parametrization the trace pairing on the slice reads

$$
\mathrm{Tr}(\tilde{\rho}\tilde{\sigma}) = \tfrac{1}{2}\bigl(1 + \mathbf{r}\cdot\mathbf{s}\bigr) \qquad \text{for } \tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r}),\ \tilde{\sigma} = \tfrac{1}{2}(e_0 + i\mathbf{s}),
$$

so the Hilbert–Schmidt geometry of the slice is the Euclidean geometry of $\mathbb{R}^3$, up to the additive constant and the factor inherited from the trace.

## The Bloch Ball as the Trace-One Slice of the Future Cone

### The Slice Lemma

The intersection of an affine hyperplane $h_0 = c$ with the closed future cone is easy to describe. If $c > 0$, the future condition $h_0 \geq 0$ is automatic, the causal condition reduces to $|\mathbf{h}| \leq c$, and the apex is excluded; the intersection is a closed three-dimensional ball of radius $c$ in $\mathbf{h}$-coordinates, centered at $\mathbf{h} = 0$. If $c = 0$ the intersection degenerates to the single point at the apex, and if $c < 0$ the intersection with the future cone is empty.

For the trace-one hyperplane $c = \tfrac{1}{2}$, the ball has radius $\tfrac{1}{2}$ in $\mathbf{h}$-coordinates, equivalently radius $1$ in the Bloch coordinate $\mathbf{r} = 2\mathbf{h}$. Explicitly, the norm form on the slice is

$$
N(\tilde{\rho}) = \bigl(h_0^2 - |\mathbf{h}|^2\bigr)e_0 = \tfrac{1}{4}\bigl(1 - |\mathbf{r}|^2\bigr)e_0 ,
$$

so the causal condition $N(\tilde{\rho}) \geq 0$ is exactly

$$
|\mathbf{r}|^2 = r_1^2 + r_2^2 + r_3^2 \leq 1 .
$$

The intersection is the closed unit ball $B^3 = \{\mathbf{r} \in \mathbb{R}^3 : |\mathbf{r}| \leq 1\}$: the **Bloch ball**.

### Positivity Is Causality on the Slice

The eigenvalues of $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$ are

$$
\lambda_\pm = \tfrac{1}{2}\bigl(1 \pm |\mathbf{r}|\bigr),
$$

and they are non-negative if and only if $|\mathbf{r}| \leq 1$. Their product is the norm form,

$$
\lambda_+ \lambda_- = \tfrac{1}{4}\bigl(1 - |\mathbf{r}|^2\bigr) = N(\tilde{\rho}),
$$

so the norm form is exactly the product of the two eigenvalues. Because $h_0 = \tfrac{1}{2} > 0$ forces $\lambda_+ = h_0 + |\mathbf{h}| > 0$, the sign of $N$ determines the sign of the remaining eigenvalue: $N(\tilde{\rho}) \geq 0$ if and only if $\tilde{\rho} \geq 0$. Thus, restricted to the trace-one hyperplane, the Proposition of the previous section specializes to a clean statement.

**The state space.** The states of a qubit — the positive, trace-one elements of $\mathbb{M}_+$ — are exactly the elements of the trace-one hyperplane that lie in the closed future light cone:

$$
\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r}), \qquad |\mathbf{r}| \leq 1 .
$$

The intersection with the null cone $N(\tilde{\rho}) = 0$, i.e. the sphere $|\mathbf{r}| = 1$, is the boundary of the ball; the intersection with the interior of the cone, $N(\tilde{\rho}) > 0$, i.e. $|\mathbf{r}| < 1$, is the interior of the ball.

The elements of the trace-one hyperplane with $|\mathbf{r}| > 1$ have $N(\tilde{\rho}) < 0$; they are Hermitian and of trace one but not positive semidefinite (each has one negative eigenvalue), so they are not states. They lie outside the cone, in the spacelike region. The picture is summarized in the following table.

| Condition on $\tilde{\rho}\in\mathcal{S}$ | Algebraic form | Geometric form |
|---|---|---|
| Hermitian | $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$ | trace-one hyperplane of $\mathbb{M}_+$ |
| positive semidefinite | $\lambda_\pm = \tfrac{1}{2}(1 \pm |\mathbf{r}|) \geq 0$ | closed future cone, $N(\tilde{\rho}) \geq 0$ |
| pure | idempotent, rank one | boundary of the cone, $N(\tilde{\rho}) = 0$ |
| mixed | not idempotent, rank two | interior of the cone, $N(\tilde{\rho}) > 0$ |

## Pure States: The Boundary of the Ball

The boundary $|\mathbf{r}| = 1$ consists of the states that lie on the null cone. In the algebra these have three equivalent descriptions, and the equivalence is the content of this section.

**Idempotents and rank-one projections.** For $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$,

$$
\tilde{\rho}^2 = \tfrac{1}{4}\bigl(e_0 + i\mathbf{r}\bigr)^2 = \tfrac{1}{4}\bigl(1 + |\mathbf{r}|^2\bigr)e_0 + \tfrac{1}{2} i\mathbf{r},
$$

using $(i\mathbf{r})^2 = |\mathbf{r}|^2 e_0$. Hence

$$
\tilde{\rho}^2 - \tilde{\rho} = \tfrac{1}{4}\bigl(|\mathbf{r}|^2 - 1\bigr)e_0 ,
$$

and $\tilde{\rho}$ is idempotent if and only if $|\mathbf{r}| = 1$. The idempotents of trace one have the form

$$
\tilde{P}_\pm(\hat{\boldsymbol{\mu}}) = \tfrac{1}{2}\bigl(e_0 \pm i\hat{\boldsymbol{\mu}}\bigr), \qquad |\hat{\boldsymbol{\mu}}| = 1 ,
$$

and are the rank-one projections of $\mathbb{M}_+$; under the isomorphism they are the standard spin-up and spin-down projectors along $\hat{\boldsymbol{\mu}}$. The boundary is thus parametrized by the unit sphere $S^2 \subset \mathbb{R}^3$, with $\hat{\boldsymbol{\mu}}$ and $-\hat{\boldsymbol{\mu}}$ giving the complementary idempotents:

$$
\tilde{P}_+(\hat{\boldsymbol{\mu}}) + \tilde{P}_-(\hat{\boldsymbol{\mu}}) = e_0, \qquad \tilde{P}_+(\hat{\boldsymbol{\mu}})\tilde{P}_-(\hat{\boldsymbol{\mu}}) = 0 .
$$

**Zero divisors.** On the boundary $N(\tilde{\rho}) = 0$ with $\tilde{\rho} \neq 0$, so $\tilde{\rho}$ is a zero divisor of $\mathbb{B}$. Conversely, a positive trace-one element of $\mathbb{M}_+$ that is a zero divisor has vanishing norm form, hence $|\mathbf{r}| = 1$, hence is pure. Within the trace-one hyperplane of $\mathbb{M}_+$, therefore,

$$
\text{pure state} \quad\Longleftrightarrow\quad \text{idempotent} \quad\Longleftrightarrow\quad \text{zero divisor} \quad\Longleftrightarrow\quad N(\tilde{\rho}) = 0 .
$$

This is the sense in which "the pure states are the zero divisors at trace one": the ideal boundary of the state space is exactly the set of elements at which the algebra ceases to be invertible. An interior state has $N(\tilde{\rho}) > 0$ and is invertible; a pure state has $N(\tilde{\rho}) = 0$ and is not. Purity is the loss of invertibility at the boundary of the cone.

**Extreme rays.** The positive cone is generated by its extreme rays, and these are the rank-one projections. Equivalently, the pure states are the extreme points of the Bloch ball: every state in the interior of the ball is a nontrivial convex combination of boundary points, while no boundary point is a convex combination of two other states.

The transition probability between two pure states is the trace pairing,

$$
\mathrm{Tr}\bigl(\tilde{P}(\hat{\boldsymbol{\mu}})\tilde{P}(\hat{\boldsymbol{\nu}})\bigr) = \tfrac{1}{2}\bigl(1 + \hat{\boldsymbol{\mu}}\cdot\hat{\boldsymbol{\nu}}\bigr) = \cos^2\frac{\theta}{2},
$$

where $\theta$ is the angle between the two Bloch directions. It equals $1$ for $\hat{\boldsymbol{\mu}} = \hat{\boldsymbol{\nu}}$ and $0$ for $\hat{\boldsymbol{\mu}} = -\hat{\boldsymbol{\nu}}$, the two antipodal points corresponding to the complementary orthogonal idempotents. Since the trace pairing is the Euclidean pairing, this is the usual cosine-squared law on the Bloch sphere.

## Mixed States: The Interior of the Ball

The interior $|\mathbf{r}| < 1$ consists of the states that lie strictly inside the future cone. For these, $N(\tilde{\rho}) > 0$ and $\tilde{\rho}$ is invertible, with eigenvalues

$$
\lambda_+ = \tfrac{1}{2}\bigl(1 + |\mathbf{r}|\bigr), \qquad \lambda_- = \tfrac{1}{2}\bigl(1 - |\mathbf{r}|\bigr),
$$

both strictly positive and summing to one. The spectral decomposition is

$$
\tilde{\rho} = \lambda_+ \tilde{P}_+(\hat{\mathbf{r}}) + \lambda_- \tilde{P}_-(\hat{\mathbf{r}}), \qquad \hat{\mathbf{r}} = \frac{\mathbf{r}}{|\mathbf{r}|},
$$

a convex combination of the two complementary pure states along the Bloch direction $\hat{\mathbf{r}}$. This is the algebraic statement that every mixed state is a statistical mixture of two orthogonal pure states, with weights determined by the radius.

The center of the ball is the **maximally mixed state**

$$
\mathbf{r} = 0, \qquad \tilde{\rho} = \tfrac{1}{2} e_0 ,
$$

with equal eigenvalues $\tfrac{1}{2}, \tfrac{1}{2}$; it is the barycenter of the ball and the only state invariant under all rotations of the boundary sphere. It is the state of minimal purity and maximal entropy.

The affine structure of the slice matches the convex structure of the state space. If $\tilde{\rho}_i = \tfrac{1}{2}(e_0 + i\mathbf{r}_i)$ are states and $p_i \geq 0$ with $\sum_i p_i = 1$, then

$$
\sum_i p_i \tilde{\rho}_i = \tfrac{1}{2}\Bigl(e_0 + i \sum_i p_i \mathbf{r}_i\Bigr)
$$

is again a state, with Bloch vector $\sum_i p_i \mathbf{r}_i$. Convex combinations of states are convex combinations of Bloch vectors, so the Bloch ball is a faithful affine model of the state space. The deviation of a state from purity is captured by

$$
\tilde{\rho}^2 - \tilde{\rho} = \tfrac{1}{4}\bigl(|\mathbf{r}|^2 - 1\bigr)e_0 ,
$$

which vanishes identically on the boundary and is strictly negative at every interior point.

## The Bloch Vector, Purity, and Mixedness

The **purity** of a state is

$$
\mathrm{Tr}(\tilde{\rho}^2) = \tfrac{1}{2}\bigl(1 + |\mathbf{r}|^2\bigr),
$$

which ranges from $\tfrac{1}{2}$ at the center of the ball ($|\mathbf{r}| = 0$) to $1$ on the boundary ($|\mathbf{r}| = 1$). Inverting,

$$
|\mathbf{r}| = \sqrt{2\,\mathrm{Tr}(\tilde{\rho}^2) - 1},
$$

so the Bloch radius is a monotone function of the purity: the radius **is** the purity, measured in the Euclidean geometry of the slice. Purity is the statement $|\mathbf{r}| = 1$, and it is equivalent to idempotency and to membership of the boundary.

A convenient measure of mixedness is the **linear entropy**

$$
S_{\mathrm{lin}}(\tilde{\rho}) = 1 - \mathrm{Tr}(\tilde{\rho}^2) = \tfrac{1}{2}\bigl(1 - |\mathbf{r}|^2\bigr) = 2\,N(\tilde{\rho}) ,
$$

which vanishes on the boundary and is maximal, equal to $\tfrac{1}{2}$, at the center. The last equality is worth emphasis: **the norm form is, up to the factor $2$, the linear entropy on the trace-one hyperplane.** The quadratic form whose cone cuts out the state space is the same form that measures how mixed a state is. The reason mixedness has a norm-form expression is that both are governed by the same quantity $\lambda_+ \lambda_- = N(\tilde{\rho})$.

Finally, the Euclidean geometry of the slice gives the trace pairing a direct metrical meaning on states. The squared Hilbert–Schmidt distance between $\tilde{\rho}$ and $\tilde{\sigma}$ is

$$
\mathrm{Tr}\bigl((\tilde{\rho} - \tilde{\sigma})^2\bigr) = \tfrac{1}{2}|\mathbf{r} - \mathbf{s}|^2 ,
$$

and the trace distance from a state to the maximally mixed state is

$$
D\bigl(\tilde{\rho}, \tfrac{1}{2}e_0\bigr) = \tfrac{1}{2}\bigl|\mathbf{r}\bigr| .
$$

The Bloch radius is thus twice the trace distance to the center of the ball — another expression of the same fact, that the radius is the state's purity.

## Entropy

The **von Neumann entropy** of a state is defined spectrally,

$$
S(\tilde{\rho}) = -\mathrm{Tr}\bigl(\tilde{\rho}\log\tilde{\rho}\bigr) = -\lambda_+ \log \lambda_+ - \lambda_- \log \lambda_-,
$$

with $\lambda_\pm = \tfrac{1}{2}(1 \pm |\mathbf{r}|)$ the eigenvalues. Written in terms of the Bloch radius $r = |\mathbf{r}|$,

$$
S(\tilde{\rho}) = -\frac{1+r}{2}\log\frac{1+r}{2} - \frac{1-r}{2}\log\frac{1-r}{2},
$$

which depends on the state only through $r$, not through the direction $\hat{\mathbf{r}}$. This is the geometric statement that entropy is a function of the radius: the level sets of entropy on the Bloch ball are the concentric spheres, and two states are equally mixed precisely when they have the same radius.

On the boundary, $r = 1$, the eigenvalues are $1$ and $0$, and the entropy vanishes: pure states carry no entropy. At the center, $r = 0$, both eigenvalues are $\tfrac{1}{2}$ and the entropy is $\log 2$, its maximum on the ball. Between them, $S$ decreases strictly with $r$: differentiating the expression above,

$$
\frac{dS}{dr} = -\frac{1}{2}\log\frac{1+r}{1-r} < 0 \qquad (0 < r < 1),
$$

so entropy decreases monotonically from the center to the boundary, in step with the increase of purity. Entropy and purity therefore carry the same information on a qubit — both are functions of $|\mathbf{r}|$, and each determines the other — the entropy being the steeper, logarithmically scaled version.

Because the logarithm is the spectral logarithm on the positive cone, the trace form of the entropy is unambiguous for interior states: writing $\log\tilde{\rho} = \log\lambda_+\, \tilde{P}_+(\hat{\mathbf{r}}) + \log\lambda_-\, \tilde{P}_-(\hat{\mathbf{r}})$, one has $-2\,\mathrm{Sc}(\tilde{\rho}\log\tilde{\rho}) = S(\tilde{\rho})$, consistent with $\mathrm{Tr} = 2\,\mathrm{Sc}$.

## Fidelity and Transition Probability

For two pure states, the **transition probability** is the trace pairing computed above,

$$
\mathrm{Tr}\bigl(\tilde{P}(\hat{\boldsymbol{\mu}})\tilde{P}(\hat{\boldsymbol{\nu}})\bigr) = \tfrac{1}{2}\bigl(1 + \hat{\boldsymbol{\mu}}\cdot\hat{\boldsymbol{\nu}}\bigr) = \cos^2\frac{\theta}{2},
$$

a function of the angle between the Bloch directions alone. In terms of the boundary of the ball, it is a function of the chordal separation of two points of the sphere.

For two general states the Uhlmann transition probability is

$$
T(\tilde{\rho},\tilde{\sigma}) = \Bigl(\mathrm{Tr}\sqrt{\sqrt{\tilde{\rho}}\;\tilde{\sigma}\sqrt{\tilde{\rho}}}\,\Bigr)^{2}.
$$

All square roots here are the positive square roots within $\mathbb{M}_+$: since $\tilde{\rho}$ is a convex combination of complementary idempotents, $\sqrt{\tilde{\rho}} = \sqrt{\lambda_+}\,\tilde{P}_+(\hat{\mathbf{r}}) + \sqrt{\lambda_-}\,\tilde{P}_-(\hat{\mathbf{r}})$ lies in $\mathbb{M}_+$, and the same holds for the inner square root. In Bloch coordinates the expression evaluates to the closed form

$$
T(\tilde{\rho},\tilde{\sigma}) = \tfrac{1}{2}\Bigl(1 + \mathbf{r}\cdot\mathbf{s} + \sqrt{\bigl(1 - |\mathbf{r}|^2\bigr)\bigl(1 - |\mathbf{s}|^2\bigr)}\Bigr).
$$

Three checks are immediate. When both states are pure, $|\mathbf{r}| = |\mathbf{s}| = 1$, the radical vanishes and $T = \tfrac{1}{2}(1 + \mathbf{r}\cdot\mathbf{s})$, recovering the pure-state transition probability. When the states coincide, $\mathbf{s} = \mathbf{r}$, the expression is $\tfrac{1}{2}(1 + |\mathbf{r}|^2 + 1 - |\mathbf{r}|^2) = 1$. When $\tilde{\rho}$ is maximally mixed, $\mathbf{r} = 0$, it reduces to $T = \tfrac{1}{2}\bigl(1 + \sqrt{1 - |\mathbf{s}|^2}\bigr)$, which equals $\tfrac{1}{2}$ for a pure $\tilde{\sigma}$ and $1$ for $\tilde{\sigma}$ maximally mixed. The transition probability therefore measures, through $\mathbf{r}\cdot\mathbf{s}$, the alignment of the two Bloch vectors, and, through the radical, how far the two states are from the boundary. For mixed states it depends on the angle between the Bloch vectors as well as on the two radii; only the pure-pure case is a function of the angle alone.

## Symmetries of the Slice

The structure just described is preserved by the unitary action. If $\tilde{U}$ is a unitary biquaternion, $\tilde{U}\tilde{U}^\dagger = e_0$, then the conjugation

$$
\tilde{\rho} \;\longmapsto\; \tilde{U}\tilde{\rho}\tilde{U}^\dagger
$$

fixes the scalar part, hence preserves the trace-one hyperplane, and preserves the Hermitian property; because conjugation by a unitary is an algebra automorphism, it preserves the norm form $N(\tilde{U}\tilde{\rho}\tilde{U}^\dagger) = N(\tilde{\rho})$, hence preserves the future cone and its boundary. It therefore maps the Bloch ball to itself.

On the Bloch vector the action is a rotation. The unit quaternions — the elements of $\mathbb{H}_{\mathbb{B}}$ of unit quaternion norm, forming $SU(2)$ — act by rotating the imaginary vector part and fixing the scalar part, so they act on the ball by the rotation group $SO(3)$. The general unitary group $U(2)$ acts through the same rotations, with a central phase that fixes every state. The maximally mixed state is the unique fixed point; the boundary sphere is homogeneous, and the purity radius is a complete invariant of the orbit. The slice is thus not merely a ball but a ball with its rotation group, and the geometry that makes the trace-one slice of the cone into a state space is exactly the geometry that the algebra's unitary group preserves.

## What the Slice Picture Shows

The main structural points are these. The state space of a qubit is not postulated as a ball of vectors; it is the trace-one slice of a cone. The cone is the positive cone of the Hermitian subspace, and the positive cone is, in turn, exactly the future light cone of the algebra's norm form. The three conditions that define a state — Hermitian, positive, trace one — become membership in $\mathbb{M}_+$, a trace normalization, and a single quadratic inequality supplied by the norm form; positivity is not an extra axiom but the statement that the state lies in the cone. Purity is a boundary condition rather than a separate axiom: the pure states are the idempotents, the rank-one projections, and the zero divisors of trace one, all at once, and they are the extreme rays of the cone. Mixedness is the interior, and the norm form restricted to the slice is, up to a factor, the linear entropy. Entropy and fidelity are then functions of the radius and of the Bloch vectors in the Euclidean geometry of the slice.

Several points are left open in this picture. The base of the logarithm in the entropy is a convention, natural logarithms giving nats and base-two logarithms giving bits; the geometry does not prefer one. The normalization of the transition probability is likewise a convention, since some authors take the unsquared expression as the fidelity and others its square; the closed form above is stated for the squared normalization, which is the one that reduces to the pure-state transition probability. The extension of the slice picture to $n$ qubits requires the tensor product and the corresponding higher-dimensional cones, and the identification of the correct positivity domain there is a separate problem. Finally, this article has used only the future cone; the past cone, and the negative-trace elements of $\mathbb{M}_+$, have no state interpretation here, and whether they acquire one in a wider reading of the algebra is an open question.

## Summary

The Hermitian subspace $\mathbb{M}_+$ of the biquaternion algebra carries a norm form of signature $(1,3)$, whose positive cone coincides exactly with its future light cone. The qubit state space is the intersection of that cone with the affine hyperplane $\{\mathrm{Sc} = \tfrac{1}{2}\}$. Writing a state as

$$
\tilde{\rho} = \tfrac{1}{2}\bigl(e_0 + i\mathbf{r}\bigr),
$$

the intersection is the closed unit ball $|\mathbf{r}| \leq 1$, the **Bloch ball**, whose boundary is the intersection with the null cone.

The pure states are the boundary of the ball. Equivalently, they are the idempotents $\tilde{P}_\pm(\hat{\boldsymbol{\mu}}) = \tfrac{1}{2}(e_0 \pm i\hat{\boldsymbol{\mu}})$, the rank-one projections, the extreme rays of the positive cone, and the zero divisors of $\mathbb{B}$ at trace one; the boundary is parametrized by the Bloch sphere $S^2$. The mixed states are the interior, with eigenvalues $\tfrac{1}{2}(1 \pm |\mathbf{r}|)$; the maximally mixed state is the center $\mathbf{r} = 0$.

Purity is $\mathrm{Tr}(\tilde{\rho}^2) = \tfrac{1}{2}(1 + |\mathbf{r}|^2)$, so the Bloch radius is a measure of purity, and the linear entropy is $1 - \mathrm{Tr}(\tilde{\rho}^2) = 2N(\tilde{\rho})$, twice the norm form. The von Neumann entropy depends only on $|\mathbf{r}|$, vanishing on the boundary and maximal, equal to $\log 2$, at the center. The Uhlmann transition probability has the closed form $\tfrac{1}{2}\bigl(1 + \mathbf{r}\cdot\mathbf{s} + \sqrt{(1-|\mathbf{r}|^2)(1-|\mathbf{s}|^2)}\bigr)$, reducing on the boundary to $\cos^2(\theta/2)$. In every case the state space, its purity stratification, its entropy, and its fidelity are read off from the norm form and the trace on $\mathbb{M}_+$, without additional postulates.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{C}_{\mathbb{B}}$ | Complex subspace (center), fixed points of quaternion conjugation |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, fixed points of complex conjugation |
| $\mathbb{M}_+$ | Hermitian subspace, fixed points of $\dagger$ |
| $\mathbb{M}_-$, with $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ | Anti-Hermitian subspace, fixed points of $\flat$ |
| $\tilde{H} = h_0 e_0 + i\mathbf{h}$ | General Hermitian element |
| $\mathrm{Tr}(\tilde{H}) = 2 h_0$ | Trace |
| $N(\tilde{H}) = \tilde{H}\bar{\tilde{H}} = (h_0^2 - |\mathbf{h}|^2)e_0$ | Norm form, signature $(1,3)$ |
| $\mathrm{Tr}(\tilde{H}\tilde{K}) = 2(h_0 k_0 + \mathbf{h}\cdot\mathbf{k})$ | Trace pairing, signature $(4,0)$ |
| $\mathcal{S} = \{\mathrm{Sc} = \tfrac{1}{2}\}$ | Trace-one hyperplane |
| $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$ | State, Bloch vector $\mathbf{r}$ |
| $\tilde{P}_\pm(\hat{\boldsymbol{\mu}}) = \tfrac{1}{2}(e_0 \pm i\hat{\boldsymbol{\mu}})$ | Idempotent (pure state), $|\hat{\boldsymbol{\mu}}| = 1$ |
| $\mathrm{Tr}(\tilde{\rho}^2) = \tfrac{1}{2}(1 + |\mathbf{r}|^2)$ | Purity |
| $S(\tilde{\rho}) = -\mathrm{Tr}(\tilde{\rho}\log\tilde{\rho})$ | Von Neumann entropy |
| $T(\tilde{\rho},\tilde{\sigma}) = (\mathrm{Tr}\sqrt{\sqrt{\tilde{\rho}}\,\tilde{\sigma}\sqrt{\tilde{\rho}}})^2$ | Uhlmann transition probability |

## Further Reading

- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Bloch sphere, the density matrix formalism, and the standard fidelity.
- Ingemar Bengtsson and Karol Życzkowski, *Geometry of Quantum States* (Cambridge, 2006), for the differential and convex geometry of the state space and the Bloch ball.
- Asher Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for the operational meaning of states, purity, and distinguishability.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the spin-1/2 formalism and the Bloch vector.
- Richard Jozsa, "Fidelity for mixed quantum states," *Journal of Modern Optics* **41** (1994) 2315–2323, for the closed-form Uhlmann fidelity of a qubit.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the algebraic structure of $\mathrm{Cl}_{1,3}$ and its idempotents.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra treatment of spinors, projectors, and the light cone.
- Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones* (Oxford, 1994), for the cone-of-squares description of the positive cone of a Euclidean Jordan algebra.
