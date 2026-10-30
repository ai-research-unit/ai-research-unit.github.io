# __$M_4(\mathbb{C})$ Representation : The Two-Sided Operators on the Biquaternion Algebra__

## Introduction

The $4\times4$ model reads each biquaternion $\tilde Q$ as one $4\times4$ matrix, its left regular matrix $\mathsf{M}_4^{L}(\tilde Q)$, whose image is the four-dimensional copy $M_4(\mathbb{C})_{\mathbb{B},L}$. This article is one of a series; it records the construction and one gamma frame, and it takes the frame of the corpus from *Conventions in Mathematics*, §*The Matrix Models*. That is a representation of the algebra $\mathbb{B}$ on itself by left multiplication: the image has complex dimension four, and the product is preserved.

The operator $x\mapsto a\,x\,b$ is not a left multiplication when $b$ is not a scalar. It needs the right multiplication as well. The pair $(a,b)$ defines the **two-sided operator**

$$
T_{a,b}(x)=a\,x\,b .
$$

The operators $T_{a,b}$ span the whole matrix algebra $M_4(\mathbb{C})$, of complex dimension sixteen. This article builds that representation and its sixteen basis matrices. The construction is the case $n=2$ of $M_n(\mathbb{C})\otimes M_n(\mathbb{C})^{\mathrm{opp}}\cong M_{n^2}(\mathbb{C})$; it is recorded as one construction route in *The Matrix Algebra $M_4(\mathbb{C})$*, §*A Construction from the Two-Sided Operators*.

**Three objects, three dimensions.** The carrier is the biquaternion algebra $\mathbb{B}$, of complex dimension four. Its left regular image $L(\mathbb{B})=\{\mathsf{M}_4^{L}(a)\}$ is a four-dimensional subalgebra of $M_4(\mathbb{C})$. The operator algebra is the tensor product

$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\;\cong\;\operatorname{End}_{\mathbb{C}}(\mathbb{B}),
$$

of complex dimension sixteen; its **matrix representation** in the canonical frame is $M_4(\mathbb{C})$. The sixteen basis matrices are the images of the sixteen elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$.

**The tensor-product question.** Three products must be kept apart. The Kronecker product $L_\mu\otimes L_\nu$ of two $4\times4$ matrices is a $16\times16$ matrix acting on $\mathbb{C}^4\otimes\mathbb{C}^4$; it is *not* the matrix of $x\mapsto e_\mu x e_\nu$. The Kronecker product of two $2\times2$ matrices *is* a $4\times4$ matrix, and in the canonical frame it gives the two-sided operators directly through the identification $\mathbb{B}\cong M_2(\mathbb{C})$; the formula is written below. The product that builds the sixteen is the tensor product of algebras, $e_\mu\otimes e_\nu^{\mathrm{opp}}\mapsto L_\mu R_\nu$, and in matrices it is the ordinary product of two $4\times4$ matrices.

**Conventions.** The algebra, the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and the matrix $\mathsf{M}_4^{L}$ are those of *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*. Write $L_a=\mathsf{M}_4^{L}(a)$ for left multiplication by $a$, and $R_b$ for right multiplication, $R_b(x)=x\,b$. Matrices are written in the canonical frame of *Conventions in Mathematics*, §*The Matrix Models*, the Peirce frame, where

$$
L_a=\mathrm I_2\otimes\mathsf M_2(a),
\qquad
\mathsf M_2(e_t)=\mathrm I_2,\quad \mathsf M_2(e_k)=-i\sigma_k .
$$

The coefficient basis $(t,x,y,z)$ is used only where it is named; there the matrix of quaternion conjugation is $D=\operatorname{diag}(1,-1,-1,-1)$, and $N(a)=\langle a\rangle_{\natural}=a_t^2+a_x^2+a_y^2+a_z^2$ is the quaternionic norm.

**Boundaries.** The abstract algebra, its two regular representations and its double centraliser are *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*. The family $\{T_{a,b}\}$, its composition, its adjoint and its type criteria are *Two-Sided Operators on the Biquaternion Algebra*. The model and its four-dimensional image are *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*. The one-sided families are *One-Sided Operators on the Biquaternion Algebra*. The congruence is *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Sandwich*, and the $2\times2$ model is *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*.

## The Four Left Matrices

**Definition.** The left regular matrix $L_a=\mathsf{M}_4^{L}(a)$ is the $4\times4$ matrix of $x\mapsto a\,x$ in the canonical frame. Its $j$-th column is the coordinate column of $a\,P_j$, with $(P_1,P_2,P_3,P_4)=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$; in the coefficient basis, where $P_j=e_j$, this is the coordinate column of $a\,e_j$.

The four basis matrices are

$$
L_t=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
L_x=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},
$$

$$
L_y=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
L_z=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix}.
$$

Equivalently

$$
L_t=\mathrm I_4,\qquad
L_x=-i\,\mathrm I_2\otimes\sigma_1,\qquad
L_y=-i\,\mathrm I_2\otimes\sigma_2,\qquad
L_z=-i\,\mathrm I_2\otimes\sigma_3,
$$

and a general element is

$$
L_a=\mathrm I_2\otimes\mathsf M_2(a)=
\begin{pmatrix}
a_t-ia_z&-ia_x-a_y&0&0\\
-ia_x+a_y&a_t+ia_z&0&0\\
0&0&a_t-ia_z&-ia_x-a_y\\
0&0&-ia_x+a_y&a_t+ia_z
\end{pmatrix}.
$$

**The image is four-dimensional.** The matrices $L_\mu$ are linearly independent, and every product $L_aL_b=L_{ab}$ stays in their span. So $L(\mathbb{B})$ is a copy of $\mathbb{B}$, not the whole of $M_4(\mathbb{C})$.

## The Four Right Matrices

**Definition.** The right multiplication is $R_b(x)=x\,b$. Its matrix is not $\mathsf{M}_4^{L}(b)$: the two families commute, and $R_b$ is the commuting partner of $L_b$.

**Proposition.** In the canonical frame

$$
R_b=\mathsf M_2(b)^{\mathsf T}\otimes\mathrm I_2 .
$$

*Proof.* Left multiplication is $L_a=\mathrm I_2\otimes\mathsf M_2(a)$, so it acts on the second tensor factor. Right multiplication acts on the first: if $X=\mathsf M_2(x)$ is the $2\times2$ matrix of $x$, then $\mathsf M_2(xb)=X\mathsf M_2(b)$, and on the vectorised matrix $\operatorname{vec}X$ the map is $\operatorname{vec}X\mapsto\operatorname{vec}(X\mathsf M_2(b))=(\mathsf M_2(b)^{\mathsf T}\otimes\mathrm I_2)\operatorname{vec}X$.

For the basis this reads $R_t=\mathrm I_4$ and, for $k=x,y,z$,

$$
R_x=-i\,\sigma_1\otimes\mathrm I_2,\qquad
R_y=+i\,\sigma_2\otimes\mathrm I_2,\qquad
R_z=-i\,\sigma_3\otimes\mathrm I_2 .
$$

Explicitly,

