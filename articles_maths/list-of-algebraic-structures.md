# __List of Algebraic Structures__

## Introduction

This article lists the algebraic structures the corpus builds, one rung at a time, and the axiom each rung adds. The ladder begins with a set carrying a single binary operation and climbs by adding associativity, an identity, inverses and commutativity; a second operation then makes a ring and, once every nonzero element becomes invertible, a field; scalars acting on an abelian group make a module, a vector space and finally an algebra. Some rungs are non-associative rather than associative — the Lie algebras and the Jordan algebras — and they are gathered apart from the associative ladder.

Every entry points to the article that introduces the structure and states the property that fixes the rung. This article is a list: it introduces no definition, states no theorem, gives no proof, and carries no display mathematics. It records examples and non-examples side by side, a non-example being an object that differs from its rung by exactly one axiom, with the failure named and the article that records it.

## The One-Operation Rungs

A **monoid** is the lowest rung the corpus writes down: one associative operation and an identity, with no assumption of inverses or commutativity. A **group** adds inverses, and an **abelian group** adds commutativity on top of the group axioms. The scope of the list names a closure-only rung and a semigroup rung below the monoid; neither is introduced anywhere in Parts I to III, and no entry is written for them.

| Structure | The property it has | Introduced in |
|---|---|---|
| Monoid | one associative binary operation with an identity | *Universal Properties and Categories* |
| Group | a monoid in which every element is invertible | *Groups*, §1 |
| Abelian group | a group whose operation is commutative | *Groups*, §1 |
| Non-example: $(\mathbb{Z} \setminus \{0\}, \cdot)$ | a monoid that fails inverses; only $\pm 1$ are invertible | *Groups*, §1 |
| Non-example: the symmetric group $S_n$, $n \geq 3$ | a group that fails commutativity | *Groups*, §1 |
| Non-example: $\mathbb{N}$ under addition | a commutative monoid that fails additive inverses | *The Natural Numbers* (Part V) |

## The Two-Operation Rungs

A **ring** is an abelian group carrying a second operation, a multiplication that is associative and distributive over the addition; the corpus fixes $1 \neq 0$. The **commutative ring** adds $ab = ba$, the **integral domain** adds the absence of zero divisors, and the **field** requires every nonzero element to be invertible. The **division ring** keeps associativity and inverses but drops commutativity; it is the rung at which the commutative and the non-commutative ladders part.

| Structure | The property it has | Introduced in |
|---|---|---|
| Ring | an abelian group with an associative multiplication distributive over the addition | *Rings*, §1 |
| Commutative ring | a ring whose multiplication is commutative | *Commutative Rings*; stated in *Rings*, §5 |
| Reduced ring | a commutative ring with no nonzero nilpotent | *Reduced Rings and the Nilradical* |
| Integral domain | a commutative ring with $1 \neq 0$ and no zero divisors | *Integral Domains*; stated in *Rings*, §12 |
| GCD domain | a domain in which any two elements have a greatest common divisor | *GCD Domains* |
| Bézout domain | a domain in which every finitely generated ideal is principal | *Bézout Domains* |
| Unique factorisation domain | a domain in which every nonzero nonunit factors uniquely into irreducibles | *Unique Factorisation Domains* |
| Principal ideal domain | a domain in which every ideal is principal | *Principal Ideal Domains* |
| Euclidean domain | a domain carrying a Euclidean degree function and division with remainder | *Euclidean Domains* |
| Division ring | a ring with $1 \neq 0$ in which every nonzero element is invertible | *Division Rings* |
| Ore domain | a domain in which every two nonzero elements have a common left and a common right multiple | *Ore Domains and Division Rings of Fractions* |
| Field | a commutative ring with $1 \neq 0$ in which every nonzero element is invertible | *Fields*, §1 |
| Non-example: $\mathbb{Z}$ | an integral domain that fails the field axiom: $2$ has no inverse | *The Integers* (Part V); *Rings* |
| Non-example: the split-complex numbers $\mathbb{D}$ | a commutative ring that fails the domain axiom: $(1+j)(1-j) = 0$ | *Examples of Rings and Fields* |
| Non-example: the dual numbers $\mathbb{D}'$ | a commutative ring that fails the domain axiom: $\varepsilon^2 = 0$ | *Examples of Rings and Fields* |
| Non-example: the matrix ring $M_2(\mathbb{R})$ | a ring that fails commutativity and fails inverses for nonzero elements | *Examples of Algebras* |
| Non-example: the quaternions $\mathbb{H}$ | a division ring that fails commutativity, hence is not a field | *Division Algebras* |

