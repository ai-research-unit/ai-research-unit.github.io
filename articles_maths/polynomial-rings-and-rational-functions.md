# __Polynomial Rings and Rational Functions__

## Introduction

The polynomial ring $R[x]$ over a commutative ring $R$ is the free commutative $R$-ring on one generator, and its fraction field $K(x)$, the field of rational functions, is the simplest field of transcendence degree one over $K$. Between them they carry most of the elementary algebra of the corpus: the division algorithm and the Euclidean algorithm, the content and Gauss's lemma, the universal property of evaluation, the Chinese remainder theorem for coprime moduli, , over a field, the Euclidean–principal–unique-factorisation chain of *Euclidean Domains*. They are also the two objects of which the applications are most numerous: interpolation, partial fractions, resultants and discriminants, the arithmetic of number fields through $\mathbb{Z}[x]$ and its quotients, the combinatorics of symmetric functions in $R[x_1,\ldots,x_n]$, and the codes, are all statements about polynomials and rational functions.

This article collects the structural facts about $R[x]$ and $K(x)$ that the rest of the corpus uses, and then turns to the applications. It is an applications article of the category *Rings and Fields*, so the emphasis is on what the objects do: a polynomial is an object of a ring and at the same time a function on the ring; a rational function is an element of a fraction field and at the same time a decomposition into partial fractions; and the two readings are related by the universal property, which is the only formal tool needed to pass between them.

The ring-theoretic background is *Rings*, *Integral Domains*, *Unique Factorisation Domains* and *Localization and the Fraction Field*; the field-theoretic background is *Fields*, *Field Extensions* and *Splitting Fields and Algebraic Closure*; the multivariate theory is *Gröbner Bases and Elimination Theory* and *Symmetric Functions and Schur Functions*, and the arithmetic uses are in *Algebraic Number Theory* and *Dedekind Domains and Ideal Class Groups*. Throughout, $R$ is a commutative ring with $1 \neq 0$, $K$ is a field, $R[x]$ is the polynomial ring in one indeterminate and $R[x_1,\ldots,x_n]$ the polynomial ring in $n$ indeterminates; $K(x)$ is the field of rational functions, the fraction field of $K[x]$; and $\deg f$, $\operatorname{lc}(f)$ and $\operatorname{cont}(f)$ are the degree, the leading coefficient and the content.

---

## The Polynomial Ring

### The Universal Property

**Definition.** For a commutative ring $R$ the **polynomial ring** $R[x]$ is the set of formal sums $\sum_{k\geq0}a_kx^k$ with $a_k \in R$ and $a_k = 0$ for all but finitely many $k$, with the termwise addition and the multiplication given by the Cauchy rule $\left(\sum a_ix^i\right)\left(\sum b_jx^j\right) = \sum_k\left(\sum_{i+j=k}a_ib_j\right)x^k$. The **degree** of a nonzero polynomial is the largest $k$ with $a_k \neq 0$, and the **leading coefficient** is that $a_k$.

**Theorem (universal property).** Let $R$ be commutative, $S$ a commutative ring and $\varphi : R \to S$ a ring homomorphism. Then for every $s \in S$ there is exactly one ring homomorphism $\Phi : R[x] \to S$ with $\Phi(x) = s$ and $\Phi|_R = \varphi$, given by $\Phi(\sum a_kx^k) = \sum\varphi(a_k)s^k$. In particular the evaluation maps $\operatorname{ev}_s : R[x] \to R$ are the heart of the theory: a polynomial is determined by the functor it induces on the category of commutative $R$-rings.

**Proof.** Existence and uniqueness are checked on monomials, where the value of $\Phi$ is forced, and the Cauchy rule is exactly what makes $\Phi$ multiplicative. $\square$

**Theorem (elementary arithmetic).** Let $R$ be commutative.

**(a)** $\deg(fg) \leq \deg f+\deg g$, with equality when $\operatorname{lc}(f)$ or $\operatorname{lc}(g)$ is a nonzerodivisor; if $R$ is an integral domain, $R[x]$ is an integral domain and $\deg(fg) = \deg f+\deg g$.

**(b)** (division with remainder) If $g$ has invertible leading coefficient, then for every $f$ there are unique $q, r$ with $f = qg+r$ and $\deg r < \deg g$. Hence over a field $K[x]$ is a Euclidean domain with degree as Euclidean function, and a principal ideal domain and a unique factorisation domain.

**(c)** (Hilbert basis theorem) If $R$ is Noetherian, then $R[x]$ is Noetherian, and by induction $R[x_1,\ldots,x_n]$ is Noetherian.

