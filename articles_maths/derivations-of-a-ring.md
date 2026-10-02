
# __Derivations of a Ring__

## Introduction

A **derivation** of a ring is an additive operator $D$ that satisfies the Leibniz rule
$D(xy) = D(x)y + x\,D(y)$. It is the algebraic form of the infinitesimal variation of a product, and it is the first operator on a ring that is defined by a rule rather than by an element: the left and right multiplications are read off an element $a$, an automorphism is an invertible multiplicative map, while a derivation is constrained by the product alone and need not come from any element. This article defines the derivations of a ring, proves the elementary rules they obey, and studies the two structures they carry: the **Lie ring** they form under the commutator $[D,E] = DE - ED$, and the **inner derivations** $\operatorname{ad}_a(x) = ax - xa$ cut out by the elements.

The article is purely algebraic. The Leibniz rule is a rule about the two operations of the ring and nothing else; no distance, norm, limit or derivative in the analytic sense occurs, and a derivation is never integrated. The linearisation of a group action, the one-parameter groups of automorphisms, and the exponential that recovers them from their infinitesimal generators are analytic subjects, and they belong to Part III; what is recorded here is the algebraic statement that a derivation is the linear part of an automorphism, together with the one case in which the exponential is a finite algebraic sum.

The vocabulary is that of *Rings* for the object, its centre $Z(A)$, its units $A^\times$ and its ideals, *Commutative Rings* and *Integral Domains* for the polynomial examples, and *Ring and Field Automorphisms* for the automorphism group. The derivations of the algebras of the ladder, the Skolem–Noether theorem and the Kähler differentials are named where they would enter and deferred: the first two to *Automorphisms and Derivations of Algebras* in the category *Linear Algebras*, the last to *Change of Rings*. Throughout, $A$ is a ring with $1 \neq 0$, not assumed commutative; a derivation is a derivation of $A$ into itself unless a module of values is named, and the word **operator** means an additive map $A \to A$.

## The Leibniz Rule

### Definition and elementary properties

**Definition.** A **derivation** of the ring $A$ is an additive map $D : A \to A$ such that for all $x, y \in A$

$$
D(x+y) = D(x) + D(y), \qquad D(xy) = D(x)\,y + x\,D(y).
$$

The set of all derivations of $A$ is written $\operatorname{Der}(A)$. The **trivial derivation** is $D = 0$.

**Proposition.** Let $D \in \operatorname{Der}(A)$.

**(a)** $D(0) = 0$ and $D(-x) = -D(x)$; more generally $D$ is $\mathbb{Z}$-linear, $D(nx) = nD(x)$ for $n \in \mathbb{Z}$.

**(b)** $D(1) = 0$, and $D$ kills the prime subring: $D(n\cdot 1) = 0$ for every integer $n$.

**(c)** $D(x^n) = \displaystyle\sum_{i=0}^{n-1} x^{i}\,D(x)\,x^{n-1-i}$ for $n \geq 1$. When $x$ and $D(x)$ commute this collapses to $D(x^n) = n\,x^{n-1}D(x)$.

**(d)** If $u \in A^\times$ then $u^{-1}D(u)u^{-1} \in A$ and

$$
D(u^{-1}) = -u^{-1}\,D(u)\,u^{-1}.
$$

**(e)** $D$ maps the centre into the centre only when it annihilates it; in general $D(Z(A)) \subseteq Z(A)$, and in particular the restriction of $D$ to the centre is a derivation of the commutative ring $Z(A)$.

**Proof.** (a) Additivity gives $D(0) = D(0+0) = D(0)+D(0)$ and $D(-x)+D(x) = D(0) = 0$; the integer statement follows by iteration. (b) $D(1) = D(1\cdot 1) = D(1)\cdot 1 + 1\cdot D(1) = 2D(1)$ gives $D(1) = 0$ in every ring, since subtracting $D(1)$ from both sides gives $D(1) = 0$; then $D(n\cdot 1) = nD(1) = 0$. (c) Induction on $n$: $D(x^{n+1}) = D(x^n)x + x^nD(x) = \bigl(\sum_{i=0}^{n-1}x^{i}D(x)x^{n-1-i}\bigr)x + x^nD(x) = \sum_{i=0}^{n}x^{i}D(x)x^{n-i}$. (d) From $uu^{-1} = 1$ one gets $0 = D(u)u^{-1} + uD(u^{-1})$, and multiplying on the left and on the right by $u^{-1}$ gives (d). (e) If $z \in Z(A)$ and $x \in A$, then $D(zx) = D(xz)$, that is, $D(z)x + zD(x) = D(x)z + xD(z)$; subtracting $zD(x) = D(x)z$ leaves $D(z)x = xD(z)$, so $D(z) \in Z(A)$. The restriction to $Z(A)$ is additive and satisfies the Leibniz rule, hence is a derivation of the commutative ring $Z(A)$.

