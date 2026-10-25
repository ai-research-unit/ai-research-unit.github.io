# __Introduction to the General Quaternionic Sesqualgebra__

## Introduction

The underlying $\mathbb{C}$-vector space of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products, defined side by side in *The Four General Products and Their Relations over the Biquaternion Algebra*. Two of the four are the multiplication of an algebra over $\mathbb{C}$ in the broad sense, the two whose second slot is read without a conjugation, and two are the multiplication of a **sesqualgebra** over $\mathbb{C}$ with its conjugation as base involution, the two whose second slot carries the star; the first reading of each pair is *The Biquaternion Algebra and Its Vector Spaces* and *Introduction to the General Plain Sesqualgebra*, and the second reading of each pair is the isotope of the first by the natural conjugation. This article is the fourth reading: the **general quaternionic sesquilinear product** $\tilde Q_1^{\natural}\tilde Q_2^{*}$ is additive in each variable, $\mathbb{C}$-linear in the first and conjugate-linear in the second, so it satisfies the two scalar rules of *Sesqualgebras* and is the multiplication of a sesqualgebra over the conjugation, and it is the product of the four that fails to be the **derived operation** $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ of the algebra with its involution. Once the multiplication is in place, the article reads off what the two scalar rules give it: the tensor product and its two factor embeddings, the scalar action that is not a structure map, the trivial centre, the generators and the presentation of the underlying plain algebra, and the one-element subalgebras.

The consequences differ from the sibling reading in every place where the first slot matters. There the product is the derived operation, the unit is a right unit, the involution exchanges the two slots, the idempotents are the Hermitian idempotents of the algebra, the squares generate the algebraic positive cone and the ternary product is an algebraic $J^{*}$-algebra. Here the product carries the $\mathbb{C}$-linear ${}^{\natural}$ in the first slot as well: **there is no unit on either side**, the two one-sided actions of $e_t$ being the two conjugations of the algebra; the involution does not exchange the slots, and what it produces instead is the plain product in the reversed order; the idempotents are not the Hermitian ones, and they form a two-parameter family in the quaternion subspace; the square is not fixed by the involution in general and its scalar part carries the signs of the four coordinates, the three vector squares entering negatively; and the ternary product, although it has the parity of an algebraic $J^{*}$-algebra, **fails the Jordan triple identity**. The article is therefore the record of what the sesquilinear axioms alone force, read on the product of the four that fails to be the derived one.

The boundaries are stated at once. The product is not defined here, and neither are the four general products as a family: the coordinate rule and the four names are *The Four General Products and Their Relations over the Biquaternion Algebra*, the identities that link the four general products are *The Four General Products and Their Relations over the Biquaternion Algebra*, and their properties are compared in *The Four General Products and Their Relations over the Biquaternion Algebra*, whose sesquilinear row is the one read below. The other three readings and the general theory that each of them uses are the three articles *The Biquaternion Algebra and Its Vector Spaces*, *Introduction to the General Plain Sesqualgebra* and *Introduction to the General Quaternionic Algebra*, and nothing of theirs is repeated here; where the present product differs from the general plain sesquilinear one, the difference is stated and the sibling is named. The elements, the basis, the conjugations and the remarkable subspaces are *The Biquaternion Algebra and Its Vector Spaces*, *Introduction to the Remarkable Subspaces*, *Decompositions Along the Remarkable Subspaces* and *Comparison of the Remarkable Subspaces*, the two halves cut out by the involution being the subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ of *Hermitian and Skew-Hermitian Elements*. On the biquaternion side, the units and the invertibility criterion are read in the same article, the zero divisors are *N-Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*, the idempotents of the algebra are *Idempotents of the General Plain Algebra*, the simplicity of the ring is *Ideals and Peirce Decompositions of the Biquaternion Algebra*, and the two bilinear articles are the ones named in the sentence above. The general theory is the sesquilinear block: the definition is *Sesqualgebras*, the calculus of the product is *The Sesquilinear Product*, the associator and the ternary product are *The Sesquilinear Associator and the Ternary Product*, the abstract ternary system is *Algebraic J\*-Algebras*, the operator readings are *The Ternary Product as an Operator* and *The Adjoint of the Ternary Product*, the two halves are *Hermitian and Skew-Hermitian Elements*, and the ideals are *Ideals and Quotients of a Sesqualgebra*.

$$
\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*}
$$

throughout, the natural conjugation ${}^{\natural}$ acting in the first slot and the star ${}^{*}$ in the second, the two **slot involutions** of the block. The four general products and their notation are those of *The Four General Products and Their Relations over the Biquaternion Algebra*.

## The Product Read as a Multiplication

### The Rule

**Definition.** The **multiplication** of the sesqualgebra is the rule

$$
\star \; : \; \mathbb{B}\times\mathbb{B}\longrightarrow\mathbb{B} , \qquad
(\tilde Q_1,\tilde Q_2)\longmapsto \tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*}=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}\varepsilon_\mu\varepsilon_\nu Q_{1\mu}\overline{Q_{2\nu}}\,e_\mu e_\nu ,
$$

the general quaternionic sesquilinear product of *The Four General Products and Their Relations over the Biquaternion Algebra*; each of the sixteen products $e_\mu e_\nu$ is a basis element up to sign, so the double sum is a complex combination of $e_t,\dots,\vec e_z$ and the rule is a map into $\mathbb{B}$ and is well defined. On the four coordinates it reads

$$
\tilde Q_1\star\tilde Q_2=\bigl(Q_{1t}\overline{Q_{2t}}-Q_{1x}\overline{Q_{2x}}-Q_{1y}\overline{Q_{2y}}-Q_{1z}\overline{Q_{2z}}\bigr)
+\bigl(-Q_{1t}\overline{Q_{2x}}-Q_{1x}\overline{Q_{2t}}+Q_{1y}\overline{Q_{2z}}-Q_{1z}\overline{Q_{2y}}\bigr)\vec e_x
+\bigl(-Q_{1t}\overline{Q_{2y}}-Q_{1x}\overline{Q_{2z}}-Q_{1y}\overline{Q_{2t}}+Q_{1z}\overline{Q_{2x}}\bigr)\vec e_y
+\bigl(-Q_{1t}\overline{Q_{2z}}+Q_{1x}\overline{Q_{2y}}-Q_{1y}\overline{Q_{2x}}-Q_{1z}\overline{Q_{2t}}\bigr)\vec e_z ,
$$

The rule is the general plain sesquilinear product with the first factor read through the $\mathbb{C}$-linear ${}^{\natural}$ as well, which is the insertion that will turn out to change every property that involves the first slot.

### The Scalar–Vector Form

Collecting the scalar part and the vector part of the two elements, the vector part of the first negated and that of the second read through the coefficientwise conjugate, the same product reads

$$
\tilde Q_1\star\tilde Q_2=\bigl(Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})\bigr)-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2} .
$$

Both displays are quoted from *The Four General Products and Their Relations over the Biquaternion Algebra*; its scalar part is $\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ with $\varepsilon=(1,-1,-1,-1)$.

### The Two Scalar Rules

**Proposition.** The multiplication is **additive in each variable**; it is $\mathbb{C}$-**linear in the first** variable and $\varsigma$-**semilinear in the second**, with $\varsigma(z)=\bar z$:

$$
\boxed{\; (\lambda\tilde Q_1)\star\tilde Q_2=\lambda\,(\tilde Q_1\star\tilde Q_2) , \qquad
\tilde Q_1\star(\lambda\tilde Q_2)=\bar\lambda\,(\tilde Q_1\star\tilde Q_2) , \qquad \lambda\in\mathbb{C} , \qquad
(\tilde Q_1+\tilde Q_3)\star\tilde Q_2=\tilde Q_1\star\tilde Q_2+\tilde Q_3\star\tilde Q_2 \;}.
$$

**Proof.** The coordinates of the developed form are sums of terms $Q_{1\mu}\overline{Q_{2\nu}}$ with fixed coefficients, so they are additive and $\mathbb{C}$-linear in the four coordinates of $\tilde Q_1$ alone and additive and conjugate-linear in the four coordinates of $\tilde Q_2$ alone. The three displays are that statement read coordinate by coordinate; the natural conjugation is $\mathbb{C}$-linear and contributes no conjugation.

**Corollary.** The product is a multiplication of a **sesqualgebra** over $(\mathbb{C},\varsigma)$ in the sense of *Sesqualgebras*: the two axioms are the two scalar rules and nothing else is assumed, no associativity, no commutativity and no two-sided unit being among them (*The Sesquilinear Product*). The product belongs to the sesquilinear row of *The Four General Products and Their Relations over the Biquaternion Algebra*, which reads yes there, and it is one of the two of the four that do.

### The Multiplication Table

**Proposition.** The products of the basis elements are $e_\mu\star e_\nu=\varepsilon_\mu\varepsilon_\nu\,e_\mu e_\nu$, and they are

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $-\vec e_x$ | $-\vec e_y$ | $-\vec e_z$ |
| $\vec e_x$ | $-\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $-\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $-\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

