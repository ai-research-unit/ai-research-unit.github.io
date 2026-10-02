
# __Operators on a Variety__

## Introduction

A variety is a set with a sheaf of functions, and the operators on it are the maps of that sheaf that respect the structure it carries. Three classes are visible at once, and they are the subject of this article: the **multiplications** by the global functions, which are all the endomorphisms of the structure sheaf that are linear over it; the **derivations** of the structure sheaf, which are the vector fields; and the **automorphisms** of the variety, which are the invertible ring endomorphisms of the structure sheaf and which act on the other two classes by conjugation. The article fixes the operator layer of the category, the sheaf $\mathcal{E}nd_{\mathcal{O}_X}(\mathcal{O}_X) = \mathcal{O}_X$ and the tangent sheaf $\mathcal{T}_X = \mathcal{D}er_k(\mathcal{O}_X)$, and it records the action of the automorphism group on both. It is the first article of the `- Operator Theory` group, and it fixes the marks and the layer conventions that the five articles after it use: *The Galois Action as an Operator*, *The Frobenius Operator*, *The Pullback Operator of a Morphism*, *The Divisor Operator* and *The Sheaf of Differential Operators*.

Nothing here is analytic. A derivation is defined by the Leibniz rule, as in Part I's *Derivations of a Ring*, and it is not a limit of difference quotients; the tangent sheaf is the dual of the algebraic cotangent sheaf $\Omega^1_{X/k}$ of *Schemes*, and the tangent space at a point is the algebraic $\mathrm{M}_P/\mathrm{M}_P^2$ of *Algebraic Geometry*. The differential calculus on a smooth manifold, in which a vector field is a section of the tangent bundle defined by an atlas, is Part III's, and the article names that structure only to defer to it.

The variety $X$ is reduced and of finite type over a field $k$ throughout, so that it carries the coordinate ring of *Algebraic Geometry* on each affine chart and the structure sheaf of *Schemes* on the whole; a general scheme is admitted only where the statement is purely sheaf-theoretic and is said so.

## The Operator Layer of a Variety

**Definition.** Let $(X,\mathcal{O}_X)$ be a variety over $k$. The **operator layer** of $X$ is the sheaf of $k$-algebras

$$
\mathcal{E}nd(\mathcal{O}_X) = \mathcal{H}om_{\mathcal{O}_X}(\mathcal{O}_X,\mathcal{O}_X),
$$

whose sections over an open $U$ are the $\mathcal{O}_X(U)$-linear endomorphisms of $\mathcal{O}_X(U)$, with composition as product. Its global sections form the $k$-algebra $\operatorname{End}_{\mathcal{O}_X}(\mathcal{O}_X)$.

**Theorem (the operator layer is the structure sheaf).** The map
$$
s \longmapsto m_s, \qquad m_s(t) = st,
$$
is an isomorphism of sheaves of $\mathcal{O}_X$-algebras $\mathcal{O}_X\xrightarrow{\ \sim\ }\mathcal{E}nd(\mathcal{O}_X)$. Consequently every endomorphism of $\mathcal{O}_X$ linear over itself is the multiplication by a unique function, and the algebra of global operators is
$$
\operatorname{End}_{\mathcal{O}_X}(\mathcal{O}_X)\cong\Gamma(X,\mathcal{O}_X),
$$
a commutative ring. Its group of units is $\Gamma(X,\mathcal{O}_X^\times)$, the group of invertible global functions.

*Proof.* The map is $\mathcal{O}_X$-linear and multiplicative, $m_sm_t = m_{st}$, and it is injective because $m_s(1) = s$. For surjectivity, let $\varphi$ be a section of $\mathcal{H}om_{\mathcal{O}_X}(\mathcal{O}_X,\mathcal{O}_X)$ over $U$ and put $s = \varphi(1)$. Then for any section $t$ of $\mathcal{O}_X$ over $U$, $\mathcal{O}_X$-linearity gives $\varphi(t) = \varphi(t\cdot 1) = t\,\varphi(1) = ts$, so $\varphi = m_s$. On the global sections the product is pointwise and the ring is $\Gamma(X,\mathcal{O}_X)$; its units are exactly the sections that are invertible at every point, which is $\Gamma(X,\mathcal{O}_X^\times)$.

