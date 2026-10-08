# __Tensor Products of Sesqualgebras__

## Introduction

The direct product of two sesqualgebras multiplies them componentwise and needs no universal property at all; the tensor product is the other classical construction, and it is the one that is characterised by a universal property. It is the construction of *Tensor Products of Algebras* carried into the sesquilinear layer, and the one new datum the layer adds is the involution: the tensor product of two involutive algebras carries the involution $x\otimes y\mapsto x^{*}\otimes y^{*}$, and the question this article answers is what that involution does to the sesquilinear product and how the two factor structures sit inside the product.

The answer has two parts. The product of the tensor product is built from the products of the two factors and inherits their scalar rules, so $A\otimes_R B$ is a sesqualgebra over the same datum $(R,\varsigma)$ and the $\varsigma$-twist is carried through untouched. The involution is the subtler half: it is an anti-automorphism of the tensor product of the two associative products, and read on the sesquilinear product of the layer, which is the **derived** operation of those products, it does not preserve that product but **transposes** it, $\natural(X\star Y)=Y\star X$. That is what the involution of a tensor product of sesquilinear objects does, and it is the reason the tensor product is not the componentwise construction of *Direct Products of Sesqualgebras*: in the direct product the two factors annihilate one another, and here they commute and their products fill the algebra.

The setting is that of *Sesqualgebras*: $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, and a sesqualgebra over $(R,\varsigma)$ is an $R$-module $A$ with a product that is $R$-linear in the first variable and $\varsigma$-semilinear in the second; throughout, the product in play is the **derived** operation $x\star y=xy^{*}$ of an associative algebra carrying a $\varsigma$-semilinear involution ${}^{*}$ of order two with $(xy)^{*}=y^{*}x^{*}$, which is the standard example of *Sesqualgebras*, §*The Standard Example*, and ${}^{*}$ is the datum involution of the layer. Both factors are taken over the same datum. The universal property, the comparison with the free product and the tensor product of ideals are *Tensor Products of Algebras*; the componentwise construction and the central idempotents it cuts are *Direct Products of Sesqualgebras*; the transposed product and the two parities are *The Sesquilinear Product*; the two-sided ideals and the quotients are *Ideals and Quotients of a Sesqualgebra*; and the worked algebras are *Biquaternions as a General Plain Algebra (GPA) over $\mathbb{C}$*, *Biquaternions as an Algebra over $\mathbb{R}$* and *Biquaternions as a Vector Space over $\mathbb{C}$*.

---

## The Sesquilinear Tensor Product

### The Product on the Tensor Product

**Definition.** Let $A$ and $B$ be sesqualgebras over the same datum $(R,\varsigma)$. The **sesquilinear tensor product** $A\otimes_R B$ is the tensor product of the underlying $R$-modules, equipped with the product

$$
(a\otimes b)(c\otimes d) = ac\otimes bd, \qquad a, c\in A, \quad b, d\in B,
$$

extended to all of $A\otimes_R B$ by additivity, and with the involution defined in the next section.

The definition presumes that the displayed value on elementary tensors extends, exactly as in the bilinear layer. The products $ac$ and $bd$ are the products of the factors, which by hypothesis are $\varsigma$-sesquilinear; when the factors are presented as the derived operations of associative involutive algebras, as in §*The Two Products of the Tensor Product* below, this is the tensor product of those derived operations. The verifications are the ones of *Tensor Products of Algebras*, §*The Algebra Structure*, and are repeated only so far as the twist changes them.

**Proposition (well-definedness).** The product above is well defined, and $A\otimes_R B$ is an $R$-module with a product additive in each variable.

*Proof.* By the universal property of the tensor product of modules, an $R$-bilinear map $A\times B\to M$ into an $R$-module $M$ induces an $R$-linear map $A\otimes_R B\to M$. Fix $c\in A$ and $d\in B$ and consider $(a,b)\mapsto ac\otimes bd$; it is $R$-bilinear because the products of $A$ and $B$ are additive in each variable, so it induces an $R$-linear $L_{c,d}$ with $L_{c,d}(a\otimes b)=ac\otimes bd$. Fixing instead $x=\sum_ia_i\otimes b_i$ and mapping $(c,d)\mapsto L_{c,d}(x)$ is again $R$-bilinear and induces $R_x$ with $R_x(c\otimes d)=\sum_i a_ic\otimes b_id$; setting $xy=R_x(y)$ gives the product, well defined because $R_x$ depends on $x$ alone. $\square$

