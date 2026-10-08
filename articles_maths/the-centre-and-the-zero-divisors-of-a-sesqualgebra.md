# __The Centre and the Zero Divisors of a Sesqualgebra__

## Introduction

The centre of a ring is the set of the elements that commute with every element, and the zero divisors are the nonzero elements that annihilate something. Both notions are stated with the product alone, so both carry over to a sesqualgebra, and the two new axioms meet them in two different places: the second scalar rule meets the centre in its behaviour under the scalars, and the involution meets the zero divisors in the pairing of the one-sided classes. The centre is the piece of the algebra that the arguments of the block keep returning to: it is the set of the elements whose inner map vanishes, it is carried to itself by the involution, and, over the complex numbers with the conjugation, a nonzero centre is a witness that the algebra is not of full type.

Throughout, $A$ is a sesqualgebra over the datum $(R,\varsigma)$ with a $\varsigma$-semilinear involution $*$, in the sense of *Sesqualgebras*: the product is additive in each variable, $R$-linear in the first and $\varsigma$-semilinear in the second, and $*$ is additive, of order two, anti-multiplicative and $\varsigma$-semilinear. The product need not be associative and need not have a unit, and where an argument uses associativity or a unit it is said so. The comparison is with *Centre, Units, Zero Divisors and Division Algebras* in the bilinear layer; the inner derivations that the centre cuts are the subject of *Derivations of a Sesqualgebra*.

What is added here: the centre and its closure under the scalars, the parts cut by the involution, the centre of a unital or annihilator-free algebra, the one-sided and the two-sided zero divisors, the annihilators with the sides that the involution and the derived operation pair, and the interaction of the centre with the zero divisors.

## The Centre

### Definition

**Definition.** The **centre** of $A$ is
$$
Z(A) = \{ z \in A : zx = xz \text{ for every } x \in A \}.
$$
It is the **centralizer** of $A$ in itself, $Z(A) = C_{A}(A)$, where the centralizer of a subset $S \subseteq A$ is $C_{A}(S) = \{ a \in A : as = sa \text{ for every } s \in S \}$. In the notation of *The Left and Right Multiplication Operators of a Sesqualgebra*, the centre is the set of the $z$ with $L_{z} = R_{z}$, the elements whose two multiplications agree.

**Proposition.** $Z(A)$ is an additive subgroup of $A$, and $0 \in Z(A)$; if $A$ is unital then $1 \in Z(A)$.

**Proof.** For $y, z \in Z(A)$ and any $x$, $(y + z)x = yx + zx = xy + xz = x(y + z)$ by the additivity of the product in each variable, and $(-z)x = -(zx) = -(xz) = x(-z)$, so the centre is an additive subgroup. The element $0$ commutes with everything. A unit $1$ has $1x = x = x1$ for every $x$. $\square$

### Closure under the Scalars

**Proposition.** $\lambda z \in Z(A)$ for every $z \in Z(A)$ and every $\lambda \in R$. Hence $Z(A)$ is an $R$-submodule of $A$.

**Proof.** For $z \in Z(A)$ and $x \in A$, $(\lambda z)x = \lambda(zx)$ by the first scalar rule, while $x(\lambda z) = \varsigma(\lambda)(xz)$ by the second, so the difference $(\lambda z)x - x(\lambda z)$ is $(\lambda - \varsigma(\lambda))zx$. Now the centrality of $z$ tested at the element $\lambda x$ reads $z(\lambda x) = (\lambda x)z$, that is $\varsigma(\lambda)(zx) = \lambda(xz)$, using the same two rules, and $xz = zx$ because $z$ is central; so $(\lambda - \varsigma(\lambda))zx = 0$ for every $x$, the difference vanishes, and $\lambda z$ is central. $\square$

**Remark.** The second scalar rule does not restrict the centre, and the reason is visible in the proof: the centrality of $z$ can be tested at the element $\lambda x$, and the two rules then agree on it. This is not the behaviour of the derivations. A multiple $\lambda D$ of a derivation is a derivation only when $(\lambda - \varsigma(\lambda))A \cdot D(A) = 0$, so the derivations of *Derivations of a Sesqualgebra* form a module over the fixed ring $R^{\varsigma}$ and over all of $R$ only in the bilinear case; the fixed ring governs the derivations, and it does not govern the centre.

### The Involution on the Centre

**Proposition.** $z^{*} \in Z(A)$ for every $z \in Z(A)$, and the involution maps the centre onto itself.

