# __Introduction to the General Plain Sesqualgebra of Biquaternions__

## Introduction

The underlying $\mathbb{C}$-vector space of the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ carries four general products, defined side by side in *The Four General Products of the Biquaternion $\mathbb{C}$ Space*. Read as a multiplication, one of the four makes that space an associative unital algebra, the general plain bilinear product $\tilde P\tilde Q$, and that reading is *Introduction to the General Plain Algebra of Biquaternions*. A second reading is available, and it is the subject of this article: the **general plain sesquilinear product** $\tilde P\tilde Q^{*}$ is additive in each variable, $\mathbb{C}$-linear in the first and $\mathbb{C}$-**conjugate**-linear in the second, and those are the two scalar rules of a **sesqualgebra** over $\mathbb{C}$ with its conjugation as the base involution (*Sesqualgebras*). The fourth product satisfies the same two rules, its first slot being read through the $\mathbb{C}$-linear ${}^{\natural}$, so the rules alone do not select this product; what does is proved in §*Which of the Four Is a Sesquilinear Multiplication*. This article takes $\tilde P\tilde Q^{*}$ as the multiplication and builds the sesqualgebra it defines.

The consequences are of a different kind from the bilinear case. Associativity is not available: a sesqualgebra of full type with a nontrivial involution is **never** associative, by the collapse theorem of *Sesqualgebras*, and $\mathbb{B}$ is of full type. What survives is the structure that does not need associativity: a unit on one side alone, an involution that exchanges the two slots, the ternary product $\tilde P\tilde Q^{*}\tilde R$ with the algebraic $J^{*}$-algebra it defines, the two halves of the algebra cut out by the involution, the squares that generate the positive cone, and the simplicity of the product as an ideal-theoretic object.

Three boundaries are stated at once. The product is not defined here, and neither are the four general products as a family: the coordinate rule and the four names are *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and the comparison of their properties is *Comparison Between the Four General Products*. The same space read as an algebra and the question of its base rings are *Introduction to the General Plain Algebra of Biquaternions* and, with the real scalars, *Biquaternions as an Algebra over $\mathbb{R}$*, and neither is repeated here. And the elements, the basis, the conjugations and the remarkable subspaces are *Biquaternions as a Vector Space over $\mathbb{C}$*, *Introduction to the Remarkable Subspaces* and *Decompositions Along the Remarkable Subspaces*; the subspaces are named here only as the two halves the involution cuts out.

One word on the two scalar rules, because they are weaker than they look. They admit a product as soon as it is additive in each variable and sesquilinear for **some** involution of $\mathbb{C}$, so they admit all four general products of $\mathbb{B}$: the two bilinear ones for the trivial involution and the two carrying the star for the conjugation. The corresponding row of *Comparison Between the Four General Products* is therefore read with the definition and with nothing added, and it reads no, no, yes, yes: **both** products carrying the star are multiplications of a sesqualgebra over $\mathbb{C}$ with the conjugation, and the two bilinear ones are the trivial-involution collapse of the same definition. The section *Which of the Four Is a Sesquilinear Multiplication* draws that conclusion and then decides the sharper question, which of the four general products is the **derived operation** $\tilde X\star\tilde Y=\tilde X\tilde Y^{*}$ of the algebra $\mathbb{B}$ with its conjugate-linear involution; the answer is the general plain sesquilinear product alone, and that is the product this article is about.

The general theory is the sesquilinear block: the definition and the standard example are *Sesqualgebras*, the calculus of the product is *The Sesquilinear Product*, the semilinear maps and the conjugate module are *Conjugate-Linear Maps and the Conjugate Dual*, the associator and the ternary product are *The Sesquilinear Associator and the Ternary Product*, the abstract ternary system is *Algebraic J\*-Algebras*, the two halves of an involutive algebra are *Hermitian and Skew-Hermitian Elements*, the squares are *Hermitian Squares and the Algebraic Positive Cone*, and the ideals are *Ideals and Quotients of a Sesqualgebra*. On the biquaternion side, the two-sided ideals of the algebra and the simplicity of the ring are *Biquaternion Ideals and Peirce Decomposition*, and the idempotents are *Idempotents of the General Plain Algebra*.

**Conventions.** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is the biquaternion algebra, with basis $e_0,e_1,e_2,e_3$ and central scalar imaginary $i$, $i^2 = -1$; a general element is $\tilde Q = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$. Throughout, a biquaternion is written $\tilde Q = Q_0e_0 + \mathbf Q$ with $\mathbf Q = \sum_{k=1}^{3} Q_ke_k$, and $\overline{\mathbf Q}$ is the coefficientwise conjugate of the vector part. The base involution is the complex conjugation, written $\varsigma(z) = \bar z$, and the involution of the algebra is the Hermitian conjugation ${}^{*} = \bar{\cdot} \circ {}^{\natural}$, with the coordinates $Q^{*}_0 = \overline{Q_0}$ and $Q^{*}_k = -\overline{Q_k}$ for $k = 1,2,3$, that is $Q^{*}_\nu = \varepsilon_\nu \overline{Q_\nu}$ with $\varepsilon = (1,-1,-1,-1)$. The four general products and their notation are those of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*.

## The Product Read as a Multiplication

### The Rule

**Definition.** The **multiplication** of the sesqualgebra is the rule

$$
\star \; : \; \mathbb{B} \times \mathbb{B} \longrightarrow \mathbb{B} , \qquad
(\tilde P,\tilde Q) \longmapsto \tilde P \star \tilde Q = \tilde P\tilde Q^{*} ,
$$

the general plain sesquilinear product of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*. On the coordinates it reads

