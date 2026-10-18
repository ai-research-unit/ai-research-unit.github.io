# __Coarse-Graining and the Biquaternion Entropy Functional__

## Introduction

A **coarse-graining** is a description that discards fine-grained distinctions. The state of a physical system is replaced by a record of which cell of a partition it occupies, and the information the record carries is measured by the entropy of the induced cell distribution. Coarse-graining is the operation that makes entropy increase: the fine-grained descriptions of classical mechanics are conserved by the reversible flow, while the coarse-grained ones are not, and the difference between the two is the content of the second law.

This article develops the coarse-grained entropy functional of the informational sector $\mathbb{M}_+$ of the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. The two ingredients are both already in the framework. The **states** of the sector are the positive trace-one elements $\tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r)$ of $\mathbb{M}_+$, the Bloch ball; its **pure states** are the idempotents, and they sit on the null cone of the biquaternion norm, which is the zero-divisor cone of the algebra. The **coarse-grainings** are the conditional expectations of the sector: the completely positive, trace-preserving, idempotent maps onto a commutative subalgebra, of which the fully dephasing channel of the companion article *Quantum Channels and the Reversible/Irreversible Dichotomy* is the canonical example. The entropy functional is the algebra's own logarithm applied to a state and paired with it through the trace:

$$
\mathcal{S}(\tilde{Ϛ}) = -2\,\mathrm{Sc}\!\left(\tilde{Ϛ}\log\tilde{Ϛ}\right).
$$

The article's central result is that this functional depends on the state **only through its biquaternion norm**. With $\langle\tilde{Ϛ}\rangle_{\natural} = \tilde{Ϛ}\tilde{Ϛ}^{\natural} = \tfrac{1}{4}(1-|\vec r|^2)e_t$, one has $|\vec r| = \sqrt{1 - 4\,\mathrm{Sc}\,\langle\tilde{Ϛ}\rangle_{\natural}}$, and therefore

$$
\mathcal{S}(\tilde{Ϛ}) = h\!\left(\sqrt{1 - 4\,\mathrm{Sc}\,\langle\tilde{Ϛ}\rangle_{\natural}}\right),
$$

where $h$ is the binary entropy function. The entropy vanishes exactly on the null cone, that is, exactly on the zero divisors; it is maximal at the maximally mixed state; and it measures the depth of the state inside the future cone of the biquaternion norm. The functional and the biquaternion norm are thus the same information, read as a number and as a quadratic form.

Two functionals appear below and must be kept apart, because the whole subject turns on the difference. The **spectral** value $\mathcal{S}(\tilde{Ϛ})$ is a property of the state and is invariant under reversible rotor flow; it is the fine-grained reference. The **coarse-grained** value $\mathcal{S}(\Phi(\tilde{Ϛ}))$ is the entropy of the image of the state under a coarse-graining $\Phi$, and it is this second number that increases under a coarse-graining. The second law, in this language, is the statement that a coarse-graining is a contraction of the Bloch ball, so that the entropy of the image is never less than the entropy of the state. The two are reconciled by the fact that the fine-grained value is the *minimum* over all preparations of the state, and hence the least coarse description the state admits.

The treatment is **classical**. The entropy here is the Shannon entropy of a coarse description, and the functional is the classical one throughout. The functional $\mathcal{S}$ coincides numerically, on the matrix representative of $\tilde{Ϛ}$, with the von Neumann entropy of that $2\times 2$ density matrix, and the reader should not be misled by the coincidence: the von Neumann entropy as such, and the entropies attached to POVMs and to entanglement, belong to the informational subcategory of the sibling quantum category, where the companion article *Von Neumann Entropy and the Biquaternion Norm* develops them, and they are not developed here. Where the quantum interpretation is used, it is used as a bound, and it is identified as such.

The probabilities the functional is built from are themselves trace pairings. The weights $\lambda_\pm$ of the spectral decomposition are $\lambda_\pm = \mathrm{Tr}(\tilde\Pi_{1,2}(\vec u_r)\tilde{Ϛ})$, and the companion article *The Born Rule as a Trace Formula — Derivation and Comparison* derives the form of that pairing and fixes the objects it relates; this article takes the form as given and uses it only to read the state's own two-outcome distribution.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_k^2 = -e_t$; the scalar imaginary is $i$, central in $\mathbb{B}$; the two four-dimensional real subspaces are the anti-Hermitian material sector $\mathbb{M}_-$ and the Hermitian informational sector $\mathbb{M}_+$, with $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$; the trace is $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$, normalised by $\mathrm{Tr}(e_t) = 2$; and the trace formula for a state and an observable is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H) = 2\langle\tilde{P},\tilde{H}\rangle$.

## The State Space of the Informational Sector

A state of the informational sector is an element

$$
\tilde{Ϛ} = \tfrac{1}{2}\left(e_t + i\,\vec r\right), \qquad \vec r = r_1 \vec e_x + r_2 \vec e_y + r_3 \vec e_z, \quad \vec r \in \mathbb{R}^3,
$$

of the Hermitian subspace $\mathbb{M}_+$. The scalar part of $\tilde{Ϛ}$ is real, its vector part is purely imaginary, and its trace is

$$
\mathrm{Tr}(\tilde{Ϛ}) = 2\,\mathrm{Sc}(\tilde{Ϛ}) = 1 .
$$

The state is positive precisely when the Bloch vector lies in the closed unit ball,

$$
\tilde{Ϛ} \ge 0 \quad \Longleftrightarrow \quad |\vec r| \le 1 ,
$$

so that the states form the **Bloch ball**; the pure states are its boundary sphere. A pure state is an idempotent,

