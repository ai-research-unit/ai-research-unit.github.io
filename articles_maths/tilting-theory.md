
# __Tilting Theory__

## Introduction

Tilting theory is the study of the modules that behave like the free module of rank one but are allowed to have a projective resolution of length one and to compute the whole module category by a change of the algebra. A **tilting module** $T$ over a finite-dimensional algebra $A$ is a module with projective dimension at most one, with $\operatorname{Ext}^1_A(T,T)=0$, and with an exact sequence $0\to A\to T_0\to T_1\to0$ in which $T_0,T_1$ are direct sums of summands of $T$. The endomorphism algebra $B=\operatorname{End}_A(T)^{\mathrm{op}}$ is the **tilted algebra**, and the functor
$$
\operatorname{RHom}_A(T,-):D^b(A)\to D^b(B)
$$
is an equivalence of triangulated categories. In this way two algebras with very different module categories can have the same derived category, and the representation theory of one is transported to the other: the tilting module turns into the free module, the indecomposable summands of $T$ into the indecomposable projectives of $B$, and the modules that are not in the torsion-free class disappear from the module category while remaining in the derived one.

The theory has three faces. The **homological** face is the derived equivalence above and the invariance of the derived category under tilting. The **module-theoretic** face is the Brenner–Butler theorem, which describes the effect of a tilting module as an equivalence between a torsion class in the module category of $A$ and a torsion-free class in the module category of $B$, together with the induced maps on the Grothendieck groups. The **combinatorial** face is the APR construction, which obtains a tilting module over the path algebra of a quiver by reflecting a sink or a source, and which therefore realises the change of orientation of a quiver as a derived equivalence. The cluster-tilting objects and the cluster algebras are the further development of the last face.

This article develops tilting modules and tilted algebras, the derived equivalence and its construction, the Brenner–Butler theorem and the torsion pairs, the APR tilting modules and the change of orientation, the classification of the tilting modules over a hereditary algebra, and the examples of the quivers of type $A$ and of the Kronecker quiver. It follows *Derived Categories*, *Auslander–Reiten Theory*, *Ext and Tor*, *Quiver Representations and Representation Type* and *K-Theory of Rings*, and it prepares.

Throughout, $k$ is a field, $A$ and $B$ are finite-dimensional $k$-algebras, modules are finite-dimensional left modules, and $D^b(A)$ is the bounded derived category of *Derived Categories* with the shift and the triangles of that article. The functor $\operatorname{RHom}$ and the Grothendieck group $K_0$ are those of *Derived Functors*, *Ext and Tor* and *K-Theory of Rings*. The algebra is finite-dimensional only where the tilting theory of finite-dimensional algebras requires it, and this is flagged; the abstract definition of a tilting module over a ring is given first. No topology or form occurs.

## Tilting Modules

### The Definition

**Definition.** Let $A$ be a ring. A left $A$-module $T$ is **tilting** if the following three conditions hold:
1. the projective dimension of $T$ is at most one;
2. $\operatorname{Ext}^1_A(T,T)=0$;
3. there is an exact sequence $0\to A\to T_0\to T_1\to0$ in which $T_0$ and $T_1$ are direct summands of finite direct sums of copies of $T$, that is, $T_0,T_1\in\operatorname{add}T$.

A module satisfying only the first two conditions is **partial tilting**; a partial tilting module with $n$ pairwise non-isomorphic indecomposable summands, where $n$ is the rank of $K_0(A)$, is automatically tilting when $A$ is finite-dimensional.

**Proposition.** Let $T$ be a tilting $A$-module and let $B=\operatorname{End}_A(T)^{\mathrm{op}}$ act on $T$ on the right. Then:
- the functor $\operatorname{Hom}_A(T,-):\mathrm{Mod}\,A\to\mathrm{Mod}\,B$ is left exact, and its right derived functor $\operatorname{RHom}_A(T,-)$ is an equivalence $D^b(A)\to D^b(B)$;
- $T$ is a projective generator of the category of $B$-modules under the equivalence, and the inverse equivalence is $-\otimes^{\mathbf L}_BT$;
- the functors induce mutually inverse isomorphisms $\operatorname{Ext}^i_A(M,N)\to\operatorname{Ext}^i_B(\operatorname{RHom}_A(T,M),\operatorname{RHom}_A(T,N))$ for all $i$ and all modules in the derived categories.

