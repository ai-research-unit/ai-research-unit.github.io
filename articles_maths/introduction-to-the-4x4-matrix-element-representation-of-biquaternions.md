# __Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ and its four-vector coordinates are those of *The Biquaternion Algebra and Its Vector Spaces* and *The Four-Vector Element Representation of Biquaternions*.

Two $4\times4$ matrices carry the multiplication of $\mathbb{B}$ in the basis $e_t, \vec e_x, \vec e_y, \vec e_z$. The **left regular matrix** $\mathsf{M}_4^{L}(\tilde Q)$ is the matrix whose $\mu$-th column is the coordinate column of the product $\tilde Q e_\mu$; the **right regular matrix** $\mathsf{M}_4^{R}(\tilde Q)$ is the matrix whose $\mu$-th column is the coordinate column of the product $e_\mu \tilde Q$. Both are complex $4\times4$ matrices, both carry a letter, and neither is the default: the shorter notation $\mathsf{M}_4$ stands for the left one $\mathsf{M}_4^{L}$, and the letter $L$ is kept here so that the two stand on the same footing.

The **left regular matrix** $\mathsf{M}_4^{L}(\tilde Q)$ in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, its multiplicativity and injectivity, the trace $\operatorname{Tr}\mathsf{M}_4^{L}(\tilde Q)=4Q_t$ and the determinant $\det\mathsf{M}_4^{L}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^2$, and the remarkable subspaces in the regular model are stated below, in §*The Left and the Right Regular Matrices*, §*Remarkable Subspaces in the Regular Model* and §*The Two Models Compared*.

The image of the left regular matrix is written $M_4(\mathbb{C})_L$: it is the subspace of $M_4(\mathbb{C})$ of the matrices $\mathsf{M}_4^{L}(\tilde Q)$, of complex dimension $4$ inside the $16$ of $M_4(\mathbb{C})$, and it is the object of this article.

The article owns the left regular matrix and its invariants, the right regular matrix and the relation between the two matrices, the module structure and the decomposition $\mathbb{B}=I_1\oplus I_2\cong V\oplus V$, the double centralizer, the $8\times8$ real form, the sandwich read in the regular basis, and a second $4\times4$ realization with the sixteen products of the biparavectors. It is the first reducible realization met in this subcategory. Two further sections read the product and the form in the regular model: §*The General Plain Bilinear Form in the Regular Model*, for the trace pairing, its Gram matrix, its isotropic cone and its automorphism group, and §*The Four Words and the Four Traces in the Regular Model*, for the four products as four words in the regular matrix and its transpose and dagger and for the four forms as four traces. It does not treat the eigenvalues, the Cayley–Hamilton identity or the eigenspace dimensions of the regular matrix, which belong to *Biquaternion Spectral Theory*; and it does not treat the idempotents and the Peirce decomposition, which belong to *Idempotents of the Biquaternion Algebra* and *Ideals and Peirce Decompositions of the Biquaternion Algebra*, except to cite the idempotents that split the algebra into its two minimal left ideals. No physical vocabulary is used: the two-sided action of the group of elements of $N=1$ on the Hermitian subspace is a statement of algebra, not a spinor, a chirality or a handedness of a physical particle.

One comparative item is added beyond the representation itself: a second $4 \times 4$ realization of $\mathbb{B}$ taken from the literature on eigenvector bundles, recorded with the multiplicative quadratic map it carries, because it is the natural contrast with both the regular realization and the congruence-shaped quadratic map of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*.

## The Left and the Right Regular Matrices

**Definition (the left regular matrix).** The **left regular matrix** is the isomorphism written $\mathsf{M}_4^{L}$. It converts a biquaternion into a $4 \times 4$ complex matrix,

$$
\mathsf{M}_4^{L} : \mathbb{B} \longrightarrow M_4(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity. In the basis $e_t, \vec e_x, \vec e_y, \vec e_z$, the $\mu$-th column of $\mathsf{M}_4^{L}(\tilde Q)$ is the coordinate column of $\tilde Q e_\mu$:

$$
\boxed{\; \mathsf{M}_4^{L}(\tilde{Q}) = \begin{pmatrix}
Q_t & -Q_x & -Q_y & -Q_z \\
Q_x & Q_t & -Q_z & Q_y \\
Q_y & Q_z & Q_t & -Q_x \\
Q_z & -Q_y & Q_x & Q_t
\end{pmatrix} \;}.
$$

This is the Cayley matrix of the left multiplication, written $\mathsf{M}_4(\tilde Q)$ in the shorter notation; every entry is a single coefficient of $\tilde Q$ with a sign, and no entry is a sum of two or more coefficients.

**Example.** For $\tilde{Q}=(2+i)e_t+(1-i)\vec e_x+3\vec e_y+i\vec e_z$ the regular matrix is

$$
\mathsf{M}_4(\tilde{Q})=\begin{pmatrix}
2+i&-1+i&-3&-i\\
1-i&2+i&-i&3\\
3&i&2+i&-1+i\\
i&-3&1-i&2+i
\end{pmatrix}.
$$

The column of $\tilde Q_4=e_t+\vec e_x$, namely $R=(1,1,0,0)$, is carried to the column $(1+2i,3,3+i,-3+i)$, which is the four-vector of the product $\tilde{Q}\tilde Q_4$ computed by the component formula of *The Four-Vector Element Representation of Biquaternions*. Its biquaternion norm, the determinant of the $2\times2$ matrix of the same element, is $11+2i$, so the regular determinant is $(11+2i)^2=117+44i$ and the trace is $4(2+i)=8+4i$.

**Theorem (the left regular matrix is an injective algebra homomorphism).** For all $\tilde Q_1, \tilde Q_2 \in \mathbb{B}$,

$$
\boxed{\; \mathsf{M}_4^{L}(\tilde Q_1)\,\mathsf{M}_4^{L}(\tilde Q_2) = \mathsf{M}_4^{L}(\tilde Q_1\tilde Q_2), \qquad \mathsf{M}_4^{L}(\tilde Q_2) = 0 \iff \tilde Q_2 = 0 \;},
$$

so the assignment is an injective algebra homomorphism, of complex dimension $4$, and the coefficient space is a left $\mathbb{B}$-module under it.

**Proof.** The multiplicativity is read on the basis: for every $\mu$, associativity gives $\tilde Q_1(\tilde Q_2 e_\mu)=(\tilde Q_1\tilde Q_2)e_\mu$, so the two matrices agree on every column $\operatorname{col}(e_\mu)$ and hence everywhere. The injectivity follows from the first column, which is the column of $\tilde Q_2$ and alone recovers the four coefficients.

The two orders differ, and the example $\tilde Q=e_t+\vec e_x$, $\tilde Q_4=e_t+\vec e_y$ shows it: the products $\tilde Q\tilde Q_4=e_t+\vec e_x+\vec e_y+\vec e_z$ and $\tilde Q_4\tilde Q=e_t+\vec e_x+\vec e_y-\vec e_z$ have first columns $(1,1,1,1)$ and $(1,1,1,-1)$, so $\mathsf{M}_4(\tilde Q)\mathsf{M}_4(\tilde Q_4)\neq\mathsf{M}_4(\tilde Q_4)\mathsf{M}_4(\tilde Q)$, exactly as $\tilde Q\tilde Q_4\neq\tilde Q_4\tilde Q$.

**Definition (the right regular matrix).** The **right regular matrix** is the assignment written $\mathsf{M}_4^{R}$. It converts a biquaternion into a $4 \times 4$ complex matrix,

$$
\mathsf{M}_4^{R} : \mathbb{B} \longrightarrow M_4(\mathbb{C}),
$$

also fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity. In the same basis, the $\mu$-th column of $\mathsf{M}_4^{R}(\tilde Q)$ is the coordinate column of $e_\mu \tilde Q$:

$$
\mathsf{M}_4^{R}(\tilde{Q}) = \begin{pmatrix}
Q_t & -Q_x & -Q_y & -Q_z \\
Q_x & Q_t & Q_z & -Q_y \\
Q_y & -Q_z & Q_t & Q_x \\
Q_z & Q_y & -Q_x & Q_t
\end{pmatrix}.
$$

**Proposition (the right regular matrix).** The columns are the images $e_\mu \tilde{Q}$, and one expands as in the left case above with the factors in the opposite order. Alternatively, since each $e_\mu$ is either $e_t$ or one of the $\vec e_\lambda$, and $\vec e_\lambda \vec e_\nu = -\vec e_\nu \vec e_\lambda$ for $\nu \neq \lambda$, the matrix is the transpose of the left matrix conjugated by the fixed sign matrix of the next section, $\mathsf{M}_4^{R}(\tilde{Q}) = D\,\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf T}D$, and direct computation of the four general products confirms the display.

**Theorem (the right regular matrix is anti-multiplicative).** For all $\tilde Q_1, \tilde Q_2 \in \mathbb{B}$,

$$
\mathsf{M}_4^{R}(\tilde Q_1)\,\mathsf{M}_4^{R}(\tilde Q_2) = \mathsf{M}_4^{R}(\tilde Q_2\tilde Q_1).
$$

Hence the right regular matrix is an algebra **anti**-homomorphism, and its image is the regular representation of the opposite algebra $\mathbb{B}^{\mathrm{opp}}$, not a second representation of $\mathbb{B}$.

**Proof.** Write $\operatorname{col}(\tilde Q_5)$ for the coordinate column of $\tilde Q_5$. The defining property of the right matrix is $\mathsf{M}_4^{R}(\tilde Q_1)\operatorname{col}(\tilde Q_5) = \operatorname{col}(\tilde Q_5\tilde Q_1)$, because the $\mu$-th column of $\mathsf{M}_4^{R}(\tilde Q_1)$ is $\operatorname{col}(e_\mu\tilde Q_1)$ and a column is a linear combination of the $e_\mu$. Hence, for each $\mu$,

$$
\mathsf{M}_4^{R}(\tilde Q_1)\,\mathsf{M}_4^{R}(\tilde Q_2)\operatorname{col}(e_\mu) = \mathsf{M}_4^{R}(\tilde Q_1)\operatorname{col}(e_\mu\tilde Q_2) = \operatorname{col}\bigl((e_\mu\tilde Q_2)\tilde Q_1\bigr) = \operatorname{col}\bigl(e_\mu(\tilde Q_2\tilde Q_1)\bigr) = \mathsf{M}_4^{R}(\tilde Q_2\tilde Q_1)\operatorname{col}(e_\mu),
$$

the third step being associativity. The two matrices therefore agree on the four columns $\operatorname{col}(e_\mu)$, which are the standard basis of $\mathbb{C}^4$, so they are equal. An anti-homomorphism is by definition a homomorphism from the opposite algebra, and the underlying linear assignment is the same.

