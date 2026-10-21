# __Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions__

## Introduction

The **2×2 matrix realization** is the form in which a biquaternion is a $2\times2$ complex matrix; it is the form that carries the spin, the qubit, the Bell states, the Dirac equation and the Fock space of the corpus. Algebraically, the algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is isomorphic, as a complex algebra, to the algebra of $2 \times 2$ complex matrices,

$$
\mathbb{B} \cong M_2(\mathbb{C}),
$$

and the isomorphism is written $\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C})$ throughout. A biquaternion and a $2 \times 2$ complex matrix are the same object written twice, and this is the form in which every statement about the algebra becomes an arithmetic check: the trace reads off the scalar part, the determinant **is** the biquaternion norm, invertibility becomes non-vanishing determinant, the Hermitian subspace becomes the Hermitian matrices, and the minimal left ideals become the matrix columns.

The article supplies the $2 \times 2$ matrices that carry a single chirality, that is, the simple module $S = \mathbb{C}^2$ on which the algebra acts irreducibly. Its coefficient space is that of *The Four-Vector Element Representation of Biquaternions*, the left multiplication written on that space is that of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*, and that representation is the direct sum $S \oplus S$ of two copies of the simple module treated here. The article states the assignment, checks that the four basis matrices multiply as the four units do, notes why the signs cannot be chosen differently, and reads off the invariants, the remarkable subspaces, the two ideals as columns, the conjugations, and the spin and qubit structures. Two further sections read the product and the form in the model: §*The General Plain Bilinear Form in the Model*, for the trace pairing, its Gram matrix, its isotropic cone and its automorphism group, and §*The Four Words and the Four Traces*, for the four products as four words in the matrix and its two involutions and for the four forms as four traces.

The assignment is fixed here. It is not free: it is used identically by the spin, qubit, Bell-state, Dirac and Fock-space articles, and the two conventions a reader is likely to meet elsewhere do not agree with it.

## The Representation

The isomorphism is written $\mathsf{M}_2$. It converts a biquaternion into a $2 \times 2$ complex matrix,

$$
\mathsf{M}_2 : \mathbb{B} \longrightarrow M_2(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity. The scalar imaginary $i$ is the complex unit of the coefficients and is central, so it maps to a scalar matrix; the quaternion units are assigned the matrices

$$
\mathsf{M}_2(e_t) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2, \qquad
\mathsf{M}_2(\vec e_x) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}, \qquad
\mathsf{M}_2(\vec e_y) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad
\mathsf{M}_2(\vec e_z) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix},
$$

with $\mathsf{M}_2(i) = i\,\mathsf{M}_2(e_t)$ on the central scalar $\mathbb{C}_{\mathbb{B}}$.

This is the assignment, taken as fixed for the whole series. A general biquaternion $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$ therefore maps to

$$
\mathsf{M}_2(\tilde{Q}) = Q_t\,\mathsf{M}_2(e_t) + Q_x \mathsf{M}_2(\vec e_x) + Q_y \mathsf{M}_2(\vec e_y) + Q_z \mathsf{M}_2(\vec e_z)
= \begin{pmatrix} Q_t - i Q_z & -i Q_x - Q_y \\ -i Q_x + Q_y & Q_t + i Q_z \end{pmatrix}.
$$

**Remark (the choice, stated).** The assignment above is the corpus's choice, held fixed so that the realization agrees with *The Realification and the Effect of the Change of Scalars*. It is convenient because the three images of $\vec e_x,\vec e_y,\vec e_z$ are $-i$ times the Pauli matrices, mentioned once as a shorthand and nothing more: every proposition is a statement about $\mathbb{B}$ and about $M_2(\mathbb{C})$. The choice is not canonical; a different isomorphism differs from this one by conjugation by an invertible matrix, and the invariants below are unchanged.

**Remark.** The four coefficients and the four matrix entries carry the same data, but the passage between them is not a rearrangement: each entry is a fixed linear combination of two coefficients, with coefficients among $1,-1,i,-i$; the entry $\mathsf{M}_2(\tilde Q)_{12}=-iQ_1-Q_y$ involves two components at once.

**The check.** The assignment is the right one because the four matrices multiply as the four units do. Squaring a vector image,

$$
\mathsf{M}_2(\vec e_x)^2 = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}^2 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -\mathsf{M}_2(e_t),
$$

and the same holds for $\mathsf{M}_2(\vec e_y)$ and $\mathsf{M}_2(\vec e_z)$; so $\vec e_k^2 = -e_t$ is reproduced. Multiplying the first two,

$$
\mathsf{M}_2(\vec e_x)\mathsf{M}_2(\vec e_y) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
= \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} = \mathsf{M}_2(\vec e_z),
$$

and the other products give $\mathsf{M}_2(\vec e_y)\mathsf{M}_2(\vec e_z) = \mathsf{M}_2(\vec e_x)$ and $\mathsf{M}_2(\vec e_z)\mathsf{M}_2(\vec e_x) = \mathsf{M}_2(\vec e_y)$, reproducing $\vec e_x\vec e_y = \vec e_z$ with its cyclic companions; reversing the order of the factors reverses the sign of each product, reproducing $\vec e_\mu \vec e_\nu = -\vec e_\nu \vec e_\mu$ for $\mu \neq \nu$. Those relations are the whole multiplication table of the units, so the correspondence of bases is an isomorphism of algebras and not a formal analogy.

The map is also invertible, which is worth recording explicitly since it is what makes the representation a change of coordinates rather than a forgetful operation. Reading the coefficients back off an arbitrary matrix,

$$
Q_t = \tfrac12(a + d), \qquad Q_x = \tfrac{i}{2}(b + c), \qquad Q_y = \tfrac12(c - b), \qquad Q_z = \tfrac{i}{2}(a - d),
\qquad
\mathsf{M}_2^{-1}\!:\ \begin{pmatrix} a & b \\ c & d \end{pmatrix} \longmapsto Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z ,
$$

so every $2 \times 2$ complex matrix is the image of exactly one biquaternion, and a biquaternion identity holds exactly when the corresponding matrix identity does.

**Theorem.** The map $\mathsf{M}_2$ is an algebra isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$.

**Proof.** The images of $\vec e_x,\vec e_y,\vec e_z$ satisfy the quaternion relations. Each squares to $-I$, since $\mathsf{M}_2(\vec e_x)^2=\mathsf{M}_2(\vec e_y)^2=\mathsf{M}_2(\vec e_z)^2=-I$ by direct computation, and the cyclic products match, $\mathsf{M}_2(\vec e_x)\mathsf{M}_2(\vec e_y)=\mathsf{M}_2(\vec e_z)$ while $\mathsf{M}_2(\vec e_y)\mathsf{M}_2(\vec e_x)=-\mathsf{M}_2(\vec e_z)$. The algebra $\mathbb{B}$ is generated by $\vec e_x,\vec e_y,\vec e_z$ subject only to these relations, so the linear map extending the assignment is multiplicative, hence an algebra homomorphism. It is bijective because the four images are linearly independent in the four-dimensional space $M_2(\mathbb{C})$, and so form a basis.

**Corollary (the centre).** The centre of $M_2(\mathbb{C})$ is the set of scalar matrices $\lambda I$, so the centre of $\mathbb{B}$ is the scalar subspace $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$, and $M_2(\mathbb{C}_{\mathbb{B}})$ is the set of scalar matrices.

**Proof.** A matrix commuting with every matrix is a scalar matrix; transport along $\mathsf{M}_2$.

**Remark (the Pauli matrices).** The three matrices

$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
\sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad
\sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

are the Pauli matrices, and they are the basis images multiplied by the factor $i$. The relation may be read in either direction:

$$
\sigma_k = i\,\mathsf{M}_2(\vec e_k) = \mathsf{M}_2(i\vec e_k),
\qquad\text{equivalently}\qquad
\mathsf{M}_2(\vec e_k) = -i\,\sigma_k .
$$

The factor $i$ is thus all that separates the algebra's own matrices from the ones a physicist writes down, and the form $\sigma_k = \mathsf{M}_2(i\vec e_k)$ states the same relation through the algebra: it is the **Hermitian** quaternion units $i\vec e_k$ whose images are the Hermitian Pauli matrices.

**Remark (other realizations from the null-cone basis).** A second family of $2\times2$ models comes from the **isotropic (null-cone) basis** used in *The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation*. Writing a biquaternion in the null coordinates there, two of that article's four general products become ordinary matrix products under two maps, the **outer** product under $M=\left(\begin{smallmatrix}\xi&\alpha\\\beta&\eta\end{smallmatrix}\right)$ and the **diagonal** product under $F\leftrightarrow\left(\begin{smallmatrix}f_\alpha&-f_\beta\\-f_\xi&f_\eta\end{smallmatrix}\right)$; the source's claimed third, the **inner** product, is false, an exhaustive search finding no realization of it. The two maps differ from $\mathsf{M}_2$ by the change of basis between the isotropic basis and the corpus's basis, and they are named here only to place $\mathsf{M}_2$ among the others.

## Why the Signs Are Forced

Two features of the asserted assignment are not free: the factor $i$, and its sign. Both are settled by the check above, and that is what makes the assignment a statement about the algebra rather than a choice of convention.

