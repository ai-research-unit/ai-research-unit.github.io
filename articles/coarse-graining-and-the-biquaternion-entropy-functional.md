# __Coarse-Graining and the Biquaternion Entropy Functional__

## Introduction

A **coarse-graining** is a description that discards fine-grained distinctions. The state of a physical system is replaced by a record of which cell of a partition it occupies, and the information the record carries is measured by the entropy of the induced cell distribution. Coarse-graining is the operation that makes entropy increase: the fine-grained descriptions of classical mechanics are conserved by the reversible flow, while the coarse-grained ones are not, and the difference between the two is the content of the second law.

This article develops the coarse-grained entropy functional of the informational sector $\mathbb{M}_+$ of the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. The two ingredients are both already in the framework. The **states** of the sector are the positive trace-one elements $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$ of $\mathbb{M}_+$, the Bloch ball; its **pure states** are the idempotents, and they sit on the null cone of the norm form, which is the zero-divisor cone of the algebra. The **coarse-grainings** are the conditional expectations of the sector: the completely positive, trace-preserving, idempotent maps onto a commutative subalgebra, of which the fully dephasing channel of the companion article *Quantum Channels and the Reversible/Irreversible Dichotomy* is the canonical example. The entropy functional is the algebra's own logarithm applied to a state and paired with it through the trace:

$$
\mathcal{S}(\tilde{\rho}) = -2\,\mathrm{Sc}\!\left(\tilde{\rho}\log\tilde{\rho}\right).
$$

The article's central result is that this functional depends on the state **only through its norm form**. With $N(\tilde{\rho}) = \tilde{\rho}\bar{\tilde{\rho}} = \tfrac{1}{4}(1-|\mathbf{r}|^2)e_0$, one has $|\mathbf{r}| = \sqrt{1 - 4\,\mathrm{Sc}\,N(\tilde{\rho})}$, and therefore

$$
\mathcal{S}(\tilde{\rho}) = h\!\left(\sqrt{1 - 4\,\mathrm{Sc}\,N(\tilde{\rho})}\right),
$$

where $h$ is the binary entropy function. The entropy vanishes exactly on the null cone, that is, exactly on the zero divisors; it is maximal at the maximally mixed state; and it measures the depth of the state inside the future cone of the norm form. The functional and the norm form are thus the same information, read as a number and as a quadratic form.

Two functionals appear below and must be kept apart, because the whole subject turns on the difference. The **spectral** value $\mathcal{S}(\tilde{\rho})$ is a property of the state and is invariant under reversible rotor flow; it is the fine-grained reference. The **coarse-grained** value $\mathcal{S}(\Phi(\tilde{\rho}))$ is the entropy of the image of the state under a coarse-graining $\Phi$, and it is this second number that increases under a coarse-graining. The second law, in this language, is the statement that a coarse-graining is a contraction of the Bloch ball, so that the entropy of the image is never less than the entropy of the state. The two are reconciled by the fact that the fine-grained value is the *minimum* over all preparations of the state, and hence the least coarse description the state admits.

The treatment is **classical**. The entropy here is the Shannon entropy of a coarse description, and the functional is the classical one throughout. The functional $\mathcal{S}$ coincides numerically, on the matrix representative of $\tilde{\rho}$, with the von Neumann entropy of that $2\times 2$ density matrix, and the reader should not be misled by the coincidence: the von Neumann entropy as such, and the entropies attached to POVMs and to entanglement, belong to the informational subcategory of the sibling quantum category, where the companion article *Von Neumann Entropy and the Biquaternion Norm Form* develops them, and they are not developed here. Where the quantum reading is used, it is used as a bound, and it is identified as such.

The probabilities the functional is built from are themselves trace pairings. The weights $\lambda_\pm$ of the spectral decomposition are $\lambda_\pm = \mathrm{Tr}(\tilde{P}_\pm(\hat{\mathbf{r}})\tilde{\rho})$, and the companion article *The Born Rule as a Trace Formula — Derivation and Comparison* derives the form of that pairing and fixes the objects it relates; this article takes the form as given and uses it only to read the state's own two-outcome distribution.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$; the scalar imaginary is $i$, central in $\mathbb{B}$; the two four-dimensional real subspaces are the anti-Hermitian material sector $\mathbb{M}_-$ and the Hermitian informational sector $\mathbb{M}_+$, with $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$; the trace is $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$, normalised by $\mathrm{Tr}(e_0) = 2$; and the trace formula for a state and an observable is $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$.

## The State Space of the Informational Sector

A state of the informational sector is an element

$$
\tilde{\rho} = \tfrac{1}{2}\left(e_0 + i\,\mathbf{r}\right), \qquad \mathbf{r} = r_1 e_1 + r_2 e_2 + r_3 e_3, \quad \mathbf{r} \in \mathbb{R}^3,
$$

of the Hermitian subspace $\mathbb{M}_+$. The scalar part of $\tilde{\rho}$ is real, its vector part is purely imaginary, and its trace is

$$
\mathrm{Tr}(\tilde{\rho}) = 2\,\mathrm{Sc}(\tilde{\rho}) = 1 .
$$

The state is positive precisely when the Bloch vector lies in the closed unit ball,

$$
\tilde{\rho} \ge 0 \quad \Longleftrightarrow \quad |\mathbf{r}| \le 1 ,
$$

so that the states form the **Bloch ball**; the pure states are its boundary sphere. A pure state is an idempotent,

