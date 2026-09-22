
# __The Matrix Representation in the Biquaternion Universe__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is isomorphic, as a complex algebra, to the algebra of $2 \times 2$ complex matrices,

$$
\mathbb{B} \cong M_2(\mathbb{C}).
$$

This is the statement that a biquaternion and a $2 \times 2$ complex matrix are the same object written twice, and it is the most computationally useful form the algebra takes. In the four-vector and polar forms of the companion articles, the algebra is described by its components and by its norm; in the matrix form it is described by entries, and every statement about it becomes an arithmetic check. The trace reads off the scalar part, the determinant **is** the norm form, invertibility becomes non-vanishing determinant, the Hermitian subspace becomes the Hermitian matrices, and the minimal left ideals become the matrix columns. None of this is new mathematics, but it is the reason the physics articles of this corpus can compute with biquaternions at all.

**The convention of this article, and of the corpus.** The matrix representation is the one fixed by *Biquaternion Algebraic Representations* in the mathematics pages, and the isomorphism that carries a biquaternion into its matrix is written $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ throughout. This article states the assignment, checks that the four basis matrices multiply as the four units do, notes why the signs cannot be chosen differently, and reads off the consequences: the invariants, the four subspaces, the two ideals as columns, the conjugations, and the spin and qubit structures. The convention is not free. It is used identically by the spin, qubit, Bell-state, Dirac and Fock-space articles, and the two conventions that a reader is likely to meet elsewhere do not agree with it.

## The Representation

The isomorphism is written $\Phi$. It converts a biquaternion into a $2 \times 2$ complex matrix,

$$
\Phi : \mathbb{B} \longrightarrow M_2(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity. The scalar imaginary $i$ is the complex unit of the coefficients and is central, so it maps to a scalar matrix; the quaternion units are assigned the matrices

$$
\Phi(e_0) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2, \qquad
\Phi(e_1) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}, \qquad
\Phi(e_2) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad
\Phi(e_3) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix},
$$

with $\Phi(i) = iI_2$ on the central scalar $\mathbb{C}_{\mathbb{B}}$. This is the assignment of the mathematics article *Biquaternion Algebraic Representations*, taken over unchanged. A general biquaternion $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$ therefore maps to

$$
\Phi(\tilde{Q}) = Q_0 I_2 + Q_1 \Phi(e_1) + Q_2 \Phi(e_2) + Q_3 \Phi(e_3)
= \begin{pmatrix} Q_0 - i Q_3 & -i Q_1 - Q_2 \\ -i Q_1 + Q_2 & Q_0 + i Q_3 \end{pmatrix}.
$$

**The check.** The assignment is the right one because the four matrices multiply as the four units do. Squaring a vector image,

$$
\Phi(e_1)^2 = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}^2 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I_2,
$$

and the same holds for $\Phi(e_2)$ and $\Phi(e_3)$; so $e_k^2 = -e_0$ is reproduced. Multiplying the first two,

$$
\Phi(e_1)\Phi(e_2) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
= \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} = \Phi(e_3),
$$

and the other products give $\Phi(e_2)\Phi(e_3) = \Phi(e_1)$ and $\Phi(e_3)\Phi(e_1) = \Phi(e_2)$, reproducing $e_1e_2 = e_3$ with its cyclic companions; reversing the order of the factors reverses the sign of each product, reproducing $e_ie_j = -e_je_i$ for $i \neq j$. Those relations are the whole multiplication table of the units, so the correspondence of bases is an isomorphism of algebras and not a formal analogy.

The map is also invertible, which is worth recording explicitly since it is what makes the representation a change of coordinates rather than a forgetful operation. Reading the coefficients back off an arbitrary matrix,

$$
Q_0 = \tfrac12(a + d), \qquad Q_1 = \tfrac{i}{2}(b + c), \qquad Q_2 = \tfrac12(c - b), \qquad Q_3 = \tfrac{i}{2}(a - d),
\qquad
\Phi^{-1}\!:\ \begin{pmatrix} a & b \\ c & d \end{pmatrix} \longmapsto Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3 ,
$$

so every $2 \times 2$ complex matrix is the image of exactly one biquaternion. Together with multiplicativity this makes $\Phi$ an algebra isomorphism, and a biquaternion identity holds exactly when the corresponding matrix identity does.