$$
R_t=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
R_x=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix},
$$

$$
R_y=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
R_z=\begin{pmatrix}-i&0&0&0\\0&-i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix}.
$$

In the coefficient basis the same operators read $R_b=D L_{b^{\natural}}D$ with $D=\operatorname{diag}(1,-1,-1,-1)$, the matrix of quaternion conjugation there. The formula is a statement about that basis, not about the operator: in the canonical frame it becomes $\mathsf M_2(b)^{\mathsf T}\otimes\mathrm I_2$.

**The two families commute.** $L_aR_b=R_bL_a$, because both sides send $x$ to $a\,x\,b$. This is why the sixteen products below need no ordering convention.

## The Sixteen Basis Matrices

**Definition.** For $\mu,\nu\in\{t,x,y,z\}$ set

$$
T_{\mu\nu}=L_\mu\,R_\nu .
$$

The matrix $T_{\mu\nu}$ is the matrix of the operator $x\mapsto e_\mu\,x\,e_\nu$. A general two-sided operator is the linear combination

$$
T_{a,b}=\sum_{\mu,\nu}a_\mu b_\nu\,T_{\mu\nu},
$$

and conversely every element of the family $\{T_{a,b}\}$ is obtained this way.

**Proposition (they are a basis).** The sixteen matrices $T_{\mu\nu}$ are distinct, invertible, of determinant $1$ and rank $4$, and are linearly independent. They are a basis of $M_4(\mathbb{C})$.

*Proof.* By the theorem of *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*, the map $a\otimes b^{\mathrm{opp}}\mapsto L_aR_b$ is an isomorphism $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. The sixteen elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$ are a basis of the left side, so their images $T_{\mu\nu}$ are a basis of the right side. In the canonical frame each is a Kronecker product $A_\nu^{\mathsf T}\otimes A_\mu$ of two invertible $2\times2$ matrices, so it is invertible, of determinant $1$ and rank $4$. Distinct pairs give distinct products, because the four $A_\mu$ are linearly independent.

**The rule.** Column $j$ of $T_{\mu\nu}$ is the coordinate column of $e_\mu\,P_j\,e_\nu$ in the canonical frame $P_j=\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-$. In the coefficient basis, where the basis vector $j$ is $e_j$, this is the coordinate column of $e_\mu e_j e_\nu$.

**The table.** Write $A_t=\mathrm I_2$ and $A_k=-i\sigma_k$, so that $L_\mu=\mathrm I_2\otimes A_\mu$ and $R_\nu=A_\nu^{\mathsf T}\otimes\mathrm I_2$. Then

$$
T_{\mu\nu}=L_\mu R_\nu=A_\nu^{\mathsf T}\otimes A_\mu,
$$

that is,

| $\mu\backslash\nu$ | $t$ | $k=x,y,z$ |
|---|---|---|
| $t$ | $\mathrm I_4$ | $-i\,\sigma_k^{\mathsf T}\otimes\mathrm I_2$ |
| $j=x,y,z$ | $-i\,\mathrm I_2\otimes\sigma_j$ | $-\sigma_k^{\mathsf T}\otimes\sigma_j$ |

The sixteen are the four blocks of this table; the tensor factors are $2\times2$, the product is $4\times4$, and no change of basis is needed. The factor $-i$ is the one of $\mathsf M_2(e_k)=-i\sigma_k$, carried by the left factor.

**One entry, checked.** The table gives $T_{xy}=-\sigma_y^{\mathsf T}\otimes\sigma_x=\sigma_2\otimes\sigma_1$,
$$
T_{xy}=\begin{pmatrix}0&0&0&-i\\0&0&-i&0\\0&i&0&0\\i&0&0&0\end{pmatrix}.
$$
Its first column is the coordinate column of $e_x\tilde\Pi_+e_y=i\tilde\Pi_-$, because $\tilde\Pi_+e_y=-\vec\Upsilon_-$ and $e_x\vec\Upsilon_-=-i\tilde\Pi_-$.

**The sixteen, in four families.** The four families are
$$
T_{tt}=\mathrm I_4,\qquad
T_{tk}=-i\,\sigma_k^{\mathsf T}\otimes\mathrm I_2,\qquad
T_{kt}=-i\,\mathrm I_2\otimes\sigma_k,\qquad
T_{jk}=-\sigma_k^{\mathsf T}\otimes\sigma_j .
$$

**The sixteen, entry by entry.** In the canonical frame, grouped by the left index $\mu$,
$$
T_{tt}=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
T_{tx}=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix},
$$
$$
T_{ty}=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
T_{tz}=\begin{pmatrix}-i&0&0&0\\0&-i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix},
$$
$$
T_{xt}=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},\qquad
T_{xx}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},
$$
$$
T_{xy}=\begin{pmatrix}0&0&0&-i\\0&0&-i&0\\0&i&0&0\\i&0&0&0\end{pmatrix},\qquad
T_{xz}=\begin{pmatrix}0&-1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix},
$$
$$
T_{yt}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
T_{yx}=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},
$$
$$
T_{yy}=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&1&0&0\\-1&0&0&0\end{pmatrix},\qquad
T_{yz}=\begin{pmatrix}0&i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&i&0\end{pmatrix},
$$
$$
T_{zt}=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix},\qquad
T_{zx}=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\-1&0&0&0\\0&1&0&0\end{pmatrix},
$$
$$
T_{zy}=\begin{pmatrix}0&0&-i&0\\0&0&0&i\\i&0&0&0\\0&-i&0&0\end{pmatrix},\qquad
T_{zz}=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix}.
$$

Each has four nonzero entries, one in each row and each column, and the nonzero entries are $\pm1$ or $\pm i$. The coefficient basis is the conjugate display: there the same sixteen are the signed permutation matrices $S\,T_{\mu\nu}\,S^{-1}$.

**Composition.** The product of two basis operators is a signed basis operator:
$$
T_{\mu\nu}\,T_{\rho\sigma}=T_{e_\mu e_\rho,\;e_\sigma e_\nu}=\epsilon\,\epsilon'\,T_{\mu'\nu'},
$$
where $e_\mu e_\rho=\epsilon\,e_{\mu'}$ and $e_\sigma e_\nu=\epsilon'\,e_{\nu'}$. For general parameters,
$$
T_{a,b}\,T_{c,d}=T_{ac,\,db}.
$$
The sixteen are therefore closed under multiplication up to sign, with the unit $T_{tt}=\mathrm{I}_4$. They are not a group: $-T_{\mu\nu}$ is not one of the sixteen.

**Inverse, trace and determinant.** For $a,b$ with $N(a)N(b)\neq0$,
$$
T_{a,b}^{-1}=T_{a^{-1},b^{-1}},\qquad
\operatorname{Tr}T_{a,b}=4\,a_t b_t,\qquad
\det T_{a,b}=N(a)^2N(b)^2 .
$$
In particular every basis matrix is invertible, with inverse $\pm$ one of the sixteen; the trace is $4$ only for $T_{tt}$ and $0$ for the other fifteen, and the determinant is $1$ for all sixteen.

**Orthogonality.** For the Hilbert–Schmidt inner product $\langle A,B\rangle=\operatorname{Tr}(A^{\dagger}B)$,
$$
\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}T_{\rho\sigma}\bigr)=4\,\delta_{\mu\rho}\,\delta_{\nu\sigma}.
$$
The sixteen are an orthogonal basis, each of norm $2$. The normalization is the same $4$ as the trace of a left multiplication, because the carrier has four dimensions.

