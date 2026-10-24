
# __Introduction to the Operators of the Biquaternion Algebra__

## Introduction

The four general products of $\mathbb{B}$ are four rules that pair two elements, and the corpus gives each of them an operator family: the plain bilinear product the *Association* family, the general plain sesquilinear product the *Hermitian Adjoint* family, the general quaternionic bilinear product the *Signed Inner Conjugation* family, and the general quaternionic sesquilinear product the Krein form, which carries its own indefinite theory rather than a family of the four-adjoint kind. A reader may conclude from that list that the product *decides* the operator, and may then ask whether the product decides whether an element acts as a rotation or as a reflection. **It does not.** The four general products have the same multiplication table of the units; they differ only in which conjugation is inserted into which slot of the pair. What they decide is the *pairing*, hence the adjoint, hence the name of the family. The action — a rotation, a reflection, an inner automorphism — is decided by the element and by the inserted sign, and the inserted sign is a choice among the involutions that the algebra already carries.

This article states that division of labour precisely, with the matrices of one element read through all four insertions. It opens the group *Operators* and carries the passage from a product to an operator.

The answer to the question of the title is therefore a negative one, and it agrees with the intuition that the algebra and its product come first and the operator is obtained from them by choosing the element and the insertion. The qualification is that the choice is not arbitrary: on the vector subspace the plain product cannot produce a reflection, only its negative, so that one insertion is *forced* by the algebra and not merely preferred.

The four general products, their relations and their comparison are *The Four General Products and Their Relations*; the four pairings and their Gram matrices are *The Four Forms and the Four Algebraic Norms*; the four adjoints and the reading of the family names are *The Four Adjoints of the Biquaternion Algebra in Examples*; the conjugations and their group are *The Group of Involutions*; the signed sandwich and its reflection formula are *The Signed Sandwich on a Clifford Algebra* and *Two-Sided Operators with the Signed Product*. The article is pure algebra. The two insertions are also the subject of a group: each is an involution, they commute, and the four readings of a rule form the group $\mathbb{Z}_2\times\mathbb{Z}_2$. Read on a general algebra with two commuting anti-involutions, the same construction gives the slot family, whose second slot governs the composition and whose first slot governs the form, and the table of the slots records the four settings. That is §*The Four Readings and Their Group*.

## The Four General Products Are One Multiplication with Two Insertions

### The Four Rules

**Definition (the four general products).** The four general products are

$$
\tilde Q_1\tilde Q_2 ,
\qquad
\tilde Q_1\tilde Q_2^{*} ,
\qquad
\tilde Q_1^{\natural}\tilde Q_2 ,
\qquad
\tilde Q_1^{\natural}\tilde Q_2^{*} ,
$$

the plain bilinear, the general plain sesquilinear, the general quaternionic bilinear and the general quaternionic sesquilinear product.

**Proposition (one table, two insertions).** The four rules multiply the coordinates on the same products $e_\mu e_\nu$ of the basis. They differ in one point alone: whether the coordinates of each of the two elements are used as they stand or taken from the conjugated element, the two elements being treated independently of one another. Equivalently, the four general products are the four members of the orbit

$$
\bigl\{K_1(\tilde Q_1)\,K_2(\tilde Q_2)\;:\;K_1\in\{\mathrm{id},{}^{\natural}\},\;K_2\in\{\mathrm{id},{}^{*}\}\bigr\}
$$

of a single rule under the insertion of a conjugation into the first slot and a conjugation into the second.

*Proof.* Reading the four definitions side by side, the products $e_\mu e_\nu$ of the basis and the order of the factors are the same in all four; the only difference is the source of $Q_{1,\mu}$ in the first factor and of $Q_{2,\nu}$ in the second.

**Remark (why "complex products").** The word *complex* records the base field and not a second multiplication: the multiplication of the units is that of $\mathbb{H}$ extended to $\mathbb{C}$, and the four rules move over it. There is no product among the four that is not the plain one with an insertion.

### One Multiplication Table, Four Pairings

**Theorem (the scalar parts are the four pairings).** The scalar parts of the four general products are the four pairings of the algebra,

$$
\boxed{\;
\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2),\quad
\langle\tilde Q_1,\tilde Q_2\rangle_{\ast}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*}),\quad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2),\quad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural\ast}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})
\;},
$$

with Gram matrices in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ equal to $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$, $\mathrm{I}_4$, $\mathrm{I}_4$ and $\mathrm{E}$.

*Proof.* $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ with $\varepsilon=(1,-1,-1,-1)$, and on the basis units the two insertions act by $e_\mu^{\natural}=\varepsilon_\mu e_\mu$ and $e_\mu^{*}=\varepsilon_\mu e_\mu$, the coordinates of the units being real, so that the sign $\varepsilon_\mu$ cancels as soon as the unit is read through one of the two insertions. The Gram matrix is therefore $\varepsilon$ exactly when the two insertions agree, that is for the plain product and for the general quaternionic sesquilinear one, and $1$ when they differ, that is $\mathrm{E},\mathrm{I}_4,\mathrm{I}_4,\mathrm{E}$. The four pairings are distinct as maps — two are bilinear and two sesquilinear in the second argument, and no two agree on complex coefficients — while two pairs of them share a Gram matrix, a Gram matrix seeing the basis units alone, on which the conjugations act by a sign.

**Corollary (a product is a pairing, not an operator).** The four general products endow $\mathbb{B}$ with the four pairings and nothing else. Each of them is a bilinear or a sesquilinear *form*, and a form does not act on the algebra; it pairs two of its elements. Whatever acts is a map, and a map has to be built.

## The Four Readings and Their Group

The four general products are four rules on one and the same space, and each of the three others is, as *The Four General Products and Their Relations*, §*Which of the Four Is a Multiplication*, reads it, the general plain bilinear product with a conjugation inserted in a slot. **The four insertions that appear there are the four elements of a group.** One insertion reads the first argument through the natural conjugation and one reads the second through the Hermitian conjugation; each of the two is its own inverse, the two commute, and the four are these two insertions, their composite and the identity. The group is of order four and elementary abelian, and the four general products are its four elements read on one and the same rule. **Each of the two generators touches one slot**, and it is that reading which decides which property of the four general products belongs to which slot: the group is read on the rules above, the same operation is read on a general algebra with its two anti-involutions in §*The Operation on a General Algebra*, the settings are collected in §*The Table of the Slots*, and the one setting whose square is central is §*The Square at One Setting*.

