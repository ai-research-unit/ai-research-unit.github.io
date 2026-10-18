# __The Enveloping Operator Algebra of the General Plain Sesqualgebra and the Bi-module Structure__

## Introduction

An algebra acts on itself from the left and from the right, and the algebra in which the pair of actions naturally lives is the **enveloping algebra** $\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$, with the sandwich action $(\tilde Q_2\otimes\tilde Q_1^{\mathrm{opp}})\cdot\tilde{Q}_5=\tilde Q_2\tilde{Q}_5\tilde Q_1$. For the biquaternion **algebra** this is *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*, whose main theorem is that the action is faithful and exhausts the linear operators, $\mathbb{B}^{\mathrm e}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$, and whose closing remark is that the envelope is a **luxury of the associative unital case**, the other eleven structures of the corpus keeping only their **multiplication algebra**.

The **general plain sesqualgebra** is one of those other structures, and the naive envelope of its multiplication is unavailable: the multiplication $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ is neither associative nor left-unital, so the left regular map $\tilde Q_6\mapsto L_{\tilde Q_6}$, $L_{\tilde Q_6}(\tilde Q_3)=\tilde Q_6\star\tilde Q_3$, is not multiplicative and no algebra structure on the parameter space presents it. What the block does carry is a **sandwich**: the operator $\tilde Q_3\mapsto\tilde Q_1\tilde Q_3\tilde Q_2$ is unambiguous, because the plain product of $\mathbb{B}$ is associative, and pairs $(\tilde Q_1,\tilde Q_2)$ therefore parametrise $\mathbb{C}$-linear operators even though the product $\tilde Q_1\star\tilde Q_2$ does not. This article reads the block's operators through that sandwich, and its three results are the following.

The first is that the block's **one-sided families generate the operator algebra in pairs**. A single left multiplication $L_{\tilde Q_6}(\tilde Q_3)=\tilde Q_6\tilde Q_3^{*}$ is conjugate-linear and lies outside the $\mathbb{C}$-linear operators, but the composite of two is the ordinary two-sided multiplication, $L_{\tilde Q_6}L_{\tilde Q_4}=T_{\tilde Q_6,\tilde Q_4^{*}}$; the $\mathbb{C}$-linear operators produced by the block's own one-sided multiplications therefore fill the enveloping algebra of the underlying algebra, and it is $\mathbb{B}^{\mathrm e}$ again. The block does not add an algebra to the envelope; it adds a **reading** of it, and the reading is what the two other results make precise.

The second is the **sandwich monoid**. The conjugate-indexed parametrisation $(\tilde Q_1,\tilde Q_2)\mapsto W_{\tilde Q_1,\tilde Q_2}$, $W_{\tilde Q_1,\tilde Q_2}(\tilde Q_3)=\tilde Q_1\tilde Q_3\tilde Q_2^{*}$, is a homomorphism of monoids from the direct product $\mathbb{B}\times\mathbb{B}$ with kernel the diagonal $\mathbb{C}^{\times}$, and its image is the monoid $(\mathbb{B}\times\mathbb{B})/\mathbb{C}^{\times}$ of the **decomposable** operators, a proper submonoid of the endomorphism monoid whose **span** is the whole endomorphism algebra; the multiplication of the block is the value of the sandwich at the unit, $\tilde Q_1\star\tilde Q_2=W_{\tilde Q_1,\tilde Q_2}(e_t)$.

The third is the **bi-module** read through the involution. The block's regular bimodule is the algebra's, with the plain actions, which commute; the block's own one-sided multiplications are those actions **twisted by the involution** in the appropriate slot, and they no longer commute, $L_{\tilde Q_6}R_{\tilde Q_4}=L_{\tilde Q_6\tilde Q_4}$ against $R_{\tilde Q_4}L_{\tilde Q_6}=S_{\tilde Q_6,\tilde Q_4}$. So the block is a bi-module over its enveloping algebra, and the two-sidedness of the algebra's own is spent on the twist.

**Boundaries.** The block's one-sided multiplications, their parities and their composition laws are *The Left and Right Multiplications of the Biquaternioid Sesqualgebra*; the sandwich is *The Sesquilinear Sandwich on the Biquaternioid*; the one-sided and two-sided operators of the block are *One-Sided Operators on the General Plain Sesqualgebra* and *Two-Sided Operators on the General Plain Sesqualgebra*; the general operator theory of a sesqualgebra is *The Left and Right Multiplication Operators of a Sesqualgebra* and *The Sesquilinear Sandwich Operator*; the algebra's envelope, its Peirce decomposition, its bi-module and its left-versus-right question are *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*; the multiplication and the associator of the block are *Introduction to the General Plain Sesqualgebra* and *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*; the projections are *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*; and the Peirce lines of the block are *Ideals and Peirce Decomposition of the General Plain Sesqualgebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t$ the unit, and $i$ is the central scalar imaginary. ${}^{*}={}^{\natural}\circ\bar{\cdot}$ is the Hermitian conjugation; the block's product is $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$; the involution as an operator is $\eta(\tilde Q_3)=\tilde Q_3^{*}$. The four operator families are

$$
L_{\tilde Q_6}(\tilde Q_3)=\tilde Q_6\star\tilde Q_3=\tilde Q_6\tilde Q_3^{*},\qquad
R_{\tilde Q_6}(\tilde Q_3)=\tilde Q_3\star\tilde Q_6=\tilde Q_3\tilde Q_6^{*},
$$

the block's one-sided multiplications, conjugate-linear and linear, and

$$
T_{\tilde Q_1,\tilde Q_2}(\tilde Q_3)=\tilde Q_1\tilde Q_3\tilde Q_2,\qquad
S_{\tilde Q_1,\tilde Q_2}(\tilde Q_3)=\tilde Q_1\tilde Q_3^{*}\tilde Q_2^{*},
$$

