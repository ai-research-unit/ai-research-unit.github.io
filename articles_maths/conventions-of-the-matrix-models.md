# __Conventions of the Matrix Models__

## Introduction

The algebra is read in matrices in two ways, and the two answer different questions. The **$2\times2$ isomorphism** $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ reads the element itself as a complex matrix of the algebra's own size; the **$4\times4$ regular representation** reads multiplication as a linear map on the algebra taken as a complex vector space, and its image is a four-dimensional subalgebra of the ambient $M_4(\mathbb{C})$.

The algebra is $M_2(\mathbb{C})$ and it is never $M_4(\mathbb{C})$. The ambient $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ is the operator algebra, it carries no biquaternion structure and takes no biquaternion name; the left and right copies are named $\mathbb{B}_L$ and $\mathbb{B}_R$, and the retired label $M_4(\mathbb{C})_L$ is read as $\mathbb{B}_L$.

The order is: the table of objects, the $2\times2$ isomorphism with its four forced images and its trace and determinant, the $4\times4$ regular representation in the canonical Peirce frame, and the Clifford structure of the cells that closes it. The article assumes the base of *Conventions in Mathematics* and the Peirce convention of *Conventions of the Special Elements and the Peirce Decomposition*, whose standard pair fixes the frame.

## The Matrix Models

**The biquaternion algebra is $M_2(\mathbb{C})$, and it is never $M_4(\mathbb{C})$.** Two kinds of matrix model read it, and they answer different questions. The **isomorphism** $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ reads the element itself as a $2\times2$ complex matrix, of the algebra's own size. The **regular representation** reads multiplication as a linear map on the algebra taken as a complex vector space, and its target is $\mathrm{End}_{\mathbb{C}}(\mathbb{B})=M_4(\mathbb{C})$; its image is a four-dimensional subspace of that ambient algebra, not the ambient algebra. The two are different representations, not two sizes of one.

| object | writing | meaning |
|---|---|---|
| the algebra | $\mathbb{B}$ | $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ |
| the isomorphism | $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | the element read as a $2\times2$ matrix |
| the ambient | $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ | operators on the algebra as a vector space |
| the left copy | $\mathbb{B}_L=M_4(\mathbb{C})_{\mathbb{B},L}=\rho_L(\mathbb{B})$ | four-dimensional subalgebra |
| the right copy | $\mathbb{B}_R=M_4(\mathbb{C})_{\mathbb{B},R}=\rho_R(\mathbb{B})$ | the commutant of $\mathbb{B}_L$ |
| the matrix of an element | $\mathsf{M}_4^{L}(\tilde Q)$, $\mathsf{M}_4^{R}(\tilde Q)$ | the matrices of $\rho_L(\tilde Q)$, $\rho_R(\tilde Q)$ in the frame the article names; canonical by default |

### The 2×2 Isomorphism

**The map.** The isomorphism is $\mathbb{C}$-linear, multiplicative and bijective,
$$
\mathsf{M}_2:\mathbb{B}\longrightarrow M_2(\mathbb{C}),\qquad
\mathsf{M}_2(\tilde Q_1+\tilde Q_2)=\mathsf{M}_2(\tilde Q_1)+\mathsf{M}_2(\tilde Q_2),\qquad
\mathsf{M}_2(\tilde Q_1\tilde Q_2)=\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2),
$$
and it is the reading every numerical check in the corpus is performed with.

**The four unit images.** The images of the units are fixed once, because every article depends on them agreeing:
$$
\mathsf{M}_2(e_t)=I_2,\qquad
\mathsf{M}_2(\vec e_x)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf{M}_2(\vec e_y)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf{M}_2(\vec e_z)=\begin{pmatrix}-i&0\\0&i\end{pmatrix},
$$
with $\mathsf{M}_2(i)=iI_2$ on the central scalar. The three vector images are $-i\sigma_k$, with $\sigma_k$ the Pauli matrices, and $\mathbb{C}$-linearity gives the Hermitian units, $\mathsf{M}_2(i\vec e_k)=i\,\mathsf{M}_2(\vec e_k)$.