**The basis consists of units, its span does not.** Every $T_{\mu\nu}$ is invertible, but a sum need not be. For example
$$
T_{tt}+T_{xx}=\mathrm I_4-\sigma_1\otimes\sigma_1=
\begin{pmatrix}1&0&0&-1\\0&1&-1&0\\0&-1&1&0\\-1&0&0&1\end{pmatrix},
$$
of rank two. The algebra is simple and has many zero divisors; a basis of invertible matrices does not change that.

## The Tensor Product

**The Kronecker product of the sixteen is not the construction.** The Kronecker product $T_{\mu\nu}\otimes T_{\rho\sigma}$ is a $16\times16$ matrix. It acts on $\mathbb{C}^4\otimes\mathbb{C}^4$, a space of dimension sixteen, not on the carrier $\mathbb{C}^4$. It does not represent $x\mapsto a\,x\,b$.

**The Kronecker product at the $M_2$ level is exact.** In the canonical frame the two one-sided matrices are already Kronecker products,

$$
L_a=\mathrm I_2\otimes\mathsf M_2(a),\qquad
R_b=\mathsf M_2(b)^{\mathsf T}\otimes\mathrm I_2,
$$

and therefore

$$
\boxed{\;T_{a,b}=L_aR_b=\mathsf M_2(b)^{\mathsf T}\otimes\mathsf M_2(a)\;}
$$

for all $a,b$. In particular, for the basis,

$$
T_{\mu\nu}=\mathsf M_2(e_\nu)^{\mathsf T}\otimes\mathsf M_2(e_\mu),
\qquad \mathsf M_2(e_t)=\mathrm I_2,\quad \mathsf M_2(e_k)=-i\sigma_k .
$$

The two Kronecker factors are $2\times2$, not $4\times4$; the result is $4\times4$. The order is fixed: the right parameter $b$ goes in the first factor, transposed, and the left parameter $a$ in the second.

**The coefficient basis is the conjugate display.** The change $S$ of *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*,
$$
S=\begin{pmatrix}
\tfrac12&0&0&\tfrac12\\
0&\tfrac{i}{2}&\tfrac{i}{2}&0\\
0&\tfrac12&-\tfrac12&0\\
\tfrac{i}{2}&0&0&-\tfrac{i}{2}
\end{pmatrix},
\qquad
\det S=-\tfrac14,
$$
has the Peirce elements as columns. In that basis the same operators read
$$
L_a=S\bigl(\mathrm I_2\otimes\mathsf M_2(a)\bigr)S^{-1},\qquad
R_b=S\bigl(\mathsf M_2(b)^{\mathsf T}\otimes\mathrm I_2\bigr)S^{-1},
\qquad
T_{a,b}=S\bigl(\mathsf M_2(b)^{\mathsf T}\otimes\mathsf M_2(a)\bigr)S^{-1},
$$
and the sixteen are the signed permutation matrices $S\,T_{\mu\nu}\,S^{-1}$. The conjugation changes the entries, not the tensor factors.

**In the canonical frame the sixteen are tensor products, not matrix units.** Each $T_{\mu\nu}$ is a Kronecker product of two $2\times2$ matrices and is not a $4\times4$ matrix unit. The matrix units are the sixteen products $L_{P_i}R_{P_j}$ of the four Peirce elements $P_i$, not the sixteen $T_{\mu\nu}$. The canonical frame is adapted to both the chiral blocks and the tensor basis, and this is why the gamma construction closes on it.

**Another basis conjugates the sixteen.** A change of basis $U$ of $\mathbb{B}$ replaces each $T_{\mu\nu}$ by $U\,T_{\mu\nu}\,U^{-1}$. The sixteen matrices change, the algebra they span does not. The coefficient basis is the one in which they are signed permutations; the canonical frame is the one in which they are the Kronecker products above.

## The Sandwich Inside the Sixteen

The **bilinear sandwich** is the member of the family whose two parameters are tied:

$$
\Theta_Q=T_{Q,Q^{*}} .
$$

It is not a generic two-sided operator. The second slot is $Q^{*}$, not an independent $b$; the sandwich has one complex parameter, and it is quadratic in it,
$$
\Theta_{\lambda Q}=\lvert\lambda\rvert^{2}\Theta_Q .
$$

**The family and the algebra.** The sixteen-dimensional algebra is the span of $\{T_{a,b}\}$ by linear combination. The family itself is the set of **decomposable tensors** $a\otimes b^{\mathrm{opp}}$: an affine cone of complex dimension seven, the cone over the Segre variety $\mathbb{P}^3\times\mathbb{P}^3\subset\mathbb{P}^{15}$. The sandwich is the graph $b=Q^{*}$ inside it: a real cone of dimension seven, because the phase of $Q$ cancels,
$$
(e^{i\theta}Q)\,x\,(e^{-i\theta}Q)^{*}=Q\,x\,Q^{*}.
$$

**Two values.** $Q=e_t$ gives $\Theta_{e_t}=\mathrm{I}_4$. $Q=\vec e_y$ gives $Q^{*}=-\vec e_y$ and
$$
\Theta_{\vec e_y}=T_{\vec e_y,-\vec e_y}=-T_{yy}=-\sigma_2\otimes\sigma_2=
\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$

**The gamma matrices are not sandwiches.** They are five cells of the tensor basis with a free second parameter; §*The Gamma Frame* treats them.

## A Gamma Frame, and the Choice Behind It

**Status.** This section records one frame, not the frame. The Clifford relations hold for every frame of the normal form below; the cell table holds for one frame only.

**The five operators.** In the reference frame the Dirac generators are five cells multiplied by $i$:
$$
\gamma^0=iT_{e_t,e_x},\qquad
\gamma^1=iT_{e_x,e_y},\qquad
\gamma^2=iT_{e_y,e_y},\qquad
\gamma^3=iT_{e_z,e_y},\qquad
\gamma_5=-iT_{e_t,e_z}.
$$
In the canonical frame they are
$$
\gamma^0=\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
\gamma^1=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},
$$
$$
\gamma^2=\begin{pmatrix}0&0&0&-i\\0&0&i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},\qquad
\gamma^3=\begin{pmatrix}0&0&1&0\\0&0&0&-1\\-1&0&0&0\\0&1&0&0\end{pmatrix},
$$
$$
\gamma_5=\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.
$$
Each has trace $0$, determinant $1$ and rank $4$.

