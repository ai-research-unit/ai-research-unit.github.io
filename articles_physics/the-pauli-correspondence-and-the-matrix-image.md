# __The Pauli Correspondence and the Matrix Image__

## Introduction

The $2\times2$ image is the one in which the algebra looks like the quantum mechanics of a two-state system. The reason is a single line: the three Hermitian units of the algebra map to the three Pauli matrices, and the three vector units map to $-i$ times them. Everything else follows from that line: the observables as Hermitian matrices, the states as positive trace-one matrices, the spin as a triple of commutators, the Bloch ball as the trace-one slice of a cone.

The matrix has two uses, and the article keeps them apart. The **element image** $\mathsf M_2(\tilde Q)$ is the element acting on the spinor module; it carries the data an object acts on. The **map image** $\mathsf M_4^{L}(\tilde Q)$ is the element acting on the algebra itself; it carries the objects. The sandwich is a third matrix, quadratic in the element. The three have different traces, different determinants and different spectra, and only the vanishing set is common. The doubling is the dimension of the module, not a physical factor.

The article states the correspondence and reads its invariants: the trace as the weight, the determinant as the norm and the mixedness, the eigenvalues as the doubled rapidity, the phase as the fibre of the Hopf bundle. It proves nothing: the identities are proved in the mathematics articles named in the source table. What it adds is the reading, and the separation between what the reading says and what it does not.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The assignment $\mathsf M_2(e_t)=\mathrm I_2$, $\mathsf M_2(\vec e_k)=-i\sigma_k$, the isomorphism and the inverse map | [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](../articles_maths/m2c-model-the-product-the-trace-and-the-determinant.html) |
| The Hermitian subspace $\mathbb M_+$ as the Hermitian matrices, the anti-Hermitian $\mathbb M_-$ as the anti-Hermitian matrices, and $\mathbb M_-=i\mathbb M_+$ | [$M_2(\mathbb{C})$ Model : The Six Subspaces as Matrix Conditions](../articles_maths/m2c-model-the-six-subspaces-as-matrix-conditions.html) |
| $\operatorname{Tr}\mathsf M_2(\tilde Q)=2Q_t$, $\det\mathsf M_2(\tilde Q)=N$, and the norm on each subspace | [$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm](../articles_maths/m2c-representation-trace-determinant-and-the-biquaternion-norm.html) |
| The regular image $\mathsf M_4^{L}(\tilde Q)$, its trace and determinant, and the block splitting | [$M_4(\mathbb{C})$ Model : The Product, the Trace and the Determinant](../articles_maths/m4c-model-the-product-the-trace-and-the-determinant.html) |
| The sandwich operator, its spectrum $\lambda_i\bar\lambda_j$, its determinant and trace | [Two-Sided Operator and the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](../articles_maths/the-sandwich-of-a-n-regular-spectrally-regular-biquaternion.html) |
| Hermitian conjugation ${}^{*}$ as the conjugate transpose, and the four involutions as four matrix operations | [$M_2(\mathbb{C})$ Representation : The Conjugations and the Adjoints](../articles_maths/m2c-representation-the-conjugations-and-the-adjoints.html) |
| The spin operators, the pure states, the density matrix, the Bloch vector and the measurement formulae | [$M_2(\mathbb{C})$ Representation : Spin, Qubits and the Bloch Vector](../articles_maths/m2c-representation-spin-qubits-and-the-bloch-vector.html) |
| The rank-one matrices, the two strata of the null cone and the trace-one idempotents | [$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety](../articles_maths/m2c-representation-rank-one-matrices-and-the-determinantal-variety.html) |
| The unit-norm slice as $SL_2(\mathbb{C})$, the $*$-unitary slice as $SU(2)$, and the polar decomposition | [$M_2(\mathbb{C})$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant](../articles_maths/m2c-representation-gl2-sl2-and-the-determinant.html) |
| The eigenvalue decomposition and the eigenprojections | [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html) |
| The bundle, the connection, the curvature and the holonomy | [Fibre Bundles, Connections and Curvature](../articles_maths/fibre-bundles-connections-and-curvature.html) |

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

