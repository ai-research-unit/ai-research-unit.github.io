# __The Left Multiplications of the Quaternionic Product and the Opposite Monoid__

## Introduction

The **left multiplication** of the general quaternionic bilinear product $\tilde p \star \tilde q = \tilde p^{\natural}\tilde q$ of *Introduction to the General Quaternionic Algebra of Quaternions* is the linear operator

$$
L_{\tilde p}(\tilde x) = \tilde p \star \tilde x = \tilde p^{\natural}\tilde x .
$$

The family $\{L_{\tilde p} : \tilde p \in \mathbb{H}\}$ is the image of the algebra in the space of linear operators, and it is the object that carries the semigroup-theoretic content of the block: the product is not associative, so the single fact that decides the whole one-sided theory is the **composition law of the family**, and that law turns out to be the *opposite* of the plain one. This article computes the law, describes the monoid it defines, identifies the $\mathbb{R}$-algebra of operators it generates, compares the whole picture with the plain algebra of the same space, and relates it to the two one-sided actions of the block.

The two-sided operators $\tilde q \mapsto \tilde a^{\natural}\tilde q\,\tilde b$ and the one-sided operators of the product are the articles of *Two-Sided Operators on the General Quaternionic Algebra of Quaternions* and *One-Sided Operators on the General Quaternionic Algebra of Quaternions*, both below this article in this category; this article owns the **left** family and the monoid, and it cites the other two for the adjoint theory and for the two-sided completer. The element theory is not used beyond the norm and the coincidence of the one-sided inverses (*Norm and Invertibility in the General Quaternionic Algebra*).

## The Left Multiplications and their Composition

**Definition.** For $\tilde p \in \mathbb{H}$ the **left multiplication** by $\tilde p$ is $L_{\tilde p} : \mathbb{H} \to \mathbb{H}$, $L_{\tilde p}(\tilde x) = \tilde p^{\natural}\tilde x$. It is an $\mathbb{R}$-linear endomorphism of $\mathbb{H}$, and it is the plain left multiplication by the conjugate: $L_{\tilde p} = M_{\tilde p^{\natural}}$, where $M_{\tilde a}(\tilde x) = \tilde a\tilde x$ is the plain left multiplication.

**Theorem (the composition law).** For all $\tilde p,\tilde q \in \mathbb{H}$,

$$
L_{\tilde p}L_{\tilde q} = L_{\tilde q\tilde p} , \qquad \text{and} \qquad L_{\tilde p^{\natural}}L_{\tilde q^{\natural}} = L_{\tilde p\tilde q} .
$$

The composition is therefore the **opposite** of the plain multiplication in the index, and the family closes under composition.

*Proof.* $L_{\tilde p}L_{\tilde q}(\tilde x) = M_{\tilde p^{\natural}}M_{\tilde q^{\natural}}(\tilde x) = \tilde p^{\natural}(\tilde q^{\natural}\tilde x) = (\tilde p^{\natural}\tilde q^{\natural})\tilde x$, and $\tilde p^{\natural}\tilde q^{\natural} = (\tilde q\tilde p)^{\natural}$ because the conjugation is an anti-automorphism of the plain product; hence $L_{\tilde p}L_{\tilde q} = M_{(\tilde q\tilde p)^{\natural}} = L_{\tilde q\tilde p}$. The second law is the first with $\tilde p^{\natural},\tilde q^{\natural}$ in place of $\tilde p,\tilde q$, using $\tilde p^{\natural\natural} = \tilde p$: $L_{\tilde p^{\natural}}L_{\tilde q^{\natural}} = L_{\tilde q^{\natural}\tilde p^{\natural}} = L_{(\tilde p\tilde q)^{\natural}}$ — applied to the element $\tilde p\tilde q$ — and $L_{(\tilde p\tilde q)^{\natural}} = L_{\tilde p\tilde q}$ because the index depends on the conjugate, $(\tilde p\tilde q)^{\natural\natural} = \tilde p\tilde q$.