$$
\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}\left(e_t \pm i\,\vec u\right), \qquad |\vec u| = 1, \qquad \tilde\Pi_{1,2}^2 = \tilde\Pi_{1,2} ,
$$

and conversely every idempotent of $\mathbb{M}_+$ has this form. The complementary idempotents are orthogonal and complete, $\tilde\Pi_1\tilde\Pi_2 = 0$ and $\tilde\Pi_1 + \tilde\Pi_2 = e_t$.

### The Biquaternion Norm of a State

The biquaternion norm of the algebra is $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$. On the state it evaluates to a scalar multiple of the identity:

$$
\langle\tilde{Ϛ}\rangle_{\natural} = \tilde{Ϛ}\tilde{Ϛ}^{\natural} = \left(\tfrac{1}{2}\right)^2 + \left(\tfrac{i r_1}{2}\right)^2 + \left(\tfrac{i r_2}{2}\right)^2 + \left(\tfrac{i r_3}{2}\right)^2 = \tfrac{1}{4}\left(1 - |\vec r|^2\right)e_t .
$$

This single identity carries the geometry of the state space. The biquaternion norm is **positive** in the interior of the Bloch ball, **zero** on its boundary, and **negative** outside it, so that the state space is exactly the trace-one slice of the future cone of the biquaternion norm. The boundary of the state space is the **zero-divisor cone**: the pure states are the elements of $\mathbb{M}_+$ that fail to be invertible. The biquaternion norm therefore measures how far inside the cone a state lies, and its vanishing is the algebraic statement of purity.

Two further identities follow from the multiplication table and are used throughout. Squaring the state gives

$$
\tilde{Ϛ}^2 = \tfrac{1}{4}\left(\left(1 + |\vec r|^2\right)e_t + 2i\,\vec r\right),
$$

because $(i\vec r)^2 = -\vec r^2 = |\vec r|^2 e_t$ and $(i\vec r)$ commutes with the scalar; and therefore the **deviation from idempotency** is a pure scalar,

$$
\tilde{Ϛ}^2 - \tilde{Ϛ} = \tfrac{1}{4}\left(|\vec r|^2 - 1\right)e_t .
$$

Equivalently, the purity is

$$
\mathrm{Tr}\!\left(\tilde{Ϛ}^2\right) = \tfrac{1}{2}\left(1 + |\vec r|^2\right),
$$

so that purity and idempotency are the same condition, and the biquaternion norm, the deviation from idempotency, and the purity are three interpretations of the single number $|\vec r|^2$.

## The Entropy Functional

### Existence of the Logarithm

The entropy functional is built from the algebra's logarithm. The logarithm of a biquaternion is defined as the inverse of the exponential, and the companion article *Biquaternion Elementary Functions* establishes the relevant fact: the logarithm exists exactly on the group of units,

$$
\mathbb{B}^\times = \left\{\tilde{Q} \in \mathbb{B} : \langle\tilde{Q}\rangle_{\natural} \neq 0\right\},
$$

and on no larger set. The proof is the polar decomposition $\tilde{Q} = R\exp(\Theta\vec u)$ with $R = \sqrt{\langle\tilde{Q}\rangle_{\natural}}$, which fails precisely when $\langle\tilde{Q}\rangle_{\natural} = 0$.

For the state this condition is transparent. A state in the interior of the Bloch ball has

$$
\langle\tilde{Ϛ}\rangle_{\natural} = \tfrac{1}{4}\left(1 - |\vec r|^2\right)e_t \neq 0 \qquad (|\vec r| < 1),
$$

so it is a unit and its logarithm exists. A **pure** state has $\langle\tilde{Ϛ}\rangle_{\natural} = 0$: it is a zero divisor, the logarithm does not exist there, and the entropy is defined on the boundary by continuity. The locus where the entropy functional is analytically singular is exactly the locus of purity, and that coincidence is the geometric content of the whole subject.

### Definition from the Spectral Decomposition

The logarithm of a state is evaluated with the idempotents. Writing $\vec u_r = \vec r/|\vec r|$ for a state with $\vec r \neq 0$, the spectral decomposition of the state in its own basis is

$$
\tilde{Ϛ} = \lambda_+\, \tilde\Pi_1(\vec u_r) + \lambda_-\, \tilde\Pi_2(\vec u_r), \qquad
\lambda_\pm = \tfrac{1}{2}\left(1 \pm |\vec r|\right),
$$

as one verifies directly from the definitions of the idempotents. The eigenvalues $\lambda_\pm$ are the classical probabilities of the two pointer outcomes in the eigenbasis, they are non-negative for $|\vec r| \le 1$, and they sum to one. The functional calculus of the algebra then gives

$$
\log\tilde{Ϛ} = \left(\log\lambda_+\right)\tilde\Pi_1(\vec u_r) + \left(\log\lambda_-\right)\tilde\Pi_2(\vec u_r),
$$

which is the principal branch on the positive part of $\mathbb{M}_+$; on the general algebra the logarithm is multivalued, and positivity of the state removes the ambiguity by fixing the branch. Multiplying and taking the scalar part, using $\mathrm{Sc}(\tilde\Pi_{1,2}) = \tfrac{1}{2}$, gives $\mathrm{Sc}(\tilde{Ϛ}\log\tilde{Ϛ}) = \tfrac{1}{2}(\lambda_+\log\lambda_+ + \lambda_-\log\lambda_-)$, and therefore

$$
\mathcal{S}(\tilde{Ϛ}) = -2\,\mathrm{Sc}\!\left(\tilde{Ϛ}\log\tilde{Ϛ}\right)
= -\lambda_+\log\lambda_+ - \lambda_-\log\lambda_- .
$$

