# __Jordan Algebras with an Involution__

## Introduction

An involution of an algebra is an anti-automorphism of order two; on the commutative symmetrised product of an associative algebra the distinction between an automorphism and an anti-automorphism disappears, and a **Jordan algebra with an involution** carries a semilinear map $\sigma$ of order two that **preserves** the Jordan product,

$$
\sigma(a\circ b) = \sigma(a)\circ\sigma(b) , \qquad \sigma^2 = \mathrm{id} , \qquad \sigma(\lambda a + \mu b) = \varsigma(\lambda)\sigma(a)+\varsigma(\mu)\sigma(b) ,
$$

with $\varsigma$ an involution of the field of scalars. The map $\sigma$ is a **conjugate-linear involution of the Jordan algebra**; because the Jordan product is commutative, it is at the same time an anti-automorphism and an automorphism of the product, so the algebra-theoretic distinction of *Involutive Linear Algebras*, where an involution reverses the product and an involutive automorphism preserves it, is void here: the two classes of order-two maps on a Jordan algebra coincide. What matters instead is whether the map is **linear** ($\varsigma = \mathrm{id}$) or **conjugate-linear** ($\varsigma \ne \mathrm{id}$), and this is the invariant the article develops.

The article defines the conjugate-linear involution of a Jordan algebra, introduces its **self-adjoint part** $H(J)$ and its skew part, and proves the decomposition $J = H(J)\oplus i\,H(J)$ in the conjugate-linear case over a field extension of degree two. It shows that the self-adjoint part is a Jordan subalgebra and that it is the fixed set of an involutive automorphism exactly in the linear case, so the conjugate-linear involution is the structure that genuinely adds a new object, the real Jordan algebra of self-adjoint elements. It states the **formal reality** of the involution as the condition that no nontrivial sum of squares of self-adjoint elements vanishes, and defers the theory of that condition to *Formally Real Algebras and the Sum of Squares*, later in this group. Finally it gives the **realisation**: for an associative algebra $A$ with involution $\ast$, the special Jordan algebra $J = A^+$ carries the involution $\sigma(a) = a^*$, under which $H(J)$ is the set $H(A)$ of the $\ast$-self-adjoint elements of $A$, themselves closed under the symmetrised product; so every special Jordan algebra with involution is the symmetrisation of an associative $\ast$-algebra, and the classification of the involutions of $J$ reduces to that of the involutions of $A$.

The article assumes *Involutive Linear Algebras* for the involution of an associative algebra, the symmetric and skew elements and the symmetrised product (cited, not reproved), *Jordan Algebras* for the Jordan object and its powers, *The Left and Right Multiplication Operators on a Jordan Algebra* for the quadratic representation and the structure group, *Algebras* and *Unital Algebras* for the objects, and *Tensor Products of Algebras* for the scalar extension $B\otimes_F K$. The real form of a complex Jordan algebra and the descent are *Real Forms and the Descent of an Algebra*; the symmetric powers, the symmetric algebra and the Jordan triples with an involution are the other entries of this group. Throughout, $F$ is a field, $K/F$ is a quadratic extension with nontrivial automorphism $\varsigma$ when a conjugate-linear involution is at hand, $J$ is a unital Jordan $F$-algebra, and $\sigma$ is a $\varsigma$-semilinear involution of $J$ preserving the product. No form, norm, distance or order occurs; the sum of squares is treated as an algebraic condition and its order-theoretic reading is Part III.

## Jordan Algebras with a Conjugate-Linear Involution

### Definition

**Definition.** Let $F$ be a field and let $\varsigma$ be an involution of $F$. A **$\varsigma$-semilinear involution** of a Jordan $F$-algebra $J$ is a map $\sigma : J \to J$ with

$$
\sigma(a+b) = \sigma(a)+\sigma(b), \quad \sigma(\lambda a) = \varsigma(\lambda)\,\sigma(a), \quad \sigma(a\circ b) = \sigma(a)\circ\sigma(b), \quad \sigma^2 = \mathrm{id}.
$$

It is **linear** when $\varsigma = \mathrm{id}$ and **conjugate-linear** when $\varsigma \ne \mathrm{id}$; a **Jordan algebra with involution** is a pair $(J,\sigma)$.

