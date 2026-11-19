# __$M_4(\mathbb{C})$ Pauli Representation : Products, Forms and Norms__

## Introduction

**The subject.** The matrix expression, in the Peirce frame, of every quantity of the algebra that involves two elements: the product, the symmetric and the antisymmetric part of a product, the four forms, the four norms, the trace and the determinant.

**Why two elements.** *$M_4(\mathbb{C})$ Pauli Representation* reads one element: the block $A=\mathsf M_2(\tilde Q)$, the tensor display $L=\mathrm I_2\otimes A$ and $R=A^{\mathsf T}\otimes\mathrm I_2$, the trace, the determinant, the eigenvalues and the six subspaces. It never writes a word in two matrices. This article does, and its one subject is what an operation on two elements becomes as an operation on their two blocks.

**The order of the article.** The frame, the block and the three companion words come first (§*The Two Elements in the Peirce Frame*). The product and the split of a product into its two parts follow (§*The Product*, §*The Symmetric and the Antisymmetric Part*), then the twelve products in one table (§*The Twelve Products*). The four forms are read next, with their Gram matrices in this frame, which are not the Gram matrices of the axis-free frame (§*The Four Forms*). The trace, the determinant and the four norms follow (§*The Trace*, §*The Determinant*, §*The Four Norms*), the constants are counted (§*The Factors*), and what this frame gives and what it costs closes the article (§*What the Peirce Frame Gives*).

**The frame and the block.** The frame is the standard Peirce frame
$$
\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-),\qquad
\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z),\qquad
\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y),
$$
and the block of an element is
$$
A=\mathsf M_2(\tilde Q)=\begin{pmatrix}P_+&X_-\\X_+&P_-\end{pmatrix},\qquad
P_\pm=Q_t\mp iQ_z,\qquad X_\pm=-iQ_x\pm Q_y .
$$
The two displays are $L(\tilde Q)=\mathrm I_2\otimes A$ and $R(\tilde Q)=A^{\mathsf T}\otimes\mathrm I_2$, both from §*The Left Family* and §*The Right Family* of *$M_4(\mathbb{C})$ Pauli Representation*. Write $A_1$ and $A_2$ for the blocks of $\tilde Q_1$ and $\tilde Q_2$.

**The algebra.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on $(e_t,\vec e_x,\vec e_y,\vec e_z)$, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$; the central scalar imaginary is $i$. Write $\tilde Q_a=Q_{at}e_t+\vec Q_a$, $B_a^2=Q_{ax}^2+Q_{ay}^2+Q_{az}^2$ and $\langle\tilde Q_a\rangle_{\natural}=Q_{at}^2+B_a^2$, and write $(\vec Q_1,\vec Q_2)$ and $\vec Q_1\times\vec Q_2$ for the complex bilinear dot and cross products of the vector parts.

**The result in one line.** In this frame each of the twelve words is a word in the two blocks $A_1$ and $A_2$ and in the three block companions $A^{\natural}=\sigma_2A^{\mathsf T}\sigma_2$, $A^{c}=\sigma_2\overline{A}\sigma_2$ and $A^{*}=A^{\dagger}$; the four forms are $\tfrac14$ times the four $4\times4$ trace words, which is $\tfrac12$ times the four block trace words; the symmetric part of the quaternionic product is $N(\tilde Q_1,\tilde Q_2)\mathrm I_2$; and the Gram matrices of the four forms in this frame are half-integer arrays of which only the Hermitian one is diagonal, where the axis-free frame has the sign matrix and the identity.

**Boundaries.** The frame, the block and the two displays are *$M_4(\mathbb{C})$ Pauli Representation*; this article takes them and does not rebuild them. The change of frame in general is *Families of Matrix Representations*. The four general products and the twelve products are *The Four General Products and Their Relations over the Biquaternion Algebra* and *Symmetric and Antisymmetric Decomposition of the Four General Products*. The four forms and the four norms without matrices are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*. The same content in the coefficient basis is *$M_4(\mathbb{C})$ Axis-Free Representation : Products, Forms and Norms*, and at the element size it is *$M_2(\mathbb{C})$ Pauli Representation : Products, Forms and Norms*.

## The Two Elements in the Peirce Frame

**The two matrices.** Write
$$
L_a:=L(\tilde Q_a)=\mathrm I_2\otimes A_a,\qquad R_a:=R(\tilde Q_a)=A_a^{\mathsf T}\otimes\mathrm I_2,\qquad a=1,2 .
$$
The block $A_a$ carries the four Peirce coordinates of $\tilde Q_a$, and the $4\times4$ matrix is the block repeated twice on the diagonal, once for each Peirce plane.

**The three companions, in the block.** The three conjugations of the element act on the block by the three rules
$$
A_a^{\natural}:=\mathsf M_2(\tilde Q_a^{\natural})=\sigma_2A_a^{\mathsf T}\sigma_2,\qquad
A_a^{c}:=\mathsf M_2(\bar{\tilde Q}_a)=\sigma_2\overline{A_a}\sigma_2,\qquad
A_a^{*}:=\mathsf M_2(\tilde Q_a^{*})=A_a^{\dagger},
$$
with $\sigma_2$ the second Pauli matrix and $\sigma_2^2=\mathrm I_2$. The first two are congruences of the transpose and of the entrywise conjugate, and the third is the adjoint without any congruence.

**Why the three rules differ.** The dagger row holds because the four frame vectors are orthogonal for the Hermitian form and have the same norm $\tfrac12$, which is proved in §*The Transpose Is Not the Conjugation* of *$M_4(\mathbb{C})$ Pauli Representation*: a frame orthogonal with equal norms gives the conjugate transpose as the adjoint, up to the common factor. The other two rows carry $\sigma_2$ because the frame vectors are not real: the Peirce coordinates $P_\pm$ and $X_\pm$ are complex-linear combinations of the coefficients with the imaginary unit in them, so conjugating the coefficients does not conjugate the coordinates, and transposing the coordinates does not negate the vector part.

