# __Introduction to the General Quaternionic Sesqualgebra of Biquaternions__

## Introduction

The underlying $\mathbb{C}$-vector space of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products, defined side by side in *The Four General Products of the Biquaternion $\mathbb{C}$ Space*. Two of the four are the multiplication of an algebra over $\mathbb{C}$ in the broad sense, the two whose second slot is read without a conjugation, and two are the multiplication of a **sesqualgebra** over $\mathbb{C}$ with its conjugation as base involution, the two whose second slot carries the star; the first reading of each pair is *Introduction to the General Plain Algebra of Biquaternions* and *Introduction to the General Plain Sesqualgebra of Biquaternions*, and the second reading of each pair is the isotope of the first by the natural conjugation. This article is the fourth reading: the **general quaternionic sesquilinear product** $\tilde P^{\natural}\tilde Q^{*}$ is additive in each variable, $\mathbb{C}$-linear in the first and conjugate-linear in the second, so it satisfies the two scalar rules of *Sesqualgebras* and is the multiplication of a sesqualgebra over the conjugation, and it is the product of the four that fails to be the **derived operation** $\tilde X\star\tilde Y=\tilde X\tilde Y^{*}$ of the algebra with its involution.

The consequences differ from the sibling reading in every place where the first slot matters. There the product is the derived operation, the unit is a right unit, the involution exchanges the two slots, the idempotents are the Hermitian idempotents of the algebra, the squares generate the algebraic positive cone and the ternary product is an algebraic $J^{*}$-algebra. Here the product carries the $\mathbb{C}$-linear ${}^{\natural}$ in the first slot as well: **there is no unit on either side**, the two one-sided actions of $e_0$ being the two conjugations of the algebra; the involution does not exchange the slots, and what it produces instead is the plain product in the reversed order; the idempotents are not the Hermitian ones, and they form a two-parameter family in the quaternion subspace; the square is not fixed by the involution in general and its scalar part carries the signs of the four coordinates, the three vector squares entering negatively; and the ternary product, although it has the parity of an algebraic $J^{*}$-algebra, **fails the Jordan triple identity**. The article is therefore the record of what the sesquilinear axioms alone force, read on the product of the four that fails to be the derived one.

The boundaries are stated at once. The product is not defined here, and neither are the four general products as a family: the coordinate rule and the four names are *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, the identities that link the four general products are *Relations Between the Four General Products*, and their properties are compared in *Comparison Between the Four General Products*, whose sesquilinear row is the one read below. The other three readings and the general theory that each of them uses are the three articles *Introduction to the General Plain Algebra of Biquaternions*, *Introduction to the General Plain Sesqualgebra of Biquaternions* and *Introduction to the General Quaternionic Algebra of Biquaternions*, and nothing of theirs is repeated here; where the present product differs from the general plain sesquilinear one, the difference is stated and the sibling is named. The elements, the basis, the conjugations and the remarkable subspaces are *Biquaternions as a Vector Space over $\mathbb{C}$*, *Introduction to the Remarkable Subspaces*, *Decompositions Along the Remarkable Subspaces* and *Comparison of the Remarkable Subspaces*, the two halves cut out by the involution being the subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ of *Hermitian and Skew-Hermitian Elements*. On the biquaternion side, the units and the invertibility criterion are read in the same article, the zero divisors are *Biquaternion Zero Divisors*, the idempotents of the algebra are *Biquaternion Idempotents and Projections*, the simplicity of the ring is *Biquaternion Ideals and Peirce Decomposition*, and the two bilinear articles are the ones named in the sentence above. The general theory is the sesquilinear block: the definition is *Sesqualgebras*, the calculus of the product is *The Sesquilinear Product*, the associator and the ternary product are *The Sesquilinear Associator and the Ternary Product*, the abstract ternary system is *Algebraic J\*-Algebras*, the operator readings are *The Ternary Product as an Operator* and *The Adjoint of the Ternary Product*, the two halves are *Hermitian and Skew-Hermitian Elements*, and the ideals are *Ideals and Quotients of a Sesqualgebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra, with basis $e_0,e_1,e_2,e_3$ and central scalar imaginary $i$, $i^2=-1$; a general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. Throughout, an element is written $\tilde Q=Q_0e_0+\mathbf Q$ with $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$, and $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$ and $\mathbf P\times\mathbf Q$ are the complex bilinear dot and cross products of the vector parts. The conjugations are the natural one ${}^{\natural}$, which keeps the scalar coordinate and negates the three vector coordinates, the coefficientwise one $\bar{\cdot}$, which conjugates the four coefficients, and the star ${}^{*}=\bar{\cdot}\circ{}^{\natural}={}^{\natural}\circ\bar{\cdot}$, with $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ and $\varepsilon=(1,-1,-1,-1)$. The base involution of the sesqualgebra is the complex conjugation $\varsigma(z)=\bar z$. The plain product is written $\tilde P\tilde Q$, the general plain sesquilinear product of the sibling article is written $\tilde P\tilde Q^{*}$, and the product of this article is written $\star$, with

$$
\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}
$$

throughout. The four general products and their notation are those of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*.

## The Product Read as a Multiplication

### The Rule

**Definition.** The **multiplication** of the sesqualgebra is the rule

$$
\star \; : \; \mathbb{B}\times\mathbb{B}\longrightarrow\mathbb{B} , \qquad
(\tilde P,\tilde Q)\longmapsto \tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}=\sum_{\mu=0}^{3}\sum_{\nu=0}^{3}\varepsilon_\mu\varepsilon_\nu P_\mu\overline{Q_\nu}\,e_\mu e_\nu ,
$$

the general quaternionic sesquilinear product of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*; each of the sixteen products $e_\mu e_\nu$ is a basis element up to sign, so the double sum is a complex combination of $e_0,\dots,e_3$ and the rule is a map into $\mathbb{B}$ and is well defined. On the four coordinates it reads

$$
\tilde P\star\tilde Q=\bigl(P_0\overline{Q_0}-P_1\overline{Q_1}-P_2\overline{Q_2}-P_3\overline{Q_3}\bigr)
+\bigl(-P_0\overline{Q_1}-P_1\overline{Q_0}+P_2\overline{Q_3}-P_3\overline{Q_2}\bigr)e_1
+\bigl(-P_0\overline{Q_2}-P_1\overline{Q_3}-P_2\overline{Q_0}+P_3\overline{Q_1}\bigr)e_2
+\bigl(-P_0\overline{Q_3}+P_1\overline{Q_2}-P_2\overline{Q_1}-P_3\overline{Q_0}\bigr)e_3 ,
$$