**Remark (which side is which).** The two matrices are the two ways a non-commutative algebra multiplies its own basis. The left matrix is multiplicative and the right matrix anti-multiplicative. Since quaternion conjugation is an anti-automorphism, the matrix $\mathsf{M}_4^{L}(\tilde{Q}^{\natural})$ depends anti-multiplicatively on $\tilde Q$; it is therefore the right regular matrix up to a fixed change of basis, and §*Transposition and the Two Matrices* identifies that change of basis and shows that it is not the identity. The two matrices differ as soon as the algebra is non-commutative.

## Remarkable Subspaces in the Regular Model

The remarkable subspaces have the following images under $\mathsf{M}_4$, read from the matrix. Each row records the image of the subspace.

| Subspace | Image under $\mathsf{M}_4$ | Description |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\{A I_4:A\in\mathbb{C}\}$ | the scalar matrices |
| $\mathrm{Vect}(\mathbb{B})$ | $\{M:\operatorname{Tr}M=0\}$ | the traceless matrices |
| $\mathbb{H}_{\mathbb{B}}$ | the real matrices | the quaternion subspace is the real part of the realization |
| $i\mathbb{H}_{\mathbb{B}}$ | the purely imaginary matrices | $i$ times the real matrices |
| $\mathbb{M}_+$ | $\{M:M=M^\dagger\}$ | the Hermitian matrices |
| $\mathbb{M}_-$ | $\{M:M=-M^\dagger\}$ | the anti-Hermitian matrices |

Here $\dagger$ is the conjugate transpose, and a matrix is Hermitian or anti-Hermitian in the ordinary sense.

**Proof.** A central element is $\tilde Q=Ae_t$, and $\mathsf{M}_4(Ae_t)=AI_4$ because $e_t$ is the identity. The trace of the matrix is $4Q_t$, so the traceless matrices are exactly the elements with vanishing scalar part, that is the vector subspace. For the quaternion subspace the coefficients $Q_\mu=h_\mu$ are real, and each entry of the matrix is a single coefficient up to sign, so the image is the set of real matrices; the anti-quaternion subspace, whose coefficients are purely imaginary, is its $i$-multiple, the purely imaginary matrices. Finally $\mathsf{M}_4(\vec e_\lambda)$ is real and skew-symmetric, so for a Hermitian element, whose scalar part is real and whose vector coefficients are purely imaginary, the image $q_tI_4+\sum_\lambda iq'_\lambda\mathsf{M}_4(\vec e_\lambda)$ is a real scalar matrix plus a purely imaginary skew matrix, which is Hermitian; the anti-Hermitian element gives the negative pattern.

The table is the matrix reading of the linear-spaces picture, and it is visibly different from the $2\times2$ one: in the regular model the quaternion and anti-quaternion subspaces are the real and the purely imaginary matrices, an entrywise condition, whereas in the $2\times2$ model the same two subspaces are the $\epsilon$-conjugation pattern and its $i$-multiple. The two models agree on the centre, the vector subspace and the two Hermitian subspaces.

### Explicit Patterns and Invariants

Read from the matrix above, each of the remarkable subspaces has a fixed pattern. With $Q_\mu=q_\mu+iq'_\mu$,

**The centre.** For $\tilde Q=Q_te_t$ the matrix is scalar,

$$
\mathsf{M}_4(Q_te_t)=\begin{pmatrix}Q_t&0&0&0\\0&Q_t&0&0\\0&0&Q_t&0\\0&0&0&Q_t\end{pmatrix}=Q_tI_4,\qquad \operatorname{Tr}=4Q_t,\quad \det=Q_t^4 .
$$

**The vector subspace.** For $\tilde Q=\vec P=P_x\vec e_x+P_y\vec e_y+P_z\vec e_z$ the matrix is traceless,

$$
\mathsf{M}_4(\vec P)=\begin{pmatrix}0&-P_x&-P_y&-P_z\\P_x&0&-P_z&P_y\\P_y&P_z&0&-P_x\\P_z&-P_y&P_x&0\end{pmatrix},\qquad \operatorname{Tr}=0,\quad \det=\bigl(P_x^2+P_y^2+P_z^2\bigr)^2 .
$$

**The quaternion subspace.** For $\tilde Q=h=h_te_t+h_x\vec e_x+h_y\vec e_y+h_z\vec e_z$ with $h_\mu\in\mathbb{R}$ the matrix is real,

$$
\mathsf{M}_4(h)=\begin{pmatrix}h_t&-h_x&-h_y&-h_z\\h_x&h_t&-h_z&h_y\\h_y&h_z&h_t&-h_x\\h_z&-h_y&h_x&h_t\end{pmatrix},\qquad \operatorname{Tr}=4h_t,\quad \det=\bigl(h_t^2+h_x^2+h_y^2+h_z^2\bigr)^2>0 .
$$

**The anti-quaternion subspace.** For $\tilde Q=ih$ with $h$ real the matrix is $i$ times the preceding one, and purely imaginary,

$$
\mathsf{M}_4(ih)=i\,\mathsf{M}_4(h)=\begin{pmatrix}ih_t&-ih_x&-ih_y&-ih_z\\ih_x&ih_t&-ih_z&ih_y\\ih_y&ih_z&ih_t&-ih_x\\ih_z&-ih_y&ih_x&ih_t\end{pmatrix},\qquad \operatorname{Tr}=4ih_t,\quad \det=\bigl(h_t^2+h_x^2+h_y^2+h_z^2\bigr)^2>0 .
$$

**The Hermitian subspace.** For $\tilde Q=a_te_t+i\vec p$ with $a_t$ real and $\vec p$ a real vector the matrix is Hermitian,

$$
\mathsf{M}_4(\tilde Q)=\begin{pmatrix}a_t&-ip_x&-ip_y&-ip_z\\ip_x&a_t&-ip_z&ip_y\\ip_y&ip_z&a_t&-ip_x\\ip_z&-ip_y&ip_x&a_t\end{pmatrix}=\mathsf{M}_4(\tilde Q)^\dagger,\qquad \operatorname{Tr}=4a_t,\quad \det=\bigl(a_t^2-p_x^2-p_y^2-p_z^2\bigr)^2 .
$$

**The anti-Hermitian subspace.** For $\tilde Q=ib_te_t+\vec q$ with $b_t$ real and $\vec q$ a real vector the matrix is anti-Hermitian,

$$
\mathsf{M}_4(\tilde Q)=\begin{pmatrix}ib_t&-q_x&-q_y&-q_z\\q_x&ib_t&-q_z&q_y\\q_y&q_z&ib_t&-q_x\\q_z&-q_y&q_x&ib_t\end{pmatrix}=-\mathsf{M}_4(\tilde Q)^\dagger,\qquad \operatorname{Tr}=4ib_t,\quad \det=\bigl(q_x^2+q_y^2+q_z^2-b_t^2\bigr)^2 .
$$

The trace is the scalar part times four in every case, so it separates the centre from the vector subspace and sees nothing else. The determinant is the square of the $2\times2$ determinant of the same element in every case; on the quaternion subspace that $2\times2$ determinant is a sum of four real squares, strictly positive, so no element there is singular, and on the anti-quaternion subspace it is the negative of that sum, strictly negative, so it is the $2\times2$ model and not the regular one that sees the sign the subspace carries, the regular square being positive in both cases. The two models are set side by side in the next section.

## The Two Models Compared

The $2\times2$ realization $\mathsf{M}_2$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* and the regular realization $\mathsf{M}_4$ above are the two basic matrix models of $\mathbb{B}$. Both are injective and multiplicative, so both see the remarkable subspaces, and the same six matrix conditions describe them in both; the invariant columns give, first, the value in the $2\times2$ model and, second, the value in the regular model. Here $\Delta=\Delta(\tilde Q)=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ is the determinant of the $2\times2$ matrix, a sum of four real squares on the quaternion subspace, the negative of that sum on the anti-quaternion subspace, and real on the two Hermitian subspaces.

| Subspace | Condition in the $2\times2$ model | Condition in the $4\times4$ model | $\operatorname{Tr}\mathsf{M}_2$ / $\operatorname{Tr}\mathsf{M}_4$ | $\det\mathsf{M}_2$ / $\det\mathsf{M}_4$ |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\mathsf{M}_2(\tilde Q)=AI_2$ | $\mathsf{M}_4(\tilde Q)=AI_4$ | $2A$ / $4A$ | $A^2$ / $A^4$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\operatorname{Tr}\mathsf{M}_2(\tilde Q)=0$ | $\operatorname{Tr}\mathsf{M}_4(\tilde Q)=0$ | $0$ / $0$ | $\Delta$ / $\Delta^2$ |
| $\mathbb{H}_{\mathbb{B}}$ | fixed by $M\mapsto\epsilon\overline M\epsilon^{-1}$ | the real matrices | $2h_t$ / $4h_t$ | $\Delta>0$ / $\Delta^2$ |
| $i\mathbb{H}_{\mathbb{B}}$ | anti-fixed by the same map | the purely imaginary matrices | $2ih_t$ / $4ih_t$ | $\Delta<0$ / $\Delta^2$ |
| $\mathbb{M}_+$ | $\mathsf{M}_2(\tilde Q)^\dagger=\mathsf{M}_2(\tilde Q)$ | $\mathsf{M}_4(\tilde Q)^\dagger=\mathsf{M}_4(\tilde Q)$ | $2a_t$ / $4a_t$ | $\Delta$ real / $\Delta^2$ |
| $\mathbb{M}_-$ | $\mathsf{M}_2(\tilde Q)^\dagger=-\mathsf{M}_2(\tilde Q)$ | $\mathsf{M}_4(\tilde Q)^\dagger=-\mathsf{M}_4(\tilde Q)$ | $2ib_t$ / $4ib_t$ | $\Delta$ real / $\Delta^2$ |

Here $\epsilon=i\sigma_2$, and the two middle rows are the only ones that look different: the four entries of the $2\times2$ matrix are four $\mathbb{C}$-linear combinations of the four coefficients, so realness of the coefficients is not realness of the entries, whereas the entries of the regular matrix are the coefficients up to sign.

**Theorem (the regular matrix is two copies of the $2\times2$ matrix).** Let $\tilde\Pi=\tfrac12(e_t+i\vec e_x)$ and $f=e_t-\tilde\Pi$, so that $\mathbb{B}=\mathbb{B}\tilde\Pi\oplus\mathbb{B}f$ splits into two minimal left ideals, and let $\tilde Q_4=\vec e_z+i\vec e_y$, $\tilde Q_7=\vec e_z-i\vec e_y$. In the basis $\tilde\Pi,\tilde Q_4,f,\tilde Q_7$ the regular matrix is block diagonal,

$$
\mathsf{M}_4(\tilde Q)=\begin{pmatrix}A_+&0\\0&A_-\end{pmatrix},\qquad A_+\text{ and }A_-\text{ conjugate to }\mathsf{M}_2(\tilde Q),
$$

and each block has trace $2Q_t$ and determinant $\Delta(\tilde Q)$.

**Proof.** Left multiplication preserves each left ideal, so the matrix is block diagonal in a basis adapted to the splitting. Each block is left multiplication by $\tilde Q$ on a minimal left ideal, every minimal left ideal is isomorphic to the simple module $V=\mathbb{C}^2$, and on $V$ left multiplication is $\mathsf{M}_2(\tilde Q)$; a change of basis inside the block replaces it by a conjugate matrix, which has the same trace and determinant.

