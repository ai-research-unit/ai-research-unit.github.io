# __Introduction to Mathematics__

## Introduction

This article is the entry point to the mathematical corpus and describes how its articles are organised. It states what the corpus contains, the six parts and the five-slot spine they share, the object ladder, the ordering rules that decide where an article belongs, the boundaries between the parts and the local tests they give, the synthetic progression, the method by which the corpus is learnt, and the two exclusions — applications and physics. It introduces no mathematics of its own beyond the examples that make the organisation intelligible.

The notation the articles assume is gathered separately, in the companion article *Conventions in Mathematics*. The two articles stand together at the head of the menu, outside the parts; what follows concerns the organisation alone.

## The Six Parts

### Part I : Algebra

Algebra builds the objects themselves, and nothing else. It begins with sets, functions and relations, with the logic of proof, with cardinality and the axiom of choice, and with universal properties; it then adds structure in successive layers — a group law, a second operation making a ring and then a field, an action of scalars making a linear space, and finally a multiplication turning that space into a linear algebra. Symmetric algebras, anti-symmetric algebras and the linear spaces over an algebra complete the part.

Nothing in Part I refers to a distance, a length, a limit or a manifold. Part I does carry the **form** — a bilinear, quadratic or sesquilinear pairing with values in the ring or in the algebra — and its **algebraic norm**, the quadratic form $Q(x)=B(x,x)$ or the multiplicative norm $N(x)=x x^{\natural}$, whose value is an **element** and not a length; the algebraic norm of a biquaternion is a biquaternion. What Part I lacks is the **topological norm**, the norm **selected** so that its values are positive reals, and with it the distance, the balls and the limit. This is the meaning of the statement that **algebra is clean**: the part is developed without a length, and every concept that would require one is deferred to Part II. The distinction is stated in full in *Algebra and Topology: the distance* below.

### Part II : Topology

Topology is what becomes available once a **distance** is placed on the objects of Part I. From a distance come balls, open sets, neighbourhoods, continuity, convergence, completeness and compactness. The part begins with distance and its general theory, and then lays a distance — or the weaker and more general notion of a topology — on each object of Part I in turn: on groups, rings and fields, linear spaces and algebras. The structure the part adds is the **topological norm**, the selection of a norm whose values are positive reals, from which the distance is built; on a linear space it is the norm itself, and on an algebra it is the topological reading of a form, whose further subject is *Topology on Algebras with a degree-2 form*. The forms themselves, with their algebraic norms, their Clifford algebras and their spinors, are algebraic and belong to Part I. Part II closes with the algebraic topology that measures what a distance leaves invariant, with the sheaves and the algebraic geometry that the cohomological machinery of the part makes possible, and with the **geometric topology** the distance supports on manifolds: the low-dimensional manifolds and their classification, the knots and their invariants, the cobordism and surgery theory, and the symplectic and contact topology with the Floer homology those carry.

### Part III : Analysis

Analysis is what becomes available once a distance is used **quantitatively**, through the two limits that need more than a topology: the **derivative**, which needs a norm, and the **integral**, which needs a measure. From the derivative come the differential calculus on normed spaces, the smooth manifolds it defines, and the differential topology those support — differential forms and Stokes' theorem, bundles, connections and curvature, characteristic classes; from the calculus come the differential equations, and, once the smooth structure is in place, the Lie groups. From the measure come integration and the modes of convergence, the analytic functions, the transform theory, the distributions and the spectral theory. The part closes with the two measure-theoretic subjects that only a limit can define, probability and ergodic theory, and with the dynamical systems those support. The general analysis that underlies the per-system articles is deliberately thin: each transform, each integral and each special function is developed in the category of the system to which it belongs, in Part VI.

### Part IV : Geometry

Geometry takes the **distance as an object** rather than as a tool. It adds no new rung to the object ladder: the distance is the rung, and Part II already owns it. Geometry is the second reading of that same structure — its shape, its symmetries and its figures — and it is placed after Analysis because its synthesis is built from the derivative and the measure that Analysis supplies. Its **shape** is length, angle, area, curvature, the geodesics and the comparison of distances: Riemannian, Lorentzian and metric geometry, and Gromov–Hausdorff convergence. Its **motions** are the translations, the rotations, the reflections and the isometries, and the group of transformations a space admits — the form-defined classical groups $O$, $U$, $SO$ and $SU$. Its **figures** are the Euclidean, spherical, hyperbolic, affine, projective and conformal geometries, the congruence of figures, and Klein's programme, in which a geometry is its group of motions. Its **settings** are the homogeneous and symmetric spaces, the Grassmannians and the flag manifolds, and the geometries that a distance selects: symplectic, contact, Kähler and Calabi–Yau geometry. Its **algebras** are the geometries an algebra defines: the spin geometry of the Clifford algebras, the quaternionic and hyperkähler geometries of the quaternions, the $G_2$ and $\operatorname{Spin}(7)$ manifolds of the exceptional algebras, and supergeometry. Its **extension** is its synthesis with Analysis: Hodge theory, the index theorem, harmonic maps, the Ricci and mean-curvature flows, the geodesic flow, geometric measure theory and the spectral triples of noncommutative geometry. Its categories are *Foundations of Geometry*, *Geometry on Groups*, *Geometry on Rings and Fields*, *Geometry on Linear Spaces*, *Geometry on Algebras* and *Synthesis of Geometry and Analysis*. Read against the spine, the six line up one to a slot — the distance as an object, the motions, the figures, the settings, and the geometries an algebra defines — with the *Synthesis* standing as geometry's further subject. The form-defined classical groups $O$, $SO$, $U$, $SU$ and $Sp$ sit in *Geometry on Groups*, at the Group slot, because a group read from a form is the motion group of the geometry that form determines.

### Part V : Catalogues

Parts I to IV are organised by structure, and Part VI by system. Part V is organised by **object**. Its four categories are the four structural parts of the corpus — *Catalogue of Algebra*, *Catalogue of Topology*, *Catalogue of Analysis* and *Catalogue of Geometry* — and each of their articles is a transversal list of the objects of one kind that the corpus meets. A geometry is a structure placed on a topological space, so the forms are listed with the objects of the algebra and the groups that act on them with the geometry. A catalogue of fields collects every field, a catalogue of forms every form with its signature, a catalogue of spaces every space. The part answers the question that a progression by parts cannot: which objects have been met, and how do they compare.

The catalogues are the one part that adds no structure and proves no theorem. Their articles obey a rule of their own:

> A catalogue names an object and points to the article or articles that introduce it. It introduces
> nothing and it proves nothing.

The one condition on what a catalogue may list is that its object has been **introduced somewhere in Parts I to IV**. It need not have an article of its own: an object introduced in a single line of an article, or in one of its examples, is a legitimate entry, and the catalogue points to that article rather than to an owner. What a catalogue may not do is name an object that appears nowhere in Parts I to IV, or bring in a concept of its own — if a list needs one, the corpus writes the article that introduces it first.