**The grading construction.** The frame is generated by the left action and one grading of the multiplicity factor. Take
$$
G=\sigma_2\otimes\mathrm I_2,\qquad R_u=\sigma_1\otimes\mathrm I_2=iT_{e_t,e_x},
$$
where $R_u$ is the exchange of the two copies (not a right multiplication), and set
$$
\Gamma_t=R_u=\sigma_1\otimes\mathrm I_2,\qquad
\Gamma_k=L_{i e_k}G=\sigma_2\otimes\sigma_k .
$$
Because $L_{i e_k}=\mathrm I_2\otimes\sigma_k$ in the canonical frame, the product $L_{i e_k}G$ is $(\mathrm I_2\otimes\sigma_k)(\sigma_2\otimes\mathrm I_2)=\sigma_2\otimes\sigma_k$: no rotation is needed, and no change of spinor basis. The four $\Gamma_\mu$ all square to $+\mathrm I_4$ and anticommute in pairs. The Lorentzian generators are the same frame with the spatial generators multiplied by $i$,
$$
\gamma^0=\Gamma_t,\qquad \gamma^k=i\Gamma_k=i\,\sigma_2\otimes\sigma_k,
$$
so that $(\gamma^0)^2=\mathrm I_4$ and $(\gamma^k)^2=-\mathrm I_4$. The pseudoscalar is $\gamma_5=-iT_{e_t,e_z}=-\sigma_3\otimes\mathrm I_2$.

**What the rotation was.** The same left action with the grading read along $\sigma_3$ instead gives
$$
\Gamma_k=L_{i e_k}(\sigma_3\otimes\mathrm I_2)=\sigma_3\otimes\sigma_k,
$$
the Peirce grading. The two frames use the same $L$ and the same $E_k$; they differ only by the choice of direction in the multiplicity plane. That choice is a basis change of the copy label, not an algebraic obstruction.

**The invariant.** No change of basis removes the $-i$. The unit $\vec e_k$ acts as an operator of square $-\mathrm I_4$, so its eigenvalues are $\pm i$; a gamma-like matrix with $\Gamma_k^2=+\mathrm I_4$ cannot represent $\vec e_k$. The closest gamma set is the Pauli set $-\sigma_k$, and that is what the frame uses: $\Gamma_k=\sigma_2\otimes\sigma_k$ is the gamma-like square root, and $\gamma^k=i\Gamma_k$ is the Lorentzian generator. The coefficient basis, where the four left matrices are real signed permutations, is the same representation with the $i$ hidden in the change of basis $S$.

**The gamma-built set is another representation.** The four matrices
$$
\mathrm I_4,\qquad \Gamma_t\Gamma_1,\qquad \Gamma_t\Gamma_2,\qquad -\Gamma_1\Gamma_2
$$
square to $-\mathrm I_4$ in the three vector slots, anticommute, and multiply as the quaternion units. They are a valid representation of $\mathbb{B}$, and they are not the left action: $\Gamma_t\Gamma_1=i\sigma_3\otimes\sigma_1$ is not $\mathrm I_2\otimes\sigma_1=L_{ie_x}$. Choosing the Pauli set as the gamma frame is a choice of representation, not the only one; it is the choice that makes the generators of the frame the left matrices times one grading.

**The frame is a choice of two directions.** The following normal form gives a frame for every orthogonal pair. Let $\beta,\delta$ be unit spatial directions, orthogonal:
$$
\beta^2=\delta^2=-e_t,\qquad \beta\delta=-\delta\beta,
$$
and set
$$
\gamma^0=iL_{e_t}R_{\delta},\qquad
\gamma^k=iL_{e_k}R_{\beta},\qquad k=x,y,z .
$$
Then
$$
\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}\mathrm{I}_4,\qquad
(\gamma_5)^2=\mathrm{I}_4,\qquad
\gamma_5\gamma^\mu=-\gamma^\mu\gamma_5,\qquad
\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3=iT_{e_t,\beta\delta}.
$$
*Proof.* $(\gamma^0)^2=-R_{\delta^2}=\mathrm{I}_4$; $(\gamma^k)^2=-L_{e_k^2}R_{\beta^2}=-\mathrm{I}_4$; $\gamma^0\gamma^k+\gamma^k\gamma^0=-L_{e_k}(R_{\delta\beta}+R_{\beta\delta})=0$; $\gamma^j\gamma^k+\gamma^k\gamma^j=-L_{e_je_k+e_ke_j}R_{\beta^2}=0$. For the pseudoscalar the left factor is $L_{e_te_xe_ye_z}=L_{-e_t}$ and the right factor is $R_{\beta^3\delta}=R_{-\beta\delta}$; the two signs cancel, so the product is $T_{e_t,\beta\delta}$.

The reference frame is $(\beta,\delta)=(e_y,e_x)$, so $\beta\delta=-e_z$. It is the frame the physics articles use, and in the canonical frame it is the one displayed above: $\gamma^0=\sigma_1\otimes\mathrm I_2$ and $\gamma^k=i\sigma_2\otimes\sigma_k$. The earlier articles wrote the same five matrices after the Peirce change; the change is now the identity.

**The pair is the choice.** The five operators determine the pair: $\delta$ is the right factor of $\gamma^0$, and $\beta$ is the right factor of $\gamma^1$. Distinct pairs therefore give distinct frames, not two descriptions of one frame. For the corpus pair $(e_y,e_x)$ the five are cells. If $\beta$ is not one of $e_x,e_y,e_z$, the three spatial generators are not cells: $\gamma^k=iT_{e_k,\beta}=i\sum_\nu\beta_\nu T_{k\nu}$ is a single product of coefficient rank one, supported on several cells. If $\delta$ is not a coordinate axis, $\gamma^0$ is not a cell either. The cell property is a property of the pair, not of the construction.

**Nothing selects the pair.** The proof above uses only $\beta^2=\delta^2=-e_t$ and $\beta\delta=-\delta\beta$: every such pair gives a frame, and every identity in the frame follows from those two lines. No Clifford relation mentions $\beta$ or $\delta$. The three spatial directions enter in three roles — $\beta$ as the common right factor of $\gamma^1,\gamma^2,\gamma^3$, $\delta$ as the right factor of $\gamma^0$, and $\beta\delta$ as the right factor of $\gamma_5$ — and the algebra assigns no direction to any role. What changes with the pair is the list of operators: the five matrices, whether they are cells, the sign of $\gamma_5$ through $\beta\delta$, and the grade column. The pair is a free parameter of the construction, not a consequence of it.

**A remark on conjugacy.** For a unit $u$ and $U=L_uR_{u^{-1}}$ one has $U\,T_{a,b}\,U^{-1}=T_{uau^{-1},\,ubu^{-1}}$. This is the matrix of the inner automorphism $x\mapsto uxu^{-1}$, and it carries frames to frames. It does not preserve the normal form, because it rotates the left factors $e_k$ as well as the right factors: the image of $\gamma^k=iT_{e_k,\beta}$ is $iT_{ue_ku^{-1},u\beta u^{-1}}$, whose left factor is no longer a coordinate axis. The normal form is therefore a slice through the set of frames, not a conjugacy class. Which frames of $M_4(\mathbb{C})$ are of this form is not settled here; the classification is listed among the open questions.

