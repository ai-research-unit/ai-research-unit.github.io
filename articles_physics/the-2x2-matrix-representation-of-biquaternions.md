# __The 2×2 Matrix Representation of Biquaternions__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is isomorphic, as a complex algebra, to the algebra of $2 \times 2$ complex matrices,

$$
\mathbb{B} \cong M_2(\mathbb{C}),
$$

and the isomorphism is written $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ throughout. A biquaternion and a $2 \times 2$ complex matrix are the same object written twice, and this is the form in which every statement about the algebra becomes an arithmetic check: the trace reads off the scalar part, the determinant **is** the norm form, invertibility becomes non-vanishing determinant, the Hermitian subspace becomes the Hermitian matrices, and the minimal left ideals become the matrix columns.

The article supplies the $2 \times 2$ matrices that carry a single chirality, that is, the simple module $S = \mathbb{C}^2$ on which the algebra acts irreducibly. Its coefficient space is that of *The Four-Vector Representation of Biquaternions*, the left multiplication written on that space is that of *The 4×4 Regular Matrix Representation of Biquaternions*, and that representation is the direct sum $S \oplus S$ of two copies of the simple module treated here. The article states the assignment, checks that the four basis matrices multiply as the four units do, notes why the signs cannot be chosen differently, and reads off the invariants, the six subspaces, the two ideals as columns, the conjugations, and the spin and qubit structures.

The assignment is the one fixed by *Biquaternion Algebraic Representations* in the mathematics pages. It is not free: it is used identically by the spin, qubit, Bell-state, Dirac and Fock-space articles, and the two conventions a reader is likely to meet elsewhere do not agree with it.

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

with $\Phi(i) = i\,\Phi(e_0)$ on the central scalar $\mathbb{C}_{\mathbb{B}}$.
<!-- CONVENTION — the matrix basis: the four basis images are asserted, and the images of the Hermitian units follow from them as Phi(i e_k) = i Phi(e_k) by C-linearity, needing no new choice. Both the factor i and the sign are forced (e_k^2 = -e_0 and e_1 e_2 = e_3), so a reviewer must not "correct" the assignment by making the three images real, nor by negating all three, and must not treat the choice as free. -->

This is the assignment of the mathematics article *Biquaternion Algebraic Representations*, taken over unchanged. A general biquaternion $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$ therefore maps to

$$
\Phi(\tilde{Q}) = Q_0\,\Phi(e_0) + Q_1 \Phi(e_1) + Q_2 \Phi(e_2) + Q_3 \Phi(e_3)
= \begin{pmatrix} Q_0 - i Q_3 & -i Q_1 - Q_2 \\ -i Q_1 + Q_2 & Q_0 + i Q_3 \end{pmatrix}.
$$

**The check.** The assignment is the right one because the four matrices multiply as the four units do. Squaring a vector image,

$$
\Phi(e_1)^2 = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}^2 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -\Phi(e_0),
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

square to $+\Phi(e_0)$. Assigning them to $e_1, e_2, e_3$ would therefore give $e_k^2 = +e_0$, the wrong sign. Multiplying by the complex unit repairs this, and both $+i$ and $-i$ times these matrices satisfy $e_k^2 = -e_0$; the squaring relation alone therefore requires the factor $i$ but leaves its sign open.

**The sign is then forced by the cross-relations.** The alternative assignment sends $e_k$ to $-\Phi(e_k)$, reversing the sign of every vector image. The product of the images of $e_1$ and $e_2$ is then

$$
\big(-\Phi(e_1)\big)\big(-\Phi(e_2)\big) = \Phi(e_1)\Phi(e_2) = \Phi(e_3),
$$

because the two minus signs cancel — while the image of $e_3$ under that assignment is $-\Phi(e_3)$. The product of the images comes out as *minus* the image of the required value, so the alternative fails at $e_1e_2 = e_3$; the same cancellation of signs makes it fail at every other cross-relation, where the target is again a single vector image and flips while the product does not. Under the assignment asserted above the same computation gives

$$
\Phi(e_1)\Phi(e_2) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
= \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} = \Phi(e_3),
$$

which is exactly the image of $e_3$. So the assignment asserted above passes the check and the alternative fails it. Both statements were verified on the explicit matrices.

The physical reading of the sign is the one recorded in the remark above. The Hermitian quaternion units $ie_k$ are Hermitian elements, and their images $\Phi(ie_k) = i\,\Phi(e_k)$ are the Hermitian matrices; the imaginary quaternion units themselves are not, since $\Phi(e_k)^\dagger = -\Phi(e_k)$ in the three vector cases. The assignment is thus the one under which the Hermitian elements of the algebra become the Hermitian matrices, and that is what makes it an algebra of observables. It is why the sign is a consequence of the algebra rather than a convention that could have gone either way.

## Trace, Determinant and the Norm Form

**The trace is twice the scalar part.** The trace is taken in this representation, with $\mathrm{Tr}(e_0) = 2$ as it comes from $\Phi(e_0) = I_2$. From the general matrix,

$$
\mathrm{Tr}(\tilde{Q}) = (Q_0 - i Q_3) + (Q_0 + i Q_3) = 2 Q_0 .
$$

So the scalar part of a biquaternion is a matrix trace, and the traceless matrices are the vector parts. This is why the center subspace is the scalar matrices: an element commutes with everything exactly when its matrix is a multiple of the identity.

The factor $2$ — not $1$ — is a consequence of $\Phi(e_0) = I_2$ and not a normalisation: it comes with the four basis images and cannot be divided out. Restricting neither argument to $\mathbb{M}_+$, the identity reads

$$
\mathrm{Tr}(\tilde{Q}_1\tilde{Q}_2) = 2\,\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2) \qquad \text{for all } \tilde{Q}_1, \tilde{Q}_2 \in \mathbb{B},
$$

where $\mathrm{Tr}(\tilde{Q}_1\tilde{Q}_2)$ is the trace of the product of the matrices, $\mathrm{Tr}(\Phi(\tilde{Q}_1)\Phi(\tilde{Q}_2))$. This follows from $\mathrm{Tr}\,\Phi(\tilde{Q}) = 2Q_0$, the $\mathbb{C}$-linearity of $\Phi$ and the multiplicativity of the trace; the pairs drawn from $\mathbb{M}_+$ are the case in which the pairing is real. It is the form in which the operator articles use the identity, and in the quantum-information articles it is the Born rule, $p = \mathrm{Tr}(\tilde{P}\tilde{\rho})$.

**The determinant is the norm form.** Expanding,