**Corollary.** $\operatorname{Tr}\mathsf{M}_4(\tilde Q)=2\operatorname{Tr}\mathsf{M}_2(\tilde Q)=4Q_t$ and $\det\mathsf{M}_4(\tilde Q)=\det\mathsf{M}_2(\tilde Q)^2$: the factor two in the trace and the square in the determinant are one block decomposition and not two coincidences. In both models the trace is the scalar part times the size of the matrix, so it separates the centre from the vector subspace and sees nothing else.

**Remark (the one place the two models see different signs).** The $2\times2$ determinant is $\Delta$ and the regular determinant is $\Delta^2$. On the anti-quaternion subspace the first is $-(h_t^2+h_x^2+h_y^2+h_z^2)<0$ and the second is positive, so the $2\times2$ model sees that $i\mathbb{H}_{\mathbb{B}}$ is the negative-definite half of the coefficient space, while the regular model, whose determinant is blind to the sign, does not; this is the only place where the two models disagree. On the quaternion subspace both determinants are strictly positive, nothing there is singular, which is the matrix statement that the quaternion subspace carries no zero divisor and is the largest of the remarkable subspaces with that property. The centre is the only one of the remarkable subspaces whose image is scalar matrices in both models, and a scalar matrix $AI$ is singular only at $A=0$, so the centre contains no singular matrix but the zero one. The vector units explain the two Hermitian rows: $\mathsf{M}_2(\vec e_\lambda)$ is $-i$ times a Hermitian (Pauli) matrix, whereas $\mathsf{M}_4(\vec e_\lambda)$ is real and skew-symmetric, so $i\mathsf{M}_4(\vec e_\lambda)$ is Hermitian, and in both models a Hermitian element has a Hermitian image.


## The General Plain Bilinear Form in the Regular Model

The regular matrix carries the same pairing as the $2\times2$ one, with the trace four times the scalar part where the $2\times2$ trace is twice it.

**Theorem (the trace pairing of the regular matrices).** For all biquaternions,

$$
\boxed{\; \tfrac12\operatorname{Tr}\bigl(\mathsf{M}_4^{L}(\tilde Q_1)\mathsf{M}_4^{L}(\tilde Q_2)\bigr)=2\,\langle\tilde Q_1,\tilde Q_2\rangle,\qquad
\langle\tilde Q_1,\tilde Q_2\rangle=\tfrac14\operatorname{Tr}\bigl(\mathsf{M}_4^{L}(\tilde Q_1)\mathsf{M}_4^{L}(\tilde Q_2)\bigr) \;},
$$

so the plain trace pairing of the regular matrices is twice the general plain bilinear form of the algebra, and on the diagonal

$$
\tfrac14\operatorname{Tr}\bigl(\mathsf{M}_4^{L}(\tilde{Q})^2\bigr)=\langle\tilde Q,\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^2,\qquad \varepsilon_0=+1,\ \varepsilon_1=\varepsilon_2=\varepsilon_3=-1 .
$$

*Proof.* The representation is a homomorphism, so $\operatorname{Tr}(\mathsf{M}_4^{L}(\tilde Q_1)\mathsf{M}_4^{L}(\tilde Q_2))=\operatorname{Tr}\mathsf{M}_4^{L}(\tilde Q_1\tilde Q_2)=4\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$; the factor $2$ of the first display and the factor $\tfrac14$ of the second follow. The diagonal is the same identity on the basis, where $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$.

**The Gram matrix, the congruence and the signature.** In the coefficient basis the Gram matrix of $B$ is the sign matrix $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$, the negative of the sign matrix $D$ of the transposition theorem below, which is the same statement because $(-D)M^{\mathsf T}(-D)=DM^{\mathsf T}D$; a change of basis of matrix $S$ replaces it by $S^{\mathsf T}\mathrm{E}S$, and over $\mathbb{C}$ the form is determined up to congruence by its rank alone. Over $\mathbb{R}$ the form has signature $(4,4)$ on the eight real coordinates of the coefficient space, and it is indefinite.

**The null set.** The pairing vanishes on the cone $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ of real dimension $6$, the same cone as in the $2\times2$ model; the two representations carry the same null set, because the form is transported by the two realizations of the same element. It is the null set of neither the determinant nor the general quaternionic bilinear form.

**The automorphisms.** A matrix preserves the trace pairing exactly when $T^{\mathsf T}\mathrm{E}T=\mathrm{E}$, so the automorphism group on the coefficient space is $\{T\in GL_4(\mathbb{C}):T^{\mathsf T}\mathrm{E}T=\mathrm{E}\}=O_4(\mathbb{C})$, of complex dimension $6$ and real dimension $12$, its Lie algebra $\{X:X^{\mathsf T}\mathrm{E}+\mathrm{E}X=0\}$ being of real dimension $12$; its real forms $O(4)$ and $O(1,3)$ are cut out by the Hermitian and the coefficient conjugation on the Hermitian and the quaternion subspace. The group of real-linear automorphisms of the realified form is the larger $O(4,4)$, not the group the form defines over $\mathbb{C}$. Two operators act on the regular matrix from the algebra: the transposition, which carries the natural conjugation, $\mathsf{M}_4^{L}(\tilde{Q})\mapsto\mathsf{M}_4^{L}(\tilde{Q}^{\natural})$, and the conjugation $\mathsf{M}_4^{L}(\tilde{Q})\mapsto\mathsf{M}_4^{L}(\tilde{U})\mathsf{M}_4^{L}(\tilde{Q})\mathsf{M}_4^{L}(\tilde{U})^{-1}$ by a unit; both are automorphisms of the pairing.

## Transposition and the Two Matrices

**Proposition (transposition is quaternion conjugation).** For every biquaternion $\tilde{Q}$,

$$
\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} = \mathsf{M}_4^{L}(\tilde{Q}^{\natural}),
$$

where the transpose is taken in the basis $e_t, \vec e_x, \vec e_y, \vec e_z$ of the corpus.

**Proof.** Transposing the displayed closed form of $\mathsf{M}_4^{L}(\tilde{Q})$ gives

$$
\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} = \begin{pmatrix}
Q_t & Q_x & Q_y & Q_z \\
-Q_x & Q_t & Q_z & -Q_y \\
-Q_y & -Q_z & Q_t & Q_x \\
-Q_z & Q_y & -Q_x & Q_t
\end{pmatrix},
$$

and replacing $Q_\mu$ by $-Q_\mu$ in that same closed form reproduces this matrix.

**Remark (the false identity).** The right regular matrix is **not** the transpose of the left one:

$$
\mathsf{M}_4^{R}(\tilde{Q}) \neq \mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} \quad \text{in general}.
$$

For $\tilde{Q} = \vec e_x$ the left matrix is $\mathsf{M}_4^{L}(\vec e_x) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$, whose transpose is $\begin{pmatrix} 0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{pmatrix}$, while the right matrix is $\mathsf{M}_4^{R}(\vec e_x) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{pmatrix}$: the two differ in the sign of the upper-left block. The proposition above gives the reason: the transpose is the left regular matrix of the quaternion conjugate, $\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} = \mathsf{M}_4^{L}(\tilde{Q}^{\natural})$, so it is a left regular matrix and equals a right regular matrix only on the centre. The variant that replaces $\tilde{Q}$ by $\tilde{Q}^{\natural}$ is not a second identity, since $\tilde{Q} \mapsto \tilde{Q}^{\natural}$ is a bijection of the algebra.

**Theorem (the correct relation).** Let $D = \operatorname{diag}(-1, 1, 1, 1)$, so that $D^2 = I$. Then for every biquaternion $\tilde{Q}$,

$$
\boxed{\; \mathsf{M}_4^{R}(\tilde{Q}) = D\,\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}\,D = D\,\mathsf{M}_4^{L}(\tilde{Q}^{\natural})\,D \;}.
$$

Hence the right regular matrix is the contragredient of the left one up to the fixed change of basis $D$.

**Proof.** Apply $D$ on the left and on the right to the transpose of the closed form of $\mathsf{M}_4^{L}(\tilde{Q})$. Left multiplication by $D$ negates the first row, and right multiplication by $D$ negates the first column; the corner entry lies in both and is negated twice, hence unchanged. The resulting matrix is the closed form of $\mathsf{M}_4^{R}(\tilde{Q})$ displayed above. The second equality uses the transpose proposition.

**Corollary (the difference vanishes exactly on the centre).** The difference $\mathsf{M}_4^{L}(\tilde{Q}) - \mathsf{M}_4^{R}(\tilde{Q})$ is the zero matrix if and only if $\tilde{Q} \in \mathbb{C}_{\mathbb{B}} = \mathbb{C} e_t$.

**Proof.** If $\tilde{Q} = \lambda e_t$ then $\mathsf{M}_4^{L}(\tilde{Q}) = \mathsf{M}_4^{R}(\tilde{Q}) = \lambda I$, since scalar multiplication is central. Conversely, if the two matrices agree then $\tilde{Q}\tilde Q_4 = \tilde Q_4\tilde{Q}$ for every $\tilde Q_4$, so $\tilde{Q}$ lies in the centre, which is the scalar subspace. Comparing the two closed forms directly, the entries in the three last rows and columns agree only when $Q_x = Q_y = Q_z = 0$.

**Remark (what left and right mean).** The two matrices differ **because the algebra is non-commutative**. The $\mu$-th column of the difference $\mathsf{M}_4^{L}(\tilde{Q}) - \mathsf{M}_4^{R}(\tilde{Q})$ is the coordinate column of $\tilde{Q}e_\mu - e_\mu\tilde{Q}$, the commutator $[\tilde{Q}, e_\mu]$; the difference vanishes on $\mathbb{C}_{\mathbb{B}}$ and nowhere else. This is the sense in which the left and right regular matrices of $\mathbb{B}$ are distinct, and the sense in which the row of *The Four-Vector Element Representation of Biquaternions* carries the right action and not a further left one.

## The Module Structure and Reducibility

The regular representation is the first reducible realization in this subcategory, and its reduction is the decomposition of the algebra into two minimal left ideals.

**Definition.** Let

$$
\tilde\Pi_+ = \tfrac{1}{2}(e_t + i \vec e_z), \qquad \tilde\Pi_- = \tfrac{1}{2}(e_t - i \vec e_z).
$$

**Lemma (orthogonal idempotents).** The elements $\tilde\Pi_+$ and $\tilde\Pi_-$ satisfy

$$
\tilde\Pi_+^2 = \tilde\Pi_+, \qquad \tilde\Pi_-^2 = \tilde\Pi_-, \qquad \tilde\Pi_+\tilde\Pi_- = \tilde\Pi_-\tilde\Pi_+ = 0, \qquad \tilde\Pi_+ + \tilde\Pi_- = e_t,
$$

