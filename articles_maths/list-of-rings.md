
# __List of Rings__

## Introduction

This article lists the rings that the corpus meets, commutative and non-commutative, with the data that separate them: their units, their zero divisors, their ideals and their chain conditions. Every entry points to the article that introduces the object.

The convention is that of *Rings*: a ring is associative and unital and satisfies $1 \neq 0$, so the zero ring is the single exception and is named where it occurs. The classes into which these rings fall — commutative ring, reduced ring, integral domain, unique factorisation domain, principal ideal domain, Euclidean domain, field and division ring — are gathered in *List of Structures from Rings to Fields* and *List of Structures from Rings to Division Rings*. This article gathers the objects, not the rungs.

The article introduces nothing and proves nothing. It records examples and non-examples side by side, and it records the objects that a reader might expect to find here and will not.

## The Number Systems

| Ring | Units | Zero divisors | Ideals and chain conditions | Introduced in |
|---|---|---|---|---|
| $\mathbb{Z}$ | $\pm 1$ | none | every ideal principal; Noetherian, not Artinian | *The Integers* |
| $\mathbb{Q}$ | $\mathbb{Q}\setminus\{0\}$ | none | $0,\ \mathbb{Q}$; Noetherian and Artinian | *The Rational Numbers* |
| $\mathbb{R}$ | $\mathbb{R}\setminus\{0\}$ | none | $0,\ \mathbb{R}$; Noetherian and Artinian | *The Real Numbers* |
| $\mathbb{C}$ | $\mathbb{C}\setminus\{0\}$ | none | $0,\ \mathbb{C}$; Noetherian and Artinian | *The Complex Numbers* |
| $\mathbb{D}$ | $N(u) \neq 0$ | the null cone $\{N = 0\}$ | $0,\ \mathbb{D}e_{\pm},\ \mathbb{D}$; Artinian | *Split-Complex Algebra* |
| $\mathbb{D}'$ | $x \neq 0$ | the maximal ideal $\mathfrak{m} = (\varepsilon)$ | the powers $(\varepsilon^m)$; local, Artinian | *Dual-Numbers Algebra* |
| $\mathbb{H}$ | $\mathbb{H}\setminus\{0\}$ | none | only $0$ and $\mathbb{H}$; simple | *Quaternion Algebra* |
| $\mathbb{H}_{\mathbb{D}}$ | $N(u) \in \mathbb{D}^{\times}$ | yes | two maximal ideals | *Split-Biquaternion Algebra* |
| $\mathbb{B}$ | $N(\tilde{Q}) \neq 0$ | yes | only $0$ and $\mathbb{B}$; simple, not division | *Biquaternion Algebra* |

The quaternions $\mathbb{H}$ are the non-commutative ring whose every nonzero element is a unit; the biquaternions $\mathbb{B}$ and the split-biquaternions $\mathbb{H}_{\mathbb{D}}$ are the two eight-dimensional relatives that acquire zero divisors, and the split-complex numbers $\mathbb{D}$ and the dual numbers $\mathbb{D}'$ are the two-dimensional commutative rings with a degenerate or indefinite norm form.

## Residue Rings, Finite Rings and Products

