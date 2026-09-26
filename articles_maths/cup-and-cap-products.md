
# __Cup and Cap Products__

## Introduction

Cohomology with a ring of coefficients is not merely a graded module: it carries a multiplication, the **cup product**, which is defined on cochains by restricting a singular simplex to its front and back faces and multiplying the two values. The product is graded-commutative, natural, and unital, so the direct sum $H^*(X;R)$ is a graded ring — the **cohomology ring** — and this ring is a strictly finer invariant than the graded module of cohomology groups: the two are the same for $S^2 \vee S^4$ and $\mathbb{CP}^2$ in the module sense and different as rings. The companion article *Cohomology and the Universal Coefficient Theorem* supplies the cohomology groups; the present article supplies the product on them, the **cap product** that pairs cohomology with homology, and the two computational theorems that follow — the **Künneth formula** for a product of spaces, and the resulting computations for the spheres, the projective spaces and the tori.

The construction is entirely formal. The only input beyond the singular chain complex of *Simplicial and Singular Homology* is the **Eilenberg–Zilber** comparison of the chains of a product with the tensor product of the chains of the factors, which is what makes the cross product well defined; and the only algebraic input is the $\operatorname{Tor}$ functor of the planned *Ext and Tor* of Part I, written in parallel, in the Künneth formula for coefficients in a general ring.

The article does not yet use Poincaré duality: the cap product with a fundamental class, the intersection form and the duality theorem itself lie outside this article. The cap product is defined here because its formal properties — associativity with the cup product, naturality, and the projection formula — are needed wherever cohomology acts on homology, and because it is the operation through which duality is later stated.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$, and all coefficients are in $R$ unless a module $G$ is named. Cohomology is contravariant, $f^*$ is the pullback, and the cohomology of a pair is as in *Cohomology and the Universal Coefficient Theorem*. The degree of a cohomology class $\varphi$ is written $|\varphi|$.

## The Cup Product

### Definition on Cochains

**Definition.** Let $\varphi \in C^k(X;R)$ and $\psi \in C^l(X;R)$ be singular cochains, and let $\sigma : \Delta_{k+l} \to X$ be a singular $(k+l)$-simplex with vertices $v_0, \ldots, v_{k+l}$. The **front $k$-face** of $\sigma$ is the restriction $\sigma|_{[v_0,\ldots,v_k]}$ and the **back $l$-face** is $\sigma|_{[v_k,\ldots,v_{k+l}]}$, both read as maps of the standard simplex by the canonical affine identification. The **cup product** is the cochain

$$
(\varphi \smile \psi)(\sigma) = \varphi\bigl(\sigma|_{[v_0,\ldots,v_k]}\bigr)\cdot\psi\bigl(\sigma|_{[v_k,\ldots,v_{k+l}]}\bigr),
$$

extended $R$-linearly, so that $\varphi \smile \psi \in C^{k+l}(X;R)$ and $\smile$ is a bilinear pairing $C^k \times C^l \to C^{k+l}$.

Note that the two faces share the vertex $v_k$; this overlap is what makes the product associative on the nose at the cochain level and forces the sign in the graded-commutativity relation below.

**Theorem (Leibniz rule).** The coboundary is a graded derivation for the cup product:

$$
\delta(\varphi \smile \psi) = (\delta\varphi) \smile \psi + (-1)^{|\varphi|}\, \varphi \smile (\delta\psi).
$$

Consequently the cup product of two cocycles is a cocycle, and the product of a cocycle with a coboundary is a coboundary, so $\smile$ descends to a well-defined product

$$
\smile : H^k(X;R) \times H^l(X;R) \longrightarrow H^{k+l}(X;R).
$$

*Proof.* Evaluate both sides on a singular $(k+l+1)$-simplex $\sigma$. The left side is a signed sum over the facets of $\sigma$ of products of the front and back evaluations; the right side expands by the boundary formula, and the terms with the omitted vertex in the interior of $[v_0,\ldots,v_k]$ regroup into the first summand, those with the omitted vertex in the interior of $[v_k,\ldots,v_{k+l}]$ into the second with the sign $(-1)^k$ emerging from the index shift, and the two terms at the shared vertex $v_k$ cancel between the two summands. $\square$

