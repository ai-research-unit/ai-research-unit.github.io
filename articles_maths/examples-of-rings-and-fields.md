# __Examples of Rings and Fields__

## Introduction

A definition of a ring and of a field is only useful once it is known how varied the examples are, and this article collects the objects that recur in the rest of the corpus, together with the invariants that separate them. The list is deliberately heterogeneous: the integers and their quotients, the rings of algebraic integers in small quadratic fields, polynomial and power series rings, the localisations of $\mathbb{Z}$ at a prime, the matrix rings, the group rings of small groups, and the dual and split complex numbers. Each entry is presented as a ring in the sense of *Rings* — a set with two operations, the multiplication commutative unless the contrary is said — and its properties are recorded: whether it is a domain, whether it is Noetherian, whether it is a unique factorisation domain or a principal ideal domain, whether it is local, whether it is a field, and what its units and its zero divisors are.

The examples serve a second purpose. They separate the hypotheses of the theorems of this category from one another: $\mathbb{Z}[x]$ is a unique factorisation domain that is not a principal ideal domain; $\mathbb{Z}[\sqrt{-5}]$ is a Noetherian domain that is not a unique factorisation domain; $\mathbb{Z}/6\mathbb{Z}$ is a Noetherian ring that is not a domain; $\mathbb{R}[\varepsilon]/(\varepsilon^2)$ is a local ring in which every nonunit is nilpotent, and the split complex numbers are isomorphic to a product of two fields; and $k[x_1,x_2,\ldots]$ in infinitely many variables is a domain that is not Noetherian. Taken together they show that no one of the implications

$$
\text{field} \Rightarrow \text{PID} \Rightarrow \text{UFD} \Rightarrow \text{domain}
$$

reverses, and that the Noetherian condition is independent of all of them except as the theorems demand it.

The background is *Rings*, *Integral Domains*, *Unique Factorisation Domains*, *Localization and the Fraction Field*, *Finite Fields*, *Algebraically Closed Fields*, *Real-Closed and Complete Ordered Fields*, *Dedekind Domains and Ideal Class Groups*, *Valuation Theory and Henselian Rings* and *Algebraic Number Theory*. Throughout, all rings have $1 \neq 0$ and are commutative unless stated otherwise; the zero ring is excluded by this convention and is not an example of anything below. The symbols $\mathbb{D}$ (split complex numbers, unit $j$, $j^2 = +1$) and $\mathbb{D}'$ (dual numbers, unit $\varepsilon$, $\varepsilon^2 = 0$) are those fixed in *Dual Numbers Algebra*; they are two distinct two-dimensional rings and the notation is chosen so that they do not collide.

---

## Finite Rings and Their Quotients

**Example ($\mathbb{Z}/n\mathbb{Z}$).** For $n \geq 1$ the ring $\mathbb{Z}/n\mathbb{Z}$ has $n$ elements and characteristic $n$. Its units are the classes of the integers coprime to $n$, so the group of units is $(\mathbb{Z}/n\mathbb{Z})^\times$ of order $\varphi(n)$; it is a domain exactly when it is a field, exactly when $n$ is prime, in which case it is $\mathbb{F}_p$; and for composite $n$ every class of a nonunit that is not zero is a zero divisor, since $ab \equiv 0$ with $a,b$ proper divisors of $n$. For $n = 4$ the units are $1, 3$ and the maximal ideal is $(2)$; for $n = 6$ the ring is $\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$ by the Chinese remainder theorem, with idempotents $0,1$ in each factor giving four idempotents in the product.

**Example (finite fields).** For $q = p^f$ there is, up to isomorphism, exactly one field $\mathbb{F}_q$ with $q$ elements; its group of units is cyclic of order $q-1$, and its prime subfield is $\mathbb{F}_p$. The smallest cases are $\mathbb{F}_2 = \{0,1\}$, $\mathbb{F}_3$, $\mathbb{F}_4 = \mathbb{F}_2[x]/(x^2+x+1)$ and $\mathbb{F}_8 = \mathbb{F}_2[x]/(x^3+x+1)$; these are the fields in which *Finite Fields* andbeing, work, and each is a simple extension of its prime field by an irreducible polynomial.

**Example (Boolean rings).** In $\mathbb{F}_2^n$ with coordinatewise operations every element is idempotent, $a^2 = a$, and $a+a = 0$; such a ring is a product of copies of $\mathbb{F}_2$ and is not a domain for $n \geq 2$, since the standard basis elements multiply to zero.

