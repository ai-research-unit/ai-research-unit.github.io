
# __List of Maximal Structures Before Failure__

## Introduction

This article lists, for each property of the commutative ladder, the strongest structure of the corpus that still lacks it, together with the exact object at the boundary. It is the complement of *List of Structures from Rings to Fields*: where that article names the structure that has each property, this one names the structure that just fails to have it.

The pattern is the same at every rung. A structure is maximal before a failure when it satisfies every stronger property except one, so that the failure is isolated; the object is then the exact counterexample at that boundary. The method is that of the three examples the scope names: a reduced commutative ring is the strongest structure that fails to be an integral domain, a unique factorisation domain is the strongest that fails to be a principal ideal domain, and a principal ideal domain is the strongest that fails to be a Euclidean domain.

The article introduces nothing and proves nothing. It records examples and non-examples side by side, and it names, at each boundary, the object that shows the failure is real.

## The Strongest Structure Below Each Rung

| The property | The strongest structure that lacks it | The exact object at the boundary | Introduced in |
|---|---|---|---|
| commutativity | a division ring | $\mathbb{H}$ | *Quaternion Algebra* |
| no nonzero nilpotent | a local Artinian ring with nilpotent maximal ideal | the dual numbers $\mathbb{D}'$ | *Dual-Numbers Algebra* |
| no zero divisors | a reduced commutative ring with idempotents | $\mathbb{Z} \times \mathbb{Z}$ | *Examples of Rings and Fields* |
| unique factorisation | a Bézout domain, hence a GCD domain | $\overline{\mathbb{Z}}$ | *Bézout Domains* |
| every ideal principal | a unique factorisation domain | $\mathbb{Z}[x]$ | *Polynomial Rings and Rational Functions* |
| a Euclidean degree | a principal ideal domain | $\mathbb{Z}[(1+\sqrt{-19})/2]$ | *Euclidean Domains* |
| every nonzero element a unit | a Euclidean domain | $\mathbb{Z}$ | *The Integers* |

Each row is justified below, and the two boundaries of the non-commutative ladder are treated in a section of their own.

## The Refinement at the GCD Rung

Between an integral domain and a unique factorisation domain the corpus places the GCD domains, and the step upward branches into two incomparable steps. The boundary objects are the same ones, read in the other direction.

| The property | The strongest structure that lacks it | The exact object at the boundary | Introduced in |
|---|---|---|---|
| every finitely generated ideal is principal (a Bézout domain) | a GCD domain, in particular a unique factorisation domain | $\mathbb{Z}[x]$ | *Bézout Domains* |
| unique factorisation (a UFD) | a Bézout domain, hence a GCD domain | $\overline{\mathbb{Z}}$ | *Bézout Domains* |

Thus $\mathbb{Z}[x]$ is simultaneously the exact object at the boundary of the Bézout property and the exact object at the boundary of the principal-ideal property, and $\overline{\mathbb{Z}}$ is the exact object at the boundary of unique factorisation. The refinement itself is the subject of *GCD Domains* and *Bézout Domains*.

## The Boundary at Commutativity

The strongest structure that is not commutative is a division ring: it has no zero divisors, every nonzero element is a unit, and only the commutative law is absent. The exact object is $\mathbb{H}$, the real quaternions, in which $e_1e_2 = -e_2e_1$. The matrix ring $M_2(\mathbb{R})$ is also non-commutative, but it is a weaker witness, since it has zero divisors; the quaternions show that commutativity can fail at the very top of the ladder. The non-commutative side of this boundary is developed in *List of Structures from Rings to Division Rings*, and the division-ring property itself in *Division Rings*.

## The Boundary at Reducedness

A ring is reduced when it has no nonzero nilpotent. The strongest structure that fails to be reduced is local and Artinian with a nilpotent maximal ideal; the exact object is the dual numbers $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$, in which $\varepsilon \neq 0$ and $\varepsilon^2 = 0$. The ring $\mathbb{Z}/4\mathbb{Z}$ is the same phenomenon in finite form, with $2^2 = 0$; the dual numbers are the stronger witness because they are an algebra over a field and their only nilpotents are the elements of the maximal ideal $(\varepsilon)$. The nilradical, its identification with the intersection of the prime ideals, and the counterexamples that fix the rung are the subject of *Reduced Rings and the Nilradical*.

