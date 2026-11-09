# __The Native Qubit and the Defining Module of the Biquaternion Algebra__

## Introduction

The companion articles develop a formulation of quantum physics in which states and observables are elements of the Hermitian subspace $\mathbb{B}_{\Psi}$ of the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, and in which the Born rule is the normalised Hermitian form $\langle\tilde{R}_{\Psi,1},\tilde{R}_{\Psi,2}\rangle_{*}/\langle\tilde{R}_{\Psi,1},e_t\rangle_{*}$, whose $2\times2$ reading is $\mathrm{Tr}(\tilde{R}_{\Psi,1}\tilde{R}_{\Psi,2}^{*})=2\,\mathrm{Sc}(\tilde{R}_{\Psi,1}\tilde{R}_{\Psi,2}^{*})$. That development presupposes a carrier for the state: a two-dimensional complex vector space on which the elements of $\mathbb{B}$ act. The purpose of this article is to say precisely what that carrier is, and why, in this framework, it is not an additional postulate.

The claim to be established is that the informational unit of the framework — the **qubit** — is the **defining module** of the algebra $\mathbb{B}\cong M_2(\mathbb{C})$: the unique simple left module $S$ on which $\mathbb{B}$ acts faithfully. A complex two-dimensional space is not chosen and then equipped with operators; it is the object the algebra is a matrix algebra *of*. The state vectors are elements of $S$; the rank-one projectors on $S$ correspond exactly to the idempotents of $\mathbb{B}_{\Psi}$ that are normalised by $\langle\tilde\Pi,e_t\rangle_{*}=\tfrac12$ (trace one in the image); and the inner product that quantum physics requires is the algebra's own Hermitian form, whose matrix reading is the trace pairing, restricted to the module.

This is the informational interpretation of a structural fact. The article does not claim that the biquaternion algebra predicts the existence of a two-state system, nor that it excludes systems of other dimension: it claims that *if* the informational sector is described by $\mathbb{B}$, then its elementary carrier is forced, because an algebra of $2\times2$ complex matrices has exactly one simple module up to isomorphism, and that module is two-dimensional over $\mathbb{C}$. The qubit is native in the sense that it is read off the algebra rather than imposed on it. What is genuinely open is whether the tensor product $\mathbb{B}\otimes\mathbb{B}$, on which the multi-qubit information-theoretic articles of this subcategory depend, is native in the same sense. The carrier is native and the composition is not, and the second statement is not a matter of taste: the criterion that decides whether two qubits are separate is the determinant of the amplitude array, a polynomial of the tensor product that the algebra does not carry, as the section *The Composition Rule and the Rank-One Condition* shows.

The article proceeds as follows. The algebra and its matrix representative are fixed first. Then the defining module is introduced, its simplicity and uniqueness are recorded, and it is shown that the algebra's left regular module is two copies of it. Then the states are placed on the module: the Hermitian elements act as observables, the rank-one idempotents correspond to rays, and the Hermitian form becomes the Hilbert-space inner product, read as the trace pairing. Then the geometry of the module's state space is read off the biquaternion norm. A section collects what the module supplies and what it does not. A further section then tests the composition rule itself, identifies the invariant that decides separability, and shows that it is not a form of the algebra. The article closes with the open questions.

## The Algebra and a Matrix Representative

### The biquaternion algebra

The biquaternion algebra is

$$
\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H},
$$

the complexification of the real quaternion algebra $\mathbb{H}$. Its quaternion units are $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with

$$
e_t^2 = e_t, \qquad \vec e_\eta^2 = -e_t \quad (\eta=1,2,3), \qquad \vec e_x\vec e_y = \vec e_z, \quad \vec e_y\vec e_z = \vec e_x, \quad \vec e_z\vec e_x = \vec e_y,
$$

and the scalar imaginary is central and is written $i$, with $i^2 = -1$. A general element is

$$
\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z, \qquad Q_\mu \in \mathbb{C},
$$

and the trace is $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q}) = 2Q_t$. The trace is not intrinsic to the biquaternion: it is the $2\times2$ matrix reading, $\mathrm{Tr}=\mathrm{tr}\circ\mathsf{M}_2$, whereas $\mathrm{Sc}(\tilde Q)$ is defined for every biquaternion. The four conjugations of the algebra — quaternion conjugation, complex conjugation, their composition, and the identity — are fixed in *Algebra and Element Conventions*. For the present purpose only two are needed: the quaternion conjugate $\tilde{Q}^{\natural} = Q_te_t - Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z$, and the Hermitian conjugate

$$
\tilde{Q}^{*} = \bigl(\tilde{Q}^{\natural}\bigr)^{*} = Q_t^{*}e_t - Q_x^{*}\vec e_x - Q_y^{*}\vec e_y - Q_z^{*}\vec e_z ,
$$

which is an anti-linear involution of the algebra.

