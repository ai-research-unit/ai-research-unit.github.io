# __The Symmetric and Antisymmetric Parts of a Sesqualgebra Product__

## Introduction

A sesqualgebra product is conjugate-linear in one argument. The product $\star$ of $A$ over the datum $(R,\varsigma)$ is $R$-linear in the first variable and $\varsigma$-semilinear in the second (*Sesqualgebras*, *The Sesquilinear Product*), and like every product of two arguments it carries an exchange, and the exchange cuts the product into the part it fixes and the part it negates. The exchange of a sesqualgebra product is **not** the bare transposition of the two arguments. The transposed product is $\varsigma$-semilinear in the first variable and $R$-linear in the second, the opposite parity, so the two halves of the bare transpose are only $R^{\varsigma}$-bilinear operations and they are not products of the class. The exchange has therefore to be **adapted**: the arguments are exchanged **and the value is conjugated**, the conjugation being a compatible involution $c$ of the module. With the adapted exchange

$$
f^{c}(x,y) := c\bigl(f(y,x)\bigr), \qquad f^{\mathrm s} = \tfrac12\bigl(f + f^{c}\bigr), \qquad f^{\mathrm a} = \tfrac12\bigl(f - f^{c}\bigr),
$$

the two parts $f^{\mathrm s}$ and $f^{\mathrm a}$ are sesquilinear of the original parity again, and they are the **symmetric part** and the **antisymmetric part** of $f$. The split of a sesqualgebra product by the adapted exchange **keeps the sesqualgebra**, and that is what distinguishes it from the bare transposition of the bilinear theory.

This article states the adapted split: the transposition and the two parity classes that force the adaptation, the adapted exchange and its two parts, the reconstruction and the uniqueness, the two exchange-symmetries the two parts detect, the diagonal and the square, the sesquilinearity of the two parts, the derived case and the biquaternion instance. The long development of the same split — the conjugation and its compatibility, the projections of the space of products, the scalar theorem, the structure constants and their count, the standard example of the complex matrices and the collapse in characteristic two — is *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, where the two parts also carry the longer names **conjugate-symmetric** and **skew-conjugate-symmetric**; this article uses the short names of the sesqualgebra and cites that article for the rest. The bilinear case, in which the bare transposition already keeps the class and the conjugation is the identity, is *The Symmetric and Antisymmetric Parts of an Algebra Product*, of which this article is the case of a product with a conjugate-linear slot. The two halves of the **bare** transpose are the symmetrised sesquilinear product $x \circ y$ of *The Sesquilinear Symmetrised Product* and the sesquilinear commutator $[x,y]_{\varsigma}$ of *The Sesquilinear Commutator*, which own those two operations of the fixed ring and are cited rather than repeated.

**Setting and notation.** The setting is that of *Sesqualgebras*, *The Sesquilinear Product* and *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*: $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$ with fixed ring

$$
R^{\varsigma} = \{\lambda \in R : \varsigma(\lambda) = \lambda\},
$$

and $A$ is an $R$-module carrying a $\varsigma$-sesquilinear product $\star$, additive in each variable, $R$-linear in the first and $\varsigma$-semilinear in the second,

$$
(\lambda x) \star y = \lambda\,(x \star y), \qquad x \star (\lambda y) = \varsigma(\lambda)\,(x \star y).
$$

The product need not be associative, commutative or unital. The **conjugation** $c : A \to A$ is additive, involutive, $c^{2} = \mathrm{id}$, and $\varsigma$-semilinear in the sense $c(\lambda x) = \varsigma(\lambda)\,c(x)$; it is the datum the adapted exchange needs, and its compatibility with the involution of the algebra is stated in *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*. The elements fixed and anti-fixed by the involution of the algebra, the Hermitian and the skew-Hermitian ones, are *Hermitian and Skew-Hermitian Elements*; and throughout $2$ is invertible in $R$, so that every halving below is available, exactly as in the bilinear article.

**A note on the word *symmetric*.** Here *symmetric* is said of the **operation**, in the sense that the operation is fixed by the adapted exchange, $f^{\mathrm s}(x,y) = c\bigl(f^{\mathrm s}(y,x)\bigr)$, and not of the elements of $A$; the elements fixed by the involution of the algebra are called **Hermitian**. The longer name for the fixed operation is **conjugate-symmetric**, and the two readings of the word and their occurrences are separated in the Introduction of *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*.

---

## The Transposition and the Two Parity Classes

### The Transposition

**Definition.** Let $f : A \times A \to A$ be additive in each variable. Its **transposition** is the map

$$
E(f)(x,y) := f(y,x).
$$

**Proposition.** The transposition is additive and involutive on the abelian group of the additive maps $A \times A \to A$,

$$
E(f + g) = E(f) + E(g), \qquad E\bigl(E(f)\bigr) = f .
$$