$$
\tilde{P}_\pm(\hat{\boldsymbol{\mu}}) = \tfrac{1}{2}\left(e_0 \pm i\,\hat{\boldsymbol{\mu}}\right), \qquad |\hat{\boldsymbol{\mu}}| = 1, \qquad \tilde{P}_\pm^2 = \tilde{P}_\pm ,
$$

and conversely every idempotent of $\mathbb{M}_+$ has this form. The complementary idempotents are orthogonal and complete, $\tilde{P}_+\tilde{P}_- = 0$ and $\tilde{P}_+ + \tilde{P}_- = e_0$.

### The Norm Form of a State

The norm form of the algebra is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$. On the state it evaluates to a scalar multiple of the identity:

$$
N(\tilde{\rho}) = \tilde{\rho}\bar{\tilde{\rho}} = \left(\tfrac{1}{2}\right)^2 + \left(\tfrac{i r_1}{2}\right)^2 + \left(\tfrac{i r_2}{2}\right)^2 + \left(\tfrac{i r_3}{2}\right)^2 = \tfrac{1}{4}\left(1 - |\mathbf{r}|^2\right)e_0 .
$$

This single identity carries the geometry of the state space. The norm form is **positive** in the interior of the Bloch ball, **zero** on its boundary, and **negative** outside it, so that the state space is exactly the trace-one slice of the future cone of the norm form. The boundary of the state space is the **zero-divisor cone**: the pure states are the elements of $\mathbb{M}_+$ that fail to be invertible. The norm form therefore measures how far inside the cone a state lies, and its vanishing is the algebraic statement of purity.

Two further identities follow from the multiplication table and are used throughout. Squaring the state gives

$$
\tilde{\rho}^2 = \tfrac{1}{4}\left(\left(1 + |\mathbf{r}|^2\right)e_0 + 2i\,\mathbf{r}\right),
$$

because $(i\mathbf{r})^2 = -\mathbf{r}^2 = |\mathbf{r}|^2 e_0$ and $(i\mathbf{r})$ commutes with the scalar; and therefore the **deviation from idempotency** is a pure scalar,

$$
\tilde{\rho}^2 - \tilde{\rho} = \tfrac{1}{4}\left(|\mathbf{r}|^2 - 1\right)e_0 .
$$

Equivalently, the purity is

$$
\mathrm{Tr}\!\left(\tilde{\rho}^2\right) = \tfrac{1}{2}\left(1 + |\mathbf{r}|^2\right),
$$

so that purity and idempotency are the same condition, and the norm form, the deviation from idempotency, and the purity are three readings of the single number $|\mathbf{r}|^2$.

## The Entropy Functional

### Existence of the Logarithm

The entropy functional is built from the algebra's logarithm. The logarithm of a biquaternion is defined as the inverse of the exponential, and the companion article *Biquaternion Elementary Functions* establishes the relevant fact: the logarithm exists exactly on the group of units,

$$
\mathbb{B}^\times = \left\{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) \neq 0\right\},
$$

and on no larger set. The proof is the polar decomposition $\tilde{Q} = R\exp(\Theta\hat{n})$ with $R = \sqrt{N(\tilde{Q})}$, which fails precisely when $N(\tilde{Q}) = 0$.

For the state this condition is transparent. A state in the interior of the Bloch ball has

$$
N(\tilde{\rho}) = \tfrac{1}{4}\left(1 - |\mathbf{r}|^2\right)e_0 \neq 0 \qquad (|\mathbf{r}| < 1),
$$

so it is a unit and its logarithm exists. A **pure** state has $N(\tilde{\rho}) = 0$: it is a zero divisor, the logarithm does not exist there, and the entropy is defined on the boundary by continuity. The locus where the entropy functional is analytically singular is exactly the locus of purity, and that coincidence is the geometric content of the whole subject.

### Definition from the Spectral Decomposition

The logarithm of a state is evaluated with the idempotents. Writing $\hat{\mathbf{r}} = \mathbf{r}/|\mathbf{r}|$ for a state with $\mathbf{r} \neq 0$, the spectral decomposition of the state in its own basis is

$$
\tilde{\rho} = \lambda_+\, \tilde{P}_+(\hat{\mathbf{r}}) + \lambda_-\, \tilde{P}_-(\hat{\mathbf{r}}), \qquad
\lambda_\pm = \tfrac{1}{2}\left(1 \pm |\mathbf{r}|\right),
$$

as one verifies directly from the definitions of the idempotents. The eigenvalues $\lambda_\pm$ are the classical probabilities of the two pointer outcomes in the eigenbasis, they are non-negative for $|\mathbf{r}| \le 1$, and they sum to one. The functional calculus of the algebra then gives

$$
\log\tilde{\rho} = \left(\log\lambda_+\right)\tilde{P}_+(\hat{\mathbf{r}}) + \left(\log\lambda_-\right)\tilde{P}_-(\hat{\mathbf{r}}),
$$

which is the principal branch on the positive part of $\mathbb{M}_+$; on the general algebra the logarithm is multivalued, and positivity of the state removes the ambiguity by fixing the branch. Multiplying and taking the scalar part, using $\mathrm{Sc}(\tilde{P}_\pm) = \tfrac{1}{2}$, gives $\mathrm{Sc}(\tilde{\rho}\log\tilde{\rho}) = \tfrac{1}{2}(\lambda_+\log\lambda_+ + \lambda_-\log\lambda_-)$, and therefore

$$
\mathcal{S}(\tilde{\rho}) = -2\,\mathrm{Sc}\!\left(\tilde{\rho}\log\tilde{\rho}\right)
= -\lambda_+\log\lambda_+ - \lambda_-\log\lambda_- .
$$

