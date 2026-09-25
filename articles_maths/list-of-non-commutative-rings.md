
# __List of Non-Commutative Rings__

## Introduction

This article lists the non-commutative rings of the corpus — the matrix rings, the quaternions and their relatives, the group rings, the free algebra, the tensor algebra and the Weyl algebra — and it records what is lost by comparison with the commutative case. Every entry points to the article that introduces the object.

The list gathers the rings in which $ab \neq ba$ for some pair of elements. It includes the division ring $\mathbb{H}$, which is the non-commutative ring with the fewest zero divisors; the matrix rings, which are the non-commutative source of idempotents and one-sided ideals; the group rings, which are non-commutative exactly when the group is; the free algebra and the tensor algebra, which are the freely generated cases; and the Weyl algebra, which is the quantised polynomial ring.

The article introduces nothing and proves nothing. It records examples and non-examples side by side, and it names the commutative features that each non-commutative ring replaces.

## The Matrix Rings

| Ring | Centre | Zero divisors | The structure that is lost | Introduced in |
|---|---|---|---|---|
| $M_n(R)$, $n \geq 2$ | the scalars | $E_{11}E_{22} = 0$ | commutativity; the ring is simple for $R$ a field | *Matrix Algebras* |
| $M_2(\mathbb{C})$ | $\mathbb{C}$ | yes | the biquaternion algebra is this ring | *Biquaternion Algebra* |
| the upper triangular matrices | the diagonal | strictly upper triangular matrices square to zero | not simple: it has a nontrivial nilpotent ideal | *Matrix Algebras* |
| $M_n(R) \times M_m(S)$ | $Z(R) \times Z(S)$ | $(1,0)(0,1) = 0$ | not simple | *Examples of Rings and Fields* |

The matrix ring is the standard non-commutative ring: it is simple when the coefficient ring is a field, so it has no nontrivial two-sided ideals, and it is therefore not a domain and not a division ring, since the matrix units are zero divisors. The Wedderburn–Artin theorem writes every finite-dimensional semisimple algebra as a product of matrix algebras over division algebras, and this is recorded in *Division Algebras*.

## The Quaternion Algebras and Their Relatives

| Ring | Centre | Zero divisors | What it is | Introduced in |
|---|---|---|---|---|
| $\mathbb{H}$ | $\mathbb{R}$ | none | a division ring, and a domain | *Quaternion Algebra* |
| $\mathbb{B}$, the biquaternions | $\mathbb{C}$ | yes | isomorphic to $M_2(\mathbb{C})$ as a $\mathbb{C}$-algebra | *Biquaternion Algebra* |
| $\mathbb{H}_{\mathbb{D}}$, the split-biquaternions | $\mathbb{D}$ | yes | isomorphic to $\mathbb{H} \oplus \mathbb{H}$ via the idempotents $e_{\pm}$ | *Split-Biquaternion Algebra* |
| $\mathbb{O}$, the octonions | $\mathbb{R}$ | none | not a ring: the multiplication is not associative | *Octonion Algebra* |

The three eight-dimensional relatives of $\mathbb{H}$ differ exactly in the sign of the norm form, and the sign decides whether a zero divisor exists. The biquaternions have the algebraically closed centre $\mathbb{C}$ and split as $M_2(\mathbb{C})$; the split-biquaternions have the split centre $\mathbb{D} = \mathbb{R}[j]/(j^2-1)$ and split as $\mathbb{H} \oplus \mathbb{H}$ through the idempotents $e_{\pm} = \tfrac{1}{2}(1 \pm j)$, which satisfy $e_+ e_- = 0$. The octonions are excluded from the list of rings by non-associativity and not by a zero divisor.

## The Group Rings

| Group ring | The group | Commutative? | Zero divisors | Introduced in |
|---|---|---|---|---|
| $k[G]$ for $G$ abelian | abelian | yes, a commutative ring | none if $G$ is torsion-free and $k$ a domain | *Group Algebras* |
| $k[G]$ for $G$ non-abelian | non-abelian | no | none if $G$ is torsion-free and $k$ a domain | *Group Algebras* |
| $k[F_n]$, the free group | $F_n$ | no for $n \geq 2$ | none: $F_n$ is torsion-free | *Ore Domains and Division Rings of Fractions* |
| $\mathbb{Q}[C_3]$ | $C_3$ | yes | $\mathbb{Q}[C_3] \cong \mathbb{Q} \times \mathbb{Q}(\zeta_3)$, so it has idempotents | *Examples of Rings and Fields* |
| $\mathbb{F}_2[C_2]$ | $C_2$ | yes | $\mathbb{F}_2[C_2] \cong \mathbb{F}_2[x]/(x+1)^2$, with a nilpotent | *Examples of Rings and Fields* |
| $k[C_p]$, with $\zeta_p \in k$ and $\operatorname{char} k \nmid p$ | $C_p$ | yes | $k[C_p] \cong k^p$, a product of fields | *Group Algebras* |

