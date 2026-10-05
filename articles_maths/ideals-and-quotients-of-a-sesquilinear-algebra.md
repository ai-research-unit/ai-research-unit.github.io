# __Ideals and Quotients of a Sesquilinear Algebra__

## Introduction

A quotient of an algebra is formed by an ideal, and in a sesquilinear algebra an ideal has to respect one structure more than an ordinary algebra does: the two scalar rules. The two sides are not interchangeable here, because the product is $R$-linear in the first variable and $\varsigma$-semilinear in the second, so a left ideal and a right ideal are genuinely different sets, and the involution is the map that exchanges them. The involution descends to the quotient only when the ideal is carried to itself by it, and that is the second condition the algebra imposes.

Throughout, $A$ is a $\varsigma$-sesquilinear algebra with a $\varsigma$-semilinear involution $*$, in the sense of *Sesquilinear Algebras*, with the product of that article: additive in each variable, $R$-linear in the first slot and $\varsigma$-semilinear in the second. The product need not be associative; where an argument uses associativity it is said so.

What is added here: the three kinds of ideal and the $*$-ideal, the closure of the ideals under intersection and sum, the fact that the involution exchanges the two sides, the conjugate image $I^{*}$ and the smallest $*$-ideal through it, the quotient by a two-sided ideal together with the exact condition for the involution to descend, the first and third isomorphism theorems, and the three worked quotients $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{B}$.

## Ideals

### Definition

**Definition.** A **left ideal** of $A$ is an $R$-submodule $I \subseteq A$ with $AI \subseteq I$; a **right ideal** is an $R$-submodule with $IA \subseteq I$; a **two-sided ideal** is an $R$-submodule with both. The **conjugate image** of a subset $I$ is

$$
I^{*} = \{ x^{*} : x \in I \} ,
$$

and a **$*$-ideal** is a two-sided ideal with $I^{*} \subseteq I$.

**Remark.** The $R$-submodule condition is part of the definition because the quotient of an $R$-module is an $R$-module only by a submodule, and the scalar rules are read in the quotient through it. In a unital algebra the condition is automatic, as the proposition below shows, so there the three notions are the plain product-closed ones.

**Remark.** The two sides differ, and an ideal that is only one-sided is not a defect of the definition. In $M_n(\mathbb{C})$ with the conjugate transpose, the matrices whose last column vanishes form a left ideal: the last column of $AX$ is the product of $A$ with the last column of $X$, so it vanishes whenever that of $X$ does. They do not form a right ideal, since the last column of $XA$ is $X$ applied to the last column of $A$ and need not vanish. The same set is the conjugate image of the matrices whose last row vanishes, a right ideal, as the next proposition explains in general.

### The Unital Case

**Proposition.** Suppose $A$ is unital, with unit $1$. If an additive subgroup $I \subseteq A$ satisfies $AI \subseteq I$, then it is an $R$-submodule and a left ideal; if it satisfies $IA \subseteq I$, then it is an $R$-submodule and a right ideal; and if it satisfies both, it is an $R$-submodule and a two-sided ideal.

**Proof.** For the left case and $x \in I$, the first scalar rule gives $\lambda x = (\lambda 1)x \in AI \subseteq I$, so $I$ is closed under the scalars. For the right case and $x \in I$, the second rule gives $x(\lambda 1) = \varsigma(\lambda)x$, and $x(\lambda 1) \in IA \subseteq I$, so $\varsigma(\lambda)x \in I$ for every $\lambda$; since $\varsigma$ is a bijection with $\varsigma = \varsigma^{-1}$, every $\mu \in R$ is $\varsigma(\lambda)$ for $\lambda = \varsigma(\mu)$, so $\mu x \in I$ and $I$ is closed under the scalars. The two-sided case follows from either. $\square$

**Remark.** The right-hand case is where the sesquilinearity is felt at the level of ideals: it is the second scalar rule, not the first, that a right ideal obeys, and the bijectivity of $\varsigma$ is what converts the closure under the scalars $\varsigma(\lambda)$ into closure under all scalars. Without a unit the scalar closure is a genuine extra condition, which is why it is written into the definition.

### Elementary Closure

**Proposition.** The intersection of any family of left ideals is a left ideal, and the same holds for right ideals and for two-sided ideals; the sum $I + J$ of two left ideals is a left ideal, and likewise on the right and for two-sided ideals.

