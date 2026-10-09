# __The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product__

## Introduction

A bilinear product is split into two halves by one operation and its inverse: the **exchange** of the two arguments of a pair. The product of a sesqualgebra is conjugate-linear in one argument, and there the exchange of the arguments alone **fails**: the transposed product is $\varsigma$-semilinear in the first slot and $R$-linear in the second, the opposite parity, so it is not a $\varsigma$-sesquilinear product and the two halves of the plain split are $R^{\varsigma}$-bilinear maps and not products of the class. The symmetry has therefore to be **adapted**: the arguments are exchanged *and the value is conjugated*, and the conjugation is supplied by a second operation of the algebra, a compatible involution $c$.

The adaptation presents the shape of the bilinear theory but not its arithmetic. The exchange is an involution of the class of products, the split is unique, the two projections of the space of products are idempotent and orthogonal, and each half can be prescribed independently — all of this carries over untouched. What changes is the scalar part: the conjugate-symmetric half carries the whole of the scalar part of the product, once the scalar form is Hermitian, whereas the plain split distributes only the even part of that form into its symmetric half. What does not carry over is the **polarisation of the square**: the identity $(x+y)\star(x+y) - x\star x - y\star y = x\star y + y\star x$ polarises the plain symmetrisation and not the exchanged one, and the diagonal of the adapted split is the part of the square fixed by the conjugation rather than the square itself.

This article develops the obstruction, the adaptation and its uniqueness, the two halves, the two projections, the scalar theorem, the constants of the exchange and their count, the square, the standard example with the complex matrices and the biquaternion products, and the collapse outside characteristic not two. It is the sesquilinear companion of *The Symmetric and Antisymmetric Parts of an Algebra Product*: that article is the case $\varsigma = \mathrm{id}$ of this one, where the conjugation is the identity and the exchange is the plain one, and the two agree exactly on the bilinear products.

The setting and the notation are those of *Sesqualgebras* and *The Sesquilinear Product*: $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$ with fixed ring $R^{\varsigma} = \{\lambda : \varsigma(\lambda) = \lambda\}$, and $A$ is an $R$-module carrying a $\varsigma$-sesquilinear product $\star$, additive in each variable, $R$-linear in the first variable and $\varsigma$-semilinear in the second. The product need not be associative, commutative or unital. The transposed product, the difference bracket $[x,y]_{\varsigma} = x\star y - y\star x$ and the structure constants $c^{k}{}_{ij}$ are those of *The Sesquilinear Product*; the two halves of the involution of the algebra are *Hermitian and Skew-Hermitian Elements*; the plain symmetrisation and the plain difference of this product are *The Sesquilinear Symmetrised Product* and *The Sesquilinear Commutator*, which own those two operations and are cited rather than repeated. The bilinear theory that this article adapts is *The Symmetric and Antisymmetric Parts of an Algebra Product*; the equation of the two halves with the fixed and the anti-fixed sets of an involution is the construction of *Involutive Algebras*, and the ternary product forced by the failure of associativity of the standard example is *The Sesquilinear Associator and the Ternary Product*. Throughout, $2$ is invertible in $R$, so that every halving below is available.

The adjectives need fixing at the outset, because the corpus uses the word *Hermitian* for two different things and *conjugate-symmetric* for a third. On the side of the **elements**, the Hermitian elements are the fixed set of the involution $*$ of the algebra, $H(A) = \{x : x^{*} = x\}$, and they are *Hermitian and Skew-Hermitian Elements*. On the side of the **product**, *The Sesquilinear Product* calls the halves of the plain split the Hermitian and the skew-Hermitian parts, because the symmetrised part takes Hermitian values and the difference skew-Hermitian values; that is a statement about the *values* of an operation. Finally, on the side of a **form**, *Hermitian Geometry and the Unitary Group* calls a form conjugate-symmetric when $h(x,y) = \overline{h(y,x)}$. Here a fourth reading is used, a statement about the *operation*: a product is **conjugate-symmetric** when it is fixed by an exchange of its arguments twisted by a conjugation of the algebra. The four are different, §*The Two Halves* says where they part and where the third and the fourth agree, and the word *conjugate-symmetric* is reserved for the operation throughout.

---

## The Obstruction

### The Transposed Product Has the Opposite Parity

**Proposition (the transposed product has the opposite parity).** The map $(x, y) \mapsto y \star x$ is $\varsigma$-semilinear in the first variable and $R$-linear in the second, so it is the $R$-bilinear map $A^{\varsigma} \times A \to A$ of *The Sesquilinear Product*, §*The Transposed Product*, where the statement is proved. For $\lambda \in R$,

$$
y \star (\lambda x) = \varsigma(\lambda)\,(y \star x), \qquad (\lambda y) \star x = \lambda\,(y \star x).
$$

It is a $\varsigma$-sesquilinear product of the original parity exactly in the degenerate case $\bigl(\varsigma(\lambda) - \lambda\bigr)(y \star x) = 0$ for all $\lambda, x, y$.

*Proof.* The two displays are the two scalar rules of *Sesqualgebras* read in the exchanged slots, and the degenerate case is read off them: semilinearity and linearity in the first slot agree exactly when $\varsigma(\lambda)(y\star x) = \lambda(y\star x)$ for all $\lambda$ and all $y, x$. $\square$

**Remark.** The reversal of the parity is the product-level form of the asymmetry of the opposite sesqualgebra, and it is already recorded in *The Sesquilinear Product*, §*The Transposed Product*. It is the whole obstruction of this article: **for a sesquilinear product the transposition of the two arguments is not an operation of the class**, and no construction built on it alone can be a symmetry of the class. The fact is due to *The Sesquilinear Product* and is recalled here because this article is built on the repair of it. For $\varsigma = \mathrm{id}$ the two parities coincide, the transposed product is a product, and the obstruction disappears; that is the bilinear case of *The Symmetric and Antisymmetric Parts of an Algebra Product*.

### The Plain Split

**Proposition (the plain halves are $R^{\varsigma}$-bilinear).** Put

$$
\star^{\mathrm{sym}}(x,y) = \tfrac12\bigl(x \star y + y \star x\bigr), \qquad
\star^{\mathrm{dif}}(x,y) = x \star y - y \star x .
$$

Then $\star = \star^{\mathrm{sym}} + \tfrac12 \star^{\mathrm{dif}}$, the first operation is symmetric and the second antisymmetric, and both are $R^{\varsigma}$-bilinear. Neither is $\varsigma$-sesquilinear of the original parity unless the product is degenerate.

*Proof.* The reconstruction and the symmetry are the definitions. For the scalar of the first operation in the first slot,