**The same three rules at the $4\times4$ size.** With $C_L=\mathrm I_2\otimes\sigma_2$,
$$
L(\tilde Q_a^{\natural})=C_LL_a^{\mathsf T}C_L,\qquad
L(\bar{\tilde Q}_a)=C_L\overline{L_a}C_L,\qquad
L(\tilde Q_a^{*})=L_a^{\dagger},
$$
and the three are the block rules with the factor $\mathrm I_2$ on the left, since $\mathrm I_2\otimes(\sigma_2A^{\mathsf T}\sigma_2)=C_L(\mathrm I_2\otimes A)^{\mathsf T}C_L$. The matrix $C_L$ is its own inverse, $C_L^2=\mathrm I_4$, so each congruence is an involution.

**What the block sees and what it does not.** The block is the compression of the $4\times4$ matrix to one Peirce plane, as in *$M_2(\mathbb{C})$ Pauli Representation*, so every word of degree two in the blocks is the compression of the corresponding $4\times4$ word. Two things do not compress and appear only at the $4\times4$ size: the mixed trace of §*The Trace* and the commutation of the two families. Everything else in this article is read on the block, and each formula is given in both sizes.

## The Product

**The word of a product is the product of the blocks.** For all $\tilde Q_1,\tilde Q_2$,
$$
L(\tilde Q_1\tilde Q_2)=\mathrm I_2\otimes(A_1A_2),\qquad R(\tilde Q_1\tilde Q_2)=R_2R_1 .
$$
The first identity is the multiplicativity of the left family read through the tensor display: $(\mathrm I_2\otimes A_1)(\mathrm I_2\otimes A_2)=\mathrm I_2\otimes(A_1A_2)$. The second is the same computation on the right, where the order of the factors reverses because the right action is anti-multiplicative.

**The powers and the inverse.** For every integer $n$,
$$
L(\tilde Q^n)=\mathrm I_2\otimes A^n,\qquad R(\tilde Q^n)=R^n,\qquad
L(\tilde Q^{-1})=\mathrm I_2\otimes A^{-1},\qquad R(\tilde Q^{-1})=R^{-1},
$$
the last two when $\langle\tilde Q\rangle_{\natural}\neq0$, that is when $\det A\neq0$. The block inverse is $A^{-1}=\operatorname{adj}A/\det A$, which is $\sigma_2A^{\mathsf T}\sigma_2$ up to the factor $\langle\tilde Q\rangle_{\natural}$.

**The two planes carry the same block.** The identity $L=\mathrm I_2\otimes A$ says that the left action on the two Peirce planes is the same matrix $A$. Every $4\times4$ word of the form $\mathrm I_2\otimes X$ is therefore two copies of $X$, and every trace of such a word is twice the trace of $X$. This single observation accounts for every constant of §*The Factors*, and it is the reason almost every word of this article is read on one block.

**The two families still commute.** For all $\tilde Q_1,\tilde Q_2$,
$$
L_1R_2=R_2L_1,
$$
which is the associativity of the algebra read on both sides. It is a statement about four matrices, and it does not compress: at the element size $A$ and $A^{\mathsf T}$ need not commute, as §*The Product* of *$M_2(\mathbb{C})$ Pauli Representation* shows on $\vec\Upsilon_+$.

**The mixed trace.** For all $\tilde Q_1,\tilde Q_2$,
$$
\operatorname{Tr}(L_1R_2)=4Q_{1t}Q_{2t}.
$$
The identity holds at the $4\times4$ size and is the one statement of this article that has no element-size counterpart. Its block reading is a trace over the two tensor factors, and the $2\times2$ product $A_1A_2^{\mathsf T}$ has a different trace, computed in §*The Product* of *$M_2(\mathbb{C})$ Pauli Representation*.

## The Symmetric and the Antisymmetric Part