**Proof sketch.** (a) and (b) are direct from the Cauchy rule and the leading terms; (c) is the content of *Noetherian and Artinian Rings*, proved by the leading-coefficient ideal argument. $\square$

**Example.** Over $\mathbb{Z}$: $2x+2$ and $2x^2+2x$ have product $4x^3+8x^2+4x$, of degree $3 = 1+2$; the leading coefficients $2, 2$ are nonzero but not invertible, and division by $2x$ is impossible without inverting $2$, in accordance with (b). Over $\mathbb{F}_2$: $x^2+x = x(x+1)$ and $x^3+x = x(x+1)^2$, and division is always possible by any nonzero polynomial.

### Polynomials as Functions

**Theorem (Lagrange interpolation).** Let $K$ be a field, $a_1,\ldots,a_m$ distinct elements of $K$ and $b_1,\ldots,b_m \in K$. Then there is exactly one polynomial $f \in K[x]$ of degree $< m$ with $f(a_i) = b_i$ for all $i$, namely

$$
f(x) = \sum_{i=1}^{m}b_i\prod_{j\neq i}\frac{x-a_j}{a_i-a_j}.
$$

**Proof.** Each summand $\prod_{j\neq i}(x-a_j)/(a_i-a_j)$ takes the value $1$ at $a_i$ and $0$ at the other $a_j$, so the sum interpolates. Uniqueness holds because a nonzero polynomial of degree $< m$ has at most $m-1$ roots, and a polynomial of degree $< m$ vanishing at $m$ points is zero, by the root theorem of *Integral Domains*. $\square$

**Example.** For the points $(0,1), (1,2), (2,5)$: the interpolating polynomial is $\frac{(x-1)(x-2)}{2}+\frac{2x(x-2)}{-1}+\frac{5x(x-1)}{2} = x^2+1$, and the values $1,2,5,17,10$ at $0,1,2,4,-3$ agree with $x^2+1$ at each, as verified by substitution.

**Theorem (polynomials versus polynomial functions).** If $R$ is an infinite integral domain, the map $R[x] \to R^R$ sending a polynomial to its evaluation function is injective. If $R$ is finite, it is not: over a finite field $\mathbb{F}_q$ the polynomial $x^q-x$ vanishes at every element, and the map $\mathbb{F}_q[x] \to \mathbb{F}_q^{\mathbb{F}_q}$ has kernel the ideal generated by $x^q-x$, so distinct polynomials may define the same function.

**Proof.** A nonzero polynomial over an infinite integral domain has finitely many roots, so it cannot vanish at every point; over $\mathbb{F}_q$ the group $\mathbb{F}_q^\times$ has order $q-1$, so every nonzero element satisfies $x^{q-1} = 1$, hence $\mathbb{F}_q[x]/(x^q-x)$ is a ring of $q^q$ elements which surjects onto the ring of all functions from $\mathbb{F}_q$ to itself, of the same cardinality $q^q$; the surjection is therefore an isomorphism, by the counting theorem of *Finite Fields*. $\square$

### Contents and Gauss's Lemma

**Definition.** For $R$ a unique factorisation domain and $f \in R[x]$ the **content** $\operatorname{cont}(f)$ is the greatest common divisor of the coefficients, and $f$ is **primitive** if its content is a unit.

**Theorem (Gauss).** Let $R$ be a unique factorisation domain and let $K$ be its fraction field.

**(a)** The product of primitive polynomials is primitive.

**(b)** $f \in R[x]$ is irreducible in $R[x]$ and primitive if and only if it is irreducible in $K[x]$; consequently $R[x]$ is a unique factorisation domain, and so is $R[x_1,\ldots,x_n]$.

**Proof sketch.** (a) If $p$ is a prime dividing all coefficients of $fg$, then reducing modulo $p$ gives $\bar f\bar g = 0$ in $(R/pR)[x]$, a domain, so $p$ divides all coefficients of $f$ or all of $g$. (b) If $f = gh$ in $K[x]$, clearing denominators and extracting contents writes $f$ as a product of primitive polynomials in $R[x]$ up to a unit, and (a) controls the contents; the rest is the lifting of a factorisation from $K[x]$ to $R[x]$. $\square$