$$
\det(\tilde{Q}) = (Q_0 - iQ_3)(Q_0 + iQ_3) - (-iQ_1 - Q_2)(-iQ_1 + Q_2)
= (Q_0^2 + Q_3^2) - \big[(-iQ_1)^2 - Q_2^2\big] = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = N(\tilde{Q}).
$$

This is the central fact of the representation. The norm form, defined algebraically as $\tilde{Q}\bar{\tilde{Q}}$, is the determinant of the corresponding matrix — not merely similar to it, but equal to it. Three consequences follow at once.

**Invertibility.** A biquaternion is invertible exactly when its norm form is nonzero, because a matrix is invertible exactly when its determinant is. The algebraic inverse $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$ is the matrix inverse, since for a $2\times 2$ matrix the adjugate is $\det(M)\,M^{-1}$.

**Multiplicativity.** $N(\tilde{Q}\tilde{R}) = N(\tilde{Q})N(\tilde{R})$ holds because the determinant is multiplicative. The algebraic proof of this identity is a computation in eight real components; in the matrix form it is one line, and this is the clearest illustration of what the representation buys.

**Zero divisors.** The zero divisors of $\mathbb{B}$ are the singular matrices. The null cone $N(\tilde{Q}) = 0$ is the determinant-zero locus. Since $\mathbb{B}$ is not a division algebra, this locus is nonempty, and its elements are exactly the matrices of rank at most one.

## The Six Subspaces

Each of the algebra's distinguished subspaces has a description in matrix language, and each description is a statement a physicist recognizes. Following the conventions article, the components of a general biquaternion are written $Q_0, Q_1, Q_2, Q_3$ and are **complex**; the parameters of a real subspace are written in lowercase and are **real**, with the prime recording which slot carries the $i$: $q_\mu$ is the coefficient entering with $e_\mu$ and $q'_\mu$ the one entering with $ie_\mu$, so that $Q_\mu = q_\mu + iq'_\mu$ — unprimed the real part, primed the imaginary part. Every matrix below is the one rule

$$
\Phi(\tilde{Q}) = Q_0\,\Phi(e_0) + Q_1\,\Phi(e_1) + Q_2\,\Phi(e_2) + Q_3\,\Phi(e_3),
$$

with the subspace's own parametrisation substituted for the coefficients:

| subspace | defining condition | basis image | parametrisation | image |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\bar{\tilde{Q}} = \tilde{Q}$ | $\Phi(e_0)$ | $Q_0 = q_0 + iq'_0$ | the scalar matrices |
| $\mathrm{Vect}(\mathbb{B})$ | $\bar{\tilde{Q}} = -\tilde{Q}$ | $\Phi(e_1),\ \Phi(e_2),\ \Phi(e_3)$ | $Q_0 = 0$ | the traceless matrices |
| $\mathbb{H}_{\mathbb{B}}$ | $\tilde{Q}^* = \tilde{Q}$ | $\Phi(e_0),\ \Phi(e_1),\ \Phi(e_2),\ \Phi(e_3)$ | $Q_\mu = q_\mu$ | $\begin{pmatrix} z & w \\ -\bar{w} & \bar{z} \end{pmatrix}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\tilde{Q}^* = -\tilde{Q}$ | $i\Phi(e_0),\ i\Phi(e_1),\ i\Phi(e_2),\ i\Phi(e_3)$ | $Q_\mu = iq'_\mu$ | $i$ times the quaternion matrices |
| $\mathbb{M}_+$ | $\tilde{Q}^\dagger = \tilde{Q}$ | $\Phi(e_0),\ i\Phi(e_1),\ i\Phi(e_2),\ i\Phi(e_3)$ | $Q_0 = q_0$, $Q_k = iq'_k$ | a Hermitian matrix |
| $\mathbb{M}_-$ | $\tilde{Q}^\flat = \tilde{Q}$ | $i\Phi(e_0),\ \Phi(e_1),\ \Phi(e_2),\ \Phi(e_3)$ | $Q_0 = iq'_0$, $Q_k = q_k$ | $i$ times a Hermitian matrix |

The four basis images $\Phi(e_\mu)$ are the ones displayed in *The Representation*; no Pauli matrix is needed to write any of the matrices down. Each subspace is then taken in its turn below: the center subspace, the vector subspace, the quaternion subspace, the antiquaternion subspace, the informational subspace and the material subspace. The vector subspace is the only one of the six that is not four- or two-dimensional. The conventions article calls $\mathbb{M}_+$ and $\mathbb{M}_-$ the informational and material *sectors*; here, with all six on the same footing, they are called subspaces like the other four.

Each subspace is displayed as a three-step chain: the matrix in the complex coefficients $Q_\mu$, the same matrix with that subspace's real parameters substituted, and the same matrix in the physical coordinates, under the one dictionary

$$
q_0 = ct', \quad q'_0 = ct, \quad q_1 = x, \quad q_2 = y, \quad q_3 = z, \quad q'_1 = x', \quad q'_2 = y', \quad q'_3 = z' ,
$$

the unprimed slot carrying the informational time $ct'$ and the material space $\mathbf{x}$, the primed slot the material time $ct$ and the informational space $\mathbf{x}'$.

### The Center Subspace $\mathbb{C}_{\mathbb{B}}$

The center subspace, the fixed space of quaternion conjugation $\bar{\cdot}$: the elements $Q_0e_0$ with $Q_0$ complex, carried onto the scalar matrices,

$$
\Phi(\tilde{Q}) = Q_0\,\Phi(e_0) = \begin{pmatrix} Q_0 & 0 \\ 0 & Q_0 \end{pmatrix}
= \begin{pmatrix} q_0 + iq'_0 & 0 \\ 0 & q_0 + iq'_0 \end{pmatrix}
= \begin{pmatrix} ct' + ict & 0 \\ 0 & ct' + ict \end{pmatrix},
$$

the scalar matrix reached from the complex coefficient through its two real parameters to the two physical times. The one subspace with no vector part: $Q_0e_0$ is Hermitian exactly when $Q_0$ is real and anti-Hermitian exactly when $Q_0$ is purely imaginary. Its two complex coefficients reduce to the two real parameters $q_0 = ct'$ and $q'_0 = ct$, so its physical reading is the two temporal directions together,

$$
\tilde{Q} = q_0e_0 + q'_0(ie_0) = ct'\,e_0 + ict\,e_0 ,
$$

the informational time and the material time. It is the only one of the six of real dimension two, and the only commutative one; the vector subspace and the four four-dimensional ones are the rest.

### The Vector Subspace $\mathrm{Vect}(\mathbb{B})$

The complement of the center subspace: the elements with no scalar part, those with $\mathrm{Sc}(\tilde{Q}) = 0$, carried onto the **traceless** matrices,

