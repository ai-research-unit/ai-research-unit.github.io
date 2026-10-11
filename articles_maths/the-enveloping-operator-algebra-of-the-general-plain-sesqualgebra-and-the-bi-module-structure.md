# __The Enveloping Operator Algebra of the General Plain Sesqualgebra and the Bi-module Structure__

## Introduction

An algebra acts on itself from the left and from the right, and the algebra in which the pair of actions naturally lives is the **enveloping algebra** $\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$, with the sandwich action $(\tilde Q\otimes\tilde P^{\mathrm{op}})\cdot\tilde R=\tilde Q\tilde R\tilde P$. For the biquaternion **algebra** this is *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*, whose main theorem is that the action is faithful and exhausts the linear operators, $\mathbb{B}^{\mathrm e}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$, and whose closing remark is that the envelope is a **luxury of the associative unital case**, the other eleven structures of the corpus keeping only their **multiplication algebra**.

The **general plain sesqualgebra** is one of those other structures, and the naive envelope of its multiplication is unavailable: the multiplication $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ is neither associative nor left-unital, so the left regular map $\tilde A\mapsto L_{\tilde A}$, $L_{\tilde A}(\tilde X)=\tilde A\star\tilde X$, is not multiplicative and no algebra structure on the parameter space presents it. What the block does carry is a **sandwich**: the operator $\tilde X\mapsto\tilde P\tilde X\tilde Q$ is unambiguous, because the plain product of $\mathbb{B}$ is associative, and pairs $(\tilde P,\tilde Q)$ therefore parametrise $\mathbb{C}$-linear operators even though the product $\tilde P\star\tilde Q$ does not. This article reads the block's operators through that sandwich, and its three results are the following.

The first is that the block's **one-sided families generate the operator algebra in pairs**. A single left multiplication $L_{\tilde A}(\tilde X)=\tilde A\tilde X^{*}$ is conjugate-linear and lies outside the $\mathbb{C}$-linear operators, but the composite of two is the ordinary two-sided multiplication, $L_{\tilde A}L_{\tilde B}=T_{\tilde A,\tilde B^{*}}$; the $\mathbb{C}$-linear operators produced by the block's own one-sided multiplications therefore fill the enveloping algebra of the underlying algebra, and it is $\mathbb{B}^{\mathrm e}$ again. The block does not add an algebra to the envelope; it adds a **reading** of it, and the reading is what the two other results make precise.

The second is the **sandwich monoid**. The conjugate-indexed parametrisation $(\tilde P,\tilde Q)\mapsto W_{\tilde P,\tilde Q}$, $W_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X\tilde Q^{*}$, is a homomorphism of monoids from the direct product $\mathbb{B}\times\mathbb{B}$ with kernel the diagonal $\mathbb{C}^{\times}$, and its image is the monoid $(\mathbb{B}\times\mathbb{B})/\mathbb{C}^{\times}$ of the **decomposable** operators, a proper submonoid of the endomorphism monoid whose **span** is the whole endomorphism algebra; the multiplication of the block is the value of the sandwich at the unit, $\tilde P\star\tilde Q=W_{\tilde P,\tilde Q}(e_0)$.

The third is the **bi-module** read through the involution. The block's regular bimodule is the algebra's, with the plain actions, which commute; the block's own one-sided multiplications are those actions **twisted by the involution** in the appropriate slot, and they no longer commute, $L_{\tilde A}R_{\tilde B}=L_{\tilde A\tilde B}$ against $R_{\tilde B}L_{\tilde A}=S_{\tilde A,\tilde B}$. So the block is a bi-module over its enveloping algebra, and the two-sidedness of the algebra's own is spent on the twist.

**Boundaries.** The block's one-sided multiplications, their parities and their composition laws are *The Left and Right Multiplications of the Biquaternion Sesqualgebra*; the sandwich is *The Sesquilinear Sandwich on the Biquaternions*; the one-sided and two-sided operators of the block are *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions* and *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*; the general operator theory of a sesqualgebra is *The Left and Right Multiplication Operators of a Sesqualgebra* and *The Sesquilinear Sandwich Operator*; the algebra's envelope, its Peirce decomposition, its bi-module and its left-versus-right question are *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*; the multiplication and the associator of the block are *Introduction to the General Plain Sesqualgebra of Biquaternions* and *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*; the projections are *Idempotents of the General Plain Sesqualgebra*; and the Peirce lines of the block are *Ideals and Peirce Decomposition of the General Plain Sesqualgebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_0$ the unit, and $i$ is the central scalar imaginary. ${}^{*}={}^{\natural}\circ\bar{\cdot}$ is the Hermitian conjugation; the block's product is $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$; the involution as an operator is $\eta(\tilde X)=\tilde X^{*}$. The four operator families are

$$
L_{\tilde A}(\tilde X)=\tilde A\star\tilde X=\tilde A\tilde X^{*},\qquad
R_{\tilde A}(\tilde X)=\tilde X\star\tilde A=\tilde X\tilde A^{*},
$$

the block's one-sided multiplications, conjugate-linear and linear, and

$$
T_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X\tilde Q,\qquad
S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*},
$$

