# __Introduction and Mathematical Conventions__

## Introduction

This article is the entry point to the mathematical corpus. It states what the corpus contains, how it is organised into parts and categories, the ordering principle that decides where an article belongs, and the notational conventions the other articles assume. It introduces no mathematics of its own beyond the examples needed to make the organisation intelligible.

The corpus is a single edifice rather than a collection of subjects. One family of objects is built once — sets, groups, rings and fields, linear spaces, algebras — and is then re-examined as further structure is laid on it: first a distance, then the limits and derivatives that a distance makes possible. Each examination is a *Part*. The result is a progression and not an encyclopaedia: an article presupposes the categories that precede its own and none of those that follow it.

Three consequences explain most of the decisions recorded below, and they are worth stating at once.

- **An article never uses a structure that the corpus has not yet introduced.** The reader is never asked to know a distance while reading the algebra.
- **When a new structure is introduced, every earlier object re-read through it belongs to the new category.** The article on topological groups is a topology article, not a group-theory article.
- **An article depends on nothing.** Within a category the articles are mutually dependent, and a use of something the category introduces further on is stated in line and marked; across a category boundary the dependency is excluded.

These rules are stated precisely in *The Three Rules of the Ordering* below.

## The Five Parts

### Part I : Algebra

Algebra builds the objects themselves, and nothing else. It begins with sets, functions and relations, with the logic of proof, with cardinality and the axiom of choice, and with universal properties; it then adds structure in successive layers — a group law, a second operation making a ring and then a field, an action of scalars making a linear space, and finally a multiplication turning that space into a linear algebra. Symmetric linear algebras, anti-symmetric linear algebras and the linear spaces over a linear algebra complete the part.

Nothing in Part I refers to a distance, a norm, a limit, a form or a manifold. This is the meaning of the statement that **algebra is clean**: the part is developed without topology, and every concept that would require it is deferred to Part II.

### Part II : Topology and Geometry

Topology is what becomes available once a **distance** is placed on the objects of Part I. From a distance come balls, open sets, neighbourhoods, continuity, convergence, completeness and compactness. The part begins with distance and its general theory, and then lays a distance — or the weaker and more general notion of a topology — on each object of Part I in turn: on groups, rings and fields, linear spaces and algebras. A **form** is the second structure of the part, since a bilinear or quadratic form defines a distance-like pairing and generates the classical groups, the Clifford algebras and the spinors. Part II closes with the geometry and the manifolds that these structures produce, with the algebraic topology that measures what a distance leaves invariant, and with the sheaves and the algebraic geometry that the cohomological machinery of the part makes possible.

### Part III : Analysis

Analysis is what becomes available once limits exist. It begins with measure and integration and with the modes of convergence; it then develops analytic functions, differential calculus, the transform theory and the differential equations that the preceding parts make possible, on the objects the preceding parts supply. It closes with the two measure-theoretic subjects that only a limit can define, probability and ergodic theory, and with the dynamical systems those support. The general analysis that underlies the per-system articles is deliberately thin: each transform, each integral and each special function is developed in the category of the system to which it belongs, in Part V.

### Part IV : Catalogues

Parts I to III are organised by structure, and Part V by system. Part IV is organised by **object**. Its three categories are the three layers of the corpus — *Catalogue of Algebra*, *Catalogue of Topology and Geometry* and *Catalogue of Analysis* — and each of their articles is a transversal list of the objects of one kind that the corpus meets. The second is the wider of the three: a geometry is a structure placed on a topological space, so the spaces, the forms and the groups that act on them are listed together. A catalogue of fields collects every field, a catalogue of forms every form with its signature, a catalogue of spaces every space. The part answers the question that a progression by layers cannot: which objects have been met, and how do they compare.

The catalogues are the one part that adds no structure and proves no theorem. Their articles obey a rule of their own:

> A catalogue names an object and points to the article or articles that introduce it. It introduces
> nothing and it proves nothing.

The one condition on what a catalogue may list is that its object has been **introduced somewhere in Parts I to III**. It need not have an article of its own: an object introduced in a single line of an article, or in one of its examples, is a legitimate entry, and the catalogue points to that article rather than to an owner. What a catalogue may not do is name an object that appears nowhere in Parts I to III, or bring in a concept of its own — if a list needs one, the corpus writes the article that introduces it first.

