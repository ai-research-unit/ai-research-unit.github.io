# __Matrix Representations : Spin, Qubits and the Bloch Vector__

## Introduction

A qubit is a Hermitian element of trace one and non-negative norm. Its matrix is $\tfrac12(\mathrm I+\vec r\cdot\vec\sigma)$, and the vector $\vec r$ lies in the unit ball. The Pauli matrices are the images of the Hermitian units $i\vec e_k$, and the spin operators are the images of $\tfrac{\hbar}{2}i\vec e_k$. In the regular model every object is doubled, the state becomes a rank-two matrix, and the Bloch vector is unchanged.

This article develops the Hermitian basis, the spin operators, the pure states, the general state and the Bloch ball, the Born rule, the reconstruction of the vector, the spinor and the Hopf fibration, and the limits of the correspondence. It is the article in which the real form $\mathbb M_+$ of *Matrix Representations : The Six Subspaces as Matrix Conditions* becomes a state space.

**Conventions.** The algebra and the displays are those of *Matrix Representations : The Models and the Change of Frame*. The element is $\tilde Q=Q_te_t+\vec Q$, with $2\times2$ entry matrix $B=\mathsf M_2(\tilde Q)$ and $4\times4$ regular matrix $L=I_2\otimes B$. The Pauli matrices are $\sigma_1,\sigma_2,\sigma_3$, and $\mathsf M_2(\vec e_k)=-i\sigma_k$. The Hermitian adjoint is the conjugate transpose.

**Boundaries.** The matrix statements are *Matrix Representations : Spin, Qubits and the Bloch Vector*; the real form is *Matrix Representations : The Six Subspaces as Matrix Conditions*; the Pauli correspondence is *The Pauli Correspondence and the Matrix Image*; the spinor carriers are *Spinors as Peirce Coordinates in the Biquaternion Algebra*; the measurement rule is *Spin and the Three Elementary Carriers*.

## Common Aspects

### The Hermitian Basis

**The Pauli images.**
$$
\mathsf M_2(\vec e_k)=-i\sigma_k,
\qquad
\mathsf M_2(i\vec e_k)=\sigma_k,
\qquad
\mathsf M_2(i\vec e_k)^2=\mathrm I_2 .
$$

| Unit | Image | Square | Hermitian |
|---|---|---|---|
| $e_t$ | $\mathrm I_2$ | $\mathrm I_2$ | yes |
| $\vec e_k$ | $-i\sigma_k$ | $-\mathrm I_2$ | no |
| $i\vec e_k$ | $\sigma_k$ | $\mathrm I_2$ | yes |

**The general element.**
$$
\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i\bigl(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3\bigr).
$$