**The two exchanges.** The bilinear products are split by the interchange of the two arguments,
$$
f^{\mathrm{s}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)+f(\tilde Q_2,\tilde Q_1)\bigr),\qquad
f^{\mathrm{a}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)-f(\tilde Q_2,\tilde Q_1)\bigr),
$$
and the sesquilinear products by the interchange followed by the coefficientwise conjugation of the value,
$$
g^{\mathrm{s}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(g(\tilde Q_1,\tilde Q_2)+\overline{g(\tilde Q_2,\tilde Q_1)}\bigr),\qquad
g^{\mathrm{a}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(g(\tilde Q_1,\tilde Q_2)-\overline{g(\tilde Q_2,\tilde Q_1)}\bigr),
$$
as in *Symmetric and Antisymmetric Decomposition of the Four General Products*. The second pair is not the first pair applied to $g$: the interchange alone returns $\tilde Q_2\tilde Q_1^{*}$, a product of the opposite class, and the conjugation is what brings it back. The twelve products of §*The Twelve Products* are the four instances of each.

**The conjugated product, in the block.** The sesquilinear exchange needs the conjugated value as a product, and the two identities
$$
\overline{\tilde Q_2\tilde Q_1^{*}}=\bar{\tilde Q}_2\tilde Q_1^{\natural},\qquad
\overline{\tilde Q_2^{\natural}\tilde Q_1^{*}}=\bar{\tilde Q}_2^{\natural}\tilde Q_1^{\natural}
$$
are the coefficient conjugation applied to a product. In the block they read
$$
A_2^{c}A_1^{\natural}=\sigma_2\overline{A_2}A_1^{\mathsf T}\sigma_2,\qquad
(A_2^{c})^{\natural}A_1^{\natural}=\overline{A_2}^{\mathsf T}A_1^{\natural},
$$
the first because $\sigma_2^2=\mathrm I_2$ cancels the two inner factors, and the second because $(A^{c})^{\natural}=\overline{A}^{\mathsf T}$, which is the two congruences composed.

**The plain bilinear split, in the block.** For all $\tilde Q_1,\tilde Q_2$,
$$
\mathsf M_2(\tilde Q_1\bullet\tilde Q_2)=\tfrac12\bigl(A_1A_2+A_2A_1\bigr),\qquad
\mathsf M_2(\tilde Q_1\wedge\tilde Q_2)=\tfrac12\bigl(A_1A_2-A_2A_1\bigr),
$$
and the $4\times4$ words are the same two expressions with $\mathrm I_2\otimes$ in front. The symmetric part is the anticommutator and the antisymmetric part the commutator, and the commutator is traceless. This is the one split that compresses to the plain operations of the matrix algebra, and it compresses for a reason that the other three lack: the two slots of the plain product carry no conjugation, so the exchange of the arguments is the exchange of the two factors and nothing else.

**The plain antisymmetric part is a cross product.** By expansion in the scalar and the vector parts,
$$
\tilde Q_1\bullet\tilde Q_2=(Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2))+(Q_{1t}\vec Q_2+Q_{2t}\vec Q_1),\qquad
\tilde Q_1\wedge\tilde Q_2=\vec Q_1\times\vec Q_2,
$$
so the antisymmetric part is a pure vector and its block is traceless. The two identities are the expansion of *Symmetric and Antisymmetric Decomposition of the Four General Products*, written in the Peirce frame, and they hold in every frame: the cross product is an operation of the algebra and not of the representation.

**The quaternionic bilinear split, and the first price.** The same two steps with the first slot read through ${}^{\natural}$ give
$$
\mathsf M_2(\tilde Q_1\bullet_{\natural}\tilde Q_2)=\tfrac12\bigl(A_1^{\natural}A_2+A_2^{\natural}A_1\bigr)=N(\tilde Q_1,\tilde Q_2)\,\mathrm I_2,
$$
$$
\mathsf M_2(\tilde Q_1\wedge_{\natural}\tilde Q_2)=\tfrac12\bigl(A_1^{\natural}A_2-A_2^{\natural}A_1\bigr)=\tfrac12\bigl(\sigma_2A_1^{\mathsf T}\sigma_2A_2-\sigma_2A_2^{\mathsf T}\sigma_2A_1\bigr).
$$
The symmetric part collapses to a scalar matrix, for the element reason of the axis-free article: the two vector parts enter with opposite signs and cancel. The antisymmetric part is **not** a commutator of blocks. It is traceless all the same, but not for the reason a commutator is: its two terms have the same trace $2N(\tilde Q_1,\tilde Q_2)$. This is the first place where the frame shows its cost. In the axis-free frame the same word is $\tfrac12(L_1^{\mathsf T}L_2-L_2^{\mathsf T}L_1)$, a commutator of literal matrices; here the transpose of the frame is the congruence $\sigma_2A^{\mathsf T}\sigma_2$, and the $\sigma_2$ sits between the two factors.

**The plain sesquilinear split.** With the two terms of the exchange,
$$
\mathsf M_2(\tilde Q_1\bullet_*\tilde Q_2)=\tfrac12\bigl(A_1A_2^{\dagger}+\sigma_2\overline{A_2}A_1^{\mathsf T}\sigma_2\bigr),\qquad
\mathsf M_2(\tilde Q_1\wedge_*\tilde Q_2)=\tfrac12\bigl(A_1A_2^{\dagger}-\sigma_2\overline{A_2}A_1^{\mathsf T}\sigma_2\bigr).
$$
The first term is the block of the product $\tilde Q_1\tilde Q_2^{*}$, and the second is the block of its conjugated exchange. The adjoint is free in this frame and the entrywise conjugate is not, so the two terms cost differently.

**The quaternionic sesquilinear split.** The same with both slots of the first product read through their conjugations:
$$
\mathsf M_2(\tilde Q_1\bullet_{\natural*}\tilde Q_2)=\tfrac12\bigl(A_1^{\natural}A_2^{\dagger}+\overline{A_2}^{\mathsf T}A_1^{\natural}\bigr),\qquad
\mathsf M_2(\tilde Q_1\wedge_{\natural*}\tilde Q_2)=\tfrac12\bigl(A_1^{\natural}A_2^{\dagger}-\overline{A_2}^{\mathsf T}A_1^{\natural}\bigr).
$$
The second term simplifies because $(A_2^{c})^{\natural}=\overline{A_2}^{\mathsf T}$, so the quaternion conjugation remains on $A_1$ alone. The four splits are collected in the table of §*The Twelve Products*.

**The trace splits cleanly.** For each of the four products the antisymmetric part is traceless and the symmetric part carries the whole trace,
$$
\operatorname{Tr}\mathsf M_2(f^{\mathrm{a}}(\tilde Q_1,\tilde Q_2))=0,\qquad
\operatorname{Tr}\mathsf M_2(f^{\mathrm{s}}(\tilde Q_1,\tilde Q_2))=\operatorname{Tr}\mathsf M_2(f(\tilde Q_1,\tilde Q_2)),
$$
the first because a block trace is $2Q_t$ and the antisymmetric parts have zero scalar part, the second by subtraction. The same holds at the $4\times4$ size with the factor $4$ instead of $2$.

**The equal-argument case.** At $\tilde Q_1=\tilde Q_2=\tilde Q$ the bilinear antisymmetric parts vanish, since each is negated by the interchange of two equal arguments, and the square is the symmetric part alone. The sesquilinear antisymmetric part does not vanish there: it is the coefficientwise imaginary part of $\tilde Q\tilde Q^{*}$, of zero scalar part and of nonzero vector part as soon as the square is not fixed by the coefficient conjugation. In the block this is a traceless matrix of the form $\tfrac12(X-\overline{X})$ with $X=\tilde Q\tilde Q^{*}$, and its content is entirely in the traceless part.

## The Twelve Products

**The table.** Each row is one product, its $4\times4$ word, its block, and its trace at the $4\times4$ size. The four forms are those of §*The Four Forms*; the block column is the compression of the $4\times4$ word, valid when the word commutes with the tensor factor $\mathrm I_2$, which is the case for all twelve.

| Product | $4\times4$ word | Block | Trace |
|---|---|---|---|
| $\tilde Q_1\tilde Q_2$ | $L_1L_2$ | $A_1A_2$ | $4P$ |
| $\tilde Q_1^{\natural}\tilde Q_2$ | $L_1^{\mathsf T}L_2$ | $A_1^{\natural}A_2$ | $4N$ |
| $\tilde Q_1\tilde Q_2^{*}$ | $L_1L_2^{\dagger}$ | $A_1A_2^{\dagger}$ | $4H$ |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $L_1^{\mathsf T}L_2^{\dagger}$ | $A_1^{\natural}A_2^{\dagger}$ | $4\mathrm{Kr}$ |
| $\tilde Q_1\bullet\tilde Q_2$ | $\tfrac12(L_1L_2+L_2L_1)$ | $\tfrac12(A_1A_2+A_2A_1)$ | $4P$ |
| $\tilde Q_1\bullet_{\natural}\tilde Q_2$ | $\tfrac12(L_1^{\mathsf T}L_2+L_2^{\mathsf T}L_1)$ | $N\mathrm I_2$ | $4N$ |
| $\tilde Q_1\bullet_*\tilde Q_2$ | $\tfrac12(L_1L_2^{\dagger}+L_2^{c}L_1^{\mathsf T})$ | $\tfrac12(A_1A_2^{\dagger}+\sigma_2\overline{A_2}A_1^{\mathsf T}\sigma_2)$ | $4H$ |
| $\tilde Q_1\bullet_{\natural*}\tilde Q_2$ | $\tfrac12(L_1^{\mathsf T}L_2^{\dagger}+(L_2^{c})^{\mathsf T}L_1^{\mathsf T})$ | $\tfrac12(A_1^{\natural}A_2^{\dagger}+\overline{A_2}^{\mathsf T}A_1^{\natural})$ | $4\mathrm{Kr}$ |
| $\tilde Q_1\wedge\tilde Q_2$ | $\tfrac12(L_1L_2-L_2L_1)$ | $\tfrac12(A_1A_2-A_2A_1)$ | $0$ |
| $\tilde Q_1\wedge_{\natural}\tilde Q_2$ | $\tfrac12(L_1^{\mathsf T}L_2-L_2^{\mathsf T}L_1)$ | $\tfrac12(A_1^{\natural}A_2-A_2^{\natural}A_1)$ | $0$ |
| $\tilde Q_1\wedge_*\tilde Q_2$ | $\tfrac12(L_1L_2^{\dagger}-L_2^{c}L_1^{\mathsf T})$ | $\tfrac12(A_1A_2^{\dagger}-\sigma_2\overline{A_2}A_1^{\mathsf T}\sigma_2)$ | $0$ |
| $\tilde Q_1\wedge_{\natural*}\tilde Q_2$ | $\tfrac12(L_1^{\mathsf T}L_2^{\dagger}-(L_2^{c})^{\mathsf T}L_1^{\mathsf T})$ | $\tfrac12(A_1^{\natural}A_2^{\dagger}-\overline{A_2}^{\mathsf T}A_1^{\natural})$ | $0$ |

**What the table shows.** The four upper rows are the products, the four middle rows their symmetric parts, and the trace column repeats the four forms eight times and then gives zero four times. The block column is the same table at the element size, and it is the table of *$M_2(\mathbb{C})$ Pauli Representation : Products, Forms and Norms* with the trace column halved. The split of the block column is sharp: five rows are words in $A_1$, $A_2$ and their two daggers alone, and the other seven carry $\sigma_2$.

**The count of the $\sigma_2$.** Five block words carry none: the plain product $A_1A_2$, the plain dagger product $A_1A_2^{\dagger}$, the two plain halves, and the collapsed quaternionic symmetric product $N\mathrm I_2$, in which the two congruences cancel. The other seven carry it, through $A^{\natural}=\sigma_2A^{\mathsf T}\sigma_2$ or $\sigma_2\overline{A}\sigma_2$, always two congruences to a conjugated slot. The count is not the count of the axis-free article, where eight rows carry a transpose or an entrywise conjugate: there the dagger is not free, and the row that collapses here is a word in two transposes. The difference is the frame's fingerprint, and it is the content of §*What the Peirce Frame Gives*.

## The Four Forms

**The four words.** The four forms are the scalar parts of the four products, and the scalar part of an element is $\tfrac14$ of the $4\times4$ trace and $\tfrac12$ of the block trace:
$$
\operatorname{Sc}\tilde X=\tfrac14\operatorname{Tr}L(\tilde X)=\tfrac12\operatorname{Tr}A,\qquad
L(\tilde X)=\mathrm I_2\otimes A .
$$
Applying the identity to the four products gives the four words in the two sizes,
$$
P=\tfrac14\operatorname{Tr}(L_1L_2)=\tfrac12\operatorname{Tr}(A_1A_2),\qquad
N=\tfrac14\operatorname{Tr}(L_1^{\mathsf T}L_2)=\tfrac12\operatorname{Tr}(A_1^{\natural}A_2),
$$
$$
H=\tfrac14\operatorname{Tr}(L_1L_2^{\dagger})=\tfrac12\operatorname{Tr}(A_1A_2^{\dagger}),\qquad
\mathrm{Kr}=\tfrac14\operatorname{Tr}(L_1^{\mathsf T}L_2^{\dagger})=\tfrac12\operatorname{Tr}(A_1^{\natural}A_2^{\dagger}),
$$
with the letters and the names of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*: the plain form $P$, the quaternionic form $N$, the Hermitian form $H$ and the Krein form $\mathrm{Kr}$.

**The factor of two.** Each $4\times4$ word is twice the block word, and the reason is the trace rule of the tensor product,
$$
\operatorname{Tr}(\mathrm I_2\otimes X)=\operatorname{Tr}\mathrm I_2\operatorname{Tr}X=2\operatorname{Tr}X .
$$
The factor $4$ of the axis-free article and the factor $2$ of this one are therefore the same factor: the trace of the identity of the carrier. Here the carrier splits into a two-dimensional tensor factor and a two-dimensional block, and the trace of the first is the $2$ that the second does not carry.

**The Gram matrices are the frame's business.** The Gram matrix of a form in the frame is the array of its values on the four frame vectors. In the Peirce frame the four arrays are
$$
[P]_{\mathcal P}=\tfrac12\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{pmatrix},\qquad
[N]_{\mathcal P}=\tfrac12\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix},
$$
$$
[H]_{\mathcal P}=\tfrac12\mathrm I_4,\qquad
[\mathrm{Kr}]_{\mathcal P}=\tfrac12\begin{pmatrix}0&0&0&1\\0&-1&0&0\\0&0&-1&0\\1&0&0&0\end{pmatrix}.
$$
Each is computed from the four words on the four pairs of frame vectors, and each is a half-integer array. The Hermitian one is diagonal, because the frame is orthogonal for $H$ with equal norms $\tfrac12$; the plain one has $\tfrac12$ at the two scalar corners $(\tilde\Pi_+,\tilde\Pi_+)$ and $(\tilde\Pi_-,\tilde\Pi_-)$, zero at the two nilpotent corners, and $\tfrac12$ at the two mixed entries $(\vec\Upsilon_+,\vec\Upsilon_-)$ and $(\vec\Upsilon_-,\vec\Upsilon_+)$, because $\mathrm{Sc}(\tilde\Pi_\pm^2)=\tfrac12$ and $\mathrm{Sc}(\vec\Upsilon_\pm^2)=0$, while $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ has scalar part $\tfrac12$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ the same.