**Example.** $2x^2+2 = 2(x^2+1)$ in $\mathbb{Z}[x]$: the content is $2$, and $x^2+1$ is primitive and irreducible in $\mathbb{Q}[x]$, so $2x^2+2$ factors in $\mathbb{Z}[x]$ only through its content, as Gauss's lemma asserts. The polynomials $x^2-2$ and $x^2-4x+2$ are irreducible in $\mathbb{Z}[x]$ and in $\mathbb{Q}[x]$ alike; the **rational root theorem** is the special case of (b) at degree $2$ and $3$, and in general it states that a rational root of a primitive polynomial is a quotient of a divisor of the constant term by a divisor of the leading coefficient.

---

## Rational Functions

### The Fraction Field

**Definition.** For a field $K$ the **field of rational functions** $K(x)$ is the fraction field of $K[x]$, whose elements are the classes of quotients $f/g$ with $g \neq 0$; for $R$ an integral domain the fraction field of $R[x]$ is $\operatorname{Frac}(R)(x)$, and the formation of fractions commutes with the formation of polynomials: $\operatorname{Frac}(R[x]) \cong \operatorname{Frac}(R)(x)$.

**Theorem (degree as a valuation).** Let $K$ be a field and define $\nu(f/g) = \deg f-\deg g$ for $f,g \in K[x]$, $g \neq 0$. Then $\nu$ is a well-defined map $K(x)^\times \to \mathbb{Z}$ with $\nu(uv) = \nu(u)+\nu(v)$ and $\nu(u+v) \geq \min(\nu(u),\nu(v))$, equal to the minimum unless $\nu(u) = \nu(v)$; moreover $\nu$ is the valuation of $K(x)$ at the point at infinity, and its residue field is $K$. The associated absolute value and the completion of $K(x)$ with respect to it — the field of formal Laurent series — belong and to Part II, where the topological language is available.

**Proof.** The degree is additive on products of polynomials and subadditive on sums, and these properties descend to fractions. $\square$

**Theorem (Lüroth).** Let $K$ be a field and let $L$ be a field with $K \subseteq L \subseteq K(x)$. Then $L = K(\varphi)$ for some $\varphi \in K(x)$; in particular $L$ is either $K$ or a rational function field in one variable over $K$.

**Proof sketch.** Writing $\varphi = f/g$ in lowest terms and using the degree $\max(\deg f,\deg g) = [K(x):K(\varphi)]$, one shows that if $L \supsetneq K$ contains an element $\varphi$ of minimal degree, then $L = K(\varphi)$; any $\psi \in L$ is algebraic over $K(\varphi)$, and the degree estimate forces it to lie in $K(\varphi)$. $\square$

**Example.** In $\mathbb{R}(x)$ the subfield $\mathbb{R}(x^2)$, consisting of the rational functions even in $x$, is a rational function field in one variable with $[\,\mathbb{R}(x):\mathbb{R}(x^2)\,] = 2$: the element $x$ satisfies the quadratic $T^2-x^2$ over $\mathbb{R}(x^2)$. Likewise $\mathbb{R}(x^3+x)$ is a proper intermediate field with $[\,\mathbb{R}(x):\mathbb{R}(x^3+x)\,] = 3$, since $x$ satisfies $T^3+T-(x^3+x)$.

### Partial Fractions

**Theorem (partial fractions).** Let $K$ be a field, $f, g \in K[x]$ with $g \neq 0$ and with factorisation into pairwise coprime powers $g = g_1^{e_1}\cdots g_r^{e_r}$. Then there are polynomials $p_i$, with $\deg p_i < e_i\deg g_i$, and a polynomial part $p$, unique, with

$$
\frac{f}{g} = p + \sum_{i=1}^{r}\frac{p_i}{g_i^{e_i}} ,
$$

and if $g_i$ is linear, say $g_i = x-a_i$, each summand has the form $\sum_{j=1}^{e_i}c_{ij}/(x-a_i)^j$ with $c_{ij} \in K$.

**Proof.** The Chinese remainder theorem for the coprime moduli $g_i^{e_i}$ identifies $K[x]/(g)$ with the product $\prod_iK[x]/(g_i^{e_i})$, so the class of $f$ is a sum of classes $p_i$ with the stated degree bounds; subtract the corresponding fractions from $f/g$ and the remaining fraction has numerator divisible by $g$, which is the polynomial part $p$, of degree $\deg f-\deg g$ when $\deg f \geq \deg g$. $\square$

**Example.** In $\mathbb{Q}(x)$: the function $\frac{x^3+1}{x(x^2+1)}$ has partial fraction decomposition

$$
\frac{x^3+1}{x(x^2+1)} = 1+\frac{1}{x}-\frac{x+1}{x^2+1},
$$