This is the **biquaternion entropy functional**. It is a real number, it is computed from the algebra's own product, logarithm and trace, and it is the classical Shannon entropy of the two-outcome distribution $(\lambda_+,\lambda_-)$ that the state induces in its eigenbasis. Written out in the Bloch radius it is the binary entropy function,

$$
\mathcal{S}(\tilde{\rho}) = h(|\mathbf{r}|), \qquad
h(x) = -\frac{1+x}{2}\log\frac{1+x}{2} - \frac{1-x}{2}\log\frac{1-x}{2},
$$

with the boundary values $h(0) = \log 2$ and $h(1) = 0$.

The evaluation is stable under the same computation in the full algebra. For the interior state obtained by superposing two orthogonal pure states with equal weight, $\tilde{\rho} = \tfrac{1}{2}\left(\tilde{P}_+(e_1) + \tilde{P}_+(e_2)\right)$, one has $\mathbf{r} = \tfrac{1}{2}(e_1 + e_2)$, $|\mathbf{r}| = 1/\sqrt{2}$, and the two routes agree:

$$
\mathcal{S} = -2\,\mathrm{Sc}\!\left(\tilde{\rho}\log\tilde{\rho}\right) = 0.4164955307\ldots,
$$

matching $h(1/\sqrt{2})$ to machine precision. The verification is on this superposition, that is, on an interior (mixed) state, where the logarithm is nonsingular and the two-outcome distribution is nontrivial.

### Elementary Properties

Three properties follow immediately and are worth recording, because they are the properties the coarse-grained entropy inherits.

**Range.** Since $0 \le \lambda_\pm \le 1$ with $\lambda_+ + \lambda_- = 1$, the functional is non-negative and bounded above:

$$
0 \le \mathcal{S}(\tilde{\rho}) \le \log 2 ,
$$

with the lower bound attained exactly on the pure states, $|\mathbf{r}| = 1$, and the upper bound exactly at the maximally mixed state, $\mathbf{r} = 0$, where $\tilde{\rho} = \tfrac{1}{2}e_0$ and $\lambda_+ = \lambda_- = \tfrac{1}{2}$.

**Symmetry.** The functional is unchanged by the exchange $\lambda_+ \leftrightarrow \lambda_-$, equivalently by $\mathbf{r} \mapsto -\mathbf{r}$; both are the same classical distribution. It is a function of the radius alone, so it is invariant under every rotation of the Bloch ball.

**Concavity.** The binary entropy is concave in its argument, so $\mathcal{S}$ is concave along the Bloch radius: for a mixture $\tilde{\rho} = p\tilde{\rho}_1 + (1-p)\tilde{\rho}_2$,

$$
\mathcal{S}\!\left(p\tilde{\rho}_1 + (1-p)\tilde{\rho}_2\right)
\;\ge\; p\,\mathcal{S}\!\left(\tilde{\rho}_1\right) + (1-p)\,\mathcal{S}\!\left(\tilde{\rho}_2\right),
$$

a mixture being never less entropic than the average of its constituents. This is the elementary form of the second law for the sector. The comparison is against the **average** and not against each constituent separately: mixing the maximally mixed state with a pure state in equal parts gives $\mathcal{S} = h(\tfrac{1}{2}) = 0.5623351$, which is below the $\log 2 = 0.6931472$ of the maximally mixed state alone, so mixing can lower the entropy of a particular constituent even though it can never lower it below the mean.

The functional is measured in nats. Multiplying by the Boltzmann constant, $\mathcal{S}_{\rm th} = k_B\,\mathcal{S}$, gives a thermodynamic entropy; the algebra supplies the dimensionless information content, and the unit is a convention of thermodynamics rather than of the algebra.

## The Entropy Is a Function of the Norm Form

The norm form of the state and the entropy of the state are not independent quantities. The norm form gives $|\mathbf{r}|$ directly, and the entropy is a function of $|\mathbf{r}|$; composing the two eliminates the Bloch vector and leaves a function of the norm form alone.

Inverting $N(\tilde{\rho}) = \tfrac{1}{4}(1-|\mathbf{r}|^2)e_0$ gives

$$
|\mathbf{r}| = \sqrt{1 - 4\,\mathrm{Sc}\,N(\tilde{\rho})},
$$

and substituting into $\mathcal{S} = h(|\mathbf{r}|)$ gives the central identity of the article:

$$
\boxed{\;\mathcal{S}(\tilde{\rho}) = h\!\left(\sqrt{1 - 4\,\mathrm{Sc}\,N(\tilde{\rho})}\right).\;}
$$

The identity says that **the entropy of a state of the informational sector is a function of its norm form and of nothing else**. The norm form is the quantitatively meaningful invariant of the algebra; the entropy is a monotone reparametrisation of it. Three consequences are immediate, and they are the reason the identity is worth isolating.

First, the entropy vanishes exactly where the norm form vanishes. The condition $\mathcal{S}(\tilde{\rho}) = 0$ is $|\mathbf{r}| = 1$, which is $N(\tilde{\rho}) = 0$, which is the statement that $\tilde{\rho}$ is a zero divisor. **Zero entropy and the zero-divisor cone are the same locus.** The pure states are the informationless states, and the algebraic reason is that they are the non-invertible ones.

