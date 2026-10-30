# __The Endomorphisms of the Biquaternion Algebra__

## Introduction

The biquaternion algebra $\mathbb{B}$ is a complex vector space of dimension four, and its multiplication is a bilinear map $\mathbb{B}\times\mathbb{B}\to\mathbb{B}$. A third structure is easy to overlook: the complex-linear maps of $\mathbb{B}$ into itself. They form an algebra under composition, the **endomorphism algebra** $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen. A basis of $\mathbb{B}$ turns each map into a $4\times4$ matrix, and the algebra into $M_4(\mathbb{C})$.

This article opens the group *Operators* of the Biquaternions chapter and takes that route to $M_4(\mathbb{C})$: the operator space first, the matrix algebra as its coordinate form, and then the operators that the multiplication singles out. The route is basis-free until matrices are wanted. It separates three questions that the notation often merges: what an operator is, how it is written as a matrix, and which operators the algebra structure distinguishes.

**The scope of the word.** In this article an **endomorphism** is a $\mathbb{C}$-linear map $\mathbb{B}\to\mathbb{B}$, with no condition of preserving the product. The maps that preserve the product are the **algebra** endomorphisms; for $\mathbb{B}$ every nonzero unital one is invertible, and they form the group $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})\cong PGL_2(\mathbb{C})$, of dimension three. The two uses of the word are separated in §*The Two Kinds of Endomorphism*, and confusing them is the first trap of the subject.

**The other route.** The corpus also builds $M_4(\mathbb{C})$ from the two-sided operators $T_{a,b}=L_aR_b$. That is the route of *The Two-Sided Operators Method to Build $M_4(\mathbb{C})$* and of *$M_4(\mathbb{C})$ Representation : The Two-Sided Operators on the Biquaternion Algebra*. The two routes reach the same algebra and answer different questions: the endomorphism route says what the algebra is, the two-sided route says how the multiplication generates it. §*The Bridge to the Two-Sided Operators* compares them.

**Three objects.** The rest of the article keeps apart the carrier, its left regular image and its full operator algebra.

| Object | Elements | Complex dimension | Matrix form |
|---|---|---|---|
| $\mathbb{B}$ | the biquaternions | $4$ | $2\times2$ in the $M_2(\mathbb{C})$ model |
| $L(\mathbb{B})$ | the left multiplications $x\mapsto ax$ | $4$ | a $4\times4$ subalgebra |
| $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | all complex-linear maps | $16$ | $M_4(\mathbb{C})$ after a basis |

$L(\mathbb{B})$ and $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ are both made of $4\times4$ matrices in the coefficient basis. They are not the same object: the first has dimension four, the second dimension sixteen. The subscript $L$ in $M_4(\mathbb{C})_{\mathbb{B},L}$ records the first.

**Boundaries.** The algebra, its basis and its multiplication are *The Biquaternion Algebra*. The matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ is *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. The ambient operator space in general is *The Operators on an Algebra*; the regular representations and the double centraliser are *The Regular Representation as an Algebra of Operators*. The two-sided operators are *Two-Sided Operators on the Biquaternion Algebra*, and their matrix form is *$M_4(\mathbb{C})$ Representation : The Two-Sided Operators on the Biquaternion Algebra*. The abstract isomorphism with the enveloping algebra is *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*. The article is pure algebra: no bilinear form, no topology, and the only norm it uses is the multiplicative quaternionic norm.

## The Carrier and Its Linear Maps

**Definition.** The **carrier** of the biquaternion algebra is the underlying complex vector space of $\mathbb{B}$, with basis

$$
e_t,\ \vec e_x,\ \vec e_y,\ \vec e_z ,
$$

in the order $(t,x,y,z)$. A vector is written $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, and its **coordinate column** is $(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}\in\mathbb{C}^4$. The carrier is $\mathbb{C}^4$; the algebra is the carrier with its multiplication added.

**Definition (operator).** An **operator** on $\mathbb{B}$ is a map $F:\mathbb{B}\to\mathbb{B}$ that is complex-linear:

$$
F(x+\lambda y)=F(x)+\lambda F(y)
$$

for all $x,y\in\mathbb{B}$ and all $\lambda\in\mathbb{C}$. The operators form the **endomorphism algebra** $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ under addition and composition, with the identity map as unit.

**Proposition (dimension).** $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ has complex dimension $16$.

*Proof.* A linear map is determined by the four images $F(e_t),F(\vec e_x),F(\vec e_y),F(\vec e_z)$, and each image has four complex coordinates. The data are therefore $4\times4=16$ complex numbers, and every choice of them defines one and only one linear map.