$$
(\lambda x) \star^{\mathrm{sym}} y = \tfrac12\Bigl(\lambda\,(x \star y) + \varsigma(\lambda)\,(y \star x)\Bigr),
$$

which is $\lambda\star^{\mathrm{sym}}(x,y)$ when $\varsigma(\lambda) = \lambda$ and not otherwise; the second slot is the same computation, and the difference is the difference of the two. $\square$

**Remark.** The two halves are therefore operations of the wrong kind: they are bilinear over the fixed ring and nothing more. They are not new objects — the symmetric half is the **symmetrised sesquilinear product** and half the antisymmetric one is the **sesquilinear commutator**, and they are developed, with their scalar rules, their Jordan property on the Hermitian part and their failure of the Jacobi identity, in *The Sesquilinear Symmetrised Product* and *The Sesquilinear Commutator*. Those two articles are the theory of the plain split, and this article takes them as read. The plain split is the literal analogue of the bilinear one and it does not stay in the category; the rest of the article is the repair.

### The Scalar Form Under the Plain Split

**Proposition.** Let $\varepsilon : A \to R$ be additive with $\varepsilon(\lambda x) = \lambda \varepsilon(x)$ for $\lambda \in R$, and put $s = \varepsilon \circ \star$. Then

$$
\varepsilon\bigl(\star^{\mathrm{sym}}(x,y)\bigr) = \tfrac12\bigl(s(x,y) + s(y,x)\bigr), \qquad
\tfrac12\,\varepsilon\bigl(\star^{\mathrm{dif}}(x,y)\bigr) = \tfrac12\bigl(s(x,y) - s(y,x)\bigr).
$$

*Proof.* Apply $\varepsilon$ to the two definitions and use its additivity and its linearity over $R$. $\square$

**Proposition (the Hermitian case).** Suppose in addition that the form $s$ is $\varsigma$-**Hermitian**, that is $s(y,x) = \varsigma(s(x,y))$ for all $x, y$. Then

$$
\varepsilon\bigl(\star^{\mathrm{sym}}(x,y)\bigr) = \tfrac12\bigl(s(x,y) + \varsigma(s(x,y))\bigr), \qquad
\tfrac12\,\varepsilon\bigl(\star^{\mathrm{dif}}(x,y)\bigr) = \tfrac12\bigl(s(x,y) - \varsigma(s(x,y))\bigr),
$$

the $\varsigma$-even and the $\varsigma$-odd parts of the form. Over $\mathbb{C}$ with $\varsigma$ the conjugation these are $\operatorname{Re} s$ and $i\operatorname{Im} s$.

*Proof.* Substitute the Hermitian condition $s(y,x) = \varsigma(s(x,y))$ in the preceding display. Over $\mathbb{C}$ the $\varsigma$-even part of a complex number is its real part and the $\varsigma$-odd part is $i$ times its imaginary part. $\square$

**Remark.** The scalar form of a sesquilinear product is Hermitian as soon as the product is the standard one, and the standard example below proves it. What the plain split does to that form is therefore the classical arithmetic of a Hermitian form: its real part is a symmetric bilinear form and its imaginary part is an alternating one, and the plain split separates exactly those two. **The plain split of the scalar form is the split into its symmetric and its alternating real parts, and it is not the split into the two parts of the product.** The next section gives the exchange for which the whole form, and not only its even part, falls on one side.

---

## The Adapted Exchange

### The Conjugation

**Definition.** A **conjugation** of $A$ over the datum $(R,\varsigma)$ is a map $c : A \to A$ that is additive, $\varsigma$-semilinear in the sense

$$
c(\lambda x) = \varsigma(\lambda)\,c(x) \qquad (\lambda \in R,\ x \in A),
$$

and involutive, $c^2 = \mathrm{id}$.

**Proposition.** A conjugation is an $R$-linear isomorphism $A^{\varsigma} \to A$, from the conjugate module of *Sesqualgebras* into $A$. In particular $c = \mathrm{id}$ is a conjugation exactly when $\varsigma = \mathrm{id}$.

*Proof.* Read $\lambda$ in the twisted action of the conjugate module as $\lambda \cdot x = \varsigma(\lambda)x$; then

$$
c(\lambda \cdot x) = c\bigl(\varsigma(\lambda)x\bigr) = \varsigma\bigl(\varsigma(\lambda)\bigr)c(x) = \lambda\,c(x),
$$

because $\varsigma^2 = \mathrm{id}$, which is $R$-linearity of $c$ as a map $A^{\varsigma} \to A$. The map $\mathrm{id}$ is $\varsigma$-semilinear exactly when $\varsigma(\lambda)x = \lambda x$ for all $\lambda$ and $x$, that is when $\varsigma = \mathrm{id}$. $\square$

**Remark.** The conjugation is the operation that the sesquilinear context requires and the bilinear one does not have. In the standard example of *Sesqualgebras*, where $A$ is an associative algebra with a $\varsigma$-semilinear involution $*$, the natural conjugation is the one that conjugates the coefficients of the algebra without moving them, the operation whose fixed set is the $R^{\varsigma}$-form of $A$; on the complex matrices it is the entrywise conjugation, on a matrix algebra over a field it is the entrywise action of $\varsigma$. It is an automorphism there, but the definition above asks only for an involutive semilinear map, and multiplicativity is used nowhere below.

### The Exchange

**Definition.** The **exchange of $\star$ by $c$**, written $\star^{c}$ or $E_{c}(\star)$, is

$$
\star^{c}(x,y) := c\bigl(\star(y,x)\bigr).
$$

**Theorem (the exchange is an involution of the class).** For every $\varsigma$-sesquilinear product $\star$ the map $\star^{c}$ is again $\varsigma$-sesquilinear, and

$$
(\star^{c})^{c} = \star .
$$

So $E_{c}$ is an involutive operator on the set of $\varsigma$-sesquilinear products of $A$, and its fixed points are the products with $\star(x,y) = c(\star(y,x))$.

*Proof.* Additivity in each variable is inherited from $\star$ and from the additivity of $c$. For the first scalar rule,

$$
\star^{c}(\lambda x, y) = c\bigl(\star(y, \lambda x)\bigr) = c\bigl(\varsigma(\lambda)\,\star(y,x)\bigr) = \varsigma(\varsigma(\lambda))\,c\bigl(\star(y,x)\bigr) = \lambda\,\star^{c}(x,y),
$$

and for the second,

$$
\star^{c}(x, \lambda y) = c\bigl(\star(\lambda y, x)\bigr) = c\bigl(\lambda\,\star(y,x)\bigr) = \varsigma(\lambda)\,\star^{c}(x,y).
$$