*Proof.* Both statements are read argument by argument from the definition: $E(f+g)(x,y) = (f+g)(y,x) = f(y,x) + g(y,x)$, and $E(E(f))(x,y) = E(f)(y,x) = f(x,y)$. $\square$

**Proposition (the transposition reverses the parity).** Let $f$ be $\varsigma$-sesquilinear. Then its transposition is $\varsigma$-semilinear in the first variable and $R$-linear in the second:

$$
E(f)(\lambda x, y) = \varsigma(\lambda)\,E(f)(x,y), \qquad E(f)(x, \lambda y) = \lambda\,E(f)(x,y).
$$

*Proof.* The first display is the second scalar rule of $\star$ read in the exchanged slots, $E(f)(\lambda x,y) = f(y,\lambda x) = \varsigma(\lambda) f(y,x)$, and the second is the first scalar rule, $E(f)(x,\lambda y) = f(\lambda y, x) = \lambda f(y,x)$. $\square$

**Remark.** Write $\mathrm{Sesq}(A)$ for the $R$-module of the $\varsigma$-sesquilinear products and $\mathrm{Sesq}^{\mathrm{op}}(A)$ for the $R$-module of the additive maps that are $\varsigma$-semilinear in the first variable and $R$-linear in the second, the products of the **opposite parity**. The proposition says that the transposition is a bijection

$$
E : \mathrm{Sesq}(A) \longrightarrow \mathrm{Sesq}^{\mathrm{op}}(A),
$$

so **the transposition does not preserve the class of the product**, and no construction made of it alone can stay inside the sesqualgebra. The two classes coincide exactly in the degenerate case $\bigl(\varsigma(\lambda) - \lambda\bigr)(y \star x) = 0$ for all $\lambda, x, y$, which contains the case $\varsigma = \mathrm{id}$ of the bilinear theory and the case of a product that is identically zero. The obstruction is the reason the exchange is adapted below, and it is the subject of the opening section of *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, §*The Obstruction*.

### The Adapted Exchange

**Definition.** Let $c$ be a conjugation of $A$. The **exchange of $f$ by $c$** is the transposition of the arguments followed by the conjugation of the value,

$$
f^{c} := c \circ E(f), \qquad f^{c}(x,y) = c\bigl(f(y,x)\bigr).
$$

**Proposition (the adapted exchange keeps the class).** Let $f$ be $\varsigma$-sesquilinear and let $c$ be a conjugation. Then $f^{c}$ is $\varsigma$-sesquilinear, of the same parity as $f$; the assignment $f \mapsto f^{c}$ is additive and involutive,

$$
(f + g)^{c} = f^{c} + g^{c}, \qquad (\lambda f)^{c} = \varsigma(\lambda)\, f^{c}, \qquad \bigl(f^{c}\bigr)^{c} = f ,
$$

so that it is an involution of the $R^{\varsigma}$-module of the products of the class.

*Proof.* For the first slot of $f^{c}$,

$$
f^{c}(\lambda x, y) = c\bigl(f(y, \lambda x)\bigr) = c\bigl(\varsigma(\lambda)\, f(y,x)\bigr) = \varsigma\bigl(\varsigma(\lambda)\bigr)\, c\bigl(f(y,x)\bigr) = \lambda\, f^{c}(x,y),
$$

the middle step being the $\varsigma$-semilinearity of $c$ and the last the involution property $\varsigma \circ \varsigma = \mathrm{id}$ of the base involution; the second slot is the same computation with the two scalar rules exchanged, $f^{c}(x, \lambda y) = c\bigl(\lambda f(y,x)\bigr) = \varsigma(\lambda) f^{c}(x,y)$. Additivity and the scalar rule in $f$ are coefficientwise, and the involution is

$$
\bigl(f^{c}\bigr)^{c}(x,y) = c\bigl(f^{c}(y,x)\bigr) = c\bigl(c\bigl(f(x,y)\bigr)\bigr) = f(x,y),
$$

which is $c^{2} = \mathrm{id}$. $\square$

**Remark.** The conjugation repairs the parity that the transposition reverses: the transposition alone carries a sesquilinear product to one of the opposite parity, and composing with $c$ brings it back. The exchange $f \mapsto f^{c}$ is written $\star^{c}$ or $E_{c}(\star)$ in *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, §*The Exchange*, where the compatibility of $c$ with the datum is stated; the identity behind the repaired parity is the display of this proof.

**Remark (the choice of $c$).** On the biquaternions with $(\mathbb{C},\bar{\cdot})$ two conjugations are available, the coefficientwise conjugation $\bar{\cdot}$ and the Hermitian conjugation ${}^{*}$, and they do not give the same split. With $c = {}^{*}$ the exchange of the derived operation returns the product itself, $\tilde{Q}\tilde{P}^{*\,*} = \tilde{P}\tilde{Q}^{*}$, and the split is trivial; with $c = \bar{\cdot}$ the exchange is the natural conjugate of the value, $\overline{\tilde{Q}\tilde{P}^{*}} = \bigl(\tilde{P}\tilde{Q}^{*}\bigr)^{\natural}$, and the split is the one carried out in §*The Biquaternion Instance*. The two candidates are separated in *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, §*The Derived Operation*.