This is the **biquaternion entropy functional**. It is a real number, it is computed from the algebra's own product, logarithm and trace, and it is the classical Shannon entropy of the two-outcome distribution $(\lambda_+,\lambda_-)$ that the state induces in its eigenbasis. Written out in the Bloch radius it is the binary entropy function,

$$
\mathcal{S}(\tilde{Ϛ}) = h(|\vec r|), \qquad
h(x) = -\frac{1+x}{2}\log\frac{1+x}{2} - \frac{1-x}{2}\log\frac{1-x}{2},
$$

with the boundary values $h(0) = \log 2$ and $h(1) = 0$.

The evaluation is stable under the same computation in the full algebra. For the interior state obtained by superposing two orthogonal pure states with equal weight, $\tilde{Ϛ} = \tfrac{1}{2}\left(\tilde\Pi_1(\vec e_x) + \tilde\Pi_1(\vec e_y)\right)$, one has $\vec r = \tfrac{1}{2}(\vec e_x + \vec e_y)$, $|\vec r| = 1/\sqrt{2}$, and the two routes agree:

$$
\mathcal{S} = -2\,\mathrm{Sc}\!\left(\tilde{Ϛ}\log\tilde{Ϛ}\right) = 0.4164955307\ldots,
$$

matching $h(1/\sqrt{2})$ to machine precision. The verification is on this superposition, that is, on an interior (mixed) state, where the logarithm is nonsingular and the two-outcome distribution is nontrivial.

### Elementary Properties

Three properties follow immediately and are worth recording, because they are the properties the coarse-grained entropy inherits.

**Range.** Since $0 \le \lambda_\pm \le 1$ with $\lambda_+ + \lambda_- = 1$, the functional is non-negative and bounded above:

$$
0 \le \mathcal{S}(\tilde{Ϛ}) \le \log 2 ,
$$

with the lower bound attained exactly on the pure states, $|\vec r| = 1$, and the upper bound exactly at the maximally mixed state, $\vec r = 0$, where $\tilde{Ϛ} = \tfrac{1}{2}e_t$ and $\lambda_+ = \lambda_- = \tfrac{1}{2}$.

**Symmetry.** The functional is unchanged by the exchange $\lambda_+ \leftrightarrow \lambda_-$, equivalently by $\vec r \mapsto -\vec r$; both are the same classical distribution. It is a function of the radius alone, so it is invariant under every rotation of the Bloch ball.

**Concavity.** The binary entropy is concave in its argument, so $\mathcal{S}$ is concave along the Bloch radius: for a mixture $\tilde{Ϛ} = p\tilde{Ϛ}_1 + (1-p)\tilde{Ϛ}_2$,

$$
\mathcal{S}\!\left(p\tilde{Ϛ}_1 + (1-p)\tilde{Ϛ}_2\right)
\;\ge\; p\,\mathcal{S}\!\left(\tilde{Ϛ}_1\right) + (1-p)\,\mathcal{S}\!\left(\tilde{Ϛ}_2\right),
$$

a mixture being never less entropic than the average of its constituents. This is the elementary form of the second law for the sector. The comparison is against the **average** and not against each constituent separately: mixing the maximally mixed state with a pure state in equal parts gives $\mathcal{S} = h(\tfrac{1}{2}) = 0.5623351$, which is below the $\log 2 = 0.6931472$ of the maximally mixed state alone, so mixing can lower the entropy of a particular constituent even though it can never lower it below the mean.

The functional is measured in nats. Multiplying by the Boltzmann constant, $\mathcal{S}_{\rm th} = k_B\,\mathcal{S}$, gives a thermodynamic entropy; the algebra supplies the dimensionless information content, and the unit is a convention of thermodynamics rather than of the algebra.

## The Entropy Is a Function of the Biquaternion Norm

The biquaternion norm of the state and the entropy of the state are not independent quantities. The biquaternion norm gives $|\vec r|$ directly, and the entropy is a function of $|\vec r|$; composing the two eliminates the Bloch vector and leaves a function of the biquaternion norm alone.

Inverting $\langle\tilde{Ϛ}\rangle_{\natural} = \tfrac{1}{4}(1-|\vec r|^2)e_t$ gives

$$
|\vec r| = \sqrt{1 - 4\,\mathrm{Sc}\,\langle\tilde{Ϛ}\rangle_{\natural}},
$$

and substituting into $\mathcal{S} = h(|\vec r|)$ gives the central identity of the article:

$$
\boxed{\;\mathcal{S}(\tilde{Ϛ}) = h\!\left(\sqrt{1 - 4\,\mathrm{Sc}\,\langle\tilde{Ϛ}\rangle_{\natural}}\right).\;}
$$

The identity says that **the entropy of a state of the informational sector is a function of its biquaternion norm and of nothing else**. The biquaternion norm is the quantitatively meaningful invariant of the algebra; the entropy is a monotone reparametrisation of it. Three consequences are immediate, and they are the reason the identity is worth isolating.

First, the entropy vanishes exactly where the biquaternion norm vanishes. The condition $\mathcal{S}(\tilde{Ϛ}) = 0$ is $|\vec r| = 1$, which is $\langle\tilde{Ϛ}\rangle_{\natural} = 0$, which is the statement that $\tilde{Ϛ}$ is a zero divisor. **Zero entropy and the zero-divisor cone are the same locus.** The pure states are the informationless states, and the algebraic reason is that they are the non-invertible ones.

