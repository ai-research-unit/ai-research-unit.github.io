# __$M_4(\mathbb{C})_L$ Representation : The Two-Sided Operators on the Biquaternion Algebra__

## Introduction

The $M_4(\mathbb{C})_L$ model assigns to each biquaternion $\tilde Q$ one $4\times4$ matrix, its left regular matrix $\mathsf{M}_4(\tilde Q)$. That is a representation of the algebra $\mathbb{B}$ on itself by left multiplication: the image has complex dimension four, and the product is preserved.

The operator $x\mapsto a\,x\,b$ is not a left multiplication when $b$ is not a scalar. It needs the right multiplication as well. The pair $(a,b)$ defines the **two-sided operator**

$$
T_{a,b}(x)=a\,x\,b .
$$

The operators $T_{a,b}$ span the whole matrix algebra $M_4(\mathbb{C})$, of complex dimension sixteen. This article builds that representation and its sixteen basis matrices.

**Three objects, three dimensions.** The carrier is the biquaternion algebra $\mathbb{B}$, of complex dimension four. Its left regular image $L(\mathbb{B})=\{\mathsf{M}_4(a)\}$ is a four-dimensional subalgebra of $M_4(\mathbb{C})$. The operator algebra is the tensor product

$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\;\cong\;\operatorname{End}_{\mathbb{C}}(\mathbb{B}),
$$

of complex dimension sixteen; its **matrix representation** in the coefficient basis is $M_4(\mathbb{C})$. The sixteen basis matrices are the images of the sixteen elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$.

**The tensor-product question.** Three products must be kept apart. The Kronecker product $L_\mu\otimes L_\nu$ of two $4\times4$ matrices is a $16\times16$ matrix acting on $\mathbb{C}^4\otimes\mathbb{C}^4$; it is *not* the matrix of $x\mapsto e_\mu x e_\nu$. The Kronecker product of two $2\times2$ matrices *is* a $4\times4$ matrix, and it gives the two-sided operators through the identification $\mathbb{B}\cong M_2(\mathbb{C})$; the change of basis is written below. The product that builds the sixteen is the tensor product of algebras, $e_\mu\otimes e_\nu^{\mathrm{opp}}\mapsto L_\mu R_\nu$, and in matrices it is the ordinary product of two $4\times4$ matrices.

**Conventions.** The algebra, the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and the matrix $\mathsf{M}_4$ are those of *$M_4(\mathbb{C})_L$ Model : The Product, the Trace and the Determinant*. Write $L_a=\mathsf{M}_4(a)$ for left multiplication by $a$, and $R_b$ for right multiplication, $R_b(x)=x\,b$. The coefficient order is $(t,x,y,z)$. The matrix of quaternion conjugation on coefficients is

$$
D=\operatorname{diag}(1,-1,-1,-1),
$$

and $N(a)=\langle a\rangle_{\natural}=a_t^2+a_x^2+a_y^2+a_z^2$ is the quaternionic norm.

**Boundaries.** The abstract algebra, its two regular representations and its double centraliser are *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*. The family $\{T_{a,b}\}$, its composition, its adjoint and its type criteria are *Two-Sided Operators on the Biquaternion Algebra*. The model and its four-dimensional image are *$M_4(\mathbb{C})_L$ Model : The Product, the Trace and the Determinant*. The one-sided families are *One-Sided Operators on the Biquaternion Algebra*. The congruence is *$M_4(\mathbb{C})_L$ Model : The Sandwich*, and the $2\times2$ model is *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*.

## The Four Left Matrices

**Definition.** The left regular matrix $L_a=\mathsf{M}_4(a)$ is the $4\times4$ matrix whose $\mu$-th column is the coordinate column of $a\,e_\mu$. On a coefficient column $x$ it acts by $x\mapsto a\,x$.

The four basis matrices are

$$
L_t=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
L_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
$$

$$
L_y=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
L_z=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

A general element is $L_a=\sum_\mu a_\mu L_\mu$, with the matrix displayed in the model article:

$$
L_a=\begin{pmatrix}
a_t&-a_x&-a_y&-a_z\\
a_x&a_t&-a_z&a_y\\
a_y&a_z&a_t&-a_x\\
a_z&-a_y&a_x&a_t
\end{pmatrix}.
$$

**The image is four-dimensional.** The matrices $L_\mu$ are linearly independent, and every product $L_aL_b=L_{ab}$ stays in their span. So $L(\mathbb{B})$ is a copy of $\mathbb{B}$, not the whole of $M_4(\mathbb{C})$.

## The Four Right Matrices

**Definition.** The right multiplication is $R_b(x)=x\,b$. Its matrix is not $\mathsf{M}_4(b)$: the two families commute, and $R_b$ is the commuting partner of $L_b$.

**Proposition.** With $D=\operatorname{diag}(1,-1,-1,-1)$,

$$
R_b=D\,L_{b^{\natural}}\,D .
$$

*Proof.* On coefficients $D$ is quaternion conjugation, $D x=x^{\natural}$. Hence
$$
(D L_b D)(x)=D\bigl(b\,x^{\natural}\bigr)=\bigl(b\,x^{\natural}\bigr)^{\natural}=(x^{\natural})^{\natural}\,b^{\natural}=x\,b^{\natural}=R_{b^{\natural}}(x).
$$
Replacing $b$ by $b^{\natural}$ gives the formula. $\square$

For the basis this reads $R_t=L_t=\mathrm{I}_4$ and, for $k=x,y,z$,

$$
R_k=-D\,L_k\,D .
$$

Explicitly,

$$
R_t=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
R_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},
$$

$$
R_y=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
R_z=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$

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

**Proposition (they are a basis).** The sixteen matrices $T_{\mu\nu}$ are distinct, are signed permutation matrices, have determinant $1$ and rank $4$, and are linearly independent. They are a basis of $M_4(\mathbb{C})$.

*Proof.* By the theorem of *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*, the map $a\otimes b^{\mathrm{opp}}\mapsto L_aR_b$ is an isomorphism $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. The sixteen elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$ are a basis of the left side, so their images $T_{\mu\nu}$ are a basis of the right side. Each is a product of two monomial matrices, hence monomial; each $L_\mu$ and $R_\nu$ has determinant $1$, so the product has determinant $1$; and a monomial $4\times4$ matrix of determinant $1$ has rank $4$. The distinctness is read off the table below. $\square$

**The rule.** Column $j$ of $T_{\mu\nu}$ is the coordinate column of $e_\mu\,e_j\,e_\nu$. In particular the first column, the column of $e_t$, is the coordinate column of $e_\mu e_\nu$.

**The table.** Write a monomial matrix as $(\pi;\epsilon)$, meaning that column $j$ has entry $\epsilon_j$ in row $\pi(j)$, with rows and columns indexed in the order $t,x,y,z$ by $0,1,2,3$. The sixteen matrices are:

| $\mu\backslash\nu$ | $t$ | $x$ | $y$ | $z$ |
|---|---|---|---|---|
| $t$ | $(0123;++++)$ | $(1032;+--+)$ | $(2301;++--)$ | $(3210;+-+-)$ |
| $x$ | $(1032;+-+-)$ | $(0123;--++)$ | $(3210;+--+)$ | $(2301;----)$ |
| $y$ | $(2301;+--+)$ | $(3210;----)$ | $(0123;-+-+)$ | $(1032;++--)$ |
| $z$ | $(3210;++--)$ | $(2301;+-+-)$ | $(1032;----)$ | $(0123;-++-)$ |

**One entry, checked.** The table gives $T_{xy}=(3210;+--+)$. Its columns are, in order, $e_z$, $-e_y$, $-e_x$, $e_t$; that is,
$$
T_{xy}=\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$
The first column is $e_z$, because $e_xe_te_y=e_z$.

**The sixteen matrices, written out.**

$$
T_{tt}=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad T_{tx}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}
$$

$$
T_{ty}=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad T_{tz}=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}
$$

$$
T_{xt}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad T_{xx}=\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}
$$

