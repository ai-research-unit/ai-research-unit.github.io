# __Introduction to the 4×4 Matrix Representation $M_4(\mathbb{C})_L$ of Biquaternions__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the four-dimensional complex algebra with basis $e_0=1,e_1,e_2,e_3$, where $e_k^2=-e_0$ and $e_je_k=-e_ke_j$ for $j\neq k$, and with a central scalar imaginary $i$; a general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The four coefficients are the coordinates of *Biquaternions as a Vector Space over $\mathbb{C}$*, and the six distinguished subspaces are those of *Introduction to the Six Subspaces*.

This article is the first reading of the **regular representation**: the algebra acting on itself on the left, and the $4\times4$ matrix of that action in the coefficient basis. It belongs to the linear algebra of the algebra, beside the $2\times2$ reading of *Introduction to the 2×2 Matrix Representation of Biquaternions*: where the $2\times2$ realization exhibits the algebra inside $M_2(\mathbb{C})$, the regular realization writes the multiplication itself as a matrix, and the six distinguished subspaces reappear as six matrix conditions. It is the first realization of the algebra that is reducible, the coefficient space splitting into two copies of the simple module.

This article owns the operator, its matrix in the basis, the multiplicativity, the **determinant** and the **trace**, the six subspace conditions, and the comparison with the $2\times2$ model. The further development — the right multiplication, the transposition relation between the two representations, the module structure and the decomposition, the double centralizer, the $8\times8$ real form and the second realization — is *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*.

## The Regular Representation

**Definition.** The **left regular matrix** is the isomorphism written $\mathsf{M}_4$. It converts a biquaternion into a $4 \times 4$ complex matrix,

$$
\mathsf{M}_4:\mathbb{B}\longrightarrow M_4(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity. The quaternion units are assigned the matrices

$$
\mathsf{M}_4(e_0)=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\quad
\mathsf{M}_4(e_1)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\quad
\mathsf{M}_4(e_2)=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\quad
\mathsf{M}_4(e_3)=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix},
$$

with $\mathsf{M}_4(ie_\mu)=i\,\mathsf{M}_4(e_\mu)$ on the central scalar $\mathbb{C}_{\mathbb{B}}$.

A general biquaternion $\tilde Q=\sum_\mu Q_\mu e_\mu$ therefore maps to

$$
\mathsf{M}_4(\tilde Q)=
\begin{pmatrix}
Q_0&-Q_1&-Q_2&-Q_3\\
Q_1&Q_0&-Q_3&Q_2\\
Q_2&Q_3&Q_0&-Q_1\\
Q_3&-Q_2&Q_1&Q_0
\end{pmatrix}.
$$

Each entry is a single coefficient of $\tilde Q$ carrying a sign, and **no entry is a sum of two or more coefficients**, because in this basis each product of basis elements is one basis element times a sign. The first column is the four-vector $(Q_0,Q_1,Q_2,Q_3)$ of $\tilde Q$.

**Proof (the general matrix).** The columns are the products $\tilde Qe_m$ written in the basis. For $m=0$ the image is $\tilde Q$, giving the first column. For $m=k\geq1$, using $e_je_k=\epsilon^{ijk}e_i$ for $j\neq k$, one gets $\tilde Qe_k=Q_0e_k-Q_ke_0+\sum_{j\neq k}\epsilon^{ijk}Q_je_i$, and expanding with $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$ gives the displayed columns.

**The check.** The assignment is the right one because the four matrices multiply as the four units do. Squaring a vector image,

$$
\mathsf{M}_4(e_1)^2=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}^2=\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&0&-1\end{pmatrix}=-\mathsf{M}_4(e_0),
$$

and the same holds for $\mathsf{M}_4(e_2)$ and $\mathsf{M}_4(e_3)$; so $e_k^2=-e_0$ is reproduced. Multiplying the first two,

$$
\mathsf{M}_4(e_1)\mathsf{M}_4(e_2)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}=\mathsf{M}_4(e_3),
$$

