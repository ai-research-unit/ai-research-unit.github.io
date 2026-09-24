
# __Moduli Spaces__

## Introduction

A moduli problem asks for a space whose points are the isomorphism classes of the objects of a given kind — curves of a fixed genus, vector bundles of fixed rank and degree on a curve, subschemes with a fixed Hilbert polynomial — and the algebraic theory of such spaces consists of two parts: a categorical formulation, in which the problem is a functor on the category of schemes and the space is a representing object, and a constructive part, in which the space is exhibited as a quotient of a simpler scheme by a group action or as a closed subscheme of a Grassmannian. The functorial formulation is the more informative: it records not only the objects but the families of objects over a base, and it distinguishes the two notions that the subject turns on, that of a **fine moduli space**, which represents the functor and therefore carries a universal family, and that of a **coarse moduli space**, which only receives a natural transformation from the functor and classifies the objects up to isomorphism without the universal family. The failure of representability is never an accident: it is caused by the automorphisms of the objects, since a family that is constant up to isomorphism but not constant as a family cannot be a pullback of a universal family, and the repair is either to rigidify the problem by adding structure, or to pass to the coarse space, or to work with a stack, which is not covered here.

This article develops the theory in its classical form. The first section formulates moduli functors, fine and coarse moduli spaces, and the universal family, with the elementary examples. The second treats the quotients by group actions, since the constructive existence theorems for moduli spaces all proceed by exhibiting the moduli problem as a quotient: the geometric invariant theory of Mumford produces the quotient of an open subscheme of a projective scheme by a reductive group as the projective spectrum of the ring of invariants, and the Hilbert–Mumford numerical criterion decides which points are stable. The third section states Grothendieck's representability theorem for the Hilbert and Quot functors, which supplies the projective scheme that is to be quotiented; the fourth and fifth apply the machinery to the two classical moduli problems, the curves of genus $g$ and the vector bundles on a curve, computing the dimensions by deformation theory and recording the compactifications; and the sixth section places the deformation theory in its functorial form, states Artin's criteria for the algebraicity of a moduli functor, and points forward to the stack-theoretic refinement. The relation to the earlier articles of the category is direct: the coherent sheaves and their cohomology are *Coherent Sheaves*, the geometry of schemes and their morphisms *Schemes*, the varieties *Algebraic Geometry*, and the cohomological computations *Sheaves in Algebraic Geometry*; the local Ext groups are the tangent and obstruction spaces, exactly as in the deformation-theoretic remark of *Coherent Sheaves*.

Two boundaries are respected throughout. The formal deformation theory — the deformation functors, the cotangent complex, the obstruction theory, the Schlessinger conditions — is Part I's *Deformation Theory*, and is cited rather than developed. The arithmetic of the moduli of curves, the moduli interpretation of the modular curves, and the applications to the arithmetic of elliptic curves belong to Part I's *Algebraic Curves*, *Elliptic Curves* and *The Riemann–Roch Theorem for Curves*, and to the analytic and arithmetic theories that follow; the present article takes the geometric side. Nothing in the article uses a distance, a measure or a limit; where the differential-geometric description of a moduli space arises (as in the description of the moduli of stable bundles on a curve by unitary representations of its fundamental group) the analytic input is deferred to Part III, while the topological input — the fundamental group and the covering spaces — is that of *The Fundamental Group and Covering Spaces*.

## Moduli Functors, Fine and Coarse Spaces

**Definition.** Let $S$ be a scheme and let $\mathcal{C}$ be a class of objects over $S$-schemes (schemes, sheaves, morphisms) with a notion of base change. The associated **moduli functor** is the contravariant functor

$$
\mathcal{M} : (\mathbf{Sch}/S)^{\mathrm{op}}\to\mathbf{Sets}, \qquad \mathcal{M}(T) = \{\text{objects over } T \text{ of the given kind}\}\big/\cong,
$$

