# __Involutions of a Free Algebra__

## Introduction

A free algebra has no relations, so an involution of it is a map that has nowhere to hide: it is determined by what it does to the generators, and the only obstruction to its existence is the order-two condition. The free algebra on a set carries one canonical anti-involution that exists for every set, the **reversal of words**, which reads a word backwards; it carries also the involutive automorphisms given by signs and permutations of the generators. Every involutive quotient of a free algebra — the polynomial algebra, the exterior algebra, the group algebra — inherits its involution from one of these by descent.

This article develops the free algebra, the reversal as its canonical anti-involution with its fixed and skew elements, the general anti-involution determined by the images of the generators and the condition for it to have order two, the involutive automorphisms determined by a signed permutation of the generators, and the descent to the quotients. The free algebra is the tensor algebra of the free linear space on the set, so the tensor-power theory is that of *Tensor Powers and the Free Algebra*, the induced reversal of the tensor algebra is that of *Involutions of the Tensor Algebra*, and the general theory of an involution on the elements is *Involutive Algebras*.

Throughout, $k$ is a field, $X$ is a set, and $F\langle X\rangle$ is the free associative $k$-algebra on $X$; its elements are the linear combinations of **words** in the elements of $X$, and a word is a finite sequence $x_1 x_2 \cdots x_n$ of generators. The free algebra is the tensor algebra of the free $k$-linear space with basis $X$, and the words of length $n$ span the $n$-th tensor power; the notation $F\langle X\rangle$ is that of *Tensor Powers and the Free Algebra*, and the modules and the ideals are those of *Modules over an Algebra* and *Ideals and Quotients of Algebras*.

## The Free Algebra

### Definition and Universal Property

**Definition.** The **free algebra** on $X$ over $k$ is the $k$-algebra $F\langle X\rangle$ whose underlying $k$-linear space has a basis the set of words in the elements of $X$, with the product given by concatenation of words and extended bilinearly; the empty word is the unit $1$.

**Theorem (universal property).** For every $k$-algebra $B$ and every map $X \to B$ there is a unique $k$-algebra homomorphism $F\langle X\rangle \to B$ extending it. In particular $F\langle X\rangle$ is the tensor algebra of the free space on $X$, and it is generated as an algebra by $X$.

*Proof.* A map on the generators determines the images of the words by multiplicativity, and the words span the algebra, so an extension is unique; the assignment $x_1\cdots x_n \mapsto f(x_1)\cdots f(x_n)$, extended linearly, is multiplicative and fixes the empty word, so it exists. The identification with the tensor algebra is the observation that the words of length $n$ are the basis of the $n$-th tensor power of the free space.

The property is the reason the free algebra is the domain of the anti-involutions: a map need only be specified on $X$, and the reversal, in particular, needs no data at all.

### The Grading and the Word Length

**Proposition.** The free algebra is graded by the word length, $F\langle X\rangle = \bigoplus_{n\geq0} F\langle X\rangle_n$, where $F\langle X\rangle_n$ is spanned by the words of length $n$; the product respects the grading, and the **grade involution** $\alpha$ acts by $\alpha(w) = (-1)^{|w|} w$ on a word $w$, where $|w|$ is its length. It is an algebra automorphism of order two.

*Proof.* The concatenation of a word of length $m$ and a word of length $n$ has length $m+n$, so the product respects the grading; the multiplicativity of $\alpha$ and $\alpha^2 = \mathrm{id}$ are the computation of *Involutions of the Tensor Algebra*.

## The Canonical Anti-Involution

### The Reversal of a Word

**Definition.** The **reversal** of a word $w = x_1 x_2 \cdots x_n$ is the word

$$
\mathrm{rev}(w) = x_n \cdots x_2 x_1, \qquad \mathrm{rev}(1) = 1,
$$

and the **reversal map** on $F\langle X\rangle$ is the linear extension of $\mathrm{rev}$ to the words. A word with $\mathrm{rev}(w) = w$ is a **palindrome**.