**The assignment is forced.** $\vec e_k^2=-e_t$ requires the factor $i$, and $\vec e_x\vec e_y=\vec e_z$ fixes the sign. The three images cannot be made real, nor all three negated; *The $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* derives both.

**No frame is needed.** The isomorphism is a map of algebras and does not depend on a frame of $\mathbb{B}$. The four matrices above are the images of the units, not the entries of a matrix read in a basis, and no Peirce family enters. The frame enters only in the regular representation of §*The 4×4 Regular Representation*, which reads an operator on the algebra.

**The invariants.** The determinant of the image is the biquaternion norm and its trace is twice the scalar part,
$$
\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural},\qquad
\operatorname{tr}\mathsf{M}_2(\tilde Q)=2Q_t .
$$
The determinant is multiplicative, which is what makes the matrix model compute every norm in the corpus; the invertibility criterion, the group of units and the unit-norm group are read from it.

### The 4×4 Regular Representation

**The maps.** Left multiplication is the linear map $\rho_L:\mathbb{B}\to\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, $\rho_L(\tilde Q_1)(\tilde Q_2)=\tilde Q_1\tilde Q_2$, and right multiplication is $\rho_R(\tilde Q_1)(\tilde Q_2)=\tilde Q_2\tilde Q_1$. The target is the ambient operator algebra $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$.

**The copy is named, the ambient is not.** The left copy is $\mathbb{B}_L=\rho_L(\mathbb{B})$, also written $M_4(\mathbb{C})_{\mathbb{B},L}$, and the right copy is $\mathbb{B}_R=\rho_R(\mathbb{B})$, also written $M_4(\mathbb{C})_{\mathbb{B},R}$. Each is a subalgebra of $M_4(\mathbb{C})$ isomorphic to $M_2(\mathbb{C})$, and $\mathbb{B}_R$ is the commutant of $\mathbb{B}_L$ in $M_4(\mathbb{C})$.

A bare $M_4(\mathbb{C})_{\mathbb{B}}$ means the left copy; the side is $L$ unless written. The ambient $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ is an operator algebra, carries no biquaternion structure and takes no biquaternion name.

**The subscript names the action, not a tensor slot.** $L$ is left multiplication and $R$ is right multiplication, read as on $L_{\tilde Q}$ and $R_{\tilde Q}$ in *Conventions of the Operators and the Differential Calculus*, §*The Operators*. In the canonical frame below the left copy is the second tensor factor and the right copy the first, and another choice of frame exchanges the two slots without exchanging the two actions. A subscript naming a slot would therefore change meaning with the frame, and the action does not.

**The canonical frame is the Peirce frame of the standard pair.** The matrix model fixes the family and the two mixed units,
$$
\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z),\qquad
\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y),
$$
which satisfy
$$
\tilde\Pi_+^2=\tilde\Pi_+,\quad \tilde\Pi_-^2=\tilde\Pi_-,\quad \tilde\Pi_+\tilde\Pi_-=0,\quad
\vec\Upsilon_\pm^2=0,\quad \vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\quad \vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+ .
$$
So $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ is a Peirce basis, and the frame is that basis in that order: the two elements of $\mathbb{B}\tilde\Pi_+$ first and those of $\mathbb{B}\tilde\Pi_-$ second. This is the frame of the $\mathsf{M}_2$ model, and it is a choice of frame inside the matrix model. The Peirce convention fixes no family (*Conventions of the Special Elements and the Peirce Decomposition*, §*The Biquaternion Peirce Convention*), and the choice here is not a preferred pair: it is the frame the matrix model is written in.

**In this frame the two copies are the two tensor factors.**
$$
\rho_L(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q),\qquad
\rho_R(\tilde Q)=\mathsf{M}_2(\tilde Q)^{\mathsf T}\otimes I_2 .
$$
So the left copy is the set of matrices $I_2\otimes A$ and the right copy the set $B\otimes I_2$: in the $4\times4$ matrix of an element the four blocks are $\mathsf{M}_2(\tilde Q)$, $0$, $0$, $\mathsf{M}_2(\tilde Q)$ on the left, and $M_{11}I_2$, $M_{21}I_2$, $M_{12}I_2$, $M_{22}I_2$ on the right, where $M_{ij}$ are the entries of $\mathsf{M}_2(\tilde Q)$. The regular matrix is the $2\times2$ matrix taken twice.