the **ordinary two-sided multiplication** and the **sandwich**. The block's composition laws are $L_{\tilde A}L_{\tilde B}=T_{\tilde A,\tilde B^{*}}$, $R_{\tilde A}R_{\tilde B}=R_{\tilde A\tilde B}$, $L_{\tilde A}R_{\tilde B}=L_{\tilde A\tilde B}$ and $R_{\tilde B}L_{\tilde A}=S_{\tilde A,\tilde B}$ of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*. A projection is a Hermitian idempotent $\tilde\Pi=\tilde\Pi_1(\hat\mu)=\tfrac12(e_0+i\hat\mu)$ with $\hat\mu$ a real unit vector; $\tilde\Pi^{\perp}=e_0-\tilde\Pi$ is its complement, and $\tilde e_1=\tilde\Pi$, $\tilde e_2=\tilde\Pi^{\perp}$.

## The Sandwich and the Two-Sided Multiplications

### The Families and Their Parities

The block's one-sided multiplications are of opposite $\mathbb{C}$-parity: $L_{\tilde A}$ is conjugate-linear and $R_{\tilde A}$ is linear, and a single one of them is therefore not an element of a complex-algebra representation of $\mathbb{B}$ (*The Left and Right Multiplications of the Biquaternion Sesqualgebra*, §*The Obstruction to a Single Linear Representation*). The two two-sided families are of one parity each without exception: $T_{\tilde P,\tilde Q}$ is $\mathbb{C}$-linear and $S_{\tilde P,\tilde Q}$ is $\mathbb{C}$-conjugate-linear, and the difference between them is whether the involution acts.

**Remark (which product uses which).** The block multiplies by the conjugate in the second slot, so its own two-sided operator carries the involution on the right factor, and the passage from $T$ to $S$ is the insertion of $\eta$:

$$
S_{\tilde P,\tilde Q}=W_{\tilde P,\tilde Q}\circ\eta=\eta\circ T_{\tilde Q,\tilde P^{*}},\qquad W_{\tilde P,\tilde Q}=T_{\tilde P,\tilde Q^{*}} .
$$

So the block's family is the ordinary two-sided multiplication read with the conjugate in the second parameter.

### The Composition of the Two-Sided Multiplications

**Theorem.** For all $\tilde P,\tilde Q,\tilde R,\tilde S$,

$$
T_{\tilde P,\tilde Q}\,T_{\tilde R,\tilde S}=T_{\tilde P\tilde R,\tilde S\tilde Q} , \qquad
S_{\tilde P,\tilde Q}\,S_{\tilde R,\tilde S}=T_{\tilde P\tilde S,(\tilde Q\tilde R)^{*}}=W_{\tilde P\tilde S,\tilde Q\tilde R} .
$$

**Proof.** For the first, $T_{\tilde P,\tilde Q}(T_{\tilde R,\tilde S}(\tilde X))=\tilde P(\tilde R\tilde X\tilde S)\tilde Q=\tilde P\tilde R\,\tilde X\,\tilde S\tilde Q$. For the second, $S_{\tilde P,\tilde Q}(S_{\tilde R,\tilde S}(\tilde X))=S_{\tilde P,\tilde Q}(\tilde R\tilde X^{*}\tilde S^{*})=\tilde P(\tilde R\tilde X^{*}\tilde S^{*})^{*}\tilde Q^{*}=\tilde P\tilde S\tilde X\tilde R^{*}\tilde Q^{*}=T_{\tilde P\tilde S,\tilde R^{*}\tilde Q^{*}}(\tilde X)$, and $\tilde R^{*}\tilde Q^{*}=(\tilde Q\tilde R)^{*}$.

**Remark (the reversal).** The first law multiplies the two first parameters in the forward order and the two second parameters in the **reverse** order. The reversal is forced by the association of the plain product, and it is the reason the second tensor factor of the enveloping algebra is written with an $\mathrm{op}$: the two-sided multiplications are the elementary elements of $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$. The block's own family, carrying the involution, is treated in §*The Conjugate-Indexed Family and the Sandwich Monoid*.

## The Conjugate-Indexed Family and the Sandwich Monoid

### The Conjugate-Indexed Family

**Definition.** For $\tilde P,\tilde Q\in\mathbb{B}$ set

$$
W_{\tilde P,\tilde Q}=T_{\tilde P,\tilde Q^{*}},\qquad W_{\tilde P,\tilde Q}(\tilde X)=\tilde P\,\tilde X\,\tilde Q^{*} .
$$

The family is the ordinary two-sided multiplications read with the conjugate in the second parameter, and it is the family the block's product produces: $\tilde P\star\tilde Q=W_{\tilde P,\tilde Q}(e_0)$.

**Proposition (linearity).** $W_{\tilde P,\tilde Q}$ is $\mathbb{C}$-linear in $\tilde X$, $\mathbb{C}$-linear in the first parameter and $\mathbb{C}$-**anti**-linear in the second; the family is therefore a family of $\mathbb{C}$-linear operators indexed by the pairs, and not a $\mathbb{C}$-bilinear function of the pair.

**Proof.** $W_{\tilde P,\tilde Q}(\lambda\tilde X)=\lambda W_{\tilde P,\tilde Q}(\tilde X)$ and $W_{\lambda\tilde P,\tilde Q}=\lambda W_{\tilde P,\tilde Q}$, while $W_{\tilde P,\lambda\tilde Q}(\tilde X)=\tilde P\tilde X(\lambda\tilde Q)^{*}=\overline{\lambda}\,W_{\tilde P,\tilde Q}(\tilde X)$. In particular $W_{i\tilde P,\tilde Q}=-W_{\tilde P,i\tilde Q}$, so the family does not descend to the tensor product over $\mathbb{C}$ of the two copies of $\mathbb{B}$; it descends to $\mathbb{B}\otimes_{\mathbb{C}}\overline{\mathbb{B}}$, the second factor being the conjugate algebra of §*The Enveloping Algebra*.