| Ring | Units | Zero divisors | Ideals and chain conditions | Introduced in |
|---|---|---|---|---|
| $\mathbb{Z}/n\mathbb{Z}$ | the classes coprime to $n$, of order $\varphi(n)$ | the nonunits of a composite modulus | ideals correspond to the divisors of $n$; finite, Artinian | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{F}_p$ | $\mathbb{F}_p^{\times}$, cyclic of order $p-1$ | none | only $0$ and $\mathbb{F}_p$; field | *Finite Fields* |
| $\mathbb{F}_q$, $q = p^n$ | cyclic of order $q-1$ | none | only $0$ and $\mathbb{F}_q$; field | *Finite Fields* |
| $\mathbb{F}_2^n$ | the elements with all coordinates $1$ | yes for $n \geq 2$ | a product of copies of $\mathbb{F}_2$ | *Examples of Rings and Fields* |
| $R \times S$ | the pairs $(u, v)$ of units | $(1, 0)(0, 1) = 0$ | a product of the ideals of the factors | *Examples of Rings and Fields* |
| $\mathbb{Z}/4\mathbb{Z}$ | $\{1, 3\}$ | $2$ is nilpotent, $2^2 = 0$, so the ring is not reduced | local with maximal ideal $(2)$; Artinian | *Reduced Rings and the Nilradical* |
| $\mathbb{Z}/6\mathbb{Z}$ | $\{1, 5\}$ | $2 \cdot 3 = 0$, neither factor zero | the product $\mathbb{F}_2 \times \mathbb{F}_3$; finite, Artinian | *Modular Arithmetic and the Ring of Residues* |
| the zero ring $\{0\}$ | $1 = 0$ | — | excluded by the convention $1 \neq 0$ | *Rings*, §2 |

The non-example that fixes this section is $\mathbb{Z}/6\mathbb{Z}$: it is reduced, being the product $\mathbb{F}_2 \times \mathbb{F}_3$, and it is not an integral domain, since $2 \cdot 3 = 0$ with both factors nonzero.

## Characteristic

The characteristic is that of *Rings*, §1: the least $n \geq 1$ with $n \cdot 1 = 0$, or $0$ if there is none. The table records where each value occurs among the rings above.

| Characteristic | Rings | Introduced in |
|---|---|---|
| $0$ | $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$, $\mathbb{H}$, $\mathbb{H}_{\mathbb{D}}$, $\mathbb{B}$ | *Rings*, §1; *The Integers*, *The Rational Numbers*, *The Real Numbers*, *The Complex Numbers*, *Split-Complex Algebra*, *Dual-Numbers Algebra*, *Quaternion Algebra*, *Split-Biquaternion Algebra*, *Biquaternion Algebra* |
| $0$ | $R[x]$, $R[[x]]$, $k(x)$, $k((t))$, $\mathbb{Z}[i]$, $\mathbb{Z}[\sqrt{2}]$, $\mathbb{Z}[\sqrt{-5}]$, $\mathcal{O}_K$, $\overline{\mathbb{Z}}$ | *Polynomial Rings and Rational Functions*, *Formal Power Series and Completion*, *Fields*, §19, *Absolute Values, Valuations and Completions*, *Examples of Rings and Fields*, *Algebraic Number Theory*, *Bézout Domains* |
| $p$ | $\mathbb{F}_p$, $\mathbb{F}_{p^n}$ | *Finite Fields* |
| $p$ | $\mathbb{F}_p[[t]]$ | *Local Fields* |
| $n$ | $\mathbb{Z}/n\mathbb{Z}$ | *Modular Arithmetic and the Ring of Residues* |
| $2$ | $\mathbb{F}_2^n$ | *Examples of Rings and Fields* |

A finite ring has nonzero characteristic, and a ring of characteristic $0$ contains a copy of $\mathbb{Z}$; a ring of characteristic $n$ contains a copy of $\mathbb{Z}/n\mathbb{Z}$. The zero ring is the only ring in which the characteristic would be $1$, and it is excluded by the convention $1 \neq 0$.

## Polynomial, Power Series and Function Rings

