# __The Sesquilinear Sandwich Operator__

## Introduction

The sesqualgebra built from an associative algebra with an involution has a two-sided operator, the map $x \mapsto a x^{*} b$, obtained by putting the involution in the middle slot and a fixed element on each side. It is the operator form of the triple product $\{a, x, b\}$ of *Sesqualgebras*, read with the middle slot as the variable, and it is the smallest operator that uses the whole sesquilinear structure: one slot carries the involution, two carry the multiplication, and the result is a conjugate-linear map of the same $\varsigma$-twisted kind as the left multiplication. This article develops the family of those operators, its composition law, the monoid that it generates together with the ordinary two-sided multiplications, the criterion for a sandwich to be invertible together with the kernel of its parametrisation, and the reflections that the unitary elements produce.

The subject is the operator theory of the category, and it belongs to the group *Operator Theory* of the sesqualgebras. The sandwich stands to the sesqualgebra as the ordinary two-sided multiplication $x \mapsto axb$ stands to the associative algebra, and as the signed sandwich of *The Signed Sandwich on a Bimodule over an Algebra* stands to the algebra with an involution; the left and the right multiplication of the category, which are the one-sided cases, are *The Left and Right Multiplication Operators of a Sesqualgebra*. The triple product from which the sandwich is built, its additivity, its two linear slots and its one conjugate-linear slot, are *Sesqualgebras*, §*The Ternary Product*; the Jordan triple identity it satisfies is *Algebraic J\*-Algebras*; and the operator attached to a pair with the third slot as the variable, together with the Lie structure that the operators form, is *The Ternary Product as an Operator*.

The setting is the standard example of *Sesqualgebras*: $A$ is an associative unital $R$-algebra with a $\varsigma$-semilinear involution $*$, the sesquilinear product is $x \star y = xy^{*}$, and the triple product is $\{x,y,z\} = (x \star y) \star z^{*} = xy^{*}z$. Juxtaposition denotes the associative product of $A$. The unitary elements and the inner $*$-automorphisms are *Units and the Unitary Elements*; the inner involutions $\sigma_u(x) = ux^{*}u^{*}$ and the criterion for them to be of order two are *The Involutions of a Sesqualgebra*; and the bilinear case $\varsigma = \mathrm{id}$, where the two families are both $R$-linear, is *Left and Right Multiplication*.

---

## The Definition

### The Sandwich

**Definition.** For $a, b \in A$ the **sesquilinear sandwich** with parameters $a$ and $b$ is the operator

$$
\mathcal{T}_{a,b}(x) = a\,x^{*}\,b = \{a, x, b\} .
$$

The **ordinary two-sided multiplication** with the same parameters is $L_{a}R_{b}(x) = axb$.

**Proposition.** The operator $\mathcal{T}_{a,b}$ is additive and $\varsigma$-semilinear, $\mathcal{T}_{a,b}(\lambda x) = \varsigma(\lambda)\mathcal{T}_{a,b}(x)$, so it lies in $\operatorname{End}_{R^{\varsigma}}(A)$; the operator $L_{a}R_{b}$ is additive and $R$-linear, so it lies in $\operatorname{End}_{R}(A)$.

**Proof.** Additivity and the scalars are those of the triple product, which is $R$-linear in the first and the third variable and $\varsigma$-semilinear in the middle, by *Sesqualgebras*, §*The Ternary Product*; here the first and the third variables are the fixed parameters $a$ and $b$, and the middle variable is $x$. The slot through which the scalar enters is therefore the middle one, and it is the $\varsigma$-semilinear one.

**Remark.** The sandwich is the two-sided operator of the sesquilinear structure and the ordinary two-sided multiplication is the two-sided operator of the associative structure, and the whole difference between them is the involution in the middle: $\mathcal{T}_{a,b} = L_{a}R_{b} \circ {}^{*}$, where ${}^{*}$ is the involution itself, regarded as an operator on $A$. The involution is an anti-automorphism, not an automorphism, and it is exactly the crossing of the two factors in a product that the middle slot performs.

