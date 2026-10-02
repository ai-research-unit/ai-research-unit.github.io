# __The Transpose of a Linear Map__

## Introduction

To a linear map $T : V \to W$ the dual construction attaches a linear map in the opposite direction on the dual spaces, $T^{\mathsf{T}} : W^{*} \to V^{*}$, defined by evaluating a functional against the image of a vector. The construction is elementary, but it is the source of three things that the corpus uses everywhere: the contravariant functor $(-)^{*}$ on linear spaces, the identification of a finite-dimensional space with its double dual, and the anti-isomorphism that makes the endomorphism algebra isomorphic to its opposite. This article develops the transpose for itself, with the elementary properties, the double dual, the matrix description and the naturality that make it a functor rather than an assignment.

The dual space, the dual basis and the identification $\operatorname{Hom}_F(V,W) \cong M_{m\times n}(F)$ after bases are fixed belong to *Linear Maps and Matrices*, and are not re-derived. The rank, the kernel and the image of a linear map, and the rank–nullity theorem, are there too. The endomorphism algebra $E = \operatorname{End}_F(V)$, its opposite and its deferred anti-isomorphism are *Endomorphisms of a Linear Space*, the preceding article of this group. What is established here is the transpose as a map between dual spaces, its interaction with kernel and image through annihilators, its matrix form, the double dual and the naturality that make the transposition a functor.

The article assumes a field $F$, finite-dimensional $F$-linear spaces, the dual space $V^{*} = \operatorname{Hom}_F(V,F)$, and the elementary facts about linear maps. It uses no form, no norm and no distance. The **adjoint** of an operator with respect to a non-degenerate pairing is a different operation, one that reverses the direction of a pairing rather than passing to the dual, and it is treated in *The Adjoint of an Endomorphism*; nothing of that article is anticipated here.

## The Dual Map

### Definition and Elementary Properties

**Definition.** Let $V$ and $W$ be $F$-linear spaces and let $T : V \to W$ be linear. The **transpose** of $T$ is the linear map

$$
T^{\mathsf{T}} : W^{*} \longrightarrow V^{*}, \qquad (T^{\mathsf{T}}\varphi)(v) = \varphi(Tv) ,
$$

that is, $T^{\mathsf{T}}\varphi = \varphi \circ T$.

**Proposition (well defined and linear).** $T^{\mathsf{T}}$ is $F$-linear, and it is the unique linear map $W^{*} \to V^{*}$ with $(T^{\mathsf{T}}\varphi)(v) = \varphi(Tv)$ for all $\varphi,v$.

**Proof.** The composite of a linear map $V \to W$ and a linear functional $W \to F$ is linear, so $T^{\mathsf{T}}\varphi \in V^{*}$; for $\varphi,\psi$ and $\lambda \in F$ one has $(T^{\mathsf{T}}(\varphi+\lambda\psi))(v) = (\varphi+\lambda\psi)(Tv) = \varphi(Tv)+\lambda\psi(Tv)$, so $T^{\mathsf{T}}(\varphi+\lambda\psi) = T^{\mathsf{T}}\varphi + \lambda T^{\mathsf{T}}\psi$. Uniqueness holds because two maps agreeing on every $v$ agree.

**Proposition (the elementary laws).** For linear maps $S : U \to V$ and $T : V \to W$,

$$
(T \circ S)^{\mathsf{T}} = S^{\mathsf{T}} \circ T^{\mathsf{T}}, \qquad
(\mathrm{id}_V)^{\mathsf{T}} = \mathrm{id}_{V^{*}}, \qquad
(\lambda T)^{\mathsf{T}} = \lambda\, T^{\mathsf{T}} .
$$

**Proof.** For the first, $((T S)^{\mathsf{T}}\varphi)(u) = \varphi(TSu) = (T^{\mathsf{T}}\varphi)(Su) = (S^{\mathsf{T}}T^{\mathsf{T}}\varphi)(u)$ for every $u$, and the maps agree. The other two are immediate from the definitions.

**Remark (contravariance).** The first law shows that $(-)^{\mathsf{T}}$ reverses the order of composition: the transposition is a **contravariant** functor from $F$-linear spaces with linear maps to themselves. An isomorphism $T$ has transpose $T^{-1^{\mathsf{T}}} = (T^{\mathsf{T}})^{-1}$, and the transpose of an injective or a surjective map is respectively surjective or injective, by the next proposition.

### Kernel, Image and Annihilators

**Definition.** For a subspace $U \subseteq V$ the **annihilator** of $U$ is

$$
U^{0} = \{\varphi \in V^{*} : \varphi(u) = 0 \text{ for all } u \in U\} .
$$