**Proof.** For $z \in Z(A)$ and any $x$, $z^{*}x = (x^{*}z)^{*} = (zx^{*})^{*} = xz^{*}$: the first and the last steps are the anti-multiplicativity of the involution, and the middle step is the centrality of $z$ at the element $x^{*}$. Since $*^{2} = \mathrm{id}$ the map is onto. $\square$

### The Hermitian and the Skew-Hermitian Parts

Let $H(A) = \{a : a^{*} = a\}$ and $S(A) = \{a : a^{*} = -a\}$ be the Hermitian and the skew-Hermitian elements of $A$, as in *Hermitian and Skew-Hermitian Elements*.

**Proposition.** The sets $Z(A) \cap H(A)$ and $Z(A) \cap S(A)$ are the fixed part and the anti-fixed part of the involution on $Z(A)$. If $2$ is invertible in $R$, every $z \in Z(A)$ has the unique decomposition
$$
z = z_{+} + z_{-}, \qquad z_{+} = \tfrac{1}{2}(z + z^{*}), \qquad z_{-} = \tfrac{1}{2}(z - z^{*}),
$$
with $z_{+} \in Z(A) \cap H(A)$ and $z_{-} \in Z(A) \cap S(A)$.

**Proof.** The centre is an $R$-submodule by the proposition on the scalars, hence closed under sums and under the halving, and the involution is additive and carries the centre to itself, so the two parts lie in the centre; they are fixed and anti-fixed by the involution, and the decomposition is the one of *Hermitian and Skew-Hermitian Elements*, unique when $2$ is invertible. $\square$

**Remark.** Each of the two parts is an $R$-submodule of the centre, and the involution acts on the first as the identity and on the second as the negation. When $2$ is invertible in $R$ the centre is the direct sum of the two parts, and in the associative case, where the centre is a commutative algebra, the involution acts on it as a $\pm 1$-grading.

### The Associative Case

**Proposition.** Let $A$ be associative. Then $Z(A)$ is a commutative subalgebra of $A$, and with the involution it is a commutative $*$-subalgebra.

**Proof.** For $y, z \in Z(A)$ and any $x$, associativity gives $(yz)x = y(zx) = y(xz) = (yx)z = (xy)z = x(yz)$, so $yz \in Z(A)$; and $yz = zy$ because $z$ is central, so the centre is commutative. The stability under the involution is the proposition above, and the stability under the scalars is the proposition on the scalars, so the centre is a $*$-subalgebra. $\square$

**Remark.** Associativity is used at the first step, $(yz)x = y(zx)$; without it the centre of a sesqualgebra need not be closed under the product, only the additive and the scalar statements surviving. There are small examples over the two-element field in which two central elements multiply to a non-central element.

### The Kernel of the Inner Maps

**Proposition.** For $a \in A$ let $\mathrm{ad}_{a}(x) = ax - xa$ be the inner map of $a$. Then $\mathrm{ad}_{a} = 0$ exactly when $a \in Z(A)$.

**Proof.** The map $\mathrm{ad}_{a}$ vanishes exactly when $ax = xa$ for every $x$, which is the centrality of $a$. $\square$

**Remark.** This identifies the centre with the kernel of the map $a \mapsto \mathrm{ad}_{a}$ of *Derivations of a Sesqualgebra*, so that, when the inner maps are derivations, the inner derivations are read on the quotient $A/Z(A)$: the centre is exactly that which the inner derivations do not see.

## The Zero Divisors

### One-Sided and Two-Sided

**Definition.** A nonzero $z \in A$ is a **left zero divisor** if there is $0 \neq w \in A$ with $zw = 0$, and a **right zero divisor** if there is $0 \neq w \in A$ with $wz = 0$. It is a **zero divisor** if it is a left or a right one, and $A$ is a **domain** if it has none.

**Remark.** In a commutative algebra the two classes coincide. In an associative algebra a unit is neither a left nor a right zero divisor, since $zw = 0$ gives $w = v(zw) = (vz)w = 0$ for a left inverse $v$ of $z$; the class of the units and the class of the zero divisors are disjoint. They need not exhaust the algebra, and the disjointness does use associativity: in a non-associative unital algebra a unit can be a zero divisor.

### The Annihilators

**Definition.** The **left annihilator** and the **right annihilator** of $z \in A$ are
$$
\operatorname{Ann}_{\ell}(z) = \{ w \in A : zw = 0 \}, \qquad \operatorname{Ann}_{r}(z) = \{ w \in A : wz = 0 \}.
$$