**The four unit matrices.** The left images of the four units are
$$
\mathsf{M}_4^{L}(e_t)=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
\mathsf{M}_4^{L}(\vec e_x)=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},
$$
$$
\mathsf{M}_4^{L}(\vec e_y)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
\mathsf{M}_4^{L}(\vec e_z)=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix},
$$
each equal to $I_2\otimes\mathsf{M}_2(\vec e_k)$. A general element is their linear combination, $\mathsf{M}_4^{L}(\tilde Q)=Q_t\mathsf{M}_4^{L}(e_t)+Q_x\mathsf{M}_4^{L}(\vec e_x)+Q_y\mathsf{M}_4^{L}(\vec e_y)+Q_z\mathsf{M}_4^{L}(\vec e_z)$.

**The invariants.** With $\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ and $\operatorname{tr}\mathsf{M}_2(\tilde Q)=2Q_t$,
$$
\det\mathsf{M}_4^{L}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^{2},\qquad
\operatorname{tr}\mathsf{M}_4^{L}(\tilde Q)=4Q_t .
$$

**The gamma frame.** The five Dirac generators are two-sided operators of the canonical frame, with $L$ and $R$ the left and right multiplications of *Conventions of the Operators and the Differential Calculus*, §*The Operators*:
$$
\gamma^0=iR_{\vec e_x},\qquad
\gamma^1=iL_{\vec e_x}R_{\vec e_y},\qquad
\gamma^2=iL_{\vec e_y}R_{\vec e_y},\qquad
\gamma^3=iL_{\vec e_z}R_{\vec e_y},\qquad
\gamma_5=-iR_{\vec e_z}.
$$
In the canonical frame their matrices are
$$
\gamma^0=\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
\gamma^1=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},
$$
$$
\gamma^2=\begin{pmatrix}0&0&0&-i\\0&0&i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},\qquad
\gamma^3=\begin{pmatrix}0&0&1&0\\0&0&0&-1\\-1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
\gamma_5=\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},
$$
and they satisfy $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4$ and $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$. The sixteen products of the frame are the sixteen cells $L_{e_\mu}R_{e_\nu}$, each with a coefficient of unit modulus; the table, the proof and the choice of frame are §*A Gamma Frame, and the Choice Behind It* of *$M_4(\mathbb{C})$ Representation : The Two-Sided Operators on the Biquaternion Algebra*. The frame is one frame among many: another orthogonal pair gives another set of five matrices, the relations survive, and the cell labels do not.

**The frame is not the object.** Another gauge, another order of the four basis elements, or another Peirce family gives another matrix of the same operator; the two formulas above hold in the canonical frame alone. An article that uses another frame says so and gives the change of frame. What the frame does not change is the copy and the element: the matrix is an image of the element, never the element and never the algebra.

**The explicit matrices are written in the canonical frame.** The model articles display $\mathsf{M}_4^{L}(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q)$ in the canonical Peirce frame. The coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ is the conjugate display $C_{\Pi}(I_2\otimes\mathsf{M}_2)C_{\Pi}^{-1}$, with the Peirce change $C_{\Pi}$ of *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*. The articles whose subject is the transpose dictionary use the coefficient basis, because quaternion conjugation is transposition there, and each declares it. An article that uses another frame declares it; an entry is read only with the frame that produced it.

**The label $M_4(\mathbb{C})_L$ is retired.** It named a matrix set rather than an algebra, and it changed meaning with the basis. An older article that writes $M_4(\mathbb{C})_L$ is read as $M_4(\mathbb{C})_{\mathbb{B},L}$, and one that writes $M_4(\mathbb{C})_R$ as $M_4(\mathbb{C})_{\mathbb{B},R}$. The same rule governs the matrices: a bare $\mathsf{M}_4$ is not written for a regular matrix, which carries the superscript $L$ or $R$.