### The defining representation

The algebra is isomorphic, as a complex algebra, to the full matrix algebra $M_2(\mathbb{C})$:

$$
\mathbb{B} \;\cong\; M_2(\mathbb{C}), \qquad
e_t \mapsto I_2, \qquad \vec e_x \mapsto -i\sigma_1, \qquad \vec e_y \mapsto -i\sigma_2, \qquad \vec e_z \mapsto -i\sigma_3,
$$

with $i \mapsto iI_2$ on the central scalar and $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices. The assignment is fixed by *Quantum Physics in Biquaternionic Form* and is the one used throughout this subcategory. Two consequences are worth recording:

- the Hermitian basis of $\mathbb{B}_{\Psi}$, namely $\{e_t, i\vec e_x, i\vec e_y, i\vec e_z\}$, maps to $\{I_2,\sigma_1,\sigma_2,\sigma_3\}$, so the isomorphism sends traceless Hermitian biquaternions to traceless Hermitian matrices;
- the involution ${}^{*}$ maps to the matrix Hermitian conjugate.

That a complex associative algebra with these generators is isomorphic to $M_2(\mathbb{C})$ is Wedderburn's theorem for $\mathbb{C}$: $\mathbb{B}$ is a finite-dimensional simple complex algebra, hence a full matrix algebra over its unique simple module's endomorphism ring, which here is $\mathbb{C}$.

### The module in components

It is useful to write the correspondence out in components, because every later statement is a component statement in disguise. A biquaternion $\tilde{Q} = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ maps to

$$
M(\tilde{Q}) = \begin{pmatrix} Q_t - iQ_3 & -iQ_1 - Q_y \\ -iQ_1 + Q_y & Q_t + iQ_3 \end{pmatrix},
$$

so that the Hermitian element $\tilde R_\Psi = r_t\,e_t + i(r'_x\vec e_x + r'_y\vec e_y + r'_z\vec e_z)$ with real $h_\mu$ maps to

$$
M(\tilde R_\Psi) = \begin{pmatrix} r_t + r'_z & r'_x - ir'_y \\ r'_x + ir'_y & r_t - r'_z \end{pmatrix}
= r_t I_2 + r'_x\sigma_1 + r'_y\sigma_2 + r'_z\sigma_3 .
$$

Acting on $|u\rangle = (u_x, u_y)^{\mathsf T}\in S$, this is the ordinary Hermitian operator of the two-level system. The rank-one idempotent along the unit direction $\vec u$ maps to

$$
M\bigl(\tilde\Pi_1(\vec u)\bigr) = \tfrac12\begin{pmatrix} 1+\mu_3 & \mu_1 - i\mu_2 \\ \mu_1 + i\mu_2 & 1-\mu_3 \end{pmatrix},
$$

whose image is the ray of the spinor $(\cos\!\frac{\theta}{2}, \exp(i\theta_{\mathrm{azm}})\sin\!\frac{\theta}{2})^{\mathsf T}$ with $\vec u = (\sin\theta\cos\theta_{\mathrm{azm}}, \sin\theta\sin\theta_{\mathrm{azm}}, \cos\theta)$. Conversely, given a unit spinor of that form, the algebra element $\tfrac12(e_t + i\vec u)$ is recovered. The two descriptions carry exactly the same data.

### The Hermitian subspace

The Hermitian and anti-Hermitian subspaces are defined by the involution:

$$
\mathbb{B}_{\Psi} = \{\tilde{Q} : \tilde{Q}^{*} = \tilde{Q}\}, \qquad
\mathbb{B}_{\Phi} = \{\tilde{Q} : \tilde{Q}^{*} = -\tilde{Q}\}, \qquad
\mathbb{B} = \mathbb{B}_{\Psi} \oplus \mathbb{B}_{\Phi} .
$$

Both are four-dimensional over $\mathbb{R}$, and multiplication by the central $i$ exchanges them, $i\,\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$. Elements of the form $\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi$ with $r_t\in\mathbb{R}$ and $\vec r_\Psi\in\mathbb{R}^3$ span $\mathbb{B}_{\Psi}$; the corresponding matrices are $r_t\,I_2 + \vec r_\Psi\cdot\boldsymbol{\sigma}$, the general Hermitian $2\times2$ matrix. This is the sense in which states and observables live in $\mathbb{B}_{\Psi}$: $\mathbb{B}_{\Psi}$ **is** the real vector space of Hermitian operators of the two-level system, carried by the algebra rather than postulated beside it.

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
\boxed{\;\mathbb{B} \;\cong\; S \oplus S \qquad (\text{as left } \mathbb{B}\text{-modules})\;},
$$

the two summands being the minimal left ideals spanned by the first and second columns. Both are isomorphic to $S$; they are the two Peirce components of any complete set of matrix units. This is the algebraic origin of the framework's two-component spinor structure, and it is the reason the algebra, not the module, is four-complex-dimensional. The qubit's state vectors occupy one copy of $S$; the algebra is *two* copies of the same module, which is what allows an operator to mix the two components.

It is worth separating the two uses of the word "state" that this structure produces. A **state vector** is an element of $S$; a **state**, in the quantum-mechanical sense of a statistical description, is a positive element of $\mathbb{B}_{\Psi}$ normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12$ (trace one in the $2\times2$ image), which is an operator on $S$. The vector and the operator are related by the rank-one correspondence of the next section. The framework keeps both, and the distinction is the same one that ordinary quantum physics draws between a ket and a density operator.

## States on the Module

### Rank-one idempotents and rays

For $|u\rangle_{*}\in S$ with $\langle u|u\rangle = 1$, the rank-one idempotent $|u\rangle\langle u|$ is an element of $\mathbb{B}_{\Psi}$ and satisfies

$$
\bigl(|u\rangle\langle u|\bigr)^2 = |u\rangle\langle u|, \qquad 2\bigl\langle |u\rangle\langle u|,e_t\bigr\rangle_{*} = 1, \qquad \mathrm{Tr}\bigl(|u\rangle\langle u|\bigr) = 1 .
$$

Conversely, every positive normalised idempotent of $\mathbb{B}$ (trace one in the image) has rank one and is the projector onto a ray of $S$. Since two unit vectors define the same projector exactly when they differ by a phase, the map

$$
\boxed{\;\{\text{rays of } S\} \;\longleftrightarrow\; \{\text{rank-one idempotents of } \mathbb{B}_{\Psi}\}\;}
$$

is a bijection. This is the biquaternion form of the standard correspondence between pure states and rays.

In the basis of the algebra the pure states are the elements

$$
\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}\bigl(e_t \pm i\vec u\bigr), \qquad \vec u\in\mathbb{R}^3,\ |\vec u|=1 ,
$$