| Ring | Units | Zero divisors | Ideals and chain conditions | Introduced in |
|---|---|---|---|---|
| $R[x]$ | the units of $R$ | none when $R$ is a domain | principal when $R$ is a field; Noetherian when $R$ is | *Polynomial Rings and Rational Functions* |
| $R[x_1, \dots, x_n]$ | the units of $R$ | none when $R$ is a domain | finitely generated ideals, Noetherian when $R$ is | *Polynomial Rings and Rational Functions* |
| $R[[x]]$ | the series with unit constant term | none when $R$ is a domain | local when $R$ is a field | *Formal Power Series and Completion* |
| $k(x)$ | every nonzero rational function | none | only $0$ and $k(x)$; field | *Fields*, §19 |
| $k((t))$ | the Laurent series with nonzero leading term | none | the valuation ring $k[[t]]$; field | *Absolute Values, Valuations and Completions* |
| $k[[x]]$ | the series with nonzero constant term | none when $k$ is a field | local with maximal ideal $(x)$ | *Examples of Rings and Fields* |
| $k[x, x^{-1}]$ | the monomials $c x^m$, $c \neq 0$ | none | principal; the group ring $k[\mathbb{Z}]$ | *Group Algebras* |
| $\mathbb{Z}_p$ | the units of $\mathbb{Z}_p$, $\lvert x \rvert_p = 1$ | none | local with maximal ideal $(p)$ | *Absolute Values, Valuations and Completions* |
| $\mathbb{Z}_{(p)}$ | the fractions with numerator prime to $p$ | none | local with maximal ideal $p\mathbb{Z}_{(p)}$ | *Localization and the Fraction Field* |
| $\mathbb{Z}[i]$ | $\pm 1, \pm i$ | none | Euclidean, hence every ideal principal | *Examples of Rings and Fields* |
| $\mathbb{Z}[\sqrt{2}]$ | $\pm(1+\sqrt{2})^m$ | none | Euclidean, hence every ideal principal | *Examples of Rings and Fields* |
| $\mathbb{Z}[\sqrt{-2}]$ | $\pm 1$ | none | Euclidean | *Examples of Rings and Fields* |
| $\mathbb{Z}[\sqrt{-5}]$ | $\pm 1$ | none | Noetherian, not principal | *Examples of Rings and Fields* |
| $\mathbb{Z}[\zeta_n]$ | finite rank, by Dirichlet's unit theorem | none | Dedekind, not principal in general | *Cyclotomic Fields* |
| $\mathcal{O}_K$ | by Dirichlet's unit theorem | none | Dedekind, so nonzero ideals factor uniquely | *Algebraic Number Theory* |
| $\overline{\mathbb{Z}}$ | the roots of unity it contains | none | not Noetherian, but Bézout | *Bézout Domains* |

The list separates the rings in which factorisation is governed by a Euclidean algorithm ($\mathbb{Z}[i]$) from those in which it is governed only by ideals ($\mathbb{Z}[\sqrt{-5}]$ and $\mathcal{O}_K$) and from those that are not Noetherian at all ($\overline{\mathbb{Z}}$, the ring of all algebraic integers). The failure of unique factorisation in $\mathbb{Z}[\sqrt{-5}]$ is recorded in *Unique Factorisation Domains* and in *Examples of Rings and Fields*.

## Matrix, Group and Non-Commutative Rings

