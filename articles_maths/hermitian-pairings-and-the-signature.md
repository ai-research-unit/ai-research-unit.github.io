
# __Hermitian Pairings and the Signature__

## Introduction

A **Hermitian pairing** is a sesquilinear form over a ring with an involution, symmetric or antisymmetric in the appropriate sense; the **signature** is its basic numerical invariant over the reals, and the classification of such pairings up to the addition of hyperbolic forms is the **Witt group**. This article develops the algebra: the $\varepsilon$-Hermitian forms, the Witt group and the signature, the Grothendieck–Witt ring, and the **Wall groups** that arise as the Witt groups of forms over a group ring. It is the algebraic home of the intersection form of *Poincaré Duality* and of the equivariant form of *The Involution on the Homology*, and it is the input of the surgery obstruction and of the equivariant signature.

The vocabulary is needed because the intersection form of a manifold is only the first of a family: the form twisted by a group action, the form over the group ring of the fundamental group, and the $\varepsilon$-quadratic refinements all live in the same framework, and the signature is the universal numerical invariant of the family over the reals. The Wall groups then organise the vanishing of the higher-dimensional forms, and the periodicity of the groups is the algebra behind the dimension-four periodicity of the signature.

**The article assumes** the linear algebra of bilinear and sesquilinear forms over a field or a ring (*Bilinear Forms*, *Linear Spaces*), the intersection form and the signature of *Poincaré Duality*, the group ring and its involution from *The Involution as an Operator on the Homology*, and the tensor and exterior algebra.

**The boundaries of the article.** The intersection form of a manifold, its signature and the signature theorem are *Poincaré Duality* and the differential topology of Part III; the equivariant version is *Hermitian Pairings and the Equivariant Signature*, the next article; the surgery obstruction and the Wall groups as the obstructions of the surgery are *Cobordism and Surgery Theory*; the analytic index theory of the signature is Part IV. The higher algebraic K-theory and the Hermitian K-theory are named and belong to *Higher Algebraic K-Theory*, written in Part II of the algebraic topology material. No analysis is used.

## Hermitian and $\varepsilon$-Hermitian Forms

**Definition.** Let $A$ be a ring with an involution $a\mapsto\bar a$ (an additive map with $\overline{ab} = \bar b\bar a$ and $\bar{\bar a} = a$). A **sesquilinear form** on a left $A$-module $M$ is a biadditive map $\varphi : M\times M\to A$ with $\varphi(ax,by) = a\varphi(x,y)\bar b$; it is **$\varepsilon$-Hermitian** for a central unit $\varepsilon$ with $\bar\varepsilon\varepsilon = 1$ if
$$
\varphi(y,x) = \varepsilon\,\overline{\varphi(x,y)} ,
$$
and it is **alternating** when in addition $\varphi(x,x) = 0$ and $\varepsilon = -1$. The associated **quadratic refinement** is a function $q : M\to A/\{a-\bar a\}$ with $q(ax) = aq(x)\bar a$ and $q(x+y)-q(x)-q(y) = \varphi(x,y)$, and an **$\varepsilon$-quadratic form** is a pair $(\varphi,q)$.

**Examples.** (a) $A = \mathbb{R}$ with the trivial involution and $\varepsilon = +1$: the symmetric bilinear forms $Q(x,y) = Q(y,x)$. (b) $A = \mathbb{C}$ with complex conjugation and $\varepsilon = +1$: the Hermitian forms $\varphi(y,x) = \overline{\varphi(x,y)}$. (c) $A = \mathbb{Z}[\pi]$ with the involution $g\mapsto g^{-1}$ and $\varepsilon = \pm1$: the forms of the surgery theory. (d) The intersection form of a closed oriented $2k$-manifold is symmetric for $k$ even and alternating for $k$ odd, that is, $(-1)^k$-Hermitian over $\mathbb{Z}$ with the trivial involution.

**Proposition (symmetry and the sign).** Over a field $F$ of characteristic not two, every alternating form is skew-symmetric and conversely; a symmetric form has $\varphi(x,x)$ arbitrary and an antisymmetric one has $\varphi(x,x) = 0$. The intersection form of a closed oriented $2k$-manifold is $\varepsilon$-Hermitian with $\varepsilon = (-1)^k$, so the alternating case is the odd middle dimension.

**Proof.** The statements are the definitions and the parity computation of *Poincaré Duality*: the commutativity of the cup product up to $(-1)^k$ on the middle cohomology gives the sign.

**Definition (nondegeneracy).** A form is **nondegenerate** if the map $M\to M^{*} = \operatorname{Hom}_A(M,A)$, $x\mapsto\varphi(x,-)$, is an isomorphism; a **Lagrangian** is a submodule $L$ with $L = L^{\perp}$; a form is **hyperbolic** if it is nondegenerate and has a Lagrangian.