$$
\tilde P \star \tilde Q = \sum_{\mu=0}^{3}\sum_{\nu=0}^{3} P_\mu Q^{*}_\nu \, e_\mu e_\nu
= \sum_{\mu=0}^{3}\sum_{\nu=0}^{3} \varepsilon_\nu P_\mu \overline{Q_\nu} \, e_\mu e_\nu ,
$$

each product $e_\mu e_\nu$ being a basis element up to sign, so that the double sum is a complex combination of $e_0,\dots,e_3$ and the rule is well defined. The rule is the product $\tilde P\tilde Q^{*}$ and nothing else: it is quoted here, not defined, and the equality of the two displays is the definition of $\tilde Q^{*}$ in coordinates.

### The Scalar–Vector Form

Collecting the scalar part and the vector part of the two elements, the vector part of the second read through the coefficientwise conjugate, the same product reads

$$
\tilde P\star\tilde Q=\bigl(P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q})\bigr)-P_0\overline{\mathbf Q}+\overline{Q_0}\mathbf P-\mathbf P\times\overline{\mathbf Q} ,
$$

where $(\mathbf P,\overline{\mathbf Q})$ and $\mathbf P\times\overline{\mathbf Q}$ are the complex bilinear dot and cross products of the vector parts and the display is the one of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*. Its scalar part is $\mathrm{Sc}(\tilde P\star\tilde Q)=\sum_{\mu=0}^{3}P_\mu\overline{Q_\mu}$, conjugate-linear in the coordinates of the second element, and its vector part is the one displayed.

### The Two Scalar Rules

**Proposition.** The multiplication is **additive in each variable**; it is $\mathbb{C}$-**linear in the first** variable and $\varsigma$-**semilinear in the second**, with $\varsigma(z) = \bar z$:

$$
(\lambda\tilde P) \star \tilde Q = \lambda\,(\tilde P \star \tilde Q), \qquad
\tilde P \star (\lambda\tilde Q) = \bar\lambda\,(\tilde P \star \tilde Q), \qquad \lambda \in \mathbb{C} .
$$

**Proof.** The coordinates of the developed form are sums of terms $P_\mu\overline{Q_\nu}$ with fixed coefficients, so they are additive and $\mathbb{C}$-linear in the four coordinates of $\tilde P$ alone and additive and $\mathbb{C}$-conjugate-linear in the four coordinates of $\tilde Q$ alone. The two displays are that statement read coordinate by coordinate; the second is the reason the rule is not bilinear. $\square$

These are the two axioms of a sesquilinear product over $(\mathbb{C},\varsigma)$ and nothing else: no associativity, no commutativity and no two-sided unit is assumed (*The Sesquilinear Product*). The product is thus a second multiplication on the same space, of the sesquilinear kind, and the rest of the article asks what it forces.

### The Multiplication Table

**Proposition.** On the four basis elements the multiplication is

$$
e_\mu \star e_\nu = \varepsilon_\nu\, e_\mu e_\nu , \qquad \varepsilon = (1,-1,-1,-1) ,
$$

so the sixteen products are

| $\star$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $-e_1$ | $-e_2$ | $-e_3$ |
| $e_1$ | $e_1$ | $e_0$ | $-e_3$ | $e_2$ |
| $e_2$ | $e_2$ | $e_3$ | $e_0$ | $-e_1$ |
| $e_3$ | $e_3$ | $-e_2$ | $e_1$ | $e_0$ |

**Proof.** The involution acts on the basis by $e^{*}_\nu = \varepsilon_\nu e_\nu$, since ${}^{*}$ conjugates the coefficient and negates the vector units while fixing $e_0$. Multiplying by $e_\mu$ on the left with the general plain bilinear product gives the displayed products. $\square$

The table is not the quaternion table. Its diagonal is $e_0$ throughout, the three imaginary units anticommuting on the off-diagonal block with the signs of the quaternion product, $e_j \star e_k = -e_k \star e_j$ for $j \neq k$ in $\{1,2,3\}$; and the first row is the negation of the identity row, because $e_0 \star e_\nu = e^{*}_\nu$. The unit is therefore the unit of a single side only, and this asymmetry is the visible form of the second scalar rule.

### The Product Is the Derived Operation

**Theorem.** Let $\mathbb{B}$ be read as the associative $\mathbb{C}$-algebra with its conjugate-linear involution ${}^{*}$. Then the general plain sesquilinear product is the **derived operation** of that pair,

$$
\tilde P \star \tilde Q = \tilde P\tilde Q^{*} ,
$$

in the sense of *Sesqualgebras*: the multiplication of the algebra with the involution inserted in the second slot.

**Proof.** This is the definition of the rule read in the notation of the standard example, and the verification of the axioms is the proposition above; the involution ${}^{*}$ is $\varsigma$-semilinear, $(xy)^{*} = y^{*}x^{*}$ and $*^{2} = \mathrm{id}$, which is the datum the construction requires (*The Group of Involutions*, *Introduction to the General Plain Algebra of Biquaternions*). $\square$

**Corollary.** $(\mathbb{B},\star)$ is the standard example of a sesqualgebra over $(\mathbb{C},\varsigma)$ built on the biquaternion algebra, and every general theorem of *Sesqualgebras*, *The Sesquilinear Product* and *The Sesquilinear Associator and the Ternary Product* applies to it. In particular the derived operation has the properties that the general theory proves for it, and the article reads off the ones that are explicit for $\mathbb{B}$.

## The Axioms and What They Do Not Force

### The Right Unit