The involution is $(\star^{c})^{c}(x,y) = c\bigl(\star^{c}(y,x)\bigr) = c\bigl(c(\star(x,y))\bigr) = \star(x,y)$. $\square$

**Remark.** The theorem is the exact point of the adaptation. The plain transposition of §*The Transposed Product Has the Opposite Parity* left the class; the transposition followed by the conjugation returns to it. **The conjugation repairs the parity that the transposition reverses**, and it does so for every product at once, so that the repair is a symmetry of the category and not a trick on one example.

### The Exchange in the Conjugate Module

**Remark (the exchange is a transposition read back through $c$).** The product is the $R$-bilinear map $\star : A \times A^{\varsigma} \to A$ of *The Sesquilinear Product*, and its transposition is the map $t : A^{\varsigma} \times A \to A$ with $t(u,y) = \star(y,u)$. By the proposition of §*The Conjugation* the conjugation is an $R$-linear isomorphism $c : A^{\varsigma} \to A$, and the exchange is the transposed map read back through it:

$$
\star^{c}(x,y) = c\bigl(\star(y,x)\bigr) = c\bigl(t(x,y)\bigr),
$$

the element $x$ being read in $A^{\varsigma}$ on the left. So the exchange is an ordinary transposition of a bilinear map, made into an operation of the class by the identification of $A^{\varsigma}$ with $A$ that the conjugation supplies. In the bilinear case $\varsigma = \mathrm{id}$, the two modules coincide, the identification is the identity, and the exchange is the plain one.

---

## The Two Halves

### Definition and Reconstruction

**Definition.** The **conjugate-symmetric part** and the **skew-conjugate-symmetric part** of $\star$, relative to the conjugation $c$, are

$$
\star_{+}(x,y) := \tfrac12\bigl(x \star y + c(y \star x)\bigr), \qquad
\star_{-}(x,y) := \tfrac12\bigl(x \star y - c(y \star x)\bigr).
$$

**Proposition.** For all $x, y \in A$,

$$
x \star y = \star_{+}(x,y) + \star_{-}(x,y), \qquad
c\bigl(\star_{+}(y,x)\bigr) = \star_{+}(x,y), \qquad
c\bigl(\star_{-}(y,x)\bigr) = -\star_{-}(x,y),
$$

and both halves are $\varsigma$-sesquilinear products of $A$. On the diagonal $\star_{+}(x,x) = \tfrac12\bigl(x \star x + c(x \star x)\bigr)$ and $\star_{-}(x,x) = \tfrac12\bigl(x \star x - c(x \star x)\bigr)$.

*Proof.* The reconstruction is the sum of the two definitions. The symmetry of the first half is $\tfrac12(x\star y + c(y\star x))$ read at the pair $(y,x)$ and then conjugated, which is $\tfrac12(c(y\star x) + c^2(x\star y)) = \star_{+}(x,y)$, and the antisymmetry of the second is the same computation with a sign. Both are $\varsigma$-sesquilinear by the theorem of §*The Exchange*, being half the sum and half the difference of two products of the class. The diagonal is the definitions at $y = x$. $\square$

**Remark (the naming, and the two neighbours it must not be confused with).** The corpus already uses the words *Hermitian* and *skew-Hermitian* for the two halves of the **plain** split of the product, by the **values** they take under the involution $*$: the symmetrisation is Hermitian-valued, $(x\star y + y\star x)^{*} = x\star y + y\star x$, and the difference skew-Hermitian-valued, in *The Sesquilinear Product*, §*The Hermitian and the Skew-Hermitian Parts*. It also calls a *form* conjugate-symmetric when $h(x,y) = \overline{h(y,x)}$, in *Hermitian Geometry and the Unitary Group*. The phrase of this article, **conjugate-symmetric product**, is of a third kind: it names the **operation**, not a value, and it means fixed by the exchange $E_{c}$. The three are different, and the article keeps the third for these two halves. The plain split and its Hermitian-valued halves are §*The Plain Split*; the Hermitian elements, the fixed set of $*$, are *Hermitian and Skew-Hermitian Elements*, and are a statement about the elements and not about the product.

**Remark (where the two notions of *conjugate-symmetric* agree).** Take $A = R$ as a free module of rank one, so that the product is scalar-valued, and let $\varepsilon$ be the identity with $s = \star$ and $c = \varsigma$. Then $\star$ is conjugate-symmetric in the sense of this article exactly when $\star(x,y) = \varsigma(\star(y,x))$ for all $x,y$, which is the **Hermitian** condition of *Hermitian Geometry and the Unitary Group*, and its skew half is then skew-Hermitian in the same sense. For a scalar-valued product the exchange split of this article is therefore the Hermitian–skew-Hermitian split of the value, and the two names agree. For an algebra-valued product they differ by the transposition, and the two splits are different: **the exchange split is the transposition followed by the conjugation, the value split is the conjugation alone.**

### Exchange-Symmetry and Exchange-Antisymmetry

**Proposition (what each half detects).** The conjugate-symmetric half vanishes identically exactly when the product is exchange-**anticommutative**, and the skew half vanishes identically exactly when it is exchange-**symmetric**:

$$
\star_{+} = 0 \ \text{for all pairs} \iff x \star y = -c(y \star x) \ \text{for all } x,y,
$$

$$
\star_{-} = 0 \ \text{for all pairs} \iff x \star y = c(y \star x) \ \text{for all } x,y.
$$

*Proof.* The first half is zero exactly when $x\star y = -c(y\star x)$ for every pair, which is the first condition, and the second half is zero exactly when $x\star y = c(y\star x)$ for every pair. $\square$

**Remark.** The two extremes are the degenerate cases, as in the bilinear theory: the skew half measures nothing but the failure of exchange-symmetry, and the conjugate-symmetric half nothing but the failure of exchange-anticommutativity. Nothing else about the product enters either half. In the bilinear case the two conditions read $xy = -yx$ and $xy = yx$, which is anticommutativity and commutativity, and the proposition is that of *The Symmetric and Antisymmetric Parts of an Algebra Product*.

### Uniqueness

**Theorem (uniqueness of the split).** Suppose $x \star y = u(x,y) + v(x,y)$ for all $x, y$, with $u$ exchange-symmetric and $v$ exchange-antisymmetric. Then $u = \star_{+}$ and $v = \star_{-}$.

*Proof.* Interchanging the arguments in the assumed decomposition and conjugating gives $c(y \star x) = u(x,y) - v(x,y)$, because $u$ satisfies $c(u(y,x)) = u(x,y)$ and $v$ satisfies $c(v(y,x)) = -v(x,y)$. Adding the two relations, $x\star y + c(y\star x) = 2u(x,y)$; subtracting them, $x\star y - c(y\star x) = 2v(x,y)$. The quotients by $2$ are the two halves, and the division by $2$ is the only place where the invertibility of $2$ is used. $\square$

