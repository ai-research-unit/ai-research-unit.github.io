# __The Bloch Ball as the Trace-One Slice of the Future Light Cone__

## Introduction

The companion articles established that the Hermitian subspace $\mathbb{M}_+$ of the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ carries the operator algebra of a two-state quantum system. Its Hermitian elements are the observables, its positive trace-one elements are the states, and the trace formula

$$
\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H) = 2\langle\tilde{P},\tilde{H}\rangle
$$

is the Born rule. This article is about the **geometry** of that state space. Its subject is one structural fact, developed in full:

> The state space of a qubit — the Bloch ball — is the intersection of the affine hyperplane $\{\mathrm{Sc} = \tfrac{1}{2}\}$ in $\mathbb{M}_+$ with the future light cone of the biquaternion norm $\langle\tilde{H}\rangle_{\natural} = \langle\tilde{H},\tilde{H}\rangle_{\natural} = \tilde{H}\tilde{H}^{\natural}$.

In the standard formalism the Bloch ball is assembled state by state: one takes the set of positive trace-one operators on a two-dimensional Hilbert space and derives the condition $|\vec r| \leq 1$ from the positivity of a $2 \times 2$ matrix. In the biquaternion framework the same object appears as a **slice of a cone by a hyperplane**. The three conditions that look independent in the matrix formalism — Hermitian, positive, trace one — become, in the algebra, membership in $\mathbb{M}_+$, a trace normalization, and a single quadratic inequality that is the causal condition of a Lorentzian form. Purity becomes a boundary condition; mixedness becomes the interior of the ball; and the zero divisors of the algebra at trace one, which elsewhere in the series describe light-like propagation, here describe the pure states.

The article is organized as follows. First the Hermitian subspace, its trace, and its biquaternion norm are recalled, together with the light cone and the zero divisors. Then the trace-one hyperplane is described and coordinatized by the Bloch vector. Then the Bloch ball is obtained as the slice of the future cone by that hyperplane, and the positivity of a state is identified with its causality. Then the pure states are characterized as the boundary of the ball — idempotents, extreme rays, and zero divisors at trace one — and the mixed states as its interior. Then purity, the Bloch radius, entropy, and fidelity are expressed in these terms. The article closes with the symmetries of the slice, with the mirror interpretation that places the ball against the material sector and its light cone and separates the two actor groups that the one action admits, with what the picture shows, and with open questions.

The conventions are those of the companion articles: the biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_k^2 = -e_t$, and $i$ is the scalar imaginary. The four fixed-point subspaces are $\mathbb{C}_{\mathbb{B}}$ (the complex subspace, the centre of $\mathbb{B}$), $\mathbb{H}_{\mathbb{B}}$ (the real-quaternion subspace), and the two complementary four-dimensional subspaces $\mathbb{M}_+$ (Hermitian) and $\mathbb{M}_-$ (anti-Hermitian), with $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$. The trace is $\mathrm{Tr}(\tilde Q)=2\,\mathrm{Sc}(\tilde Q)$.

## The Hermitian Subspace and the Biquaternion Norm

### Coordinates and Trace

An element of the Hermitian subspace is written

$$
\tilde{H} = h_0\,e_t + i\,\vec h, \qquad h_0 \in \mathbb{R}, \qquad \vec h = h_1 \vec e_x + h_2 \vec e_y + h_3 \vec e_z,
$$

where $\vec h$ is a pure real quaternion, identified with the vector $(h_1, h_2, h_3) \in \mathbb{R}^3$. The scalar part $h_0 e_t$ lies in the centre $\mathbb{C}_{\mathbb{B}}$; here it is real, and the imaginary vector part $i\vec h$ carries the three remaining real coordinates. A natural basis of $\mathbb{M}_+$ over $\mathbb{R}$ is

$$
\{e_t,\; i \vec e_x,\; i \vec e_y,\; i \vec e_z\},
$$

so that $\mathbb{M}_+$ is a four-dimensional real vector space and the fixed-point set of the Hermitian conjugation ${}^{*}$. Its **trace** is twice the scalar part:

$$
\mathrm{Tr}(\tilde{H}) = 2 h_0 .
$$

### The Biquaternion Norm

The quaternion conjugate $\tilde{H}^{\natural} = h_0 e_t - i\vec h$ is again Hermitian, so quaternion conjugation preserves $\mathbb{M}_+$; it leaves the scalar part and negates the imaginary vector part. The **biquaternion norm** is

$$
\langle\tilde{H}\rangle_{\natural} = \langle\tilde{H},\tilde{H}\rangle_{\natural} = \tilde{H}\tilde{H}^{\natural} = \bigl(h_0^2 - |\vec h|^2\bigr) e_t ,
$$

a real-valued quadratic form on $\mathbb{M}_+$, of **signature $(1,3)$**: the scalar direction $e_t$ is positive, the three imaginary directions $i \vec e_x, i \vec e_y, i \vec e_z$ are negative. This is the mirror image of the signature $(3,1)$ that the same biquaternion norm carries on the anti-Hermitian subspace $\mathbb{M}_-$.

The biquaternion norm is not the trace pairing. The trace pairing

$$
\mathrm{Tr}(\tilde{H}\tilde{K}) = 2\bigl(h_0 k_0 + \vec h\cdot\vec k\bigr)
$$

is positive-definite, of signature $(4,0)$; it is the analogue of the Hilbert–Schmidt inner product. The biquaternion norm and the trace pairing are distinct quadratic structures on the same four-dimensional space, and keeping them apart is essential: positivity of a state is a condition on the biquaternion norm, while the Born rule is a condition on the trace pairing.

### The Light Cone and the Zero Divisors

The vanishing of the biquaternion norm defines the **light cone** of $\mathbb{M}_+$:

$$
\langle\tilde{H}\rangle_{\natural} = 0 \quad\Longleftrightarrow\quad h_0^2 = |\vec h|^2 ,
$$

a double cone in $\mathbb{R}^4$ with apex at the origin. The complement of the cone has three connected components: the spacelike region $N < 0$ (a single component), and the two components of the timelike region $N > 0$, namely $h_0 > |\vec h|$ and $h_0 < -|\vec h|$. The first of these, $h_0 > |\vec h|$, is the **future** component.

Under the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ that maps $e_t \mapsto I$ and $\vec e_j \mapsto -i\sigma_j$, a Hermitian element $\tilde{H} = h_0 e_t + i\vec h$ maps to the Hermitian matrix $h_0 I + \vec h\cdot\boldsymbol{\sigma}$, whose determinant is $h_0^2 - |\vec h|^2$. The biquaternion norm is therefore the determinant form:

$$
\langle\tilde{H}\rangle_{\natural} \;\longmapsto\; \det\bigl(h_0 I + \vec h\cdot\boldsymbol{\sigma}\bigr) I .
$$

Consequently the nonzero elements of the light cone are exactly the **zero divisors** of $\mathbb{B}$ that lie in $\mathbb{M}_+$: $\langle\tilde{H}\rangle_{\natural} = \langle\tilde{H},\tilde{H}\rangle_{\natural} = 0$ with $\tilde{H} \neq 0$ means the corresponding matrix is singular, hence a zero divisor. Conversely every zero divisor in $\mathbb{M}_+$ has vanishing biquaternion norm. This is the same zero-divisor cone that, in $\mathbb{M}_-$, describes null four-vectors; here it will describe the pure states.

### The Positive Cone Is the Future Light Cone

The decisive structural fact is that, in $\mathbb{M}_+$, the algebra's positive cone and the geometry's future cone are the same set. A Hermitian element $\tilde{H} = h_0 e_t + i\vec h$ has eigenvalues $h_0 \pm |\vec h|$ (they are the eigenvalues of $h_0 I + \vec h\cdot\boldsymbol{\sigma}$), so it is positive semidefinite precisely when the smaller eigenvalue is non-negative. This gives:

**Proposition.** For $\tilde{H} \in \mathbb{M}_+$,

$$
\tilde{H} \geq 0 \quad\Longleftrightarrow\quad \langle\tilde{H}\rangle_{\natural} = h_0^2 - |\vec h|^2 \geq 0 \ \ \text{and}\ \ h_0 \geq 0 .
$$

The right-hand side is exactly the statement that $\tilde{H}$ lies in the closed future cone of the biquaternion norm. Thus the **positive cone of $\mathbb{M}_+$ coincides with the future light cone**, region for region, boundary included. In particular the positive cone is the future cone of a form of signature $(1,3)$, and the rank-one projections — the extreme rays of the positive cone — are precisely its null generators, $\langle\tilde{H}\rangle_{\natural} = 0$.

This is why the qubit state space is a canonical object of the algebra rather than a postulated set: one starts with a quadratic form that the algebra supplies, and one reads off a cone; positivity and causality are then two names for the same condition. Note also that the positive cone is exactly the set of squares of Hermitian elements: every $\tilde{H} \geq 0$ has a Hermitian square root $\sqrt{\tilde{H}} \in \mathbb{M}_+$, and conversely $A^2 = AA^\dagger \geq 0$ for Hermitian $A$.

## The Trace-One Hyperplane

The **trace-one hyperplane** is the affine hyperplane

$$
\mathcal{S} = \bigl\{\tilde{H} \in \mathbb{M}_+ : \mathrm{Sc}(\tilde{H}) = \tfrac{1}{2}\bigr\} = \bigl\{\tilde{H} \in \mathbb{M}_+ : \mathrm{Tr}(\tilde{H}) = 1\bigr\},
$$

the two descriptions being equivalent by $\mathrm{Tr} = 2\,\mathrm{Sc}$. In coordinates it is the level set $h_0 = \tfrac{1}{2}$. It is an affine hyperplane of real dimension three, with direction space the traceless subspace

$$
\{\tilde{H} \in \mathbb{M}_+ : h_0 = 0\} = \operatorname{span}_\mathbb{R}\{i \vec e_x, i \vec e_y, i \vec e_z\}.
$$

The hyperplane does not contain the origin, and its normal direction is $e_t$. Since $\langle e_t\rangle_{\natural} = 1 > 0$, the normal is timelike and the hyperplane is **spacelike**; the quadratic form induced on it by (minus) the biquaternion norm is positive-definite. The slice is therefore a Euclidean three-space, and the ball that it will be found to contain is a genuine round ball in that Euclidean structure.

Every element of $\mathcal{S}$ is written uniquely as

$$
\tilde{Ϛ} = \tfrac{1}{2}\bigl(e_t + i\,\vec r\bigr), \qquad \vec r = (r_1, r_2, r_3) \in \mathbb{R}^3 ,
$$

where $\vec r = 2\vec h$. The map $\vec r \mapsto \tilde{Ϛ}$ is an affine isomorphism $\mathbb{R}^3 \to \mathcal{S}$, and $\vec r$ is the **Bloch vector**. In this parametrization the trace pairing on the slice reads

$$
\mathrm{Tr}(\tilde{Ϛ}\tilde{\sigma}) = \tfrac{1}{2}\bigl(1 + \vec r\cdot\vec s\bigr) \qquad \text{for } \tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r),\ \tilde{\sigma} = \tfrac{1}{2}(e_t + i\vec s),
$$

so the Hilbert–Schmidt geometry of the slice is the Euclidean geometry of $\mathbb{R}^3$, up to the additive constant and the factor inherited from the trace.

## The Bloch Ball as the Trace-One Slice of the Future Cone

### The Slice Lemma

The intersection of an affine hyperplane $h_0 = c$ with the closed future cone is easy to describe. If $c > 0$, the future condition $h_0 \geq 0$ is automatic, the causal condition reduces to $|\vec h| \leq c$, and the apex is excluded; the intersection is a closed three-dimensional ball of radius $c$ in $\vec h$-coordinates, centred at $\vec h = 0$. If $c = 0$ the intersection degenerates to the single point at the apex, and if $c < 0$ the intersection with the future cone is empty.

For the trace-one hyperplane $c = \tfrac{1}{2}$, the ball has radius $\tfrac{1}{2}$ in $\vec h$-coordinates, equivalently radius $1$ in the Bloch coordinate $\vec r = 2\vec h$. Explicitly, the biquaternion norm on the slice is

$$
\langle\tilde{H}\rangle_{\natural} = \bigl(h_0^2 - |\vec h|^2\bigr)e_t = \tfrac{1}{4}\bigl(1 - |\vec r|^2\bigr)e_t ,
$$

so the causal condition $\langle\tilde{H}\rangle_{\natural} \geq 0$ is exactly

$$
|\vec r|^2 = r_1^2 + r_2^2 + r_3^2 \leq 1 .
$$

The intersection is the closed unit ball $B^3 = \{\vec r \in \mathbb{R}^3 : |\vec r| \leq 1\}$: the **Bloch ball**.

### Positivity Is Causality on the Slice

The eigenvalues of $\tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r)$ are

$$
\lambda_\pm = \tfrac{1}{2}\bigl(1 \pm |\vec r|\bigr),
$$

and they are non-negative if and only if $|\vec r| \leq 1$. Their product is the biquaternion norm,

$$
\lambda_+ \lambda_- = \tfrac{1}{4}\bigl(1 - |\vec r|^2\bigr) = \langle\tilde{Ϛ}\rangle_{\natural},
$$

so the biquaternion norm is exactly the product of the two eigenvalues. Because $h_0 = \tfrac{1}{2} > 0$ forces $\lambda_+ = h_0 + |\vec h| > 0$, the sign of $\langle\cdot\rangle_{\natural}$ determines the sign of the remaining eigenvalue: $\langle\tilde{Ϛ}\rangle_{\natural} \geq 0$ if and only if $\tilde{Ϛ} \geq 0$. Thus, restricted to the trace-one hyperplane, the Proposition of the previous section specializes to a clean statement.

**The state space.** The states of a qubit — the positive, trace-one elements of $\mathbb{M}_+$ — are exactly the elements of the trace-one hyperplane that lie in the closed future light cone:

$$
\tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r), \qquad |\vec r| \leq 1 .
$$

The intersection with the null cone $\langle\tilde{Ϛ}\rangle_{\natural} = 0$, i.e. the sphere $|\vec r| = 1$, is the boundary of the ball; the intersection with the interior of the cone, $\langle\tilde{Ϛ}\rangle_{\natural} > 0$, i.e. $|\vec r| < 1$, is the interior of the ball.

The elements of the trace-one hyperplane with $|\vec r| > 1$ have $\langle\tilde{Ϛ}\rangle_{\natural} < 0$; they are Hermitian and of trace one but not positive semidefinite (each has one negative eigenvalue), so they are not states. They lie outside the cone, in the spacelike region. The picture is summarized in the following table.

| Condition on $\tilde{Ϛ}\in\mathcal{S}$ | Algebraic form | Geometric form |
|---|---|---|
| Hermitian | $\tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r)$ | trace-one hyperplane of $\mathbb{M}_+$ |
| positive semidefinite | $\lambda_\pm = \tfrac{1}{2}(1 \pm |\vec r|) \geq 0$ | closed future cone, $\langle\tilde{Ϛ}\rangle_{\natural} \geq 0$ |
| pure | idempotent, rank one | boundary of the cone, $\langle\tilde{Ϛ}\rangle_{\natural} = 0$ |
| mixed | not idempotent, rank two | interior of the cone, $\langle\tilde{Ϛ}\rangle_{\natural} > 0$ |