the **ordinary two-sided multiplication** and the **sandwich**. The block's composition laws are $L_{\tilde Q_6}L_{\tilde Q_4}=T_{\tilde Q_6,\tilde Q_4^{*}}$, $R_{\tilde Q_6}R_{\tilde Q_4}=R_{\tilde Q_6\tilde Q_4}$, $L_{\tilde Q_6}R_{\tilde Q_4}=L_{\tilde Q_6\tilde Q_4}$ and $R_{\tilde Q_4}L_{\tilde Q_6}=S_{\tilde Q_6,\tilde Q_4}$ of *The Left and Right Multiplications of the Biquaternioid Sesqualgebra*. A Hermitian idempotent is an idempotent $\tilde\Pi=\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi)$ with $\vec u$ a real unit vector; $\tilde\Pi^{\perp}=e_t-\tilde\Pi$ is its complement, and $\tilde\Pi_+=\tilde\Pi$, $\tilde\Pi_-=\tilde\Pi^{\perp}$.

## The Sandwich and the Two-Sided Multiplications

### The Families and Their Parities

The block's one-sided multiplications are of opposite $\mathbb{C}$-parity: $L_{\tilde Q_6}$ is conjugate-linear and $R_{\tilde Q_6}$ is linear, and a single one of them is therefore not an element of a complex-algebra representation of $\mathbb{B}$ (*The Left and Right Multiplications of the Biquaternioid Sesqualgebra*, §*The Obstruction to a Single Linear Representation*). The two two-sided families are of one parity each without exception: $T_{\tilde Q_1,\tilde Q_2}$ is $\mathbb{C}$-linear and $S_{\tilde Q_1,\tilde Q_2}$ is $\mathbb{C}$-conjugate-linear, and the difference between them is whether the involution acts.

**Remark (which product uses which).** The block multiplies by the conjugate in the second slot, so its own two-sided operator carries the involution on the right factor, and the passage from $T$ to $S$ is the insertion of $\eta$:

$$
S_{\tilde Q_1,\tilde Q_2}=W_{\tilde Q_1,\tilde Q_2}\circ\eta=\eta\circ T_{\tilde Q_2,\tilde Q_1^{*}},\qquad W_{\tilde Q_1,\tilde Q_2}=T_{\tilde Q_1,\tilde Q_2^{*}} .
$$

So the block's family is the ordinary two-sided multiplication read with the conjugate in the second parameter.

### The Composition of the Two-Sided Multiplications

**Theorem.** For all $\tilde Q_1,\tilde Q_2,\tilde{Q}_5,\tilde Q_7$,

$$
T_{\tilde Q_1,\tilde Q_2}\,T_{\tilde{Q}_5,\tilde Q_7}=T_{\tilde Q_1\tilde{Q}_5,\tilde Q_7\tilde Q_2} , \qquad
S_{\tilde Q_1,\tilde Q_2}\,S_{\tilde{Q}_5,\tilde Q_7}=T_{\tilde Q_1\tilde Q_7,(\tilde Q_2\tilde{Q}_5)^{*}}=W_{\tilde Q_1\tilde Q_7,\tilde Q_2\tilde{Q}_5} .
$$

**Proof.** For the first, $T_{\tilde Q_1,\tilde Q_2}(T_{\tilde{Q}_5,\tilde Q_7}(\tilde Q_3))=\tilde Q_1(\tilde{Q}_5\tilde Q_3\tilde Q_7)\tilde Q_2=\tilde Q_1\tilde{Q}_5\,\tilde Q_3\,\tilde Q_7\tilde Q_2$. For the second, $S_{\tilde Q_1,\tilde Q_2}(S_{\tilde{Q}_5,\tilde Q_7}(\tilde Q_3))=S_{\tilde Q_1,\tilde Q_2}(\tilde{Q}_5\tilde Q_3^{*}\tilde Q_7^{*})=\tilde Q_1(\tilde{Q}_5\tilde Q_3^{*}\tilde Q_7^{*})^{*}\tilde Q_2^{*}=\tilde Q_1\tilde Q_7\tilde Q_3\tilde{Q}_5^{*}\tilde Q_2^{*}=T_{\tilde Q_1\tilde Q_7,\tilde{Q}_5^{*}\tilde Q_2^{*}}(\tilde Q_3)$, and $\tilde{Q}_5^{*}\tilde Q_2^{*}=(\tilde Q_2\tilde{Q}_5)^{*}$.

**Remark (the reversal).** The first law multiplies the two first parameters in the forward order and the two second parameters in the **reverse** order. The reversal is forced by the association of the plain product, and it is the reason the second tensor factor of the enveloping algebra is written with an $\mathrm{op}$: the two-sided multiplications are the elementary elements of $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$. The block's own family, carrying the involution, is treated in §*The Conjugate-Indexed Family and the Sandwich Monoid*.

## The Conjugate-Indexed Family and the Sandwich Monoid

### The Conjugate-Indexed Family

**Definition.** For $\tilde Q_1,\tilde Q_2\in\mathbb{B}$ set

$$
W_{\tilde Q_1,\tilde Q_2}=T_{\tilde Q_1,\tilde Q_2^{*}},\qquad W_{\tilde Q_1,\tilde Q_2}(\tilde Q_3)=\tilde Q_1\,\tilde Q_3\,\tilde Q_2^{*} .
$$

The family is the ordinary two-sided multiplications read with the conjugate in the second parameter, and it is the family the block's product produces: $\tilde Q_1\star\tilde Q_2=W_{\tilde Q_1,\tilde Q_2}(e_t)$.

**Proposition (linearity).** $W_{\tilde Q_1,\tilde Q_2}$ is $\mathbb{C}$-linear in $\tilde Q_3$, $\mathbb{C}$-linear in the first parameter and $\mathbb{C}$-**anti**-linear in the second; the family is therefore a family of $\mathbb{C}$-linear operators indexed by the pairs, and not a $\mathbb{C}$-bilinear function of the pair.

**Proof.** $W_{\tilde Q_1,\tilde Q_2}(\lambda\tilde Q_3)=\lambda W_{\tilde Q_1,\tilde Q_2}(\tilde Q_3)$ and $W_{\lambda\tilde Q_1,\tilde Q_2}=\lambda W_{\tilde Q_1,\tilde Q_2}$, while $W_{\tilde Q_1,\lambda\tilde Q_2}(\tilde Q_3)=\tilde Q_1\tilde Q_3(\lambda\tilde Q_2)^{*}=\overline{\lambda}\,W_{\tilde Q_1,\tilde Q_2}(\tilde Q_3)$. In particular $W_{i\tilde Q_1,\tilde Q_2}=-W_{\tilde Q_1,i\tilde Q_2}$, so the family does not descend to the tensor product over $\mathbb{C}$ of the two copies of $\mathbb{B}$; it descends to $\mathbb{B}\otimes_{\mathbb{C}}\overline{\mathbb{B}}$, the second factor being the conjugate algebra of §*The Enveloping Algebra*.

