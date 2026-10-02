
# __The Frobenius Operator on a Field of Characteristic p__

## Introduction

In a field $F$ of prime characteristic $p$ the map $\varphi(x) = x^p$ is not merely a power map but a ring endomorphism. The reason is the binomial theorem: the intermediate binomial coefficients $\binom{p}{1}, \dots, \binom{p}{p-1}$ are all divisible by $p$, and in a ring of characteristic $p$ the corresponding terms vanish, leaving the **freshman's dream**
$$(x+y)^p = x^p + y^p.$$
With multiplicativity, $(xy)^p = x^py^p$, this makes $\varphi$ additive and multiplicative at once, hence an injective ring endomorphism of $F$, the **Frobenius endomorphism**. In characteristic $0$ the same computation gives no collapse — $\binom{2}{1} = 2 \neq 0$ — and $x \mapsto x^p$ is neither additive nor an endomorphism.

This article treats $\varphi$ as an operator on the field, in the sense of the operator layer of this category: it is a distinguished element of $\operatorname{End}(F)$, it generates the automorphism group of a finite field, its fixed field is the prime field, and its image $F^p$ measures whether $F$ is perfect. The Frobenius operator is the arithmetic operator par excellence: it exists on every field of characteristic $p$, it is canonically determined by the field, and its failure to be onto is exactly the failure of the field to be perfect. The vocabulary is that of *Fields* for the object and its prime field, *Finite Fields* for the finite case in which $\varphi$ is an automorphism generating the Galois group, and *Ring and Field Automorphisms* for the automorphism group of a field and the fact that the Frobenius is an automorphism exactly over a perfect field. Throughout, $F$ is a field of characteristic $p > 0$ unless another characteristic is signalled, $F^p = \{x^p : x \in F\}$, and $\mathbb{F}_p$ is the prime field.

## The p-th Power Map

### Definition

**Definition.** Let $F$ be a field of characteristic $p$. The **Frobenius operator** is

$$
\varphi : F \to F, \qquad \varphi(x) = x^p .
$$

The **$n$-th Frobenius power** is its $n$-fold iterate $\varphi^n(x) = x^{p^n}$.

**Proposition.** $\varphi(xy) = \varphi(x)\varphi(y)$ for all $x, y$, and $\varphi(1) = 1$, $\varphi(0) = 0$. In particular $\varphi$ is multiplicative on the whole of $F$, and $\varphi^n(xy) = \varphi^n(x)\varphi^n(y)$.

**Proof.** $(xy)^p = x^p y^p$ is commutativity and the power law in a commutative ring; multiplicativity iterates. $\varphi(1) = 1^p = 1$ and $\varphi(0) = 0$.

### Additivity and the freshman's dream

