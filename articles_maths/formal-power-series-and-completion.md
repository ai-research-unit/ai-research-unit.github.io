# __Formal Power Series and Completion__

## Introduction

This article completes the polynomial algebra at its augmentation ideal and identifies the result with the algebra of formal power series. The base structure is a **commutative ring** $R$ with identity $1 \neq 0$, and the algebra conventions are those of *Commutative Algebras*: the category $\mathsf{CAlg}_R$, free objects, tensor products and spectra. The symmetric algebra of *The Symmetric Algebra* and its graded pieces, the symmetric powers of *Symmetric Powers*, supply the associated graded object that the completion forgets.

The construction is the $I$-adic completion

$$
\hat A = \varprojlim_k A/I^k,
$$

for an ideal $I \subseteq A$. Applied to the polynomial algebra $R[x_1, \ldots, x_n]$ at the ideal $\mathfrak{m} = (x_1, \ldots, x_n)$ of polynomials with zero constant term, it produces the algebra $R[[x_1, \ldots, x_n]]$ of formal power series. The two algebras carry the same generators and the same linear terms but differ in what they allow: a polynomial must be finite, a formal power series may be infinite, and the completion is exactly the device that admits the infinite sums while keeping every individual computation finite.

The article develops the basic algebra of formal power series, the order and the $\mathfrak{m}$-adic topology, the completion functor and the completion of the polynomial algebra, the formal inverse function theorem with its contraction proof, and the relation between completion, the symmetric algebra and Taylor expansion. The formal inverse function theorem is derived here, not cited, because its proof is the clean illustration of why $\mathfrak{m}$-adic completeness is the right hypothesis.

## Formal Power Series

### Definition and Order

Let $R$ be a commutative ring and let $x_1, \ldots, x_n$ be indeterminates. A **formal power series** in the $x_i$ with coefficients in $R$ is a formal expression

$$
f = \sum_{(a_1,\ldots,a_n) \in \mathbb{N}^n} c_{a_1\ldots a_n} x_1^{a_1}\cdots x_n^{a_n}, \qquad c_{a_1\ldots a_n} \in R,
$$

with no restriction on the number of nonzero coefficients. The set of all such series is written $R[[x_1, \ldots, x_n]]$, and the sum and product are the formal ones,

$$
\Bigl(\sum_a c_a x^a\Bigr) + \Bigl(\sum_a d_a x^a\Bigr) = \sum_a (c_a + d_a)x^a, \qquad \Bigl(\sum_a c_a x^a\Bigr)\Bigl(\sum_b d_b x^b\Bigr) = \sum_{a, b} c_a d_b x^{a+b},
$$

the second being finite in each degree because there are only finitely many pairs $(a,b)$ with $a + b$ fixed. With these operations $R[[x_1,\ldots,x_n]]$ is a commutative $R$-algebra, the **formal power series algebra**, and it contains the polynomial algebra $R[x_1,\ldots,x_n]$ as the subalgebra of series with finitely many nonzero coefficients.

The **order** of a nonzero series $f$ is

$$
\operatorname{ord}(f) = \min\{a_1 + \cdots + a_n : c_{a_1\ldots a_n} \neq 0\},
$$

with $\operatorname{ord}(0) = +\infty$. The order satisfies $\operatorname{ord}(f+h) \geq \min(\operatorname{ord} f, \operatorname{ord} h)$ and $\operatorname{ord}(fh) \geq \operatorname{ord} f + \operatorname{ord} h$; over a domain the second is an equality.

### The Augmentation Ideal and the $\mathfrak{m}$-adic Filtration

Let

$$
\mathfrak{m} = (x_1, \ldots, x_n) = \{f : \operatorname{ord}(f) \geq 1\}
$$

be the ideal of series vanishing at the origin, the **augmentation ideal**. Its powers are the sets of series of order at least $k$,

$$
\mathfrak{m}^k = \{f : \operatorname{ord}(f) \geq k\},
$$

so the $\mathfrak{m}$-adic filtration of $R[[x_1,\ldots,x_n]]$ is the order filtration. The quotients are