**Proof.** Read from the rule: $e_\mu\star e_\nu=\varepsilon_\mu(e_\mu)^{\natural}\,\varepsilon_\nu(e_\nu)^{*}=\varepsilon_\mu\varepsilon_\nu\,e_\mu e_\nu$, and the entries are the products of the quaternion units, multiplied by the two signs.

The table differs from the $\natural$-bilinear table of *Introduction to the General Quaternionic Algebra* in one block: its first row and its first column are both the negated basis, $e_t\star e_\nu=-e_\nu$ and $e_\mu\star e_t=-e_\mu$ for $\mu,\nu\neq t$ with $e_t\star e_t=e_t$, while there the first row was the identity row; and its three-by-three block is the quaternion table itself and not its negative. The whole difference is the star in the second slot, which negates the vector units there and leaves the scalar unit alone.

### The Product Is Not the Derived Operation

**Theorem.** The general plain sesquilinear product $\tilde Q_1\tilde Q_2^{*}$ is the **derived operation** of $\mathbb{B}$ read as the associative algebra with its conjugate-linear involution ${}^{*}$, and the general quaternionic sesquilinear product is not: in the notation of *Sesqualgebras*, the map $\sigma(\tilde Q_2)=e_t\star\tilde Q_2$ satisfies condition (i), being the involution ${}^{*}$ itself, and fails condition (ii), so that no involution of the algebra makes the product the value of the plain product on a conjugated pair.

**Proof.** The first clause is the theorem of *Introduction to the General Plain Sesqualgebra*, and it is repeated here only to fix the comparison. For the second, $e_t\star\tilde Q=e_t^{\natural}\tilde Q^{*}=\tilde Q^{*}$, so $\sigma={}^{*}$, which is conjugate-linear and involutive, and (i) holds; condition (ii) would read $\tilde Q_1^{\natural}\tilde Q_2^{*}=\tilde Q_1\tilde Q_2^{*}$ for every pair, and at $\tilde Q_2=e_t$ this is $\tilde Q_1^{\natural}=\tilde Q_1$ for every $\tilde Q_1$, which fails at $\tilde Q_1=\vec e_x$, where the two sides are $-\vec e_x$ and $\vec e_x$. Equivalently the product has no right unit, as the next section shows, and the sibling article records that the failure of (ii) is the same statement.

**Corollary.** The product is the **isotope** of the derived operation by the natural conjugation: $\tilde Q_1\star\tilde Q_2=\natural(\tilde Q_1)\,\tilde Q_2^{*}$, with $\natural$ the $\mathbb{C}$-linear anti-automorphism and bijection of §*The Isotope Interpretation*. The two sesquilinear products of the four are therefore the derived operation and its $\natural$-isotope, exactly as the two bilinear products are the plain multiplication and its $\natural$-isotope, and in both pairs the second is the first with the $\mathbb{C}$-linear insertion that the *derived operation* test rejects (*The Four General Products and Their Relations over the Biquaternion Algebra*, *Which of the Four Is a Sesquilinear Multiplication*).

## The Two Actions of the Unit

### The Left Action Is the Star

**Proposition.** The unit acts on the left by the involution: $e_t\star\tilde Q=\tilde Q^{*}$ for every $\tilde Q$. In particular $e_t$ is not a left unit, and the map $\tilde Q\mapsto e_t\star\tilde Q$ is conjugate-linear, being the star.

**Proof.** $e_t^{\natural}=e_t$, so $e_t\star\tilde Q=e_t\tilde Q^{*}=\tilde Q^{*}$, and the star is conjugate-linear and not the identity.

### The Right Action Is the Natural Conjugation

**Proposition.** The unit acts on the right by the natural conjugation: $\tilde Q\star e_t=\tilde Q^{\natural}$ for every $\tilde Q$. In particular $e_t$ is not a right unit.

**Proof.** $e_t^{*}=e_t$, so $\tilde Q\star e_t=\tilde Q^{\natural}e_t=\tilde Q^{\natural}$, and $\natural$ is not the identity.

### No Unit on Either Side

**Proposition.** The multiplication has **no unit on either side**.

**Proof.** A left unit $\tilde E$ satisfies $\tilde E\star\tilde Q=\tilde Q$ for every $\tilde Q$, and at $\tilde Q=e_t$ this reads $\tilde E\star e_t=\tilde E^{\natural}=e_t$, whence $\tilde E=e_t$; but $e_t\star \vec e_x=\vec e_x^{*}=-\vec e_x\neq \vec e_x$, so $e_t$ is not a left unit and there is none. A right unit $\tilde E$ satisfies $\tilde Q_1\star\tilde E=\tilde Q_1$ for every $\tilde Q_1$, and at $\tilde Q_1=e_t$ this reads $e_t\star\tilde E=\tilde E^{*}=e_t$, whence $\tilde E=e_t$; but $\vec e_x\star e_t=\vec e_x^{\natural}=-\vec e_x\neq \vec e_x$, so $e_t$ is not a right unit either.

**Remark.** The two one-sided actions of $e_t$ are the two conjugations of the algebra, ${}^{*}$ on the left and ${}^{\natural}$ on the right, and no element plays the part of a unit on either side; this is the sharpest single difference from the sibling product, where the first of the two actions is the identity and $e_t$ is a right unit. The comparison of the four records it in the row "$1$ is a right identity", which reads yes only for the general plain sesquilinear product and no for the two $\natural$-products, and it is the reason the same article excludes the fourth product from the derived operation.

## The Axioms and What They Do Not Force

### Neither Associative Nor Commutative

**Theorem.** The multiplication is neither associative nor commutative; a sesqualgebra of full type with a nontrivial involution is never associative, by the collapse theorem of *Sesqualgebras*, and $\mathbb{B}$ is of full type.

**Proof of the collapse, quoted.** If a product satisfying the two scalar rules with a nontrivial $\varsigma$ is associative, then the two scalar rules for $\lambda$ and associativity applied to $\lambda(\tilde Q_1\tilde Q_2)=(\lambda\tilde Q_1)\tilde Q_2=\tilde Q_1(\lambda\tilde Q_2)$ force the involution to be trivial on the scalars that act; the argument is *The Collapse at the Identity* of *Sesqualgebras*, and it is the same for the sibling product. Two witnesses settle the two axioms here directly: $(e_t\star \vec e_x)\star \vec e_x=(-\vec e_x)\star \vec e_x=e_t$ while $e_t\star(\vec e_x\star \vec e_x)=e_t\star(-e_t)=-e_t$, so the product is not associative; and $\vec e_x\star \vec e_y=\vec e_z$ while $\vec e_y\star \vec e_x=-\vec e_z$, so it is not commutative.

### The Associator

**Proposition.** The associator of the multiplication,

$$
[\tilde Q_1,\tilde Q_2,\tilde Q_3]=(\tilde Q_1\star\tilde Q_2)\star\tilde Q_3-\tilde Q_1\star(\tilde Q_2\star\tilde Q_3) ,
$$

is

$$
[\tilde Q_1,\tilde Q_2,\tilde Q_3]=\overline{\tilde Q_2}\,\tilde Q_1\,\tilde Q_3^{*}-\tilde Q_1^{\natural}\,\tilde Q_3\,\overline{\tilde Q_2} .
$$

**Proof.** Two identities of §*The Star of a Product* are used: $(\tilde Q_5\star\tilde Q_4)^{*}=\tilde Q_4\overline{\tilde Q_5}$ and $(\tilde Q_5\star\tilde Q_4)^{\natural}=\overline{\tilde Q_4}\tilde Q_5$. Hence $(\tilde Q_1\star\tilde Q_2)\star\tilde Q_3=(\tilde Q_1\star\tilde Q_2)^{\natural}\tilde Q_3^{*}=\overline{\tilde Q_2}\tilde Q_1\tilde Q_3^{*}$ on the one hand, and $\tilde Q_1\star(\tilde Q_2\star\tilde Q_3)=\tilde Q_1^{\natural}(\tilde Q_2\star\tilde Q_3)^{*}=\tilde Q_1^{\natural}\tilde Q_3\overline{\tilde Q_2}$ on the other, and the difference of the two is the associator displayed.

**Remark.** The associator is a sum of two terms of opposite parity in the second variable and the same parity in the first and the third, and it vanishes under none of the standard hypotheses; the product has no identity on either side, so the associator is not the instrument of an associativity theory for this algebra, and the structural object that survives is the ternary product of §*The Ternary Product*.

**Remark (the witnesses and the count).** The associator is nonzero on $256$ of the $512$ triples of the eight-element basis, at the clean witnesses $(e_t,e_t,\vec e_x)$ and $(e_t,\vec e_x,\vec e_x)$, where the display gives

$$
[e_t,e_t,\vec e_x]=-2\vec e_x,\qquad [e_t,\vec e_x,\vec e_x]=2e_t .
$$

The two witnesses show that the associator is **not confined to one grade**: one value is pure vector and the other pure scalar, so the defect of composition is neither a purely central shift nor a purely vectorial one, unlike the defects of the antisymmetric half, which are pure vector.