and the other products give $\mathsf{M}_4(e_2)\mathsf{M}_4(e_3)=\mathsf{M}_4(e_1)$ and $\mathsf{M}_4(e_3)\mathsf{M}_4(e_1)=\mathsf{M}_4(e_2)$, reproducing $e_1e_2=e_3$ with its cyclic companions; reversing the order of the factors reverses the sign of each product, reproducing $e_ie_j=-e_je_i$ for $i\neq j$. Those relations are the whole multiplication table of the units, so the correspondence of bases is an isomorphism of algebras and not a formal analogy. Write $\operatorname{col}(\tilde S)$ for the coordinate column of $\tilde S$; then the matrix acts on columns by $\mathsf{M}_4(\tilde Q)\operatorname{col}(\tilde S)=\operatorname{col}(\tilde Q\tilde S)$, which is the column convention of *The Four-Vector Element Representation of Biquaternions*.

**Remark (the same four for a different reason).** The matrix above is $4\times4$, and the coefficient space of *The Four-Vector Element Representation of Biquaternions* has complex dimension $4$. These are the same four for the same reason and not by coincidence: the algebra has complex dimension $4$ and the regular representation is the algebra acting on itself, so the space and the index set of the matrix are the same object.

**Example.** For $\tilde{Q}=(2+i)e_0+(1-i)e_1+3e_2+ie_3$ the regular matrix is

$$
\mathsf{M}_4(\tilde{Q})=\begin{pmatrix}
2+i&-1+i&-3&-i\\
1-i&2+i&-i&3\\
3&i&2+i&-1+i\\
i&-3&1-i&2+i
\end{pmatrix}.
$$

The column of $\tilde{R}=e_0+e_1$, namely $R=(1,1,0,0)$, is carried to the column $(1+2i,3,3+i,-3+i)$, which is the four-vector of the product $\tilde{Q}\tilde{R}$ computed by the component formula of *The Four-Vector Element Representation of Biquaternions*.

## The Representation Is a Homomorphism

**Theorem (multiplicativity).** For all $\tilde Q,\tilde R\in\mathbb{B}$, $\mathsf{M}_4(\tilde Q)\mathsf{M}_4(\tilde R)=\mathsf{M}_4(\tilde Q\tilde R)$. Hence $\mathsf{M}_4$ is an algebra homomorphism, and the coefficient space is a left $\mathbb{B}$-module under it.

**Proof.** Both sides are computed on the basis: for every $m$, associativity gives $\tilde Q(\tilde Re_m)=(\tilde Q\tilde R)e_m$, so the two matrices agree on every column $\operatorname{col}(e_m)$ and hence everywhere. $\square$

**Corollary (injectivity).** The map $\mathsf{M}_4$ is injective, so the algebra is realized faithfully; indeed $\mathsf{M}_4(\tilde Q)=0$ forces its first column, which is the column of $\tilde Q$, to vanish, and the first column alone recovers the four coefficients.

The two orders differ, and the example $\tilde Q=e_0+e_1$, $\tilde R=e_0+e_2$ shows it: the products $\tilde Q\tilde R=e_0+e_1+e_2+e_3$ and $\tilde R\tilde Q=e_0+e_1+e_2-e_3$ have first columns $(1,1,1,1)$ and $(1,1,1,-1)$, so $\mathsf{M}_4(\tilde Q)\mathsf{M}_4(\tilde R)\neq\mathsf{M}_4(\tilde R)\mathsf{M}_4(\tilde Q)$, exactly as $\tilde Q\tilde R\neq\tilde R\tilde Q$.

## The Determinant and the Trace

**Proposition (determinant and trace).** For every biquaternion $\tilde Q$, writing $\Delta(\tilde Q)$ for the determinant of its $2\times2$ matrix,

$$
\det\mathsf{M}_4(\tilde Q)=\Delta(\tilde Q)^2,\qquad \operatorname{Tr}\mathsf{M}_4(\tilde Q)=4Q_0,\qquad \Delta(\tilde Q)=Q_0^2+Q_1^2+Q_2^2+Q_3^2 .
$$

The determinant of the regular matrix is the **square** of the determinant of the $2\times2$ model, and it is not that determinant itself.

**Proof.** Write $A=\Phi(\tilde Q)$, so that $A$ is the matrix of $\tilde Q$ of *Introduction to the 2×2 Matrix Representation of Biquaternions*, of trace $2Q_0$ and determinant $\Delta(\tilde Q)$. The map $\mathsf{M}_4(\tilde Q)$ is left multiplication by $A$ on $M_2(\mathbb{C})$, and in the basis of $M_2(\mathbb{C})$ grouped by columns that operator is block diagonal with two copies of $A$, because $A(Xe_j)=(AX)e_j$ for each column $Xe_j$. The trace and the determinant of a block diagonal matrix are the sum and the product of those of the blocks, so $\operatorname{Tr}\mathsf{M}_4(\tilde Q)=2\operatorname{Tr}A=4Q_0$ and $\det\mathsf{M}_4(\tilde Q)=\det(A)^2=\Delta(\tilde Q)^2$. $\square$