### The Readings and Their Group

**Definition (the two insertions and the four readings).** Let $f$ be a rule of two arguments on $\mathbb{B}$. The **first insertion** and the **second insertion** carry $f$ to the rules

$$
(\tilde Q_1,\tilde Q_2)\longmapsto f(\tilde Q_1^{\natural},\tilde Q_2),
\qquad
(\tilde Q_1,\tilde Q_2)\longmapsto f(\tilde Q_1,\tilde Q_2^{*}).
$$

The **four readings** of $f$ are $f$ itself, its image under the first insertion, its image under the second insertion, and its image under the composite of the two. Following the convention of *Introduction to the Operators of the Biquaternion Algebra*, the readings are written (none), (${}^{\natural}$), (${}^{*}$) and (both), the label naming the insertions made: none, the first insertion, the second insertion, or both.

**Remark (why four readings and not sixteen).** The involutions at hand are four — $\mathrm{id}$, ${}^{\natural}$, the coefficient conjugation $\bar{\cdot}$ and the Hermitian conjugation ${}^{*}$ — so insertions built from all four would a priori give sixteen readings. The four general products use only $\mathrm{id}$ or ${}^{\natural}$ in the first slot and only $\mathrm{id}$ or ${}^{*}$ in the second, and two features of that choice matter in this part. The first slot is $\mathbb{C}$-linear and never conjugates the coefficients, while the second is conjugate-linear whenever it is not the identity; that asymmetry is why the two slots are not interchangeable, and it is the source of every entry of §*The Table of the Slots*. And the two conjugations chosen are the ones that produce the split read in *The Four General Products and Their Relations*, §*Which of the Four Is a Multiplication*, in which the second slot alone decides whether the product is the multiplication of an algebra over $\mathbb{C}$. The part asserts nothing about the other readings, and every statement in it is about the four.

**Theorem (the four readings form a group).** The four readings of any rule are closed under composition, and they form a group isomorphic to $\mathbb{Z}_2\times\mathbb{Z}_2$, of which (none) is the identity and of which the first insertion and the second insertion are two generators.

*Proof.* The first insertion applied twice returns the rule, since $\tilde Q_1^{\natural\natural}=\tilde Q_1$ and ${}^{\natural}$ is an involution, and the second insertion applied twice returns it for the same reason, ${}^{*}$ being an involution. Each of the two insertions is therefore its own inverse, and so is each of the four readings. The first insertion touches the first argument alone and the second the second argument alone, so the two commute, and their composite is the reading (both). The four readings are closed, every element is its own inverse, and the group is abelian of order four with exponent two, that is $\mathbb{Z}_2\times\mathbb{Z}_2$. The product is the table, in which the row is the first factor and the column the second.

| $\circ$ | (none) | (${}^{\natural}$) | (${}^{*}$) | (both) |
|---|---|---|---|---|
| (none) | (none) | (${}^{\natural}$) | (${}^{*}$) | (both) |
| (${}^{\natural}$) | (${}^{\natural}$) | (none) | (both) | (${}^{*}$) |
| (${}^{*}$) | (${}^{*}$) | (both) | (none) | (${}^{\natural}$) |
| (both) | (both) | (${}^{*}$) | (${}^{\natural}$) | (none) |

**Theorem (the four general products are one rule and its three readings).** Read on the general plain bilinear product, the four readings give the four general products,

$$
\boxed{\;
\tilde Q_1\tilde Q_2,
\qquad
\tilde Q_1^{\natural}\tilde Q_2,
\qquad
\tilde Q_1\tilde Q_2^{*},
\qquad
\tilde Q_1^{\natural}\tilde Q_2^{*}
\;},
$$

in the order (none), (${}^{\natural}$), (${}^{*}$), (both). The four are pairwise distinct, so the group permutes them faithfully and the orbit of the general plain bilinear product is the four. **The four general products are therefore one rule and the three modifications of it, a modification being one insertion.**

*Proof.* The three non-identity readings applied to the general plain bilinear product are the three formulas of *The Four General Products and Their Relations*, §*Which of the Four Is a Multiplication*: the first insertion gives $\natural(\tilde Q_1)\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$, the second gives $\tilde Q_1\,\natural(\bar{\tilde Q}_2)=\tilde Q_1\tilde Q_2^{*}$, and the composite gives $\natural(\tilde Q_1)\natural(\bar{\tilde Q}_2)=\tilde Q_1^{\natural}\tilde Q_2^{*}$. The four are pairwise distinct, by *The Four General Products and Their Relations*, and each non-identity reading moves the general plain bilinear product, since it changes the first element, the second, or both; the orbit is therefore the four general products and the action is faithful.

**Corollary (the group is the two slots).** Each generator touches one slot alone, so a property that depends on one slot alone is carried by one generator, a property that depends on both requires the two, and a property that sees neither is carried by the whole group. **The two generators of the group are the two slots**, and the property table above reads row by row along them: §*The Table of the Slots* gives the rule that places each row.

**Corollary (the same group on the pairings and on the Gram matrices).** Read on the scalar part of a rule, the four readings give the four pairings, whose Gram matrices in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ are $\mathrm{E},\mathrm{I}_4,\mathrm{I}_4,\mathrm{E}$ in the order (none), (${}^{\natural}$), (${}^{*}$), (both). The coefficient $\varepsilon=(1,-1,-1,-1)$ survives therefore for exactly the two readings in which the two insertions agree, (none), where neither is applied, and (both), where both are, and it is replaced by $1$ for the two in which they differ; that alternation is the sign matrix $\mathrm{E}$ against the identity $\mathrm{I}_4$ of *The Four Forms and the Four Algebraic Norms*.

**Remark (the group of the operations is not the group of the involutions).** The four readings are operations on rules, and the group they form is generated by the two insertions; the group of *The Group of Involutions*, generated by the natural conjugation ${}^{\natural}$ and the coefficient conjugation $\bar{\cdot}$, is a group of maps of the algebra. Both are elementary abelian of order four, and they are not the same group: the elements of the first are readings of a rule and the elements of the second are conjugations of an element. **A reading is not a conjugation of an element**, and the four general products are the four readings of one rule and not the four conjugations of one element.

