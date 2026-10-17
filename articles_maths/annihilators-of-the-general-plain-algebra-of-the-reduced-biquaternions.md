# __Annihilators of the Algebra of the Reduced Biquaternions__

## Introduction

This article reads the **annihilators** of the multiplication. For an element $Q_{\pm,1}$ the annihilator is
$$
\operatorname{Ann}(Q_{\pm,1})=\{Q_{\pm,2}:Q_{\pm,1}Q_{\pm,2}=0\},
$$
the set of elements the multiplication by $Q_{\pm,1}$ kills. The result is a **dichotomy**: the annihilator of a **unit** is $\{0\}$, and the annihilator of a **zero divisor** is a whole idempotent line,
$$
\operatorname{Ann}(2Q_{++}\Pi_+)=\mathbb{C}\Pi_-,\qquad \operatorname{Ann}(2Q_{--}\Pi_-)=\mathbb{C}\Pi_+\qquad(Q_{++},Q_{--}\neq0),
$$
the **other** line, of real dimension two. The annihilator of $0$ is the whole algebra. Because the algebra is commutative, the left and the right annihilators coincide, and the annihilator of an element is a two-sided ideal; the two maximal ideals $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$ are the annihilators of each other.

The article also reads the **two-sided annihilator of the structure**, the set of elements that annihilate the algebra, and records that it is $\{0\}$ because the algebra is unital. The two results are different: the annihilators of the elements are the two lines, and the annihilator of the algebra is trivial.

**The results.** The left and the right annihilators of an element coincide, since the multiplication is commutative, and they are an ideal. The annihilator of a unit is $\{0\}$; the annihilator of a nonzero element of one idempotent line is the other idempotent line, a complex line of real dimension two; the annihilator of $0$ is the whole algebra; and the annihilator of the whole algebra is $\{0\}$. The map $Q_\pm\mapsto\operatorname{Ann}(Q_\pm)$ takes the units and $0$ to the two trivial ideals and the two lines to each other, so the set of annihilators of the elements is the set of the four ideals of the algebra.

**Boundaries.** The zero divisors, the two lines and the maximal ideals are *Zero Divisors of the Algebra of the Reduced Biquaternions*, above this article in this category. The criterion of invertibility is *Norm and Invertibility in the Algebra of the Reduced Biquaternions*, above this article. The idempotents and the projections are *Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions*, below this article, and the Peirce decomposition into the ideals the idempotents carry is *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*, below this article in this category. The annihilators as ideals in the biquaternion layer, with the one-sided annihilators of a non-commutative algebra, are *Annihilators of the Biquaternion Algebra*.

## The Annihilator of an Element

### Left and Right, They Coincide

**The left and the right annihilators of an element are equal, because the multiplication is commutative.**

**Definition.** For $Q_{\pm,1}\in\mathbb{B}_{\mathrm{r}}$,
$$
\operatorname{Ann}(Q_{\pm,1})=\{Q_{\pm,2}:Q_{\pm,1}Q_{\pm,2}=0\}
$$
is the **annihilator** of $Q_{\pm,1}$. Since the multiplication is commutative (*Introduction to the Algebra of the Reduced Biquaternions*), the left annihilator $\{Q_{\pm,2}:Q_{\pm,2}Q_{\pm,1}=0\}$ and the right annihilator $\{Q_{\pm,2}:Q_{\pm,1}Q_{\pm,2}=0\}$ are the same set, so the word needs no side.

**Proposition.** The annihilator of an element is a two-sided ideal of the algebra.

*Proof.* If $Q_{\pm,1}Q_{\pm,2}=0$ and $Q_{\pm,1}Q_{\pm,3}=0$ then $Q_{\pm,1}(Q_{\pm,2}+Q_{\pm,3})=0$; if $Q_{\pm,1}Q_{\pm,2}=0$ and $Q_{\pm,3}$ is any element then $Q_{\pm,1}(Q_{\pm,3}Q_{\pm,2})=(Q_{\pm,1}Q_{\pm,3})Q_{\pm,2}=(Q_{\pm,3}Q_{\pm,1})Q_{\pm,2}=Q_{\pm,3}(Q_{\pm,1}Q_{\pm,2})=0$, using the associativity and the commutativity. Hence $\operatorname{Ann}(Q_{\pm,1})$ is closed under addition and under multiplication by an arbitrary element, that is an ideal.

