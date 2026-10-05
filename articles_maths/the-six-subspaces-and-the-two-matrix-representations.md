# __The Six Subspaces and the Two Matrix Representations__

## Introduction

The biquaternion algebra carries two basic **matrix models**, the two matrix representations of the group: the $2 \times 2$ **matrix element representation** $\Phi$, an isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$, and the $4 \times 4$ **regular matrix element representation** $\rho_L$, the matrix of left multiplication in the coefficient space of the algebra itself. The first is the model of the simple module $V = \mathbb{C}^2$ and is irreducible; the second is the model of the algebra acting on itself and is reducible. Both are the subject of their own articles — *Biquaternion 2×2 Matrix Element Representation* and *Biquaternion 4×4 Regular Matrix Element Representation* — and what is added here is the reading of the six distinguished subspaces in each of them, stated once for the six.

Both models are $\mathbb{C}$-linear and multiplicative,

$$
\Phi(\tilde P\tilde Q) = \Phi(\tilde P)\Phi(\tilde Q), \qquad
\rho_L(\tilde P\tilde Q) = \rho_L(\tilde P)\rho_L(\tilde Q),
$$

so both carry the algebra structure, and both are injective, so both see all six subspaces as distinct images. The **striking fact is that the same six matrix conditions describe the six in both models**: the scalars, the traceless matrices, the matrices coming from the real coefficients, the matrices coming from the purely imaginary ones, the Hermitian matrices and the anti-Hermitian matrices.

| subspace | condition in the $2 \times 2$ model | condition in the $4 \times 4$ model |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\Phi(\tilde Q) = A I_2$ | $\rho_L(\tilde Q) = A I_4$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\operatorname{Tr}\Phi(\tilde Q) = 0$ | $\operatorname{Tr}\rho_L(\tilde Q) = 0$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\Phi(\tilde Q)$ is fixed by $M \mapsto \epsilon \overline{M} \epsilon^{-1}$ | $\rho_L(\tilde Q)$ is real |
| $i\mathbb{H}_{\mathbb{B}}$ | $\Phi(\tilde Q)$ is anti-fixed by the same map | $\rho_L(\tilde Q)$ is purely imaginary |
| $\mathbb{M}_+$ | $\Phi(\tilde Q)^{\dagger} = \Phi(\tilde Q)$ | $\rho_L(\tilde Q)^{\dagger} = \rho_L(\tilde Q)$ |
| $\mathbb{M}_-$ | $\Phi(\tilde Q)^{\dagger} = -\Phi(\tilde Q)$ | $\rho_L(\tilde Q)^{\dagger} = -\rho_L(\tilde Q)$ |

with $\epsilon = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ and $\dagger$ the conjugate transpose. The middle two rows differ in appearance because the four entries of the $2 \times 2$ matrix are four $\mathbb{C}$-linear combinations of the four coefficients, so realness of the coefficients is not realness of the entries, while the entries of the $4 \times 4$ matrix are the coefficients up to sign.

The two models differ in exactly one structural way, and it is visible in their two invariants. Writing $\tilde Q = Q_0e_0 + \mathbf{Q}$ with vector part $\mathbf{Q}$,

$$
\operatorname{Tr}\Phi(\tilde Q) = 2Q_0, \quad \det\Phi(\tilde Q) = N(\tilde Q), \qquad
\operatorname{Tr}\rho_L(\tilde Q) = 4Q_0, \quad \det\rho_L(\tilde Q) = N(\tilde Q)^2 .
$$

The trace is the scalar part times the size of the matrix in both models, and the determinant of the $2 \times 2$ model is the biquaternion norm itself, while the determinant of the regular model is its square; the square root of the regular determinant, with the sign taken from the $2 \times 2$ one, is the norm. The factor two in the trace and the square in the determinant have the same source: the regular matrix is **block diagonal with two blocks, each a copy of the $2 \times 2$ matrix of the same element**, in the basis adapted to the two minimal left ideals. That is the content of the next section.

## The Two Models