**Theorem (freshman's dream).** In a commutative ring of characteristic $p$, $(x+y)^p = x^p + y^p$; consequently the Frobenius operator of a field of characteristic $p$ is additive, and is a unital ring endomorphism of $F$.

**Proof.** The binomial theorem in a commutative ring gives $(x+y)^p = \sum_{k=0}^{p} \binom{p}{k} x^k y^{p-k}$. For $1 \leq k \leq p-1$ the binomial coefficient $\binom{p}{k} = \frac{p!}{k!(p-k)!}$ is divisible by $p$: the factor $p$ in the numerator is not cancelled by the factorials $k!$ and $(p-k)!$, both of which involve only integers less than $p$ and hence are coprime to $p$. In characteristic $p$ the products $\binom{p}{k} x^ky^{p-k} = 0$ for those $k$, and the two end terms remain: $(x+y)^p = x^p + y^p$. With the multiplicativity above, $\varphi$ is a unital endomorphism.

**Corollary (the naive expansion fails in characteristic $0$).** In a field of characteristic $0$ the coefficients $\binom{p}{k}$ do not vanish, and the expansion does not collapse. For example over $\mathbb{Q}$,
$$
(1+1)^2 = 4 \neq 2 = 1^2 + 1^2,
$$
so the map $x \mapsto x^2$ on $\mathbb{Q}$ is not additive and therefore not an endomorphism; the same computation shows that over any field of characteristic $0$ the power map $x \mapsto x^p$ adds a stack of intervening terms and is not a ring homomorphism. The Frobenius operator owes its existence entirely to the vanishing of the binomial coefficients modulo $p$.

**Remark (a noncommutative warning).** In a noncommutative ring of characteristic $p$ the freshman's dream fails: $(xy)^p = xyxy\cdots xy \neq x^py^p$ in general, and the expansion of $(x+y)^p$ is a sum over all words of length $p$ rather than a sum of the two end terms. The Frobenius is therefore a homomorphism of a **commutative** ring of characteristic $p$, and on a noncommutative ring it is additive and multiplicative only on commuting elements. The finite-field and field cases of this article are automatically commutative.

## The Image and the Kernel

### Injectivity

**Proposition.** The Frobenius endomorphism of a field is injective, hence $\ker \varphi = 0$ and the image $F^p$ is a subfield isomorphic to $F$.

**Proof.** $\varphi(x) = 0 \iff x^p = 0 \iff x = 0$ in a field. A unital ring homomorphism out of a field whose kernel is a proper ideal must be injective, since a field has no proper nonzero two-sided ideals; the image of a homomorphism is a subring, and it is a subfield because $\varphi$ is multiplicative and $\varphi(x)^{-1} = \varphi(x^{-1})$ for $x \neq 0$.

**Corollary.** $\varphi$ restricts to an automorphism of the prime field $\mathbb{F}_p$: for $a \in \mathbb{F}_p$ one has $\varphi(a) = a^p = a$, since every element of $\mathbb{F}_p$ satisfies $a^p = a$.

### Surjectivity and perfect fields

**Definition.** A field $F$ of characteristic $p$ is **perfect** when every element is a $p$-th power, that is, $F = F^p$.

**Theorem.** The Frobenius operator is an automorphism if and only if $F$ is perfect. For an imperfect field, $\varphi$ is injective and not surjective, and it is a bijection of $F$ onto the proper subfield $F^p$; the extension $F/F^p$ is purely inseparable and, when finite, has degree $p^e$.

**Proof.** Surjectivity is exactly $F = F^p$, which is perfectness; an injective surjective endomorphism of $F$ is an automorphism. For the last statements, every element $x$ satisfies $x^p \in F^p$, so $F$ is generated over $F^p$ by $p$-th roots, and the minimal polynomial of $x$ over $F^p$ divides $X^p - x^p = (X-x)^p$, hence has a single root: the extension is purely inseparable. A finite purely inseparable extension has degree a power of $p$.

**Examples.** The finite fields $\mathbb{F}_{p^n}$ are perfect, since they are finite and $\varphi$ is injective on a finite set; so $\varphi$ is an automorphism there. The rational function field $\mathbb{F}_p(t)$ is imperfect: $F^p = \mathbb{F}_p(t^p)$, and $t \notin F^p$, so $\varphi$ is not onto and $[\mathbb{F}_p(t) : \mathbb{F}_p(t^p)] = p$. A separably closed or algebraically closed field is perfect.

## The Fixed Field and the Galois Action

### The fixed field is the prime field

**Theorem.** The fixed field of the Frobenius operator is the prime field:
$$
F^{\varphi} = \{x \in F : x^p = x\} = \mathbb{F}_p .
$$

**Proof.** The elements fixed by $\varphi$ are the roots in $F$ of the polynomial $X^p - X$, which has at most $p$ roots in the field $F$. The $p$ elements of $\mathbb{F}_p$ all satisfy $a^p = a$ (the multiplicative group $\mathbb{F}_p^\times$ has order $p-1$, so $a^{p-1}=1$ for $a\neq0$, and $0^p=0$), so they are exactly the $p$ roots and there are no others.

**Corollary.** The Frobenius operator fixes no element outside the prime field; the fixed field of $\varphi^n$ is the field of elements with $x^{p^n} = x$, which for the finite field $\mathbb{F}_{p^m}$ equals $\mathbb{F}_{p^{\gcd(m,n)}}$.

### The finite case and the Galois group

**Theorem (the Frobenius generates $\operatorname{Gal}(\mathbb{F}_{p^n}/\mathbb{F}_p)$).** For the finite field $\mathbb{F}_{p^n}$, the Frobenius operator $\varphi$ is an automorphism of order $n$, and
$$
\operatorname{Gal}(\mathbb{F}_{p^n}/\mathbb{F}_p) = \langle \varphi \rangle \cong \mathbb{Z}/n .
$$
Its fixed field is $\mathbb{F}_p$, and $\varphi^n = \mathrm{id}$ on $\mathbb{F}_{p^n}$.

**Proof.** The multiplicative group $\mathbb{F}_{p^n}^\times$ is cyclic of order $p^n - 1$, so every nonzero element satisfies $x^{p^n - 1} = 1$ and hence $x^{p^n} = x$; together with $0$, every element of $\mathbb{F}_{p^n}$ is fixed by $\varphi^n$, so $\varphi^n = \mathrm{id}$. If $\varphi^d = \mathrm{id}$ for some $d < n$, then every element of $\mathbb{F}_{p^n}$ would satisfy $x^{p^d} = x$, giving at most $p^d < p^n$ elements, a contradiction; so the order of $\varphi$ is $n$. The field $\mathbb{F}_{p^n}$ is a splitting field of $X^{p^n}-X$ over $\mathbb{F}_p$, hence Galois, and its Galois group has order $n = [\mathbb{F}_{p^n} : \mathbb{F}_p]$; the subgroup generated by $\varphi$ has order $n$ and is therefore the whole group.

**Remark.** For a finite field the Frobenius is the canonical generator of the Galois group, and the subfields of $\mathbb{F}_{p^n}$ correspond to the divisors of $n$ through the subgroups of $\langle \varphi \rangle$. Over an infinite field the Frobenius need not be an automorphism and need not generate the automorphism group; the finite case is the one in which it is both onto and generating.

## The Frobenius and the Derivations

### The Frobenius kills the derivations

**Proposition.** In a field $F$ of characteristic $p$, every derivation $D$ of $F$ annihilates the image of the Frobenius:
$$
D\bigl(x^p\bigr) = p\,x^{p-1}D(x) = 0 \quad \text{for all } x \in F, \qquad D\big|_{F^p} = 0 .
$$
Hence $F^p \subseteq F^{D}$ for every derivation $D$, and if $F$ is perfect every derivation is zero.

**Proof.** The power rule for a derivation in a commutative ring gives $D(x^p) = p\,x^{p-1}D(x)$, and $p = 0$ in $F$. For a perfect field $F = F^p$, so $D = 0$ on all of $F$.

**Example.** On $\mathbb{F}_p(t)$ the derivation $\partial/\partial t$ is nonzero and kills $\mathbb{F}_p(t^p) = F^p$. The pair $(\varphi, \partial_t)$ exhibits the two operators in characteristic $p$: the Frobenius is the endomorphism with image the constants of the derivation, and the derivation is the one that the Frobenius's image annihilates. This is the algebraic skeleton of the theory of derivations of an imperfect field, and it is used in *Derivations of a Ring*.

## Summary

In a field $F$ of characteristic $p$ the Frobenius operator $\varphi(x) = x^p$ is multiplicative and, because the binomial coefficients $\binom{p}{k}$ vanish modulo $p$, additive; it is therefore a unital ring endomorphism of $F$, the freshman's dream $(x+y)^p = x^p+y^p$ being the additivity. In characteristic $0$ the coefficients do not vanish, the expansion does not collapse, and the power map is not additive: this is the failure that distinguishes the two characteristics. In a noncommutative ring of characteristic $p$ the map is a homomorphism only on commuting elements, and the fields of the article are commutative.

The Frobenius is injective with image the subfield $F^p$; it is an automorphism exactly when $F$ is perfect, and otherwise it is a bijection onto the proper subfield $F^p$ with $F/F^p$ purely inseparable. Its fixed field is the prime field $\mathbb{F}_p$, the roots of $X^p - X$. On the finite field $\mathbb{F}_{p^n}$ it is an automorphism of order $n$ generating $\operatorname{Gal}(\mathbb{F}_{p^n}/\mathbb{F}_p) \cong \mathbb{Z}/n$. Every derivation of $F$ annihilates $F^p$, so on a perfect field there are no nonzero derivations; the Frobenius and the derivations are the two characteristic-$p$ operators, and the image of the one is the zero set of the other.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $p$ | A prime; the characteristic of $F$ |
| $\mathbb{F}_p$ | Prime field, the fixed field of the Frobenius |
| $\varphi(x) = x^p$ | Frobenius operator |
| $\varphi^n(x) = x^{p^n}$ | Iterated Frobenius |
| $(x+y)^p = x^p+y^p$ | Freshman's dream; additivity of $\varphi$ |
| $F^p = \{x^p\}$ | Image of $\varphi$, a subfield |
| $F = F^p$ | Perfect field; $\varphi$ is an automorphism |
| $[\mathbb{F}_p(t) : \mathbb{F}_p(t^p)] = p$ | The standard imperfect example |
| $F^\varphi = \mathbb{F}_p$ | Fixed field of $\varphi$ |
| $\operatorname{Gal}(\mathbb{F}_{p^n}/\mathbb{F}_p) = \langle\varphi\rangle \cong \mathbb{Z}/n$ | Finite-field Galois group |
| $D(x^p) = 0$, $F^p \subseteq F^D$ | Derivations kill the Frobenius image |
| $\partial/\partial t$ on $\mathbb{F}_p(t)$ | Nonzero derivation, zero on $F^p$ |

## Further Reading

- Serge Lang, *Algebra*, 3rd ed. (Springer, 2002), for the Frobenius endomorphism, perfect and imperfect fields and purely inseparable extensions.
- Nathan Jacobson, *Basic Algebra I*, 2nd ed. (Dover, 2009), for the Frobenius map, the freshman's dream and the structure of finite fields.
- Rudolf Lidl and Harald Niederreiter, *Finite Fields*, Encyclopedia of Mathematics and its Applications 20 (Cambridge University Press, 2nd ed. 1997), for the Frobenius as the generator of the Galois group of a finite field and the subfield lattice.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for characteristic $p$ phenomena, derivations and their vanishing on $p$-th powers.