| Ring | Units | Zero divisors | Ideals and chain conditions | Introduced in |
|---|---|---|---|---|
| $M_n(R)$, $n \geq 2$ | the matrices whose determinant is a unit of $R$ | yes, already for $n = 2$ | only $0$ and $M_n(k)$ when $k$ is a field; simple | *Matrix Algebras* |
| $M_n(D)$, $D$ a division ring | the invertible matrices $\mathrm{GL}_n(D)$ | yes | only $0$ and $M_n(D)$; simple | *Matrix Algebras* |
| $k[G]$, $G$ finite | contains $k^\times G$ | yes as soon as $\lvert G \rvert \geq 2$ | governed by the representations of $G$ | *Group Algebras* |
| $k[G]$, $G$ infinite | contains $k^\times G$ | yes unless $k[G]$ is a domain | not Artinian, Noetherian only for special $G$ | *Group Algebras* |
| $k[G]$ for $G$ torsion-free and $k$ a domain | contains $k^\times G$ | none | — | *Non-Commutative Domains* |
| $A_1(k) = k\langle x, y\rangle/(yx - xy - 1)$ | the nonzero constants $k^{\times}$ | none | a domain; the ideal structure is one-sided | *Quotients of the Tensor Algebra* |
| $R\langle x_1, \dots, x_n\rangle$ | the units of $R$ | none | a domain when $R$ is; the one-sided ideals differ | *Tensor Powers and the Free Algebra* |
| $T(V)$, the tensor algebra | the units of $R$ when $V$ is free of rank $\geq 1$ | none when $R$ is a domain and $V$ is free | $\mathbb{Z}$-graded, with the universal property of the free algebra | *Tensor Powers and the Free Algebra* |
| $\Lambda(M)$, the exterior algebra | — | — | associative and unital, graded-commutative, generated by $M$ | *The Exterior Algebra* |
| $\mathbb{C}\ell(V, q)$, the Clifford algebra | — | — | associative and unital, parity-graded, with $v^2 = q(v)$ | *The Clifford Algebra* |
| $\operatorname{End}_A(M)$, the endomorphism ring | the automorphisms $\operatorname{Aut}_A(M)$ | — | generally non-commutative; $M_n(R) = \operatorname{End}_R(R^n)$ | *Automorphisms of Modules over an Algebra* |

The matrix ring $M_n(\mathbb{R})$, $n \geq 2$, is the standard ring that is neither commutative nor free of zero divisors; it appears again in *List of Non-Commutative Rings* and *List of Zero Divisors and Nilpotents*. The Weyl algebra $A_1(k)$ is the standard non-commutative domain whose ideal theory is asymmetric, and the free algebra $R\langle x_1, \dots, x_n\rangle$ is the free object from which the others are obtained by imposing relations.

## Rings Introduced in Other Parts of the Corpus

The corpus meets rings outside its algebra articles as well; the property the corpus records for each, and the article that introduces it, are given here.

| Ring | What the corpus records | Introduced in |
|---|---|---|
| the Boolean ring $B$ | every element satisfies $x^2 = x$; commutative of characteristic $2$, reduced and regular | *Von Neumann Regular Rings* |
| the power set ring of a set | symmetric difference and intersection; the standard Boolean ring | *Von Neumann Regular Rings* |
| the cohomology ring $H^*(X; R)$ | associative and unital, and graded-commutative: $uv = (-1)^{\lvert u \rvert \lvert v \rvert} vu$ | *Cup and Cap Products* |
| the representation ring $R_k(G)$ | the free abelian group on the isomorphism classes of finite-dimensional $k[G]$-modules, with $[V][W] = [V \otimes_k W]$ and unit the trivial module | *Character Theory* |
| the Grothendieck–Witt ring $GW(F)$ | the Grothendieck group of the isometry classes of non-degenerate quadratic forms under $\perp$, made a ring by the tensor product of forms | *The Witt Group and the Grothendieck–Witt Ring* |
| the Witt ring $W(F)$ | the quotient $GW(F)/\mathbb{Z}[H]$ by the hyperbolic plane, with the fundamental ideal $I = \ker \dim$ | *The Witt Group and the Grothendieck–Witt Ring* |
| the ring of symmetric functions $\Lambda$ | the polynomial ring $K[e_1, e_2, \dots]$ in countably many variables | *Symmetric Functions and Schur Functions* |
| the graded ring of modular forms $M_*(\Gamma(1))$ | $\mathbb{C}[E_4, E_6]$, the two generators algebraically independent of weights $4$ and $6$ | *Modular Forms* |

## Warnings

An object that a reader may expect among the rings, and does not find, is recorded here with the reason.

| Object | Why it is not listed as a ring | Introduced in |
|---|---|---|
| the octonions $\mathbb{O}$ | a division algebra, but multiplication is not associative, so $\mathbb{O}$ is not a ring | *Octonion Algebra* |
| the sedenions $\mathbb{S}$ | a sixteen-dimensional real algebra with zero divisors, whose multiplication is not associative; neither a ring nor a division algebra | *Division Algebras* |
| the zero ring $\{0\}$ | a ring, but excluded from every list by the corpus convention $1 \neq 0$ | *Rings*, §2 |
| a Lie algebra $\mathfrak{g}$ | not a ring: the bracket is bilinear and antisymmetric but not associative | *Lie Algebras* |

