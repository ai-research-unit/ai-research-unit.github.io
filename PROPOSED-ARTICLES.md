# Proposed Articles – Revised List

**Status.** Merged. All 289 entries are now in `maths.md`, in the category and at the position given below, each carrying the `+` prefix that marks a planned article. This file stays as the record of what was proposed, of what was moved, merged or dropped, and of why. Where the two differ, `maths.md` is authoritative: `Random Dynamical Systems` was later moved from *Differential Equations* to *Dynamical Systems*. The links below were rewritten from `articles/` to `articles_maths/` when the corpus was split into a maths and a physics collection; every article proposed here is a mathematical one.

**Source.** The list suggested by the external AI (~421 distinct titles), revised here.

**Placement.** Entries were not appended to the end of their category. Each was placed at the point in the progression where the structures it uses have been introduced, so that the notes reading *the relation to X* point backwards. Where an article is a prerequisite of one already in the corpus, it precedes it.

**Rules applied.** These are the rules of `articles_maths/introduction-and-mathematical-conventions.md`, used as the acceptance test.

- **Law 1.** No category may use a structure it has not yet introduced. Entries whose scope needed a later part's structure were **moved** to the part where that structure exists, or their scope was **cut back** to what the earlier part supports.
- **Law 2.** The layers are strictly ordered, and algebra is the most fundamental. Within each part the entries are ordered so that every article precedes the articles that use it.
- **Law 3.** A revisited object belongs to the layer that revisits it. An object re-read through a limit is an analysis article, not an algebra one.
- **Distance rule.** If a concept needs a distance, a norm, a limit or an open set, it is not algebraic. Several entries were moved out of Parts I and II under this rule.
- **Pure mathematics.** No article is about an application of mathematics. Numerical analysis, control theory, signal and image processing, computer graphics, robotics, computer vision, cryptography as an engineering subject, mathematical finance, mathematical biology and operations research are excluded, and the introduction now states the rule in the section *Pure Mathematics*. The *Applications* slots of Parts I to III mean the concrete instances of a structure, not uses of it.
- **No physics.** The mathematical corpus keeps a concept with a physical origin only where its mathematical content is autonomous, and then stripped of every reference to physics. Physics-named entries were not carried over; they belong in `physics.md`.

**How to read.** Each category below lists only the **new** entries for that category; the entries a category already has stay in place and precede them. Slugs are provisional and have been checked for uniqueness against the 507 articles on disk and against the 543 entries of the two menus. New categories are marked *(new category)*. Scope notes are first-pass: enough to fix the boundary of the article, to be expanded to full house-style comments when the article is written.

**Size.** 289 new entries – 82 in Part I, 112 in Part II, 74 in Part III, 21 in Part IV – with five new categories, one new system, 45 merges and no title or slug collision with the existing corpus.

---

# Part I : Algebra

## Foundations of Algebra

## - Theory

+### <a href="articles_maths/order-theory-and-lattices.html">Order Theory and Lattices</a>
<!-- partial orders, total orders and well-orders; lattices, complete, distributive and modular lattices; Galois connections; the Knaster–Tarski theorem; the lattice of subsets, forward-referenced to the Boolean algebras of Part IV. -->

+### <a href="articles_maths/formal-logic-and-computability.html">Formal Logic and Computability</a>
<!-- first-order logic, formal systems and derivations; soundness and completeness; compactness and the Löwenheim–Skolem theorem; Turing machines and recursive functions; decidability and undecidability; Gödel's incompleteness theorems; the halting problem. -->

+### <a href="articles_maths/model-theory.html">Model Theory</a>
<!-- structures and languages; satisfaction and elementary equivalence; compactness; quantifier elimination; ultraproducts; the model theory of algebraically closed, real-closed and valued fields. -->

+### <a href="articles_maths/proof-theory-and-type-theory.html">Proof Theory and Type Theory</a>
<!-- natural deduction and the sequent calculus; cut elimination; normalisation; intuitionistic logic; the Curry–Howard correspondence; the lambda calculus; the categorical reading of proofs. -->

+### <a href="articles_maths/set-theoretic-foundations.html">Set-Theoretic Foundations</a>
<!-- the Zermelo–Fraenkel axioms and the axiom of choice; ordinals and cardinals; transfinite induction and recursion; the cumulative hierarchy; the independence of the continuum hypothesis; large cardinals in outline. -->

## Groups

## - Theory

+### <a href="articles_maths/solvable-and-nilpotent-groups.html">Solvable and Nilpotent Groups</a>
<!-- solvable groups, the derived series and the commutator subgroup; nilpotent groups and the lower central series; Hall subgroups; the Fitting and Frattini subgroups; examples from matrix groups. -->

+### <a href="articles_maths/group-cohomology.html">Group Cohomology</a>
<!-- the cohomology of a group, the standard resolution and the low-dimensional interpretations; $H^1$ and $H^2$ as derivations and as extensions; the Schur multiplier; the cohomology of finite groups. -->

+### <a href="articles_maths/combinatorial-group-theory.html">Combinatorial Group Theory</a>
<!-- free groups, presentations and the word problem; the Nielsen–Schreier theorem; the Kurosh subgroup theorem; HNN extensions and amalgamated products; the accessibility of finitely presented groups; Bass–Serre theory is treated in Part II, where the tree a group acts on is a topological space. -->

+### <a href="articles_maths/coxeter-groups.html">Coxeter Groups</a>
<!-- Coxeter systems and diagrams; the presentation of a Coxeter group; finite and affine Coxeter groups and the classification of the finite ones; the word problem; reflection groups and Weyl groups require a form and belong to Part II. -->

+### <a href="articles_maths/braid-groups.html">Braid Groups</a>
<!-- the braid group on $n$ strands and its presentation; the pure braid group; the relation to the symmetric group; the algebraic properties of the braid groups; mapping class groups and knot theory belong to Part II. -->

+### <a href="articles_maths/infinite-groups.html">Infinite Groups</a>
<!-- infinite groups and their properties; finitely generated infinite groups, torsion groups and the Burnside problem; the Tits alternative; the algebraic theory only, the geometric theory of Cayley graphs and growth belonging to Part II. -->

+### <a href="articles_maths/infinite-abelian-groups.html">Infinite Abelian Groups</a>
<!-- abelian groups as modules over $\mathbb{Z}$; free abelian groups and rank; torsion and torsion-free groups; divisible groups and their classification; the structure of infinite abelian groups, the finitely generated case being treated separately. -->

+### <a href="articles_maths/classification-of-finite-simple-groups.html">The Classification of Finite Simple Groups</a>
<!-- the statement of the classification; the alternating groups; the groups of Lie type; the sporadic groups; the Feit–Thompson theorem; the classification of groups of small order. -->

+### <a href="articles_maths/finite-simple-groups-of-lie-type.html">Finite Simple Groups of Lie Type</a>
<!-- the Chevalley, Steinberg, Suzuki–Ree and twisted groups as abstract finite groups; the classification of the finite simple groups of Lie type; the orders of the groups; the algebraic-group structure, the Zariski topology and the building-theoretic constructions belong to Part II. -->

## Rings and Fields

## - Theory

+### <a href="articles_maths/noetherian-and-artinian-rings.html">Noetherian and Artinian Rings</a>
<!-- the ascending and descending chain conditions; the Hilbert basis theorem; the Akizuki–Hopkins theorem; the relation to the finitely generated modules of Part I. -->

+### <a href="articles_maths/primary-decomposition.html">Primary Decomposition</a>
<!-- primary ideals and primary decomposition; the uniqueness of the associated primes; the relation to the Nullstellensatz and to the ideals of this part. -->

+### <a href="articles_maths/integral-extensions-and-krull-dimension.html">Integral Extensions and Krull Dimension</a>
<!-- integral extensions; the lying-over, going-up and going-down theorems; the Krull dimension; the dimension of a polynomial ring. -->

+### <a href="articles_maths/dedekind-domains-and-ideal-class-groups.html">Dedekind Domains and Ideal Class Groups</a>
<!-- Dedekind domains and the unique factorisation of ideals; fractional ideals; the ideal class group and the finiteness of the class number. -->

+### <a href="articles_maths/valuation-theory-and-henselian-rings.html">Valuation Theory and Henselian Rings</a>
<!-- valuations and valuation rings; the extension of valuations; the relation to the ordered fields of this part; the p-adic completions are treated in Part II, where a distance first appears; Hensel's lemma, Henselian rings and the lifting of factorisations. -->


+### <a href="articles_maths/algebraic-number-theory.html">Algebraic Number Theory</a>
<!-- number fields and rings of integers; ideals and unique factorisation; the ideal class group and Dirichlet's unit theorem; the Minkowski theory; the decomposition of primes; the relation to Galois theory. -->

+### <a href="articles_maths/global-fields.html">Global Fields</a>
<!-- number fields and function fields of curves over a finite field as the two kinds of global field; places and the product formula; the arithmetic of global fields. -->

+### <a href="articles_maths/galois-cohomology.html">Galois Cohomology</a>
<!-- the cohomology of a Galois group; the Galois cohomology of local and global fields; the relation to group cohomology and to class field theory. -->

+### <a href="articles_maths/kummer-theory.html">Kummer Theory</a>
<!-- abelian extensions of exponent $n$; the Kummer pairing; the relation to Galois cohomology and to the cyclotomic fields. -->

+### <a href="articles_maths/cyclotomic-fields.html">Cyclotomic Fields</a>
<!-- the cyclotomic polynomial and the cyclotomic field; the Galois group; the relation to the Galois theory of this part; the constructible polygons belong to Part II. -->

+### <a href="articles_maths/class-field-theory.html">Class Field Theory</a>
<!-- abelian extensions of local and global fields; the Artin reciprocity law; the Hilbert class field; the relation to Galois cohomology and to Kummer theory; the adelic formulation is treated in Part II. -->

+### <a href="articles_maths/elliptic-curves.html">Elliptic Curves</a>
<!-- elliptic curves and the group law; the Weierstrass equation; the Mordell–Weil theorem; the algebraic theory of elliptic curves and their isogenies; the L-function and modularity are treated in Part III. -->

+### <a href="articles_maths/algebraic-curves.html">Algebraic Curves</a>
<!-- affine and projective plane curves; the function field of a curve; divisors and the genus; the relation to algebraic number theory and to the Riemann–Roch theorem. -->

+### <a href="articles_maths/riemann-roch-theorem-for-curves.html">The Riemann–Roch Theorem for Curves</a>
<!-- divisors and linear systems on a curve; the classical Riemann–Roch theorem and Serre duality for curves; the genus as the first obstruction; the surface and Grothendieck forms require the sheaf and derived machinery of Part II. -->

+### <a href="articles_maths/grobner-bases-and-elimination-theory.html">Gröbner Bases and Elimination Theory</a>
<!-- monomial orders; the division algorithm; Gröbner bases and Buchberger's algorithm; the elimination theorem; the relation to polynomial rings and to ideal theory; resultants, discriminants and the elimination theorem, as the classical counterpart of Buchberger's algorithm. -->


+### <a href="articles_maths/invariant-theory.html">Invariant Theory</a>
<!-- the invariant ring of a group action; the Hilbert basis theorem for invariants; the nullcone; the relation to the symmetric algebras of this part and to representation theory. -->

