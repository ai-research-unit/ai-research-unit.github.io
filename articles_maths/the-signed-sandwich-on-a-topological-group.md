
# __The Signed Sandwich on a Topological Group__

## Introduction

A two-sided operator on a topological group dresses an element between two factors, $x \mapsto axb$, and the sandwich is the operator so formed; when the group carries a continuous involutive automorphism $\alpha$, the element in the middle may be twisted by it before it is dressed, and the operator $x \mapsto a\,\alpha(x)\,b$ is the **signed sandwich**. The algebra of these operators is settled on an abstract group, and what the topology adds is exactly what the topology always adds to an operator layer: the sandwiches are homeomorphisms rather than mere bijections, the families they form are topological subgroups and cosets of $\operatorname{Homeo}(G)$, the parametrisation is a continuous map whose kernel is the anti-diagonal centre, and the fixed sets of the reflections are closed.

The article assumes the continuous involutive automorphism, the fixed set and the dictionary of the fixed and inverted sets from *Involutive Topological Groups*; the abstract signed sandwich, its factorisation $\Sigma^\alpha_{a,b} = \Sigma_{a,b}\alpha$, the composition laws, the coset $\mathfrak{S}^\alpha = \mathfrak{S}\alpha$ and the square of the signed conjugation from *The Signed Sandwich on a Group*; the translations and the operator layer from *Operators on a Topological Group*; and the local base at the identity, the uniformities and the compactness theorems from *Topological Groups*. The reflections read as operators, the correspondence with the elements that carry them and the degenerate cases are *Reflections as Signed Two-Sided Operators on a Topological Group*; the adjoint of the signed sandwich is *The Signed Adjoint Sandwich on a Topological Group*. Nothing analytic and nothing geometric is used.

Throughout, $G$ is a Hausdorff topological group with identity $e$, $\iota$ is the inversion, $\sigma$ is a topological involution, $\alpha = \sigma\iota$ is the associated **continuous involutive automorphism** — the grade involution — and $(G,\alpha)$ is a graded topological group. The fixed subgroup of $\alpha$ is $G^\alpha = \{x : \alpha(x) = x\}$ and the fixed set of $\sigma$ is $G^\sigma = I(\alpha)$, by the dictionary of *Involutive Topological Groups*.

## The Continuous Grade Involution

**Definition.** A **grade involution** of the topological group $G$ is a continuous automorphism $\alpha : G \to G$ with $\alpha^2 = \mathrm{id}$; the pair $(G,\alpha)$ is a **graded topological group**.

**Proposition.** The grade involution is a homeomorphism of $G$ of order two, so it conjugates $\operatorname{Homeo}(G)$ to itself and preserves every topological property of the group; it commutes with the inversion and with every topological involution of $G$ in the sense that $\iota\alpha = \alpha\iota$.

**Proof.** $\alpha$ is a continuous bijection with continuous inverse $\alpha$, hence a homeomorphism; a homeomorphism preserves open sets, compactness, connectedness and the uniformities. The inversion commutes with every homomorphism, so $\iota\alpha = \alpha\iota$.

**Proposition (the grade involution acts on the translations).** For all $a, b \in G$,

$$
\alpha\,L_a\,\alpha = L_{\alpha(a)}, \qquad \alpha\,R_b\,\alpha = R_{\alpha(b)} .
$$

**Proof.** $(\alpha L_a\alpha)(x) = \alpha(a\alpha(x)) = \alpha(a)x = L_{\alpha(a)}(x)$, and symmetrically for $R_b$.

So the grade involution is an automorphism of the operator layer: it conjugates each of the two translation subgroups onto itself, and it is a homeomorphism of the group.

## The Unsigned Sandwich

**Definition.** For $a, b \in G$ the **sandwich** by $(a,b)$ is

$$
\Sigma_{a,b} : G \longrightarrow G, \qquad \Sigma_{a,b}(x) = a\,x\,b .
$$

**Theorem (the sandwiche is a homeomorphism).** Each $\Sigma_{a,b}$ is a homeomorphism of $G$, with inverse $\Sigma_{a^{-1},b^{-1}}$, and the assignment $(a,b) \mapsto \Sigma_{a,b}$ is a continuous homomorphism