**Remark.** The Jordan product is commutative, so the equation $\sigma(a\circ b) = \sigma(a)\circ\sigma(b)$ is the same as $\sigma(a\circ b) = \sigma(b)\circ\sigma(a)$; a map of order two on a Jordan algebra that reverses the product therefore preserves it, and the two notions of *Involutive Linear Algebras* — the involution and the involutive automorphism — coincide as far as the product is concerned. The linear case is exactly an involutive automorphism of $J$; the conjugate-linear case is a new object.

**Proposition.** The map $\sigma$ is bijective, its restriction to the copy $F\cdot 1$ of the scalars is $\varsigma$, it preserves the powers, $\sigma(a^n) = \sigma(a)^n$ for every $n \ge 0$, and it commutes with the quadratic representation, $\sigma\circ U_{a,b} = U_{\sigma(a),\sigma(b)}\circ\sigma$, so that $\sigma\,U_a\,\sigma^{-1} = U_{\sigma(a)}$.

*Proof.* Bijectivity is $\sigma^2 = \mathrm{id}$. The restriction is $\sigma(\lambda\cdot1) = \varsigma(\lambda)\cdot1$. Powers are preserved by multiplicativity and additivity. For the quadratic representation, $\sigma(a\circ(b\circ x)) = \sigma(a)\circ(\sigma(b)\circ\sigma(x))$ and the defining formula $U_{a,b} = L_aL_b+L_bL_a-L_{a\circ b}$ is carried to its analogue at $\sigma(a),\sigma(b)$. $\square$

**Corollary.** The map $\sigma$ is an automorphism of the Jordan algebra $J$ in the $\varsigma$-semilinear sense; in the linear case it is an involutive automorphism and the fixed set is a Jordan subalgebra, by *Involutive Linear Algebras*; in the conjugate-linear case the fixed set is only a linear space over the fixed field and needs the decomposition below.

## The Self-Adjoint Part

### The Fixed and the Skew Elements

**Definition.** The **self-adjoint part** of $(J,\sigma)$ is the fixed set

$$
H(J) = \{x \in J : \sigma(x) = x\},
$$

its elements are the **self-adjoint** (or **Hermitian**) elements, and an element with $\sigma(x) = -x$ is **skew**. The skew elements are written $S(J)$.

**Proposition.** If $\sigma$ is linear, $H(J)$ and $S(J)$ are $F$-subspaces of $J$ and $J = H(J)\oplus S(J)$ when $2 \neq 0$. If $\sigma$ is $\varsigma$-semilinear and nontrivial, $H(J)$ and $S(J)$ are linear spaces over the fixed field $F^\varsigma$, and $J = H(J)\oplus S(J)$ as $F^\varsigma$-linear spaces still; $H(J)$ is not an $F$-subspace, and $\lambda H(J)\subseteq H(J)$ only for $\lambda \in F^\varsigma$.

*Proof.* The additive decomposition $x = \tfrac12(x+\sigma(x)) + \tfrac12(x-\sigma(x))$ is additive and $F^\varsigma$-linear; it is $F$-linear when $\varsigma = \mathrm{id}$. The scalar behaviour follows from $\sigma(\lambda x) = \varsigma(\lambda)\sigma(x)$. $\square$

### The Decomposition by a Quadratic Extension

**Theorem.** Let $K/F$ be a quadratic extension with nontrivial automorphism $\varsigma$, and let $(J,\sigma)$ be a $K$-Jordan algebra with a $\varsigma$-semilinear involution. Then

$$
J = H(J) \oplus i\,H(J) ,
$$

where $i \in K$ satisfies $\varsigma(i) = -i$ and $K = F\oplus Fi$; the sum is direct and is a decomposition of $J$ into two copies of the $F$-Jordan algebra $H(J)$.

*Proof.* For $x \in J$ put $h_1 = \tfrac12(x+\sigma(x))$ and $h_2 = \tfrac{1}{2i}(x-\sigma(x))$. Then $\sigma(h_1) = \tfrac12(\sigma(x)+x) = h_1$ and $\sigma(h_2) = \tfrac{1}{2\varsigma(i)}(\sigma(x)-x) = \tfrac{-1}{-2i}(\sigma(x)-x) = \tfrac{1}{2i}(x-\sigma(x)) = h_2$, so both lie in $H(J)$, and $x = h_1+ih_2$. If $h_1 + ih_2 = 0$ with $h_i \in H(J)$, applying $\sigma$ gives $h_1 - ih_2 = 0$, whence $2h_1 = 0$ and $2ih_2 = 0$, so $h_1 = h_2 = 0$ when $2 \neq 0$. $\square$