**Example (products).** For rings $R,S$ the product $R\times S$ has units $(u,v)$ with $u,v$ units, idempotents the four combinations of the idempotents of $R$ and $S$, and zero divisors whenever both factors are nonzero: $(1,0)(0,1) = 0$. A product of two nonzero rings is never a domain and never local.

---

## Rings of Number Theory

**Example (the Gaussian integers).** $\mathbb{Z}[i] = \{a+bi : a,b\in\mathbb{Z}\}$ is an integral domain, Euclidean with respect to the norm $N(a+bi) = a^2+b^2$, hence a principal ideal domain and a unique factorisation domain. Its units are $\pm1, \pm i$, the four elements of norm $1$; the element $2$ factors as $-i(1+i)^2$, and an odd rational prime $p$ remains prime in $\mathbb{Z}[i]$ if $p \equiv 3 \bmod 4$ and splits as $\pi\bar\pi$ with $N(\pi) = p$ if $p \equiv 1 \bmod 4$, the case $5 = (2+i)(2-i)$.

**Example ($\mathbb{Z}[\sqrt{-5}]$ and the failure of unique factorisation).** The ring $\mathbb{Z}[\sqrt{-5}] = \{a+b\sqrt{-5}\}$ is an integral domain, being a subring of $\mathbb{C}$, and it is Noetherian, being a quotient of $\mathbb{Z}[x]$ by the Noetherian property of *Noetherian and Artinian Rings*. It is not a unique factorisation domain:

$$
6 = 2\cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5}),
$$

and the four factors are irreducible, since the norm $N(a+b\sqrt{-5}) = a^2+5b^2$ takes the values $4, 9, 6, 6$ on them and no element of norm $2$ or $3$ exists in the ring. The two factorisations are genuinely different, since the factors are pairwise nonassociate: the units of the ring are $\pm1$ alone, and $1+\sqrt{-5}$ is not a unit multiple of $2$ or of $3$. The ring is nonetheless a Dedekind domain, and its ideal class group has order $2$, generated by the class of the ideal $(2, 1+\sqrt{-5})$, as in *Dedekind Domains and Ideal Class Groups*; the failure of unique factorisation of elements is repaired by the unique factorisation of ideals. Its field of fractions is $\mathbb{Q}(\sqrt{-5})$, and $\mathbb{Z}[\sqrt{-5}]$ is the full ring of integers of that field.

**Example (rings of integers).** For a number field $K$ the ring of integers $\mathcal{O}_K$ is a Dedekind domain, hence Noetherian, integrally closed, and of Krull dimension one, and it is a unique factorisation domain exactly when its class group is trivial; $\mathbb{Z}$, $\mathbb{Z}[i]$, $\mathbb{Z}[\sqrt{-2}]$ and $\mathbb{Z}[\zeta_n]$ are the classical examples with class number one, and $\mathbb{Z}[\sqrt{-5}]$ the classical counterexample. The cyclotomic case $\mathbb{Z}[\zeta_n]$ is Euclidean for $n \leq 10$ and $n = 12, 14$ and fails to be a unique factorisation domain first at $n = 23$. The theory is *Algebraic Number Theory* and *Cyclotomic Fields*.

**Example ($\mathbb{Z}[\sqrt{-2}]$).** This ring is Euclidean with norm $a^2+2b^2$, hence a principal ideal domain and a unique factorisation domain, and the point worth recording is the contrast with $\mathbb{Z}[\sqrt{-5}]$: the norm $a^2+2b^2$ admits a division algorithm with remainder of smaller norm, while $a^2+5b^2$ does not, and this is exactly the difference between class number one and class number two in these two quadratic fields. The same norm renders $\mathbb{Z}[\sqrt{-3}]$ Euclidean only after the ring is enlarged to the full ring of integers $\mathbb{Z}[\zeta_3]$, whose norm is $a^2-ab+b^2$.

---

## Polynomial, Power Series and Quotient Rings

**Example ($\mathbb{Z}[x]$ and $K[x]$).** $\mathbb{Z}[x]$ is an integral domain, Noetherian by the Hilbert basis theorem, and a unique factorisation domain by Gauss's lemma; it is not a principal ideal domain, since the ideal $(2,x)$ is not principal: a generator would have to divide $2$, hence be $\pm1$ or $\pm2$, and neither generates $(2,x)$, as $2$ does not divide $x$ and $1 \notin (2,x)$. Over a field the situation improves: $K[x]$ is Euclidean with the degree as Euclidean function, hence a principal ideal domain, and $K[x,y]$ is a unique factorisation domain by Gauss's lemma applied twice but again not principal, since $(x,y)$ is not principal.