**Theorem.** The reversal is an anti-automorphism of $F\langle X\rangle$ of order two, hence an involution; it is the unique anti-automorphism fixing every generator, and it is the reversal involution $\theta_{\mathrm{id}}$ of *Involutions of the Tensor Algebra* for the identity involution of the space of generators. The free algebra therefore carries a canonical involution, independently of any choice on $X$.

*Proof.* For two words $u$ and $v$ one has $\mathrm{rev}(uv) = \mathrm{rev}(v)\mathrm{rev}(u)$, because reversing the concatenation reverses each factor and exchanges their order; the reversal fixes the empty word, so it extends to an anti-homomorphism, and it is bijective with inverse itself. It fixes every generator, and an anti-automorphism of $F\langle X\rangle$ fixing the generators is determined on them and hence everywhere by the universal property.

### The Fixed and the Skew Elements

**Proposition.** The reversal involution has fixed space spanned by the **palindromes** together with the sums $w + \mathrm{rev}(w)$ and skew part spanned by the differences $w - \mathrm{rev}(w)$; the underlying space decomposes as

$$
F\langle X\rangle = F\langle X\rangle^+ \oplus F\langle X\rangle^-, \qquad F\langle X\rangle^\pm = \{a : \mathrm{rev}(a) = \pm a\},
$$

and the fixed space is the span of the symmetric combinations and the skew space the span of the antisymmetric ones.

*Proof.* The map has order two, so its eigenvalues are $1$ and $-1$ and the space is the direct sum of the two eigenspaces, over a field of characteristic not two; a word is fixed exactly when it is a palindrome, and a word that is not a palindrome contributes the pair $w + \mathrm{rev}(w)$ to the fixed space and $w - \mathrm{rev}(w)$ to the skew space.

**Corollary.** The reversal is the identity exactly when every word is a palindrome, which is the case for $X$ empty, for $X$ with one element, and for a free algebra on one generator; it is the identity on the commutative quotients, where the words are identified with their reversals by the commutativity of the product, as in the polynomial algebra.

## Anti-Involutions from the Generators

### Arbitrary Anti-Homomorphisms

**Theorem.** Let $B$ be a $k$-algebra. Every map $f : X \to B$ extends uniquely to an anti-homomorphism $F\langle X\rangle \to B$, given on a word by $x_1\cdots x_n \mapsto f(x_n)\cdots f(x_1)$. In particular the anti-homomorphisms of $F\langle X\rangle$ correspond bijectively to the maps $X \to F\langle X\rangle$, and an anti-homomorphism is an anti-automorphism exactly when its images of the generators generate $F\langle X\rangle$.

*Proof.* The formula reverses the order of the images, so the concatenation is reversed and the map is anti-multiplicative; it is the unique one with the given values on $X$ because $X$ generates. Surjectivity holds exactly when the images generate, since the image of the algebra is the subalgebra generated by the images of $X$.

**Corollary.** The anti-involutions of the free algebra correspond bijectively to the maps $f : X \to F\langle X\rangle$ such that the images generate $F\langle X\rangle$ and $f$ extends to a map of order two, that is, such that the anti-homomorphism $\theta_f$ satisfies $\theta_f^2 = \mathrm{id}$. The reversal is the case $f = \mathrm{id}$.

### The Involutive Automorphisms

**Proposition.** Let $\pi$ be a permutation of $X$ with $\pi^2 = \mathrm{id}$ and let $\epsilon : X \to \{\pm1\}$ be a map. Then the assignment $x \mapsto \epsilon(x)\,x^{\pi}$ extends to an algebra automorphism of $F\langle X\rangle$, and it is an involution exactly when $\epsilon(\pi(x))\epsilon(x) = 1$ for every $x$. In particular the **signed permutation involution** $x \mapsto \epsilon(x)x^{\pi}$ is an involutive automorphism, and the grade involution $\alpha$ is the case $\pi = \mathrm{id}$, $\epsilon(x) = -1$ on every generator.