**Remark (the identity element, and what the group does not produce).** The group has an identity element, the reading with no insertion, and read on the general plain bilinear product that reading is the general plain bilinear product itself. The four general products are nevertheless introduced independently, one by one on the coordinates, in *The Four General Products and Their Relations*, and the group is read on the four afterwards; it is read in the same way on the four pairings, which are the scalar parts. What the group does not produce is an operator: its four elements act on rules, an operator acts on elements, and an operator needs an element of the algebra beside the reading (*Introduction to the Operators of the Biquaternion Algebra*).

### The Operation on a General Algebra

An insertion is an operation on a rule of two arguments, and nothing in its definition uses the multiplication of $\mathbb{B}$: the operation is available on the multiplication of any algebra carrying the two conjugations. The four readings of that multiplication are then four products again, and they are the **slot family** of the algebra; the four general products are its instance $\mathbb{B}$, and the two generators of §*The Readings and Their Group* are the two slots of the family.

**Definition (the slot family).** Let $A$ be a unital associative $\mathbb{C}$-algebra, and let $\natural$ and $\varsigma$ be involutive anti-automorphisms of $A$ that commute, with $\natural$ $\mathbb{C}$-linear, $\varsigma$ conjugate-linear and $\natural(1)=\varsigma(1)=1$. For $K_1\in\{\mathrm{id},\natural\}$ and $K_2\in\{\mathrm{id},\varsigma\}$ put

$$
x\star_{K_1K_2}y=K_1(x)\,K_2(y).
$$

The **first slot** is $K_1$ and the **second slot** is $K_2$. In $\mathbb{B}$, with $A=\mathbb{B}$, $\natural$ the natural conjugation and $\varsigma$ the Hermitian conjugation, the four settings are the four general products in the order of the readings, $\star_{\mathrm{id}\,\mathrm{id}}$, $\star_{{}^{\natural}\mathrm{id}}$, $\star_{\mathrm{id}{}^{*}}$ and $\star_{{}^{\natural}{}^{*}}$.

**Theorem (the second slot rules the composition).** With $A$, $\natural$, $\varsigma$ as in the definition, let $K_1\in\{\mathrm{id},\natural\}$, $K_2\in\{\mathrm{id},\varsigma\}$ and $x\star y=x\star_{K_1K_2}y$. The following four statements are equivalent.

- $K_2=\mathrm{id}$.
- $\star$ is $\mathbb{C}$-bilinear in its second argument.
- $1$ is a left unit for $\star$: $1\star x=x$ for every $x$.
- The left multiplications $L_x:x'\mapsto x\star x'$ of $\star$ are closed under composition.

When they hold, $L_x\circ L_y=L_{xy}$ if $K_1=\mathrm{id}$ and $L_x\circ L_y=L_{yx}$ if $K_1={}^{\natural}$, so that the monoid of left multiplications is $A$ in the first case and the opposite monoid of $A$ in the second. When they fail, $L_x\circ L_y$ is $\mathbb{C}$-linear in its argument while every $L_z$ is conjugate-linear, so the composition is not a left multiplication at all.

