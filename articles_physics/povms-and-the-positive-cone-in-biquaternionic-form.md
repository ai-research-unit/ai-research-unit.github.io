# __POVMs and the Positive Cone in Biquaternionic Form__

## Introduction

The most general measurement that quantum physics admits is not a projective measurement. It is a **positive operator-valued measure**: a family of positive elements summing to the identity, each paired with the state by the Born rule. In the biquaternion framework these elements are elements of the Hermitian subspace $\mathbb{B}_{\Psi}$, and the condition that a measurement be possible is the condition that they lie in the **positive cone** of the algebra. This article develops the cone, the effects it contains, and the general measurement, in the framework's own terms.

The central observation is that the positive cone of $\mathbb{B}_{\Psi}$ is the positive cone of the biquaternion norm. For a Hermitian element $\tilde{\mathcal E}_{\Psi} = a_te_t + i\vec a$ with $a_t\in\mathbb{R}$, $\vec a\in\mathbb{R}^3$, positivity of the operator is

$$
\boxed{\;\tilde{\mathcal E}_{\Psi}\geq0 \quad\Longleftrightarrow\quad \langle\tilde{\mathcal E}_{\Psi}\rangle_{\natural} = a_t^2 - |\vec a|^2 \geq 0 \ \text{ and }\ a_t\geq0
\quad\Longleftrightarrow\quad a_t\geq|\vec a|\;},
$$

so the cone of the algebra is the future light cone of the biquaternion norm. An **effect** is an element of the operator interval $0\leq\tilde{\mathcal E}_{\Psi}\leq e_t$, which in coefficients reads $|\vec a|\leq\min(a_t,1-a_t)$; a **POVM** is a resolution of the identity by effects, $\sum_y\tilde{\mathcal E}_{\Psi,y} = e_t$; and the Born weight for the measurement is the normalised Hermitian form $\langle\tilde{Ϛ}_{\Psi},\tilde{\mathcal E}_{\Psi,y}\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}$, read as $p_y = \mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{\mathcal E}_{\Psi,y}^{*})/\mathrm{Sc}(\tilde{Ϛ}_{\Psi})$; the value is read once, at normalisation. The projective measurements are the special case in which the effects are idempotents, and they are the extreme elements of the set of effects; the general measurement is a convex decomposition of the identity into non-extreme effects, and it is strictly more powerful.

The cone is self-dual with respect to the Hermitian form (the matrix trace of the $2\times2$ image, halved), which is the algebraic reason the pairing serves both as the Born rule and as the duality that makes the measurement formalism work. The article derives this, characterizes the effects, exhibits the general POVM, and works two examples: the **trine** POVM, which distinguishes three equatorial states better than any projective measurement, and unambiguous discrimination, which two non-orthogonal states admit with a POVM and not with a projective measurement. The general measurement's realization as a projective measurement on a larger system — Naimark's dilation — is stated in the framework's language, and its status as an extension of the algebra is noted.

## The Positive Cone

### Positivity as the biquaternion norm

Let $\tilde H_\Psi = h_t\,e_t + i\vec h_\Psi$ be a general Hermitian element, with $h_t\in\mathbb{R}$ and $\vec h_\Psi\in\mathbb{R}^3$. Its matrix image is $h_t\,I_2 + \vec h_\Psi\cdot\boldsymbol{\sigma}$, whose eigenvalues are $h_t\pm|\vec h_\Psi|$. Hence

$$
\tilde H_\Psi\geq0 \quad\Longleftrightarrow\quad h_t \geq |\vec h_\Psi| ,
$$

and the biquaternion norm is

$$
\langle\tilde H_\Psi\rangle_{\natural} = \langle\tilde H_\Psi,\tilde H_\Psi\rangle_{\natural} = \tilde H_\Psi\tilde H_\Psi^{\natural} = h_t^2 - |\vec h_\Psi|^2 = \det M(\tilde H_\Psi),
$$

a real scalar. The two conditions $\langle\tilde H_\Psi\rangle_{\natural}\geq0$ and $h_t\geq0$ are together equivalent to $h_t\geq|\vec h_\Psi|$, so the set of positive elements is the future light cone of the biquaternion norm:

$$
C_+ = \bigl\{h_t\,e_t + i\vec h_\Psi\in\mathbb{B}_{\Psi} : h_t \geq |\vec h_\Psi|\bigr\} .
$$

This is the **positive cone** of the algebra. Its boundary $h_t = |\vec h_\Psi|$ is the set of positive elements of rank one — the rank-one Hermitian idempotents and their non-negative multiples — which are the zero divisors of the biquaternion norm. Its interior $h_t>|\vec h_\Psi|$ is the set of positive definite elements.