## Pure States: The Boundary of the Ball

The boundary $|\vec r| = 1$ consists of the states that lie on the null cone. In the algebra these have three equivalent descriptions, and the equivalence is the content of this section.

**Idempotents and rank-one projections.** For $\tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r)$,

$$
\tilde{Ϛ}^2 = \tfrac{1}{4}\bigl(e_t + i\vec r\bigr)^2 = \tfrac{1}{4}\bigl(1 + |\vec r|^2\bigr)e_t + \tfrac{1}{2} i\vec r,
$$

using $(i\vec r)^2 = |\vec r|^2 e_t$. Hence

$$
\tilde{Ϛ}^2 - \tilde{Ϛ} = \tfrac{1}{4}\bigl(|\vec r|^2 - 1\bigr)e_t ,
$$

and $\tilde{Ϛ}$ is idempotent if and only if $|\vec r| = 1$. The idempotents of trace one have the form

$$
\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}\bigl(e_t \pm i\vec u\bigr), \qquad |\vec u| = 1 ,
$$

and are the rank-one projections of $\mathbb{M}_+$; under the isomorphism they are the standard spin-up and spin-down projectors along $\vec u$. The boundary is thus parametrized by the unit sphere $S^2 \subset \mathbb{R}^3$, with $\vec u$ and $-\vec u$ giving the complementary idempotents:

$$
\tilde\Pi_1(\vec u) + \tilde\Pi_2(\vec u) = e_t, \qquad \tilde\Pi_1(\vec u)\tilde\Pi_2(\vec u) = 0 .
$$

**Zero divisors.** On the boundary $\langle\tilde{Ϛ}\rangle_{\natural} = 0$ with $\tilde{Ϛ} \neq 0$, so $\tilde{Ϛ}$ is a zero divisor of $\mathbb{B}$. Conversely, a positive trace-one element of $\mathbb{M}_+$ that is a zero divisor has vanishing biquaternion norm, hence $|\vec r| = 1$, hence is pure. Within the trace-one hyperplane of $\mathbb{M}_+$, therefore,

$$
\text{pure state} \quad\Longleftrightarrow\quad \text{idempotent} \quad\Longleftrightarrow\quad \text{zero divisor} \quad\Longleftrightarrow\quad \langle\tilde{Ϛ}\rangle_{\natural} = 0 .
$$

This is the sense in which "the pure states are the zero divisors at trace one": the ideal boundary of the state space is exactly the set of elements at which the algebra ceases to be invertible. An interior state has $\langle\tilde{Ϛ}\rangle_{\natural} > 0$ and is invertible; a pure state has $\langle\tilde{Ϛ}\rangle_{\natural} = 0$ and is not. Purity is the loss of invertibility at the boundary of the cone.

**Extreme rays.** The positive cone is generated by its extreme rays, and these are the rank-one projections. Equivalently, the pure states are the extreme points of the Bloch ball: every state in the interior of the ball is a nontrivial convex combination of boundary points, while no boundary point is a convex combination of two other states.

The transition probability between two pure states is the trace pairing,

$$
\mathrm{Tr}\bigl(\tilde\Pi(\vec u_x)\tilde\Pi(\vec u_y)\bigr) = \tfrac{1}{2}\bigl(1 + \vec u_x\cdot\vec u_y\bigr) = \cos^2\frac{\theta}{2},
$$

where $\theta$ is the angle between the two Bloch directions. It equals $1$ for $\vec u_x = \vec u_y$ and $0$ for $\vec u_x = -\vec u_y$, the two antipodal points corresponding to the complementary orthogonal idempotents. Since the trace pairing is the Euclidean pairing, this is the usual cosine-squared law on the Bloch sphere.

## Mixed States: The Interior of the Ball

The interior $|\vec r| < 1$ consists of the states that lie strictly inside the future cone. For these, $\langle\tilde{Ϛ}\rangle_{\natural} > 0$ and $\tilde{Ϛ}$ is invertible, with eigenvalues

$$
\lambda_+ = \tfrac{1}{2}\bigl(1 + |\vec r|\bigr), \qquad \lambda_- = \tfrac{1}{2}\bigl(1 - |\vec r|\bigr),
$$

both strictly positive and summing to one. The spectral decomposition is

$$
\tilde{Ϛ} = \lambda_+ \tilde\Pi_1(\vec u_r) + \lambda_- \tilde\Pi_2(\vec u_r), \qquad \vec u_r = \frac{\vec r}{|\vec r|},
$$

a convex combination of the two complementary pure states along the Bloch direction $\vec u_r$. This is the algebraic statement that every mixed state is a statistical mixture of two orthogonal pure states, with weights determined by the radius.

The centre of the ball is the **maximally mixed state**

$$
\vec r = 0, \qquad \tilde{Ϛ} = \tfrac{1}{2} e_t ,
$$

with equal eigenvalues $\tfrac{1}{2}, \tfrac{1}{2}$; it is the barycentre of the ball and the only state invariant under all rotations of the boundary sphere. It is the state of minimal purity and maximal entropy.

The affine structure of the slice matches the convex structure of the state space. If $\tilde{Ϛ}_i = \tfrac{1}{2}(e_t + i\vec r_i)$ are states and $p_i \geq 0$ with $\sum_i p_i = 1$, then

$$
\sum_i p_i \tilde{Ϛ}_i = \tfrac{1}{2}\Bigl(e_t + i \sum_i p_i \vec r_i\Bigr)
$$

is again a state, with Bloch vector $\sum_i p_i \vec r_i$. Convex combinations of states are convex combinations of Bloch vectors, so the Bloch ball is a faithful affine model of the state space. The deviation of a state from purity is captured by

$$
\tilde{Ϛ}^2 - \tilde{Ϛ} = \tfrac{1}{4}\bigl(|\vec r|^2 - 1\bigr)e_t ,
$$

which vanishes identically on the boundary and is strictly negative at every interior point.

## The Bloch Vector, Purity, and Mixedness

The **purity** of a state is

$$
\mathrm{Tr}(\tilde{Ϛ}^2) = \tfrac{1}{2}\bigl(1 + |\vec r|^2\bigr),
$$

which ranges from $\tfrac{1}{2}$ at the centre of the ball ($|\vec r| = 0$) to $1$ on the boundary ($|\vec r| = 1$). Inverting,

$$
|\vec r| = \sqrt{2\,\mathrm{Tr}(\tilde{Ϛ}^2) - 1},
$$

so the Bloch radius is a monotone function of the purity: the radius **is** the purity, measured in the Euclidean geometry of the slice. Purity is the statement $|\vec r| = 1$, and it is equivalent to idempotency and to membership of the boundary.

A convenient measure of mixedness is the **linear entropy**

$$
S_{\mathrm{lin}}(\tilde{Ϛ}) = 1 - \mathrm{Tr}(\tilde{Ϛ}^2) = \tfrac{1}{2}\bigl(1 - |\vec r|^2\bigr) = 2\,\langle\tilde{Ϛ}\rangle_{\natural} ,
$$

which vanishes on the boundary and is maximal, equal to $\tfrac{1}{2}$, at the centre. The last equality is worth emphasis: **the biquaternion norm is, up to the factor $2$, the linear entropy on the trace-one hyperplane.** The quadratic form whose cone cuts out the state space is the same form that measures how mixed a state is. The reason mixedness has a biquaternion-norm expression is that both are governed by the same quantity $\lambda_+ \lambda_- = \langle\tilde{Ϛ}\rangle_{\natural}$.

Finally, the Euclidean geometry of the slice gives the trace pairing a direct metrical meaning on states. The squared Hilbert–Schmidt distance between $\tilde{Ϛ}$ and $\tilde{\sigma}$ is