$$
\Phi(\tilde{Q}) = \begin{pmatrix} -iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & iQ_3 \end{pmatrix}
= \begin{pmatrix} -i(q_3 + iq'_3) & -i(q_1 + iq'_1) - (q_2 + iq'_2) \\ -i(q_1 + iq'_1) + (q_2 + iq'_2) & i(q_3 + iq'_3) \end{pmatrix}
= \begin{pmatrix} -i(z + iz') & -i(x + ix') - (y + iy') \\ -i(x + ix') + (y + iy') & i(z + iz') \end{pmatrix}, \qquad \mathrm{Tr}\,\Phi = 0 .
$$

Its image is exactly $\mathfrak{sl}(2,\mathbb{C})$, the traceless complex matrices, so the third split $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$ of the relations article reads here as the trace decomposition $M_2(\mathbb{C}) = \mathbb{C}\Phi(e_0) \oplus \mathfrak{sl}(2,\mathbb{C})$: scalar part against traceless part. It is the **anti-fixed space** of quaternion conjugation, the elements with $\bar{\tilde{Q}} = -\tilde{Q}$, whose fixed space is the center subspace above; equivalently it is the kernel of the scalar part. It is the only one of the six that is six-dimensional, being three-dimensional over $\mathbb{C}$. Under the commutator it is closed, $[\mathfrak{sl}_2,\mathfrak{sl}_2] \subseteq \mathfrak{sl}_2$, and indeed it is the derived subspace $[\mathbb{B},\mathbb{B}]$; under multiplication it is not — the product of two traceless matrices need not be traceless, since $\mathrm{Tr}(M^2) = -2\det M$. Its six real parameters are the two spatial blocks together,

$$
\tilde{Q} = q_1e_1 + q_2e_2 + q_3e_3 + q'_1(ie_1) + q'_2(ie_2) + q'_3(ie_3) = \mathbf{x} + i\mathbf{x}' ,
$$

so its real and imaginary parts are the material and the informational space block, $\mathrm{Vect}(\mathbb{B}) = X_{\mathrm{m}} \oplus X_{\mathrm{i}}$: it takes one spatial block from $\mathbb{M}_+$ and one from $\mathbb{M}_-$, the spatial counterpart of the center subspace's two temporal blocks. Reading its entries back off the traceless matrix returns the three complex coefficients $Q_k = q_k + iq'_k$, whose real and imaginary parts are the two spatial vectors. Its determinant is the norm form with the scalar term dropped, $\det = Q_1^2 + Q_2^2 + Q_3^2$.

### The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$

The real-quaternion subspace, the fixed space of complex conjugation ${}^{*}$: the elements with all four $q_\mu$ real, carried from the basis $\{e_0, e_1, e_2, e_3\}$ onto the four basis images themselves,

$$
\big\{\, \Phi(e_0),\ \Phi(e_1),\ \Phi(e_2),\ \Phi(e_3) \,\big\},
$$

with no factor of $i$ anywhere — this is the image of the algebra's own basis, and the one subspace whose matrix basis is the assignment $\Phi(e_\mu)$ read off just as it stands. Writing its general element as $q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3$, the same three-step chain applies, with the complex coefficients and the real parameters the same four numbers,

$$
\Phi(\tilde{Q}) = \begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3 \end{pmatrix}
= \begin{pmatrix} q_0 - iq_3 & -iq_1 - q_2 \\ -iq_1 + q_2 & q_0 + iq_3 \end{pmatrix}
= \begin{pmatrix} ct' - iz & -ix - y \\ -ix + y & ct' + iz \end{pmatrix},
$$

with $q_0 = ct'$ and $q_k = x_k$. Naming the two complex entries,

$$
\Phi(q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3) = \begin{pmatrix} z & w \\ -\bar{w} & \bar{z} \end{pmatrix}, \qquad z = q_0 - iq_3, \quad w = -iq_1 - q_2 ,
$$

where the entry $z$ is this one complex number, the combination $q_0 - iq_3$ of the two physical parameters on the diagonal. The letter is doing double duty: in the chain above, the $z$ inside the combination is the spatial coordinate $q_3 = z$ of the four-vector article, while in this display the whole entry is named $z$, and the combination $q_0 - iq_3$ is what says which is meant.

That is the matrix statement of $M = \epsilon\overline{M}\epsilon^{-1}$. The trace is $2q_0$, twice the scalar part, and the determinant is

$$
\det = |z|^2 + |w|^2 = q_0^2 + q_1^2 + q_2^2 + q_3^2 ,
$$

a sum of squares, which vanishes only at the zero element. This is a four-**real**-dimensional set, not the four-dimensional complex space of all matrices with $z, w \in \mathbb{C}$, and on it the determinant is **definite** — which is the matrix reason $\mathbb{H}$ is a division algebra while $\mathbb{B}$ is not. Removing the complex coefficients from the algebra makes the norm form positive definite, and that is all that separates the two cases.

### The Antiquaternion Subspace $i\mathbb{H}_{\mathbb{B}}$

The anti-fixed space of complex conjugation: the elements with all four $q'_\mu$ real, carried from the basis $\{ie_0, ie_1, ie_2, ie_3\}$ onto $i$ times the four basis images,

$$
\big\{\, i\Phi(e_0),\ i\Phi(e_1),\ i\Phi(e_2),\ i\Phi(e_3) \,\big\}.
$$

Since $\Phi$ is $\mathbb{C}$-linear and $i\mathbb{H}_{\mathbb{B}} = i\,\mathbb{H}_{\mathbb{B}}$, its image is simply $i$ times the image of the quaternion subspace, $\Phi(iq'_\mu e_\mu) = i\,\Phi(q'_\mu e_\mu)$, and the chain is the quaternion one under the factor $i$,

$$
\Phi(\tilde{Q}) = \begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3 \end{pmatrix}
= i\begin{pmatrix} q'_0 - iq'_3 & -iq'_1 - q'_2 \\ -iq'_1 + q'_2 & q'_0 + iq'_3 \end{pmatrix}
= i\begin{pmatrix} ct - iz' & -ix' - y' \\ -ix' + y' & ct + iz' \end{pmatrix},
$$

with $q'_0 = ct$ and $q'_k = x'_k$. Naming the two complex entries as in the quaternion case,