**Theorem (the forward law).** For all $\tilde Q_1,\tilde Q_2,\tilde{Q}_5,\tilde Q_7$,

$$
W_{\tilde Q_1,\tilde Q_2}\,W_{\tilde{Q}_5,\tilde Q_7}=W_{\tilde Q_1\tilde{Q}_5,\tilde Q_2\tilde Q_7} .
$$

**Proof.** $W_{\tilde Q_1,\tilde Q_2}W_{\tilde{Q}_5,\tilde Q_7}=T_{\tilde Q_1,\tilde Q_2^{*}}T_{\tilde{Q}_5,\tilde Q_7^{*}}=T_{\tilde Q_1\tilde{Q}_5,\tilde Q_7^{*}\tilde Q_2^{*}}=T_{\tilde Q_1\tilde{Q}_5,(\tilde Q_2\tilde Q_7)^{*}}=W_{\tilde Q_1\tilde{Q}_5,\tilde Q_2\tilde Q_7}$, by the law of §*The Composition of the Two-Sided Multiplications*.

**Remark (why the law is forward).** The involution in the second slot reverses the order once, and the composition of the plain two-sided multiplications reverses it once; the two reversals cancel. This is the operator form of the product $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ read with the conjugate in the parameter: the antilinearity of $W$ in the second parameter absorbs exactly the reversal of the composition law.

### The Sandwich Monoid

**Theorem.** The parametrisation $(\tilde Q_1,\tilde Q_2)\mapsto W_{\tilde Q_1,\tilde Q_2}$ is a homomorphism of monoids

$$
\varphi\colon \mathbb{B}\times\mathbb{B}\longrightarrow \operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad \varphi(\tilde Q_1,\tilde Q_2)=W_{\tilde Q_1,\tilde Q_2},
$$

the monoid of the source being the direct product of the multiplicative monoid $(\mathbb{B},\cdot)$ with itself, with the elementwise product and the identity $(e_t,e_t)$. Its kernel is the diagonal

$$
\ker\varphi=\{(\lambda e_t,\overline{\lambda}^{-1}e_t):\lambda\in\mathbb{C}^{\times}\}\cong\mathbb{C}^{\times},
$$

and its image is the **proper** submonoid of the **decomposable** operators, so that

$$
\varphi(\mathbb{B}\times\mathbb{B})\;\cong\;(\mathbb{B}\times\mathbb{B})/\mathbb{C}^{\times}
$$

is the monoid of the elementary tensors $\tilde Q_1\otimes\tilde Q_2^{\mathrm{opp}}$ of $\mathbb{B}^{\mathrm e}$. The whole endomorphism algebra is the **span** of the image and not the image. The group of units of the image is $(\mathbb{B}^{\times}\times\mathbb{B}^{\times})/\mathbb{C}^{\times}$, the two unit groups amalgamated along the diagonal centre.

**Proof.** That $\varphi$ is a monoid homomorphism with the elementwise product is the forward law, and $\varphi(e_t,e_t)=W_{e_t,e_t}=\mathrm{id}$. For the kernel, $W_{\tilde Q_1,\tilde Q_2}=\mathrm{id}$ means $\tilde Q_1\tilde Q_3\tilde Q_2^{*}=\tilde Q_3$ for every $\tilde Q_3$; at $\tilde Q_3=e_t$ this is $\tilde Q_1\tilde Q_2^{*}=e_t$, so that $\tilde Q_1$ and $\tilde Q_2$ are units with $\tilde Q_2^{*}=\tilde Q_1^{-1}$, and substituting this back gives $\tilde Q_1\tilde Q_3\tilde Q_1^{-1}=\tilde Q_3$ for every $\tilde Q_3$, that is, $\tilde Q_1$ is central; since the centre of $\mathbb{B}$ is $\mathbb{C}e_t$, this is $\tilde Q_1=\lambda e_t$ with a nonzero complex $\lambda$, and then $\tilde Q_2=\overline{\lambda}^{-1}e_t$. So the kernel is the set of the pairs $(\lambda e_t,\overline{\lambda}^{-1}e_t)$, the diagonal displayed. The quotient by the kernel is the image, and under the isomorphism $\mathbb{B}^{\mathrm e}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ of §*The Enveloping Algebra* the image is the set of the elementary tensors $\tilde Q_1\otimes\tilde Q_2^{\mathrm{opp}}$. It is proper: at the standard pair in the matrix model the operator
$$
D\colon\tilde Q_3\longmapsto\tilde\Pi_+\tilde Q_3\tilde\Pi_++\tilde\Pi_-\tilde Q_3\tilde\Pi_-
$$
is the sum of the two independent elementary tensors $E_{11}\otimes E_{11}^{\mathrm{opp}}+E_{22}\otimes E_{22}^{\mathrm{opp}}$, and it is not one of them. Indeed if $D(\tilde Q_3)=\tilde Q_1\tilde Q_3\tilde Q_2$ for all $\tilde Q_3$, then $D(E_{11})=E_{11}$ forces the first column of $P$ and the first row of $Q$ to be nonzero, $D(E_{12})=0$ then forces the second row of $Q$ to vanish, and $D(E_{22})=E_{22}$ forces that row to be nonzero: a contradiction. The span of the image is the whole of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, because the elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$ over the basis are a basis of $\mathbb{B}^{\mathrm e}$, which is the dimension count of §*The Enveloping Algebra*. Finally $W_{\tilde Q_1,\tilde Q_2}$ is invertible exactly when $\tilde Q_1$ and $\tilde Q_2$ are, by the criterion of *The Sesquilinear Sandwich Operator*, §*The Invertible Sandwiches*, transported to $W_{\tilde Q_1,\tilde Q_2}=S_{\tilde Q_1,\tilde Q_2^{*}}$, so the units of the image are the classes of the pairs of units, the quotient displayed.