**Corollary.** In the conjugate-linear case the fixed set is a **real form** of $J$ in the sense of the extension of scalars: $J \cong H(J)\otimes_F K$, and $\sigma$ is the map $\mathrm{id}\otimes\varsigma$. The passage from a complex Jordan algebra with conjugate-linear involution to its self-adjoint part is the **descent**, and it is the subject of *Real Forms and the Descent of an Algebra*.

### The Self-Adjoint Part is a Jordan Subalgebra

**Theorem.** $H(J)$ is closed under the Jordan product, so it is a Jordan subalgebra of $J$ over the fixed field.

*Proof.* If $\sigma(x) = x$ and $\sigma(y) = y$ then $\sigma(x\circ y) = \sigma(x)\circ\sigma(y) = x\circ y$. $\square$

**Corollary.** The self-adjoint part is the Jordan algebra of the fixed points, and in the linear case it is exactly the fixed subalgebra of the involutive automorphism $\sigma$. The quadratic representation of $H(J)$ is the restriction of that of $J$, because $U_{x,y}$ for self-adjoint $x,y$ is self-adjoint as an operator: $U_{x,y}$ commutes with $\sigma$ by the proposition above.

## Formal Reality of the Involution

**Definition.** The involution $\sigma$ is **formally real** when a finite sum of squares of self-adjoint elements vanishes only trivially:

$$
\sum_{i=1}^n h_i\circ h_i = 0, \qquad h_i \in H(J) \ \Longrightarrow \ h_1 = \cdots = h_n = 0 .
$$

**Theorem.** A linear involution $\sigma$ of a formally real Jordan algebra $J$ is formally real, and the condition is equivalent to the statement that $-1$ is not a sum of squares in $H(J)$.

*Proof.* If $J$ is formally real as a Jordan algebra, a sum of squares $\sum h_i^2 = 0$ with $h_i \in J$ forces each $h_i = 0$, hence in particular for $h_i \in H(J)$; conversely the displayed condition applied with $h_i$ self-adjoint and $-1 = \sum h_i^2$ gives the second form, since then $\sum h_i^2 + 1 = 0$ is a nontrivial sum of squares. $\square$

**Remark.** Formal reality is a condition on the Jordan algebra of self-adjoint elements, and the order it carries, the existence of the square roots and the Sylvester law are the subject of *Formally Real Algebras and the Sum of Squares*, later in this group; the article records only the condition and its equivalence with the non-vanishing of the sum of squares.

## The Realisation as a Symmetrisation

### An Associative Algebra with Involution

Let $A$ be an associative unital $F$-algebra with an involution $\ast$ in the sense of *Involutive Linear Algebras*, with self-adjoint part $H(A,\ast) = \{a : a^* = a\}$. The special Jordan algebra $J = A^+$ has the halved product $x\circ y = \tfrac12(xy+yx)$ of *Jordan Algebras*.

**Theorem.** The map $\sigma = \ast$ restricted to $J = A^+$ is a linear involution of the Jordan algebra $J$, and

$$
H(J) = H(A,\ast) ,
$$

the self-adjoint part of $J$ being exactly the set of the $\ast$-self-adjoint elements of $A$; the self-adjoint part is a Jordan subalgebra of $A^+$.

*Proof.* $\ast$ is an anti-automorphism of $A$ with $\ast^2 = \mathrm{id}$, so $\sigma(x\circ y) = \tfrac12((xy+yx))^* = \tfrac12(y^*x^*+x^*y^*) = \tfrac12(x^*y^*+y^*x^*) = \sigma(x)\circ\sigma(y)$ by the commutativity of the symmetrised product; and $\sigma^2 = \mathrm{id}$. The fixed set is the $\ast$-self-adjoint part by definition, and it is closed under $\circ$ by the theorem of the previous section. $\square$

**Theorem (realisation).** Every special Jordan algebra with involution $J\subseteq A^+$ for an associative algebra $A$ arises from an involution of $A$ when $A$ is generated by $J$ and $J$ is the self-adjoint part of a $\ast$-algebra: the involution $\ast$ of $A$ restricting to $\sigma$ on $J$ is an **associative envelope** of the involution, and it is unique when $A$ is the universal envelope of $J$.

*Proof.* The involution $\sigma$ of $J$ extends to the associative algebra generated by $J$ by the universal property of the free algebra and the anti-multiplicativity of $\ast$ on the generators; the extension is an involution because it preserves the relations $\sigma^2 = \mathrm{id}$ and the multiplication on the generators. $\square$