**The same form in two frames.** The four arrays above are not the four arrays of the axis-free article, which are the sign matrix $\mathrm E$ and the identity. The form is the same function of two elements in the two frames; only the array changes. The rule is the congruence of *Families of Matrix Representations*,
$$
[\text{form}]_{\mathcal P}=\mathsf C^{\mathsf T}[\text{form}]_{\mathcal E}\mathsf C,\qquad
[\text{form}]_{\mathcal P}=\mathsf C^{\dagger}[\text{form}]_{\mathcal E}\mathsf C,
$$
for the two bilinear forms and the two sesquilinear ones, $\mathsf C$ being the matrix whose columns are the four frame vectors in the coefficient basis, of determinant $-\tfrac14$. The check is the determinant: $\det[P]_{\mathcal P}=-\tfrac{1}{16}$ against $\det\mathrm E=-1$, and $\det(\mathsf C)^2=\tfrac{1}{16}$.

**The Gram matrix is not the form.** Nothing in the four words of the first display depends on the frame: they are traces, and a trace is invariant. The arrays of the second display depend on the frame entirely. The two statements are consistent because the coordinates of a pair of elements change with the frame and the value of the form does not. The axis-free article reads the four forms as $\mathrm E$ and $\mathrm I_4$ and this one as half-integer arrays, and both are the same four forms.