so that $\mathbb{B} = \mathbb{B}\tilde\Pi_+ \oplus \mathbb{B}\tilde\Pi_-$ as a direct sum of left ideals. $i\vec e_z$ is a root of $+1$, $(i\vec e_z)^2 = e_t$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents.

**Proof.** Because $i$ is central, $\vec e_z^2 = -e_t$ and $i^2 = -1$, one computes $\tilde\Pi_+^2 = \tfrac{1}{4}(e_t^2 + 2i\vec e_z + i^2 \vec e_z^2) = \tfrac{1}{4}(e_t + 2i\vec e_z + e_t) = \tfrac{1}{2}(e_t + i\vec e_z) = \tilde\Pi_+$, and similarly $\tilde\Pi_-^2 = \tilde\Pi_-$, while $\tilde\Pi_+\tilde\Pi_- = \tfrac{1}{4}(e_t^2 - i^2\vec e_z^2) = \tfrac{1}{4}(e_t - e_t) = 0$. The sum is $e_t$, and the two ideals meet only in $0$: an element lying in both satisfies $\tilde{Q} = \tilde{Q}\tilde\Pi_- = 0$, because membership of $\mathbb{B}\tilde\Pi_-$ gives $\tilde{Q}\tilde\Pi_- = \tilde{Q}$ while $\tilde\Pi_+\tilde\Pi_- = 0$. The sum is therefore direct. The idempotents and the Peirce decomposition are the subject of *Ideals and Peirce Decompositions of the Biquaternion Algebra*; the statement is used here only to split the module.

**Theorem (the left regular matrix is $V \oplus V$).** In the basis

$$
\tilde\Pi_+, \quad \vec e_x \tilde\Pi_+, \quad \tilde\Pi_-, \quad \vec e_x \tilde\Pi_-
$$

of $\mathbb{B}$, the left regular matrix of $\tilde{Q}$ is

$$
\mathsf{M}_4^{L}(\tilde{Q}) \sim \begin{pmatrix}
Q_t - iQ_z & -Q_x + iQ_y & 0 & 0 \\
Q_x + iQ_y & Q_t + iQ_z & 0 & 0 \\
0 & 0 & Q_t + iQ_z & -Q_x - iQ_y \\
0 & 0 & Q_x - iQ_y & Q_t - iQ_z
\end{pmatrix},
$$

with the four corner entries zero: the subspaces spanned by $\tilde\Pi_+, \vec e_x\tilde\Pi_+$ and by $\tilde\Pi_-, \vec e_x\tilde\Pi_-$ are invariant under $\mathsf{M}_4^{L}(\tilde{Q})$, and on each of them the action is that of a minimal left ideal, hence a copy of the simple module $V$, so that the left regular representation is

$$
\boxed{\; \mathbb{B} \cong V \oplus V \;}
$$

as a left $\mathbb{B}$-module. The regular representation is therefore reducible, and it is the first reducible realization in this subcategory.

**Proof.** The two ideals $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ are stable under left multiplication by $\tilde Q$, because $\tilde{Q}(\tilde{Q}_5\tilde\Pi_+) = (\tilde{Q}\tilde{Q}_5)\tilde\Pi_+$ for every $\tilde{Q}_5$; hence the matrix is block diagonal in any basis adapted to the decomposition. The ideal $\mathbb{B}\tilde\Pi_+$ has the basis $\tilde\Pi_+, \vec e_x\tilde\Pi_+$, since $\vec e_y \tilde\Pi_+ = i \vec e_x \tilde\Pi_+$ and $\vec e_z \tilde\Pi_+ = -i\tilde\Pi_+$. Its multiplication by the basis elements is read from

$$
\vec e_x \tilde\Pi_+ = \vec e_x\tilde\Pi_+, \quad \vec e_y \tilde\Pi_+ = i\vec e_x\tilde\Pi_+, \quad \vec e_z \tilde\Pi_+ = -i\tilde\Pi_+, \qquad \vec e_x(\vec e_x\tilde\Pi_+) = -\tilde\Pi_+, \quad \vec e_y(\vec e_x\tilde\Pi_+) = i\tilde\Pi_+, \quad \vec e_z(\vec e_x\tilde\Pi_+) = i\vec e_x\tilde\Pi_+,
$$

so in the basis $\tilde\Pi_+, \vec e_x\tilde\Pi_+$ the sum $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ acts by the first two rows and columns of the displayed matrix, and the same computation on the basis $\tilde\Pi_-, \vec e_x\tilde\Pi_-$ of $\mathbb{B}\tilde\Pi_-$ gives the last two. The trace of the matrix is $4Q_t$ by inspection and the determinant is the product of its two diagonal groups,

$$
(Q_t - iQ_z)(Q_t + iQ_z) - (-Q_x + iQ_y)(Q_x + iQ_y) = \langle\tilde{Q}\rangle_{\natural},
$$

each of the two diagonal groups contributing the same factor, so that the determinant of the regular matrix is $\langle\tilde{Q}\rangle_{\natural}^2$.

**Remark (the characteristic polynomial).** In the adapted basis of the theorem above the regular matrix is diagonal in the two invariant subspaces, so its characteristic polynomial is the square of that of the simple module,

$$
\chi_{\mathsf{M}_4^{L}(\tilde{Q})}(\lambda) = \bigl( \lambda^2 - 2Q_t\lambda + \langle\tilde{Q}\rangle_{\natural} \bigr)^2,
$$

which the form of the theorem above gives at once. The eigenvalues themselves, the Cayley–Hamilton identity, the eigenspace dimensions and the doubling of the multiplicities that the square produces are the subject of *Biquaternion Spectral Theory*, later in this chapter, and are cited from there rather than developed here.

**Remark (the irreducible submodules are the minimal left ideals).** The two invariant subspaces are the two minimal left ideals $I_1 = \mathbb{B}\tilde\Pi_+$ and $I_2 = \mathbb{B}\tilde\Pi_-$ of the algebra. Both afford the module $V$, and the fact that $V$ is the only simple module is the classification of the simple modules. The decomposition $\mathbb{B} = I_1 \oplus I_2$ is therefore the same fact as the diagonal form of the regular matrix, read as ideals rather than as a matrix; the same decomposition is stated in *Modules over the Biquaternion Algebra*, where the simple module is written $S$, as $\mathbb{B} \cong S \oplus S$.

## The Double Centralizer

**Theorem (the centralizer is the right copy).** The centralizer of the image $\mathsf{M}_4^{L}(\mathbb{B})$ in $M_4(\mathbb{C})$,

$$
\bigl\{ C \in M_4(\mathbb{C}) \;:\; C\,\mathsf{M}_4^{L}(\tilde Q_4) = \mathsf{M}_4^{L}(\tilde Q_4)\,C \ \text{ for every } \tilde Q_4 \in \mathbb{B} \bigr\},
$$

is the image $\mathsf{M}_4^{R}(\mathbb{B})$, of complex dimension $4$.

**Proof.** Write $\operatorname{col}(\tilde Q_5)$ for the coordinate column of $\tilde Q_5$. The defining property of the left matrix is $\mathsf{M}_4^{L}(\tilde Q_4)\operatorname{col}(\tilde Q_5) = \operatorname{col}(\tilde Q_4\tilde{Q}_5)$, and in particular $\mathsf{M}_4^{L}(\tilde Q_4)\operatorname{col}(e_t) = \operatorname{col}(\tilde Q_4)$. Let $C$ be in the centralizer and let $\vec q_a = C\operatorname{col}(e_t)$ be its first column; write $\tilde{Q}$ for the element of that coordinate column. Then, for every $\tilde Q_4$,

$$
C\operatorname{col}(\tilde Q_4) = C\,\mathsf{M}_4^{L}(\tilde Q_4)\operatorname{col}(e_t) = \mathsf{M}_4^{L}(\tilde Q_4)\,C\operatorname{col}(e_t) = \mathsf{M}_4^{L}(\tilde Q_4)\operatorname{col}(\tilde{Q}) = \operatorname{col}(\tilde Q_4\tilde{Q}) = \mathsf{M}_4^{R}(\tilde{Q})\operatorname{col}(\tilde Q_4),
$$

the last step being the defining property of the right matrix. The four columns $\operatorname{col}(\tilde Q_4)$ span $\mathbb{C}^4$, so $C = \mathsf{M}_4^{R}(\tilde{Q})$ and the centralizer is contained in $\mathsf{M}_4^{R}(\mathbb{B})$. Conversely every $\mathsf{M}_4^{R}(\tilde{Q})$ commutes with every $\mathsf{M}_4^{L}(\tilde Q_4)$, because $(\tilde Q_4\tilde{Q}_5)\tilde{Q} = \tilde Q_4(\tilde{Q}_5\tilde{Q})$ is associativity; hence the centralizer is exactly $\mathsf{M}_4^{R}(\mathbb{B})$. It has complex dimension $4$ because $\mathsf{M}_4^{R}$ is injective: $\mathsf{M}_4^{R}(\tilde{Q}) = 0$ forces its first column, which is the coordinate column of $\tilde Q$, to vanish.

**Remark.** The theorem is the regular-module case of the double centralizer phenomenon, and it is the mirror of the identification of $\mathbb{B}$ with the matrix algebra of the simple module in *Modules over the Biquaternion Algebra*: the algebra is recovered as the centralizer of the opposite copy. The two images $\mathsf{M}_4^{L}(\mathbb{B})$ and $\mathsf{M}_4^{R}(\mathbb{B})$ commute, and the products of one matrix from each already span the full matrix algebra $M_4(\mathbb{C})$, as the section on the sixteen products shows.

## The Real Form

**Proposition (the real regular matrix).** Regarded over $\mathbb{R}$ in the real basis

$$
e_t, \vec e_x, \vec e_y, \vec e_z, i e_t, i \vec e_x, i \vec e_y, i \vec e_z,
$$

of the eight-dimensional real space underlying $\mathbb{B}$, the left regular matrix becomes an $8 \times 8$ real matrix $\mathsf{M}_4^{L,\mathbb{R}}(\tilde{Q})$, with

$$
\det \mathsf{M}_4^{L,\mathbb{R}}(\tilde{Q}) = |\langle\tilde{Q}\rangle_{\natural}|^4, \qquad \operatorname{Tr}\mathsf{M}_4^{L,\mathbb{R}}(\tilde{Q}) = 8 \operatorname{Re}(Q_t).
$$

**Proof.** The real matrix is the realification of the complex matrix $\mathsf{M}_4^{L}(\tilde{Q})$, each complex entry being replaced by its real $2\times2$ block. A complex-linear map with eigenvalues $\lambda_1, \ldots, \lambda_4$ has realification with eigenvalues $\lambda_1, \bar\lambda_1, \ldots, \lambda_4, \bar\lambda_4$, so its determinant is $|\lambda_1 \cdots \lambda_4|^2 = |\det \mathsf{M}_4^{L}(\tilde{Q})|^2 = |\langle\tilde{Q}\rangle_{\natural}^2|^2 = |\langle\tilde{Q}\rangle_{\natural}|^4$, and its trace is $2\operatorname{Re}(\lambda_1 + \cdots + \lambda_4) = 2\operatorname{Re}(4Q_t) = 8\operatorname{Re}(Q_t)$.

