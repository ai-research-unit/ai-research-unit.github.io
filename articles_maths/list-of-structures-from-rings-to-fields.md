
# __List of Structures from Rings to Fields__

## Introduction

This article lists the linear progression of commutative structures that the corpus builds one rung at a time, from a ring to a field: ring, commutative ring, reduced ring, integral domain, unique factorisation domain, principal ideal domain, Euclidean domain, field. Every entry points to the article that introduces the structure.

Each rung is recorded with the property it gains over the rung below and with the witness that shows the gain is strict: an object that satisfies every lower rung and fails the one above. The witnesses are objects of the corpus, not constructions of this article.

The article introduces nothing and proves nothing. It records examples and non-examples side by side, and it records the branch points at which the progression ceases to be linear.

## The Ladder

| Structure | The property it adds | Introduced in |
|---|---|---|
| ring | addition and multiplication with the distributive laws, unital with $1 \neq 0$ | *Rings* |
| commutative ring | $ab = ba$ for all $a, b$ | *Commutative Rings* |
| reduced ring | no nonzero nilpotent | *Reduced Rings and the Nilradical* |
| integral domain | no zero divisors, equivalently cancellation for nonzero elements | *Integral Domains* |
| GCD domain | every pair of elements has a greatest common divisor | *GCD Domains* |
| Bézout domain | every finitely generated ideal is principal | *Bézout Domains* |
| unique factorisation domain | every nonzero nonunit is a product of irreducibles, uniquely up to order and associates | *Unique Factorisation Domains* |
| principal ideal domain | every ideal is principal | *Principal Ideal Domains* |
| Euclidean domain | a Euclidean degree with division with remainder | *Euclidean Domains* |
| field | every nonzero element is a unit | *Fields* |

The progression that the menu names runs Ring → Commutative ring → Reduced ring → Integral domain → UFD → PID → Euclidean domain → Field. The two entries GCD domain and Bézout domain are the refinement of the step from an integral domain to a UFD, and they are treated separately below because at that step the progression branches rather than continuing in a line.

## The Strictness of Each Step

| Implication | The hypothesis whose loss the witness shows | Witness | Introduced in |
|---|---|---|---|
| a commutative ring is a ring | commutativity | $M_n(\mathbb{R})$, $n \geq 2$ | *Matrix Algebras* |
| a reduced ring is a commutative ring | no nonzero nilpotent | $\mathbb{Z}/4\mathbb{Z}$, in which $2^2 = 0$ | *Reduced Rings and the Nilradical* |
| an integral domain is a reduced ring | no zero divisors | $\mathbb{Z} \times \mathbb{Z}$, with $(1,0)(0,1) = 0$ | *Examples of Rings and Fields* |
| a unique factorisation domain is an integral domain | unique factorisation | $\mathbb{Z}[\sqrt{-5}]$, in which $6 = 2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$ | *Unique Factorisation Domains* |
| a principal ideal domain is a unique factorisation domain | every ideal principal | $\mathbb{Z}[x]$, whose ideal $(2, x)$ is not principal | *Principal Ideal Domains* |
| a Euclidean domain is a principal ideal domain | a Euclidean degree | $\mathbb{Z}[(1+\sqrt{-19})/2]$ | *Euclidean Domains* |
| a field is a Euclidean domain | every nonzero element a unit | $\mathbb{Z}$, in which $2$ is not a unit | *The Integers* |

The first witness, $M_2(\mathbb{R})$, is the matrix ring of *Matrix Algebras*; the progression is not entered by $M_2(\mathbb{R})$ again. The witness $\mathbb{Z}[\sqrt{-5}]$ is the classical Noetherian domain whose class group has order $2$, recorded in *Dedekind Domains and Ideal Class Groups* as well as in *Unique Factorisation Domains*. The witness $\mathbb{Z}[(1+\sqrt{-19})/2]$ is the principal ideal domain that fails to be Euclidean, recorded in *Euclidean Domains*; the subring $\mathbb{Z}[\sqrt{-19}]$ is not integrally closed.

## Examples on Each Rung

The table records where the standard objects of the corpus sit. An object appears at the strongest rung it reaches among the eight; where an object reaches a rung only through a branch, the branch is named.