### The Clifford Structure

**The Clifford algebra is the cell algebra.** The sixteen cells $T_{e_\mu,e_\nu}=L_{e_\mu}R_{e_\nu}$ are linearly independent, and their complex span is all of $M_4(\mathbb{C})$. They multiply by $T_{e_\mu,e_\nu}T_{e_\rho,e_\sigma}=T_{e_\mu e_\rho,\,e_\sigma e_\nu}$, so the assignment $e_\mu\otimes e_\nu^{\mathrm{opp}}\mapsto T_{e_\mu,e_\nu}$ is an algebra isomorphism
$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\longrightarrow M_4(\mathbb{C})\cong\mathrm{Cl}_{1,3}(\mathbb{C}).
$$
The sixteen products of the five generators span over $\mathbb{R}$ the algebra $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$, of real dimension $16$, and the sixteen cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$, the opposite real form. The Dirac, Weyl and Majorana matrices are three bases of the same complex algebra, related by a change of gamma basis; a change of gamma basis is a change of frame, not a change of object.

**The opposite algebra is written with three letters.** The opposite of an algebra, with the product reversed, carries the superscript $\mathrm{opp}$: the reversed product is $a\cdot_{\mathrm{opp}}b=ba$, and the opposite of $\mathbb{B}$ is $\mathbb{B}^{\mathrm{opp}}$. The two-letter form $\mathrm{op}$ is reserved for the operator norm $\|A\|_{\mathrm{op}}$, not for the opposite algebra.

**The comparison map.** The $\mathbb{R}$-linear map $\iota_{\mathrm{Cl}}$ of the Dirac articles is read in cells as $\iota_{\mathrm{Cl}}(e_\mu)=T_{e_\mu,e_t}$ and $\iota_{\mathrm{Cl}}(i)=T_{e_t,e_z}$, equivalently $\iota_{\mathrm{Cl}}(\vec e_x)=\gamma^2\gamma^3$, $\iota_{\mathrm{Cl}}(\vec e_y)=\gamma^3\gamma^1$, $\iota_{\mathrm{Cl}}(\vec e_z)=\gamma^1\gamma^2$ and $\iota_{\mathrm{Cl}}(i)=-\gamma^0\gamma^1\gamma^2\gamma^3$. Its image is the real span of the eight cells $T_{e_\mu,e_t}$ and $T_{e_\mu,e_z}$, of real dimension $8$, and it satisfies $\iota_{\mathrm{Cl}}(i\tilde Q)=T_{e_t,e_z}\,\iota_{\mathrm{Cl}}(\tilde Q)$. It is $\mathbb{R}$-linear and not $\mathbb{C}$-linear: it is the comparison with the even subalgebra of $\mathrm{Cl}_{1,3}$, not a second representation of $\mathbb{B}$.

## Summary

The **$2\times2$ isomorphism** $\mathsf{M}_2$ is fixed by four images: $e_t\mapsto I_2$, the three vector units to $-i$ times the Pauli matrices, and $\mathsf{M}_2(i)=iI_2$ on the central scalar. The assignment is forced by $\vec e_k^2=-e_t$ and by $\vec e_x\vec e_y=\vec e_z$. The trace of the image is twice the scalar part, the determinant is the biquaternion norm $\langle\tilde Q\rangle_{\natural}$, and the determinant is multiplicative, which is what makes the matrix model compute every norm in the corpus.

The **$4\times4$ regular representation** is $\rho_L(\tilde Q_1)(\tilde Q_2)=\tilde Q_1\tilde Q_2$ and $\rho_R(\tilde Q_1)(\tilde Q_2)=\tilde Q_2\tilde Q_1$. The image of $\rho_L$ is the four-dimensional subalgebra $\mathbb{B}_L=M_4(\mathbb{C})_{\mathbb{B},L}$ of the ambient $M_4(\mathbb{C})$, and $\mathbb{B}_R=M_4(\mathbb{C})_{\mathbb{B},R}$ is its commutant; the ambient is an operator algebra and takes no biquaternion name. The side is $L$ unless written.

