
# __The Dehn Twist as an Operator__

## Introduction

A **Dehn twist** is the simplest nontrivial homeomorphism of a surface: cut the surface along a simple closed curve, rotate one of the two sides by a full turn, and reglue. The result is a homeomorphism supported in a neighbourhood of the curve, fixing the curve pointwise, and infinite in order. Its action on the first homology is the **transvection** determined by the intersection form, and this article reads the twist as an operator: the operator on the homology, its formula, and its place in the mapping class group, where the twists are the generators.

The twist is the second surface operator of the group, alongside *The Mapping Class Group Action* with which it pairs: the twists generate the mapping class group, the mapping class group acts on the homology, and the two facts together say that the transvections generate the symplectic group. The **Picard–Lefschetz formula** — that the monodromy around a vanishing cycle is the transvection with that cycle — is the same operator in a one-parameter family, and is named here and developed in the algebraic geometry of this batch.

**The article assumes** the intersection form on the first homology of a surface and the symplectic group, from *Bilinear Forms* and *Symplectic Forms and Poisson Brackets*, the fundamental group and the mapping class group from *The Fundamental Group and Covering Spaces* and the articles of this Part, and the notion of an isotopy class of homeomorphisms.

**The boundaries of the article.** The mapping class group as a whole — its definition, presentations, the Nielsen–Thurston classification, the curve complex and the Torelli group — is *Mapping Class Groups*, written in this Part, and is cited here; the present article treats the single operator and its immediate consequences. The measured foliations and the Thurston boundary need the measure theory of Part III. The monodromy of a Lefschetz fibration and the vanishing cycles are the algebraic-geometry articles of *Algebraic Geometry*; the higher-dimensional analogues of the twist, the twists along spheres, need the smooth structures of Part III and are named there. No metric, no hyperbolic structure and no analysis is used.

## The Dehn Twist

**Definition.** Let $S$ be a closed orientable surface and let $a\subseteq S$ be a simple closed curve. Choose a closed annular neighbourhood $N$ of $a$, with a homeomorphism $N\cong S^1\times[-1,1]$ carrying $a$ to $S^1\times\{0\}$. The **Dehn twist about $a$** is the homeomorphism
$$
T_a : S\to S
$$
equal to the identity outside $N$ and, on $N = S^1\times[-1,1]$, given by
$$
T_a(\theta,t) = (\theta + \pi(t+1),\, t) \qquad (\theta\in S^1 = \mathbb{R}/2\pi\mathbb{Z},\ t\in[-1,1]),
$$
so that the two halves $t<0$ and $t>0$ of the annulus are rotated by a full turn relative to each other while the curve $a = S^1\times\{0\}$ is fixed pointwise.

**Proposition (well-definedness and first properties).** The isotopy class of $T_a$ depends only on the isotopy class of $a$ and not on the annulus nor on the direction chosen; $T_a$ is orientation-preserving and preserves the curve $a$ pointwise; $T_a^{-1}$ is the twist about $a$ with the opposite direction, so $T_a$ has infinite order in the homeomorphism group modulo isotopy, except when $a$ bounds a disc on both sides.

**Proof.** Two annular neighbourhoods of an isotopic curve are isotopic, and an isotopy of the annulus can be arranged to carry one twist to the other; the twist is orientation-preserving because it preserves the orientation of the annulus. The curve $a$ is fixed pointwise by the formula. The order is the standard computation: on a curve crossing $a$ once, the twist adds one copy of the class of $a$, so the $k$-th power acts nontrivially for every $k\neq0$, as the transvection formula below shows.

**Remark (support and the general position of the curve).** The operator is supported in the annulus $N$, so it is the identity on the complement of $N$; a curve disjoint from $a$ is unchanged, and a curve crossing $a$ transversely is dragged through the full turn. This is the reason the twist is the elementary move of the mapping class group and the elementary operation of the Kirby calculus.

## The Action on the Homology

Let $S = S_g$ be a closed orientable surface of genus $g$, so that $H_1(S;\mathbb{Z})\cong\mathbb{Z}^{2g}$ carries the nondegenerate alternating **intersection form**
$$
i : H_1(S;\mathbb{Z})\times H_1(S;\mathbb{Z})\to\mathbb{Z},
$$
normalised by $i(e_1,e_2) = 1$ on the two curves of a standard torus summand.