$$
T_{xy}=\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix},\qquad T_{xz}=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\-1&0&0&0\\0&-1&0&0\end{pmatrix}
$$

$$
T_{yt}=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad T_{yx}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix}
$$

$$
T_{yy}=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&-1&0\\0&0&0&1\end{pmatrix},\qquad T_{yz}=\begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&-1&0\end{pmatrix}
$$

$$
T_{zt}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix},\qquad T_{zx}=\begin{pmatrix}0&0&1&0\\0&0&0&-1\\1&0&0&0\\0&-1&0&0\end{pmatrix}
$$

$$
T_{zy}=\begin{pmatrix}0&-1&0&0\\-1&0&0&0\\0&0&0&-1\\0&0&-1&0\end{pmatrix},\qquad T_{zz}=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix}
$$
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
The sixteen are an orthogonal basis, each of norm $2$. The normalization is the same $4$ as the trace of a left multiplication, because the coefficient basis has four elements.

**The basis consists of units, its span does not.** Every $T_{\mu\nu}$ is invertible, but a sum need not be. For example
$$
T_{tt}+T_{xx}=\operatorname{diag}(0,0,2,2),
$$
of rank two. The algebra is simple and has many zero divisors; a basis of invertible monomial matrices does not change that.

## The Tensor Product

**The Kronecker product of the sixteen is not the construction.** The Kronecker product $T_{\mu\nu}\otimes T_{\rho\sigma}$ is a $16\times16$ matrix. It acts on $\mathbb{C}^4\otimes\mathbb{C}^4$, a space of dimension sixteen, not on the carrier $\mathbb{C}^4$. It does not represent $x\mapsto a\,x\,b$.

**The Kronecker product at the $M_2$ level is.** Since $\mathbb{B}\cong M_2(\mathbb{C})$, let $S$ be the Peirce change of *$M_4(\mathbb{C})_L$ Model : The Product, the Trace and the Determinant*:

$$
S=\begin{pmatrix}
\tfrac12&0&0&\tfrac12\\
0&\tfrac{i}{2}&\tfrac{i}{2}&0\\
0&\tfrac12&-\tfrac12&0\\
\tfrac{i}{2}&0&0&-\tfrac{i}{2}
\end{pmatrix},
\qquad
\det S=-\tfrac14 .
$$

Its columns are $\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-$; it carries the Peirce column to the coefficient column, and $S^{-1}$ carries the coefficient column to $\operatorname{vec}\mathsf{M}_2(a)$. Then

$$
L_a=S\bigl(\mathrm{I}_2\otimes\mathsf{M}_2(a)\bigr)S^{-1},\qquad
R_b=S\bigl(\mathsf{M}_2(b)^{\mathsf T}\otimes\mathrm{I}_2\bigr)S^{-1},
$$

and therefore

$$
\boxed{\;T_{a,b}=S\bigl(\mathsf{M}_2(b)^{\mathsf T}\otimes\mathsf{M}_2(a)\bigr)S^{-1}\;}
$$

for all $a,b$. In particular, for the basis,

$$
T_{\mu\nu}=S\bigl(\mathsf{M}_2(e_\nu)^{\mathsf T}\otimes\mathsf{M}_2(e_\mu)\bigr)S^{-1},
\qquad \mathsf{M}_2(e_t)=\mathrm{I}_2,\quad \mathsf{M}_2(e_k)=-i\sigma_k .
$$

The two Kronecker factors are $2\times2$, not $4\times4$; the result is $4\times4$. The order is fixed: the right parameter $b$ goes in the first factor, transposed, and the left parameter $a$ in the second.

**In the Peirce basis the sixteen remain monomial.** The Peirce change sends $T_{\mu\nu}$ to a monomial matrix with entries in $\{1,-1,i,-i\}$; it does not send it to a matrix unit. The matrix units are the sixteen products $L_{P_i}R_{P_j}$ of the four Peirce elements $P_i$, not the sixteen $T_{\mu\nu}$. The coefficient basis is adapted to the tensor basis; the Peirce basis is adapted to the chiral blocks.

