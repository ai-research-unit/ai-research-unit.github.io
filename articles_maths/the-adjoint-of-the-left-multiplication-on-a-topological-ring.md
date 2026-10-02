
# __The Adjoint of the Left Multiplication on a Topological Ring__

## Introduction

The left multiplication $L_a$ is the archetype of the operators of a ring, and its adjoint with respect to the form of the category is again a left multiplication, that by the image of $a$ under the involution: $(L_a)^\dagger = L_{\sigma(a)}$. The formula carries three things at once: the explicit expression of the adjoint, the compatibility of the adjoint with the involution, and the fact that the left regular representation is a `*`-representation. From it follow the self-adjointness, the skewness, the unitarity and the involutivity of the left multiplication, each read off from the corresponding property of the element, and the adjoints of the right multiplication and of the unsigned sandwich. This article computes the adjoint of the left multiplication, proves the compatibility with the involution, derives the dictionary between the properties of the operator and the properties of the element, and reads the whole thing through the topology, where the adjoint is continuous and the adjointable operators form a closed subalgebra.

The article assumes the topological ring and the bounded and continuous operators from *Topological Rings and Fields* and *Operators on a Topological Ring*; the left and right multiplications from *The Left and Right Multiplication Operators on a Topological Ring*; the operator adjoint, the form of the category and the left regular representation from *The Involution on Bounded Operators of a Ring*; the continuous involution, the fixed and skew sets and the closedness of the fixed set from *Involutive Topological Rings and Fields*; and the self-adjoint, skew, unitary and inverted elements from *Involutive Topological Division Rings*. The adjoints under the residue pairing and under the Hermitian valuation are *Adjoints under the Residue Pairing* and *The Adjoint under a Hermitian Valuation*; the signed versions are the three articles that follow.

Throughout, $R$ is a Hausdorff topological ring with a continuous involution $\sigma$, a continuous $\sigma$-invariant trace $\tau$ and the **form of the category** $\{x,y\} = \tau(x\sigma(y))$; $L_a(x) = ax$ and $R_b(x) = xb$ are the multiplications; the unsigned sandwich is $\Sigma_{a,b} = L_aR_b$; and the adjoint $T^\dagger$ is defined by $\{Tx,y\} = \{x,T^\dagger y\}$.

## The Adjoint of the Left Multiplication

**Theorem (the explicit form).** For every $a\in R$ the left multiplication is adjointable and

$$
(L_a)^\dagger = L_{\sigma(a)} , \qquad (R_b)^\dagger = R_{\sigma(b)} .
$$

Hence the adjoint of a left multiplication is the left multiplication by the image of $a$ under the involution, and the adjoint of a right multiplication is the right multiplication by the image of $b$.

**Proof.** For all $x,y$, $\{L_ax,y\} = \tau(ax\sigma(y)) = \tau(x\sigma(y)a)$, by the cyclic invariance of the trace; and $\tau(x\sigma(y)a) = \tau(x\sigma(\sigma(a)y)) = \{x,L_{\sigma(a)}y\}$, by $\sigma^2 = \mathrm{id}$. Hence $L_{\sigma(a)}$ satisfies the defining identity, and it is the adjoint by the nondegeneracy of the form. The right-handed computation is the mirror image.

**Corollary (compatibility with the involution and the `*`-representation).** The adjoint intertwines the left multiplication with the involution, $(L_a)^\dagger = L_{a^\sigma}$ with $a^\sigma = \sigma(a)$, and the left regular representation $a\mapsto L_a$ is a `*`-representation of $(R,\sigma)$ in the involutive operator algebra; equivalently, $(L_a)^\dagger = L_a\circ\sigma$ read on the parameter and $(L_{\sigma(a)})^\dagger = L_a$.

**Proof.** The formula is the theorem; the `*`-representation statement is *The Involution on Bounded Operators of a Ring*, and the last identity is the theorem applied twice, $(L_{\sigma(a)})^\dagger = L_{\sigma^2(a)} = L_a$.

**Corollary (the unsigned sandwich).** The unsigned sandwich $\Sigma_{a,b}(x) = axb$ is adjointable with

$$
(\Sigma_{a,b})^\dagger = \Sigma_{\sigma(a),\sigma(b)} ,
$$

the sandwich of the images, with the order of the parameters restored rather than reversed.

**Proof.** $\Sigma_{a,b} = L_aR_b$, so $(\Sigma_{a,b})^\dagger = R_b{}^\dagger L_a{}^\dagger = R_{\sigma(b)}L_{\sigma(a)} = \Sigma_{\sigma(a),\sigma(b)}$ by the anti-multiplicativity of the adjoint.

## The Dictionary between the Operator and the Element

**Theorem (self-adjointness and skewness).** The left multiplication satisfies

$$
L_a^\dagger = L_a \iff \sigma(a) = a , \qquad L_a^\dagger = -L_a \iff \sigma(a) = -a ,
$$

so the self-adjoint left multiplications are exactly those by the self-adjoint elements, and the skew ones exactly those by the skew elements.

