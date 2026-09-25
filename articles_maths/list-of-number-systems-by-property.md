# __List of Number Systems by Property__

## Introduction

This article lists the number systems of the corpus as a table of properties: for each system it records whether the multiplication is commutative, associative, alternative and power-associative, whether there are zero divisors, whether the system is a division algebra, and whether it is a field. The list is organised along the doubling chain, and at each step it names the property that is lost.

Every entry points to the article that introduces the number system and states its properties. This article is a list: it introduces no definition, states no theorem, gives no proof, and carries no display mathematics. It records examples and non-examples side by side, a non-example being a number system that fails a property the previous one had — the loss of order at $\mathbb{C}$, of commutativity at $\mathbb{H}$, of associativity at $\mathbb{O}$, of the multiplicative norm at the sedenions — with the failure named and the article that records it.

## The Ordered Number Systems

The chain begins with the systems that are ordered: $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$ and $\mathbb{R}$. Each is commutative, associative, alternative and power-associative; $\mathbb{N}$ is not a group under addition, $\mathbb{Z}$ is an integral domain but not a field, $\mathbb{Q}$ and $\mathbb{R}$ are fields, and only $\mathbb{R}$ is complete. None has zero divisors.

| Number system | Commutative, associative, alternative, power-associative; zero divisors; division algebra; field | Introduced in |
|---|---|---|
| $\mathbb{N}$ | commutative, associative, power-associative; no zero divisors; not a division algebra and not a field; ordered | *The Natural Numbers* |
| $\mathbb{Z}$ | commutative, associative; an integral domain, no zero divisors; not a division algebra and not a field; ordered | *The Integers* |
| $\mathbb{Q}$ | commutative, associative; a field, so a division algebra; no zero divisors; ordered | *The Rational Numbers* |
| $\mathbb{R}$ | commutative, associative; a field and a division algebra; no zero divisors; ordered and complete | *The Real Numbers* |
| $\mathbb{Q}$ as a prime field | the smallest field of characteristic $0$; the prime field embedding | *Fields* |
| Non-example: $\mathbb{N}$ as a field | fails: it has no additive inverses and no multiplicative inverses beyond $1$ | *The Natural Numbers* |
| Non-example: $\mathbb{Z}$ as a division algebra | fails: only $\pm 1$ are units | *The Integers* |

## The Complex Numbers: the Loss of Order

The doubling of $\mathbb{R}$ gives $\mathbb{C}$, which retains commutativity, associativity, alternativity and power-associativity, remains a field and a division algebra, and has no zero divisors. What it loses is the **order**: $\mathbb{C}$ is not orderable, and its only field automorphisms fixing $\mathbb{R}$ are the identity and complex conjugation.

| Number system | Commutative, associative, alternative, power-associative; zero divisors; division algebra; field | Introduced in |
|---|---|---|
| $\mathbb{C}$ | commutative, associative; a field and a division algebra; no zero divisors; not orderable | *The Complex Numbers* |
| $\mathbb{C}$ as $\mathbb{R}[t]/(t^2+1)$ | the algebraic closure of $\mathbb{R}$; every polynomial splits | *Splitting Fields and Algebraic Closure* |
| Complex conjugation | the nontrivial $\mathbb{R}$-automorphism; the only non-identity one | *The Complex Numbers* |
| Non-example: $\mathbb{C}$ as an ordered field | fails: no ordering is compatible with the field operations | *Algebraically Closed Fields* |
| Non-example: $\mathbb{C}$ as a real algebra of dimension $1$ | fails: its real dimension is $2$ | *The Complex Numbers* |

## The Quaternions: the Loss of Commutativity

The doubling of $\mathbb{C}$ gives the quaternions $\mathbb{H}$, which retain associativity, alternativity and power-associativity, remain a division algebra and have no zero divisors, but lose **commutativity**: $ij = k$ while $ji = -k$. The quaternions are a division ring but not a field, and their centre is $\mathbb{R}$.