**What the frame fixes and what it does not.** Every frame of the normal form has: the relations $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$; the identity $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3=iT_{e_t,\beta\delta}$ and the anticommutation of $\gamma_5$ with the four generators; the property that the products span $M_4(\mathbb{C})$; the isomorphism with $\mathrm{Cl}_{1,3}(\mathbb{C})$; the abstract Lorentz algebra generated by the commutators; and the type of each generator, $\gamma^0,\gamma_5\in R(\mathbb{B})$ and $\gamma^1,\gamma^2,\gamma^3\in M_4(\mathbb{C})\setminus\bigl(L(\mathbb{B})\cup R(\mathbb{B})\bigr)$. What the frame does not fix: the individual matrices, the cell labels, the grade column of the table, the Peirce images (for the corpus frame, the chiral Dirac matrices up to a change of spinor basis), the sign of $\gamma_5$, and every table that identifies a gamma with a named operator.

**In this frame the sixteen products are the sixteen cells.** The products of the frame, in increasing grade, are

| Grade | $\gamma$-product | Cell | $c$ | Conversion |
|---|---|---|---|---|
| $0$ | $1$ | $T_{tt}$ | $1$ | $T_{tt}=\mathrm I_4$ |
| $1$ | $\gamma^0$ | $T_{tx}$ | $i$ | $T_{tx}=-i\,\gamma^0$ |
| $1$ | $\gamma^1$ | $T_{xy}$ | $i$ | $T_{xy}=-i\,\gamma^1$ |
| $1$ | $\gamma^2$ | $T_{yy}$ | $i$ | $T_{yy}=-i\,\gamma^2$ |
| $1$ | $\gamma^3$ | $T_{zy}$ | $i$ | $T_{zy}=-i\,\gamma^3$ |
| $2$ | $\gamma^0\gamma^1$ | $T_{xz}$ | $1$ | $T_{xz}=\gamma^0\gamma^1$ |
| $2$ | $\gamma^0\gamma^2$ | $T_{yz}$ | $1$ | $T_{yz}=\gamma^0\gamma^2$ |
| $2$ | $\gamma^0\gamma^3$ | $T_{zz}$ | $1$ | $T_{zz}=\gamma^0\gamma^3$ |
| $2$ | $\gamma^1\gamma^2$ | $T_{zt}$ | $1$ | $T_{zt}=\gamma^1\gamma^2$ |
| $2$ | $\gamma^1\gamma^3$ | $T_{yt}$ | $-1$ | $T_{yt}=-\gamma^1\gamma^3$ |
| $2$ | $\gamma^2\gamma^3$ | $T_{xt}$ | $1$ | $T_{xt}=\gamma^2\gamma^3$ |
| $3$ | $\gamma^0\gamma^1\gamma^2$ | $T_{zx}$ | $i$ | $T_{zx}=-i\,\gamma^0\gamma^1\gamma^2$ |
| $3$ | $\gamma^0\gamma^1\gamma^3$ | $T_{yx}$ | $-i$ | $T_{yx}=i\,\gamma^0\gamma^1\gamma^3$ |
| $3$ | $\gamma^0\gamma^2\gamma^3$ | $T_{xx}$ | $i$ | $T_{xx}=-i\,\gamma^0\gamma^2\gamma^3$ |
| $3$ | $\gamma^1\gamma^2\gamma^3$ | $T_{ty}$ | $-i$ | $T_{ty}=i\,\gamma^1\gamma^2\gamma^3$ |
| $4$ | $\gamma^0\gamma^1\gamma^2\gamma^3$ | $T_{tz}$ | $-1$ | $T_{tz}=i\,\gamma_5=-\gamma^0\gamma^1\gamma^2\gamma^3$ |

The fourth column is $c$, the coefficient that makes the product equal $c\,T_{\mu\nu}$; the fifth writes $T_{\mu\nu}$ in terms of the product. Since $c\in\{1,-1,i,-i\}$, the inverse coefficient is $\bar c$.

*Proof.* Direct multiplication with $T_{\mu\nu}T_{\rho\sigma}=T_{e_\mu e_\rho,\,e_\sigma e_\nu}$; the sixteen entries are distinct, so the products are the sixteen cells in some order, each with a unit coefficient. The pseudoscalar is the last row multiplied by $i$, which is the identity $\gamma_5=iT_{e_t,\beta\delta}$ with $\beta\delta=-e_z$.

**In the canonical frame: the Dirac representation.** For this frame,
$$
\gamma^0=\begin{pmatrix}0&\mathrm{I}_2\\\mathrm{I}_2&0\end{pmatrix},\qquad
\gamma^k=\begin{pmatrix}0&\sigma_k\\-\sigma_k&0\end{pmatrix},\qquad
\gamma_5=\operatorname{diag}(-1,-1,1,1).
$$
These are entry for entry the matrices of *The Dirac Algebra and Biquaternions: A Dictionary*, §*The Isomorphism*, and no change of spinor basis is needed. In the coefficient basis the same matrices are $S\,\gamma^\mu\,S^{-1}$. The two blocks are the two Weyl spinors; $\gamma_5$ is their sign; the four generators exchange them.

**The projectors are products, not cells.** The chirality projectors are
$$
P_\pm=\tfrac12(\mathrm{I}_4\pm\gamma_5)=\tfrac12\bigl(T_{tt}\pm iT_{e_t,\beta\delta}\bigr)=T_{e_t/2,\;e_t\pm i\beta\delta}.
$$
In the canonical frame $P_+=\operatorname{diag}(0,0,1,1)$ and $P_-=\operatorname{diag}(1,1,0,0)$. Both have rank two, and the second parameter has quaternionic norm zero. They are single two-sided operators, but not cells: a single product can be singular, and a single product need not be a cell.

**Why the left regular model cannot hold them.** A product $L_aR_b$ lies in the left image $L(\mathbb{B})$ only when $b$ is a scalar, since $L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\mathrm{I}_4$. The right factors here are $\delta$, $\beta$ and $\beta\delta$, all spatial, so no gamma and no $\gamma_5$ lies in $L(\mathbb{B})$. The left image is block diagonal in the canonical frame, $L_a=\operatorname{diag}(\mathsf{M}_2(a),\mathsf{M}_2(a))$, so it preserves the two chiral blocks; the four generators exchange them. The Dirac algebra is not contained in $M_4(\mathbb{C})_{\mathbb{B},L}$; it needs the two-sided operators.

**The Lorentz generators.** For this frame the six commutators
$$
\Sigma^{\mu\nu}=\tfrac{i}{2}[\gamma^\mu,\gamma^\nu]
$$
are again cells:
$$
\Sigma^{01}=iT_{xz},\quad
\Sigma^{02}=iT_{yz},\quad
\Sigma^{03}=iT_{zz},\quad
\Sigma^{12}=iT_{zt},\quad
\Sigma^{13}=-iT_{yt},\quad
\Sigma^{23}=iT_{xt}.
$$
They are even, of grade two; the three $\Sigma^{0k}$ are anti-Hermitian and the three $\Sigma^{jk}$ Hermitian; they are linearly independent and close under commutation on the same six. They generate the spinor representation of $\mathfrak{so}(1,3)$ on $\mathbb{B}\cong\mathbb{C}^4$. The sandwich $\Theta_Q$ is the vector representation on the four-dimensional real subspace of anti-Hermitian elements; the two are different representations of the same group, and the tensor basis carries both. The cell labels are those of this frame.