### The Flexibility and the Degree-Three Identity

**Proposition.** The multiplication is **not flexible** and **not power associative**.

**Proof.** The flexible law $(\tilde Q_1\star\tilde Q_2)\star\tilde Q_1=\tilde Q_1\star(\tilde Q_2\star\tilde Q_1)$ fails at $\tilde Q_1=ie_t$, $\tilde Q_2=e_t$, where the two sides are $e_t$ and $-e_t$ (*The Four General Products and Their Relations over the Biquaternion Algebra*); and the degree-three identity $\tilde Q_1\star(\tilde Q_1\star\tilde Q_1)=(\tilde Q_1\star\tilde Q_1)\star\tilde Q_1$ fails at $\tilde Q_1=i\vec e_z$, where the two sides are $i\vec e_z$ and $-i\vec e_z$.

**Remark.** The witness of the degree-three identity is the same one the comparison records for this product, and it is worth reading: $\tilde Q=i\vec e_z$ is not a zero divisor and $\tilde Q\star\tilde Q=-e_t$ is a scalar, so the two bracketings of the triple product differ by the star in the second slot acting on the scalar line, which is the single place where the conjugation in that slot bites.

### The Algebra Structure

**Theorem.** With the general quaternionic sesquilinear product as its multiplication, $\mathbb{B}$ is a four-dimensional **sesqualgebra over $(\mathbb{C},\varsigma)$** in the sense of *Sesqualgebras* — additive in each variable, $\mathbb{C}$-linear in the first and $\varsigma$-semilinear in the second — with no unit on either side; it is neither associative nor commutative, neither flexible nor power associative, and it is not the derived operation of the algebra with its involution.

**Proof.** The product is a sesquilinear binary operation on the $\mathbb{C}$-vector space $\mathbb{B}$, which is the definition of a sesqualgebra over the pair $(\mathbb{C},\varsigma)$, and the remaining clauses are the propositions above.

## The Multiplication as a Scalar Extension

### The Tensor Product

The underlying space of $\mathbb{B}$ is the tensor product $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ of the two $\mathbb{R}$-algebras $\mathbb{C}$ and $\mathbb{H}$, and the general plain bilinear product is the product of the tensor product of algebras, $(A_1\otimes h_1)(A_2\otimes h_2)=(A_1A_2)\otimes(h_1h_2)$, read under the identification $1\otimes e_k\mapsto e_k$, $i\otimes e_k\mapsto ie_k$ (*The Biquaternion Algebra and Its Vector Spaces*, §*The Multiplication as a Scalar Extension*). The multiplication of this article is **not** a product of the tensor product: a product induced by the tensor product of the two $\mathbb{R}$-algebras is $\mathbb{C}$-bilinear, since the imaginary scalar is central in the first factor, whereas $\star$ is $\mathbb{C}$-linear in the first slot and $\varsigma$-semilinear in the second (§*The Two Scalar Rules*). What the tensor product gives the block is the underlying space, its two factor embeddings, and the statement that a product additive in each variable is determined by its values on a basis.

**Proposition.** The multiplication is $\mathbb{R}$-bilinear, and it is determined by its values on the eight real basis elements $e_t,\dots,\vec e_z,ie_t,\dots,i\vec e_z$; equivalently, by its values on the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ together with the two slot parities.

**Proof.** Additivity in each variable and the two scalar rules give $\mathbb{R}$-bilinearity. For the determination, write $\tilde Q_1=p+ip'$ and $\tilde Q_2=q+iq'$ with $p,p',q,q'\in\mathbb{H}_{\mathbb{B}}$; expanding by additivity and the parities, $(\lambda\tilde Q_1)\star\tilde Q_2=\lambda(\tilde Q_1\star\tilde Q_2)$ and $\tilde Q_1\star(\lambda\tilde Q_2)=\bar\lambda(\tilde Q_1\star\tilde Q_2)$ for $\lambda=i$, gives

$$
\tilde Q_1\star\tilde Q_2=p\star q-i\,(p\star q')+i\,(p'\star q)+p'\star q' ,
$$

so that the four values on $\mathbb{H}_{\mathbb{B}}$ determine the value everywhere. The sixteen products of the complex basis $e_\mu\star e_\nu$ are the table of §*The Multiplication Table* and are the same determination read on the complex basis.

### The Two Factor Embeddings

The two factor embeddings

$$
\mathbb{C}\longrightarrow\mathbb{B}, \quad A\longmapsto A\otimes 1=Ae_t , \qquad
\mathbb{H}\longrightarrow\mathbb{B}, \quad h\longmapsto 1\otimes h ,
$$

have images that do **not** commute here. The second image is the real quaternion subspace $\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_t+\mathbb{R}\vec e_x+\mathbb{R}\vec e_y+\mathbb{R}\vec e_z$ of *Introduction to the Remarkable Subspaces*, and on it the multiplication is the conjugate of the reversed quaternion product. The failure of the images to commute is the failure of the structure map read on the two embeddings: for $\lambda\in\mathbb{C}$ and a real quaternion $q$ one has $(\lambda e_t)\star q=\lambda q^{\natural}=\lambda\overline{q}$ and $q\star(\lambda e_t)=\overline{\lambda}\,q^{\natural}=\overline{\lambda}\,\overline{q}$, which agree for every $q$ only when $\lambda$ is real. In the plain algebra the two images commute and the scalar is central; here they do not, and the scalar line is not the centre.

**Proposition.** For $p,q\in\mathbb{H}_{\mathbb{B}}$,

$$
p\star q=p^{\natural}q^{*}=\overline{p}\,\overline{q}=\overline{qp} ,
$$

the quaternion conjugate of the plain product taken in the reversed order.

**Proof.** The coefficients of $p$ and $q$ are real, so $p^{\natural}=\overline{p}$ and $q^{*}=\overline{q^{\natural}}=\overline{q}$; the quaternion conjugation is anti-multiplicative, hence $\overline{p}\,\overline{q}=\overline{qp}$. On the basis, $\vec e_x\star \vec e_y=\vec e_z=\overline{\vec e_y \vec e_x}$, while the plain product in the written order gives $\overline{\vec e_x \vec e_y}=-\vec e_z$.

So the block is the complexification of the real quaternion space, and not the complexification of the quaternion algebra: on the real quaternion subspace the multiplication is not the quaternion product but its reversed conjugate, and the complex structure of the space, the scalar action by $i$, follows the two parities of the product, being $\mathbb{C}$-linear in the first slot and conjugate-linear in the second, so it is not a complex structure of the multiplication (§*The Two Scalar Rules*, §*The Scalars Are Not the Centre*).

## The Scalars, the Centre and the Structure Map

### The Structure Map

The scalars of an algebra enter through the homomorphism $\varphi:\mathbb{C}\to Z(\mathbb{B})$, $\varphi(A)=Ae_t$, whose image is the scalar line $\mathbb{C}e_t$. **Here there is no such homomorphism for the multiplication of this article.** The image would be the line $\mathbb{C}e_t$, which is not central (§*The Scalars Are Not the Centre*), and $\varphi$ is not multiplicative, since

$$
\varphi(z)\star\varphi(w)=ze_t\star we_t=z\overline{w}\,e_t=\varphi(z\overline{w})\neq\varphi(zw)
$$

for every non-real $w$ and $z\neq 0$. What survives is the scalar action $\mathbb{C}\times\mathbb{B}\to\mathbb{B}$, $A\cdot\tilde Q=A\tilde Q$, applied to the four coefficients, and it is compatible with the product in the first slot alone:

$$
A\cdot(\tilde Q_1\star\tilde Q_2)=(A\cdot\tilde Q_1)\star\tilde Q_2 , \qquad
\tilde Q_1\star(A\cdot\tilde Q_2)=\bar A\,(\tilde Q_1\star\tilde Q_2) , \qquad A\in\mathbb{C} .
$$

The first identity is the $\mathbb{C}$-linearity of the first slot and the second is the $\varsigma$-semilinearity of the second; together they are the two scalar rules of *Sesqualgebras*, which replace the axiom that the scalars are central. The block is a sesqualgebra over $(\mathbb{C},\varsigma)$ and not a $\mathbb{C}$-algebra: the scalar line is not the centre, and the scalar action is not two-sided.

### The Gate: a Central Element of Square $-1$

**The gate, applied here, is empty.** For an algebra, a complex structure compatible with the product is the same thing as a central element $j$ with $j^2=-1$, the scalar action being $(a+ib)\tilde Q_1=a\tilde Q_1+bj\tilde Q_1$ (*The Biquaternion Algebra and Its Vector Spaces*, §*The Gate: a Central Element of Square $-1$*). Here no element plays the part, because the centre is trivial: there is no central element at all, and a fortiori none of square $-1$. The scalar imaginary $i$, which has $i^2=-1$, is not central, and its failure is one computation:

$$
(ie_t)\star \vec e_x=ie_t\cdot \vec e_x^{*}=ie_t\cdot(-\vec e_x)=-i\vec e_x , \qquad
\vec e_x\star(ie_t)=\vec e_x^{\natural}\cdot(ie_t)^{*}=(-\vec e_x)(-ie_t)=i\vec e_x .
$$

The complex structure of the underlying space is therefore not a complex structure of the multiplication; it is carried by the first slot, where the scalar action is linear, and it does not pass to the second, where the scalar action is conjugate-linear. In a sesqualgebra the two parities are part of the definition, through the base involution $\varsigma$, and they are not read off from a central element.

### The Scalars Are Not the Centre

**Proposition.** For the general quaternionic sesquilinear product the centre of $\mathbb{B}$ is trivial:

$$
Z(\mathbb{B})=\{\tilde Q_1:\tilde Q_1\star\tilde Q_2=\tilde Q_2\star\tilde Q_1 \text{ for every } \tilde Q_2\}=0 .
$$

**Proof.** Let $\tilde Q_1$ be central. Testing against $\tilde Q_2=e_t$ and using the two one-sided actions, $\tilde Q_1\star e_t=\tilde Q_1^{\natural}$ and $e_t\star\tilde Q_1=\tilde Q_1^{*}$, so $\tilde Q_1^{\natural}=\tilde Q_1^{*}$; on the four coordinates this reads $\varepsilon_\nu X_\nu=\varepsilon_\nu\overline{X_\nu}$, hence every $X_\nu$ is real and $\tilde Q_1\in\mathbb{H}_{\mathbb{B}}$. For a real $\tilde Q_1=x_t+x_x\vec e_x+x_y\vec e_y+x_z\vec e_z$ one has $\tilde Q_1^{\natural}=\overline{\tilde Q_1}=x_t-x_x\vec e_x-x_y\vec e_y-x_z\vec e_z$ (the natural conjugation is the quaternion conjugation on the real subspace) and $\tilde Q_1^{*}=\overline{\tilde Q_1}$, while $(i\vec e_y)^{\natural}=-i\vec e_y$ and $(i\vec e_y)^{*}=i\vec e_y$. Testing against $\tilde Q_2=i\vec e_y$ gives $\tilde Q_1\star i\vec e_y=\overline{\tilde Q_1}\,i\vec e_y$ and $i\vec e_y\star\tilde Q_1=-i\vec e_y\overline{\tilde Q_1}$, so centrality forces $\overline{\tilde Q_1}\vec e_y+\vec e_y\overline{\tilde Q_1}=0$. The quaternion product is $\overline{\tilde Q_1}\vec e_y+\vec e_y\overline{\tilde Q_1}=2x_t\vec e_y+2x_y e_t$, hence $x_t=x_y=0$; the tests against $i\vec e_x$ and $i\vec e_z$ give $x_x=x_z=0$ in the same way. Therefore $\tilde Q_1=0$, and no nonzero element is central.

**Corollary.** The block is **not a central sesqualgebra**: its scalar line and its centre are disjoint but for $0$, since the first is $\mathbb{C}e_t$ and the second is $0$. This is the sharpest structural difference from the plain row, whose centre is $\mathbb{C}e_t$ (*The Biquaternion Algebra and Its Vector Spaces*, §*The Scalars Are the Centre*); there the scalars are the centre, here the scalar action is one-sided and reaches no centre.

### Simplicity and the Absence of Division

**Proposition.** The block is **simple**: its only two-sided ideals are $0$ and $\mathbb{B}$. This is §*Simplicity*, with the ideal theory of *Ideals and Quotients of a Sesqualgebra*, cited and not repeated. Since the centre is trivial and is not the scalar line, the block is simple and **not central simple**: the scalar line $\mathbb{C}e_t$ is a proper subspace of $\mathbb{B}$ that meets the centre only at $0$.

**Proposition.** The sesqualgebra is **not a division algebra**.

**Proof.** The element $e_t+i\vec e_x$ is nonzero and its square vanishes,

$$
(e_t+i\vec e_x)\star(e_t+i\vec e_x)=(e_t-i\vec e_x)(e_t+i\vec e_x)=e_t-(i\vec e_x)^2=e_t-i^2\vec e_x^2=e_t-e_t=0 ,
$$

so $e_t+i\vec e_x$ is a nonzero nilpotent of index two, hence a zero divisor, and the product has no division. It has no unit and no inverse either, the two one-sided actions of $e_t$ being the two conjugations; the substitute of the block for invertibility is the group of units of the **plain** algebra, and it is *Norm and Invertibility in the General Quaternionic Sesqualgebra*. The zero divisors and the nilpotents are *Zero Divisors of the General Quaternionic Sesqualgebra* and *Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra*.

## Generators and the Presentation

### The Generators

**Proposition.** The plain algebra $\mathbb{B}$ is generated, as a $\mathbb{C}$-algebra with unit, by $\vec e_x$ and $\vec e_y$; and the sesqualgebra, whose multiplication differs from the plain one by the $\mathbb{C}$-linear natural conjugation inserted in the first slot, is generated by the same two elements.

**Proof.** In the plain algebra the relations $\vec e_x^2=-e_t$ and $\vec e_x \vec e_y=\vec e_z$ of the table give the identity and the fourth unit from $\vec e_x$ and $\vec e_y$, and the four basis elements span (*The Biquaternion Algebra and Its Vector Spaces*, §*The Generators*). In the block the same two relations read $\vec e_x\star \vec e_x=-e_t$ and $\vec e_x\star \vec e_y=\vec e_z$, so the identity and the fourth unit are again reached; the scalar action supplies the complex coefficients in the first slot, and every element is a $\mathbb{C}$-combination of $e_t,\vec e_x,\vec e_y,\vec e_z$.

### The Relations and the Presentation

**Proposition.** The generators $\vec e_x,\vec e_y$ satisfy the quaternion relations read in the product,

$$
\vec e_x\star \vec e_x=\vec e_y\star \vec e_y=-e_t , \qquad \vec e_x\star \vec e_y+\vec e_y\star \vec e_x=0 ,
$$

and $\vec e_x\star \vec e_y=\vec e_z$ returns the third imaginary unit. The relations do **not present the sesqualgebra** as a quotient of a free associative algebra, because the product is not associative and no such quotient is a sesqualgebra of this type; what they present is the underlying plain algebra,

$$
\mathbb{B}\cong\mathbb{C}\langle E_1,E_2\rangle\big/\bigl(E_1^2+1,\;E_2^2+1,\;E_1E_2+E_2E_1\bigr) ,
$$

of §*The Relations and the Presentation* of *The Biquaternion Algebra and Its Vector Spaces*.

**Remark.** The presentation of the model and the presentation of the block are the same presentation of the plain algebra, and the multiplication is not: the block is that presented algebra with the natural conjugation inserted in the first slot, the isotope of §*The Isotope Interpretation*. A presentation of the sesqualgebra itself, as a quotient of a free sesqualgebra by sesquilinear relations, is not given here, and the absence is stated rather than filled.

## The Subalgebra Generated by One Element

The model reads the unital subalgebra $\mathbb{C}[\tilde Q]=\mathbb{C}e_t+\mathbb{C}\tilde Q+\mathbb{C}\tilde Q^y+\cdots$ from the identity $\tilde Q^y=\bigl(Q_t^2-(\vec Q,\vec Q)\bigr)+2Q_t\vec Q$, which puts the square in $\mathbb{C}e_t+\mathbb{C}\tilde Q$ and makes that plane a commutative subalgebra of dimension at most two over $\mathbb{C}$ (*The Biquaternion Algebra and Its Vector Spaces*, §*The Subalgebra Generated by One Element*). **That identity fails here**, and with it the whole reading.

**Proposition.** For a generic element $\tilde Q$ the three elements $e_t,\tilde Q,\tilde Q\star\tilde Q$ are linearly independent over $\mathbb{C}$, so the square does not lie in $\mathbb{C}e_t+\mathbb{C}\tilde Q$; and the multiplication is not power associative, since at $\tilde Q=i\vec e_z$ the two cubings differ,

$$
i\vec e_z\star(i\vec e_z\star i\vec e_z)=i\vec e_z , \qquad (i\vec e_z\star i\vec e_z)\star i\vec e_z=-i\vec e_z .
$$

**Proof.** The square is $\tilde Q\star\tilde Q=\bigl(\overline{\tilde Q}\tilde Q\bigr)^{\natural}$ (§*The Square and the Two Halves*); the identity of the model would place it in $\mathbb{C}e_t+\mathbb{C}\tilde Q$, and a recomputation of the complex rank of $e_t,\tilde Q,\tilde Q\star\tilde Q$ on random elements gives three, not two, for a generic $\tilde Q$. The two cubings are those of §*The Flexibility and the Degree-Three Identity*, where the failure is recorded.

**Proposition.** The subalgebra generated by a generic element is the whole space. The left-nested powers $\tilde Q,\tilde Q\star\tilde Q,(\tilde Q\star\tilde Q)\star\tilde Q,\dots$ of a generic element span the whole space, of real dimension eight and complex dimension four, so the smallest subalgebra containing $\tilde Q$ is $\mathbb{B}$ itself.

