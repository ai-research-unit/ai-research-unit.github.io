# __The $M_2(\mathbb{C})$ Representation: The Pauli Correspondence__

## Introduction

The $2\times2$ image is the one in which the algebra looks like the quantum mechanics of a two-state system. The reason is a single line: the three Hermitian units of the algebra map to the three Pauli matrices, and the three vector units map to $-i$ times them. Everything else in the correspondence follows from that line — the observables as Hermitian matrices, the states as positive trace-one matrices, the spin as a triple of commutators, the Bloch ball as the trace-one slice of a cone.

This article states the correspondence and gives its physical interpretations, one by one, each with its boundary. It proves nothing: the identities are proved in the mathematics articles named in the source table, and the formulas of the state space are developed in *$M_2(\mathbb{C})$ Representation : Spin, Qubits and the Bloch Vector*. What this article adds is the reading, and the separation between what the reading says and what it does not.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The assignment $\mathsf M_2(e_t)=\mathrm I_2$, $\mathsf M_2(\vec e_k)=-i\sigma_k$, the isomorphism and the inverse map | [$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure](../articles_maths/m2c-representation-the-matrix-product-and-the-algebra-structure.html) |
| The Hermitian subspace $\mathbb M_+$ as the Hermitian matrices, the anti-Hermitian $\mathbb M_-$ as the anti-Hermitian matrices, and $\mathbb M_-=i\mathbb M_+$ | [$M_2(\mathbb{C})$ Representation : The Six Subspaces as Matrix Conditions](../articles_maths/m2c-representation-the-six-subspaces-as-matrix-conditions.html) |
| $\operatorname{Tr}\mathsf M_2(\tilde Q)=2Q_t$, $\det\mathsf M_2(\tilde Q)=N$, and the norm on each subspace | [$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm](../articles_maths/m2c-representation-trace-determinant-and-the-biquaternion-norm.html) |
| The trace pairing $\tfrac12\operatorname{Tr}(XY)=\langle\tilde P,\tilde Q\rangle$, its Gram matrix and its signature | [$M_2(\mathbb{C})$ Representation : The Four Words and the Four Traces](../articles_maths/m2c-representation-the-four-words-and-the-four-traces.html) |
| Hermitian conjugation ${}^{*}$ as the conjugate transpose, and the four involutions as four matrix operations | [$M_2(\mathbb{C})$ Representation : The Conjugations and the Adjoints](../articles_maths/m2c-representation-the-conjugations-and-the-adjoints.html) |
| The spin operators, the pure states, the density matrix, the Bloch vector and the measurement formulae | [$M_2(\mathbb{C})$ Representation : Spin, Qubits and the Bloch Vector](../articles_maths/m2c-representation-spin-qubits-and-the-bloch-vector.html) |
| The rank-one matrices, the two strata of the null cone and the trace-one idempotents | [$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety](../articles_maths/m2c-representation-rank-one-matrices-and-the-determinantal-variety.html) |
| The unit-norm slice as $SL_2(\mathbb{C})$, the unitary slice as $SU(2)$, and the polar decomposition | [$M_2(\mathbb{C})$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant](../articles_maths/m2c-representation-gl2-sl2-and-the-determinant.html) |

## The Correspondence

### The Assignment on the Units

| unit | matrix | square | Hermitian |
|---|---|---|---|
| $e_t$ | $\mathrm I_2$ | $\mathrm I_2$ | yes |
| $\vec e_x$ | $\begin{pmatrix}0&-i\\-i&0\end{pmatrix}=-i\sigma_1$ | $-\mathrm I_2$ | no |
| $\vec e_y$ | $\begin{pmatrix}0&-1\\1&0\end{pmatrix}=-i\sigma_2$ | $-\mathrm I_2$ | no |
| $\vec e_z$ | $\begin{pmatrix}-i&0\\0&i\end{pmatrix}=-i\sigma_3$ | $-\mathrm I_2$ | no |
| $i\vec e_x$ | $\sigma_1$ | $\mathrm I_2$ | yes |
| $i\vec e_y$ | $\sigma_2$ | $\mathrm I_2$ | yes |
| $i\vec e_z$ | $\sigma_3$ | $\mathrm I_2$ | yes |

The table is the whole correspondence. The algebra's own basis goes to $-i$ times the Pauli matrices; the Hermitian basis, which is the basis multiplied by $i$, goes to the Pauli matrices themselves. There is no third case: the factor $i$ is the only difference between the two rows.

### The General Element

$$
\boxed{\;\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i\bigl(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3\bigr)=
\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}\;}.
$$

The scalar part multiplies the identity and the vector part multiplies the three Pauli matrices with the factor $-i$. In the Hermitian sector, where $Q_t$ is real and $Q_k=iq'_k$ with $q'_k$ real, the same formula reads