**The factor $i$ is required by $\vec e_k^2 = -e_t$.** The three matrices

$$
\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad
\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

square to $+\mathsf{M}_2(e_t)$. Assigning them to $\vec e_x, \vec e_y, \vec e_z$ would therefore give $\vec e_k^2 = +e_t$, the wrong sign. Multiplying by the complex unit repairs this, and both $+i$ and $-i$ times these matrices satisfy $\vec e_k^2 = -e_t$; the squaring relation alone therefore requires the factor $i$ but leaves its sign open.

**The sign is then forced by the cross-relations.** The alternative assignment sends $\vec e_k$ to $-\mathsf{M}_2(\vec e_k)$, reversing the sign of every vector image. The product of the images of $\vec e_x$ and $\vec e_y$ is then

$$
\big(-\mathsf{M}_2(\vec e_x)\big)\big(-\mathsf{M}_2(\vec e_y)\big) = \mathsf{M}_2(\vec e_x)\mathsf{M}_2(\vec e_y) = \mathsf{M}_2(\vec e_z),
$$

because the two minus signs cancel — while the image of $\vec e_z$ under that assignment is $-\mathsf{M}_2(\vec e_z)$. The product of the images comes out as *minus* the image of the required value, so the alternative fails at $\vec e_x\vec e_y = \vec e_z$; the same cancellation of signs makes it fail at every other cross-relation, where the target is again a single vector image and flips while the product does not. Under the assignment asserted above the same computation gives

$$
\mathsf{M}_2(\vec e_x)\mathsf{M}_2(\vec e_y) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
= \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} = \mathsf{M}_2(\vec e_z),
$$

which is exactly the image of $\vec e_z$. So the assignment asserted above passes the check and the alternative fails it. Both statements were verified on the explicit matrices.

The physical reading of the sign is the one recorded in the remark above. The Hermitian quaternion units $i\vec e_k$ are Hermitian elements, and their images $\mathsf{M}_2(i\vec e_k) = i\,\mathsf{M}_2(\vec e_k)$ are the Hermitian matrices; the imaginary quaternion units themselves are not, since $\mathsf{M}_2(\vec e_k)^\dagger = -\mathsf{M}_2(\vec e_k)$ in the three vector cases. The assignment is thus the one under which the Hermitian elements of the algebra become the Hermitian matrices, and that is what makes it an algebra of observables. It is why the sign is a consequence of the algebra rather than a convention that could have gone either way.

## Trace, Determinant and the Biquaternion Norm

**The trace is twice the scalar part.** The trace is taken in this representation, with $\mathrm{Tr}(e_t) = 2$ as it comes from $\mathsf{M}_2(e_t) = I_2$. From the general matrix,

$$
\mathrm{Tr}(\tilde{Q}) = (Q_t - i Q_z) + (Q_t + i Q_z) = 2 Q_t .
$$

So the scalar part of a biquaternion is a matrix trace, and the traceless matrices are the vector parts. This is why the centre subspace is the scalar matrices: an element commutes with everything exactly when its matrix is a multiple of the identity.

The factor $2$ — not $1$ — is a consequence of $\mathsf{M}_2(e_t) = I_2$ and not a normalisation: it comes with the four basis images and cannot be divided out. Restricting neither argument to $\mathbb{M}_+$, the identity reads

$$
\mathrm{Tr}(\tilde{Q}_1\tilde{Q}_2) = 2\,\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2) \qquad \text{for all } \tilde{Q}_1, \tilde{Q}_2 \in \mathbb{B},
$$

where $\mathrm{Tr}(\tilde{Q}_1\tilde{Q}_2)$ is the trace of the product of the matrices, $\mathrm{Tr}(\mathsf{M}_2(\tilde{Q}_1)\mathsf{M}_2(\tilde{Q}_2))$. This follows from $\mathrm{Tr}\,\mathsf{M}_2(\tilde{Q}) = 2Q_t$, the $\mathbb{C}$-linearity of $\mathsf{M}_2$ and the multiplicativity of the trace; the pairs drawn from $\mathbb{M}_+$ are the case in which the pairing is real. It is the form in which the operator articles use the identity, and in the quantum-information articles it is the Born rule, $p = \mathrm{Tr}(\tilde\Pi\tilde{Ϛ})$.

**The determinant is the biquaternion norm.** Expanding,

$$
\det(\tilde{Q}) = (Q_t - iQ_3)(Q_t + iQ_3) - (-iQ_1 - Q_y)(-iQ_1 + Q_y)
= (Q_t^2 + Q_z^2) - \big[(-iQ_1)^2 - Q_y^2\big] = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 = \langle\tilde{Q}\rangle_{\natural}.
$$

This is the central fact of the representation. The biquaternion norm, defined algebraically as $\tilde{Q}\tilde{Q}^{\natural}$, is the determinant of the corresponding matrix — not merely similar to it, but equal to it. Three consequences follow at once.

**Invertibility.** A biquaternion is invertible exactly when its biquaternion norm is nonzero, because a matrix is invertible exactly when its determinant is. The algebraic inverse $\tilde{Q}^{-1} = \tilde{Q}^{\natural}/\langle\tilde{Q}\rangle_{\natural}$ is the matrix inverse, since for a $2\times 2$ matrix the adjugate is $\det(M)\,M^{-1}$.

**Multiplicativity.** $\langle\tilde{Q}_1\tilde{Q}_2\rangle_{\natural} = \langle\tilde{Q}_1\rangle_{\natural}\langle\tilde{Q}_2\rangle_{\natural}$ holds because the determinant is multiplicative. The algebraic proof of this identity is a computation in eight real components; in the matrix form it is one line, and this is the clearest illustration of what the representation buys.

**Zero divisors.** The zero divisors of $\mathbb{B}$ are the singular matrices. The null cone $\langle\tilde{Q}\rangle_{\natural} = 0$ is the determinant-zero locus. Since $\mathbb{B}$ is not a division algebra, this locus is nonempty, and its elements are exactly the matrices of rank at most one.

**Worked example.** For $\tilde{Q}=(2+i)e_t+(1-i)\vec e_x+3\vec e_y+i\vec e_z$ the image is $\begin{pmatrix}3+i&-4-i\\2-i&1+i\end{pmatrix}$, of trace $4+2i=2Q_t$ and determinant $11+2i=\langle\tilde{Q}\rangle_{\natural}$, so the element is a unit with inverse $\tilde{Q}^{\natural}/N$.

## The Rank-One Elements and the Outer Product

The determinant is the norm, so the zero divisors are the nonzero singular matrices; the matrix form also says what such a matrix is.

**Proposition.** For $\tilde{Q}\neq0$ the following are equivalent: $\langle\tilde{Q}\rangle_{\natural}=0$; $\mathsf{M}_2(\tilde{Q})$ is singular; $\mathsf{M}_2(\tilde{Q})$ is an outer product
$$
\mathsf{M}_2(\tilde{Q})=uv^{T},\qquad u=\binom{\alpha}{\beta}\neq0,\quad v=\binom{\gamma}{\delta}\neq0,
$$
the pair $(u,v)$ being determined up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$.

**Proof.** The first two are equivalent by $\det \mathsf{M}_2(\tilde{Q})=\langle\tilde{Q}\rangle_{\natural}$, and $\tilde{Q}\neq0$ makes the matrix nonzero; a nonzero singular two-by-two matrix has rank one. Let $M=\mathsf{M}_2(\tilde{Q})$ have rank one and let $M_{pq}\neq0$ be an entry. Every two-by-two minor of $M$ vanishes, so $M_{iq}M_{pj}=M_{ij}M_{pq}$ for all $i,j$; hence, with $u$ the $q$-th column and $v^{T}$ the $p$-th row divided by $M_{pq}$,
$$
u=\binom{M_{1q}}{M_{2q}},\qquad v^{T}=\frac{1}{M_{pq}}\begin{pmatrix}M_{p1}&M_{p2}\end{pmatrix},
$$
one has $(uv^{T})_{ij}=M_{iq}M_{pj}/M_{pq}=M_{ij}$, so $M=uv^{T}$, and $u\neq0$ because its $p$-th entry is $M_{pq}\neq0$. A different pivot gives a pair differing by precisely the rescaling: the $j$-th columns of $uv^{T}=u'(v')^{T}$ give $u'=\lambda u$ for $\lambda=v_{j}/v'_{j}\neq0$, and the remaining entries give $v'=\lambda^{-1}v$.

**Worked example.** For $\tilde{Q}=\vec e_y+i\vec e_z$ the image is $\mathsf{M}_2(\tilde{Q})=\begin{pmatrix}1&-1\\1&-1\end{pmatrix}$, of rank one; the pivot $M_{11}=1$ gives $u=(1,1)^{T}$, $v=(1,-1)^{T}$, and the pivot $M_{12}=-1$ gives $u=(-1,-1)^{T}$, $v=(-1,1)^{T}$, the same pair rescaled by $\lambda=-1$.

## The General Plain Bilinear Form in the Model

The trace identity of §*Trace, Determinant and the Biquaternion Norm* is a pairing of the algebra, and this is its name.

**Theorem (the trace pairing).** For all biquaternions,

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}\bigl(\tilde Q_1\tilde Q_2\bigr)=\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2)\bigr),
$$