A catalogue lists examples and non-examples side by side. Beside the objects that have the property it gathers it records the objects that fail it, each failure named and pointed to the article that records it — $\mathbb{Z}[\sqrt{-5}]$ is a domain but not a unique factorisation domain, $\mathbb{Z}[x]$ is a unique factorisation domain but not a principal ideal domain, $M_2(\mathbb{R})$ is a ring but not a division ring — and the non-examples are what show that each class is a proper subclass of the one above it. They are recorded with the same care as the examples.

A catalogue also records a warning where an object is expected and does not appear — $\mathbb{H}$ is a division ring but not a field, $\mathbb{O}$ is a division algebra but not a ring, the orthogonal group is not a group-layer object because it is defined by a form — each with the article in which the object is introduced. Every list is assembled from the introductions and the *Summary of Notation* sections of the articles of Parts I to III, which is what keeps it true as the corpus grows.

### Part V : Synthetic Studies

Parts I to III develop the general theory layer by layer. Part V reverses the direction and studies one system at a time, taking each system through the whole ladder. Its categories are the number systems and their relatives — the Booleans, the naturals, the integers, the rationals, the reals, the complex numbers, the split-complex numbers, the dual numbers, the quaternions, the split-quaternions, the biquaternions, the split-biquaternions and the octonions — and its articles take that system through the layers of Parts I to III. Part V is described in *The Synthetic Progression* below.

The sizes of the parts are deliberately not recorded here. Articles are written continuously, so a census that is accurate today is stale tomorrow; the menu is the only authority on what exists and on what is still planned. What is stable is the structure, and the structure is what the rest of this article describes.

## The Homogeneity of the Parts

Each of Parts I, II and III is organised by the **same five-slot spine**. The slots are the layers of the object ladder, and they appear in the same order in every part:

> Foundations → Groups → Rings and Fields → Linear Spaces → Linear Algebras

The spine is what makes the parts comparable. Part II is not a collection of topology articles; it is the spine of Part I, category for category, with a distance added. The same holds for Part III with limits. The correspondence is exact, and it is the structural claim of the whole corpus:

| Slot | Part I : Algebra | Part II : Topology and Geometry | Part III : Analysis |
|---|---|---|---|
| Foundations | Foundations of Algebra | Foundations of Topology | Foundations of Analysis |
| Groups | Groups | Topology on Groups | Analysis on Groups |
| Rings and Fields | Rings and Fields | Topology on Rings and Fields | Analysis on Rings and Fields |
| Linear Spaces | Linear Spaces | Topology on Linear Spaces | Analysis on Linear Spaces |
| Linear Algebras | Linear Algebras | Topology on Linear Algebras | Analysis on Linear Algebras |
| Extensions | Symmetric Linear Algebras; Anti-symmetric Linear Algebras; Linear Spaces over Linear Algebras | Quadratic Forms and Clifford Algebras; Geometry and Manifolds; Algebraic Topology; Sheaves and Cohomology; Algebraic Geometry | Differential Equations; Probability and Ergodic Theory; Dynamical Systems |

Three features of the table deserve comment.

**The Foundations slot is first in every part.** A part begins by assembling the language it needs. In Part I that language is set theory, logic and universal properties. In Part II it is the theory of distance itself: metric, uniform and complete spaces, then general topological spaces, then the metrisation and separation axioms that measure the gap between the two. In Part III it is measure and the modes of convergence. Foundations is a slot and not a preface: it has articles, and later slots refer back to them.

**The naming is mechanical in both directions.** A category of Part II is named *Topology on X* and a category of Part III *Analysis on X*, where X is the name of the slot in Part I; Part I's own categories carry the bare slot names, because Part I is the base against which the other two are named. The three parts therefore read in parallel, slot for slot and name for name, and a slot name carries a qualifier exactly where the object requires one. The fourth slot is named *Linear Spaces*, and keeps that name even where the scalars form a ring and the objects are modules, because the slot is the theory of scalars acting on an abelian group. The fifth slot is named *Linear Algebras* rather than *Algebras* because the multiplication is added to a linear space and not to a set: the name records the layer below it. The objects themselves continue to be called linear spaces and algebras in the articles; the qualified names are the names of the layers.

**Each part adds extensions after the spine.** Part I extends its spine with the *Symmetric Linear Algebras*, the *Anti-symmetric Linear Algebras* and the *Linear Spaces over Linear Algebras* — structures internal to algebra. Part II extends with *Quadratic Forms and Clifford Algebras* and with *Geometry and Manifolds*, which a distance makes possible, and then with *Algebraic Topology*, *Sheaves and Cohomology* and *Algebraic Geometry*, which are built on the cohomological machinery those structures supply: algebraic topology measures what a distance leaves invariant, sheaf cohomology is the derived functor theory of Part I read on a space, and algebraic geometry is the geometry of schemes, coherent sheaves and moduli that the sheaf theory supports. Part III extends with *Differential Equations* and then with *Probability and Ergodic Theory* and *Dynamical Systems*, the measure-theoretic subjects that only a limit can define. An extension is where a part's own new structure generates objects that have no analogue in the other parts.