$$
\mathrm{Tr}\bigl((\tilde{Ϛ} - \tilde{\sigma})^2\bigr) = \tfrac{1}{2}|\vec r - \vec s|^2 ,
$$

and the trace distance from a state to the maximally mixed state is

$$
D\bigl(\tilde{Ϛ}, \tfrac{1}{2}e_t\bigr) = \tfrac{1}{2}\bigl|\vec r\bigr| .
$$

The Bloch radius is thus twice the trace distance to the centre of the ball — another expression of the same fact, that the radius is the state's purity.

## Entropy

The **von Neumann entropy** of a state is defined spectrally,

$$
S(\tilde{Ϛ}) = -\mathrm{Tr}\bigl(\tilde{Ϛ}\log\tilde{Ϛ}\bigr) = -\lambda_+ \log \lambda_+ - \lambda_- \log \lambda_-,
$$

with $\lambda_\pm = \tfrac{1}{2}(1 \pm |\vec r|)$ the eigenvalues. Written in terms of the Bloch radius $r = |\vec r|$,

$$
S(\tilde{Ϛ}) = -\frac{1+r}{2}\log\frac{1+r}{2} - \frac{1-r}{2}\log\frac{1-r}{2},
$$

which depends on the state only through $r$, not through the direction $\vec u_r$. This is the geometric statement that entropy is a function of the radius: the level sets of entropy on the Bloch ball are the concentric spheres, and two states are equally mixed precisely when they have the same radius.

On the boundary, $r = 1$, the eigenvalues are $1$ and $0$, and the entropy vanishes: pure states carry no entropy. At the centre, $r = 0$, both eigenvalues are $\tfrac{1}{2}$ and the entropy is $\log 2$, its maximum on the ball. Between them, $S$ decreases strictly with $r$: differentiating the expression above,

$$
\frac{dS}{dr} = -\frac{1}{2}\log\frac{1+r}{1-r} < 0 \qquad (0 < r < 1),
$$

so entropy decreases monotonically from the centre to the boundary, in step with the increase of purity. Entropy and purity therefore carry the same information on a qubit — both are functions of $|\vec r|$, and each determines the other — the entropy being the steeper, logarithmically scaled version.

Because the logarithm is the spectral logarithm on the positive cone, the trace form of the entropy is unambiguous for interior states: writing $\log\tilde{Ϛ} = \log\lambda_+\, \tilde\Pi_1(\vec u_r) + \log\lambda_-\, \tilde\Pi_2(\vec u_r)$, one has $-2\,\mathrm{Sc}(\tilde{Ϛ}\log\tilde{Ϛ}) = S(\tilde{Ϛ})$, consistent with $\mathrm{Tr} = 2\,\mathrm{Sc}$.

## Fidelity and Transition Probability

For two pure states, the **transition probability** is the trace pairing computed above,

$$
\mathrm{Tr}\bigl(\tilde\Pi(\vec u_x)\tilde\Pi(\vec u_y)\bigr) = \tfrac{1}{2}\bigl(1 + \vec u_x\cdot\vec u_y\bigr) = \cos^2\frac{\theta}{2},
$$

a function of the angle between the Bloch directions alone. In terms of the boundary of the ball, it is a function of the chordal separation of two points of the sphere.

For two general states the Uhlmann transition probability is

$$
T(\tilde{Ϛ},\tilde{\sigma}) = \Bigl(\mathrm{Tr}\sqrt{\sqrt{\tilde{Ϛ}}\;\tilde{\sigma}\sqrt{\tilde{Ϛ}}}\,\Bigr)^{2}.
$$

All square roots here are the positive square roots within $\mathbb{M}_+$: since $\tilde{Ϛ}$ is a convex combination of complementary idempotents, $\sqrt{\tilde{Ϛ}} = \sqrt{\lambda_+}\,\tilde\Pi_1(\vec u_r) + \sqrt{\lambda_-}\,\tilde\Pi_2(\vec u_r)$ lies in $\mathbb{M}_+$, and the same holds for the inner square root. In Bloch coordinates the expression evaluates to the closed form

$$
T(\tilde{Ϛ},\tilde{\sigma}) = \tfrac{1}{2}\Bigl(1 + \vec r\cdot\vec s + \sqrt{\bigl(1 - |\vec r|^2\bigr)\bigl(1 - |\vec s|^2\bigr)}\Bigr).
$$

Three checks are immediate. When both states are pure, $|\vec r| = |\vec s| = 1$, the radical vanishes and $T = \tfrac{1}{2}(1 + \vec r\cdot\vec s)$, recovering the pure-state transition probability. When the states coincide, $\vec s = \vec r$, the expression is $\tfrac{1}{2}(1 + |\vec r|^2 + 1 - |\vec r|^2) = 1$. When $\tilde{Ϛ}$ is maximally mixed, $\vec r = 0$, it reduces to $T = \tfrac{1}{2}\bigl(1 + \sqrt{1 - |\vec s|^2}\bigr)$, which equals $\tfrac{1}{2}$ for a pure $\tilde{\sigma}$ and $1$ for $\tilde{\sigma}$ maximally mixed. The transition probability therefore measures, through $\vec r\cdot\vec s$, the alignment of the two Bloch vectors, and, through the radical, how far the two states are from the boundary. For mixed states it depends on the angle between the Bloch vectors as well as on the two radii; only the pure-pure case is a function of the angle alone.

## Symmetries of the Slice

The structure just described is preserved by the unitary action. If $\tilde{U}$ is a unitary biquaternion, $\tilde{U}\tilde{U}^{*} = e_t$, then the conjugation

$$
\tilde{Ϛ} \;\longmapsto\; \tilde{U}\tilde{Ϛ}\tilde{U}^{*}
$$

fixes the scalar part, hence preserves the trace-one hyperplane, and preserves the Hermitian property; because conjugation by a unitary is an algebra automorphism, it preserves the biquaternion norm $\langle\tilde{U}\tilde{Ϛ}\tilde{U}^{*}\rangle_{\natural} = \langle\tilde{Ϛ}\rangle_{\natural}$, hence preserves the future cone and its boundary. It therefore maps the Bloch ball to itself.

On the Bloch vector the action is a rotation. The unit quaternions — the elements of $\mathbb{H}_{\mathbb{B}}$ of unit quaternion norm, forming $SU(2)$ — act by rotating the imaginary vector part and fixing the scalar part, so they act on the ball by the rotation group $SO(3)$. The general unitary group $\mathrm{U}(2)$ acts through the same rotations, with a central phase that fixes every state. The maximally mixed state is the unique fixed point; the boundary sphere is homogeneous, and the purity radius is a complete invariant of the orbit. The slice is thus not merely a ball but a ball with its rotation group, and the geometry that makes the trace-one slice of the cone into a state space is exactly the geometry that the algebra's unitary group preserves.

### The Boundary Sphere as the Compact Member of a Family

The sphere $S^2$ of the boundary is the compact member of a family of homogeneous spaces that the same two-dimensional module models, and naming the family places the ball in the wider picture the corpus uses. As a homogeneous space the boundary sphere is $S^2=SU(2)/\mathrm{U}(1)$, the quotient of the compact group $SU(2)$ by the $\mathrm{U}(1)$ that fixes the Bloch vector. The two companion spaces come from the rank-one non-compact group $SU(1,1)\cong SL(2,\mathbb{R})\cong Sp(2,\mathbb{R})$, the double cover of the three-dimensional Lorentz group $SO(1,2)$ and the dynamical group of the oscillator's squeezings: they are the two-sheeted time-like hyperboloid $H^\pm=SU(1,1)/\mathrm{U}(1)$ and the one-sheeted hyperboloid $H^{sl}$, whose vector stabiliser is the non-compact boost subgroup, the first being the case of $S^2$ with the compact direction replaced by a time-like one. All three are modelled on spinors of the same module in the same way the boundary sphere is:

