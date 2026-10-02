# __The Signed Left Multiplication on an Algebra__

## Introduction

The left multiplication of an algebra is $L(a)(x) = ax$, and when the algebra carries an involutive automorphism $\alpha$ the operator can be twisted in the argument, giving the **signed left multiplication**

$$
\Lambda(a)(x) = a\,\alpha(x).
$$

The twist converts the operator into the one-sided half of the signed sandwich: every signed sandwich is a signed left multiplication followed by a right multiplication, exactly as every unsigned sandwich is a left followed by a right. The signed left multiplication is therefore the one-sided atom of the signed operator theory, the way the left multiplication is the atom of the unsigned one.

Throughout, $k$ is a field and $A$ is a unital associative $k$-algebra with an involutive automorphism $\alpha$, $\alpha^2 = \mathrm{id}$; the grade involution of a $\mathbb{Z}/2$-grading is the standard instance and the grading theory is *Superalgebras and Graded Structures*. The unsigned left multiplication $L(a)$, the unsigned right multiplication $R(a)$ and the sandwich $T_{a,b}$ are those of *Left and Right Multiplication* and *The Sandwich Operator on an Algebra*, and the signed sandwich $S_{a,b}$ is that of *The Signed Sandwich on an Algebra*.

## The Signed Left Multiplication

### Definition

**Definition.** For $a \in A$ the **signed left multiplication** by $a$ is the operator

$$
\Lambda(a) : A \to A, \qquad \Lambda(a)(x) = a\,\alpha(x).
$$

The **space of signed left multiplications** is $\Lambda(A) = \{\Lambda(a) : a \in A\}$, and the assignment $a \mapsto \Lambda(a)$ is the **signed left regular map**.

The operator is $k$-linear in $x$, because $\alpha$ and the left multiplication are, and it is $k$-linear in $a$, because the product is. The definition differs from the left multiplication in exactly one place, the argument, which is twisted by $\alpha$ before the multiplication by $a$ is applied.

### The Elementary Identities

**Proposition.** For all $a, b \in A$,

**(a)** $\Lambda(a) = L(a)\,\alpha = \alpha\, L(\alpha(a))$;

**(b)** $\Lambda(1) = \alpha$;

**(c)** $\Lambda(a)(1) = a$;

**(d)** $\Lambda(a)L(b) = \Lambda\bigl(a\,\alpha(b)\bigr)$ and $L(a)\Lambda(b) = \Lambda(ab)$.

*Proof.* (a) Evaluate: $L(a)\alpha(x) = a\alpha(x)$ and $\alpha L(\alpha(a))(x) = \alpha(\alpha(a)x) = a\alpha(x)$, using the multiplicativity of $\alpha$ and $\alpha^2 = \mathrm{id}$. (b) $\Lambda(1)(x) = \alpha(x)$. (c) $\alpha(1) = 1$. (d) $\Lambda(a)L(b)(x) = a\alpha(bx) = a\alpha(b)\alpha(x) = \Lambda(a\alpha(b))(x)$, and $L(a)\Lambda(b)(x) = a\,b\,\alpha(x) = \Lambda(ab)(x)$.

The identities of (a) say that the signed left multiplication is the left multiplication with the involution inserted on the right of the operator, and the involution can be moved to the left at the price of twisting $a$ into $\alpha(a)$. The signed left multiplications are thus the set $L(A)\alpha$ of operators, the image of the unsigned left multiplications under composition with the fixed involution $\alpha$.

### Injectivity

**Proposition.** The signed left regular map $a \mapsto \Lambda(a)$ is injective, and its image $\Lambda(A)$ is a subspace of $\operatorname{End}_k(A)$ of dimension $n = \dim_k A$.

*Proof.* If $\Lambda(a) = 0$ then $a = \Lambda(a)(1) = 0$. The map is $k$-linear and injective, so it carries the $k$-vector space $A$ isomorphically onto its image.

**Corollary.** The signed left multiplications form the space $L(A)\alpha$ obtained from the left multiplications by composition with $\alpha$, and $\dim_k \Lambda(A) = n$. In particular $\Lambda$ is injective exactly as $L$ is, and the two spaces are related by an invertible operator on $\operatorname{End}_k(A)$.