**Proof.** The span of the words in $\tilde Q$ is stable under the product by construction and is the smallest subalgebra containing $\tilde Q$; it contains the left-nested powers, and a recomputation on random elements gives complex rank four, the full complex dimension of $\mathbb{B}$, for the powers alone. Hence the generated subalgebra is $\mathbb{B}$.

**Remark.** The proper subalgebras generated by one element are not only the scalar line. The scalar line $\mathbb{C}e_t$ **is** a subalgebra, of complex dimension one, with the multiplication $ze_t\star we_t=z\overline{w}\,e_t$, conjugate-symmetric and not commutative; it is the subalgebra generated by $ie_t$, whose left-nested powers are $ie_t,e_t,-ie_t,-e_t,\dots$, and it is the only one-dimensional case generated by a single element. But two-dimensional cases abound. Every element of the real quaternion subspace generates at most a two-dimensional subalgebra, because for real $\tilde Q$ the two conjugations coincide with the quaternion conjugation, so $\tilde Q\star e_t=e_t\star\tilde Q=\overline{\tilde Q}$ and $\tilde Q\star\tilde Q=\overline{\tilde Q^{2}}$ both lie in $\mathbb{C}e_t+\mathbb{C}\tilde Q$: the algebra generated by $\vec e_x$ is $\mathbb{C}e_t\oplus\mathbb{C}\vec e_x$, and that generated by the nilpotent $e_t+i\vec e_x$ is $\mathbb{C}e_t\oplus\mathbb{C}(e_t+i\vec e_x)$. What the block loses is the model's guarantee rather than the subalgebras themselves: the model has a two-dimensional subalgebra at **every** element, and the block has one only on the degenerate locus, the algebra of a generic element being the whole space, of complex dimension four. None of these one-generator subalgebras is commutative either, the scalar line included, because the scalar action is conjugate-linear in the second slot; the commutative plane of the model is exactly what that conjugate-linear slot removes.

## The Involution and the Two Halves

### The Star of a Product

**Proposition.** The involution of the multiplication is the plain product in the reversed order:

$$
\boxed{\; (\tilde Q_1\star\tilde Q_2)^{*}=\tilde Q_2\,\overline{\tilde Q_1} , \qquad\text{equivalently}\qquad
\tilde Q_2\star\tilde Q_1=\bigl(\overline{\tilde Q_1}\tilde Q_2\bigr)^{\natural} \;}.
$$

**Proof.** $(\tilde Q_1\star\tilde Q_2)^{*}=(\tilde Q_1^{\natural}\tilde Q_2^{*})^{*}=(\tilde Q_2^{*})^{*}(\tilde Q_1^{\natural})^{*}=\tilde Q_2\,\overline{\tilde Q_1}$, since ${}^{*}$ is an anti-automorphism, ${}^{*2}=\mathrm{id}$ and $(\tilde Q_1^{\natural})^{*}=\overline{\tilde Q_1}$, the two conjugations commuting. The same computation with ${}^{\natural}$ in place of ${}^{*}$ gives the companion identity $(\tilde Q_1\star\tilde Q_2)^{\natural}=\overline{\tilde Q_2}\tilde Q_1$, which is the one used for the associator below.

**Remark.** The sibling identity $(\tilde Q_1\star\tilde Q_2)^{*}=\tilde Q_2\star\tilde Q_1$ does **not** hold here: the star of the product is a value of the plain product and not of the multiplication, and the transposed product involves ${}^{\natural}$ where the star does not. In the language of *The Sesquilinear Product* the multiplication is therefore not Hermitian-symmetric for the involution, and the defect is exactly the insertion of ${}^{\natural}$ in the first slot.

### The Product Does Not Exchange the Halves

The two halves that the involution cuts out of the algebra are the Hermitian and the skew-Hermitian subspaces

$$
\mathbb{M}_+=\{\tilde Q:\tilde Q^{*}=\tilde Q\} , \qquad \mathbb{M}_-=\{\tilde Q:\tilde Q^{*}=-\tilde Q\} ,
$$

of *Hermitian and Skew-Hermitian Elements*, *Introduction to the Remarkable Subspaces* and *Decompositions Along the Remarkable Subspaces*, the fixed and the anti-fixed sets of ${}^{*}$.

**Proposition.** The multiplication does not preserve the two halves: the product of two Hermitian elements can be skew-Hermitian. The square of an element of either half is a scalar, the central scalar $\tilde Q_1^{\natural}\tilde Q_1$ with the sign of the half,

$$
\tilde Q_1\star\tilde Q_1=\Bigl(\sum_{\mu\in\{t,x,y,z\}}Q_{1\mu}^2\Bigr)e_t \ \ (\tilde Q_1\in\mathbb{M}_+) , \qquad
\tilde Q_1\star\tilde Q_1=-\Bigl(\sum_{\mu\in\{t,x,y,z\}}Q_{1\mu}^2\Bigr)e_t \ \ (\tilde Q_1\in\mathbb{M}_-) ,
$$

so in particular the square of an element of either half is fixed by the involution.

**Proof.** For the first clause take $\tilde Q_1=i\vec e_x$ and $\tilde Q_2=i\vec e_y$, both Hermitian; then $\tilde Q_1\star\tilde Q_2=(-i\vec e_x)(i\vec e_y)=\vec e_z$, and $\vec e_z$ is skew-Hermitian, $\vec e_z^{*}=-\vec e_z$. For the second, let $\tilde Q_1=Q_{1t}+\vec Q_1\in\mathbb{M}_+$, so that $Q_{1t}$ is real, $\vec Q_1$ is purely imaginary and $\overline{\tilde Q_1}=\tilde Q_1^{\natural}$, while $\tilde Q_1^{*}=\tilde Q_1$; then $\tilde Q_1\star\tilde Q_1=\tilde Q_1^{\natural}\tilde Q_1^{*}=\tilde Q_1^{\natural}\tilde Q_1=\bigl(\sum_\mu Q_{1\mu}^2\bigr)e_t$, the two factors commuting and $\tilde Q_1^{\natural}\tilde Q_1$ being the central scalar on which the square turns. Let $\tilde Q_1\in\mathbb{M}_-$: then $Q_{1t}$ is purely imaginary and $\vec Q_1$ is real, so $\overline{\tilde Q_1}=-\tilde Q_1^{\natural}$ and $\tilde Q_1^{*}=-\tilde Q_1$, whence $\tilde Q_1\star\tilde Q_1=\tilde Q_1^{\natural}\tilde Q_1^{*}=-\tilde Q_1^{\natural}\tilde Q_1=-\bigl(\sum_\mu Q_{1\mu}^2\bigr)e_t$.

**Remark.** The sibling proves that its product is Hermitian-symmetric, that is that the involution exchanges its two slots, and then reads the two halves as the involution's fixed and anti-fixed subspaces of the multiplication. Here the involution does not exchange the slots, and the halves are the halves of the algebra; the multiplication reads them by the proposition above, which is what is left of the sibling's theorem when the first slot carries the natural conjugation.

### The Other Exchange, and the Two Sesquilinear Halves

The **plain exchange** of the two arguments swaps them, and the proposition above reads the outcome, $\tilde Q_2\star\tilde Q_1=\bigl(\overline{\tilde Q_1}\tilde Q_2\bigr)^{\natural}$: the swapped product is the natural conjugate of a **plain** product, and the value $\tilde Q_1\star\tilde Q_2=(\overline{\tilde Q_2}\tilde Q_1)^{\natural}$ determines only that plain product, whose factorisation is not unique. So the plain exchange is a **genuine reversal**, no conjugation of the value returns it, and its two halves are only $\mathbb{R}$-bilinear and lie in no subspace of the remarkable subspaces; they are the symmetrised product of *The Sesquilinear Symmetrised Product* and the sesquilinear commutator of *The Sesquilinear Commutator*, and they are not the two parts named $\mathrm{SQS}$ and $\mathrm{AQS}$ of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

The **exchange by the coefficientwise conjugation** $c=\overline{\cdot}$, $f^{c}(\tilde Q_1,\tilde Q_2)=c(\tilde Q_2\star\tilde Q_1)$, keeps the class; since $c$ is an automorphism of $\mathbb{B}$ and $c(\tilde Q_2^{\natural})=\tilde Q_2^{*}$, its two halves are the symmetrisation of $\tilde Q_1^{\natural}$ with $\tilde Q_2^{*}$ and half their commutator in the plain product,

$$
\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}+\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr),\qquad
\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}-\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr),
$$

and both are sesquilinear over $\mathbb{C}$: the skew half is the cross product $\vec Q_1\times\overline{\vec Q_2}$, vector-valued, and the symmetric half carries the general quaternionic sesquilinear form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ in its scalar part. They are the conjugate-symmetric and skew-conjugate-symmetric parts of *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, and they **are** the operations $\mathrm{SQS}$ and $\mathrm{AQS}$ of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the biquaternion instance of the two bare halves of both sesqualgebras is *Symmetric and Antisymmetric Decomposition of the Four General Products*, §*The Other Exchange, and the Class It Keeps*.