*Proof (in outline).* The module $T$ is a generator (condition 3) with a length-one projective resolution by condition 1, so the functor $\operatorname{Hom}_A(T,-)$ is exact on the subcategory of $\operatorname{add}T$ and the adjunction with $-\otimes_BT$ is an equivalence on that subcategory; conditions 1 and 2 propagate along the resolution and show that $\operatorname{RHom}_A(T,-)$ kills only the complexes that are already zero in the derived category, and that its right adjoint $-\otimes^{\mathbf L}_BT$ is its inverse. $\square$

**Definition.** With the notation of the proposition, $B=\operatorname{End}_A(T)^{\mathrm{op}}$ is the **tilted algebra** of $T$, and the tilting module $T$ is a **bimodule** $_{B}T_{A}$; two algebras $A$ and $B$ related by a tilting module are **derived equivalent**, and the equivalence of the proposition is a **tilting equivalence**.

**Example.** The free module $A$ is a tilting module with $T_0=A$, $T_1=0$, and the tilted algebra is $A$ itself. Direct sums of copies of $A$ give trivial tilting modules.

**Example.** For the quiver $1\to2\to3$ the reflection at the sink $3$ replaces the simple projective $P_3=S_3$ by a module involving the other end of the Auslander–Reiten quiver, and the APR tilting module has three pairwise non-isomorphic indecomposable summands; the module $P_1\oplus P_2\oplus I_2$, where $I_2=[1,2]$ is the injective envelope of $S_2$, is a tilting module with $\operatorname{Ext}^1_{kQ}(T,T)=0$, and its tilted algebra is the path algebra of the quiver $1\to2\leftarrow3$, as the theorem below states.

### The Brenner–Butler Theorem

**Definition.** A **torsion pair** in $\mathrm{mod}\,A$ is a pair $(\mathcal{T},\mathcal{F})$ of full subcategories such that $\operatorname{Hom}_A(\mathcal{T},\mathcal{F})=0$, every module $M$ sits in a short exact sequence $0\to tM\to M\to M/tM\to0$ with $tM\in\mathcal{T}$ and $M/tM\in\mathcal{F}$, and $\mathcal{T}$ is closed under quotients and extensions; the module $tM$ is the **torsion part** of $M$. A **torsion-free class** is the second member of a torsion pair.

**Theorem (Brenner–Butler).** Let $T$ be a tilting $A$-module and $B=\operatorname{End}_A(T)^{\mathrm{op}}$. Let $\mathcal{T}$ be the full subcategory of the $A$-modules $M$ with $\operatorname{Ext}^1_A(T,M)=0$, and let $\mathcal{Y}$ be the full subcategory of the $B$-modules $N$ with $\operatorname{Tor}_1^B(N,T)=0$. Then $\mathcal{T}$ is a torsion class in $\mathrm{mod}\,A$, with torsion-free class the $A$-modules $M$ with $\operatorname{Hom}_A(T,M)=0$, and $\mathcal{Y}$ is a torsion-free class in $\mathrm{mod}\,B$, with torsion class the $B$-modules $N$ with $N\otimes_BT=0$; the functor $\operatorname{Hom}_A(T,-)$ restricts to an equivalence $\mathcal{T}\to\mathcal{Y}$ with inverse $-\otimes_BT$, and it induces isomorphisms
$$
K_0(\mathcal{T})\cong K_0(\mathcal{Y}),\qquad K_0(A)\cong K_0(B),
$$
on the Grothendieck groups, so that the derived equivalence preserves the number of indecomposable projective modules and the numerical invariants of the module category.

*Proof (in outline).* The vanishing of $\operatorname{Ext}^1_A(T,M)$ for $M\in\mathcal{T}$ makes the functor $\operatorname{Hom}_A(T,-)$ exact on $\mathcal{T}$; adjointness with $-\otimes_BT$ gives the inverse on $\mathcal{Y}$, and the two conditions $\operatorname{Ext}^1_A(T,M)=0$ and $\operatorname{Tor}_1^B(N,T)=0$ are matched by the tilting conditions. The closure properties and the existence of the torsion sequence are checked from the length-one projective resolution of $T$. The group isomorphisms follow from the additivity of the functors and from the fact that $T$ and the free module generate the same class in $K_0$. $\square$

**Example.** For the Kronecker quiver with two arrows $1\rightrightarrows2$ the indecomposable projectives are $P_1$ of dimension vector $(1,2)$ and $P_2$ of dimension vector $(0,1)$, and $P_1\oplus P_2$ is a tilting module with two indecomposable summands. Further tilting modules are obtained by the APR tilts at the two vertices and by iterating them; the tilted algebras are the path algebras of the two orientations of the underlying graph, which are isomorphic. For every tilting module the $\operatorname{Ext}^1$ groups between distinct indecomposable summands vanish, and the regular indecomposables of the tubes never occur as summands, because a regular module has a self-extension in its tube.