The rule is the general plain sesquilinear product with the first factor read through the $\mathbb{C}$-linear ${}^{\natural}$ as well, which is the insertion that will turn out to change every property that involves the first slot.

### The Scalar–Vector Form

Collecting the scalar part and the vector part of the two elements, the vector part of the first negated and that of the second read through the coefficientwise conjugate, the same product reads

$$
\tilde P\star\tilde Q=\bigl(P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})\bigr)-P_0\overline{\mathbf Q}-\overline{Q_0}\mathbf P+\mathbf P\times\overline{\mathbf Q} .
$$

Both displays are quoted from *The Four General Products of the Biquaternion $\mathbb{C}$ Space*; its scalar part is $\mathrm{Sc}(\tilde P\star\tilde Q)=\sum_{\mu=0}^{3}\varepsilon_\mu P_\mu\overline{Q_\mu}$ with $\varepsilon=(1,-1,-1,-1)$.

### The Two Scalar Rules

**Proposition.** The multiplication is **additive in each variable**; it is $\mathbb{C}$-**linear in the first** variable and $\varsigma$-**semilinear in the second**, with $\varsigma(z)=\bar z$:

$$
(\lambda\tilde P)\star\tilde Q=\lambda\,(\tilde P\star\tilde Q) , \qquad
\tilde P\star(\lambda\tilde Q)=\bar\lambda\,(\tilde P\star\tilde Q) , \qquad \lambda\in\mathbb{C} , \qquad
(\tilde P+\tilde R)\star\tilde Q=\tilde P\star\tilde Q+\tilde R\star\tilde Q .
$$

**Proof.** The coordinates of the developed form are sums of terms $P_\mu\overline{Q_\nu}$ with fixed coefficients, so they are additive and $\mathbb{C}$-linear in the four coordinates of $\tilde P$ alone and additive and conjugate-linear in the four coordinates of $\tilde Q$ alone. The three displays are that statement read coordinate by coordinate; the natural conjugation is $\mathbb{C}$-linear and contributes no conjugation. $\square$

**Corollary.** The product is a multiplication of a **sesqualgebra** over $(\mathbb{C},\varsigma)$ in the sense of *Sesqualgebras*: the two axioms are the two scalar rules and nothing else is assumed, no associativity, no commutativity and no two-sided unit being among them (*The Sesquilinear Product*). The product belongs to the sesquilinear row of *Comparison Between the Four General Products*, which reads yes there, and it is one of the two of the four that do.

### The Multiplication Table

**Proposition.** The products of the basis elements are $e_\mu\star e_\nu=\varepsilon_\mu\varepsilon_\nu\,e_\mu e_\nu$, and they are

| $\star$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $-e_1$ | $-e_2$ | $-e_3$ |
| $e_1$ | $-e_1$ | $-e_0$ | $e_3$ | $-e_2$ |
| $e_2$ | $-e_2$ | $-e_3$ | $-e_0$ | $e_1$ |
| $e_3$ | $-e_3$ | $e_2$ | $-e_1$ | $-e_0$ |

**Proof.** Read from the rule: $e_\mu\star e_\nu=\varepsilon_\mu(e_\mu)^{\natural}\,\varepsilon_\nu(e_\nu)^{*}=\varepsilon_\mu\varepsilon_\nu\,e_\mu e_\nu$, and the entries are the products of the quaternion units, multiplied by the two signs. $\square$

The table differs from the $\natural$-bilinear table of *Introduction to the General Quaternionic Algebra of Biquaternions* in one block: its first row and its first column are both the negated basis, $e_0\star e_\nu=-e_\nu$ and $e_\mu\star e_0=-e_\mu$ for $\mu,\nu\neq0$ with $e_0\star e_0=e_0$, while there the first row was the identity row; and its three-by-three block is the quaternion table itself and not its negative. The whole difference is the star in the second slot, which negates the vector units there and leaves the scalar unit alone.

### The Product Is Not the Derived Operation

**Theorem.** The general plain sesquilinear product $\tilde P\tilde Q^{*}$ is the **derived operation** of $\mathbb{B}$ read as the associative algebra with its conjugate-linear involution ${}^{*}$, and the general quaternionic sesquilinear product is not: in the notation of *Sesqualgebras*, the map $\sigma(\tilde Y)=e_0\star\tilde Y$ satisfies condition (i), being the involution ${}^{*}$ itself, and fails condition (ii), so that no involution of the algebra makes the product the value of the plain product on a conjugated pair.

**Proof.** The first clause is the theorem of *Introduction to the General Plain Sesqualgebra of Biquaternions*, and it is repeated here only to fix the comparison. For the second, $e_0\star\tilde Y=e_0^{\natural}\tilde Y^{*}=\tilde Y^{*}$, so $\sigma={}^{*}$, which is conjugate-linear and involutive, and (i) holds; condition (ii) would read $\tilde P^{\natural}\tilde Q^{*}=\tilde P\tilde Q^{*}$ for every pair, and at $\tilde Q=e_0$ this is $\tilde P^{\natural}=\tilde P$ for every $\tilde P$, which fails at $\tilde P=e_1$, where the two sides are $-e_1$ and $e_1$. Equivalently the product has no right unit, as the next section shows, and the sibling article records that the failure of (ii) is the same statement. $\square$

**Corollary.** The product is the **isotope** of the derived operation by the natural conjugation: $\tilde P\star\tilde Q=\natural(\tilde P)\,\tilde Q^{*}$, with $\natural$ the $\mathbb{C}$-linear anti-automorphism and bijection of §*The Isotope Reading*. The two sesquilinear products of the four are therefore the derived operation and its $\natural$-isotope, exactly as the two bilinear products are the plain multiplication and its $\natural$-isotope, and in both pairs the second is the first with the $\mathbb{C}$-linear insertion that the *derived operation* test rejects (*Comparison Between the Four General Products*, *Which of the Four Is a Sesquilinear Multiplication*).

## The Two Actions of the Unit

### The Left Action Is the Star

**Proposition.** The unit acts on the left by the involution: $e_0\star\tilde Q=\tilde Q^{*}$ for every $\tilde Q$. In particular $e_0$ is not a left unit, and the map $\tilde Q\mapsto e_0\star\tilde Q$ is conjugate-linear, being the star.

