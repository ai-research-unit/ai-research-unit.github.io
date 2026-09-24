# __The Native Qubit and the Defining Module of the Biquaternion Algebra__

## Introduction

The companion articles develop a formulation of quantum mechanics in which states and observables are elements of the Hermitian subspace $\mathbb{M}_+$ of the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, and in which the Born rule is the trace pairing $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$. That development presupposes a carrier for the state: a two-dimensional complex vector space on which the elements of $\mathbb{B}$ act. The purpose of this article is to say precisely what that carrier is, and why, in this framework, it is not an additional postulate.

The claim to be established is that the informational unit of the framework — the **qubit** — is the **defining module** of the algebra $\mathbb{B}\cong M_2(\mathbb{C})$: the unique simple left module $S$ on which $\mathbb{B}$ acts faithfully. A complex two-dimensional space is not chosen and then equipped with operators; it is the object the algebra is a matrix algebra *of*. The state vectors are elements of $S$, the rank-one projectors on $S$ are exactly the idempotents of $\mathbb{M}_+$ that have trace one, and the inner product that quantum mechanics requires is the algebra's own trace pairing, restricted to the module.

This is the informational reading of a structural fact. The article does not claim that the biquaternion algebra predicts the existence of a two-state system, nor that it excludes systems of other dimension: it claims that *if* the informational sector is described by $\mathbb{B}$, then its elementary carrier is forced, because an algebra of $2\times2$ complex matrices has exactly one simple module up to isomorphism, and that module is two-dimensional over $\mathbb{C}$. The qubit is native in the sense that it is read off the algebra rather than imposed on it. What is genuinely open is whether the tensor product $\mathbb{B}\otimes\mathbb{B}$, on which the multi-qubit information-theoretic articles of this subcategory depend, is native in the same sense; that question is raised here and left where the companion articles leave it.

The article proceeds as follows. The algebra and its matrix representative are fixed first. Then the defining module is introduced, its simplicity and uniqueness are recorded, and it is shown that the algebra's left regular module is two copies of it. Then the states are placed on the module: the Hermitian elements act as observables, the rank-one idempotents correspond to rays, and the trace pairing becomes the Hilbert-space inner product. Then the geometry of the module's state space is read off the norm form. A section collects what the module supplies and what it does not, and the article closes with the open questions.

## The Algebra and a Matrix Representative

### The biquaternion algebra

The biquaternion algebra is

$$
\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H},
$$

the complexification of the real quaternion algebra $\mathbb{H}$. Its quaternion units are $e_0 = 1, e_1, e_2, e_3$ with

$$
e_0^2 = e_0, \qquad e_k^2 = -e_0 \quad (k=1,2,3), \qquad e_1e_2 = e_3, \quad e_2e_3 = e_1, \quad e_3e_1 = e_2,
$$

and the scalar imaginary is central and is written $i$, with $i^2 = -1$. A general element is

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C},
$$

and the trace is $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q}) = 2Q_0$. The four conjugations of the algebra — quaternion conjugation, complex conjugation, their composition, and the identity — are fixed in *Conventions in the Biquaternion Universe*. For the present purpose only two are needed: the quaternion conjugate $\bar{\tilde{Q}} = Q_0e_0 - Q_1e_1-Q_2e_2-Q_3e_3$, and the Hermitian conjugate

$$
\tilde{Q}^\dagger = \bigl(\bar{\tilde{Q}}\bigr)^{*} = Q_0^{*}e_0 - Q_1^{*}e_1 - Q_2^{*}e_2 - Q_3^{*}e_3 ,
$$

which is an anti-linear involution of the algebra.

### The defining representation

The algebra is isomorphic, as a complex algebra, to the full matrix algebra $M_2(\mathbb{C})$:

$$
\mathbb{B} \;\cong\; M_2(\mathbb{C}), \qquad
e_0 \mapsto I_2, \qquad e_1 \mapsto -i\sigma_1, \qquad e_2 \mapsto -i\sigma_2, \qquad e_3 \mapsto -i\sigma_3,
$$