**Example.** For $\tilde{Q}=(2+i)e_0+(1-i)e_1+3e_2+ie_3$ the $2\times2$ determinant is $\Delta(\tilde Q)=11+2i$, hence $\det\mathsf{M}_4(\tilde Q)=(11+2i)^2=117+44i$ and $\operatorname{Tr}\mathsf{M}_4(\tilde Q)=4(2+i)=8+4i$.

**Remark (the determinant is not the $2\times2$ determinant).** The difference from the $2\times2$ model is a genuine feature of the regular representation: its carrier has twice the dimension of the simple module, so the two-copy structure doubles the trace and squares the determinant. Each block carries $\Delta(\tilde Q)$ as its determinant and $2Q_0$ as its trace.

## The Six Subspaces in the Regular Model

The six distinguished subspaces have the following images under $\mathsf{M}_4$, read from the matrix. Each row records the image of the subspace.

| Subspace | Image under $\mathsf{M}_4$ | Description |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\{A I_4:A\in\mathbb{C}\}$ | the scalar matrices |
| $\mathrm{Vect}(\mathbb{B})$ | $\{M:\operatorname{Tr}M=0\}$ | the traceless matrices |
| $\mathbb{H}_{\mathbb{B}}$ | the real matrices | the quaternion subspace is the real part of the realization |
| $i\mathbb{H}_{\mathbb{B}}$ | the purely imaginary matrices | $i$ times the real matrices |
| $\mathbb{M}_+$ | $\{M:M=M^\dagger\}$ | the Hermitian matrices |
| $\mathbb{M}_-$ | $\{M:M=-M^\dagger\}$ | the anti-Hermitian matrices |

Here $\dagger$ is the conjugate transpose, and a matrix is Hermitian or anti-Hermitian in the ordinary sense.

**Proof.** A central element is $\tilde Q=Ae_0$, and $\mathsf{M}_4(Ae_0)=AI_4$ because $e_0$ is the identity. The trace of the matrix is $4Q_0$, so the traceless matrices are exactly the elements with vanishing scalar part, that is the vector subspace. For the quaternion subspace the coefficients $Q_\mu=h_\mu$ are real, and each entry of the matrix is a single coefficient up to sign, so the image is the set of real matrices; the anti-quaternion subspace, whose coefficients are purely imaginary, is its $i$-multiple, the purely imaginary matrices. Finally $\mathsf{M}_4(e_k)$ is real and skew-symmetric, so for a Hermitian element, whose scalar part is real and whose vector coefficients are purely imaginary, the image $q_0I_4+\sum_k iq'_k\mathsf{M}_4(e_k)$ is a real scalar matrix plus a purely imaginary skew matrix, which is Hermitian; the anti-Hermitian element gives the negative pattern. $\square$

The table is the matrix reading of the linear-spaces picture, and it is visibly different from the $2\times2$ one: in the regular model the quaternion and anti-quaternion subspaces are the real and the purely imaginary matrices, an entrywise condition, whereas in the $2\times2$ model the same two subspaces are the $\epsilon$-conjugation pattern and its $i$-multiple. The two models agree on the centre, the vector subspace and the two Hermitian subspaces.

### Explicit Patterns and Invariants

Read from the matrix above, each of the six subspaces has a fixed pattern. With $Q_\mu=q_\mu+iq'_\mu$,

**The centre.** For $\tilde Q=Q_0e_0$ the matrix is scalar,

$$
\mathsf{M}_4(Q_0e_0)=\begin{pmatrix}Q_0&0&0&0\\0&Q_0&0&0\\0&0&Q_0&0\\0&0&0&Q_0\end{pmatrix}=Q_0I_4,\qquad \operatorname{Tr}=4Q_0,\quad \det=Q_0^4 .
$$

**The vector subspace.** For $\tilde Q=\mathbf P=P_1e_1+P_2e_2+P_3e_3$ the matrix is traceless,