the two antipodal idempotents of the direction $\vec u$. Each satisfies $\tilde\Pi_{1,2}^2 = \tilde\Pi_{1,2}$ and $\langle\tilde\Pi_{1,2},e_t\rangle_{*}=\tfrac12\langle e_t\rangle$, and the matrix image is $\tfrac12(I_2 \pm \vec u\cdot\boldsymbol{\sigma})$. The family of rays is therefore parametrized by the unit sphere $S^2$, and the two idempotents of a direction are the antipodal points of the Bloch sphere.

### The general state and the Hermitian form

A general state is a positive element of $\mathbb{B}_{\Psi}$ normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12\langle e_t\rangle_{*}$,

$$
\tilde{Ϛ}_{\Psi} = \tfrac{1}{2}\bigl(e_t + i\vec r\bigr), \qquad \vec r\in\mathbb{R}^3,
$$

positive exactly when $|\vec r|\leq1$. It is the operator on $S$ with matrix $\tfrac12(I_2 + \vec r\cdot\boldsymbol{\sigma})$. The **Hermitian form** between a state and an observable $\tilde R_\Psi\in\mathbb{B}_{\Psi}$ is

$$
\langle\tilde{Ϛ}_{\Psi},\tilde R_\Psi\rangle_{*} = \mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde R_\Psi^{*}),
$$

and the Born weight is $\langle\tilde{Ϛ}_{\Psi},\tilde R_\Psi\rangle_{*}/\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}$. For a pure state $\tilde\Pi = |u\rangle\langle u|$ it reproduces the module inner product,

$$
\boxed{\;\frac{\langle\tilde\Pi,\tilde R_\Psi\rangle_{*}}{\langle\tilde\Pi,e_t\rangle_{*}} = \langle u|H|u\rangle\;},
$$

where $H$ is the matrix image of $\tilde R_\Psi$. On $\mathbb{B}_{\Psi}$ the star is inert, so the same number is $\mathrm{Sc}(\tilde\Pi\tilde R_\Psi)/\mathrm{Sc}(\tilde\Pi)$, the plain scalar. The normalisation is $\langle\tilde\Pi,e_t\rangle_{*}=\tfrac12$; the trace appears only as its $2\times2$ reading, $\operatorname{Tr}(\tilde\Pi)=1$, and then $\mathrm{Tr}(\tilde\Pi\tilde R_\Psi^{*}) = \langle u|H|u\rangle$. This identity is the bridge between the two descriptions: the Born rule of the algebra is the normalised Hermitian form, read on the module as the ordinary expectation value. Its derivation from the Hermitian form was given in *The Born Rule from the Hermitian Form — Derivation and Comparison*, and it requires nothing beyond the fact that the form is the scalar part of the product.

### Mixed states and the density-operator correspondence

A general state $\tilde{Ϛ}_{\Psi}$ is a convex combination of pure states,