A catalogue lists examples and non-examples side by side. Beside the objects that have the property it gathers it records the objects that fail it, each failure named and pointed to the article that records it — $\mathbb{Z}[\sqrt{-5}]$ is a domain but not a unique factorisation domain, $\mathbb{Z}[x]$ is a unique factorisation domain but not a principal ideal domain, $M_2(\mathbb{R})$ is a ring but not a division ring — and the non-examples are what show that each class is a proper subclass of the one above it. They are recorded with the same care as the examples.

A catalogue also records a warning where an object is expected and does not appear — $\mathbb{H}$ is a division ring but not a field, $\mathbb{O}$ is a division algebra but not a ring, the orthogonal group is not a group-layer object because it is defined by a form — each with the article in which the object is introduced. Every list is assembled from the introductions and the *Summary of Notation* sections of the articles of Parts I to IV, which is what keeps it true as the corpus grows.

### Part VI : Synthetic Studies

Parts I to IV develop the general theory layer by layer. Part VI reverses the direction and studies one system at a time, taking each system through the whole ladder. Its categories are the number systems and their relatives — the Booleans, the naturals, the integers, the rationals, the reals, the complex numbers, the split-complex numbers, the dual numbers, the quaternions, the split-quaternions, the biquaternions, the split-biquaternions and the octonions — and its articles take that system through Parts I to IV. Part VI is described in *The Synthetic Progression* below.

The sizes of the parts are deliberately not recorded here. Articles are written continuously, so a census that is accurate today is stale tomorrow; the menu is the only authority on what exists and on what is still planned. What is stable is the structure, and the structure is what the rest of this article describes.

## The Homogeneity of the Parts

Each of Parts I, II and III is organised by the **same five-slot spine**. The slots are the layers of the object ladder, and they appear in the same order in every part:

> Foundations → Groups → Rings and Fields → Linear Spaces → Algebras

The ladder does not stop at *Algebras*. Each part appends **further subjects** after its five slots, and it is there, at the open end of the ladder, that a subject needing a structure introduced later finds its place. A part is therefore its spine followed by its further subjects, and the further subjects are ordered by dependency among themselves.

The spine is what makes the parts comparable. Part II is not a collection of topology articles; it is the spine of Part I, category for category, with a distance added. The same holds for Part III with the derivative and the measure. The correspondence is exact, and it is the structural claim of the whole corpus:

| Slot | Part I : Algebra | Part II : Topology | Part III : Analysis | Part IV : Geometry |
|---|---|---|---|---|
| Foundations | Foundations of Algebra | Foundations of Topology | Foundations of Analysis | Foundations of Geometry |
| Groups | Groups | Topology on Groups | Analysis on Groups | Geometry on Groups |
| Rings and Fields | Rings and Fields | Topology on Rings and Fields | Analysis on Rings and Fields | Geometry on Rings and Fields |
| Linear Spaces | Linear Spaces | Topology on Linear Spaces | Analysis on Linear Spaces | Geometry on Linear Spaces |
| Algebras | Algebras | Topology on Algebras | Analysis on Algebras | Geometry on Algebras |
| Further subjects | Symmetric Algebras; Anti-symmetric Algebras; Linear Spaces over Algebras; Sesqualgebras; Algebras with a degree-2 form; Sesqualgebras with a degree-2 form | Topology on Algebras with a degree-2 form; Topology on Sesqualgebras with a degree-2 form; Algebraic Topology; Sheaves and Cohomology; Algebraic Geometry; Geometric Topology | Convexity and Order; Smooth Manifolds and Differential Topology; Differential Equations; Lie Groups; Probability and Ergodic Theory; Dynamical Systems | Synthesis of Geometry and Analysis |

Part IV is not a layer. Geometry adds no structure of its own, so it does not repeat the spine with one more structure added — but the distance can be placed on the object of every rung, so geometry can be **read** at every rung, and its categories follow the same slots in the same order, one category per slot. *Synthesis of Geometry and Analysis* stands as geometry's further subject, the analogue of the further subjects the other parts append after their spine.

The ladder **is** the progression. A subject that needs a structure introduced later is not pulled back into an earlier slot; it is placed at the open end of the ladder, as a further subject of the part that owns the structure it needs. The Lie groups are the case: they need the smooth structure, which Part III introduces, so they are a further subject of Part III, placed after the calculus, and they are stated in Rule 2 below.

Three features of the table deserve comment.

**The Foundations slot is first in every part.** A part begins by assembling the language it needs. In Part I that language is set theory, logic and universal properties. In Part II it is the theory of distance itself: metric, uniform and complete spaces, then general topological spaces, then the metrisation and separation axioms that measure the gap between the two. In Part III it is measure and the modes of convergence. Foundations is a slot and not a preface: it has articles, and later slots refer back to them.

**The naming is mechanical in both directions.** A category of Part II is named *Topology on X* and a category of Part III *Analysis on X*, where X is the name of the slot in Part I; Part I's own categories carry the bare slot names, because Part I is the base against which the other two are named. The three parts therefore read in parallel, slot for slot and name for name, and a slot name carries a qualifier exactly where the object requires one. The fourth slot is named *Linear Spaces*, and keeps that name even where the scalars form a ring and the objects are modules, because the slot is the theory of scalars acting on an abelian group. The fifth slot is named *Algebras* rather than *Algebras* because the multiplication is a bilinear map on the linear space and not an operation on a bare set: the name records the bilinearity of the product. The objects themselves continue to be called linear spaces and algebras in the articles; the qualified names are the names of the layers.

**Each part adds further subjects after the spine.** Part I extends its spine with the *Symmetric Algebras*, the *Anti-symmetric Algebras*, the *Linear Spaces over Algebras* and the two degree-2 form categories, *Algebras with a degree-2 form* and *Sesqualgebras with a degree-2 form* — the form and its algebraic norm, structures internal to algebra, which need no length. Part II extends with *Topology on Algebras with a degree-2 form* and *Topology on Sesqualgebras with a degree-2 form*, the topological norms and the distances built on those forms, then with *Algebraic Topology*, *Sheaves and Cohomology* and *Algebraic Geometry*, which are built on the cohomological machinery that structure supplies: algebraic topology measures what a distance leaves invariant, sheaf cohomology is the derived functor theory of Part I read on a space, and algebraic geometry is the geometry of schemes, coherent sheaves and moduli that the sheaf theory supports. It closes with *Geometric Topology*, the low-dimensional and knot-theoretic subjects a distance supports on manifolds. Part III extends with *Smooth Manifolds and Differential Topology*, the smooth structure the derivative makes possible, then with *Differential Equations* and *Lie Groups*, and finally with *Probability and Ergodic Theory* and *Dynamical Systems*, the measure-theoretic subjects that only a limit can define. Part IV adds the synthesis of geometry and analysis: Hodge theory, the index theorem, the geometric flows and the spectral triples. A further subject is where a part's own new structure generates objects that have no analogue in the other parts, or where an object needs a structure the part introduces further on.

## The Object Ladder

The spine exists because the objects themselves form a ladder, and each layer adds exactly one thing.