**Theorem (the forward law).** For all $\tilde P,\tilde Q,\tilde R,\tilde S$,

$$
W_{\tilde P,\tilde Q}\,W_{\tilde R,\tilde S}=W_{\tilde P\tilde R,\tilde Q\tilde S} .
$$

**Proof.** $W_{\tilde P,\tilde Q}W_{\tilde R,\tilde S}=T_{\tilde P,\tilde Q^{*}}T_{\tilde R,\tilde S^{*}}=T_{\tilde P\tilde R,\tilde S^{*}\tilde Q^{*}}=T_{\tilde P\tilde R,(\tilde Q\tilde S)^{*}}=W_{\tilde P\tilde R,\tilde Q\tilde S}$, by the law of §*The Composition of the Two-Sided Multiplications*.

**Remark (why the law is forward).** The involution in the second slot reverses the order once, and the composition of the plain two-sided multiplications reverses it once; the two reversals cancel. This is the operator form of the product $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ read with the conjugate in the parameter: the antilinearity of $W$ in the second parameter absorbs exactly the reversal of the composition law.

### The Sandwich Monoid

**Theorem.** The parametrisation $(\tilde P,\tilde Q)\mapsto W_{\tilde P,\tilde Q}$ is a homomorphism of monoids

$$
\varphi\colon \mathbb{B}\times\mathbb{B}\longrightarrow \operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad \varphi(\tilde P,\tilde Q)=W_{\tilde P,\tilde Q},
$$

the monoid of the source being the direct product of the multiplicative monoid $(\mathbb{B},\cdot)$ with itself, with the elementwise product and the identity $(e_0,e_0)$. Its kernel is the diagonal

$$
\ker\varphi=\{(\lambda e_0,\overline{\lambda}^{-1}e_0):\lambda\in\mathbb{C}^{\times}\}\cong\mathbb{C}^{\times},
$$

and its image is the **proper** submonoid of the **decomposable** operators, so that

$$
\varphi(\mathbb{B}\times\mathbb{B})\;\cong\;(\mathbb{B}\times\mathbb{B})/\mathbb{C}^{\times}
$$

is the monoid of the elementary tensors $\tilde P\otimes\tilde Q^{\mathrm{op}}$ of $\mathbb{B}^{\mathrm e}$. The whole endomorphism algebra is the **span** of the image and not the image. The group of units of the image is $(\mathbb{B}^{\times}\times\mathbb{B}^{\times})/\mathbb{C}^{\times}$, the two unit groups amalgamated along the diagonal centre.

**Proof.** That $\varphi$ is a monoid homomorphism with the elementwise product is the forward law, and $\varphi(e_0,e_0)=W_{e_0,e_0}=\mathrm{id}$. For the kernel, $W_{\tilde P,\tilde Q}=\mathrm{id}$ means $\tilde P\tilde X\tilde Q^{*}=\tilde X$ for every $\tilde X$; at $\tilde X=e_0$ this is $\tilde P\tilde Q^{*}=e_0$, so that $\tilde P$ and $\tilde Q$ are units with $\tilde Q^{*}=\tilde P^{-1}$, and substituting this back gives $\tilde P\tilde X\tilde P^{-1}=\tilde X$ for every $\tilde X$, that is, $\tilde P$ is central; since the centre of $\mathbb{B}$ is $\mathbb{C}e_0$, this is $\tilde P=\lambda e_0$ with a nonzero complex $\lambda$, and then $\tilde Q=\overline{\lambda}^{-1}e_0$. So the kernel is the set of the pairs $(\lambda e_0,\overline{\lambda}^{-1}e_0)$, the diagonal displayed. The quotient by the kernel is the image, and under the isomorphism $\mathbb{B}^{\mathrm e}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ of §*The Enveloping Algebra* the image is the set of the elementary tensors $\tilde P\otimes\tilde Q^{\mathrm{op}}$. It is proper: at the standard pair in the matrix model the operator
$$
D\colon\tilde X\longmapsto\tilde e_1\tilde X\tilde e_1+\tilde e_2\tilde X\tilde e_2
$$
is the sum of the two independent elementary tensors $E_{11}\otimes E_{11}^{\mathrm{op}}+E_{22}\otimes E_{22}^{\mathrm{op}}$, and it is not one of them. Indeed if $D(\tilde X)=\tilde P\tilde X\tilde Q$ for all $\tilde X$, then $D(E_{11})=E_{11}$ forces the first column of $P$ and the first row of $Q$ to be nonzero, $D(E_{12})=0$ then forces the second row of $Q$ to vanish, and $D(E_{22})=E_{22}$ forces that row to be nonzero: a contradiction. The span of the image is the whole of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, because the elementary tensors $e_\mu\otimes e_\nu^{\mathrm{op}}$ over the basis are a basis of $\mathbb{B}^{\mathrm e}$, which is the dimension count of §*The Enveloping Algebra*. Finally $W_{\tilde P,\tilde Q}$ is invertible exactly when $\tilde P$ and $\tilde Q$ are, by the criterion of *The Sesquilinear Sandwich Operator*, §*The Invertible Sandwiches*, transported to $W_{\tilde P,\tilde Q}=S_{\tilde P,\tilde Q^{*}}$, so the units of the image are the classes of the pairs of units, the quotient displayed.

**Remark (the same statement for the family $T$).** The two parametrisations are exchanged by the involution of the second factor, $W_{\tilde P,\tilde Q}=T_{\tilde P,\tilde Q^{*}}$, so the statement for $T$ is the same with the kernel $\{(\lambda e_0,\lambda^{-1}e_0)\}$, the two diagonals being exchanged by the involution of the second coordinate; the image is the same submonoid of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ and the quotient is the same monoid.

