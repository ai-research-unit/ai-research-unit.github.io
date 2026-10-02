
# __The Completion Operator__

## Introduction

The completion of a topological ring is a ring through which the given ring maps, into which its Cauchy sequences converge, and which is characterised by a single universal property; read as an assignment on rings it is an **operator**, $R \mapsto \widehat{R}$, defined on the category of topological rings. This article treats that operator for itself: it fixes the completion, proves that the assignment is a functor, identifies the universal property as the statement that the operator is the reflection of the category into its complete Hausdorff subcategory, computes the kernel as the closure of zero, shows that the operator is idempotent and hence adds nothing the second time, and records its behaviour on ideals, quotients and products.

The article assumes the topological ring, its neighbourhoods of zero, its linear topologies, the closure of zero, the fundamental system of ideals, the $I$-adic topology and the inverse limit $\varprojlim R/I^n$ from *Topological Rings and Fields*; the ring homomorphism and the quotient and product constructions from *Rings*; and the continuous operators, the monoid $\operatorname{Map}_c(R)$, the homeomorphisms and the continuous homomorphisms from *Operators on a Topological Ring*. The metric completion of a valued field, the fields $\mathbb{Q}_p$ and $\mathbb{R}$ and the persistence of the residue field are *Absolute Values, Valuations and Completions*, and are named only: this article completes a ring for a linear topology, and the valued completion is a different construction on a different object. No measure, no norm and no form occurs.

Throughout, $R$ is a topological ring carrying a linear topology, that is a topology for which the neighbourhoods of zero are the ideals of a fundamental system; $\widehat{R}$ is its completion; $\iota_R : R \to \widehat{R}$ is the canonical continuous homomorphism; $\overline{\{0\}}$ is the closure of zero; and $\mathcal{C}$ denotes the category of complete Hausdorff topological rings with continuous homomorphisms.

## The Completion

**Definition.** Let $R$ be a topological ring with a linear topology given by a fundamental system of neighbourhoods of zero consisting of ideals $\{I_\lambda\}_{\lambda \in \Lambda}$, directed by containment. The **completion** of $R$ is the inverse limit

$$
\widehat{R} = \varprojlim_{\lambda} R/I_\lambda ,
$$

taken in the category of rings, with the inverse limit topology, and the **canonical map** $\iota_R : R \to \widehat{R}$ sends $x$ to the family of its classes. When the topology is the $I$-adic topology of a single ideal $I$, so that the fundamental system is $\{I^n\}_{n\geq 0}$, this reads $\widehat{R} = \varprojlim_n R/I^n$.

**Proposition (the completion is a topological ring).** $\widehat{R}$ is a ring under componentwise operations, the projections $\pi_\lambda : \widehat{R} \to R/I_\lambda$ are ring homomorphisms, the inverse limit topology is a linear topology with fundamental system the kernels of the $\pi_\lambda$, and $\widehat{R}$ is complete and Hausdorff for it. The map $\iota_R$ is a continuous ring homomorphism.

**Proof.** The inverse limit of rings, taken componentwise in $\prod_\lambda R/I_\lambda$, is the subring of the product on which the transition maps agree; the restrictions of the product operations make it a ring and the projections homomorphisms. The inverse limit topology is the weakest making all projections continuous; the kernels of the projections are ideals forming a fundamental system of neighbourhoods of zero, so the topology is linear. An inverse limit of complete Hausdorff rings is complete and Hausdorff, and the $R/I_\lambda$ are complete and Hausdorff because they are discrete, which is the standard statement for the inverse limit of a system of discrete rings. The map $\iota_R$ is a homomorphism because each component $R \to R/I_\lambda$ is one, and it is continuous because each component is.

**Proposition (the kernel and the Hausdorff quotient).** The kernel of $\iota_R$ is the closure of zero, $\ker \iota_R = \overline{\{0\}}$, a closed ideal; $\iota_R$ is injective exactly when $R$ is Hausdorff; and the completion of $R$ depends only on its Hausdorff quotient, $\widehat{R} \cong \widehat{R/\overline{\{0\}}}$.

