# __The Group of Units of the Algebra of the Reduced Biquaternions__

## Introduction

Of the eight algebraic structures that the reduced biquaternion complex space carries, exactly one is an associative unital algebra, the general plain product $\breve Q_{1}\breve Q_{2}$ of *Introduction to the Algebra of the Reduced Biquaternions*; the specificity that its associativity and its two-sided unit $1$ deliver is that the invertible elements form a genuine **group** (*The Specificities of the Algebra of the Reduced Biquaternions*). This article studies that group and the exact meaning of its boundary. The group of units is the complement of the null set of the norm, the algebra is the disjoint union of the units, the zero divisors and the single element $0$, and the null set of the norm is at once the complement of the group and its boundary.

The boundary deserves an article of its own because it is drawn by a form the product does not visibly carry. The plain product has its algebraic norm $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$, and $\langle\cdot\rangle_{\mathrm{ts}}$ is **multiplicative**: $\langle \breve Q_{1}\breve Q_{2}\rangle_{\mathrm{ts}}=\langle \breve Q_{1}\rangle_{\mathrm{ts}}\langle \breve Q_{2}\rangle_{\mathrm{ts}}$. That multiplicativity is exactly the reason the non-vanishing set of $\langle\cdot\rangle_{\mathrm{ts}}$ is closed under the product and under inversion, hence a group, and the zero-divisor set is the punctured vanishing set of $\langle\cdot\rangle_{\mathrm{ts}}$, $\mathcal N=\{\breve Q\neq0:\langle \breve Q\rangle_{\mathrm{ts}}=0\}$. The two statements of the article are the pair of these facts: **the units of the plain product are the elements of non-vanishing norm $\langle\cdot\rangle_{\mathrm{ts}}$, and the complement of the unit group is the union of two lines**, the two idempotent lines $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$.

**The results.** The algebra is the disjoint union
$$
\mathbb{B}_{\mathrm{r}}=\mathbb{B}_{\mathrm{r}}^{\times}\ \sqcup\ \mathcal N\ \sqcup\ \{0\},
$$
where $\mathbb{B}_{\mathrm{r}}^{\times}$ is the unit group and $\mathcal N$ is the zero-divisor set, the punctured vanishing set of the norm. The unit group is the group
$$
\mathbb{B}_{\mathrm{r}}^{\times}=\{\breve Q:\langle \breve Q\rangle_{\mathrm{ts}}\neq0\}=\{\breve Q:Q_{\blacktriangle}+Q_{\blacktriangledown}\neq0\ \text{and}\ Q_{\blacktriangle}-Q_{\blacktriangledown}\neq0\}\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times},
$$
**abelian and connected**, of complex dimension two and real dimension four, with fundamental group $\mathbb{Z}\times\mathbb{Z}$. The isomorphism is the idempotent coordinate map $\breve Q\mapsto(Q_{+},Q_{-})=(Q_{\blacktriangle}+Q_{\blacktriangledown},Q_{\blacktriangle}-Q_{\blacktriangledown})$, under which the product is componentwise. The zero-divisor set is the **punctured union of the two idempotent lines** $\mathcal N=(\mathbb{C}\Pi_+\cup\mathbb{C}\Pi_-)\setminus\{0\}$, whose elements are the nonzero zero divisors. Every nonzero element of the algebra is either a unit or a zero divisor; there is no third kind.

## The Partition of the Algebra

**The algebra is the disjoint union of its units, its nonzero zero divisors and the single element $0$.**

**Definition (the zero-divisor set).** An element $\breve Q$ is a **zero divisor** when there is a nonzero $\breve Q_{2}$ with $\breve Q \breve Q_{2}=0$; the **zero-divisor set** is the set of the zero divisors. It is the punctured **null set** of the norm, $\mathcal N=\{\breve Q\neq0:\langle \breve Q\rangle_{\mathrm{ts}}=0\}$.

**Theorem (the partition).** The zero-divisor set of the general plain algebra is the union of the two idempotent lines with the origin removed,
$$
\mathcal N=\bigl(\mathbb{C}\Pi_+\cup\mathbb{C}\Pi_-\bigr)\setminus\{0\},
$$
and the algebra is the disjoint union
$$
\boxed{\; \mathbb{B}_{\mathrm{r}}=\mathbb{B}_{\mathrm{r}}^{\times}\ \sqcup\ \mathcal N\ \sqcup\ \{0\} \;}.
$$