*Proof.* The assignment extends to an automorphism by the universal property, since the images are generators; the square of the automorphism carries $x$ to $\epsilon(x)\epsilon(\pi(x))x$, because $\pi^2 = \mathrm{id}$, so it is the identity exactly when the product of the two signs is $1$ for every $x$. The grade involution sends a word $x_1\cdots x_n$ to $(-1)^n x_1\cdots x_n$, which is the extension of the assignment $x\mapsto -x$, and $-x$ is a generator up to sign.

**Corollary.** The group of automorphisms of $F\langle X\rangle$ contains the signed permutations of the generators of order two, and the reversal involution lies outside it as an anti-automorphism; the two generate the involutive structure of the free algebra, the reversal being canonical and the signed permutations being the automorphism half.

## The Quotients

### Descent

**Proposition.** Let $I$ be a two-sided ideal of $F\langle X\rangle$ stable under an anti-involution $\theta$ of the free algebra. Then $I$ is stable under $\theta$, the quotient $F\langle X\rangle/I$ carries the descended anti-involution $\bar\theta$ of order two, and the quotient map is equivariant. The same holds for the descent of an involutive automorphism, with stability the only hypothesis.

*Proof.* Stability of the ideal under the involution makes the map on the quotient well defined, and the quotient inherits the order-two and anti-multiplicativity properties from the free algebra; this is the descent of *Ideals and Quotients of Algebras*.

### The Three Classical Quotients

**Proposition.** The following quotients inherit an involution from the free algebra.

**(1)** The **polynomial algebra** $k[x_1,\dots,x_n] = F\langle X\rangle/I_{\mathrm s}$ by the commutator ideal is the quotient by the ideal generated by $x_ix_j - x_jx_i$; it is stable under the reversal, because the reversal of a commutator is minus the commutator, and the descended reversal is the identity, since the quotient is commutative. The descended signed permutation involutions are the automorphisms of the polynomial algebra induced by signed permutations of the variables.

**(2)** The **exterior algebra** $\Lambda(V) = F\langle X\rangle/I_{\mathrm e}$ by the ideal generated by the squares $x^2$ and the anticommutators $x_ix_j + x_jx_i$ is stable under the reversal and under the grade involution. The descended reversal is the anti-automorphism fixing every generator, which acts on the degree-$n$ part by $(-1)^{n(n-1)/2}$; the descended grade involution acts on the degree-$n$ part by $(-1)^n$. The two agree on the degrees $n \equiv 0, 3 \pmod 4$ and differ on the degrees $n \equiv 1, 2 \pmod 4$.

**(3)** The **group algebra** $k[G] = F\langle X\rangle/I_G$, for $X = G$ and the ideal generated by the relations $x_gx_h - x_{gh}$, is stable under the reversal exactly when $G$ is abelian; the descended reversal is then the identity. When $G$ is not abelian the reversal does not descend, and the inversion $g \mapsto g^{-1}$ supplies a different anti-automorphism of $k[G]$, which has order two exactly when every element of $G$ has order dividing two, as in *Opposite Algebras and Anti-Isomorphisms*.

*Proof.* In each case the ideal is generated by elements that the reversal carries into the ideal, so the descent applies, and the descended map is computed on the generators of the quotient, which are the images of the free generators. For the exterior algebra the reversal of a word of length $n$ is the word read backwards, which equals $(-1)^{n(n-1)/2}$ times the word because each of the $n(n-1)/2$ transpositions of adjacent generators contributes a sign; the grade involution contributes $(-1)^n$. For the group algebra, $\mathrm{rev}(x_gx_h - x_{gh}) = x_hx_g - x_{gh}$, which lies in the ideal for all $g, h$ exactly when $hg = gh$; when it descends, the reversal fixes each generator and is the identity on the commutative quotient.

## The Examples

### One Generator

For $X = \{x\}$ the free algebra is the polynomial algebra $k[x]$ in one variable, every word is a palindrome, the reversal is the identity, and the only signed permutation involution is $x \mapsto -x$, which is the grade involution of the degree grading of $T(k)$. The fixed skew decomposition is trivial in the skew part, since the reversal is the identity, and the example marks the degenerate case in which the canonical involution carries no information.

