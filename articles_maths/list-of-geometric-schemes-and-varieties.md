
# __List of Geometric Schemes and Varieties__

## Introduction

This article lists the schemes, the varieties and the moduli spaces of the corpus, with the invariants attached to each. Every entry points to the article that introduces the object, and the article introduces nothing and proves nothing.

The list follows the construction of the theory. A scheme is a locally ringed space that is locally the spectrum of a ring, and it carries the functor of points, the fibre products and the local conditions — finite type, flat, smooth, étale, separated and proper — by which the geometric properties are stated. A variety is the classical case of a reduced scheme of finite type over a field, with the Zariski topology, the function field, the rational maps and the blow-up. The coherent sheaves are the coefficients of the theory, their cohomology gives the invariants — the Hilbert polynomial, the Euler characteristic, the canonical sheaf and the genus — and the moduli spaces are the schemes and stacks that parametrise the varieties, the sheaves and the curves.

The article records examples and non-examples side by side. Beside the schemes and the varieties it lists the non-reduced schemes that are not varieties, the schemes that are not of finite type, the coefficients that fail to compare the algebraic theory with the analytic one, the moduli functors that have no fine moduli space, and the algebraic spaces and stacks that are not schemes, each with the failure named and the article that records it.

## Schemes and the Functor of Points

A scheme is a locally ringed space locally isomorphic to the spectrum of a ring, and the morphisms are the morphisms of locally ringed spaces.

