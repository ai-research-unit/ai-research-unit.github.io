
# __Involutions of a Polynomial Ring and the Symmetric Part__

## Introduction

The polynomial ring $R[x]$ over a commutative ring $R$ with an involution $\sigma$ carries involutions obtained by sending $x$ to a polynomial $f$ and the coefficients by $\sigma$; the smallest interesting one is $x \mapsto -x$, whose fixed subring is $R[x^2]$ and which turns $R[x]$ into a $\mathbb{Z}/2$-graded ring with even part $R[x^2]$ and odd part $xR[x^2]$. The general involution of $R[x]$ that restricts to $\sigma$ on the coefficients is determined by $f$, it is an involution exactly when $f \circ f = x$ and $f$ is compatible with $\sigma$, and the affine ones $f(x) = ax+b$ are classified by the two conditions $a\sigma(a) = 1$ and $\sigma(a)b + \sigma(b) = 0$; the map $x \mapsto -x$ is the case $a = -1$ and $b$ a fixed element, and the identity is the case $a = 1$.

This article treats those involutions, the symmetric part they define, and the graded decomposition that the involution $x \mapsto -x$ induces. It opens with the structure of an involution of $R[x]$, continues with the symmetric part and the grading, and closes with the examples of $x \mapsto -x$, of the conjugation of $\mathbb{R}[x]$ inside $\mathbb{C}[x]$, and of the characteristic-$p$ phenomena. It assumes *Polynomial Rings and Rational Functions* for the polynomial ring and its degree, *Involutive Rings* for the involution and its fixed ring, and *Ring and Field Automorphisms* for the automorphisms of $R[x]$; the symmetric and skew elements are *The Skew Field of a Ring with Involution*, the article of this group that follows. Throughout, $R$ is a commutative ring with $1 \neq 0$ and an involution $\sigma$, and $R[x]^+$ denotes the fixed subring of an involution.

## Involutions of R[x]

**Definition.** Let $f \in R[x]$. The **involution of $R[x]$ determined by $f$** is the additive map

$$
\Bigl(\sum_i a_i x^i\Bigr)^{\sigma,f} = \sum_i \sigma(a_i)\,f(x)^i ;
$$

it restricts to $\sigma$ on the constants and sends $x$ to $f$.

**Theorem.** The map $(\,)^{\sigma,f}$ is a ring homomorphism for every $f$, because $R[x]$ is commutative, and it is an involution if and only if

$$
\sigma^2 = \mathrm{id}, \qquad f(f(x)) = x, \qquad \text{and the coefficients of } f \text{ are twisted compatibly with } \sigma .
$$

The involution is the identity on $R[x]$ exactly when $\sigma = \mathrm{id}$ and $f = x$.

**Proof.** The map is additive by construction, it sends $1$ to $1$, and it is multiplicative because it is an evaluation of the commutative ring $R[x]$ with the coefficients twisted: $(gh)^{\sigma,f} = g^{\sigma,f}h^{\sigma,f}$ for all $g,h$ once the coefficients of $f$ satisfy $\sigma(c)f(x) = f(x)\sigma(c)$, which holds automatically in the commutative ring. Applying the map twice gives $x \mapsto f(f(x))$ and $a_i \mapsto \sigma^2(a_i)$, so the square is the identity exactly under the stated conditions; the triviality statement is the comparison of $x$ and of the coefficients.

**Proposition (affine involutions).** An involution of $R[x]$ with $f(x) = ax+b$ of degree one restricts to $\sigma$ on $R$ and satisfies the conditions

$$
a\,\sigma(a) = 1, \qquad \sigma(a)\,b + \sigma(b) = 0 .
$$

Conversely every pair $(a,b)$ with these two conditions and $\sigma^2 = \mathrm{id}$ determines an affine involution, $(\sum a_i x^i)^{\sigma,f} = \sum \sigma(a_i)(ax+b)^i$.

**Proof.** Let $\Phi$ be the twisted evaluation. Then $\Phi^2(x) = \Phi(ax+b) = \sigma(a)\Phi(x)+\sigma(b) = \sigma(a)a\,x + \sigma(a)b + \sigma(b)$; the square is the identity on $x$ exactly when $\sigma(a)a = 1$ and $\sigma(a)b+\sigma(b) = 0$, and on the coefficients it is $\sigma^2 = \mathrm{id}$. The converse is the same computation.