**Proposition (the annihilator is a subspace of the complementary dimension).** $U^{0}$ is a subspace of $V^{*}$ and $\dim_F U^{0} = \dim_F V - \dim_F U$.

**Proof.** That $U^{0}$ is a subspace is immediate. Choose a basis of $U$ and extend it to a basis $v_1,\dots,v_n$ of $V$; the dual basis $\varphi^{i}$ has $\varphi^{i}(v_j) = \delta^{i}_{j}$, and a functional annihilates $U$ exactly when its coefficients on the functionals $\varphi^{1},\dots,\varphi^{r}$ vanish, where $r=\dim_F U$; hence the annihilator has the basis $\varphi^{r+1},\dots,\varphi^{n}$ and dimension $n-r$. This is *Linear Maps and Matrices*.

**Proposition (the transpose through kernel and image).** For a linear $T : V \to W$,

$$
\ker T^{\mathsf{T}} = (\operatorname{im}T)^{0}, \qquad \operatorname{im}T^{\mathsf{T}} = (\ker T)^{0} .
$$

**Proof.** $T^{\mathsf{T}}\varphi = 0$ means $\varphi(Tv) = 0$ for all $v$, that is, $\varphi$ annihilates $\operatorname{im}T$; this is the first identity. For the second, a functional of the form $T^{\mathsf{T}}\varphi$ vanishes on $\ker T$, so $\operatorname{im}T^{\mathsf{T}} \subseteq (\ker T)^{0}$; the two spaces have the same dimension, because $\dim\operatorname{im}T^{\mathsf{T}} = \dim W^{*} - \dim(\operatorname{im}T)^{0} = \dim\operatorname{im}T$ by rank–nullity, while $\dim(\ker T)^{0} = \dim V - \dim\ker T = \dim\operatorname{im}T$. Equal dimensions and a containment give equality.

**Corollary (the rank is preserved).** $\operatorname{rk}T^{\mathsf{T}} = \operatorname{rk}T$. Consequently $T$ is injective if and only if $T^{\mathsf{T}}$ is surjective, and $T$ is surjective if and only if $T^{\mathsf{T}}$ is injective.

**Proof.** From $\operatorname{im}T^{\mathsf{T}} = (\ker T)^{0}$ and the dimension formula, $\operatorname{rk}T^{\mathsf{T}} = \dim V - \dim\ker T = \operatorname{rk}T$.

## The Double Dual

### The Evaluation Map

**Definition.** The **double dual** of $V$ is $V^{**} = (V^{*})^{*}$, and the **evaluation** at $v \in V$ is the functional $\mathrm{ev}_v \in V^{**}$ on $V^{*}$ given by $\mathrm{ev}_v(\varphi) = \varphi(v)$; the assignment $\mathrm{ev} : V \to V^{**}$, $v \mapsto \mathrm{ev}_v$, is the evaluation map.

**Proposition.** $\mathrm{ev}$ is linear and injective for every $V$; if $V$ is finite-dimensional then $\mathrm{ev}$ is an isomorphism.

**Proof.** For $v,w \in V$ and $\lambda \in F$, $\mathrm{ev}_{v+\lambda w}(\varphi) = \varphi(v+\lambda w) = \varphi(v)+\lambda\varphi(w) = (\mathrm{ev}_v + \lambda\,\mathrm{ev}_w)(\varphi)$, so $\mathrm{ev}$ is linear. If $v \neq 0$, extend $v$ to a basis and let $\varphi$ be the first dual functional; then $\mathrm{ev}_v(\varphi) = \varphi(v) = 1 \neq 0$, so $\mathrm{ev}_v \neq 0$ and the map is injective. In finite dimension $\dim_F V^{**} = \dim_F V^{*} = \dim_F V$, so injective implies bijective.

**Remark (canonical, not a choice).** The map $\mathrm{ev}$ uses no basis and no bilinear pairing; it is natural, whereas an isomorphism $V \to V^{*}$ requires the choice of a basis or a non-degenerate pairing, and the pairing version belongs to the adjoint articles. The double dual is the reason the transpose is a functor and not merely an order-reversing assignment on maps.

### The Transpose of the Transpose

**Proposition.** For a linear $T : V \to W$, the maps $\mathrm{ev}_W \circ T$ and $T^{\mathsf{TT}} \circ \mathrm{ev}_V$ are equal, $T^{\mathsf{TT}}\,\mathrm{ev}_V = \mathrm{ev}_W\,T$, so that under the identifications $V \cong V^{**}$ and $W \cong W^{**}$ the double transpose is $T$.