or, in the more refined form that keeps the automorphisms, the functor to groupoids $T\mapsto$ the groupoid of such objects and their isomorphisms. A **fine moduli space** is a scheme $M$ over $S$ with an isomorphism $\mathcal{M}\cong h_M = \operatorname{Hom}_S(-,M)$; by Yoneda's lemma the functor is then represented by $M$, the identity of $M$ corresponds to a **universal family** $\mathcal{U}\to M$ with $\mathcal{M}(T) = \{$pullbacks of $\mathcal{U}\}$ for every $T$, and $M$ is unique up to unique isomorphism. A **coarse moduli space** is a scheme $M$ with a natural transformation $\mathcal{M}\to h_M$ such that (i) for every scheme $N$ and natural transformation $\mathcal{M}\to h_N$ there is a unique morphism $M\to N$ through which it factors, and (ii) the map on geometric points $\mathcal{M}(\operatorname{Spec}\bar k)\to M(\bar k)$ is a bijection.

**Theorem (the universal family and the failure of representability).** Let $\mathcal{M}$ be a moduli functor.

1. If $\mathcal{M}$ is representable by $M$, the universal family is $\mathcal{M}(M)$ evaluated at the identity of $M$, and for every $T$ the objects over $T$ are exactly the pullbacks of the universal family; a fine moduli space is determined up to unique isomorphism.
2. If $\mathcal{M}$ is representable and the objects admit nontrivial automorphisms, then every object must be pulled back from the universal family, and a nontrivial automorphism of an object over a point forces the automorphism group to act trivially on the base; for a moduli functor in groupoids the obstruction to representability is exactly the presence of objects with nontrivial automorphisms.
3. If a coarse moduli space exists it is unique up to unique isomorphism, and the natural transformation $\mathcal{M}\to h_M$ induces a bijection on geometric points; the coarse space exists whenever the moduli problem is bounded, the automorphism groups are finite and there is a quotient presentation, the three conditions verified in the cases below.

*Proof.* (1) is Yoneda's lemma applied to the definition. (2) For an object $x\in\mathcal{M}(k)$ with automorphism $\sigma\neq\mathrm{id}$, the corresponding morphism $\operatorname{Spec} k\to M$ together with $\sigma$ gives an automorphism of the pullback of the universal family; if the moduli problem is represented by $M$ the automorphism of the object must come from the identity on $M$, since the pullback of the universal family determines the morphism to $M$ up to the automorphisms of the object, and the construction of a family over $M\times A$ for a scheme $A$ on which the automorphism acts nontrivially contradicts the existence of a universal family. (3) is the standard uniqueness and existence statement, and its proof in the cases at hand is the content of the next three sections. $\square$

**Example (the Grassmannian, fine).** Fix a locally free sheaf $\mathcal{E}$ of rank $n$ on $S$ and an integer $r$. The functor $\mathcal{G}_r(\mathcal{E})$ with

$$
\mathcal{G}_r(\mathcal{E})(T) = \{\text{rank-}r \text{ locally free quotients of } \mathcal{E}_T\}\big/\cong
$$

is representable by the **Grassmannian** $\operatorname{Gr}_r(\mathcal{E})\to S$, a projective scheme over $S$: the universal quotient on the Grassmannian is the universal family, and the functor has no nontrivial automorphisms because a quotient has none. Taking $\mathcal{E} = \mathcal{O}_S^{n}$ gives the Grassmannian of $r$-planes in $n$-space, and $r = 1$ the projective space $\mathbb{P}^{n-1}_S$ as the moduli of hyperplanes.