$$
\mathsf{M}_4(\mathbf P)=\begin{pmatrix}0&-P_1&-P_2&-P_3\\P_1&0&-P_3&P_2\\P_2&P_3&0&-P_1\\P_3&-P_2&P_1&0\end{pmatrix},\qquad \operatorname{Tr}=0,\quad \det=\bigl(P_1^2+P_2^2+P_3^2\bigr)^2 .
$$

**The quaternion subspace.** For $\tilde Q=h=h_0e_0+h_1e_1+h_2e_2+h_3e_3$ with $h_\mu\in\mathbb{R}$ the matrix is real,

$$
\mathsf{M}_4(h)=\begin{pmatrix}h_0&-h_1&-h_2&-h_3\\h_1&h_0&-h_3&h_2\\h_2&h_3&h_0&-h_1\\h_3&-h_2&h_1&h_0\end{pmatrix},\qquad \operatorname{Tr}=4h_0,\quad \det=\bigl(h_0^2+h_1^2+h_2^2+h_3^2\bigr)^2>0 .
$$

**The anti-quaternion subspace.** For $\tilde Q=ih$ with $h$ real the matrix is $i$ times the preceding one, and purely imaginary,

$$
\mathsf{M}_4(ih)=i\,\mathsf{M}_4(h)=\begin{pmatrix}ih_0&-ih_1&-ih_2&-ih_3\\ih_1&ih_0&-ih_3&ih_2\\ih_2&ih_3&ih_0&-ih_1\\ih_3&-ih_2&ih_1&ih_0\end{pmatrix},\qquad \operatorname{Tr}=4ih_0,\quad \det=\bigl(h_0^2+h_1^2+h_2^2+h_3^2\bigr)^2>0 .
$$

**The Hermitian subspace.** For $\tilde Q=a_0e_0+i\mathbf p$ with $a_0$ real and $\mathbf p$ a real vector the matrix is Hermitian,

$$
\mathsf{M}_4(\tilde Q)=\begin{pmatrix}a_0&-ip_1&-ip_2&-ip_3\\ip_1&a_0&-ip_3&ip_2\\ip_2&ip_3&a_0&-ip_1\\ip_3&-ip_2&ip_1&a_0\end{pmatrix}=\mathsf{M}_4(\tilde Q)^\dagger,\qquad \operatorname{Tr}=4a_0,\quad \det=\bigl(a_0^2-p_1^2-p_2^2-p_3^2\bigr)^2 .
$$

**The anti-Hermitian subspace.** For $\tilde Q=ib_0e_0+\mathbf q$ with $b_0$ real and $\mathbf q$ a real vector the matrix is anti-Hermitian,

$$
\mathsf{M}_4(\tilde Q)=\begin{pmatrix}ib_0&-q_1&-q_2&-q_3\\q_1&ib_0&-q_3&q_2\\q_2&q_3&ib_0&-q_1\\q_3&-q_2&q_1&ib_0\end{pmatrix}=-\mathsf{M}_4(\tilde Q)^\dagger,\qquad \operatorname{Tr}=4ib_0,\quad \det=\bigl(q_1^2+q_2^2+q_3^2-b_0^2\bigr)^2 .
$$

The trace is the scalar part times four in every case, so it separates the centre from the vector subspace and sees nothing else. The determinant is the square of the $2\times2$ determinant of the same element in every case; on the quaternion subspace that $2\times2$ determinant is a sum of four real squares, strictly positive, so no element there is singular, and on the anti-quaternion subspace it is the negative of that sum, strictly negative, so it is the $2\times2$ model and not the regular one that sees the sign the subspace carries, the regular square being positive in both cases. The two models are set side by side in the next section.

## The Two Models Compared

The $2\times2$ realization $\Phi$ of *Introduction to the 2×2 Matrix Representation of Biquaternions* and the regular realization $\mathsf{M}_4$ above are the two basic matrix models of $\mathbb{B}$. Both are injective and multiplicative, so both see the six distinguished subspaces, and the same six matrix conditions describe them in both; the invariant columns give, first, the value in the $2\times2$ model and, second, the value in the regular model. Here $\Delta=\Delta(\tilde Q)=Q_0^2+Q_1^2+Q_2^2+Q_3^2$ is the determinant of the $2\times2$ matrix, a sum of four real squares on the quaternion subspace, the negative of that sum on the anti-quaternion subspace, and real on the two Hermitian subspaces.