**Proof.** For $v \in V$ and $\psi \in W^{*}$ one has $(T^{\mathsf{TT}}\mathrm{ev}_v)(\psi) = \mathrm{ev}_v(T^{\mathsf{T}}\psi) = (T^{\mathsf{T}}\psi)(v) = \psi(Tv) = \mathrm{ev}_{Tv}(\psi)$, so $T^{\mathsf{TT}}\mathrm{ev}_v = \mathrm{ev}_{Tv}$. Reading this for all $v$ gives the identity.

**Corollary (no information is lost in finite dimension).** For finite-dimensional $V$ and $W$, the assignment $T \mapsto T^{\mathsf{T}}$ is a bijection

$$
\operatorname{Hom}_F(V,W) \longrightarrow \operatorname{Hom}_F(W^{*},V^{*}) ,
$$

natural in $V$ and $W$, and it is an isomorphism of linear spaces.

**Proof.** The assignment is linear by the elementary laws and it is injective because $T^{\mathsf{T}}=0$ forces $\varphi \circ T = 0$ for every $\varphi$, hence $T = 0$; the domain and the target have the same dimension, namely $\dim_F V\dim_F W$, so it is bijective.

## Matrices and the Opposite Algebra

### The Matrix of the Transpose

Fix bases $\mathcal{B}$ of $V$ and $\mathcal{C}$ of $W$, and let $\mathcal{B}^{*},\mathcal{C}^{*}$ be the dual bases. If $T$ has matrix $A = [T]^{\mathcal{C}}_{\mathcal{B}}$, of size $(\dim W)\times(\dim V)$, then $T^{\mathsf{T}}$ has matrix

$$
[T^{\mathsf{T}}]^{\mathcal{B}^{*}}_{\mathcal{C}^{*}} = A^{\mathsf{T}} ,
$$

the transpose matrix, of size $(\dim V)\times(\dim W)$, whose $(i,j)$ entry is $A_{ji}$. This is the computation of *Linear Maps and Matrices*: the $j$-th coefficient of $T^{\mathsf{T}}\varphi^{i}$ is $\varphi^{i}(Tv_j) = A_{ij}$.

### The Anti-Isomorphism of the Endomorphism Algebra

**Theorem.** For a finite-dimensional $V$, the transpose restricts to a bijection $E \to E$ on the endomorphism algebra $E = \operatorname{End}_F(V) \cong \operatorname{Hom}_F(V^{*},V^{*})$, and it is an anti-isomorphism

$$
(A B)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}} , \qquad (\mathrm{id}_V)^{\mathsf{T}} = \mathrm{id}_V , \qquad (A + \lambda B)^{\mathsf{T}} = A^{\mathsf{T}} + \lambda B^{\mathsf{T}} .
$$

Under the identification of $E$ with $\operatorname{End}_F(V^{*})$ it is an isomorphism $E \to E^{\mathrm{op}}$, whence $E \cong E^{\mathrm{op}}$ as $F$-algebras.

**Proof.** The identifications are those of the double-dual corollary, applied to $W=V$; the laws are the elementary laws applied to composites of endomorphisms, the associativity of composition giving the reversal. That $E \cong E^{\mathrm{op}}$ follows by composing the anti-isomorphism with the identity of the underlying linear space, which is an isomorphism $E^{\mathrm{op}} \to E$ of algebras; this discharges the deferred statement of *Endomorphisms of a Linear Space*.

**Corollary.** The transpose of a matrix is an anti-automorphism of $M_n(F)$; the transpose of an endomorphism has the same rank, trace and determinant, and the same characteristic polynomial, so the transposition acts as the identity on the spectrum of an endomorphism.

**Proof.** Rank is preserved by the corollary above; the trace and the determinant are the sums and products of diagonal or of all entries and are invariant under transposition of the matrix, and the characteristic polynomial $\det(xI-A) = \det(xI-A)^{\mathsf{T}} = \det(xI-A^{\mathsf{T}})$ is unchanged.

## Naturality

**Proposition (naturality of the transposition).** For a linear $T : V \to W$ and linear functionals, the construction is natural: if $U \xrightarrow{S} V \xrightarrow{T} W$ is a composable pair then $(TS)^{\mathsf{T}} = S^{\mathsf{T}}T^{\mathsf{T}}$, and for the identity the transposition satisfies $(\mathrm{id})^{\mathsf{T}} = \mathrm{id}$. Equivalently, the transposition is a contravariant functor on the category of finite-dimensional $F$-linear spaces, and the evaluation maps $\mathrm{ev}_V$ assemble into a natural isomorphism $\mathrm{id} \to (-)^{**}$.