$$
R[[x_1,\ldots,x_n]]/\mathfrak{m}^k \cong R[x_1,\ldots,x_n]/(x_1,\ldots,x_n)^k,
$$

the polynomials of degree less than $k$; both sides consist of the truncations of order at most $k - 1$. The algebra is $\mathfrak{m}$-adically complete, meaning that the canonical map

$$
R[[x_1, \ldots, x_n]] \longrightarrow \varprojlim_k R[[x_1,\ldots,x_n]]/\mathfrak{m}^k
$$

is a bijection: a series is the same thing as a coherent sequence of its truncations. This is the structure that the next sections exploit.

### Units

**Proposition.** A formal power series $f \in R[[x_1,\ldots,x_n]]$ is a unit if and only if its constant term $f(0)$ is a unit of $R$.

*Proof.* If $f(0) = u \in R^{\times}$, write $f = u(1 - h)$ with $h \in \mathfrak{m}$. Since $h^k \in \mathfrak{m}^k$ and every series is a limit of its truncations, the geometric series

$$
f^{-1} = u^{-1}\bigl(1 + h + h^2 + h^3 + \cdots\bigr)
$$

converges $\mathfrak{m}$-adically, and multiplying the series by $1 - h$ gives $1$; so $f$ is a unit. Conversely, if $f$ is a unit then $fh = 1$ for some $h$, and evaluating the constant terms gives $f(0)h(0) = 1$, so $f(0)$ is a unit. $\square$

**Example.** $1 + x$ is a unit in $R[[x]]$ with inverse $1 - x + x^2 - x^3 + \cdots$, the coefficients being $(-1)^k$. The series $x$ is not a unit; over a domain it is a non-zerodivisor, so not every non-unit of $R[[x]]$ is a zerodivisor.

### Substitution and Composition

Let $h_1, \ldots, h_n$ be series with $h_i \in \mathfrak{m}$, that is $\operatorname{ord}(h_i) \geq 1$. For any $f \in R[[x_1,\ldots,x_n]]$, the substituted series $f(h_1,\ldots,h_n)$ is defined: the contribution of the monomial $x^a$ of degree $d$ lies in $\mathfrak{m}^d$, so each coefficient of the result is a finite sum of contributions from the finitely many monomials of bounded degree. The substitution depends only on the truncations of $f$, and it is a continuous $R$-algebra homomorphism

$$
R[[x_1,\ldots,x_n]] \longrightarrow R[[x_1,\ldots,x_n]], \qquad f \longmapsto f(h_1,\ldots,h_n),
$$

precisely when the $h_i$ have no constant terms. Without that condition the substitution of a series with infinitely many terms need not make sense, and the requirement $h_i \in \mathfrak{m}$ is the standard hypothesis under which composition is defined.

## The $\mathfrak{m}$-adic Completion

### The Completion Functor

Let $A$ be a commutative $R$-algebra and let $I \subseteq A$ be an ideal. The **$I$-adic completion** of $A$ is

$$
\hat A = \varprojlim_k A/I^k,
$$

the module of coherent sequences $(a_k)_{k\geq0}$ with $a_k \in A/I^k$ and $a_{k+1} \equiv a_k \bmod I^k$. It is a commutative $R$-algebra under componentwise operations, the natural map $A \to \hat A$, $a \mapsto (a + I^k)_k$ is a homomorphism with kernel $\bigcap_k I^k$, and $\hat A$ is complete for the filtration by the kernels of $\hat A \to A/I^k$. The construction is functorial: a homomorphism $A \to B$ carrying $I$ into an ideal $J$ induces $\hat A \to \hat B$, so $I$-adic completion is a functor on the appropriate category of filtered algebras.

**Proposition.** The completion of the polynomial algebra at the augmentation ideal is the formal power series algebra:

$$
R[x_1,\ldots,x_n]^{\wedge}_{\mathfrak{m}} \cong R[[x_1,\ldots,x_n]], \qquad \mathfrak{m} = (x_1,\ldots,x_n),
$$

where $\widehat{\phantom{A}}$ denotes $\mathfrak{m}$-adic completion.

*Proof.* For each $k$ the truncation map $R[[x_1,\ldots,x_n]]\to R[x_1,\ldots,x_n]/\mathfrak{m}^k$ is surjective with kernel $\mathfrak{m}^k$, giving isomorphisms