| Subspace | Condition in the $2\times2$ model | Condition in the $4\times4$ model | $\operatorname{Tr}\Phi$ / $\operatorname{Tr}\mathsf{M}_4$ | $\det\Phi$ / $\det\mathsf{M}_4$ |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\Phi(\tilde Q)=AI_2$ | $\mathsf{M}_4(\tilde Q)=AI_4$ | $2A$ / $4A$ | $A^2$ / $A^4$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\operatorname{Tr}\Phi(\tilde Q)=0$ | $\operatorname{Tr}\mathsf{M}_4(\tilde Q)=0$ | $0$ / $0$ | $\Delta$ / $\Delta^2$ |
| $\mathbb{H}_{\mathbb{B}}$ | fixed by $M\mapsto\epsilon\overline M\epsilon^{-1}$ | the real matrices | $2h_0$ / $4h_0$ | $\Delta>0$ / $\Delta^2$ |
| $i\mathbb{H}_{\mathbb{B}}$ | anti-fixed by the same map | the purely imaginary matrices | $2ih_0$ / $4ih_0$ | $\Delta<0$ / $\Delta^2$ |
| $\mathbb{M}_+$ | $\Phi(\tilde Q)^\dagger=\Phi(\tilde Q)$ | $\mathsf{M}_4(\tilde Q)^\dagger=\mathsf{M}_4(\tilde Q)$ | $2a_0$ / $4a_0$ | $\Delta$ real / $\Delta^2$ |
| $\mathbb{M}_-$ | $\Phi(\tilde Q)^\dagger=-\Phi(\tilde Q)$ | $\mathsf{M}_4(\tilde Q)^\dagger=-\mathsf{M}_4(\tilde Q)$ | $2ib_0$ / $4ib_0$ | $\Delta$ real / $\Delta^2$ |

Here $\epsilon=i\sigma_2$, and the two middle rows are the only ones that look different: the four entries of the $2\times2$ matrix are four $\mathbb{C}$-linear combinations of the four coefficients, so realness of the coefficients is not realness of the entries, whereas the entries of the regular matrix are the coefficients up to sign.

**Theorem (the regular matrix is two copies of the $2\times2$ matrix).** Let $\tilde\Pi=\tfrac12(e_0+ie_1)$ and $f=e_0-\tilde\Pi$, so that $\mathbb{B}=\mathbb{B}\tilde\Pi\oplus\mathbb{B}f$ splits into two minimal left ideals, and let $\tilde R=e_3+ie_2$, $\tilde T=e_3-ie_2$. In the basis $\tilde\Pi,\tilde R,f,\tilde T$ the regular matrix is block diagonal,

$$
\mathsf{M}_4(\tilde Q)=\begin{pmatrix}A_+&0\\0&A_-\end{pmatrix},\qquad A_+\text{ and }A_-\text{ conjugate to }\Phi(\tilde Q),
$$

and each block has trace $2Q_0$ and determinant $\Delta(\tilde Q)$.

**Proof.** Left multiplication preserves each left ideal, so the matrix is block diagonal in a basis adapted to the splitting. Each block is left multiplication by $\tilde Q$ on a minimal left ideal, every minimal left ideal is isomorphic to the simple module $V=\mathbb{C}^2$, and on $V$ left multiplication is $\Phi(\tilde Q)$; a change of basis inside the block replaces it by a conjugate matrix, which has the same trace and determinant. $\square$

**Corollary.** $\operatorname{Tr}\mathsf{M}_4(\tilde Q)=2\operatorname{Tr}\Phi(\tilde Q)=4Q_0$ and $\det\mathsf{M}_4(\tilde Q)=\det\Phi(\tilde Q)^2$: the factor two in the trace and the square in the determinant are one block decomposition and not two coincidences. In both models the trace is the scalar part times the size of the matrix, so it separates the centre from the vector subspace and sees nothing else.

