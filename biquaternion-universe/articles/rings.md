

# __Rings: A General Introduction__

## Introduction

This article introduces the theory of rings, the algebraic structures that generalize the number systems we use every day. Rings are the natural setting for addition and multiplication, and they include the integers, the rational numbers, the real numbers, the complex numbers, and many other structures.

The treatment is introductory and purely mathematical. We assume familiarity with sets, functions, and basic algebraic operations.

We begin with the definition of a ring, then introduce the most important classes of rings: commutative rings, integral domains, fields, and division rings. We state the basic properties that will be used in the study of modules, algebras, and Clifford algebras.

---

# Part I: Rings

## 1. Definition of a Ring

A **ring** is a set $R$ equipped with two binary operations, **addition** $+$ and **multiplication** $\cdot$, satisfying the following axioms.

**(R1) Addition is an abelian group.** The pair $(R, +)$ is an abelian group. That is:

- **Associativity.** $(a + b) + c = a + (b + c)$ for all $a, b, c \in R$.
- **Commutativity.** $a + b = b + a$ for all $a, b \in R$.
- **Identity.** There is an element $0 \in R$ such that $a + 0 = a$ for all $a \in R$.
- **Inverses.** For every $a \in R$, there is an element $-a \in R$ such that $a + (-a) = 0$.

**(R2) Multiplication is associative.** $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ for all $a, b, c \in R$.

**(R3) Multiplication distributes over addition.**

$$
a \cdot (b + c) = a \cdot b + a \cdot c, \qquad (a + b) \cdot c = a \cdot c + b \cdot c
$$

for all $a, b, c \in R$.

A ring is **unital** if it has a multiplicative identity $1 \in R$ such that

$$
1 \cdot a = a \cdot 1 = a
$$

for all $a \in R$. In this article, all rings are assumed to be unital, unless stated otherwise.

A ring is **commutative** if

$$
a \cdot b = b \cdot a
$$

for all $a, b \in R$.

A ring is **associative** if multiplication is associative, as in (R2). All rings in this article are associative.

## 2. Elementary Properties

Let $R$ be a ring. The following properties follow from the axioms.

**(a) Uniqueness of identity.** The additive identity $0$ is unique. The multiplicative identity $1$ is unique, if it exists.

**(b) Uniqueness of inverses.** For each $a \in R$, the additive inverse $-a$ is unique.

**(c) Multiplication by zero.** For all $a \in R$,

$$
a \cdot 0 = 0 \cdot a = 0.
$$

**(d) Sign rules.** For all $a, b \in R$,

$$
(-a) \cdot b = a \cdot (-b) = -(a \cdot b), \qquad (-a) \cdot (-b) = a \cdot b.
$$

**(e) The identity and zero.** If $R$ is unital and $1 = 0$, then $R = \{0\}$. This is the **zero ring**, the only ring in which the multiplicative identity equals the additive identity.

## 3. Subrings

A subset $S \subseteq R$ of a ring $R$ is a **subring** if:

**(S1)** $S$ is a subgroup of $(R, +)$: for all $a, b \in S$, $a - b \in S$.

**(S2)** $S$ is closed under multiplication: for all $a, b \in S$, $a b \in S$.

**(S3)** $S$ contains the multiplicative identity $1$ of $R$.

A subring is itself a ring under the inherited operations.

## 4. Ring Homomorphisms

Let $R$ and $S$ be rings. A **ring homomorphism** is a function

$$
\varphi : R \to S
$$

such that for all $a, b \in R$:

**(H1)** $\varphi(a + b) = \varphi(a) + \varphi(b)$.

**(H2)** $\varphi(a b) = \varphi(a) \varphi(b)$.

**(H3)** $\varphi(1_R) = 1_S$.

A ring homomorphism that is bijective is a **ring isomorphism**. If there is a ring isomorphism $R \to S$, we write $R \cong S$ and say that $R$ and $S$ are **isomorphic**.

The **kernel** of a ring homomorphism $\varphi : R \to S$ is

$$
\ker \varphi = \{a \in R : \varphi(a) = 0\}.
$$

The **image** of $\varphi$ is

$$
\operatorname{im} \varphi = \{\varphi(a) : a \in R\}.
$$