## The Square, the Idempotents and the Ternary Product

### The Square and the Two Halves

**Proposition.** The square of an element in the multiplication is

$$
\boxed{\; \tilde Q\star\tilde Q=\bigl(\overline{\tilde Q}\tilde Q\bigr)^{\natural}=\tilde Q^{\natural}\tilde Q^{*} \;},
$$

its scalar part is the sum of the four coordinates read at the two equal arguments,

$$
\mathrm{Sc}(\tilde Q\star\tilde Q)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_\mu\overline{Q_\mu}=|Q_t|^2-|Q_x|^2-|Q_y|^2-|Q_z|^2 ,
$$

the three vector squares entering negatively; and on the two halves the square is the central scalar $\tilde Q\star\tilde Q=\pm\bigl(\sum_\mu Q_\mu^{2}\bigr)e_t$, with the sign $+$ on $\mathbb{M}_+$ and the sign $-$ on $\mathbb{M}_-$.

**Proof.** The first display is the two conjugations of the rule read on equal arguments, and the second is the scalar–vector form: the dot product enters negatively and the two vector terms cancel. The scalar part is the scalar part $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ of the four-general-products article with the first factor read through ${}^{\natural}$, which is $\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ at $\tilde Q_1=\tilde Q_2$. The last clause is the proposition of §*The Product Does Not Exchange the Halves*, where the two signs are computed.

**Caution on the two squares.** The square of the sibling product is $\tilde Q\tilde Q^{*}$, it is fixed by the involution ${}^{*}$ for every $\tilde Q$ and its scalar part is the sum of the modulus squares $\sum_\mu|Q_\mu|^{2}$, so that the sums of those squares are the algebraic positive cone of *Hermitian Squares and the Algebraic Positive Cone*. Here the square is **not** fixed by the involution in general, its scalar part is $\sum_\mu\varepsilon_\mu Q_\mu\overline{Q_\mu}$ with the sign vector $\varepsilon=(1,-1,-1,-1)$, and the three vector squares enter the sum negatively, so that no such cone is attached to this multiplication. The square and the double product $\tilde Q^{\natural}\tilde Q$ agree on the two halves, up to the sign of the half, and there the square is a real scalar; on the Hermitian idempotents of the algebra the square nevertheless vanishes, as the next subsection recalls.

### The Idempotents

**Proposition.** The idempotents of the multiplication, the solutions of $\tilde Q\star\tilde Q=\tilde Q$, are the solutions of

$$
\overline{\tilde Q}\,\tilde Q=\tilde Q^{\natural} ,
$$

and among the elements of the quaternion subspace $\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_t+\mathbb{R}\vec e_x+\mathbb{R}\vec e_y+\mathbb{R}\vec e_z$ they are $0$, $e_t$, and the **two-parameter family**

$$
\tilde\Pi(\vec u)=-\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u , \qquad \vec u\in\mathrm{Vect}(\mathbb{B})_{\mathbb{R}} , \quad (\vec u,\vec u)=1 ,
$$

a two-parameter family in the real three-dimensional vector subspace.

**Proof.** The equation $\tilde Q\star\tilde Q=\tilde Q$ reads $(\overline{\tilde Q}\tilde Q)^{\natural}=\tilde Q$; applying ${}^{\natural}$ to both sides, which is an involution, gives the criterion. On the quaternion subspace the coefficients are real, so $\overline{\tilde Q}=\tilde Q^{\natural}$ and the criterion reads $\tilde Q^{2}=\tilde Q^{\natural}$; with $\tilde Q=Q_t+\vec Q$ the plain square is $\bigl(Q_t^{2}-(\vec Q,\vec Q)\bigr)+2Q_t\vec Q$, so the scalar coordinates give $Q_t^{2}-(\vec Q,\vec Q)=Q_t$ and the vector coordinates give $(2Q_t+1)\vec Q=0$. If $\vec Q=0$ then $Q_t\in\{0,1\}$ and the solutions are $0$ and $e_t$; if $\vec Q\neq0$ then $Q_t=-\tfrac12$ and $(\vec Q,\vec Q)=Q_t^{2}-Q_t=\tfrac34$, which is the family.

**Remark.** The idempotents of this multiplication are therefore not the idempotents of the algebra and not the idempotents of the sibling multiplication. The sibling proves that its idempotents are exactly the Hermitian idempotents of the algebra, $0$, $e_t$ and the pure states $\tfrac12(e_t+\tilde\Xi)$ with $\vec u$ a real unit vector; here those elements are **not** idempotent, each of them having $\tilde\Pi\star\tilde\Pi=0$, since it is a zero divisor of the algebra (*N-Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*) and its square in the other product is the central scalar $\tilde Q^{\natural}\tilde Q$. The idempotents here beyond the two trivial ones are the family above, and the family is outside the Hermitian subspace: $\tilde\Pi(\vec u)$ has real vector part, so $\tilde\Pi(\vec u)^{*}\neq\tilde\Pi(\vec u)$. Their central scalar $\tilde Q_1^{\natural}\tilde Q_1$ is $e_t$ and the scalar part of their square is $-\tfrac12$, and they are the elements of $\mathbb{B}$ that are idempotent for the fourth product and for it alone among the four.

### The Ternary Product

**Definition.** The **ternary product** attached to the multiplication is

$$
\{\tilde Q_1,\tilde Q_2,\tilde Q_3\}=(\tilde Q_1\star\tilde Q_2)\star\tilde Q_3^{*}=\overline{\tilde Q_2}\,\tilde Q_1\,\tilde Q_3 ,
$$

the definition $\{x,y,z\}=(x\star y)\star z^{*}$ of *The Sesquilinear Associator and the Ternary Product* read with this multiplication.

**Proposition.** The ternary product is additive in each variable, it is $\mathbb{C}$-linear in the first and the third variables and conjugate-linear in the second, and under the relabelling $\tilde Q\mapsto\tilde Q^{\natural}$ it is the product $x^{*}yz$ of the algebra with its anti-automorphism ${}^{*}$, that is the **left** model of *Algebraic J\*-Algebras* in place of the middle model $xy^{*}z$.

**Proof.** The first display is computed from the rule and the anti-multiplicativity of the two conjugations; the parities are read on the coordinates. For the relabelling, $\overline{\tilde Q_2}\,\tilde Q_1\,\tilde Q_3$ is the left model $x^{*}yz$ with the three slots $(\tilde Q_2^{\natural},\tilde Q_1,\tilde Q_3)$, using $\overline{\tilde Q_2}=\bigl(\tilde Q_2^{\natural}\bigr)^{*}$; and the map ${}^{*}$ is the conjugate-linear involutive anti-automorphism of the algebra, the datum of the construction.

### The Failure of the Jordan Triple Identity

**Proposition.** The ternary product does **not** satisfy the Jordan triple identity

$$
\{x,y,\{u,v,w\}\}=\{\{x,y,u\},v,w\}-\{u,\{y,x,v\},w\}+\{u,v,\{x,y,w\}\}
$$

of *Algebraic J\*-Algebras*. At the basis elements $(x,y,u,v,w)=(e_t,\vec e_x,e_t,\vec e_y,e_t)$ the two sides are $\vec e_z$ and $-3\vec e_z$.

**Proof.** The bar conjugates the coefficients, which are real on the basis, so $\overline{e_t}=e_t$ and $\overline{e_k}=e_k$ for $k=1,2,3$. The left-hand side is $\{e_t,\vec e_x,\{e_t,\vec e_y,e_t\}\}$; the inner bracket is $\overline{\vec e_y}e_t e_t=\vec e_y$, and the outer one is $\overline{\vec e_x}e_t \vec e_y=\vec e_x \vec e_y=\vec e_z$. The right-hand side is $\{\{e_t,\vec e_x,e_t\},\vec e_y,e_t\}-\{e_t,\{\vec e_x,e_t,\vec e_y\},e_t\}+\{e_t,\vec e_y,\{e_t,\vec e_x,e_t\}\}$; the first bracket is $\{e_t,\vec e_x,e_t\}=\overline{\vec e_x}e_t e_t=\vec e_x$, and $\{\vec e_x,\vec e_y,e_t\}=\overline{\vec e_y}\vec e_x e_t=\vec e_y \vec e_x=-\vec e_z$; the middle inner bracket is $\{\vec e_x,e_t,\vec e_y\}=\overline{e_t}\vec e_x \vec e_y=\vec e_x \vec e_y=\vec e_z$, and $\{e_t,\vec e_z,e_t\}=\overline{\vec e_z}e_t e_t=\vec e_z$; the third bracket is again $\vec e_x$, and $\{e_t,\vec e_y,\vec e_x\}=\overline{\vec e_y}e_t \vec e_x=\vec e_y \vec e_x=-\vec e_z$. The sum is $-\vec e_z-\vec e_z-\vec e_z=-3\vec e_z$, which differs from $\vec e_z$.