## The APR Tilting Modules and Change of Orientation

### Reflection at a Sink or a Source

**Definition.** Let $Q$ be a finite acyclic quiver and let $i$ be a **sink** (all arrows at $i$ point into $i$) or a **source** (all arrows point out of $i$). The **reflected quiver** $s_iQ$ has the same vertices and the same arrows with the orientations of the arrows at $i$ reversed; it is again acyclic, and the underlying graph is unchanged.

**Theorem (APR).** Let $Q$ be a finite acyclic quiver, $A=kQ$, and $i$ a sink or a source. Then there is a tilting $A$-module $T_i$, obtained by applying the inverse reflection functor at $i$ to the indecomposable projective $P_i$ of the reflected algebra $k(s_iQ)$, with the following properties:
- $T_i$ has $n$ pairwise non-isomorphic indecomposable summands, one for each vertex of $Q$;
- $\operatorname{Ext}^1_A(T_i,T_i)=0$, and $\operatorname{End}_A(T_i)^{\mathrm{op}}\cong k(s_iQ)$, the path algebra of the quiver reflected at $i$;
- the functor $\operatorname{RHom}_A(T_i,-)$ is an equivalence $D^b(kQ)\cong D^b(k(s_iQ))$.

The summands are the images of the indecomposable modules of the reflected algebra under the inverse reflection functor, and they are not in general the projectives $P_j$, $j\neq i$: the summand replacing $P_i$ is a module at the opposite end of the Auslander–Reiten quiver, an indecomposable which is projective only in the trivial cases. For the quiver $1\to2$ the sink $2$ gives $P_2$ injective, so the inverse reflection leaves $P_2$ alone and the tilt is the regular module $P_1\oplus P_2$, with endomorphism algebra $k(1\leftarrow2)\cong k(1\to2)$; here $P_1=S_1$, and the simple at the source is not an independent summand. For $1\to2\to3$ the tilt at the sink $3$ has three pairwise non-isomorphic summands and endomorphism algebra of dimension $5$, namely $P_1\oplus P_2\oplus I_2$ with $I_2=[1,2]$, and the tilt at the source $1$, computed in the opposite algebra where $1$ is a sink, has endomorphism algebra $k(1\leftarrow2\to3)$, of the same dimension.

Consequently two acyclic quivers with the same underlying graph have derived equivalent path algebras, and the reflection functors of *Quiver Representations and Representation Type* induce an equivalence between the full subcategories of the modules vanishing at the reflected vertex on the two sides.

*Proof (in outline).* The inverse reflection functor at $i$ is an equivalence between the full subcategories of the modules over $k(s_iQ)$ and over $kQ$ that vanish at the reflected vertex, and the module $T_i$ is built from the images of the projective modules of $k(s_iQ)$; each summand is projective or has a length-one projective resolution. The sum has no self-extensions because the extension groups between the distinct summands vanish by the reflection, and it generates the module category; the endomorphism algebra is computed from the arrow reversal, since the reflection reverses each arrow at $i$ and the radicals of the Hom spaces between the summands reproduce the path algebra of $s_iQ$. The endomorphism algebra is computed on the arrow reversal: the reflection reverses each arrow at $i$, and the radicals of the Hom spaces between the summands reproduce the path algebra of $s_iQ$. $\square$

**Corollary.** Two acyclic quivers with the same underlying graph have path algebras with equivalent derived categories, and the equivalence is realised by a composite of APR tilts. The number of indecomposable summands of every tilting module is the number of vertices, and the Grothendieck group is free of that rank.

**Example.** For the quiver $1\to2$ the reflection at the sink $2$ produces the quiver $1\leftarrow2$; the two path algebras are isomorphic (both have basis $e_1,e_2,a$ with $a^2=0$), and the regular module $T=P_1\oplus P_2$ has endomorphism algebra $k(1\leftarrow2)\cong k(1\to2)$, so the derived equivalence is the identity on the isomorphism classes. For the quiver $1\to2\to3$ the reflection at the sink $3$ produces $1\to2\leftarrow3$, and the APR tilting module has three pairwise non-isomorphic indecomposable summands: the module $T=P_1\oplus P_2\oplus I_2$, with $I_2=[1,2]$ the injective envelope of $S_2$, satisfies $\operatorname{Ext}^1_{kQ}(T,T)=0$ and has $\operatorname{End}_{kQ}(T)$ of dimension $5$ with radical-quotient quiver $1\to2\leftarrow3$, so that $\operatorname{End}_{kQ}(T)^{\mathrm{op}}\cong k(1\to2\leftarrow3)$; the derived categories of the two orientations are equivalent, although the two algebras are not isomorphic (their dimensions are $6$ and $5$).