## The Object Ladder

The spine exists because the objects themselves form a ladder, and each layer adds exactly one thing.

| Layer | Objects | Structure added | What the layer introduces |
|---|---|---|---|
| Sets | sets, functions, relations, cardinals | membership | the language in which everything else is written |
| Groups | groups, actions, presentations | one associative operation with inverses | symmetry, and the first algebraic invariant |
| Rings and Fields | rings, domains, fields | a second operation, distributive over the first | arithmetic, factorisation, division |
| Linear Spaces | modules, vector spaces, linear maps | scalars acting on an abelian group | linear algebra: bases, dimension, matrices |
| Linear Algebras | algebras, ideals, quotients | a multiplication of the space with itself | multiplication and linear structure at once |

Each layer presupposes the one above it and adds a single axiom system. Nothing is anticipated: a group is not assumed to be abelian, a ring is not assumed commutative or to be a domain, a module is not assumed free, an algebra is not assumed associative or to have a unit, and none of them is assumed to carry a distance. The qualifiers are earned by the articles that introduce them.

The ladder is also the reason the parts can be homogeneous. Because each layer adds one structure, the question "what happens to this if we add a distance?" can be asked layer by layer and answered in the same order — which is exactly how Parts II and III are organised.

## The Three Rules of the Ordering

### Rule 1 — No layer may use a structure it has not yet introduced

An article may use the language of its own layer and of the layers below it, and nothing else. This is a constraint on the *writing*, not merely on the placement: an article of Part I may not name a distance, a norm, a completion taken as a limit, a form, a manifold, an orthogonal or special orthogonal group, or a rotation. Where such a concept is genuinely needed, the article states the result in the language it has and **defers the enriched statement** to the category that owns the structure, with an explicit forward reference of the form *"this is treated in Part II, where the form and the distance are available"*.

The rule is applied to the articles' descriptions in the menu as well as to the articles. A description that mentions a structure belonging to a later part is corrected, not tolerated. The consequence is that a reader can read Part I from beginning to end without ever meeting an undefined distance.

Two clarifications, because the rule is easy to over-apply.

- The rule forbids *using* a structure, not *naming* it. An article may say that a concept will later be enriched, and may point forward. What it may not do is reason with the structure.
- The rule concerns structure, not vocabulary. The words *open*, *complete*, *limit*, *continuous* and *normal* have purely algebraic meanings in several places — an open condition in a presentation, an order-complete field, an inverse limit of rings, a normal subgroup — and these are legitimate. What is excluded is the topological *meaning* of the word.

**The reading unit is the category.** The rule above governs *structure*. A second constraint, finer, governs the order of the articles themselves:

> No article may depend on anything.

A **category** —*Rings and Fields*, *Quadratic Forms and Clifford Algebras* — is the **reading unit** of the corpus. Inside a single reading unit the articles are a cluster of mutually dependent concepts, and a dependency there may run in either direction. Where an article needs something that its own category introduces further on, it states what it needs in the terms it already has and marks the article that owns it; the full treatment is met when the category reaches it. What is not permitted is a dependency that crosses a category boundary **forward**. An algebra article does not lean on a linear-space article, and a topology article does not lean on an analysis article.

Two or more sibling categories that form one cluster may be **declared a single reading unit**, in which case dependencies among them are internal and permitted. The four categories of the linear-algebra layer — *Linear Algebras*, *Symmetric Linear Algebras*, *Anti-symmetric Linear Algebras* and *Linear Spaces over Linear Algebras* — are declared together in this way. They divide one cluster of mutually dependent concepts, and the division between them is a division of subject matter, not of prerequisite.

### Rule 2 — The layers are strictly ordered, and algebra is the most fundamental

The layers are

$$
\text{Algebra} \;\longrightarrow\; \text{Topology} \;\longrightarrow\; \text{Analysis},
$$

and each presupposes the one before it. Algebra needs nothing but sets. Topology needs algebra, because a distance is a function to the reals and the objects it is placed on are the algebraic objects. Analysis needs topology, because a limit is defined by a distance or by a topology. No layer may be anticipated by an earlier one.

The test for placing a concept is therefore:

> Can this be defined using only the structures of its own layer and the layers below it?

Applying the test explains several placements that might otherwise look arbitrary.

