
# __Rings categorization__

## Introduction

This article gives a classification of rings, organized by their structural properties. For each class of rings, we state the defining axioms, give concrete examples, and describe the position of the class in the hierarchy of ring-theoretic structures.

The general theory of rings is in the preceding article, *Rings: A General Introduction*. We assume familiarity with the definitions given there.

We classify rings by the following properties:

- Whether multiplication is **commutative**.
- Whether there is a **multiplicative identity**.
- Whether there are **zero divisors**.
- Whether every nonzero element is a **unit**.

We also classify rings by additional chain conditions and factorization properties: Euclidean domains, principal ideal domains, unique factorization domains, and integral domains.

Throughout this article, the standard examples are:

- $\mathbb{Z}$: the integers.
- $\mathbb{Q}$: the rational numbers.
- $\mathbb{R}$: the real numbers.
- $\mathbb{C}$: the complex numbers.
- $\mathbb{H}$: the quaternions.
- $\mathbb{D}$: the split complex numbers.
- $\mathbb{B} = \mathbb{H} \otimes \mathbb{C}$: the biquaternions.
- $\mathbb{Z}/n\mathbb{Z}$: the integers modulo $n$.
- $M_n(R)$: the ring of $n \times n$ matrices over a ring $R$.
- $R[x]$: the polynomial ring over a ring $R$.

---

# Part I: The Main Hierarchy

## 1. The Classification by Axioms

The most important classes of rings are defined by combinations of four properties:

**(P1) Commutativity.** $a b = b a$ for all $a, b \in R$.

**(P2) Unitality.** There is an element $1 \in R$ with $1 \neq 0$ such that $1 a = a 1 = a$ for all $a \in R$.

**(P3) No zero divisors.** $a b = 0 \implies a = 0$ or $b = 0$.

**(P4) Every nonzero element is a unit.** For every $a \neq 0$, there exists $b \in R$ with $a b = b a = 1$.

These four properties give the following table of ring classes.

| Class | (P1) Commutative | (P2) Unital | (P3) No zero divisors | (P4) All nonzero units |
|---|---|---|---|---|
| General ring | no | no | no | no |
| Unital ring | no | yes | no | no |
| Commutative ring | yes | yes | no | no |
| Integral domain | yes | yes | yes | no |
| Division ring | no | yes | yes | yes |
| Field | yes | yes | yes | yes |

The inclusions among these classes can be read off from the table. A field is both a division ring and an integral domain. It is the most restrictive class. A general ring is the least restrictive.

## 2. General Rings

A **general ring** satisfies only the axioms (R1), (R2), (R3) from the preceding article. It need not be commutative, need not be unital, may have zero divisors, and need not have inverses.

General rings are rarely studied in isolation. Most of the theory assumes at least unitality.

## 3. Unital Rings

A **unital ring** is a ring with a multiplicative identity $1 \neq 0$.

Unitality is the most basic assumption in modern ring theory. It allows the definition of modules, algebras, and homomorphisms in the standard way.

**Examples.**

- $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{D}$.
- $\mathbb{B} = \mathbb{H} \otimes \mathbb{C}$, the biquaternions.
- $\mathbb{Z}/n\mathbb{Z}$ for any $n \geq 1$.
- $M_n(R)$ for any unital ring $R$.
- $R[x]$ for any unital ring $R$.

## 4. Commutative Rings

A **commutative ring** is a unital ring in which multiplication is commutative.

Commutative rings are the natural setting for algebraic geometry, number theory, and the theory of quadratic forms and Clifford algebras. They need not be integral domains: they may have zero divisors.

**Examples.**

- $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$.
- $\mathbb{Z}/n\mathbb{Z}$ for any $n \geq 1$.
- $\mathbb{D}$, the split complex numbers.
- The dual numbers $\mathbb{R}[\epsilon]/(\epsilon^2)$.
- $R[x]$ for any commutative ring $R$.
- $R[x_1, \ldots, x_n]$ for any commutative ring $R$.

**Non-examples.**

- $\mathbb{H}$, the quaternions, because they are not commutative.
- $\mathbb{B} = \mathbb{H} \otimes \mathbb{C}$, the biquaternions, because they are not commutative.
- $M_n(R)$ for $n \geq 2$, because matrix multiplication is not commutative.