### Two Generators

For $X = \{x,y\}$ the free algebra $F\langle x,y\rangle$ is the algebra of noncommutative polynomials in two variables, and its reversal is not the identity: the word $xy$ is reversed to $yx$ and the difference $xy - yx$ is skew, while $xy + yx$ is symmetric. The signed permutation involutions come from the identity and the transposition of the two generators, each with signs subject to the order-two condition; for the identity permutation the condition is $\epsilon(x)^2 = \epsilon(y)^2 = 1$ and the involutions are the four sign choices, among them the grade involution. The commutator ideal is stable, the quotient is the polynomial algebra $k[x,y]$, and the descended reversal is the identity there.

### The Free Algebra on a Group

For $X = G$ a group, the free algebra on the elements of $G$ has the group algebra as a quotient, and the anti-involutions of the free algebra that preserve the group relations descend to the anti-automorphisms of the group algebra. The inversion is the canonical one; it is an involution exactly when every element of $G$ has order dividing two, by *Opposite Algebras and Anti-Isomorphisms*.

## Summary

The free algebra $F\langle X\rangle$ on a set $X$ has for basis the words in the generators, the product being concatenation, and it satisfies the universal property that every map $X \to B$ into an algebra extends uniquely to a homomorphism. Its **canonical anti-involution** is the **reversal** $\mathrm{rev}(x_1\cdots x_n) = x_n\cdots x_1$, the unique anti-automorphism fixing every generator; it has order two, its fixed space is spanned by the palindromes and the symmetric sums and its skew part by the antisymmetric differences, and it is the identity exactly when every word is a palindrome. Its **involutive automorphisms** are the **signed permutations** $x \mapsto \epsilon(x)x^{\pi}$ with $\pi^2 = \mathrm{id}$ and $\epsilon(\pi(x))\epsilon(x) = 1$, among them the grade involution $x \mapsto -x$, which acts on a word by the sign $(-1)^{|w|}$.

Anti-homomorphisms of $F\langle X\rangle$ correspond bijectively to maps $X \to F\langle X\rangle$, and an anti-involution corresponds to a map $f$ with $\theta_f^2 = \mathrm{id}$ and generating image; the reversal is $f = \mathrm{id}$. An ideal stable under an involution admits the descent, and the classical quotients receive their involutions this way: the polynomial algebra by the (stable) commutator ideal, with the descended reversal the identity; the exterior algebra, with the descended reversal the identity and the descended grade involution the degree sign; and the group algebra, where the descended reversal of the generators is the inversion. The tensor-power theory and the identification of the free algebra with the tensor algebra belong to *Tensor Powers and the Free Algebra*; the reversal involution of the tensor algebra and its quotients is *Involutions of the Tensor Algebra*; the general theory of an involution on the elements is *Involutive Algebras*; and the involutions of the path algebras, which are quotients of a free algebra by the relations of a quiver, are *Involutions of a Path Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the field of scalars |
| $X$ | the set of generators |
| $F\langle X\rangle$ | the free associative algebra, basis the words |
| $w = x_1\cdots x_n$ | a word, of length $n$ |
| $\mathrm{rev}(w) = x_n\cdots x_1$ | the reversal of a word |
| $\theta_f$ | the anti-homomorphism extending $f : X \to B$ |
| $x \mapsto \epsilon(x)x^{\pi}$ | a signed permutation involution |
| $\alpha(w) = (-1)^{|w|}w$ | the grade involution |
| $F\langle X\rangle = F\langle X\rangle^+\oplus F\langle X\rangle^-$ | the fixed and skew parts of the reversal |
| $I_{\mathrm s}, I_{\mathrm e}, I_G$ | the ideals of the classical quotients |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the free algebra, its universal property and the classical quotients.
- Paul M. Cohn, *Free Rings and their Relations* (Academic Press, second edition, 1985), for the free associative algebra and its anti-automorphisms.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the free algebra and the reversal of words.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the anti-involutions determined on a generating set.