**Remark (the Pauli matrices).** The three matrices

$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
\sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad
\sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

are the Pauli matrices, and they are the basis images multiplied by the factor $i$. The relation may be read in either direction:

$$
\sigma_k = i\,\Phi(e_k) = \Phi(ie_k),
\qquad\text{equivalently}\qquad
\Phi(e_k) = -i\,\sigma_k .
$$

The factor $i$ is thus all that separates the algebra's own matrices from the ones a physicist writes down, and the form $\sigma_k = \Phi(ie_k)$ states the same relation through the algebra: it is the **Hermitian** quaternion units $ie_k$ whose images are the Hermitian Pauli matrices.

## Why the Signs Are Forced

Two features of the asserted assignment are not free: the factor $i$, and its sign. Both are settled by the check above, and that is what makes the assignment a statement about the algebra rather than a choice of convention.

**The factor $i$ is required by $e_k^2 = -e_0$.** The three matrices

$$
\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad
\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

square to $+I_2$. Assigning them to $e_1, e_2, e_3$ would therefore give $e_k^2 = +e_0$, the wrong sign. Multiplying by the complex unit repairs this, and both $+i$ and $-i$ times these matrices satisfy $e_k^2 = -e_0$.

**The sign is then forced by the cross-relations.** These three matrices are the $\sigma_k$ of the remark above. The alternative assignment sends $e_k$ to $+i\sigma_k = -\Phi(e_k)$, reversing the sign of every vector image. The image of the product is then

$$
(+i\sigma_1)(+i\sigma_2) = i^2\sigma_1\sigma_2 = -\sigma_1\sigma_2 = -i\sigma_3 ,
$$

while the image of $e_3$ is $+i\sigma_3$. The product of the images is thus minus the image of the required value, so the plus assignment fails at the first cross-relation. Under the minus assignment, which is the one asserted above,

$$
(-i\sigma_1)(-i\sigma_2) = (-i)^2\sigma_1\sigma_2 = -\sigma_1\sigma_2 = -i\sigma_3 = \Phi(e_3) ,
$$

which is exactly the image of $e_3$. So the assignment asserted above passes the check, and the alternative fails not in one relation but in all of the cross-relations. Both statements were verified on the explicit matrices.

The physical reading of the sign is the one recorded in the remark: the assignment is the one whose images of the **Hermitian** quaternion units are Hermitian, $\sigma_k = \Phi(ie_k)$. The imaginary quaternion units themselves are not Hermitian, $\Phi(e_k)^\dagger = i\sigma_k = -\Phi(e_k)$, while $ie_k$ is. This is what makes the algebra an algebra of observables, and it is why the sign is a consequence of the algebra rather than a convention that could have gone either way.

## Trace, Determinant and the Norm Form

**The trace is twice the scalar part.** From the general matrix,

$$
\mathrm{Tr}(\tilde{Q}) = (Q_0 - i Q_3) + (Q_0 + i Q_3) = 2 Q_0 .
$$

So the scalar part of a biquaternion is a matrix trace, and the traceless matrices are the vector parts. This is why the center of the algebra is the scalar matrices: an element commutes with everything exactly when its matrix is a multiple of the identity.

**The determinant is the norm form.** Expanding,

$$
\det(\tilde{Q}) = (Q_0 - iQ_3)(Q_0 + iQ_3) - (-iQ_1 - Q_2)(-iQ_1 + Q_2)
= (Q_0^2 + Q_3^2) - \big[(-iQ_1)^2 - Q_2^2\big] = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = N(\tilde{Q}).
$$

This is the central fact of the representation. The norm form, defined algebraically as $\tilde{Q}\bar{\tilde{Q}}$, is the determinant of the corresponding matrix — not merely similar to it, but equal to it. Three consequences follow at once.

**Invertibility.** A biquaternion is invertible exactly when its norm form is nonzero, because a matrix is invertible exactly when its determinant is. The algebraic inverse $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$ is the matrix inverse, since for a $2\times 2$ matrix the adjugate is $\det(M)\,M^{-1}$.

**Multiplicativity.** $N(\tilde{Q}\tilde{R}) = N(\tilde{Q})N(\tilde{R})$ holds because the determinant is multiplicative. The algebraic proof of this identity is a computation in eight real components; in the matrix form it is one line, and this is the clearest illustration of what the representation buys.