**Remark.** The reindexing in the second law is the point of the article. The family is anti-isomorphic to the algebra through the identity map of the indices and isomorphic to it through the conjugation, so the same family carries two laws, and the choice between them is the choice of where the anti-automorphism is put. The first law is the one that the product forces; the second is the one that shows the family is a copy of the algebra itself and not of its opposite only.

## The Monoid

**Theorem (the monoid).** The family $\{L_{\tilde p}\}$ is closed under composition, contains the identity $L_{e_0} = \mathrm{id}$, and is therefore a monoid under composition. The map $\tilde p \mapsto L_{\tilde p}$ is a bijection onto it and an **anti-isomorphism** of monoids from the multiplicative monoid $(\mathbb{H},\cdot)$; equivalently it is an isomorphism $(\mathbb{H}^{\mathrm{opp}},\cdot) \to \{L_{\tilde p}\}$. The reindexed map $\tilde p \mapsto L_{\tilde p^{\natural}}$ is an isomorphism of monoids from $(\mathbb{H},\cdot)$.

*Proof.* Closure and the identity are the composition law read at $\tilde q = e_0$: $L_{e_0}(\tilde x) = e_0^{\natural}\tilde x = \tilde x$. Injectivity holds because $\tilde p$ is recovered from $L_{\tilde p}$ at $\tilde x = e_0$: $L_{\tilde p}(e_0) = \tilde p^{\natural}e_0 = \tilde p^{\natural}$, so the index is the conjugate of the value at $e_0$. The two isomorphism statements are the two laws of the composition theorem.

**Corollary (the units).** The invertible elements of the monoid are exactly the $L_{\tilde p}$ with $\tilde p$ invertible in the plain algebra, that is with $N(\tilde p) \neq 0$; the reindexing carries those to the nonzero elements, and the group of invertible elements of the monoid is the multiplicative group $\mathbb{H}^{\times}$, of real dimension four, isomorphic to the plain unit group. The quaternionic block therefore has a monoid of left multiplications whose group of units is the plain unit group, while the units of the product itself do not form a group (*Norm and Invertibility in the General Quaternionic Algebra*).

*Proof.* An element of a monoid of maps is invertible exactly when the map is a bijection; $L_{\tilde p}$ is bijective exactly when $M_{\tilde p^{\natural}}$ is, and a plain left multiplication is bijective exactly when its index is a unit of the division algebra, that is when $N(\tilde p) \neq 0$.

## The Enveloping Structure

**Theorem (the generated algebra).** The $\mathbb{R}$-linear span $L(\mathbb{H})$ of the family is a four-dimensional real subalgebra of $\mathrm{End}_{\mathbb{R}}(\mathbb{H})$, it is isomorphic to $\mathbb{H}^{\mathrm{opp}}$ under $\tilde p \mapsto L_{\tilde p}$, and it is a division algebra: every nonzero element of $L(\mathbb{H})$ is invertible as an operator. It is therefore simple, semisimple and central over $\mathbb{R}$; its centre is the line $\mathbb{R}\,\mathrm{id}$ generated by the identity operator.

*Proof.* The span is closed because the family is; it is four-dimensional because $\tilde p \mapsto L_{\tilde p}$ is injective and linear; the composition law makes it anti-isomorphic, hence isomorphic, to $\mathbb{H}^{\mathrm{opp}}$, and $\mathbb{H}^{\mathrm{opp}} \cong \mathbb{H}$ as an algebra through the conjugation (*The Two General Products of the Quaternion $\mathbb{R}$ Space*). A division algebra is simple and semisimple, and the centre of $\mathbb{H}\cong\mathbb{H}^{\mathrm{opp}}$ is the scalar line, which corresponds to the multiples of the identity.