**Definition.** The **matrix realization** $\Phi$ is determined on the basis by

$$
\Phi(e_0) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad
\Phi(e_1) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}, \quad
\Phi(e_2) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \quad
\Phi(e_3) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix},
$$

and on the central scalar by $\Phi(ie_\mu) = i\Phi(e_\mu)$, so that on a general element

$$
\Phi(\tilde Q) = \begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3 \end{pmatrix}.
$$

**Definition.** The **regular realization** $\rho_L$ is the matrix of left multiplication, $\tilde R \mapsto \tilde Q\tilde R$, in the basis $e_0, e_1, e_2, e_3$,

$$
\rho_L(\tilde Q) = \begin{pmatrix}
Q_0 & -Q_1 & -Q_2 & -Q_3 \\
Q_1 & Q_0 & -Q_3 & Q_2 \\
Q_2 & Q_3 & Q_0 & -Q_1 \\
Q_3 & -Q_2 & Q_1 & Q_0
\end{pmatrix},
$$

whose first column is the four-vector $(Q_0, Q_1, Q_2, Q_3)$ of $\tilde Q$; $\rho_L$ is injective for that reason. Each model is treated in its own article, where the multiplicativity, the invariants and the module theory are proved; the formulas above are quoted from there.

**Remark (the images of the vector units).** The two models present the three vector units differently, and the difference is what makes the two Hermitian subspaces matrix-visible in both. In the $2 \times 2$ model $\Phi(e_k) = -i\sigma_k$, where $\sigma_1, \sigma_2, \sigma_3$ are the three Pauli matrices, so each vector unit's image is $-i$ times a Hermitian matrix; in the regular model $\rho_L(e_k)$ is real and skew-symmetric, so each vector unit's image is real skew, and $i$ times it is Hermitian. In both cases

$$
\Phi(\tilde Q) = Q_0 I_2 + \sum_k Q_k\Phi(e_k), \qquad
\rho_L(\tilde Q) = Q_0 I_4 + \sum_k Q_k\rho_L(e_k),
$$

so a Hermitian element, whose scalar part is real and whose vector coefficients are purely imaginary, has a Hermitian image in both models, and an anti-Hermitian element has an anti-Hermitian image in both.

**Theorem (the regular matrix is two copies of the $2 \times 2$ matrix).** Let $\tilde\Pi = \tfrac{1}{2}(e_0 + ie_1)$ and $f = e_0 - \tilde\Pi$, so that $\mathbb{B} = \mathbb{B}\tilde\Pi \oplus \mathbb{B}f$ is the splitting of the algebra into two minimal left ideals of *The Six Subspaces and the Structure*. In the basis $\tilde\Pi, \tilde R, f, \tilde T$ of $\mathbb{B}$, where $\tilde R = e_3 + ie_2$ spans the nilpotent line of $\mathbb{B}\tilde\Pi$ and $\tilde T = e_3 - ie_2$ that of $\mathbb{B}f$, the regular matrix is block diagonal,

$$
\rho_L(\tilde Q) = \begin{pmatrix} \Phi(\tilde Q) & 0 \\ 0 & \Phi(\tilde Q) \end{pmatrix}
\qquad \text{up to conjugation in each block,}
$$

and each block has trace $2Q_0$ and determinant $N(\tilde Q)$.

**Proof.** Both summands of $\mathbb{B} = \mathbb{B}\tilde\Pi \oplus \mathbb{B}f$ are left ideals, so left multiplication by $\tilde Q$ preserves each of them and the matrix is block diagonal in a basis adapted to the splitting. Each block is the matrix of left multiplication by $\tilde Q$ on a minimal left ideal, and every minimal left ideal is isomorphic to the simple module $V = \mathbb{C}^2$ as a left $\mathbb{B}$-module, on which left multiplication is exactly $\Phi(\tilde Q)$; a change of basis inside the block replaces it by a conjugate matrix, which has the same trace and determinant. $\square$