*Proof.* By *Zero Divisors of the Algebra of the Reduced Biquaternions* the zero divisors are the nonzero elements of the null set of the norm, and by *Norm and Invertibility in the Algebra of the Reduced Biquaternions* the null set is $\mathcal N\cup\{0\}=\mathbb{C}\Pi_+\cup\mathbb{C}\Pi_-$, since $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=(Q_{\blacktriangle}+Q_{\blacktriangledown})(Q_{\blacktriangle}-Q_{\blacktriangledown})=0$ if and only if $Q_{\blacktriangle}+Q_{\blacktriangledown}=0$ or $Q_{\blacktriangle}-Q_{\blacktriangledown}=0$, that is $\breve Q\in\mathbb{C}\Pi_-$ or $\breve Q\in\mathbb{C}\Pi_+$. The zero divisors are the nonzero elements of that set, that is $\mathcal N$; the units are the elements of $N\neq0$; and $0$ is neither.

**Corollary (no third kind).** Every nonzero element of $\mathbb{B}_{\mathrm{r}}$ is a unit or a zero divisor. There is no element that is neither, and none that is both.

## The Invertibility Criterion

**An element is a unit exactly when its norm does not vanish, equivalently when neither idempotent coordinate vanishes.**

**Theorem (the criterion).** For $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ the following are equivalent:

1. $\breve Q$ is a unit, that is, there is $\breve Q_{2}$ with $\breve Q \breve Q_{2}=\breve Q_{2}\breve Q=1$;
2. $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}\neq0$;
3. both idempotent coordinates are nonzero, $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}\neq0$ and $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}\neq0$.

When they hold, the inverse is
$$
\boxed{\; \breve Q^{-1}=\frac{Q_{\blacktriangle}-jQ_{\blacktriangledown}}{Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}}=\frac{1}{2}\Bigl(\frac{1}{Q_{\blacktriangle}+Q_{\blacktriangledown}}+\frac{1}{Q_{\blacktriangle}-Q_{\blacktriangledown}}\Bigr)+\frac{1}{2}\Bigl(\frac{1}{Q_{\blacktriangle}+Q_{\blacktriangledown}}-\frac{1}{Q_{\blacktriangle}-Q_{\blacktriangledown}}\Bigr)j \;},
$$
with idempotent coordinates $(Q_{+}^{-1},Q_{-}^{-1})$.

*Proof.* (1)$\Rightarrow$(2): a unit is not a zero divisor, and the zero divisors are the elements with $\langle \breve Q\rangle_{\mathrm{ts}}=0$, so $\langle \breve Q\rangle_{\mathrm{ts}}\neq0$. (2)$\Rightarrow$(3): $Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=(Q_{\blacktriangle}+Q_{\blacktriangledown})(Q_{\blacktriangle}-Q_{\blacktriangledown})$, and $\mathbb{C}$ is a field, so the product is nonzero exactly when both factors are. (3)$\Rightarrow$(1): the displayed $\breve Q^{-1}$ has $\breve Q \breve Q^{-1}=1$ by the multiplication rule $\breve Q_{1}\breve Q_{2}=(Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown})+(Q_{1\blacktriangle}Q_{2\blacktriangledown}+Q_{1\blacktriangledown}Q_{2\blacktriangle})j$, since
$$
Q_{\blacktriangle}\cdot\frac{Q_{\blacktriangle}}{Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}}+Q_{\blacktriangledown}\cdot\frac{-Q_{\blacktriangledown}}{Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}}=\frac{Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}}{Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}}=1,
$$
and $Q_{\blacktriangle}\cdot\frac{-Q_{\blacktriangledown}}{Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}}+Q_{\blacktriangledown}\cdot\frac{Q_{\blacktriangle}}{Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}}=0$; in the idempotent coordinates the inverse is $(Q_{+}^{-1},Q_{-}^{-1})$, which is the componentwise inverse.

**Corollary (multiplicativity is the mechanism).** The norm is multiplicative, $\langle \breve Q_{1}\breve Q_{2}\rangle_{\mathrm{ts}}=\langle \breve Q_{1}\rangle_{\mathrm{ts}}\langle \breve Q_{2}\rangle_{\mathrm{ts}}$, because $\langle\cdot\rangle_{\mathrm{ts}}$ is the product of the two idempotent coordinates, $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{+}Q_{-}$, and the coordinates of the product are the products of the coordinates. Hence the set $N\neq0$ is closed under the product, and the criterion makes it closed under inversion as well; this is why it is a group. The multiplicativity is read on the product of the two copies of $\mathbb{C}^{\times}$.