**Corollary.** The left regular representation $\tilde p \mapsto L_{\tilde p}$ is a faithful anti-representation of $(\mathbb{H},\cdot)$ by linear operators, and the reindexed representation $\tilde p \mapsto L_{\tilde p^{\natural}}$ is a faithful representation. The whole two-sided operator algebra, in which $L(\mathbb{H})$ sits as one of two commuting copies, is *Two-Sided Operators on the General Quaternionic Algebra of Quaternions*, below this article in this category.

## The Comparison with the Plain Algebra

**Proposition.** For the plain product the left multiplication $M_{\tilde p}(\tilde x) = \tilde p\tilde x$ satisfies the **direct** law $M_{\tilde p}M_{\tilde q} = M_{\tilde p\tilde q}$, so the plain left regular representation is a homomorphism of algebras and its image is a copy of $\mathbb{H}$ with the direct law. For the quaternionic product the left multiplication satisfies the **opposite** law, and its image is a copy of $\mathbb{H}^{\mathrm{opp}}$.

*Proof.* The plain law is the associativity of the plain product; the quaternionic law is the composition theorem above.

**Remark.** The two images are the same subspace of $\mathrm{End}(\mathbb{H})$, spanned by the same four operators reindexed: $L_{\tilde p} = M_{\tilde p^{\natural}}$, so $L(\mathbb{H}) = M(\mathbb{H})$. What changes is the multiplication carried by that subspace, direct in the plain reading and opposite in the quaternionic one, and the change is exactly the anti-automorphism that the quaternionic product puts in the first slot. The two readings agree as sets of operators and differ as algebras, and they agree as algebras too through the conjugation, $\mathbb{H} \cong \mathbb{H}^{\mathrm{opp}}$; this is the classical statement that the quaternion algebra is anti-isomorphic to itself, and it is the reason a right unit can be manufactured out of the left family when the product does not supply one.

## The Two One-Sided Actions

**Theorem (the twisted right family).** The honest right multiplications $R_{\tilde p}(\tilde x) = \tilde x \star \tilde p = \tilde x^{\natural}\tilde p$ do **not** close under composition. The **twisted** right multiplications

$$
\varrho_{\tilde p}(\tilde x) = \tilde x\,\tilde p^{\natural} ,
$$

the plain right multiplication by the conjugate, do close, with the direct law $\varrho_{\tilde p}\varrho_{\tilde q} = \varrho_{\tilde p\tilde q}$, so that $\{\varrho_{\tilde p}\} \cong \mathbb{H}$ on the right; and the two families commute, $L_{\tilde p}\varrho_{\tilde q} = \varrho_{\tilde q}L_{\tilde p}$, so that $\mathbb{H}$ carries a two-sided action of $\mathbb{H}$ on itself.

*Proof.* For the failure, $R_{\tilde p}R_{\tilde q}(\tilde x) = (\tilde x^{\natural}\tilde q)^{\natural}\tilde p = \tilde q^{\natural}\tilde x\tilde p$; if this were $R_{\tilde r}(\tilde x) = \tilde x^{\natural}\tilde r$ for every $\tilde x$ then taking $\tilde x = e_0$ would give $\tilde r = \tilde q^{\natural}\tilde p$, and at $\tilde p = \tilde q = \tilde x = e_1$ the two sides would be $\tilde q^{\natural}\tilde x\tilde p = (-e_1)e_1e_1 = e_1$ and $\tilde x^{\natural}\tilde r = (-e_1)(e_1^{\natural}e_1) = -e_1$, which differ. For the direct law of the twisted family, $\varrho_{\tilde p}\varrho_{\tilde q}(\tilde x) = (\tilde x\tilde q^{\natural})\tilde p^{\natural} = \tilde x(\tilde q^{\natural}\tilde p^{\natural}) = \tilde x(\tilde p\tilde q)^{\natural} = \varrho_{\tilde p\tilde q}(\tilde x)$. For the commutation, both readings are the composition of the plain left multiplication $M_{\tilde p^{\natural}}$ with the plain right multiplication by $\tilde q^{\natural}$, which commute by the associativity of the plain product, $(a\tilde x)b = a(\tilde x b)$.

