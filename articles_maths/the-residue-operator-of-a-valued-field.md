
# __The Residue Operator of a Valued Field__

## Introduction

A valued field carries a canonical ring homomorphism to a field of a different kind: the **residue map**, which sends an element of the valuation ring to its class modulo the maximal ideal. Read as an operator it is a continuous surjection whose kernel is the maximal ideal, whose image is the residue field and whose domain is the valuation ring; it is the operator by which a valued field is compared with its residue field, and it is the reduction that every lifting theorem inverts. This article treats the residue map for itself: it fixes the operator, computes its kernel, its image and its continuity, shows that it is a morphism of the valued structure, records its extension to the completion, and separates its additive part from its multiplicative part, where it is a homomorphism from the principal units to the residue field.

The article assumes the absolute value, the valuation, the valuation ring $\mathcal{O}$, the maximal ideal $\mathrm{M}$ and the residue field $k = \mathcal{O}/\mathrm{M}$ from *Absolute Values, Valuations and Completions*; the linear topology of the valuation ring, the closure of zero and the completion from *Topological Rings and Fields*; the completion operator and its kernel from *The Completion Operator*; and the continuous homomorphisms and the ring operators from *Operators on a Topological Ring*. Local compactness, the structure of the multiplicative group $\mathcal{O}^\times$, the ramification and the maximal unramified extension are *Local Fields*, and are named only. No measure and no norm occurs beyond the absolute value already carried by the field.

Throughout, $F$ is a field with a non-Archimedean absolute value $\lvert \cdot \rvert$ or, equivalently, a valuation $v$ into an ordered abelian group $\Gamma$; $\mathcal{O} = \{x : \lvert x \rvert \leq 1\}$ is its valuation ring, $\mathrm{M} = \{x : \lvert x \rvert < 1\}$ its maximal ideal, $k = \mathcal{O}/\mathrm{M}$ its residue field, $\Gamma = \lvert F^\times \rvert$ its value group and $\mathrm{res}$ its residue map. The completion is written $\widehat{F}$ and its valuation ring $\widehat{\mathcal{O}}$.

## The Reduction

**Definition.** The **residue map** of the valued field $(F, \lvert \cdot \rvert)$ is the quotient map

$$
\mathrm{res} : \mathcal{O} \longrightarrow k = \mathcal{O}/\mathrm{M}, \qquad \mathrm{res}(x) = x + \mathrm{M} .
$$

The element $\mathrm{res}(x)$ is the **residue** of $x$; the operator $\mathrm{res}$ is also called the **reduction** modulo $\mathrm{M}$, and written $x \mapsto \bar x$.

**Proposition (it is a ring homomorphism).** The residue map is a surjective ring homomorphism with kernel $\mathrm{M}$; it carries $1$ to $1$, it is additive and multiplicative, and it is the unique ring homomorphism from $\mathcal{O}$ onto $k$ with kernel $\mathrm{M}$.

**Proof.** The quotient map of a ring onto a quotient by an ideal is a surjective ring homomorphism with that ideal as kernel; the uniqueness is the universal property of the quotient.

**Proposition (the valuation ring and the residue field as domain and image).** The valuation ring is the domain of the residue map, $\mathrm{res}$ is defined exactly on $\mathcal{O}$, and the residue field is its image, $k = \mathrm{res}(\mathcal{O})$. An element $x$ is a unit of $\mathcal{O}$ exactly when $\mathrm{res}(x) \neq 0$; the non-units are exactly the elements of $\mathrm{M}$.

**Proof.** By definition $\mathrm{res}$ has domain $\mathcal{O}$ and image $\mathcal{O}/\mathrm{M} = k$. An element of a local ring is a unit exactly when its image in the residue field is nonzero; here the local ring is $\mathcal{O}$ with maximal ideal $\mathrm{M}$.

**Proposition (the residue map is continuous).** Give $\mathcal{O}$ the subspace topology of the metric topology of $F$ and $k$ the discrete topology. Then $\mathrm{res}$ is continuous, open and closed, its fibres are the cosets of $\mathrm{M}$, which are open and closed, and it is a quotient map.

**Proof.** The kernel $\mathrm{M} = \{x : \lvert x \rvert < 1\}$ is open, being a ball, so its cosets are open; a map to a discrete space is continuous exactly when the fibres are open, which they are; the fibres are also closed because their complements are unions of fibres, so the map is closed. It is open because it is the quotient map of an open equivalence relation.

## The Kernel and the Image

**Proposition (kernel and image).** The kernel of the residue map is the maximal ideal, $\ker \mathrm{res} = \mathrm{M}$, a closed ideal of $\mathcal{O}$; the image is the residue field, $\operatorname{im} \mathrm{res} = k$, a field; and the residue map factors as the quotient of $\mathcal{O}$ by the closed ideal $\mathrm{M}$ followed by an isomorphism onto $k$.

**Proof.** The kernel of a quotient map by $\mathrm{M}$ is $\mathrm{M}$; the ideal is closed because it is the preimage of the closed point $0$ of the discrete field under the continuous map. The factorisation is the first isomorphism theorem.