+### <a href="articles_maths/symmetric-functions-and-schur-functions.html">Symmetric Functions and Schur Functions</a>
<!-- symmetric polynomials and symmetric functions; the elementary, complete and power-sum bases; the fundamental theorem of symmetric functions; the Schur functions and Young tableaux, the Jacobi–Trudi identity and the Littlewood–Richardson rule. -->


+### <a href="articles_maths/representation-theory-of-symmetric-groups.html">Representation Theory of Symmetric Groups</a>
<!-- the irreducible representations of the symmetric group; Young diagrams and Specht modules; the hook length formula. -->

+### <a href="articles_maths/schur-weyl-duality.html">Schur–Weyl Duality</a>
<!-- the double commutant theorem for the symmetric and general linear groups; the decomposition of tensor powers of the defining representation. -->

+### <a href="articles_maths/inverse-galois-problem.html">The Inverse Galois Problem</a>
<!-- the problem and its history; the solution for solvable groups; the relation to the classification of finite simple groups and to the Galois theory of this part. -->

+### <a href="articles_maths/real-algebraic-geometry.html">Real Algebraic Geometry</a>
<!-- real algebraic sets and semialgebraic sets; the Tarski–Seidenberg theorem; the relation to the real-closed fields of this part; o-minimality is treated in Part IV. -->

## - Applications

+### <a href="articles_maths/linear-codes-over-finite-fields.html">Linear Codes over Finite Fields</a>
<!-- linear codes over a finite field, generator and parity-check matrices; the Hamming and Reed–Solomon codes; the minimum distance and the decoding problem; the algebraic constructions only, the information-theoretic questions belonging elsewhere. -->


## Linear Spaces

## - Theory

+### <a href="articles_maths/module-categories.html">Module Categories</a>
<!-- the category of modules over a ring; functors and natural transformations between module categories; the relation to Morita equivalence and to the abelian categories. -->

+### <a href="articles_maths/abelian-and-grothendieck-categories.html">Abelian and Grothendieck Categories</a>
<!-- additive and abelian categories; kernels, cokernels and exact sequences; the Freyd–Mitchell embedding theorem; the relation to the module categories of this part; the Grothendieck categories, the categories with a generator and all colimits, and the Gabriel–Popescu theorem. -->


+### <a href="articles_maths/homological-algebra.html">Homological Algebra</a>
<!-- chain complexes and homology; exact sequences and the snake lemma; projective and injective resolutions; the relation to the modules of this part; the applications to sheaf cohomology and to algebraic topology belong to Part II. -->

+### <a href="articles_maths/derived-functors.html">Derived Functors</a>
<!-- left and right derived functors; the long exact sequence; the relation to Ext and Tor; the applications to sheaf cohomology belong to Part II. -->

+### <a href="articles_maths/ext-and-tor.html">Ext and Tor</a>
<!-- the functors Ext and Tor and their interpretations; the universal coefficient theorem; the Künneth formula; the applications to algebraic topology belong to Part II. -->

+### <a href="articles_maths/spectral-sequences.html">Spectral Sequences</a>
<!-- the notion of a spectral sequence; filtration and convergence; the Grothendieck spectral sequence; the Leray–Serre sequence of a fibration belongs to Part II. -->

+### <a href="articles_maths/derived-categories.html">Derived Categories</a>
<!-- the derived category of an abelian category; triangulated categories; the relation to derived functors; the applications to sheaf cohomology belong to Part II. -->

+### <a href="articles_maths/k-theory-of-rings.html">K-Theory of Rings</a>
<!-- the Grothendieck group $K_0$ of a ring and the projective modules that generate it; $K_1$ and the determinant; the higher K-groups are treated in Part II, where the topological constructions they need are available. -->

+### <a href="articles_maths/hochschild-homology.html">Hochschild Homology</a>
<!-- the Hochschild homology and cohomology of an algebra; the relation to the trace and to the determinant. -->

+### <a href="articles_maths/cyclic-homology.html">Cyclic Homology</a>
<!-- cyclic homology and its relation to Hochschild homology; the Connes exact sequence; the applications to noncommutative geometry belong to Part II. -->

+### <a href="articles_maths/deformation-theory.html">Deformation Theory</a>
<!-- deformations of algebras and of modules; the Kodaira–Spencer map; obstruction theory; the applications to moduli belong to Part II. -->

+### <a href="articles_maths/operads.html">Operads</a>
<!-- operads and their algebras; the little disks operad; the relation to the algebras of this part; the homotopy-theoretic applications belong to Part II; the bar and cobar constructions, and the algebra of operads. -->

+### <a href="articles_maths/multilinear-algebra.html">Multilinear Algebra</a>
<!-- multilinear maps and the tensor product; the universal property; the relation to the tensor, symmetric and exterior algebras of this part. -->

+### <a href="articles_maths/quiver-representations-and-representation-type.html">Quiver Representations and Representation Type</a>
<!-- quivers and their representations; path algebras; Gabriel's theorem on finite representation type; the finite, tame and wild representation types and the Drozd theorem. -->

+### <a href="articles_maths/auslander-reiten-theory.html">Auslander–Reiten Theory</a>
<!-- almost split sequences; the Auslander–Reiten quiver; the representation type of an algebra. -->

+### <a href="articles_maths/tilting-theory.html">Tilting Theory</a>
<!-- tilting modules and tilted algebras; the Brenner–Butler theorem; the relation to the derived categories of this part. -->

+### <a href="articles_maths/cluster-algebras.html">Cluster Algebras</a>
<!-- cluster algebras and their seeds; the Laurent phenomenon; the relation to quiver representations. -->


+### <a href="articles_maths/topoi.html">Topoi</a>
<!-- elementary and Grothendieck topoi; the logical and categorical content; the relation to the categories of this part; sheaves on a topological space belong to Part II. -->

+### <a href="articles_maths/sheaves-on-sites.html">Sheaves on Sites</a>
<!-- Grothendieck topologies and sites; sheaves on a site; the categorical content; the cohomological theory on a topological space belongs to Part II. -->

+### <a href="articles_maths/descent-theory.html">Descent Theory</a>
<!-- descent for sheaves and for modules; the relation to Grothendieck topologies; the geometric applications belong to Part II. -->

## Linear Algebras

## - Theory

+### <a href="articles_maths/central-simple-algebras-and-the-brauer-group.html">Central Simple Algebras and the Brauer Group</a>
<!-- central simple algebras over a field; the Skolem–Noether theorem; the relation to the division algebras and the matrix algebras of this part; the Brauer group of a field and the division algebras that represent its classes. -->


+### <a href="articles_maths/crossed-products.html">Crossed Products</a>
<!-- crossed products of algebras by group actions; the relation to the group algebras and to the central simple algebras of this part. -->

+### <a href="articles_maths/separable-algebras.html">Separable Algebras</a>
<!-- separable algebras over a commutative ring; the relation to the central simple algebras and to the étale algebras of this part. -->

+### <a href="articles_maths/frobenius-algebras.html">Frobenius Algebras</a>
<!-- Frobenius algebras and their properties; the relation to the symmetric algebras of this part and to Poincaré duality. -->

+### <a href="articles_maths/calabi-yau-algebras.html">Calabi–Yau Algebras</a>
<!-- Calabi–Yau algebras and their Hochschild homology; the relation to the derived categories of this part. -->

+### <a href="articles_maths/hopf-algebras.html">Hopf Algebras</a>
<!-- algebras, coalgebras and bialgebras; the antipode; the relation to the group algebras of this part and to tensor products of algebras. -->

+### <a href="articles_maths/quantum-groups.html">Quantum Groups</a>
<!-- quantised enveloping algebras; the quantum plane; the relation to the Hopf algebras of this part and to the root systems of the Lie algebras. -->

+### <a href="articles_maths/deformation-quantization.html">Deformation Quantization</a>
<!-- star products and formal deformations of an algebra; the relation to the Poisson algebras and to the deformation theory of this part. -->


+### <a href="articles_maths/koszul-duality.html">Koszul Duality</a>
<!-- Koszul algebras and their duals; the relation to quadratic algebras and to the operads of this part. -->

+### <a href="articles_maths/differential-graded-algebras.html">Differential Graded Algebras</a>
<!-- differential graded algebras and their homology; the relation to the homological algebra of this part. -->

+### <a href="articles_maths/differential-graded-categories.html">Differential Graded Categories</a>
<!-- differential graded categories and their modules; the relation to the derived categories of this part. -->

+### <a href="articles_maths/a-infinity-and-l-infinity-algebras.html">A-Infinity and L-Infinity Algebras</a>
<!-- $A_\infty$-algebras and their morphisms; the relation to the differential graded algebras of this part and to homotopy theory; the $L_\infty$-algebras, their relation to the Lie algebras and the Maurer–Cartan equation. -->


## - Applications

+### <a href="articles_maths/normed-division-algebras-and-the-hurwitz-theorem.html">Normed Division Algebras and the Hurwitz Theorem</a>
<!-- the four normed division algebras $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$; the Hurwitz theorem that there are no others; the Cayley–Dickson construction and the loss of associativity at each step; the relation to the division algebras and to the Clifford algebras of this part. -->

## Symmetric Linear Algebras

## - Theory


+### <a href="articles_maths/macdonald-and-hall-littlewood-polynomials.html">Macdonald and Hall–Littlewood Polynomials</a>
<!-- the Macdonald polynomials and their properties; the relation to the symmetric functions and to the double affine Hecke algebras; the Hall–Littlewood polynomials as the one-parameter deformation of the Schur functions. -->

+### <a href="articles_maths/hecke-algebras.html">Hecke Algebras</a>
<!-- the Hecke algebra of a Coxeter group; the relation to the representation theory of the symmetric group and to the quantum groups. -->

## Anti-symmetric Linear Algebras

## - Theory

+### <a href="articles_maths/universal-enveloping-algebras.html">Universal Enveloping Algebras</a>
<!-- the universal enveloping algebra of a Lie algebra; the Poincaré–Birkhoff–Witt theorem; the relation to the representations of Lie algebras. -->

+### <a href="articles_maths/lie-algebra-cohomology.html">Lie Algebra Cohomology</a>
<!-- the cohomology of a Lie algebra; the Chevalley–Eilenberg complex; the relation to deformation theory and to group cohomology; the deformations of a Lie algebra and their classification by the second cohomology group. -->


+### <a href="articles_maths/poisson-and-gerstenhaber-algebras.html">Poisson and Gerstenhaber Algebras</a>
<!-- Poisson algebras and the properties of the bracket; the relation to the symplectic and Poisson forms of Part II; the Gerstenhaber algebras and their relation to Hochschild cohomology. -->


+### <a href="articles_maths/graded-lie-algebras-and-lie-superalgebras.html">Graded Lie Algebras and Lie Superalgebras</a>
<!-- graded Lie algebras and their properties; the relation to the superalgebras and to the root systems of this part; the Lie superalgebras as the graded case. -->


+### <a href="articles_maths/vertex-algebras.html">Vertex Algebras</a>
<!-- vertex algebras and their modules; the state-field correspondence; the relation to the affine Lie algebras and to the symmetric algebra construction. -->

## Linear Spaces over Linear Algebras

## - Theory

+### <a href="articles_maths/character-theory.html">Character Theory</a>
<!-- the characters of the representations of a finite group; the orthogonality relations; the character table; the relation to the group algebras of this part. -->

+### <a href="articles_maths/induced-representations.html">Induced Representations</a>
<!-- induced and restricted representations; Frobenius reciprocity; the relation to the modules over a group algebra; the Mackey theory belongs to Part II; Frobenius reciprocity for the induced and the restricted representations. -->