| Number system | Commutative, associative, alternative, power-associative; zero divisors; division algebra; field | Introduced in |
|---|---|---|
| $\mathbb{H}$ | associative, alternative, power-associative; a division algebra, no zero divisors; **not commutative**, not a field; centre $\mathbb{R}$ | *Quaternion Algebra* |
| Quaternion units | $i^2 = j^2 = k^2 = ijk = -1$; $ij = k = -ji$ | *Quaternion Algebra* |
| $\mathbb{H}$ as a division ring | every nonzero element invertible, with $x^{-1} = \bar x/N(x)$ | *Quaternion Algebra* |
| $\mathbb{H}$ as an algebra over its centre | dimension $4$ over $\mathbb{R}$, the centre | *Division Algebras* |
| Non-example: $\mathbb{H}$ as a field | fails: multiplication is not commutative | *Quaternion Algebra* |
| Non-example: $\mathbb{H}$ as an ordered field | fails: an ordered field is commutative, and $\mathbb{H}$ is not even a field | *Quaternion Algebra* |

## The Octonions: the Loss of Associativity

The doubling of $\mathbb{H}$ gives the octonions $\mathbb{O}$, which retain alternativity and power-associativity, remain a division algebra and have no zero divisors, but lose **associativity**: the associator $(xy)z - x(yz)$ is nonzero. The octonions are the last normed division algebra, and they are neither commutative nor associative.

| Number system | Commutative, associative, alternative, power-associative; zero divisors; division algebra; field | Introduced in |
|---|---|---|
| $\mathbb{O}$ | alternative and power-associative; a division algebra, no zero divisors; **not associative**, not commutative, not a field | *Octonion Algebra* |
| Octonion basis $e_0,\dots,e_7$ | $e_0 = 1$, $e_i^2 = -1$ for $i \geq 1$; the Fano-plane multiplication | *Octonion Algebra* |
| The associator | $(e_1e_2)e_4 = e_7$ but $e_1(e_2e_4) = -e_7$; the failure of associativity made explicit | *Normed Division Algebras and the Hurwitz Theorem* |
| Artin's theorem | the subalgebra generated by two elements is associative, so $\mathbb{O}$ is alternative | *Octonion Algebra* |
| Non-example: $\mathbb{O}$ as an associative algebra | fails: the associator is nonzero | *Octonion Algebra* |
| Non-example: $\mathbb{O}$ as a field | fails: it is not commutative and not associative | *Octonion Algebra* |

## The Sedenions: the Loss of Division

The doubling of $\mathbb{O}$ gives the sedenions $\mathbb{S}$, of dimension sixteen; the norm is no longer multiplicative, the system has **zero divisors**, and it is therefore not a division algebra. The sedenions are still power-associative, and the doubling continues indefinitely as a sequence of algebras.

| Number system | Commutative, associative, alternative, power-associative; zero divisors; division algebra; field | Introduced in |
|---|---|---|
| $\mathbb{S}$ | power-associative; **has zero divisors**; not a division algebra, not alternative, not a field | *Octonion Algebra* |
| The failure of the norm | $N(xy) \neq N(x)N(y)$ in dimension $16$; the multiplicative norm stops at $\mathbb{O}$ | *Normed Division Algebras and the Hurwitz Theorem* |
| Non-example: $\mathbb{S}$ as a division algebra | fails: it has zero divisors | *Octonion Algebra* |
| Non-example: a normed division algebra of dimension $16$ | does not exist: Hurwitz' theorem stops the normed division algebras at $8$ | *Normed Division Algebras and the Hurwitz Theorem* |

## The Split and Degenerate Number Systems

Beside the division chain the corpus develops the split and degenerate systems, which are commutative or associative but have zero divisors and are not division algebras: the split-complex numbers, the dual numbers, the split-biquaternions, the split-octonions and the biquaternions. These systems show that the properties are independent, and that losing order, commutativity or associativity is not the only way to fail to be a field.