$$
\mathsf M_2(\tilde Q)=q_t\mathrm I_2+q'_x\sigma_1+q'_y\sigma_2+q'_z\sigma_3 ,
$$

with no factor and no sign. The four real numbers of a Hermitian element are the coefficients of the identity and the three Pauli matrices.

### The Hermitian Units

The three elements $i\vec e_k$ are Hermitian, and so are their images $\sigma_k$. The three elements $\vec e_k$ are anti-Hermitian, and so are their images $-i\sigma_k$. Hermitian conjugation on the algebra becomes the conjugate transpose on the matrices,

$$
\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger},
$$

so the fixed space of ${}^{*}$ is carried onto the fixed space of the dagger. That identity is the algebraic fact behind the word **observable**, and it is the subject of the first interpretation below.

## The Factor $i$ Is the Complex Structure

**The factor is forced.** A $2\times2$ matrix with real entries and square $-\mathrm I_2$ defines a complex structure on $\mathbb R^2$; three of them, anticommuting, define the quaternionic structure. The algebra in which $\vec e_k^2=-e_t$ holds is the complexified one, and the coefficient field supplies the $i$ that turns $\sigma_k$ into $-i\sigma_k$. With the assignment $\vec e_k\mapsto\sigma_k$ the square would be $+\mathrm I_2$, which is the split-quaternion sign, not the quaternion one.

**The sign is then forced.** The alternative assignment $\vec e_k\mapsto-\mathsf M_2(\vec e_k)$ preserves the squares and fails the products: $\vec e_x\vec e_y=\vec e_z$ becomes $(-\mathsf M_2(\vec e_x))(-\mathsf M_2(\vec e_y))=\mathsf M_2(\vec e_z)$, which is minus the image of $\vec e_z$ under that assignment. The check is two lines of matrix multiplication, and it fixes the sign.

**The interpretation.** The factor $i$ is not a bookkeeping convention of physicists. It is the statement that the three directions of the algebra are generators of rotations and not observables: $\vec e_k$ is anti-Hermitian and generates, $i\vec e_k$ is Hermitian and is measured. The two roles differ by the factor that the complexification supplies.

**The boundary.** This explains why the factor is present in the model. It does not say that nature is complex, and it does not derive the complex numbers from anything physical. The complex field is the coefficient field of the algebra, fixed before any interpretation begins.

## Physical Interpretations

### The Hermitian Elements Are the Observables

An element $\tilde H\in\mathbb M_+$ has a Hermitian matrix, and a Hermitian matrix has real eigenvalues and an orthogonal eigenbasis. The spectral theorem for the matrix is therefore the spectral statement for the element, and the eigenvalues are the possible outcomes of a measurement of $\tilde H$.

The identification is exact: $\mathbb M_+$ is carried onto the Hermitian matrices, and the expectation is the trace of the product,

$$
\operatorname{Tr}\bigl(\mathsf M_2(\tilde{Ϛ})\mathsf M_2(\tilde H)\bigr)=2\langle\tilde{Ϛ},\tilde H\rangle_{*}=h_t+\vec r\cdot\vec h ,
$$

for the state $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$ of trace one.

**Boundary.** The word *observable* uses the involution ${}^{*}$, which belongs to the real structure of $\mathbb B$. The complex isomorphism $\mathbb B\cong M_2(\mathbb{C})$ alone does not single out $\mathbb M_+$: it carries $\mathbb M_+$ and $\mathbb M_-$ to two complementary subspaces of the same complex algebra, and the choice between them is physical. A reader who knows only the complex algebra cannot tell which half is measured.

### The Three Directions Are the Three Spin Axes

A traceless Hermitian element is $\tilde H=i\vec h$ with $\vec h\in\mathbb R^3$, and its matrix is $\vec h\cdot\vec\sigma$. The three coefficients are the components of a spatial vector, and the three Pauli matrices are the three components of the measurement. For the spin operators $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$ the matrix is $\tfrac{\hbar}{2}\sigma_k$, and the commutator

$$
[\tilde S_i,\tilde S_j]=i\hbar\,\epsilon_{ijk}\tilde S_k
$$

is the angular-momentum algebra. The three directions close under the commutator into $\mathfrak{su}(2)$, and the exponentials are the rotations of the state space.

**Boundary.** The naming of the three directions $x,y,z$ is a choice of basis, and the algebra has no preferred axis. A rotation of $\mathbb R^3$ permutes the three operators and conjugates the matrices; the physics is invariant, the labels are not.

### The Trace Is the Weight

The trace of the matrix is twice the scalar part, $\operatorname{Tr}\mathsf M_2(\tilde Q)=2Q_t$. On a state the trace is normalised to one, and the scalar part is then $\tfrac12$. The factor two is the dimension of the spinor module, not a physical factor: it appears because the identity is a $2\times2$ matrix.

