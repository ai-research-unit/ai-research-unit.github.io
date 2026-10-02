# __Equivariant Operators and the Transfer__

## Introduction

An operator on a space with a group action is equivariant when it commutes with the action, and the equivariant operators form the fixed part of the algebra of all operators under the conjugation by the group: the fixed part of $\operatorname{End}(M)$ for a representation $M$ of $G$ is the algebra $\operatorname{End}_G(M)$ of the intertwining operators. On this fixed part the group produces two further operators, which are the subject of the article: the **norm** $N = \sum_{g}\rho(g)$, whose average over the group is the projection onto the fixed vectors when the order of the group is invertible, and the **transfer** $\mathrm{tr}$ attached to a subgroup $H\leq G$, which moves classes up from $H$ to $G$ and is adjoint to the **restriction** under the evaluation pairing. The adjointness — **Frobenius reciprocity** for the induction and the restriction, in the form $\langle \mathrm{tr}\,\alpha,\beta\rangle = \langle\alpha,\mathrm{res}\,\beta\rangle$ — together with the two compositions $\mathrm{res}\,\mathrm{tr} = [G:H]$ and $\mathrm{tr}\,\mathrm{res} = N_H$, is the operator content of the group action, and the **fixed part** is its spectral resolution: the fixed part of an operator algebra is the algebra of the operators the group does not move, and the transfer is the operator that selects it.

The article develops the equivariant operators and the transfer. It defines the operators of the action and their fixed part, the norm and its idempotent average, the restriction and the transfer attached to a subgroup, proves the adjointness relation and computes the two composites, identifies the fixed part of the operator algebra with the intertwining operators, states Shapiro's lemma as the equivariant form of the adjunction, and closes with the examples of the group algebra, the free action and the fixed action. The group action, the fixed-point functors and the orbit category are those of *Equivariant Homotopy Theory*; the equivariant cohomology and the transfer in the Borel model are those of *Equivariant Cohomology* and *The Transfer and the Involution*; the module and pairing conventions, the evaluation pairing and the adjoint of an operator are those of *The Operators on an Algebra* and *Dual Spaces and the Adjoint Operator*; and the invariants and the coinvariants are those of *Group Cohomology* and *Classifying Spaces and Cohomology Operations*. Nothing analytic and nothing geometric is used.

Throughout, $G$ is a finite group acting on abelian groups, modules or cochain complexes, and $M$ is a $G$-module with the action written $\rho : G\to\operatorname{Aut}(M)$; the **fixed part** is $M^G = \{m : \rho(g)m = m \ \forall g\}$ and the **coinvariants** are $M_G = M/\langle \rho(g)m - m\rangle$. For a subgroup $H\leq G$ the **restriction** is $\mathrm{res}_H^G : M^G\to M^H$ (and more generally $\mathrm{res} : M\to \mathrm{Res}_H^G M$), the **transfer** is $\mathrm{tr}_H^G : M^H\to M^G$, and the **norm** is $N_H = \sum_{h\in H}\rho(h)$, acting on $M$. When $G$ acts on a space $X$, the same operators act on the cohomology $H^*(X;k)$ with $\rho(g) = (g^{-1})^*$, and the **equivariant operators** are the elements of $\operatorname{End}(H^*(X;k))^G$, the operators commuting with the action. The evaluation pairing is $\langle\cdot,\cdot\rangle$ and the coefficient field is $k$, of characteristic not dividing $|G|$ when an average is taken.

## The Operators of the Action

### The Action Operators and Their Fixed Part

**Definition.** For a finite group $G$ acting on a module $M$, the **action operators** are the automorphisms $\rho(g) \in \operatorname{Aut}(M)$, and an operator $T \in \operatorname{End}(M)$ is **equivariant** when it commutes with all of them, $T\rho(g) = \rho(g)T$ for every $g$; the **fixed part of the operator algebra** is

$$
\operatorname{End}(M)^G = \{T : \rho(g)T\rho(g)^{-1} = T \ \forall g\} = \operatorname{End}_G(M),
$$