### The Two Families

**Proposition.** The two families convert into each other under the involution:

$$
\boxed{\;\mathcal{T}_{a,b} = L_{a}R_{b} \circ {}^{*} , \qquad {}^{*} \circ L_{p}R_{q} = \mathcal{T}_{q^{*},\,p^{*}}\;} .
$$

**Proof.** The first is the definition. For the second, $({}^{*} \circ L_{p}R_{q})(x) = (p x q)^{*} = q^{*} x^{*} p^{*} = \mathcal{T}_{q^{*},p^{*}}(x)$, using $(uv)^{*} = v^{*}u^{*}$ and $*^{2} = \mathrm{id}$.

**Corollary.** The sandwiches are exactly the products of an ordinary two-sided multiplication with the involution, on one side or the other, so the two families generate the same monoid.

**Proof.** Every sandwich is $L_{a}R_{b} \circ {}^{*}$ and every composite $\mathcal{T}_{q^{*},p^{*}}$ is ${}^{*} \circ L_{p}R_{q}$, so the two families differ by one factor of ${}^{*}$ and the monoid they generate is the same whether the involution is adjoined on the left or on the right.

**Remark.** The parametrisation is not injective: for a **central** unit $p$ one has $\mathcal{T}_{ap,\,p^{-1}b} = \mathcal{T}_{a,b}$, because $p$ commutes with $x^{*}$. On the units the kernel is exactly the group of the central units, as the proposition on the parametrisation below makes precise, so the invertible sandwiches are the quotient of $A^{\times} \times A^{\times}$ by that action.

## The Composition

### The Multiplication Table

**Theorem.** For $a, b, c, d, p, q, r, s \in A$ the composites are

$$
\mathcal{T}_{c,d} \circ \mathcal{T}_{a,b} = L_{c b^{*}}R_{\, a^{*} d} , \qquad L_{p}R_{q} \circ \mathcal{T}_{a,b} = \mathcal{T}_{pa,\, bq} ,
$$
$$
\mathcal{T}_{c,d} \circ L_{p}R_{q} = \mathcal{T}_{c q^{*},\, p^{*} d} , \qquad L_{p}R_{q} \circ L_{r}R_{s} = L_{pr}R_{\, sq} .
$$

**Proof.** Each is a direct computation with $(uv)^{*} = v^{*}u^{*}$ and the associativity of $A$. For the first, $\mathcal{T}_{c,d}(\mathcal{T}_{a,b}(x)) = c\,(a x^{*} b)^{*}\,d = c\,b^{*} x\,a^{*} d = L_{cb^{*}}R_{a^{*}d}(x)$. For the second, $L_{p}R_{q}(\mathcal{T}_{a,b}(x)) = p\,a x^{*} b\,q = \mathcal{T}_{pa, bq}(x)$. For the third, $\mathcal{T}_{c,d}(L_{p}R_{q}(x)) = c\,(p x q)^{*}\,d = c\,q^{*} x^{*} p^{*} d = \mathcal{T}_{cq^{*}, p^{*}d}(x)$. For the fourth, $L_{p}R_{q}(L_{r}R_{s}(x)) = p r x s q = L_{pr}R_{ sq}(x)$.

**Corollary (the parity).** The composite of two sandwiches is an ordinary two-sided multiplication, that of a sandwich and a two-sided multiplication in either order is a sandwich, and that of two two-sided multiplications is a two-sided multiplication. So the sandwiches are not closed under composition, and the set
$$
\{L_{p}R_{q} : p, q \in A\} \cup \{\mathcal{T}_{a,b} : a, b \in A\}
$$
is a monoid under composition, with unit $L_{1}R_{1}$; when $\varsigma \neq \mathrm{id}$ the sandwiches are its $\varsigma$-semilinear elements and the two-sided multiplications its $R$-linear ones, while for $\varsigma = \mathrm{id}$ the two families are both $R$-linear and the parity collapses.