**Proof.** An intersection of $R$-submodules is an $R$-submodule, and $A \cdot \bigl(\bigcap_\alpha I_\alpha\bigr) \subseteq AI_\alpha \subseteq I_\alpha$ for every $\alpha$, hence the inclusion lands in the intersection. A sum of $R$-submodules is an $R$-submodule, and $A(I + J) \subseteq AI + AJ \subseteq I + J$. The right-hand case is the same with the product written on the other side and the two-sided case is the two together. $\square$

**Proposition.** The sum and the intersection of two $*$-ideals are $*$-ideals, and a two-sided ideal $I$ is a $*$-ideal if and only if $I^{*} = I$.

**Proof.** The involution is additive and swaps the sides, so $(I + J)^{*} = I^{*} + J^{*} = I + J$ and $(I \cap J)^{*} = I^{*} \cap J^{*} = I \cap J$ when $I$ and $J$ are $*$-ideals, and the sum and the intersection are two-sided by the previous proposition. For the last statement, $I^{*} \subseteq I$ gives $I = (I^{*})^{*} \subseteq I^{*}$ on applying $*$ again, hence equality, and the converse is immediate. $\square$

### The Involution Swaps the Two Sides

**Proposition.** If $I$ is a left ideal then $I^{*}$ is a right ideal, if $I$ is a right ideal then $I^{*}$ is a left ideal, and if $I$ is two-sided then $I^{*}$ is two-sided.

**Proof.** Let $I$ be a left ideal. An element of $I^{*}$ is $x^{*}$ with $x \in I$, and for $a \in A$,

$$
x^{*} a = (a^{*} x)^{*} ,
$$

because $*$ is anti-multiplicative and $*^{2} = \mathrm{id}$. Now $a^{*}x \in AI \subseteq I$, so $x^{*}a \in I^{*}$ and $I^{*}A \subseteq I^{*}$; thus $I^{*}$ is a right ideal. The other case is the same with the roles of the sides exchanged, and the two-sided case is the two together. $\square$

**Remark.** The involution is the map that identifies the two sides of the algebra, and the proposition is its statement at the level of ideals: the conjugate image of a left ideal is a right ideal. It is also the reason a $*$-ideal is defined as a two-sided ideal that is carried to itself, since for a one-sided ideal there is no self to be carried to.

### The Smallest $*$-Invariant Ideal

**Proposition.** Let $I$ be a two-sided ideal. Then $I + I^{*}$ is a two-sided ideal, it is the smallest $*$-ideal containing $I$, and it equals $I$ exactly when $I$ is a $*$-ideal.

**Proof.** By the proposition above $I^{*}$ is two-sided, and a sum of two-sided ideals is two-sided, so $I + I^{*}$ is two-sided. It is $*$-stable because $(I + I^{*})^{*} = I^{*} + I = I + I^{*}$. It contains $I$. If $J$ is any $*$-ideal containing $I$, then $I^{*} \subseteq J^{*} = J$, so $I + I^{*} \subseteq J$ and $I + I^{*}$ is the smallest. Finally $I + I^{*} = I$ says $I^{*} \subseteq I$, which is the definition of a $*$-ideal. $\square$

**Remark.** The proposition is the repair of a two-sided ideal that the involution does not preserve: the conjugate image detects the failure, $I \neq I^{*}$, and adjoining it by the sum gives the smallest ideal on which the involution is defined. The class of an element $x \in I$ with $x^{*} \notin I$ is the obstruction, since in the quotient the involution would have to send the class $I = 0 + I$ to the class $x^{*} + I$, which is nonzero.

## The Quotient

### The Product Descends

**Theorem (the quotient of a sesquilinear algebra).** Let $I$ be a two-sided ideal of $A$. Then the rule

$$
(x + I)(y + I) = xy + I
$$

is well defined, and with it $A/I$ is a $\varsigma$-sesquilinear algebra with the same base involution $\varsigma$; the quotient map $\pi : A \to A/I$ is a surjective homomorphism with kernel $I$.

**Proof.** Let $x' = x + i$ and $y' = y + j$ with $i, j \in I$. Then

$$
x'y' = xy + xj + iy + ij ,
$$

where $xj \in AI \subseteq I$ and $iy \in IA \subseteq I$ because $I$ is two-sided, and $ij \in II \subseteq AI \subseteq I$ because $i \in I \subseteq A$ and $I$ is a left ideal. Hence $x'y' \in xy + I$ and the product is well defined. It is additive in each variable because the product of $A$ is, and it inherits the scalar rules: $((\lambda x) + I)(y + I) = (\lambda x)y + I = \lambda(xy) + I = \lambda((x+I)(y+I))$ and $(x + I)((\lambda y) + I) = x(\lambda y) + I = \varsigma(\lambda)xy + I = \varsigma(\lambda)((x+I)(y+I))$. The quotient map is additive and multiplicative by construction, it is surjective because every class is the image of a representative, and its kernel is the class of $0$, which is $I$. $\square$