**The Dirac operator.** With $\partial_\mu=\partial/\partial Q_\mu$,
$$
i\gamma^\mu\partial_\mu=-\bigl(T_{e_t,e_x}\partial_0+T_{e_x,e_y}\partial_1+T_{e_y,e_y}\partial_2+T_{e_z,e_y}\partial_3\bigr),
$$
so on $x\in\mathbb{B}$,
$$
x\mapsto-\bigl(\partial_0x\,e_x+e_x\,\partial_1x\,e_y+e_y\,\partial_2x\,e_y+e_z\,\partial_3x\,e_y\bigr).
$$
The mass term is $-mT_{tt}$. This is the matrix Dirac operator of the dictionary, written in this frame and in the canonical frame. It is not the biquaternionic gradient $\tilde\nabla$ of the physics articles: the gradient is the left multiplication $L_{\tilde\nabla}$, while the matrix operator is two-sided. The dictionary relates the two; it does not identify them as operators on the same carrier.

## Products of a Left Matrix and a Right Matrix

**The question.** For which $M\in M_4(\mathbb{C})$ do there exist $a,b\in\mathbb{B}$ with $M=L_aR_b$?

**The map.** Define
$$
\Phi:\mathbb{B}\times\mathbb{B}\longrightarrow M_4(\mathbb{C}),\qquad \Phi(a,b)=L_aR_b .
$$
It is $\mathbb{C}$-bilinear: $L$ is linear in $a$, $R$ is linear in $b$, and the matrix product is bilinear.

**Lemma 1 (expansion).** For all $a,b$,
$$
\Phi(a,b)=\sum_{\mu,\nu}a_\mu\,b_\nu\,T_{\mu\nu}.
$$
*Proof.* Write $a=\sum_\mu a_\mu e_\mu$ and $b=\sum_\nu b_\nu e_\nu$. By bilinearity, $\Phi(a,b)=\sum_{\mu,\nu}a_\mu b_\nu\,\Phi(e_\mu,e_\nu)$, and $\Phi(e_\mu,e_\nu)=T_{\mu\nu}$.

**Definition (coefficient matrix).** By §*The Sixteen Basis Matrices*, every $M\in M_4(\mathbb{C})$ has a unique expansion $M=\sum_{\mu,\nu}c_{\mu\nu}T_{\mu\nu}$. The matrix $c(M)=(c_{\mu\nu})$ is the **coefficient matrix** of $M$. The orthogonality relation gives it directly from $M$:
$$
c(M)_{\mu\nu}=\tfrac14\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}M\bigr).
$$
Hence $M\mapsto c(M)$ is a linear isomorphism of $M_4(\mathbb{C})$ onto itself.

**Theorem 1 (which matrices are products).** Let $M\in M_4(\mathbb{C})$ and $c=c(M)$. Then
$$
M=L_aR_b\ \text{for some }a,b \iff c=a\,b^{\mathsf T}.
$$
The product set is therefore $\{M:\operatorname{rank}c(M)\le1\}$.

*Proof.* If $M=\Phi(a,b)$, Lemma 1 gives the expansion of $M$ with coefficients $a_\mu b_\nu$; uniqueness of the expansion gives $c=ab^{\mathsf T}$. Conversely, if $c=ab^{\mathsf T}$ then $\sum c_{\mu\nu}T_{\mu\nu}=\sum a_\mu b_\nu T_{\mu\nu}=\Phi(a,b)$ by Lemma 1, and this is $M$.

**Lemma 2 (the factors are unique up to scale).** Let $a,b,a',b'$ be units. Then $\Phi(a,b)=\Phi(a',b')$ if and only if $a'=\lambda a$ and $b'=\lambda^{-1}b$ for some $\lambda\in\mathbb{C}^{\times}$.

*Proof.* If $a'=\lambda a$ and $b'=\lambda^{-1}b$ the products are equal. Conversely, evaluating at $e_t$ gives $ab=a'b'$. For every $x$, $axb=a'xb'$; multiplying on the left by $a^{-1}$ and on the right by $b^{-1}$ gives
$$
x=(a^{-1}a')\,x\,(b'b^{-1}),
$$
that is $L_{p}R_{q}=\mathrm{I}_4$ with $p=a^{-1}a'$ and $q=b'b^{-1}$. Then $L_p=R_{q^{-1}}$, so $px=xq^{-1}$ for all $x$; at $x=e_t$ this gives $p=q^{-1}$, hence $px=xp$ for all $x$, and $p$ is central. The centre of $\mathbb{B}\cong M_2(\mathbb{C})$ is $\mathbb{C}$, so $p=\lambda e_t$ and $q=\lambda^{-1}e_t$, that is $a'=\lambda a$ and $b'=\lambda^{-1}b$.

**Definition (length).** The **length** $\ell(M)$ is the least $r\ge0$ such that $M=\Phi(a_1,b_1)+\cdots+\Phi(a_r,b_r)$; $\ell(0)=0$.

**Theorem 2 (length is the rank of the coefficient matrix).** For every $M\in M_4(\mathbb{C})$,
$$
\ell(M)=\operatorname{rank}c(M).
$$

*Proof.* If $M=\sum_{i\le r}\Phi(a_i,b_i)$, then $c(M)=\sum_{i\le r}a_i b_i^{\mathsf T}$ is a sum of $r$ matrices of rank one, so $\operatorname{rank}c(M)\le r$; hence $\ell(M)\ge\operatorname{rank}c(M)$. Conversely, let $\operatorname{rank}c=r$ and write $c=UV$ with $U$ of size $4\times r$ and $V$ of size $r\times4$ of rank $r$; let $a_i$ be the $i$-th column of $U$ and let $b_i^{\mathsf T}$ be the $i$-th row of $V$. Then $c=\sum_{i\le r}a_ib_i^{\mathsf T}$, so $M=\sum_{i\le r}\Phi(a_i,b_i)$ by Lemma 1, and $\ell(M)\le r$.

**Corollary 1 (four products suffice, and four are needed generically).** Every $M$ is a sum of at most four products, and $\ell(M)=4$ exactly when $\det c(M)\neq0$. The condition $\det c(M)\neq0$ is open and dense, so a generic matrix needs four products and none needs five.