**Theorem (the two scalar rules).** If the products of $A$ and of $B$ are $R$-linear in the first variable and $\varsigma$-semilinear in the second, then so is the product of $A\otimes_R B$; the tensor product is therefore a sesqualgebra over the same datum $(R,\varsigma)$.

*Proof.* Additivity is the proposition. For the scalars it suffices to compute on elementary tensors. In the first variable,

$$
\bigl(\lambda(a\otimes b)\bigr)(c\otimes d) = (\lambda a\otimes b)(c\otimes d) = (\lambda a)c\otimes bd = \lambda(ac)\otimes bd = \lambda\bigl((a\otimes b)(c\otimes d)\bigr),
$$

by the first rule of $A$. In the second,

$$
(a\otimes b)\bigl(\lambda(c\otimes d)\bigr) = (a\otimes b)(\lambda c\otimes d) = a(\lambda c)\otimes bd = \varsigma(\lambda)(ac)\otimes bd = \varsigma(\lambda)\bigl((a\otimes b)(c\otimes d)\bigr),
$$

by the second rule of $A$. The two computations use $A$ alone; the same ones with $B$ in the second slot give the same conclusion, and the general case follows by additivity. $\square$

**Corollary (the collapse at $\varsigma = \mathrm{id}$).** If $\varsigma = \mathrm{id}$ then the products of $A$ and $B$ are bilinear, the product above is the ordinary tensor product of algebras, and $A\otimes_R B$ is an ordinary $R$-algebra. As in *Sesqualgebras*, the sesquilinear construction contains the bilinear one as the case of the trivial base involution, and the tensor product contains the tensor product of algebras as the same case.

### The Tensor Involution

**Definition.** The **tensor involution** of $A\otimes_R B$ is the map

$$
\natural : A\otimes_R B\longrightarrow A\otimes_R B, \qquad \natural(a\otimes b) = a^{*}\otimes b^{*},
$$

extended by additivity.

**Theorem.** The tensor involution is well defined, additive, of order two, and $\varsigma$-semilinear: $\natural(\lambda x)=\varsigma(\lambda)\natural(x)$ for $\lambda\in R$ and $x\in A\otimes_R B$. If moreover the involutions of $A$ and of $B$ are anti-automorphisms of their products, then $\natural$ is an anti-automorphism of the product of $A\otimes_R B$,

$$
\natural(xy) = \natural(y)\,\natural(x) .
$$

*Proof.* Well definedness and additivity are the universal property of the tensor product of modules applied to $(a,b)\mapsto a^{*}\otimes b^{*}$, which is additive in each variable. Order two is $\natural^2(a\otimes b)=a^{**}\otimes b^{**}=a\otimes b$. Semilinearity is

$$
\natural\bigl(\lambda(a\otimes b)\bigr) = \natural(\lambda a\otimes b) = (\lambda a)^{*}\otimes b^{*} = \varsigma(\lambda)\,a^{*}\otimes b^{*} = \varsigma(\lambda)\,\natural(a\otimes b),
$$

using the semilinearity of ${}^{*}$ on $A$; the same with $B$ gives the other factor. For the anti-multiplicativity, on elementary tensors,

$$
\natural\bigl((a\otimes b)(c\otimes d)\bigr) = \natural(ac\otimes bd) = (ac)^{*}\otimes(bd)^{*} = c^{*}a^{*}\otimes d^{*}b^{*} = (c^{*}\otimes d^{*})(a^{*}\otimes b^{*}) = \natural(c\otimes d)\,\natural(a\otimes b),
$$

and the general case is additivity. $\square$

**Remark.** The hypothesis of the last clause is a hypothesis on the factors and not on the construction: the anti-multiplicativity of $\natural$ is the anti-multiplicativity of the two factor involutions read coordinatewise. It holds for the **envelope**, that is the associative product, where ${}^{*}$ reverses products by definition, and it fails for the **derived** operation $x\star y=xy^{*}$ that is the sesquilinear product of the layer; the next section shows what survives in that case, namely the transposition $\natural(x\star y)=y\star x$. The two readings of the construction are the tensor product of the two associative algebras and the sesquilinear tensor product of the two sesqualgebras, and they are different objects: the subalgebra of the tensor product generated by the two canonical images is closed under $\natural$ in the first reading and not in the second.

## The Two Products of the Tensor Product

### The Envelope and the Derived Operation

A sesqualgebra of the group carries an associative product together with its involution, and its sesquilinear product is the **derived operation** $x\star y=xy^{*}$ of *Sesqualgebras*, §*The Standard Example*. The tensor product carries both structures, and they behave differently under $\natural$.