## The Scalar-Action Rungs

A **module** is an abelian group on which a ring acts by scalars, and a **vector space** is the case of a field of scalars, where every module is free and every space has a basis. An **algebra** adds a bilinear product of the space with itself. The corpus's broad sense of *algebra* assumes neither associativity, nor commutativity, nor a unit; the qualifiers are earned separately.

| Structure | The property it has | Introduced in |
|---|---|---|
| Module over a ring $R$ | an abelian group with a scalar action of $R$ | *Modules* |
| Vector space over a field | a module over a field, hence free with a basis | *Vector Spaces* |
| Algebra over a commutative ring | a module with a bilinear product | *Algebras* |
| Associative algebra | an algebra with $(xy)z = x(yz)$ | *Algebras* |
| Unital algebra | an algebra with an identity for its product | *Algebras* |
| Commutative algebra | an associative algebra with $xy = yx$ | *Commutative Algebras* |
| Ideals and quotients of an algebra | the two-sided ideals of an algebra and the quotient algebras they define | *Ideals and Quotients of Algebras* |
| Centre, units and zero divisors | the centre $Z(A)$, the group of units $A^\times$ and the zero divisors of an algebra | *Centre, Units, Zero Divisors and Division Algebras* |

## The Non-Associative Rungs

Two rungs replace associativity by an identity of their own: the **Lie algebra**, whose product is antisymmetric and satisfies the Jacobi identity, and the **Jordan algebra**, whose product is commutative and satisfies the Jordan identity. The non-associative algebras in general, and the identities that lie between associativity and its failure, are the subject of *Non-Associative Algebras and the Property Ladder*. The octonions are the standard non-example: a division algebra whose multiplication is not associative.

| Structure | The property it has | Introduced in |
|---|---|---|
| Lie algebra | an antisymmetric product satisfying the Jacobi identity | *Lie Algebras* |
| Jordan algebra | a commutative product satisfying the Jordan identity | *Jordan Algebras* |
| Non-associative algebra | an algebra carrying no associativity axiom | *Non-Associative Algebras and the Property Ladder* |
| Non-example: the octonions $\mathbb{O}$ | a division algebra that fails associativity, hence is not a ring | *Division Algebras*; *Octonion Algebra* (Part V) |
| Non-example: the cross product on $\mathbb{R}^3$ | an algebra that fails associativity and has no identity | *Algebras* |

## Structures Defined by an Order

The corpus also meets two rungs whose operation is not written as a multiplication: the **lattice**, with its two order-theoretic operations of join and meet, and the **Boolean algebra** of the algebra of subsets and of propositional logic. The lattice is introduced in the foundational layer; the Boolean algebra is developed as a subject in the synthetic study of the Booleans.

| Structure | The property it has | Introduced in |
|---|---|---|
| Lattice | a partial order in which every two elements have a join and a meet | *Order Theory and Lattices* |
| Complete lattice | a lattice in which every subset has a supremum and an infimum | *Order Theory and Lattices* |
| Boolean algebra | a complemented distributive lattice, the algebra of subsets | *Boolean Algebras and Lattices* (Part V) |
| Non-example: the lattice $N_5$ | a modular lattice that fails distributivity | *Order Theory and Lattices* |