**Theorem (the Picard–Lefschetz transvection).** Let $A = [a]\in H_1(S;\mathbb{Z})$ be the class of the curve $a$. Then the operator induced by the Dehn twist on the homology is
$$
(T_a)_* : H_1(S;\mathbb{Z})\to H_1(S;\mathbb{Z}), \qquad (T_a)_*(x) = x + i(A,x)\,A ,
$$
the **transvection** with direction $A$. Equivalently $(T_a)_*(x) = x - i(x,A)A$; the two forms differ by the choice of sign convention for the intersection number, and either is a transvection.

**Proof.** Compute on a basis. The twist fixes every class disjoint from $a$, so it fixes the classes in the kernel of $i(A,-)$; on a curve $b$ crossing $a$ once at a point, the twist drags $b$ through the full turn and replaces it by a curve homologous to $b\cup a$ or $b\cup(-a)$ according to the sign of the crossing, so $(T_a)_*[b] = [b] + i(A,[b])A$. Both sides are bilinear in $x$ and agree on a set of classes generating $H_1$, hence agree everywhere.

**Corollary (the matrix and the order).** In a symplectic basis $e_1,f_1,\dots,e_g,f_g$ of $H_1(S;\mathbb{Z})$ with $i(e_j,f_j) = 1$ and all other pairings zero, the matrix of $(T_a)_*$ is the symplectic transvection
$$
(T_a)_* = I + A\,A^{\dagger}\,J,
$$
where $J$ is the matrix of the intersection form; the matrix is unipotent, with all eigenvalues equal to $1$, and $(T_a)_*^k - I$ has rank one for $k\neq0$, so the transvection has infinite order.

**Proposition (the separating and the non-separating cases).** If $a$ is **non-separating**, then $A\neq0$ and the transvection is a nontrivial unipotent operator; if $a$ is **separating**, then $A = 0$ in $H_1(S;\mathbb{Z})$ and $(T_a)_* = \mathrm{id}$. Consequently every Dehn twist about a separating curve acts trivially on the homology and lies in the Torelli group.

**Proof.** A curve is separating exactly when it is null-homologous, $[a] = 0$, by the classification of curves on a surface; the transvection formula then gives the identity. For a non-separating curve the class $A$ is primitive and nonzero, so $i(A,x)\neq0$ for suitable $x$ and the operator moves it.

**Example (the torus).** For $S = T^2$ with $H_1\cong\mathbb{Z}^2$ and basis $e_1,e_2$ satisfying $i(e_1,e_2) = 1$, the twist about the first curve has $A = e_1$ and
$$
(T_{e_1})_*(m\,e_1 + n\,e_2) = m\,e_1 + n\,e_2 + n\,e_1 = (m+n)e_1 + n\,e_2,
$$
so its matrix is $\begin{pmatrix}1&1\\0&1\end{pmatrix}$. The mapping class group of the torus is $SL_2(\mathbb{Z})$, generated by this matrix and by its transpose, which are the images of the twists about the two coordinate curves.

**Example (a separating twist on the genus-two surface).** On $S_2$ let $a$ be a curve separating off a one-holed torus; then $[a] = 0$ and $T_a$ acts trivially on $H_1(S_2;\mathbb{Z})\cong\mathbb{Z}^4$, although it is a nontrivial mapping class. This is the standard first example of the gap between the mapping class group and its symplectic image, and it is the reason the Torelli group is not trivial.

## The Twist and the Mapping Class Group

The twists are the generators of the mapping class group, and the transvections are the generators of the symplectic group; the two statements are the same statement read at the two levels.

**Definition.** The **mapping class group** $\mathrm{Mod}(S)$ is the group of isotopy classes of orientation-preserving homeomorphisms of $S$, and $\mathrm{Mod}^{\pm}(S)$ the group of all isotopy classes, orientation-preserving or not.

**Theorem (Dehn–Lickorish).** For a closed orientable surface $S_g$ the group $\mathrm{Mod}(S_g)$ is generated by finitely many Dehn twists; concretely, the twists about the curves of a chain of $3g-1$ curves generate $\mathrm{Mod}(S_g)$.

**Theorem (Humphries).** The curves of a chain of $3g-1$ twists may be reduced: $2g+1$ Dehn twists about suitable curves generate $\mathrm{Mod}(S_g)$, and no set of $2g$ or fewer Dehn twists generates it, for $g\geq2$.