**Theorem (the derived operation is the tensor product of the derived operations).** With $\star$ the derived operation of the tensor product and $\star$ also written for the derived operations of $A$ and of $B$,

$$
(a\otimes b)\star(c\otimes d) = (a\star c)\otimes(b\star d) .
$$

*Proof.* $(a\otimes b)\star(c\otimes d)=(a\otimes b)\,\natural(c\otimes d)=(a\otimes b)(c^{*}\otimes d^{*})=ac^{*}\otimes bd^{*}=(a\star c)\otimes(b\star d)$. $\square$

**Theorem (the involution transposes the sesquilinear product).** Suppose the involutions of $A$ and of $B$ are anti-automorphisms of their products, as in the theorem above. Then for all $x, y\in A\otimes_R B$,

$$
\natural(x\star y) = y\star x .
$$

*Proof.* By the two theorems above and the anti-multiplicativity of the involutions of the factors, on elementary tensors $\natural\bigl((a\otimes b)\star(c\otimes d)\bigr)=\natural\bigl((ac^{*})\otimes(bd^{*})\bigr)=(ac^{*})^{*}\otimes(bd^{*})^{*}=ca^{*}\otimes db^{*}=(c\star a)\otimes(d\star b)=(c\otimes d)\star(a\otimes b)$, and the general case is additivity. $\square$

**Corollary.** Suppose the factors are unital, so that $A\otimes_R B$ has the unit $1\otimes 1$. Then the tensor involution is an anti-automorphism of the sesquilinear product $\star$, that is $\natural(x\star y)=\natural(y)\star\natural(x)$ for all $x$, $y$, if and only if both factor involutions are trivial and the tensor product of the envelopes is commutative. Whenever either factor carries a nontrivial involution it is not, and the identity $\natural(x\star y)=y\star x$ is then the sharp form of what it does. The reason is that $\natural$ is anti-multiplicative for the envelopes, so that $\natural(x\star y)=y\,\natural(x)$ and $\natural(y)\star\natural(x)=\natural(y)\,x$, and with the unit $y=1\otimes 1$ the two agree for every pair only if $\natural$ is the identity; the case of trivial involutions is left with the commutativity of the envelope alone. Without a unit the "only if" direction fails: the **zero product** is $\varsigma$-sesquilinear for every involution, its involution is an anti-automorphism because both products vanish, and the anti-automorphism property then holds with a nontrivial $\natural$. The transposed product $y\star x$ and its opposite parity are *The Sesquilinear Product*.

**Remark (the boundary of the construction).** The tensor product of two sesqualgebras is therefore not a sesqualgebra on which the tensor involution acts as an involution of the sesquilinear product, except in the degenerate case. What it is, and what the involution does, are the two theorems above: the product is sesquilinear and the involution transposes it. The obstruction is that $\natural$ is not the identity: an anti-automorphism of $\star$ forces $\natural=\mathrm{id}$ by the corollary above, so both factor involutions must be trivial, and by the collapse theorem of *Sesqualgebras*, §*The Collapse at the Identity*, a sesqualgebra of full type with a nontrivial involution is never associative. In the full-type case the transposition is therefore the trace of the failure of associativity of the derived operation, and not an accident of the construction.

## The Commuting Images

### The Two Maps

**Definition.** The **canonical maps** are

$$
\iota_A : A\to A\otimes_R B, \quad \iota_A(a) = a\otimes 1, \qquad \iota_B : B\to A\otimes_R B, \quad \iota_B(b) = 1\otimes b .
$$

**Theorem.** The two canonical maps are morphisms of sesqualgebras over $(R,\varsigma)$, they commute with the involution, and their images commute:

$$
\iota_A(a)\iota_B(b) = a\otimes b = \iota_B(b)\iota_A(a) .
$$

*Proof.* Additivity and $R$-linearity of $\iota_A$ are $(a+a')\otimes 1=(a\otimes 1)+(a'\otimes 1)$ and $(\lambda a)\otimes 1=\lambda(a\otimes 1)$, and its multiplicativity is $aa'\otimes 1=(a\otimes 1)(a'\otimes 1)$; the same holds with $\iota_B$. Compatibility with the involution is $\natural(a\otimes 1)=a^{*}\otimes 1$ and $\natural(1\otimes b)=1\otimes b^{*}$. The commuting is $(a\otimes 1)(1\otimes b)=a\otimes b=(1\otimes b)(a\otimes 1)$. $\square$