**Corollary.** The two invariants of the regular model are the doubled trace and the squared determinant of the model of the simple module, $\operatorname{Tr}\rho_L(\tilde Q) = 2\operatorname{Tr}\Phi(\tilde Q)$ and $\det\rho_L(\tilde Q) = \det\Phi(\tilde Q)^2$.

**Proof.** The trace and the determinant of a block diagonal matrix are the sum and the product of those of the blocks.

## The Centre Subspace

A central element is $\tilde Q = Ae_0$ with $A \in \mathbb{C}$, and its two images are the scalar matrices

$$
\Phi(Ae_0) = A I_2, \qquad \rho_L(Ae_0) = A I_4 ,
$$

which follows from the definitions and from $e_0$ being the identity. The invariants are $\operatorname{Tr} = 2A$ and $\det = A^2$ in the first model, $\operatorname{Tr} = 4A$ and $\det = A^4$ in the second: the scalar is what both models detect in the centre, and the powers are the sizes. The image of the centre is the centre of the matrix algebra in the $2 \times 2$ case, the scalar matrices being exactly the matrices commuting with every matrix, which is the standard form of Schur's lemma quoted in *Biquaternion 2×2 Matrix Element Representation*.

The centre is the only one of the six whose image in each model is a **set of scalar matrices**, and this is the same statement as the centre being the set of elements commuting with every element. It is also the only one of the six on which a model's determinant is a square of a scalar: $\det\Phi(Ae_0) = A^2$ and $\det\rho_L(Ae_0) = A^4$ vanish exactly at $A = 0$, so the centre contains no singular matrix other than the zero matrix in either model.

## The Vector Subspace

A pure element is $\tilde Q = \mathbf{P} = \sum_k P_ke_k$, whose scalar part vanishes, so both traces vanish and the images are the traceless matrices,

$$
\operatorname{Tr}\Phi(\mathbf{P}) = 0, \qquad \operatorname{Tr}\rho_L(\mathbf{P}) = 0 ,
$$

and conversely an element whose image is traceless has vanishing scalar part, in either model, because the trace is twice or four times the scalar part. **The trace of either model separates the centre from the vector subspace and nothing else**: the scalar part is the only coefficient it sees.

The determinants are $\det\Phi(\mathbf{P}) = N(\mathbf{P})$ and $\det\rho_L(\mathbf{P}) = N(\mathbf{P})^2$, so the null elements of the vector subspace, which are its zero divisors, are exactly the singular matrices of the image in either model, and the nilpotents, whose norm has a double zero, are the matrices of rank one in the $2 \times 2$ model, as recorded in *Biquaternion 2×2 Matrix Element Representation*.

The image of the vector subspace under $\Phi$ is the traceless matrices, that is $\mathrm{SL}(2,\mathbb{C})$ as a Lie algebra, and its real form is the image of the real vector triple; both are recorded in *Biquaternion 2×2 Matrix Element Representation*. The commutator of two traceless matrices is traceless, and the corresponding closedness of the vector subspace under the commutator is *The Six Subspaces and the Four Complex Products*.

## The Quaternion Subspace

A real quaternion is $\tilde Q = h = h_0e_0 + h_1e_1 + h_2e_2 + h_3e_3$ with real coefficients $h_\mu$, and its two images are

$$
\Phi(h) = \begin{pmatrix} h_0 - ih_3 & -ih_1 - h_2 \\ -ih_1 + h_2 & h_0 + ih_3 \end{pmatrix},
\qquad
\rho_L(h) = \begin{pmatrix}
h_0 & -h_1 & -h_2 & -h_3 \\
h_1 & h_0 & -h_3 & h_2 \\
h_2 & h_3 & h_0 & -h_1 \\
h_3 & -h_2 & h_1 & h_0
\end{pmatrix},
$$

so that **in the regular model the image is exactly the real matrices, and the quaternion subspace is the real part of the regular representation**. In the $2 \times 2$ model the entries involve $i$, and the correct condition is the one of the table: $\Phi(h)$ is fixed by $M \mapsto \epsilon\overline{M}\epsilon^{-1}$, that is $M_{22} = \overline{M_{11}}$ and $M_{21} = -\overline{M_{12}}$.