**Boundary.** The trace is additive and blind to the vector part. It cannot distinguish two states with the same scalar part, and it is not the norm. The invariant that sees the whole element is the determinant.

### The Determinant Is the Invariant

The determinant of the matrix is the quaternionic norm, $\det\mathsf M_2(\tilde Q)=N(\tilde Q)$, and it reads differently on the two sectors:

| sector | element | determinant | signature |
|---|---|---|---|
| material | $iq'_te_t+q_k\vec e_k$ | $-(q'_t)^2+q_x^2+q_y^2+q_z^2$ | $(3,1)$ |
| informational | $q_te_t+iq'_k\vec e_k$ | $q_t^2-(q'_x)^2-(q'_y)^2-(q'_z)^2$ | $(1,3)$ |
| state slice | $\tfrac12(e_t+i\vec r)$ | $\tfrac14(1-\lvert\vec r\rvert^2)$ | positivity |

The same algebraic function is the interval on the material sector, the causal type and the positivity test on the informational sector, and the mixedness on the trace-one slice. The zero set is one object in the three readings: the light cone, the boundary of the state space, and the set of pure states.

**Boundary.** These are three restrictions of one function to three different real slices, not three different quantities. A statement about the determinant must say which slice it is on, because the sign, the signature and the physical meaning all change with the slice and the zero set does not.

### The Determinant Is a Volume

Multiplication by $M$ is a real linear map of $\mathbb C^2\cong\mathbb R^4$, and its real determinant is $\lvert\det M\rvert^2$. The complex determinant is the complex area scale of the parallelogram spanned by the two columns, and the real volume scale is its squared modulus. On the unit-norm slice $N=1$, that is $\det M=1$, the real determinant is $1$: the group is $SL_2(\mathbb C)$, and its action preserves the real volume. The larger slice $\lvert\det M\rvert=1$ also preserves it.

**Boundary.** The volume is the volume of the realification of the module, not a spacetime volume. On the material sector the same determinant is the interval, and an interval is not a volume. The two readings coincide in the zero set and nowhere else.

### The State Is the Positive Trace-One Matrix

A state is a Hermitian element of trace one whose matrix is positive semidefinite. In the model it is

$$
\tilde{Ϛ}=\tfrac12(e_t+i\vec r),
\qquad
\rho=\mathsf M_2(\tilde{Ϛ})=\tfrac12\bigl(\mathrm I_2+\vec r\cdot\vec\sigma\bigr),
\qquad \lvert\vec r\rvert\le1 .
$$

The trace-one condition is the normalisation, the positivity is the condition $\lvert\vec r\rvert\le1$, and the purity is the boundary $\lvert\vec r\rvert=1$. The state space is the Bloch ball, the pure states are its boundary and the maximally mixed state is its centre.

**Boundary.** Positivity is not a property of the complex algebra. It uses the involution ${}^{*}$ and the orientation of $\mathbb M_+$, and it is the matrix form of the statement that the state space is the positive cone of the informational sector, intersected with the trace-one slice.

### The Central Phase Is the Fibre

The central element $e^{i\alpha}e_t$ maps to the scalar matrix $e^{i\alpha}\mathrm I_2$. It multiplies the element matrix by a phase, multiplies the determinant by $e^{2i\alpha}$, multiplies a state by $e^{i\alpha}$ and therefore does not preserve the trace-one slice, and it acts trivially in the sandwich. A pure state is a ray, not a vector: the spinor $\xi$ and $e^{i\alpha}\xi$ give the same $\rho$, and the circle of phases over each pure state is the fibre of the Hopf bundle.

**Boundary.** The bundle, its connection, its curvature and its holonomy are owned by *The Hopf Fibration and the Biquaternion Gauge Bundle* and by *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*. This article records the matrix identity — the phase is a scalar matrix and disappears from the congruence — and adds no topology.

### The Double Cover Is the Spin

The unit-norm elements are $SL_2(\mathbb{C})$, and it covers the proper orthochronous Lorentz group two-to-one with kernel $\{\pm\mathrm I_2\}$. A rotation through $2\pi$ gives $-\mathrm I_2$ and a rotation through $4\pi$ gives $\mathrm I_2$. The sign is the sign of the spinor, and it is the discrete difference between the spinor picture and the four-vector picture.

**Boundary.** The double cover is a statement about the group, not about a particular state. It says that the two matrices $\pm M$ define the same transformation of the material sector; it does not say that the two signs are physically distinguishable for every state.

## The Sign and the Conventions

**The alternative assignment fails.** If the three vector units were sent to $+\sigma_k$ instead of $-i\sigma_k$, the squares would be $+\mathrm I_2$ and the product $\vec e_x\vec e_y$ would be $\sigma_x\sigma_y=i\sigma_z$, while the image of $\vec e_z$ would be $\sigma_z$. The assignment is therefore fixed by the multiplication table, not chosen.