$$
\Phi(iq'_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3) = \begin{pmatrix} iz' & iw' \\ -i\bar{w}' & i\bar{z}' \end{pmatrix}, \qquad z' = q'_0 - iq'_3, \quad w' = -iq'_1 - q'_2 ,
$$

with the same double duty of the letter $z'$, resolved there too by the combination $q'_0 - iq'_3$.

The determinant changes sign with the factor, $\det = -(q'^2_0 + q'^2_1 + q'^2_2 + q'^2_3)$, **negative definite** — the exact mirror of the definite form on $\mathbb{H}_{\mathbb{B}}$. Together the two images exhaust $M_2(\mathbb{C})$, so the real-and-imaginary split of the algebra is, in matrix language, the split of $M_2(\mathbb{C})$ into the quaternion matrices and $i$ times them.

### The Informational Subspace $\mathbb{M}_+$

The Hermitian subspace, the fixed space of $\dagger$: the elements with $q_0, q'_1, q'_2, q'_3$ real, carried from the basis $\{e_0, ie_1, ie_2, ie_3\}$ onto the four matrices

$$
\big\{\, \Phi(e_0),\ i\Phi(e_1),\ i\Phi(e_2),\ i\Phi(e_3) \,\big\}
= \left\{\,
\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},\
\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},\
\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix},\
\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \,\right\},
$$

the three non-identity members being the Hermitian basis matrices that the remark of *The Representation* names the Pauli matrices.

Writing the general element of the subspace as $\tilde{Q} = q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 = (ct')\,e_0 + (ix')\,e_1 + (iy')\,e_2 + (iz')\,e_3$, with $q_0 = ct'$ and $q'_k = x'_k$ real, the same three-step chain gives

$$
\Phi(\tilde{Q}) = \begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3 \end{pmatrix}
= \begin{pmatrix} q_0 + q'_3 & q'_1 - iq'_2 \\ q'_1 + iq'_2 & q_0 - q'_3 \end{pmatrix}
= \begin{pmatrix} ct' + z' & x' - iy' \\ x' + iy' & ct' - z' \end{pmatrix},
$$

the general Hermitian $2 \times 2$ matrix — the general observable of a two-state system — with scalar part half the trace, $\mathrm{Tr}\,\Phi(\tilde{Q}) = 2q_0$, real, against the purely imaginary $2iq'_0$ of the material subspace. Its determinant is

$$
\det\Phi(\tilde{Q}) = q_0^2 - q'^2_1 - q'^2_2 - q'^2_3 ,
$$

the mirror interval of signature $(1,3)$, read on the informational coordinate $(ct')\,e_0 + i\,x'\,e_1 + i\,y'\,e_2 + i\,z'\,e_3$, that is $q_0 = ct'$, $q'_1 = x'$, $q'_2 = y'$, $q'_3 = z'$.

### The Material Subspace $\mathbb{M}_-$

The anti-Hermitian subspace, the fixed space of $\flat$: the elements with $q'_0, q_1, q_2, q_3$ real, carried from the basis $\{ie_0, e_1, e_2, e_3\}$ onto the four matrices

$$
\big\{\, i\Phi(e_0),\ \Phi(e_1),\ \Phi(e_2),\ \Phi(e_3) \,\big\}
= \left\{\,
i\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},\
\begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix},\
\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix},\
\begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} \,\right\}.
$$

Writing the general element as $\tilde{Q} = iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 = ic\,t\,e_0 + x\,e_1 + y\,e_2 + z\,e_3$, with $q'_0 = ct$ and $q_k = x_k$ real, the chain from the complex coefficients to the real parameters to the physical coordinates is

$$
\Phi(\tilde{Q}) = \begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3 \end{pmatrix}
= \begin{pmatrix} iq'_0 - iq_3 & -iq_1 - q_2 \\ -iq_1 + q_2 & iq'_0 + iq_3 \end{pmatrix}
= \begin{pmatrix} ict - iz & -ix - y \\ -ix + y & ict + iz \end{pmatrix}
= i\begin{pmatrix} q'_0 - q_3 & -q_1 + iq_2 \\ -q_1 - iq_2 & q'_0 + q_3 \end{pmatrix},
$$

which is $i$ times a Hermitian matrix: the scalar part is carried by $i$, and the vector signs are reversed. Its trace is $2iq'_0$, purely imaginary, and its determinant is

$$
\det\Phi(\tilde{Q}) = N(\tilde{Q}) = -q'^2_0 + q_1^2 + q_2^2 + q_3^2 ,
$$

the Minkowski interval of signature $(3,1)$: the $ict$ metric of the corpus, read on the material four-position of the companion article, $\tilde{Q} = ict\,e_0 + x\,e_1 + y\,e_2 + z\,e_3$, that is $q'_0 = ct$, $q_1 = x$, $q_2 = y$, $q_3 = z$, giving $-(ct)^2 + \mathbf{x}^2$. This is the most economical place to see why the material subspace is the **anti**-Hermitian one: the anti-Hermitian matrices are exactly those on which the determinant comes out with one minus sign.

### How They Fit Together

The relations among the subspaces — the three splits, their intersections, and the pairs that span the algebra — are worked out in *Relations Between Subspaces*. Two consequences are used repeatedly in this article and are recorded here.

**The three splits cross.** The split $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$ is the trace decomposition and is not four-plus-four at all: it separates the two-dimensional center subspace from the six-dimensional traceless part. The other two splits, the real-and-imaginary split $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$ and the sector split $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$, are both four-plus-four, and neither refines the other. Each of $\mathbb{M}_+$ and $\mathbb{M}_-$ takes its scalar from one half and its vectors from the other, which is why the prime pattern is three-and-one rather than four-and-none. Multiplication by the central $i$ exchanges $\mathbb{M}_+$ and $\mathbb{M}_-$, and exchanges the two halves.

**Two of the six are subalgebras.** $\mathbb{C}_{\mathbb{B}}$ is closed under multiplication; $\mathrm{Vect}(\mathbb{B})$ is closed under the commutator but not under the product; $\mathbb{H}_{\mathbb{B}}$ is closed under multiplication; and $i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_\pm$ are neither — the product of two Hermitian matrices is Hermitian only when they commute. The center subspace meets $\mathbb{M}_+$ and $\mathbb{M}_-$ in the two central lines, $\mathbb{C}_{\mathbb{B}} \cap \mathbb{M}_+ = \mathbb{R}e_0$ and $\mathbb{C}_{\mathbb{B}} \cap \mathbb{M}_- = \mathbb{R}(ie_0)$, and every element splits as a Hermitian plus an anti-Hermitian part, $\tilde{Q} = \tfrac12(\tilde{Q} + \tilde{Q}^\dagger) + \tfrac12(\tilde{Q} - \tilde{Q}^\dagger)$, the two parts differing by the factor $i$ that carries $\mathbb{M}_-$ into $\mathbb{M}_+$.

## The Ideals as Columns and the Spinor Module

The matrix form makes the algebra's ideal structure a statement about columns. The idempotents