Second, the entropy is a strictly increasing function of the biquaternion norm on the positive cone. As the state moves inward from the boundary, $|\vec r|$ falls, $\langle\cdot\rangle_{\natural}$ rises from zero to its maximum $\tfrac{1}{4}e_t$ at the centre, and the entropy rises from zero to $\log 2$. Differentiating the boxed identity confirms the direction, $\partial\mathcal{S}/\partial\,\mathrm{Sc}\,N = 2\,\mathrm{artanh}\,|\vec r|/|\vec r| > 0$. The biquaternion norm is therefore a measure of **depth inside the cone**, and the entropy is that depth expressed in information units.

Third, the entropy is invariant under every operation that preserves the biquaternion norm. In particular, it is invariant under the rotor conjugation of a reversible flow, which is the subject of a later section.

The same identity holds for a coarse-grained state, since a coarse-grained state is a state. If $\Phi$ is a coarse-graining and $\tilde{Ϛ}_\Phi = \Phi(\tilde{Ϛ})$ is its image, then

$$
\mathcal{S}(\tilde{Ϛ}_\Phi) = h\!\left(\sqrt{1 - 4\,\mathrm{Sc}\,\langle\tilde{Ϛ}_\Phi\rangle_{\natural}}\right),
$$

so the whole information content of the coarse description is likewise carried by one scalar read from the biquaternion norm. This is what makes the coarse-grained entropy tractable: the second law for the sector reduces to a statement about the biquaternion norm of the image.

## Coarse-Graining on the Informational Sector

### What a Coarse-Graining Is

A coarse-graining is a description that remembers less. In the language of the sector it is a map

$$
\Phi : \mathbb{M}_+ \longrightarrow \mathbb{M}_+, \qquad \tilde{Ϛ} \longmapsto \Phi(\tilde{Ϛ}),
$$

subject to four conditions, each of which has an operational interpretation.

- **Linearity.** $\Phi(a\tilde{Ϛ}_1 + b\tilde{Ϛ}_2) = a\Phi(\tilde{Ϛ}_1) + b\Phi(\tilde{Ϛ}_2)$ for real $a,b$. A coarse-graining of a mixture is the mixture of the coarse-grainings, because the description acts on the preparation rather than on the individual outcome.
- **Positivity, in the strong form of complete positivity.** The map must remain positive when the sector is described jointly with any reference system, which is the condition that distinguishes a physical operation from a merely positive map, as the companion article *Quantum Channels and the Reversible/Irreversible Dichotomy* develops.
- **Trace preservation.** $\mathrm{Tr}(\Phi(\tilde{Ϛ})) = \mathrm{Tr}(\tilde{Ϛ})$, so that a state is sent to a state. Equivalently the dual map fixes the identity, $\Phi^{*}(e_t) = e_t$.
- **Idempotency and unitality.** $\Phi \circ \Phi = \Phi$ and $\Phi(e_t) = e_t$. The first says that coarse-graining twice is coarse-graining once: once a distinction has been discarded, it cannot be discarded again. The second says that the maximally mixed state is already as coarse as the description can be, so it is fixed.

A linear, completely positive, trace-preserving, idempotent, unital map is a **conditional expectation**: it projects the state space onto the states of a commutative subalgebra, the subalgebra of the quantities the description retains. For a single qubit the commutative subalgebras of $\mathbb{B}$ are two-dimensional, generated by a pair of orthogonal idempotents, and the conditional expectation onto the subalgebra generated by $\tilde\Pi_{1,2}(\vec u)$ is the fully dephasing map

$$
\Phi_{\vec u}(\tilde{Ϛ}) = \tilde\Pi_1(\vec u)\,\tilde{Ϛ}\,\tilde\Pi_1(\vec u) + \tilde\Pi_2(\vec u)\,\tilde{Ϛ}\,\tilde\Pi_2(\vec u) .
$$

This is the map of the companion article *Decoherence as Idempotent Projection* at $p = 1$. On the Bloch vector it acts by

$$
\vec r \longmapsto \left(\vec u\cdot\vec r\right)\vec u,
$$

annihilating the component transverse to the axis and retaining the component along it. The image is the **diameter** of the Bloch ball along $\vec u$: the classical bit that the description retains.

### The Binary Limitation

It must be said plainly that a coarse-graining of a single qubit is **binary**. The reason is algebraic and not a shortcoming of the treatment: $\mathbb{M}_+$ has only two orthogonal idempotents at a time, so a commutative subalgebra of $\mathbb{B}$ is at most two-dimensional, and a conditional expectation can retain at most one classical bit. A partition of the state space into three or more cells is not a conditional expectation of $\mathbb{B}$ and has no image in the sector; it requires the tensor product $\mathbb{B}^{\otimes n}$, whose states are treated in the sibling quantum category. What the single-qubit framework supplies is the *mechanism* of coarse-graining — the conditional expectation, its idempotency, its contraction of the ball — and the mechanism is what the entropy functional needs. The many-cell case is a matter of enlarging the algebra, not of changing the argument.

### The Coarse-Grained Entropy

With the coarse-graining fixed, the **coarse-grained entropy** is the entropy functional evaluated on the image,

$$
\mathcal{S}_{\rm cg}\!\left[\tilde{Ϛ};\Phi\right] = \mathcal{S}\!\left(\Phi(\tilde{Ϛ})\right) = -2\,\mathrm{Sc}\!\left(\Phi(\tilde{Ϛ})\log\Phi(\tilde{Ϛ})\right).
$$

For the pointer conditional expectation $\Phi_{\vec u}$, the image is $\tilde{Ϛ}_{\rm cg} = \tfrac{1}{2}(e_t + i(\vec u\cdot\vec r)\vec u)$, whose eigenvalues are

$$
p_\pm = \tfrac{1}{2}\left(1 \pm \vec u\cdot\vec r\right),
$$

the classical probabilities of the two pointer outcomes. The coarse-grained entropy is therefore the binary Shannon entropy