**Another basis conjugates the sixteen.** A change of basis $U$ of $\mathbb{B}$ replaces each $T_{\mu\nu}$ by $U\,T_{\mu\nu}\,U^{-1}$. The sixteen matrices change, the algebra they span does not. The coefficient basis is the one in which they are signed permutations; the Peirce basis is the one in which the left factor is block diagonal.

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
\Theta_{\vec e_y}=T_{\vec e_y,-\vec e_y}=-T_{yy}=\operatorname{diag}(1,-1,1,-1).
$$

**Why the gamma matrices are not sandwiches.** The Dirac generators are five single two-sided operators, not sandwiches:
$$
\gamma^0=T_{e_t,\,i\vec e_x},\qquad
\gamma^k=T_{i\vec e_k,\,\vec e_y},\qquad
\gamma_5=T_{e_t,\,-i\vec e_z}.
$$
Their second slot is free; the sandwiches have $b=Q^{*}$. The gammas do not preserve the Hermitian sector, while every sandwich does. They are four of the sixteen basis operators up to the scalar $i$, and $\gamma_5$ is a fifth; their products give the rest.

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
-1+i&-2-i&i&-3\\
2+i&-1+i&-3&-i\\
i&-3&1-i&2+i\\
-3&-i&-2-i&1-i
\end{pmatrix}.
$$
The first column is $a\,e_t\,e_x=a\,e_x$; the other columns are the same product on the other basis elements. The matrix is not monomial: a sum of basis elements is a general matrix.

## Summary

The two-sided operators on $\mathbb{B}$ form the algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, whose matrix representation in the coefficient basis is $M_4(\mathbb{C})$. The sixteen matrices $T_{\mu\nu}=L_\mu R_\nu$ are a basis. They are built from the four left matrices of the $M_4(\mathbb{C})_L$ model and the four right matrices $R_b=D L_{b^{\natural}}D$, by ordinary matrix multiplication. They are signed permutation matrices of determinant $1$, orthogonal for the Hilbert–Schmidt form, closed under multiplication up to sign, and their span contains singular matrices. The correct tensor product is at the algebra level, or equivalently at the $M_2$ level through the change $S$; the Kronecker product of two $4\times4$ matrices is not the construction. The bilinear sandwich is one member of the family, with the second parameter tied to the first; the Dirac gammas are five members with free second parameters.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, complex dimension $4$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the coefficient basis |
| $L_a=\mathsf{M}_4(a)$ | left multiplication, the $M_4(\mathbb{C})_L$ matrix |
| $R_b$ | right multiplication, $x\mapsto xb$ |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | quaternion conjugation on coefficients |
| $T_{a,b}=L_aR_b$ | the two-sided operator $x\mapsto axb$ |
| $T_{\mu\nu}=L_\mu R_\nu$ | the sixteen basis matrices |
| $S$ | the Peirce change of the model article, $\det S=-\tfrac14$ |
| $\Theta_Q=T_{Q,Q^{*}}$ | the bilinear sandwich |
| $N(a)=a_t^2+a_x^2+a_y^2+a_z^2$ | the quaternionic norm |

## Further Reading

- [$M_4(\mathbb{C})_L$ Model : The Product, the Trace and the Determinant](m4c-model-the-product-the-trace-and-the-determinant.html), for the left matrices and the model
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the abstract algebra and the theorem that it is the endomorphism algebra
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the family, its composition, its adjoint and its type criteria
- [One-Sided Operators on the Biquaternion Algebra](one-sided-operators-on-the-biquaternion-algebra.html), for the two regular families
- [$M_4(\mathbb{C})_L$ Model : The Sandwich](the-sandwich-in-the-m4c-l-model.html), for the congruence $MXM^{\dagger}$
- [$M_4(\mathbb{C})_L$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m4c-model-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the Peirce basis, the chiral blocks and the matrix units $L_{P_i}R_{P_j}$
- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the $2\times2$ model and the Kronecker factors
- [The Dirac Algebra and Biquaternions: A Dictionary](../articles_physics/the-dirac-algebra-and-biquaternions-a-dictionary.html), for the gamma matrices as operators