## The Axiom Added at Each Rung

The ladder is a list of one added axiom per rung, and the table reads it in that direction: each row names the axiom the rung adds to the one above it, with an object at the rung.

| Rung | The axiom it adds to the rung above | A structure at the rung | Introduced in |
|---|---|---|---|
| Monoid | associativity and an identity, from a bare operation | $(\mathbb{N}, +)$ | *Universal Properties and Categories* |
| Group | inverses | $(\mathbb{Z}, +)$ | *Groups*, §1 |
| Abelian group | commutativity | $(\mathbb{Z}, +)$ | *Groups*, §1 |
| Ring | a second operation, distributing over the first | $\mathbb{Z}$ | *Rings*, §1 |
| Commutative ring | commutativity of the second operation | $\mathbb{Z}$ | *Rings*, §5 |
| Integral domain | no zero divisors | $\mathbb{Z}$ | *Rings*, §12 |
| Field | inverses for the nonzero elements | $\mathbb{Q}$ | *Fields*, §1 |
| Module | an action of a ring on an abelian group | $\mathbb{Z}^n$ | *Modules* |
| Vector space | the scalars form a field | $\mathbb{R}^n$ | *Vector Spaces* |
| Algebra | the abelian group carries a bilinear product | $M_2(\mathbb{R})$ | *Algebras* |

The non-associative rungs branch off at the algebra: the Lie algebras and the Jordan algebras keep the module structure and change the identity the product satisfies, which is why they are listed apart from the associative ladder.

## Summary

The list gathers the rungs of the algebraic ladder the corpus builds. The one-operation rungs are the monoid, the group and the abelian group; the two-operation rungs are the ring, the commutative ring, the reduced ring, the integral domain, the GCD, Bézout, unique factorisation, principal ideal and Euclidean domains, the division ring, the Ore domain and the field; the scalar-action rungs are the module, the vector space and the algebra with its associative, unital and commutative refinements; and the non-associative rungs are the Lie algebra, the Jordan algebra and the general non-associative algebra, with the lattice and the Boolean algebra met through an order rather than a product. Each row points to the article that introduces the structure, and the non-examples — $(\mathbb{Z} \setminus \{0\}, \cdot)$, $S_n$, $\mathbb{N}$, $\mathbb{Z}$, the split-complex numbers and the dual numbers, $M_2(\mathbb{R})$, $\mathbb{H}$, $\mathbb{O}$, the cross product on $\mathbb{R}^3$ and the lattice $N_5$ — name the single axiom each one fails.

## Summary of Notation

The article denotes its objects by name; the symbols that appear in the tables are the standard number systems and the two two-dimensional algebras.

| Symbol | Meaning |
|---|---|
| $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | the naturals, the integers, the rationals, the reals |
| $\mathbb{D}$ | the split-complex numbers, unit $j$, $j^2 = +1$ |
| $\mathbb{D}'$ | the dual numbers, unit $\varepsilon$, $\varepsilon^2 = 0$ |
| $\mathbb{H}$ | the real quaternions |
| $\mathbb{O}$ | the octonions |
| $S_n$ | the symmetric group on $n$ letters |
| $M_2(\mathbb{R})$ | the ring of $2 \times 2$ real matrices |
| $N_5$ | the pentagon lattice, the non-distributive modular lattice |
| $Z(A)$, $A^\times$ | the centre and the group of units of an algebra $A$ |
| $1 \neq 0$ | the nontriviality convention fixed for every ring and algebra |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the axiom-by-axiom construction of the structures of the ladder and the names fixed for each rung.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for groups, rings, modules and algebras in one ordered development.
- Saunders Mac Lane and Garrett Birkhoff, *Algebra* (Chelsea, 3rd ed. 1999), for the tabulation of structures by the axioms they satisfy.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the passage from the associative to the non-associative rungs.