**Theorem 3 (the product set, as a subset of $M_4(\mathbb{C})$).**
(i) $\Phi(\mathbb{B}\times\mathbb{B})=\{M:\operatorname{rank}c(M)\le1\}$ is a closed algebraic cone, cut out by all $2\times2$ minors of $c(M)$, that is, by the quadratic equations
$$
\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}M\bigr)\operatorname{Tr}\bigl(T_{\rho\sigma}^{\dagger}M\bigr)
=\operatorname{Tr}\bigl(T_{\mu\sigma}^{\dagger}M\bigr)\operatorname{Tr}\bigl(T_{\rho\nu}^{\dagger}M\bigr)
$$
for all $\mu,\nu,\rho,\sigma$.
(ii) Its image in $\mathbb{P}^{15}$ is the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$, of dimension $6$; the cone has dimension $7$, in an ambient space of dimension $16$.
(iii) It is closed under multiplication and under inverses on its invertible part, and not under addition; it is a proper subset of $M_4(\mathbb{C})$.

*Proof.* (i) is Theorem 1 and the standard rank-one criterion. (ii) The map $[a],[b]\mapsto[ab^{\mathsf T}]$ is injective and is the Segre embedding of $\mathbb{P}^3\times\mathbb{P}^3$, of dimension $3+3=6$; the affine cone adds one dimension. Equivalently, $\Phi$ is defined on $\mathbb{C}^8$, its fibre over a product of units is the scaling orbit of Lemma 2, of dimension $1$, and $8-1=7$. (iii) $\Phi(a,b)\Phi(c,d)=\Phi(ac,db)$ and $\Phi(a,b)^{-1}=\Phi(a^{-1},b^{-1})$; $T_{tt}+T_{xx}$ is not a product by (i), since its coefficient matrix is $\operatorname{diag}(1,1,0,0)$; and $7<16$.

**Theorem 4 (matrix rank of a single product).** For $M=\Phi(a,b)$,
$$
\operatorname{rank}M=\operatorname{rank}\mathsf{M}_2(a)\cdot\operatorname{rank}\mathsf{M}_2(b)\in\{0,1,2,4\}.
$$
In particular $\operatorname{rank}M=4$ exactly when $a$ and $b$ are units, and no product has rank $3$.

*Proof.* By §*The Tensor Product*, $T_{a,b}=\mathsf{M}_2(b)^{\mathsf T}\otimes\mathsf{M}_2(a)$. The singular values of a Kronecker product are the pairwise products of the singular values of the factors, so its rank is the product of the ranks. For $\mathsf{M}_2(a)$ the determinant is $N(a)$, so the rank is $2$ when $N(a)\neq0$, $1$ when $a\neq0$ and $N(a)=0$, and $0$ when $a=0$.

**Theorem 5 (the two ranks are independent).** Neither $\operatorname{rank}M$ nor $\operatorname{rank}c(M)$ determines the other.
(i) The rank-one matrix $M_1=(e_2+e_3)(e_2+e_3)^{\mathsf T}$, with $e_i$ the standard column of $\mathbb{C}^4$, has $\operatorname{rank}M_1=1$ and $\ell(M_1)=4$.
(ii) $P_+$ has $\operatorname{rank}P_+=2$ and $\ell(P_+)=1$.
(iii) Among the matrices of rank one, those of length four form a dense open subset.

*Proof.* (i) The matrix is
$$
M_1=\begin{pmatrix}0&0&0&0\\0&1&1&0\\0&1&1&0\\0&0&0&0\end{pmatrix},
$$
of rank one. Its coefficient matrix is
$$
c(M_1)=\tfrac12\operatorname{diag}(1,-1,1,1),
$$
of determinant $-\tfrac1{16}$ and rank $4$, so Theorem 2 gives $\ell(M_1)=4$ and the decomposition
$$
M_1=\tfrac12\bigl(T_{tt}-T_{xx}+T_{yy}+T_{zz}\bigr).
$$
(ii) $P_+=\tfrac12(T_{tt}-iT_{tz})=T_{e_t/2,\,e_t-ie_z}$, so $c(P_+)$ has rank $1$, while $P_+$ has rank $2$ (it is a projector onto a plane).
(iii) The condition $\ell\le3$ is $\operatorname{rank}c\le3$, which is closed. It is proper, by (i). The variety of rank-one matrices is the irreducible Segre variety, so a proper closed subset has dense open complement.

**The two ranks on examples.**

| $M$ | $\operatorname{rank}M$ | $\operatorname{rank}c(M)$ | $\ell(M)$ | decomposition |
|---|---|---|---|---|
| $T_{tt}+T_{tz}$ | $4$ | $1$ | $1$ | $T_{e_t,\,e_t+e_z}$ |
| $P_+$ | $2$ | $1$ | $1$ | $T_{e_t/2,\,e_t-ie_z}$ |
| $T_{a,b}$, $a,b\neq0$, $N(a)=N(b)=0$ | $1$ | $1$ | $1$ | by construction |
| $T_{tt}+T_{xx}$ | $2$ | $2$ | $2$ | $T_{e_t,e_t}+T_{e_x,e_x}$ |
| $M_1=(e_2+e_3)(e_2+e_3)^{\mathsf T}$ | $1$ | $4$ | $4$ | $\tfrac12(T_{tt}-T_{xx}+T_{yy}+T_{zz})$ |
| generic $M$ | $4$ | $4$ | $4$ | four terms, none removable |

**How to decide, and how to decompose.** Compute the sixteen numbers $\tfrac14\operatorname{Tr}(T_{\mu\nu}^{\dagger}M)$ and form the $4\times4$ array $c$. If $\operatorname{rank}c=1$, then $M$ is a product: take $a$ to be any nonzero column of $c$ and $b^{\mathsf T}$ the corresponding row divided by the entry where that column is nonzero. If $\operatorname{rank}c=r>1$, then $M$ is a sum of $r$ products and of no fewer; a rank factorisation $c=UV$ of the array gives the $r$ terms, as in the proof of Theorem 2. No test on $\operatorname{rank}M$ alone decides the question, by Theorem 5.

**Remark (the invertible products).** By Lemma 2 and the composition law, the invertible products form a subgroup of $\mathrm{GL}_4(\mathbb{C})$ isomorphic to $\bigl(\mathbb{B}^{\times}\times\mathbb{B}^{\times}\bigr)/\mathbb{C}^{\times}$, of dimension $7$. It is a small subgroup of a group of dimension $16$, and it is not the set of all invertible matrices: an invertible matrix is a product exactly when its coefficient matrix has rank one.

**The answer in one line.** A matrix is a left times a right matrix exactly when its coefficient matrix has rank one; the product set is a closed cone of dimension $7$ inside a space of dimension $16$, and every matrix is a sum of at most four of its elements.

## Worked Example

Take
$$
a=(2+i)e_t+(1-i)\vec e_x+3\vec e_y+i\vec e_z,\qquad b=\vec e_x .
$$
Then $T_{a,b}=L_aR_x$. In the basis,
$$
T_{a,b}=(2+i)T_{tx}+(1-i)T_{xx}+3T_{yx}+iT_{zx},
$$
and the four matrices are read off the display above. The sum is
$$
T_{a,b}=
\begin{pmatrix}
0&0&1-3i&-1+4i\\
0&0&-1-2i&1-i\\
1-3i&-1+4i&0&0\\
-1-2i&1-i&0&0
\end{pmatrix}.
$$
Column $j$ is the coordinate column of $a\,P_j\,e_x$ in the canonical frame; the matrix is block anti-diagonal, the two blocks carrying the two Peirce planes.