- the sphere $S^2$, by one Weyl spinor with the definite pairing $\langle z|\sigma^i|z\rangle$ and $\langle z|z\rangle=1$ — the pure-state correspondence of the preceding sections, since the boundary of the ball is exactly the spin-$1/2$ pure states;
- the hyperboloid $H^\pm$, by one Weyl spinor with the indefinite pairing $[u|v]=u^{\dagger}\sigma_3v$;
- the hyperboloid $H^{sl}$, by a **pair** of Majorana spinors.

The three spaces are graded by causal character, and the grading shows in the representation label: $S^2$ carries a discrete spin label from the finite-dimensional $SU(2)$ multiplets, while the two hyperboloids carry a label from the discrete or the continuous series of $SU(1,1)$. The sphere of this article is therefore the space-like, compact case of a classification into causal types, and the non-compact cases are the ones on which a continuous rather than a discrete label appears. The construction is external to the framework and is cited in *Quantum Gravity under the Biquaternion Framework — A Research Agenda*.

## The Mirror Reading: The Ball and the Material Cone

The ball has so far been described entirely inside $\mathbb{M}_+$, by its own cone and its own trace. It has a second interpretation, obtained with the algebra's central imaginary unit, that places it against the material sector $\mathbb{M}_-$ and its light cone. The interpretation is one map together with a dictionary, and it also settles what the two sectors are **not**: they are anti-isometric real quadratic spaces, not isomorphic algebras, and neither of them is closed under multiplication.

### The Dictionary Between the Ball and the Cone

Multiplication by $-\tfrac{i}{2}$ is a real-linear bijection carrying $\mathbb{M}_-$ onto $\mathbb{M}_+$. For a material four-vector $\tilde{Q} = ict\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ it gives the Hermitian element

