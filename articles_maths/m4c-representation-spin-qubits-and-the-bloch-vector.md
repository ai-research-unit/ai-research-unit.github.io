# __$M_4(\mathbb{C})_L$ Representation : Spin, Qubits and the Bloch Vector__

## Introduction

The regular model carries two copies of the spinor module. A Hermitian element acts on the two copies by the same $2\times2$ matrix, so its Bloch vector is repeated: the algebra's state is read twice, and the copy label is unpolarized. The pure states of the algebra become rank-two projectors, not rank-one projectors, and the normalized $4\times4$ density matrix is a product of the maximally mixed copy label with the algebraic state.

This article develops the Hermitian basis, the spin operators, the pure and general states, the Bloch vector and the doubling. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Representation : Spin, Qubits and the Bloch Vector*.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})_L$ Representation : The Matrix Product and the Algebra Structure*. The Pauli matrices are $\sigma_1,\sigma_2,\sigma_3$, and
$$
\Sigma_k=\mathsf{M}_4(i\vec e_k),
\qquad
\mathsf{M}_4(\vec e_k)=-i\Sigma_k.
$$
In the Peirce basis, $\Sigma_k=\operatorname{diag}(\sigma_k,\sigma_k)$; in the fixed coefficient basis the block form is conjugated by $S$.
The Hermitian subspace is $\mathbb{M}_+$. A state is written $\tilde\varrho$ and its Bloch vector $\vec r=(r_1,r_2,r_3)\in\mathbb{R}^3$.

**Boundaries.** The spinor module is *$M_4(\mathbb{C})_L$ Representation : The Columns, the Rows and the Spinor Spaces*; the spectral projectors are *$M_4(\mathbb{C})_L$ Representation : The Spectral Projectors and the Nilpotents*; the physical reading is *The $M_2(\mathbb{C})$ Representation: The Pauli Correspondence*; the $2\times2$ version is *$M_2(\mathbb{C})$ Representation : Spin, Qubits and the Bloch Vector*.

## The Hermitian Basis

**The Pauli matrices are the images of the Hermitian units.** Since $\mathsf{M}_4$ is $\mathbb{C}$-linear,
$$
\mathsf{M}_4(\vec e_k)=-i\Sigma_k,
\qquad
\mathsf{M}_4(i\vec e_k)=\Sigma_k.
$$

| unit | image | square | Hermitian |
|---|---|---|---|
| $e_t$ | $\mathrm I_4$ | $\mathrm I_4$ | yes |
| $\vec e_k$ | $-i\Sigma_k$ | $-\mathrm I_4$ | no |
| $i\vec e_k$ | $\Sigma_k$ | $\mathrm I_4$ | yes |

**The general element.** Expanding on the basis,
$$
\mathsf{M}_4(\tilde Q)=Q_t\mathrm I_4-i\bigl(Q_x\Sigma_1+Q_y\Sigma_2+Q_z\Sigma_3\bigr).
$$