### The Two Projections

**Definition.** On the set of $\varsigma$-sesquilinear products of $A$ define

$$
p(\star)(x,y) = \tfrac12\bigl(x \star y + c(y \star x)\bigr), \qquad
q(\star)(x,y) = \tfrac12\bigl(x \star y - c(y \star x)\bigr).
$$

**Proposition.** The operators $p$ and $q$ are additive and satisfy

$$
p^2 = p, \qquad q^2 = q, \qquad pq = qp = 0, \qquad p + q = \mathrm{id},
$$

so that the space of products is the direct sum of its conjugate-symmetric products, the image of $p$, and its skew-conjugate-symmetric products, the image of $q$.

*Proof.* Additivity is immediate. Applying $p$ twice,

$$
p(p(\star))(x,y) = \tfrac12\bigl(p(\star)(x,y) + c(p(\star)(y,x))\bigr) = \tfrac14\bigl(x\star y + c(y\star x) + c(y\star x) + c^2(x\star y)\bigr),
$$

which is $\tfrac12(x\star y + c(y\star x)) = p(\star)(x,y)$, and the computation for $q$ is the same with the two signs. For the product of the two,

$$
p(q(\star))(x,y) = \tfrac14\bigl(x\star y - c(y\star x) + c(y\star x) - c^2(x\star y)\bigr) = 0,
$$

and $qp = 0$ likewise. Finally $p(\star) + q(\star)$ is $\tfrac12(x\star y + c(y\star x)) + \tfrac12(x\star y - c(y\star x)) = x\star y$, which is $p + q = \mathrm{id}$. A family of idempotents that sum to the identity and annihilate one another gives a direct sum decomposition, so the space of products is the sum of the two images and the sum is direct. $\square$

**Corollary (each half can be prescribed).** A $\varsigma$-sesquilinear map on $A$ is a conjugate-symmetric part if and only if it is exchange-symmetric, and a skew-conjugate-symmetric part if and only if it is exchange-antisymmetric. Moreover for any exchange-symmetric $u$ and any exchange-antisymmetric $v$ the product $\star = u + v$ satisfies $p(\star) = u$ and $q(\star) = v$.

*Proof.* An exchange-symmetric $u$ satisfies $p(u) = u$, and an exchange-antisymmetric $v$ satisfies $p(v) = 0$ and $q(v) = v$, which gives the first sentence; for the second, $p(u+v) = p(u) + p(v) = u$ and $q(u+v) = q(u) + q(v) = v$. $\square$

**Remark.** The corollary is the precise sense in which the two halves are independent data: **the conjugate-symmetric half of a product places no constraint on its skew half and conversely**, and a condition imposed on one half can be studied with no hypothesis at all on the other. In the bilinear case the two independent halves are the Jordan part and the Lie part of the product, and the corollary is the one that separates Lie-admissibility from Jordan-admissibility in *The Symmetric and Antisymmetric Parts of an Algebra Product*.

---

## The Scalar Part

### The Scalar Theorem

**Definition.** An additive map $\varepsilon : A \to R$ with $\varepsilon(\lambda x) = \lambda\varepsilon(x)$ is **compatible with the conjugation** $c$ when

$$
\varepsilon\bigl(c(x)\bigr) = \varsigma\bigl(\varepsilon(x)\bigr) \qquad (x \in A).
$$

The **scalar form** of the product is $s = \varepsilon \circ \star$, and $s$ is $\varsigma$-**Hermitian** when $s(y,x) = \varsigma(s(x,y))$ for all $x, y$.

**Theorem (the scalar form follows the split).** Let $\varepsilon$ be compatible with $c$ and put $s = \varepsilon\circ\star$. Then for all $x, y \in A$,

$$
\varepsilon\bigl(\star_{+}(x,y)\bigr) = \tfrac12\bigl(s(x,y) + \varsigma(s(y,x))\bigr), \qquad
\varepsilon\bigl(\star_{-}(x,y)\bigr) = \tfrac12\bigl(s(x,y) - \varsigma(s(y,x))\bigr).
$$

So the scalar form of the conjugate-symmetric half is the Hermitian part of $s$, $\tfrac12\bigl(s(x,y) + \varsigma(s(y,x))\bigr)$, and the scalar form of the skew half is its skew part: the two combinations that a Hermitian form is decomposed into, and the reason the names of *Hermitian Geometry and the Unitary Group* are met again here.

*Proof.* By the definition of the halves and the compatibility,

$$
\varepsilon\bigl(\star_{+}(x,y)\bigr) = \tfrac12\bigl(\varepsilon(x\star y) + \varepsilon(c(y\star x))\bigr) = \tfrac12\bigl(s(x,y) + \varsigma(s(y,x))\bigr),
$$

and the computation for $\star_{-}$ is the same with a sign. $\square$

### The Case of a Hermitian Form

**Theorem (the whole scalar part is conjugate-symmetric).** Let $\varepsilon$ be compatible with $c$ and suppose the scalar form $s = \varepsilon\circ\star$ is $\varsigma$-Hermitian. Then

$$
\varepsilon\bigl(\star_{-}(x,y)\bigr) = 0, \qquad \varepsilon\bigl(\star_{+}(x,y)\bigr) = s(x,y) = \varepsilon(x \star y)
$$

for all $x, y$. The skew-conjugate-symmetric half is scalar-free, and the conjugate-symmetric half carries the whole scalar form.

*Proof.* If $s(y,x) = \varsigma(s(x,y))$ then $\varsigma(s(y,x)) = \varsigma^2(s(x,y)) = s(x,y)$; substituting in the scalar theorem gives the two displays. $\square$

**Remark.** This is the sharpest difference from the plain split, and the reason for adapting the exchange at all. The plain split of §*The Scalar Form Under the Plain Split* puts only the $\varsigma$-even part of the form in its symmetric half and leaves the $\varsigma$-odd part in the difference; **the exchanged split puts the form itself, in its entirety, in the conjugate-symmetric half.** The form is then read off one half alone, and the other half carries no scalar of the product at all.

**Corollary (the values of the skew half are scalar-free).** Under the hypotheses of the theorem, no value of $\star_{-}$ has a nonzero scalar part; in a free algebra on a basis of $n$ elements whose first element is fixed by $c$ and carries the scalars, the coefficient of that element vanishes in every value of the skew half.

*Proof.* The scalar part of a value is $\varepsilon$ of that value, and the theorem makes it zero. $\square$

---

## The Structure Constants

### The Constants of the Exchange