**Remark (the value at the unit).** The multiplication is the diagonal of the sandwich evaluated at the unit, $\tilde P\star\tilde Q=W_{\tilde P,\tilde Q}(e_0)$, and the two terms of the associator are the two ways of composing the parameters before the evaluation,

$$
(\tilde P\star\tilde Q)\star\tilde R=W_{\tilde P\tilde Q^{*},\tilde R}(e_0),\qquad
\tilde P\star(\tilde Q\star\tilde R)=W_{\tilde P,\tilde Q\tilde R^{*}}(e_0).
$$

The associator is the difference of the two values, and it does not vanish in general because the two monoid elements $(\tilde P\tilde Q^{*},\tilde R)$ and $(\tilde P,\tilde Q\tilde R^{*})$ are not equal in the quotient $(\mathbb{B}\times\mathbb{B})/\mathbb{C}^{\times}$; the monoid law itself is not violated, and the non-associativity of the multiplication is the non-equality of those two monoid elements. The associator is computed in *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*.

## The Enveloping Algebra

### The Definition

**Definition.** The **enveloping algebra** of the block over $\mathbb{C}$ is the enveloping algebra of the underlying algebra,

$$
\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}},
$$

with multiplication the tensor product of the plain multiplications, $(\tilde P\otimes\tilde Q^{\mathrm{op}})(\tilde R\otimes\tilde S^{\mathrm{op}})=\tilde P\tilde R\otimes(\tilde S\tilde Q)^{\mathrm{op}}$, and unit $e_0\otimes e_0^{\mathrm{op}}$. It has complex dimension $16$, and it acts on $\mathbb{B}$ by the **sandwich action**

$$
(\tilde P\otimes\tilde Q^{\mathrm{op}})\cdot\tilde X=\tilde P\tilde X\tilde Q=T_{\tilde P,\tilde Q}(\tilde X).
$$