**Remark (why the dimension doubles).** The real dimension doubles because $\mathbb{B}$ is a complex vector space and is regarded as a real vector space by restriction of scalars: the correspondence $\operatorname{Res}_{\mathbb{C}/\mathbb{R}} \mathbb{C}^4 = \mathbb{R}^8$ replaces each complex coordinate by its real and imaginary parts. The same doubling applies to the module $V$, whose realification $S$ has real dimension $4$, so over $\mathbb{R}$ the left regular matrix is $\mathsf{M}_4^{L,\mathbb{R}} \cong \operatorname{Res}_{\mathbb{C}/\mathbb{R}}(V \oplus V)$, and the decomposition of the complex case survives with each part doubled in size. Restricted to the real subalgebra $\mathbb{H}_{\mathbb{B}}$, and read on $\mathbb{H}_{\mathbb{B}}$ itself, the same construction is the $4 \times 4$ real regular matrix of the quaternions, which is the subject of *Quaternion Element Representations*; complexifying the algebra doubles both its real dimension and the size of the regular matrix.

## The Sandwich in the Regular Basis

The Hermitian sandwich $\tilde Q_4 \mapsto \tilde Q\tilde Q_4\tilde Q^{*}$ of *Two-Sided Operators on the General Plain Sesqualgebra* is read here as a single matrix.

**The sandwich matrix.** Put

$$
\mathsf{H}_{\tilde Q} := \mathsf{M}_4^{L}(\tilde{Q})\,\mathsf{M}_4^{R}(\tilde{Q}^{*}) .
$$

It is the matrix that carries the coordinate column of $\tilde Q_4$ to the coordinate column of $\tilde{Q}\tilde Q_4\tilde{Q}^{*}$: indeed $\mathsf{M}_4^{R}(\tilde{Q}^{*})\operatorname{col}(\tilde Q_4) = \operatorname{col}(\tilde Q_4\tilde{Q}^{*})$ and then $\mathsf{M}_4^{L}(\tilde{Q})\operatorname{col}(\tilde Q_4\tilde{Q}^{*}) = \operatorname{col}(\tilde{Q}\tilde Q_4\tilde{Q}^{*})$. In that sense it is the regular-basis reading of the sandwich, and it has three properties that no other realization shows.

**Lemma (the left regular matrix respects the dagger).** For every $\tilde{Q}$,

$$
\mathsf{M}_4^{L}(\tilde{Q}^{*}) = \mathsf{M}_4^{L}(\tilde{Q})^{\dagger} ,
$$

the conjugate transpose of the regular matrix.

**Proof.** Both sides are conjugate-linear in $\tilde{Q}$ and additive, so it suffices to check the eight real basis elements. On $e_t$ both sides are $I$ and on $ie_t$ both are $-iI$. On $\vec e_\lambda$ the left side is $-\mathsf{M}_4^{L}(\vec e_\lambda)$, and the right side is $\mathsf{M}_4^{L}(\vec e_\lambda)^{\dagger} = \mathsf{M}_4^{L}(\vec e_\lambda)^{\mathsf{T}} = -\mathsf{M}_4^{L}(\vec e_\lambda)$, because left multiplication by the vector unit $\vec e_\lambda$ is given by the products $\vec e_\lambda \vec e_\nu$, whose four matrices are real and skew-symmetric. On $i\vec e_\lambda$ the left side is $i\mathsf{M}_4^{L}(\vec e_\lambda)$ and the right side is $(i\mathsf{M}_4^{L}(\vec e_\lambda))^{\dagger} = -i\mathsf{M}_4^{L}(\vec e_\lambda)^{\mathsf{T}} = i\mathsf{M}_4^{L}(\vec e_\lambda)$, the same skew-symmetry applied once more.

**Theorem (the sandwich matrix is a product of the two regular matrices).** For every $\tilde{Q}$,

$$
\mathsf{H}_{\tilde Q} = \mathsf{M}_4^{L}(\tilde{Q})\,\mathsf{M}_4^{R}(\tilde{Q}^{*}) ,
$$

the left regular matrix of $\tilde Q$ multiplied by the right regular matrix of its Hermitian conjugate, in that order.

**Proof.** For every $\tilde Q_4$, $\mathsf{M}_4^{R}(\tilde{Q}^{*})\operatorname{col}(\tilde Q_4) = \operatorname{col}(\tilde Q_4\tilde{Q}^{*})$ and $\mathsf{M}_4^{L}(\tilde{Q})\operatorname{col}(\tilde Q_4\tilde{Q}^{*}) = \operatorname{col}(\tilde{Q}\tilde Q_4\tilde{Q}^{*})$, the defining properties of the two matrices applied in turn; the product therefore carries $\operatorname{col}(\tilde Q_4)$ to $\operatorname{col}(\tilde{Q}\tilde Q_4\tilde{Q}^{*})$, which is what defines $\mathsf{H}_{\tilde Q}$.

The identity is the regular-basis reading of the double centralizer above: the two factors come from the two commuting images $\mathsf{M}_4^{L}(\mathbb{B})$ and $\mathsf{M}_4^{R}(\mathbb{B})$, and their order is immaterial because the images commute. It also says that the sandwich is a **congruence** and not a similarity: a similarity would pair $\tilde{Q}$ with $\tilde{Q}^{-1}$, whereas here the second factor is $\tilde{Q}^{*}$, equal to the inverse only on the unitary slice.

**Corollary (closed form in the coefficient basis).** For every $\tilde{Q}$,

$$
\mathsf{H}_{\tilde Q} = \mathsf{M}_4^{L}(\tilde{Q})\,D\,\mathsf{M}_4^{L}(\tilde{Q})^{*}\,D , \qquad D = \operatorname{diag}(-1,1,1,1) ,
$$

the star being the entrywise complex conjugate.

**Proof.** By the transposition theorem, $\mathsf{M}_4^{R}(\tilde{Q}^{*}) = D\,\mathsf{M}_4^{L}(\tilde{Q}^{*})^{\mathsf{T}}\,D$; by the lemma above, $\mathsf{M}_4^{L}(\tilde{Q}^{*}) = \mathsf{M}_4^{L}(\tilde{Q})^{\dagger}$, and the conjugate transpose is $(\mathsf{M}_4^{L}(\tilde{Q})^{*})^{\mathsf{T}}$. Substituting into the theorem gives the display. Every entry of $\mathsf{H}_{\tilde Q}$ is therefore sesquilinear in the four coefficients of $\tilde{Q}$, so the sandwich is quadratic in $\tilde Q$ and linear in the operand.

**Proposition (the real $8 \times 8$ invariants).** Write $\mathsf{H}_{\tilde Q}^{\mathbb{R}}$ for the realification of $\mathsf{H}_{\tilde Q}$ in the real basis $e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z$. Then

$$
\det\bigl(\mathsf{H}_{\tilde Q}^{\mathbb{R}}\bigr) = |\langle\tilde{Q}\rangle_{\natural}|^{8}, \qquad \operatorname{Tr}\bigl(\mathsf{H}_{\tilde Q}^{\mathbb{R}}\bigr) = 8\,|Q_t|^{2} .
$$

**Proof.** Realification replaces each complex eigenvalue by the pair formed with its conjugate, so the determinant is the squared modulus of the complex determinant and the trace is twice the real part of the complex trace. The sandwich has the four complex eigenvalues $\lambda_i\overline{\lambda_j}$, of product $\lvert\lambda_1\lambda_2\rvert^{4} = \lvert \langle\tilde{Q}\rangle_{\natural}\rvert^{4}$ and of sum $\lvert\operatorname{tr}\mathsf{M}_4^{L}(\tilde{Q})\rvert^{2} = 4\lvert Q_t\rvert^{2}$ (*The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint*); the realification therefore gives $(\lvert N\rvert^{4})^{2} = \lvert N\rvert^{8}$ for the determinant and $2\cdot 4\lvert Q_t\rvert^{2} = 8\lvert Q_t\rvert^{2}$ for the trace. The two agree with the real form of the element above to the same exponents: the left regular matrix $\mathsf{M}_4^{L}(\tilde{Q})$ has $\lvert N\rvert^{4}$ and $8\operatorname{Re}Q_t$, the sandwich matrix has $\lvert N\rvert^{8}$ and $8\lvert Q_t\rvert^{2}$, and the second invariant of each is a modulus rather than a real part because the sandwich has lost the phase.

## A Second $4 \times 4$ Realization, and the Multiplicative Map

The regular matrix is not the only $4 \times 4$ realization of $\mathbb{B}$ in use, and the second one worth recording comes from a question with no algebra in it: the eigenvectors of a parameterised family of matrices. Its shape is different enough that the difference is instructive, and the object it is built for — a multiplicative quadratic map into the real matrices, with no counterpart in the regular realization — is the reason for recording it here rather than in a dedicated article.

**The realization.** In the basis $e_t, i\vec e_x, i\vec e_y, i\vec e_z$, for which

$$
(i\vec e_x)^2 = (i\vec e_y)^2 = (i\vec e_z)^2 = e_t, \qquad (i\vec e_x)(i\vec e_y) = i(i\vec e_z), \qquad (i\vec e_y)(i\vec e_z) = i(i\vec e_x), \qquad (i\vec e_z)(i\vec e_x) = i(i\vec e_y) ,
$$

the matrix whose columns are the coordinate columns of $\tilde Q e_t, \tilde Q i\vec e_x, \tilde Q i\vec e_y, \tilde Q i\vec e_z$, written $\mathsf{M}'_4$ for this second realization to keep it apart from the regular matrix $\mathsf{M}_4^{L}$,

$$
\mathsf{M}'_4(A_t, A_x, A_y, A_z) = \begin{pmatrix} A_t & A_x & A_y & A_z \\ A_x & A_t & -iA_z & iA_y \\ A_y & iA_z & A_t & -iA_x \\ A_z & -iA_y & iA_x & A_t \end{pmatrix}
$$

is a multiplicative realization of $\mathbb{B}$. Its first row and column coincide, since $\mathsf{M}'_4$ is symmetric in the coefficients, which the Cayley matrix of the regular realization is not; the price is the scalar imaginary scattered through the lower block. The change of basis is what makes the squares $+e_t$: the generators of this realization are the elements $i\vec e_\lambda$, not the $\vec e_\lambda$, and the difference is a change of orientation, the two choices being interchanged by the coefficient conjugation, not two different algebras.

**The realization is equivalent to the regular one.** Nothing in the representation theory of the two distinguishes them, and everything the corpus says about the regular representation as a module carries over.

**What the realization brings.** Each of $i\vec e_x, i\vec e_y, i\vec e_z$ is skew **for the Minkowski form** $D$ of the remark below, $M^{\mathsf T} = -DMD$, and not in the plain sense: it is the form's matrix, not the identity, that makes them skew. The products of the basis elements give a second Hermitian basis of $M_4(\mathbb{C})$: the sixteen matrices