**Corollary (the two basic affine cases).** The affine involution $x \mapsto -x+b$ is the case $a = -1$, for which $\sigma(a)b+\sigma(b) = -b+\sigma(b)$ vanishes exactly when $b$ is fixed; the identity is the case $a = 1$ and $b$ with $2b = 0$. When $2$ is invertible in $R$, the affine involutions are exactly $x \mapsto -x+b$ with $b \in R^\sigma$, together with the identity.

**Proof.** For $a = -1$ the first condition is $(-1)(-1) = 1$, automatic, and the second is $-b+\sigma(b) = 0$; for $a = 1$ the second is $2b = 0$. When $2$ is invertible the only solution of $2b = 0$ is $b = 0$, giving the identity.

**Theorem (degree two and beyond).** If $R$ is an integral domain and $\deg$ is multiplicative on $R[x]$, then every involution of $R[x]$ restricting to $\sigma$ on the coefficients is affine: $\deg(f\circ f) = (\deg f)^2 = 1$ forces $\deg f = 1$. Over a ring with zero divisors and nilpotents there are non-affine involutions, the smallest being $x \mapsto x + t$ in $R[x]$ with $t^2 = 0$ and $t$ fixed, which has order two.

**Proof.** $R[x]$ is an integral domain when $R$ is, and the degree of a composition of nonconstant polynomials is the product of the degrees; $\deg(\mathrm{id}) = 1$ gives $(\deg f)^2 = 1$, so $f$ is linear. For the example, $(x+t)\circ(x+t) = x+2t+t^2 = x$ when $2t = 0$ and $t^2 = 0$, and the twisted evaluation by $\sigma = \mathrm{id}$ has order two.

## The Symmetric Part and the Grading

**Theorem.** The involution $x \mapsto -x$ of $R[x]$ has fixed subring

$$
R[x]^{+} = R[x^2] = \{g(x^2) : g \in R[x]\},
$$

the polynomials in $x^2$, and it induces the $\mathbb{Z}/2$-grading

$$
R[x] = R[x^2] \oplus x\,R[x^2],
$$

with even part $R[x^2]$ and odd part $xR[x^2]$. The symmetric part is the even part and the skew part is the odd part.

**Proof.** A polynomial $\sum a_i x^i$ is fixed by $x \mapsto -x$ exactly when the coefficients of the odd powers vanish, that is, when it is a polynomial in $x^2$; the direct sum is the grouping of the even and the odd powers, and the product of an element of $x^iR[x^2]$ and one of $x^jR[x^2]$ lies in $x^{i+j}R[x^2]$, which is the grading. The identification of the eigenspaces is the additive decomposition of *Involutive Rings*.

**Corollary (the affine case as a translation).** For the involution $x \mapsto -x+b$ with $b \in R^\sigma$ and $2$ invertible, the translation $y = x - b/2$ carries it to $y \mapsto -y$, and the fixed subring is $R[(x-b/2)^2]$, with the grading $R[x] = R[(x-b/2)^2] \oplus (x-b/2)R[(x-b/2)^2]$.

**Proof.** $x \mapsto -x+b$ is the reflection of the line about $b/2$, so the substitution $y = x-b/2$ makes it $y \mapsto -y$; the fixed subring and the grading are those of the previous theorem transported by the automorphism $x \mapsto x+b/2$ of $R[x]$, which is legitimate because $b$ is fixed.

**Remark.** For the involution $x \mapsto -x$ with $\sigma = \mathrm{id}$ the fixed subring $R[x^2]$ is a polynomial ring in $x^2$ and $R[x]$ is free over it with basis $1, x$; for a general affine involution the fixed subring is the intersection of the coefficient conditions with the vanishing of the odd powers of the translate and need not be a polynomial ring in one element.

## Examples

**(a) The basic case.** $R[x]$ with $\sigma = \mathrm{id}$ and $x \mapsto -x$ has fixed subring $R[x^2]$ and the grading $R[x] = R[x^2]\oplus xR[x^2]$; this is the model of the $\mathbb{Z}/2$-grading by parity of degree.

**(b) The conjugation of the real polynomials.** $R = \mathbb{C}$, $\sigma$ the conjugation, $f = x$: the involution is the coefficientwise conjugation, its fixed subring is $\mathbb{R}[x]$ inside $\mathbb{C}[x]$, and the pair is the quadratic extension $\mathbb{C}[x]/\mathbb{R}[x]$.