**Remark (why the envelope is the algebra's).** The block's multiplication is neither associative nor left-unital, so it produces no algebra structure on $\mathbb{B}$ and no envelope of its own; what it produces is the family of sandwich operators, and those operators are the elementary elements of the envelope of the underlying plain product. The block's own multiplication is recovered from the envelope together with the involution, $\star=m\circ(\mathrm{id}\otimes\eta)$, $m$ being the plain multiplication read as $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\to\mathbb{B}$, and this is stated as the comparison of §*The Comparison with the Algebra*.

### The Enveloping Algebra Is the Endomorphism Algebra

**Theorem.** The sandwich action defines an isomorphism of $\mathbb{C}$-algebras

$$
\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad \tilde P\otimes\tilde Q^{\mathrm{op}}\mapsto\bigl(\tilde X\mapsto\tilde P\tilde X\tilde Q\bigr),
$$

so that $\mathbb{B}^{\mathrm e}\cong M_4(\mathbb{C})$ and the left action of $\mathbb{B}^{\mathrm e}$ on $\mathbb{B}$ is faithful and exhausts all $\mathbb{C}$-linear operators.

**Proof.** This is the theorem of *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*, §*The Enveloping Algebra*, whose algebra is the same $\mathbb{B}$ with the same plain product; the proof there runs on the matrix units of $\mathbb{B}\cong M_2(\mathbb{C})$ and applies here without change. In particular the two-sided multiplications $T_{\tilde P,\tilde Q}$ are the elementary tensors, and they span the whole endomorphism algebra, which is the spanning statement used in §*The Sandwich Monoid*.

### The Block's Operators in the Envelope

**Corollary (the block's operator content).** The block's own operators are the elements of the envelope twisted by the involution:

$$
R_{\tilde A}=\varphi\bigl(e_0\otimes(\tilde A^{*})^{\mathrm{op}}\bigr),\qquad
\Theta_{\tilde Q}=\varphi\bigl(\tilde Q\otimes(\tilde Q^{*})^{\mathrm{op}}\bigr),\qquad
L_{\tilde A}=\varphi\bigl(\tilde A\otimes e_0^{\mathrm{op}}\bigr)\circ\eta ,
$$

where $\varphi(\tilde P\otimes\tilde Q^{\mathrm{op}})$ is the sandwich action of $\tilde P\otimes\tilde Q^{\mathrm{op}}$.

**Proof.** $\varphi(e_0\otimes(\tilde A^{*})^{\mathrm{op}})(\tilde X)=e_0\tilde X\tilde A^{*}=\tilde X\tilde A^{*}=R_{\tilde A}(\tilde X)$, so the right multiplications are the envelope's right-sided elements with the conjugated parameter. The two-sided operator $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{\dagger}=\tilde Q\tilde X\tilde Q^{*}$ is $\varphi(\tilde Q\otimes(\tilde Q^{*})^{\mathrm{op}})$, the elementary tensor whose two parameters are conjugate. Finally $\varphi(\tilde A\otimes e_0^{\mathrm{op}})(\tilde X)=\tilde A\tilde X$, so $L_{\tilde A}(\tilde X)=\tilde A\tilde X^{*}=(\varphi(\tilde A\otimes e_0^{\mathrm{op}})\circ\eta)(\tilde X)$.

**Remark (the pair generation).** The corollary explains the block's composition laws. The product of two right multiplications stays among the envelope's right-sided elements, $R_{\tilde A}R_{\tilde B}=\varphi(e_0\otimes(\tilde B^{*}\tilde A^{*})^{\mathrm{op}})=R_{\tilde A\tilde B}$; the product of two left multiplications leaves the conjugate-linear operators and is the elementary tensor $L_{\tilde A}L_{\tilde B}=T_{\tilde A,\tilde B^{*}}$, that is $\varphi(\tilde A\otimes\tilde B^{\mathrm{op}})$ read with the conjugated parameter; and a mixed product is a left multiplication or a sandwich according to the order. So the even products of the block's own one-sided multiplications span the envelope, and a single one-sided multiplication never lies in it: a single one is not $\mathbb{C}$-linear, and the pairs are. In the notation of §*The Conjugate-Indexed Family and the Sandwich Monoid*, $L_{\tilde A}L_{\tilde B}=W_{\tilde A,\tilde B}$, $R_{\tilde A}=W_{e_0,\tilde A}$ and $L_{\tilde A}=W_{\tilde A,e_0}\circ\eta$.

### The Base Field and the Real Dimension Count

**Remark (over $\mathbb{R}$ the action is not faithful).** Regard $\mathbb{B}$ as a real algebra, $\dim_{\mathbb{R}}\mathbb{B}=8$, so that $\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B}^{\mathrm{op}}$ has real dimension $64$, the same as $\operatorname{End}_{\mathbb{R}}(\mathbb{B})$. The sandwich map is then **not** injective: the element $i e_0\otimes e_0^{\mathrm{op}}-e_0\otimes(i e_0)^{\mathrm{op}}$ acts as $\tilde X\mapsto i\tilde X-\tilde X i=0$, because $i$ is central, and the image is only the space of $\mathbb{C}$-linear operators, of real dimension $32$, so the kernel has real dimension $32$. The complex base field removes exactly this redundancy, which is why the theorem above is stated over $\mathbb{C}$; the computation is the one of *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*, §*The Base Field and the Real Dimension Count*, and the block inherits it unchanged.

### The Comparison with the Algebra

**Remark (the conjugate-indexed prescription and the conjugate algebra).** The block's parametrisation $(\tilde P,\tilde Q)\mapsto W_{\tilde P,\tilde Q}$ is $\mathbb{C}$-antilinear in the second coordinate (§*The Conjugate-Indexed Family and the Sandwich Monoid*, Proposition), so it is not the elementary-tensor map of the envelope. It becomes one after the substitution $\tilde Q\mapsto\tilde Q^{*}$, which is the identification of $\mathbb{B}$ with its conjugate algebra $\overline{\mathbb{B}}$: the assignment

$$
\tilde P\otimes\overline{\tilde Q}\longmapsto W_{\tilde P,\tilde Q}=\bigl(\tilde X\mapsto\tilde P\tilde X\tilde Q^{*}\bigr)
$$

is an isomorphism of $\mathbb{C}$-algebras $\mathbb{B}\otimes_{\mathbb{C}}\overline{\mathbb{B}}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, and $\overline{\mathbb{B}}\to\mathbb{B}^{\mathrm{op}}$, $\tilde Q\mapsto\tilde Q^{*}$, is an isomorphism of $\mathbb{C}$-algebras. So the block's envelope is the algebra's with the second factor conjugated, and the passage from one presentation to the other is the involution.

**Remark (what the block adds and what it does not).** The block adds **nothing to the algebra of the envelope**: $\mathbb{B}^{\mathrm e}$ is the underlying algebra's, and the block's product is not a new multiplication on it but the derived product $m\circ(\mathrm{id}\otimes\eta)$. What the block adds is the **reading**: its one-sided multiplications are the envelope's one-sided elements twisted by the involution, its product is the diagonal of the sandwich monoid, and its bi-module of §*The Bi-module Structure* is the algebra's bimodule with the involution inserted. In the language of §*The Envelope as a Luxury of the Associative Unital Case* of the twin, the block inherits the envelope exactly because the sandwich uses the associative unital **plain** product, and what it does not inherit is the multiplicativity of its own regular maps, $\tilde A\mapsto L_{\tilde A}$ not being multiplicative and $\tilde A\mapsto R_{\tilde A}$ being multiplicative only in the plain parameter. The block's envelope is therefore a genuine instance and not a new structure, and the article's content is the reading rather than the algebra.

### The Peirce Decomposition of the Enveloping Algebra

The Peirce decomposition of the block of *Ideals and Peirce Decomposition of the General Plain Sesqualgebra* tensors to a decomposition of $\mathbb{B}^{\mathrm e}$, exactly as in the algebra's case. The four elements

$$
E_{ik}=\tilde e_i\otimes\tilde e_k^{\mathrm{op}},\qquad i,k\in\{1,2\},
$$

are idempotent and pairwise orthogonal, $E_{ik}E_{jl}=\delta_{ij}\delta_{kl}E_{ik}$, and they sum to the unit $e_0\otimes e_0^{\mathrm{op}}=\sum_{ik}E_{ik}$; they are primitive, each corner $E_{ik}\mathbb{B}^{\mathrm e}E_{ik}$ being the one-dimensional line $\mathbb{C}(\tilde e_i\otimes\tilde e_k^{\mathrm{op}})$.

**Proposition (the sixteen corners).** The Peirce decomposition of $\mathbb{B}^{\mathrm e}$ with respect to the family $E_{ik}$ has sixteen one-dimensional corners

$$
E_{ik}\,\mathbb{B}^{\mathrm e}\,E_{jl}=\bigl(\tilde e_i\mathbb{B}\tilde e_j\bigr)\otimes\bigl(\tilde e_l\mathbb{B}\tilde e_k\bigr)^{\mathrm{op}}=\mathbb{C}\bigl(\Lambda_{ij}\otimes\Lambda_{lk}^{\mathrm{op}}\bigr),
$$

where $\Lambda_{ij}$ generates the block's corner $\tilde e_i\mathbb{B}\tilde e_j$ — that is $\tilde\Pi,\tilde\Upsilon_1,\tilde\Upsilon_2,\tilde\Pi^{\perp}$ for $(i,j)=(1,1),(1,2),(2,1),(2,2)$ — and the corners multiply by

$$
\bigl(E_{ik}\mathbb{B}^{\mathrm e}E_{jl}\bigr)\bigl(E_{i'k'}\mathbb{B}^{\mathrm e}E_{j'l'}\bigr)\subseteq\delta_{ji'}\delta_{lk'}\,E_{ik}\mathbb{B}^{\mathrm e}E_{j'l'} .
$$

**Proof.** The corner is $(\tilde e_i\otimes\tilde e_k^{\mathrm{op}})(\mathbb{B}\otimes\mathbb{B}^{\mathrm{op}})(\tilde e_j\otimes\tilde e_l^{\mathrm{op}})=(\tilde e_i\mathbb{B}\tilde e_j)\otimes(\tilde e_l\mathbb{B}\tilde e_k)^{\mathrm{op}}$, the reversal of the second index pair being the reversal of the multiplication in the second factor; each factor is one-dimensional by *Ideals and Peirce Decomposition of the General Plain Sesqualgebra*, §*The Biquaternion Cases*, and the product rule is the algebra table applied in each factor, with the second factor read in the reversed order.

**Remark (the second Peirce index is reversed).** The corner basis element is $\Lambda_{ij}\otimes\Lambda_{lk}^{\mathrm{op}}$, with the second index pair reversed, and the transposed shape is not an artefact of the writing: it is the reversal of §*The Composition of the Two-Sided Multiplications*, the same reversal as in the composition of the elementary tensors, and it is the reason the second factor is written with an $\mathrm{op}$. The block's own multiplication then reads the corners with the **transposed** index rule of *Ideals and Peirce Decomposition of the General Plain Sesqualgebra*, §*The Two Tables*; the envelope's reversal and the multiplication's transposition are the two faces of the same involution.

**Remark (the action of the four idempotents).** Under the sandwich action the four idempotents cut the block itself:

$$
E_{ik}\cdot\tilde X=(\tilde e_i\otimes\tilde e_k^{\mathrm{op}})\cdot\tilde X=\tilde e_i\tilde X\tilde e_k ,
$$

which is the Peirce projection onto the corner $\tilde e_i\mathbb{B}\tilde e_k$ of the block. Since the four idempotents are complete and orthogonal, the left $\mathbb{B}^{\mathrm e}$-module ${}_{\mathbb{B}^{\mathrm e}}\mathbb{B}$ splits as the direct sum of the four complex lines $\tilde e_i\mathbb{B}\tilde e_k$: the Peirce decomposition of the block is the decomposition of $\mathbb{B}$ as a module over its enveloping algebra, and the identity operator is $\sum_{ik}E_{ik}=e_0\otimes e_0^{\mathrm{op}}$. This is the module form of *Ideals and Peirce Decomposition of the General Plain Sesqualgebra*.

**Remark (where the family comes from).** The complementary pair $(\tilde\Pi,\tilde\Pi^{\perp})$ that indexes the four idempotents is a pair of **orthogonal** right $\star$-ideals of the block, and it is one pair out of the projective line of them: by *Ideals and Peirce Decomposition of the General Plain Sesqualgebra*, §*The Complementary Pairs and the Peirce Decompositions*, every unordered pair of distinct right ideals carries a complete family $\tilde e,e_0-\tilde e$ and a Peirce decomposition, and the orthogonal pairs are exactly the ones whose idempotents are Hermitian, that is, the pairs of projections used here. The four idempotents of the envelope, the corners of the block and the $2\times2$ matrix realizations of the same section are three readings of the one right-ideal lattice.

## The Bi-module Structure

### The Definition and the Twisted Actions

**Definition.** A $\mathbb{B}$-$\mathbb{B}$**-bi-module** is a complex vector space $M$ with a left and a right $\mathbb{B}$-action that commute, $(\tilde P\cdot m)\cdot\tilde Q=\tilde P\cdot(m\cdot\tilde Q)$. The block with the **plain** actions,

$$
\tilde P\cdot\tilde X=\tilde P\tilde X,\qquad \tilde X\cdot\tilde Q=\tilde X\tilde Q ,
$$

is the algebra's regular bi-module, and it is the left regular module of the enveloping algebra by $(\tilde P\otimes\tilde Q^{\mathrm{op}})\cdot\tilde X=\tilde P\tilde X\tilde Q$. With the **twisted** actions of the block,

$$
\tilde P\cdot\tilde X=\tilde P\star\tilde X=L_{\tilde P}(\tilde X),\qquad \tilde X\cdot\tilde Q=\tilde X\star\tilde Q=R_{\tilde Q}(\tilde X),
$$

the same space carries the two one-sided families of the multiplication.

**Proposition (the twist).** On the regular bi-module the twisted actions are the plain actions composed with the involution in one slot,

$$
L_{\tilde P}(\tilde X)=\bigl((\tilde P\cdot{})\circ\eta\bigr)(\tilde X),\qquad
R_{\tilde Q}(\tilde X)=\bigl(({}\cdot\tilde Q^{*})\bigr)(\tilde X),
$$

and the twisted actions **do not commute**: $L_{\tilde A}R_{\tilde B}=L_{\tilde A\tilde B}$ while $R_{\tilde B}L_{\tilde A}=S_{\tilde A,\tilde B}$, and the two differ in general, the witness being $\tilde A=e_1,\tilde B=e_2,\tilde X=e_0$, where $L_{e_1}R_{e_2}(e_0)=e_3$ and $R_{e_2}L_{e_1}(e_0)=-e_3$.

**Proof.** The first display is the definition, $L_{\tilde P}(\tilde X)=\tilde P\tilde X^{*}$ and $R_{\tilde Q}(\tilde X)=\tilde X\tilde Q^{*}$. The composition laws are those of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, §*The Mixed Composites*: $L_{\tilde A}R_{\tilde B}(\tilde X)=\tilde A(\tilde X\tilde B^{*})^{*}=\tilde A\tilde B\tilde X^{*}=L_{\tilde A\tilde B}(\tilde X)$ and $R_{\tilde B}L_{\tilde A}(\tilde X)=(\tilde A\tilde X^{*})\tilde B^{*}=\tilde A\tilde X^{*}\tilde B^{*}=S_{\tilde A,\tilde B}(\tilde X)$; the value at $\tilde A=e_1,\tilde B=e_2,\tilde X=e_0$ is $e_1e_2=e_3$ against $e_1e_0^{*}e_2^{*}=e_1\cdot e_0\cdot(-e_2)=-e_3$, the witness recorded in that article.

**Remark (what the failure costs).** The plain actions commute and make $\mathbb{B}$ a bi-module; the twisted actions do not, so the multiplication alone does not give a bi-module structure on the block. The failure is the non-associativity of the multiplication, and it is measured by the difference between the left multiplication $L_{\tilde A\tilde B}$ and the sandwich $S_{\tilde A,\tilde B}$ of the mixed composites. The block therefore has a bi-module structure only through its enveloping algebra: $\mathbb{B}$ is the left regular module of $\mathbb{B}^{\mathrm e}$, the multiplication is the diagonal of the envelope read at the unit, and the two twisted actions are the plain ones read through the derived product $m\circ(\mathrm{id}\otimes\eta)$, so the loss of commutativity is the price of the derivation.

### The Two-Sided Operators and the Diagonal

**Corollary.** The two-sided operators of the block are the diagonal of the sandwich family, $\Theta_{\tilde Q}=W_{\tilde Q,\tilde Q}=\varphi(\tilde Q\otimes(\tilde Q^{*})^{\mathrm{op}})$, that is the subfamily in which the two parameters are conjugate.

**Proof.** $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}=W_{\tilde Q,\tilde Q}(\tilde X)$.