**Proof.** $e_0^{\natural}=e_0$, so $e_0\star\tilde Q=e_0\tilde Q^{*}=\tilde Q^{*}$, and the star is conjugate-linear and not the identity. $\square$

### The Right Action Is the Natural Conjugation

**Proposition.** The unit acts on the right by the natural conjugation: $\tilde P\star e_0=\tilde P^{\natural}$ for every $\tilde P$. In particular $e_0$ is not a right unit.

**Proof.** $e_0^{*}=e_0$, so $\tilde P\star e_0=\tilde P^{\natural}e_0=\tilde P^{\natural}$, and $\natural$ is not the identity. $\square$

### No Unit on Either Side

**Proposition.** The multiplication has **no unit on either side**.

**Proof.** A left unit $\tilde E$ satisfies $\tilde E\star\tilde Q=\tilde Q$ for every $\tilde Q$, and at $\tilde Q=e_0$ this reads $\tilde E\star e_0=\tilde E^{\natural}=e_0$, whence $\tilde E=e_0$; but $e_0\star e_1=e_1^{*}=-e_1\neq e_1$, so $e_0$ is not a left unit and there is none. A right unit $\tilde E$ satisfies $\tilde P\star\tilde E=\tilde P$ for every $\tilde P$, and at $\tilde P=e_0$ this reads $e_0\star\tilde E=\tilde E^{*}=e_0$, whence $\tilde E=e_0$; but $e_1\star e_0=e_1^{\natural}=-e_1\neq e_1$, so $e_0$ is not a right unit either. $\square$

**Remark.** The two one-sided actions of $e_0$ are the two conjugations of the algebra, ${}^{*}$ on the left and ${}^{\natural}$ on the right, and no element plays the part of a unit on either side; this is the sharpest single difference from the sibling product, where the first of the two actions is the identity and $e_0$ is a right unit. The comparison of the four records it in the row "$1$ is a right identity", which reads yes only for the general plain sesquilinear product and no for the two $\natural$-products, and it is the reason the same article excludes the fourth product from the derived operation.

## The Axioms and What They Do Not Force

### Neither Associative Nor Commutative

**Theorem.** The multiplication is neither associative nor commutative; a sesqualgebra of full type with a nontrivial involution is never associative, by the collapse theorem of *Sesqualgebras*, and $\mathbb{B}$ is of full type.

**Proof of the collapse, quoted.** If a product satisfying the two scalar rules with a nontrivial $\varsigma$ is associative, then the two scalar rules for $\lambda$ and associativity applied to $\lambda(\tilde P\tilde Q)=(\lambda\tilde P)\tilde Q=\tilde P(\lambda\tilde Q)$ force the involution to be trivial on the scalars that act; the argument is *The Collapse at the Identity* of *Sesqualgebras*, and it is the same for the sibling product. Two witnesses settle the two axioms here directly: $(e_0\star e_1)\star e_1=(-e_1)\star e_1=e_0$ while $e_0\star(e_1\star e_1)=e_0\star(-e_0)=-e_0$, so the product is not associative; and $e_1\star e_2=e_3$ while $e_2\star e_1=-e_3$, so it is not commutative. $\square$

### The Associator

**Proposition.** The associator of the multiplication,

$$
[\tilde P,\tilde Q,\tilde R]=(\tilde P\star\tilde Q)\star\tilde R-\tilde P\star(\tilde Q\star\tilde R) ,
$$

is

$$
[\tilde P,\tilde Q,\tilde R]=\overline{\tilde Q}\,\tilde P\,\tilde R^{*}-\tilde P^{\natural}\,\tilde R\,\overline{\tilde Q} .
$$

**Proof.** Two identities of §*The Star of a Product* are used: $(\tilde A\star\tilde B)^{*}=\tilde B\overline{\tilde A}$ and $(\tilde A\star\tilde B)^{\natural}=\overline{\tilde B}\tilde A$. Hence $(\tilde P\star\tilde Q)\star\tilde R=(\tilde P\star\tilde Q)^{\natural}\tilde R^{*}=\overline{\tilde Q}\tilde P\tilde R^{*}$ on the one hand, and $\tilde P\star(\tilde Q\star\tilde R)=\tilde P^{\natural}(\tilde Q\star\tilde R)^{*}=\tilde P^{\natural}\tilde R\overline{\tilde Q}$ on the other, and the difference of the two is the associator displayed. $\square$

**Remark.** The associator is a sum of two terms of opposite parity in the second variable and the same parity in the first and the third, and it vanishes under none of the standard hypotheses; the product has no identity on either side, so the associator is not the instrument of an associativity theory for this algebra, and the structural object that survives is the ternary product of §*The Ternary Product*.

**Remark (the witnesses and the count).** The associator is nonzero on $256$ of the $512$ triples of the eight-element basis, at the clean witnesses $(e_0,e_0,e_1)$ and $(e_0,e_1,e_1)$, where the display gives

$$
[e_0,e_0,e_1]=-2e_1,\qquad [e_0,e_1,e_1]=2e_0 .
$$

The two witnesses show that the associator is **not confined to one grade**: one value is pure vector and the other pure scalar, so the defect of composition is neither a purely central shift nor a purely vectorial one, unlike the defects of the antisymmetric half, which are pure vector. Recomputed on the basis; the count is a count on a basis and not an invariant.

### The Flexibility and the Degree-Three Identity

**Proposition.** The multiplication is **not flexible** and **not power associative**.

**Proof.** The flexible law $(\tilde P\star\tilde Q)\star\tilde P=\tilde P\star(\tilde Q\star\tilde P)$ fails at $\tilde P=ie_0$, $\tilde Q=e_0$, where the two sides are $e_0$ and $-e_0$ (*Comparison Between the Four General Products*); and the degree-three identity $\tilde P\star(\tilde P\star\tilde P)=(\tilde P\star\tilde P)\star\tilde P$ fails at $\tilde P=ie_3$, where the two sides are $ie_3$ and $-ie_3$. $\square$

**Remark.** The witness of the degree-three identity is the same one the comparison records for this product, and it is worth reading: $\tilde P=ie_3$ is not a zero divisor and $\tilde P\star\tilde P=-e_0$ is a scalar, so the two bracketings of the triple product differ by the star in the second slot acting on the scalar line, which is the single place where the conjugation in that slot bites.

### The Algebra Structure

**Theorem.** With the general quaternionic sesquilinear product as its multiplication, $\mathbb{B}$ is a four-dimensional **sesqualgebra over $(\mathbb{C},\varsigma)$** in the sense of *Sesqualgebras* — additive in each variable, $\mathbb{C}$-linear in the first and $\varsigma$-semilinear in the second — with no unit on either side; it is neither associative nor commutative, neither flexible nor power associative, and it is not the derived operation of the algebra with its involution.