so the matrix trace is the carrier of the scalar part, and on the diagonal

$$
\langle\tilde Q,\tilde Q\rangle=\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde Q)^2\bigr)=\sum_\mu\varepsilon_\mu Q_\mu^2,\qquad \varepsilon_0=+1,\ \varepsilon_1=\varepsilon_2=\varepsilon_3=-1 .
$$

*Proof.* The first equality is the definition of the general plain bilinear form; the second is the trace identity of §*Trace, Determinant and the Biquaternion Norm* applied to the product $\tilde Q_1\tilde Q_2$; the diagonal is that identity read on the basis, where $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and $\operatorname{Tr}(\mathsf{M}_2(e_\mu)\mathsf{M}_2(e_\nu))=2\varepsilon_\mu\delta_{\mu\nu}$.

**The Gram matrix, the congruence and the signature.** In the coefficient basis the Gram matrix of $B$ is the sign matrix $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$, and a change of basis of matrix $S$ replaces it by $S^{\mathsf T}\mathrm{E}S$; over $\mathbb{C}$ the form is determined up to congruence by its rank alone, every non-degenerate complex quadratic form of rank $4$ being equivalent to this one. The plain product is what puts the sign matrix $\mathrm{E}$, and not $\mathrm{I}_4$, in the coefficient basis. Over $\mathbb{R}$ the form has signature $(4,4)$ on the eight real coordinates, and it is indefinite.

**The null set.** The pairing vanishes on the isotropic cone $\sum_\mu\varepsilon_\mu Q_\mu^2=0$, a complex cone of real dimension $6$ in $\mathbb{R}^8$, with two families of isotropic planes. It is the null set of neither the determinant nor the general quaternionic bilinear form; the quadric, its isotropic planes, the hyperbolic splitting and the index are *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*.

**The automorphisms.** A matrix preserves the trace pairing exactly when $T^{\mathsf T}\mathrm{E}T=\mathrm{E}$, so on the coefficients the automorphism group is $\{T\in GL_4(\mathbb{C}):T^{\mathsf T}\mathrm{E}T=\mathrm{E}\}=O_4(\mathbb{C})$, of complex dimension $6$ and real dimension $12$, its Lie algebra $\{X:X^{\mathsf T}\mathrm{E}+\mathrm{E}X=0\}$ being of real dimension $12$. The real structures exhibit the real forms: the Hermitian conjugation is an antilinear form reversal whose fixed space is the Hermitian subspace, of restriction signature $(4,0)$, so the automorphisms commuting with it form the real orthogonal group $O(4)$; the coefficient conjugation has fixed space the quaternion subspace, of signature $(1,3)$, exhibited by $O(1,3)$. The group of real-linear automorphisms of the realified form is the larger $O(4,4)$, which is not the group the form defines over $\mathbb{C}$. On the matrices the conjugation $M\mapsto UMU^{-1}$ by a unit and the transposition $M\mapsto M^{\mathsf T}$ are automorphisms, since $\operatorname{Tr}(UMU^{-1}\cdot UNU^{-1})=\operatorname{Tr}(MN)$ and $\operatorname{Tr}(M^{\mathsf T}N^{\mathsf T})=\operatorname{Tr}(MN)$; the inner automorphisms and the transposition together form a proper subgroup of the full group $O_4(\mathbb{C})$.

## Remarkable Subspaces

Each of the algebra's remarkable subspaces has a description in matrix language, and each description is a statement a physicist recognizes. Following the conventions article, the components of a general biquaternion are written $Q_t, Q_x, Q_y, Q_z$ and are **complex**; the parameters of a real subspace are written in lowercase and are **real**, with the prime recording which slot carries the $i$: $q_\mu$ is the coefficient entering with $e_\mu$ and $q'_\mu$ the one entering with $ie_\mu$, so that $Q_\mu = q_\mu + iq'_\mu$ — unprimed the real part, primed the imaginary part. Every matrix below is the one rule

$$
\mathsf{M}_2(\tilde{Q}) = Q_t\,\mathsf{M}_2(e_t) + Q_x\,\mathsf{M}_2(\vec e_x) + Q_y\,\mathsf{M}_2(\vec e_y) + Q_z\,\mathsf{M}_2(\vec e_z),
$$

with the subspace's own parametrisation substituted for the coefficients:

| subspace | defining condition | basis image | parametrisation | image |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\tilde{Q}^{\natural} = \tilde{Q}$ | $\mathsf{M}_2(e_t)$ | $Q_t = q_t + iq'_t$ | the scalar matrices |
| $\mathrm{Vect}(\mathbb{B})$ | $\tilde{Q}^{\natural} = -\tilde{Q}$ | $\mathsf{M}_2(\vec e_x),\ \mathsf{M}_2(\vec e_y),\ \mathsf{M}_2(\vec e_z)$ | $Q_t = 0$ | the traceless matrices |
| $\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde{Q}} = \tilde{Q}$ | $\mathsf{M}_2(e_t),\ \mathsf{M}_2(\vec e_x),\ \mathsf{M}_2(\vec e_y),\ \mathsf{M}_2(\vec e_z)$ | $Q_\mu = q_\mu$ | $\begin{pmatrix} z & w \\ -\bar{w} & \bar{z} \end{pmatrix}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde{Q}} = -\tilde{Q}$ | $i\mathsf{M}_2(e_t),\ i\mathsf{M}_2(\vec e_x),\ i\mathsf{M}_2(\vec e_y),\ i\mathsf{M}_2(\vec e_z)$ | $Q_\mu = iq'_\mu$ | $i$ times the quaternion matrices |
| $\mathbb{M}_+$ | $\tilde{Q}^{*} = \tilde{Q}$ | $\mathsf{M}_2(e_t),\ i\mathsf{M}_2(\vec e_x),\ i\mathsf{M}_2(\vec e_y),\ i\mathsf{M}_2(\vec e_z)$ | $Q_t = q_t$, $Q_k = iq'_k$ | a Hermitian matrix |
| $\mathbb{M}_-$ | $\tilde{Q}^\flat = \tilde{Q}$ | $i\mathsf{M}_2(e_t),\ \mathsf{M}_2(\vec e_x),\ \mathsf{M}_2(\vec e_y),\ \mathsf{M}_2(\vec e_z)$ | $Q_t = iq'_t$, $Q_k = q_k$ | $i$ times a Hermitian matrix |

The four basis images $\mathsf{M}_2(e_\mu)$ are the ones displayed in *The Representation*; no Pauli matrix is needed to write any of the matrices down. Each subspace is then taken in its turn below: the centre subspace, the vector subspace, the quaternion subspace, the antiquaternion subspace, the informational subspace and the material subspace. The vector subspace is the only one of the remarkable subspaces that is not four- or two-dimensional. The conventions article calls $\mathbb{M}_+$ and $\mathbb{M}_-$ the informational and material *sectors*; here, with all six on the same footing, they are called subspaces like the other four.

Each subspace is displayed as a two-step chain: the matrix in the complex coefficients $Q_\mu$, and the same matrix with that subspace's real parameters substituted, $Q_\mu = q_\mu + iq'_\mu$.

### The Centre Subspace $\mathbb{C}_{\mathbb{B}}$

The centre subspace, the fixed space of quaternion conjugation ${}^{\natural}$: the elements $Q_te_t$ with $Q_t$ complex, carried onto the scalar matrices,

$$
\mathsf{M}_2(\tilde{Q}) = Q_t\,\mathsf{M}_2(e_t) = \begin{pmatrix} Q_t & 0 \\ 0 & Q_t \end{pmatrix}
= \begin{pmatrix} q_t + iq'_t & 0 \\ 0 & q_t + iq'_t \end{pmatrix},
$$

the scalar matrix written through its two real parameters. The one subspace with no vector part: $Q_te_t$ is Hermitian exactly when $Q_t$ is real and anti-Hermitian exactly when $Q_t$ is purely imaginary. Its two complex coefficients reduce to the two real parameters $q_t$ and $q'_t$, so its reading is the two central directions together,

$$
\tilde{Q} = q_te_t + q'_t(ie_t) ,
$$

the informational scalar and the material scalar. It is the only one of the remarkable subspaces of real dimension two, and the only commutative one; the vector subspace and the four four-dimensional ones are the rest.

### The Vector Subspace $\mathrm{Vect}(\mathbb{B})$

The complement of the centre subspace: the elements with no scalar part, those with $\mathrm{Sc}(\tilde{Q}) = 0$, carried onto the **traceless** matrices,

$$
\mathsf{M}_2(\tilde{Q}) = \begin{pmatrix} -iQ_3 & -iQ_1 - Q_y \\ -iQ_1 + Q_y & iQ_3 \end{pmatrix}
= \begin{pmatrix} -i(q_z + iq'_z) & -i(q_x + iq'_x) - (q_y + iq'_y) \\ -i(q_x + iq'_x) + (q_y + iq'_y) & i(q_z + iq'_z) \end{pmatrix}, \qquad \mathrm{Tr}\,\mathsf{M}_2 = 0 .
$$