- A **distance** can be defined on a bare set, so the theory of distance belongs to *Foundations of Topology* and needs no algebra beyond sets and the reals.
- A **norm** cannot: it needs a linear space, since it is defined by scaling. The theory of normed spaces therefore sits in the linear-spaces slot of Part II, not in its foundations.
- A **derivative** needs a linear structure and a limit, so it belongs to Part III, and in the linear-spaces slot because the linear structure is what it differentiates.
- A **Lie group** fails the test for algebra. A Lie group is a group that is also a smooth manifold; a manifold needs a topology, and a topology needs a distance. A Lie group is therefore not an algebra object, and its articles belong to *Topology on Groups*. Its **Lie algebra**, by contrast, is defined by the bracket alone and is pure algebra: it stays in Part I. The passage between the two — the exponential map, the correspondence, the adjoint representation — is a topology article, because it is the passage that needs the manifold.
- The **orthogonal and special orthogonal groups** fail for the same reason in the group slot: they are defined as the transformations preserving a form, and a form is a structure of Part II. They therefore appear not in the group slot but in the category that introduces the form, together with the isometries and the rotations that form generates.
- A **rotation** is not an algebra word. It requires an orientation and a measure, and both require the distance. Rotations appear in Part II and in the geometry slot of each Part V system.

The ordering also explains why algebra can be presented, as it is here, with no warning that topology will follow: it is a complete subject on its own. The converse is false, which is the sense in which algebra is more fundamental than topology.

### Rule 3 — A revisited object belongs to the layer that revisits it

When a category introduces a new structure, it absorbs every earlier object that is re-read through that structure. Those articles live in the **new** category and never in the old one. The earlier article is not duplicated and is not expanded: it keeps exactly what requires no new structure.

| New structure | Introduced in | Re-reads | Articles it absorbs |
|---|---|---|---|
| Distance | Foundations of Topology | sets | metric, uniform and complete spaces; topological spaces |
| Distance on a group | Topology on Groups | groups | topological groups; Lie groups; profinite groups; locally compact groups; matrix and classical groups |
| Distance on a ring and field | Topology on Rings and Fields | rings, fields | topological rings and fields; valuations and completions; the $p$-adic numbers |
| Distance on a linear space | Topology on Linear Spaces | linear spaces | topological vector spaces; normed and Banach spaces |
| Distance on a linear algebra | Topology on Linear Algebras | algebras | topological and Banach algebras; operator algebras; Hilbert modules |
| A form and its distance | Quadratic Forms and Clifford Algebras | groups, linear spaces, Lie algebras | isometries; orthogonal, unitary and symplectic groups; Clifford algebras; spinors; Witt theory |
| A smooth structure | Geometry and Manifolds | forms, groups | manifolds and differential geometry; curvature and geodesics; bundles, connections and curvature; differential forms |
| Measure and limit | the whole of Part III | all of the above | measure; analytic functions; differential calculus; hypercomplex analysis and integration |
| Everything at once | every Part V category | one system at a time | the whole ladder, per system |

The same object therefore appears at several depths, and that is intended. The quaternion group $Q_8$ is a group . The group of unit quaternions is a Lie group (in *Topology on Groups*). Its representations belong to the representation theory of the algebras (in *Linear Spaces over Linear Algebras*), and its harmonic analysis belongs to the quaternion category of Part V. Nothing is repeated: each article adds the structure that its category owns.

An important corollary: **an object is not moved merely because a later structure could be placed on it.** The rule applies only when an article actually uses the new structure. The integers are a ring (in *Rings and Fields*) and also, with the discrete distance, a topological group (in *Topology on Groups*) and a locally compact group — but the article on the integers as a ring stays in *Rings and Fields*, because it reasons with the ring structure alone.

**Part IV is outside the correspondence.** *Catalogues* is not a layer and carries no new structure: its categories cut across the five slots rather than repeating them, and its articles gather the objects of Parts I to III into lists without adding to them. It is placed after the three parts, whose objects it lists, and before *Synthetic Studies*.

## Distance: the Boundary Between Algebra and Topology

The whole ordering turns on one concept. **Distance is the boundary.** Algebra is the theory of objects; topology begins the moment a distance is placed on them. This gives a sharp diagnostic for placing anything:

> If the definition or the proof requires a distance, a norm, a limit, openness, or a neighbourhood, the concept is not algebraic, whatever object it is attached to.

Under this rule three familiar mathematical families change address.