**Example (a coarse moduli problem with automorphisms).** Let $\mathcal{M}(T)$ be the set of isomorphism classes of elliptic curves over $T$. It is not representable: every elliptic curve has a nontrivial automorphism $-1$, and the corresponding automorphism of the universal family would have to act trivially. The coarse moduli space is the $j$-line $\mathbb{A}^1$ (or $\mathbb{P}^1$), with the natural transformation given by the $j$-invariant, and the two curves with $j = 0$ and $j = 1728$ have larger automorphism groups and are the points where the coarse space fails to distinguish the extra structure; the fine moduli problem is representable only after rigidification by a level structure, which is the moduli interpretation of the modular curves. The arithmetic of the elliptic curves themselves is Part I's *Elliptic Curves*.

## Quotients by Group Actions

**Definition.** Let $G$ be a group scheme of finite type over a field $k$ acting on a $k$-scheme $X$. A morphism $\pi : X\to Y$ is a **categorical quotient** if it is $G$-invariant and every $G$-invariant morphism factors uniquely through it; it is a **geometric quotient** if in addition the fibres are the orbits and the map on sheaves has the appropriate exactness. A **linearisation** of the action is a $G$-equivariant invertible sheaf $\mathcal{L}$ on $X$, and a point $x$ is **semistable** for the linearisation if there is an invariant section of some $\mathcal{L}^{\otimes m}$, $m>0$, not vanishing at $x$, and **stable** if in addition the orbit is closed in the semistable locus and the stabiliser is finite.

**Theorem (geometric invariant theory).** Let $G$ be a reductive group over $k$ acting on a projective scheme $X$ with a linearisation by an ample $\mathcal{L}$.

1. The open subscheme $X^{ss}$ of semistable points admits a categorical quotient $X^{ss}\to X^{ss}/\!/G$ which is a good quotient: it is $G$-invariant, affine on affine pieces, identifies two points exactly when the closures of their orbits intersect, and has $\mathcal{O}_{X^{ss}/\!/G} = (\pi_*\mathcal{O}_{X^{ss}})^G$. The quotient is projective when $X$ is projective and is the projective spectrum of the ring of invariants.
2. The restriction of the quotient to the stable locus is a geometric quotient $X^{s}\to X^{s}/G$, whose fibres are the orbits.
3. **Hilbert–Mumford criterion**: a point is semistable, respectively stable, if and only if every one-parameter subgroup of $G$ has nonnegative, respectively positive, weight on it; the criterion reduces a stability question to the numerical theory of one-parameter subgroups, and it is the practical test.

*Proof.* (1) reduces to the affine case, where the quotient is $\operatorname{Spec}$ of the ring of invariants of a reductive group acting on a finitely generated algebra; the finiteness of the ring of invariants is Hilbert's theorem, and the good-quotient properties are the properties of invariants, proved by the Reynolds operator. (2) uses that closed orbits with finite stabiliser are separated by an invariant section and the quotient is then a principal bundle in the finite case. (3) is the numerical criterion, proved by reducing to $\mathbb{G}_m$ and using the decomposition of the affine coordinate ring into weight spaces. $\square$

**Corollary (the quotient of a projective scheme as a moduli space).** If $\mathcal{M}$ is a moduli functor which is presented as a quotient of an open subscheme $X^{s}$ of a projective scheme by a reductive group, then $\mathcal{M}$ has a coarse moduli space $X^{s}/G$, projective for $X$ projective, and the construction of moduli spaces reduces to the construction of the quotient presentation and the verification of the stability conditions. The moduli of curves and the moduli of vector bundles below are constructed in exactly this way, from the Quot scheme as the projective source and the reductive group as the change of basis or the change of embedding.

## The Hilbert and Quot Schemes

**Definition.** Let $S$ be a locally Noetherian scheme, $\mathcal{E}$ a coherent sheaf on $S$, and $\Phi$ a polynomial. The **Quot functor** is

$$
\mathcal{Q} uot_{\mathcal{E}/S}^{\Phi}(T) = \left\{\text{coherent quotients } \mathcal{E}_T\to\mathcal{F} \text{ flat over } T \text{ with Hilbert polynomial } \Phi\right\}\big/\cong,
$$

