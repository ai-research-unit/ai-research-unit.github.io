
# __Division Rings__

## Introduction

This article is the last rung of the non-commutative chain of *Rings and Fields*, directly above *Ore Domains and Division Rings of Fractions*. It is also the article in which the two chains are compared: the commutative chain ends at the fields, the non-commutative chain ends at the division rings, and the difference between the two ends is exactly the commutativity hypothesis that the chain has been shedding since *Rings*. Throughout, $D$ denotes a ring with $1 \neq 0$ **not assumed commutative**; the corpus default, the commutative ring, is not the base here, and every statement that requires commutativity says so.

A **division ring** is a ring with $1 \neq 0$ in which every nonzero element is a unit, and a **skew field** is another name for the same object. The article gives the elementary theory — that a division ring has no zero divisors, that its centre is a field, and that it is finite-dimensional or infinite-dimensional over that centre — and proves **Wedderburn's little theorem**, that every finite division ring is a field. The two kinds of example are the quaternions, finite-dimensional over their centre, and the first Weyl field of *Ore Domains and Division Rings of Fractions*, above, infinite-dimensional over its centre. The article stops here: the theory of simple and semisimple rings, of the Jacobson radical and of the Wedderburn–Artin structure theorem belongs to *Simple and Semisimple Modules*, in a later category of this Part, and is not stated in this chain.

---

## Division Rings

**Definition.** A **division ring** is a ring $D$ with $1 \neq 0$ in which every nonzero element is a unit: $D^{\times} = D \setminus \{0\}$. A commutative division ring is a **field**, and the older name for a division ring is a **skew field**.

**Proposition.** A division ring is a domain, hence is prime, hence is semiprime, and it has no nonzero nilpotent element and no nonzero nilpotent ideal.

**Proof.** If $ab = 0$ with $a \neq 0$ then $b = a^{-1}ab = 0$, so there are no zero divisors and the ring is a domain. The chain of implications is the one of *Non-Commutative Domains* and *Prime Rings*, above. $\square$

**Corollary.** Every field is a division ring, and a division ring is a field exactly when it is commutative. The class of division rings is not closed under subrings: the field $\mathbb{Q}$ is a division ring, the ring $\mathbb{Z}$ is a subring of it and is not one.

**Proof.** A field is a commutative ring with $1 \neq 0$ in which every nonzero element is invertible, which is the definition here with the word commutative added. $\square$

**Proposition.** A finite domain is a division ring.

**Proof.** Let $A$ be a finite ring with $1 \neq 0$ and no zero divisors, and let $a \neq 0$. The map $x \mapsto ax$ from $A$ to itself is injective, since $ax = ay$ gives $a(x - y) = 0$ and hence $x = y$; an injective map of a finite set to itself is bijective, so there is $x$ with $ax = 1$. So every nonzero element has a right inverse. A right inverse in a ring with no zero divisors is two-sided: if $ax = 1$ with $x \neq 0$, then $(xa - 1)x = xax - x = x - x = 0$, and cancelling the nonzero $x$ on the right gives $xa = 1$. Hence $A$ is a division ring. $\square$

**Corollary.** In a finite ring, the conditions of having no left zero divisor, of having no right zero divisor, of being a domain and of being a division ring coincide, and by Wedderburn's little theorem below they also coincide with being a field.

---

## The Centre and the Dimension over It

**Proposition.** The centre $Z(D)$ of a division ring is a field.

**Proof.** The centre is a commutative subring containing $1$, and it has no zero divisors, since $D$ does not. If $0 \neq z \in Z(D)$ then $z$ is invertible in $D$, and its inverse is central: for every $d \in D$,

$$
z^{-1}d = z^{-1}dzz^{-1} = z^{-1}zdz^{-1} = dz^{-1} ,
$$

using $dz = zd$. Hence every nonzero element of $Z(D)$ is a unit of $Z(D)$, and $Z(D)$ is a field. $\square$

**Definition.** $D$ is **finite-dimensional over its centre** if there are finitely many elements $d_1, \ldots, d_n \in D$ such that every element of $D$ is a $Z(D)$-linear combination $z_1d_1 + \cdots + z_nd_n$ with $z_i \in Z(D)$; the least such $n$ is the **dimension** of $D$ over its centre. Otherwise $D$ is **infinite-dimensional over its centre**.