$$
\tilde{Ϛ}_{\Psi} = \lambda_+\,\tilde\Pi_1(\vec u_r) + \lambda_-\,\tilde\Pi_2(\vec u_r),
\qquad \lambda_\pm = \tfrac{1}{2}\bigl(1\pm|\vec r|\bigr),
$$

when $\vec r\neq0$, and is the maximally mixed state $\tfrac12 e_t$ when $\vec r=0$. This is the spectral decomposition on the module: the two eigenvectors are the rays of $\vec u_r$ and $-\vec u_r$. The correspondence is exactly the ordinary one between a density operator and its eigenvectors, expressed in the algebra. The Bloch ball is the image of the trace-one positive cone, and its boundary is the set of rank-one projectors; the companion article *The Bloch Ball as the Normalised Slice of the Future Light Cone* develops that geometry from the biquaternion norm, and it is recalled below only as far as the module requires.

## The Geometry of the Module

### The biquaternion norm on the module

The biquaternion norm of the algebra is

$$
\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\,\tilde{Q}^{\natural} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu^2 .
$$

On $\mathbb{B}_{\Psi}$, writing $\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi$ with real $r_t,\vec r_\Psi$, it evaluates to

$$
\langle\tilde R_\Psi\rangle_{\natural} = \bigl(r_t^2 - |\vec r_\Psi|^2\bigr)e_t ,
$$

which is a real scalar. Positivity of the operator is the non-negativity of the biquaternion norm together with $r_t\geq0$: the biquaternion norm is the determinant of the matrix image, $\langle\tilde R_\Psi\rangle_{\natural} = \det M(\tilde R_\Psi)\,e_t$, so it vanishes on the boundary of the positive cone as well as outside it, and only the sign of $r_t$ selects the future cone. For a state

$$
\boxed{\;\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural} = \tfrac{1}{4}\bigl(1 - |\vec r|^2\bigr)e_t\;}.
$$

The biquaternion norm therefore measures the departure of a state from the boundary of the Bloch ball, and it vanishes precisely on the rank-one idempotents — the rays of the module. On the pure states the algebra's biquaternion norm has a nonzero kernel; that degenerate cone is the module's set of rays, and it is the geometric reason the rank-one idempotents are the zero divisors of $\mathbb{B}_{\Psi}$.

### Tomography on the module

The module's state is fixed by the three expectations of the coordinate observables $i\vec e_\eta$, $\eta=1,2,3$:

$$
r_\eta = \frac{\langle\tilde{Ϛ}_{\Psi},i\vec e_\eta\rangle_{*}}{\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}} = \langle \sigma_\eta\rangle_{*} ,
$$

so the state is reconstructed from three real numbers obtained by measuring the three Pauli observables. Equivalently, since

$$
p_\eta^{\pm} = \frac{\langle\tilde{Ϛ}_{\Psi},\tilde\Pi_{1,2}(\vec u_\eta)\rangle_{*}}{\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}} = 2\,\mathrm{Sc}\bigl(\tilde{Ϛ}_{\Psi}\,\tilde\Pi_{1,2}(\vec u_\eta)^{*}\bigr) = \tfrac12\bigl(1 \pm r_\eta\bigr),
$$

the three pairs of outcome probabilities determine $\vec r$ and hence the state; the trace form $\mathrm{Tr}(\tilde{Ϛ}_{\Psi}\,\tilde\Pi_{1,2}(\vec u_\eta)^{*})=\mathrm{Tr}(\tilde{Ϛ}_{\Psi}\,\tilde\Pi_{1,2}(\vec u_\eta))$ is the $2\times2$ reading, with $\operatorname{Tr}(\tilde{Ϛ}_{\Psi})=1$; the star is inert and the unstarred trace is real and non-negative. This is the elementary tomographic completeness of the three coordinate measurements, and it is the module-level content of the mutually unbiased bases of a qubit. The module carries no further state parameters: it has complex dimension two, its rays are parametrized by two real angles, and its states by three real numbers.

## What the Module Supplies and What It Does Not

**What it supplies.**

- **The carrier is forced, not chosen.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has a unique simple left module $S=\mathbb{C}^2$, so the elementary informational unit is two-dimensional over $\mathbb{C}$ and is read off the algebra.
- **The inner product is native.** The Hilbert-space inner product on $S$ is the Hermitian form of the algebra, whose $2\times2$ reading is the trace, $\langle u|v\rangle = 2\,\mathrm{Sc}(|v\rangle\langle u|)=\mathrm{Tr}(|v\rangle\langle u|)$; it is not an independent axiom.
- **The pure states are the module's rays.** The rank-one idempotents of $\mathbb{B}_{\Psi}$ correspond bijectively to the rays of $S$, and their matrix images are the rank-one Hermitian projectors.
- **The Born rule is a module pairing.** The normalised Hermitian form and the module expectation value are the same operation; in the $2\times2$ image it reads $\mathrm{Tr}(\tilde\Pi\tilde R_\Psi^{*}) = \langle u|H|u\rangle$, with the trace used only to normalise the state.
- **The state geometry is the biquaternion norm's cone slice.** The Bloch ball is the normalised positive slice of $\mathbb{B}_{\Psi}$ (trace one in the image), its boundary is the zero-divisor cone of the biquaternion norm, and the rays are its extreme points.