the algebra of the intertwining operators, under the conjugation action of $G$ on $\operatorname{End}(M)$.

**Theorem.** The fixed part of the operator algebra is the algebra of the $G$-module endomorphisms of $M$: it is a subalgebra of $\operatorname{End}(M)$, closed under composition and under the adjoint when $M$ is a Hilbert space or a module with a compatible duality, and it is an invariant of the representation up to isomorphism. The whole operator algebra is a $G$-module under the conjugation, with fixed part exactly $\operatorname{End}_G(M)$, and the inclusion of the fixed part as the invariant subalgebra is the operator form of taking invariants.

*Proof.* An operator commutes with all $\rho(g)$ exactly when it lies in the fixed part of the conjugation action; a composition of two such operators commutes with all $\rho(g)$, and the adjoint commutes with the action when the pairing is invariant, so the fixed part is a subalgebra closed under the adjoint. $\square$

### The Norm and the Average

**Definition.** The **norm** of the action is the operator

$$
N = \sum_{g\in G}\rho(g) \in \operatorname{End}(M),
$$

and, when $|G|$ is invertible in $k$, the **average** is $\bar{N} = |G|^{-1}N$.

**Theorem.** The norm is equivariant, $N\in\operatorname{End}_G(M)$, and it satisfies $N^2 = |G|\,N$, so the average is an idempotent: $\bar{N}^2=\bar{N}$. When $|G|$ is invertible in $k$ the idempotent $\bar{N}$ is the projection onto the fixed part, $\bar{N}M = M^G$, with kernel the coinvariants $\ker\bar{N} = \langle\rho(g)m - m\rangle$, and the module splits as $M = M^G\oplus \langle\rho(g)m-m\rangle$ on which $\bar{N}$ is the projection and its complement.

*Proof.* The norm commutes with every $\rho(h)$ because right multiplication by $h$ permutes the sum; and $N^2 = \sum_{g,h}\rho(gh) = |G|\sum_{g'}\rho(g') = |G|N$; an idempotent $|G|^{-1}N$ has image the vectors with $\rho(g)m=m$ for all $g$, that is the fixed part, and its kernel is the augmenting ideal, that is the coinvariants. $\square$

So the operator content of the action begins with the norm, whose average is the projection onto the fixed part: the fixed part is the image of an operator built from the action.

## The Transfer and the Restriction

### The Restriction and the Corestriction

**Definition.** For a subgroup $H\leq G$ the **restriction** is the inclusion of fixed parts

$$
r = \mathrm{res}_H^G : M^G \hookrightarrow M^H ,
$$

and the **transfer** (corestriction) is the operator

$$
t = \mathrm{cor}_H^G : M^H \longrightarrow M^G , \qquad t(x) = \sum_{g\in G/H}\rho(g)x ,
$$

the sum over a set of coset representatives of $H$ in $G$; the summands depend only on the coset because $x$ is $H$-fixed, and the sum is $G$-fixed, so the operator is well defined and independent of the choice of the representatives.

**Theorem.** The restriction and the transfer satisfy the composition identities

$$
r\circ t = [G:H]\,\mathrm{id}_{M^H}, \qquad t\circ r = [G:H]\,\mathrm{id}_{M^G}, \qquad N_G = t\circ N_H ,
$$

where $[G:H]$ is the index and $N_G=\sum_{g\in G}\rho(g)$, $N_H=\sum_{h\in H}\rho(h)$ are the norms; the norm of the subgroup acts on the fixed part $M^H$ by the scalar $|H|$. For $H=1$ the transfer is the norm $N_G$ and for $H=G$ the restriction is the identity and the transfer is the identity.