### The cone is self-dual

The Hermitian form on $\mathbb{B}_{\Psi}$ is

$$
\langle\tilde H_\Psi,\tilde{\mathcal E}_{\Psi}\rangle_{*} = \mathrm{Sc}(\tilde H_\Psi\tilde{\mathcal E}_{\Psi}^{*}) = h_t\,a_t + \vec h_\Psi\cdot\vec a,
$$

where $\tilde{\mathcal E}_{\Psi} = a_te_t + i\vec a$, and the doubled pairing $2\langle\tilde H_\Psi,\tilde{\mathcal E}_{\Psi}\rangle_{*}$ is the matrix trace of the $2\times2$ image. Direct computation of the Hermitian form on the Hermitian basis gives

$$
\langle e_t,e_t\rangle = 1, \qquad \langle e_t,i\vec e_k\rangle = 0, \qquad \langle i\vec e_j,i\vec e_k\rangle = \delta_{jk},
$$

so the Hermitian form is the positive definite Euclidean form of inertia $(4,0)$ in the coefficients. The **dual cone** is

$$
C_+^{*} = \bigl\{\tilde H_\Psi : \langle\tilde H_\Psi,\tilde{\mathcal E}_{\Psi}\rangle_{*}=\mathrm{Sc}(\tilde H_\Psi\tilde{\mathcal E}_{\Psi}^{*})\geq0 \ \text{ for all } \tilde{\mathcal E}_{\Psi}\in C_+\bigr\},
$$

and it coincides with $C_+$. To see this, if $h_t\geq|\vec h_\Psi|$ then $h_t\,a_t+\vec h_\Psi\cdot\vec a\geq h_t\,a_t-|\vec h_\Psi|\,|\vec a|\geq0$ for every $a_t\geq|\vec a|$, so $C_+^{*}\supseteq C_+$. Conversely, if $h_t<|\vec h_\Psi|$, take $\tilde{\mathcal E}_{\Psi}$ on the boundary with $\vec a = -\lambda\,\vec u_\Psi$ and $a_t = \lambda$; then $h_t\,a_t+\vec h_\Psi\cdot\vec a = \lambda(h_t-|\vec h_\Psi|)<0$ for $\lambda>0$, so $\tilde H_\Psi\notin C_+^{*}$. Hence $C_+^{*}=C_+$: **the positive cone is self-dual with respect to the Hermitian form.**

The self-duality is what makes the Hermitian form the natural pairing of measurement theory. The same pairing that gives the Born rule, $p_y = \langle\tilde{Ϛ}_{\Psi},\tilde{\mathcal E}_{\Psi,y}\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}$, expresses the duality between states and effects, and it makes the cone its own dual. There is no second pairing needed to define the allowed measurements.

### Extremal rays and the pure states

The extreme rays of $C_+$ are the rays through the rank-one Hermitian idempotents $\tilde\Pi_{\mathrm{id},1}(\vec u) = \tfrac12(e_t+i\vec u)$ and their positive multiples; every positive element is a non-negative combination of these. On the normalised slice — the intersection of $C_+$ with the affine hyperplane $2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}) = 1$ — the extreme points are exactly the pure states. This is the cone-theoretic statement of the fact, developed in the companion articles, that the Bloch ball is the normalised slice of the cone and its boundary is the set of idempotents. The normalized states are a section of the cone, and the pure states are its extreme rays.

## Effects

### Definition

An **effect** is a positive element bounded above by the identity:

$$
0 \;\leq\; \tilde{\mathcal E}_{\Psi} \;\leq\; e_t .
$$

Effects are the possible measurement outcomes. Writing $\tilde{\mathcal E}_{\Psi} = a_te_t+i\vec a$, the two inequalities are

$$
a_t \geq |\vec a| \qquad \text{and} \qquad 1-a_t \geq |\vec a|,
$$

because $e_t-\tilde{\mathcal E}_{\Psi} = (1-a_t)e_t - i\vec a$ is positive exactly when $1-a_t\geq|\vec a|$. Equivalently,

$$
\boxed{\;|\vec a| \;\leq\; \min\bigl(a_t,\ 1-a_t\bigr)\;},
$$

which requires $0\leq a_t\leq1$. The set of effects is thus the intersection of the cone $C_+$ with its reflection $e_t - C_+$; it is a compact convex body, the **operator interval** $[0,e_t]$.

### The extremes of the effect body

The extreme points of the operator interval are exactly the idempotents,

$$
\boxed{\;\tilde{\mathcal E}_{\Psi}^2 = \tilde{\mathcal E}_{\Psi} \quad\Longleftrightarrow\quad \tilde{\mathcal E}_{\Psi}\in\mathrm{ext}[0,e_t]\;},
$$