**Proposition (the exchange on the constants).** Let $A$ be free with basis $(e_{1},\dots,e_{n})$ and write

$$
e_{i} \star e_{j} = \sum_{k} c^{k}{}_{ij}\, e_{k}, \qquad c(e_{i}) = \sum_{l} \gamma^{l}{}_{i}\, e_{l} .
$$

Then the constants of the exchanged product are

$$
e_{i} \star^{c} e_{j} = \sum_{l} \tilde{c}^{\,l}{}_{ij}\, e_{l},
\qquad \tilde{c}^{\,l}{}_{ij} = \sum_{k} \gamma^{l}{}_{k}\, \varsigma\bigl(c^{k}{}_{ji}\bigr).
$$

When the basis is fixed by the conjugation, $c(e_{i}) = e_{i}$ for every $i$, this reads

$$
\tilde{c}^{\,k}{}_{ij} = \varsigma\bigl(c^{k}{}_{ji}\bigr),
$$

and the conjugate-symmetric products are exactly those whose constants satisfy the **conjugate-symmetry** $c^{k}{}_{ij} = \varsigma\bigl(c^{k}{}_{ji}\bigr)$.

*Proof.* Compute the exchanged product on basis elements, $\star^{c}(e_{i}, e_{j}) = c(\star(e_{j}, e_{i}))$, expand the inner product and use the semilinearity of $c$, $c(\lambda e_{k}) = \varsigma(\lambda)c(e_{k})$; when each basis vector is fixed this is $\sum_{k}\varsigma(c^{k}{}_{ji})e_{k}$. The condition $c^{k}{}_{ij} = \varsigma(c^{k}{}_{ji})$ is the fixed-point equation of the previous line. $\square$

**Remark.** The conjugation therefore conjugates the constants as well as transposing their two lower indices, and the two operations are the two halves of the adaptation: the transposition is the exchange of the arguments, the conjugation is the repair of the parity. In the bilinear case $\varsigma = \mathrm{id}$ the conjugation of the constants is invisible and the condition is the ordinary symmetry $c^{k}{}_{ij} = c^{k}{}_{ji}$ of the structure constants of a commutative product.

### The Count

**Proposition (the count over the fixed field).** Let $R$ be a field, $\varsigma$ a nontrivial involution of $R$, so that $R$ is of rank two over $R^{\varsigma}$, and let $c(e_{i}) = e_{i}$ on a basis of $n$ elements. Then the space of $\varsigma$-sesquilinear products is an $R^{\varsigma}$-module of rank $2n^{3}$, its conjugate-symmetric products form a submodule of rank $n^{3}$, and its skew products one of rank $n^{3}$.

*Proof.* A product is the same thing as an arbitrary family of $n^{3}$ constants in $R$, by *The Sesquilinear Product*, §*The Axioms of the Product*, and $R$ has rank two over $R^{\varsigma}$, so the space of products has rank $2n^{3}$. The conjugate-symmetry $c^{k}{}_{ij} = \varsigma(c^{k}{}_{ji})$ is an additive involution of that module; its free data are the $n$ diagonal values, each in the fixed field, together with the entries above the diagonal, each an arbitrary element of $R$ that determines the entry below it, of which there are $n(n-1)$; the total per upper index is $n + n(n-1) = n^{2}$, and over the $n$ values of the upper index it is $n^{3}$. The skew products have the same count, since an arbitrary product is the sum of one of each. $\square$

| $n$ | products, $2n^{3}$ | conjugate-symmetric, $n^{3}$ | skew, $n^{3}$ |
|---|---|---|---|
| 2 | 16 | 8 | 8 |
| 3 | 54 | 27 | 27 |
| 4 | 128 | 64 | 64 |

**Remark (the two counts compared).** In the bilinear theory the constants number $n^{3}$, of which the symmetric half takes $\binom{n+1}{2}n$ and the antisymmetric half $\binom{n}{2}n$, so the symmetric half is the larger of the two for every $n$. In the sesquilinear theory the space of products doubles, to $2n^{3}$ over the fixed field, and the two halves take $n^{3}$ each: **the conjugate-symmetric and the skew halves are of equal rank for every $n$, and the acquisition of the conjugation is exactly what pays for the second copy of the constants.** Per upper index the bilinear table carries $\binom{n+1}{2} + \binom{n}{2} = n^{2}$ independent constants, the sesquilinear table carries $n + n = 2n$.

---

## The Square

### The Polarisation of the Plain Symmetrisation

**Proposition.** For all $x, y \in A$,

$$
(x + y) \star (x + y) - x \star x - y \star y = x \star y + y \star x = 2\star^{\mathrm{sym}}(x,y).
$$

*Proof.* Expand the product by its additivity in each variable and cancel the two squares. $\square$

**Remark (the square polarises the plain symmetrisation, not the exchanged one).** The right-hand side is twice the **plain** symmetrisation of *The Sesquilinear Symmetrised Product*, and it is $2\star_{+}(x,y)$ only when $c$ is the identity, that is in the bilinear case. The identity that the algebra article proves as the polarisation of the symmetric half therefore has no analogue for the adapted half:

$$
(x + y) \star (x + y) - x \star x - y \star y = 2\star^{\mathrm{sym}}(x,y) \neq 2\star_{+}(x,y) \quad \text{in general.}
$$

The square map sees the plain symmetrisation and it cannot see the exchanged one, and the reason is that the exchange conjugates the value while the square of a sum conjugates nothing.

### The Diagonal

**Proposition (the diagonal is the conjugated square).** For every $x \in A$,

$$
\star_{+}(x,x) = \tfrac12\bigl(x \star x + c(x \star x)\bigr), \qquad
\star_{-}(x,x) = \tfrac12\bigl(x \star x - c(x \star x)\bigr).
$$

So the conjugate-symmetric half is symmetric on the diagonal, the skew half is the antisymmetrised square, and

$$
\star_{-}(x,x) = 0 \ \text{for all } x \iff c(x \star x) = x \star x \ \text{for all } x .
$$

*Proof.* The displays are the definitions at $y = x$, and the equivalence is the second display read at a single element. $\square$

**Remark (the analogue of $x \wedge x = 0$ is a condition, not an identity).** In the bilinear theory the antisymmetric half vanishes on the diagonal identically, $x \wedge x = \tfrac12(x^2 - x^2) = 0$, and that identity is what separates the squares that the symmetric half carries from the ones it cannot. In the sesquilinear theory the diagonal of the skew half is the antisymmetrised square, which **need not vanish**: it vanishes exactly when the square of every element is fixed by the conjugation. By the theorem of §*The Case of a Hermitian Form* its scalar part vanishes whenever the scalar form is Hermitian, so the surviving values are vector-valued, and the biquaternion products below exhibit them. The diagonal is therefore the place where the adaptation costs something, and the price is paid in the square and not in the scalar.

