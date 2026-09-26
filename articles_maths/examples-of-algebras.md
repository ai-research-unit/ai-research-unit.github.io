
# __Examples of Algebras__

## Introduction

The preceding articles developed the general theory of algebras over a commutative ring: ideals and quotients, the centre, units and zero divisors, automorphisms and derivations, the tensor constructions, the topological layer and the operator-algebraic layer. This article collects the standard examples and records, for each, the data the theory associates with it — the dimension, the centre, the group of units, the zero divisors, the ideals, and the position of the algebra in the classification into division, simple and semisimple algebras. It is a reference article: the individual algebras are treated in their own articles, and the purpose here is to make the data comparable at a glance.

The ground ring is a field $k$ unless a different ring is stated, and the finite-dimensional algebras are over their ground field. The number systems are those of the shared conventions: $\mathbb{R}$, $\mathbb{C}$, the split complex numbers $\mathbb{D}$ with unit $j$, $j^2 = +1$, the dual numbers $\mathbb{D}'$ with unit $\varepsilon$, $\varepsilon^2 = 0$, the quaternions $\mathbb{H}$, the split biquaternions $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_\mathbb{R}\mathbb{H}$, and the biquaternions $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$.

## The Data Table

The following table is the summary; each entry is justified in the sections below.

| Algebra | $\dim_k$ | Centre | Units | Zero divisors | Ideals | Type |
|---|---|---|---|---|---|---|
| $\mathbb{R}$ | $1$ | $\mathbb{R}$ | $\mathbb{R}\setminus\{0\}$ | none | $0,\ \mathbb{R}$ | field, division |
| $\mathbb{C}$ | $2$ | $\mathbb{C}$ | $\mathbb{C}\setminus\{0\}$ | none | $0,\ \mathbb{C}$ | field, division |
| $\mathbb{D}$ | $2$ | $\mathbb{D}$ | $N(u) \neq 0$ | yes | $0,\ \mathbb{D}e_\pm,\ \mathbb{D}$ | semisimple, not simple |
| $\mathbb{D}'$ | $2$ | $\mathbb{D}'$ | $x \neq 0$ | yes | $(\varepsilon^m)$ | local, not semisimple |
| $\mathbb{H}$ | $4$ | $\mathbb{R}$ | $\mathbb{H}\setminus\{0\}$ | none | $0,\ \mathbb{H}$ | division, simple |
| $\mathbb{H}_{\mathbb{D}}$ | $8$ | $\mathbb{D}$ | $N(u) \in \mathbb{D}^\times$ | yes | two maximal ideals | semisimple, not simple |
| $\mathbb{B}$ | $8$ (over $\mathbb{R}$) | $\mathbb{C}$ | $N(\tilde{Q}) \neq 0$ | yes | $0,\ \mathbb{B}$ | simple, not division |
| $M_n(k)$, $n \geq 2$ | $n^2$ | $k I_n$ | $\mathrm{GL}_n(k)$ | yes | $0,\ M_n(k)$ | simple, not division |
| $k[x]$ | $\infty$ | $k[x]$ | $k^\times$ | none | principal | domain, not simple |
| $k[G]$, $G$ finite | $\lvert G\rvert$ | class sums | contains $G$ | yes if $\lvert G\rvert\geq2$ | from representations | semisimple if $\operatorname{char} k \nmid \lvert G\rvert$ |

## The One-Dimensional and Two-Dimensional Algebras

### The Real Numbers

$\mathbb{R}$ is the unique one-dimensional real algebra with $1 \neq 0$: the product is forced by bilinearity and $1\cdot 1 = 1$, and the basis element $1$ has square $+1$. It is a field, hence a division algebra; its only ideals are $0$ and $\mathbb{R}$; and its group of units is $\mathbb{R}^\times = \mathbb{R}\setminus\{0\}$.

### The Complex Numbers

$\mathbb{C} = \mathbb{R}[x]/(x^2+1)$ is two-dimensional over $\mathbb{R}$, commutative, and a field; the generator $i$ satisfies $i^2 = -1$, and the norm form $N(z) = z z^* = x^2 + y^2$ vanishes only at $z = 0$, so every nonzero element is a unit. Its only ideals are $0$ and $\mathbb{C}$. Over a general field $k$, the algebra $k[x]/(f)$ is a field exactly when $f$ is irreducible, which for $f = x^2+1$ happens over $k = \mathbb{R}$ and fails over $k = \mathbb{C}$; this is the simplest instance of the dependence of the structure on the ground field.