**Example (power series).** The ring $K[[x]]$ of formal power series is an integral domain in which every series with nonzero constant term is a unit; consequently it is a local ring with maximal ideal $(x)$, and every nonzero ideal is $(x^n)$ for some $n$, so $K[[x]]$ is a principal ideal domain and a unique factorisation domain: its only irreducible element is $x$, up to multiplication by units. This is the prototype of a discrete valuation ring, as in *Valuation Theory and Henselian Rings*; the ring is not a field, and $x$ is a nonunit that is not a zero divisor.

**Example (quotients of a polynomial ring).** For $K$ a field and $f \in K[x]$ nonzero of degree $m$, the quotient $K[x]/(f)$ has dimension $m$ over $K$ and is a field exactly when $f$ is irreducible; it is a product of fields exactly when $f$ is squarefree. Thus $\mathbb{R}[x]/(x^2+1) \cong \mathbb{C}$, $\mathbb{R}[x]/(x^2-1) \cong \mathbb{R}\times\mathbb{R}$, and $\mathbb{R}[x]/(x^2) \cong \mathbb{D}'$, the dual numbers, whose elements are $a+b\varepsilon$ with $\varepsilon^2 = 0$, of which the units are those with $a \neq 0$ and the nonunits are all nilpotent.

**Example (split complex numbers).** The split complex numbers $\mathbb{D}$ have basis $1, j$ with $j^2 = +1$; the assignment $j \mapsto (1,-1)$ identifies

$$
\mathbb{D} = \mathbb{R}[j]/(j^2-1) \cong \mathbb{R}\times\mathbb{R},
$$

so that $\mathbb{D}$ is a product of two fields, with the nontrivial idempotents $e_\pm = \frac12(1\pm j)$ satisfying $e_+e_- = 0$, $e_+^2 = e_+$, $e_-^2 = e_-$. The contrast with $\mathbb{D}'$ is instructive: $j^2 = +1$ splits into two fields, while $\varepsilon^2 = 0$ gives a ring with a nilpotent; the two rings are the two possible two-dimensional quotients of $\mathbb{R}[x]$ by a nonconstant polynomial up to isomorphism, corresponding to a squarefree and to a nonsquarefree quadratic.

---

## Local, Noncommutative and Group Rings

**Example (localisations).** For a prime $p$ the localisation $\mathbb{Z}_{(p)}$ of $\mathbb{Z}$ at the multiplicative set of integers prime to $p$ is an integral domain with a unique maximal ideal $(p)$, so it is a local ring; its units are the fractions $a/b$ with $a,b$ both prime to $p$, and it is a principal ideal domain and a discrete valuation ring with value the exponent of $p$. Every nonzero ideal is $(p^n)$. Similarly $\mathbb{F}_p[x]_{(x)}$ and $K[[x]]$ are discrete valuation rings, and a general discrete valuation ring is characterised as a local principal ideal domain with nilradical zero, as in *Valuation Theory and Henselian Rings*.

**Example (matrix rings).** For a ring $R$ and $n \geq 2$ the ring $M_n(R)$ of $n\times n$ matrices is noncommutative, has zero divisors — the standard matrix units satisfy $E_{11}E_{22} = 0$ while both are nonzero — and has units the invertible matrices; over a field the units are the matrices of nonzero determinant. $M_n(R)$ is Noetherian when $R$ is, and it is never a domain for $n\geq2$. The upper triangular matrices form a subring that is not commutative either and that has many zero divisors.

**Example (group rings).** For a finite group $G$ and a field $K$ the group ring $K[G]$ consists of the formal $K$-linear combinations of elements of $G$, with multiplication induced by the group law. For $G = C_2 = \langle g\rangle$:

$$
\mathbb{Q}[C_2] \cong \mathbb{Q}[x]/(x^2-1) \cong \mathbb{Q}\times\mathbb{Q}, \qquad \mathbb{F}_2[C_2] \cong \mathbb{F}_2[x]/(x^2-1) = \mathbb{F}_2[x]/(x+1)^2,
$$

the first by the Chinese remainder theorem applied to the coprime factors $x-1$ and $x+1$, and the second because $x^2-1 = (x+1)^2$ in characteristic $2$; so the same group gives a product of two fields in characteristic zero and a local ring with a nilpotent in characteristic two. For $G = C_3$ and $K = \mathbb{Q}$ the factorisation $x^3-1 = (x-1)(x^2+x+1)$ with the second factor irreducible gives $\mathbb{Q}[C_3] \cong \mathbb{Q}\times\mathbb{Q}(\zeta_3)$, a product of the rational field and the quadratic cyclotomic field. The general theory is *Representation Theory of Symmetric Groups* and *Cyclotomic Fields*.