Its image is exactly $\mathrm{SL}(2,\mathbb{C})$, the traceless complex matrices, so the third split $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$ of the relations article reads here as the trace decomposition $M_2(\mathbb{C}) = \mathbb{C}\mathsf{M}_2(e_t) \oplus \mathrm{SL}(2,\mathbb{C})$: scalar part against traceless part. It is the **anti-fixed space** of quaternion conjugation, the elements with $\tilde{Q}^{\natural} = -\tilde{Q}$, whose fixed space is the centre subspace above; equivalently it is the kernel of the scalar part. It is the only one of the remarkable subspaces that is six-dimensional, being three-dimensional over $\mathbb{C}$. Under the commutator it is closed, $[\mathrm{SL}_2,\mathrm{SL}_2] \subseteq \mathrm{SL}_2$, and indeed it is the derived subspace $[\mathbb{B},\mathbb{B}]$; under multiplication it is not — the product of two traceless matrices need not be traceless, since $\mathrm{Tr}(M^2) = -2\det M$. Its six real parameters are the two spatial blocks together,

$$
\tilde{Q} = q_x\vec e_x + q_y\vec e_y + q_z\vec e_z + q'_x(i\vec e_x) + q'_y(i\vec e_y) + q'_z(i\vec e_z) ,
$$

so its real and imaginary parts are the material and the informational space block, $\mathrm{Vect}(\mathbb{B}) = X_{\mathrm{m}} \oplus X_{\mathrm{i}}$: it takes one spatial block from $\mathbb{M}_+$ and one from $\mathbb{M}_-$, the vector counterpart of the centre subspace's two scalar blocks. Reading its entries back off the traceless matrix returns the three complex coefficients $Q_k = q_k + iq'_k$, whose real and imaginary parts are the two spatial vectors. Its determinant is the biquaternion norm with the scalar term dropped, $\det = Q_x^2 + Q_y^2 + Q_z^2$.

### The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$

The real-quaternion subspace, the fixed space of complex conjugation $\bar{\cdot}$: the elements with all four $q_\mu$ real, carried from the basis $\{e_t, \vec e_x, \vec e_y, \vec e_z\}$ onto the four basis images themselves,

$$
\big\{\, \mathsf{M}_2(e_t),\ \mathsf{M}_2(\vec e_x),\ \mathsf{M}_2(\vec e_y),\ \mathsf{M}_2(\vec e_z) \,\big\},
$$

with no factor of $i$ anywhere — this is the image of the algebra's own basis, and the one subspace whose matrix basis is the assignment $\mathsf{M}_2(e_\mu)$ read off just as it stands. Writing its general element as $q_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$, the same two-step chain applies, with the complex coefficients and the real parameters the same four numbers,

$$
\mathsf{M}_2(\tilde{Q}) = \begin{pmatrix} Q_t - iQ_3 & -iQ_1 - Q_y \\ -iQ_1 + Q_y & Q_t + iQ_3 \end{pmatrix}
= \begin{pmatrix} q_t - iq_3 & -iq_1 - q_y \\ -iq_1 + q_y & q_t + iq_3 \end{pmatrix},
$$

with all four $q_\mu$ real. Naming the two complex entries,

$$
\mathsf{M}_2(q_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z) = \begin{pmatrix} z & w \\ -\bar{w} & \bar{z} \end{pmatrix}, \qquad z = q_t - iq_3, \quad w = -iq_1 - q_y ,
$$

where the entry $z$ is this one complex number, the combination $q_t - iq_3$ of two real parameters on the diagonal, $q_3$ being the third vector coefficient.

That is the matrix statement of $M = \epsilon\overline{M}\epsilon^{-1}$. The trace is $2q_t$, twice the scalar part, and the determinant is

$$
\det = |z|^2 + |w|^2 = q_t^2 + q_x^2 + q_y^2 + q_z^2 ,
$$

a sum of squares, which vanishes only at the zero element. This is a four-**real**-dimensional set, not the four-dimensional complex space of all matrices with $z, w \in \mathbb{C}$, and on it the determinant is **definite** — which is the matrix reason $\mathbb{H}$ is a division algebra while $\mathbb{B}$ is not. Removing the complex coefficients from the algebra makes the biquaternion norm positive definite, and that is all that separates the two cases.

### The Antiquaternion Subspace $i\mathbb{H}_{\mathbb{B}}$

The anti-fixed space of complex conjugation: the elements with all four $q'_\mu$ real, carried from the basis $\{ie_t, i\vec e_x, i\vec e_y, i\vec e_z\}$ onto $i$ times the four basis images,

$$
\big\{\, i\mathsf{M}_2(e_t),\ i\mathsf{M}_2(\vec e_x),\ i\mathsf{M}_2(\vec e_y),\ i\mathsf{M}_2(\vec e_z) \,\big\}.
$$

Since $\mathsf{M}_2$ is $\mathbb{C}$-linear and $i\mathbb{H}_{\mathbb{B}} = i\,\mathbb{H}_{\mathbb{B}}$, its image is simply $i$ times the image of the quaternion subspace, $\mathsf{M}_2(iq'_\mu e_\mu) = i\,\mathsf{M}_2(q'_\mu e_\mu)$, and the chain is the quaternion one under the factor $i$,

$$
\mathsf{M}_2(\tilde{Q}) = \begin{pmatrix} Q_t - iQ_3 & -iQ_1 - Q_y \\ -iQ_1 + Q_y & Q_t + iQ_3 \end{pmatrix}
= i\begin{pmatrix} q'_t - iq'_z & -iq'_x - q'_y \\ -iq'_x + q'_y & q'_t + iq'_z \end{pmatrix},
$$

with the four $q'_\mu$ real. Naming the two complex entries as in the quaternion case,

$$
\mathsf{M}_2(iq'_te_t + iq'_x\vec e_x + iq'_y\vec e_y + iq'_z\vec e_z) = \begin{pmatrix} iz' & iw' \\ -i\bar{w}' & i\bar{z}' \end{pmatrix}, \qquad z' = q'_t - iq'_z, \quad w' = -iq'_x - q'_y ,
$$

where the entry $z'$ is the combination $q'_t - iq'_z$ of two real parameters.

The determinant changes sign with the factor, $\det = -((q'_t)^2 + (q'_x)^2 + (q'_y)^2 + (q'_z)^2)$, **negative definite** — the exact mirror of the definite form on $\mathbb{H}_{\mathbb{B}}$. Together the two images exhaust $M_2(\mathbb{C})$, so the real-and-imaginary split of the algebra is, in matrix language, the split of $M_2(\mathbb{C})$ into the quaternion matrices and $i$ times them.

### The Informational Subspace $\mathbb{M}_+$

The Hermitian subspace, the fixed space of ${}^{*}$: the elements with $q_t, q'_x, q'_y, q'_z$ real, carried from the basis $\{e_t, i\vec e_x, i\vec e_y, i\vec e_z\}$ onto the four matrices

$$
\big\{\, \mathsf{M}_2(e_t),\ i\mathsf{M}_2(\vec e_x),\ i\mathsf{M}_2(\vec e_y),\ i\mathsf{M}_2(\vec e_z) \,\big\}
= \left\{\,
\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},\
\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},\
\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix},\
\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \,\right\},
$$

the three non-identity members being the Hermitian basis matrices that the remark of *The Representation* names the Pauli matrices.

Writing the general element of the subspace as $\tilde{Q} = q_te_t + iq'_x\vec e_x + iq'_y\vec e_y + iq'_z\vec e_z$, with $q_t$ and the $q'_k$ real, the same two-step chain gives

$$
\mathsf{M}_2(\tilde{Q}) = \begin{pmatrix} Q_t - iQ_3 & -iQ_1 - Q_y \\ -iQ_1 + Q_y & Q_t + iQ_3 \end{pmatrix}
= \begin{pmatrix} q_t + q'_z & q'_x - iq'_y \\ q'_x + iq'_y & q_t - q'_z \end{pmatrix},
$$

the general Hermitian $2 \times 2$ matrix — the general observable of a two-state system — with scalar part half the trace, $\mathrm{Tr}\,\mathsf{M}_2(\tilde{Q}) = 2q_t$, real, against the purely imaginary $2iq'_t$ of the material subspace. Its determinant is

$$
\det \mathsf{M}_2(\tilde{Q}) = q_t^2 - (q'_x)^2 - (q'_y)^2 - (q'_z)^2 ,
$$

the mirror interval of signature $(1,3)$, read on the informational element $q_te_t + i(q'_x\vec e_x + q'_y\vec e_y + q'_z\vec e_z)$.

### The Material Subspace $\mathbb{M}_-$

The anti-Hermitian subspace, the fixed space of $\flat$: the elements with $q'_t, q_x, q_y, q_z$ real, carried from the basis $\{ie_t, \vec e_x, \vec e_y, \vec e_z\}$ onto the four matrices

$$
\big\{\, i\mathsf{M}_2(e_t),\ \mathsf{M}_2(\vec e_x),\ \mathsf{M}_2(\vec e_y),\ \mathsf{M}_2(\vec e_z) \,\big\}
= \left\{\,
i\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},\
\begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix},\
\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix},\
\begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} \,\right\}.
$$

Writing the general element as $\tilde{Q} = iq'_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$, with $q'_t$ and the $q_k$ real, the chain from the complex coefficients to the real parameters is