### The Split Complex Numbers

$\mathbb{D} = \mathbb{R}[x]/(x^2-1)$ is two-dimensional and commutative, with unit $j$, $j^2 = +1$. The element $u = x + jy$ has

$$
N(u) = u u^* = x^2 - y^2, \qquad u^{-1} = \frac{x - jy}{x^2 - y^2} \ \ (x^2 \neq y^2),
$$

so the units are the elements off the two lines $x = \pm y$, and the nonzero elements on those lines are zero divisors. The idempotents

$$
e_+ = \tfrac{1}{2}(1+j), \qquad e_- = \tfrac{1}{2}(1-j)
$$

satisfy $e_+^2 = e_+$, $e_-^2 = e_-$, $e_+e_- = 0$, $e_+ + e_- = 1$, and exhibit the isomorphism $\mathbb{D} \cong \mathbb{R}\times\mathbb{R}$, $x + jy \mapsto (x+y, x-y)$. Through this isomorphism the ideals are $0$, $\mathbb{R}e_+$, $\mathbb{R}e_-$ and $\mathbb{D}$: the algebra is semisimple (it is a product of two fields) but not simple, and it is not a domain. The relation $e_+e_- = 0$ with both factors nonzero is the archetype of a zero-divisor pair.

### The Dual Numbers

$\mathbb{D}' = \mathbb{R}[x]/(x^2)$ is two-dimensional and commutative, with unit $\varepsilon$, $\varepsilon^2 = 0$. The element $x + \varepsilon y$ is a unit exactly when $x \neq 0$, with

$$
(x + \varepsilon y)^{-1} = \frac{1}{x} - \frac{y}{x^2}\,\varepsilon,
$$

and every element of the maximal ideal $(\varepsilon)$ is nilpotent, hence a zero divisor. The ideals of $\mathbb{D}'$ are the powers $(\varepsilon^m)$, $m = 0, 1, 2$, so the algebra is a local ring with unique maximal ideal $(\varepsilon)$; it is not semisimple, because its Jacobson radical $(\varepsilon)$ is nonzero and nilpotent. Unlike $\mathbb{D}$, the algebra $\mathbb{D}'$ cannot be decomposed as a product of fields, and the obstruction is exactly the nilpotent.

## The Four-Dimensional and Higher Real Algebras

### The Quaternions

$\mathbb{H}$ is four-dimensional over $\mathbb{R}$, with basis $e_0 = 1$, $e_1, e_2, e_3$, $e_k^2 = -e_0$ and $e_1e_2 = e_3$ cyclically. The norm form is

$$
N(q) = q\bar q = q_0^2 + q_1^2 + q_2^2 + q_3^2,
$$

which vanishes only at $q = 0$; hence every nonzero quaternion is a unit and $\mathbb{H}$ is a division algebra. Its centre is $\mathbb{R}\cdot 1$, it has no nonzero zero divisors, and its only ideals are $0$ and $\mathbb{H}$: it is a division ring, hence simple. It is non-commutative, so it is the first example in the list that is neither a field nor commutative.

### The Split Biquaternions

$\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_\mathbb{R}\mathbb{H}$ is eight-dimensional over $\mathbb{R}$ and four-dimensional over the split complex numbers. Since $\mathbb{D} \cong \mathbb{R}\times\mathbb{R}$ as a real algebra, distributivity of the tensor product gives

$$
\mathbb{H}_{\mathbb{D}} \cong (\mathbb{R}\times\mathbb{R})\otimes_\mathbb{R}\mathbb{H} \cong \mathbb{H}\times\mathbb{H}.
$$

So $\mathbb{H}_{\mathbb{D}}$ is a product of two copies of $\mathbb{H}$: it is semisimple, it is not simple, its centre is $\mathbb{D}$, and it has zero divisors, beginning with $1+j$ and $1-j$, which are the images of $(2,0)$ and $(0,2)$ and multiply to zero. The unit criterion is $N(u) \in \mathbb{D}^\times$. This algebra is not the four-dimensional coquaternion algebra $M_2(\mathbb{R})$; the two are distinct, and the corpus's $\mathbb{H}_{\mathbb{D}}$ is the tensor product above.

## The Biquaternion Algebra