**Proof.** An element $x$ lies in the kernel exactly when $x \in I_\lambda$ for every $\lambda$, which is exactly the condition $x \in \overline{\{0\}}$ for a linear topology. The closure of zero is an ideal because the ideals $I_\lambda$ are closed and their intersection is closed, and it is the smallest closed ideal. The two rings $R$ and $R/\overline{\{0\}}$ have the same quotients $R/I_\lambda$, because every $I_\lambda$ contains $\overline{\{0\}}$, so their inverse limits coincide.

So the completion of a non-Hausdorff ring is the completion of its Hausdorff quotient; the operator is blind to the closure of zero, and it is on Hausdorff rings that it embeds.

## Functoriality

**Proposition (continuity gives uniform continuity).** Let $f : R \to S$ be a continuous homomorphism of topological rings with linear topologies. Then $f$ is uniformly continuous for the additive uniformities, and $f(I_\lambda) \subseteq J_\mu$ for every $\mu$ and all sufficiently small $\lambda$.

**Proof.** A homomorphism of additive topological groups commutes with the translations, and a continuous homomorphism at the origin is continuous at every point; for the additive uniform structures, which are the left uniform structures of the additive groups, continuity at every point is uniform continuity. The condition $f(I_\lambda) \subseteq J_\mu$ is the continuity of $f$ at $0$ read on the fundamental systems.

**Theorem (functoriality).** Let $f : R \to S$ be a continuous homomorphism of topological rings with linear topologies. Then there is a unique continuous homomorphism $\widehat{f} : \widehat{R} \to \widehat{S}$ with $\widehat{f}\circ \iota_R = \iota_S \circ f$, given componentwise by the induced maps $\bar{f} : R/I_\lambda \to S/J_\mu$. The assignment $f \mapsto \widehat{f}$ is functorial: $\widehat{\mathrm{id}} = \mathrm{id}$ and $\widehat{g \circ f} = \widehat{g}\circ \widehat{f}$.

**Proof.** Uniform continuity gives, for each $\mu$, a $\lambda$ with $f(I_\lambda) \subseteq J_\mu$, hence a well-defined ring homomorphism $R/I_\lambda \to S/J_\mu$, and these are compatible with the transition maps by construction; passing to the limit gives $\widehat{f}$. Uniqueness holds because $\iota_R(R)$ is dense in $\widehat{R}$ and a continuous map is determined by its values on a dense set; density holds because in each discrete quotient $R/I_\lambda$ the image of $R$ is everything. The functorial identities are immediate from the componentwise definition.

**Corollary (the completion is a functor).** The completion is an endofunctor of the category of topological rings with linear topologies and continuous homomorphisms, and it takes values in the full subcategory $\mathcal{C}$ of complete Hausdorff rings.

**Proof.** The theorem gives the action on morphisms and the preceding proposition gives the object-level statement; the values are complete Hausdorff by the first proposition.

## The Universal Property

**Theorem (universal property).** Let $R$ be a topological ring with a linear topology and let $T$ be a complete Hausdorff topological ring. For every continuous homomorphism $g : R \to T$ there is a unique continuous homomorphism $h : \widehat{R} \to T$ with $h \circ \iota_R = g$.

**Proof.** The map $g$ is uniformly continuous, so it carries the Cauchy filter of $R$ to a Cauchy filter of $T$, which converges in the complete ring $T$ to a limit $h(x)$ for each $x \in \widehat{R}$; the limit is independent of the approximating net and is continuous in $x$, and it is additive and multiplicative because those operations are continuous and compatible with limits. Uniqueness is again density of $\iota_R(R)$ in $\widehat{R}$.

**Corollary (the completion is a reflection).** The operator $R \mapsto \widehat{R}$, together with $\iota_R$, is the reflection of the category of topological rings with linear topologies into the full subcategory of complete Hausdorff rings: the functor $\widehat{}$ is left adjoint to the inclusion of $\mathcal{C}$, and the unit of the adjunction is $\iota$.

**Proof.** The universal property is the statement that the map $h \mapsto h\circ\iota_R$ from continuous homomorphisms $\widehat{R} \to T$ to continuous homomorphisms $R \to T$ is a bijection, which is the defining property of a reflection; the inclusion functor is the right adjoint.

**Proposition (Hausdorffisation).** Passing to the Hausdorff quotient and completing are the same in the sense that $\iota_R$ factors as the quotient map $R \to R/\overline{\{0\}}$ followed by the injective completion map of the Hausdorff ring, and the reflection kills exactly the closure of zero.

