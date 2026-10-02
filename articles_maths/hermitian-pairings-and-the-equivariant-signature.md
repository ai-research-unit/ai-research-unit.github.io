
# __Hermitian Pairings and the Equivariant Signature__

## Introduction

The **equivariant signature** of a $G$-manifold is the family of signatures of the intersection form restricted to the eigenspaces of the action, one for each element of the group, and the **$G$-signature theorem** computes them from the fixed sets and their normal representations. This article is the equivariant layer of *Hermitian Pairings and the Signature*: the equivariant Hermitian forms, the multisignature, the equivariant Wall groups, and the theorem that turns the algebra into a computation on the fixed set.

The subject is the meeting point of the whole batch. The equivariant form on the middle homology is the form of *The Involution on the Homology* made into a family parameterised by the group; the equivariant signature is a cobordism invariant of *Involutions and the Cobordism of Group Actions*; it is the $L$-theoretic obstruction of the equivariant surgery of *Involutions on Manifolds and Equivariant Surgery*; and its supertrace interpretation is the Lefschetz number of *The Involution on the Homology Operators*. The $G$-signature theorem is the analytic computation, and its statement is the goal of the article.

**The article assumes** the Hermitian forms, the Witt and Wall groups and the signature of *Hermitian Pairings and the Signature*, the equivariant homology and the fixed-set theory of *The Involution on the Homology* and *Involutions on Manifolds and Equivariant Surgery*, the representation theory of the finite groups (*Linear Spaces*, Part I), and the equivariant signature as a cobordism invariant from *Involutions and the Cobordism of Group Actions*.

**The boundaries of the article.** The algebra of the forms is *Hermitian Pairings and the Signature*, the previous article; the equivariant surgery obstruction is *Involutions on Manifolds and Equivariant Surgery*; the equivariant cobordism is *Involutions and the Cobordism of Group Actions*; the analytic index theory of the signature operator, the Atiyah–Singer theorem and the $\rho$-invariants are Part IV (*Index Theory and the Atiyah–Singer Theorem*), and the Floer-theoretic secondary invariants are *Floer Homology*. The article states the $G$-signature theorem and its consequences without the analysis, and refers to Part IV for the proof.

## The Equivariant Form and the Multisignature

**Definition.** Let a finite group $G$ act on a closed oriented $4k$-manifold $M$, and let $H = H_{2k}(M;\mathbb{Q})$ with the nondegenerate symmetric intersection form $Q$, made into a $G$-module by the action. For $g\in G$ the $g$-eigenspace decomposition $H\otimes\mathbb{C} = \bigoplus_{\lambda}H_{\lambda}$ by the eigenvalues $\lambda$ of $g_*$ provides the **equivariant signature**
$$
\sigma(g,M) = \sum_{\lambda}\lambda\,\sigma\bigl(Q\,|\,H_{\lambda}\bigr),
$$
where $\sigma(Q|H_{\lambda})$ is the signature of the Hermitian form induced on the eigenspace; for the identity $\sigma(e,M) = \sigma(M)$, and for an involution the formula is $\sigma(g,M) = \sigma(Q|H_{+})-\sigma(Q|H_{-})$ with the two eigenspaces of $g_*$.

**Proposition (equivariance and the twisted form).** The form $Q$ is $G$-invariant (for an orientation-preserving action), so the eigenspaces of $g_*$ are $Q$-orthogonal and the restriction of $Q$ to each is nondegenerate; the equivariant signature is therefore a sum of ordinary signatures, and the form itself is the equivariant Hermitian form of *The Involution on the Homology*, whose eigenspace decomposition is the "twisted" form of the equivariant theory. The element $g\mapsto\sigma(g,M)$ defines a function on the group which is a virtual character of the representation of $G$ on $H$, so the multisignature is an element of the representation ring $R(G)$.