## 5. Integral Domains

An **integral domain** is a commutative ring with no zero divisors.

Integral domains are intermediate between commutative rings and fields. They satisfy the cancellation law: if $a b = a c$ and $a \neq 0$, then $b = c$.

**Examples.**

- $\mathbb{Z}$.
- $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$.
- $\mathbb{Z}/p\mathbb{Z}$ for any prime $p$.
- $\mathbb{Q}[\sqrt{2}]$, the quadratic extension of $\mathbb{Q}$.
- $R[x]$ for any integral domain $R$.
- Every field.

**Non-examples.**

- $\mathbb{Z}/6\mathbb{Z}$, because $2 \cdot 3 = 0$ with both factors nonzero.
- $\mathbb{D}$, because $(1 + e)(1 - e) = 0$.
- The dual numbers, because $\epsilon^2 = 0$ with $\epsilon \neq 0$.
- $\mathbb{B} = \mathbb{H} \otimes \mathbb{C}$, the biquaternions, because they have zero divisors.
- $M_n(R)$ for $n \geq 2$, because it has zero divisors.

## 6. Division Rings

A **division ring** (or **skew field**) is a unital ring in which every nonzero element is a unit.

Division rings need not be commutative. The quaternions $\mathbb{H}$ are the classical example of a non-commutative division ring.

By **Wedderburn's little theorem**, every finite division ring is a field. So non-commutative division rings must be infinite.

**Examples.**

- Every field: $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{Z}/p\mathbb{Z}$ for prime $p$.
- $\mathbb{H}$, the quaternions.

**Non-examples.**

- $\mathbb{Z}$, because $2$ has no inverse.
- $\mathbb{D}$, because $1 + e$ has no inverse.
- The dual numbers, because $\epsilon$ has no inverse.
- $\mathbb{B} = \mathbb{H} \otimes \mathbb{C}$, the biquaternions, because they have zero divisors.
- $M_n(R)$ for $n \geq 2$, because it has zero divisors.

## 7. Fields

A **field** is a commutative division ring. Equivalently, a field is a commutative ring with $1 \neq 0$ in which every nonzero element is a unit.

Fields are the most important class of rings for linear algebra and the theory of quadratic forms. Every module over a field is free, so every algebra over a field has a well-defined dimension.

**Examples.**

- $\mathbb{Q}$, the rational numbers.
- $\mathbb{R}$, the real numbers.
- $\mathbb{C}$, the complex numbers.
- $\mathbb{Z}/p\mathbb{Z}$ for any prime $p$.
- $\mathbb{Q}[\sqrt{2}]$, the quadratic extension of $\mathbb{Q}$.
- Any finite field $\mathbb{F}_q$ with $q = p^n$ elements.

**Non-examples.**

- $\mathbb{Z}$, because $2$ has no inverse.
- $\mathbb{D}$, because $1 + e$ has no inverse.
- The dual numbers, because $\epsilon$ has no inverse.
- $\mathbb{H}$, because it is not commutative.
- $\mathbb{B} = \mathbb{H} \otimes \mathbb{C}$, the biquaternions, because they are not commutative and have zero divisors.
- $M_n(R)$ for $n \geq 2$, because it has zero divisors.

---

# Part II: Chain Conditions and Factorization

## 8. Euclidean Domains

A **Euclidean domain** is an integral domain $R$ equipped with a function

$$
N : R \setminus \{0\} \to \mathbb{N}
$$

such that for all $a, b \in R$ with $b \neq 0$, there exist $q, r \in R$ with

$$
a = q b + r, \qquad r = 0 \text{ or } N(r) < N(b).
$$

The function $N$ is called the **Euclidean norm** or **Euclidean valuation**.

Euclidean domains admit a Euclidean algorithm, which allows the computation of greatest common divisors.

**Examples.**

- $\mathbb{Z}$, with $N(a) = |a|$.
- Every field $F$, with $N(a) = 0$.
- $F[x]$ for any field $F$, with $N(p) = \deg(p)$.
- The Gaussian integers $\mathbb{Z}[i]$, with $N(a + bi) = a^2 + b^2$.

