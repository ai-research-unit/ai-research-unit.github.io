# __The Polar Decomposition of a Kraus Operator: Effect, Backaction and the Measurement Boundary__

## Introduction

A Kraus operator is the amplitude of one outcome, not the outcome itself. The probability of the outcome is the trace of the effect $\tilde K^{*}\tilde K$; the post-measurement state is the normalized image $\tilde K\tilde{Ϛ}\tilde K^{*}$; and the element $\tilde K$ carries both, together with a phase that the probability discards. This article asks what the polar decomposition of $\tilde K$ says about the three objects.

The thesis is one sentence. **Every Kraus operator factors as $\tilde K=\tilde H_{\mathrm{pos}}\tilde U_{\mathrm{p}}$, with $\tilde H_{\mathrm{pos}}$ Hermitian positive semidefinite and $\tilde U_{\mathrm{p}}$ a partial isometry; the positive factor is the outcome's strength, the partial isometry is its backaction, and the effect is the squared strength conjugated by the backaction, $\tilde E=\tilde K^{*}\tilde K=\tilde U_{\mathrm{p}}^{*}\tilde H_{\mathrm{pos}}^{2}\tilde U_{\mathrm{p}}$.** Three consequences follow. A one-Kraus channel is trace preserving exactly when the strength is trivial, $\tilde H_{\mathrm{pos}}=e_t$, and then the channel is unitary. A sharp outcome has a rank-one amplitude on the null cone, where the strength is a scaled projection and the backaction a partial isometry. And the reversibility of a channel is its Kraus rank, not the strength of any single term: a channel can be a sum of terms whose individual polar factors are unitary and still be irreversible.

The distinction between one Kraus operator, an instrument, and a channel is the source of most misreadings: the polar decomposition is always available for one operator, while the one-Kraus unitarity and the multi-Kraus irreversibility are statements about a channel.

This article is the pilot of the polar programme in the physics corpus: the object is the Kraus operator of a measurement outcome, the examples are two-dimensional, and every numerical claim is checked in the matrix model. It does not derive the measurement postulate or classify channels; it tests the grammar of the generalized Cartan pairing on the object where that grammar has the most work to do.

The conventions are those of the companion articles. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^{2}=-e_t$, and central scalar imaginary $i$. The Hermitian conjugation is ${}^{*}$, the Hermitian subspace is $\mathbb{M}_+$, the anti-Hermitian subspace is $\mathbb{M}_-$. A state is $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$ with $\vec r\in\mathbb{R}^{3}$ and $|\vec r|\leq1$. The positive factor of the polar decomposition is written $\tilde H_{\mathrm{pos}}$ and the partial isometry $\tilde U_{\mathrm{p}}$; they are the $\tilde H$ and $\tilde U$ of the generalized Cartan pairing, and the subscripts keep them apart from the Hamiltonian $\tilde H_R$ and the unitary element $\tilde U$ of a channel. The trace is $\operatorname{Tr}\tilde Q=2\operatorname{Sc}\tilde Q=2Q_t$, read at normalisation.

## The Results It Uses

| result | established in | used here for |
|---|---|---|
| the generalized Cartan pairing on all of $\mathbb{B}$ | [*The Generalized Polar Decomposition of a Biquaternion: Partial Isometries and the Null Cone*](../articles_maths/the-general-polar-decomposition-of-a-biquaternion-partial-isometries-and-the-null-cone.html), §*The Biquaternion Reading* | $\tilde K=\tilde H_{\mathrm{pos}}\tilde U_{\mathrm{p}}$, $\tilde H_{\mathrm{pos}}=\sqrt{\tilde K\tilde K^{*}}$, $\tilde U_{\mathrm{p}}=\tilde H_{\mathrm{pos}}^{+}\tilde K$ |
| the Cartan pairing off the null cone | [*The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions*](../articles_maths/the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), §*The Statement* | the invertible case, where $\tilde U_{\mathrm{p}}$ is unitary |
| the positive cone and the Hermitian square root | [*Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*](../articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.html), §*The Polar Decomposition* | positivity of $\tilde H_{\mathrm{pos}}$ and of the effect |
| the rank-one Hermitian idempotents | [*Square Roots of One and the Idempotents of the Biquaternion Algebra*](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), §*The Classification of the Idempotents* | the sharp outcome $\tilde K=\tilde\Pi$ and the Bloch form of its projections |
| the zero-divisor cone | [*Norm Regularity and Degeneracy in the Biquaternion Algebra*](../articles_maths/norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), §*The Zero Divisor Set* | the boundary where the amplitude loses rank |
| the Kraus representation and the channel dichotomy | [*Quantum Channels and the Reversible/Irreversible Dichotomy*](quantum-channels-and-the-reversible-irreversible-dichotomy.html), §*The Kraus Representation* | the instrument and channel context |
| the effect as a Kraus square | [*POVMs and the Positive Cone in Biquaternionic Form*](povms-and-the-positive-cone-in-biquaternionic-form.html), §*The post-measurement state* | $\tilde E=\tilde K^{*}\tilde K$ and the Born weight |