**Corollary (the two one-sided actions and the missing right unit).** The product of the block has a left unit and no right one; its left multiplications form the monoid $L(\mathbb{H}) \cong \mathbb{H}^{\mathrm{opp}}$ and its honest right multiplications do not form a monoid at all; its twisted right multiplications form a monoid and give a right action, and the two commute. The asymmetry of the unit is therefore visible at the level of the operators as the choice of the twist: the left action needs no twist, the right action needs one, and the twist is the conjugation.

*Proof.* The unit statements are those of *Introduction to the General Quaternionic Algebra of Quaternions* and *The Specificities of the General Quaternionic Algebra*; the operator statements are the two composition laws above. A right unit would be an operator $R_{\tilde u}$ equal to the identity, and $R_{\tilde u}(\tilde x) = \tilde x^{\natural}\tilde u$ is never $\tilde x$ for all $\tilde x$ by the non-existence theorem for the right unit.

## Summary

The left multiplication of the quaternionic product is $L_{\tilde p}(\tilde x) = \tilde p^{\natural}\tilde x$, the plain left multiplication by the conjugate; the family closes under composition with the **opposite** law $L_{\tilde p}L_{\tilde q} = L_{\tilde q\tilde p}$, and it is reindexed to the direct law $L_{\tilde p^{\natural}}L_{\tilde q^{\natural}} = L_{\tilde p\tilde q}$. As a monoid it is anti-isomorphic to $(\mathbb{H},\cdot)$ and isomorphic to $(\mathbb{H}^{\mathrm{opp}},\cdot)$; its group of units is the plain unit group $\mathbb{H}^{\times}$, of real dimension four. Its linear span is a four-dimensional real division subalgebra of $\mathrm{End}_{\mathbb{R}}(\mathbb{H})$, simple, semisimple and central, isomorphic to $\mathbb{H}^{\mathrm{opp}} \cong \mathbb{H}$ and equal as a subspace to the plain left-multiplication algebra. The plain reading is direct where this one is opposite, and the difference is the conjugation in the first slot. The honest right multiplications do not close; the twisted ones do, with the direct law, and they commute with the left family, so the block carries a left action and a twisted right action, and the missing right unit is visible as the twist that the right action needs and the left one does not.

## Summary of Notation

| symbol | meaning |
|---|---|
| $L_{\tilde p}(\tilde x) = \tilde p \star \tilde x = \tilde p^{\natural}\tilde x$ | the left multiplication of the quaternionic product |
| $L_{\tilde p}L_{\tilde q} = L_{\tilde q\tilde p}$ | the composition law, the opposite of the plain one |
| $L_{\tilde p^{\natural}}L_{\tilde q^{\natural}} = L_{\tilde p\tilde q}$ | the same family, reindexed to the direct law |
| $M_{\tilde a}(\tilde x) = \tilde a\tilde x$ | the plain left multiplication, $L_{\tilde p} = M_{\tilde p^{\natural}}$ |
| $R_{\tilde p}(\tilde x) = \tilde x \star \tilde p$ | the honest right multiplication, which does not close |
| $\varrho_{\tilde p}(\tilde x) = \tilde x\tilde p^{\natural}$ | the twisted right multiplication, $\varrho_{\tilde p}\varrho_{\tilde q} = \varrho_{\tilde p\tilde q}$ |
| $L(\mathbb{H})$ | the four-dimensional algebra generated by the family, $\cong \mathbb{H}^{\mathrm{opp}}$ |
| $\mathbb{H}^{\mathrm{opp}}$ | the opposite algebra, $\cong \mathbb{H}$ through the conjugation |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the multiplication algebra of a nonassociative algebra and its enveloping structure.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the left and right multiplication operators of a bilinear product and the mutations of a product.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the regular representation, the opposite ring and the anti-isomorphism $\mathbb{H} \cong \mathbb{H}^{\mathrm{opp}}$.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the multiplication algebra generated by the left and right multiplications of an algebra.