**Proposition.** The element $e_0$ is a **right identity** for the multiplication: $\tilde Q \star e_0 = \tilde Q$ for every $\tilde Q$. It is not a left identity.

**Proof.** The right identity is the second column of the table, $e_\mu \star e_0 = e_\mu$, which is the statement $e^{*}_0 = e_0$ pushed through the product; on a general element it follows by additivity. For the left action, the first row gives $e_0 \star \tilde Q = \tilde Q^{*}$, and this equals $\tilde Q$ for every $\tilde Q$ only if the involution is the identity, which it is not; the witness is $e_0 \star e_1 = -e_1 \neq e_1$. $\square$

**Remark.** The one-sided unit is the mark of the derived operation and appears in the general theory in the same form: the standard sesqualgebra has a right unit and no left one (*Sesqualgebras*). It is not a defect of $\mathbb{B}$ but a consequence of the involution sitting in the second slot; the left action by $e_0$ is the involution itself.

### Neither Associative Nor Commutative

**Theorem.** The multiplication is **neither associative nor commutative**.

**Proof.** The algebra is of full type with respect to the product: it is faithful over $\mathbb{C}$, the products of its elements span it, and no nonzero element annihilates it on the left, since a left annihilator $a$ would satisfy $a = a \star e_0 = 0$ by the right unit. The involution $\varsigma$ of the base is not the identity, and for an algebra of full type with a nontrivial involution the sesquilinear product is never associative, by the collapse theorem of *Sesqualgebras*; the same hypothesis makes it non-commutative, since a commutative product would likewise force $\varsigma = \mathrm{id}$. $\square$

**Witnesses.** Associativity fails on the triple $(e_0,e_1,e_1)$:

$$
(e_0 \star e_1) \star e_1 = (-e_1) \star e_1 = -e_0, \qquad
e_0 \star (e_1 \star e_1) = e_0 \star e_0 = e_0 ,
$$

and the two differ. Commutativity fails on the pair $(e_1,e_2)$: $e_1 \star e_2 = -e_3$ while $e_2 \star e_1 = e_3$.

The failure of associativity is not an accident of the chosen basis, and the two products of $\mathbb{B}$ that are not associative must be told apart. The $\natural$-product fails associativity for want of a two-sided unit and remains $\mathbb{C}$-bilinear; the sesquilinear product fails it while being conjugate-linear in a slot, and the failure is the general collapse of *Sesqualgebras*.

### The Associator

**Definition.** The **associator** of the multiplication is

$$
[\tilde P,\tilde Q,\tilde R] = (\tilde P \star \tilde Q) \star \tilde R - \tilde P \star (\tilde Q \star \tilde R) .
$$

**Proposition.** For the derived operation of an associative algebra with a $\varsigma$-semilinear involution,

$$
[\tilde P,\tilde Q,\tilde R] = \tilde P\bigl((\tilde R\tilde Q)^{*} - \tilde R\tilde Q^{*}\bigr) = \tilde P\bigl(\tilde Q^{*}\tilde R^{*} - \tilde R\tilde Q^{*}\bigr) ,
$$

so the associator is $\mathbb{C}$-linear in $\tilde P$, $\varsigma$-semilinear in $\tilde Q$ and carries the difference of the two parities in $\tilde R$.

**Proof.** The first identity is the general formula of *The Sesquilinear Associator and the Ternary Product* for the derived operation, $\tilde P\bigl((\tilde R\tilde Q)^{*} - \tilde R\tilde Q^{*}\bigr)$; the expansion $(\tilde R\tilde Q)^{*} = \tilde Q^{*}\tilde R^{*}$ is the anti-multiplicativity of ${}^{*}$. The last clause is the parity theorem of the same article: the two groupings are trilinear on two different modules, $(\tilde P\tilde Q) \star \tilde R$ on $\mathbb{B} \times \mathbb{B}^{\varsigma} \times \mathbb{B}^{\varsigma}$ and $\tilde P \star (\tilde Q \star \tilde R)$ on $\mathbb{B} \times \mathbb{B}^{\varsigma} \times \mathbb{B}$, so the associator is not homogeneous in the third slot. $\square$

The associator vanishes exactly when the two groupings agree, that is when the product is associative, and it does not. The quantities that replace it are the ternary product and the two halves of the next section.

## The Involution and the Two Halves

### The Involution Exchanges the Slots

**Proposition.** The involution reverses the multiplication:

$$
(\tilde P \star \tilde Q)^{*} = \tilde Q \star \tilde P .
$$

**Proof.** $(\tilde P\tilde Q^{*})^{*} = \tilde Q\tilde P^{*} = \tilde Q \star \tilde P$, using $*^{2} = \mathrm{id}$ and the anti-multiplicativity of ${}^{*}$. $\square$

**Remark.** The identity is the sesquilinear counterpart of the commutativity of a bilinear product: it does not make the product commutative, since $\tilde Q \star \tilde P$ is the transposed product of *The Sesquilinear Product* and not the value on the same ordered pair, but it does make the involution exchange the two arguments, and it is the reason the two halves below fit together. In the notation of the general theory it is the statement that the product is Hermitian-symmetric with respect to the involution.

### The Two Halves Are the Remarkable Subspaces

**Theorem.** The sets

$$
H(\mathbb{B}) = \{\tilde Q : \tilde Q^{*} = \tilde Q\} , \qquad S(\mathbb{B}) = \{\tilde Q : \tilde Q^{*} = -\tilde Q\}
$$

of Hermitian and skew-Hermitian elements of the sesqualgebra are the Hermitian and the anti-Hermitian subspaces,