$$
\pi : G\times G \longrightarrow \operatorname{Homeo}(G), \qquad \pi(a,b) = L_aR_b ,
$$

onto the subgroup $\mathfrak{S} = \{\Sigma_{a,b}\}$ of $\operatorname{Homeo}(G)$, whose kernel is $\ker\pi = \{(z,z^{-1}) : z \in Z(G)\}$; hence $\mathfrak{S} \cong (G\times G)/Z(G)$ as an abstract group.

**Proof.** $\Sigma_{a,b} = L_aR_b$ is a composite of homeomorphisms, so it is a homeomorphism, and its inverse is $L_{a^{-1}}R_{b^{-1}} = \Sigma_{a^{-1},b^{-1}}$. The composition law $\Sigma_{a,b}\Sigma_{c,d} = \Sigma_{ac,db}$ and the kernel computation are those of *Operators on a Topological Group*; continuity of $\pi$ is the continuity of the action by translation and of the parametrisation in the compact-open topology.

**Corollary (closedness and compactness).** If $G$ is compact then $\pi$ is a homeomorphism onto its image and $\mathfrak{S}$ is a compact, hence closed, subgroup of $\operatorname{Homeo}(G)$; the same holds for a closed subgroup of $G$ with the induced topology. For locally compact $G$ the map $\pi$ is a continuous injection on $(G\times G)/Z(G)$, and $\mathfrak{S}$ is a subgroup of $\operatorname{Homeo}(G)$.

**Proof.** A compact group is locally compact, and for locally compact $G$ the compact-open topology on $\operatorname{Homeo}(G)$ is a group topology in which $(a,b)\mapsto L_aR_b$ is continuous; when $G$ is compact the domain $G\times G$ is compact, so the quotient $(G\times G)/Z(G)$ is compact, and a continuous bijection from a compact space onto a Hausdorff image is a homeomorphism, which makes the image compact and closed.

## The Signed Sandwich

**Definition.** Let $(G,\alpha)$ be a graded topological group. The **signed sandwich** by $(a,b)$ is

$$
\Sigma^{\alpha}_{a,b} : G \longrightarrow G, \qquad \Sigma^{\alpha}_{a,b}(x) = a\,\alpha(x)\,b .
$$

**Theorem (factorisation and continuity).** $\Sigma^{\alpha}_{a,b} = \Sigma_{a,b} \circ \alpha$, so every signed sandwich is a homeomorphism, with inverse $(\Sigma^{\alpha}_{a,b})^{-1} = \Sigma^{\alpha}_{\alpha(a)^{-1},\alpha(b)^{-1}} = \Sigma^{\alpha}_{a^{-1},b^{-1}}$ when $a,b$ are inverted by $\alpha$, and the signed sandwiches are the coset

$$
\mathfrak{S}^{\alpha} = \{\Sigma^{\alpha}_{a,b} : a,b\in G\} = \mathfrak{S}\,\alpha .
$$

**Proof.** $(\Sigma_{a,b}\circ\alpha)(x) = a\alpha(x)b$ is the definition; a composite of homeomorphisms is a homeomorphism, and the inverse is computed by solving $a\alpha(x)b = y$, which gives $x = \alpha(a^{-1}yb^{-1}) = \alpha(a)^{-1}\alpha(y)\alpha(b)^{-1}$ because $\alpha$ is an automorphism. The coset statement is the abstract one, and it is an identity of maps, so it survives the passage to $\operatorname{Homeo}(G)$.

**Proposition (the composition laws).** For all $a,b,c,d \in G$,

$$
\Sigma^{\alpha}_{a,b}\circ\Sigma^{\alpha}_{c,d} = \Sigma_{a\alpha(c),\,\alpha(d)b}, \qquad
\Sigma_{a,b}\circ\Sigma^{\alpha}_{c,d} = \Sigma^{\alpha}_{ac,\,db}, \qquad
\Sigma^{\alpha}_{a,b}\circ\Sigma_{c,d} = \Sigma^{\alpha}_{a\alpha(c),\,\alpha(d)b} .
$$

**Proof.** The computations are those of *The Signed Sandwich on a Group*; each is performed by inserting $\alpha^2 = \mathrm{id}$ into the middle factor, and the continuity of the operators is already established.