## Summary

This article has listed the rings of the corpus with their units, their zero divisors, their ideals and their chain conditions. The number systems $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, the split-complex numbers, the dual numbers, the quaternions, the split-biquaternions and the biquaternions open the list; the residue rings, the finite fields and the products follow; the polynomial, power series, localisation, quadratic-integer and Dedekind rings occupy the commutative middle; and the matrix, group, Weyl, free, tensor, exterior, Clifford and endomorphism rings close it. A final section gathers the rings the corpus meets outside its algebra articles: the Boolean rings, the cohomology and representation rings, the Grothendieck–Witt and Witt rings, the symmetric functions and the graded ring of modular forms. Beside the examples stand the non-examples — $\mathbb{Z}/6\mathbb{Z}$ and $\mathbb{Z}/4\mathbb{Z}$ among the finite rings, $\mathbb{Z}[\sqrt{-5}]$ and $\overline{\mathbb{Z}}$ among the commutative ones, $M_n(\mathbb{R})$ among the non-commutative ones — each with the failure named.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following, and they are the symbols of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ | The number systems |
| $\mathbb{Z}/n\mathbb{Z}$, $\mathbb{F}_p$, $\mathbb{F}_q$ | Residue ring, prime field, finite field |
| $\mathbb{D}$, $\mathbb{D}'$ | Split-complex numbers and dual numbers |
| $\mathbb{H}$, $\mathbb{H}_{\mathbb{D}}$, $\mathbb{B}$, $\mathbb{O}$ | Quaternions, split-biquaternions, biquaternions, octonions |
| $R[x]$, $R[x_1,\dots,x_n]$, $R[[x]]$ | Polynomial and power series rings |
| $k(x)$, $k((t))$ | Rational function field, Laurent series field |
| $\mathbb{Z}_{(p)}$ | Localisation of $\mathbb{Z}$ at the prime $p$ |
| $\mathbb{Z}[i]$, $\mathbb{Z}[\sqrt{2}]$, $\mathbb{Z}[\sqrt{-5}]$ | Quadratic integer rings |
| $\mathcal{O}_K$, $\overline{\mathbb{Z}}$ | Ring of integers of a number field, all algebraic integers |
| $M_n(R)$ | Matrix ring |
| $k[G]$ | Group algebra |
| $A_1(k)$, $D_1(k)$ | The Weyl algebra $k\langle x,y\rangle/(yx-xy-1)$ and its division ring of fractions |
| $R\langle x_1,\dots,x_n\rangle$, $T(V)$ | Free algebra and tensor algebra |
| $\Lambda(M)$, $\mathbb{C}\ell(V,q)$ | Exterior algebra and Clifford algebra |
| $\operatorname{End}_A(M)$ | Endomorphism ring of a module |
| $B$ | A Boolean ring |
| $H^*(X;R)$, $R_k(G)$, $GW(F)$, $W(F)$ | Cohomology ring, representation ring, Grothendieck–Witt ring, Witt ring |
| $\Lambda$, $M_*(\Gamma(1))$ | Ring of symmetric functions, graded ring of modular forms |

## Further Reading

- Tsit-Yuen Lam, *Exercises in Classical Ring Theory* (Springer, 2nd ed. 2003), for a catalogue of the standard rings with their units, zero divisors and chain conditions.
- Louis H. Rowen, *Ring Theory*, Volume I (Academic Press, 1988), for the survey of commutative and non-commutative rings that the list follows.
- Irving Kaplansky, *Commutative Rings* (University of Chicago Press, revised ed. 1974), for the commutative rings of the list and their ideal theory.
