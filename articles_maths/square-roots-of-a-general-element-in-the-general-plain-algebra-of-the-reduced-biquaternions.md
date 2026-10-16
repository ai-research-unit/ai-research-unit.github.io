# __Square Roots of a General Element in the General Plain Algebra of the Reduced Biquaternions__

## Introduction

This article solves the square-root problem in the multiplication of the general plain algebra: given $T\in\mathbb{B}_{\mathrm{r}}$, find every $X\in\mathbb{B}_{\mathrm{r}}$ with

$$
X^{2}=T .
$$

The method needs no norm and no form. It uses the one structural fact the algebra carries, the **idempotent coordinates**: the multiplication is componentwise in the basis $\Pi_{1},\Pi_{2}$ of the two nontrivial idempotents, so the single equation $X^{2}=T$ splits into the **two independent complex equations** $p^{2}=q_1$ and $q^{2}=q_2$, where $X=(p,q)$ and $T=(q_1,q_2)$ are the pairs of idempotent coordinates. This is the same split that solves the central cases $X^{2}=1$ and $X^{2}=0$ in *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions* and *Square Roots of Zero and the Nilpotents of the General Plain Algebra of the Reduced Biquaternions*, carried to an arbitrary radicand.

**The results.** Every element of the algebra has a square root, because every complex number does; there is **no rootless element**, in sharp contrast with the biquaternion algebra of *Square Roots of a General Element in the Biquaternion Algebra*, where a whole row of radicands has an empty root set. The count is read from the two idempotent coordinates alone:

- **four roots** when $T$ lies on neither of the two idempotent lines, that is when $q_1\neq0$ and $q_2\neq0$;
- **two roots** when $T$ lies on exactly one of the two lines and is not $0$, that is when exactly one of $q_1,q_2$ vanishes;
- **one root** when $T=0$.

The four roots are $\pm p\Pi_{1}\pm q\Pi_{2}$ with the signs independent, where $p$ and $q$ are fixed square roots of $q_1$ and $q_2$; they are the two opposite pairs $\pm X$ and $\pm X'$, with $X'$ the **conjugate root** $p\Pi_{1}-q\Pi_{2}$, and neither pair can be predicted from the other. The three central values of the two companion articles are recovered as the radicands $T=-1$, $0$ and $+1$.

**Boundaries.** The algebra and its idempotents are *Reduced Biquaternion Space* and *Introduction to the General Plain Algebra of the Reduced Biquaternions*, above this article in this category; the idempotent coordinates are those of *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$*. The roots of one and the roots of zero are the companion articles *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions* and *Square Roots of Zero and the Nilpotents of the General Plain Algebra of the Reduced Biquaternions*, above this article. The zero-divisor set, which is the union of the two idempotent lines, is *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*; the norm $\langle T\rangle_{\natural}=A^{2}-B^{2}$ whose vanishing draws that set is *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions*. The square-root problems of the other three general products are the thematic articles of their blocks, and the four products themselves are *The Four Products, Their Forms and Their Algebraic Norms*.

Throughout, an element is $T=A+Bj$ with $A,B\in\mathbb{C}$, the idempotent coordinates are
$$
q_1=A+B,\qquad q_2=A-B,\qquad T=q_1\Pi_{1}+q_2\Pi_{2},\qquad \Pi_{1,2}=\tfrac12(1\pm j),
$$
and a root is written $X=p\Pi_{1}+q\Pi_{2}$ with the same letters. The square is the one of the general plain product $TW$, the multiplication of the algebra.

## The Reduction to Two Complex Equations

**In the idempotent coordinates the squaring is componentwise, so the single equation $X^{2}=T$ is the pair of complex equations $p^{2}=q_1$ and $q^{2}=q_2$.**

**Proposition (squaring in idempotent coordinates).** For $X=p\Pi_{1}+q\Pi_{2}$ one has
$$
X^{2}=p^{2}\Pi_{1}+q^{2}\Pi_{2}.
$$

*Proof.* The two idempotents are orthogonal and complementary, $\Pi_{1}^{2}=\Pi_{1}$, $\Pi_{2}^{2}=\Pi_{2}$ and $\Pi_{1}\Pi_{2}=0$ (*Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions*). Expanding the square with the multiplication commutative gives
$$
(p\Pi_{1}+q\Pi_{2})^{2}=p^{2}\Pi_{1}^{2}+2pq\,\Pi_{1}\Pi_{2}+q^{2}\Pi_{2}^{2}=p^{2}\Pi_{1}+q^{2}\Pi_{2}.
$$