$$
\mathsf{M}_2(\tilde{Q}) = \begin{pmatrix} Q_t - iQ_3 & -iQ_1 - Q_y \\ -iQ_1 + Q_y & Q_t + iQ_3 \end{pmatrix}
= \begin{pmatrix} iq'_t - iq_3 & -iq_1 - q_y \\ -iq_1 + q_y & iq'_t + iq_3 \end{pmatrix}
= i\begin{pmatrix} q'_t - q_z & -q_x + iq_2 \\ -q_x - iq_2 & q'_t + q_z \end{pmatrix},
$$

which is $i$ times a Hermitian matrix: the scalar part is carried by $i$, and the vector signs are reversed. Its trace is $2iq'_t$, purely imaginary, and its determinant is

$$
\det \mathsf{M}_2(\tilde{Q}) = \langle\tilde{Q}\rangle_{\natural} = -(q'_t)^2 + q_x^2 + q_y^2 + q_z^2 ,
$$

the quadratic form of signature $(3,1)$: the form of the material sector, read on $\tilde{Q} = iq'_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$, giving $-(q'_t)^2 + q_x^2 + q_y^2 + q_z^2$. This is the most economical place to see why the material subspace is the **anti**-Hermitian one: the anti-Hermitian matrices are exactly those on which the determinant comes out with one minus sign.

### How They Fit Together

The relations among the subspaces — the three splits, their intersections, and the pairs that span the algebra — are worked out in *Relations Between Subspaces*. Two consequences are used repeatedly in this article and are recorded here.

**The three splits cross.** The split $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$ is the trace decomposition and is not four-plus-four at all: it separates the two-dimensional centre subspace from the six-dimensional traceless part. The other two splits, the real-and-imaginary split $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$ and the sector split $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$, are both four-plus-four, and neither refines the other. Each of $\mathbb{M}_+$ and $\mathbb{M}_-$ takes its scalar from one half and its vectors from the other, which is why the prime pattern is three-and-one rather than four-and-none. Multiplication by the central $i$ exchanges $\mathbb{M}_+$ and $\mathbb{M}_-$, and exchanges the two halves.

**Two of the remarkable subspaces are subalgebras.** $\mathbb{C}_{\mathbb{B}}$ is closed under multiplication; $\mathrm{Vect}(\mathbb{B})$ is closed under the commutator but not under the product; $\mathbb{H}_{\mathbb{B}}$ is closed under multiplication; and $i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_\pm$ are neither — the product of two Hermitian matrices is Hermitian only when they commute. The centre subspace meets $\mathbb{M}_+$ and $\mathbb{M}_-$ in the two central lines, $\mathbb{C}_{\mathbb{B}} \cap \mathbb{M}_+ = \mathbb{R}e_t$ and $\mathbb{C}_{\mathbb{B}} \cap \mathbb{M}_- = \mathbb{R}(ie_t)$, and every element splits as a Hermitian plus an anti-Hermitian part, $\tilde{Q} = \tfrac12(\tilde{Q} + \tilde{Q}^{*}) + \tfrac12(\tilde{Q} - \tilde{Q}^{*})$, the two parts differing by the factor $i$ that carries $\mathbb{M}_-$ into $\mathbb{M}_+$.

## The Ideals as Columns and the Spinor Module

The matrix form makes the algebra's ideal structure a statement about columns. The idempotents

$$
\tilde\Pi_+ = \tfrac12(e_t + i\vec e_z) \;\longmapsto\; \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = E_{11}, \qquad
\tilde\Pi_- = \tfrac12(e_t - i\vec e_z) \;\longmapsto\; \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = E_{22}
$$

generate the two **columns** of the matrix algebra,

$$
\mathbb{B}\tilde\Pi_+ = \mathbb{C}E_{11} \oplus \mathbb{C}E_{21}, \qquad \mathbb{B}\tilde\Pi_- = \mathbb{C}E_{12} \oplus \mathbb{C}E_{22},
$$

with $\mathbb{B} = \mathbb{B}\tilde\Pi_+ \oplus \mathbb{B}\tilde\Pi_-$; the first column is the set of matrices whose second column vanishes, the second those whose first column vanishes. $i\vec e_z$ is a root of $+1$, $(i\vec e_z)^2 = e_t$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents. Each column is two-dimensional over $\mathbb{C}$ and minimal, and left multiplication acts on it irreducibly: the column **is** the spinor module $S = \mathbb{C}^2$ of the companion articles on the spinor module and on representation theory — the abstract simple module realised inside the algebra, with the algebra acting on it by left multiplication — and not merely a space isomorphic to it.

Two structural facts are visible in this form, and both are used by the physics articles.

**The two columns are the two chiralities.** Left multiplication preserves each column: for any $M$, the products $ME_{11}$ and $ME_{21}$ again have vanishing second column. No left multiplication can therefore relate the two columns. A mass term that couples the left- and right-handed components cannot be a left multiplication; it must be a **right** multiplication, and the element that performs it is the one carried to the off-diagonal matrix unit,

$$
\vec\Upsilon_x = \tfrac12(i\vec e_x - \vec e_y) \;\longmapsto\; \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = E_{12} = |0\rangle\langle 1| .
$$

whose right action maps the first column onto the second — $E_{11} \mapsto E_{12}$ and $E_{21} \mapsto E_{22}$ — while annihilating the second. This is the matrix form of the structural reason the biquaternionic Dirac equation couples the chiralities by a right multiplication, and of the statement that the spinor module, not the whole algebra, is the carrier of the Dirac field. The element is the corpus's truncated lowering operator — the name matches the image $|0\rangle\langle 1|$ exactly — and the spinor-module articles write it $\vec\Upsilon_x$, with $\vec\Upsilon_y = \tfrac12(i\vec e_x + \vec e_y)$; the pair satisfies the matrix-unit relations $\vec\Upsilon_x\vec\Upsilon_y = \tilde\Pi_+$, $\vec\Upsilon_y\vec\Upsilon_x = \tilde\Pi_-$, $\vec\Upsilon_x^2 = \vec\Upsilon_y^2 = 0$.

**The two-sided ideals are not among them.** Since $\mathbb{B} \cong M_2(\mathbb{C})$ is simple, its only two-sided ideals are $0$ and $\mathbb{B}$; the columns are one-sided. That is what allows the algebra to be simple and still carry two distinct chiralities, and it is why the mass term must be off-diagonal rather than a multiplication confined to a single column.

The pair $\tilde\Pi_\pm$ used here is not the only one: every unit vector $\vec u$ gives the idempotent pair $\tilde\Pi_{1,2}(\vec u) = \tfrac12(e_t \pm i\vec u)$, and $\tilde\Pi_\pm = \tilde\Pi_{1,2}(\vec u_z)$ is the choice for which the two columns are the coordinate columns. The idempotent $\tilde\Pi_1(\vec u_x)$ of the section *Spin, Qubits and the Bloch Vector* is a member of that family, corresponding to a different direction.

## The Conjugations in Matrix Form

The four involutions of the algebra become four matrix operations. Writing $M = \mathsf{M}_2(\tilde{Q})$:

| Involution | Definition | Matrix image |
|---|---|---|
| Quaternion conjugation | $\tilde{Q}^{\natural} = Q_te_t - Q_x\vec e_x - Q_y\vec e_y - Q_z\vec e_z$ | the **adjugate** $\mathrm{adj}\,M = \epsilon M^{\mathsf T}\epsilon^{-1}$ |
| Complex conjugation | $Q_\mu \mapsto Q_\mu^{*}$ | $\epsilon\,\overline{M}\,\epsilon^{-1}$ |
| Hermitian conjugation | $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$ | the **conjugate transpose** $M^\dagger$ |
| Anti-Hermitian conjugation | $\tilde{Q}^\flat = -\tilde{Q}^{*}$ | $-\,M^\dagger$ |

Two of the four are dressed by the antisymmetric form

$$
\epsilon = \mathsf{M}_2(-\vec e_y) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix},
$$

the invariant antisymmetric form $\varepsilon$ of the spinor module: quaternion conjugation is the transpose dressed by $\epsilon$, and complex conjugation is the entrywise conjugation dressed by $\epsilon$. The adjugate statement is worth writing out, since it is the least familiar:

$$
\tilde{Q}^{\natural} \;\mapsto\; \begin{pmatrix} Q_t + i Q_z & i Q_x + Q_y \\ i Q_x - Q_y & Q_t - i Q_z \end{pmatrix}
= \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
\quad\text{for}\quad M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}.
$$

Quaternion conjugation is therefore the classical adjoint, and the identity $\tilde{Q}\tilde{Q}^{\natural} = \langle\tilde{Q}\rangle_{\natural}e_t$ is the matrix identity $M\,\mathrm{adj}(M) = \det(M)\,\mathsf{M}_2(e_t)$. The other two are the operations a physicist expects: ${}^{*}$ is the conjugate transpose, so its fixed points are the Hermitian matrices, and $\flat = -{}^{*}$ has the anti-Hermitian matrices as its fixed points. The real structure $\flat$, which the corpus uses for the $\mathbb{M}_\pm$ split and for Majorana-type pairings, is the negative conjugate transpose.