**Proof.** The invariance of the intersection form under an orientation-preserving homeomorphism makes the action preserve $Q$; the eigenspaces of $g_*$ are then orthogonal for $Q$ because distinct eigenvalues of a form-preserving operator are orthogonal for the Hermitian form, and the restriction to each is nondegenerate. The function $g\mapsto\operatorname{sign}$-combination is the character of the "signature representation", and the statement about $R(G)$ is the identification of the invariants of the form with the virtual representations of the group.

**Example (the swap of $S^2\times S^2$).** On $M = S^2\times S^2$ with $T$ the swap, $H_2 = \mathbb{Z}\langle a,b\rangle$ with $Q(a,a) = Q(b,b) = 0$ and $Q(a,b) = 1$; the eigenspaces are $\mathbb{Z}\langle a+b\rangle$ with $Q = 2$ and signature $+1$, and $\mathbb{Z}\langle a-b\rangle$ with $Q = -2$ and signature $-1$. Hence $\sigma(T,M) = 1-(-1) = 2$ and $\sigma(e,M) = 1+(-1) = 0 = \sigma(S^2\times S^2)$, consistent with the vanishing of the signature of the product. The example is the smallest computation of the multisignature.

**Example (the sphere with the reflection).** The reflection of $S^{2k}$ has the fixed sphere $S^{2k-1}$; the middle homology is the sum of the two eigenspaces of dimensions giving the signature $\sigma(T,M) = 0$ and $\sigma(e,M) = 0$, because the middle homology of a sphere is zero; the example shows the triviality of the invariants in the low degrees and is the boundary case of the theory.

## The $G$-Signature Theorem

**Theorem ($G$-signature theorem, statement).** Let a finite group $G$ act smoothly and orientation-preservingly on a closed oriented $4k$-manifold $M$, and let $g\in G$. Then the equivariant signature is computed from the fixed set by
$$
\sigma(g,M) = \sum_{F\subseteq M^{\langle g\rangle}} \bigl(\text{the contribution of }F\bigr),
$$
where the sum is over the components of the fixed set of the cyclic group generated by $g$, and the contribution of a component $F$ is the evaluation on $F$ of the equivariant characteristic class of the normal bundle, that is, of the $L$-class of the normal bundle formed with the "characteristic power series" of $g$ acting on the normal representation; for a fixed component of the identity element the contribution reduces to the ordinary signature of $F$ when $F$ has dimension divisible by four.

**Proof sketch.** The theorem is the Lefschetz fixed point formula for the signature operator: the equivariant index of the signature operator is the equivariant signature, and the Atiyah–Bott fixed point formula computes the index as the sum of the local contributions at the fixed components, each contribution being the evaluation of a characteristic class of the normal bundle. The equality of the equivariant index with the equivariant signature is the analytic input, and the local formula is the differential-geometric computation; the proof belongs to Part IV, and the statement is recorded here for the topological consequences.

**Corollary (the involution case).** For an involution $T$ of a closed oriented $4k$-manifold the theorem computes $\sigma(T,M)$ from the fixed components with their normal representations; if the fixed set is empty the equivariant signature vanishes, which is the statement of the free involutions, and if the fixed set is a union of isolated points the contribution of each is $\pm1$. The congruence of the eigenvalues of the normal representations at the fixed points is the arithmetic content of the formula.

**Proof.** The local contribution is a characteristic number of the normal representation of the component; for an isolated fixed point the normal representation is the reflection $-I$ on the tangent space, and its contribution to the formula is $1$, with the sign determined by the orientation of the local model; the free case is the emptiness of the sum. The details of the local terms with the normal representations are the content of the $G$-signature theorem.

**Remark (the equivariant form and the surgery obstruction).** The equivariant signature is the $L$-theoretic part of the equivariant surgery obstruction of *Involutions on Manifolds and Equivariant Surgery*: the obstruction group $L_{4k}(\mathbb{Z}[G])$ is detected rationally by the multisignature, so a surgery problem with vanishing equivariant signatures is rationally unobstructed. This is the reason the equivariant signature is the first and the principal obstruction in the even-dimensional equivariant surgery, and the torsion of the obstruction groups is detected by the finer invariants of *Stable Homotopy Theory* and the surgery literature.