+### <a href="articles_maths/projective-representations.html">Projective Representations</a>
<!-- projective representations and the Schur multiplier; the relation to group cohomology and to the representation theory of groups; the Schur multiplier of a group and its identification with the second cohomology group. -->


+### <a href="articles_maths/modular-representation-theory.html">Modular Representation Theory</a>
<!-- representations over a field of positive characteristic; the relation to the ordinary character theory and to the group algebras of this part; the Brauer characters and their relation to the ordinary characters. -->


+### <a href="articles_maths/blocks-and-defect-groups.html">Blocks and Defect Groups</a>
<!-- the blocks of a group algebra; the defect groups; the relation to the modular representation theory and to the Brauer characters. -->

+### <a href="articles_maths/integral-representations.html">Integral Representations</a>
<!-- representations over the integers; the relation to the modular representation theory and to the representations of finite groups. -->

# Part II : Topology

## Foundations of Topology

## - Theory

+### <a href="articles_maths/nets-filters-and-convergence.html">Nets, Filters and Convergence</a>
<!-- nets and filters; convergence in an arbitrary topological space; ultrafilters; the equivalence of the two formulations; the role of nets where no metric exists; the relation to the Tychonoff theorem; the convergence spaces and the categorical description of convergence. -->

+### <a href="articles_maths/paracompactness-and-partitions-of-unity.html">Paracompactness and Partitions of Unity</a>
<!-- paracompactness and the shrinking lemma; partitions of unity subordinate to a cover; the Smirnov metrisation theorem; the role of partitions of unity in the construction of smooth structures. -->

+### <a href="articles_maths/dimension-theory.html">Dimension Theory</a>
<!-- the covering dimension and the inductive dimensions; the invariance of dimension; the dimension of a manifold; the relation to the Lebesgue covering lemma. -->

+### <a href="articles_maths/continuum-theory.html">Continuum Theory</a>
<!-- continua and their properties; indecomposable continua; Peano spaces; the relation to compactness and to the dynamical systems of Part III. -->


+### <a href="articles_maths/baire-spaces-and-category.html">Baire Spaces and Category</a>
<!-- Baire spaces and the Baire category theorem; meagre sets; the relation to completeness and to the functional analysis of Part III. -->

+### <a href="articles_maths/proximity-spaces.html">Proximity Spaces</a>
<!-- proximity spaces and the proximity relation; the relation to the uniform spaces and to the topological spaces. -->


+### <a href="articles_maths/bornology.html">Bornology</a>
<!-- bornologies and bounded sets; the relation to the topological spaces and to the bounded sets of the functional analysis of Part III. -->

## Topology on Groups

## - Theory

+### <a href="articles_maths/abelian-topological-groups.html">Abelian Topological Groups</a>
<!-- abelian topological groups; the duality of a locally compact abelian group with its character group; the relation to the harmonic analysis of Part III. -->

+### <a href="articles_maths/pontryagin-duality.html">Pontryagin Duality</a>
<!-- the character group of a locally compact abelian group; Pontryagin duality and its consequences; the relation to Fourier analysis, treated in Part III. -->

+### <a href="articles_maths/geometric-group-theory.html">Geometric Group Theory</a>
<!-- Cayley graphs and word metrics; quasi-isometries; the Gromov boundary; the Milnor–Wolf theorem; the Švarc–Milnor lemma; the growth of groups. -->

+### <a href="articles_maths/hyperbolic-groups.html">Hyperbolic Groups</a>
<!-- Gromov-hyperbolic spaces and groups; the Morse lemma; the boundary at infinity; the classification of isometries; the Rips complex; the algorithmic properties of hyperbolic groups. -->

+### <a href="articles_maths/amenable-groups.html">Amenable Groups</a>
<!-- amenability and the Følner condition; the fixed-point property; the class of elementary amenable groups; the von Neumann conjecture and its failure; the topological case is treated in the same article. -->

+### <a href="articles_maths/bass-serre-theory.html">Bass–Serre Theory</a>
<!-- groups acting on trees; graphs of groups and their fundamental groups; the structure theorem; the theory of ends and the Stallings theorem; the tree is a topological space, which is why this article belongs to this part. -->

+### <a href="articles_maths/buildings-and-tits-systems.html">Buildings and Tits Systems</a>
<!-- buildings as simplicial complexes with the chamber topology; the Moufang property; Tits systems and BN-pairs; the classification of spherical and affine buildings; the relation to the finite simple groups of Lie type of Part I. -->

+### <a href="articles_maths/representation-theory-of-locally-compact-groups.html">Representation Theory of Locally Compact Groups</a>
<!-- the unitary representations of a locally compact group; the relation to the operator algebras of this part and to the harmonic analysis of Part III. -->

+### <a href="articles_maths/induced-representations-of-locally-compact-groups.html">Induced Representations of Locally Compact Groups</a>
<!-- induced representations of locally compact groups; the imprimitivity theorem; the relation to the Mackey theory and to the operator algebras of this part. -->

+### <a href="articles_maths/mackey-theory.html">Mackey Theory</a>
<!-- the Mackey machine for induced representations; the imprimitivity theorem; the relation to the representation theory of locally compact groups. -->

+### <a href="articles_maths/type-i-groups.html">Type I Groups</a>
<!-- type I groups and their representation theory; the relation to the operator algebras of this part and to the harmonic analysis of Part III. -->

+### <a href="articles_maths/property-t.html">Property (T)</a>
<!-- Kazhdan's property (T); the relation to the representation theory of locally compact groups and to the lattices in Lie groups; the relation to the ergodic theory of Part III. -->

+### <a href="articles_maths/lattices-in-lie-groups.html">Lattices in Lie Groups</a>
<!-- lattices in Lie groups; the relation to arithmetic groups and to homogeneous spaces; the relation to the ergodic theory of Part III. -->

+### <a href="articles_maths/arithmetic-groups.html">Arithmetic Groups</a>
<!-- arithmetic groups and their properties; the relation to lattices in Lie groups and to the algebraic number theory of Part I. -->

+### <a href="articles_maths/bruhat-tits-theory.html">Bruhat–Tits Theory</a>
<!-- the Bruhat–Tits building of a reductive group over a local field; the relation to buildings and Tits systems and to the p-adic Lie groups of this part. -->

+### <a href="articles_maths/p-adic-lie-groups.html">p-adic Lie Groups</a>
<!-- p-adic Lie groups and their Lie algebras; the relation to the Lie groups of this part and to the p-adic numbers of this part. -->

+### <a href="articles_maths/loop-groups.html">Loop Groups</a>
<!-- loop groups and their representations; the relation to the Kac–Moody groups and to the operator algebras of this part. -->

+### <a href="articles_maths/kac-moody-groups.html">Kac–Moody Groups</a>
<!-- Kac–Moody groups and their properties; the relation to the Lie groups of this part and to the root systems of Part I. -->

+### <a href="articles_maths/diffeomorphism-groups.html">Diffeomorphism Groups</a>
<!-- diffeomorphism groups of manifolds; the relation to the infinite-dimensional Lie theory of this part and to the geometry of this part. -->

## Topology on Rings and Fields

## - Theory

+### <a href="articles_maths/local-fields.html">Local Fields</a>
<!-- local fields and their completions; the p-adic fields; the structure of the multiplicative group; the residue field and ramification; the relation to the p-adic numbers and to the algebraic number theory of Part I. -->

+### <a href="articles_maths/adeles-and-ideles.html">Adeles and Ideles</a>
<!-- the ring of adeles and the group of ideles; the restricted product topology; the relation to the algebraic number theory of Part I and to the locally compact groups of this part; the relation to the automorphic forms of Part III. -->

+### <a href="articles_maths/rigid-analytic-geometry.html">Rigid Analytic Geometry</a>
<!-- affinoid algebras and rigid spaces; the maximum modulus principle; the relation to the non-Archimedean analysis of Part III and to the p-adic numbers of this part. -->

+### <a href="articles_maths/berkovich-spaces.html">Berkovich Spaces</a>
<!-- Berkovich analytic spaces; the relation to the rigid analytic geometry of this part and to the non-Archimedean analysis of Part III. -->

+### <a href="articles_maths/formal-schemes.html">Formal Schemes</a>
<!-- formal schemes and their properties; the relation to the completion of Part I and to the rigid analytic geometry of this part. -->

+### <a href="articles_maths/adic-spaces.html">Adic Spaces</a>
<!-- adic spaces and their properties; the relation to the rigid analytic geometry and to the formal schemes of this part. -->

+### <a href="articles_maths/perfectoid-spaces.html">Perfectoid Spaces</a>
<!-- perfectoid spaces and their properties; the relation to the adic spaces of this part and to the algebraic number theory of Part I. -->

## Topology on Linear Spaces

## - Theory

+### <a href="articles_maths/locally-convex-spaces.html">Locally Convex Spaces</a>
<!-- locally convex spaces and their properties; seminorms and Fréchet spaces; the relation to the topological vector spaces and to the normed spaces of this part; the LF spaces and the inductive limits of Fréchet spaces; the Montel spaces and the Heine–Borel property. -->

+### <a href="articles_maths/frechet-spaces.html">Fréchet Spaces</a>
<!-- Fréchet spaces and their properties; the relation to the locally convex spaces and to the Banach spaces of this part. -->



+### <a href="articles_maths/nuclear-spaces.html">Nuclear Spaces</a>
<!-- nuclear spaces and their properties; the relation to the locally convex spaces and to the topological tensor products of this part. -->

+### <a href="articles_maths/duality-theory.html">Duality Theory</a>
<!-- dual pairs and their properties; the weak and strong topologies; the Mackey–Arens theorem and the bipolar theorem; the relation to the locally convex spaces of this part; the weak and weak-star topologies; the strong topology on the dual; the Mackey–Arens theorem on the admissible topologies; the bipolar theorem and the polars of a dual pair. -->





+### <a href="articles_maths/topological-tensor-products.html">Topological Tensor Products</a>
<!-- completed tensor products; the relation to the balanced product of Part I and to the nuclear spaces of this part. -->

## Topology on Linear Algebras

## - Theory

+### <a href="articles_maths/locally-convex-and-frechet-algebras.html">Locally Convex and Fréchet Algebras</a>
<!-- Fréchet algebras and their properties; the relation to the Banach algebras and to the topological algebras of this part; the locally convex algebras and the topological algebras between which the Fréchet algebras sit. -->


+### <a href="articles_maths/topological-k-theory.html">Topological K-Theory</a>
<!-- topological K-theory and its properties; the relation to the operator algebras of this part and to the index theory of this part. -->

+### <a href="articles_maths/k-theory-of-operator-algebras.html">K-Theory of Operator Algebras</a>
<!-- the K-groups of a C*-algebra; the six-term exact sequence; the relation to the operator algebras of this part and to the index theory. -->

+### <a href="articles_maths/kk-theory.html">KK-Theory</a>
<!-- KK-theory and its properties; the relation to the K-theory of operator algebras and to the index theory of this part. -->

+### <a href="articles_maths/toeplitz-algebras.html">Toeplitz Algebras</a>
<!-- Toeplitz algebras and their properties; the relation to the operator algebras and to the index theory of this part. -->