$$
\mathcal{S}_{\rm cg}\!\left[\tilde{Ϛ};\Phi_{\vec u}\right] = -p_+\log p_+ - p_-\log p_- = h\!\left(|\vec u\cdot\vec r|\right).
$$

This is the article's second main formula. It is the entropy of the classical record the coarse description keeps, and it is manifestly a function of the retained component of the Bloch vector alone.

## Monotonicity Under Coarse-Graining

### The Contraction

Coarse-graining cannot decrease the entropy. The proof has two steps, and both are standard.

The first step is that a unital, completely positive, trace-preserving map is a **contraction of the Bloch ball**. This is the Kadison–Schwarz inequality: for a unital completely positive map $\Phi$ one has $\Phi(\tilde{Q})^2 \leq \Phi(\tilde{Q}^2)$ in the matrix order. Taking the trace, and using trace preservation in the form $\mathrm{Tr}(\Phi(\tilde{Q}^2)) = \mathrm{Tr}(\tilde{Q}^2)$,

$$
\mathrm{Tr}\!\left(\Phi(\tilde{Q})^2\right) \le \mathrm{Tr}\!\left(\Phi(\tilde{Q}^2)\right) = \mathrm{Tr}\!\left(\tilde{Q}^2\right),
$$

and with $\tilde{Q} = \tilde{Ϛ}$ this is the purity inequality $\mathrm{Tr}(\Phi(\tilde{Ϛ})^2) \le \mathrm{Tr}(\tilde{Ϛ}^2)$. By the purity formula $\mathrm{Tr}(\tilde{Ϛ}^2) = \tfrac{1}{2}(1+|\vec r|^2)$ this is exactly

$$
|\vec r_\Phi| \le |\vec r| ,
$$

the statement that the map does not push a state outward. Equivalently, and in the form used for classical mechanics, every completely positive trace-preserving map is a contraction in the trace distance, and for a qubit the trace distance between two states is half the Euclidean distance between their Bloch vectors; the contraction of the metric and the contraction of the radius are the same statement.

The second step is the monotonicity of the entropy as a function of the radius, established above: $h$ is decreasing on $[0,1]$. Composing the two,

$$
\mathcal{S}\!\left(\Phi(\tilde{Ϛ})\right) = h\!\left(|\vec r_\Phi|\right) \ge h\!\left(|\vec r|\right) = \mathcal{S}\!\left(\tilde{Ϛ}\right),
$$

or, in one line,

$$
\boxed{\;\mathcal{S}\!\left(\Phi(\tilde{Ϛ})\right) \ge \mathcal{S}\!\left(\tilde{Ϛ}\right)\;}
$$

for every coarse-graining $\Phi$. **Coarse-graining never creates information; it can only fail to retain it.** The inequality is strict unless the state already lies in the image of $\Phi$, so a genuine coarse-graining strictly increases the entropy of every state outside its image.

The restriction to unital maps matters and is worth naming. A trace-preserving completely positive map that is *not* unital can lower the entropy of the state — that is refrigeration, which exports entropy to an environment — and such a map is not a coarse-graining in the sense used here. A coarse-graining discards distinctions *within* the description and keeps no ledger of what it exported; the environment, and with it the full accounting of the second law, is the subject of the companion articles *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form* and *Maxwell's Demon and the Informational Sector in Biquaternionic Form*.

### The Dephasing Family and Its Rate

The dephasing channel of the companion article *Decoherence as Idempotent Projection* interpolates between the identity and the coarse-graining. At strength $p \in [0,1]$ along $\vec u$ it acts by

$$
\vec r \longmapsto \vec r' = (1-p)\,\vec r + p\left(\vec u\cdot\vec r\right)\vec u,
$$

so that

$$
|\vec r'|^2 = \left(\vec u\cdot\vec r\right)^2 + (1-p)^2\left(|\vec r|^2 - \left(\vec u\cdot\vec r\right)^2\right) \le |\vec r|^2 ,
$$

with equality only at $p=0$, or for states already on the axis. The entropy therefore increases monotonically with $p$ from $\mathcal{S}(\tilde{Ϛ})$ to $h(|\vec u\cdot\vec r|)$, and it is maximised over the axis by the choice $\vec u \perp \vec r$, which discards the state entirely and returns $\log 2$.

In continuous time, with the transverse component decaying as $\exp(-\Gamma t)$ and the axial component fixed, the Bloch radius is

$$
r(t) = \sqrt{r_\parallel^2 + r_\perp(t)^2}, \qquad r_\perp(t) = \exp(-\Gamma t)r_\perp(0),
$$

where $r_\parallel = \vec u\cdot\vec r(0)$ is the fixed axial component and $r_\perp(t)$ is the **instantaneous** transverse component, and the entropy production rate is

$$
\frac{d}{dt}\mathcal{S}\!\left(\tilde{Ϛ}(t)\right)
= -\left(dr/dt\right)(t)\,\mathrm{artanh}\,r(t)
= \Gamma\,\frac{r_\perp(t)^2}{r(t)}\,\mathrm{artanh}\,r(t) \;\ge\; 0 ,
$$

using $\frac{dh}{dr}(r) = -\mathrm{artanh}\,r$ and $\left(dr/dt\right)(t) = -\Gamma r_\perp(t)^2/r(t)$. The rate is supported by the instantaneous transverse component, since it is $r_\perp(t)$ that carries the contraction; the initial component alone would overstate the rate at every $t > 0$.