**Theorem (the symplectic representation is surjective).** The action on the homology gives a surjective homomorphism
$$
\mathrm{Mod}(S_g)\longrightarrow \operatorname{Sp}\bigl(2g,\mathbb{Z}\bigr), \qquad \bigl[\phi\bigr]\longmapsto \phi_* ,
$$
whose kernel is the **Torelli group** $\mathcal{I}(S_g)$; the images of the Dehn twists are the transvections, and the transvections generate $\operatorname{Sp}(2g,\mathbb{Z})$. For $g = 1$ the map is an isomorphism $\mathrm{Mod}(T^2)\cong SL_2(\mathbb{Z})$.

**Proof sketch.** The image of a homeomorphism preserves the intersection form, so the map is well defined; it is surjective because the transvections generate the symplectic group (this is the elementary generation of $\operatorname{Sp}$ by transvections, a theorem of linear algebra over a principal ideal domain), and the transvections are the images of the twists by the Picard–Lefschetz formula, so the surjectivity follows from the generation of $\mathrm{Mod}$ by twists. The kernel is the Torelli group by definition. The full discussion with the Nielsen–Thurston classification and the geometry of the group is *Mapping Class Groups*.

**Remark (the generators of the Torelli group).** The separating twists are in the kernel by the proposition above, and together with the **bounding pair maps** they generate the Torelli group; this is Johnson's theorem and belongs to *Mapping Class Groups*. The present article keeps only the operator-theoretic part: which twists are visible on the homology and which are not.

## The Twist as an Operation on Other Invariants

**The action on the fundamental group.** For a surface with nonempty boundary and a curve $a$ in it, the twist about $a$ acts on $\pi_1$ by an inner automorphism on one side of $a$ and an inner automorphism on the other: if the fundamental group is split along $a$ into two pieces, the twist conjugates the second factor by the class of $a$ and fixes the first. This is the origin of the description of the mapping class group of a surface with boundary as a subgroup of the automorphism group of a free group, and it is the reason a Dehn twist is not the identity as a map of the fundamental group even when it is trivial on the homology.

**The action on the curve complex.** On the **curve complex** $\mathcal{C}(S)$, whose vertices are the isotopy classes of essential simple closed curves and whose simplices are the sets of disjoint curves, a Dehn twist acts hyperbolically: for every curve $\gamma$ meeting $a$, the translation length of $T_a$ is $2$, so that $d_{\mathcal{C}}(T_a^k\gamma,\gamma)\to\infty$ linearly in $|k|$. The action is realised on the Gromov boundary of $\mathcal{C}(S)$ by a "parabolic" map, and the classification is that of *Mapping Class Groups*; the measure-theoretic description of the boundary is Part III.

**The action on the curve graph of a subsurface / on the Teichmüller space.** The twist acts trivially on the Teichmüller space of a subsurface not containing $a$ and nontrivially on the rest; the precise statement is the "subsurface projection" of *Mapping Class Groups* and *Teichmüller Theory*, and it is a sharpening of the operator description.

**Remark (the higher-dimensional twist).** In a manifold of dimension $n$ a homeomorphism supported near an embedded sphere $S^k\times D^{n-k}$ and acting as a "full twist" on the second factor exists when the topology of the disc permits; the operation is the linking of the sphere and the "sphere twist" of the surgery theory, and its construction in the smooth and piecewise-linear categories belongs to Part III and to *Cobordism and Surgery Theory*. The surface case is the one treated here, and it is the only case in which the operator is a single transvection on the homology.

## Examples and Applications

**Example (the Picard–Lefschetz monodromy).** Let $\pi : E\to D$ be a topological fibre bundle over the disc whose fibre is a surface and whose total space is a manifold with a single singular fibre; the monodromy around the singular point is the Dehn twist about the **vanishing cycle**, and its action on the first homology of the fibre is the transvection $x\mapsto x + i(A,x)A$. This is the geometric content of the Picard–Lefschetz formula; the holomorphic theory of the family belongs to the algebraic geometry of this batch, and the formula is the same operator.

**Example (the twist and the framing of a knot).** In the theory of the trefoil and of the torus knots, the Dehn twists about the two coordinate curves of a Heegaard torus realise the periodic self-homeomorphisms of the ambient orbit; the classification of lens spaces and of the Seifert fibrings is *Lens Spaces* and *Low-Dimensional Topology*, and the elementary input is the transvection formula of this article.