i.e. the elements $a_t = 1$ with $|\vec a|=0$ (the identity) and $a_t = \tfrac12$ with $|\vec a| = \tfrac12$ (the rank-one Hermitian idempotents). A **projective measurement** uses only these extreme effects; a general measurement uses interior effects, which are convex combinations $\tilde{\mathcal E}_{\Psi} = t\tilde\Pi_{\mathrm{id},1} + (1-t)\tilde\Pi_{\mathrm{id},2}$ of orthogonal idempotents. An interior effect is a "soft" outcome: it responds partially to both alternatives, which is exactly what allows a measurement to have more outcomes than the dimension.

### The Born rule for effects

For any state $\tilde{Ϛ}_{\Psi}$ and effect $\tilde{\mathcal E}_{\Psi}$ the probability is the normalised Hermitian form

$$
p=\frac{\langle\tilde{Ϛ}_{\Psi},\tilde{\mathcal E}_{\Psi}\rangle_{*}}{\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}}
=\frac{\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{\mathcal E}_{\Psi}^{*})}{\mathrm{Sc}(\tilde{Ϛ}_{\Psi})}
=\frac{\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{\mathcal E}_{\Psi})}{\mathrm{Sc}(\tilde{Ϛ}_{\Psi})}\in[0,1],
$$

because $\tilde{Ϛ}_{\Psi}\geq0$, $\tilde{\mathcal E}_{\Psi}\geq0$ make the pairing non-negative, and $\tilde{\mathcal E}_{\Psi}\leq e_t$ gives $p\leq1$. This is the Born rule in its general form; the projective case is $\tilde{\mathcal E}_{\Psi} = \tilde\Pi_{\mathrm{id}}$, and then the same ratio is the usual probability of an eigenspace.

The value is read at normalisation. Since $2\,\mathrm{Sc}(e_t)=2$ and $2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi})=1$, the ratio is

$$
p=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{\mathcal E}_{\Psi}^{*})=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{\mathcal E}_{\Psi}),
$$

On $\mathbb{B}_{\Psi}$ both factors are Hermitian, so the star is inert and $\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{\mathcal E}_{\Psi}^{*})=\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{\mathcal E}_{\Psi})$. The scalar part of the product is real, because $(AB)^{\dagger}=BA$ for Hermitian $A,B$ makes it equal to its own conjugate; it is non-negative for $0\le\tilde{\mathcal E}_{\Psi}\le e_t$, because $\mathrm{Sc}(AB)=\mathrm{Sc}(A^{1/2}BA^{1/2})\ge0$ when both factors are positive. Hence $p=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{\mathcal E}_{\Psi})\in[0,1]$, which is the usual matrix expression with the trace replaced by twice the scalar part. No additional postulate is required for the general measurement: functions of effects are obtained by the same Hermitian form.

## POVMs

### Definition and statistics

A **positive operator-valued measure** is a finite or countable family of effects resolving the identity:

$$
\tilde{\mathcal E}_{\Psi,y} \geq 0, \qquad \sum_y \tilde{\mathcal E}_{\Psi,y} = e_t .
$$

Given a state $\tilde{Ϛ}_{\Psi}$, the outcome probabilities are $p_y=\langle\tilde{Ϛ}_{\Psi},\tilde{\mathcal E}_{\Psi,y}\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{\mathcal E}_{\Psi,y}^{*})/\mathrm{Sc}(\tilde{Ϛ}_{\Psi})$; on $\mathbb{B}_{\Psi}$ this is the plain scalar $\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{\mathcal E}_{\Psi,y})/\mathrm{Sc}(\tilde{Ϛ}_{\Psi})$, that is $p_y=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{\mathcal E}_{\Psi,y})$ at normalisation. They are non-negative and sum to one:

$$
\sum_y p_y = \mathrm{Sc}\!\left(\tilde{Ϛ}_{\Psi}\sum_y\tilde{\mathcal E}_{\Psi,y}\right)\Big/\mathrm{Sc}(\tilde{Ϛ}_{\Psi}) = \frac{\mathrm{Sc}(\tilde{Ϛ}_{\Psi})}{\mathrm{Sc}(\tilde{Ϛ}_{\Psi})} = 1 ,
$$
since $\sum_y\tilde{\mathcal E}_{\Psi,y}=e_t$ and $\mathrm{Sc}(e_t)=1$.