$$
\tilde{H} \;=\; -\tfrac{i}{2}\,\tilde{Q} \;=\; \tfrac{1}{2}\bigl(ct\,e_t - i(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\bigr) \;=\; h_0\,e_t + i\vec h,
$$

with $h_0 = \tfrac{1}{2}ct$ and $\vec h = -\tfrac{1}{2}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$, and

$$
\mathrm{Tr}(\tilde{H}) \;=\; 2\,\mathrm{Sc}(\tilde{H}) \;=\; ct,
\qquad
\langle\tilde{H}\rangle_{\natural} \;=\; -\tfrac{1}{4}\langle\tilde{Q}\rangle_{\natural}.
$$

Each of the two relations is exact. The second is the whole dictionary in one line: the norm of the image is minus a quarter of the interval of the four-vector it mirrors. The image is a state exactly on the trace-one slice $ct = 1$, where it is $\tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r)$ with Bloch vector $\vec r = 2\vec h = -(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$; there the relations specialize to

$$
\tilde{Ϛ} \geq 0
\;\Longleftrightarrow\;
\langle\tilde{Ϛ}\rangle_{\natural} \geq 0
\;\Longleftrightarrow\;
\langle\tilde{Q}\rangle_{\natural} \leq 0
\;\Longleftrightarrow\;
ct \geq |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z| ,
$$

so **positivity of a state is the causal condition of the four-vector it mirrors**. The boundary $|\vec r| = 1$ is $\langle\tilde{Q}\rangle_{\natural} = 0$, so the pure states of the ball are the lightlike four-vectors of the slice and the mixed states are the timelike ones. The correspondence is summarized in the following table.

| Material object in $\mathbb{M}_-$ | Informational object in $\mathbb{M}_+$ |
|---|---|
| four-vector $\tilde{Q} = ict\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | Hermitian element $\tilde{H} = -\tfrac{i}{2}\tilde{Q}$ |
| interval $\langle\tilde{Q}\rangle_{\natural} = -c^2t^2 +x^2+y^2+z^2$ | norm $\langle\tilde{H}\rangle_{\natural} = -\tfrac{1}{4}\langle\tilde{Q}\rangle_{\natural}$ |
| future cone, $ct \geq |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|$ | positive cone, $\tilde{H} \geq 0$ |
| null cone, $\langle\tilde{Q}\rangle_{\natural} = 0$ | null cone, $\langle\tilde{H}\rangle_{\natural} = 0$; the pure states at trace one |
| interior of the timelike cone | positive definite elements; the interior of the ball at trace one |
| trace-one slice, $ct = 1$ | trace-one hyperplane, $\mathrm{Sc} = \tfrac{1}{2}$ |
| spatial part $x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | Bloch vector $\vec r = -(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$ |
| unit-norm rotor, $\langle\tilde{\Lambda}\rangle_{\natural} = 1$ | unitary element, $\tilde{U}\tilde{U}^{*} = e_t$ |

<!-- PHYSICAL READING — one cone, not two cones in correspondence. On the trace-one slice the positive cone of the informational sector is exactly the image of the causal future of the material sector under $-\tfrac{i}{2}$: the map sends $ct$ to $h_0 = ct/2$ and $x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ to $\vec h = -(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)/2$, so $h_0 - |\vec h| = (ct - |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|)/2$. The statement is that a qubit state IS a timelike four-vector normalized to $ct = 1$ and read from inside: positivity of the operator is the timelike condition of the four-vector, and purity is nullness. Do not write that the two cones are "analogous" or "in correspondence"; they are one cone. -->

<!-- INFORMATIONAL READING — mixedness is the timelike deficit. The centre of the ball, $\vec r = 0$, mirrors $\tilde{Q} = ict\,e_t$ at $ct = 1$, which is the four-velocity of a particle at rest in units $c = 1$; the boundary of the ball mirrors the light cone. Since the linear entropy satisfies $S_{\mathrm{lin}} = 2\langle\tilde{Ϛ}\rangle_{\natural}$ and $\langle\tilde{Q}\rangle_{\natural}$ is the interval, the linear entropy of a state is $-\tfrac{1}{2}\langle\tilde{Q}\rangle_{\natural}$ of its mirror: purity is nullness and mixedness is the timelike deficit. Reading mixedness as "how timelike the mirror is" is an interpretation of the dictionary and not a new result; the identity it rests on, $\langle\tilde{Ϛ}\rangle_{\natural} = -\tfrac{1}{4}\langle\tilde{Q}\rangle_{\natural}$, is exact. -->

### The Whole Timelike Cone, Not Only the Slice

The trace-one restriction is not essential to the correspondence, and saying so locates the normalization correctly. Off trace one, $-\tfrac{i}{2}$ carries the whole future timelike cone of $\mathbb{M}_-$ onto the positive definite elements of $\mathbb{M}_+$, of every trace (its apex, the origin, going to $0$), and the past timelike cone onto the negative definite elements. Writing the image as $\tilde{H} = h_0 e_t + i\vec h$, with $h_0 = ct/2$ and $\vec h = -(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)/2$, its eigenvalues are

$$
\lambda_\pm \;=\; h_0 \pm |\vec h| \;=\; \tfrac{1}{2}\bigl(ct \pm |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|\bigr),
$$

both non-negative for $ct > 0$ and both non-positive for $ct < 0$. The sign of the trace is the sign of $ct$, so it is the **trace sign and not the sign of the norm** that separates the two sheets: $\langle\tilde{H}\rangle_{\natural} = -\tfrac{1}{4}\langle\tilde{Q}\rangle_{\natural}$ is positive on both timelike cones, and the quadratic form alone cannot tell them apart.


The maximally mixed state is the image the map singles out. It is $\tilde{Ϛ} = \tfrac{1}{2}e_t$, the centre of the ball, and its mirror on the trace-one slice is $\tilde{Q} = i\,e_t$: timelike, of the largest interval on that slice, and equal to the four-velocity of a particle at rest divided by $c$. At the other end the idempotents, the boundary of the ball, mirror the null four-vectors. So the ordering of the ball by purity is the ordering of the timelike cone by the interval, read in reverse: the least pure state mirrors the most timelike four-vector, and the pure states mirror the light cone.

**Interpretation (decoherence as inward motion).** The dictionary has a process interpretation. The pure states are the boundary of the ball and the light cone of the material sector; the maximally mixed state is the centre and the rest four-vector. A decoherence process moves a state from the boundary toward the centre, and under the mirror map that is motion from the null boundary into the **causal interior**, from a lightlike four-vector toward the timelike rest vector. Because the linear entropy is $S_{\mathrm{lin}} = 2\langle\tilde{Ϛ}\rangle_{\natural} = -\tfrac{1}{2}\langle\tilde{Q}\rangle_{\natural}$, an increase in entropy is exactly the growth of the timelike interval of the mirror, so **entropy increase tracks the inward motion** on the causal side. The interpretation is an interpretation of the dictionary and not a new theorem: the dictionary is static and exact, the motion is the added interpretation, and the algebra supplies no rate and no mechanism for it.

### One Formula, Two Actors

The two interpretations use one action. On $\mathbb{M}_-$,

$$
\Gamma_{\tilde{\Lambda}}(\tilde{Q}) \;=\; \tilde{\Lambda}\,\tilde{Q}\,\tilde{\Lambda}^{*},
\qquad
\tilde{\Lambda}\tilde{\Lambda}^{\natural} = e_t ,
$$

preserves the interval and hence the cone. On $\mathbb{M}_+$ the same formula acts with the unitary of *Symmetries of the Slice*,

$$
\Gamma_{\tilde{U}}(\tilde{Ϛ}) \;=\; \tilde{U}\,\tilde{Ϛ}\,\tilde{U}^{*},
\qquad
\tilde{U}\tilde{U}^{*} = e_t ,
$$

and preserves the Hermitian property, the trace, and the norm, hence the ball. Writing $\tilde{A}$ for whichever actor is in play, the two cases are the one formula $\Gamma_{\tilde{A}}(\tilde{Q}) = \tilde{A}\tilde{Q}\tilde{A}^{*}$, and what differs between the relativistic and the quantum reading is only the class of actor and the invariant that defines it, $\langle\tilde{\Lambda}\rangle_{\natural} = 1$ against $\tilde{U}\tilde{U}^{*} = e_t$.

<!-- PHYSICAL READING — one formula, two actors. Relativity and quantum theory are not two structures laid in correspondence here; they are two classes of acting element of one algebra acting by one rule. A Lorentz transformation and a quantum evolution differ in this framework by the relation their actor satisfies, $\langle\tilde{\Lambda}\rangle_{\natural} = 1$ or $\tilde{U}\tilde{U}^{*} = e_t$, and not by the shape of the action. The intersection of the two classes is the rotation group $SU(2)$, which is the group common to the two readings. This is the sharpest single statement of the "two faces of one algebra" thesis, and it is established material rather than a proposal. -->

### The Two Actors Are Not the Same Group

The formula in question is not new here. *Biquaternion Rotations and Lorentz Transformations* defines the conjugation $\Phi_{\tilde{\Lambda}}(\tilde{B}) = \tilde{\Lambda}\tilde{B}\tilde{\Lambda}^{*}$ on the whole algebra and proves that it carries each of the two sectors to itself and preserves the norm on both. What the previous subsection adds is only the reading of that one map on the two sectors in turn, and the actor substituted into it. The two substitutions are:

$$
\tilde{\Lambda}\tilde{\Lambda}^{\natural} = e_t
\quad\text{on } \mathbb{M}_-,
\qquad\qquad
\tilde{U}\tilde{U}^{*} = e_t
\quad\text{on } \mathbb{M}_+ .
$$

These are different groups. The unit-norm condition is $SL(2,\mathbb{C})$, whose action on a four-vector of $\mathbb{M}_-$ is the general proper orthochronous Lorentz transformation, boosts included. The unitary condition is $\mathrm{U}(2)$, whose action is conjugation, which fixes the scalar part and rotates the vector part:

$$
\tilde{U}\tilde{H}\tilde{U}^{*} = \tilde{U}\tilde{H}\tilde{U}^{-1},
\qquad
h_0 \ \text{fixed},
\qquad
\vec h \longmapsto R\,\vec h,
\qquad
R \in SO(3).
$$

That is a Lorentz transformation as well, but only a rotation, and no boost is available to it. Neither class contains the other: the boost rotor $\tilde{\Lambda} = \cosh(\phi/2)e_t + i\sinh(\phi/2)\vec u$ has unit norm and is far from unitary, while $\exp(i\theta)e_t$ is unitary with $N = \exp(2i\theta)$, equal to $1$ only when $\theta$ is a multiple of $\pi$. What the two classes share is their intersection, $SU(2)$, and what that intersection induces is the rotations.

The names of the two actors are the names of the two factors of the polar word. Every element of non-vanishing norm factors as $\tilde{Q} = r\,\exp(i\alpha)\tilde{B}\tilde{q}$, with a positive scale, a central phase, a positive definite Hermitian factor $\tilde{B}$ and a unit real quaternion rotor $\tilde{q}$ (*The Polar Element Representation in Subspaces*, *The Twisted Spinor Operator Representation of Biquaternions*). The two classes above are exactly the two ways of keeping two of those four factors:

| actor | polar form | which factor is free | group |
|---|---|---|---|
| unit-norm rotor | $\tilde{B}\tilde{q}$ | the boost factor $\tilde{B}$ | $SL(2,\mathbb{C})$ |
| unitary | $\exp(i\alpha)\tilde{q}$ | the central phase $\exp(i\alpha)$ | $\mathrm{U}(2)$ |
| both | $\tilde{q}$, any | neither | $Sp(1) = SU(2)$ |

So it is not merely that the two groups differ: **the boost factor is what a Lorentz transformation has and a unitary does not, and the central phase is what a unitary has and a boost does not.** The polar article states the first as its criterion for a trivial boost factor — $\tilde{Q}\tilde{Q}^{*}$ is a positive real multiple of $e_t$ exactly when $\tilde{B} = e_t$ — which in the matrix picture is the statement that the element is unitary up to a scale. The second is the same statement read the other way: unit norm forces $r = 1$ and $\exp(2i\alpha) = 1$, so the phase has no room and the boost factor has all of it. And the boost factor is not an outside object. It is $\tilde{B} = \sqrt{\tilde{Q}\tilde{Q}^{*}}/r$, a positive definite element of $\mathbb{M}_+$ itself, so the factor that carries a state off the trace-one slice belongs to the sector whose states they are. The twisted spinor article records the division on the other action: of the two, the unit-norm case is the Lorentz transformation on the material sector, while the unitary case is a rotation with no dilatation.

The dividing line is sharper than a statement about groups, and the corpus draws it. *The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone* records that the action is an inner automorphism exactly in the unitary sector, where $\tilde{A}^{*} = \tilde{A}^{-1}$, and not elsewhere; for a unit-norm rotor that equation means $\tilde{\Lambda}$ is a real quaternion — the pure-rotation case — while a boost has $\tilde{\Lambda}^{*} = \tilde{\Lambda}$, so $\tilde{\Lambda}^{*}\tilde{\Lambda} = \tilde{\Lambda}^{2} \neq e_t$ and the map is not multiplicative. That same equation, $\tilde{\Lambda}\tilde{\Lambda}^{*} = e_t$, is exactly unitarity. So one condition wears five faces:

$$
\tilde{U}\tilde{U}^{*} = e_t
\;\Longleftrightarrow\;
\tilde{U}^{*} = \tilde{U}^{-1}
\;\Longleftrightarrow\;
\Phi_{\tilde{U}} \ \text{is an algebra automorphism}
\;\Longleftrightarrow\;
\Phi_{\tilde{U}} \ \text{fixes the centre}
\;\Longleftrightarrow\;
\Phi_{\tilde{U}} \ \text{preserves the trace}.
$$

The unitary actor is therefore the one for which the shared formula is a symmetry of the algebra itself, an inner automorphism; the unit-norm boost actor is the one for which it is a symmetry only of the sector and of the cone. This is why the general Lorentz transformation acts on the cone of $\mathbb{M}_+$ but not on the states. The remark in *Biquaternion Rotations and Lorentz Transformations* that on the identity the conjugation returns $\tilde{Q}\tilde{Q}^{*}$, so that "the unit leaves the centre and the centre is carried into the Hermitian sector", is precisely the state-space statement: the image of the identity is

$$
\Phi_{\tilde{\Lambda}}(e_t) = \tilde{\Lambda}\tilde{\Lambda}^{*} = \tilde{\Lambda}^{2} = \cosh\phi\,e_t + i\sinh\phi\,\vec u,
$$

which is not central. On the maximally mixed state it gives

$$
\tfrac{1}{2}e_t \;\longmapsto\; \tfrac{1}{2}\bigl(\cosh\phi\,e_t + i\sinh\phi\,\vec u\bigr),
$$

of trace $\cosh\phi$, a positive definite element of $\mathbb{M}_+$ that is not a state. Not fixing the centre is not preserving the trace, and not preserving the trace is leaving the slice. The Lorentz group acts on the cone of the informational sector; the group that acts on its state space is the rotation group. That a qubit carries rotations and no boost is then not an assumption imported from quantum theory: it is the statement that the trace, the normalization of a state, is not a Lorentz invariant.


### The Sectors Are Anti-Isometric, Not Isomorphic

The map above is a real-linear bijection, and it is tempting to read it as an isomorphism of the two sectors. It is not, and the failure is one line. Multiplication by $i$ is central, so $i(\tilde{Q}\tilde{Y}) = (i\tilde{Q})\tilde{Y} = \tilde{Q}(i\tilde{Y})$; but

$$
(i\tilde{Q})(i\tilde{Y}) \;=\; i^2\,\tilde{Q}\tilde{Y} \;=\; -\,\tilde{Q}\tilde{Y},
$$

which is not $i(\tilde{Q}\tilde{Y})$ unless $\tilde{Q}\tilde{Y} = 0$. So $i$ is not multiplicative, and the two sectors are not isomorphic as algebras. The correct product rule inside one sector is a **reversal**,

$$
(\tilde{Q}\tilde{Y})^{*} \;=\; \tilde{Y}\tilde{Q}
\qquad
(\tilde{Q},\tilde{Y} \text{ in the same sector}),
$$

from which three consequences follow at once. First, $\tilde{Q}\tilde{Y}$ is Hermitian exactly when $\tilde{Q}$ and $\tilde{Y}$ commute, and anti-Hermitian exactly when they anticommute. Second, both cases occur: $(ie_t)^2 = -e_t$ is Hermitian, a commuting pair, while $\vec e_x \vec e_y = \vec e_z$ is anti-Hermitian, an anticommuting pair. So neither sector is a subalgebra of $\mathbb{B}$, and a product of two material four-vectors can leave the material sector. Third, the commutator always returns:

$$
(\tilde{Q}\tilde{Y} - \tilde{Y}\tilde{Q})^{*} \;=\; \tilde{Y}\tilde{Q} - \tilde{Q}\tilde{Y},
\qquad\text{so}\qquad
[\mathbb{M}_\pm,\mathbb{M}_\pm] \subseteq \mathbb{M}_- .
$$

The material sector is therefore closed under the bracket and not under the product, which is the form in which the Minkowski signature re-enters the algebra: the antilinear involution $\flat$ makes $\mathbb{M}_-$ a real slice whose complexification is $\mathbb{B}$, and $i$ identifies the two sectors only as anti-isometric real quadratic spaces, with $\langle i\tilde{Q}\rangle_{\natural} = -\langle\tilde{Q}\rangle_{\natural}$, not as algebras.


## What the Slice Picture Shows

The main structural points are these. The state space of a qubit is not postulated as a ball of vectors; it is the trace-one slice of a cone. The cone is the positive cone of the Hermitian subspace, and the positive cone is, in turn, exactly the future light cone of the algebra's biquaternion norm. The three conditions that define a state — Hermitian, positive, trace one — become membership in $\mathbb{M}_+$, a trace normalization, and a single quadratic inequality supplied by the biquaternion norm; positivity is not an extra axiom but the statement that the state lies in the cone. Purity is a boundary condition rather than a separate axiom: the pure states are the idempotents, the rank-one projections, and the zero divisors of trace one, all at once, and they are the extreme rays of the cone. Mixedness is the interior, and the biquaternion norm restricted to the slice is, up to a factor, the linear entropy. Entropy and fidelity are then functions of the radius and of the Bloch vectors in the Euclidean geometry of the slice.

Several points are left open in this picture. The base of the logarithm in the entropy is a convention, natural logarithms giving nats and base-two logarithms giving bits; the geometry does not prefer one. The normalization of the transition probability is likewise a convention, since some authors take the unsquared expression as the fidelity and others its square; the closed form above is stated for the squared normalization, which is the one that reduces to the pure-state transition probability. The extension of the slice picture to $n$ qubits requires the tensor product and the corresponding higher-dimensional cones, and the identification of the correct positivity domain there is a separate problem. Finally, this article has used only the future cone; the past cone, and the negative-trace elements of $\mathbb{M}_+$, have no state interpretation here, and whether they acquire one in a wider interpretation of the algebra is an open question.

The mirror interpretation adds the material face of the same object. Under the map $\tilde{H} = -\tfrac{i}{2}\tilde{Q}$ the ball is the trace-one slice of the timelike cone of the material sector, with the trace sign selecting the future sheet; positivity of a state is the causal condition $ct \geq |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|$, purity is nullness, and the maximally mixed state is the rest four-velocity of the material interpretation. The same action formula $\tilde{A}\tilde{Q}\tilde{A}^{*}$ serves both faces, the actor being a unit-norm rotor, hence a general Lorentz transformation, in one case and a unitary element, hence a rotation, in the other. What the two sectors are not is isomorphic: the product rule within a sector reverses the order, so a product of two material elements need not be material, while the commutator always is. The identity of the two faces is therefore an identity of quadratic spaces, not of algebras.

## Summary

The Hermitian subspace $\mathbb{M}_+$ of the biquaternion algebra carries a biquaternion norm of signature $(1,3)$, whose positive cone coincides exactly with its future light cone. The qubit state space is the intersection of that cone with the affine hyperplane $\{\mathrm{Sc} = \tfrac{1}{2}\}$. Writing a state as

$$
\tilde{Ϛ} = \tfrac{1}{2}\bigl(e_t + i\vec r\bigr),
$$

the intersection is the closed unit ball $|\vec r| \leq 1$, the **Bloch ball**, whose boundary is the intersection with the null cone.

The pure states are the boundary of the ball. Equivalently, they are the idempotents $\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$, the rank-one projections, the extreme rays of the positive cone, and the zero divisors of $\mathbb{B}$ at trace one; the boundary is parametrized by the Bloch sphere $S^2$. The mixed states are the interior, with eigenvalues $\tfrac{1}{2}(1 \pm |\vec r|)$; the maximally mixed state is the centre $\vec r = 0$.

Purity is $\mathrm{Tr}(\tilde{Ϛ}^2) = \tfrac{1}{2}(1 + |\vec r|^2)$, so the Bloch radius is a measure of purity, and the linear entropy is $1 - \mathrm{Tr}(\tilde{Ϛ}^2) = 2\langle\tilde{Ϛ}\rangle_{\natural}$, twice the biquaternion norm. The von Neumann entropy depends only on $|\vec r|$, vanishing on the boundary and maximal, equal to $\log 2$, at the centre. The Uhlmann transition probability has the closed form $\tfrac{1}{2}\bigl(1 + \vec r\cdot\vec s + \sqrt{(1-|\vec r|^2)(1-|\vec s|^2)}\bigr)$, reducing on the boundary to $\cos^2(\theta/2)$. In every case the state space, its purity stratification, its entropy, and its fidelity are read off from the biquaternion norm and the trace on $\mathbb{M}_+$, without additional postulates.

The ball has a mirror interpretation in the material sector. The map $\tilde{H} = -\tfrac{i}{2}\tilde{Q}$ carries $\mathbb{M}_-$ onto $\mathbb{M}_+$, sends the material four-vector $ict\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ to $\tfrac{1}{2}(ct\,e_t - i(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z))$, and satisfies $\mathrm{Tr}(\tilde{H}) = ct$ and $\langle\tilde{H}\rangle_{\natural} = -\tfrac{1}{4}\langle\tilde{Q}\rangle_{\natural}$. The image is a state exactly at $ct = 1$, where it is $\tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r)$ with $\vec r = -(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$. On that slice the map turns positivity of a state into the causal condition $ct \geq |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|$: the ball is the trace-one slice of the timelike cone, the pure states are its lightlike elements, and the maximally mixed state is the rest four-vector. The future cone maps onto the positive elements and the past cone onto the negative definite ones, so the trace sign, not the sign of the norm, selects the state sheet — which is why the past cone has no state interpretation here. Both interpretations use the one action $\Gamma_{\tilde{A}}(\tilde{Q}) = \tilde{A}\tilde{Q}\tilde{A}^{*}$, with a unit-norm rotor as actor on the material side and a unitary element on the informational side. The two actors are different groups: the unit-norm rotor gives the full Lorentz group, boosts included, while the unitary gives only the rotations of the ball, because unitarity is exactly the condition that preserves the trace and the trace-one slice is the state space. What the map is not is an algebra isomorphism: $i$ is not multiplicative, so $(i\tilde{Q})(i\tilde{Y}) = -\tilde{Q}\tilde{Y} \neq i(\tilde{Q}\tilde{Y})$; within a sector the product reverses the order, $(\tilde{Q}\tilde{Y})^{*} = \tilde{Y}\tilde{Q}$, so a product of two material elements need not be material, while the commutator always lands in $\mathbb{M}_-$. The two sectors are anti-isometric real quadratic spaces with $\langle i\tilde{Q}\rangle_{\natural} = -\langle\tilde{Q}\rangle_{\natural}$, not isomorphic algebras.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{C}_{\mathbb{B}}$ | Complex subspace (centre), fixed points of quaternion conjugation |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, fixed points of complex conjugation |
| $\mathbb{M}_+$ | Hermitian subspace, fixed points of ${}^{*}$ |
| $\mathbb{M}_-$, with $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ | Anti-Hermitian subspace, fixed points of $\flat$ |
| $\tilde{H} = h_0 e_t + i\vec h$ | General Hermitian element |
| $\mathrm{Tr}(\tilde{H}) = 2 h_0$ | Trace |
| $\langle\tilde{H}\rangle_{\natural} = \langle\tilde{H},\tilde{H}\rangle_{\natural} = \tilde{H}\tilde{H}^{\natural} = (h_0^2 - |\vec h|^2)e_t$ | Biquaternion norm, signature $(1,3)$ |
| $\mathrm{Tr}(\tilde{H}\tilde{K}) = 2(h_0 k_0 + \vec h\cdot\vec k)$ | Trace pairing, signature $(4,0)$ |
| $\mathcal{S} = \{\mathrm{Sc} = \tfrac{1}{2}\}$ | Trace-one hyperplane |
| $\tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r)$ | State, Bloch vector $\vec r$ |
| $\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$ | Idempotent (pure state), $|\vec u| = 1$ |
| $\mathrm{Tr}(\tilde{Ϛ}^2) = \tfrac{1}{2}(1 + |\vec r|^2)$ | Purity |
| $S(\tilde{Ϛ}) = -\mathrm{Tr}(\tilde{Ϛ}\log\tilde{Ϛ})$ | Von Neumann entropy |
| $T(\tilde{Ϛ},\tilde{\sigma}) = (\mathrm{Tr}\sqrt{\sqrt{\tilde{Ϛ}}\,\tilde{\sigma}\sqrt{\tilde{Ϛ}}})^2$ | Uhlmann transition probability |
| $S^2 = SU(2)/\mathrm{U}(1)$ | Boundary (Bloch) sphere as a homogeneous space |
| $H^\pm = SU(1,1)/\mathrm{U}(1)$, $H^{sl}$ | Time-like two-sheeted and space-like one-sheeted hyperboloids of $\mathbb{R}^{1,2}$ |
| $[u|v] = u^{\dagger}\sigma_3 v$ | Indefinite $SU(1,1)$-invariant pairing on the spinor module |
| $\tilde{H} = -\tfrac{i}{2}\tilde{Q}$ | Mirror map carrying $\mathbb{M}_-$ onto $\mathbb{M}_+$ |
| $\mathrm{Tr}(\tilde{H}) = ct$, $\langle\tilde{H}\rangle_{\natural} = -\tfrac{1}{4}\langle\tilde{Q}\rangle_{\natural}$ | Trace and norm under the mirror map |
| $(\tilde{Q}\tilde{Y})^{*} = \tilde{Y}\tilde{Q}$ | Product rule within a sector; $[\mathbb{M}_\pm,\mathbb{M}_\pm] \subseteq \mathbb{M}_-$ |
| $\tilde{Q} = r \exp(i\alpha)\tilde{B}\tilde{q}$ | Polar word: scale, central phase, boost factor, rotor |
| $\tilde{B}$, $\tilde{q}$ | Boost factor, in $\mathbb{M}_+$ positive definite; rotor, in $Sp(1)$ |
| $\tilde{B}\tilde{q}$, $\exp(i\alpha)\tilde{q}$ | The two actors: $SL(2,\mathbb{C})$ on the cone, $\mathrm{U}(2)$ on the slice; both meet at $Sp(1) = SU(2)$ |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |

## Further Reading

- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Bloch sphere, the density matrix formalism, and the standard fidelity.
- Ingemar Bengtsson and Karol Życzkowski, *Geometry of Quantum States* (Cambridge, 2006), for the differential and convex geometry of the state space and the Bloch ball.
- Asher Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for the operational meaning of states, purity, and distinguishability.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the spin-1/2 formalism and the Bloch vector.
- Richard Jozsa, "Fidelity for mixed quantum states," *Journal of Modern Optics* **41** (1994) 2315–2323, for the closed-form Uhlmann fidelity of a qubit.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the algebraic structure of $\mathrm{Cl}_{1,3}$ and its idempotents.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra treatment of spinors, projectors, and the light cone.
- Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones* (Oxford, 1994), for the cone-of-squares description of the positive cone of a Euclidean Jordan algebra.
- J. D. Simão, "Biquaternions, Majorana spinors and time-like spin-foams," arXiv:2401.10324 [gr-qc] (2024), for the spinor models of $S^2$, $H^\pm$ and $H^{sl}$ with the definite and the indefinite pairing, and for the causal grading that makes the Bloch sphere the compact member of the family. External; cited for the family only.
