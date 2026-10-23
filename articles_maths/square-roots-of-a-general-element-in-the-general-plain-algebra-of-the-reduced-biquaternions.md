# __Square Roots of a General Element in the Algebra of the Reduced Biquaternions__

## Introduction

This article solves the square-root problem in the multiplication of the general plain algebra: given $\breve Q\in\mathbb{B}_{\mathrm{r}}$, find every $X\in\mathbb{B}_{\mathrm{r}}$ with

$$
X^{2}=\breve Q .
$$

The method needs no norm and no form. It uses the one structural fact the algebra carries, the **idempotent coordinates**: the multiplication is componentwise in the basis $\Pi_+,\Pi_-$ of the two nontrivial idempotents, so the single equation $X^{2}=\breve Q$ splits into the **two independent complex equations** $p^{2}=Q_{+}$ and $q^{2}=Q_{-}$, where $X=(p,q)$ and $\breve Q=(Q_{+},Q_{-})$ are the pairs of idempotent coordinates. This is the same split that solves the central cases $X^{2}=1$ and $X^{2}=0$ in *Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions* and *Square Roots of Zero and the Nilpotents of the Algebra of the Reduced Biquaternions*, carried to an arbitrary radicand.

**The results.** Every element of the algebra has a square root, because every complex number does; there is **no rootless element**, in sharp contrast with the biquaternion algebra of *Square Roots of a General Element in the Biquaternion Algebra*, where a whole row of radicands has an empty root set. The count is read from the two idempotent coordinates alone:

- **four roots** when $\breve Q$ lies on neither of the two idempotent lines, that is when $Q_{+}\neq0$ and $Q_{-}\neq0$;
- **two roots** when $\breve Q$ lies on exactly one of the two lines and is not $0$, that is when exactly one of $Q_{+},Q_{-}$ vanishes;
- **one root** when $\breve Q=0$.

The four roots are $\pm p\Pi_+\pm q\Pi_-$ with the signs independent, where $p$ and $q$ are fixed square roots of $Q_{+}$ and $Q_{-}$; they are the two opposite pairs $\pm X$ and $\pm X'$, with $X'$ the **conjugate root** $p\Pi_+-q\Pi_-$, and neither pair can be predicted from the other. The three central values of the two companion articles are recovered as the radicands $\breve Q=-1$, $0$ and $+1$.

Throughout, an element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{C}$, the idempotent coordinates are
$$
Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown},\qquad Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown},\qquad \breve Q=Q_{+}\Pi_++Q_{-}\Pi_-,\qquad \Pi_{\pm}=\tfrac12(1\pm j),
$$
and a root is written $X=p\Pi_++q\Pi_-$ with the same letters. The square is the one of the general plain product $\breve Q_{1}\breve Q_{2}$, the multiplication of the algebra.

## The Reduction to Two Complex Equations

**In the idempotent coordinates the squaring is componentwise, so the single equation $X^{2}=\breve Q$ is the pair of complex equations $p^{2}=Q_{+}$ and $q^{2}=Q_{-}$.**

**Proposition (squaring in idempotent coordinates).** For $X=p\Pi_++q\Pi_-$ one has
$$
X^{2}=p^{2}\Pi_++q^{2}\Pi_-.
$$

*Proof.* The two idempotents are orthogonal and complementary, $\Pi_+^{2}=\Pi_+$, $\Pi_-^{2}=\Pi_-$ and $\Pi_+\Pi_-=0$ (*Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions*). Expanding the square with the multiplication commutative gives
$$
(p\Pi_++q\Pi_-)^{2}=p^{2}\Pi_+^{2}+2pq\,\Pi_+\Pi_-+q^{2}\Pi_-^{2}=p^{2}\Pi_++q^{2}\Pi_-.
$$

**Corollary (the reduction).** $X^{2}=\breve Q$ holds if and only if
$$
\boxed{\; p^{2}=Q_{+}\qquad\text{and}\qquad q^{2}=Q_{-} \;}.
$$

*Proof.* The element $\breve Q$ has the unique idempotent coordinates $(Q_{+},Q_{-})$, and by the proposition $X^{2}$ has the coordinates $(p^{2},q^{2})$; two elements are equal exactly when their coordinates are equal. So the single algebra equation is the pair of equations in the field $\mathbb{C}$, and the two are **independent**: neither $p$ nor $q$ is constrained by the other.