$$
R[x_1,\ldots,x_n]/\mathfrak{m}^k \cong R[[x_1,\ldots,x_n]]/\mathfrak{m}^k
$$

because every class modulo $\mathfrak{m}^k$ has a polynomial representative, namely its truncation. Passing to the inverse limit and using that the power series algebra is $\mathfrak{m}$-adically complete gives the stated isomorphism. $\square$

The proposition is the precise sense in which the polynomial algebra and the power series algebra are the same thing: they have the same finite truncations, and the second is obtained from the first by completing the filtration.

### Exactness and Finite Generation

Completion is not exact on arbitrary modules, but it is well behaved on finitely generated modules over Noetherian rings. If $R$ is Noetherian, $A$ is a finitely generated $R$-algebra and $M$ a finitely generated $A$-module, then the natural map $M\otimes_A\hat A\to\hat M$ is an isomorphism and the completion functor is exact on finitely generated modules; this follows from the **Artin–Rees lemma**, quoted here as standard. Over a Noetherian base the completion of a finitely generated module is therefore computed by base change. Without the finiteness hypotheses the completion can behave badly. Let $A = \bigoplus_{n\geq0} R$ with componentwise multiplication and let $I = \bigoplus_{n\geq1} R$; writing $e_n$ for the idempotent supported at $n$, one has $e_n^2 = e_n$, so $I^2 = I$ and hence $A/I^k \cong A/I \cong R$ for every $k \geq 1$, giving $\hat A \cong R$. The natural map $A \to \hat A$ is the projection onto the degree-zero component, and its kernel is $I \neq 0$: the completion of this non-Noetherian algebra loses information, and the filtration by the powers of $I$ does not separate its elements. The Noetherian hypotheses are what rule out such behaviour.

## The Formal Inverse Function Theorem

### Statement

Let $R$ be a commutative ring and let $F = (F_1, \ldots, F_n)$ be an $n$-tuple of formal power series in $x_1, \ldots, x_n$ with no constant terms. Write the **Jacobian matrix** at the origin

$$
J = \Bigl(\frac{\partial F_i}{\partial x_j}(0)\Bigr)_{i,j} .
$$

**Theorem (formal inverse function theorem).** If $J$ is invertible over $R$, then there is a unique $n$-tuple $G = (G_1,\ldots,G_n)$ of formal power series with no constant terms such that

$$
F \circ G = \mathrm{id} = G \circ F,
$$

that is $F_i(G_1,\ldots,G_n) = x_i$ and $G_i(F_1,\ldots,F_n) = x_i$ for all $i$.

### Proof by $\mathfrak{m}$-adic Contraction

Write $F(x) = Jx + N(x)$, where $N = (N_1,\ldots,N_n)$ has no terms of degree $0$ or $1$, and put $L = J^{-1}$. The equation $F(G) = x$ is equivalent to the fixed-point equation

$$
G = \Phi(G), \qquad \Phi(G) = L\bigl(x - N(G)\bigr).
$$

**Lemma (contraction on the filtration).** $\Phi$ gains one order on the $\mathfrak{m}$-adic filtration: if $G \equiv G' \bmod \mathfrak{m}^k$ then $\Phi(G) \equiv \Phi(G') \bmod \mathfrak{m}^{k+1}$.

*Proof.* Since $N$ has no terms of degree at most $1$, every monomial of $N$ has degree at least $2$ and therefore contains at least one factor from the tuple's variables; hence