### The Annihilator of a Unit

**The annihilator of a unit is $\{0\}$.**

**Theorem.** If $\langle Q_{\pm,1}\rangle_{\natural}\neq0$ then $\operatorname{Ann}(Q_{\pm,1})=\{0\}$.

*Proof.* If $Q_{\pm,1}Q_{\pm,2}=0$ then multiplying by $Q_{\pm,1}^{-1}$ gives $Q_{\pm,2}=Q_{\pm,1}^{-1}(Q_{\pm,1}Q_{\pm,2})=0$, and the inverse exists by *Norm and Invertibility in the Algebra of the Reduced Biquaternions*. So no nonzero element is annihilated by a unit.

### The Annihilator of a Zero Divisor

**The annihilator of a nonzero element of one idempotent line is the other idempotent line, a complex line of real dimension two.**

**Theorem (the annihilator of a line).** For $Q_{++},Q_{--}\in\mathbb{C}^{\times}$,
$$
\operatorname{Ann}(2Q_{++}\Pi_+)=\mathbb{C}\Pi_-,\qquad \operatorname{Ann}(2Q_{--}\Pi_-)=\mathbb{C}\Pi_+.
$$

*Proof.* Write $Q_{\pm,2}=Q_{2+}+jQ_{2-}$ and read it in the idempotent coordinates $Q_{\pm,2}=Q_{2++}\Pi_++Q_{2--}\Pi_-$, with $Q_{2++}=Q_{2+}+Q_{2-}$ and $Q_{2--}=Q_{2+}-Q_{2-}$. Then $(2Q_{++}\Pi_+)Q_{\pm,2}=2Q_{++}Q_{2++}\Pi_+$, because $\Pi_+^{2}=\Pi_+$ and $\Pi_+\Pi_-=0$ (*Zero Divisors of the Algebra of the Reduced Biquaternions*), and this is zero iff $Q_{2++}=0$, since $Q_{++}\neq0$ and a complex number has no zero divisors. The condition $Q_{2++}=0$ is $Q_{\pm,2}=Q_{2+}-Q_{2+}j=Q_{2+}(1-j)=2Q_{2+}\Pi_-$ with $Q_{2+}\in\mathbb{C}$, that is $Q_{\pm,2}\in\mathbb{C}\Pi_-$. The same computation on the other line.

**Corollary (the two lines annihilate each other).** The two maximal ideals are the annihilators of each other,
$$
\operatorname{Ann}(\mathbb{C}\Pi_+)=\mathbb{C}\Pi_-,\qquad \operatorname{Ann}(\mathbb{C}\Pi_-)=\mathbb{C}\Pi_+,
$$
and each is a complex line of real dimension two.

*Proof.* The annihilator of a set is the intersection of the annihilators of its elements; every nonzero element of the line has the same annihilator, the other line, and the element $0$ of the line has the whole algebra, so the intersection is the other line.

### The Annihilators of Zero and of the Subsets

**The annihilator of $0$ is the whole algebra, and the annihilator of the set of all zero divisors is $\{0\}$.**

**Theorem.** $\operatorname{Ann}(0)=\mathbb{B}_{\mathrm{r}}$, and $\operatorname{Ann}(\mathcal{N}\cup\{0\})=\{0\}$, where $\mathcal{N}$ is the null cone.

*Proof.* $0\cdot Q_{\pm,2}=0$ for every $Q_{\pm,2}$, so the annihilator of $0$ is the whole algebra. If $Q_{\pm,2}$ annihilates every zero divisor, then in particular $Q_{\pm,2}\Pi_+=0$ and $Q_{\pm,2}\Pi_-=0$; expanding $Q_{\pm,2}=Q_{2++}\Pi_++Q_{2--}\Pi_-$ gives $Q_{2++}=Q_{2--}=0$, so $Q_{\pm,2}=0$.