**Corollary (the reduction).** $X^{2}=T$ holds if and only if
$$
p^{2}=q_1\qquad\text{and}\qquad q^{2}=q_2 .
$$

*Proof.* The element $T$ has the unique idempotent coordinates $(q_1,q_2)$, and by the proposition $X^{2}$ has the coordinates $(p^{2},q^{2})$; two elements are equal exactly when their coordinates are equal. So the single algebra equation is the pair of equations in the field $\mathbb{C}$, and the two are **independent**: neither $p$ nor $q$ is constrained by the other.

**Remark (why the reduction is complete).** The reduction is not an ansatz: every element of the algebra has a unique expression $p\Pi_{1}+q\Pi_{2}$, so every candidate root is of the displayed form, and the proposition computes its square. The problem in the four-dimensional real algebra is therefore exactly the problem in the complex field, taken twice, and the count of the roots is the product of the two complex counts. This is the structural reason the reduced biquaternion square-root problem is shorter than the biquaternion one: the biquaternion algebra is not a direct product, its squaring couples the scalar and the vector part, and its root set can be empty.

## The Roots

**Every element has a square root; the number is four, two or one according to how many of the two idempotent coordinates are zero.**

Because $\mathbb{C}$ is algebraically closed, a complex number $z$ has a square root, and the number of square roots is two when $z\neq0$ and one when $z=0$. Applying this to each coordinate of the reduction gives the following theorem.

**Theorem (the roots).** Let $T=q_1\Pi_{1}+q_2\Pi_{2}$.

1. If $q_1\neq0$ and $q_2\neq0$, choose square roots $p$ of $q_1$ and $q$ of $q_2$; then the four square roots of $T$ are
$$
X=\sigma\,p\,\Pi_{1}+\tau\,q\,\Pi_{2},\qquad \sigma,\tau\in\{+1,-1\},
$$
and there are no others.
2. If exactly one of $q_1,q_2$ is $0$, say $q_2=0$ and $q_1\neq0$, then $T=q_1\Pi_{1}$, the second equation forces $q=0$, and the two square roots are
$$
X=\pm p\,\Pi_{1},\qquad p^{2}=q_1 .
$$
3. If $q_1=q_2=0$, then $T=0$ and the only square root is $X=0$.

*Proof.* By the reduction $X=\sigma p\Pi_{1}+\tau q\Pi_{2}$ is a root exactly when $p^{2}=q_1$ and $q^{2}=q_2$, and $p$ and $q$ are chosen independently. In the field $\mathbb{C}$ the equation $z^{2}=w$ has two solutions for $w\neq0$ (the two opposite square roots) and one for $w=0$. Multiplying the counts and reading $\sigma p$ as the two choices of $p$ gives the three cases. In case 2 the element $X=\sigma p\Pi_{1}$ has $X^{2}=p^{2}\Pi_{1}=q_1\Pi_{1}=T$, and a root with $q\neq0$ would have $X^{2}$ with a nonzero $\Pi_{2}$ coordinate; so no such root exists. In case 3, $X^{2}=(p^{2},q^{2})=(0,0)$ forces $p=q=0$.

**Corollary (roots come in opposite pairs).** If $X$ is a root of $T$ then so is $-X$, since $(-X)^{2}=X^{2}$. The pair $\pm X$ is the same element only when $X=0$, which happens only in case 3. In case 1 the four roots form **two** opposite pairs, $\pm X$ and $\pm X'$, where
$$
X=p\Pi_{1}+q\Pi_{2},\qquad X'=p\Pi_{1}-q\Pi_{2},
$$
and $X'$ is the **conjugate root**, obtained from $X$ by negating its second idempotent coordinate; the two pairs are distinct because $q\neq0$.

**Corollary (the classification by the idempotent lines).** The condition $q_1=0$ is exactly $T=q_2\Pi_{2}$, that is $T$ on the idempotent line $\mathbb{C}\Pi_{2}$; the condition $q_2=0$ is exactly $T=q_1\Pi_{1}$, that is $T$ on the line $\mathbb{C}\Pi_{1}$. So the count of the roots of $T$ is read from the position of $T$ with respect to the two lines:

| position of $T$ | count of roots |
|---|---|
| on neither of $\mathbb{C}\Pi_{1}$, $\mathbb{C}\Pi_{2}$ | four |
| on exactly one of the two lines, $T\neq0$ | two |
| $T=0$ | one |

There is no empty row: **the square-root problem is solvable for every radicand.**

## The Roots in the Real Coordinates

**In the real basis $1,i,j,ij$ the root formulas are polynomial in the two complex square roots, and the count is the one above.**

Writing the complex square roots in the real coordinates displays the four-dimensional nature of the answer. If $p=p_{r}+ip_{i}$ and $q=q_{r}+iq_{i}$, then the root $X=p\Pi_{1}+q\Pi_{2}=\tfrac12(p+q)+\tfrac12(p-q)j$ has the four real coordinates
$$
X=\tfrac12(p_{r}+q_{r})+\tfrac12(p_{i}+q_{i})i+\tfrac12(p_{r}-q_{r})j+\tfrac12(p_{i}-q_{i})ij .
$$
The element $T=A+Bj$ has $q_1=A+B$ and $q_2=A-B$, so the two complex equations are
$$
p^{2}=A+B,\qquad q^{2}=A-B .
$$
The **first** is solved by $p$ a square root of $A+B$ and the **second** by $q$ a square root of $A-B$; the four roots of the generic case are the four ways of pairing the two signs. The two special rows are read as the two equations $A+B=0$ and $A-B=0$, which are the two idempotent lines $\mathbb{C}\Pi_{2}$ and $\mathbb{C}\Pi_{1}$ of the algebra.

**Remark (the two square roots of the norm).** The product $q_1q_2=(A+B)(A-B)=A^{2}-B^{2}=\langle T\rangle_{\natural}$ is the norm of *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions*, and the two equations display its two factors: the norm of the radicand is the product of the norms of the idempotent coordinates, $\langle T\rangle_{\natural}=p^{2}q^{2}=(pq)^{2}$, and the two lines are exactly where one factor dies.

## The Central Values

**The three central values $T=-1,0,+1$ recover the three sets of the companion articles on the roots of one and of zero.**

**$T=1$ ($q_1=q_2=1$).** Both coordinates are nonzero, so the row is the four-root one: $p,q\in\{+1,-1\}$ and the roots are
$$
X=\Pi_{1}+\Pi_{2}=1,\qquad X=\Pi_{1}-\Pi_{2}=j,\qquad X=-\Pi_{1}+\Pi_{2}=-j,\qquad X=-\Pi_{1}-\Pi_{2}=-1,
$$
namely the four elements $1,-1,j,-j$ of *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions*. The two opposite pairs are $\pm 1$ and $\pm j$.

**$T=0$ ($q_1=q_2=0$).** The third case: the only root is $X=0$, which is the statement of *Square Roots of Zero and the Nilpotents of the General Plain Algebra of the Reduced Biquaternions* that the multiplication has no nonzero nilpotent.

**$T=-1$ ($q_1=q_2=-1$).** Both coordinates are nonzero, so there are four roots, with $p,q\in\{+i,-i\}$:
$$
X=\pm i\,\Pi_{1}\pm i\,\Pi_{2},
$$
that is the four elements $\pm i$ and $\pm ij$, the roots of $-1$ of *Conventions in Mathematics*, §*The Roots*; they are the roots of one multiplied by $i$. The example shows that the four-root count is shared by $1$ and $-1$ and that the two sets are the translate of one another by $i$.

The agreement of the three special cases with the direct computations of the companion articles is the check that the general method and those computations are the same computation.

## Worked Examples

The examples are computed from the theorem and verified by squaring.

**A generic element.** For $T=2+3j$ the idempotent coordinates are $q_1=5$ and $q_2=-1$, both nonzero, so there are four roots. Taking $p=\sqrt5$ and $q=i$,
$$
X=\sqrt5\,\Pi_{1}+i\,\Pi_{2}=\frac{\sqrt5+i}{2}+\frac{\sqrt5-i}{2}j,
$$
and the four roots are $\pm X$ and $\pm X'$ with $X'=\sqrt5\,\Pi_{1}-i\,\Pi_{2}$. Squaring gives $X^{2}=5\Pi_{1}+(-1)\Pi_{2}=2+3j=T$, since $q_1\Pi_{1}+q_2\Pi_{2}=\tfrac12(q_1+q_2)+\tfrac12(q_1-q_2)j=2+3j$.