### The Symmetrisation and the Antisymmetrisation

**Definition.** For a product $f$ of the class put

$$
f^{\mathrm s} = \tfrac12\bigl(f + f^{c}\bigr), \qquad f^{\mathrm a} = \tfrac12\bigl(f - f^{c}\bigr).
$$

The **symmetric part** of $f$ is $f^{\mathrm s}$ and its **antisymmetric part** is $f^{\mathrm a}$; read on the arguments,

$$
f^{\mathrm s}(x,y) = \tfrac12\bigl(f(x,y) + c(f(y,x))\bigr), \qquad f^{\mathrm a}(x,y) = \tfrac12\bigl(f(x,y) - c(f(y,x))\bigr).
$$

**Proposition.** Both parts are $\varsigma$-sesquilinear of the class of $f$ and additive in each variable, and for all $x, y \in A$

$$
f^{\mathrm s}(x,y) = c\bigl(f^{\mathrm s}(y,x)\bigr), \qquad f^{\mathrm a}(x,y) = -c\bigl(f^{\mathrm a}(y,x)\bigr),
$$

together with the reconstruction

$$
f = f^{\mathrm s} + f^{\mathrm a}, \qquad f^{c} = f^{\mathrm s} - f^{\mathrm a}, \qquad f - f^{c} = 2\,f^{\mathrm a}.
$$

*Proof.* Sesquilinearity is the proposition of §*The Adapted Exchange* applied to $f$ and to $f^{c}$ and closed under the halves, and additivity is inherited from $f$ coefficient by coefficient. Exchanging $x$ and $y$ in the definition of $f^{\mathrm s}$ and conjugating gives $c\bigl(f^{\mathrm s}(y,x)\bigr) = \tfrac12\bigl(c(f(y,x)) + c^{2}(f(x,y))\bigr) = \tfrac12\bigl(c(f(y,x)) + f(x,y)\bigr) = f^{\mathrm s}(x,y)$, and the antisymmetric display is the same computation with the sign; the reconstruction is the sum and the difference of the two definitions. $\square$

**Theorem (uniqueness of the split).** Suppose $f = s + t$ with $s$ fixed by the exchange, $s(x,y) = c(s(y,x))$, and $t$ negated by it, $t(x,y) = -c(t(y,x))$ for all $x, y$. Then $s = f^{\mathrm s}$ and $t = f^{\mathrm a}$.

*Proof.* Exchanging the arguments in the assumed decomposition and conjugating gives $c(f(y,x)) = s(x,y) - t(x,y)$, because $s$ is fixed and $t$ negated. Adding this relation to $f(x,y) = s(x,y) + t(x,y)$ gives $f(x,y) + c(f(y,x)) = 2s(x,y)$, and subtracting it gives $f(x,y) - c(f(y,x)) = 2t(x,y)$; the two quotients by $2$ are the two parts. The division by $2$ is the only place where the hypothesis on the ring is used. $\square$

**Corollary (what each part detects).** The symmetric part vanishes identically exactly when the product is exchange-**anticommutative**, $f(x,y) = -c(f(y,x))$ for all $x, y$, and the antisymmetric part vanishes identically exactly when it is exchange-**symmetric**, $f(x,y) = c(f(y,x))$.

*Proof.* The first part is zero exactly when $f(x,y) = -c(f(y,x))$ for every pair, which is the first condition; the second is zero exactly when $f(x,y) = c(f(y,x))$. $\square$

**Remark.** The pair of the two parts is the product: to give a product of the class is to give a conjugate-symmetric operation and a skew-conjugate-symmetric one, and the exchange $f \mapsto f^{c}$ is the involution that separates them. Nothing in this section refers to the transposition alone, and the section holds for every product of the class with a conjugation.

### The Diagonal and the Square

**Proposition (the polarisation of the square).** For all $x, y \in A$,

$$
f(x+y, x+y) - f(x,x) - f(y,y) = f(x,y) + f(y,x) = 2\,f^{\mathrm{sym}}(x,y),
$$

where $f^{\mathrm{sym}}(x,y) = \tfrac12\bigl(f(x,y) + f(y,x)\bigr)$ is the **plain** symmetrisation, the half of the bare transposition.

*Proof.* Expand the left-hand side by the additivity in each variable and cancel the two squares:

$$
f(x+y,x+y) = f(x,x) + f(x,y) + f(y,x) + f(y,y).
$$

$\square$