**Remark (the base field is part of the data).** Read as a real algebra, $\mathbb{B}$ has real dimension eight, and $\operatorname{End}_{\mathbb{R}}(\mathbb{B})\cong M_8(\mathbb{R})$ has real dimension sixty-four. The complex-linear maps form the subspace of real dimension thirty-two on which the real structure $J$, the multiplication by $i$, is respected:

$$
\operatorname{End}_{\mathbb{C}}(\mathbb{B})=\{F\in\operatorname{End}_{\mathbb{R}}(\mathbb{B}):FJ=JF\}.
$$

The coefficient conjugation $\bar{\cdot}$ and the Hermitian conjugation ${}^{*}$ are conjugate-linear, so they are **not** elements of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$; they belong to $\operatorname{End}_{\mathbb{R}}(\mathbb{B})$. The natural conjugation $\natural$, which fixes the coefficients and changes the sign of the three vector units, is $\mathbb{C}$-linear, and it is an element of the complex endomorphism algebra, although it is an anti-automorphism and not an algebra endomorphism. This distinction is the reason the four adjoints of the corpus are not all complex-linear: an adjoint built with ${}^{*}$ or $\bar{\cdot}$ is a conjugate-linear map of the operator space, while the plain transpose is complex-linear.

## The Matrix of an Endomorphism

**Definition (matrix in a basis).** Fix the basis $\mathcal{B}=(e_t,\vec e_x,\vec e_y,\vec e_z)$. The **matrix** $[F]_{\mathcal{B}}$ is the $4\times4$ complex matrix whose $j$-th column is the coordinate column of $F(e_j)$, the $j$-th basis vector.

**Proposition (the matrix represents the operator).** The assignment $F\mapsto[F]_{\mathcal{B}}$ is an isomorphism of complex algebras

$$
\operatorname{End}_{\mathbb{C}}(\mathbb{B})\longrightarrow M_4(\mathbb{C}),
$$

that is, $[F+G]=[F]+[G]$, $[F\circ G]=[F]\,[G]$, and $[\mathrm{id}]=\mathrm{I}_4$. It is bijective.

*Proof.* The $j$-th column of $[F\circ G]$ is $(F\circ G)(e_j)=F(G(e_j))$, which is $[F]$ times the $j$-th column of $[G]$; this is the matrix product. Addition and the identity are immediate. Bijectivity is the dimension count of the previous section, or the reconstruction of $F$ from its four columns.

**Proposition (change of basis).** Let $\mathcal{B}'$ be another basis, and let $S$ be the matrix whose columns are the coordinates of the vectors of $\mathcal{B}'$ in $\mathcal{B}$. Then

$$
[F]_{\mathcal{B}'}=S^{-1}\,[F]_{\mathcal{B}}\,S .
$$

*Proof.* Both sides have the same $j$-th column: the coordinate column of $F$ applied to the $j$-th vector of $\mathcal{B}'$, read in $\mathcal{B}'$.

**Remark (the isomorphism is not canonical).** There is no basis-free identification of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ with the algebra of $4\times4$ matrices. The operator space is canonical; its matrix form depends on a basis, and two bases give two conjugate matrix algebras. A statement about an operator is therefore a statement invariant under $[F]\mapsto S^{-1}[F]S$. This is why the corpus can speak of *the* matrix algebra $M_4(\mathbb{C})$ only after a basis has been fixed, and why it names the basis: the coefficient basis in the $M_4(\mathbb{C})_{\mathbb{B},L}$ model, the Peirce basis for the chiral blocks.

**Definition (trace, determinant, spectrum).** The **trace** and the **determinant** of an operator are those of any of its matrices,

$$
\operatorname{tr}F=\operatorname{tr}[F]_{\mathcal{B}},\qquad \det F=\det[F]_{\mathcal{B}} .
$$

They are well defined, because $\operatorname{tr}(S^{-1}AS)=\operatorname{tr}A$ and $\det(S^{-1}AS)=\det A$. The **characteristic polynomial** $\chi_F(\lambda)=\det(\lambda\,\mathrm{id}-F)$ and the **spectrum** are well defined for the same reason. The **rank** of $F$ is the rank of any of its matrices, and it is the dimension of its image.

## The Two Kinds of Endomorphism

**Definition (algebra endomorphism).** An **algebra endomorphism** of $\mathbb{B}$ is a linear map $F$ with

$$
F(xy)=F(x)F(y),\qquad F(e_t)=e_t .
$$

The second condition is unitality. The algebra endomorphisms that are bijective form the **automorphism group** $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})$.