$$
H(\mathbb{B}) = \mathbb{M}_+ , \qquad S(\mathbb{B}) = \mathbb{M}_- ,
$$

and they are the fixed and the anti-fixed subspaces of ${}^{*}$; in particular $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ is the Hermitian decomposition of *Decompositions Along the Remarkable Subspaces* and *Introduction to the Remarkable Subspaces*.

**Proof.** The two definitions are the definitions of the fixed and anti-fixed sets of the involution ${}^{*}$ of the algebra, that is, of the Hermitian and the anti-Hermitian subspaces of *Biquaternions as a Vector Space over $\mathbb{C}$*; the decomposition into the two halves is the order-two property of the involution, in the form of *Hermitian and Skew-Hermitian Elements*. $\square$

**Remark.** This is the first place where the sesquilinear reading meets the remarkable subspaces: two of the remarkable subspaces, $\mathbb{M}_+$ and $\mathbb{M}_-$, are the halves that the involution ${}^{*}$ of the sesquilinear datum cuts out, while the other four are the halves of the other conjugations (*Comparison of the Remarkable Subspaces*). The pairing is not an analogy: the fixed and anti-fixed sets of an involution are the two halves of any sesqualgebra, and here they carry their corpus names.

### The Other Exchange, and the Scalar and the Vector Part

The two halves above are the halves of the **involution** ${}^{*}$. The halves of the **exchange** of the two arguments are a second pair, and that exchange comes in two forms.

The **plain exchange** swaps the two arguments, $\tilde{P}\tilde{Q}^{*}\mapsto\tilde{Q}\tilde{P}^{*}$, and the proposition above reads it on the value, $\tilde{Q}\tilde{P}^{*}=(\tilde{P}\tilde{Q}^{*})^{*}$: its symmetric part is the Hermitian part and its antisymmetric part the skew-Hermitian part of the value, valued in $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$. Those two halves are only $\mathbb{R}$-bilinear, since the swap moves the conjugate-linear slot to the other side, and they are the symmetrised sesquilinear product of *The Sesquilinear Symmetrised Product* and the sesquilinear commutator of *The Sesquilinear Commutator*; they are not the two parts named $\mathrm{SPS}$ and $\mathrm{APS}$ of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

The **exchange by the coefficientwise conjugation** $c=\overline{\cdot}$ composes the swap with $c$, $f^{c}(\tilde{P},\tilde{Q})=\overline{f(\tilde{Q},\tilde{P})}$, and it keeps the class: its two parts are sesquilinear over $\mathbb{C}$ again, and they are the scalar part and the vector part of the value,

$$
\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+\overline{\tilde{Q}\tilde{P}^{*}}\bigr)=\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+(\tilde{P}\tilde{Q}^{*})^{\natural}\bigr)=\mathrm{Sc}(\tilde{P}\tilde{Q}^{*}),\qquad
\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}-\overline{\tilde{Q}\tilde{P}^{*}}\bigr)=\mathrm{Vect}(\tilde{P}\tilde{Q}^{*}),
$$

the first central and the second vector-valued. The two readings are the conjugate-symmetric ones of *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, and the biquaternion instance, with the two parts of the other sesqualgebra, is *The 12 Products of the Biquaternion Complex Space*, §*The Other Exchange, and the Class It Keeps*. This reading stays inside the class of this article, and it is the one the twelve names $\mathrm{SPS}$ and $\mathrm{APS}$ belong to; the bare reading is the other, and it leaves the class.

### The Ternary Product

**Theorem.** The ternary product attached to the multiplication is

$$
\{\tilde P,\tilde Q,\tilde R\} = (\tilde P \star \tilde Q) \star \tilde R^{*} = \tilde P\tilde Q^{*}\tilde R ,
$$

and $\mathbb{B}$ with this ternary product is an **algebraic $J^{*}$-algebra**: the operation is additive in each variable, $\mathbb{C}$-linear in the first and the third and conjugate-linear in the second, and satisfies the Jordan triple identity (*Algebraic J\*-Algebras*).

**Proof.** The first equality is the definition of the ternary product of a sesqualgebra, $\{x,y,z\} = (x \star y) \star z^{*}$, and the second is the derived form of *The Sesquilinear Associator and the Ternary Product*; the unital reading $\{\tilde P,\tilde Q,e_0\} = \tilde P \star \tilde Q$ and $\{e_0,\tilde Q,e_0\} = \tilde Q^{*}$ recovers the multiplication and the involution from the ternary product. The axioms are the theorem that the model $xy^{*}z$ of an associative algebra with a sesquilinear involution is an algebraic $J^{*}$-algebra. $\square$

**Remark.** The ternary product is the binary multiplication's surviving form: it is associative-like in the only sense available, its identities hold where the binary ones fail, and it is defined by a formula, $\tilde P\tilde Q^{*}\tilde R$, in which the middle slot carries the involution and the two outer slots do not. The operator form, the Lie triple system and the adjoint are *The Ternary Product as an Operator* and *The Adjoint of the Ternary Product*.

### The Squares and the Positive Cone

**Proposition.** The square of an element in the sesquilinear multiplication is

$$
\tilde Q \star \tilde Q = \tilde Q\tilde Q^{*} ,
$$

it is fixed by the involution ${}^{*}$ for every $\tilde Q$, and its scalar part is the sum of the modulus squares of the coordinates,

$$
\mathrm{Sc}(\tilde Q \star \tilde Q) = \sum_{\mu=0}^{3} Q_\mu\overline{Q_\mu} = \sum_{\mu=0}^{3} |Q_\mu|^{2} ,
$$

a sum fixed by the complex conjugation.