**Remark (the polarisation sees the plain symmetrisation, not the symmetric part).** The right-hand side is twice the plain symmetrisation of *The Sesquilinear Symmetrised Product*, the operation $x \circ y$ of the bare transpose, and it is twice the symmetric part $f^{\mathrm s}$ only when $c$ is the identity, that is in the bilinear case. **The polarisation identity therefore does not recover the symmetric part of a sesqualgebra product**, and it is the first of the two facts of the bilinear theory that the adaptation costs. The reason is that the square of a sum conjugates nothing while the exchange conjugates the value, so the diagonal and the polarisation cannot both see the same operation.

**Proposition (the diagonal is the separated square).** For every $x \in A$,

$$
f^{\mathrm s}(x,x) = \tfrac12\bigl(f(x,x) + c(f(x,x))\bigr), \qquad f^{\mathrm a}(x,x) = \tfrac12\bigl(f(x,x) - c(f(x,x))\bigr).
$$

*Proof.* The definitions at $y = x$. $\square$

**Remark (the antisymmetric part is not zero on the diagonal).** In the bilinear theory the antisymmetric part vanishes identically on the diagonal, $f_{-}(x,x) = \tfrac12(f(x,x) - f(x,x)) = 0$, and that vanishing is what makes the square a function of the symmetric part alone. For a sesqualgebra product the antisymmetric part on the diagonal is the antisymmetrised square $\tfrac12\bigl(f(x,x) - c(f(x,x))\bigr)$, which **need not vanish**: it vanishes exactly when the square of every element is fixed by the conjugation. This is the second fact the adaptation costs, and the two are the same fact read on the diagonal and off it.

**Remark (what the diagonal carries).** The pair $\bigl(f^{\mathrm s}(x,x), f^{\mathrm a}(x,x)\bigr)$ is the decomposition of the square $f(x,x)$ into its part fixed and its part anti-fixed by the conjugation, and both are recovered from the square alone. What is lost is the recovery of the two parts **off** the diagonal from the square map: no polarisation identity recovers the exchange-conjugate symmetrisation, and the diagonal is the one piece of the square that stays. The construction of the two parts is common to an algebra product and to a sesqualgebra product only in the bilinear case; in the general case the exchange is adapted and the square is split by the conjugation instead of by the transposition.

**Remark (the two parts are independent data).** Since a product of the class is an arbitrary pair $(s,t)$ of a conjugate-symmetric and a skew-conjugate-symmetric operation by the uniqueness theorem, **a condition imposed on the symmetric part imposes nothing on the antisymmetric part and conversely**. The independence is inherited from the definitions, and the two projections of the space of products onto its two halves are stated in *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, §*The Two Projections*, where they are idempotent, orthogonal and sum to the identity.

### The Two Parts Under Their Own Names

**Remark.** On a sesqualgebra the symmetric part and the antisymmetric part of the product $\star$ have their own names and their own articles.

- The symmetric part is the **conjugate-symmetric part** of the product relative to $c$,
$$
f^{\mathrm s}(x,y) = \tfrac12\bigl(x \star y + c(y \star x)\bigr),
$$
the operation fixed by the adapted exchange; its diagonal is the part of the square fixed by the conjugation.
- The antisymmetric part is the **skew-conjugate-symmetric part**,
$$
f^{\mathrm a}(x,y) = \tfrac12\bigl(x \star y - c(y \star x)\bigr),
$$
the operation negated by the adapted exchange; its diagonal is the antisymmetrised square.

The two are developed, with the scalar theorem, the projections and the standard example, in *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*; the reconstruction $x \star y = f^{\mathrm s}(x,y) + f^{\mathrm a}(x,y)$ is the display at the opening of §*Definition and Reconstruction* there.

**Remark (the two operations of the bare transpose, and why they are not the two parts).** The transposition alone defines two further operations, the **symmetrised sesquilinear product**

$$
x \circ y := \tfrac12\bigl(x \star y + y \star x\bigr)
$$

of *The Sesquilinear Symmetrised Product* and the **sesquilinear commutator**

$$
[x,y]_{\varsigma} := x \star y - y \star x
$$

of *The Sesquilinear Commutator*, whose correction term $\bigl(\lambda - \varsigma(\lambda)\bigr)(y \star x)$ is the whole difference from the bilinear case and whose Jacobi identity fails. By the proposition of §*The Transposition and the Two Parity Classes* the two are only $R^{\varsigma}$-bilinear and are not products of the sesqualgebra. **They are the two halves of the bare transpose and not the two parts of the product**, and the plain reconstruction

$$
x \star y = x \circ y + \tfrac12\,[x,y]_{\varsigma}
$$

is the reconstruction of that bare split. The corpus reads the twelve operations of the biquaternion space under the adapted exchange; the plain operations keep their own articles and their own laws, and the contrast between the two readings of the same product is the subject of §*The Adapted Exchange* of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.

---

## The Split Keeps the Class

### The Two Parts Are Sesquilinear