A **projection-valued measure** is the special case in which every $\tilde{\mathcal E}_{\Psi,y}$ is idempotent; then the effects are orthogonal, $\tilde{\mathcal E}_{\Psi,y}\tilde{\mathcal E}_{\Psi,y_2} = \delta_{yy_2}\tilde{\mathcal E}_{\Psi,y}$, and the POVM is a projective measurement. Every PVM is a POVM; the converse fails.

### The post-measurement state

A general measurement is specified not only by the outcome probabilities but by the state left behind. If the effect is written in a Kraus form

$$
\tilde{\mathcal E}_{\Psi,y} = \tilde M_{\mathrm{kraus},y}^{*}\tilde M_{\mathrm{kraus},y} , \qquad \tilde M_{\mathrm{kraus},y}\in\mathbb{B},
$$

then the unnormalized post-measurement state is $\tilde M_{\mathrm{kraus},y}\tilde{Ϛ}_{\Psi}\tilde M_{\mathrm{kraus},y}^{*}$ and the normalized state is

$$
\tilde{Ϛ}_{\Psi,y} = \frac{\tilde M_{\mathrm{kraus},y}\tilde{Ϛ}_{\Psi}\tilde M_{\mathrm{kraus},y}^{*}}{2\,\mathrm{Sc}(\tilde M_{\mathrm{kraus},y}\tilde{Ϛ}_{\Psi}\tilde M_{\mathrm{kraus},y}^{*})},
$$

The outcome probability is $p_y=\mathrm{Sc}(\tilde M_{\mathrm{kraus},y}\tilde{Ϛ}_{\Psi}\tilde M_{\mathrm{kraus},y}^{*})/\mathrm{Sc}(\tilde{Ϛ}_{\Psi})=2\,\mathrm{Sc}(\tilde M_{\mathrm{kraus},y}\tilde{Ϛ}_{\Psi}\tilde M_{\mathrm{kraus},y}^{*}) = 2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{\mathcal E}_{\Psi,y}^{*})=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{\mathcal E}_{\Psi,y})$, which at normalisation is the outcome probability $p_y$, and the resolution of the identity is $\sum_y\tilde M_{\mathrm{kraus},y}^{*}\tilde M_{\mathrm{kraus},y} = e_t$. The measurement is therefore an **instrument**: a family of completely positive maps indexed by the outcome, one of which occurs. This is the measurement side of the channel formalism of the companion article *Quantum Channels and the Reversible/Irreversible Dichotomy*; a measurement followed by discarding the outcome is the channel $Ξ(\tilde{Ϛ}_{\Psi}) = \sum_y\tilde M_{\mathrm{kraus},y}\tilde{Ϛ}_{\Psi}\tilde M_{\mathrm{kraus},y}^{*}$.

### The Polar Form of an Effect

The Kraus form has a polar reading. Write each Kraus operator as

$$
\tilde M_{\mathrm{kraus},y}=\tilde H_{\Psi,\mathrm{pos},y}\tilde Q_{\mathrm{p},y},
\qquad
\tilde H_{\Psi,\mathrm{pos},y}=\sqrt{\tilde M_{\mathrm{kraus},y}\tilde M_{\mathrm{kraus},y}^{*}},
$$

with $\tilde H_{\Psi,\mathrm{pos},y}$ Hermitian positive semidefinite and $\tilde Q_{\mathrm{p},y}$ a partial isometry. Then

$$
\tilde{\mathcal E}_{\Psi,y}=\tilde M_{\mathrm{kraus},y}^{*}\tilde M_{\mathrm{kraus},y}
=\tilde Q_{\mathrm{p},y}^{*}\tilde H_{\Psi,\mathrm{pos},y}^{2}\tilde Q_{\mathrm{p},y}.
$$

The effect is the squared strength conjugated by the backaction. Its eigenvalues are the squares of the singular values of $\tilde M_{\mathrm{kraus},y}$. For an invertible amplitude in the complete polar decomposition $\varrho e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$, the singular values are $\varrho e^{\pm\theta_{\mathrm{rpd},w}/2}$, with $\theta_{\mathrm{rpd},w}$ the rapidity of that boost factor, $\tanh\theta_{\mathrm{rpd},w}=v_{\mathrm b}/c$, so the effect has eigenvalues $r^{2}e^{\pm\theta_{\mathrm{rpd},w}}$: the scale and the rapidity survive and the angles drop out. The effect therefore sees the strength but not the backaction: $\tilde M_{\mathrm{kraus},y}$ and $\tilde U\tilde M_{\mathrm{kraus},y}$ with $\tilde U$ $*$-unitary have the same effect and different polar factors.

Here $\theta_{\mathrm{pha}}$ is the phase of the polar form: it is the argument of the central complex scalar, a real angle taken modulo a full turn, and the exponential that carries it is $\exp(i\theta_{\mathrm{pha}})$.