### Properties

**Theorem.** The cup product is associative, unital and graded-commutative, and it is natural. Precisely:

1. $(\varphi \smile \psi) \smile \theta = \varphi \smile (\psi \smile \theta)$;
2. there is a unit $1 \in H^0(X;R)$, the class of the cocycle sending every singular $0$-simplex to $1 \in R$, with $1 \smile \varphi = \varphi \smile 1 = \varphi$;
3. $\varphi \smile \psi = (-1)^{|\varphi||\psi|}\, \psi \smile \varphi$;
4. for a continuous map $f : X \to Y$, $f^*(\varphi \smile \psi) = f^*\varphi \smile f^*\psi$.

*Proof.* Associativity is the identity of the front and back face decompositions of a simplex into three consecutive blocks: both sides evaluate a triple $(\varphi,\psi,\theta)$ at the three blocks $[v_0..v_k]$, $[v_k..v_{k+l}]$, $[v_{k+l}..v_{k+l+m}]$ of a simplex, the only difference being the order in which the restrictions are taken, and the face maps commute. Unitality is the observation that the front $0$-face of any simplex is its initial vertex. Graded commutativity is proved by a chain homotopy: the **shuffle map** $\rho : C_{k+l}(X) \to C_{k+l}(X)$ sending a simplex to the alternating sum of the $(k,l)$-shuffles satisfies $\rho \simeq (-1)^{kl}\mathrm{id}$, and comparing $\varphi \smile \psi$ with $\psi \smile \varphi$ precomposed with $\rho$ gives the sign. Naturality is immediate from $f_\#(\sigma) = f \circ \sigma$ and the definition. $\square$

**Corollary.** $H^*(X;R)$ is an associative graded ring with unit, and the cup product makes it a graded-commutative algebra: for classes $x$ of even degree, $x \smile y = y \smile x$, and for $x$ of odd degree, $x \smile x = -x \smile x$, so $2(x \smile x) = 0$ and $x \smile x = 0$ when $R$ has no $2$-torsion.

**Remark.** Graded commutativity with the sign $(-1)^{kl}$ is the Koszul sign rule of the graded algebra of Part I; the cohomology ring is thus a graded-commutative $R$-algebra, and the structure theory of such algebras — free algebras, divided powers, Koszul duality — applies to it. The exterior algebra $\Lambda(V)$ of *The Exterior Algebra* is the model: the cohomology of a torus is an exterior algebra on odd classes, as computed below.

### Relative Version and the Pairing with Coefficients

**Definition.** For a pair $(X,A)$ the cup product is defined on relative cochains by the same formula, and gives

$$
\smile : H^k(X,A;R) \times H^l(X;R) \to H^{k+l}(X,A;R), \qquad \smile : H^k(X;R) \times H^l(X,A;R) \to H^{k+l}(X,A;R),
$$

the relative class being the one that must be supported away from $A$. Combining the two gives $H^k(X,A;R) \times H^l(X,A;R) \to H^{k+l}(X,A;R)$ only when the two classes have disjoint supports in the sense of the diagonal approximation; the general statement uses the **cross product** below.

## The Cap Product

### Definition

**Definition.** Let $\varphi \in C^k(X;R)$ be a cochain and $\sigma : \Delta_n \to X$ a singular $n$-simplex with $n \geq k$ and vertices $v_0,\ldots,v_n$. The **cap product** is the chain

$$
\sigma \frown \varphi = \varphi\bigl(\sigma|_{[v_0,\ldots,v_k]}\bigr)\cdot \sigma|_{[v_k,\ldots,v_n]},
$$

extended $R$-linearly to $\frown : C_n(X;R) \times C^k(X;R) \to C_{n-k}(X;R)$. The back face is the singular $(n-k)$-simplex $\Delta_{n-k} \to X$ obtained by the canonical identification with $[v_k,\ldots,v_n]$.