| Layer | Objects | Structure added | What the layer introduces |
|---|---|---|---|
| Sets | sets, functions, relations, cardinals | membership | the language in which everything else is written |
| Groups | groups, actions, presentations | one associative operation with inverses | symmetry, and the first algebraic invariant |
| Rings and Fields | rings, domains, fields | a second operation, distributive over the first | arithmetic, factorisation, division |
| Linear Spaces | modules, vector spaces, linear maps | scalars acting on an abelian group | linear algebra: bases, dimension, matrices |
| Algebras | algebras, ideals, quotients | a multiplication of the space with itself | multiplication and linear structure at once |
| *Further subjects* (not a rung) | — | the part's own structure, read further | the subjects a part's structure makes possible, placed at the open end |

Each layer presupposes the one above it and adds a single axiom system. Nothing is anticipated: a group is not assumed to be abelian, a ring is not assumed commutative or to be a domain, a module is not assumed free, an algebra is not assumed associative or to have a unit, and none of them is assumed to carry a distance. The qualifiers are earned by the articles that introduce them.

The ladder is also the reason the parts can be homogeneous. Because each layer adds one structure, the question "what happens to this if we add a distance?" can be asked layer by layer and answered in the same order — which is exactly how Parts II and III are organised.

Above *Algebras* the ladder has no further object rung: a distance and a measure are structures placed on the objects, not objects of a new layer. What a part adds beyond its five slots is therefore not a rung of the object ladder but a **further subject** — a body of mathematics the part's own structure makes possible, placed at the open end and ordered by dependency. The two are kept distinct: the five slots are read in parallel across Parts I, II and III, and the further subjects are read in sequence within each part.

## The Three Rules of the Ordering

### Rule 1 — No part may use a structure it has not yet introduced

An article may use the language of its own part and of the parts below it, and nothing else. This is a constraint on the *writing*, not merely on the placement: an article of Part I may not name a distance, a length, a **topological norm** (a norm selected so that its values are positive reals), a completion taken as a limit, a manifold, an orthogonal or special orthogonal group, or a rotation, while it **may** define and use a **form** and its **algebraic norm**, whose values lie in the ring or the algebra. Where such a concept is genuinely needed, the article states the result in the language it has and **defers the enriched statement** to the category that owns the structure, with an explicit forward reference of the form *"this is treated in Part II, where the form and the distance are available"*.

The rule is applied to the articles' descriptions in the menu as well as to the articles. A description that mentions a structure belonging to a later part is corrected, not tolerated. The consequence is that a reader can read Part I from beginning to end without ever meeting an undefined distance.

Two clarifications, because the rule is easy to over-apply.

- The rule forbids *using* a structure, not *naming* it. An article may say that a concept will later be enriched, and may point forward. What it may not do is reason with the structure.
- The rule concerns structure, not vocabulary. The words *open*, *complete*, *limit*, *continuous* and *normal* have purely algebraic meanings in several places — an open condition in a presentation, an order-complete field, an inverse limit of rings, a normal subgroup — and these are legitimate. What is excluded is the topological *meaning* of the word.

**The reading unit is the category.** The rule above governs *structure*. A second constraint, finer, governs the order of the articles themselves:

> No article may depend on anything.

A **category** —*Rings and Fields*, *Algebras with a degree-2 form* — is the **reading unit** of the corpus. Inside a single reading unit the articles are a cluster of mutually dependent concepts, and a dependency there may run in either direction. Where an article needs something that its own category introduces further on, it states what it needs in the terms it already has and marks the article that owns it; the full treatment is met when the category reaches it. What is not permitted is a dependency that crosses a category boundary **forward**. An algebra article does not lean on a linear-space article, a topology article does not lean on an analysis article, and an analysis article does not lean on a geometry article.

Two or more sibling categories that form one cluster may be **declared a single reading unit**, in which case dependencies among them are internal and permitted. The four categories of the algebra layer — *Algebras*, *Symmetric Algebras*, *Anti-symmetric Algebras* and *Linear Spaces over Algebras* — are declared together in this way. They divide one cluster of mutually dependent concepts, and the division between them is a division of subject matter, not of prerequisite. The device serves sibling categories that divide one cluster; it is not a substitute for the progression. A subject that needs a structure introduced later is placed at the open end of the ladder, not joined to an earlier category.

**An example is a use, and the order of the articles governs it.** No concept is used in an article that a later article introduces. A later concept may be *named*, with the forward reference that marks where it is treated; it may not be *used*, and an illustration is a use. So no article takes as an example an object whose own introduction comes later, not even where the illustration is true and familiar. Two cases fix the intent. $\mathbb{R}$ and $\mathbb{C}$ are introduced in *Rings and Fields*, so no article of *Foundations of Algebra* or of *Groups* may take $\mathbb{R}$ or $\mathbb{C}$ as an example. $\mathbb{H}$ and $\mathbb{B}$ are introduced in *Algebras*, so no article placed before that category — in *Foundations of Algebra*, *Groups*, *Rings and Fields* or *Linear Spaces* — may take a quaternion or a biquaternion as an example. The rule binds the articles and their descriptions in the menu alike.

**Inside a category the articles are grouped.** A category is not a flat list. Its articles fall into groups, and each group adds one thing to the group before it. The group `- Theory` holds the structure itself, read with the product of its elements. The group `- Operator Theory` adds the operators on that structure — the left and right multiplications, the derivations, the automorphisms, the actions, the sandwich — and adds an operator layer and nothing else. The group `- * Theory` reads the same structure with an involution on its **elements**. The group `- * Operator Theory` reads the involution on the **operators** — the operators built from it, of which the adjoint is the archetype. The group `- Applications`, the concrete instances of the structure, closes the category; the marks themselves and their meanings are fixed in *Conventions in Mathematics*.

The split between the last two groups is the one easiest to miss, and it is a rule and not a remark: **the involution on the elements and the adjoint on the operators are two structures, not one**. The star names them both — it is the mark of the involutive layer, on the elements and on the operators alike — but the two layers need not coincide. The dagger stays the notation of the adjoint of a particular operator, and it is not a group name. An involution on the elements does not by itself produce an adjoint on the operators, and two adjoints of the same structure may differ — the transpose and the Hermitian adjoint of a matrix are both adjoints, taken with respect to different forms. When the two do agree the representation is a `*`-representation, and the agreement is proved in the article, never assumed by the menu.

### Rule 2 — The parts are strictly ordered, and algebra is the most fundamental

The progression is

$$
\text{Algebra} \;\longrightarrow\; \text{Topology} \;\longrightarrow\; \text{Analysis} \;\longrightarrow\; \text{Geometry},
$$

and each part presupposes the one before it. Algebra needs nothing but sets. Topology needs algebra, because a distance is a function to the reals and the objects it is placed on are the algebraic objects. Analysis needs topology, because the derivative needs a norm and the integral needs a measure, and both are built on the distance and the topology it induces. Geometry needs analysis, because the shape, the curvature and the geodesics of a distance are read with the derivative, and because its synthesis with analysis uses the measure. No part may be anticipated by an earlier one.

The order is strict, but only the first three parts are **layers** of the object ladder, each adding one structure. Geometry is the fourth part and adds none: the distance is the structure, Part II owns it, and geometry is the second reading of that same structure, placed last because the reading needs the calculus.

The test for placing a concept is therefore:

> Can this be defined using only the structures of its own part and the parts below it?

Applying the test explains several placements that might otherwise look arbitrary.