**Remark (the same statement for the family $T$).** The two parametrisations are exchanged by the involution of the second factor, $W_{\tilde Q_1,\tilde Q_2}=T_{\tilde Q_1,\tilde Q_2^{*}}$, so the statement for $T$ is the same with the kernel $\{(\lambda e_t,\lambda^{-1}e_t)\}$, the two diagonals being exchanged by the involution of the second coordinate; the image is the same submonoid of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ and the quotient is the same monoid.

**Remark (the value at the unit).** The multiplication is the diagonal of the sandwich evaluated at the unit, $\tilde Q_1\star\tilde Q_2=W_{\tilde Q_1,\tilde Q_2}(e_t)$, and the two terms of the associator are the two ways of composing the parameters before the evaluation,

$$
(\tilde Q_1\star\tilde Q_2)\star\tilde{Q}_5=W_{\tilde Q_1\tilde Q_2^{*},\tilde{Q}_5}(e_t),\qquad
\tilde Q_1\star(\tilde Q_2\star\tilde{Q}_5)=W_{\tilde Q_1,\tilde Q_2\tilde{Q}_5^{*}}(e_t).
$$

The associator is the difference of the two values, and it does not vanish in general because the two monoid elements $(\tilde Q_1\tilde Q_2^{*},\tilde{Q}_5)$ and $(\tilde Q_1,\tilde Q_2\tilde{Q}_5^{*})$ are not equal in the quotient $(\mathbb{B}\times\mathbb{B})/\mathbb{C}^{\times}$; the monoid law itself is not violated, and the non-associativity of the multiplication is the non-equality of those two monoid elements. The associator is computed in *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*.

## The Enveloping Algebra

### The Definition

**Definition.** The **enveloping algebra** of the block over $\mathbb{C}$ is the enveloping algebra of the underlying algebra,

$$
\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}},
$$

with multiplication the tensor product of the plain multiplications, $(\tilde Q_1\otimes\tilde Q_2^{\mathrm{opp}})(\tilde{Q}_5\otimes\tilde Q_7^{\mathrm{opp}})=\tilde Q_1\tilde{Q}_5\otimes(\tilde Q_7\tilde Q_2)^{\mathrm{opp}}$, and unit $e_t\otimes e_t^{\mathrm{opp}}$. It has complex dimension $16$, and it acts on $\mathbb{B}$ by the **sandwich action**

$$
(\tilde Q_1\otimes\tilde Q_2^{\mathrm{opp}})\cdot\tilde Q_3=\tilde Q_1\tilde Q_3\tilde Q_2=T_{\tilde Q_1,\tilde Q_2}(\tilde Q_3).
$$