**Corollary.** The ternary product has the parity of an algebraic $J^{*}$-algebra but not its identity, so the general theorems of *Algebraic J\*-Algebras*, *The Ternary Product as an Operator* and *The Adjoint of the Ternary Product* do not apply to the fourth product's ternary reading. The reason is the one the section *The Product Is Not the Derived Operation* isolates: the model of the theory is the **middle** model $xy^{*}z$, which does satisfy the identity, and the ternary product of this multiplication is the **left** model $x^{*}yz$, the two being the same formula read with the involution in the first rather than in the middle slot. The insertion of ${}^{\natural}$ in the first slot of the multiplication is what transposes the two, and no identity survives the transposition.

**Remark.** The sibling reading has the theorem in the positive direction, its ternary product being the middle model and hence an algebraic $J^{*}$-algebra. Here the same construction applied to the fourth product leaves the class, and the article records the failure rather than the theorem: the binary multiplication and its ternary form are separated for this product as they are not for the general plain sesquilinear one.

### The First Slot Is the Source

The failures of the multiplication are not independent, and the section separates the ones the first slot owns from the ones it does not. Three are the work of the **first slot** alone, and §*The Isotope Interpretation* names them: the absence of a unit on either side (the sibling product has $e_t$ on the right), the failure of the slot exchange of §*The Product Does Not Exchange the Halves*, and the failure of the Jordan triple identity of the ternary reading (the sibling's ternary product is the middle model and satisfies the identity). The same insertion also removes the product's status as the derived operation of the algebra with an involution.

The remaining failures are **not** the first slot's work, and the article says so plainly. Non-commutativity, non-associativity, non-flexibility and the failure of the degree-three identity are shared with the sibling product that inserts nothing in the first slot. On the eight-element basis the general plain sesquilinear product fails associativity on $256$ of the $512$ triples, commutativity on $32$ of the $64$ pairs, flexibility on $32$ of the $64$ pairs and the degree-three identity at $4$ of the $8$ elements; the fourth product fails at exactly the same counts. What separates the two is therefore not composition but the **pair (no unit, no Jordan triple)**: the fourth product loses both, the sibling loses neither.

**Remark (what the synthesis is and is not).** The statement is bookkeeping over the propositions above and not a new theorem. Its value is that it keeps apart two claims that are easy to merge: the **sign vector** $\varepsilon$ of the scalar form, and with it the loss of the unit, is the first slot's, while the **loss of composition** is common to every nontrivial row and is not. The physics band reads the first item as gauge and reads the two no-go results (no unit, no Jordan triple) as the bounds of the fourth corner; those two are the first slot's. Nothing here identifies the first slot as the source of the non-associativity or of the non-closure of the antisymmetric half, both of which the second slot already spoils. The synthesis is the article's; the counts are a computation on a basis and not invariants.

## The Sesqualgebra as an Object

### Simplicity

**Theorem.** The only two-sided ideals of the sesqualgebra $(\mathbb{B},\star)$ are $0$ and $\mathbb{B}$.

**Proof.** Let $I$ be a two-sided ideal, so that $\tilde Q_5\star\tilde Q_1\in I$ and $\tilde Q_1\star\tilde Q_5\in I$ for every $\tilde Q_5\in\mathbb{B}$ and $\tilde Q_1\in I$. The first condition with $\tilde Q_5=e_t$ gives $\tilde Q_1^{*}\in I$, and the second gives $\tilde Q_1^{\natural}\in I$: the ideal is stable under both conjugations. The first condition then reads that $\tilde Q_5^{\natural}\tilde Q_1^{*}\in I$ for every $\tilde Q_5$ and $\tilde Q_1\in I$; as $\tilde Q_1$ runs over $I$ the element $\tilde Q_1^{*}$ runs over $I$, and as $\tilde Q_5$ runs over $\mathbb{B}$ so does $\tilde Q_5^{\natural}$, whence $\mathbb{B}I\subseteq I$. The second condition reads that $\tilde Q_1^{\natural}\tilde Q_5^{*}\in I$, and gives $I\mathbb{B}\subseteq I$ in the same way. Hence $I$ is a two-sided ideal of the ring $\mathbb{B}$, which is simple by *Ideals and Peirce Decompositions of the Biquaternion Algebra*, so $I$ is $0$ or $\mathbb{B}$.

**Remark.** The conclusion is the one the sibling reaches, and by the same route, but the route uses both one-sided actions of $e_t$ here: the star produces the ${}^{*}$-stability and the natural conjugation the ${}^{\natural}$-stability, and neither would suffice alone, since a one-sided ideal condition gives only one of the two. In the theory of *Ideals and Quotients of a Sesqualgebra* the ideals are the two-sided ideals of the algebra, so the answer here is the same as for the two readings already established.

### The Left Multiplications

**Proposition.** The left multiplications $L_{\tilde Q_5}(\tilde Q_1)=\tilde Q_5\star\tilde Q_1$ satisfy

$$
L_{\tilde Q_5}\circ L_{\tilde Q_4}(\tilde Q_1)=\tilde Q_5^{\natural}\,\tilde Q_1\,\overline{\tilde Q_4} ,
$$

so the composition of two of them is $\mathbb{C}$-linear in $\tilde Q_1$ and is not a left multiplication of the multiplication.

**Proof.** $L_{\tilde Q_5}(L_{\tilde Q_4}(\tilde Q_1))=\tilde Q_5^{\natural}\bigl(\tilde Q_4^{\natural}\tilde Q_1^{*}\bigr)^{*}=\tilde Q_5^{\natural}\tilde Q_1\,\overline{\tilde Q_4}$, using ${}^{*2}=\mathrm{id}$ and the anti-multiplicativity. Each $L_{\tilde Q_5}$ is conjugate-linear in its argument, so the composition of two is linear, whereas $L_{\tilde Q_5}$ itself is not; hence no composition equals a left multiplication.

**Corollary.** The left multiplications of the multiplication do **not** form a monoid, and this is the row of *The Four General Products and Their Relations over the Biquaternion Algebra* that reads no for the two sesquilinear products and yes for the two bilinear ones; the sibling article records it from *The Four General Products and Their Relations over the Biquaternion Algebra*, where the composition of two of their left multiplications is shown to leave the class. The product itself is left-linear over $\mathbb{C}$ and the composition is $\mathbb{C}$-linear, so the operator closure of the multiplication is not the multiplication.

### The Scalar Part of the Multiplication

**Proposition.** The scalar part of the multiplication is

$$
\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=\mathrm{Sc}\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}=Q_{1t}\overline{Q_{2t}}-Q_{1x}\overline{Q_{2x}}-Q_{1y}\overline{Q_{2y}}-Q_{1z}\overline{Q_{2z}} ,
$$

and the multiplication is that scalar part read coefficientwise against the basis, with the two signs of the two conjugations.

**Proof.** The scalar part of the product is the scalar part of $\tilde Q_1^{\natural}\tilde Q_2^{*}$, which carries the signs $\varepsilon_\mu$ on the four coefficients; the second display is the definition of the rule read on the basis pairs.

**Remark.** The two scalar parts are separated here as they are in the sibling article: the scalar part of the general plain sesquilinear product is $\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$, while the scalar part of the product of this article carries the signs $\varepsilon_\mu$ in front of the four coefficients, the three vector squares entering negatively. The multiplication is not its scalar part: the scalar part alone does not determine it, and it is the two conjugations that turn the pairings of the coordinates into the product.

## The Four General Products and the Sesquilinear Structure

### Which of the Four Is a Sesquilinear Multiplication

The row of the table of *The Four General Products and Their Relations over the Biquaternion Algebra* headed "multiplication of a sesqualgebra over $\mathbb{C}$" is read with the definition of *Sesqualgebras* and with nothing added to it, and it reads no, no, yes, yes: the two products carrying the star are **both** multiplications of a sesqualgebra over the conjugation, since the first slot of either is read by a map that is $\mathbb{C}$-linear, and the two bilinear products are the trivial-involution collapse of the same definition. The two are separated not by the scalar rules but by the **unit**: the general plain sesquilinear product has $e_t$ on the right, $\tilde Q_1\tilde Q_2^{*}$ with $\tilde Q_2=e_t$ returning $\tilde Q_1$, and the general quaternionic sesquilinear product has not, as §*No Unit on Either Side* proves.

The sharper division is the one of the **derived operation**. The general theory of *Sesqualgebras* builds a multiplication from the algebra and its involution by inserting the involution in the second slot, $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$, and the sibling article proves that the general plain sesquilinear product is that construction for the pair $(\mathbb{B},{}^{*})$. The product of this article inserts the $\mathbb{C}$-linear ${}^{\natural}$ in the first slot as well, and §*The Product Is Not the Derived Operation* proves that this is not the derived operation of any involution of the algebra: condition (i) holds because the first row is the star itself, and condition (ii) fails because it would force ${}^{\natural}$ to be the identity. **The classification of the four** is therefore: one multiplication of an associative unital algebra, the plain product; one multiplication of a sesqualgebra that is the derived operation of the algebra with its star, the general plain sesquilinear product; and the two $\natural$-products, which are the two $\natural$-isotopes of those two, the $\natural$-bilinear product of *Introduction to the General Quaternionic Algebra* and the $\natural$-sesquilinear product of this article.