+### <a href="articles_maths/graph-c-algebras.html">Graph C*-Algebras</a>
<!-- graph C*-algebras and their properties; the relation to the Cuntz algebras and to the operator algebras of this part; the Cuntz algebras as the graph C*-algebras of the one-vertex graphs. -->

+### <a href="articles_maths/groupoid-c-algebras.html">Groupoid C*-Algebras</a>
<!-- groupoid C*-algebras and their properties; the relation to the operator algebras of this part and to the group algebras of Part I. -->

+### <a href="articles_maths/crossed-products-of-c-algebras.html">Crossed Products of C*-Algebras</a>
<!-- crossed products of C*-algebras by group actions; the relation to the operator algebras of this part and to the crossed products of Part I. -->

+### <a href="articles_maths/locally-compact-quantum-groups.html">Locally Compact Quantum Groups</a>
<!-- the operator-algebraic notion of a quantum group; the relation to the Hopf algebras and quantum groups of Part I and to the operator algebras of this part. -->

## Quadratic Forms and Clifford Algebras

## - Theory

+### <a href="articles_maths/symplectic-reflection-algebras.html">Symplectic Reflection Algebras</a>
<!-- symplectic reflection algebras and their representations; the relation to the rational Cherednik algebras; the symplectic form is a structure of this part, which is why the article belongs here. -->

+### <a href="articles_maths/rational-cherednik-algebras.html">Rational Cherednik Algebras</a>
<!-- rational Cherednik algebras and their representations; the relation to the Hecke algebras and to the symplectic reflection algebras of this part. -->

+### <a href="articles_maths/spin-geometry.html">Spin Geometry</a>
<!-- spin structures and spin manifolds; the Dirac operator and the Lichnerowicz formula; the relation to the Clifford algebras of this part and to the index theory of this part; the analytic theory of the operator itself is treated in Part III. -->

+### <a href="articles_maths/characteristic-classes.html">Characteristic Classes</a>
<!-- the characteristic classes of a vector bundle: the Chern, Pontryagin, Stiefel–Whitney and Euler classes; the relation to the fibre bundles of this part and to the index theory. -->

+### <a href="articles_maths/conformal-geometry.html">Conformal Geometry</a>
<!-- conformal geometry and the conformal group; the relation to the Riemannian geometry and to the twistor construction. -->

+### <a href="articles_maths/mobius-and-lie-sphere-geometry.html">Möbius and Lie Sphere Geometry</a>
<!-- Möbius geometry and its properties; the relation to the conformal geometry and to the Lie sphere geometry of this part; the Lie sphere geometry and its relation to the Möbius geometry. -->


+### <a href="articles_maths/projective-geometry.html">Projective Geometry</a>
<!-- projective geometry and its properties; the relation to the projective spaces of this part and to the Klein correspondence; the projective spaces and their coordinates. -->

+### <a href="articles_maths/metric-geometry.html">Metric Geometry</a>
<!-- metric geometry and its properties; the relation to the Riemannian geometry of this part and to the Gromov–Hausdorff convergence. -->

## Geometry and Manifolds

## - Theory

+### <a href="articles_maths/differential-topology.html">Differential Topology</a>
<!-- transversality and Sard's theorem; degree theory; cobordism in outline; the relation to the algebraic topology of this part. -->

+### <a href="articles_maths/riemannian-geometry.html">Riemannian Geometry</a>
<!-- Riemannian metrics and connections; the curvature tensors; the Gauss–Bonnet theorem; the relation to the curvature and geodesics of this part and to the dynamical systems of Part III. -->

+### <a href="articles_maths/pseudo-riemannian-and-lorentzian-geometry.html">Pseudo-Riemannian and Lorentzian Geometry</a>
<!-- pseudo-Riemannian metrics and their properties; the relation to the Riemannian geometry and to the Lorentzian geometry of this part; the Lorentzian case of signature $(3,1)$ and its causal structure. -->


+### <a href="articles_maths/symplectic-geometry.html">Symplectic Geometry</a>
<!-- symplectic manifolds and their properties; the Darboux theorem; the relation to the symplectic forms of this part and to the Hamiltonian systems of Part III. -->

+### <a href="articles_maths/poisson-geometry.html">Poisson Geometry</a>
<!-- Poisson manifolds and their properties; the relation to the symplectic geometry of this part and to the Poisson algebras of Part I. -->

+### <a href="articles_maths/contact-geometry.html">Contact Geometry</a>
<!-- contact manifolds and their properties; the relation to the symplectic geometry and to the differential forms of this part. -->

+### <a href="articles_maths/kahler-geometry.html">Kähler Geometry</a>
<!-- Kähler manifolds and their properties; the relation to the complex manifolds and to the symplectic geometry of this part. -->


+### <a href="articles_maths/hermitian-geometry-and-almost-complex-structures.html">Hermitian Geometry and Almost Complex Structures</a>
<!-- Hermitian metrics and their properties; the relation to the Kähler geometry and to the complex manifolds of this part; the almost complex structures and the integrability condition. -->

+### <a href="articles_maths/quaternionic-geometry.html">Quaternionic Geometry</a>
<!-- quaternionic manifolds and their properties; the relation to the hyperkähler geometry and to the quaternions of Part IV. -->

+### <a href="articles_maths/hyperkahler-geometry.html">Hyperkähler Geometry</a>
<!-- hyperkähler manifolds and their properties; the relation to the quaternionic geometry and to the Calabi–Yau manifolds of this part. -->

+### <a href="articles_maths/calabi-yau-manifolds.html">Calabi–Yau Manifolds</a>
<!-- Calabi–Yau manifolds and their properties; the relation to the Kähler geometry of this part. -->

+### <a href="articles_maths/g2-and-spin7-manifolds.html">G2 and Spin(7) Manifolds</a>
<!-- G2 and Spin(7) manifolds and their properties; the relation to the exceptional holonomy and to the Clifford algebras of this part. -->

+### <a href="articles_maths/homogeneous-spaces.html">Homogeneous Spaces</a>
<!-- homogeneous spaces $G/H$; the relation to the Lie group actions and to the symmetric spaces of this part; the representation-theoretic and the geometric treatments are brought together here. -->

+### <a href="articles_maths/symmetric-spaces.html">Symmetric Spaces</a>
<!-- symmetric spaces and their classification; the relation to the homogeneous spaces and to the Lie groups of this part. -->

+### <a href="articles_maths/flag-manifolds.html">Flag Manifolds</a>
<!-- flag manifolds and their geometry; the relation to the homogeneous spaces of this part and to the representation theory of this part. -->

+### <a href="articles_maths/grassmannians-and-stiefel-manifolds.html">Grassmannians and Stiefel Manifolds</a>
<!-- Grassmannians and their geometry; the relation to the homogeneous spaces of this part and to the algebraic topology of this part; the Stiefel manifolds and their fibration over the Grassmannians. -->



+### <a href="articles_maths/lens-spaces.html">Lens Spaces</a>
<!-- lens spaces and their topology; the relation to the algebraic topology and to the manifolds of this part. -->

+### <a href="articles_maths/teichmuller-theory.html">Teichmüller Theory</a>
<!-- Teichmüller spaces and their properties; the relation to the moduli spaces and to the mapping class groups of this part. -->

+### <a href="articles_maths/mapping-class-groups.html">Mapping Class Groups</a>
<!-- mapping class groups and their properties; the relation to the Teichmüller theory of this part and to the braid groups of Part I. -->

+### <a href="articles_maths/hyperbolic-geometry.html">Hyperbolic Geometry</a>
<!-- hyperbolic geometry and its properties; the relation to the Riemannian geometry of this part and to the three-manifolds. -->

+### <a href="articles_maths/spherical-geometry.html">Spherical Geometry</a>
<!-- spherical geometry and its properties; the relation to the Riemannian geometry of this part. -->

+### <a href="articles_maths/euclidean-geometry.html">Euclidean Geometry</a>
<!-- Euclidean geometry and its properties; the relation to the Riemannian geometry of this part and to the isometries of this part. -->

+### <a href="articles_maths/non-euclidean-geometry.html">Non-Euclidean Geometry</a>
<!-- non-Euclidean geometry and its properties; the relation to the hyperbolic and spherical geometry of this part. -->

+### <a href="articles_maths/fractal-geometry.html">Fractal Geometry</a>
<!-- fractals and their properties; the Hausdorff dimension; the relation to the metric geometry of this part and to the dynamical systems of Part III. -->

+### <a href="articles_maths/gromov-hausdorff-convergence.html">Gromov–Hausdorff Convergence</a>
<!-- Gromov–Hausdorff convergence and its properties; the relation to the metric geometry and to the Riemannian geometry of this part. -->

+### <a href="articles_maths/symplectic-and-contact-topology.html">Symplectic and Contact Topology</a>
<!-- symplectic topology and its properties; the relation to the symplectic geometry of this part and to Floer homology; the contact topology and the Legendre submanifolds. -->

+### <a href="articles_maths/floer-homology.html">Floer Homology</a>
<!-- Floer homology and its properties; the relation to the symplectic topology of this part and to the algebraic topology of this part. -->


+### <a href="articles_maths/low-dimensional-topology.html">Low-Dimensional Topology</a>
<!-- low-dimensional topology and its properties; the relation to the three-manifolds and four-manifolds of this part; the three-manifolds and their geometrisation; the four-manifolds and their intersection forms. -->

+### <a href="articles_maths/knot-theory.html">Knot Theory</a>
<!-- knot theory and its properties; the relation to the braid groups of Part I and to the three-manifolds of this part. -->




+### <a href="articles_maths/cobordism-and-surgery-theory.html">Cobordism and Surgery Theory</a>
<!-- cobordism theory and its properties; the relation to surgery theory and to the algebraic topology of this part; the surgery of manifolds and the surgery exact sequence. -->

+### <a href="articles_maths/supergeometry.html">Supergeometry</a>
<!-- supermanifolds and their geometry; the relation to the superalgebras of Part I and to the graded structures of this part. -->

## Algebraic Topology  *(new category)*

## - Theory

+### <a href="articles_maths/the-fundamental-group-and-covering-spaces.html">The Fundamental Group and Covering Spaces</a>
<!-- homotopy of paths and maps; the fundamental group $\pi_1(X,x_0)$; change of basepoint; the fundamental group of the circle; simply connected spaces; functoriality; van Kampen's theorem; covering spaces and the lifting properties; the correspondence between the coverings of a space and the subgroups of its fundamental group; deck transformations and the universal cover. -->


+### <a href="articles_maths/cw-complexes-and-cellular-approximation.html">CW Complexes and Cellular Approximation</a>
<!-- CW complexes, cells, skeleta and attaching maps; the homotopy extension property; cellular approximation; the cellular boundary formula; the Euler characteristic. -->

+### <a href="articles_maths/simplicial-and-singular-homology.html">Simplicial and Singular Homology</a>
<!-- simplicial and singular homology; the chain complex, cycles and boundaries; the homology groups $H_n(X)$; functoriality and homotopy invariance; the Mayer–Vietoris sequence; the homology of spheres and graphs. -->

+### <a href="articles_maths/cohomology-and-the-universal-coefficient-theorem.html">Cohomology and the Universal Coefficient Theorem</a>
<!-- the cohomology groups $H^n(X; G)$; the universal coefficient theorem; cohomology with coefficients; the cohomology of a CW complex; the Bockstein homomorphism. -->

+### <a href="articles_maths/cup-and-cap-products.html">Cup and Cap Products</a>
<!-- the cup product on cohomology; the cohomology ring and graded-commutativity; the cap product; the Künneth formula; the cohomology of projective spaces and of tori. -->