**The classical groups.** $O(V,Q)$, $SO(V,Q)$, $U(V,h)$ and $Sp(V,\omega)$ are not group-theory objects. Each is defined as the set of transformations preserving a form, and a form is the structure from which the geometry, and with it the distance, is read. They belong to the category that introduces forms, and they arrive together with the isometries, the rotations and the reflections those forms generate.

**The Lie groups.** A Lie group is a group that is a manifold. Manifolds, bundles and connections belong to *Geometry and Manifolds*, and the Lie groups to the group slot of Part II, where a topological group has already been introduced. The Lie algebras remain in Part I, and the exponential map and the correspondence that join the two lie with the groups, because it is the manifold side of that correspondence that needs the topology.

**Rotations and reflections.** These are not algebra words. A reflection is defined by a form; a rotation is an orientation-preserving isometry; both need a measure. They appear when the form is available, and then per system in Part V.

### Topology and geometry are the same layer

Since geometry begins with a distance, the corpus does not treat geometry as a fifth part. It treats it as a second intent within the same layer. Part II's foundations study the distance as a **tool**: they extract what all distances have in common — the open sets, the topology — and prove that many different distances give the same answer. The geometry category studies the distance as an **object**: its shape, its curvature, its geodesics, its isometries, and the figures and congruences it defines. The two are complementary readings of one structure, and that is why the geometry articles of Part II sit beside the forms and the Clifford algebras, and why each Part V system carries a geometry slot.

## The Synthetic Progression

Parts I to III are general: each category is about a structure, and the objects of that category are whatever satisfies it. Part IV is transversal: its categories cut across the three, and each of its articles lists the objects of one kind. Part V is concrete: each category is a single system, and the article slots are the layers of Parts I to III applied to that system. The slots recur across the systems:

> Algebra · Topology · Geometry · Representations · Analysis · Integration · Spectral Theory · Special Functions · Harmonic Analysis

A system carries those of them that exist for it, which is a fact about the system rather than a target. The systems themselves form a progression, driven by the addition of one structure at a time.

| System | What it adds |
|---|---|
| Booleans | idempotence; a logic |
| $\mathbb{N}$ | order and induction |
| $\mathbb{Z}$ | additive inverses |
| $\mathbb{Q}$ | division |
| $\mathbb{R}$ | completeness |
| $\mathbb{C}$ | a square root of $-1$ |
| split-complex $\mathbb{D}$ | a hyperbola rather than a circle |
| dual numbers $\mathbb{D}'$ | a nilpotent direction |
| $\mathbb{H}$ | non-commutativity |
| split-quaternions $\mathbb{H}_{\mathrm{s}}$ | a matrix model; isotropic vectors |
| $\mathbb{B}$ (biquaternions) | complexification; zero divisors |
| split-biquaternions $\mathbb{H}_{\mathbb{D}}$ | an indefinite form |
| octonions $\mathbb{O}$ | non-associativity |

The systems are listed in the order in which the corpus reaches them.

Three remarks on the progression.

**The arithmetic systems are deliberately thin.** They carry the algebra and very little above it, because most of the ladder does not exist for them and the corpus says so rather than hiding the gap. The Booleans support an algebra and a topology but no analysis, and the article on Boolean algebras states this explicitly. $\mathbb{N}$ has no additive inverses, so no subtraction, so no difference and no analysis in the usual sense. $\mathbb{Z}$ has no division, so no analytic functions. $\mathbb{Q}$ is incomplete. A missing slot is a mathematical statement, and a system with a gap is as informative as a system without one.

**The four-dimensional systems are the linear progression.** From $\mathbb{C}$ to the split-quaternions every system is a two- or four-dimensional real algebra, and the ladder of the four-dimensional ones is the linear spine of the corpus: $\mathbb{H}$ is the division algebra, the split-quaternions are its indefinite relative, and $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is the complexification — no longer a division algebra, since it has zero divisors, but the system in which the linear structure, the representations and the spectral theory are richest. The biquaternion category is the one in which the ladder is most fully developed.

**The octonions close the progression.** They are the last of the four normed division algebras, and the only system here whose multiplication is not associative. The Cayley–Dickson construction doubles $\mathbb{R}$ to $\mathbb{C}$, $\mathbb{C}$ to $\mathbb{H}$ and $\mathbb{H}$ to $\mathbb{O}$, and then stops: the next doubling has zero divisors. That is why the category is last, and the reason is what the octonions cost. Every system before them is associative, and the module theory of Part I, on which the representations, the operator algebras and the spectral theory rest, assumes associativity. For the octonions that theory is obstructed rather than available, and the octonion articles state the obstruction instead of hiding it. What remains is the algebra and the geometry the octonions generate themselves — $G_2$ as their automorphism group, the exceptional Lie groups and Jordan algebras built from them, the exceptional geometries of holonomy $G_2$ and $\operatorname{Spin}(7)$ — together with the analysis, the integration and the harmonic analysis that the non-associativity shapes rather than prevents. The category is where the ladder of the number systems ends.