**Proof.** The product is a sesquilinear binary operation on the $\mathbb{C}$-vector space $\mathbb{B}$, which is the definition of a sesqualgebra over the pair $(\mathbb{C},\varsigma)$, and the remaining clauses are the propositions above. $\square$

## The Involution and the Two Halves

### The Star of a Product

**Proposition.** The involution of the multiplication is the plain product in the reversed order:

$$
(\tilde P\star\tilde Q)^{*}=\tilde Q\,\overline{\tilde P} , \qquad\text{equivalently}\qquad
\tilde Q\star\tilde P=\bigl(\overline{\tilde P}\tilde Q\bigr)^{\natural} .
$$

**Proof.** $(\tilde P\star\tilde Q)^{*}=(\tilde P^{\natural}\tilde Q^{*})^{*}=(\tilde Q^{*})^{*}(\tilde P^{\natural})^{*}=\tilde Q\,\overline{\tilde P}$, since ${}^{*}$ is an anti-automorphism, ${}^{*2}=\mathrm{id}$ and $(\tilde P^{\natural})^{*}=\overline{\tilde P}$, the two conjugations commuting. The same computation with ${}^{\natural}$ in place of ${}^{*}$ gives the companion identity $(\tilde P\star\tilde Q)^{\natural}=\overline{\tilde Q}\tilde P$, which is the one used for the associator below. $\square$

**Remark.** The sibling identity $(\tilde P\star\tilde Q)^{*}=\tilde Q\star\tilde P$ does **not** hold here: the star of the product is a value of the plain product and not of the multiplication, and the transposed product involves ${}^{\natural}$ where the star does not. In the language of *The Sesquilinear Product* the multiplication is therefore not Hermitian-symmetric for the involution, and the defect is exactly the insertion of ${}^{\natural}$ in the first slot.

### The Product Does Not Exchange the Halves

The two halves that the involution cuts out of the algebra are the Hermitian and the skew-Hermitian subspaces

$$
\mathbb{M}_+=\{\tilde Q:\tilde Q^{*}=\tilde Q\} , \qquad \mathbb{M}_-=\{\tilde Q:\tilde Q^{*}=-\tilde Q\} ,
$$

of *Hermitian and Skew-Hermitian Elements*, *Introduction to the Remarkable Subspaces* and *Decompositions Along the Remarkable Subspaces*, the fixed and the anti-fixed sets of ${}^{*}$.

**Proposition.** The multiplication does not preserve the two halves: the product of two Hermitian elements can be skew-Hermitian. The square of an element of either half is a scalar, the central scalar $\tilde P^{\natural}\tilde P$ with the sign of the half,

$$
\tilde P\star\tilde P=\Bigl(\sum_{\mu=0}^{3}P_\mu^2\Bigr)e_0 \ \ (\tilde P\in\mathbb{M}_+) , \qquad
\tilde P\star\tilde P=-\Bigl(\sum_{\mu=0}^{3}P_\mu^2\Bigr)e_0 \ \ (\tilde P\in\mathbb{M}_-) ,
$$

so in particular the square of an element of either half is fixed by the involution.

**Proof.** For the first clause take $\tilde P=ie_1$ and $\tilde Q=ie_2$, both Hermitian; then $\tilde P\star\tilde Q=(-ie_1)(ie_2)=e_3$, and $e_3$ is skew-Hermitian, $e_3^{*}=-e_3$. For the second, let $\tilde P=P_0+\mathbf P\in\mathbb{M}_+$, so that $P_0$ is real, $\mathbf P$ is purely imaginary and $\overline{\tilde P}=\tilde P^{\natural}$, while $\tilde P^{*}=\tilde P$; then $\tilde P\star\tilde P=\tilde P^{\natural}\tilde P^{*}=\tilde P^{\natural}\tilde P=\bigl(\sum_\mu P_\mu^2\bigr)e_0$, the two factors commuting and $\tilde P^{\natural}\tilde P$ being the central scalar on which the square turns. Let $\tilde P\in\mathbb{M}_-$: then $P_0$ is purely imaginary and $\mathbf P$ is real, so $\overline{\tilde P}=-\tilde P^{\natural}$ and $\tilde P^{*}=-\tilde P$, whence $\tilde P\star\tilde P=\tilde P^{\natural}\tilde P^{*}=-\tilde P^{\natural}\tilde P=-\bigl(\sum_\mu P_\mu^2\bigr)e_0$. $\square$

**Remark.** The sibling proves that its product is Hermitian-symmetric, that is that the involution exchanges its two slots, and then reads the two halves as the involution's fixed and anti-fixed subspaces of the multiplication. Here the involution does not exchange the slots, and the halves are the halves of the algebra; the multiplication reads them by the proposition above, which is what is left of the sibling's theorem when the first slot carries the natural conjugation.

### The Other Exchange, and the Two Sesquilinear Halves

The **plain exchange** of the two arguments swaps them, and the proposition above reads the outcome, $\tilde{Q}\star\tilde{P}=\bigl(\overline{\tilde{P}}\tilde{Q}\bigr)^{\natural}$: the swapped product is the natural conjugate of a **plain** product, and the value $\tilde{P}\star\tilde{Q}=(\overline{\tilde{Q}}\tilde{P})^{\natural}$ determines only that plain product, whose factorisation is not unique. So the plain exchange is a **genuine reversal**, no conjugation of the value returns it, and its two halves are only $\mathbb{R}$-bilinear and lie in no subspace of the remarkable subspaces; they are the symmetrised product of *The Sesquilinear Symmetrised Product* and the sesquilinear commutator of *The Sesquilinear Commutator*, and they are not the two parts named $\mathrm{SQS}$ and $\mathrm{AQS}$ of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

The **exchange by the coefficientwise conjugation** $c=\overline{\cdot}$, $f^{c}(\tilde{P},\tilde{Q})=c(\tilde{Q}\star\tilde{P})$, keeps the class; since $c$ is an automorphism of $\mathbb{B}$ and $c(\tilde{Q}^{\natural})=\tilde{Q}^{*}$, its two halves are the symmetrisation of $\tilde{P}^{\natural}$ with $\tilde{Q}^{*}$ and half their commutator in the plain product,