$\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is four-dimensional over $\mathbb{C}$ and eight-dimensional over $\mathbb{R}$. Its centre is the copy of $\mathbb{C}$ spanned by $e_0$, its norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_{\mu=0}^{3} Q_\mu^2$, and

$$
\tilde{Q} \text{ is a unit} \iff N(\tilde{Q}) \neq 0 .
$$

Unlike the quaternion case, the equation $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0$ has nonzero complex solutions, for instance $Q_0 = i$, $Q_1 = 1$; hence $i e_0 + e_1$ is a zero divisor, $(i e_0 + e_1)(i e_0 - e_1) = -1 + 1 = 0$. Thus $\mathbb{B}$ has zero divisors and is not a division algebra. As a $\mathbb{C}$-algebra it is isomorphic to $M_2(\mathbb{C})$, so it is simple, with only the trivial two-sided ideals, and its centre is $\mathbb{C}$. It is the standard example of a simple algebra that is not a division algebra, and the two phenomena — simplicity and zero divisors — coexist because the ground field is $\mathbb{C}$ rather than $\mathbb{R}$.

## The General Framework

Two classical theorems organise the whole table, and the examples are best read as instances of them.

**Theorem (Wedderburn–Artin, standard).** A finite-dimensional semisimple algebra over a field $k$ is isomorphic to a finite product

$$
A \cong M_{n_1}(D_1) \times \dots \times M_{n_r}(D_r),
$$

where the $D_i$ are finite-dimensional division algebras over $k$. The algebra is simple if and only if $r = 1$.

**Theorem (Jacobson radical, standard).** The radical $J(A)$ of a finite-dimensional $k$-algebra is a nilpotent two-sided ideal containing every nilpotent one-sided ideal, and $A$ is semisimple if and only if $J(A) = 0$. For a finite-dimensional algebra this is equivalent to the absence of a nonzero nilpotent two-sided ideal, and for a commutative algebra it is equivalent to the algebra being a product of fields.

These two theorems explain the entries of the table. The split complex numbers decompose as $\mathbb{D} \cong \mathbb{R}\times\mathbb{R}$, a product of two fields, hence $r = 2$, $n_1 = n_2 = 1$, $D_1 = D_2 = \mathbb{R}$; the split biquaternions decompose as $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H}\times\mathbb{H}$, hence $r = 2$ and $D_1 = D_2 = \mathbb{H}$; the biquaternions are $M_2(\mathbb{C})$, hence $r = 1$; and the dual numbers have $J(\mathbb{D}') = (\varepsilon)\neq0$, so they are not semisimple. The classification is not a mere list: each algebra is placed by its decomposition into matrix algebras over division algebras.

## The Centre Computed

Three of the entries in the table are worth computing rather than quoting.

**The centre of $\mathbb{H}$.** Let $q = q_0 + q_1e_1 + q_2e_2 + q_3e_3$ commute with $e_1$. Then

$$
qe_1 = -q_1 + q_0e_1 - q_2e_3 + q_3e_2, \qquad e_1q = -q_1 + q_0e_1 + q_2e_3 - q_3e_2,
$$

so $q_2 = q_3 = 0$. Commuting with $e_2$ in the same way gives $q_1 = q_3 = 0$. Hence $q = q_0 \in \mathbb{R}$, and $Z(\mathbb{H}) = \mathbb{R}$.

**The centre of $M_n(k)$.** If $A$ commutes with every matrix unit $E_{ij}$, then for every $i,j$,

$$
E_{ij}A = AE_{ij},
$$

which on comparing the two sides forces $A_{ii} = A_{jj}$ for all $i,j$ and $A_{rs} = 0$ for $r \neq s$. Hence $A = \lambda I_n$, and $Z(M_n(k)) = kI_n$.

**The centre of $\mathbb{H}_{\mathbb{D}}$.** Since $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\times\mathbb{H}$, the centre is $Z(\mathbb{H})\times Z(\mathbb{H}) \cong \mathbb{R}\times\mathbb{R} \cong \mathbb{D}$; under the identification $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_\mathbb{R}\mathbb{H}$ this is the copy $\mathbb{D}\otimes 1$ spanned by $e_0$ and $j$, as claimed.

**The centre of $k[G]$.** An element $\sum_g a_g g$ commutes with every $h \in G$ precisely when the coefficient function $a : G \to k$ is constant on conjugacy classes; hence the centre has a basis of **class sums** and dimension equal to the number of conjugacy classes.

## The Units Computed

The unit group is determined by a norm form in each of the division-algebra-like cases, and the criterion is that the norm be invertible in the coefficient ring of the form: over $\mathbb{R}$ and over $\mathbb{C}$ this is the statement that the norm does not vanish, while for $\mathbb{H}_{\mathbb{D}}$ the norm takes values in $\mathbb{D}$ and must be a unit there.

| Algebra | Norm form | Unit criterion | Example of a non-unit |
|---|---|---|---|
| $\mathbb{D}$ | $x^2 - y^2$ | $x^2 \neq y^2$ | $1 + j$ |
| $\mathbb{D}'$ | $x^2$ | $x \neq 0$ | $\varepsilon$ |
| $\mathbb{H}$ | $q_0^2+q_1^2+q_2^2+q_3^2$ | $q \neq 0$ | none |
| $\mathbb{H}_{\mathbb{D}}$ | $\sum_\mu Q_\mu^2$, $Q_\mu = q_\mu + jq'_\mu \in \mathbb{D}$ | $N(u) \in \mathbb{D}^\times$ | $1 + j$ |
| $\mathbb{B}$ | $Q_0^2+Q_1^2+Q_2^2+Q_3^2$ | $N(\tilde{Q}) \neq 0$ | $ie_0 + e_1$ |

In each case the inverse is the conjugate divided by the norm, and the criterion is that the division be legitimate. For $\mathbb{D}$, the elements on the two null lines have no inverse and are zero divisors; for $\mathbb{D}'$, the whole maximal ideal consists of non-units, all nilpotent; for $\mathbb{H}$, the norm form is positive definite, so there are no non-units besides $0$; for $\mathbb{B}$ the norm form takes values in the field $\mathbb{C}$, and its isotropic vectors are precisely the nonzero zero divisors. For $\mathbb{H}_{\mathbb{D}}$ the norm form takes values in $\mathbb{D}$, whose real part $\sum_\mu(q_\mu^2 + q'^2_\mu)$ is positive definite, so $N(u) = 0$ forces $u = 0$ and the norm form does not single out the zero divisors: a nonzero $u$ is a zero divisor exactly when $N(u)$ is a nonzero zero divisor of $\mathbb{D}$, as for $u = 1+j$, with $N(u) = 2 + 2j$.