**Theorem (every nonzero algebra endomorphism is an automorphism).** Let $F:\mathbb{B}\to\mathbb{B}$ be a nonzero unital algebra endomorphism. Then $F$ is bijective.

*Proof.* The kernel of $F$ is a two-sided ideal of $\mathbb{B}$. The algebra is simple, so the kernel is $0$ or $\mathbb{B}$. It is not $\mathbb{B}$, because $F(e_t)=e_t\neq0$. Hence $F$ is injective, and an injective linear map of a finite-dimensional space to itself is bijective.

**Theorem (the automorphism group).** $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})\cong PGL_2(\mathbb{C})$, of complex dimension $3$.

*Proof.* Fix an isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$. Every automorphism of a central simple algebra is inner, by the Skolem–Noether theorem, so it has the form $x\mapsto uxu^{-1}$ for a unit $u$. The units that give the identity are the central ones, $\mathbb{C}^\times\mathrm{I}_2$. Hence the group is $GL_2(\mathbb{C})/\mathbb{C}^\times\cong PGL_2(\mathbb{C})$, of dimension $4-1=3$.

**Definition (derivation).** A **derivation** of $\mathbb{B}$ is a linear map $\delta$ with the Leibniz rule

$$
\delta(xy)=\delta(x)y+x\,\delta(y).
$$

The derivations form the subspace $\operatorname{Der}_{\mathbb{C}}(\mathbb{B})$ of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$.

**Proposition (the derivations are the inner ones).** Every derivation of $\mathbb{B}$ is inner,

$$
\delta=\operatorname{ad}_a=L_a-R_a,\qquad \operatorname{ad}_a(x)=ax-xa,
$$

and $\operatorname{ad}_a=0$ exactly when $a$ is central. Hence $\operatorname{Der}_{\mathbb{C}}(\mathbb{B})\cong\mathbb{B}/\mathbb{C}e_t$, of complex dimension $3$. In particular every derivation is a sum of a left and a right multiplication.

*Proof.* The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is central simple, so every derivation is inner; this is the standard theorem for central simple algebras. The kernel of $a\mapsto\operatorname{ad}_a$ is the centre $\mathbb{C}e_t$, by definition of the centre. The dimension is $4-1=3$, and the identity $\operatorname{ad}_a=L_a-R_a$ is the definition.

**Remark (a subspace against a group).** The derivations are cut out by a condition linear in the operator, so they form a subspace of dimension three. The automorphisms are cut out by a condition quadratic in the operator, so they form a group and not a subspace: the sum of two automorphisms is generally not an automorphism. The two dimensions agree, three and three, because the derivations are the tangent space of the group at the identity. This is the rule of *The Operators on an Algebra*, read on $\mathbb{B}$.

## The Canonical Operators of the Multiplication

### Left Multiplication

**Definition.** For $a\in\mathbb{B}$, the **left multiplication** by $a$ is

$$
L_a:\mathbb{B}\longrightarrow\mathbb{B},\qquad L_a(x)=ax .
$$

**Proposition (the laws).** For all $a,b\in\mathbb{B}$,

$$
L_aL_b=L_{ab},\qquad L_{e_t}=\mathrm{id},\qquad L_a\ \text{is invertible}\iff a\ \text{is a unit}.
$$

The assignment $a\mapsto L_a$ is an injective algebra homomorphism $\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, and its image $L(\mathbb{B})$ is a subalgebra of dimension four.

*Proof.* $(L_aL_b)(x)=a(bx)=(ab)x=L_{ab}(x)$. The unit is $L_{e_t}(x)=x$. The inverse of $L_a$ is $L_{a^{-1}}$ when $a$ is a unit, and if $L_a$ is invertible then $a=L_a(e_t)$ is a unit. Injectivity: $L_a=0$ gives $a=L_a(e_t)=0$. The image is closed under composition and addition and has dimension four, since the four $L_\mu$ are the images of a basis and are independent by injectivity.

**The matrix.** In the coefficient basis,

$$
L_a=\begin{pmatrix}
a_t&-a_x&-a_y&-a_z\\
a_x&a_t&-a_z&a_y\\
a_y&a_z&a_t&-a_x\\
a_z&-a_y&a_x&a_t
\end{pmatrix}.
$$

**The invariants.** $\operatorname{tr}L_a=4a_t$, $\det L_a=N(a)^2$, with $N(a)=a_t^2+a_x^2+a_y^2+a_z^2$ the quaternionic norm.

### Right Multiplication

**Definition.** For $b\in\mathbb{B}$, the **right multiplication** is

