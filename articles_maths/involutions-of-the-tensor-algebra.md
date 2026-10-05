# __Involutions of the Tensor Algebra__

## Introduction

The tensor algebra $T(V)$ of a linear space $V$ carries every involution that $V$ itself carries, and it carries one more that $V$ does not: the **sign involution** that is $+1$ on the even tensor powers and $-1$ on the odd ones. The first is an anti-automorphism, obtained by reversing the order of the factors of a tensor and applying the involution of $V$ to each; the second is an automorphism, the grade involution of the degree grading. They generate the involutions of the tensor algebra, and their behaviour under the quotients of $T(V)$ — the symmetric algebra and the exterior algebra — is the subject of the article.

This article develops the tensor algebra, the two constructions of an involution on it, the sign rule that distinguishes them, and the passage to the quotients by an ideal stable under the involution. The tensor algebra itself, its universal property and its identification with the free associative algebra are the subject of *Tensor Powers and the Free Algebra*; the involutions determined by a set of generators and by the reversal of words are the subject of *Involutions of a Free Algebra*; and the general theory of an involution on the elements, with its symmetric and skew parts, is *Involutive Algebras*.

Throughout, $k$ is a field of characteristic not two, $V$ is a $k$-linear space, $T(V) = \bigoplus_{n \geq 0} V^{\otimes n}$ is its tensor algebra with $V^{\otimes 0} = k$, and $\sigma$ is a $k$-linear involution of $V$, $\sigma^2 = \mathrm{id}_V$. The tensor powers are those of *Tensor Powers and the Free Algebra*, and the tensor product of algebras is that of *Tensor Products of Algebras*.

## The Tensor Algebra

### Definition

**Definition.** The **tensor algebra** of $V$ is the graded $k$-algebra

$$
T(V) = \bigoplus_{n \geq 0} V^{\otimes n}, \qquad V^{\otimes 0} = k, \qquad V^{\otimes 1} = V,
$$

with the product given on decomposable tensors by concatenation,

$$
(v_1 \otimes \cdots \otimes v_m)(w_1 \otimes \cdots \otimes w_n) = v_1 \otimes \cdots \otimes v_m \otimes w_1 \otimes \cdots \otimes w_n,
$$

extended bilinearly, and with unit $1 \in V^{\otimes 0} = k$. The element $v_1 \otimes \cdots \otimes v_n$ is written $v_1 \cdots v_n$.

The product is associative, because concatenation of words is associative, and the grading is the degree, $T(V)^n = V^{\otimes n}$; the tensor algebra is the free associative algebra on the space $V$, with the universal property that every $k$-linear map $V \to B$ into an associative $k$-algebra $B$ extends uniquely to an algebra homomorphism $T(V) \to B$.

### The Degree and the Sign

**Definition.** The **degree** of a homogeneous tensor $v_1 \cdots v_n$ is $n$, and the **grade involution** of $T(V)$ is the linear map

$$
\alpha : T(V) \to T(V), \qquad \alpha(x) = (-1)^n x \ \text{ on } V^{\otimes n} .
$$

**Proposition.** The grade involution is an algebra automorphism of $T(V)$ with $\alpha^2 = \mathrm{id}$, and it is the unique automorphism of $T(V)$ that is $-\mathrm{id}$ on $V$. Its fixed algebra is the even part $\bigoplus_{n \text{ even}} V^{\otimes n}$ and its negated part is the odd part $\bigoplus_{n \text{ odd}} V^{\otimes n}$; the grading of $T(V)$ is the one whose grade involution is $\alpha$.

*Proof.* On decomposable tensors, $\alpha(xy) = (-1)^{m+n} xy = \alpha(x)\alpha(y)$, so $\alpha$ is multiplicative; $\alpha^2 = \mathrm{id}$ because $(-1)^{2n} = 1$, and $\alpha(1) = 1$. An automorphism that is $-\mathrm{id}$ on $V$ is determined on $V$ and hence, by the universal property, on all of $T(V)$, so it is unique. The eigenspaces are the even and the odd parts by definition.

## The Reversal Involution

### The Induced Map

**Definition.** Let $\sigma$ be an involution of $V$. The **reversal involution** is the linear map

$$
\theta_\sigma : T(V) \to T(V), \qquad \theta_\sigma(v_1 \cdots v_n) = \sigma(v_n) \cdots \sigma(v_1), \qquad \theta_\sigma(1) = 1,
$$

defined on decomposable tensors and extended linearly.

