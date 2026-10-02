# __The Hochschild Differential as an Operator__

## Introduction

A cochain complex is a graded module with an operator of degree one whose square is zero, and the first cochain complex that an algebra produces from itself is the **Hochschild complex**. Its cochains are the multilinear maps on the algebra with values in a bimodule, and its operator is the **Hochschild differential** $b$, the alternating sum of the ways of multiplying the arguments together and acting on the value. The whole content of the complex is two properties of this single operator: it is $k$-linear of degree one, and its square is zero.

This article studies the differential as an operator. It fixes the cochain module, defines $b$ on it, proves $b^2 = 0$ by a cancellation of the twelve terms, and reads the consequence — the cocycles, the coboundaries and the cohomology — as the kernel, the image and the quotient of the operator. The cohomology itself, its identification with the derived functors of the invariants, its low-dimensional interpretations and its products are the subject of *Hochschild Homology*, and the general theory of a cochain complex, its differential and its cohomology belongs to *Homological Algebra*; the present article is the operator layer of the first and cites the second for the ambient theory.

Throughout, $k$ is a commutative ring with identity $1 \neq 0$, $A$ is a unital associative $k$-algebra, not necessarily commutative, and $M$ is an $A$-bimodule. The tensor powers are over $k$, and $\operatorname{Hom}$ without a subscript means $\operatorname{Hom}_k$; the enveloping algebra is $A^{\mathrm{e}} = A \otimes_k A^{\mathrm{op}}$, so that $A$-bimodules are the left $A^{\mathrm{e}}$-modules. No norm, distance or completion occurs.

## The Cochain Module

### Definition

**Definition.** For $n \geq 0$ the module of **$n$-cochains** of $A$ with coefficients in $M$ is

$$
C^n(A, M) = \operatorname{Hom}_k(A^{\otimes n}, M),
$$

the $k$-module of $k$-multilinear maps $f : A^n \to M$. For $n = 0$ the empty tensor power is $A^{\otimes 0} = k$, so that $C^0(A,M) = \operatorname{Hom}_k(k, M) \cong M$; the element of $M$ corresponding to a $0$-cochain is written $m$, and the map is $k \mapsto km$.

The **Hochschild cochain module** is the graded module

$$
C^{\bullet}(A, M) = \bigoplus_{n \geq 0} C^n(A, M).
$$

An element of $C^\bullet(A,M)$ is a finite sequence $f = (f_0, f_1, f_2, \dots)$ with $f_n \in C^n(A,M)$ and $f_n = 0$ for all but finitely many $n$; the module is graded, and a single $n$-cochain is homogeneous of degree $n$.

### The Bimodule Structure

The cochain module carries more than its $k$-module structure, and the extra structure is what makes the differential a map of the right kind.

**Proposition.** For $a \in A$ and $f \in C^n(A,M)$ the assignments

$$
(af)(a_1,\dots,a_n) = a\,f(a_1,\dots,a_n), \qquad (fa)(a_1,\dots,a_n) = f(a_1,\dots,a_n)\,a
$$

turn $C^n(A,M)$ into an $A$-bimodule, and the same formulas turn $C^{\bullet}(A,M)$ into a graded $A$-bimodule: the two actions commute, each is $k$-linear in $f$, and $C^{\bullet}(A,M)$ is a left module over the enveloping algebra $A^{\mathrm{e}}$.