**Non-examples.**

- $\mathbb{Z}[\sqrt{-5}]$, which is not even a UFD.
- $\mathbb{D}$, because it is not an integral domain.

## 9. Principal Ideal Domains

A **principal ideal domain** (PID) is an integral domain $R$ in which every ideal is principal: every ideal $I \subseteq R$ is of the form

$$
I = (a) = \{r a : r \in R\}
$$

for some $a \in R$.

In a PID, every ideal is generated by a single element. This is a strong condition that implies unique factorization.

**Examples.**

- $\mathbb{Z}$.
- Every field $F$.
- $F[x]$ for any field $F$.
- The Gaussian integers $\mathbb{Z}[i]$.

**Non-examples.**

- $\mathbb{Z}[x]$, because the ideal $(2, x)$ is not principal.
- $\mathbb{Z}[\sqrt{-5}]$, because the ideal $(2, 1 + \sqrt{-5})$ is not principal.
- $\mathbb{D}$, because it is not an integral domain.

## 10. Unique Factorization Domains

A **unique factorization domain** (UFD) is an integral domain $R$ in which every nonzero non-unit element can be written uniquely as a product of irreducible elements, up to order and multiplication by units.

The uniqueness is the key property: the factorization into irreducibles is essentially unique.

**Examples.**

- $\mathbb{Z}$.
- Every field $F$.
- $F[x]$ for any field $F$.
- $\mathbb{Z}[x]$.
- $\mathbb{Z}[i]$, the Gaussian integers.
- $R[x]$ for any UFD $R$.

**Non-examples.**

- $\mathbb{Z}[\sqrt{-5}]$, because $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$ gives two essentially different factorizations.
- $\mathbb{D}$, because it is not an integral domain.

## 11. The Chain of Inclusions

The following chain of inclusions holds:

$$
\text{Euclidean domains} \subset \text{Principal ideal domains} \subset \text{Unique factorization domains} \subset \text{Integral domains} \subset \text{Commutative rings}.
$$

Each inclusion is strict: there are PIDs that are not Euclidean domains, UFDs that are not PIDs, integral domains that are not UFDs, and commutative rings that are not integral domains.

**Examples separating the classes.**

- $\mathbb{Z}$ is a Euclidean domain.
- $\mathbb{Z}[(1 + \sqrt{-19})/2]$ is a PID that is not a Euclidean domain.
- $\mathbb{Z}[x]$ is a UFD that is not a PID.
- $\mathbb{Z}[\sqrt{-5}]$ is an integral domain that is not a UFD.
- $\mathbb{Z}/6\mathbb{Z}$ is a commutative ring that is not an integral domain.
- $\mathbb{D}$ is a commutative ring that is not an integral domain.

## 12. Summary of Factorization Classes

| Class | Euclidean algorithm | Every ideal principal | Unique factorization | No zero divisors | Examples |
|---|---|---|---|---|---|
| Euclidean domain | yes | yes | yes | yes | $\mathbb{Z}$, $F[x]$ |
| Principal ideal domain | no | yes | yes | yes | $\mathbb{Z}$, $F[x]$ |
| Unique factorization domain | no | no | yes | yes | $\mathbb{Z}[x]$ |
| Integral domain | no | no | no | yes | $\mathbb{Z}[\sqrt{-5}]$ |
| Commutative ring | no | no | no | no | $\mathbb{Z}/6\mathbb{Z}$, $\mathbb{D}$ |

---

# Part III: Other Classes of Rings

## 13. Noetherian Rings

A **Noetherian ring** is a commutative ring $R$ in which every ideal is finitely generated. Equivalently, every ascending chain of ideals

$$
I_1 \subseteq I_2 \subseteq I_3 \subseteq \cdots
$$

stabilizes: there exists $N$ such that $I_n = I_N$ for all $n \geq N$.

Noetherian rings are the natural setting for algebraic geometry. Every field, every PID, and every quotient of a polynomial ring over a field is Noetherian.

**Examples.**

- Every field $F$.
- $\mathbb{Z}$.
- Every PID.
- $F[x_1, \ldots, x_n]$ for any field $F$.
- $\mathbb{Z}[x_1, \ldots, x_n]$.
- $\mathbb{D}$, because it is a quotient of $\mathbb{R}[x]$ and $\mathbb{R}$ is Noetherian.