**Theorem.** The reversal involution $\theta_\sigma$ is an anti-automorphism of $T(V)$ with $\theta_\sigma^2 = \mathrm{id}$, it extends $\sigma$ on $V^{\otimes 1} = V$, and it is the unique anti-automorphism of $T(V)$ extending $\sigma$.

*Proof.* For two words $x = v_1\cdots v_m$ and $y = w_1\cdots w_n$ one has $\theta_\sigma(xy) = \theta_\sigma(v_1\cdots v_m w_1\cdots w_n) = \sigma(w_n)\cdots\sigma(w_1)\sigma(v_m)\cdots\sigma(v_1) = \theta_\sigma(y)\theta_\sigma(x)$, so $\theta_\sigma$ reverses products; it is linear and bijective with inverse $\theta_{\sigma^{-1}} = \theta_\sigma$, since $\sigma^2 = \mathrm{id}$, and it fixes $1$. On $V$ it is $\sigma$. An anti-automorphism extending $\sigma$ agrees with it on $V$, and an anti-homomorphism from $T(V)$ is determined by its restriction to $V$ because $V$ generates $T(V)$ as an algebra and the reversal of the order is the same on every word; hence the extension is unique.

**Corollary.** $\theta_\sigma$ is an involution of the algebra $T(V)$ in the sense of *Involutive Algebras*, its fixed algebra is the span of the symmetric words and its skew part is the span of the antisymmetric words, and on the tensor powers it satisfies $\theta_\sigma(V^{\otimes n}) = V^{\otimes n}$.

*Proof.* The reversal maps a word of length $n$ to a word of length $n$, so each tensor power is stable; the fixed and skew elements are the symmetric and antisymmetric combinations of the words, by the decomposition of *Involutive Algebras*.

### The Relation of the Two

**Proposition.** The reversal involution and the grade involution commute, $\theta_\sigma\alpha = \alpha\theta_\sigma$, and their composite $\theta_\sigma\alpha$ is an anti-automorphism of $T(V)$ of order two, the **signed reversal**, acting on a decomposable tensor by

$$
\theta_\sigma\alpha(v_1\cdots v_n) = (-1)^n \sigma(v_n)\cdots\sigma(v_1) .
$$

*Proof.* The grade involution multiplies a word of length $n$ by $(-1)^n$ and the reversal preserves the length, so the two commute; the composite of an anti-automorphism with an automorphism is an anti-automorphism, and its square is $\theta_\sigma^2\alpha^2 = \mathrm{id}$.

**Corollary.** For every $n$ the involution $\theta_\sigma$ of the tensor power $V^{\otimes n}$ is the tensor product $\sigma^{\otimes n}$ composed with the swap that reverses the order of the factors, and the signed version differs from it by the sign $(-1)^n$. In particular the two agree on the even powers and are opposite on the odd powers, which is the sign rule that the graded and the ungraded involutions of the tensor algebra impose.

## The Involutions of the Tensor Algebra

### The Extensions

**Theorem.** Let $V$ be a $k$-linear space. The anti-automorphisms of $T(V)$ of order two are exactly the maps $\theta_\sigma$ for the linear involutions $\sigma$ of $V$; the automorphisms of $T(V)$ of order two that are $+1$ on $V$ are the identity alone; and the group of automorphisms of $T(V)$ contains $\alpha$ and the automorphisms induced by the linear automorphisms of $V$.

*Proof.* An anti-automorphism of order two is determined by its restriction to $V$, which is a linear involution; the extension is unique by the reversal theorem, so the anti-involutions are the $\theta_\sigma$. An automorphism that is the identity on $V$ is the identity on the generating space and hence on $T(V)$ by the universal property. The grade involution $\alpha$ is an automorphism of order two, and a linear automorphism $g$ of $V$ extends to an algebra automorphism of $T(V)$, the two constructions being compatible with the grading.

**Remark.** For $\dim_k V \geq 2$ the group of automorphisms of $T(V)$ is larger than the two families displayed; it contains the automorphisms that permute the tensor powers in a manner compatible with the universal property, and it is not computed here. The two families that matter for the involutive theory are the reversals $\theta_\sigma$ and the grade involution $\alpha$, because every involution of the tensor algebra that is homogeneous and respects the grading is built from them.

### The Sign Rule

**Proposition.** Let $x$ and $y$ be homogeneous elements of $T(V)$ of degrees $m$ and $n$. Then

$$
\theta_\sigma(xy) = \theta_\sigma(y)\theta_\sigma(x), \qquad \alpha(xy) = \alpha(x)\alpha(y), \qquad (\theta_\sigma\alpha)(xy) = (\theta_\sigma\alpha)(y)\,(\theta_\sigma\alpha)(x),
$$