**Proof.** $L_a^\dagger = L_{\sigma(a)}$ and $L$ is injective on a ring with unit, so $L_{\sigma(a)} = \pm L_a$ iff $\sigma(a) = \pm a$.

**Theorem (unitarity and involutivity).** The left multiplication satisfies

$$
L_a^\dagger L_a = \mathrm{id} \iff \sigma(a)a = 1 , \qquad L_aL_a^\dagger = \mathrm{id} \iff a\sigma(a) = 1 , \qquad L_a^2 = \mathrm{id} \iff a^2 = 1 ,
$$

so the left multiplication is unitary, $L_a^\dagger L_a = L_aL_a^\dagger = \mathrm{id}$, exactly when $a$ is unitary in the two-sided sense; it is normal, $L_a^\dagger L_a = L_aL_a^\dagger$, exactly when $a$ commutes with $\sigma(a)$.

**Proof.** $L_a^\dagger L_a = L_{\sigma(a)}L_a = L_{\sigma(a)a}$, and $L_c = \mathrm{id}$ iff $c = 1$, since $cx = x$ for all $x$ with $x = 1$ gives $c = 1$; hence the left unitarity is $\sigma(a)a = 1$, and the right unitarity is the mirror statement $a\sigma(a) = 1$. Involutivity is $L_a^2 = L_{a^2}$. Normality is $L_{\sigma(a)a} = L_{a\sigma(a)}$, that is $\sigma(a)a = a\sigma(a)$.

**Remark (the three sets).** The self-adjoint left multiplications form the image of the self-adjoint elements, a closed additive family; the unitary left multiplications form the image of the unitary elements, a subgroup; the involutive left multiplications form the image of the elements of order two, a set closed under nothing in particular; and the three coincide only on the intersection, the unitary elements of order two that are self-adjoint, where the self-adjoint unitary elements of order two are the orthogonal involutions of the ring.

## The Derivation $ad_a$ and the Trace Form

**Proposition (the derivation and its adjoint).** The map $ad_a = L_a - R_a$ is a continuous derivation of $R$, $ad_a(xy) = ad_a(x)y + x\,ad_a(y)$, and its adjoint with respect to the form of the category is $ad_a^\dagger = ad_{\sigma(a)}$; hence $ad_a$ is self-adjoint exactly when $\sigma(a) - a$ is central and skew exactly when $\sigma(a) + a$ is central, and the inner derivations form a closed $\sigma$-stable subspace of the bounded operators.

**Proof.** $ad_a = L_a - R_a$ is a derivation by the Leibniz rule for the two multiplications; its adjoint is $L_{\sigma(a)} - R_{\sigma(a)} = ad_{\sigma(a)}$ by the two adjoint formulas; $ad_c = 0$ exactly when $c$ is central, since $cx - xc = 0$ for all $x$ is centrality. The trace of the derivation vanishes, $\tau(ad_a x) = \tau(ax - xa) = 0$, by the cyclicity of the trace, so every inner derivation is a skew-map for the invariant trace.

## Topological Compatibility

**Theorem (continuity and closedness).** If the multiplication of $R$ is continuous then every left multiplication is bounded and continuous, the adjoint map $T\mapsto T^\dagger$ is continuous on the adjointable operators in the topology of bounded convergence, and the self-adjoint left multiplications form a closed subset of the operator algebra; the set of $a$ with $L_a$ self-adjoint is closed, namely the self-adjoint elements of $R$.

**Proof.** Continuity of $L_a$ is the continuity of the product and boundedness is that a fixed factor carries bounded sets to bounded sets; the continuity of the adjoint is *The Involution on Bounded Operators of a Ring*; the self-adjoint elements are closed by *Involutive Topological Rings and Fields*, and their image under the continuous injective map $a\mapsto L_a$ is closed in the image.

**Corollary (the completion).** The adjoint of the left multiplication of the completion is the left multiplication by the image under the extended involution, and the dictionary of operator and element properties is preserved by the passage to the completion, by *The Involution and the Completion of a Ring*.

**Proof.** The completion carries the extended continuous involution and the extended trace, the form is the completed form, and the adjoint is computed by the same cyclicity; the properties of the element that are the conditions of the dictionary are preserved by closure.

## Ideals, the Dual and the Division Case

**Proposition (the action on the ideals).** The left multiplication carries a left ideal into itself, $L_a(I) = aI\subseteq I$ for a left ideal $I$, and a two-sided ideal into itself; the adjoint acts on the annihilator by $L_a^\dagger(\mathrm{Ann}(I))\subseteq \mathrm{Ann}(I)$ when $I$ is $\sigma$-invariant, and a form-preserving operator carries the lattice of $\sigma$-invariant two-sided ideals into itself.

**Proof.** $a I\subseteq I$ for a left ideal, and $aI\subseteq I$ on both sides for a two-sided ideal; the annihilator statement is the transpose of the inclusion, and a form-preserving operator with its adjoint preserves the ideals by the two inclusions.