A group ring is commutative exactly when the group is abelian, so the non-commutative group rings are those of the non-abelian groups. The torsion-free hypothesis governs the zero divisors and not the commutativity: $k[F_n]$ is a non-commutative domain, while $k[C_2]$ is a commutative ring with zero divisors. The group ring of a torsion-free group is a domain, and it is listed among the non-commutative domains in *List of Domains*.

## The Free Algebra, the Tensor Algebra and the Weyl Algebra

| Ring | Presentation | The universal property | Introduced in |
|---|---|---|---|
| $R\langle x_1, \dots, x_n\rangle$, the free algebra | the non-commuting polynomial ring | the free $R$-algebra on $n$ generators | *Tensor Powers and the Free Algebra* |
| $T(V)$, the tensor algebra | $\bigoplus_{n \geq 0} V^{\otimes n}$ | the free associative algebra on the vector space $V$ | *Tensor Powers and the Free Algebra* |
| $\Lambda(V)$, the exterior algebra | $T(V)/(v \otimes v)$ | the free graded-commutative algebra; $v^2 = 0$ | *The Exterior Algebra* |
| $A_1(k) = k\langle x, y\rangle/(yx - xy - 1)$, the Weyl algebra | the quantised polynomial ring in two variables | the algebra of differential operators on $k[x]$ | *Quotients of the Tensor Algebra* |
| $\mathbb{C}\ell(V, q)$, a Clifford algebra | $T(V)/(v \otimes v - q(v))$ | the quantised exterior algebra | *The Clifford Algebra* |

The free algebra and the tensor algebra are the non-commutative analogues of the polynomial ring, and they lose the commutative universal property: a homomorphism from $R\langle x_1, \dots, x_n\rangle$ may send the $x_i$ to arbitrary elements, but the images need not commute, so the commutative polynomial ring is a quotient of the free algebra by the commutator ideal. The Weyl algebra and the Clifford algebras are the quotients of the tensor algebra in which the commutator and the square are fixed by a relation, and they are the standard quantisations.

## The Two-Sided Ideals

| Ring | Simple? | The two-sided ideals | Introduced in |
|---|---|---|---|
| $M_n(k)$, $n \geq 2$ | yes | $(0)$ and $M_n(k)$ alone | *Matrix Algebras* |
| $\mathbb{H}$ | yes | $(0)$ and $\mathbb{H}$ alone | *Quaternion Algebra* |
| $\mathbb{B} \cong M_2(\mathbb{C})$ | yes | $(0)$ and $\mathbb{B}$ alone | *Biquaternion Algebra* |
| $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$ | no | the two ideals $\mathbb{H}e_+$ and $\mathbb{H}e_-$ | *Split-Biquaternion Algebra* |
| $A_1(k)$ | yes | $(0)$ and $A_1(k)$ alone | *Quotients of the Tensor Algebra* |
| the free algebra $R\langle x_1, \dots, x_n\rangle$ | no | the commutator ideal and the ideals generated by the relations | *Tensor Powers and the Free Algebra* |
| the upper triangular matrices | no | the nilpotent ideal of strictly upper triangular matrices | *Matrix Algebras* |

The simple rings replace the maximal ideals of the commutative theory: a commutative ring is a field exactly when its only ideals are $(0)$ and $(1)$, and the non-commutative analogue is the simple ring, of which $M_n(k)$ and $A_1(k)$ are the standard examples. The split-biquaternions are the example that shows the difference between simple and semisimple, since they are semisimple without being simple, and their two ideals come from the idempotents $e_{\pm}$.

## What Is Lost by Comparison with the Commutative Case