**Zero divisors.** The zero divisors of $\mathbb{B}$ are the singular matrices. The null cone $N(\tilde{Q}) = 0$ is the determinant-zero locus. Since $\mathbb{B}$ is not a division algebra, this locus is nonempty, and its elements are exactly the matrices of rank at most one.

## The Four Subspaces

Each of the four fixed-point subspaces of the algebra has a one-line description in matrix language, and each description is a statement a physicist recognizes.

| Subspace | Matrix characterisation | Reading |
|---|---|---|
| Center $\mathbb{C}_{\mathbb{B}}$ | the scalar matrices $Q_0 I_2$ | the complex numbers |
| Real quaternions $\mathbb{H}_{\mathbb{B}}$ | $\begin{pmatrix} z & w \\ -\bar{w} & \bar{z}\end{pmatrix}$, $z, w \in \mathbb{C}$ | a subalgebra, isomorphic to $\mathbb{H}$ |
| Hermitian $\mathbb{M}_+$ | the Hermitian matrices $M = M^\dagger$ | observables |
| Anti-Hermitian $\mathbb{M}_-$ | the anti-Hermitian matrices $M = -M^\dagger$ | the material sector |

The identification of $\mathbb{M}_+$ with the observables is immediate from $ie_k \mapsto \sigma_k$: an element $\tilde{H} = h_0e_0 + ih_1e_1 + ih_2e_2 + ih_3e_3$ with real $h_\mu$ maps to

$$
\tilde{H} \;\mapsto\; h_0 I_2 + h_1\sigma_1 + h_2\sigma_2 + h_3\sigma_3 ,
$$

which is the general Hermitian $2\times 2$ matrix, i.e. the general observable of a two-state system. The anti-Hermitian subspace is $i$ times the Hermitian one, so the material sector is the observables multiplied by $i$ — the statement that the material sector is the Hermitian sector rotated by the complex structure, in matrix form.

The quaternion subspace deserves its own line, because it is the one that is **not** the whole algebra: the real quaternions are the matrices of the form $\begin{pmatrix} z & w \\ -\bar{w} & \bar{z}\end{pmatrix}$. This is a four-**real**-dimensional subalgebra, not the four-dimensional complex space of all matrices with $z, w \in \mathbb{C}$, and it is the matrix reason that $\mathbb{H}$ is a division algebra while $\mathbb{B}$ is not: the determinant of that form is $|z|^2 + |w|^2$, which vanishes only when $z = w = 0$.

## The Ideals as Columns and the Spinor Module

The matrix form makes the algebra's ideal structure a statement about columns. The idempotents

$$
P_+ = \tfrac12(e_0 + ie_3) \;\longmapsto\; \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = E_{11}, \qquad
P_- = \tfrac12(e_0 - ie_3) \;\longmapsto\; \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = E_{22}
$$

generate the two **columns** of the matrix algebra,

$$
\mathbb{B}P_+ = \mathbb{C}E_{11} \oplus \mathbb{C}E_{21} = \left\{ \begin{pmatrix} a & 0 \\ c & 0 \end{pmatrix} : a, c \in \mathbb{C} \right\}, \qquad
\mathbb{B}P_- = \mathbb{C}E_{12} \oplus \mathbb{C}E_{22} = \left\{ \begin{pmatrix} 0 & b \\ 0 & d \end{pmatrix} : b, d \in \mathbb{C} \right\},
$$

with $\mathbb{B} = \mathbb{B}P_+ \oplus \mathbb{B}P_-$. Each column is two-dimensional over $\mathbb{C}$ and minimal, and left multiplication acts on it irreducibly: the column **is** the spinor module $S = \mathbb{C}^2$ of the companion articles on the spinor module and on representation theory, not merely a space isomorphic to it.

Two structural facts are visible in this form, and both are used by the physics articles.

**The two columns are the two chiralities.** Left multiplication preserves each column: for any $M$, the products $ME_{11}$ and $ME_{21}$ again have vanishing second column, so $M(\mathbb{B}P_+) \subseteq \mathbb{B}P_+$. No left multiplication can therefore relate the two columns. A mass term that couples the left- and right-handed components cannot be a left multiplication; it must be a **right** multiplication, and the matrix unit that performs it is

$$
x = \tfrac12(ie_1 - e_2) \;\longmapsto\; \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = E_{12},
$$