**Complex conjugation is the one that does not act entrywise.** It is sometimes said that $\tilde{Q}^*$ conjugates the entries of the matrix. That is not true, and the reason is structural: the representation is built with the same $i$ that conjugates the coefficients, so the two operations compete. Conjugating the entries of $\mathsf{M}_2(\tilde{Q})$ sends $\mathsf{M}_2(\vec e_x) \mapsto -\mathsf{M}_2(\vec e_x)$ and $\mathsf{M}_2(\vec e_z) \mapsto -\mathsf{M}_2(\vec e_z)$ — the images of $\vec e_x$ and $\vec e_z$ to their negatives — while the image of $\vec e_y$ is left alone; the entrywise operation is therefore not $\mathsf{M}_2(\tilde{Q}^*)$, and it is not the image of any involution of the algebra. The correct correspondence is the one in the table,

$$
\mathsf{M}_2(\tilde{Q}^*) = \epsilon\,\overline{\mathsf{M}_2(\tilde{Q})}\,\epsilon^{-1}, \qquad \epsilon = \mathsf{M}_2(-\vec e_y),
$$

verified on explicit matrices, and the adjugate form of quaternion conjugation is the same dressing applied to the transpose. In this representation the safe rule is: use $\bar{\phantom{Q}}$, $\bar{\cdot}$, ${}^{*}$ and $\flat$ through the four formulas above, and never conjugate the matrix entries on their own.

## The Four Words and the Four Traces

The twelve operations of the two chapters are built from four products, and each product is a word in the two matrices $X=\mathsf{M}_2(\tilde Q_1)$ and $Y=\mathsf{M}_2(\tilde Q_2)$ and in the two involutions of the model, the adjugate and the conjugate transpose.

| product | first slot | second slot | the word |
|---|---|---|---|
| general plain | $X$ | $Y$ | $XY$ |
| general quaternionic | $\operatorname{adj}X$ | $Y$ | $\operatorname{adj}X\,Y$ |
| general plain sesquilinear | $X$ | $Y^{\dagger}$ | $XY^{\dagger}$ |
| general quaternionic sesquilinear | $\operatorname{adj}X$ | $Y^{\dagger}$ | $\operatorname{adj}X\,Y^{\dagger}$ |

The symmetric part of a product is the half-sum of its word and of the word with the two slots exchanged, and the antisymmetric part is the half-difference; those two halves are the subjects of the remaining representation articles of the block.

**The four forms are four traces.** The four products are four matrix traces, and the four forms of the algebra are read from them:

$$
\tfrac12\operatorname{Tr}(XY)=\langle\tilde Q_1,\tilde Q_2\rangle,\qquad
\tfrac12\operatorname{Tr}(\operatorname{adj}X\,Y)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural},\qquad
\tfrac12\operatorname{Tr}(XY^{\dagger})=\langle\tilde Q_1,\tilde Q_2\rangle_{*},\qquad
\tfrac12\operatorname{Tr}(\operatorname{adj}X\,Y^{\dagger})=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*},
$$

the general plain bilinear, the general quaternionic bilinear, the general plain sesquilinear and the general quaternionic sesquilinear form, in the two slots the table of the words prescribes. The adjugate is quaternion conjugation and the dagger is Hermitian conjugation, so in the two slots the four words are the two conjugations switched on and off, and the four forms are one trace read four times.

## Spin, Qubits and the Bloch Vector

The matrix representation is what connects the algebra to the physics of two-state systems, and the connection runs through the single identity $i\vec e_k \mapsto \mathsf{M}_2(i\vec e_k)$. The images are the Hermitian basis matrices that the remark of *The Representation* names the Pauli matrices, and the whole section is written in those images.

**Spin operators.** The spin operators of the biquaternion framework are $\tilde{S}_k = \tfrac{\hbar}{2}i\vec e_k$, and under the isomorphism,

$$
\tilde{S}_k = \tfrac{\hbar}{2}i\vec e_k \;\longmapsto\; \tfrac{\hbar}{2}\mathsf{M}_2(i\vec e_k) = \tfrac{\hbar}{2}\,i\,\mathsf{M}_2(\vec e_k) ,
$$

which are the Hermitian spin matrices. The eigenvalue statement $\tilde{S}_k^2 = \tfrac{\hbar^2}{4}e_t$, the anticommutation $\{\tilde{S}_i, \tilde{S}_j\} = \tfrac{\hbar^2}{2}\delta_{ij}e_t$ and the commutator $[\tilde{S}_i,\tilde{S}_j] = i\hbar\varepsilon_{ijk}\tilde{S}_k$ are, matrix by matrix, the standard angular-momentum algebra of a spin-$\tfrac12$ system. In the matrix form they are checked by multiplying $2\times 2$ matrices.

**States as Hermitian idempotents.** The rank-one Hermitian idempotents of $\mathbb{M}_+$ are the pure states. The element

$$
\tilde\Pi_1(\vec u_x) = \tfrac{1}{2}(e_t + i\vec e_x) \;\longmapsto\; \tfrac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}
= \tfrac{1}{2}\big(\mathsf{M}_2(e_t) + \mathsf{M}_2(i\vec e_x)\big)
$$

satisfies $\tilde\Pi_1^2 = \tilde\Pi_1$, has trace $1$ and determinant $0$: its matrix is a rank-one projector, hence the element is a pure state. Its complement $\tilde\Pi_2(\vec u_x) = \tfrac12(e_t - i\vec e_x)$ is the complementary Hermitian idempotent, and $\tilde\Pi_1(\vec u_x) + \tilde\Pi_2(\vec u_x) = e_t$ is $\mathsf{M}_2(e_t)$. Both have vanishing biquaternion norm, which is the matrix way of saying that the rank-one idempotents of $\mathbb{M}_+$ live on the null cone: a pure state is a null element of the algebra. Note that not every idempotent of $\mathbb{M}_+$ is a state: the unit $e_t$ is idempotent, and its matrix $\mathsf{M}_2(e_t)$ has trace $2$ and determinant $1$, so its matrix is the full-rank projector and does not lie on the null cone. This is the representation-theoretic content of *The Biquaternion Vacuum as a Minimal Idempotent*.

**The density matrix.** A general mixed state is

$$
\rho = \tfrac{1}{2}\big(\mathsf{M}_2(e_t) + r_1\mathsf{M}_2(i\vec e_x) + r_2\mathsf{M}_2(i\vec e_y) + r_3\mathsf{M}_2(i\vec e_z)\big),
$$

with Bloch vector $\vec r \in \mathbb{R}^3$. It is Hermitian with unit trace, so it lies in the image of $\mathbb{M}_+$, and the Bloch components are recovered by the trace pairing,

$$
r_k = \mathrm{Tr}\big(\rho\,\mathsf{M}_2(i\vec e_k)\big),
$$

verified for all three components. The purity condition $\mathrm{Tr}(\rho^2) = 1$ is $|\vec r| = 1$, and the boundary of the Bloch ball is the set of rank-one projectors, i.e. the matrices of the pure states found above. So the three-level description — biquaternion state, density matrix, Bloch vector — is one statement in three coordinate systems, and the passage between them is matrix multiplication and the trace.

## The Groups

The multiplicative group of the algebra has a matrix image with a standard name. An element of unit norm, $\langle\tilde{Q}\rangle_{\natural} = e_t$, has

$$
\det \mathsf{M}_2(\tilde{Q}) = 1,
$$

so the unit-norm biquaternions map into the special linear group,

$$
\{\tilde{Q} \in \mathbb{B} : \langle\tilde{Q}\rangle_{\natural} = e_t\} \;\cong\; \mathrm{SL}(2,\mathbb{C}).
$$

This is the matrix form of the statement that the unit-norm elements act on $\mathbb{M}_-$ by rotor conjugation and generate the Lorentz group. Concretely, the rotation rotors are the unit-norm elements of $\mathbb{H}_{\mathbb{B}}$, which map to the $SU(2)$ matrices

$$
\tilde u(\theta, \vec u) = \exp\!\big(\tfrac{1}{2}\theta \vec u\cdot e\big) \;\longmapsto\; \exp\!\big(\tfrac{1}{2}\theta\,u_k\,\mathsf{M}_2(\vec e_k)\big),
$$

and the boost rotors are the Hermitian unit-norm elements, which map to the Hermitian $\mathrm{SL}(2,\mathbb{C})$ matrices. The two cases are distinguished in the matrix form by Hermiticity, exactly as they are distinguished in the algebra by the split $\mathbb{M}_+ \oplus \mathbb{M}_-$.

The advantage of the matrix form here is not computational but structural: writing a general unit-norm element as a boost times a rotation, $\tilde U_{\mathrm L}=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, is the polar decomposition of its $\mathrm{SL}(2,\mathbb{C})$ matrix into a positive Hermitian factor and a unitary one, in that order, and the double cover $SU(2) \to SO(3)$ is the statement that $\pm M$ give the same rotation. In the algebra the double cover has to be argued from the biquaternion norm; in the matrix form it is visible, because $-\mathsf{M}_2(e_t)$ is a unit-norm element acting trivially on the material subspace.