$$
R_b:\mathbb{B}\longrightarrow\mathbb{B},\qquad R_b(x)=xb .
$$

**Proposition (the laws).** For all $a,b\in\mathbb{B}$,

$$
R_aR_b=R_{ba},\qquad R_{e_t}=\mathrm{id},\qquad L_aR_b=R_bL_a .
$$

The assignment $b\mapsto R_b$ is an injective anti-homomorphism $\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, and its image $R(\mathbb{B})$ is a subalgebra of dimension four.

*Proof.* $(R_aR_b)(x)=(xb)a=x(ba)=R_{ba}(x)$; the commutation is associativity, $(ax)b=a(xb)$; injectivity is $R_b(e_t)=b$; the dimension is four as for $L$.

**The relation to the left family.** Let $D$ be the natural conjugation, $D(x)=x^{\natural}$, with matrix

$$
D=\operatorname{diag}(1,-1,-1,-1).
$$

Then

$$
R_b=D\,L_{b^{\natural}}\,D .
$$

*Proof.* On coordinates $D$ is the conjugation, so $(DL_bD)(x)=D\bigl(b\,x^{\natural}\bigr)=(b\,x^{\natural})^{\natural}=x\,b^{\natural}=R_{b^{\natural}}(x)$. Replacing $b$ by $b^{\natural}$ gives the formula.

### The Conjugation

**Definition.** The **natural conjugation** is the linear map

$$
D:\mathbb{B}\longrightarrow\mathbb{B},\qquad D(x)=x^{\natural}=x_t e_t-x_x\vec e_x-x_y\vec e_y-x_z\vec e_z .
$$

**Proposition.** $D$ is a $\mathbb{C}$-linear involution, $D^2=\mathrm{id}$, and an anti-automorphism, $D(xy)=D(y)D(x)$. Its matrix is $\operatorname{diag}(1,-1,-1,-1)$, so $\operatorname{tr}D=-2$ and $\det D=-1$. It is neither a left nor a right multiplication.

*Proof.* Linearity and the square are read on the basis: $D$ fixes $e_t$ and changes the sign of the three vector units. The anti-automorphism is the standard property of the quaternion conjugation, extended by $\mathbb{C}$-linearity. If $D=L_a$, then $a=D(e_t)=e_t$ and $D=L_{e_t}=\mathrm{id}$, which is false; the same argument with $R_b$ gives $b=e_t$ and the same contradiction.

**Remark (which conjugations are endomorphisms).** Of the corpus's three conjugations, only $\natural$ is $\mathbb{C}$-linear. The coefficient conjugation $\bar{\cdot}$ and the Hermitian conjugation ${}^{*}$ conjugate the complex coefficients, so they are conjugate-linear and live in $\operatorname{End}_{\mathbb{R}}(\mathbb{B})\setminus\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. An operator statement that uses $\bar{\cdot}$ or ${}^{*}$ is a real-linear statement, even when the carrier is written over $\mathbb{C}$.

### The Double Centraliser

**Definition (commutant).** For a subset $\mathcal{S}\subseteq\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, the **commutant** is

$$
\mathcal{S}'=\{T\in\operatorname{End}_{\mathbb{C}}(\mathbb{B}):TS=ST\ \text{for every }S\in\mathcal{S}\}.
$$

**Theorem (the double centraliser).** In $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$,

$$
L(\mathbb{B})'=R(\mathbb{B}),\qquad R(\mathbb{B})'=L(\mathbb{B}),\qquad \bigl(L(\mathbb{B})\cup R(\mathbb{B})\bigr)'=\mathbb{C}\,\mathrm{id},
$$

and the bicommutant of $L(\mathbb{B})$ is $L(\mathbb{B})$ itself.

*Proof.* Let $T$ commute with every $L_a$. Evaluating at $e_t$,

$$
T(x)=T(L_x(e_t))=L_x(T(e_t))=x\,T(e_t)=R_{T(e_t)}(x),
$$

so $T=R_b$ with $b=T(e_t)$, and $R(\mathbb{B})\subseteq L(\mathbb{B})'$. The reverse inclusion is $L_aR_b=R_bL_a$. The proof of $R(\mathbb{B})'=L(\mathbb{B})$ is the same with the roles exchanged: $T(x)=T(R_x(e_t))=R_x(T(e_t))=T(e_t)\,x=L_{T(e_t)}(x)$. An operator commuting with both families is therefore $R_b$ with $b$ central, hence $b\in\mathbb{C}e_t$ and $T=\lambda\,\mathrm{id}$. Finally $L(\mathbb{B})''=R(\mathbb{B})'=L(\mathbb{B})$.