*Proof.* By identity (a) the set $\Lambda(A)$ is the image of $L(A)$ under right composition with $\alpha$, and the map $M \mapsto M\alpha$ on $\operatorname{End}_k(A)$ is a $k$-linear bijection with inverse $M \mapsto M\alpha$.

## The Relation to the Unsigned Left Multiplication

### The Comparison

**Proposition.** For $a \in A$,

$$
\Lambda(a) = L(a) \qquad \Longleftrightarrow \qquad a\,\alpha(x) = a\,x \ \text{ for all } x \qquad \Longleftrightarrow \qquad a\,A^- = 0,
$$

where $A^- = \{x : \alpha(x) = -x\}$ is the negated part of the decomposition $A = A^+ \oplus A^-$ of *The Signed Sandwich on an Algebra*. In particular, if $\alpha = \mathrm{id}$, or if $A^- = 0$, then $\Lambda(a) = L(a)$ for every $a$; and if $a$ is a unit and $A^- \neq 0$, then $\Lambda(a) \neq L(a)$.

*Proof.* Subtract the two operators: $\Lambda(a) - L(a)$ sends $x$ to $a(\alpha(x) - x)$, and $\alpha(x) - x$ lies in $A^-$ and runs over $A^-$ as $x$ does, so the operator vanishes exactly when $a$ annihilates $A^-$. If $\alpha = \mathrm{id}$ then $A^- = 0$ and the condition is vacuous. If $a$ is a unit and $aA^- = 0$, then $A^- = a^{-1}aA^- = 0$, so a unit satisfies the condition only in the degenerate case.

The proposition is the precise sense in which the signed left multiplication is a new operator: it differs from the unsigned one exactly on the odd part of the algebra, and it differs at all only when there is an odd part and the element is a zero divisor along it. For the elements that annihilate $A^-$ — in particular for the elements of $A^-$ themselves when $A^-$ squares to zero — the signed and the unsigned operators coincide.

### The Commutators with the Left Multiplications

**Proposition.** For all $a, b \in A$,

$$
\bigl[L(b),\, \Lambda(a)\bigr] = \Lambda\bigl(ba - a\alpha(b)\bigr),
$$

and $\Lambda(a)$ commutes with $L(b)$ if and only if $ba = a\alpha(b)$, that is, if and only if $L(b)$ fixes the image of $\Lambda(a)$ in the appropriate sense.

*Proof.* By the elementary identities, $L(b)\Lambda(a) = \Lambda(ba)$ and $\Lambda(a)L(b) = \Lambda(a\alpha(b))$, so the difference is $\Lambda(ba - a\alpha(b))$, which vanishes exactly when the argument vanishes, by the injectivity of $\Lambda$.

**Corollary.** If $b \in A^+$ is even, $\alpha(b) = b$, then $[L(b),\Lambda(a)] = \Lambda([b,a])$; if $b \in A^-$ is odd, $\alpha(b) = -b$, then $[L(b),\Lambda(a)] = \Lambda(ba + ab)$, the signed anticommutator of $b$ with $a$.

*Proof.* Substitute $\alpha(b) = \pm b$ in the identity: for $b$ even, $ba - ab = [b,a]$; for $b$ odd, $ba - a(-b) = ba + ab$.

The corollary is the sign rule of the grading in operator form: the even left multiplications commute with the signed left multiplications up to the unsigned commutator, and the odd ones up to the anticommutator, which is the statement that $\Lambda$ is a graded map with respect to the induced grading of the operator space.

### The Invertible Signed Left Multiplications

**Proposition.** Let $A$ be finite-dimensional. The signed left multiplication $\Lambda(a)$ is invertible in $\operatorname{End}_k(A)$ if and only if $a$ is a unit, and then

$$
\Lambda(a)^{-1} = \Lambda\bigl(\alpha(a^{-1})\bigr) = \Lambda\bigl(\alpha(a)^{-1}\bigr).
$$