## The Equivariant Wall Groups and the Localisation

**Theorem (detection of the equivariant Wall groups).** For a finite group $G$ the homomorphism
$$
L_{4k}\bigl(\mathbb{Z}[G]\bigr)\longrightarrow \bigoplus_{\chi\in\hat G}\mathbb{Z}, \qquad \text{multisignature},
$$
sending a form to the signatures of its twisted forms by the complex characters of $G$, is injective after tensoring with $\mathbb{Q}$ (and is the rationalisation of the group); the kernel of the integral map is the torsion of the Wall group, detected by the other invariants. For the equivariant surgery of a manifold the multisignature is therefore a complete rational obstruction.

**Proof sketch.** The group ring $\mathbb{C}[G]$ splits as a product of matrix algebras indexed by the irreducible characters, and the forms over $\mathbb{C}[G]$ decompose into the forms over the simple summands; the signature of a form over a simple summand is the signature of the corresponding twisted form, and the collection of these is the multisignature. The rational injectivity is the semisimplicity of $\mathbb{C}[G]$; the integral torsion is the difference between the Wall group and its rationalisation. The details are the Wall group computations, and the statement is the algebraic form of the $G$-signature theorem.

**Corollary (the localisation of the equivariant signature).** The multisignature is the localisation of the equivariant form at the characters, so the equivariant signature is determined by the fixed-set data through the $G$-signature theorem and conversely the fixed-set data are constrained by the multisignature; the two descriptions agree because both compute the same equivariant index.

**Remark (the position in the sequence).** The equivariant Wall groups fit into the equivariant surgery exact sequence of *Involutions on Manifolds and Equivariant Surgery*; the rational part is the multisignature, the torsion is the equivariant Arf and the higher Whitehead-type invariants, and the whole is the equivariant analogue of the simply connected case where $L_0(\mathbb{Z}) = \mathbb{Z}$ and $L_2(\mathbb{Z}) = \mathbb{Z}/2$.

## Applications

**Example (the signature of a branched cover).** Let $\Sigma\to M$ be a cyclic branched cover of a closed oriented $4k$-manifold with the branching locus a submanifold, arising from an action of $\mathbb{Z}/n$; the signature of the cover is the equivariant signature of the action on the base evaluated with the "regular" character, so the $G$-signature theorem computes the signature of the branched cover from the fixed set of the action. This is the topological form of the classical formulas for the signatures of the cyclic covers, and it is the tool by which the signatures of the covers of a knot or of a surface are computed in *Equivariant Knot Theory* and *Knot Theory*.

**Example (the free involutions and the vanishing).** A free involution of a closed oriented $4k$-manifold has empty fixed set, so the $G$-signature theorem gives $\sigma(T,M) = 0$; the equivariant signature vanishes on the free part of the equivariant cobordism, in agreement with the reduction of the free case to the quotient in *Involutions and the Cobordism of Group Actions*.

**Example (the four-dimensional case).** For an orientation-preserving involution of a closed oriented four-manifold the two numbers $\sigma(e,M) = \sigma(M) = \sigma(M^{+})+\sigma(M^{-})$ and $\sigma(T,M) = \sigma(M^{+})-\sigma(M^{-})$ determine the signatures of the fixed and the anti-fixed parts of the middle homology; for the swap of $S^2\times S^2$ they are $(0,2)$, and for the involution $-I$ of $T^4$ they are $(0,0)$ because the form of the torus is hyperbolic on a symmetric splitting. The dimension four is the smallest in which the invariant is nontrivial, and the computations reproduce the splitting examples of *The Involution on the Homology* and *The Involution on the Homology Operators*.