**What it does not supply.**

- **The dimension of composite systems.** The defining module is the single-qubit carrier. The two-qubit arena is the tensor product $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$, whose module $\mathbb{C}^4$ is *not* the defining module of $\mathbb{B}$; it is the defining module of the larger algebra. That the tensor product is the correct composition rule is an additional structure, identified as an open question in *Entangled Subsystems in the Biquaternion Framework* and analysed in the section *The Composition Rule and the Rank-One Condition* above.
- **Systems of other dimension.** A qutrit would require $M_3(\mathbb{C})$, which is not isomorphic to $\mathbb{B}$. The framework as developed here describes two-level systems; whether it can be extended is a separate question.
- **A dynamics.** The module fixes the kinematics — carriers, states, observables, probabilities — and says nothing about which Hamiltonian acts.
- **An interpretation.** That the module is the algebra's own carrier is a structural fact; that it is a physical informational sector is the interpretive hypothesis of *The Informational Sector: States, Observables and Probability*, and it is not required by anything in this article.

## The Composition Rule and the Rank-One Condition

The first of the open questions below can be given a partial answer, and the answer is negative in a sense precise enough to be computed. The algebra forces its carrier, because it is a matrix algebra and has one simple module. It does not force how two carriers combine. And when the combination is supplied, the criterion that separates the products from the rest is a condition on $\mathbb{C}^2\otimes\mathbb{C}^2$ as a **vector space**, carried by a polynomial that the algebra does not possess.

### The amplitude array and its determinant

A two-qubit state vector is $|\tilde{Ξ}_{\mathrm{sp}}\rangle=\sum_{A_1,A_2}c_{A_1A_2}|A_1A_2\rangle$ with $A_1,A_2\in\{0,1\}$. Its four amplitudes form the array $\mathbf c=(c_{A_1A_2})$, and the linear isomorphism $\mathbb{C}^2\otimes\mathbb{C}^2\to\mathrm{End}(\mathbb{C}^2)$ sends $|u\rangle\otimes|v\rangle$ to the rank-one operator $|u\rangle\langle v|$. The determinant of the array,

$$
\mathrm{Det}(\mathbf c)=c_{00}c_{11}-c_{01}c_{10},
$$

is the **hyperdeterminant of format $2\times2$**, the generator of the polynomial invariants of $\mathbb{C}^2\otimes\mathbb{C}^2$ under the local group $SL(2,\mathbb{C})\times SL(2,\mathbb{C})$.

**Proposition (separability is the rank-one condition).** $|\tilde{Ξ}_{\mathrm{sp}}\rangle$ is a product $|u\rangle\otimes|v\rangle$ if and only if $\operatorname{rank}\mathbf c=1$, if and only if $\mathrm{Det}(\mathbf c)=0$.

**Proof.** A product gives $\mathbf c=|u\rangle\langle v|$, of rank one. Conversely an array of rank one is $|u\rangle\langle v|$ for a nonzero column $|u\rangle$ and a nonzero row $\langle v|$, and the corresponding vector is $|u\rangle\otimes|v\rangle$. An array has rank at most one exactly when its $2\times2$ minor vanishes, and there is one minor.

The condition is one quadratic equation in $\mathbb{P}^3$, so the product states form a quadric surface, the Segre variety $\mathbb{P}^1\times\mathbb{P}^1$ that *Projective Geometry* records as the low-dimensional model of the Klein quadric. The vanishing of the single $2\times2$ minor is the rank-one condition of that embedding — the same determinantal phenomenon that, for a $2\times4$ matrix, gives the single Plücker relation cutting out the Klein quadric, as *Grassmannians and Stiefel Manifolds* states it. This surface is not the Segre variety of *The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$*, which at $n=2$ lives in $\mathbb{P}^{15}$: the two are one construction applied to different tensor products. The same condition is recorded numerically, in the component order $c_1,c_2,c_3,c_4$, in *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*, where $c_1c_4-c_2c_3=0$ is the test for a product state and $2\lvert c_1c_4-c_2c_3\rvert$ the concurrence. What is added here is the name of the object that carries the test and the conclusion that follows from it.

**Concurrence is the modulus of the determinant.** For a normalised state the concurrence is

$$
\frac{2\,\lvert\mathrm{Det}(\mathbf c)\rvert}{\sum_{A_1,A_2}\lvert c_{A_1A_2}\rvert^2}=\frac{2\sigma_1\sigma_2}{\sigma_1^2+\sigma_2^2},
$$