*Proof.* The form $\Lambda(a) = L(a)\alpha$ is the composite of the invertible operator $\alpha$ and the left multiplication $L(a)$, so it is invertible exactly when $L(a)$ is, which by the injectivity of $L$ and finite dimension is exactly when $a$ is a unit. For the inverse, use the identity $\Lambda(a)\Lambda(c) = L(a\alpha(c))$: with $c = \alpha(a^{-1})$ one gets $a\alpha(c) = a\alpha(\alpha(a^{-1})) = aa^{-1} = 1$, so $\Lambda(a)\Lambda(\alpha(a^{-1})) = L(1) = \mathrm{id}$; the same computation in the other order gives the two-sided inverse. The second form uses $\alpha(a^{-1}) = \alpha(a)^{-1}$.

**Corollary.** The units of $A$ act on $A$ by the operators $\Lambda(a)$, $a \in A^\times$, and the assignment $a \mapsto \Lambda(a)$ is an injective map from the unit group into the general linear group of the twist $\alpha$; the composite $\Lambda(a) = L(a)\alpha$ is the left multiplication twisted by the involution.

## The Fixed Elements

### The Fixed Points of a Single Operator

**Definition.** Let $a \in A$. An element $x \in A$ is **fixed** by $\Lambda(a)$ when $\Lambda(a)(x) = x$, that is

$$
a\,\alpha(x) = x .
$$

The set of fixed points of $\Lambda(a)$ is written $\operatorname{Fix}\Lambda(a)$.

The equation $a\alpha(x) = x$ is linear in $x$ and defines the kernel of $\mathrm{id} - \Lambda(a)$; the fixed set is a subspace containing $0$, and over a finite-dimensional $A$ it is nonzero exactly when $1 - L(a)\alpha$ is not invertible.

**Proposition.** The fixed points of $\Lambda(a)$ satisfy $x = a\alpha(x)$, and applying $\alpha$ gives $\alpha(x) = \alpha(a)x$; conversely $\alpha(x) = \alpha(a)x$ gives back $x = a\alpha(x)$ on applying $\alpha$ again, so

$$
\Lambda(a)(x) = x \qquad \Longleftrightarrow \qquad \alpha(x) = \alpha(a)\,x .
$$

*Proof.* Applying $\alpha$ to $x = a\alpha(x)$ gives $\alpha(x) = \alpha(a)\alpha^2(x) = \alpha(a)x$; applying $\alpha$ to the second equation gives $x = a\alpha(x)$, so the two conditions are equivalent.

**Corollary.** The map $\alpha$ carries $\operatorname{Fix}\Lambda(a)$ bijectively onto the fixed points of the **signed** left multiplication $\Lambda(\alpha(a))$, since $x$ is fixed by $\Lambda(a)$ exactly when $\alpha(x)$ is fixed by $\Lambda(\alpha(a))$; hence
$$
\operatorname{Fix}\Lambda(a) = \alpha\bigl(\operatorname{Fix}\Lambda(\alpha(a))\bigr),
$$
$\Lambda(a)$ has a nonzero fixed point exactly when $1 - \Lambda(\alpha(a))$ fails to be injective, and $\Lambda(a)$ acts as the identity on its fixed subspace. The **unsigned** left multiplication is the wrong comparison: for a unit $a$ with $\alpha(a) \neq a$ the two fixed spaces need not have the same dimension — on $M_2(k)$ with $\alpha$ the conjugation by $\mathrm{diag}(1,-1)$ and $a$ the swap matrix, $\operatorname{Fix}\Lambda(a) = 0$ while $\operatorname{Fix}L(\alpha(a)) = \operatorname{Fix}L(a)$ is two-dimensional.

### The Fixed Elements of the Family

**Proposition.** The operator $\Lambda(1)$ is $\alpha$, so its fixed set is the plus part,

$$
\operatorname{Fix}\Lambda(1) = A^+ ;
$$

and the common fixed set of the whole family is trivial,

$$
\bigcap_{a \in A} \operatorname{Fix}\Lambda(a) = \{0\}.
$$

*Proof.* The first statement is the definition of $A^+$. For the second, let $x$ be fixed by every $\Lambda(a)$; taking $a = 1$ gives $\alpha(x) = x$, and taking an arbitrary $a$ gives $ax = x$; taking $a = 0$ then gives $x = 0$ unless the algebra is the zero algebra, which is excluded by $1 \neq 0$.