**Proof.** The four identities of the theorem say that the parity of the composite is the product of the two parities, in the sense of the two-element group, and that the two-sided operator produced by two sandwiches is the one displayed. Closure under composition is the four identities, and $L_{1}R_{1} = \mathrm{id}$ is the unit.

**Remark.** The composition of two sandwiches is the composition of two conjugate-linear maps, hence linear, and this is the reason the family does not close: a sandwich is a square root of a two-sided multiplication in the same sense in which an anti-automorphism of order two is a square root of an automorphism. In particular
$$
\mathcal{T}_{a,b} \circ \mathcal{T}_{a,b} = L_{a b^{*}}R_{\, a^{*} b} ,
$$
so a sandwich is an involution exactly when $a b^{*} = 1$, equivalently $a^{*} b = 1$, that is when $b = (a^{*})^{-1}$. For unitary parameters this last condition reads $b = a$.

**Corollary.** $\mathcal{T}_{a,b} \circ \mathcal{T}_{b^{*}, a^{*}} = L_{a^{2}}R_{b^{2}}$ and $\mathcal{T}_{1,1}$ is the datum involution ${}^{*}$.

**Proof.** Write the table as $\mathcal{T}_{p,q} \circ \mathcal{T}_{r,s} = L_{p s^{*}}R_{\, r^{*} q}$. At $(p,q) = (a,b)$ and $(r,s) = (b^{*},a^{*})$ this gives $p s^{*} = a (a^{*})^{*} = a^{2}$ and $r^{*} q = (b^{*})^{*} b = b^{2}$, so the composite is $L_{a^{2}}R_{b^{2}}$. The second statement is $\mathcal{T}_{1,1}(x) = 1\,x^{*}\,1 = x^{*}$.

## The Invertible Sandwiches

**Theorem.** The sandwich $\mathcal{T}_{a,b}$ is invertible if and only if $a$ and $b$ are units of $A$, and then

$$
\boxed{\;\mathcal{T}_{a,b}^{-1} = \mathcal{T}_{(b^{-1})^{*},\, (a^{-1})^{*}}\;} .
$$

**Proof.** If $a$ or $b$ is not a unit then multiplication by it is not injective, so $\mathcal{T}_{a,b}$ has a nonzero kernel and is not invertible. Conversely $\mathcal{T}_{a,b}(x) = a x^{*} b$ is inverted by $\mathcal{T}_{(b^{-1})^{*},(a^{-1})^{*}}$ by the table: writing the table as $\mathcal{T}_{p,q} \circ \mathcal{T}_{r,s} = L_{p s^{*}}R_{\, r^{*} q}$, the composite $\mathcal{T}_{a,b} \circ \mathcal{T}_{(b^{-1})^{*},(a^{-1})^{*}}$ is $L_{a d^{*}}R_{\, c^{*} b}$ with $c = (b^{-1})^{*}$ and $d = (a^{-1})^{*}$, that is $L_{a a^{-1}}R_{\, (b^{-1}) b} = L_{1}R_{1} = \mathrm{id}$, and the same computation in the other order gives $\mathrm{id}$ as well.

**Proposition (the kernel of the parametrisation).** Let $a, b, c, d$ be units of $A$. Then $\mathcal{T}_{a,b} = \mathcal{T}_{c,d}$ if and only if there is a central unit $p$ with $c = ap$ and $d = p^{-1} b$, and the assignment $(a,b) \mapsto \mathcal{T}_{a,b}$ induces a bijection from the quotient of $A^{\times} \times A^{\times}$ by the action $p \cdot (a,b) = (ap,\, p^{-1}b)$ of the central units onto the set of the invertible sandwiches.