$$
N(G) - N(G') \in \mathfrak{m}\cdot(G_1 - G'_1, \ldots, G_n - G'_n) \subseteq \mathfrak{m}^{k+1}
$$

whenever $G_i - G'_i \in \mathfrak{m}^k$ for all $i$, which is the gain of one order. Applying the linear map $-L$ preserves membership in $\mathfrak{m}^{k+1}$. $\square$

*Proof of the theorem.* Choose $G^{(0)} = Lx$, which has zero constant term and satisfies $F(G^{(0)}) \equiv x \bmod \mathfrak{m}^2$ because $F(Lx) = JLx + N(Lx) = x + N(Lx)$ and $N(Lx) \in \mathfrak{m}^2$. Set $G^{(r+1)} = \Phi(G^{(r)})$. By the lemma, $G^{(r+1)} - G^{(r)} \in \mathfrak{m}^{r+1}$, so the sequence converges $\mathfrak{m}$-adically to a limit $G$, and $G$ satisfies $F(G) = x$ by continuity. For uniqueness, suppose $F(G) = F(G') = x$. Then $J(G - G') + (N(G) - N(G')) = 0$, and $N(G) - N(G') \in \mathfrak{m}\cdot(G-G')$, so $(J + M)(G - G') = 0$ with $M$ having entries in $\mathfrak{m}$; since $J$ is invertible and $M$ is topologically nilpotent, $J + M$ is invertible, whence $G = G'$. Finally, $G$ has Jacobian $L$ at the origin, also invertible, so the same argument applied to $G$ produces $H$ with $G\circ H = \mathrm{id}$; then

$$
G \circ F = (G\circ F)\circ (G\circ H) = G \circ (F \circ G)\circ H = G\circ H = \mathrm{id},
$$

so $G$ is a two-sided inverse. $\square$

### Consequence: the Implicit Function Theorem

The implicit form follows by the usual device of adding variables. If $F(x, y)$ is a series with $F(0,0) = 0$ and $\partial F/\partial y(0,0)$ invertible, then the map $(x,y)\mapsto(x, F(x,y))$ has invertible Jacobian at the origin, so it has a formal inverse $(x, y(x))$, giving the unique series $y = y(x)$ with $F(x, y(x)) = 0$. The formal and the analytic inverse function theorems have the same statement and the same Newton iteration; the formal one is the algebraisation of the analytic one, valid over any commutative ring in which the Jacobian is invertible.

**Example.** For $n = 1$ and $F(x) = x + x^2$ the Jacobian is $1$, and the inverse is

$$
G(x) = x - x^2 + 2x^3 - 5x^4 + 14x^5 - \cdots,
$$

the coefficient of $x^m$ being $(-1)^{m-1}C_{m-1}$, where $C_m = \frac{1}{m+1}\binom{2m}{m}$ is the $m$-th Catalan number. This is the formal version of the Lagrange inversion formula. For $n = 2$ and $F(x,y) = (x + y^2,\ y + x^2)$, the Jacobian is the identity and the inverse begins

$$
G(x, y) = \bigl(x - y^2 + 2x^2 y + \cdots,\ y - x^2 + 2x y^2 + \cdots\bigr),
$$

the further terms determined recursively by the contraction. In both examples $G$ satisfies $F\circ G = G\circ F = \mathrm{id}$ in the sense of the formal power series, by the uniqueness part of the theorem applied to the two compositions.

## Hensel's Lemma

The same Newton iteration that inverts a series lifts a root of a polynomial modulo a complete ideal to a root modulo the ideal.

**Theorem (Hensel's lemma).** Let $A$ be a commutative $R$-algebra that is complete for the $I$-adic filtration, let $f(t) \in A[t]$ be a polynomial, and let $a_0 \in A$ satisfy

$$
f(a_0) \in I, \qquad f'(a_0) \in A^{\times} .
$$

Then there is a unique $a \in A$ with $f(a) = 0$ and $a \equiv a_0 \bmod I$.

*Proof.* Set $a_{n+1} = a_n - f(a_n) f'(a_n)^{-1}$, the Newton step. We show by induction that $f(a_n) \in I^{2^n}$ and $a_{n+1} \equiv a_n \bmod I^{2^n}$, so that $(a_n)$ is Cauchy and converges to some $a$ with $f(a) = 0$ by continuity. For the induction, write $a_n = a_{n-1} + h$ with $h \in I^{2^{n-1}}$; Taylor expansion of the polynomial $f$ at $a_{n-1}$ gives

$$
f(a_n) = f(a_{n-1}) + h f'(a_{n-1}) + h^2 r
$$

for some $r \in A$; now $f'(a_{n-1}) \equiv f'(a_0) \bmod I$ because $a_{n-1}\equiv a_0 \bmod I$, so $f'(a_{n-1})$ is a unit, and the choice of $h = -f(a_{n-1})f'(a_{n-1})^{-1}$ makes $f(a_n) = h^2 r \in I^{2^n}$. Uniqueness: if $f(a) = f(a') = 0$ with $a \equiv a' \equiv a_0 \bmod I$, then $0 = f(a) - f(a') = (a - a')(f'(a_0) + m)$ with $m \in I$, and $f'(a_0) + m$ is a unit, so $a = a'$. $\square$

**Example.** In $R[[x]]$ the series $y = \sqrt{1 + x}$ is produced by Hensel's lemma applied to $f(t) = t^2 - (1+x)$ at $a_0 = 1$: the derivative $2t$ is a unit at $t = 1$ when $2$ is invertible, and the root is the binomial series $y = \sum_{k\geq0}\binom{1/2}{k}x^k = 1 + \tfrac12 x - \tfrac18 x^2 + \tfrac{1}{16}x^3 - \cdots$. Over the $p$-adic integers $\mathbb{Z}_p$ with $p$ odd, applied to $f(t) = t^2 - u$ at a unit $a_0$ with $a_0^2 \equiv u \pmod{p}$, the derivative $2a_0$ is a unit and the lemma lifts the square root modulo $p$ to a square root in $\mathbb{Z}_p$; this is the classical instance of Hensel's lemma.

## Completion, the Symmetric Algebra and Taylor Expansion

### The Associated Graded Algebra

The completion assembles the graded pieces of the symmetric algebra into a power series algebra whose associated graded algebra is the symmetric algebra again.

**Theorem.** Let $M$ be a free $R$-module of rank $n$ and let $S = \operatorname{Sym}(M) = \bigoplus_{k\geq0}\operatorname{Sym}^k(M)$, graded, with augmentation ideal $\mathfrak{m} = \bigoplus_{k\geq1}\operatorname{Sym}^k(M)$. Then

$$
\operatorname{gr}_{\mathfrak{m}} S = \bigoplus_{k\geq0}\mathfrak{m}^k/\mathfrak{m}^{k+1} \cong \operatorname{Sym}(M),
$$

and the $\mathfrak{m}$-adic completion of $S$ is

$$
\hat S \cong \prod_{k\geq0}\operatorname{Sym}^k(M).
$$

*Proof.* The associated graded of a polynomial algebra in $n$ variables is the polynomial algebra again, since $\mathfrak{m}^k/\mathfrak{m}^{k+1}$ is the module of homogeneous polynomials of degree $k$, isomorphic to $\operatorname{Sym}^k(M)$; this is the general fact that $\operatorname{gr}$ of the symmetric algebra of a free module is the symmetric algebra. The completion consists of the coherent sequences of truncations, and a coherent sequence is exactly a formal sum $\sum_{k\geq0} s_k$ with $s_k \in \operatorname{Sym}^k(M)$, that is, an element of the product $\prod_k\operatorname{Sym}^k(M)$. $\square$

Thus the passage from the symmetric algebra to its completion replaces the direct sum by the product, allowing arbitrary infinite homogeneous components. The algebra $R[[x_1,\ldots,x_n]]$ is the completion $\hat S$ in the case $M = R^n$, and its associated graded algebra is $R[x_1,\ldots,x_n]$ again: the completion does not change the graded pieces, only the way they are assembled.

### Taylor Expansion

Assume $R$ contains the rational numbers. Every formal power series has the **Taylor expansion**

$$
f = \sum_{a \in \mathbb{N}^n} \frac{1}{a!}\,\partial^a f(0)\, x^a, \qquad a! = a_1!\cdots a_n!,
$$

where $\partial^a f(0)$ denotes the iterated formal derivative evaluated at the origin; the formula is the definition of the derivatives read backwards: the iterated derivative $\partial^a f(0)$ is $a_1!\cdots a_n!$ times the coefficient of $x^a$. The linear part of $f$ is the element of $\operatorname{Hom}_R(\mathfrak{m}/\mathfrak{m}^2, R)$ with components $\partial_1 f(0), \ldots, \partial_n f(0)$; the cotangent space is $\mathfrak{m}/\mathfrak{m}^2 \cong \operatorname{Sym}^1(M) \cong R^n$, and its dual $(\mathfrak{m}/\mathfrak{m}^2)^*$, the tangent space, is the module of $R$-derivations of $R[[x_1,\ldots,x_n]]$ at the origin. The formal inverse function theorem is the statement that an invertible linear part lifts to an invertible series.

**Remark.** In characteristic zero the Taylor formula identifies $R[[x_1,\ldots,x_n]]$ with the completed divided-power algebra, and the natural divided powers $\gamma_k(x) = x^k/k!$ are the coefficients of the exponential; the divided-power algebra of *Divided Powers* is the correct substitute in small characteristic, where the factorials are not invertible. The completion, the symmetric algebra and the divided-power algebra therefore agree in characteristic zero and diverge in small characteristic, exactly as in the uncompleted case.

## Summary

The formal power series algebra $R[[x_1,\ldots,x_n]]$ is the completed polynomial algebra: it is the $I$-adic completion

$$
R[x_1,\ldots,x_n]^{\wedge}_{\mathfrak{m}} = \varprojlim_k R[x_1,\ldots,x_n]/\mathfrak{m}^k \cong R[[x_1,\ldots,x_n]], \qquad \mathfrak{m} = (x_1,\ldots,x_n),
$$

where completion takes the inverse limit of the quotient algebras $A/I^k$. The filtration is the order filtration, $\mathfrak{m}^k$ is the set of series of order at least $k$, and the algebra is $\mathfrak{m}$-adically complete. A series is a unit exactly when its constant term is a unit, by the geometric series; substitution is defined for series with zero constant term. The formal inverse function theorem states that an $n$-tuple $F$ with $F(0) = 0$ and invertible Jacobian $J = (\partial F_i/\partial x_j)(0)$ has a unique two-sided compositional inverse, and it is proved by the contraction $G \mapsto L(x - N(G))$ on the $\mathfrak{m}$-adic filtration, a formal Newton iteration. Completion converts the direct-sum symmetric algebra $\operatorname{Sym}(M)$ into the product $\prod_k \operatorname{Sym}^k(M)$, leaves the associated graded algebra unchanged, and in characteristic zero agrees with the Taylor expansion and with the completed divided-power algebra. In small characteristic the divided powers provide the correct substitute.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $R[[x_1,\ldots,x_n]]$ | Formal power series algebra |
| $\mathfrak{m} = (x_1,\ldots,x_n)$ | Augmentation ideal, series of positive order |
| $\operatorname{ord}(f)$ | Order of a series; least total degree of a term |
| $\mathfrak{m}^k$ | Series of order at least $k$ |
| $\hat A = \varprojlim A/I^k$ | $I$-adic completion of $A$ |
| $\operatorname{gr}_{\mathfrak{m}} A$ | Associated graded algebra |
| $J = (\partial F_i/\partial x_j(0))$ | Jacobian matrix at the origin |
| $\Phi(G) = L(x - N(G))$ | Contraction operator, $L = J^{-1}$ |
| $\mathfrak{m}/\mathfrak{m}^2$ | Cotangent space at the origin |
| $C_m = \frac{1}{m+1}\binom{2m}{m}$ | Catalan number, coefficients of the inverse of $x + x^2$ |
| $a_{n+1} = a_n - f(a_n)f'(a_n)^{-1}$ | Newton step in Hensel's lemma |

## Further Reading

- Nicolas Bourbaki, *Algebra II: Chapters 4–7* (Springer, 1990), for formal power series, substitution and the formal inverse function theorem.
- Nicolas Bourbaki, *Commutative Algebra: Chapters 1–7* (Springer, 1989), for $I$-adic completion, the Artin–Rees lemma and the associated graded algebra.
- Michael F. Atiyah and Ian G. Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, 1969), for completions, filtrations and the completion of local rings.
- Hideyuki Matsumura, *Commutative Ring Theory* (Cambridge University Press, 1986), for completions of finitely generated modules and the Krull intersection theorem.
- Richard P. Stanley, *Enumerative Combinatorics*, Volume 2 (Cambridge University Press, 1999), for the Lagrange inversion formula and the Catalan numbers.