**Theorem (the division case).** If $R$ is a division ring, every nonzero element is a unit, so every nonzero left multiplication is invertible with $L_a^{-1} = L_{a^{-1}}$ and the dictionary of *The Involution on Bounded Operators of a Ring* is complete: the self-adjoint left multiplications are exactly the left multiplications by the self-adjoint elements, the unitary ones exactly those by the unitary elements, and the involutive ones exactly those by the elements of order two.

**Proof.** A division ring has no nonzero nonunits, so $L_a$ for $a\ne0$ is invertible; the dictionary is the general theorem, with the kernel of the parametrisation trivial, and the three sets are the images of the three sets of elements.

**Remark (the dual).** On the algebraic dual $R^*$ the transpose of $L_a$ is $L_a^{\mathrm t}(\varphi) = \varphi\circ L_a$, so the adjoint under the form and the transpose on the dual are the two faces of the same operation; the transpose acts by the right multiplication on the dual when the dual is identified with $R$ through the form, which is the reason the adjoint of the left multiplication under the residue pairing is a right multiplication.

## Examples

**Example (the matrix algebra).** $R = M_n(F)$ with the transpose and the trace form; $(L_X)^\dagger = L_{X^{\mathrm t}}$, the self-adjoint left multiplications are the left multiplications by symmetric matrices, and the unitary ones by the orthogonal matrices.

**Example (a field with the identity involution).** $(L_a)^\dagger = L_a$ for every $a$, the form is symmetric, and every left multiplication is self-adjoint; the operator involution is the identity and the `*`-representation is the ordinary left regular representation.

**Example (a group algebra).** For $k[G]$ with the form $B(u,v) = \sum_g u_gv_{\sigma(g)}$, the adjoint of $L_a$ is $L_{\sigma(a)}$, recovering the adjoint of the left multiplication on a topological group when the group is discrete.

**Example (the residue pairing).** Under the residue pairing of *Adjoints under the Residue Pairing* the adjoint of $L_a$ is the right multiplication $R_{\sigma(a)}$; this is the article of the category in which the form is not the category form, and it shows that the compatibility of the adjoint with the involution is the compatibility with the specific form, not with the ring alone.

## Summary

The adjoint of the left multiplication of a topological ring with respect to the form of the category is the left multiplication by the image of the element under the involution, $(L_a)^\dagger = L_{\sigma(a)}$, and the adjoint of the right multiplication is $(R_b)^\dagger = R_{\sigma(b)}$; the adjoint therefore intertwines the multiplication with the involution and makes the left regular representation a `*`-representation. The adjoint of the unsigned sandwich is $\Sigma_{\sigma(a),\sigma(b)}$. The inner derivation $ad_a = L_a - R_a$ has adjoint $ad_{\sigma(a)}$, so it is self-adjoint exactly when $\sigma(a) - a$ is central and skew exactly when $\sigma(a) + a$ is central, and its trace vanishes; the inner derivations form a closed $\sigma$-stable subspace. The dictionary between operator and element is exact: the left multiplication is self-adjoint exactly for the self-adjoint elements, skew for the skew elements, unitary for the unitary elements with central norm, involutive for the elements of order two, and normal exactly for the elements commuting with their image under the involution. Topologically the left multiplications are bounded and continuous, the adjoint map is continuous in the topology of bounded convergence, the self-adjoint elements are closed, and the whole dictionary passes to the completion. Under a different form — the residue pairing — the adjoint of the left multiplication is a right multiplication, which shows that the adjoint depends on the form even when the involution is fixed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $\sigma$, $\tau$, $\{x,y\}$ | Ring, involution, trace, form of the category |
| $L_a(x) = ax$, $R_b(x) = xb$ | Left and right multiplications |
| $(L_a)^\dagger = L_{\sigma(a)}$ | The adjoint of the left multiplication |
| $(R_b)^\dagger = R_{\sigma(b)}$ | The adjoint of the right multiplication |
| $\Sigma_{a,b} = L_aR_b$ | The unsigned sandwich |
| $(\Sigma_{a,b})^\dagger = \Sigma_{\sigma(a),\sigma(b)}$ | Its adjoint |
| $L_a^\dagger = L_a \iff \sigma(a) = a$ | Self-adjoint left multiplications |
| $L_a^\dagger L_a = \mathrm{id} \iff \sigma(a)a = 1$ | Left-unitary left multiplications |
| $L_a^2 = \mathrm{id} \iff a^2 = 1$ | Involutive left multiplications |
| $ad_a = L_a - R_a$ | The inner derivation, $ad_a^\dagger = ad_{\sigma(a)}$ |
| $\sigma(a) - a$ central | $ad_a$ self-adjoint |
| $\sigma(a) + a$ central | $ad_a$ skew |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the regular representation of a ring with involution and its symmetric elements.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the left and right multiplications and their ideals.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for the adjoint under a sesquilinear form and the `*`-representation.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for the continuous operators of a topological ring and the topology of bounded convergence.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the operator adjoint, self-adjointness and normality.