**Remark.** The centre $Z(D)$ is the largest subfield of $D$ that lies in the centre, and the definition of dimension is the elementary one: it asks for a finite list whose central multiples exhaust $D$. The vocabulary of algebras and of vector spaces over a field, which formalises this, belongs to *Algebras* and to *Linear Spaces*, in later categories of this Part, and nothing from those articles is used here beyond the definition just given.

**Theorem.** Every finite division ring is a field.

**Proof (Wedderburn's little theorem).** Let $D$ be a finite division ring, let $F = Z(D)$ be its centre, and write $q = |F|$ and $n$ for the dimension of $D$ over $F$, so that $|D| = q^n$ and $|D^{\times}| = q^n - 1$. The centre is a field by the proposition above, hence $q = p^m$ is a prime power, and $n \geq 1$.

The multiplicative group $D^{\times}$ acts on itself by conjugation. The orbits are the conjugacy classes of $D^{\times}$, and the class of $x$ has size $(q^n - 1)/(q^{n_x} - 1)$, where $C_D(x)$ is the centraliser of $x$ in $D$, a division ring containing $F$, and $|C_D(x)| = q^{n_x}$ with $n_x$ dividing $n$. The central elements are the elements of $F^{\times}$, and they contribute $q - 1$ classes of size one. Writing the class equation and omitting the central terms gives

$$
|D^{\times}| = |F^{\times}| + \sum_{x} \big( |D^{\times}| / |C_D(x)^{\times}| \big) = (q - 1) + \sum_{x} \frac{q^n - 1}{q^{n_x} - 1} ,
$$

the sum being over representatives of the non-central conjugacy classes, for which $n_x < n$ and $n_x$ divides $n$.

Suppose $n \geq 2$ and let $\Phi_n$ be the $n$-th cyclotomic polynomial. Since $n_x$ divides $n$ and $n_x < n$, the polynomial $\Phi_n$ divides $x^n - 1$ and also divides the quotient $(x^n - 1)/(x^{n_x} - 1)$, because $\Phi_n$ is the product of the linear factors of $x^n - 1$ belonging to the primitive $n$-th roots of unity and none of those is a root of $x^{n_x} - 1$. Hence $\Phi_n(q)$ divides $q^n - 1$ and each quotient $(q^n - 1)/(q^{n_x} - 1)$, and therefore divides $(q - 1)$, which is the difference of $q^n - 1$ and the sum of the quotients in the class equation.

On the other hand $\Phi_n(q) = \prod (q - \zeta)$, the product being over the primitive $n$-th roots of unity, and for each of them $q - \zeta$ lies in the open half-plane $\operatorname{Re} z > q - 1$, so $|q - \zeta| > q - 1$. Hence $|\Phi_n(q)| > (q-1)^{\varphi(n)} \geq q - 1$ for $n \geq 2$ and $q \geq 2$, contradicting the divisibility just proved. Therefore $n = 1$ and $D = F$: the division ring is a field. $\square$

**Corollary.** Every finite skew field is a field, and the finite division rings are exactly the finite fields. In particular a finite division ring has $p^m$ elements for a prime $p$ and an integer $m \geq 1$.

**Proof.** The theorem gives the first statement, and the finite fields are classified by their orders in *Finite Fields*, above; $\mathbb{F}_p$ for prime $p$ is the smallest example of each characteristic. $\square$

**Example (a finite division ring that is not a field does not exist).** The matrix-style candidates fail: $\mathbb{Z}/4\mathbb{Z}$ is finite, commutative and not a field, and the smallest finite division rings are the fields $\mathbb{F}_p$. The theorem is the reason no finite non-commutative division ring appears anywhere in this corpus.

---

## The Two Kinds of Example

### Finite-Dimensional over the Centre

**Theorem.** The quaternions $\mathbb{H}$ form a division ring that is not a field, and $\mathbb{H}$ is four-dimensional over its centre $\mathbb{R}$.

**Proof.** By *Non-Commutative Domains*, above, where $\mathbb{H}$ is defined as the real algebra with basis $1, i, j, k$ and $i^2 = j^2 = k^2 = ijk = -1$, every nonzero element is a unit, so $\mathbb{H}$ is a division ring; and $ij = k \neq -k = ji$, so $\mathbb{H}$ is not commutative. The centre contains $\mathbb{R} = \mathbb{R} \cdot 1$; conversely, if $q = a + bi + cj + dk$ is central, then $qi = iq$ gives, comparing coefficients, $b = c = d = 0$, so $q \in \mathbb{R}$. Hence $Z(\mathbb{H}) = \mathbb{R}$ and the basis $1, i, j, k$, four elements, generates $\mathbb{H}$ over $\mathbb{R}$, so the dimension over the centre is four. $\square$

**Remark.** The computation of the centre is the standard one: a central element must commute with each of $i, j, k$, and each of those conditions kills two of the three imaginary coefficients. The quaternion ring is the standard example of a division ring finite-dimensional over its centre, and its centre is the field $\mathbb{R}$.

### The Multiplication Table and the Subfields of the Quaternions

The basis elements multiply as follows, the table being read with the row element on the left and the column element on the right; the identities $i^2 = j^2 = k^2 = ijk = -1$ generate the whole table.

| $\cdot$ | $1$ | $i$ | $j$ | $k$ |
|---|---|---|---|---|
| $1$ | $1$ | $i$ | $j$ | $k$ |
| $i$ | $i$ | $-1$ | $k$ | $-j$ |
| $j$ | $j$ | $-k$ | $-1$ | $i$ |
| $k$ | $k$ | $j$ | $-i$ | $-1$ |

**Theorem.** The multiplication table of $\mathbb{H}$ is as displayed, the conjugate of $q = a + bi + cj + dk$ is $\bar q = a - bi - cj - dk$, and $q\bar q = \bar q q = a^2 + b^2 + c^2 + d^2$ is a positive real number for $q \neq 0$.

**Proof.** The diagonal entries are the defining relations $i^2 = j^2 = k^2 = -1$. Multiplying $ijk = -1$ on the right by $k$ gives $-ij = -k$, so $ij = k$; multiplying it on the left by $i$ gives $-jk = -i$, so $jk = i$. From $jk = i$, multiplication on the left by $j$ gives $ji = j^2k = -k$, and multiplication on the right by $k$ gives $ik = jk^2 = -j$. Next, $(ik)(ki) = ik^2i = -i^2 = 1$, so that $ki$ is the inverse of $ik$: thus $ki = (-j)^{-1} = -j^{-1} = j$, using $j^{-1} = -j$. Finally, multiplying $ik = -j$ on the left by $k$ gives $kik = -kj$, while $kik = (ki)k = jk = i$, so $kj = -i$. Hence the table is as displayed. The conjugate is the linear map sending $1, i, j, k$ to $1, -i, -j, -k$, and multiplying $q$ by $\bar q$ with the table gives $a^2 + b^2 + c^2 + d^2$ in the centre. $\square$

**Example (subfields of $\mathbb{H}$).** The real span of $1$ and $i$ is a subfield of $\mathbb{H}$ isomorphic to $\mathbb{C}$, and it is a maximal commutative subring; the real span of $1$ is a subfield isomorphic to $\mathbb{R}$, the centre. Every nonzero imaginary unit $u$ with $u^2 = -1$ spans a copy of $\mathbb{C}$ with $1$, so $\mathbb{H}$ contains infinitely many subfields isomorphic to $\mathbb{C}$, and none of them is the centre. In particular the centre of a subring of a division ring need not lie in the centre of the division ring: $\mathbb{C} \subseteq \mathbb{H}$ has centre $\mathbb{C}$, while $Z(\mathbb{H}) = \mathbb{R}$.

**Remark.** The centre of $\mathbb{H}$ is $\mathbb{R}$, and $\mathbb{H}$ is four-dimensional over it; that a division ring finite-dimensional over its centre is a division algebra is the language of *Division Algebras*, in *Linear Algebras*, a later category of this Part, and the multiplication table above is the whole of what this chain needs from the quaternions.

### Infinite-Dimensional over the Centre

**Theorem.** The first Weyl field $D_1(k) = \operatorname{Frac}(A_1(k))$ is a division ring that is not a field and is infinite-dimensional over its centre $k$.

**Proof.** It is a division ring by Ore's theorem, it is not commutative because $A_1(k)$ is not, and its centre is $k$ by the computation in *Ore Domains and Division Rings of Fractions*, above (the article shows $Z(A_1(k)) = k$ and that the powers of $y$ are linearly independent over $k$). No finite list of elements can generate $D_1(k)$ over $k$: if $d_1, \ldots, d_n$ generated it, then $A_1(k)$, being a subring, would be contained in the $k$-span of the finitely many products of the $d_i$, and that span is finite-dimensional whereas $A_1(k)$ contains the powers of $y$, which are linearly independent over $k$ and infinitely many. $\square$

**Corollary.** The two division rings of this section are not isomorphic over their centres: the first is finite-dimensional over its centre and the second is not, and the dimension over the centre is an invariant of a division ring together with its centre.

**Proof.** An isomorphism of division rings carries the centre to the centre, and it carries a finite generating list over the centre to a finite generating list, so the property of being finite-dimensional over the centre is preserved. $\square$

**Example.** The quaternion division ring and the first Weyl field are the two kinds of example that the corpus uses, and they stand at the two ends of the range of possibilities: a division ring can be finite-dimensional over its centre, like $\mathbb{H}$, or infinite-dimensional over its centre, like $D_1(k)$. The finite-dimensional ones are the division algebras of $k$-theory, treated in *Division Algebras*, in *Linear Algebras*, a later category of this Part, and the theory of both kinds together is the structure theory of simple rings of *Simple and Semisimple Modules*, also later.

### An Infinite Division Ring of Characteristic $p$

**Example.** Let $k$ be a field of characteristic $p > 0$ and let $G$ be an ordered group that is
not abelian, for instance the free group on two generators, with Malcev–Neumann division ring
$D = k((G))$ of *Ore Domains and Division Rings of Fractions*, above. Then $D$ has characteristic
$p$ and is not a field, since the group elements multiply as they do in $G$; and $D$ is
infinite-dimensional over its centre, because its centre contains $k$ while the elements of $G$
are linearly independent over $k$ and infinitely many. So the division rings of the second kind
occur in every characteristic, and the characteristic-$p$ case is the one in which the first Weyl
field of the preceding subsection is unavailable, the Weyl algebra being defined over a field of
characteristic zero.

### Finite Subgroups of the Multiplicative Group

**Example.** The multiplicative group of a division ring does not share the arithmetic of the multiplicative group of a field. In $\mathbb{H}$ the eight elements $\pm 1, \pm i, \pm j, \pm k$ form a subgroup isomorphic to the quaternion group $Q_8$, which is finite, non-abelian and non-cyclic, whereas every finite subgroup of the multiplicative group of a field is cyclic, by the standard theorem of *Finite Fields*, above. Wedderburn's little theorem constrains the ring and not the group: the subring generated by these eight elements is the ring of Lipschitz quaternions $\mathbb{Z}[i, j, k]$, which is infinite and of characteristic zero, so the theorem does not apply to it, and its element $2$ is not a unit.

**Remark.** In characteristic $p > 0$ the two theories come closer: a finite subgroup $G$ of $D^{\times}$ there generates a subring that is finite, since its elements are finite sums of products of elements of $G$ with coefficients in $\mathbb{F}_p$, and a finite subring without zero divisors is a field by the proposition above together with Wedderburn's little theorem. No such reduction is available in characteristic zero, and the quaternion group inside $\mathbb{H}$ is the witness.

### Matrix Rings over a Division Ring

**Theorem.** Let $D$ be a division ring and let $n \geq 2$. Then the matrix ring $M_n(D)$ is prime and semiprime, is not a domain for $n \geq 2$, and is not a division ring; the matrix ring $M_n(D)$ is a division ring only for $n = 1$.

**Proof.** The matrix ring is prime if and only if $D$ is prime, by the theorem on matrix rings in *Prime Rings*, above, and $D$ is prime; the same theorem gives semiprimeness. The computation $E_{12}E_{12} = 0$ with $E_{12} \neq 0$ shows that there are zero divisors for $n \geq 2$, and a ring with zero divisors is not a division ring. $\square$

**Remark.** The matrix rings over division rings are the standard examples of simple rings, and the theorem that they exhaust the simple Artinian rings together with the Wedderburn–Artin structure theorem belongs to *Simple and Semisimple Modules*, in a later category of this Part; the chain of this article stops before them, and only the primeness and the absence of the domain property are recorded here.


---

## The Position in the Chains

**Theorem.** The classes of the non-commutative chain are ordered as

$$
\text{division ring} \implies \text{Ore domain} \implies \text{domain} \implies \text{prime} \implies \text{semiprime} ,
$$

and each implication is strict.

**Proof.** A division ring is a domain by the proposition above, and it is an Ore domain: for nonzero $a, b$ the choice $x = a^{-1}$, $y = b^{-1}$ gives nonzero $x, y$ with $xa = 1 = yb$, which is the oriented form of the left Ore condition. Every Ore domain is a domain by definition, and the implications from domain onward are *Non-Commutative Domains* and *Prime Rings*, above.

The implications are strict: $\mathbb{Z}$ is an Ore domain and not a division ring; the free algebra $k\langle x_1, x_2\rangle$ is a domain and not an Ore domain; $M_2(F)$ is prime and not a domain; and $k \times k$ is semiprime and not prime. $\square$

**Corollary.** The commutative chain and the non-commutative chain meet exactly at the fields and the integral domains: a commutative division ring is a field, a commutative Ore domain is an integral domain, and the intersection of the two chains is the commutative half of each.

**Proof.** A commutative domain is an integral domain by *Non-Commutative Domains*, above, and a commutative division ring is a field by definition; the chains themselves are the two halves of the category. $\square$

---

## Summary

A division ring, or skew field, is a ring with $1 \neq 0$ in which every nonzero element is a unit; a commutative division ring is a field, so the class of fields is the intersection of the two chains of the category. A division ring is a domain, hence prime and semiprime, and a finite domain is a division ring. The centre of a division ring is a field, and a division ring is either finite-dimensional or infinite-dimensional over its centre, in the elementary sense of a finite generating list of central multiples; Wedderburn's little theorem states that a finite division ring is a field, so finite skew fields and finite fields are the same class, and its proof is the class equation of the multiplicative group together with the divisibility of the cyclotomic polynomial values. The two examples are the quaternions, four-dimensional over the centre $\mathbb{R}$ and not commutative, and the first Weyl field, infinite-dimensional over the centre $k$ and not commutative; the two are distinguished by the dimension over the centre. The multiplicative group of a division ring is not the multiplicative group of a field: the quaternion group sits inside $\mathbb{H}^{\times}$, while in characteristic zero the subring it generates is infinite and Wedderburn's little theorem does not reach it. The chain stops at the division rings: simple and semisimple modules, the Jacobson radical and the Wedderburn–Artin theorem belong to the module theory of a later category of this Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $D$ | A ring with $1 \neq 0$, not assumed commutative; the base of this article |
| division ring, skew field | A ring with $1 \neq 0$ in which $D^{\times} = D \setminus \{0\}$ |
| field | A commutative division ring |
| $D^{\times}$ | The group of units, equal to $D \setminus \{0\}$ |
| $Z(D)$ | The centre of $D$, a field |
| $Z(\mathbb{H}) = \mathbb{R}$, $Z(D_1(k)) = k$ | The centres of the two standard examples |
| finite-dimensional over the centre | There is a finite list of elements whose central multiples exhaust $D$ |
| dimension over the centre | The least length of such a list; four for $\mathbb{H}$, infinite for $D_1(k)$ |
| $\mathbb{H}$ | The quaternions $a + bi + cj + dk$ with $i^2 = j^2 = k^2 = ijk = -1$ |
| $A_1(k)$, $D_1(k)$ | The Weyl algebra and the first Weyl field $\operatorname{Frac}(A_1(k))$ |
| $q^n = |D|$, $q^{n_x} = |C_D(x)|$ | The orders used in the class equation of Wedderburn's theorem |
| $\Phi_n$ | The $n$-th cyclotomic polynomial, used in the proof of Wedderburn's little theorem |
| $M_n(D)$, $M_2(F)$ | The matrix ring over a division ring, prime and not a domain for $n \geq 2$ |
| $\mathbb{Z}$, $k \times k$ | The witnesses of the strictness of the chain of classes |
| $Q_8 \subseteq \mathbb{H}^{\times}$ | The quaternion group, a finite non-abelian subgroup of the units of a division ring |

## Further Reading

- L. E. Dickson, *Algebras and Their Arithmetics* (University of Chicago Press, 1923), for the classical theory of division algebras and the place of the quaternions.
- I. N. Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for division rings, their centres and the chain of ring classes.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the structure theory of division rings and the matrix rings over them.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for Wedderburn's little theorem with the cyclotomic proof, and for the finite-dimensional division algebras.
- J. H. M. Wedderburn, *A theorem on finite algebras* (Transactions of the American Mathematical Society, 1905), for the original statement and proof that every finite division ring is a field.