$$
P_+ = \tfrac12(e_0 + ie_3) \;\longmapsto\; \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = E_{11}, \qquad
P_- = \tfrac12(e_0 - ie_3) \;\longmapsto\; \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = E_{22}
$$

generate the two **columns** of the matrix algebra,

$$
\mathbb{B}P_+ = \mathbb{C}E_{11} \oplus \mathbb{C}E_{21}, \qquad \mathbb{B}P_- = \mathbb{C}E_{12} \oplus \mathbb{C}E_{22},
$$

with $\mathbb{B} = \mathbb{B}P_+ \oplus \mathbb{B}P_-$; the first column is the set of matrices whose second column vanishes, the second those whose first column vanishes. Each column is two-dimensional over $\mathbb{C}$ and minimal, and left multiplication acts on it irreducibly: the column **is** the spinor module $S = \mathbb{C}^2$ of the companion articles on the spinor module and on representation theory — the abstract simple module realised inside the algebra, with the algebra acting on it by left multiplication — and not merely a space isomorphic to it.

Two structural facts are visible in this form, and both are used by the physics articles.

**The two columns are the two chiralities.** Left multiplication preserves each column: for any $M$, the products $ME_{11}$ and $ME_{21}$ again have vanishing second column. No left multiplication can therefore relate the two columns. A mass term that couples the left- and right-handed components cannot be a left multiplication; it must be a **right** multiplication, and the element that performs it is the one carried to the off-diagonal matrix unit,

$$
\tilde{a}_{\mathrm{tr}} = \tfrac12(ie_1 - e_2) \;\longmapsto\; \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = E_{12} = |0\rangle\langle 1| .
$$

whose right action maps the first column onto the second — $E_{11} \mapsto E_{12}$ and $E_{21} \mapsto E_{22}$ — while annihilating the second. This is the matrix form of the structural reason the biquaternionic Dirac equation couples the chiralities by a right multiplication, and of the statement that the spinor module, not the whole algebra, is the carrier of the Dirac field. The element is the corpus's truncated lowering operator — the name matches the image $|0\rangle\langle 1|$ exactly — and the spinor-module articles write it $x$, with $\tilde{a}_{\mathrm{tr}}^\dagger = \tfrac12(ie_1 + e_2)$ written $y$; the pair satisfies the matrix-unit relations $xy = P_+$, $yx = P_-$, $x^2 = y^2 = 0$.

**The two-sided ideals are not among them.** Since $\mathbb{B} \cong M_2(\mathbb{C})$ is simple, its only two-sided ideals are $0$ and $\mathbb{B}$; the columns are one-sided. That is what allows the algebra to be simple and still carry two distinct chiralities, and it is why the mass term must be off-diagonal rather than a multiplication confined to a single column.

The pair $P_\pm$ used here is not the only one: every unit vector $\hat{\boldsymbol\mu}$ gives the idempotent pair $\tilde{P}_\pm(\hat{\boldsymbol\mu}) = \tfrac12(e_0 \pm i\hat{\boldsymbol\mu})$, and $P_\pm = \tilde{P}_\pm(\hat{\mathbf{e}}_3)$ is the choice for which the two columns are the coordinate columns. The projector $\tilde{P}_+(\hat{\mathbf{e}}_1)$ of the section *Spin, Qubits and the Bloch Vector* is a member of that family, corresponding to a different direction.

## The Conjugations in Matrix Form

The four involutions of the algebra become four matrix operations. Writing $M = \Phi(\tilde{Q})$:

| Involution | Definition | Matrix image |
|---|---|---|
| Quaternion conjugation | $\bar{\tilde{Q}} = Q_0e_0 - Q_1e_1 - Q_2e_2 - Q_3e_3$ | the **adjugate** $\mathrm{adj}\,M = \epsilon M^{\mathsf T}\epsilon^{-1}$ |
| Complex conjugation | $Q_\mu \mapsto Q_\mu^{*}$ | $\epsilon\,\overline{M}\,\epsilon^{-1}$ |
| Hermitian conjugation | $\tilde{Q}^\dagger = \bar{\tilde{Q}}^{\,*}$ | the **conjugate transpose** $M^\dagger$ |
| Anti-Hermitian conjugation | $\tilde{Q}^\flat = -\tilde{Q}^\dagger$ | $-\,M^\dagger$ |

Two of the four are dressed by the antisymmetric form

$$
\epsilon = \Phi(-e_2) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix},
$$
<!-- CONVENTION — the conjugation dictionary: quaternion conjugation is the adjugate epsilon M^T epsilon^-1 and complex conjugation is epsilon conj(M) epsilon^-1, while dagger and flat are undressed. A reviewer must not "simplify" complex conjugation to a plain entrywise conjugation of M: that operation is the image of no involution, sends e_1 and e_3 to minus themselves and leaves e_2 fixed, and so destroys the subspace dictionary. -->

the invariant antisymmetric form $\varepsilon$ of the spinor module: quaternion conjugation is the transpose dressed by $\epsilon$, and complex conjugation is the entrywise conjugation dressed by $\epsilon$. The adjugate statement is worth writing out, since it is the least familiar:

$$
\bar{\tilde{Q}} \;\mapsto\; \begin{pmatrix} Q_0 + i Q_3 & i Q_1 + Q_2 \\ i Q_1 - Q_2 & Q_0 - i Q_3 \end{pmatrix}
= \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
\quad\text{for}\quad M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}.
$$

Quaternion conjugation is therefore the classical adjoint, and the identity $\tilde{Q}\bar{\tilde{Q}} = N(\tilde{Q})e_0$ is the matrix identity $M\,\mathrm{adj}(M) = \det(M)\,\Phi(e_0)$. The other two are the operations a physicist expects: $\dagger$ is the conjugate transpose, so its fixed points are the Hermitian matrices, and $\flat = -\dagger$ has the anti-Hermitian matrices as its fixed points. The real structure $\flat$, which the corpus uses for the $\mathbb{M}_\pm$ split and for Majorana-type pairings, is the negative conjugate transpose.

**Complex conjugation is the one that does not act entrywise.** It is sometimes said that $\tilde{Q}^*$ conjugates the entries of the matrix. That is not true, and the reason is structural: the representation is built with the same $i$ that conjugates the coefficients, so the two operations compete. Conjugating the entries of $\Phi(\tilde{Q})$ sends $\Phi(e_1) \mapsto -\Phi(e_1)$ and $\Phi(e_3) \mapsto -\Phi(e_3)$ — the images of $e_1$ and $e_3$ to their negatives — while the image of $e_2$ is left alone; the entrywise operation is therefore not $\Phi(\tilde{Q}^*)$, and it is not the image of any involution of the algebra. The correct correspondence is the one in the table,