### The Ext-Algebra and the Torsion Pairs

**Proposition.** Let $T$ be a tilting $A$-module with endomorphism algebra $B$. Then the functor $\operatorname{Hom}_A(T,-)$ carries the indecomposable summands of $T$ to the indecomposable projectives of $B$, and it carries the other indecomposables of $A$ either to $B$-modules or to complexes with cohomology in two degrees. The **Ext-algebra** $\bigoplus_i\operatorname{Ext}^i_A(T,T)$ is the graded endomorphism algebra of $T$ in the derived category and is isomorphic to $B$ concentrated in degree zero.

*Proof.* The first statement is the definition of the equivalence on the additive closure of $T$. The second follows from the length of the projective resolution of $T$: a module with a two-step resolution maps to a complex with at most two cohomology degrees. The Ext-algebra statement is that $T$ has no self-extensions and the endomorphisms are the degree-zero part. $\square$

**Example.** For a hereditary algebra $A=kQ$ the tilting modules are exactly the direct sums of $n$ pairwise non-isomorphic indecomposables $T_1,\dots,T_n$ with $\operatorname{Ext}^1_A(T_i,T_j)=0$ for all $i,j$; their number is finite when $Q$ is a Dynkin quiver, and infinite when $Q$ is the Kronecker quiver.

## Tilting and the Derived Category

**Theorem (Happel).** Let $A$ be a finite-dimensional hereditary $k$-algebra. Two hereditary algebras are derived equivalent if and only if their quivers have the same underlying graph, and every derived equivalence between hereditary algebras is a composite of APR tilts up to isomorphism. The derived category $D^b(kQ)$ determines the underlying graph of $Q$, and hence the representation type of $Q$: two orientations of the same graph are derived equivalent, and the Auslander–Reiten structures of their module categories are related by the tilting.

*Proof (in outline).* The APR tilts provide the derived equivalences for two orientations, and the connectedness of the graph under the reflections gives all orientations. The converse uses the invariance of the Grothendieck group and of the Euler characteristic under a derived equivalence to recover the graph. $\square$

**Remark.** The tilting theory of finite-dimensional algebras is the algebraic model of the derived equivalences of coherent sheaves on algebraic varieties, where tilting complexes and Fourier–Mukai transforms play the same role; the geometric theory belongs to Part II, where the sheaves and their derived categories are available, and is not used here. The cluster-tilting objects are the analogues of the tilting modules in the cluster category, and the cluster algebras are their combinatorial shadow.

## Tilting Complexes and Derived Equivalences

**Definition.** Let $A$ be a ring. A **tilting complex** is a bounded complex $T$ of finitely generated projective $A$-modules with $\operatorname{Hom}_{D^b(A)}(T,T[i])=0$ for $i\neq0$, such that the smallest triangulated subcategory of $D^b(A)$ containing $T$ and closed under direct summands is all of $D^b(A)$. A single module $T$ placed in degree zero is a tilting complex exactly when it is a tilting module in the sense above.

**Theorem (Rickard).** Two rings $A$ and $B$ have equivalent bounded derived categories if and only if there is a tilting complex $T$ over $A$ with $\operatorname{End}_{D^b(A)}(T)\cong B$; the equivalence is $X\mapsto\operatorname{RHom}_A(T,X)$ with inverse $-\otimes^{\mathbf L}_BT$. Consequently derived equivalence is an equivalence relation on rings, it preserves the Grothendieck group and the Hochschild homology, and for finite-dimensional algebras it preserves the number of isomorphism classes of simple modules.

*Proof (in outline).* The functor $\operatorname{RHom}_A(T,-)$ is fully faithful when $T$ is a compact generator of the derived category, and the compact generators of $D^b(A)$ are the objects with finitely generated cohomology in each degree; the vanishing of the self-extensions makes the endomorphism algebra in the derived category a ring whose module category is equivalent to $D^b(A)$. The inverse functor is the left adjoint $-\otimes^{\mathbf L}_BT$, and the preservation statements follow because both functors are equivalences of triangulated categories. $\square$

**Example.** For a finite-dimensional algebra the tilting complexes include the two-term complexes $P_1\to P_0$ of a tilting module, and the derived equivalences they induce are the tilting equivalences above. The analogue for a smooth projective variety is a tilting sheaf, whose endomorphism algebra is in general infinite-dimensional; the geometric theory belongs to Part II.