**The Hermitian condition.** An element lies in $\mathbb{M}_+$ exactly when $Q_t$ is real and the three $Q_k$ are purely imaginary:
$$
\tilde Q=q_t e_t+i\bigl(q'_x\vec e_x+q'_y\vec e_y+q'_z\vec e_z\bigr),
\qquad q_t,q'_k\in\mathbb{R}.
$$
Its image is
$$
\mathsf{M}_4(\tilde Q)=q_t\mathrm I_4+q'_x\Sigma_1+q'_y\Sigma_2+q'_z\Sigma_3.
$$
In the Peirce basis it is
$$
\operatorname{diag}(q_t\mathrm I_2+q'_k\sigma_k,\ q_t\mathrm I_2+q'_k\sigma_k),
$$
which is Hermitian, and every Hermitian matrix of the image arises this way. The map is an isomorphism of real vector spaces
$$
\mathbb{M}_+\longrightarrow \operatorname{Herm}_4(\mathbb{C})_L,
\qquad
q_t e_t+iq'_k\vec e_k\longmapsto q_t\mathrm I_4+q'_k\Sigma_k.
$$

**The four real coordinates.** The coefficient $q_t$ is the weight of the identity and the three $q'_k$ are the weights of the Pauli matrices, repeated in both blocks. They are the four real numbers of a Hermitian element, and the passage between the two writings has no factor and no sign.

## The Spin Operators

**Definition.** The spin operators are
$$
\tilde S_k=\tfrac{\hbar}{2}i\vec e_k,
\qquad
\mathsf{M}_4(\tilde S_k)=\tfrac{\hbar}{2}\Sigma_k.
$$
They are Hermitian elements of $\mathbb{M}_+$; in the Peirce basis their images are block-diagonal Hermitian matrices.

**The algebra.** The Pauli matrices satisfy
$$
\sigma_i\sigma_j=\delta_{ij}\mathrm I_2+i\epsilon_{ijk}\sigma_k,
$$
and therefore
$$
\Sigma_i\Sigma_j=\delta_{ij}\mathrm I_4+i\epsilon_{ijk}\Sigma_k.
$$
The spin operators obey
$$
\{\tilde S_i,\tilde S_j\}=\tfrac{\hbar^2}{2}\delta_{ij}e_t,
\qquad
[\tilde S_i,\tilde S_j]=i\hbar\,\epsilon_{ijk}\tilde S_k.
$$
The commutator is the angular-momentum algebra of a spin-$\tfrac12$ system, and the representation is two copies of the fundamental representation: the eigenvalues of each $\tilde S_k$ are $\pm\hbar/2$, each twice.

**Two roles of one direction.** The commutator is anti-Hermitian, so it lies in $\mathbb{M}_-$: the generators of the unitary group are the elements $\vec e_k$, whose images $-i\Sigma_k$ are anti-Hermitian. The observables are the elements $i\vec e_k$, whose images $\Sigma_k$ are Hermitian. The same three directions appear twice, as generators and as observables, and the two appearances differ by the factor $i$.

**The span.** The three spin operators span over $\mathbb{R}$ the traceless Hermitian subspace of the image, of real dimension three. With the identity they span the whole of $\mathbb{M}_+$, of real dimension four. They do not span the algebra over $\mathbb{R}$: the products $\Sigma_i\Sigma_j$ leave the Hermitian subspace whenever $i\neq j$.

## Pure States

**Definition.** For a real unit vector $\vec u$,
$$
\tilde\Pi(\vec u)=\tfrac12\bigl(e_t+i\vec u\bigr)
=\tfrac12\bigl(e_t+iu_1\vec e_x+iu_2\vec e_y+iu_3\vec e_z\bigr).
$$

**Proposition.** $\tilde\Pi(\vec u)$ is a Hermitian idempotent of trace one and determinant zero, and
$$
\mathsf{M}_4\bigl(\tilde\Pi(\vec u)\bigr)
=\tfrac12\bigl(\mathrm I_4+\vec u\cdot\vec\Sigma\bigr)
=\operatorname{diag}\bigl(\tfrac12(\mathrm I_2+\vec u\cdot\vec\sigma),\ \tfrac12(\mathrm I_2+\vec u\cdot\vec\sigma)\bigr)
\quad\text{(Peirce basis)}
$$
is a rank-two projector of trace two.

*Proof.* The image is Hermitian because $\vec u$ is real. It squares to itself because $(\vec u\cdot\vec\Sigma)^2=|\vec u|^2\mathrm I_4=\mathrm I_4$. Its trace is $2$ and its determinant is $0$, so it has rank two; a rank-two Hermitian idempotent is the orthogonal projector onto its image, which is $W\oplus W$ for the line $W$ of the spinor of spin up along $\vec u$. $\square$

**The normalized state.** The trace-one density matrix is
$$
\rho_4(\vec u)=\tfrac12\mathsf{M}_4\bigl(\tilde\Pi(\vec u)\bigr)
=\tfrac14\bigl(\mathrm I_4+\vec u\cdot\vec\Sigma\bigr)
=\tfrac12\mathrm I_2\otimes\tilde\Pi(\vec u),
$$
where the first factor is the copy label and the tensor product is in the Peirce basis. It is a rank-two state of purity $\tfrac12$, not a pure state of the four-level system. The algebraic pure state is pure in the algebra; in the regular model it is a product of the maximally mixed copy label with that pure state.

**The complementary state.** $\tilde\Pi(\vec u)+\tilde\Pi(-\vec u)=e_t$, and
$$
\mathsf{M}_4\bigl(\tilde\Pi(-\vec u)\bigr)=\mathrm I_4-\mathsf{M}_4\bigl(\tilde\Pi(\vec u)\bigr),
$$
so the two projectors are complementary and orthogonal.

**The null cone.** A pure state has $N(\tilde\Pi(\vec u))=0$ and scalar part $\tfrac12$, so it lies on the null cone. Its image has rank two and determinant zero; it is a projector, not a nilpotent. The two notions of purity must not be conflated: the null cone contains both strata, and the pure states are the idempotent half.

**The sphere.** The map $\vec u\mapsto\tilde\Pi(\vec u)$ is a bijection from the unit sphere onto the set of pure states of the algebra. The antipodal point gives the orthogonal state, $\tilde\Pi(\vec u)\tilde\Pi(-\vec u)=0$. The state is a point of the sphere, not a spinor: the spinor is defined up to a phase, and the phase is the circle over the point.

## The General State

**Definition.** A state is a Hermitian element of trace one whose matrix is positive semidefinite:
$$
\tilde\varrho=\tfrac12\bigl(e_t+i\vec r\bigr),
\qquad \vec r\in\mathbb{R}^3,
\qquad
\mathsf{M}_4(\tilde\varrho)=\operatorname{diag}(\rho,\rho)
\quad\text{(Peirce basis)},
\qquad
\rho=\tfrac12\bigl(\mathrm I_2+\vec r\cdot\vec\sigma\bigr).
$$
The normalized trace-one matrix is
$$
\rho_4=\tfrac12\operatorname{diag}(\rho,\rho)=\tfrac12\mathrm I_2\otimes\rho
\quad\text{(Peirce basis)}.
$$

**The Bloch vector.** The vector $\vec r$ is read from the matrix by
$$
r_k=\operatorname{Tr}\bigl(\rho_4\Sigma_k\bigr),
$$
because each copy contributes $\tfrac12\operatorname{Tr}(\rho\sigma_k)$ and the two contributions add to $\operatorname{Tr}(\rho\sigma_k)=r_k$.

**The positivity.** The matrix $\rho$ is positive semidefinite exactly when $|\vec r|\le1$, and then $\rho_4$ is positive semidefinite with eigenvalues the halves of those of $\rho$, each twice. The Bloch ball $|\vec r|\le1$ is therefore a three-dimensional slice of the fifteen-dimensional state space of the image.

**The purity.** The purity of the $4\times4$ state is
$$
\operatorname{Tr}(\rho_4^2)=\tfrac12\operatorname{Tr}(\rho^2)=\tfrac14(1+|\vec r|^2),
$$
which is $\tfrac12$ on the Bloch sphere and $\tfrac14$ at the centre. At the Bloch sphere the deficit $\tfrac12$ is the maximally mixed copy label; away from it the deficit also includes the mixedness of $\rho$. The two copies are equally weighted, and no measurement of the algebra can polarize the label.

**The two copies.** In the Peirce basis the state is block diagonal, so the two copies carry the same Bloch vector $\vec r$. The copy label is the maximally mixed state $\tfrac12\mathrm I_2$, and the two copies carry the same spin state: a measurement of the spin in either copy gives the same distribution, while the label itself carries no polarization. The left action of the algebra preserves the two copies and the right action mixes them; the state is diagonal in the copy label, so it has no coherence between the copies.

## The Born Rule and the Convex Splitting

**The Born rule.** For a measurement along the unit vector $\vec u$, the two outcomes have probabilities
$$
p_\pm=\operatorname{Tr}\bigl(\rho_4\,\Pi^4_\pm(\vec u)\bigr)
=\tfrac12\bigl(1\pm\vec r\cdot\vec u\bigr),
\qquad
\Pi^4_\pm(\vec u)=\tfrac12\bigl(\mathrm I_4\pm\vec u\cdot\vec\Sigma\bigr).
$$
The probabilities are non-negative exactly when $\lvert\vec r\rvert\le1$, and they sum to one. The two copies contribute equally, and the trace kills the copy label. The expectation of the spin operator $\tfrac{\hbar}{2}\vec u\cdot\vec\Sigma$ is $\tfrac{\hbar}{2}\vec r\cdot\vec u$.

**The convex splitting.** For $\vec r\neq0$ every state is a convex combination of the two pure states along its own axis:
$$
\rho_4=\frac{1+\lvert\vec r\rvert}{2}\,\Pi^4_+(\hat r)
+\frac{1-\lvert\vec r\rvert}{2}\,\Pi^4_-(\hat r),
\qquad
\hat r=\frac{\vec r}{\lvert\vec r\rvert},
$$
and for $\vec r=0$ the state is $\tfrac14\mathrm I_4$. The weights are non-negative and sum to one. The decomposition is the chord of the Bloch ball through the centre, doubled: the state lies on the segment between the two boundary points $\pm\hat r$, and its distance from the centre is the bias of the mixture.

**The geometry.** The pure states are the boundary sphere, the maximally mixed state is the centre, and the ball is convex. The matrix form of the convex structure is the statement that the positive semidefinite matrices of trace one in the image form a convex set whose extreme points are the rank-two projectors $\tfrac12(\mathrm I_4+\vec u\cdot\vec\Sigma)$.

## Reading the Vector Back

**Proposition.** The Bloch coordinates are the traces against the Pauli matrices,
$$
r_k=\operatorname{Tr}\bigl(\rho_4\,\Sigma_k\bigr),
$$
and, in the algebra, twice the trace pairing against the Hermitian units,
$$
r_k=2\bigl\langle\tilde{\varrho},i\vec e_k\bigr\rangle.
$$

*Proof.* The first identity follows from $\operatorname{Tr}\Sigma_k=0$ and $\operatorname{Tr}(\Sigma_j\Sigma_k)=4\delta_{jk}$, together with the normalization $\rho_4=\tfrac12\mathrm I_2\otimes\rho$. The second is the trace pairing of *$M_4(\mathbb{C})_L$ Representation : The Four Words and the Four Traces* applied to $\tilde{\varrho}$ and $i\vec e_k$, with the factor two of the duplication.

**The reconstruction.** The three numbers $r_k$ determine the state, because
$$
\rho_4=\tfrac14\Bigl(\mathrm I_4+r_k\Sigma_k\Bigr),
$$
and the four matrices $\mathrm I_4,\Sigma_1,\Sigma_2,\Sigma_3$ are a basis of the Hermitian matrices of the image over $\mathbb R$. The state, the matrix and the vector are three writings of four real numbers.

**The measurement formulae.** For a unit vector $\vec u$, the probability of the outcome $+$ in the measurement of the spin along $\vec u$ is
$$
p_+(\vec u)=\operatorname{Tr}\bigl(\rho_4\,\mathsf M_4(\tilde\Pi(\vec u))\bigr)
=\tfrac12\bigl(1+\vec r\cdot\vec u\bigr),
$$
and the probability of the outcome $-$ is $p_-=\tfrac12(1-\vec r\cdot\vec u)$. The expectation of the spin is
$$
\langle S_{\vec u}\rangle=\operatorname{Tr}\bigl(\rho_4\,\mathsf M_4(\tilde S_{\vec u})\bigr)
=\tfrac{\hbar}{2}\,\vec r\cdot\vec u.
$$
More generally, for a Hermitian observable $\tilde H=h_t e_t+i\vec h$ the expectation is
$$
\operatorname{Tr}\bigl(\rho_4\,\mathsf M_4(\tilde H)\bigr)=h_t+\vec r\cdot\vec h,
$$
which is the affine function of the state determined by the four numbers $(h_t,\vec h)$. The Born pairing of *The Spinor Module and Its Two Structures* is the same identity written with the state idempotent, and the doubling cancels because both copies carry the same state.

## The Qubit as a Spinor

**The pure case.** Every pure state of the algebra is a rank-one projector $\Pi=\xi\xi^{\dagger}$, and its regular image is
$$
\rho_4=\tfrac12\bigl(\Pi\oplus\Pi\bigr)
=\tfrac12\bigl((\xi\oplus0)(\xi\oplus0)^{\dagger}+(0\oplus\xi)(0\oplus\xi)^{\dagger}\bigr),
$$
a rank-two projector with Bloch vector
$$
r_k=\xi^{\dagger}\sigma_k\xi.
$$
The vector $\xi$ is defined up to a phase, $\xi\mapsto e^{i\alpha}\xi$, and the phase cancels in $\rho$: the state is the ray, not the vector. In the algebra the spinor is an element of the minimal left ideal $\mathbb B\tilde\Pi_+$, and the module structure that makes it a Hilbert space is the second structure of *The Spinor Module and Its Two Structures*.

**The mixed case.** A general state is a convex combination of pure ones,
$$
\rho_4=\sum_i p_i\,\tfrac12(\Pi_i\oplus\Pi_i),
\qquad p_i\ge0,\quad \sum_i p_i=1,
$$
and the Bloch vector is the corresponding convex combination of the pure Bloch vectors. The ball is the convex hull of the sphere, which is the matrix form of the statement that every state is a mixture.

**The phase and the Hopf fibration.** The central phase $e^{i\alpha}e_t$ acts on the spinor by multiplication and on the algebra by the identity sandwich. In the regular model the spinor is doubled, $\xi\oplus\xi$, and the projector is $\Pi\oplus\Pi$. The map
$$
S^3\longrightarrow S^2,\qquad \xi\longmapsto\vec r
$$
is the Hopf fibration, with fibre $S^1$; in the regular model the total space is the diagonal $S^3$ inside $S^3\times S^3$, and the base sphere and the fibre are the same. The left action preserves each copy and the right action mixes them, so the two copies give the two chiralities of *$M_4(\mathbb{C})_L$ Representation : The Columns, the Rows and the Spinor Spaces*.

**The copy label.** The doubled spinor is not a spinor of the four-level system: it is two copies of the same spinor, and the state is the product of the maximally mixed copy label with the algebraic state. The phase circle over each pure state is the fibre of *The Matrix Images: Mixedness, Rapidity and the Phase Fibre*.

## Where the Correspondence Stops

**The Pauli matrices are not elements of the algebra.** They are the images of $i\vec e_k$, and the algebra's own units are $-i\sigma_k$, doubled. A statement about the $\Sigma_k$ must be translated back through the factor $i$ before it is a statement about $\mathbb B$; the commutator of two Pauli matrices is $i$ times a Pauli matrix, and the commutator of two algebra units is an algebra unit.

**The real form is extra data.** The identification $\mathbb B\cong M_2(\mathbb C)$ is an isomorphism of complex algebras, and it does not by itself select $\mathbb M_+$. The statement that the Hermitian elements are the observables uses the involution ${}^{*}$, which is part of the real structure of $\mathbb B$ and is not visible in the complex algebra alone. The same matrix algebra carries the anti-Hermitian sector, and the choice between the two sectors is a physical choice, not a matrix identity.

**The multiplicity is extra data.** The regular model doubles every state, and the doubling is not a physical two-level system: the copy label is maximally mixed and no algebra observable can polarize it. A measurement on the four-level matrix sees the same Bloch vector in both copies, and the purity is halved. The physical content is in the algebra, not in the multiplicity.

**No dynamics.** Nothing in this article evolves a state. The spin operators generate the rotations of the state space through the commutator, and the Hamiltonian that would generate a motion in time is a choice of observable, not a consequence of the model.

## Summary

The Hermitian basis of the regular image is $\mathrm I_4$ and the three Pauli matrices $\Sigma_k$, block diagonal in the Peirce basis. The spin operators are $\tfrac{\hbar}{2}\Sigma_k$, and they represent two copies of the spin-$\tfrac12$ algebra. A pure state $\tilde\Pi(\vec u)$ maps to the rank-two projector $\tfrac12(\mathrm I_4+\vec u\cdot\vec\Sigma)$, and the normalized density matrix is $\tfrac12\mathrm I_2\otimes\tilde\Pi(\vec u)$, a product of the maximally mixed copy label with the algebraic state. A general state has the Bloch vector $\vec r$ repeated in both copies, positivity $|\vec r|\le1$, and purity $\tfrac14(1+|\vec r|^2)$. The Hopf fibration is the same on both copies.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Sigma_k=\mathsf{M}_4(i\vec e_k)$ | the Pauli matrices, block diagonal in the Peirce basis |
| $\tilde\Pi(\vec u)=\tfrac12(e_t+i\vec u)$ | the pure state of the algebra |
| $\tfrac12(\mathrm I_4+\vec u\cdot\vec\Sigma)$ | its rank-two projector |
| $\rho_4=\tfrac12\mathrm I_2\otimes\rho$ | the normalized $4\times4$ state |
| $\vec r$ | the Bloch vector, repeated in both copies |
| $\operatorname{Tr}(\rho_4^2)=\tfrac14(1+\lvert\vec r\rvert^2)$ | the purity |

## Further Reading

- [$M_4(\mathbb{C})_L$ Representation : The Columns, the Rows and the Spinor Spaces](m4c-representation-the-columns-the-rows-and-the-spinor-spaces.html), for the two copies
- [$M_4(\mathbb{C})_L$ Representation : The Spectral Projectors and the Nilpotents](m4c-representation-the-spectral-projectors-and-the-nilpotents.html), for the projectors
- [$M_2(\mathbb{C})$ Representation : Spin, Qubits and the Bloch Vector](m2c-representation-spin-qubits-and-the-bloch-vector.html), for the $2\times2$ version
- [The Spinor Module and Its Two Structures](../articles_physics/the-spinor-module-and-its-two-structures.html), for the spinor
- [The $M_2(\mathbb{C})$ Representation: The Pauli Correspondence](../articles_physics/the-m2c-representation-and-the-pauli-correspondence.html), for the physical reading