so the reversal and the signed reversal are anti-multiplicative and the grade involution is multiplicative. The sign rule of the grading is $\alpha(x) = (-1)^m x$ on the degree-$m$ part: the grade involution is the identity on the even part and minus the identity on the odd part, and the signed reversal differs from the reversal by the sign $(-1)^m$ on the degree-$m$ part. The two maps $\alpha$ and $\theta_\sigma$ commute, and neither of them carries a Koszul factor of its own: the factor $(-1)^{mn}$ belongs to the graded twist of *Superalgebras and Graded Structures*, and it is what separates the graded involution from the superinvolution in *Involutive Graded Algebras*.

*Proof.* The reversal is anti-multiplicative by the theorem, and the signed reversal is the composite of an anti-automorphism with an automorphism, hence anti-multiplicative. The grade involution is multiplicative on decomposable tensors, $\alpha(xy) = (-1)^{m+n}xy = \alpha(x)\alpha(y)$. The commutation of the two is the observation that the reversal preserves the degree and the grade involution is scalar on each degree.

## The Quotients

### Stable Ideals

**Definition.** Let $I \subseteq T(V)$ be a two-sided ideal. The involution $\theta$ (respectively the automorphism $\alpha$) **descends** to the quotient $T(V)/I$ if $I$ is $\theta$-stable (respectively $\alpha$-stable), that is $\theta(I) \subseteq I$; the descended map on the quotient is defined by $\theta(x + I) = \theta(x) + I$.

**Proposition.** A two-sided ideal $I$ of $T(V)$ is stable under $\theta_\sigma$ if and only if it is stable under the reversal of the words, and it is stable under $\alpha$ if and only if it is generated by homogeneous elements of definite parity. When $I$ is stable under both, the quotient $T(V)/I$ carries the descended anti-involution $\theta_\sigma$ and the descended grade involution $\alpha$, and the quotient map is equivariant for both.

*Proof.* A two-sided ideal stable under an anti-automorphism is automatically stable under the inverse map because the map has order two, so stability for $\theta_\sigma$ is well defined and equivalent to the generator condition; the descent is the standard property of a quotient by an invariant ideal. For $\alpha$, stability is the statement that the ideal is graded, equivalently generated by homogeneous elements.

### The Commutative and the Exterior Quotients

**Theorem.** Let $\sigma$ be an involution of $V$ and let $I$ be a $\theta_\sigma$-stable ideal of $T(V)$. Then the quotient $T(V)/I$ is an involutive algebra with the descended reversal, and the following hold.

**(1)** For the **symmetric algebra** $S(V) = T(V)/I_{\mathrm s}$, where $I_{\mathrm s}$ is the ideal generated by the commutators $v \otimes w - w \otimes v$, the ideal is stable under every $\theta_\sigma$ and under $\alpha$, and the descended reversal is the automorphism of $S(V)$ induced by $\sigma$; the descended grade involution is the automorphism acting by $(-1)^n$ on the degree-$n$ part of $S(V)$, which is the involutive automorphism of the polynomial algebra in a basis.

**(2)** For the **exterior algebra** $\Lambda(V) = T(V)/I_{\mathrm e}$, where $I_{\mathrm e}$ is generated by the elements $v \otimes v$ for $v \in V$ (equivalently, by the $v \otimes w + w \otimes v$), the ideal is stable under every $\theta_\sigma$ and under $\alpha$; the descended reversal is the anti-automorphism that extends $\sigma$ and reverses the order of the factors, so for $\sigma = \mathrm{id}$ it acts on the degree-$n$ part by $(-1)^{n(n-1)/2}$, while the descended grade involution acts on the degree-$n$ part by $(-1)^n$; the two agree on the degrees $n \equiv 0, 3 \pmod 4$ and differ on the degrees $n \equiv 1, 2 \pmod 4$.

*Proof.* (1) The commutator ideal is stable under every linear map of $V$ and under $\alpha$, so both descend; on the quotient the product is commutative, and a reversal of a commutative word is the word itself with $\sigma$ applied to each letter, which is the automorphism induced by $\sigma$. (2) The element $v \otimes v$ is reversed to $\sigma(v)\otimes\sigma(v)$, which lies in the ideal, and it is even, so the ideal is stable under both maps; the identification of the reversal with the extension of $\sigma$ uses the relation $v \otimes w = -w \otimes v$. $\square$