**The Hermitian condition.** An element lies in $\mathbb M_+$ exactly when $Q_t$ is real and the three $Q_k$ are purely imaginary:
$$
\tilde Q=q_te_t+i\bigl(q'_x\vec e_x+q'_y\vec e_y+q'_z\vec e_z\bigr),
\qquad q_t,q'_k\in\mathbb R,
$$
and then
$$
\mathsf M_2(\tilde Q)=q_t\mathrm I_2+q'_x\sigma_1+q'_y\sigma_2+q'_z\sigma_3 .
$$
The map is an isomorphism of real vector spaces
$$
\mathbb M_+\longrightarrow\operatorname{Herm}_2(\mathbb C),
\qquad
q_te_t+iq'_k\vec e_k\longmapsto q_t\mathrm I_2+q'_k\sigma_k .
$$

**The regular display.** In the regular image the same element is
$$
L(\tilde Q)=q_t\mathrm I_4+q'_x\Sigma_1+q'_y\Sigma_2+q'_z\Sigma_3,
\qquad
\Sigma_k=\operatorname{diag}(\sigma_k,\sigma_k),
$$
and in the Peirce frame it is the block diagonal matrix with two equal Hermitian blocks.

**The real coordinates.** The coefficient $q_t$ is the weight of the identity and the three $q'_k$ are the weights of the Pauli matrices. They are the four real numbers of a Hermitian matrix, and the passage between the two writings has no factor and no sign.

### The Spin Operators

**The definition.**
$$
\tilde S_k=\tfrac{\hbar}{2}i\vec e_k,
\qquad
\mathsf M_2(\tilde S_k)=\tfrac{\hbar}{2}\sigma_k .
$$
They are Hermitian elements of $\mathbb M_+$, and their images are the Hermitian spin matrices.

**The algebra.** Since $\sigma_i\sigma_j=\delta_{ij}\mathrm I_2+i\epsilon_{ijk}\sigma_k$,
$$
\tilde S_i\tilde S_j=\tfrac{\hbar^2}{4}\delta_{ij}e_t-\tfrac{\hbar^2}{4}\epsilon_{ijk}\vec e_k,
$$
and therefore
$$
\{\tilde S_i,\tilde S_j\}=\tfrac{\hbar^2}{2}\delta_{ij}e_t,
\qquad
[\tilde S_i,\tilde S_j]=i\hbar\,\epsilon_{ijk}\tilde S_k .
$$
The commutator is the angular-momentum algebra of a spin-$\tfrac12$ system; the anticommutator is the Clifford relation of the three directions.

**Two roles of one direction.** The commutator is anti-Hermitian and lies in $\mathbb M_-$: the generators of the unitary group are $\vec e_k$, with images $-i\sigma_k$. The observables are $i\vec e_k$, with images $\sigma_k$. The same three directions appear twice, as generators and as observables, and the two appearances differ by the factor $i$.

**The span.** The three spin operators span over $\mathbb R$ the traceless Hermitian subspace of real dimension three. Together with the identity they span $\mathbb M_+$, of real dimension four. They do not span the algebra over $\mathbb R$: the products $\sigma_i\sigma_j$ leave the Hermitian subspace when $i\neq j$.

**The regular display.**
$$
L(\tilde S_k)=\tfrac{\hbar}{2}\Sigma_k=\tfrac{\hbar}{2}\operatorname{diag}(\sigma_k,\sigma_k),
$$
so the spin operators are doubled and the commutation relations are unchanged.

### Pure States

**The definition.** For a real unit vector $\vec u$,
$$
\tilde\Pi(\vec u)=\tfrac12\bigl(e_t+i\vec u\bigr)
=\tfrac12\bigl(e_t+iu_1\vec e_x+iu_2\vec e_y+iu_3\vec e_z\bigr).
$$

**The proposition.** $\tilde\Pi(\vec u)$ is a Hermitian idempotent of trace one and determinant zero, and
$$
\mathsf M_2\bigl(\tilde\Pi(\vec u)\bigr)=\tfrac12\bigl(\mathrm I_2+\vec u\cdot\vec\sigma\bigr)
$$
is the rank-one projector onto the line of the spinor of spin up along $\vec u$. Writing $\vec u=(\sin\theta\cos\varphi,\sin\theta\sin\varphi,\cos\theta)$, that line is spanned by
$$
\bigl(\cos\tfrac{\theta}{2},\ e^{i\varphi}\sin\tfrac{\theta}{2}\bigr).
$$

*Proof.* The image is Hermitian because $\vec u$ is real. It squares to itself because $(\vec u\cdot\vec\sigma)^2=\lvert\vec u\rvert^2\mathrm I_2=\mathrm I_2$. Its trace is one and its determinant is $\tfrac14(1-\lvert\vec u\rvert^2)=0$, so it has rank one and is the orthogonal projector onto its image line.

**The complementary state.** $\tilde\Pi(\vec u)+\tilde\Pi(-\vec u)=e_t$, and the two projectors are orthogonal:
$$
\operatorname{Tr}\bigl(\mathsf M_2(\tilde\Pi(\vec u))\mathsf M_2(\tilde\Pi(-\vec u))\bigr)=0 .
$$

**The null cone.** A pure state has $N(\tilde\Pi(\vec u))=0$ and scalar part $\tfrac12$, so it lies on the null cone but not in the pure stratum of *Matrix Representations : Rank-One Matrices and the Determinantal Variety*: it is an idempotent, not a nilpotent. The two words "pure" are not the same word.

**The sphere.** The map $\vec u\mapsto\tilde\Pi(\vec u)$ is a bijection from the unit sphere onto the pure states, and the antipodal point gives the orthogonal state. The state is a point of the sphere, not a spinor: the spinor is defined up to a phase, and the phase is the circle over the point.

**The regular display.** The regular image of the pure state is
$$
\tfrac12\bigl(\Pi(\vec u)\oplus\Pi(\vec u)\bigr),
$$
a rank-two projector of trace one. It is not a pure state of the four-level matrix, where purity would require rank one; the copy label is maximally mixed.

### The Born Rule

**The probabilities.** For a measurement along the unit vector $\vec u$,
$$
p_\pm=\operatorname{Tr}\bigl(\rho\,\Pi_\pm(\vec u)\bigr)
=\tfrac12\bigl(1\pm\vec r\cdot\vec u\bigr),
\qquad
\Pi_\pm(\vec u)=\tfrac12\bigl(\mathrm I_2\pm\vec u\cdot\vec\sigma\bigr).
$$
The probabilities are non-negative exactly when $\lvert\vec r\rvert\le1$, and they sum to one.

**The expectation.**
$$
\langle S_{\vec u}\rangle=\operatorname{Tr}\bigl(\rho\,\mathsf M_2(\tilde S_{\vec u})\bigr)
=\tfrac{\hbar}{2}\,\vec r\cdot\vec u .
$$
For a general Hermitian observable $\tilde H=h_te_t+i\vec h$,
$$
\operatorname{Tr}\bigl(\rho\,\mathsf M_2(\tilde H)\bigr)=h_t+\vec r\cdot\vec h,
$$
the affine function of the state determined by the four numbers $(h_t,\vec h)$.

**The regular display.** The same probabilities and expectations hold for $\rho_4$, because the trace of the doubled matrix is the trace of one copy and the doubling cancels the factor $\tfrac12$.

**The convex splitting.** For $\vec r\neq0$,
$$
\rho=\frac{1+\lvert\vec r\rvert}{2}\Pi_+(\hat r)
+\frac{1-\lvert\vec r\rvert}{2}\Pi_-(\hat r),
\qquad
\hat r=\frac{\vec r}{\lvert\vec r\rvert},
$$
and for $\vec r=0$ the state is $\tfrac12\mathrm I_2$. The weights are non-negative and sum to one. The state lies on the chord of the ball between the two boundary points $\pm\hat r$, and its distance from the centre is the bias of the mixture.

**The geometry.** The pure states are the boundary sphere, the maximally mixed state is the centre, and the ball is convex. The matrix form of the convex structure is the statement that the positive semidefinite matrices of trace one form a convex set whose extreme points are the rank-one projectors.

### Reading the Vector Back

**The traces.**
$$
r_k=\operatorname{Tr}(\rho\sigma_k),
\qquad
r_k=2\bigl\langle\tilde{\varrho},i\vec e_k\bigr\rangle .
$$
The first identity follows from $\operatorname{Tr}\sigma_k=0$ and $\operatorname{Tr}(\sigma_j\sigma_k)=2\delta_{jk}$; the second is the trace pairing of *Matrix Representations : The Four Words and the Four Traces*.

**The reconstruction.**
$$
\rho=\tfrac12\bigl(\mathrm I_2+r_k\sigma_k\bigr),
$$
and the four matrices $\mathrm I_2,\sigma_1,\sigma_2,\sigma_3$ are a basis of the Hermitian matrices over $\mathbb R$. The state, the matrix and the vector are three writings of four real numbers.

### The Qubit as a Spinor

**The pure case.** Every pure state is a rank-one projector,
$$
\rho=\xi\xi^{\dagger},
\qquad \xi\in\mathbb C^2,\quad\lVert\xi\rVert=1,
\qquad
r_k=\xi^{\dagger}\sigma_k\xi .
$$
The vector $\xi$ is defined up to a phase, and the phase cancels in $\rho$: the state is the ray, not the vector. In the algebra the spinor is an element of the Peirce carrier $\mathbb B\tilde\Pi_+$, the minimal left ideal.

**The mixed case.** A general state is a convex combination of pure ones,
$$
\rho=\sum_i p_i\,\xi_i\xi_i^{\dagger},
\qquad p_i\ge0,\quad\sum_i p_i=1,
$$
and the Bloch vector is the corresponding convex combination. The ball is the convex hull of the sphere.

**The Hopf fibration.** The map
$$
S^3\longrightarrow S^2,
\qquad
\xi\longmapsto\vec r=\xi^{\dagger}\vec\sigma\xi,
$$
is the Hopf fibration, with fibre $S^1$ the phase circle. In the regular display the total space is the diagonal $S^3$ inside $S^3\times S^3$, and the base and the fibre are the same.

**The copy label.** The doubled spinor is not a spinor of a four-level system: it is two copies of the same spinor, and the state is the product of the maximally mixed copy label with the algebraic state. No algebra observable can polarize the label.

### Where the Correspondence Stops

**The Pauli matrices are not elements of the algebra.** They are the images of $i\vec e_k$, and the algebra's own units are $-i\sigma_k$. A statement about the $\sigma_k$ must be translated back through the factor $i$; the commutator of two Pauli matrices is $i$ times a Pauli matrix, and the commutator of two algebra units is an algebra unit.

**The real form is extra data.** The identification $\mathbb B\cong M_2(\mathbb C)$ is an isomorphism of complex algebras and does not by itself select $\mathbb M_+$. The statement that the Hermitian elements are the observables uses the involution $*$, which is part of the real structure and is not visible in the complex algebra alone.

**The multiplicity is extra data.** The regular model doubles every state, and the doubling is not a two-level system: the copy label is maximally mixed, the rank is two, and the purity is halved. The physical content is in the algebra, not in the multiplicity.

**No dynamics.** Nothing in this article evolves a state. The spin operators generate the rotations through the commutator; a Hamiltonian would be a choice of observable, not a consequence of the model.

## The Coefficient Frame

**The state in coefficient coordinates.** The coefficient frame is the frame in which the Hermitian units are the Pauli matrices:
$$
\mathsf M_2(i\vec e_k)=\sigma_k,\qquad
\mathsf M_2(\vec e_k)=-i\sigma_k.
$$
A state is
$$
\tilde{\varrho}=\tfrac12\bigl(e_t+i\vec r\bigr)
=\tfrac12e_t+\tfrac{i}{2}\bigl(r_1\vec e_x+r_2\vec e_y+r_3\vec e_z\bigr),
$$
with coefficient column
$$
[\varrho]=\tfrac12\bigl(1,\ ir_1,\ ir_2,\ ir_3\bigr)^{\mathsf T}.
$$
The scalar coefficient is the weight of the identity and the three imaginary coefficients are the Bloch vector. Hermiticity is exactly the condition that the scalar coefficient is real and the three vector coefficients are purely imaginary.

**Reading the vector.** The Bloch vector is the coefficient pairing with the Hermitian units:
$$
r_k=2\bigl\langle\tilde{\varrho},i\vec e_k\bigr\rangle
=\operatorname{Tr}(\rho\sigma_k),
$$
because $\operatorname{Tr}(\sigma_j\sigma_k)=2\delta_{jk}$ and $\operatorname{Tr}\sigma_k=0$. The four real numbers $(1,r_1,r_2,r_3)$ are the coordinates of the state in the basis $(e_t,i\vec e_x,i\vec e_y,i\vec e_z)$ of $\mathbb M_+$.

**The regular display.** The regular matrix in the coefficient frame is $C_{\Pi}(I_2\otimes\rho)C_{\Pi}^{-1}$; its first column is $[\varrho]$, and its trace is one. The Bloch vector is unchanged by the doubling: the copy label contributes no imaginary coefficients.

## The Entry Model

### The General State

**The definition.** A state is a Hermitian element of trace one whose matrix is positive semidefinite:
$$
\tilde{\varrho}=\tfrac12\bigl(e_t+i\vec r\bigr),
\qquad \vec r\in\mathbb R^3,
\qquad
\mathsf M_2(\tilde{\varrho})=\rho=\tfrac12\bigl(\mathrm I_2+\vec r\cdot\vec\sigma\bigr).
$$

**The invariants.**
$$
\det\rho=\tfrac14\bigl(1-\lvert\vec r\rvert^2\bigr),
\qquad
\operatorname{Tr}\rho^2=\tfrac12\bigl(1+\lvert\vec r\rvert^2\bigr).
$$

**The equivalence.** The following are equivalent: $\rho$ is positive semidefinite; $\lvert\vec r\rvert\le1$; $N(\tilde{\varrho})\ge0$; the eigenvalues $\tfrac12(1\pm\lvert\vec r\rvert)$ are non-negative. The state is pure exactly when $\lvert\vec r\rvert=1$, that is exactly when $N(\tilde{\varrho})=0$.

**The state space.** The states are the trace-one slice of the positive cone of $\mathbb M_+$:
$$
\mathcal S=\bigl\{\tilde{\varrho}\in\mathbb M_+:\operatorname{Tr}\mathsf M_2(\tilde{\varrho})=1,\ N(\tilde{\varrho})\ge0\bigr\}.
$$
The map $\tilde{\varrho}\mapsto\vec r$ is a bijection onto the closed unit ball of $\mathbb R^3$. The ball is the Bloch ball, its interior is the mixed states, its boundary is the pure states, and its centre is the maximally mixed state $\tfrac12e_t\mapsto\tfrac12\mathrm I_2$ with $\vec r=0$. The boundary is the trace-one slice of the null cone.

**The radius as mixedness.** The number $\lvert\vec r\rvert$ measures the distance from the centre, and $\det\rho=\tfrac14(1-\lvert\vec r\rvert^2)$ measures the distance from the boundary. On the trace-one slice the determinant is a measure of mixing, and its vanishing is purity.

**The regular display.** The regular state is
$$
\rho_4=\tfrac12(\rho\oplus\rho),
$$
with eigenvalues $\tfrac14(1\pm\lvert\vec r\rvert)$, each twice. Its trace is one, its determinant is $\tfrac1{256}(1-\lvert\vec r\rvert^2)^2$, and
$$
\operatorname{Tr}\rho_4^2=\tfrac12\operatorname{Tr}\rho^2=\tfrac14\bigl(1+\lvert\vec r\rvert^2\bigr).
$$
At $\lvert\vec r\rvert=1$ this is $\tfrac12$, not $1$: the purity is halved, because the two copies share the same Bloch vector and the copy label carries no information.

## The Peirce Frame

**The doubled state.** In the regular display the state is
$$
\rho_4=\tfrac12(\rho\oplus\rho),
$$
with eigenvalues $\tfrac14(1\pm\lvert\vec r\rvert)$, each twice. Its trace is one, its determinant is $\tfrac1{256}(1-\lvert\vec r\rvert^2)^2$, and
$$
\operatorname{Tr}\rho_4^2=\tfrac12\operatorname{Tr}\rho^2=\tfrac14\bigl(1+\lvert\vec r\rvert^2\bigr).
$$
At $\lvert\vec r\rvert=1$ this is $\tfrac12$, not $1$: the purity is halved, because the two copies share the same Bloch vector and the copy label carries no information.

**The Born rule.** The probabilities and expectations are the same as in the entry model,
$$
p_\pm=\operatorname{Tr}\bigl(\rho_4\,(\Pi_\pm(\vec u)\oplus\Pi_\pm(\vec u))\bigr)
=\tfrac12\bigl(1\pm\vec r\cdot\vec u\bigr),
\qquad
\langle S_{\vec u}\rangle=\tfrac{\hbar}{2}\vec r\cdot\vec u,
$$
because the trace of the doubled matrix is the trace of one copy and the doubling cancels the factor $\tfrac12$ in the normalisation of the state.

**The copy label.** The doubled state is not a pure state of a four-level system: a pure state there would have rank one, while $\rho_4$ has rank two. The state is the product of the maximally mixed copy label with the algebraic state, and no algebra observable can polarise the label. The spinor picture doubles accordingly: the total space of the Hopf fibration is the diagonal $S^3$ inside $S^3\times S^3$, and the base and the fibre are the same as in the entry model.

## Summary

The Hermitian units map to the Pauli matrices, $\mathsf M_2(i\vec e_k)=\sigma_k$, and the vector units to $-i\sigma_k$; the general element is $Q_t\mathrm I_2-iQ_k\sigma_k$. The spin operators $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$ satisfy $\{\tilde S_i,\tilde S_j\}=\tfrac{\hbar^2}{2}\delta_{ij}e_t$ and $[\tilde S_i,\tilde S_j]=i\hbar\epsilon_{ijk}\tilde S_k$. A state is $\tilde{\varrho}=\tfrac12(e_t+i\vec r)$ with $\lvert\vec r\rvert\le1$, its matrix is $\rho=\tfrac12(\mathrm I_2+\vec r\cdot\vec\sigma)$, and its Bloch vector is recovered by $r_k=\operatorname{Tr}(\rho\sigma_k)=2\langle\tilde{\varrho},i\vec e_k\rangle$. The pure states are the rank-one Hermitian idempotents, $\lvert\vec r\rvert=1$, $N=0$; they are the boundary of the ball and the trace-one slice of the null cone. The measurement formulae are $p_\pm(\vec u)=\tfrac12(1\pm\vec r\cdot\vec u)$ and $\langle S_{\vec u}\rangle=\tfrac{\hbar}{2}\vec r\cdot\vec u$. In the regular display every object is doubled: the state becomes $\tfrac12(\rho\oplus\rho)$, of rank two, with the same Bloch vector and half the purity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma_k$ | the Pauli matrices, images of $i\vec e_k$ |
| $\Sigma_k=\operatorname{diag}(\sigma_k,\sigma_k)$ | their regular images |
| $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$ | the spin operators |
| $\tilde\Pi(\vec u)$ | the pure state along $\vec u$ |
| $\tilde{\varrho}=\tfrac12(e_t+i\vec r)$ | the general state |
| $\rho=\tfrac12(\mathrm I_2+\vec r\cdot\vec\sigma)$ | its matrix |
| $\vec r$ | the Bloch vector |
| $\lvert\vec r\rvert\le1$ | the Bloch ball |
| $p_\pm(\vec u)$ | the Born probabilities |
| $S^3\to S^2$ | the Hopf fibration |

## Further Reading

- [Matrix Representations : The Six Subspaces as Matrix Conditions](matrix-representations-the-six-subspaces-as-matrix-conditions.html), for the real form $\mathbb M_+$
- [Matrix Representations : Peirce Coordinates, Matrix Units and the Spinor Planes](matrix-representations-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the spinor carrier
- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the displays
- [The Pauli Correspondence and the Matrix Image](../articles_physics/the-pauli-correspondence-and-the-matrix-image.html), for the correspondence