### The Left-versus-Right Question

The algebra records a question of which of the two regular actions carries a given physical degree of freedom, and answers the algebraic half of it by exhibiting the pair inside one commutative envelope. The block answers it differently.

**What the block says.** The two one-sided families of the block are **not** of the same algebraic type: the left multiplications are conjugate-linear and the right ones are linear, and a single one of either kind is not an element of the enveloping algebra but at best an element composed with the involution (§*The Enveloping Algebra*, Corollary). The pair is therefore not a pair of commuting copies inside the envelope; the two families do not even commute (§*The Twisted Actions*), and the honest commuting pair inside the envelope is the **plain** left and right multiplications, which is the algebra's.

**The precise form of the question for the block.** A construction covariant under the block and multiplying the unknown on both sides uses the twisted actions, hence the sandwich parameters rather than the factor parameters; the question of which face of the block carries which physical degree of freedom is then the question of which sandwich parameter is the left one, a question that the algebra alone can only relocate into the envelope, where the two factors are the same algebra $\mathbb{B}$ up to the involution and the involution is the only thing that distinguishes them.

## Worked Verification

The claims of the article were recomputed on the model $\mathsf{M}_2$ at no more than one hundred samples per claim.

- **The composition laws.** The laws $T_{\tilde P,\tilde Q}T_{\tilde R,\tilde S}=T_{\tilde P\tilde R,\tilde S\tilde Q}$, $W_{\tilde P,\tilde Q}W_{\tilde R,\tilde S}=W_{\tilde P\tilde R,\tilde Q\tilde S}$, $S_{\tilde P,\tilde Q}S_{\tilde R,\tilde S}=T_{\tilde P\tilde S,(\tilde Q\tilde R)^{*}}$ and the four laws of *The Left and Right Multiplications of the Biquaternion Sesqualgebra* were verified with residual at most $2\cdot10^{-13}$ on a hundred quadruples each.
- **The monoid kernel.** The scaling $(\tilde P,\tilde Q)\mapsto(\lambda\tilde P,\overline{\lambda}^{-1}\tilde Q)$ leaves $W_{\tilde P,\tilde Q}$ unchanged on a hundred random pairs and scalars, with residual at most $5\cdot10^{-16}$, and the operator is the identity exactly on that set, as the theorem states.
- **The span.** The complex span of the sixteen operators $T_{e_\mu,e_\nu}$ over the basis is all of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen, and the real span of the sandwich operators over the real basis is thirty-two.
- **The properness of the image.** The operator $D(\tilde X)=E_{11}\tilde XE_{11}+E_{22}\tilde XE_{22}$ has coefficient matrix $\operatorname{diag}(1,0,0,1)$ of rank two in the tensor basis $E_{ij}\otimes E_{kl}^{\mathrm{op}}$, so it is not an elementary tensor; and the equations of the proof were checked on the matrix units, where $PE_{11}Q=E_{11}$ forces the first column of $P$ and the first row of $Q$ nonzero, $PE_{12}Q=0$ then forces the second row of $Q$ to vanish, and $PE_{22}Q=E_{22}$ forces it not to.
- **The envelope axioms.** The sandwich action is a left action (residual zero on a hundred triples), the unit acts as the identity, the map $\mathbb{B}\otimes\mathbb{B}^{\mathrm{op}}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is multiplicative, and the identity operator is $T_{e_0,e_0}$.
- **The block's operators in the envelope.** The identities $R_{\tilde A}=W_{e_0,\tilde A}$, $\Theta_{\tilde Q}=W_{\tilde Q,\tilde Q}$, $L_{\tilde A}=W_{\tilde A,e_0}\circ\eta$, $L_{\tilde A}L_{\tilde B}=W_{\tilde A,\tilde B}$ and the witness $L_{e_1}R_{e_2}(e_0)=e_3$, $R_{e_2}L_{e_1}(e_0)=-e_3$ were each verified with residual zero.