**Proof.** The quotient map has kernel $\overline{\{0\}}$, and the completion of the quotient is the completion of $R$ by the proposition above; the second map is injective because the quotient is Hausdorff.

## Idempotence

**Theorem (the operator is idempotent).** For a topological ring $R$ with a linear topology the canonical map $\iota_{\widehat{R}} : \widehat{R} \to \widehat{\widehat{R}}$ is an isomorphism of topological rings; equivalently $\widehat{R}$ is complete.

**Proof.** The completion $\widehat{R}$ is complete by the first proposition, so $\iota_{\widehat{R}}$ is the canonical map of a complete ring into its completion and is a homeomorphism; alternatively, the quotients $\widehat{R}/\widehat{I}_\lambda$ equal those of $R$ by the exactness of the inverse limit of a system with surjective transition maps, and the two inverse limits coincide.

**Corollary.** The operator $R \mapsto \widehat{R}$ is idempotent: applied twice it gives the same ring, and the natural transformation $\iota : \mathrm{id} \to \widehat{}$ is an isomorphism precisely on the complete Hausdorff rings. So the operator is a projection of the category of topological rings onto its complete Hausdorff subcategory, which it fixes pointwise.

**Proof.** The theorem is the idempotence; the unit is an isomorphism at a complete Hausdorff ring $T$ because the universal property applied to $\mathrm{id}_T$ inverts $\iota_T$.

## Behaviour on Ideals and Quotients

**Proposition (ideals).** Let $I$ be an ideal of $R$ with the subspace topology and the induced linear topology. Then $\widehat{I}$ is an ideal of $\widehat{R}$, the inclusion extends to a continuous injective map $\widehat{I} \to \widehat{R}$, and when $I$ is closed and $R$ is complete the map is a homeomorphism onto $I$. The completion of the quotient is the quotient of the completion,

$$
\widehat{R/I} \cong \widehat{R}/\widehat{I} ,
$$

for the topology on $R/I$ given by the images of the $I_\lambda$.

**Proof.** The completion of the inclusion is a continuous homomorphism by functoriality, injective because an element of $\widehat I$ has a vanishing image in each $R/I_\lambda$ only if it vanishes in $I/I_\lambda$ for all $\lambda$, which means it is zero; the image is an ideal because the multiplication of limits is the limit of the products. The quotient statement follows from the exactness of the inverse limit over a directed set for sequences of surjections: $\varprojlim (R/I_\lambda)/(I/I_\lambda) = \varprojlim R/I_\lambda$ modulo the closures of the images.

**Proposition (exactness).** The completion functor is left exact: it preserves kernels and finite products. It need not be right exact, and it is exact on the category of finitely generated modules over a Noetherian ring with the $I$-adic topology, by the Artin–Rees lemma.

**Proof.** The inverse limit over a directed set is left exact, being a limit; it is not right exact in general because the transition maps need not be surjective and the Mittag-Leffler condition can fail, which is the origin of the derived $\varprojlim^1$. For finitely generated modules over a Noetherian ring the topological refinement of the Artin–Rees lemma makes the transition maps essentially surjective on the relevant submodules, restoring exactness; this is the standard theorem of commutative algebra.

**Remark (the field case).** A field has no proper nonzero ideal, so the only linear topology on a field is the trivial one and its $I$-adic completion is the field itself; a nontrivial completion of a field therefore proceeds through an absolute value or a valuation and is the metric completion of *Absolute Values, Valuations and Completions*. The completion operator of this article is the one of a linear topology on a ring, and the two constructions agree on the subring $\mathcal{O}$ of a valued field, whose completion is $\varprojlim \mathcal{O}/\mathrm{M}^n$.

## Examples

**Example ($\mathbb{Z}$ and $\mathbb{Z}_p$).** On $\mathbb{Z}$ with the $(p)$-adic topology, the completion is $\varprojlim_n \mathbb{Z}/p^n\mathbb{Z} = \mathbb{Z}_p$, the ring of $p$-adic integers, and $\iota$ is the diagonal embedding; $\mathbb{Z}$ is Hausdorff and its completion is compact, because it is an inverse limit of finite rings.