**Non-examples.**

- The ring of continuous functions on $[0, 1]$, which is not Noetherian.

## 14. Artinian Rings

An **Artinian ring** is a commutative ring $R$ in which every descending chain of ideals

$$
I_1 \supseteq I_2 \supseteq I_3 \supseteq \cdots
$$

stabilizes.

Artinian rings are in some sense dual to Noetherian rings. Every Artinian ring is Noetherian, but not conversely.

**Examples.**

- Every field $F$.
- $\mathbb{Z}/n\mathbb{Z}$ for any $n \geq 1$.
- Every finite ring.

**Non-examples.**

- $\mathbb{Z}$, because the descending chain $(2) \supseteq (4) \supseteq (8) \supseteq \cdots$ does not stabilize.
- $\mathbb{D}$, because the descending chain $(e) \supseteq (e^2) \supseteq \cdots$ does not stabilize (since $e^2 = 1$, this chain is constant, but $\mathbb{D}$ is not Artinian as a ring; more precisely, $\mathbb{D}$ is not Artinian because it has infinitely many ideals).

## 15. Local Rings

A **local ring** is a commutative ring $R$ with a unique maximal ideal $\mathfrak{m}$.

Local rings are the natural setting for the study of singularities in algebraic geometry. The quotient $R/\mathfrak{m}$ is a field, called the **residue field** of $R$.

**Examples.**

- Every field $F$, with maximal ideal $(0)$.
- $\mathbb{Z}/p^n\mathbb{Z}$ for any prime $p$ and $n \geq 1$.
- The ring of formal power series $F[[x]]$ over a field $F$.

**Non-examples.**

- $\mathbb{Z}$, because it has many maximal ideals: $(2), (3), (5), \ldots$.
- $\mathbb{D}$, because it has two maximal ideals: $(1 + e)$ and $(1 - e)$.

## 16. Dedekind Domains

A **Dedekind domain** is an integral domain $R$ in which every nonzero proper ideal factors uniquely as a product of prime ideals.

Dedekind domains generalize PIDs: every PID is a Dedekind domain, but not conversely. The ring of integers of a number field is a Dedekind domain.

**Examples.**

- Every PID, including $\mathbb{Z}$ and $F[x]$.
- The ring of integers of any number field.
- $\mathbb{Z}[\sqrt{-5}]$, which is a Dedekind domain but not a UFD.

**Non-examples.**

- $\mathbb{Z}[x]$, because it is not integrally closed.
- $\mathbb{D}$, because it is not an integral domain.

## 17. Valuation Rings

A **valuation ring** is an integral domain $R$ with a valuation

$$
v : R \setminus \{0\} \to \Gamma
$$

where $\Gamma$ is a totally ordered abelian group, such that

$$
v(a b) = v(a) + v(b), \qquad v(a + b) \geq \min(v(a), v(b)).
$$

Valuation rings are the local rings of algebraic geometry and number theory.

**Examples.**

- Every field $F$, with the trivial valuation.
- The ring of $p$-adic integers $\mathbb{Z}_p$.
- The ring of formal power series $F[[x]]$ over a field $F$.

**Non-examples.**

- $\mathbb{Z}$, because it is not local.
- $\mathbb{D}$, because it is not an integral domain.

---

# Part IV: Summary

## 18. The Main Hierarchy

The inclusions among the main classes of rings are as follows. A field is both a division ring and an integral domain; it is the most restrictive class. A general ring is the least restrictive.

- Every **field** is a **division ring**.
- Every **field** is an **integral domain**.
- Every **division ring** is a **unital ring**.
- Every **integral domain** is a **commutative ring**.
- Every **unital ring** is a **ring**.
- Every **commutative ring** is a **ring**.

A field is the intersection of the division-ring branch and the integral-domain branch. It is the most restrictive class.

**Examples in the hierarchy.**