*Proof.* ($K_2=\mathrm{id}$ implies bilinear and left unit.) $x\star(\lambda y)=K_1(x)\lambda y=\lambda(x\star y)$, and $1\star x=K_1(1)x=x$ since $\natural(1)=1$. ($K_2=\mathrm{id}$ implies closure.) $(L_x\circ L_y)(x')=K_1(x)K_1(y)x'$, which is $(xy)x'=L_{xy}(x')$ when $K_1=\mathrm{id}$ and $\natural(x)\natural(y)x'=\natural(yx)x'=L_{yx}(x')$ when $K_1={}^{\natural}$, the middle step because $\natural$ is an anti-automorphism.

(Bilinear implies $K_2=\mathrm{id}$.) Suppose $K_2=\varsigma$. Then $1\star(\lambda 1)=K_1(1)\varsigma(\lambda)1=\varsigma(\lambda)$, while $\lambda(1\star1)=\lambda$, and $\varsigma(\lambda)=\lambda$ fails at $\lambda=i$; so $\star$ is not $\mathbb{C}$-bilinear in its second argument, while it is $\mathbb{C}$-linear in the first, since $K_1$ is.

(Left unit implies $K_2=\mathrm{id}$.) Suppose $K_2=\varsigma$ and $1\star x=x$ for every $x$. Then $\varsigma(x)=1\star x=x$, so $\varsigma=\mathrm{id}$ against the hypothesis.

(Closure implies $K_2=\mathrm{id}$.) Suppose $K_2=\varsigma$. Then $1\star(1\star x)=\varsigma(\varsigma(x))=x$, so $L_1\circ L_1$ is the identity, while $L_z(\lambda x')=K_1(z)\varsigma(\lambda x')=\varsigma(\lambda)L_z(x')$ for every $z$, and $\varsigma\neq\mathrm{id}$; the identity is therefore not a left multiplication.

**Theorem (the first slot rules the right unit).** With the hypotheses and notation of the previous theorem, $1$ is a right unit for $\star$ if and only if $K_1=\mathrm{id}$.

*Proof.* $x\star 1=K_1(x)K_2(1)=K_1(x)$, since $\varsigma(1)=1$; this is $x$ for every $x$ if and only if $K_1=\mathrm{id}$.

**Corollary (the units, in the two slots).** $1$ is a left unit for the two settings whose second slot is trivial and a right unit for the two whose first slot is trivial, so exactly one of the four has a two-sided unit. These are the four unit entries of the property table of *The Four General Products and Their Relations* and of its §*Identities and Units*, where a left unit is called a left identity, and the reason for them is the two slots.

**Theorem (associativity needs both slots trivial, in $\mathbb{B}$).** In $\mathbb{B}$ the product $\star_{K_1K_2}$ is associative if and only if $K_1=\mathrm{id}$ and $K_2=\mathrm{id}$.

*Proof.* The product $\star_{\mathrm{id}\,\mathrm{id}}$ is the multiplication of the associative algebra $\mathbb{B}$. For the converse, each of the other three settings is excluded by a triple of *The Four General Products and Their Relations*, §*The Failure of Associativity*: $(\tilde Q_1,\tilde Q_2,\tilde Q_3)=(-\vec e_y,-\vec e_y,\vec e_y)$ at the setting $({}^{\natural},\mathrm{id})$, $(-\vec e_z,\vec e_y,\vec e_y)$ at $(\mathrm{id},{}^{*})$, and $(-\vec e_z,\vec e_z,e_t)$ at $({}^{\natural},{}^{*})$, the two sides differing by the sign of a single basis element in each case.

**Remark (the first two theorems are theorems about the family, the third is not).** The two slot theorems hold in any $A$ of the definition, because their proofs use only that $\varsigma$ is conjugate-linear and not linear and that $\natural$ is an anti-automorphism. Associativity is not read on the slots: when both anti-involutions are the identity the four settings coincide, and with them associativity, so no rule stated in the two slots alone can hold for the whole family at once. Associativity is therefore decided in $\mathbb{B}$, by the triples above, and it remains the row of the property table that the slots do not read.

### The Table of the Slots

The two slot theorems, the pairings and the square collect into one table, one row for each property of the four general products, with the slot that carries the property and the rule it follows. The italic entries are the two that are not read on the slots of the general family.

| property of $\star_{K_1K_2}$ | decided by | the rule |
|---|---|---|
| $\mathbb{C}$-bilinear in the second argument | the second slot | yes if and only if $K_2=\mathrm{id}$ |
| $1$ is a left unit | the second slot | yes if and only if $K_2=\mathrm{id}$ |
| the left multiplications compose | the second slot | yes if and only if $K_2=\mathrm{id}$ |
| $1$ is a right unit | the first slot | yes if and only if $K_1=\mathrm{id}$ |
| the coefficient $\varepsilon$ survives in the scalar part | the two slots | yes if and only if the two slots agree |
| the Hermitian reading is positive definite | exactly one setting | only at $(\mathrm{id},{}^{*})$ |
| the form is definite on each sector | the first slot | yes if and only if $K_1=\mathrm{id}$ |
| $1$ is a two-sided unit | the two slots | yes if and only if $K_1=K_2=\mathrm{id}$ |
| *associative* | the two slots | yes if and only if $K_1=K_2=\mathrm{id}$, in $\mathbb{B}$ |
| *the square is scalar* | exactly one setting | only at $({}^{\natural},\mathrm{id})$ |

The first four rows are the slot reading of the property table of *The Four General Products and Their Relations*, §*The Property Table*, whose columns are the four general products. The fifth is the coefficient $\varepsilon$ of the corollary on the pairings, and the sixth and the seventh are the two form rows, the Hermitian reading on the whole space and the form on the two sectors $\mathbb{M}_-$ and $\mathbb{M}_+$ of dimension four; they are the rows of *The Four Forms and the Four Algebraic Norms*, which owns the forms and their signatures. The eighth is the two unit rows together, and the last two are the two rows that the slots do not decide, associativity in §*The Operation on a General Algebra* and the scalar square in §*The Square at One Setting*.

The table says that the second slot governs the **composition**: iterating the operation, the unit acting on the left and the left multiplications forming a monoid are one property of one slot. The first slot governs the **form**: the unit acting on the right, the definiteness of the form on a sector and, jointly with the second slot, the survival of the coefficient $\varepsilon$. A product in the right-hand column is a pairing and not a composition, and no choice in the first slot repairs that.

### The Square at One Setting

**Theorem (the square is scalar at exactly one setting).** In $\mathbb{B}$, $\tilde Q\star_{K_1K_2}\tilde Q$ is a scalar, that is a multiple of $e_t$, if and only if $(K_1,K_2)=({}^{\natural},\mathrm{id})$; and then $\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$ with $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$.

*Proof.* By *Norm Regularity and Degeneracy in the Biquaternion Algebra* the ${}^{\natural}$-square is $\langle\tilde Q\rangle_{\natural}e_t$ for every element, the norm form of the quaternion algebra $\mathbb{B}$ taking its values in the centre $\mathbb{C}e_t$. Each of the other three settings is excluded by one element: at the reading (none) the element $e_t+\vec e_x$ has the square $2\vec e_x$, at the reading (${}^{*}$) the element $e_t+i\vec e_x$ has the square $2e_t+2i\vec e_x$, and at the reading (both) the element $e_t+\vec e_x$ has the square $-2\vec e_x$; none of the three is a scalar.

**Remark (this rule is not general).** The rule uses that $\natural$ is the standard involution of a quaternion algebra and that its norm form therefore lands in the centre, and it fails as soon as the algebra is changed and the involution kept. In the matrix algebra $M_2(\mathbb{C})$ with the transpose in the role of $\natural$, the element

$$
\begin{pmatrix}0&1\\0&0\end{pmatrix}
\quad\text{has the square}\quad
\begin{pmatrix}0&0\\0&1\end{pmatrix},
$$

which is not a scalar multiple of $\mathrm{I}_2$. **The scalar square is a property of $\mathbb{B}$ and not of the slot family**, and it is the row of the table of §*The Table of the Slots* that assigns the ${}^{\natural}$-product its place among the four.


## The Two Switches and the Twisted Right Factor

The four readings of §*The Readings and Their Group* are also read on a single operator, once the two insertions are put on the right factor. The first is the **coefficient involution** $\sigma$, the conjugation of the scalars of $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, which on this algebra is the coefficient conjugation $\bar{\cdot}$ of *The Group of Involutions*; the second is the **sign character** $\alpha$, the identity on the centre $\mathbb{C}_{\mathbb{B}}$ and minus the identity on the vector subspace $V$, which on this algebra is the natural conjugation $\natural$ read as a twist, as in *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, where the same operator carries $\alpha$ in place of $\natural$. The two commute, one being linear over $\mathbb{C}$ and the other conjugate-linear, and their four settings are the four settings of the products, now on one parameter rather than on the two slots.

**Definition (the twisted right factor and its operator).** For a switch pair $(\sigma,\alpha)$ and a parameter $\tilde Q_4$ put

$$
c_{\sigma,\alpha}(\tilde Q_4)=\sigma\bigl(\alpha(\tilde Q_4)\bigr),
\qquad
\Phi^{\sigma,\alpha}_{\tilde Q_4}(\tilde Q)=\tilde Q_4\,\tilde Q\,c_{\sigma,\alpha}(\tilde Q_4).
$$

**The four settings.** Each switch is either the identity or its involution, so there are four right factors:

| $\sigma$ | $\alpha$ | $c_{\sigma,\alpha}(\tilde Q_4)$ | the operator | value at $e_t$ |
|---|---|---|---|---|
| $\mathrm{id}$ | $\mathrm{id}$ | $\tilde Q_4$ | $\tilde Q\mapsto\tilde Q_4\tilde Q\tilde Q_4$ | $\tilde Q_4^{2}$ |
| $\mathrm{id}$ | $\alpha$ | $\tilde Q_4^{\natural}$ | the conjugation sandwich, the operator of *Two-Sided Operators on the General Quaternionic Algebra* | $\langle\tilde Q_4\rangle_{\natural}=\tilde Q_4\tilde Q_4^{\natural}$, central |
| $\sigma$ | $\mathrm{id}$ | $\bar{\tilde Q_4}$ | $\tilde Q\mapsto\tilde Q_4\tilde Q\bar{\tilde Q_4}$ | $\tilde Q_4\bar{\tilde Q_4}$, scalar part the split norm |
| $\sigma$ | $\alpha$ | $\tilde Q_4^{\ast}$ | the Hermitian sandwich, $\tilde Q\mapsto\tilde Q_4\tilde Q\tilde Q_4^{\ast}$ | $\tilde Q_4\tilde Q_4^{\ast}$, Hermitian |

The fifth conjugation of the algebra, the reversal $\flat=-\ast$ of *The Group of Involutions*, is the last row with the extra central sign: $\tilde Q_4^{\flat}=-\tilde Q_4^{\ast}$, so the reversal sandwich is minus the Hermitian sandwich.

**Proposition (which right factors close the family).** The composite of two such operators is $\Phi^{\sigma,\alpha}_{\tilde Q_4}\circ\Phi^{\sigma,\alpha}_{\tilde Q_1}=\Phi^{\sigma,\alpha}_{\tilde Q_4\tilde Q_1}$ exactly when $c$ is an anti-automorphism, which holds for the two rows with $\alpha$ and fails for the other two. The four scalar parts of the value at $e_t$ are the four forms, and the adjoint-side reading of the same two switches is *The Four Adjoints of the Biquaternion Algebra in Examples*, §*Which Switch Does What*.

**Remark (the same two switches on the left factor).** The left slot may also carry a twist, and there it must be an automorphism, so the two possibilities are the identity and $\sigma$. With the right factor $c$ the inverse, $\natural$ or $\ast$, and the left slot either the identity or $\sigma$, the six members are the ones the corpus uses: the inner conjugation $\mathrm{Ad}_{\tilde Q_4}$, the conjugation sandwich $\tilde Q_4\,\tilde Q\,\tilde Q_4^{\natural}$ and the Hermitian sandwich $\tilde Q_4\,\tilde Q\,\tilde Q_4^{\ast}$ are the three with the identity on the left, while $\bar{\tilde Q_4}\,\tilde Q\,\tilde Q_4^{-1}$ is the $\sigma$-twisted one, the operator of the general theory of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, and $(\sigma,\natural)$, $(\sigma,\ast)$ are the two remaining. Every one of the remarkable subspaces is multiplicative in the parameter, by the proposition above.

## What the Products Decide and What the Choice Decides

### The Products Decide the Four Adjoints

**Theorem (the four adjoints are decided by the four general products).** For the left multiplication $L_{\tilde Q_4}$ the adjoints of the four pairings are

$$
\boxed{\;
(L_{\tilde Q_4})^{\approx}=R_{\tilde Q_4},\qquad
(L_{\tilde Q_4})^{\ast}=L_{\tilde Q_4^{\ast}},\qquad
(L_{\tilde Q_4})^{N}=L_{\tilde Q_4^{\natural}},\qquad
(L_{\tilde Q_4})^{\natural\ast}=R_{\bar{\tilde Q_4}}
\;},
$$

and for the two-sided operator $(L_{\tilde Q_4}R_{\tilde Q_1})^{\approx}=L_{\tilde Q_1}R_{\tilde Q_4}$, $(L_{\tilde Q_4}R_{\tilde Q_1})^{\ast}=L_{\tilde Q_4^{\ast}}R_{\tilde Q_1^{\ast}}$, $(L_{\tilde Q_4}R_{\tilde Q_1})^{N}=L_{\tilde Q_4^{\natural}}R_{\tilde Q_1^{\natural}}$, $(L_{\tilde Q_4}R_{\tilde Q_1})^{\natural\ast}=L_{\bar{\tilde Q_1}}R_{\bar{\tilde Q_4}}$.

*Proof.* *The Four Adjoints of the Biquaternion Algebra in Examples*, where all sixteen cases are verified on the pairs of basis elements.

So the product *does* decide something of the first importance: which adjoint exists, and therefore which of the four operator families has a coherent adjoint theory. That is the whole content of the naming rule of the corpus, and it is a statement about *forms*.

### The Operator Is Not Decided

**Remark (the missing inputs).** The four general products share the table of the units, so no two of them can differ in the way an operator differs from another. To write down an operator one has still to supply

1. an **element** $\tilde Q_4$ of the algebra, and
2. an **insertion**: which involution, if any, is put on the element, and on which side.

The products do not supply 1, and they supply the *repertoire* of 2 without choosing from it. That is the sense in which the operator is chosen by the modeller: given the algebra with its product, one chooses $\natural$, or $\bar{\cdot}$, or ${}^{*}$, or none, and therefore the operator.

## One Element, Four Operators

### The Four Operators of $\vec e_x$

Fix the element $\tilde Q_4=\vec e_x$, a unit with $\langle \vec e_x\rangle_{\natural}=-e_t$, so that $\vec e_x^{-1}=-\vec e_x$. Read it through the four insertions, using the inverse of the conjugated element in the right factor:

$$
\begin{aligned}
\text{no insertion:}\quad & L_{\vec e_x}R_{\vec e_x^{-1}} & \tilde Q_2&\longmapsto \vec e_x\tilde Q_2 \vec e_x^{-1},\\
\text{sign }\natural\text{ on the left:}\quad & L_{\vec e_x^{\natural}}R_{\vec e_x^{-1}} & \tilde Q_2&\longmapsto \vec e_x^{\natural}\tilde Q_2 \vec e_x^{-1},\\
\text{star on the right:}\quad & L_{\vec e_x}R_{(\vec e_x^{*})^{-1}} & \tilde Q_2&\longmapsto \vec e_x\tilde Q_2 (\vec e_x^{*})^{-1},\\
\text{both:}\quad & L_{\vec e_x^{\natural}}R_{(\vec e_x^{*})^{-1}} & \tilde Q_2&\longmapsto \vec e_x^{\natural}\tilde Q_2(\vec e_x^{*})^{-1}.
\end{aligned}
$$

For $\vec e_x$ the two conjugations are $\natural(\vec e_x)=-\vec e_x$ and $\vec e_x^{*}=-\vec e_x$, so the four operators are two, and in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ they are

$$
\operatorname{diag}(1,1,-1,-1)
\quad\text{and}\quad
\operatorname{diag}(-1,-1,1,1),
$$

the first for the two insertions that agree (none or both), the second for the sign on the left or the star on the right alone. On the vector subspace $V$ they restrict to

$$
\operatorname{diag}(1,-1,-1)
\quad\text{and}\quad
\operatorname{diag}(-1,1,1).
$$

**Remark (the four insertions collapse).** For a parameter that one of the conjugations fixes, the four operators are fewer than four: the sign insertion is invisible exactly when $\tilde Q_4^{\natural}=\tilde Q_4$, which holds for the central $\tilde Q_4$, and the star insertion is invisible exactly when $\tilde Q_4^{*}=\tilde Q_4$, which holds for the parameters with real central coefficient and purely imaginary vector coefficients, the fixed space $\mathbb{M}_{+}$ of the Hermitian conjugation. For a vector $\tilde Q_4\in V$ with real coefficients the four operators are two, $\pm L_{\tilde Q_4}R_{\tilde Q_4^{-1}}$; for a generic complex vector of $V$ the four are pairwise distinct. The number of distinct operators is therefore a property of the *element*, and not of the product.

## Rotation, Reflection, and Where the Sign Is Read

### The Plain Product Gives Minus the Reflection

**Theorem (the reflection is reached only through the sign).** Let $\tilde Q_4\in V$ be a vector with $\langle\tilde Q_4\rangle_{\natural}\ne0$, and let $\rho_{\tilde Q_4}$ be the reflection of $V$ in the hyperplane $\tilde Q_4^{\perp}$ for the polar form of $q=-\sum_kQ_k^{2}$, which on $V$ is the general plain bilinear form $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$,

$$
\rho_{\tilde Q_4}(\tilde Q_3)=\tilde Q_3-\frac{2\langle\tilde Q_3,\tilde Q_4\rangle}{\mathfrak{Q}(\tilde Q_4)}\,\tilde Q_4 .
$$

Then the two insertions that read the parameter as it stands keep $V$ stable, and

$$
\boxed{\;
L_{\tilde Q_4}R_{\tilde Q_4^{-1}}\big|_{V}=-\rho_{\tilde Q_4},\qquad
L_{\tilde Q_4^{\natural}}R_{\tilde Q_4^{-1}}\big|_{V}=\rho_{\tilde Q_4}
\;},
$$

with determinant of the restriction $+1$ and $-1$. The two insertions that read the right factor through ${}^{*}$ behave differently, and the proposition below says exactly how.

*Proof.* For $\tilde Q_4\in V$ the sign reads the parameter as $\tilde Q_4^{\natural}=-\tilde Q_4$, so that $L_{\tilde Q_4^{\natural}}R_{\tilde Q_4^{-1}}=-L_{\tilde Q_4}R_{\tilde Q_4^{-1}}$; the identity $L_{\tilde Q_4}R_{\tilde Q_4^{-1}}\big|_{V}=-\rho_{\tilde Q_4}$ is the reflection formula of the Clifford algebra in the convention $\mathfrak{Q}(\tilde Q_4)=\langle\tilde Q_4,\tilde Q_4\rangle<0$, equivalently $\tilde Q_4\tilde Q_3+\tilde Q_3\tilde Q_4=2\langle\tilde Q_4,\tilde Q_3\rangle$ and $\tilde Q_4^{2}=\mathfrak{Q}(\tilde Q_4)e_t$.

**Proposition (the star insertions leave $V$ in general).** For $\tilde Q_4\in V$ the right factor of the starred insertions is $(\tilde Q_4^{*})^{-1}=-(\bar{\tilde Q_4})^{-1}$, so the two starred operators are $-L_{\tilde Q_4}R_{(\bar{\tilde Q_4})^{-1}}$ and $+L_{\tilde Q_4}R_{(\bar{\tilde Q_4})^{-1}}$. They keep $V$ stable exactly when $\bar{\tilde Q_4}$ is a scalar multiple of $\tilde Q_4$, that is when the coefficient vector of $\tilde Q_4$ is a complex multiple of a real one. When it is, and only then, a determinant on $V$ is defined: it is $-1$ for the star insertion and $+1$ for the both insertion when the coefficient vector is real, the two are exchanged when it is purely imaginary, and for a coefficient vector that is a non-real, non-imaginary complex multiple of a real one the restriction is neither $\pm\rho_{\tilde Q_4}$ nor form-preserving. For a generic complex parameter, $V$ is not preserved and the starred insertions are read on the algebra and not on $V$.

*Proof.*

**Remark (the sentence of the corpus, translated).** *The Signed Sandwich on a Clifford Algebra* says that the ordinary sandwich by a vector is the **negative** of the reflection, and that inserting the grade involution *repairs the sign*. The theorem above is that sentence in the biquaternion model: the plain product gives $-\rho_{\tilde Q_4}$, the involution of $V$ whose fixed space has codimension one, and the sign insertion gives $\rho_{\tilde Q_4}$. This is the one place where the algebra forces a choice rather than permitting one.

**Corollary (where a determinant plus one lives).** On the algebra $\mathbb{B}$ itself, of complex dimension four, all four operators have determinant $+1$; the sign shows in the determinant only on the odd-dimensional restriction $V$, or on a real form of odd dimension. A "rotation" and a "reflection" are therefore read on $V$.

*Proof.* The operators are products $L_{\tilde Q_4}R_{\tilde Q_1}$, whose determinant on $\mathbb{B}$ is $\det(L_{\tilde Q_4})\det(R_{\tilde Q_1})$, and for a four-dimensional space the sign $-1$ on a parameter contributes the factor $(-1)^{4}=+1$.

### The Sign Is Invisible on the Centre and on Even Parameters

**Proposition.** If $\tilde Q_4$ is central, $\tilde Q_4=a_0e_t$, then the sign insertion changes nothing, $L_{\tilde Q_4^{\natural}}R_{\tilde Q_4^{-1}}=L_{\tilde Q_4}R_{\tilde Q_4^{-1}}$. If $\tilde Q_4\in V$ is a vector, the sign insertion negates the operator, $L_{\tilde Q_4^{\natural}}R_{\tilde Q_4^{-1}}=-L_{\tilde Q_4}R_{\tilde Q_4^{-1}}$.

*Proof.* $\natural$ fixes the centre and negates $V$; left multiplication and right multiplication commute.

**Theorem (the determinant table).** For a unit $\tilde Q_4$ let $d$ be the determinant of the operator restricted to $V$ for the four insertions, in the order (none, sign on the left, star on the right, both). Then

| $\tilde Q_4$ | none | sign | star | both |
|---|---|---|---|---|
| $e_t$ | $+1$ | $+1$ | $+1$ | $+1$ |
| $i e_t$ | $+1$ | $+1$ | $-1$ | $-1$ |
| $\vec e_x$ | $+1$ | $-1$ | $-1$ | $+1$ |
| $\vec e_x+\vec e_y$ | $+1$ | $-1$ | $-1$ | $+1$ |
| $i \vec e_x$ | $+1$ | $-1$ | $+1$ | $-1$ |
| $e_t+\vec e_x$ | $+1$ | $0$ | $0$ | $+1$ |

The zero entries are the starred insertions of a mixed parameter, whose operator does not preserve $V$, so that the restricted determinant is $0$ and is not a rotation-reflection marker; the star and both columns are read on $V$ only for the rows whose parameter has a real or purely imaginary coefficient vector.

*Proof.* The rows are the computed determinants; the first row is the identity on $V$; the second row shows that a central imaginary parameter, on which the sign is invisible, is still separated by the conjugate-linear insertion, $(\tilde Q_4^{*})^{-1}=i e_t$, which gives $-e_t$ on the left factor and hence $-\mathrm{id}$ on $V$; the third and fourth rows are the theorem above; the fifth row is a purely imaginary vector, on which the star insertion coincides with the plain one and the both insertion with the sign, so that the determinants are those of the third row read with the two insertions exchanged; the last row is a mixed parameter, whose starred operators do not keep $V$ stable.

**Remark (the two central rows).** The proposition and the table together show the two independent choices: the *sign* $\natural$ is invisible on the centre and reads only the odd part, while the *star* is invisible on the real directions and reads the coefficient imaginary. Neither is a property of the product; both are properties of the insertion into the chosen element.

## Which Involution Is "the Sign" Is Itself a Choice

**Remark (the corpus fixes the sign by a formula).** The biquaternion corpus calls $\natural$ the sign and uses it throughout, but the map that plays the role of the sign is a choice among the involutions of the algebra. The identification $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, $\gamma_k\mapsto i\vec e_k$, has the grades $\text{grade }0=\mathbb{R}e_t$, $\text{grade }1=\mathrm{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$, $\text{grade }2=\mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$, $\text{grade }3=\mathbb{R}ie_t$, and in that reading

| map on $\mathbb{B}$ | Clifford partner | signs on grades $0,1,2,3$ | coefficient sign vector on $e_t,\vec e_x,\vec e_y,\vec e_z$ |
|---|---|---|---|
| quaternion conjugation $\natural$ | Clifford conjugation $\alpha(X^{r})$ | $+,-,-,+$ | $(1,-1,-1,-1)$ |
| complex conjugation $\bar{\cdot}$ | grade involution $\alpha$ | $+,-,+,-$ | fixes $\vec e_x,\vec e_y,\vec e_z$, reverses $i$ |
| Hermitian conjugation ${}^{*}$ | reversion $X^{r}$ | $+,+,-,-$ | $-1$ on $\vec e_x,\vec e_y,\vec e_z$ and $-1$ on $ie_t$ |

So the corpus's "sign" is the map with the sign vector $(1,-1,-1,-1)$, and it is *not* the grade involution of that Clifford reading: the grade involution is the coefficient conjugation, and on $V$, which is the grade-two part there, it is the identity. Two consequences follow, and both answer the question of the title. First, the corpus's choice of $\natural$ as the sign is a convention of the biquaternion model, fixed by the coefficient formula and not by an abstract parity. Second, the reflection theorem is nevertheless not a convention: with the sign $\natural$ it holds, and with the grade involution, which is trivial on $V$, it fails.

**Remark (parameter or argument).** The sign may be inserted in the **parameter**, $L_{\tilde Q_4^{\natural}}R_{\tilde Q_4^{-1}}$, which is the *signed inner conjugation* of the corpus, or in the **argument**, $\tilde Q_2\mapsto\tilde Q_4\,\tilde Q_2^{\natural}\,\tilde Q_4^{-1}$, which is the *signed sandwich* of *The Signed Sandwich on a Clifford Algebra*. On the vector subspace the two agree, because both act by the sign $-\mathrm{id}$ there; on the whole algebra they differ, and the general corpus keeps the two families apart on purpose, the one twisting the parameter and the other the argument.

## Summary

The four general products of the biquaternion algebra are one multiplication with a conjugation inserted independently into each of the two slots. They therefore share the multiplication table of the units, and they determine the four pairings — their scalar parts — and with the pairings the four adjoints and the names of the four operator families. They do not determine an operator. An operator needs an element, and it needs an insertion: which involution, if any, is put on the element and on which side, and whether the sign goes into the parameter or into the argument. The element $\vec e_x$ read through the four insertions gives two operators, $\operatorname{diag}(1,1,-1,-1)$ and $\operatorname{diag}(-1,-1,1,1)$, and on the vector subspace they are $-\rho_{\vec e_x}$ and $\rho_{\vec e_x}$: the plain product gives $-\rho_{\vec e_x}$, and the reflection is reached only through the sign. On the four-dimensional algebra both have determinant $+1$, so rotation and reflection are read on the vector subspace. Finally, which map plays the role of the sign is itself chosen: the biquaternion corpus fixes it as the natural conjugation $\natural$, whose sign vector is $(1,-1,-1,-1)$, and that is a convention of the model, whereas the identity "the reflection needs the sign" is a theorem. The answer to the question is therefore: no, the product does not decide between a rotation and a reflection; the algebra and its product come first, and the operator is obtained from them by choosing the element and the insertion.

The four insertions are the four elements of a group. One reads the first argument through the natural conjugation, one reads the second through the Hermitian conjugation; each is its own inverse, the two commute, and the four are the two, their composite and the identity. Read on a general algebra with two commuting anti-involutions, the group gives the slot family: the second slot carries the $\mathbb{C}$-bilinearity in the second argument, the left unit and the monoid of left multiplications, the first slot carries the right unit, and associativity and the scalar square are not decided by the slots alone. The table of the slots records the four settings, their units, their squares and the one setting whose square is central.

The same two switches are read on one operator, with the conjugation in the right factor: $\Phi^{\sigma,\alpha}_{\tilde Q_4}(\tilde Q)=\tilde Q_4\tilde Qc_{\sigma,\alpha}(\tilde Q_4)$, where $c$ is the identity, the natural conjugation, the coefficient conjugation or the Hermitian conjugation. The family closes under composition exactly when $c$ is an anti-automorphism, that is for the two right factors that carry the sign; the four scalar parts of one element are the four forms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{id}$, $\natural$, ${}^{*}$, $\natural{}^{*}$ | the four readings, the elements of $\mathbb{Z}_2\times\mathbb{Z}_2$; (none), (${}^{\natural}$), (${}^{*}$), (both) |
| $\star_{K_1K_2}$ | the general slot product, $x\star_{K_1K_2}y=K_1(x)K_2(y)$ with $K_1\in\{\mathrm{id},\natural\}$ and $K_2\in\{\mathrm{id},\varsigma\}$ |
| $\varsigma$ | the involution that defines the class, $\natural$ or ${}^{*}$; $\varsigma=\mathrm{id}$ for the bilinear class |
| $\star^{\mathrm{op}}$ | the opposite product, $x\star^{\mathrm{op}}y=y\star x$ |
| $\tilde Q_1\tilde Q_2$, $\tilde Q_1\tilde Q_2^{*}$, $\tilde Q_1^{\natural}\tilde Q_2$, $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | the four general products: one table, the two insertions |
| $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\ast}$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{\natural\ast}$ | their scalar parts, the four pairings, Gram matrices $\mathrm{E},\mathrm{I}_4,\mathrm{I}_4,\mathrm{E}$ |
| ${}^{\approx}$, ${}^{*}$, ${}^{N}$, ${}^{\natural\ast}$ | the four adjoints, decided by the four general products |
| $\natural$, $\bar{\cdot}$, ${}^{*}$ | the sign, the coefficient conjugation, the Hermitian conjugation; $\natural$ has sign vector $(1,-1,-1,-1)$ |
| $\sigma$, $\alpha$ | the coefficient involution and the sign character, the two switches |
| $c_{\sigma,\alpha}(\tilde Q_4)=\sigma(\alpha(\tilde Q_4))$ | the twisted right factor: $\tilde Q_4$, $\tilde Q_4^{\natural}$, $\bar{\tilde Q_4}$ or $\tilde Q_4^{\ast}$ |
| $\Phi^{\sigma,\alpha}_{\tilde Q_4}(\tilde Q)=\tilde Q_4\tilde Qc_{\sigma,\alpha}(\tilde Q_4)$ | the two-sided operator of the switches |
| $L_{\tilde Q_4}R_{\tilde Q_1}$ | a two-sided operator; $L_{\tilde Q_4}R_{\tilde Q_4^{-1}}$ the inner automorphism of the plain product |
| $L_{\tilde Q_4^{\natural}}R_{\tilde Q_4^{-1}}$, $\tilde Q_2\mapsto\tilde Q_4\tilde Q_2^{\natural}\tilde Q_4^{-1}$ | the sign inserted in the parameter, and in the argument |
| $\rho_{\tilde Q_4}$ | the reflection of $V$ in $\tilde Q_4^{\perp}$; the plain product gives $-\rho_{\tilde Q_4}$, the sign gives $\rho_{\tilde Q_4}$ |
| $\operatorname{diag}(1,1,-1,-1)$, $\operatorname{diag}(-1,-1,1,1)$ | the two operators of $\vec e_x$, and their restrictions $\operatorname{diag}(1,-1,-1)$, $\operatorname{diag}(-1,1,1)$ to $V$ |

## Further Reading

- [The Four General Products and Their Relations](the-four-general-products-and-their-relations.html), for the four rules, the statement that they differ in one insertion alone, and the table of the four side by side
- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the four forms, their Gram matrices, their signatures and their isometry groups
- [The Four Adjoints of the Biquaternion Algebra in Examples](the-four-adjoints-of-the-biquaternion-algebra-in-examples.html), for the four adjoints on explicit operators and the naming rule of the operator families
- [The Group of Involutions](the-group-of-involutions.html), for the four conjugations and their group
- [The Signed Sandwich on a Clifford Algebra](the-signed-sandwich-on-a-clifford-algebra.html), for the ordinary sandwich, its minus sign and the repair by the grade involution
- [Two-Sided Operators with the Signed Product](two-sided-operators-with-the-signed-product.html), for the signed family, its twisted composition law and its coset structure
- [Two-Sided Operators on the General Quaternionic Algebra](two-sided-operators-on-the-general-quaternionic-algebra.html), for the parameter insertion in the biquaternion model
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the plain family that the right factors twist, and its criteria
- [Remarkable Subspaces and the Four General Products, Forms and Norms](remarkable-subspaces-and-the-four-general-products-forms-and-norms.html), for the four general products read on the remarkable real subspaces
- [Biquaternion Versors and the Orthogonal Group](biquaternion-versors-and-the-orthogonal-group.html), for the parity, the determinant and the Lorentz group