**Example (division rings, deferred).** A **division ring** is a ring in which every nonzero element is a unit, and a division ring that is not commutative is a **skew field**. By Wedderburn's little theorem of *Division Rings*, a finite division ring is a field, so every skew field is infinite; the standard skew field of the corpus is introduced in the algebra layer, in *Division Algebras*. Nothing in the present category requires its construction.

**Example (a non-Noetherian domain).** The polynomial ring $k[x_1,x_2,x_3,\ldots]$ in countably many indeterminates is an integral domain and a unique factorisation domain, but it is not Noetherian: the ideal $(x_1,x_2,x_3,\ldots)$ is not finitely generated, since any finite set of generators involves only finitely many of the variables. This is the standard witness that the Hilbert basis theorem fails for infinitely many variables, and hence that the Noetherian hypothesis in the theorems of *Noetherian and Artinian Rings* is not automatic.

---

## A Table of Invariants

The following table records, for the examples above, the properties discussed in this article. "Domain" means an integral domain, "PID" a principal ideal domain, and "UFD" a unique factorisation domain; "local" means a single maximal ideal, and the entries for rings that are not domains are marked "—" in the factorisation columns, since those notions are defined only for domains.

| Ring | Domain | Noetherian | PID | UFD | Local | Field | Characteristic | Units |
|---|---|---|---|---|---|---|---|---|
| $\mathbb{Z}$ | yes | yes | yes | yes | no | no | $0$ | $\pm1$ |
| $\mathbb{Z}/p\mathbb{Z} = \mathbb{F}_p$ | yes | yes | yes | yes | yes | yes | $p$ | $p-1$ elements |
| $\mathbb{Z}/4\mathbb{Z}$ | no | yes | — | — | yes | no | $4$ | $\{1,3\}$ |
| $\mathbb{Z}[i]$ | yes | yes | yes | yes | no | no | $0$ | $\pm1,\pm i$ |
| $\mathbb{Z}[\sqrt{-2}]$ | yes | yes | yes | yes | no | no | $0$ | $\pm1$ |
| $\mathbb{Z}[\sqrt{-5}]$ | yes | yes | no | no | no | no | $0$ | $\pm1$ |
| $\mathbb{Z}[x]$ | yes | yes | no | yes | no | no | $0$ | $\pm1$ |
| $K[x,y]$ | yes | yes | no | yes | no | no | $0$ | $K^\times$ |
| $K[[x]]$ | yes | yes | yes | yes | yes | no | $0$ | nonzero constant term |
| $\mathbb{Z}_{(p)}$ | yes | yes | yes | yes | yes | no | $0$ | $a/b$, $p\nmid a,b$ |
| $K[x]/(x^m)$ | no | yes | — | — | yes | no | — | $a_0\neq0$ |
| $\mathbb{D}' \cong \mathbb{R}[x]/(x^2)$ | no | yes | — | — | yes | no | $0$ | $a\neq0$ in $a+b\varepsilon$ |
| $\mathbb{D} \cong \mathbb{R}\times\mathbb{R}$ | no | yes | — | — | no | no | $0$ | $a^2>b^2$ in $a+bj$ |
| $\mathbb{Q}[C_2] \cong \mathbb{Q}\times\mathbb{Q}$ | no | yes | — | — | no | no | $0$ | $(a,b)$ with $ab\neq0$ |
| $M_2(\mathbb{R})$ | no | yes | — | — | no | no | $0$ | $\det\neq0$ |
| $k[x_1,x_2,\ldots]$ | yes | no | no | yes | no | no | $0$ | $k^\times$ |

**Remark.** The table shows the independence of the four chain conditions: $\mathbb{Z}[x]$ is a unique factorisation domain that is not principal; $\mathbb{Z}[\sqrt{-5}]$ is Noetherian but not a unique factorisation domain; $\mathbb{Z}/4\mathbb{Z}$ and $\mathbb{D}'$ are local and not domains; $M_2(\mathbb{R})$ is Noetherian with zero divisors; and $k[x_1,x_2,\ldots]$ is a unique factorisation domain that is not Noetherian.

---

## Summary