## Summary

The block's one-sided multiplications are of opposite $\mathbb{C}$-parity, and a single one lies outside the $\mathbb{C}$-linear operators, but the product of two lies inside: $L_{\tilde A}L_{\tilde B}=T_{\tilde A,\tilde B^{*}}$, and the products of the block's own one-sided multiplications fill the enveloping algebra of the underlying plain product.

The parametrisation $(\tilde P,\tilde Q)\mapsto W_{\tilde P,\tilde Q}$, $W_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X\tilde Q^{*}$, is a homomorphism of monoids from the direct product $\mathbb{B}\times\mathbb{B}$ with kernel the diagonal $\mathbb{C}^{\times}$, and its image is the monoid $(\mathbb{B}\times\mathbb{B})/\mathbb{C}^{\times}$ of the decomposable operators, a proper submonoid of the endomorphism monoid whose span is the whole endomorphism algebra; the block's product is the value of the sandwich at the unit, $\tilde P\star\tilde Q=W_{\tilde P,\tilde Q}(e_0)$. The parametrisation is $\mathbb{C}$-linear in the first parameter and conjugate-linear in the second, so its envelope is $\mathbb{B}\otimes_{\mathbb{C}}\overline{\mathbb{B}}$, the second factor conjugated and isomorphic to $\mathbb{B}^{\mathrm{op}}$.