Second, the entropy is a strictly increasing function of the norm form on the positive cone. As the state moves inward from the boundary, $|\mathbf{r}|$ falls, $N$ rises from zero to its maximum $\tfrac{1}{4}e_0$ at the centre, and the entropy rises from zero to $\log 2$. Differentiating the boxed identity confirms the direction, $\partial\mathcal{S}/\partial\,\mathrm{Sc}\,N = 2\,\mathrm{artanh}\,|\mathbf{r}|/|\mathbf{r}| > 0$. The norm form is therefore a measure of **depth inside the cone**, and the entropy is that depth expressed in information units.

Third, the entropy is invariant under every operation that preserves the norm form. In particular, it is invariant under the rotor conjugation of a reversible flow, which is the subject of a later section.

The same identity holds for a coarse-grained state, since a coarse-grained state is a state. If $\Phi$ is a coarse-graining and $\tilde{\rho}_\Phi = \Phi(\tilde{\rho})$ is its image, then

$$
\mathcal{S}(\tilde{\rho}_\Phi) = h\!\left(\sqrt{1 - 4\,\mathrm{Sc}\,N(\tilde{\rho}_\Phi)}\right),
$$

so the whole information content of the coarse description is likewise carried by one scalar read from the norm form. This is what makes the coarse-grained entropy tractable: the second law for the sector reduces to a statement about the norm form of the image.

## Coarse-Graining on the Informational Sector

### What a Coarse-Graining Is

A coarse-graining is a description that remembers less. In the language of the sector it is a map

$$
\Phi : \mathbb{M}_+ \longrightarrow \mathbb{M}_+, \qquad \tilde{\rho} \longmapsto \Phi(\tilde{\rho}),
$$

subject to four conditions, each of which has an operational reading.

- **Linearity.** $\Phi(a\tilde{\rho}_1 + b\tilde{\rho}_2) = a\Phi(\tilde{\rho}_1) + b\Phi(\tilde{\rho}_2)$ for real $a,b$. A coarse-graining of a mixture is the mixture of the coarse-grainings, because the description acts on the preparation rather than on the individual outcome.
- **Positivity, in the strong form of complete positivity.** The map must remain positive when the sector is described jointly with any reference system, which is the condition that distinguishes a physical operation from a merely positive map, as the companion article *Quantum Channels and the Reversible/Irreversible Dichotomy* develops.
- **Trace preservation.** $\mathrm{Tr}(\Phi(\tilde{\rho})) = \mathrm{Tr}(\tilde{\rho})$, so that a state is sent to a state. Equivalently the dual map fixes the identity, $\Phi^{*}(e_0) = e_0$.
- **Idempotency and unitality.** $\Phi \circ \Phi = \Phi$ and $\Phi(e_0) = e_0$. The first says that coarse-graining twice is coarse-graining once: once a distinction has been discarded, it cannot be discarded again. The second says that the maximally mixed state is already as coarse as the description can be, so it is fixed.

A linear, completely positive, trace-preserving, idempotent, unital map is a **conditional expectation**: it projects the state space onto the states of a commutative subalgebra, the subalgebra of the quantities the description retains. For a single qubit the commutative subalgebras of $\mathbb{B}$ are two-dimensional, generated by a pair of orthogonal idempotents, and the conditional expectation onto the subalgebra generated by $\tilde{P}_\pm(\hat{\mathbf{n}})$ is the fully dephasing map

$$
\Phi_{\hat{\mathbf{n}}}(\tilde{\rho}) = \tilde{P}_+(\hat{\mathbf{n}})\,\tilde{\rho}\,\tilde{P}_+(\hat{\mathbf{n}}) + \tilde{P}_-(\hat{\mathbf{n}})\,\tilde{\rho}\,\tilde{P}_-(\hat{\mathbf{n}}) .
$$

This is the map of the companion article *Decoherence as Idempotent Projection* at $p = 1$. On the Bloch vector it acts by

$$
\mathbf{r} \longmapsto \left(\hat{\mathbf{n}}\cdot\mathbf{r}\right)\hat{\mathbf{n}},
$$

annihilating the component transverse to the axis and retaining the component along it. The image is the **diameter** of the Bloch ball along $\hat{\mathbf{n}}$: the classical bit that the description retains.

### The Binary Limitation

It must be said plainly that a coarse-graining of a single qubit is **binary**. The reason is algebraic and not a shortcoming of the treatment: $\mathbb{M}_+$ has only two orthogonal idempotents at a time, so a commutative subalgebra of $\mathbb{B}$ is at most two-dimensional, and a conditional expectation can retain at most one classical bit. A partition of the state space into three or more cells is not a conditional expectation of $\mathbb{B}$ and has no image in the sector; it requires the tensor product $\mathbb{B}^{\otimes n}$, whose states are treated in the sibling quantum category. What the single-qubit framework supplies is the *mechanism* of coarse-graining — the conditional expectation, its idempotency, its contraction of the ball — and the mechanism is what the entropy functional needs. The many-cell case is a matter of enlarging the algebra, not of changing the argument.

### The Coarse-Grained Entropy

With the coarse-graining fixed, the **coarse-grained entropy** is the entropy functional evaluated on the image,

$$
\mathcal{S}_{\rm cg}\!\left[\tilde{\rho};\Phi\right] = \mathcal{S}\!\left(\Phi(\tilde{\rho})\right) = -2\,\mathrm{Sc}\!\left(\Phi(\tilde{\rho})\log\Phi(\tilde{\rho})\right).
$$

For the pointer conditional expectation $\Phi_{\hat{\mathbf{n}}}$, the image is $\tilde{\rho}_{\rm cg} = \tfrac{1}{2}(e_0 + i(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}})$, whose eigenvalues are