### The Elements for Which the Signed Operator Is the Unsigned One

**Proposition.** The elements $a$ for which the signed left multiplication coincides with the unsigned one are

$$
\{a : aA^- = 0\} = \operatorname{Ann}(A^-),
$$

the annihilator of the negated part; this set always contains $0$, it is a subspace of $A$, and it is all of $A$ exactly when $\alpha = \mathrm{id}$.

*Proof.* This is the comparison proposition: $\Lambda(a) = L(a)$ exactly when $a$ annihilates the negated part. The annihilator of a subspace contains $0$ and is a subspace, and it is all of $A$ exactly when $A^- = 0$, which is to say that no element is negated by $\alpha$ and hence $\alpha = \mathrm{id}$.

The two readings of "the elements it fixes" — the fixed points of the operator and the elements for which the operator is the unsigned one — are the two sides of the same twist, and the annihilator reading is the second of them.

## The Signed Sandwich as a Signed Left Followed by a Right

### The Factorisation

**Theorem.** For all $a, b \in A$,

$$
S_{a,b} = \Lambda(a)\,R\bigl(\alpha(b)\bigr) = L(a)\,\alpha\,R\bigl(\alpha(b)\bigr),
$$

so the signed sandwich is the signed left multiplication followed by a right multiplication.

*Proof.* On the one hand $\Lambda(a)R(\alpha(b))(x) = \Lambda(a)(x\alpha(b)) = a\alpha(x\alpha(b)) = a\alpha(x)\alpha^2(b) = a\alpha(x)b = S_{a,b}(x)$. On the other hand $L(a)\alpha R(\alpha(b))(x) = a\alpha(x\alpha(b)) = a\alpha(x)b = S_{a,b}(x)$, the same value, since $\Lambda(a) = L(a)\alpha$; so the three operators agree. Note the second index of the right multiplication in the last form is $\alpha(b)$, not $b$: the twist moves to the right factor.

**Corollary.** Every signed sandwich is a product of a signed left multiplication and a right multiplication, and the signed sandwich space is the product $\Lambda(A)\,R(A)$ of the two spaces. In particular the signed sandwich space is the image of the unsigned sandwich space under composition with $\alpha$, and the two share their dimension, as stated in *The Signed Sandwich on an Algebra*.

### The Commutation with the Right Multiplications

**Proposition.** For all $a, b \in A$,

$$
\Lambda(a)\,R(b) - R(b)\,\Lambda(a) = S_{a,\,\alpha(b)} - S_{a,\,b} .
$$

*Proof.* Evaluate the two products on $x$: $\Lambda(a)R(b)(x) = a\alpha(xb) = a\alpha(x)\alpha(b) = S_{a,\alpha(b)}(x)$, while $R(b)\Lambda(a)(x) = \Lambda(a)(x)\,b = a\alpha(x)b = S_{a,b}(x)$.

The right multiplications and the signed left multiplications fail to commute by the difference of two signed sandwiches, and the difference is measured by $\alpha(b) - b$: it vanishes for all $a$ exactly when $\alpha(b) = b$, that is on the plus part, and on the negated part it is $S_{a,-b} - S_{a,b} = -2S_{a,b}$. This is the operator form of the sign rule that distinguishes the graded theory from the ungraded one, and in characteristic two the difference vanishes identically because $-2 = 0$.

## The Examples

### A Trivial Twist

If $\alpha = \mathrm{id}$, then $\Lambda(a) = L(a)$ for every $a$, the signed left multiplication is the left multiplication, the composition rules reduce to $L(a)L(b) = L(ab)$, and the whole of the article collapses to the left half of *Left and Right Multiplication*. The signed left multiplication is a new operator only when the twist is nontrivial.

### A Group Algebra with a Parity

Let $A = k[G]$ with the parity $\chi$ of *The Signed Sandwich on an Algebra*. Then $\Lambda(g)$ sends the group element $x_h$ to $\chi(h)\,x_{gh}$, the left translation dressed by the parity of the element acted on and not of the acting one: $\Lambda(g)(x) = g\,\alpha(x)$, so the sign is $\chi$ of the argument. Since $g$ is a unit, the comparison $\Lambda(g) = L(g)$ forces the odd part to vanish, so for a nontrivial parity no group element has the signed left multiplication equal to the unsigned one, and the two coincide for every $g$ exactly when $\chi$ is trivial.