The identification is structural, and it is not the cheaper route to the numbers. Sangwine & Hitzer note that $\mathsf{M}_2(\tilde{Q})$ carries a four-fold redundancy — the $4\times4$ complex representation of a biquaternion is one of a special form, not an arbitrary complex matrix, and a general numerical polar decomposition of an arbitrary matrix need not preserve that form accurately over a series of computational steps — so the biquaternion algorithm needs less memory and fewer operations. Their algorithm also obtains the hyperbolic factor by dividing out the trigonometric factor, which is cheaper than forming the square root $\sqrt{\tilde{Q}\tilde{Q}^{*}}$ used above to exhibit the identity and the Hermiticity: the square root is the proof that the factor exists, and the division is how it is computed.

## What the Matrix Form Makes Visible

The representation is a change of coordinates, and its value is what the new coordinates make obvious. Collected: the scalar part is a trace; the biquaternion norm is a determinant; invertibility is nonzero determinant; the informational and material subspaces are the Hermitian and anti-Hermitian matrices; the observables are the Hermitian matrices generated by the images of the Hermitian units; the pure states are the rank-one Hermitian idempotents on the null cone; the unit-norm group is $\mathrm{SL}(2,\mathbb{C})$; and the zero divisors are the rank-one matrices. Each of these is a theorem in the algebra and an inspection in the matrix form.

The limitation is equally clear. The matrix form is a representation of the **complexified** algebra: it uses $i$ in its entries, so it identifies $\mathbb{B}$ with $M_2(\mathbb{C})$ and does not, by itself, display the real structure that distinguishes the material subspace from the informational one. That structure — the choice of $\flat$, and the physical statement that $\mathbb{M}_-$ is the subspace where mass lives — is a choice of real form, and it is visible in the algebra and in the Hermitian/anti-Hermitian split, but not in the identification $\mathbb{B} \cong M_2(\mathbb{C})$ alone. The matrix form is the computational face of the algebra, not the whole of it.

## Physical Interpretations

The isomorphism reads as the dictionary of the framework: the trace is the scalar part and the determinant the biquaternion norm, so the interval and the mass are the trace and the determinant of one $2\times2$ complex matrix. Read on the states, the Hermitian matrices are the observables and the determinant is the positivity test, so the same two matrix invariants carry the framework's metric and its state condition. Read on the conjugations, the matrix image of a conjugation is a matrix conjugation, which is why the four forms can be computed in the smallest representation that carries them.

The determinant is read as a **volume**: $\det \mathsf{M}_2(\tilde{Q})=\langle\tilde{Q}\rangle_{\natural}$ is the biquaternion norm, so the unit-norm slice is $\mathrm{SL}(2,\mathbb{C})$, read as the **volume-preserving** group, and a general element is a four-volume element its determinant measures. The Lorentz group is therefore the volume-preserving group of the representation, which is the matrix form of the statement that a Lorentz transformation preserves the interval.

Read as a **phase fibre**, the unit spinors of the representation are the three-sphere over the Bloch sphere, and the $\mathrm{U}(1)$ that fixes a state's ray is the central phase, so the phase of the framework is a fibre over the state space and its holonomy is the geometric phase. Boundary: the bundle, the invariant and the phase are owned by *The Hopf Fibration and the Biquaternion Gauge Bundle* and by *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*; the reading records the smallest matrix image of the fibre and adds no topology.

## Summary

The matrix representation of the biquaternion algebra is the isomorphism $\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C})$ given by $\mathsf{M}_2(e_t) = I_2$ and the three basis matrices asserted above, with $\mathsf{M}_2(i) = i\,\mathsf{M}_2(e_t)$ on the central scalar. The images of the Hermitian units, $\mathsf{M}_2(i\vec e_k) = i\,\mathsf{M}_2(\vec e_k)$, are the three Hermitian basis matrices named in the remark above.