| Object | Strongest rung reached | Introduced in |
|---|---|---|
| $\mathbb{Z}$ | Euclidean domain, not a field | *The Integers* |
| $\mathbb{Z}[i]$ | Euclidean domain, not a field | *Examples of Rings and Fields* |
| $k[x]$ | Euclidean domain, not a field | *Polynomial Rings and Rational Functions* |
| $k[x_1, \dots, x_n]$, $n \geq 2$ | unique factorisation domain, not principal | *Polynomial Rings and Rational Functions* |
| $\mathbb{Z}[x]$ | unique factorisation domain, not principal | *Polynomial Rings and Rational Functions* |
| $k[x, y]$ | unique factorisation domain, not principal | *Polynomial Rings and Rational Functions* |
| $\mathbb{Z}[\sqrt{2}]$ | Euclidean domain, not a field | *Examples of Rings and Fields* |
| $\mathbb{Z}[\sqrt{-5}]$ | integral domain, not a unique factorisation domain | *Examples of Rings and Fields* |
| $\mathcal{O}_K$ | Dedekind domain, not principal in general; a unique factorisation domain exactly when the class number is $1$ | *Algebraic Number Theory*, *Dedekind Domains and Ideal Class Groups* |
| $\mathbb{Z} \times \mathbb{Z}$ | reduced ring, not an integral domain | *Examples of Rings and Fields* |
| $\mathbb{Z}/4\mathbb{Z}$ | commutative ring, not reduced | *Reduced Rings and the Nilradical* |
| $\mathbb{Z}/6\mathbb{Z}$ | reduced ring, not an integral domain: $2 \cdot 3 = 0$ | *Modular Arithmetic and the Ring of Residues* |
| $M_2(\mathbb{R})$ | ring, not commutative | *Matrix Algebras* |
| $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ | field | *The Rational Numbers*, *The Real Numbers*, *The Complex Numbers* |
| $\mathbb{F}_p$, $\mathbb{F}_q$ | field | *Finite Fields* |

Every field sits at the top rung, so $\mathbb{F}_p$, $\mathbb{F}_q$, $\mathbb{Q}$, $\mathbb{R}$ and $\mathbb{C}$ are Euclidean domains as well as fields; the ring $\mathbb{Z}[\sqrt{2}]$ is Euclidean, with norm $\lvert a^2 - 2b^2 \rvert$, and reaches the same rung as $\mathbb{Z}[i]$.

## The Two Strengthenings of a GCD Domain

The step from an integral domain to a unique factorisation domain passes through a rung whose two strengthenings are incomparable. A GCD domain is an integral domain in which every pair of elements has a greatest common divisor; a Bézout domain is an integral domain in which every finitely generated ideal is principal.

| Structure | Relation to a GCD domain | Witness of strictness | Introduced in |
|---|---|---|---|
| GCD domain | the rung itself | — | *GCD Domains* |
| Bézout domain | a GCD domain in which every finitely generated ideal is principal | $\mathbb{Z}[x]$ is a GCD domain (indeed a UFD) that is not Bézout | *Bézout Domains* |
| unique factorisation domain | an incomparable strengthening of a GCD domain | $\overline{\mathbb{Z}}$ is Bézout and not a UFD | *Unique Factorisation Domains* |
| principal ideal domain | the intersection: a UFD that is Bézout, equivalently a Noetherian Bézout domain | $\mathbb{Z}[x]$ is a GCD domain (a UFD) that is not principal | *Principal Ideal Domains* |

Thus a principal ideal domain is exactly a unique factorisation domain that is also Bézout, and also exactly a Bézout domain that is Noetherian. The ring $\overline{\mathbb{Z}}$ of all algebraic integers is the standard witness that a Bézout domain need not be Noetherian and need not be a unique factorisation domain; it is introduced in *Bézout Domains*.

## The Fraction Field of Each Domain

Every rung from an integral domain upward embeds in its field of fractions, which is introduced in *Localization and the Fraction Field*. The table records the fraction field of the standard domains of the corpus; the field is the top rung of the ladder, so each domain is separated from the top by the loss of some divisibility property and not by the absence of inverses.