with $i \mapsto iI_2$ on the central scalar and $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices. The assignment is fixed by *Quantum Mechanics in Biquaternionic Form* and is the one used throughout this subcategory. Two consequences are worth recording:

- the Hermitian basis of $\mathbb{M}_+$, namely $\{e_0, ie_1, ie_2, ie_3\}$, maps to $\{I_2,\sigma_1,\sigma_2,\sigma_3\}$, so the isomorphism sends traceless Hermitian biquaternions to traceless Hermitian matrices;
- the involution $\dagger$ maps to the matrix Hermitian conjugate.

That a complex associative algebra with these generators is isomorphic to $M_2(\mathbb{C})$ is Wedderburn's theorem for $\mathbb{C}$: $\mathbb{B}$ is a finite-dimensional simple complex algebra, hence a full matrix algebra over its unique simple module's endomorphism ring, which here is $\mathbb{C}$.

### The module in components

It is useful to write the correspondence out in components, because every later statement is a component statement in disguise. A biquaternion $\tilde{Q} = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$ maps to

$$
M(\tilde{Q}) = \begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3 \end{pmatrix},
$$

so that the Hermitian element $\tilde{H} = h_0e_0 + i(h_1e_1 + h_2e_2 + h_3e_3)$ with real $h_\mu$ maps to

$$
M(\tilde{H}) = \begin{pmatrix} h_0 + h_3 & h_1 - ih_2 \\ h_1 + ih_2 & h_0 - h_3 \end{pmatrix}
= h_0 I_2 + h_1\sigma_1 + h_2\sigma_2 + h_3\sigma_3 .
$$

Acting on $|u\rangle = (u_1, u_2)^{\mathsf T}\in S$, this is the ordinary Hermitian operator of the two-level system. The rank-one idempotent along the unit direction $\hat{\mu}$ maps to

$$
M\bigl(\tilde{P}_+(\hat{\mu})\bigr) = \tfrac12\begin{pmatrix} 1+\mu_3 & \mu_1 - i\mu_2 \\ \mu_1 + i\mu_2 & 1-\mu_3 \end{pmatrix},
$$

whose image is the ray of the spinor $(\cos\!\frac{\theta}{2}, e^{i\varphi}\sin\!\frac{\theta}{2})^{\mathsf T}$ with $\hat{\mu} = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$. Conversely, given a unit spinor of that form, the algebra element $\tfrac12(e_0 + i\hat{\mu})$ is recovered. The two descriptions carry exactly the same data.

### The Hermitian subspace

The Hermitian and anti-Hermitian subspaces are defined by the involution:

$$
\mathbb{M}_+ = \{\tilde{Q} : \tilde{Q}^\dagger = \tilde{Q}\}, \qquad
\mathbb{M}_- = \{\tilde{Q} : \tilde{Q}^\dagger = -\tilde{Q}\}, \qquad
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_- .
$$

Both are four-dimensional over $\mathbb{R}$, and multiplication by the central $i$ exchanges them, $i\,\mathbb{M}_+ = \mathbb{M}_-$. Elements of the form $\tilde{H} = h_0e_0 + i\mathbf{h}$ with $h_0\in\mathbb{R}$ and $\mathbf{h}\in\mathbb{R}^3$ span $\mathbb{M}_+$; the corresponding matrices are $h_0I_2 + \mathbf{h}\cdot\boldsymbol{\sigma}$, the general Hermitian $2\times2$ matrix. This is the sense in which states and observables live in $\mathbb{M}_+$: $\mathbb{M}_+$ **is** the real vector space of Hermitian operators of the two-level system, carried by the algebra rather than postulated beside it.

## The Defining Module

### The module

Let $S = \mathbb{C}^2$ be the space of column vectors, acted on from the left by $M_2(\mathbb{C})$, hence by $\mathbb{B}$ through the isomorphism above:

$$
\rho_S(\tilde{Q})\,|u\rangle = M(\tilde{Q})\,|u\rangle .
$$