**Proposition.** Let $\star$ be $\varsigma$-sesquilinear and let $\star^{\mathrm s}$ and $\star^{\mathrm a}$ be its two parts under the adapted exchange. Then both are $\varsigma$-sesquilinear of the class of $\star$: for $\lambda \in R$,

$$
(\lambda x) \star^{\mathrm s} y = \lambda\,(x \star^{\mathrm s} y), \qquad x \star^{\mathrm s} (\lambda y) = \varsigma(\lambda)\,(x \star^{\mathrm s} y),
$$

and the same two rules hold for $\star^{\mathrm a}$.

*Proof.* This is the proposition of §*The Adapted Exchange* for $\star^{c}$, closed under the half-sum and the half-difference. $\square$

**Remark.** The proposition is the substance of the article. **A sesqualgebra product is split into two parts and the two parts are products of the sesqualgebra**: the split does not leave the class, and the closure that the bare transpose loses by the correction term $\tfrac12\bigl(\varsigma(\lambda) - \lambda\bigr)(y \star x)$ is restored by the conjugation of the value. The four operations $\mathrm{SPS}$, $\mathrm{APS}$, $\mathrm{SQS}$ and $\mathrm{AQS}$ of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* are the four parts of the two biquaternion sesqualgebra products under this exchange, and they are sesquilinear over $(\mathbb{C},\bar{\cdot})$; the four parts of the **bare** split, which are only $\mathbb{R}$-bilinear and are not sesqualgebra products, are the readings of *The 12 Products of the Biquaternion Complex Space*, where the split is carried by the order symmetry.

**Remark (the count).** The two parts of a product of the class are not an independent pair of a symmetric and an antisymmetric **bilinear** map, as in the algebra article: the space of products of the class is the direct sum of its conjugate-symmetric and its skew-conjugate-symmetric elements, both of which are sesquilinear, so the two halves are of equal size. On a free module of rank $n$ over the fixed field the two arrays of structure constants each have rank $n^{3}$ entries relative to the split of the constants by the transposition and the conjugation together, which is the count of *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, §*The Count*.

### The Values in the Derived Case

**Definition.** The standard example of *Sesqualgebras* is the **derived operation** of an associative $R$-algebra $A$ with a $\varsigma$-semilinear involution $*$, that is the product

$$
x \star y := x\,y^{*},
$$

where the juxtaposition is the associative product, $R$-linear in the first variable and $\varsigma$-semilinear in the second.

**Proposition.** Let $c$ be a conjugation of $A$ and let $\star$ be the derived operation. Then

$$
\star^{c}(x,y) = c\bigl(yx^{*}\bigr), \qquad
\star^{\mathrm s}(x,y) = \tfrac12\bigl(xy^{*} + c(yx^{*})\bigr), \qquad
\star^{\mathrm a}(x,y) = \tfrac12\bigl(xy^{*} - c(yx^{*})\bigr),
$$

and if $c$ is an automorphism of the associative product this reads $\star^{c}(x,y) = c(y)\,c(x^{*})$.

*Proof.* Substitute the derived operation in the adapted exchange: $\star^{c}(x,y) = c\bigl(\star(y,x)\bigr) = c(yx^{*})$, and the two halves are the definitions; the last display is the multiplicativity of an automorphism $c$. $\square$

**Remark (the two twists, and which one carries information).** The algebra carries the involution $*$ itself as a second conjugation, and with it the exchange $\star \mapsto \star^{*}$, $\star^{*}(x,y) = \bigl(\star(y,x)\bigr)^{*}$. For the derived operation this exchange does nothing,

$$
\bigl(\star(y,x)\bigr)^{*} = \bigl(yx^{*}\bigr)^{*} = xy^{*} = \star(x,y),
$$

so the derived operation is fixed by the $*$-exchange and its split by that exchange is trivial. **The derived operation is conjugate-symmetric in the $*$-sense automatically, and it is the other conjugation — the one whose fixed ring contains the scalars — that carries the split.** The two exchanges must not be confused, and it is the second that this article uses; the computation is *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, §*The Derived Operation*.

**Remark (the Hermitian half in the derived case).** When $c$ is the identity of the algebra the symmetric part is the plain symmetrisation, $\star^{\mathrm s}(x,y) = \tfrac12(xy^{*} + yx^{*})$, which takes Hermitian values, $(\star^{\mathrm s}(x,y))^{*} = \star^{\mathrm s}(x,y)$, and the antisymmetric part skew-Hermitian values; that is the bilinear-certificate case of the algebra article, where the two halves are the Hermitian and the skew-Hermitian parts of the value. For a genuine sesqualgebra with $c \neq \mathrm{id}$ the two parts are not the Hermitian and the skew-Hermitian parts in general, and the symmetric part carries the scalar part of the product rather than the Hermitian part of the value: the scalar theorem of *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, §*The Scalar Theorem*, says that the whole scalar form of a derived operation lies in the symmetric part, whereas the plain split distributes only the even part of that form into its symmetric half.