The distinction matters as soon as the state has an axial part. Take $\vec r = (0.3, 0.4, 0.5)$ with $\vec u = \vec e_z$ and $\Gamma = 0.7$, so that $r_\parallel = 0.5$ and $r_\perp(0) = 0.5$: at $t = 1$ the finite-difference derivative is $0.0487233141$ and $\Gamma r_\perp(t)^2\,\mathrm{artanh}\,r(t)/r(t) = 0.0487233141$, whereas the same expression with $r_\perp(0)$ in place of $r_\perp(t)$ gives $0.1975827817$. On the state of the earlier checks, $\vec r = \tfrac{1}{2}(\vec e_x+\vec e_y)$ with $\vec u = \vec e_z$, the axial part vanishes, $r_\perp(t) = r(t)$, and at $t = 0$ the rate is $\Gamma\,r\,\mathrm{artanh}\,r = 0.4362576681$; that case cannot separate the two interpretations, which is why the state with $r_\parallel \neq 0$ is the decisive check.

The rate is positive and it vanishes when the transverse component vanishes. It also vanishes at the maximally mixed state, since there $r_\perp(t) \le r(t) \to 0$ and $\mathrm{artanh}\,r(t) \to 0$ together. It **diverges on the boundary sphere off the pointer axis**, where $\mathrm{artanh}\,r$ blows up while the transverse component stays positive: a state that is nearly pure and nearly orthogonal to the pointer axis has the most information left to lose, and it loses that information fastest. The extremum of the rate over the ball is therefore at purity, not at maximal mixing: the rate is zero at the maximally mixed state and grows without bound as the pure sphere is approached away from the axis, so it is unbounded above over the ball and has no finite maximum.

## Fine and Coarse: Liouville and the Second Law

The distinction between the two values of the functional is now exact, and it is the classical content of the subject.

**Reversible flow preserves the fine-grained entropy.** A reversible evolution of the sector is a matrix-unitary rotor conjugation,

$$
\tilde{Ϛ}(t) = \tilde{U}(t)\,\tilde{Ϛ}(0)\,\tilde{U}(t)^{*}, \qquad \tilde{U}(t)\tilde{U}(t)^{*} = e_t .
$$

Such a map is an automorphism of the algebra; it rotates the Bloch vector without changing its length, $|\vec r(t)| = |\vec r(0)|$. Consequently

$$
\mathcal{S}\!\left(\tilde{Ϛ}(t)\right) = \mathcal{S}\!\left(\tilde{Ϛ}(0)\right),
$$

and the biquaternion norm is likewise invariant. This is the biquaternion form of **Liouville's theorem**: the fine-grained description carries a constant amount of information, and the reversible flow merely permutes it. The companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow* develops the generator-level correspondence between the rotor and the Hamiltonian flow; the conservation of the biquaternion norm is the invariant that the correspondence preserves.

**Coarse-graining produces the increase.** If a fixed coarse-graining $\Phi$ is applied to the state of a reversible flow $\tilde{Ϛ}(t) = \tilde{U}(t)\tilde{Ϛ}(0)\tilde{U}(t)^{*}$, the entropy of the coarse description,

$$
\mathcal{S}_{\rm cg}(t) = \mathcal{S}\!\left(\Phi(\tilde{Ϛ}(t))\right) \ge \mathcal{S}\!\left(\tilde{Ϛ}(t)\right) = \mathcal{S}\!\left(\tilde{Ϛ}(0)\right),
$$

exceeds the fine-grained value at every instant, but it need not grow with $t$: the rotor can carry the transverse component onto the pointer axis and back, and the coarse-grained entropy then oscillates with no trend. A single application of $\Phi$ raises the entropy once and then leaves it fixed, since $\Phi$ is idempotent. Neither a reversible flow nor a fixed coarse-graining produces a *monotone* increase on its own; what produces one is a **one-parameter family of contractions** applied along the flow. The dephasing semigroup is the canonical example — it is the curve $\Phi_{p(t)}$ from the identity at $t=0$ towards the pointer coarse-graining as $t\to\infty$ — and for it the entropy of the evolving state rises monotonically. Both the flow and the contraction are needed for the inequality to bite, and the second law of the sector is a statement about the pair. This is exactly the classical structure of the Gibbs and Boltzmann entropies, now written with the algebra's own instruments.

The dephasing rate makes the statement quantitative: the fine-grained value $\mathcal{S}(\tilde{Ϛ}(0))$ is the conserved reference, the evolving state's entropy increases at rate $\Gamma\,(r_\perp(t)^2/r(t))\,\mathrm{artanh}\,r(t)$, and the total production over an infinite time is $h(|\vec u\cdot\vec r(0)|) - h(|\vec r(0)|)$, the entropy of the retained classical bit less the entropy of the state.

## Preparations, Partitions, and the Least Coarse Description

There is one further relation between the fine and coarse interpretations, and it explains why the fine-grained value is the right reference. A **preparation** of a state is an ensemble of pure states with weights,

$$
\tilde{Ϛ} = \sum_a w_a\, \tilde\Pi(\vec u_a), \qquad w_a \ge 0, \quad \sum_a w_a = 1 ,
$$

so that $\vec r = \sum_a w_a \vec u_a$. The Shannon entropy of the preparation is $H(w) = -\sum_a w_a\log w_a$. The standard theorem on ensembles with a common density matrix states that

$$
\mathcal{S}(\tilde{Ϛ}) \le H(w) ,
$$

with equality exactly for the spectral ensemble, whose states are the two idempotents $\tilde\Pi_{1,2}(\vec u_r)$ with weights $\lambda_\pm$. The fine-grained entropy is therefore the **minimum over preparations** — the least coarse description the state admits. A partition of the pure-state sphere into cells is one preparation among many; merging cells lowers $H$ but changes the mean state, so the comparison is not between $H$ and the entropy of the *same* state. The invariant entropy of the state is the infimum, and the coarse-grained entropies are the values above it.