## Pure Mathematics

The corpus is pure mathematics. It is an account of mathematical structures and of nothing else, and it admits no article about an application of mathematics. Numerical analysis, the finite element and boundary element methods, control theory, signal and image processing, computer graphics, robotics, computer vision, cryptography as an engineering subject, mathematical finance, mathematical biology and operations research do not belong to it, and no title in it begins *Applications of …*.

The reason is the one that governs the order of the parts. An application is a place where a structure is used, and the use is not a property of the structure. Where the applied subject meets the mathematics it brings constraints of its own — accuracy, cost, numerical stability, real time — and those constraints are not mathematical. The corpus stops at the structure. A reader who wants the applications will find them in the literature of the applied subject, where the mathematics is the instrument and the application is the point.

A concept that is mathematics but is named after its use is admitted on the same terms as one named from physics, and then only for its mathematical content. Convex optimisation is the study of a convex function and a convex set, and is mathematics; the simplex method is an algorithm for computing with them, and is not an article here. The algebra of a finite field and the arithmetic of an elliptic curve are mathematics; the engineering of a channel or of a protocol that uses them is not.

The word *application* occurs in the menu in a second sense, and the two must not be confused. The slot named *Applications* inside a category of Parts I to III means the concrete instances of the structure of that category —under Groups,under Linear Algebras,under the Integers. Those are examples, and examples are mathematics. What the corpus excludes is not the example but the use.

The exclusion of physics, stated in the next section, is the sharpest case of the same rule: a physical theory uses mathematics, and the corpus keeps the mathematics and not the theory. Nothing about the origin of a concept decides whether it is admitted. What decides is whether its mathematical content stands on its own.

## No Physics in the Mathematical Corpus

The mathematical corpus contains no article about a physical theory. There is no time in it, no measurement, no experimental input, no observable, and no interpretation. The physics corpus is a separate body of articles with its own menu, and the two are not mixed.

The rule is not that mathematical concepts with a physical origin are forbidden. It is that the **mathematical content must be autonomous**. Where a concept was named first in physics and is by now an ordinary mathematical object, the name may be kept, provided everything physical about it is dropped.

The clearest case is the **Lorentz group**. The Lorentz group is the group of linear transformations preserving a quadratic form of signature $(3,1)$. That is a complete definition in pure algebra, and the group is treated as such: its structure, its subgroups, its one-parameter subgroups and its relation to the split-biquaternions are ordinary mathematics. What the corpus does not write is *spacetime*, *the speed of light*, *an observer*, *a clock* or *a measurement*.

The same discipline applies to vocabulary that carries a physical flavour more strongly than its mathematical content. Where a mathematical synonym exists it is preferred: a **hyperbolic rotation** rather than a *boost*, the **null cone of a quadratic form** rather than a *light cone*, and **signature** rather than any metrical vocabulary from relativity. A reader coming from physics will recognise these objects; the corpus describes them as the algebra and the geometry that they are.

Where a physical interpretation exists and is worth stating, it belongs to the physics corpus. The mathematical article says so with a forward reference and stops.

## Notational Conventions

The conventions below are those used throughout the corpus. They are stated once, here, so that the other articles need not repeat them.

### Symbols

| Symbol | Meaning |
|---|---|
| $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$ | the naturals, integers, rationals, reals, complex numbers |
| $\mathbb{H}$ | the real quaternions |
| $\mathbb{D}$ | the split-complex numbers, $\mathbb{R}[x]/(x^2-1)$ |
| $\mathbb{D}'$ | the dual numbers, $\mathbb{R}[x]/(x^2)$ |
| $\mathbb{B}$ | the biquaternions, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $\mathbb{H}_{\mathbb{D}}$ | the split-biquaternions, $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternions, $\mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ |
| $\mathbb{O}$ | the octonions |
| $G$ | a group; $R$ a ring; $k$, $F$ a field; $V$ a vector space; $M$ a module; $A$ an algebra |
| $\mathfrak{g}, \mathfrak{h}, \mathfrak{sl}_n$ | Lie algebras, in Fraktur |
| $\mathfrak{m}, \mathfrak{p}$ | ideals and prime ideals, in Fraktur |
| $\operatorname{Sym}(X), \operatorname{Aut}(X)$ | symmetric group of a set; automorphism group of a structure |
| $\operatorname{End}(V), \operatorname{Der}(A), \operatorname{Inn}(A), \operatorname{Out}(A)$ | endomorphisms, derivations, inner and outer automorphisms |
| $GL, SL, PGL, O, SO, U, SU, Sp$ | the classical groups |
| $T(V), S(V), \Lambda(V), Cl(V,Q)$ | tensor, symmetric, exterior and Clifford algebras |
| $V^{\otimes n}, S^n V, \Lambda^n V$ | tensor, symmetric and exterior powers |
| $B(v,w), Q(v), N(x)$ | bilinear form, quadratic form, norm form |
| $\bar{\cdot}, {}^{*}, {}^{\dagger}, {}^{\flat}$ | the conjugations of an algebra with involution |