**Example (the $\rho$-invariants).** A closed oriented $(4k-1)$-manifold bounding a $4k$-manifold with a group action has the signature defect of the boundary, the $\rho$-invariant, whose equivariant version is a function on the group generalising the multisignature; the invariant is a bordism invariant of the boundary and its analytic definition is Part IV, with the Floer-theoretic refinements in *Floer Homology*. The example shows the secondary layer of the theory, one dimension down from the multisignature.

## The Multisignature as a Character

**Theorem (the multisignature is a virtual character).** The function $g\mapsto\sigma(g,M)$ is constant on the conjugacy classes of $G$ and is the character of a virtual complex representation of $G$: decomposing the $\mathbb{C}[G]$-module $H\otimes\mathbb{C}$ into the isotypic components of the irreducible characters $\chi$, and writing $\sigma_{\chi}(M)$ for the signature of the $\chi$-twisted Hermitian form, one has
$$
\sigma(g,M) = \sum_{\chi}\sigma_{\chi}(M)\,\chi(g),
$$
so the multisignature is an element of the representation ring $R(G)$ and is determined by the finitely many integers $\sigma_{\chi}(M)$.

**Proof.** The group ring $\mathbb{C}[G]$ is semisimple, so $H\otimes\mathbb{C}$ is the direct sum of the isotypic components $\rho\otimes\operatorname{Hom}_G(\rho,H)$; the form, being $G$-invariant, respects the decomposition, and its signature on an isotypic component is $\dim(\rho)$ times the signature of the $\chi$-twisted form. Evaluating the character identity at the identity gives $\sum_{\chi}\sigma_{\chi}(M)\dim(\chi) = \sigma(M)$, which is the ordinary signature, and the values at the other elements are the multisignature; hence the assignment is a virtual character.

**Corollary (the values at the identity and the regular element).** The value at the identity is the ordinary signature $\sigma(M)$, and the value at an element of order two with the eigenvalues $\pm1$ is the difference of the signatures of the two eigenspaces; for the trivial group the multisignature reduces to the single integer $\sigma(M)$ of *Hermitian Pairings and the Signature*. The example of the swap of $S^2\times S^2$ has character values $\sigma(e) = 0$ and $\sigma(T) = 2$, the two generating values of the representation ring of $\mathbb{Z}/2$ in this case.

## Multiplicativity and the Products

**Theorem (multiplicativity of the signature and the multisignature).** For closed oriented manifolds $M,N$ of dimensions divisible by four, the signature is multiplicative, $\sigma(M\times N) = \sigma(M)\sigma(N)$, and for a $G$-action on each with the diagonal action on the product the equivariant signature is multiplicative,
$$
\sigma(g,M\times N) = \sigma(g,M)\,\sigma(g,N),\qquad g\in G .
$$

**Proof.** The intersection form of $M^{4a}\times N^{4b}$ in the middle degree $2(a+b)$ is the sum of the tensor products of the forms of $M$ and $N$ in the complementary degrees; the only contribution to the signature is the tensor product of the middle forms, by the additivity and the vanishing of the signature on the alternating forms, and the tensor product of symmetric forms has the product of the signatures. The equivariant case follows because the action on the product is diagonal, so the eigenspaces of $g_*$ on the middle homology are the tensor products of the eigenspaces on the two factors, and the sign and the signature multiply.

**Corollary (the multiplicativity of the $G$-signature theorem).** The two sides of the $G$-signature theorem are multiplicative, so the theorem for a product follows from the theorem for the factors; this is the compatibility of the fixed-set formula with the products, since the fixed set of the diagonal action is the product of the fixed sets with the normal representations, and the characteristic classes multiply.

**Remark (the products with the trivial actions).** If $G$ acts trivially on $N$ then $\sigma(g,M\times N) = \sigma(g,M)\sigma(N)$ with the constant factor $\sigma(N)$, so the multisignature is a module over the ordinary signature in the product with a manifold of trivial action; this is the operator-theoretic form of the module structure of the equivariant bordism of *Involutions and the Cobordism of Group Actions*.

## Summary