---

## The Biquaternion Instance

The complex space of the biquaternion algebra carries two sesqualgebra products over $(\mathbb{C},\bar{\cdot})$, the sesquilinear one $\tilde{P}\tilde{Q}^{*}$ and the general quaternionic sesquilinear one $\tilde{P}^{\natural}\tilde{Q}^{*}$. Their base involution is the complex conjugation and their conjugation is the coefficientwise conjugation $\bar{\cdot}$, so their adapted exchange is the transposition of the two arguments followed by $\bar{\cdot}$, and the two parts of each are the four operations $\mathrm{SPS}$, $\mathrm{APS}$, $\mathrm{SQS}$ and $\mathrm{AQS}$ of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

- For the **sesquilinear product** the exchange is the natural conjugation of the value, $\overline{\tilde{Q}\tilde{P}^{*}} = \bigl(\tilde{P}\tilde{Q}^{*}\bigr)^{\natural}$, so the two parts are the scalar and the vector part of the one value:
$$
\mathrm{SPS} = \tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+\overline{\tilde{Q}\tilde{P}^{*}}\bigr) = \mathrm{Sc}\bigl(\tilde{P}\tilde{Q}^{*}\bigr) = P_0\overline{Q_0} + (\mathbf{P},\overline{\mathbf{Q}}), \qquad
\mathrm{APS} = \tfrac12\bigl(\tilde{P}\tilde{Q}^{*}-\overline{\tilde{Q}\tilde{P}^{*}}\bigr) = \mathrm{Vect}\bigl(\tilde{P}\tilde{Q}^{*}\bigr) = -P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}},
$$
respectively **central** and **pure vector**. The symmetric part is the Hermitian form $H = \mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$ of *Biquaternion Norm and Invertibility* read as a product, and the antisymmetric part is the whole vector part $-P_0\overline{\mathbf{Q}} + \overline{Q_0}\mathbf{P} - \mathbf{P}\times\overline{\mathbf{Q}}$.
- For the **general quaternionic sesquilinear product** the exchange is not a conjugation of the value, and the two parts are the symmetrisation and half the commutator of two elements in the plain product,
$$
\mathrm{SQS} = \tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*} + \tilde{Q}^{*}\tilde{P}^{\natural}\bigr), \qquad
\mathrm{AQS} = \tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*} - \tilde{Q}^{*}\tilde{P}^{\natural}\bigr),
$$
since $\overline{\tilde{Q}^{\natural}\tilde{P}^{*}} = \tilde{Q}^{*}\tilde{P}^{\natural}$. The antisymmetric part is the cross product $\mathbf{P}\times\overline{\mathbf{Q}}$, **pure vector**; the symmetric part carries the general quaternionic sesquilinear form $K = P_0\overline{Q_0} - (\mathbf{P},\overline{\mathbf{Q}})$ in its scalar part and $-\bigl(P_0\overline{\mathbf{Q}} + \overline{Q_0}\mathbf{P}\bigr)$ in its vector part, and it lies in **no** subspace of the six.

The two parts of each of the four general products are written in scalar–vector form, and the four operations are read, with their laws, in *The 12 Products of the Biquaternion Complex Space*, and named in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. The two $\mathbb{C}$-bilinear products of the space have the trivial base involution, so their exchange is the bare transposition and their parts are the same under either reading: the plain and the quaternionic algebra rows $\mathrm{SPA}$, $\mathrm{APA}$, $\mathrm{SQA}$ and $\mathrm{AQA}$ are unchanged by the adaptation, and the adaptation touches only the four sesqualgebra parts.

**Remark (the twelve and the ten).** On the **real** part of the space, where the coefficientwise conjugation acts trivially, the two readings of the exchange coincide, and two pairs of the twelve operations coincide: the central forms agree, $\mathrm{SQA} = \mathrm{SPS}$, and the two cross products agree, $\mathrm{APA} = \mathrm{AQS}$. The twelve are pairwise distinct on the complex space and fall to ten on the real part; the count and the coincidences are *The 12 Products of the Biquaternion Complex Space*, §*The Twelve Are Distinct, and Ten on the Real Part*.

---

## Degenerations

**Remark (the bilinear case).** When the base involution is trivial, $\varsigma = \mathrm{id}$, the conjugation $c$ that carries information is the identity, the adapted exchange is the bare transposition, the two classes coincide, and every statement of this article is a statement of *The Symmetric and Antisymmetric Parts of an Algebra Product*: the two projections are projections of the space of products, the direct sum $S^{2} A \oplus \Lambda^{2} A$ is available, the antisymmetric part vanishes on the diagonal, and the polarisation recovers the symmetric part. The present article is therefore the general form of which the bilinear article is the case of two slots of the same type, and the case of a trivial conjugation.