**Proposition.** $\operatorname{Ann}_{\ell}(z)$ and $\operatorname{Ann}_{r}(z)$ are $R$-submodules of $A$, and for a nonzero $z$ the annihilator $\operatorname{Ann}_{\ell}(z)$ is nonzero exactly when $z$ is a left zero divisor while $\operatorname{Ann}_{r}(z)$ is nonzero exactly when $z$ is a right zero divisor. If $A$ is associative, $\operatorname{Ann}_{\ell}(z)$ is a right ideal and $\operatorname{Ann}_{r}(z)$ is a left ideal.

**Proof.** Both sets are additive, since the product is additive in each variable. For the scalars, $z(\lambda w) = \varsigma(\lambda)(zw) = 0$ when $zw = 0$ by the second rule, and $(\lambda w)z = \lambda(wz) = 0$ when $wz = 0$ by the first rule; so the two are $R$-submodules. For the ideals, if $w \in \operatorname{Ann}_{\ell}(z)$ and $a \in A$ then $z(wa) = (zw)a = 0$ by associativity, so $wa \in \operatorname{Ann}_{\ell}(z)$ and the left annihilator is a right ideal, and dually $(aw)z = a(wz) = 0$ makes the right annihilator a left ideal. The nonvanishing statements restate the definitions. $\square$

**Remark.** The scalars behave here better than on the derivations: a scalar entering an annihilator is pulled out by one of the two rules as a factor of zero, so no fixed ring appears, and the annihilators are $R$-submodules with no hypothesis. The difference is that in the annihilator the product is already zero, and the scalar meets a zero product rather than a product of two arbitrary elements.

### The Involution and the Sides

**Proposition.** For $z, w \in A$ one has $w \in \operatorname{Ann}_{\ell}(z)$ exactly when $w^{*} \in \operatorname{Ann}_{r}(z^{*})$; hence $\operatorname{Ann}_{\ell}(z)^{*} = \operatorname{Ann}_{r}(z^{*})$. In particular $z$ is a left zero divisor exactly when $z^{*}$ is a right zero divisor, so the involution maps the left zero divisors onto the right ones.

**Proof.** The element $zw$ vanishes exactly when $(zw)^{*} = w^{*}z^{*}$ vanishes, by the bijectivity of the involution and the anti-multiplicativity, and this is the condition $w^{*} \in \operatorname{Ann}_{r}(z^{*})$. Applying this to $*^{2} = \mathrm{id}$ gives the equality of sets, and the statement on the zero divisors is the nonvanishing form. $\square$

**Remark.** An element is a left zero divisor exactly when its conjugate is a right one; the two one-sided classes are exchanged by the involution, and a one-sided zero divisor therefore comes in a conjugate pair, one on each side.

### The Derived Operation

Let $A$ be associative with a $\varsigma$-semilinear involution, let $\star$ be the derived operation $x \star y = xy^{*}$, and write $\operatorname{Ann}^{\star}_{\ell}(z) = \{w : z \star w = 0\}$ for the left annihilator of $z$ for the derived operation.

**Proposition.** $\operatorname{Ann}^{\star}_{\ell}(z) = \operatorname{Ann}_{\ell}(z)^{*} = \operatorname{Ann}_{r}(z^{*})$, and $z$ is a left zero divisor for $\star$ exactly when it is a left zero divisor for the product.

**Proof.** The identity $z \star w = zw^{*}$ shows that $z \star w = 0$ exactly when $w^{*} \in \operatorname{Ann}_{\ell}(z)$, that is $w \in \operatorname{Ann}_{\ell}(z)^{*}$, and the equality with $\operatorname{Ann}_{r}(z^{*})$ is the proposition above. Since the involution is bijective, the set $\{w : zw^{*} = 0\}$ is nonzero exactly when $\{u : zu = 0\}$ is, which is the statement on the zero divisors. $\square$

**Remark.** The conjugate-linear slot of the derived operation does not change which elements are one-sided zero divisors, because the involution is bijective and merely renames the partner; what it changes is the side the partner is taken on, the $\star$-annihilator being the conjugate of the annihilator of the product. The same statement holds on the right, with $\operatorname{Ann}^{\star}_{r}(z) = \operatorname{Ann}_{\ell}(z^{*})$.

## The Centre and the Zero Divisors

### The Annihilator of a Central Element