The strata are the strata of the effect body. A **sharp** effect is $\tilde{\mathcal E}_{\Psi,y}=\tilde\Pi_{\mathrm{id}}$; then $\tilde M_{\mathrm{kraus},y}=\tilde\Pi_{\mathrm{id}}$, $\tilde H_{\Psi,\mathrm{pos},y}=\tilde\Pi_{\mathrm{id}}$ and $\tilde Q_{\mathrm{p},y}=\tilde\Pi_{\mathrm{id}}$, and the amplitude is a zero divisor on the null cone. A **soft rank-one** effect is $\tilde{\mathcal E}_{\Psi,y}=\lambda\tilde\Pi_{\mathrm{id}}$ with $0<\lambda<1$; then $\tilde M_{\mathrm{kraus},y}=\sqrt{\lambda}\,\tilde\Pi_{\mathrm{id}}$, $\tilde H_{\Psi,\mathrm{pos},y}=\sqrt{\lambda}\,\tilde\Pi_{\mathrm{id}}$ and $\tilde Q_{\mathrm{p},y}=\tilde\Pi_{\mathrm{id}}$, and the amplitude is again null, although the effect is on the boundary of the cone and not at an extreme point. A **full-rank** effect is $\tilde{\mathcal E}_{\Psi,y}>0$; then $\tilde M_{\mathrm{kraus},y}$ is invertible, $\tilde H_{\Psi,\mathrm{pos},y}$ is positive definite, $\tilde Q_{\mathrm{p},y}$ is $*$-unitary, and the effect lies in the interior of the effect body. The extreme points of the body are $0$, $e_t$ and the rank-one projectors; the polar form reaches the interior through invertible amplitudes. The null cone of the amplitude is therefore the rank-one boundary of the effect cone, not only the sharp set. The companion article *The Polar Decomposition of a Kraus Operator* works the examples and gives the measurement reading.

### Naimark dilation

Every POVM on the defining module $S$ is the compression of a projective measurement on a larger module. There is an ancillary space $\mathbb{C}^d$, an isometry $V:S\to S\otimes\mathbb{C}^d$, and a PVM $\{\tilde{F}_y\}$ on the larger space such that

$$
\boxed{\;\tilde{\mathcal E}_{\Psi,y} = V^\dagger \tilde{F}_y V\;}.
$$

This is **Naimark's dilation theorem**, the measurement analogue of Stinespring's dilation for channels. In the framework's language, the dilation adjoins an ancillary factor and replaces the general effects by orthogonal idempotents; the price is that the ancillary factor must be reduced over, which is precisely the information loss that a non-projective measurement represents. The dilation is standard; it is cited, not derived, and it belongs to the same circle of ideas as the Kraus representation of channels. It also shows why the framework's general measurement theory does not require abandoning the idempotent picture of a projective measurement: it embeds it in a larger algebra.

## Two Worked Examples

### The trine POVM

Let $\vec u_k$, $k=1,2,3$, be three unit vectors in the equatorial plane at $120^\circ$ from one another, so that $\sum_{k\in\{x,y,z\}}\vec u_k = 0$ and $\sum_{k\in\{x,y,z\}}\tilde\Pi_{\mathrm{id},1}(\vec u_k) = \tfrac32 e_t$. Define

$$
\tilde{\mathcal E}_{\Psi,k} = \tfrac{2}{3}\,\tilde\Pi_{\mathrm{id},1}(\vec u_k), \qquad k=1,2,3 .
$$

Each $\tilde{\mathcal E}_{\Psi,k}$ is an effect — its coefficients are $a_t = \tfrac13$ and $|\vec a| = \tfrac13$, on the boundary of the interval — and they resolve the identity:

$$
\sum_{k\in\{x,y,z\}}\tilde{\mathcal E}_{\Psi,k} = \tfrac{2}{3}\sum_{k\in\{x,y,z\}}\tilde\Pi_{\mathrm{id},1}(\vec u_k) = \tfrac{2}{3}\cdot\tfrac{3}{2}e_t = e_t .
$$

The trine POVM has three outcomes, which no projective measurement of a qubit can have. For the three equally likely states $\tilde{Ϛ}_{\Psi,k} = \tilde\Pi_{\mathrm{id},1}(\vec u_k)$, the probability of correctly identifying the state is

$$
P_{\mathrm{succ}} = \frac{1}{3}\sum_{k\in\{x,y,z\}}2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi,k}\tilde{\mathcal E}_{\Psi,k}^{*})
= \frac{1}{3}\sum_{k\in\{x,y,z\}}2\,\mathrm{Sc}\!\left(\tilde{Ϛ}_{\Psi,k}\,\tfrac23\tilde{Ϛ}_{\Psi,k}\right)
= \frac{1}{3}\sum_{k\in\{x,y,z\}}\frac{2}{3} = \frac{2}{3},
$$