**Remark.** The rule $D(1) = 0$ needs no characteristic hypothesis: it is the cancellation of the common term $D(1)$ in $D(1) = 2D(1)$. The rule $D(x^n) = nx^{n-1}D(x)$ likewise needs no hypothesis when $x$ and $D(x)$ commute, which is automatic in a commutative ring, and the integer $n$ is read in the prime subring.

### The derivation of a product and of a quotient

The Leibniz rule extends from two factors to any finite list, and the extension is the algebraic statement that a derivation acts as a sum of partial differentiations.

**Proposition (the product rule).** For $x_1, \dots, x_n \in A$,

$$
D(x_1 x_2 \cdots x_n) = \sum_{i=1}^{n} x_1 \cdots x_{i-1}\, D(x_i)\, x_{i+1} \cdots x_n .
$$

**Proof.** Induction on $n$, the case $n = 1$ being the definition and the step being the two-factor rule applied to $x_1\cdots x_{n-1}$ and $x_n$.

**Corollary.** A derivation of a commutative ring is determined by its values on any generating set, and it acts on a monomial by the sum of the partial derivations with respect to the generators. This is the algebraic form of the partial derivative, and it is why the polynomial ring below has a basis of derivations indexed by the individual variables.

### Examples

**(a) The trivial derivation.** $D = 0$ is a derivation of every ring.

**(b) Derivations of the polynomial ring.** In $R[x]$ over a commutative ring $R$, the formal operator

$$
\frac{d}{dx}\Bigl(\sum_i r_i x^i\Bigr) = \sum_i i\,r_i\,x^{i-1}
$$

is a derivation, the **formal derivative**, and it is $R$-linear. The derivations of $R[x]$ that are zero on $R$ form the free $R[x]$-module on $\dfrac{d}{dx}$; over a field of characteristic $0$ this is the whole $R[x]$-module of derivations. Over a field of characteristic $p$ the formal derivative is not the only one: it is the one that annihilates $R[x^p]$.

**(c) Derivations of a matrix ring.** For $A = M_n(R)$ over a commutative ring $R$, every derivation is inner, $D(X) = MX - XM$ for some matrix $M$: the module of derivations is the image of $\operatorname{ad} : M_n(R) \to \operatorname{Der}(M_n(R))$. This is the matrix instance of the theorem of the next-to-last section and it is proved there.

**(d) Derivations of a field of characteristic $p$.** If $F$ is a field of characteristic $p$, then $D(x^p) = p\,x^{p-1}D(x) = 0$ for every derivation and every $x$, so a derivation of $F$ kills the subfield $F^p$ of $p$-th powers. Over a perfect field $F^p = F$ and therefore $\operatorname{Der}(F) = 0$; over an imperfect field such as $\mathbb{F}_p(t)$ the derivation $\partial/\partial t$ is nonzero and kills $\mathbb{F}_p(t^p)$.

**(e) A derivation with $D^2 = 0$.** In the dual numbers $R[\varepsilon]/(\varepsilon^2)$, the map $\varepsilon \mapsto 1$, $1 \mapsto 0$ is a derivation with $D^2 = 0$. It is the algebraic model of a first-order variation.

## The Lie Ring of Derivations

### The commutator of two derivations

**Theorem.** If $D, E \in \operatorname{Der}(A)$, then the commutator

$$
[D, E] = D \circ E - E \circ D
$$

is again a derivation of $A$. The set $\operatorname{Der}(A)$ is therefore closed under $[\cdot,\cdot]$ and contains $0$; with this bracket it is a **Lie ring**, that is, an additive group in which the bracket is bilinear over $\mathbb{Z}$, alternating, $[D,D] = 0$, and satisfies the Jacobi identity.

**Proof.** The bracket is additive in each variable and alternating since $[D,D]=0$. For the Leibniz rule, compute on a product:

$$
DE(xy) - ED(xy) = D\bigl(E(x)y + xE(y)\bigr) - E\bigl(D(x)y + xD(y)\bigr).
$$