## The Boundary at the Domain Property

A reduced commutative ring need not be an integral domain: it can have idempotents that are not $0$ or $1$, and the products of complementary idempotents are zero divisors. The strongest such structure is a reduced ring that is a product of domains, and the exact object is $\mathbb{Z} \times \mathbb{Z}$, in which $(1,0)(0,1) = 0$ while neither factor is zero and no nonzero element is nilpotent. This is the boundary that the scope names first: a reduced commutative ring is the strongest structure that still fails to be an integral domain. The product rings and their idempotents are recorded in *Examples of Rings and Fields* and in *List of Rings by Their Idempotents*.

## The Boundary at Unique Factorisation

The strongest structure in which unique factorisation fails is a Bézout domain. A Bézout domain is a GCD domain, so greatest common divisors exist and divisibility is as well behaved as it can be without unique factorisation; and a Bézout domain need not be a unique factorisation domain. The exact object is $\overline{\mathbb{Z}}$, the ring of all algebraic integers: it is Bézout, it is not Noetherian, and it is not a unique factorisation domain. The classical Noetherian witness is $\mathbb{Z}[\sqrt{-5}]$, in which $6 = 2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$; the two factorisations are recorded in *Unique Factorisation Domains* and in *Examples of Rings and Fields*. The Bézout alternative is introduced in *Bézout Domains*.

## The Boundary at Principal Ideals

The strongest structure that is not a principal ideal domain is a unique factorisation domain, since unique factorisation is the rung immediately below and does not force every ideal to be principal. The exact object is $\mathbb{Z}[x]$: it is a unique factorisation domain by Gauss's lemma, and the ideal $(2, x)$ is not principal. The same boundary is crossed by $k[x_1, \dots, x_n]$ for $n \geq 2$. This is the second boundary that the scope names, and the failure is recorded in *Principal Ideal Domains* and in *Polynomial Rings and Rational Functions*.

## The Boundary at the Euclidean Property

The strongest structure that is not Euclidean is a principal ideal domain. A Euclidean domain is a principal ideal domain with a division algorithm, and the division algorithm is a genuine extra hypothesis: there are principal ideal domains on which no Euclidean degree exists. The exact object is $\mathbb{Z}[(1+\sqrt{-19})/2]$, the ring of integers of $\mathbb{Q}(\sqrt{-19})$, which is a principal ideal domain and is not Euclidean. The example is the one the scope names third, and it is recorded in *Euclidean Domains*. The Euclidean domains themselves are $\mathbb{Z}$, the norm-Euclidean quadratic rings $\mathbb{Z}[i]$, $\mathbb{Z}[\sqrt{-2}]$ and $\mathbb{Z}[\sqrt{2}]$, the Eisenstein integers, and the polynomial ring $k[x]$ over a field, each with its degree or norm.

## The Boundary at the Field Property

The strongest structure that is not a field is a Euclidean domain, since every field is a Euclidean domain and the loss of "every nonzero element is a unit" is the only failure. The exact object is $\mathbb{Z}$: it has a Euclidean degree, namely the absolute value, and the element $2$ is neither zero nor a unit. The Gaussian integers $\mathbb{Z}[i]$, Euclidean for the norm $a^2 + b^2$, and the polynomial ring $k[x]$ are the other standard witnesses, and they show that the boundary can be crossed while every ideal remains principal. The fields that lie beyond the boundary are listed in *List of Fields*.

## The Same Boundaries in Finite Form

The residue rings of *Modular Arithmetic and the Ring of Residues* carry the same boundaries in the smallest possible objects, and they are the finite witnesses that keep the list honest.

| Ring | The boundary it shows | Introduced in |
|---|---|---|
| $\mathbb{F}_p$ | none; a finite field lies beyond every boundary of this article | *Finite Fields* |
| $\mathbb{Z}/4\mathbb{Z}$ | reducedness: $2$ is nilpotent, the ring is local and not reduced | *Reduced Rings and the Nilradical* |
| $\mathbb{Z}/6\mathbb{Z}$ | the domain property: $2 \cdot 3 = 0$, and the ring is the product $\mathbb{F}_2 \times \mathbb{F}_3$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{Z}/n\mathbb{Z}$, $n$ composite with a repeated factor | reducedness; for $n$ squarefree the ring is a product of fields and is reduced | *Modular Arithmetic and the Ring of Residues* |