**Remark (why the envelope is the algebra's).** The block's multiplication is neither associative nor left-unital, so it produces no algebra structure on $\mathbb{B}$ and no envelope of its own; what it produces is the family of sandwich operators, and those operators are the elementary elements of the envelope of the underlying plain product. The block's own multiplication is recovered from the envelope together with the involution, $\star=m\circ(\mathrm{id}\otimes\eta)$, $m$ being the plain multiplication read as $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\to\mathbb{B}$, and this is stated as the comparison of §*The Comparison with the Algebra*.

### The Enveloping Algebra Is the Endomorphism Algebra

**Theorem.** The sandwich action defines an isomorphism of $\mathbb{C}$-algebras

$$
\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad \tilde Q_1\otimes\tilde Q_2^{\mathrm{opp}}\mapsto\bigl(\tilde Q_3\mapsto\tilde Q_1\tilde Q_3\tilde Q_2\bigr),
$$

so that $\mathbb{B}^{\mathrm e}\cong M_4(\mathbb{C})$ and the left action of $\mathbb{B}^{\mathrm e}$ on $\mathbb{B}$ is faithful and exhausts all $\mathbb{C}$-linear operators.

**Proof.** This is the theorem of *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*, §*The Enveloping Algebra*, whose algebra is the same $\mathbb{B}$ with the same plain product; the proof there runs on the matrix units of $\mathbb{B}\cong M_2(\mathbb{C})$ and applies here without change. In particular the two-sided multiplications $T_{\tilde Q_1,\tilde Q_2}$ are the elementary tensors, and they span the whole endomorphism algebra, which is the spanning statement used in §*The Sandwich Monoid*.

### The Block's Operators in the Envelope

**Corollary (the block's operator content).** The block's own operators are the elements of the envelope twisted by the involution:

$$
R_{\tilde Q_6}=\varphi\bigl(e_t\otimes(\tilde Q_6^{*})^{\mathrm{opp}}\bigr),\qquad
\Theta_{\tilde Q_2}=\varphi\bigl(\tilde Q_2\otimes(\tilde Q_2^{*})^{\mathrm{opp}}\bigr),\qquad
L_{\tilde Q_6}=\varphi\bigl(\tilde Q_6\otimes e_t^{\mathrm{opp}}\bigr)\circ\eta ,
$$

where $\varphi(\tilde Q_1\otimes\tilde Q_2^{\mathrm{opp}})$ is the sandwich action of $\tilde Q_1\otimes\tilde Q_2^{\mathrm{opp}}$.

**Proof.** $\varphi(e_t\otimes(\tilde Q_6^{*})^{\mathrm{opp}})(\tilde Q_3)=e_t\tilde Q_3\tilde Q_6^{*}=\tilde Q_3\tilde Q_6^{*}=R_{\tilde Q_6}(\tilde Q_3)$, so the right multiplications are the envelope's right-sided elements with the conjugated parameter. The two-sided operator $\Theta_{\tilde Q_2}(\tilde Q_3)=\tilde Q_2\tilde Q_3\tilde Q_2^{\dagger}=\tilde Q_2\tilde Q_3\tilde Q_2^{*}$ is $\varphi(\tilde Q_2\otimes(\tilde Q_2^{*})^{\mathrm{opp}})$, the elementary tensor whose two parameters are conjugate. Finally $\varphi(\tilde Q_6\otimes e_t^{\mathrm{opp}})(\tilde Q_3)=\tilde Q_6\tilde Q_3$, so $L_{\tilde Q_6}(\tilde Q_3)=\tilde Q_6\tilde Q_3^{*}=(\varphi(\tilde Q_6\otimes e_t^{\mathrm{opp}})\circ\eta)(\tilde Q_3)$.

**Remark (the pair generation).** The corollary explains the block's composition laws. The product of two right multiplications stays among the envelope's right-sided elements, $R_{\tilde Q_6}R_{\tilde Q_4}=\varphi(e_t\otimes(\tilde Q_4^{*}\tilde Q_6^{*})^{\mathrm{opp}})=R_{\tilde Q_6\tilde Q_4}$; the product of two left multiplications leaves the conjugate-linear operators and is the elementary tensor $L_{\tilde Q_6}L_{\tilde Q_4}=T_{\tilde Q_6,\tilde Q_4^{*}}$, that is $\varphi(\tilde Q_6\otimes\tilde Q_4^{\mathrm{opp}})$ read with the conjugated parameter; and a mixed product is a left multiplication or a sandwich according to the order. So the even products of the block's own one-sided multiplications span the envelope, and a single one-sided multiplication never lies in it: a single one is not $\mathbb{C}$-linear, and the pairs are. In the notation of §*The Conjugate-Indexed Family and the Sandwich Monoid*, $L_{\tilde Q_6}L_{\tilde Q_4}=W_{\tilde Q_6,\tilde Q_4}$, $R_{\tilde Q_6}=W_{e_t,\tilde Q_6}$ and $L_{\tilde Q_6}=W_{\tilde Q_6,e_t}\circ\eta$.

### The Base Field and the Real Dimension Count

**Remark (over $\mathbb{R}$ the action is not faithful).** Regard $\mathbb{B}$ as a real algebra, $\dim_{\mathbb{R}}\mathbb{B}=8$, so that $\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B}^{\mathrm{opp}}$ has real dimension $64$, the same as $\operatorname{End}_{\mathbb{R}}(\mathbb{B})$. The sandwich map is then **not** injective: the element $i e_t\otimes e_t^{\mathrm{opp}}-e_t\otimes(i e_t)^{\mathrm{opp}}$ acts as $\tilde Q_3\mapsto i\tilde Q_3-\tilde Q_3 i=0$, because $i$ is central, and the image is only the space of $\mathbb{C}$-linear operators, of real dimension $32$, so the kernel has real dimension $32$. The complex base field removes exactly this redundancy, which is why the theorem above is stated over $\mathbb{C}$; the computation is the one of *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*, §*The Base Field and the Real Dimension Count*, and the block inherits it unchanged.

### The Comparison with the Algebra

**Remark (the conjugate-indexed prescription and the conjugate algebra).** The block's parametrisation $(\tilde Q_1,\tilde Q_2)\mapsto W_{\tilde Q_1,\tilde Q_2}$ is $\mathbb{C}$-antilinear in the second coordinate (§*The Conjugate-Indexed Family and the Sandwich Monoid*, Proposition), so it is not the elementary-tensor map of the envelope. It becomes one after the substitution $\tilde Q_2\mapsto\tilde Q_2^{*}$, which is the identification of $\mathbb{B}$ with its conjugate algebra $\overline{\mathbb{B}}$: the assignment

$$
\tilde Q_1\otimes\overline{\tilde Q}_2\longmapsto W_{\tilde Q_1,\tilde Q_2}=\bigl(\tilde Q_3\mapsto\tilde Q_1\tilde Q_3\tilde Q_2^{*}\bigr)
$$

is an isomorphism of $\mathbb{C}$-algebras $\mathbb{B}\otimes_{\mathbb{C}}\overline{\mathbb{B}}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, and $\overline{\mathbb{B}}\to\mathbb{B}^{\mathrm{opp}}$, $\tilde Q_2\mapsto\tilde Q_2^{*}$, is an isomorphism of $\mathbb{C}$-algebras. So the block's envelope is the algebra's with the second factor conjugated, and the passage from one presentation to the other is the involution.

**Remark (what the block adds and what it does not).** The block adds **nothing to the algebra of the envelope**: $\mathbb{B}^{\mathrm e}$ is the underlying algebra's, and the block's product is not a new multiplication on it but the derived product $m\circ(\mathrm{id}\otimes\eta)$. What the block adds is the **reading**: its one-sided multiplications are the envelope's one-sided elements twisted by the involution, its product is the diagonal of the sandwich monoid, and its bi-module of §*The Bi-module Structure* is the algebra's bimodule with the involution inserted. In the language of §*The Envelope as a Luxury of the Associative Unital Case* of the twin, the block inherits the envelope exactly because the sandwich uses the associative unital **plain** product, and what it does not inherit is the multiplicativity of its own regular maps, $\tilde Q_6\mapsto L_{\tilde Q_6}$ not being multiplicative and $\tilde Q_6\mapsto R_{\tilde Q_6}$ being multiplicative only in the plain parameter. The block's envelope is therefore a genuine instance and not a new structure, and the article's content is the reading rather than the algebra.

### The Peirce Decomposition of the Enveloping Algebra

The Peirce decomposition of the block of *Ideals and Peirce Decomposition of the General Plain Sesqualgebra* tensors to a decomposition of $\mathbb{B}^{\mathrm e}$, exactly as in the algebra's case. The four elements

$$
E_{ik}=\tilde\Pi_i\otimes\tilde\Pi_k^{\mathrm{opp}},\qquad i,k\in\{+,-\},
$$

are idempotent and pairwise orthogonal, $E_{ik}E_{jl}=\delta_{ij}\delta_{kl}E_{ik}$, and they sum to the unit $e_t\otimes e_t^{\mathrm{opp}}=\sum_{ik}E_{ik}$; they are primitive, each corner $E_{ik}\mathbb{B}^{\mathrm e}E_{ik}$ being the one-dimensional line $\mathbb{C}(\tilde\Pi_i\otimes\tilde\Pi_k^{\mathrm{opp}})$.

**Proposition (the sixteen corners).** The Peirce decomposition of $\mathbb{B}^{\mathrm e}$ with respect to the family $E_{ik}$ has sixteen one-dimensional corners

$$
E_{ik}\,\mathbb{B}^{\mathrm e}\,E_{jl}=\bigl(\tilde\Pi_i\mathbb{B}\tilde\Pi_j\bigr)\otimes\bigl(\tilde\Pi_l\mathbb{B}\tilde\Pi_k\bigr)^{\mathrm{opp}}=\mathbb{C}\bigl(\Lambda_{ij}\otimes\Lambda_{lk}^{\mathrm{opp}}\bigr),
$$

where $\Lambda_{ij}$ generates the block's corner $\tilde\Pi_i\mathbb{B}\tilde\Pi_j$ — that is $\tilde\Pi,\vec\Upsilon_x,\vec\Upsilon_y,\tilde\Pi^{\perp}$ for $(i,j)=(+,+),(+,-),(-,+),(-,-)$ — and the corners multiply by

$$
\bigl(E_{ik}\mathbb{B}^{\mathrm e}E_{jl}\bigr)\bigl(E_{i'k'}\mathbb{B}^{\mathrm e}E_{j'l'}\bigr)\subseteq\delta_{ji'}\delta_{lk'}\,E_{ik}\mathbb{B}^{\mathrm e}E_{j'l'} .
$$

**Proof.** The corner is $(\tilde\Pi_i\otimes\tilde\Pi_k^{\mathrm{opp}})(\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}})(\tilde\Pi_j\otimes\tilde\Pi_l^{\mathrm{opp}})=(\tilde\Pi_i\mathbb{B}\tilde\Pi_j)\otimes(\tilde\Pi_l\mathbb{B}\tilde\Pi_k)^{\mathrm{opp}}$, the reversal of the second index pair being the reversal of the multiplication in the second factor; each factor is one-dimensional by *Ideals and Peirce Decomposition of the General Plain Sesqualgebra*, §*The Biquaternion Cases*, and the product rule is the algebra table applied in each factor, with the second factor read in the reversed order.