## The Group and Its Structure

**The unit group is the abelian group $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$, connected, of complex dimension two.**

**Theorem (the structure of the unit group).** The map
$$
\boxed{\; \Phi:\mathbb{B}_{\mathrm{r}}^{\times}\to\mathbb{C}^{\times}\times\mathbb{C}^{\times},\qquad \breve Q\mapsto(Q_{+},Q_{-})=(Q_{\blacktriangle}+Q_{\blacktriangledown},Q_{\blacktriangle}-Q_{\blacktriangledown}) \;},
$$
is an isomorphism of groups.

*Proof.* The idempotent coordinate map $\breve Q\mapsto(Q_{+},Q_{-})$ is an algebra isomorphism of $(\mathbb{B}_{\mathrm{r}},\cdot)$ onto $\mathbb{C}\times\mathbb{C}$ (*The Specificities of the Algebra of the Reduced Biquaternions*); it carries the invertible elements onto the pairs of invertible elements, that is onto $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$. The product is componentwise and the identity $1$ corresponds to $(1,1)$.

**Corollary (the structure).** The unit group is:

- **abelian**, because $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ is;
- **connected**, because each copy of $\mathbb{C}^{\times}\cong\mathbb{R}_{>0}\times S^{1}$ is connected, so the product has no component beyond one;
- of **complex dimension two** and **real dimension four**, hence a real Lie group of dimension four;
- with **fundamental group** $\pi_{1}=\mathbb{Z}\times\mathbb{Z}$, since $\mathbb{C}^{\times}\simeq S^{1}$;
- **not compact**, and **not simply connected**.

The contrast with the biquaternion unit group is the point: there the general plain algebra is $M_{2}(\mathbb{C})$ and its unit group is $GL(2,\mathbb{C})$, non-abelian, with $\pi_{1}=\mathbb{Z}$; here the group is a product of two circles' worth of scalars and is abelian. The commutativity of the multiplication is visible in the group.

## The Boundary

**The complement of the unit group is the union of the two idempotent lines, and that union is the topological boundary of the group.**

**Definition.** The **null set** of the norm is $\mathcal N\cup\{0\}=\{\breve Q:\langle \breve Q\rangle_{\mathrm{ts}}=0\}=\mathbb{C}\Pi_+\cup\mathbb{C}\Pi_-$, the union of the two idempotent lines, each a complex line through the origin, with $\mathcal N$ its punctured part.

**Theorem (the boundary).** The unit group $\mathbb{B}_{\mathrm{r}}^{\times}$ is open and dense in $\mathbb{B}_{\mathrm{r}}$; its complement is $\mathcal N\cup\{0\}$, the union of the two lines; and $\mathcal N\cup\{0\}$ is the topological boundary $\partial\mathbb{B}_{\mathrm{r}}^{\times}=\overline{\mathbb{B}_{\mathrm{r}}^{\times}}\setminus\mathbb{B}_{\mathrm{r}}^{\times}=\mathcal N\cup\{0\}$.

*Proof.* The null set is the vanishing set of the continuous function $\langle\cdot\rangle_{\mathrm{ts}}$, hence closed, so its complement $\mathbb{B}_{\mathrm{r}}^{\times}$ is open; the null set has empty interior because each of the two lines does (a complex line in $\mathbb{C}^{2}$ has empty interior), so $\mathbb{B}_{\mathrm{r}}^{\times}$ is dense; and a dense open set has closure the whole space, so its boundary is its complement, the null set.

**Remark (two lines, not one cone).** The boundary of the reduced biquaternion unit group is **two complex lines**, of real dimension two each, not a single cone of real dimension three as in the biquaternion category. The difference is the split of the algebra: the biquaternion reduced norm is an irreducible quadratic in four complex variables, whose null set is an irreducible cone; the reduced biquaternion norm factors, $\langle\cdot\rangle_{\mathrm{ts}}=(Q_{\blacktriangle}+Q_{\blacktriangledown})(Q_{\blacktriangle}-Q_{\blacktriangledown})$, and its null set is the union of the two hyperplanes $Q_{\blacktriangle}+Q_{\blacktriangledown}=0$ and $Q_{\blacktriangle}-Q_{\blacktriangledown}=0$. The factoring is the idempotent splitting read on the norm, and it is the reason the boundary here is a union of lines.