since $\tilde{Ϛ}_{\Psi,k}^2 = \tilde{Ϛ}_{\Psi,k}$ and $2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi,k}) = 1$. A projective measurement of a qubit has only two outcomes and cannot separate three symmetric states as well; the trine POVM is the standard example of a genuinely non-projective measurement, and it is expressed here purely in terms of the idempotents and the plain form of the algebra.

### Unambiguous discrimination

Let two non-orthogonal pure states have overlap $c = |\langle\tilde{Ξ}_{0}|\tilde{Ξ}_{1}\rangle|\in(0,1)$. A **projective** measurement of a qubit has two outcomes, each of which responds to both states, so neither outcome can certify which state was prepared. A POVM with three effects can:

$$
\tilde{\mathcal E}_{\Psi,0} = \frac{1}{1+c}\,\tilde\Pi_{\mathrm{id}}\bigl(\tilde{Ξ}_{1}^{\perp}\bigr), \qquad
\tilde{\mathcal E}_{\Psi,1} = \frac{1}{1+c}\,\tilde\Pi_{\mathrm{id}}\bigl(\tilde{Ξ}_{0}^{\perp}\bigr), \qquad
\tilde{\mathcal E}_{\Psi,?} = e_t-\tilde{\mathcal E}_{\Psi,0}-\tilde{\mathcal E}_{\Psi,1} ,
$$

where $\tilde\Pi_{\mathrm{id}}(\tilde{Ξ}^{\perp})$ is the idempotent orthogonal to $|\tilde{Ξ}\rangle$. The effect $\tilde{\mathcal E}_{\Psi,0}$ annihilates $|\tilde{Ξ}_{1}\rangle$, so the outcome $0$ certifies $|\tilde{Ξ}_{0}\rangle$; symmetrically for outcome $1$; and outcome $?$ is inconclusive. The resolution holds because the largest eigenvalue of $\tilde{\mathcal E}_{\Psi,0}+\tilde{\mathcal E}_{\Psi,1}$ is $1$ at this normalization, and the success probability for equal priors is

$$
P_{\mathrm{succ}} = \mathrm{Sc}(\tilde{Ϛ}_{\Psi,0}\tilde{\mathcal E}_{\Psi,0}^{*}) + \mathrm{Sc}(\tilde{Ϛ}_{\Psi,1}\tilde{\mathcal E}_{\Psi,1}^{*})
= \tfrac12(1-c)+\tfrac12(1-c) = 1-c ,
$$

which is the standard Ivanovic–Dieks–Peres value. Unambiguous discrimination is thus possible exactly with a non-projective measurement, and its failure probability is the overlap. In the algebra the construction uses three effects, each of them a scaled idempotent of rank one and therefore on the boundary of the cone: the two conclusive outcomes are the idempotents orthogonal to the state they exclude, and the inconclusive outcome — the scaled idempotent $\tilde{\mathcal E}_{\Psi,?} = \frac{2c}{1+c}\tilde\Pi_{\mathrm{id}}(\vec u_m)$ for a suitable direction $\vec u_m$ — is the effect that makes the resolution complete.

## The Positive Cone and the Meaning of a Measurement

Collecting the structure, a measurement in the framework is a resolution of the identity into positive elements of $\mathbb{B}_{\Psi}$:

- **States** are the elements of the cone $C_+$ normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12$ (scalar part one half); the cone is the future light cone of the biquaternion norm.
- **Effects** are the elements of the operator interval $[0,e_t]$, i.e. the cone intersected with its reflection through $\tfrac12 e_t$; in coefficients, $|\vec a|\leq\min(a_t,1-a_t)$.
- **POVMs** are resolutions of the identity by effects; **PVMs** are the resolutions by idempotents, i.e. by extreme effects.
- **Probabilities** are the normalised Hermitian form $p_y=2\langle\tilde{Ϛ}_{\Psi},\tilde{\mathcal E}_{\Psi,y}\rangle_{*}$, read at normalisation; the pairing is the one under which the cone is self-dual.
- **Post-measurement states** are the Kraus images $\tilde M_{\mathrm{kraus},y}\tilde{Ϛ}_{\Psi}\tilde M_{\mathrm{kraus},y}^{*}$, normalized.

The general measurement is a convex decomposition of the identity into effects that are not extreme. The idempotents remain the extreme effects, and the projective measurement remains the extreme case; what the general measurement adds is the ability to have more outcomes than the dimension of the module, which is exactly what is needed for tasks such as state discrimination with more than two candidate states.