**Remark (the two readings of "endomorphism").** The theorem is about the operators **linear over the structure sheaf**, and those are the multiplications. The ring endomorphisms of $\mathcal{O}_X$ as a sheaf of rings, which need not be $\mathcal{O}_X$-linear, are a different and larger object, and they are treated in *Endomorphisms and Automorphisms of the Structure Sheaf* below. The two must be kept apart: a multiplication $m_s$ is never an automorphism of the pair $(X,\mathcal{O}_X)$ unless $s$ is a unit, while an automorphism of the variety is a ring automorphism that is almost never $\mathcal{O}_X$-linear.

**Example ($\mathbb{A}^1$ and a global function).** On $X = \mathbb{A}^1_k$ the global operators are the polynomials, $\Gamma(X,\mathcal{O}_X) = k[t]$, and $m_t$ is the operator that multiplies a function by the coordinate; it is injective and not surjective, since $1$ is not in its image. On $X = \mathbb{A}^1_k\setminus\{0\}$ the global functions are $k[t,t^{-1}]$ and the unit group is $k^\times t^m$, $m\in\mathbb{Z}$, so the unitaries of the operator layer are the multiplications by the monomials.

## Vector Fields

**Definition.** A **derivation** of $\mathcal{O}_X$ over $k$ is a $k$-linear map $D : \mathcal{O}_X(U)\to\mathcal{O}_X(U)$ on each open $U$, compatible with restriction, satisfying the Leibniz rule
$$
D(fg) = f\,D(g) + D(f)\,g .
$$
The derivations form a sheaf $\mathcal{D}er_k(\mathcal{O}_X)$ of $k$-vector spaces; a global section is a **vector field** on $X$. The **tangent sheaf** is
$$
\mathcal{T}_X = \mathcal{D}er_k(\mathcal{O}_X).
$$

**Theorem (the operator structure of the vector fields).** On each open $U$ the derivations $\operatorname{Der}_k(\mathcal{O}_X(U))$ form a Lie algebra under the commutator
$$
[D_1,D_2] = D_1D_2 - D_2D_1,
$$
and a module over the ring $\mathcal{O}_X(U)$ under $(fD)(g) = f\,D(g)$. The two are compatible in the Leibniz rule for the bracket,
$$
[fD_1,\,gD_2] = fg\,[D_1,D_2] + f\,D_1(g)\,D_2 - g\,D_2(f)\,D_1 ,
$$
so that $\mathcal{D}er_k(\mathcal{O}_X)$ is a sheaf of Lie algebras over $k$ and a sheaf of modules over $\mathcal{O}_X$ at once.

*Proof.* The bracket of two derivations is a derivation: the Leibniz rule applied twice gives $[D_1,D_2](fg) = f[D_1,D_2](g) + [D_1,D_2](f)g$, since the four cross-terms cancel in pairs. The bracket is $k$-bilinear, alternating and satisfies the Jacobi identity because the commutator of operators always does, by Part I's *Algebras of Endomorphisms*. The module axioms and the displayed Leibniz rule are checked by expanding both sides and cancelling the two terms in which $D_1(g)$ or $D_2(f)$ is differentiated.

**Proposition (the tangent sheaf is the dual of the cotangent sheaf).** There is a natural isomorphism of $\mathcal{O}_X$-modules
$$
\mathcal{T}_X \cong \mathcal{H}om_{\mathcal{O}_X}(\Omega^1_{X/k},\mathcal{O}_X),
$$
where $\Omega^1_{X/k}$ is the cotangent sheaf of *Schemes*. On an affine chart $X = \operatorname{Spec} A$ it is the identification $\operatorname{Der}_k(A)\cong\operatorname{Hom}_A(\Omega^1_{A/k},A)$.

*Proof.* The universal derivation $d : A\to\Omega^1_{A/k}$ of the module of Kähler differentials has the universal property that every $k$-derivation $\delta : A\to M$ factors uniquely through $\operatorname{Hom}_A(\Omega^1_{A/k},M)$; taking $M = A$ gives the duality on the chart, and the two sides are sheaves, so the identification glues.