$$
p_\pm = \tfrac{1}{2}\left(1 \pm \hat{\mathbf{n}}\cdot\mathbf{r}\right),
$$

the classical probabilities of the two pointer outcomes. The coarse-grained entropy is therefore the binary Shannon entropy

$$
\mathcal{S}_{\rm cg}\!\left[\tilde{\rho};\Phi_{\hat{\mathbf{n}}}\right] = -p_+\log p_+ - p_-\log p_- = h\!\left(|\hat{\mathbf{n}}\cdot\mathbf{r}|\right).
$$

This is the article's second main formula. It is the entropy of the classical record the coarse description keeps, and it is manifestly a function of the retained component of the Bloch vector alone.

## Monotonicity Under Coarse-Graining

### The Contraction

Coarse-graining cannot decrease the entropy. The proof has two steps, and both are standard.

The first step is that a unital, completely positive, trace-preserving map is a **contraction of the Bloch ball**. This is the Kadison–Schwarz inequality: for a unital completely positive map $\Phi$ one has $\Phi(\tilde{X})^2 \leq \Phi(\tilde{X}^2)$ in the matrix order. Taking the trace, and using trace preservation in the form $\mathrm{Tr}(\Phi(\tilde{X}^2)) = \mathrm{Tr}(\tilde{X}^2)$,

$$
\mathrm{Tr}\!\left(\Phi(\tilde{X})^2\right) \le \mathrm{Tr}\!\left(\Phi(\tilde{X}^2)\right) = \mathrm{Tr}\!\left(\tilde{X}^2\right),
$$

and with $\tilde{X} = \tilde{\rho}$ this is the purity inequality $\mathrm{Tr}(\Phi(\tilde{\rho})^2) \le \mathrm{Tr}(\tilde{\rho}^2)$. By the purity formula $\mathrm{Tr}(\tilde{\rho}^2) = \tfrac{1}{2}(1+|\mathbf{r}|^2)$ this is exactly

$$
|\mathbf{r}_\Phi| \le |\mathbf{r}| ,
$$

the statement that the map does not push a state outward. Equivalently, and in the form used for classical mechanics, every completely positive trace-preserving map is a contraction in the trace distance, and for a qubit the trace distance between two states is half the Euclidean distance between their Bloch vectors; the contraction of the metric and the contraction of the radius are the same statement.

The second step is the monotonicity of the entropy as a function of the radius, established above: $h$ is decreasing on $[0,1]$. Composing the two,

$$
\mathcal{S}\!\left(\Phi(\tilde{\rho})\right) = h\!\left(|\mathbf{r}_\Phi|\right) \ge h\!\left(|\mathbf{r}|\right) = \mathcal{S}\!\left(\tilde{\rho}\right),
$$

or, in one line,

$$
\boxed{\;\mathcal{S}\!\left(\Phi(\tilde{\rho})\right) \ge \mathcal{S}\!\left(\tilde{\rho}\right)\;}
$$

for every coarse-graining $\Phi$. **Coarse-graining never creates information; it can only fail to retain it.** The inequality is strict unless the state already lies in the image of $\Phi$, so a genuine coarse-graining strictly increases the entropy of every state outside its image.

The restriction to unital maps matters and is worth naming. A trace-preserving completely positive map that is *not* unital can lower the entropy of the state — that is refrigeration, which exports entropy to an environment — and such a map is not a coarse-graining in the sense used here. A coarse-graining discards distinctions *within* the description and keeps no ledger of what it exported; the environment, and with it the full accounting of the second law, is the subject of the companion articles *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form* and *Maxwell's Demon and the Informational Sector in Biquaternionic Form*.

### The Dephasing Family and Its Rate

The dephasing channel of the companion article *Decoherence as Idempotent Projection* interpolates between the identity and the coarse-graining. At strength $p \in [0,1]$ along $\hat{\mathbf{n}}$ it acts by

$$
\mathbf{r} \longmapsto \mathbf{r}' = (1-p)\,\mathbf{r} + p\left(\hat{\mathbf{n}}\cdot\mathbf{r}\right)\hat{\mathbf{n}},
$$

so that

$$
|\mathbf{r}'|^2 = \left(\hat{\mathbf{n}}\cdot\mathbf{r}\right)^2 + (1-p)^2\left(|\mathbf{r}|^2 - \left(\hat{\mathbf{n}}\cdot\mathbf{r}\right)^2\right) \le |\mathbf{r}|^2 ,
$$

with equality only at $p=0$, or for states already on the axis. The entropy therefore increases monotonically with $p$ from $\mathcal{S}(\tilde{\rho})$ to $h(|\hat{\mathbf{n}}\cdot\mathbf{r}|)$, and it is maximised over the axis by the choice $\hat{\mathbf{n}} \perp \mathbf{r}$, which discards the state entirely and returns $\log 2$.

In continuous time, with the transverse component decaying as $e^{-\Gamma t}$ and the axial component fixed, the Bloch radius is

$$
r(t) = \sqrt{r_\parallel^2 + r_\perp(t)^2}, \qquad r_\perp(t) = e^{-\Gamma t}r_\perp(0),
$$

where $r_\parallel = \hat{\mathbf{n}}\cdot\mathbf{r}(0)$ is the fixed axial component and $r_\perp(t)$ is the **instantaneous** transverse component, and the entropy production rate is

$$
\frac{d}{dt}\mathcal{S}\!\left(\tilde{\rho}(t)\right)
= -\dot{r}(t)\,\mathrm{artanh}\,r(t)
= \Gamma\,\frac{r_\perp(t)^2}{r(t)}\,\mathrm{artanh}\,r(t) \;\ge\; 0 ,
$$