## What the Framework Does and Does Not Claim

**What it does.**

- It identifies the positive cone of $\mathbb{B}_{\Psi}$ with the future light cone of the biquaternion norm and derives the effect condition $|\vec a|\leq\min(a_t,1-a_t)$.
- It shows that the cone is self-dual with respect to the Hermitian form, so that one pairing serves both the Born rule and the state-effect duality.
- It identifies the idempotents as the extreme effects and the projective measurements as the extreme resolutions, with the general POVM as a convex decomposition.
- It expresses the general measurement, its Kraus form, and its post-measurement state entirely in terms of elements of $\mathbb{B}$.

**What it does not.**

- It does not derive the cone structure from a deeper principle; the cone is the positivity condition of the algebra, and positivity of a Hermitian operator is standard.
- It does not prove Naimark's theorem; the dilation is cited as standard.
- It does not claim that every POVM is physically implementable by a given apparatus; implementability is a dynamical question the algebra does not answer.
- It does not extend the classification of effects beyond the qubit; for higher-dimensional modules the effect body is more complicated, and the framework's defining module is two-dimensional.

## Open Questions

**1. The effect body in higher dimensions.** The characterization $|\vec a|\leq\min(a_t,1-a_t)$ is special to $M_2(\mathbb{C})$. For $\mathbb{B}\otimes\mathbb{B}$ and its effects, what is the analogous coefficient condition, and does the biquaternion norm of the tensor product define the cone?

**2. Instruments and information.** A general instrument produces a post-measurement state that depends on the outcome, and the information it leaves in the system is quantified by the disturbance it causes. Is there an algebraic characterization of the instruments that are "minimally disturbing" for a given POVM, in terms of the two sectors $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$?

**3. The self-duality and the two pairings.** The cone is self-dual under the plain form; the biquaternion norm defines the cone but is a different, indefinite pairing. Is there an algebraic relation between the two pairings — a form of Lorentzian duality — that explains why the cone is the biquaternion norm's cone and the measurement pairing is the normalised Hermitian form, read through the trace?

**4. Continuous POVMs.** The article treats finite POVMs. Position and momentum measurements require continuous families of effects; their biquaternion form, and the status of the biquaternion norm for unbounded effects, is open.

**5. Empirical content.** The POVM formalism in biquaternion form reproduces the standard one and predicts nothing new.

## Summary

A general measurement of a qubit is a resolution of the identity into positive elements of the Hermitian subspace. The positive cone of $\mathbb{B}_{\Psi}$ is the future light cone of the biquaternion norm:

$$
\tilde{\mathcal E}_{\Psi} = a_te_t+i\vec a\geq0 \quad\Longleftrightarrow\quad a_t\geq|\vec a| \quad\Longleftrightarrow\quad \langle\tilde{\mathcal E}_{\Psi}\rangle_{\natural} = a_t^2-|\vec a|^2\geq0,\ a_t\geq0,
$$