**Remark.** No associativity is used. The three inclusions $AI \subseteq I$, $IA \subseteq I$ and $II \subseteq I$ are what the well-definedness requires, and the third follows from the first because $I \subseteq A$. The quotient inherits the base involution $\varsigma$ unchanged, because the base ring is not touched by the quotient; what descends is the algebra, and it descends as a sesquilinear algebra over the same datum $(R, \varsigma)$.

### The Involution Descends

**Theorem (the involution descends exactly for a $*$-ideal).** Let $I$ be a two-sided ideal. Then the rule

$$
(x + I)^{*} = x^{*} + I
$$

defines a map on $A/I$ if and only if $I$ is a $*$-ideal, and in that case $A/I$ is an algebra with a $\varsigma$-semilinear involution, and $\pi$ is a $*$-homomorphism.

**Proof.** Suppose first that the rule defines a map. For $x \in I$ the class $x + I$ is $0 + I$, so $x^{*} + I = 0^{*} + I = I$ and $x^{*} \in I$; hence $I^{*} \subseteq I$ and $I$ is a $*$-ideal. Conversely suppose $I^{*} \subseteq I$ and let $x' - x \in I$. Then $x'^{*} - x^{*} = (x' - x)^{*} \in I^{*} \subseteq I$, so $x'^{*}$ and $x^{*}$ have the same class and the rule is well defined. The induced map is additive, it has $*^{2} = \mathrm{id}$ and the anti-multiplicativity $(xy)^{*} = y^{*}x^{*}$ inherited from $A$, and the second scalar rule holds in the quotient because it holds in $A$ and the product descends; hence $A/I$ is an algebra with a $\varsigma$-semilinear involution. Finally $\pi(x^{*}) = x^{*} + I = (x + I)^{*} = \pi(x)^{*}$, so $\pi$ is a $*$-homomorphism. $\square$

**Remark.** Two conditions are needed for the quotient, and they are independent: two-sidedness lets the product descend, and $*$-stability lets the involution descend. A two-sided ideal need not be $*$-stable, and the commutative case already shows it: in $\mathbb{C}[x]$ with the involution of complex conjugation on the coefficients, the ideal $(x - i)$ is two-sided, since the algebra is commutative, while $(x - i)^{*} = (x + i) \neq (x - i)$, so the involution does not descend and the quotient carries none, even though it is the field $\mathbb{C}$.

## Homomorphisms

### Kernels and Images

**Definition.** A **homomorphism** of $\varsigma$-sesquilinear algebras $f : A \to B$ is an $R$-linear map with $f(xy) = f(x)f(y)$; it is a **$*$-homomorphism** if in addition $f(x^{*}) = f(x)^{*}$.

**Remark.** Only the first scalar rule is imposed, and the second is then a consequence: $f(x(\lambda y)) = f(\varsigma(\lambda) xy) = \varsigma(\lambda) f(x)f(y) = f(x)(\lambda f(y))$. The $\varsigma$-semilinearity of the product in the second slot is carried by the $R$-linearity of $f$ together with the sesquilinearity of the two products, so the definition does not need to name it.

**Proposition.** The kernel of a homomorphism is a two-sided ideal, and the kernel of a $*$-homomorphism is a $*$-ideal. The image is an $R$-submodule closed under the product.

**Proof.** The kernel is an $R$-submodule because $f$ is $R$-linear. For $x \in \ker f$ and $a \in A$ one has $f(ax) = f(a)f(x) = 0$ and $f(xa) = f(x)f(a) = 0$, so $ax$ and $xa$ lie in $\ker f$, which is therefore two-sided. If $f$ is a $*$-homomorphism and $x \in \ker f$ then $f(x^{*}) = f(x)^{*} = 0$, so $x^{*} \in \ker f$ and the kernel is a $*$-ideal. The image of an $R$-linear map is an $R$-submodule, and $f(x)f(y) = f(xy)$ is the image of $xy$, so the image is closed under the product. $\square$

### The First Isomorphism Theorem

**Theorem.** Let $f : A \to B$ be a homomorphism with kernel $I$. Then $I$ is a two-sided ideal, and the map $\bar f : A/I \to B$ given by $\bar f(x + I) = f(x)$ is well defined, injective and multiplicative, and it is an isomorphism of $A/I$ onto $f(A)$. If $f$ is a $*$-homomorphism then $I$ is a $*$-ideal and $\bar f$ is a $*$-isomorphism.

**Proof.** The kernel is a two-sided ideal by the proposition above. If $x' - x \in I$ then $f(x') - f(x) = f(x' - x) = 0$, so $\bar f$ is well defined, and it is additive and multiplicative because $f$ is. Its kernel is the set of the classes $x + I$ with $f(x) = 0$, which is the single class $I$, so $\bar f$ is injective; its image is $f(A)$ by construction, so it is an isomorphism onto it. If $f$ is a $*$-homomorphism then $I$ is a $*$-ideal, the involution descends to $A/I$, and $\bar f((x + I)^{*}) = \bar f(x^{*} + I) = f(x^{*}) = f(x)^{*} = \bar f(x + I)^{*}$, so $\bar f$ is a $*$-isomorphism. $\square$

**Remark.** The first isomorphism theorem has the same shape as in the ordinary case, and the only change is the second clause: the isomorphism respects the involution exactly when the map does, which is the same condition under which the involution descends to the quotient. The kernel and the quotient carry the same datum $(R, \varsigma)$ as the algebra, so no change of base occurs anywhere in the statement.

**Theorem (the third isomorphism theorem).** Let $I \subseteq J$ be two-sided ideals of $A$. Then $J/I$ is a two-sided ideal of $A/I$, and

$$
\frac{A/I}{J/I} \; \cong \; A/J
$$

as $\varsigma$-sesquilinear algebras. If in addition $I$ and $J$ are $*$-ideals, then the involution descends to each of them and the isomorphism is a $*$-isomorphism.

**Proof.** The map $A \to A/J$ is a homomorphism with kernel $J$, and it factors through $A/I$ because $I \subseteq J$: if $x' - x \in I \subseteq J$ then $x'$ and $x$ have the same class modulo $J$, so $x + I \mapsto x + J$ is well defined. It is $R$-linear and multiplicative as a composite of homomorphisms, it is onto because both quotient maps are, and its kernel is the set of the classes $x + I$ with $x \in J$, which is $J/I$; this is therefore a two-sided ideal of $A/I$, and the first isomorphism theorem applied to the map gives the isomorphism. When $I$ and $J$ are $*$-ideals, an $x + I \in J/I$ has $x \in J$ and $(x+I)^{*} = x^{*} + I$ with $x^{*} \in J$, so $J/I$ is $*$-stable, and the map is induced by the quotient maps, which are $*$-homomorphisms, hence is a $*$-isomorphism. $\square$

## Three Worked Quotients

### The Complex Numbers

**Proposition.** Let $A = \mathbb{R}[x]$ with $\varsigma = \mathrm{id}$ and the involution fixing $\mathbb{R}$ and sending $x$ to $-x$. Then the ideal $I = (x^{2} + 1)$ is a $*$-ideal and the quotient $A/I$ is $\mathbb{C}$ with the involution of complex conjugation.

**Proof.** The algebra is commutative, so $I$ is two-sided. The generator is $*$-fixed, $(x^{2}+1)^{*} = (-x)^{2} + 1 = x^{2}+1$, so $I^{*} = I$ and $I$ is a $*$-ideal, and the involution descends. The quotient is $\mathbb{R}[x]/(x^{2}+1) = \mathbb{C}$, the class of $x$ being a root of $t^{2}+1$, and the descended involution sends that class to the class of $-x$, which is its negative, so it is the map $i \mapsto -i$, that is complex conjugation. $\square$

### The Quaternions

**Proposition.** Let $A$ be the free associative $\mathbb{R}$-algebra on $x, y$ with the involution $x^{*} = -x$, $y^{*} = -y$. Then the ideal $J$ generated by $x^{2}+1$, $y^{2}+1$ and $xy + yx$ is a $*$-ideal and the quotient is $\mathbb{H}$ with the involution that negates $i, j, k$.

**Proof.** Each generator is $*$-fixed: $x^{2}+1$ and $y^{2}+1$ because $(-x)^{2} = x^{2}$ and likewise for $y$, and $xy + yx$ because $(xy + yx)^{*} = y^{*}x^{*} + x^{*}y^{*} = yx + xy$. An ideal generated by $*$-fixed elements is a $*$-ideal, since $(\sum a_i g_i b_i)^{*} = \sum b_i^{*} g_i a_i^{*}$ is again in the ideal. The quotient is the algebra presented by $x^{2} = y^{2} = -1$ and $xy = -yx$, which is $\mathbb{H}$ with $x = i$, $y = j$ and $xy = k$. The descended involution sends $x$ to $-x$ and $y$ to $-y$, hence $k = xy$ to $(xy)^{*} = y^{*}x^{*} = (-y)(-x) = yx = -xy = -k$, so it is the involution that negates the three imaginary units. $\square$

### The Biquaternions

**Proposition.** Let $A$ be the free associative $\mathbb{C}$-algebra on $x, y$ with $\varsigma$ the conjugation and the involution $x^{*} = -x$, $y^{*} = -y$ together with $\varsigma$ on the coefficients. Then the ideal generated by the same three elements is a $*$-ideal and the quotient is the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ with the involution acting by $\varsigma$ on the coefficients of $\mathbb{C}$ and by the negation of $i, j, k$ on the quaternion factor.

**Proof.** The three generators are still $*$-fixed, because the coefficients in $x^{2}+1$ and $y^{2}+1$ are the fixed scalars $1$, and $xy + yx$ is again fixed as above; an ideal generated by fixed elements is a $*$-ideal. The quotient is the complexification of the algebra of the previous proposition, that is $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, and the descended involution is the tensor product of the conjugation of $\mathbb{C}$ with the negation of the three units, which is what the acting of $*$ gives on the generators and hence on all of $\mathbb{B}$. $\square$

**Remark.** The three examples are the same construction over an increasing base: the quotient of a free or polynomial algebra by the ideal of the defining relations, which is $*$-stable because the relations are, and the descended involution is the standard one of the algebra obtained. The obstruction of the previous section does not arise here. The complex and the biquaternion algebras are among the standard examples of the category in *Sesquilinear Algebras*, where they appear with these involutions, the quaternions being the real algebra whose complexification is $\mathbb{B}$.

## Summary

A left ideal of a sesquilinear algebra is an $R$-submodule $I$ with $AI \subseteq I$, a right ideal one with $IA \subseteq I$, and a two-sided ideal one with both; a $*$-ideal is a two-sided ideal with $I^{*} \subseteq I$, where $I^{*}$ is the conjugate image. The ideals are closed under intersection and sum, the involution exchanges the left and the right ideals by $x^{*}a = (a^{*}x)^{*}$, and the smallest $*$-ideal containing a two-sided ideal $I$ is $I + I^{*}$, which equals $I$ exactly when $I$ is a $*$-ideal. The quotient $A/I$ by a two-sided ideal is a sesquilinear algebra over the same datum $(R, \varsigma)$, with the product $(x+I)(y+I) = xy + I$, and the involution descends to it exactly when $I$ is a $*$-ideal, as in $\mathbb{C}[x]/(x - i)$ it does not. The kernel of a homomorphism is a two-sided ideal, the kernel of a $*$-homomorphism is a $*$-ideal, and $A/\ker f$ is isomorphic to the image of $f$, as algebras with involution when $f$ is a $*$-homomorphism; for two-sided ideals $I \subseteq J$ one has $(A/I)/(J/I) \cong A/J$, a $*$-isomorphism when both ideals are $*$-ideals. The quotients of the free algebras by the defining relations of the classical algebras give $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{B}$ with their standard involutions.

## Summary of Notation

| symbol | meaning |
|---|---|
| $AI \subseteq I$ | the condition for a left ideal, $A$ multiplying on the left |
| $IA \subseteq I$ | the condition for a right ideal, $A$ multiplying on the right |
| $I^{*} = \{x^{*} : x \in I\}$ | the conjugate image, a right ideal when $I$ is a left ideal |
| $I^{*} \subseteq I$ | the condition for a $*$-ideal, equivalently $I^{*} = I$ |
| $I + I^{*}$ | the smallest $*$-ideal containing the two-sided ideal $I$ |
| $(x+I)(y+I) = xy + I$ | the product on the quotient by a two-sided ideal |
| $(x+I)^{*} = x^{*} + I$ | the descended involution, defined exactly for a $*$-ideal |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the ideals, the involutions and the quotients of a ring with involution.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutive ideals and the quotients of an algebra with involution.
- Richard S. Pierce, *Associative Algebras* (Graduate Texts in Mathematics 88, Springer, 1982), for the general theory of the ideals and the quotients of an associative algebra.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Graduate Texts in Mathematics 131, Springer, 2001), for the isomorphism theorems and the ideals of a noncommutative algebra.