### Groups, rings and operations

A group is written multiplicatively by default, with unit $e$ and inverse $x^{-1}$, and additively when it is the underlying group of a ring, with zero $0$ and inverse $-x$. A ring is a triple $(R, +, \cdot)$; a ring need not be commutative and need not have a unit, and the article that introduces it says which conventions it adopts. A field is a commutative ring with $1 \neq 0$ in which every nonzero element is invertible. A module is written with its scalars on the left unless the article says otherwise, and the side matters as soon as the ring is non-commutative. Products are written by juxtaposition: $ab$ for the product in a group or an algebra, $fv$ for the action of a scalar on a vector.

### Numbers of the corpus

The four conjugations of the biquaternions are $\bar{\cdot}$ (quaternion conjugation), ${}^{*}$ (complex conjugation), ${}^{\dagger} = \bar{\cdot}{}^{*}$ (Hermitian conjugation) and ${}^{\flat} = {}^{*}\bar{\cdot}$. The two subspaces $\mathbb{M}_{-}$ and $\mathbb{M}_{+}$ are the anti-Hermitian and Hermitian parts, and the norm form is $N(x) = \sum_\mu x_\mu^2$, which vanishes on the zero divisors. The same symbol denotes the same object across the whole corpus: $\mathbb{B}$ is always the biquaternion algebra and $\mathbb{H}$ always the real quaternions.

### LaTeX and typesetting

The articles are rendered with KaTeX on the page, and the following rules are observed in the source.

- Inline mathematics is written between single dollars, and display mathematics between double dollars on lines of their own.
- Inline mathematics never spans a line break. If a formula is too long, it is displayed.
- Display mathematics inside a list is indented four spaces.
- A prime is never written immediately after a symbol that also carries a subscript: the form `q'_0^2` is not written. The prime is applied to the symbol first, and the subscript follows it.
- Tables are Markdown tables. A LaTeX array is never used for a table.
- Every heading that introduces a comparison or a classification is a real `###` heading, and the objects are defined before they are tabulated.
- The macros `\dddot` and `\slashed` are available. The characters `|`, `{`, `}`, `<` and `>` inside mathematics need no escaping.
- A malformed formula is rendered in red on the page rather than reported as an error, so mathematics is checked by eye and not by the absence of a warning.

## Conventions of the Corpus Itself

The corpus has a small number of working conventions that are not mathematical.

**The menus.** Every article is registered in exactly one menu: `maths.md` for the mathematical corpus and `physics.md` for the physics corpus. An entry has the form of a link to the article followed by a comment that lists the contents of the article in outline. The mathematical menu opens with this article, outside the five parts, since it describes the corpus rather than belonging to one of its layers. An entry that begins with `+` is a **planned** article, one that is registered in the menu and not yet written; an entry without the marker has its article on disk.

**The category names and numbers.** The menu numbers its categories, and an article elsewhere in the corpus may address one by number rather than by name: *category n* means the n-th category of the mathematical menu, read in order. This article refers to categories by **name** throughout, because the names are the stable thing and the numbers shift whenever a category is inserted or split. A reader who meets a bare number in another article can resolve it in the menu.

**The article files.** The corpus is split into two collections, each with its own folder: a mathematical article is a file `articles_maths/<slug>.md` and a physical article is a file `articles_physics/<slug>.md`, where the slug is the title in lower case with hyphens in place of spaces and punctuation. The folder and the menu agree — an article lies in the folder whose menu lists it, and no article lies in both. Each article has a companion `<slug>.thinking` beside it in the same folder, recording the sources consulted and the authoring decisions taken; the companion is not part of the published corpus and is inert for the build.