**Remark (the one place the two models see different signs).** The $2\times2$ determinant is $\Delta$ and the regular determinant is $\Delta^2$. On the anti-quaternion subspace the first is $-(h_0^2+h_1^2+h_2^2+h_3^2)<0$ and the second is positive, so the $2\times2$ model sees that $i\mathbb{H}_{\mathbb{B}}$ is the negative-definite half of the coefficient space, while the regular model, whose determinant is blind to the sign, does not; this is the only place where the two models disagree. On the quaternion subspace both determinants are strictly positive, nothing there is singular, which is the matrix statement that the quaternion subspace carries no zero divisor and is the largest of the six with that property. The centre is the only one of the six whose image is scalar matrices in both models, and a scalar matrix $AI$ is singular only at $A=0$, so the centre contains no singular matrix but the zero one. The vector units explain the two Hermitian rows: $\Phi(e_k)$ is $-i$ times a Hermitian (Pauli) matrix, whereas $\mathsf{M}_4(e_k)$ is real and skew-symmetric, so $i\mathsf{M}_4(e_k)$ is Hermitian, and in both models a Hermitian element has a Hermitian image.

## Summary

The left regular representation $\mathsf{M}_4$ sends $\tilde Q$ to the matrix of left multiplication by $\tilde Q$ in the coefficient basis, a matrix whose entries are the four coefficients up to sign and whose first column is the four-vector of $\tilde Q$. It is an injective algebra homomorphism, so $\mathsf{M}_4(\tilde Q)\mathsf{M}_4(\tilde R)=\mathsf{M}_4(\tilde Q\tilde R)$. The trace of the matrix is $4Q_0$ and the determinant is the square of the $2\times2$ determinant of the same element, the doubled trace and the squared determinant of the $2\times2$ model. The six distinguished subspaces become six matrix conditions: scalar, traceless, real, purely imaginary, Hermitian and anti-Hermitian matrices, the same six that hold in the $2\times2$ model, the two differing only in that the $2\times2$ determinant sees the sign on the anti-quaternion subspace while the regular one sees only its square. The right multiplication, the transposition relation, the module decomposition, the double centralizer, the $8\times8$ real form and the second realization are the further development and belong to *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde Q)\operatorname{col}(\tilde R)=\operatorname{col}(\tilde Q\tilde R)$ | the left regular matrix |
| $M_4(\mathbb{C})_L=\operatorname{image}\mathsf{M}_4=\{\mathsf{M}_4(\tilde Q)\}$ | the regular matrices, the subspace of complex dimension $4$ inside $M_4(\mathbb{C})$ |
| $\mathsf{M}_4(\tilde Q)=\begin{pmatrix}Q_0&-Q_1&-Q_2&-Q_3\\Q_1&Q_0&-Q_3&Q_2\\Q_2&Q_3&Q_0&-Q_1\\Q_3&-Q_2&Q_1&Q_0\end{pmatrix}$ | its matrix in the basis $e_0,e_1,e_2,e_3$ |
| $\mathsf{M}_4(\tilde Q)\mathsf{M}_4(\tilde R)=\mathsf{M}_4(\tilde Q\tilde R)$ | multiplicativity |
| $\operatorname{Tr}\mathsf{M}_4(\tilde Q)=4Q_0$ | the trace |
| $\Delta(\tilde Q)=Q_0^2+Q_1^2+Q_2^2+Q_3^2$ | the determinant of the $2\times2$ matrix of $\tilde Q$ |
| $\det\mathsf{M}_4(\tilde Q)=\Delta(\tilde Q)^2$ | the determinant, the square of the $2\times2$ determinant |
| $(Q_0,Q_1,Q_2,Q_3)$ | the first column, the four-vector of $\tilde Q$ |
| $\tilde\Pi=\tfrac12(e_0+ie_1)$, $f=e_0-\tilde\Pi$ | orthogonal idempotents splitting $\mathbb{B}$ into two minimal left ideals |
| $\tilde R=e_3+ie_2$, $\tilde T=e_3-ie_2$ | the nilpotent generators of the two ideals, the adapted basis $\tilde\Pi,\tilde R,f,\tilde T$ |
| $A_+,A_-$ | the two diagonal blocks of $\mathsf{M}_4$, each conjugate to $\Phi(\tilde Q)$ |

## Further Reading

- *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/the-4x4-matrix-element-representation-of-biquaternions.md`), for the right multiplication, the transposition relation, the module structure and reducibility, the double centralizer, the real form and the second realization
- *Introduction to the 2×2 Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`), for the companion realization, its trace $2Q_0$ and its determinant
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the two minimal left ideals and the Peirce basis used in the block form of the regular matrix