**Remark (what the theorem says).** The two regular families are mutual commutants and each is its own bicommutant. They are as large as two commuting families can be: nothing outside $R(\mathbb{B})$ commutes with all left multiplications. This is the double centraliser theorem for the regular bimodule, and it is the structural reason the left and right actions of the corpus are both available and both of the same size.

**Corollary (the intersection).** $L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\,\mathrm{id}$, so the sum $L(\mathbb{B})+R(\mathbb{B})$ has dimension $4+4-1=7$.

*Proof.* If $L_a=R_b$, then $a=L_a(e_t)=R_b(e_t)=b$ and $ax=xa$ for all $x$, so $a$ is central. The converse is immediate.

## The Ladder and the Generation Theorem

### The Generation Theorem

**Theorem (the two families generate every operator).** The algebra generated by $L(\mathbb{B})\cup R(\mathbb{B})$ is the whole of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$.

*Proof.* Fix an isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ and matrix units $F_{ij}$, $i,j\in\{1,2\}$. For $X=\sum_{a,b}x_{ab}F_{ab}$,

$$
L_{F_{ij}}R_{F_{kl}}(X)=F_{ij}XF_{kl}=\sum_{a,b}x_{ab}\,F_{ij}F_{ab}F_{kl}=x_{jk}\,F_{il},
$$

since $F_{ij}F_{ab}F_{kl}=\delta_{ja}\delta_{bk}F_{il}$. On the four-dimensional space with basis $F_{ab}$, this operator sends the single basis vector $F_{jk}$ to $F_{il}$ and all other basis vectors to zero. It is therefore the matrix unit $E_{(il),(jk)}$ of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. As $(i,j,k,l)$ runs over the sixteen choices, these are the sixteen matrix units of the operator space in the basis $F_{ab}$, so they span it. The products $L_aR_b$ therefore span the operator space.

**Corollary (the products are a basis in the coefficient basis).** With $T_{\mu\nu}=L_{e_\mu}R_{e_\nu}$, the sixteen matrices are a basis of $M_4(\mathbb{C})$.

*Proof.* Every product $L_aR_b$ is a linear combination of the sixteen $T_{\mu\nu}$, by bilinearity in $a$ and $b$, and the products span by the generation theorem. The sixteen $T_{\mu\nu}$ therefore span, and sixteen vectors in a space of dimension sixteen are a basis.

### The Ladder

Each of $L(\mathbb{B})$ and $R(\mathbb{B})$ contains $\mathbb{C}\,\mathrm{id}$ and sits in the sum, and the sum sits in the whole space:

$$
\mathbb{C}\,\mathrm{id}\;\subset\;L(\mathbb{B})\;\subset\;L(\mathbb{B})+R(\mathbb{B})\;\subset\;\operatorname{End}_{\mathbb{C}}(\mathbb{B}),
$$

and the same chain holds with $R(\mathbb{B})$ in place of $L(\mathbb{B})$. The dimensions are $1$, $4$, $7$, $16$; the derivations form a three-dimensional subspace of the sum, and the automorphisms a three-dimensional group inside the unit group.

| Object | Definition | Kind | Complex dimension |
|---|---|---|---|
| scalars | $\lambda\,\mathrm{id}$ | subspace | $1$ |
| $L(\mathbb{B})$ | $x\mapsto ax$ | subalgebra | $4$ |
| $R(\mathbb{B})$ | $x\mapsto xb$ | subalgebra | $4$ |
| $L(\mathbb{B})+R(\mathbb{B})$ | sums of the two | subspace, not a subalgebra | $7$ |
| $\operatorname{Der}_{\mathbb{C}}(\mathbb{B})$ | $\delta(xy)=\delta(x)y+x\delta(y)$ | subspace | $3$ |
| $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | all linear maps | algebra | $16$ |
| $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})$ | multiplicative bijections | group | $3$ |

**Remark (why the sum is not a subalgebra).** The algebra generated by the two families is the whole space, of dimension sixteen, while the sum has dimension seven. If the sum were closed under composition it would be the generated algebra, which it is not. Some single product $L_aR_b$ therefore lies outside the sum: the dimension count shows that the sum is not closed, and expanding a product of two of its elements gives such a product.

**Remark (the two threes).** The derivations sit inside the sum, because $\operatorname{ad}_a=L_a-R_a$, and they have dimension three. The automorphisms are not a subspace at all; their dimension three is the dimension of the tangent space, in agreement with the general rule of *The Operators on an Algebra*.

## The Bridge to the Two-Sided Operators

### The Elementary Tensors