**Proposition.** Let $A$ be associative and let $z \in Z(A)$. Then $\operatorname{Ann}_{\ell}(z) = \operatorname{Ann}_{r}(z)$, and it is a two-sided ideal of $A$. Consequently $z$ is a left zero divisor exactly when it is a right one, and it is a two-sided zero divisor or none.

**Proof.** For $z$ central, $zw = wz$ for every $w$, so the two annihilators are the same set. For $w$ in it and $a \in A$, $z(aw) = (za)w = (az)w = a(zw) = 0$ and $z(wa) = (zw)a = 0$, so the set is closed under both the left and the right multiplication by $A$, a two-sided ideal. The statement on the sides is the definition read with $z$ central. $\square$

### The Annihilator of the Algebra

**Definition.** The **left annihilator of $A$** is $\ell(A) = \{ w \in A : wA = 0 \}$, and the **right annihilator of $A$** is $r(A) = \{ w \in A : Aw = 0 \}$.

**Proposition.** Let $A$ be associative. Then $\ell(A)$ and $r(A)$ are two-sided ideals of $A$, and $r(A) = \ell(A)^{*}$. An algebra is of **full type**, in the sense of *Sesqualgebras*, only when both annihilators vanish.

**Proof.** If $wA = 0$ and $a, b \in A$ then $(aw)b = a(wb) = 0$ and $(wa)b = w(ab) = 0$ by associativity, so $\ell(A)$ is a two-sided ideal, and dually for $r(A)$. For the conjugation, $w \in \ell(A)$ means $wA = 0$, that is $(wA)^{*} = A^{*}w^{*} = Aw^{*} = 0$, so $w^{*} \in r(A)$ and $\ell(A)^{*} = r(A)$. The last statement restates the definition of the full type. $\square$

**Remark.** The left annihilator is the joint kernel of the left multiplications $L_{a}$ of *The Left and Right Multiplication Operators of a Sesqualgebra*, and the annihilators are two-sided ideals; their vanishing is the annihilator clause in the definition of the full type of *Sesqualgebras*.

### The Centre of a Unital or Annihilator-Free Algebra

**Theorem.** For $z \in Z(A)$ and every $\lambda \in R$ one has $(\lambda - \varsigma(\lambda))\,zA = 0$. Consequently, if some $\lambda - \varsigma(\lambda)$ acts injectively on $A$, then $zA = 0$, and by centrality $Az = 0$, so that $Z(A) \subseteq \ell(A) \cap r(A)$; under that hypothesis a unital $A$, or one with zero annihilator, has $Z(A) = 0$.

**Proof.** For $x \in A$ the centrality of $z$ at the element $\lambda x$ gives $z(\lambda x) = (\lambda x)z$, that is $\varsigma(\lambda)(zx) = \lambda(xz) = \lambda(zx)$ by the two scalar rules and the centrality of $z$; hence $(\lambda - \varsigma(\lambda))zx = 0$. If $\lambda - \varsigma(\lambda)$ is injective then $zx = 0$ for every $x$, and $Az = zA = 0$ by centrality. A unit lies in $A$, so $z = z1 = 0$, and a zero annihilator gives the same. $\square$

**Corollary.** Over $(\mathbb{C},\varsigma)$ with $\varsigma$ the conjugation, the scalar $i - \varsigma(i) = 2i$ acts injectively on every complex module, so the centre of a sesqualgebra over $(\mathbb{C},\varsigma)$ is contained in the annihilator of $A$. A unital sesqualgebra over $(\mathbb{C},\varsigma)$ has zero centre.

**Remark.** So a twisted centre is either zero or annihilating: over the complex numbers with the conjugation a nonzero central element kills the whole algebra, and a nonzero centre forces a nonzero annihilator. The bilinear case is different: the real matrix algebra of the examples below has the scalar matrices as its centre, and the twisted matrix algebra has none.

## Examples

### The Real Matrix Algebra

**Proposition.** Let $A = M_{n}(\mathbb{R})$ over the datum $(\mathbb{R},\mathrm{id})$ with the transpose as the involution and $n \geq 2$. Then the centre is the set of the scalar matrices, the zero divisors are the nonzero singular matrices, every nonsingular matrix is a unit, and the centre has no zero divisors.