The finite witnesses are weaker than the infinite ones — the dual numbers are a local algebra over a field, where $\mathbb{Z}/4\mathbb{Z}$ is only a finite local ring — but they are the reason the boundaries are not artefacts of infinite constructions.

## The Two Boundaries of the Non-Commutative Ladder

The same method applies to the non-commutative ladder of *List of Structures from Rings to Division Rings*.

| The property | The strongest structure that lacks it | The exact object at the boundary | Introduced in |
|---|---|---|---|
| the Ore condition | a non-commutative domain that is not Ore | the free algebra $R\langle x_1, \dots, x_n\rangle$ | *Tensor Powers and the Free Algebra* |
| every nonzero element a unit, without commutativity | an Ore domain that is not a division ring | the Weyl algebra $A_1(k)$ | *Quotients of the Tensor Algebra* |

The free algebra is the strongest domain at which the passage to a division ring of fractions fails, and the Weyl algebra is the strongest domain at which it succeeds without the domain itself being a division ring. Both are recorded in *Ore Domains and Division Rings of Fractions*.

## Warnings

| Object | Why it is not a boundary witness here | Introduced in |
|---|---|---|
| $M_2(\mathbb{R})$ | it fails commutativity, but it also has zero divisors, so it is not maximal before a single failure | *Matrix Algebras* |
| $\mathbb{B}$ | it has zero divisors and is not commutative; it is not maximal before any one property of the ladder | *Biquaternion Zero Divisors* |
| $\mathbb{O}$ | not a ring, so no rung of the ladder applies | *Octonion Algebra* |
| the zero ring $\{0\}$ | excluded by the convention $1 \neq 0$ | *Rings*, §2 |

## Summary

This article has paired each property of the commutative ladder with the strongest structure of the corpus that lacks it and with the exact object at the boundary: $\mathbb{H}$ at commutativity, the dual numbers at reducedness, $\mathbb{Z} \times \mathbb{Z}$ at the domain property, $\overline{\mathbb{Z}}$ and $\mathbb{Z}[\sqrt{-5}]$ at unique factorisation, $\mathbb{Z}[x]$ at principal ideals, $\mathbb{Z}[(1+\sqrt{-19})/2]$ at the Euclidean property, and $\mathbb{Z}$ at the field property. It has added the free algebra and the Weyl algebra for the two boundaries of the non-commutative ladder. At every rung the object is maximal except for the one named failure.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The real quaternions, a division ring that is not a field |
| $\mathbb{D}'$ | The dual numbers, $\mathbb{R}[\varepsilon]/(\varepsilon^2)$ |
| $\mathbb{Z}$, $\mathbb{Z}/4\mathbb{Z}$, $\mathbb{Z} \times \mathbb{Z}$ | The integers, the residue ring, the product ring |
| $\mathbb{Z}[x]$, $k[x]$, $k[x_1,\dots,x_n]$ | Polynomial rings |
| $\mathbb{Z}[i]$, $\mathbb{Z}[\sqrt{-2}]$, $\mathbb{Z}[\sqrt{-5}]$ | Quadratic integer rings |
| $\mathbb{Z}[(1+\sqrt{-19})/2]$ | A principal ideal domain that is not Euclidean |
| $\overline{\mathbb{Z}}$ | The ring of all algebraic integers, a non-Noetherian Bézout domain |
| $M_2(\mathbb{R})$ | The $2 \times 2$ real matrix ring |
| $A_1(k)$, $R\langle x_1,\dots,x_n\rangle$ | The Weyl algebra and the free algebra |
| $\mathbb{B}$, $\mathbb{O}$ | The biquaternions and the octonions |

## Further Reading

- Oscar Zariski and Pierre Samuel, *Commutative Algebra*, Volume I (Van Nostrand, 1958), for the containment relations among Euclidean, principal, unique factorisation and Bézout domains.
- Tsit-Yuen Lam, *Exercises in Classical Ring Theory* (Springer, 2nd ed. 2003), for the standard counterexamples at each rung of the ladder.
- Paulo Ribenboim, *Classical Theory of Algebraic Numbers* (Springer, 2001), for the rings of integers, the class group and the failure of unique factorisation.