$$
\Phi(\tilde{Q}^*) = \epsilon\,\overline{\Phi(\tilde{Q})}\,\epsilon^{-1}, \qquad \epsilon = \Phi(-e_2),
$$

verified on explicit matrices, and the adjugate form of quaternion conjugation is the same dressing applied to the transpose. In this representation the safe rule is: use $\bar{\phantom{Q}}$, ${}^*$, $\dagger$ and $\flat$ through the four formulas above, and never conjugate the matrix entries on their own.

## Spin, Qubits and the Bloch Vector

The matrix representation is what connects the algebra to the physics of two-state systems, and the connection runs through the single identity $ie_k \mapsto \Phi(ie_k)$. The images are the Hermitian basis matrices that the remark of *The Representation* names the Pauli matrices, and the whole section is written in those images.

**Spin operators.** The spin operators of the biquaternion framework are $\tilde{S}_k = \tfrac{\hbar}{2}ie_k$, and under the isomorphism,

$$
\tilde{S}_k = \tfrac{\hbar}{2}ie_k \;\longmapsto\; \tfrac{\hbar}{2}\Phi(ie_k) = \tfrac{\hbar}{2}\,i\,\Phi(e_k) ,
$$

which are the Hermitian spin matrices. The eigenvalue statement $\tilde{S}_k^2 = \tfrac{\hbar^2}{4}e_0$, the anticommutation $\{\tilde{S}_i, \tilde{S}_j\} = \tfrac{\hbar^2}{2}\delta_{ij}e_0$ and the commutator $[\tilde{S}_i,\tilde{S}_j] = i\hbar\varepsilon_{ijk}\tilde{S}_k$ are, matrix by matrix, the standard angular-momentum algebra of a spin-$\tfrac12$ system. In the matrix form they are checked by multiplying $2\times 2$ matrices.

**States as projectors.** The rank-one idempotents of $\mathbb{M}_+$ are the pure-state projectors. The element

$$
\tilde{P}_+(\hat{\mathbf{e}}_1) = \tfrac{1}{2}(e_0 + ie_1) \;\longmapsto\; \tfrac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}
= \tfrac{1}{2}\big(\Phi(e_0) + \Phi(ie_1)\big)
$$

satisfies $\tilde{P}^2 = \tilde{P}$, has trace $1$ and determinant $0$: it is a rank-one projector, hence a pure state. Its complement $\tilde{P}_-(\hat{\mathbf{e}}_1) = \tfrac12(e_0 - ie_1)$ is the orthogonal projector, and $\tilde{P}_+(\hat{\mathbf{e}}_1) + \tilde{P}_-(\hat{\mathbf{e}}_1) = e_0$ is $\Phi(e_0)$. Both have vanishing norm form, which is the matrix way of saying that the rank-one idempotents of $\mathbb{M}_+$ live on the null cone: a pure state is a null element of the algebra. Note that not every idempotent of $\mathbb{M}_+$ is a state: the unit $e_0$ is idempotent, and its matrix $\Phi(e_0)$ has trace $2$ and determinant $1$, so it is the full-rank projector and does not lie on the null cone. This is the representation-theoretic content of *The Biquaternion Vacuum as a Minimal Idempotent*.

**The density matrix.** A general mixed state is

$$
\rho = \tfrac{1}{2}\big(\Phi(e_0) + r_1\Phi(ie_1) + r_2\Phi(ie_2) + r_3\Phi(ie_3)\big),
$$

with Bloch vector $\mathbf{r} \in \mathbb{R}^3$. It is Hermitian with unit trace, so it lies in the image of $\mathbb{M}_+$, and the Bloch components are recovered by the trace pairing,

$$
r_k = \mathrm{Tr}\big(\rho\,\Phi(ie_k)\big),
$$

verified for all three components. The purity condition $\mathrm{Tr}(\rho^2) = 1$ is $|\mathbf{r}| = 1$, and the boundary of the Bloch ball is the set of rank-one projectors, i.e. the pure states found above. So the three-level description — biquaternion state, density matrix, Bloch vector — is one statement in three coordinate systems, and the passage between them is matrix multiplication and the trace.

## The Groups

The multiplicative group of the algebra has a matrix image with a standard name. An element of unit norm form, $N(\tilde{Q}) = e_0$, has

$$
\det\Phi(\tilde{Q}) = 1,
$$

so the unit-norm biquaternions map into the special linear group,

$$
\{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) = e_0\} \;\cong\; \mathrm{SL}(2,\mathbb{C}).
$$

This is the matrix form of the statement that the unit-norm elements act on $\mathbb{M}_-$ by rotor conjugation and generate the Lorentz group. Concretely, the rotation rotors are the unit-norm elements of $\mathbb{H}_{\mathbb{B}}$, which map to the $SU(2)$ matrices

$$
\tilde{R}(\theta, \hat{\mathbf{n}}) = \exp\!\big(\tfrac{1}{2}\theta \hat{\mathbf{n}}\cdot e\big) \;\longmapsto\; \exp\!\big(\tfrac{1}{2}\theta\,n_k\,\Phi(e_k)\big),
$$

and the boost rotors are the Hermitian unit-norm elements, which map to the Hermitian $\mathrm{SL}(2,\mathbb{C})$ matrices. The two cases are distinguished in the matrix form by Hermiticity, exactly as they are distinguished in the algebra by the split $\mathbb{M}_+ \oplus \mathbb{M}_-$.

The advantage of the matrix form here is not computational but structural: writing a general unit-norm element as a rotation times a boost is the polar decomposition of its $\mathrm{SL}(2,\mathbb{C})$ matrix into a unitary factor and a positive Hermitian one, and the double cover $SU(2) \to SO(3)$ is the statement that $\pm M$ give the same rotation. In the algebra the double cover has to be argued from the norm form; in the matrix form it is visible, because $-\Phi(e_0)$ is a unit-norm element acting trivially on the material subspace.

The identification is structural, and it is not the cheaper route to the numbers. Sangwine & Hitzer note that $\Phi(\tilde{Q})$ carries a four-fold redundancy — the $4\times4$ complex representation of a biquaternion is one of a special form, not an arbitrary complex matrix, and a general numerical polar decomposition of an arbitrary matrix need not preserve that form accurately over a series of computational steps — so the biquaternion algorithm needs less memory and fewer operations. Their algorithm also obtains the hyperbolic factor by dividing out the trigonometric factor, which is cheaper than forming the square root $\sqrt{\tilde{Q}\tilde{Q}^\dagger}$ used above to exhibit the identity and the Hermiticity: the square root is the proof that the factor exists, and the division is how it is computed.

## What the Matrix Form Makes Visible