whose right action maps the first column onto the second — $E_{11} \mapsto E_{12}$ and $E_{21} \mapsto E_{22}$ — while annihilating the second. This is the matrix form of the structural reason the biquaternionic Dirac equation couples the chiralities by a right multiplication, and of the statement that the spinor module, not the whole algebra, is the carrier of the Dirac field.

**The two-sided ideals are not among them.** Since $\mathbb{B} \cong M_2(\mathbb{C})$ is simple, its only two-sided ideals are $0$ and $\mathbb{B}$; the columns are one-sided. That is what allows the algebra to be simple and still carry two distinct chiralities, and it is why the mass term must be off-diagonal rather than a multiplication confined to a single column.

The pair $P_\pm$ used here is not the only one: every unit vector $\hat{\boldsymbol\mu}$ gives idempotents $\tfrac12(e_0 \pm i\hat{\boldsymbol\mu})$, and the choice $e_3$ is the one for which the two columns are the coordinate columns. The idempotent $\tfrac12(e_0 + ie_1)$ of the section *Spin, Qubits and the Bloch Vector* is a member of that family, corresponding to a different direction.

## The Conjugations in Matrix Form

The four involutions of the algebra become four matrix operations. Writing $M = M(\tilde{Q})$:

| Involution | Definition | Matrix image |
|---|---|---|
| Quaternion conjugation | $\bar{\tilde{Q}} = Q_0e_0 - Q_1e_1 - Q_2e_2 - Q_3e_3$ | the **adjugate** $\mathrm{adj}\,M = \epsilon M^{\mathsf T}\epsilon^{-1}$ |
| Complex conjugation | $Q_\mu \mapsto Q_\mu^{*}$ | $\epsilon\,\overline{M}\,\epsilon^{-1}$ |
| Hermitian conjugation | $\tilde{Q}^\dagger = \bar{\tilde{Q}}^{\,*}$ | the **conjugate transpose** $M^\dagger$ |
| Anti-Hermitian conjugation | $\tilde{Q}^\flat = -\tilde{Q}^\dagger$ | $-\,M^\dagger$ |

Two of the four are dressed by the antisymmetric form

$$
\epsilon = i\sigma_2 = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = \Phi(-e_2),
$$

the invariant antisymmetric form $\varepsilon$ of the spinor module: quaternion conjugation is the transpose dressed by $\epsilon$, and complex conjugation is the entrywise conjugation dressed by $\epsilon$. The adjugate statement is worth writing out, since it is the least familiar:

$$
\bar{\tilde{Q}} \;\mapsto\; \begin{pmatrix} Q_0 + i Q_3 & i Q_1 + Q_2 \\ i Q_1 - Q_2 & Q_0 - i Q_3 \end{pmatrix}
= \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
\quad\text{for}\quad M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}.
$$

Quaternion conjugation is therefore the classical adjoint, and the identity $\tilde{Q}\bar{\tilde{Q}} = N(\tilde{Q})e_0$ is the matrix identity $M\,\mathrm{adj}(M) = \det(M)I_2$. The other two are the operations a physicist expects: $\dagger$ is the conjugate transpose, so its fixed points are the Hermitian matrices, and $\flat = -\dagger$ has the anti-Hermitian matrices as its fixed points. The real structure $\flat$, which the corpus uses for the $\mathbb{M}_\pm$ split and for Majorana-type pairings, is the negative conjugate transpose.

**Complex conjugation is the one that does not act entrywise.** It is sometimes said that $\tilde{Q}^*$ conjugates the entries of the matrix. That is not true, and the reason is structural: the representation is built with the same $i$ that conjugates the coefficients, so the two operations compete. Conjugating the entries of $M(\tilde{Q})$ sends $-i\sigma_1 \mapsto +i\sigma_1$ and $-i\sigma_3 \mapsto +i\sigma_3$ — the images of $e_1$ and $e_3$ to their negatives — while the image of $e_2$ is left alone; the entrywise operation is therefore not $M(\tilde{Q}^*)$, and it is not the image of any involution of the algebra. The correct correspondence is the one in the table,

$$
\Phi(\tilde{Q}^*) = \epsilon\,\overline{\Phi(\tilde{Q})}\,\epsilon^{-1}, \qquad \epsilon = i\sigma_2 = \Phi(-e_2),
$$