## The Units inside the Remarkable Subspaces

**The units and the zero divisors are distributed over the remarkable subspaces as follows: every nonzero element of the scalar line, the $j$-line, the Hermitian plane and the anti-Hermitian plane is a unit, the two split planes carry the two real zero-divisor lines $\mathbb{R}\Pi_+$, $\mathbb{R}\Pi_-$ beside their units, and every zero divisor of the algebra lies on one of the two idempotent lines.**

**Theorem (the distribution).** For the remarkable subspaces of *The Six Subspaces*:

| subspace | definition | norm $\langle\cdot\rangle_{\mathrm{ts}}$ | elements |
|---|---|---|---|
| scalar line $\mathbb{C}$ | $\breve Q=Q_{\blacktriangle}$ ($Q_{\blacktriangledown}=0$) | $Q_{\blacktriangle}^{2}$ | unit iff $Q_{\blacktriangle}\neq0$ |
| $j$-line $\mathbb{C}j$ | $\breve Q=jQ_{\blacktriangledown}$, $Q_{\blacktriangle}=0$ | $-Q_{\blacktriangledown}^{2}$ | unit iff $Q_{\blacktriangledown}\neq0$ |
| real subalgebra $\mathbb{R}\{1,j\}$ | $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{R}$ | $q_{\blacktriangle}^{2}-q_{\blacktriangledown}^{2}$ | unit iff $\lvert q_{\blacktriangle}\rvert\neq\lvert q_{\blacktriangledown}\rvert$ |
| $i$-multiple $i\mathbb{R}\{1,j\}$ | $\breve Q=i\breve Q_{2}$, $\breve Q_{2}$ real-split | $-(a^{2}-b^{2})$ | unit iff $\lvert a\rvert\neq\lvert b\rvert$ |
| Hermitian subspace $\mathbb{R}\{1,ij\}$ | $\breve Q=a+bij$, $a,b\in\mathbb{R}$ | $a^{2}+b^{2}$ | unit iff $(a,b)\neq(0,0)$ |
| anti-Hermitian subspace $\mathbb{R}\{i,j\}$ | $\breve Q=ai+bj$ | $-(a^{2}+b^{2})$ | unit iff $(a,b)\neq(0,0)$ |
| idempotent lines $\mathbb{C}\Pi_+$, $\mathbb{C}\Pi_-$ | $\breve Q=Q_{+}\Pi_+$ or $\breve Q=Q_{-}\Pi_-$ | $0$ | all nonzero elements are zero divisors |

*Proof.* The norm is computed on each subspace from its definition $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ and the criterion of §*The Invertibility Criterion*. On $\mathbb{C}$ and $\mathbb{C}j$ the norm is $\pm$ the square of the single complex coordinate, nonzero for a nonzero coordinate. On the real subalgebra and its $i$-multiple the norm is $\pm(a^{2}-b^{2})$ with $a,b$ real, vanishing exactly on the two real lines $a=\pm b$. On the Hermitian and anti-Hermitian subspaces the norm is $\pm(a^{2}+b^{2})$ with $a,b$ real, nonzero for every nonzero element. On the idempotent lines the norm is $0$.

**Corollary (the two families of lines).** The two lines of the tessarine sign — the scalar line and the $j$-line — carry a unit at every nonzero element, and so do the Hermitian and the anti-Hermitian plane; the two split planes $\mathbb{R}\{1,j\}$ and $\mathbb{R}\{i,ij\}$ are the only remarkable subspaces that carry zero divisors, on the two real lines $\mathbb{R}\Pi_+$, $\mathbb{R}\Pi_-$; and the two lines of the idempotent splitting — $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$ — carry a zero divisor at every nonzero element. The distinction between *unit at every nonzero point* and *zero divisor at every nonzero point* is exactly the distinction between the fixed and anti-fixed spaces of the tessarine sign and the eigenlines of the multiplication by $j$.

## The Complement in the Other Seven Structures

**For the other seven structures the complement of the unit set is not a group, and the plain product is the only one whose non-vanishing set is closed under its own operation.**