The representation is a change of coordinates, and its value is what the new coordinates make obvious. Collected: the scalar part is a trace; the norm form is a determinant; invertibility is nonzero determinant; the informational and material subspaces are the Hermitian and anti-Hermitian matrices; the observables are the Hermitian matrices generated by the images of the Hermitian units; the pure states are rank-one projectors on the null cone; the unit-norm group is $\mathrm{SL}(2,\mathbb{C})$; and the zero divisors are the singular matrices. Each of these is a theorem in the algebra and an inspection in the matrix form.

The limitation is equally clear. The matrix form is a representation of the **complexified** algebra: it uses $i$ in its entries, so it identifies $\mathbb{B}$ with $M_2(\mathbb{C})$ and does not, by itself, display the real structure that distinguishes the material subspace from the informational one. That structure — the choice of $\flat$, and the physical statement that $\mathbb{M}_-$ is the subspace where mass lives — is a choice of real form, and it is visible in the algebra and in the Hermitian/anti-Hermitian split, but not in the identification $\mathbb{B} \cong M_2(\mathbb{C})$ alone. The matrix form is the computational face of the algebra, not the whole of it.

## Summary

The matrix representation of the biquaternion algebra is the isomorphism $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ given by $\Phi(e_0) = I_2$ and the three basis matrices asserted above, with $\Phi(i) = i\,\Phi(e_0)$ on the central scalar. The images of the Hermitian units, $\Phi(ie_k) = i\,\Phi(e_k)$, are the three Hermitian basis matrices named in the remark above.

