
# __Algebras: A General Introduction__

## Introduction

This article introduces algebras as mathematical structures. The treatment is introductory and purely mathematical. The goal is to explain what an algebra is, how it relates to the more familiar notion of a module, and what additional properties an algebra may or may not have.

This article treats the general theory over a **commutative ring**. A separate article, *Algebras: Categorization*, gives a classification organized by ring.

A note on terminology. The word "algebra" is used in this article in the **broad sense**: a module over a commutative ring $R$ equipped with a bilinear product, with no further assumptions. In this sense, an algebra need not be associative, need not be commutative, and need not have a unit. When we want to insist on associativity, we say **associative algebra**. The word "algebra" without qualification always means the broad sense.

Some authors use the word "algebra" in the **narrow sense**, meaning an associative algebra. This is a common convention, but it is not the one we adopt here. The reason is that some of the most important algebras in mathematics — Lie algebras, Jordan algebras, and the cross product algebra on $\mathbb{R}^3$ — are not associative, and it would be awkward to have to say "non-associative algebra" every time we want to mention them.

A word on the base structure. The classical theory of algebras assumes that the scalars form a field. But many of the constructions and theorems carry over to the more general setting where the scalars form a **commutative ring**. This is the setting we adopt here. The main differences from the field case are:

- Modules over a commutative ring need not be free, whereas vector spaces over a field always are.
- Invertibility of a linear transformation requires the determinant to be a **unit** of the ring, not merely nonzero.
- Zero divisors may exist in the ring, and consequently in the algebra.

We indicate where these differences matter.

---

## Part I: Modules over a Commutative Ring

### The Idea

Before we can say what an algebra is, we need to say what a module is. A **module** over a commutative ring $R$ is a set of objects — called **vectors** — that can be added together and multiplied by scalars from $R$, subject to certain rules.

When $R$ is a field, a module over $R$ is exactly a **vector space** over $R$. So modules generalize vector spaces to arbitrary commutative rings.

### The Definition

Let $R$ be a commutative ring with identity. An **$R$-module** is a set $M$ equipped with two operations:

1. **Addition:** a rule that assigns to any two vectors $u, v \in M$ a vector $u + v \in M$.
2. **Scalar multiplication:** a rule that assigns to any scalar $r \in R$ and any vector $v \in M$ a vector $r v \in M$.

These operations must satisfy the following axioms:

**Axioms for addition:**

- **Associativity:** $(u + v) + w = u + (v + w)$ for all $u, v, w \in M$.
- **Commutativity:** $u + v = v + u$ for all $u, v \in M$.
- **Identity element:** there exists a vector $0 \in M$ such that $0 + v = v$ for all $v \in M$.
- **Inverse elements:** for every $v \in M$ there exists a vector $-v \in M$ such that $v + (-v) = 0$.

**Axioms for scalar multiplication:**

- **Compatibility with ring multiplication:** $r(s v) = (r s) v$ for all $r, s \in R$ and $v \in M$.
- **Identity element:** $1 v = v$ for all $v \in M$, where $1$ is the multiplicative identity of $R$.

**Distributivity axioms:**

- **Distributivity over vector addition:** $r(u + v) = r u + r v$ for all $r \in R$ and $u, v \in M$.
- **Distributivity over scalar addition:** $(r + s)v = r v + s v$ for all $r, s \in R$ and $v \in M$.

These are the axioms. Everything else follows from them.

### Free Modules and Bases

A **basis** of an $R$-module $M$ is a set of vectors $\{e_1, e_2, \ldots\}$ such that:

1. **Spanning:** every vector in $M$ can be written as a linear combination of the basis vectors with coefficients in $R$.
2. **Linear independence:** no basis vector can be written as a linear combination of the others.

An $R$-module is **free** if it has a basis. If $M$ has a finite basis $\{e_1, \ldots, e_n\}$ over $R$, then every vector $v \in M$ can be written uniquely as

$$
v = r_1 e_1 + r_2 e_2 + \cdots + r_n e_n
$$

where $r_1, \ldots, r_n \in R$ are the **coordinates** of $v$ with respect to the basis. In this case, $M \cong R^n$, and we say that $M$ has **rank** $n$.