**Remark (why the reduction is complete).** The reduction is not an ansatz: every element of the algebra has a unique expression $p\Pi_++q\Pi_-$, so every candidate root is of the displayed form, and the proposition computes its square. The problem in the four-dimensional real algebra is therefore exactly the problem in the complex field, taken twice, and the count of the roots is the product of the two complex counts. This is the structural reason the reduced biquaternion square-root problem is shorter than the biquaternion one: the biquaternion algebra $\mathbb{B}$ is not a direct product, its squaring couples its scalar part and its vector part, and its root set can be empty.

## The Roots

**Every element has a square root; the number is four, two or one according to how many of the two idempotent coordinates are zero.**

Because $\mathbb{C}$ is algebraically closed, a complex number $z$ has a square root, and the number of square roots is two when $z\neq0$ and one when $z=0$. Applying this to each coordinate of the reduction gives the following theorem.

**Theorem (the roots).** Let $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$.

1. If $Q_{+}\neq0$ and $Q_{-}\neq0$, choose square roots $p$ of $Q_{+}$ and $q$ of $Q_{-}$; then the four square roots of $\breve Q$ are
$$
\boxed{\; X=\sigma\,p\,\Pi_++\tau\,q\,\Pi_-,\qquad \sigma,\tau\in\{+1,-1\} \;},
$$
and there are no others.
2. If exactly one of $Q_{+},Q_{-}$ is $0$, say $Q_{-}=0$ and $Q_{+}\neq0$, then $\breve Q=Q_{+}\Pi_+$, the second equation forces $q=0$, and the two square roots are
$$
X=\pm p\,\Pi_+,\qquad p^{2}=Q_{+} .
$$
3. If $Q_{+}=Q_{-}=0$, then $\breve Q=0$ and the only square root is $X=0$.

*Proof.* By the reduction $X=\sigma p\Pi_++\tau q\Pi_-$ is a root exactly when $p^{2}=Q_{+}$ and $q^{2}=Q_{-}$, and $p$ and $q$ are chosen independently. In the field $\mathbb{C}$ the equation $z^{2}=w$ has two solutions for $w\neq0$ (the two opposite square roots) and one for $w=0$. Multiplying the counts and reading $\sigma p$ as the two choices of $p$ gives the three cases. In case 2 the element $X=\sigma p\Pi_+$ has $X^{2}=p^{2}\Pi_+=Q_{+}\Pi_+=\breve Q$, and a root with $q\neq0$ would have $X^{2}$ with a nonzero $\Pi_-$ coordinate; so no such root exists. In case 3, $X^{2}=(p^{2},q^{2})=(0,0)$ forces $p=q=0$.

**Corollary (roots come in opposite pairs).** If $X$ is a root of $\breve Q$ then so is $-X$, since $(-X)^{2}=X^{2}$. The pair $\pm X$ is the same element only when $X=0$, which happens only in case 3. In case 1 the four roots form **two** opposite pairs, $\pm X$ and $\pm X'$, where
$$
X=p\Pi_++q\Pi_-,\qquad X'=p\Pi_+-q\Pi_-,
$$
and $X'$ is the **conjugate root**, obtained from $X$ by negating its second idempotent coordinate; the two pairs are distinct because $q\neq0$.

**Corollary (the classification by the idempotent lines).** The condition $Q_{+}=0$ is exactly $\breve Q=Q_{-}\Pi_-$, that is $\breve Q$ on the idempotent line $\mathbb{C}\Pi_-$; the condition $Q_{-}=0$ is exactly $\breve Q=Q_{+}\Pi_+$, that is $\breve Q$ on the line $\mathbb{C}\Pi_+$. So the count of the roots of $\breve Q$ is read from the position of $\breve Q$ with respect to the two lines:

| position of $\breve Q$ | count of roots |
|---|---|
| on neither of $\mathbb{C}\Pi_+$, $\mathbb{C}\Pi_-$ | four |
| on exactly one of the two lines, $\breve Q\neq0$ | two |
| $\breve Q=0$ | one |

There is no empty row: **the square-root problem is solvable for every radicand.**

## The Roots in the Real Coordinates

**In the real basis $1,i,j,ij$ the root formulas are polynomial in the two complex square roots, and the count is the one above.**