**Corollary.** Every element of $A\otimes_R B$ is a finite sum of products of an element of the image of $\iota_A$ and an element of the image of $\iota_B$, and the two images generate $A\otimes_R B$ as a sesqualgebra; the tensor product is generated by two commuting copies of its factors.

**Remark.** The commuting of the two images is the whole difference from the direct product. In $A\times B$ the two factors are ideals that annihilate one another, $(a,0)(0,b)=(0,0)$; here they commute and their products fill the whole algebra, which is why the tensor product mixes the factors and the direct product keeps them apart. The next section shows that this commuting condition is also exactly the condition the universal property needs.

## The Universal Property

### The Pairs with Commuting Images

**Theorem (universal property of $A\otimes_R B$).** Let $A$, $B$, $C$ be sesqualgebras over $(R,\varsigma)$ whose products are associative and unital and which carry their involutions. There is a natural bijection between

- morphisms $\Phi : A\otimes_R B\to C$ with $\Phi(\natural(x))=\Phi(x)^{*}$, the tensor product carrying the tensor involution $\natural$, and
- pairs of morphisms $f : A\to C$, $g : B\to C$ with $f(a^{*})=f(a)^{*}$, $g(b^{*})=g(b)^{*}$ and commuting images, $f(a)g(b)=g(b)f(a)$ for all $a$, $b$.

The pair recovered from $\Phi$ is $f(a)=\Phi(a\otimes 1)$, $g(b)=\Phi(1\otimes b)$, and the morphism recovered from the pair is $\Phi(a\otimes b)=f(a)g(b)$.

*Proof.* Given $\Phi$, the maps $f$ and $g$ are morphisms and commute with the involution, and their images commute because $(a\otimes 1)(1\otimes b)=a\otimes b=(1\otimes b)(a\otimes 1)$. Conversely, given $f$ and $g$ with commuting images, $(a,b)\mapsto f(a)g(b)$ is additive in each variable, hence induces an additive $\Phi$; multiplicativity is

$$
\Phi\bigl((a\otimes b)(c\otimes d)\bigr) = \Phi(ac\otimes bd) = f(ac)g(bd) = f(a)f(c)g(b)g(d) = f(a)g(b)f(c)g(d) = \Phi(a\otimes b)\Phi(c\otimes d),
$$

where the middle equality is the commuting of the images; and compatibility with the involution is

$$
\Phi\bigl(\natural(a\otimes b)\bigr) = \Phi(a^{*}\otimes b^{*}) = f(a^{*})g(b^{*}) = f(a)^{*}g(b)^{*} = \bigl(f(a)g(b)\bigr)^{*} = \Phi(a\otimes b)^{*},
$$

the second-to-last equality again by the commuting of the images. The two constructions are inverse. $\square$

**Corollary (the coproduct of the commutative factors).** If $A$, $B$, $C$ are commutative, the commuting condition is automatic and the theorem reads

$$
\operatorname{Hom}\bigl(A\otimes_R B, C\bigr) \cong \operatorname{Hom}(A, C)\times\operatorname{Hom}(B, C) ,
$$

so that $A\otimes_R B$ with the two canonical maps is the **coproduct** of $A$ and $B$ in the category of commutative sesqualgebras over $(R,\varsigma)$. It is not the product: the product of the category is the direct product of *Direct Products of Sesqualgebras*, and its two factors do not commute but annihilate.

### The Comparison with the Free Product

**Proposition.** The tensor product is not the coproduct in the category of all sesqualgebras over $(R,\varsigma)$. For noncommutative factors the coproduct is the free product, and the tensor product is its quotient by the relation that every element of $A$ commutes with every element of $B$.

*Proof.* The free product of *Tensor Products of Algebras*, §*The Universal Property*, satisfies the universal property of pairs of morphisms with no commuting condition; imposing $f(a)g(b)=g(b)f(a)$ is exactly the tensor product's condition, so the tensor product is the quotient of the free product by those relations. $\square$

**Remark.** The three constructions are distinguished by what they ask of the two factors, and the table is the one of *Direct Products of Sesqualgebras* with the sesquilinear column added.

| construction | the product of the pair | the coproduct | the involution |
|---|---|---|---|
| direct product $A\times B$ | $(a,b)(c,d)=(ac,bd)$ | no | $(a,b)^{*}=(a^{*},b^{*})$ |
| tensor product $A\otimes_R B$ | $(a\otimes b)(c\otimes d)=ac\otimes bd$ | for commuting images | $\natural(a\otimes b)=a^{*}\otimes b^{*}$ |
| free product $A\sqcup B$ | no componentwise form | yes | $x\mapsto x^{*}$ on the words |