where the Hilbert polynomial is taken along the fibres. When $\mathcal{E} = \mathcal{O}_S$ and the quotient is required to be the structure sheaf of a closed subscheme, the functor is the **Hilbert functor** $\mathcal{H}ilb_S^\Phi$, whose values are the closed subschemes of $S\times T$ that are flat over $T$ with Hilbert polynomial $\Phi$.

**Theorem (Grothendieck's representability theorem).** Let $S$ be a Noetherian scheme, $\mathcal{E}$ a coherent sheaf on $S$ and $\Phi$ a polynomial. Then:

1. the Quot functor $\mathcal{Q} uot_{\mathcal{E}/S}^{\Phi}$ is representable by a projective $S$-scheme $\operatorname{Quot}_{\mathcal{E}/S}^{\Phi}$, and the Hilbert functor $\mathcal{H}ilb_S^\Phi$ by a closed subscheme $\operatorname{Hilb}_S^\Phi\subseteq\operatorname{Quot}$;
2. the representing object is constructed as a closed subscheme of a Grassmannian of quotients of a fixed vector bundle, the integer $m$ being chosen so that the Hilbert polynomial determines the quotient for all twists by $\mathcal{O}(m)$;
3. for a closed subscheme $Z\in\operatorname{Hilb}_S^\Phi$ over a point, the tangent space of the Hilbert scheme at $Z$ is $H^0(Z,\mathcal{N}_{Z/X})$ and the obstructions to deforming $Z$ lie in $H^1(Z,\mathcal{N}_{Z/X})$, with $\mathcal{N}_{Z/X}$ the normal sheaf, and the deformation functor is pro-representable when those groups are finite-dimensional.

*Proof.* (1) and (2): for $m$ large the functor $\mathcal{F}\mapsto\mathcal{F}(m)$ is represented by a quotient of a fixed finite-dimensional vector space, the map to the Grassmannian is a closed immersion, and the resulting subscheme of the Grassmannian represents the functor; the argument is Grothendieck's, and the flatness over $T$ is what makes the construction work in families. (3) is the identification of the first-order deformations of a closed immersion with the sections of the normal sheaf, computed from the exact sequence $0\to\mathcal{I}/\mathcal{I}^2\to\Omega^1_{X/S}|_Z\to\Omega^1_{Z/S}\to0$ and the cohomology of *Coherent Sheaves*, with the obstruction class in $H^1$ obtained from the same sequence; the relation to the deformation functors of Part I's *Deformation Theory* is that the functor is the one whose tangent space and obstruction space are these groups. $\square$

**Remark (the Chow variety, and why the Hilbert scheme is better).** The reduced scheme underlying the Hilbert scheme can be replaced by the **Chow variety**, which parametrises the cycles rather than the subschemes, and which is easier to construct but forgets the multiplicity structure of the families. The Hilbert scheme retains the scheme structure and the flatness over the base, which is what makes it able to carry a universal family and hence to serve as the source of the moduli of curves and of sheaves; the price is that the Hilbert scheme can be very singular, and the singularities are exactly the points at which the deformation theory has obstructions.

## The Moduli of Curves

**Definition.** Fix an integer $g\geq2$ and let $\mathcal{M}_g$ be the moduli functor

$$
\mathcal{M}_g(T) = \{\text{smooth projective curves of genus } g \text{ over } T\}\big/\cong,
$$

the curves being flat and proper over $T$ with connected fibres of arithmetic genus $g$. Let $\overline{\mathcal{M}}_g$ be the analogous functor with "stable curves" — connected, projective, with at worst nodes and finite automorphism group, of arithmetic genus $g$ — in place of smooth ones.

**Theorem (the moduli of curves).**

1. The functor $\mathcal{M}_g$ has a coarse moduli space $M_g$, a quasiprojective variety of dimension $3g-3$ over $k$, irreducible for every $g\geq2$; it is not a fine moduli space, since a curve with a nontrivial automorphism obstructs representability.
2. The tangent space to $M_g$ at the point $[C]$ is $H^1(C,T_C)$, of dimension $3g-3$, and the deformations of $C$ are unobstructed; the dimension count is
   $$\dim H^1(C,T_C) = -\chi(T_C) = 3g-3, \qquad \chi(T_C) = \deg T_C + (1-g) = 3-3g,$$
   using Riemann–Roch and $H^0(C,T_C) = 0$ for $g\geq2$.
3. The functor $\overline{\mathcal{M}}_g$ has a coarse moduli space $\overline M_g$, projective of dimension $3g-3$ and irreducible, containing $M_g$ as a dense open subscheme; the boundary parametrises the nodal degenerations. The spaces are constructed as quotients of open subschemes of a Hilbert scheme, the source being the Hilbert scheme of tricanonically embedded curves and the group the change of coordinates in projective space, and the stability conditions are verified by the Hilbert–Mumford criterion.
4. $\mathcal{M}_g$ is a Deligne–Mumford stack, the automorphism groups of the curves being finite, and $M_g$ is its coarse space; the stack-theoretic formulation repairs the failure of representability and carries a universal curve.

*Proof.* (1) and (3): the tricanonical embedding of a curve of genus $g\geq2$ realises it as a curve of degree $6g-6$ in $\mathbb{P}^{5g-6}$, with Hilbert polynomial fixed, so $\mathcal{M}_g$ is the quotient of the open subscheme of the Hilbert scheme consisting of the smooth tricanonical curves by the action of $\operatorname{PGL}_{5g-5}$; the quotient exists by geometric invariant theory, and the stable curves are the points at which the quotient is taken in the compactified Hilbert scheme; the dimension count and the irreducibility are the standard results of the theory. (2) the deformation space of a smooth curve is the first cohomology of its tangent sheaf, unobstructed because a smooth curve is a smooth variety and the obstruction space $H^2(C,T_C)$ vanishes for dimension reasons; the computation of the Euler characteristic is the Riemann–Roch theorem on a curve of Part I's *The Riemann–Roch Theorem for Curves* with $T_C = \omega_C^{-1}$ of degree $2-2g$ and $H^0(C,T_C) = 0$. (4) the finiteness of the automorphism groups is the standard theorem that a curve of genus at least two has finite automorphism group, so the moduli functor in groupoids is a Deligne–Mumford stack with the stated coarse space. $\square$

**Example (the low genera).** For $g = 0$ every smooth projective curve is isomorphic to $\mathbb{P}^1$ and the coarse moduli space is a single point; the moduli functor is nevertheless far from representable, since the automorphism group of $\mathbb{P}^1$ is infinite, and the stack quotient is the classifying stack of $\operatorname{PGL}_2$. For $g = 1$ the smooth projective curves are the elliptic curves, the coarse moduli space is the $j$-line, of dimension one, and the automorphism groups are finite — of order two generically, of orders four and six at $j = 1728$ and $j = 0$ — so the failure of representability is caused by the generic automorphism $-1$ rather than by infinitude. The formula $3g-3$ for the dimension is obtained as $h^1(C,T_C)$ and uses $H^0(C,T_C) = 0$: for an elliptic curve $H^0(C,T_C)$ is one-dimensional, an elliptic curve carrying a nonzero vector field, and this nonvanishing accounts for the dimension one. For $g = 2$ the space $M_2$ has dimension three and every curve is hyperelliptic, so that $M_2$ is the quotient of the space of binary sextics by $\operatorname{PGL}_2$; for $g\geq3$ the general curve is not hyperelliptic, and the hyperelliptic locus is a closed subvariety of dimension $2g-1$, the first of the special strata whose study is the enumerative geometry of the moduli space.

## The Moduli of Vector Bundles

**Definition.** Let $C$ be a smooth projective curve of genus $g$ over $k$ and let $r\geq1$, $d\in\mathbb{Z}$. Let $\mathcal{M}(r,d)$ be the moduli functor whose value at $T$ is the set of isomorphism classes of families of rank-$r$ degree-$d$ vector bundles on the fibres of $C\times T\to T$, and let $\mathcal{M}^{s}(r,d)$ be the analogous functor with stable bundles, a bundle $E$ being **stable** if for every proper nonzero subsheaf $F\subsetneq E$ the inequality of slopes holds:

$$
\frac{\deg F}{\operatorname{rank}F} < \frac{\deg E}{\operatorname{rank}E}, \qquad \mu(E) = \frac{\deg E}{\operatorname{rank}E},
$$

and **semistable** if the inequality is weak.

**Theorem (the moduli of vector bundles on a curve).**

1. For $g\geq2$ the functors $\mathcal{M}^{s}(r,d)\subseteq\mathcal{M}(r,d)$ have coarse moduli spaces $M^{s}(r,d)\subseteq M(r,d)$, quasiprojective of dimension
   $$r^2(g-1)+1,$$
 the locus of stable bundles being open and the semistable ones forming the projective quotient; the dimension is
   $$\dim\operatorname{Ext}^1(E,E) = h^1(C,\mathcal{E}nd E) = -\chi(\mathcal{E}nd E) = r^2(g-1)+1,$$
   using $\mathcal{E}nd E$ of degree zero and $\operatorname{Hom}(E,E) = k$ for stable $E$.
2. The tangent space of $M^{s}(r,d)$ at $[E]$ is $H^1(C,\mathcal{E}nd E)$ and the obstructions lie in $H^2(C,\mathcal{E}nd E) = 0$ by dimension, so the deformations are unobstructed; the infinitesimal automorphisms are $H^0(C,\mathcal{E}nd E) = k$, and it is this one-dimensional automorphism group — the scalars — that prevents representability and forces the coarse formulation or the stack.
3. The construction of the moduli space is a quotient presentation: the Quot scheme of quotients of a fixed bundle with the appropriate Hilbert polynomial parametrises the bundles with a chosen generating space of sections, the reductive group $\operatorname{GL}$ of change of the basis acts, and the quotient of the stable locus is $M^{s}(r,d)$; the stability condition in the sense of vector bundles agrees with the Hilbert–Mumford stability for this action.
4. For $r = 1$ the moduli space is the Jacobian of $C$, of dimension $g$, and for $g\geq1$ the stable bundles are the line bundles, so the theory specialises to the classical Picard variety; and $\mathcal{M}(r,d)$ is a Deligne–Mumford stack for the same reason as $\mathcal{M}_g$, with the coarse space $M(r,d)$.

*Proof.* (1) and (3): the Quot scheme of *Coherent Sheaves* supplies a projective scheme on which $\operatorname{GL}_N$ acts with a linearisation, and the moduli of semistable bundles is the geometric invariant theory quotient, by the theorem of the second section; the identification of the two notions of stability is a theorem of Gieseker and Maruyama, quoted as standard. (1)–(2) the deformation theory is the one of *Coherent Sheaves*: deformations of $E$ are classified by $\operatorname{Ext}^1(E,E) = H^1(C,\mathcal{E}nd E)$ and unobstructed because the second Ext group vanishes on a curve for dimension reasons, and $\chi(\mathcal{E}nd E) = \deg\mathcal{E}nd E + r^2(1-g) = r^2(1-g)$ gives the dimension. (4) the case $r=1$ is the classical theory of divisors and the Picard group, Part I's *Algebraic Curves*. $\square$

**Remark (the differential-geometric description).** A stable bundle of degree zero on a compact Riemann surface corresponds to an irreducible unitary representation of its fundamental group, so that the moduli space $M^{s}(r,0)$ is also the space of such representations modulo conjugation. The topological input is the fundamental group and its representations, treated in *The Fundamental Group and Covering Spaces* and *Homotopy Groups and Fibrations*; the analytic part of the theorem — the existence and uniqueness of the harmonic metric realising a stable bundle, which is a statement about a differential equation — requires the theory of Part III, and the theorem is recorded here only as the reason the moduli spaces of bundles on a curve carry a second, topological, description.

## Deformation Theory and Artin's Criteria

**Definition.** Let $k$ be a field and let $\mathcal{D}$ be a functor on the category of local artinian $k$-algebras with residue field $k$ — the **deformation functor** of an object $X_0$ over $k$, with $\mathcal{D}(A)$ the deformations of $X_0$ to $A$, that is, the objects over $\operatorname{Spec} A$ whose restriction to the closed point is $X_0$. A moduli functor $\mathcal{M}$ as above has a deformation functor at each point, and the local theory of the moduli problem is the theory of that functor; the general theory is Part I's *Deformation Theory*, and only the geometric statements used above are recorded here.

**Theorem (Artin's criteria, in outline).** Let $\mathcal{M}$ be a moduli functor on the category of schemes locally of finite type over a field, in groupoids.

1. If $\mathcal{M}$ is a **limit-preserving** functor — the value at a filtered limit of schemes is the filtered limit of the values — and is **locally of finite presentation**, and if the deformation functors at geometric points satisfy Schlessinger's conditions of Part I's *Deformation Theory* with finite-dimensional tangent and obstruction spaces, then $\mathcal{M}$ is represented by an **algebraic space**: a sheaf for the étale topology which is locally the quotient of a scheme by an étale equivalence relation.
2. The hypotheses hold for the moduli functors of this article, which is why their coarse spaces exist as algebraic spaces and, in the cases presented, as schemes or projective schemes obtained by explicit GIT quotients.
3. When the objects to be parametrised have finite automorphism groups — the curves and the stable bundles above — the correct home of the functor is the category of algebraic stacks, and the coarse space is recovered as its coarse moduli space.

*Pro.* (1) is Artin's theorem, whose proof approximates the functor by a scheme and verifies the effectivity of the descent data of Part I's *Descent Theory*; the finite-dimensionality of the deformation spaces is what makes the approximation possible at each step. (2) is the verification in each case, which for the Hilbert and Quot functors is Grothendieck's theorem and for the curves and bundles is the quotient construction of the previous sections. (3) is the theorem on the relation between stacks and their coarse spaces, stated. $\square$

**Remark (the three degrees of representability).** The subject is organised by the strength of the parametrisation. A **fine moduli space** represents the functor and carries a universal family; it exists when the objects are rigid, as for the Grassmannian and for the subschemes parametrised by the Hilbert scheme. A **coarse moduli space** classifies the objects up to isomorphism without the universal family; it exists much more often and is the classical object of study. An **algebraic stack** keeps the automorphism groups and represents the groupoid-valued functor; it is the correct notion when the automorphisms are finite and nonzero, and it recovers the coarse space by forgetting the automorphisms. The three are not competitors but a hierarchy, and the position of a given moduli problem in the hierarchy is determined by its deformation theory, that is, by the automorphism groups, the deformations and the obstructions computed in *Coherent Sheaves*.

## Summary

A moduli problem is a functor on the category of schemes, assigning to each base the objects of a fixed kind over it up to isomorphism. A fine moduli space represents the functor and carries a universal family, from which all families are pulled back; a coarse moduli space receives a natural transformation from the functor, is initial among such, and induces a bijection on geometric points. Representability fails exactly when the objects have nontrivial automorphisms, since the automorphisms of an object over a point must then act trivially on the base, so the classical moduli problems of curves and of bundles require either rigidification, or the coarse formulation, or the stack-theoretic refinement. The construction of the classical spaces proceeds through two ingredients: Grothendieck's theorem that the Hilbert and Quot functors are representable by projective schemes, which supplies the projective source, and geometric invariant theory, which supplies the quotient of an open subscheme by a reductive group as the projective spectrum of the ring of invariants, with the Hilbert–Mumford numerical criterion deciding stability.

Applying the machinery, the moduli of curves of genus $g\geq2$ has a coarse moduli space $M_g$ of dimension $3g-3$, quasiprojective and irreducible, obtained as the quotient of the tricanonically embedded curves in a Hilbert scheme, with tangent space $H^1(C,T_C)$ at a curve and unobstructed deformations, and a projective compactification $\overline M_g$ by stable curves; the moduli of stable vector bundles of rank $r$ and degree $d$ on a curve has a quasiprojective coarse moduli space of dimension $r^2(g-1)+1$, with tangent space $H^1(C,\mathcal{E}nd E)$ and unobstructed deformations, constructed as a quotient of a Quot scheme, and specialising for $r=1$ to the Jacobian. Both functors have finite automorphism groups on their stable loci and are the prototypical Deligne–Mumford stacks, with the coarse spaces as above. Finally, Artin's criteria give the general algebraic-space theorem for a limit-preserving moduli functor with finite-dimensional deformation spaces, and they identify the precise hypotheses under which the heuristic constructions of the classical theory produce an algebraic object.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{M}$, $\mathcal{M}(T)$ | moduli functor; objects over $T$ up to isomorphism |
| fine moduli space | scheme representing $\mathcal{M}$; universal family $\mathcal{U}\to M$ |
| coarse moduli space | $M$ with $\mathcal{M}\to h_M$ initial and bijective on geometric points |
| $h_M = \operatorname{Hom}_S(-,M)$ | functor of points of $M$ |
| $X^{ss}$, $X^{s}$, $X/\!/G$ | semistable and stable loci; GIT quotient |
| $\mathcal{H}ilb_S^\Phi$, $\operatorname{Quot}_{\mathcal{E}/S}^\Phi$ | Hilbert and Quot functors and their representing schemes |
| $\mathcal{N}_{Z/X}$, $\mathcal{I}/\mathcal{I}^2$ | normal sheaf and conormal sheaf; $T_Z\operatorname{Hilb} = H^0(Z,\mathcal{N}_{Z/X})$ |
| $M_g$, $\overline M_g$ | coarse moduli of curves of genus $g$; stable-curve compactification; $\dim = 3g-3$ |
| $M(r,d)$, $M^s(r,d)$ | coarse moduli of semistable and of stable bundles; $\dim = r^2(g-1)+1$ |
| $\mu(E) = \deg E/\operatorname{rank}E$ | slope; stability and semistability |
| $T_C = \omega_C^{-1}$, $\mathcal{E}nd E$ | tangent sheaf of a curve; endomorphism sheaf |
| Artin's criteria | limit-preserving, locally of finite presentation, finite-dimensional deformations $\Rightarrow$ algebraic space |







## Further Reading

- David Mumford, John Fogarty and Frances Kirwan, *Geometric Invariant Theory* (Springer, third edition, 1994), for the quotient theorems, the Hilbert–Mumford criterion and the construction of moduli spaces.
- Alexander Grothendieck, *Techniques de construction et théorèmes d'existence en géométrie algébrique IV: Les schémas de Hilbert* (Séminaire Bourbaki, 1961), for the representability of the Hilbert and Quot functors.
- Pierre Deligne and David Mumford, *The irreducibility of the space of curves of given genus* (Publications Mathématiques de l'IHÉS 36, 1969), for the moduli of stable curves and the compactification.
- David Mumford, *Projective invariants of projective structures and applications* and *Stability of projective varieties* (IHÉS, 1962–1977), for the moduli of vector bundles and the stability theory.
- Michael Artin, *Versal deformations and algebraic stacks* (Inventiones Mathematicae 27, 1974), for the criteria for algebraicity of a moduli functor.
- Joseph Le Potier, *Lectures on Vector Bundles* (Cambridge, 1997), for the moduli of bundles on a curve and the stability conditions.