This is the **defining module**, also called the spinor module. It is a left $\mathbb{B}$-module, complex two-dimensional, and its elements are the state vectors of the qubit. The action is the ordinary matrix action; the notation $\rho_S$ records that the module, not the algebra, is the carrier.

Two elementary facts about $S$ govern everything that follows.

**Simplicity.** $S$ has no nontrivial $\mathbb{B}$-submodules. If $|u\rangle\neq0$, the operators $|w\rangle\langle u|$, realized in $\mathbb{B}$, carry $|u\rangle$ to any prescribed $|w\rangle$; hence every nonzero vector generates $S$, and the only submodules are $0$ and $S$. A nonzero vector is therefore *cyclic*.

**Uniqueness.** Every simple left $\mathbb{B}$-module is isomorphic to $S$. For $M_n(\mathbb{C})$ this is the standard classification: the simple left module is the column space, and it is unique up to isomorphism. There is no second two-dimensional carrier, and there is no one- or three-dimensional one.

These two facts are the precise content of the word "native." The framework does not select a two-dimensional Hilbert space from a family of candidates; an algebra isomorphic to $M_2(\mathbb{C})$ has exactly one irreducible representation, and it is on $S$. The qubit is the algebra's own elementary carrier.

### The left regular module

The algebra acts on itself by left multiplication, and this gives a second module worth naming. In a matrix representative the left regular module decomposes as

$$
\mathbb{B} \;\cong\; S \oplus S \qquad (\text{as left } \mathbb{B}\text{-modules}),
$$

the two summands being the minimal left ideals spanned by the first and second columns. Both are isomorphic to $S$; they are the two Peirce components of any complete set of matrix units. This is the algebraic origin of the framework's two-component spinor structure, and it is the reason the algebra, not the module, is four-complex-dimensional. The qubit's state vectors occupy one copy of $S$; the algebra is *two* copies of the same module, which is what allows an operator to mix the two components.

It is worth separating the two uses of the word "state" that this structure produces. A **state vector** is an element of $S$; a **state**, in the quantum-mechanical sense of a statistical description, is a positive trace-one element of $\mathbb{M}_+$, which is an operator on $S$. The vector and the operator are related by the rank-one correspondence of the next section. The framework keeps both, and the distinction is the same one that ordinary quantum mechanics draws between a ket and a density operator.

## States on the Module

### Rank-one idempotents and rays

For $|u\rangle\in S$ with $\langle u|u\rangle = 1$, the rank-one projector $|u\rangle\langle u|$ is an element of $\mathbb{M}_+$ and satisfies

$$
\bigl(|u\rangle\langle u|\bigr)^2 = |u\rangle\langle u|, \qquad \mathrm{Tr}\bigl(|u\rangle\langle u|\bigr) = 1 .
$$

Conversely, every positive trace-one idempotent of $\mathbb{B}$ has rank one and is the projector onto a ray of $S$. Since two unit vectors define the same projector exactly when they differ by a phase, the map

$$
\{\text{rays of } S\} \;\longleftrightarrow\; \{\text{rank-one idempotents of } \mathbb{M}_+\}
$$

is a bijection. This is the biquaternion form of the standard correspondence between pure states and rays.

In the basis of the algebra the pure states are the elements

$$
\tilde{P}_\pm(\hat{\mu}) = \tfrac{1}{2}\bigl(e_0 \pm i\hat{\mu}\bigr), \qquad \hat{\mu}\in\mathbb{R}^3,\ |\hat{\mu}|=1 ,
$$

the two antipodal idempotents of the direction $\hat{\mu}$. Each satisfies $\tilde{P}_\pm^2 = \tilde{P}_\pm$ and $\mathrm{Tr}(\tilde{P}_\pm)=1$, and the matrix image is $\tfrac12(I_2 \pm \hat{\mu}\cdot\boldsymbol{\sigma})$. The family of rays is therefore parametrized by the unit sphere $S^2$, and the two idempotents of a direction are the antipodal points of the Bloch sphere.

### The general state and the trace pairing