+### <a href="articles_maths/poincare-duality.html">Poincaré Duality</a>
<!-- orientability and the fundamental class; Poincaré duality for closed manifolds; the intersection form; Lefschetz duality; applications to surfaces. -->

+### <a href="articles_maths/homotopy-groups-and-fibrations.html">Homotopy Groups and Fibrations</a>
<!-- the higher homotopy groups $\pi_n(X)$; the long exact sequence of a fibration; the homotopy groups of spheres; the Hopf fibration; the Hurewicz theorem; the Freudenthal suspension theorem. -->

+### <a href="articles_maths/the-leray-serre-spectral-sequence.html">The Leray–Serre Spectral Sequence</a>
<!-- the Leray–Serre spectral sequence of a fibration; the Atiyah–Hirzebruch spectral sequence; convergence and the comparison theorem; the cohomology of fibre bundles and homogeneous spaces. -->

+### <a href="articles_maths/model-categories-and-homotopy-theory.html">Model Categories and Homotopy Theory</a>
<!-- model categories and their homotopy theory; the homotopy category; the relation to the differential graded algebras of Part I. -->

+### <a href="articles_maths/higher-algebra-and-higher-categories.html">Higher Algebra and Higher Categories</a>
<!-- higher categories and higher algebras; the relation to homotopy theory and to the algebras of Part I. -->

+### <a href="articles_maths/stable-homotopy-theory.html">Stable Homotopy Theory</a>
<!-- spectra and stable homotopy; the stable homotopy groups of spheres; the relation to cobordism and to the algebraic topology of this part. -->

+### <a href="articles_maths/higher-algebraic-k-theory.html">Higher Algebraic K-Theory</a>
<!-- the higher K-groups of a ring; the plus construction and the classifying-space definition; the relation to the K-theory of rings of Part I and to the K-theory of operator algebras of this part. -->

+### <a href="articles_maths/the-fundamental-group-of-a-lie-group.html">The Fundamental Group of a Lie Group</a>
<!-- the fundamental group of a topological group is abelian; the fundamental groups of the classical groups; the universal cover of $SO(n)$ and the spin groups; the double cover $SU(2)\to SO(3)$. -->

+### <a href="articles_maths/homology-of-classical-groups-and-homogeneous-spaces.html">Homology of Classical Groups and Homogeneous Spaces</a>
<!-- the homology of $GL_n$, $SL_n$, $O(n)$, $SO(n)$, $U(n)$ and $SU(n)$; the homology of Grassmannians and Stiefel manifolds; Schubert calculus; the relation to the characteristic classes of this part. -->

+### <a href="articles_maths/degree-theory-and-the-brouwer-fixed-point-theorem.html">Degree Theory and the Brouwer Fixed Point Theorem</a>
<!-- the degree of a map between spheres; the Brouwer fixed point theorem; the Jordan–Brouwer separation theorem; the hairy ball theorem; the Lefschetz fixed point theorem. -->

## Sheaves and Cohomology  *(new category)*

## - Theory

+### <a href="articles_maths/presheaves-and-sheaves.html">Presheaves and Sheaves</a>
<!-- presheaves and sheaves on a topological space; the sheaf condition; stalks and germs; sheafification; the category of sheaves; the constant sheaf. -->

+### <a href="articles_maths/sheaf-cohomology.html">Sheaf Cohomology</a>
<!-- the derived-functor definition of sheaf cohomology; flabby and soft sheaves; the long exact sequence; the relation to singular cohomology; the de Rham complex as a resolution of the constant sheaf. -->

+### <a href="articles_maths/cech-cohomology.html">Čech Cohomology</a>
<!-- Čech cohomology with respect to an open cover; the comparison with sheaf cohomology; the Leray theorem; the Čech-to-derived spectral sequence; the nerve of a cover. -->

+### <a href="articles_maths/derived-functors-and-sheaf-cohomology.html">Derived Functors and Sheaf Cohomology</a>
<!-- the derived functors of the global sections functor; injective resolutions; the Grothendieck spectral sequence; the relation to the homological algebra of Part I. -->

+### <a href="articles_maths/sheaves-and-the-de-rham-complex.html">Sheaves and the de Rham Complex</a>
<!-- the de Rham complex as a resolution of the constant sheaf; the de Rham theorem; the comparison of de Rham and singular cohomology; the Poincaré lemma as a local statement. -->

+### <a href="articles_maths/sheaves-in-algebraic-geometry.html">Sheaves in Algebraic Geometry</a>
<!-- the structure sheaf of a scheme; coherent sheaves and their cohomology; Serre duality; the relation to the algebraic geometry of this part. -->

## Algebraic Geometry  *(new category)*

## - Theory

+### <a href="articles_maths/algebraic-geometry.html">Algebraic Geometry</a>
<!-- affine and projective varieties; the Nullstellensatz; morphisms and rational maps; the relation to commutative algebra and to sheaf theory. -->

+### <a href="articles_maths/schemes.html">Schemes</a>
<!-- the spectrum of a ring; the Zariski topology; the structure sheaf; schemes and their morphisms; the relation to the commutative algebra of Part I. -->

+### <a href="articles_maths/coherent-sheaves.html">Coherent Sheaves</a>
<!-- coherent and quasi-coherent sheaves on a scheme; their cohomology; the relation to the sheaf cohomology of this part and to the modules of Part I. -->

+### <a href="articles_maths/moduli-spaces.html">Moduli Spaces</a>
<!-- moduli problems and their representability; the moduli of curves and of vector bundles; the relation to the deformation theory of Part I and to the algebraic geometry of this part. -->

+### <a href="articles_maths/stacks.html">Stacks</a>
<!-- algebraic stacks and their moduli; the relation to the descent theory of Part I and to the moduli spaces of this part. -->

# Part III : Analysis

## Foundations of Analysis

## - Theory

+### <a href="articles_maths/descriptive-set-theory.html">Descriptive Set Theory</a>
<!-- Polish spaces and Borel sets; the projective hierarchy; analytic and coanalytic sets; the perfect set property; the relation to the descriptive topology of Part II; the descriptive topology of the Polish spaces and their Borel and analytic sets. -->

+### <a href="articles_maths/fourier-analysis-on-euclidean-spaces.html">Fourier Analysis on Euclidean Spaces</a>
<!-- the Fourier transform on $\mathbb{R}^n$ and its properties; the inversion theorem and Plancherel's theorem; Schwarz functions and tempered distributions in outline; the relation to the harmonic analysis of this part. -->

+### <a href="articles_maths/convex-analysis.html">Convex Analysis</a>
<!-- convex sets and convex functions; the subdifferential; the Fenchel conjugate; the supporting hyperplane theorem; the relation to the variational methods of this part. -->

+### <a href="articles_maths/nonsmooth-and-variational-analysis.html">Nonsmooth and Variational Analysis</a>
<!-- nonsmooth functions and their subdifferentials; the Clarke subdifferential; the relation to convex analysis and to the variational analysis of this part; the variational problems, the direct method and the existence of minimisers. -->


+### <a href="articles_maths/geometric-measure-theory.html">Geometric Measure Theory</a>
<!-- rectifiable sets and currents; the area and coarea formulae; the plateau problem; the relation to the minimal surfaces of this part. -->

+### <a href="articles_maths/potential-theory.html">Potential Theory</a>
<!-- harmonic functions and the Dirichlet problem; potentials and capacity; the relation to the harmonic analysis and to the partial differential equations of this part. -->

## Analysis on Groups

## - Theory

+### <a href="articles_maths/noncommutative-harmonic-analysis.html">Noncommutative Harmonic Analysis</a>
<!-- harmonic analysis on non-abelian groups; the relation to the representation theory of locally compact groups of Part II and to the operator algebras of Part II. -->

+### <a href="articles_maths/the-plancherel-theorem.html">The Plancherel Theorem</a>
<!-- the Plancherel theorem for locally compact groups; the Plancherel measure; the relation to the harmonic analysis and to the representation theory of this part. -->

+### <a href="articles_maths/the-peter-weyl-theorem.html">The Peter–Weyl Theorem</a>
<!-- the Peter–Weyl theorem for compact groups; the decomposition of $L^2(G)$; the relation to the representation theory of Part II and to the harmonic analysis of this part. -->

+### <a href="articles_maths/the-convolution-algebra-l1g.html">The Convolution Algebra $L^1(G)$</a>
<!-- the convolution algebra $L^1(G)$ of a locally compact group; the relation to the group algebras of Part I and to the operator algebras of Part II. -->

+### <a href="articles_maths/ergodic-theory-of-group-actions.html">Ergodic Theory of Group Actions</a>
<!-- ergodic and mixing actions; the mean ergodic theorem for group actions; the relation to the ergodic theory of this part and to the homogeneous dynamics. -->

+### <a href="articles_maths/homogeneous-dynamics.html">Homogeneous Dynamics</a>
<!-- dynamics on homogeneous spaces $G/\Gamma$; unipotent flows; the relation to the lattices in Lie groups of Part II and to Ratner's theorems. -->

+### <a href="articles_maths/ratners-theorems.html">Ratner's Theorems</a>
<!-- Ratner's classification of unipotent flows and its consequences; the equidistribution of orbits; the relation to homogeneous dynamics. -->

+### <a href="articles_maths/equidistribution.html">Equidistribution</a>
<!-- equidistribution of sequences and of orbits; Weyl's criterion; the relation to the homogeneous dynamics and to the ergodic theory of this part. -->

+### <a href="articles_maths/automorphic-forms.html">Automorphic Forms</a>
<!-- automorphic forms on a reductive group; the relation to the adeles of Part II and to the representation theory of Part II; the relation to Tate's thesis and to the L-functions of this part. -->

+### <a href="articles_maths/the-langlands-program.html">The Langlands Program</a>
<!-- the Langlands program and its conjectures; the relation to automorphic forms and to the Galois representations of Part I. -->

## Analysis on Rings and Fields

## - Theory

+### <a href="articles_maths/p-adic-analysis.html">p-adic Analysis</a>
<!-- continuous and analytic functions on the p-adic numbers; the p-adic exponential and logarithm; the relation to the local fields of Part II. -->

+### <a href="articles_maths/p-adic-integration.html">p-adic Integration</a>
<!-- the Haar measure on the p-adic numbers; p-adic integration and its properties; the relation to the local fields of Part II and to the adelic analysis of this part. -->

+### <a href="articles_maths/p-adic-differential-equations.html">p-adic Differential Equations</a>
<!-- differential equations over a p-adic field; the Robba ring; the relation to the rigid analytic functions of this part. -->

+### <a href="articles_maths/rigid-analytic-functions.html">Rigid Analytic Functions</a>
<!-- analytic functions on a rigid space; the maximum modulus principle; the relation to the rigid analytic geometry of Part II. -->

+### <a href="articles_maths/adelic-analysis.html">Adelic Analysis</a>
<!-- analysis on the adeles and ideles; the Fourier transform on the adeles; the relation to the adeles of Part II and to Tate's thesis; Tate's thesis and the local and global zeta integrals. -->


+### <a href="articles_maths/l-functions.html">L-Functions</a>
<!-- Dirichlet L-functions and their properties; the functional equation; the relation to the zeta functions and to the analytic number theory of this part; the Dirichlet L-functions and their characters. -->

