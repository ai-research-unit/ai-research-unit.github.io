# __$M_2(\mathbb{C})$ Representation : Spin, Qubits and the Bloch Vector__

## Introduction

The $2\times2$ model is the smallest matrix picture of the algebra, and it is the one in which the Hermitian subspace becomes the algebra of observables of a two-state system. Three objects carry the correspondence: the three Hermitian basis matrices $\mathsf M_2(i\vec e_k)=\sigma_k$; the trace-one Hermitian elements, which are the states; and the three traces against the basis matrices, which are the coordinates of a state in the Bloch ball.

This article develops the dictionary. It states the spin operators and their algebra, the pure states as the rank-one Hermitian idempotents on the null cone, the general state and its Bloch vector, and the measurement formulae that read the vector back off the matrix. It proves the identities in the matrix model and leaves their physical interpretation to *The Pauli Correspondence and the Matrix Image*, which reads the same identities physically and states what they do not claim.

**Conventions.** The algebra and the model are those of *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*: $\mathsf M_2(\vec e_k)=-i\sigma_k$ and $\mathsf M_2(e_t)=\mathrm I_2$. The Pauli matrices are $\sigma_1,\sigma_2,\sigma_3$, the scalar part is $Q_t=\tfrac12\operatorname{Tr}\mathsf M_2(\tilde Q)$, and the quaternionic norm is $N=\det\mathsf M_2(\tilde Q)$. The Hermitian subspace is $\mathbb M_+$ and the anti-Hermitian subspace is $\mathbb M_-$. A state is written $\tilde{\varrho}$ and its Bloch vector $\vec r=(r_1,r_2,r_3)\in\mathbb R^3$.

**Boundaries.** The Born pairing and the Hilbert structure of the spinor module are *Spin and the Three Elementary Carriers*; the mixedness and phase-fibre interpretations of the same matrices are *The Pauli Correspondence and the Matrix Image*; the state geometry as a slice of the light cone is *The Bloch Ball as the Normalised Slice of the Future Light Cone*; the pure states as idempotents are *Roots, Idempotents and Observables*; the spectral projectors of a general element are *$M_2(\mathbb{C})$ Model : The Spectral Projectors*.

## The Hermitian Basis

**The three Pauli matrices are the images of the Hermitian units.** Since $\mathsf M_2$ is $\mathbb C$-linear and $\sigma_k=i\mathsf M_2(\vec e_k)$,

$$
\mathsf M_2(\vec e_k)=-i\sigma_k,
\qquad
\mathsf M_2(i\vec e_k)=\sigma_k .
$$

| unit | image | square | Hermitian |
|---|---|---|---|
| $e_t$ | $\mathrm I_2$ | $\mathrm I_2$ | yes |
| $\vec e_k$ | $-i\sigma_k$ | $-\mathrm I_2$ | no |
| $i\vec e_k$ | $\sigma_k$ | $\mathrm I_2$ | yes |

**The general element.** Expanding on the basis,

$$
\boxed{\;\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i\bigl(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3\bigr)\;}.
$$

**The Hermitian condition.** An element lies in $\mathbb M_+$ exactly when $Q_t$ is real and the three $Q_k$ are purely imaginary, that is when