using $h'(r) = -\mathrm{artanh}\,r$ and $\dot{r}(t) = -\Gamma r_\perp(t)^2/r(t)$. The rate is supported by the instantaneous transverse component, since it is $r_\perp(t)$ that carries the contraction; the initial component alone would overstate the rate at every $t > 0$.

The distinction matters as soon as the state has an axial part. Take $\mathbf{r} = (0.3, 0.4, 0.5)$ with $\hat{\mathbf{n}} = e_3$ and $\Gamma = 0.7$, so that $r_\parallel = 0.5$ and $r_\perp(0) = 0.5$: at $t = 1$ the finite-difference derivative is $0.0487233141$ and $\Gamma r_\perp(t)^2\,\mathrm{artanh}\,r(t)/r(t) = 0.0487233141$, whereas the same expression with $r_\perp(0)$ in place of $r_\perp(t)$ gives $0.1975827817$. On the state of the earlier checks, $\mathbf{r} = \tfrac{1}{2}(e_1+e_2)$ with $\hat{\mathbf{n}} = e_3$, the axial part vanishes, $r_\perp(t) = r(t)$, and at $t = 0$ the rate is $\Gamma\,r\,\mathrm{artanh}\,r = 0.4362576681$; that case cannot separate the two readings, which is why the state with $r_\parallel \neq 0$ is the decisive check.

The rate is positive and it vanishes when the transverse component vanishes. It also vanishes at the maximally mixed state, since there $r_\perp(t) \le r(t) \to 0$ and $\mathrm{artanh}\,r(t) \to 0$ together. It **diverges on the boundary sphere off the pointer axis**, where $\mathrm{artanh}\,r$ blows up while the transverse component stays positive: a state that is nearly pure and nearly orthogonal to the pointer axis has the most information left to lose, and it loses that information fastest. The extremum of the rate over the ball is therefore at purity, not at maximal mixing: the rate is zero at the maximally mixed state and grows without bound as the pure sphere is approached away from the axis, so it is unbounded above over the ball and has no finite maximum.

## Fine and Coarse: Liouville and the Second Law

The distinction between the two values of the functional is now exact, and it is the classical content of the subject.

**Reversible flow preserves the fine-grained entropy.** A reversible evolution of the sector is a matrix-unitary rotor conjugation,

$$
\tilde{\rho}(t) = \tilde{U}(t)\,\tilde{\rho}(0)\,\tilde{U}(t)^\dagger, \qquad \tilde{U}(t)\tilde{U}(t)^\dagger = e_0 .
$$

Such a map is an automorphism of the algebra; it rotates the Bloch vector without changing its length, $|\mathbf{r}(t)| = |\mathbf{r}(0)|$. Consequently

$$
\mathcal{S}\!\left(\tilde{\rho}(t)\right) = \mathcal{S}\!\left(\tilde{\rho}(0)\right),
$$

and the norm form is likewise invariant. This is the biquaternion form of **Liouville's theorem**: the fine-grained description carries a constant amount of information, and the reversible flow merely permutes it. The companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow* develops the generator-level correspondence between the rotor and the Hamiltonian flow; the conservation of the norm form is the invariant that the correspondence preserves.

**Coarse-graining produces the increase.** If a fixed coarse-graining $\Phi$ is applied to the state of a reversible flow $\tilde{\rho}(t) = \tilde{U}(t)\tilde{\rho}(0)\tilde{U}(t)^\dagger$, the entropy of the coarse description,

$$
\mathcal{S}_{\rm cg}(t) = \mathcal{S}\!\left(\Phi(\tilde{\rho}(t))\right) \ge \mathcal{S}\!\left(\tilde{\rho}(t)\right) = \mathcal{S}\!\left(\tilde{\rho}(0)\right),
$$

exceeds the fine-grained value at every instant, but it need not grow with $t$: the rotor can carry the transverse component onto the pointer axis and back, and the coarse-grained entropy then oscillates with no trend. A single application of $\Phi$ raises the entropy once and then leaves it fixed, since $\Phi$ is idempotent. Neither a reversible flow nor a fixed coarse-graining produces a *monotone* increase on its own; what produces one is a **one-parameter family of contractions** applied along the flow. The dephasing semigroup is the canonical example — it is the curve $\Phi_{p(t)}$ from the identity at $t=0$ towards the pointer coarse-graining as $t\to\infty$ — and for it the entropy of the evolving state rises monotonically. Both the flow and the contraction are needed for the inequality to bite, and the second law of the sector is a statement about the pair. This is exactly the classical structure of the Gibbs and Boltzmann entropies, now written with the algebra's own instruments.

The dephasing rate makes the statement quantitative: the fine-grained value $\mathcal{S}(\tilde{\rho}(0))$ is the conserved reference, the evolving state's entropy increases at rate $\Gamma\,(r_\perp(t)^2/r(t))\,\mathrm{artanh}\,r(t)$, and the total production over an infinite time is $h(|\hat{\mathbf{n}}\cdot\mathbf{r}(0)|) - h(|\mathbf{r}(0)|)$, the entropy of the retained classical bit less the entropy of the state.

## Preparations, Partitions, and the Least Coarse Description

There is one further relation between the fine and coarse readings, and it explains why the fine-grained value is the right reference. A **preparation** of a state is an ensemble of pure states with weights,

$$
\tilde{\rho} = \sum_a w_a\, \tilde{P}(\hat{\boldsymbol{\mu}}_a), \qquad w_a \ge 0, \quad \sum_a w_a = 1 ,
$$