**Proof.** The square is the derived product with equal arguments; it is fixed by ${}^{*}$ because $(\tilde Q\tilde Q^{*})^{*} = \tilde Q\tilde Q^{*}$; and its scalar part is the scalar part $\mathrm{Sc}(\tilde P\tilde Q^{*}) = \sum_\mu P_\mu\overline{Q_\mu}$ of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* at $\tilde P = \tilde Q$, each term $Q_\mu\overline{Q_\mu}$ being fixed by the complex conjugation. $\square$

**Corollary.** The finite sums of the squares $\tilde Q \star \tilde Q$ are the elements of the **algebraic positive cone** $C(\mathbb{B})$ of *Hermitian Squares and the Algebraic Positive Cone*, and $\tilde Q \star \tilde Q = \tilde Q\tilde Q^{*}$ is the element the involution attaches to $\tilde Q$. The cone is generated by the squares of the sesquilinear product as much as by the squares of the involution, the two generating sets coinciding.

**Caution on the two squares.** The square $\tilde Q\tilde Q^{*}$ of the sesquilinear multiplication is not the other square of the algebra, $\tilde Q\tilde Q^{\natural} = \sum_\mu Q_\mu^{2}$, which is built on the $\mathbb{C}$-linear conjugation ${}^{\natural}$, is central, and vanishes exactly on the zero divisors; it is the central scalar on which invertibility turns (*Introduction to the Remarkable Subspaces*). The square $\tilde Q\tilde Q^{*}$ is fixed by the involution ${}^{*}$ and its scalar part is the sum of the modulus squares displayed above. The two agree when all four coordinates are real, that is on the quaternion subspace, where the two conjugations coincide, and differ in general.

## The Sesqualgebra as an Object

### Simplicity

**Theorem.** The only two-sided ideals of the sesqualgebra $(\mathbb{B},\star)$ are $0$ and $\mathbb{B}$.

**Proof.** Let $I$ be a two-sided ideal, so that $\tilde A \star \tilde X \in I$ and $\tilde X \star \tilde A \in I$ for every $\tilde A \in \mathbb{B}$ and $\tilde X \in I$. The first condition with $\tilde A = e_0$ gives $\tilde X^{*} \in I$, so $I$ is stable under the involution; with that, the first condition reads $\mathbb{B}I \subseteq I$, and the second reads $I\mathbb{B} \subseteq I$. Hence $I$ is a two-sided ideal of the ring $\mathbb{B}$, and the ring is simple by *Biquaternion Ideals and Peirce Decomposition*, so $I$ is $0$ or $\mathbb{B}$. $\square$

**Remark.** The sesqualgebra is simple with respect to the multiplication $\star$ although that multiplication is neither associative nor two-sidedly unital, and it is simple for the same underlying reason as the algebra, the simplicity of the ring. In the theory of *Ideals and Quotients of a Sesqualgebra* the ideals here are the two-sided ideals of the algebra, so the answer is the same as the bilinear one.

### The Idempotents of the Multiplication

**Proposition.** An element is idempotent for the sesquilinear multiplication, $\tilde Q \star \tilde Q = \tilde Q$, if and only if it is a Hermitian idempotent of the algebra; hence the idempotents of the multiplication are $0$, $e_0$, and the **pure states**

$$
\tilde\Pi_1(\hat\mu) = \tfrac12\bigl(e_0 + i\hat\mu\bigr) , \qquad \hat\mu \in \mathbb{R}^{3}, \ |\hat\mu| = 1 ,
$$

indexed by the real unit vectors (*Conventions in Mathematics*, *Idempotents of the General Plain Algebra*).

**Proof.** If $\tilde Q \star \tilde Q = \tilde Q$ then $\tilde Q\tilde Q^{*} = \tilde Q$, and applying ${}^{*}$ gives $\tilde Q\tilde Q^{*} = \tilde Q^{*}$ because the square is Hermitian, so $\tilde Q = \tilde Q^{*}$; hence $\tilde Q\tilde Q^{*} = \tilde Q^{2}$ and $\tilde Q$ is an idempotent of the algebra, Hermitian. Conversely a Hermitian idempotent satisfies $\tilde Q \star \tilde Q = \tilde Q\tilde Q^{*} = \tilde Q^{2} = \tilde Q$. The Hermitian idempotents of $\mathbb{B}$ are classified in *Idempotents of the General Plain Algebra*: the idempotents are the elements $\tfrac12(e_0 + \xi i)$ with $\xi$ a root of $-1$, and the Hermitian ones are those of the **real root** family, $\xi = \pm\mu$ with $\mu$ a unit pure real quaternion, that is the elements $\tfrac12(e_0 \pm \mu i)$, together with the trivial idempotents $0$ and $e_0$. $\square$

**Remark.** The unit $e_0$ is idempotent on both sides, and each $\tilde\Pi_1(\hat\mu)$ is idempotent for the multiplication while being a Hermitian idempotent of the algebra, a pure state of *Idempotents of the General Plain Algebra*; the sesquilinear multiplication therefore has the same idempotents as the algebra has Hermitian ones, and none besides. The idempotents of the algebra that are not Hermitian, the non-trivial-root family of *Idempotents of the General Plain Algebra*, are **not** idempotent for the multiplication.

## The Four General Products and the Sesquilinear Structure

### Which of the Four Is a Sesquilinear Multiplication

The row of the table of *Comparison Between the Four General Products* headed "multiplication of a sesqualgebra over $\mathbb{C}$" is read with the definition of *Sesqualgebras* and with nothing added to it. That definition is the two scalar rules: a sesqualgebra is an $R$-module with a product additive in each variable, $R$-linear in the first and $\varsigma$-semilinear in the second. Over $(\mathbb{C},\varsigma)$ with the conjugation $\varsigma(z)=\bar z$ the rules are