as is checked by putting the right side over the common denominator $x(x^2+1)$: the numerator becomes $x(x^2+1)+x^2+1-x(x+1) = x^3+x+x^2+1-x^2-x = x^3+1$. The polynomial part is $1$, of degree $\deg(x^3+1)-3 = 0$, and the two proper summands are attached to the coprime moduli $x$ and $x^2+1$. The verification is exact over $\mathbb{Q}$: substituting $x = 2,3,-5,\tfrac72,11$ gives equality of rational numbers at every value.

**Corollary (Hermite interpolation).** Given distinct $a_1,\ldots,a_m \in K$ and prescribed values of a rational function and of its divided differences at the $a_i$ up to order $e_i-1$, there is a unique rational function with denominator $\prod(x-a_i)^{e_i}$ realising them, obtained from the partial fraction decomposition by solving for the coefficients $c_{ij}$. The case $e_i = 1$ for all $i$ is Lagrange interpolation.

---

## Applications

### Resultants and Discriminants

**Definition.** For $f = a_mx^m+\cdots+a_0$ and $g = b_nx^n+\cdots+b_0$ the **resultant** $\operatorname{Res}(f,g)$ is the determinant of the $(m+n)\times(m+n)$ Sylvester matrix of the two coefficient vectors; the **discriminant** of $f$ of degree $m$ with leading coefficient $a_m$ is $\operatorname{Disc}(f) = (-1)^{m(m-1)/2}a_m^{-1}\operatorname{Res}(f,f')$.

**Theorem.** Over a field, $\operatorname{Res}(f,g) = 0$ if and only if $f$ and $g$ have a common root in an algebraic closure, and $\operatorname{Disc}(f) = 0$ if and only if $f$ has a multiple root; moreover for a monic $f$ of degree $m$ with roots $\alpha_1,\ldots,\alpha_m$ in a splitting field, $\operatorname{Disc}(f) = \prod_{i<j}(\alpha_i-\alpha_j)^2$, a square in the coefficient field, which is why the Galois group of a separable polynomial lies in the alternating group exactly when the discriminant is a square, as used in *The Inverse Galois Problem*.

**Example.** For $f = x^3-3x+1$ the Sylvester determinant of $f$ and $f' = 3x^2-3$ is $-81$, and the normalisation above gives $\operatorname{Disc}(f) = (-1)^{3}\cdot(-81) = 81$, a square with root $9 \in \mathbb{Q}$; in agreement, the polynomial has three real roots and its Galois group is $\mathbb{Z}/3\mathbb{Z}$. The elimination-theoretic computation of such resultants, and Gröbner-basis methods in several variables, are *Gröbner Bases and Elimination Theory*.

### Polynomial Rings and Their Quotients

**Theorem (quotients by principal ideals).** Let $K$ be a field and $f \in K[x]$ of degree $m$.

**(a)** $K[x]/(f)$ is a $K$-vector space of dimension $m$, with basis the classes of $1,x,\ldots,x^{m-1}$, and it is a field if and only if $f$ is irreducible.

**(b)** If $f = f_1^{e_1}\cdots f_r^{e_r}$ with the $f_i$ irreducible, distinct and pairwise coprime, then $K[x]/(f) \cong \prod_iK[x]/(f_i^{e_i})$, a product of local rings, and $K[x]/(f)$ is a product of fields exactly when $f$ is squarefree, that is, when $\gcd(f,f') = 1$.

**Proof.** (a) is the dimension count for the remainder representation and the standard criterion for a quotient by a maximal ideal; (b) is the Chinese remainder theorem of *Localization and the Fraction Field* and *Rings*, together with the fact that $K[x]/(f_i^{e_i})$ is local with maximal ideal $(f_i)$ and that $f$ is squarefree exactly when no $f_i^2$ divides it. $\square$

**Example.** $\mathbb{R}[x]/(x^2+1) \cong \mathbb{C}$, of dimension $2$; $\mathbb{R}[x]/(x^2-1) \cong \mathbb{R}\times\mathbb{R}$ by the Chinese remainder theorem, with factors corresponding to the two roots; $\mathbb{F}_2[x]/(x^3+x+1)$ is a field of $8$ elements, since $x^3+x+1$ has no root in $\mathbb{F}_2$ and degree $3$. The last example is the construction of the fields used.

**Theorem (evaluation).** Let $K$ be a field and $S \subseteq K$ a set of $n$ distinct elements. Then the evaluation map $K[x]_{<k} \to K^S$, $f \mapsto (f(s))_{s\in S}$, is injective for $k \leq n$ and is an isomorphism for $k = n$; for $k \leq n$ its image is a subspace of $K^S$ of dimension $k$ in which any two distinct elements differ in at least $n-k+1$ coordinates, since a nonzero polynomial of degree $<k$ has at most $k-1$ roots. This is the algebraic fact behind the Reed–Solomon codes; the codes themselves and their parameters are.

**Proof.** Injectivity is the root bound; the dimension count follows, and the coordinate-difference statement is the same root bound applied to the difference. $\square$

---

## Summary

The polynomial ring $R[x]$ is the free commutative $R$-ring on one generator: for every $s$ in a commutative $R$-ring $S$ there is exactly one homomorphism $R[x] \to S$ with $x \mapsto s$. Its arithmetic is controlled by the degree, which is additive on products over an integral domain and which makes $K[x]$ a Euclidean domain, hence a principal ideal domain and a unique factorisation domain; over a Noetherian ring it is again Noetherian by the Hilbert basis theorem, so that $R[x_1,\ldots,x_n]$ is Noetherian. Content and Gauss's lemma transfer factorisation between $R[x]$ and the fraction field $\operatorname{Frac}(R)(x)$, and the rational root theorem is the degree-two and degree-three case of the same transfer. Polynomials and polynomial functions part company only over finite rings: over a finite field the kernel of evaluation is the ideal generated by $x^q-x$.

The fraction field $K(x)$ is the rational function field, and the degree difference is a valuation on it, the valuation at infinity, whose completion belongs to Part II. Lüroth's theorem states that every intermediate field $K \subseteq L \subseteq K(x)$ is generated by one element, so that such an $L$ is again a rational function field. Partial fractions are the Chinese remainder decomposition of an element of $K(x)$ along the coprime factors of its denominator, and they yield the Hermite interpolation theorem, of which Lagrange interpolation is the case of simple factors. The applications follow the same circle of ideas: resultants and discriminants decide common roots and multiple roots and compute the square-root criterion for membership in the alternating group; the quotient $K[x]/(f)$ is a product of fields exactly when $f$ is squarefree, and is a field when $f$ is irreducible, giving the finite fields; and the evaluation map $K[x]_{<k} \to K^S$ is the algebraic source of the Reed–Solomon codes, its injectivity being the root bound.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with $1 \neq 0$ |
| $K$ | Field, usually the fraction field of $R$ |
| $R[x]$, $R[x_1,\ldots,x_n]$ | Polynomial rings in one and in $n$ indeterminates |
| $K(x)$ | Field of rational functions |
| $\deg f$, $\operatorname{lc}(f)$ | Degree and leading coefficient |
| $\operatorname{cont}(f)$ | Content of a polynomial over a unique factorisation domain |
| $\operatorname{ev}_s$ | Evaluation at $s$ |
| $\operatorname{Res}(f,g)$ | Resultant, determinant of the Sylvester matrix |
| $\operatorname{Disc}(f)$ | Discriminant |
| $\nu$ | The valuation $\deg f-\deg g$ at infinity |
| $K[x]_{<k}$ | Polynomials of degree less than $k$ |
| $K^S$ | Functions from $S$ to $K$ |



## Further Reading

- Serge Lang, *Algebra* (Springer, revised 3rd ed. 2002), for the universal property, Gauss's lemma and the arithmetic of polynomial rings.
- B. L. van der Waerden, *Moderne Algebra* (Springer, 1930–1931), for the classical development of polynomial arithmetic and Lüroth's theorem.
- Bartel Leendert van der Waerden, *Algebra*, Volume 1 (Springer, 1991), for the elementary theory with the division and Euclidean algorithms.
- Oskar Perron, *Algebra I* (de Gruyter, 1927), for resultants, discriminants and elimination in the classical style.
- Jacob Lüroth, "Beweis eines Satzes über rationale Curven", *Mathematische Annalen* 9 (1875), 163–165, for the rationality theorem.
- Richard P. Stanley, *Enumerative Combinatorics*, Volume 1 (Cambridge University Press, 2nd ed. 2012), for the combinatorics of polynomial rings and symmetric functions.
- Rudolf Lidl and Harald Niederreiter, *Finite Fields* (Cambridge University Press, 2nd ed. 1997), for quotients of $K[x]$ and the evaluation codes.
- F. S. Macaulay, *The Algebraic Theory of Modular Systems* (Cambridge University Press, 1916), for the elimination-theoretic uses of polynomial rings.