so that $\mathbf{r} = \sum_a w_a \hat{\boldsymbol{\mu}}_a$. The Shannon entropy of the preparation is $H(w) = -\sum_a w_a\log w_a$. The standard theorem on ensembles with a common density matrix states that

$$
\mathcal{S}(\tilde{\rho}) \le H(w) ,
$$

with equality exactly for the spectral ensemble, whose states are the two eigenprojectors $\tilde{P}_\pm(\hat{\mathbf{r}})$ with weights $\lambda_\pm$. The fine-grained entropy is therefore the **minimum over preparations** — the least coarse description the state admits. A partition of the pure-state sphere into cells is one preparation among many; merging cells lowers $H$ but changes the mean state, so the comparison is not between $H$ and the entropy of the *same* state. The invariant entropy of the state is the infimum, and the coarse-grained entropies are the values above it.

The identity is verified on the three-point ensemble

$$
w = (0.5,\,0.3,\,0.2), \qquad \hat{\boldsymbol{\mu}} = (e_1,\,e_2,\,-e_3),
$$

for which $\mathbf{r} = 0.5\,e_1 + 0.3\,e_2 - 0.2\,e_3$, $|\mathbf{r}| = 0.6164414$, $\mathcal{S} = 0.4887927$, and the refinement entropy is $H = 1.0296530$, above the invariant value as the theorem requires. Merging the first two members — the pair with no $e_3$ component, which the partition by the sign of the third component places in the positive cell — into a single cell of combined weight $0.8$ replaces the ensemble by the two-cell preparation $\{e_1,e_2\}\mid\{-e_3\}$ with weights $(0.8,\,0.2)$ and states $(\hat{\boldsymbol{\mu}}_+,-e_3)$, where $\hat{\boldsymbol{\mu}}_+ = (0.5\,e_1+0.3\,e_2)/\sqrt{0.34}$. That ensemble assembles a **different** state, of radius $\sqrt{0.68} = 0.8246211$ and entropy $0.2971592$, and against *its own* invariant value the merged entropy is again the larger, $H = 0.5004024 > 0.2971592$. Merging lowers $H$ — from $1.0296530$ to $0.5004024$ — and moves the assembled state outward, so the two ends of the comparison both change; the bound holds at either level, and what it does not license is reading the merged $H$ against the entropy of the unmerged state.

The framework's own coarse-grainings sit in this picture as the conditional expectations: the coarsest description of a state along an axis retains the single classical bit $(\hat{\mathbf{n}}\cdot\mathbf{r})$, and its entropy $h(|\hat{\mathbf{n}}\cdot\mathbf{r}|)$ is the largest value among the conditional expectations, attained by the axis orthogonal to the state.

## What Is Derived and What Is Imported

**Derived from the algebra.** The entropy functional $\mathcal{S}(\tilde{\rho}) = -2\,\mathrm{Sc}(\tilde{\rho}\log\tilde{\rho})$ itself, its evaluation in the spectral decomposition, and its identification with the classical entropy of the two-outcome pointer distribution; the existence of the logarithm on the interior of the Bloch ball and its failure on the pure states; the identity $\mathcal{S} = h(\sqrt{1 - 4\,\mathrm{Sc}\,N})$, which makes the entropy a function of the norm form and locates the zero-entropy states exactly on the zero-divisor cone; the invariance of the functional under reversible rotor flow; the form of the coarse-grained conditional expectation and its action $\mathbf{r}\mapsto(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}}$; and the entropy production rate of continuous dephasing. Each of these is an identity of the algebra, checked by expanding in the basis and, where numerical, on an interior superposition rather than a single pure state.

**Imported from standard physics and standard mathematics.** The Kadison–Schwarz contraction of unital completely positive maps, and hence the monotonicity of the entropy under a coarse-graining; the classification of conditional expectations onto commutative subalgebras; the minimum-ensemble theorem $\mathcal{S}(\tilde{\rho}) = \min_w H(w)$; and the identification of the dimensionless functional with the physical thermodynamic entropy through the factor $k_B$. None of these is re-derived here; they are transcribed, and they are the same theorems that give the Gibbs and Boltzmann entropies their classical meaning.

**Not supplied.** The framework does not select which coarse-graining is physically realised; the pointer axis $\hat{\mathbf{n}}$ is an input to the conditional expectation, not an output of it, for the reason given in the companion article *Decoherence as Idempotent Projection*. It does not derive a dynamics for the environment, and therefore does not derive the rate $\Gamma$. It does not, on a single qubit, support a partition into more than two cells. And it predicts no departure from the classical entropy accounting it reformulates.

## Summary

A coarse-graining of the informational sector is a conditional expectation $\Phi$ on $\mathbb{M}_+$: linear, completely positive, trace-preserving, idempotent and unital. For a single qubit it is the projection onto the states of a commutative subalgebra, and its canonical form is the fully dephasing map along an axis $\hat{\mathbf{n}}$, whose action on the Bloch vector is $\mathbf{r}\mapsto(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}}$.

The **biquaternion entropy functional** is

$$
\mathcal{S}(\tilde{\rho}) = -2\,\mathrm{Sc}\!\left(\tilde{\rho}\log\tilde{\rho}\right)
= -\lambda_+\log\lambda_+ - \lambda_-\log\lambda_- = h(|\mathbf{r}|),
\qquad \lambda_\pm = \tfrac{1}{2}\left(1\pm|\mathbf{r}|\right),
$$