**Proof.** The equality $\mathcal{T}_{a,b} = \mathcal{T}_{c,d}$ says $a x^{*} b = c x^{*} d$ for every $x$; multiplying by $a^{-1}$ on the left and by $b^{-1}$ on the right, it is $x^{*} = a^{-1}c\,x^{*}\,d\,b^{-1}$ for every $x$, that is, with $p = a^{-1}c$ and $q = d\,b^{-1}$, the identity $x^{*} = p\,x^{*}\,q$ for every $x$. At $x = 1$ this gives $pq = 1$, and then $x^{*} = p\,x^{*}\,p^{-1}$ for every $x^{*}$, which holds exactly when $p$ commutes with every element of $A$, since $*$ is onto; so $p$ is a central unit with $q = p^{-1}$, that is $c = ap$ and $d = p^{-1}b$. Conversely a central unit $p$ gives $\mathcal{T}_{ap, p^{-1}b} = \mathcal{T}_{a,b}$, since $p$ commutes with $x^{*}$.

**Remark.** The invertible sandwiches are not closed under composition: the product of two of them is an ordinary two-sided multiplication, by the table, and it is a two-sided multiplication rather than a sandwich precisely because the composite of two conjugate-linear maps is linear. They are therefore not a group, and the subgroup they generate together with the invertible two-sided multiplications is the unit group of the monoid of the corollary, with the sandwiches as its $\varsigma$-semilinear half and the two-sided multiplications as its $R$-linear half. For unitary parameters the inverse reads $\mathcal{T}_{u,v}^{-1} = \mathcal{T}_{v,u}$, since $(v^{-1})^{*} = v$ and $(u^{-1})^{*} = u$, and the kernel of the parametrisation is the group of the central unitary elements.

## The Reflections

### The Sandwich as a Reflection

**Proposition.** For a unitary $u$ the sandwich $\mathcal{T}_{u,u}$ is an involution of the module:

$$
\boxed{\;\mathcal{T}_{u,u}^{2} = L_{u u^{*}}R_{\, u^{*} u} = L_{1}R_{1} = \mathrm{id} , \qquad \mathcal{T}_{u,u}(x) = u\,x^{*}\,u\;} .
$$

**Proof.** The square is read from the table, and for a unitary $u$ one has $u u^{*} = 1 = u^{*} u$.

**Remark.** The reflection $\mathcal{T}_{u,u}$ is the composite $L_{u}R_{u} \circ {}^{*}$ of the involution with the two-sided multiplication by the unitary element $u$, so it is the sandwich that carries the unitary element on the two sides; the sandwich $\mathcal{T}_{u,u^{*}}$ is instead the inner involution, and it carries the unitary element on the left and its inverse on the right. The datum ${}^{*} = \mathcal{T}_{1,1}$ is the sandwich of the identity, and the reflections $\mathcal{T}_{u,u}$ are the family read along the unitary elements.

**Proposition.** Let $u$ be unitary. Then the sandwich $\mathcal{T}_{u, u^{*}}$ is the inner involution $\sigma_{u}(x) = ux^{*}u^{*}$ of *The Involutions of a Sesqualgebra*, and it is an involution exactly when $u^{2}$ is central.

**Proof.** $\mathcal{T}_{u,u^{*}}(x) = u\,x^{*}\,u^{*} = \sigma_u(x)$, and $\sigma_u^{2} = \alpha_{u^{2}}$, where $\alpha_{u^{2}}(x) = u^{2}x(u^{2})^{*}$ is the inner $*$-automorphism, by the theorem of *The Involutions of a Sesqualgebra*, §*The Family of a Unitary Element*, which is stated for a unitary $u$; since $u^{2}$ is then unitary as well, $\alpha_{u^{2}} = \mathrm{id}$ exactly when $u^{2}$ is central.

**Remark.** The two families $\mathcal{T}_{u,u}$ and $\mathcal{T}_{u,u^{*}}$ are the two ways of placing a unitary element in the sandwich: the first is always a reflection, the second is a reflection exactly when the square of the parameter is central, and the difference between them is the difference between $u$ and $u^{*}$ in the right slot. The second family is the inner family of the involutions of the sesqualgebra, which is the reason the criterion $u^{2} \in Z(A)$ of that article is a statement about sandwiches.

## Worked Cases

### The Complex Matrices