The equivariant signature of a $G$-manifold is the sum of the signatures of the intersection form restricted to the eigenspaces of the action, and it is an element of the representation ring; for the identity it is the ordinary signature, and for an involution it is the difference of the signatures on the fixed and anti-fixed parts. The form is $G$-invariant, so the eigenspaces are orthogonal and the definition is elementary; the $G$-signature theorem computes the equivariant signature from the fixed set, as the sum over the fixed components of the evaluations of the equivariant characteristic classes of the normal bundles, and it is the Lefschetz fixed point formula for the signature operator. The equivariant Wall groups are detected rationally by the multisignature, so the equivariant signature is the complete rational obstruction of the equivariant surgery in dimension divisible by four, with the torsion carrying the finer invariants. The applications are the signatures of the cyclic branched covers, the vanishing of the equivariant signature for the free actions, the four-dimensional computations, and the $\rho$-invariants one dimension down; the analytic proof and the secondary invariants belong to Part IV and to *Floer Homology*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma(g,M)$ | the equivariant signature, an element of the representation ring $R(G)$ |
| $\sigma(g,M) = \sum_{\lambda}\lambda\,\sigma(Q|H_{\lambda})$ | the definition via the eigenspaces of $g_*$ |
| $\sigma(g,M) = \sigma(Q|H_{+})-\sigma(Q|H_{-})$ | the involution case |
| $G$-signature theorem | $\sigma(g,M) = \sum_{F\subseteq M^{\langle g\rangle}}(\text{normal contribution of }F)$ |
| $L_{4k}(\mathbb{Z}[G])\to\bigoplus_{\chi}\mathbb{Z}$ | the multisignature, rationally injective on the equivariant Wall group |
| $R(G)$ | the representation ring; the receptor of the multisignature |
| branched cover signature | computed by the $G$-signature theorem from the fixed set |
| $\rho$-invariant | the signature defect of a $(4k-1)$-manifold; the secondary invariant (Part IV) |
| $\sigma(g,M) = \sum_{\chi}\sigma_{\chi}(M)\chi(g)$ | the multisignature as a virtual character, $\sigma_{\chi}$ the twisted signatures |
| $H\otimes\mathbb{C} = \bigoplus_{\chi}\rho_{\chi}\otimes\operatorname{Hom}_G(\rho_{\chi},H)$ | the isotypic decomposition of the middle homology |
| $\sigma(g,M\times N) = \sigma(g,M)\sigma(g,N)$ | multiplicativity for the diagonal action |

## Further Reading

- Michael F. Atiyah and Isadore M. Singer, "The Index of Elliptic Operators: III", *Annals of Mathematics* 87 (1968), 546–604, for the $G$-signature theorem.
- Michael F. Atiyah and Raoul Bott, "A Lefschetz Fixed Point Formula for Elliptic Complexes II", *Annals of Mathematics* 88 (1968), 451–491, for the local contributions and the fixed-point formula.
- Friedrich Hirzebruch and Don Zagier, *The Atiyah–Singer Theorem and Elementary Number Theory* (Publish or Perish, 1974), for the computations of the equivariant signatures.
- C. T. C. Wall, *Surgery on Compact Manifolds* (Academic Press, 1970), for the Wall groups, their rational detection by the signatures and the surgery obstruction.
- Andrew Ranicki, *Algebraic and Geometric Surgery* (Oxford University Press, 2002), for the algebraic surgery, the multisignature and the assembly.
- Karl Heinz Dovermann and Reinhard Schultz, *Equivariant Surgery Theories and Their Periodicity Properties* (Springer Lecture Notes 1443, 1990), for the equivariant signatures as the rational surgery obstructions.
- Michael F. Atiyah, Vijay K. Patodi and Isadore M. Singer, "Spectral Asymmetry and Riemannian Geometry II", *Mathematical Proceedings of the Cambridge Philosophical Society* 78 (1975), 405–432, for the $\rho$-invariants and the secondary invariants of Part IV.