**Example ($k[x]$ and $k[[x]]$).** On $k[x]$ with the $(x)$-adic topology, the completion is $\varprojlim_n k[x]/(x^n) = k[[x]]$, the ring of formal power series, and $\iota$ is the map sending a polynomial to its series.

**Example (a polynomial ring completed at the origin).** On $\mathbb{R}[x]$ with the $(x)$-adic topology the completion is $\mathbb{R}[[x]]$; the ideal $(x)$ is closed, its completion is the ideal of series with zero constant term, and the completion of the quotient $\mathbb{R} = \mathbb{R}[x]/(x)$ is the quotient of the completion by that ideal, by the quotient formula above.

**Example (a non-Hausdorff ring).** Let $R$ be a ring and give $R \times R$ the linear topology whose only proper open ideal is $0 \times R$, with the powers of the zero ideal in the second factor; then $\overline{\{0\}} = 0\times R$, the Hausdorff quotient is $R$, and the completion is $\widehat{R}$ computed from the first factor. The completion is blind to the closed ideal that the topology confuses with zero, which is the content of the kernel proposition.

## Summary

The completion of a topological ring with a linear topology and fundamental ideals $\{I_\lambda\}$ is the inverse limit $\widehat{R} = \varprojlim_\lambda R/I_\lambda$, a complete Hausdorff topological ring for its inverse limit topology, with a canonical continuous homomorphism $\iota_R : R \to \widehat{R}$ whose kernel is the closure of zero; the completion is injective exactly on Hausdorff rings and depends only on the Hausdorff quotient. A continuous homomorphism is uniformly continuous, so it induces a unique continuous homomorphism of the completions, and this assignment is functorial; the completion is therefore an endofunctor of the category of topological rings with linear topologies taking values in the complete Hausdorff rings. It is characterised by the universal property that every continuous homomorphism from $R$ to a complete Hausdorff ring factors uniquely through $\iota_R$, so that the completion is the reflection of the category into its complete Hausdorff subcategory, left adjoint to the inclusion.

The operator is idempotent, $\widehat{\widehat{R}} \cong \widehat{R}$, and the unit $\iota$ is an isomorphism exactly on the complete Hausdorff rings, so the completion is a projection of the category onto its complete Hausdorff part, which it fixes. It carries an ideal to an ideal of the completion and a quotient to the quotient of the completion, it is left exact and not generally right exact, being exact on finitely generated modules over a Noetherian ring by Artin–Rees. The standard instances are $\mathbb{Z}_p = \varprojlim \mathbb{Z}/p^n$ and $k[[x]] = \varprojlim k[x]/(x^n)$; a field has no nontrivial linear topology, and the nontrivial completion of a field is the valued completion, which is a different construction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $\widehat{R}$ | Topological ring with a linear topology, and its completion |
| $I_\lambda$ | Fundamental system of ideals of neighbourhoods of zero |
| $\varprojlim_\lambda R/I_\lambda$ | The completion as an inverse limit |
| $\iota_R$ | The canonical continuous homomorphism $R \to \widehat{R}$ |
| $\overline{\{0\}}$ | The closure of zero; the kernel of $\iota_R$ |
| $\widehat{f}$ | The continuous homomorphism of completions induced by a continuous $f$ |
| $\mathcal{C}$ | The category of complete Hausdorff topological rings |
| $\widehat{R/I} \cong \widehat{R}/\widehat{I}$ | The completion of a quotient |
| $\varprojlim^1$ | The obstruction to right exactness of the inverse limit |
| $\mathbb{Z}_p$, $k[[x]]$ | The standard completions of $\mathbb{Z}$ and $k[x]$ |

## Further Reading

- Nicolas Bourbaki, *General Topology, Chapters 1–4* (Springer, 1995), for the completion of a uniform space, the extension of uniformly continuous maps and the universal property.
- Nicolas Bourbaki, *Commutative Algebra, Chapters 1–7* (Springer, 1998), for the $I$-adic completion, its functoriality, its exactness and the Artin–Rees lemma.
- Michael Atiyah and Ian Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, 1969), for the $I$-adic topology, the Krull intersection theorem and the completion of a local ring.
- Hideyuki Matsumura, *Commutative Ring Theory* (Cambridge University Press, 1989), for the exactness properties of completion and the behaviour of ideals under it.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for the completion of topological rings for a linear topology and its universal property.