**(c) The conjugation twisted.** $R = \mathbb{C}$, $\sigma$ the conjugation, $f = -x$: the fixed subring consists of the polynomials with real coefficients in the even powers and purely imaginary coefficients in the odd powers, that is the ring $\mathbb{R}[x^2] \oplus i\,x\,\mathbb{R}[x^2]$, a free $\mathbb{R}[x^2]$-module of rank two.

**(d) The involution of the circle.** $R = \mathbb{R}$, $f = -x$: the fixed subring $\mathbb{R}[x^2]$; the ring $\mathbb{R}[x]/(x^2+1) = \mathbb{C}$ carries the induced conjugation, which is the involution $i \mapsto -i$, and the fixed field is $\mathbb{R}$.

**(e) Characteristic two.** $R = \mathbb{F}_2$ with $\sigma = \mathrm{id}$: the involution $x \mapsto -x$ is the identity, since $-x = x$; the affine involutions satisfy $2b = 0$ automatically, and $x \mapsto x+1$ is an involution whose fixed subring is the constants $\mathbb{F}_2$, because a nonconstant polynomial cannot satisfy $g(x+1) = g(x)$ over $\mathbb{F}_2$.

**(f) The power series case.** The same computation gives the involution $t \mapsto -t$ of $k[[t]]$ with fixed subring $k[[t^2]]$ and the grading $k[[t]] = k[[t^2]]\oplus t\,k[[t^2]]$; this is the local analogue of (a) and is used in *Involutive Local Rings*.

## Summary

An involution of $R[x]$ that restricts to $\sigma$ on the coefficients is determined by a polynomial $f$ and sends $\sum a_i x^i$ to $\sum \sigma(a_i)f(x)^i$; it is an involution exactly when $\sigma^2 = \mathrm{id}$ and $f \circ f = x$ with the coefficient compatibility, and it is an automorphism because $R[x]$ is commutative. The affine involutions $f(x) = ax+b$ are classified by $a\sigma(a) = 1$ and $\sigma(a)b+\sigma(b) = 0$; over a field $R$ of characteristic zero, or over any integral domain with a multiplicative degree, every involution is affine, and when $2$ is invertible the only ones are the identity and $x \mapsto -x+b$ with $b$ fixed. Over a ring with nilpotents there are non-affine involutions, such as $x \mapsto x+t$ with $t^2 = 0$.

The involution $x \mapsto -x$ is the model of the $\mathbb{Z}/2$-grading: its fixed subring is $R[x^2]$, the symmetric part is the even part and the skew part is the odd part, and $R[x] = R[x^2]\oplus xR[x^2]$. The affine involution $x \mapsto -x+b$ is the translate of this one by $b/2$, with fixed subring $R[(x-b/2)^2]$, and the conjugation of $\mathbb{C}[x]$ over $\mathbb{R}[x]$, the twisted case $x \mapsto -x$, the circle example $\mathbb{R}[x]/(x^2+1)$ and the power series analogue are the standard instances.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $\sigma$ | Commutative ring and its involution |
| $f \in R[x]$ | The polynomial to which $x$ is sent |
| $(\sum a_i x^i)^{\sigma,f} = \sum \sigma(a_i)f^i$ | The involution determined by $f$ |
| $f\circ f = x$, $\sigma^2 = \mathrm{id}$ | Conditions for the map to be an involution |
| $f = ax+b$, $a\sigma(a) = 1$, $\sigma(a)b+\sigma(b) = 0$ | Classification of the affine involutions |
| $x \mapsto -x$ | The basic involution; fixed subring $R[x^2]$ |
| $R[x] = R[x^2]\oplus xR[x^2]$ | The induced $\mathbb{Z}/2$-grading |
| $x \mapsto -x+b$, $b \in R^\sigma$ | Affine case, translate of $x \mapsto -x$ by $b/2$ |
| $\mathbb{R}[x] \subset \mathbb{C}[x]$ | Conjugation example |
| $\mathbb{F}_2[x]$, $x \mapsto x+1$ | Characteristic-two involution; dual numbers |

## Further Reading

- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for the automorphisms of a polynomial ring and the degree of a composition.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the involutions of $R[x]$, their fixed subrings and the affine classification.
- Nicolas Bourbaki, *Algebra II* (Springer, 2003), for the graded structures, the fixed rings and the invariants of an order-two automorphism.
- Michael Atiyah and Ian Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, 1969), for the polynomial ring, the power series ring and their maximal ideals.