The identity is verified on the three-point ensemble

$$
w = (0.5,\,0.3,\,0.2), \qquad \vec u = (\vec e_x,\,\vec e_y,\,-\vec e_z),
$$

for which $\vec r = 0.5\,\vec e_x + 0.3\,\vec e_y - 0.2\,\vec e_z$, $|\vec r| = 0.6164414$, $\mathcal{S} = 0.4887927$, and the refinement entropy is $H = 1.0296530$, above the invariant value as the theorem requires. Merging the first two members — the pair with no $\vec e_z$ component, which the partition by the sign of the third component places in the positive cell — into a single cell of combined weight $0.8$ replaces the ensemble by the two-cell preparation $\{\vec e_x,\vec e_y\}\mid\{-\vec e_z\}$ with weights $(0.8,\,0.2)$ and states $(\vec u_+,-\vec e_z)$, where $\vec u_+ = (0.5\,\vec e_x+0.3\,\vec e_y)/\sqrt{0.34}$. That ensemble assembles a **different** state, of radius $\sqrt{0.68} = 0.8246211$ and entropy $0.2971592$, and against *its own* invariant value the merged entropy is again the larger, $H = 0.5004024 > 0.2971592$. Merging lowers $H$ — from $1.0296530$ to $0.5004024$ — and moves the assembled state outward, so the two ends of the comparison both change; the bound holds at either level, and what it does not license is reading the merged $H$ against the entropy of the unmerged state.

The framework's own coarse-grainings sit in this picture as the conditional expectations: the coarsest description of a state along an axis retains the single classical bit $(\vec u\cdot\vec r)$, and its entropy $h(|\vec u\cdot\vec r|)$ is the largest value among the conditional expectations, attained by the axis orthogonal to the state.

## What Is Derived and What Is Imported

**Derived from the algebra.** The entropy functional $\mathcal{S}(\tilde{Ϛ}) = -2\,\mathrm{Sc}(\tilde{Ϛ}\log\tilde{Ϛ})$ itself, its evaluation in the spectral decomposition, and its identification with the classical entropy of the two-outcome pointer distribution; the existence of the logarithm on the interior of the Bloch ball and its failure on the pure states; the identity $\mathcal{S} = h(\sqrt{1 - 4\,\mathrm{Sc}\,N})$, which makes the entropy a function of the biquaternion norm and locates the zero-entropy states exactly on the zero-divisor cone; the invariance of the functional under reversible rotor flow; the form of the coarse-grained conditional expectation and its action $\vec r\mapsto(\vec u\cdot\vec r)\vec u$; and the entropy production rate of continuous dephasing. Each of these is an identity of the algebra, checked by expanding in the basis and, where numerical, on an interior superposition rather than a single pure state.

**Imported from standard physics and standard mathematics.** The Kadison–Schwarz contraction of unital completely positive maps, and hence the monotonicity of the entropy under a coarse-graining; the classification of conditional expectations onto commutative subalgebras; the minimum-ensemble theorem $\mathcal{S}(\tilde{Ϛ}) = \min_w H(w)$; and the identification of the dimensionless functional with the physical thermodynamic entropy through the factor $k_B$. None of these is re-derived here; they are transcribed, and they are the same theorems that give the Gibbs and Boltzmann entropies their classical meaning.

**Not supplied.** The framework does not select which coarse-graining is physically realised; the pointer axis $\vec u$ is an input to the conditional expectation, not an output of it, for the reason given in the companion article *Decoherence as Idempotent Projection*. It does not derive a dynamics for the environment, and therefore does not derive the rate $\Gamma$. It does not, on a single qubit, support a partition into more than two cells. And it predicts no departure from the classical entropy accounting it reformulates.

## Summary

A coarse-graining of the informational sector is a conditional expectation $\Phi$ on $\mathbb{M}_+$: linear, completely positive, trace-preserving, idempotent and unital. For a single qubit it is the projection onto the states of a commutative subalgebra, and its canonical form is the fully dephasing map along an axis $\vec u$, whose action on the Bloch vector is $\vec r\mapsto(\vec u\cdot\vec r)\vec u$.

The **biquaternion entropy functional** is

$$
\mathcal{S}(\tilde{Ϛ}) = -2\,\mathrm{Sc}\!\left(\tilde{Ϛ}\log\tilde{Ϛ}\right)
= -\lambda_+\log\lambda_+ - \lambda_-\log\lambda_- = h(|\vec r|),
\qquad \lambda_\pm = \tfrac{1}{2}\left(1\pm|\vec r|\right),
$$

with $0 \le \mathcal{S} \le \log 2$. It is computed from the algebra's logarithm, which exists exactly on the group of units, that is, on the interior of the Bloch ball: the pure states are the zero divisors, and the entropy is singular there and vanishes there.

The functional depends on the state only through its biquaternion norm. With $\langle\tilde{Ϛ}\rangle_{\natural} = \tfrac{1}{4}(1-|\vec r|^2)e_t$,

$$
\mathcal{S}(\tilde{Ϛ}) = h\!\left(\sqrt{1 - 4\,\mathrm{Sc}\,\langle\tilde{Ϛ}\rangle_{\natural}}\right),
$$

so the entropy vanishes exactly on the null (zero-divisor) cone, is maximal at the maximally mixed state, and measures the depth of the state inside the future cone. The natural invariant of the algebra and the information content of the state are one quantity in two interpretations.