## The Object and the Three Levels

### One Operator, One Outcome, One Channel

An **instrument** is a family of completely positive maps indexed by an outcome. In the algebra it is a family of Kraus operators $\tilde K_y$ with

$$
\tilde E_y=\tilde K_y^{*}\tilde K_y,\qquad \sum_y\tilde E_y=e_t,\qquad p_y=\operatorname{Tr}\!\left(\tilde{Ϛ}\,\tilde E_y\right),\qquad \tilde{Ϛ}_y=\frac{\tilde K_y\tilde{Ϛ}\tilde K_y^{*}}{p_y}.
$$

Dropping the outcome label gives the **channel**

$$
\Phi(\tilde{Ϛ})=\sum_y\tilde K_y\tilde{Ϛ}\tilde K_y^{*}.
$$

A single Kraus operator is a channel only when it is the whole instrument, that is, when $\tilde K^{*}\tilde K=e_t$. Otherwise it is one outcome among several, and its effect is not the identity.

The polar decomposition is a statement about $\tilde K$, not about the channel. It exists for every $\tilde K\in\mathbb{B}$, including $\tilde K=0$. It is unique once the initial and final projections are fixed, and it does not require the trace-preservation condition. The channel statements enter only when the Kraus operators are summed or when the one-term condition is imposed.

### The Three Statements That Must Not Be Confused

| statement | object | condition | content |
|---|---|---|---|
| polar form | one Kraus operator | none | $\tilde K=\tilde H_{\mathrm{pos}}\tilde U_{\mathrm{p}}$ |
| one-Kraus channel | the map $\tilde{Ϛ}\mapsto\tilde K\tilde{Ϛ}\tilde K^{*}$ | $\tilde K^{*}\tilde K=e_t$ | $\tilde K$ is unitary, $\tilde H_{\mathrm{pos}}=e_t$ |
| irreversible channel | the sum $\sum_y\tilde K_y\cdot\tilde K_y^{*}$ | minimal Kraus rank $\geq2$ | no single unitary represents the map |

The three rows are independent. A single Kraus operator can have a non-trivial $\tilde H_{\mathrm{pos}}$ and still be a legitimate outcome of an instrument. A single Kraus operator can have a trivial $\tilde H_{\mathrm{pos}}$ and belong to an irreversible channel. A channel can be a sum of two terms whose individual $\tilde H_{\mathrm{pos}}$ are scalar and whose individual $\tilde U_{\mathrm{p}}$ are unitary, and still be irreversible.

## The Polar Form of a Kraus Operator

### The Factorization

The generalized Cartan pairing, read with $\tilde Q=\tilde K$, gives the following. For every $\tilde K\in\mathbb{B}$ there is exactly one pair $(\tilde H_{\mathrm{pos}},\tilde U_{\mathrm{p}})$ with

1. $\tilde H_{\mathrm{pos}}$ Hermitian positive semidefinite and $\operatorname{ran}\tilde H_{\mathrm{pos}}=\operatorname{ran}\tilde K$;
2. $\tilde U_{\mathrm{p}}$ a partial isometry, $\tilde U_{\mathrm{p}}\tilde U_{\mathrm{p}}^{*}\tilde U_{\mathrm{p}}=\tilde U_{\mathrm{p}}$, with $\tilde U_{\mathrm{p}}^{*}\tilde U_{\mathrm{p}}$ the projection onto $\operatorname{ran}\tilde K^{*}$ and $\tilde U_{\mathrm{p}}\tilde U_{\mathrm{p}}^{*}$ the projection onto $\operatorname{ran}\tilde K$;
3. $\tilde K=\tilde H_{\mathrm{pos}}\tilde U_{\mathrm{p}}$.

It is

$$
\boxed{\;\tilde H_{\mathrm{pos}}=\sqrt{\tilde K\tilde K^{*}},\qquad \tilde U_{\mathrm{p}}=\tilde H_{\mathrm{pos}}^{+}\tilde K\;},
$$