The **canonical frame** is the Peirce frame of the standard pair: $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ and $\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y)$, with the four Peirce components in the order $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$. In it the left matrix is $I_2\otimes\mathsf{M}_2(\tilde Q)$ and the right matrix is $\mathsf{M}_2(\tilde Q)\otimes I_2$, with the left coupling to the second tensor factor and the right to the first.

The label $M_4(\mathbb{C})_L$ is retired: it named a matrix set rather than an algebra, and it changed meaning with the basis. An older article that writes it is read as $\mathbb{B}_L$, and an older $M_4(\mathbb{C})_R$ as $\mathbb{B}_R$.

The **Clifford structure** is the algebra of the cells: $e_\mu\otimes e_\nu^{\mathrm{opp}}\mapsto T_{e_\mu,e_\nu}$ is an isomorphism onto $M_4(\mathbb{C})\cong\mathrm{Cl}_{1,3}(\mathbb{C})$, the sixteen gamma products span $\mathrm{Cl}_{1,3}(\mathbb{R})$ and the sixteen cells span $\mathrm{Cl}_{3,1}(\mathbb{R})$. The five generators of the canonical frame are cells up to a factor $i$, and a change of gamma basis is a change of frame. The map $\iota_{\mathrm{Cl}}$ is the $\mathbb{R}$-linear comparison with the even subalgebra, $\iota_{\mathrm{Cl}}(e_\mu)=T_{e_\mu,e_t}$ and $\iota_{\mathrm{Cl}}(i)=T_{e_t,e_z}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | The isomorphism of the element; $\mathsf{M}_2(e_t)=I_2$, $\mathsf{M}_2(\vec e_k)=-i\sigma_k$ |
| $\operatorname{Tr}\tilde Q=\operatorname{tr}\mathsf{M}_2(\tilde Q)$ | The trace, twice the scalar part |
| $\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ | The determinant, the biquaternion norm |
| $\rho_L,\rho_R$ | Left and right multiplication as linear maps |
| $\mathbb{B}_L=M_4(\mathbb{C})_{\mathbb{B},L}$ | The left copy, $\rho_L(\mathbb{B})$; $\mathbb{B}_R$ is its commutant |
| $\mathsf{M}_4^{L}(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q)$ | The left regular matrix in the canonical frame |
| $\mathsf{M}_4^{R}(\tilde Q)=\mathsf{M}_2(\tilde Q)\otimes I_2$ | The right regular matrix in the canonical frame |
| $T_{e_\mu,e_\nu}=L_{e_\mu}R_{e_\nu}$ | The sixteen cells; their complex span is $M_4(\mathbb{C})\cong\mathrm{Cl}_{1,3}(\mathbb{C})$ |
| $\gamma^\mu,\gamma_5$ | The generators of the canonical frame, cells up to a factor $i$ |
| $\iota_{\mathrm{Cl}}$ | The $\mathbb{R}$-linear comparison with the even subalgebra; $\iota_{\mathrm{Cl}}(e_\mu)=T_{e_\mu,e_t}$, $\iota_{\mathrm{Cl}}(i)=T_{e_t,e_z}$ |
| $\tilde\Pi_\pm$, $\vec\Upsilon_\pm$ | The standard pair and its two mixed units, which fix the frame |

## Further Reading

- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636. The biquaternion conjugations and the conventions of the complexified algebra in the applied literature.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022. The reduced biquaternion algebra of the engineering literature, its idempotent decomposition, its ring-valued norm and its transform.
- [$M_4(\mathbb{C})$ Representation : The Two-Sided Operators on the Biquaternion Algebra](m4c-representation-the-two-sided-operators-on-the-biquaternion-algebra.html), for the sixteen cells, the gamma frames and the proof of the cell table.
- [The Dirac Algebra and Biquaternions — A Dictionary](../articles_physics/the-dirac-algebra-and-biquaternions-a-dictionary.html), for the comparison with the even subalgebra and the gamma correspondence.