with $\sigma_1,\sigma_2$ the singular values of $\mathbf c$, and it equals $2\sqrt{\det\rho_1}$ for the reduced state $\rho_1$ of the first qubit. It is named in words and carries no glyph here, because $\mathcal{C}$ is already the charge conjugation of the spinor module in *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, and one letter names one object of the subcategory. The determinant is therefore not an auxiliary quantity: it *is* the entanglement measure of a pure two-qubit state, up to normalisation. On a hundred random normalised states the three expressions agreed to $5.6\times10^{-16}$, and on a hundred product states $\lvert\mathrm{Det}(\mathbf c)\rvert$ did not exceed $5.5\times10^{-17}$.

**The maximally entangled states.** The concurrence depends only on the ratio of the singular values and reaches $1$ exactly when they are equal, that is, when the array is a nonzero scalar multiple of a unitary matrix. Projectively those are the classes of $U(2)$ modulo the scalar $U(1)$, so the maximally entangled states form $U(2)/U(1)\cong SO(3)\cong\mathbb{RP}^3$ inside $\mathbb{CP}^3$, a real three-dimensional manifold lying off the Segre quadric. On a hundred random unitary arrays the concurrence was $1$ to $2.2\times10^{-16}$. The two-qubit state space is thus $\mathbb{CP}^3$, with one quadric for the products and one copy of $\mathbb{RP}^3$ for maximal entanglement; the Schmidt decomposition of the state is the singular value decomposition of $\mathbf c$.

### The two quadratic forms on one element

The identification $\mathbb{C}^4\cong\mathbb{B}$ of *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*, namely $|00\rangle\mapsto e_t$, $|01\rangle\mapsto\vec e_x$, $|10\rangle\mapsto\vec e_y$, $|11\rangle\mapsto\vec e_z$, puts the amplitude array of a state at the coefficients of an element, $\mathbf c=(Q_t,Q_x,Q_y,Q_z)$, and the hyperdeterminant then reads

$$
\mathrm{Det}(\mathbf c)=Q_tQ_z-Q_xQ_y .
$$

The same four coefficients carry the algebra's own quadratic form, the determinant of the matrix image, which is the biquaternion norm:

$$
\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2 ,
$$

verified to $3.6\times10^{-15}$ on a hundred random elements. Two quadratic forms on one element, answering different questions, and the difference is not a change of scale. It is visible on the smallest examples:

- $|00\rangle$ is a product state. Its array is $\operatorname{diag}(1,0)$, of rank one and hyperdeterminant zero; its element is $e_t$, whose matrix image is the identity, of rank two and determinant one.
- $|01\rangle$ is a product state, and its element $\vec e_x$ has $\det\mathsf M_2(\vec e_x)=1$.
- $(\lvert00\rangle+i\lvert01\rangle)/\sqrt2$ is a product state whose element $(e_t+i\vec e_x)/\sqrt2$ has $\langle\tilde Q\rangle_{\natural}=\tfrac12-\tfrac12=0$, and whose matrix image is singular.

**The norm does not track separability.** The biquaternion norm vanishes on some product states and equals one on others, and the matrix image of a product state may be invertible or singular. Neither the rank nor the determinant of $\mathsf M_2$ separates the products from the entangled states.

**Why no algebraic change of description repairs this.** Every automorphism of $\mathbb{B}$ is inner, by Skolem–Noether, so it preserves $\det\mathsf M_2$ exactly; and $\mathrm{Det}$ is not a function of $\langle\tilde Q\rangle_{\natural}$, since on $e_t+\vec e_x$ the first is zero and the second is two. The two forms are not proportional either, the symmetric matrix of $\mathrm{Det}$ in the order $(Q_t,Q_x,Q_y,Q_z)$ being purely off-diagonal. The invariance groups differ, and that is the operative difference: $\mathrm{Det}$ is invariant under $SL(2,\mathbb{C})\times SL(2,\mathbb{C})$ acting on the two factors, and is the generator of those invariants, while $\langle\tilde Q\rangle_{\natural}$ is invariant under the inner automorphisms of the algebra.

**The caveat that keeps the statement honest.** Both forms are nondegenerate quadrics on $\mathbb{C}^4$, of rank four — the symmetric matrix of $\mathrm{Det}$ is invertible, of determinant $\tfrac1{16}$ in this basis — so some complex linear change of coordinates does carry one to the other. What no such change can do is respect either structure. A change that carries $\mathrm{Det}$ to the norm does not preserve the tensor decomposition and is not a symmetry of the algebra, and a change that preserves the algebra leaves $\mathrm{Det}$ where it is. **Separability is a property of the tensor product: it is invariant under the local group and not under the algebra's own symmetries.** That is the precise content of the statement that the composition rule is additional structure.