**Remark (the second Peirce index is reversed).** The corner basis element is $\Lambda_{ij}\otimes\Lambda_{lk}^{\mathrm{opp}}$, with the second index pair reversed, and the transposed shape is not an artefact of the writing: it is the reversal of §*The Composition of the Two-Sided Multiplications*, the same reversal as in the composition of the elementary tensors, and it is the reason the second factor is written with an $\mathrm{op}$. The block's own multiplication then reads the corners with the **transposed** index rule of *Ideals and Peirce Decomposition of the General Plain Sesqualgebra*, §*The Two Tables*; the envelope's reversal and the multiplication's transposition are the two faces of the same involution.

**Remark (the action of the four idempotents).** Under the sandwich action the four idempotents cut the block itself:

$$
E_{ik}\cdot\tilde Q_3=(\tilde\Pi_i\otimes\tilde\Pi_k^{\mathrm{opp}})\cdot\tilde Q_3=\tilde\Pi_i\tilde Q_3\tilde\Pi_k ,
$$

which is the Peirce projection onto the corner $\tilde\Pi_i\mathbb{B}\tilde\Pi_k$ of the block. Since the four idempotents are complete and orthogonal, the left $\mathbb{B}^{\mathrm e}$-module ${}_{\mathbb{B}^{\mathrm e}}\mathbb{B}$ splits as the direct sum of the four complex lines $\tilde\Pi_i\mathbb{B}\tilde\Pi_k$: the Peirce decomposition of the block is the decomposition of $\mathbb{B}$ as a module over its enveloping algebra, and the identity operator is $\sum_{ik}E_{ik}=e_t\otimes e_t^{\mathrm{opp}}$. This is the module form of *Ideals and Peirce Decomposition of the General Plain Sesqualgebra*.

**Remark (where the family comes from).** The complementary pair $(\tilde\Pi,\tilde\Pi^{\perp})$ that indexes the four idempotents is a pair of **orthogonal** right $\star$-ideals of the block, and it is one pair out of the projective line of them: by *Ideals and Peirce Decomposition of the General Plain Sesqualgebra*, §*The Complementary Pairs and the Peirce Decompositions*, every unordered pair of distinct right ideals carries a complete family $\tilde\Pi,e_t-\tilde\Pi$ and a Peirce decomposition, and the orthogonal pairs are exactly the ones whose idempotents are Hermitian, that is, the pairs of projections used here. The four idempotents of the envelope, the corners of the block and the $2\times2$ matrix realizations of the same section are three readings of the one right-ideal lattice.

## The Bi-module Structure

### The Definition and the Twisted Actions

**Definition.** A $\mathbb{B}$-$\mathbb{B}$**-bi-module** is a complex vector space $M$ with a left and a right $\mathbb{B}$-action that commute, $(\tilde Q_1\cdot m)\cdot\tilde Q_2=\tilde Q_1\cdot(m\cdot\tilde Q_2)$. The block with the **plain** actions,

$$
\tilde Q_1\cdot\tilde Q_3=\tilde Q_1\tilde Q_3,\qquad \tilde Q_3\cdot\tilde Q_2=\tilde Q_3\tilde Q_2 ,
$$

is the algebra's regular bi-module, and it is the left regular module of the enveloping algebra by $(\tilde Q_1\otimes\tilde Q_2^{\mathrm{opp}})\cdot\tilde Q_3=\tilde Q_1\tilde Q_3\tilde Q_2$. With the **twisted** actions of the block,

$$
\tilde Q_1\cdot\tilde Q_3=\tilde Q_1\star\tilde Q_3=L_{\tilde Q_1}(\tilde Q_3),\qquad \tilde Q_3\cdot\tilde Q_2=\tilde Q_3\star\tilde Q_2=R_{\tilde Q_2}(\tilde Q_3),
$$

the same space carries the two one-sided families of the multiplication.

**Proposition (the twist).** On the regular bi-module the twisted actions are the plain actions composed with the involution in one slot,

$$
L_{\tilde Q_1}(\tilde Q_3)=\bigl((\tilde Q_1\cdot{})\circ\eta\bigr)(\tilde Q_3),\qquad
R_{\tilde Q_2}(\tilde Q_3)=\bigl(({}\cdot\tilde Q_2^{*})\bigr)(\tilde Q_3),
$$

and the twisted actions **do not commute**: $L_{\tilde Q_6}R_{\tilde Q_4}=L_{\tilde Q_6\tilde Q_4}$ while $R_{\tilde Q_4}L_{\tilde Q_6}=S_{\tilde Q_6,\tilde Q_4}$, and the two differ in general, the witness being $\tilde Q_6=\vec e_x,\tilde Q_4=\vec e_y,\tilde Q_3=e_t$, where $L_{\vec e_x}R_{\vec e_y}(e_t)=\vec e_z$ and $R_{\vec e_y}L_{\vec e_x}(e_t)=-\vec e_z$.