**Corollary.** The tensor algebra is the universal source of the involutive algebras built from a space: an involution of $V$ that preserves the relations of a quotient descends to an involution of the quotient, and the two classical quotients — the symmetric and the exterior algebra — receive the descended reversal and the descended grade involution together. The involution of the exterior algebra belongs to *The Exterior Algebra* of the anti-symmetric category; a third quotient, the Clifford algebra, needs a quadratic form and belongs to *Quadratic Forms and Clifford Algebras* of Part II, where the form is owned, and is named only. The present article supplies only the descent from $T(V)$.

## The Examples

### One Generator

Let $\dim_k V = 1$, with basis $v$, so that $T(V) = k[v]$ is the polynomial algebra in one variable; every linear involution of $V$ is $\sigma(v) = \pm v$. If $\sigma = \mathrm{id}$, the reversal involution is the identity on $k[v]$, because a power of $v$ is a one-letter word and the reversal of a word of length one is the word itself. If $\sigma(v) = -v$, the reversal involution is the algebra automorphism $v \mapsto -v$, which is also the grade involution composed with the identity; on the monomial $v^n$ it acts by $(-1)^n$. The symmetric and exterior quotients are $k[v]$ and $k[v]/(v^2)$ respectively, and the descended involutions are the ones displayed.

### Two Generators

Let $\dim_k V = 2$, with basis $u, v$, so that $T(V)$ is the free associative algebra on two generators and its words are the words in $u$ and $v$. The reversal of a word reverses the order of its letters; for a word of length $\geq 2$ this is not the identity, and the reversal involution of $T(V)$ has many fixed elements, for instance $uv + vu$ and $u v w + w v u$ for any letters. The grade involution acts by $(-1)^n$ on words of length $n$, so the word $uv$ is fixed by $\alpha$ and the word $uvw$ is negated. The composite sends $uvw$ to $-wvu$; this is the signed reversal of the free algebra, and it is the involution that the free-algebra article studies from the side of the generators.

## Summary

The tensor algebra $T(V) = \bigoplus_{n\geq0} V^{\otimes n}$ carries two involutions built from the space. The **grade involution** $\alpha$ is the automorphism that is $+1$ on the even tensor powers and $-1$ on the odd ones, $\alpha(x) = (-1)^n x$ on $V^{\otimes n}$; it is multiplicative, $\alpha(xy) = \alpha(x)\alpha(y)$, it is the unique automorphism that is $-\mathrm{id}$ on $V$, and its grading is the degree grading. The **reversal involution** $\theta_\sigma$ is the anti-automorphism extending a linear involution $\sigma$ of $V$, $\theta_\sigma(v_1\cdots v_n) = \sigma(v_n)\cdots\sigma(v_1)$; it is the unique anti-automorphism extending $\sigma$, it has order two, and it is the composite of $\sigma^{\otimes n}$ with the reversal of the factors on each tensor power. The two commute, and their composite $\theta_\sigma\alpha$ is the signed reversal acting by $(-1)^n\sigma(v_n)\cdots\sigma(v_1)$; neither of the two maps carries a Koszul factor of its own, and the factor $(-1)^{mn}$ belongs to the graded twist of *Superalgebras and Graded Structures*.

An ideal stable under the reversal and the grade involution admits both on the quotient. The symmetric algebra receives the extension of $\sigma$ and the degree sign automorphism, and the exterior algebra receives the extension of $\sigma$ and the grade involution. A third quotient, the Clifford algebra of a quadratic map, needs a form and belongs to *Quadratic Forms and Clifford Algebras* of Part II, where it is named only. The tensor algebra itself, its universal property and its identification with the free associative algebra belong to *Tensor Powers and the Free Algebra*; the involutions read on the generators and the reversal of words are *Involutions of a Free Algebra*; the exterior algebra is *The Exterior Algebra* of the anti-symmetric category; and the general theory of an involution on the elements is *Involutive Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the field of scalars, of characteristic not two |
| $V$ | a $k$-linear space |
| $T(V) = \bigoplus_n V^{\otimes n}$ | the tensor algebra |
| $V^{\otimes n}$ | the tensor power |
| $\sigma$ | a linear involution of $V$ |
| $\alpha(x) = (-1)^n x$ | the grade involution |
| $\theta_\sigma(v_1\cdots v_n) = \sigma(v_n)\cdots\sigma(v_1)$ | the reversal involution |
| $\theta_\sigma\alpha$ | the signed reversal |
| $S(V), \Lambda(V)$ | the symmetric and exterior quotients |
| $I_{\mathrm s}, I_{\mathrm e}$ | the ideals defining the two quotients |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the tensor algebra, its universal property and the classical quotients.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the tensor algebra and the free associative algebra.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions of the tensor constructions.
