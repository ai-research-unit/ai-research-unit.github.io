# __The Classes of Element of the Complex Algebra__

## Introduction

The complex field is the one-dimensional complex algebra, and this article reads on it the general classes of element: the zero divisors, the annihilators, the idempotents, the nilpotents, the roots, the ideals and the modules. The answer is short and it is the answer of a field. Most of these classes are empty or two-point on $\mathbb{C}$, and the work of the article is to say which, to prove it, and to account for the collapse.

The article is a consolidation, not a translation. On $\mathbb{C}$ the classes are not numerous enough to carry an article each, so they are gathered here as sections. Nothing is proved twice: the products $Q_1Q_2$ and $Q_1\bar Q_2$ are *The Two Products of the Complex Space*, the two forms $\langle Q_1,Q_2\rangle=Q_1Q_2$ and $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ and the two algebraic norms $Q_1^{2}$ and $Q_1\bar Q_1$ are *The Two Forms and the Two Algebraic Norms of the Complex Space*, and the norm, the invertibility criterion and the group of invertibles are *Complex Norm and Invertibility*. Every class below is a class of element of the algebra, taken with respect to a product. The field property behind every emptiness is *The Specificities of the Complex Algebra*, below this article in this category.

**Interpretation and notation.** The base involution is the complex conjugation $\bar Q_1=q_1-iq'_1$; the Hermitian conjugation is the bar, ${}^{*}=\bar{\cdot}$. The two products are the plain bilinear product $Q_1Q_2$, the multiplication of the field, and the plain sesquilinear product $Q_1\bar Q_2$. The element is $Q_1=q_1+iq'_1$, a second element is $Q_2=q_2+iq'_2$, and their product is $Q_1Q_2=(q_1q_2-q'_1q'_2)+i(q_1q'_2+q'_1q_2)$. The two brackets $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}$ name the two forms, and are never used for elements. A class of element is defined with respect to a product, and every class below is read in both products.

## The Zero Divisors and the Annihilators

**Definition.** An element $Q_1$ is a **zero divisor** of a product when $Q_1\neq0$ and some $Q_2\neq0$ has $Q_1Q_2=0$ or $Q_2Q_1=0$; the **annihilator** of $Q_1\neq0$ is the set of the $Q_2$ with $Q_1Q_2=0$ (the left annihilator) or with $Q_2Q_1=0$ (the right annihilator).

**Theorem.** In either product $\mathbb{C}$ has no zero divisor, and the annihilator of every nonzero element is $\{0\}$ on both sides.

**Proof.** For the plain product, let $Q_1Q_2=0$ with $Q_1\neq0$. Since $\mathbb{C}$ is a field, $Q_1$ is invertible, and $Q_2=Q_1^{-1}(Q_1Q_2)=0$; the same on the other side. For the sesquilinear product, $Q_1\bar Q_2=0$ with $Q_1\neq0$ gives $\bar Q_2=Q_1^{-1}0=0$, hence $Q_2=0$; and $Q_2\bar Q_1=0$ with $Q_1\neq0$ gives $Q_2=0$. The annihilator statements are the same computation read as a set.

**Remark (the collapse of the class).** On $\mathbb{C}$ the zero divisors and the nontrivial annihilators both vanish, and for the same reason: an element is invertible exactly when it is nonzero.

## The Idempotents

**Definition.** An element $\Pi_{\mathrm{id}}$ is an **idempotent** of a product when $\Pi_{\mathrm{id}}^{2}=\Pi_{\mathrm{id}}$ in that product, the zero element being counted.

**Theorem.** In either product the idempotents of $\mathbb{C}$ are $0$ and $1$, and no more.

**Proof.** For the plain product, $\Pi_{\mathrm{id}}^{2}=\Pi_{\mathrm{id}}$ reads $\Pi_{\mathrm{id}}(\Pi_{\mathrm{id}}-1)=0$; the field has no zero divisor, so $\Pi_{\mathrm{id}}=0$ or $\Pi_{\mathrm{id}}=1$. For the sesquilinear product, $\Pi_{\mathrm{id}}\bar\Pi_{\mathrm{id}}=\Pi_{\mathrm{id}}$; if $\Pi_{\mathrm{id}}=0$ this holds, and if $\Pi_{\mathrm{id}}\neq0$ it gives $\bar\Pi_{\mathrm{id}}=1$, that is $\Pi_{\mathrm{id}}=1$, which is idempotent.