+### <a href="articles_maths/zeta-functions.html">Zeta Functions</a>
<!-- the Riemann zeta function and its properties; the Euler product and the functional equation; the relation to the prime number theorem and to the Riemann hypothesis. -->

+### <a href="articles_maths/analytic-number-theory.html">Analytic Number Theory</a>
<!-- the distribution of the primes; the methods of complex analysis applied to arithmetic; the relation to the zeta functions and to the L-functions of this part. -->

+### <a href="articles_maths/the-prime-number-theorem.html">The Prime Number Theorem</a>
<!-- the prime number theorem and its proof; the zero-free region; the relation to the zeta functions and to the analytic number theory of this part. -->

+### <a href="articles_maths/the-riemann-hypothesis.html">The Riemann Hypothesis</a>
<!-- the Riemann hypothesis and its consequences; the critical strip; the relation to the zeta functions and to the prime number theorem; the generalised Riemann hypothesis. -->


+### <a href="articles_maths/modular-forms.html">Modular Forms</a>
<!-- modular forms and their properties; the modular group and its congruence subgroups; the relation to the elliptic curves of Part I and to the automorphic forms of this part. -->

+### <a href="articles_maths/non-archimedean-functional-analysis.html">Non-Archimedean Functional Analysis</a>
<!-- Banach and normed spaces over a non-Archimedean field; the relation to the p-adic analysis of this part and to the functional analysis of this part. -->

## Analysis on Linear Spaces

## - Theory

+### <a href="articles_maths/the-schwartz-kernel-theorem.html">The Schwartz Kernel Theorem</a>
<!-- the Schwartz kernel theorem and its consequences; the relation to the topological tensor products of Part II and to the distributions of this part. -->

+### <a href="articles_maths/fredholm-theory.html">Fredholm Theory</a>
<!-- Fredholm operators and their index; the Fredholm alternative; compact perturbations; the relation to the index theory of Part II and to the spectral theory of operators. -->

+### <a href="articles_maths/pseudodifferential-operators.html">Pseudodifferential Operators</a>
<!-- pseudodifferential operators and their symbols; elliptic operators; the relation to the partial differential equations and to the microlocal analysis of this part. -->

+### <a href="articles_maths/microlocal-analysis.html">Microlocal Analysis</a>
<!-- the wavefront set and microlocal regularity; the propagation of singularities; the relation to the pseudodifferential operators of this part. -->

+### <a href="articles_maths/semiclassical-analysis.html">Semiclassical Analysis</a>
<!-- the semiclassical limit and its properties; the relation to the pseudodifferential operators of this part and to the partial differential equations; the mathematical content only. -->

+### <a href="articles_maths/nonlinear-functional-analysis.html">Nonlinear Functional Analysis</a>
<!-- nonlinear operators and their properties; monotone and accretive operators; the relation to the fixed point theory and to the partial differential equations of this part. -->

+### <a href="articles_maths/fixed-point-theory-and-degree-theory.html">Fixed Point Theory and Degree Theory</a>
<!-- the fixed point theorems of analysis; the contraction mapping principle; the Schauder and Kakutani theorems; the relation to the nonlinear functional analysis of this part; the Leray–Schauder degree and its use in existence theorems. -->


+### <a href="articles_maths/interpolation-theory.html">Interpolation Theory</a>
<!-- interpolation of Banach and Sobolev spaces; the real and complex methods; the relation to the function spaces of this part. -->

+### <a href="articles_maths/besov-and-triebel-lizorkin-spaces.html">Besov and Triebel–Lizorkin Spaces</a>
<!-- Besov spaces and their properties; the relation to the interpolation theory and to the Sobolev spaces of this part; the Triebel–Lizorkin spaces and their relation to the Besov spaces. -->


## Analysis on Linear Algebras

## - Theory

+### <a href="articles_maths/clifford-analysis.html">Clifford Analysis</a>
<!-- the analysis of functions with values in a Clifford algebra; the Dirac operator and monogenic functions; the Cauchy integral formula; the relation to the Clifford algebras of Part II; the monogenic and polymonogenic functions. -->

+### <a href="articles_maths/dirac-operators.html">Dirac Operators</a>
<!-- the analytic theory of Dirac operators; self-adjointness and the spectrum; the relation to the spin geometry of Part II and to the index theory of Part II. -->


+### <a href="articles_maths/fueter-theory.html">Fueter Theory</a>
<!-- Fueter's theory of regular functions of a quaternionic variable; the Cauchy–Fueter integral formula; the relation to the hypercomplex analysis of this part. -->

+### <a href="articles_maths/holomorphic-functional-calculus.html">Holomorphic Functional Calculus</a>
<!-- the holomorphic functional calculus for a Banach algebra; the relation to the Banach algebras of Part II and to the spectral theory of operators. -->

+### <a href="articles_maths/cyclic-cohomology.html">Cyclic Cohomology</a>
<!-- cyclic cohomology and its properties; the Connes exact sequence; the relation to the cyclic homology of Part I and to the operator algebras of Part II. -->

## Differential Equations

## - Theory

+### <a href="articles_maths/ricci-flow.html">Ricci Flow</a>
<!-- the Ricci flow equation; the evolution of curvature; the relation to the Riemannian geometry of Part II and to the partial differential equations of this part. -->

+### <a href="articles_maths/mean-curvature-flow.html">Mean Curvature Flow</a>
<!-- the mean curvature flow and its properties; the evolution of hypersurfaces; the relation to the partial differential equations of this part and to the minimal surfaces. -->

+### <a href="articles_maths/minimal-surfaces.html">Minimal Surfaces</a>
<!-- minimal surfaces and the variational problem they solve; the relation to the calculus of variations of this part and to the geometric measure theory of this part. -->

+### <a href="articles_maths/harmonic-maps.html">Harmonic Maps</a>
<!-- harmonic maps between Riemannian manifolds; the energy functional; the relation to the calculus of variations of this part and to the Riemannian geometry of Part II. -->

+### <a href="articles_maths/integrable-systems.html">Integrable Systems</a>
<!-- integrable systems and their properties; the Lax pair; the relation to the Hamiltonian systems and to the soliton theory of this part. -->

+### <a href="articles_maths/soliton-theory.html">Soliton Theory</a>
<!-- solitons and their properties; the inverse scattering transform; the relation to the integrable systems of this part. -->


+### <a href="articles_maths/lagrangian-and-hamiltonian-systems.html">Lagrangian and Hamiltonian Systems</a>
<!-- Hamiltonian systems and their properties; the symplectic form; the relation to the symplectic geometry of Part II and to the integrable systems of this part; the Lagrangian systems, the Euler–Lagrange equations and the Legendre transform between the two pictures. -->


+### <a href="articles_maths/stochastic-differential-equations.html">Stochastic Differential Equations</a>
<!-- stochastic differential equations; the Itô and Stratonovich integrals; the relation to the Brownian motion of this part and to the partial differential equations. -->

+### <a href="articles_maths/stochastic-partial-differential-equations.html">Stochastic Partial Differential Equations</a>
<!-- stochastic partial differential equations; the relation to the stochastic differential equations of this part and to the partial differential equations. -->

+### <a href="articles_maths/random-dynamical-systems.html">Random Dynamical Systems</a>
<!-- random dynamical systems; the multiplicative ergodic theorem; the relation to the dynamical systems of this part and to the stochastic differential equations. -->

+### <a href="articles_maths/delay-and-functional-differential-equations.html">Delay and Functional Differential Equations</a>
<!-- delay differential equations and their properties; the method of steps; the relation to the ordinary differential equations of this part; the functional differential equations of which the delay equations are the first case. -->


+### <a href="articles_maths/fractional-differential-equations.html">Fractional Differential Equations</a>
<!-- fractional derivatives and fractional differential equations; the relation to the partial differential equations of this part. -->

+### <a href="articles_maths/impulsive-differential-equations.html">Impulsive Differential Equations</a>
<!-- impulsive differential equations and their properties; the relation to the ordinary differential equations of this part. -->

+### <a href="articles_maths/differential-algebraic-equations.html">Differential-Algebraic Equations</a>
<!-- differential-algebraic equations and their properties; the index of a differential-algebraic equation; the relation to the ordinary differential equations of this part. -->

## Probability and Ergodic Theory  *(new category)*

## - Theory

+### <a href="articles_maths/measure-theoretic-probability.html">Measure-Theoretic Probability</a>
<!-- probability spaces and random variables; distributions and their properties; the relation to the measure theory of Part III; expectation and the standard limit theorems in outline. -->

+### <a href="articles_maths/independence-and-conditional-expectation.html">Independence and Conditional Expectation</a>
<!-- independence of events and of random variables; conditional expectation as a projection; filtrations; the relation to the martingales of this part. -->

+### <a href="articles_maths/laws-of-large-numbers-and-the-central-limit-theorem.html">Laws of Large Numbers and the Central Limit Theorem</a>
<!-- the strong and weak laws of large numbers; characteristic functions; the central limit theorem and its variants; the relation to the independence of this part. -->

+### <a href="articles_maths/martingales.html">Martingales</a>
<!-- martingales and their properties; the optional stopping theorem; the martingale convergence theorem; the relation to the conditional expectation of this part. -->

+### <a href="articles_maths/markov-chains-and-processes.html">Markov Chains and Processes</a>
<!-- Markov chains and their properties; stationarity and recurrence; the relation to the measure-theoretic probability of this part. -->

+### <a href="articles_maths/brownian-motion-and-stochastic-calculus.html">Brownian Motion and Stochastic Calculus</a>
<!-- Brownian motion and its properties; the Itô integral and Itô's formula; the relation to the stochastic differential equations of this part. -->

+### <a href="articles_maths/ergodic-theory.html">Ergodic Theory</a>
<!-- measure-preserving transformations; ergodicity and mixing; the Birkhoff and von Neumann ergodic theorems; the relation to the measure-theoretic probability of this part. -->

+### <a href="articles_maths/the-probabilistic-method.html">The Probabilistic Method</a>
<!-- the probabilistic method in combinatorics; random graphs and the first and second moment methods; the Lovász local lemma; the relation to the measure-theoretic probability of this part. -->

+### <a href="articles_maths/probabilistic-number-theory.html">Probabilistic Number Theory</a>
<!-- the distribution of arithmetic functions; the Erdős–Kac theorem; the relation to the analytic number theory of this part and to the measure-theoretic probability of this part. -->

+### <a href="articles_maths/random-walks-on-groups.html">Random Walks on Groups</a>
<!-- random walks on groups and their properties; recurrence and transience; the relation to the geometric group theory of Part II and to the measure-theoretic probability of this part. -->

## Dynamical Systems  *(new category)*

## - Theory

+### <a href="articles_maths/topological-dynamics.html">Topological Dynamics</a>
<!-- topological dynamical systems; recurrence and minimality; topological transitivity; the relation to the topological spaces of Part II and to the ergodic theory of this part. -->

+### <a href="articles_maths/smooth-dynamical-systems.html">Smooth Dynamical Systems</a>
<!-- smooth dynamical systems and their properties; fixed points and periodic orbits; the relation to the ordinary differential equations of this part. -->

+### <a href="articles_maths/hyperbolic-dynamics-and-anosov-systems.html">Hyperbolic Dynamics and Anosov Systems</a>
<!-- hyperbolic sets and Anosov systems; stable and unstable manifolds; the relation to the smooth dynamical systems of this part; the ergodic theory of the hyperbolic systems and the Bowen–Ruelle measure. -->