The regular image is more than real: it is $h_0 I_4 + \sum_k h_k\rho_L(e_k)$, a real scalar matrix plus a real-linear combination of the three real skew matrices $\rho_L(e_k)$, which is the matrix form of the quaternion relations. The invariants are $\operatorname{Tr} = 2h_0$ and $\det = N(h) > 0$ in the $2 \times 2$ model, $\operatorname{Tr} = 4h_0$ and $\det = N(h)^2 > 0$ in the regular model, so that in both models the quaternion subspace is a set of matrices of strictly positive determinant: **it is the largest of the six whose images contain no singular matrix**, which is the matrix statement of its being a division algebra, and the same as the absence of zero divisors there in *The Six Subspaces and the Elements*.

## The Anti-Quaternion Subspace

An element of $i\mathbb{H}_{\mathbb{B}}$ is $\tilde Q = ih$ with $h$ a real quaternion, and its images are $i$ times those of $h$: in the regular model the image is exactly the purely imaginary matrices, and in the $2 \times 2$ model the anti-fixed matrices of $M \mapsto \epsilon\overline{M}\epsilon^{-1}$,

$$
M_{22} = -\overline{M_{11}}, \qquad M_{21} = \overline{M_{12}} .
$$

The invariants are $\operatorname{Tr} = 2ih_0$ and $\det = N(h_\mu i) = -N(h) < 0$ in the $2 \times 2$ model, and $\operatorname{Tr} = 4ih_0$ and $\det = N(h)^2 > 0$ in the regular model.

The last two formulas are the sharpest single difference between the two models on the six. The $2 \times 2$ determinant is $N$, so it is **strictly negative** on the anti-quaternion subspace and detects the sign; the regular determinant is $N^2$, so it is strictly positive there and loses the sign. Only the $2 \times 2$ model sees that the anti-quaternion subspace is the negative-definite half of the coefficient space; the regular model sees that its image there is a set of matrices of positive determinant, which is all it can see.

## The Hermitian Subspace

A Hermitian element is $\tilde Q = a_0e_0 + i\mathbf{p}$ with $a_0$ real and $\mathbf{p}$ a real vector. Its scalar part is real and its vector coefficients are purely imaginary, so by the remark of §*The Two Models* both images are Hermitian matrices,

$$
\Phi(\tilde Q)^{\dagger} = \Phi(\tilde Q), \qquad \rho_L(\tilde Q)^{\dagger} = \rho_L(\tilde Q),
$$

and conversely an element with Hermitian image has real scalar part and purely imaginary vector coefficients, in either model. So **the Hermitian subspace is the fixed space of the conjugate transpose in both models**, which the other three conjugations of the algebra are not: realness of the coefficients is an entry condition in the regular model only, and the two quaternion conjugations are never entry conditions.

The invariants are $\operatorname{Tr} = 2a_0$ and $\det = N(\tilde Q) \in \mathbb{R}$ in the $2 \times 2$ model, $\operatorname{Tr} = 4a_0$ and $\det = N(\tilde Q)^2 \geq 0$ in the regular model. The determinant is real in both, so a Hermitian element is a zero divisor exactly when its image is singular, and the image is singular for exactly the null Hermitian elements of *The Six Subspaces and the Elements*; those are the real multiples of the Hermitian idempotents, which are the rank-one Hermitian matrices of the $2 \times 2$ model, as recorded in the house article.

## The Anti-Hermitian Subspace

An anti-Hermitian element is $\tilde Q = ib_0e_0 + \mathbf{q}$ with $b_0$ real and $\mathbf{q}$ a real vector, and its images are anti-Hermitian,

$$
\Phi(\tilde Q)^{\dagger} = -\Phi(\tilde Q), \qquad \rho_L(\tilde Q)^{\dagger} = -\rho_L(\tilde Q),
$$