### What the Diagonal Carries

**Corollary (the diagonal, read on the square).** By the proposition of §*The Diagonal*, the pair $\bigl(\star_{+}(x,x), \star_{-}(x,x)\bigr)$ is the decomposition of the square $x\star x$ into its parts fixed and anti-fixed by the conjugation: $2\star_{+}(x,x) = x \star x + c(x \star x)$ and $2\star_{-}(x,x) = x \star x - c(x \star x)$ for every $x \in A$.

**Remark (the diagonal is the honest replacement for the polarisation).** The square of an element is split by the conjugation into a fixed part and an anti-fixed part, the first is the value of the conjugate-symmetric half and the second the value of the skew half, and the two are recovered from the square alone. What is lost is the reconstruction of the halves **off** the diagonal from the square map: the polarisation identity recovers the plain symmetrisation from the square, and no identity recovers the exchanged one. The exchange and the polarisation are therefore not compatible, and the diagonal is the one that holds.

---

## The Standard Example

### The Derived Operation

**Proposition.** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution $*$, let the product be the derived operation $\star(x,y) = xy^{*}$ of *Sesqualgebras*, juxtaposition being the product of the associative algebra and $\star$ the derived operation, and let $c$ be a conjugation commuting with $*$. Then

$$
\star^{c}(x,y) = c(yx^{*}), \qquad \star_{+}(x,y) = \tfrac12\bigl(xy^{*} + c(yx^{*})\bigr), \qquad
\star_{-}(x,y) = \tfrac12\bigl(xy^{*} - c(yx^{*})\bigr),
$$

and if $c$ is an automorphism of the algebra product this reads $\star^{c}(x,y) = c(y)\,c(x^{*})$.

*Proof.* Substitute the derived operation in the exchange: $\star^{c}(x,y) = c\bigl(\star(y,x)\bigr) = c(yx^{*})$, and for an automorphism $c$ the conjugation passes through the product, $c(yx^{*}) = c(y)c(x^{*})$. $\square$

**Remark (the Hermitian form).** For a $\varsigma$-semilinear involution $*$ and an additive $R$-linear $\varepsilon$ with $\varepsilon(x^{*}) = \varsigma(\varepsilon(x))$, the scalar form of the derived operation is Hermitian:

$$
s(y,x) = \varepsilon(yx^{*}) = \varsigma\bigl(\varepsilon(xy^{*})\bigr) = \varsigma(s(x,y)),
$$

the middle step being $\varepsilon(u^{*}) = \varsigma(\varepsilon(u))$ at $u = xy^{*}$ together with $(xy^{*})^{*} = yx^{*}$. So the hypothesis of §*The Case of a Hermitian Form* holds for the standard example, and the whole scalar form of a derived operation lies in its conjugate-symmetric half.

**Remark (the other twist is degenerate).** The algebra carries a second involution besides the conjugation, namely $*$ itself, and with it the exchange $\star \mapsto (\star)^{*}$, $(\star)^{*}(x,y) = (\star(y,x))^{*}$. For the derived operation this exchange does nothing,

$$
(\star)^{*}(x,y) = (yx^{*})^{*} = xy^{*} = \star(x,y),
$$

so the derived operation is fixed by the $*$-exchange and its split by that exchange is trivial. **The derived operation is conjugate-symmetric in the $*$-sense automatically, and it is the other conjugation — the one whose fixed set contains the scalars — that carries information.** The two exchanges must not be confused, and it is the second that this article uses.

### The Complex Matrices

**Proposition.** Let $A = M_{n}(\mathbb{C})$ with the conjugate transpose $X\mapsto X^{*}=\overline{X}^{\mathsf{T}}$ as its involution and the entrywise conjugation $\bar{\cdot}$ as the conjugation. Then the exchanged product of the derived operation is

$$
\star^{c}(x,y) = \bar{y}\,x^{\mathsf{T}},
$$

the conjugate of the second argument multiplied on the left by the transpose of the first.

*Proof.* $\overline{yx^{*}} = \bar{y}\,\overline{x^{*}}$ by the multiplicativity of the entrywise conjugation, and $\overline{x^{*}} = x^{\mathsf{T}}$ because the conjugate of the conjugate transpose is the transpose. $\square$

**Remark.** With the trace $\varepsilon = \operatorname{tr}$ as the scalar form the hypotheses of the scalar theorem hold, since $\operatorname{tr}(\bar{x}) = \overline{\operatorname{tr}(x)}$, and the trace of a value of the skew half vanishes:

$$
\operatorname{tr}\bigl(\star_{-}(x,y)\bigr) = \tfrac12\Bigl(\operatorname{tr}(xy^{*}) - \operatorname{tr}(\bar{y}x^{\mathsf{T}})\Bigr) = 0,
$$

the second trace being the conjugate of the first, since $\operatorname{tr}(\bar{y}x^{\mathsf{T}}) = \operatorname{tr}(xy^{*})$ is the sum of the entries $x_{ij}\overline{y_{ij}}$. The conjugate-symmetric half carries the whole trace instead, and $\operatorname{tr}(\star_{+}(x,y)) = \operatorname{tr}(xy^{*})$.

### The Biquaternion Products

**Remark (four general products, two exchanges).** The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products, the general plain bilinear $\tilde{P}\tilde{Q}$, the general quaternionic bilinear $\tilde{P}^{\natural}\tilde{Q}$, the general plain sesquilinear $\tilde{P}\tilde{Q}^{*}$ and the general quaternionic sesquilinear $\tilde{P}^{\natural}\tilde{Q}^{*}$ of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*. The first two are bilinear, so their base involution is trivial and their exchange is the plain transposition; the last two are sesquilinear over $(\mathbb{C},\varsigma)$ with $\varsigma$ the complex conjugation, and their conjugation is the coefficientwise conjugation $\bar{\cdot}$ of *The Clifford Algebra Representation*, so their exchange is the transposition followed by the coefficientwise conjugation. **The exchange that applies to a product is read off the base involution of the product, and the four general products fall into two pairs by it.**