$$
I,\; i\vec e_xK_1,\; i\vec e_yK_2,\; i\vec e_zK_3,\quad i\vec e_x,\; K_1,\; i\vec e_yK_3,\; i\vec e_zK_2,\quad i\vec e_y,\; K_2,\; i\vec e_xK_3,\; i\vec e_zK_1,\quad i\vec e_z,\; K_3,\; i\vec e_xK_2,\; i\vec e_yK_1 ,
$$

with $K_1, K_2, K_3$ the coefficient conjugates of $i\vec e_x, i\vec e_y, i\vec e_z$, each squaring to $I$ and each Hermitian, so that real linear combinations of them are exactly the Hermitian $4 \times 4$ matrices; every one but $I$ is traceless. The same basis contains generators of the complex Clifford algebra $\mathbb{C}\ell(4)$, namely $i\vec e_x, i\vec e_y, i\vec e_zK_1, i\vec e_zK_2$, which anticommute pairwise to $\delta_{\mu\nu}I$ up to the conventional factor, so the realization also places $\mathbb{B}$ inside $M_4(\mathbb{C})$ in the Clifford manner of *Biquaternion Other Algebraic Element Representations*.

**The transposition identity is exact in this basis, and these are the matrices of the Maxwell literature.** The realization is the one in which the two $D$'s of the theorem of the transposition section disappear, and this is worth stating because it separates two things that the first basis runs together. Write the left regular matrix of the element $\tilde{Q} = A_t e_t + A_x i\vec e_x + A_y i\vec e_y + A_z i\vec e_z$ in this realization as

$$
\mathsf{M}'_4(\tilde{Q}) = A_t I + cF(\vec A), \qquad
cF(\vec A) := \begin{pmatrix} 0 & \vec A^{\mathsf{T}} \\ \vec A & i[\vec A]_\times \end{pmatrix}, \qquad \vec A = (A_x, A_y, A_z),
$$

with $[\vec A]_\times$ the matrix of $\vec v \mapsto \vec A \times \vec v$; this is the display of the realization above, and it is the same $cF$ that a matrix formulation of Maxwell's equations multiplies into the column $(-\partial/\partial t, \nabla)^{\mathsf{T}}$. In this basis the right regular matrix is **exactly the transpose**,

$$
\mathsf{M}'^{R}_4(\tilde{Q}) = \mathsf{M}'_4(\tilde{Q})^{\mathsf{T}} ,
$$

with no sign matrix, where in the basis $e_t, \vec e_x, \vec e_y, \vec e_z$ of the transposition section the relation read $\mathsf{M}_4^{R} = D\,\mathsf{M}_4^{L}{}^{\mathsf{T}}D$ instead. So the *false identity* remark of the transposition section is a statement about a basis and not about the algebra: in the basis whose vector units square to $-e_t$ the transpose of the left matrix is the left regular matrix of the conjugate, while in the basis whose vector units square to $+e_t$ it is the right regular matrix, exactly, and the two $D$'s are the price of the first basis. The sixteen-matrix basis above is the same object read on the other side: as matrices it is $I$, the three $cF(\mathbf{e}_i)$, their complex conjugates and the pairwise products $cF(\mathbf{e}_i)(cF(\mathbf{e}_j))^{\natural}$, which are Hermitian and involutive with square $I$, traceless except for $I$, and orthogonal under the trace, $\operatorname{tr}(M_kM_l) = 4\delta_{kl}$ — all checked exactly — and the three $cF(\mathbf{e}_i)$ anticommute pairwise with $cF(\mathbf{e}_1)cF(\mathbf{e}_2) = i\,cF(\mathbf{e}_3)$.

**The multiplicative map.** The object the realization is built for is

$$
m(A) = A A^{\natural}, \qquad A \in I + \mathbb{B},
$$

the **multiplicative map** $m(A) = A A^{\natural}$, named after the complex absolute value. Since $A^{\natural}$ commutes with $A$, the product is central, and in this realization it is the **scalar** matrix

$$
m(A) = \bigl(A_t^2 - A_x^2 - A_y^2 - A_z^2\bigr) I \;=\; \Delta(A)\, I ,
$$

checked exactly (all four entries equal, the off-diagonal ones vanishing). The image is therefore a real matrix exactly when the four coefficients $A_\mu$ are real, and $\Delta$ is then the Lorentzian square of the coefficient vector; for a genuinely complex element $\Delta$ need not be real — at $A = (1+i)e_t$ it is $2i$ — so it is the *centrality* that the commutation with $A^{\natural}$ delivers, and the reality of the image is a separate property of the real coefficient set. Multiplicativity follows from the centrality, $m(AB) = ABB^{\natural}A^{\natural} = A\cdot\Delta(B)\cdot A^{\natural} = \Delta(A)\Delta(B)I = m(A)m(B)$, and it was checked exactly as well. The read-off of the map is a quadratic map with no complex-linear analogue. What the corpus takes from the map is the existence of a *multiplicative* quadratic real map of this kind at all, next to the one it already owns: the congruence $Y\mapsto \mathsf{M}_2(\tilde{Q})\,Y\,\mathsf{M}_2(\tilde{Q})^{\dagger}$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* is the quadratic map of the same algebra that is **not** multiplicative, being a congruence rather than a product, and the two together show that the algebra carries a multiplicative and a non-multiplicative quadratic map.

**The Minkowski form of the realization.** The real span of $e_t, i\vec e_x, i\vec e_y, i\vec e_z$ carries a real form of signature $(1,3)$, whose matrix in the coefficient order $(e_t, i\vec e_x, i\vec e_y, i\vec e_z)$ is

$$
D = \operatorname{diag}(-1, 1, 1, 1)
$$

— the same sign matrix as in the transposition theorem above, one negative square on the scalar slot and three positive ones on the vector slots.

**Proposition (the generators are the infinitesimal generators of $O(1,3)$).** Each of the three generators satisfies

$$
M^{\mathsf T} = -DMD, \qquad \text{equivalently} \qquad M^{\mathsf T}D + DM = 0,
$$

that is, $DM$ is skew-symmetric; the second form is the defining condition for an element of the Lie algebra $\mathfrak{o}(1,3)$ of $O(1,3)$.

**Proof.** Direct verification on the three matrices $i\vec e_x, i\vec e_y, i\vec e_z$ of the realization, entry by entry and exactly, in each of the three equivalent forms.

The relation is a statement about the form and its orthogonal group, and the difference between it and the plain statement "$M$ is skew-symmetric" is the whole content: the three matrices are not skew in the plain sense, and it is $D$, not $I$, that makes them skew. Two real forms live here and they are different objects. The **general quaternionic bilinear form** $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural} = \operatorname{Sc}(\tilde Q_1\tilde Q_2^{\natural})$ is $\mathbb{C}$-bilinear and indefinite of signature $(4,4)$ on the eight-dimensional $\mathbb{B}_{\mathbb{R}}$, and it vanishes on the null elements; it is the form *of the algebra*, and it is owned by *The General Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*. The **Minkowski form** above is a real form of signature $(1,3)$ on the four-dimensional real slice spanned by $e_t, i\vec e_x, i\vec e_y, i\vec e_z$, and it is the form *of the realization's real slice*, with orthogonal group $O(1,3)$; it is not a form of the eight-dimensional realification, whose four realified forms have signatures $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$ (*The Realification and the Effect of the Change of Scalars*).

## The Sixteen Products and the Biparavectors

The double centralizer of the earlier section says that the left and the right images commute and that together they span the whole matrix algebra. The basis that exhibits this is the set of products of one matrix from each image, and in the second realization it can be taken Hermitian.

**The products.** For the coordinate units put

$$
P_{\mu\nu} := \mathsf{M}_4^{L}(e_\mu)\,\mathsf{M}_4^{R}(e_\nu), \qquad \mu, \nu \in \{t,x,y,z\}.
$$

In the second realization the right regular matrix is the transpose of the left, so $P_{\mu\nu}$ is the ordinary matrix product $\mathsf{M}'_4(e_\mu)\mathsf{M}'_4(e_\nu)^{\mathsf T}$; writing $E_\mu := \mathsf{M}'_4(e_\mu)$ for $\mu \in \{x, y, z\}$ and $E_t = I$,

$$
P_{\mu\nu} = E_\mu E_\nu^{\mathsf T}.
$$

The three units satisfy $E_\lambda^2 = I$ and anticommute pairwise, and their product is the complex structure of the realization, $E_xE_y = iE_z$; the matrices $E_\lambda$ are Hermitian, so $E_\nu^{\mathsf T}$ is its complex conjugate.

**Proposition (the sixteen products are an orthogonal basis).** The matrices $E_\mu E_\nu^{\mathsf T}$ are Hermitian, linearly independent over $\mathbb{C}$, and orthogonal under the trace, with a common normalisation:

$$
\operatorname{tr}\!\left(E_\mu E_\nu^{\mathsf T}\, E_\lambda E_\rho^{\mathsf T}\right) = 4\,\delta_{\mu\lambda}\delta_{\nu\rho}.
$$

This was checked entry by entry: the diagonal value is $4$ for each of the sixteen and every off-diagonal value is $0$. Independence follows, and the sixteen are a basis of $M_4(\mathbb{C})$.

**The expansion.** By the orthogonality every complex matrix $M$ has the expansion

$$
M = \sum_{\mu,\nu} a_{\mu\nu}\,E_\mu E_\nu^{\mathsf T}, \qquad a_{\mu\nu} = \tfrac14\operatorname{tr}\!\left(M\,E_\mu E_\nu^{\mathsf{T}}\right),
$$

the coefficients being read off one at a time. Recomputing the expansion on a random complex $4 \times 4$ matrix returns it to $5 \times 10^{-16}$.

**Reading the expansion in the algebra.** The tensor square $\mathbb{B} \otimes_{\mathbb{C}} \mathbb{B}$ is spanned by the sixteen $e_\mu \otimes e_\nu$, and the expansion says that these sixteen span the whole matrix algebra $M_4(\mathbb{C})$: the two-sided transformation $\tilde Q \mapsto \sum_{\mu,\nu} a_{\mu\nu}\, e_\mu \tilde Q e_\nu$ has matrix

$$
\sum_{\mu,\nu} a_{\mu\nu}\,\mathsf{M}_4^{L}(e_\mu)\,\mathsf{M}_4^{R}(e_\nu) = \sum_{\mu,\nu} a_{\mu\nu}\,P_{\mu\nu},
$$

and every complex matrix arises this way. Such an element $\sum a_{\mu\nu}\,e_\mu \otimes e_\nu$ is a **biparavector** in the language of the paravector formulation. That the sixteen products already span the matrices is the concrete form of the double centralizer: the left image supplies the first index and the right image the second, and the two fill $M_4(\mathbb{C})$ between them. Recomputing the matrix of the biparavector against the product $\mathsf{M}_4^{L}(\tilde Q_6)\mathsf{M}_4^{R}(\tilde Q_3)$ of a left–right sandwich returns $1.5 \times 10^{-14}$.