*Proof.* The sum over the cosets is invariant under replacing the representatives by another set, because a changed summand is replaced by an equal one by the $H$-fixity of $x$ and the $G$-fixity of the sum, which also proves that $t$ lands in $M^G$: $\rho(h)\sum_{\bar g}\rho(g)x=\sum_{\bar g}\rho(hg)x=\sum_{\bar g}\rho(g)x$ for $h\in H$ extended over the cosets. The first composition counts one copy of $x$ per coset and the second one copy of $m$ per coset because $m$ is fixed, giving the index in both; and $t\circ N_H$ sums $\rho(g)\rho(h)$ over the cosets and over $H$, which is the sum over all of $G$. $\square$

### Frobenius Adjointness

**Theorem (adjointness).** Under the evaluation pairing the transfer is the adjoint of the restriction,

$$
\langle t\,\alpha , \beta \rangle = \langle \alpha , r\,\beta \rangle , \qquad \alpha \in M^H,\ \beta \in (M^G)^* ,
$$

and in the cohomology of the group, with $r=\mathrm{res}_H^G : H^*(G;M)\to H^*(H;M)$ and $t=\mathrm{cor}_H^G : H^*(H;M)\to H^*(G;M)$,

$$
r\circ t = [G:H]\,\mathrm{id}, \qquad t\circ r = \sum_{g\in G/H}g^* , \qquad \langle t\,\alpha,\beta\rangle=\langle\alpha,r\,\beta\rangle ,
$$

the last identity being **Frobenius reciprocity**; for $H=1$ the transfer is the norm $N_G=\sum_{g\in G}g^*$ and $t\circ r = N_G$. The restriction is the transpose of the transfer under the pairing, and the pair is adjoint in the additive category of the $G$-modules, so that the transfer is both the left and the right adjoint of the restriction.

*Proof.* The pairing is the evaluation of a functional on a vector, and the identity is the verification $\langle\sum_{\bar g}\rho(g)\alpha,\beta\rangle=\langle\alpha,\sum_{\bar g}\rho(g)^*\beta\rangle$ with $\beta$ restricted to the invariants of the whole group; the composite $t\circ r$ is the sum of the conjugates $g^*$ over the cosets, which for $H=1$ is the norm, and $r\circ t$ is the index because each coset contributes one copy. $\square$

**Corollary.** The transfer is an operator of degree zero, it lands in the fixed part, and it is natural for morphisms of the representation and for the equivariant maps; its composite with the restriction is the index on the fixed part and the coset-sum of the conjugates in general, and the fixed part of the whole group receives the $N_H$-sums of the fixed part of the subgroup through the identity $N_G=t\circ N_H$.

*Proof.* The transfer lands in $M^G$ because the sum is invariant; the naturality is the naturality of the sum; the composites are the theorem and the identity $N_G=t\circ N_H$. $\square$

## Shapiro's Lemma and the Equivariant Adjointness

### The Statement