**Remark (what the split gives on the four general products).** With those exchanges the two halves separate as follows. For the general plain bilinear and the general quaternionic sesquilinear products, the two for which the pair of arguments carries an even number of the conjugations ${}^{\natural}$ and ${}^{*}$, the skew half is a cross product, $\mathbf P\times\mathbf Q$ and $\mathbf P\times\overline{\mathbf Q}$ respectively; for the general quaternionic bilinear and the general plain sesquilinear products, for which that number is odd, the conjugate-symmetric half is the form alone and the skew half is therefore the whole vector part of the product. The conjugate-symmetric half carries the four forms of the biquaternion block: the general plain bilinear form $B$ on the first product, the general quaternionic bilinear form $N$ on the second, the general plain sesquilinear form $H$ on the third and the general quaternionic sesquilinear form $K$ on the fourth. In all four cases the scalar part lies entirely in the conjugate-symmetric half, which is the scalar theorem of this article; the diagonal of the skew half is scalar-free in all four cases, and it is nonzero and vector-valued exactly for the two sesquilinear products, which is the diagonal proposition. The computation of the four general products and the four forms is *The Four Pairings of the Biquaternion Algebra*, and the halves of the first product, with its Jordan property, are *The 12 Products of the Biquaternion Complex Space*.

**Remark (the two sesquilinear halves in closed form).** On the general plain sesquilinear product the central half and the skew half are the scalar and the vector part of the value,
$$
\tfrac12\bigl(\tilde P\tilde Q^{*}+(\tilde P\tilde Q^{*})^{\natural}\bigr)=\mathrm{Sc}(\tilde P\tilde Q^{*})e_0=\bigl(P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q})\bigr)e_0,\qquad
\tfrac12\bigl(\tilde P\tilde Q^{*}-(\tilde P\tilde Q^{*})^{\natural}\bigr)=\mathrm{Vect}(\tilde P\tilde Q^{*}),
$$
the first the Hermitian form $H$ in the centre and the second the whole vector part; on the general quaternionic sesquilinear product they are the symmetrisation of $\tilde P^{\natural}$ with $\tilde Q^{*}$ and half their commutator,
$$
\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural}\bigr),\qquad
\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr),
$$
both sesquilinear over $\mathbb C$ — the class is kept — and here the skew half is the cross product $\mathbf P\times\overline{\mathbf Q}$, vector-valued, while the symmetric half carries the general quaternionic sesquilinear form $K$ in its scalar part, $K(\tilde P,\tilde Q)=P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})$, and is not central in general.

**Remark (the order swap and the conjugation of the biquaternion products).** The four general products each admit the plain interchange of the two arguments, the **order symmetry**, and its two halves are the symmetric and the antisymmetric parts of *The 12 Products of the Biquaternion Complex Space*. For the two bilinear products that plain split is the split of this article, since $\varsigma = \mathrm{id}$ and the exchange is the plain one, and it is the split developed in that article. For the two sesquilinear products the order symmetry gives halves that are only $R^{\varsigma}$-bilinear, by §*The Plain Split*, and it is therefore the wrong symmetry for the category: the symmetric and antisymmetric parts of the order symmetry of $\tilde{P}\tilde{Q}^{*}$ and $\tilde{P}^{\natural}\tilde{Q}^{*}$ are not products of a sesqualgebra, and their reading with the symmetrised sesquilinear product and the sesquilinear commutator is *The Sesquilinear Commutator and the Symmetrised Product on the Biquaternions*. The conjugate-symmetric and skew halves of this article are the corrected form of the same idea, the one in which the two halves stay in the category, and the two notions coincide exactly on the two bilinear products.

---

## When 2 Is Not Invertible

**Remark (the reductions).** Two degenerations of the construction are worth naming. When $\varsigma = \mathrm{id}$ the base involution is trivial, $c = \mathrm{id}$ is a conjugation, the exchange is the plain transposition, and every statement of this article reduces to the corresponding statement of *The Symmetric and Antisymmetric Parts of an Algebra Product*; the article is therefore the general form of which that one is the bilinear case. When $c = \mathrm{id}$ and $\varsigma \neq \mathrm{id}$ there is no conjugation at all, by the proposition of §*The Conjugation*, and the exchange of §*The Exchange* is unavailable: **the twist is not optional decoration, it is the only exchange the sesquilinear context has.**

**Remark (characteristic two).** If $2 = 0$ in $R$ then $-1 = 1$, the exchange and its negative coincide, and the two halves $\star_{+}$ and $\star_{-}$ are equal, being $\tfrac12(\star \pm \star^{c})$ with the two signs indistinguishable. The projections $p$ and $q$ of §*The Two Projections* are then unavailable, since they are built from $\tfrac12$, and the split of this article does not exist: an arbitrary product is not determined by its conjugate-symmetric and skew parts, because the two are the same part. The same collapse afflicts the bilinear theory, and for the same reason, and it is recorded there in §*The Collapse in Characteristic 2*.

**Remark (the general commutative ring).** The construction needs $\tfrac12$, not a field: over a commutative ring in which $2$ is invertible everything above goes through unchanged, with $R^{\varsigma}$ the fixed ring of the involution. The count of §*The Count* is the one place where a field is used, and there only to speak of the rank of a module.

---

## Where the Corpus Uses the Split

The split is used at several places in the corpus, and each use is recorded in the article that owns it.

**The two halves of the plain split.** The symmetrised sesquilinear product $x \star y + y \star x$ and the difference bracket $[x,y]_{\varsigma} = x \star y - y \star x$ are the plain halves, and they are developed for their own sake in *The Sesquilinear Symmetrised Product* and *The Sesquilinear Commutator*: the scalar rules of the symmetrisation, its factorisation on the Hermitian part, the Jordan identity on that part and its failure off it; the correction term of the bracket, its skew-Hermitian values, and the failure of the Jacobi identity. This article does not repeat them, and the exchanged split is not the plain one.

**The involution of the algebra.** The two halves of the involution $*$, the Hermitian and the skew-Hermitian elements, and the two algebras they carry, the Jordan algebra on the Hermitian part and the Lie algebra on the skew part, are *Hermitian and Skew-Hermitian Elements*, *The Hermitian Jordan Algebra* and *The Unitary Lie Algebra*. The distinction between the two kinds of halving — of the involution on the elements and of the exchange on the product — is made in the Introduction of this article and used throughout.

**The squares and the cone.** The elements of the form $x^{*}x$ and the algebraic positive cone they generate are *Hermitian Squares and the Algebraic Positive Cone*; the diagonal of the exchanged split is a statement about $x\star x$ and not about $x^{*}x$, and the two must not be identified.

**The standard example and its ternary product.** The derived operation $x\star y = xy^{*}$ is not associative, and the associator and the ternary product $\{x,y,z\} = xy^{*}z$ it forces are *The Sesquilinear Associator and the Ternary Product*; the reading of the derived operation as a $J^{*}$-algebra and the recovery of the binary data from the ternary one are *Algebraic J\*-Algebras*. The split of this article is not needed for either, and the two articles are named here so that the reader does not expect the associator to be a statement about the halves.