Let $A = M_n(\mathbb{C})$ with the conjugate transpose and $\varsigma$ the complex conjugation. The sandwich is $\mathcal{T}_{a,b}(X) = aX^{*}b$ and it is conjugate-linear: $\mathcal{T}_{a,b}(\lambda X) = \bar{\lambda}\mathcal{T}_{a,b}(X)$. The composition table is the one of the theorem, and the reflections appear as follows: for the swap $u = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ the sandwich $\mathcal{T}_{u,u}(X) = uX^{*}u$ is the conjugate transpose followed by the interchange of the rows and the columns, an involution of the space of the matrices; for $u = \operatorname{diag}(i, 1)$ the sandwich $\mathcal{T}_{u,u^{*}}(X) = uX^{*}u^{*}$ is not an involution, since $u^{2}$ is not central, which is the witness of *The Involutions of a Sesqualgebra*. The invertible sandwiches are those with $a$ and $b$ invertible matrices, with $\mathcal{T}_{a,b}^{-1} = \mathcal{T}_{(b^{-1})^{*},(a^{-1})^{*}}$, and for unitary $a$ and $b$ the inverse reads $\mathcal{T}_{b,a}$.

### The Field

Let $A = \mathbb{C}$ over $R = \mathbb{R}$, with $\varsigma = \mathrm{id}$ and $*$ the conjugation, which is an $\mathbb{R}$-linear involution of $\mathbb{C}$. The sandwich is $\mathcal{T}_{a,b}(x) = a\bar{x}b$ and the ordinary two-sided multiplication is $L_{p}R_{q}(x) = pqx$; both are $\mathbb{R}$-linear, so the two families are not separated by the parity here, and they are separated by the complex structure instead: $\mathcal{T}_{a,b}$ is, over $\mathbb{C}$, the conjugate-linear map $z \mapsto ab\bar{z}$, while $L_{p}R_{q}$ is the $\mathbb{C}$-linear map $z \mapsto pqz$. The composition table still holds and reads $\mathcal{T}_{c,d} \circ \mathcal{T}_{a,b} = L_{c\bar{b}}R_{\,\bar{a}d}$ in the multiplicative notation of the field, so the composite of two sandwiches is the $\mathbb{C}$-linear map of multiplication by $cd\,\overline{ab}$, and the reflections $\mathcal{T}_{u,u}$ with $|u| = 1$ are the maps $z \mapsto u^{2}\bar{z}$. The picture is the degeneration of the matrix one: the $\mathbb{C}$-linear maps $\mathbb{C} \to \mathbb{C}$ are the $z \mapsto cz$ and the conjugate-linear ones are the $z \mapsto c\bar{z}$, and these two classes do not exhaust the $\mathbb{R}$-linear maps, which are the sums $z \mapsto cz + d\bar{z}$.

### The Quaternions

Let $A = \mathbb{H}$ over $R = \mathbb{R}$ with $\varsigma = \mathrm{id}$ and the quaternion conjugation $q \mapsto \bar{q}$. The sandwich is $\mathcal{T}_{a,b}(q) = a\bar{q}b$, an $\mathbb{R}$-linear map of the algebra of the quaternions, and the composition table is the one of the theorem with $R^{\varsigma} = R$. The unitary elements are the quaternions of unit length, since $\bar{q}q = |q|^{2}$; the reflection $\mathcal{T}_{u,u}$ is the sandwich $q \mapsto u\bar{q}u$ for $u$ of unit length, and the inner involution $\mathcal{T}_{u,\bar{u}}$ is $q \mapsto u\bar{q}\bar{u}$. The square of a sandwich is $\mathcal{T}_{a,b}^{2} = L_{ab^{*}}R_{\, a^{*}b}$, the operator $q \mapsto ab^{*}\,q\,a^{*}b$, and for suitable parameters it is genuinely two-sided, since the quaternions are noncommutative. For $a = i$ and $b = k$ one has $ab^{*} = i\bar{k} = i(-k) = j$ and $a^{*}b = (-i)k = j$, so the square $\mathcal{T}_{i,k}^{2}$ is $q \mapsto jqj$, which fixes $i$ and sends $1$ to $-1$ and is therefore not a scalar multiple of the identity; in the commutative field the same composite collapses to a single multiplication.