+### <a href="articles_maths/bifurcation-theory.html">Bifurcation Theory</a>
<!-- bifurcations and their classification; normal forms; the relation to the ordinary differential equations and to the dynamical systems of this part. -->

+### <a href="articles_maths/chaos-and-strange-attractors.html">Chaos and Strange Attractors</a>
<!-- chaos and its properties; strange attractors; the relation to the hyperbolic dynamics and to the topological dynamics of this part. -->

+### <a href="articles_maths/symbolic-dynamics.html">Symbolic Dynamics</a>
<!-- symbolic dynamics and subshifts; the shift space and coding; the relation to the topological dynamics of this part. -->

+### <a href="articles_maths/dynamics-and-number-theory.html">Dynamics and Number Theory</a>
<!-- the dynamics of arithmetic origin; the Gauss map and continued fractions; the relation to the homogeneous dynamics of this part. -->

+### <a href="articles_maths/the-geodesic-flow.html">The Geodesic Flow</a>
<!-- the geodesic flow of a Riemannian manifold; its ergodic properties; the relation to the Riemannian geometry of Part II and to the hyperbolic dynamics of this part. -->


# Part IV : Synthetic Studies

## Booleans

## - Algebra

+### <a href="articles_maths/heyting-algebras-and-intuitionistic-logic.html">Heyting Algebras and Intuitionistic Logic</a>
<!-- Heyting algebras and their properties; the algebraic semantics of intuitionistic logic; the relation to the Boolean algebras of this system and to the proof theory of Part I. -->

+### <a href="articles_maths/mv-algebras-and-many-valued-logic.html">MV-Algebras and Many-Valued Logic</a>
<!-- MV-algebras and their properties; the algebraic semantics of Łukasiewicz logic; the relation to the Boolean algebras of this system. -->

+### <a href="articles_maths/effect-algebras-and-orthomodular-lattices.html">Effect Algebras and Orthomodular Lattices</a>
<!-- effect algebras and orthomodular lattices; the algebraic content of the non-distributive logic; the relation to the Boolean algebras of this system; the mathematical content only. -->

+### <a href="articles_maths/quantales-and-frames.html">Quantales and Frames</a>
<!-- quantales and frames; the pointfree topology; the relation to the Boolean algebras of this system and to the topological spaces of Part II. -->

## Natural Numbers

## - Algebra

+### <a href="articles_maths/peano-arithmetic-and-model-theory.html">Peano Arithmetic and Model Theory</a>
<!-- Peano arithmetic as a first-order theory; non-standard models; the incompleteness theorems; the relation to the model theory of Part I. -->

+### <a href="articles_maths/computability-theory.html">Computability Theory</a>
<!-- computable functions and Turing machines; decidability and undecidability; the halting problem and the recursion theorems; the relation to the formal logic of Part I. -->

## Real Numbers

## - Geometry

+### <a href="articles_maths/o-minimality.html">O-Minimality</a>
<!-- o-minimal structures and their properties; definable sets and cells; the relation to real algebraic geometry and to the model theory of Part I. -->

## Complex Numbers

## - Analysis

+### <a href="articles_maths/several-complex-variables.html">Several Complex Variables</a>
<!-- holomorphic functions of several variables; domains of holomorphy; the Hartogs phenomenon; pseudoconvexity; the relation to the complex analysis of this system and to the complex manifolds of Part II. -->

## Quaternions

## - Geometry

+### <a href="articles_maths/quaternion-geometry.html">Quaternion Geometry</a>
<!-- quaternion geometry and its properties; the relation to the quaternion algebra and to the quaternion rotations and reflections of this system; the relation to the quaternionic geometry of Part II. -->

## Octonions  *(new system)*

## - Algebra

+### <a href="articles_maths/octonion-algebra.html">Octonion Algebra</a>
<!-- the octonions on $\mathbb{R}^8$; the multiplication and its non-associativity; the norm form; the conjugation; the relation to the normed division algebras and to the Hurwitz theorem of Part I; the relation to the Clifford algebras of Part II. -->

+### <a href="articles_maths/octonion-norm-and-invertibility.html">Octonion Norm and Invertibility</a>
<!-- the norm form on the octonions; the invertibility criterion; the group of units and the fact that the octonions have no zero divisors, in contrast to the biquaternions and the split-quaternions; the relation to the octonion algebra and to the division algebras of Part I. -->

## - Representations

+### <a href="articles_maths/octonion-representations.html">Octonion Representations</a>
<!-- representations of the octonions and their classification; the bimodules over a non-associative algebra and the obstruction to an associative module theory; the relation to the octonion algebra and to the representation theory of algebras. -->

+### <a href="articles_maths/octonions-and-the-exceptional-lie-groups.html">Octonions and the Exceptional Lie Groups</a>
<!-- the construction of the exceptional Lie groups from the octonions, by the magic square and through the exceptional Jordan algebras; $G_2$ as the automorphism group of the octonions; the relation to the Lie algebras of Part I and to the exceptional Jordan algebras of Part I. -->

## - Geometry

+### <a href="articles_maths/octonion-geometry.html">Octonion Geometry</a>
<!-- octonion geometry and its properties; the octonionic projective plane; the relation to the octonion algebra and to the exceptional geometry; the relation to the geometry of Part II. -->

+### <a href="articles_maths/octonions-and-exceptional-geometry.html">Octonions and Exceptional Geometry</a>
<!-- the use of the octonions in exceptional geometry; the holonomy groups $G_2$ and $\operatorname{Spin}(7)$ and the manifolds that carry them; the relation to the octonion algebra and to the $G_2$ and $\operatorname{Spin}(7)$ manifolds of Part II. -->

## - Analysis

+### <a href="articles_maths/octonion-analysis.html">Octonion Analysis</a>
<!-- octonion analysis and its properties; the non-associativity and what it costs; the relation to the hypercomplex analysis and to the octonion algebra; the relation to the Clifford analysis of Part III. -->

## - Integration

+### <a href="articles_maths/octonion-integration.html">Octonion Integration</a>
<!-- integration of octonion-valued functions; the relation to the hypercomplex integration and to the octonion analysis of this system. -->

## - Special Functions

+### <a href="articles_maths/octonion-special-functions.html">Octonion Special Functions</a>
<!-- special functions of an octonion variable; the relation to the octonion analysis of this system and to the special functions of Part IV. -->

## - Harmonic Analysis

+### <a href="articles_maths/octonion-harmonic-analysis.html">Octonion Harmonic Analysis</a>
<!-- harmonic analysis on the octonions; the relation to the octonion analysis of this system and to the harmonic analysis of Part III. -->

## Split-Quaternions

## - Geometry

+### <a href="articles_maths/split-quaternion-geometry.html">Split-Quaternion Geometry</a>
<!-- split-quaternion geometry and its properties; the relation to the split-quaternion algebra and to the split-quaternion rotations and the Lorentz group of this system; the relation to the Lorentzian geometry of Part II. -->

+### <a href="articles_maths/split-quaternions-and-hyperbolic-geometry.html">Split-Quaternions and Hyperbolic Geometry</a>
<!-- the model of hyperbolic three-space on the split-quaternions of unit norm; the relation to the split-quaternion rotations and the Lorentz group of this system and to the hyperbolic geometry of Part II. -->

---

# Dispositions

Counts are given in the validation section. The entries below are **not** in the list above.

## Not carried over: the same title proposed in two or three places

One article, one title. The duplicates were collapsed to the single placement shown in the list above.

| Title as proposed | Where the external list put it | Where it is now |
|---|---|---|
| Quantum Groups | Parts I, II and III | Part I only (Part II has *Locally Compact Quantum Groups*) |
| Induced Representations | Parts I, II and III | Part I (Part II has the locally compact version) |
| Homogeneous Spaces, Symmetric Spaces, Flag Manifolds, Grassmannians | Topology on Groups **and** Geometry and Manifolds | Geometry and Manifolds only |
| Clifford Analysis, Dirac Operators | Quadratic Forms **and** Analysis on Linear Algebras | Part III (Dirac; Clifford Analysis), Spin Geometry keeps the geometric side in Part II |
| Crossed Products | Parts I and II | Part I (Part II has *Crossed Products of C*-Algebras*) |
| Automorphic Forms | Analysis on Groups **and** Analysis on Rings | Analysis on Groups only |
| Global Fields, Algebraic Number Theory, Elliptic Curves | Parts I and II/III | Part I only; the analytic aspects stay in Part III |
| Spectral Sequences | Parts I and II | Part I; Part II has *The Leray–Serre Spectral Sequence* |
| Amenable Groups, Property (T), Lattices, Arithmetic Groups, Representation Theory of LCP Groups | Parts II and III | Part II only |
| Berkovich Spaces, Deformation Quantization, Moduli Spaces, Stacks | two places each | one place each as shown |
| Pontryagin Duality, Mackey Theory, Induced Representations of Groups | Parts II and III | Part II only |
| Applications of Topology to Data Analysis / Topological Data Analysis | two places | neither (see below) |
| Sobolev Spaces, Evolution Equations, Operator Semigroups, Spectral Theory | Part III, duplicating the Differential Equations category | already covered by the six planned entries of *Differential Equations* |
| Bifurcation Theory | Analysis on Linear Spaces **and** Dynamical Systems | Dynamical Systems only |

## Not carried over: title already an article in the corpus

| Proposed title | Existing article |
|---|---|
| Group Algebras | *Group Algebras* (exact title match) |
| Noncommutative Geometry / Spectral Triples | *Spectral Triples and Noncommutative Geometry* |
| Clifford Modules | *Spin Representations and Clifford Modules*; *Clifford Modules and the Twisted Cauchy–Riemann Operator* |
| Index Theory | *The Atiyah–Singer Index Theorem and K-Theory* |
| Fueter Theory | *Fueter Theory for Biquaternions* (the Part III article is the general one) |
| Lattices | *Lattices and the Quaternion Lattice* |
| Tensor Algebra | *Tensor Powers and the Free Algebra*; *Quotients of the Tensor Algebra* |
| Determinants and Traces | *The Determinant and Alternating Forms* |
| Abelian Groups | *Finitely Generated Abelian Groups* (the new article is *Infinite Abelian Groups*) |
| Uniform Spaces | *Metric, Uniform and Complete Spaces* |
| Compact Groups | *Locally Compact Groups and Haar Measure*; *Analysis on Compact Groups* |
| Infinite-Dimensional Lie Groups | *Hilbert's Fifth Problem and Infinite-Dimensional Lie Theory* |
| Function Spaces | overlaps *Sobolev Spaces*, *Besov Spaces*, *Triebel–Lizorkin Spaces* |
| Recursion Theory | synonym of *Computability Theory* |
| Twistor Theory | *Twistor Theory and Biquaternions* (physics corpus) |
| Gauge Theory | *Lattice Gauge Theory and the Biquaternion Path Integral* (physics corpus) |
| Projective Geometry | kept, but see *Biquaternion Null Quadric and Projective Geometry*, which remains the biquaternion article |
| Quaternionic Analysis, Biquaternionic Analysis, Split-Quaternionic Analysis | the per-system analyses of Part IV already cover these |
| Continuous / Borel Functional Calculus | covered by the topological algebras article; only the holomorphic calculus is new |

## Not carried over: physics-named

The corpus is purely mathematical. These were dropped as physics-named; their mathematical content is covered by the articles listed in the list above.