with $0 \le \mathcal{S} \le \log 2$. It is computed from the algebra's logarithm, which exists exactly on the group of units, that is, on the interior of the Bloch ball: the pure states are the zero divisors, and the entropy is singular there and vanishes there.

The functional depends on the state only through its norm form. With $N(\tilde{\rho}) = \tfrac{1}{4}(1-|\mathbf{r}|^2)e_0$,

$$
\mathcal{S}(\tilde{\rho}) = h\!\left(\sqrt{1 - 4\,\mathrm{Sc}\,N(\tilde{\rho})}\right),
$$

so the entropy vanishes exactly on the null (zero-divisor) cone, is maximal at the maximally mixed state, and measures the depth of the state inside the future cone. The natural invariant of the algebra and the information content of the state are one quantity in two readings.

The **coarse-grained entropy** is the functional evaluated on the image, $\mathcal{S}(\Phi(\tilde{\rho}))$; for the pointer conditional expectation it is the binary Shannon entropy $h(|\hat{\mathbf{n}}\cdot\mathbf{r}|)$. Since a unital completely positive map contracts the Bloch ball, $|\mathbf{r}_\Phi|\le|\mathbf{r}|$, the coarse-grained entropy never falls below the fine-grained one, with equality only for states already in the image. The fine-grained entropy is invariant under reversible rotor flow — the biquaternion form of Liouville's theorem — and the increase appears only when a flow and a coarse-graining are composed. That composition is the second law of the sector.

The fine-grained value is also the minimum over all preparations of the state, $\mathcal{S}(\tilde{\rho}) = \min_w H(w)$, so it is the least coarse description the state admits and the correct reference for the accounting. The framework supplies the functional, its geometry, and its monotonicity; it does not supply the pointer axis, the environment, or the rate, and it predicts nothing beyond the classical entropy accounting it reformulates.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian (informational) and anti-Hermitian (material) subspaces |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$ | State of the informational sector, Bloch vector $\mathbf{r}$ |
| $\tilde{P}_\pm(\hat{\boldsymbol{\mu}}) = \tfrac{1}{2}(e_0 \pm i\hat{\boldsymbol{\mu}})$ | Idempotent (pure state, rank-one projector) |
| $\lambda_\pm = \tfrac{1}{2}(1\pm|\mathbf{r}|)$ | Eigenvalues (pointer probabilities) of the state |
| $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$, $\mathrm{Tr}(e_0)=2$ | Trace |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form |
| $N(\tilde{\rho}) = \tfrac{1}{4}(1-|\mathbf{r}|^2)e_0$ | Norm form of a state |
| $\tilde{\rho}^2 - \tilde{\rho} = \tfrac{1}{4}(|\mathbf{r}|^2-1)e_0$ | Deviation from idempotency (mixedness) |
| $\mathrm{Tr}(\tilde{\rho}^2) = \tfrac{1}{2}(1+|\mathbf{r}|^2)$ | Purity |
| $\log\tilde{\rho} = (\log\lambda_+)\tilde{P}_+(\hat{\mathbf{r}}) + (\log\lambda_-)\tilde{P}_-(\hat{\mathbf{r}})$ | Logarithm of a state, $|\mathbf{r}|<1$ |
| $\mathcal{S}(\tilde{\rho}) = -2\,\mathrm{Sc}(\tilde{\rho}\log\tilde{\rho}) = h(|\mathbf{r}|)$ | Biquaternion entropy functional |
| $h(x) = -\tfrac{1+x}{2}\log\tfrac{1+x}{2} - \tfrac{1-x}{2}\log\tfrac{1-x}{2}$ | Binary entropy function |
| $\mathcal{S} = h\!\left(\sqrt{1-4\,\mathrm{Sc}\,N(\tilde{\rho})}\right)$ | Entropy as a function of the norm form |
| $\Phi$ | Coarse-graining (conditional expectation) |
| $\Phi_{\hat{\mathbf{n}}}(\tilde{\rho}) = \tilde{P}_+\tilde{\rho}\tilde{P}_+ + \tilde{P}_-\tilde{\rho}\tilde{P}_-$ | Pointer coarse-graining along $\hat{\mathbf{n}}$ |
| $\mathbf{r}\mapsto(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}}$ | Action of the pointer coarse-graining |
| $\mathcal{S}_{\rm cg}[\tilde{\rho};\Phi] = \mathcal{S}(\Phi(\tilde{\rho}))$ | Coarse-grained entropy |
| $\mathcal{S}_{\rm cg} = h(|\hat{\mathbf{n}}\cdot\mathbf{r}|)$ | Coarse-grained entropy, pointer basis |
| $r_\parallel = \hat{\mathbf{n}}\cdot\mathbf{r}$, $r_\perp(t) = e^{-\Gamma t}r_\perp(0)$, $r(t)^2 = r_\parallel^2 + r_\perp(t)^2$ | Axial and instantaneous transverse components of the dephasing flow |
| $\mathbf{r}\mapsto(1-p)\mathbf{r} + p(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}}$ | Dephasing at strength $p\in[0,1]$ |
| $\dot{\mathcal{S}} = \Gamma (r_\perp(t)^2/r(t))\,\mathrm{artanh}\,r(t)$ | Entropy production rate of continuous dephasing (instantaneous $r_\perp$) |
| $\tilde{U}(t)$, $\tilde{U}\tilde{U}^\dagger = e_0$ | Matrix-unitary rotor (reversible flow) |
| $H(w) = -\sum_a w_a\log w_a$ | Preparation entropy |

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