and the cone is self-dual with respect to the Hermitian form, $2\langle\tilde H_\Psi,\tilde{\mathcal E}_{\Psi}\rangle_{*} = 2(h_t\,a_t+\vec h_\Psi\cdot\vec a)$. An effect is an element of the operator interval $0\leq\tilde{\mathcal E}_{\Psi}\leq e_t$, characterized by $|\vec a|\leq\min(a_t,1-a_t)$; its extreme points are the idempotents, so the projective measurements are the extreme resolutions. A POVM is a family $\{\tilde{\mathcal E}_{\Psi,y}\}$ with $\tilde{\mathcal E}_{\Psi,y}\geq0$ and $\sum_y\tilde{\mathcal E}_{\Psi,y} = e_t$; the outcome probabilities are the normalised Hermitian form, $p_y=\langle\tilde{Ϛ}_{\Psi},\tilde{\mathcal E}_{\Psi,y}\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{\mathcal E}_{\Psi,y}^{*})/\mathrm{Sc}(\tilde{Ϛ}_{\Psi})$, read at normalisation as $p_y = 2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde{\mathcal E}_{\Psi,y})$, and the post-measurement states are the Kraus images. Every POVM is the compression of a projective measurement on a larger space (Naimark), and every measurement is an instrument, a family of completely positive maps indexed by the outcome. The cone, the effects, and the Born rule are thus all read off the algebra: positivity is the biquaternion norm's non-negativity, and measurement is the normalised Hermitian form on the effect body, read once at the end.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace (states and effects) |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion units, $\vec e_k^2 = -e_t$ |
| $i$ | Central scalar imaginary |
| $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm |
| $C_+ = \{h_t\,e_t+i\vec h_\Psi: h_t\ge\lvert\vec h_\Psi\rvert\}$ | Positive cone (future light cone of $\langle\cdot\rangle_{\natural}$) |
| $C_+^{*} = C_+$ | Self-duality under the Hermitian form |
| $2\langle\tilde H_\Psi,\tilde{\mathcal E}_{\Psi}\rangle_{*} = 2(h_t\,a_t+\vec h_\Psi\cdot\vec a)$ | Doubled Hermitian form |
| $0\le\tilde{\mathcal E}_{\Psi}\le e_t$ | Effect (operator interval) |
| $\lvert\vec a\rvert\le\min(a_t,1-a_t)$ | Effect condition in coefficients |
| $\mathrm{ext}[0,e_t] = \{\text{idempotents}\}$ | Extreme effects |
| $\{\tilde{\mathcal E}_{\Psi,y}\}$, $\tilde{\mathcal E}_{\Psi,y}\ge0$, $\sum_y\tilde{\mathcal E}_{\Psi,y} = e_t$ | POVM |
| $p_y = 2\langle\tilde{Ϛ}_{\Psi},\tilde{\mathcal E}_{\Psi,y}\rangle_{*}$ | Born rule for a POVM |
| $\tilde{\mathcal E}_{\Psi,y} = \tilde M_{\mathrm{kraus},y}^{*}\tilde M_{\mathrm{kraus},y}$ | Kraus form of an effect |
| $\tilde M_{\mathrm{kraus},y}=\tilde H_{\Psi,\mathrm{pos},y}\tilde Q_{\mathrm{p},y}$, $\tilde H_{\Psi,\mathrm{pos},y}=\sqrt{\tilde M_{\mathrm{kraus},y}\tilde M_{\mathrm{kraus},y}^{*}}$ | Polar form of the Kraus operator; $\tilde H_{\Psi,\mathrm{pos},y}\ge0$, $\tilde Q_{\mathrm{p},y}$ a partial isometry |
| $\tilde{\mathcal E}_{\Psi,y}=\tilde Q_{\mathrm{p},y}^{*}\tilde H_{\Psi,\mathrm{pos},y}^{2}\tilde Q_{\mathrm{p},y}$ | Effect as the backaction-conjugated squared strength |
| $\tilde{Ϛ}_{\Psi,y} = \tilde M_{\mathrm{kraus},y}\tilde{Ϛ}_{\Psi}\tilde M_{\mathrm{kraus},y}^{*}/p_y$ | Post-measurement state |
| $\tilde{\mathcal E}_{\Psi,y} = V^\dagger\tilde{F}_yV$ | Naimark dilation |
| $\tilde{\mathcal E}_{\Psi,k} = \tfrac23\tilde\Pi_{\mathrm{id},1}(\vec u_k)$ | Trine POVM |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- [The Polar Decomposition of a Kraus Operator: Effect, Backaction and the Measurement Boundary](the-polar-decomposition-of-a-kraus-operator-effect-backaction-and-the-measurement-boundary.html), for the strength, the backaction, and the null-cone reading of an effect.
- A. Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for POVMs, effects, and generalized measurements.
- K. Kraus, *States, Effects, and Operations* (Springer, 1983), for the operator-algebraic formulation of effects and instruments.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for POVMs, Naimark's dilation, and the post-measurement state.
- M. A. Naimark, "Spectral functions of a symmetric operator," *Izvestiya Akademii Nauk SSSR, Seriya Matematicheskaya* **4** (1940) 277–318, for the dilation of a POVM to a projective measurement.
- C. W. Helstrom, *Quantum Detection and Estimation Theory* (Academic Press, 1976), for state discrimination and the role of non-projective measurements.
- I. D. Ivanovic, "How to differentiate between non-orthogonal states," *Physics Letters A* **123** (1987) 257–259; D. Dieks, "Overlap and distinguishability of quantum states," *Physics Letters A* **126** (1988) 303–306; A. Peres, "How to differentiate between non-orthogonal states," *Physics Letters A* **128** (1988) 19, for unambiguous discrimination.
- I. Bengtsson and K. Życzkowski, *Geometry of Quantum States* (Cambridge, 2006), for the geometry of the state cone, the effect body, and self-duality.
- The companion articles of this series: [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html), [States, Observables and the Born Weight](states-observables-and-the-born-weight.html), [Quantum Channels and the Reversible/Irreversible Dichotomy](quantum-channels-and-the-reversible-irreversible-dichotomy.html), and [Decoherence as Idempotent Projection](decoherence-as-idempotent-projection.html).