**Example (the twist as a vanishing of a homology class).** On a curve $a$ with $[a]\neq0$ the twist kills nothing on the homology but moves the complementary classes; on a separating curve it is invisible on the homology. The contrast between "$T_a\neq\mathrm{id}$ but $(T_a)_* = \mathrm{id}$" and "$(T_a)_*\neq\mathrm{id}$" is the operator-theoretic statement of the difference between the mapping class group and the symplectic group, and it is the reason the Torelli group is the natural object of study for a classification finer than the homology.

## Summary

A Dehn twist is the homeomorphism of a surface that cuts along a simple closed curve, rotates one side by a full turn and reglues; it is supported in an annulus, fixes the curve pointwise, and has infinite order. Its operator on the first homology is the transvection $(T_a)_*(x) = x + i(A,x)A$ determined by the class $A = [a]$ and the intersection form $i$, a unipotent operator of rank one whose powers move every class crossing $a$; a separating curve has $A = 0$ and its twist acts trivially on the homology, hence lies in the Torelli group. The Dehn twists generate the mapping class group (Dehn–Lickorish; $2g+1$ twists suffice and are minimal for $g\geq2$, Humphries), and their images, the transvections, generate the symplectic group $\operatorname{Sp}(2g,\mathbb{Z})$, so that the symplectic representation $\mathrm{Mod}(S_g)\to\operatorname{Sp}(2g,\mathbb{Z})$ is surjective with kernel the Torelli group. On the fundamental group the twist acts by an inner automorphism on one side of the curve, and on the curve complex it acts hyperbolically with translation length two. The Picard–Lefschetz monodromy of a vanishing cycle is the same transvection.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a\subseteq S$ | a simple closed curve and $N\cong S^1\times[-1,1]$ an annular neighbourhood |
| $T_a$ | the Dehn twist about $a$; supported in $N$, fixing $a$ pointwise |
| $A = [a]\in H_1(S;\mathbb{Z})$ | the homology class of the curve; $A=0$ iff $a$ is separating |
| $i(-,-)$ | the algebraic intersection form on $H_1(S;\mathbb{Z})$ |
| $(T_a)_*(x) = x + i(A,x)A$ | the Picard–Lefschetz transvection, the action on the homology |
| $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ | the matrix of the transvection for the torus in the basis $i(e_1,e_2)=1$ |
| $\mathrm{Mod}(S)$, $\mathrm{Mod}^{\pm}(S)$ | the mapping class group of orientation-preserving (resp. all) isotopy classes |
| $\mathcal{I}(S_g)$ | the Torelli group, the kernel of the symplectic representation |
| $\operatorname{Sp}(2g,\mathbb{Z})$ | the symplectic group; the image of the representation |
| $\mathcal{C}(S)$ | the curve complex; the twist acts with translation length $2$ on it |
| $3g-1$, $2g+1$ | the number of twists in the Dehn–Lickorish chain and the minimal Humphries number |

## Further Reading

- Max Dehn, "Die Gruppe der Abbildungsklassen", *Acta Mathematica* 69 (1938), 135–206, for the original twist and the generation of the mapping class group.
- W. B. R. Lickorish, "A Finite Set of Generators for the Mapping Class Group of a Surface", *Proceedings of the Cambridge Philosophical Society* 60 (1964), 769–778, for the chain of $3g-1$ twists.
- Stephen P. Humphries, "Generators for the Mapping Class Group", in *Topology of Low-Dimensional Manifolds* (Springer Lecture Notes 722, 1979), for the minimal set of $2g+1$ twists.
- Benson Farb and Dan Margalit, *A Primer on Mapping Class Groups* (Princeton University Press, 2012), for the twist, the transvection formula, Lickorish–Humphries and the Torelli group.
- Nikolai Ivanov, *Subgroups of Teichmüller Modular Groups* (American Mathematical Society, 1992), for the rigidity and the generation theorems of the mapping class group.
- Howard Masur and Yair Minsky, "Geometry of the Complex of Curves I", *Inventiones Mathematicae* 138 (1999), 103–149, for the hyperbolic action of the twist on the curve complex and the translation length.
- Dennis Johnson, "The Structure of the Torelli Group I", *Annals of Mathematics* 118 (1983), 423–442, for the generation of the Torelli group by separating twists and bounding pairs.