**Corollary.** A product of two signed sandwiches is an unsigned sandwich, a product of an unsigned and a signed sandwich is signed, and the group generated by $\mathfrak{S}$ and $\alpha$ inside $\operatorname{Homeo}(G)$ is $\mathfrak{S} \sqcup \mathfrak{S}\alpha$, of order $2\lvert\mathfrak{S}\rvert$ when $\alpha \notin \mathfrak{S}$ and equal to $\mathfrak{S}$ otherwise. Moreover $\alpha \in \mathfrak{S}$ exactly when $\alpha$ is an inner automorphism.

**Proof.** The coset identity $\mathfrak{S}^\alpha = \mathfrak{S}\alpha$ and the parity of the product are abstract; the last statement is *The Signed Sandwich on a Group*. The point here is that both families lie in $\operatorname{Homeo}(G)$, so the generated object is a group of homeomorphisms.

**Corollary (degeneracy).** If $\alpha$ is inner then the signed sandwiches are exactly the unsigned ones and the operator adds nothing; the signed family is a genuinely new coset exactly when $\alpha$ is not inner. In particular the signed sandwich collapses to the unsigned one on an abelian group, where every continuous involutive automorphism is either the identity or the inversion, and every such automorphism is inner.

**Proof.** This is the abstract degeneracy, retained verbatim; the topological statement adds only that inner automorphisms are continuous.

## The Reflections it Realises

**Definition.** For $a \in G$ the **signed conjugation** by $a$ is the signed sandwich with $b = a^{-1}$,

$$
\rho_a := \Sigma^{\alpha}_{a,\,a^{-1}} : G \longrightarrow G, \qquad \rho_a(x) = a\,\alpha(x)\,a^{-1} .
$$

**Proposition (its square).** $\rho_a$ is the continuous automorphism $c_a\alpha$, and

$$
\rho_a^2 = c_{a\alpha(a)} = \Sigma_{a\alpha(a),\,(a\alpha(a))^{-1}} ,
$$

so $\rho_a$ is an involution of the set $G$ exactly when $a\alpha(a) \in Z(G)$.

**Proof.** $\rho_a = c_a\circ\alpha$ is a composite of continuous automorphisms, hence a continuous automorphism; the square is the abstract computation of *The Signed Sandwich on a Group*, and an inner conjugation is the identity exactly on the central elements.

**Definition.** A **reflection** of the graded topological group $(G,\alpha)$ is a signed conjugation that is an involution, $\rho_a^2 = \mathrm{id}$, equivalently $a\alpha(a) \in Z(G)$.

**Theorem (the reflections are topological involutions).** A reflection $\rho_a$ is a continuous involutive automorphism of $G$; its fixed set

$$
\operatorname{Fix}(a) = \{x \in G : \alpha(x) = a^{-1}xa\}
$$

is closed, it is a subgroup of $G$ containing $e$, and it is a coset of the fixed subgroup $G^\alpha$ when it is nonempty. Every element of the inverted subgroup $I(\sigma) = G^\alpha$ carries a reflection automatically.

**Proof.** A reflection is a homeomorphism of order two, hence a topological involution in the sense of *Involutive Topological Groups*, and its fixed set is closed, being the equalizer of the continuous maps $\alpha$ and $c_{a^{-1}}$. That the fixed set is a subgroup and a coset of $G^\alpha$ is the abstract statement of *Reflections as Signed Two-Sided Operators on a Group*; the closedness is the new ingredient and it is the general theorem on continuous involutions. For $a \in I(\sigma) = G^\alpha$, the dictionary gives $\alpha(a) = a^{-1}$, so $a\alpha(a) = e$ is central and $\rho_a$ is an involution.

**Corollary (the reflections are closed under composition).** The reflections generate a subgroup of $\operatorname{Homeo}(G)$ contained in $\operatorname{Aut}_c(G)$, and the set of reflections that are carried by the elements $a$ with $a\alpha(a)$ central is the union of the cosets $aZ(G)$ for those $a$.