**Proof.** The composition law and the identity law are the elementary laws; naturality of $\mathrm{ev}$ is the identity $T^{\mathsf{TT}}\mathrm{ev}_V = \mathrm{ev}_W T$ of the double-dual proposition, read as the commutativity of the square with $T$ on the top and $T^{\mathsf{TT}}$ on the bottom.

**Remark (what naturality buys).** Because the transposition is natural, statements about a linear map may be transported to its transpose without a choice of bases: the rank, the injectivity and the surjectivity are shared by transposition and dualisation, and the kernel and image of the transpose are the annihilators of the image and the kernel. This is the ordinary linear algebra of duality, and it is what makes the dual space an invariant of the linear structure and not a coordinate gadget.

**Remark (transpose and adjoint are different).** The transpose always exists and needs no extra datum; it passes from $V \to W$ to $W^{*} \to V^{*}$, reversing the arrow. The adjoint is defined only with respect to a non-degenerate pairing on a single space, passes from $V \to V$ to $V \to V$, and preserves the direction; when a pairing is used to identify $V$ with $V^{*}$ the two constructions are related, and that relation, together with the involutions it defines on $\operatorname{End}_F(V)$, is the subject of *The Adjoint of an Endomorphism* and *Involutions of the Endomorphism Algebra*.

## Summary

The transpose of a linear map $T : V \to W$ is the linear map $T^{\mathsf{T}} : W^{*} \to V^{*}$ given by $T^{\mathsf{T}}\varphi = \varphi \circ T$. It is additive and homogeneous, it reverses composition, $(TS)^{\mathsf{T}} = S^{\mathsf{T}}T^{\mathsf{T}}$, and it carries the identity to the identity; it is therefore a contravariant functor. Its kernel is the annihilator of the image of $T$, its image is the annihilator of the kernel, and it preserves the rank, so it turns injective maps into surjective ones and conversely. The evaluation map $\mathrm{ev} : V \to V^{**}$, $\mathrm{ev}_v(\varphi) = \varphi(v)$, is linear and injective, and an isomorphism in finite dimension; it is natural, and it identifies the double transpose $T^{\mathsf{TT}}$ with $T$, so that transposition is a bijection $\operatorname{Hom}_F(V,W) \to \operatorname{Hom}_F(W^{*},V^{*})$ and a natural isomorphism $\mathrm{id} \to (-)^{**}$. In a basis the transpose is the transpose matrix, and on endomorphisms it is an anti-automorphism of $E = \operatorname{End}_F(V)$, which identifies $E$ with its opposite algebra and preserves rank, trace, determinant and characteristic polynomial. The transpose needs no extra datum, unlike the adjoint with respect to a pairing, which is a different construction treated in the `*`-operator group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | the field of scalars |
| $V,W$ | finite-dimensional $F$-linear spaces |
| $V^{*} = \operatorname{Hom}_F(V,F)$ | the dual space |
| $T^{\mathsf{T}} : W^{*} \to V^{*}$ | the transpose of $T : V \to W$, $T^{\mathsf{T}}\varphi = \varphi T$ |
| $(-)^{*}$ | the contravariant dualisation functor |
| $U^{0} \subseteq V^{*}$ | the annihilator of a subspace $U \subseteq V$ |
| $\mathrm{ev}_v(\varphi) = \varphi(v)$ | the evaluation functional at $v$ |
| $\mathrm{ev} : V \to V^{**}$ | the evaluation map, an isomorphism in finite dimension |
| $T^{\mathsf{TT}}$ | the double transpose, equal to $T$ under $\mathrm{ev}$ |
| $A^{\mathsf{T}}$ | the transpose of a matrix |
| $E = \operatorname{End}_F(V)$ | the endomorphism algebra |
| $E^{\mathrm{op}}$ | the opposite algebra, reached by the transpose anti-isomorphism |

## Further Reading

- Michael Atiyah and Ian MacDonald, *Introduction to Commutative Algebra* (Addison–Wesley, 1969), for duality of modules and the naturality of the double dual.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the dual space, the transpose and the canonical map to the double dual.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for the transpose as an anti-isomorphism of matrix algebras.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra* (Prentice Hall, 2nd ed. 1971), for the dual basis, the annihilator and the rank of the transpose.
- Saunders Mac Lane, *Categories for the Working Mathematician* (Springer, 2nd ed. 1998), for contravariant functors and natural transformations.
- Serge Lang, *Linear Algebra* (Springer, 3rd ed. 1987), for the duality of finite-dimensional vector spaces and the double dual.