| Domain | Field of fractions | Introduced in |
|---|---|---|
| $\mathbb{Z}$ | $\mathbb{Q}$ | *The Rational Numbers* |
| $\mathbb{Z}[i]$ | $\mathbb{Q}(i)$ | *Examples of Rings and Fields* |
| $\mathbb{Z}[\sqrt{-5}]$ | $\mathbb{Q}(\sqrt{-5})$ | *Examples of Rings and Fields* |
| $\mathbb{Z}[\sqrt{2}]$ | $\mathbb{Q}(\sqrt{2})$ | *Examples of Rings and Fields* |
| $k[x]$, $k[x_1,\dots,x_n]$ | $k(x)$, $k(x_1,\dots,x_n)$ | *Polynomial Rings and Rational Functions* |
| $\mathbb{Z}[x]$ | $\mathbb{Q}(x)$ | *Polynomial Rings and Rational Functions* |
| $\mathcal{O}_K$ | the number field $K$ | *Algebraic Number Theory* |
| $\overline{\mathbb{Z}}$ | $\overline{\mathbb{Q}}$ | *Algebraically Closed Fields* |
| an arbitrary domain $R$ | $\operatorname{Frac}(R)$ | *Localization and the Fraction Field* |

The passage to the fraction field does not repair a failure of unique factorisation: $\operatorname{Frac}(\mathbb{Z}[\sqrt{-5}]) = \mathbb{Q}(\sqrt{-5})$ is a field, hence a unique factorisation domain, while $\mathbb{Z}[\sqrt{-5}]$ is not, because the failure lives in the integral elements.

## Warnings: Structures Expected and Absent

| Object | Why it is not on this ladder | Introduced in |
|---|---|---|
| $\mathbb{H}$ | a division ring, but not commutative, so it never enters the commutative progression | *Quaternion Algebra* |
| the free algebra $R\langle x_1, \dots, x_n\rangle$ | a non-commutative domain; the non-commutative ladder is the subject of *List of Structures from Rings to Division Rings* | *Tensor Powers and the Free Algebra* |
| $\mathbb{O}$ | a division algebra whose multiplication is not associative; not even a ring | *Octonion Algebra* |
| the zero ring $\{0\}$ | excluded by the convention $1 \neq 0$ | *Rings*, §2 |

A non-commutative division ring is not stopped by a missing zero divisor: it is stopped by commutativity, and the two chains meet only at the fields. This is recorded again, from the non-commutative side, in *List of Structures from Rings to Division Rings*.

## Summary

This article has listed the eight rungs from a ring to a field, the property gained at each, and the witness that makes each gain strict. It has recorded the two further strengthenings of a GCD domain, the unique factorisation domains and the Bézout domains, which are incomparable to each other and meet at the principal ideal domains, and it has placed the standard objects of the corpus on the rung they reach. The witnesses $M_2(\mathbb{R})$, $\mathbb{Z}/4\mathbb{Z}$, $\mathbb{Z} \times \mathbb{Z}$, $\mathbb{Z}[\sqrt{-5}]$, $\mathbb{Z}[x]$, $\mathbb{Z}[(1+\sqrt{-19})/2]$ and $\mathbb{Z}$ separate the seven steps in order.

## Summary of Notation

A catalogue denotes its structures by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ | The number systems |
| $\mathbb{Z}/n\mathbb{Z}$, $\mathbb{F}_p$, $\mathbb{F}_q$ | Residue ring, prime field, finite field |
| $M_2(\mathbb{R})$, $M_n(R)$ | Matrix rings |
| $\mathbb{Z}[i]$, $\mathbb{Z}[\sqrt{2}]$, $\mathbb{Z}[\sqrt{-5}]$ | Quadratic integer rings |
| $\mathbb{Z}[(1+\sqrt{-19})/2]$ | Ring of integers of $\mathbb{Q}(\sqrt{-19})$, a principal ideal domain that is not Euclidean |
| $\overline{\mathbb{Z}}$ | Ring of all algebraic integers |
| $\mathcal{O}_K$ | Ring of integers of a number field |
| $k[x]$, $k[x_1,\dots,x_n]$, $k[x,y]$ | Polynomial rings |
| $R\langle x_1,\dots,x_n\rangle$ | Free algebra |
| $\mathbb{H}$, $\mathbb{O}$ | Quaternions, octonions |

## Further Reading

- Irving Kaplansky, *Commutative Rings* (University of Chicago Press, revised ed. 1974), for the chain of classes and the standard counterexamples separating them.
- Oscar Zariski and Pierre Samuel, *Commutative Algebra*, Volume I (Van Nostrand, 1958), for the divisibility theory of domains, GCD domains and Bézout domains.
- Robert B. Ash, *Abstract Algebra: The Basic Graduate Year* (Dover, 2007), for a tabulation of the implications among Euclidean, principal, unique factorisation and Bézout domains.