**Theorem (the boundary rule).** For $\varphi \in C^k(X;R)$ and $c \in C_n(X;R)$,

$$
\partial(c \frown \varphi) = (-1)^k\bigl((\partial c) \frown \varphi - c \frown \delta\varphi\bigr).
$$

Hence $\frown$ descends to a pairing

$$
\frown : H_n(X;R) \times H^k(X;R) \longrightarrow H_{n-k}(X;R), \qquad (\text{class of } c) \frown (\text{class of } \varphi) = \text{class of } c \frown \varphi,
$$

which is well defined because a cycle capped with a cocycle is a cycle and a boundary capped with a cocycle, or a cycle capped with a coboundary, is a boundary.

*Proof.* Evaluate the boundary of the chain $c \frown \varphi$ on the facets of a simplex. The facets not containing the block $[v_0..v_k]$ reassemble into $(\partial c) \frown \varphi$, and those meeting the block into $c \frown \delta\varphi$; the signs collected from the boundary formula give $(-1)^k$ and the stated difference. $\square$

### Properties

**Theorem.** The cap product satisfies:

1. **Associativity with the cup product:** for $c \in H_n(X;R)$, $\varphi \in H^k(X;R)$ and $\psi \in H^l(X;R)$,
   $$c \frown (\varphi \smile \psi) = (c \frown \varphi) \frown \psi;$$