so the fixed space of ${}^{*}$ is carried onto the fixed space of the dagger. That identity is the algebraic fact behind the word **observable**.

### The Factor $i$ Is the Complex Structure

The factor is forced. A $2\times2$ matrix with real entries and square $-\mathrm I_2$ defines a complex structure on $\mathbb R^2$; three of them, anticommuting, define the quaternionic structure. The algebra in which $\vec e_k^2=-e_t$ holds is the complexified one, and the coefficient field supplies the $i$ that turns $\sigma_k$ into $-i\sigma_k$. With the assignment $\vec e_k\mapsto\sigma_k$ the square would be $+\mathrm I_2$, which is the split-quaternion sign, not the quaternion one.

The sign is then forced. The alternative assignment $\vec e_k\mapsto-\mathsf M_2(\vec e_k)$ preserves the squares and fails the products: $\vec e_x\vec e_y=\vec e_z$ becomes $(-\mathsf M_2(\vec e_x))(-\mathsf M_2(\vec e_y))=\mathsf M_2(\vec e_z)$, which is minus the image of $\vec e_z$ under that assignment. Two lines of matrix multiplication fix the sign.

The interpretation is that the factor $i$ is not a bookkeeping convention. It is the statement that the three directions of the algebra are generators of rotations and not observables: $\vec e_k$ is anti-Hermitian and generates, $i\vec e_k$ is Hermitian and is measured. The two roles differ by the factor that the complexification supplies.

The boundary is that this explains why the factor is present in the model. It does not say that nature is complex, and it does not derive the complex numbers from anything physical.

## Two Images of One Element

### The Element Image and the Map Image

The algebra is isomorphic to $M_2(\mathbb{C})$, and the regular representation gives a second image:

$$
\mathsf M_2(\tilde Q)\in M_2(\mathbb{C}),
\qquad
\mathsf M_4^{L}(\tilde Q)\in M_4(\mathbb{C}).
$$

The first is the matrix of the element as it acts on the spinor module $S\cong\mathbb{C}^2$. The second is the matrix of the element as it acts on the algebra, taken as a module over itself, in the canonical frame of *Conventions in Mathematics*, §*The Matrix Models*.

The two are the same object seen through two kinds of data. $\mathsf M_2(\tilde Q)$ is the matrix of an element acting on the data an object acts on; $\mathsf M_4^{L}(\tilde Q)$ is the matrix of an element acting on the objects themselves. The regular module is $S\oplus S$, split by the two minimal left ideals, which are the two column chiralities. In that frame the regular image is block diagonal with two equal blocks, $\mathsf M_4^{L}(\tilde Q)=I_2\otimes\mathsf M_2(\tilde Q)$, and

$$
\mathsf M_4^{L}\;\cong\;\mathsf M_2\oplus\mathsf M_2 .
$$

The map-data image is the element-data image taken twice, one copy per chirality.

### The Bookkeeping of the Doubling

The doubling is visible in every invariant. The trace doubles, from $2Q_t$ to $4Q_t$; the determinant squares, from $N$ to $N^{2}$; and the sandwich, which is the product of the two regular images, has determinant $\lvert N\rvert^{4}$ and trace $4\lvert Q_t\rvert^{2}$. None of these factors is a physical quantity. They are the dimension of the module over which the trace is taken and the number of copies the regular module contains. The one invariant that does not move is the vanishing set: all three determinants vanish exactly on the zero-divisor cone.

The boundary is that the two pictures are one representation taken twice, not two theories. A result proved in one picture must be translated before it is read in the other, and the determinant degree is where the translation is most often skipped.

### The Sandwich

The sandwich is a third matrix,

$$
\operatorname{H}_{\tilde Q}=\mathsf M_4^{L}(\tilde Q)\mathsf M_4^{R}(\tilde Q^{*}),
$$

quadratic in the parameter and a congruence rather than a similarity. Its spectrum is $\lambda_i\bar\lambda_j$: the squares of the element's eigenvalues, with the two transverse directions fixed. The element stores half of the frame change; the congruence stores the whole of it.

## The Invariants

### The Trace Is the Weight

The trace of the element matrix is twice the scalar part,