| Number system | Commutative, associative, alternative, power-associative; zero divisors; division algebra; field | Introduced in |
|---|---|---|
| $\mathbb{D}$ split-complex | commutative, associative; **has zero divisors**, $\cong \mathbb{R}\times\mathbb{R}$; not a division algebra, not a field | *Split-Complex Algebra* |
| $\mathbb{D}'$ dual numbers | commutative, associative; **has nilpotents**, local; not a division algebra, not a field | *Dual Numbers Algebra* |
| Split biquaternions $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ | associative; **has zero divisors**, $\cong \mathbb{H}\oplus\mathbb{H}$, and no nonzero nilpotents; not a division algebra, not a field | *Split-Biquaternion Algebra* |
| Split-octonions | alternative; **has zero divisors**; not a division algebra, not associative | *Normed Division Algebras and the Hurwitz Theorem* |
| $\mathbb{B}$ biquaternions | associative; **has zero divisors**, $\cong M_2(\mathbb{C})$; not a division algebra, not a field | *Biquaternion Algebra* |
| Non-example: $\mathbb{D}$ as a field | fails: $(1-t)(1+t) = 0$ | *Split-Complex Algebra* |
| Non-example: the split biquaternions as a division algebra | fail: they have zero divisors, though they have no nonzero nilpotents | *Split-Biquaternion Algebra* |

## The Property Table

The properties are independent, and the table records which system has which; each entry reads yes or no.

| System | Commutative | Associative | Alternative | Power-associative | No zero divisors | Division algebra | Field |
|---|---|---|---|---|---|---|---|
| $\mathbb{N}$ | yes | yes | yes | yes | yes | no | no |
| $\mathbb{Z}$ | yes | yes | yes | yes | yes | no | no |
| $\mathbb{Q}$ | yes | yes | yes | yes | yes | yes | yes |
| $\mathbb{R}$ | yes | yes | yes | yes | yes | yes | yes |
| $\mathbb{C}$ | yes | yes | yes | yes | yes | yes | yes |
| $\mathbb{H}$ | no | yes | yes | yes | yes | yes | no |
| $\mathbb{O}$ | no | no | yes | yes | yes | yes | no |
| $\mathbb{S}$ | no | no | no | yes | no | no | no |
| $\mathbb{D}$ | yes | yes | yes | yes | no | no | no |
| $\mathbb{D}'$ | yes | yes | yes | yes | no | no | no |
| $\mathbb{H}_{\mathbb{D}}$ | no | yes | yes | yes | no | no | no |
| split-octonions | no | no | yes | yes | no | no | no |
| $\mathbb{B}$ | no | yes | yes | yes | no | no | no |

## Summary

The list gathers the number systems of the corpus by their properties. The ordered systems are $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$ and $\mathbb{R}$, which are commutative and associative and have no zero divisors. The doubling chain then loses one property at each step: $\mathbb{C}$ loses order, $\mathbb{H}$ loses commutativity, $\mathbb{O}$ loses associativity and the sedenions lose the multiplicative norm and acquire zero divisors. $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$ are the four normed division algebras, and only $\mathbb{Q}$, $\mathbb{R}$ and $\mathbb{C}$ are fields. The split and degenerate systems — the split-complex numbers, the dual numbers, the split-biquaternions, the split-octonions and the biquaternions — are commutative or associative but have zero divisors and are not division algebras. The final table records the seven properties for all thirteen systems. The non-examples — $\mathbb{N}$ and $\mathbb{Z}$ as non-fields, $\mathbb{Z}$ as a non-division algebra, $\mathbb{C}$ as non-orderable, $\mathbb{H}$ as non-commutative, $\mathbb{O}$ as non-associative, $\mathbb{S}$ as having zero divisors, the split-complex numbers as a non-field and the split-biquaternions as non-division-algebras — each name the failure.

## Summary of Notation

The article denotes its objects by name; the symbols appearing in the tables are those of the introducing articles.

| Symbol | Meaning |
|---|---|
| $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$ | naturals, integers, rationals, reals |
| $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$ | complex, split-complex, dual numbers |
| $\mathbb{H}$, $\mathbb{O}$, $\mathbb{S}$ | quaternions, octonions, sedenions |
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ | split biquaternions, of real dimension $8$ |
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | biquaternions |
| $i,j,k$ | quaternion units |
| $e_0,\dots,e_7$ | octonion basis; $e_0,\dots,e_{15}$ the sedenion basis |
| $N(x)$ | norm form |

## Further Reading

- Richard Schafer, *An Introduction to Nonassociative Algebras* (Dover, 1995), for power-associativity, alternativity, the Cayley–Dickson construction and the sedenions.
- John Conway and Derek Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the property table of the number systems and the geometry of the division algebras.
- Ian Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the realisation of the number systems as Clifford algebras and the properties they inherit.
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for the ordered systems, the field properties and the orderability criterion.