Expanding and cancelling the four mixed terms $E(x)D(y)$, $D(x)E(y)$, $E(x)D(y)$, $D(x)E(y)$ leaves

$$
\bigl(DE(x) - ED(x)\bigr)y + x\bigl(DE(y) - ED(y)\bigr) = [D,E](x)\,y + x\,[D,E](y),
$$

which is the Leibniz rule for $[D,E]$. The Jacobi identity is the associativity of composition read through the bracket, and holds in every associative ring.

**Remark.** The commutator is not defined by an element, and the bracket of two derivations need not be zero; the Lie ring $\operatorname{Der}(A)$ is therefore a genuinely new structure built on $A$. It is a ring, not a field, and it is a Lie ring and not an associative one: the composition $D\circ E$ is in general not a derivation, and only its antisymmetrisation is.

### The Lie algebra structure

When $A$ is a $k$-algebra over a commutative ring $k$, the derivations that are $k$-linear form the **$k$-linear derivations** $\operatorname{Der}_k(A)$, and this subset is closed under the bracket and under multiplication by $k$. It is then a **Lie algebra** over $k$.

**Proposition.** $\operatorname{Der}_k(A)$ is a $k$-submodule of $\operatorname{End}_k(A)$ and a Lie algebra over $k$; $\operatorname{Der}(A) = \operatorname{Der}_{\mathbb{Z}}(A)$.

**Proof.** A $k$-linear derivation is $k$-linear as an operator and satisfies the Leibniz rule; both conditions are preserved by $k$-linear combinations, and the bracket of two $k$-linear maps is $k$-linear. The last identity records that $\mathbb{Z}$-linearity is additivity.

**Examples of Lie algebras of derivations.** $\operatorname{Der}_R(R[x])$ is the free $R[x]$-module on $\frac{d}{dx}$ with bracket $0$, since all the elements are $R[x]$-multiples of one derivation and commute. For the algebra of dual numbers $\mathbb{D}' = R[\varepsilon]/(\varepsilon^2)$ the derivations that kill $R$ form the one-dimensional space $R\cdot\partial_\varepsilon$, again abelian. For $M_n(R)$ the derivations are inner and the Lie algebra $\operatorname{Der}(M_n(R))$ is the quotient of $\mathfrak{gl}_n(R) = M_n(R)$ by the scalars.

## Inner Derivations

### Definition and the adjoint map

**Definition.** For $a \in A$ the **inner derivation** determined by $a$ is

$$
\operatorname{ad}_a : A \to A, \qquad \operatorname{ad}_a(x) = ax - xa = [a, x].
$$

The inner derivations form the image of the map $\operatorname{ad} : A \to \operatorname{Der}(A)$.

**Proposition.** For every $a \in A$, $\operatorname{ad}_a$ is a derivation; the map $\operatorname{ad}$ is additive and satisfies

$$
[\operatorname{ad}_a, \operatorname{ad}_b] = \operatorname{ad}_{[a,b]}, \qquad \operatorname{ad}_a = 0 \iff a \in Z(A).
$$

Hence $\operatorname{ad}$ is a homomorphism of Lie rings $A \to \operatorname{Der}(A)$ with kernel the centre, so that

$$
\operatorname{Inn}_{\mathrm{der}}(A) := \operatorname{ad}(A) \;\cong\; A / Z(A)
$$

as Lie rings. The elements of $\operatorname{Inn}_{\mathrm{der}}(A)$ are the **inner derivations**.

**Proof.** $\operatorname{ad}_a(xy) = a xy - xy a$ and $\operatorname{ad}_a(x)y + x\operatorname{ad}_a(y) = (ax-xa)y + x(ay-ya) = axy - xay + xay - xya = axy - xya$. Additivity is immediate. For the bracket, both sides are derivations that agree on a generating set: $[\operatorname{ad}_a,\operatorname{ad}_b](x) = a(bx-xb) - (bx-xb)a - b(ax-xa) + (ax-xa)b = abx - axb - bxa + xba - bax + bxa + axb - xab = (ab-ba)x - x(ab-ba) = \operatorname{ad}_{[a,b]}(x)$, all middle terms cancelling. Finally $\operatorname{ad}_a = 0$ says $ax = xa$ for all $x$, that is, $a \in Z(A)$.