**Where the uniform normalisation comes from.** The constant $4$ in the trace relation is a property of the second realization and not of the regular basis. In the corpus basis $e_t, \vec e_x, \vec e_y, \vec e_z$ the matrix of the sixteen products is still diagonal, but its diagonal entries are $\pm 4$ rather than $4$, so the coefficient formula there carries the sign of $\operatorname{tr}(P_{\mu\nu}^2)$; it is the Hermitian realisation that makes the coefficients uniform. The tensor-square reading is the same object as the sixteen matrices listed by the realization above, read as outer products rather than as products of the two units.

## The Three Classical Functions and Their Matrices

The Conway calculus singles out three linear functions of the algebra, of the antisymmetric, the diagonal and the diagonal-less symmetric type. In the coordinate order $(\vec e_x,\vec e_y,\vec e_z,e_t)$ — vector part first, scalar last, the order of the displays — they are, with $t_x=s_ys_z$, $t_y=s_xs_z$ and $t_z=s_xs_y$,

$$
A\{a\}=\tfrac12\bigl(a[\,]-[\,]a\bigr)\ \longleftrightarrow\
\begin{pmatrix}0&-a_z&a_y&0\\a_z&0&-a_x&0\\-a_y&a_x&0&0\\0&0&0&0\end{pmatrix},
$$

$$
D\{d\}=\tfrac12\bigl(d_x\vec e_x[\,]\vec e_x+d_y\vec e_y[\,]\vec e_y+d_z\vec e_z[\,]\vec e_z\bigr)
\ \longleftrightarrow\
\tfrac12\begin{pmatrix}-d_x+d_y+d_z&0&0&0\\0&d_x-d_y+d_z&0&0\\0&0&d_x+d_y-d_z&0\\0&0&0&-(d_x+d_y+d_z)\end{pmatrix},
$$

$$
S\{s\}=D\{s_x^2,s_y^2,s_z^2\}-\tfrac12\,s[\,]s
\ \longleftrightarrow\
\begin{pmatrix}0&t_z&t_y&0\\t_z&0&t_x&0\\t_y&t_x&0&0\\0&0&0&0\end{pmatrix}.
$$

**Proposition (the matrix dictionary).** In the order $(\vec e_x,\vec e_y,\vec e_z,e_t)$ the function $A\{a\}$ is the antisymmetric $3\times3$ block, $D\{d\}$ the traceless diagonal and $S\{s\}$ the diagonal-less symmetric $3\times3$ block, each with a vanishing fourth row and column, and the three families together span the traceless part of $M_3(\mathbb C)$.

*Proof.* Direct computation of the sixteen matrices and comparison with the displays. The coordinate order is a genuine trap: the corpus's basis order is $(e_t,\vec e_x,\vec e_y,\vec e_z)$, whereas the matrix displays put the scalar last, and in the corpus's order the same matrices appear shifted by one.

**Remark (the source's sign).** The source writes the symmetric function with the two terms in the opposite order, $S\{s\}=\tfrac12 s[\,]s-D\{s_x^2,s_y^2,s_z^2\}$; its two displays of $S$ then differ by an overall sign. The corpus fixes the sign by the printed matrix, the one written here. $A\{a\}$ and $D\{d\}$ reproduce the source's displays exactly, with zero residual.

**Remark (the method degrades from three to four dimensions).** The antisymmetric, diagonal and diagonal-less symmetric functions exhaust the traceless part of $M_3(\mathbb C)$ in the order $(\vec e_x,\vec e_y,\vec e_z,e_t)$, since each acts on the vector part and fixes the scalar. For a general traceless $\mathbb C^4\to\mathbb C^4$ map the same three families no longer suffice: the symmetric part needs a function that mixes the scalar and vector parts, and the source records that the expression for it is cumbersome and not useful. The four-dimensional unitary groups are therefore assembled from two $SO(4)$ factors rather than from a single quaternion closed form — the same asymmetry that the Lie-group article reads as the clean three-dimensional and less clean four-dimensional parametrizations.

## The Four Words and the Four Traces in the Regular Model

The twelve operations of the two chapters are built from four products, and in the regular model each product is a word in the two matrices $X=\mathsf{M}_4^{L}(\tilde Q_1)$ and $Y=\mathsf{M}_4^{L}(\tilde Q_2)$ and in the two involutions of the realization, the transpose and the conjugate transpose. The transpose plays the part the adjugate plays in the $2\times2$ model, because $\mathsf{M}_4^{L}(\tilde Q)^{\mathsf T}=\mathsf{M}_4^{L}(\tilde Q^{\natural})$ is quaternion conjugation.

| product | first slot | second slot | the word |
|---|---|---|---|
| general plain | $X$ | $Y$ | $XY$ |
| general quaternionic | $X^{\mathsf T}$ | $Y$ | $X^{\mathsf T}Y$ |
| general plain sesquilinear | $X$ | $Y^{\dagger}$ | $XY^{\dagger}$ |
| general quaternionic sesquilinear | $X^{\mathsf T}$ | $Y^{\dagger}$ | $X^{\mathsf T}Y^{\dagger}$ |

The symmetric part of a product is the half-sum of its word and of the word with the two slots exchanged, and the antisymmetric part is the half-difference, as in the $2\times2$ model.

**The four forms are four traces.** The four products are four matrix traces, and the four forms of the algebra are read from them:

$$
\tfrac14\operatorname{Tr}(XY)=\langle\tilde Q_1,\tilde Q_2\rangle,\qquad
\tfrac14\operatorname{Tr}(X^{\mathsf T}Y)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural},\qquad
\tfrac14\operatorname{Tr}(XY^{\dagger})=\langle\tilde Q_1,\tilde Q_2\rangle_{*},\qquad
\tfrac14\operatorname{Tr}(X^{\mathsf T}Y^{\dagger})=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*},
$$

the general plain bilinear, the general quaternionic bilinear, the general plain sesquilinear and the general quaternionic sesquilinear form. The factor is $\tfrac14$ where the $2\times2$ model has $\tfrac12$, because the regular trace is four times the scalar part where the $2\times2$ trace is twice it; the two models compute the four forms from the same four words with their own normalisation.

## Summary

The left regular matrix $\mathsf{M}_4^{L}$ is the Cayley matrix of the left multiplication, with its multiplicativity, its trace $4Q_t$ and its determinant $\langle\tilde{Q}\rangle_{\natural}^2$. In the regular model the remarkable subspaces are the scalar, the traceless, the real, the purely imaginary, the Hermitian and the anti-Hermitian matrices, and the regular matrix is two copies of the $2\times2$ matrix of the same element, so its trace is twice and its determinant the square of the $2\times2$ ones, $\operatorname{Tr}\mathsf{M}_4^{L}(\tilde{Q}) = 2\operatorname{Tr}\mathsf{M}_2(\tilde{Q})$ and $\det\mathsf{M}_4^{L}(\tilde{Q}) = \det\mathsf{M}_2(\tilde{Q})^2$. Its transpose is the left regular matrix of the quaternion conjugate, $\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} = \mathsf{M}_4^{L}(\tilde{Q}^{\natural})$.

The right regular matrix $\mathsf{M}_4^{R}$, whose $\mu$-th column is the coordinate column of $e_\mu\tilde Q$, is anti-multiplicative and is the regular representation of the opposite algebra. The naive identity $\mathsf{M}_4^{R}(\tilde{Q}) = \mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}$ is false — and the variant with $\tilde{Q}^{\natural}$ is the same statement, since $\mathsf{M}_4^{L}(\tilde{Q}^{\natural})^{\mathsf{T}} = \mathsf{M}_4^{L}(\tilde{Q})$ — while what holds is $\mathsf{M}_4^{R}(\tilde{Q}) = D\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}D = D\mathsf{M}_4^{L}(\tilde{Q}^{\natural})D$ with $D = \operatorname{diag}(-1,1,1,1)$. The difference $\mathsf{M}_4^{L} - \mathsf{M}_4^{R}$ vanishes exactly on the centre $\mathbb{C}_{\mathbb{B}}$, and its $\mu$-th column is the coordinate column of $[\tilde Q, e_\mu]$; that is the precise sense in which left and right differ because the algebra is non-commutative.

The regular module is $\mathbb{B} = I_1 \oplus I_2$ with $I_1 = \mathbb{B}\tilde\Pi_+$, $I_2 = \mathbb{B}\tilde\Pi_-$ and $\tilde\Pi_+ = \tfrac{1}{2}(e_t + i\vec e_z)$, $\tilde\Pi_- = \tfrac12(e_t - i\vec e_z)$; in the adapted basis $\tilde\Pi_+, \vec e_x\tilde\Pi_+, \tilde\Pi_-, \vec e_x\tilde\Pi_-$ the left regular matrix is diagonal over the two invariant subspaces $I_1$, $I_2$, each a copy of the simple module $V$. So the regular module is $V \oplus V$, the regular representation is reducible, and it is the first reducible realization of this subcategory. The centralizer of $\mathsf{M}_4^{L}(\mathbb{B})$ is the right copy $\mathsf{M}_4^{R}(\mathbb{B})$, of complex dimension $4$. Over $\mathbb{R}$ the left regular matrix is $8 \times 8$ real with $\det = |N|^4$ and trace $8\operatorname{Re}(Q_t)$, the dimension doubling by restriction of scalars. The Hermitian sandwich $\tilde Q_4 \mapsto \tilde Q\tilde Q_4\tilde Q^{*}$ has the matrix $\mathsf{H}_{\tilde Q} = \mathsf{M}_4^{L}(\tilde{Q})\,\mathsf{M}_4^{R}(\tilde{Q}^{*}) = \mathsf{M}_4^{L}(\tilde{Q})\,D\,\mathsf{M}_4^{L}(\tilde{Q})^{*}\,D$, a congruence and not a similarity; its realification has $\det = |N|^{8}$ and trace $8|Q_t|^{2}$.

A second $4 \times 4$ realization, the one used in the literature on eigenvector bundles, is equivalent to the regular one as a module — every faithful four-dimensional complex realization is $V \oplus V$ — and it carries a multiplicative quadratic map $m(A) = A A^{\natural} = \Delta(A) I$ of the algebra into the scalar matrices, $\Delta = A_t^2 - A_x^2 - A_y^2 - A_z^2$, which is a real quadratic map on the real coefficients and which the regular realization does not have, in contrast with the congruence-shaped quadratic map of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*. Its real slice $e_t, i\vec e_x, i\vec e_y, i\vec e_z$ carries the Minkowski form $D = \operatorname{diag}(-1,1,1,1)$, of signature $(1,3)$, for which the three generators are the infinitesimal generators of $O(1,3)$, $M^{\mathsf T} = -DMD$; this is the form of the realization's real slice and must be distinguished from the general quaternionic bilinear form of signature $(4,4)$, which is the form of the eight-dimensional algebra. In that realization the sixteen products $\mathsf{M}_4^{L}(e_\mu)\mathsf{M}_4^{R}(e_\nu)$ are the Hermitian outer products $E_\mu E_\nu^{\mathsf T}$ and form a basis of $M_4(\mathbb{C})$ orthogonal for the trace, $\operatorname{tr}(P_{\mu\nu}P_{\lambda\rho}) = 4\delta_{\mu\lambda}\delta_{\nu\rho}$; the expansion it gives is the tensor-square reading of the double centralizer, and it says that every complex matrix is a biparavector, $\sum a_{\mu\nu}\,\mathsf{M}_4^{L}(e_\mu)\mathsf{M}_4^{R}(e_\nu)$.