$$
(\lambda\tilde P)\star\tilde Q = \lambda(\tilde P\star\tilde Q), \qquad
\tilde P\star(\lambda\tilde Q) = \bar\lambda(\tilde P\star\tilde Q).
$$

The general plain sesquilinear product satisfies them by its definition, and the general quaternionic sesquilinear product satisfies them too: its first slot is read through the $\mathbb{C}$-linear conjugation ${}^{\natural}$, which the first rule does not see, and its second slot carries the star, which supplies the conjugation of the second rule. **Both products carrying the star are therefore multiplications of a sesqualgebra over $\mathbb{C}$ with the conjugation**, and the row of the comparison table reads no, no, yes, yes; the two bilinear products are sesqualgebras as well, for the trivial involution, which is the collapse of §*The Collapse at the Identity* of *Sesqualgebras* and the bilinear row of the same table. The definition alone therefore does not select the product of this article.

What does select it is a sharper property, and it is the property the corpus's own standard example carries: the product must be the **derived operation** $\tilde X\star\tilde Y=\tilde X\tilde Y^{*}$ of the associative algebra $\mathbb{B}$ with its conjugate-linear involution. That is a statement about the algebra and its involution and not about the scalar rules, and among the four general products it holds for the general plain sesquilinear product alone. The rest of this section states and proves it.

**Definition.** Let $\star$ be one of the four general products. Put

$$
\sigma(\tilde Y) = e_0 \star \tilde Y ,
$$

the first row of $\star$ read on $\tilde Y$. Then $\star$ is the **derived operation** of the algebra $\mathbb{B}$ with the conjugate-linear involution $\sigma$ when the two conditions hold:

(i) $\sigma$ is a conjugate-linear **involution** of the algebra, that is $\sigma(\lambda\tilde Y) = \bar\lambda\,\sigma(\tilde Y)$, $\sigma^2 = \mathrm{id}$, $\sigma(\tilde X\tilde Y) = \sigma(\tilde Y)\sigma(\tilde X)$ and $\sigma(e_0) = e_0$;

(ii) $\sigma$ rebuilds $\star$, that is $\tilde X \star \tilde Y = \tilde X\,\sigma(\tilde Y)$ for all $\tilde X,\tilde Y$.

Condition (i) says that $\sigma$ is an involution of the algebra of the kind ${}^{*}$ and not of the kind ${}^{\natural}$ (*The Group of Involutions*, *Introduction to the General Plain Algebra of Biquaternions*); condition (ii) says that $\star$ is the multiplication with that involution inserted in the second slot and the first factor untouched. Together they are the statement that $\star$ is the derived operation of *Sesqualgebras*, and $\sigma$ is then the involution of the definition and is **determined** by $\star$, being its first row.

**Theorem (the derived operation among the four).** Among the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, the general plain sesquilinear product is the only one that is the derived operation of $\mathbb{B}$ with a conjugate-linear involution, and the involution is ${}^{*}$. The general quaternionic sesquilinear product is a multiplication of a sesqualgebra over $\mathbb{C}$ all the same, and it is not of this derived form.

**Proof.** The four first rows are read from the products themselves, and they are $\sigma = \mathrm{id}$ for $\tilde X\tilde Y$, $\sigma = \mathrm{id}$ for $\tilde X^{\natural}\tilde Y$ because ${}^{\natural}$ fixes $e_0$ and so $e_0 \star \tilde Y = e_0^{\natural}\tilde Y = \tilde Y$, and $\sigma = {}^{*}$ for both $\tilde X\tilde Y^{*}$ and $\tilde X^{\natural}\tilde Y^{*}$, because $e_0 \star \tilde Y = e_0^{\natural}\tilde Y^{*} = \tilde Y^{*}$ in either case. The two conditions then separate the four:

| product | $\sigma$ (first row) | (i) | (ii) |
|---|---|---|---|
| $\tilde X\tilde Y$ | $\mathrm{id}$ | no | yes |
| $\tilde X^{\natural}\tilde Y$ | $\mathrm{id}$ | no | no |
| $\tilde X\tilde Y^{*}$ | ${}^{*}$ | yes | yes |
| $\tilde X^{\natural}\tilde Y^{*}$ | ${}^{*}$ | yes | no |

*Condition (i).* The identity is not conjugate-linear, since $\sigma(\lambda\tilde Y) = \lambda\tilde Y \neq \bar\lambda\tilde Y$ for a non-real $\lambda$ and $\tilde Y \neq 0$; and ${}^{\natural}$ is $\mathbb{C}$-linear by construction (*Introduction to the General Plain Algebra of Biquaternions*). So the two products whose first row is the identity fail (i) on the first clause, and the two products carrying the star pass it, the star being conjugate-linear, involutive, anti-multiplicative and fixing $e_0$ (*The Group of Involutions*, *Introduction to the General Plain Algebra of Biquaternions*).

*Condition (ii).* With $\tilde X = e_0$, condition (ii) says that $e_0$ is a **right** unit of $\star$, in the form $e_0 \star \tilde Y = \sigma(\tilde Y)$; and with $\sigma$ fixed it says that $\star$ is the algebra product with $\sigma$ inserted in the second slot. For the general plain sesquilinear product this is the definition of the rule and holds. For the general quaternionic sesquilinear product it would read $\tilde X^{\natural}\tilde Y^{*} = \tilde X\tilde Y^{*}$, and at $\tilde Y = e_0$ this is $\tilde X^{\natural} = \tilde X$ for every $\tilde X$, which fails at $\tilde X = e_1$; equivalently the fourth product has no right unit, $e_1 \star^{\natural} e_0 = e_1^{\natural} = -e_1$. For the $\natural$-product, (ii) with $\sigma = \mathrm{id}$ would read $\tilde X^{\natural}\tilde Y = \tilde X\tilde Y$, which already fails at $\tilde X = e_1$ and $\tilde Y = e_0$.