- The signs are forced: $e_k^2 = -e_0$ requires the factor $i$, and $e_1e_2 = +e_3$ requires the minus sign. Both are checked by multiplying the four basis matrices. The equivalent statement, that the images of the Hermitian elements are Hermitian, is why the Hermitian elements of the algebra are its observables.
- The trace is twice the scalar part, $\mathrm{Tr}(\tilde{Q}) = 2Q_0$, and the determinant **is** the norm form, $\det(\tilde{Q}) = N(\tilde{Q}) = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2$. Invertibility, multiplicativity of the norm, and the zero divisors as singular matrices all follow.
- The subspaces of the algebra are the center subspace $\mathbb{C}_{\mathbb{B}}$, $Q_0e_0 \mapsto Q_0\Phi(e_0)$, the only one of the six of real dimension two; the vector subspace $\mathrm{Vect}(\mathbb{B})$, the traceless part, $Q_1e_1 + Q_2e_2 + Q_3e_3 \mapsto \mathfrak{sl}(2,\mathbb{C})$, the anti-fixed space of quaternion conjugation; the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ (the matrices $\begin{pmatrix} z & w \\ -\bar{w} & \bar{z}\end{pmatrix}$ with $z = q_0 - iq_3$, $w = -iq_1 - q_2$, determinant $q_0^2 + q_1^2 + q_2^2 + q_3^2$ definite); the antiquaternion subspace $i\mathbb{H}_{\mathbb{B}}$ ($i$ times the quaternion matrices, determinant $-q'^2_0 - q'^2_1 - q'^2_2 - q'^2_3$, negative definite); the Hermitian subspace $\mathbb{M}_+$ (the informational subspace, $q_0e_0 + iq'_ke_k$ mapped to a Hermitian matrix, $\det = q_0^2 - q'^2_1 - q'^2_2 - q'^2_3 = c^2t'^2 - \mathbf{x}'^2$); and the anti-Hermitian subspace $\mathbb{M}_-$ (the material subspace, $iq'_0e_0 + q_ke_k$ mapped to $i$ times a Hermitian matrix, $\det = -q'^2_0 + q_1^2 + q_2^2 + q_3^2 = -c^2t^2 + \mathbf{x}^2$, the $ict$ interval). Every element splits into a Hermitian plus an anti-Hermitian part, $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$, with $\mathbb{M}_- = i\mathbb{M}_+$.
- The minimal left ideals are the matrix **columns**: $P_\pm = \tfrac12(e_0 \pm ie_3)$ map to $E_{11}$ and $E_{22}$, and $\mathbb{B} = \mathbb{B}P_+ \oplus \mathbb{B}P_-$ is the split into the two chiralities. Left multiplication preserves each column, while right multiplication by $\tilde{a}_{\mathrm{tr}} = \tfrac12(ie_1 - e_2) \mapsto E_{12}$ carries the first column onto the second — it annihilates the second — and that is why the mass term of the Dirac equation is a right multiplication. The algebra is simple, so these ideals are one-sided, not two-sided.
- Quaternion conjugation is the adjugate $\epsilon M^{\mathsf T}\epsilon^{-1}$ and complex conjugation is $\epsilon\overline{M}\epsilon^{-1}$; both are dressed by the antisymmetric form $\epsilon = \Phi(-e_2)$. Hermitian conjugation is the conjugate transpose and $\flat = -\dagger$ is its negative, neither of them dressed. Entrywise conjugation of $M$ on its own is not the image of any involution of the algebra.
- The physics is read off the matrices: $\tilde{S}_k = \tfrac{\hbar}{2}ie_k \mapsto \tfrac{\hbar}{2}\Phi(ie_k)$; the pure states are the rank-one projectors $\tilde{P}_\pm(\hat{\boldsymbol\mu})$ and are the null elements $N(\tilde{P}) = 0$; the density matrix $\rho = \tfrac12\big(\Phi(e_0) + r_k\Phi(ie_k)\big)$ has $r_k = \mathrm{Tr}\big(\rho\,\Phi(ie_k)\big)$ on the Bloch ball.
- Unit norm form is unit determinant, so the unit-norm biquaternions are $\mathrm{SL}(2,\mathbb{C})$, with the rotations unitary and the boosts Hermitian.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{Q}$ | An element of the algebra: the general element in *The Representation*, and the element of whichever subspace the part at hand is about. Coefficients $Q_\mu$ (complex), parameters $q_\mu$ and $q'_\mu$ (real) |
| $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ | The isomorphism converting a biquaternion into its matrix |
| $\mathbb{B} \cong M_2(\mathbb{C})$ | Biquaternion algebra as $2\times 2$ complex matrices |
| $\Phi(e_0) = I_2$, $\Phi(e_k)$ as in the section *The Representation* | The representation; $\Phi(i) = i\,\Phi(e_0)$ on the central scalar |
| $\Phi(ie_k) = i\,\Phi(e_k)$ | Images of the Hermitian units: the three Hermitian basis matrices of the remark in *The Representation*, with $\Phi(ie_k)^2 = \Phi(e_0)$ |
| $\tilde{Q} \mapsto \begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3\end{pmatrix}$ | Image of a general biquaternion |
| $\mathrm{Tr}(\tilde{Q}) = 2Q_0$ | Trace is twice the scalar part |
| $\det(\tilde{Q}) = N(\tilde{Q})$ | Determinant is the norm form |
| $\bar{\tilde{Q}} \mapsto \mathrm{adj}\,M = \epsilon M^{\mathsf T}\epsilon^{-1}$ | Quaternion conjugation is the adjugate |
| $\tilde{Q}^* \mapsto \epsilon\overline{M}\epsilon^{-1}$ | Complex conjugation, dressed by $\epsilon$ |
| $\epsilon = \Phi(-e_2)$ | The antisymmetric form dressing bar and star |
| $\tilde{Q}^\dagger \mapsto M^\dagger$ | Hermitian conjugation is the conjugate transpose |
| $\tilde{Q}^\flat \mapsto -M^\dagger$ | Anti-Hermitian conjugation; the real structure |
| $\mathbb{C}_{\mathbb{B}}$ | The center subspace: $Q_0e_0 \mapsto Q_0\Phi(e_0)$, the scalar matrices; parameters $q_0, q'_0$ with $q_0 = ct'$ and $q'_0 = ct$ |
| $\mathrm{Vect}(\mathbb{B})$ | The vector subspace, the complement of the center subspace: $Q_1e_1 + Q_2e_2 + Q_3e_3 \mapsto \begin{pmatrix} -iQ_3 & -iQ_1-Q_2 \\ -iQ_1+Q_2 & iQ_3\end{pmatrix}$, the traceless matrices $\mathfrak{sl}(2,\mathbb{C})$; the anti-fixed space of quaternion conjugation, closed under the commutator and equal to the derived subspace $[\mathbb{B},\mathbb{B}]$ |
| $\mathbb{H}_{\mathbb{B}}$ | The real-quaternion subspace: $q_0e_0 + \cdots + q_3e_3 \mapsto \begin{pmatrix} z & w \\ -\bar{w} & \bar{z}\end{pmatrix}$, $z = q_0 - iq_3$, $w = -iq_1 - q_2$, determinant $q_0^2 + q_1^2 + q_2^2 + q_3^2$ |
| $i\mathbb{H}_{\mathbb{B}}$ | The antiquaternion subspace, the anti-fixed space of complex conjugation: $i$ times the real-quaternion image, $\begin{pmatrix} iz & iw \\ -i\bar{w} & i\bar{z}\end{pmatrix}$, determinant **negative** definite. With $\mathbb{H}_{\mathbb{B}}$ it gives $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$, a split crossing the $\mathbb{M}_\pm$ split |
| $\mathbb{M}_+$ | The informational subspace, the Hermitian one: $q_0e_0 + iq'_ke_k = (ct')\,e_0 + i\mathbf{x}'$, mapped to a Hermitian matrix, $\det = q_0^2 - q'^2_1 - q'^2_2 - q'^2_3 = c^2t'^2 - \mathbf{x}'^2$; parameters $q_0, q'_1, q'_2, q'_3$, with $q_0 = ct'$ |
| $\mathbb{M}_-$ | The material subspace, the anti-Hermitian one: $iq'_0e_0 + q_ke_k = ict\,e_0 + \mathbf{x}$, mapped to $i$ times a Hermitian matrix, $\det = -q'^2_0 + q_1^2 + q_2^2 + q_3^2 = -c^2t^2 + \mathbf{x}^2$; parameters $q'_0, q_1, q_2, q_3$, with $q'_0 = ct$ |
| $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$ | The trace decomposition $M_2(\mathbb{C}) = \mathbb{C}\Phi(e_0) \oplus \mathfrak{sl}(2,\mathbb{C})$: scalar part against traceless part |
| $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ | Every element is a Hermitian part plus an anti-Hermitian part; $\mathbb{M}_- = i\mathbb{M}_+$ |
| $P_\pm = \tfrac12(e_0 \pm ie_3) = \tilde{P}_\pm(\hat{\mathbf{e}}_3)$ | Idempotents generating the two minimal left ideals; $\Phi(P_\pm) = E_{11}, E_{22}$; the spinor-module articles write them $p$, $q$ |
| $\tilde{P}_\pm(\hat{\boldsymbol\mu}) = \tfrac12(e_0 \pm i\hat{\boldsymbol\mu})$ | The rank-one idempotents of $\mathbb{M}_+$, i.e. the pure-state projectors: the idempotents with $N(\tilde{P}) = 0$ |
| $\mathbb{B}P_+$, $\mathbb{B}P_-$ | The two matrix **columns**, i.e. the two chiralities; $\mathbb{B} = \mathbb{B}P_+ \oplus \mathbb{B}P_-$ |
| $\tilde{a}_{\mathrm{tr}} = \tfrac12(ie_1 - e_2) \mapsto E_{12}$ | Right multiplication carries $\mathbb{B}P_+$ onto $\mathbb{B}P_-$; the chirality coupling. The corpus's truncated lowering operator; the spinor-module articles write it $x$, its conjugate $y$ |
| $\tilde{S}_k = \tfrac{\hbar}{2}ie_k$ | Spin operators; the images $\tfrac{\hbar}{2}\Phi(ie_k)$ are Hermitian |
| $\rho = \tfrac12\big(\Phi(e_0) + r_k\Phi(ie_k)\big)$ | Density matrix; Bloch vector $\mathbf{r}$, $r_k = \mathrm{Tr}\big(\rho\,\Phi(ie_k)\big)$ |
| $\mathrm{SL}(2,\mathbb{C})$ | Image of the unit-norm biquaternions |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation of the quaternion units and their products.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of the complexified algebra.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), Chapter 3, for the matrix representations of biquaternions and the adjugate form of quaternion conjugation.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions," *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the representation theory and the conventions in use in applied work.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Pauli algebra, the relation $ie_k \leftrightarrow \sigma_k$, and the $\mathrm{SL}(2,\mathbb{C})$ description of the Lorentz group.
- Bertfried Fauser, "On the equivalence of Daviau's space Clifford algebraic and Hestenes' geometric algebra formulations of physics," arXiv:hep-th/9908200, for the identification chain that places $\mathbb{H}\oplus\mathbb{H}$, the Pauli algebra and the biquaternions in the same isomorphism class.
- *Relations Between Subspaces* (`articles_physics/relations-between-subspaces.md`), companion article, for the relations among the subspaces whose matrices are listed here — their coordinate blocks, intersections, spans, gradings and norm forms.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y; technical report CES-535, University of Essex (2019), for the identification of the biquaternion polar decomposition with the matrix polar decomposition of $M_2(\mathbb{C})$, and for the cost comparison in the section on the groups.