**Proof.** Each reflection is a continuous automorphism, so products are continuous automorphisms; the coset description of the carrying elements is the abstract statement that $\rho_a = \rho_{a'}$ exactly when $a' \in aZ(G)$.

## Summary

A graded topological group is a topological group with a continuous involutive automorphism $\alpha$, the grade involution, which is a homeomorphism and acts on the translations by $\alpha L_a\alpha = L_{\alpha(a)}$ and $\alpha R_b\alpha = R_{\alpha(b)}$. The unsigned sandwich $\Sigma_{a,b}(x) = axb$ is a homeomorphism, the map $(a,b)\mapsto\Sigma_{a,b} = L_aR_b$ is a continuous homomorphism onto a subgroup $\mathfrak{S}$ of $\operatorname{Homeo}(G)$ with kernel the anti-diagonal centre, and $\mathfrak{S}$ is compact and closed when $G$ is compact. The signed sandwich $\Sigma^\alpha_{a,b}(x) = a\alpha(x)b$ is the composite $\Sigma_{a,b}\alpha$, hence a homeomorphism, and the signed sandwiches form the coset $\mathfrak{S}^\alpha = \mathfrak{S}\alpha$; they coincide with the unsigned ones exactly when the grade involution is inner, and they collapse on an abelian group. The signed conjugation $\rho_a(x) = a\alpha(x)a^{-1}$ is the continuous automorphism $c_a\alpha$ whose square is the inner conjugation by $a\alpha(a)$, so it is a **reflection**, an involution of the topological group, exactly when $a\alpha(a)$ is central; its fixed set is closed, a subgroup, and a coset of $G^\alpha$ when nonempty, and every element of the inverted subgroup $G^\alpha$ carries a reflection automatically. The degeneracies are the three abstract ones — inner $\alpha$, abelian $G$, and non-central $a\alpha(a)$ — and the topology changes none of them; it adds the closedness of the fixed sets and the topological nature of the operator families.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$ | the grade involution, a continuous involutive automorphism of $G$ |
| $\alpha L_a\alpha = L_{\alpha(a)}$, $\alpha R_b\alpha = R_{\alpha(b)}$ | the action of $\alpha$ on the translations |
| $\Sigma_{a,b}(x) = axb$ | the unsigned sandwich, a homeomorphism |
| $\pi(a,b) = L_aR_b$ | its parametrisation, continuous with kernel the anti-diagonal centre |
| $\mathfrak{S} = \{\Sigma_{a,b}\}$ | the subgroup of $\operatorname{Homeo}(G)$ of unsigned sandwiches |
| $\Sigma^{\alpha}_{a,b}(x) = a\alpha(x)b$ | the signed sandwich, $= \Sigma_{a,b}\alpha$ |
| $\Sigma^{\alpha}_{a,b}\Sigma^{\alpha}_{c,d} = \Sigma_{a\alpha(c),\alpha(d)b}$ | the product of two signed sandwiches |
| $\mathfrak{S}^{\alpha} = \mathfrak{S}\alpha$ | the signed sandwiches as a coset |
| $\alpha \in \mathfrak{S} \iff \alpha$ inner | degeneracy of the signed family |
| $\rho_a = \Sigma^{\alpha}_{a,a^{-1}}(x) = a\alpha(x)a^{-1}$ | the signed conjugation |
| $\rho_a^2 = c_{a\alpha(a)}$ | its square; a reflection iff $a\alpha(a) \in Z(G)$ |
| $\operatorname{Fix}(a) = \{x : \alpha(x) = a^{-1}xa\}$ | the fixed set of $\rho_a$, closed |
| $G^\alpha = I(\sigma)$ | the fixed subgroup of $\alpha$, the inverted subgroup of $\sigma$ |

## Further Reading

- Lev S. Pontryagin, *Topological Groups* (Gordon and Breach, second edition, 1966), for the continuous automorphisms and the compact-open topology on the group of homeomorphisms.
- Karl H. Hofmann and Sidney A. Morris, *The Structure of Compact Groups* (De Gruyter, third edition, 2013), for the group of continuous automorphisms of a compact group and the conjugation action.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutive automorphisms and the operators built from them.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the sandwich action and the reflections it generates.
- Alexander Arhangel'skii and Mikhail Tkachenko, *Topological Groups and Related Structures* (Atlantis Press, 2008), for the compact-open topology on $\operatorname{Homeo}(G)$ and the topological automorphism group.