**Proposition.** The Grothendieck group $K_0(A)$ of *K-Theory of Rings* is invariant under derived equivalence, and under a tilting module the class of the tilting module generates the group. When $A$ is finite-dimensional and the rank of a projective module is defined, the alternating sum of the ranks of the terms of a projective resolution induces a homomorphism $K_0(A)\to\mathbb{Z}$, and this homomorphism is preserved by tilting.

*Proof.* The derived equivalence is an equivalence of triangulated categories, so it induces an isomorphism of the Grothendieck groups, which are computed from the triangulated structure; for a finite-dimensional algebra the Grothendieck group of the derived category identifies with $K_0(A)$. The rank homomorphism is additive over exact sequences and therefore factors through $K_0$. $\square$

## Summary

A tilting module over a ring is a module of projective dimension at most one with no self-extensions and with a two-term presentation of the free module; over a finite-dimensional algebra its endomorphism algebra is the tilted algebra, and the functor $\operatorname{RHom}_A(T,-)$ is an equivalence of bounded derived categories. The Brenner–Butler theorem describes the effect in the module category: the modules with $\operatorname{Ext}^1_A(T,-)$ vanishing form a torsion class, the modules over the tilted algebra with $\operatorname{Tor}_1(-,T)$ vanishing form the corresponding torsion-free class, and the functor is an equivalence between them inducing an isomorphism of Grothendieck groups. The APR construction reflects a sink or a source of an acyclic quiver and produces a tilting module whose tilted algebra is the path algebra of the reflected quiver, so that the orientation of a quiver is invisible to the derived category; for a hereditary algebra the derived equivalence classes are exactly the underlying graphs, and the tilting modules over a simply laced Dynkin quiver are finite in number.

Tilting theory is the bridge between the representation theory of *Quiver Representations and Representation Type* and *Auslander–Reiten Theory* and the cluster theory, where the tilting objects become the cluster-tilting objects of a cluster category and the tilting modules over the quivers of finite type correspond to the clusters. The geometric tilting theory, with its complexes and transforms, is deferred to Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T$ | tilting module |
| $\operatorname{add}T$ | direct summands of finite direct sums of $T$ |
| $B=\operatorname{End}_A(T)^{\mathrm{op}}$ | tilted algebra |
| $\operatorname{RHom}_A(T,-)$, $-\otimes^{\mathbf L}_BT$ | the derived equivalence and its inverse |
| $(\mathcal{T},\mathcal{F})$ | torsion pair, torsion and torsion-free classes |
| $\mathcal{Y}$ | $B$-modules $N$ with $\operatorname{Tor}_1^B(N,T)=0$ |
| $tM$ | torsion part of $M$ |
| $s_iQ$ | quiver reflected at the vertex $i$ |
| $D^b(A)$ | bounded derived category |
| $K_0(A)$ | Grothendieck group |
| $P_i$, $I_i$, $S_i$ | indecomposable projective, injective, simple module |
| $\tau$ | Auslander–Reiten translation |





## Further Reading

- Michel Auslander, María Inés Platzeck and Idun Reiten, "Coxeter functors without diagrams", *Transactions of the American Mathematical Society* 250 (1979), 1–46, for the APR tilting modules and the reflection functors.
- Sheila Brenner and Michael C. R. Butler, "Generalizations of the Bernstein–Gelfand–Ponomarev reflection functors", in *Representation Theory II* (Springer Lecture Notes in Mathematics 832, 1980), for the Brenner–Butler theorem.
- Dieter Happel, *Triangulated Categories in the Representation Theory of Finite-Dimensional Algebras* (Cambridge University Press, 1988), for the derived equivalence and the tilting theory.
- Dieter Happel and Claus M. Ringel, "Tilted algebras", *Transactions of the American Mathematical Society* 274 (1982), 399–443, for the classification of the tilted algebras and the torsion theory.
- Bernhard Keller, "Deriving DG categories", *Annales Scientifiques de l'École Normale Supérieure* 27 (1994), 63–102, for the differential graded enhancement of the derived equivalences.
- Claus M. Ringel, "Tame algebras and integral quadratic forms", *Springer Lecture Notes in Mathematics* 1099 (1984), for the tilting modules over a hereditary algebra.
- Jeremy Rickard, "Morita theory for derived categories", *Journal of the London Mathematical Society* 39 (1989), 436–456, for the general derived equivalences and the tilting complexes.