$$
\operatorname{Tr}\mathsf M_2(\tilde Q)=2Q_t.
$$

On a state the trace is normalised to one, and the scalar part is then $\tfrac12$. The factor two is the dimension of the spinor module, not a physical factor: it appears because the identity is a $2\times2$ matrix.

The trace is additive and blind to the vector part. It cannot distinguish two states with the same scalar part, and it is not the norm. The invariant that sees the whole element is the determinant.

### The Determinant Is the Invariant

The determinant of the matrix is the quaternionic norm, $\det\mathsf M_2(\tilde Q)=N$, and it reads differently on the two sectors:

| sector | element | determinant | signature |
| --- | --- | --- | --- |
| material | $iq'_te_t+q_k\vec e_k$ | $-(q'_t)^2+q_x^2+q_y^2+q_z^2$ | $(3,1)$ |
| informational | $q_te_t+iq'_k\vec e_k$ | $q_t^2-(q'_x)^2-(q'_y)^2-(q'_z)^2$ | $(1,3)$ |
| state slice | $\tfrac12(e_t+i\vec r)$ | $\tfrac14(1-\lvert\vec r\rvert^2)$ | positivity |

The same algebraic function is the interval on the material sector, the causal type and the positivity test on the informational sector, and the mixedness on the trace-one slice. The zero set is one object in the three readings: the light cone, the boundary of the state space, and the set of pure states.

The boundary is that these are three restrictions of one function to three real slices, not three different quantities. A statement about the determinant must say which slice it is on.

### The Determinant Is a Volume

Multiplication by $M$ is a real linear map of $\mathbb C^2\cong\mathbb R^4$, and its real determinant is $\lvert\det M\rvert^2$. The complex determinant is the complex area scale of the parallelogram spanned by the two columns, and the real volume scale is its squared modulus. On the unit-norm slice $N=1$, that is $\det M=1$, the real determinant is $1$: the group is $SL_2(\mathbb C)$, and its action preserves the real volume.

The boundary is that the volume is the volume of the realification of the module, not a spacetime volume. On the material sector the same determinant is the interval, and an interval is not a volume. The two readings coincide in the zero set and nowhere else.

### The Eigenvalues Are the Spectrum

The element matrix satisfies

$$
\lambda^{2}-2Q_t\,\lambda+N=0,
\qquad
\lambda_\pm=Q_t\pm iB,
\qquad
B^2=Q_x^2+Q_y^2+Q_z^2 .
$$

The product is the determinant, the sum twice the trace. The pair is a similarity invariant and not a complete one: a scalar $Q_te_t$ and a non-scalar element with $B^2=0$ share the pair $\{Q_t,Q_t\}$ and are not similar. The eigenprojections, not the pair, carry the remaining information.

### The Spectrum Is the Doubled Rapidity

The boost rotor of rapidity $\eta$ along $\vec e_z$,

$$
\tilde B_\eta=\cosh\tfrac{\eta}{2}\,e_t+\sinh\tfrac{\eta}{2}\,i\vec e_z,
$$

has norm one and matrix $\operatorname{diag}(e^{\eta/2},e^{-\eta/2})$. The sandwich has eigenvalues $e^{\eta},1,1,e^{-\eta}$: the two middle eigenvalues are the transverse directions, which the boost fixes; the longitudinal pair is squared. The element stores half the rapidity, because it acts on the spinor; the congruence stores the full rapidity, because it acts on the four-vector.

The rotation rotor of angle $\theta$ about $\vec e_z$,

$$
\tilde R_\theta=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,\vec e_z,
$$

has matrix eigenvalues $e^{\pm i\theta/2}$ and sandwich eigenvalues $e^{\pm i\theta}$ beside two ones. At $\theta=2\pi$ the element eigenvalues are $-1$ and the operator eigenvalues are $1$: the spinor returns with a sign, the vector returns unchanged. The factor two is the double cover.

The boundary is that the reading requires a diagonalisable element matrix and a pure boost or rotation. On the cone one eigenvalue vanishes; on its trace-zero part the two collide at zero and the reading stops. For a general Lorentz element no single rapidity exists; the polar decomposition separates the boost from the rotation.