**What a convention can change.** Two conventions are common in the literature. The first drops the factor $i$ and writes the generators as $\sigma_k$, which is the same algebra written with anti-Hermitian generators renamed; the second chooses $\sigma_2$ with the opposite sign, which is conjugation by a diagonal phase. Both change the entries and the signs of the commutators, and neither changes the algebra or the physics.

**Boundary.** A convention is not a symmetry. Once a convention is chosen, every formula must be read in it, and the factor $i$ between $\vec e_k$ and $i\vec e_k$ is the place where the errors concentrate.

## Limits

**The correspondence does not derive quantum mechanics.** It identifies which matrices carry the observables and the states. It does not produce a Hilbert space of states of a field, a Hamiltonian, a dynamics or a probability rule beyond the finite-dimensional Born pairing.

**The real form is extra data.** The identification $\mathbb B\cong M_2(\mathbb{C})$ is an isomorphism of complex algebras. The Hermitian sector, the positivity and the word *observable* use ${}^{*}$ and the choice of $\mathbb M_+$, which are not visible in the complex algebra alone.

**The Pauli matrices are not elements of the algebra.** They are the images of $i\vec e_k$. The real span of $\{\mathrm I_2,\sigma_1,\sigma_2,\sigma_3\}$ is the Hermitian subspace, which is not closed under multiplication; the complex span is the whole matrix algebra. A statement that identifies the algebra with the Pauli algebra is true only over $\mathbb C$ and only after the factor $i$ has been accounted for.

**One chirality.** The $2\times2$ image carries one copy of the spinor module. The second chirality is the conjugate module, and the mass coupling between the two is a right multiplication, which the $2\times2$ element picture alone does not show. The regular $4\times4$ image is the one that displays both copies.

**No dynamics, no position, no field.** The spin operators generate rotations of the state space, and the Hamiltonian that would generate a motion in time is a choice of observable, not a consequence of the model.

## Summary

The correspondence is $\mathsf M_2(\vec e_k)=-i\sigma_k$ and $\mathsf M_2(i\vec e_k)=\sigma_k$, so the general element is $Q_t\mathrm I_2-iQ_k\sigma_k$ and the Hermitian element is $q_t\mathrm I_2+q'_k\sigma_k$. Hermitian conjugation becomes the conjugate transpose, so the fixed space of ${}^{*}$ is the Hermitian matrices and the Hermitian elements are the observables. The three Hermitian units are the three spin directions, with $[\tilde S_i,\tilde S_j]=i\hbar\epsilon_{ijk}\tilde S_k$. The trace is twice the scalar part, the determinant is the norm, and the norm is the interval on the material sector, the causal type on the informational sector and the mixedness on the trace-one slice. The state is the positive trace-one matrix $\tfrac12(\mathrm I_2+\vec r\cdot\vec\sigma)$ with $\lvert\vec r\rvert\le1$, the pure states are the boundary $\lvert\vec r\rvert=1$, and the central phase is the scalar matrix that acts trivially in the sandwich. The factor $i$, the sign and the reality of the observables are forced by the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf M_2$ | the fixed $2\times2$ matrix model |
| $\sigma_1,\sigma_2,\sigma_3$ | the Pauli matrices, $\sigma_k=\mathsf M_2(i\vec e_k)$ |
| $\mathbb M_+,\mathbb M_-$ | the Hermitian and anti-Hermitian subspaces |
| $\tilde H$ | a Hermitian observable |
| $\tilde{Ϛ}$ | a state, $\tfrac12(e_t+i\vec r)$ |
| $\rho=\mathsf M_2(\tilde{Ϛ})$ | the density matrix |
| $N=\det\mathsf M_2$ | the quaternionic norm |
| $\vec r$ | the Bloch vector |

## Further Reading

- [The Element and Operator Representations](the-element-and-operator-representations.html), for the correspondence table of the four matrix pictures
- [The Matrix Images: Mixedness, Rapidity and the Phase Fibre](the-matrix-images-mixedness-rapidity-and-the-phase-fibre.html), for the phase fibre and the mixedness interpretation
- [The Spinor Module and Its Two Structures](the-spinor-module-and-its-two-structures.html), for the Born pairing and the Hilbert structure
- [The Bloch Ball as the Normalised Slice of the Future Light Cone](the-bloch-ball-as-the-trace-one-slice-of-the-future-light-cone.html), for the state geometry
- [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html), for the spin operators in the algebra
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four forms read physically
- [The Hopf Fibration and the Biquaternion Gauge Bundle](the-hopf-fibration-and-the-biquaternion-gauge-bundle.html), for the bundle over the state space
- [Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form](pancharatnams-phase-and-the-polarization-sphere-in-biquaternionic-form.html), for the phase rule