## Summary

The sesquilinear sandwich is the two-sided operator $\mathcal{T}_{a,b}(x) = ax^{*}b = \{a,x,b\}$ of the standard example, $\varsigma$-semilinear in its variable, and it is the ordinary two-sided multiplication composed with the involution, $\mathcal{T}_{a,b} = L_{a}R_{b} \circ {}^{*}$. The two families satisfy the composition table $\mathcal{T}_{c,d}\mathcal{T}_{a,b} = L_{cb^{*}}R_{a^{*}d}$, $L_{p}R_{q}\mathcal{T}_{a,b} = \mathcal{T}_{pa,bq}$, $\mathcal{T}_{c,d}L_{p}R_{q} = \mathcal{T}_{cq^{*},p^{*}d}$ and $L_{p}R_{q}L_{r}R_{s} = L_{pr}R_{sq}$, so the sandwiches are not closed under composition: the composite of two of them is an ordinary two-sided multiplication, and the two families together form a monoid in which the parity is multiplicative.

The invertible sandwiches are those with invertible parameters, with $\mathcal{T}_{a,b}^{-1} = \mathcal{T}_{(b^{-1})^{*},(a^{-1})^{*}}$, and the parametrisation has the central units as its kernel, so that $\mathcal{T}_{ap,p^{-1}b} = \mathcal{T}_{a,b}$; the invertible sandwiches are not closed under composition, two of them composing to a two-sided multiplication. A sandwich is an involution exactly when $a b^{*} = 1$, which for unitary parameters reads $b = a$, so $\mathcal{T}_{u,u}$ is a reflection for every unitary $u$; the sandwich $\mathcal{T}_{u,u^{*}}$ is the inner involution $\sigma_u$, an involution exactly when $u^{2}$ is central. The family of the sandwiches is thus the place where the operator theory of the sesqualgebra, the unitary group and the inner involutions meet.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathcal{T}_{a,b}(x) = a x^{*} b$ | the sesquilinear sandwich, $\varsigma$-semilinear |
| $L_{p}R_{q}(x) = p x q$ | the ordinary two-sided multiplication, $R$-linear |
| $\mathcal{T}_{a,b} = L_{a}R_{b} \circ {}^{*}$ | the sandwich as an ordinary sandwich with the involution |
| ${}^{*} \circ L_{p}R_{q} = \mathcal{T}_{q^{*},p^{*}}$ | the involution moved across a two-sided multiplication |
| $\mathcal{T}_{c,d} \circ \mathcal{T}_{a,b} = L_{cb^{*}}R_{a^{*}d}$ | the composite of two sandwiches is $R$-linear |
| $L_{p}R_{q} \circ \mathcal{T}_{a,b} = \mathcal{T}_{pa,bq}$ | the composite of a linear and a conjugate-linear map |
| $\mathcal{T}_{a,b}^{2} = L_{ab^{*}}R_{a^{*}b}$ | the square of a sandwich |
| $\mathcal{T}_{a,b}^{-1} = \mathcal{T}_{(b^{-1})^{*},(a^{-1})^{*}}$ | the inverse on the invertible parameters |
| $\mathcal{T}_{u,u}$ | the reflection of a unitary $u$, an involution |
| $\mathcal{T}_{u,u^{*}} = \sigma_{u}$ | the inner involution of a unit $u$ |

## Further Reading

- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the triple products of a ring with involution and the operators they induce.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the sandwich operators of a ring with involution and the conjugate-linear maps attached to them.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the semilinear operators, the two-sided multiplications and the case of the trivial involution.
- The companion articles of this series: [Sesqualgebras](sesqualgebras.html), *Algebraic J\*-Algebras*, *The Left and Right Multiplication Operators of a Sesqualgebra*, *Units and the Unitary Elements*, *The Involutions of a Sesqualgebra*, *The Signed Sandwich on a Bimodule over an Algebra*, *The Ternary Product as an Operator* and *Left and Right Multiplication*.