**Proposition (the hyperbolic form).** For a finitely generated projective $A$-module $P$ the **hyperbolic form** $H(P)$ on $P\oplus P^{*}$ with $\varphi((x,f),(y,g)) = f(y) + \varepsilon\overline{g(x)}$ is nondegenerate and has $P\oplus0$ as a Lagrangian; over a field it is the form $U^{\oplus r}$ with $U = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ for $\varepsilon = +1$ and $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ for $\varepsilon = -1$, and its signature is $0$.

**Proof.** The verification is a direct computation of the form on the summands, and the identification over a field is the change to the standard basis $e,f$; the signature vanishes because the form is hyperbolic.

## The Witt Group and the Signature

**Definition.** The **Witt group** $W^{\varepsilon}(A)$ is the Grothendieck group of the isomorphism classes of nondegenerate $(-1)^k$-forms under the orthogonal direct sum, modulo the subgroup generated by the hyperbolic forms; the **Grothendieck–Witt group** $GW^{\varepsilon}(A)$ is the corresponding group before imposing the hyperbolic relation, and the forgetful map $GW\to K_0(A)$ records the underlying projective module.

**Theorem (the signature over the reals).** Over $A = \mathbb{R}$ with the trivial involution and $\varepsilon = +1$ the signature
$$
\sigma(Q) = (\text{number of positive eigenvalues}) - (\text{number of negative eigenvalues})
$$
is the complete invariant of a nondegenerate symmetric bilinear form up to orthogonal equivalence (Sylvester's law of inertia), it is additive over orthogonal sums, it vanishes on the hyperbolic forms, and it induces an isomorphism
$$
\sigma : W(\mathbb{R})\xrightarrow{\ \cong\ }\mathbb{Z}.
$$
For $A = \mathbb{C}$ with complex conjugation and $\varepsilon = +1$ the same statement holds: the signature is the complete invariant of a nondegenerate Hermitian form and $W(\mathbb{C},-)\cong\mathbb{Z}$.

**Proof.** Sylvester's law reduces a form to the diagonal form with $p$ entries $+1$ and $q$ entries $-1$; the hyperbolic forms are those with $p = q$, so the Witt group is generated by the classes of $\langle1\rangle$ and $\langle-1\rangle = -\langle1\rangle$, and the signature is the resulting isomorphism onto $\mathbb{Z}$; the Hermitian case over $\mathbb{C}$ is the same diagonalisation with the conjugate symmetry.

**Proposition (the signature is a ring homomorphism).** The signature is multiplicative under the tensor product of forms and additive under the orthogonal direct sum, so it defines a ring homomorphism from the Witt ring of $\mathbb{R}$ to $\mathbb{Z}$; over an ordered field the same holds, and the signature of the intersection form of a manifold is the topological signature of *Poincaré Duality*.

**Proof.** The tensor product of diagonal forms is diagonal with the products of the entries, so the signatures multiply; the additivity is the direct sum. The identification with the topological signature is the comparison of the diagonalisation of the intersection form with the definition of the signature.

**Corollary (the signature of a hyperbolic and of an alternating form).** A hyperbolic form has signature zero; an alternating form over $\mathbb{R}$ has a diagonalisation with entries in pairs $\pm1$, so its signature is zero as well, and the intersection form of a closed oriented $4k+2$-manifold has signature zero. This is the first vanishing statement of the theory.

**Proof.** The hyperbolic forms have $p = q$ by the Lagrangian; an alternating form over $\mathbb{R}$ is $\varepsilon = -1$-Hermitian, and the associated symmetric form $x\cdot y\mapsto\varphi(x,Jy)$ (with $J$ the complex structure of the symplectic space) has eigenvalues in pairs $\pm$, so the signature vanishes; the topological case is the intersection form of a $(4k+2)$-manifold, which is alternating.

## The Wall Groups

**Definition.** For a ring with involution $A$ the **Wall groups** $L_n(A)$ are the Witt groups of the $\varepsilon$-quadratic forms on finitely generated free $A$-modules for $n\equiv0,1\pmod4$ (with $\varepsilon = +1$ for $n\equiv0$ and $\varepsilon = -1$ for $n\equiv2$), and the corresponding groups of formations for $n$ odd; they fit into a $4$-periodic sequence
$$
L_{n+4}(A)\cong L_n(A).
$$
For a group ring $A = \mathbb{Z}[\pi]$ with the involution $g\mapsto g^{-1}$ the groups $L_n(\mathbb{Z}[\pi])$ are the **surgery obstruction groups** of *Cobordism and Surgery Theory*.

**Theorem (properties of the Wall groups).** The groups $L_n(A)$ are the obstruction groups of the surgery theory: an $n$-dimensional surgery problem with fundamental group $\pi$ has an obstruction in $L_n(\mathbb{Z}[\pi])$, vanishing exactly when the problem can be surgered to a homotopy equivalence for $n\geq5$. The groups are $4$-periodic, the group $L_0(A)$ is the Witt group of the quadratic forms and the group $L_{4k}(\mathbb{Z}[\pi])$ is detected by the signatures of the forms twisted by the representations of $\pi$.

**Proof sketch.** The identification of the surgery obstruction with a Witt class is the content of the surgery classification; the periodicity is the periodicity of the classifying spaces $BSO$ and $BSTOP$ and the algebra of the forms; the detection of $L_{4k}$ by the twisted signatures is the "multisignature" of the next article and the algebraic statement that the signatures form a complete set of invariants over $\mathbb{Q}$. The details are *Cobordism and Surgery Theory*.

**Example (the trivial group).** For $\pi = 1$ the groups are $L_0(\mathbb{Z})\cong\mathbb{Z}$ (detected by the signature), $L_2(\mathbb{Z})\cong\mathbb{Z}/2$ (detected by the Arf invariant), and $L_1(\mathbb{Z}) = L_3(\mathbb{Z}) = 0$; the corresponding surgery obstructions are the signature and the Arf invariant, the classical invariants of the surgery of simply connected manifolds.

**Remark (the Hermitian K-theory).** The Witt group is the quotient of the Grothendieck–Witt group by the hyperbolic classes, and the higher analogues form the **Hermitian K-theory** $K_*^{h}(A)$ of Karoubi; the forgetful map to the algebraic K-theory and the Bott-type periodicity relate the two. The systematic development and the computations for the group rings are in *Higher Algebraic K-Theory* and the surgery literature, and the present article uses only the zeroth and the Wall groups.

## The Signature in Topology

**Theorem (the signature as a cobordism invariant).** The signature of a closed oriented $4k$-manifold is an invariant of its oriented cobordism class, additive under the disjoint union and multiplicative under the products; it therefore defines a ring homomorphism $\Omega_{4k}\to\mathbb{Z}$ from the oriented cobordism ring, and it factors through the rationalisation $L_{4k}(\mathbb{Z})$ of the Wall group.

**Proof.** The signature is additive over the connected sum and over the cobordism: if $W$ is an oriented $(4k+1)$-manifold with boundary $M_0\sqcup M_1$, the intersection forms of the two boundary components have the same signature because the middle-dimensional form of $W$ provides a "null-cobordism" of the two forms; the additivity and the multiplicativity are the algebra of the direct sums and the tensor products. The factorisation is the comparison of the cobordism invariant with the surgery obstruction.

**Corollary (the Hirzebruch signature theorem, named).** For a closed oriented smooth $4k$-manifold the signature is the evaluation of the $L$-genus,
$$
\sigma(M) = \int_M L_k(p_1,\dots,p_k),
$$
the Hirzebruch signature theorem; the formula is the analytic and differential-topological computation of the invariant, and it belongs to *Smooth Manifolds and Differential Topology* and Part IV. The present article uses only the topological invariance.

**Remark (the signature defect).** For a closed oriented $(4k-1)$-manifold the signature of a bounding $4k$-manifold depends on the choice of the bounding manifold through the **signature defect**, an invariant of the boundary which is the $\rho$-invariant of Atiyah–Singer–Patodi; it is a bordism invariant of the boundary and the first of the "secondary" invariants of the theory, and its analytic definition is Part IV, with the topological analogues in *Floer Homology*.

## Examples

**Example (the intersection form of a four-manifold).** The intersection form of a closed oriented four-manifold is a nondegenerate symmetric form over $\mathbb{Z}$; over $\mathbb{R}$ it is classified by its rank and signature, and the signature is the topological invariant of the previous theorem. The K3 surface with its form $2(-E_8)\oplus3U$ has signature $-16$ and rank $22$, and the $E_8$ form is the standard definite even form whose signature is $-8$; the examples are the recurrences of *Poincaré Duality*.

**Example (the hyperbolic form of a product).** The intersection form of the product $S^{2k}\times S^{2k}$ has the hyperbolic summand $U$ spanned by the two factors, with the classes of the two spheres as the Lagrangian basis; the form is hyperbolic and the signature is zero. The example is the model of the vanishing of the signature for a product.

**Example (the form of a fibered $4$-manifold).** A closed oriented $4$-manifold fibered over the circle with fiber a $3$-manifold $\Sigma$ has the intersection form determined by the monodromy of the fibration through the "Lefschetz" pairing on $H_1(\Sigma)$; the signature is the signature defect of the fibration and the example is the meeting point with *Floer Homology* and the mapping tori of *Low-Dimensional Topology*. The computation is the "Novikov–Lefschetz" formula, and it is the topological source of the $\rho$-invariants.

**Example (the Wall group of the trivial group).** For the trivial group the surgery obstruction group is $L_0(\mathbb{Z})=\mathbb{Z}$ via the signature and $L_2(\mathbb{Z})=\mathbb{Z}/2$ via the Arf invariant; the example shows that the signature is the first and the "odd-dimensional" obstruction the second of the simply connected surgery invariants, and the periodicity $L_{n+4}=L_n$ is visible in the pair.

## Summary

A Hermitian pairing over a ring with an involution is a sesquilinear form symmetric up to the sign $\varepsilon$; a nondegenerate form with a Lagrangian is hyperbolic, and the Witt group is the group of isomorphism classes modulo the hyperbolic forms. Over the real and complex numbers the signature is the complete invariant of a symmetric or Hermitian form and identifies the Witt group with $\mathbb{Z}$, and it is additive under the direct sum and multiplicative under the tensor product; the alternating forms have vanishing signature, which is the vanishing of the signature in the middle dimension of a $4k+2$-manifold. The Wall groups $L_n(A)$ are the Witt groups of the quadratic forms and of the formations over $A$, they are $4$-periodic, they are detected in dimension $4k$ by the twisted signatures, and for the group rings they are the surgery obstruction groups. The signature is a cobordism invariant of a closed oriented $4k$-manifold, computed analytically by the Hirzebruch signature theorem, and the signature defect of a boundary is the $\rho$-invariant. The intersection forms of the four-manifolds, the hyperbolic form of a product and the forms of a fibered manifold are the standard examples.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $a\mapsto\bar a$ | a ring with an involution |
| $\varepsilon$-Hermitian form $\varphi$ | sesquilinear with $\varphi(y,x) = \varepsilon\overline{\varphi(x,y)}$ |
| $(1,0)$ alternating case | $\varepsilon = -1$ with $\varphi(x,x)=0$; the intersection form of a $4k+2$-manifold |
| hyperbolic form $H(P)$, $U$ | a nondegenerate form with a Lagrangian $P\oplus0$; $U = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ |
| $W^{\varepsilon}(A)$, $GW^{\varepsilon}(A)$ | the Witt group and the Grothendieck–Witt group |
| $\sigma : W(\mathbb{R})\cong\mathbb{Z}$ | the signature, the complete invariant over $\mathbb{R}$ (Sylvester) |
| $L_n(A)$, $L_{n+4}\cong L_n$ | the Wall groups, $4$-periodic; the surgery obstruction groups for $A=\mathbb{Z}[\pi]$ |
| $L_0(\mathbb{Z})=\mathbb{Z}$, $L_2(\mathbb{Z})=\mathbb{Z}/2$ | the signature and the Arf invariant for the trivial group |
| $\Omega_{4k}\to\mathbb{Z}$ | the signature as a cobordism invariant |
| $\sigma(M)=\int_M L_k(p_1,\dots,p_k)$ | the Hirzebruch signature theorem (Part III) |
| $\rho$-invariant | the signature defect of a boundary; the secondary invariant (Part IV) |

## Further Reading

- C. T. C. Wall, "The Classification of Hermitian Forms", *Compositio Mathematica* 22 (1970), 313–319, and *Surgery on Compact Manifolds* (Academic Press, 1970), for the Wall groups and the surgery obstruction.
- Jean-Pierre Serre, *A Course in Arithmetic* (Springer, 1973), for the Witt group, the Grothendieck–Witt group and the quadratic forms over fields.
- Max Karoubi, "Le théorème fondamental de la $K$-théorie hermitienne", *Annals of Mathematics* 112 (1980), 259–282, for the Hermitian K-theory and its periodicity.
- Friedrich Hirzebruch, *Topological Methods in Algebraic Geometry* (Springer, 1966), for the signature theorem and the $L$-genus.
- Michael F. Atiyah, Vijay K. Patodi and Isadore M. Singer, "Spectral Asymmetry and Riemannian Geometry II", *Mathematical Proceedings of the Cambridge Philosophical Society* 78 (1975), 405–432, for the $\rho$-invariant and the signature defect, developed in Part IV.
- Jean Milnor and Dale Husemoller, *Symmetric Bilinear Forms* (Springer, 1973), for the Witt groups, the hyperbolic forms and the classification over the integers and the fields.
- Andrew Ranicki, *Algebraic and Geometric Surgery* (Oxford University Press, 2002), for the algebraic surgery, the Wall groups and their assembly into the surgery exact sequence.