The seven other structures of *The Four Products, Their Forms and Their Algebraic Norms* are the general tessarine bilinear product, the two sesquilinear products and the four symmetrised and antisymmetrised structures. Their inverses and their unit-like sets are read in their own blocks; the single point that belongs here is the reason the plain product is special. An operation $\circ$ has a group of "units" only when its non-vanishing set is closed under $\circ$ and under $\circ$-inversion, and that closure needs the multiplicativity of an algebraic norm that the operation respects. The general plain product has it, through $\langle \breve Q_{1}\breve Q_{2}\rangle_{\mathrm{ts}}=\langle \breve Q_{1}\rangle_{\mathrm{ts}}\langle \breve Q_{2}\rangle_{\mathrm{ts}}$; the other operations do not preserve $\langle\cdot\rangle_{\mathrm{ts}}$, so their non-vanishing sets are not closed under them, and their invertible elements do not form a group of the same kind. The biquaternion counterpart of this section is *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Group of Units*, §*The Complement in the Other Eleven Structures*.

## Summary

The general plain algebra of the reduced biquaternions is the disjoint union of its unit group, its nonzero zero divisors and the single element $0$. An element $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ is a unit exactly when its norm $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ does not vanish, equivalently when neither idempotent coordinate $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$ vanishes; the inverse is $(Q_{\blacktriangle}-jQ_{\blacktriangledown})/(Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2})$, or $(Q_{+}^{-1},Q_{-}^{-1})$ in the idempotent coordinates. The unit group is the abelian group $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ under the isomorphism $\breve Q\mapsto(Q_{+},Q_{-})$, connected, of complex dimension two, with fundamental group $\mathbb{Z}\times\mathbb{Z}$; the biquaternion unit group $GL(2,\mathbb{C})$ is its non-abelian counterpart. The complement of the group is the null set of the norm, the union of the two idempotent lines $\mathbb{C}\Pi_+\cup\mathbb{C}\Pi_-$; it is the complement of the open dense unit group, is closed and of empty interior, and is therefore the topological boundary of the group; it is a union of two complex lines and not an irreducible cone, because the norm factors as $(Q_{\blacktriangle}+Q_{\blacktriangledown})(Q_{\blacktriangle}-Q_{\blacktriangledown})$. On the remarkable subspaces every nonzero element of the scalar line, the $j$-line, the Hermitian plane and the anti-Hermitian plane is a unit, the two split planes carry the two real zero-divisor lines $\mathbb{R}\Pi_+$, $\mathbb{R}\Pi_-$ beside their units, and every nonzero element of the two idempotent lines is a zero divisor. The closure of the non-vanishing set under the operation is what makes a group, and only the plain product has it.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | a general element |
| $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ | the algebraic norm of the multiplication |
| $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown},\ Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$ | the idempotent coordinates |
| $\mathbb{B}_{\mathrm{r}}^{\times}$ | the group of units |
| $\mathcal N=\{\breve Q\neq0:\langle \breve Q\rangle_{\mathrm{ts}}=0\}=\mathbb{C}^{\times}\Pi_+\cup\mathbb{C}^{\times}\Pi_-$ | the zero-divisor set, the punctured null set |
| $\mathcal N\cup\{0\}=\mathbb{C}\Pi_+\cup\mathbb{C}\Pi_-$ | the null set, the union of the two idempotent lines |
| $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ | the unit group, under $\breve Q\mapsto(Q_{+},Q_{-})$ |
| $\breve Q^{-1}=(Q_{\blacktriangle}-jQ_{\blacktriangledown})/(Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2})$ | the inverse of a unit |
| $\partial\mathbb{B}_{\mathrm{r}}^{\times}=\mathcal N\cup\{0\}$ | the boundary of the unit group |
| $GL(2,\mathbb{C})$ | the biquaternion unit group, the non-abelian companion |

## Further Reading

- [Norm and Invertibility in the Algebra of the Reduced Biquaternions](norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the norm and the criterion.
- [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the zero-divisor set and the two lines.
- [The Specificities of the Algebra of the Reduced Biquaternions](the-specificities-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the associativity and the central split that make the group.
- [Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions](ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the idempotent lines as the minimal ideals.
- [The Multiplication Operators of the Algebra of the Reduced Biquaternions](the-multiplication-operators-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the invertibility of the operators.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the non-abelian companion.