**Corollary (the residue of the ideals).** The residue map carries an ideal $I$ of $\mathcal{O}$ to the ideal $\mathrm{res}(I) = (I + \mathrm{M})/\mathrm{M} = \bar I$ of $k$, and it carries the chain of ideals $\mathcal{O} \supseteq \mathrm{M} \supseteq \mathrm{M}^2 \supseteq \cdots$ to the decreasing chain $k \supseteq 0 = 0 = \cdots$. In particular the residue map detects whether an ideal is contained in $\mathrm{M}$: $\mathrm{res}(I) = 0$ exactly when $I \subseteq \mathrm{M}$, and $\mathrm{res}(I) = k$ exactly when $I = \mathcal{O}$.

**Proof.** The image of an ideal under a surjective homomorphism is an ideal; the computation of $\mathrm{res}(I)$ is the definition, and the vanishing is the statement that every element of $I$ reduces to zero.

**Proposition (the residue is a morphism of the valued structure).** The residue map is compatible with the valuation in the sense that $\mathrm{res}(x) = 0$ exactly when $v(x) > 0$, and $\mathrm{res}(x)$ is a unit of $k$ exactly when $v(x) = 0$. Two elements of the same value have, in general, no relation between their residues: the residue forgets the value and keeps only the leading term, and elements $x, y \in \mathcal{O}$ satisfy $\mathrm{res}(x) = \mathrm{res}(y)$ exactly when $x - y \in \mathrm{M}$, that is when $v(x - y) > 0$. As a map of topological rings it is a continuous surjective homomorphism from the valuation ring onto the discrete residue field.

**Proof.** $\mathrm{res}(x) = 0$ means $x \in \mathrm{M}$, which is $v(x) > 0$; $\mathrm{res}(x)$ is a unit of the field $k$ exactly when it is nonzero, which is $v(x) = 0$. For the relation between the residues, $\mathrm{res}(x) = \mathrm{res}(y)$ is $x - y \in \mathrm{M}$ by the definition of the quotient, which is $v(x - y) > 0$. The homomorphism statement is additivity and multiplicativity together with the continuity of the previous proposition.

## The Residue Operator and the Completion

**Theorem (the residue operator of the completion).** Let $\widehat{F}$ be the completion of $F$. Then $\widehat{\mathcal{O}}$ is the valuation ring of $\widehat{F}$ and the natural map

$$
\mathcal{O}/\mathrm{M} \longrightarrow \widehat{\mathcal{O}}/\widehat{\mathrm{M}}, \qquad x + \mathrm{M} \longmapsto \iota(x) + \widehat{\mathrm{M}} ,
$$

is an isomorphism; hence the residue map of the completion has the same residue field as the residue map of $F$, and the two operators are related by $\mathrm{res}_{\widehat{F}} \circ \iota = \mathrm{res}_F$ on $\mathcal{O}$.

**Proof.** The completion of a non-Archimedean valued field preserves the value group and the residue field, which is the standard theorem of *Absolute Values, Valuations and Completions*; the natural map is a ring homomorphism and is bijective by that theorem. The identity of the two reductions is then the commutativity of the square defining the map on classes.

**Corollary (residue commutes with completion).** Completing the field and passing to the residue are operations that commute: the residue operator of the completion restricts along $\iota$ to the residue operator of the field, and no new residue appears. In particular a lift of a residue element from $k$ to $\widehat{\mathcal{O}}$ may be taken in $\mathcal{O}$ when the field is Henselian, which is Hensel's lemma and belongs to *Absolute Values, Valuations and Completions* and *Local Fields*.

**Proof.** The commutativity is the theorem; the lifting statement is Hensel's lemma, quoted and not proved here.

## The Multiplicative Residue

**Proposition (the residue is multiplicative on the units).** The restriction $\mathrm{res} : \mathcal{O}^\times \to k^\times$ is a surjective group homomorphism with kernel the **principal units** $U^1 = 1 + \mathrm{M}$, so that

$$
\mathcal{O}^\times / (1 + \mathrm{M}) \cong k^\times .
$$

**Proof.** A unit of $\mathcal{O}$ has nonzero residue and a nonzero residue has a unit preimage, because reduction is surjective and the units of a local ring are the elements of nonzero residue; the kernel is the set of units congruent to $1$ modulo $\mathrm{M}$, namely $1 + \mathrm{M}$. The first isomorphism theorem for groups gives the isomorphism.

**Corollary (the two parts of the residue operator).** The residue map splits the study of $\mathcal{O}$ into an additive part, in which it is the quotient by the maximal ideal, and a multiplicative part, in which it exhibits $k^\times$ as the quotient of the units by the principal units. The filtration $U^n = 1 + \mathrm{M}^n$ of the principal units and its quotients $U^n/U^{n+1} \cong k^+$ are the structure of the multiplicative group of a local field and belong to *Local Fields*.