- A **distance** can be defined on a bare set, so the theory of distance belongs to *Foundations of Topology* and needs no algebra beyond sets and the reals.
- A **topological norm** cannot: it needs a linear space, since it is defined by scaling, and it needs its values to be positive reals. The theory of normed spaces therefore sits in the linear-spaces slot of Part II, not in its foundations. Its algebraic namesake, the quadratic form $Q(x)=B(x,x)$ whose value is an element of the ring or the algebra, needs only the linear space and the form, and it stays in Part I with the theory of forms.
- A **derivative** needs a linear structure and a limit, so it belongs to Part III, and in the linear-spaces slot because the linear structure is what it differentiates. The smooth manifolds and the differential topology that the derivative defines belong to the same part, since a smooth structure is a differentiable one.
- A **Lie group** needs the derivative and the smooth structure, both of which are introduced in Part III, so it is a **further subject** of Part III, at the open end of the ladder and after the calculus. A Lie group is a group that is also a smooth manifold, and a smooth manifold needs the derivative. The Lie-group articles therefore do not sit in the group slot of Analysis, where they would anticipate the calculus; they come further on, once the calculus and the smooth manifolds have been introduced, as *Lie Groups*. Its **Lie algebra**, by contrast, is a module with an alternating bilinear bracket satisfying the Jacobi identity, and that is pure algebra: it stays in Part I. The passage between the two — the exponential map, the correspondence, the adjoint representation — travels with the group, because it is the passage that needs the derivative.
- The **orthogonal and special orthogonal groups** are defined as the transformations preserving a form, and a form is a structure of Part I. They are not group-theory objects. Because they are the motions of a space, read from a chosen form, they belong to Part IV, together with the isometries and the rotations that form generates.
- A **rotation** is not an algebra word. It requires an orientation and a measure, and both require the distance. Rotations belong to Part IV and to the geometry slot of each Part VI system.

The ordering also explains why algebra can be presented, as it is here, with no warning that topology will follow: it is a complete subject on its own. The converse is false, which is the sense in which algebra is more fundamental than topology.

### Rule 3 — A revisited object belongs to the part that revisits it

When a category introduces a new structure, it absorbs every earlier object that is re-read through that structure. Those articles live in the **new** category and never in the old one. The earlier article is not duplicated and is not expanded: it keeps exactly what requires no new structure.

| New structure | Introduced in | Re-reads | Articles it absorbs |
|---|---|---|---|
| Distance | Foundations of Topology | sets | metric, uniform and complete spaces; topological spaces |
| Distance on a group | Topology on Groups | groups | topological groups; abelian topological groups; profinite groups |
| Distance on a ring and field | Topology on Rings and Fields | rings, fields | topological rings and fields; valuations and completions; the $p$-adic numbers |
| Distance on a linear space | Topology on Linear Spaces | linear spaces | topological vector spaces; normed and Banach spaces |
| Distance on a linear algebra | Topology on Algebras | algebras | topological and Banach algebras; operator algebras; Hilbert modules |
| A form and its algebraic norm | Algebras with a degree-2 form; Sesqualgebras with a degree-2 form | groups, linear spaces, Lie algebras | bilinear and quadratic forms; Hermitian forms; the Witt group; Clifford algebras; spinors |
| A topological norm and its distance | Topology on Linear Spaces; Topology on Algebras with a degree-2 form; Topology on Sesqualgebras with a degree-2 form | linear spaces, algebras | normed and Banach spaces; positivity; the completion |
| The derivative and the measure | the whole of Part III | all of the above | differential calculus; smooth manifolds; differential topology; measure; the Haar measure and invariant integration; analytic functions; spectral theory; probability and ergodic theory; the Lie groups |
| A chosen distance | Part IV : Geometry | forms, groups, manifolds | curvature and geodesics; Riemannian, metric, symplectic, Kähler and Calabi–Yau geometry; the isometries and the form-defined classical groups; spin geometry |
| Everything at once | every Part VI category | one system at a time | the whole ladder, per system |

The same object therefore appears at several depths, and that is intended. The quaternion group $Q_8$ is a group. The group of unit quaternions is a Lie group (in *Lie Groups*, Part III). Its representations belong to the representation theory of the algebras (in *Linear Spaces over Algebras*), and its harmonic analysis belongs to the quaternion category of Part VI. Nothing is repeated: each article adds the structure that its category owns.

An important corollary: **an object is not moved merely because a later structure could be placed on it.** The rule applies only when an article actually uses the new structure. The integers are a ring (in *Rings and Fields*) and also, with the discrete distance, a topological group (in *Topology on Groups*) and a locally compact group — but the article on the integers as a ring stays in *Rings and Fields*, because it reasons with the ring structure alone.

**Part V is outside the correspondence.** *Catalogues* is not a layer and carries no new structure: its categories cut across the five slots rather than repeating them, and its articles gather the objects of Parts I to IV into lists without adding to them. It is placed after the four parts, whose objects it lists, and before *Synthetic Studies*.

## The Three Boundaries

The parts are separated by three boundaries. Two of them add a structure; the third changes the intent.

### Algebra and Topology: the distance

The whole ordering turns on one concept. **Distance is the boundary.** Algebra is the theory of objects; topology begins the moment a distance is placed on them. This gives a sharp diagnostic for placing anything:

> If the definition or the proof requires a **length** — a distance, or a norm whose values are positive reals — or a limit, an openness or a neighbourhood, the concept is not algebraic, whatever object it is attached to.

The line runs through single objects, so each case is settled on its own. $GL$ and $SL$ are algebra, since they need no distance; the continuity of a linear map is topology. A determinant is algebra; an operator norm is topology. An inverse limit of rings is algebra, because its limit is an order-theoretic construction and not a topological one. A distance can be defined on a bare set, so the theory of distance needs no algebra beyond sets and the reals; a norm cannot, since it is defined by scaling, so the theory of normed spaces sits in the linear-spaces slot of Part II.

**A form and its algebraic norm are algebra; the topological norm is the boundary.** Three words — *form*, *norm*, *distance* — conceal their layers, so the ruling is stated rung by rung. The chain has five rungs, and the boundary falls at the third.

- A **form** is a bilinear, quadratic or sesquilinear pairing $B$ with values in the ring or in the algebra. It is an algebraic datum: it needs the linear space and the ring, and nothing more.
- Its **algebraic norm** — the quadratic form $Q(x)=B(x,x)$, which in an algebra is the multiplicative norm $N(x)=x x^{\natural}$ — is the same datum read on the diagonal. Its value is an **element**, not a length: the algebraic norm of a biquaternion is a biquaternion. Forms, their quadratic forms, their matrices, their radicals, their discriminants and their signatures, the Witt group, and the Clifford algebras and spinors they generate all belong to **Part I : Algebra**.
- A **topological norm** is the norm **selected** so that its values are positive reals. The selection is the new datum: it asks the ring to be ordered and the norm to be definite. This is the boundary, and the object is now a topological norm.
- A **distance** is built on the topological norm by $\lVert x-y\rVert$: it is a metric on the space, and the open balls it defines are the topology it induces.
- The **limit**, and with it continuity, completeness and compactness, is what the distance supplies.