**Proof.** The first display is the definition, $L_{\tilde Q_1}(\tilde Q_3)=\tilde Q_1\tilde Q_3^{*}$ and $R_{\tilde Q_2}(\tilde Q_3)=\tilde Q_3\tilde Q_2^{*}$. The composition laws are those of *The Left and Right Multiplications of the Biquaternioid Sesqualgebra*, §*The Mixed Composites*: $L_{\tilde Q_6}R_{\tilde Q_4}(\tilde Q_3)=\tilde Q_6(\tilde Q_3\tilde Q_4^{*})^{*}=\tilde Q_6\tilde Q_4\tilde Q_3^{*}=L_{\tilde Q_6\tilde Q_4}(\tilde Q_3)$ and $R_{\tilde Q_4}L_{\tilde Q_6}(\tilde Q_3)=(\tilde Q_6\tilde Q_3^{*})\tilde Q_4^{*}=\tilde Q_6\tilde Q_3^{*}\tilde Q_4^{*}=S_{\tilde Q_6,\tilde Q_4}(\tilde Q_3)$; the value at $\tilde Q_6=\vec e_x,\tilde Q_4=\vec e_y,\tilde Q_3=e_t$ is $\vec e_x\vec e_y=\vec e_z$ against $\vec e_xe_t^{*}\vec e_y^{*}=\vec e_x\cdot e_t\cdot(-\vec e_y)=-\vec e_z$, the witness recorded in that article.

**Remark (what the failure costs).** The plain actions commute and make $\mathbb{B}$ a bi-module; the twisted actions do not, so the multiplication alone does not give a bi-module structure on the block. The failure is the non-associativity of the multiplication, and it is measured by the difference between the left multiplication $L_{\tilde Q_6\tilde Q_4}$ and the sandwich $S_{\tilde Q_6,\tilde Q_4}$ of the mixed composites. The block therefore has a bi-module structure only through its enveloping algebra: $\mathbb{B}$ is the left regular module of $\mathbb{B}^{\mathrm e}$, the multiplication is the diagonal of the envelope read at the unit, and the two twisted actions are the plain ones read through the derived product $m\circ(\mathrm{id}\otimes\eta)$, so the loss of commutativity is the price of the derivation.

### The Two-Sided Operators and the Diagonal

**Corollary.** The two-sided operators of the block are the diagonal of the sandwich family, $\Theta_{\tilde Q_2}=W_{\tilde Q_2,\tilde Q_2}=\varphi(\tilde Q_2\otimes(\tilde Q_2^{*})^{\mathrm{opp}})$, that is the subfamily in which the two parameters are conjugate.

**Proof.** $\Theta_{\tilde Q_2}(\tilde Q_3)=\tilde Q_2\tilde Q_3\tilde Q_2^{*}=W_{\tilde Q_2,\tilde Q_2}(\tilde Q_3)$.

### The Left-versus-Right Question

The algebra records a question of which of the two regular actions carries a given physical degree of freedom, and answers the algebraic half of it by exhibiting the pair inside one commutative envelope. The block answers it differently.

**What the block says.** The two one-sided families of the block are **not** of the same algebraic type: the left multiplications are conjugate-linear and the right ones are linear, and a single one of either kind is not an element of the enveloping algebra but at best an element composed with the involution (§*The Enveloping Algebra*, Corollary). The pair is therefore not a pair of commuting copies inside the envelope; the two families do not even commute (§*The Twisted Actions*), and the honest commuting pair inside the envelope is the **plain** left and right multiplications, which is the algebra's.

**The precise form of the question for the block.** A construction covariant under the block and multiplying the unknown on both sides uses the twisted actions, hence the sandwich parameters rather than the factor parameters; the question of which face of the block carries which physical degree of freedom is then the question of which sandwich parameter is the left one, a question that the algebra alone can only relocate into the envelope, where the two factors are the same algebra $\mathbb{B}$ up to the involution and the involution is the only thing that distinguishes them.

## Worked Verification

The claims of the article were recomputed on the model $\mathsf{M}_2$ at no more than one hundred samples per claim.

- **The composition laws.** The laws $T_{\tilde Q_1,\tilde Q_2}T_{\tilde{Q}_5,\tilde Q_7}=T_{\tilde Q_1\tilde{Q}_5,\tilde Q_7\tilde Q_2}$, $W_{\tilde Q_1,\tilde Q_2}W_{\tilde{Q}_5,\tilde Q_7}=W_{\tilde Q_1\tilde{Q}_5,\tilde Q_2\tilde Q_7}$, $S_{\tilde Q_1,\tilde Q_2}S_{\tilde{Q}_5,\tilde Q_7}=T_{\tilde Q_1\tilde Q_7,(\tilde Q_2\tilde{Q}_5)^{*}}$ and the four laws of *The Left and Right Multiplications of the Biquaternioid Sesqualgebra* were verified with residual at most $2\cdot10^{-13}$ on a hundred quadruples each.
- **The monoid kernel.** The scaling $(\tilde Q_1,\tilde Q_2)\mapsto(\lambda\tilde Q_1,\overline{\lambda}^{-1}\tilde Q_2)$ leaves $W_{\tilde Q_1,\tilde Q_2}$ unchanged on a hundred random pairs and scalars, with residual at most $5\cdot10^{-16}$, and the operator is the identity exactly on that set, as the theorem states.
- **The span.** The complex span of the sixteen operators $T_{e_\mu,e_\nu}$ over the basis is all of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen, and the real span of the sandwich operators over the real basis is thirty-two.
- **The properness of the image.** The operator $D(\tilde Q_3)=E_{11}\tilde Q_3E_{11}+E_{22}\tilde Q_3E_{22}$ has coefficient matrix $\operatorname{diag}(1,0,0,1)$ of rank two in the tensor basis $E_{ij}\otimes E_{kl}^{\mathrm{opp}}$, so it is not an elementary tensor; and the equations of the proof were checked on the matrix units, where $PE_{11}Q=E_{11}$ forces the first column of $P$ and the first row of $Q$ nonzero, $PE_{12}Q=0$ then forces the second row of $Q$ to vanish, and $PE_{22}Q=E_{22}$ forces it not to.
- **The envelope axioms.** The sandwich action is a left action (residual zero on a hundred triples), the unit acts as the identity, the map $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is multiplicative, and the identity operator is $T_{e_t,e_t}$.
- **The block's operators in the envelope.** The identities $R_{\tilde Q_6}=W_{e_t,\tilde Q_6}$, $\Theta_{\tilde Q_2}=W_{\tilde Q_2,\tilde Q_2}$, $L_{\tilde Q_6}=W_{\tilde Q_6,e_t}\circ\eta$, $L_{\tilde Q_6}L_{\tilde Q_4}=W_{\tilde Q_6,\tilde Q_4}$ and the witness $L_{\vec e_x}R_{\vec e_y}(e_t)=\vec e_z$, $R_{\vec e_y}L_{\vec e_x}(e_t)=-\vec e_z$ were each verified with residual zero.