*Proof.* The module $M$ is an $A$-bimodule, so its left and right actions commute; applying them pointwise to the values of $f$ gives two actions on $C^n(A,M)$ that are $k$-linear in $f$ and commute. A left $A$-module that is also a right $A$-module with commuting actions is a left $A^{\mathrm{e}}$-module by $(a \otimes a') \cdot f = a f a'$, and the grading is preserved because the actions do not change the number of arguments.

**Remark.** The cochain module is therefore not merely a graded $k$-module but a graded $A^{\mathrm{e}}$-module, and a differential of the theory is required to commute with this action. The Hochschild differential below does; this is the operator form of the statement that the Hochschild complex is a complex of $A^{\mathrm{e}}$-modules and not only of $k$-modules.

## The Differential

### Definition

**Definition.** The **Hochschild differential** is the family of $k$-linear maps

$$
b = b_n : C^n(A, M) \longrightarrow C^{n+1}(A, M), \qquad n \geq 0,
$$

given on $f \in C^n(A,M)$ and $a_0, \dots, a_n \in A$ by

$$
(b f)(a_0, \dots, a_n) = a_0 f(a_1, \dots, a_n) + \sum_{i=1}^{n} (-1)^i f(a_0, \dots, a_{i-1}a_i, \dots, a_n) + (-1)^{n+1} f(a_0, \dots, a_{n-1})\, a_n .
$$

The definition is $k$-multilinear in the arguments, so the value on $f$ is an $(n+1)$-cochain; the formula is the alternating sum of the $n+2$ ways of inserting the product of two adjacent arguments, with the two end terms acting on the value in $M$ instead of multiplying two arguments together. The family $b = (b_n)$ is also written $\delta$ when the cochain reading is to be distinguished from the chain boundary of *Hochschild Homology*.

### Low Degrees

The formula is best read in low degrees, where the operator acquires its meaning.

**Degree zero.** Here $n = 0$ and $f = m \in M$; the sum is empty and only the two end terms survive:

$$
(b m)(a_0) = a_0 m - m a_0 .
$$

So $b : M \to \operatorname{Hom}_k(A, M)$ sends an element of the bimodule to the operator $a \mapsto am - ma$, the **inner multiplication** of the bimodule. Its kernel is the invariant submodule $M^A$.

**Degree one.** Here $f \in \operatorname{Hom}_k(A, M)$ and

$$
(b f)(a_0, a_1) = a_0 f(a_1) - f(a_0 a_1) + f(a_0) a_1 .
$$

This is the operator form of the Leibniz rule: $b f = 0$ is exactly the statement that $f$ is a **derivation** $A \to M$.

**Degree two.** Here $g \in \operatorname{Hom}_k(A^{\otimes 2}, M)$ and

$$
(b g)(a_0, a_1, a_2) = a_0 g(a_1, a_2) - g(a_0 a_1, a_2) + g(a_0, a_1 a_2) - g(a_0, a_1) a_2 .
$$

The alternating pattern of signs is visible: $-, +, -$ on the inner terms and $+$ then $-$ on the two end terms.

### The Square-Zero Property

**Theorem.** The Hochschild differential satisfies

$$
b \circ b = 0, \qquad \text{that is} \qquad b_{n+1} b_n = 0 \quad \text{for every } n \geq 0 .
$$

*Proof.* Fix $f \in C^n(A,M)$ and arguments $a_0, \dots, a_{n+1}$. The cochain $b f$ is a sum of $n+2$ terms, each of which is the value of $f$ at an $(n+1)$-tuple together with a product of two adjacent arguments contracted or an end action applied; the differential $b(bf)$ is the alternating sum over the $n+3$ positions of $(b f)$ of the same operation. Expand: the double sum ranges over the pairs $(i,j)$ with $0 \leq i < j \leq n+1$, where $i$ is the position contracted in the inner application and $j$ that contracted in the outer one; each pair $(i,j)$ arises in exactly two ways, once by contracting $a_i a_{i+1}$ first and then the resulting adjacent product with $a_{i+2}$, and once by contracting $a_{i+1}a_{i+2}$ first and then $a_i$ with the result. The two contributions are equal as values of $f$ — both amount to the single value $f(\dots, a_i a_{i+1} a_{i+2}, \dots)$ — and their coefficients in the alternating sum are $(-1)^i(-1)^{j-1}$ and $(-1)^{i+1}(-1)^j$, which are opposite. The two end terms are paired with the contractions at the ends in the same way, and every remaining term cancels; hence $b^2 f = 0$.

**Corollary.** The pair $(C^{\bullet}(A,M), b)$ is a **cochain complex**: the image of $b_n$ is contained in the kernel of $b_{n+1}$,

$$
\operatorname{im} b_n \;\subseteq\; \ker b_{n+1} .
$$

The corollary is the definition of a cochain complex in *Homological Algebra*, and the two properties that make the pair one — $b$ of degree one and $b^2 = 0$ — are exactly the two properties proved above.

### Naturality and the Bimodule Action

**Proposition.** The differential $b$ is natural in $A$ and in $M$, and it commutes with the $A^{\mathrm{e}}$-action on the cochains: for $a, a' \in A$ and $f \in C^n(A,M)$,

$$
b(a f a') = a\, (bf)\, a' .
$$

*Proof.* Naturality in $M$ is the observation that every term of the formula uses only the bimodule operations and evaluates $f$, so a bimodule map $M \to M'$ carries $bf$ to $b(f')$ where $f'$ is the composite. For the action, multiply the defining formula on the left by $a$ and on the right by $a'$; the two end terms acquire $a a_0 f(\dots) a'$ and $a f(\dots) a_n a'$, which are the end terms of $b(a f a')$, and the inner terms acquire $a f(\dots) a'$ at each contracted position, which are the corresponding inner terms.

**Corollary.** The Hochschild complex is a complex of $A^{\mathrm{e}}$-modules: the differential is $A^{\mathrm{e}}$-linear, and so the kernels, the images and the cohomology $H^{\bullet}(A,M)$ carry $A^{\mathrm{e}}$-module structures.

## Cocycles, Coboundaries and Cohomology

### The Definitions

**Definition.** Let $Z^n(A,M) = \ker b_n$ be the module of **$n$-cocycles** and let $B^n(A,M) = \operatorname{im} b_{n-1}$ be the module of **$n$-coboundaries**, with the convention $B^0(A,M) = 0$. Because $b^2 = 0$, one has $B^n \subseteq Z^n$, and the **Hochschild cohomology** is the graded quotient

$$
H^n(A, M) = Z^n(A, M) / B^n(A, M), \qquad n \geq 0 .
$$

The definitions are those of a cochain complex, and they are the reason the square-zero property is worth proving: without it the quotient would not be defined.

### The Low-Dimensional Reading

**Proposition.** The low-dimensional modules of the Hochschild complex are

$$
H^0(A,M) = M^A, \qquad H^1(A,M) = \operatorname{Der}_k(A,M) / \operatorname{InnDer}_k(A,M), \qquad H^2(A,M) = \text{the abelian extensions up to equivalence},
$$

where $M^A = \{m : am = ma\}$ is the invariant submodule, $\operatorname{Der}_k(A,M)$ is the module of $k$-linear maps satisfying the Leibniz rule, and $\operatorname{InnDer}_k(A,M)$ is the submodule of inner derivations $a \mapsto am - ma$.

*Proof.* The degree-zero statement is the computation $b m = 0 \iff am = ma$ for all $a$. The degree-one statement is the identification of the kernel of $b_1$ with the derivations, by the degree-one formula, and of the image of $b_0$ with the inner derivations. The degree-two statement is the interpretation of the second cohomology of the Hochschild complex as the group of abelian extensions of $A$ by $M$; it is the classical interpretation of the Hochschild theory and belongs, with its proof, to *Hochschild Homology*.

**Remark.** The identifications with the derived functors — $H^n(A,M) \cong \operatorname{Ext}^n_{A^{\mathrm{e}}}(A,M)$ — and the products on the cohomology are not developed here. The present article owns only the operator: the differential, its degree, its square-zero property, and the complex and the cohomology that these define. The reader who needs the derived-functor theory, the Hochschild–Kostant–Rosenberg theorem, the cup product or the Gerstenhaber bracket is directed to *Hochschild Homology*.

## The Differential as an Operator

### Degree and Square

The differential is an operator on a graded module, and its two defining properties are statements about that grading.

**Proposition.** With respect to the grading $C^{\bullet}(A,M) = \bigoplus_n C^n(A,M)$ the differential has **degree one**, $b(C^n) \subseteq C^{n+1}$, and its square is zero, $b^2 = 0$. Conversely a $k$-linear map of degree one with square zero on a graded module is exactly a differential of a cochain complex.

*Proof.* The first statement is the definition: $b$ raises the number of arguments by one. The second is the theorem. The converse is the definition of a cochain complex in *Homological Algebra*.

### The Shift

The differential is a morphism of graded modules from the complex to its shift.

**Proposition.** Let $C^{\bullet}[1]$ be the graded module with $C^{\bullet}[1]^n = C^{n+1}$. Then $b$ is a morphism of graded $A^{\mathrm{e}}$-modules $C^{\bullet} \to C^{\bullet}[1]$, and the condition $b^2 = 0$ is the statement that the composite

$$
C^{\bullet} \xrightarrow{\;b\;} C^{\bullet}[1] \xrightarrow{\;b\;} C^{\bullet}[2]
$$

is zero.

*Proof.* The first statement restates the degree of $b$ and its $A^{\mathrm{e}}$-linearity. For the second, $b^2$ as a map $C^n \to C^{n+2}$ is $b_{n+1}b_n$, zero by the theorem.

### The Transpose Relation

The differential of the cochain complex is the transpose of the boundary of the chain complex, and the two readings of the algebra are dual.

**Proposition.** Let $B_\bullet(A)$ be the bar resolution of *Hochschild Homology*, with boundary $b^{\mathrm{chain}} : B_n(A) \to B_{n-1}(A)$. Then the Hochschild differential on the cochains is the transpose of the chain boundary under the pairing
$\operatorname{Hom}_k(B_n(A), M) \times B_n(A) \to M$,

$$
\langle b f, x \rangle = \langle f, b^{\mathrm{chain}} x \rangle .
$$

In particular the cochain differential is determined by the chain boundary and vice versa, and the cochain complex is the dual of the chain complex.

*Proof.* The bar resolution has $B_n(A) = A^{\otimes(n+2)}$ and the cochains are the $A^{\mathrm{e}}$-linear maps $B_n(A) \to M$, whose underlying $k$-linear maps are $\operatorname{Hom}_k(A^{\otimes n}, M)$; the transpose of the boundary is computed by evaluating the defining formula of *Hochschild Homology* against a cochain, and it gives the formula of the present article. The identification of the two sign conventions is the standard one for a chain complex and its dual.

**Remark.** The corollary is a statement about operators and not a new construction: the cochain differential and the chain boundary are one operator read on a module and on its dual. The reader should not take the two symbols $b$ of the two articles as two operators; they are transposes.

## The Algebra as Coefficients

### The Case $M = A$

The most used case is $M = A$, with the bimodule structure given by the product.

**Proposition.** For $M = A$ one has $H^0(A,A) = Z(A)$, the centre; $H^1(A,A) = \operatorname{Der}_k(A)/\operatorname{InnDer}_k(A)$, the space of **outer derivations**; and the degree-one cocycles are exactly the derivations of $A$.

*Proof.* The invariant submodule of $A$ under the bimodule structure $ama'$ is the set of $z$ with $az = za$ for all $a$, which is the centre. The degree-one statement is the low-dimensional proposition with $M = A$, and the inner derivations are the maps $a \mapsto am - ma$ with $m \in A$, which are the inner derivations $\mathrm{ad}_m$ of *The Commutator Operator*.

**Corollary.** The differential $b_0 : A \to \operatorname{Hom}_k(A,A)$ is the operator $m \mapsto \mathrm{ad}_m$, whose image is the space of inner derivations of *Automorphisms and Derivations of Algebras* and whose kernel is the centre. Hence $H^1(A,A)$ vanishes exactly when every derivation of $A$ is inner; in particular $H^1(M_n(k), M_n(k)) = 0$ over a field, because every derivation of the full matrix algebra is inner.

*Proof.* The identification $b_0(m) = \mathrm{ad}_m$ is the degree-zero computation. The vanishing for $M_n(k)$ is the statement of *Automorphisms and Derivations of Algebras* that every derivation of a central simple algebra is inner.

## The Examples

### A Commutative Algebra

Let $A$ be commutative and let $M = A$ with the product bimodule structure. Then the invariant submodule $M^A$ is all of $A$, so $H^0(A,A) = A$; the inner derivations vanish, so $H^1(A,A) = \operatorname{Der}_k(A)$ is the whole module of derivations; and the differential $b_0$ is the zero operator. The centre is the whole algebra, and the operator $b_0$ is identically zero, which is the operator form of the commutativity of $A$.

### The Polynomial Algebra

Let $A = k[x]$ and $M = A$. A derivation is determined by its value $f = D(x) \in k[x]$, since the Leibniz rule gives $D(p) = p' f$ for the formal derivative $p'$; the module of derivations is free of rank one on $D_0 = \frac{d}{dx}$, and $H^1(k[x], k[x]) = k[x] \cdot \frac{d}{dx}$. The differential $b_1$ sends a derivation to $0$ and the inner derivations form the zero submodule, so the first cohomology is the whole derivation module. This is the smallest nonvanishing example, and the Hochschild–Kostant–Rosenberg theorem of *Hochschild Homology* is the general statement behind it.

### The Algebra of Dual Numbers

Let $A = k[\varepsilon]/(\varepsilon^2)$ and $M = A$. The derivations are the maps with $D(\varepsilon) = c + d\varepsilon$ subject to $2\varepsilon D(\varepsilon) = 0$, so $D(\varepsilon) = c$ is a scalar and the derivation module has dimension one over $k$; the inner derivations are again the zero submodule, because $A$ is commutative, and $H^1(A,A)$ has dimension one. The degree-one differential $b_1$ therefore has a one-dimensional kernel and, since $b_2 b_1 = 0$, the image of $b_1$ lies in the degree-two cocycles; the operator picture is the short exact sequence of the complex in low degree.

## Summary

The Hochschild cochains are the multilinear maps $C^n(A,M) = \operatorname{Hom}_k(A^{\otimes n},M)$, assembled into the graded $A^{\mathrm{e}}$-module $C^{\bullet}(A,M)$, and the **Hochschild differential** $b$ is the degree-one operator

$$
(b f)(a_0,\dots,a_n) = a_0 f(a_1,\dots,a_n) + \sum_{i=1}^{n}(-1)^i f(a_0,\dots,a_{i-1}a_i,\dots,a_n) + (-1)^{n+1}f(a_0,\dots,a_{n-1})a_n .
$$

In low degrees it is $b m = (a \mapsto am - ma)$ on $M$, the Leibniz operator $b f(a_0,a_1) = a_0 f(a_1) - f(a_0a_1) + f(a_0)a_1$ on the linear maps, and the three-term alternating operator on the bilinear maps. The square-zero property $b^2 = 0$ holds, by the cancellation of the twelve terms of the double sum; it makes $(C^{\bullet}(A,M), b)$ a cochain complex, and it makes the quotient $H^n(A,M) = \ker b_n / \operatorname{im} b_{n-1}$ defined. The differential commutes with the $A^{\mathrm{e}}$-action, has degree one, is the transpose of the chain boundary of *Hochschild Homology*, and its kernel and image reproduce the low-dimensional theory: $H^0(A,M) = M^A$, $H^1(A,M)$ is the module of derivations modulo the inner ones, and $H^2(A,M)$ classifies the abelian extensions. For $M = A$ the degree-zero differential is $m \mapsto \mathrm{ad}_m$, with kernel the centre and image the inner derivations, so $H^1(A,A)$ is the space of outer derivations and vanishes for a central simple algebra. The cohomology's derived-functor description, its products and its theorems are the subject of *Hochschild Homology*; the complex and the differential as an operator are the subject of this article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the commutative base ring |
| $A$ | a unital associative $k$-algebra |
| $M$ | an $A$-bimodule |
| $A^{\mathrm{e}} = A \otimes_k A^{\mathrm{op}}$ | the enveloping algebra |
| $C^n(A,M) = \operatorname{Hom}_k(A^{\otimes n},M)$ | the $n$-cochains |
| $C^{\bullet}(A,M)$ | the graded cochain module |
| $b = b_n : C^n \to C^{n+1}$ | the Hochschild differential |
| $Z^n = \ker b_n$ | the $n$-cocycles |
| $B^n = \operatorname{im} b_{n-1}$ | the $n$-coboundaries |
| $H^n(A,M) = Z^n/B^n$ | the Hochschild cohomology |
| $b^{\mathrm{chain}} : B_n(A) \to B_{n-1}(A)$ | the chain boundary of the bar resolution |
| $\operatorname{Der}_k(A,M)$, $\operatorname{InnDer}_k(A,M)$ | derivations and inner derivations |

## Further Reading

- Sarah J. Witherspoon, *Hochschild Cohomology for Algebras* (American Mathematical Society, 2019), for the differential, the complex and the whole cohomology theory.
- Murray Gerstenhaber, "The cohomology structure of an associative ring", *Annals of Mathematics* 78 (1963), 267–288, for the differential and the brackets it carries.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for the general theory of cochain complexes, differentials and their cohomology.
- Henri Cartan and Samuel Eilenberg, *Homological Algebra* (Princeton University Press, 1956), for the Hochschild complex as the standard complex of an algebra.