**Remark (the derived operation and the trivial conjugation).** When the conjugation is the involution that generates the derived operation, the exchange fixes the product, the symmetric part is the product and the antisymmetric part is zero; the split is then trivial and carries no information, exactly as in §*The Values in the Derived Case*. The interesting conjugation is the one that is not the generating involution.

**Remark (the trivial product).** When the product is identically zero the two parts are zero and the reconstruction is trivial; the obstruction of §*The Transposition and the Two Parity Classes* is then vacuous, since its correction term contains $y \star x$.

**Remark (characteristic two).** If $2 = 0$ in $R$ then $-1 = 1$, the exchange and its negative coincide, and the two parts $f^{\mathrm s}$ and $f^{\mathrm a}$ are equal, being $\tfrac12(f \pm f^{c})$ with the two signs indistinguishable. The projections are then unavailable, since they are built from $\tfrac12$, and the split of this article does not exist.

**Remark (the general commutative ring).** The construction needs $\tfrac12$, not a field, and it needs the conjugation $c$ with its $\varsigma$-semilinearity and its involution; over a commutative ring in which $2$ is invertible the whole of the article goes through unchanged, with $R^{\varsigma}$ the fixed ring of the involution. The statements on the forms of the biquaternion instance specialise $R = \mathbb{C}$ and $\varsigma$ the complex conjugation.

---

## Where the Corpus Uses the Split

The split is used at several places in the corpus, and each use is recorded in the article that owns it.

**The two parts of the sesqualgebra.** The conjugate-symmetric and the skew-conjugate-symmetric parts, their existence, their uniqueness and their scalar theorem are *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, which owns the adapted exchange and its development. This article owns the definition of the two parts as the halves of the adapted exchange and the reading of the biquaternion instance.

**The two operations of the bare transpose.** The symmetrised sesquilinear product $x \circ y$ and the sesquilinear commutator $[x,y]_{\varsigma}$ are *The Sesquilinear Symmetrised Product* and *The Sesquilinear Commutator*, which own those two operations of the fixed ring, their scalar rules, the closure of the Hermitian elements, the values of the bracket in the skew-Hermitian part and the failure of the Jacobi identity. They are the halves of the bare transpose and not the two parts of the product, and the two readings are compared in §*The Adapted Exchange* of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.

**The squares and the cone.** The diagonal of the split in the derived case is the square and the cone of the squares is its image in the fixed set of the conjugation; the construction is *Hermitian Squares and the Algebraic Positive Cone*, and the two must not be confused with the two halves of the involution of the elements.

**The biquaternion instance.** The four parts of the two sesqualgebra products of the biquaternion algebra and their scalar–vector forms, and the twelve operations with their names and their laws, are *The 12 Products of the Biquaternion Complex Space*; the order-symmetry reading of the same four parts is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.

---

## Summary

A $\varsigma$-sesquilinear product on an $R$-module $A$ is split into a symmetric part and an antisymmetric part by the **adapted exchange**, the transposition of the two arguments followed by the conjugation of the value,

$$
f^{c}(x,y) = c\bigl(f(y,x)\bigr), \qquad f^{\mathrm s} = \tfrac12\bigl(f + f^{c}\bigr), \qquad f^{\mathrm a} = \tfrac12\bigl(f - f^{c}\bigr),
$$

with the reconstruction $f = f^{\mathrm s} + f^{\mathrm a}$, the uniqueness of the pair and the sentence that the symmetric part is fixed and the antisymmetric part negated by the exchange. The exchange is adapted and not bare because the bare transposition of a sesquilinear product has the **opposite parity**: it is semilinear in the first variable and linear in the second, so the two halves of the bare transpose are only $R^{\varsigma}$-bilinear and are not products of the class. The conjugation repairs the parity, $(f^{c})^{c} = f$, and the two parts are $\varsigma$-sesquilinear again: **the split of a sesqualgebra product by the adapted exchange keeps the sesqualgebra**, the two parts are conjugate-symmetric and skew-conjugate-symmetric, and the two operations of the bare transpose are the symmetrised sesquilinear product $x \circ y$ and the sesquilinear commutator $[x,y]_{\varsigma}$, which are not the two parts.