### The Isotope Interpretation

**Proposition.** The multiplication is the **isotope** of the general plain sesquilinear product determined by the pair $(\natural,\mathrm{id})$:

$$
\tilde Q_1\star\tilde Q_2=\natural(\tilde Q_1)\,\tilde Q_2^{*} \qquad\text{with}\qquad \natural(\tilde Q_1)=\tilde Q_1^{\natural} ,
$$

the insertion of $\natural$ in the first slot being the isotope, and $\natural$ being a $\mathbb{C}$-linear anti-automorphism, an involution and a bijection of $\mathbb{B}$.

**Proof.** The first display is the definition of the product, the isotope of a binary operation being the operation obtained by inserting a pair of bijections, here $\natural$ in the first slot and the identity in the second. The map $\natural$ is $\mathbb{C}$-linear, involutive and anti-multiplicative, $(\tilde Q_1\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1^{\natural}$ (*The Group of Involutions*, *The Biquaternion Algebra and Its Vector Spaces*).

**Remark.** The two sesquilinear products are the derived operation and its $\natural$-isotope, and the two bilinear products are related in exactly the same way; the insertion of a $\mathbb{C}$-linear map changes the product without changing its sesquilinearity type, which is the observation of *The Four General Products and Their Relations over the Biquaternion Algebra*, and it is responsible for the absence of a unit here, for the failure of the slot exchange, and for the failure of the Jordan triple identity: all three are properties of the first slot.

## Summary

The general quaternionic sesquilinear product $\tilde Q_1^{\natural}\tilde Q_2^{*}$ of *The Four General Products and Their Relations over the Biquaternion Algebra*, read as a multiplication, satisfies the two scalar rules of a sesqualgebra over $\mathbb{C}$ with the conjugation, and it is the isotope of the derived operation by the natural conjugation.

$$
\boxed{\ \text{With the general quaternionic sesquilinear product, } \mathbb{B} \text{ is a four-dimensional sesqualgebra over } (\mathbb{C},\varsigma) \text{ with no unit on either side, neither associative nor commutative, and not the derived operation.}\ }
$$

Its two one-sided actions of $e_t$ are the two conjugations, $\tilde Q^{*}$ on the left and $\tilde Q^{\natural}$ on the right, so no element is a unit on either side; its table has the unit followed by the negated quaternion units as first row and as first column, and the quaternion table on the imaginary block; its associator is $\overline{\tilde Q_2}\tilde Q_1\tilde Q_3^{*}-\tilde Q_1^{\natural}\tilde Q_3\overline{\tilde Q_2}$; it is not flexible and not power associative, and its left multiplications do not form a monoid, the composition $L_{\tilde Q_5}\circ L_{\tilde Q_4}$ being the sandwich $\tilde Q_5^{\natural}(\cdot)\overline{\tilde Q_4}$, linear where each $L$ is conjugate-linear. The multiplication is $\mathbb{R}$-bilinear and is not a product of the tensor product $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, being semilinear in its second slot; on the real quaternion subspace it is the reversed conjugate $\overline{qp}$ of the quaternion product; the scalar action $\varphi(A)=Ae_t$ is not multiplicative, $\varphi(z)\star\varphi(w)=\varphi(z\overline{w})$, its image $\mathbb{C}e_t$ is not central, and the centre is trivial, $Z(\mathbb{B})=0$, so the block is a simple sesqualgebra that is not central and not a division algebra, with the nilpotent $e_t+i\vec e_x$ as witness. The star of a product is the plain product in the reversed order, $(\tilde Q_1\star\tilde Q_2)^{*}=\tilde Q_2\overline{\tilde Q_1}$, so the involution does not exchange the two slots; the square is $\bigl(\overline{\tilde Q}\tilde Q\bigr)^{\natural}$, its scalar part is $\sum_\mu\varepsilon_\mu Q_\mu\overline{Q_\mu}$, and on the two halves it is the real scalar $\pm\bigl(\sum_\mu Q_\mu^2\bigr)e_t$, the Hermitian idempotents of the algebra having a vanishing square in the multiplication. The idempotents are $0$, $e_t$ and the family $-\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$ with $(\vec u,\vec u)=1$ in the real vector subspace, the family alone lying outside the Hermitian subspace. The ternary product is $\overline{\tilde Q_2}\tilde Q_1\tilde Q_3$, the left model $x^{*}yz$; it has the parity of an algebraic $J^{*}$-algebra and fails the Jordan triple identity, at $(e_t,\vec e_x,e_t,\vec e_y,e_t)$ with the two sides $\vec e_z$ and $-3\vec e_z$. The sesqualgebra is simple, its ideals being $0$ and $\mathbb{B}$, and its scalar part is $\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$. The generators $\vec e_x,\vec e_y$ present the underlying plain algebra and not the sesqualgebra, and the one-element subalgebra of a generic element is the whole space, of complex dimension four, while the elements of the real quaternion subspace generate only two-dimensional subalgebras; no one-generator subalgebra is commutative.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, read here with the general quaternionic sesquilinear multiplication |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | complex basis; $e_t$ the unit, $e_k$ the quaternion units |
| $i$ | scalar imaginary, $i^2=-1$; central for the plain product, not for the multiplication of this article |
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion and its scalar–vector split, $\vec Q=\sum_kQ_ke_k$ |
| $\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_t+\mathbb{R}\vec e_x+\mathbb{R}\vec e_y+\mathbb{R}\vec e_z$ | the real quaternion subspace, on which $p\star q=\overline{qp}$ |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ | the natural, the coefficientwise and the star conjugation |
| $\varsigma(z)=\bar z$ | the base involution of the sesqualgebra |
| $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*}$ | the general quaternionic sesquilinear product, the multiplication of the article |
| $\varepsilon=(1,-1,-1,-1)$ | the signs of the conjugations on the basis, $Q^{\natural}_\nu=\varepsilon_\nu Q_\nu$ and $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ |
| $\sigma$ | the first row, $\sigma(\tilde Q)=e_t\star\tilde Q=\tilde Q^{*}$ |
| $[\tilde Q_1,\tilde Q_2,\tilde Q_3]$ | the associator, $\overline{\tilde Q_2}\tilde Q_1\tilde Q_3^{*}-\tilde Q_1^{\natural}\tilde Q_3\overline{\tilde Q_2}$ |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the Hermitian and the skew-Hermitian subspaces, the fixed and the anti-fixed sets of ${}^{*}$ |
| $Z(\mathbb{B})=0$ | the centre of the multiplication, trivial |
| $\varphi(A)=Ae_t$ | the scalar action; its image $\mathbb{C}e_t$ is a subalgebra but is not central |
| $\sum_\mu Q_\mu^{2}$ | the central scalar of the square on either half, $\tilde Q\star\tilde Q=\pm\bigl(\sum_\mu Q_\mu^{2}\bigr)e_t$ |
| $\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | the scalar part of the multiplication, with $\varepsilon=(1,-1,-1,-1)$ |
| $\{\tilde Q_1,\tilde Q_2,\tilde Q_3\}=\overline{\tilde Q_2}\tilde Q_1\tilde Q_3$ | the ternary product, the left model $x^{*}yz$ |
| $\tilde\Pi(\vec u)=-\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$, $(\vec u,\vec u)=1$ | the nontrivial idempotents of the multiplication, in the real vector subspace |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the quaternion product whose two conjugations are the two slots of this multiplication.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for semilinear maps, sesquilinear forms and the tensor product of algebras.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the isotopes and homotopes of an algebra, which is the reading of the $\natural$-product used in this article.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions, their parities and the models they define on an associative algebra.
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the product, its coordinate rule and its scalar–vector form.
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the property table, the witnesses and the classification of the four.
- [Introduction to the General Plain Sesqualgebra](introduction-to-the-general-plain-sesqualgebra.html), for the derived operation, the right unit, the slot exchange, the Hermitian idempotents and the algebraic $J^{*}$-algebra of the sibling product.
- [Introduction to the General Quaternionic Algebra](introduction-to-the-general-quaternionic-algebra.html), for the same insertion of ${}^{\natural}$ in a bilinear product, where the square is scalar and the left multiplications form a monoid.
- [The Sesquilinear Associator and the Ternary Product](the-sesquilinear-associator-and-the-ternary-product.html), for the associator and the ternary product of a sesqualgebra, whose model is the middle model $xy^{*}z$.
- *Algebraic J\[-Algebras](algebraic-j-star-algebras.html), for the Jordan triple identity, the two models and the parity of a ternary product.
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the Hermitian idempotents $\tfrac12(e_t+\tilde\Xi)$ of the algebra, which are not idempotent for the multiplication of this article and have a vanishing square in it.