verified on explicit matrices, and the adjugate form of quaternion conjugation is the same dressing applied to the transpose. In this representation the safe rule is: use $\bar{\phantom{Q}}$, ${}^*$, $\dagger$ and $\flat$ through the four formulas above, and never conjugate the matrix entries on their own.

## Spin, Qubits and the Bloch Vector

The matrix representation is what connects the algebra to the physics of two-state systems, and the connection runs through the single identity $ie_k \mapsto \sigma_k$.

**Spin operators.** The spin operators of the biquaternion framework are $\tilde{S}_k = \tfrac{\hbar}{2}ie_k$, and under the isomorphism,

$$
\tilde{S}_k = \tfrac{\hbar}{2}ie_k \;\longmapsto\; \tfrac{\hbar}{2}\sigma_k ,
$$

which are the Pauli spin matrices. The eigenvalue statement $\tilde{S}_k^2 = \tfrac{\hbar^2}{4}e_0$, the anticommutation $\{\tilde{S}_i, \tilde{S}_j\} = \tfrac{\hbar^2}{2}\delta_{ij}e_0$ and the commutator $[\tilde{S}_i,\tilde{S}_j] = i\hbar\varepsilon_{ijk}\tilde{S}_k$ are, matrix by matrix, the standard angular-momentum algebra of a spin-$\tfrac12$ system. In the matrix form they are checked by multiplying $2\times 2$ matrices.

**States as projectors.** The rank-one idempotents of $\mathbb{M}_+$ are the pure-state projectors. The element

$$
p = \tfrac{1}{2}(e_0 + ie_1) \;\longmapsto\; \tfrac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}
= \tfrac{1}{2}(I_2 + \sigma_1)
$$

satisfies $p^2 = p$, has trace $1$ and determinant $0$: it is a rank-one projector, hence a pure state. Its complement $p_- = \tfrac12(e_0 - ie_1)$ is the orthogonal projector, and $p + p_- = e_0$ is $I_2$. Both $p$ and $p_-$ have vanishing norm form, which is the matrix way of saying that the rank-one idempotents of $\mathbb{M}_+$ live on the null cone: a pure state is a null element of the algebra. Note that not every idempotent of $\mathbb{M}_+$ is a state: the unit $e_0$ is idempotent, and its matrix $I_2$ has trace $2$ and determinant $1$, so it is the full-rank projector and does not lie on the null cone. This is the representation-theoretic content of *The Biquaternion Vacuum as a Minimal Idempotent*.

**The density matrix.** A general mixed state is

$$
\rho = \tfrac{1}{2}\big(I_2 + r_1\sigma_1 + r_2\sigma_2 + r_3\sigma_3\big),
$$

with Bloch vector $\mathbf{r} \in \mathbb{R}^3$. It is Hermitian with unit trace, so it lies in the image of $\mathbb{M}_+$, and the Bloch components are recovered by the trace pairing,

$$
r_k = \mathrm{Tr}(\rho\,\sigma_k),
$$

verified for all three components. The purity condition $\mathrm{Tr}(\rho^2) = 1$ is $|\mathbf{r}| = 1$, and the boundary of the Bloch ball is the set of rank-one projectors, i.e. the pure states found above. So the three-level description — biquaternion state, density matrix, Bloch vector — is one statement in three coordinate systems, and the passage between them is matrix multiplication and the trace.

## The Groups

The multiplicative group of the algebra has a matrix image with a standard name. An element of unit norm form, $N(\tilde{Q}) = e_0$, has

$$
\det M(\tilde{Q}) = 1,
$$

so the unit-norm biquaternions map into the special linear group,

$$
\{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) = e_0\} \;\cong\; \mathrm{SL}(2,\mathbb{C}).
$$

This is the matrix form of the statement that the unit-norm elements act on $\mathbb{M}_-$ by rotor conjugation and generate the Lorentz group. Concretely, the rotation rotors are the unit-norm quaternions, which map to the $SU(2)$ matrices

$$
\tilde{R}(\theta, \hat{\mathbf{n}}) = \exp\!\big(\tfrac{1}{2}\theta \hat{\mathbf{n}}\cdot e\big) \;\longmapsto\; \exp\!\big(-\tfrac{i}{2}\theta\,\hat{\mathbf{n}}\cdot\boldsymbol{\sigma}\big),
$$