Only the direct product is componentwise, only the free product is the coproduct without a commuting hypothesis, and only the tensor product makes the two factors commute and fills the product with their products.

## Worked Cases

### The Complex Matrices

For $A=M_m(\mathbb{C})$ and $B=M_n(\mathbb{C})$ with the conjugate transpose over the datum $(\mathbb{C},\varsigma)$ of the conjugation, the tensor product is the matrix algebra of the Kronecker product,

$$
M_m(\mathbb{C})\otimes_{\mathbb{C}} M_n(\mathbb{C}) \cong M_{mn}(\mathbb{C}), \qquad E_{ij}\otimes E_{kl}\mapsto E_{(i,k),(j,l)},
$$

and the tensor involution is the conjugate transpose of the large matrix: $\natural(X\otimes Y)=X^{\dagger}\otimes Y^{\dagger}=(X\otimes Y)^{\dagger}$. The derived operation of the tensor product is therefore the derived operation of $M_{mn}(\mathbb{C})$, and the involution transposes it, $\natural(X\star Y)=Y\star X$, which for the matrices is the identity $(X Y^{\dagger})^{\dagger}=Y X^{\dagger}$. The tensor product of two matrix sesqualgebras is therefore again a matrix sesqualgebra, the Kronecker product assembling the two factors into one; the case $m=n=1$ is the sesquilinear field of the last case below.

### The Biquaternions

Over $R=\mathbb{R}$ the base involution is trivial and the layer degenerates, and the tensor product of the two real involutive algebras $\mathbb{C}$ and $\mathbb{H}$ is the biquaternion algebra

$$
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H} = \mathbb{B},
$$

of $\mathbb{R}$-rank $8$, with the copy of $\mathbb{C}$ given by $\mathbb{C}\otimes 1$ central and commuting with the quaternion units $1\otimes e_k$. Because $\varsigma=\mathrm{id}$ the product is bilinear and the two scalar rules coincide, so the construction here is the tensor product of *Tensor Products of Algebras*, and the $\varsigma$-twist is carried by the **coefficient conjugation** of $\mathbb{B}$ rather than by the base. The tensor involution is the Hermitian conjugation ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ of *Biquaternions as a General Plain Algebra (GPA) over $\mathbb{C}$*, the conjugate-linear involution that conjugates the coefficients and negates the vector units, and with it $\mathbb{B}$ is the sesqualgebra of *Biquaternions as a General Plain Sesqualgebra (GPS) over $\mathbb{C}$*. The invariant of the case is that the twist sits in the coefficients: it is the coefficient conjugation, and not the trivial base involution, that makes the product sesquilinear.

### The Quaternion Matrices

Over $R=\mathbb{R}$ and with $A=B=\mathbb{H}$ carrying the quaternion conjugation, the tensor product is the matrix algebra

$$
\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H} \cong \operatorname{End}_{\mathbb{R}}(\mathbb{H}) = M_4(\mathbb{R}),
$$

through $x\otimes y\mapsto\bigl(h\mapsto xh\bar{y}\bigr)$, the left multiplication by $x$ followed by the right multiplication by $\bar{y}$. The map is multiplicative, and its image on the sixteen elementary tensors $e_a\otimes e_b$ of the quaternion basis is a basis of $M_4(\mathbb{R})$, so it is an isomorphism. Under it the tensor involution $\natural(x\otimes y)=\bar{x}\otimes\bar{y}$ is the **transpose**,

$$
\natural \longmapsto {}^{\mathsf{T}},
$$

because the adjoint of $h\mapsto xh\bar{y}$ for the quaternion scalar product is $h\mapsto\bar{x}hy$. This is the smallest case in which the tensor involution is visible as a familiar operator: on the tensor product of two copies of the quaternions it is the transpose of the matrix algebra, and the identity $\natural(x\star y)=y\star x$ of the section above is the identity $(XY^{\mathsf{T}})^{\mathsf{T}}=YX^{\mathsf{T}}$ of the matrices.

### The Field with Itself

For the sesquilinear field $\mathbb{C}$ over $(\mathbb{C},\varsigma)$ with product $z\star w=z\bar{w}$ and involution the conjugation, the tensor product is $\mathbb{C}$ again: under the identification $\mathbb{C}\otimes_{\mathbb{C}}\mathbb{C}\cong\mathbb{C}$ the product is $(z\otimes w)(z'\otimes w')=(zz')\otimes(ww')$, the derived operation is $(z\star z')\otimes(w\star w')$, and the tensor involution is the conjugation of the single copy. The identity $\natural(x\star y)=y\star x$ holds there because the field is commutative, so this is the degenerate case of the corollary and the one case in which the tensor involution is an anti-automorphism of the sesquilinear product after all.