## Observables and States

### The Hermitian Elements Are the Observables

An element $\tilde H\in\mathbb M_+$ has a Hermitian matrix, and a Hermitian matrix has real eigenvalues and an orthogonal eigenbasis. The spectral theorem for the matrix is therefore the spectral statement for the element, and the eigenvalues are the possible outcomes of a measurement of $\tilde H$.

The identification is exact: $\mathbb M_+$ is carried onto the Hermitian matrices, and the expectation is the trace of the product,

$$
\operatorname{Tr}\bigl(\mathsf M_2(\tilde\varrho)\mathsf M_2(\tilde H)\bigr)=2\langle\tilde\varrho,\tilde H\rangle_{*}=h_t+\vec r\cdot\vec h ,
$$

for the state $\tilde\varrho=\tfrac12(e_t+i\vec r)$ of trace one.

The boundary is that the word *observable* uses the involution ${}^{*}$, which belongs to the real structure of $\mathbb B$. The complex isomorphism alone does not single out $\mathbb M_+$: it carries $\mathbb M_+$ and $\mathbb M_-$ to two complementary subspaces of the same complex algebra, and the choice between them is physical.

### The Three Directions Are the Three Spin Axes

A traceless Hermitian element is $\tilde H=i\vec h$ with $\vec h\in\mathbb R^3$, and its matrix is $\vec h\cdot\vec\sigma$. The three coefficients are the components of a spatial vector, and the three Pauli matrices are the three components of the measurement. For the spin operators $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$ the matrix is $\tfrac{\hbar}{2}\sigma_k$, and the commutator

$$
[\tilde S_i,\tilde S_j]=i\hbar\,\epsilon_{ijk}\tilde S_k
$$

is the angular-momentum algebra. The three directions close under the commutator into $\mathfrak{su}(2)$, and the exponentials are the rotations of the state space.

The boundary is that the naming of the three directions is a choice of basis, and the algebra has no preferred axis. A rotation permutes the operators and conjugates the matrices; the physics is invariant, the labels are not.

### The State Is the Positive Trace-One Matrix

A state is a Hermitian element of trace one whose matrix is positive semidefinite:

$$
\tilde\varrho=\tfrac12(e_t+i\vec r),
\qquad
\rho=\mathsf M_2(\tilde\varrho)=\tfrac12\bigl(\mathrm I_2+\vec r\cdot\vec\sigma\bigr),
\qquad
\lvert\vec r\rvert\le1 .
$$

The trace-one condition is the normalisation, the positivity is $\lvert\vec r\rvert\le1$, and the purity is the boundary $\lvert\vec r\rvert=1$. The state space is the Bloch ball, the pure states are its boundary and the maximally mixed state is its centre.

The determinant of the state matrix is

$$
\det\mathsf M_2(\tilde\varrho)=\tfrac14\bigl(1-\lvert\vec r\rvert^{2}\bigr),
$$

the product of the two eigenvalues $\tfrac12(1\pm\lvert\vec r\rvert)$. On the ball it is the radial gap to the pure boundary: it vanishes on the sphere and is maximal at the centre.

### Purity, Entropy and the Zero Divisor

Three quantities read off the same determinant:

$$
\operatorname{Tr}(\tilde\varrho^{2})=1-2\det\mathsf M_2(\tilde\varrho),
\qquad
S_L=1-\operatorname{Tr}(\tilde\varrho^{2})=2\det\mathsf M_2(\tilde\varrho).
$$

The first is the purity; the second is the linear entropy. At the centre the determinant is $\tfrac14$, the purity $\tfrac12$ and the linear entropy $\tfrac12$. On the sphere the determinant vanishes, the purity is one and the entropy is zero.

| position | $\det$ | purity | linear entropy | state |
| --- | --- | --- | --- | --- |
| centre | $\tfrac14$ | $\tfrac12$ | $\tfrac12$ | maximally mixed |
| interior | $\tfrac14(1-r^{2})$ | $\tfrac12(1+r^{2})$ | $\tfrac12(1-r^{2})$ | mixed |
| boundary | $0$ | $1$ | $0$ | pure |