and the boost rotors are the Hermitian unit-norm elements, which map to the Hermitian $\mathrm{SL}(2,\mathbb{C})$ matrices. The two cases are distinguished in the matrix form by Hermiticity, exactly as they are distinguished in the algebra by the split $\mathbb{M}_+ \oplus \mathbb{M}_-$.

The advantage of the matrix form here is not computational but structural: the classification of the unit-norm elements into rotations and boosts is the classification of the $\mathrm{SL}(2,\mathbb{C})$ matrices into unitary and Hermitian ones, and the double cover $SU(2) \to SO(3)$ is the statement that $\pm M$ give the same rotation. In the algebra the double cover has to be argued from the norm form; in the matrix form it is visible, because $-I_2$ is a unit-norm element acting trivially on the material sector.

## What the Matrix Form Makes Visible

The representation is a change of coordinates, and its value is what the new coordinates make obvious. Collected: the scalar part is a trace; the norm form is a determinant; invertibility is nonzero determinant; the material and informational sectors are the anti-Hermitian and Hermitian matrices; the observables are the Hermitian matrices generated by $\sigma_k$; the pure states are rank-one projectors on the null cone; the unit-norm group is $\mathrm{SL}(2,\mathbb{C})$; and the zero divisors are the singular matrices. Each of these is a theorem in the algebra and an inspection in the matrix form.

The limitation is equally clear. The matrix form is a representation of the **complexified** algebra: it uses $i$ in its entries, so it identifies $\mathbb{B}$ with $M_2(\mathbb{C})$ and does not, by itself, display the real structure that distinguishes the material sector from the informational one. That structure — the choice of $\flat$, and the physical statement that $\mathbb{M}_-$ is the sector where mass lives — is a choice of real form, and it is visible in the algebra and in the Hermitian/anti-Hermitian split, but not in the identification $\mathbb{B} \cong M_2(\mathbb{C})$ alone. The matrix form is the computational face of the algebra, not the whole of it.

## Summary

The matrix representation of the biquaternion algebra is the isomorphism $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ given by $\Phi(e_0) = I_2$ and the three basis matrices asserted above, with $\Phi(i) = iI_2$ on the central scalar. The Pauli matrices are the basis images multiplied by the factor $i$, that is $\sigma_k = i\,\Phi(e_k) = \Phi(ie_k)$, equivalently $\Phi(e_k) = -i\,\sigma_k$.