### What this leaves of the question

The module question is settled by the algebra; the composition question is not. $\mathbb{B}$ supplies one carrier and one inner product, and it supplies neither a second carrier nor the rule that pairs two carriers. What a pair supplies is one polynomial, the hyperdeterminant, hence one entanglement coordinate for each pure state, and its geometry is the rank-one locus in a projective space rather than a property of the algebra product. The framework is not wrong to use $\mathbb{B}\otimes\mathbb{B}$; it is using a second structure, and that structure is now named. For three or more qubits the criterion is in addition relative to a bipartition: separability across a cut $\mathbb{C}^L\otimes\mathbb{C}^l$ is the rank-one condition on the $L\times l$ array, whose vanishing minors are the Plücker relations. There, even the criterion is a choice of cut.

## Open Questions

**1. The tensor product.** Is $\mathbb{B}\otimes\mathbb{B}$ native to the framework, or is it imposed? The defining module of $\mathbb{B}\otimes\mathbb{B}$ is $\mathbb{C}^4$, and the composition of two qubits into one four-level system is an assumption about how subsystems combine. This is the central open structural question for the informational interpretation, and it is inherited from the companion articles on entanglement. The section above answers the part of it that can be answered: the *criterion* of the composition is the hyperdeterminant, which is not a function of the algebra, so the composition is additional at the level of what it means for two qubits to be separate, and not only at the level of the carrier.

**2. The doubling of the regular module.** The left regular module is $S\oplus S$. The qubit uses one copy. Does the second copy have informational content — a chirality, a superselection rule, or nothing — or is it a redundancy of the matrix representative? *Spin-1/2 Quantum Physics in Biquaternionic Form* develops the spinor side of this question.

**3. Higher-dimensional modules.** The algebra's simple module is two-dimensional, but its *projective* representations and its tensor powers are not. Which of those are physically available is the module-theoretic form of the question whether the framework admits qutrits and larger systems.

**4. The status of the inner product at the boundary.** The trace pairing is positive definite on $\mathbb{B}_{\Psi}$ but the biquaternion norm is degenerate on the rank-one idempotents. The relation between these two pairings — one the Born rule, the other the light-cone structure — is the geometric thread running through this subcategory, and it is pursued in the entropy and positive-cone articles that follow.

**5. Empirical contact.** As for the whole framework, a reformulation of the qubit's carrier predicts nothing that ordinary quantum physics does not. The module's nativeness is a statement about how the formalism hangs together, not a new observable.

## Summary

The elementary informational unit of the biquaternion framework is the defining module of the algebra. Because $\mathbb{B}\cong M_2(\mathbb{C})$ is a simple finite-dimensional complex algebra, it has a unique simple left module $S=\mathbb{C}^2$, the column space, and every irreducible representation is equivalent to the action on $S$. The qubit is therefore native to the algebra: it is what the algebra is a matrix algebra of, not a Hilbert space adjoined to it.

On the module, the elements of $\mathbb{B}_{\Psi}$ act as Hermitian operators; the rank-one idempotents $\tilde\Pi_{1,2}(\vec u) = \tfrac12(e_t\pm i\vec u)$ correspond bijectively to the rays of $S$, and are exactly the pure states; the normalised Hermitian form $\langle\tilde\Pi,\tilde R_\Psi\rangle_{*}/\langle\tilde\Pi,e_t\rangle_{*}=2\,\mathrm{Sc}(\tilde\Pi\tilde R_\Psi^{*})=2\langle\tilde\Pi,\tilde R_\Psi\rangle_{*}$ is the Born rule and coincides with the module expectation value $\langle u|H|u\rangle$; its $2\times2$ reading is the trace formula. A general state $\tilde{Ϛ}_{\Psi} = \tfrac12(e_t+i\vec r)$ is a positive element normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12$ (trace one in the image) with spectral decomposition into two rays, and the biquaternion norm $\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural} = \tfrac14(1-|\vec r|^2)e_t$ vanishes exactly on the rays, so that the pure states are the zero divisors of $\mathbb{B}_{\Psi}$ and the Bloch ball is the state slice of the positive cone. The left regular module is $\mathbb{B}\cong S\oplus S$, an algebraic doubling whose informational content is left open.