**Proof.** A matrix $z$ is central exactly when $zX = Xz$ for every $X$, which forces $z$ to be diagonal with all the diagonal entries equal, that is $z = cI_{n}$; the standard computation is the one of *Centre, Units, Zero Divisors and Division Algebras*. A nonzero matrix is singular exactly when it annihilates a nonzero vector, that is, is a left zero divisor, and for the matrices the left and the right zero divisors coincide by the transpose; the nonsingular matrices are the units, and a nonzero scalar matrix is nonsingular. $\square$

### The Twisted Matrix Algebra

**Proposition.** Let $A = M_{n}(\mathbb{C})$ with the conjugate transpose $\dagger$, the product $x \star y = xy^{\dagger}$ and the datum $(\mathbb{C},\varsigma)$ with $\varsigma$ the conjugation, and let $n \geq 2$. Then the centre is zero, the left $\star$-zero divisors are the nonzero singular matrices, and there is no unit for the product.

**Proof.** The product is the derived operation of the involutive algebra $(M_{n}(\mathbb{C}),\dagger)$, and the annihilator of $A$ is zero, since $w \star A = 0$ gives $w = w \star 1 = w1^{\dagger} = 0$. The centre is therefore zero by the theorem, the corollary supplying the injectivity of $2i$. A matrix $z$ is a left $\star$-zero divisor exactly when $z \star w = zw^{\dagger} = 0$ for some nonzero $w$, that is $zu = 0$ for some nonzero $u = w^{\dagger}$, which is the singularity of $z$, by the proposition on the derived operation. The unit $1$ is a right unit but not a left one, since $1 \star w = w^{\dagger}$, so the product has no two-sided unit and the corollary on the unital case does not apply. $\square$

**Remark.** This is the algebra whose derivations are nonempty in *Derivations of a Sesqualgebra*: its centre is zero, so the map $a \mapsto \mathrm{ad}_{a}$ is injective here, and the centre, being the kernel of that map, cuts nothing.

### The Quaternions

**Proposition.** Let $A = \mathbb{H}$ over the datum $(\mathbb{R},\mathrm{id})$ with quaternion conjugation and the ordinary product. Then the centre is the set of the real quaternions, there are no zero divisors, and every nonzero quaternion is a unit.

**Proof.** The centre of $\mathbb{H}$ is $\mathbb{R}$ because $\mathbb{H}$ is a central division algebra over $\mathbb{R}$; a nonzero quaternion has a two-sided inverse $q^{-1} = q^{*}/(qq^{*})$ with $qq^{*}$ a nonzero real number, so it is a unit, and $A$ is a domain. $\square$

### The Sesquilinear Field

**Proposition.** Let $A = \mathbb{C}$ over the datum $(\mathbb{C},\varsigma)$ with $\varsigma$ the conjugation and the product $x \star y = x\bar y$. Then the centre is zero, there are no zero divisors, and there is no unit.

**Proof.** The centre: $z \star x = x \star z$ reads $z\bar x = x\bar z$ for every $x$; at $x = 1$ it gives $z = \bar z$, so $z$ is real, and at $x = i$ it gives $z\,\overline{i} = i\bar z$, that is $-iz = iz$, so $z = 0$. No zero divisors, since $z\bar x = 0$ forces $z = 0$ or $x = 0$. No unit: a two-sided unit $u$ satisfies $x \star u = x$ for every $x$, and at $x = 1$ this reads $\bar u = 1$, so $u = 1$, and then $1 \star x = \bar x$ differs from $x$ for a non-real $x$. $\square$

**Remark.** The field shows the twisted behaviour in its purest form: the centre is zero but the algebra is a domain, so the vanishing of the centre is not a degeneracy of the zero divisors but the effect of the injectivity of $2i$. The two notions are independent, and it is the annihilator that the theorem controls.

### A Twisted Algebra with a Nonzero Centre

**Proposition.** Let $A = \mathbb{C}^{2}$ with the product $(x_{1},x_{2}) \star (y_{1},y_{2}) = (x_{1}\bar y_{1}, 0)$, the involution $(x_{1},x_{2})^{*} = (\bar x_{1},\bar x_{2})$ and the datum $(\mathbb{C},\varsigma)$ with $\varsigma$ the conjugation. Then the centre is $\{(0,q) : q \in \mathbb{C}\}$, a nonzero subspace, and it is precisely the annihilator of $A$.