The vanishing of the determinant is the vanishing of the norm, hence the invertibility criterion. Inside the ball the state is a unit; on the sphere it is a zero divisor, of rank one, and its matrix is the rank-one projector onto a ray. The pure states are exactly the states on the wall of the algebra.

### The Singular Values of the Amplitude

For a general element the matrix has a polar decomposition and two singular values. The amplitude is

$$
\mathsf M_2(\tilde Q_H)=\sqrt{\mathsf M_2(\tilde Q)\mathsf M_2(\tilde Q)^{\dagger}},
$$

so $\tilde Q_H$ is Hermitian positive semidefinite and its eigenvalues $\sigma_1\ge\sigma_2\ge0$ are the singular values of $\tilde Q$. On the amplitude,

$$
\langle\tilde Q_H\rangle_{\natural}=\det\mathsf M_2(\tilde Q_H)=\sigma_1\sigma_2=\lvert N(\tilde Q)\rvert .
$$

The norm of an amplitude is real and non-negative. The state inherits the singular values and loses the phase: with $\tilde Q_{\mathrm n}=\tilde Q_H/\sqrt{\sigma_1^{2}+\sigma_2^{2}}$, the state is $\tilde Q_{\mathrm n}^{2}$, its eigenvalues are $p_i=\sigma_i^{2}/(\sigma_1^{2}+\sigma_2^{2})$, and its determinant is

$$
\det\mathsf M_2(\tilde\varrho_Q)=\frac{\sigma_1^{2}\sigma_2^{2}}{(\sigma_1^{2}+\sigma_2^{2})^{2}}\in\left[0,\tfrac14\right].
$$

The mixedness is the spread of the singular values. The boundary is that the singular values are not the moduli of the eigenvalues for a non-normal element; only for a normal element do the two coincide.

## The Phase Fibre

### The Central Phase

The central element $e^{i\alpha}e_t$ maps to the scalar matrix $e^{i\alpha}\mathrm I_2$. It multiplies the element matrix by a phase, multiplies the determinant by $e^{2i\alpha}$, multiplies a state by $e^{i\alpha}$ and therefore does not preserve the trace-one slice, and acts trivially in the sandwich. A pure state is a ray, not a vector: the spinor $\xi$ and $e^{i\alpha}\xi$ give the same $\rho$, and the circle of phases over each pure state is the fibre of the Hopf bundle.

### The Hopf Map

The spinor module is $S\cong\mathbb{C}^2$. Its unit vectors form $S^3$, and the map

$$
\pi(\varsigma)=\varsigma\varsigma^{\dagger}
$$

sends a unit spinor to a rank-one Hermitian matrix of trace one, which is a pure state. In the algebra it is the idempotent $\tfrac12(e_t+i\vec u)$ with $\vec u$ the Bloch vector of $\varsigma$. The map is surjective onto $S^2$, and its fibre is the phase circle. The bundle

$$
U(1)\hookrightarrow S^{3}\longrightarrow S^{2}
$$

is the Hopf bundle, of first Chern number one. The state carries the axis and no phase; the phase is the fibre.

### The Two Circles

The corpus's Hopf article writes the same geometry on the unit real quaternions, where the map is $\tilde U\mapsto\tilde U\vec e_z\bar{\tilde U}$ and the fibre is the stabiliser of the axis, the circle of rotations about $\vec e_z$. That circle and the central phase circle are different subgroups of $U(2)$: the stabiliser is the diagonal torus, the central phase is the scalar circle, and they meet only in $\{\pm\mathrm I_2\}$.

The two descriptions are two presentations of the Hopf bundle, and they must not be identified fibre by fibre. In the spinor-ray description the fibre is the overall phase; in the quaternion-conjugation description the fibre is the stabiliser. Both statements are correct, and neither is the other.

### The Holonomy

The natural connection on the Hopf bundle has curvature $-\tfrac12$ times the area form of the sphere. Its holonomy over a loop is

$$
\gamma=-\tfrac12\,\Omega,
$$

minus one half of the enclosed solid angle. This is the Pancharatnam phase, and the Berry phase of a spin in a slowly varying field is the same holonomy. The factor $\tfrac12$ is the double cover again.