Read as a pairing, the regular matrix carries the general plain bilinear form with the normalisation of its size: $\langle\tilde Q_1,\tilde Q_2\rangle=\tfrac14\operatorname{Tr}(\mathsf{M}_4^{L}(\tilde Q_1)\mathsf{M}_4^{L}(\tilde Q_2))$, of Gram matrix $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$, of signature $(4,4)$ on the eight real coordinates, isotropic on the cone $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ of real dimension $6$ — the same cone as in the $2\times2$ model — with automorphism group $O_4(\mathbb{C})$ and the real forms $O(4)$, $O(1,3)$ and $O(4,4)$. The four products are the four words $XY$, $X^{\mathsf T}Y$, $XY^{\dagger}$ and $X^{\mathsf T}Y^{\dagger}$ in the regular matrix and its transpose and dagger, and the four forms are the four quarter-traces $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ in those words.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra |
| $e_t, \vec e_x, \vec e_y, \vec e_z$ | Algebra basis, $e_t = 1$, $\vec e_\lambda^2 = -e_t$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu$ | Developed form, $Q_\mu \in \mathbb{C}$ |
| $Q^\mu = (Q^0, Q^1, Q^2, Q^3)$ | Four-vector; $Q^0 = Q_t$, $(Q^1, Q^2, Q^3) = (Q_x, Q_y, Q_z)$ |
| $\operatorname{col}(\tilde Q_5)$ | Coordinate column of $\tilde Q_5$ in the basis $e_t, \vec e_x, \vec e_y, \vec e_z$ |
| $\mathsf{M}_4^{L}(\tilde{Q})$ | Left regular matrix, whose $\mu$-th column is $\operatorname{col}(\tilde Q e_\mu)$; written $\mathsf{M}_4(\tilde{Q})$ in the shorter notation |
| $\mathsf{M}_4^{R}(\tilde{Q})$ | Right regular matrix, whose $\mu$-th column is $\operatorname{col}(e_\mu \tilde Q)$ |
| $D = \operatorname{diag}(-1,1,1,1)$ | Fixed sign matrix of the transposition theorem, $\mathsf{M}_4^{R}(\tilde{Q}) = D\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}}D$, and matrix of the Minkowski form of the second realization, $M^{\mathsf T} = -DMD$ |
| $\langle\tilde{Q}\rangle_{\natural} = \sum_\mu Q_\mu^2$ | The norm; $\det\mathsf{M}_4^{L}(\tilde{Q}) = \langle\tilde{Q}\rangle_{\natural}^2$ |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ | Quaternion, complex, Hermitian and anti-Hermitian conjugations |
| $\mathbb{C}_{\mathbb{B}}$ | Centre, the scalar subspace $\mathbb{C} e_t$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subalgebra; its restriction carries the quaternion regular representation of *Quaternion Element Representations* |
| $\tilde\Pi_+ = \tfrac{1}{2}(e_t + i\vec e_z)$, $\tilde\Pi_- = \tfrac12(e_t - i\vec e_z)$ | Orthogonal idempotents, $\tilde\Pi_+ + \tilde\Pi_- = e_t$, $\tilde\Pi_+\tilde\Pi_- = 0$ |
| $I_1 = \mathbb{B}\tilde\Pi_+$, $I_2 = \mathbb{B}\tilde\Pi_-$ | The two minimal left ideals, $\mathbb{B} = I_1 \oplus I_2$ |
| $V = \mathbb{C}^2$ | Simple left $\mathbb{B}$-module, complex dimension $2$ |
| $\mathbb{B}^{\mathrm{opp}}$ | Opposite algebra; the right regular matrix is a homomorphism from it |
| $\epsilon^{ijk}$ | Levi-Civita symbol on the indices $1, 2, 3$ |
| $\operatorname{Res}_{\mathbb{C}/\mathbb{R}}$ | Restriction of scalars |
| $\operatorname{cent}_{M_4(\mathbb{C})}\mathsf{M}_4^{L}(\mathbb{B}) = \mathsf{M}_4^{R}(\mathbb{B})$ | The centralizer of the left image is the right copy, of complex dimension $4$ |
| $\mathsf{M}_4^{L,\mathbb{R}}(\tilde{Q})$ | Real $8 \times 8$ left regular matrix |
| $\mathsf{H}_{\tilde Q} = \mathsf{M}_4^{L}(\tilde{Q})\mathsf{M}_4^{R}(\tilde{Q}^{*})$ | The sandwich matrix, carrying $\operatorname{col}(\tilde Q_4)$ to $\operatorname{col}(\tilde Q\tilde Q_4\tilde Q^{*})$; closed form $\mathsf{M}_4^{L}(\tilde{Q})D\mathsf{M}_4^{L}(\tilde{Q})^{*}D$, realification with $\det = \lvert N\rvert^{8}$ and trace $8\lvert Q_t\rvert^{2}$ |
| $\mathsf{M}'_4(A_t, A_x, A_y, A_z)$ | Second $4 \times 4$ realization, on the generators $i\vec e_x, i\vec e_y, i\vec e_z$ with $(i\vec e_x)^2 = (i\vec e_y)^2 = (i\vec e_z)^2 = e_t$ |
| $K_1, K_2, K_3$ | Coefficient conjugates of $i\vec e_x, i\vec e_y, i\vec e_z$, used in the Hermitian basis of that realization |
| $\langle\tilde Q_1,\tilde Q_2\rangle=\tfrac14\operatorname{Tr}(XY)$, Gram $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$ | the general plain bilinear form read in the regular model, $X=\mathsf{M}_4^{L}(\tilde Q_1)$, $Y=\mathsf{M}_4^{L}(\tilde Q_2)$; $\mathrm{E}=-D$; signature $(4,4)$ on the eight real coordinates |
| $\tfrac14\operatorname{Tr}(X^{\mathsf T}Y)=N$, $\tfrac14\operatorname{Tr}(XY^{\dagger})=H$, $\tfrac14\operatorname{Tr}(X^{\mathsf T}Y^{\dagger})=K$ | the quaternionic bilinear, the plain sesquilinear and the quaternionic sesquilinear form as quarter-traces, in the four words of the realization |
| $O_4(\mathbb{C})$, $O(4)$, $O(1,3)$, $O(4,4)$ | the automorphism group of the trace pairing over $\mathbb{C}$, of complex dimension $6$, and its real forms, with the $O(4,4)$ of the realified form |
| $m(A) = A A^{\natural} = \Delta(A)I$ | The multiplicative map, $I + \mathbb{B} \to M_4(\mathbb{C})$; $\Delta = A_t^2 - A_x^2 - A_y^2 - A_z^2$, a real matrix for real coefficients, multiplicative |
| $\mathfrak{o}(1,3)$ | Lie algebra of $O(1,3)$, $\{M : M^{\mathsf T}D + DM = 0\}$, to which the generators $i\vec e_\lambda$ belong |
| $P_{\mu\nu} = \mathsf{M}_4^{L}(e_\mu)\mathsf{M}_4^{R}(e_\nu) = E_\mu E_\nu^{\mathsf T}$ | The sixteen products; an orthogonal basis of $M_4(\mathbb{C})$, $\operatorname{tr}(P_{\mu\nu}P_{\lambda\rho}) = 4\delta_{\mu\lambda}\delta_{\nu\rho}$ |
| $\sum a_{\mu\nu}\,e_\mu \otimes e_\nu$ | Biparavector, whose matrix is $\sum a_{\mu\nu}\,P_{\mu\nu}$ |
| $\mathbb{M}_+$ | Hermitian subspace of real dimension $4$ |

## Further Reading


- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the regular representation of an algebra and the identification of its centralizer.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Interscience, 1962), for the regular module, its decomposition into minimal left ideals and the double centralizer theorem.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules*, 2nd edition (Springer, 1992), for the regular module as a left module over itself and the centralizer of the left copy.
- William Fulton and Joe Harris, *Representation Theory: A First Course*, Graduate Texts in Mathematics 129 (Springer, 1991), for the regular representation as the direct sum of the simple modules with multiplicity equal to their dimensions.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for the regular representation of a quaternion algebra and its complexification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the Cayley matrix of quaternion multiplication and its transpose.
- D. H. Gottlieb, "Eigenbundles, Quaternions, and Berry's Phase," arXiv:math/0304281 [math.AT] (2003), for the second $4 \times 4$ realization and the map $m(A) = A A^{\natural}$ of the section above; the paper's $4 \times 4$ matrices are Example 5 and the map $m(A) = A A^{\natural}$ is its section 5.
- D. H. Gottlieb, "Maxwell's equations" (1 August 2004, 12 pp.), for the matrix formulation of Maxwell's equations in which the field matrix is $A_t I + cF$ of the realization above, the dual form in which the derivatives stand in the matrix and the field in the column, and the identity $\mathsf{M}'^{R}_4 = \mathsf{M}'_4{}^{\mathsf{T}}$ which holds there without a sign matrix; cited for the identification of the second realization with the matrices of the Maxwell literature and for the transposition remark of that section. Its section 5 is the source of the sixteen-product basis and the biparavectors of the section above: the coefficient formula $a_{\mu\nu} = \tfrac14\operatorname{tr}(ME_\mu E_\nu^{\mathsf{T}})$, the orthogonality of the basis for the trace, and the reading of the products as the tensor square of the algebra acting on itself on both sides. The paper's potential-level equations (13) and (14) are recorded in *Maxwell's Equations in Biquaternionic Form* with their vector parts corrected.

- A. Gsponer, "Explicit closed-form parametrization of SU(3) and SU(4) in terms of complex quaternions and elementary functions," arXiv:math-ph/0211056v2, 2002, §2–4, for the Conway operators $\vec e_\nu[\,]\vec e_\mu$, the composition and association rules, the functions $A\{a\}$, $D\{d\}$, $S\{s\}$ and their $4\times4$ matrix displays (10′)–(13′), the rule $G^{-1}=G^{+\approx}=G^{\dagger}$ for the group elements, and the remark that the quaternion method loses power from three to four dimensions.
- A. W. Conway, "Quaternions and matrices," *Proceedings of the Royal Irish Academy* **A 50** (1945) 98–130, and J. L. Synge, "Quaternions, Lorentz transformations, and the Conway–Dirac–Eddington matrices," *Communications of the Dublin Institute for Advanced Studies* **A 21** (1972), for the Conway operator calculus in its original form.