**Example.** In $A = M_2(\mathbb{Q})$ with $a = E_{12}$ and $x = E_{21}$ one has $\operatorname{ad}_a(x) = E_{12}E_{21} - E_{21}E_{12} = E_{11} - E_{22}$, so $\operatorname{ad}_{E_{12}} \neq 0$ and $E_{12} \notin Z(A)$.

### The inner derivations as a Lie ideal

**Theorem.** $\operatorname{Inn}_{\mathrm{der}}(A)$ is a Lie ideal of $\operatorname{Der}(A)$: for every derivation $D$ and every $a \in A$,

$$
[D, \operatorname{ad}_a] = \operatorname{ad}_{D(a)} .
$$

Hence $\operatorname{Inn}_{\mathrm{der}}(A) \trianglelefteq \operatorname{Der}(A)$ as Lie rings, and the quotient $\operatorname{Out}_{\mathrm{der}}(A) = \operatorname{Der}(A)/\operatorname{Inn}_{\mathrm{der}}(A)$ is the Lie ring of **outer derivations**.

**Proof.** Both sides are derivations; compute on $x$: $D(\operatorname{ad}_a(x)) - \operatorname{ad}_a(D(x)) = D(ax - xa) - aD(x) + D(x)a = D(a)x + aD(x) - D(x)a - xD(a) - aD(x) + D(x)a = D(a)x - xD(a) = \operatorname{ad}_{D(a)}(x)$.

**Remark.** The quotient is a Lie ring and not in general the Lie algebra of an automorphism group; the relation between the derivation-outer and the automorphism-outer parts is a subject of the algebra layer, where the Skolem–Noether theorem identifies the two for a central simple algebra. Here the exact sequence

$$
0 \longrightarrow Z(A) \longrightarrow A \xrightarrow{\ \operatorname{ad}\ } \operatorname{Der}(A) \longrightarrow \operatorname{Out}_{\mathrm{der}}(A) \longrightarrow 0
$$

is exact by construction; its last term is $\operatorname{Der}(A)/\operatorname{Inn}_{\mathrm{der}}(A)$, and nothing in this article computes it.

**Corollary (the Jacobi identity is the Leibniz rule on the bracket).** The fact that $\operatorname{ad}$ is a Lie homomorphism is exactly the statement that $\operatorname{ad}_a$ acts on the bracket of derivations by the Leibniz rule, $[a,[D,E]] = [[a,D],E] + [D,[a,E]]$. This is the Jacobi identity of the Lie ring $\operatorname{Der}(A)$, and it is why $\operatorname{ad}$ is a representation of the Lie ring $A/Z(A)$ on the space $\operatorname{Der}(A)$.

## Derivations and Automorphisms

### The linearisation of an automorphism

A derivation is the algebraic first-order part of an automorphism. The precise statement available without a distance is the following finiteness result.

**Proposition (a nilpotent derivation gives an automorphism).** Let $D \in \operatorname{Der}(A)$ with $D^{n+1} = 0$. Then

$$
\exp(D) = \sum_{i=0}^{n} \frac{D^i}{i!}
$$

is well defined whenever the integers $1, \dots, n$ are invertible in $A$, and it is a ring automorphism of $A$, with inverse $\exp(-D)$. Its derivative at the identity is $D$: the linear term of $\exp(D)$ is $D$.

**Proof.** The sum is finite by hypothesis. The product rule for exponentials holds for commuting operators, and $D$ commutes with every power $D^i$ of itself, so $\exp(D)\exp(-D) = \exp(0) = 1$. For multiplicativity, $\exp(D)$ is a limit of polynomials in the derivation $D$, and each polynomial in $D$ is an endomorphism of the additive group; the multiplicativity of $\exp(D)$ follows from the formula $D^k(xy) = \sum_{i+j=k}\binom{k}{i}D^i(x)D^j(y)$, which is the Leibniz rule iterated, and the division by $k!$. The linear term is the $i=1$ term.

**Example.** In $R[\varepsilon]/(\varepsilon^2)$ with $D(\varepsilon) = 1$, $D(1) = 0$, one has $D^2 = 0$ and $\exp(D) = \mathrm{id} + D$, an automorphism if $2$ is invertible. The map sends $\varepsilon \mapsto \varepsilon + 1$ and is the algebraic form of an infinitesimal translation.

### Derivations vanishing on a subring

**Definition.** Let $S \subseteq A$ be a subring. The derivations of $A$ that annihilate $S$ are written

$$
\operatorname{Der}_S(A) = \{D \in \operatorname{Der}(A) : D(s) = 0 \text{ for all } s \in S\}.
$$