$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}+\tilde{Q}^{*}\tilde{P}^{\natural}\bigr),\qquad
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{*}\tilde{P}^{\natural}\bigr),
$$

and both are sesquilinear over $\mathbb{C}$: the skew half is the cross product $\mathbf{P}\times\overline{\mathbf{Q}}$, vector-valued, and the symmetric half carries the general quaternionic sesquilinear form $K(\tilde{P},\tilde{Q})=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})$ in its scalar part. They are the conjugate-symmetric and skew-conjugate-symmetric parts of *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, and they **are** the operations $\mathrm{SQS}$ and $\mathrm{AQS}$ of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the biquaternion instance of the two bare halves of both sesqualgebras is *The 12 Products of the Biquaternion Complex Space*, §*The Other Exchange, and the Class It Keeps*.

## The Square, the Idempotents and the Ternary Product

### The Square and the Two Halves

**Proposition.** The square of an element in the multiplication is

$$
\tilde Q\star\tilde Q=\bigl(\overline{\tilde Q}\tilde Q\bigr)^{\natural}=\tilde Q^{\natural}\tilde Q^{*} ,
$$

its scalar part is read on the diagonal of the four coordinates,

$$
\mathrm{Sc}(\tilde Q\star\tilde Q)=\sum_{\mu=0}^{3}\varepsilon_\mu Q_\mu\overline{Q_\mu}=|Q_0|^2-|Q_1|^2-|Q_2|^2-|Q_3|^2 ,
$$

the three vector squares entering negatively; and on the two halves the square is the central scalar $\tilde Q\star\tilde Q=\pm\bigl(\sum_\mu Q_\mu^{2}\bigr)e_0$, with the sign $+$ on $\mathbb{M}_+$ and the sign $-$ on $\mathbb{M}_-$.

**Proof.** The first display is the two conjugations of the rule read on equal arguments, and the second is the scalar–vector form: the dot product enters negatively and the two vector terms cancel. The scalar part is the scalar part $\mathrm{Sc}(\tilde P\tilde Q^{*})$ of the four-general-products article with the first factor read through ${}^{\natural}$, which is $\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ at $\tilde P=\tilde Q$. The last clause is the proposition of §*The Product Does Not Exchange the Halves*, where the two signs are computed. $\square$

**Caution on the two squares.** The square of the sibling product is $\tilde Q\tilde Q^{*}$, it is fixed by the involution ${}^{*}$ for every $\tilde Q$ and its scalar part is the sum of the modulus squares $\sum_\mu|Q_\mu|^{2}$, so that the sums of those squares are the algebraic positive cone of *Hermitian Squares and the Algebraic Positive Cone*. Here the square is **not** fixed by the involution in general, its scalar part is $\sum_\mu\varepsilon_\mu Q_\mu\overline{Q_\mu}$ with the sign vector $\varepsilon=(1,-1,-1,-1)$, and the three vector squares enter the sum negatively, so that no such cone is attached to this multiplication. The square and the double product $\tilde Q^{\natural}\tilde Q$ agree on the two halves, up to the sign of the half, and there the square is a real scalar; on the Hermitian idempotents of the algebra the square nevertheless vanishes, as the next subsection recalls.

### The Idempotents

**Proposition.** The idempotents of the multiplication, the solutions of $\tilde Q\star\tilde Q=\tilde Q$, are the solutions of

$$
\overline{\tilde Q}\,\tilde Q=\tilde Q^{\natural} ,
$$

and among the elements of the quaternion subspace $\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_0+\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$ they are $0$, $e_0$, and the **two-parameter family**

$$
\tilde\Pi(\mu)=-\tfrac12e_0+\mu , \qquad \mu\in\mathrm{Vect}(\mathbb{B})_{\mathbb{R}} , \quad (\mu,\mu)=\tfrac34 ,
$$

a two-parameter family in the real three-dimensional vector subspace.

**Proof.** The equation $\tilde Q\star\tilde Q=\tilde Q$ reads $(\overline{\tilde Q}\tilde Q)^{\natural}=\tilde Q$; applying ${}^{\natural}$ to both sides, which is an involution, gives the criterion. On the quaternion subspace the coefficients are real, so $\overline{\tilde Q}=\tilde Q^{\natural}$ and the criterion reads $\tilde Q^{2}=\tilde Q^{\natural}$; with $\tilde Q=Q_0+\mathbf Q$ the plain square is $\bigl(Q_0^{2}-(\mathbf Q,\mathbf Q)\bigr)+2Q_0\mathbf Q$, so the scalar coordinates give $Q_0^{2}-(\mathbf Q,\mathbf Q)=Q_0$ and the vector coordinates give $(2Q_0+1)\mathbf Q=0$. If $\mathbf Q=0$ then $Q_0\in\{0,1\}$ and the solutions are $0$ and $e_0$; if $\mathbf Q\neq0$ then $Q_0=-\tfrac12$ and $(\mathbf Q,\mathbf Q)=Q_0^{2}-Q_0=\tfrac34$, which is the family. $\square$

**Remark.** The idempotents of this multiplication are therefore not the idempotents of the algebra and not the idempotents of the sibling multiplication. The sibling proves that its idempotents are exactly the Hermitian idempotents of the algebra, $0$, $e_0$ and the pure states $\tfrac12(e_0+i\hat\mu)$ with $\hat\mu$ a real unit vector; here those elements are **not** idempotent, each of them having $\tilde\Pi\star\tilde\Pi=0$, since it is a zero divisor of the algebra (*Biquaternion Zero Divisors*) and its square in the other product is the central scalar $\tilde Q^{\natural}\tilde Q$. The idempotents here are the family above, and they are outside the Hermitian subspace: $\tilde\Pi(\mu)$ has real vector part, so $\tilde\Pi(\mu)^{*}\neq\tilde\Pi(\mu)$. Their central scalar $\tilde P^{\natural}\tilde P$ is $e_0$ and the scalar part of their square is $-\tfrac12$, and they are the elements of $\mathbb{B}$ that are idempotent for the fourth product and for it alone among the four.

### The Ternary Product

**Definition.** The **ternary product** attached to the multiplication is

$$
\{\tilde P,\tilde Q,\tilde R\}=(\tilde P\star\tilde Q)\star\tilde R^{*}=\overline{\tilde Q}\,\tilde P\,\tilde R ,
$$

the definition $\{x,y,z\}=(x\star y)\star z^{*}$ of *The Sesquilinear Associator and the Ternary Product* read with this multiplication.