The **coarse-grained entropy** is the functional evaluated on the image, $\mathcal{S}(\Phi(\tilde{Ϛ}))$; for the pointer conditional expectation it is the binary Shannon entropy $h(|\vec u\cdot\vec r|)$. Since a unital completely positive map contracts the Bloch ball, $|\vec r_\Phi|\le|\vec r|$, the coarse-grained entropy never falls below the fine-grained one, with equality only for states already in the image. The fine-grained entropy is invariant under reversible rotor flow — the biquaternion form of Liouville's theorem — and the increase appears only when a flow and a coarse-graining are composed. That composition is the second law of the sector.

The fine-grained value is also the minimum over all preparations of the state, $\mathcal{S}(\tilde{Ϛ}) = \min_w H(w)$, so it is the least coarse description the state admits and the correct reference for the accounting. The framework supplies the functional, its geometry, and its monotonicity; it does not supply the pointer axis, the environment, or the rate, and it predicts nothing beyond the classical entropy accounting it reformulates.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian (informational) and anti-Hermitian (material) subspaces |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r)$ | State of the informational sector, Bloch vector $\vec r$ |
| $\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$ | Idempotent (pure state, rank one) |
| $\lambda_\pm = \tfrac{1}{2}(1\pm|\vec r|)$ | Eigenvalues (pointer probabilities) of the state |
| $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$, $\mathrm{Tr}(e_t)=2$ | Trace |
| $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Biquaternion norm |
| $\langle\tilde{Ϛ}\rangle_{\natural} = \tfrac{1}{4}(1-|\vec r|^2)e_t$ | Biquaternion norm of a state |
| $\tilde{Ϛ}^2 - \tilde{Ϛ} = \tfrac{1}{4}(|\vec r|^2-1)e_t$ | Deviation from idempotency (mixedness) |
| $\mathrm{Tr}(\tilde{Ϛ}^2) = \tfrac{1}{2}(1+|\vec r|^2)$ | Purity |
| $\log\tilde{Ϛ} = (\log\lambda_+)\tilde\Pi_1(\vec u_r) + (\log\lambda_-)\tilde\Pi_2(\vec u_r)$ | Logarithm of a state, $|\vec r|<1$ |
| $\mathcal{S}(\tilde{Ϛ}) = -2\,\mathrm{Sc}(\tilde{Ϛ}\log\tilde{Ϛ}) = h(|\vec r|)$ | Biquaternion entropy functional |
| $h(x) = -\tfrac{1+x}{2}\log\tfrac{1+x}{2} - \tfrac{1-x}{2}\log\tfrac{1-x}{2}$ | Binary entropy function |
| $\mathcal{S} = h\!\left(\sqrt{1-4\,\mathrm{Sc}\,\langle\tilde{Ϛ}\rangle_{\natural}}\right)$ | Entropy as a function of the biquaternion norm |
| $\Phi$ | Coarse-graining (conditional expectation) |
| $\Phi_{\vec u}(\tilde{Ϛ}) = \tilde\Pi_1\tilde{Ϛ}\tilde\Pi_1 + \tilde\Pi_2\tilde{Ϛ}\tilde\Pi_2$ | Pointer coarse-graining along $\vec u$ |
| $\vec r\mapsto(\vec u\cdot\vec r)\vec u$ | Action of the pointer coarse-graining |
| $\mathcal{S}_{\rm cg}[\tilde{Ϛ};\Phi] = \mathcal{S}(\Phi(\tilde{Ϛ}))$ | Coarse-grained entropy |
| $\mathcal{S}_{\rm cg} = h(|\vec u\cdot\vec r|)$ | Coarse-grained entropy, pointer basis |
| $r_\parallel = \vec u\cdot\vec r$, $r_\perp(t) = \exp(-\Gamma t)r_\perp(0)$, $r(t)^2 = r_\parallel^2 + r_\perp(t)^2$ | Axial and instantaneous transverse components of the dephasing flow |
| $\vec r\mapsto(1-p)\vec r + p(\vec u\cdot\vec r)\vec u$ | Dephasing at strength $p\in[0,1]$ |
| $d\mathcal{S}/dt = \Gamma (r_\perp(t)^2/r(t))\,\mathrm{artanh}\,r(t)$ | Entropy production rate of continuous dephasing (instantaneous $r_\perp$) |
| $\tilde{U}(t)$, $\tilde{U}\tilde{U}^{*} = e_t$ | Matrix-unitary rotor (reversible flow) |
| $H(w) = -\sum_a w_a\log w_a$ | Preparation entropy |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

## Further Reading

- C. E. Shannon, "A mathematical theory of communication," *Bell System Technical Journal* **27** (1948) 379–423, for the entropy of a coarse description and its properties.
- E. T. Jaynes, "Gibbs vs Boltzmann entropies," *American Journal of Physics* **33** (1965) 391–398, for the fine-grained and coarse-grained entropies of classical statistical mechanics.
- E. T. Jaynes, "Information theory and statistical mechanics," *Physical Review* **106** (1957) 620–630, for entropy as missing information.
- A. Wehrl, "General properties of entropy," *Reviews of Modern Physics* **50** (1978) 221–260, for the monotonicity and concavity of entropy functionals.
- L. D. Landau and E. M. Lifshitz, *Statistical Physics* (Pergamon, 1980), for the coarse-grained entropy and its increase in classical systems.
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the spectral entropy, the minimum-ensemble theorem, and the data-processing inequality.
- A. Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for the Bloch-ball geometry of states and the geometry of entropy.
- D. Petz, *Quantum Information Theory and Quantum Statistics* (Springer, 2008), for conditional expectations, coarse-graining maps, and the monotonicity of entropy.
- R. Balian, "Information in statistical physics," *Studies in History and Philosophy of Modern Physics* **36** (2005) 323–353, for the distinction between the fine-grained and coarse-grained descriptions.