## Summary

The block's one-sided multiplications are of opposite $\mathbb{C}$-parity, and a single one lies outside the $\mathbb{C}$-linear operators, but the product of two lies inside: $L_{\tilde Q_6}L_{\tilde Q_4}=T_{\tilde Q_6,\tilde Q_4^{*}}$, and the products of the block's own one-sided multiplications fill the enveloping algebra of the underlying plain product.

The parametrisation $(\tilde Q_1,\tilde Q_2)\mapsto W_{\tilde Q_1,\tilde Q_2}$, $W_{\tilde Q_1,\tilde Q_2}(\tilde Q_3)=\tilde Q_1\tilde Q_3\tilde Q_2^{*}$, is a homomorphism of monoids from the direct product $\mathbb{B}\times\mathbb{B}$ with kernel the diagonal $\mathbb{C}^{\times}$, and its image is the monoid $(\mathbb{B}\times\mathbb{B})/\mathbb{C}^{\times}$ of the decomposable operators, a proper submonoid of the endomorphism monoid whose span is the whole endomorphism algebra; the block's product is the value of the sandwich at the unit, $\tilde Q_1\star\tilde Q_2=W_{\tilde Q_1,\tilde Q_2}(e_t)$. The parametrisation is $\mathbb{C}$-linear in the first parameter and conjugate-linear in the second, so its envelope is $\mathbb{B}\otimes_{\mathbb{C}}\overline{\mathbb{B}}$, the second factor conjugated and isomorphic to $\mathbb{B}^{\mathrm{opp}}$.

The enveloping algebra is $\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$ with the sandwich action, $\mathbb{B}^{\mathrm e}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$, and it is the algebra's; the block's right multiplications and two-sided operators are its elements with the conjugated parameter, its left multiplications its elements composed with the involution, and its product is the derived product $m\circ(\mathrm{id}\otimes\eta)$. The block is the left regular module of the envelope, and its Peirce decomposition is the module decomposition along the four idempotents $\tilde\Pi_i\otimes\tilde\Pi_k^{\mathrm{opp}}$, whose corner basis is $\Lambda_{ij}\otimes\Lambda_{lk}^{\mathrm{opp}}$ with the second index pair reversed. The plain actions make $\mathbb{B}$ a bi-module and commute; the block's twisted actions do not commute, and the failure is the non-associativity of the multiplication.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ | the general plain sesquilinear product, the multiplication of the block |
| $\eta(\tilde Q_3)=\tilde Q_3^{*}$ | the involution as an operator |
| $L_{\tilde Q_6},R_{\tilde Q_6}$ | the block's one-sided multiplications, conjugate-linear and linear |
| $T_{\tilde Q_1,\tilde Q_2}(\tilde Q_3)=\tilde Q_1\tilde Q_3\tilde Q_2$ | the ordinary two-sided multiplication, $\mathbb{C}$-linear |
| $S_{\tilde Q_1,\tilde Q_2}(\tilde Q_3)=\tilde Q_1\tilde Q_3^{*}\tilde Q_2^{*}$ | the sandwich, $\mathbb{C}$-conjugate-linear |
| $W_{\tilde Q_1,\tilde Q_2}=T_{\tilde Q_1,\tilde Q_2^{*}}$ | the conjugate-indexed family, the block's own sandwich |
| $\Theta_{\tilde Q_2}=W_{\tilde Q_2,\tilde Q_2}$ | the two-sided operator $\tilde Q_2\tilde Q_3\tilde Q_2^{\dagger}$, the diagonal |
| $\mathbb{B}^{\mathrm e}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$ | the enveloping algebra of the block, with the sandwich action |
| $\overline{\mathbb{B}}$ | the conjugate algebra, $\overline{\mathbb{B}}\cong\mathbb{B}^{\mathrm{opp}}$ by $\tilde Q_2\mapsto\tilde Q_2^{*}$ |
| $E_{ik}=\tilde\Pi_i\otimes\tilde\Pi_k^{\mathrm{opp}}$ | the four idempotents of the envelope's Peirce family |
| $\Lambda_{ij}$ | the generator of the Peirce corner $\tilde\Pi_i\mathbb{B}\tilde\Pi_j$ |

## Further Reading

- *The Left and Right Multiplications of the Biquaternioid Sesqualgebra* — the parities, the composition laws and the four families.
- *The Sesquilinear Sandwich on the Biquaternioid* — the sandwich $S_{\tilde Q_1,\tilde Q_2}$ and its composition table.
- *One-Sided Operators on the General Plain Sesqualgebra* — the block's one-sided operators and the double centraliser.
- *Two-Sided Operators on the General Plain Sesqualgebra* — the two-sided operator $\Theta_{\tilde Q_2}$ and its square law.
- *The Left and Right Multiplication Operators of a Sesqualgebra* — the general operator theory of a sesqualgebra.
- *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure* — the twin, with the algebra's envelope, its Peirce decomposition and the bi-module.
- *Ideals and Peirce Decomposition of the General Plain Sesqualgebra* — the four Peirce lines of the block that the envelope cuts out.
- *Square Roots of One and the Idempotents of the General Plain Sesqualgebra* — the projections that index the Peirce family.
- *The Ternary Product and the Associator of the Biquaternion Sesqualgebra* — the associator whose two terms are the two values of the sandwich monoid.