**An element of one line.** For $T=\Pi_{1}$ the coordinates are $q_1=1$, $q_2=0$; the row is the two-root one, and the roots are
$$
X=\pm\Pi_{1},
$$
which square to $\Pi_{1}^{2}=\Pi_{1}$ and $(-\Pi_{1})^{2}=\Pi_{1}$. The element $\Pi_{1}$ is a zero divisor (its product with $\Pi_{2}$ is $0$), and it has two roots although its norm $\langle \Pi_{1}\rangle_{\natural}=0$ vanishes.

**The origin.** For $T=0$ the only root is $X=0$; this is case 3 and the statement that the multiplication is reduced.

**A root of $-1$ and a root of $j$ beside it.** The element $T=-1$ has the four roots $\pm i,\pm ij$. The element $T=j$ has $q_1=1$, $q_2=-1$, both nonzero, so four roots; with $p=1$ and $q=i$,
$$
X=\Pi_{1}+i\,\Pi_{2}=\frac{1+i}{2}+\frac{1-i}{2}j,
$$
and squaring gives $\Pi_{1}+(-1)\Pi_{2}=j$. The four roots of $j$ are $\pm X$ and $\pm X'$, the two opposite pairs the theorem produces.

## Summary

The square-root problem $X^{2}=T$ in the multiplication is solved by the idempotent coordinates: with $T=q_1\Pi_{1}+q_2\Pi_{2}$ and $X=p\Pi_{1}+q\Pi_{2}$ the squaring is componentwise, $X^{2}=p^{2}\Pi_{1}+q^{2}\Pi_{2}$, and the equation is the pair of complex equations $p^{2}=q_1$, $q^{2}=q_2$. Because $\mathbb{C}$ is algebraically closed **every element has a square root**, and the count is read from the position of the radicand: **four** roots when $T$ lies on neither idempotent line, **two** when it lies on exactly one and is not $0$, and **one** when $T=0$. In the generic case the roots are $\pm p\Pi_{1}\pm q\Pi_{2}$ with the signs independent, forming the two opposite pairs $\pm X$ and $\pm X'$ with $X'=p\Pi_{1}-q\Pi_{2}$ the conjugate root. The three central values reproduce the four roots of one of *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions*, the single root of zero of *Square Roots of Zero and the Nilpotents of the General Plain Algebra of the Reduced Biquaternions*, and the four roots of $-1$; the norm $\langle T\rangle_{\natural}=A^{2}-B^{2}$ is the product $(A+B)(A-B)=(pq)^{2}$ of the two idempotent coordinates, and its vanishing set is the union of the two idempotent lines. No radicand is rootless.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\mathrm{r}}$ | Reduced biquaternion algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ |
| $T=A+Bj$ | The radicand, $A,B\in\mathbb{C}$ |
| $X=p\Pi_{1}+q\Pi_{2}$ | A square root, in the idempotent coordinates |
| $q_1=A+B,\ q_2=A-B$ | The idempotent coordinates of $T$, with $T=q_1\Pi_{1}+q_2\Pi_{2}$ |
| $p,q$ | Square roots of $q_1$ and $q_2$ |
| $X'=p\Pi_{1}-q\Pi_{2}$ | The conjugate root, the partner of $X$ in the second opposite pair |
| $\Pi_{1,2}=\tfrac12(1\pm j)$ | The two nontrivial idempotents |
| $\langle T\rangle_{\natural}=A^{2}-B^{2}=(A+B)(A-B)$ | The norm of the multiplication |

## Further Reading

- *Introduction to the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the multiplication and the idempotent coordinates.
- *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the roots of one.
- *Square Roots of Zero and the Nilpotents of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the roots of zero.
- *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the norm and its vanishing set.
- *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the two idempotent lines.
- *Square Roots of a General Element in the Biquaternion Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-biquaternion-algebra.md`), for the non-split companion, whose root set can be empty.