**Example ($\mathbb{A}^n$ and the Euler field).** On $\mathbb{A}^n_k$ the derivations form the free $\mathcal{O}$-module of rank $n$,
$$
\operatorname{Der}_k(k[x_1,\ldots,x_n]) = \bigoplus_{i=1}^n k[x_1,\ldots,x_n]\,\partial_i, \qquad \partial_i = \frac{\partial}{\partial x_i},
$$
so $\mathcal{T}_{\mathbb{A}^n}$ is free of rank $n$. The **Euler derivation** $E = \sum_i x_i\partial_i$ satisfies $E(f) = \deg(f)\,f$ on homogeneous polynomials, and it is the generator of the grading of the polynomial ring. On $\mathbb{A}^1$ the derivations are $k[t]\partial_t$, and the space is one-dimensional over the ring; the only derivation with $D(t) = 1$ is $\partial_t$.

**Example (global vector fields on projective space).** On $\mathbb{P}^n_k$ the global vector fields form the space
$$
H^0(\mathbb{P}^n,\mathcal{T}_{\mathbb{P}^n}) \cong \mathrm{sl}_{n+1}(k),
$$
of dimension $(n+1)^2-1$, spanned by the derivations $x_i\partial_j$ of the polynomial ring with the radial field $\sum_i x_i\partial_i$ removed. The identification of this space with the Lie algebra of the automorphism group $\mathrm{PGL}_{n+1}$ is the operator-level form of the statement that the automorphisms of $\mathbb{P}^n$ are the projective linear transformations; the Lie algebra of a group is a Part III notion, and the space itself is an algebraic one.

## Endomorphisms and Automorphisms of the Structure Sheaf

**Definition.** An **endomorphism of the variety** $X$ is a morphism $\varphi : X\to X$ of ringed spaces; it is an **automorphism** when it is invertible. It induces a $k$-algebra homomorphism $\varphi^* : \Gamma(X,\mathcal{O}_X)\to\Gamma(X,\mathcal{O}_X)$ on the global functions, the **pullback**. The automorphisms form the group $\operatorname{Aut}(X)$ under composition.

**Theorem (affine correspondence).** Let $X = \operatorname{Spec} A$ be an affine variety, so that $A = k[X]$ is a finitely generated reduced $k$-algebra. Then formation of the pullback is a bijection
$$
\operatorname{Hom}_{\mathbf{Sch}}(X,X)\ \cong\ \operatorname{Hom}_{k\text{-}\mathbf{alg}}(A,A), \qquad \varphi\longmapsto\varphi^*,
$$
and it restricts to an isomorphism $\operatorname{Aut}(X)\cong\operatorname{Aut}_{k\text{-}\mathbf{alg}}(A)$.

*Proof.* This is the contravariant equivalence of *Schemes*: a morphism of affine schemes is a $k$-algebra homomorphism in the opposite direction, and an invertible morphism corresponds to an invertible homomorphism. Reducedness and finite type are not used for the bijection and are used only to recognise $X$ as a variety.

**Theorem (the automorphisms act on the operator layer).** Let $\varphi\in\operatorname{Aut}(X)$. Then conjugation by $\varphi^*$,
$$
\mathrm{Ad}_\varphi(T) = (\varphi^*)^{-1}\,T\,\varphi^*,
$$
is an automorphism of the $k$-algebra $\Gamma(X,\mathcal{O}_X)$ of multiplication operators, and the pushforward of derivations
$$
(\varphi_*D)(f) = (\varphi^*)^{-1}\bigl(D(\varphi^*f)\bigr)
$$
is an isomorphism of Lie algebras $\operatorname{Der}_k(\mathcal{O}_X)\to\operatorname{Der}_k(\mathcal{O}_X)$. Hence $\operatorname{Aut}(X)$ acts on the operator layer by algebra automorphisms, and the multiplication operators are fixed by the action precisely when $\varphi$ acts trivially on the global functions.