**Key difference from the field case.** Over a field, every module is free. Over a general commutative ring, this is false. For example, $\mathbb{Z}/n\mathbb{Z}$ is a $\mathbb{Z}$-module that is not free for $n \geq 2$. So the notion of a basis is not as universal as it is over a field.

The rank depends on the ring. The same underlying set can have different ranks over different rings. For example, $\mathbb{C}$ has rank 2 over $\mathbb{R}$ and rank 1 over $\mathbb{C}$.

---

## Part II: What Is an Algebra?

### The Idea

A module allows us to add vectors and multiply them by scalars. But it does not allow us to multiply two vectors together. An **algebra** is a module equipped with a product — a rule for multiplying two vectors to get a third vector.

The product is required to be **bilinear**, meaning it is linear in each argument separately. This is the minimum requirement. Beyond bilinearity, an algebra may or may not satisfy further properties.

### The Definition

Let $R$ be a commutative ring. An **algebra over $R$** is an $R$-module $A$ equipped with a **product** — a rule that assigns to any two vectors $u, v \in A$ a vector $uv \in A$ — satisfying the following axioms:

**Bilinearity:**

- **Left distributivity:** $(u + v)w = uw + vw$ for all $u, v, w \in A$.
- **Right distributivity:** $u(v + w) = uv + uw$ for all $u, v, w \in A$.
- **Left compatibility with scalars:** $(r u)v = r(uv)$ for all $r \in R$ and $u, v \in A$.
- **Right compatibility with scalars:** $u(r v) = r(uv)$ for all $r \in R$ and $u, v \in A$.

These four axioms are equivalent to the single statement that the product is **bilinear**: linear in each argument separately.

This is the minimum requirement. An algebra need not be associative, need not be commutative, need not have a unit, and need not have inverses. Those are additional properties that an algebra may or may not have.

### Additional Properties

Beyond bilinearity, an algebra may satisfy any of the following properties:

**Associativity.** The product is associative if

$$
(uv)w = u(vw)
$$

for all $u, v, w \in A$.

**Commutativity.** The product is commutative if

$$
uv = vu
$$

for all $u, v \in A$.

**Existence of a unit.** The algebra has a unit if there exists an element $1 \in A$ such that

$$
1v = v1 = v
$$

for all $v \in A$.

**Existence of inverses.** An element $v \in A$ has an inverse if there exists an element $v^{-1} \in A$ such that

$$
vv^{-1} = v^{-1}v = 1
$$

where $1$ is the unit of the algebra. An algebra in which every nonzero element has an inverse is called a **division algebra**.

**Key difference from the field case.** Over a field, a division algebra requires every nonzero element to be invertible. Over a commutative ring with zero divisors, this is impossible for any algebra of rank greater than 1, because the zero divisors of $R$ become zero divisors in the algebra. So the notion of a division algebra is most useful when $R$ is at least an integral domain, and the classical theorems (Frobenius, Wedderburn) require $R$ to be a field.

### Replacing Associativity

Associativity is not the only possible identity that a bilinear product can satisfy. There are other identities, and algebras satisfying them are studied in their own right. The most important is the **Jacobi identity**.

A bilinear product $[\cdot, \cdot]$ is **antisymmetric** if

$$
[u, v] = -[v, u]
$$

for all $u, v \in A$. It satisfies the **Jacobi identity** if

$$
[u, [v, w]] + [v, [w, u]] + [w, [u, v]] = 0
$$

for all $u, v, w \in A$. An algebra over a commutative ring $R$ equipped with an antisymmetric product satisfying the Jacobi identity is called a **Lie algebra**. The product is called the **Lie bracket**.

The Jacobi identity is the replacement for associativity. It says that the failure of the bracket to be associative is controlled: the three nested brackets sum to zero. This is the precise sense in which the identity substitutes for associativity.

Lie algebras are not associative in general. The cross product on $\mathbb{R}^3$ is the simplest example: it is antisymmetric and satisfies the Jacobi identity, but it is not associative.

Another important identity is the **Jordan identity**:

$$
u(v(uu)) = (uv)(uu).
$$

An algebra over a commutative ring $R$ equipped with a commutative product satisfying the Jordan identity is called a **Jordan algebra**. Jordan algebras arise in the study of observables in quantum mechanics. They are not associative in general.

### The Hierarchy of Algebraic Structures

Let me lay out the hierarchy of algebraic structures over a fixed commutative ring $R$, from weakest to strongest:

1. **Module over $R$.** A set with addition and scalar multiplication, satisfying the module axioms. No product of vectors.
2. **Algebra over $R$.** A module over $R$ with a bilinear product. No further requirements.
3. **Associative algebra over $R$.** An algebra with associative product.
4. **Unital algebra over $R$.** An associative algebra with a unit element $1$.
5. **Division algebra over $R$.** A unital associative algebra in which every nonzero element has a multiplicative inverse. May or may not be commutative. Requires $R$ to be at least an integral domain.
6. **Field extension of $F$.** When $R = F$ is a field, a commutative division algebra over $F$. Equivalently, a commutative unital associative algebra over $F$ in which every nonzero element is invertible.

So, over a field $F$:

$$
\text{field} \subset \text{division algebra} \subset \text{unital associative algebra} \subset \text{associative algebra} \subset \text{algebra} \subset \text{vector space}.
$$

The inclusions are strict. For example:

- The algebra $\mathbb{R}^3$ with the cross product is an algebra over $\mathbb{R}$ that is not associative.
- The algebra $M_2(\mathbb{R})$ of $2 \times 2$ real matrices is a unital associative algebra over $\mathbb{R}$ that is not a division algebra.
- The quaternions $\mathbb{H}$ over $\mathbb{R}$ form a division algebra over $\mathbb{R}$ that is not a field.
- The real numbers $\mathbb{R}$ are a field that is infinite-dimensional over its prime field $\mathbb{Q}$.

Over a commutative ring $R$, the hierarchy is:

$$
\text{algebra over } R \supset \text{associative algebra over } R \supset \text{unital algebra over } R.
$$

The notion of a division algebra over $R$ is only meaningful when $R$ is an integral domain, and the classical theory requires $R$ to be a field.

---

## Part III: Properties of Algebras

### Associativity

An algebra over a commutative ring $R$ is **associative** if

$$
(uv)w = u(vw)
$$

for all $u, v, w \in A$. Associativity allows us to write products of three or more elements without parentheses.

Most algebras of interest in mathematics and physics are associative. The cross product algebra $\mathbb{R}^3$ is a notable exception.

### Commutativity

An algebra over a commutative ring $R$ is **commutative** if

$$
uv = vu
$$

for all $u, v \in A$. Commutativity is a strong condition.

### The Center

The **center** of an algebra $A$ over a commutative ring $R$ is the set of elements that commute with every element of $A$:

$$
Z(A) = \{z \in A : zv = vz \text{ for all } v \in A\}.
$$

The center is always a commutative subalgebra of $A$ over $R$.

### Units and Zero Divisors

A **unit** in an algebra $A$ over a commutative ring $R$ is an element $u$ that has a multiplicative inverse: there exists $u^{-1} \in A$ such that $uu^{-1} = u^{-1}u = 1$. The set of all units in $A$ forms a group under multiplication, called the **group of units** of $A$.

A **zero divisor** in an algebra $A$ over a commutative ring $R$ is a nonzero element $z$ such that there exists a nonzero element $w$ with $zw = 0$ or $wz = 0$. An algebra with no zero divisors is called a **domain**.

**Key difference from the field case.** Over a field, an algebra may or may not have zero divisors. Over a commutative ring with zero divisors, the zero divisors of the ring automatically become zero divisors in the algebra. For example, over $\mathbb{D}$, the element $(1 + e) \cdot 1$ is a zero divisor in any $\mathbb{D}$-algebra.

### Ideals

An **ideal** in an algebra $A$ over a commutative ring $R$ is a submodule $I \subseteq A$ such that for all $a \in A$ and $x \in I$, both $ax \in I$ and $xa \in I$. Ideals are precisely the submodules by which one can quotient.