Two facts of the bilinear theory are paid for by the adaptation. The polarisation of the square polarises the **plain** symmetrisation and not the symmetric part, and the antisymmetric part does not vanish on the diagonal: it is the antisymmetrised square, which vanishes exactly when the square of every element is fixed by the conjugation. The diagonal of the split is the decomposition of the square by the conjugation into its fixed and its anti-fixed part, and both are recovered from the square alone, while the recovery of the two parts off the diagonal from the square map is lost. On the biquaternion space the two parts of the sesquilinear product are the scalar part and the vector part of the value, $\mathrm{SPS} = \mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$ in the centre and $\mathrm{APS} = \mathrm{Vect}(\tilde{P}\tilde{Q}^{*})$ in the vector subspace, and the two parts of the general quaternionic sesquilinear product are the symmetrisation and half the commutator of $\tilde{P}^{\natural}$ with $\tilde{Q}^{*}$, whose antisymmetric half is the cross product $\mathbf{P}\times\overline{\mathbf{Q}}$. The two $\mathbb{C}$-bilinear products have the trivial base involution, their exchange is the bare transposition, and the four algebra parts $\mathrm{SPA}$, $\mathrm{APA}$, $\mathrm{SQA}$ and $\mathrm{AQA}$ are unchanged. The twelve operations are pairwise distinct on the complex space and fall to ten on the real part, where $\mathrm{SQA} = \mathrm{SPS}$ and $\mathrm{APA} = \mathrm{AQS}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $\varsigma$, $R^{\varsigma}$ | A commutative ring with $1$; an involution of $R$; its fixed ring $\{\lambda : \varsigma(\lambda) = \lambda\}$ |
| $A$, $\star$ | An $R$-module; a $\varsigma$-sesquilinear product, $R$-linear in the first variable and $\varsigma$-semilinear in the second |
| $c$ | A conjugation of $A$: additive, involutive, $c(\lambda x) = \varsigma(\lambda)c(x)$ |
| $E(f)(x,y) = f(y,x)$ | The bare transposition; additive and involutive; it reverses the parity |
| $f^{c}(x,y) = c\bigl(f(y,x)\bigr)$ | The adapted exchange; an involution of the class of products |
| $\mathrm{Sesq}(A)$, $\mathrm{Sesq}^{\mathrm{op}}(A)$ | The products of the class and the products of the opposite parity; the transposition is a bijection between them |
| $f^{\mathrm s} = \tfrac12(f + f^{c})$ | The symmetric part of $f$, the conjugate-symmetric part |
| $f^{\mathrm a} = \tfrac12(f - f^{c})$ | The antisymmetric part of $f$, the skew-conjugate-symmetric part |
| $f = f^{\mathrm s} + f^{\mathrm a}$ | The reconstruction; the two parts determine the product |
| $f^{\mathrm s}(x,y) = c(f^{\mathrm s}(y,x))$, $f^{\mathrm a}(x,y) = -c(f^{\mathrm a}(y,x))$ | The two exchange-symmetries the parts satisfy |
| $f^{\mathrm s}(x,x) = \tfrac12(x \star x + c(x \star x))$ | The diagonal of the symmetric part: the fixed part of the square |
| $f(x{+}y,x{+}y) - f(x,x) - f(y,y) = 2f^{\mathrm{sym}}(x,y)$ | The polarisation of the square: it recovers the plain symmetrisation |
| $x \circ y = \tfrac12(x \star y + y \star x)$ | The symmetrised sesquilinear product, the half of the bare transpose (*The Sesquilinear Symmetrised Product*) |
| $[x,y]_{\varsigma} = x \star y - y \star x$ | The sesquilinear commutator, the other half of the bare transpose (*The Sesquilinear Commutator*) |
| $x \star y = x y^{*}$ | The derived operation of an associative algebra with a $\varsigma$-semilinear involution $*$ |
| $\mathrm{SPS}$, $\mathrm{APS}$, $\mathrm{SQS}$, $\mathrm{AQS}$ | The four parts of the two biquaternion sesqualgebra products, read in *The 12 Products of the Biquaternion Complex Space* and named in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* |
| $\mathrm{SPS}=\tfrac12(\tilde{P}\tilde{Q}^{*}+\overline{\tilde{Q}}\tilde{P}^{\natural})=\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$ | The symmetric part of the plain sesquilinear product, central |
| $\mathrm{AQS} = \mathbf{P}\times\overline{\mathbf{Q}}$ | The antisymmetric part of the general quaternionic sesquilinear product, pure vector |

## Further Reading

- N. Bourbaki, *Algèbre*, Chapitre IX: *Formes sesquilinéaires et formes quadratiques* (Hermann, 1959), for the sesquilinear forms, the base ring with involution and the symmetric and alternating parts of a Hermitian form.
- W. Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften **270** (Springer, 1985), for the conjugate module, the fixed ring of an involution and the forms carried by the two parities.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications **44** (American Mathematical Society, 1998), for the involutions of an algebra, the conjugations they define and the fixed sets that carry the scalars.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the symmetrisation and the antisymmetrisation of a product in the bilinear case, of which this article is the sesquilinear form.
- Nathan Jacobson, *Lie Algebras* (Interscience, 1962), for the commutator of an associative algebra, the Jacobi identity and the reason the antisymmetrisation of a sesquilinear product is a bracket only over the fixed ring.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the symmetrised product, the polarisation of its square and the Jordan identity on the Hermitian part.