the imaginary scalar part and the real vector part being the two conditions for this. The invariants are $\operatorname{Tr} = 2ib_0$ and $\det = N(\tilde Q) \in \mathbb{R}$ in the $2 \times 2$ model, $\operatorname{Tr} = 4ib_0$ and $\det = N(\tilde Q)^2 \geq 0$ in the regular model.

The two Hermitian subspaces are mirror images in the matrix models, and the mirror is the dagger: the images of $\mathbb{M}_+$ are the Hermitian matrices and those of $\mathbb{M}_-$ the anti-Hermitian ones, in both models, and $i\mathbb{M}_+ = \mathbb{M}_-$ in the algebra corresponds to $i$ times a Hermitian matrix being anti-Hermitian. In the regular model the images of the two are distinguished by the trace, $4a_0$ real against $4ib_0$ purely imaginary, and by nothing else, since the determinant is $N^2 \geq 0$ for both.

## Summary

The algebra has two basic matrix models, the irreducible $2 \times 2$ model of the simple module and the reducible $4 \times 4$ regular model of left multiplication, and the six distinguished subspaces have the same six descriptions in both: the scalars, the traceless matrices, the matrices of the real coefficients, those of the purely imaginary coefficients, the Hermitian matrices and the anti-Hermitian matrices, the middle two reading as a conjugate-reflection condition in the $2 \times 2$ model because its entries are linear combinations of the coefficients and as realness or pure imaginaryness in the regular model because its entries are the coefficients up to sign. The invariants are $\operatorname{Tr}\Phi(\tilde Q) = 2Q_0$ with $\det\Phi(\tilde Q) = N(\tilde Q)$, and $\operatorname{Tr}\rho_L(\tilde Q) = 4Q_0$ with $\det\rho_L(\tilde Q) = N(\tilde Q)^2$; the trace is the scalar part times the size, so it separates the centre from the vector subspace in both models and sees nothing else, and the determinant of the $2 \times 2$ model is the norm itself while that of the regular model is its square. The factor two and the square are the same phenomenon: in the basis adapted to the two minimal left ideals the regular matrix is block diagonal with two blocks, each a copy of the $2 \times 2$ matrix of the same element, and each minimal left ideal is a copy of the simple module. The quaternion subspace is the real matrices in the regular model and the fixed space of the conjugate-reflection in the $2 \times 2$ model, and it is the only one of the six whose images have strictly positive determinant in both; the anti-quaternion subspace is where the $2 \times 2$ determinant is strictly negative and the regular determinant is not, which is the one place where the two models see different signs. The models themselves, their multiplicativity, their module theory and their standard names are the business of *Biquaternion 2×2 Matrix Element Representation* and *Biquaternion 4×4 Regular Matrix Element Representation*; what is added here is the restriction to the six and the bridge between the two.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $\Phi$ | the $2 \times 2$ matrix realization, the model of the simple module |
| $\rho_L$ | the $4 \times 4$ regular realization of left multiplication |
| $N$ | the biquaternion norm, $\det\Phi$ |
| $\epsilon$ | $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, the matrix of the conjugate-reflection |
| $\tilde\Pi, f$ | the Hermitian idempotent $\tfrac{1}{2}(e_0 + ie_1)$ and its complement |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section
- *Biquaternion 2×2 Matrix Element Representation* (`articles_maths/biquaternion-2x2-matrix-element-representation.md`), for the model $\Phi$, its invariants, its module and its own table of the six in matrix form
- *Biquaternion 4×4 Regular Matrix Element Representation* (`articles_maths/biquaternion-4x4-regular-matrix-element-representation.md`), for the model $\rho_L$, its left and right operators, the module structure and the double centralizer
- *The Six Subspaces and the Structure* (`articles_maths/the-six-subspaces-and-the-structure.md`), for the two minimal left ideals whose basis makes the regular matrix block diagonal
- *The Six Subspaces and the Elements* (`articles_maths/the-six-subspaces-and-the-elements.md`), for the null elements, which are the singular matrices of the images
- *The Six Subspaces and the Norms* (`articles_maths/the-six-subspaces-and-the-norms.md`), for the pairings that the trace and the determinant polarise