The examples of this article exhibit the separation of the basic properties of rings. $\mathbb{Z}$, $\mathbb{Z}[i]$, $\mathbb{Z}[\sqrt{-2}]$ and $K[x]$ are Euclidean and hence principal ideal domains; $\mathbb{Z}[x]$ and $K[x,y]$ are unique factorisation domains that are not principal, the ideals $(2,x)$ and $(x,y)$ being the standard witnesses; $\mathbb{Z}[\sqrt{-5}]$ is a Noetherian integral domain that is not a unique factorisation domain, with $6 = 2\cdot3 = (1+\sqrt{-5})(1-\sqrt{-5})$ two factorisations into irreducible and pairwise nonassociate elements, and it is a Dedekind domain of class number two whose ideals do factor uniquely; and $k[x_1,x_2,\ldots]$ is a unique factorisation domain that is not Noetherian. The finite rings $\mathbb{Z}/n\mathbb{Z}$ are fields exactly for $n$ prime and have zero divisors otherwise; the quotients $K[x]/(f)$ are fields exactly when $f$ is irreducible and products of fields exactly when $f$ is squarefree, which makes $\mathbb{R}[x]/(x^2+1) \cong \mathbb{C}$ and $\mathbb{R}[x]/(x^2-1) \cong \mathbb{R}\times\mathbb{R}$.

The two two-dimensional rings fixed by the conventions appear in their proper places: the dual numbers $\mathbb{D}' = \mathbb{R}[x]/(x^2)$, a local ring whose nonunits are nilpotent and whose unit group consists of the elements with nonzero constant term, and the split complex numbers $\mathbb{D} = \mathbb{R}[j]/(j^2-1) \cong \mathbb{R}\times\mathbb{R}$, a product of two fields with the idempotents $\frac12(1\pm j)$. $\mathbb{Z}_{(p)}$ and $K[[x]]$ are the discrete valuation rings of the list, local principal ideal domains; $M_2(R)$ and the upper triangular matrices are the noncommutative rings with zero divisors; the skew fields, which are the noncommutative division rings, belong to the algebra layer. Group rings interpolate between the two behaviours according to the characteristic: $\mathbb{Q}[C_2] \cong \mathbb{Q}\times\mathbb{Q}$ and $\mathbb{Q}[C_3]\cong\mathbb{Q}\times\mathbb{Q}(\zeta_3)$ are products of fields, while $\mathbb{F}_2[C_2] \cong \mathbb{F}_2[x]/(x+1)^2$ is local with a nilpotent.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ | The number systems |
| $\mathbb{Z}/n\mathbb{Z}$, $\mathbb{F}_p$, $\mathbb{F}_q$ | Residue rings, prime field, finite field |
| $\varphi(n)$ | Euler totient, the order of $(\mathbb{Z}/n\mathbb{Z})^\times$ |
| $\mathbb{Z}[i]$ | Gaussian integers, norm $a^2+b^2$ |
| $\mathbb{Z}[\sqrt{-2}]$, $\mathbb{Z}[\sqrt{-5}]$ | Quadratic integer rings |
| $N(a+b\sqrt{-d})$ | Norm $a^2+db^2$ |
| $\mathcal{O}_K$ | Ring of integers of a number field |
| $\mathbb{Z}_{(p)}$ | Localisation of $\mathbb{Z}$ at $p$ |
| $K[x]$, $K[x,y]$, $K[[x]]$ | Polynomial and power series rings |
| $\mathbb{D}$ | Split complex numbers, $j^2 = +1$, $e_\pm = \frac12(1\pm j)$ |
| $\mathbb{D}'$ | Dual numbers, $\varepsilon^2 = 0$ |
| $M_n(R)$ | Ring of $n\times n$ matrices over $R$ |
| $K[G]$ | Group ring of a finite group |
| $\zeta_n$ | Primitive $n$-th root of unity |



## Further Reading

- Serge Lang, *Algebra* (Springer, revised 3rd ed. 2002), for the catalogue of rings and their standard properties.
- Richard Dedekind, *Vorlesungen über Zahlentheorie*, Supplement XI (Vieweg, 1871), for the ideals of $\mathbb{Z}[\sqrt{-5}]$ and the origin of ideal factorisation.
- Harold Davenport, *The Higher Arithmetic* (Cambridge University Press, 8th ed. 2008), for the arithmetic of $\mathbb{Z}[i]$ and the quadratic integer rings.
- Paulo Ribenboim, *Classical Theory of Algebraic Numbers* (Springer, 2001), for rings of integers, class numbers and the failure of unique factorisation.
- Rudolf Lidl and Harald Niederreiter, *Finite Fields* (Cambridge University Press, 2nd ed. 1997), for the finite rings and fields.
- Bartel Leendert van der Waerden, *Algebra*, Volume 2 (Springer, 1991), for group rings and matrix rings in the classical setting.
- Oscar Zariski and Pierre Samuel, *Commutative Algebra*, Volume 1 (Van Nostrand, 1958), for local rings, discrete valuation rings and the Noetherian condition.