## Matrix Algebras

Let $k$ be a field and $n \geq 2$. The algebra $M_n(k)$ of $n\times n$ matrices has dimension $n^2$, its centre is the scalar matrices $kI_n$, and its group of units is the general linear group $\mathrm{GL}_n(k)$. Its two-sided ideals are only $0$ and $M_n(k)$: the algebra is simple. Indeed, if a nonzero ideal contains a matrix $A$ with a nonzero entry $A_{ij}$, then multiplying by the matrix units $E_{ki}$ and $E_{jl}$ produces every matrix unit, hence the whole algebra.

The zero divisors are the nonzero non-invertible matrices, which exist as soon as $n \geq 2$: the matrix units satisfy $E_{11}E_{22} = 0$ with both factors nonzero, and any nonzero matrix of rank less than $n$ kills a nonzero vector on one side. So $M_n(k)$ is simple but not a division algebra, and the two-sided ideal theory is trivial while the one-sided theory is not: the left ideals of $M_n(k)$ are exactly the sets of matrices whose columns lie in a fixed subspace of $k^n$. The matrix algebra is treated in detail.

## Polynomial Algebras

Let $k$ be a field and let $k[x_1, \dots, x_n]$ be the polynomial algebra in $n$ commuting indeterminates. It is commutative, infinite-dimensional over $k$, and an integral domain: a product of nonzero polynomials is nonzero. Its group of units is $k^\times$, because only the nonzero constants have inverses; its ideals are finitely generated for every $n$, by the Hilbert basis theorem, and they are principal for $n = 1$, while for $n \geq 2$ they need not be principal. It is not simple, and it has no nonzero nilpotent elements.

For $n = 1$ the structure is completely described by divisibility: every ideal of $k[x]$ is $(f)$ for a unique monic polynomial $f$, the maximal ideals are $(x - a)$ for $a \in k$ when $k$ is algebraically closed, and the units are the nonzero constants. The polynomial algebra is the free commutative $k$-algebra on one generator, and it is the commutative counterpart of the free algebra of *Tensor Powers and the Free Algebra*; it is treated.