Hence only the general plain sesquilinear product satisfies (i) and (ii). $\square$

**Corollary (the row of the comparison table).** The two rows of *Comparison Between the Four General Products* that name the categories record the definitional facts, and they read yes, yes, no, no for the bilinear row and no, no, yes, yes for the sesquilinear one: the two star-products are **both** multiplications of a sesqualgebra over $\mathbb{C}$ with the conjugation, and the definition does not separate them. The property proved here is sharper and does separate them, reading no, no, yes, no. The three failures fall on different clauses, which is why both conditions are needed: the general plain bilinear product satisfies (ii) and fails (i) alone, the $\natural$-product fails both, and the general quaternionic sesquilinear product passes (i) and fails (ii) alone — it carries the right conjugation in the second slot but twists the first slot by ${}^{\natural}$ as well, so it is not the derived operation, and the two products carrying the star share the first row $\sigma = {}^{*}$. Equivalently, the two are separated by the unit, which is the row "$1$ is a right identity" of the same table: $e_0$ is a right unit of the general plain sesquilinear product and there is none for the complex quaternionic one.

**Corollary (the caution on ${}^{\natural}$).** The conjugation that makes a product sesquilinear is the conjugate-linear involution ${}^{*} = \bar{\cdot}\circ{}^{\natural}$, not the $\mathbb{C}$-linear ${}^{\natural}$. The map ${}^{\natural}$ fixes the complex scalars, so it is invisible to the scalar rules: a slot conjugated by ${}^{\natural}$ is still $\mathbb{C}$-linear, and this is why a product twisted by ${}^{\natural}$ in the first slot is still sesquilinear while the star must stay in the second slot: a second slot carrying ${}^{\natural}$ instead of the star makes the product bilinear. A sesquilinear structure over $\mathbb{C}$ with its conjugation therefore rests on the star, the involution of the algebra; a product whose second slot carries ${}^{\natural}$ instead of the star is bilinear, and it is the bilinear structure of *Introduction to the General Plain Algebra of Biquaternions*.

### The Scalar Part of the Multiplication

**Proposition.** The scalar part of the multiplication is

$$
\mathrm{Sc}(\tilde P \star \tilde Q) = \mathrm{Sc}(\tilde P\tilde Q^{*}) = \sum_{\mu=0}^{3} P_\mu\overline{Q_\mu} ,
$$

conjugate-linear in its second argument, and the multiplication is that scalar part read coefficientwise against the basis,

$$
\tilde P\tilde Q^{*} = \sum_{\mu=0}^{3}\sum_{\nu=0}^{3}\varepsilon_\nu P_\mu\overline{Q_\nu}\,e_\mu e_\nu .
$$

**Proof.** The scalar part of the derived product is read on the coordinates by the displayed scalar–vector form of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, $\mathrm{Sc}(\tilde P\tilde Q^{*}) = \sum_\mu P_\mu\overline{Q_\mu}$, conjugate-linear in the second argument; the second display is the coordinate rule of the definition, whose coefficients $\varepsilon_\nu P_\mu\overline{Q_\nu}$ are that scalar part read on each basis pair. $\square$

**Remark.** The scalar part and the multiplication are two readings of one datum, and the article separates them deliberately: the scalar part of the product, whatever is made of it later, is not the object here, and the multiplication is. The scalar part alone does not determine the product, and it is the involution that turns the pairings of the coordinates into the multiplication; conversely the product determines the involution, hence the scalar part, together.

**Remark (the scalar part is a product of the same class).** Under the exchange by the coefficientwise conjugation the scalar part is the **conjugate-symmetric part** of the multiplication, $\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+(\tilde{P}\tilde{Q}^{*})^{\natural}\bigr)=\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$, so it is a product in the same sense as the multiplication, sesquilinear over $\mathbb{C}$ and not merely $\mathbb{R}$-bilinear, with the vector part $\mathrm{Vect}(\tilde{P}\tilde{Q}^{*})$ as its antisymmetric partner; §*The Other Exchange, and the Scalar and the Vector Part*. It is not the symmetrisation of the multiplication, which is Hermitian-valued in $\mathbb{M}_{+}$ and only $\mathbb{R}$-bilinear (*The Sesquilinear Symmetrised Product*).

## The Reading in the Physics Band

The block is the algebraic home of the pairing of two quantum roles. Its two slots are not interchangeable: the first reads its element plainly and the second through the Hermitian conjugation, so the multiplication pairs an element with the adjoint of another. Its scalar part, $\mathrm{Sc}(\tilde P\tilde Q^{*}) = \sum_\mu P_\mu\overline{Q_\mu}$ of §*The Scalar Part of the Multiplication*, is the Hermitian form the physics band writes $H$. The one-sided unit is that asymmetry seen on the identity, the left action by $e_0$ being the involution itself.