### Homomorphisms

An **algebra homomorphism** from an algebra $A$ over a commutative ring $R$ to an algebra $B$ over the same ring $R$ is an $R$-linear map $\varphi: A \to B$ that preserves the product:

$$
\varphi(uv) = \varphi(u)\varphi(v)
$$

for all $u, v \in A$. An **isomorphism** is a bijective homomorphism.

---

## Part IV: Constructions on Algebras

### Direct Sums

Let $A$ and $B$ be algebras over the same commutative ring $R$. The **direct sum** $A \oplus B$ is the algebra over $R$ whose underlying module is the direct sum of the modules $A$ and $B$, with product defined componentwise:

$$
(a_1, b_1)(a_2, b_2) = (a_1 a_2, b_1 b_2).
$$

If $A$ and $B$ are free of ranks $m$ and $n$, then $A \oplus B$ is free of rank $m + n$.

### Tensor Products

Let $A$ and $B$ be algebras over the same commutative ring $R$. The **tensor product** $A \otimes_R B$ is the algebra over $R$ whose underlying module is the tensor product of the modules $A$ and $B$, with product defined on elementary tensors by

$$
(a_1 \otimes b_1)(a_2 \otimes b_2) = (a_1 a_2) \otimes (b_1 b_2)
$$

and extended bilinearly.

If $A$ and $B$ are free of ranks $m$ and $n$, then $A \otimes_R B$ is free of rank $mn$.

### Quotients

Let $A$ be an algebra over a commutative ring $R$ and let $I$ be a two-sided ideal of $A$. The **quotient algebra** $A/I$ is the set of cosets $\{a + I : a \in A\}$ with addition, scalar multiplication, and product defined by

$$
(a + I) + (b + I) = (a + b) + I,
$$

$$
r(a + I) = (r a) + I,
$$

$$
(a + I)(b + I) = (ab) + I.
$$

These operations are well-defined precisely because $I$ is an ideal.

### Base Change

Let $R \to S$ be a ring homomorphism, and let $A$ be an $R$-algebra. The **base change** of $A$ to $S$ is the $S$-algebra

$$
A \otimes_R S,
$$

with the natural $S$-module structure. This is a common construction: for example, complexifying a real algebra is base change along $\mathbb{R} \to \mathbb{C}$.

---

## Part V: Summary

Let me summarize the main points.

**A module over a commutative ring $R$** is a set of vectors that can be added and multiplied by scalars in $R$. When $R$ is a field, this is exactly a vector space.

**An algebra over a commutative ring $R$** is a module over $R$ equipped with a bilinear product. The product need not be associative, commutative, or unital.

**The ring matters.** The same underlying set can be a module or an algebra over different rings, and the structure depends on the choice of ring.

**Additional properties** that an algebra may have include associativity, commutativity, existence of a unit, and existence of inverses.

**The hierarchy of algebraic structures** over a field $F$ is:

$$
\text{field} \subset \text{division algebra} \subset \text{unital associative algebra} \subset \text{associative algebra} \subset \text{algebra} \subset \text{vector space}.
$$

Over a general commutative ring $R$, the hierarchy is shorter:

$$
\text{algebra over } R \supset \text{associative algebra over } R \supset \text{unital algebra over } R.
$$

The notion of a division algebra requires $R$ to be at least an integral domain, and the classical theory requires $R$ to be a field.

**Key differences from the field case.**

- Not every module is free, so not every algebra has a well-defined rank.
- Invertibility requires the determinant to be a unit of $R$, not merely nonzero.
- Zero divisors in $R$ become zero divisors in any $R$-algebra.
- Division algebras are only meaningful when $R$ is an integral domain.

**Constructions on algebras** include direct sums, tensor products, quotients, and base change.

The next article, *Algebras: Categorization*, gives a classification organized by ring.

---

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991).
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002).
- I. N. Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975).
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003).
- Nathan Jacobson, *Basic Algebra I* and *II* (Dover, 2nd ed. 2009).
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004).
- Thomas W. Hungerford, *Algebra* (Springer, 1974).