| Object | The property it has | Introduced in |
|---|---|---|
| the spectrum $\operatorname{Spec} A$ | the prime ideals of $A$ with the Zariski topology and the structure sheaf | *Schemes* |
| a scheme $(X,\mathcal{O}_X)$ | a locally ringed space locally affine, with stalks the local rings | *Schemes* |
| the structure sheaf $\mathcal{O}_X$ | the sheaf of the functions, with $\mathcal{O}_{X,\mathfrak{p}} = A_{\mathfrak{p}}$ | *Schemes* |
| a morphism of schemes | a morphism of locally ringed spaces, $f^{\#} : \mathcal{O}_Y \to f_*\mathcal{O}_X$ | *Schemes* |
| an $S$-scheme $X \to S$ and the functor of points $X(T)$ | the relative viewpoint and the functor represented by the scheme | *Schemes* |
| the fibre product $X\times_SY$ and the fibre $X_s$ | the base change and the geometric fibres | *Schemes* |
| finite type, finite, flat, smooth, étale | the local conditions defining the geometric classes of morphisms | *Schemes* |
| a closed or open immersion | a locally closed subscheme, with the quotient or the localisation of the structure sheaf | *Schemes* |
| separated and proper morphisms | the closed diagonal, and properness by the valuative criterion | *Schemes* |
| the dimension $\dim X$ | the Krull dimension, equal to the transcendence degree of the function field | *Schemes* |
| reduced, normal, regular schemes | the local rings reduced, integrally closed, regular | *Schemes* |
| the cotangent sheaf $\Omega^1_{X/k}$ | the sheaf of Kähler differentials, the cotangent space $\mathfrak{m}_x/\mathfrak{m}_x^2$ | *Schemes* |
| a projective scheme $\operatorname{Proj} S$ | the projective spectrum of a graded ring, with the twisting sheaf | *Sheaves in Algebraic Geometry* |

The scheme is the object that carries the nilpotents, the arithmetic fibres and the geometrically meaningful base change, and the functor of points converts the scheme into a representable functor, so that the constructions on schemes are the constructions on their functors. The fibre product and the fibres are the operations that make a scheme over a base a family, and the local conditions on the morphisms classify the families.

## Varieties and the Classical Theory

A variety is the classical geometric object: a reduced scheme of finite type over a field, described by polynomial equations and studied through its coordinate ring and its function field.

| Object | The property it has | Introduced in |
|---|---|---|
| the affine variety $V(S)$ | the zero set of a set of polynomials, with the Zariski topology | *Algebraic Geometry* |
| the coordinate ring $k[X]$ | the quotient $k[x_1,\ldots,x_n]/I(X)$, its Krull dimension the dimension of the variety | *Algebraic Geometry* |
| the projective variety and its homogeneous coordinate ring | the zero set in $\mathbb{P}^n_k$ of homogeneous polynomials | *Algebraic Geometry* |
| the Zariski topology | the closed sets $V(\mathfrak{a})$: quasicompact, Noetherian, not Hausdorff | *Algebraic Geometry* |
| an irreducible variety | not the union of two proper closed subsets; the components are the maximal ones | *Algebraic Geometry* |
| a morphism of varieties and its pullback | a polynomial map and the ring map $\varphi^* : k[Y] \to k[X]$ | *Algebraic Geometry* |
| the function field $k(X)$ | the fraction field of $k[X]$, of transcendence degree $\dim X$ | *Algebraic Geometry* |
| a rational map and a birational map | a morphism on a dense open set; a rational map with a rational inverse | *Algebraic Geometry* |
| the blow-up $\tilde X \to X$ | the birational map that replaces a subvariety by a divisor | *Algebraic Geometry* |
| a smooth point and the singular locus | $\dim_kT_PX = \dim X$; the singular locus is closed and proper | *Algebraic Geometry* |
| the theorem of Bézout and the intersection multiplicity | the number of intersections of two plane curves, counted with multiplicity | *Algebraic Curves*, §Plane Curves |
| an arithmetic scheme | a scheme over $\mathbb{Z}$, with $\operatorname{Spec}\mathbb{Z}$ the base | *Algebraic Number Theory* |

The variety is the case of the scheme in which the structure sheaf has no nilpotents and the base is a field, and it is recovered from its coordinate ring, its function field or its points. The rational maps and the blow-ups are the birational operations, and the blow-up is the elementary move by which a rational map is made into a morphism; the singular locus and the tangent space at a point are the local invariants of the variety.

## Coherent Sheaves and the Invariants of a Scheme

The coherent sheaves are the coefficients of the cohomology of a scheme, and their cohomology gives the numerical invariants of the object.

| Object | The property it has | Introduced in |
|---|---|---|
| a quasi-coherent sheaf $\mathcal{F}$ | a sheaf of $\mathcal{O}_X$-modules locally associated with a module | *Sheaves in Algebraic Geometry* |
| a coherent sheaf | a quasi-coherent sheaf of finite type with finitely generated kernels on an affine cover | *Coherent Sheaves* |
| the equivalence $M \mapsto \widetilde M$ | the equivalence of the modules over $A$ and the quasi-coherent sheaves on $\operatorname{Spec} A$ | *Sheaves in Algebraic Geometry* |
| the twisting sheaf $\mathcal{O}_X(d)$ | the invertible sheaf of the projective space, with $\mathcal{O}(d)\otimes\mathcal{O}(e) \cong \mathcal{O}(d+e)$ | *Sheaves in Algebraic Geometry* |
| the canonical sheaf $\omega_X = \Lambda^n\Omega^1_{X/k}$ | the top exterior power of the cotangent sheaf | *Sheaves in Algebraic Geometry* |
| Serre duality | the pairing $\mathcal{F}\leftrightarrow\mathcal{F}^{\vee}\otimes\omega_X$ | *Sheaves in Algebraic Geometry* |
| the cohomology $H^i(X,\mathcal{F})$ | the derived functors of the global sections | *Coherent Sheaves* |
| the Euler characteristic $\chi(\mathcal{F})$ | the alternating sum of the dimensions of the cohomology | *Sheaves in Algebraic Geometry* |
| the Hilbert polynomial | the polynomial in $d$ giving $\chi(\mathcal{F}(d))$ for large $d$ | *Sheaves in Algebraic Geometry* |
| the algebraic de Rham complex $\Omega^\bullet_{X/k}$ | the complex of the differential forms, with its hypercohomology | *Sheaves in Algebraic Geometry* |
| the Picard group and the Jacobian | the group of the line bundles and its moduli, of dimension $g$ on a curve | *Moduli Spaces* |

The coherent sheaves are the natural coefficients for the cohomology of a scheme, and the two invariants of the theory — the Hilbert polynomial and the Euler characteristic — are computed from them. The canonical sheaf is the sheaf of the top differentials and enters the Serre duality and the Riemann–Roch theorem, and the Picard group is the group of the invertible sheaves, whose degree-zero part on a curve is the Jacobian.

## Moduli Spaces

A moduli space is the scheme or stack that parametrises a family of objects up to isomorphism, and the moduli functor is the functor it represents.

| Object | The property it has | Introduced in |
|---|---|---|
| the moduli functor $\mathcal{M}$ | the functor of the families of objects up to isomorphism | *Moduli Spaces* |
| a fine moduli space | a scheme representing the functor, with a universal family | *Moduli Spaces* |
| a coarse moduli space | a space with a natural map from the functor, bijective on geometric points but without a universal family | *Moduli Spaces* |
| the GIT quotient $X/\!/G$ | the quotient of the semistable locus by the group, the projective construction | *Moduli Spaces* |
| the Hilbert scheme $\mathcal{H}ilb_S^\Phi$ | the scheme parametrising the subschemes with a fixed Hilbert polynomial | *Moduli Spaces* |
| the Quot scheme | the scheme parametrising the quotients of a fixed sheaf with a fixed Hilbert polynomial | *Moduli Spaces* |
| the moduli space $M_g$ of curves | the coarse moduli space of the curves of genus $g$, of dimension $3g-3$ | *Moduli Spaces* |
| the stable-curve compactification $\overline M_g$ | the projective compactification by the stable curves | *Moduli Spaces* |
| the moduli space $M(r,d)$ of stable bundles | the coarse moduli of the stable vector bundles on a curve, of dimension $r^2(g-1)+1$ | *Moduli Spaces* |
| the Jacobian as $M(1,d)$ | the moduli of the line bundles of degree $d$, of dimension $g$ | *Moduli Spaces* |
| a Deligne–Mumford stack and a coarse space | the stack with finite automorphism groups, with its coarse moduli space | *Moduli Spaces* |
| an algebraic space, and Artin's theorem on algebraic stacks | the quotient of a scheme by an étale equivalence relation, of which a stack with finite stabilisers is the generalisation | *Moduli Spaces* |

The moduli space is constructed as a quotient of a Hilbert or Quot scheme by a reductive group, and the distinction between the fine and the coarse moduli space is the presence or the absence of a universal family. The spaces $M_g$, $M(r,d)$ and the Jacobian are the three instances of the corpus, and the stacks and algebraic spaces are the objects that resolve the automorphism-group obstruction that prevents the existence of a fine moduli space.

## Warnings

An object that a reader may expect among the schemes and varieties, and does not find, is recorded with the reason.

| Object | Why it is not listed as a scheme or a variety of the list | Introduced in |
|---|---|---|
| the non-reduced scheme $\operatorname{Spec} k[x]/(x^2)$ | a scheme with nilpotents, not a variety | *Schemes* |
| a scheme that is not of finite type | not a variety, and not the local model of one | *Schemes* |
| a non-separated scheme | the Zariski topology is not Hausdorff; separatedness is the substitute, and without it the intersection theory fails | *Schemes* |
| the constant sheaf on a variety over $\mathbb{C}$ | its Zariski cohomology differs from the singular cohomology; the comparison needs the étale or the analytic topology | *Sheaves in Algebraic Geometry*, §The Comparison with the Topological Theory |
| a moduli functor without a fine moduli space | the objects have non-trivial automorphisms, so only a coarse space or a stack exists | *Moduli Spaces* |
| an algebraic stack that is not a scheme | a quotient groupoid with infinite stabilisers, not representable by a scheme | *Moduli Spaces* |

## Summary

This article has listed the schemes, varieties and moduli spaces of the corpus with their invariants. The schemes open the list, with the spectrum, the structure sheaf, the morphisms, the functor of points, the fibre products and the local conditions, and with the projective spectrum; the varieties follow, with the coordinate ring, the Zariski topology, the function field, the rational maps, the blow-up and the smooth and singular loci; the coherent sheaves are recorded with the twisting and canonical sheaves, the Serre duality, the cohomology, the Hilbert polynomial and the de Rham complex; and the moduli spaces close the list, with the moduli functor, the fine and coarse spaces, the GIT quotient, the Hilbert and Quot schemes, $M_g$, $M(r,d)$, the Jacobian, the Deligne–Mumford stacks and the algebraic spaces. Beside the examples stand the non-examples: a non-reduced scheme is not a variety, a non-separated scheme is not the setting for the intersection theory, the constant sheaf is the wrong coefficient system for the Zariski topology, and a moduli functor need not have a fine moduli space.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following, and they are the symbols of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $\operatorname{Spec} A$, $\operatorname{Proj} S$, $D(f)$, $V(\mathfrak{a})$ | Spectrum, projective spectrum, distinguished open, closed set |
| $\mathcal{O}_X$, $\mathcal{O}_X(d)$, $\omega_X$ | Structure sheaf, twisting sheaf, canonical sheaf |
| $X\times_SY$, $X(T)$, $X_s$ | Fibre product, functor of points, fibre |
| $k[X]$, $k(X)$, $I(X)$, $V(S)$ | Coordinate ring, function field, vanishing ideal, zero set |
| $\Omega^1_{X/k}$, $H^i(X,\mathcal{F})$, $\chi(\mathcal{F})$ | Cotangent sheaf, cohomology, Euler characteristic |
| $M_g$, $\overline M_g$, $M(r,d)$, $\mathcal{H}ilb_S^\Phi$ | Moduli spaces and Hilbert scheme |
| $X/\!/G$ | GIT quotient |
| $\mathbb{Z}$, $\mathbb{C}$ | The standard number systems of the corpus |
| $\mathbb{P}^n_k$ | Projective space over $k$, the ambient of a projective variety |
| $\mathfrak{p}$, $\mathfrak{m}_x$, $\mathcal{M}$ | Prime ideal; maximal ideal of a point; moduli functor |

## Further Reading

- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), for the schemes, the varieties, the coherent sheaves and the cohomology.
- Alexander Grothendieck and Jean Dieudonné, *Éléments de Géométrie Algébrique* (Publications Mathématiques de l'IHÉS, 1960–1967), for the foundations of the scheme theory and the functor of points.
- David Mumford, John Fogarty and Frances Kirwan, *Geometric Invariant Theory* (Springer, 3rd ed. 1994), for the GIT quotients and the construction of the moduli spaces.
- Joseph Harris and Ian Morrison, *Moduli of Curves* (Springer, 1998), for the moduli space $M_g$, its compactification and the construction of the coarse spaces.