| Commutative feature | What replaces it | The witness | Introduced in |
|---|---|---|---|
| $ab = ba$ | the commutator $[a,b] = ab - ba$ | $M_2(\mathbb{R})$ and every matrix ring | *Matrix Algebras* |
| left ideals are right ideals | the two-sided, left and right ideals differ | the free algebra | *Non-Commutative Domains* |
| the field of fractions always exists | a division ring of fractions exists only under the Ore condition | $A_1(k)$ is Ore, the free algebra is not | *Ore Domains and Division Rings of Fractions* |
| every finite domain is a field | Wedderburn's little theorem: every finite division ring is a field | the finite fields of *List of Finite Fields* | *Division Rings* |
| the maximal ideals give quotients that are fields | simple rings replace the maximal ideals | $M_n(\mathbb{R})$ is simple, and not a field | *Matrix Algebras* |

The losses accumulate from the first row to the last: the commutative theory of divisibility rests on the maximal ideals and the primes, and the non-commutative theory replaces them with the simple rings and the one-sided ideals. Every row of the table is a feature that a reader arriving from the commutative sections of this Part will look for in vain, and the last column names where the non-commutative substitute is developed.

## Warnings

| Object | Why it is not a non-commutative ring of this list | Introduced in |
|---|---|---|
| $\mathbb{O}$, the octonions | not associative, so not a ring | *Octonion Algebra* |
| $\mathbb{S}$, the sedenions | not associative, and with zero divisors | *Division Algebras* |
| $\mathbb{D}$, the split-complex numbers | commutative, with zero divisors | *Split-Complex Algebra* |
| $\mathbb{D}'$, the dual numbers | commutative, with a nilpotent | *Dual-Numbers Algebra* |
| $\mathbb{Z}/6\mathbb{Z}$ | commutative, with zero divisors | *Modular Arithmetic and the Ring of Residues* |
| every commutative ring | not on this list: commutativity is the criterion for exclusion | *Commutative Rings* |

The objects in the first two rows are the ones a reader might expect here on the strength of the quaternions: they are the next two algebras of the Cayley–Dickson chain, and they are excluded by the failure of associativity at the octonions.

## Summary

This article has listed the non-commutative rings of the corpus: the matrix rings $M_n(R)$, which are simple and have zero divisors; the quaternions, which are a division ring; the biquaternions and split-biquaternions, which are the eight-dimensional relatives with zero divisors and the identifications $M_2(\mathbb{C})$ and $\mathbb{H} \oplus \mathbb{H}$; the group rings, non-commutative exactly for the non-abelian groups and a domain for the torsion-free ones; the free algebra and the tensor algebra, which are the freely generated cases; and the Weyl algebra and the Clifford algebras, which are the quantised quotients. Beside them the article has recorded what the commutative case loses: commutativity replaced by the commutator, the coincidence of left and right ideals lost, the field of fractions made conditional on the Ore condition, the maximal ideals replaced by the simple rings, and unique factorisation without a general theory.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $M_n(R)$ | The $n \times n$ matrix ring |
| $E_{11}, E_{22}$ | Matrix units |
| $\mathbb{H}$, $\mathbb{B}$, $\mathbb{H}_{\mathbb{D}}$, $\mathbb{O}$ | Quaternions, biquaternions, split-biquaternions, octonions |
| $\mathbb{D}$ | The split-complex numbers, the centre of $\mathbb{H}_{\mathbb{D}}$ |
| $e_{\pm} = \tfrac{1}{2}(1 \pm j)$ | The idempotents of $\mathbb{H}_{\mathbb{D}}$ |
| $k[G]$, $k[F_n]$, $k[C_2]$ | Group rings; $F_n$ free, $C_2$ of order two |
| $R\langle x_1,\dots,x_n\rangle$ | The free algebra |
| $T(V)$, $\Lambda(V)$, $\mathbb{C}\ell(V,q)$ | Tensor, exterior and Clifford algebras |
| $A_1(k)$ | The Weyl algebra $k\langle x,y\rangle/(yx - xy - 1)$ |
| $[a,b] = ab - ba$ | The commutator |

## Further Reading

- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for matrix rings, simple rings and the non-commutative substitutes for the commutative theory.
- Paul M. Cohn, *Free Rings and Their Relations* (Academic Press, 2nd ed. 1985), for the free algebra, the tensor algebra and the free ideal theory.
- Donald S. Passman, *The Algebraic Structure of Group Rings* (Wiley, 1977), for the group ring and the zero-divisor problem.