The kernel is an ideal of $R$, and the image is a subring of $S$.

---

# Part II: Commutative Rings

## 5. Definition of a Commutative Ring

A **commutative ring** is a ring $R$ in which multiplication is commutative:

$$
a \cdot b = b \cdot a
$$

for all $a, b \in R$.

Commutative rings are the most important class of rings for algebraic geometry, number theory, and the theory of quadratic forms and Clifford algebras.

## 6. Ideals

A subset $I \subseteq R$ of a commutative ring $R$ is an **ideal** if:

**(I1)** $I$ is a subgroup of $(R, +)$: for all $a, b \in I$, $a - b \in I$.

**(I2)** $I$ is closed under multiplication by elements of $R$: for all $r \in R$ and $a \in I$, $r a \in I$.

An ideal $I$ is **proper** if $I \neq R$. It is **maximal** if it is proper and there is no ideal strictly between $I$ and $R$. It is **prime** if for all $a, b \in R$,

$$
a b \in I \implies a \in I \text{ or } b \in I.
$$

## 7. Quotient Rings

Let $R$ be a commutative ring and $I$ an ideal. The **quotient ring** $R/I$ is the set of cosets

$$
R/I = \{r + I : r \in R\}
$$

with addition and multiplication defined by

$$
(r + I) + (s + I) = (r + s) + I, \qquad (r + I)(s + I) = rs + I.
$$

These operations are well-defined, and $R/I$ is a commutative ring with identity $1 + I$.

The **first isomorphism theorem** states that if $\varphi : R \to S$ is a ring homomorphism, then

$$
R / \ker \varphi \cong \operatorname{im} \varphi.
$$

## 8. Zero Divisors

An element $a \in R$ is a **zero divisor** if there exists a nonzero $b \in R$ such that

$$
a b = 0.
$$

A commutative ring $R$ is an **integral domain** if it has no zero divisors and $1 \neq 0$. That is, for all $a, b \in R$,

$$
a b = 0 \implies a = 0 \text{ or } b = 0.
$$

## 9. Units

An element $a \in R$ is a **unit** if there exists $b \in R$ such that

$$
a b = b a = 1.
$$

The set of units of $R$ is denoted $R^\times$. It is a group under multiplication.

## 10. Fields

A **field** is a commutative ring $F$ in which every nonzero element is a unit. That is, for every $a \in F$ with $a \neq 0$, there exists $b \in F$ such that

$$
a b = 1.
$$

Equivalently, a field is a commutative ring with $1 \neq 0$ in which every nonzero element has a multiplicative inverse.

## 11. Properties of Fields

Fields have many special properties that make them the natural setting for linear algebra and the theory of quadratic forms.

**(a) No zero divisors.** Every field is an integral domain.

**(b) Cancellation.** If $a b = a c$ and $a \neq 0$, then $b = c$.

**(c) Every nonzero element is a unit.** This is the defining property.

**(d) The only ideals are $0$ and $F$.** A field has no proper nonzero ideals.

**(e) Every module is free.** Every vector space over a field has a basis. This is the key property that makes linear algebra work.

**(f) Every finitely generated module is free.** Over a field, every finitely generated module is a finite-dimensional vector space.

**(g) The classification of quadratic forms is clean.** Over a field, quadratic forms are classified by their rank and signature (over $\mathbb{R}$) or by arithmetic invariants (over $\mathbb{Q}$).

## 12. Integral Domains

An **integral domain** is a commutative ring $R$ with $1 \neq 0$ and no zero divisors.

Integral domains are intermediate between general commutative rings and fields. Every field is an integral domain, but not every integral domain is a field.

In an integral domain, cancellation holds: if $a b = a c$ and $a \neq 0$, then $b = c$. This is because $a(b - c) = 0$ and $a \neq 0$, so $b - c = 0$.

## 13. Division Rings

A **division ring** (or **skew field**) is a ring $R$ with $1 \neq 0$ in which every nonzero element is a unit. Unlike a field, a division ring need not be commutative.

By **Wedderburn's little theorem**, every finite division ring is a field.

---

# Part III: Modules over Rings

## 14. Definition of a Module

Let $R$ be a commutative ring. An **$R$-module** is an abelian group $(M, +)$ equipped with a scalar multiplication