The readings are these, and each belongs to the physics article named; this article stops at the algebra. The square $\tilde Q\tilde Q^{*}$ — its positivity, its determinant and its rank — is read as probability, as the interval and as a count of polarisations in *Mass, Rank and the Positivity of the Dagger*. The one-sided unit and the involution sitting in the second slot are read as the state/observable asymmetry and as the internal gauge action in *Observables, Gauge Generators and the Chirality of the Internal Action*. The ternary product $\tilde P\tilde Q^{*}\tilde R$ and its associator are read as a three-field coupling and its order dependence in *Particle Types, Discrete Charge and Three-Particle Couplings*.

## Summary

The general plain sesquilinear product $\tilde P\tilde Q^{*}$ of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, read as a multiplication, is additive in each variable, $\mathbb{C}$-linear in the first and conjugate-linear in the second. Those are the two axioms of a sesqualgebra over $\mathbb{C}$ with its conjugation, and the product is the derived operation of the associative algebra $\mathbb{B}$ with its conjugate-linear involution ${}^{*}$.

$$
\boxed{\ \text{With the general plain sesquilinear product, } \mathbb{B} \text{ is a sesquilinear } \mathbb{C}\text{-algebra, neither associative nor commutative, with a right unit and the involution } {}^{*}. \ }
$$

The product has the unit $e_0$ on the right and none on the left, the left action by $e_0$ being the involution; it is neither associative nor commutative, by the collapse theorem, with the witnesses $(e_0,e_1,e_1)$ and $(e_1,e_2)$; the involution exchanges the two slots, $(\tilde P \star \tilde Q)^{*} = \tilde Q \star \tilde P$; the Hermitian and skew-Hermitian elements are the two remarkable subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$; the ternary product $\tilde P\tilde Q^{*}\tilde R$ makes $\mathbb{B}$ an algebraic $J^{*}$-algebra and recovers the multiplication and the involution by inserting the unit; the square $\tilde Q \star \tilde Q$ is fixed by the involution and its scalar part is the sum of the modulus squares of the coordinates; the two-sided ideals are $0$ and $\mathbb{B}$; and the idempotents of the multiplication are the Hermitian idempotents of the algebra.

Among the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, **both** products carrying the star are multiplications of a sesqualgebra over $\mathbb{C}$ with the conjugation, and the general plain sesquilinear product is the only one that is the **derived operation** $\tilde X\star\tilde Y=\tilde X\tilde Y^{*}$ of $\mathbb{B}$ with the conjugate-linear involution ${}^{*}$, in the sense of the two conditions (i) and (ii) of §*Which of the Four Is a Sesquilinear Multiplication*. The general quaternionic sesquilinear product shares the involution in the second slot and fails (ii), reading the first factor through the $\mathbb{C}$-linear ${}^{\natural}$ as well, and equivalently it has no right unit; the two bilinear products have $\sigma = \mathrm{id}$ and fail (i). The conjugation that does this is the star, the conjugate-linear involution; the natural sign ${}^{\natural}$ is $\mathbb{C}$-linear, so a second slot carrying it gives a bilinear product, which is the caution of *Sesqualgebras* made explicit on the biquaternion algebra. The row of *Comparison Between the Four General Products* that names the sesquilinear kind is read with the definition and not with the derived form, and it holds for both star-products; the derived form is the sharper property proved in this article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | the biquaternion algebra, read here with the sesquilinear multiplication |
| $e_0,e_1,e_2,e_3$ | complex basis; $e_0$ the unit, $e_k$ the quaternion units |
| $i$ | central scalar imaginary, $i^2=-1$ |
| $\tilde Q = Q_0e_0 + \mathbf Q$ | a biquaternion and its scalar–vector split |
| $\varsigma(z) = \bar z$ | the base involution, the complex conjugation |
| ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ | the Hermitian conjugation, the conjugate-linear involution of the algebra |
| $\sigma(\tilde Y) = e_0 \star \tilde Y$ | the first row of a product, the involution of the derived operation |
| $\tilde P \star \tilde Q = \tilde P\tilde Q^{*}$ | the general plain sesquilinear product, the multiplication of the sesqualgebra |
| $\varepsilon = (1,-1,-1,-1)$ | the signs of the involution on the basis, $e^{*}_\nu = \varepsilon_\nu e_\nu$ |
| $[\tilde P,\tilde Q,\tilde R]$ | the associator, $(\tilde P \star \tilde Q) \star \tilde R - \tilde P \star (\tilde Q \star \tilde R)$ |
| $\{\tilde P,\tilde Q,\tilde R\} = \tilde P\tilde Q^{*}\tilde R$ | the ternary product, the $J^{*}$-structure |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the Hermitian and the anti-Hermitian halves, $H(\mathbb{B})$ and $S(\mathbb{B})$ |
| $C(\mathbb{B})$ | the algebraic positive cone, the sums of the squares $\tilde Q \star \tilde Q$ |
| $\tilde\Pi_1(\hat\mu) = \tfrac12(e_0+i\hat\mu)$ | the idempotents of the multiplication, $\hat\mu$ a real unit vector |

## Further Reading

- Irving Kaplansky, *Rings of Operators* (Benjamin, 1968), for the $J^{*}$-algebras and the ternary product $xy^{*}z$ that the derived operation defines.
- Harald Hanche-Olsen and Erling Størmer, *Jordan Operator Algebras* (Pitman, 1984), for the Jordan triple identity and the model of an involutive algebra.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. I (Academic Press, 1983), for the adjoint, the Hermitian and the skew-Hermitian elements and the positive cone.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the $\varsigma$-semilinear involutions and the derived operation.
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the product, its coordinate rule and its scalar–vector form.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table that decides which of the four general products is a sesquilinear multiplication.
- *Sesqualgebras* (`articles_maths/sesqualgebras.md`), for the axioms, the collapse theorem and the standard example.