### The Exterior Algebra

Let $A = \Lambda(V)$ with the degree grading. For an odd element $a$, the operator $\Lambda(a)$ sends an even element to an odd one with a sign, and an odd element to an even one; it is the left multiplication graded by the parity, and the sign rules of the exterior algebra are those of the corollary. For a vector $v$ the operator $\Lambda(v)$ has $\Lambda(v)^2 = 0$, since $\Lambda(v)^2 = L(v\alpha(v)) = L(-v^2) = 0$, which is the exterior relation $v^2 = 0$ read on the operator; the signed left multiplication by a vector is thus a square-zero operator on the exterior algebra.

## Summary

The signed left multiplication is the operator $\Lambda(a)(x) = a\alpha(x)$ on $A$, $k$-linear in $x$ and in $a$, with $\Lambda(1) = \alpha$, $\Lambda(a)(1) = a$, and the two readings $\Lambda(a) = L(a)\alpha = \alpha L(\alpha(a))$ of the unsigned left multiplication; the map $a \mapsto \Lambda(a)$ is injective and its image has dimension $n$, and $\Lambda(a)$ is invertible exactly when $a$ is a unit, with inverse $\Lambda(\alpha(a^{-1}))$. Its product with the left multiplications is $\Lambda(a)L(b) = \Lambda(a\alpha(b))$ and $L(a)\Lambda(b) = \Lambda(ab)$, whence $[L(b),\Lambda(a)] = \Lambda(ba - a\alpha(b))$, which is $\Lambda([b,a])$ for even $b$ and $\Lambda(ba + ab)$ for odd $b$.

The signed left multiplication differs from the unsigned one exactly by the operator $x \mapsto a(\alpha(x) - x)$, so $\Lambda(a) = L(a)$ exactly when $a$ annihilates the negated part $A^-$; its fixed points are the solutions of $a\alpha(x) = x$, which the involution $\alpha$ carries onto the fixed points of the signed left multiplication $\Lambda(\alpha(a))$; the operator $\Lambda(1)$ is $\alpha$, so its fixed set is the plus part $A^+$, while the elements fixed by the whole family are only $0$. Every signed sandwich is a signed left multiplication followed by a right multiplication, $S_{a,b} = \Lambda(a)R(\alpha(b))$, and the failure of the right multiplications to commute with the signed left ones is the difference of two signed sandwiches, which is the sign rule of the grading in operator form. The corresponding adjoint operations are the subject of *The Signed Adjoint of the Left Multiplication on an Algebra* of the group `- * Operator Theory`; the unsigned left and right multiplications are *Left and Right Multiplication*, and the twist is that of *The Signed Sandwich on an Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the field of scalars |
| $A$ | a unital associative $k$-algebra |
| $\alpha$ | the fixed involutive automorphism, $\alpha^2 = \mathrm{id}$ |
| $A = A^+ \oplus A^-$ | the plus and the negated parts |
| $L(a)$, $R(a)$ | the unsigned left and right multiplications |
| $\Lambda(a)(x) = a\alpha(x)$ | the signed left multiplication |
| $\Lambda(A) = L(A)\alpha$ | the space of signed left multiplications |
| $\Lambda(a) = L(a)\alpha = \alpha L(\alpha(a))$ | the reading through the unsigned operators |
| $S_{a,b}(x) = a\alpha(x)b$ | the signed sandwich |
| $S_{a,b} = \Lambda(a)R(\alpha(b)) = L(a)\alpha R(\alpha(b)) = R(b)\Lambda(a)$ | the factorisation of the signed sandwich |
| $\operatorname{Fix}\Lambda(a)$ | the fixed points of $\Lambda(a)$, with $a\alpha(x) = x$ |
| $\operatorname{Ann}(A^-) = \{a : aA^- = 0\}$ | the elements with $\Lambda(a) = L(a)$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the graded left multiplications and the regular representation.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the twisted one-sided operators and the annihilators.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the one-sided operators of the graded and Jordan theories.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for the sign rules of a grading and the graded operator calculus.