The boundary is that the bundle, its Chern number and its holonomy are owned by *The Hopf Fibration and the Biquaternion Gauge Bundle* and *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*. The unit spinor is not a unit-norm biquaternion: the unit spinors form $S^3$, the unit-norm biquaternions form $SL_2(\mathbb{C})$, and the unit real quaternions, read as spinors, are the common three-sphere.

## The Double Cover

The unit-norm elements are $SL_2(\mathbb{C})$, and they cover the proper orthochronous Lorentz group two-to-one with kernel $\{\pm\mathrm I_2\}$. A rotation through $2\pi$ gives $-\mathrm I_2$ and a rotation through $4\pi$ gives $\mathrm I_2$. The sign is the sign of the spinor, and it is the discrete difference between the spinor picture and the four-vector picture.

The boundary is that the double cover is a statement about the group, not about a particular state. It says that the two matrices $\pm M$ define the same transformation of the material sector; it does not say that the two signs are physically distinguishable for every state.

## What the Three Readings Share

A $2\times2$ matrix has two scalar invariants, its determinant and its trace, and the readings divide them.

| matrix | determinant | eigenvalue pair | reading |
| --- | --- | --- | --- |
| $\mathsf M_2(\tilde\varrho)$ | $\tfrac14(1-r^{2})$ | $\tfrac12(1\pm r)$ | mixedness; the purity is affine in the determinant |
| $\mathsf M_2(\tilde B_\eta)$ | $1$ | $e^{\pm\eta/2}$ | half the rapidity |
| $\mathsf M_2(\tilde R_\theta)$ | $1$ | $e^{\pm i\theta/2}$ | half the angle |
| $\varsigma\varsigma^{\dagger}$ | $0$ | $1,0$ | a pure state; the fibre is the phase |

The determinant is a **scale**, the eigenvalue ratio a **shape**, and the phase the one datum the map to the ray forgets. The three are independent. A state matrix has a determinant and a real eigenvalue ratio; the ratio is a population ratio and not a rapidity, because the state is Hermitian and is not a Lorentz frame element. A boost matrix has a rapidity and determinant one, because it is a unit. A unit spinor has a phase and a pure-state image of determinant zero, because the map to the ray is rank one.

Read together, the three readings say what a matrix image can carry: a norm, a frame and a volume. It cannot carry the phase of the element, which the sandwich loses and the state ray forgets, and it cannot carry a dynamics.

## Physical Interpretations

- **The three Hermitian units are the three Pauli matrices.** The correspondence is the identity $\mathsf M_2(i\vec e_k)=\sigma_k$; the factor $i$ is the complex structure that turns generators into observables.
- **The Hermitian elements are the observables.** $\mathbb M_+$ is carried onto the Hermitian matrices; the spectral theorem gives the outcomes, and the trace gives the expectation.
- **The three directions are the spin axes.** The traceless Hermitian elements close under the commutator into $\mathfrak{su}(2)$; the exponentials are the rotations of the state space.
- **The trace is the weight.** $\operatorname{Tr}=2Q_t$; the factor two is the dimension of the spinor module.
- **The determinant is the norm.** The same function is the interval on the material slice, the causal type and positivity on the informational slice, and the mixedness on the state slice.
- **The eigenvalues are the spectrum.** $\lambda_\pm=Q_t\pm iB$; their product is the determinant and their sum twice the trace.
- **The spectrum is the doubled rapidity.** The element matrix stores half the rapidity or half the angle; the sandwich stores the full one. The double cover is the factor two.
- **The state is the positive trace-one matrix.** The Bloch ball is the state space; the determinant is the mixedness; purity is the zero divisor.
- **The phase is the fibre.** The Hopf bundle $U(1)\hookrightarrow S^3\to S^2$; the central phase is the fibre, and the holonomy is minus half the solid angle.
- **The two images are one representation taken twice.** The map-data image is the element-data image taken twice, one copy per chirality; the trace doubles and the determinant squares.

## Limits

The article reads invariants. It derives no equation of motion, no Lorentz action and no measurement update.

The mixedness reading requires a trace-one positive element. For a general element the determinant is the complex norm, and it is not a mixedness.