The same array of scalars can carry either reading, and the test is the **value**: an article that keeps the value an element of the ring or the algebra is algebraic, and an article that asks the value to be a positive real has a topological norm and belongs to Part II. A **form** and its **algebraic norm** therefore belong to **Part I : Algebra**; the **topological norm**, the distance and the limit belong to **Part II : Topology**. The topological norm sits in the linear-spaces slot, *Topology on Linear Spaces*; the topological reading of a form sits in the further subject *Topology on Algebras with a degree-2 form*. An article of Part I may define a form and its algebraic norm and prove anything with them; it may not **select** the norm to be positive, read a length or a unit sphere off a form, or build a distance with one.

**A bare pairing is algebraic, and so is a form.** The operator layer of a category uses a bilinear map $\beta$ on an algebra for one purpose only, to define the **adjoint** of an operator, $\beta(Fx,y)=\beta(x,F^{\dagger}y)$, and no length and no positivity is read off it. Such a **pairing** — nondegenerate, balanced, invariant, or the trace form, used only to take adjoints — is an algebraic datum and is permitted in Part I, in the `- * Operator Theory` groups and in the Lie theory, exactly as the symmetric bilinear Killing form is permitted there. The **form** is admitted on the same terms and further: it may be tabulated, diagonalised, classified by its rank, its radical, its discriminant and its signature, and used to build its Clifford algebra and its spinors, all in Part I, because none of that asks for a length. What is forbidden is the same object read as a **length**: the positive definite norm, the unit sphere, the distance and the limit. The test is the value, not the symbol. An article that reads a positive real off its bilinear map has a topological norm and belongs to Part II; an article that keeps the value in the ring, or only takes adjoints with it, belongs to Part I.

**A Part I article carries no topology, no metric and no analysis layer.** Algebra is the base of the ladder, and an article of it is written with sets, groups, rings and fields, linear spaces, forms and algebras alone; no article of Part I has a section, an appendix or a further subject that is topological, metric or analytic. The `- * Operator Theory` groups are algebraic in every part of their structure: they take adjoints with the pairing above and stop. When a statement needs a length, a positivity or a unit sphere, the article keeps the algebraic statement it can make and defers the enriched one, by forward reference, to the category that owns the structure.

**The determinant stays in Algebra.** Its definition is a polynomial in the entries — an alternating multilinear functional of the columns — and it uses no distance, no limit and no measure, so the determinant is a Part I object, and the group $SL$ that its vanishing defines is Part I's too. The determinant is not read as a volume at this layer: a volume needs a positive definite form to supply the length, and the reading is then Geometry's. The contrast is the one drawn above — a determinant is algebra, an operator norm is topology — and the determinant is the case the boundary is easiest to misdraw, since the same array of scalars can carry either.

### Topology and Analysis: the derivative and the measure

Topology is the theory of the distance and of the limit as a topological notion. Analysis begins when the distance is used **quantitatively** — when a quantity is differentiated or averaged. The two limits of analysis are the derivative, which needs a norm, and the integral, which needs a measure, and neither is supplied by a topology alone. This line also runs through single subjects. A derivative belongs to Analysis, and so does the smooth manifold, a smooth structure being a differentiable one; the local existence and uniqueness of an ordinary differential equation belongs to Analysis with the rest of the calculus. Integration, the $L^p$ spaces, the analytic functions, the distributions, the spectral theory and the ergodic theory belong to Analysis, each because its definition uses a measure or an integral. The same rule settles the measure a **group** carries. A locally compact group is a topological object, so the group is Part II's; but its **Haar measure** is a measure, and no topology supplies one, so the measure — its existence, uniqueness and invariance, the modular function and the homogeneous-space measure — is Analysis, and so is everything built on it. The article *Locally Compact Groups and Haar Measure*, once the last structural article of *Topology on Groups*, therefore opens *Analysis on Groups* in Part III.

### Analysis and Geometry: a change of intent

This line adds no structure, and that is what separates it from the other two: it divides two **intents**, not two layers. Topology and Analysis study the distance as a **tool**; Geometry studies a **chosen** distance as an **object**, with its shape, its symmetries and its figures. The line falls wherever a statement stops holding for every distance and starts depending on the one chosen. A form is a Part I structure, and its isometries are the motions of the space that a chosen form defines, so the form-defined classical groups belong to Geometry. A Riemannian metric is a smoothly varying inner product in Analysis, and geometry once its curvature and its geodesics are read from it. The synthesis of the two — Hodge theory, the index theorem, harmonic maps, the Ricci and mean-curvature flows, the geodesic flow — is geometry's extension, and it is what requires geometry to stand after analysis.

### Geometry is a part, and it is not a layer

Since geometry begins with a distance, and the distance is what Part II introduces, geometry adds no rung to the object ladder. It is the second intent of the layer that owns the distance, and because the distance can be placed on the object of every rung, it is read at every rung: its categories follow the same slots as the spine, from the distance as an object to the synthesis with analysis. It is made a part because it is large, self-contained and asks a different question of the same structure, and it is placed last because the reading uses the derivative and the measure of Analysis: its curvature and its geodesics are differential, and its synthesis with analysis is integral. That is why the geometry articles do not sit with the forms and the Clifford algebras, and why each Part VI system carries a geometry slot.

## Boundary Tests

The three boundaries give a set of tests. Each test is **local**: it is applied to one definition or one proof at a time, not to an article as a whole. Each is also a test of what a part may **not** use. A part may use everything introduced below it and nothing introduced above it, and the tests state that restriction structure by structure.

The tests govern what a part may **reason with**, not what it may **name**. An article may name a structure introduced later, as a forward reference, and it may carry the vocabulary of a later part in a sense that is already available; what it may not do is define or prove anything with a structure that its part has not introduced.

### The test for Part I : Algebra

A statement belongs to Algebra only if its definition and its proof can be written without any of the following. If one of them is needed, the subject belongs to a later part, and the bracket names where.

> **nothing topological** — distance, metric, **topological norm (a norm selected to take positive real values)**, length, uniform structure, ball, open set, closed set, neighbourhood, continuity, convergence, limit, completeness, compactness, a positive definiteness, a unit sphere — *a form and its algebraic norm, whose values lie in the ring or the algebra, are algebraic; a bare pairing, taken only to define an adjoint, is algebraic too* [Part II];
> **nothing analytic** — derivative, differentiability, smooth structure, atlas, tangent space, smooth manifold, differential form, measure, integral, $L^p$ space, probability [Part III];
> **nothing geometric** — a chosen distance or form read as an object: curvature, geodesic, the motion of a chosen distance, rotation, angle, figure — *the isometry of a form, read as the solution set of $B(Tx,Ty)=B(x,y)$, is algebraic and stays in Part I; what is geometric is the motion of the chosen distance* [Part IV].

**A form and its algebraic norm are algebra; the topological norm is topology.** A Part I article may define a form, tabulate it, take its quadratic form, its matrix, its rank, its radical, its discriminant and its signature, and build its Clifford algebra and its spinors: none of that asks for a length. What it may not do is **select** the norm so that its values are positive reals, read a length or a unit sphere off a form, or build a distance. The **topological norm** is *Topology on Linear Spaces*, and the topological reading of a form is *Topology on Algebras with a degree-2 form*; the form itself, and its algebraic norm, are **Part I**. **A bare pairing is algebraic too**, and the distinction is the point of the test: the `- * Operator Theory` articles and the Lie theory take adjoints with respect to a bilinear map, and that use is algebraic. The moment the same map is asked for a **length** — a positive real, a distance, a unit sphere — it has become a topological norm and the subject moves to Topology.