*Proof.* Conjugation by an invertible element of a ring is a ring automorphism, and $\varphi^*$ is invertible with inverse $(\varphi^{-1})^*$. For the derivations, $\varphi_*D$ is the transport of the derivation $D$ along the $k$-algebra isomorphism $\varphi^*$, so it is a derivation and the assignment is a Lie-algebra isomorphism because conjugation of operators preserves commutators. The fixed-multiplication statement is $\mathrm{Ad}_\varphi(m_s) = m_{\varphi^*(s)} = m_s$ for all $s$, that is $\varphi^* = \mathrm{id}$.

**Example (the affine line and its inversions).** On $\mathbb{A}^1_k$ the automorphisms are the affine maps $t\mapsto at+b$ with $a\in k^\times$, $b\in k$, since these are exactly the invertible $k$-algebra endomorphisms of $k[t]$. The group is the affine group of the line, of dimension two, and its conjugation action sends the vector field $f(t)\partial_t$ to $f(at+b)\partial_t$ with the chain-rule factor $a^{-1}$ absorbed: precisely, $(\varphi_*D)(t) = a^{-1}D(at+b)$. On the projective line $\mathbb{P}^1_k$ the automorphism group is $\mathrm{PGL}_2(k)$, of dimension three, and the global vector fields form its three-dimensional Lie algebra $\mathrm{sl}_2(k)$.

## The Action on the Function Field and on Cohomology

**Proposition (the action on the function field).** A dominant endomorphism $\varphi : X\to X$ of an irreducible variety pulls back rational functions, $k(X)\to k(X)$, $f\mapsto \varphi^*f = f\circ\varphi$, a $k$-algebra homomorphism; if $\varphi$ is an automorphism the pullback is a $k$-automorphism of $k(X)$.

*Proof.* The pullback of a rational function along a dominant morphism is the composition with $\varphi$ on a dense open set on which both are defined, and the composition is independent of the open set chosen; invertibility of $\varphi$ makes the pullback invertible with inverse $(\varphi^{-1})^*$.

**Proposition (the action on cohomology).** Let $\varphi : X\to X$ be an endomorphism and $\mathcal{F}$ a quasi-coherent sheaf on $X$. Then $\varphi$ induces a $k$-linear map
$$
\varphi^* : H^i(X,\mathcal{F})\longrightarrow H^i(X,\varphi^*\mathcal{F})
$$
natural in $\mathcal{F}$, and for $\mathcal{F} = \mathcal{O}_X$ with $\varphi$ an automorphism this is an automorphism of the graded $k$-vector space $H^\bullet(X,\mathcal{O}_X)$. If $\varphi$ is the identity on a closed subscheme $Z\subseteq X$, the map factors through the cohomology of $Z$ in the sense of the long exact sequence of the pair $(X,Z)$ whenever $\mathcal{F}$ is supported there.

*Proof.* A morphism of schemes induces a morphism of the associated ringed spaces, hence a map of cohomology with coefficients pulled back; the functoriality $\varphi^*\circ\psi^* = (\psi\varphi)^*$ is the functoriality of $f^*$ of *Coherent Sheaves*, and invertibility carries over. The factorisation statement is the exactness of the cohomology sequence of a short exact sequence of sheaves, applied to the ideal sheaf of $Z$.

The **Lefschetz number** of an endomorphism is the alternating sum $\sum_i(-1)^i\operatorname{tr}\bigl(\varphi^*|H^i(X,\mathcal{O}_X)\bigr)$; the fixed-point theorem that computes it as an intersection number is stated in the arithmetic setting in *The Frobenius Operator*, below in this group, and its topological form belongs to *Algebraic Topology*.

## Summary

The operator layer of a variety $X$ is the sheaf $\mathcal{E}nd(\mathcal{O}_X) = \mathcal{H}om_{\mathcal{O}_X}(\mathcal{O}_X,\mathcal{O}_X)$ of endomorphisms of the structure sheaf, and it is isomorphic to $\mathcal{O}_X$ itself: every operator linear over the functions is a multiplication $m_s$, and the algebra of global operators is the commutative ring $\Gamma(X,\mathcal{O}_X)$ with unit group $\Gamma(X,\mathcal{O}_X^\times)$. The second class is the derivations of $\mathcal{O}_X$, the vector fields, forming the tangent sheaf $\mathcal{T}_X = \mathcal{D}er_k(\mathcal{O}_X)$, a sheaf of Lie algebras and of modules over $\mathcal{O}_X$, and the $\mathcal{O}_X$-dual of the cotangent sheaf $\Omega^1_{X/k}$. On affine space the vector fields are the free module on the partial derivations, the Euler field generates the grading, and on projective space the global vector fields are $\mathrm{sl}_{n+1}(k)$.