The enveloping algebra is $\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$ with the sandwich action, $\mathbb{B}^{\mathrm e}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$, and it is the algebra's; the block's right multiplications and two-sided operators are its elements with the conjugated parameter, its left multiplications its elements composed with the involution, and its product is the derived product $m\circ(\mathrm{id}\otimes\eta)$. The block is the left regular module of the envelope, and its Peirce decomposition is the module decomposition along the four idempotents $\tilde e_i\otimes\tilde e_k^{\mathrm{op}}$, whose corner basis is $\Lambda_{ij}\otimes\Lambda_{lk}^{\mathrm{op}}$ with the second index pair reversed. The plain actions make $\mathbb{B}$ a bi-module and commute; the block's twisted actions do not commute, and the failure is the non-associativity of the multiplication.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the general plain sesquilinear product, the multiplication of the block |
| $\eta(\tilde X)=\tilde X^{*}$ | the involution as an operator |
| $L_{\tilde A},R_{\tilde A}$ | the block's one-sided multiplications, conjugate-linear and linear |
| $T_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X\tilde Q$ | the ordinary two-sided multiplication, $\mathbb{C}$-linear |
| $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*}$ | the sandwich, $\mathbb{C}$-conjugate-linear |
| $W_{\tilde P,\tilde Q}=T_{\tilde P,\tilde Q^{*}}$ | the conjugate-indexed family, the block's own sandwich |
| $\Theta_{\tilde Q}=W_{\tilde Q,\tilde Q}$ | the two-sided operator $\tilde Q\tilde X\tilde Q^{\dagger}$, the diagonal |
| $\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$ | the enveloping algebra of the block, with the sandwich action |
| $\overline{\mathbb{B}}$ | the conjugate algebra, $\overline{\mathbb{B}}\cong\mathbb{B}^{\mathrm{op}}$ by $\tilde Q\mapsto\tilde Q^{*}$ |
| $E_{ik}=\tilde e_i\otimes\tilde e_k^{\mathrm{op}}$ | the four idempotents of the envelope's Peirce family |
| $\Lambda_{ij}$ | the generator of the Peirce corner $\tilde e_i\mathbb{B}\tilde e_j$ |

## Further Reading

- *The Left and Right Multiplications of the Biquaternion Sesqualgebra* — the parities, the composition laws and the four families.
- *The Sesquilinear Sandwich on the Biquaternions* — the sandwich $S_{\tilde P,\tilde Q}$ and its composition table.
- *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions* — the block's one-sided operators and the double centraliser.
- *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions* — the two-sided operator $\Theta_{\tilde Q}$ and its square law.
- *The Left and Right Multiplication Operators of a Sesqualgebra* — the general operator theory of a sesqualgebra.
- *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure* — the twin, with the algebra's envelope, its Peirce decomposition and the bi-module.
- *Ideals and Peirce Decomposition of the General Plain Sesqualgebra* — the four Peirce lines of the block that the envelope cuts out.
- *Idempotents of the General Plain Sesqualgebra* — the projections that index the Peirce family.
- *The Ternary Product and the Associator of the Biquaternion Sesqualgebra* — the associator whose two terms are the two values of the sandwich monoid.