## Group Algebras

Let $G$ be a finite group and $k$ a field. The group algebra $k[G]$ has $k$-basis $G$, so $\dim_k k[G] = |G|$, and multiplication is the bilinear extension of the group law; every element of $G$ is a unit, so $G \subseteq k[G]^\times$. The **augmentation map** $\pi : k[G] \to k$, $\pi\bigl(\sum a_g g\bigr) = \sum a_g$, is an algebra homomorphism, and its kernel is the **augmentation ideal** $I(G)$, generated by the elements $g - 1_G$; the quotient $k[G]/I(G) \cong k$ is the trivial representation. Over a field of characteristic dividing $|G|$ the algebra is local when $G$ is a $p$-group, with $I(G)$ the unique maximal ideal, and in characteristic zero the structure of $k[G]$ is that of the semisimple decomposition below.

Zero divisors appear as soon as $G$ is nontrivial: if $g \in G$ has order $m \geq 2$, then

$$
(1 - g)(1 + g + \dots + g^{m-1}) = 1 - g^m = 0,
$$

with both factors nonzero, so $1 - g$ is a zero divisor. When $\operatorname{char} k$ does not divide $|G|$, Maschke's theorem makes $k[G]$ semisimple, and over $k = \mathbb{C}$ it decomposes as a product of matrix algebras

$$
\mathbb{C}[G] \cong \prod_{\rho \text{ irreducible}} M_{n_\rho}(\mathbb{C}),
$$

one factor for each irreducible complex representation, of size equal to its degree; the algebra is simple only for the trivial group. The centre of $k[G]$ consists of the class sums, and it has dimension equal to the number of conjugacy classes. Group algebras are treated, and their operator-algebraic completions.

## Summary

The examples fall into a small number of structural types. The **division algebras** among them are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$; the **fields** are the commutative ones, and the **simple algebras** are those with no nontrivial two-sided ideals, namely $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{B} \cong M_2(\mathbb{C})$ and $M_n(k)$. The algebras with **zero divisors or nilpotents** — $\mathbb{D}$, $\mathbb{D}'$, $\mathbb{H}_{\mathbb{D}}$, $\mathbb{B}$, $M_n(k)$ for $n\geq2$, $k[G]$ for $|G|\geq2$ — are exactly the ones that are not division algebras, and the two criteria of size of the centre and existence of zero divisors separate the cases: $\mathbb{H}$ is a division algebra with centre $\mathbb{R}$, $\mathbb{B}$ is simple but not a division algebra with centre $\mathbb{C}$, $\mathbb{D}$ is semisimple but not simple with centre $\mathbb{D}$, and $\mathbb{D}'$ is local with a nilpotent radical.

The table at the head of the article records the data for each algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | Ground field |
| $\mathbb{R}, \mathbb{C}$ | Real and complex numbers |
| $\mathbb{D}$ | Split complex numbers, unit $j$, $j^2 = +1$ |
| $\mathbb{D}'$ | Dual numbers, unit $\varepsilon$, $\varepsilon^2 = 0$ |
| $\mathbb{H}$ | Quaternions, basis $e_0 = 1, e_1, e_2, e_3$ |
| $\mathbb{H}_{\mathbb{D}}$ | Split biquaternions, $\mathbb{D}\otimes_\mathbb{R}\mathbb{H}$, $\dim_\mathbb{R} = 8$ |
| $\mathbb{B}$ | Biquaternions, $\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ |
| $M_n(k)$ | $n\times n$ matrices over $k$ |
| $k[x_1,\dots,x_n]$ | Polynomial algebra |
| $k[G]$ | Group algebra of a finite group |
| $Z(A)$ | Centre of $A$ |
| $A^\times$ | Group of units of $A$ |
| $N(u) = uu^*$ | Norm form, multiplicative |
| $\pi$ | Augmentation map $k[G] \to k$ |



## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the classification of finite-dimensional algebras and the examples.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for simplicity, semisimplicity and the Jacobson radical.
- Thomas W. Hungerford, *Algebra* (Springer, 1974), for fields, polynomial algebras and group algebras.
- Irving Kaplansky, *Fields and Rings* (Chicago, 2nd ed. 1972), for division rings and the Wedderburn theory.
- Lynn H. Loomis and Shlomo Sternberg, *Advanced Calculus* (Addison-Wesley, 1968), for the matrix and polynomial examples over the reals.