The third class is the automorphisms of the variety, the invertible ring endomorphisms of the structure sheaf; on an affine variety they are the $k$-algebra automorphisms of the coordinate ring, and they act on the operator layer by conjugation, fixing the multiplication operators exactly when they act trivially on the global functions. An endomorphism pulls back rational functions on the function field and acts on the cohomology of a quasi-coherent sheaf by $\varphi^*$, and the alternating trace of that action on $H^\bullet(X,\mathcal{O}_X)$ is the Lefschetz number. The four articles that follow read the same layer through one operator each: the Galois action of the base field, the Frobenius of characteristic $p$, the pullback of a general morphism, and the divisor map; the last reads the layer through the differential operators generated by the vector fields.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{O}_X$, $\Gamma(X,\mathcal{O}_X)$ | structure sheaf; ring of global functions |
| $\mathcal{E}nd(\mathcal{O}_X)=\mathcal{H}om_{\mathcal{O}_X}(\mathcal{O}_X,\mathcal{O}_X)$ | operator layer of endomorphisms of the structure sheaf |
| $m_s$, $m_s(t)=st$ | multiplication operator by a function $s$ |
| $\mathcal{O}_X^\times$, $\Gamma(X,\mathcal{O}_X^\times)$ | sheaf of units; group of invertible global functions |
| $\mathcal{D}er_k(\mathcal{O}_X)$ | sheaf of $k$-derivations of the structure sheaf |
| $\mathcal{T}_X=\mathcal{D}er_k(\mathcal{O}_X)$ | tangent sheaf; the vector fields |
| $[D_1,D_2]=D_1D_2-D_2D_1$ | Lie bracket of derivations |
| $(fD)(g)=fD(g)$ | $\mathcal{O}_X$-module structure on the vector fields |
| $\Omega^1_{X/k}$ | cotangent sheaf; $\mathcal{T}_X$ is its $\mathcal{O}_X$-dual |
| $E=\sum_ix_i\partial_i$ | Euler derivation of the polynomial ring |
| $\operatorname{Aut}(X)$, $\varphi^*$ | automorphism group; pullback of functions |
| $\mathrm{Ad}_\varphi(T)=(\varphi^*)^{-1}T\varphi^*$ | conjugation action of an automorphism on the operator layer |
| $k(X)$ | function field; rational functions pulled back by a dominant map |
| $\varphi^*$ on $H^i$ | action of an endomorphism on cohomology |
| $\sum_i(-1)^i\operatorname{tr}(\varphi^*\vert H^i(X,\mathcal{O}_X))$ | Lefschetz number of an endomorphism |

## Further Reading

- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), for the tangent sheaf, its duality with the cotangent sheaf and the vector fields on projective space.
- Igor R. Shafarevich, *Basic Algebraic Geometry 1* (Springer, third edition, 2013), for derivations of a coordinate ring and the automorphism groups of the affine and projective spaces.
- David Eisenbud, *Commutative Algebra with a View Toward Algebraic Geometry* (Springer, 1995), for the module of Kähler differentials and the universal property of the derivation.
- James E. Humphreys, *Linear Algebraic Groups* (Springer, 1975), for the identification of the derivations with the Lie algebra of the automorphism group.
- Michel Demazure and Pierre Gabriel, *Introduction to Algebraic Geometry and Algebraic Groups* (North-Holland, 1980), for the functor-of-points reading of the automorphism group.
- Alexander Grothendieck and Jean Dieudonné, *Éléments de géométrie algébrique IV* (Publications Mathématiques de l'IHÉS, 1964–1967), for the relative tangent and cotangent sheaves.