**Definition.** For $a,b\in\mathbb{B}$, the **two-sided operator** is

$$
T_{a,b}=L_aR_b,\qquad T_{a,b}(x)=a\,x\,b .
$$

It is an element of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, the product of a left and a right multiplication.

**Theorem (the enveloping description).** The map

$$
\Phi:\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad a\otimes b^{\mathrm{opp}}\mapsto T_{a,b},
$$

is an isomorphism of algebras. In particular every operator is a sum of products $L_aR_b$.

*Proof.* Multiplicativity is $(a\otimes b^{\mathrm{opp}})(c\otimes d^{\mathrm{opp}})=ac\otimes(db)^{\mathrm{opp}}\mapsto L_{ac}R_{db}=L_aR_bL_cR_d$. Injectivity and surjectivity follow from the generation theorem: the sixteen $T_{\mu\nu}$ are a basis, and the sixteen elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$ are a basis of the tensor product. The full proof, with the matrix-unit computation, is *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*.

**The sixteen matrices.** In the coefficient basis the products $T_{\mu\nu}=L_{e_\mu}R_{e_\nu}$ are signed permutation matrices of determinant one. They satisfy the composition, trace, determinant and orthogonality laws

$$
T_{a,b}T_{c,d}=T_{ac,db},\qquad
\operatorname{tr}T_{a,b}=4a_tb_t,\qquad
\det T_{a,b}=N(a)^2N(b)^2,
$$

$$
\operatorname{tr}\bigl(T_{\mu\nu}^{\dagger}T_{\rho\sigma}\bigr)=4\,\delta_{\mu\rho}\delta_{\nu\sigma}.
$$

They are displayed and tabulated in *$M_4(\mathbb{C})$ Representation : The Two-Sided Operators on the Biquaternion Algebra*.

### The Cone of Products and the Length

**The family is not the space.** The set $\{T_{a,b}\}$ is the set of decomposable tensors $a\otimes b^{\mathrm{opp}}$ under the isomorphism. It is an affine cone of complex dimension seven, the cone over the Segre variety $\mathbb{P}^3\times\mathbb{P}^3\subset\mathbb{P}^{15}$. It is not the whole sixteen-dimensional algebra; only its linear span is.

**The length.** Every operator has a unique expansion

$$
M=\sum_{\mu,\nu}c_{\mu\nu}(M)\,T_{\mu\nu},\qquad
c_{\mu\nu}(M)=\tfrac14\operatorname{tr}\bigl(T_{\mu\nu}^{\dagger}M\bigr).
$$

$M$ is a single product $L_aR_b$ exactly when the **coefficient matrix** $c(M)$ has rank at most one, that is, when $c(M)=a\,b^{\mathsf T}$; for $M\neq0$ this is rank one. In general the **length** is

$$
\ell(M)=\min\{r:M=T_{a_1,b_1}+\cdots+T_{a_r,b_r}\}=\operatorname{rank}c(M),
$$

so every operator is a sum of at most four products, and a generic operator needs four.

**Remark (rank does not determine length).** The matrix rank of $M$ does not fix the length. The projection $E_{11}$ of §*Worked Example* has rank one and length four, while the chirality projector $P_+=\tfrac12(T_{tt}-iT_{tz})$ has rank two and length one. No test on the rank of $M$ alone decides whether $M$ is a product.

### The Two Routes Compared

The two constructions of $M_4(\mathbb{C})$ answer different questions.

| | Endomorphism route | Two-sided route |
|---|---|---|
| Starts with | the vector space $\mathbb{B}$ | the algebra $\mathbb{B}$ and its multiplication |
| Basic objects | arbitrary linear maps $F$ | $L_a$, $R_b$, $T_{a,b}$ |
| What is primary | the operator space $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | the two regular actions |
| Natural basis | matrix units $E_{ij}$, after a basis of $\mathbb{B}$ | the family $\{T_{a,b}\}$ is canonical; the sixteen $T_{\mu\nu}$ are a basis after the coefficient basis |
| Product table | $E_{ij}E_{kl}=\delta_{jk}E_{il}$ | $T_{a,b}T_{c,d}=T_{ac,db}$ |
| Extra structure | trace, determinant, spectrum, rank | bimodule, $L(\mathbb{B})$, $R(\mathbb{B})$, Peirce corners, length |
| Main risk | forgetting the multiplication | confusing the family with its span |

The endomorphism route is the answer to "what is the algebra?". The two-sided route is the answer to "how does the biquaternion multiplication generate it?". Neither replaces the other. The abstract bridge is the isomorphism of §*The Elementary Tensors*; the concrete bridge is the basis $T_{\mu\nu}$.