with $\tilde H_{\mathrm{pos}}^{+}$ the Moore–Penrose inverse. This is the generalized polar decomposition of the mathematical article; it is cited, not re-proved.

### Strength and Backaction

In the singular value form, with at most two terms because $\mathbb{B}\cong M_2(\mathbb{C})$,

$$
\tilde K=\sum_i\sigma_i\,u_i v_i^{*},\qquad \tilde H_{\mathrm{pos}}=\sum_i\sigma_i\,u_i u_i^{*},\qquad \tilde U_{\mathrm{p}}=\sum_i u_i v_i^{*},
$$

with $\sigma_i\geq0$, and $u_i,v_i$ orthonormal in the matrix model. The two readings are:

- **strength**: the unordered pair $\{\sigma_1,\sigma_2\}$, the eigenvalues of $\tilde H_{\mathrm{pos}}$. It is basis-independent; it is the list of singular values of $\tilde K$.
- **backaction**: the partial isometry $\tilde U_{\mathrm{p}}$, which carries the input direction $v_i$ to the output direction $u_i$. Off the cone it is unitary; on the cone it has rank one.

The strength is what the outcome probability can see: the effect has eigenvalues $\sigma_i^{2}$. The backaction is what the probability discards: two amplitudes with the same singular values but different $\tilde U_{\mathrm{p}}$ have the same effect and different post-measurement states.

The domains are fixed once and for all:

| statement | domain | factors |
|---|---|---|
| generalized polar form | every $\tilde K\in\mathbb{B}$, including $0$ | $\tilde H_{\mathrm{pos}}\geq0$, $\tilde U_{\mathrm{p}}$ a partial isometry |
| Cartan pairing off the cone | $\langle\tilde K\rangle_{\natural}\neq0$ | $\tilde H_{\mathrm{pos}}>0$, $\tilde U_{\mathrm{p}}$ unitary |
| one-Kraus channel | $\tilde K^{*}\tilde K=e_t$ | $\tilde H_{\mathrm{pos}}=e_t$, $\tilde U_{\mathrm{p}}=\tilde K$ unitary |
| null case | $\langle\tilde K\rangle_{\natural}=0$, $\tilde K\neq0$ | $\operatorname{rank}\tilde H_{\mathrm{pos}}=1$, $\tilde U_{\mathrm{p}}$ rank one |

The strength decides the case of the operator, not the case of the channel; the four cases are collected in §*The Three Strata*.

## Trace Preservation Is the Triviality of the Strength

### The One-Kraus Channel

Let $\tilde K$ be the single Kraus operator of a channel. Trace preservation is

$$
\tilde K^{*}\tilde K=e_t .
$$

In $\mathbb{B}\cong M_2(\mathbb{C})$ this makes $\tilde K$ invertible, with inverse $\tilde K^{*}$; then $\tilde K\tilde K^{*}=e_t$ as well. Hence

$$
\tilde H_{\mathrm{pos}}=\sqrt{\tilde K\tilde K^{*}}=e_t,\qquad \tilde U_{\mathrm{p}}=\tilde K,
$$

and $\tilde K$ is unitary. Conversely, if $\tilde H_{\mathrm{pos}}=e_t$ and $\tilde U_{\mathrm{p}}$ is unitary, then $\tilde K=\tilde U_{\mathrm{p}}$ and $\tilde K^{*}\tilde K=e_t$. Therefore:

> A one-Kraus channel is trace preserving if and only if its positive factor is trivial; the channel is then conjugation by a unitary biquaternion.