**Theorem (Shapiro's lemma).** For a subgroup $H\leq G$, a $G$-module $M$ and its restriction to $H$, there is a natural isomorphism

$$
H^*(G; \mathrm{Ind}_H^G N) \cong H^*(H;N), \qquad H^*_G(G/H \times Z; \underline M) \cong H^*_H(Z;\underline M),
$$

the cohomology of the induced module is the cohomology of the subgroup, and the same with the Bredon cohomology of the orbit $G/H$ and of the coefficient system restricted to $H$: the induction and the restriction form an adjoint pair on the cohomology.

*Proof.* The tensor identity $\mathrm{Ind}_H^G N = k[G]\otimes_{k[H]}N$ with the induction, and the standard resolution of the induced module; the equivariant form is the identification of the $G$-cells of the orbit $G/H\times Z$ with the $H$-cells of $Z$, which is the same computation in the equivariant setting. $\square$

### The Equivariant Transfer

**Theorem.** In the equivariant cohomology the transfer of a subgroup is the operator

$$
\mathrm{tr}_H^G : H^*_H(X;\underline{M}) \longrightarrow H^*_G(X;\underline{M}) , \qquad \mathrm{tr}_H^G = \sum_{g\in G/H}(g^{-1})^* ,
$$

well defined on the $H$-equivariant cohomology; it is adjoint to the restriction $\mathrm{res}_H^G : H^*_G(X;\underline M)\to H^*_H(X;\underline M)$ under the evaluation pairing, and the two composites are $r\circ t=[G:H]$ and $t\circ r=\sum_{g\in G/H}g^*$ as before; for the trivial subgroup the transfer is the norm $N_G$. The transfer is the equivariant operator of the induction, and it is the operator form of the induction isomorphism of Shapiro's lemma.

*Proof.* The transfer is the sum of the action operators over the cosets composed with the identification of the $H$-fixed part; the adjointness and the composites are the identities of the previous sections applied to the cochain complex, and the identification with Shapiro's lemma is the naturality of the isomorphism. $\square$

## The Fixed Part of the Operator Algebra

### The Operators Commuting with the Action

**Theorem.** The fixed part of the operator algebra on the cohomology,

$$
\operatorname{End}(H^*(X;k))^G = \{T : g^*T = Tg^* \ \forall g\},
$$

consists of the operators commuting with the induced action, and it is the algebra in which the natural operators of the equivariant theory live: the transfer, the restriction, the norms and the equivariant multiplications are all in it, while the operators that do not commute with the action, such as a single multiplication by a non-invariant class or a single $\rho(g)$ for $g\neq1$, lie outside. The fixed part is therefore the algebra of the **equivariant operators**, and the transfer is its canonical non-scalar element.

*Proof.* The condition $g^*T=Tg^*$ for all $g$ is the definition of the fixed part; the listed operators satisfy it, the transfer because it is a sum of the $g^*$ with the restriction, and the multiplications by invariant classes because the action is a ring automorphism; the operators outside are those moved by some $g^*$, by the definition. $\square$

### The Projection and the Fixed Part

**Theorem.** The average $\bar N = |G|^{-1}\sum_g g^*$ is the projection of the operator algebra onto its fixed part, and it is a morphism of the operator algebra in the sense that it commutes with composition; the fixed part is a direct summand of the operator algebra as a module, and the image of the transfer of the trivial subgroup is the fixed part of the cohomology. The transfer for the trivial subgroup is the norm, whose average is the projection onto the invariants, so the fixed part of the cohomology and the fixed part of the operator algebra are selected by the same average.

*Proof.* The average is an idempotent by the norm computation, and it commutes with the conjugation action, hence it projects onto the fixed part of the operator algebra; the transfer of the trivial subgroup is the sum of the action operators, whose average is the projection onto the invariants. $\square$

## The Double Cosets and the Mackey Formula

### The Transitivity and the Conjugation

**Theorem.** The transfers and the restrictions are transitive: for subgroups $K\leq H\leq G$,

$$
\mathrm{cor}_H^G\circ\mathrm{cor}_K^H = \mathrm{cor}_K^G , \qquad \mathrm{res}_K^H\circ\mathrm{res}_H^G = \mathrm{res}_K^G ,
$$

and they are compatible with the conjugation, $g\,\mathrm{res}_K^G\,g^{-1}=\mathrm{res}_{gKg^{-1}}^{gGg^{-1}}$, with the same for the transfers; the assignment $H\mapsto$ the pair $(\mathrm{res}_H^G,\mathrm{cor}_H^G)$ is therefore a functor on the poset of the subgroups up to conjugation.

*Proof.* The corestriction is the sum over the cosets and the cosets compose, $G/K=(G/H)(H/K)$, giving the first identity; the restriction is the inclusion of the fixed parts and the fixed parts nest, giving the second; the conjugation statement is the transport of the fixed parts along the conjugating automorphism. $\square$

### The Double Coset Formula

**Theorem (Mackey).** For subgroups $H,K\leq G$ the composite of the transfer from $H$ with the restriction to $K$ is the sum over the double cosets of the conjugates of the transfers and the restrictions:

$$
\mathrm{res}_K^G\circ\mathrm{cor}_H^G = \sum_{KgH\in K\backslash G/H} \mathrm{cor}_{K\cap gHg^{-1}}^{K}\circ g\circ\mathrm{res}_{H\cap g^{-1}Kg}^{H} ,
$$

the **double coset formula**, which is the multiplication rule of the Mackey functor of the equivariant operators; for $H=K=1$ it specialises to the norm and for $H=K$ normal to the sum of the conjugations over the quotient $G/H$.

*Proof.* The cosets of $H$ in $G$ are partitioned by the double cosets $KgH$, and the restriction to $K$ of the transfer is the sum of the restrictions to $K$ of the summands of each double coset; within a double coset the summands are the conjugates of the transfer from $K\cap gHg^{-1}$ to $K$, which is the stated sum. $\square$

### The Specialisations

**Corollary.** For $H=K=1$ the formula reads $\mathrm{res}_1^G\circ\mathrm{cor}_1^G = N_G$, the norm; for $H=K$ general it reads the sum over the double cosets of the conjugates of the transfers from $H\cap gHg^{-1}$, which is the single identity when $H$ is normal and the orbit of the conjugates otherwise; the specialisations are the identities that the operator theory uses most.

*Proof.* Each is the evaluation of the double coset formula in the stated case, using that a single double coset generates the composite. $\square$

## The Normal Subgroups and the Invariant Operators

### The Quotient Operators

**Theorem.** Let $N\trianglelefteq G$ be a normal subgroup. The fixed part of the operator algebra for $G$ factors through the fixed part for $N$ and the quotient:

$$
\operatorname{End}(M)^G = \bigl(\operatorname{End}(M)^N\bigr)^{G/N},
$$

so the equivariant operators are the $G/N$-invariant operators among the $N$-equivariant ones; the transfer $\mathrm{cor}_N^G$ and the restriction $\mathrm{res}_N^G$ are the operators that compare the two fixed parts, and they are the ones that the quotient action does not move.

*Proof.* An operator commutes with all of $G$ exactly when it commutes with $N$ and its conjugation action descends to the quotient $G/N$, which is the stated iterated fixed part; the transfer and the restriction are equivariant for the quotient action by the conjugation compatibility. $\square$

### The Inflation and the Fixed Part

**Corollary.** If the action of $N$ on $M$ is trivial, then $\operatorname{End}(M)^N=\operatorname{End}(M)$ and the fixed part under $G$ is the fixed part under the quotient, $\operatorname{End}(M)^G=\operatorname{End}(M)^{G/N}$, the action being inflated from the quotient; for the group of order two the fixed part of the operator algebra is the invariants of the single involution, and the transfer and the norm generate the algebra of the invariant operators.

*Proof.* The triviality of the action of $N$ makes the first fixed part everything, and the inflation statement is the definition of the action through the quotient. $\square$

## Examples

**Example (the group algebra).** For the regular representation $M = k[G]$ the fixed part is the one-dimensional space of the constants, the norm is the matrix of rank one whose entries are all one, the average is the projection onto the constants, and the transfer for $H=1$ is the norm; the operator algebra $\operatorname{End}(k[G])$ with its fixed part is the group algebra acting on itself by left and right multiplication with the conjugation action of $G$, whose fixed part is the centre.

**Example (the free action).** For a free action on $X$ the induced action on $H^*(X;k)$ may still be non-trivial in the presence of torsion; when two is invertible in $k$ and the action is free the fixed part of the cohomology is the cohomology of the orbit space by *The Cohomology of an Orbit Space*, and the transfer is an isomorphism onto it up to the scalar, so the fixed part of the operator algebra is the operator algebra of the quotient.

**Example (the fixed action).** For the trivial action every operator commutes with the action, so the fixed part is the whole operator algebra and the transfer is the index-times-identity; the average is the identity, and the example is the extreme case in which the fixed part carries no information. The two extremes bracket the equivariant case, in which the fixed part is a proper subalgebra.

## Summary

The equivariant operators on a $G$-module are the fixed part $\operatorname{End}(M)^G = \operatorname{End}_G(M)$ of the operator algebra under the conjugation action, the intertwining operators; the group contributes the norm $N=\sum_g\rho(g)$, whose average $|G|^{-1}N$ is the projection onto the fixed part when the order is invertible, and, for a subgroup $H$, the restriction $r=\mathrm{res}_H^G$, the inclusion $M^G\hookrightarrow M^H$, and the transfer $t=\mathrm{cor}_H^G(x)=\sum_{g\in G/H}\rho(g)x$ from $M^H$ to $M^G$. The two are adjoint under the evaluation pairing, $\langle t\,\alpha,\beta\rangle=\langle\alpha,r\,\beta\rangle$, and their composites are $r\circ t=[G:H]$, $t\circ r=[G:H]$ on the fixed parts and $t\circ r=\sum_{g\in G/H}g^*$ in the group cohomology, together with $N_G=t\circ N_H$; the adjunction is Frobenius reciprocity, and its cohomological form is Shapiro's lemma $H^*_G(G/H\times Z;\underline M)\cong H^*_H(Z;\underline M)$. The fixed part of the operator algebra is the algebra of the equivariant operators, containing the transfers, the restrictions and the multiplications by the invariant classes, and it is the summand selected by the averaging projection; the fixed part of the cohomology and the fixed part of the operator algebra are selected by the same average, and the free and the trivial actions are the two extremes. The equivariant homotopy theory and the orbit category are those of *Equivariant Homotopy Theory*, the transfer in the Borel model is that of *The Transfer and the Involution*, the adjoint of an operator is that of *Dual Spaces and the Adjoint Operator*, and the invariants and the group cohomology are those of *Group Cohomology*. Nothing analytic and nothing geometric was used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$, $\rho : G\to\operatorname{Aut}(M)$ | $G$-module and the action |
| $M^G$, $M_G$ | Fixed part and coinvariants |
| $\operatorname{End}(M)^G = \operatorname{End}_G(M)$ | Fixed part of the operator algebra; intertwining operators |
| $N=\sum_g\rho(g)$, $\bar N=|G|^{-1}N$ | Norm and its idempotent average |
| $\bar N$ | Projection onto $M^G$; kernel the coinvariants |
| $r=\mathrm{res}_H^G : M^G\hookrightarrow M^H$ | Restriction, the inclusion of fixed parts |
| $t=\mathrm{cor}_H^G(x)=\sum_{g\in G/H}\rho(g)x$ | Transfer (corestriction) $M^H\to M^G$ |
| $r\circ t=[G:H]$, $t\circ r=[G:H]$ | The two composition identities on the fixed parts |
| $t\circ r=\sum_{g\in G/H}g^*$, $N_G=t\circ N_H$ | Coset-sum identity and the norm identity |
| $\langle t\,\alpha,\beta\rangle=\langle\alpha,r\,\beta\rangle$ | Adjointness (Frobenius reciprocity) |
| $H^*_G(G/H\times Z;\underline M)\cong H^*_H(Z;\underline M)$ | Shapiro's lemma for the equivariant cohomology |
| $H^*_G(X;\underline M)$, $\mathrm{tr}_H^G=\sum_{g\in G/H}(g^{-1})^*$ | Equivariant cohomology and its transfer operator |

## Further Reading

- Kenneth S. Brown, *Cohomology of Groups* (Springer, 1982), for the transfer, the restriction and Frobenius reciprocity in group cohomology.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the equivariant operators and the transfer to the fixed part.
- Tammo tom Dieck, *Transformation Groups* (de Gruyter, 1987), for the equivariant cohomology, Shapiro's lemma and the transfer.
- Jean-Pierre Serre, *Linear Representations of Finite Groups* (Springer, 1977), for the norm, the averaging projection and the intertwining operators.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the fixed part of the operator algebra and the group algebra with its conjugation action.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for the adjunction of the induction and the restriction and the induced modules.