**Why the two-sided route is clean here.** The equality $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is a property of the central simple algebra. For a general unital finite-dimensional algebra $A$, the map $A\otimes A^{\mathrm{opp}}\to\operatorname{End}_k(A)$ has the multiplication algebra as its image, which may be strictly smaller than the endomorphism algebra, and it may also have a kernel. For the dual numbers, $A\otimes A^{\mathrm{opp}}$ and $\operatorname{End}_k(A)$ both have dimension four, the image has dimension two, and the kernel has dimension two. The biquaternion algebra is central simple, so the map is both injective and surjective, the two-sided operators span the whole space, and no operator is lost.

### The Three Objects Called Matrices

The notation $M_4(\mathbb{C})$ hides three different objects in the corpus, and the difference is a frequent source of confusion.

| Object | What an element is | Complex dimension | Where it is written |
|---|---|---|---|
| $\mathbb{B}$ | a biquaternion | $4$ | $2\times2$ matrix in the $M_2(\mathbb{C})$ model |
| $M_4(\mathbb{C})_{\mathbb{B},L}=L(\mathbb{B})$ | a left multiplication | $4$ | $4\times4$ matrix, block diagonal in the Peirce basis |
| $M_4(\mathbb{C})=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | an arbitrary operator | $16$ | $4\times4$ matrix in a basis of $\mathbb{B}$ |

The second row is a subalgebra of the third, not a quotient and not a different matrix size. A $4\times4$ matrix can therefore be an element of the four-dimensional left model or an element of the sixteen-dimensional operator algebra; the matrix size alone does not tell which. The label and the context do.

## What the Endomorphism View Explains

**The dimension sixteen.** It is $4\times4$: four basis vectors, four coordinates each. No multiplication is used.

**The trace and the determinant of a left multiplication.** In the Peirce basis of *$M_4(\mathbb{C})$ Model : The Product, the Trace and the Determinant*, $L_a$ is two copies of the $2\times2$ matrix of $a$,

$$
S^{-1}L_aS=\operatorname{diag}\bigl(\mathsf{M}_2(a),\mathsf{M}_2(a)\bigr),
$$

so every eigenvalue of $\mathsf{M}_2(a)$ occurs twice. Hence $\operatorname{tr}L_a=2\operatorname{tr}\mathsf{M}_2(a)=4a_t$ and $\det L_a=\det\mathsf{M}_2(a)^2=N(a)^2$. The formulas of the $M_4(\mathbb{C})_{\mathbb{B},L}$ model are read off the operator spectrum, without a determinant computation.

**Why the two regular families are mutual commutants.** An operator commuting with every left multiplication is a right multiplication, and conversely. The proof is the two-line evaluation at $e_t$ of §*The Double Centraliser*, and it does not use matrices.

**Why there is no canonical matrix form.** The operator space is canonical, but the identification with $M_4(\mathbb{C})$ needs a basis. The coefficient basis and the Peirce basis are two bases of $\mathbb{B}$, and they give two conjugate matrix algebras; a gamma frame is a further choice inside the operator algebra, not a basis of the carrier. A statement that survives a change of basis is a statement about operators; one that does not is a statement about a table.

**What the view does not supply.** It supplies no multiplication on the carrier, no gamma frame, no form, no norm, no grading and no physical interpretation. Those are further structures on the operator space, and each is a choice. The endomorphism view is the layer below them: it says which space the choices are made in.

## Worked Example

**The projection onto the scalar line.** Let

$$
P:\mathbb{B}\longrightarrow\mathbb{B},\qquad P(\tilde Q)=\tilde Q_t\,e_t .
$$

It is complex-linear, idempotent, of rank one, and its matrix in the coefficient basis is

$$
P=E_{11}=\begin{pmatrix}1&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}.
$$

Its invariants are $\operatorname{tr}P=1$, $\det P=0$ and $\operatorname{rank}P=1$.

**It is not a left multiplication.** If $P=L_a$, then $a=P(e_t)=e_t$, so $L_a=\mathrm{id}$, while $P\neq\mathrm{id}$. The same argument excludes $R_b$.

**Its length is four.** The coefficient matrix is

$$
c(P)=\tfrac14\operatorname{diag}(1,-1,-1,-1),
$$

of rank four, so

$$
P=\tfrac14\bigl(T_{tt}-T_{xx}-T_{yy}-T_{zz}\bigr)
$$

is a sum of four products and of no fewer. The simplest rank-one projection is therefore not a single two-sided operator. This is the sharpest small example of the difference between the matrix rank of an operator and its length in the two-sided basis.