$$
R \times M \to M, \qquad (r, m) \mapsto r m,
$$

satisfying the following axioms for all $r, s \in R$ and $m, n \in M$:

**(M1)** $r(m + n) = r m + r n$.

**(M2)** $(r + s)m = r m + s m$.

**(M3)** $(r s)m = r(s m)$.

**(M4)** $1 m = m$.

If $R$ is a field, an $R$-module is exactly a **vector space** over $R$. So modules generalize vector spaces to arbitrary commutative rings.

## 15. Free Modules

An $R$-module $M$ is **free** if it has a basis: a subset $\{e_i\}_{i \in I}$ such that every element of $M$ can be written uniquely as a finite linear combination

$$
m = \sum_{i \in I} r_i e_i
$$

with $r_i \in R$.

Not every module is free. Over a general commutative ring, modules can be more complicated than vector spaces.

## 16. Algebras over Rings

Let $R$ be a commutative ring. An **$R$-algebra** is an $R$-module $A$ equipped with a bilinear multiplication

$$
A \times A \to A, \qquad (a, b) \mapsto a b,
$$

satisfying the following axioms for all $r \in R$ and $a, b, c \in A$:

**(A1)** $r(a b) = (r a) b = a(r b)$.

**(A2)** $(a + b)c = a c + b c$ and $a(b + c) = a b + a c$.

If the multiplication is associative, $A$ is an **associative $R$-algebra**. If it is commutative, $A$ is a **commutative $R$-algebra**. If there is an identity element $1_A$, $A$ is **unital**.

---

# Part IV: Special Classes of Rings

## 17. Principal Ideal Domains

A **principal ideal domain** (PID) is an integral domain $R$ in which every ideal is principal: every ideal $I \subseteq R$ is of the form

$$
I = (a) = \{r a : r \in R\}
$$

for some $a \in R$.

## 18. Unique Factorization Domains

A **unique factorization domain** (UFD) is an integral domain $R$ in which every nonzero non-unit element can be written uniquely as a product of irreducible elements, up to order and multiplication by units.

## 19. Euclidean Domains

A **Euclidean domain** is an integral domain $R$ equipped with a function

$$
N : R \setminus \{0\} \to \mathbb{N}
$$

such that for all $a, b \in R$ with $b \neq 0$, there exist $q, r \in R$ with

$$
a = q b + r, \qquad r = 0 \text{ or } N(r) < N(b).
$$

The chain of inclusions is:

$$
\text{Euclidean domains} \subset \text{PIDs} \subset \text{UFDs} \subset \text{integral domains} \subset \text{commutative rings}.
$$

---

# Part V: Summary

## 20. Summary of Ring Classes

| Class | Commutative | Unital | No zero divisors | Every nonzero element is a unit |
|---|---|---|---|---|
| Ring | no | yes | no | no |
| Commutative ring | yes | yes | no | no |
| Integral domain | yes | yes | yes | no |
| Field | yes | yes | yes | yes |
| Division ring | no | yes | yes | yes |

## 21. The Role of Fields

Fields are the most important class of rings for the theory of quadratic forms and Clifford algebras, because:

1. Every module over a field is free, so every algebra has a well-defined dimension.
2. Every nonzero element is a unit, so division algebras are possible.
3. The classification of quadratic forms is clean and well-understood.
4. The classical theorems (Frobenius, Wedderburn) apply.

But fields are not the only setting. Commutative rings, integral domains, and division rings all play important roles in various areas of mathematics.

## 22. The Role of Commutative Rings

Commutative rings are the natural setting for:

1. **Algebraic geometry.** The ring of functions on an algebraic variety is a commutative ring.
2. **Number theory.** The ring of integers of a number field is a commutative ring.
3. **The theory of quadratic forms over rings.** Clifford algebras can be defined over any commutative ring.
4. **The theory of modules.** Modules over commutative rings generalize vector spaces.

The split complex numbers $\mathbb{D}$ are a commutative ring with zero divisors. They are not a field, but they are a perfectly good setting for the theory of quadratic forms and Clifford algebras, provided one uses the commutative-ring framework.

---

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991).
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002).
- I. N. Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975).
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003).
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009).
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004).
- Thomas W. Hungerford, *Algebra* (Springer, 1974).