**The form sees the symmetric part.** For each of the four products,
$$
\operatorname{Sc}f(\tilde Q_1,\tilde Q_2)=\operatorname{Sc}f^{\mathrm{s}}(\tilde Q_1,\tilde Q_2),\qquad
\operatorname{Sc}f^{\mathrm{a}}(\tilde Q_1,\tilde Q_2)=0,
$$
so the four symmetric rows of §*The Twelve Products* carry the same four values as the four plain rows above them. The reading is the same as in the axis-free article and the reason is the same: the trace of a commutator is zero, and the sesquilinear half-differences have equal trace by conjugate symmetry.

## The Trace

**The trace of one block.** For every $\tilde Q$,
$$
\operatorname{Tr}A=2Q_t,\qquad \operatorname{Tr}L(\tilde Q)=\operatorname{Tr}R(\tilde Q)=2\operatorname{Tr}A=4Q_t .
$$
The block trace is the sum of the two diagonal entries $P_+=Q_t-iQ_z$ and $P_-=Q_t+iQ_z$, which is $2Q_t$ whatever the three vector coefficients are. The $4\times4$ trace is twice the block trace because of the two tensor factors, and the factor $2$ is the number of Peirce planes.

**The trace of a word of two.** The four products have the four traces
$$
\operatorname{Tr}(L_1L_2)=4P,\qquad \operatorname{Tr}(L_1^{\mathsf T}L_2)=4N,\qquad
\operatorname{Tr}(L_1L_2^{\dagger})=4H,\qquad \operatorname{Tr}(L_1^{\mathsf T}L_2^{\dagger})=4\mathrm{Kr},
$$
each twice the trace of the corresponding block product. The identities are the four forms of §*The Four Forms* multiplied by four, and their block versions are the same four statements with $4$ replaced by $2$.

**The trace of a product is not the product of the traces.** The two sides are $4(Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2))$ and $16Q_{1t}Q_{2t}$, and they differ by $4(3Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2))$. The block form is $\operatorname{Tr}(A_1A_2)=2(Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2))$ against $2Q_{1t}\cdot2Q_{2t}$, and the gap is $2(Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2))$, which is not the half of the $4\times4$ gap. No frame repairs this, because the trace of the identity is the dimension.

**The mixed trace.** The one trace that needs the two families is
$$
\operatorname{Tr}(L_1R_2)=4Q_{1t}Q_{2t}.
$$
Its block reading is the trace over the two tensor factors of $\mathrm I_2\otimes A_1$ against $A_2^{\mathsf T}\otimes\mathrm I_2$, and it exists only at this size: the compression to one plane loses the second factor and with it the statement. The counterpart $A_1A_2^{\mathsf T}$ has trace $2\mathrm{Sc}(\tilde Q_1\varrho(\tilde Q_2))$ for the reflection $\varrho=\operatorname{diag}(1,-1,1,-1)$, which is a different number, and the difference is the subject of §*The Product* of *$M_2(\mathbb{C})$ Pauli Representation*.

**What the trace cannot see.** As in the axis-free article, the trace sees the symmetric part of a product and nothing of the antisymmetric part, and it sees $Q_t$ and nothing of the vector part of an element. The four zeros of the trace column of §*The Twelve Products* are the first blindness, and $\operatorname{Tr}A=2Q_t$ is the second.

## The Determinant

**The determinant of one matrix.** For every $\tilde Q$,
$$
\det A=\langle\tilde Q\rangle_{\natural}=N(\tilde Q),\qquad \det L(\tilde Q)=\det R(\tilde Q)=\det(A)^2=N(\tilde Q)^2,
$$
the $4\times4$ determinant being the square of the block determinant because the block is repeated twice. The characteristic polynomial of $L$ is $\bigl((\lambda-Q_t)^2+B^2\bigr)^2$, and that of $A$ is the same polynomial without the square, with the two roots $Q_t\pm iB$.

**The determinant of a product of matrices.** For all $\tilde Q_1,\tilde Q_2$,
$$
\det(A_1A_2)=\det A_1\det A_2,\qquad\text{that is}\qquad N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)N(\tilde Q_2),
$$
and at the $4\times4$ size the same statement squared, $N(\tilde Q_1\tilde Q_2)^2=N(\tilde Q_1)^2N(\tilde Q_2)^2$. The block form is the sharper one: it is the multiplicativity of the quaternionic norm without the sign ambiguity of the squared statement, and it is available here because one block is the whole element.