Yang–Mills Theory, Instantons, Monopoles, Seiberg–Witten Theory, Donaldson Theory, Gauge Theory, Twistor Theory. The mathematics they name (fibre bundles and connections, characteristic classes, index theory, four-manifolds, Floer homology, symplectic topology, complex and quaternionic geometry) is kept. If any of these is wanted after all, it belongs in `physics.md`.

## Not carried over: applied mathematics

The corpus is pure mathematics and admits no article about an application. This is now stated in the introduction itself, in the section *Pure Mathematics*, as the companion of the exclusion of physics. Six entries were removed under the rule after the first draft.

| Removed | Was placed in | Why |
|---|---|---|
| Quaternions in Computer Graphics | Part IV, Quaternions | computer graphics is an applied subject; the mathematics it uses is *Quaternion Rotations and Reflections* |
| Quaternions in Robotics | Part IV, Quaternions | robotics is an applied subject |
| Quaternions in Signal Processing | Part IV, Quaternions | signal processing is an applied subject; the mathematics is *Quaternion Harmonic Analysis* |
| Biquaternions in Robotics | Part IV, Biquaternions | robotics is an applied subject |
| Biquaternions in Computer Vision | Part IV, Biquaternions | computer vision is an applied subject |
| Cryptography and Number Theory | Part I, Rings and Fields | cryptography is an applied subject; the arithmetic it uses is covered by *Elliptic Curves* and *Vector Spaces over Finite Fields* |

The *Applications* slots that had been created in Part IV for these entries were removed with them. Part IV has no *Applications* slot for the four quaternion systems, and the corpus has no applied article of any kind.

One entry was kept, renamed to its mathematical content: *Error-Correcting Codes* became **Linear Codes over Finite Fields**, which is algebra over a finite field.

The 43 *Applications of …* titles of the external list remain excluded for the same reason: finance, economics and biology; numerical analysis, the finite element, finite difference, spectral element and boundary element methods, symplectic integrators, control theory, optimal control, signal processing, image processing, tomography, computer graphics, robotics, computer vision, automatic differentiation, kinematics and circuit design; topological data analysis. Five of that group were kept under mathematical names, because their content is mathematics and only the title was applied: *The Probabilistic Method*, *Probabilistic Number Theory*, *Random Walks on Groups*, *The Geodesic Flow* and *Dynamics and Number Theory*.

## Not carried over: scope notes that only restated the title

Several proposed comments read "*X and its properties*" – Fréchet spaces, optimization, game theory, metric geometry, Polish spaces, instantons. Every entry in the list above has a scope note that fixes the object, the constructions and the boundaries of the article instead.

## Merged

Forty-five proposed entries were folded into other articles rather than kept separate, because the theme was one theme and not two. In every case the surviving article took the content of the one removed, and its scope note now states it.

| Removed | Kept in |
|---|---|
| Frobenius Reciprocity | Induced Representations |
| Schur Multipliers | Projective Representations |
| Brauer Characters | Modular Representation Theory |
| Elimination Theory | Gröbner Bases and Elimination Theory |
| Hall–Littlewood Polynomials | Macdonald and Hall–Littlewood Polynomials |
| Schur Functions | Symmetric Functions and Schur Functions |
| Henselian Rings | Valuation Theory and Henselian Rings |
| Algebraic Operads | Operads |
| L-Infinity Algebras | A-Infinity and L-Infinity Algebras |
| Deformation Theory of Lie Algebras | Lie Algebra Cohomology |
| Gerstenhaber Algebras | Poisson and Gerstenhaber Algebras |
| Lie Superalgebras | Graded Lie Algebras and Lie Superalgebras |
| Brauer Groups | Central Simple Algebras and the Brauer Group |
| Grothendieck Categories | Abelian and Grothendieck Categories |
| Representation Type | Quiver Representations and Representation Type |
| Descriptive Topology | Descriptive Set Theory |
| Convergence Spaces | Nets, Filters and Convergence |
| Weak Topologies, Strong Topologies, The Mackey–Arens Theorem, The Bipolar Theorem | Duality Theory |
| LF Spaces, Montel Spaces | Locally Convex Spaces |
| Cuntz Algebras | Graph C*-Algebras |
| Locally Convex Algebras | Locally Convex and Fréchet Algebras |
| Almost Complex Structures | Hermitian Geometry and Almost Complex Structures |
| Lie Sphere Geometry | Möbius and Lie Sphere Geometry |
| Lorentzian Geometry | Pseudo-Riemannian and Lorentzian Geometry |
| Stiefel Manifolds | Grassmannians and Stiefel Manifolds |
| Projective Spaces | Projective Geometry |
| Contact Topology | Symplectic and Contact Topology |
| Surgery Theory | Cobordism and Surgery Theory |
| Three-Manifolds, Four-Manifolds | Low-Dimensional Topology |
| Covering Spaces and the Fundamental Group | The Fundamental Group and Covering Spaces |
| Variational Analysis | Nonsmooth and Variational Analysis |
| Degree Theory for Nonlinear Operators | Fixed Point Theory and Degree Theory |
| Triebel–Lizorkin Spaces | Besov and Triebel–Lizorkin Spaces |
| Inverse Scattering | Soliton Theory |
| Lagrangian Systems | Lagrangian and Hamiltonian Systems |
| Functional Differential Equations | Delay and Functional Differential Equations |
| Ergodic Theory of Hyperbolic Systems | Hyperbolic Dynamics and Anosov Systems |
| Tate's Thesis | Adelic Analysis |
| Dirichlet L-Functions | L-Functions |
| Monogenic Functions | Clifford Analysis |

The merges were chosen where the theme was one theme: a theorem named after its author that is a property of a structure already proposed (*Frobenius reciprocity*, *Hensel's lemma*), a special case of a general construction (*Cuntz algebras* as graph C*-algebras, *LF* and *Montel* spaces as locally convex spaces), a companion object introduced by the same construction (*Stiefel* manifolds with the Grassmannians), or a class of examples whose separate article would have been a list (*the exceptional* topics). Articles whose themes are genuinely distinct were kept apart, and no two entries now share a theme.

## Moved relative to the external list (Law 1)

| Article | From | To | Reason |
|---|---|---|---|
| Clifford Analysis, Dirac Operators | Part II | Part III | a derivative needs a limit; *A derivative … belongs to Part III* |
| Ricci Flow, Mean Curvature Flow, Minimal Surfaces, Harmonic Maps | Part II geometry | Part III Differential Equations | they are evolution equations |
| Vertex Algebras | Symmetric linear algebras | Anti-symmetric linear algebras | they follow from the Lie algebras, which are later in the same part |
| Rational Cherednik Algebras | Part I | Part II Quadratic Forms and Clifford Algebras | they need a symplectic form |
| Model Categories, Higher Algebra, Higher Algebraic K-Theory, Stacks | Parts I/II | Part II after algebraic topology | they need homotopy theory |
| The Schwartz Kernel Theorem | Part II | Part III | it is stated for distributions |
| Real Algebraic Geometry | Part I | Part I, with *O-Minimality* moved to Part IV | the model-theoretic half belongs to the synthetic system of the reals |
| Sheaves in Algebraic Geometry, Schemes, Moduli Spaces | Part II Foundations | Part II Algebraic Geometry | they need the geometry they describe |
| Algebraic Topology, Sheaf Theory and Algebraic Geometry | – | three new categories of Part II | the corpus had no algebraic topology, no sheaf theory and no algebraic geometry at all |
| Probability and Ergodic Theory, Dynamical Systems | – | two new categories of Part III | the corpus had no probability and no ergodic theory at all |

## Follow-up: the introduction

The pure-mathematics rule is now stated in the introduction, in a new section *Pure Mathematics* placed before the section on physics, with the two exclusions presented as one rule and two cases. The following introduction lines still change when this list merges.

1. The spine table gains the three Part II categories, the two Part III categories and the Octonions system of Part IV.
2. Any statement that the extensions of Part II stop at geometry must be revised.
3. The object ladder gains the octonion rung, so that it reads $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{B}, \mathbb{O}$.
4. The summary of the corpus must be revised (the counts in the introduction).

## Late additions: the quaternion and octonion batch

Eighteen entries were added on request, plus one dependency in Part I. Five of them, the applied ones, were then removed under the pure-mathematics rule, leaving thirteen. Ten of the titles as given could not be used; the retitles that survive are below.

### Retitled

| Title as given | Title used | Why |
|---|---|---|
| Quaternionic Geometry (slug `quaternionic-geometry-quaternions`) | Quaternion Geometry | *Quaternionic Geometry* is already the Part II article; this is the Part IV counterpart and follows the `quaternion-*` naming of its own system. |
| Split-Quaternionic Geometry | Split-Quaternion Geometry | same reason; matches *Split-Quaternion Algebra*, *Split-Quaternion Analysis*. |
| Applications of Split-Quaternions to Hyperbolic Geometry | Split-Quaternions and Hyperbolic Geometry | mathematics, not an application: the model of hyperbolic three-space on the split-quaternions of unit norm. |
| Applications of Octonions to Exceptional Lie Groups | Octonions and the Exceptional Lie Groups | mathematics, not an application: the construction of the exceptional groups from the octonions. |
| Applications of Octonions to Exceptional Geometry | Octonions and Exceptional Geometry | mathematics, not an application: the holonomy groups $G_2$ and $\operatorname{Spin}(7)$. |

The five applied titles, *Applications of Quaternions to Computer Graphics*, *to Robotics* and *to Signal Processing*, and *Applications of Biquaternions to Robotics* and *to Computer Vision*, are not retitled but removed; see *Not carried over: applied mathematics*.

### Placement

**Octonions sits after Biquaternions.** The order of the systems of Part IV is $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{B}, \mathbb{O}, \mathbb{H}'$: the octonions follow the biquaternions as the next system after them, and the split-quaternions follow the octonions as before. The Octonions category carries the standard slots, Algebra, Representations, Geometry, Analysis, Integration, Special Functions and Harmonic Analysis, and no *Applications* slot.

### Decisions required

**Octonions are non-associative, and this is the first such system in the corpus.** Every algebra in Parts I to III is associative, and the interior of the corpus leans on that without saying so: the tensor and exterior algebras, the quotient constructions, the module theory, the Wedderburn and Morita theorems. The octonions are not a ring in the associative sense, so:

- the definition of an algebra in Part I must be read as admitting non-associative algebras, or the octonions must be introduced as a named exception;
- *Octonion Representations* cannot mean representations in the module sense; the scope note says so, and pins the article to bimodules and to the obstruction;
- the octonions are nevertheless a division algebra with no zero divisors, in contrast to the biquaternions and the split-quaternions, which the corpus treats in detail.

The other dependencies already exist: *Division Algebras* and *Special and Exceptional Jordan Algebras* are in Part I. *Normed Division Algebras and the Hurwitz Theorem* was added to Part I, because it is the theorem that admits the octonions to the corpus at all and it is the article the octonion entries cite. It sits in the *Applications* slot of Linear Algebras; if the octonions are kept, it may deserve the *Theory* slot instead, since it is now a structural article rather than an example.

### Checked

Thirteen entries plus one dependency survive from this batch. All 289 slugs and all 289 titles of the file are unique, and none collides with the 507 articles on disk or the 543 menu entries. The Octonions category follows the slot order of the other systems and carries no *Applications* slot; the six applied entries and the four Part IV *Applications* slots created for them are gone.