**The biquaternion instance.** The four general products of the biquaternion algebra and their halves are §*The Biquaternion Products* of this article, and the four forms that the conjugate-symmetric halves carry are *The Four Pairings of the Biquaternion Algebra*; the bilinear case is *The 12 Products of the Biquaternion Complex Space*, and the Lie and Jordan readings of the two halves of the first product are *The 12 Products of the Biquaternion Complex Space*.

**Forms and Hermitian geometry.** The Hermitian property of the derived operation read as a two-variable map, which is the hypothesis of §*The Case of a Hermitian Form*, is the opening of *Hermitian Forms on a Sesqualgebra*; the forms themselves, their classification by signature, their symmetric and alternating real parts and their unitary groups are *Hermitian Geometry and the Unitary Group*, and the invariant form and the unitary representations of the Lie part are *Hermitian Forms on a Lie Algebra*.

---

## Summary

A $\varsigma$-sesquilinear product is conjugate-linear in one argument, and the exchange of its two arguments alone does not preserve the class: the transposed product is $\varsigma$-semilinear in the first slot and $R$-linear in the second, so the two halves of the plain split are only $R^{\varsigma}$-bilinear. That plain split is the symmetrised sesquilinear product and the sesquilinear commutator, and it splits the scalar form of a Hermitian product into its $\varsigma$-even and $\varsigma$-odd parts, which over $\mathbb{C}$ are the real and the alternating parts.

The symmetry that does preserve the class is the exchange twisted by a **conjugation** $c$ of the algebra, an additive involutive $\varsigma$-semilinear map, the operation $\star^{c}(x,y) = c(y \star x)$. The exchange is an involution of the set of $\varsigma$-sesquilinear products, its fixed points are the **conjugate-symmetric** products, and the split

$$
x \star y = \star_{+}(x,y) + \star_{-}(x,y), \qquad
\star_{\pm}(x,y) = \tfrac12\bigl(x \star y \pm c(y \star x)\bigr)
$$

is unique, with $p$ and $q$ idempotent, orthogonal and summing to the identity on the space of products, so that the conjugate-symmetric half and the skew half are independent data and either can be prescribed. The conjugate-symmetric half vanishes identically exactly for an exchange-anticommutative product and the skew half exactly for an exchange-symmetric one. The scalar form $s = \varepsilon \circ \star$ follows the split, its Hermitian part going to the conjugate-symmetric half and its skew part to the skew half; when $s$ is Hermitian, which is the case for the derived operation and for the complex matrices, the skew half is scalar-free and the **whole** scalar form lies in the conjugate-symmetric half, which is the sharpening the plain split does not give.

The exchange conjugates the constants as well as transposing their lower indices, the conjugate-symmetric products being those with $c^{k}{}_{ij} = \varsigma(c^{k}{}_{ji})$, and over the fixed field the products have rank $2n^{3}$ while each half has rank $n^{3}$: the conjugate-symmetric and skew halves are of equal rank, in contrast with the bilinear counts $\binom{n+1}{2}n$ and $\binom{n}{2}n$. The square of an element is split by the conjugation into its fixed and anti-fixed parts, which are the diagonal values of the two halves, and the polarisation identity of the bilinear theory does **not** carry over: $(x+y)\star(x+y) - x\star x - y\star y$ is the plain symmetrisation and not the exchanged one, so the square map sees the plain split and not the adapted one.

The construction needs $2$ invertible, and in characteristic two the two halves coincide and the split does not exist. For $\varsigma = \mathrm{id}$ the article reduces to *The Symmetric and Antisymmetric Parts of an Algebra Product*, and when $c = \mathrm{id}$ and $\varsigma \neq \mathrm{id}$ there is no conjugation and therefore no exchange.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $\varsigma$, $R^{\varsigma}$ | A commutative ring with $1$; an involution of $R$; its fixed ring $\{\lambda : \varsigma(\lambda) = \lambda\}$ |
| $A$, $\star$ | An $R$-module; a $\varsigma$-sesquilinear product, $R$-linear in the first variable and $\varsigma$-semilinear in the second |
| $x \star y$ | The product; sesquilinear as above, and no further hypothesis |
| $\star^{\mathrm{sym}}$, $\star^{\mathrm{dif}}$ | The plain symmetrisation $\tfrac12(x \star y + y \star x)$ and the difference $x \star y - y \star x$, of *The Sesquilinear Symmetrised Product* and *The Sesquilinear Commutator* |
| $c$ | A conjugation: additive, $c(\lambda x) = \varsigma(\lambda)c(x)$, $c^{2} = \mathrm{id}$; an $R$-linear isomorphism $A^{\varsigma} \to A$ |
| $\star^{c} = E_{c}(\star)$ | The exchange $c(y \star x)$; an involution of the set of $\varsigma$-sesquilinear products |
| $\star_{+}$, $\star_{-}$ | The conjugate-symmetric and skew-conjugate-symmetric parts, $\tfrac12(x\star y \pm c(y\star x))$ |
| $p$, $q$ | The projections of a product onto its two halves, $p^{2} = p$, $q^{2} = q$, $pq = 0$, $p + q = \mathrm{id}$ |
| $\varepsilon$, $s = \varepsilon \circ \star$ | An additive $R$-linear form compatible with $c$; the scalar form of the product |
| $c^{k}{}_{ij}$, $\gamma^{l}{}_{i}$ | The structure constants $e_{i}\star e_{j} = \sum_{k}c^{k}{}_{ij}e_{k}$, and the matrix of the conjugation $c(e_{i}) = \sum_{l}\gamma^{l}{}_{i}e_{l}$ |

## Further Reading

- N. Bourbaki, *Algèbre*, Chapitre IX: *Formes sesquilinéaires et formes quadratiques* (Hermann, 1959), for the sesquilinear forms, their Hermitian and skew-Hermitian parts and the decomposition under an involution of the base ring.
- W. Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften **270** (Springer, 1985), for the base ring with involution, the conjugate module and the classification of the forms the conjugate-symmetric halves carry.
- L. C. Grove, *Classical Groups and Geometric Algebra*, Graduate Studies in Mathematics **39** (American Mathematical Society, 2002), for the real and imaginary parts of a Hermitian form and the unitary groups they define.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications **44** (American Mathematical Society, 1998), for the involutions of an algebra and the conjugation whose fixed set carries the scalars.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the symmetrisation of a product, the Jordan and Lie identities and the polarisation of the square in the bilinear case.
- K. A. Zhevlakov, A. M. Slinko, I. P. Shestakov and A. I. Shirshov, *Rings That Are Nearly Associative* (Academic Press, 1982), for the identities below associativity and the ternary structure that the standard example forces.