**The other three rows.** With $\det A^{\dagger}=\overline{\det A}$ and $\det A^{\mathsf T}=\det A$,
$$
\det(A_1^{\natural}A_2)=N(\tilde Q_1)N(\tilde Q_2),\qquad
\det(A_1A_2^{\dagger})=N(\tilde Q_1)\overline{N(\tilde Q_2)},
\qquad
\det(A_1^{\natural}A_2^{\dagger})=N(\tilde Q_1)\overline{N(\tilde Q_2)}.
$$
The first is the quaternionic product read again, since the congruence $\sigma_2A^{\mathsf T}\sigma_2$ has determinant $\det A$. The last two pair the determinant with its conjugate, so the sesquilinear rows are conjugate-multiplicative, which is the determinant's version of the split between the bilinear and the sesquilinear words.

**The determinant is the only word that factors.** Of the four quadratic words of the four norms, $\tfrac14\operatorname{Tr}(L^{\mathsf T}L)$ is the only one that is a scalar matrix, and its scalar is $N$; $\det L=N^2$ is the only one that factors across a product with no conjugate. The plain word $\tfrac14\operatorname{Tr}(L^2)$ factors on no pair and is the subject of §*The Four Norms*.

**The rank.** The rank of $L$ is twice that of $A$, and the possible values are $0$, $2$ and $4$. The rank drops exactly when $N(\tilde Q)=0$, that is on the zero-divisor cone of *Zero Divisors and Invertibles in the Biquaternion Algebra*, and the two tensor factors explain why an odd rank never occurs.

## The Four Norms

**The four words at two equal arguments.** The four norms are the four forms on the diagonal, and their words in the two sizes are
$$
P=\tfrac14\operatorname{Tr}(L^2)=\tfrac12\operatorname{Tr}(A^2),\qquad
N=\tfrac14\operatorname{Tr}(L^{\mathsf T}L)=\tfrac12\operatorname{Tr}(A^{\natural}A),
$$
$$
H=\tfrac14\operatorname{Tr}(L^{\dagger}L)=\tfrac12\operatorname{Tr}(A^{\dagger}A),\qquad
\mathrm{Kr}=\tfrac14\operatorname{Tr}(L^{\mathsf T}L^{\dagger})=\tfrac12\operatorname{Tr}(A^{\natural}A^{\dagger}).
$$
The four letters, the four coordinate expressions and the four inertias are those of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

**The quaternionic norm is an eigenvalue of the block.** The second word is not merely a trace:
$$
A^{\natural}A=AA^{\natural}=N(\tilde Q)\,\mathrm I_2,\qquad
L^{\mathsf T}L=N(\tilde Q)\,\mathrm I_4 .
$$
The block identity follows from $A^{\natural}=\sigma_2A^{\mathsf T}\sigma_2$ and the explicit entries: the two diagonal entries of $A^{\natural}A$ are equal to $N(\tilde Q)$ and its two off-diagonal entries vanish, so the matrix is $N(\tilde Q)\mathrm I_2$ and the single number $N$ is read twice on the diagonal. That number is also $\det A$, which is the reason the collapse and the determinant agree. The $4\times4$ identity is the same statement with $\mathrm I_2\otimes$ in front. The collapse is the matrix form of $\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_t$.

**The Hermitian norm is the Hilbert–Schmidt square.** Since $\operatorname{Tr}(A^{\dagger}A)=\sum_{ij}|A_{ij}|^2$,
$$
\tfrac12\operatorname{Tr}(A^{\dagger}A)=\tfrac12\lVert A\rVert_{\mathrm{HS}}^2=H(\tilde Q),
\qquad
\tfrac14\operatorname{Tr}(L^{\dagger}L)=\tfrac14\lVert L\rVert_{\mathrm{HS}}^2=H(\tilde Q),
$$
and the two agree because the Hilbert–Schmidt norm of $\mathrm I_2\otimes A$ is twice that of $A$. It is the only one of the four that is positive definite, of inertia $(8,0)$ on the real algebra.

**The Krein norm is the mixed word.** The fourth pairs the transpose with the dagger,
$$
\tfrac12\operatorname{Tr}(A^{\natural}A^{\dagger})=\mathrm{Kr}(\tilde Q),
$$
which is positive on the centre and negative on the vector subspace, of inertia $(2,6)$.

**The multiplicativity table.**

| Norm | $4\times4$ word | Block | Multiplicative | Definite | Value ring |
|---|---|---|---|---|---|
| $P$ | $\tfrac14\operatorname{Tr}(L^2)$ | $\tfrac12\operatorname{Tr}(A^2)$ | no | no | $\mathbb{C}$ |
| $N$ | $\tfrac14\operatorname{Tr}(L^{\mathsf T}L)$ | $\det A$ | yes | no | $\mathbb{C}$ |
| $H$ | $\tfrac14\operatorname{Tr}(L^{\dagger}L)$ | $\tfrac12\lVert A\rVert^2_{\mathrm{HS}}$ | no | yes | $\mathbb{R}$ |
| $\mathrm{Kr}$ | $\tfrac14\operatorname{Tr}(L^{\mathsf T}L^{\dagger})$ | $\tfrac12\operatorname{Tr}(A^{\natural}A^{\dagger})$ | no | no | $\mathbb{R}$ |

The multiplicativity column is that of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the two word columns are the contribution of this article, and the block column is the one that shows why $N$ is written $\det A$: at the element size the only multiplicative word is the determinant itself.

**The defect of the plain norm.** Write $\tilde Q_a=s_a+\vec Q_a$ with $s_a=Q_{at}$. Then
$$
P(\tilde Q_1\tilde Q_2)-P(\tilde Q_1)P(\tilde Q_2)
=-2(\vec Q_1\times\vec Q_2,\vec Q_1\times\vec Q_2)-4s_1s_2(\vec Q_1,\vec Q_2),
$$
by the expansion of the axis-free article, and the identity is the same in this frame because it involves no matrix. In words: the plain norm fails to be multiplicative by minus twice the norm of the antisymmetric part of the product, minus four times the two scalar parts times the dot product of the two vector parts. The first term is the square of the cross product, and the second vanishes when either scalar part vanishes, so a pair of pure vectors has the defect $-2(\vec Q_1\times\vec Q_2,\vec Q_1\times\vec Q_2)$ and nothing else.