- The signs are forced: $e_k^2 = -e_0$ requires the factor $i$, and $e_1e_2 = +e_3$ requires the minus sign. Both are checked by multiplying the four basis matrices. The equivalent statement, $\sigma_k = \Phi(ie_k)$, is why the Hermitian elements of the algebra are its observables.
- The trace is twice the scalar part, $\mathrm{Tr}(\tilde{Q}) = 2Q_0$, and the determinant **is** the norm form, $\det(\tilde{Q}) = N(\tilde{Q}) = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2$. Invertibility, multiplicativity of the norm, and the zero divisors as singular matrices all follow.
- The four subspaces are the scalar matrices (center), the matrices $\begin{pmatrix} z & w \\ -\bar{w} & \bar{z}\end{pmatrix}$ (real quaternions), the Hermitian matrices ($\mathbb{M}_+$, observables) and the anti-Hermitian matrices ($\mathbb{M}_-$, material sector).
- The minimal left ideals are the matrix **columns**: $P_\pm = \tfrac12(e_0 \pm ie_3)$ map to $E_{11}$ and $E_{22}$, and $\mathbb{B} = \mathbb{B}P_+ \oplus \mathbb{B}P_-$ is the split into the two chiralities. Left multiplication preserves each column, while right multiplication by $\tfrac12(ie_1 - e_2) \mapsto E_{12}$ carries the first column onto the second — it annihilates the second — and that is why the mass term of the Dirac equation is a right multiplication. The algebra is simple, so these ideals are one-sided, not two-sided.
- Quaternion conjugation is the adjugate $\epsilon M^{\mathsf T}\epsilon^{-1}$ and complex conjugation is $\epsilon\overline{M}\epsilon^{-1}$; both are dressed by the antisymmetric form $\epsilon = i\sigma_2 = \Phi(-e_2)$. Hermitian conjugation is the conjugate transpose and $\flat = -\dagger$ is its negative, neither of them dressed. Entrywise conjugation of $M$ on its own is not the image of any involution of the algebra.
- The physics is read off the matrices: $\tilde{S}_k = \tfrac{\hbar}{2}ie_k \mapsto \tfrac{\hbar}{2}\sigma_k$; the pure states are the rank-one projectors and are the null elements $N(p) = 0$; the density matrix $\rho = \tfrac12(I_2 + \mathbf{r}\cdot\boldsymbol{\sigma})$ has $r_k = \mathrm{Tr}(\rho\sigma_k)$ on the Bloch ball.
- Unit norm form is unit determinant, so the unit-norm biquaternions are $\mathrm{SL}(2,\mathbb{C})$, with the rotations unitary and the boosts Hermitian.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ | The isomorphism converting a biquaternion into its matrix |
| $\mathbb{B} \cong M_2(\mathbb{C})$ | Biquaternion algebra as $2\times 2$ complex matrices |
| $\Phi(e_0) = I_2$, $\Phi(e_k)$ as in the section *The Representation* | The representation; $\Phi(i) = iI_2$ on the central scalar |
| $\sigma_1, \sigma_2, \sigma_3$ | Pauli matrices, $\sigma_k = i\,\Phi(e_k) = \Phi(ie_k)$, equivalently $\Phi(e_k) = -i\,\sigma_k$, so $\sigma_k^2 = I_2$ |
| $\tilde{Q} \mapsto \begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3\end{pmatrix}$ | Image of a general biquaternion |
| $\mathrm{Tr}(\tilde{Q}) = 2Q_0$ | Trace is twice the scalar part |
| $\det(\tilde{Q}) = N(\tilde{Q})$ | Determinant is the norm form |
| $\bar{\tilde{Q}} \mapsto \mathrm{adj}\,M = \epsilon M^{\mathsf T}\epsilon^{-1}$ | Quaternion conjugation is the adjugate |
| $\tilde{Q}^* \mapsto \epsilon\overline{M}\epsilon^{-1}$ | Complex conjugation, dressed by $\epsilon$ |
| $\epsilon = i\sigma_2 = \Phi(-e_2)$ | The antisymmetric form dressing bar and star |
| $\tilde{Q}^\dagger \mapsto M^\dagger$ | Hermitian conjugation is the conjugate transpose |
| $\tilde{Q}^\flat \mapsto -M^\dagger$ | Anti-Hermitian conjugation; the real structure |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian and anti-Hermitian matrices |
| $P_\pm = \tfrac12(e_0 \pm ie_3)$ | Idempotents generating the two minimal left ideals; $\Phi(P_\pm) = E_{11}, E_{22}$ |
| $\mathbb{B}P_+$, $\mathbb{B}P_-$ | The two matrix **columns**, i.e. the two chiralities; $\mathbb{B} = \mathbb{B}P_+ \oplus \mathbb{B}P_-$ |
| $x = \tfrac12(ie_1 - e_2) \mapsto E_{12}$ | Right multiplication carries $\mathbb{B}P_+$ onto $\mathbb{B}P_-$; the chirality coupling |
| $\tilde{S}_k = \tfrac{\hbar}{2}ie_k \mapsto \tfrac{\hbar}{2}\sigma_k$ | Spin operators |
| $\rho = \tfrac12(I_2 + \mathbf{r}\cdot\boldsymbol{\sigma})$ | Density matrix; Bloch vector $\mathbf{r}$, $r_k = \mathrm{Tr}(\rho\sigma_k)$ |
| $\mathrm{SL}(2,\mathbb{C})$ | Image of the unit-norm biquaternions |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation of the quaternion units and their products.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of the complexified algebra.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), Chapter 3, for the matrix representations of biquaternions and the adjugate form of quaternion conjugation.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions," *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the representation theory and the conventions in use in applied work.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Pauli algebra, the relation $ie_k \leftrightarrow \sigma_k$, and the $\mathrm{SL}(2,\mathbb{C})$ description of the Lorentz group.
- Bertfried Fauser, "On the equivalence of Daviau's space Clifford algebraic and Hestenes' geometric algebra formulations of physics," arXiv:hep-th/9908200, for the identification chain that places $\mathbb{H}\oplus\mathbb{H}$, the Pauli algebra and the biquaternions in the same isomorphism class.