- $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ are fields.
- $\mathbb{H}$ is a division ring that is not a field.
- $\mathbb{Z}$ is an integral domain that is not a field.
- $\mathbb{D}$ is a commutative ring that is not an integral domain.
- $\mathbb{B} = \mathbb{H} \otimes \mathbb{C}$, the biquaternions, is a unital ring that is neither commutative nor an integral domain.
- $M_n(\mathbb{R})$ for $n \geq 2$ is a unital ring that is neither commutative nor an integral domain.

## 19. The Factorization Hierarchy

The following chain summarizes the factorization classes:

$$
\text{Euclidean domains} \subset \text{PIDs} \subset \text{UFDs} \subset \text{Integral domains} \subset \text{Commutative rings}.
$$

Each inclusion is strict.

**Examples separating the classes.**

- $\mathbb{Z}$ is a Euclidean domain.
- $\mathbb{Z}[(1 + \sqrt{-19})/2]$ is a PID that is not a Euclidean domain.
- $\mathbb{Z}[x]$ is a UFD that is not a PID.
- $\mathbb{Z}[\sqrt{-5}]$ is an integral domain that is not a UFD.
- $\mathbb{Z}/6\mathbb{Z}$ is a commutative ring that is not an integral domain.
- $\mathbb{D}$ is a commutative ring that is not an integral domain.

## 20. The Chain Condition Hierarchy

The following chain summarizes the chain condition classes:

$$
\text{Artinian rings} \subset \text{Noetherian rings} \subset \text{Commutative rings}.
$$

Every Artinian ring is Noetherian. Not every Noetherian ring is Artinian.

**Examples separating the classes.**

- $\mathbb{Z}/n\mathbb{Z}$ is Artinian and Noetherian.
- $\mathbb{Z}$ is Noetherian but not Artinian.
- The ring of continuous functions on $[0, 1]$ is commutative but not Noetherian.
- $\mathbb{D}$ is Noetherian but not Artinian.

## 21. The Local Hierarchy

The following chain summarizes the local classes:

$$
\text{Valuation rings} \subset \text{Dedekind domains} \subset \text{Integral domains}.
$$

Every valuation ring is a local ring. Every Dedekind domain is an integral domain.

**Examples separating the classes.**

- $\mathbb{Z}_p$ is a valuation ring.
- $\mathbb{Z}[\sqrt{-5}]$ is a Dedekind domain but not a valuation ring.
- $\mathbb{Z}[x]$ is an integral domain but not a Dedekind domain.

## 22. Summary Table

| Class | Commutative | No zero divisors | Every ideal principal | Unique factorization | Chain conditions | Examples |
|---|---|---|---|---|---|---|
| Field | yes | yes | yes | yes | Noetherian, Artinian | $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ |
| Division ring | no | yes | — | — | — | $\mathbb{H}$ |
| Euclidean domain | yes | yes | yes | yes | Noetherian | $\mathbb{Z}$, $F[x]$ |
| PID | yes | yes | yes | yes | Noetherian | $\mathbb{Z}$, $F[x]$ |
| UFD | yes | yes | no | yes | — | $\mathbb{Z}[x]$ |
| Dedekind domain | yes | yes | no | ideals factor | Noetherian | $\mathbb{Z}[\sqrt{-5}]$ |
| Integral domain | yes | yes | no | no | — | $\mathbb{Z}[\sqrt{-5}]$ |
| Noetherian ring | yes | no | no | no | ascending | $\mathbb{Z}$, $F[x]$, $\mathbb{D}$ |
| Artinian ring | yes | no | no | no | descending | $\mathbb{Z}/n\mathbb{Z}$ |
| Local ring | yes | no | no | no | unique maximal ideal | $\mathbb{Z}_p$, $F[[x]]$ |
| Commutative ring | yes | no | no | no | — | $\mathbb{Z}/6\mathbb{Z}$, $\mathbb{D}$ |
| Unital ring | no | no | no | no | — | $M_n(\mathbb{R})$, $\mathbb{B}$ |
| General ring | no | no | no | no | — | — |

---

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991).
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002).
- I. N. Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975).
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003).
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009).
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004).
- Thomas W. Hungerford, *Algebra* (Springer, 1974).
- Oscar Zariski and Pierre Samuel, *Commutative Algebra* (Springer, 1975).
- Hideyuki Matsumura, *Commutative Ring Theory* (Cambridge University Press, 1989).