This is a Lie subring of $\operatorname{Der}(A)$, and it is a module over the centraliser of $S$: for $c$ commuting with $S$, $cD$ is again a derivation vanishing on $S$ when $cD$ is additive and satisfies the rule, which it does if $c \in Z(A)$.

**Proposition.** $\operatorname{Der}_S(A)$ is a Lie subring of $\operatorname{Der}(A)$ and a submodule over $Z(A)$; it is the kernel of the restriction map $\operatorname{Der}(A) \to \operatorname{Der}(S)$, which is a homomorphism of Lie rings.

**Proof.** A derivation vanishing on $S$ restricts to the zero derivation of $S$, so the set is the kernel of a Lie-ring homomorphism, hence a Lie ideal and in particular a Lie subring. For centrality, if $c \in Z(A)$ then $cD$ is additive and $(cD)(xy) = c(D(x)y + xD(y)) = (cD)(x)y + x(cD)(y)$, and $(cD)(s) = c\cdot 0 = 0$.

## Summary

A derivation of the ring $A$ is an additive operator satisfying $D(xy) = D(x)y + xD(y)$. It satisfies $D(0)=0$, $D(1)=0$, $D(-x)=-D(x)$, the product rule over any finite list, the power rule $\sum_i x^iD(x)x^{n-1-i}$ for $x^n$, and the rule $D(u^{-1}) = -u^{-1}D(u)u^{-1}$ for a unit; it carries the centre into the centre. The formal derivative of a polynomial ring, the inner derivations of a matrix ring, and the derivation $\partial/\partial t$ of an imperfect field are the standard examples; in characteristic $p$ every derivation kills $p$-th powers, so a perfect field has no nonzero derivation.

The derivations are closed under the commutator $[D,E] = DE - ED$, which is again a derivation, and form the Lie ring $\operatorname{Der}(A)$; over a commutative base $k$ the $k$-linear derivations form the Lie algebra $\operatorname{Der}_k(A)$. The map $a \mapsto \operatorname{ad}_a$, $\operatorname{ad}_a(x) = ax - xa$, is a homomorphism of Lie rings $A \to \operatorname{Der}(A)$ with kernel $Z(A)$ and image the inner derivations $\operatorname{Inn}_{\mathrm{der}}(A) \cong A/Z(A)$, and $[D,\operatorname{ad}_a] = \operatorname{ad}_{D(a)}$ shows that the inner derivations form a Lie ideal, with the outer derivations as the quotient $\operatorname{Der}(A)/\operatorname{Inn}_{\mathrm{der}}(A)$. A derivation is the linear part of an automorphism; when it is nilpotent and the necessary integers are invertible, its exponential is an automorphism with that linear part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | Ring with $1 \neq 0$, not assumed commutative |
| $D, E$ | Derivations of $A$; additive maps with the Leibniz rule |
| $\operatorname{Der}(A)$ | Lie ring of derivations, bracket $[D,E] = DE - ED$ |
| $\operatorname{Der}_k(A)$ | $k$-linear derivations, a Lie algebra over a commutative base $k$ |
| $\operatorname{ad}_a(x) = ax - xa = [a,x]$ | Inner derivation determined by $a$ |
| $\operatorname{Inn}_{\mathrm{der}}(A) = \operatorname{ad}(A) \cong A/Z(A)$ | Lie ideal of inner derivations |
| $\operatorname{Out}_{\mathrm{der}}(A) = \operatorname{Der}(A)/\operatorname{Inn}_{\mathrm{der}}(A)$ | Lie ring of outer derivations |
| $[D,\operatorname{ad}_a] = \operatorname{ad}_{D(a)}$ | Inn is a Lie ideal |
| $\operatorname{Der}_S(A)$ | Derivations annihilating a subring $S$ |
| $\exp(D)$ | Automorphism of a nilpotent derivation when the integers are invertible |
| $Z(A)$, $A^\times$ | Centre and unit group of $A$ |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the Lie algebra of derivations, the inner derivations and the exact sequence obtained from the adjoint map.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1956), for derivations of rings, the inner derivations and the derivations of a matrix ring.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for derivations, the module of derivations and the functorial description of the Kähler differentials.
- Serge Lang, *Algebra*, 3rd ed. (Springer, 2002), for derivations of fields, the behaviour of a derivation on $p$-th powers and the derivations of a separable extension.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for derivations commuting with an involution and the Lie structure they carry.