2. **Naturality:** for a continuous map $f : X \to Y$, $f_\#(c \frown f^*\varphi) = f_\#(c) \frown \varphi$;
3. **Projection formula:** $f_*(f^*(c') \frown \varphi) = c' \frown f_*\varphi$ for $c' \in H_*(Y;R)$;
4. the unit acts trivially: $c \frown 1 = c$.

*Proof.* All four are verified at the cochain level by the same face-decomposition computation as the Leibniz rule; the second and third are the statements that $f_\#$ is a module map over the cochain pullback $f^\#$ for the cap pairing, which follows from $f_\#(\sigma \frown f^\#\psi) = f_\#(\sigma) \frown \psi$ applied simplex by simplex. $\square$

**Corollary.** For each $k$, the cap product makes $H_*(X;R)$ a graded module over the graded ring $H^*(X;R)$: the assignment $(c,\varphi) \mapsto c \frown \varphi$ is a graded bilinear pairing with $c \frown (\varphi \smile \psi) = (c \frown \varphi) \frown \psi$. This module structure is the algebraic object whose properties Poincaré duality describes.

## The Künneth Formula

### The Cross Product

**Definition.** Let $X$ and $Y$ be spaces, with projections $\mathrm{pr}_1 : X\times Y \to X$ and $\mathrm{pr}_2 : X \times Y \to Y$. The **Eilenberg–Zilber chain map** is the natural chain map

$$
\Xi : C_*(X;R) \otimes_R C_*(Y;R) \longrightarrow C_*(X \times Y;R)
$$

sending $\sigma \otimes \tau$ to the chain obtained by composing $x \mapsto (\sigma(x),\tau(y))$ with a fixed subdivision of the product of standard simplices $\Delta_i \times \Delta_j$ into $(i+j)$-simplices, the **shuffle** subdivision. The **homology cross product** is the induced map

$$
\times : H_i(X;R) \otimes_R H_j(Y;R) \longrightarrow H_{i+j}(X\times Y;R), \qquad c \times d = \Xi_*(c \otimes d),
$$

and the **cohomology cross product** is

$$
\times : H^i(X;R) \times H^j(Y;R) \longrightarrow H^{i+j}(X\times Y;R), \qquad \varphi \times \psi = \mathrm{pr}_1^*\varphi \smile \mathrm{pr}_2^*\psi.
$$

**Theorem.** The Eilenberg–Zilber map is a chain map and a chain homotopy equivalence, natural in both variables, so the cross products are well defined and associative; and the two are related by the cap product.

**Remark.** The subdivision of $\Delta_i \times \Delta_j$ into $(i+j)!/(i!j!)$ simplices is the combinatorial input; the theorem of Eilenberg and Zilber is that the resulting chain map is natural and a homotopy equivalence, which is the statement that the graded module $H_*(X\times Y)$ is computed from $H_*(X)$ and $H_*(Y)$ up to the correction of the next theorem.

### The Künneth Formula

**Theorem (Künneth).** Let $X$ and $Y$ be topological spaces and let $R$ be a principal ideal domain. For each $n$ there is a short exact sequence of $R$-modules

$$
0 \to \bigoplus_{i+j=n} H_i(X;R) \otimes_R H_j(Y;R) \xrightarrow{\ \times\ } H_n(X\times Y;R) \to \bigoplus_{i+j=n-1} \operatorname{Tor}_1^R\bigl(H_i(X;R), H_j(Y;R)\bigr) \to 0,
$$

which splits, though not naturally. Its middle term is the cokernel of the multiplication by the Tor term, and the isomorphism

$$
H_n(X\times Y;R) \cong \Bigl(\bigoplus_{i+j=n} H_i(X;R)\otimes_R H_j(Y;R)\Bigr) \oplus \Bigl(\bigoplus_{i+j=n-1}\operatorname{Tor}_1^R(H_i(X),H_j(Y))\Bigr)
$$

is non-natural. The functor $\operatorname{Tor}_1^R$ is the one of Part I's *Ext and Tor*, written in parallel.

*Proof sketch.* For each $n$ the Eilenberg–Zilber map gives a natural map $\bigoplus_{i+j=n}H_i(X)\otimes H_j(Y) \to H_n(X\times Y)$, and the cokernel is the Tor term; the argument is the algebraic Künneth theorem for chain complexes of free modules over a principal ideal domain, applied to $C_*(X;R)\otimes_R C_*(Y;R) \to C_*(X\times Y;R)$. $\square$

**Corollary (field coefficients).** If $R = F$ is a field then $\operatorname{Tor}_1^F = 0$, so the cross product is an isomorphism

$$
\bigoplus_{i+j=n} H_i(X;F)\otimes_F H_j(Y;F) \xrightarrow{\ \cong\ } H_n(X\times Y;F),
$$

and dually, for cohomology, $H^*(X\times Y;F) \cong H^*(X;F)\otimes_F H^*(Y;F)$ as graded rings. For a principal ideal domain with one factor of finite type, the Tor term vanishes if either factor's homology is free.

**Corollary (tori).** For the $n$-torus $T^n = (S^1)^n$, over a field $F$ the Künneth formula iterates to give

$$
\dim_F H_k(T^n;F) = \binom{n}{k},
$$

so $\chi(T^n) = 0$ for $n \geq 1$; over $\mathbb{Z}$ the homology is free of rank $\binom{n}{k}$, and the cohomology ring is the exterior algebra $H^*(T^n;\mathbb{Z}) \cong \Lambda_{\mathbb{Z}}(\alpha_1,\ldots,\alpha_n)$ on classes $\alpha_i$ of degree one, a graded-commutative ring in which $\alpha_i \smile \alpha_j = -\alpha_j \smile \alpha_i$ and $\alpha_i^2 = 0$.

## Computations

### The Projective Spaces

**Theorem.** For the complex projective space,

$$
H^*(\mathbb{CP}^n;\mathbb{Z}) \cong \mathbb{Z}[x]/(x^{n+1}), \qquad |x| = 2,
$$

with $x$ the class dual to a hyperplane, and the ring is a truncated polynomial algebra on a single even generator. For the real projective space,

$$
H^*(\mathbb{RP}^n;\mathbb{Z}/2) \cong (\mathbb{Z}/2)[x]/(x^{n+1}), \qquad |x| = 1,
$$

a truncated polynomial algebra on an odd generator over $\mathbb{Z}/2$; integrally the cohomology is $\mathbb{Z}$ in degrees $0$ and $n$ (the latter for $n$ odd) and $\mathbb{Z}/2$ in the odd degrees below $n$.

*Proof.* The cell structure of *CW Complexes and Cellular Approximation* has one cell in each even degree up to $2n$ for $\mathbb{CP}^n$ and one in each degree up to $n$ for $\mathbb{RP}^n$, with all cellular coboundaries zero for $\mathbb{CP}^n$ and the duals of multiplication by $1+(-1)^k$ for $\mathbb{RP}^n$; hence the additive groups are as stated. The ring structure is determined by the fact that the generator $x$ in degree $2$ (respectively degree $1$) has nonzero $k$-th power in degree $2k \leq 2n$ (respectively $k \leq n$), because the top class is the dual of the top cell and is a product of lower classes; the nonvanishing is computed by evaluating $x^k$ on the fundamental class of the appropriate $\mathbb{CP}^k \subseteq \mathbb{CP}^n$. $\square$

**Remark.** The cup product therefore distinguishes $\mathbb{CP}^2$ from $S^2 \vee S^4$: both have $\mathbb{Z}$ in degrees $0,2,4$ and zero elsewhere, but in the cohomology ring of $\mathbb{CP}^2$ the degree-two generator squares to the degree-four generator while in the wedge the product of the two generators is zero. The ring is a strictly finer invariant than the graded group.

### Products of Spheres and the Hopf Map

**Example.** For $S^m \times S^n$ with $m,n \geq 1$ and field coefficients, the Künneth formula gives $H^k \cong F$ for $k \in \{0,m,n,m+n\}$ with the multiplicity of $m=n$ accounted for, and zero otherwise. For $m \neq n$ the cohomology ring is the graded tensor product $\bigwedge(\alpha_m)\otimes\bigwedge(\beta_n)$ on generators of degrees $m$ and $n$, and both generators square to zero: the only class of degree $m$ is $\alpha_m = x\otimes 1$ with $x^2 = 0$ in $H^*(S^m)$, and likewise for $\beta_n$. For $m = n$ the ring is $\bigwedge(\alpha)\otimes\bigwedge(\beta)$ on two generators of the same degree $m$, still with $\alpha^2 = \beta^2 = 0$ and with $\alpha\beta$ generating the one-dimensional $H^{2m}$; a class $a\alpha + b\beta$ then has square $(a\alpha+b\beta)^2 = ab(\alpha\beta+\beta\alpha) = ab(1+(-1)^m)\alpha\beta$, which vanishes for $m$ odd and equals $2ab\,\alpha\beta$ for $m$ even, so that squares of degree-$m$ classes are nonzero in characteristic not $2$ although the generators are not.

**Example (the Hopf map and $\mathbb{CP}^2$).** The quotient $S^3 \to S^2$ has fibre $S^1$; the associated disc bundle, glued with a $4$-disc, produces $\mathbb{CP}^2$ as the mapping cone of the Hopf map, and this gives a second computation of its cohomology ring from the cell structure with cells in degrees $0,2,4$ and the relation $x^2 = y$. The construction of the Hopf fibration and the general theory of fibrations belong .

### Ring Structures and the Classification of Surfaces

**Example (the torus and the spheres).** The cohomology ring of the $n$-torus is the exterior algebra on $n$ generators of degree one,

$$
H^*(T^n;\mathbb{Z})\cong\bigwedge\nolimits_{\mathbb{Z}}(\alpha_1,\dots,\alpha_n),\qquad \alpha_i\alpha_j = -\alpha_j\alpha_i,
$$

which is the Künneth computation of the circle $H^*(S^1) = \mathbb{Z}\oplus\mathbb{Z}[1]$; for $n = 2$ the ring is generated by $\alpha,\beta$ with $\alpha^2 = \beta^2 = 0$ and $\alpha\beta = -\beta\alpha$ the generator of $H^2(T^2;\mathbb{Z})$. For the sphere, $H^*(S^n;\mathbb{Z})$ has $x^2 = 0$ for the degree-$n$ generator, since $x^2$ would lie in $H^{2n}(S^n) = 0$; and for the projective spaces the rings are $\mathbb{Z}[x]/(x^{n+1})$ with $\deg x = 2$ and $\mathbb{F}_2[x]/(x^{n+1})$ with $\deg x = 1$, whose truncated polynomial form makes the cohomology ring a genuinely finer invariant than the Betti numbers.

**Example (three spaces with the same Betti numbers).** The spaces $S^2\vee S^2\vee S^4$, $S^2\times S^2$ and $\mathbb{CP}^2\vee S^2$ all have Betti numbers $b_0 = b_4 = 1$, $b_2 = 2$ and $b_1 = b_3 = 0$, and their cohomology rings are pairwise non-isomorphic. For the wedge, the cohomology is the direct sum of the reduced cohomologies of the summands with all products of classes from different summands zero, and $a^2 = 0$ for $a$ of degree two, because $a^2$ would lie in $H^4(S^2) = 0$; hence every product of two degree-two classes vanishes. For the product, the Künneth formula gives $H^*(S^2\times S^2) = \bigwedge(\alpha,\beta)$ with $\alpha^2 = \beta^2 = 0$ and $\alpha\beta$ a generator of $H^4$, so some products vanish and one does not. For $\mathbb{CP}^2\vee S^2$ the class $x$ coming from $\mathbb{CP}^2$ satisfies $x^2\neq0$ while the class $y$ from the sphere satisfies $y^2 = xy = 0$. The three rings are therefore pairwise distinct and the cup product separates the three spaces, although the Betti numbers, and hence the additive cohomology, do not.

**Example (non-orientable surfaces and $\mathbb{Z}/2$ coefficients).** With $\mathbb{Z}/2$ coefficients the graded-commutativity loses its sign and the rings simplify: $H^*(\mathbb{RP}^n;\mathbb{Z}/2) = \mathbb{F}_2[x]/(x^{n+1})$ with $\deg x = 1$, so the ring detects the projective dimension. For a closed connected non-orientable surface $N_g$ — the connected sum of $g$ projective planes, so that $H_1(N_g;\mathbb{Z}) = \mathbb{Z}^{g-1}\oplus\mathbb{Z}/2$ — the classes $u_1,\dots,u_g$ of degree one dual to the $g$ circles $\mathbb{RP}^1$ of the summands satisfy

$$
u_iu_j = 0\ (i\neq j),\qquad u_i^2 = \gamma\neq 0,
$$

where $\gamma$ generates $H^2(N_g;\mathbb{Z}/2)\cong\mathbb{Z}/2$; all the squares are equal because $H^2$ is one-dimensional. The relations are the mod-2 intersection numbers of the dual curves: the $g$ circles lie in different summands and can be made disjoint, so the off-diagonal products vanish, while a projective line in a projective plane has mod-2 self-intersection one, so the squares do not. The pairing is nondegenerate, as Poincaré duality requires. Over $\mathbb{Z}$ the same surface has $H^1(N_g;\mathbb{Z})\cong\mathbb{Z}^{g-1}\oplus\mathbb{Z}/2$ and, by the universal coefficient theorem, $H^2(N_g;\mathbb{Z})\cong\mathbb{Z}/2$; the integral invariants are therefore determined by $g$ additively, and the mod-2 ring exhibits the product structure explicitly.

### The Cap Product in Low Degrees

**Example.** For a path-connected space $X$ and a class $\varphi \in H^1(X;R)$ represented by a cocha, the cap product with $\varphi$ is a derivation-like operation $H_n(X;R) \to H_{n-1}(X;R)$; when $\varphi$ is the class dual to a map $X \to S^1$, the cap product with $\varphi$ is the homology operation induced by the corresponding infinite cyclic cover, and it computes the twisted homology that appears in the Leray–Serre theory. The systematic statement uses the fundamental class and Poincaré duality and is given.

**Remark.** The cap product is the operation through which a cohomology class acts on homology, and it is therefore the algebraic form of the statement that a cohomology class is a family of subvarieties or of level sets. In the geometric articles of this corpus — the homology of the classical groups, the characteristic classes of *Fibre Bundles, Connections and Curvature*, and the intersection form of Poincaré duality — it is used exactly in this sense.

## Summary

The cup product is defined on singular cochains by multiplying the evaluations on the front and back faces of a simplex; the coboundary is a graded derivation for it, so it descends to cohomology. The resulting product is associative, unital, graded-commutative with the Koszul sign $(-1)^{|\varphi||\psi|}$, and natural under pullback, so $H^*(X;R)$ is a graded-commutative $R$-algebra, a strictly finer invariant than the graded module of cohomology groups. The cap product pairs a cohomology class of degree $k$ with a homology class of degree $n$ to give one of degree $n-k$; it satisfies the boundary rule with the sign $(-1)^k$, is associative with the cup product, is natural, and obeys the projection formula, so $H_*(X;R)$ is a graded module over the ring $H^*(X;R)$.

The Eilenberg–Zilber chain equivalence relates the chains of a product to the tensor product of the chains of the factors, and the Künneth formula states the resulting split short exact sequence with a tensor term and a $\operatorname{Tor}$ term; over a field the Tor term vanishes and the cross product is an isomorphism of graded rings. The computations that follow are the cohomology rings of the spheres, of the tori — an exterior algebra on odd generators — and of the projective spaces — a truncated polynomial algebra on one even generator over $\mathbb{Z}$ for $\mathbb{CP}^n$, and on one odd generator over $\mathbb{Z}/2$ for $\mathbb{RP}^n$ — and these distinguish spaces whose cohomology groups agree.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity $1 \neq 0$; also the coefficient ring |
| $\varphi, \psi, \theta$ | Cochains or cohomology classes; $|\varphi|$ the degree |
| $\smile$ | Cup product; $C^k \times C^l \to C^{k+l}$, $H^k \times H^l \to H^{k+l}$ |
| $\delta$ | Coboundary; a graded derivation for $\smile$ |
| $\frown$ | Cap product; $C_n \times C^k \to C_{n-k}$, $H_n \times H^k \to H_{n-k}$ |
| $H^*(X;R)$ | Graded cohomology ring; associative, unital, graded-commutative |
| $(-1)^{kl}$ | Koszul sign; $\varphi \smile \psi = (-1)^{|\varphi||\psi|}\psi \smile \varphi$ |
| $\times$ | Cross product in homology and in cohomology |
| Eilenberg–Zilber | Chain equivalence $C_*(X)\otimes C_*(Y) \to C_*(X\times Y)$ |
| Künneth sequence | $0 \to \bigoplus_{i+j=n}H_i\otimes H_j \to H_n(X\times Y) \to \bigoplus_{i+j=n-1}\operatorname{Tor}_1(H_i,H_j) \to 0$ |
| $\operatorname{Tor}_1^R$ | Torsion functor of Part I, written in parallel; the Künneth correction |
| $x \in H^2(\mathbb{CP}^n;\mathbb{Z})$ | Generator; $H^*(\mathbb{CP}^n;\mathbb{Z}) \cong \mathbb{Z}[x]/(x^{n+1})$ |
| $x \in H^1(\mathbb{RP}^n;\mathbb{Z}/2)$ | Generator; $H^*(\mathbb{RP}^n;\mathbb{Z}/2) \cong (\mathbb{Z}/2)[x]/(x^{n+1})$ |
| $\Lambda_R(\alpha_1,\ldots,\alpha_n)$ | Exterior algebra; $H^*(T^n;R)$ for $R$ a field or $\mathbb{Z}$ |
| $T^n = (S^1)^n$ | The $n$-torus |





## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the cup and cap products, the Künneth formula and the cohomology rings of the classical examples.
- Samuel Eilenberg and Norman Steenrod, *Foundations of Algebraic Topology* (Princeton University Press, 1952), for the original construction of the products and the axioms they satisfy.
- James R. Munkres, *Elements of Algebraic Topology* (Addison-Wesley, 1984), for the shuffle argument giving graded commutativity.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the de Rham counterpart, in which the cup product is the wedge of forms.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for the algebraic Künneth theorem and the role of $\operatorname{Tor}$.
- Edwin H. Spanier, *Algebraic Topology* (McGraw–Hill, 1966), for the relative products and the cap product with local coefficients.
- Glen E. Bredon, *Topology and Geometry* (Springer, 1993), for the comparison of the ring structures and the applications to manifolds.