A general state is a positive trace-one element of $\mathbb{M}_+$,

$$
\tilde{\rho} = \tfrac{1}{2}\bigl(e_0 + i\mathbf{r}\bigr), \qquad \mathbf{r}\in\mathbb{R}^3,
$$

positive exactly when $|\mathbf{r}|\leq1$. It is the operator on $S$ with matrix $\tfrac12(I_2 + \mathbf{r}\cdot\boldsymbol{\sigma})$. The **trace pairing** between a state and an observable $\tilde{H}\in\mathbb{M}_+$ is

$$
\mathrm{Tr}(\tilde{\rho}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{\rho}\tilde{H}),
$$

and for a pure state $\tilde{P} = |u\rangle\langle u|$ it reproduces the module inner product,

$$
\mathrm{Tr}(\tilde{P}\tilde{H}) = \langle u|\hat{H}|u\rangle ,
$$

where $\hat{H}$ is the matrix image of $\tilde{H}$. This identity is the bridge between the two descriptions: the Born rule of the algebra is the ordinary expectation value on the module. Its derivation from the trace was given in *The Born Rule as a Trace Formula — Derivation and Comparison*, and it requires nothing beyond the fact that the trace of a rank-one operator is the inner product of its two vectors.

### Mixed states and the density-operator correspondence

A general state $\tilde\rho$ is a convex combination of pure states,

$$
\tilde{\rho} = \lambda_+\,\tilde{P}_+(\hat{\mathbf{r}}) + \lambda_-\,\tilde{P}_-(\hat{\mathbf{r}}),
\qquad \lambda_\pm = \tfrac{1}{2}\bigl(1\pm|\mathbf{r}|\bigr),
$$

when $\mathbf{r}\neq0$, and is the maximally mixed state $\tfrac12 e_0$ when $\mathbf{r}=0$. This is the spectral decomposition on the module: the two eigenvectors are the rays of $\hat{\mathbf{r}}$ and $-\hat{\mathbf{r}}$. The correspondence is exactly the ordinary one between a density operator and its eigenvectors, expressed in the algebra. The Bloch ball is the image of the trace-one positive cone, and its boundary is the set of rank-one projectors; the companion article *The Bloch Ball as the Trace-One Slice of the Future Light Cone* develops that geometry from the norm form, and it is recalled below only as far as the module requires.

## The Geometry of the Module

### The norm form on the module

The norm form of the algebra is

$$
N(\tilde{Q}) = \tilde{Q}\,\bar{\tilde{Q}} = \sum_{\mu=0}^{3} Q_\mu^2 .
$$

On $\mathbb{M}_+$, writing $\tilde{Q} = q_0e_0 + i\mathbf{q}$ with real $q_0,\mathbf{q}$, it evaluates to

$$
N(\tilde{Q}) = \bigl(q_0^2 - |\mathbf{q}|^2\bigr)e_0 ,
$$

which is a real scalar. Positivity of the operator is the non-negativity of the norm form together with $q_0\geq0$: the norm form is the determinant of the matrix image, $N(\tilde{Q}) = \det M(\tilde{Q})\,e_0$, so it vanishes on the boundary of the positive cone as well as outside it, and only the sign of $q_0$ selects the future cone. For a state

$$
N(\tilde{\rho}) = \tfrac{1}{4}\bigl(1 - |\mathbf{r}|^2\bigr)e_0 .
$$

The norm form therefore measures the departure of a state from the boundary of the Bloch ball, and it vanishes precisely on the rank-one idempotents — the rays of the module. On the pure states the algebra's norm form has a nonzero kernel; that degenerate cone is the module's set of rays, and it is the geometric reason the rank-one idempotents are the zero divisors of $\mathbb{M}_+$.

### Tomography on the module

The module's state is fixed by the three expectations of the coordinate observables $ie_k$, $k=1,2,3$:

$$
r_k = \mathrm{Tr}(\tilde{\rho}\,ie_k) = \langle \sigma_k\rangle ,
$$

so the state is reconstructed from three real numbers obtained by measuring the three Pauli observables. Equivalently, since