- The signs are forced: $\vec e_k^2 = -e_t$ requires the factor $i$, and $\vec e_x\vec e_y = +\vec e_z$ requires the minus sign. Both are checked by multiplying the four basis matrices. The equivalent statement, that the images of the Hermitian elements are Hermitian, is why the Hermitian elements of the algebra are its observables.
- The trace is twice the scalar part, $\mathrm{Tr}(\tilde{Q}) = 2Q_t$, and the determinant **is** the biquaternion norm, $\det(\tilde{Q}) = \langle\tilde{Q}\rangle_{\natural} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2$. Invertibility, multiplicativity of the norm, and the zero divisors as rank-one (singular) matrices $\mathsf{M}_2(\tilde{Q}) = uv^{T}$ all follow.
- The subspaces of the algebra are the centre subspace $\mathbb{C}_{\mathbb{B}}$, $Q_te_t \mapsto Q_t\mathsf{M}_2(e_t)$, the only one of the remarkable subspaces of real dimension two; the vector subspace $\mathrm{Vect}(\mathbb{B})$, the traceless part, $Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z \mapsto \mathrm{SL}(2,\mathbb{C})$, the anti-fixed space of quaternion conjugation; the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ (the matrices $\begin{pmatrix} z & w \\ -\bar{w} & \bar{z}\end{pmatrix}$ with $z = q_t - iq_3$, $w = -iq_1 - q_y$, determinant $q_t^2 + q_x^2 + q_y^2 + q_z^2$ definite); the antiquaternion subspace $i\mathbb{H}_{\mathbb{B}}$ ($i$ times the quaternion matrices, determinant $-(q'_t)^2 - (q'_x)^2 - (q'_y)^2 - (q'_z)^2$, negative definite); the Hermitian subspace $\mathbb{M}_+$ (the informational subspace, $q_te_t + iq'_k\vec e_k$ mapped to a Hermitian matrix, $\det = q_t^2 - (q'_x)^2 - (q'_y)^2 - (q'_z)^2 = c^2(t')^2 -(x'^2+y'^2+z'^2)$); and the anti-Hermitian subspace $\mathbb{M}_-$ (the material subspace, $iq'_te_t + q_k\vec e_k$ mapped to $i$ times a Hermitian matrix, $\det = -(q'_t)^2 + q_x^2 + q_y^2 + q_z^2$, the interval of signature $(3,1)$). Every element splits into a Hermitian plus an anti-Hermitian part, $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$, with $\mathbb{M}_- = i\mathbb{M}_+$.
- The minimal left ideals are the matrix **columns**: $\tilde\Pi_\pm = \tfrac12(e_t \pm i\vec e_z)$ map to $E_{11}$ and $E_{22}$, and $\mathbb{B} = \mathbb{B}\tilde\Pi_+ \oplus \mathbb{B}\tilde\Pi_-$ is the split into the two chiralities. Left multiplication preserves each column, while right multiplication by $\vec\Upsilon_x = \tfrac12(i\vec e_x - \vec e_y) \mapsto E_{12}$ carries the first column onto the second — it annihilates the second — and that is why the mass term of the Dirac equation is a right multiplication. The algebra is simple, so these ideals are one-sided, not two-sided.
- Quaternion conjugation is the adjugate $\epsilon M^{\mathsf T}\epsilon^{-1}$ and complex conjugation is $\epsilon\overline{M}\epsilon^{-1}$; both are dressed by the antisymmetric form $\epsilon = \mathsf{M}_2(-\vec e_y)$. Hermitian conjugation is the conjugate transpose and $\flat = -{}^{*}$ is its negative, neither of them dressed. Entrywise conjugation of $M$ on its own is not the image of any involution of the algebra.
- The physics is read off the matrices: $\tilde{S}_k = \tfrac{\hbar}{2}i\vec e_k \mapsto \tfrac{\hbar}{2}\mathsf{M}_2(i\vec e_k)$; the pure states are the rank-one Hermitian idempotents $\tilde\Pi_{1,2}(\vec u)$ and are the null elements $\langle\tilde\Pi\rangle_{\natural} = 0$; the density matrix $\rho = \tfrac12\big(\mathsf{M}_2(e_t) + r_k\mathsf{M}_2(i\vec e_k)\big)$ has $r_k = \mathrm{Tr}\big(\rho\,\mathsf{M}_2(i\vec e_k)\big)$ on the Bloch ball.
- Unit norm is unit determinant, so the unit-norm biquaternions are $\mathrm{SL}(2,\mathbb{C})$, with the rotations unitary and the boosts Hermitian.
- The form and the four products are traces. The trace pairing is $\langle\tilde Q_1,\tilde Q_2\rangle=\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2))$, of Gram matrix $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$, of signature $(4,4)$ on the eight real coordinates, isotropic on the cone $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ of real dimension $6$, with automorphism group $O_4(\mathbb{C})$ and the real forms $O(4)$, $O(1,3)$ and $O(4,4)$. The four products are the four words $XY$, $\operatorname{adj}X\,Y$, $XY^{\dagger}$ and $\operatorname{adj}X\,Y^{\dagger}$ in the matrix and its adjugate and dagger, and the four forms are the four half-traces $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ in those words.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{Q}$ | An element of the algebra: the general element in *The Representation*, and the element of whichever subspace the part at hand is about. Coefficients $Q_\mu$ (complex), parameters $q_\mu$ and $q'_\mu$ (real) |
| $\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C})$ | The isomorphism converting a biquaternion into its matrix |
| $\mathbb{B} \cong M_2(\mathbb{C})$ | Biquaternion algebra as $2\times 2$ complex matrices |
| $\mathsf{M}_2(e_t) = I_2$, $\mathsf{M}_2(\vec e_k)$ as in the section *The Representation* | The representation; $\mathsf{M}_2(i) = i\,\mathsf{M}_2(e_t)$ on the central scalar |
| $\mathsf{M}_2(i\vec e_k) = i\,\mathsf{M}_2(\vec e_k)$ | Images of the Hermitian units: the three Hermitian basis matrices of the remark in *The Representation*, with $\mathsf{M}_2(i\vec e_k)^2 = \mathsf{M}_2(e_t)$ |
| $\sigma_1,\sigma_2,\sigma_3$ | the Pauli matrices, a shorthand for the images of $\vec e_x,\vec e_y,\vec e_z$ |
| $\epsilon=i\sigma_2=\mathsf{M}_2(-\vec e_y)$ | the matrix of the conjugate-reflection of the quaternion subspace |
| $\tilde{Q} \mapsto \begin{pmatrix} Q_t - iQ_3 & -iQ_1 - Q_y \\ -iQ_1 + Q_y & Q_t + iQ_3\end{pmatrix}$ | Image of a general biquaternion |
| $\mathrm{Tr}(\tilde{Q}) = 2Q_t$ | Trace is twice the scalar part |
| $\det(\tilde{Q}) = \langle\tilde{Q}\rangle_{\natural}$ | Determinant is the biquaternion norm |
| $\mathsf{M}_2(\tilde{Q}) = uv^{T}$ | Rank-one form of a nonzero null element: the columns $u = (\alpha,\beta)^{T}$ and $v = (\gamma,\delta)^{T}$ are nonzero and determined up to $(\lambda u,\lambda^{-1}v)$ |
| $\tilde{Q}^{\natural} \mapsto \mathrm{adj}\,M = \epsilon M^{\mathsf T}\epsilon^{-1}$ | Quaternion conjugation is the adjugate |
| $\tilde{Q}^* \mapsto \epsilon\overline{M}\epsilon^{-1}$ | Complex conjugation, dressed by $\epsilon$ |
| $\epsilon = \mathsf{M}_2(-\vec e_y)$ | The antisymmetric form dressing bar and star |
| $\tilde{Q}^{*} \mapsto M^\dagger$ | Hermitian conjugation is the conjugate transpose |
| $\tilde{Q}^\flat \mapsto -M^\dagger$ | Anti-Hermitian conjugation; the real structure |
| $\mathbb{C}_{\mathbb{B}}$ | The centre subspace: $Q_te_t \mapsto Q_t\mathsf{M}_2(e_t)$, the scalar matrices; parameters $q_t, q'_t$ |
| $\mathrm{Vect}(\mathbb{B})$ | The vector subspace, the complement of the centre subspace: $Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z \mapsto \begin{pmatrix} -iQ_3 & -iQ_1-Q_y \\ -iQ_1+Q_y & iQ_3\end{pmatrix}$, the traceless matrices $\mathrm{SL}(2,\mathbb{C})$; the anti-fixed space of quaternion conjugation, closed under the commutator and equal to the derived subspace $[\mathbb{B},\mathbb{B}]$ |
| $\mathbb{H}_{\mathbb{B}}$ | The real-quaternion subspace: $q_te_t + \cdots + q_z\vec e_z \mapsto \begin{pmatrix} z & w \\ -\bar{w} & \bar{z}\end{pmatrix}$, $z = q_t - iq_3$, $w = -iq_1 - q_y$, determinant $q_t^2 + q_x^2 + q_y^2 + q_z^2$ |
| $i\mathbb{H}_{\mathbb{B}}$ | The antiquaternion subspace, the anti-fixed space of complex conjugation: $i$ times the real-quaternion image, $\begin{pmatrix} iz & iw \\ -i\bar{w} & i\bar{z}\end{pmatrix}$, determinant **negative** definite. With $\mathbb{H}_{\mathbb{B}}$ it gives $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$, a split crossing the $\mathbb{M}_\pm$ split |
| $\mathbb{M}_+$ | The informational subspace, the Hermitian one: $q_te_t + iq'_k\vec e_k$, mapped to a Hermitian matrix, $\det = q_t^2 - (q'_x)^2 - (q'_y)^2 - (q'_z)^2$; parameters $q_t, q'_x, q'_y, q'_z$ |
| $\mathbb{M}_-$ | The material subspace, the anti-Hermitian one: $iq'_te_t + q_k\vec e_k$, mapped to $i$ times a Hermitian matrix, $\det = -(q'_t)^2 + q_x^2 + q_y^2 + q_z^2$; parameters $q'_t, q_x, q_y, q_z$ |
| $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$ | The trace decomposition $M_2(\mathbb{C}) = \mathbb{C}\mathsf{M}_2(e_t) \oplus \mathrm{SL}(2,\mathbb{C})$: scalar part against traceless part |
| $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ | Every element is a Hermitian part plus an anti-Hermitian part; $\mathbb{M}_- = i\mathbb{M}_+$ |
| $\tilde\Pi_\pm = \tfrac12(e_t \pm i\vec e_z) = \tilde\Pi_{1,2}(\vec u_z)$ | Idempotents generating the two minimal left ideals; $\mathsf{M}_2(\tilde\Pi_\pm) = E_{11}, E_{22}$ |
| $\tilde\Pi_{1,2}(\vec u) = \tfrac12(e_t \pm i\vec u)$ | The pure-state idempotents, the rank-one idempotents of $\mathbb{M}_+$: the idempotents with $\langle\tilde\Pi\rangle_{\natural} = 0$ |
| $\mathbb{B}\tilde\Pi_+$, $\mathbb{B}\tilde\Pi_-$ | The two matrix **columns**, i.e. the two chiralities; $\mathbb{B} = \mathbb{B}\tilde\Pi_+ \oplus \mathbb{B}\tilde\Pi_-$ |
| $\vec\Upsilon_x = \tfrac12(i\vec e_x - \vec e_y) \mapsto E_{12}$ | Right multiplication carries $\mathbb{B}\tilde\Pi_+$ onto $\mathbb{B}\tilde\Pi_-$; the chirality coupling. The corpus's truncated lowering operator; the spinor-module articles write it $\vec\Upsilon_x$, its conjugate $\vec\Upsilon_y$ |
| $\tilde{S}_k = \tfrac{\hbar}{2}i\vec e_k$ | Spin operators; the images $\tfrac{\hbar}{2}\mathsf{M}_2(i\vec e_k)$ are Hermitian |
| $\rho = \tfrac12\big(\mathsf{M}_2(e_t) + r_k\mathsf{M}_2(i\vec e_k)\big)$ | Density matrix; Bloch vector $\vec r$, $r_k = \mathrm{Tr}\big(\rho\,\mathsf{M}_2(i\vec e_k)\big)$ |
| $\mathrm{SL}(2,\mathbb{C})$ | Image of the unit-norm biquaternions |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\langle\tilde{Q}\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle=\tfrac12\operatorname{Tr}(XY)$, Gram $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$ | the general plain bilinear form as a half-trace in the model, $X=\mathsf{M}_2(\tilde Q_1)$, $Y=\mathsf{M}_2(\tilde Q_2)$; signature $(4,4)$ on the eight real coordinates |
| $\tfrac12\operatorname{Tr}(\operatorname{adj}X\,Y)=N$, $\tfrac12\operatorname{Tr}(XY^{\dagger})=H$, $\tfrac12\operatorname{Tr}(\operatorname{adj}X\,Y^{\dagger})=K$ | the quaternionic bilinear, the plain sesquilinear and the quaternionic sesquilinear form as half-traces, in the words the table prescribes |
| $\operatorname{adj}X=M^{\natural}$, $Y^{\dagger}=M^{*}$ | the adjugate is quaternion conjugation and the dagger is Hermitian conjugation, the two involutions the four words are built from |
| $O_4(\mathbb{C})$, $O(4)$, $O(1,3)$, $O(4,4)$ | the automorphism group of the trace pairing over $\mathbb{C}$, of complex dimension $6$, and its real forms cut out by the Hermitian and the coefficient conjugations, with the $O(4,4)$ of the realified form |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation of the quaternion units and their products.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of the complexified algebra.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), Chapter 3, for the matrix representations of biquaternions and the adjugate form of quaternion conjugation.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions," *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the representation theory and the conventions in use in applied work.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Pauli algebra, the relation $i\vec e_k \leftrightarrow \sigma_k$, and the $\mathrm{SL}(2,\mathbb{C})$ description of the Lorentz group.
- Bertfried Fauser, "On the equivalence of Daviau's space Clifford algebraic, Hestenes' and Parra's formulations of (real) Dirac theory," arXiv:hep-th/9908200, for the identification chain that places $\mathbb{H}\oplus\mathbb{H}$, the Pauli algebra and the biquaternions in the same isomorphism class; the space Clifford formulation itself is in *The Daviau Map and the Space Clifford Formulation of the Dirac Equation*.
- *The Biquaternion Space, the Group of Involutions and the Six Subspaces* (`articles_physics/the-biquaternion-space-the-group-of-involutions-and-the-six-subspaces.md`), companion article, for the relations among the subspaces whose matrices are listed here — their coordinate blocks, intersections, spans, gradings and biquaternion norms.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y; technical report CES-535, University of Essex (2019), for the identification of the biquaternion polar decomposition with the matrix polar decomposition of $M_2(\mathbb{C})$, and for the cost comparison in the section on the groups.