$$
\tilde Q=q_t e_t+i\bigl(q'_x\vec e_x+q'_y\vec e_y+q'_z\vec e_z\bigr),
\qquad q_t,q'_k\in\mathbb R .
$$

Its image is then

$$
\mathsf M_2(\tilde Q)=q_t\mathrm I_2+q'_x\sigma_1+q'_y\sigma_2+q'_z\sigma_3,
$$

which is Hermitian, and every Hermitian matrix arises this way with these four real numbers. The map is thus an isomorphism of real vector spaces

$$
\mathbb M_+\longrightarrow \operatorname{Herm}_2(\mathbb C),
\qquad
q_t e_t+iq'_k\vec e_k\longmapsto q_t\mathrm I_2+q'_k\sigma_k ,
$$

and the same statement holds on $\mathbb M_-$ with the factor $i$: an anti-Hermitian element maps to an anti-Hermitian matrix, and $\mathbb M_-=i\mathbb M_+$ is the image statement $\mathsf M_2(i\tilde Q)=i\mathsf M_2(\tilde Q)$.

**The four real coordinates.** On $\mathbb M_+$ the coefficient $q_t$ is the weight of the identity and the three $q'_k$ are the weights of the Pauli matrices. They are the four real numbers of a Hermitian $2\times2$ matrix, and the passage between the two writings is the identity above, with no factor and no sign.

## The Spin Operators

**Definition.** The spin operators are

$$
\tilde S_k=\tfrac{\hbar}{2}i\vec e_k,
\qquad
\mathsf M_2(\tilde S_k)=\tfrac{\hbar}{2}\sigma_k .
$$

They are Hermitian elements of $\mathbb M_+$, and their images are the Hermitian spin matrices.

**The algebra.** Direct multiplication of the Pauli matrices gives

$$
\sigma_i\sigma_j=\delta_{ij}\mathrm I_2+i\epsilon_{ijk}\sigma_k ,
$$

and therefore

$$
\tilde S_i\tilde S_j=\tfrac{\hbar^2}{4}\delta_{ij}e_t-\tfrac{\hbar^2}{4}\epsilon_{ijk}\vec e_k .
$$

Taking the symmetric and the antisymmetric parts,

$$
\{\tilde S_i,\tilde S_j\}=\tfrac{\hbar^2}{2}\delta_{ij}e_t,
\qquad
[\tilde S_i,\tilde S_j]=i\hbar\,\epsilon_{ijk}\tilde S_k .
$$

The commutator is the angular-momentum algebra of a spin-$\tfrac12$ system, and it is the matrix form of the Lie algebra of $\mathrm{SU}(2)$. The anticommutator is the Clifford relation of the same three directions.

**Two roles of one direction.** The commutator is anti-Hermitian, so it lies in $\mathbb M_-$: the generators of the $*$-unitary group are the elements $\vec e_k$, whose images $-i\sigma_k$ are anti-Hermitian. The observables are the elements $i\vec e_k$, whose images $\sigma_k$ are Hermitian. The same three directions therefore appear twice, as generators and as observables, and the two appearances differ by the factor $i$. This is the precise content of the phrase that the Pauli matrices generate the rotations and measure the spin.

**The span.** The three spin operators span over $\mathbb R$ the traceless Hermitian subspace, $\mathbb M_+\cap\mathrm{Vect}(\mathbb B)$, of real dimension three. With the identity they span the whole of $\mathbb M_+$, of real dimension four. They do not span the algebra over $\mathbb R$: the products $\sigma_i\sigma_j$ leave the Hermitian subspace whenever $i\neq j$.

## Pure States

**Definition.** For a real unit vector $\vec u$,

$$
\tilde\Pi(\vec u)=\tfrac12\bigl(e_t+i\vec u\bigr)=\tfrac12\bigl(e_t+iu_1\vec e_x+iu_2\vec e_y+iu_3\vec e_z\bigr).
$$

**Proposition.** $\tilde\Pi(\vec u)$ is a Hermitian idempotent of trace one and determinant zero, and

$$
\mathsf M_2\bigl(\tilde\Pi(\vec u)\bigr)=\tfrac12\bigl(\mathrm I_2+\vec u\cdot\vec\sigma\bigr)
$$

is the rank-one projector onto the line of the spinor of spin up along $\vec u$. Writing $\vec u=(\sin\theta\cos\varphi,\sin\theta\sin\varphi,\cos\theta)$, that line is spanned by

$$
\Bigl(\cos\tfrac{\theta}{2},\ e^{i\varphi}\sin\tfrac{\theta}{2}\Bigr).
$$

*Proof.* The image is Hermitian because $\vec u$ is real. It squares to itself because $(\vec u\cdot\vec\sigma)^2=|\vec u|^2\mathrm I_2=\mathrm I_2$. Its trace is $1$ and its determinant is $\frac14(1-|\vec u|^2)=0$, so it has rank one; a rank-one Hermitian idempotent is the orthogonal projector onto its image line. The kernel is the orthogonal line, which is the image of $\tilde\Pi(-\vec u)$.

**The complementary state.** $\tilde\Pi(\vec u)+\tilde\Pi(-\vec u)=e_t$, and

$$
\mathsf M_2\bigl(\tilde\Pi(-\vec u)\bigr)=\mathrm I_2-\mathsf M_2\bigl(\tilde\Pi(\vec u)\bigr),
$$

so the two projectors are complementary and orthogonal, $\operatorname{Tr}\bigl(\mathsf M_2(\tilde\Pi(\vec u))\mathsf M_2(\tilde\Pi(-\vec u))\bigr)=0$.

**The null cone.** A pure state has $N(\tilde\Pi(\vec u))=0$ and scalar part $\tfrac12$, so it lies on the null cone but not in the pure stratum of *$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety*: it is a rank-one idempotent, not a nilpotent. The two notions of purity must not be conflated. The null cone contains both strata, and the pure states are the idempotent half.

**The sphere.** The map $\vec u\mapsto\tilde\Pi(\vec u)$ is a bijection from the unit sphere onto the set of pure states, and the antipodal point gives the orthogonal state, $\tilde\Pi(\vec u)\tilde\Pi(-\vec u)=0$. The state is a point of the sphere, not a spinor: the spinor is defined up to a phase, and the phase is the circle over the point.

## The General State

**Definition.** A state is a Hermitian element of trace one whose matrix is positive semidefinite:

$$
\tilde{\varrho}=\tfrac12\bigl(e_t+i\vec r\bigr),
\qquad \vec r\in\mathbb R^3,
\qquad
\mathsf M_2(\tilde{\varrho})=\rho=\tfrac12\bigl(\mathrm I_2+\vec r\cdot\vec\sigma\bigr).
$$

**The three numbers.** The matrix $\rho$ is Hermitian of trace one for every real $\vec r$, and its determinant and square are

$$
\det\rho=\tfrac14\bigl(1-|\vec r|^2\bigr),
\qquad
\operatorname{Tr}\rho^2=\tfrac12\bigl(1+|\vec r|^2\bigr).
$$

**Proposition.** The following are equivalent: $\rho$ is positive semidefinite; $|\vec r|\le1$; $N(\tilde{\varrho})\ge0$; the two eigenvalues $\tfrac12(1\pm|\vec r|)$ are non-negative. The state is pure exactly when $|\vec r|=1$, that is exactly when $N(\tilde{\varrho})=0$.

*Proof.* The eigenvalues of $\vec r\cdot\vec\sigma$ are $\pm|\vec r|$, so those of $\rho$ are $\tfrac12(1\pm|\vec r|)$. The determinant is their product, and the norm is the determinant. The purity is the equality $\operatorname{Tr}\rho^2=(\operatorname{Tr}\rho)^2$, which reads $|\vec r|=1$.

**The state space.** The states are therefore the trace-one slice of the positive cone of $\mathbb M_+$,

$$
\mathcal S=\bigl\{\tilde{\varrho}\in\mathbb M_+ : \operatorname{Tr}\mathsf M_2(\tilde{\varrho})=1,\ N(\tilde{\varrho})\ge0\bigr\},
$$

and the map $\tilde{\varrho}\mapsto\vec r$ is a bijection onto the closed unit ball of $\mathbb R^3$. The ball is the Bloch ball, its interior is the mixed states, its boundary is the pure states, and its centre is the maximally mixed state

$$
\tfrac12 e_t\longmapsto\tfrac12\mathrm I_2,
\qquad \vec r=0 .
$$

The boundary is the trace-one slice of the null cone, so the pure states are exactly the states of vanishing norm. This is the matrix form of the statement that the pure states are the extreme points of the state space.

**The radius as mixedness.** The number $|\vec r|$ measures how far the state is from the centre, and $\det\rho=\frac14(1-|\vec r|^2)$ measures the distance from the boundary. Both are functions of the single invariant $|\vec r|$, and that invariant is the modulus of the vector part of $\tilde{\varrho}$ in the Hermitian basis. The determinant of a state matrix is therefore not the interval: on the trace-one slice it is a measure of mixing, and its vanishing is purity.

## The Born Rule and the Convex Splitting

**The Born rule.** For a measurement along the unit vector $\vec u$, the two outcomes have probabilities

$$
p_\pm=\operatorname{Tr}\bigl(\rho\,\Pi_\pm(\vec u)\bigr)
=\tfrac12\bigl(1\pm\vec r\cdot\vec u\bigr),
\qquad
\Pi_\pm(\vec u)=\tfrac12\bigl(\mathrm I_2\pm\vec u\cdot\vec\sigma\bigr).
$$

The probabilities are non-negative exactly when $\lvert\vec r\rvert\le1$, and they sum to one. The expectation of the spin operator $\tfrac{\hbar}{2}\vec u\cdot\vec\sigma$ is $\tfrac{\hbar}{2}\vec r\cdot\vec u$.

**The convex splitting.** For $\vec r\neq0$ every state is a convex combination of the two pure states along its own axis:

$$
\rho=\frac{1+\lvert\vec r\rvert}{2}\,\Pi_+(\hat r)
+\frac{1-\lvert\vec r\rvert}{2}\,\Pi_-(\hat r),
\qquad
\hat r=\frac{\vec r}{\lvert\vec r\rvert},
$$

and for $\vec r=0$ the state is $\tfrac12\mathrm I_2$. The weights are non-negative and sum to one. The decomposition is the chord of the Bloch ball through the centre: the state lies on the segment between the two boundary points $\pm\hat r$, and its distance from the centre is the bias of the mixture.

**The geometry.** The pure states are the boundary sphere, the maximally mixed state is the centre, and the ball is convex. The matrix form of the convex structure is the statement that the positive semidefinite matrices of trace one form a convex set whose extreme points are the rank-one projectors.

## Reading the Vector Back

**Proposition.** The Bloch coordinates are the traces against the Pauli matrices,

$$
r_k=\operatorname{Tr}\bigl(\rho\,\sigma_k\bigr),
$$

and, in the algebra, twice the trace pairing against the Hermitian units,

$$
r_k=2\bigl\langle\tilde{\varrho},i\vec e_k\bigr\rangle .
$$

*Proof.* The first identity follows from $\operatorname{Tr}\sigma_k=0$ and $\operatorname{Tr}(\sigma_j\sigma_k)=2\delta_{jk}$. The second is the trace pairing $\langle\tilde P,\tilde Q\rangle=\tfrac12\operatorname{Tr}(\mathsf M_2(\tilde P)\mathsf M_2(\tilde Q))$ of *$M_2(\mathbb{C})$ Representation : The Four Words and the Four Traces* applied to $\tilde{\varrho}$ and $i\vec e_k$.

**The reconstruction.** The three numbers $r_k$ determine the state, because

$$
\rho=\tfrac12\Bigl(\mathrm I_2+r_k\sigma_k\Bigr),
$$

and the four matrices $\mathrm I_2,\sigma_1,\sigma_2,\sigma_3$ are a basis of the Hermitian matrices over $\mathbb R$. The state, the matrix and the vector are three writings of four real numbers.

**The measurement formulae.** For a unit vector $\vec u$, the probability of the outcome $+$ in the measurement of the spin along $\vec u$ is

$$
p_+(\vec u)=\operatorname{Tr}\bigl(\rho\,\mathsf M_2(\tilde\Pi(\vec u))\bigr)
=\tfrac12\bigl(1+\vec r\cdot\vec u\bigr),
$$

and the probability of the outcome $-$ is $p_-=\tfrac12(1-\vec r\cdot\vec u)$. The expectation of the spin is

$$
\langle S_{\vec u}\rangle=\operatorname{Tr}\bigl(\rho\,\mathsf M_2(\tilde S_{\vec u})\bigr)
=\tfrac{\hbar}{2}\,\vec r\cdot\vec u .
$$

More generally, for a Hermitian observable $\tilde H=h_t e_t+i\vec h$ the expectation is

$$
\operatorname{Tr}\bigl(\rho\,\mathsf M_2(\tilde H)\bigr)=h_t+\vec r\cdot\vec h ,
$$

which is the affine function of the state determined by the four numbers $(h_t,\vec h)$. The Born pairing of *Spin and the Three Elementary Carriers* is the same identity written with the state idempotent.

## The Qubit as a Spinor

**The pure case.** Every pure state is a rank-one projector, so it is

$$
\rho=\xi\xi^{\dagger},
\qquad \xi=\binom{\xi_1}{\xi_2}\in\mathbb C^2,
\qquad \|\xi\|=1,
$$

and the Bloch vector is

$$
r_k=\xi^{\dagger}\sigma_k\xi .
$$

The vector $\xi$ is defined up to a phase, $\xi\mapsto e^{i\alpha}\xi$, and the phase cancels in $\rho$: the state is the ray, not the vector. In the algebra the spinor is an element of the Peirce carrier $\mathbb B\tilde\Pi_+$, which is the minimal left ideal here, and the module structure that makes it a Hilbert space is the second structure of *Spin and the Three Elementary Carriers*.

**The mixed case.** A general state is a convex combination of pure ones,

$$
\rho=\sum_i p_i\,\xi_i\xi_i^{\dagger},
\qquad p_i\ge0,\quad \sum_i p_i=1,
$$

and the Bloch vector is the corresponding convex combination of the pure Bloch vectors. The ball is the convex hull of the sphere, which is the matrix form of the statement that every state is a mixture.

**The phase.** The central phase $e^{i\alpha}e_t$ acts on the spinor by multiplication and on the algebra by the identity sandwich. It is a scalar matrix, it multiplies $\rho$ by $e^{i\alpha}$ and does not preserve the trace-one slice; the physical state is the ray, and the circle of phases over each pure state is the fibre of *The Pauli Correspondence and the Matrix Image*. This article records the matrix identity and adds no topology.

## Where the Correspondence Stops

**The Pauli matrices are not elements of the algebra.** They are the images of $i\vec e_k$, and the algebra's own units are $-i\sigma_k$. A statement about the $\sigma_k$ must be translated back through the factor $i$ before it is a statement about $\mathbb B$; the commutator of two Pauli matrices is $i$ times a Pauli matrix, and the commutator of two algebra units is an algebra unit.

**The real form is extra data.** The identification $\mathbb B\cong M_2(\mathbb C)$ is an isomorphism of complex algebras, and it does not by itself select $\mathbb M_+$. The statement that the Hermitian elements are the observables uses the involution ${}^{*}$, which is part of the real structure of $\mathbb B$ and is not visible in the complex algebra alone. The same matrix algebra carries the anti-Hermitian sector, and the choice between the two sectors is a physical choice, not a matrix identity.

**No dynamics.** Nothing in this article evolves a state. The spin operators generate the rotations of the state space through the commutator, and the Hamiltonian that would generate a motion in time is a choice of observable, not a consequence of the model.

## Summary

The Hermitian units of the algebra map to the Pauli matrices, $\mathsf M_2(i\vec e_k)=\sigma_k$, and the vector units map to $-i\sigma_k$; the general element is $Q_t\mathrm I_2-iQ_k\sigma_k$. The spin operators $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$ satisfy $\{\tilde S_i,\tilde S_j\}=\tfrac{\hbar^2}{2}\delta_{ij}e_t$ and $[\tilde S_i,\tilde S_j]=i\hbar\epsilon_{ijk}\tilde S_k$. A state is $\tilde{\varrho}=\tfrac12(e_t+i\vec r)$ with $|\vec r|\le1$, its matrix is $\rho=\tfrac12(\mathrm I_2+\vec r\cdot\vec\sigma)$, and its Bloch vector is recovered by $r_k=\operatorname{Tr}(\rho\sigma_k)=2\langle\tilde{\varrho},i\vec e_k\rangle$. The pure states are the rank-one Hermitian idempotents, $|\vec r|=1$, $N=0$; they are the boundary of the ball and the trace-one slice of the null cone. The measurement formulae are $p_\pm(\vec u)=\tfrac12(1\pm\vec r\cdot\vec u)$ and $\langle S_{\vec u}\rangle=\tfrac{\hbar}{2}\vec r\cdot\vec u$. The correspondence uses the real form $\mathbb M_+$, which the complex isomorphism alone does not select.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma_1,\sigma_2,\sigma_3$ | the Pauli matrices, $\sigma_k=\mathsf M_2(i\vec e_k)$ |
| $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$ | the spin operators |
| $\tilde\Pi(\vec u)=\tfrac12(e_t+i\vec u)$ | the pure state of spin up along $\vec u$ |
| $\tilde{\varrho}=\tfrac12(e_t+i\vec r)$ | a general state |
| $\rho=\mathsf M_2(\tilde{\varrho})$ | the density matrix |
| $\vec r$ | the Bloch vector, $r_k=\operatorname{Tr}(\rho\sigma_k)$ |
| $N(\tilde{\varrho})=\det\rho$ | the norm, $\tfrac14(1-\lvert\vec r\rvert^2)$ on the state slice |
| $p_\pm(\vec u)$ | the outcome probabilities, $\tfrac12(1\pm\vec r\cdot\vec u)$ |

## Further Reading

- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the assignment and the Pauli correspondence
- [$M_2(\mathbb{C})$ Model : The Six Subspaces as Matrix Conditions](m2c-model-the-six-subspaces-as-matrix-conditions.html), for $\mathbb M_+$ as the Hermitian matrices
- [$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety](m2c-representation-rank-one-matrices-and-the-determinantal-variety.html), for the null cone and its two strata
- [$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm](m2c-representation-trace-determinant-and-the-biquaternion-norm.html), for the determinant as the norm
- [$M_2(\mathbb{C})$ Representation : The Four Words and the Four Traces](m2c-representation-the-four-words-and-the-four-traces.html), for the trace pairing
- [The Pauli Correspondence and the Matrix Image](../articles_physics/the-pauli-correspondence-and-the-matrix-image.html), for the physical interpretation of these identities
- [Spin and the Three Elementary Carriers](../articles_physics/spin-and-the-three-elementary-carriers.html), for the Hilbert structure of the module
- [The Bloch Ball as the Normalised Slice of the Future Light Cone](../articles_physics/the-bloch-ball-as-the-trace-one-slice-of-the-future-light-cone.html), for the state geometry
- G. B. Folland, *Quantum Field Theory: A Tourist Guide for Mathematicians* (AMS, 2008), for the Pauli and Bloch conventions.