## The Two-Sided Annihilator of the Structure

**The two-sided annihilator of the algebra is $\{0\}$, because the algebra is unital.**

**Definition.** The **two-sided annihilator of the structure** is
$$
\operatorname{Ann}(\mathbb{B}_{\mathrm{r}})=\{Q_{\pm,2}:Q_{\pm,1}Q_{\pm,2}=0\ \text{for all }Q_{\pm,1}\in\mathbb{B}_{\mathrm{r}}\}.
$$

**Theorem (the structure's annihilator is trivial).** $\operatorname{Ann}(\mathbb{B}_{\mathrm{r}})=\{0\}$.

*Proof.* Take $Q_{\pm,1}=1$, the unit: $1\cdot Q_{\pm,2}=Q_{\pm,2}$, so $Q_{\pm,2}$ in the annihilator satisfies $Q_{\pm,2}=0$. Conversely $0$ is annihilated by everything. The triviality is exactly the existence of a two-sided unit (*Introduction to the Algebra of the Reduced Biquaternions*), and it is the reason the interesting annihilators of this article are the per-element ones and not the structure's.

**Remark (the two readings of the words).** The phrase *the two-sided annihilator of the structure* has been read here as the annihilator of the ring; its value is $\{0\}$. The phrase *the annihilator of the structure* can also be read as the annihilator of the set of zero divisors, and that value is also $\{0\}$; and it can be read as the set of common annihilators of the two maximal ideals, which is $\mathbb{C}\Pi_+\cap\mathbb{C}\Pi_-=\{0\}$ as well. All three readings agree, and the single nonzero fact of the section is that the annihilators of the elements are the two lines while the annihilators of the structures are trivial.

## The Lattice of Annihilators

**The annihilators of the elements are the four ideals of the algebra, and the correspondence is the one of the table.**

| element $Q_\pm$ | $\operatorname{Ann}(Q_\pm)$ | real dimension of $\operatorname{Ann}(Q_\pm)$ |
|---|---|---|
| unit, $\langle Q_\pm\rangle_{\natural}\neq0$ | $\{0\}$ | $0$ |
| $2Q_{++}\Pi_+$, $Q_{++}\neq0$ | $\mathbb{C}\Pi_-$ | $2$ |
| $2Q_{--}\Pi_-$, $Q_{--}\neq0$ | $\mathbb{C}\Pi_+$ | $2$ |
| $0$ | $\mathbb{B}_{\mathrm{r}}$ | $4$ |

**Theorem (the four ideals).** The set $\{\operatorname{Ann}(Q_\pm):Q_\pm\in\mathbb{B}_{\mathrm{r}}\}$ is $\{0,\mathbb{C}\Pi_+,\mathbb{C}\Pi_-,\mathbb{B}_{\mathrm{r}}\}$, which is the set of all ideals of the algebra, and it is **ordered by inclusion** as the two chains $\{0\}\subset\mathbb{C}\Pi_+\subset\mathbb{B}_{\mathrm{r}}$ and $\{0\}\subset\mathbb{C}\Pi_-\subset\mathbb{B}_{\mathrm{r}}$, which share their two ends.

*Proof.* The table is read from the three theorems above. The ideals of the algebra are the four displayed (*Zero Divisors of the Algebra of the Reduced Biquaternions*, §*The Maximal Ideals*). The two lines are incomparable and both contain $\{0\}$ and are contained in $\mathbb{B}_{\mathrm{r}}$.

**Corollary (the annihilator of the annihilator).** $\operatorname{Ann}(\operatorname{Ann}(Q_\pm))=Q_\pm$ in the sense of ideals: the double annihilator of a unit is $\mathbb{B}_{\mathrm{r}}$, that of $2Q_{++}\Pi_+$ is $\mathbb{C}\Pi_+$, that of $2Q_{--}\Pi_-$ is $\mathbb{C}\Pi_-$, and that of $0$ is $\{0\}$.

*Proof.* $\operatorname{Ann}(\mathbb{B}_{\mathrm{r}})=\{0\}$ and $\operatorname{Ann}(\{0\})=\mathbb{B}_{\mathrm{r}}$ by the definition; and $\operatorname{Ann}(\mathbb{C}\Pi_-)=\mathbb{C}\Pi_+$ and $\operatorname{Ann}(\mathbb{C}\Pi_+)=\mathbb{C}\Pi_-$ are the corollary above. Reading the table twice reproduces the two lines.

## Summary

The annihilator of an element is $\operatorname{Ann}(Q_{\pm,1})=\{Q_{\pm,2}:Q_{\pm,1}Q_{\pm,2}=0\}$; the multiplication is commutative, so the left and the right annihilators coincide and the annihilator of an element is a two-sided ideal. The annihilator of a **unit** is $\{0\}$; the annihilator of a nonzero element of one **idempotent line** is the **other** line,
$$
\operatorname{Ann}(2Q_{++}\Pi_+)=\mathbb{C}\Pi_-,\qquad \operatorname{Ann}(2Q_{--}\Pi_-)=\mathbb{C}\Pi_+\qquad(Q_{++},Q_{--}\neq0),
$$
a complex line of real dimension two; the annihilator of $0$ is the whole algebra; and the annihilator of the set of all zero divisors is $\{0\}$. The two maximal ideals $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$ are the annihilators of each other.

The **two-sided annihilator of the structure** is trivial,
$$
\operatorname{Ann}(\mathbb{B}_{\mathrm{r}})=\{Q_{\pm,2}:Q_{\pm,1}Q_{\pm,2}=0\ \text{for all }Q_{\pm,1}\}=\{0\},
$$
because the algebra is unital; and the three readings of the phrase — the annihilator of the ring, the annihilator of the set of zero divisors and the common annihilator of the maximal ideals — all give $\{0\}$. The set of annihilators of the elements is the set of the four ideals of the algebra, $\{0,\mathbb{C}\Pi_+,\mathbb{C}\Pi_-,\mathbb{B}_{\mathrm{r}}\}$, ordered by inclusion with the two lines incomparable; and the double annihilator returns the line, the algebra or the zero ideal according to the table.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Ann}(Q_{\pm,1})=\{Q_{\pm,2}:Q_{\pm,1}Q_{\pm,2}=0\}$ | the annihilator of an element, the left and the right coinciding |
| $\operatorname{Ann}(2Q_{++}\Pi_+)=\mathbb{C}\Pi_-$ | the annihilator of a nonzero element of the first line |
| $\operatorname{Ann}(2Q_{--}\Pi_-)=\mathbb{C}\Pi_+$ | the annihilator of a nonzero element of the second line |
| $\operatorname{Ann}(0)=\mathbb{B}_{\mathrm{r}}$ | the annihilator of zero |
| $\operatorname{Ann}(\mathbb{B}_{\mathrm{r}})=\{0\}$ | the two-sided annihilator of the structure |
| $\{0,\mathbb{C}\Pi_+,\mathbb{C}\Pi_-,\mathbb{B}_{\mathrm{r}}\}$ | the four ideals, the values of the annihilator |

## Further Reading

- *Zero Divisors of the Algebra of the Reduced Biquaternions* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), above this article in this category, for the two lines and the maximal ideals.
- *Norm and Invertibility in the Algebra of the Reduced Biquaternions* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.md`), above this article, for the criterion of invertibility and the group of units.
- *Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), below this article, for the idempotents and the projections.
- *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), below this article in this category, for the ideals the idempotents carry.
- *Annihilators of the Biquaternion Algebra* (`articles_maths/annihilators-of-the-biquaternion-algebra.md`), the non-commutative counterpart, where the left and the right annihilators need not coincide.
- *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the definition of an ideal and of an annihilator.