The same boundary governs the **inner product**. In Part I an inner product may be formed, evaluated to a scalar and split into its symmetric and antisymmetric parts — $\langle x,y\rangle$, its vanishing, its nondegeneracy, its orthogonality $\langle x,y\rangle=0$ — but nothing may be measured with it: no length and no positive definiteness, and no orthonormal decomposition.

**The isometry of a form, and the Clifford theory built on it, are algebra.** The word *isometry* names an equation, not a distance, and the same test settles the whole cluster. A Part I article may carry, with no distance anywhere:

- the **orthogonality** of two vectors, $B(x,y)=0$;
- the **reflection** in the hyperplane orthogonal to a non-isotropic vector, $x\mapsto x-2B(x,a)B(a,a)^{-1}a$;
- the **isometry group** of the form, defined as the set of solutions of $B(Tx,Ty)=B(x,y)$ — a system of polynomial equations over the ring, so the group is an algebraic group and a Part I object;
- $\mathrm{SO}$ as the determinant-one part of that set;
- the **versors**, the rotors and the sandwich $x\mapsto uxu^{-1}$, with $\mathrm{Pin}$ and $\mathrm{Spin}$ as subgroups of the Clifford algebra;
- the group statement $\ker(\mathrm{Spin}\to\mathrm{SO})=\{\pm1\}$, which is a computation inside the Clifford algebra.

The isometry group is defined by an equation, so it is neither Geometry nor Topology. Its reading as the **motions** of a metric space is the Geometry reading, taken up when a definite form is chosen and a distance is built on it; the group itself is Part I's.

What a Part I article may **not** carry, in the same subject, is the other half of the vocabulary:

- a **rotation through an angle** — the angle is read from the definite form, the unit sphere and the arc, so it is Geometry [Part IV];
- the **exponential** $\exp(B)=\sum_k B^k/k!$ and the exponential map — the series asks for convergence, hence for a limit and a topological norm, so the exponential map is Analysis [Part III];
- the **unit sphere**, the unit ball, and the **compactness** of $\mathrm{SO}(n)$ — each asks for the positive-real norm and the distance, so they are Topology [Part II];
- the **double cover as a covering space**, the connected components and the universal cover — a covering space is a topological map, so the cover is Topology, while the group-theoretic statement $\ker(\mathrm{Spin}\to\mathrm{SO})=\{\pm1\}$ stays in Part I;
- the **Lie group structure**, the smooth action and the **Poisson bracket** — a smooth structure needs the derivative, so each is Analysis [Part III].

The test is what the article *Automorphisms and Derivations of Algebras* states in its own words: an algebra automorphism preserves no length, angle or volume, because none is available at that layer, and the identification of $\operatorname{Inn}(\mathbb{H})$ with a rotation group is made in Part IV.

### The test for Part II : Topology

Topology is the layer of the distance, so it may use the **topological norm** — a norm selected so that its values are positive reals — and the distance built on it, the topology that distance generates, and every notion defined by them — balls, open and closed sets, neighbourhoods, continuity, convergence, limits, completeness, compactness, uniform structures. The form itself is a Part I structure, but its **topological reading** — the selection of a positive definite norm, the positivity, the completion — is topology's. What it may not use is everything above.

**The Hermitian layer is split in the same way.** An involution of the algebra and a Hermitian form tied to the product by the adjoint axiom — $\langle xy,z\rangle=\langle y,x^{\dagger}z\rangle$ — are Part I: the correspondence $\langle x,y\rangle=\langle x^{\dagger}y,1\rangle$, the adjoint of a multiplication, the Hermitian sandwich $\Theta_x(y)=xyx^{\dagger}$, the unitary slice and the isometry group of the form are algebraic, and they are the content of *Hermitian Algebras* and of the four operator groups of `Sesqualgebras with a degree-2 form`. What is Part II is the **positiveness** of the form — the cone $\{\sum_i x_i^{\dagger}x_i\}$, the Cauchy–Schwarz inequality, the norm read from the diagonal and the completion — and the operator algebras built on the completion: the Hilbert algebra, the Krein space, the GNS construction, the modular operator and the Von Neumann completeness.

> **nothing analytic** — derivative, differentiability, smooth structure, atlas, tangent space, smooth manifold, differential form, measure, integral, $L^p$ space, probability [Part III];
> **nothing geometric** — a chosen distance or form read as an object: its curvature, its geodesics, its isometries, its rotations, its figures [Part IV].

The two cases the corpus settles with this test are the smooth manifold and the Lie group: both need the derivative, so neither is topology, and both sit in Part III. A manifold that carries no smooth structure needs no derivative and is not excluded by the test.

A third case is the **measure a topological group carries**. A locally compact group is a topological object and is Part II's, so an article may name the Haar measure, quote its invariance and integrate over the group in that cited sense; but a measure is on the forbidden list, so the measure itself — its construction, its uniqueness, the modular function, the homogeneous-space measure and Weil's formula — is Part III's, and an article of Part II may not construct it or prove anything with it. This is the ruling of the corpus, and it is why *Locally Compact Groups and Haar Measure* is the opening article of Part III's *Analysis on Groups*, while the locally compact group as a topological object remains a Part II notion, read in *Topological Groups*.

### The test for Part III : Analysis

Analysis may use everything in Algebra and Topology, and adds the derivative and the measure. Nothing below it is forbidden; its one boundary is with Geometry, and that boundary is one of intent rather than of structure.

> A statement that uses a distance **as a tool** — to differentiate, to integrate, to measure, to take a limit — belongs to Analysis. A statement that treats a **chosen** distance or form as its object — its curvature, its geodesics, its isometries, its figures — belongs to Geometry.

The Riemannian metric is the standard case: introduced as a smoothly varying inner product on each tangent space, it is analysis; the curvature and the geodesics read from it are geometry.

### The test for Part IV : Geometry

Geometry has the reverse test. A statement belongs to Geometry only if it depends on a **chosen** distance or form.

> If the statement holds for every distance on the object, it is topology or analysis and not geometry. If it holds for the distance chosen, it is geometry.

A theorem about all topological spaces is topology; a theorem about the geometry of one metric is geometry. The forms and the classical groups they define are the test at its sharpest: a form is a Part I structure, while the isometries the form defines are the motions of the space it defines, and the motions belong to Geometry.

For the same reason the *Automorphisms and Derivations* article of a system sits in that system's Geometry slot: the automorphism group and its derivation space are read as the symmetries of the algebra — its motions — which is the geometric intent even when only algebraic tools are used, so the placement stands for the real system too, where both invariants are trivial, the triviality being a result and not a change of subject.

### The tests for Parts V and VI

The last two parts are not layers, and their tests are different in kind.