**The two other defects, by witness.** The Hermitian norm fails on $\tilde Q=\vec e_x+i\vec e_y$, which has $H(\tilde Q)=2$ and square $0$. The Krein norm fails on $\tilde Q=e_t+\vec e_x$, which has $\mathrm{Kr}(\tilde Q)=0$ and square $2\vec e_x$ with $\mathrm{Kr}=-4$. In the block the two witnesses are the matrices
$$
A(\vec e_x+i\vec e_y)=\begin{pmatrix}0&-2i\\0&0\end{pmatrix},\qquad A(e_t+\vec e_x)=\begin{pmatrix}1&-i\\-i&1\end{pmatrix},
$$
of determinant $0$ and $2$. The first is a zero divisor, as the vanishing of $N$ requires, and it is the reason $H$ has no factorisation. The second is invertible, of inverse $e_t-\vec e_x$ up to the factor $\tfrac12$, and a multiplicative $\mathrm{Kr}$ would then need $\mathrm{Kr}(e_t)=\mathrm{Kr}(\tilde Q)\mathrm{Kr}(\tilde Q^{-1})=0$, against $\mathrm{Kr}(e_t)=1$. The witness is therefore decisive and not merely a coincidence of two values.

**Why only $N$ is scalar.** The three other products $A^2$, $A^{\dagger}A$ and $A^{\natural}A^{\dagger}$ are not scalar matrices, and their traces are the three norms. The reason is the one of the axis-free article: $\natural$ is the only one of the three conjugations whose product with the element is a scalar, and ${}^{*}$ is not, because $\tilde Q^{*}\tilde Q$ has a vector part as soon as $\tilde Q$ is complex. The frame's contribution is that $A^{\natural}$ is a congruence of the transpose, so the collapse is visible as the vanishing of the off-diagonal entries.

## The Factors

**Two factors, one source.** The $4\times4$ size carries the factor $4$ and the block carries the factor $2$, and both are the trace of an identity:
$$
\operatorname{Tr}\mathrm I_4=4,\qquad \operatorname{Tr}\mathrm I_2=2,\qquad \operatorname{Tr}(\mathrm I_2\otimes X)=2\operatorname{Tr}X .
$$

| Quantity | $4\times4$ | Block | Factor |
|---|---|---|---|
| scalar part | $\tfrac14\operatorname{Tr}L$ | $\tfrac12\operatorname{Tr}A$ | $1/\dim$ |
| trace of an element | $4Q_t$ | $2Q_t$ | $\dim$ |
| form | $\tfrac14\operatorname{Tr}(L_1L_2)$ | $\tfrac12\operatorname{Tr}(A_1A_2)$ | $1/\dim$ |
| norm | $\tfrac14\operatorname{Tr}(L^{\mathsf T}L)$ | $\tfrac12\operatorname{Tr}(A^{\natural}A)$ | $1/\dim$ |
| the determinant of the image | $N^2$ | $N$ | no factor |
| determinant of the identity | $1$ | $1$ | $\det\mathrm I=1$ |

**Where each factor comes from.** The trace of the identity is the dimension of the space the matrix acts on. At the $4\times4$ size that space is the algebra, of complex dimension four, and the identity is one tensor factor of dimension two times a block of dimension two. The scalar part is one coordinate out of four at the first size and one row out of two at the second, so the same quarter and half appear in the same places. The determinant is normalised at the identity and carries no factor.

**The square is the tensor repetition.** The determinant squares from the block to the $4\times4$ matrix because the block appears twice, and the trace doubles for the same reason. Additive quantities double, multiplicative quantities square, and the quadratic words quadruple. This is the route from *$M_4(\mathbb{C})$ Pauli Representation* to *$M_2(\mathbb{C})$ Pauli Representation* read on words of two matrices instead of on words of one.

**The half in the sesquilinear words.** The two sesquilinear forms carry the same factor as the two bilinear ones, and no extra half appears. The conjugation does not change the dimension of the carrier and therefore does not change the constant. The only structure that the sesquilinear family adds is the conjugate in the second slot, visible in $\det(A_1A_2^{\dagger})=N(\tilde Q_1)\overline{N(\tilde Q_2)}$ and nowhere in the constants.

## What the Peirce Frame Gives

**The block structure.** Every word of §*The Twelve Products* is a $2\times2$ word in this frame, and four of them are the plain operations of the matrix algebra: the product, its anticommutator, its commutator and the dagger product. A reader who knows $M_2(\mathbb{C})$ reads half the table at sight. In the axis-free frame the same four words are dense $4\times4$ expressions with integer entries, and none of them is a plain operation.

**The price in $\sigma_2$.** The three companion rules of §*The Two Elements in the Peirce Frame* put $\sigma_2$ into the quaternionic words: $A^{\natural}=\sigma_2A^{\mathsf T}\sigma_2$ and $A^{c}=\sigma_2\overline{A}\sigma_2$. Seven of the twelve words carry it, and none of the seven is a commutator of literal blocks. In the axis-free frame these seven rows are words in the two matrices, their transposes and their entrywise conjugates, with no other matrix present; the count there is higher by one, because the row that collapses to $N\mathrm I_2$ carries two transposes.

**The one rule that is free.** The dagger is free in both frames: $L(\tilde Q^{*})=L^{\dagger}$ and $A(\tilde Q^{*})=A^{\dagger}$ hold in the axis-free frame and here, because both frames are orthogonal for the Hermitian form, up to the common norm of the frame vectors. The two sesquilinear forms are therefore read without a congruence in both frames, and the two bilinear ones are read without a congruence in one only.

**The check that the two frames agree.** The change matrix $\mathsf C$ from the coefficient basis to the Peirce frame has determinant $-\tfrac14$, and every identity of this article is the corresponding identity of the axis-free article conjugated by $\mathsf C$. The four words of §*The Four Forms* are equal in the two frames because they are traces, and the four Gram matrices differ by the congruence of the same section. The conjugation is a check on the article: no trace word, no determinant and no norm of this article depends on the frame, and only the displays do.