### Examples

**Example (the matrix algebra).** For $A = M_n(\mathbb{C})$ with the conjugate transpose $\ast$, the special Jordan algebra $J = A^+$ is the Jordan algebra of the complex matrices under $x\circ y = \tfrac12(xy+yx)$, and $H(J) = H_n(\mathbb{C})$ is the real Jordan algebra of the Hermitian matrices, closed under the symmetrised product. The conjugate-linear involution is the conjugate transpose, whose fixed set is the Hermitian part, and the decomposition $M_n(\mathbb{C}) = H_n(\mathbb{C})\oplus iH_n(\mathbb{C})$ is the decomposition of a matrix into its Hermitian and skew-Hermitian parts.

**Example (the spin factor).** Let $J = F\oplus V$ be the spin factor of *Jordan Algebras* with the product $(\alpha,v)\circ(\beta,w) = (\alpha\beta+B(v,w),\alpha w+\beta v)$, and let $\varsigma$ be an involution of $F$ with a compatible $\varsigma$-semilinear map on $V$ preserving $B$ in the sense $B(\sigma v,\sigma w) = \varsigma(B(v,w))$. Then $(\alpha,v)\mapsto(\varsigma(\alpha),\sigma(v))$ is a $\varsigma$-semilinear involution of $J$, and its self-adjoint part is the spin factor of the fixed field with the fixed part of $V$.

## Summary

A **Jordan algebra with an involution** is a Jordan $F$-algebra $J$ with a $\varsigma$-semilinear map $\sigma$ of order two preserving the Jordan product; since the product is commutative, the involution and the involutive automorphism coincide as product-relevant maps, and the only distinction is linear versus conjugate-linear. The **self-adjoint part** $H(J)$ is a Jordan subalgebra over the fixed field, the skew elements are $S(J)$, and $J = H(J)\oplus S(J)$ always, with $J = H(J)\oplus iH(J)$ over a quadratic extension $K/F$. The involution is **formally real** when no nontrivial sum of squares of self-adjoint elements vanishes, equivalently when $-1$ is not a sum of squares in $H(J)$; the order theory of this condition is *Formally Real Algebras and the Sum of Squares*. Every **associative $\ast$-algebra** $A$ gives a special Jordan algebra with involution, $J = A^+$ with $\sigma = \ast$, and $H(J) = H(A,\ast)$; conversely a special Jordan algebra with involution is realised by an associative envelope, which is unique for the universal envelope. The matrix algebra with the conjugate transpose and the Hermitian matrices are the standard example, and the complex case is the decomposition into Hermitian and skew-Hermitian parts. No form, norm, distance or order occurs in this article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | Field of scalars |
| $\varsigma$ | Involution of $F$; $\varsigma=\mathrm{id}$ in the linear case |
| $K/F$ | Quadratic extension, $K = F\oplus Fi$, $\varsigma(i) = -i$ |
| $J$ | Unital Jordan $F$-algebra |
| $\sigma$ | $\varsigma$-semilinear involution preserving $\circ$ |
| $H(J)$ | Self-adjoint (Hermitian) part, the fixed set |
| $S(J)$ | Skew elements, $\sigma(x) = -x$ |
| $J = H(J)\oplus S(J)$ | Additive decomposition |
| $J = H(J)\oplus iH(J)$ | Decomposition over a quadratic extension |
| $\sigma(a\circ b) = \sigma(a)\circ\sigma(b)$ | Preservation of the Jordan product |
| $F^\varsigma$ | Fixed field of the involution of the scalars |
| $\sum h_i^2 = 0 \Rightarrow h_i = 0$ | Formal reality of the involution |
| $A, \ast$ | Associative algebra with involution |
| $J = A^+$, $\sigma = \ast$, $H(J) = H(A,\ast)$ | Realisation as a symmetrisation |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for Jordan algebras with involution, the self-adjoint part and formal reality.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the symmetrisation of an associative $\ast$-algebra and the Hermitian part.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for involutions of an algebra, the two kinds and the descent by a quadratic extension.
- Ottmar Loos, *Symmetric Spaces I: General Theory* (Benjamin, 1969), for the self-adjoint part, the quadratic representation and the structure group of a Jordan algebra with involution.
- Hel Braun and Max Koecher, *The Jordan Algebra Approach to Bounded Symmetric Domains* (Springer, 1966), for the formally real Jordan algebras, the self-adjoint part and the order it carries.