- **Part V : Catalogues.** A catalogue introduces no structure and proves no theorem, so its test is not what it may use but what it may do: it names an object and points to the article that introduces it. It may name anything from any part, because naming a structure is not using it.
- **Part VI : Synthetic Studies.** A system article may use the whole ladder, because it is written once the ladder is complete. Its test is not the layer but the **system**: it may use any part, but only for the one system it treats.

### Quick reference

| If the candidate needs | It belongs to |
|---|---|
| nothing beyond sets, groups, rings, fields, linear spaces, forms and algebras | Part I : Algebra |
| a topological norm — a norm selected to take positive real values — a length or a distance, and nothing above | Part II : Topology |
| the derivative, the smooth structure, a measure or an integral | Part III : Analysis |
| a chosen distance or form read as an object — its shape, its motions or its figures | Part IV : Geometry |
| nothing of its own; names and pointers only | Part V : Catalogues |
| the whole ladder, applied to one system at a time | Part VI : Synthetic Studies |

## The Synthetic Progression

Parts I to IV are general: each category is about a structure, and the objects of that category are whatever satisfies it. Part V is transversal: its categories cut across the four, and each of its articles lists the objects of one kind. Part VI is concrete: each category is a single system, and the article slots are the parts of the general theory applied to that system. The slots recur across the systems:

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

## Learning Mathematics

The order of the parts is an order of **dependency**, not an order of **study**. Rule 2 fixes what may be built on what; it does not say that the whole of Algebra must be read before Topology is opened. A subject is placed where its prerequisites first exist, and the placement is exact — but a reader needs only *enough* of a prerequisite to enter the next part, not all of it. The corpus is meant to be learnt by **successive paths**.

A path runs through the six parts at one depth, in the order the parts are given, and then the reader returns to the beginning and runs the same path again, a level deeper. Each pass is a cycle:

> basic Algebra → basic Topology → basic Analysis → basic Geometry → a first Catalogue → a first Synthetic study → and then the second cycle, deeper than the first.

The first cycle uses the most basic entry of each part: Algebra through sets, groups, rings and fields, linear spaces and algebras; Topology through the distance itself, that is the metric, uniform and complete spaces; Analysis through the derivative and the measure and the calculus they give, including the calculus of curves and surfaces; Geometry through the distance read as an object, that is shape and metric geometry; a Catalogue as a first list of one kind of object; and the Synthetic study of the natural numbers, the smallest system that exercises the whole ladder. That cycle gives the shape of the corpus. It does not finish any part, and it is not meant to.

The geometry column follows the same ladder as the rest, so each cycle reaches the geometry of the rung it has climbed: the distance as an object at the bottom, then the motions and the figures, then the settings, the structured spaces and the geometries an algebra defines, and the synthesis with analysis at the top.

| Cycle | Algebra | Topology | Analysis | Geometry | Catalogue | Synthetic study |
|---|---|---|---|---|---|---|
| First | sets, groups, rings and fields, linear spaces, algebras | the distance; metric, uniform and complete spaces | the derivative and the measure; the calculus of curves and surfaces | *Foundations of Geometry*: the distance, the length, the geodesics | a first list, one kind of object | $\mathbb{N}$ |
| Second | the spine in full: modules, tensor and exterior algebras, Galois theory, representation, forms and Clifford algebras | general topological spaces, compactness and completeness, the topological norm and the completion | smooth manifolds, differential forms, integration, spectral theory, differential equations | *Geometry on Groups* and *Geometry on Rings and Fields*: the isometry group of a form; Euclidean, spherical and hyperbolic geometry | the full catalogue | $\mathbb{Z}$, $\mathbb{Q}$ |
| Third | homological algebra, operads, differential graded categories, the non-associative algebras | algebraic topology, sheaves and cohomology, algebraic geometry, geometric topology | functional analysis, operator algebras, noncommutative analysis, the dynamical systems | *Geometry on Linear Spaces* and *Geometry on Algebras*: symplectic and Kähler geometry, spin geometry; the synthesis with analysis | re-read against the parts in full | $\mathbb{R}$, $\mathbb{C}$ |

Further cycles continue in the same way, through the systems that remain, to the octonions.

**Why a path and not a part at a time.** The corpus is built so that each layer adds exactly one structure, and the same object therefore appears at every depth. A first cycle shows an object at one depth; a later cycle re-reads it with more structure around it. The recurrence is the point: *distance* is crossed early, with metric spaces, and returns in general topology; a *group* is crossed as a group, and returns as a topological group, a Lie group and a symmetry. Reading a whole part to the end before opening the next hides that recurrence and delays the crossing that gives the corpus its shape.

**A cycle is complete when all six parts have been entered**, not when any one of them is finished. The synthetic study closes the cycle, because a system exercises the whole ladder at once and shows where the ladder stops for that system: $\mathbb{N}$ supports an algebra and a topology but no analysis, and the corpus says so. Later cycles carry a richer system, and the stopping point moves.

**The depth is carried by the ladder, not by the cycle count.** Within a cycle the reader advances up the spine as far as the time allows, and the next cycle begins one rung deeper. Nothing forces a cycle to exhaust a part; what it must do is enter every part and leave the ladder one rung higher than it found it.

## Pure Mathematics

The corpus is pure mathematics. It is an account of mathematical structures and of nothing else, and it admits no article about an application of mathematics. Numerical analysis, the finite element and boundary element methods, control theory, signal and image processing, computer graphics, robotics, computer vision, cryptography as an engineering subject, mathematical finance, mathematical biology and operations research do not belong to it, and no title in it begins *Applications of …*.

The reason is the one that governs the order of the parts. An application is a place where a structure is used, and the use is not a property of the structure. Where the applied subject meets the mathematics it brings constraints of its own — accuracy, cost, numerical stability, real time — and those constraints are not mathematical. The corpus stops at the structure. A reader who wants the applications will find them in the literature of the applied subject, where the mathematics is the instrument and the application is the point.

A concept that is mathematics but is named after its use is admitted on the same terms as one named from physics, and then only for its mathematical content. Convex optimisation is the study of a convex function and a convex set, and is mathematics; the simplex method is an algorithm for computing with them, and is not an article here. The algebra of a finite field and the arithmetic of an elliptic curve are mathematics; the engineering of a channel or of a protocol that uses them is not.

The word *application* occurs in the menu in a second sense, and the two must not be confused. The slot named *Applications* inside a category of Parts I to IV means the concrete instances of the structure of that category — under Groups, under Algebras, under the Integers. Those are examples, and examples are mathematics. What the corpus excludes is not the example but the use.

The exclusion of physics, stated in the next section, is the sharpest case of the same rule: a physical theory uses mathematics, and the corpus keeps the mathematics and not the theory. Nothing about the origin of a concept decides whether it is admitted. What decides is whether its mathematical content stands on its own.

## No Physics in the Mathematical Corpus

The mathematical corpus contains no article about a physical theory. There is no time in it, no measurement, no experimental input, no observable, and no interpretation. The physics corpus is a separate body of articles with its own menu, and the two are not mixed.

The rule is not that mathematical concepts with a physical origin are forbidden. It is that the **mathematical content must be autonomous**. Where a concept was named first in physics and is by now an ordinary mathematical object, the name may be kept, provided everything physical about it is dropped.