**Proof.** The additive part is the definition; the multiplicative part is the proposition. The filtration statement is the standard computation of *Local Fields*, named and not used.

## Examples

**Example ($\mathbb{Z}_p$ and $\mathbb{F}_p$).** For $F = \mathbb{Q}_p$, $\mathcal{O} = \mathbb{Z}_p$, $\mathrm{M} = p\mathbb{Z}_p$ and $k = \mathbb{F}_p$; the residue map $\mathbb{Z}_p \to \mathbb{F}_p$ is the reduction modulo $p$, it is continuous and surjective, and its kernel is $p\mathbb{Z}_p$. On the units it is $\mathbb{Z}_p^\times \to \mathbb{F}_p^\times$ with kernel $1 + p\mathbb{Z}_p$, so $\mathbb{Z}_p^\times/(1+p\mathbb{Z}_p) \cong \mathbb{F}_p^\times$.

**Example ($k[[t]]$ and $k$).** For $F = k((t))$, $\mathcal{O} = k[[t]]$, $\mathrm{M} = t k[[t]]$ and the residue field is $k$; the residue map is the evaluation at $t = 0$, carrying a series to its constant term, and its kernel is the ideal of series with zero constant term.

**Example (the reduction of a polynomial).** Let $f \in \mathcal{O}[X]$; applying $\mathrm{res}$ to the coefficients gives the reduction $\bar f \in k[X]$. The map $f \mapsto \bar f$ is the residue operator on the polynomial ring, and Hensel's lemma is the statement that a simple root of $\bar f$ lifts to a root of $f$, which is the exact inverse of the reduction on the roots.

## Summary

The residue operator of a valued field is the quotient map $\mathrm{res} : \mathcal{O} \to k = \mathcal{O}/\mathrm{M}$ sending an element of the valuation ring to its class modulo the maximal ideal. It is a surjective ring homomorphism with kernel $\mathrm{M}$, its domain is the valuation ring and its image is the residue field, and with the discrete topology on $k$ it is continuous, open and closed with the cosets of $\mathrm{M}$ as fibres; it is the unique homomorphism from $\mathcal{O}$ onto $k$ with kernel $\mathrm{M}$. An element of $\mathcal{O}$ is a unit exactly when its residue is nonzero, and the residue carries an ideal $I$ to the ideal $(I+\mathrm{M})/\mathrm{M}$, vanishing exactly on the ideals contained in $\mathrm{M}$.

The residue operator commutes with completion: the completion of a non-Archimedean valued field has the same residue field, $\mathcal{O}/\mathrm{M} \cong \widehat{\mathcal{O}}/\widehat{\mathrm{M}}$, and the residue of the completion restricts along $\iota$ to the residue of the field, so no new residue appears and a lift of a residue element may be taken in the field when the field is Henselian. On the units the residue is a surjective homomorphism $\mathcal{O}^\times \to k^\times$ with kernel the principal units $1 + \mathrm{M}$, giving $\mathcal{O}^\times/(1+\mathrm{M}) \cong k^\times$; the additive part is the quotient by $\mathrm{M}$ and the multiplicative part is the quotient by the principal units, and the higher filtration is the structure theory of a local field.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $\lvert \cdot \rvert$, $v$ | Valued field, its absolute value and its valuation |
| $\mathcal{O}$, $\mathrm{M}$, $k = \mathcal{O}/\mathrm{M}$ | Valuation ring, maximal ideal and residue field |
| $\mathrm{res} : \mathcal{O} \to k$ | The residue operator, $x \mapsto x + \mathrm{M}$ |
| $\bar x$ | The residue $\mathrm{res}(x)$ of $x$ |
| $\Gamma = \lvert F^\times \rvert$ | The value group |
| $\mathcal{O}^\times$, $U^1 = 1+\mathrm{M}$ | The units of $\mathcal{O}$ and the principal units |
| $\mathcal{O}^\times/U^1 \cong k^\times$ | The multiplicative residue |
| $\widehat{F}$, $\widehat{\mathcal{O}}$, $\widehat{\mathrm{M}}$ | The completion and its valuation ring and maximal ideal |
| $\mathrm{res}_{\widehat{F}}\circ\iota = \mathrm{res}_F$ | Residue commutes with completion |
| $f \mapsto \bar f$ | Reduction of a polynomial, the inverse of Hensel's lifting |

## Further Reading

- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for the residue field, the residue map and Hensel's lemma.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for the valuation ring as a topological ring and the continuity of the residue map.
- Nicolas Bourbaki, *Commutative Algebra, Chapters 1–7* (Springer, 1998), for valuations, valuation rings and the residue field of a valuation.
- James Milne, *Algebraic Number Theory* (v3.08, 2020, available online), for the residue field of a local field and the reduction of polynomials.
- Fernando Q. Gouvêa, *p-adic Numbers: An Introduction* (Springer, 2nd ed. 1997), for the reduction modulo $p$ of $\mathbb{Z}_p$ and Hensel's lemma with worked examples.