Writing the complex square roots in the real coordinates displays the four-dimensional nature of the answer. If $p=p_{r}+ip_{i}$ and $q=q_{r}+iq_{i}$, then the root $X=p\Pi_++q\Pi_-=\tfrac12(p+q)+\tfrac12(p-q)j$ has the four real coordinates
$$
X=\tfrac12(p_{r}+q_{r})+\tfrac12(p_{i}+q_{i})i+\tfrac12(p_{r}-q_{r})j+\tfrac12(p_{i}-q_{i})ij .
$$
The element $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ has $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$, so the two complex equations are
$$
\boxed{\; p^{2}=Q_{\blacktriangle}+Q_{\blacktriangledown},\qquad q^{2}=Q_{\blacktriangle}-Q_{\blacktriangledown} \;}.
$$
The **first** is solved by $p$ a square root of $Q_{\blacktriangle}+Q_{\blacktriangledown}$ and the **second** by $q$ a square root of $Q_{\blacktriangle}-Q_{\blacktriangledown}$; the four roots of the generic case are the four ways of pairing the two signs. The two special rows are read as the two equations $Q_{\blacktriangle}+Q_{\blacktriangledown}=0$ and $Q_{\blacktriangle}-Q_{\blacktriangledown}=0$, which are the two idempotent lines $\mathbb{C}\Pi_-$ and $\mathbb{C}\Pi_+$ of the algebra.

**Remark (the two square roots of the norm).** The product $Q_{+}Q_{-}=(Q_{\blacktriangle}+Q_{\blacktriangledown})(Q_{\blacktriangle}-Q_{\blacktriangledown})=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=\langle \breve Q\rangle_{\mathrm{ts}}$ is the norm of *Norm and Invertibility in the Algebra of the Reduced Biquaternions*, and the two equations display its two factors: the norm of the radicand is the product of the norms of the idempotent coordinates, $\langle \breve Q\rangle_{\mathrm{ts}}=p^{2}q^{2}=(pq)^{2}$, and the two lines are exactly where one factor dies.

## The Central Values

**The three central values $\breve Q=-1,0,+1$ recover the three sets of the companion articles on the roots of one and of zero.**

**$\breve Q=1$ ($Q_{+}=Q_{-}=1$).** Both coordinates are nonzero, so the row is the four-root one: $p,q\in\{+1,-1\}$ and the roots are
$$
X=\Pi_++\Pi_-=1,\qquad X=\Pi_+-\Pi_-=j,\qquad X=-\Pi_++\Pi_-=-j,\qquad X=-\Pi_+-\Pi_-=-1,
$$
namely the four elements $1,-1,j,-j$ of *Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions*. The two opposite pairs are $\pm 1$ and $\pm j$.

**$\breve Q=0$ ($Q_{+}=Q_{-}=0$).** The third case: the only root is $X=0$, which is the statement of *Square Roots of Zero and the Nilpotents of the Algebra of the Reduced Biquaternions* that the multiplication has no nonzero nilpotent.

**$\breve Q=-1$ ($Q_{+}=Q_{-}=-1$).** Both coordinates are nonzero, so there are four roots, with $p,q\in\{+i,-i\}$:
$$
X=\pm i\,\Pi_+\pm i\,\Pi_-,
$$
that is the four elements $\pm i$ and $\pm ij$, the roots of $-1$ of *Conventions in Mathematics*, §*The Roots*; they are the roots of one multiplied by $i$. The example shows that the four-root count is shared by $1$ and $-1$ and that the two sets are the translate of one another by $i$.

The agreement of the three special cases with the direct computations of the companion articles is the check that the general method and those computations are the same computation.

## Worked Examples

The examples are computed from the theorem and verified by squaring.

**A generic element.** For $\breve Q=2+3j$ the idempotent coordinates are $Q_{+}=5$ and $Q_{-}=-1$, both nonzero, so there are four roots. Taking $p=\sqrt5$ and $q=i$,
$$
X=\sqrt5\,\Pi_++i\,\Pi_-=\frac{\sqrt5+i}{2}+\frac{\sqrt5-i}{2}j,
$$
and the four roots are $\pm X$ and $\pm X'$ with $X'=\sqrt5\,\Pi_+-i\,\Pi_-$. Squaring gives $X^{2}=5\Pi_++(-1)\Pi_-=2+3j=\breve Q$, since $Q_{+}\Pi_++Q_{-}\Pi_-=\tfrac12(Q_{+}+Q_{-})+\tfrac12(Q_{+}-Q_{-})j=2+3j$.