## Summary

The **sesquilinear tensor product** $A\otimes_R B$ of two sesqualgebras over the same datum $(R,\varsigma)$ is the tensor product of the underlying modules with the product $(a\otimes b)(c\otimes d)=ac\otimes bd$ and the **tensor involution** $\natural(a\otimes b)=a^{*}\otimes b^{*}$. The product is $R$-linear in the first variable and $\varsigma$-semilinear in the second, so $A\otimes_R B$ is a sesqualgebra over $(R,\varsigma)$ and the $\varsigma$-twist is carried through the construction untouched; the involution is additive, $\varsigma$-semilinear, of order two, and an anti-automorphism of the product of the tensor product whenever the factor involutions are anti-automorphisms of their products.

The tensor product carries the **envelope** product and the **derived** sesquilinear operation $\star$, and the derived operation of the tensor product is the tensor product of the derived operations of the factors. The tensor involution does not preserve that sesquilinear product but **transposes** it: $\natural(x\star y)=y\star x$. It is therefore an anti-automorphism of the sesquilinear product, for unital factors, only when both factor involutions are trivial and the tensor product of the envelopes is commutative, and never for a factor that carries a nontrivial involution; the transposition is the sharp statement in general. The two **canonical maps** $a\mapsto a\otimes 1$ and $b\mapsto 1\otimes b$ are morphisms, they commute with the involution, and their images commute and generate the product; the tensor product is characterised by a universal property for the pairs of morphisms with commuting images, is the coproduct of the commutative factors, and is the quotient of the free product by the commuting relation, the coproduct of the noncommutative case being the free product itself.

The worked cases are the complex matrices, where $M_m(\mathbb{C})\otimes_{\mathbb{C}}M_n(\mathbb{C})\cong M_{mn}(\mathbb{C})$ with the Kronecker product and the conjugate transpose; the biquaternions $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}=\mathbb{B}$, where the base involution is trivial and the twist is carried by the coefficient conjugation; the quaternion matrices $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}\cong M_4(\mathbb{R})$, where the tensor involution is the transpose; and the sesquilinear field with itself, the commutative case in which the involution is an anti-automorphism of the sesquilinear product after all.

## Summary of Notation

| symbol | meaning |
|---|---|
| $A\otimes_R B$ | the sesquilinear tensor product of two sesqualgebras over $(R,\varsigma)$ |
| $(a\otimes b)(c\otimes d)=ac\otimes bd$ | the product of the tensor product |
| $\natural(a\otimes b)=a^{*}\otimes b^{*}$ | the tensor involution |
| $x\star y=xy^{*}$ | the derived sesquilinear operation |
| $\natural(x\star y)=y\star x$ | the involution transposes the sesquilinear product |
| $\iota_A(a)=a\otimes 1$, $\iota_B(b)=1\otimes b$ | the canonical maps, with commuting images |
| $\Phi(a\otimes b)=f(a)g(b)$ | the morphism of a pair with commuting images |
| $M_m(\mathbb{C})\otimes_{\mathbb{C}}M_n(\mathbb{C})\cong M_{mn}(\mathbb{C})$ | the Kronecker case |
| $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}=\mathbb{B}$ | the biquaternions |
| $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}\cong M_4(\mathbb{R})$ | the quaternion matrices, $\natural\mapsto{}^{\mathsf{T}}$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the tensor product of modules and algebras and its universal property.
- Serge Lang, *Algebra* (Springer, third edition, 2002), for the tensor product of algebras, the coproduct of commutative algebras and the free product.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the tensor product of involutive algebras and the involution of a tensor product.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the involutions of a tensor product and their behaviour on the factors.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for the matrix algebras, the Kronecker product and the quaternion algebras.
- The companion articles of this series: *Sesqualgebras*, *Direct Products of Sesqualgebras*, *Tensor Products of Algebras*, *The Sesquilinear Product*, *Ideals and Quotients of a Sesqualgebra*, *Matrix Sesqualgebras*, *Biquaternions as a General Plain Sesqualgebra (GPS) over $\mathbb{C}$* and *Biquaternions as a General Plain Algebra (GPA) over $\mathbb{C}$*.