The clearest case is the **Lorentz group**. The Lorentz group is the group of linear transformations preserving a quadratic form of signature $(3,1)$. That is a complete definition in pure algebra, and the group is treated as such: its structure, its subgroups, its one-parameter subgroups and its relation to the split-biquaternions are ordinary mathematics. What the corpus does not write is *spacetime*, *the speed of light*, *an observer*, *a clock* or *a measurement*.

The same discipline applies to vocabulary that carries a physical flavour more strongly than its mathematical content. Where a mathematical synonym exists it is preferred: a **hyperbolic rotation** rather than a *boost*, the **null cone of a quadratic form** rather than a *light cone*, and **signature** rather than any metrical vocabulary from relativity. A reader coming from physics will recognise these objects; the corpus describes them as the algebra and the geometry that they are.

Where a physical interpretation exists and is worth stating, it belongs to the physics corpus. The mathematical article says so with a forward reference and stops.

## Summary

The mathematical corpus is organised in six parts. Part I, Algebra, builds the objects — sets, groups, rings and fields, linear spaces, algebras — and carries the **form** and its **algebraic norm**, whose values lie in the ring or the algebra; what it lacks is a **length**, that is a norm selected to take positive real values. Part II, Topology, makes that selection — the **topological norm** — and places the distance it defines on each object of Part I in turn, with *Topology on Linear Spaces* for the norm and *Topology on Algebras with a degree-2 form* for the topological reading of a form, together with the algebraic topology, the sheaves and the algebraic geometry built on its cohomology. Part III, Analysis, uses the derivative and the measure that the distance supplies — the differential calculus, the smooth manifolds and the differential topology, the Lie groups, the integration, the analytic functions, the spectral theory, the differential equations, and the probability, the ergodic theory and the dynamical systems that only a limit can define. Part IV, Geometry, reads the distance as an object rather than as a tool: its shape, its motions, its figures and its settings, and its synthesis with analysis in Hodge theory, the index theorem and the geometric flows. Part V, Catalogues, gathers the objects of Parts I to IV into transversal lists, one kind of object per article, naming each object and pointing to the articles that introduce it without introducing or proving anything. Part VI, Synthetic Studies, re-traverses the whole ladder one system at a time, from the Booleans to the octonions.

Parts I to III share one five-slot spine — Foundations, Groups, Rings and Fields, Linear Spaces, Algebras — and each part adds its own further subjects after them. The spine follows the object ladder, in which each layer adds exactly one structure to the layer above. Geometry is not a layer and adds no structure, but the distance can be placed on the object of every rung, so geometry is read at every rung and its categories follow the same slots in the same order — *Foundations of Geometry*, *Geometry on Groups*, *Geometry on Rings and Fields*, *Geometry on Linear Spaces*, *Geometry on Algebras* — closing with its further subject, *Synthesis of Geometry and Analysis*.

The order of the parts is an order of dependency, not an order of study. The corpus is learnt by **successive paths**: a cycle runs through the six parts at one depth — basic Algebra, basic Topology, basic Analysis, basic Geometry, a first catalogue and a first synthetic study, the natural numbers — and then the reader returns to the beginning and runs the same path one rung deeper.

Three rules fix the placement of every article. No category may use a structure it has not yet introduced, and no article may use a concept — an example included, since an example is a use — that a later article introduces. The parts are strictly ordered, and algebra, which needs no distance, is the most fundamental. And an object re-read through a new structure belongs to the new category, not the old one: the Lie groups are further subjects of Analysis, placed after the calculus they need, and the isometries and the form-defined classical groups are geometry articles, once a form is read as a motion.

The catalogues of Part V obey a rule of their own. A catalogue names an object and points to the articles that introduce it; it introduces nothing and it proves nothing. The one condition on what it may list is that the object has been introduced somewhere in Parts I to IV, whether or not an article is devoted to it.

Distance is the boundary between algebra and topology, and the diagnostic for placing anything: a **form** and its **algebraic norm**, whose value is an element, belong to Algebra, and the concept turns topological the moment the norm is **selected** to take positive real values and a length or a distance is asked of it. The derivative and the measure are the boundary between topology and analysis. A change of intent is the boundary between analysis and geometry: topology and analysis study the distance as a tool, geometry studies a chosen distance as an object — its shape, its symmetries and its figures — with the topological norm and the distance in topology and the transformations a chosen form defines in geometry. Each boundary gives a local test of what a part may not use, and the tests are collected in *Boundary Tests*: nothing topological in Algebra, nothing analytic in Topology, and, in Geometry, the reverse requirement that the statement depend on the distance chosen. The tests govern what a part may reason with, not what it may name.

The corpus is pure mathematics. No article is about an application of mathematics — no numerical analysis, computer graphics, robotics or cryptography — and no article is about a physical theory. A concept is kept only where its mathematical content is autonomous, whatever its origin, and it is then stripped of every reference to an application, to physics, to time and to measurement.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| Part I, II, III, IV, V, VI | Algebra, Topology, Analysis, Geometry, Catalogues, Synthetic Studies |
| Foundations, Groups, Rings and Fields, Linear Spaces, Algebras, Further subjects | the five-slot spine shared by Parts I to III, and the further subjects each part adds after it |
| Rule 1 | no part may use a structure it has not yet introduced, and no article may use a concept — an example included — that a later article introduces |
| Rule 2 | the parts are strictly ordered; algebra is the most fundamental |
| Rule 3 | a revisited object belongs to the part that revisits it |
| Boundary Tests | the local tests of what a part may not use: nothing topological in Part I — no length, no distance, no positive definiteness — nothing analytic in Part II, a chosen distance in Part III, and the reverse test for Part IV; they bind what a part reasons with, not what it names |
| Successive paths | the reading method: a cycle through the six parts at one depth — basic Algebra, basic Topology, basic Analysis, basic Geometry, a first Catalogue, a first Synthetic study ($\mathbb{N}$) — and then the next cycle one rung deeper |

## Further Reading

- Nicolas Bourbaki, *Éléments de mathématique* (Hermann, then Springer). The model for treating algebra, topology and analysis as separate and strictly ordered bodies of theory.
- Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed. (Springer, 1998). Universal properties and the language of the Foundations slot of Part I.
- Felix Klein, *Vergleichende Betrachtungen über neuere geometrische Forschungen* (Erlangen, 1872). The programme that defines a geometry by its transformation group, which is the organising idea of Part IV.
- Hermann Weyl, *The Classical Groups: Their Invariants and Representations* (Princeton, 1939). The forms first, the groups they define second.
- John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed. (Springer, 2013). Manifolds, bundles and curvature, for the differential topology of Part III and the geometry of Part IV.
- James R. Munkres, *Topology*, 2nd ed. (Prentice Hall, 2000). Metric and topological spaces, and metrisation.
- Serge Lang, *Algebra*, 3rd ed. (Springer, 2002). The reference for the object ladder of Part I.
- Michael Artin, *Algebra*, 2nd ed. (Pearson, 2011). An account in which the examples precede the general theory.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991). The representations that recur in the Part VI slots.
- John C. Baez, "The Octonions", *Bulletin of the American Mathematical Society* 39 (2002), 145–205. The chain of real division algebras that ends the ladder of the number systems.