**Proposition.** The ternary product is additive in each variable, it is $\mathbb{C}$-linear in the first and the third variables and conjugate-linear in the second, and under the relabelling $\tilde Q\mapsto\tilde Q^{\natural}$ it is the product $\tilde X^{*}\tilde Y\tilde Z$ of the algebra with its anti-automorphism ${}^{*}$, that is the **left** model of *Algebraic J\*-Algebras* in place of the middle model $\tilde X\tilde Y^{*}\tilde Z$.

**Proof.** The first display is computed from the rule and the anti-multiplicativity of the two conjugations; the parities are read on the coordinates. For the relabelling, $\overline{\tilde Q}\,\tilde P\,\tilde R=\tilde X^{*}\tilde Y\tilde Z$ with $\tilde X=\tilde Q^{\natural}$, $\tilde Y=\tilde P$ and $\tilde Z=\tilde R$, using $\overline{\tilde Q}=\bigl(\tilde Q^{\natural}\bigr)^{*}$; and the map ${}^{*}$ is the conjugate-linear involutive anti-automorphism of the algebra, the datum of the construction. $\square$

### The Failure of the Jordan Triple Identity

**Proposition.** The ternary product does **not** satisfy the Jordan triple identity

$$
\{x,y,\{u,v,w\}\}=\{\{x,y,u\},v,w\}-\{u,\{y,x,v\},w\}+\{u,v,\{x,y,w\}\}
$$

of *Algebraic J\*-Algebras*. At the basis elements $(x,y,u,v,w)=(e_0,e_1,e_0,e_2,e_0)$ the two sides are $e_3$ and $-3e_3$.

**Proof.** The bar conjugates the coefficients, which are real on the basis, so $\overline{e_0}=e_0$ and $\overline{e_k}=e_k$ for $k=1,2,3$. The left-hand side is $\{e_0,e_1,\{e_0,e_2,e_0\}\}$; the inner bracket is $\overline{e_2}e_0e_0=e_2$, and the outer one is $\overline{e_1}e_0e_2=e_1e_2=e_3$. The right-hand side is $\{\{e_0,e_1,e_0\},e_2,e_0\}-\{e_0,\{e_1,e_0,e_2\},e_0\}+\{e_0,e_2,\{e_0,e_1,e_0\}\}$; the first bracket is $\{e_0,e_1,e_0\}=\overline{e_1}e_0e_0=e_1$, and $\{e_1,e_2,e_0\}=\overline{e_2}e_1e_0=e_2e_1=-e_3$; the middle inner bracket is $\{e_1,e_0,e_2\}=\overline{e_0}e_1e_2=e_1e_2=e_3$, and $\{e_0,e_3,e_0\}=\overline{e_3}e_0e_0=e_3$; the third bracket is again $e_1$, and $\{e_0,e_2,e_1\}=\overline{e_2}e_0e_1=e_2e_1=-e_3$. The sum is $-e_3-e_3-e_3=-3e_3$, which differs from $e_3$. $\square$

**Corollary.** The ternary product has the parity of an algebraic $J^{*}$-algebra but not its identity, so the general theorems of *Algebraic J\*-Algebras*, *The Ternary Product as an Operator* and *The Adjoint of the Ternary Product* do not apply to the fourth product's ternary reading. The reason is the one the section *The Product Is Not the Derived Operation* isolates: the model of the theory is the **middle** model $\tilde X\tilde Y^{*}\tilde Z$, which does satisfy the identity, and the ternary product of this multiplication is the **left** model $\tilde X^{*}\tilde Y\tilde Z$, the two being the same formula read with the involution in the first rather than in the middle slot. The insertion of ${}^{\natural}$ in the first slot of the multiplication is what transposes the two, and no identity survives the transposition.

**Remark.** The sibling reading has the theorem in the positive direction, its ternary product being the middle model and hence an algebraic $J^{*}$-algebra. Here the same construction applied to the fourth product leaves the class, and the article records the failure rather than the theorem: the binary multiplication and its ternary form are separated for this product as they are not for the general plain sesquilinear one.

### The First Slot Is the Source