The rapidity reading requires a diagonalisable element matrix and a pure boost or rotation. On the cone the reading stops; for a general Lorentz element no single rapidity exists.

The phase-fibre reading is the Hopf bundle, not a gauge field. The connection, its curvature and its Chern number are cited; no gauge dynamics and no charge quantisation are derived.

The element-data and map-data distinction is an interpretation of the doubling $\mathsf M_4\cong\mathsf M_2\oplus\mathsf M_2$, not an identification of two theories.

The correspondence does not say that nature is complex, and it does not derive the complex numbers. The complex field is the coefficient field of the algebra, fixed before any interpretation begins.

## Summary

- The $2\times2$ image is the Pauli correspondence: $e_t\mapsto\mathrm I_2$ and $\vec e_k\mapsto-i\sigma_k$, so $i\vec e_k\mapsto\sigma_k$.
- The factor $i$ is the complex structure that separates the generators from the observables; it is forced by the squares and the products.
- The element matrix has trace $2Q_t$ and determinant $N$; the regular image has trace $4Q_t$ and determinant $N^{2}$; the sandwich has trace $4\lvert Q_t\rvert^{2}$ and determinant $\lvert N\rvert^{4}$. Only the vanishing set is common.
- The eigenvalues are $\lambda_\pm=Q_t\pm iB$; their product is the determinant and their sum twice the trace.
- The element matrix stores half the rapidity or half the angle; the sandwich stores the full one. The double cover is the factor two.
- The Hermitian elements are the observables; the traceless ones are the spin axes; the commutator is $\mathfrak{su}(2)$.
- The state is the positive trace-one matrix; the determinant is $\tfrac14(1-r^{2})$, the mixedness; purity is the zero divisor; the purity and the linear entropy are affine in the determinant.
- The phase is the fibre of the Hopf bundle $U(1)\hookrightarrow S^3\to S^2$; the holonomy is minus half the solid angle.
- The determinant is a scale, the eigenvalue ratio a shape, and the phase what the ray forgets. No invariant of a single matrix supplies a dynamics.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathsf M_2(\tilde Q)$ | the element image; $\det=N$, $\operatorname{Tr}=2Q_t$ |
| $\mathsf M_4^{L}(\tilde Q)$ | the left regular image; $\det=N^{2}$, $\operatorname{Tr}=4Q_t$ |
| $\operatorname{H}_{\tilde Q}$ | the sandwich; $\det=\lvert N\rvert^{4}$, $\operatorname{Tr}=4\lvert Q_t\rvert^{2}$ |
| $\tilde\varrho=\tfrac12(e_t+i\vec r)$ | a trace-one state of the Bloch ball |
| $\det\mathsf M_2(\tilde\varrho)=\tfrac14(1-r^{2})$ | the mixedness |
| $S_L=2\det\mathsf M_2(\tilde\varrho)$ | the linear entropy |
| $\tilde B_\eta$ | the boost rotor of rapidity $\eta$ |
| $\tilde R_\theta$ | the rotation rotor of angle $\theta$ |
| $\varsigma$ | a unit spinor of $S\cong\mathbb C^2$ |
| $\pi(\varsigma)=\varsigma\varsigma^{\dagger}$ | the Hopf map to the Bloch sphere |
| $\gamma=-\tfrac12\Omega$ | the Pancharatnam phase |

## Further Reading

- [Element and Operator Representations: The Three Actions](the-element-and-operator-representations.html), for the correspondence table this article extends.
- [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html), for the spectrum and the eigenprojections.
- [The Bloch Ball as the Normalised Slice of the Future Light Cone](the-bloch-ball-as-the-trace-one-slice-of-the-future-light-cone.html), for the ball and its boundary.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the state conditions and the Born pairing.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the cone as the boundary of the state space.
- [The Hopf Fibration and the Biquaternion Gauge Bundle](the-hopf-fibration-and-the-biquaternion-gauge-bundle.html), for the bundle, its fibre and its Chern number.
- [Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form](pancharatnams-phase-and-the-polarization-sphere-in-biquaternionic-form.html), for the half-solid-angle rule.