$$
p_k^{\pm} = \mathrm{Tr}\bigl(\tilde{\rho}\,\tilde{P}_\pm(\hat{e}_k)\bigr) = \tfrac12\bigl(1 \pm r_k\bigr),
$$

the three pairs of outcome probabilities determine $\mathbf{r}$ and hence the state. This is the elementary tomographic completeness of the three coordinate measurements, and it is the module-level content of the mutually unbiased bases of a qubit. The module carries no further state parameters: it has complex dimension two, its rays are parametrized by two real angles, and its states by three real numbers.

## What the Module Supplies and What It Does Not

**What it supplies.**

- **The carrier is forced, not chosen.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has a unique simple left module $S=\mathbb{C}^2$, so the elementary informational unit is two-dimensional over $\mathbb{C}$ and is read off the algebra.
- **The inner product is native.** The Hilbert-space inner product on $S$ is the trace pairing of the algebra, $\langle u|v\rangle = \mathrm{Tr}(|u\rangle\langle v|)$; it is not an independent axiom.
- **The pure states are the module's rays.** The rank-one idempotents of $\mathbb{M}_+$ correspond bijectively to the rays of $S$, and their matrix images are the rank-one Hermitian projectors.
- **The Born rule is a module pairing.** $\mathrm{Tr}(\tilde{P}\tilde{H}) = \langle u|\hat{H}|u\rangle$; the algebra's trace formula and the module expectation value are the same operation.
- **The state geometry is the norm form's cone slice.** The Bloch ball is the trace-one positive slice of $\mathbb{M}_+$, its boundary is the zero-divisor cone of the norm form, and the rays are its extreme points.

**What it does not supply.**

- **The dimension of composite systems.** The defining module is the single-qubit carrier. The two-qubit arena is the tensor product $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$, whose module $\mathbb{C}^4$ is *not* the defining module of $\mathbb{B}$; it is the defining module of the larger algebra. That the tensor product is the correct composition rule is an additional structure, identified as an open question in *Entangled Subsystems in the Biquaternion Framework*.
- **Systems of other dimension.** A qutrit would require $M_3(\mathbb{C})$, which is not isomorphic to $\mathbb{B}$. The framework as developed here describes two-level systems; whether it can be extended is a separate question.
- **A dynamics.** The module fixes the kinematics — carriers, states, observables, probabilities — and says nothing about which Hamiltonian acts.
- **An interpretation.** That the module is the algebra's own carrier is a structural fact; that it is a physical informational sector is the interpretive hypothesis of *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, and it is not required by anything in this article.

## Open Questions

**1. The tensor product.** Is $\mathbb{B}\otimes\mathbb{B}$ native to the framework, or is it imposed? The defining module of $\mathbb{B}\otimes\mathbb{B}$ is $\mathbb{C}^4$, and the composition of two qubits into one four-level system is an assumption about how subsystems combine. This is the central open structural question for the informational reading, and it is inherited from the companion articles on entanglement.

**2. The doubling of the regular module.** The left regular module is $S\oplus S$. The qubit uses one copy. Does the second copy have informational content — a chirality, a superselection rule, or nothing — or is it a redundancy of the matrix representative? *Spin-1/2 Quantum Mechanics in Biquaternionic Form* develops the spinor side of this question.

**3. Higher-dimensional modules.** The algebra's simple module is two-dimensional, but its *projective* representations and its tensor powers are not. Which of those are physically available is the module-theoretic form of the question whether the framework admits qutrits and larger systems.

**4. The status of the inner product at the boundary.** The trace pairing is positive definite on $\mathbb{M}_+$ but the norm form is degenerate on the rank-one idempotents. The relation between these two pairings — one the Born rule, the other the light-cone structure — is the geometric thread running through this subcategory, and it is pursued in the entropy and positive-cone articles that follow.

**5. Empirical contact.** As for the whole framework, a reformulation of the qubit's carrier predicts nothing that ordinary quantum mechanics does not. The module's nativeness is a statement about how the formalism hangs together, not a new observable.