This is the reversible case of *Quantum Channels and the Reversible/Irreversible Dichotomy*, read in the polar language. The Hamiltonian $\tilde H_R\in\mathbb{M}_+$ generates the unitary factor through $\tilde U=\exp(-i\tilde H_Rt'/\hbar)$, and the generator $-i\tilde H_R/\hbar$ lies in $\mathbb{M}_-$. The polar factor $\tilde U_{\mathrm{p}}$ is the evolution itself; its logarithm is the material generator. The condition $\tilde H_{\mathrm{pos}}=e_t$ says that the evolution attenuates nothing.

### What Trace Preservation Does Not Say

Trace preservation of a one-Kraus channel is not the same as trace preservation of an instrument. An instrument satisfies $\sum_y\tilde K_y^{*}\tilde K_y=e_t$; a single term need not. A term with $\tilde H_{\mathrm{pos}}\neq e_t$ is a legitimate outcome, and its effect is not the identity. The one-Kraus statement applies only when there is one term and no other outcome. The dephasing channel of §*Channels and Kraus Rank* is the witness: one Kraus operator is a scalar multiple of the identity, with $\tilde U_{\mathrm{p}}=e_t$, and the channel is still irreversible because there is a second term.

## Effects as Squares

### The Effect Is the Conjugated Square

The effect of the outcome is

$$
\boxed{\;\tilde E=\tilde K^{*}\tilde K=\tilde U_{\mathrm{p}}^{*}\tilde H_{\mathrm{pos}}^{2}\tilde U_{\mathrm{p}}\;}.
$$

The eigenvalues of $\tilde E$ are $\sigma_i^{2}$, the squares of the singular values of $\tilde K$ and the eigenvalues of $\tilde H_{\mathrm{pos}}^{2}$. The effect is positive, and $\tilde E\leq e_t$ exactly when every $\sigma_i\leq1$; for an instrument the resolution $\sum_y\tilde E_y=e_t$ forces each $\sigma_i\leq1$.

The formula is not $\tilde E=\tilde H_{\mathrm{pos}}^{2}$ in general. The two agree only when $\tilde U_{\mathrm{p}}$ commutes with $\tilde H_{\mathrm{pos}}$, and in particular when $\tilde U_{\mathrm{p}}$ is a function of $\tilde H_{\mathrm{pos}}$. On the cone they need not agree at all: the effect and the squared strength can sit on different lines, with $\tilde U_{\mathrm{p}}$ carrying one to the other.

### The Effect Does Not Determine the Split

The effect determines the singular values, not the factorization. If $\tilde W$ is unitary and $\tilde K'=\tilde W\tilde K$, then

$$
\tilde K'^{*}\tilde K'=\tilde K^{*}\tilde K=\tilde E,
\qquad
\tilde H_{\mathrm{pos}}'=\tilde W\tilde H_{\mathrm{pos}}\tilde W^{*},
\qquad
\tilde U_{\mathrm{p}}'=\tilde W\tilde U_{\mathrm{p}}.
$$

The same effect therefore admits different strengths and different backactions. The canonical choice $\tilde K=\sqrt{\tilde E}$ gives $\tilde H_{\mathrm{pos}}=\sqrt{\tilde E}$ and $\tilde U_{\mathrm{p}}$ the projection onto $\operatorname{ran}\tilde E$; a physical Kraus operator need not be that choice. The polar decomposition is a decomposition of the amplitude, not a decomposition of the effect. This is the precise sense in which the effect is the probability functional and the amplitude carries more.

### A Null Example Where the Two Differ

Take the non-Hermitian null element

$$
\tilde K=i\vec e_x-\vec e_y,\qquad \langle\tilde K\rangle_{\natural}=i^{2}+(-1)^{2}=0.
$$

Its singular values are $2$ and $0$. The generalized pairing gives

$$
\tilde H_{\mathrm{pos}}=e_t+i\vec e_z=2\tilde\Pi_{\vec e_z},\qquad
\tilde U_{\mathrm{p}}=\tfrac{i}{2}\vec e_x-\tfrac12\vec e_y=\tfrac12\tilde K .
$$

The effect and the squared strength are

$$
\boxed{\;\tilde E=\tilde K^{*}\tilde K=4\tilde\Pi_{-\vec e_z}=2e_t-2i\vec e_z,
\qquad
\tilde H_{\mathrm{pos}}^{2}=4\tilde\Pi_{\vec e_z}=2e_t+2i\vec e_z\;} .
$$

They are different rank-one elements, on opposite Bloch points. The partial isometry carries the initial line $\tilde\Pi_{-\vec e_z}$ to the final line $\tilde\Pi_{\vec e_z}$, and the effect sees the initial line while the squared strength sees the final one. The example is exact; the identities $\tilde K=\tilde H_{\mathrm{pos}}\tilde U_{\mathrm{p}}$ and $\tilde E=\tilde U_{\mathrm{p}}^{*}\tilde H_{\mathrm{pos}}^{2}\tilde U_{\mathrm{p}}$ hold with no residual.

## The Three Strata

The four cases of the amplitude are the four rows of the table. The rank is the matrix rank of $\mathsf M_2(\tilde K)$; the projections are $\tilde\Pi_{\mathrm i}=\tilde U_{\mathrm{p}}^{*}\tilde U_{\mathrm{p}}$ and $\tilde\Pi_{\mathrm f}=\tilde U_{\mathrm{p}}\tilde U_{\mathrm{p}}^{*}$.

| stratum | $\operatorname{rank}\tilde K$ | $\tilde H_{\mathrm{pos}}$ | $\tilde U_{\mathrm{p}}$ | effect $\tilde E$ | example |
|---|---|---|---|---|---|
| unitary | $2$ | $e_t$ | $\tilde K$, unitary | $e_t$ | reversible one-Kraus channel |
| invertible, not unitary | $2$ | positive definite, $\neq e_t$ | unitary, $\neq\tilde K$ | positive definite, $<e_t$ | unsharp outcome |
| null, rank one | $1$ | $\sigma\tilde\Pi_{\mathrm f}$, $\sigma>0$ | rank-one partial isometry | $\sigma^{2}\tilde\Pi_{\mathrm i}$ | sharp ($\sigma=1$) or soft ($\sigma<1$) outcome |
| zero | $0$ | $0$ | $0$ | $0$ | null outcome |

## Sharp Measurement on the Null Cone

Take the rank-one Hermitian idempotent

$$
\tilde K=\tilde\Pi=\tfrac12\left(e_t+i\vec u\right),\qquad \vec u^{2}=-e_t.
$$

It satisfies $\tilde\Pi^{2}=\tilde\Pi=\tilde\Pi^{*}$ and $\langle\tilde\Pi\rangle_{\natural}=0$, so it is a zero divisor. Its polar factors are $\tilde H_{\mathrm{pos}}=\tilde U_{\mathrm{p}}=\tilde\Pi$, because $\tilde\Pi\tilde\Pi^{*}=\tilde\Pi$ and $\tilde\Pi^{+}=\tilde\Pi$. The effect is $\tilde E=\tilde\Pi$, and the two projections of the partial isometry are both $\tilde\Pi$. The outcome probability for a state $\tilde{Ϛ}$ is $p=\operatorname{Tr}(\tilde{Ϛ}\tilde\Pi)$, and the post-measurement state is $\tilde\Pi$.

The sharp outcome therefore sits exactly on the null cone, and its amplitude is a partial isometry, not a unitary. The "collapse" is the rank drop: the amplitude has rank one, the effect has rank one, and the post-measurement state is a pure state. The mathematical pairing that covers it is the generalized Cartan pairing; the Cartan pairing on $\langle\tilde K\rangle_{\natural}\neq0$ does not.

A projective measurement of a two-level system is the pair $\tilde\Pi_1,\tilde\Pi_2$ with $\tilde\Pi_1+\tilde\Pi_2=e_t$. Both Kraus operators are null; both effects are idempotent; the instrument is sharp. The resolution of the identity is the statement $\tilde\Pi_1+\tilde\Pi_2=e_t$, not a statement about either factor alone.

## Weak Measurement and Backaction

### The Invertible Outcome

An outcome is **unsharp** when $\tilde K$ is invertible. Then $\tilde H_{\mathrm{pos}}$ is positive definite, $\tilde U_{\mathrm{p}}$ is unitary, and the effect is positive definite. The post-measurement state is

$$
\tilde{Ϛ}_y=\frac{\tilde H_{\mathrm{pos}}\tilde U_{\mathrm{p}}\tilde{Ϛ}\tilde U_{\mathrm{p}}^{*}\tilde H_{\mathrm{pos}}}{p_y}.
$$

The order is fixed by the word: the unitary factor acts first, then the positive filter. The backaction is the rotation $\tilde U_{\mathrm{p}}$; the filter is the strength $\tilde H_{\mathrm{pos}}$ in the output basis. A weak measurement is the regime in which the $\sigma_i$ are close to $1$; the outcome then disturbs the state only slightly, and the effect is close to $e_t$.

### A Worked Unsharp Outcome

Take the strength $\tilde H_0=\tfrac{1+\eta}{2}e_t+\tfrac{\eta-1}{2}i\vec e_z=0.8e_t-0.2i\vec e_z$ with $\eta=0.6$ and eigenvalues $0.6$ and $1$, and the unitary backaction $\tilde U_0=\cos\tfrac{\theta}{2}e_t+\sin\tfrac{\theta}{2}\vec e_x=0.866025404e_t+0.5\vec e_x$ with $\theta=\pi/3$. Set $\tilde K=\tilde U_0\tilde H_0$. The polar factors are

$$
\tilde H_{\mathrm{pos}}=\tilde U_0\tilde H_0\tilde U_0^{*}=0.8e_t+0.173205081i\vec e_y-0.1i\vec e_z,\qquad
\tilde U_{\mathrm{p}}=\tilde U_0,
$$

and the amplitude is $\tilde K=0.692820323e_t+0.4\vec e_x+0.1i\vec e_y-0.173205081i\vec e_z$.
The effect is

$$
\boxed{\;\tilde E=\tilde K^{*}\tilde K=\tilde H_0^{2}=0.68e_t-0.32i\vec e_z=0.36\tilde\Pi_{\vec e_z}+\tilde\Pi_{-\vec e_z}\;},
$$

with eigenvalues $0.36$ and $1$. The outcome is unsharp: the effect is full rank, no direction is annihilated, and the backaction is a rotation by $60^{\circ}$ about $\vec e_x$. The strength is the pair $\{0.6,1\}$; the effect sees its squares. The complement $e_t-\tilde E=0.64\tilde\Pi_{\vec e_z}$ is rank one, with Kraus operator $0.8\tilde\Pi_{\vec e_z}$, which is null. The two outcomes resolve the identity: one is unsharp and invertible, the other is rank one and on the cone. The example shows the boundary in a single instrument.

## Channels and Kraus Rank

### The Sum of the Terms

A channel is a sum of terms, and the polar decomposition applies to each term separately:

$$
\Phi(\tilde{Ϛ})=\sum_l\tilde K_l\tilde{Ϛ}\tilde K_l^{*}
=\sum_l\tilde H_{\mathrm{pos},l}\tilde U_{\mathrm{p},l}\tilde{Ϛ}\tilde U_{\mathrm{p},l}^{*}\tilde H_{\mathrm{pos},l}.
$$

Trace preservation is

$$
\sum_l\tilde U_{\mathrm{p},l}^{*}\tilde H_{\mathrm{pos},l}^{2}\tilde U_{\mathrm{p},l}=e_t.
$$

The polar decomposition of the sum is not the sum of the polar decompositions. The object decomposed here is each Kraus operator; the channel is a completely positive map, and its own polar decomposition as an operator on the Hilbert–Schmidt space is a different statement, not made here.

### The Dichotomy Is the Minimal Number of Terms

A channel is reversible exactly when it has a one-term Kraus representation, and then the term is unitary. It is irreversible exactly when its minimal Kraus rank is at least two. The value of one $\tilde H_{\mathrm{pos}}$ does not decide the channel: a term can have $\tilde H_{\mathrm{pos}}=e_t$ and the channel can still be irreversible, and a term can have $\tilde H_{\mathrm{pos}}\neq e_t$ and the channel can still be reversible if the representation is non-minimal and the map has a one-term form.

### Dephasing as the Counterexample

The dephasing channel of *Quantum Channels and the Reversible/Irreversible Dichotomy* leaves the populations and scales the coherences by $1-p$. In the pointer basis it is

$$
\Phi_p(\tilde{Ϛ})=(1-p)\tilde{Ϛ}+p\left(\tilde\Pi_1\tilde{Ϛ}\tilde\Pi_1+\tilde\Pi_2\tilde{Ϛ}\tilde\Pi_2\right).
$$

The companion article displays the three-term representation $\tilde K_0=\sqrt{1-p}e_t$, $\tilde K_{1,2}=\sqrt p\tilde\Pi_{1,2}$. That representation is not minimal: because $e_t=\tilde\Pi_1+\tilde\Pi_2$, the same channel has the two-term form

$$
\tilde K_0=\sqrt{1-\tfrac p2}\,e_t,\qquad
\tilde K_1=\sqrt{\tfrac p2}\,Z,\qquad Z=i\vec e_z,
$$

with $Z$ unitary and $Z^{2}=e_t$. For $0<p<1$ both terms have scalar strength, $\tilde H_{\mathrm{pos},0}=\sqrt{1-p/2}e_t$ and $\tilde H_{\mathrm{pos},1}=\sqrt{p/2}e_t$, and both have unitary backaction, $\tilde U_{\mathrm{p},0}=e_t$ and $\tilde U_{\mathrm{p},1}=Z$. The channel is nevertheless irreversible for every $p>0$, because its minimal Kraus rank is two. At $p=0$ the second term vanishes and the channel is the identity; at $p=1$ the two terms are $e_t/\sqrt2$ and $Z/\sqrt2$ and the channel is fully dephasing.

The example states the article's negative thesis. The reversibility of a channel is not the triviality of a single strength and not the unitarity of a single backaction. It is the minimal number of terms in the sum.

## Physical Interpretation

The polar form separates two questions that the outcome probability answers together. The strength answers **how much** the outcome responds to each direction; the backaction answers **which way** the state is carried when the outcome occurs. The probability is the trace of the effect, so it sees only the squares of the strengths. The post-measurement state sees the backaction as well. Two amplitudes with the same effect but different $\tilde U_{\mathrm{p}}$ are indistinguishable in their statistics and distinguishable in their aftermath; the polar form is what makes the difference explicit.

The unitary stratum is the case of no filter. The outcome rotates the state and does not weight it; if it is the whole channel, the process is reversible and its generator is a Hamiltonian in $\mathbb{M}_-$. The invertible stratum is the unsharp outcome: the state is rotated and then weighted, no direction is annihilated, and the effect lies strictly inside the effect body. The null stratum is the sharp or soft rank-one outcome: the amplitude projects onto a line, the effect is rank one, and the post-measurement state is pure. The three strata are the three physical regimes of a measurement outcome, read from the rank of the amplitude.

The null cone is the **measurement boundary** in a precise but limited sense. It is the locus where the amplitude loses rank, the boundary of the positive cone, and the boundary between the invertible and the rank-one outcomes. It is not a boundary in space or time, and it is not a dynamical condition that says when a measurement occurs. The algebra classifies the amplitude; it does not select it. The companion article *The Measurement Problem in Algebraic Form* owns that distinction, and this article does not improve on it.

The channel-level statement is the correction that the polar programme makes to a natural but false reading. It is tempting to say that a process is reversible when its positive factor is trivial, or that a process is a measurement when its backaction is a projector. Neither is a statement about a channel. A channel is a sum, and its reversibility is the minimal number of terms. The dephasing channel is the counterexample: two scalar strengths and two unitary backactions, and an irreversible map.

## What This Does Not Claim

- It does not prove the generalized polar decomposition. The existence, uniqueness and projection conditions are owned by the mathematical article and are cited.
- It does not classify channels by the polar factor of one Kraus operator. The channel dichotomy is the minimal Kraus rank; the polar factor is a property of a term.
- It does not identify $\tilde H_{\mathrm{pos}}$ with a physical field or $\tilde U_{\mathrm{p}}$ with a force. The strength and backaction are readings of the amplitude, not new dynamics.
- It does not claim that the null cone is a physical boundary in space or time. It is the singular locus of the algebra.
- It does not resolve the measurement problem. It restates the classification of the acting element; the selection of the outcome and of the unitary-versus-idempotent case is not in the algebra.
- It does not treat continuous POVMs, non-completely-positive maps, or the polar decomposition of a channel as a superoperator.

## Summary

### Main Results

| item | result |
|---|---|
| polar form | $\tilde K=\tilde H_{\mathrm{pos}}\tilde U_{\mathrm{p}}$, $\tilde H_{\mathrm{pos}}=\sqrt{\tilde K\tilde K^{*}}$, $\tilde U_{\mathrm{p}}=\tilde H_{\mathrm{pos}}^{+}\tilde K$ |
| strength | the singular values $\sigma_i$, the eigenvalues of $\tilde H_{\mathrm{pos}}$ |
| backaction | the partial isometry $\tilde U_{\mathrm{p}}$, unitary off the cone, rank one on it |
| effect | $\tilde E=\tilde K^{*}\tilde K=\tilde U_{\mathrm{p}}^{*}\tilde H_{\mathrm{pos}}^{2}\tilde U_{\mathrm{p}}$, eigenvalues $\sigma_i^{2}$ |
| one-Kraus channel | $\tilde K^{*}\tilde K=e_t$ iff $\tilde H_{\mathrm{pos}}=e_t$ and $\tilde U_{\mathrm{p}}=\tilde K$ unitary |
| sharp outcome | $\tilde K=\tilde\Pi$: $\tilde H_{\mathrm{pos}}=\tilde U_{\mathrm{p}}=\tilde\Pi$, $\tilde E=\tilde\Pi$, on the null cone |
| soft rank-one outcome | $\tilde K=\sigma\tilde\Pi$: $\tilde H_{\mathrm{pos}}=\sigma\tilde\Pi$, $\tilde U_{\mathrm{p}}=\tilde\Pi$, $\tilde E=\sigma^{2}\tilde\Pi$ |
| unsharp outcome | $\tilde K$ invertible: $\tilde H_{\mathrm{pos}}>0$, $\tilde U_{\mathrm{p}}$ unitary, $\tilde E>0$ |
| channel | $\sum_l\tilde U_{\mathrm{p},l}^{*}\tilde H_{\mathrm{pos},l}^{2}\tilde U_{\mathrm{p},l}=e_t$; reversible iff minimal Kraus rank one |
| dephasing | two scalar strengths and two unitary backactions, minimal Kraus rank two, irreversible for $p>0$ |

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | quaternion basis, $\vec e_k^{2}=-e_t$ |
| $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$ | state, $\lvert\vec r\rvert\leq1$ |
| $\tilde K$, $\tilde K_y$, $\tilde K_l$ | Kraus operator, one outcome, one term of a channel |
| $\tilde H_{\mathrm{pos}}=\sqrt{\tilde K\tilde K^{*}}$ | positive (strength) factor of the Kraus operator |
| $\tilde U_{\mathrm{p}}=\tilde H_{\mathrm{pos}}^{+}\tilde K$ | partial-isometry (backaction) factor |
| $\tilde H_{\mathrm{pos}}^{+}$ | Moore–Penrose inverse |
| $\tilde E=\tilde K^{*}\tilde K=\tilde U_{\mathrm{p}}^{*}\tilde H_{\mathrm{pos}}^{2}\tilde U_{\mathrm{p}}$ | effect of the outcome |
| $\tilde\Pi=\tfrac12(e_t+i\vec u)$ | rank-one Hermitian idempotent, $\vec u$ a real unit vector |
| $\tilde\Pi_{\mathrm i}=\tilde U_{\mathrm{p}}^{*}\tilde U_{\mathrm{p}}$, $\tilde\Pi_{\mathrm f}=\tilde U_{\mathrm{p}}\tilde U_{\mathrm{p}}^{*}$ | initial and final projections of $\tilde U_{\mathrm{p}}$ |
| $\sigma_i$ | singular values of $\tilde K$, eigenvalues of $\tilde H_{\mathrm{pos}}$ |
| $\Phi(\tilde{Ϛ})=\sum_l\tilde K_l\tilde{Ϛ}\tilde K_l^{*}$ | channel |
| $Z=i\vec e_z$ | the unitary Pauli-$z$ element, $Z^{2}=e_t$ |
| $\operatorname{Tr}\tilde Q=2\operatorname{Sc}\tilde Q=2Q_t$ | trace convention |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | biquaternion norm (determinant) |

## Further Reading

- [The Generalized Polar Decomposition of a Biquaternion: Partial Isometries and the Null Cone](../articles_maths/the-general-polar-decomposition-of-a-biquaternion-partial-isometries-and-the-null-cone.html), for the theorem, its uniqueness with the initial and final projections, and the rank-one case.
- [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](../articles_maths/the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), for the pairing off the null cone and the unitary factor.
- [Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint](../articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.html), for the positive cone and the Hermitian square root.
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the rank-one idempotents and the Bloch sphere.
- [Norm Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the null cone and its singular locus.
- [Quantum Channels and the Reversible/Irreversible Dichotomy](quantum-channels-and-the-reversible-irreversible-dichotomy.html), for the Kraus representation, the channel dichotomy, and the dephasing channel.
- [POVMs and the Positive Cone in Biquaternionic Form](povms-and-the-positive-cone-in-biquaternionic-form.html), for effects, the effect body, and the Born rule.
- [The Measurement Problem in Algebraic Form](the-measurement-problem-in-algebraic-form.html), for the selection problem and the unitary-versus-idempotent acting element.
- [Decoherence as Idempotent Projection](decoherence-as-idempotent-projection.html), for the dephasing channel and the pointer basis.
- [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html), for the state space and the measurement update.
- [The Born Rule from the Hermitian Form — Derivation and Comparison](the-born-rule-as-a-trace-formula-derivation-and-comparison.html), for the trace reading of the Born weight.
- K. Kraus, *States, Effects, and Operations* (Springer, 1983), for the original formulation of completely positive maps and instruments.
- [The Cartan Pairing, the Amplitude and the Operator-to-State Map](the-cartan-pairing-amplitude-and-the-operator-to-state-map.html), for the input-free operator-to-state map and the purity table that the three outcome strata follow.
- M.-D. Choi, "Completely positive linear maps on complex matrices," *Linear Algebra and its Applications* **10** (1975) 285–290, for the Choi matrix and the minimal Kraus rank.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Kraus representation, the polar decomposition of operators, and generalized measurements.