**The three frames in one sentence each.** In the axis-free frame the twelve words are polynomials in the two matrices and their transposes, and the price is a dense display; in the Peirce frame they are $2\times2$ words of the blocks, and the price is the congruence $\sigma_2$ in the seven rows whose word conjugates a slot; at the element size the words are the same $2\times2$ words with the constants $\tfrac12$ and $2$, and the mixed trace has no word at all.

## Summary

The four forms are $\tfrac14$ of the four $4\times4$ trace words and $\tfrac12$ of the four block trace words, and the factor of two between them is $\operatorname{Tr}\mathrm I_2$. The plain product is $A_1A_2$ on the block, its symmetric part is the anticommutator, its antisymmetric part is the commutator, and the commutator is traceless, so the trace sees the four products and their symmetrisations and nothing of the four antisymmetrisations. The quaternionic symmetric part is the form times the identity, $\tfrac12(A_1^{\natural}A_2+A_2^{\natural}A_1)=N(\tilde Q_1,\tilde Q_2)\mathrm I_2$, and the corresponding single-element statement is $A^{\natural}A=N(\tilde Q)\mathrm I_2$.

The frame puts $\sigma_2$ into three of its four companion rules: $A^{\natural}=\sigma_2A^{\mathsf T}\sigma_2$ and $A^{c}=\sigma_2\overline{A}\sigma_2$ are congruences, and only $A^{*}=A^{\dagger}$ is free. Nine rows have a conjugated slot in the element and seven of them carry the congruence in the block: the dagger is free, and the collapse of the quaternionic symmetric row cancels the other two. In the axis-free frame the nine are literal words in the matrices, their transposes, their entrywise conjugates and their daggers; here seven are words in the two blocks and the two congruences. Neither display is the algebra, and the table of §*The Twelve Products*, read in both frames, is the algebra.

The constants are the trace of the identity and its reciprocal: $4$ and $\tfrac14$ at the full size, $2$ and $\tfrac12$ at the block, and no constant at all for the determinant. The determinant of the $4\times4$ matrix is the square of the block determinant, and the multiplicativity of the quaternionic norm is sharper on the block, where it reads $N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)N(\tilde Q_2)$ and not only its square. The defect of the plain norm is the same in every frame, since it involves no matrix: minus twice the square of the cross product, minus four times the two scalar parts times the dot product of the two vector parts.

The Gram matrices of the four forms in this frame are half-integer arrays, of which only the Hermitian one is diagonal, where the axis-free frame has the sign matrix and the identity. The forms are the same in the two frames; the arrays are not, and the congruence $[\text{form}]_{\mathcal P}=\mathsf C^{\mathsf T}[\text{form}]_{\mathcal E}\mathsf C$ with $\det\mathsf C=-\tfrac14$ is the whole of the difference.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{P}$ | the standard Peirce frame $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ |
| $A_a$ | $\mathsf M_2(\tilde Q_a)$, the block of $\tilde Q_a$, $a=1,2$ |
| $A_a^{\natural}$, $A_a^{c}$, $A_a^{*}$ | $\sigma_2A_a^{\mathsf T}\sigma_2$, $\sigma_2\overline{A_a}\sigma_2$, $A_a^{\dagger}$ |
| $L_a$, $R_a$ | $\mathrm I_2\otimes A_a$ and $A_a^{\mathsf T}\otimes\mathrm I_2$ |
| $C_L$ | $\mathrm I_2\otimes\sigma_2$, the congruence of the transpose and of the entrywise conjugate |
| $\sigma_2$ | $\begin{pmatrix}0&-i\\i&0\end{pmatrix}$, of square $\mathrm I_2$ |
| $P_\pm$, $X_\pm$ | $Q_t\mp iQ_z$ and $-iQ_x\pm Q_y$, the four Peirce coordinates |
| $\tilde Q_1\bullet\tilde Q_2$, $\tilde Q_1\wedge\tilde Q_2$ | the symmetric and antisymmetric plain bilinear products |
| $\tilde Q_1\bullet_{\natural}\tilde Q_2$, $\tilde Q_1\wedge_{\natural}\tilde Q_2$ | the quaternionic bilinear pair, the first a scalar equal to $N$ |
| $\tilde Q_1\bullet_*\tilde Q_2$, $\tilde Q_1\wedge_*\tilde Q_2$ | the plain sesquilinear pair, exchange with the coefficient conjugation |
| $\tilde Q_1\bullet_{\natural*}\tilde Q_2$, $\tilde Q_1\wedge_{\natural*}\tilde Q_2$ | the quaternionic sesquilinear pair |
| $P$, $N$, $H$, $\mathrm{Kr}$ | the plain, quaternionic, Hermitian and Krein forms and norms |
| $\mathsf C$ | the change matrix from the coefficient basis, of determinant $-\tfrac14$ |
| $[\,\cdot\,]_{\mathcal P}$, $[\,\cdot\,]_{\mathcal E}$ | the Gram matrix of a form in the Peirce and in the axis-free frame |

## Further Reading

- [$M_4(\mathbb{C})$ Pauli Representation](m4c-pauli-representation.html), for the frame, the two displays and the compression.
- [$M_4(\mathbb{C})$ Axis-Free Representation : Products, Forms and Norms](m4c-axis-free-representation-products-forms-norms.html), for the same content in the coefficient basis, with the transpose as the conjugation.
- [$M_2(\mathbb{C})$ Pauli Representation : Products, Forms and Norms](m2c-pauli-representation-products-forms-norms.html), for the same content at the element size.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four forms and the four norms without matrices.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the two exchanges and the twelve products.
- [Families of Matrix Representations](families-of-matrix-representations.html), for the change of frame and the congruence of the Gram matrices.
- [The Element, the Coordinates and the Conjugations in the Biquaternion Algebra](the-element-the-coordinates-and-the-conjugations-in-the-biquaternion-algebra.html), for the three conjugations.
- [Zero Divisors and Invertibles in the Biquaternion Algebra](zero-divisors-and-invertibles-in-the-biquaternion-algebra.html), for the cone $\langle\tilde Q\rangle_{\natural}=0$ and the rank.
- [The Biquaternion Algebra](introduction-to-the-algebra-of-biquaternions.html), for the algebra and the multiplication table.