## Summary

The elementary informational unit of the biquaternion framework is the defining module of the algebra. Because $\mathbb{B}\cong M_2(\mathbb{C})$ is a simple finite-dimensional complex algebra, it has a unique simple left module $S=\mathbb{C}^2$, the column space, and every irreducible representation is equivalent to the action on $S$. The qubit is therefore native to the algebra: it is what the algebra is a matrix algebra of, not a Hilbert space adjoined to it.

On the module, the elements of $\mathbb{M}_+$ act as Hermitian operators; the rank-one idempotents $\tilde{P}_\pm(\hat{\mu}) = \tfrac12(e_0\pm i\hat{\mu})$ correspond bijectively to the rays of $S$, and are exactly the pure states; the trace pairing $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is the Born rule and coincides with the module expectation value $\langle u|\hat{H}|u\rangle$. A general state $\tilde{\rho} = \tfrac12(e_0+i\mathbf{r})$ is a positive trace-one element with spectral decomposition into two rays, and the norm form $N(\tilde{\rho}) = \tfrac14(1-|\mathbf{r}|^2)e_0$ vanishes exactly on the rays, so that the pure states are the zero divisors of $\mathbb{M}_+$ and the Bloch ball is the trace-one slice of the positive cone. The left regular module is $\mathbb{B}\cong S\oplus S$, an algebraic doubling whose informational content is left open.

What the module does not supply is the composition rule for several qubits: the tensor product $\mathbb{B}\otimes\mathbb{B}$ and its four-dimensional module are an additional structure. That, and not the definition of the unit, is where the framework's informational assumptions become substantive.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion units, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_+$ | Hermitian subspace (states and observables) |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (generators of reversible evolution) |
| $S = \mathbb{C}^2$ | Defining (spinor) module of $\mathbb{B}$ |
| $\rho_S$ | The defining representation of $\mathbb{B}$ on $S$ |
| $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$ | Trace |
| $\tilde{Q}^\dagger$ | Hermitian conjugate (anti-linear involution) |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form |
| $\tilde{P}_\pm(\hat{\mu}) = \tfrac12(e_0\pm i\hat{\mu})$ | Rank-one idempotents (pure states) |
| $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$ | State with Bloch vector $\mathbf{r}$, $|\mathbf{r}|\le1$ |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H}) = \langle u|\hat{H}|u\rangle$ | Trace pairing (Born rule) |
| $r_k = \mathrm{Tr}(\tilde{\rho}\,ie_k)$ | Bloch components (tomography) |
| $N(\tilde{\rho}) = \tfrac14(1-|\mathbf{r}|^2)e_0$ | Norm form of a state |

## Further Reading

- F. W. Anderson and K. R. Fuller, *Rings and Categories of Modules* (Springer, 1992), for the left regular module of $M_n(\mathbb{C})$, its simple modules, and the uniqueness of the defining module.
- I. N. Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for Wedderburn's structure theorem for finite-dimensional simple algebras.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the biquaternion algebra, its units, and its identification with $M_2(\mathbb{C})$.
- W. E. Baylis, *Electrodynamics: A Modern Geometric Approach* (Birkhäuser, 1999), for the complex-quaternion formalism and its Hermitian subspaces.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the qubit, the density operator, and the correspondence between pure states and rays.
- A. Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for the geometry of the Bloch ball and the statistical interpretation of the trace pairing.
- J. S. Bell, "On the problem of hidden variables in quantum mechanics," *Reviews of Modern Physics* **38** (1966) 447–452, for the noncontextual hidden-variable model of a single qubit, which illustrates the special position of the two-dimensional module.
- The companion articles of this series: *Introduction to the Biquaternion Universe*, *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, *Conventions in the Biquaternion Universe*, *Quantum Mechanics in Biquaternionic Form*, *The Born Rule as a Trace Formula — Derivation and Comparison*, *The Bloch Ball as the Trace-One Slice of the Future Light Cone*, and *Spin-1/2 Quantum Mechanics in Biquaternionic Form*.