What the module does not supply is the composition rule for several qubits: the tensor product $\mathbb{B}\otimes\mathbb{B}$ and its four-dimensional module are an additional structure. That, and not the definition of the unit, is where the framework's informational assumptions become substantive. The composition can be tested, and the test is negative in a precise sense. The array of amplitudes of a two-qubit state is a $2\times2$ matrix whose hyperdeterminant $\mathrm{Det}(\mathbf c)=c_{00}c_{11}-c_{01}c_{10}$ vanishes exactly on the product states and whose modulus, normalised, is the concurrence; the product states are the Segre quadric $\mathbb{P}^1\times\mathbb{P}^1\subset\mathbb{P}^3$, and the maximally entangled states are a copy of $\mathbb{RP}^3$. The hyperdeterminant is not the biquaternion norm of anything, the two quadratic forms on the four coefficients are not related by an automorphism of the algebra, and the rank and the determinant of $\mathsf M_2$ do not track separability at all: the matrix image of $|00\rangle$ is the identity. The carrier is native, the composition is not, and the difference is a named invariant rather than a vague reservation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion units, $\vec e_\eta^2 = -e_t$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace (states and observables) |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian subspace (generators of reversible evolution) |
| $S = \mathbb{C}^2$ | Defining (spinor) module of $\mathbb{B}$ |
| $\rho_S$ | The defining representation of $\mathbb{B}$ on $S$ |
| $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$ | Trace, the $2\times2$ reading |
| $\tilde{Q}^{*}$ | Hermitian conjugate (anti-linear involution) |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Biquaternion norm |
| $\tilde\Pi_{1,2}(\vec u) = \tfrac12(e_t\pm i\vec u)$ | Rank-one idempotents (pure states) |
| $\tilde{Ϛ}_{\Psi} = \tfrac12(e_t + i\vec r)$ | State with Bloch vector $\vec r$, $|\vec r|\le1$ |
| $\operatorname{Tr}(\tilde\Pi\tilde R_\Psi^{*})=\operatorname{Tr}(\tilde\Pi\tilde R_\Psi)=2\langle\tilde\Pi,\tilde R_\Psi\rangle_{*}=2\,\mathrm{Sc}(\tilde\Pi\tilde R_\Psi^{*}) = \langle u|H|u\rangle_{*}$ | Trace reading of the Hermitian form; the $2\times2$ reading of the Born rule |
| $r_\eta = 2\langle\tilde{Ϛ}_{\Psi},i\vec e_\eta\rangle_{*} = \mathrm{Tr}(\tilde{Ϛ}_{\Psi}\,(i\vec e_\eta)^{*})$ | Bloch components (tomography) |
| $\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural} = \tfrac14(1-|\vec r|^2)e_t$ | Biquaternion norm of a state |
| $\mathbf c=(c_{A_1A_2})$ | Amplitude array of a two-qubit state, the $2\times2$ matrix of the four amplitudes |
| $\mathrm{Det}(\mathbf c)=c_{00}c_{11}-c_{01}c_{10}$ | Hyperdeterminant of format $2\times2$; it vanishes exactly on the product states |

## Further Reading

- F. W. Anderson and K. R. Fuller, *Rings and Categories of Modules* (Springer, 1992), for the left regular module of $M_n(\mathbb{C})$, its simple modules, and the uniqueness of the defining module.
- I. N. Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for Wedderburn's structure theorem for finite-dimensional simple algebras.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the biquaternion algebra, its units, and its identification with $M_2(\mathbb{C})$.
- W. E. Baylis, *Electrodynamics: A Modern Geometric Approach* (Birkhäuser, 1999), for the complex-quaternion formalism and its Hermitian subspaces.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the qubit, the density operator, and the correspondence between pure states and rays.
- A. Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for the geometry of the Bloch ball and the statistical interpretation of the trace pairing.
- J. S. Bell, "On the problem of hidden variables in quantum mechanics," *Reviews of Modern Physics* **38** (1966) 447–452, for the noncontextual hidden-variable model of a single qubit, which illustrates the special position of the two-dimensional module.
- I. M. Gelfand, M. M. Kapranov and A. V. Zelevinsky, *Discriminants, Resultants, and Multidimensional Determinants* (Birkhäuser, 1994), for the hyperdeterminant of format $2\times2$, the rank-one condition on a tensor, and the invariants of $\mathbb{C}^2\otimes\mathbb{C}^2$ under the local group.
- The mathematics corpus: [Projective Geometry](../articles_maths/projective-geometry.html), §*Quadrics, Rank One and the Segre Embedding*, for the Segre embedding $\mathbb{P}^1\times\mathbb{P}^1\subset\mathbb{P}^3$ as the rank-one locus, and [Grassmannians and Stiefel Manifolds](../articles_maths/grassmannians-and-stiefel-manifolds.html), for the Plücker embedding and the Plücker relations.
- The companion articles of this series: [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html), [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html), [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html), [The Born Rule from the Hermitian Form — Derivation and Comparison](the-born-rule-from-the-hermitian-form-derivation-and-comparison.html), [The Bloch Ball as the Normalised Slice of the Future Light Cone](the-bloch-ball-as-the-normalised-slice-of-the-future-light-cone.html), and [Spin-1/2 Quantum Physics in Biquaternionic Form](spin-1-2-quantum-physics-in-biquaternionic-form.html).