**A check of basis independence.** In any other basis the matrix of $P$ is $S^{-1}E_{11}S$, which is generally not diagonal, but its trace, determinant and rank are unchanged. The operator is the same; only its array of numbers moves.

## Summary

The complex-linear maps of the biquaternion algebra into itself form the endomorphism algebra $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen. A basis of $\mathbb{B}$ identifies it with $M_4(\mathbb{C})$, and the identification is a choice: a change of basis conjugates the matrices and preserves the trace, the determinant, the spectrum and the rank. The multiplication singles out the left multiplications $L_a$, the right multiplications $R_b$ and the natural conjugation $D$; the first two are four-dimensional subalgebras, their mutual commutants, and together they generate the whole operator space. The derivations are the three-dimensional inner derivations $L_a-R_a$, and the automorphisms form the three-dimensional group $PGL_2(\mathbb{C})$. The two-sided operators $T_{a,b}=L_aR_b$ are the elementary tensors of the enveloping algebra; their span is the whole operator space, but the family itself is a seven-dimensional cone, and the least number of products in a sum is the rank of the coefficient matrix. The endomorphism route and the two-sided route reach the same algebra from opposite ends: the first defines the space, the second exhibits the generating operators. The label $M_4(\mathbb{C})_{\mathbb{B},L}$ denotes the four-dimensional left regular image, not the sixteen-dimensional endomorphism algebra, although both are written with $4\times4$ matrices.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, complex dimension $4$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the coefficient basis |
| $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | the complex-linear operators on $\mathbb{B}$, dimension $16$ |
| $[F]_{\mathcal{B}}$ | the matrix of $F$ in the basis $\mathcal{B}$ |
| $S$ | the change-of-basis matrix, $[F]_{\mathcal{B}'}=S^{-1}[F]_{\mathcal{B}}S$ |
| $\operatorname{tr},\det,\operatorname{rank}$ | the basis-independent invariants of an operator |
| $L_a$ | left multiplication, $x\mapsto ax$ |
| $R_b$ | right multiplication, $x\mapsto xb$ |
| $D$ | the natural conjugation, $\operatorname{diag}(1,-1,-1,-1)$ |
| $N(a)$ | the quaternionic norm, $a_t^2+a_x^2+a_y^2+a_z^2$ |
| $\mathsf{M}_2(a)$ | the $2\times2$ matrix of $a$ in the $M_2(\mathbb{C})$ model |
| $\operatorname{ad}_a=L_a-R_a$ | the inner derivation by $a$ |
| $T_{a,b}=L_aR_b$ | the two-sided operator, $x\mapsto axb$ |
| $T_{\mu\nu}=L_{e_\mu}R_{e_\nu}$ | the sixteen basis operators |
| $c(M)$ | the coefficient matrix, $c_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{\dagger}M)$ |
| $\ell(M)$ | the length, equal to $\operatorname{rank}c(M)$ |

## Further Reading

- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra, its basis and its multiplication
- [Introduction to the Operators of the Biquaternion Algebra](introduction-to-the-operators-of-the-biquaternion-algebra.html), for the narrower question that follows this article: what the four general products decide about an operator, and what they leave to the choice of element and insertion
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the matrix algebra and the distinction from the regular model
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the plain family $T_{\tilde Q_1,\tilde Q_2}=L_{\tilde Q_1}R_{\tilde Q_2}$ and its criteria
- [The Two-Sided Operators Method to Build $M_4(\mathbb{C})$](the-two-sided-operators-method-to-build-m4c.html), for the construction from $L_a$ and $R_b$ and the sixteen matrices
- [$M_4(\mathbb{C})$ Representation : The Two-Sided Operators on the Biquaternion Algebra](m4c-representation-the-two-sided-operators-on-the-biquaternion-algebra.html), for the tables, the gamma frame and the product question
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the abstract isomorphism $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})$
- [The Operators on an Algebra](the-operators-on-an-algebra.html), for the general ambient space and the subspace-group rule
- [The Regular Representation as an Algebra of Operators](the-regular-representation-as-an-algebra-of-operators.html), for the double centraliser of the regular bimodule
- [$M_4(\mathbb{C})$ Model : The Centraliser and the Double Centraliser](m4c-model-the-centraliser-and-the-double-centraliser.html), for the centraliser of a single regular matrix
- [The Derivations and the Automorphisms of $M_4(\mathbb{C})$](the-derivations-and-the-automorphisms-of-m4c.html), for the derivations and automorphisms at matrix level
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation of the corpus