**Proof.** The product is additive in each variable, $(\lambda x) \star y = (\lambda x_{1}\bar y_{1}, 0) = \lambda(x \star y)$, and $x \star (\lambda y) = (x_{1}\overline{\lambda y_{1}}, 0) = \bar\lambda\,(x \star y) = \varsigma(\lambda)(x \star y)$, so the two scalar rules hold. The involution is additive, of order two, $\varsigma$-semilinear, and anti-multiplicative, since $(x \star y)^{*} = (\bar x_{1}y_{1}, 0)$ while $y^{*} \star x^{*} = (\bar y_{1}\overline{\bar x_{1}}, 0) = (\bar y_{1}x_{1}, 0)$ and $\mathbb{C}$ is commutative. For the centre, $z \star x = (z_{1}\bar x_{1}, 0)$ and $x \star z = (x_{1}\bar z_{1}, 0)$, and the equality for every $x$ forces $z_{1}\bar x_{1} = x_{1}\bar z_{1}$; at $x_{1} = 1$ this gives $z_{1} = \bar z_{1}$, and at $x_{1} = i$ it gives $-iz_{1} = iz_{1}$, so $z_{1} = 0$ and the centre is $\{(0,q)\}$. The annihilator is $\{w : wA = 0\}$, that is $w_{1}\bar x_{1} = 0$ for every $x_{1}$, which is $w_{1} = 0$, the same set. $\square$

**Remark.** This is the case the theorem allows: the centre is nonzero and it is annihilating, so the algebra is not of full type. Compared with the algebra on the same module, whose product is commutative and whose centre is therefore the whole algebra, the twist cuts the centre down to $\{(0,q)\}$.

## Summary

The centre of a sesqualgebra is the set of the elements that commute with every element, an additive subgroup, an $R$-submodule, and a subset stable under the involution; the parts it cuts by the involution are the Hermitian central elements and the skew-Hermitian central elements, which decompose the centre when $2$ is invertible. In the associative case the centre is a commutative $*$-subalgebra. The second scalar rule does not restrict it, unlike the derivations, which form a module over the fixed ring only, because the centrality of an element can be tested at the element $\lambda x$ and the two rules then agree. The centre is the set of the elements whose inner map vanishes, and in the twisted case over the complex numbers with the conjugation it is either zero or annihilating: if some $\lambda - \varsigma(\lambda)$ acts injectively then every central element kills the whole algebra, so a unital or annihilator-free sesqualgebra over $(\mathbb{C},\varsigma)$ has zero centre. The zero divisors come as one-sided and two-sided, and their annihilators are $R$-submodules with no scalar defect; the involution exchanges the left and the right classes, and the derived operation takes the left annihilator of an element to the conjugate of its left annihilator for the product, without changing which elements are one-sided zero divisors. A central element has equal left and right annihilators, and they are a two-sided ideal. The left and the right annihilators of the whole algebra are two-sided ideals exchanged by the involution, and their vanishing is the full-type hypothesis of the collapse theorems.

## Summary of Notation

| symbol | meaning |
|---|---|
| $Z(A) = C_{A}(A)$ | the centre, the centralizer of $A$ in itself |
| $C_{A}(S) = \{a : as = sa \text{ for } s \in S\}$ | the centralizer of a subset |
| $H(A)$, $S(A)$ | the Hermitian and the skew-Hermitian elements |
| $\mathrm{ad}_{a}(x) = ax - xa$ | the inner map; $\mathrm{ad}_{a} = 0$ exactly when $a \in Z(A)$, so the centre is the kernel of $a \mapsto \mathrm{ad}_{a}$ |
| $\operatorname{Ann}_{\ell}(z) = \{w : zw = 0\}$ | the left annihilator of $z$, a right ideal in the associative case |
| $\operatorname{Ann}_{r}(z) = \{w : wz = 0\}$ | the right annihilator of $z$, a left ideal in the associative case |
| $\ell(A) = \{w : wA = 0\}$, $r(A) = \{w : Aw = 0\}$ | the annihilators of $A$, two-sided ideals in the associative case |
| $x \star y = xy^{*}$ | the derived operation, with $\operatorname{Ann}^{\star}_{\ell}(z) = \operatorname{Ann}_{\ell}(z)^{*}$ |
| $R^{\varsigma}$ | the fixed ring, which governs the derivations and not the centre |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the centre of a ring with involution, the parts cut by the involution and the symmetric and the skew elements.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for the centre, the units and the zero divisors of a ring, and the annihilator arguments.
- Sterling K. Berberian, *Baer $*$-Rings* (Springer, 1972), for the interplay of an involution with the one-sided annihilators and the projection on the structure of an involutive ring.