**The article skeleton.** Every article opens with its title as the first heading, followed by an *Introduction* that states what the article does and what it assumes, then the thematic sections, and closes with three sections in this order: *Summary*, *Summary of Notation*, and *Further Reading*. The introduction states the article's boundaries — what it deliberately does not cover, and where the reader will find it.

**Cross-references and boundaries.** A concept is introduced once, in the category that owns it, and referred to afterwards rather than restated. Articles do not duplicate the content of other articles; they cite them. Every article that touches a structure belonging to a later part states the deferral explicitly, which is the mechanism by which Rule 1 is enforced.

## Summary

The mathematical corpus is organised in five parts. Part I, Algebra, builds the objects — sets, groups, rings and fields, linear spaces, linear algebras — and uses nothing but those objects. Part II, Topology and Geometry, places a distance on each of them in turn, and then studies the forms, the classical groups, the Clifford algebras and the geometry that the distance makes possible, together with the algebraic topology, the sheaves and the algebraic geometry built on its cohomology. Part III, Analysis, uses the limits that the distance supplies, down to the probability, the ergodic theory and the dynamical systems that only a limit can define. Part IV, Catalogues, gathers the objects of Parts I to III into transversal lists, one kind of object per article, naming each object and pointing to the articles that introduce it without introducing or proving anything. Part V, Synthetic Studies, re-traverses the whole ladder one system at a time, from the Booleans to the octonions.

Parts I to III share one five-slot spine — Foundations, Groups, Rings and Fields, Linear Spaces, Linear Algebras — and each part adds its own extensions after it. The spine follows the object ladder, in which each layer adds exactly one structure to the layer above.

Three rules fix the placement of every article. No category may use a structure it has not yet introduced. The layers are strictly ordered, and algebra, which needs no distance, is the most fundamental. And an object re-read through a new structure belongs to the new category, not the old one: once a distance exists, the topological groups, the classical groups, the Lie groups and the isometries are topology articles, however algebraic their objects.

The catalogues of Part IV obey a rule of their own. A catalogue names an object and points to the articles that introduce it; it introduces nothing and it proves nothing. The one condition on what it may list is that the object has been introduced somewhere in Parts I to III, whether or not an article is devoted to it.

Distance is the boundary between the parts and the diagnostic for placing anything: if a concept needs a distance, a norm, a limit or an open set, it is not algebraic. Under this rule geometry is not a fifth part but the second intent of the same layer — topology studies the distance as a tool, geometry studies it as an object — and the classical groups and the rotations arrive with the forms, not with the groups.

The corpus is pure mathematics. No article is about an application of mathematics — no numerical analysis, computer graphics, robotics or cryptography — and no article is about a physical theory. A concept is kept only where its mathematical content is autonomous, whatever its origin, and it is then stripped of every reference to an application, to physics, to time and to measurement.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| Part I, II, III, IV, V | Algebra, Topology and Geometry, Analysis, Catalogues, Synthetic Studies |
| Foundations, Groups, Rings and Fields, Linear Spaces, Linear Algebras, Extensions | the five-slot spine shared by Parts I to III, and the extensions each part adds after it |
| Rule 1 | no category may use a structure it has not yet introduced |
| Rule 2 | the layers are strictly ordered; algebra is the most fundamental |
| Rule 3 | a revisited object belongs to the layer that revisits it |





## Further Reading

- Nicolas Bourbaki, *Éléments de mathématique* (Hermann, then Springer). The model for treating algebra, topology and analysis as separate and strictly ordered bodies of theory.
- Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed. (Springer, 1998). Universal properties and the language of the Foundations slot of Part I.
- Felix Klein, *Vergleichende Betrachtungen über neuere geometrische Forschungen* (Erlangen, 1872). The programme that defines a geometry by its transformation group, which is the reason geometry sits inside topology here.
- Hermann Weyl, *The Classical Groups: Their Invariants and Representations* (Princeton, 1939). The forms first, the groups they define second.
- John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed. (Springer, 2013). Manifolds, bundles and curvature, for *Geometry and Manifolds*.
- James R. Munkres, *Topology*, 2nd ed. (Prentice Hall, 2000). Metric and topological spaces, and metrisation.
- Serge Lang, *Algebra*, 3rd ed. (Springer, 2002). The reference for the object ladder of Part I.
- Michael Artin, *Algebra*, 2nd ed. (Pearson, 2011). An account in which the examples precede the general theory.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991). The representations that recur in the Part V slots.
- John C. Baez, "The Octonions", *Bulletin of the American Mathematical Society* 39 (2002), 145–205. The chain of real division algebras that ends the ladder of the number systems.