**Remark (the degenerate Peirce decomposition).** The Peirce decomposition of an algebra with respect to an idempotent $\Pi_{\mathrm{id}}$ separates the two corner pieces $\Pi_{\mathrm{id}}\mathbb{C}\Pi_{\mathrm{id}}$ and the two mixed pieces; here the only nonzero idempotent is $1$, for which the corner is $\mathbb{C}$ itself and both mixed pieces vanish. The decomposition is therefore trivial, and there are no minimal left ideals off the two obvious corner pieces.

## The Nilpotents

**Definition.** A nonzero element $\Pi_{\mathrm{nil}}$ is a **nilpotent** when some power of it vanishes. Over a field the square already suffices, since $\Pi_{\mathrm{nil}}^{n}=0$ with $n$ least factors as $\Pi_{\mathrm{nil}}\cdot\Pi_{\mathrm{nil}}^{n-1}=0$ and forces $\Pi_{\mathrm{nil}}^{n-1}=0$; the theorem below is proved for $\Pi_{\mathrm{nil}}^{2}=0$.

**Theorem.** In either product the only element of $\mathbb{C}$ with $\Pi_{\mathrm{nil}}^{2}=0$ is $0$.

**Proof.** For the plain product, $\Pi_{\mathrm{nil}}^{2}=0=\Pi_{\mathrm{nil}}\cdot\Pi_{\mathrm{nil}}$ forces $\Pi_{\mathrm{nil}}=0$ by the absence of zero divisors. For the sesquilinear product, $\Pi_{\mathrm{nil}}\bar\Pi_{\mathrm{nil}}=(u^{2}+u'{}^{2})$, where $\Pi_{\mathrm{nil}}=u+iu'$, and a sum of two real squares vanishes only at $u=u'=0$.

**Remark.** The second computation is also the reason the sesquilinear square of an element is a non-negative real, the value $\langle\Pi_{\mathrm{nil}}\rangle_{*}$ of the definite algebraic norm; the square-zero set of the sesquilinear product is the origin alone.

## The Roots of the Distinguished Values

**Definition.** A **root** of a value $W$ in a product is an element $Z$ with $Z^{2}=W$ in that product; a root of a central value is written $Ζ$, the tilde-free glyph of the complex layer, the case rule being the one of *Special Element and Peirce Conventions*, §*The Root Convention*.

**Theorem.** In the plain product the roots are as follows: of $-1$ exactly the two elements $i$ and $-i$; of $+1$ exactly the two elements $1$ and $-1$; of $0$ the element $0$ alone.

**Proof.** The equation $Z^{2}=W$ with $Z=z+iz'$ reads $z^{2}-z'{}^{2}=W$ and $2zz'=0$ for real $W$; thus $z=0$ or $z'=0$. For $W=-1$ the case $z=0$ gives $-z'{}^{2}=-1$, so $z'=\pm1$ and $Z=\pm i$, while the case $z'=0$ gives $z^{2}=-1$, with no real solution. For $W=+1$ the case $z'=0$ gives $z=\pm1$ and $Z=\pm1$, while the case $z=0$ gives $-z'{}^{2}=1$, with no real solution. For $W=0$ both cases give $Z=0$. In a field a quadratic equation has at most two roots, so the lists are complete.

**Remark (general value).** For a general $W=a+ia'\neq0$ the same equation has exactly two solutions, opposite to each other, written $Z=\pm Z_{0}$ with $Z_{0}^{2}=W$. For $W$ away from the closed negative real axis the root is

$$ \boxed{\;Z_{0}=\sqrt{\tfrac{r+a}{2}}+i\,\frac{a'}{2\sqrt{(r+a)/2}}, \qquad r=|W|=\sqrt{a^{2}+a'{}^{2}}\;},
$$

with real part $\sqrt{(r+a)/2}$ and imaginary part a real multiple of $a'$; on the negative real axis the formula degenerates and the root is the purely imaginary $Z_{0}=i\sqrt{|W|}$. The two roots are real exactly for the real $W>0$ and purely imaginary exactly for the real $W<0$; at every other value of $W$ both parts are non-zero. For $W=0$ the two roots coalesce into the single root $0$, so the criterion for two distinct roots is $W\neq0$. The existence of a root for every $W$ is the algebraic closure of $\mathbb{C}$, owned by *Complex Algebra*.

**Remark (the root sets compared).** On $\mathbb{C}$ the root sets are two points each, and the count is the count of a field.

## The Hermitian Square

**Remark (the sesquilinear reading).** The class of the square has a second reading in the sesquilinear product, and it is not the reading above. The square is now $Z\bar Z$, a real value $\ge0$, so the equation $Z\bar Z=W$ is solvable exactly for the real $W\ge0$: for $W>0$ it has the circle $\{Z:Z\bar Z=W\}$ of solutions, a one-parameter family rather than two points, and for $W<0$ or non-real $W$ it has none. The equation is therefore not the equation of a field, and its solvability is not the algebraic closure: the sesquilinear square is the diagonal of the Hermitian form and not the multiplication of the field. The form and its diagonal are *The Two Forms and the Two Algebraic Norms of the Complex Space* and *The Positivity and the Ray of Squares of the Complex Space*, below this article in this category.

## The Ideals and the Quotients

**Definition.** A **left ideal** of an algebra is an additive subgroup closed under left multiplication by the algebra; the two-sided ideals are the ideals of the ring.

**Theorem.** The complex field has exactly two two-sided ideals, $\{0\}$ and $\mathbb{C}$; it is simple; every nonzero ideal is the whole ring, and the quotient by a nonzero ideal is the zero ring.

**Proof.** Let $\mathrm{M}$ be a nonzero ideal and let $Q_1\in\mathrm{M}$ with $Q_1\neq0$. Since $Q_1$ is invertible, $1=Q_1^{-1}Q_1\in\mathrm{M}$, and an ideal containing $1$ is the whole ring. Hence no proper nonzero ideal exists.

**Remark.** The ideal $\mathbb{C}Q_1$ generated by a nonzero element is $\mathbb{C}$, the ideal generated by a square-zero element is $\{0\}$, and the two-sided ideals of the plain and of the sesquilinear product coincide as sets, both being the ring ideals of the field.

## The Modules

**Theorem.** Every module over $\mathbb{C}$ is free, and the finitely generated modules are classified by their rank alone: a finitely generated module is $\mathbb{C}^{n}$ for a unique $n$.

**Proof.** A module over a field is a vector space, and every vector space has a basis; the cardinality of a basis of a finitely generated space is finite and well defined, which is the rank. The definition of a module and of a free module is *Modules*; the rank is *Direct Sums, Free Modules and Rank*.

**Remark.** The regular module ${}_{\mathbb{C}}\mathbb{C}$ is one-dimensional, of rank one, and its endomorphism ring is $\mathbb{C}$ itself, so that the algebra and the endomorphisms of its regular module agree.

## Summary

Read on the complex field, these classes of element are the classes of a field. There are no zero divisors in either product, and the annihilator of every nonzero element is $\{0\}$ on both sides; the idempotents are $0$ and $1$ in the plain product and the same two in the sesquilinear one; the only nilpotent is $0$; the roots of $-1$ are $\pm i$, those of $+1$ are $\pm1$, and those of $0$ are $0$ alone, while a general nonzero value has exactly two opposite roots and the value $0$ has one; the Hermitian square $Z\bar Z$ is not the field square, and its equation is solvable exactly for the non-negative real values, with a circle of roots. The field has two ideals, $\{0\}$ and $\mathbb{C}$, and is simple; every module over it is free and the finitely generated ones are classified by rank alone. Every one of these emptinesses is the absence of zero divisors, that is, the field property, which is *The Specificities of the Complex Algebra*, below this article in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}$ | the complex field, the one-dimensional complex algebra |
| $Q_1=q_1+iq'_1$, $Q_2=q_2+iq'_2$ | two complex elements, with the real coordinates $q_1,q'_1$ and $q_2,q'_2$ |
| $\bar Q_1=q_1-iq'_1$ | the complex conjugation, the base involution; ${}^{*}=\bar{\cdot}$ |
| $Q_1Q_2$, $Q_1\bar Q_2$ | the general plain bilinear and the general plain sesquilinear product |
| $\Pi_{\mathrm{id}}$ | an idempotent of the complex layer, a capital with no tilde |
| $\Pi_{\mathrm{nil}}$ | a nilpotent of the complex layer, a capital with no tilde |
| $Ζ$ | a root of a central value, a capital with no tilde |

## Further Reading

- Serge Lang, *Algebra*, Graduate Texts in Mathematics 211 (Springer, third edition, 2002), for fields, ideals, modules, free modules and the rank of a finitely generated module.
- Nathan Jacobson, *Basic Algebra I* (Dover, second edition, 2009), for the field axioms, the polynomial ring over a field and the algebraically closed case.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the structure of fields, simple rings and the quotient by an ideal.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings*, Graduate Texts in Mathematics 131 (Springer, second edition, 2001), for simple rings, ideals and the contrast with a noncommutative algebra.
- Theodor W. Gamelin, *Complex Analysis* (Springer, 2001), for the algebraic closure of the complex field and the roots of a complex value.