## What Remains Open

The following are candidate articles, not results. None of them is written, and the frame question is not settled by this article.

- The classification of Clifford frames in $M_4(\mathbb{C})$: is every frame of the normal form above, and what is the stabiliser of the cell frame?
- The choice of frame as a choice of Clifford structure: which gradings the algebra admits, and how they are related.
- A dictionary, frame by frame, between the explicit gamma matrices of the physics articles and the tensor basis. The corpus has eighteen explicit representations, and they need not use the same $(\beta,\delta)$.
- Which physical statements are frame-independent, and which are artefacts of a table. The mass bilinear, the axial current and the chiral projectors are the first candidates.
- The $\gamma_5$ sign and the choice of the second central root of $-1$, the sign $\chi=i\tilde\Xi_{\mathrm{ad}}$; the two conventions must not be mixed inside one computation.
- The Peirce image of a general frame, and the spinor-basis change that relates two frames.
- The Segre length in physics: the equations are known, since the matrices of length at most $r$ are the locus $\operatorname{rank}c\le r$, cut out by the $(r+1)\times(r+1)$ minors; what is not known is which physical operators have length two or three, and why.
- The two-sided Dirac operator against the left gradient: the dictionary at the level of differential operators, not only of matrices.
- The odd sector, the module structure and the reality conditions in a frame that is not the reference frame.

## Summary

The two-sided operators on $\mathbb{B}$ form the algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, whose matrix representation in the canonical frame is $M_4(\mathbb{C})$. The sixteen matrices $T_{\mu\nu}=L_\mu R_\nu$ are a basis. They are built from the four left matrices $L_\mu=\mathrm I_2\otimes\mathsf M_2(e_\mu)$ and the four right matrices $R_\nu=\mathsf M_2(e_\nu)^{\mathsf T}\otimes\mathrm I_2$, by ordinary matrix multiplication, so each is the Kronecker product $T_{\mu\nu}=\mathsf M_2(e_\nu)^{\mathsf T}\otimes\mathsf M_2(e_\mu)$. They are invertible, of determinant $1$, orthogonal for the Hilbert–Schmidt form, closed under multiplication up to sign, and their span contains singular matrices. The correct tensor product is at the algebra level and, in the canonical frame, at the $M_2$ level with no change of basis; the Kronecker product of two $4\times4$ matrices is not the construction. The bilinear sandwich is one member of the family, with the second parameter tied to the first. The Dirac gammas are $i$ times the five products $L_{e_t}R_\delta$ and $L_{e_k}R_\beta$ for a pair $(\beta,\delta)$ of orthogonal spatial directions; the reference frame takes $(e_y,e_x)$. Nothing selects the pair. Only pairs of coordinate axes make the five into cells; a generic pair gives five single products of coefficient rank one, each spread over several cells. The pair is a free parameter of the construction: no Clifford relation mentions it. What survives a change of pair are the relations, the isomorphism with $\mathrm{Cl}_{1,3}(\mathbb{C})$, and the type of each generator (right multiplication or two-sided); what does not survive is the matrices, the cell labels, the grade column and the sign of $\gamma_5$. In the corpus frame the sixteen products of the five gammas are the sixteen cells up to units.

For the product question, write $M=\sum c_{\mu\nu}T_{\mu\nu}$ with $c(M)_{\mu\nu}=\tfrac14\operatorname{Tr}(T_{\mu\nu}^{\dagger}M)$. Then $M=L_aR_b$ exactly when $c(M)=ab^{\mathsf T}$, that is, exactly when $c(M)$ has rank one. The least number of products in a sum is $\operatorname{rank}c(M)$; every matrix is a sum of at most four, and a generic matrix needs four. The product set is the closed cone over the Segre $\mathbb{P}^3\times\mathbb{P}^3$, of dimension seven, not the algebra of dimension sixteen. Matrix rank does not decide the question: the rank-one block $M_1=(e_2+e_3)(e_2+e_3)^{\mathsf T}$ needs four products, while $P_+$ has rank two and is one product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, complex dimension $4$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the coefficient basis |
| $L_a=\mathsf{M}_4^{L}(a)$ | left multiplication, the $M_4(\mathbb{C})_{\mathbb{B},L}$ matrix |
| $R_b$ | right multiplication, $x\mapsto xb$ |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | quaternion conjugation in the coefficient basis |
| $T_{a,b}=L_aR_b$ | the two-sided operator $x\mapsto axb$ |
| $T_{\mu\nu}=L_\mu R_\nu$ | the sixteen basis matrices |
| $S$ | the matrix of the Peirce elements, $\det S=-\tfrac14$, change from the canonical frame to the coefficient basis |
| $\Theta_Q=T_{Q,Q^{*}}$ | the bilinear sandwich |
| $N(a)=a_t^2+a_x^2+a_y^2+a_z^2$ | the quaternionic norm |
| $\beta,\delta$ | the two right directions of a frame, $\beta^2=\delta^2=-e_t$, $\beta\delta=-\delta\beta$ |
| $G=\sigma_2\otimes\mathrm I_2$ | the grading in the multiplicity factor of the gamma frame |
| $\Gamma_t,\Gamma_1,\Gamma_2,\Gamma_3$ | $\Gamma_t=\sigma_1\otimes\mathrm I_2$, $\Gamma_k=L_{ie_k}G=\sigma_2\otimes\sigma_k$ |
| $\gamma^0,\gamma^1,\gamma^2,\gamma^3,\gamma_5$ | one Dirac frame; five cells multiplied by $i$ in the reference frame |
| $c(M)$ | the coefficient matrix, $c(M)_{\mu\nu}=\tfrac14\operatorname{Tr}(T_{\mu\nu}^{\dagger}M)$ |
| $\ell(M)$ | the least number of products summing to $M$; equal to $\operatorname{rank}c(M)$ |
| $\Sigma^{\mu\nu}=\tfrac{i}{2}[\gamma^\mu,\gamma^\nu]$ | the Lorentz generators, six even cells |

## Further Reading

- [$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant](m4c-model-the-product-the-trace-and-the-determinant.html), for the left matrices and the model
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the abstract algebra and the theorem that it is the endomorphism algebra
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the construction of $M_4(\mathbb{C})$ from the sandwich map and the change to the matrix-unit basis
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the family, its composition, its adjoint and its type criteria
- [One-Sided Operators on the Biquaternion Algebra](one-sided-operators-on-the-biquaternion-algebra.html), for the two regular families
- [$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Sandwich](the-sandwich-in-the-m4c-l-model.html), for the congruence $MXM^{\dagger}$
- [$M_4(\mathbb{C})_{\mathbb{B}}$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m4c-model-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the Peirce basis, the chiral blocks and the matrix units $L_{P_i}R_{P_j}$
- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the $2\times2$ model and the Kronecker factors
- [The Dirac Algebra and Biquaternions: A Dictionary](../articles_physics/the-dirac-algebra-and-biquaternions-a-dictionary.html), for the explicit chiral matrices of one frame, the Peirce match and the chirality