**An element of one line.** For $\breve Q=\Pi_+$ the coordinates are $Q_{+}=1$, $Q_{-}=0$; the row is the two-root one, and the roots are
$$
X=\pm\Pi_+,
$$
which square to $\Pi_+^{2}=\Pi_+$ and $(-\Pi_+)^{2}=\Pi_+$. The element $\Pi_+$ is a zero divisor (its product with $\Pi_-$ is $0$), and it has two roots although its norm $\langle \Pi_+\rangle_{\mathrm{ts}}=0$ vanishes.

**The origin.** For $\breve Q=0$ the only root is $X=0$; this is case 3 and the statement that the multiplication is reduced.

**A root of $-1$ and a root of $j$ beside it.** The element $\breve Q=-1$ has the four roots $\pm i,\pm ij$. The element $\breve Q=j$ has $Q_{+}=1$, $Q_{-}=-1$, both nonzero, so four roots; with $p=1$ and $q=i$,
$$
X=\Pi_++i\,\Pi_-=\frac{1+i}{2}+\frac{1-i}{2}j,
$$
and squaring gives $\Pi_++(-1)\Pi_-=j$. The four roots of $j$ are $\pm X$ and $\pm X'$, the two opposite pairs the theorem produces.

## Summary

The square-root problem $X^{2}=\breve Q$ in the multiplication is solved by the idempotent coordinates: with $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$ and $X=p\Pi_++q\Pi_-$ the squaring is componentwise, $X^{2}=p^{2}\Pi_++q^{2}\Pi_-$, and the equation is the pair of complex equations $p^{2}=Q_{+}$, $q^{2}=Q_{-}$. Because $\mathbb{C}$ is algebraically closed **every element has a square root**, and the count is read from the position of the radicand: **four** roots when $\breve Q$ lies on neither idempotent line, **two** when it lies on exactly one and is not $0$, and **one** when $\breve Q=0$. In the generic case the roots are $\pm p\Pi_+\pm q\Pi_-$ with the signs independent, forming the two opposite pairs $\pm X$ and $\pm X'$ with $X'=p\Pi_+-q\Pi_-$ the conjugate root. The three central values reproduce the four roots of one of *Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions*, the single root of zero of *Square Roots of Zero and the Nilpotents of the Algebra of the Reduced Biquaternions*, and the four roots of $-1$; the norm $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ is the product $(Q_{\blacktriangle}+Q_{\blacktriangledown})(Q_{\blacktriangle}-Q_{\blacktriangledown})=(pq)^{2}$ of the two idempotent coordinates, and its vanishing set is the union of the two idempotent lines. No radicand is rootless.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\mathrm{r}}$ | Reduced biquaternion algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ |
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | The radicand, $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{C}$ |
| $X=p\Pi_++q\Pi_-$ | A square root, in the idempotent coordinates |
| $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown},\ Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$ | The idempotent coordinates of $\breve Q$, with $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$ |
| $p,q$ | Square roots of $Q_{+}$ and $Q_{-}$ |
| $X'=p\Pi_+-q\Pi_-$ | The conjugate root, the partner of $X$ in the second opposite pair |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | The two nontrivial idempotents |
| $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=(Q_{\blacktriangle}+Q_{\blacktriangledown})(Q_{\blacktriangle}-Q_{\blacktriangledown})$ | The norm of the multiplication |

## Further Reading

- [Introduction to the Algebra of the Reduced Biquaternions](introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the multiplication and the idempotent coordinates.
- [Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions](square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the roots of one.
- [Square Roots of Zero and the Nilpotents of the Algebra of the Reduced Biquaternions](square-roots-of-zero-and-the-nilpotents-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the roots of zero.
- [Norm and Invertibility in the Algebra of the Reduced Biquaternions](norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the norm and its vanishing set.
- [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the two idempotent lines.
- [Square Roots of a General Element in the Biquaternion Algebra](square-roots-of-a-general-element-in-the-biquaternion-algebra.html), for the non-split companion, whose root set can be empty.