The failures of the multiplication are not independent, and the section separates the ones the first slot owns from the ones it does not. Three are the work of the **first slot** alone, and §*The Isotope Reading* names them: the absence of a unit on either side (the sibling product has $e_0$ on the right), the failure of the slot exchange of §*The Product Does Not Exchange the Halves*, and the failure of the Jordan triple identity of the ternary reading (the sibling's ternary product is the middle model and satisfies the identity). The same insertion also removes the product's status as the derived operation of the algebra with an involution.

The remaining failures are **not** the first slot's work, and the article says so plainly. Non-commutativity, non-associativity, non-flexibility and the failure of the degree-three identity are shared with the sibling product that inserts nothing in the first slot. On the eight-element basis the general plain sesquilinear product fails associativity on $256$ of the $512$ triples, commutativity on $32$ of the $64$ pairs, flexibility on $32$ of the $64$ pairs and the degree-three identity at $4$ of the $8$ elements; the fourth product fails at exactly the same counts. What separates the two is therefore not composition but the **pair (no unit, no Jordan triple)**: the fourth product loses both, the sibling loses neither.

**Remark (what the synthesis is and is not).** The statement is bookkeeping over the propositions above and not a new theorem. Its value is that it keeps apart two claims that are easy to merge: the **metric** — the sign vector $\varepsilon$ of the scalar form and, with it, the loss of the unit — is the first slot's, while the **loss of composition** is common to every nontrivial row and is not. The physics band reads the first item as gauge and reads the two no-go results (no unit, no Jordan triple) as the bounds of the fourth corner; those two are the first slot's. Nothing here identifies the first slot as the source of the non-associativity or of the non-closure of the antisymmetric half, both of which the second slot already spoils. The synthesis is the article's; the counts are a computation on a basis and not invariants.

## The Sesqualgebra as an Object

### Simplicity

**Theorem.** The only two-sided ideals of the sesqualgebra $(\mathbb{B},\star)$ are $0$ and $\mathbb{B}$.

**Proof.** Let $I$ be a two-sided ideal, so that $\tilde A\star\tilde X\in I$ and $\tilde X\star\tilde A\in I$ for every $\tilde A\in\mathbb{B}$ and $\tilde X\in I$. The first condition with $\tilde A=e_0$ gives $\tilde X^{*}\in I$, and the second gives $\tilde X^{\natural}\in I$: the ideal is stable under both conjugations. The first condition then reads that $\tilde A^{\natural}\tilde X^{*}\in I$ for every $\tilde A$ and $\tilde X\in I$; as $\tilde X$ runs over $I$ the element $\tilde X^{*}$ runs over $I$, and as $\tilde A$ runs over $\mathbb{B}$ so does $\tilde A^{\natural}$, whence $\mathbb{B}I\subseteq I$. The second condition reads that $\tilde X^{\natural}\tilde A^{*}\in I$, and gives $I\mathbb{B}\subseteq I$ in the same way. Hence $I$ is a two-sided ideal of the ring $\mathbb{B}$, which is simple by *Biquaternion Ideals and Peirce Decomposition*, so $I$ is $0$ or $\mathbb{B}$. $\square$

**Remark.** The conclusion is the one the sibling reaches, and by the same route, but the route uses both one-sided actions of $e_0$ here: the star produces the ${}^{*}$-stability and the natural conjugation the ${}^{\natural}$-stability, and neither would suffice alone, since a one-sided ideal condition gives only one of the two. In the theory of *Ideals and Quotients of a Sesqualgebra* the ideals are the two-sided ideals of the algebra, so the answer here is the same as for the two readings already established.

### The Left Multiplications

**Proposition.** The left multiplications $L_{\tilde A}(\tilde X)=\tilde A\star\tilde X$ satisfy

$$
L_{\tilde A}\circ L_{\tilde B}(\tilde X)=\tilde A^{\natural}\,\tilde X\,\overline{\tilde B} ,
$$

so the composition of two of them is $\mathbb{C}$-linear in $\tilde X$ and is not a left multiplication of the multiplication.

**Proof.** $L_{\tilde A}(L_{\tilde B}(\tilde X))=\tilde A^{\natural}\bigl(\tilde B^{\natural}\tilde X^{*}\bigr)^{*}=\tilde A^{\natural}\tilde X\,\overline{\tilde B}$, using ${}^{*2}=\mathrm{id}$ and the anti-multiplicativity. Each $L_{\tilde A}$ is conjugate-linear in its argument, so the composition of two is linear, whereas $L_{\tilde A}$ itself is not; hence no composition equals a left multiplication. $\square$

**Corollary.** The left multiplications of the multiplication do **not** form a monoid, and this is the row of *Comparison Between the Four General Products* that reads no for the two sesquilinear products and yes for the two bilinear ones; the sibling article records it from *Relations Between the Four General Products*, where the composition of two of their left multiplications is shown to leave the class. The product itself is left-linear over $\mathbb{C}$ and the composition is $\mathbb{C}$-linear, so the operator closure of the multiplication is not the multiplication.

### The Scalar Part of the Multiplication

**Proposition.** The scalar part of the multiplication is

$$
\mathrm{Sc}(\tilde P\star\tilde Q)=\mathrm{Sc}\bigl(\tilde P^{\natural}\tilde Q^{*}\bigr)=\sum_{\mu=0}^{3}\varepsilon_\mu P_\mu\overline{Q_\mu}=P_0\overline{Q_0}-P_1\overline{Q_1}-P_2\overline{Q_2}-P_3\overline{Q_3} ,
$$

and the multiplication is that scalar part read coefficientwise against the basis, with the two signs of the two conjugations.

**Proof.** The scalar part of the product is the scalar part of $\tilde P^{\natural}\tilde Q^{*}$, which carries the signs $\varepsilon_\mu$ on the four coefficients; the second display is the definition of the rule read on the basis pairs. $\square$

**Remark.** The two scalar parts are separated here as they are in the sibling article: the scalar part of the general plain sesquilinear product is $\sum_\mu P_\mu\overline{Q_\mu}$, while the scalar part of the product of this article carries the signs $\varepsilon_\mu$ in front of the four coefficients, the three vector squares entering negatively. The multiplication is not its scalar part: the scalar part alone does not determine it, and it is the two conjugations that turn the pairings of the coordinates into the product.

## The Four General Products and the Sesquilinear Structure

### Which of the Four Is a Sesquilinear Multiplication

The row of the table of *Comparison Between the Four General Products* headed "multiplication of a sesqualgebra over $\mathbb{C}$" is read with the definition of *Sesqualgebras* and with nothing added to it, and it reads no, no, yes, yes: the two products carrying the star are **both** multiplications of a sesqualgebra over the conjugation, since the first slot of either is read by a map that is $\mathbb{C}$-linear, and the two bilinear products are the trivial-involution collapse of the same definition. The two are separated not by the scalar rules but by the **unit**: the general plain sesquilinear product has $e_0$ on the right, $\tilde P\tilde Q^{*}$ with $\tilde Q=e_0$ returning $\tilde P$, and the general quaternionic sesquilinear product has not, as §*No Unit on Either Side* proves.

The sharper division is the one of the **derived operation**. The general theory of *Sesqualgebras* builds a multiplication from the algebra and its involution by inserting the involution in the second slot, $\tilde X\star\tilde Y=\tilde X\tilde Y^{*}$, and the sibling article proves that the general plain sesquilinear product is that construction for the pair $(\mathbb{B},{}^{*})$. The product of this article inserts the $\mathbb{C}$-linear ${}^{\natural}$ in the first slot as well, and §*The Product Is Not the Derived Operation* proves that this is not the derived operation of any involution of the algebra: condition (i) holds because the first row is the star itself, and condition (ii) fails because it would force ${}^{\natural}$ to be the identity. **The classification of the four** is therefore: one multiplication of an associative unital algebra, the plain product; one multiplication of a sesqualgebra that is the derived operation of the algebra with its star, the general plain sesquilinear product; and the two $\natural$-products, which are the two $\natural$-isotopes of those two, the $\natural$-bilinear product of *Introduction to the General Quaternionic Algebra of Biquaternions* and the $\natural$-sesquilinear product of this article.

### The Isotope Reading

**Proposition.** The multiplication is the **isotope** of the general plain sesquilinear product determined by the pair $(\natural,\mathrm{id})$:

$$
\tilde P\star\tilde Q=\natural(\tilde P)\,\tilde Q^{*} \qquad\text{with}\qquad \natural(\tilde P)=\tilde P^{\natural} ,
$$

the insertion of $\natural$ in the first slot being the isotope, and $\natural$ being a $\mathbb{C}$-linear anti-automorphism, an involution and a bijection of $\mathbb{B}$.

**Proof.** The first display is the definition of the product, the isotope of a binary operation being the operation obtained by inserting a pair of bijections, here $\natural$ in the first slot and the identity in the second. The map $\natural$ is $\mathbb{C}$-linear, involutive and anti-multiplicative, $(\tilde P\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P^{\natural}$ (*The Group of Involutions*, *Introduction to the General Plain Algebra of Biquaternions*). $\square$

**Remark.** The two sesquilinear products are the derived operation and its $\natural$-isotope, and the two bilinear products are related in exactly the same way; the insertion of a $\mathbb{C}$-linear map changes the product without changing its sesquilinearity type, which is the observation of *Comparison Between the Four General Products*, and it is responsible for the absence of a unit here, for the failure of the slot exchange, and for the failure of the Jordan triple identity: all three are properties of the first slot.

## Summary

The general quaternionic sesquilinear product $\tilde P^{\natural}\tilde Q^{*}$ of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, read as a multiplication, satisfies the two scalar rules of a sesqualgebra over $\mathbb{C}$ with the conjugation, and it is the isotope of the derived operation by the natural conjugation.

$$
\boxed{\ \text{With the general quaternionic sesquilinear product, } \mathbb{B} \text{ is a four-dimensional sesqualgebra over } (\mathbb{C},\varsigma) \text{ with no unit on either side, neither associative nor commutative, and not the derived operation.}\ }
$$

Its two one-sided actions of $e_0$ are the two conjugations, $\tilde Q^{*}$ on the left and $\tilde Q^{\natural}$ on the right, so no element is a unit on either side; its table has the unit followed by the negated quaternion units as first row and as first column, and the quaternion table on the imaginary block; its associator is $\overline{\tilde Q}\tilde P\tilde R^{*}-\tilde P^{\natural}\tilde R\overline{\tilde Q}$; it is not flexible and not power associative, and its left multiplications do not form a monoid, the composition $L_{\tilde A}\circ L_{\tilde B}$ being the sandwich $\tilde A^{\natural}(\cdot)\overline{\tilde B}$, linear where each $L$ is conjugate-linear. The star of a product is the plain product in the reversed order, $(\tilde P\star\tilde Q)^{*}=\tilde Q\overline{\tilde P}$, so the involution does not exchange the two slots; the square is $\bigl(\overline{\tilde Q}\tilde Q\bigr)^{\natural}$, its scalar part is $\sum_\mu\varepsilon_\mu Q_\mu\overline{Q_\mu}$, and on the two halves it is the real scalar $\pm\bigl(\sum_\mu Q_\mu^2\bigr)e_0$, the Hermitian idempotents of the algebra having a vanishing square in the multiplication. The idempotents are $0$, $e_0$ and the family $-\tfrac12e_0+\mu$ with $(\mu,\mu)=\tfrac34$ in the real vector subspace, none of them Hermitian. The ternary product is $\overline{\tilde Q}\tilde P\tilde R$, the left model $\tilde X^{*}\tilde Y\tilde Z$; it has the parity of an algebraic $J^{*}$-algebra and fails the Jordan triple identity, at $(e_0,e_1,e_0,e_2,e_0)$ with the two sides $e_3$ and $-3e_3$. The sesqualgebra is simple, its ideals being $0$ and $\mathbb{B}$, and its scalar part is $\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, read here with the general quaternionic sesquilinear multiplication |
| $e_0,e_1,e_2,e_3$ | complex basis; $e_0$ the unit, $e_k$ the quaternion units |
| $i$ | central scalar imaginary, $i^2=-1$ |
| $\tilde Q=Q_0e_0+\mathbf Q$ | a biquaternion and its scalar–vector split, $\mathbf Q=\sum_kQ_ke_k$ |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ | the natural, the coefficientwise and the star conjugation |
| $\varsigma(z)=\bar z$ | the base involution of the sesqualgebra |
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$ | the general quaternionic sesquilinear product, the multiplication of the article |
| $\varepsilon=(1,-1,-1,-1)$ | the signs of the conjugations on the basis, $Q^{\natural}_\nu=\varepsilon_\nu Q_\nu$ and $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ |
| $\sigma$ | the first row, $\sigma(\tilde Q)=e_0\star\tilde Q=\tilde Q^{*}$ |
| $[\tilde P,\tilde Q,\tilde R]$ | the associator, $\overline{\tilde Q}\tilde P\tilde R^{*}-\tilde P^{\natural}\tilde R\overline{\tilde Q}$ |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the Hermitian and the skew-Hermitian subspaces, the fixed and the anti-fixed sets of ${}^{*}$ |
| $\sum_\mu Q_\mu^{2}$ | the central scalar of the square on either half, $\tilde Q\star\tilde Q=\pm\bigl(\sum_\mu Q_\mu^{2}\bigr)e_0$ |
| $\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the scalar part of the multiplication, with $\varepsilon=(1,-1,-1,-1)$ |
| $\{\tilde P,\tilde Q,\tilde R\}=\overline{\tilde Q}\tilde P\tilde R$ | the ternary product, the left model $\tilde X^{*}\tilde Y\tilde Z$ |
| $\tilde\Pi(\mu)=-\tfrac12e_0+\mu$, $(\mu,\mu)=\tfrac34$ | the idempotents of the multiplication in the real vector subspace |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the quaternion product whose two conjugations are the two slots of this multiplication.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for semilinear maps, sesquilinear forms and the tensor product of algebras.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the isotopes and homotopes of an algebra, which is the reading of the $\natural$-product used in this article.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions, their parities and the models they define on an associative algebra.
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the product, its coordinate rule and its scalar–vector form.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table, the witnesses and the classification of the four.
- *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the derived operation, the right unit, the slot exchange, the Hermitian idempotents and the algebraic $J^{*}$-algebra of the sibling product.
- *Introduction to the General Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-biquaternions.md`), for the same insertion of ${}^{\natural}$ in a bilinear product, where the square is scalar and the left multiplications form a monoid.
- *The Sesquilinear Associator and the Ternary Product* (`articles_maths/the-sesquilinear-associator-and-the-ternary-product.md`), for the associator and the ternary product of a sesqualgebra, whose model is the middle model $\tilde X\tilde Y^{*}\tilde Z$.
- *Algebraic J\*-Algebras* (`articles_maths/algebraic-j-star-algebras.md`), for the Jordan triple identity, the two models and the parity of a ternary product.
- *Biquaternion Idempotents and Projections* (`articles_maths/biquaternion-idempotents-and-projections.md`), for the Hermitian idempotents $\tfrac12(e_0+i\hat\mu)$ of the algebra, which are not idempotent for the multiplication of this article and have a vanishing square in it.
